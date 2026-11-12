# Model health

Rebuilt 2026-11-12 by the nightly grading run. Back to [TODAY.md](TODAY.md).

## Verdict: **SAME**

Last 7 days 1.8% better than baseline, 30 days 1.4%: steady.

How to read this: the model is judged against a simple rule anyone could use, each player's average over his last 10 games. "% better" is how much smaller the model's average miss is. Watch the trend, not single days: one game day is mostly noise.

## Projection accuracy (players the model had at 90%+ to play)

| window                      |   game days |   players |   minutes miss |   minutes % better than last-10 |   minutes lean (+ = too high) |   points miss |   points % better than last-10 |   points lean (+ = too high) |
|:----------------------------|------------:|----------:|---------------:|--------------------------------:|------------------------------:|--------------:|-------------------------------:|-----------------------------:|
| Last 7 days                 |           6 |       825 |           4.96 |                            11.5 |                          2.13 |          4.93 |                            1.8 |                         0.78 |
| Last 30 days                |          12 |      1639 |           4.96 |                            13.3 |                          1.83 |          5.15 |                            1.4 |                         0.93 |
| Season                      |          12 |      1639 |           4.96 |                            13.3 |                          1.83 |          5.15 |                            1.4 |                         0.93 |
| Backtest (held-out 2025-26) |             |           |                |                            15.4 |                               |               |                            5.4 |                              |

Live should sit near the backtest line. Well below it for weeks means the model is doing worse on new games than it did in testing (overfitting or something broke).

## Best bets (EV ≥ 5%, odds ≤ 4)

**Main record: the final list.** The bets still in TODAY.md's best-bets table on the last update before each game's tip (after lineups and injury news), graded at the price shown then.

Each table shows two ways of counting: units at a flat 1-unit stake on every bet (so results compare cleanly), and profit at the sheet's suggested stake, the quarter-Kelly % of bankroll capped at 2% that TODAY.md shows on every bet. ROI (sheet stakes) is that profit divided by the total staked. Rows are the last 7 days, last 30 days and whole season; a longer period only gets its own row once it holds more bets than the shorter one.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |      7 |     4 |             3.01 |           43   |                  11.7 |                                  6.4  |                   54.7 |
| Last 30 days |     31 |    12 |            -0.27 |           -0.9 |                  39.3 |                                  0.63 |                    1.6 |

<details><summary>Every final-list bet (31)</summary>

| date (US)   | bet                                       | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
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
| Last 7 days  |     67 |     6 |            13.4  |           20   |                  13.4 |                                 -1.18 |                   -8.8 |
| Last 30 days |    195 |    12 |           -16.64 |           -8.5 |                  61.1 |                                 -4.31 |                   -7   |

<details><summary>Every long shot (195)</summary>

