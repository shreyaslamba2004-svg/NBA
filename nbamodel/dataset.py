"""Assemble model-ready player and game frames from history (+ optional upcoming slate)."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .context import (add_depth, add_rest_habits, add_standings, add_travel, award_games_pressure,
                      referee_factors)
from .features import (ARCH_STATS, LONG_HL, PROP_STATS, RATE_STATS, SHORT_HL, _ewm, archetype_defense,
                       assign_archetypes, player_features, roster_absences, team_features, team_game_table)

DATA = Path(__file__).resolve().parents[1] / "data" / "processed"
MODELS = Path(__file__).resolve().parents[1] / "models"
# which opponent-vs-player-group features the rate models use: "arch", "pos" or "both"
DEFENSE_GROUPS = "both"

BASE_TEAM_FEATS = ["ortg_s", "ortg_l", "drtg_s", "drtg_l", "pace_s", "pace_l", "net_s", "net_l",
                   "three_rate_l", "three_rate_allowed_l", "season_gp", "rest_days", "b2b", "g_last4d", "g_last7d"]
# optional context factor groups (each can be switched off for ablation tests)
CONTEXT_GROUPS = {
    "travel": ["travel_km", "tz_shift", "tz_from_home", "altitude_m", "road_trip_game", "km_last7d",
               "travel_per_rest"],
    "schedule_load": ["g_last6d"],
    "rotation_depth": ["n_rot_l", "top8_share_l"],
    "rest_habits": ["b2b_rest_rate", "b2b_rest_risk"],
    "motivation": ["win_pct_pre", "games_left", "conf_rank", "gb_6", "gb_10", "eliminated", "tank_zone",
                   "seed_locked"],
}
GAME_CONTEXT = {"referees": ["crew_fouls", "crew_fta", "crew_pts"]}
REP_MIN = ["min_s_rep", "min_l_rep", "min_season_s", "min_stint_s", "min_stint"]
REP_RATE_STATS = ["pts", "reb", "ast", "fg3m", "stl", "blk", "tov", "fga", "fta", "fg3a", "usage"]
PLAYER_CONTEXT = {"shooting_luck": ["fg3_pct_s", "fg3_pct_l", "ts_s", "ts_l", "fg3_luck", "ts_luck"],
                  "award_pressure": ["award_pressure"],
                  # minutes left by absent teammates who play the same position
                  "pos_absence": ["vac_min_same_pos"],
                  "mates_scoring": ["mates_pts", "mates_fg3m"],
                  "ot_adjust": ["min_s_reg", "min_l_reg"],
                  "vs_opponent": ["vs_opp_min"] + [f"vs_opp_{s}" for s in ("pts", "reb", "ast", "fg3m")],
                  # representative history: form that skips comeback/blowout games and restarts by season/team
                  "rep_history": REP_MIN + [f"{s}_r_{k}" for s in REP_RATE_STATS for k in ("stint", "season")]}
DISABLED: set[str] = set()  # names of groups to leave out of the models


def _ctx_feats(groups: dict) -> list[str]:
    return [f for k, v in groups.items() if k not in DISABLED for f in v]


TEAM_FEATS = BASE_TEAM_FEATS + [f for v in CONTEXT_GROUPS.values() for f in v]
ABS_FEATS = ["vac_min", "vac_usage", "vac_value", "vac_pts", "vac_ast", "vac_reb", "vac_starters",
             "n_absent", "avail_value", "roster_value"]


def load_history() -> tuple[pd.DataFrame, pd.DataFrame]:
    pg = pd.read_parquet(DATA / "player_games.parquet")
    g = pd.read_parquet(DATA / "games.parquet")
    dnp = DATA / "dnp_cd_pbp_seasons.parquet"  # dressed-but-unused players for pbp-derived seasons
    if dnp.exists():
        d = pd.read_parquet(dnp).merge(g[["game_id", "game_date", "season", "playoff"]], on="game_id")
        d = d.merge(pg.drop_duplicates(["game_id", "team"])[["game_id", "team", "home"]], on=["game_id", "team"])
        d["min"], d["starter"] = 0.0, 0
        d = d[~d.set_index(["game_id", "player_id"]).index.isin(pg.set_index(["game_id", "player_id"]).index)]
        pg = pd.concat([pg, d], ignore_index=True)
    extra = DATA / "current_season_player_games.parquet"  # appended by the live updater
    if extra.exists():
        pg = pd.concat([pg, pd.read_parquet(extra)], ignore_index=True).drop_duplicates(
            ["game_id", "player_id"], keep="last")
        g = pd.concat([g, pd.read_parquet(DATA / "current_season_games.parquet")],
                      ignore_index=True).drop_duplicates("game_id", keep="last")
    return pg, g


REP_RETURN_GAMES = 5   # first games back from a long absence (often on a minutes limit)
REP_BLOWOUT = 25       # final margin at/above which starters sit and benches play


def add_rep_history(pf: pd.DataFrame, games: pd.DataFrame) -> None:
    """Representative-history features (in place).

    Minutes form that ignores the first games back from a long absence and blowouts; and minutes and
    per-minute rates that restart each season and with each new team, so a traded player or a changed
    role shows up after a few games instead of being averaged with the old one.
    """
    pid = pf["player_id"]
    stint = (pf["team"] != pf.groupby("player_id")["team"].shift(1)).groupby(pid).cumsum()
    g = games.set_index("game_id")
    margin = (g["home_pts"] - g["away_pts"]).abs().reindex(pf["game_id"]).values
    # a comeback is a long absence within a season, or a full season+ away (not just the off-season)
    days_out = (pf["game_date"] - pf.groupby("player_id")["game_date"].shift(1)).dt.days
    same_season = pf["season"] == pf.groupby("player_id")["season"].shift(1)
    opened = pf["season"].map(games.groupby("season")["game_date"].min())
    late_start = ~same_season & ((pf["game_date"] - opened).dt.days >= 21)  # missed the start of a season
    back = (((pf["games_missed"] >= 10) | (days_out >= 30)) & same_season) | late_start | (days_out >= 400)
    since = pf.groupby([pid, back.astype(int).groupby(pid).cumsum()]).cumcount()
    rep = ~(back.groupby(pid).cumsum().gt(0) & (since < REP_RETURN_GAMES)) & ~(margin >= REP_BLOWOUT)
    m_rep = pf["min"].where(rep)
    pf["min_s_rep"] = _ewm(m_rep, pid, SHORT_HL)
    pf["min_l_rep"] = _ewm(m_rep, pid, LONG_HL)
    pf["min_season_s"] = _ewm(m_rep, [pid, pf["season"]], 4)
    # overtime: minutes rescaled to a 48-minute game (the simulation adds overtime itself)
    periods = g["periods"].reindex(pf["game_id"]).fillna(4).clip(lower=4).values
    m_reg = pf["min"] * 48 / (48 + 5 * (periods - 4))
    pf["min_s_reg"] = _ewm(m_reg, pid, SHORT_HL)
    pf["min_l_reg"] = _ewm(m_reg, pid, LONG_HL)
    pf["min_stint_s"] = _ewm(m_rep, [pid, stint], 4)
    pf["min_stint"] = pf.groupby([pid, stint])["min"].transform(lambda x: x.shift(1).expanding().mean())
    pf["usage"] = pf["fga"] + 0.44 * pf["fta"] + pf["tov"]
    for name, keys in (("stint", [pid, stint]), ("season", [pid, pf["season"]])):
        cm = pf.groupby(keys)["min"].shift(1).groupby(keys).cumsum()
        for s in REP_RATE_STATS:
            cs = pf.groupby(keys)[s].shift(1).groupby(keys).cumsum()
            pf[f"{s}_r_{name}"] = (cs / cm).where(cm >= 30)


VS_OPP_STATS = ["pts", "reb", "ast", "fg3m"]
VS_OPP_PRIOR_MIN = 72  # shrinkage: his history vs this team counts as much as ~2 games at his usual rate


def add_vs_opponent(P: pd.DataFrame) -> None:
    """Player vs this specific opponent (in place): his past production against them relative to his
    usual rate, shrunk hard toward 1 because he only meets each team a few times a year."""
    keys = [P["player_id"], P["opp"]]
    mins = P.groupby(keys)["min"].shift(1).groupby(keys).cumsum().fillna(0)
    P["vs_opp_min"] = mins
    for s in VS_OPP_STATS:
        r = P[f"{s}_r_l"].clip(lower=0.005)
        got = P.groupby(keys)[s].shift(1).groupby(keys).cumsum().fillna(0)
        exp = P.groupby(keys)["min"].shift(1).mul(r).groupby(keys).cumsum().fillna(0)
        prior = VS_OPP_PRIOR_MIN * r
        P[f"vs_opp_{s}"] = (got + prior) / (exp + prior)


def build(pg: pd.DataFrame, games: pd.DataFrame, slate: pd.DataFrame | None = None,
          slate_players: pd.DataFrame | None = None, pit_out: dict | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (player_frame, game_frame).

    slate: upcoming games (game_id, game_date, season, home, away)
    slate_players: expected participants (game_id, team, player_id, player_name, play_prob,
                   starter [optional, NaN if unknown])
    """
    pg = pg.copy()
    pg["is_target"] = False
    games = games.copy()
    if slate is not None and len(slate):
        sp = slate_players.copy()
        sp = sp.merge(slate[["game_id", "game_date", "season", "home", "away"]], on="game_id")
        sp["home"] = (sp["team"] == sp["home"]).astype(int)
        sp = sp.drop(columns=["away"])
        sp["is_target"] = True
        sp["playoff"] = 0
        sp["comment"] = ""
        for c in ["min", "pts", "fgm", "fga", "fg3m", "fg3a", "ftm", "fta", "oreb", "dreb", "reb",
                  "ast", "stl", "blk", "tov", "pf", "plus_minus"]:
            sp[c] = np.nan
        if "starter" not in sp:
            sp["starter"] = np.nan
        pg = pd.concat([pg, sp], ignore_index=True)
        sg = slate.copy()
        for c in ("home_pts", "away_pts"):
            sg[c] = np.nan
        sg["periods"] = 4
        sg["playoff"] = 0
        games = pd.concat([games, sg], ignore_index=True)

    pf = player_features(pg)
    hist_pg = pg[~pg["is_target"]]
    tg = team_game_table(hist_pg, games)
    if slate is not None and len(slate):
        rows = []
        for r in slate.itertuples(index=False):
            for team, opp, ih in ((r.home, r.away, 1), (r.away, r.home, 0)):
                rows.append({"game_id": r.game_id, "team": team, "opp": opp, "is_home": ih,
                             "game_date": r.game_date, "season": r.season, "playoff": 0, "periods": 4})
        tg = pd.concat([tg, pd.DataFrame(rows)], ignore_index=True)
    tf = team_features(tg)

    # absences: for target games "who plays" = expected participants with play_prob >= .5
    # available = played, or dressed but unused (coach's decision). Counting coach's-decision
    # DNPs as absences would leak game script: deep benches only get minutes in blowouts.
    pg_for_abs = pg.copy()
    cd = pg_for_abs["comment"].fillna("").str.contains("coach", case=False) & (pg_for_abs["min"].fillna(0) == 0)
    pg_for_abs.loc[cd, "min"] = 0.01
    if slate is not None and len(slate):
        tmask = pg_for_abs["is_target"]
        pg_for_abs.loc[tmask, "min"] = np.where(pg_for_abs.loc[tmask, "play_prob"] >= 0.5, 1.0, 0.0)
    posf = DATA / "positions.parquet"
    pos_map = pd.read_parquet(posf).set_index("player_id")["pos"].to_dict() if posf.exists() else {}
    ab = roster_absences(pg_for_abs, pf, tf, pit_out=pit_out, pos=pos_map)
    tf = tf.merge(ab[["game_id", "team", "n_star_absent"]], on=["game_id", "team"], how="left")
    tf = add_standings(add_rest_habits(add_depth(add_travel(tf), hist_pg)))

    # sequence numbers -> team games missed since a player's last appearance
    tf = tf.sort_values(["game_date", "game_id"])
    tf["team_seq"] = tf.groupby("team").cumcount()
    seq = tf.set_index(["game_id", "team"])["team_seq"]
    pf["team_seq"] = seq.reindex(pd.MultiIndex.from_frame(pf[["game_id", "team"]])).values
    prev_seq = pf.groupby("player_id")["team_seq"].shift(1)
    prev_team = pf.groupby("player_id")["team"].shift(1)
    pf["games_missed"] = np.where(prev_team == pf["team"], pf["team_seq"] - prev_seq - 1, 0)
    pf["games_missed"] = pf["games_missed"].clip(0, 82).fillna(0)
    pf["new_team"] = ((prev_team != pf["team"]) & prev_team.notna()).astype(int)
    # --- role on a new team: games with current team, and how much of the team's minutes and
    # shots the other available players already claim (low = room for a bigger role)
    stint = (pf["team"] != prev_team).groupby(pf["player_id"]).cumsum()
    pf["gp_team"] = pf.groupby([pf["player_id"], stint]).cumcount()
    present = pf[(pf["min"].fillna(0) > 0) | (pf["is_target"] & (pf.get("play_prob", 1) >= 0.5))]
    ms = present["min_s"].fillna(0)
    tot = present.assign(mu=ms, uu=ms * present["usage_r_s"].fillna(0), pp=ms * present["pts_r_s"].fillna(0),
                         p3=ms * present["fg3m_r_s"].fillna(0)
                         ).groupby(["game_id", "team"])[["mu", "uu", "pp", "p3"]].sum()
    key = pd.MultiIndex.from_frame(pf[["game_id", "team"]])
    own_m = pf["min_s"].fillna(0)
    pf["mates_min"] = tot["mu"].reindex(key).values - own_m.values
    pf["mates_usage"] = tot["uu"].reindex(key).values - (own_m * pf["usage_r_s"].fillna(0)).values
    # how well the available teammates score (an assist needs a teammate to make the shot)
    pf["mates_pts"] = tot["pp"].reindex(key).values - (own_m * pf["pts_r_s"].fillna(0)).values
    pf["mates_fg3m"] = tot["p3"].reindex(key).values - (own_m * pf["fg3m_r_s"].fillna(0)).values
    # --- comeback from long absences: days since last game (uncapped) and games since return
    pf["days_out"] = (pf["game_date"] - pf.groupby("player_id")["game_date"].shift(1)).dt.days.fillna(0)
    same_season = pf["season"] == pf.groupby("player_id")["season"].shift(1)
    # long absence: 10+ team games missed, a month out mid-season, or a whole season+ away
    long_abs = (pf["games_missed"] >= 10) | ((pf["days_out"] >= 30) & same_season) | (pf["days_out"] >= 250)
    ret_id = long_abs.astype(int).groupby(pf["player_id"]).cumsum()
    pf["games_since_return"] = np.where(ret_id > 0, pf.groupby([pf["player_id"], ret_id]).cumcount(), 99)
    pf["games_since_return"] = pf["games_since_return"].clip(upper=99)
    pf["last_absence_len"] = pf["games_missed"].where(long_abs).groupby(pf["player_id"]).ffill().fillna(0)
    add_rep_history(pf, games)

    own = tf[["game_id", "team", "opp", "is_home"] + TEAM_FEATS +
             [c for c in tf.columns if c.startswith("allow_") and c.endswith("_l")]]
    own = own.merge(ab, on=["game_id", "team"], how="left")
    opp = own.drop(columns=["opp", "is_home"]).rename(
        columns=lambda c: c if c == "game_id" else f"opp_{c}").rename(columns={"opp_team": "opp"})
    ctx = own.merge(opp, on=["game_id", "opp"], how="left")

    keep = [c for c in ctx.columns if not (c.startswith("allow_") or c.startswith("opp_allow_"))
            or c.startswith("opp_allow_")]
    sched = ["rest_days", "b2b", "g_last4d", "g_last6d", "g_last7d"]  # player's own versions take precedence
    P = pf.merge(ctx[[c for c in keep if c not in sched]], on=["game_id", "team"], how="inner")
    P["net_diff"] = P["net_l"] - P["opp_net_l"]
    add_vs_opponent(P)
    P["arch"] = assign_archetypes(P, MODELS / "archetypes.pkl")
    P = P.merge(archetype_defense(P), on=["game_id", "opp", "arch"], how="left")
    # listed position (G/F/C); players never listed get their player type's most common position
    pos = DATA / "positions.parquet"
    P["pos"] = P["player_id"].map(pd.read_parquet(pos).set_index("player_id")["pos"]) if pos.exists() else np.nan
    arch_pos = P.dropna(subset=["pos"]).groupby("arch")["pos"].agg(lambda x: x.mode().iloc[0])
    P["pos"] = P["pos"].fillna(P["arch"].map(arch_pos))
    P = P.merge(archetype_defense(P, group="pos", prefix="opp_pos_"), on=["game_id", "opp", "pos"], how="left")
    P["pos_code"] = P["pos"].map({"G": 0, "F": 1, "C": 2})
    P["vac_min_same_pos"] = 0.0
    for k in ("G", "F", "C"):
        P.loc[P["pos"] == k, "vac_min_same_pos"] = P.loc[P["pos"] == k, f"vac_min_{k}"]
    P["exp_pace"] = (P["pace_l"] + P["opp_pace_l"]) / 2
    P["vac_min_share"] = P["vac_min"] / 240
    P["award_pressure"] = award_games_pressure(P)
    off = DATA / "officials.parquet"
    officials = pd.read_parquet(off) if off.exists() else None
    if officials is not None and "officials" in (slate.columns if slate is not None else []):
        officials = pd.concat([officials, slate[["game_id", "officials"]].explode("officials").rename(
            columns={"officials": "official"}).dropna()], ignore_index=True)
    crew = referee_factors(games, tg, officials)
    P = P.merge(crew, on="game_id", how="left")

    # game frame (home perspective)
    h = ctx[ctx["is_home"] == 1].drop(columns=["is_home"])
    G = h.rename(columns={c: f"h_{c}" for c in h.columns if c not in ("game_id",)})
    G = G.rename(columns={"h_opp": "away", "h_team": "home"})
    G = G.rename(columns=lambda c: c.replace("h_opp_", "a_") if c.startswith("h_opp_") else c)
    G = G.merge(games[["game_id", "game_date", "season", "playoff", "home_pts", "away_pts", "periods"]],
                on="game_id")
    G["margin"] = G["home_pts"] - G["away_pts"]
    G["total"] = G["home_pts"] + G["away_pts"]
    for f in ("net_s", "net_l", "ortg_l", "drtg_l", "pace_l", "rest_days", "avail_value", "vac_value",
              "roster_value"):
        G[f"d_{f}"] = G[f"h_{f}"] - G[f"a_{f}"]
    G["exp_pace"] = (G["h_pace_l"] + G["a_pace_l"]) / 2
    G["exp_eff"] = (G["h_ortg_l"] + G["a_drtg_l"] + G["a_ortg_l"] + G["h_drtg_l"]) / 4
    G = G.merge(crew, on="game_id", how="left")
    return P, G


