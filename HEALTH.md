# Model health

Rebuilt 2026-10-31 by the nightly grading run. Back to [TODAY.md](TODAY.md).

## Verdict: **TOO EARLY**

Only 3 graded game day(s) so far; a verdict needs 5.

How to read this: the model is judged against a simple rule anyone could use, each player's average over his last 10 games. "% better" is how much smaller the model's average miss is. Watch the trend, not single days: one game day is mostly noise.

## Projection accuracy (players the model had at 90%+ to play)

| window                      |   game days |   players |   minutes miss |   minutes % better than last-10 |   minutes lean (+ = too high) |   points miss |   points % better than last-10 |   points lean (+ = too high) |
|:----------------------------|------------:|----------:|---------------:|--------------------------------:|------------------------------:|--------------:|-------------------------------:|-----------------------------:|
| Last 7 days                 |           3 |       393 |           4.55 |                            17   |                          1.29 |          5.21 |                            2.8 |                         0.89 |
| Last 30 days                |           3 |       393 |           4.55 |                            17   |                          1.29 |          5.21 |                            2.8 |                         0.89 |
| Season                      |           3 |       393 |           4.55 |                            17   |                          1.29 |          5.21 |                            2.8 |                         0.89 |
| Backtest (held-out 2025-26) |             |           |                |                            15.4 |                               |               |                            5.4 |                              |

Live should sit near the backtest line. Well below it for weeks means the model is doing worse on new games than it did in testing (overfitting or something broke).

## Best bets (EV ≥ 5%, odds ≤ 4)

**Main record: the final list.** The bets still in TODAY.md's best-bets table on the last update before each game's tip (after lineups and injury news), graded at the price shown then.

Each table shows two ways of counting: units at a flat 1-unit stake on every bet (so results compare cleanly), and profit at the sheet's suggested stake, the quarter-Kelly % of bankroll capped at 2% that TODAY.md shows on every bet. ROI (sheet stakes) is that profit divided by the total staked. Rows are the last 7 days, last 30 days and whole season; a longer period only gets its own row once it holds more bets than the shorter one.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Since 28 Oct |      9 |     5 |             3.95 |           43.9 |                   8.7 |                                  5.55 |                   64.1 |

<details><summary>Every final-list bet (9)</summary>

| date (US)   | bet                                | game      | book        |   odds | EV    | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-----------------------------------|:----------|:------------|-------:|:------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-10-30  | Jarace Walker PTS over 10.5 (11+)  | IND @ MIA | pointsbetau |   2    | +7.3% | 1.8%          | won      |             1    |                           1.82 |
| 2026-10-30  | Pascal Siakam AST over 5.5 (6+)    | IND @ MIA | draftkings  |   3.66 | +6.6% | 0.6%          | lost     |            -1    |                          -0.62 |
| 2026-10-29  | Kingston Flemings PTS under 8.5    | CLE @ ATL | tab         |   2    | +8.5% | 2.0%          | won      |             1    |                           2    |
| 2026-10-29  | Damian Lillard AST over 5.5 (6+)   | MEM @ POR | draftkings  |   3.87 | +6.4% | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-10-29  | Ja Morant AST over 7.5 (8+)        | MEM @ POR | draftkings  |   3.25 | +5.4% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-28  | Darius Garland PTS over 29.5 (30+) | LAL @ LAC | draftkings  |   3.67 | +5.8% | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-10-28  | Jarace Walker REB over 6.5 (7+)    | PHI @ IND | draftkings  |   3.43 | +5.8% | 0.6%          | won      |             2.43 |                           1.46 |
| 2026-10-28  | IND +5.5                           | PHI @ IND | unibet      |   1.95 | +5.4% | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-28  | Pascal Siakam PRA over 39.5 (40+)  | PHI @ IND | draftkings  |   3.57 | +5.0% | 0.5%          | won      |             2.57 |                           1.26 |

</details>

## Long shots (EV ≥ 5%, odds above 4)

TODAY.md's long-shot table, graded the same way: the final pre-tip list at the price shown then, 1 unit flat. Expect long losing runs; judge it over hundreds of bets.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Since 28 Oct |     75 |     5 |            10.76 |           14.3 |                  28.8 |                                 11.27 |                   39.2 |

<details><summary>Every long shot (75)</summary>

