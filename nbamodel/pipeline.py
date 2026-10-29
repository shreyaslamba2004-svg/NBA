"""Daily projection run: refresh data -> availability -> features -> models -> simulation -> edges."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from .dataset import DATA, build, load_history, mates_basis, read_store, write_store
from .models import SIM_STATS, predict_team, Bundle, predict_minutes, predict_rates
from . import rotation, edges as E
from . import bookie, scenarios as SC, sgm
from .simulate import expected_minutes, simulate_game, summarize_game, summarize_players
from .sources import espn, live
from .sources.live import SourceUnavailable, norm_name

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
# probability a player suits up, by report status (league-wide historical rates, rounded)
PLAY_PROB = {"out": 0.0, "doubtful": 0.2, "questionable": 0.55, "day-to-day": 0.7, "game time decision": 0.55,
             "probable": 0.93, "available": 1.0, "active": 1.0, "suspension": 0.0}


def season_label(d: date) -> str:
    y = d.year if d.month >= 8 else d.year - 1
    return f"{y}-{str(y + 1)[2:]}"


# ------------------------------------------------------------------ data refresh

def refresh_current_season(day: date) -> None:
    """Pull every completed game since the end of stored history from ESPN."""
    pg, g = load_history()
    cw = espn.Crosswalk(pg, DATA / "espn_crosswalk.json")
    start = (g["game_date"].max() + pd.Timedelta(days=1)).date()
    if start >= day:
        return
    known = set(g["game_id"].astype(int))
    seasons = {}
    d = start
    while d < day:  # chunk by season label
        seasons.setdefault(season_label(d), []).append(d)
        d += timedelta(days=1)
    B, Gm, L = [], [], []
    for s, days in seasons.items():
        print(f"backfilling {s}: {days[0]} .. {days[-1]}")
        b, gm, ln = espn.backfill(days[0], days[-1] + timedelta(days=1), cw, s, known)
        B.append(b), Gm.append(gm), L.append(ln)
    b = pd.concat([x for x in B if len(x)], ignore_index=True) if any(len(x) for x in B) else pd.DataFrame()
    if b.empty:
        return
    gm = pd.concat(Gm, ignore_index=True)
    ln = pd.concat([x for x in L if len(x)], ignore_index=True) if any(len(x) for x in L) else pd.DataFrame()
    b["team_id"] = None
    for f, new in (("current_season_player_games", b), ("current_season_games", gm),
                   ("current_season_lines", ln)):
        old = read_store(f)
        if old is not None and len(new):
            new = pd.concat([old, new], ignore_index=True)
        if len(new):
            key = ["game_id", "player_id"] if "player_id" in new else ["game_id"]
            write_store(f, new.drop_duplicates(key, keep="last"))


# ------------------------------------------------------------------ availability

def availability(slate: pd.DataFrame, day: date, pg: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Expected participants per team with play probabilities, from rosters + injury reports."""
    cw = espn.Crosswalk(pg, DATA / "espn_crosswalk.json")
    inj_frames = []
    try:
        inj_frames.append(live.injuries_official(day).assign(priority=0))
    except (SourceUnavailable, Exception) as e:  # PDF layout changes shouldn't stop a run
        print("official injury report unavailable:", e)
    notes = {}
    try:
        ei = live.injuries_espn()
        inj_frames.append(ei.assign(priority=1))
        notes = dict(zip(ei["key"], ei["reason"]))  # beat-writer blurbs: restrictions, starts
    except SourceUnavailable as e:
        print("ESPN injuries unavailable:", e)
    inj = pd.concat(inj_frames, ignore_index=True) if inj_frames else pd.DataFrame(
        columns=["team", "player", "status", "reason", "key", "priority"])
    inj = inj.sort_values("priority").drop_duplicates("key")
    rows = []
    for r in slate.itertuples(index=False):
        for team in (r.home, r.away):
            roster = espn.team_roster(team)
            for a in roster.itertuples(index=False):
                pid = cw.lookup(a.espn_id, a.player_name, team)
                st = inj[inj["key"] == norm_name(a.player_name)]
                status = st["status"].iloc[0] if len(st) else (a.injury_status or "")
                prob = PLAY_PROB.get(str(status).lower(), 1.0) if status else 1.0
                note = notes.get(norm_name(a.player_name), "")
                rows.append({"game_id": r.game_id, "team": team, "player_id": pid,
                             "player_name": a.player_name, "status": status or "Active",
                             "reason": st["reason"].iloc[0] if len(st) else "", "play_prob": prob,
                             "note": note, "min_cap": minutes_cap(note),
                             "starting": starting_flag(note)})
    sp = pd.DataFrame(rows).drop_duplicates(["game_id", "player_id"])
    sp = _apply_lineups(sp, slate, cw)
    cw.save()
    return sp, inj


