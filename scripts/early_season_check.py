"""Early-season form: should projections lean harder on this season's minutes and per-minute rates?

Train through 2023-24 (as rep_check), project 2024-25 and 2025-26. For players early in a season
(3-19 games), move the projection part of the way toward this-season form:
  minutes  pmin' = pmin + w_min * (season minutes form - pmin)
  stat     rate' = rate + w_s   * (season per-minute rate - rate)
Weights are fit per games-played bucket on 2024-25 (lowest MAE) and judged on 2025-26 only.
Writes output/early_season_check.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import nbamodel.dataset as D  # noqa: E402
from nbamodel.models import predict_minutes, predict_rates, train  # noqa: E402
from scripts.train_backtest import team_normalise  # noqa: E402

THRU, FIT, TEST = "2023-24", "2024-25", "2025-26"
STATS = ["pts", "reb", "ast", "fg3m"]
BUCKETS = [(3, 5), (6, 10), (11, 19)]
GRID = np.round(np.arange(0, 1.01, 0.05), 2)


def project() -> pd.DataFrame:
    P = pd.read_parquet(D.DATA / "P.parquet")
    G = pd.read_parquet(D.DATA / "G.parquet")
    b = train(P, G, THRU, None)
    t = P[P["season"].isin([FIT, TEST]) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    t["pmin_raw"] = predict_minutes(b, t)
    t["pmin"] = team_normalise(t, "pmin_raw")
    r = predict_rates(b, t)
    for s in STATS:
        t[f"rate_{s}"] = r[s]
    t["gps"] = t["gp_season"]
    return t


def mae(a, b) -> float:
    return float(np.nanmean(np.abs(np.asarray(a) - np.asarray(b))))


def main():
    cache = ROOT / "output" / "early_season_proj.parquet"
    t = pd.read_parquet(cache) if cache.exists() else project()
    t.to_parquet(cache)
    t = t[(t["gps"] >= 3) & (t["gps"] <= 19)]
    rows, weights = [], {}
    for lo, hi in BUCKETS:
        bk = t[(t["gps"] >= lo) & (t["gps"] <= hi)]
        fit, test = bk[bk["season"] == FIT], bk[bk["season"] == TEST]
        # minutes
        def pm(d, w):
            return d["pmin"] + w * (d["min_season_s"].fillna(d["pmin"]) - d["pmin"])
        wm = min(GRID, key=lambda w: mae(fit["min"], pm(fit, w)))
        weights[(lo, hi, "min")] = wm
        rows.append({"games into season": f"{lo}-{hi}", "stat": "min", "fitted weight": wm, "test rows": len(test),
                     "test MAE now": round(mae(test["min"], test["pmin"]), 4),
                     "test MAE adjusted": round(mae(test["min"], pm(test, wm)), 4)})
        for s in STATS:
            def pr(d, w, wmin):
                rate = d[f"rate_{s}"] + w * (d[f"{s}_r_season"].fillna(d[f"rate_{s}"]) - d[f"rate_{s}"])
                return rate * pm(d, wmin)
            ws = min(GRID, key=lambda w: mae(fit[s], pr(fit, w, wm)))
            weights[(lo, hi, s)] = ws
            rows.append({"games into season": f"{lo}-{hi}", "stat": s, "fitted weight": ws, "test rows": len(test),
                         "test MAE now": round(mae(test[s], test[f"rate_{s}"] * test["pmin"]), 4),
                         "test MAE adjusted": round(mae(test[s], pr(test, ws, wm)), 4)})
    res = pd.DataFrame(rows)
    res["change %"] = (100 * (res["test MAE adjusted"] / res["test MAE now"] - 1)).round(2)
    md = ["# Early-season form check\n",
          f"Model trained through {THRU}. Weights fit on {FIT}, judged on {TEST} (never seen in fitting). "
          "Weight = how far to move toward this season's minutes form / per-minute rate (0 = current model). "
          "Lower MAE is better.\n", res.to_markdown(index=False)]
    (ROOT / "output" / "early_season_check.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
