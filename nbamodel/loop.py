"""Game-day loop that runs inside one long GitHub Actions job and hands over to the next.

GitHub's cron trigger never fired for this repo (only manual runs started), so instead of
relying on it, one job runs for ~5.4 hours and, as its last step, starts the next job
(.github/workflows/game-day.yml). Inside the job, on a timer:
  - the morning snapshot once per US date, from 13:00 UTC (python -m nbamodel.cli snapshot)
  - the live check (python -m nbamodel.cli live; free sources only, re-projects when anything moved):
    every 30 min from the end of a slate until midnight Sydney, every 15 min from midnight until
    3 hours before the next tip, every 5 min from then until the last tip
  - Mondays from 14:00 UTC, starts the weekly retrain workflow
  - commits and pushes whatever changed after each step
State (what's been done today) lives in logs/state/loop.json so the next job carries on.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "logs" / "state" / "loop.json"
RUN_HOURS = 5.4
NEAR_TIP_MIN = 180  # within this many minutes of a tip, check every 5 minutes
FAST, OVERNIGHT, EVENING = 300, 900, 1800  # seconds between live checks


def check_every(mins_to_tip: float, now: pd.Timestamp) -> int:
    """5 min near a tip; otherwise 15 min after midnight Sydney (slate morning), 30 min from
    noon (games over) until midnight."""
    if mins_to_tip <= NEAR_TIP_MIN:
        return FAST
    return OVERNIGHT if now.tz_convert("Australia/Sydney").hour < 12 else EVENING


def sh(cmd: str) -> int:
    print("$", cmd, flush=True)
    return subprocess.run(cmd, shell=True, cwd=ROOT).returncode


def commit(msg: str) -> None:
    sh("git add -f TODAY.md HEALTH.md logs output data/processed/current_season_* data/processed/espn_crosswalk.json")
    if sh("git diff --cached --quiet") == 0:
        return
    sh(f'git commit -q -m "{msg}"')
    for _ in range(4):
        if sh("git pull -q --rebase -X theirs origin main && git push -q origin HEAD:main") == 0:
            return
        time.sleep(15)


def load() -> dict:
    try:
        return json.loads(STATE.read_text())
    except (OSError, ValueError):
        return {}


def save(st: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st))


def mins_to_next_tip(day) -> float:
    try:
        from .sources import espn
        sb = espn.scoreboard(day)
        up = sb[sb["status"] == "STATUS_SCHEDULED"]
        if up.empty:
            return float("inf")
        return float(((pd.to_datetime(up["tip_utc"], utc=True) - pd.Timestamp.now(tz="UTC"))
                      .dt.total_seconds() / 60).min())
    except Exception as e:  # network hiccup: check again on the slow timer
        print("scoreboard failed:", e)
        return float("inf")


def main() -> None:
    end = time.time() + RUN_HOURS * 3600
    while time.time() < end:
        start = time.time()
        now = pd.Timestamp.now(tz="UTC")
        day = now.tz_convert("America/New_York").date()
        st = load()
        if now.hour >= 13 and st.get("snapshot") != str(day):
            if sh("python -m nbamodel.cli snapshot") == 0:
                st["snapshot"] = str(day)
                save(st)
            commit(f"snapshot {now:%Y-%m-%dT%H:%MZ}")
        if now.weekday() == 0 and now.hour >= 14 and st.get("weekly") != str(now.date()):
            if sh("gh workflow run weekly.yml") == 0:
                st["weekly"] = str(now.date())
                save(st)
                commit(f"loop state {now:%Y-%m-%dT%H:%MZ}")
        sh("python -m nbamodel.cli live")
        commit(f"projections {pd.Timestamp.now(tz='UTC'):%Y-%m-%dT%H:%MZ}")
        wait = check_every(mins_to_next_tip(day), pd.Timestamp.now(tz="UTC"))
        time.sleep(max(30.0, min(wait - (time.time() - start), end - time.time())))


if __name__ == "__main__":
    main()