LINEUP_WINDOW_MIN = 75  # ESPN posts starters / inactives roughly 30 minutes before tip


def _lineup(r, nba_ids: dict, cw) -> tuple[pd.DataFrame, str]:
    """Posted starters / ruled-out players for one game: the NBA's own pre-game box first (lists
    ACTIVE / INACTIVE and starters before tip), ESPN's box as the fallback. Empty if neither has it."""
    gid = nba_ids.get((r.home, r.away))
    if gid is not None:
        b = live.pregame_actives(gid)
        if b is not None and len(b) and b["starter"].sum() >= 10:
            return pd.DataFrame({"player_id": b["player_id"], "team": b["team"], "starter": b["starter"] == 1,
                                 "out": b["status"].astype(str).str.upper() == "INACTIVE"}), "nba"
    lu = espn.pregame_lineup(r.game_id)
    if lu.empty or lu["team"].nunique() != 2 or not (lu.groupby("team")["starter"].sum() == 5).all():
        return pd.DataFrame(), ""
    lu["player_id"] = [cw.lookup(e, n, t) for e, n, t in zip(lu["espn_id"], lu["player_name"], lu["team"])]
    return lu, "espn"


def _apply_lineups(sp: pd.DataFrame, slate: pd.DataFrame, cw) -> pd.DataFrame:
    """Once a game's starting lineups are posted: starters are certain to play (and start), and
    players ruled out are out. Coach's decisions aren't known before tip, so the rest keep their
    chance-to-play estimates. Each attempt is logged to output/lineups_log.csv."""
    if "tip_utc" not in slate:
        return sp
    now = pd.Timestamp.now(tz="UTC")
    near = [r for r in slate.itertuples(index=False)
            if -5 <= (pd.Timestamp(r.tip_utc) - now).total_seconds() / 60 <= LINEUP_WINDOW_MIN]
    if not near:
        return sp
    try:
        sch = live.schedule(pd.Timestamp(near[0].game_date).date())
        nba_ids = {(h, a): int(g) for g, h, a in zip(sch["game_id"], sch["home"], sch["away"]) if int(g) < 10**8}
    except Exception as e:  # NBA site unreachable: ESPN only
        print("NBA schedule unavailable:", e)
        nba_ids = {}
    sp, log = sp.copy(), []
    for r in near:
        lu, src = _lineup(r, nba_ids, cw)
        mins = (pd.Timestamp(r.tip_utc) - now).total_seconds() / 60
        log.append({"checked_utc": now.strftime("%Y-%m-%dT%H:%MZ"), "game": f"{r.away}@{r.home}",
                    "mins_to_tip": round(mins), "nba_id_found": (r.home, r.away) in nba_ids, "source": src or "none"})
        if lu.empty:
            continue
        g = sp["game_id"] == r.game_id
        start = g & sp["player_id"].isin(lu.loc[lu["starter"], "player_id"])
        sp.loc[start, ["starting", "play_prob"]] = [1, 1.0]
        sp.loc[start, "status"] = "Starting"
        out = g & sp["player_id"].isin(lu.loc[lu["out"], "player_id"])
        sp.loc[out, ["play_prob", "starting"]] = [0.0, 0]
        sp.loc[out, "status"] = "Out"
        print(f"lineups posted for {r.away}@{r.home} ({src}): {int(start.sum())} starters, {int(out.sum())} out")
    f = OUT / "lineups_log.csv"
    pd.DataFrame(log).to_csv(f, mode="a", header=not f.exists(), index=False)
    return sp


