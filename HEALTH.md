# Model health

Rebuilt 2026-11-18 by the nightly grading run. Back to [TODAY.md](TODAY.md).

## Verdict: **BETTER**

Last 7 days beat the baseline by 4.7% vs 2.4% over 30 days.

How to read this: the model is judged against a simple rule anyone could use, each player's average over his last 10 games. "% better" is how much smaller the model's average miss is. Watch the trend, not single days: one game day is mostly noise.

## Projection accuracy (players the model had at 90%+ to play)

| window                      |   game days |   players |   minutes miss |   minutes % better than last-10 |   minutes lean (+ = too high) |   points miss |   points % better than last-10 |   points lean (+ = too high) |
|:----------------------------|------------:|----------:|---------------:|--------------------------------:|------------------------------:|--------------:|-------------------------------:|-----------------------------:|
| Last 7 days                 |           6 |       708 |           5.56 |                            10.2 |                          1.58 |          5.19 |                            4.7 |                         0.66 |
| Last 30 days                |          18 |      2347 |           5.14 |                            12.3 |                          1.76 |          5.16 |                            2.4 |                         0.85 |
| Season                      |          18 |      2347 |           5.14 |                            12.3 |                          1.76 |          5.16 |                            2.4 |                         0.85 |
| Backtest (held-out 2025-26) |             |           |                |                            15.4 |                               |               |                            5.4 |                              |

Live should sit near the backtest line. Well below it for weeks means the model is doing worse on new games than it did in testing (overfitting or something broke).

## Best bets (EV ≥ 5%, odds ≤ 4)

**Main record: the final list.** The bets still in TODAY.md's best-bets table on the last update before each game's tip (after lineups and injury news), graded at the price shown then.

Each table shows two ways of counting: units at a flat 1-unit stake on every bet (so results compare cleanly), and profit at the sheet's suggested stake, the quarter-Kelly % of bankroll capped at 2% that TODAY.md shows on every bet. ROI (sheet stakes) is that profit divided by the total staked. Rows are the last 7 days, last 30 days and whole season; a longer period only gets its own row once it holds more bets than the shorter one.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |     13 |     7 |             2    |           15.4 |                  20.2 |                                  4.37 |                   21.6 |
| Last 30 days |     43 |    18 |            -0.08 |           -0.2 |                  57.7 |                                  1.64 |                    2.8 |

<details><summary>Every final-list bet (43)</summary>

| date (US)   | bet                                       | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-17  | Sion James PTS over 7.5 (8+)              | CHA @ LAL | draftkings  |   2.56 | +28.2% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-17  | POR to win                                | POR @ MIN | draftkings  |   2.5  | +11.8% | 2.0%          | lost     |            -1    |                          -1.98 |
| 2026-11-16  | Danny Wolf PTS over 9.5 (10+)             | PHI @ BKN | draftkings  |   2.68 | +30.3% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-16  | Meleek Thomas PTS over 12.5 (13+)         | CHI @ CLE | unibet      |   2.12 | +5.5%  | 1.2%          | lost     |            -1    |                          -1.22 |
| 2026-11-15  | Ryan Kalkbrenner PTS over 4.5 (5+)        | CHA @ LAC | pointsbetau |   2.1  | +7.2%  | 1.6%          | won      |             1.1  |                           1.79 |
| 2026-11-15  | Dylan Cardwell PTS over 5.5 (6+)          | OKC @ SAC | pointsbetau |   2.05 | +6.7%  | 1.6%          | won      |             1.05 |                           1.67 |
| 2026-11-15  | Josh Okogie PTS over 4.5 (5+)             | SAS @ UTA | draftkings  |   1.98 | +6.4%  | 1.6%          | won      |             0.98 |                           1.59 |
| 2026-11-15  | MIL to win                                | ATL @ MIL | draftkings  |   3.81 | +5.2%  | 0.5%          | lost     |            -1    |                          -0.46 |
| 2026-11-14  | Day'Ron Sharpe PTS over 9.5 (10+)         | BKN @ MEM | pointsbetau |   2.05 | +7.2%  | 1.7%          | won      |             1.05 |                           1.78 |
| 2026-11-14  | Cedric Coward PTS over 14.5 (15+)         | BKN @ MEM | pointsbetau |   1.95 | +5.5%  | 1.5%          | won      |             0.95 |                           1.39 |
| 2026-11-13  | Nic Claxton PTS over 9.5 (10+)            | ATL @ CHI | draftkings  |   2.78 | +8.5%  | 1.2%          | lost     |            -1    |                          -1.19 |
| 2026-11-13  | Aday Mara PTS under 11.5                  | OKC @ LAC | draftkings  |   2.06 | +6.5%  | 1.5%          | won      |             1.06 |                           1.63 |
| 2026-11-11  | Kenrich Williams PTS over 9.5 (10+)       | OKC @ POR | draftkings  |   2.81 | +13.5% | 1.9%          | won      |             1.81 |                           3.37 |
| 2026-11-10  | Scoot Henderson PTS over 11.5 (12+)       | OKC @ POR | draftkings  |   2.74 | +13.2% | 1.9%          | lost     |            -1    |                          -1.89 |
| 2026-11-10  | Isaiah Collier PTS over 11.5 (12+)        | MIA @ UTA | draftkings  |   2.55 | +8.7%  | 1.4%          | won      |             1.55 |                           2.17 |
| 2026-11-09  | Jamison Battle PTS over 9.5 (10+)         | MEM @ TOR | draftkings  |   2.22 | +19.0% | 2.0%          | won      |             1.22 |                           2.44 |
| 2026-11-08  | Brice Sensabaugh PTS over 9.5 (10+)       | UTA @ MIN | draftkings  |   2.53 | +30.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-07  | Meleek Thomas 3PM over 1.5 (2+)           | NYK @ CLE | draftkings  |   2.43 | +22.3% | 2.0%          | won      |             1.43 |                           2.86 |
| 2026-11-07  | ORL to win                                | ORL @ GSW | draftkings  |   3.5  | +5.5%  | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-11-02  | CHA to win                                | DET @ CHA | draftkings  |   2.82 | +8.0%  | 1.1%          | lost     |            -1    |                          -1.1  |
| 2026-11-01  | Gui Santos PTS over 9.5 (10+)             | LAC @ GSW | draftkings  |   2.4  | +21.8% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-01  | Nolan Traore PTS under 12.5               | BKN @ IND | draftkings  |   1.99 | +7.0%  | 1.8%          | lost     |            -1    |                          -1.75 |
| 2026-11-01  | Rui Hachimura PTS under 15.5              | LAC @ GSW | draftkings  |   1.97 | +6.6%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-01  | Scottie Barnes AST over 7.5 (8+)          | TOR @ LAL | draftkings  |   3.73 | +6.5%  | 0.6%          | lost     |            -1    |                          -0.59 |
| 2026-11-01  | Jamal Shead PTS over 6.5 (7+)             | TOR @ LAL | pointsbetau |   2.05 | +5.8%  | 1.4%          | won      |             1.05 |                           1.45 |
| 2026-11-01  | Aaron Nesmith PTS over 12.5 (13+)         | BKN @ IND | pointsbetau |   2.05 | +5.5%  | 1.3%          | lost     |            -1    |                          -1.32 |
| 2026-11-01  | Gui Santos REB over 5.5 (6+)              | LAC @ GSW | draftkings  |   3.81 | +5.4%  | 0.5%          | lost     |            -1    |                          -0.48 |
| 2026-10-31  | Zach Edey PTS over 8.5 (9+)               | SAC @ MEM | pointsbetau |   2.05 | +11.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Donovan Clingan PTS over 11.5 (12+)       | POR @ UTA | draftkings  |   2.26 | +8.2%  | 1.6%          | lost     |            -1    |                          -1.63 |
| 2026-10-31  | Donovan Clingan BLK over 2.5 (3+)         | POR @ UTA | draftkings  |   3.66 | +7.0%  | 0.7%          | lost     |            -1    |                          -0.66 |
| 2026-10-31  | Jaylen Wells PTS over 11.5 (12+)          | SAC @ MEM | unibet      |   1.66 | +6.2%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Trey Murphy III AST over 3.5 (4+)         | ATL @ NOP | draftkings  |   2.22 | +6.1%  | 1.3%          | won      |             1.22 |                           1.54 |
| 2026-10-31  | Saddiq Bey PRA over 24.5 (25+)            | ATL @ NOP | draftkings  |   3.5  | +5.7%  | 0.6%          | won      |             2.5  |                           1.43 |
| 2026-10-31  | Shai Gilgeous-Alexander AST over 7.5 (8+) | OKC @ HOU | draftkings  |   3.83 | +5.6%  | 0.5%          | lost     |            -1    |                          -0.49 |
| 2026-10-30  | Jarace Walker PTS over 10.5 (11+)         | IND @ MIA | pointsbetau |   2    | +7.3%  | 1.8%          | won      |             1    |                           1.82 |
| 2026-10-30  | Pascal Siakam AST over 5.5 (6+)           | IND @ MIA | draftkings  |   3.66 | +6.6%  | 0.6%          | lost     |            -1    |                          -0.62 |
| 2026-10-29  | Kingston Flemings PTS under 8.5           | CLE @ ATL | tab         |   2    | +8.5%  | 2.0%          | won      |             1    |                           2    |
| 2026-10-29  | Damian Lillard AST over 5.5 (6+)          | MEM @ POR | draftkings  |   3.87 | +6.4%  | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-10-29  | Ja Morant AST over 7.5 (8+)               | MEM @ POR | draftkings  |   3.25 | +5.4%  | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-28  | Darius Garland PTS over 29.5 (30+)        | LAL @ LAC | draftkings  |   3.67 | +5.8%  | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-10-28  | Jarace Walker REB over 6.5 (7+)           | PHI @ IND | draftkings  |   3.43 | +5.8%  | 0.6%          | won      |             2.43 |                           1.46 |
| 2026-10-28  | IND +5.5                                  | PHI @ IND | unibet      |   1.95 | +5.4%  | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-28  | Pascal Siakam PRA over 39.5 (40+)         | PHI @ IND | draftkings  |   3.57 | +5.0%  | 0.5%          | won      |             2.57 |                           1.26 |

</details>

## Long shots (EV ≥ 5%, odds above 4)

TODAY.md's long-shot table, graded the same way: the final pre-tip list at the price shown then, 1 unit flat. Expect long losing runs; judge it over hundreds of bets.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |    118 |     3 |           -97.36 |          -82.5 |                  24.1 |                                -14.65 |                  -60.8 |
| Last 30 days |    291 |    15 |           -92    |          -31.6 |                  80.6 |                                -14.37 |                  -17.8 |

