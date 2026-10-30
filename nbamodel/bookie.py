"""Which player props the user's bookie actually offers (bookie_markets.json at the repo root).

Bookies don't list every player for every stat: Sportsbet has points for most of the rotation but
assists, PRA and the two-stat combos only for the main players, and the combos only at one line.
No free feed says exactly who is listed, so main over/under lines count for each team's top
`lines_per_team` players in that stat (Sportsbet: about 6), and milestones (X+) count for everyone
on the ladder's steps (e.g. points 10+, 15+). An over X.5 is the same bet as the (X+1)+ milestone.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .simulate import COMBOS

CONFIG = Path(__file__).resolve().parents[1] / "bookie_markets.json"


def config() -> dict:
    return json.loads(CONFIG.read_text()) if CONFIG.exists() else {"only_offered": False, "markets": {}}


def offered(offers: pd.DataFrame, gp: pd.DataFrame) -> pd.Series:
    """True for offers the bookie lists. offers: market, player_id, paired; gp: the game's players
    with pmin and rate_<stat> (expected-minutes projection)."""
    cfg = config()
    if not cfg.get("only_offered"):
        return pd.Series(True, index=offers.index)
    mk = cfg["markets"]
    exp = {}  # stat -> players with a main over/under line: each team's top `lines_per_team` in that stat
    team = gp["team"] if "team" in gp else pd.Series("all", index=gp.index)
    for stat in mk:
        parts = COMBOS.get(stat, [stat])
        if all(f"rate_{p}" in gp for p in parts):
            # rank by output if he plays: a questionable star is still listed by the bookie
            v = sum(gp[f"rate_{p}"] for p in parts) * gp["pmin"] * gp.get("rotation_prob", gp.get("play_prob", 1.0))
            n = mk[stat].get("lines_per_team", 6)
            top = v.groupby(team).rank(ascending=False, method="first") <= n
            exp[stat] = set(gp.loc[top, "player_id"])
    ok = []
    for r in offers.itertuples():
        if not str(r.market).startswith("prop_"):
            ok.append(True)
            continue
        stat = r.market[5:]
        rule = mk.get(stat)
        if not rule:
            ok.append(False)
            continue
        # main over/under lines only for each team's top players; milestones (X+) for everyone.
        # An over X.5 is the same bet as the (X+1)+ milestone, if that number is on the ladder.
        step = rule.get("milestone_step", 1)
        milestone = (rule.get("milestones", True) and str(getattr(r, "selection", "over")) == "over"
                     and (float(r.line) + 0.5) % step == 0)
        main = bool(getattr(r, "paired", True)) and r.player_id in exp.get(stat, set())
        ok.append(bool(main or milestone))
    return pd.Series(ok, index=offers.index)
