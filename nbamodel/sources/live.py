"""Live data: today's slate, current-season box scores, injuries/rest, and market odds.

All of these need outbound network access to the hosts listed in README.md. Each fetcher
returns a DataFrame and raises `SourceUnavailable` when a host can't be reached so the
pipeline can fall back to the next source.
"""
from __future__ import annotations

import io
import os
import re
import time
import unicodedata
from datetime import date, datetime, timedelta

import pandas as pd
import requests

from ..teams import canonical_team

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36",
      "Referer": "https://www.nba.com/", "Origin": "https://www.nba.com", "Accept": "application/json"}
CDN = "https://cdn.nba.com/static/json"
ESPN = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba"
ODDS_API = "https://api.the-odds-api.com/v4/sports/basketball_nba"
STATUS_WORDS = ["Out", "Doubtful", "Questionable", "Probable", "Available"]


CREDITS: dict = {"remaining": None}
MIN_CREDITS = int(os.environ.get("ODDS_API_MIN_CREDITS", "20"))


class SourceUnavailable(RuntimeError):
    pass


def _get(url: str, params=None, timeout=20, retries=3, raw=False):
    last = None
    for i in range(retries):
        try:
            r = requests.get(url, params=params, headers=UA, timeout=timeout)
            if "x-requests-remaining" in r.headers:  # The Odds API credit meter
                CREDITS["remaining"] = int(float(r.headers["x-requests-remaining"]))
            if r.status_code == 200:
                return r.content if raw else r.json()
            if r.status_code in (403, 404):
                raise SourceUnavailable(f"{url} -> HTTP {r.status_code}")
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            last = e
        time.sleep(1.5 * (i + 1))  # be polite: back off between retries
    raise SourceUnavailable(f"{url}: {last}")


def norm_name(n: str) -> str:
    n = unicodedata.normalize("NFKD", str(n)).encode("ascii", "ignore").decode()
    if "," in n:  # "Last, First" (official injury report)
        last, first = [x.strip() for x in n.split(",", 1)]
        n = f"{first} {last}"
    n = re.sub(r"[^a-z]", "", n.lower())
    return re.sub(r"(jr|sr|iii|ii|iv)$", "", n)


# ---------------------------------------------------------------- schedule

def schedule(day: date) -> pd.DataFrame:
    """Games on `day` (ET). Primary: NBA league schedule; fallback: ESPN scoreboard."""
    try:
        js = _get(f"{CDN}/staticData/scheduleLeagueV2.json")
        rows = []
        for d in js["leagueSchedule"]["gameDates"]:
            if datetime.strptime(d["gameDate"][:10], "%m/%d/%Y").date() != day:
                continue
            for g in d["games"]:
                if not str(g["gameId"]).startswith(("002", "004", "006")):
                    continue  # regular season, playoffs, NBA Cup knockout
                rows.append({"game_id": int(g["gameId"]), "game_date": pd.Timestamp(day),
                             "tip_utc": g.get("gameDateTimeUTC"),
                             "home": canonical_team(g["homeTeam"]["teamTricode"]),
                             "away": canonical_team(g["awayTeam"]["teamTricode"])})
        return pd.DataFrame(rows)
    except SourceUnavailable:
        js = _get(f"{ESPN}/scoreboard", params={"dates": day.strftime("%Y%m%d")})
        rows = []
        for e in js.get("events", []):
            comp = e["competitions"][0]
            teams = {c["homeAway"]: canonical_team(c["team"]["abbreviation"]) for c in comp["competitors"]}
            rows.append({"game_id": int(e["id"]), "game_date": pd.Timestamp(day), "tip_utc": e["date"],
                         "home": teams["home"], "away": teams["away"]})
        return pd.DataFrame(rows)


# ---------------------------------------------------------------- box scores (current season)

def _iso_min(s) -> float:
    m = re.match(r"PT(\d+)M([\d.]+)S", str(s))
    return int(m.group(1)) + float(m.group(2)) / 60 if m else 0.0