| date (US)   | bet                                         | game      | book          |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:--------------------------------------------|:----------|:--------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-11  | CHI to win                                  | SAS @ CHI | betfair_ex_au |  10.5  | +25.9% | 0.7%          | lost     |             -1   |                          -0.68 |
| 2026-11-11  | Derik Queen PRA over 34.5 (35+)             | BKN @ NOP | draftkings    |  19.4  | +13.7% | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-11  | Pascal Siakam AST over 7.5 (8+)             | WAS @ IND | draftkings    |  16.2  | +13.0% | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-11  | MIL to win                                  | LAL @ MIL | betfair_ex_au |   7.65 | +12.4% | 0.5%          | lost     |             -1   |                          -0.47 |
| 2026-11-11  | Ryan Rollins AST over 7.5 (8+)              | LAL @ MIL | draftkings    |  17.2  | +12.0% | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-11  | Pascal Siakam PA over 44.5 (45+)            | WAS @ IND | draftkings    |  22    | +11.9% | 0.1%          | lost     |             -1   |                          -0.14 |
| 2026-11-11  | Derik Queen PRA over 29.5 (30+)             | BKN @ NOP | draftkings    |   8.8  | +10.8% | 0.4%          | lost     |             -1   |                          -0.35 |
| 2026-11-11  | Shai Gilgeous-Alexander AST over 9.5 (10+)  | OKC @ POR | draftkings    |  11.8  | +9.8%  | 0.2%          | lost     |             -1   |                          -0.23 |
| 2026-11-11  | Kevin Durant AST over 7.5 (8+)              | GSW @ HOU | draftkings    |  15.6  | +9.3%  | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-11  | Victor Wembanyama REB over 17.5 (18+)       | SAS @ CHI | draftkings    |  12.8  | +8.9%  | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-11  | Dejounte Murray AST over 9.5 (10+)          | BKN @ NOP | draftkings    |  13.4  | +8.8%  | 0.2%          | lost     |             -1   |                          -0.18 |
| 2026-11-11  | Derik Queen PTS over 19.5 (20+)             | BKN @ NOP | draftkings    |  13.2  | +8.8%  | 0.2%          | lost     |             -1   |                          -0.18 |
| 2026-11-11  | Jamal Shead AST over 11.5 (12+)             | BOS @ TOR | draftkings    |  15.8  | +8.7%  | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-11  | Victor Wembanyama PTS over 49.5 (50+)       | SAS @ CHI | draftkings    |  25    | +8.5%  | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-11  | Pascal Siakam PA over 39.5 (40+)            | WAS @ IND | draftkings    |  10.8  | +7.6%  | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-11  | Derik Queen AST over 5.5 (6+)               | BKN @ NOP | draftkings    |  13.8  | +7.6%  | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-11  | Andrew Nembhard PRA over 39.5 (40+)         | WAS @ IND | draftkings    |  11    | +7.5%  | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-11  | Victor Wembanyama PRA over 64.5 (65+)       | SAS @ CHI | draftkings    |  16.4  | +7.5%  | 0.1%          | lost     |             -1   |                          -0.12 |
| 2026-11-11  | Andrew Nembhard AST over 13.5 (14+)         | WAS @ IND | draftkings    |  14    | +7.3%  | 0.1%          | lost     |             -1   |                          -0.14 |
| 2026-11-11  | Jamal Shead PA over 24.5 (25+)              | BOS @ TOR | draftkings    |  13.2  | +7.3%  | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-11  | Victor Wembanyama REB over 19.5 (20+)       | SAS @ CHI | draftkings    |  22    | +7.3%  | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-11  | Jaime Jaquez Jr. AST over 5.5 (6+)          | LAL @ MIL | draftkings    |   9.5  | +7.0%  | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-11  | Ryan Rollins PTS over 19.5 (20+)            | LAL @ MIL | draftkings    |  12.6  | +6.9%  | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-11  | Andrew Nembhard PRA over 44.5 (45+)         | WAS @ IND | draftkings    |  21    | +6.4%  | 0.1%          | lost     |             -1   |                          -0.08 |
| 2026-11-11  | Alex Caruso PA over 19.5 (20+)              | OKC @ POR | draftkings    |  11.6  | +6.2%  | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-10  | Shai Gilgeous-Alexander AST over 9.5 (10+)  | OKC @ POR | draftkings    |  11.8  | +10.5% | 0.2%          | lost     |             -1   |                          -0.24 |
| 2026-11-10  | MIL to win                                  | MIL @ NYK | betfair_ex_au |   9.17 | +10.0% | 0.3%          | lost     |             -1   |                          -0.3  |
| 2026-11-10  | Shai Gilgeous-Alexander AST over 11.5 (12+) | OKC @ POR | draftkings    |  28    | +8.9%  | 0.1%          | lost     |             -1   |                          -0.08 |
| 2026-11-10  | Giannis Antetokounmpo PTS over 49.5 (50+)   | MIA @ UTA | draftkings    |  31    | +8.2%  | 0.1%          | lost     |             -1   |                          -0.07 |
| 2026-11-10  | Bam Adebayo PA over 34.5 (35+)              | MIA @ UTA | draftkings    |  14.2  | +7.0%  | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-10  | Precious Achiuwa PRA over 24.5 (25+)        | ORL @ SAC | draftkings    |   9    | +6.9%  | 0.2%          | lost     |             -1   |                          -0.22 |
| 2026-11-10  | Giannis Antetokounmpo PA over 54.5 (55+)    | MIA @ UTA | draftkings    |  22    | +6.5%  | 0.1%          | lost     |             -1   |                          -0.08 |
| 2026-11-10  | Sidy Cissoko PRA over 19.5 (20+)            | OKC @ POR | draftkings    |  16.4  | +5.8%  | 0.1%          | won      |             15.4 |                           1.39 |
| 2026-11-10  | Precious Achiuwa PTS over 14.5 (15+)        | ORL @ SAC | draftkings    |   8.3  | +5.4%  | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-10  | Precious Achiuwa PRA over 29.5 (30+)        | ORL @ SAC | draftkings    |  20.6  | +5.2%  | 0.1%          | lost     |             -1   |                          -0.07 |
| 2026-11-09  | Jeremiah Fears PA over 34.5 (35+)           | NOP @ GSW | draftkings    |  19.2  | +17.5% | 0.2%          | lost     |             -1   |                          -0.24 |
| 2026-11-09  | Andrew Nembhard AST over 11.5 (12+)         | IND @ DAL | draftkings    |  11.8  | +11.8% | 0.3%          | won      |             10.8 |                           2.92 |
| 2026-11-09  | Andrew Nembhard AST over 13.5 (14+)         | IND @ DAL | draftkings    |  26    | +11.8% | 0.1%          | lost     |             -1   |                          -0.12 |
| 2026-11-09  | Jeremiah Fears PRA over 39.5 (40+)          | NOP @ GSW | draftkings    |  15    | +11.6% | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-09  | Andrew Nembhard PRA over 39.5 (40+)         | IND @ DAL | draftkings    |  14.6  | +11.0% | 0.2%          | lost     |             -1   |                          -0.2  |
| 2026-11-09  | Jeremiah Fears PR over 34.5 (35+)           | NOP @ GSW | draftkings    |  16.6  | +10.7% | 0.2%          | lost     |             -1   |                          -0.17 |
| 2026-11-09  | Pascal Siakam PRA over 49.5 (50+)           | IND @ DAL | draftkings    |  21    | +8.7%  | 0.1%          | lost     |             -1   |                          -0.11 |
| 2026-11-09  | Alex Sarr BLK over 3.5 (4+)                 | WAS @ DET | draftkings    |  14.2  | +8.6%  | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-09  | Jarace Walker REB over 7.5 (8+)             | IND @ DAL | draftkings    |  11.2  | +8.5%  | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-09  | Andrew Nembhard PA over 34.5 (35+)          | IND @ DAL | draftkings    |  11.4  | +8.4%  | 0.2%          | lost     |             -1   |                          -0.2  |
| 2026-11-09  | Andrew Nembhard PA over 39.5 (40+)          | IND @ DAL | draftkings    |  24    | +8.3%  | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-09  | Dejounte Murray AST over 9.5 (10+)          | NOP @ GSW | draftkings    |  12.4  | +8.3%  | 0.2%          | lost     |             -1   |                          -0.18 |
| 2026-11-09  | Kevin Durant PRA over 44.5 (45+)            | DEN @ HOU | draftkings    |  13.2  | +8.1%  | 0.2%          | lost     |             -1   |                          -0.17 |
| 2026-11-09  | Pascal Siakam AST over 7.5 (8+)             | IND @ DAL | draftkings    |  24    | +7.8%  | 0.1%          | won      |             23   |                           1.84 |
| 2026-11-09  | Pascal Siakam AST over 5.5 (6+)             | IND @ DAL | draftkings    |   7.7  | +7.6%  | 0.3%          | won      |              6.7 |                           1.88 |
| 2026-11-09  | Pascal Siakam PRA over 44.5 (45+)           | IND @ DAL | draftkings    |  11.2  | +7.4%  | 0.2%          | won      |             10.2 |                           1.84 |
| 2026-11-09  | Jeremiah Fears PRA over 34.5 (35+)          | NOP @ GSW | draftkings    |   6.86 | +6.9%  | 0.3%          | lost     |             -1   |                          -0.29 |
| 2026-11-09  | Jeremiah Fears PR over 29.5 (30+)           | NOP @ GSW | draftkings    |   7.2  | +6.8%  | 0.3%          | lost     |             -1   |                          -0.27 |
| 2026-11-09  | Andrew Nembhard PRA over 44.5 (45+)         | IND @ DAL | draftkings    |  26    | +6.6%  | 0.1%          | lost     |             -1   |                          -0.07 |
| 2026-11-09  | Kevin Durant PRA over 49.5 (50+)            | DEN @ HOU | draftkings    |  24    | +6.3%  | 0.1%          | lost     |             -1   |                          -0.07 |
| 2026-11-09  | Kevin Durant PA over 39.5 (40+)             | DEN @ HOU | draftkings    |  16.2  | +6.0%  | 0.1%          | lost     |             -1   |                          -0.1  |
| 2026-11-09  | Karlo Matkovic PTS over 14.5 (15+)          | NOP @ GSW | draftkings    |   8    | +6.0%  | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-09  | Kevin Durant PTS over 34.5 (35+)            | DEN @ HOU | draftkings    |  16.6  | +5.7%  | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-09  | Dejounte Murray AST over 11.5 (12+)         | NOP @ GSW | draftkings    |  29    | +5.6%  | 0.1%          | lost     |             -1   |                          -0.05 |
| 2026-11-09  | Daniss Jenkins PA over 24.5 (25+)           | WAS @ DET | draftkings    |   9.3  | +5.3%  | 0.2%          | won      |              8.3 |                           1.33 |
| 2026-11-08  | SAC to win                                  | MIA @ SAC | draftkings    |   5.29 | +18.4% | 1.1%          | lost     |             -1   |                          -1.07 |
| 2026-11-08  | MIL to win                                  | BOS @ MIL | betfair_ex_au |   6.89 | +13.2% | 0.6%          | lost     |             -1   |                          -0.56 |
| 2026-11-08  | UTA to win                                  | UTA @ MIN | betfair_ex_au |   6.13 | +6.0%  | 0.3%          | lost     |             -1   |                          -0.29 |
| 2026-11-07  | WAS to win                                  | WAS @ OKC | betfair_ex_au |   5.75 | +5.6%  | 0.3%          | lost     |             -1   |                          -0.3  |
| 2026-11-06  | SAC to win                                  | SAS @ SAC | sportsbet     |  10    | +11.8% | 0.3%          | lost     |             -1   |                          -0.33 |
| 2026-11-06  | Darius Acuff Jr. AST over 11.5 (12+)        | SAS @ SAC | draftkings    |  17    | +6.6%  | 0.1%          | lost     |             -1   |                          -0.1  |
| 2026-11-06  | Precious Achiuwa PRA over 29.5 (30+)        | SAS @ SAC | draftkings    |  16.6  | +5.7%  | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-02  | UTA to win                                  | UTA @ SAS | ladbrokes_au  |  10    | +18.9% | 0.5%          | lost     |             -1   |                          -0.53 |
| 2026-11-02  | Brandin Podziemski PRA over 44.5 (45+)      | PHX @ GSW | draftkings    |  27    | +10.8% | 0.1%          | lost     |             -1   |                          -0.1  |
| 2026-11-02  | Precious Achiuwa PA over 29.5 (30+)         | SAC @ DAL | draftkings    |  27    | +8.3%  | 0.1%          | lost     |             -1   |                          -0.08 |
| 2026-11-01  | Pascal Siakam PTS over 44.5 (45+)           | BKN @ IND | draftkings    |  29    | +26.1% | 0.2%          | lost     |             -1   |                          -0.23 |
| 2026-11-01  | Noah Clowney REB over 7.5 (8+)              | BKN @ IND | draftkings    |  11.8  | +25.3% | 0.6%          | lost     |             -1   |                          -0.59 |
| 2026-11-01  | Pascal Siakam PA over 44.5 (45+)            | BKN @ IND | draftkings    |  15.2  | +25.2% | 0.4%          | lost     |             -1   |                          -0.44 |
| 2026-11-01  | Pascal Siakam PA over 49.5 (50+)            | BKN @ IND | draftkings    |  26    | +24.5% | 0.2%          | lost     |             -1   |                          -0.24 |
| 2026-11-01  | Pascal Siakam PRA over 54.5 (55+)           | BKN @ IND | draftkings    |  16.8  | +22.8% | 0.4%          | lost     |             -1   |                          -0.36 |
| 2026-11-01  | Pascal Siakam PTS over 39.5 (40+)           | BKN @ IND | draftkings    |  14.8  | +21.9% | 0.4%          | lost     |             -1   |                          -0.4  |
| 2026-11-01  | Julius Randle PTS over 34.5 (35+)           | BKN @ IND | draftkings    |  17.2  | +21.6% | 0.3%          | lost     |             -1   |                          -0.33 |
| 2026-11-01  | Jayson Tatum PTS over 44.5 (45+)            | BOS @ ORL | draftkings    |  22    | +20.0% | 0.2%          | lost     |             -1   |                          -0.24 |
| 2026-11-01  | Noah Clowney REB over 9.5 (10+)             | BKN @ IND | draftkings    |  28    | +17.8% | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-01  | Jayson Tatum PTS over 39.5 (40+)            | BOS @ ORL | draftkings    |  11.2  | +16.0% | 0.4%          | lost     |             -1   |                          -0.39 |
| 2026-11-01  | Pascal Siakam PRA over 49.5 (50+)           | BKN @ IND | draftkings    |   8.8  | +15.6% | 0.5%          | lost     |             -1   |                          -0.5  |
| 2026-11-01  | Jarace Walker PR over 24.5 (25+)            | BKN @ IND | draftkings    |   7.9  | +15.2% | 0.5%          | lost     |             -1   |                          -0.55 |
| 2026-11-01  | Jarace Walker PR over 29.5 (30+)            | BKN @ IND | draftkings    |  18.4  | +14.8% | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-01  | Gui Santos PRA over 24.5 (25+)              | LAC @ GSW | draftkings    |  10    | +14.4% | 0.4%          | lost     |             -1   |                          -0.4  |
| 2026-11-01  | Jayson Tatum PR over 54.5 (55+)             | BOS @ ORL | draftkings    |  18.2  | +14.1% | 0.2%          | lost     |             -1   |                          -0.2  |
| 2026-11-01  | Scottie Barnes AST over 9.5 (10+)           | TOR @ LAL | draftkings    |   9.5  | +14.1% | 0.4%          | lost     |             -1   |                          -0.41 |
| 2026-11-01  | Pascal Siakam PA over 39.5 (40+)            | BKN @ IND | draftkings    |   7.1  | +12.9% | 0.5%          | lost     |             -1   |                          -0.53 |
| 2026-11-01  | Scottie Barnes AST over 11.5 (12+)          | TOR @ LAL | draftkings    |  23    | +12.6% | 0.1%          | lost     |             -1   |                          -0.14 |
| 2026-11-01  | Scottie Barnes PA over 44.5 (45+)           | TOR @ LAL | draftkings    |  17.2  | +12.4% | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-01  | Julius Randle PTS over 29.5 (30+)           | BKN @ IND | draftkings    |   7.2  | +11.8% | 0.5%          | lost     |             -1   |                          -0.48 |
| 2026-11-01  | Jayson Tatum PR over 49.5 (50+)             | BOS @ ORL | draftkings    |   9.9  | +11.7% | 0.3%          | lost     |             -1   |                          -0.33 |
| 2026-11-01  | Julius Randle PTS over 39.5 (40+)           | BKN @ IND | draftkings    |  28    | +10.2% | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-01  | Pascal Siakam PTS over 34.5 (35+)           | BKN @ IND | draftkings    |   6.61 | +9.6%  | 0.4%          | lost     |             -1   |                          -0.43 |
| 2026-11-01  | Jayson Tatum REB over 13.5 (14+)            | BOS @ ORL | draftkings    |  13    | +9.2%  | 0.2%          | lost     |             -1   |                          -0.19 |
| 2026-11-01  | Pascal Siakam AST over 7.5 (8+)             | BKN @ IND | draftkings    |  12.2  | +8.8%  | 0.2%          | lost     |             -1   |                          -0.2  |
| 2026-10-31  | Kevin Durant AST over 7.5 (8+)              | OKC @ HOU | draftkings    |  21    | +57.8% | 0.7%          | lost     |             -1   |                          -0.72 |
| 2026-10-31  | Cameron Boozer REB over 13.5 (14+)          | SAC @ MEM | draftkings    |  10.6  | +28.9% | 0.8%          | lost     |             -1   |                          -0.75 |
| 2026-10-31  | Jaylen Brown PTS over 39.5 (40+)            | PHI @ CHA | draftkings    |  21    | +28.1% | 0.4%          | lost     |             -1   |                          -0.35 |
| 2026-10-31  | Tari Eason REB over 11.5 (12+)              | OKC @ HOU | draftkings    |  21    | +28.0% | 0.4%          | lost     |             -1   |                          -0.35 |
| 2026-10-31  | Cameron Boozer REB over 15.5 (16+)          | SAC @ MEM | draftkings    |  20    | +26.3% | 0.4%          | lost     |             -1   |                          -0.35 |

