# Model monitor (2026-11-02)

## Probability accuracy (lower logloss is better)

| market     | window      |   bets graded |   logloss model |   logloss market (no-vig) |   logloss blend |
|:-----------|:------------|--------------:|----------------:|--------------------------:|----------------:|
| game lines | last 7 days |          2678 |          0.7044 |                    0.6505 |          0.6506 |
| game lines | season      |          2678 |          0.7044 |                    0.6505 |          0.6506 |
| props      | last 7 days |         33229 |          0.5271 |                    0.5156 |          0.5156 |
| props      | season      |         33229 |          0.5271 |                    0.5156 |          0.5156 |

## Best bets (EV ≥ 5%, odds ≤ 4) as listed in TODAY.md

CLV compares the price you'd have taken with the final no-vig market before tip. Consistently positive CLV is the best early sign of a real edge; ROI is noisy for months.

| market     | window      |   bets |   win % |   ROI % (1 unit each) |   avg CLV % |   beat closing % |
|:-----------|:------------|-------:|--------:|----------------------:|------------:|-----------------:|
| game lines | last 7 days |     46 |     6.5 |                 -86.6 |        -6.5 |              2.2 |
| props      | last 7 days |     51 |    31.4 |                  -0.5 |         1.3 |             45.1 |
| game lines | season      |     46 |     6.5 |                 -86.6 |        -6.5 |              2.2 |
| props      | season      |     51 |    31.4 |                  -0.5 |         1.3 |             45.1 |

Blend weights refit from logged results: props 0.075, game_logged 0.0

## Weekly retrain

Safety check (model trained on past seasons, tested on this season): games 44
Retrained on all games through 2026-11-02 and saved.