RESTRICT = re.compile(r"minutes? (restriction|limit|cap)|limited minutes|on a (strict )?minutes|limited to|"
                      r"pitch count|ease (him|back)|managed workload", re.I)


def minutes_cap(note: str) -> float:
    """Minutes cap from news text: an explicit number ('limited to around 20 minutes') if given,
    else 22 for an unspecified restriction. NaN = no restriction mentioned."""
    if not note or not RESTRICT.search(note):
        return np.nan
    m = re.search(r"(\d{1,2})\s*(?:-|to)?\s*(?:\d{1,2})?\s*minutes", note)
    return float(m.group(1)) if m and 8 <= int(m.group(1)) <= 36 else 22.0


def starting_flag(note: str) -> float:
    if not note:
        return np.nan
    if re.search(r"(will|is expected to|set to|slated to) (start|be in the starting lineup)|will draw the start", note, re.I):
        return 1.0
    if re.search(r"(come|coming) off the bench|bench role|move to the bench", note, re.I):
        return 0.0
    return np.nan


def availability_hash(sp: pd.DataFrame) -> str:
    key = sp.sort_values(["team", "player_id"])[["team", "player_id", "status", "min_cap", "starting"]].to_csv(
        index=False)
    return hashlib.sha1(key.encode()).hexdigest()


# ------------------------------------------------------------------ projection

def _expected_mates(tP: pd.DataFrame) -> pd.DataFrame:
    """Teammates' claim on minutes and shots, counting each teammate by his chance to play.

    In training these count the players who got on court. Live, build() counted every healthy
    roster player, deep bench included, so rotations looked crowded and every projection sagged
    (live-like backtest, 2025-26: minutes bias -0.96 and MAE 4.63 that way; weighting by chance to
    play: bias +0.24, MAE 4.51)."""
    tP = tP.copy()
    here = (tP["avail_prob"] >= 0.5) & ~tP["maybe"]
    w = np.where(here, tP["rotation_prob"].fillna(0), 0.0)
    ms, us = mates_basis(tP).values, tP["usage_r_s"].fillna(0).values
    key = [tP["game_id"], tP["team"]]
    mu = pd.Series(w * ms, index=tP.index).groupby(key).transform("sum")
    uu = pd.Series(w * ms * us, index=tP.index).groupby(key).transform("sum")
    tP["mates_min"] = mu - w * ms
    tP["mates_usage"] = uu - w * ms * us
    return tP


def rookie_prior(pick: int | None) -> tuple[float, float]:
    """(minutes if he plays, chance the coach plays him) for a player with no NBA games.
    Hand-set from typical early-career usage by draft slot; replaced by his own numbers after
    a few games."""
    if pick is None:
        return 8.0, 0.35
    for top, mins, rot in ((3, 30.0, 0.97), (10, 24.0, 0.9), (20, 16.0, 0.75), (30, 12.0, 0.6)):
        if pick <= top:
            return mins, rot
    return 8.0, 0.4


