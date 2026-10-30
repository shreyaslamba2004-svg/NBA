"""Automatic sanity checks on every projection run, so odd numbers are flagged instead of found by eye.

Per game (confirmed-player projections):
  team minutes   a team's expected minutes far from a normal game (the model no longer forces 240,
                 so a big gap means the roster or play chances look wrong)
  player minutes a regular projected well above anything he's played lately, or well below his usual
                 (his last 10 games this season for his current team)
  team points    projected team score far from what the betting market implies
  player points  projected points far from DraftKings' main line
Writes output/<date>/sanity.csv; TODAY.md lists the flags and HEALTH.md counts them per day.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

TEAM_MIN = (210.0, 270.0)  # normal range for a team's expected minutes (live-like backtest: 10th-90th pct 220-260)
ABOVE_MAX = 4.0            # minutes above his most in the last 10 games
BELOW_AVG = 8.0            # minutes below his last-10 average (regulars only)
TEAM_PTS_GAP = 8.0         # points from the market-implied team score
PLAYER_PTS_GAP = (5.0, 0.25)  # points from DraftKings' main line: at least 5 and 25% of the line


COLS = ["game_id", "matchup", "check", "detail", "why"]


class _Context:
    """What usually explains an unusual projection: this season's form for his current team, last
    season's, teammates who are out, a new team, a minutes limit, and roster turnover."""

    def __init__(self, pg: pd.DataFrame, avail: pd.DataFrame | None):
        played = pg[pg["min"].fillna(0) > 0]
        self.season = pg["season"].max()
        seasons = sorted(pg["season"].dropna().unique())
        self.last = seasons[-2] if len(seasons) > 1 else None
        self.cur = played[played["season"] == self.season]
        reg = played[(played["season"] == self.last) & (played.get("playoff", 0) == 0)] if self.last else played.iloc[:0]
        self.prev = reg.groupby("player_id").agg(pts=("pts", "sum"), min=("min", "sum"), gp=("min", "size"),
                                                 team=("team", "last"))
        self.avail = avail if avail is not None else pd.DataFrame(columns=["team", "player_id", "player_name",
                                                                           "play_prob", "min_cap", "status"])

    def outs(self, team: str) -> tuple[list[str], float]:
        """Regulars ruled out tonight (10+ minutes a game this season or last) and their minutes."""
        a = self.avail[(self.avail["team"] == team) & (self.avail["play_prob"] == 0)]
        cur = self.cur[self.cur["team"] == team].groupby("player_id")["min"].mean()
        names, mins = [], 0.0
        for r in a.itertuples():
            m = cur.get(r.player_id, np.nan)
            if np.isnan(m) and r.player_id in self.prev.index:
                pv = self.prev.loc[r.player_id]
                m = pv["min"] / pv["gp"] if pv["team"] == team else np.nan
            if not np.isnan(m) and m >= 10:
                names.append(str(r.player_name).split()[-1])
                mins += m
        return names, mins

    def player(self, r, team: str, proj_pts: float | None = None) -> str:
        bits = []
        me = self.cur[(self.cur["player_id"] == r.player_id) & (self.cur["team"] == team)]
        pv = self.prev.loc[r.player_id] if r.player_id in self.prev.index else None
        if len(me) < 3:
            bits.append(f"only {len(me)} game(s) for {team} this season, so it leans on older form")
        else:
            bits.append(f"minutes {r.proj_min:.0f} vs {me['min'].mean():.0f} this season")
        if pv is not None and pv["team"] != team:
            bits.append(f"new team (was {pv['team']} last season)")
        if proj_pts is not None and r.proj_min > 0:
            rate = proj_pts / r.proj_min
            txt = f"scoring {rate:.2f}/min"
            if len(me) >= 3:
                txt += f" vs {me['pts'].sum() / me['min'].sum():.2f} this season"
            if pv is not None and pv["min"] > 0:
                txt += f", {pv['pts'] / pv['min']:.2f} last season"
            bits.append(txt)
        names, mins = self.outs(team)
        if names:
            bits.append(f"teammates out: {', '.join(names[:4])} (~{mins:.0f} min a game)")
        cap = self.avail.loc[(self.avail["player_id"] == r.player_id), "min_cap"]
        if len(cap) and pd.notna(cap.iloc[0]):
            bits.append(f"minutes limit in the news (~{cap.iloc[0]:.0f})")
        return "; ".join(bits)

    def team(self, team: str, proj_min: pd.Series) -> str:
        """proj_min: tonight's expected minutes per player_id for this team."""
        bits = []
        gp = self.cur[self.cur["team"] == team]["game_id"].nunique()
        new = [pid for pid in proj_min.index if pid in self.prev.index and self.prev.loc[pid, "team"] != team
               or pid not in self.prev.index]
        share = proj_min.reindex(new).sum() / max(proj_min.sum(), 1)
        if share >= 0.3:
            bits.append(f"{share:.0%} of tonight's minutes go to players new to {team} since last season, "
                        "and the team ratings still lean on last season")
        if gp < 8:
            bits.append(f"{team} have played {gp} games this season")
        names, mins = self.outs(team)
        if names:
            bits.append(f"{team} out: {', '.join(names[:4])}")
        return "; ".join(bits) or "no obvious cause: worth a manual look"


