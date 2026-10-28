"""Game-context factors: travel/altitude, schedule load, rotation depth, rest habits,
standings/motivation, referee crews. All computed strictly from information before tip-off."""
from __future__ import annotations

import numpy as np
import pandas as pd

# arena latitude, longitude, UTC offset (standard time), altitude in metres
ARENAS = {
    "ATL": (33.757, -84.396, -5, 320), "BOS": (42.366, -71.062, -5, 5), "BKN": (40.683, -73.976, -5, 10),
    "CHA": (35.225, -80.839, -5, 230), "CHI": (41.881, -87.674, -6, 180), "CLE": (41.496, -81.688, -5, 200),
    "DAL": (32.790, -96.810, -6, 130), "DEN": (39.749, -105.008, -7, 1609), "DET": (42.341, -83.055, -5, 190),
    "GSW": (37.768, -122.388, -8, 5), "HOU": (29.751, -95.362, -6, 15), "IND": (39.764, -86.155, -5, 220),
    "LAC": (33.945, -118.341, -8, 30), "LAL": (34.043, -118.267, -8, 80), "MEM": (35.138, -90.051, -6, 80),
    "MIA": (25.781, -80.188, -5, 2), "MIL": (43.045, -87.917, -6, 190), "MIN": (44.979, -93.276, -6, 260),
    "NOP": (29.949, -90.082, -6, 2), "NYK": (40.751, -73.993, -5, 10), "OKC": (35.463, -97.515, -6, 370),
    "ORL": (28.539, -81.384, -5, 30), "PHI": (39.901, -75.172, -5, 5), "PHX": (33.446, -112.071, -7, 340),
    "POR": (45.532, -122.667, -8, 15), "SAC": (38.580, -121.500, -8, 10), "SAS": (29.427, -98.438, -6, 200),
    "TOR": (43.643, -79.379, -5, 80), "UTA": (40.768, -111.901, -7, 1288), "WAS": (38.898, -77.021, -5, 10),
}
EAST = {"ATL", "BOS", "BKN", "CHA", "CHI", "CLE", "DET", "IND", "MIA", "MIL", "NYK", "ORL", "PHI", "TOR", "WAS"}


def _haversine(a, b):
    la1, lo1, la2, lo2 = map(np.radians, (a[:, 0], a[:, 1], b[:, 0], b[:, 1]))
    h = np.sin((la2 - la1) / 2) ** 2 + np.cos(la1) * np.cos(la2) * np.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * np.arcsin(np.sqrt(h))


def add_travel(tf: pd.DataFrame) -> pd.DataFrame:
    """Distance flown since last game, time-zone shift, altitude, road-trip length."""
    tf = tf.sort_values(["game_date", "game_id"]).copy()
    venue = np.where(tf["is_home"] == 1, tf["team"], tf["opp"])
    tf["venue"] = venue
    prev = tf.groupby("team")["venue"].shift(1).fillna(tf["team"])
    cur_xy = np.array([ARENAS.get(v, (np.nan,) * 4)[:2] for v in tf["venue"]], dtype=float)
    prev_xy = np.array([ARENAS.get(v, (np.nan,) * 4)[:2] for v in prev], dtype=float)
    tf["travel_km"] = _haversine(prev_xy, cur_xy)
    tz = lambda s: np.array([ARENAS.get(v, (0, 0, np.nan, 0))[2] for v in s], dtype=float)  # noqa: E731
    tf["tz_shift"] = tz(tf["venue"]) - tz(prev)   # + = travelled east
    tf["travel_per_rest"] = tf["travel_km"] / tf["rest_days"].clip(lower=1)
    home_tz = tz(tf["team"])
    tf["tz_from_home"] = tz(tf["venue"]) - home_tz
    tf["altitude_m"] = np.array([ARENAS.get(v, (0, 0, 0, 0))[3] for v in tf["venue"]], dtype=float) * (
        tf["is_home"] == 0)
    away = (tf["is_home"] == 0).astype(int)
    streak = (away != away.groupby(tf["team"]).shift(1)).astype(int).groupby(tf["team"]).cumsum()
    tf["road_trip_game"] = np.where(away == 1, tf.groupby([tf["team"], streak]).cumcount() + 1, 0)
    tf["km_last7d"] = _rolling_sum_days(tf, "travel_km", 7)
    return tf


