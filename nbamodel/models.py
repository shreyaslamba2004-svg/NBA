"""Model training: player minutes, per-minute stat rates, and team margin/total.

All models are gradient-boosted trees (LightGBM) on the leak-free features in dataset.py.
Uncertainty parameters for the simulator (minutes sd, count over-dispersion, score sds)
are estimated from out-of-sample residuals, never from training fit.
"""
from __future__ import annotations

import pickle
from dataclasses import dataclass, field
from pathlib import Path

import lightgbm as lgb
import numpy as np
import pandas as pd

from .dataset import game_feats, min_feats, rate_feats
from .features import PROP_STATS

MODELS = Path(__file__).resolve().parents[1] / "models"
SIM_STATS = PROP_STATS + ["fga", "fta"]

LGB_PARAMS = dict(n_estimators=600, learning_rate=0.03, num_leaves=63, min_child_samples=100,
                  subsample=0.8, subsample_freq=1, colsample_bytree=0.8, reg_lambda=1.0, verbose=-1)


@dataclass
class Bundle:
    minutes: lgb.LGBMRegressor | None = None
    rates: dict = field(default_factory=dict)
    rate_features: dict = field(default_factory=dict)
    min_features: list = field(default_factory=list)
    game_features: list = field(default_factory=list)
    margin: lgb.LGBMRegressor | None = None
    total: lgb.LGBMRegressor | None = None
    # uncertainty
    min_sd: dict = field(default_factory=dict)      # by predicted-minutes bucket
    disp: dict = field(default_factory=dict)        # NB dispersion k per stat
    margin_sd: float = 12.5
    total_sd: float = 18.0
    score_corr: float = 0.0
    # minutes multiplier by final |margin|, for players by projected-minutes role (see fit_blowout)
    blowout: dict = field(default_factory=dict)
    use_blowout: bool = False  # off: did not improve held-out prop probabilities (output/blowout_backtest.md)
    trained_through: str = ""
    rate_base_fill: dict = field(default_factory=dict)  # set = rate models predict a multiplier

    def save(self, path: Path | None = None):
        path = path or MODELS / "bundle.pkl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path: Path | None = None) -> "Bundle":
        with open(path or MODELS / "bundle.pkl", "rb") as f:
            return pickle.load(f)


def _played(P: pd.DataFrame) -> pd.DataFrame:
    # need at least a few prior games for the form features to mean anything
    return P[(P["min"] > 0) & (P["gp"] >= 3)]


def season_weight(season: pd.Series, half_life: float | None) -> np.ndarray:
    """Down-weight older seasons: weight halves every `half_life` seasons (None = equal)."""
    if not half_life:
        return np.ones(len(season))
    y = season.str[:4].astype(int)
    return 0.5 ** ((y.max() - y) / half_life).values


def fit_minutes(P: pd.DataFrame, half_life: float | None = None) -> lgb.LGBMRegressor:
    d = _played(P).copy()
    # confirmed starter: known in history, only sometimes known live (late news) -> train with
    # half the values hidden so the model works with or without it
    rng = np.random.default_rng(0)
    d["starter_today"] = np.where(rng.random(len(d)) < 0.5, d["starter"].astype(float), np.nan)
    m = lgb.LGBMRegressor(objective="regression", **LGB_PARAMS)
    m.fit(d[min_feats()], d["min"], sample_weight=season_weight(d["season"], half_life))
    return m


def rate_base(P: pd.DataFrame, stat: str, fill: float | None = None) -> pd.Series:
    """Player's own recent per-minute rate: the starting point the rate model adjusts."""
    rs, rl = P[f"{stat}_r_s"], P[f"{stat}_r_l"]
    base = 0.6 * rs.fillna(rl) + 0.4 * rl.fillna(rs)
    if fill is not None:
        base = base.fillna(fill)
    return base.clip(lower=0.005)


def fit_rates(P: pd.DataFrame, half_life: float | None = None) -> tuple[dict, dict]:
    """Per-minute rate models, fit as a multiplier on the player's own recent rate.

    Predicting the rate directly made the trees shrink the best players toward average (top-1%
    passers ~3.5% low, shooters ~11% low on held-out games); predicting the adjustment instead
    halves that and slightly lowers overall error (see README)."""
    d = _played(P)
    d = d[d["min"] >= 4]
    out, fill = {}, {}
    for s in SIM_STATS:
        f = rate_feats(s)
        fill[s] = float((d[s].sum() / d["min"].sum()))
        base = rate_base(d, s, fill[s])
        w = d["min"].values * base.values * season_weight(d["season"], half_life)
        m = lgb.LGBMRegressor(objective="regression", **LGB_PARAMS)
        m.fit(d[f], (d[s] / d["min"]) / base, sample_weight=w)
        out[s] = m
    return out, fill


def fit_team(G: pd.DataFrame, half_life: float | None = None) -> tuple[lgb.LGBMRegressor, lgb.LGBMRegressor]:
    d = G.dropna(subset=["margin"])
    d = d[(d["h_season_gp"] >= 3) & (d["a_season_gp"] >= 3)]
    w = season_weight(d["season"], half_life)
    params = LGB_PARAMS | dict(n_estimators=400, num_leaves=15, min_child_samples=200, learning_rate=0.02)
    F = game_feats()
    mm = lgb.LGBMRegressor(objective="regression", **params).fit(d[F], d["margin"], sample_weight=w)
    tt = lgb.LGBMRegressor(objective="regression", **params).fit(d[F], d["total"], sample_weight=w)
    return mm, tt


