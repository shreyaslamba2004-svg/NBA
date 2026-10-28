"""Download and unify every historical source reachable into data/processed/.

Outputs
  player_games.parquet  one row per player per game (incl. DNP rows where known)
  games.parquet         one row per game with home/away and final score
  odds.parquet          historical closing lines (spread, total, moneylines)
"""
from __future__ import annotations

import sqlite3
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nbamodel.sources.pbp_box import season_box  # noqa: E402
from nbamodel.teams import canonical_team  # noqa: E402

RAW, OUT = ROOT / "data/raw", ROOT / "data/processed"
NB = "https://raw.githubusercontent.com/NocturneBear/NBA-Data-2010-2024/main/"
SH = "https://raw.githubusercontent.com/shufinskiy/nba_data/main/datasets/"
ODDS = "https://raw.githubusercontent.com/kyleskom/NBA-Machine-Learning-Sports-Betting/master/Data/OddsData.sqlite"
NB_FILES = [f"regular_season_box_scores_2010_2024_part_{i}.csv" for i in (1, 2, 3)] + [
    "play_off_box_scores_2010_2024.csv", "regular_season_totals_2010_2024.csv",
    "play_off_totals_2010_2024.csv"]
# cdn.nba.com play-by-play archives; file year = season start year (2024 -> 2024-25)
PBP_SEASONS = {"cdnnba_2024": ("2024-25", 0), "cdnnba_po_2024": ("2024-25", 1),
               "cdnnba_2025": ("2025-26", 0), "cdnnba_po_2025": ("2025-26", 1)}


def fetch(url: str, dest: Path) -> Path:
    if not dest.exists():
        print("downloading", url)
        subprocess.run(["curl", "-sSfL", "-o", str(dest), url], check=True)
    return dest


def _mins(x) -> float:
    if not isinstance(x, str) or ":" not in x:
        return 0.0
    a, b = x.split(":")
    return int(a) + int(b) / 60


def load_nocturne() -> tuple[pd.DataFrame, pd.DataFrame]:
    for f in NB_FILES:
        fetch(NB + f, RAW / f)
    parts = []
    for f, po in [(f, 0) for f in NB_FILES[:3]] + [(NB_FILES[3], 1)]:
        d = pd.read_csv(RAW / f, low_memory=False)
        d["playoff"] = po
        parts.append(d)
    d = pd.concat(parts, ignore_index=True)
    pg = pd.DataFrame({
        "season": d["season_year"], "game_id": d["gameId"].astype(int),
        "game_date": pd.to_datetime(d["game_date"]), "playoff": d["playoff"],
        "team_id": d["teamId"].astype(int), "team": d["teamTricode"],
        "player_id": d["personId"].astype(int), "player_name": d["personName"],
        "starter": d["position"].notna().astype(int), "pos": d["position"],
        "comment": d["comment"].fillna(""), "min": d["minutes"].map(_mins),
        "pts": d["points"], "fgm": d["fieldGoalsMade"], "fga": d["fieldGoalsAttempted"],
        "fg3m": d["threePointersMade"], "fg3a": d["threePointersAttempted"],
        "ftm": d["freeThrowsMade"], "fta": d["freeThrowsAttempted"],
        "oreb": d["reboundsOffensive"], "dreb": d["reboundsDefensive"],
        "reb": d["reboundsTotal"], "ast": d["assists"], "stl": d["steals"],
        "blk": d["blocks"], "tov": d["turnovers"], "pf": d["foulsPersonal"],
        "plus_minus": d["plusMinusPoints"],
    })
    pg["home"] = (~d["matchup"].str.contains("@")).astype(int).values
    # games from team totals
    t = pd.concat([pd.read_csv(RAW / NB_FILES[4]).assign(playoff=0),
                   pd.read_csv(RAW / NB_FILES[5]).assign(playoff=1)])
    t["home"] = ~t["MATCHUP"].str.contains("@")
    h = t[t.home].set_index("GAME_ID")
    a = t[~t.home].set_index("GAME_ID")
    g = pd.DataFrame({
        "game_id": h.index.astype(int), "season": h["SEASON_YEAR"].values,
        "game_date": pd.to_datetime(h["GAME_DATE"]).values, "playoff": h["playoff"].values,
        "home_team_id": h["TEAM_ID"].values, "home": h["TEAM_ABBREVIATION"].values,
        "home_pts": h["PTS"].values,
        "periods": 4 + ((h["MIN"].values - 48) / 5).round().clip(0),
    }).merge(pd.DataFrame({"game_id": a.index.astype(int), "away_team_id": a["TEAM_ID"].values,
                           "away": a["TEAM_ABBREVIATION"].values, "away_pts": a["PTS"].values}),
             on="game_id")
    return pg, g


