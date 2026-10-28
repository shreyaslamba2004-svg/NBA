"""Compare the simulation against every offered price, with bookmaker margin removed.

Every source is normalised to "offers": one row per (book, market, selection, line, price).
For each offer we report
  model_prob        probability from the 20k-run simulation
  book_novig_prob   that book's own price with its margin removed (over/under or home/away
                    pair at the same line; one-sided markets use a typical margin)
  market_novig_prob median of the no-vig probabilities across all books for the same bet
  ev                expected profit per 1 unit staked, at the actual offered price (pure model)
  blend_prob        model blended with the no-vig market (BLEND_W_*), used for bet decisions
  ev_blend          expected profit at the offered price using blend_prob
  kelly_25          quarter-Kelly stake from blend_prob (fraction of bankroll)
  check_news        model and market disagree by more than CHECK_GAP: usually the model is
                    missing news (late scratch, minutes limit), not a real edge
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .odds import american_to_decimal, american_to_prob, edge, kelly, prob_to_decimal

CHECK_GAP = 0.15
BLEND_W_GAME = 0.35   # weight on the model vs no-vig market for sides/totals (to be refit in backtests)
BLEND_W_PROPS = 0.25  # props: model spread vs book spread not yet validated (refit from logged results)
ONE_SIDED_MARGIN = 1.07  # typical overround on milestone / alt props without an opposite side


def offers_from_espn_lines(game_id: int, home: str, away: str, ln: dict) -> pd.DataFrame:
    """DraftKings game lines as carried by ESPN."""
    book = (ln.get("book") or "draftkings").lower()
    rows = []
    if pd.notna(ln.get("ml_home")) and pd.notna(ln.get("ml_away")):
        rows += [("moneyline", home, None, ln["ml_home"]), ("moneyline", away, None, ln["ml_away"])]
    if pd.notna(ln.get("spread_home")):
        rows += [("spread", home, ln["spread_home"], ln.get("spread_home_price") or -110),
                 ("spread", away, -ln["spread_home"], ln.get("spread_away_price") or -110)]
    if pd.notna(ln.get("total")):
        rows += [("total", "over", ln["total"], ln.get("over_price") or -110),
                 ("total", "under", ln["total"], ln.get("under_price") or -110)]
    return pd.DataFrame([{"game_id": game_id, "book": book, "market": m, "selection": s, "line": l,
                          "price": float(p), "player_id": None, "paired": True} for m, s, l, p in rows])


def offers_from_odds_api(game_id: int, books: pd.DataFrame) -> pd.DataFrame:
    """The Odds API game lines (live.odds_games rows for one event)."""
    mk = {"h2h": "moneyline", "spreads": "spread", "totals": "total"}
    d = books.assign(game_id=game_id, market=books["market"].map(mk),
                     selection=books["side"].astype(str).str.lower().where(books["market"] == "totals", books["side"]),
                     player_id=None, paired=True)
    d.loc[d["market"] == "moneyline", "line"] = None
    return d[["game_id", "book", "market", "selection", "line", "price", "player_id", "paired"]]


def offers_from_props(props: pd.DataFrame) -> pd.DataFrame:
    d = props.copy()
    d["market"] = "prop_" + d["stat"].astype(str)
    d["selection"] = d["side"].str.lower()
    # milestones ("15+") have no opposite side to de-vig against
    d["paired"] = props["market"] != "milestone" if "market" in props else True
    return d[["game_id", "book", "market", "selection", "line", "price", "player_id", "paired"]]


def _model_prob(sim: dict, home: str, market: str, selection, line, player_id) -> float:
    if market == "moneyline":
        p = (sim["margin"] > 0).mean()
        return float(p if selection == home else 1 - p)
    if market == "spread":
        m = sim["margin"] if selection == home else -sim["margin"]
        return float((m + line > 0).mean())
    if market == "total":
        t = sim["total"]
        return float((t > line).mean() if selection == "over" else (t < line).mean())
    stat = market[5:]
    for pl in sim["players"]:
        if pl["player_id"] == player_id:
            x = pl["draws"][stat][pl["draws"]["min"] > 0]
            if len(x) == 0:
                return float("nan")
            return float((x > line).mean() if selection == "over" else (x < line).mean())
    return float("nan")


def _s(x: pd.Series) -> pd.Series:
    """String key that keeps missing values as text (pandas' str dtype would turn the whole key NaN)."""
    return x.astype(object).map(str)


def evaluate(sim: dict, home: str, offers: pd.DataFrame, labels: dict | None = None) -> pd.DataFrame:
    if offers is None or offers.empty:
        return pd.DataFrame()
    o = offers.dropna(subset=["price"]).copy()
    o["book"] = o["book"].astype(str).str.lower().str.replace(" ", "", regex=False)
    o["implied"] = american_to_prob(o["price"].astype(float))
    # pair each offer with the opposite side at the same book/market/line/player
    o["pkey"] = (_s(o["book"]) + "|" + _s(o["market"]) + "|" + _s(o["line"].astype(float).abs()) + "|" +
                 _s(o["player_id"]))
    tot = o.groupby("pkey")["implied"].transform("sum")
    n = o.groupby("pkey")["implied"].transform("size")
    o["book_novig_prob"] = np.where((n == 2) & o["paired"].astype(bool), o["implied"] / tot,
                                    o["implied"] / ONE_SIDED_MARGIN)
    o["book_margin_pct"] = np.where(n == 2, 100 * (tot - 1), np.nan)
    bkey = _s(o["market"]) + "|" + _s(o["selection"]) + "|" + _s(o["line"]) + "|" + _s(o["player_id"])
    o["market_novig_prob"] = o.groupby(bkey)["book_novig_prob"].transform("median")
    o["model_prob"] = [_model_prob(sim, home, r.market, r.selection, r.line, r.player_id) for r in o.itertuples()]
    o = o.dropna(subset=["model_prob"])
    o["ev"] = edge(o["model_prob"], o["price"].astype(float))
    # The backtest shows closing lines beat the pure model on game markets, so bet decisions use a
    # blend that leans on the no-vig market. The pure model stays in model_prob / ev.
    w = np.where(o["market"].str.startswith("prop_"), BLEND_W_PROPS, BLEND_W_GAME)
    mk = o["market_novig_prob"].astype(float)
    o["blend_prob"] = np.where(mk.notna(), w * o["model_prob"] + (1 - w) * mk, o["model_prob"])
    o["ev_blend"] = edge(o["blend_prob"], o["price"].astype(float))
    o["kelly_25"] = kelly(o["blend_prob"], o["price"].astype(float))
    o["price_decimal"] = american_to_decimal(o["price"].astype(float))
    o["fair_decimal"] = prob_to_decimal(o["model_prob"])
    o["model_minus_market"] = o["model_prob"] - o["market_novig_prob"]
    o["check_news"] = o["model_minus_market"].abs() > CHECK_GAP
    if labels:
        o["player"] = o["player_id"].map(labels)
    cols = ["game_id", "market", "selection", "player", "player_id", "line", "book", "price", "price_decimal",
            "model_prob", "fair_decimal", "book_novig_prob", "market_novig_prob", "model_minus_market",
            "book_margin_pct", "ev", "blend_prob", "ev_blend", "kelly_25", "check_news"]
    o = o.reindex(columns=cols)
    for c in ("price_decimal", "fair_decimal", "book_margin_pct"):
        o[c] = o[c].astype(float).round(2)
    for c in ("model_prob", "book_novig_prob", "market_novig_prob", "model_minus_market", "ev", "blend_prob", "ev_blend", "kelly_25"):
        o[c] = o[c].astype(float).round(4)
    return o
