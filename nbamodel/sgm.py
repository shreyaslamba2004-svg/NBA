"""Same-game multis priced from the joint simulation.

Every simulated game carries the final score and every player's line together, so the
probability that ALL legs land is just the share of simulations where they all do. That
captures correlation (star points + team win, PG assists + C points, overs together) that
multiplying single-leg prices ignores.

Bookmakers price SGMs with their own correlation model and margin, and no API exposes AU
SGM prices. So for each suggested multi we report the model's fair odds and the minimum
price worth taking; `check()` evaluates a price a bookie actually quotes.
"""
from __future__ import annotations

import itertools
import re

import numpy as np
import pandas as pd

from .edges import blend_weights
from .odds import american_to_decimal

MIN_LEG_PROB = 0.30
MAX_LEG_ODDS = 4.0  # long-shot milestone tails aren't validated yet
MIN_PRICE = 1.5     # whole multi priced between these (legs multiplied, a stand-in for the bookie's quote)
MAX_PRICE = 2.5
BANDS = [(1.50, 1.65), (1.65, 1.85), (1.85, 2.10), (2.10, 2.50)]
PER_BAND = 3        # kept per game and price band
MAX_LEGS_SEARCH = 16  # best-value legs searched
SAFE_LEGS = 10        # plus this many high-probability legs (e.g. 10+ points) close to fair price
SAFE_PROB, SAFE_MIN_EV = 0.75, -0.06
MIN_SHOWN_EV = -0.15  # at multiplied leg prices
MIN_EDGE = 0.05  # "min price worth taking" = fair odds x (1 + MIN_EDGE)


def leg_mask(sim: dict, home: str, away: str, market: str, selection: str, line, player_id=None):
    """Boolean array over simulations: did this leg win? Player legs need the player to play."""
    if market == "moneyline":
        return sim["margin"] > 0 if selection == home else sim["margin"] < 0
    if market == "spread":
        m = sim["margin"] if selection == home else -sim["margin"]
        return m + float(line) > 0
    if market == "total":
        return sim["total"] > float(line) if selection == "over" else sim["total"] < float(line)
    if market == "team_total":
        pts = sim["home_pts"] if selection.split()[0] == home else sim["away_pts"]
        return pts > float(line) if selection.endswith("over") else pts < float(line)
    stat = market[5:]
    for p in sim["players"]:
        if p["player_id"] == player_id:
            x, played = p["draws"][stat], p["draws"]["min"] > 0
            return played & ((x > float(line)) if selection == "over" else (x < float(line)))
    return None


def played_mask(sim: dict, player_id=None) -> np.ndarray:
    """Simulations where the leg's player got on court (all of them for game legs). A player who
    doesn't play voids his leg at the bookie, so multis are priced given every leg player plays."""
    n = len(sim["margin"])
    if player_id is None or pd.isna(player_id):
        return np.ones(n, dtype=bool)
    for p in sim["players"]:
        if p["player_id"] == player_id:
            return p["draws"]["min"] > 0
    return np.ones(n, dtype=bool)


def _conflict(a: dict, b: dict) -> bool:
    if a.get("player_id") is not None and pd.notna(a.get("player_id")) and a.get("player_id") == b.get("player_id"):
        return True  # one leg per player: stacked stats of one player are near-duplicates books price as such
    if a["market"] == b["market"] and a.get("player_id") == b.get("player_id"):
        return True  # same market twice (both sides, or two lines of one stat)
    game_side = {"moneyline", "spread"}
    return a["market"] in game_side and b["market"] in game_side


