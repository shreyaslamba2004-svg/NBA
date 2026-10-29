# Model health

Rebuilt 2026-10-29 by the nightly grading run. Back to [TODAY.md](TODAY.md).

## Verdict: **TOO EARLY**

Only 1 graded game day(s) so far; a verdict needs 5.

How to read this: the model is judged against a simple rule anyone could use, each player's average over his last 10 games. "% better" is how much smaller the model's average miss is. Watch the trend, not single days: one game day is mostly noise.

## Projection accuracy (players the model had at 90%+ to play)

| window                      |   game days |   players |   minutes miss |   minutes % better than last-10 |   minutes lean (+ = too high) |   points miss |   points % better than last-10 |   points lean (+ = too high) |
|:----------------------------|------------:|----------:|---------------:|--------------------------------:|------------------------------:|--------------:|-------------------------------:|-----------------------------:|
| Last 7 days                 |           1 |       164 |           4.99 |                            11.1 |                          1.74 |          5.21 |                            4.1 |                         1.23 |
| Last 30 days                |           1 |       164 |           4.99 |                            11.1 |                          1.74 |          5.21 |                            4.1 |                         1.23 |
| Season                      |           1 |       164 |           4.99 |                            11.1 |                          1.74 |          5.21 |                            4.1 |                         1.23 |
| Backtest (held-out 2025-26) |             |           |                |                            15.5 |                               |               |                            5.4 |                              |

Live should sit near the backtest line. Well below it for weeks means the model is doing worse on new games than it did in testing (overfitting or something broke).

## Best bets (EV ≥ 5%, odds ≤ 4)

Every bet that showed in TODAY.md's main best-bets table at any point in the day, graded at the first price it showed at (the sheet changes through the day, so this is more than the final pre-tip list).

| window       |   bets |   won |   profit (units) |   ROI % |   avg CLV % |   beat closing % |
|:-------------|-------:|------:|-----------------:|--------:|------------:|-----------------:|
| Last 7 days  |     19 |     9 |             1.95 |    10.3 |        -2.5 |             15.8 |
| Last 30 days |     19 |     9 |             1.95 |    10.3 |        -2.5 |             15.8 |
| Season       |     19 |     9 |             1.95 |    10.3 |        -2.5 |             15.8 |

CLV (closing-line value) compares the price taken with the final no-vig market price before tip. Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings for months.

## Multis (top 3 per price band)

| window       |   multis |   won |   model expected to win |   profit (units, at multiplied leg prices) |
|:-------------|---------:|------:|------------------------:|-------------------------------------------:|
| Last 7 days  |       10 |     4 |                     5.1 |                                      -1.91 |
| Last 30 days |       10 |     4 |                     5.1 |                                      -1.91 |
| Season       |       10 |     4 |                     5.1 |                                      -1.91 |

If "won" keeps landing near "expected", the multi probabilities are honest. Profit uses the legs' prices multiplied together; the bookie's actual SGM price is usually lower.

## Day by day (last 30)

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|
| 2026-10-28 |      12 |       164 | 4.99 / 5.61                      | 5.21 / 5.43                     |          1.23 |