<details><summary>Every long shot (291)</summary>

| date (US)   | bet                                       | game      | book          |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:--------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-17  | Scottie Barnes AST over 9.5 (10+)         | NYK @ TOR | draftkings    |  14.8  | +8.8%  | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-11-17  | Paul Reed PRA over 34.5 (35+)             | DET @ SAS | draftkings    |  16.4  | +7.8%  | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-17  | Jrue Holiday AST over 7.5 (8+)            | POR @ MIN | draftkings    |   9.4  | +7.7%  | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-11-17  | Paul Reed PR over 29.5 (30+)              | DET @ SAS | draftkings    |  11    | +7.4%  | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-11-17  | Paul Reed PRA over 29.5 (30+)             | DET @ SAS | draftkings    |   7.3  | +7.1%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-17  | Jrue Holiday AST over 9.5 (10+)           | POR @ MIN | draftkings    |  25    | +6.6%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-11-17  | Paul Reed REB over 11.5 (12+)             | DET @ SAS | draftkings    |   9    | +5.3%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-17  | Paul Reed REB over 13.5 (14+)             | DET @ SAS | draftkings    |  19.2  | +5.2%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-11-17  | Scottie Barnes AST over 7.5 (8+)          | NYK @ TOR | draftkings    |   5.44 | +5.0%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-16  | Zach Edey REB over 15.5 (16+)             | MEM @ WAS | draftkings    |  25    | +24.8% | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-16  | Zach Edey REB over 13.5 (14+)             | MEM @ WAS | draftkings    |  14    | +24.5% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-11-16  | Derik Queen PRA over 34.5 (35+)           | GSW @ NOP | draftkings    |  19.6  | +13.3% | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-11-16  | Taylor Hendricks REB over 7.5 (8+)        | MEM @ WAS | draftkings    |  12.8  | +11.2% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-11-16  | Derik Queen PRA over 29.5 (30+)           | GSW @ NOP | draftkings    |   8.5  | +10.5% | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-11-16  | Kevin Durant AST over 7.5 (8+)            | HOU @ MIA | draftkings    |   9.7  | +9.6%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-16  | Derik Queen PR over 29.5 (30+)            | GSW @ NOP | draftkings    |  15.4  | +9.3%  | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-11-16  | Kevin Durant AST over 9.5 (10+)           | HOU @ MIA | draftkings    |  26    | +8.5%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-16  | Donovan Mitchell PA over 49.5 (50+)       | CHI @ CLE | draftkings    |  20.4  | +8.2%  | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-11-16  | Donovan Mitchell PTS over 44.5 (45+)      | CHI @ CLE | draftkings    |  22    | +7.9%  | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-11-16  | Derik Queen PTS over 19.5 (20+)           | GSW @ NOP | draftkings    |  12.6  | +7.9%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-16  | Draymond Green AST over 11.5 (12+)        | GSW @ NOP | draftkings    |  19    | +7.4%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-16  | Reed Sheppard AST over 7.5 (8+)           | HOU @ MIA | draftkings    |  18.8  | +7.2%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-16  | Jarrett Allen BLK over 3.5 (4+)           | CHI @ CLE | draftkings    |  18    | +7.0%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-16  | Jarrett Allen BLK over 2.5 (3+)           | CHI @ CLE | draftkings    |   7.5  | +7.0%  | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-11-16  | James Harden PA over 39.5 (40+)           | CHI @ CLE | draftkings    |  15.8  | +6.8%  | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-11-16  | PHX to win                                | PHX @ DEN | unibet        |   4.8  | +6.8%  | 0.4%          | won      |             3.8  |                           1.67 |
| 2026-11-16  | Derik Queen PR over 24.5 (25+)            | GSW @ NOP | draftkings    |   6.34 | +6.2%  | 0.3%          | won      |             5.34 |                           1.55 |
| 2026-11-16  | Derik Queen AST over 5.5 (6+)             | GSW @ NOP | draftkings    |  11.2  | +6.1%  | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-16  | Reed Sheppard AST over 5.5 (6+)           | HOU @ MIA | draftkings    |   6.29 | +6.0%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-16  | Taylor Hendricks REB over 9.5 (10+)       | MEM @ WAS | draftkings    |  29    | +5.9%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-16  | Cedric Coward PTS over 29.5 (30+)         | MEM @ WAS | draftkings    |  18    | +5.7%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-16  | Giannis Antetokounmpo PRA over 64.5 (65+) | HOU @ MIA | draftkings    |  14.8  | +5.6%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-16  | Nikola Jokic PA over 54.5 (55+)           | PHX @ DEN | draftkings    |  20.2  | +5.6%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-11-16  | James Harden PRA over 44.5 (45+)          | CHI @ CLE | draftkings    |  13.4  | +5.6%  | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-11-15  | Kevin Durant PRA over 49.5 (50+)          | HOU @ WAS | draftkings    |  21    | +25.6% | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-11-15  | Kevin Durant PR over 44.5 (45+)           | HOU @ WAS | draftkings    |  20    | +18.6% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-11-15  | SAC to win                                | OKC @ SAC | draftkings    |   5.58 | +18.2% | 1.0%          | lost     |            -1    |                          -1    |
| 2026-11-15  | DAL to win                                | DAL @ BOS | draftkings    |   7.4  | +15.5% | 0.6%          | lost     |            -1    |                          -0.61 |
| 2026-11-15  | Domantas Sabonis PA over 34.5 (35+)       | OKC @ SAC | draftkings    |  23    | +15.0% | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-15  | Alperen Sengun PTS over 39.5 (40+)        | HOU @ WAS | draftkings    |  30    | +14.0% | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-11-15  | Alperen Sengun PTS over 34.5 (35+)        | HOU @ WAS | draftkings    |  17    | +13.1% | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-11-15  | Domantas Sabonis PTS over 29.5 (30+)      | OKC @ SAC | draftkings    |  30    | +13.1% | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-11-15  | Kevin Durant PR over 39.5 (40+)           | HOU @ WAS | draftkings    |   9.7  | +12.2% | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-11-15  | Alperen Sengun PR over 49.5 (50+)         | HOU @ WAS | draftkings    |  21    | +12.2% | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-15  | UTA to win                                | SAS @ UTA | betfair_ex_au |  10.02 | +12.1% | 0.3%          | lost     |            -1    |                          -0.33 |
| 2026-11-15  | Domantas Sabonis PA over 29.5 (30+)       | OKC @ SAC | draftkings    |  10.2  | +12.1% | 0.3%          | lost     |            -1    |                          -0.33 |
| 2026-11-15  | Alperen Sengun PR over 44.5 (45+)         | HOU @ WAS | draftkings    |  11.6  | +11.8% | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-15  | Kevin Durant AST over 7.5 (8+)            | HOU @ WAS | draftkings    |  11    | +11.7% | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-11-15  | Jaime Jaquez Jr. AST over 7.5 (8+)        | ATL @ MIL | draftkings    |  14.2  | +11.3% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-11-15  | Scottie Barnes AST over 9.5 (10+)         | NYK @ TOR | draftkings    |  18    | +10.7% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-11-15  | Domantas Sabonis PRA over 49.5 (50+)      | OKC @ SAC | draftkings    |  20.4  | +10.4% | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-15  | Kevin Durant AST over 9.5 (10+)           | HOU @ WAS | draftkings    |  28    | +8.6%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-15  | Trae Young AST over 13.5 (14+)            | HOU @ WAS | draftkings    |  16.2  | +8.3%  | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-11-15  | Tyrese Maxey AST over 9.5 (10+)           | IND @ PHI | draftkings    |  14.2  | +7.7%  | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-15  | Tyrese Maxey PR over 49.5 (50+)           | IND @ PHI | draftkings    |  24    | +7.4%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-15  | Pascal Siakam PRA over 49.5 (50+)         | IND @ PHI | draftkings    |  16.2  | +7.2%  | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-11-15  | Luka Doncic PTS over 54.5 (55+)           | LAL @ PHX | draftkings    |  16.2  | +6.9%  | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-11-15  | Alperen Sengun PTS over 29.5 (30+)        | HOU @ WAS | draftkings    |   7.2  | +6.3%  | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-15  | Dylan Cardwell REB over 13.5 (14+)        | OKC @ SAC | draftkings    |  20.4  | +6.3%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-14  | CHI to win                                | CHI @ MIN | sportsbet     |   9.5  | +19.6% | 0.6%          | won      |             8.5  |                           4.93 |
| 2026-11-14  | Karlo Matkovic PTS over 14.5 (15+)        | DEN @ NOP | draftkings    |  14.4  | +17.4% | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-11-14  | Karlo Matkovic PR over 24.5 (25+)         | DEN @ NOP | draftkings    |  25    | +13.9% | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-11-14  | Karlo Matkovic REB over 7.5 (8+)          | DEN @ NOP | draftkings    |   9.4  | +9.7%  | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-11-14  | Karlo Matkovic REB over 9.5 (10+)         | DEN @ NOP | draftkings    |  22    | +7.9%  | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-11-14  | Jaylon Tyson PA over 34.5 (35+)           | DAL @ CLE | draftkings    |  14.8  | +5.2%  | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-11-14  | Thomas Bryant PTS over 29.5 (30+)         | DAL @ CLE | draftkings    |  18.2  | +5.2%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-14  | Thomas Bryant PTS over 24.5 (25+)         | DAL @ CLE | draftkings    |   8.4  | +5.0%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-13  | Karlo Matkovic PRA over 24.5 (25+)        | MEM @ NOP | draftkings    |  14.6  | +17.3% | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-11-13  | Kevin Durant PA over 39.5 (40+)           | UTA @ HOU | draftkings    |  14.4  | +16.1% | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-11-13  | Kevin Durant PA over 44.5 (45+)           | UTA @ HOU | draftkings    |  26    | +15.8% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-11-13  | Kevin Durant PRA over 49.5 (50+)          | UTA @ HOU | draftkings    |  20.2  | +15.6% | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-11-13  | UTA to win                                | UTA @ HOU | betfair_ex_au |   9.55 | +13.6% | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-11-13  | Karlo Matkovic PR over 24.5 (25+)         | MEM @ NOP | draftkings    |  18.4  | +13.0% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-13  | Kevin Durant PRA over 44.5 (45+)          | UTA @ HOU | draftkings    |  10.5  | +12.5% | 0.3%          | lost     |            -1    |                          -0.33 |
| 2026-11-13  | Karlo Matkovic PTS over 14.5 (15+)        | MEM @ NOP | draftkings    |  10.7  | +11.8% | 0.3%          | lost     |            -1    |                          -0.31 |
| 2026-11-13  | Kevin Durant PR over 44.5 (45+)           | UTA @ HOU | draftkings    |  18.8  | +10.7% | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-13  | Kevin Durant AST over 7.5 (8+)            | UTA @ HOU | draftkings    |  14.4  | +10.3% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-13  | Jalen Suggs PRA over 24.5 (25+)           | MIL @ ORL | draftkings    |   9    | +9.7%  | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-11-13  | Cam Spencer AST over 9.5 (10+)            | MEM @ NOP | draftkings    |  22    | +9.4%  | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-11-13  | Jalen Suggs PRA over 29.5 (30+)           | MIL @ ORL | draftkings    |  20.8  | +8.9%  | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-11-13  | Derik Queen PRA over 34.5 (35+)           | MEM @ NOP | draftkings    |  16    | +8.5%  | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-11-13  | Kevin Durant PR over 39.5 (40+)           | UTA @ HOU | draftkings    |   9.6  | +8.3%  | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-11-13  | Scoot Henderson AST over 5.5 (6+)         | POR @ SAC | draftkings    |  15.8  | +7.5%  | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-13  | Jalen Suggs AST over 7.5 (8+)             | MIL @ ORL | draftkings    |  12.8  | +7.5%  | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-11-13  | GSW to win                                | GSW @ SAS | sportsbet     |   6.15 | +7.1%  | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-11-13  | Amen Thompson AST over 7.5 (8+)           | UTA @ HOU | draftkings    |  17.8  | +6.8%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-13  | Donovan Mitchell PTS over 44.5 (45+)      | CLE @ MIA | draftkings    |  26    | +6.8%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-11-13  | Derik Queen PA over 29.5 (30+)            | MEM @ NOP | draftkings    |  26    | +6.8%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-11-13  | Cam Spencer AST over 7.5 (8+)             | MEM @ NOP | draftkings    |   8.5  | +6.6%  | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-11-13  | Derik Queen PTS over 24.5 (25+)           | MEM @ NOP | draftkings    |  30    | +6.4%  | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-11-13  | Jalen Suggs REB over 5.5 (6+)             | MIL @ ORL | draftkings    |   9.6  | +6.4%  | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-13  | Kevin Durant PRA over 54.5 (55+)          | UTA @ HOU | draftkings    |  27    | +6.3%  | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-11-12  | Ryan Kalkbrenner PR over 19.5 (20+)       | CHA @ PHX | draftkings    |  13.6  | +16.9% | 0.3%          | lost     |            -1    |                          -0.34 |
| 2026-11-12  | Ryan Kalkbrenner REB over 9.5 (10+)       | CHA @ PHX | draftkings    |  10.7  | +7.8%  | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-11-12  | Ryan Kalkbrenner REB over 11.5 (12+)      | CHA @ PHX | draftkings    |  23    | +6.2%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-11-12  | Ryan Kalkbrenner PTS over 14.5 (15+)      | CHA @ PHX | draftkings    |  23    | +5.1%  | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-11-11  | CHI to win                                | SAS @ CHI | betfair_ex_au |  10.5  | +25.9% | 0.7%          | lost     |            -1    |                          -0.68 |
| 2026-11-11  | Derik Queen PRA over 34.5 (35+)           | BKN @ NOP | draftkings    |  19.4  | +13.7% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-11  | Pascal Siakam AST over 7.5 (8+)           | WAS @ IND | draftkings    |  16.2  | +13.0% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-11-11  | MIL to win                                | LAL @ MIL | betfair_ex_au |   7.65 | +12.4% | 0.5%          | lost     |            -1    |                          -0.47 |

