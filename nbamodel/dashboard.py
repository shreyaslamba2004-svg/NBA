"""Daily betting sheet as Markdown, rebuilt after every run.

Reads output/<date>/*.csv and writes TODAY.md at the repo root (plus output/<date>/today.md as
an archive). GitHub renders it as tables on the web and in its mobile app. No API keys: only
the CSVs the pipeline already writes.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
TODAY = ROOT / "TODAY.md"

MIN_EV = 0.05          # best-bets threshold
MAX_STAKE_PCT = 2.0    # cap on quarter-Kelly stake, % of bankroll
TOP_BETS = 25
MAX_ODDS = 4.0         # best bets only up to this decimal price
STATS = [("pts", "PTS"), ("reb", "REB"), ("ast", "AST"), ("fg3m", "3PM"), ("stl", "STL"), ("blk", "BLK"),
         ("tov", "TOV"), ("pra", "PRA")]


def _c(x) -> str:
    """Table-safe cell text."""
    return "" if x is None or (isinstance(x, float) and pd.isna(x)) else str(x).replace("|", "/")


def _f(x, nd=2, pct=False, sign=False) -> str:
    if x is None or pd.isna(x):
        return "–"
    v = float(x) * (100 if pct else 1)
    s = f"{v:+.{nd}f}" if sign else f"{v:.{nd}f}"
    return s + ("%" if pct else "")


def _table(head: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] + ["--:"] * (len(head) - 1)) + "|"]
    out += ["| " + " | ".join(_c(x) for x in r) + " |" for r in rows]
    return "\n".join(out)


def _read(d: Path, name: str) -> pd.DataFrame:
    p = d / f"{name}.csv"
    try:
        return pd.read_csv(p) if p.exists() else pd.DataFrame()
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _bet_label(r) -> str:
    m, sel, line = r["market"], str(r["selection"]), r["line"]
    if m == "moneyline":
        return f"{sel} to win"
    if m == "spread":
        return f"{sel} {float(line):+g}"
    if m == "total":
        return f"Total {sel} {line}"
    if m == "team_total":
        return f"{sel} {line}"
    stat = m.replace("prop_", "").upper().replace("FG3M", "3PM")
    plus = f" ({float(line) + 0.5:g}+)" if sel == "over" and float(line) % 1 == 0.5 else ""  # Sportsbet's milestone name
    return f"{r.get('player', '')} {stat} {sel} {line}{plus}"


def _stake(k) -> str:
    return "–" if pd.isna(k) else f"{min(MAX_STAKE_PCT, max(0.0, 100 * float(k))):.1f}%"


def _bets_table(df: pd.DataFrame) -> str:
    rows = [[_bet_label(r), r["matchup"], r["book"], _f(r["price_decimal"]),
             _f(1 / float(r["blend_prob"]) if float(r["blend_prob"] or 0) > 0 else None), _f(r["fair_decimal"]),
             _f(r["model_prob"], 1, pct=True), _f(r["market_novig_prob"], 1, pct=True),
             _f(r["blend_prob"], 1, pct=True), _f(r["ev_blend"], 1, pct=True, sign=True),
             _f(r["ev"], 1, pct=True, sign=True), _stake(r["kelly_25"])] for _, r in df.iterrows()]
    return _table(["Bet", "Game", "Book", "Odds", "Min odds", "Fair (model)", "Model", "No-vig mkt", "Blend", "EV", "EV model only",
                   "Stake"], rows)


def best_bets(edges: pd.DataFrame, longshots: bool | None = False, offered: bool = True) -> tuple[str, str, str]:
    """(best bets, wait-for-news, check-news) tables; longshots=True does the same for odds above MAX_ODDS
    (None: any odds), offered=False for bets the bookie doesn't list."""
    if edges.empty:
        return "_No market prices were available for this run._", "", ""
    e = edges.copy()
    if "offered" in e:  # only what the bookie lists (bookie_markets.json)
        e = e[(e["offered"].astype(str).str.lower() != "false") == offered]
    e["check_news"] = e["check_news"].astype(str).str.lower() == "true"
    dep = e.get("depends_on", pd.Series("", index=e.index)).fillna("").astype(str)
    e["depends_on"] = dep
    # long shots excluded until the stat-distribution tails are validated in backtests
    in_band = (e["price_decimal"] > 0 if longshots is None else
               e["price_decimal"] > MAX_ODDS if longshots else e["price_decimal"] <= MAX_ODDS)
    good = e[(e["ev_blend"] >= MIN_EV) & in_band].sort_values("ev_blend", ascending=False)
    good = good.drop_duplicates(["matchup", "market", "selection", "line", "player"])  # best price per bet
    waiting = good[good["depends_on"] != ""].head(TOP_BETS)
    rest = good[good["depends_on"] == ""]
    clean, flagged = rest[~rest["check_news"]].head(TOP_BETS), rest[rest["check_news"]].head(TOP_BETS)
    main = _bets_table(clean) if len(clean) else "_No bets clear the edge threshold right now._"
    wait = ""
    if len(waiting):
        rows = [[_bet_label(r), r["matchup"], r["book"], _f(r["price_decimal"]), r["depends_on"],
                 "void" if r["depends_on"] == r.get("player") else _f(r["p_if_out"], 1, pct=True),
                 _f(r["p_if_in"], 1, pct=True),
                 _f(r["ev_blend"], 1, pct=True, sign=True)] for _, r in waiting.iterrows()]
        wait = _table(["Bet", "Game", "Book", "Odds", "Wait for news on", "Model if he sits", "Model if he plays",
                       "EV now (blended odds he plays)"], rows)
    return main, wait, (_bets_table(flagged) if len(flagged) else "")


