"""Which player props the user's bookie actually offers (bookie_markets.json at the repo root).

Bookies don't list every player for every stat: Sportsbet has points for most of the rotation but
assists, PRA and the two-stat combos only for the main players, and the combos only at one line.
No free feed says exactly who is listed, so each stat allows the top N players in the game by
projected output, and stats without a milestone ladder allow only the main over/under line. An over X.5 alt line is
the same bet as a (X+1)+ milestone, so it counts wherever the stat has a ladder; alt unders never do.
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
    exp = {}
    for stat in mk:
        parts = COMBOS.get(stat, [stat])
        if all(f"rate_{p}" in gp for p in parts):
            v = sum(gp[f"rate_{p}"] for p in parts) * gp["pmin"] * gp.get("play_prob", 1.0)
            exp[stat] = set(gp.loc[v.sort_values(ascending=False).index[:mk[stat]["players_per_game"]], "player_id"])
    ok = []
    for r in offers.itertuples():
        if not str(r.market).startswith("prop_"):
            ok.append(True)
            continue
        stat = r.market[5:]
        rule = mk.get(stat)
        main = bool(getattr(r, "paired", True))
        # an alt over X.5 is the same bet as the bookie's (X+1)+ milestone; there are no alt unders
        step = rule.get("milestone_step", 1) if rule else 1  # combos come in 10+, 15+, ...
        alt_ok = (rule and rule.get("milestones", True) and str(getattr(r, "selection", "over")) == "over"
                  and (float(r.line) + 0.5) % step == 0)
        ok.append(bool(rule) and r.player_id in exp.get(stat, set()) and (main or bool(alt_ok)))
    return pd.Series(ok, index=offers.index)
