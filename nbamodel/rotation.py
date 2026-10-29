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


SEASON_HL, SEASON_W = 3, 2.0  # this season's games take over from the career signal as they accrue


def _signal(played: pd.Series, n_prior: pd.Series) -> np.ndarray:
    # blend with a weak prior so a player with 1-2 games isn't treated as certain
    k, prior = 2.0, 0.6
    n = np.minimum(n_prior, 20)
    return ((played.fillna(prior) * n + k * prior) / (n + k)).values


def _signals(d: pd.DataFrame) -> np.ndarray:
    """Pre-game signal per row of d (sorted by player, date; `played` NaN on rows still to come).
    Career EWM of "got minutes", then this season's EWM (shorter memory) weighted in as the season's
    games accrue: four straight coach's-decision DNPs to open a season now count for a lot more than
    last season's minutes (tested on 2025-26: logloss .2526 -> .2503, first 15 games .2929 -> .2850)."""
    ewm = d.groupby("player_id")["played"].transform(lambda s: s.shift().ewm(halflife=HALF_LIFE).mean())
    base = _signal(ewm, d.groupby("player_id").cumcount())
    g = d.groupby(["player_id", "season"])["played"]
    es = g.transform(lambda s: s.shift().ewm(halflife=SEASON_HL).mean()).fillna(0).values
    ns = g.cumcount().values
    return np.where(ns > 0, (es * ns + base * SEASON_W) / (ns + SEASON_W), base)


def history_signal(pg: pd.DataFrame) -> pd.DataFrame:
    """Per (game_id, player_id): the pre-game signal (for fitting) and played flag."""
    d = pg.sort_values(["player_id", "game_date"])[["game_id", "player_id", "season", "min"]].copy()
    d["played"] = (d["min"].fillna(0) > 0).astype(float)
    d["signal"] = _signals(d)
    return d


def current_signal(pg: pd.DataFrame, player_ids, season: str | None = None,
                   unseen: dict | None = None) -> pd.Series:
    """Signal for each player's next game (in `season`, default the latest in pg), from his full history.
    unseen: {player_id: n} team games this season he wasn't on the box score at all (not dressed),
    counted as games he didn't play."""
    d = pg[pg["player_id"].isin(player_ids)].sort_values(["player_id", "game_date"])
    d = d[["player_id", "season", "game_date", "min"]].copy()
    d["played"] = (d["min"].fillna(0) > 0).astype(float)
    season = season or (pg["season"].max() if len(pg) else None)
    if unseen:
        extra = [(p, season, 0.0) for p, n in unseen.items() for _ in range(int(n))]
        d = pd.concat([d, pd.DataFrame(extra, columns=["player_id", "season", "played"])], ignore_index=True)
    nxt = pd.DataFrame({"player_id": d["player_id"].unique(), "season": season, "played": np.nan})
    d = pd.concat([d, nxt], ignore_index=True)  # the game to predict goes last for each player
    d["_o"] = np.arange(len(d))
    d = d.sort_values(["player_id", "_o"])
    d["signal"] = _signals(d)
    sig = d.groupby("player_id")["signal"].last()
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