def project(day: date, slate: pd.DataFrame, sp: pd.DataFrame, b: Bundle,
            history_from: str | None = None, market: pd.DataFrame | None = None,
            props: pd.DataFrame | None = None, book_lines: pd.DataFrame | None = None) -> dict:
    """Project every game under who-plays scenarios (see scenarios.py).

    base      every maybe player OUT: what the sheet shows for confirmed players
    if X      maybe player X IN (others out): his projection, and for impactful players the
              whole game re-projected
    expected  all in/out combinations blended by probability: used to price bets
    """
    pg, g = load_history()
    history_from = history_from or season_label(day.replace(year=day.year - 3))  # last 3 seasons + this one
    pg, g = pg[pg["season"] >= history_from], g[g["season"] >= history_from]
    slate = slate.assign(season=season_label(day))
    sp = sp.copy()
    # a maybe stops being a maybe once he's confirmed: ruled out (play_prob 0), cleared, or
    # reported as starting -> the game collapses to one projection on the next run
    sp["maybe"] = sp["status"].map(SC.is_maybe) & (sp["play_prob"] > 0) & (sp["starting"] != 1)
    P, G = build(pg, g, slate, sp.assign(play_prob=np.where(sp["maybe"], 0.0, sp["play_prob"])))
    tP = P[P["is_target"] & P["game_id"].isin(slate["game_id"])].copy()
    tG = G[G["game_id"].isin(slate["game_id"])].copy()
    late = ["status", "reason", "note", "min_cap", "starting", "maybe"]
    tP = tP.drop(columns=[c for c in late + ["play_prob"] if c in tP.columns]).merge(
        sp[["game_id", "player_id", "play_prob"] + late], on=["game_id", "player_id"], how="left")
    tP["maybe"] = tP["maybe"].fillna(False).astype(bool)
    tP["avail_prob"] = tP["play_prob"].fillna(0.0)
    tP["starter_today"] = tP["starting"]  # confirmed starters from late news, when known
    # healthy isn't the same as playing: the chance the coach uses him (see rotation.py)
    # not on a single box score this season (not even a coach's-decision DNP) and not on the injury
    # report: a two-way or end-of-bench player who hasn't dressed. Those team games count as games he
    # didn't play (28 Oct: 9 such players at ~60% to play, none played; the two who did were on the
    # injury report, i.e. returning from injury, and are left alone)
    season = season_label(day)
    cur = pg[pg["season"] == season]
    team_games = cur.groupby("team")["game_id"].nunique()
    seen = set(cur["player_id"])
    off_report = tP["status"].isna() | (tP["status"].astype(str) == "Active")
    unseen = {int(r.player_id): int(team_games.get(r.team, 0)) for r in tP[off_report].itertuples()
              if r.player_id not in seen and team_games.get(r.team, 0) >= 2}
    tP["rotation_prob"] = rotation.prob(rotation.current_signal(pg, tP["player_id"].tolist(), season,
                                                                unseen).values)
    # no NBA games yet (rookies, injured before debut): prior from draft slot
    tP["rookie_min"] = np.nan
    seen_any = set(pg["player_id"])
    for i in tP.index[tP["gp"].fillna(0) == 0]:
        pid = int(tP.at[i, "player_id"])
        pick = espn.draft_pick(pid - espn.SYNTH) if pid >= espn.SYNTH else None
        mins, rot = rookie_prior(pick)
        if pid in seen_any or pid in unseen:  # coach's-decision DNPs or undressed games count too
            rot = min(rot, tP.at[i, "rotation_prob"])
        tP.at[i, "rookie_min"], tP.at[i, "rotation_prob"] = mins, rot
    tP.loc[tP["starting"] == 1, "rotation_prob"] = 1.0
    tP = _expected_mates(tP)

    games_out, players_out, edges, sgms, sim_inputs = [], [], [], [], []
    for gr in tG.itertuples(index=False):
        Pg0, Gg0 = tP[tP["game_id"] == gr.game_id], tG[tG["game_id"] == gr.game_id]
        matchup = f"{gr.away} @ {gr.home}"
        mk = None
        if market is not None and len(market):
            m = market[market["game_id"] == gr.game_id]
            if len(m):
                mk = m.iloc[0]
        maybes = Pg0[Pg0["maybe"] & (Pg0["avail_prob"] > 0)]
        cmb = SC.combos(maybes) if len(maybes) else [(frozenset(), 1.0)]
        exact = set().union(*[c for c, _ in cmb])
        seed = int(gr.game_id) % 2**31  # same random numbers in every scenario: differences are real
        sims = {}
        for S, _ in cmb:
            Pg, Gg = Pg0, Gg0
            for pid in S:
                Pg, Gg = SC.switch_in(Pg, Gg, Pg0[Pg0["player_id"] == pid].iloc[0].to_dict())
            Pg = Pg.copy()
            Pg["play_prob"] = Pg["avail_prob"] * Pg["rotation_prob"]
            ex = Pg["player_id"].isin(exact)
            Pg.loc[ex, "play_prob"] = np.where(Pg.loc[ex, "player_id"].isin(S), 1.0, 0.0)  # scenario: he plays
            gp, mu_m, mu_t = _prepare(Pg, Gg, b)
            game = {"game_id": gr.game_id, "home": gr.home, "away": gr.away, "mu_margin": mu_m, "mu_total": mu_t}
            if mk is not None:
                game["market_spread_home"], game["market_total"] = mk.get("spread_home"), mk.get("total")
            sims[S] = (simulate_game(game, gp, b, seed=seed), gp, game)
        base_sim, base_gp, base_game = sims[frozenset()]
        exp_sim = SC.mixture([(sims[S][0], w) for S, w in cmb], len(base_sim["margin"])) if len(cmb) > 1 else base_sim
        names = dict(zip(Pg0["player_id"], Pg0["player_name"]))
        out_players = Pg0[Pg0["avail_prob"] == 0]
        out_txt = ", ".join(f"{r.player_name} ({r.team})" for r in out_players.itertuples()
                            if r.min_s == r.min_s and r.min_s > 8)

        def game_row(sim, game, scen, label):
            gs = summarize_game(sim, game)
            gs.update({"game_id": gr.game_id, "date": day.isoformat(), "out": out_txt,
                       "scenario": scen, "scenario_label": label})
            return gs

        def player_rows(sim, gp, scen, label, only=None):
            ps = summarize_players(sim)
            if only is not None:
                ps = ps[ps["player_id"].isin(only)]
            ps.insert(0, "game_id", gr.game_id)
            ps.insert(1, "matchup", matchup)
            ps["scenario"], ps["scenario_label"] = scen, label
            return ps.merge(gp[["player_id", "reason", "avail_prob", "rotation_prob"]], on="player_id", how="left")

        maybe_names = ", ".join(names[p] for p in exact)
        games_out.append(game_row(base_sim, base_game, "base", f"without {maybe_names}" if exact else "all confirmed"))
        players_out.append(player_rows(base_sim, base_gp, "base", "base"))
        if len(cmb) > 1:
            games_out.append(game_row(exp_sim, base_game, "expected", "blended by each maybe's chance to play"))
        for pid in exact:
            sim, gp, game = sims[frozenset([pid])]
            r = gp[gp["player_id"] == pid]
            impact = bool(len(r) and float(r["pmin"].iloc[0]) >= SC.IMPACT_MIN)
            scen, label = f"in:{pid}", f"if {names[pid]} plays"
            g_row = game_row(sim, game, scen, label)
            g_row["impact"] = impact
            games_out.append(g_row)
            players_out.append(player_rows(sim, gp, scen, label, None if impact else [pid]).assign(
                maybe_player=pid, impact=impact, maybe_avail=float(Pg0.loc[Pg0["player_id"] == pid, "avail_prob"].iloc[0])))

        offers = []
        if mk is not None:
            offers.append(E.offers_from_espn_lines(gr.game_id, gr.home, gr.away, mk.to_dict()))
        if book_lines is not None and len(book_lines):
            bl = book_lines[(book_lines["home"] == gr.home) & (book_lines["away"] == gr.away)]
            if len(bl):
                offers.append(E.offers_from_odds_api(gr.game_id, bl))
        if props is not None and len(props):
            pp = props[props["game_id"] == gr.game_id]
            if len(pp):
                offers.append(E.offers_from_props(pp))
        if offers:
            allo = pd.concat(offers, ignore_index=True)
            for c in ("player_id", "line"):  # book feeds disagree on dtypes (None vs NaN ids)
                allo[c] = pd.to_numeric(allo[c], errors="coerce")
            allo["offered"] = bookie.offered(allo, base_gp).values
            ev = E.evaluate(exp_sim, gr.home, allo, labels=names)
            key = ["market", "selection", "line", "player_id"]
            ok = allo.groupby(key, dropna=False)[["offered", "paired"]].max().reset_index()
            ok = ok.rename(columns={"paired": "main_line"})  # a book prices both sides: not an alt line
            for d in (ev, ok):
                d["player_id"] = pd.to_numeric(d["player_id"], errors="coerce")
                d["line"] = pd.to_numeric(d["line"], errors="coerce")
            ev = ev.merge(ok, on=key, how="left")
            ev["offered"] = ev["offered"].fillna(True).astype(bool)
            ev.insert(1, "matchup", matchup)
            ev = _depends_on(ev, sims, exact, names, gr.home)
            edges.append(ev)
            # same-game multis only from players certain to play (questionable legs could void)
            certain_ids = base_gp.loc[(base_gp["avail_prob"] >= 0.99) & (base_gp["rotation_prob"] >= 0.95), "player_id"]
            certain = allo[(allo["player_id"].isna() | allo["player_id"].isin(certain_ids)) & allo["offered"]]
            mk_p = ev[["market", "selection", "line", "player_id", "market_novig_prob"]].drop_duplicates(
                ["market", "selection", "line", "player_id"])
            certain = certain.merge(mk_p, on=["market", "selection", "line", "player_id"], how="left")
            sg = sgm.suggest(exp_sim, gr.home, gr.away, certain, names)
            if len(sg):
                sg.insert(0, "matchup", matchup)
                sgms.append(sg)
        sim_inputs.append(base_gp.assign(game_mu_margin=base_game["mu_margin"], game_mu_total=base_game["mu_total"],
                                         game_home=gr.home, game_away=gr.away))
    games_df = pd.DataFrame(games_out)
    players_df = pd.concat(players_out, ignore_index=True) if players_out else pd.DataFrame()
    edges_df = pd.concat(edges, ignore_index=True) if edges else pd.DataFrame()
    if len(edges_df):
        edges_df = edges_df.sort_values("ev_blend", ascending=False)
    keep = ["game_id", "team", "player_id", "player_name", "play_prob", "pmin", "game_mu_margin",
            "game_mu_total", "game_home", "game_away"] + [f"rate_{s}" for s in SIM_STATS]
    return {"games": games_df, "players": players_df, "edges": edges_df,
            "sgm": pd.concat(sgms, ignore_index=True) if sgms else pd.DataFrame(),
            "sim_inputs": pd.concat(sim_inputs, ignore_index=True)[keep] if sim_inputs else pd.DataFrame()}


