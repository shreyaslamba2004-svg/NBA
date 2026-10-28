# Backtest: trained through 2023-24, noise calibrated on 2024-25, tested on 2025-26

## Player projections (2025-26, every player-game, n=28328)

| stat | model MAE | baseline MAE (recent avg) | improvement |
|---|---|---|---|
| minutes | 4.36 | 5.13 | 15.0% |
| pts | 4.36 | 4.59 | 4.8% |
| reb | 1.81 | 1.89 | 3.9% |
| ast | 1.30 | 1.34 | 2.9% |
| fg3m | 0.87 | 0.88 | 1.1% |
| stl | 0.71 | 0.72 | 1.0% |
| blk | 0.51 | 0.50 | -1.3% |
| tov | 0.87 | 0.89 | 2.5% |

## Games (2025-26, n=1265; 505 with closing lines)

Calibrated noise: margin sd 14.05, total sd 18.35

| metric | model (all games) | model (games w/ lines) | closing line |
|---|---|---|---|
| Margin MAE | 11.28 | 10.93 | 10.60 |
| Total MAE | 15.03 | 15.59 | 14.93 |
| Total MAE (bottom-up from players) | 15.44 | | |

Win probability log-loss: model 0.5889 (all), model 0.6233 vs no-vig closing moneyline 0.6167 (same 505 games). Brier: model 0.2170 vs market 0.2140.

Win-prob calibration:

| bucket | games | predicted | actual |
|---|---|---|---|
| (0.0, 0.2] | 29.0 | 0.163 | 0.034 |
| (0.2, 0.35] | 160.0 | 0.284 | 0.219 |
| (0.35, 0.5] | 308.0 | 0.428 | 0.412 |
| (0.5, 0.65] | 332.0 | 0.576 | 0.578 |
| (0.65, 0.8] | 318.0 | 0.720 | 0.748 |
| (0.8, 1.0] | 118.0 | 0.845 | 0.907 |

## Betting simulation vs closing lines at -110 (2025-26)

| market | edge threshold | bets | win % | ROI |
|---|---|---|---|---|
| spread | 0% | 415 | 47.0% | -10.3% |
| spread | 3% | 292 | 49.0% | -6.5% |
| spread | 5% | 220 | 49.1% | -6.3% |
| spread | 8% | 134 | 50.0% | -4.5% |
| total | 0% | 451 | 49.4% | -5.6% |
| total | 3% | 363 | 51.8% | -1.1% |
| total | 5% | 308 | 50.3% | -3.9% |
| total | 8% | 218 | 54.1% | +3.3% |

Break-even at -110 is 52.4%. Closing lines are the sharpest benchmark; beating openers or soft books is easier than this.