def check(res: dict, pg: pd.DataFrame) -> pd.DataFrame:
    rows = []
    ps, gs, ed = res.get("players", pd.DataFrame()), res.get("games", pd.DataFrame()), res.get("edges", pd.DataFrame())
    if ps is None or ps.empty:
        return pd.DataFrame(columns=COLS)
    p = ps[ps["scenario"] == "base"].copy()
    mu = p.groupby("game_id")["matchup"].first()
    cx = _Context(pg, res.get("availability"))

    def flag(gid, kind, detail, why=""):
        rows.append({"game_id": gid, "matchup": mu.get(gid, ""), "check": kind, "detail": detail, "why": why})

    # team minutes
    tm = (p["proj_min"] * p["play_prob"]).groupby([p["game_id"], p["team"]]).sum()
    for (gid, team), v in tm.items():
        if not TEAM_MIN[0] <= v <= TEAM_MIN[1]:
            t = p[(p["game_id"] == gid) & (p["team"] == team)]
            flag(gid, "team minutes", f"{team} players add up to {v:.0f} expected minutes (normal is about 240)",
                 cx.team(team, (t["proj_min"] * t["play_prob"]).set_axis(t["player_id"])))
    # player minutes vs his last 10 games this season for his current team (last season's playoff
    # minutes or an old team's role aren't a fair comparison, e.g. a player traded into a smaller role)
    hist = pg[(pg["min"].fillna(0) > 0) & (pg["season"] == pg["season"].max())].sort_values("game_date")
    hist = hist.merge(p[["player_id", "team"]].drop_duplicates("player_id"), on=["player_id", "team"])
    rec = hist.groupby("player_id").tail(10).groupby("player_id")["min"].agg(["max", "mean", "size"])
    p = p.join(rec, on="player_id")
    hi = p[(p["size"] >= 3) & (p["proj_min"] >= 28) & (p["proj_min"] > p["max"] + ABOVE_MAX)]
    for r in hi.itertuples():
        flag(r.game_id, "player minutes", f"{r.player} projected {r.proj_min:.0f} min; most in his last 10 games is {r.max:.0f}",
             cx.player(r, r.team))
    lo = p[(p["size"] >= 4) & (p["mean"] >= 24) & (p["play_prob"] >= 0.9) & (p["proj_min"] < p["mean"] - BELOW_AVG)]
    for r in lo.itertuples():
        flag(r.game_id, "player minutes", f"{r.player} projected {r.proj_min:.0f} min; he's averaged {r.mean:.0f} in his last 10",
             cx.player(r, r.team))
    # team points vs market
    g = gs[gs["scenario"] == "base"] if "scenario" in gs else gs
    for r in g.itertuples():
        t, s = getattr(r, "market_total", np.nan), getattr(r, "market_spread_home", np.nan)
        if pd.isna(t) or pd.isna(s):
            continue
        for team, proj, implied in ((r.home, r.proj_home_pts, (t - s) / 2), (r.away, r.proj_away_pts, (t + s) / 2)):
            if abs(proj - implied) > TEAM_PTS_GAP:
                t = p[(p["game_id"] == r.game_id) & (p["team"] == team)]
                opp = r.away if team == r.home else r.home
                why = cx.team(team, (t["proj_min"] * t["play_prob"]).set_axis(t["player_id"]))
                t2 = p[(p["game_id"] == r.game_id) & (p["team"] == opp)]
                why2 = cx.team(opp, (t2["proj_min"] * t2["play_prob"]).set_axis(t2["player_id"]))
                if not why2.startswith("no obvious"):
                    why = why + " | " + why2 if not why.startswith("no obvious") else why2
                flag(r.game_id, "team points", f"{team} projected {proj:.0f}, market implies {implied:.0f}", why)
    # player points vs DraftKings main line
    if ed is not None and len(ed) and "main_line" in ed:
        dk = ed[(ed["market"] == "prop_pts") & (ed["book"].astype(str).str.lower() == "draftkings")
                & (ed["main_line"].astype(str).str.lower() == "true")]
        dk = dk.drop_duplicates(["game_id", "player_id"])
        dk = dk.merge(p[["game_id", "player_id", "team", "proj_pts", "proj_min"]],
                      on=["game_id", "player_id"], how="inner")
        gap = (dk["proj_pts"] - dk["line"].astype(float)).abs()
        big = dk[gap >= np.maximum(PLAYER_PTS_GAP[0], PLAYER_PTS_GAP[1] * dk["line"].astype(float))]
        for r in big.itertuples():
            flag(r.game_id, "player points", f"{r.player} projected {r.proj_pts:.1f} pts vs DraftKings line {r.line:g}",
                 cx.player(r, r.team, r.proj_pts))
    return pd.DataFrame(rows, columns=COLS)


def section(df: pd.DataFrame, limit: int = 20) -> str:
    """Markdown for TODAY.md."""
    if df is None or df.empty:
        return "All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, " \
               "player points vs DraftKings)."
    head = (f"{len(df)} flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), "
            "but check them before betting on the players or games listed.")
    why = df["why"] if "why" in df else pd.Series("", index=df.index)
    rows = ["| Game | Check | Detail | Likely reason |", "|---|---|---|---|"] + \
           [f"| {r.matchup} | {r.check} | {r.detail} | {w if isinstance(w, str) else ''} |"
            for r, w in zip(df.head(limit).itertuples(), why.head(limit))]
    more = f"\n\n_+{len(df) - limit} more in the sanity.csv file._" if len(df) > limit else ""
    return head + "\n\n" + "\n".join(rows) + more
