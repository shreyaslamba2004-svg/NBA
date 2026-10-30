"""Append-only log of market lines next to model projections, to build a model-vs-market record.

Game lines (moneyline, spread, total) and the full DraftKings player-prop menu (open and
current prices) come from ESPN's public feeds: free, no key. If ODDS_API_KEY is set, other
books' prop prices from The Odds API are logged too (free tier: 500 credits/month).

Files (CSV, one row per observation, never overwritten; one file per game day so none grows
past GitHub's 100 MB file limit, and days more than one day old are gzipped by the nightly run):
  logs/market/game_lines/<date>.csv   snapshot_utc, game_id, matchup, book, spreads/totals/MLs
  logs/market/props/<date>.csv        snapshot_utc, game_id, player, stat, side, line, price, book
  logs/market/book_lines/<date>.csv   every AU book's game lines (Odds API)
  logs/projections/<date>_games.csv / _players.csv / _edges.csv   model output at each snapshot
  logs/results/<date>.csv        final scores + player box lines, joined later for grading
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from .sources import espn, live
from .sources.live import SourceUnavailable

ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "logs"


def _append(path: Path, df: pd.DataFrame) -> None:
    if df is None or df.empty:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        head = path.open().readline().strip().split(",")
        if list(df.columns) != head:  # columns changed (new fields): rewrite with the union
            old = _read_log(path)
            pd.concat([old, df], ignore_index=True).to_csv(path, index=False)
            return
    df.to_csv(path, mode="a", header=not path.exists(), index=False)


def log_file(path: Path) -> Path | None:
    """A day's log, plain or already gzipped by compact(); None if neither exists."""
    gz = path.with_name(path.name + ".gz")
    return path if path.exists() else gz if gz.exists() else None


def recent_logs(folder: Path, n: int = 2) -> list[Path]:
    """The last n dated logs in a folder (plain or gzipped)."""
    fs = sorted(list(folder.glob("*.csv")) + list(folder.glob("*.csv.gz")), key=lambda f: f.name[:10])
    return fs[-n:]


def compact(keep_days: int = 2) -> None:
    """Gzip dated logs older than keep_days (they're no longer appended to). About 8x smaller."""
    import gzip
    import shutil
    cutoff = (pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=keep_days)).strftime("%Y-%m-%d")
    for f in [*(LOGS / "projections").glob("*.csv"), *(LOGS / "market").glob("*/*.csv")]:
        if f.name[:10] < cutoff and f.name[:4].isdigit():
            with f.open("rb") as src, gzip.open(f.with_name(f.name + ".gz"), "wb") as dst:
                shutil.copyfileobj(src, dst)
            f.unlink()


def _read_log(path: Path) -> pd.DataFrame:
    """Read a log even if an older version appended rows with extra columns under an old header."""
    import csv
    import io
    with path.open() as f:
        rows = list(csv.reader(f))
    head, body = rows[0], rows[1:]
    width = max(len(r) for r in body) if body else len(head)
    if width > len(head):
        head = head + [f"_extra{i}" for i in range(width - len(head))]
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(head)
    w.writerows(r + [""] * (width - len(r)) for r in body)
    buf.seek(0)
    return pd.read_csv(buf, low_memory=False)  # same type inference as a normal read


def log_game_lines(slate: pd.DataFrame, snapshot: str) -> pd.DataFrame:
    rows = []
    for r in slate.itertuples(index=False):
        try:
            ln = espn.lines_from_summary(espn.summary(r.game_id))
        except SourceUnavailable:
            continue
        if ln:
            rows.append({"snapshot_utc": snapshot, "game_id": r.game_id, "date": str(r.game_date)[:10],
                         "matchup": f"{r.away} @ {r.home}", **ln})
    df = pd.DataFrame(rows)
    for d, part in df.groupby("date") if len(df) else []:
        _append(LOGS / "market" / "game_lines" / f"{d}.csv", part)
    return df


def log_props(slate: pd.DataFrame, snapshot: str, use_odds_api: bool = True) -> pd.DataFrame:
    """Every DraftKings prop ESPN carries (free), plus Odds API books when ODDS_API_KEY is set."""
    from .pipeline import props_market
    df = props_market(slate, use_odds_api=use_odds_api)
    if df is None or df.empty:
        return pd.DataFrame()
    df = df.assign(snapshot_utc=snapshot, date=str(slate["game_date"].iloc[0])[:10])
    _append(LOGS / "market" / "props" / f"{str(slate['game_date'].iloc[0])[:10]}.csv", df)
    return df


def log_book_lines(snapshot: str) -> pd.DataFrame:
    """Every bookmaker's ML/spread/total in ODDS_REGIONS (e.g. "au": Sportsbet, TAB, Ladbrokes,
    Neds, PointsBet, Betfair Exchange...). One call covers the whole slate."""
    try:
        df = live.odds_games()
    except SourceUnavailable as e:
        print("book lines skipped:", e)
        return pd.DataFrame()
    df = df.assign(snapshot_utc=snapshot)
    _append(LOGS / "market" / "book_lines" / f"{snapshot[:10]}.csv", df)
    return df


def log_projections(day: date, res: dict, snapshot: str) -> None:
    for k in ("games", "players", "edges"):
        if k in res and len(res[k]):
            _append(LOGS / "projections" / f"{day.isoformat()}_{k}.csv", res[k].assign(snapshot_utc=snapshot))


def log_results(day: date) -> None:
    """Final scores and player lines for `day`, used to grade earlier projections/markets."""
    sb = espn.scoreboard(day)
    if sb.empty:
        return
    fin = sb[sb["status"] == "STATUS_FINAL"]
    path = LOGS / "results" / f"{day.isoformat()}.csv"
    if path.exists():
        return
    class _Ids:  # results are keyed by name; no need for nba.com ids here
        lookup = staticmethod(lambda espn_id, name, team=None: int(espn_id))
    cw = _Ids()
    rows = []
    for g in fin.itertuples(index=False):
        b = espn.box_from_summary(espn.summary(g.game_id), cw)
        b = b[b["min"] > 0]
        for r in b.itertuples(index=False):
            rows.append({"game_id": g.game_id, "home": g.home, "away": g.away, "home_pts": g.home_pts,
                         "away_pts": g.away_pts, "team": r.team, "player": r.player_name, "min": r.min,
                         "pts": r.pts, "reb": r.reb, "ast": r.ast, "fg3m": r.fg3m, "stl": r.stl,
                         "blk": r.blk, "tov": r.tov})
    _append(path, pd.DataFrame(rows))