def _rolling_sum_days(tf: pd.DataFrame, col: str, days: int) -> np.ndarray:
    out = pd.Series(0.0, index=tf.index)
    for _, g in tf.groupby("team"):
        s = g.set_index("game_date")[col].rolling(f"{days}D").sum()
        out.loc[g.index] = s.values
    return out.values


def add_depth(tf: pd.DataFrame, pg: pd.DataFrame) -> pd.DataFrame:
    """Coach's rotation habits: how many players get real minutes, and how concentrated the
    minutes are among the top 8. EWMA over previous games (adapts after a coaching change)."""
    p = pg[pg["min"] > 0]
    g = p.groupby(["game_id", "team"])["min"]
    d = pd.DataFrame({"n_rot": g.apply(lambda m: (m >= 10).sum()),
                      "top8_share": g.apply(lambda m: m.nlargest(8).sum() / max(m.sum(), 1))}).reset_index()
    tf = tf.merge(d, on=["game_id", "team"], how="left").sort_values(["game_date", "game_id"])
    for c in ("n_rot", "top8_share"):
        tf[f"{c}_l"] = tf.groupby("team")[c].transform(lambda x: x.shift(1).ewm(halflife=10, ignore_na=True).mean())
    return tf.drop(columns=["n_rot", "top8_share"])


def add_rest_habits(tf: pd.DataFrame) -> pd.DataFrame:
    """How often a team sits its high-minute players on the 2nd night of back-to-backs, over and
    above its normal injury absences. Expanding history per team (coach-agnostic)."""
    tf = tf.sort_values(["game_date", "game_id"]).copy()
    star_out = (tf["n_star_absent"] > 0).astype(float)
    b2b = tf["b2b"] == 1
    grp = tf["team"]
    rate_b2b = star_out.where(b2b).groupby(grp).transform(lambda x: x.shift(1).expanding().mean())
    rate_other = star_out.where(~b2b).groupby(grp).transform(lambda x: x.shift(1).expanding().mean())
    rate_b2b = rate_b2b.groupby(grp).ffill()
    rate_other = rate_other.groupby(grp).ffill()
    tf["b2b_rest_rate"] = (rate_b2b - rate_other).clip(-0.2, 0.6)
    tf["b2b_rest_risk"] = tf["b2b_rest_rate"] * tf["b2b"]
    return tf


def add_standings(tf: pd.DataFrame) -> pd.DataFrame:
    """Pre-game record, conference rank, games behind 6th (top-6 seed) and 10th (play-in),
    games left, and whether the team is effectively eliminated / locked (motivation proxies)."""
    tf = tf.sort_values(["game_date", "game_id"]).copy()
    reg = tf["playoff"] == 0
    win = (tf["pts"] > tf["opp_pts"]).astype(float).where(tf["pts"].notna())
    key = [tf["team"], tf["season"]]
    tf["w_pre"] = win.where(reg, 0).groupby(key).transform(lambda x: x.shift(1).fillna(0).cumsum())
    tf["gp_pre"] = reg.astype(int).groupby(key).transform(lambda x: x.shift(1).fillna(0).cumsum())
    tf["win_pct_pre"] = (tf["w_pre"] + 2) / (tf["gp_pre"] + 4)
    tf["games_left"] = (82 - tf["gp_pre"]).clip(lower=0)
    tf["conf"] = np.where(tf["team"].isin(EAST), "E", "W")
    # conference table as of each date: latest record of every team before that date
    out = []
    for (season, conf), g in tf.groupby(["season", "conf"]):
        dates = np.sort(g["game_date"].unique())
        last = g.sort_values("game_date")
        for dt in dates:
            snap = last[last["game_date"] < dt].drop_duplicates("team", keep="last")
            rec = snap.set_index("team")
            w = (rec["w_pre"] + (rec["pts"] > rec["opp_pts"])).astype(float)
            n = rec["gp_pre"] + 1
            wl = pd.DataFrame({"w": w, "l": n - w})
            today = g[g["game_date"] == dt]
            for r in today.itertuples():
                if r.team in wl.index:
                    tbl = wl
                else:
                    tbl = pd.concat([wl, pd.DataFrame({"w": [0.0], "l": [0.0]}, index=[r.team])])
                tbl = tbl.assign(pct=(tbl["w"] + 1) / (tbl["w"] + tbl["l"] + 2)).sort_values("pct", ascending=False)
                me = tbl.loc[r.team]
                rank = int((tbl["pct"] > me["pct"]).sum()) + 1
                gb = lambda k: (((tbl.iloc[min(k, len(tbl)) - 1]["w"] - me["w"]) +  # noqa: E731
                                 (me["l"] - tbl.iloc[min(k, len(tbl)) - 1]["l"])) / 2) if len(tbl) >= k else 0.0
                out.append((r.Index, rank, gb(6), gb(10)))
    s = pd.DataFrame(out, columns=["idx", "conf_rank", "gb_6", "gb_10"]).set_index("idx")
    tf = tf.join(s)
    tf["eliminated"] = ((tf["gb_10"] > tf["games_left"]) & (tf["gp_pre"] > 40)).astype(int)
    tf["tank_zone"] = ((tf["conf_rank"] >= 12) & (tf["gp_pre"] >= 55)).astype(int)
    tf["seed_locked"] = ((tf["games_left"] <= 3) & (tf["conf_rank"] <= 2)).astype(int)
    return tf.drop(columns=["conf"])


