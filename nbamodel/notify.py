"""Phone alerts for new best bets, through ntfy (https://ntfy.sh: free app, no account).

Set the NTFY_TOPIC secret to a long random topic name and subscribe to it in the ntfy app. Each run
sends only bets that weren't already alerted today (output/<date>/alerted.json). No topic, no alerts.
"""
from __future__ import annotations

import json
import os
from datetime import date
from pathlib import Path

import pandas as pd
import requests

from . import dashboard as D

SHEET = "https://github.com/shreyaslamba2004-svg/NBA/blob/main/TODAY.md"


def _best(ed: pd.DataFrame) -> pd.DataFrame:
    """The rows in TODAY.md's main best-bets table."""
    e = ed.copy()
    if "offered" in e:
        e = e[e["offered"].astype(str).str.lower() != "false"]
    e = e[(e["check_news"].astype(str).str.lower() != "true") & (e["depends_on"].fillna("").astype(str) == "")
          & (e["ev_blend"] >= D.MIN_EV) & (e["price_decimal"] <= D.MAX_ODDS)]
    return e.sort_values("ev_blend", ascending=False).drop_duplicates(["matchup", "market", "selection", "line", "player"])


def alert(day: date, out_dir: Path) -> int:
    topic = os.environ.get("NTFY_TOPIC", "").strip()
    if topic:
        ping_once()
    f = out_dir / "edges.csv"
    if not topic or not f.exists():
        return 0
    try:
        ed = pd.read_csv(f, low_memory=False)
    except pd.errors.EmptyDataError:
        return 0
    if ed.empty:
        return 0
    seen_f = out_dir / "alerted.json"
    seen = set(json.loads(seen_f.read_text())) if seen_f.exists() else set()
    lines, keys = [], []
    for _, r in _best(ed).iterrows():
        k = f"{r['matchup']}|{r['market']}|{r['selection']}|{r['line']}|{r.get('player', '')}"
        if k in seen:
            continue
        keys.append(k)
        lines.append(f"{D._bet_label(r)} ({r['matchup']})\n{r['book']} {float(r['price_decimal']):.2f}, "
                     f"min odds {1 / float(r['blend_prob']):.2f}, EV {100 * float(r['ev_blend']):+.1f}%, "
                     f"stake {D._stake(r['kelly_25'])}")
    if not lines:
        return 0
    try:
        requests.post(f"https://ntfy.sh/{topic}", data="\n\n".join(lines).encode(), timeout=15,
                      headers={"Title": f"{len(lines)} new best bet{'s' if len(lines) > 1 else ''}",
                               "Tags": "basketball", "Click": SHEET})
    except requests.RequestException as e:  # an alert must never stop the sheet
        print("alert failed:", e)
        return 0
    seen_f.write_text(json.dumps(sorted(seen | set(keys))))
    return len(lines)


def ping_once() -> bool:
    """Push one confirmation the first time a run sees NTFY_TOPIC (marker: logs/ntfy_connected)."""
    topic = os.environ.get("NTFY_TOPIC", "").strip()
    marker = Path(__file__).resolve().parents[1] / "logs" / "ntfy_connected"
    if not topic or marker.exists():
        print("NTFY_TOPIC", "set" if topic else "not set")
        return False
    requests.post(f"https://ntfy.sh/{topic}", timeout=15, data=b"The GitHub loop can reach your phone. "
                  b"New best bets will arrive here.", headers={"Title": "NBA alerts connected", "Tags": "white_check_mark"})
    marker.write_text(date.today().isoformat() + "\n")
    return True
