"""Retest the blowout-minutes adjustment at lighter strengths.

Configs: off, or the historical curve raised to a power k (0.5 = half strength), with the independent
minutes spread optionally shrunk (part of that spread is game script, which the curve now models).
Choose on 2024-25 games, judge on 2025-26 games; the backtest bundle is trained <= 2023-24, so both are
held out. Writes output/blowout_strength.md.
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

STATS = ["pts", "reb", "ast", "fg3m", "min"]
CONFIGS = {"off": None, "k=0.5": (0.5, 1.0), "k=0.5, sd x0.95": (0.5, 0.95), "k=1": (1.0, 1.0),
           "k=1, sd x0.9": (1.0, 0.9)}


def run(b, P, G, season, n_games, n_sims=4000):
    bundles = {}
    for name, cfg in CONFIGS.items():
        bb = copy.copy(b)
        bb.use_blowout = cfg is not None
        if cfg:
            bb.blowout_k, bb.blowout_sd_scale = cfg
        bundles[name] = bb
    g = G[(G["season"] == season) & (G["h_season_gp"] >= 3) & (G["a_season_gp"] >= 3)].dropna(subset=["margin"])
    g = g.sample(n_games, random_state=7)
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
        seed = int(gr.game_id) % 2**31
        sims = {name: simulate_game(game, gp, bb, n=n_sims, seed=seed) for name, bb in bundles.items()}
        actual = gp.set_index("player_id")
        for j, p in enumerate(sims["off"]["players"]):
            a = actual.loc[p["player_id"]]
            for s in STATS:
                base = p["draws"][s]
                for line in np.floor(np.quantile(base, [0.25, 0.5, 0.75])) + 0.5:  # main line and alt lines
                    row = {"pmin": a["pmin"], "stat": s, "y": float(a[s] > line)}
                    for name, sim in sims.items():
                        row[name] = np.clip((sim["players"][j]["draws"][s] > line).mean(), 0.01, 0.99)
                    rows.append(row)
    d = pd.DataFrame(rows)
    d["role"] = np.where(d["pmin"] >= 30, "starters 30+", np.where(d["pmin"] >= 15, "rotation 15-30", "bench <15"))
    return d


def ll(p, y):
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def table(d):
    out = []
    for grp, x in [("all props (no minutes)", d[d["stat"] != "min"])] + \
            [(f"{r}, props", d[(d["role"] == r) & (d["stat"] != "min")]) for r in sorted(d["role"].unique())]:
        rec = {"group": grp, "n": len(x)}
        for name in CONFIGS:
            rec[name] = round(ll(x[name], x["y"]), 5)
        out.append(rec)
    return pd.DataFrame(out)


def main(n_games: int = 250):
    b = Bundle.load(ROOT / "models" / "bundle_backtest.pkl")
    P = pd.read_parquet(DATA / "P.parquet")
    G = pd.read_parquet(DATA / "G.parquet")
    fit = table(run(b, P, G, "2024-25", n_games))
    test = table(run(b, P, G, "2025-26", n_games))
    best = min(CONFIGS, key=lambda c: fit.loc[0, c])
    md = ["# Blowout minutes at lighter strengths (logloss, lower is better)\n",
          f"{n_games} games per season, P(over) at three lines per player and stat. Pick on 2024-25, judge on "
          f"2025-26. Picked on 2024-25: **{best}**.\n",
          "## 2024-25 (selection)\n", fit.to_markdown(index=False),
          "\n## 2025-26 (test)\n", test.to_markdown(index=False)]
    (ROOT / "output" / "blowout_strength.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main(*(int(x) for x in sys.argv[1:2]))