</details>

## Check news first (EV ≥ 5%, odds ≤ 4)

TODAY.md's "check news first" table: bets that clear the bar but where the model and market disagree by more than 15 points, so something may be missing. Final pre-tip list at the price shown then. Kept apart from best bets; if this stays unprofitable, the flag is doing its job.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |      9 |     5 |             2.64 |           29.3 |                  10.7 |                                  4.2  |                   39.4 |
| Last 30 days |     86 |    40 |            -2.22 |           -2.6 |                 128.4 |                                  3.59 |                    2.8 |

<details><summary>Every check-news bet (86)</summary>

| date (US)   | bet                                  | game      | book         |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-------------------------------------|:----------|:-------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-16  | Zach Edey REB over 9.5 (10+)         | MEM @ WAS | draftkings   |   3.62 | +8.3%  | 0.8%          | won      |             2.62 |                           2.07 |
| 2026-11-16  | Tyrese Proctor PTS over 10.5 (11+)   | CHI @ CLE | pointsbetau  |   2.05 | +7.5%  | 1.8%          | won      |             1.05 |                           1.88 |
| 2026-11-16  | Luka Garza PTS under 9.5             | ORL @ BOS | pointsbetau  |   1.87 | +5.1%  | 1.5%          | won      |             0.87 |                           1.26 |
| 2026-11-14  | Karlo Matkovic PTS over 9.5 (10+)    | DEN @ NOP | draftkings   |   3.98 | +7.3%  | 0.6%          | lost     |            -1    |                          -0.61 |
| 2026-11-13  | Karlo Matkovic PTS over 7.5 (8+)     | MEM @ NOP | draftkings   |   2.24 | +20.3% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-13  | Brayden Burries PTS under 11.5       | MIL @ ORL | pointsbetau  |   2    | +5.8%  | 1.4%          | won      |             1    |                           1.44 |
| 2026-11-13  | Karlo Matkovic PR over 14.5 (15+)    | MEM @ NOP | draftkings   |   3    | +5.6%  | 0.7%          | lost     |            -1    |                          -0.7  |
| 2026-11-13  | Karlo Matkovic PTS over 9.5 (10+)    | MEM @ NOP | draftkings   |   3.38 | +5.5%  | 0.6%          | lost     |            -1    |                          -0.58 |
| 2026-11-11  | Jamison Battle PTS over 8.5 (9+)     | BOS @ TOR | pointsbetau  |   2.1  | +5.8%  | 1.3%          | won      |             1.1  |                           1.44 |
| 2026-11-10  | Precious Achiuwa PTS over 7.5 (8+)   | ORL @ SAC | pointsbetau  |   2.1  | +9.2%  | 2.0%          | won      |             1.1  |                           2.2  |
| 2026-11-02  | Khaman Maluach REB under 6.5         | PHX @ GSW | draftkings   |   2.07 | +6.0%  | 1.4%          | won      |             1.07 |                           1.49 |
| 2026-11-01  | Jarace Walker PR over 19.5 (20+)     | BKN @ IND | draftkings   |   3.42 | +9.1%  | 0.9%          | lost     |            -1    |                          -0.94 |
| 2026-11-01  | Walker Kessler PTS under 12.5        | TOR @ LAL | tab          |   1.9  | +6.1%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-01  | Brandon Williams PTS under 14.5      | LAC @ GSW | draftkings   |   1.88 | +5.0%  | 1.4%          | lost     |            -1    |                          -1.41 |
| 2026-10-31  | Tari Eason REB over 7.5 (8+)         | OKC @ HOU | draftkings   |   3.87 | +13.6% | 1.2%          | lost     |            -1    |                          -1.19 |
| 2026-10-31  | Isaiah Collier PRA over 19.5 (20+)   | POR @ UTA | draftkings   |   3.7  | +13.5% | 1.2%          | lost     |            -1    |                          -1.25 |
| 2026-10-31  | Cameron Boozer REB over 9.5 (10+)    | SAC @ MEM | draftkings   |   2.84 | +12.1% | 1.6%          | lost     |            -1    |                          -1.64 |
| 2026-10-31  | Damian Lillard PTS under 23.5        | POR @ UTA | betright     |   1.96 | +11.7% | 2.0%          | won      |             0.96 |                           1.92 |
| 2026-10-31  | Isaiah Collier PTS over 9.5 (10+)    | POR @ UTA | draftkings   |   3.09 | +9.1%  | 1.1%          | lost     |            -1    |                          -1.09 |
| 2026-10-31  | Adem Bona PR under 14.5              | PHI @ CHA | draftkings   |   1.77 | +9.1%  | 2.0%          | won      |             0.77 |                           1.54 |
| 2026-10-31  | Kevin Durant RA over 8.5 (9+)        | OKC @ HOU | draftkings   |   2    | +9.1%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Kevin Durant AST over 3.5 (4+)       | OKC @ HOU | draftkings   |   2.16 | +8.8%  | 1.9%          | won      |             1.16 |                           2.2  |
| 2026-10-31  | Adem Bona REB under 5.5              | PHI @ CHA | draftkings   |   2.14 | +8.7%  | 1.9%          | won      |             1.14 |                           2.18 |
| 2026-10-31  | AJ Green 3PM under 1.5               | CLE @ MIL | draftkings   |   2.33 | +8.7%  | 1.6%          | won      |             1.33 |                           2.17 |
| 2026-10-31  | Jerami Grant PTS over 14.5 (15+)     | SAC @ MEM | draftkings   |   3.09 | +8.4%  | 1.0%          | lost     |            -1    |                          -1    |
| 2026-10-31  | Adem Bona REB under 6.5              | PHI @ CHA | draftkings   |   1.87 | +8.4%  | 2.0%          | won      |             0.87 |                           1.74 |
| 2026-10-31  | Amen Thompson AST over 5.5 (6+)      | OKC @ HOU | draftkings   |   3.08 | +8.3%  | 1.0%          | lost     |            -1    |                          -1    |
| 2026-10-31  | Joan Beringer PR under 18.5          | MIN @ SAS | draftkings   |   1.9  | +8.2%  | 2.0%          | won      |             0.9  |                           1.8  |
| 2026-10-31  | Tari Eason PR over 19.5 (20+)        | OKC @ HOU | draftkings   |   3.03 | +7.2%  | 0.9%          | lost     |            -1    |                          -0.89 |
| 2026-10-31  | Damian Lillard PTS under 22.5        | POR @ UTA | draftkings   |   1.97 | +6.8%  | 1.7%          | won      |             0.97 |                           1.69 |
| 2026-10-31  | Scoot Henderson PTS under 14.5       | POR @ UTA | draftkings   |   1.93 | +6.4%  | 1.7%          | won      |             0.93 |                           1.6  |
| 2026-10-31  | VJ Edgecombe PTS under 15.5          | PHI @ CHA | pointsbetau  |   2.05 | +5.4%  | 1.3%          | won      |             1.05 |                           1.35 |
| 2026-10-31  | Darryn Peterson PTS under 14.5       | POR @ UTA | betright     |   1.92 | +5.3%  | 1.5%          | lost     |            -1    |                          -1.45 |
| 2026-10-31  | Kevin Durant REB over 5.5 (6+)       | OKC @ HOU | draftkings   |   2.33 | +5.2%  | 1.0%          | lost     |            -1    |                          -0.98 |
| 2026-10-31  | Cameron Boozer RA over 14.5 (15+)    | SAC @ MEM | draftkings   |   2    | +5.1%  | 1.3%          | lost     |            -1    |                          -1.29 |
| 2026-10-31  | Dean Wade REB under 4.5              | PHI @ CHA | draftkings   |   2.13 | +5.0%  | 1.1%          | lost     |            -1    |                          -1.11 |
| 2026-10-30  | Quenton Jackson PR over 9.5 (10+)    | IND @ MIA | draftkings   |   2.01 | +9.6%  | 2.0%          | won      |             1.01 |                           2.02 |
| 2026-10-30  | Quenton Jackson PA over 9.5 (10+)    | IND @ MIA | draftkings   |   1.83 | +8.9%  | 2.0%          | won      |             0.83 |                           1.66 |
| 2026-10-30  | Quenton Jackson AST over 3.5 (4+)    | IND @ MIA | draftkings   |   2.29 | +8.8%  | 1.7%          | lost     |            -1    |                          -1.71 |
| 2026-10-30  | Cameron Johnson PTS under 10.5       | DEN @ PHX | unibet       |   1.97 | +8.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-30  | Khaman Maluach PR under 15.5         | DEN @ PHX | draftkings   |   1.94 | +7.7%  | 2.0%          | won      |             0.94 |                           1.88 |
| 2026-10-30  | AJ Dybantsa PTS under 15.5           | CHA @ WAS | draftkings   |   1.95 | +7.6%  | 2.0%          | lost     |            -1    |                          -1.99 |
| 2026-10-30  | Kevin Durant PRA over 39.5 (40+)     | HOU @ DAL | draftkings   |   3.14 | +7.5%  | 0.9%          | lost     |            -1    |                          -0.88 |
| 2026-10-30  | Nolan Traore PTS under 9.5           | DET @ BKN | pointsbetau  |   2.05 | +7.5%  | 1.8%          | won      |             1.05 |                           1.87 |
| 2026-10-30  | Khaman Maluach REB under 7.5         | DEN @ PHX | draftkings   |   2.01 | +7.4%  | 1.8%          | won      |             1.01 |                           1.86 |
| 2026-10-30  | Cameron Johnson 3PM under 1.5        | DEN @ PHX | draftkings   |   2.1  | +7.4%  | 1.7%          | lost     |            -1    |                          -1.69 |
| 2026-10-30  | Walker Kessler PTS under 13.5        | LAL @ GSW | sportsbet    |   2.02 | +7.0%  | 1.7%          | won      |             1.02 |                           1.74 |
| 2026-10-30  | John Collins PTS under 14.5          | DET @ BKN | tab          |   1.9  | +6.8%  | 1.9%          | won      |             0.9  |                           1.71 |
| 2026-10-30  | Walker Kessler PTS under 14.5        | LAL @ GSW | ladbrokes_au |   1.83 | +6.5%  | 1.9%          | won      |             0.83 |                           1.62 |
| 2026-10-30  | DeMar DeRozan AST over 3.5 (4+)      | DEN @ PHX | draftkings   |   3.1  | +6.4%  | 0.8%          | won      |             2.1  |                           1.6  |
| 2026-10-30  | Kevin Durant RA over 9.5 (10+)       | HOU @ DAL | draftkings   |   1.95 | +6.0%  | 1.6%          | lost     |            -1    |                          -1.58 |
| 2026-10-30  | Naz Reid PTS under 17.5              | CHA @ WAS | pointsbetau  |   2    | +5.8%  | 1.5%          | won      |             1    |                           1.45 |
| 2026-10-30  | AJ Dybantsa PR under 20.5            | CHA @ WAS | draftkings   |   1.94 | +5.8%  | 1.5%          | lost     |            -1    |                          -1.53 |
| 2026-10-30  | Nolan Traore PTS under 10.5          | DET @ BKN | draftkings   |   1.85 | +5.7%  | 1.7%          | won      |             0.85 |                           1.42 |
| 2026-10-30  | Kevin Durant AST over 3.5 (4+)       | HOU @ DAL | draftkings   |   1.78 | +5.6%  | 1.8%          | lost     |            -1    |                          -1.79 |
| 2026-10-30  | Bilal Coulibaly PTS over 9.5 (10+)   | CHA @ WAS | draftkings   |   2.8  | +5.1%  | 0.7%          | lost     |            -1    |                          -0.71 |
| 2026-10-30  | Kevin Durant RA over 8.5 (9+)        | HOU @ DAL | draftkings   |   1.72 | +5.1%  | 1.8%          | lost     |            -1    |                          -1.78 |
| 2026-10-30  | AJ Dybantsa PRA under 23.5           | CHA @ WAS | draftkings   |   1.83 | +5.0%  | 1.5%          | lost     |            -1    |                          -1.53 |
| 2026-10-29  | Zion Williamson PTS over 24.5 (25+)  | SAC @ NOP | draftkings   |   3.63 | +10.8% | 1.0%          | lost     |            -1    |                          -1.03 |
| 2026-10-29  | Cedric Coward PTS under 13.5         | MEM @ POR | sportsbet    |   1.96 | +8.0%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-29  | Cameron Boozer PTS under 17.5        | MEM @ POR | tab          |   1.9  | +7.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-29  | Jrue Holiday PRA over 24.5 (25+)     | MEM @ POR | draftkings   |   3.38 | +7.1%  | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-10-29  | Precious Achiuwa PTS over 14.5 (15+) | SAC @ NOP | draftkings   |   3.53 | +6.9%  | 0.7%          | won      |             2.53 |                           1.72 |
| 2026-10-29  | Jrue Holiday AST over 4.5 (5+)       | MEM @ POR | draftkings   |   2.5  | +6.6%  | 1.1%          | lost     |            -1    |                          -1.1  |
| 2026-10-29  | Jeremiah Fears PA over 16.5 (17+)    | SAC @ NOP | draftkings   |   1.95 | +5.4%  | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-29  | Jrue Holiday REB over 4.5 (5+)       | MEM @ POR | draftkings   |   2.67 | +5.4%  | 0.8%          | won      |             1.67 |                           1.34 |
| 2026-10-28  | AJ Dybantsa PA under 13.5            | WAS @ CLE | draftkings   |   1.93 | +18.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Clint Capela PR under 13.5           | HOU @ MIL | draftkings   |   1.98 | +12.0% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Clint Capela PTS under 7.5           | HOU @ MIL | draftkings   |   1.81 | +11.5% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Kevin Durant AST over 5.5 (6+)       | HOU @ MIL | draftkings   |   3.63 | +10.9% | 1.0%          | lost     |            -1    |                          -1.04 |
| 2026-10-28  | Saddiq Bey PR over 19.5 (20+)        | DEN @ NOP | draftkings   |   3.49 | +10.1% | 1.0%          | lost     |            -1    |                          -1.01 |
| 2026-10-28  | Klay Thompson 3PM under 2.5          | MIA @ ATL | draftkings   |   1.87 | +9.3%  | 2.0%          | won      |             0.87 |                           1.74 |
| 2026-10-28  | LAC +4.5                             | LAL @ LAC | tab          |   1.9  | +8.4%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Saddiq Bey PTS over 14.5 (15+)       | DEN @ NOP | draftkings   |   3.01 | +7.9%  | 1.0%          | lost     |            -1    |                          -0.99 |
| 2026-10-28  | Trae Young PA under 30.5             | WAS @ CLE | draftkings   |   1.94 | +6.8%  | 1.8%          | won      |             0.94 |                           1.68 |
| 2026-10-28  | Trae Young PTS under 20.5            | WAS @ CLE | draftkings   |   1.94 | +6.7%  | 1.8%          | won      |             0.94 |                           1.67 |
| 2026-10-28  | Clint Capela REB under 7.5           | HOU @ MIL | draftkings   |   1.72 | +6.6%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Trae Young PRA under 32.5            | WAS @ CLE | draftkings   |   1.93 | +6.3%  | 1.7%          | won      |             0.93 |                           1.56 |
| 2026-10-28  | Kobe Sanders 3PM under 1.5           | LAL @ LAC | draftkings   |   2.17 | +6.1%  | 1.3%          | won      |             1.17 |                           1.53 |
| 2026-10-28  | Daniss Jenkins REB over 3.5 (4+)     | CHA @ DET | draftkings   |   3.03 | +5.9%  | 0.7%          | lost     |            -1    |                          -0.73 |
| 2026-10-28  | Tim Hardaway Jr. 3PM under 1.5       | MIA @ ATL | draftkings   |   2.04 | +5.8%  | 1.4%          | lost     |            -1    |                          -1.39 |
| 2026-10-28  | Trae Young AST under 10.5            | WAS @ CLE | draftkings   |   1.72 | +5.6%  | 1.9%          | won      |             0.72 |                           1.4  |
| 2026-10-28  | Paul Reed REB under 9.5              | CHA @ DET | draftkings   |   1.71 | +5.4%  | 1.9%          | won      |             0.71 |                           1.33 |
| 2026-10-28  | Kevin Durant AST over 4.5 (5+)       | HOU @ MIL | draftkings   |   2.31 | +5.2%  | 1.0%          | lost     |            -1    |                          -0.99 |
| 2026-10-28  | Trae Young PR under 22.5             | WAS @ CLE | draftkings   |   1.93 | +5.1%  | 1.4%          | won      |             0.93 |                           1.26 |
| 2026-10-28  | Myles Turner 3PM under 1.5           | HOU @ MIL | draftkings   |   1.99 | +5.0%  | 1.3%          | won      |             0.99 |                           1.26 |

