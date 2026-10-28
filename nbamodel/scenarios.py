"""Who-plays scenarios for questionable players.

Every game is projected with all "maybe" players (questionable, doubtful, day-to-day, game-time
decision) OUT: that is the base the sheet shows for confirmed players. Each maybe player can then
be switched IN: his team's absence features shrink by what he brings (minutes, usage, value,
points/assists/rebounds), teammates' "minutes/usage already claimed" grow, the opponent sees the
same change on its side, and the team model re-predicts score, margin and total. Minutes and
rates are re-predicted for everyone, so his teammates lose minutes and shots and the game line moves.

The absence features are sums over absent players (see features.roster_absences), so switching a
player in is an exact subtraction of his contribution, not an approximation.
"""
from __future__ import annotations

import itertools

import numpy as np
import pandas as pd

MAYBE = {"questionable", "doubtful", "day-to-day", "game time decision", "gtd"}
MAX_EXACT = 4          # maybes per game handled as explicit in/out combinations
IMPACT_MIN = 20.0      # "impactful" maybe: projects at least this many minutes if he plays


def is_maybe(status) -> bool:
    return str(status).strip().lower() in MAYBE


def _contrib(r) -> dict:
    """What a player removes from his team's absence features when he plays."""
    f = lambda c: float(np.nan_to_num(r.get(c, 0.0)))  # noqa: E731
    m = f("min_s")
    return {"vac_min": -m, "vac_usage": -m * f("usage_r_s"), "vac_value": -m * f("value_r"),
            "vac_pts": -m * f("pts_r_s"), "vac_ast": -m * f("ast_r_s"), "vac_reb": -m * f("reb_r_s"),
            "vac_starters": -f("starter_s"), "n_absent": -1.0, "n_star_absent": -float(m >= 28),
            "avail_value": m * f("value_r"),
            **({f"vac_min_{r['pos']}": -m} if r.get("pos") in ("G", "F", "C") else {})}


def counted_absent(r) -> bool:
    """Was he in the base absence set? (= appeared for this team in its last 10 games)"""
    return bool(r.get("gp", 0) > 0 and r.get("games_missed", 99) < 10 and r.get("new_team", 0) == 0)


def switch_in(Pg: pd.DataFrame, Gg: pd.DataFrame, r: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return copies of a game's player rows and game row with player r switched IN."""
    Pg, Gg = Pg.copy(), Gg.copy()
    if not counted_absent(r):
        return Pg, Gg  # he wasn't counted as missing (long absence / new), so nothing to give back
    d = _contrib(r)
    team = r["team"]
    own, opp = Pg["team"] == team, Pg["opp"] == team
    for c, v in d.items():
        if c in Pg:
            Pg.loc[own, c] += v
        if f"opp_{c}" in Pg:
            Pg.loc[opp, f"opp_{c}"] += v
        side = "h" if Gg["home"].iloc[0] == team else "a"
        if f"{side}_{c}" in Gg:
            Gg[f"{side}_{c}"] += v
    mates = own & (Pg["player_id"] != r["player_id"])
    m = float(np.nan_to_num(r.get("min_s", 0.0)))
    if "mates_min" in Pg:
        Pg.loc[mates, "mates_min"] += m
    if "mates_usage" in Pg:
        Pg.loc[mates, "mates_usage"] += m * float(np.nan_to_num(r.get("usage_r_s", 0.0)))
    for c, rate in (("mates_pts", "pts_r_s"), ("mates_fg3m", "fg3m_r_s")):
        if c in Pg:
            Pg.loc[mates, c] += m * float(np.nan_to_num(r.get(rate, 0.0)))
    if "vac_min_same_pos" in Pg and r.get("pos") in ("G", "F", "C"):
        Pg.loc[own & (Pg["pos"] == r["pos"]), "vac_min_same_pos"] -= m
    if "vac_min_share" in Pg:
        Pg["vac_min_share"] = Pg["vac_min"] / 240
    for f in ("avail_value", "vac_value", "roster_value"):
        if f"d_{f}" in Gg:
            Gg[f"d_{f}"] = Gg[f"h_{f}"] - Gg[f"a_{f}"]
    return Pg, Gg


def combos(maybes: pd.DataFrame) -> list[tuple[frozenset, float]]:
    """All in/out combinations of the top MAX_EXACT maybes (by minutes), with probabilities."""
    top = maybes.sort_values("min_s", ascending=False).head(MAX_EXACT)
    ids, ps = top["player_id"].tolist(), top["avail_prob"].clip(0, 1).tolist()
    out = []
    for bits in itertools.product([0, 1], repeat=len(ids)):
        w = float(np.prod([p if b else 1 - p for p, b in zip(ps, bits)]))
        out.append((frozenset(i for i, b in zip(ids, bits) if b), w))
    return out


def mixture(sims: list[tuple[dict, float]], n: int) -> dict:
    """Blend scenario simulations by probability into one set of n runs (used to price bets)."""
    takes = [(s, int(round(n * w))) for s, w in sims if w > 0]
    takes = [(s, k) for s, k in takes if k > 0]
    cat = lambda key: np.concatenate([s[key][:k] for s, k in takes])  # noqa: E731
    out = {k: cat(k) for k in ("home_pts", "away_pts", "margin", "total", "ot")}
    meta = {}
    for s, _ in takes:
        for p in s["players"]:
            meta.setdefault(p["player_id"], p)
    players = []
    for pid, p0 in meta.items():
        draws = {}
        for stat in p0["draws"]:
            parts = []
            for s, k in takes:
                hit = next((p for p in s["players"] if p["player_id"] == pid), None)
                parts.append(hit["draws"][stat][:k] if hit else np.zeros(k, dtype=p0["draws"][stat].dtype))
            draws[stat] = np.concatenate(parts)
        players.append({**{k: v for k, v in p0.items() if k != "draws"}, "draws": draws})
    out["players"] = players
    return out
