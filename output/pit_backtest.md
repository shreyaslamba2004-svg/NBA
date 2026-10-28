# Point-in-time backtest

Backtest bundle trained through 2023-24. Point-in-time rows rebuild every absence feature from the ~5pm ET official injury report (Out/Doubtful absent, Questionable/Probable available), so late scratches are surprises, exactly as live.

Report matching: report rows (Out/Doubtful) 21267, matched to a player 21023, games covered 2606

| season   | availability from             |   games |   margin MAE |   total MAE |   closing spread MAE |   ATS win % |   win logloss model |   win logloss market |
|:---------|:------------------------------|--------:|-------------:|------------:|---------------------:|------------:|--------------------:|---------------------:|
| 2024-25  | box score (knows who played)  |    1266 |       10.9   |      14.686 |               10.643 |      50.08  |               0.597 |                0.585 |
| 2024-25  | injury report (point-in-time) |    1266 |       11.025 |      14.669 |               10.643 |      47.91  |               0.605 |                0.585 |
| 2025-26  | box score (knows who played)  |    1265 |       11.283 |      15.032 |               10.596 |      45.129 |               0.623 |                0.617 |
| 2025-26  | injury report (point-in-time) |    1265 |       11.344 |      15.068 |               10.596 |      46.72  |               0.624 |                0.617 |

## Model/market blend (fit on 2024-25, tested on 2025-26)

Weight = share given to the model; the rest goes to the no-vig closing market. Lower logloss is better.

| market    |   fit games |   test games |   fitted model weight |   test logloss market only |   test logloss blend |   test logloss model only |
|:----------|------------:|-------------:|----------------------:|---------------------------:|---------------------:|--------------------------:|
| moneyline |        1266 |          505 |                     0 |                     0.6167 |               0.6167 |                    0.6245 |
| spread    |        1244 |          503 |                     0 |                     0.6931 |               0.6931 |                    0.7155 |
| total     |        1252 |          505 |                     0 |                     0.6931 |               0.6931 |                    0.7189 |

Saved to models/blend.json and used by nbamodel/edges.py.
