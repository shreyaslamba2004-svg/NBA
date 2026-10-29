"""Is the model getting better or worse? One page, HEALTH.md, rebuilt by the nightly grading run.

For each graded US date it takes the last projection logged before each tip (players the model
had at 90%+ to play) and compares minutes and points with what happened, next to a simple
baseline: each player's average over his last 10 games. Daily rows are kept in
logs/health_daily.csv so each night only adds the new date. Bets and multis are graded from the
same logs (bets via monitor.graded_offers, multis from output/<date>/sgm.csv).
"""
from __future__ import annotations

import re
from datetime import date

import numpy as np
import pandas as pd

from . import monitor
from .sources.live import norm_name

ROOT = monitor.ROOT
LOGS = monitor.LOGS
DAILY = LOGS / "health_daily.csv"
PAGE = ROOT / "HEALTH.md"
MIN_DAYS = 5  # fewer graded dates than this in the window: too early for a verdict
SAME_BAND = 2.0  # percentage points of "better than baseline" that still count as no change
SGM_STAT = {"pts": "pts", "reb": "reb", "ast": "ast", "3pm": "fg3m", "pra": "pra", "pr": "pr", "pa": "pa",
            "ra": "ra", "stl": "stl", "blk": "blk"}


def _results(d: str) -> pd.DataFrame:
    r = pd.read_csv(LOGS / "results" / f"{d}.csv")
    for c, parts in monitor.COMBOS.items():
        r[c] = r[parts].sum(axis=1)
    r["k"] = r["player"].map(norm_name)
    return r


def _tips(d: str) -> dict:
    """Tip time per game: the first logged game snapshot is never after tip, so use ESPN."""
    from .sources import espn
    sb = espn.scoreboard(date.fromisoformat(d))
    return dict(zip(sb["game_id"], pd.to_datetime(sb["tip_utc"], utc=True)))


def _grade_sgms(d: str, r: pd.DataFrame, tips: dict) -> dict:
    f = ROOT / "output" / d / "sgm.csv"
    if not f.exists():
        return {}
    s = pd.read_csv(f)
    if s.empty:
        return {}
    games = r.drop_duplicates("game_id")
    gid = {f"{g.away} @ {g.home}": g.game_id for g in games.itertuples()}

    def leg(text, mu):
        a = re.match(r"(.+) (\w+) (over|under) ([\d.]+)$", text)
        b = re.match(r"(.+) (\d+)\+ (\w+)$", text)
        w = re.match(r"(\w+) win$", text)
        g = games[games["game_id"] == gid.get(mu)]
        if g.empty:
            return np.nan
        if w:
            g = g.iloc[0]
            return float(w.group(1) == (g.home if g.home_pts > g.away_pts else g.away))
        if a:
            name, st, side, line = a.groups()
        elif b:
            name, line, st = b.groups()
            line, side = float(line) - 0.5, "over"
        else:
            return np.nan
        x = r[(r["game_id"] == gid.get(mu)) & (r["k"] == norm_name(name))]
        if x.empty or st not in SGM_STAT:
            return np.nan  # didn't play: void
        v = x.iloc[0][SGM_STAT[st]]
        return np.nan if v == float(line) else float((v > float(line)) == (side == "over"))

    won = []
    for x in s.itertuples():
        legs = [leg(t, x.matchup) for t in str(x.legs).split(" + ")]
        won.append(np.nan if any(pd.isna(legs)) else float(all(legs)))
    s["won"] = won
    shown = s.sort_values("ev_at_multiplied_prices", ascending=False).groupby("band").head(3).dropna(subset=["won"])
    return {"sgm_n": len(shown), "sgm_won": shown["won"].sum(),
            "sgm_profit": float(np.where(shown["won"] == 1, shown["multiplied_leg_prices"] - 1, -1.0).sum()),
            "sgm_exp": shown["model_prob"].sum()}


def grade_day(d: str, pg: pd.DataFrame) -> dict | None:
    pf = LOGS / "projections" / f"{d}_players.csv"
    if not pf.exists() or not (LOGS / "results" / f"{d}.csv").exists():
        return None
    r = _results(d)
    tips = _tips(d)
    pr = pd.read_csv(pf, low_memory=False)
    pr = pr[pr["scenario"] == "base"].copy()
    pr["snap"] = pd.to_datetime(pr["snapshot_utc"].astype(str).str.split("|").str[0], utc=True)
    pr = pr[pr["game_id"].map(tips) > pr["snap"]]
    pr = pr[pr["game_id"].isin(r["game_id"])]
    pr = pr.sort_values("snap").groupby(["game_id", "player_id"]).tail(1)
    pr = pr[pr["play_prob"] >= 0.9]
    if pr.empty:
        return None
    pr["k"] = pr["player"].map(norm_name)
    m = pr.merge(r[["game_id", "k", "min", "pts"]], on=["game_id", "k"], how="left").fillna({"min": 0, "pts": 0})
    hist = pg[pd.to_datetime(pg["game_date"]) < pd.Timestamp(d)].sort_values("game_date")
    base = hist.groupby("player_id").tail(10).groupby("player_id")[["min", "pts"]].mean()
    m = m.merge(base.add_prefix("b_"), left_on="player_id", right_index=True, how="inner")
    row = {"date": d, "games": m["game_id"].nunique(), "players": len(m)}
    for s in ("min", "pts"):
        row[f"{s}_mae"] = (m[f"proj_{s}"] - m[s]).abs().mean()
        row[f"{s}_base"] = (m[f"b_{s}"] - m[s]).abs().mean()
        row[f"{s}_bias"] = (m[f"proj_{s}"] - m[s]).mean()
    row.update(_grade_sgms(d, r, tips))
    f = ROOT / "output" / d / "sanity.csv"  # the day's last sanity checks (nbamodel/sanity.py)
    if f.exists():
        try:
            fl = pd.read_csv(f)
        except pd.errors.EmptyDataError:
            fl = pd.DataFrame(columns=["check"])
        row["flags"] = len(fl)
        row["flag_kinds"] = ", ".join(f"{k} {v}" for k, v in fl["check"].value_counts().items()) or "none"
    return row


