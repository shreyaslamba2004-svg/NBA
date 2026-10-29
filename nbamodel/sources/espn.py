"""ESPN public JSON API: schedule, box scores, injuries, officials and DraftKings lines.

nba.com (stats/cdn) refuses requests from most cloud IPs, so ESPN is the primary live
source for the current season. ESPN athlete ids are mapped onto nba.com person ids by
normalised name (falling back to a synthetic id) so history and live rows share one key.
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from ..teams import canonical_team
from .live import SourceUnavailable, _get, norm_name

BASE = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba"
SYNTH = 900_000_000  # synthetic player ids for players with no nba.com history


def scoreboard(day: date) -> pd.DataFrame:
    js = _get(f"{BASE}/scoreboard", params={"dates": day.strftime("%Y%m%d"), "limit": 50})
    rows = []
    for e in js.get("events", []):
        comp = e["competitions"][0]
        t = {c["homeAway"]: c for c in comp["competitors"]}
        if e.get("season", {}).get("type") not in (2, 3, 5):  # regular, playoffs, play-in
            continue
        rows.append({"game_id": int(e["id"]), "game_date": pd.Timestamp(day), "tip_utc": e["date"],
                     "home": canonical_team(t["home"]["team"]["abbreviation"]),
                     "away": canonical_team(t["away"]["team"]["abbreviation"]),
                     "home_pts": float(t["home"].get("score") or np.nan),
                     "away_pts": float(t["away"].get("score") or np.nan),
                     "status": e["status"]["type"]["name"],
                     "period": e["status"].get("period", 4),
                     "playoff": int(e["season"]["type"] == 3)})
    return pd.DataFrame(rows)


def summary(event_id: int) -> dict:
    return _get(f"{BASE}/summary", params={"event": event_id})


def _split(s: str) -> tuple[int, int]:
    try:
        a, b = s.split("-")
        return int(a), int(b)
    except Exception:
        return 0, 0


def _num(v) -> float:
    try:
        return float(str(v).replace("+", ""))
    except ValueError:  # '--' for players who checked in without logging a stat
        return 0.0


def box_from_summary(js: dict, crosswalk: "Crosswalk") -> pd.DataFrame:
    comp = js["header"]["competitions"][0]
    home_abbr = next(c["team"]["abbreviation"] for c in comp["competitors"] if c["homeAway"] == "home")
    rows = []
    for tb in js["boxscore"].get("players", []):
        team = canonical_team(tb["team"]["abbreviation"])
        st = tb["statistics"][0]
        lab = st["labels"]
        for a in st["athletes"]:
            ath = a["athlete"]
            pid = crosswalk.lookup(ath["id"], ath["displayName"], team)
            r = {"game_id": int(js["header"]["id"]), "team": team,
                 "home": int(team == canonical_team(home_abbr)), "player_id": pid,
                 "player_name": ath["displayName"], "espn_id": int(ath["id"]),
                 "starter": int(bool(a.get("starter"))),
                 "comment": (a.get("reason") or "") if a.get("didNotPlay") else ""}
            s = dict(zip(lab, a.get("stats") or []))
            if a.get("didNotPlay") or not s:
                r.update({"min": 0.0})
            else:
                fgm, fga = _split(s.get("FG", "0-0"))
                tpm, tpa = _split(s.get("3PT", "0-0"))
                ftm, fta = _split(s.get("FT", "0-0"))
                num = lambda k: _num(s.get(k, "0"))  # noqa: E731
                r.update({"min": num("MIN"), "pts": num("PTS"), "fgm": fgm, "fga": fga, "fg3m": tpm,
                          "fg3a": tpa, "ftm": ftm, "fta": fta, "oreb": num("OREB"), "dreb": num("DREB"),
                          "reb": num("REB"), "ast": num("AST"), "stl": num("STL"), "blk": num("BLK"),
                          "tov": num("TO"), "pf": num("PF"), "plus_minus": num("+/-")})
            rows.append(r)
    return pd.DataFrame(rows)


def injuries_from_summary(js: dict) -> pd.DataFrame:
    rows = []
    for t in js.get("injuries", []):
        team = canonical_team(t["team"]["abbreviation"])
        for i in t.get("injuries", []):
            rows.append({"team": team, "player": i["athlete"]["displayName"],
                         "espn_id": int(i["athlete"]["id"]), "status": i.get("status", ""),
                         "reason": (i.get("details") or {}).get("type", ""),
                         "return_date": (i.get("details") or {}).get("returnDate"), "source": "espn"})
    return pd.DataFrame(rows)


def lines_from_summary(js: dict) -> dict:
    """DraftKings lines carried on ESPN (open and current/close)."""
    pc = (js.get("pickcenter") or [{}])[0]
    if not pc:
        return {}
    out = {"book": pc.get("provider", {}).get("name"), "spread_home": pc.get("spread"),
           "total": pc.get("overUnder"), "over_price": pc.get("overOdds"),
           "under_price": pc.get("underOdds"),
           "ml_home": (pc.get("homeTeamOdds") or {}).get("moneyLine"),
           "ml_away": (pc.get("awayTeamOdds") or {}).get("moneyLine"),
           "spread_home_price": (pc.get("homeTeamOdds") or {}).get("spreadOdds"),
           "spread_away_price": (pc.get("awayTeamOdds") or {}).get("spreadOdds")}
    try:
        out["spread_home_open"] = float(pc["pointSpread"]["home"]["open"]["line"])
        out["total_open"] = float(pc["total"]["over"]["open"]["line"][1:])
    except (KeyError, TypeError, ValueError):
        pass
    return out


def officials_from_summary(js: dict) -> list[str]:
    return [o["displayName"] for o in js.get("gameInfo", {}).get("officials", [])]


ESPN_ABBR = {"GSW": "GS", "NOP": "NO", "NYK": "NY", "SAS": "SA", "UTA": "UTAH", "WAS": "WSH"}


def team_roster(team: str) -> pd.DataFrame:
    """Current roster (catches signings/trades not yet in any box score)."""
    js = _get(f"{BASE}/teams/{ESPN_ABBR.get(team, team).lower()}/roster")
    return pd.DataFrame([{"team": canonical_team(team), "espn_id": int(a["id"]),
                          "player_name": a["displayName"],
                          "injury_status": (a.get("injuries") or [{}])[0].get("status") if a.get("injuries") else None}
                         for a in js.get("athletes", [])])


class Crosswalk:
    """ESPN athlete id -> nba.com person id, matched on normalised name (team as tie-break)."""

    def __init__(self, pg_hist: pd.DataFrame, path: Path):
        self.path = path
        self.map: dict[str, int] = json.loads(path.read_text()) if path.exists() else {}
        recent = pg_hist.sort_values("game_date").drop_duplicates("player_id", keep="last")
        recent = recent[recent["game_date"] >= recent["game_date"].max() - pd.Timedelta(days=4 * 365)]
        self.by_name: dict[str, list] = {}
        for r in recent[["player_id", "player_name", "team"]].itertuples(index=False):
            if isinstance(r.player_name, str):
                self.by_name.setdefault(norm_name(r.player_name), []).append((r.player_id, r.team))
        # play-by-play derived seasons store surnames only; full names come from boxscore years
        full = pg_hist[pg_hist["player_name"].str.contains(" ", na=False)].drop_duplicates("player_id")
        for r in full[["player_id", "player_name", "team"]].itertuples(index=False):
            k = norm_name(r.player_name)
            if all(p != r.player_id for p, _ in self.by_name.get(k, [])):
                self.by_name.setdefault(k, []).append((r.player_id, r.team))

        # surname + team index for play-by-play seasons (2024-25 on), which only carry surnames
        self.by_last: dict[tuple, list] = {}
        self.new_names: dict[str, int] = {}  # players with no NBA history, filled as rosters are read
        pbp = pg_hist[pg_hist["season"] >= "2024-25"].sort_values("game_date").drop_duplicates(
            ["player_id", "team"], keep="last")
        for r in pbp[["player_id", "player_name", "team"]].itertuples(index=False):
            self.by_last.setdefault((norm_name(r.player_name), r.team), []).append(r.player_id)

    def lookup(self, espn_id, name: str, team: str | None = None) -> int:
        key = str(espn_id)
        if key in self.map:
            if self.map[key] >= SYNTH and name:
                self.new_names[norm_name(name)] = self.map[key]
            return self.map[key]
        cands = self.by_name.get(norm_name(name), [])
        if not cands and norm_name(name) in self.new_names:
            return self.new_names[norm_name(name)]
        if not cands and team:
            parts = name.split(" ", 1)
            ids = self.by_last.get((norm_name(parts[-1]), team), [])
            if len(set(ids)) == 1:
                cands = [(ids[0], team)]
        if len(cands) == 1:
            pid = int(cands[0][0])
        elif cands:
            same = [p for p, t in cands if t == team]
            pid = int(same[0] if same else cands[-1][0])
        elif key.isdigit():
            pid = SYNTH + int(espn_id)  # no NBA history yet (rookies, new signings)
            self.new_names[norm_name(name)] = pid
        else:
            return None  # name-only lookup with no match
        self.map[key] = pid
        return pid

    def save(self):
        self.path.write_text(json.dumps(self.map))


def backfill(start: date, end: date, crosswalk: Crosswalk, season: str,
             known_ids: set[int] | None = None) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Box scores + results + DraftKings lines for completed games in [start, end)."""
    known_ids = known_ids or set()
    boxes, games, lines = [], [], []
    d = start
    while d < end:
        try:
            sb = scoreboard(d)
        except SourceUnavailable as e:
            print("scoreboard unavailable", d, e)
            d += timedelta(days=1)
            continue
        if sb.empty:
            d += timedelta(days=1)
            continue
        for g in sb[sb["status"] == "STATUS_FINAL"].itertuples(index=False):
            if g.game_id in known_ids:
                continue
            try:
                js = summary(g.game_id)
                b = box_from_summary(js, crosswalk)
            except (SourceUnavailable, KeyError, IndexError) as e:
                print("skipping", g.game_id, e)
                continue
            b["game_date"] = pd.Timestamp(d)
            b["season"] = season
            b["playoff"] = g.playoff
            boxes.append(b)
            games.append({"game_id": g.game_id, "season": season, "game_date": pd.Timestamp(d),
                          "playoff": g.playoff, "home": g.home, "away": g.away,
                          "home_pts": g.home_pts, "away_pts": g.away_pts, "periods": g.period,
                          "home_team_id": None, "away_team_id": None})
            ln = lines_from_summary(js)
            if ln:
                lines.append({"game_id": g.game_id, "game_date": pd.Timestamp(d), "home": g.home,
                              "away": g.away, **ln, "officials": ", ".join(officials_from_summary(js))})
        d += timedelta(days=1)
    crosswalk.save()
    cat = lambda x: pd.concat(x, ignore_index=True) if x else pd.DataFrame()  # noqa: E731
    return cat(boxes), pd.DataFrame(games), pd.DataFrame(lines)