| date (US)   | bet                                    | game      | book       |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------------|:----------|:-----------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-10-30  | Quenton Jackson PA over 24.5 (25+)     | IND @ MIA | draftkings |  26    | +47.6% | 0.5%          | won      |            25    |                          12    |
| 2026-10-30  | Quenton Jackson PR over 19.5 (20+)     | IND @ MIA | draftkings |  13.8  | +42.4% | 0.8%          | won      |            12.8  |                          10.62 |
| 2026-10-30  | Quenton Jackson AST over 7.5 (8+)      | IND @ MIA | draftkings |  17.6  | +41.6% | 0.6%          | lost     |            -1    |                          -0.63 |
| 2026-10-30  | Quenton Jackson PRA over 29.5 (30+)    | IND @ MIA | draftkings |  27    | +40.5% | 0.4%          | lost     |            -1    |                          -0.39 |
| 2026-10-30  | Kevin Durant PRA over 54.5 (55+)       | HOU @ DAL | draftkings |  21    | +35.5% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-10-30  | Quenton Jackson PTS over 19.5 (20+)    | IND @ MIA | draftkings |  30    | +35.1% | 0.3%          | won      |            29    |                           8.7  |
| 2026-10-30  | Kevin Durant PA over 49.5 (50+)        | HOU @ DAL | draftkings |  27    | +32.9% | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-10-30  | Kevin Durant AST over 9.5 (10+)        | HOU @ DAL | draftkings |  26    | +28.2% | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-10-30  | Kevin Durant PRA over 49.5 (50+)       | HOU @ DAL | draftkings |  11.2  | +27.7% | 0.7%          | lost     |            -1    |                          -0.68 |
| 2026-10-30  | Pascal Siakam PA over 49.5 (50+)       | IND @ MIA | draftkings |  24    | +24.9% | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-10-30  | Pascal Siakam PTS over 44.5 (45+)      | IND @ MIA | draftkings |  27    | +24.4% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-10-30  | Kevin Durant PR over 49.5 (50+)        | HOU @ DAL | draftkings |  20.8  | +24.0% | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-10-30  | Pascal Siakam PR over 49.5 (50+)       | IND @ MIA | draftkings |  16    | +23.5% | 0.4%          | lost     |            -1    |                          -0.39 |
| 2026-10-30  | Kevin Durant PTS over 44.5 (45+)       | HOU @ DAL | draftkings |  28    | +23.3% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-10-30  | Pascal Siakam PA over 44.5 (45+)       | IND @ MIA | draftkings |  13.2  | +22.9% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-10-30  | Pascal Siakam PR over 54.5 (55+)       | IND @ MIA | draftkings |  27    | +22.1% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-30  | Kevin Durant PTS over 39.5 (40+)       | HOU @ DAL | draftkings |  14    | +19.0% | 0.4%          | lost     |            -1    |                          -0.37 |
| 2026-10-30  | Pascal Siakam PTS over 39.5 (40+)      | IND @ MIA | draftkings |  13.2  | +18.7% | 0.4%          | lost     |            -1    |                          -0.38 |
| 2026-10-30  | Pascal Siakam AST over 7.5 (8+)        | IND @ MIA | draftkings |  11.2  | +16.6% | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-10-30  | DeMar DeRozan AST over 5.5 (6+)        | DEN @ PHX | draftkings |  10.8  | +16.5% | 0.4%          | lost     |            -1    |                          -0.42 |
| 2026-10-30  | Kevin Durant PR over 44.5 (45+)        | HOU @ DAL | draftkings |  10.3  | +16.2% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-10-30  | DeMar DeRozan PRA over 29.5 (30+)      | DEN @ PHX | draftkings |  13.2  | +14.1% | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-10-30  | Pascal Siakam PR over 44.5 (45+)       | IND @ MIA | draftkings |   7.9  | +13.5% | 0.5%          | lost     |            -1    |                          -0.49 |
| 2026-10-30  | Bam Adebayo PR over 44.5 (45+)         | IND @ MIA | draftkings |  18.2  | +12.8% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-10-30  | Yaxel Lendeborg PRA over 44.5 (45+)    | LAL @ GSW | draftkings |  12.8  | +12.7% | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-10-29  | Zion Williamson PTS over 34.5 (35+)    | SAC @ NOP | draftkings |  19.6  | +44.5% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-29  | Jrue Holiday AST over 8.5 (9+)         | MEM @ POR | draftkings |  20.8  | +32.1% | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-10-29  | Jrue Holiday AST over 7.5 (8+)         | MEM @ POR | draftkings |  12.2  | +29.3% | 0.7%          | lost     |            -1    |                          -0.65 |
| 2026-10-29  | Ja Morant AST over 11.5 (12+)          | MEM @ POR | draftkings |  20.8  | +25.2% | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-10-29  | Ja Morant AST over 10.5 (11+)          | MEM @ POR | draftkings |  13.4  | +23.2% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-10-29  | Jrue Holiday AST over 9.5 (10+)        | MEM @ POR | draftkings |  30    | +22.1% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-10-29  | Damian Lillard AST over 8.5 (9+)       | MEM @ POR | draftkings |  21    | +19.0% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-10-29  | Jrue Holiday REB over 7.5 (8+)         | MEM @ POR | draftkings |  12.8  | +18.1% | 0.4%          | lost     |            -1    |                          -0.38 |
| 2026-10-29  | Ja Morant AST over 12.5 (13+)          | MEM @ POR | draftkings |  29    | +17.6% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-29  | Ja Morant AST over 9.5 (10+)           | MEM @ POR | draftkings |   8.2  | +17.0% | 0.6%          | lost     |            -1    |                          -0.59 |
| 2026-10-29  | Jrue Holiday PRA over 39.5 (40+)       | MEM @ POR | draftkings |  27    | +16.4% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-29  | Jrue Holiday REB over 6.5 (7+)         | MEM @ POR | draftkings |   7.5  | +16.3% | 0.6%          | lost     |            -1    |                          -0.63 |
| 2026-10-29  | Damian Lillard AST over 7.5 (8+)       | MEM @ POR | draftkings |  11.8  | +16.2% | 0.4%          | lost     |            -1    |                          -0.38 |
| 2026-10-29  | Jrue Holiday PRA over 34.5 (35+)       | MEM @ POR | draftkings |  16.4  | +16.0% | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-10-29  | Jrue Holiday REB over 8.5 (9+)         | MEM @ POR | draftkings |  21    | +16.0% | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-10-29  | Jrue Holiday PRA over 29.5 (30+)       | MEM @ POR | draftkings |   7.4  | +14.4% | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-10-29  | Precious Achiuwa PTS over 19.5 (20+)   | SAC @ NOP | draftkings |   9.6  | +13.6% | 0.4%          | won      |             8.6  |                           3.35 |
| 2026-10-29  | Derik Queen PTS over 24.5 (25+)        | SAC @ NOP | draftkings |  22    | +13.2% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-29  | Derik Queen REB over 13.5 (14+)        | SAC @ NOP | draftkings |  14.6  | +12.5% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-10-29  | Derik Queen REB over 12.5 (13+)        | SAC @ NOP | draftkings |   9.7  | +11.9% | 0.3%          | lost     |            -1    |                          -0.34 |
| 2026-10-29  | Damian Lillard AST over 6.5 (7+)       | MEM @ POR | draftkings |   6.69 | +11.7% | 0.5%          | lost     |            -1    |                          -0.51 |
| 2026-10-29  | Precious Achiuwa PTS over 17.5 (18+)   | SAC @ NOP | draftkings |   6.36 | +11.4% | 0.5%          | won      |             5.36 |                           2.84 |
| 2026-10-29  | Ja Morant AST over 8.5 (9+)            | MEM @ POR | draftkings |   5.04 | +10.5% | 0.7%          | lost     |            -1    |                          -0.65 |
| 2026-10-29  | Trey Murphy III PRA over 44.5 (45+)    | SAC @ NOP | draftkings |  19.2  | +10.2% | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-10-29  | Derik Queen PTS over 19.5 (20+)        | SAC @ NOP | draftkings |   7.9  | +9.9%  | 0.4%          | lost     |            -1    |                          -0.36 |
| 2026-10-28  | Darius Garland PRA over 54.5 (55+)     | LAL @ LAC | draftkings |  22    | +32.8% | 0.4%          | lost     |            -1    |                          -0.39 |
| 2026-10-28  | Darius Garland PTS over 39.5 (40+)     | LAL @ LAC | draftkings |  16.6  | +30.0% | 0.5%          | lost     |            -1    |                          -0.48 |
| 2026-10-28  | Darius Garland PRA over 49.5 (50+)     | LAL @ LAC | draftkings |  12    | +27.5% | 0.6%          | lost     |            -1    |                          -0.62 |
| 2026-10-28  | Darius Garland PTS over 44.5 (45+)     | LAL @ LAC | draftkings |  29    | +27.4% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-10-28  | Pascal Siakam PRA over 54.5 (55+)      | PHI @ IND | draftkings |  24    | +27.1% | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-10-28  | Kevin Durant AST over 8.5 (9+)         | HOU @ MIL | draftkings |  18.4  | +25.1% | 0.4%          | lost     |            -1    |                          -0.36 |
| 2026-10-28  | Pascal Siakam PRA over 49.5 (50+)      | PHI @ IND | draftkings |  13.6  | +23.9% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-10-28  | Kevin Durant AST over 7.5 (8+)         | HOU @ MIL | draftkings |  10.9  | +23.8% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-28  | Saddiq Bey PTS over 24.5 (25+)         | DEN @ NOP | draftkings |  18.6  | +22.9% | 0.3%          | lost     |            -1    |                          -0.33 |
| 2026-10-28  | Brook Lopez PTS over 24.5 (25+)        | LAL @ LAC | draftkings |  24    | +20.6% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-10-28  | Kevin Durant AST over 9.5 (10+)        | HOU @ MIL | draftkings |  29    | +20.4% | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-10-28  | Darius Garland PTS over 34.5 (35+)     | LAL @ LAC | draftkings |   7.7  | +17.2% | 0.6%          | lost     |            -1    |                          -0.64 |
| 2026-10-28  | Saddiq Bey PTS over 19.5 (20+)         | DEN @ NOP | draftkings |   7.3  | +17.0% | 0.7%          | lost     |            -1    |                          -0.68 |
| 2026-10-28  | Saddiq Bey PR over 29.5 (30+)          | DEN @ NOP | draftkings |  17.8  | +17.0% | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-10-28  | Saddiq Bey PR over 24.5 (25+)          | DEN @ NOP | draftkings |   7.9  | +16.6% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-28  | Pascal Siakam PRA over 44.5 (45+)      | PHI @ IND | draftkings |   6.82 | +14.0% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-28  | Jarace Walker REB over 9.5 (10+)       | PHI @ IND | draftkings |  13    | +13.9% | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-10-28  | Daniss Jenkins REB over 5.5 (6+)       | CHA @ DET | draftkings |   9.9  | +13.7% | 0.4%          | lost     |            -1    |                          -0.38 |
| 2026-10-28  | Darius Garland PRA over 44.5 (45+)     | LAL @ LAC | draftkings |   5.84 | +13.5% | 0.7%          | lost     |            -1    |                          -0.7  |
| 2026-10-28  | Isaiah Hartenstein REB over 18.5 (19+) | OKC @ DAL | draftkings |  21    | +12.5% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-28  | Jarace Walker REB over 8.5 (9+)        | PHI @ IND | draftkings |   8.3  | +12.1% | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-10-28  | Darius Garland PR over 44.5 (45+)      | LAL @ LAC | draftkings |  15    | +12.0% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-28  | Daniss Jenkins REB over 6.5 (7+)       | CHA @ DET | draftkings |  17.6  | +11.9% | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-10-28  | Jarace Walker REB over 10.5 (11+)      | PHI @ IND | draftkings |  19.8  | +11.8% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-28  | Keyonte George AST over 12.5 (13+)     | SAS @ UTA | draftkings |  23    | +11.8% | 0.1%          | lost     |            -1    |                          -0.13 |