</details>

## Not on Sportsbet (EV ≥ 5%, odds ≤ 4)

TODAY.md's "not on Sportsbet" table: bets that meet the best-bets rules (EV ≥ 5%, odds ≤ 4, no news flag), but in a market Sportsbet doesn't list (bookie_markets.json), so only other books have them. Final pre-tip list at the price shown then.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |      2 |     1 |              0.2 |             10 |                   3.7 |                                  0.02 |                    0.4 |
| Last 30 days |      9 |     3 |             -2.7 |            -30 |                  12.2 |                                 -3.09 |                  -25.3 |

<details><summary>Every not-on-Sportsbet bet (9)</summary>

| date (US)   | bet                              | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-14  | Yves Missi PTS under 5.5         | DEN @ NOP | draftkings  |   2.2  | +8.1%  | 1.7%          | won      |             1.2  |                           2.02 |
| 2026-11-11  | Gui Santos PTS over 7.5 (8+)     | GSW @ HOU | draftkings  |   2.67 | +22.0% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-10  | Bennett Stirtz PTS over 6.5 (7+) | OKC @ POR | pointsbetau |   2.05 | +5.3%  | 1.3%          | won      |             1.05 |                           1.32 |
| 2026-11-09  | Ryan Kalkbrenner PTS under 7.5   | CLE @ CHA | draftkings  |   1.99 | +5.6%  | 1.4%          | lost     |            -1    |                          -1.42 |
| 2026-11-01  | Keon Ellis PTS over 6.5 (7+)     | BKN @ IND | pointsbetau |   2.05 | +7.6%  | 1.8%          | lost     |            -1    |                          -1.82 |
| 2026-10-31  | Jrue Holiday AST over 6.5 (7+)   | POR @ UTA | draftkings  |   3.61 | +6.2%  | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-31  | Julian Champagnie PTS under 10.5 | MIN @ SAS | tab         |   2    | +5.7%  | 1.4%          | lost     |            -1    |                          -1.42 |
| 2026-10-30  | Leonard Miller PTS under 8.5     | CHI @ BOS | pointsbetau |   2.05 | +5.9%  | 1.4%          | won      |             1.05 |                           1.47 |
| 2026-10-29  | Derik Queen PR over 24.5 (25+)   | SAC @ NOP | draftkings  |   3.58 | +6.6%  | 0.6%          | lost     |            -1    |                          -0.64 |

