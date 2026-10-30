"""Automatic sanity checks on every projection run, so odd numbers are flagged instead of found by eye.

Per game (confirmed-player projections):
  team minutes   a team's expected minutes far from a normal game (the model no longer forces 240,
                 so a big gap means the roster or play chances look wrong)
  player minutes a regular projected well above anything he's played lately, or well below his usual
                 (his last 10 games this season for his current team)
  team points    projected team score far from what the betting market implies
  player points  projected points far from DraftKings' main line
Writes output/<date>/sanity.csv; TODAY.md lists the flags and HEALTH.md counts them per day.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

TEAM_MIN = (210.0, 270.0)  # normal range for a team's expected minutes (live-like backtest: 10th-90th pct 220-260)
ABOVE_MAX = 4.0            # minutes above his most in the last 10 games
BELOW_AVG = 8.0            # minutes below his last-10 average (regulars only)
TEAM_PTS_GAP = 8.0         # points from the market-implied team score
PLAYER_PTS_GAP = (5.0, 0.25)  # points from DraftKings' main line: at least 5 and 25% of the line


def check(res: dict, pg: pd.DataFrame) -> pd.DataFrame:
    rows = []
    ps, gs, ed = res.get("players", pd.DataFrame()), res.get("games", pd.DataFrame()), res.get("edges", pd.DataFrame())
    if ps is None or ps.empty:
        return pd.DataFrame(columns=["game_id", "matchup", "check", "detail"])
    p = ps[ps["scenario"] == "base"].copy()
    mu = p.groupby("game_id")["matchup"].first()

    def flag(gid, kind, detail):
        rows.append({"game_id": gid, "matchup": mu.get(gid, ""), "check": kind, "detail": detail})

    # team minutes
    tm = (p["proj_min"] * p["play_prob"]).groupby([p["game_id"], p["team"]]).sum()
    for (gid, team), v in tm.items():
        if not TEAM_MIN[0] <= v <= TEAM_MIN[1]:
            flag(gid, "team minutes", f"{team} players add up to {v:.0f} expected minutes (normal is about 240)")
    # player minutes vs his last 10 games this season for his current team (last season's playoff
    # minutes or an old team's role aren't a fair comparison, e.g. a player traded into a smaller role)
    hist = pg[(pg["min"].fillna(0) > 0) & (pg["season"] == pg["season"].max())].sort_values("game_date")
    hist = hist.merge(p[["player_id", "team"]].drop_duplicates("player_id"), on=["player_id", "team"])
    rec = hist.groupby("player_id").tail(10).groupby("player_id")["min"].agg(["max", "mean", "size"])
    p = p.join(rec, on="player_id")
    hi = p[(p["size"] >= 3) & (p["proj_min"] >= 28) & (p["proj_min"] > p["max"] + ABOVE_MAX)]
    for r in hi.itertuples():
        flag(r.game_id, "player minutes", f"{r.player} projected {r.proj_min:.0f} min; most in his last 10 games is {r.max:.0f}")
    lo = p[(p["size"] >= 4) & (p["mean"] >= 24) & (p["play_prob"] >= 0.9) & (p["proj_min"] < p["mean"] - BELOW_AVG)]
    for r in lo.itertuples():
        flag(r.game_id, "player minutes", f"{r.player} projected {r.proj_min:.0f} min; he's averaged {r.mean:.0f} in his last 10")
    # team points vs market
    g = gs[gs["scenario"] == "base"] if "scenario" in gs else gs
    for r in g.itertuples():
        t, s = getattr(r, "market_total", np.nan), getattr(r, "market_spread_home", np.nan)
        if pd.isna(t) or pd.isna(s):
            continue
        for team, proj, implied in ((r.home, r.proj_home_pts, (t - s) / 2), (r.away, r.proj_away_pts, (t + s) / 2)):
            if abs(proj - implied) > TEAM_PTS_GAP:
                flag(r.game_id, "team points", f"{team} projected {proj:.0f}, market implies {implied:.0f}")
    # player points vs DraftKings main line
    if ed is not None and len(ed) and "main_line" in ed:
        dk = ed[(ed["market"] == "prop_pts") & (ed["book"].astype(str).str.lower() == "draftkings")
                & (ed["main_line"].astype(str).str.lower() == "true")]
        dk = dk.drop_duplicates(["game_id", "player_id"])
        dk = dk.merge(p[["game_id", "player_id", "player", "proj_pts"]].drop(columns="player"),
                      on=["game_id", "player_id"], how="inner")
        gap = (dk["proj_pts"] - dk["line"].astype(float)).abs()
        big = dk[gap >= np.maximum(PLAYER_PTS_GAP[0], PLAYER_PTS_GAP[1] * dk["line"].astype(float))]
        for r in big.itertuples():
            flag(r.game_id, "player points", f"{r.player} projected {r.proj_pts:.1f} pts vs DraftKings line {r.line:g}")
    return pd.DataFrame(rows, columns=["game_id", "matchup", "check", "detail"])


def section(df: pd.DataFrame, limit: int = 20) -> str:
    """Markdown for TODAY.md."""
    if df is None or df.empty:
        return "All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, " \
               "player points vs DraftKings)."
    head = (f"{len(df)} flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), "
            "but check them before betting on the players or games listed.")
    rows = ["| Game | Check | Detail |", "|---|---|---|"] + \
           [f"| {r.matchup} | {r.check} | {r.detail} |" for r in df.head(limit).itertuples()]
    more = f"\n\n_+{len(df) - limit} more in the sanity.csv file._" if len(df) > limit else ""
    return head + "\n\n" + "\n".join(rows) + more