</details>

## Best bets: any time in the day (secondary)

**Any time in the day.** Every bet that showed in the table at any point, graded at the first price it showed at. Bets that dropped off before tip (news, price moves) count here.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |   avg CLV % |   beat closing % |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|------------:|-----------------:|
| Since 28 Oct |     33 |    15 |            12.64 |           38.3 |                    17 |                                  6.78 |                     40 |        -0.3 |             30.3 |

<details><summary>Every bet that showed at any time (odds = first price shown) (33)</summary>

| date (US)   | bet                                  | game      | book          |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-------------------------------------|:----------|:--------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-10-30  | Khaman Maluach PTS under 7.5         | DEN @ PHX | pointsbetau   |   2.05 | +11.5% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-30  | Jarace Walker PTS over 10.5 (11+)    | IND @ MIA | pointsbetau   |   2    | +7.3%  | 1.8%          | won      |             1    |                           1.82 |
| 2026-10-30  | Pascal Siakam AST over 5.5 (6+)      | IND @ MIA | draftkings    |   3.52 | +6.6%  | 0.6%          | lost     |            -1    |                          -0.62 |
| 2026-10-30  | Naz Reid PTS under 17.5              | CHA @ WAS | pointsbetau   |   2    | +5.8%  | 1.5%          | won      |             1    |                           1.45 |
| 2026-10-30  | Payton Pritchard PTS under 15.5      | CHI @ BOS | unibet        |   2.06 | +4.9%  | 1.2%          | lost     |            -1    |                          -1.16 |
| 2026-10-30  | Aaron Gordon PTS under 14.5          | DEN @ PHX | pointsbetau   |   2    | +4.7%  | 1.2%          | lost     |            -1    |                          -1.18 |
| 2026-10-30  | Jarace Walker AST over 3.5 (4+)      | IND @ MIA | draftkings    |   3.5  | +3.2%  | 0.4%          | won      |             2.5  |                           0.9  |
| 2026-10-30  | Scottie Barnes AST over 7.5 (8+)     | ORL @ TOR | draftkings    |   4    | +0.1%  | 0.0%          | lost     |            -1    |                          -0.01 |
| 2026-10-30  | IND to win                           | IND @ MIA | draftkings    |   3.6  | -3.2%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-30  | BKN to win                           | DET @ BKN | draftkings    |   3.5  | -3.3%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-30  | PHI to win                           | NYK @ PHI | draftkings    |   2.3  | -4.0%  | 0.0%          | won      |             1.3  |                           0    |
| 2026-10-29  | Kingston Flemings PTS under 8.5      | CLE @ ATL | tab           |   2    | +8.5%  | 2.0%          | won      |             1    |                           2    |
| 2026-10-29  | Precious Achiuwa PTS over 14.5 (15+) | SAC @ NOP | draftkings    |   3.54 | +6.9%  | 0.7%          | won      |             2.54 |                           1.73 |
| 2026-10-29  | Damian Lillard AST over 5.5 (6+)     | MEM @ POR | draftkings    |   3.9  | +6.4%  | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-10-29  | Darius Acuff Jr. REB over 4.5 (5+)   | SAC @ NOP | draftkings    |   3.94 | +6.0%  | 0.5%          | won      |             2.94 |                           1.38 |
| 2026-10-29  | Ja Morant AST over 7.5 (8+)          | MEM @ POR | draftkings    |   3.28 | +5.4%  | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-29  | Derik Queen REB over 9.5 (10+)       | SAC @ NOP | draftkings    |   3.45 | +4.3%  | 0.5%          | lost     |            -1    |                          -0.48 |
| 2026-10-29  | Cam Spencer AST over 4.5 (5+)        | MEM @ POR | draftkings    |   3.8  | +2.5%  | 0.2%          | won      |             2.8  |                           0.7  |
| 2026-10-29  | Jeremiah Fears REB over 4.5 (5+)     | SAC @ NOP | draftkings    |   3.94 | -5.6%  | 0.0%          | won      |             2.94 |                           0    |
| 2026-10-28  | Darius Garland PTS over 29.5 (30+)   | LAL @ LAC | draftkings    |   3.67 | +5.8%  | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-10-28  | Jarace Walker REB over 6.5 (7+)      | PHI @ IND | draftkings    |   3.43 | +5.8%  | 0.6%          | won      |             2.43 |                           1.46 |
| 2026-10-28  | IND +5.5                             | PHI @ IND | unibet        |   1.95 | +5.4%  | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-28  | Pascal Siakam PRA over 39.5 (40+)    | PHI @ IND | draftkings    |   3.57 | +5.0%  | 0.5%          | won      |             2.57 |                           1.26 |
| 2026-10-28  | Scottie Barnes AST over 7.5 (8+)     | ORL @ TOR | draftkings    |   3.88 | +2.2%  | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-28  | Ace Bailey PR over 24.5 (25+)        | SAS @ UTA | draftkings    |   3.96 | +0.4%  | 0.1%          | won      |             2.96 |                           0.15 |
| 2026-10-28  | MIL to win                           | HOU @ MIL | betfair_ex_au |   3.76 | +0.3%  | 0.0%          | lost     |            -1    |                          -0.03 |
| 2026-10-28  | Ace Bailey PTS over 17.5 (18+)       | SAS @ UTA | draftkings    |   3.78 | -1.2%  | 0.0%          | won      |             2.78 |                           0    |
| 2026-10-28  | Total under 239.5                    | WAS @ CLE | playup        |   1.93 | -2.7%  | 0.0%          | won      |             0.93 |                           0    |
| 2026-10-28  | CHA +7.5                             | CHA @ DET | unibet        |   1.96 | -2.8%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | IND to win                           | PHI @ IND | betfair_ex_au |   2.8  | -4.0%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | CHA to win                           | CHA @ DET | unibet        |   3.45 | -4.2%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | ATL -2.5                             | MIA @ ATL | draftkings    |   1.98 | -4.5%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | ATL to win                           | MIA @ ATL | tab           |   1.8  | -4.6%  | 0.0%          | lost     |            -1    |                          -0    |

