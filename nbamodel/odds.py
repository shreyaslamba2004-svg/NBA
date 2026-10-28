"""Probability <-> odds conversions, vig removal and edge/Kelly maths."""
from __future__ import annotations

import numpy as np


def prob_to_american(p):
    p = np.clip(np.asarray(p, dtype=float), 1e-6, 1 - 1e-6)
    return np.where(p >= 0.5, -100 * p / (1 - p), 100 * (1 - p) / p).round(0)


def american_to_prob(o):
    o = np.asarray(o, dtype=float)
    return np.where(o < 0, -o / (-o + 100), 100 / (o + 100))


def prob_to_decimal(p):
    return 1 / np.clip(np.asarray(p, dtype=float), 1e-6, 1)


def american_to_decimal(o):
    o = np.asarray(o, dtype=float)
    return np.where(o < 0, 1 + 100 / -o, 1 + o / 100)


def devig(*american_odds):
    """Multiplicative vig removal: returns fair probabilities that sum to 1."""
    p = np.array([american_to_prob(o) for o in american_odds], dtype=float)
    return p / p.sum(axis=0)


def edge(model_p, american):
    """Expected value per unit staked of betting `american` odds when true prob is model_p."""
    return model_p * american_to_decimal(american) - 1


def kelly(model_p, american, fraction=0.25):
    b = american_to_decimal(american) - 1
    f = (model_p * b - (1 - model_p)) / b
    return np.clip(f * fraction, 0, None)