# ------------------------------------------------------------------ player props (DraftKings via ESPN)

CORE = "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba"
PROP_TYPES = {"Total Points": "pts", "Total Rebounds": "reb", "Total Assists": "ast",
              "Total 3-Point Field Goals": "fg3m", "Total Steals": "stl", "Total Blocks": "blk",
              "Total Turnovers": "tov", "Total Points and Rebounds": "pr", "Total Points and Assists": "pa",
              "Total Assists and Rebounds": "ra", "Total Points, Rebounds, and Assists": "pra",
              "Total Steals and Blocks": "stocks"}
MILESTONES = {"Points Milestones": "pts", "Rebounds Milestones": "reb", "Assists Milestones": "ast",
              "3-Point Field Goals Milestones": "fg3m", "Steals Milestones": "stl", "Blocks Milestones": "blk",
              "Points + Rebounds Milestones": "pr", "Points + Assists Milestones": "pa",
              "Points + Assists + Rebounds Milestones": "pra"}


def props(event_id: int, provider: int = 100) -> pd.DataFrame:
    """Every player prop ESPN carries for a game (provider 100 = DraftKings), open + current.

    Over/under props arrive as consecutive pairs with no side label: the feed lists the over
    first. Milestones ("15+") are over-only and are stored as line N-0.5.
    """
    url = f"{CORE}/events/{event_id}/competitions/{event_id}/odds/{provider}/propBets"
    items, page = [], 1
    while True:
        js = _get(url, params={"limit": 1000, "page": page})
        items += js.get("items", [])
        if page >= js.get("pageCount", 1):
            break
        page += 1
    rows, seen = [], {}
    for it in items:
        name = it["type"]["name"]
        ath = it.get("athlete", {}).get("$ref", "")
        if not ath:
            continue
        aid = int(ath.split("/athletes/")[1].split("?")[0])
        odds = it.get("odds", {})
        am = odds.get("american", {})
        cur_t = (it.get("current") or {}).get("target", {}).get("value")
        open_t = (it.get("open") or {}).get("target", {}).get("value")
        if name in PROP_TYPES:
            k = (aid, name, cur_t)
            side = "over" if k not in seen else "under"
            seen[k] = True
            stat, line, open_line = PROP_TYPES[name], cur_t, open_t
        elif name in MILESTONES:
            side, stat = "over", MILESTONES[name]
            line = cur_t - 0.5 if cur_t is not None else None
            open_line = open_t - 0.5 if open_t is not None else None
        else:
            continue
        rows.append({"game_id": int(event_id), "espn_id": aid, "stat": stat,
                     "market": "milestone" if name in MILESTONES else "ou", "side": side,
                     "line": line, "price": _num(am.get("value")), "open_line": open_line,
                     "open_price": _num(am.get("open")), "book": "draftkings",
                     "last_updated": it.get("lastUpdated")})
    return _main_ladders(pd.DataFrame(rows))