def load_pbp_seasons() -> tuple[pd.DataFrame, pd.DataFrame]:
    pgs, gs = [], []
    for name, (season, po) in PBP_SEASONS.items():
        tar = RAW / f"{name}.tar.xz"
        try:
            fetch(SH + f"{name}.tar.xz", tar)
        except subprocess.CalledProcessError:
            print("not available:", name)
            continue
        d = RAW / name
        d.mkdir(exist_ok=True)
        csv = d / f"{name}.csv"
        if not csv.exists():
            subprocess.run(["tar", "-xJf", str(tar), "-C", str(d)], check=True)
        print("rebuilding box scores from play-by-play:", name)
        b, g = season_box(pd.read_csv(csv, low_memory=False))
        for x in (b, g):
            x["season"] = season
            x["playoff"] = po
            x["game_date"] = pd.to_datetime(x["game_date"])
        b["comment"] = ""
        b["pos"] = np.where(b["starter"] == 1, "S", None)
        pgs.append(b)
        gs.append(g)
    return pd.concat(pgs, ignore_index=True), pd.concat(gs, ignore_index=True)


def load_odds() -> pd.DataFrame:
    db = fetch(ODDS, RAW / "OddsData.sqlite")
    con = sqlite3.connect(db)
    tables = pd.read_sql("select name from sqlite_master where type='table'", con).name
    frames = []
    for t in tables:
        d = pd.read_sql(f'select * from "{t}"', con)
        cols = {c.lower(): c for c in d.columns}
        if not {"home", "away", "ou", "spread"} <= set(cols):
            continue
        frames.append(pd.DataFrame({
            "game_date": pd.to_datetime(d[cols["date"]], errors="coerce", format="mixed"),
            "home": d[cols["home"]].map(canonical_team), "away": d[cols["away"]].map(canonical_team),
            "close_total": pd.to_numeric(d[cols["ou"]], errors="coerce"),
            # source stores the home team's margin-of-favouritism; convert to standard home spread
            "close_spread_home": -pd.to_numeric(d[cols["spread"]], errors="coerce"),
            "ml_home": pd.to_numeric(d.get(cols.get("ml_home")), errors="coerce"),
            "ml_away": pd.to_numeric(d.get(cols.get("ml_away")), errors="coerce"),
            "src_table": t}))
    o = pd.concat(frames, ignore_index=True).dropna(subset=["game_date", "home", "away"])
    # older tables store an unsigned spread: sign it by the moneyline favourite
    fav_home = np.where(o.ml_home.notna() & o.ml_away.notna(), o.ml_home < o.ml_away, o.close_spread_home < 0)
    o["close_spread_home"] = np.where(fav_home, -1, 1) * o["close_spread_home"].abs()
    # "_new" tables supersede the older scrape for the same game
    o["pref"] = o.src_table.str.endswith("_new") | ~o.src_table.str.startswith("odds_")
    o = o.sort_values("pref").drop_duplicates(["game_date", "home", "away"], keep="last")
    return o.drop(columns="pref")


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    pg1, g1 = load_nocturne()
    pg2, g2 = load_pbp_seasons()
    cols = ["season", "game_id", "game_date", "playoff", "team_id", "team", "home", "player_id",
            "player_name", "starter", "comment", "min", "pts", "fgm", "fga", "fg3m", "fg3a",
            "ftm", "fta", "oreb", "dreb", "reb", "ast", "stl", "blk", "tov", "pf", "plus_minus"]
    pg = pd.concat([pg1[cols], pg2[cols]], ignore_index=True)
    pg["team"] = pg["team"].map(canonical_team)
    gcols = ["game_id", "season", "game_date", "playoff", "home_team_id", "home", "home_pts",
             "away_team_id", "away", "away_pts", "periods"]
    g = pd.concat([g1[gcols], g2[gcols]], ignore_index=True).drop_duplicates("game_id")
    g["home"], g["away"] = g["home"].map(canonical_team), g["away"].map(canonical_team)
    # dates for pbp-derived games come from timestamps; align player rows to game table dates
    pg = pg.drop(columns="game_date").merge(g[["game_id", "game_date"]], on="game_id")
    pg.to_parquet(OUT / "player_games.parquet", index=False)
    g.to_parquet(OUT / "games.parquet", index=False)
    o = load_odds()
    o.to_parquet(OUT / "odds.parquet", index=False)
    print(f"player rows {len(pg):,}  games {len(g):,}  odds rows {len(o):,}")
    print(g.groupby("season").size().to_string())


if __name__ == "__main__":
    main()