RECONCILE = 0.5  # live-like backtest, points MAE: full 4.470, half 4.447, none 4.454
RATE_PRIOR = {"pts": .42, "reb": .18, "ast": .09, "fg3m": .04, "stl": .03, "blk": .02, "tov": .05,
              "fga": .36, "fta": .10}


def _prepare(Pg: pd.DataFrame, Gg: pd.DataFrame, b: Bundle) -> tuple[pd.DataFrame, float, float]:
    """Minutes, per-minute rates and team score for one game's scenario."""
    Pg = Pg.copy()
    has = Pg["gp"].fillna(0) > 0
    Pg["pmin_raw"] = np.where(has, predict_minutes(b, Pg), Pg["rookie_min"])
    rates = predict_rates(b, Pg)
    for s in SIM_STATS:
        Pg[f"rate_{s}"] = np.where(has, rates[s], RATE_PRIOR[s])
    mu_m, mu_t = predict_team(b, Gg)
    mu_m, mu_t = float(np.asarray(mu_m)[0]), float(np.asarray(mu_t)[0])
    Pg["pmin"] = 0.0
    for _, idx in Pg.groupby("team").groups.items():
        Pg.loc[idx, "pmin"] = expected_minutes(Pg.loc[idx], b)
    gp = Pg[Pg["play_prob"] > 0].copy()
    home = Gg["home"].iloc[0]
    for team in gp["team"].unique():
        mu = (mu_t + mu_m) / 2 if team == home else (mu_t - mu_m) / 2
        t = gp["team"] == team
        bu = (gp.loc[t, "rate_pts"] * gp.loc[t, "pmin"] * gp.loc[t, "play_prob"]).sum()
        if bu > 0:  # reconcile player points with the team model, half way: the player side
            f = (mu / bu) ** RECONCILE  # is already near the team total, a full pull overcorrects
            gp.loc[t, "rate_pts"] *= f
            gp.loc[t, "rate_fga"] *= f ** 0.5
    return gp, mu_m, mu_t


