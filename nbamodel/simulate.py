"""Monte Carlo game simulation -> score/margin/total distributions and player stat distributions.

Each simulation draws (1) correlated team scores around the team-model means, resolving ties
with overtime, (2) player availability for questionable players, (3) player minutes, rescaled
so each team plays 240 (+25 per OT) minutes, and (4) player stat counts from gamma-Poisson
(negative binomial) draws whose means scale with the simulated team scoring/pace, so player
props stay correlated with the game script.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .models import SIM_STATS, Bundle
from .odds import prob_to_american, prob_to_decimal

N_SIMS = 20000
COMBOS = {"pra": ["pts", "reb", "ast"], "pr": ["pts", "reb"], "pa": ["pts", "ast"], "ra": ["reb", "ast"],
          "stocks": ["stl", "blk"]}
# how strongly each stat follows simulated team scoring (pts) / game pace
TEAM_ELAST = {"pts": 1.0, "fg3m": 0.8, "ast": 0.8, "fga": 0.5, "fta": 0.5, "reb": 0.0, "stl": 0.0,
              "blk": 0.0, "tov": 0.0}
PACE_ELAST = {"reb": 0.6, "stl": 0.5, "blk": 0.5, "tov": 0.5}
OT_MEAN, OT_SD = 10.5, 3.5


def _scale_minutes(pmin: np.ndarray, target: float, cap=46.0) -> np.ndarray:
    """Scale minutes to the team target; `cap` may be per player (e.g. minutes restrictions)."""
    m = pmin.astype(float).copy()
    cap = np.broadcast_to(np.asarray(cap, dtype=float), m.shape)
    m = np.minimum(m, cap)
    for _ in range(10):
        free = m < cap
        s = m.sum()
        if s <= 0 or abs(s - target) < 0.05:
            break
        excess = target - m[~free].sum()
        m[free] *= excess / max(m[free].sum(), 1e-9)
        m = np.minimum(m, cap)
    return m


def expected_minutes(players: pd.DataFrame, b: Bundle) -> np.ndarray:
    """Normalise model minutes so a team's expected minutes sum to 240 + expected OT."""
    target = 240 + 25 * 0.06
    w = players["play_prob"].values
    raw = players["pmin_raw"].values
    # scale only over expected participants; questionable players count at their play_prob
    caps = players["min_cap"].fillna(46.0).values if "min_cap" in players else 46.0
    scaled = _scale_minutes(raw * w, target, np.minimum(caps, 46.0) * np.maximum(w, 1e-9))
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(w > 0, scaled / w, 0.0)