def boxscore(game_id: int) -> tuple[pd.DataFrame, dict]:
    """Final (or live) box score from cdn.nba.com, same schema as history player_games."""
    js = _get(f"{CDN}/liveData/boxscore/boxscore_{game_id:010d}.json")["game"]
    rows = []
    for side in ("homeTeam", "awayTeam"):
        t = js[side]
        for p in t["players"]:
            s = p.get("statistics", {})
            rows.append({
                "game_id": int(game_id), "team_id": t["teamId"], "team": canonical_team(t["teamTricode"]),
                "home": int(side == "homeTeam"), "player_id": p["personId"], "player_name": p["name"],
                "starter": int(p.get("starter", "0") == "1"),
                "comment": p.get("notPlayingReason", "") or "",
                "min": _iso_min(s.get("minutes")), "pts": s.get("points", 0),
                "fgm": s.get("fieldGoalsMade", 0), "fga": s.get("fieldGoalsAttempted", 0),
                "fg3m": s.get("threePointersMade", 0), "fg3a": s.get("threePointersAttempted", 0),
                "ftm": s.get("freeThrowsMade", 0), "fta": s.get("freeThrowsAttempted", 0),
                "oreb": s.get("reboundsOffensive", 0), "dreb": s.get("reboundsDefensive", 0),
                "reb": s.get("reboundsTotal", 0), "ast": s.get("assists", 0), "stl": s.get("steals", 0),
                "blk": s.get("blocks", 0), "tov": s.get("turnovers", 0), "pf": s.get("foulsPersonal", 0),
                "plus_minus": s.get("plusMinusPoints", 0), "status": p.get("status")})
    meta = {"game_id": int(game_id), "home": canonical_team(js["homeTeam"]["teamTricode"]),
            "away": canonical_team(js["awayTeam"]["teamTricode"]),
            "home_team_id": js["homeTeam"]["teamId"], "away_team_id": js["awayTeam"]["teamId"],
            "home_pts": js["homeTeam"]["score"], "away_pts": js["awayTeam"]["score"],
            "periods": js.get("period", 4), "game_status": js.get("gameStatus")}
    return pd.DataFrame(rows), meta


def season_games_so_far(season_start_year: int, through: date) -> pd.DataFrame:
    """Completed games of the current season, from the league schedule."""
    js = _get(f"{CDN}/staticData/scheduleLeagueV2.json")
    rows = []
    for d in js["leagueSchedule"]["gameDates"]:
        gd = datetime.strptime(d["gameDate"][:10], "%m/%d/%Y").date()
        if gd >= through:
            continue
        for g in d["games"]:
            if str(g["gameId"]).startswith(("002", "004", "006")) and g.get("gameStatus") == 3:
                rows.append({"game_id": int(g["gameId"]), "game_date": pd.Timestamp(gd)})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- injuries / rest