def _game_extras(gid, ed: pd.DataFrame) -> str:
    """Best single props for one game."""
    out = []
    if len(ed):
        e = ed[(ed["game_id"] == gid) & ed["market"].astype(str).str.startswith("prop_") &
               (ed["price_decimal"] <= MAX_ODDS) & (ed["ev_blend"] > 0)]
        if "depends_on" in e:
            e = e[e["depends_on"].fillna("").astype(str) == ""]
        if "check_news" in e:
            e = e[e["check_news"].astype(str).str.lower() != "true"]
        if "offered" in e:
            e = e[e["offered"].astype(str).str.lower() != "false"]
        if "main_line" in e:  # each player's actual line, not alt/milestone lines
            e = e[e["main_line"].astype(str).str.lower() == "true"]
        e = e.sort_values("ev_blend", ascending=False).drop_duplicates(["player", "market", "selection", "line"])
        if len(e):
            out.append("**Best player props (main lines)**\n\n" + _bets_table(e))
    return "\n\n".join(out)


LINES: dict = {}  # (player_id, stat, book) -> main line, set by build()
LINE_STATS = {"pts": "DK · SB", "reb": "DK", "ast": "DK", "fg3m": "DK"}  # Sportsbet is only bought for points


def _book_lines(pid, stat) -> str:
    dk, sb = LINES.get((pid, stat, "draftkings")), LINES.get((pid, stat, "sportsbet"))
    if stat != "pts":
        return "" if dk is None else f"{dk:g}"
    if dk is None and sb is None:
        return ""
    return f"{'–' if dk is None else f'{dk:g}'} · {'–' if sb is None else f'{sb:g}'}"


LAST5: dict = {}  # (player_id, stat) -> "31,33,29,-,40", oldest to newest, set by build()
LAST5_STATS = ("min", "pts", "reb", "ast", "fg3m")