def _depends_on(ev: pd.DataFrame, sims: dict, exact: set, names: dict, home: str) -> pd.DataFrame:
    """For each offer: the maybe player whose status moves its probability most, both ways."""
    ev = ev.copy()
    ev["depends_on"], ev["p_if_out"], ev["p_if_in"] = "", np.nan, np.nan
    if not exact or ev.empty:
        return ev
    base = sims[frozenset()][0]
    rows = list(ev.itertuples(index=False))
    p_out = np.array([E._model_prob(base, home, r.market, r.selection, r.line, r.player_id) for r in rows], float)
    best_gap = np.zeros(len(rows))
    for pid in exact:
        sim = sims[frozenset([pid])][0]
        p_in = np.array([E._model_prob(sim, home, r.market, r.selection, r.line, r.player_id) for r in rows], float)
        own = ev["player_id"].values == pid
        gap = np.where(own, 1.0, np.abs(np.nan_to_num(p_in) - np.nan_to_num(p_out)))
        upd = gap > np.maximum(best_gap, 0.04)
        ev.loc[upd, "depends_on"] = names[pid]
        ev.loc[upd, "p_if_out"] = np.where(own[upd], 0.0, p_out[upd])
        ev.loc[upd, "p_if_in"] = p_in[upd]
        best_gap = np.where(upd, gap, best_gap)
    for c in ("p_if_out", "p_if_in"):
        ev[c] = ev[c].round(4)
    return ev


