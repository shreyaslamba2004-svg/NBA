"""Does old data help? Same test season (2025-26), different training windows / recency weights."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA  # noqa: E402
from nbamodel.models import predict_team, predict_minutes, predict_rates, train  # noqa: E402
from scripts.train_backtest import team_normalise  # noqa: E402

TEST, THRU = "2025-26", "2024-25"
CONFIGS = [("2010+ equal", "2010-11", None), ("2016+ equal", "2016-17", None),
           ("2019+ equal", "2019-20", None), ("2010+ half-life 4 seasons", "2010-11", 4.0)]


def main():
    P = pd.read_parquet(DATA / "P.parquet")
    G = pd.read_parquet(DATA / "G.parquet")
    odds = pd.read_parquet(DATA / "odds.parquet")
    t = P[(P["season"] == TEST) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    g = G[G["season"] == TEST].dropna(subset=["margin"])
    g = g[(g["h_season_gp"] >= 3) & (g["a_season_gp"] >= 3)].merge(
        odds[["game_date", "home", "away", "close_spread_home", "close_total"]], on=["game_date", "home", "away"],
        how="left")
    rows = []
    for name, start, hl in CONFIGS:
        b = train(P, G, THRU, None, from_season=start, half_life=hl)
        t["pmin_raw"] = predict_minutes(b, t)
        t["pmin"] = team_normalise(t, "pmin_raw")
        r = predict_rates(b, t)
        pm, pt = predict_team(b, g)
        gl = g["close_spread_home"].notna()
        res = (g["margin"] + g["close_spread_home"])[gl]
        side = np.sign(pm[gl] + g["close_spread_home"][gl])
        row = {"training data": name, "min MAE": np.abs(t["min"] - t["pmin"]).mean()}
        for s in ("pts", "reb", "ast", "fg3m"):
            row[f"{s} MAE"] = np.abs(t[s] - r[s] * t["pmin"]).mean()
        row["margin MAE"] = np.abs(g["margin"] - pm).mean()
        row["total MAE"] = np.abs(g["total"] - pt).mean()
        row["ATS win% vs close"] = 100 * (np.sign(res) == side)[res != 0].mean()
        rows.append(row)
        print(row, flush=True)
    out = pd.DataFrame(rows).round(3)
    md = out.to_markdown(index=False) if hasattr(out, "to_markdown") else out.to_string(index=False)
    (ROOT / "output" / "era_experiment.md").write_text(
        f"# Training window experiment (train through {THRU}, test {TEST})\n\n{md}\n")
    print(md)


if __name__ == "__main__":
    main()