def injuries_official(day: date) -> pd.DataFrame:
    """Parse the latest official NBA injury report PDF published for `day`.

    The league publishes reports through the day (every 15 min since 2025-26);
    walk back from now until one exists.
    """
    import pdfplumber

    base = "https://ak-static.cms.nba.com/referee/injury/Injury-Report_{d}_{t}.pdf"
    now = pd.Timestamp.now(tz="America/New_York").tz_localize(None).to_pydatetime()
    t = now.replace(minute=(now.minute // 15) * 15, second=0, microsecond=0)
    pdf = None
    for _ in range(4 * 30):
        for fmt in ("%I_%M%p", "%I%p"):
            url = base.format(d=day.isoformat(), t=t.strftime(fmt))
            try:
                pdf = _get(url, raw=True, retries=1, timeout=10)
                break
            except SourceUnavailable:
                continue
        if pdf:
            break
        t -= timedelta(minutes=15)
    if not pdf:
        raise SourceUnavailable("no official injury report found")
    df = parse_injury_pdf(pdf)
    return df[df["game_date"].isna() | (df["game_date"] == pd.Timestamp(day))] if len(df) else df


def fetch_injury_pdf(day: date, time_label: str) -> bytes:
    """A specific report, e.g. time_label '05PM' (pre-2025) or '05_00PM' (2025-26 on)."""
    return _get(f"https://ak-static.cms.nba.com/referee/injury/Injury-Report_{day.isoformat()}_{time_label}.pdf",
                raw=True, retries=1, timeout=15)


def parse_injury_pdf(pdf: bytes) -> pd.DataFrame:
    import pdfplumber
    text = "\n".join(p.extract_text() or "" for p in pdfplumber.open(io.BytesIO(pdf)).pages)
    # the PDF text layer often drops spaces inside cells: "BrooklynNets Bilodeau,Tyler Out GLeague-Two-Way"
    from ..teams import TEAMS
    full_names = {v[1].replace(" ", ""): k for k, v in TEAMS.items()}
    full_names["LAClippers"] = "LAC"
    rows, team, gdate = [], None, None
    for line in text.splitlines():
        dm = re.match(r"\s*(\d{2}/\d{2}/\d{4})", line)
        if dm:
            gdate = pd.Timestamp(datetime.strptime(dm.group(1), "%m/%d/%Y"))
        compact = line.replace(" ", "")
        for name, tri in full_names.items():
            if name in compact:
                team = tri
        m = re.search(r"([A-Z][\w'.\-]*(?: (?:Jr\.|Sr\.|II|III|IV))?,\s?[A-Z][\w'.\-]*)\s+(" +
                      "|".join(STATUS_WORDS) + r")\b(.*)", line)
        if m and team:
            rows.append({"game_date": gdate, "team": team, "player": m.group(1).strip(), "status": m.group(2),
                         "reason": m.group(3).strip(), "source": "nba_official"})
    df = pd.DataFrame(rows)
    if len(df):
        df["key"] = df["player"].map(norm_name)
    return df


def injuries_espn() -> pd.DataFrame:
    js = _get(f"{ESPN}/injuries")
    rows = []
    for t in js.get("injuries", []):
        tri = canonical_team(t.get("displayName"))
        for i in t.get("injuries", []):
            st = i.get("status", "")
            st = "Out" if st.lower().startswith("out") else st.title()
            rows.append({"team": tri, "player": i["athlete"]["displayName"], "status": st,
                         "reason": i.get("shortComment", ""), "source": "espn"})
    df = pd.DataFrame(rows)
    if len(df):
        df["key"] = df["player"].map(norm_name)
    return df


def injuries(day: date) -> pd.DataFrame:
    """Merge official report (authoritative) with ESPN (fills gaps, e.g. long-term injuries)."""
    frames = []
    for f in (lambda: injuries_official(day), injuries_espn):
        try:
            frames.append(f())
        except SourceUnavailable as e:
            print("injury source unavailable:", e)
    if not frames:
        raise SourceUnavailable("no injury source reachable")
    df = pd.concat(frames, ignore_index=True)
    return df.drop_duplicates("key", keep="first")


def pregame_actives(game_id: int) -> pd.DataFrame | None:
    """~30-60 min before tip the live boxscore lists ACTIVE/INACTIVE and starters."""
    try:
        b, _ = boxscore(game_id)
    except SourceUnavailable:
        return None
    return b[["team", "player_id", "player_name", "starter", "status", "comment"]]


# ---------------------------------------------------------------- odds

GAME_MARKETS = "h2h,spreads,totals"
PROP_MARKETS = {"player_points": "pts", "player_rebounds": "reb", "player_assists": "ast",
                "player_threes": "fg3m", "player_steals": "stl", "player_blocks": "blk",
                "player_turnovers": "tov", "player_points_rebounds_assists": "pra"}


def odds_games(api_key: str | None = None, regions: str | None = None,
               bookmakers: str | None = None) -> pd.DataFrame:
    """Moneyline / spread / total from The Odds API (free tier: 500 credits/month)."""
    key = api_key or os.environ.get("ODDS_API_KEY")
    if not key:
        raise SourceUnavailable("set ODDS_API_KEY (https://the-odds-api.com)")
    # one call returns every game: cost = 3 markets x regions (e.g. 3 credits for "au")
    regions = regions or os.environ.get("ODDS_REGIONS", "us")
    params = {"apiKey": key, "regions": regions, "markets": GAME_MARKETS, "oddsFormat": "american"}
    if bookmakers:
        params["bookmakers"] = bookmakers
    js = _get(f"{ODDS_API}/odds", params=params)
    rows = []
    for ev in js:
        home, away = canonical_team(ev["home_team"]), canonical_team(ev["away_team"])
        for bk in ev["bookmakers"]:
            for mk in bk["markets"]:
                for o in mk["outcomes"]:
                    rows.append({"event_id": ev["id"], "commence": ev["commence_time"], "home": home,
                                 "away": away, "book": bk["key"], "market": mk["key"],
                                 "side": canonical_team(o["name"]) if mk["key"] != "totals" else o["name"],
                                 "line": o.get("point"), "price": o["price"]})
    return pd.DataFrame(rows)


def odds_events(api_key: str | None = None) -> pd.DataFrame:
    """Upcoming NBA events (free: costs no credits)."""
    key = api_key or os.environ.get("ODDS_API_KEY")
    if not key:
        raise SourceUnavailable("set ODDS_API_KEY")
    js = _get(f"{ODDS_API}/events", params={"apiKey": key})
    return pd.DataFrame([{"event_id": e["id"], "commence": e["commence_time"],
                          "home": canonical_team(e["home_team"]), "away": canonical_team(e["away_team"])}
                         for e in js])


def odds_props(event_id: str, api_key: str | None = None, regions: str | None = None) -> pd.DataFrame:
    """Costs len(markets) credits per call; default two markets keeps a daily run under 500/month."""
    if CREDITS["remaining"] is not None and CREDITS["remaining"] < MIN_CREDITS:
        raise SourceUnavailable(f"only {CREDITS['remaining']} Odds API credits left; saving them")
    # default fits the free 500/month: ~8 games x 1 market x 30 days + game lines
    markets = os.environ.get("PROP_MARKETS", "player_points")
    regions = regions or os.environ.get("ODDS_REGIONS", "us")
    key = api_key or os.environ.get("ODDS_API_KEY")
    if not key:
        raise SourceUnavailable("set ODDS_API_KEY")
    js = _get(f"{ODDS_API}/events/{event_id}/odds",
              params={"apiKey": key, "regions": regions, "markets": markets,
                      "oddsFormat": "american"})
    rows = []
    for bk in js.get("bookmakers", []):
        for mk in bk["markets"]:
            for o in mk["outcomes"]:
                rows.append({"event_id": event_id, "book": bk["key"], "stat": PROP_MARKETS.get(mk["key"]),
                             "player": o.get("description"), "key": norm_name(o.get("description", "")),
                             "side": o["name"], "line": o.get("point"), "price": o["price"]})
    return pd.DataFrame(rows)


def referees(day: date) -> pd.DataFrame:
    """Official referee assignments (published ~9am ET). Stored for analysis/features."""
    js = _get("https://official.nba.com/wp-json/api/v1/get-game-officials",
              params={"date": day.isoformat()})
    rows = []
    for g in js.get("nba", {}).get("Table", {}).get("rows", []):
        rows.append({"game_id": g.get("game_id"), "home": canonical_team(g.get("home_team")),
                     "away": canonical_team(g.get("away_team")),
                     "officials": [g.get(k) for k in ("official1", "official2", "official3")]})
    return pd.DataFrame(rows)