def _main_ladders(df: pd.DataFrame) -> pd.DataFrame:
    """ESPN files several milestone ladders under one type (e.g. full-game and what look like
    first-quarter rebounds, both "Rebounds Milestones"). In feed order a new ladder starts when the
    target stops increasing. Keep the full-game ladder: the one whose price at the player's main
    over/under line matches that over price, else the ladder reaching the highest target."""
    if df.empty:
        return df
    ms = df[df["market"] == "milestone"].copy()
    ms["ladder"] = (ms.groupby(["espn_id", "stat"])["line"].diff().fillna(1) <= 0).astype(int)
    ms["ladder"] = ms.groupby(["espn_id", "stat"])["ladder"].cumsum()
    ou = df[(df["market"] == "ou") & (df["side"] == "over")].set_index(["espn_id", "stat"])
    keep = []
    for (aid, stat), g in ms.groupby(["espn_id", "stat"]):
        if g["ladder"].nunique() == 1:
            keep.append(g)
            continue
        best = None
        if (aid, stat) in ou.index:
            o = ou.loc[[(aid, stat)]].iloc[0]
            at = g[g["line"] == o["line"]]
            if len(at):
                gap = (_implied(at["price"]) - float(_implied(pd.Series([o["price"]])).iloc[0])).abs()
                if gap.min() < 0.08:
                    best = at.loc[gap.idxmin(), "ladder"]
        if best is None:
            best = g.loc[g["line"].idxmax(), "ladder"]
        keep.append(g[g["ladder"] == best])
    ms = pd.concat(keep).drop(columns="ladder") if keep else ms.drop(columns="ladder")
    return pd.concat([df[df["market"] != "milestone"], ms], ignore_index=True)


