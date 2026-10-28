"""Which opponent-vs-player-group features help? Rate models only, judged on 2025-26 using
actual minutes so the comparison isolates per-minute production."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import nbamodel.dataset as ds  # noqa: E402
from nbamodel.models import Bundle, fit_rates, predict_rates  # noqa: E402

STATS = ["pts", "reb", "ast", "fg3m", "stl", "blk", "tov"]


def main():
    P = pd.read_parquet(ds.DATA / "P.parquet")
    tr = P[(P["season"] <= "2024-25") & (P["season"] >= "2016-17")]
    te = P[(P["season"] == "2025-26") & (P["min"] >= 4) & (P["gp"] >= 3)]
    rows = []
    for mode in ("none", "pos", "arch", "both"):
        ds.DEFENSE_GROUPS = mode
        b = Bundle(rates=fit_rates(tr), rate_features={s: ds.rate_feats(s) for s in STATS + ["fga", "fta"]})
        r = predict_rates(b, te)
        row = {"opponent features": {"none": "team-level only", "pos": "+ defense vs position (G/F/C)",
                                     "arch": "+ defense vs player type", "both": "+ both"}[mode]}
        for s in STATS:
            row[s] = np.abs(te[s] - r[s] * te["min"]).mean()
        rows.append(row)
        print(row, flush=True)
    out = pd.DataFrame(rows).round(4)
    md = out.to_markdown(index=False)
    (ROOT / "output" / "dvp_experiment.md").write_text(
        "# Opponent-vs-player-group features: MAE per stat on 2025-26 (given actual minutes)\n\n" + md + "\n")
    print(md)


if __name__ == "__main__":
    main()
