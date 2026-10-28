"""Grade simulated prop probabilities on held-out games, with and without the blowout-minutes
adjustment. Uses the backtest bundle (trained <= 2023-24) on 2025-26 games."""
from __future__ import annotations

import copy
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA  # noqa: E402
from nbamodel.models import predict_team, SIM_STATS, Bundle, predict_minutes, predict_rates  # noqa: E402
from nbamodel.simulate import simulate_game  # noqa: E402
from scripts.train_backtest import team_normalise  # noqa: E402

STATS = ["pts", "reb", "ast", "fg3m"]


def main(n_games: int = 300):
    b = Bundle.load(ROOT / "models" / "bundle_backtest.pkl")
    b.use_blowout = True
    nb = copy.copy(b)
    nb.use_blowout = False
    P = pd.read_parquet(DATA / "P.parquet")
    G = pd.read_parquet(DATA / "G.parquet")
    g = G[(G["season"] == "2025-26") & (G["h_season_gp"] >= 3) & (G["a_season_gp"] >= 3)].dropna(subset=["margin"])
    g = g.sample(n_games, random_state=1)
    t = P[P["game_id"].isin(g["game_id"]) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    t["pmin_raw"] = predict_minutes(b, t)
    t["pmin"] = team_normalise(t, "pmin_raw")
    r = predict_rates(b, t)
    for s in SIM_STATS:
        t[f"rate_{s}"] = r[s]
    t["play_prob"] = 1.0
    g["mu_margin"], g["mu_total"] = predict_team(b, g)
    rows = []
    for gr in g.itertuples():
        game = {"home": gr.home, "away": gr.away, "mu_margin": gr.mu_margin, "mu_total": gr.mu_total}
        gp = t[t["game_id"] == gr.game_id].copy()
        for team, mu in ((gr.home, (gr.mu_total + gr.mu_margin) / 2), (gr.away, (gr.mu_total - gr.mu_margin) / 2)):
            m = gp["team"] == team
            bu = (gp.loc[m, "rate_pts"] * gp.loc[m, "pmin"]).sum()
            if bu > 0:
                gp.loc[m, "rate_pts"] *= mu / bu
        sims = {name: simulate_game(game, gp, bb, n=6000, seed=int(gr.game_id) % 2**31)
                for name, bb in (("blowout", b), ("no_blowout", nb))}
        actual = gp.set_index("player_id")
        for j, p in enumerate(sims["no_blowout"]["players"]):
            a = actual.loc[p["player_id"]]
            for s in STATS + ["min"]:
                base = p["draws"][s]
                line = np.floor(np.median(base)) + 0.5
                row = {"pmin": a["pmin"], "stat": s, "line": line, "y": float(a[s] > line)}
                for name, sim in sims.items():
                    x = sim["players"][j]["draws"][s]
                    row[f"p_{name}"] = np.clip((x > line).mean(), 0.01, 0.99)
                    row[f"crps_{name}"] = np.mean(np.abs(x - a[s])) - 0.5 * np.mean(np.abs(x - np.roll(x, 1)))
                rows.append(row)
    d = pd.DataFrame(rows)
    d["role"] = np.where(d["pmin"] >= 30, "starters 30+ min", np.where(d["pmin"] >= 15, "rotation 15-30", "bench <15"))
    out = []
    for (role, s), x in d.groupby(["role", "stat"]):
        rec = {"role": role, "stat": s, "n": len(x)}
        for name in ("no_blowout", "blowout"):
            p = x[f"p_{name}"]
            rec[f"logloss {name}"] = -np.mean(x["y"] * np.log(p) + (1 - x["y"]) * np.log(1 - p))
            rec[f"CRPS {name}"] = x[f"crps_{name}"].mean()
        out.append(rec)
    res = pd.DataFrame(out).round(4)
    md = res.to_markdown(index=False)
    (ROOT / "output" / "blowout_backtest.md").write_text(
        f"# Blowout-minutes adjustment, {n_games} held-out 2025-26 games (lower is better)\n\n{md}\n")
    print(md)


if __name__ == "__main__":
    main()