</details>

CLV (closing-line value) compares the price taken with the final no-vig market price before tip. Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings for months.

## Best player props per game (main lines)

The "Best player props" box in each game's section of TODAY.md: every main-line prop with positive EV, no news flag and offered at Sportsbet, as listed on the last update before tip, graded at the price shown then. These include edges under 5%, so expect a thinner margin than best bets.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Since 28 Oct |    114 |    42 |           -31.39 |          -27.5 |                  39.1 |                                 -4.93 |                  -12.6 |

<details><summary>Every graded game prop (114)</summary>

| date (US)   | bet                                        | game      | book        |   odds | EV    | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-------------------------------------------|:----------|:------------|-------:|:------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-10-30  | Jarace Walker PTS over 10.5 (11+)          | IND @ MIA | pointsbetau |   2    | +7.3% | 1.8%          | won      |             1    |                           1.82 |
| 2026-10-30  | Payton Pritchard PTS under 15.5            | CHI @ BOS | unibet      |   2.06 | +4.9% | 1.2%          | lost     |            -1    |                          -1.16 |
| 2026-10-30  | Miles Bridges PTS under 15.5               | DEN @ PHX | tab         |   1.95 | +4.8% | 1.3%          | lost     |            -1    |                          -1.26 |
| 2026-10-30  | Aaron Gordon PTS under 14.5                | DEN @ PHX | pointsbetau |   2    | +4.7% | 1.2%          | lost     |            -1    |                          -1.18 |
| 2026-10-30  | Mikel Brown Jr. PTS under 11.5             | DET @ BKN | unibet      |   1.89 | +4.4% | 1.2%          | won      |             0.89 |                           1.1  |
| 2026-10-30  | Norman Powell PTS under 19.5               | CHI @ BOS | unibet      |   1.93 | +4.2% | 1.1%          | won      |             0.93 |                           1.05 |
| 2026-10-30  | Pascal Siakam PTS over 23.5 (24+)          | IND @ MIA | pointsbetau |   1.95 | +3.8% | 1.0%          | lost     |            -1    |                          -1.01 |
| 2026-10-30  | Trae Young PTS under 19.5                  | CHA @ WAS | pointsbetau |   2    | +3.5% | 0.9%          | lost     |            -1    |                          -0.88 |
| 2026-10-30  | Andrew Nembhard PTS over 17.5 (18+)        | IND @ MIA | unibet      |   2    | +3.4% | 0.9%          | won      |             1    |                           0.86 |
| 2026-10-30  | Alex Sarr BLK over 1.5 (2+)                | CHA @ WAS | draftkings  |   2.79 | +3.1% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-10-30  | Kyshawn George PTS over 13.5 (14+)         | CHA @ WAS | pointsbetau |   2.15 | +3.1% | 0.7%          | lost     |            -1    |                          -0.67 |
| 2026-10-30  | Karl-Anthony Towns PTS under 19.5          | NYK @ PHI | pointsbetau |   2    | +3.0% | 0.7%          | lost     |            -1    |                          -0.74 |
| 2026-10-30  | Neemias Queta PTS under 8.5                | CHI @ BOS | pointsbetau |   2.05 | +2.7% | 0.6%          | lost     |            -1    |                          -0.63 |
| 2026-10-30  | Alex Sarr PTS over 10.5 (11+)              | CHA @ WAS | pointsbetau |   2.1  | +2.6% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-30  | Kentavious Caldwell-Pope PTS over 6.5 (7+) | NYK @ PHI | draftkings  |   1.92 | +2.5% | 0.7%          | lost     |            -1    |                          -0.68 |
| 2026-10-30  | Cooper Flagg PTS under 24.5                | HOU @ DAL | pointsbetau |   1.83 | +2.4% | 0.7%          | lost     |            -1    |                          -0.73 |
| 2026-10-30  | Paul George PTS under 20.5                 | CHI @ BOS | pointsbetau |   1.95 | +2.4% | 0.6%          | won      |             0.95 |                           0.6  |
| 2026-10-30  | Rudy Gobert PTS under 10.5                 | LAC @ MIN | tab         |   1.87 | +2.4% | 0.7%          | won      |             0.87 |                           0.59 |
| 2026-10-30  | Austin Reaves PTS under 22.5               | LAL @ GSW | sportsbet   |   2    | +2.4% | 0.6%          | won      |             1    |                           0.59 |
| 2026-10-30  | AJ Dybantsa PTS under 14.5                 | CHA @ WAS | unibet      |   1.94 | +2.1% | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-10-30  | Cooper Flagg PTS under 23.5                | HOU @ DAL | sportsbet   |   1.96 | +2.0% | 0.5%          | lost     |            -1    |                          -0.53 |
| 2026-10-30  | Brook Lopez PTS under 10.5                 | LAC @ MIN | tab         |   1.9  | +1.9% | 0.5%          | lost     |            -1    |                          -0.54 |
| 2026-10-30  | Julius Randle PTS under 19.5               | DET @ BKN | unibet      |   1.94 | +1.9% | 0.5%          | won      |             0.94 |                           0.48 |
| 2026-10-30  | Giannis Antetokounmpo PTS under 31.5       | IND @ MIA | sportsbet   |   1.9  | +1.8% | 0.5%          | won      |             0.9  |                           0.46 |
| 2026-10-30  | De'Anthony Melton PTS over 9.5 (10+)       | LAL @ GSW | draftkings  |   2.18 | +1.7% | 0.4%          | won      |             1.18 |                           0.44 |
| 2026-10-30  | Tre Jones PTS over 8.5 (9+)                | CHI @ BOS | pointsbetau |   2.05 | +1.6% | 0.4%          | won      |             1.05 |                           0.4  |
| 2026-10-30  | Austin Reaves PTS under 23.5               | LAL @ GSW | pointsbetau |   1.87 | +1.6% | 0.4%          | won      |             0.87 |                           0.39 |
| 2026-10-30  | Kelly Oubre Jr. PTS over 11.5 (12+)        | IND @ MIA | sportsbet   |   1.92 | +1.5% | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-10-30  | Jalen Brunson PTS under 26.5               | NYK @ PHI | pointsbetau |   2    | +1.4% | 0.4%          | won      |             1    |                           0.35 |
| 2026-10-30  | Day'Ron Sharpe PTS under 8.5               | DET @ BKN | tab         |   1.9  | +1.4% | 0.4%          | won      |             0.9  |                           0.34 |
| 2026-10-30  | Stephen Curry PTS under 24.5               | LAL @ GSW | sportsbet   |   1.96 | +1.3% | 0.3%          | lost     |            -1    |                          -0.34 |
| 2026-10-30  | Giannis Antetokounmpo PTS under 30.5       | IND @ MIA | pointsbetau |   2    | +1.2% | 0.3%          | lost     |            -1    |                          -0.31 |
| 2026-10-30  | LaMelo Ball PTS under 20.5                 | LAC @ MIN | draftkings  |   1.92 | +1.2% | 0.3%          | lost     |            -1    |                          -0.34 |
| 2026-10-30  | Joel Embiid PTS under 24.5                 | NYK @ PHI | sportsbet   |   1.96 | +1.2% | 0.3%          | won      |             0.96 |                           0.3  |
| 2026-10-30  | John Collins REB under 6.5                 | DET @ BKN | draftkings  |   2.12 | +1.2% | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-10-30  | Darius Garland PTS under 22.5              | LAC @ MIN | pointsbetau |   2    | +1.1% | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-10-30  | Jaden McDaniels PTS under 17.5             | LAC @ MIN | draftkings  |   1.95 | +1.0% | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-10-30  | Rui Hachimura PTS under 14.5               | LAC @ MIN | draftkings  |   1.95 | +1.0% | 0.3%          | won      |             0.95 |                           0.25 |
| 2026-10-30  | Kevin Durant PTS over 23.5 (24+)           | HOU @ DAL | sportsbet   |   1.9  | +0.9% | 0.3%          | won      |             0.9  |                           0.23 |
| 2026-10-30  | Tari Eason STL over 1.5 (2+)               | HOU @ DAL | draftkings  |   2.58 | +0.9% | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-10-30  | Brandon Miller PTS under 27.5              | CHA @ WAS | unibet      |   1.94 | +0.9% | 0.2%          | won      |             0.94 |                           0.23 |
| 2026-10-30  | Josh Hart PTS under 10.5                   | NYK @ PHI | tab         |   2    | +0.9% | 0.2%          | won      |             1    |                           0.22 |
| 2026-10-30  | Jayson Tatum PTS under 27.5                | CHI @ BOS | sportsbet   |   2.02 | +0.9% | 0.2%          | won      |             1.02 |                           0.21 |
| 2026-10-30  | Kris Dunn RA under 8.5                     | LAC @ MIN | draftkings  |   1.93 | +0.8% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-10-30  | Stephen Curry PTS under 25.5               | LAL @ GSW | tab         |   1.85 | +0.8% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-10-30  | Michael Porter Jr. PTS under 21.5          | DET @ BKN | draftkings  |   1.91 | +0.8% | 0.2%          | won      |             0.91 |                           0.2  |
| 2026-10-30  | Kelly Oubre Jr. PTS over 12.5 (13+)        | IND @ MIA | unibet      |   2    | +0.8% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-10-30  | Brandin Podziemski PTS under 15.5          | LAL @ GSW | tab         |   1.87 | +0.8% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-30  | Rui Hachimura 3PM under 1.5                | LAC @ MIN | draftkings  |   2.36 | +0.7% | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-10-30  | Bam Adebayo STL over 1.5 (2+)              | IND @ MIA | draftkings  |   2.75 | +0.6% | 0.1%          | won      |             1.75 |                           0.16 |
| 2026-10-30  | Yaxel Lendeborg PTS over 19.5 (20+)        | LAL @ GSW | pointsbetau |   2    | +0.6% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-30  | Norman Powell PA under 21.5                | CHI @ BOS | draftkings  |   1.92 | +0.6% | 0.2%          | won      |             0.92 |                           0.15 |
| 2026-10-30  | Paul George PA under 24.5                  | CHI @ BOS | draftkings  |   1.93 | +0.6% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-30  | Franz Wagner RA under 12.5                 | ORL @ TOR | draftkings  |   1.89 | +0.6% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-30  | Miles Bridges PR under 21.5                | DEN @ PHX | draftkings  |   1.97 | +0.6% | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-10-30  | Desmond Bane 3PM under 2.5                 | ORL @ TOR | draftkings  |   2.12 | +0.5% | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-10-30  | OG Anunoby REB over 5.5 (6+)               | NYK @ PHI | draftkings  |   2.15 | +0.5% | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-10-30  | Gui Santos PTS under 9.5                   | LAL @ GSW | tab         |   1.85 | +0.5% | 0.1%          | won      |             0.85 |                           0.12 |
| 2026-10-30  | Aaron Nesmith PTS over 13.5 (14+)          | IND @ MIA | sportsbet   |   1.8  | +0.5% | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-10-30  | Tari Eason PTS over 13.5 (14+)             | HOU @ DAL | sportsbet   |   2.08 | +0.5% | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-10-30  | Derrick White PA under 20.5                | CHI @ BOS | draftkings  |   1.97 | +0.5% | 0.1%          | won      |             0.97 |                           0.12 |
| 2026-10-30  | Miles Bridges PRA under 24.5               | DEN @ PHX | draftkings  |   1.93 | +0.5% | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-10-30  | LaMelo Ball PA under 27.5                  | LAC @ MIN | draftkings  |   1.94 | +0.4% | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-10-30  | Cooper Flagg PRA under 35.5                | HOU @ DAL | draftkings  |   1.93 | +0.4% | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-10-30  | Zaccharie Risacher REB over 4.5 (5+)       | HOU @ DAL | draftkings  |   2.16 | +0.4% | 0.1%          | won      |             1.16 |                           0.09 |
| 2026-10-30  | Kevin Durant PRA over 33.5 (34+)           | HOU @ DAL | draftkings  |   1.84 | +0.3% | 0.1%          | won      |             0.84 |                           0.08 |
| 2026-10-30  | Cooper Flagg PA under 28.5                 | HOU @ DAL | draftkings  |   1.94 | +0.3% | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-10-30  | LaMelo Ball 3PM under 3.5                  | LAC @ MIN | draftkings  |   1.91 | +0.3% | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-10-30  | Derrick Jones Jr. PTS under 10.5           | LAC @ MIN | tab         |   1.95 | +0.3% | 0.1%          | won      |             0.95 |                           0.07 |
| 2026-10-30  | Tari Eason RA over 7.5 (8+)                | HOU @ DAL | draftkings  |   1.86 | +0.2% | 0.1%          | won      |             0.86 |                           0.06 |
| 2026-10-30  | LaMelo Ball PR under 25.5                  | LAC @ MIN | draftkings  |   1.85 | +0.2% | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-10-30  | Derrick White PR under 19.5                | CHI @ BOS | draftkings  |   1.96 | +0.2% | 0.1%          | won      |             0.96 |                           0.06 |
| 2026-10-30  | Payton Pritchard PTS under 16.5            | CHI @ BOS | draftkings  |   1.91 | +0.2% | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-10-30  | Miles Bridges 3PM under 1.5                | DEN @ PHX | draftkings  |   2.13 | +0.2% | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-10-30  | Cooper Flagg PR under 30.5                 | HOU @ DAL | draftkings  |   1.85 | +0.2% | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-10-30  | Landry Shamet PR over 9.5 (10+)            | NYK @ PHI | draftkings  |   1.87 | +0.2% | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-10-30  | Anthony Davis BLK over 1.5 (2+)            | CHA @ WAS | draftkings  |   2.54 | +0.1% | 0.0%          | lost     |            -1    |                          -0.02 |
| 2026-10-30  | Pascal Siakam PRA over 35.5 (36+)          | IND @ MIA | draftkings  |   1.84 | +0.1% | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-10-30  | Anfernee Simons PA under 13.5              | NYK @ PHI | draftkings  |   1.83 | +0.1% | 0.0%          | lost     |            -1    |                          -0.04 |
| 2026-10-30  | Jayson Tatum PTS under 28.5                | CHI @ BOS | draftkings  |   1.91 | +0.1% | 0.0%          | won      |             0.91 |                           0.04 |
| 2026-10-30  | Devin Booker PTS under 23.5                | DEN @ PHX | pointsbetau |   1.9  | +0.1% | 0.0%          | won      |             0.9  |                           0.04 |
| 2026-10-30  | Al Horford 3PM under 0.5                   | LAL @ GSW | draftkings  |   2.7  | +0.1% | 0.0%          | lost     |            -1    |                          -0.02 |
| 2026-10-30  | Pascal Siakam 3PM over 1.5 (2+)            | IND @ MIA | draftkings  |   2.14 | +0.1% | 0.0%          | lost     |            -1    |                          -0.02 |
| 2026-10-30  | Grayson Allen PTS over 14.5 (15+)          | CHA @ WAS | draftkings  |   1.91 | +0.1% | 0.0%          | lost     |            -1    |                          -0.02 |
| 2026-10-30  | Josh Giddey PTS under 10.5                 | CHI @ BOS | pointsbetau |   2.05 | +0.0% | 0.0%          | lost     |            -1    |                          -0.01 |
| 2026-10-30  | AJ Dybantsa PA under 16.5                  | CHA @ WAS | draftkings  |   1.95 | +0.0% | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-30  | Cooper Flagg PA under 29.5                 | HOU @ DAL | draftkings  |   1.85 | +0.0% | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-29  | Kingston Flemings PTS under 8.5            | CLE @ ATL | tab         |   2    | +8.5% | 2.0%          | won      |             1    |                           2    |
| 2026-10-29  | Cedric Coward PTS under 12.5               | MEM @ POR | draftkings  |   1.94 | +4.4% | 1.1%          | lost     |            -1    |                          -1.15 |
| 2026-10-29  | Jalen Johnson PTS under 22.5               | CLE @ ATL | unibet      |   1.91 | +3.2% | 0.9%          | won      |             0.91 |                           0.8  |
| 2026-10-29  | Sam Merrill PTS under 8.5                  | CLE @ ATL | tab         |   1.95 | +2.9% | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-10-29  | Ty Jerome PTS under 23.5                   | MEM @ POR | tab         |   1.95 | +2.6% | 0.7%          | won      |             0.95 |                           0.66 |
| 2026-10-29  | Jrue Holiday PTS over 12.5 (13+)           | MEM @ POR | tab         |   1.95 | +2.5% | 0.7%          | lost     |            -1    |                          -0.65 |
| 2026-10-29  | Derik Queen PTS over 11.5 (12+)            | SAC @ NOP | sportsbet   |   1.92 | +2.4% | 0.7%          | lost     |            -1    |                          -0.67 |
| 2026-10-29  | Ty Jerome PTS under 24.5                   | MEM @ POR | betright    |   1.86 | +2.0% | 0.6%          | won      |             0.86 |                           0.51 |
| 2026-10-29  | Aaron Wiggins PTS under 11.5               | CLE @ ATL | draftkings  |   1.99 | +1.7% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-10-29  | Zach Edey PTS under 8.5                    | MEM @ POR | draftkings  |   1.9  | +0.9% | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-10-29  | Scoot Henderson PTS over 8.5 (9+)          | MEM @ POR | tab         |   1.9  | +0.9% | 0.2%          | won      |             0.9  |                           0.22 |
| 2026-10-29  | Dyson Daniels PTS under 11.5               | CLE @ ATL | tab         |   1.87 | +0.7% | 0.2%          | won      |             0.87 |                           0.18 |
| 2026-10-29  | Damian Lillard RA over 8.5 (9+)            | MEM @ POR | draftkings  |   2.1  | +0.6% | 0.1%          | lost     |            -1    |                          -0.13 |

</details>

## Day by day (last 30)

Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising count means something in the inputs is going wrong.

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean | sanity flags   |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|:---------------|
| 2026-10-30 |      10 |       176 | 4.05 / 5.25                      | 4.96 / 5.12                     |          0.5  | 0 (none)       |
| 2026-10-29 |       3 |        53 | 4.86 / 5.88                      | 6.06 / 5.94                     |          1.13 | 0 (none)       |
| 2026-10-28 |      12 |       164 | 4.99 / 5.61                      | 5.21 / 5.43                     |          1.23 |                |