</details>

## Check news first (EV ≥ 5%, odds ≤ 4)

TODAY.md's "check news first" table: bets that clear the bar but where the model and market disagree by more than 15 points, so something may be missing. Final pre-tip list at the price shown then. Kept apart from best bets; if this stays unprofitable, the flag is doing its job.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |      2 |     2 |             2.2  |          110   |                   3.3 |                                  3.64 |                  110   |
| Last 30 days |     78 |    36 |            -3.76 |           -4.8 |                 119   |                                  0.83 |                    0.7 |

<details><summary>Every check-news bet (78)</summary>

| date (US)   | bet                                  | game      | book         |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-------------------------------------|:----------|:-------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
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
| Last 7 days  |      3 |     1 |            -0.95 |          -31.7 |                   4.7 |                                 -2.1  |                  -44.8 |
| Last 30 days |      8 |     2 |            -3.9  |          -48.8 |                  10.6 |                                 -5.11 |                  -48.4 |

<details><summary>Every not-on-Sportsbet bet (8)</summary>

| date (US)   | bet                              | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
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
| Last 7 days  |     23 |    10 |             0.42 |            1.8 |                  14.2 |                                  6.3  |                   44.3 |        10.6 |             60.9 |                           7 |                        18.3 |                  85.7 |
| Last 30 days |     86 |    29 |            -5.67 |           -6.6 |                  58.7 |                                 -4.85 |                   -8.3 |         3.2 |             45.3 |                          30 |                         5   |                  43.3 |