PLAYER_MIN_FEATS = ["min_s", "min_l", "min_last", "min_last3", "starter_s", "gp", "gp_season",
                    "min_season", "rest_days", "b2b", "g_last4d", "g_last7d", "games_missed", "new_team",
                    "gp_team", "mates_min", "mates_usage", "days_out", "games_since_return", "last_absence_len",
                    "vac_min", "vac_starters", "vac_usage", "n_absent", "net_diff", "is_home", "playoff",
                    "usage_r_s", "value_r", "avail_value", "roster_value"]


def min_feats() -> list[str]:
    ctx = _ctx_feats({k: v for k, v in CONTEXT_GROUPS.items() if k in ("travel", "schedule_load",
                                                                       "rotation_depth", "rest_habits",
                                                                       "motivation")})
    rep = (REP_MIN + ["usage_r_stint", "usage_r_season"]) if "rep_history" not in DISABLED else []
    rep += _ctx_feats({"pos_absence": PLAYER_CONTEXT["pos_absence"], "ot_adjust": PLAYER_CONTEXT["ot_adjust"]})
    return (PLAYER_MIN_FEATS + ctx + _ctx_feats({"award_pressure": PLAYER_CONTEXT["award_pressure"]}) + rep +
            (["starter_today"] if "late_news" not in DISABLED else []))


