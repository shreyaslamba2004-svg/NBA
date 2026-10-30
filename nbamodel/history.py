"""Readable archive of past days: the final pre-tip projections next to what actually happened.

history/<date>.md per game day (built by the nightly grading run once results are in) and
history/README.md as the index. Projections are the last ones logged before each game's tip.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from .health import LOGS, ROOT, _results, _tips
from .sources.live import norm_name

HIST = ROOT / "history"
STATS = [("min", "Min"), ("pts", "Pts"), ("reb", "Reb"), ("ast", "Ast"), ("fg3m", "3PM")]


def _last_before_tip(df: pd.DataFrame, tips: dict, keys: list) -> pd.DataFrame:
    df = df.copy()
    df["snap"] = pd.to_datetime(df["snapshot_utc"].astype(str).str.split("|").str[0], utc=True)
    df = df[df["game_id"].map(tips) > df["snap"]]
    return df.sort_values("snap").groupby(keys).tail(1)


def build_day(d: str) -> bool:
    from .market_log import log_file
    pf, gf = log_file(LOGS / "projections" / f"{d}_players.csv"), log_file(LOGS / "projections" / f"{d}_games.csv")
    if pf is None or not (LOGS / "results" / f"{d}.csv").exists():
        return False
    r, tips = _results(d), _tips(d)
    pr = pd.read_csv(pf, low_memory=False)
    pr = _last_before_tip(pr[pr["scenario"] == "base"], tips, ["game_id", "player_id"])
    pr["k"] = pr["player"].map(norm_name)
    m = pr.merge(r[["game_id", "k"] + [s for s, _ in STATS]], on=["game_id", "k"], how="left")
    gm = pd.read_csv(gf, low_memory=False) if gf is not None else pd.DataFrame()
    if len(gm):
        gm = gm[gm["scenario"].isna() | (gm["scenario"] == "base")] if "scenario" in gm else gm
        gm = _last_before_tip(gm, tips, ["game_id"]).set_index("game_id")
    scores = r.drop_duplicates("game_id").set_index("game_id")
    out = [f"# {d}: projections vs results",
           f"Final projections before each tip, next to the box score. [That day's sheet](../output/{d}/today.md) "
           "· [All days](README.md) · [Model health](../HEALTH.md)",
           "Each cell is **projected / actual**. Projections assume the player plays; DNP = didn't play."]
    for gid, g in m.groupby("game_id", sort=False):
        s = scores.loc[gid] if gid in scores.index else None
        head = f"## {g['matchup'].iloc[0]}"
        if s is not None:
            head += f": {s['away']} {s['away_pts']:.0f}, {s['home']} {s['home_pts']:.0f}"
        out.append(head)
        if len(gm) and gid in gm.index and s is not None:
            q = gm.loc[gid]
            out.append(f"Projected {q['away']} {q['proj_away_pts']:.0f}, {q['home']} {q['proj_home_pts']:.0f} "
                       f"(total {q['proj_total']:.0f} vs {s['home_pts'] + s['away_pts']:.0f}).")
        rows = ["| Player | Plays % | " + " | ".join(n for _, n in STATS) + " |",
                "|---|--:|" + "--:|" * len(STATS)]
        g = g.sort_values(["team", "proj_min"], ascending=[True, False])
        for p in g.itertuples():
            played = pd.notna(p.min) and p.min > 0
            cells = []
            for s, _ in STATS:
                proj = getattr(p, f"proj_{s}")
                cells.append(f"{proj:.1f} / {getattr(p, s):.0f}" if played else f"{proj:.1f} / DNP")
            rows.append(f"| {p.player} ({p.team}) | {p.play_prob:.0%} | " + " | ".join(cells) + " |")
        out.append("\n".join(rows))
        miss = g[g["min"].fillna(0) > 0]
        if len(miss):
            out.append(f"Average miss for players who played: minutes {np.abs(miss['proj_min'] - miss['min']).mean():.1f}, "
                       f"points {np.abs(miss['proj_pts'] - miss['pts']).mean():.1f}.")
    HIST.mkdir(exist_ok=True)
    (HIST / f"{d}.md").write_text("\n\n".join(out) + "\n")
    return True


def build(today: date | None = None) -> None:
    """Archive every graded day that isn't archived yet, then rewrite the index."""
    days = sorted(f.stem for f in (LOGS / "results").glob("*.csv"))
    for d in days:
        if not (HIST / f"{d}.md").exists():
            build_day(d)
    have = sorted((f.stem for f in HIST.glob("20*.md")), reverse=True)
    lines = ["# Past days",
             "Each day's final projections next to the actual box scores, newest first. "
             "Back to [TODAY.md](../TODAY.md) · [Model health](../HEALTH.md)", ""]
    lines += [f"- [{d}]({d}.md) · [sheet as it stood]({'../output/' + d + '/today.md'})" for d in have]
    (HIST / "README.md").write_text("\n".join(lines) + "\n")
