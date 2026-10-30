"""Command line entry points.

  python -m nbamodel.cli run   [--date YYYY-MM-DD] [--no-props]
  python -m nbamodel.cli snapshot --kind open|pretip   (scheduled: logs lines, props, projections)
  python -m nbamodel.cli live      (scheduled by nbamodel/loop.py; 5 min near tips)
  python -m nbamodel.cli sgm --game LAL --legs "..." --price 4.2   (value-check a quoted multi)
  python -m nbamodel.cli watch [--date YYYY-MM-DD] [--every 10]
      Re-checks rosters + injury reports every N minutes and re-projects the slate whenever
      any player's status changes (injury, rest, return, signing). Stops after the last tip.
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import date, datetime, timezone
from pathlib import Path

import pandas as pd

from . import pipeline
from .models import Bundle
from .sources import espn


def _today_et() -> date:
    return pd.Timestamp.now(tz="America/New_York").date()


def cmd_run(a):
    pipeline.run(a.date, refresh=not a.no_refresh, with_props=not a.no_props)


def cmd_watch(a):
    day = a.date
    pipeline.run(day, refresh=not a.no_refresh, with_props=not a.no_props)
    b = Bundle.load()
    state = pipeline.OUT / day.isoformat() / "state.json"
    last = json.loads(state.read_text())["availability_hash"] if state.exists() else ""
    while True:
        time.sleep(a.every * 60)
        slate = espn.scoreboard(day)
        slate = slate[slate["status"] == "STATUS_SCHEDULED"][["game_id", "game_date", "home", "away", "tip_utc"]]
        if slate.empty:
            print("all games tipped; stopping")
            return
        pg, _ = pipeline.load_history()
        sp, _ = pipeline.availability(slate, day, pg)
        h = pipeline.availability_hash(sp)
        if h == last:
            print(datetime.now(timezone.utc).strftime("%H:%M"), "no availability change")
            continue
        old = pd.read_csv(pipeline.OUT / day.isoformat() / "availability.csv")
        diff = sp.merge(old[["player_id", "status"]], on="player_id", how="left", suffixes=("", "_old"))
        changed = diff[diff["status"] != diff["status_old"]]
        print("availability changed:\n", changed[["team", "player_name", "status_old", "status"]].to_string())
        res = pipeline.project(day, slate.drop(columns=["tip_utc"]), sp, b,
                               market=pipeline.market_lines(slate),
                               props=pipeline.props_market(slate) if not a.no_props else None)
        res["availability"] = sp
        pipeline.write_outputs(day, res)
        stamp = datetime.now(timezone.utc).strftime("%H%M")
        pipeline.write_outputs(day, {"changes": changed}, tag=f"_{stamp}")
        state.write_text(json.dumps({"availability_hash": h, "generated": stamp}))
        last = h


def cmd_snapshot(a):
    """Scheduled job: grade yesterday, refresh, project today's slate, log lines + props.

    --kind open    morning run (opening-ish lines and props)
    --kind pretip  before the first tip (final injury reports, near-closing lines and props)
    """
    from datetime import timedelta
    from . import market_log
    day = a.date
    snap = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    try:
        market_log.log_results(day - timedelta(days=1))
    except Exception as e:  # grading must never block projections
        print("results logging failed:", e)
    try:
        from . import health
        health.build()
    except Exception as e:
        print("health page failed:", e)
    try:
        from . import history
        history.build()  # each graded day's page is written once
    except Exception as e:
        print("history pages failed:", e)
    try:
        market_log.compact()
    except Exception as e:
        print("log compaction failed:", e)
    slate = espn.scoreboard(day)
    slate = slate[slate["status"] == "STATUS_SCHEDULED"]
    if slate.empty:
        print("no upcoming games on", day)
        return
    # log prices first so the projection (and TODAY.md) is measured against them
    market_log.log_game_lines(slate, snap)
    market_log.log_book_lines(snap)
    if not a.no_props:
        # morning: free DraftKings props only; AU-book props are bought per game by `live`
        market_log.log_props(slate, snap, use_odds_api=a.kind == "pretip")
    res = pipeline.run(day, refresh=not a.no_refresh, with_props=False, props=pipeline.latest_props(slate))
    if res:
        market_log.log_projections(day, res, f"{snap}|{a.kind}")


SYDNEY = "Australia/Sydney"
PRETIP_MIN = 40   # a game enters its pre-tip window this many minutes before tip
LOOKAHEAD_MIN = 120


def model_hash() -> str:
    """Fingerprint of the projection code and trained models, so a fix or retrain rewrites the sheet."""
    import hashlib
    root = Path(__file__).resolve().parent
    h = hashlib.sha1()
    for f in sorted([*root.rglob("*.py"), *(root.parent / "models").glob("*")]):
        if f.is_file():
            h.update(f.name.encode() + f.read_bytes())
    return h.hexdigest()


def cmd_live(a):
    """Game-day loop step: run on a timer by nbamodel/loop.py (5 min within 3h of a tip).

    Each call (all free except where noted):
      - re-checks injury reports + rosters, and fetches DraftKings props from ESPN; re-projects
        the slate (and TODAY.md) if anyone's status or any DraftKings prop price changed
      - logs DraftKings game lines from ESPN (from ~2h before the first tip)
      - for each game entering its pre-tip window (~40 min before tip), once per game:
          ESPN DraftKings props for that game, AU-book props from The Odds API (1 credit per
          prop market), and, once per day, every AU book's game lines (3 credits)
    """
    from . import market_log
    day = a.date
    now = pd.Timestamp.now(tz="UTC")
    snap = now.strftime("%Y-%m-%dT%H:%MZ")
    sb = espn.scoreboard(day)
    if sb.empty:
        print("no games today")
        return
    up = sb[sb["status"] == "STATUS_SCHEDULED"].copy()
    if up.empty:
        print("all games started")
        return
    up["mins_to_tip"] = (pd.to_datetime(up["tip_utc"], utc=True) - now).dt.total_seconds() / 60
    if getattr(a, "near_tip_only", False) and up["mins_to_tip"].min() > LOOKAHEAD_MIN:
        print(f"next tip in {up['mins_to_tip'].min():.0f} min; the slower timer covers this")
        return
    state_p = market_log.LOGS / "state" / f"{day.isoformat()}.json"
    state = {"pretip_done": [], "hash": "", "book_lines": False, "dk_hash": "", "model_hash": ""}
    if state_p.exists():
        state.update(json.loads(state_p.read_text()))
    slate = up[["game_id", "game_date", "home", "away", "tip_utc"]]
    pg, _ = pipeline.load_history()
    sp, _ = pipeline.availability(slate, day, pg)
    h = pipeline.availability_hash(sp)
    # free DraftKings props (via ESPN) every run, so value shows up early; AU books are bought pre-tip
    dk = pipeline.props_market(slate, pg, use_odds_api=False)
    dk_hash = pipeline.props_hash(dk)
    entering = up[(up["mins_to_tip"] <= PRETIP_MIN) & ~up["game_id"].isin(state["pretip_done"])]
    if len(entering):  # buy prices first so this run's edges use them
        market_log.log_props(entering, snap, use_odds_api=True)
        if not state["book_lines"]:
            market_log.log_book_lines(snap)
            state["book_lines"] = True
        state["pretip_done"] += [int(g) for g in entering["game_id"]]
        state_p.parent.mkdir(parents=True, exist_ok=True)
        state_p.write_text(json.dumps(state))  # saved now: a later failure must not re-buy these props
    mh = model_hash()
    news = h != state["hash"] or len(entering) or mh != state["model_hash"]
    if news or dk_hash != state["dk_hash"]:
        print("re-projecting:", "availability changed" if h != state["hash"] else
              "pre-tip window" if len(entering) else "model or code changed" if mh != state["model_hash"]
              else "DraftKings props moved")
        props = pipeline.latest_props(slate)
        if dk is not None:  # this run's DraftKings prices replace the last logged ones
            keep = props[props["source"] != "espn"] if props is not None else None
            props = pd.concat([keep, dk.assign(snapshot_utc=snap)], ignore_index=True)
        res = pipeline.project(day, slate.drop(columns=["tip_utc"]), sp, Bundle.load(),
                               market=pipeline.market_lines(slate), props=props,
                               book_lines=pipeline.latest_book_lines(slate))
        pipeline.finish(day, res, sp, slate)
        if news:  # the graded log keeps news-driven runs only (keeps the repo small)
            market_log.log_projections(day, res, f"{snap}|live")
        state["hash"], state["dk_hash"], state["model_hash"] = h, dk_hash, mh
    if up["mins_to_tip"].min() <= LOOKAHEAD_MIN:
        market_log.log_game_lines(slate, snap)
    state_p.parent.mkdir(parents=True, exist_ok=True)
    state_p.write_text(json.dumps(state))
    tips = ", ".join(f"{r.away}@{r.home} {pd.Timestamp(r.tip_utc).tz_convert(SYDNEY):%H:%M}"
                     for r in up.itertuples())
    print("upcoming (Sydney time):", tips)


def cmd_sgm(a):
    """Check a bookie's quoted same-game multi against the model.

    python -m nbamodel.cli sgm --game LAL --legs "LeBron James pts over 24.5; LAL win" --price 4.2
    """
    from . import sgm
    from .simulate import simulate_game
    inp = pd.read_csv(pipeline.OUT / a.date.isoformat() / "sim_inputs.csv")
    g = inp[(inp["game_home"] == a.game.upper()) | (inp["game_away"] == a.game.upper())]
    if g.empty:
        raise SystemExit(f"no game for {a.game} on {a.date}")
    r = g.iloc[0]
    game = {"home": r.game_home, "away": r.game_away, "mu_margin": r.game_mu_margin, "mu_total": r.game_mu_total}
    sim = simulate_game(game, g, Bundle.load(), seed=int(r.game_id) % 2**31)
    res = sgm.check(sim, r.game_home, r.game_away, a.legs, a.price, dict(zip(g["player_id"], g["player_name"])))
    for leg, p in res["legs"]:
        print(f"  {leg:45s} {p:6.1%}")
    print(f"together: {res['model_prob']:.1%}  fair odds {res['fair_odds']:.2f}  "
          f"quoted {a.price:.2f}  EV {res['ev']:+.1%}  -> {res['verdict']}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(required=True)
    for name, fn in (("run", cmd_run), ("watch", cmd_watch), ("snapshot", cmd_snapshot), ("live", cmd_live),
                     ("sgm", cmd_sgm)):
        p = sub.add_parser(name)
        p.add_argument("--date", type=date.fromisoformat, default=_today_et())
        p.add_argument("--no-props", action="store_true")
        p.add_argument("--no-refresh", action="store_true")
        if name == "snapshot":
            p.add_argument("--kind", choices=["open", "pretip"], default="open")
        if name == "sgm":
            p.add_argument("--game", required=True, help="either team's code, e.g. LAL")
            p.add_argument("--legs", required=True, help='e.g. "LeBron James pts over 24.5; LAL win"')
            p.add_argument("--price", type=float, required=True, help="bookie's decimal price")
        if name == "live":
            p.add_argument("--near-tip-only", action="store_true",
                           help="skip unless a game tips within 2 hours (the in-between 5-minute runs)")
        if name == "watch":
            p.add_argument("--every", type=int, default=10, help="minutes between injury checks")
        p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