</details>

## Best bets: any time in the day (secondary)

**Any time in the day.** Every bet that showed in the table at any point, graded at the first price it showed at. Bets that dropped off before tip (news, price moves) count here.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |   avg CLV % |   beat closing % |   bets with an Aussie close |   avg CLV vs Aussie close % |   beat Aussie close % |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|------------:|-----------------:|----------------------------:|----------------------------:|----------------------:|
| Last 7 days  |     25 |    14 |             6.3  |           25.2 |                  22.5 |                                  6.6  |                   29.3 |         4.9 |             84   |                          14 |                        10.9 |                  85.7 |
| Last 30 days |    108 |    42 |             0.66 |            0.6 |                  79.3 |                                 -1.92 |                   -2.4 |         3.6 |             54.6 |                          43 |                         6.1 |                  55.8 |

<details><summary>Every bet that showed at any time (odds = first price shown) (108)</summary>

| date (US)   | bet                                       | game      | book          |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:--------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-17  | Sion James PTS over 7.5 (8+)              | CHA @ LAL | draftkings    |   2.56 | +28.2% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-17  | POR to win                                | POR @ MIN | draftkings    |   2.5  | +11.8% | 2.0%          | lost     |            -1    |                          -1.98 |
| 2026-11-17  | Brandon Miller PTS over 19.5 (20+)        | CHA @ LAL | draftkings    |   2.28 | -3.7%  | 0.0%          | won      |             1.28 |                           0    |
| 2026-11-17  | TOR to win                                | NYK @ TOR | draftkings    |   2.5  | -5.5%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-16  | Danny Wolf PTS over 9.5 (10+)             | PHI @ BKN | draftkings    |   2.67 | +30.3% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-16  | Meleek Thomas PTS over 12.5 (13+)         | CHI @ CLE | unibet        |   2.12 | +5.5%  | 1.2%          | lost     |            -1    |                          -1.22 |
| 2026-11-16  | Jalen Suggs PTS over 7.5 (8+)             | ORL @ BOS | tab           |   1.75 | +4.9%  | 1.6%          | won      |             0.75 |                           1.23 |
| 2026-11-16  | Sam Hauser PTS over 6.5 (7+)              | ORL @ BOS | pointsbetau   |   2.15 | +2.8%  | 0.6%          | won      |             1.15 |                           0.7  |
| 2026-11-15  | Ryan Kalkbrenner PTS over 4.5 (5+)        | CHA @ LAC | pointsbetau   |   2.1  | +7.2%  | 1.6%          | won      |             1.1  |                           1.79 |
| 2026-11-15  | Dylan Cardwell PTS over 5.5 (6+)          | OKC @ SAC | pointsbetau   |   2.05 | +6.7%  | 1.6%          | won      |             1.05 |                           1.67 |
| 2026-11-15  | Josh Okogie PTS over 4.5 (5+)             | SAS @ UTA | draftkings    |   1.98 | +6.4%  | 1.6%          | won      |             0.98 |                           1.59 |
| 2026-11-15  | MIL to win                                | ATL @ MIL | draftkings    |   3.81 | +5.2%  | 0.5%          | lost     |            -1    |                          -0.46 |
| 2026-11-15  | Anthony Davis STL over 1.5 (2+)           | HOU @ WAS | draftkings    |   2.67 | -5.0%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-15  | Walker Kessler REB over 10.5 (11+)        | LAL @ PHX | draftkings    |   2.06 | -5.2%  | 0.0%          | won      |             1.06 |                           0    |
| 2026-11-15  | IND to win                                | IND @ PHI | draftkings    |   3.61 | -5.8%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-14  | Day'Ron Sharpe PTS over 9.5 (10+)         | BKN @ MEM | pointsbetau   |   2.05 | +7.2%  | 1.7%          | won      |             1.05 |                           1.78 |
| 2026-11-14  | Cedric Coward PTS over 14.5 (15+)         | BKN @ MEM | pointsbetau   |   1.95 | +5.5%  | 1.5%          | won      |             0.95 |                           1.39 |
| 2026-11-14  | CLE to win                                | DAL @ CLE | draftkings    |   2.37 | -1.4%  | 0.0%          | won      |             1.37 |                           0    |
| 2026-11-14  | MEM to win                                | BKN @ MEM | draftkings    |   1.68 | -7.4%  | 0.0%          | won      |             0.68 |                           0    |
| 2026-11-13  | Nic Claxton PTS over 9.5 (10+)            | ATL @ CHI | draftkings    |   2.78 | +8.5%  | 1.2%          | lost     |            -1    |                          -1.19 |
| 2026-11-13  | Aday Mara PTS under 11.5                  | OKC @ LAC | draftkings    |   2.06 | +6.5%  | 1.5%          | won      |             1.06 |                           1.63 |
| 2026-11-13  | IND to win                                | NYK @ IND | sportsbet     |   3.85 | -2.8%  | 0.0%          | won      |             2.85 |                           0    |
| 2026-11-11  | Kenrich Williams PTS over 9.5 (10+)       | OKC @ POR | draftkings    |   2.97 | +13.5% | 1.9%          | won      |             1.97 |                           3.66 |
| 2026-11-11  | OKC to win                                | OKC @ POR | draftkings    |   2.24 | -4.0%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-11  | GSW to win                                | GSW @ HOU | draftkings    |   3.17 | -5.5%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-10  | Scoot Henderson PTS over 11.5 (12+)       | OKC @ POR | draftkings    |   2.74 | +13.2% | 1.9%          | lost     |            -1    |                          -1.89 |
| 2026-11-10  | Isaiah Collier PTS over 11.5 (12+)        | MIA @ UTA | draftkings    |   2.55 | +8.7%  | 1.4%          | won      |             1.55 |                           2.17 |
| 2026-11-10  | Oso Ighodaro PTS over 6.5 (7+)            | LAC @ PHX | pointsbetau   |   2.15 | +3.6%  | 0.8%          | lost     |            -1    |                          -0.78 |
| 2026-11-10  | MIA to win                                | MIA @ UTA | draftkings    |   1.4  | -2.3%  | 0.0%          | won      |             0.4  |                           0    |
| 2026-11-10  | Shai Gilgeous-Alexander AST over 5.5 (6+) | OKC @ POR | draftkings    |   2.22 | -2.5%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-09  | Jamison Battle PTS over 9.5 (10+)         | MEM @ TOR | draftkings    |   2.23 | +19.0% | 2.0%          | won      |             1.23 |                           2.46 |
| 2026-11-09  | PHX to win                                | SAS @ PHX | draftkings    |   3.82 | +3.2%  | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-09  | DEN to win                                | DEN @ HOU | draftkings    |   3.86 | +1.6%  | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-11-09  | LAL to win                                | LAL @ ATL | draftkings    |   2.18 | -3.7%  | 0.0%          | won      |             1.18 |                           0    |
| 2026-11-09  | TOR to win                                | MEM @ TOR | draftkings    |   2.01 | -5.3%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-09  | Stephon Castle STL over 0.5 (1+)          | SAS @ PHX | draftkings    |   2.47 | -6.0%  | 0.0%          | won      |             1.47 |                           0    |
| 2026-11-08  | Brice Sensabaugh PTS over 9.5 (10+)       | UTA @ MIN | draftkings    |   2.44 | +30.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-08  | LAL to win                                | LAL @ DET | draftkings    |   2.55 | +0.9%  | 0.1%          | won      |             1.55 |                           0.17 |
| 2026-11-08  | Kyle Kuzma 3PM over 1.5 (2+)              | BOS @ MIL | draftkings    |   2.79 | -6.1%  | 0.0%          | won      |             1.79 |                           0    |
| 2026-11-07  | Meleek Thomas 3PM over 1.5 (2+)           | NYK @ CLE | draftkings    |   2.43 | +22.3% | 2.0%          | won      |             1.43 |                           2.86 |
| 2026-11-07  | ORL to win                                | ORL @ GSW | draftkings    |   3.31 | +5.5%  | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-11-07  | IND to win                                | DEN @ IND | betfair_ex_au |   3.61 | +1.6%  | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-11-06  | Deandre Ayton PTS over 7.5 (8+)           | WAS @ ATL | tab           |   1.85 | +3.4%  | 1.0%          | won      |             0.85 |                           0.85 |
| 2026-11-06  | WAS to win                                | WAS @ ATL | draftkings    |   3.61 | -4.7%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-06  | Austin Reaves 3PM over 1.5 (2+)           | POR @ LAL | draftkings    |   2.47 | -6.8%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-02  | CHA to win                                | DET @ CHA | draftkings    |   2.82 | +8.0%  | 1.1%          | lost     |            -1    |                          -1.1  |
| 2026-11-02  | Victor Wembanyama BLK over 4.5 (5+)       | UTA @ SAS | draftkings    |   3.73 | -2.8%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-01  | Gui Santos PTS over 9.5 (10+)             | LAC @ GSW | draftkings    |   2.4  | +21.8% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-01  | Nolan Traore PTS under 12.5               | BKN @ IND | draftkings    |   1.99 | +7.0%  | 1.8%          | lost     |            -1    |                          -1.75 |
| 2026-11-01  | Rui Hachimura PTS under 15.5              | LAC @ GSW | draftkings    |   1.97 | +6.6%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-01  | Scottie Barnes AST over 7.5 (8+)          | TOR @ LAL | draftkings    |   3.82 | +6.5%  | 0.6%          | lost     |            -1    |                          -0.59 |
| 2026-11-01  | Jamal Shead PTS over 6.5 (7+)             | TOR @ LAL | pointsbetau   |   2.05 | +5.8%  | 1.4%          | won      |             1.05 |                           1.45 |
| 2026-11-01  | Aaron Nesmith PTS over 12.5 (13+)         | BKN @ IND | pointsbetau   |   2.05 | +5.5%  | 1.3%          | lost     |            -1    |                          -1.32 |
| 2026-11-01  | Gui Santos REB over 5.5 (6+)              | LAC @ GSW | draftkings    |   3.81 | +5.4%  | 0.5%          | lost     |            -1    |                          -0.48 |
| 2026-11-01  | Jarace Walker AST over 3.5 (4+)           | BKN @ IND | draftkings    |   3.74 | +3.9%  | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-11-01  | Jarace Walker PRA over 24.5 (25+)         | BKN @ IND | draftkings    |   3.71 | +2.9%  | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-11-01  | Pascal Siakam PTS over 29.5 (30+)         | BKN @ IND | draftkings    |   3.88 | +0.6%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-10-31  | Tari Eason REB over 7.5 (8+)              | OKC @ HOU | draftkings    |   3.9  | +13.6% | 1.2%          | lost     |            -1    |                          -1.19 |
| 2026-10-31  | Zach Edey PTS over 8.5 (9+)               | SAC @ MEM | pointsbetau   |   2.05 | +11.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Donovan Clingan PTS over 11.5 (12+)       | POR @ UTA | draftkings    |   2.26 | +8.2%  | 1.6%          | lost     |            -1    |                          -1.63 |
| 2026-10-31  | Donovan Clingan BLK over 2.5 (3+)         | POR @ UTA | draftkings    |   3.38 | +7.0%  | 0.7%          | lost     |            -1    |                          -0.66 |
| 2026-10-31  | Jaylen Wells PTS over 11.5 (12+)          | SAC @ MEM | unibet        |   1.66 | +6.2%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Trey Murphy III AST over 3.5 (4+)         | ATL @ NOP | draftkings    |   2.25 | +6.1%  | 1.3%          | won      |             1.25 |                           1.57 |
| 2026-10-31  | Julian Champagnie PTS under 10.5          | MIN @ SAS | tab           |   2    | +5.7%  | 1.4%          | lost     |            -1    |                          -1.42 |
| 2026-10-31  | Saddiq Bey PRA over 24.5 (25+)            | ATL @ NOP | draftkings    |   3.67 | +5.7%  | 0.6%          | won      |             2.67 |                           1.52 |
| 2026-10-31  | Shai Gilgeous-Alexander AST over 7.5 (8+) | OKC @ HOU | draftkings    |   3.87 | +5.6%  | 0.5%          | lost     |            -1    |                          -0.49 |
| 2026-10-31  | Darryn Peterson PTS under 14.5            | POR @ UTA | betright      |   1.92 | +5.3%  | 1.5%          | lost     |            -1    |                          -1.45 |
| 2026-10-31  | Kel'el Ware PTS under 9.5                 | CLE @ MIL | pointsbetau   |   2    | +4.9%  | 1.2%          | lost     |            -1    |                          -1.22 |
| 2026-10-31  | Precious Achiuwa PA over 19.5 (20+)       | SAC @ MEM | draftkings    |   3.97 | +4.6%  | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-10-31  | Jabari Smith Jr. REB over 7.5 (8+)        | OKC @ HOU | draftkings    |   3.3  | +4.5%  | 0.5%          | won      |             2.3  |                           1.24 |
| 2026-10-31  | Jrue Holiday PTS over 14.5 (15+)          | POR @ UTA | draftkings    |   2.15 | +3.8%  | 0.9%          | lost     |            -1    |                          -0.85 |
| 2026-10-31  | Jaxson Hayes REB over 7.5 (8+)            | POR @ UTA | draftkings    |   3.53 | +3.6%  | 0.4%          | lost     |            -1    |                          -0.36 |
| 2026-10-31  | Zion Williamson PRA over 34.5 (35+)       | ATL @ NOP | draftkings    |   3.43 | +3.0%  | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-10-31  | Anfernee Simons REB over 3.5 (4+)         | PHI @ CHA | draftkings    |   3.99 | -1.5%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-31  | Sion James PTS over 5.5 (6+)              | PHI @ CHA | draftkings    |   2.05 | -3.6%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-30  | Khaman Maluach PTS under 7.5              | DEN @ PHX | pointsbetau   |   2.05 | +11.5% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-30  | Jarace Walker PTS over 10.5 (11+)         | IND @ MIA | pointsbetau   |   2    | +7.3%  | 1.8%          | won      |             1    |                           1.82 |
| 2026-10-30  | Pascal Siakam AST over 5.5 (6+)           | IND @ MIA | draftkings    |   3.52 | +6.6%  | 0.6%          | lost     |            -1    |                          -0.62 |
| 2026-10-30  | Naz Reid PTS under 17.5                   | CHA @ WAS | pointsbetau   |   2    | +5.8%  | 1.5%          | won      |             1    |                           1.45 |
| 2026-10-30  | Payton Pritchard PTS under 15.5           | CHI @ BOS | unibet        |   2.06 | +4.9%  | 1.2%          | lost     |            -1    |                          -1.16 |
| 2026-10-30  | Aaron Gordon PTS under 14.5               | DEN @ PHX | pointsbetau   |   2    | +4.7%  | 1.2%          | lost     |            -1    |                          -1.18 |
| 2026-10-30  | Jarace Walker AST over 3.5 (4+)           | IND @ MIA | draftkings    |   3.5  | +3.2%  | 0.4%          | won      |             2.5  |                           0.9  |
| 2026-10-30  | Scottie Barnes AST over 7.5 (8+)          | ORL @ TOR | draftkings    |   4    | +0.1%  | 0.0%          | lost     |            -1    |                          -0.01 |
| 2026-10-30  | IND to win                                | IND @ MIA | draftkings    |   3.6  | -3.2%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-30  | BKN to win                                | DET @ BKN | draftkings    |   3.5  | -3.3%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-30  | PHI to win                                | NYK @ PHI | draftkings    |   2.3  | -4.0%  | 0.0%          | won      |             1.3  |                           0    |
| 2026-10-29  | Kingston Flemings PTS under 8.5           | CLE @ ATL | tab           |   2    | +8.5%  | 2.0%          | won      |             1    |                           2    |
| 2026-10-29  | Precious Achiuwa PTS over 14.5 (15+)      | SAC @ NOP | draftkings    |   3.54 | +6.9%  | 0.7%          | won      |             2.54 |                           1.73 |
| 2026-10-29  | Damian Lillard AST over 5.5 (6+)          | MEM @ POR | draftkings    |   3.9  | +6.4%  | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-10-29  | Darius Acuff Jr. REB over 4.5 (5+)        | SAC @ NOP | draftkings    |   3.94 | +6.0%  | 0.5%          | won      |             2.94 |                           1.38 |
| 2026-10-29  | Ja Morant AST over 7.5 (8+)               | MEM @ POR | draftkings    |   3.28 | +5.4%  | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-29  | Derik Queen REB over 9.5 (10+)            | SAC @ NOP | draftkings    |   3.45 | +4.3%  | 0.5%          | lost     |            -1    |                          -0.48 |
| 2026-10-29  | Cam Spencer AST over 4.5 (5+)             | MEM @ POR | draftkings    |   3.8  | +2.5%  | 0.2%          | won      |             2.8  |                           0.7  |
| 2026-10-29  | Jeremiah Fears REB over 4.5 (5+)          | SAC @ NOP | draftkings    |   3.94 | -5.6%  | 0.0%          | won      |             2.94 |                           0    |
| 2026-10-28  | Darius Garland PTS over 29.5 (30+)        | LAL @ LAC | draftkings    |   3.67 | +5.8%  | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-10-28  | Jarace Walker REB over 6.5 (7+)           | PHI @ IND | draftkings    |   3.43 | +5.8%  | 0.6%          | won      |             2.43 |                           1.46 |
| 2026-10-28  | IND +5.5                                  | PHI @ IND | unibet        |   1.95 | +5.4%  | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-28  | Pascal Siakam PRA over 39.5 (40+)         | PHI @ IND | draftkings    |   3.57 | +5.0%  | 0.5%          | won      |             2.57 |                           1.26 |
| 2026-10-28  | Scottie Barnes AST over 7.5 (8+)          | ORL @ TOR | draftkings    |   3.88 | +2.2%  | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-28  | Ace Bailey PR over 24.5 (25+)             | SAS @ UTA | draftkings    |   3.96 | +0.4%  | 0.1%          | won      |             2.96 |                           0.15 |

