# Model monitor (2026-11-09)

## Probability accuracy (lower logloss is better)

| market     | window      |   bets graded |   logloss model |   logloss market (no-vig) |   logloss blend |
|:-----------|:------------|--------------:|----------------:|--------------------------:|----------------:|
| game lines | last 7 days |          2600 |          0.6406 |                    0.6234 |          0.6234 |
| game lines | season      |          5170 |          0.6738 |                    0.6371 |          0.6371 |
| props      | last 7 days |         33524 |          0.5153 |                    0.5108 |          0.5104 |
| props      | season      |         65070 |          0.52   |                    0.5122 |          0.512  |

## Best bets (EV ≥ 5%, odds ≤ 4) as listed in TODAY.md

CLV compares the price you'd have taken with the final no-vig market before tip. Consistently positive CLV is the best early sign of a real edge; ROI is noisy for months.

| market     | window      |   bets |   win % |   ROI % (1 unit each) |   avg CLV % |   beat closing % |
|:-----------|:------------|-------:|--------:|----------------------:|------------:|-----------------:|
| game lines | last 7 days |      5 |    20   |                 -49   |        -3.2 |             20   |
| props      | last 7 days |     12 |    33.3 |                 -24   |         9.4 |             50   |
| game lines | season      |     51 |     7.8 |                 -82.9 |        -6.2 |              3.9 |
| props      | season      |     57 |    33.3 |                   1.4 |         3   |             49.1 |

Blend weights refit from logged results: props 0.132, game_logged 0.0

## Alerts

- Best bets have negative average CLV over 4 weeks (-1.3%, n=108).

## Weekly retrain

Safety check (model trained on past seasons, tested on this season): games 98
Retrained on all games through 2026-11-09 and saved.
