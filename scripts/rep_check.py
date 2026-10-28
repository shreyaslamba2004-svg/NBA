"""Does a feature group help? Retrain with and without it and compare on held-out games, overall and
for the players it targets: just traded, back from a long absence, early in a season, or with a
same-position teammate out.

Same split as the ablation (train through 2023-24, test on 2025-26). Writes output/<group>_check.md.
Usage: rep_check.py [group] [groups to keep off in both runs...]  (default group: rep_history)
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
from scripts.ablation import THRU, TEST  # noqa: E402
from scripts.train_backtest import team_normalise  # noqa: E402

STATS = ["pts", "reb", "ast", "fg3m"]


def project(P, G) -> pd.DataFrame:
    b = train(P, G, THRU, None)
    t = P[(P["season"] == TEST) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    t["pmin_raw"] = predict_minutes(b, t)
    t["pmin"] = team_normalise(t, "pmin_raw")
    r = predict_rates(b, t)
    out = t[["player_id", "player_name", "game_date", "team", "min", "pmin"] + STATS].copy()
    for s in STATS:
        out[f"p_{s}"] = r[s] * t["pmin"]
    out["traded"] = (t["gp_team"] < 15) & (t["gp"] > t["gp_team"] + 5)
    out["comeback"] = t["games_since_return"] < 10
    out["early"] = t["gp_season"] < 10
    out["pos_gap"] = t["vac_min_same_pos"] >= 20 if "vac_min_same_pos" in t else False
    out["passer"] = t["ast_r_l"] >= 0.15  # 5+ assists per 36 minutes
    out["met_before"] = t["vs_opp_min"] >= 60 if "vs_opp_min" in t else False
    return out


def scores(o: pd.DataFrame) -> dict:
    d = {"rows": len(o), "min MAE": np.abs(o["min"] - o["pmin"]).mean()}
    for s in STATS:
        d[f"{s} MAE"] = np.abs(o[s] - o[f"p_{s}"]).mean()
    return d


def main(group: str = "rep_history", off: tuple = ()):
    """Compare the model without `group` (before) to with it (after); `off` stays disabled in both."""
    P = pd.read_parquet(D.DATA / "P.parquet")
    G = pd.read_parquet(D.DATA / "G.parquet")
    D.DISABLED.clear()
    D.DISABLED.update({group, *off})
    before = project(P, G)
    D.DISABLED.clear()
    D.DISABLED.update(off)
    after = project(P, G)
    D.DISABLED.clear()
    rows = []
    for name, m in (("all players", slice(None)), ("traded (<15 games with new team)", before["traded"]),
                    ("back from long absence (<10 games)", before["comeback"]),
                    ("first 10 games of the season", before["early"]),
                    ("same-position teammate out (20+ min)", before["pos_gap"]),
                    ("playmakers (5+ ast per 36)", before["passer"]),
                    ("60+ past minutes vs this opponent", before["met_before"])):
        for lab, o in (("before", before), ("after", after)):
            rows.append({"group": name, "model": lab, **scores(o.loc[m])})
    res = pd.DataFrame(rows)
    before.to_parquet(ROOT / "output" / f"{group}_before.parquet")
    after.to_parquet(ROOT / "output" / f"{group}_after.parquet")
    md = [f"# {group}: before vs after\n",
          f"Train through {THRU}, test on {TEST}. Mean absolute error, lower is better.\n",
          res.round(3).to_markdown(index=False)]
    (ROOT / "output" / f"{group}_check.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main(*sys.argv[1:2], off=tuple(sys.argv[2:]))
