# Model health

Rebuilt 2026-10-30 by the nightly grading run. Back to [TODAY.md](TODAY.md).

## Verdict: **TOO EARLY**

Only 2 graded game day(s) so far; a verdict needs 5.

How to read this: the model is judged against a simple rule anyone could use, each player's average over his last 10 games. "% better" is how much smaller the model's average miss is. Watch the trend, not single days: one game day is mostly noise.

## Projection accuracy (players the model had at 90%+ to play)

| window                      |   game days |   players |   minutes miss |   minutes % better than last-10 |   minutes lean (+ = too high) |   points miss |   points % better than last-10 |   points lean (+ = too high) |
|:----------------------------|------------:|----------:|---------------:|--------------------------------:|------------------------------:|--------------:|-------------------------------:|-----------------------------:|
| Last 7 days                 |           2 |       217 |           4.96 |                            12.7 |                          1.77 |          5.42 |                            2.5 |                          1.2 |
| Last 30 days                |           2 |       217 |           4.96 |                            12.7 |                          1.77 |          5.42 |                            2.5 |                          1.2 |
| Season                      |           2 |       217 |           4.96 |                            12.7 |                          1.77 |          5.42 |                            2.5 |                          1.2 |
| Backtest (held-out 2025-26) |             |           |                |                            15.4 |                               |               |                            5.4 |                              |

Live should sit near the backtest line. Well below it for weeks means the model is doing worse on new games than it did in testing (overfitting or something broke).

## Best bets (EV ≥ 5%, odds ≤ 4)

**Main record: the final list.** The bets still in TODAY.md's best-bets table on the last update before each game's tip (after lineups and injury news), graded at the price shown then.

| window       |   bets |   won |   profit (units) |   ROI % |
|:-------------|-------:|------:|-----------------:|--------:|
| Last 7 days  |      7 |     4 |             3.95 |    56.4 |
| Last 30 days |      7 |     4 |             3.95 |    56.4 |
| Season       |      7 |     4 |             3.95 |    56.4 |

**Any time in the day (secondary).** Every bet that showed in the table at any point, graded at the first price it showed at. Bets that dropped off before tip (news, price moves) count here.

| window       |   bets |   won |   profit (units) |   ROI % |   avg CLV % |   beat closing % |
|:-------------|-------:|------:|-----------------:|--------:|------------:|-----------------:|
| Last 7 days  |     36 |    20 |            14.17 |    39.4 |         2.7 |               25 |
| Last 30 days |     36 |    20 |            14.17 |    39.4 |         2.7 |               25 |
| Season       |     36 |    20 |            14.17 |    39.4 |         2.7 |               25 |

CLV (closing-line value) compares the price taken with the final no-vig market price before tip. Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings for months.

## Best player props per game (top 3 main lines)

The "Best player props" box in each game's section of TODAY.md: up to 3 main-line props per game with positive EV, no news flag and offered at Sportsbet, as listed on the last update before tip, graded at the price shown then. These include edges under 5%, so expect a thinner margin than best bets.

| window       |   bets |   won |   profit (units) |   ROI % |
|:-------------|-------:|------:|-----------------:|--------:|
| Last 7 days  |     15 |     5 |            -5.42 |   -36.1 |
| Last 30 days |     15 |     5 |            -5.42 |   -36.1 |
| Season       |     15 |     5 |            -5.42 |   -36.1 |

## Multis (top 3 per price band)

| window       |   multis |   won |   model expected to win |   profit (units, at multiplied leg prices) |
|:-------------|---------:|------:|------------------------:|-------------------------------------------:|
| Last 7 days  |       22 |     6 |                    11.1 |                                      -9.79 |
| Last 30 days |       22 |     6 |                    11.1 |                                      -9.79 |
| Season       |       22 |     6 |                    11.1 |                                      -9.79 |

If "won" keeps landing near "expected", the multi probabilities are honest. Profit uses the legs' prices multiplied together; the bookie's actual SGM price is usually lower.

## Day by day (last 30)

Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising count means something in the inputs is going wrong.

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean | sanity flags   |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|:---------------|
| 2026-10-29 |       3 |        53 | 4.86 / 5.88                      | 6.06 / 5.94                     |          1.13 | 0 (none)       |
| 2026-10-28 |      12 |       164 | 4.99 / 5.61                      | 5.21 / 5.43                     |          1.23 |                |
