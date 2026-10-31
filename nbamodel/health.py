"""Is the model getting better or worse? One page, HEALTH.md, rebuilt by the nightly grading run.

For each graded US date it takes the last projection logged before each tip (players the model
had at 90%+ to play) and compares minutes and points with what happened, next to a simple
baseline: each player's average over his last 10 games. Daily rows are kept in
logs/health_daily.csv so each night only adds the new date. Bets are graded from the
same logs via monitor.graded_offers.
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


def grade_day(d: str, pg: pd.DataFrame) -> dict | None:
    from .market_log import log_file
    pf = log_file(LOGS / "projections" / f"{d}_players.csv")
    if pf is None or not (LOGS / "results" / f"{d}.csv").exists():
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
    md.append("**Main record: the final list.** The bets still in TODAY.md's best-bets table on the last update "
              "before each game's tip (after lineups and injury news), graded at the price shown then.")
    try:
        g = monitor.graded_offers()
    except Exception as e:  # never let grading of bets block the page
        print("bet grading failed:", e)
        g = pd.DataFrame()

    def sheet(x, price_col):  # what the sheet's main table lists: no news flags, offered, one row per bet (best price)
        x = x[(x["check_news"].astype(str).str.lower() != "true")
              & (x["depends_on"].fillna("").astype(str) == "")
              & (x["offered"].astype(str).str.lower() != "false")]
        return (x.sort_values(price_col, ascending=False)
                .drop_duplicates(["game_id", "market", "selection", "player", "line"]))

    def top(x):  # TODAY.md lists at most TOP_BETS per table
        from .dashboard import TOP_BETS
        return (x.assign(_d=x["_file"].astype(str).str[:10]).sort_values("ev_blend", ascending=False)
                .groupby("_d").head(TOP_BETS))

    def stake(x):  # the sheet's suggested stake, % of bankroll (quarter-Kelly, capped)
        from .dashboard import MAX_STAKE_PCT
        return (100 * x["kelly_25"].astype(float)).clip(0, MAX_STAKE_PCT).fillna(0)

    def record(x, price_col, clv=True):
        x = x.assign(day=pd.to_datetime(x["snap"].str[:10]),
                     staked=stake(x),
                     profit=np.where(x["won"] == 1, x[price_col] - 1, -1.0),
                     clv=x["market_novig_prob"] * x[price_col] - 1)
        rows, seen = [], None
        for label, dd in (("Last 7 days", 7), ("Last 30 days", 30), ("Whole season", 400)):
            w = x[x["day"] > pd.Timestamp(today) - pd.Timedelta(days=dd)]
            if len(w) and len(w) != seen:  # a longer window with the same bets would just repeat the row
                seen = len(w)
                r = {"period": label, "bets": len(w), "won": int(w["won"].sum()),
                     "profit (units)": round(float(w["profit"].sum()), 2),
                     "ROI % (flat)": round(100 * float(w["profit"].mean()), 1),
                     "staked (% bankroll)": round(float(w["staked"].sum()), 1),
                     "profit at sheet stakes (% bankroll)": round(float((w["staked"] * w["profit"]).sum()), 2),
                     "ROI % (sheet stakes)": round(100 * float((w["staked"] * w["profit"]).sum())
                                                   / max(float(w["staked"].sum()), 1e-9), 1)}
                if clv:
                    r.update({"avg CLV %": round(100 * float(w["clv"].mean()), 1),
                              "beat closing %": round(100 * float((w["clv"] > 0).mean()), 1)})
                rows.append(r)
        if len(rows) == 1:
            rows[0]["period"] = f"Since {x['day'].min():%d %b}"
        return pd.DataFrame(rows).to_markdown(index=False)

    def bet_list(x, title, price_col="price_decimal"):  # every graded bet, newest first, to check totals by hand
        from .dashboard import MAX_STAKE_PCT, _bet_label, _stake
        x = x.assign(date=x["_file"].astype(str).str[:10]).sort_values(["date", "ev_blend"], ascending=[False, False])
        rows = [{"date (US)": r["date"], "bet": _bet_label(r), "game": r["matchup"], "book": r["book"],
                 "odds": round(float(r[price_col]), 2), "EV": f"{100 * float(r['ev_blend']):+.1f}%",
                 "sheet stake": _stake(r["kelly_25"]), "result": "won" if r["won"] == 1 else "lost",
                 "units (1 flat)": round(float(r[price_col]) - 1 if r["won"] == 1 else -1.0, 2),
                 "profit at stake (% bankroll)": round(min(MAX_STAKE_PCT, max(0.0, 100 * float(r["kelly_25"] or 0)))
                                                       * (float(r[price_col]) - 1 if r["won"] == 1 else -1.0), 2)}
                for _, r in x.head(100).iterrows()]
        return (f"<details><summary>{title} ({len(x)})</summary>\n\n"
                + pd.DataFrame(rows).to_markdown(index=False) + "\n\n</details>")

    md.append("Each table shows two ways of counting: units at a flat 1-unit stake on every bet (so results "
              "compare cleanly), and profit at the sheet's suggested stake, the quarter-Kelly % of bankroll capped "
              "at 2% that TODAY.md shows on every bet. ROI (sheet stakes) is that profit divided by the total staked. "
              "Rows are the last 7 days, last 30 days and whole season; a longer period only gets its own row once "
              "it holds more bets than the shorter one.")
    fin = top(sheet(g[(g["ev_blend"] >= monitor.BEST_EV) & (g["price_decimal"] <= monitor.BEST_MAX_ODDS)],
                    "price_decimal")) if len(g) else g
    md.append(record(fin, "price_decimal", clv=False) + "\n\n" + bet_list(fin, "Every final-list bet")
              if len(fin) else "_No graded final-list bets yet._")
    md.append(f"## Long shots (EV ≥ 5%, odds above {monitor.BEST_MAX_ODDS:g})")
    md.append("TODAY.md's long-shot table, graded the same way: the final pre-tip list at the price shown then, "
              "1 unit flat. Expect long losing runs; judge it over hundreds of bets.")
    lng = top(sheet(g[(g["ev_blend"] >= monitor.BEST_EV) & (g["price_decimal"] > monitor.BEST_MAX_ODDS)],
                    "price_decimal")) if len(g) else g
    md.append(record(lng, "price_decimal", clv=False) + "\n\n" + bet_list(lng, "Every long shot")
              if len(lng) else "_No graded long shots yet._")
    md.append("## Best bets: any time in the day (secondary)")
    md.append("**Any time in the day.** Every bet that showed in the table at any point, graded at "
              "the first price it showed at. Bets that dropped off before tip (news, price moves) count here.")
    anyt = (g.dropna(subset=["taken_price"]).sort_values("taken_price", ascending=False)  # flags checked when shown
            .drop_duplicates(["game_id", "market", "selection", "player", "line"])) if len(g) else g
    if len(anyt):
        md.append(record(anyt, "taken_price") + "\n\n" +
                  bet_list(anyt, "Every bet that showed at any time (odds = first price shown)", "taken_price"))
        md.append("CLV (closing-line value) compares the price taken with the final no-vig market price before tip. "
                  "Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings "
                  "for months.")
    else:
        md.append("_No graded best bets yet._")
    md.append("## Best player props per game (main lines)")
    md.append("The \"Best player props\" box in each game's section of TODAY.md: every main-line prop "
              "with positive EV, no news flag and offered at Sportsbet, as listed on the last update before tip, "
              "graded at the price shown then. These include edges under 5%, so expect a thinner margin than "
              "best bets.")
    pp = pd.DataFrame()
    if len(g):
        pp = g[g["market"].astype(str).str.startswith("prop_")].copy()
        main = pp["main_line"].astype(str).str.lower() if "main_line" in pp else pd.Series("nan", index=pp.index)
        old = ~main.isin(["true", "false"])  # logs before main_line existed: the line priced closest to even
        if old.any():
            o = pp[old].assign(even=(pp.loc[old, "book_novig_prob"].astype(float) - 0.5).abs())
            keep = o.sort_values("even").drop_duplicates(["game_id", "player", "market", "book"]).index
            main[old] = "false"
            main[keep] = "true"
        pp = pp[(main == "true") & (pp["ev_blend"] > 0) & (pp["price_decimal"] <= monitor.BEST_MAX_ODDS)]
        pp = sheet(pp, "price_decimal")
    md.append(record(pp, "price_decimal", clv=False) + "\n\n" + bet_list(pp, "Every graded game prop")
              if len(pp) else "_No graded game props yet._")
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
