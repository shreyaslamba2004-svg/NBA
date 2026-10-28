"""Weekly grading of everything the scheduled runs logged, blend refit, and alerts.

Inputs (all written by the scheduled job):
  logs/projections/<date>_edges.csv   every priced offer per run, with model/market/blend probs
  logs/projections/<date>_games.csv   game projections per run
  logs/results/<date>.csv             final scores and player box lines

For each offer the *last* logged snapshot before tip is the decision we grade; the first
snapshot where a bet made the best-bets list is the price we "took" (for ROI and CLV).
Writes output/monitor.md, refits models/blend.json when there's enough data, and returns a
list of alert strings (the workflow opens a GitHub issue when it's non-empty).
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "logs"
BLEND_PATH = ROOT / "models" / "blend.json"
COMBOS = {"pra": ["pts", "reb", "ast"], "pr": ["pts", "reb"], "pa": ["pts", "ast"], "ra": ["reb", "ast"],
          "stocks": ["stl", "blk"]}
MIN_PROPS_FOR_REFIT = 1500
MIN_GAMES_FOR_REFIT = 400
BEST_EV, BEST_MAX_ODDS = 0.05, 4.0


def _read_all(pattern: str) -> pd.DataFrame:
    fs = sorted((LOGS / pattern.split("/")[0]).glob(pattern.split("/")[1]))
    return pd.concat([pd.read_csv(f).assign(_file=f.name) for f in fs], ignore_index=True) if fs else pd.DataFrame()


def outcomes() -> tuple[pd.DataFrame, pd.DataFrame]:
    res = _read_all("results/*.csv")
    if res.empty:
        return res, res
    for c, parts in COMBOS.items():
        res[c] = res[parts].sum(axis=1)
    games = res.drop_duplicates("game_id")[["game_id", "home", "away", "home_pts", "away_pts"]]
    return res, games


def graded_offers() -> pd.DataFrame:
    e = _read_all("projections/*_edges.csv")
    res, games = outcomes()
    if e.empty or games.empty:
        return pd.DataFrame()
    e["snap"] = e["snapshot_utc"].str.split("|").str[0]
    key = ["game_id", "market", "selection", "player", "line", "book"]
    e = e.sort_values("snap")
    first_best = (e[(e["ev_blend"] >= BEST_EV) & (e["price_decimal"] <= BEST_MAX_ODDS)]
                  .drop_duplicates(key, keep="first")[key + ["price_decimal", "snap"]]
                  .rename(columns={"price_decimal": "taken_price", "snap": "taken_snap"}))
    last = e.drop_duplicates(key, keep="last").merge(first_best, on=key, how="left")
    last = last.merge(games, on="game_id")
    margin = last["home_pts"] - last["away_pts"]
    total = last["home_pts"] + last["away_pts"]
    sel = last["selection"].astype(str)
    line = last["line"].astype(float)
    y = pd.Series(np.nan, index=last.index)
    ml = last["market"] == "moneyline"
    y[ml] = np.where(sel[ml] == last["home"][ml], margin[ml] > 0, margin[ml] < 0)
    sp = last["market"] == "spread"
    m_sel = np.where(sel == last["home"], margin, -margin)
    y[sp] = np.where((m_sel + line)[sp] == 0, np.nan, (m_sel + line)[sp] > 0)
    tt = last["market"] == "total"
    y[tt] = np.where(total[tt] == line[tt], np.nan, np.where(sel[tt] == "over", total[tt] > line[tt], total[tt] < line[tt]))
    pr = last["market"].str.startswith("prop_")
    if pr.any():
        long = res.copy()
        p = last[pr].merge(long, on=["game_id", "player"], how="left", suffixes=("", "_r"))
        stat = p["market"].str[5:]
        x = np.array([r[s] if s in r and pd.notna(r[s]) else np.nan for r, s in zip(p.to_dict("records"), stat)])
        lp = p["line"].astype(float).values
        yy = np.where(np.isnan(x) | (x == lp), np.nan, np.where(p["selection"] == "over", x > lp, x < lp))
        y[pr] = yy  # a player who didn't play stays ungraded (voided at most books)
    last["won"] = y
    last["kind"] = np.where(pr, "props", "game lines")
    return last.dropna(subset=["won"])


def _ll(p, y) -> float:
    p = np.clip(np.asarray(p, float), 1e-4, 1 - 1e-4)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def _fit_w(pm, pk, y) -> float:
    return float(minimize_scalar(lambda w: _ll(w * pm + (1 - w) * pk, y), bounds=(0, 1), method="bounded").x)


def report(today: date | None = None) -> tuple[str, list[str], dict]:
    today = today or date.today()
    g = graded_offers()
    alerts: list[str] = []
    md = [f"# Model monitor ({today.isoformat()})\n"]
    if g.empty:
        md.append("No graded bets yet: the logs need a few game days.\n")
        return "\n".join(md), alerts, {}
    g["day"] = pd.to_datetime(g["snap"].str[:10])
    paired = g.dropna(subset=["market_novig_prob"])
    rows = []
    for (kind, window), d in [((k, w), paired[(paired["kind"] == k) & (paired["day"] >= pd.Timestamp(today) - pd.Timedelta(days=dd))])
                              for k in ("game lines", "props") for w, dd in (("last 7 days", 7), ("season", 400))]:
        if len(d) < 20:
            continue
        y = d["won"].astype(float).values
        rows.append({"market": kind, "window": window, "bets graded": len(d),
                     "logloss model": round(_ll(d["model_prob"], y), 4),
                     "logloss market (no-vig)": round(_ll(d["market_novig_prob"], y), 4),
                     "logloss blend": round(_ll(d["blend_prob"], y), 4)})
    if rows:
        md += ["## Probability accuracy (lower logloss is better)\n", pd.DataFrame(rows).to_markdown(index=False), ""]
    # best bets: ROI at the taken price, and closing-line value against the final no-vig market
    bb = g.dropna(subset=["taken_price"])
    if len(bb):
        bb = bb.assign(profit=np.where(bb["won"] == 1, bb["taken_price"] - 1, -1.0),
                       clv=bb["market_novig_prob"] * bb["taken_price"] - 1)
        summ = []
        for window, dd in (("last 7 days", 7), ("season", 400)):
            d = bb[bb["day"] >= pd.Timestamp(today) - pd.Timedelta(days=dd)]
            for kind, x in d.groupby("kind"):
                summ.append({"market": kind, "window": window, "bets": len(x), "win %": round(100 * x["won"].mean(), 1),
                             "ROI % (1 unit each)": round(100 * x["profit"].mean(), 1),
                             "avg CLV %": round(100 * x["clv"].mean(), 1),
                             "beat closing %": round(100 * (x["clv"] > 0).mean(), 1)})
        md += ["## Best bets (EV ≥ 5%, odds ≤ 4) as listed in TODAY.md\n",
               "CLV compares the price you'd have taken with the final no-vig market before tip. Consistently "
               "positive CLV is the best early sign of a real edge; ROI is noisy for months.\n",
               pd.DataFrame(summ).to_markdown(index=False), ""]
        s = bb[bb["day"] >= pd.Timestamp(today) - pd.Timedelta(days=28)]
        if len(s) >= 100 and s["clv"].mean() < -0.01:
            alerts.append(f"Best bets have negative average CLV over 4 weeks ({100*s['clv'].mean():.1f}%, n={len(s)}).")
    # blend refit
    blend = json.loads(BLEND_PATH.read_text()) if BLEND_PATH.exists() else {}
    changes = {}
    for kind, key, need in (("props", "props", MIN_PROPS_FOR_REFIT), ("game lines", "game_logged", MIN_GAMES_FOR_REFIT)):
        d = paired[paired["kind"] == kind]
        if kind == "props":
            d = d[d["book_novig_prob"].between(0.3, 0.7)]  # main lines; milestones carry a guessed margin
        if len(d) >= need:
            w = round(_fit_w(d["model_prob"].values, d["market_novig_prob"].values, d["won"].astype(float).values), 3)
            changes[key] = w
    if changes:
        blend.setdefault("logged", {}).update(changes)
        blend["logged_refit"] = today.isoformat()
        BLEND_PATH.write_text(json.dumps(blend, indent=1))
        md.append("Blend weights refit from logged results: " + ", ".join(f"{k} {v}" for k, v in changes.items()) + "\n")
    else:
        md.append(f"Blend weights unchanged (refit needs {MIN_PROPS_FOR_REFIT} graded props / "
                  f"{MIN_GAMES_FOR_REFIT} game lines).\n")
    return "\n".join(md), alerts, changes


def staleness_alerts(today: date | None = None) -> list[str]:
    today = today or date.today()
    out = []
    try:  # off-season, All-Star break: no games in the last 3 days means nothing should be logged
        from .sources import espn
        played = sum(len(espn.scoreboard(today - timedelta(days=k))) for k in (1, 2, 3))
    except Exception:
        played = 0 if today.month in (7, 8, 9) else 1
    if not played:
        return out
    recent = sorted((LOGS / "projections").glob("*_games.csv"))
    if recent:
        last = date.fromisoformat(recent[-1].name[:10])
        if (today - last).days > 3:
            out.append(f"No projections logged since {last} (check the scheduled workflow).")
    res = sorted((LOGS / "results").glob("*.csv"))
    if res and (today - date.fromisoformat(res[-1].stem)).days > 4:
        out.append(f"No results graded since {res[-1].stem}.")
    return out


def run(today: date | None = None) -> list[str]:
    md, alerts, _ = report(today)
    alerts += staleness_alerts(today)
    if alerts:
        md += "\n## Alerts\n\n" + "\n".join(f"- {a}" for a in alerts) + "\n"
    (ROOT / "output" / "monitor.md").write_text(md)
    print(md)
    return alerts