</details>

CLV vs Aussie close uses the Australian books' own closing prices (Sportsbet, TAB, PointsBet and others, margin removed, averaged) for the same bet, where they priced it. That's the market you bet into, so it's the more relevant test; Aussie books often only list points props, so coverage is partial.

CLV (closing-line value) compares the price taken with the final no-vig market price before tip. Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings for months.

## Best player props per game (main lines)

The "Best player props" box in each game's section of TODAY.md: every main-line prop with positive EV, no news flag and offered at Sportsbet, as listed on the last update before tip, graded at the price shown then. These include edges under 5%, so expect a thinner margin than best bets.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |    143 |    75 |             7.85 |            5.5 |                  58.9 |                                 12.33 |                   20.9 |
| Last 30 days |    431 |   203 |           -27.92 |           -6.5 |                 168.2 |                                 -2.74 |                   -1.6 |

<details><summary>Every graded game prop (431)</summary>

| date (US)   | bet                                     | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:----------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-17  | Sion James PTS over 7.5 (8+)            | CHA @ LAL | draftkings  |   2.56 | +28.2% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-17  | Jrue Holiday PTS over 13.5 (14+)        | POR @ MIN | tab         |   1.95 | +3.7%  | 1.0%          | won      |             0.95 |                           0.93 |
| 2026-11-17  | Ja'Kobe Walter PTS under 10.5           | NYK @ TOR | tab         |   1.95 | +3.1%  | 0.8%          | lost     |            -1    |                          -0.82 |
| 2026-11-17  | Brice Sensabaugh PTS over 13.5 (14+)    | UTA @ LAC | pointsbetau |   2.05 | +2.9%  | 0.7%          | won      |             1.05 |                           0.72 |
| 2026-11-17  | Moussa Diabate PTS over 8.5 (9+)        | CHA @ LAL | pointsbetau |   2.05 | +1.9%  | 0.4%          | lost     |            -1    |                          -0.45 |
| 2026-11-17  | Devin Vassell PTS over 11.5 (12+)       | DET @ SAS | draftkings  |   2.35 | +1.8%  | 0.3%          | won      |             1.35 |                           0.46 |
| 2026-11-17  | Rui Hachimura PTS under 13.5            | UTA @ LAC | pointsbetau |   2.05 | +1.8%  | 0.4%          | lost     |            -1    |                          -0.43 |
| 2026-11-17  | Quentin Grimes PTS under 12.5           | CHA @ LAL | betright    |   2    | +1.8%  | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-11-17  | Ace Bailey PTS over 14.5 (15+)          | UTA @ LAC | pointsbetau |   2.05 | +1.1%  | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-11-17  | John Collins PTS over 11.5 (12+)        | DET @ SAS | draftkings  |   2    | +1.0%  | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-11-17  | Paul Reed PTS over 10.5 (11+)           | DET @ SAS | pointsbetau |   1.9  | +1.0%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-17  | Donovan Clingan PTS under 12.5          | POR @ MIN | draftkings  |   1.88 | +0.9%  | 0.3%          | won      |             0.88 |                           0.23 |
| 2026-11-17  | Keyonte George PTS under 21.5           | UTA @ LAC | pointsbetau |   2.05 | +0.8%  | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-11-17  | Darryn Peterson PTS under 20.5          | UTA @ LAC | pointsbetau |   1.95 | +0.2%  | 0.1%          | won      |             0.95 |                           0.06 |
| 2026-11-16  | Danny Wolf PTS over 9.5 (10+)           | PHI @ BKN | draftkings  |   2.68 | +30.3% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-16  | Meleek Thomas PTS over 12.5 (13+)       | CHI @ CLE | unibet      |   2.12 | +5.5%  | 1.2%          | lost     |            -1    |                          -1.22 |
| 2026-11-16  | Jalen Suggs PTS over 7.5 (8+)           | ORL @ BOS | tab         |   1.75 | +4.9%  | 1.6%          | won      |             0.75 |                           1.23 |
| 2026-11-16  | Luka Garza PTS under 9.5                | ORL @ BOS | draftkings  |   1.93 | +3.5%  | 0.9%          | won      |             0.93 |                           0.86 |
| 2026-11-16  | Tristan da Silva PTS over 11.5 (12+)    | ORL @ BOS | draftkings  |   2.24 | +3.4%  | 0.7%          | won      |             1.24 |                           0.86 |
| 2026-11-16  | Sam Hauser PTS over 6.5 (7+)            | ORL @ BOS | pointsbetau |   2.15 | +2.8%  | 0.6%          | won      |             1.15 |                           0.7  |
| 2026-11-16  | Anfernee Simons PTS under 10.5          | PHI @ BKN | tab         |   2    | +2.3%  | 0.6%          | won      |             1    |                           0.57 |
| 2026-11-16  | Egor Demin PTS under 9.5                | PHI @ BKN | pointsbetau |   2.05 | +2.0%  | 0.5%          | won      |             1.05 |                           0.49 |
| 2026-11-16  | Jaylen Wells PTS over 11.5 (12+)        | MEM @ WAS | unibet      |   1.88 | +1.6%  | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-11-16  | Davion Mitchell PTS over 13.5 (14+)     | HOU @ MIA | sportsbet   |   2    | +1.4%  | 0.4%          | won      |             1    |                           0.36 |
| 2026-11-16  | Jarrett Allen PTS under 14.5            | CHI @ CLE | pointsbetau |   2.05 | +1.3%  | 0.3%          | won      |             1.05 |                           0.34 |
| 2026-11-16  | Derik Queen PTS over 10.5 (11+)         | GSW @ NOP | draftkings  |   1.99 | +1.3%  | 0.3%          | won      |             0.99 |                           0.33 |
| 2026-11-16  | Klay Thompson PTS under 13.5            | HOU @ MIA | draftkings  |   1.95 | +1.1%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-16  | Desmond Bane PTS under 17.5             | ORL @ BOS | unibet      |   1.93 | +1.1%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-16  | Jalen Suggs PTS over 8.5 (9+)           | ORL @ BOS | draftkings  |   2.03 | +1.0%  | 0.2%          | won      |             1.03 |                           0.26 |
| 2026-11-16  | Georges Niang PTS over 8.5 (9+)         | GSW @ NOP | pointsbetau |   2.05 | +0.9%  | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-11-16  | Julius Randle PTS under 19.5            | PHI @ BKN | tab         |   1.95 | +0.6%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-16  | James Harden PTS over 17.5 (18+)        | CHI @ CLE | pointsbetau |   1.9  | +0.6%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-16  | Anfernee Simons PTS over 11.5 (12+)     | PHI @ BKN | draftkings  |   2.37 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-16  | Josh Giddey PTS under 12.5              | CHI @ CLE | pointsbetau |   2    | +0.5%  | 0.1%          | won      |             1    |                           0.13 |
| 2026-11-16  | Andrew Wiggins PTS over 9.5 (10+)       | HOU @ MIA | pointsbetau |   2    | +0.4%  | 0.1%          | won      |             1    |                           0.11 |
| 2026-11-16  | Draymond Green PR over 11.5 (12+)       | GSW @ NOP | draftkings  |   2.01 | +0.4%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-16  | Derrick White PTS under 12.5            | ORL @ BOS | pointsbetau |   2.05 | +0.4%  | 0.1%          | won      |             1.05 |                           0.08 |
| 2026-11-16  | Alex Sarr PTS over 11.5 (12+)           | MEM @ WAS | sportsbet   |   1.96 | +0.3%  | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-11-16  | AJ Dybantsa PTS under 16.5              | MEM @ WAS | draftkings  |   1.89 | +0.3%  | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-11-16  | Jordan Goodwin PTS under 8.5            | PHX @ DEN | draftkings  |   1.92 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-16  | Georges Niang PTS over 7.5 (8+)         | GSW @ NOP | tab         |   1.8  | +0.0%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-15  | Ryan Kalkbrenner PTS over 4.5 (5+)      | CHA @ LAC | pointsbetau |   2.1  | +7.2%  | 1.6%          | won      |             1.1  |                           1.79 |
| 2026-11-15  | Dylan Cardwell PTS over 5.5 (6+)        | OKC @ SAC | pointsbetau |   2.05 | +6.7%  | 1.6%          | won      |             1.05 |                           1.67 |
| 2026-11-15  | Josh Okogie PTS over 4.5 (5+)           | SAS @ UTA | draftkings  |   1.98 | +6.4%  | 1.6%          | won      |             0.98 |                           1.59 |
| 2026-11-15  | Keegan Murray PTS over 13.5 (14+)       | OKC @ SAC | sportsbet   |   2    | +3.9%  | 1.0%          | lost     |            -1    |                          -0.97 |
| 2026-11-15  | Moussa Diabate PTS under 8.5            | CHA @ LAC | tab         |   2    | +3.0%  | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-11-15  | Kevin Durant PTS over 21.5 (22+)        | HOU @ WAS | pointsbetau |   1.95 | +2.6%  | 0.7%          | won      |             0.95 |                           0.65 |
| 2026-11-15  | Keldon Johnson PTS over 9.5 (10+)       | SAS @ UTA | pointsbetau |   1.9  | +1.6%  | 0.4%          | won      |             0.9  |                           0.4  |
| 2026-11-15  | Daniel Gafford PTS over 7.5 (8+)        | DAL @ BOS | draftkings  |   1.88 | +1.6%  | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-11-15  | Stephon Castle PTS over 16.5 (17+)      | SAS @ UTA | unibet      |   1.95 | +1.5%  | 0.4%          | won      |             0.95 |                           0.38 |
| 2026-11-15  | Isaiah Hartenstein PTS under 9.5        | OKC @ SAC | pointsbetau |   2.05 | +1.5%  | 0.4%          | won      |             1.05 |                           0.38 |
| 2026-11-15  | Kyshawn George PTS over 14.5 (15+)      | HOU @ WAS | pointsbetau |   2    | +1.4%  | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-11-15  | Reed Sheppard PTS over 12.5 (13+)       | HOU @ WAS | tab         |   2    | +1.3%  | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-11-15  | Sion James PTS over 6.5 (7+)            | CHA @ LAC | draftkings  |   2.03 | +1.2%  | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-11-15  | Devin Booker PTS under 24.5             | LAL @ PHX | pointsbetau |   2    | +1.1%  | 0.3%          | won      |             1    |                           0.28 |
| 2026-11-15  | Ivica Zubac PTS under 13.5              | IND @ PHI | unibet      |   1.95 | +1.0%  | 0.3%          | won      |             0.95 |                           0.26 |
| 2026-11-15  | VJ Edgecombe PTS under 13.5             | IND @ PHI | tab         |   2    | +1.0%  | 0.2%          | won      |             1    |                           0.25 |
| 2026-11-15  | Derrick Jones Jr. PTS under 10.5        | CHA @ LAC | draftkings  |   1.93 | +0.7%  | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-11-15  | Karl-Anthony Towns PTS under 19.5       | NYK @ TOR | sportsbet   |   2.02 | +0.6%  | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-15  | Sandro Mamukelashvili PTS under 11.5    | LAL @ PHX | pointsbetau |   1.9  | +0.6%  | 0.2%          | won      |             0.9  |                           0.14 |
| 2026-11-15  | LeBron James PTS over 17.5 (18+)        | IND @ PHI | draftkings  |   1.99 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-15  | Tyler Herro PTS over 22.5 (23+)         | ATL @ MIL | sportsbet   |   2.05 | +0.1%  | 0.0%          | lost     |            -1    |                          -0.04 |
| 2026-11-14  | Day'Ron Sharpe PTS over 9.5 (10+)       | BKN @ MEM | pointsbetau |   2.05 | +7.2%  | 1.7%          | won      |             1.05 |                           1.78 |
| 2026-11-14  | Cedric Coward PTS over 14.5 (15+)       | BKN @ MEM | pointsbetau |   1.95 | +5.5%  | 1.5%          | won      |             0.95 |                           1.39 |
| 2026-11-14  | Egor Demin PTS under 11.5               | BKN @ MEM | pointsbetau |   2    | +3.0%  | 0.8%          | won      |             1    |                           0.75 |
| 2026-11-14  | Nolan Traore PTS over 11.5 (12+)        | BKN @ MEM | draftkings  |   2.01 | +2.5%  | 0.6%          | lost     |            -1    |                          -0.63 |
| 2026-11-14  | Ausar Thompson PTS under 10.5           | DET @ MIA | tab         |   2    | +2.0%  | 0.5%          | won      |             1    |                           0.5  |
| 2026-11-14  | Mario Hezonja PTS over 14.5 (15+)       | DAL @ CLE | sportsbet   |   2.05 | +1.5%  | 0.4%          | won      |             1.05 |                           0.39 |
| 2026-11-14  | Klay Thompson PTS over 12.5 (13+)       | DET @ MIA | unibet      |   1.93 | +1.5%  | 0.4%          | won      |             0.93 |                           0.37 |
| 2026-11-14  | John Collins PTS under 11.5             | DET @ MIA | tab         |   2    | +1.3%  | 0.3%          | won      |             1    |                           0.32 |
| 2026-11-14  | Kyrie Irving PTS under 22.5             | DAL @ CLE | betright    |   1.98 | +1.2%  | 0.3%          | lost     |            -1    |                          -0.31 |
| 2026-11-14  | Saddiq Bey PTS over 18.5 (19+)          | DEN @ NOP | sportsbet   |   2.02 | +0.9%  | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-11-14  | Meleek Thomas PTS over 17.5 (18+)       | DAL @ CLE | pointsbetau |   1.95 | +0.8%  | 0.2%          | won      |             0.95 |                           0.19 |
| 2026-11-14  | Julius Randle PTS under 22.5            | BKN @ MEM | draftkings  |   1.95 | +0.4%  | 0.1%          | won      |             0.95 |                           0.1  |
| 2026-11-14  | Naji Marshall PTS over 10.5 (11+)       | DAL @ CLE | pointsbetau |   2    | +0.2%  | 0.1%          | won      |             1    |                           0.06 |
| 2026-11-14  | Bobby Portis PTS over 6.5 (7+)          | DET @ MIA | unibet      |   1.94 | +0.2%  | 0.0%          | won      |             0.94 |                           0.04 |
| 2026-11-14  | Giannis Antetokounmpo PTS under 28.5    | DET @ MIA | draftkings  |   1.96 | +0.1%  | 0.0%          | lost     |            -1    |                          -0.03 |
| 2026-11-13  | Nic Claxton PTS over 9.5 (10+)          | ATL @ CHI | draftkings  |   2.78 | +8.5%  | 1.2%          | lost     |            -1    |                          -1.19 |
| 2026-11-13  | Aday Mara PTS under 11.5                | OKC @ LAC | draftkings  |   2.06 | +6.5%  | 1.5%          | won      |             1.06 |                           1.63 |
| 2026-11-13  | Scoot Henderson PTS over 11.5 (12+)     | POR @ SAC | draftkings  |   2.35 | +4.4%  | 0.8%          | lost     |            -1    |                          -0.82 |
| 2026-11-13  | Bam Adebayo PTS over 18.5 (19+)         | CLE @ MIA | pointsbetau |   2.05 | +3.7%  | 0.9%          | won      |             1.05 |                           0.92 |
| 2026-11-13  | Tristan da Silva PTS under 12.5         | MIL @ ORL | draftkings  |   1.96 | +3.6%  | 0.9%          | won      |             0.96 |                           0.91 |
| 2026-11-13  | Wendell Carter Jr. PTS under 12.5       | MIL @ ORL | tab         |   1.95 | +3.1%  | 0.8%          | won      |             0.95 |                           0.77 |
| 2026-11-13  | Jaylon Tyson PTS under 10.5             | CLE @ MIA | unibet      |   1.97 | +2.6%  | 0.7%          | lost     |            -1    |                          -0.67 |
| 2026-11-13  | Cam Spencer PTS over 8.5 (9+)           | MEM @ NOP | sportsbet   |   2.05 | +2.3%  | 0.5%          | won      |             1.05 |                           0.58 |
| 2026-11-13  | Amen Thompson PTS over 16.5 (17+)       | UTA @ HOU | pointsbetau |   2.05 | +2.1%  | 0.5%          | lost     |            -1    |                          -0.49 |
| 2026-11-13  | Pascal Siakam PTS over 20.5 (21+)       | NYK @ IND | pointsbetau |   2.05 | +1.9%  | 0.5%          | lost     |            -1    |                          -0.46 |
| 2026-11-13  | Jordan Poole PTS over 9.5 (10+)         | MEM @ NOP | tab         |   1.95 | +1.7%  | 0.4%          | won      |             0.95 |                           0.42 |
| 2026-11-13  | Josh Green PTS over 4.5 (5+)            | UTA @ HOU | sportsbet   |   2.02 | +1.7%  | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-11-13  | Gui Santos PTS over 6.5 (7+)            | GSW @ SAS | pointsbetau |   2.1  | +1.4%  | 0.3%          | won      |             1.1  |                           0.35 |
| 2026-11-13  | Cameron Boozer PTS under 17.5           | MEM @ NOP | pointsbetau |   2    | +1.1%  | 0.3%          | won      |             1    |                           0.28 |
| 2026-11-13  | Charles Bassey PTS over 4.5 (5+)        | GSW @ SAS | pointsbetau |   1.9  | +1.1%  | 0.3%          | won      |             0.9  |                           0.26 |
| 2026-11-13  | Keyonte George PTS under 20.5           | UTA @ HOU | pointsbetau |   2    | +1.0%  | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-13  | Peyton Watson PTS under 12.5            | CLE @ MIA | pointsbetau |   2.05 | +0.9%  | 0.2%          | won      |             1.05 |                           0.22 |
| 2026-11-13  | Brook Lopez PTS under 11.5              | OKC @ LAC | tab         |   1.9  | +0.8%  | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-11-13  | Nickeil Alexander-Walker PTS under 22.5 | ATL @ CHI | pointsbetau |   2    | +0.7%  | 0.2%          | won      |             1    |                           0.18 |
| 2026-11-13  | De'Aaron Fox PTS under 13.5             | GSW @ SAS | draftkings  |   1.97 | +0.6%  | 0.2%          | won      |             0.97 |                           0.16 |
| 2026-11-13  | Scoot Henderson PTS over 10.5 (11+)     | POR @ SAC | draftkings  |   2.02 | +0.6%  | 0.1%          | won      |             1.02 |                           0.15 |
| 2026-11-13  | Zach LaVine PTS under 19.5              | POR @ SAC | pointsbetau |   2    | +0.6%  | 0.1%          | won      |             1    |                           0.15 |
| 2026-11-13  | Kevin Durant PTS over 21.5 (22+)        | UTA @ HOU | sportsbet   |   1.96 | +0.5%  | 0.1%          | won      |             0.96 |                           0.12 |

