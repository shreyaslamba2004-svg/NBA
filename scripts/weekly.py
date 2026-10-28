"""Weekly job: grade the logs, refit the blend, retrain the models (with a safety check), alert.

  1. nbamodel.monitor: accuracy, best-bet ROI and closing-line value, blend refit -> output/monitor.md
  2. rebuild features from all history including this season's games
  3. safety check: a probe trained only on past seasons must still project this season's games
     about as well as the backtest did (output/backtest_report.md). If it doesn't, something is
     wrong with the data and the old model is kept.
  4. retrain on everything (noise calibration carried over), refit the chance-to-play model
Alerts go to output/alerts.txt; the workflow opens a GitHub issue when it isn't empty.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel import monitor, rotation  # noqa: E402
from nbamodel.dataset import DATA, build, load_history  # noqa: E402
from nbamodel.models import Bundle, predict_minutes, predict_rates, predict_team, train  # noqa: E402
from scripts.train_backtest import team_normalise  # noqa: E402

# held-out benchmarks from the backtest, with headroom; a probe worse than this means bad data
LIMITS = {"minutes MAE": 5.2, "pts MAE": 5.2, "margin MAE": 12.8}
MIN_GAMES = 120


def probe_check(P: pd.DataFrame, G: pd.DataFrame, season: str) -> tuple[dict, list[str]]:
    seasons = sorted(P["season"].unique())
    prev = seasons[seasons.index(season) - 1]
    g = G[(G["season"] == season) & (G["h_season_gp"] >= 3) & (G["a_season_gp"] >= 3)].dropna(subset=["margin"])
    if len(g) < MIN_GAMES:
        return {"games": len(g)}, []
    b = train(P, G, prev, None)
    t = P[(P["season"] == season) & (P["min"] > 0) & (P["gp"] >= 3)].copy()
    t["pmin_raw"] = predict_minutes(b, t)
    t["pmin"] = team_normalise(t, "pmin_raw")
    r = predict_rates(b, t)
    pm, _ = predict_team(b, g)
    m = {"games": len(g), "minutes MAE": float(np.abs(t["min"] - t["pmin"]).mean()),
         "pts MAE": float(np.abs(t["pts"] - r["pts"] * t["pmin"]).mean()),
         "margin MAE": float(np.abs(g["margin"] - pm).mean())}
    bad = [f"{k} {m[k]:.2f} is above the safety limit {v}" for k, v in LIMITS.items() if m[k] > v]
    return m, bad


OFFSEASON_DAYS = 10  # no completed games for this long (off-season, long breaks): nothing to retrain on


def main():
    alerts = monitor.run(date.today())
    # weekly heartbeat commit: GitHub switches off schedules in repos with no activity for 60 days
    (ROOT / "output" / "heartbeat.txt").write_text(f"weekly job ran {date.today().isoformat()}\n")
    pg, g = load_history()
    last_game = pd.to_datetime(g.dropna(subset=["home_pts"])["game_date"]).max()
    if (pd.Timestamp(date.today()) - last_game).days > OFFSEASON_DAYS:
        msg = f"No games since {last_game.date()}: off-season or a break, model left as is."
        with open(ROOT / "output" / "monitor.md", "a") as f:
            f.write(f"\n## Weekly retrain\n\n{msg}\n")
        (ROOT / "output" / "alerts.txt").write_text("")
        print(msg)
        return
    P, G = build(pg, g)
    season = P["season"].max()
    m, bad = probe_check(P, G, season)
    lines = ["\n## Weekly retrain\n", "Safety check (model trained on past seasons, tested on this season): " +
             ", ".join(f"{k} {v:.2f}" if isinstance(v, float) else f"{k} {v}" for k, v in m.items())]
    if bad:
        alerts += ["Retrain skipped, old model kept: " + "; ".join(bad)]
        lines.append("**Kept the previous model:** " + "; ".join(bad))
    else:
        old = Bundle.load()
        new = train(P, G, season, None)
        for k in ("min_sd", "disp", "margin_sd", "total_sd", "score_corr"):
            setattr(new, k, getattr(old, k))
        new.save()
        seasons = sorted(pg["season"].unique())
        rotation.fit(pg[pg["season"] >= seasons[-3]], seasons[-2])
        lines.append(f"Retrained on all games through {date.today()} and saved.")
    with open(ROOT / "output" / "monitor.md", "a") as f:
        f.write("\n".join(lines) + "\n")
    (ROOT / "output" / "alerts.txt").write_text("\n".join(alerts))
    print("\n".join(lines))
    print("alerts:", alerts)


if __name__ == "__main__":
    main()