def _last5(day: date) -> dict:
    """Each player's last 5 team games before `day`; "-" where he didn't play."""
    from .pipeline import load_history
    pg, _ = load_history()
    pg = pg[pg["game_date"] < pd.Timestamp(day)]
    pg = pg[pg["season"] == pg["season"].max()]
    cur = pg.sort_values("game_date").drop_duplicates("player_id", keep="last")[["player_id", "team"]]
    games = (pg.drop_duplicates(["team", "game_id"]).sort_values("game_date")
             .groupby("team")["game_id"].apply(lambda x: list(x)[-5:]).to_dict())
    rows = pg.set_index(["player_id", "game_id"])
    out = {}
    for pid, team in cur.itertuples(index=False):
        mine = rows.loc[pid] if pid in rows.index.get_level_values(0) else None
        for s in LAST5_STATS:
            vals = []
            for gid in games.get(team, []):
                v = mine[s].get(gid) if mine is not None and gid in mine.index else None
                played = v is not None and pd.notna(v) and pd.notna(mine["min"].get(gid)) and mine["min"].get(gid) > 0
                vals.append(f"{float(v):.0f}" if played else "-")
            out[(pid, s)] = ",".join(vals)
    return out


def _with5(proj: str, pid, s) -> str:
    l5 = LAST5.get((pid, s))
    return f"{proj}<br><sub>{l5}</sub>" if l5 else proj


def _player_table(ps: pd.DataFrame, team: str | None = None, show_team: bool = False) -> str:
    t = ps if team is None else ps[ps["team"] == team]
    t = t[t["play_prob"] > 0].sort_values(["team", "proj_min"] if show_team else "proj_min",
                                          ascending=[True, False] if show_team else False)
    rows = []
    for _, r in t.iterrows():
        name = r["player"] + (f" ({r['team']})" if show_team else "")
        cells = []
        for s, _ in STATS:  # bookies' main line right after each projection that has one
            v = _f(r.get(f"proj_{s}"), 1)
            cells.append(_with5(v, r["player_id"], s) if s in LAST5_STATS else v)
            if s in LINE_STATS:
                cells.append(_book_lines(r["player_id"], s))
        rows.append([name, f"{int(round(100 * r['play_prob']))}%",
                     _with5(_f(r["proj_min"], 1), r["player_id"], "min")] + cells)
    heads = []
    for s, lab in STATS:
        heads.append(lab)
        if s in LINE_STATS:
            heads.append(f"{lab} line {LINE_STATS[s]}")
    return _table(["Player", "Plays", "Min"] + heads, rows)


def _line_cells(r) -> list:
    h, a = r["home"], r["away"]
    mkt = []
    if pd.notna(r.get("market_spread_home")):
        mkt.append(f"{h} {float(r['market_spread_home']):+g} covers {_f(r.get('p_home_cover'), 0, pct=True)}")
    if pd.notna(r.get("market_total")):
        mkt.append(f"o{r['market_total']:g} {_f(r.get('p_over'), 0, pct=True)}")
    return [f"{_f(r['proj_away_pts'], 1)}–{_f(r['proj_home_pts'], 1)}", f"{a} {_f(r['away_win_prob'], 0, pct=True)}",
            f"{_f(r['fair_dec_away'])} / {_f(r['fair_dec_home'])}", f"{h} {float(r['fair_spread_home']):+g}",
            r["fair_total"], "; ".join(mkt)]


LINE_HEAD = ["Score", "Away win", "Fair H2H a/h", "Fair line", "Fair total", "vs market"]


