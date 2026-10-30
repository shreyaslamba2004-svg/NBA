"""Over/under chances at nearby lines, for price shopping (LADDERS.md).

For each player and stat the simulation gives the model's chance at every X.5 line. The bets use a
blend with the no-vig market, so each line also gets a market chance: the books' own no-vig price
where one is priced at that line, otherwise the main line's market-vs-model gap carried over on the
log-odds scale. Min odds = 1 / blended chance (break-even).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import edges as E

STATS = ["pts", "reb", "ast", "fg3m", "stl", "blk", "pra", "pr", "pa", "ra"]
SPAN = {"pts": 4, "pra": 5, "pr": 4, "pa": 4, "ra": 3, "reb": 3, "ast": 3, "fg3m": 2, "stl": 1, "blk": 1}
MIN_PMIN = 12  # skip players projected under this many minutes


def _logit(p):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def build(sim: dict, ev: pd.DataFrame | None, gp: pd.DataFrame, game_id, matchup: str) -> pd.DataFrame:
    w = E.blend_weights()["props"]
    pmin = dict(zip(gp["player_id"], gp["pmin"]))
    mk = pd.DataFrame()
    if ev is not None and len(ev):
        mk = ev[ev["market"].astype(str).str.startswith("prop_") & (ev["selection"] == "over")
                & ev["market_novig_prob"].notna()]
        mk = mk.assign(stat=mk["market"].str[5:]).drop_duplicates(["player_id", "stat", "line"])
    rows = []
    for pl in sim["players"]:
        pid = pl["player_id"]
        if pmin.get(pid, 0) < MIN_PMIN:
            continue
        played = pl["draws"]["min"] > 0
        if not played.any():
            continue
        for s in STATS:
            if s not in pl["draws"]:
                continue
            x = pl["draws"][s][played]
            m = mk[(mk["player_id"] == pid) & (mk["stat"] == s)] if len(mk) else mk
            main = m[m["main_line"].astype(str).str.lower() == "true"] if len(m) and "main_line" in m else m.iloc[:0]
            if len(main):
                main = main.iloc[(main["market_novig_prob"].astype(float) - .5).abs().argsort()[:1]]
                centre = float(main["line"].iloc[0])
                gap = float(_logit(main["market_novig_prob"].iloc[0]) - _logit((x > centre).mean()))
            else:
                centre, gap = np.floor(np.median(x)) + .5, None
            priced = dict(zip(m["line"].astype(float), m["market_novig_prob"].astype(float))) if len(m) else {}
            for line in np.arange(max(.5, centre - SPAN[s]), centre + SPAN[s] + .5, 1.0):
                pm = float((x > line).mean())
                if line in priced:
                    pk, src = priced[line], "book"
                elif gap is not None:
                    pk, src = float(1 / (1 + np.exp(-(_logit(pm) + gap)))), "est"
                else:
                    pk, src = np.nan, "model only"
                pb = pm if np.isnan(pk) else w * pm + (1 - w) * pk
                rows.append({"game_id": game_id, "matchup": matchup, "team": pl["team"], "player_id": pid,
                             "player": pl["player_name"], "stat": s, "line": line,
                             "main": bool(len(main)) and line == centre, "p_over_model": round(pm, 4),
                             "p_over_market": None if np.isnan(pk) else round(pk, 4), "market_source": src,
                             "p_over_blend": round(pb, 4)})
    return pd.DataFrame(rows)
