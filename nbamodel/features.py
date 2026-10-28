"""Leak-free (strictly pre-game) features for players and teams.

Every rolling quantity is shifted so that a row only sees games played before it. The same
functions run on history (for training) and on history + today's slate (for projections):
today's rows simply have NaN outcomes.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

RATE_STATS = ["pts", "reb", "ast", "fg3m", "stl", "blk", "tov", "fga", "fta", "fg3a", "oreb",
              "dreb", "ftm", "pf"]
PROP_STATS = ["pts", "reb", "ast", "fg3m", "stl", "blk", "tov"]
SHORT_HL, LONG_HL = 6, 25  # EWMA half-lives in games


def _ewm(s: pd.Series, groups: pd.Series, hl: float) -> pd.Series:
    """EWMA of past values within group (excludes current row)."""
    return s.groupby(groups).transform(lambda x: x.shift(1).ewm(halflife=hl, ignore_na=True).mean())


def team_game_table(pg: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """One row per team per game with box totals, possessions and opponent."""
    played = pg[pg["min"] > 0]
    t = played.groupby(["game_id", "team"], as_index=False)[
        ["pts", "fga", "fta", "oreb", "dreb", "tov", "fg3m", "fg3a", "ast", "reb", "stl", "blk", "pf"]].sum()
    t["poss"] = t["fga"] - t["oreb"] + t["tov"] + 0.44 * t["fta"]
    g = games[["game_id", "game_date", "season", "playoff", "home", "away", "home_pts", "away_pts",
               "periods"]]
    t = t.merge(g, on="game_id")
    t["is_home"] = (t["team"] == t["home"]).astype(int)
    t["opp"] = np.where(t["is_home"] == 1, t["away"], t["home"])
    t = t.drop(columns=["home", "away", "home_pts", "away_pts"])
    o = t[["game_id", "team"] + [c for c in t.columns if c in
          ("pts", "poss", "fga", "fta", "oreb", "dreb", "tov", "fg3m", "fg3a", "ast", "reb", "stl", "blk")]]
    o = o.rename(columns={c: f"opp_{c}" for c in o.columns if c not in ("game_id",)}).rename(
        columns={"opp_team": "opp"})
    t = t.merge(o, on=["game_id", "opp"])
    t["poss_avg"] = (t["poss"] + t["opp_poss"]) / 2
    return t.sort_values(["game_date", "game_id"]).reset_index(drop=True)


def add_schedule_features(df: pd.DataFrame, key: str) -> pd.DataFrame:
    """Rest days, back-to-back, games in last 4/7 days for each `key` (team or player)."""
    df = df.sort_values(["game_date", "game_id"])
    prev = df.groupby(key)["game_date"].shift(1)
    df["rest_days"] = (df["game_date"] - prev).dt.days.clip(upper=10).fillna(10)
    df["b2b"] = (df["rest_days"] == 1).astype(int)
    for w in (4, 6, 7):
        df[f"g_last{w}d"] = _games_in_window(df, key, w)
    return df


def _games_in_window(df: pd.DataFrame, key: str, days: int) -> np.ndarray:
    out = np.zeros(len(df))
    pos = {i: n for n, i in enumerate(df.index)}
    for _, g in df.groupby(key):
        d = g["game_date"].values.astype("datetime64[D]").astype(np.int64)
        left = np.searchsorted(d, d - days, side="left")
        cnt = np.arange(len(d)) - left
        for idx, c in zip(g.index, cnt):
            out[pos[idx]] = c
    return out


def team_features(tg: pd.DataFrame) -> pd.DataFrame:
    """Pre-game team ratings (offence/defence per 100 possessions, pace), EWMA and season-to-date."""
    tg = tg.sort_values(["game_date", "game_id"]).copy()
    tg["ortg"] = 100 * tg["pts"] / tg["poss_avg"]
    tg["drtg"] = 100 * tg["opp_pts"] / tg["poss_avg"]
    tg["pace"] = tg["poss_avg"] * 48 / (48 + 5 * (tg["periods"] - 4))
    tg["net"] = tg["ortg"] - tg["drtg"]
    tg["three_rate"] = tg["fg3a"] / tg["fga"]
    tg["three_rate_allowed"] = tg["opp_fg3a"] / tg["opp_fga"]
    grp = tg["team"]
    # per-possession allowed stats feed player opponent adjustments
    for s in ("reb", "ast", "fg3m", "stl", "blk", "tov", "pts"):
        tg[f"allow_{s}_pp"] = tg[f"opp_{s}"] / tg["poss_avg"]
    cols = ["ortg", "drtg", "pace", "net", "three_rate", "three_rate_allowed"] + \
           [c for c in tg.columns if c.startswith("allow_")]
    for c in cols:
        tg[f"{c}_s"] = _ewm(tg[c], grp, 8)
        tg[f"{c}_l"] = _ewm(tg[c], grp, 30)
    # season-to-date games count (early-season shrinkage signal)
    tg["season_gp"] = tg.groupby(["team", "season"]).cumcount()
    tg = add_schedule_features(tg, "team")
    return tg


def player_features(pg: pd.DataFrame) -> pd.DataFrame:
    """Per player-game pre-game features. Uses only games the player actually played in."""
    pg = pg.sort_values(["game_date", "game_id"]).copy()
    p = pg[pg["min"] > 0].copy() if "is_target" not in pg else pg[(pg["min"] > 0) | pg["is_target"]].copy()
    grp = p["player_id"]
    p["min_s"] = _ewm(p["min"], grp, SHORT_HL)
    p["min_l"] = _ewm(p["min"], grp, LONG_HL)
    p["min_last"] = p.groupby("player_id")["min"].shift(1)
    p["min_last3"] = p.groupby("player_id")["min"].transform(lambda x: x.shift(1).rolling(3, 1).mean())
    p["starter_s"] = _ewm(p["starter"].astype(float), grp, SHORT_HL)
    p["gp"] = p.groupby("player_id").cumcount()
    p["gp_season"] = p.groupby(["player_id", "season"]).cumcount()
    p["min_season"] = p.groupby(["player_id", "season"])["min"].transform(
        lambda x: x.shift(1).expanding().mean())
    p["usage"] = p["fga"] + 0.44 * p["fta"] + p["tov"]
    # minutes-weighted rates: ratio of EWMAs of counts and minutes
    m_s = _ewm(p["min"], grp, 10)
    m_l = _ewm(p["min"], grp, 40)
    for s in RATE_STATS + ["usage"]:
        p[f"{s}_r_s"] = _ewm(p[s], grp, 10) / m_s
        p[f"{s}_r_l"] = _ewm(p[s], grp, 40) / m_l
    p["pm_r_l"] = _ewm(p["plus_minus"], grp, 40) / m_l
    # shooting luck: recent vs long-run accuracy (the model learns how much hot/cold streaks regress)
    p["fg3_pct_s"] = _ewm(p["fg3m"], grp, 8) / _ewm(p["fg3a"], grp, 8)
    p["fg3_pct_l"] = (_ewm(p["fg3m"], grp, 80) * 20 + 0.36 * 2) / (_ewm(p["fg3a"], grp, 80) * 20 + 2)
    tsa = p["fga"] + 0.44 * p["fta"]
    p["ts_s"] = _ewm(p["pts"], grp, 8) / (2 * _ewm(tsa, grp, 8))
    p["ts_l"] = _ewm(p["pts"], grp, 80) / (2 * _ewm(tsa, grp, 80))
    p["fg3_luck"] = p["fg3_pct_s"] - p["fg3_pct_l"]
    p["ts_luck"] = p["ts_s"] - p["ts_l"]
    # composite per-minute value (game-score like) used for availability-weighted team strength
    p["gmsc"] = (p["pts"] + 0.4 * p["fgm"] - 0.7 * p["fga"] - 0.4 * (p["fta"] - p["ftm"]) +
                 0.7 * p["oreb"] + 0.3 * p["dreb"] + p["stl"] + 0.7 * p["ast"] + 0.7 * p["blk"] -
                 0.4 * p["pf"] - p["tov"])
    p["value_r"] = _ewm(p["gmsc"], grp, 30) / _ewm(p["min"], grp, 30) + 0.05 * p["pm_r_l"].fillna(0)
    # schedule & injury-return signals
    p = add_schedule_features(p, "player_id")
    return p


def roster_absences(pg: pd.DataFrame, pf: pd.DataFrame, tg: pd.DataFrame, lookback: int = 10) -> pd.DataFrame:
    """For each team-game: which recent rotation players did not play, and what they leave behind.

    'Rostered' = played for the team in any of its previous `lookback` games and has not since
    appeared for another team. Absent = rostered but not in this game's box. Their pre-game
    projections (minutes/usage/value EWMAs) are summed as vacated resources.
    """
    played = pg[pg["min"] > 0][["game_id", "team", "player_id"]]
    feats = pf.set_index(["game_id", "player_id"])
    last_state = pf.sort_values(["game_date", "game_id"]).groupby("player_id")
    tg = tg.sort_values(["game_date", "game_id"])
    in_game = played.groupby(["game_id", "team"])["player_id"].apply(set).to_dict()
    # latest pre-game snapshot of every player at each point in time: use their last played row
    snap_cols = ["min_s", "min_l", "usage_r_s", "value_r", "pts_r_s", "ast_r_s", "reb_r_s", "starter_s"]
    pf_sorted = pf.sort_values(["game_date", "game_id"])
    # post-game snapshot = pre-game features of the *next* appearance are unknown, so carry the
    # player's own last pre-game features forward but updated with that game's minutes
    snap = pf_sorted[["player_id", "team", "game_date", "game_id", "min"] + snap_cols].copy()
    for c in ("min_s", "min_l"):  # fold in the last game's minutes
        hl = SHORT_HL if c == "min_s" else LONG_HL
        a = 1 - 0.5 ** (1 / hl)
        snap[c] = np.where(snap[c].isna(), snap["min"], (1 - a) * snap[c] + a * snap["min"])
    rows = []
    team_hist: dict[str, list] = {}
    player_last_team: dict[int, str] = {}
    player_snap: dict[int, dict] = {}
    snap_by_game = {k: v for k, v in snap.groupby("game_id")}
    for gid, gdate, team in tg[["game_id", "game_date", "team"]].itertuples(index=False):
        hist = team_hist.get(team, [])[-lookback:]
        roster = set().union(*hist) if hist else set()
        roster = {p for p in roster if player_last_team.get(p) == team}
        here = in_game.get((gid, team), set())
        absent = roster - here
        vac = {"vac_min": 0.0, "vac_usage": 0.0, "vac_value": 0.0, "vac_pts": 0.0, "vac_ast": 0.0,
               "vac_reb": 0.0, "vac_starters": 0.0, "n_absent": len(absent), "n_star_absent": 0}
        for p in absent:
            s = player_snap.get(p)
            if not s:
                continue
            m = s["min_s"] if s["min_s"] == s["min_s"] else 0.0
            vac["vac_min"] += m
            vac["vac_usage"] += m * np.nan_to_num(s["usage_r_s"])
            vac["vac_value"] += m * np.nan_to_num(s["value_r"])
            vac["vac_pts"] += m * np.nan_to_num(s["pts_r_s"])
            vac["vac_ast"] += m * np.nan_to_num(s["ast_r_s"])
            vac["vac_reb"] += m * np.nan_to_num(s["reb_r_s"])
            vac["vac_starters"] += np.nan_to_num(s["starter_s"])
            vac["n_star_absent"] += int(m >= 28)
        avail_value = sum(np.nan_to_num(player_snap[p]["value_r"]) * np.nan_to_num(player_snap[p]["min_s"])
                          for p in here if p in player_snap)
        rows.append({"game_id": gid, "team": team, **vac, "avail_value": avail_value,
                     "roster_value": avail_value + vac["vac_value"]})
        team_hist.setdefault(team, []).append(here)
        # update snapshots after the game
        if gid in snap_by_game:
            sg = snap_by_game[gid]
            for r in sg[sg["team"] == team].itertuples(index=False):
                player_last_team[r.player_id] = team
                player_snap[r.player_id] = {c: getattr(r, c) for c in snap_cols}
    return pd.DataFrame(rows)


# ------------------------------------------------------------------ defense vs player type

ARCH_FEATS = ["reb_r_l", "oreb_r_l", "ast_r_l", "fg3a_r_l", "blk_r_l", "usage_r_l", "fta_r_l"]
ARCH_STATS = ["pts", "reb", "ast", "fg3m", "blk", "stl", "tov"]
N_ARCH = 6


def assign_archetypes(P: pd.DataFrame, model_path) -> np.ndarray:
    """Cluster players by what they do (rebounding, playmaking, 3pt volume, rim protection,
    usage, free throws) from their pre-game long-run per-minute rates. Listed positions are
    too coarse in the modern league. The fitted clusterer is saved so live runs match training."""
    import pickle
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    X = P[ARCH_FEATS].astype(float)
    ok = X.notna().all(axis=1) & (P["gp"] >= 10)
    if model_path.exists():
        sc, km = pickle.loads(model_path.read_bytes())
    else:
        sc = StandardScaler().fit(X[ok])
        km = KMeans(N_ARCH, n_init=10, random_state=0).fit(sc.transform(X[ok].sample(min(ok.sum(), 150000),
                                                                                      random_state=0)))
        model_path.parent.mkdir(parents=True, exist_ok=True)
        model_path.write_bytes(pickle.dumps((sc, km)))
    arch = np.full(len(P), -1)
    arch[ok.values] = km.predict(sc.transform(X[ok]))
    return arch


def archetype_defense(P: pd.DataFrame, hl: float = 12, group: str = "arch",
                      prefix: str = "opp_arch_") -> pd.DataFrame:
    """For each (game, defending team, player group): pre-game EWMA of how much that defence
    lets players of that group exceed their own normal per-minute production (1.0 = neutral).
    group="arch" -> player types; group="pos" -> listed position (defense vs position)."""
    d = P[["game_id", "game_date", "opp", group, "min", "is_target"] +
          ARCH_STATS + [f"{s}_r_l" for s in ARCH_STATS]].rename(columns={group: "arch"}).copy()
    d = d[d["arch"].notna() & (d["arch"].astype(str) != "-1")]
    played = (~d["is_target"]) & (d["min"] > 0)
    rows = []
    for s in ARCH_STATS:
        d[f"exp_{s}"] = d[f"{s}_r_l"] * d["min"]
    agg = d[played].groupby(["game_id", "opp", "arch"], as_index=False)[
        ARCH_STATS + [f"exp_{s}" for s in ARCH_STATS]].sum()
    keys = d[["game_id", "game_date", "opp", "arch"]].drop_duplicates(["game_id", "opp", "arch"])
    agg = keys.merge(agg, on=["game_id", "opp", "arch"], how="left").sort_values(["game_date", "game_id"])
    out = agg[["game_id", "opp", "arch"]].copy()
    grp = [agg["opp"], agg["arch"]]
    for s in ARCH_STATS:
        num = agg[s].groupby(grp).transform(lambda x: x.shift(1).ewm(halflife=hl, ignore_na=True).mean())
        den = agg[f"exp_{s}"].groupby(grp).transform(lambda x: x.shift(1).ewm(halflife=hl, ignore_na=True).mean())
        prior = {"pts": 20, "reb": 8, "ast": 5, "fg3m": 3, "blk": 1.5, "stl": 1.5, "tov": 3}[s]
        out[f"{prefix}{s}"] = (num + prior) / (den + prior)  # shrink toward neutral
    return out.rename(columns={"arch": group})


def dvp_table(P: pd.DataFrame, asof) -> pd.DataFrame:
    """Defense vs position as of a date: each team's latest factor per position and stat, with
    league rank (1 = allows the most relative to what those players normally produce)."""
    d = P[(P["game_date"] <= pd.Timestamp(asof)) & P["pos"].notna()]
    d = d.sort_values(["game_date", "game_id"]).drop_duplicates(["opp", "pos"], keep="last")
    rows = []
    for (team, pos), r in d.set_index(["opp", "pos"]).iterrows():
        for s in ARCH_STATS:
            rows.append({"team": team, "pos": pos, "stat": s, "factor": r[f"opp_pos_{s}"]})
    t = pd.DataFrame(rows).dropna()
    t["rank"] = t.groupby(["pos", "stat"])["factor"].rank(ascending=False, method="min").astype(int)
    t["vs_avg_pct"] = (100 * (t["factor"] - 1)).round(1)
    return t.sort_values(["pos", "stat", "rank"])
