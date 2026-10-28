"""Official NBA injury reports as published ~5pm ET on each game day (2022-23 onward).

Used for point-in-time backtests: availability comes from what was public before tip-off,
not from who appeared in the box score.
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA, load_history  # noqa: E402
from nbamodel.sources.live import SourceUnavailable, fetch_injury_pdf, parse_injury_pdf  # noqa: E402

TIMES = ["05PM", "05_00PM", "04_30PM", "04PM", "05_30PM", "06PM", "06_00PM", "01PM", "01_30PM"]


def main(from_season="2022-23"):
    _, g = load_history()
    days = sorted(g[g["season"] >= from_season]["game_date"].dt.date.unique())
    out_p = DATA / "injury_reports.parquet"
    have = set(pd.read_parquet(out_p)["report_date"].dt.date) if out_p.exists() else set()
    frames = []
    for i, d in enumerate(days):
        if d in have:
            continue
        for t in TIMES:
            try:
                df = parse_injury_pdf(fetch_injury_pdf(d, t))
            except SourceUnavailable:
                continue
            except Exception as e:  # unparseable PDF
                print(d, t, "parse error", e)
                continue
            if len(df):
                df = df[df["game_date"].isna() | (df["game_date"] == pd.Timestamp(d))]
                frames.append(df.assign(report_date=pd.Timestamp(d), report_time=t))
                break
        if i % 50 == 0:
            print(i, d, flush=True)
    new = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    if out_p.exists():
        new = pd.concat([pd.read_parquet(out_p), new], ignore_index=True)
    new.to_parquet(out_p, index=False)
    print("rows", len(new), "days", new["report_date"].nunique())


if __name__ == "__main__":
    main(*sys.argv[1:])
