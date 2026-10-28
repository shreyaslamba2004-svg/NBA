"""Keep/drop test for each context factor: retrain without it and compare on held-out games.

Same split as the backtest (train through 2023-24, test on 2025-26). A factor is kept only if
removing it makes the held-out projections worse. Writes output/ablation.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import nbamodel.dataset as D  # noqa: E402
from nbamodel.models import predict_minutes, predict_rates, predict_team, train  # noqa: E402
from scripts.train_backtest import team_normalise  # noqa: E402

THRU, TEST = "2023-24", "2025-26"
FACTORS = ["travel", "schedule_load", "rotation_depth", "rest_habits", "motivation", "referees",
           "shooting_luck", "award_pressure", "late_news"]
STATS = ["pts", "reb", "ast", "fg3m"]


def evaluate(P, G) -> dict:
    b = train(P, G, THRU, None)
    t = P[(P["season"] == TEST) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    t["pmin_raw"] = predict_minutes(b, t)
    t["pmin"] = team_normalise(t, "pmin_raw")
    r = predict_rates(b, t)
    g = G[(G["season"] == TEST) & (G["h_season_gp"] >= 3) & (G["a_season_gp"] >= 3)].dropna(subset=["margin"])
    pm, pt = predict_team(b, g)
    y = (g["margin"] > 0).astype(float)
    p = np.clip(norm.cdf(pm / 12.5), 0.01, 0.99)
    out = {"min MAE": np.abs(t["min"] - t["pmin"]).mean()}
    for s in STATS:
        out[f"{s} MAE"] = np.abs(t[s] - r[s] * t["pmin"]).mean()
    out["margin MAE"] = np.abs(g["margin"] - pm).mean()
    out["total MAE"] = np.abs(g["total"] - pt).mean()
    out["win logloss"] = float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))
    return out


def main():
    P = pd.read_parquet(D.DATA / "P.parquet")
    G = pd.read_parquet(D.DATA / "G.parquet")
    rows = []
    base = evaluate(P, G)
    rows.append({"variant": "all factors (current)", **base})
    print(rows[-1], flush=True)
    for f in FACTORS:
        D.DISABLED.clear()
        D.DISABLED.add(f)
        rows.append({"variant": f"without {f}", **evaluate(P, G)})
        print(rows[-1], flush=True)
    D.DISABLED.clear()
    for dg in ("arch", "pos"):
        D.DEFENSE_GROUPS = dg
        rows.append({"variant": f"defense vs {'player type' if dg == 'arch' else 'position'} only", **evaluate(P, G)})
        print(rows[-1], flush=True)
    D.DEFENSE_GROUPS = "both"
    res = pd.DataFrame(rows).set_index("variant")
    # verdict: does removing the factor hurt (keep) or help/no change (drop)?
    player_cols = ["min MAE"] + [f"{s} MAE" for s in STATS]
    verdict = []
    for v, r in res.iterrows():
        if v.startswith("all"):
            verdict.append("")
            continue
        d_player = float(np.mean([(r[c] - base[c]) / base[c] for c in player_cols]))
        d_game = float(np.mean([(r[c] - base[c]) / base[c] for c in ("margin MAE", "total MAE", "win logloss")]))
        hurt = max(d_player, d_game)
        verdict.append("keep (helps)" if hurt > 0.001 else ("drop (no help)" if hurt > -0.001 else "drop (removing it helps)"))
    res["verdict"] = verdict
    md = ["# Context factors: keep or drop\n",
          f"Each row retrains without one factor (train through {THRU}, test on {TEST}). Lower is better. "
          "A factor is kept if removing it makes projections worse by more than 0.1% on average.\n",
          res.round(4).reset_index().to_markdown(index=False)]
    (ROOT / "output" / "ablation.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
