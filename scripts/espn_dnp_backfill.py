"""Add coach's-decision DNP rows for seasons rebuilt from play-by-play (2024-25, 2025-26).

Play-by-play only shows who played. Treating every non-participant as 'absent' leaks game
script (deep benches only play in blowouts), so we need to know who was dressed and
available but unused. ESPN box scores list those players with reason "COACH'S DECISION".
"""
from __future__ import annotations

import sys
from datetime import timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA  # noqa: E402
from nbamodel.sources import espn  # noqa: E402
from nbamodel.sources.live import SourceUnavailable  # noqa: E402


def main(seasons=("2024-25", "2025-26")):
    pg = pd.read_parquet(DATA / "player_games.parquet")
    g = pd.read_parquet(DATA / "games.parquet")
    cw = espn.Crosswalk(pg, DATA / "espn_crosswalk.json")
    gs = g[g["season"].isin(seasons)]
    key = {(r.game_date.date(), r.home, r.away): r.game_id for r in gs.itertuples()}
    rows = []
    d, end = gs["game_date"].min().date(), gs["game_date"].max().date()
    while d <= end:
        try:
            sb = espn.scoreboard(d)
        except SourceUnavailable:
            sb = pd.DataFrame()
        for e in sb.itertuples() if len(sb) else []:
            gid = key.get((d, e.home, e.away))
            if gid is None:
                continue
            try:
                js = espn.summary(e.game_id)
                b = espn.box_from_summary(js, cw)
            except (SourceUnavailable, KeyError, IndexError):
                continue
            dnp = b[(b["min"] == 0) & b["comment"].str.contains("COACH", case=False)]
            for r in dnp.itertuples():
                rows.append({"game_id": gid, "team": r.team, "player_id": r.player_id,
                             "player_name": r.player_name, "comment": "DNP - Coach's Decision"})
        d += timedelta(days=1)
    cw.save()
    out = pd.DataFrame(rows)
    out.to_parquet(DATA / "dnp_cd_pbp_seasons.parquet", index=False)
    print("DNP-CD rows", len(out), "games", out["game_id"].nunique() if len(out) else 0)


if __name__ == "__main__":
    main()