def _backtest_gain() -> dict:
    """Improvement over the baseline in the held-out backtest, from output/backtest_report.md."""
    out = {}
    try:
        for line in (ROOT / "output" / "backtest_report.md").read_text().splitlines():
            m = re.match(r"\| (minutes|pts) \| [\d.]+ \| [\d.]+ \| (-?[\d.]+)% \|", line)
            if m:
                out["min" if m.group(1) == "minutes" else "pts"] = float(m.group(2))
    except OSError:
        pass
    return out


def _window(df: pd.DataFrame, days: int, today: date) -> pd.DataFrame:
    return df[pd.to_datetime(df["date"]) > pd.Timestamp(today) - pd.Timedelta(days=days)]


def _gain(w: pd.DataFrame, s: str) -> float:
    """% better than the last-10 baseline, weighted by players graded."""
    if w.empty:
        return np.nan
    mae = np.average(w[f"{s}_mae"], weights=w["players"])
    base = np.average(w[f"{s}_base"], weights=w["players"])
    return 100 * (1 - mae / base)


def verdict(df: pd.DataFrame, today: date) -> tuple[str, str]:
    w7, w30 = _window(df, 7, today), _window(df, 30, today)
    if len(w30) < MIN_DAYS:
        return "TOO EARLY", f"Only {len(w30)} graded game day(s) so far; a verdict needs {MIN_DAYS}."
    g7, g30 = _gain(w7, "pts"), _gain(w30, "pts")
    if g30 < 0:
        return "WORSE", (f"Over 30 days the points projections are {abs(g30):.1f}% *worse* than a simple "
                         "last-10-game average. Something is off: check the alerts and recent changes.")
    if len(w7) < 3:
        return "SAME", "Not enough games in the last week to compare with the month (break in the schedule)."
    diff = g7 - g30
    if diff > SAME_BAND:
        return "BETTER", f"Last 7 days beat the baseline by {g7:.1f}% vs {g30:.1f}% over 30 days."
    if diff < -SAME_BAND:
        return "WORSE", (f"Last 7 days beat the baseline by only {g7:.1f}% vs {g30:.1f}% over 30 days. "
                         "One bad week happens; two in a row is worth a look.")
    return "SAME", f"Last 7 days {g7:.1f}% better than baseline, 30 days {g30:.1f}%: steady."


