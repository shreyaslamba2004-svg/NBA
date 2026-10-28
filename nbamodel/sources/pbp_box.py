"""Rebuild player box scores (incl. minutes, starters, on-court +/-) from cdn.nba.com play-by-play.

Used for seasons where no public box-score CSV exists (2024-25 onwards) and for live
games pulled from cdn.nba.com/static/json/liveData/playbyplay/playbyplay_<gameId>.json.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

STATS = ["pts", "fgm", "fga", "fg3m", "fg3a", "ftm", "fta", "oreb", "dreb", "reb",
         "ast", "stl", "blk", "tov", "pf"]


def _clock_seconds(clock: str) -> float:
    # ISO-8601 'PT11M36.00S'
    m = re.match(r"PT(\d+)M([\d.]+)S", str(clock))
    return int(m.group(1)) * 60 + float(m.group(2)) if m else 0.0


def _period_len(period: int) -> float:
    return 720.0 if period <= 4 else 300.0


def game_box(g: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Box score for one game's cdn play-by-play rows (sorted by orderNumber/actionNumber)."""
    sort_col = "orderNumber" if "orderNumber" in g.columns else "actionNumber"
    g = g.sort_values(sort_col)
    g = g.assign(sec_left=g["clock"].map(_clock_seconds))

    # home/away team ids from scoring events
    sc = g[(g["actionType"].isin(["2pt", "3pt", "freethrow"])) & (g["shotResult"] == "Made")]
    sh, sa = g["scoreHome"].astype(float), g["scoreAway"].astype(float)
    dh, da = sh.diff().fillna(sh), sa.diff().fillna(sa)
    home_team = away_team = None
    for idx in sc.index:
        tid = int(sc.at[idx, "teamId"])
        if dh.at[idx] > 0 and home_team is None:
            home_team = tid
        elif da.at[idx] > 0 and away_team is None:
            away_team = tid
        if home_team and away_team:
            break
    teams = [int(t) for t in g["teamId"].dropna().unique() if t and t > 0]
    if home_team is None:
        home_team = [t for t in teams if t != away_team][0]
    if away_team is None:
        away_team = [t for t in teams if t != home_team][0]

    tri = (g.dropna(subset=["teamTricode"]).groupby("teamId")["teamTricode"].first().to_dict())
    player_team: dict[int, int] = {}
    names: dict[int, str] = {}
    for pid, tid, nm in g[["personId", "teamId", "playerName"]].itertuples(index=False):
        if pid and pid > 0 and tid and tid > 0:
            player_team.setdefault(int(pid), int(tid))
            if isinstance(nm, str):
                names.setdefault(int(pid), nm)

    box: dict[int, dict] = {p: dict.fromkeys(STATS, 0) | {"sec": 0.0, "pm": 0, "starter": 0}
                            for p in player_team}

    def add(pid, key, v=1):
        if pid and pid > 0 and int(pid) in box:
            box[int(pid)][key] += v

    final_h = final_a = 0
    prev_on: dict[int, set] = {}
    for period, pg in g.groupby("period", sort=True):
        plen = _period_len(int(period))
        # players on court at period start: anyone whose first event this period is not a sub-in
        on: dict[int, set] = {home_team: set(), away_team: set()}
        seen: set = set()
        for r in pg.itertuples(index=False):
            ids = []
            if r.actionType == "substitution":
                pid = int(r.personId)
                if pid not in seen:
                    seen.add(pid)
                    if r.subType == "out":
                        on[player_team.get(pid, r.teamId)].add(pid)
                continue
            for c in ("personId", "assistPersonId", "stealPersonId", "blockPersonId"):
                v = getattr(r, c, np.nan)
                if v == v and v and v > 0:
                    ids.append(int(v))
            for pid in ids:
                if pid not in seen:
                    seen.add(pid)
                    t = player_team.get(pid)
                    if t in on and not (r.actionType == "foul" and r.sec_left == 0):
                        on[t].add(pid)
        for t in on:
            # a player who played the whole period without an event is invisible above:
            # carry over from the previous period's closing lineup
            if len(on[t]) < 5:
                subbed_in_first = {int(r.personId) for r in pg[pg.actionType == "substitution"]
                                   .drop_duplicates("personId").itertuples() if r.subType == "in"}
                for p in prev_on.get(t, ()):
                    if len(on[t]) >= 5:
                        break
                    if p not in subbed_in_first:
                        on[t].add(p)
            if len(on[t]) > 5:  # noise (bench technicals etc.)
                on[t] = set(list(on[t])[:5])
        if int(period) == 1:
            for t in on:
                for p in on[t]:
                    box[p]["starter"] = 1

        last_t = plen
        prev_h = prev_a = None
        for r in pg.itertuples(index=False):
            t_now = r.sec_left
            el = max(0.0, last_t - t_now)
            if el:
                for t in on:
                    for p in on[t]:
                        box[p]["sec"] += el
                last_t = t_now
            if r.scoreHome == r.scoreHome and r.scoreHome != "":
                h, a = int(float(r.scoreHome)), int(float(r.scoreAway))
                if prev_h is None:
                    prev_h, prev_a = final_h, final_a
                ddh, dda = h - prev_h, a - prev_a
                if ddh or dda:
                    for p in on[home_team]:
                        box[p]["pm"] += ddh - dda
                    for p in on[away_team]:
                        box[p]["pm"] += dda - ddh
                prev_h, prev_a = h, a
                final_h, final_a = h, a
            at = r.actionType
            pid = int(r.personId) if r.personId == r.personId and r.personId else 0
            if at == "substitution":
                t = player_team.get(pid, r.teamId)
                if t in on:
                    if r.subType == "out":
                        on[t].discard(pid)
                    else:
                        on[t].add(pid)
            elif at in ("2pt", "3pt"):
                add(pid, "fga")
                if at == "3pt":
                    add(pid, "fg3a")
                if r.shotResult == "Made":
                    add(pid, "fgm"); add(pid, "pts", 2 if at == "2pt" else 3)
                    if at == "3pt":
                        add(pid, "fg3m")
                    ap = getattr(r, "assistPersonId", np.nan)
                    if ap == ap and ap:
                        add(int(ap), "ast")
            elif at == "freethrow":
                add(pid, "fta")
                if r.shotResult == "Made":
                    add(pid, "ftm"); add(pid, "pts")
            elif at == "rebound" and pid:
                add(pid, "reb"); add(pid, "oreb" if r.subType == "offensive" else "dreb")
            elif at == "steal":
                add(pid, "stl")
            elif at == "block":
                add(pid, "blk")
            elif at == "turnover":
                add(pid, "tov")
            elif at == "foul" and r.subType in ("personal", "offensive", "loose ball", "shooting", "flagrant"):
                add(pid, "pf")
        if last_t > 0:
            for t in on:
                for p in on[t]:
                    box[p]["sec"] += last_t
        prev_on = {t: set(v) for t, v in on.items()}

    rows = []
    for p, b in box.items():
        t = player_team[p]
        rows.append({"player_id": p, "player_name": names.get(p, ""), "team_id": t,
                     "team": tri.get(t, ""), "home": int(t == home_team),
                     "min": round(b["sec"] / 60, 2), **{k: b[k] for k in STATS},
                     "plus_minus": b["pm"], "starter": b["starter"]})
    out = pd.DataFrame(rows)
    out = out[(out["min"] > 0) | (out[STATS].sum(axis=1) > 0)]
    meta = {"home_team_id": home_team, "away_team_id": away_team,
            "home_pts": final_h, "away_pts": final_a,
            "home": tri.get(home_team, ""), "away": tri.get(away_team, ""),
            "periods": int(g["period"].max())}
    return out, meta


def season_box(pbp: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Player box + game results for every game in a cdn pbp season file."""
    pbp = pbp.copy()
    if "timeActual" in pbp.columns:
        ts = pd.to_datetime(pbp["timeActual"], utc=True, errors="coerce", format="mixed")
        pbp["_date"] = ts.dt.tz_convert("America/New_York").dt.date
    boxes, games = [], []
    for gid, g in pbp.groupby("gameId"):
        try:
            b, m = game_box(g)
        except Exception as e:  # malformed game; skip but report
            print(f"skip {gid}: {e}")
            continue
        date = g["_date"].dropna().min() if "_date" in g else None
        b["game_id"] = int(gid)
        b["game_date"] = date
        boxes.append(b)
        games.append({"game_id": int(gid), "game_date": date, **m})
    return pd.concat(boxes, ignore_index=True), pd.DataFrame(games)