def simulate_game(game: dict, players: pd.DataFrame, b: Bundle, n: int = N_SIMS, seed: int = 0) -> dict:
    """game: {home, away, mu_margin, mu_total}; players: rows with team, pmin, play_prob, rate_<stat>."""
    rng = np.random.default_rng(seed)
    mu_h = (game["mu_total"] + game["mu_margin"]) / 2
    mu_a = (game["mu_total"] - game["mu_margin"]) / 2
    sd_m, sd_t = b.margin_sd, b.total_sd
    # sample margin & total residuals (approximately independent, corr ~ 0) then map to scores
    zm = rng.normal(0, sd_m, n)
    zt = rng.normal(0, sd_t, n)
    h = np.rint(mu_h + (zt + zm) / 2)
    a = np.rint(mu_a + (zt - zm) / 2)
    ot = np.zeros(n, dtype=int)
    tie = h == a
    while tie.any():
        k = tie.sum()
        h[tie] += np.rint(rng.normal(OT_MEAN, OT_SD, k))
        a[tie] += np.rint(rng.normal(OT_MEAN, OT_SD, k))
        ot[tie] += 1
        tie = h == a
    margin, total = h - a, h + a

    out_players = []
    for team, mu_team, sim_team in ((game["home"], mu_h, h), (game["away"], mu_a, a)):
        tp = players[players["team"] == team]
        if tp.empty:
            continue
        k = len(tp)
        avail = rng.random((n, k)) < tp["play_prob"].values
        sd = np.array([b.min_sd.get(int(x), 6.0) for x in pd.cut(
            tp["pmin"], [0, 10, 18, 26, 32, 48], labels=False, include_lowest=True).fillna(0)])
        mins = np.clip(rng.normal(tp["pmin"].values, sd, (n, k)), 0, 48) * avail
        if b.blowout and getattr(b, "use_blowout", False):  # game script: stars sit in lopsided runs, benches absorb the minutes
            from .models import BLOWOUT_EDGES, ROLE_EDGES
            mb = np.clip(np.searchsorted(BLOWOUT_EDGES, np.abs(margin), side="right") - 1,
                         0, len(BLOWOUT_EDGES) - 2)
            role = np.clip(np.searchsorted(ROLE_EDGES, tp["pmin"].values, side="right") - 1, 0, 3)
            curve = np.array([b.blowout.get(int(r), [1.0] * (len(BLOWOUT_EDGES) - 1)) for r in role])
            mins *= curve[:, mb].T * (ot == 0)[:, None] + (ot > 0)[:, None]
        target = 240 + 25 * ot
        mins *= (target / np.maximum(mins.sum(1), 1))[:, None]
        mins = np.clip(mins, 0, 53)
        f_team = (sim_team / mu_team)[:, None]
        f_pace = (total / game["mu_total"])[:, None]
        draws = {"min": mins}
        for s in SIM_STATS:
            rate = tp[f"rate_{s}"].values
            mean = rate * mins * f_team ** TEAM_ELAST.get(s, 0) * f_pace ** PACE_ELAST.get(s, 0)
            kd = b.disp.get(s, 50.0)
            lam = rng.gamma(kd, np.maximum(mean, 1e-9) / kd)
            draws[s] = rng.poisson(lam)
        draws["fg3m"] = np.minimum(draws["fg3m"], draws["pts"] // 3)
        for c, parts in COMBOS.items():
            draws[c] = sum(draws[p] for p in parts)
        for j, r in enumerate(tp.itertuples(index=False)):
            out_players.append({"team": team, "player_id": r.player_id, "player_name": r.player_name,
                                "play_prob": r.play_prob, "status": getattr(r, "status", ""),
                                "draws": {s: v[:, j] for s, v in draws.items()}})
    return {"home_pts": h, "away_pts": a, "margin": margin, "total": total, "ot": ot,
            "players": out_players, "mu_h": mu_h, "mu_a": mu_a}


def _fair_line(x: np.ndarray) -> float:
    """Half-point line closest to a 50/50 over/under split."""
    med = np.median(x)
    cands = np.arange(np.floor(med) - 2.5, np.ceil(med) + 3, 1.0)
    p = np.array([(x > c).mean() for c in cands])
    return float(cands[np.argmin(np.abs(p - 0.5))])


def summarize_game(sim: dict, game: dict) -> dict:
    m, t = sim["margin"], sim["total"]
    p_home = float((m > 0).mean())
    spread_home = -_fair_line(m)  # standard notation: negative = home favoured
    out = {"home": game["home"], "away": game["away"],
           "proj_home_pts": round(float(sim["home_pts"].mean()), 1),
           "proj_away_pts": round(float(sim["away_pts"].mean()), 1),
           "proj_margin_home": round(float(m.mean()), 1), "proj_total": round(float(t.mean()), 1),
           "home_win_prob": round(p_home, 4), "away_win_prob": round(1 - p_home, 4),
           "fair_ml_home": int(prob_to_american(p_home)), "fair_ml_away": int(prob_to_american(1 - p_home)),
           "fair_dec_home": round(float(prob_to_decimal(p_home)), 2),
           "fair_dec_away": round(float(prob_to_decimal(1 - p_home)), 2),
           "fair_spread_home": spread_home, "fair_total": _fair_line(t),
           "p_ot": round(float((sim["ot"] > 0).mean()), 4),
           }
    if game.get("market_spread_home") is not None and not pd.isna(game.get("market_spread_home")):
        line = float(game["market_spread_home"])
        p_cover = float((m + line > 0).mean())
        push = float((m + line == 0).mean())
        out.update({"market_spread_home": line, "p_home_cover": round(p_cover, 4),
                    "p_away_cover": round(1 - p_cover - push, 4)})
    if game.get("market_total") is not None and not pd.isna(game.get("market_total")):
        line = float(game["market_total"])
        out.update({"market_total": line, "p_over": round(float((t > line).mean()), 4),
                    "p_under": round(float((t < line).mean()), 4)})
    return out


def summarize_players(sim: dict, prop_lines: pd.DataFrame | None = None) -> pd.DataFrame:
    rows = []
    for p in sim["players"]:
        d = p["draws"]
        played = d["min"] > 0
        r = {"team": p["team"], "player_id": p["player_id"], "player": p["player_name"],
             "play_prob": round(float(p["play_prob"]), 2), "status": p["status"],
             "proj_min": round(float(d["min"][played].mean()) if played.any() else 0.0, 1)}
        for s in ["pts", "reb", "ast", "fg3m", "stl", "blk", "tov"] + list(COMBOS):
            x = d[s][played] if played.any() else d[s]
            r[f"proj_{s}"] = round(float(x.mean()), 2)
            fl = _fair_line(x)
            po = float((x > fl).mean())
            r[f"line_{s}"] = fl
            r[f"p_over_{s}"] = round(po, 3)
            r[f"fair_over_{s}"] = int(prob_to_american(po))
            r[f"fair_under_{s}"] = int(prob_to_american(1 - po))
            r[f"fair_over_dec_{s}"] = round(float(prob_to_decimal(po)), 2)
            r[f"fair_under_dec_{s}"] = round(float(prob_to_decimal(1 - po)), 2)
        rows.append(r)
    return pd.DataFrame(rows)


def prob_over(sim: dict, player_id: int, stat: str, line: float) -> float:
    for p in sim["players"]:
        if p["player_id"] == player_id:
            x = p["draws"][stat][p["draws"]["min"] > 0]
            return float((x > line).mean())
    return float("nan")