def referee_factors(games: pd.DataFrame, tg: pd.DataFrame, officials: pd.DataFrame | None) -> pd.DataFrame:
    """Crew tendencies: each official's EWMA of total fouls, free throws and points in games
    they worked (relative to league average that season), averaged over the crew."""
    if officials is None or officials.empty:
        return pd.DataFrame({"game_id": games["game_id"].astype(int), "crew_fouls": np.nan, "crew_fta": np.nan,
                             "crew_pts": np.nan})
    tot = tg.groupby("game_id").agg(fouls=("pf", "sum"), fta=("fta", "sum"), pts=("pts", "sum"),
                                     game_date=("game_date", "first"), season=("season", "first"))
    for c in ("fouls", "fta", "pts"):
        tot[c] = tot[c] / tot.groupby("season")[c].transform("mean")
    o = officials.merge(tot.reset_index(), on="game_id", how="left")
    # include upcoming games (no totals yet) so they receive the officials' pre-game values
    o["game_date"] = o["game_date"].fillna(o["game_id"].map(games.set_index("game_id")["game_date"]))
    o = o.sort_values(["game_date", "game_id"])
    for c in ("fouls", "fta", "pts"):
        o[f"r_{c}"] = o.groupby("official")[c].transform(lambda x: x.shift(1).ewm(halflife=40, ignore_na=True).mean())
        o[f"n_{c}"] = o.groupby("official")[c].transform(lambda x: x.shift(1).notna().cumsum())
        # shrink thin histories toward 1.0
        o[f"r_{c}"] = (o[f"r_{c}"].fillna(1) * o[f"n_{c}"] + 30) / (o[f"n_{c}"] + 30)
    crew = o.groupby("game_id")[["r_fouls", "r_fta", "r_pts"]].mean()
    return crew.rename(columns={"r_fouls": "crew_fouls", "r_fta": "crew_fta", "r_pts": "crew_pts"}).reset_index()


def award_games_pressure(P: pd.DataFrame) -> pd.Series:
    """65-game rule (since 2023-24): players need 65 games of 20+ minutes for MVP/All-NBA etc.
    Positive = games still needed relative to games left (pressure to play through minor issues).
    Only meaningful for high-minute players; shown as a note, used as a feature if it helps."""
    q = (P["min"].fillna(0) >= 20).astype(int)
    done = q.groupby([P["player_id"], P["season"]]).transform(lambda x: x.shift(1).fillna(0).cumsum())
    left = (82 - P.groupby(["player_id", "season"]).cumcount()).clip(lower=1)
    need = (65 - done).clip(lower=0)
    pressure = np.where((P["min_l"] >= 30) & (P["season"] >= "2023-24"), need / left, 0.0)
    return pd.Series(np.clip(pressure, 0, 2), index=P.index)
