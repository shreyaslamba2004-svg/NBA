# Model monitor (2026-11-16)

## Probability accuracy (lower logloss is better)

| market     | window      |   bets graded |   logloss model |   logloss market (no-vig) |   logloss blend |
|:-----------|:------------|--------------:|----------------:|--------------------------:|----------------:|
| game lines | last 7 days |          4129 |          0.6628 |                    0.6341 |          0.6341 |
| game lines | season      |          9033 |          0.6742 |                    0.6391 |          0.6392 |
| props      | last 7 days |         56532 |          0.5362 |                    0.5286 |          0.528  |
| props      | season      |        117463 |          0.5273 |                    0.5198 |          0.5194 |

## Best bets (EV ≥ 5%, odds ≤ 4) as listed in TODAY.md

CLV compares the price you'd have taken with the final no-vig market before tip. Consistently positive CLV is the best early sign of a real edge; ROI is noisy for months.

| market     | window      |   bets |   win % |   ROI % (1 unit each) |   avg CLV % |   beat closing % |
|:-----------|:------------|-------:|--------:|----------------------:|------------:|-----------------:|
| game lines | last 7 days |     12 |    41.7 |                  -4.3 |         1.1 |             50   |
| props      | last 7 days |     18 |    66.7 |                  51.4 |        10.3 |             94.4 |
| game lines | season      |     63 |    14.3 |                 -67.9 |        -4.8 |             12.7 |
| props      | season      |     73 |    41.1 |                  12.7 |         4.5 |             58.9 |

Blend weights refit from logged results: props 0.154, game_logged 0.0

## Weekly retrain

Safety check (model trained on past seasons, tested on this season): games 149, minutes MAE 4.43, pts MAE 4.42, margin MAE 11.77
Retrained on all games through 2026-11-16 and saved.
