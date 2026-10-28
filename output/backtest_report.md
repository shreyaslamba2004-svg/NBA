# Backtest: trained through 2023-24, noise calibrated on 2024-25, tested on 2025-26

## Player projections (2025-26, every player-game, n=28328)

| stat | model MAE | baseline MAE (recent avg) | improvement |
|---|---|---|---|
| minutes | 4.36 | 5.13 | 15.0% |
| pts | 4.34 | 4.59 | 5.3% |
| reb | 1.81 | 1.89 | 4.1% |
| ast | 1.30 | 1.34 | 2.9% |
| fg3m | 0.87 | 0.88 | 1.4% |
| stl | 0.71 | 0.72 | 1.0% |
| blk | 0.51 | 0.50 | -1.2% |
| tov | 0.87 | 0.89 | 2.6% |

## Games (2025-26, n=1265; 505 with closing lines)

Calibrated noise: margin sd 14.07, total sd 18.37

| metric | model (all games) | model (games w/ lines) | closing line |
|---|---|---|---|
| Margin MAE | 11.30 | 10.94 | 10.60 |
| Total MAE | 14.99 | 15.53 | 14.93 |
| Total MAE (bottom-up from players) | 15.35 | | |

Win probability log-loss: model 0.5896 (all), model 0.6221 vs no-vig closing moneyline 0.6167 (same 505 games). Brier: model 0.2166 vs market 0.2140.

Win-prob calibration:

| bucket | games | predicted | actual |
|---|---|---|---|
| (0.0, 0.2] | 30.0 | 0.167 | 0.033 |
| (0.2, 0.35] | 150.0 | 0.286 | 0.227 |
| (0.35, 0.5] | 304.0 | 0.433 | 0.401 |
| (0.5, 0.65] | 332.0 | 0.576 | 0.575 |
| (0.65, 0.8] | 332.0 | 0.720 | 0.741 |
| (0.8, 1.0] | 117.0 | 0.848 | 0.906 |

## Betting simulation vs closing lines at -110 (2025-26)

| market | edge threshold | bets | win % | ROI |
|---|---|---|---|---|
| spread | 0% | 421 | 47.0% | -10.2% |
| spread | 3% | 304 | 50.0% | -4.5% |
| spread | 5% | 229 | 50.2% | -4.1% |
| spread | 8% | 146 | 51.4% | -1.9% |
| total | 0% | 445 | 49.4% | -5.6% |
| total | 3% | 353 | 49.9% | -4.8% |
| total | 5% | 292 | 52.1% | -0.6% |
| total | 8% | 217 | 52.1% | -0.6% |

Break-even at -110 is 52.4%. Closing lines are the sharpest benchmark; beating openers or soft books is easier than this.