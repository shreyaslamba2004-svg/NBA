"""Point-in-time backtest: availability from the ~5pm ET official injury report, not the box score.

The standard backtest knows exactly who played. Live, the model only knows what the injury
report says before tip, so late scratches and questionable players are surprises. This rebuilds
the absence features from the reports (Out/Doubtful = absent; Questionable/Probable = available,
as live) and re-scores the backtest bundle on 2024-25 and 2025-26. It then fits the model/market
blend weights used for bet decisions on 2024-25 and checks them on 2025-26.

Writes output/pit_backtest.md and models/blend.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.dataset import DATA, build, load_history  # noqa: E402
from nbamodel.models import Bundle, predict_team  # noqa: E402
from nbamodel.odds import american_to_prob  # noqa: E402
from nbamodel.sources.live import norm_name  # noqa: E402

SEASONS = ["2024-25", "2025-26"]
FIT, TEST = "2024-25", "2025-26"


def pit_out_map(pg: pd.DataFrame, g: pd.DataFrame) -> tuple[dict, dict]:
    rep = pd.read_parquet(DATA / "injury_reports.parquet")
    rep = rep[rep["status"].isin(["Out", "Doubtful"])].copy()
    rep["game_date"] = pd.to_datetime(rep["game_date"].fillna(rep["report_date"])).dt.normalize()
    gl = pd.concat([g[["game_id", "game_date", "season", "home"]].rename(columns={"home": "team"}),
                    g[["game_id", "game_date", "season", "away"]].rename(columns={"away": "team"})])
    gl["game_date"] = pd.to_datetime(gl["game_date"]).dt.normalize()
    gl = gl[gl["season"].isin(SEASONS)]
    rep = rep.merge(gl, on=["game_date", "team"])
    # names -> ids: full names where any season has them, else surname within team-season
    full = pg[pg["player_name"].str.contains(" ", na=False)].sort_values("game_date")
    by_full = dict(zip(full["player_name"].map(norm_name), full["player_id"]))
    ts = pg[pg["season"].isin(SEASONS)].drop_duplicates(["season", "team", "player_id"])
    by_last: dict = {}
    for r in ts.itertuples(index=False):
        nm = str(r.player_name)
        by_last.setdefault((r.season, r.team, norm_name(nm.split(" ")[-1] if " " in nm else nm)), set()).add(r.player_id)
    ids = []
    for r in rep.itertuples(index=False):
        pid = by_full.get(r.key)
        if pid is None:
            last = norm_name(r.player.split(",")[0]) if "," in r.player else None
            c = by_last.get((r.season, r.team, last), set())
            pid = next(iter(c)) if len(c) == 1 else None
        ids.append(pid)
    rep["player_id"] = ids
    stats = {"report rows (Out/Doubtful)": len(rep), "matched to a player": int(rep["player_id"].notna().sum()),
             "games covered": int(rep["game_id"].nunique())}
    rep = rep.dropna(subset=["player_id"])
    out = rep.groupby(["game_id", "team"])["player_id"].apply(lambda s: set(s.astype(int))).to_dict()
    # games with a report but nobody ruled out still count as covered
    for r in gl[gl["game_id"].isin(rep["game_id"])].itertuples(index=False):
        out.setdefault((r.game_id, r.team), set())
    return out, stats


def score(G: pd.DataFrame, b: Bundle, odds: pd.DataFrame, season: str) -> pd.DataFrame:
    g = G[(G["season"] == season) & (G["h_season_gp"] >= 3) & (G["a_season_gp"] >= 3)].dropna(subset=["margin"]).copy()
    g["mu_margin"], g["mu_total"] = predict_team(b, g)
    g = g.merge(odds[["game_date", "home", "away", "close_spread_home", "close_total", "ml_home", "ml_away"]],
                on=["game_date", "home", "away"], how="left")
    g["p_home_model"] = norm.cdf(g["mu_margin"] / b.margin_sd)
    ih, ia = american_to_prob(g["ml_home"].astype(float)), american_to_prob(g["ml_away"].astype(float))
    g["p_home_mkt"] = ih / (ih + ia)
    # P(home covers the closing spread), model; the market prices it at ~50%
    g["p_cover_model"] = norm.cdf((g["mu_margin"] + g["close_spread_home"]) / b.margin_sd)
    g["p_over_model"] = norm.cdf((g["mu_total"] - g["close_total"]) / b.total_sd)
    return g


def metrics(g: pd.DataFrame) -> dict:
    lg = g.dropna(subset=["close_spread_home"])
    res = lg["margin"] + lg["close_spread_home"]
    side = np.sign(lg["mu_margin"] + lg["close_spread_home"])
    ml = g.dropna(subset=["p_home_mkt"])
    y = (ml["margin"] > 0).astype(float)
    ll = lambda p: float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))  # noqa: E731
    return {"games": len(g), "margin MAE": np.abs(g["margin"] - g["mu_margin"]).mean(),
            "total MAE": np.abs(g["total"] - g["mu_total"]).mean(),
            "closing spread MAE": np.abs(lg["margin"] + lg["close_spread_home"]).mean(),
            "ATS win %": 100 * (np.sign(res) == side)[res != 0].mean(),
            "win logloss model": ll(ml["p_home_model"].clip(.01, .99)), "win logloss market": ll(ml["p_home_mkt"])}


def fit_weight(p_model, p_mkt, y) -> float:
    def nll(w):
        p = np.clip(w * p_model + (1 - w) * p_mkt, 1e-4, 1 - 1e-4)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
    return float(minimize_scalar(nll, bounds=(0, 1), method="bounded").x)


def blend_ll(w, p_model, p_mkt, y) -> float:
    p = np.clip(w * p_model + (1 - w) * p_mkt, 1e-4, 1 - 1e-4)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def main():
    pg, g = load_history()
    pit_out, stats = pit_out_map(pg, g)
    print(stats, flush=True)
    P_pit, G_pit = build(pg, g, pit_out=pit_out)
    G_box = pd.read_parquet(DATA / "G.parquet")
    b = Bundle.load(ROOT / "models" / "bundle_backtest.pkl")
    odds = pd.read_parquet(DATA / "odds.parquet")
    rows, scored = [], {}
    for season in SEASONS:
        for name, G in (("box score (knows who played)", G_box), ("injury report (point-in-time)", G_pit)):
            s = score(G, b, odds, season)
            scored[(season, name)] = s
            rows.append({"season": season, "availability from": name, **metrics(s)})
    res = pd.DataFrame(rows).round(3)

    # blend weights, fit on FIT (point-in-time), checked on TEST
    pit = "injury report (point-in-time)"
    fit, test = scored[(FIT, pit)], scored[(TEST, pit)]
    out, weights = [], {}
    for mkt, pm, pk, yfn in (
            ("moneyline", "p_home_model", "p_home_mkt", lambda d: (d["margin"] > 0)),
            ("spread", "p_cover_model", None, lambda d: (d["margin"] + d["close_spread_home"] > 0)),
            ("total", "p_over_model", None, lambda d: (d["total"] > d["close_total"]))):
        cols = [pm] + ([pk] if pk else []) + (["close_spread_home"] if mkt == "spread" else []) + (
            ["close_total"] if mkt == "total" else [])
        f, t = fit.dropna(subset=cols), test.dropna(subset=cols)
        if mkt == "spread":
            f = f[f["margin"] + f["close_spread_home"] != 0]
            t = t[t["margin"] + t["close_spread_home"] != 0]
        if mkt == "total":
            f, t = f[f["total"] != f["close_total"]], t[t["total"] != t["close_total"]]
        mf = f[pk].values if pk else np.full(len(f), 0.5)
        mt = t[pk].values if pk else np.full(len(t), 0.5)
        w = fit_weight(f[pm].values, mf, yfn(f).astype(float).values)
        weights[mkt] = round(w, 3)
        yt = yfn(t).astype(float).values
        out.append({"market": mkt, "fit games": len(f), "test games": len(t), "fitted model weight": round(w, 3),
                    "test logloss market only": round(blend_ll(0, t[pm].values, mt, yt), 4),
                    "test logloss blend": round(blend_ll(w, t[pm].values, mt, yt), 4),
                    "test logloss model only": round(blend_ll(1, t[pm].values, mt, yt), 4)})
    bl = pd.DataFrame(out)
    (ROOT / "models" / "blend.json").write_text(json.dumps({"game": weights, "fit_season": FIT}, indent=1))
    md = ["# Point-in-time backtest\n",
          "Backtest bundle trained through 2023-24. Point-in-time rows rebuild every absence feature from the ~5pm ET "
          "official injury report (Out/Doubtful absent, Questionable/Probable available), so late scratches are "
          "surprises, exactly as live.\n",
          "Report matching: " + ", ".join(f"{k} {v}" for k, v in stats.items()) + "\n",
          res.to_markdown(index=False), "\n## Model/market blend (fit on 2024-25, tested on 2025-26)\n",
          "Weight = share given to the model; the rest goes to the no-vig closing market. Lower logloss is better.\n",
          bl.to_markdown(index=False), "\nSaved to models/blend.json and used by nbamodel/edges.py.\n"]
    (ROOT / "output" / "pit_backtest.md").write_text("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