<details><summary>Every bet that showed at any time (odds = first price shown) (86)</summary>

| date (US)   | bet                                       | game      | book          |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:--------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
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
| 2026-10-28  | MIL to win                                | HOU @ MIL | betfair_ex_au |   3.76 | +0.3%  | 0.0%          | lost     |            -1    |                          -0.03 |
| 2026-10-28  | Ace Bailey PTS over 17.5 (18+)            | SAS @ UTA | draftkings    |   3.78 | -1.2%  | 0.0%          | won      |             2.78 |                           0    |
| 2026-10-28  | Total under 239.5                         | WAS @ CLE | playup        |   1.93 | -2.7%  | 0.0%          | won      |             0.93 |                           0    |
| 2026-10-28  | CHA +7.5                                  | CHA @ DET | unibet        |   1.96 | -2.8%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | IND to win                                | PHI @ IND | betfair_ex_au |   2.8  | -4.0%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | CHA to win                                | CHA @ DET | unibet        |   3.45 | -4.2%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | ATL -2.5                                  | MIA @ ATL | draftkings    |   1.98 | -4.5%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-10-28  | ATL to win                                | MIA @ ATL | tab           |   1.8  | -4.6%  | 0.0%          | lost     |            -1    |                          -0    |

</details>

CLV vs Aussie close uses the Australian books' own closing prices (Sportsbet, TAB, PointsBet and others, margin removed, averaged) for the same bet, where they priced it. That's the market you bet into, so it's the more relevant test; Aussie books often only list points props, so coverage is partial.