def games_md(g: pd.DataFrame, ps: pd.DataFrame, ed: pd.DataFrame | None = None) -> str:
    if g.empty:
        return "_No games._"
    if "scenario" not in g:
        g = g.assign(scenario="base", scenario_label="all confirmed")
    if len(ps) and "scenario" not in ps:
        ps = ps.assign(scenario="base")
    base = g[g["scenario"] == "base"]
    rows = [[f"{r['away']} @ {r['home']}", r.get("tip_sydney", "")] + _line_cells(r) for _, r in base.iterrows()]
    out = ["Game lines below assume every questionable player sits; each game's section shows what changes if they play. "
           "In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, "
           "oldest to newest (- = didn't play).\n",
           _table(["Game", "Tip (Syd)"] + LINE_HEAD, rows)]
    for _, r in base.iterrows():
        a, h, gid = r["away"], r["home"], r["game_id"]
        gg, gp = g[g["game_id"] == gid], (ps[ps["game_id"] == gid] if len(ps) else ps)
        out.append(f"\n### {a} @ {h}")
        if pd.notna(r.get("out")) and r.get("out"):
            out.append(f"Out: {r['out']}\n")
        extras = _game_extras(gid, ed if ed is not None else pd.DataFrame())
        if extras:
            out.append(extras + "\n")
        alts = gg[gg["scenario"] != "base"]
        if len(alts):
            lr = [["Confirmed players only"] + _line_cells(r)]
            for _, x in alts.iterrows():
                lab = x["scenario_label"] if x["scenario"] != "expected" else "Expected (weighted by chance each plays)"
                if x["scenario"].startswith("in:") and not bool(x.get("impact", False)):
                    continue
                lr.append([lab] + _line_cells(x))
            out.append(_table(["Scenario"] + LINE_HEAD, lr) + "\n")
        if len(gp):
            maybe_rows = gp[gp["scenario"].str.startswith("in:") & (gp["player_id"] == gp.get("maybe_player"))]
            if len(maybe_rows):
                mr = []
                for _, m in maybe_rows.iterrows():
                    mr.append([f"{m['player']} ({m['team']})", _c(m.get("status")),
                               f"{int(round(100 * float(m['maybe_avail'])))}%", _f(m["proj_min"], 1)] +
                              [_f(m.get(f"proj_{s}"), 1) for s, _ in STATS] +
                              ["full tables below" if bool(m.get("impact")) else "small"])
                out.append("**Questionable players: chance to play, and their projection if they do**\n\n" +
                           _table(["Player", "Status", "Chance", "Min"] + [lab for _, lab in STATS] + ["Effect on others"], mr)
                           + "\n")
            b = gp[gp["scenario"] == "base"]
            for t in (a, h):
                out.append(f"<details><summary>{t} players (confirmed only)</summary>\n\n{_player_table(b, t)}\n\n</details>\n")
            for scen, x in gp[gp["scenario"].str.startswith("in:") & gp.get("impact", pd.Series(False, index=gp.index)).fillna(False).astype(bool)].groupby("scenario"):
                lab = x["scenario_label"].iloc[0]
                out.append(f"<details><summary>{lab}: both teams</summary>\n\n{_player_table(x, show_team=True)}\n\n</details>\n")
    return "\n".join(out)


def sanity_md(d: Path) -> str:
    from .sanity import section
    f = d / "sanity.csv"
    if not f.exists():
        return "_Checks not run yet for this slate._"
    try:
        return section(pd.read_csv(f))
    except pd.errors.EmptyDataError:
        return section(None)


LADDERS = ROOT / "LADDERS.md"
LADDER_LAB = {"pts": "PTS", "reb": "REB", "ast": "AST", "fg3m": "3PM", "stl": "STL", "blk": "BLK", "pra": "PRA",
              "pr": "PR", "pa": "PA", "ra": "RA"}


def ladders_md(lad: pd.DataFrame | None, gen: str, day: date) -> str:
    """Every nearby line per player and stat: blended chance and break-even (min) odds both ways."""
    out = [f"# Line ladders · {day.strftime('%a %d %b %Y')} (US date)",
           f"Updated **{gen}** Sydney time. Back to [TODAY.md](TODAY.md).",
           "For price shopping when a book's line differs from DraftKings'. **Over / Under** are the blended "
           "chances (model 25%, market 75%, the same as the bets on TODAY.md) if he plays; **Min odds** is the "
           "break-even price, so any price at or above it is +EV. ★ marks DraftKings' main line. *Market*: "
           "*book* = a bookie prices that exact line; *est* = the main line's market-vs-model gap carried over. Stats with no DraftKings market for "
           "a player are left out. Use the "
           "[bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) for the stake."]
    if lad is None or lad.empty:
        out.append("_No ladders for this slate yet._")
        return "\n\n".join(out) + "\n"
    lad = lad[lad["market_source"] != "model only"]  # no market to blend with: not reliable enough to shop on
    pct = lambda p: f"{100 * p:.0f}%"  # noqa: E731
    odds = lambda p: f"{1 / p:.2f}" if p > 0.005 else "–"  # noqa: E731
    for mu, g in lad.groupby("matchup", sort=False):
        out.append(f"## {mu}")
        for (team, pl), x in g.groupby(["team", "player"], sort=False):
            rows = []
            for r in x.itertuples():
                pb = float(r.p_over_blend)
                rows.append([LADDER_LAB.get(r.stat, r.stat), f"{r.line:g}" + (" ★" if r.main else ""),
                             pct(pb), odds(pb), pct(1 - pb), odds(1 - pb), r.market_source])
            out.append(f"<details><summary>{pl} ({team})</summary>\n\n" +
                       _table(["Stat", "Line", "Over", "Min odds over", "Under", "Min odds under", "Market"], rows) +
                       "\n\n</details>")
    return "\n\n".join(out) + "\n"


