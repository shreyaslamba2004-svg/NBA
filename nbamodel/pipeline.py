"""Daily projection run: refresh data -> availability -> features -> models -> simulation -> edges."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from .dataset import DATA, build, load_history
from .models import SIM_STATS, predict_team, Bundle, predict_minutes, predict_rates
from . import rotation, edges as E
from . import sgm
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
    for f, new in (("current_season_player_games.parquet", b), ("current_season_games.parquet", gm),
                   ("current_season_lines.parquet", ln)):
        p = DATA / f
        if p.exists() and len(new):
            new = pd.concat([pd.read_parquet(p), new], ignore_index=True)
        if len(new):
            key = ["game_id", "player_id"] if "player_id" in new else ["game_id"]
            new.drop_duplicates(key, keep="last").to_parquet(p, index=False)


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
    cw.save()
    sp = pd.DataFrame(rows).drop_duplicates(["game_id", "player_id"])
    return sp, inj


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

def project(day: date, slate: pd.DataFrame, sp: pd.DataFrame, b: Bundle,
            history_from: str = "2023-24", market: pd.DataFrame | None = None,
            props: pd.DataFrame | None = None, book_lines: pd.DataFrame | None = None) -> dict:
    pg, g = load_history()
    pg, g = pg[pg["season"] >= history_from], g[g["season"] >= history_from]
    slate = slate.assign(season=season_label(day))
    P, G = build(pg, g, slate, sp)
    tP = P[P["is_target"] & P["game_id"].isin(slate["game_id"])].copy()
    tG = G[G["game_id"].isin(slate["game_id"])].copy()
    late = ["status", "reason", "note", "min_cap", "starting"]
    tP = tP.drop(columns=[c for c in late if c in tP.columns]).merge(sp[["game_id", "player_id"] + late],
                  on=["game_id", "player_id"], how="left")
    tP["starter_today"] = tP["starting"]  # confirmed starters from late news, when known
    # no history at all (rookie / two-way): conservative prior so they don't vanish
    tP["pmin_raw"] = np.where(tP["gp"] > 0, predict_minutes(b, tP), 6.0)
    rates = predict_rates(b, tP)
    for s in SIM_STATS:
        prior = {"pts": .42, "reb": .18, "ast": .09, "fg3m": .04, "stl": .03, "blk": .02, "tov": .05,
                 "fga": .36, "fta": .10}[s]
        tP[f"rate_{s}"] = np.where(tP["gp"] > 0, rates[s], prior)
    # healthy isn't the same as playing: scale by the chance the coach uses him (see rotation.py)
    tP["avail_prob"] = tP["play_prob"]
    tP["rotation_prob"] = rotation.prob(rotation.current_signal(pg, tP["player_id"].tolist()).values)
    tP.loc[tP["starting"] == 1, "rotation_prob"] = 1.0
    tP["play_prob"] = tP["avail_prob"] * tP["rotation_prob"]
    tP["pmin"] = 0.0
    for (gid, team), idx in tP.groupby(["game_id", "team"]).groups.items():
        tP.loc[idx, "pmin"] = expected_minutes(tP.loc[idx], b)
    tG["mu_margin"], tG["mu_total"] = predict_team(b, tG)

    games_out, players_out, edges, sgms, sim_inputs = [], [], [], [], []
    for gr in tG.itertuples(index=False):
        game = {"game_id": gr.game_id, "home": gr.home, "away": gr.away,
                "mu_margin": gr.mu_margin, "mu_total": gr.mu_total}
        mk = None
        if market is not None and len(market):
            m = market[market["game_id"] == gr.game_id]
            if len(m):
                mk = m.iloc[0]
                game["market_spread_home"] = mk.get("spread_home")
                game["market_total"] = mk.get("total")
        gp = tP[(tP["game_id"] == gr.game_id) & (tP["play_prob"] > 0)].copy()
        # reconcile player points with the team model
        mu_h, mu_a = (gr.mu_total + gr.mu_margin) / 2, (gr.mu_total - gr.mu_margin) / 2
        for team, mu in ((gr.home, mu_h), (gr.away, mu_a)):
            t = gp["team"] == team
            bu = (gp.loc[t, "rate_pts"] * gp.loc[t, "pmin"] * gp.loc[t, "play_prob"]).sum()
            if bu > 0:
                f = mu / bu
                gp.loc[t, "rate_pts"] *= f
                gp.loc[t, "rate_fga"] *= f ** 0.5
        sim = simulate_game(game, gp, b, seed=int(gr.game_id) % 2**31)
        gs = summarize_game(sim, game)
        gs.update({"game_id": gr.game_id, "date": day.isoformat()})
        ps = summarize_players(sim)
        ps.insert(0, "game_id", gr.game_id)
        ps.insert(1, "matchup", f"{gr.away} @ {gr.home}")
        ps = ps.merge(gp[["player_id", "reason"]], on="player_id", how="left")
        out_players = tP[(tP["game_id"] == gr.game_id) & (tP["avail_prob"] == 0)]
        gs["out"] = ", ".join(f"{r.player_name} ({r.team})" for r in out_players.itertuples()
                              if r.min_s == r.min_s and r.min_s > 8)
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
        labels = dict(zip(ps["player_id"], ps["player"]))
        if offers:
            allo = pd.concat(offers, ignore_index=True)
            ev = E.evaluate(sim, gr.home, allo, labels=labels)
            ev.insert(1, "matchup", f"{gr.away} @ {gr.home}")
            edges.append(ev)
            # same-game multis only from players certain to play (questionable legs could void)
            certain = allo[allo["player_id"].isna() | allo["player_id"].isin(
                gp.loc[(gp["avail_prob"] >= 0.99) & (gp["rotation_prob"] >= 0.95), "player_id"])]
            mk_p = ev[["market", "selection", "line", "player_id", "market_novig_prob"]].drop_duplicates(
                ["market", "selection", "line", "player_id"])
            certain = certain.merge(mk_p, on=["market", "selection", "line", "player_id"], how="left")
            sg = sgm.suggest(sim, gr.home, gr.away, certain, labels)
            if len(sg):
                sg.insert(0, "matchup", f"{gr.away} @ {gr.home}")
                sgms.append(sg)
        sim_inputs.append(gp.assign(game_mu_margin=gr.mu_margin, game_mu_total=gr.mu_total,
                                    game_home=gr.home, game_away=gr.away))
        games_out.append(gs)
        players_out.append(ps)
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
        v.to_csv(d / f"{k}{tag}.csv", index=False)
    return d


def run(day: date, refresh: bool = True, with_props: bool = True) -> dict:
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
    props = props_market(slate, pg) if with_props else None
    res = project(day, slate.drop(columns=["tip_utc"]), sp, b, market=market, props=props,
                  book_lines=latest_book_lines(slate))
    tips = slate.set_index("game_id")["tip_utc"]
    if len(res["games"]):
        res["games"].insert(2, "tip_sydney", res["games"]["game_id"].map(
            lambda g: pd.Timestamp(tips[g]).tz_convert("Australia/Sydney").strftime("%a %d %b %H:%M")))
    res["availability"] = sp
    path = write_outputs(day, res)
    (path / "state.json").write_text(json.dumps({"availability_hash": availability_hash(sp),
                                                 "generated": pd.Timestamp.now(tz="UTC").isoformat()}))
    print("wrote", path)
    from .dashboard import build as build_page
    build_page(day)
    return res