BLOWOUT_EDGES = np.array([0, 4, 8, 12, 16, 20, 25, 30, 80])
ROLE_EDGES = [0, 15, 24, 30, 48]


def fit_blowout(P: pd.DataFrame, G: pd.DataFrame) -> dict:
    """How a player's minutes move with the final margin, by role (projected-minute band).

    Ratio of actual to typical minutes in each |margin| bucket, divided by the role's overall
    mean so the curve redistributes minutes across game scripts without changing the average.
    Regulation games only (OT inflates minutes for reasons unrelated to blowouts).
    """
    d = P[(P["gp"] >= 5) & (P["min"] > 0)][["game_id", "min", "min_s"]].merge(
        G[["game_id", "margin", "periods"]], on="game_id")
    d = d[(d["periods"] == 4) & (d["min_s"] > 0)]
    d["ratio"] = (d["min"] / d["min_s"]).clip(0, 3)
    d["role"] = pd.cut(d["min_s"], ROLE_EDGES, labels=False, include_lowest=True)
    d["mb"] = pd.cut(d["margin"].abs(), BLOWOUT_EDGES, labels=False, include_lowest=True)
    tab = d.groupby(["role", "mb"])["ratio"].mean().unstack()
    tab = tab.div(d.groupby("role")["ratio"].mean(), axis=0)
    return {int(r): tab.loc[r].reindex(range(len(BLOWOUT_EDGES) - 1)).ffill().bfill().values.tolist()
            for r in tab.index}


def predict_minutes(b: Bundle, P: pd.DataFrame) -> np.ndarray:
    F = b.min_features or min_feats()
    if "starter_today" in F and "starter_today" not in P:
        P = P.assign(starter_today=np.nan)
    return np.clip(b.minutes.predict(P[F]), 0, 48)


def predict_team(b: Bundle, G: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    F = b.game_features or game_feats()
    return b.margin.predict(G[F]), b.total.predict(G[F])


def predict_rates(b: Bundle, P: pd.DataFrame) -> pd.DataFrame:
    feats = lambda s: b.rate_features.get(s) or rate_feats(s)  # noqa: E731
    if getattr(b, "rate_base_fill", None):  # ratio models: multiplier on the player's own recent rate
        return pd.DataFrame({s: np.clip(m.predict(P[feats(s)]), 0, None) * rate_base(P, s, b.rate_base_fill[s]).values
                             for s, m in b.rates.items()}, index=P.index)
    return pd.DataFrame({s: np.clip(m.predict(P[feats(s)]), 0, None) for s, m in b.rates.items()},
                        index=P.index)


def calibrate(b: Bundle, Pv: pd.DataFrame, Gv: pd.DataFrame):
    """Estimate simulator noise parameters on a held-out season."""
    d = _played(Pv).copy()
    d["pmin"] = predict_minutes(b, d)
    d["bucket"] = pd.cut(d["pmin"], [0, 10, 18, 26, 32, 48], labels=False, include_lowest=True)
    b.min_sd = (d["min"] - d["pmin"]).groupby(d["bucket"]).std().to_dict()
    r = predict_rates(b, d)
    for s in SIM_STATS:
        mu = (r[s] * d["min"]).clip(lower=1e-3)  # condition on actual minutes: count noise only
        y = d[s]
        excess = ((y - mu) ** 2 - mu).sum()
        k = (mu ** 2).sum() / excess if excess > 0 else 1e6
        b.disp[s] = float(np.clip(k, 0.5, 1e6))
    g = Gv.dropna(subset=["margin"])
    g = g[(g["h_season_gp"] >= 3) & (g["a_season_gp"] >= 3)]
    pm, pt = predict_team(b, g)
    em, et = g["margin"] - pm, g["total"] - pt
    b.margin_sd, b.total_sd = float(em.std()), float(et.std())
    # implied home/away score residual correlation from margin & total residual variances
    vh = (et.var() + em.var() + 2 * np.cov(et, em)[0, 1]) / 4
    va = (et.var() + em.var() - 2 * np.cov(et, em)[0, 1]) / 4
    b.score_corr = float(((et.var() - em.var()) / 4) / np.sqrt(vh * va))


def train(P: pd.DataFrame, G: pd.DataFrame, through_season: str, calib_season: str | None,
          from_season: str = "2010-11", half_life: float | None = None) -> Bundle:
    """Fit on from_season..through_season (optionally recency-weighted); calibrate noise on
    calib_season (held out) if given."""
    sel_p = (P["season"] <= through_season) & (P["season"] >= from_season)
    sel_g = (G["season"] <= through_season) & (G["season"] >= from_season)
    tr_p, tr_g = P[sel_p], G[sel_g]
    b = Bundle(trained_through=through_season)
    b.minutes = fit_minutes(tr_p, half_life)
    b.rates, b.rate_base_fill = fit_rates(tr_p, half_life)
    b.rate_features = {s: rate_feats(s) for s in SIM_STATS}
    b.min_features, b.game_features = min_feats(), game_feats()
    b.margin, b.total = fit_team(tr_g, half_life)
    b.blowout = fit_blowout(tr_p[tr_p["season"] >= "2016-17"], tr_g)
    if calib_season:
        calibrate(b, P[P["season"] == calib_season], G[G["season"] == calib_season])
    return b
