"""Command line entry points.

  python -m nbamodel.cli run   [--date YYYY-MM-DD] [--no-props]
  python -m nbamodel.cli snapshot --kind open|pretip   (scheduled: logs lines, props, projections)
  python -m nbamodel.cli live      (scheduled every 15 min on game days; see cmd_live)
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


def cmd_live(a):
    """Game-day loop step (run every 15 min by the scheduler, from ~2h before the first tip).

    Each call (all free except where noted):
      - re-checks injury reports + rosters; re-projects the slate if anyone's status changed
      - logs DraftKings game lines from ESPN
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
    if up["mins_to_tip"].min() > LOOKAHEAD_MIN:
        print(f"first tip in {up['mins_to_tip'].min():.0f} min; nothing to do yet")
        return
    state_p = market_log.LOGS / "state" / f"{day.isoformat()}.json"
    state = json.loads(state_p.read_text()) if state_p.exists() else {"pretip_done": [], "hash": "",
                                                                         "book_lines": False}
    slate = up[["game_id", "game_date", "home", "away", "tip_utc"]]
    pg, _ = pipeline.load_history()
    sp, _ = pipeline.availability(slate, day, pg)
    h = pipeline.availability_hash(sp)
    entering = up[(up["mins_to_tip"] <= PRETIP_MIN) & ~up["game_id"].isin(state["pretip_done"])]
    if len(entering):  # buy prices first so this run's edges use them
        market_log.log_props(entering, snap, use_odds_api=True)
        if not state["book_lines"]:
            market_log.log_book_lines(snap)
            state["book_lines"] = True
        state["pretip_done"] += [int(g) for g in entering["game_id"]]
    if h != state["hash"] or len(entering):
        print("re-projecting:", "availability changed" if h != state["hash"] else "pre-tip window")
        res = pipeline.project(day, slate.drop(columns=["tip_utc"]), sp, Bundle.load(),
                               market=pipeline.market_lines(slate), props=pipeline.latest_props(slate),
                               book_lines=pipeline.latest_book_lines(slate))
        pipeline.finish(day, res, sp, slate)
        market_log.log_projections(day, res, f"{snap}|live")
        state["hash"] = h
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
        if name == "watch":
            p.add_argument("--every", type=int, default=10, help="minutes between injury checks")
        p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