def build(today: date | None = None) -> str:
    today = today or date.today()
    from .dataset import load_history
    done = pd.read_csv(DAILY) if DAILY.exists() else pd.DataFrame(columns=["date"])
    days = sorted(f.stem for f in (LOGS / "results").glob("*.csv"))
    todo = [d for d in days if d not in set(done["date"].astype(str))]
    if todo:
        pg, _ = load_history()
        rows = [x for x in (grade_day(d, pg) for d in todo) if x]
        if rows:
            done = pd.concat([done, pd.DataFrame(rows)], ignore_index=True).sort_values("date")
            DAILY.parent.mkdir(parents=True, exist_ok=True)
            done.to_csv(DAILY, index=False)
    df = done
    bt = _backtest_gain()
    v, why = verdict(df, today) if len(df) else ("TOO EARLY", "No graded game days yet.")
    md = ["# Model health",
          f"Rebuilt {today.isoformat()} by the nightly grading run. Back to [TODAY.md](TODAY.md).",
          f"## Verdict: **{v}**", why,
          "How to read this: the model is judged against a simple rule anyone could use, each player's "
          "average over his last 10 games. \"% better\" is how much smaller the model's average miss is. "
          "Watch the trend, not single days: one game day is mostly noise.",
          "## Projection accuracy (players the model had at 90%+ to play)"]
    rows = []
    for label, days_ in (("Last 7 days", 7), ("Last 30 days", 30), ("Season", 400)):
        w = _window(df, days_, today) if len(df) else df
        if w.empty:
            continue
        r = {"window": label, "game days": len(w), "players": int(w["players"].sum())}
        for s, name in (("min", "minutes"), ("pts", "points")):
            r[f"{name} miss"] = round(float(np.average(w[f"{s}_mae"], weights=w["players"])), 2)
            r[f"{name} % better than last-10"] = round(_gain(w, s), 1)
            r[f"{name} lean (+ = too high)"] = round(float(np.average(w[f"{s}_bias"], weights=w["players"])), 2)
        rows.append(r)
    if bt:
        rows.append({"window": "Backtest (held-out 2025-26)", "minutes % better than last-10": bt.get("min"),
                     "points % better than last-10": bt.get("pts")})
    md.append(pd.DataFrame(rows).astype(object).where(pd.DataFrame(rows).notna(), "").to_markdown(index=False)
              if rows else "_Nothing graded yet._")
    md.append("Live should sit near the backtest line. Well below it for weeks means the model is doing "
              "worse on new games than it did in testing (overfitting or something broke).")
    # bets
    md.append("## Best bets (EV ≥ 5%, odds ≤ 4)")
    md.append("Every bet that showed in TODAY.md's main best-bets table at any point in the day, graded at the "
              "first price it showed at (the sheet changes through the day, so this is more than the final "
              "pre-tip list).")
    try:
        g = monitor.graded_offers()
        bb = g.dropna(subset=["taken_price"]) if len(g) else g
        if len(bb):  # what the sheet's main table lists: no news flags, offered, one row per bet (best price)
            bb = bb[(bb["check_news"].astype(str).str.lower() != "true")
                    & (bb["depends_on"].fillna("").astype(str) == "")
                    & (bb["offered"].astype(str).str.lower() != "false")]
            bb = (bb.sort_values("taken_price", ascending=False)
                  .drop_duplicates(["game_id", "market", "selection", "player", "line"]))
    except Exception as e:  # never let grading of bets block the page
        print("bet grading failed:", e)
        bb = pd.DataFrame()
    if len(bb):
        bb = bb.assign(day=pd.to_datetime(bb["snap"].str[:10]),
                       profit=np.where(bb["won"] == 1, bb["taken_price"] - 1, -1.0),
                       clv=bb["market_novig_prob"] * bb["taken_price"] - 1)
        rows = []
        for label, dd in (("Last 7 days", 7), ("Last 30 days", 30), ("Season", 400)):
            x = bb[bb["day"] > pd.Timestamp(today) - pd.Timedelta(days=dd)]
            if len(x):
                rows.append({"window": label, "bets": len(x), "won": int(x["won"].sum()),
                             "profit (units)": round(float(x["profit"].sum()), 2),
                             "ROI %": round(100 * float(x["profit"].mean()), 1),
                             "avg CLV %": round(100 * float(x["clv"].mean()), 1),
                             "beat closing %": round(100 * float((x["clv"] > 0).mean()), 1)})
        md.append(pd.DataFrame(rows).to_markdown(index=False))
        md.append("CLV (closing-line value) compares the price taken with the final no-vig market price before tip. "
                  "Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings "
                  "for months.")
    else:
        md.append("_No graded best bets yet._")
    # multis
    md.append("## Multis (top 3 per price band)")
    if "sgm_n" in df and df["sgm_n"].fillna(0).sum() > 0:
        rows = []
        for label, dd in (("Last 7 days", 7), ("Last 30 days", 30), ("Season", 400)):
            x = _window(df, dd, today).fillna({"sgm_n": 0})
            if x["sgm_n"].sum():
                rows.append({"window": label, "multis": int(x["sgm_n"].sum()), "won": int(x["sgm_won"].sum()),
                             "model expected to win": round(float(x["sgm_exp"].sum()), 1),
                             "profit (units, at multiplied leg prices)": round(float(x["sgm_profit"].sum()), 2)})
        md.append(pd.DataFrame(rows).to_markdown(index=False))
        md.append("If \"won\" keeps landing near \"expected\", the multi probabilities are honest. Profit uses "
                  "the legs' prices multiplied together; the bookie's actual SGM price is usually lower.")
    else:
        md.append("_No graded multis yet._")
    # daily detail
    if len(df):
        d = df.sort_values("date", ascending=False).head(30)
        tab = pd.DataFrame({"date": d["date"], "games": d["games"].astype(int), "players": d["players"].astype(int),
                            "minutes miss (model / last-10)": [f"{a:.2f} / {b:.2f}" for a, b in zip(d["min_mae"], d["min_base"])],
                            "points miss (model / last-10)": [f"{a:.2f} / {b:.2f}" for a, b in zip(d["pts_mae"], d["pts_base"])],
                            "points lean": d["pts_bias"].round(2)})
        if "flags" in d:
            tab["sanity flags"] = [("" if pd.isna(n) else f"{int(n)} ({k})") for n, k in zip(d["flags"], d.get("flag_kinds", ""))]
        md += ["## Day by day (last 30)",
               "Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising "
               "count means something in the inputs is going wrong.", tab.to_markdown(index=False)]
    text = "\n\n".join(md) + "\n"
    PAGE.write_text(text)
    return text