def suggest(sim: dict, home: str, away: str, offers: pd.DataFrame, labels: dict,
            max_legs: int = 4) -> pd.DataFrame:
    """Rank 2..max_legs leg combos by edge of the model's joint probability over the price
    you'd get if the bookie simply multiplied its single-leg prices (best offered price per leg).
    Keeps the best PER_BAND in each price band. The leg pool mixes the best-value legs with
    near-fair "safe" legs (milestones like 10+ points) so low-priced multis can be built too."""
    if offers is None or offers.empty:
        return pd.DataFrame()
    o = offers.dropna(subset=["price"]).copy()
    o["dec"] = american_to_decimal(o["price"].astype(float))
    o = o.sort_values("dec", ascending=False).drop_duplicates(["market", "selection", "line", "player_id"])
    legs, bw = [], blend_weights()
    for r in o.itertuples():
        m = leg_mask(sim, home, away, r.market, r.selection, r.line, r.player_id)
        if m is None:
            continue
        pl = played_mask(sim, r.player_id if r.market.startswith("prop_") else None)
        if not pl.any():
            continue
        p = m.sum() / pl.sum()  # given he plays
        if p < MIN_LEG_PROB or r.dec > min(MAX_LEG_ODDS, MAX_PRICE / 1.2):
            continue
        # lean on the no-vig market the same way single bets do; correlation still comes from the sim
        mk = getattr(r, "market_novig_prob", np.nan)
        w = bw["props"] if r.market.startswith("prop_") else bw.get(r.market, bw["game"])
        pb = w * p + (1 - w) * mk if pd.notna(mk) else p
        legs.append({"market": r.market, "selection": r.selection, "line": r.line, "player_id": r.player_id,
                     "dec": r.dec, "p": p, "pb": pb, "mask": m, "pl": pl, "ev": pb * r.dec - 1,
                     "label": _label(r.market, r.selection, r.line, labels.get(r.player_id))})
    # keep the most promising legs to bound the search, plus the best "safe" legs
    legs = sorted(legs, key=lambda x: x["ev"], reverse=True)
    safe = [l for l in legs[MAX_LEGS_SEARCH:] if l["pb"] >= SAFE_PROB and l["ev"] >= SAFE_MIN_EV][:SAFE_LEGS]
    legs = legs[:MAX_LEGS_SEARCH] + safe
    packed = [np.packbits(l["mask"]) for l in legs]
    packed_pl = [np.packbits(l["pl"]) for l in legs]
    n = len(legs[0]["mask"]) if legs else 0
    rows = []
    for k in range(2, max_legs + 1):
        for combo in itertools.combinations(range(len(legs)), k):
            if any(_conflict(legs[i], legs[j]) for i, j in itertools.combinations(combo, 2)):
                continue
            acc, accp = packed[combo[0]], packed_pl[combo[0]]
            for i in combo[1:]:
                acc, accp = acc & packed[i], accp & packed_pl[i]
            n_pl = np.unpackbits(accp)[:n].sum()
            if n_pl == 0:
                continue
            joint_model = np.unpackbits(acc)[:n].sum() / n_pl  # given every leg player plays
            if joint_model <= 0:
                continue
            # blended joint: keep the sim's correlation, scale each leg to its blended probability
            joint = min(1.0, joint_model * float(np.prod([legs[i]["pb"] / legs[i]["p"] for i in combo])))
            naive_price = float(np.prod([legs[i]["dec"] for i in combo]))
            if not MIN_PRICE <= naive_price <= MAX_PRICE:
                continue
            indep = float(np.prod([legs[i]["p"] for i in combo]))
            rows.append({"legs": " + ".join(legs[i]["label"] for i in combo), "n_legs": k,
                         "model_only_prob": joint_model, "model_prob": joint, "fair_odds": 1 / joint,
                         "min_price_worth_taking": (1 / joint) * (1 + MIN_EDGE),
                         "multiplied_leg_prices": naive_price,
                         "ev_at_multiplied_prices": joint * naive_price - 1,
                         "correlation_lift": joint_model / indep})
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    # near-fair multis are kept too: the sheet shows the minimum price worth taking, which is what to
    # compare with the bookie's quote (their SGM price is not simply the legs multiplied)
    df = df[df["ev_at_multiplied_prices"] >= MIN_SHOWN_EV].copy()
    df["band"] = pd.cut(df["multiplied_leg_prices"], [b[0] for b in BANDS] + [BANDS[-1][1]],
                        labels=[f"{lo:.2f}-{hi:.2f}" for lo, hi in BANDS], include_lowest=True).astype(str)
    df = df.sort_values("ev_at_multiplied_prices", ascending=False)
    # one per leg combination: drop variants that only move a line
    df = df[~df["legs"].str.replace(r"[-+]?\d+(\.\d+)?", "#", regex=True).duplicated()]
    df = df.groupby("band").head(PER_BAND)
    return df.round({"model_only_prob": 4, "model_prob": 4, "fair_odds": 2, "min_price_worth_taking": 2, "multiplied_leg_prices": 2,
                     "ev_at_multiplied_prices": 4, "correlation_lift": 3}).reset_index(drop=True)


def _label(market, selection, line, player) -> str:
    if market == "moneyline":
        return f"{selection} win"
    if market == "spread":
        return f"{selection} {float(line):+g}"
    if market == "total":
        return f"game {selection} {line}"
    stat = market[5:].replace("fg3m", "3pm")
    if selection == "over" and float(line) % 1 == 0.5:
        return f"{player} {int(float(line) + 0.5)}+ {stat}"
    return f"{player} {stat} {selection} {line}"


LEG_RE = re.compile(r"^(?P<who>.+?)\s+(?P<what>pts|reb|ast|fg3m|stl|blk|tov|pra|pr|pa|ra|stocks|win|ml|"
                    r"spread|total)\s*(?P<side>over|under)?\s*(?P<line>[-+]?\d+(\.\d+)?)?$", re.I)


def check(sim: dict, home: str, away: str, legs_text: str, price: float, labels: dict) -> dict:
    """Evaluate a quoted SGM, e.g. 'LeBron James pts over 24.5; LAL win; game total over 228.5'."""
    names = {v.lower(): k for k, v in labels.items()}
    masks, played, parsed = [], [], []
    for leg in [x.strip() for x in legs_text.split(";") if x.strip()]:
        m = LEG_RE.match(leg)
        if not m:
            raise ValueError(f"can't read leg: {leg}")
        who, what = m["who"].strip(), m["what"].lower()
        side, line = (m["side"] or "").lower(), m["line"]
        if what in ("win", "ml"):
            mask = leg_mask(sim, home, away, "moneyline", who.upper(), None)
        elif what == "spread":
            mask = leg_mask(sim, home, away, "spread", who.upper(), float(line))
        elif what == "total":
            mask = leg_mask(sim, home, away, "total", side, float(line))
        else:
            pid = names.get(who.lower())
            if pid is None:
                raise ValueError(f"unknown player: {who}")
            mask = leg_mask(sim, home, away, f"prop_{what}", side, float(line), pid)
        pl = played_mask(sim, pid if what not in ("win", "ml", "spread", "total") else None)
        masks.append(mask)
        played.append(pl)
        parsed.append((leg, float(mask.sum() / max(pl.sum(), 1))))
    all_pl = np.logical_and.reduce(played)
    joint = float(np.logical_and.reduce(masks).sum() / max(all_pl.sum(), 1))  # given every leg player plays
    return {"legs": parsed, "model_prob": joint, "fair_odds": 1 / joint if joint else float("inf"),
            "quoted_price": price, "ev": joint * price - 1,
            "verdict": "value" if joint * price - 1 >= MIN_EDGE else "no value"}