def market_lines(slate: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for gid in slate["game_id"]:
        try:
            js = espn.summary(gid)
            ln = espn.lines_from_summary(js)
            if ln:
                rows.append({"game_id": gid, **ln})
        except SourceUnavailable:
            pass
    return pd.DataFrame(rows)


def props_market(slate: pd.DataFrame, pg: pd.DataFrame | None = None,
                 use_odds_api: bool = True) -> pd.DataFrame | None:
    """Player props from every configured source, merged into one schema:
    source, book, game_id, player_id, stat, market, side, line, price.

    - DraftKings via ESPN (free, full menu, open + current)
    - The Odds API, books in ODDS_REGIONS (e.g. "au"), if ODDS_API_KEY is set
    To add a provider, append a frame with the same columns; prop_edges takes the best
    price per (player, stat, line, side) across all of them.
    """
    if pg is None:
        pg, _ = load_history()
    cw = espn.Crosswalk(pg, DATA / "espn_crosswalk.json")
    frames = []
    for r in slate.itertuples(index=False):
        try:
            p = espn.props(r.game_id)
        except SourceUnavailable as e:
            print("ESPN props unavailable for", r.game_id, e)
            continue
        if len(p):
            names = _espn_names(cw, p["espn_id"])  # rosters usually seeded the crosswalk already
            p["player_id"] = [cw.lookup(a, names.get(int(a), str(a))) for a in p["espn_id"]]
            frames.append(p.assign(source="espn"))
    if use_odds_api and live_key_available():
        try:
            ev = live.odds_events()
            for e in ev.drop_duplicates("event_id").itertuples():  # costs credits: one call per game
                m = slate[(slate["home"] == e.home) & (slate["away"] == e.away)]
                if m.empty:
                    continue
                pr = live.odds_props(e.event_id)
                if len(pr):
                    pr["game_id"] = int(m["game_id"].iloc[0])
                    pr["player_id"] = pr["player"].map(lambda n: cw.lookup(f"name:{n}", n, None))
                    pr["side"] = pr["side"].str.lower()
                    pr["market"] = "ou"
                    frames.append(pr.assign(source="the_odds_api"))
        except SourceUnavailable as e:
            print("Odds API props skipped:", e)
    cw.save()
    return pd.concat(frames, ignore_index=True) if frames else None


def props_hash(props: pd.DataFrame | None) -> str:
    """Fingerprint of a prop menu's lines and prices (detects when DraftKings moves anything)."""
    if props is None or props.empty:
        return ""
    cols = [c for c in ("game_id", "player_id", "stat", "market", "side", "line", "price") if c in props]
    rows = props[cols].astype(str).agg("|".join, axis=1).sort_values()
    return hashlib.sha1("\n".join(rows).encode()).hexdigest()


def live_key_available() -> bool:
    import os
    return bool(os.environ.get("ODDS_API_KEY"))


_NAME_CACHE: dict[int, str] = {}


def _espn_names(cw, ids) -> dict:
    """ESPN athlete id -> display name (cached), needed only for players new to the crosswalk."""
    for a in set(int(x) for x in ids):
        if str(a) in cw.map or a in _NAME_CACHE:
            continue
        try:
            _NAME_CACHE[a] = live._get(f"{espn.CORE}/athletes/{a}")["displayName"]
        except (SourceUnavailable, KeyError):
            _NAME_CACHE[a] = str(a)
    return _NAME_CACHE


def latest_book_lines(slate: pd.DataFrame) -> pd.DataFrame | None:
    """Most recent logged Odds API game lines for today's matchups (AU books by default)."""
    p = ROOT / "logs" / "market" / "book_lines.csv"
    if not p.exists():
        return None
    d = pd.read_csv(p)
    d = d.merge(slate[["home", "away"]], on=["home", "away"])
    if d.empty:
        return None
    d = d[pd.to_datetime(d["commence"], utc=True) > pd.Timestamp.now(tz="UTC") - pd.Timedelta(hours=12)]
    return d[d["snapshot_utc"] == d["snapshot_utc"].max()] if len(d) else None


def write_outputs(day: date, res: dict, tag: str = "") -> Path:
    d = OUT / day.isoformat()
    d.mkdir(parents=True, exist_ok=True)
    for k, v in res.items():
        if k == "edges" and "ev_blend" in v:  # the sheet only lists value; the full menu is in logs/
            v = v[v["ev_blend"] > 0]
        v.to_csv(d / f"{k}{tag}.csv", index=False)
    return d


def latest_props(slate: pd.DataFrame) -> pd.DataFrame | None:
    """Most recent logged props per game and source (free ESPN DraftKings + any AU books bought)."""
    p = ROOT / "logs" / "market" / "props.csv"
    if not p.exists():
        return None
    d = pd.read_csv(p)
    d = d[d["game_id"].isin(slate["game_id"])]
    if d.empty:
        return None
    last = d.groupby(["game_id", "source"])["snapshot_utc"].transform("max")
    return d[d["snapshot_utc"] == last].reset_index(drop=True)


def finish(day: date, res: dict, sp: pd.DataFrame, slate: pd.DataFrame) -> Path:
    """Write the CSVs, run state and the readable sheet (TODAY.md)."""
    tips = slate.set_index("game_id")["tip_utc"]
    if len(res["games"]) and "tip_sydney" not in res["games"]:
        res["games"].insert(2, "tip_sydney", res["games"]["game_id"].map(
            lambda g: pd.Timestamp(tips[g]).tz_convert("Australia/Sydney").strftime("%a %d %b %H:%M")))
    res["availability"] = sp
    try:  # automatic checks on every run; flags go to TODAY.md and HEALTH.md
        from . import sanity
        res["sanity"] = sanity.check(res, load_history()[0])
    except Exception as e:  # a check must never stop the sheet
        print("sanity checks failed:", e)
    path = write_outputs(day, res)
    (path / "state.json").write_text(json.dumps({"availability_hash": availability_hash(sp),
                                                 "generated": pd.Timestamp.now(tz="UTC").isoformat()}))
    from .dashboard import build as build_page
    build_page(day)
    print("wrote", path)
    return path


def run(day: date, refresh: bool = True, with_props: bool = True, props: pd.DataFrame | None = None) -> dict:
    """Project the slate. Props: pass already-fetched ones, or with_props fetches every source."""
    if refresh:
        refresh_current_season(day)
    b = Bundle.load()
    slate = espn.scoreboard(day)
    slate = slate[slate["status"] == "STATUS_SCHEDULED"][["game_id", "game_date", "home", "away", "tip_utc"]]
    if slate.empty:
        print("no upcoming games on", day)
        return {}
    pg, _ = load_history()
    sp, _ = availability(slate, day, pg)
    market = market_lines(slate)
    if props is None and with_props:
        props = props_market(slate, pg)
    res = project(day, slate.drop(columns=["tip_utc"]), sp, b, market=market, props=props,
                  book_lines=latest_book_lines(slate))
    finish(day, res, sp, slate)
    return res
