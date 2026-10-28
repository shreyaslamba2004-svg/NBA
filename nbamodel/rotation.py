"""Chance an available player actually gets minutes (vs a coach's-decision DNP).

The minutes model predicts minutes *given* a player plays. Live, every healthy roster player is
available, so without this the deep bench soaks up minutes and starters' projections sag.
Signal: a leak-free EWMA of "got minutes" over the player's previous available games, mapped to
a probability by an isotonic fit on the previous season (models/rotation_iso.pkl).
"""
from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression

PATH = Path(__file__).resolve().parents[1] / "models" / "rotation_iso.pkl"
HALF_LIFE = 5


def _signal(played: pd.Series, n_prior: pd.Series) -> np.ndarray:
    # blend with a weak prior so a player with 1-2 games isn't treated as certain
    k, prior = 2.0, 0.6
    n = np.minimum(n_prior, 20)
    return ((played.fillna(prior) * n + k * prior) / (n + k)).values


def history_signal(pg: pd.DataFrame) -> pd.DataFrame:
    """Per (game_id, player_id): the pre-game signal (for fitting) and played flag."""
    d = pg.sort_values(["player_id", "game_date"])[["game_id", "player_id", "season", "min"]].copy()
    d["played"] = (d["min"].fillna(0) > 0).astype(float)
    d["ewm"] = d.groupby("player_id")["played"].transform(lambda s: s.shift().ewm(halflife=HALF_LIFE).mean())
    d["n_prior"] = d.groupby("player_id").cumcount()
    d["signal"] = _signal(d["ewm"], d["n_prior"])
    return d


def current_signal(pg: pd.DataFrame, player_ids) -> pd.Series:
    """Signal for the next game, from each player's full history."""
    d = pg[pg["player_id"].isin(player_ids)].sort_values(["player_id", "game_date"])
    played = (d["min"].fillna(0) > 0).astype(float)
    ewm = played.groupby(d["player_id"]).apply(lambda s: s.ewm(halflife=HALF_LIFE).mean().iloc[-1])
    n = d.groupby("player_id").size()
    sig = pd.Series(_signal(ewm, n.reindex(ewm.index)), index=ewm.index)
    return sig.reindex(player_ids).fillna(0.6)  # no history: rookies, new signings


def fit(pg: pd.DataFrame, season: str) -> IsotonicRegression:
    d = history_signal(pg)
    d = d[d["season"] == season]
    iso = IsotonicRegression(y_min=0.02, y_max=0.995, out_of_bounds="clip").fit(d["signal"], d["played"])
    PATH.parent.mkdir(exist_ok=True)
    PATH.write_bytes(pickle.dumps(iso))
    return iso


def prob(signal) -> np.ndarray:
    iso = pickle.loads(PATH.read_bytes())
    return iso.predict(np.asarray(signal, dtype=float))