</details>

## Day by day (last 30)

Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising count means something in the inputs is going wrong.

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean | sanity flags        |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|:--------------------|
| 2026-11-17 |       5 |        90 | 4.59 / 6.02                      | 5.03 / 5.37                     |          0.25 | 0 (none)            |
| 2026-11-16 |       8 |       138 | 4.73 / 5.04                      | 4.83 / 5.00                     |          0.62 | 0 (none)            |
| 2026-11-15 |       9 |       161 | 6.14 / 6.37                      | 5.48 / 5.79                     |          0.95 | 0 (none)            |
| 2026-11-14 |       5 |        87 | 7.15 / 8.34                      | 5.27 / 5.60                     |          1.78 | 0 (none)            |
| 2026-11-13 |       9 |       157 | 5.38 / 6.06                      | 5.45 / 5.59                     |          0.5  | 0 (none)            |
| 2026-11-12 |       4 |        75 | 5.56 / 5.94                      | 4.80 / 5.19                     |         -0.34 | 0 (none)            |
| 2026-11-11 |      10 |       179 | 4.90 / 5.77                      | 4.87 / 4.86                     |          0.63 | 0 (none)            |
| 2026-11-10 |       6 |       107 | 4.88 / 4.88                      | 4.71 / 4.79                     |          0.71 | 0 (none)            |
| 2026-11-09 |       8 |       136 | 5.70 / 6.20                      | 5.38 / 5.43                     |          0.97 | 0 (none)            |
| 2026-11-08 |       7 |       131 | 4.29 / 5.01                      | 4.94 / 4.95                     |          0.46 | 0 (none)            |
| 2026-11-07 |       7 |       118 | 4.87 / 5.63                      | 4.61 / 4.64                     |          1.08 | 0 (none)            |
| 2026-11-06 |       9 |       154 | 5.04 / 5.84                      | 5.00 / 5.36                     |          0.84 | 0 (none)            |
| 2026-11-02 |      15 |       238 | 5.52 / 6.23                      | 5.36 / 5.45                     |          1.27 | 2 (player points 2) |
| 2026-11-01 |       4 |        68 | 3.57 / 5.07                      | 4.79 / 4.52                     |          0.21 | 0 (none)            |
| 2026-10-31 |       7 |       115 | 6.06 / 6.77                      | 6.29 / 6.17                     |          1.87 | 0 (none)            |
| 2026-10-30 |      10 |       176 | 4.05 / 5.25                      | 4.96 / 5.12                     |          0.5  | 0 (none)            |
| 2026-10-29 |       3 |        53 | 4.86 / 5.88                      | 6.06 / 5.94                     |          1.13 | 0 (none)            |
| 2026-10-28 |      12 |       164 | 4.99 / 5.61                      | 5.21 / 5.43                     |          1.23 |                     |
