"""Which player props the user's bookie actually offers (bookie_markets.json at the repo root).

Bookies don't list every player for every stat: Sportsbet has points for most of the rotation but
assists, PRA and the two-stat combos only for the main players, and the combos only at one line.
No free feed says exactly who is listed, so each stat allows the top N players in the game by
projected output, and stats without a milestone ladder allow only the main over/under line.
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
        ok.append(bool(rule) and r.player_id in exp.get(stat, set()) and
                  (rule.get("milestones", True) or bool(getattr(r, "paired", True))))
    return pd.Series(ok, index=offers.index)
