# Model monitor (2026-11-24)

## Probability accuracy (lower logloss is better)

| market     | window      |   bets graded |   logloss model |   logloss market (no-vig) |   logloss blend |
|:-----------|:------------|--------------:|----------------:|--------------------------:|----------------:|
| game lines | last 7 days |          3664 |          0.7306 |                    0.6827 |          0.6827 |
| game lines | season      |         12871 |          0.6895 |                    0.6523 |          0.6523 |
| props      | last 7 days |         50177 |          0.5393 |                    0.5327 |          0.532  |
| props      | season      |        169254 |          0.5309 |                    0.5236 |          0.5232 |

## Best bets (EV ≥ 5%, odds ≤ 4) as listed in TODAY.md

CLV compares the price you'd have taken with the final no-vig market before tip. Consistently positive CLV is the best early sign of a real edge; ROI is noisy for months.

| market     | window      |   bets |   win % |   ROI % (1 unit each) |   avg CLV % |   beat closing % |
|:-----------|:------------|-------:|--------:|----------------------:|------------:|-----------------:|
| game lines | last 7 days |      9 |    33.3 |                 -29.9 |         3.6 |             66.7 |
| props      | last 7 days |     19 |    26.3 |                 -46.8 |         8.9 |             84.2 |
| game lines | season      |     72 |    16.7 |                 -63.2 |        -3.8 |             19.4 |
| props      | season      |     92 |    38   |                   0.4 |         5.4 |             64.1 |

Blend weights refit from logged results: props 0.181, game_logged 0.0

## Weekly retrain

Safety check (model trained on past seasons, tested on this season): games 200, minutes MAE 4.36, pts MAE 4.41, margin MAE 11.43
Retrained on all games through 2026-11-24 and saved.