CLV (closing-line value) compares the price taken with the final no-vig market price before tip. Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings for months.

## Best player props per game (main lines)

The "Best player props" box in each game's section of TODAY.md: every main-line prop with positive EV, no news flag and offered at Sportsbet, as listed on the last update before tip, graded at the price shown then. These include edges under 5%, so expect a thinner margin than best bets.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |     95 |    49 |             4.05 |            4.3 |                  36.1 |                                  3.16 |                    8.7 |
| Last 30 days |    312 |   139 |           -37.09 |          -11.9 |                 117.4 |                                -12.58 |                  -10.7 |

<details><summary>Every graded game prop (312)</summary>

| date (US)   | bet                                       | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-11  | Kenrich Williams PTS over 9.5 (10+)       | OKC @ POR | draftkings  |   2.81 | +13.5% | 1.9%          | won      |             1.81 |                           3.37 |
| 2026-11-11  | Desmond Bane PTS over 19.5 (20+)          | ORL @ UTA | pointsbetau |   2    | +4.7%  | 1.2%          | won      |             1    |                           1.17 |
| 2026-11-11  | Tari Eason PTS over 8.5 (9+)              | GSW @ HOU | pointsbetau |   2.1  | +3.9%  | 0.9%          | lost     |            -1    |                          -0.88 |
| 2026-11-11  | Julian Champagnie PTS under 11.5          | SAS @ CHI | draftkings  |   1.94 | +3.2%  | 0.9%          | lost     |            -1    |                          -0.85 |
| 2026-11-11  | Brayden Burries PTS under 12.5            | LAL @ MIL | draftkings  |   1.94 | +3.0%  | 0.8%          | won      |             0.94 |                           0.75 |
| 2026-11-11  | Ja'Kobe Walter PTS under 12.5             | BOS @ TOR | draftkings  |   1.93 | +1.5%  | 0.4%          | lost     |            -1    |                          -0.39 |
| 2026-11-11  | Day'Ron Sharpe AST over 4.5 (5+)          | BKN @ NOP | draftkings  |   2.21 | +1.3%  | 0.3%          | won      |             1.21 |                           0.31 |
| 2026-11-11  | Wendell Carter Jr. PTS over 12.5 (13+)    | ORL @ UTA | unibet      |   1.97 | +1.2%  | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-11-11  | Landry Shamet PTS under 8.5               | CLE @ NYK | tab         |   1.9  | +1.1%  | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-11-11  | Zach Edey PTS over 8.5 (9+)               | DEN @ MEM | tab         |   1.95 | +1.1%  | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-11-11  | Nic Claxton PTS under 7.5                 | SAS @ CHI | tab         |   2    | +1.1%  | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-11-11  | AJ Green PTS over 5.5 (6+)                | LAL @ MIL | draftkings  |   1.97 | +0.8%  | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-11-11  | Michael Porter Jr. PTS under 23.5         | BKN @ NOP | pointsbetau |   2    | +0.7%  | 0.2%          | won      |             1    |                           0.17 |
| 2026-11-11  | Payton Pritchard PTS under 15.5           | BOS @ TOR | draftkings  |   1.99 | +0.7%  | 0.2%          | won      |             0.99 |                           0.17 |
| 2026-11-11  | Cameron Johnson PTS under 11.5            | DEN @ MEM | pointsbetau |   2.05 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-11  | Matas Buzelis PTS under 15.5              | SAS @ CHI | tab         |   1.95 | +0.5%  | 0.1%          | won      |             0.95 |                           0.12 |
| 2026-11-11  | Bilal Coulibaly PTS over 6.5 (7+)         | WAS @ IND | pointsbetau |   1.9  | +0.3%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-11  | Neemias Queta PTS under 9.5               | BOS @ TOR | pointsbetau |   2.05 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-11  | Kenrich Williams PTS over 8.5 (9+)        | OKC @ POR | tab         |   1.95 | +0.2%  | 0.1%          | won      |             0.95 |                           0.05 |
| 2026-11-11  | OG Anunoby PTS over 17.5 (18+)            | CLE @ NYK | draftkings  |   2.06 | +0.1%  | 0.0%          | lost     |            -1    |                          -0.03 |
| 2026-11-11  | Jarrett Allen PTS under 11.5              | CLE @ NYK | unibet      |   1.93 | +0.1%  | 0.0%          | won      |             0.93 |                           0.03 |
| 2026-11-11  | Austin Reaves PTS under 22.5              | LAL @ MIL | draftkings  |   1.97 | +0.1%  | 0.0%          | won      |             0.97 |                           0.03 |
| 2026-11-11  | Fred VanVleet PTS over 11.5 (12+)         | GSW @ HOU | unibet      |   1.92 | +0.1%  | 0.0%          | won      |             0.92 |                           0.02 |
| 2026-11-11  | Toumani Camara PTS under 12.5             | OKC @ POR | tab         |   1.95 | +0.0%  | 0.0%          | lost     |            -1    |                          -0.01 |
| 2026-11-11  | Kelly Oubre Jr. PTS over 9.5 (10+)        | WAS @ IND | tab         |   2    | +0.0%  | 0.0%          | won      |             1    |                           0.01 |
| 2026-11-11  | Tyler Herro PTS under 20.5                | LAL @ MIL | draftkings  |   1.92 | +0.0%  | 0.0%          | lost     |            -1    |                          -0.01 |
| 2026-11-10  | Scoot Henderson PTS over 11.5 (12+)       | OKC @ POR | draftkings  |   2.74 | +13.2% | 1.9%          | lost     |            -1    |                          -1.89 |
| 2026-11-10  | Isaiah Collier PTS over 11.5 (12+)        | MIA @ UTA | draftkings  |   2.55 | +8.7%  | 1.4%          | won      |             1.55 |                           2.17 |
| 2026-11-10  | Anfernee Simons PTS over 6.5 (7+)         | BOS @ PHI | pointsbetau |   2.15 | +3.2%  | 0.7%          | won      |             1.15 |                           0.81 |
| 2026-11-10  | Andre Drummond PTS over 4.5 (5+)          | MIL @ NYK | tab         |   2.05 | +2.8%  | 0.7%          | lost     |            -1    |                          -0.65 |
| 2026-11-10  | Tyrese Maxey PTS under 23.5               | BOS @ PHI | pointsbetau |   1.95 | +2.6%  | 0.7%          | lost     |            -1    |                          -0.69 |
| 2026-11-10  | Kobe Sanders PTS over 7.5 (8+)            | LAC @ PHX | pointsbetau |   2    | +2.3%  | 0.6%          | won      |             1    |                           0.57 |
| 2026-11-10  | Jalen Brunson PTS over 25.5 (26+)         | MIL @ NYK | sportsbet   |   2    | +1.0%  | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-10  | Kenrich Williams PTS under 7.5            | OKC @ POR | pointsbetau |   2.05 | +1.0%  | 0.2%          | won      |             1.05 |                           0.24 |
| 2026-11-10  | Jaylen Brown PTS under 21.5               | BOS @ PHI | betright    |   2    | +0.9%  | 0.2%          | won      |             1    |                           0.22 |
| 2026-11-10  | Sam Hauser PTS over 5.5 (6+)              | BOS @ PHI | draftkings  |   1.87 | +0.6%  | 0.2%          | won      |             0.87 |                           0.16 |
| 2026-11-10  | Miles Bridges PTS under 16.5              | LAC @ PHX | betright    |   1.9  | +0.6%  | 0.2%          | won      |             0.9  |                           0.14 |
| 2026-11-10  | Jayson Tatum PTS under 26.5               | BOS @ PHI | unibet      |   1.93 | +0.6%  | 0.1%          | won      |             0.93 |                           0.14 |
| 2026-11-10  | Khaman Maluach PTS over 6.5 (7+)          | LAC @ PHX | pointsbetau |   2.05 | +0.5%  | 0.1%          | won      |             1.05 |                           0.14 |
| 2026-11-10  | Giannis Antetokounmpo PTS over 28.5 (29+) | MIA @ UTA | draftkings  |   1.96 | +0.1%  | 0.0%          | won      |             0.96 |                           0.04 |
| 2026-11-10  | Toumani Camara PTS under 12.5             | OKC @ POR | draftkings  |   1.93 | +0.1%  | 0.0%          | won      |             0.93 |                           0.04 |
| 2026-11-10  | Landry Shamet PTS over 9.5 (10+)          | MIL @ NYK | betright    |   1.95 | +0.0%  | 0.0%          | won      |             0.95 |                           0.01 |
| 2026-11-09  | Jamison Battle PTS over 9.5 (10+)         | MEM @ TOR | draftkings  |   2.22 | +19.0% | 2.0%          | won      |             1.22 |                           2.44 |
| 2026-11-09  | Karlo Matkovic PTS over 8.5 (9+)          | NOP @ GSW | sportsbet   |   1.96 | +3.2%  | 0.8%          | lost     |            -1    |                          -0.82 |
| 2026-11-09  | John Collins PTS under 11.5               | WAS @ DET | tab         |   2    | +2.3%  | 0.6%          | lost     |            -1    |                          -0.57 |
| 2026-11-09  | Jerami Grant PTS under 10.5               | MEM @ TOR | tab         |   2    | +2.0%  | 0.5%          | lost     |            -1    |                          -0.49 |
| 2026-11-09  | Kevin Huerter PTS over 8.5 (9+)           | WAS @ DET | pointsbetau |   2    | +1.3%  | 0.3%          | won      |             1    |                           0.33 |
| 2026-11-09  | Jalen Johnson PTS under 20.5              | LAL @ ATL | tab         |   1.95 | +1.2%  | 0.3%          | won      |             0.95 |                           0.29 |
| 2026-11-09  | Brandon Williams PTS over 9.5 (10+)       | NOP @ GSW | pointsbetau |   1.95 | +0.8%  | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-11-09  | Jarrett Allen PTS under 12.5              | CLE @ CHA | tab         |   1.9  | +0.8%  | 0.2%          | won      |             0.9  |                           0.19 |
| 2026-11-09  | Derik Queen PTS over 12.5 (13+)           | NOP @ GSW | draftkings  |   2.03 | +0.5%  | 0.1%          | won      |             1.03 |                           0.13 |
| 2026-11-09  | Luka Doncic PTS under 37.5                | LAL @ ATL | tab         |   1.95 | +0.1%  | 0.0%          | won      |             0.95 |                           0.03 |
| 2026-11-09  | RJ Barrett PTS over 25.5 (26+)            | MEM @ TOR | tab         |   1.95 | +0.1%  | 0.0%          | lost     |            -1    |                          -0.02 |
| 2026-11-08  | Brice Sensabaugh PTS over 9.5 (10+)       | UTA @ MIN | draftkings  |   2.53 | +30.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-08  | Ryan Rollins PTS over 9.5 (10+)           | BOS @ MIL | pointsbetau |   2.05 | +2.6%  | 0.6%          | lost     |            -1    |                          -0.62 |
| 2026-11-08  | Jalen Smith PTS under 11.5                | PHI @ CHI | tab         |   1.95 | +1.9%  | 0.5%          | lost     |            -1    |                          -0.51 |
| 2026-11-08  | Derik Queen PTS over 8.5 (9+)             | NOP @ LAC | draftkings  |   2.03 | +1.3%  | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-11-08  | Anfernee Simons PTS under 9.5             | PHI @ CHI | tab         |   1.95 | +0.8%  | 0.2%          | won      |             0.95 |                           0.2  |
| 2026-11-08  | Ayo Dosunmu PTS under 18.5                | UTA @ MIN | draftkings  |   1.95 | +0.8%  | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-11-08  | Collin Sexton PTS over 11.5 (12+)         | LAL @ DET | unibet      |   2    | +0.7%  | 0.2%          | won      |             1    |                           0.18 |
| 2026-11-08  | Neemias Queta PTS under 9.5               | BOS @ MIL | tab         |   2    | +0.6%  | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-08  | Davion Mitchell PTS under 13.5            | MIA @ SAC | draftkings  |   1.94 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-08  | Tyler Herro PTS under 20.5                | BOS @ MIL | tab         |   1.87 | +0.5%  | 0.1%          | won      |             0.87 |                           0.11 |
| 2026-11-08  | Myles Turner PTS over 9.5 (10+)           | BOS @ MIL | pointsbetau |   2.05 | +0.3%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-08  | De'Andre Hunter PTS over 13.5 (14+)       | MIA @ SAC | pointsbetau |   2    | +0.2%  | 0.1%          | won      |             1    |                           0.06 |
| 2026-11-08  | Zion Williamson PTS under 19.5            | NOP @ LAC | sportsbet   |   2.02 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-08  | De'Andre Hunter PTS under 13.5            | MIA @ SAC | draftkings  |   2    | +0.1%  | 0.0%          | lost     |            -1    |                          -0.03 |
| 2026-11-07  | Meleek Thomas 3PM over 1.5 (2+)           | NYK @ CLE | draftkings  |   2.43 | +22.3% | 2.0%          | won      |             1.43 |                           2.86 |
| 2026-11-07  | Jabari Smith Jr. PTS over 14.5 (15+)      | HOU @ PHX | draftkings  |   2.13 | +4.6%  | 1.0%          | won      |             1.13 |                           1.14 |
| 2026-11-07  | Isaiah Hartenstein PTS over 8.5 (9+)      | WAS @ OKC | unibet      |   2.07 | +3.8%  | 0.9%          | lost     |            -1    |                          -0.89 |
| 2026-11-07  | Obi Toppin PTS over 11.5 (12+)            | DEN @ IND | draftkings  |   2.09 | +3.3%  | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-11-07  | Jalen Brunson PTS under 25.5              | NYK @ CLE | unibet      |   2.08 | +2.3%  | 0.5%          | lost     |            -1    |                          -0.53 |
| 2026-11-07  | Kenrich Williams PTS over 7.5 (8+)        | WAS @ OKC | draftkings  |   1.96 | +1.8%  | 0.5%          | won      |             0.96 |                           0.44 |
| 2026-11-07  | Oso Ighodaro PTS under 6.5                | HOU @ PHX | pointsbetau |   2.1  | +1.4%  | 0.3%          | won      |             1.1  |                           0.36 |
| 2026-11-07  | Alperen Sengun PTS under 19.5             | HOU @ PHX | pointsbetau |   2.05 | +1.4%  | 0.3%          | won      |             1.05 |                           0.34 |
| 2026-11-07  | Alex Caruso PTS over 7.5 (8+)             | WAS @ OKC | pointsbetau |   2.05 | +1.3%  | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-11-07  | Meleek Thomas PTS under 11.5              | NYK @ CLE | draftkings  |   1.93 | +1.3%  | 0.3%          | won      |             0.93 |                           0.32 |
| 2026-11-07  | Sidy Cissoko PTS over 4.5 (5+)            | SAS @ POR | neds        |   1.9  | +1.1%  | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-11-07  | Jrue Holiday PTS over 12.5 (13+)          | SAS @ POR | betright    |   1.94 | +1.0%  | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-11-07  | Damian Lillard PTS under 20.5             | SAS @ POR | tab         |   1.95 | +1.0%  | 0.2%          | won      |             0.95 |                           0.24 |
| 2026-11-07  | Onyeka Okongwu PTS under 12.5             | BKN @ ATL | pointsbetau |   2.05 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-07  | Evan Mobley PTS under 17.5                | NYK @ CLE | tab         |   1.95 | +0.4%  | 0.1%          | won      |             0.95 |                           0.1  |
| 2026-11-07  | Jamal Murray PTS over 23.5 (24+)          | DEN @ IND | pointsbetau |   2    | +0.3%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-07  | Nikola Jokic PTS under 26.5               | DEN @ IND | draftkings  |   1.93 | +0.3%  | 0.1%          | won      |             0.93 |                           0.08 |
| 2026-11-07  | Bilal Coulibaly PTS over 8.5 (9+)         | WAS @ OKC | tab         |   1.95 | +0.3%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-06  | Brice Sensabaugh PTS over 7.5 (8+)        | UTA @ DAL | sportsbet   |   2.08 | +4.2%  | 1.0%          | lost     |            -1    |                          -0.98 |
| 2026-11-06  | Evan Mobley PTS over 17.5 (18+)           | PHI @ CLE | tab         |   1.95 | +1.2%  | 0.3%          | won      |             0.95 |                           0.31 |
| 2026-11-06  | Daniel Gafford PTS over 9.5 (10+)         | UTA @ DAL | draftkings  |   2.14 | +1.2%  | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-06  | Joel Embiid PTS under 21.5                | PHI @ CLE | tab         |   1.95 | +1.2%  | 0.3%          | won      |             0.95 |                           0.29 |
| 2026-11-06  | Daniel Gafford PTS over 8.5 (9+)          | UTA @ DAL | draftkings  |   1.9  | +0.6%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-06  | Kyle Kuzma PTS over 9.5 (10+)             | TOR @ MIL | tab         |   1.9  | +0.3%  | 0.1%          | won      |             0.9  |                           0.08 |
| 2026-11-06  | Ziaire Williams PTS under 7.5             | POR @ LAL | draftkings  |   2.03 | +0.3%  | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-11-06  | Kyshawn George PTS over 15.5 (16+)        | WAS @ ATL | draftkings  |   1.98 | +0.2%  | 0.1%          | won      |             0.98 |                           0.05 |
| 2026-11-06  | Anfernee Simons PTS under 8.5             | PHI @ CLE | draftkings  |   2.01 | +0.1%  | 0.0%          | won      |             1.01 |                           0.02 |
| 2026-11-06  | Jamal Shead PTS under 11.5                | TOR @ MIL | tab         |   1.95 | +0.1%  | 0.0%          | won      |             0.95 |                           0.01 |
| 2026-11-02  | Duncan Robinson 3PM under 2.5             | DET @ CHA | draftkings  |   2.3  | +1.1%  | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-11-02  | Ajay Mitchell PRA under 25.5              | OKC @ CLE | draftkings  |   1.95 | +0.4%  | 0.1%          | lost     |            -1    |                          -0.11 |
| 2026-11-02  | Karl-Anthony Towns PR under 34.5          | BKN @ NYK | draftkings  |   1.84 | +0.2%  | 0.1%          | won      |             0.84 |                           0.07 |
| 2026-11-02  | Cade Cunningham RA under 14.5             | DET @ CHA | draftkings  |   1.75 | +0.1%  | 0.1%          | won      |             0.75 |                           0.04 |
| 2026-11-01  | Gui Santos PTS over 9.5 (10+)             | LAC @ GSW | draftkings  |   2.4  | +21.8% | 2.0%          | lost     |            -1    |                          -2    |

</details>

## Day by day (last 30)

Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising count means something in the inputs is going wrong.

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean | sanity flags        |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|:--------------------|
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