def build(day: date) -> Path | None:
    d = OUT / day.isoformat()
    if not d.exists():
        return None
    g, ps, ed = (_read(d, n) for n in ("games", "players", "edges"))
    ln = _read(d, "lines")
    LINES.clear()
    if ln is not None and len(ln):
        LINES.update({(r.player_id, r.market[5:], r.book): float(r.line) for r in ln.itertuples()})
    LAST5.clear()
    try:
        LAST5.update(_last5(day))
    except Exception as e:  # never let the sheet fail over the small print
        print(f"last-5 games skipped: {e}")
    gen = "n/a"
    st = d / "state.json"
    if st.exists():
        ts = json.loads(st.read_text()).get("generated")
        if ts:
            gen = pd.Timestamp(ts).tz_convert("Australia/Sydney").strftime("%a %d %b, %I:%M %p")
    bets, waiting, flagged = best_bets(ed)
    longs = best_bets(ed, longshots=True)[0].replace("_No bets clear", "_No long shots clear")
    elsewhere = best_bets(ed, longshots=None, offered=False)[0].replace("_No bets clear", "_Nothing clears")
    parts = [f"# NBA model · {day.strftime('%a %d %b %Y')} (US date)",
             f"Updated **{gen}** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, "
             f"capped at {MAX_STAKE_PCT:g}%. **EV and stake use the Blend** of model and no-vig market "
             "(the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. "
             "Lines a point or two off DraftKings': [LADDERS.md](LADDERS.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).",
             "## Sanity checks", sanity_md(d),
             f"## Best bets (EV ≥ {MIN_EV:.0%}, odds ≤ {MAX_ODDS:g})",
             "DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 "
             "minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, "
             "so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it "
             "is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.", bets,
             f"## Long shots (EV ≥ {MIN_EV:.0%}, odds above {MAX_ODDS:g})",
             "Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't "
             "proven yet. Expect long losing runs even if the edge is real.", longs,
             f"## Not on Sportsbet: check other books (EV ≥ {MIN_EV:.0%}, any odds)",
             "Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number "
             "assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others "
             "sometimes do. Not graded in HEALTH.md.", elsewhere]
    if waiting:
        parts += ["## Wait for news",
                  "These look good but hinge on a questionable player. The model's chance is shown both ways; the EV "
                  "column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet "
                  "updates itself).", waiting]
    if flagged:
        parts += ["## Check news first",
                  "The model and the no-vig market disagree by more than 15 points on these. That's usually late "
                  "team news the model hasn't seen yet, so confirm before betting.", flagged]
    parts += ["## Projections",
              "**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). "
              "**Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. "
              "Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone "
              "else's numbers. Starters and stars who are questionable get full \"if he plays\" tables for both "
              "teams. Once a status is confirmed the next run drops the alternatives.",
              games_md(g, ps, ed),
              "---\n_Model projections, not advice. Edges are against the best price found at run time. "
              f"Full data: `output/{day.isoformat()}/`._"]
    try:
        LADDERS.write_text(ladders_md(_read(d, "ladder"), gen, day))
    except Exception as e:  # never let the ladder page block the sheet
        print("ladders skipped:", e)
    md = "\n\n".join(parts) + "\n"
    (d / "today.md").write_text(md)
    TODAY.write_text(md)
    return TODAY
