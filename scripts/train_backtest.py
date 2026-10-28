"""Walk-forward backtest + final training.

  1. fit on <= 2023-24, calibrate noise on 2024-25, evaluate on 2025-26 (untouched)
  2. compare with closing market lines and naive baselines
  3. refit on everything for live use, keeping the out-of-sample noise calibration

Writes output/backtest_report.md and models/bundle.pkl.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA  # noqa: E402
from nbamodel.features import PROP_STATS  # noqa: E402
from nbamodel.models import predict_team, Bundle, predict_minutes, predict_rates, train  # noqa: E402
from nbamodel.odds import devig  # noqa: E402
from nbamodel.simulate import _scale_minutes  # noqa: E402

TRAIN_THRU, CALIB, TEST = "2023-24", "2024-25", "2025-26"


def team_normalise(d: pd.DataFrame, col: str) -> pd.Series:
    out = pd.Series(index=d.index, dtype=float)
    for _, g in d.groupby(["game_id", "team"]):
        out.loc[g.index] = _scale_minutes(g[col].values, 241.5)
    return out


def main():
    P = pd.read_parquet(DATA / "P.parquet")
    G = pd.read_parquet(DATA / "G.parquet")
    odds = pd.read_parquet(DATA / "odds.parquet")
    lines = []
    b = train(P, G, TRAIN_THRU, CALIB)
    b.save(ROOT / "models" / "bundle_backtest.pkl")
    rep = [f"# Backtest: trained through {TRAIN_THRU}, noise calibrated on {CALIB}, tested on {TEST}\n"]

    # ---------------- players (availability = who actually played, as known from pre-game actives)
    t = P[(P["season"] == TEST) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    t["pmin_raw"] = predict_minutes(b, t)
    t["pmin"] = team_normalise(t, "pmin_raw")
    r = predict_rates(b, t)
    rep.append("## Player projections (2025-26, every player-game, n=%d)\n" % len(t))
    rep.append("| stat | model MAE | baseline MAE (recent avg) | improvement |\n|---|---|---|---|")
    mae = lambda a, b_: float(np.mean(np.abs(a - b_)))  # noqa: E731
    m1, m0 = mae(t["min"], t["pmin"]), mae(t["min"], t["min_s"].fillna(t["min_l"]))
    rep.append(f"| minutes | {m1:.2f} | {m0:.2f} | {100*(1-m1/m0):.1f}% |")
    for s in PROP_STATS:
        pred = r[s] * t["pmin"]
        base = t[f"{s}_r_s"].fillna(0) * t["min_s"].fillna(0)
        a1, a0 = mae(t[s], pred), mae(t[s], base)
        rep.append(f"| {s} | {a1:.2f} | {a0:.2f} | {100*(1-a1/a0):.1f}% |")
    # bottom-up team points
    t["ppts"] = r["pts"] * t["pmin"]
    bu = t.groupby(["game_id", "team"])["ppts"].sum().rename("bu_pts").reset_index()

    # ---------------- games
    g = G[(G["season"] == TEST)].dropna(subset=["margin"]).copy()
    g = g[(g["h_season_gp"] >= 3) & (g["a_season_gp"] >= 3)]
    g["pm"], g["pt"] = predict_team(b, g)
    g = g.merge(bu.rename(columns={"team": "home", "bu_pts": "bu_h"}), on=["game_id", "home"], how="left")
    g = g.merge(bu.rename(columns={"team": "away", "bu_pts": "bu_a"}), on=["game_id", "away"], how="left")
    g = g.merge(odds[["game_date", "home", "away", "close_spread_home", "close_total", "ml_home", "ml_away"]],
                on=["game_date", "home", "away"], how="left")
    rep.append(f"\n## Games (2025-26, n={len(g)}; {g['close_spread_home'].notna().sum()} with closing lines)\n")
    rep.append(f"Calibrated noise: margin sd {b.margin_sd:.2f}, total sd {b.total_sd:.2f}\n")
    gm = g.dropna(subset=["close_spread_home"])
    rows = [("Margin MAE", mae(g["margin"], g["pm"]), mae(gm["margin"], -gm["close_spread_home"])),
            ("Total MAE", mae(g["total"], g["pt"]), mae(gm["total"], gm["close_total"]))]
    bu_tot = g["bu_h"] + g["bu_a"]
    rep.append("| metric | model (all games) | model (games w/ lines) | closing line |\n|---|---|---|---|")
    rep.append(f"| Margin MAE | {rows[0][1]:.2f} | {mae(gm['margin'], gm['pm']):.2f} | {rows[0][2]:.2f} |")
    rep.append(f"| Total MAE | {rows[1][1]:.2f} | {mae(gm['total'], gm['pt']):.2f} | {rows[1][2]:.2f} |")
    rep.append(f"| Total MAE (bottom-up from players) | {mae(g['total'], bu_tot):.2f} | | |")
    # win prob
    g["p_home"] = norm.cdf(g["pm"] / b.margin_sd)
    y = (g["margin"] > 0).astype(int)
    ll = lambda p, y_: float(-np.mean(y_ * np.log(p) + (1 - y_) * np.log(1 - p)))  # noqa: E731
    gl = g.dropna(subset=["ml_home", "ml_away"])
    pm_mkt = devig(gl["ml_home"], gl["ml_away"])[0]
    yl = (gl["margin"] > 0).astype(int)
    rep.append(f"\nWin probability log-loss: model {ll(g['p_home'].clip(.01,.99), y):.4f} (all), "
               f"model {ll(gl['p_home'].clip(.01,.99), yl):.4f} vs no-vig closing moneyline "
               f"{ll(np.clip(pm_mkt,.01,.99), yl):.4f} (same {len(gl)} games). "
               f"Brier: model {np.mean((gl['p_home']-yl)**2):.4f} vs market {np.mean((pm_mkt-yl)**2):.4f}.")
    # calibration table
    g["bin"] = pd.cut(g["p_home"], [0, .2, .35, .5, .65, .8, 1])
    cal = g.groupby("bin", observed=True).agg(n=("p_home", "size"), pred=("p_home", "mean"),
                                              actual=("margin", lambda m: (m > 0).mean()))
    rep.append("\nWin-prob calibration:\n\n| bucket | games | predicted | actual |\n|---|---|---|---|")
    for k, v in cal.iterrows():
        rep.append(f"| {k} | {v.n} | {v.pred:.3f} | {v.actual:.3f} |")
    # ATS / totals betting simulation at -110 against closing lines
    rep.append("\n## Betting simulation vs closing lines at -110 (2025-26)\n")
    rep.append("| market | edge threshold | bets | win % | ROI |\n|---|---|---|---|---|")
    for mk in ("spread", "total"):
        for thr in (0.0, 0.03, 0.05, 0.08):
            if mk == "spread":
                p = norm.cdf((gm["pm"] + gm["close_spread_home"]) / b.margin_sd)
                res = gm["margin"] + gm["close_spread_home"]
            else:
                p = 1 - norm.cdf((gm["close_total"] - gm["pt"]) / b.total_sd)
                res = gm["total"] - gm["close_total"]
            side = np.where(p > 0.5, 1, -1)
            pe = np.maximum(p, 1 - p)
            sel = (pe - 0.5238 >= thr) & (res != 0)
            win = (np.sign(res) == side)[sel]
            n = int(sel.sum())
            roi = (win.sum() * (100 / 110) - (n - win.sum())) / max(n, 1)
            rep.append(f"| {mk} | {thr:.0%} | {n} | {100*win.mean() if n else 0:.1f}% | {100*roi:+.1f}% |")
    rep.append("\nBreak-even at -110 is 52.4%. Closing lines are the sharpest benchmark; beating "
               "openers or soft books is easier than this.")
    report = "\n".join(rep)
    (ROOT / "output").mkdir(exist_ok=True)
    (ROOT / "output/backtest_report.md").write_text(report)
    print(report)

    # ---------------- final model on everything, keep held-out noise calibration
    final = train(P, G, P["season"].max(), None)
    for k in ("min_sd", "disp", "margin_sd", "total_sd", "score_corr"):
        setattr(final, k, getattr(b, k))
    final.save()
    print("saved final bundle trained through", final.trained_through)
    from nbamodel import rotation
    from nbamodel.dataset import load_history
    pg, _ = load_history()
    seasons = sorted(pg["season"].unique())
    rotation.fit(pg[pg["season"] >= seasons[-3]], seasons[-2])  # last complete season
    print("saved rotation model")


if __name__ == "__main__":
    main()