def rate_feats(stat: str) -> list[str]:
    f = [f"{stat}_r_s", f"{stat}_r_l", "usage_r_s", "usage_r_l", "min_s", "starter_s", "gp",
         "vac_usage", "vac_pts", "vac_ast", "vac_reb", "vac_min", "pace_l", "opp_pace_l", "exp_pace",
         "opp_drtg_l", "ortg_l", "opp_three_rate_allowed_l", "three_rate_l", "is_home", "b2b", "rest_days", "net_diff",
         "fga_r_s", "fg3a_r_s", "fta_r_s", "gp_team", "new_team", "mates_usage", "mates_min",
         "games_since_return", "last_absence_len", "days_out"]
    if stat in ("reb", "ast", "fg3m", "stl", "blk", "tov", "pts"):
        f.append(f"opp_allow_{stat}_pp_l")
    f += _ctx_feats({k: v for k, v in CONTEXT_GROUPS.items() if k in ("travel", "schedule_load", "motivation")})
    f += _ctx_feats({"pos_absence": PLAYER_CONTEXT["pos_absence"]})
    if stat in ("pts", "reb", "ast", "fg3m") and "vs_opponent" not in DISABLED:
        f += ["vs_opp_min", f"vs_opp_{stat}"]
    if stat in ("ast", "pts", "fg3m", "fga", "fg3a", "tov"):
        f += _ctx_feats({"mates_scoring": PLAYER_CONTEXT["mates_scoring"]})
    if "rep_history" not in DISABLED:
        f += ["min_s_rep", "min_season_s", "min_stint_s", "usage_r_stint", "usage_r_season"]
        f += [f"{stat}_r_stint", f"{stat}_r_season"] if stat in REP_RATE_STATS else []
    if stat in ("pts", "fg3m", "fga", "fta"):
        f += _ctx_feats({"shooting_luck": PLAYER_CONTEXT["shooting_luck"]})
    if stat in ("pts", "fta", "pf"):
        f += _ctx_feats(GAME_CONTEXT)
    if stat in ARCH_STATS:
        f += [f"opp_arch_{stat}", "arch"] if DEFENSE_GROUPS in ("arch", "both") else []
        f += [f"opp_pos_{stat}", "pos_code"] if DEFENSE_GROUPS in ("pos", "both") else []
    return list(dict.fromkeys(f))


def game_feats() -> list[str]:
    team = BASE_TEAM_FEATS + _ctx_feats(CONTEXT_GROUPS)
    return ([f"h_{c}" for c in team + ABS_FEATS] + [f"a_{c}" for c in team + ABS_FEATS] +
            ["d_net_s", "d_net_l", "d_ortg_l", "d_drtg_l", "d_pace_l", "d_rest_days", "d_avail_value",
             "d_vac_value", "d_roster_value", "exp_pace", "exp_eff", "playoff"] + _ctx_feats(GAME_CONTEXT))


GAME_FEATS = game_feats()
