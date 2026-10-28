"""Referee crews for past games (ESPN game summaries), keyed to our game ids.

Seasons before the cutoff get no crew data; the model treats that as missing.
"""
from __future__ import annotations

import sys
from datetime import timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA, load_history  # noqa: E402
from nbamodel.sources import espn  # noqa: E402
from nbamodel.sources.live import SourceUnavailable  # noqa: E402


def main(from_season: str = "2022-23"):
    _, g = load_history()
    gs = g[g["season"] >= from_season]
    key = {(r.game_date.date(), r.home, r.away): r.game_id for r in gs.itertuples()}
    out_p = DATA / "officials.parquet"
    done = set(pd.read_parquet(out_p)["game_id"]) if out_p.exists() else set()
    rows = []
    d, end = gs["game_date"].min().date(), gs["game_date"].max().date()
    while d <= end:
        try:
            sb = espn.scoreboard(d)
        except SourceUnavailable:
            sb = pd.DataFrame()
        for e in sb.itertuples() if len(sb) else []:
            gid = key.get((d, e.home, e.away), e.game_id)
            if gid in done:
                continue
            try:
                refs = espn.officials_from_summary(espn.summary(e.game_id))
            except SourceUnavailable:
                continue
            for r in refs:
                rows.append({"game_id": int(gid), "official": r})
        d += timedelta(days=1)
        if d.day == 1 or d > end:  # checkpoint monthly so an interrupted run keeps its progress
            _save(out_p, rows)
            rows = []
            print(d, flush=True)


def _save(out_p, rows):
    new = pd.DataFrame(rows, columns=["game_id", "official"])
    if out_p.exists():
        new = pd.concat([pd.read_parquet(out_p), new], ignore_index=True)
    new.drop_duplicates().to_parquet(out_p, index=False)
    print("official rows", len(new), "games", new["game_id"].nunique(), flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:])
