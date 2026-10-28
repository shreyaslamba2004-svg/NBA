"""Player listed position (G/F/C) for defense-vs-position.

Priority: ESPN's current roster listing (what live runs see) > the slot a player most often
started in (nba.com boxes 2010-24) > fallback by player type, applied in dataset.build.
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA, load_history  # noqa: E402
from nbamodel.sources import espn  # noqa: E402
from nbamodel.sources.live import SourceUnavailable, _get  # noqa: E402
from nbamodel.teams import TEAMS  # noqa: E402

RAW = ROOT / "data" / "raw"


def main():
    raw = pd.concat([pd.read_csv(RAW / f"regular_season_box_scores_2010_2024_part_{i}.csv",
                                 usecols=["personId", "position"]) for i in (1, 2, 3)]).dropna()
    slot = raw.groupby("personId")["position"].agg(lambda x: x.mode().iloc[0])
    pos = {int(k): v for k, v in slot.items()}
    pg, _ = load_history()
    cw = espn.Crosswalk(pg, DATA / "espn_crosswalk.json")
    for tri in TEAMS:
        try:
            js = _get(f"{espn.BASE}/teams/{tri.lower()}/roster")
        except SourceUnavailable:
            continue
        for a in js.get("athletes", []):
            ab = (a.get("position") or {}).get("abbreviation", "")
            p = {"PG": "G", "SG": "G", "G": "G", "SF": "F", "PF": "F", "F": "F", "C": "C"}.get(ab)
            if p:
                pos[cw.lookup(a["id"], a["displayName"], tri)] = p
    cw.save()
    out = pd.DataFrame({"player_id": list(pos), "pos": list(pos.values())})
    out.to_parquet(DATA / "positions.parquet", index=False)
    print(out["pos"].value_counts())


if __name__ == "__main__":
    main()