def _implied(american: pd.Series) -> pd.Series:
    a = american.astype(float)
    return pd.Series(np.where(a < 0, -a / (100 - a), 100 / (a + 100)), index=american.index)


def draft_pick(espn_id: int) -> int | None:
    """Overall draft pick (1-60), or None if undrafted / unknown."""
    try:
        d = _get(f"{CORE}/athletes/{int(espn_id)}", params={"lang": "en", "region": "us"}).get("draft") or {}
    except SourceUnavailable:
        return None
    if not d.get("selection"):
        return None
    return int(d["selection"]) + (30 * (int(d.get("round", 1)) - 1) if d["selection"] <= 30 and d.get("round", 1) > 1 else 0)


def pregame_lineup(game_id: int) -> pd.DataFrame:
    """Starters, and players ruled out with a reason (injury, illness, personal), once ESPN posts
    the pre-game box (around 30 minutes before tip). Empty until then. ESPN's own "active" flag
    means on court right now, so it isn't used. Columns: espn_id, player_name, team, starter, out."""
    try:
        js = summary(game_id)
    except Exception:
        return pd.DataFrame()
    rows = []
    for tb in js.get("boxscore", {}).get("players", []) or []:
        team = canonical_team(tb["team"]["abbreviation"])
        for st in tb.get("statistics", [])[:1]:
            for a in st.get("athletes", []):
                ath = a.get("athlete", {})
                rows.append({"espn_id": int(ath.get("id", 0)), "player_name": ath.get("displayName", ""),
                             "team": team, "starter": bool(a.get("starter")),
                             "out": bool(a.get("didNotPlay")) and str(a.get("reason", "")).upper() != "COACH'S DECISION"})
    return pd.DataFrame(rows)

