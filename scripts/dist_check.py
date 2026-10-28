"""Are the simulated stat distributions the right width and shape? (held-out 2025-26)

For each player-game and stat we take the simulated distribution and ask where the actual result
fell (randomised PIT: uniform if the spread is right; U-shaped = too narrow; hump = too wide), plus
the log loss of over/under at three lines around the median. Variants rescale the count noise
(gamma-Poisson dispersion) and the minutes noise; the best one is reported.
Writes output/dist_check.md.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA  # noqa: E402
from nbamodel.models import SIM_STATS, Bundle, predict_minutes, predict_rates, predict_team  # noqa: E402
from nbamodel.simulate import simulate_game  # noqa: E402
from scripts.train_backtest import team_normalise  # noqa: E402

STATS = ["pts", "reb", "ast", "fg3m", "stl", "blk"]
VARIANTS = {"current": (1.0, 1.0), "count noise x0.7": (0.7, 1.0), "count noise x1.5": (1.5, 1.0),
            "count noise x2.5": (2.5, 1.0), "minutes noise x0.75": (1.0, 0.75), "minutes noise x1.25": (1.0, 1.25)}


def main(n_games: int = 250, n_sims: int = 4000):
    b0 = Bundle.load(ROOT / "models" / "bundle_backtest.pkl")
    P = pd.read_parquet(DATA / "P.parquet")
    G = pd.read_parquet(DATA / "G.parquet")
    g = G[(G["season"] == "2025-26") & (G["h_season_gp"] >= 3) & (G["a_season_gp"] >= 3)].dropna(subset=["margin"])
    g = g.sample(n_games, random_state=7)
    t = P[P["game_id"].isin(g["game_id"]) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    t["pmin_raw"] = predict_minutes(b0, t)
    t["pmin"] = team_normalise(t, "pmin_raw")
    r = predict_rates(b0, t)
    for s in SIM_STATS:
        t[f"rate_{s}"] = r[s]
    t["play_prob"] = 1.0
    g["mu_margin"], g["mu_total"] = predict_team(b0, g)
    rng = np.random.default_rng(0)
    recs = []
    for name, (kd, ms) in VARIANTS.items():
        b = copy.deepcopy(b0)
        b.disp = {k: v / kd for k, v in b0.disp.items()}  # smaller k = wider
        b.min_sd = {k: v * ms for k, v in b0.min_sd.items()}
        for gr in g.itertuples():
            gp = t[t["game_id"] == gr.game_id]
            for team, mu in ((gr.home, (gr.mu_total + gr.mu_margin) / 2), (gr.away, (gr.mu_total - gr.mu_margin) / 2)):
                m = gp["team"] == team
                bu = (gp.loc[m, "rate_pts"] * gp.loc[m, "pmin"]).sum()
                if bu > 0:
                    gp.loc[m, "rate_pts"] *= mu / bu
            sim = simulate_game({"home": gr.home, "away": gr.away, "mu_margin": gr.mu_margin,
                                 "mu_total": gr.mu_total}, gp, b, n=n_sims, seed=int(gr.game_id) % 2**31)
            act = gp.set_index("player_id")
            for p in sim["players"]:
                a = act.loc[p["player_id"]]
                for s in STATS:
                    x = p["draws"][s]
                    y = float(a[s])
                    pit = (x < y).mean() + rng.random() * (x == y).mean()
                    med = np.floor(np.median(x)) + 0.5
                    ll = []
                    for line in (med - 2, med, med + 2) if s in ("pts", "reb", "ast") else (med,):
                        po = np.clip((x > line).mean(), 0.01, 0.99)
                        ll.append(-(np.log(po) if y > line else np.log(1 - po)))
                    recs.append({"variant": name, "stat": s, "pit": pit, "ll": np.mean(ll),
                                 "in50": abs(pit - 0.5) <= 0.25, "in80": abs(pit - 0.5) <= 0.4})
        print(name, flush=True)
    d = pd.DataFrame(recs)
    summ = d.groupby(["stat", "variant"]).agg(over_under_logloss=("ll", "mean"), coverage_50=("in50", "mean"),
                                              coverage_80=("in80", "mean")).round(4).reset_index()
    best = summ.loc[summ.groupby("stat")["over_under_logloss"].idxmin(), ["stat", "variant"]]
    cur = d[d["variant"] == "current"]
    hist = cur.groupby("stat")["pit"].apply(lambda x: np.histogram(x, bins=5, range=(0, 1))[0] / len(x)).apply(
        lambda h: " ".join(f"{v:.2f}" for v in h))
    md = ["# Stat distribution check (2025-26 held out)\n",
          "Coverage: share of actual results inside the model's middle 50% / 80% range (ideal 0.50 / 0.80). "
          "Log loss is for over/under at lines around the median (lower is better).\n",
          summ.to_markdown(index=False), "\n## Best variant per stat\n", best.to_markdown(index=False),
          "\n## Where actual results landed in the current distributions (5 bins, ideal 0.20 each)\n",
          hist.reset_index().rename(columns={"pit": "share per bin (low to high)"}).to_markdown(index=False)]
    (ROOT / "output" / "dist_check.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
