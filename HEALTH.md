# Model health

Rebuilt 2026-11-28 by the nightly grading run. Back to [TODAY.md](TODAY.md).

## Verdict: **SAME**

Last 7 days 4.2% better than baseline, 30 days 3.2%: steady.

How to read this: the model is judged against a simple rule anyone could use, each player's average over his last 10 games. "% better" is how much smaller the model's average miss is. Watch the trend, not single days: one game day is mostly noise.

## Projection accuracy (players the model had at 90%+ to play)

| window                      |   game days |   players |   minutes miss |   minutes % better than last-10 |   minutes lean (+ = too high) |   points miss |   points % better than last-10 |   points lean (+ = too high) |
|:----------------------------|------------:|----------:|---------------:|--------------------------------:|------------------------------:|--------------:|-------------------------------:|-----------------------------:|
| Last 7 days                 |           5 |       718 |           4.34 |                            14.8 |                          0.79 |          4.58 |                            4.2 |                         0.68 |
| Last 30 days                |          25 |      3390 |           4.92 |                            12.9 |                          1.51 |          4.98 |                            3.2 |                         0.78 |
| Season                      |          27 |      3607 |           4.92 |                            12.9 |                          1.53 |          5.01 |                            3.1 |                         0.81 |
| Backtest (held-out 2025-26) |             |           |                |                            15.4 |                               |               |                            5.4 |                              |

Live should sit near the backtest line. Well below it for weeks means the model is doing worse on new games than it did in testing (overfitting or something broke).

## Best bets (EV ≥ 5%, odds ≤ 4)

**Main record: the final list.** The bets still in TODAY.md's best-bets table on the last update before each game's tip (after lineups and injury news), graded at the price shown then.

Each table shows two ways of counting: units at a flat 1-unit stake on every bet (so results compare cleanly), and profit at the sheet's suggested stake, the quarter-Kelly % of bankroll capped at 2% that TODAY.md shows on every bet. ROI (sheet stakes) is that profit divided by the total staked. Rows are the last 7 days, last 30 days and whole season; a longer period only gets its own row once it holds more bets than the shorter one.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |     12 |     7 |             2.65 |           22.1 |                  19.4 |                                  3.61 |                   18.7 |
| Last 30 days |     58 |    24 |            -5.09 |           -8.8 |                  85.4 |                                 -1.52 |                   -1.8 |
| Whole season |     63 |    28 |             0.86 |            1.4 |                  90.4 |                                  3.99 |                    4.4 |

<details><summary>Every final-list bet (63)</summary>

| date (US)   | bet                                       | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-27  | Brice Sensabaugh PTS over 11.5 (12+)      | DEN @ UTA | draftkings  |   2.38 | +8.4%  | 1.5%          | won      |             1.38 |                           2.11 |
| 2026-11-27  | Rudy Gobert PTS over 8.5 (9+)             | MEM @ MIN | pointsbetau |   2.05 | +5.1%  | 1.2%          | won      |             1.05 |                           1.28 |
| 2026-11-27  | Zaccharie Risacher PTS under 9.5          | DAL @ PHX | draftkings  |   2.01 | +5.1%  | 1.3%          | lost     |            -1    |                          -1.26 |
| 2026-11-25  | CLE to win                                | CLE @ NYK | draftkings  |   2.51 | +14.8% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-25  | Tre Jones PTS over 11.5 (12+)             | CHI @ CHA | tab         |   2    | +6.8%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-25  | Jose Alvarado PTS over 7.5 (8+)           | CLE @ NYK | draftkings  |   2.59 | +6.4%  | 1.0%          | won      |             1.59 |                           1.61 |
| 2026-11-24  | DET to win                                | DET @ ORL | draftkings  |   2.24 | +22.1% | 2.0%          | won      |             1.24 |                           2.48 |
| 2026-11-24  | John Collins PTS over 10.5 (11+)          | DET @ ORL | sportsbet   |   2.05 | +6.3%  | 1.5%          | won      |             1.05 |                           1.56 |
| 2026-11-23  | SAS to win                                | SAS @ SAC | draftkings  |   1.32 | +9.4%  | 2.0%          | won      |             0.32 |                           0.64 |
| 2026-11-22  | Obi Toppin PTS over 11.5 (12+)            | IND @ NYK | draftkings  |   2.29 | +5.9%  | 1.1%          | lost     |            -1    |                          -1.15 |
| 2026-11-21  | Taylor Hendricks PTS over 9.5 (10+)       | MEM @ MIN | draftkings  |   2.46 | +24.3% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-21  | NYK to win                                | POR @ NYK | draftkings  |   2.02 | +18.5% | 2.0%          | won      |             1.02 |                           2.04 |
| 2026-11-20  | Malik Monk PTS over 11.5 (12+)            | SAC @ LAL | draftkings  |   2.42 | +13.0% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-20  | Jamison Battle PTS over 11.5 (12+)        | TOR @ DET | draftkings  |   2.6  | +7.9%  | 1.2%          | lost     |            -1    |                          -1.23 |
| 2026-11-20  | DEN to win                                | HOU @ DEN | draftkings  |   2.03 | +7.3%  | 1.8%          | won      |             1.03 |                           1.83 |
| 2026-11-20  | Egor Demin PTS over 11.5 (12+)            | ORL @ BKN | draftkings  |   2.5  | +6.5%  | 1.1%          | lost     |            -1    |                          -1.08 |
| 2026-11-18  | PHI to win                                | PHI @ ORL | draftkings  |   2.46 | +11.9% | 2.0%          | won      |             1.46 |                           2.92 |
| 2026-11-18  | Javonte Green PTS over 7.5 (8+)           | DET @ NOP | tab         |   1.8  | +11.3% | 2.0%          | won      |             0.8  |                           1.6  |
| 2026-11-18  | Collin Murray-Boyles PTS over 14.5 (15+)  | WAS @ TOR | betright    |   2.05 | +8.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-18  | Kevin Huerter PTS over 14.5 (15+)         | DET @ NOP | sportsbet   |   2.05 | +5.5%  | 1.3%          | lost     |            -1    |                          -1.31 |
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
| Last 7 days  |    137 |    13 |            49.99 |           36.5 |                  28.9 |                                  1.99 |                    6.9 |
| Last 30 days |    468 |    31 |           -28.67 |           -6.1 |                 112.3 |                                 -7.73 |                   -6.9 |
| Whole season |    504 |    33 |           -48.71 |           -9.7 |                 125.6 |                                -13.94 |                  -11.1 |

<details><summary>Every long shot (504)</summary>

| date (US)   | bet                                         | game      | book       |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:--------------------------------------------|:----------|:-----------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-27  | Deni Avdija AST over 11.5 (12+)             | GSW @ POR | draftkings |  18.8  | +22.7% | 0.3%          | lost     |             -1   |                          -0.32 |
| 2026-11-27  | Jusuf Nurkic PA over 24.5 (25+)             | DEN @ UTA | draftkings |  20.8  | +18.3% | 0.2%          | lost     |             -1   |                          -0.23 |
| 2026-11-27  | Jalen Brunson PR over 49.5 (50+)            | MIA @ NYK | draftkings |  21    | +18.0% | 0.2%          | lost     |             -1   |                          -0.22 |
| 2026-11-27  | Jusuf Nurkic PR over 29.5 (30+)             | DEN @ UTA | draftkings |  17.6  | +17.3% | 0.3%          | lost     |             -1   |                          -0.26 |
| 2026-11-27  | Jalen Brunson PR over 44.5 (45+)            | MIA @ NYK | draftkings |  11    | +12.7% | 0.3%          | lost     |             -1   |                          -0.32 |
| 2026-11-27  | Scottie Barnes AST over 11.5 (12+)          | BKN @ TOR | draftkings |  24    | +12.5% | 0.1%          | lost     |             -1   |                          -0.14 |
| 2026-11-27  | Deni Avdija PRA over 59.5 (60+)             | GSW @ POR | draftkings |  21    | +12.2% | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-27  | Jrue Holiday AST over 11.5 (12+)            | GSW @ POR | draftkings |  24    | +12.1% | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-27  | Jrue Holiday AST over 9.5 (10+)             | GSW @ POR | draftkings |   9.8  | +12.1% | 0.3%          | lost     |             -1   |                          -0.34 |
| 2026-11-27  | Scottie Barnes AST over 9.5 (10+)           | BKN @ TOR | draftkings |   9.5  | +11.8% | 0.4%          | lost     |             -1   |                          -0.35 |
| 2026-11-27  | Jusuf Nurkic PTS over 14.5 (15+)            | DEN @ UTA | draftkings |   7.6  | +11.1% | 0.4%          | lost     |             -1   |                          -0.42 |
| 2026-11-27  | Joel Embiid PTS over 39.5 (40+)             | PHI @ IND | draftkings |  18.4  | +11.1% | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-27  | Jusuf Nurkic PTS over 19.5 (20+)            | DEN @ UTA | draftkings |  22    | +11.0% | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-27  | Sidy Cissoko AST over 5.5 (6+)              | GSW @ POR | draftkings |  21    | +10.3% | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-27  | Pascal Siakam PTS over 39.5 (40+)           | PHI @ IND | draftkings |  19.4  | +9.8%  | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-27  | Tyrese Maxey PTS over 39.5 (40+)            | PHI @ IND | draftkings |  17.4  | +9.4%  | 0.1%          | lost     |             -1   |                          -0.14 |
| 2026-11-27  | Deni Avdija PTS over 44.5 (45+)             | GSW @ POR | draftkings |  25    | +9.2%  | 0.1%          | lost     |             -1   |                          -0.1  |
| 2026-11-27  | Ayo Dosunmu PTS over 34.5 (35+)             | MEM @ MIN | draftkings |  18    | +8.9%  | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-27  | Pascal Siakam PA over 44.5 (45+)            | PHI @ IND | draftkings |  19    | +8.8%  | 0.1%          | lost     |             -1   |                          -0.12 |
| 2026-11-27  | Jaden McDaniels PR over 39.5 (40+)          | MEM @ MIN | draftkings |  15    | +8.7%  | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-27  | Rudy Gobert PR over 29.5 (30+)              | MEM @ MIN | draftkings |  11    | +8.7%  | 0.2%          | lost     |             -1   |                          -0.22 |
| 2026-11-27  | Jayson Tatum REB over 13.5 (14+)            | ATL @ BOS | draftkings |  18.2  | +8.6%  | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-27  | Scottie Barnes PTS over 39.5 (40+)          | BKN @ TOR | draftkings |  15.6  | +8.6%  | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-27  | Rudy Gobert PA over 19.5 (20+)              | MEM @ MIN | draftkings |  15.6  | +8.5%  | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-27  | Rudy Gobert AST over 3.5 (4+)               | MEM @ MIN | draftkings |   9.5  | +8.4%  | 0.2%          | won      |              8.5 |                           2.12 |
| 2026-11-25  | Cam Spencer AST over 9.5 (10+)              | LAC @ MEM | draftkings |  14.4  | +16.6% | 0.3%          | lost     |             -1   |                          -0.31 |
| 2026-11-25  | Jalen Brunson PRA over 54.5 (55+)           | CLE @ NYK | draftkings |  19    | +15.8% | 0.2%          | lost     |             -1   |                          -0.22 |
| 2026-11-25  | Jalen Brunson PA over 49.5 (50+)            | CLE @ NYK | draftkings |  15.8  | +14.8% | 0.2%          | lost     |             -1   |                          -0.25 |
| 2026-11-25  | Kevin Durant AST over 7.5 (8+)              | PHX @ HOU | draftkings |  15.6  | +13.5% | 0.2%          | lost     |             -1   |                          -0.23 |
| 2026-11-25  | Jalen Brunson PTS over 44.5 (45+)           | CLE @ NYK | draftkings |  21    | +13.1% | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-25  | Giannis Antetokounmpo PA over 54.5 (55+)    | MIA @ PHI | draftkings |  22    | +12.5% | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-25  | Jalen Brunson PRA over 59.5 (60+)           | CLE @ NYK | draftkings |  26    | +12.3% | 0.1%          | lost     |             -1   |                          -0.12 |
| 2026-11-25  | Jalen Brunson PTS over 39.5 (40+)           | CLE @ NYK | draftkings |  11.4  | +12.2% | 0.3%          | lost     |             -1   |                          -0.29 |
| 2026-11-25  | Jalen Brunson PRA over 49.5 (50+)           | CLE @ NYK | draftkings |   9.8  | +11.1% | 0.3%          | lost     |             -1   |                          -0.32 |
| 2026-11-25  | Shai Gilgeous-Alexander PA over 59.5 (60+)  | MIN @ OKC | draftkings |  26    | +11.1% | 0.1%          | lost     |             -1   |                          -0.11 |
| 2026-11-25  | Jalen Brunson PA over 54.5 (55+)            | CLE @ NYK | draftkings |  25    | +10.9% | 0.1%          | lost     |             -1   |                          -0.11 |
| 2026-11-25  | Draymond Green AST over 9.5 (10+)           | SAC @ GSW | draftkings |  16.8  | +10.6% | 0.2%          | won      |             15.8 |                           2.69 |
| 2026-11-25  | Cam Spencer AST over 11.5 (12+)             | LAC @ MEM | draftkings |  30    | +10.5% | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-25  | Jalen Brunson PR over 44.5 (45+)            | CLE @ NYK | draftkings |  12.6  | +9.9%  | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-25  | Jalen Brunson PR over 49.5 (50+)            | CLE @ NYK | draftkings |  22    | +9.8%  | 0.1%          | lost     |             -1   |                          -0.12 |
| 2026-11-25  | Shai Gilgeous-Alexander PRA over 64.5 (65+) | MIN @ OKC | draftkings |  24    | +9.3%  | 0.1%          | lost     |             -1   |                          -0.1  |
| 2026-11-25  | Amen Thompson PA over 29.5 (30+)            | PHX @ HOU | draftkings |  12    | +9.2%  | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-25  | Jalen Brunson PA over 44.5 (45+)            | CLE @ NYK | draftkings |   8    | +8.7%  | 0.3%          | lost     |             -1   |                          -0.31 |
| 2026-11-25  | Tre Jones PTS over 24.5 (25+)               | CHI @ CHA | draftkings |  18.6  | +8.3%  | 0.1%          | lost     |             -1   |                          -0.12 |
| 2026-11-25  | Cam Spencer AST over 7.5 (8+)               | LAC @ MEM | draftkings |   5.36 | +7.9%  | 0.4%          | lost     |             -1   |                          -0.45 |
| 2026-11-25  | Tre Jones PR over 24.5 (25+)                | CHI @ CHA | draftkings |   9.7  | +7.4%  | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-25  | Amen Thompson AST over 5.5 (6+)             | PHX @ HOU | draftkings |   6.69 | +7.3%  | 0.3%          | lost     |             -1   |                          -0.32 |
| 2026-11-25  | Giannis Antetokounmpo PA over 49.5 (50+)    | MIA @ PHI | draftkings |  11.2  | +7.1%  | 0.2%          | lost     |             -1   |                          -0.18 |
| 2026-11-25  | Amen Thompson AST over 7.5 (8+)             | PHX @ HOU | draftkings |  21    | +6.9%  | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-25  | Tre Jones PRA over 34.5 (35+)               | CHI @ CHA | draftkings |  16.2  | +6.5%  | 0.1%          | lost     |             -1   |                          -0.11 |
| 2026-11-24  | Daniss Jenkins PA over 34.5 (35+)           | DET @ ORL | draftkings |  19.4  | +18.0% | 0.2%          | lost     |             -1   |                          -0.24 |
| 2026-11-24  | Daniss Jenkins PA over 29.5 (30+)           | DET @ ORL | draftkings |   8.6  | +15.3% | 0.5%          | lost     |             -1   |                          -0.5  |
| 2026-11-24  | Trae Young AST over 13.5 (14+)              | BOS @ WAS | draftkings |  18.4  | +12.8% | 0.2%          | lost     |             -1   |                          -0.18 |
| 2026-11-24  | Kevin Huerter PA over 24.5 (25+)            | DET @ ORL | draftkings |  10.9  | +11.7% | 0.3%          | lost     |             -1   |                          -0.3  |
| 2026-11-24  | Nikola Jokic AST over 15.5 (16+)            | DAL @ DEN | draftkings |  13.8  | +10.2% | 0.2%          | lost     |             -1   |                          -0.2  |
| 2026-11-24  | Trae Young AST over 11.5 (12+)              | BOS @ WAS | draftkings |   8.1  | +8.9%  | 0.3%          | won      |              7.1 |                           2.27 |
| 2026-11-24  | Ausar Thompson PA over 24.5 (25+)           | DET @ ORL | draftkings |   9.3  | +8.7%  | 0.3%          | lost     |             -1   |                          -0.26 |
| 2026-11-24  | Nikola Jokic AST over 17.5 (18+)            | DAL @ DEN | draftkings |  27    | +8.0%  | 0.1%          | lost     |             -1   |                          -0.08 |
| 2026-11-24  | Paul Reed PTS over 24.5 (25+)               | DET @ ORL | draftkings |  22    | +7.2%  | 0.1%          | lost     |             -1   |                          -0.09 |
| 2026-11-24  | WAS to win                                  | BOS @ WAS | tabtouch   |   5    | +7.1%  | 0.4%          | lost     |             -1   |                          -0.45 |
| 2026-11-24  | Ausar Thompson PA over 29.5 (30+)           | DET @ ORL | draftkings |  23    | +6.6%  | 0.1%          | lost     |             -1   |                          -0.07 |
| 2026-11-24  | Jayson Tatum PTS over 44.5 (45+)            | BOS @ WAS | draftkings |  26    | +6.5%  | 0.1%          | lost     |             -1   |                          -0.06 |
| 2026-11-24  | Trae Young PRA over 39.5 (40+)              | BOS @ WAS | draftkings |  16.4  | +6.4%  | 0.1%          | lost     |             -1   |                          -0.1  |
| 2026-11-24  | Kevin Huerter PA over 29.5 (30+)            | DET @ ORL | draftkings |  24    | +5.8%  | 0.1%          | lost     |             -1   |                          -0.06 |
| 2026-11-24  | Paul Reed PTS over 19.5 (20+)               | DET @ ORL | draftkings |   8.1  | +5.7%  | 0.2%          | lost     |             -1   |                          -0.2  |
| 2026-11-24  | Jayson Tatum PA over 49.5 (50+)             | BOS @ WAS | draftkings |  18.6  | +5.4%  | 0.1%          | lost     |             -1   |                          -0.08 |
| 2026-11-24  | Paul Reed PR over 34.5 (35+)                | DET @ ORL | draftkings |  20.4  | +5.3%  | 0.1%          | lost     |             -1   |                          -0.07 |
| 2026-11-23  | Shai Gilgeous-Alexander PRA over 64.5 (65+) | OKC @ IND | draftkings |  27    | +25.7% | 0.2%          | lost     |             -1   |                          -0.25 |
| 2026-11-23  | Scottie Barnes PA over 44.5 (45+)           | MIL @ TOR | draftkings |  17    | +21.6% | 0.3%          | lost     |             -1   |                          -0.34 |
| 2026-11-23  | Precious Achiuwa PTS over 14.5 (15+)        | SAS @ SAC | draftkings |  18    | +19.1% | 0.3%          | lost     |             -1   |                          -0.28 |
| 2026-11-23  | Luka Doncic PRA over 69.5 (70+)             | UTA @ LAL | draftkings |  14.6  | +16.8% | 0.3%          | lost     |             -1   |                          -0.31 |
| 2026-11-23  | Scottie Barnes PRA over 54.5 (55+)          | MIL @ TOR | draftkings |  17.6  | +16.7% | 0.2%          | lost     |             -1   |                          -0.25 |
| 2026-11-23  | Shai Gilgeous-Alexander PR over 59.5 (60+)  | OKC @ IND | draftkings |  26    | +15.5% | 0.1%          | lost     |             -1   |                          -0.15 |
| 2026-11-23  | Andrew Nembhard AST over 13.5 (14+)         | OKC @ IND | draftkings |  23    | +14.7% | 0.2%          | lost     |             -1   |                          -0.17 |
| 2026-11-23  | Quenton Jackson AST over 5.5 (6+)           | OKC @ IND | draftkings |  10.1  | +14.1% | 0.4%          | lost     |             -1   |                          -0.39 |
| 2026-11-23  | Scottie Barnes PA over 49.5 (50+)           | MIL @ TOR | draftkings |  27    | +13.8% | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-23  | Scottie Barnes AST over 9.5 (10+)           | MIL @ TOR | draftkings |  11.2  | +13.4% | 0.3%          | lost     |             -1   |                          -0.33 |
| 2026-11-23  | Keldon Johnson AST over 5.5 (6+)            | SAS @ SAC | draftkings |  21    | +12.9% | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-23  | Scottie Barnes PA over 39.5 (40+)           | MIL @ TOR | draftkings |   8.1  | +12.7% | 0.4%          | lost     |             -1   |                          -0.45 |
| 2026-11-23  | Ryan Kalkbrenner REB over 9.5 (10+)         | MEM @ CHA | draftkings |  18.8  | +12.5% | 0.2%          | lost     |             -1   |                          -0.18 |
| 2026-11-23  | Andrew Nembhard AST over 11.5 (12+)         | OKC @ IND | draftkings |  10    | +12.0% | 0.3%          | lost     |             -1   |                          -0.33 |
| 2026-11-23  | Andrew Nembhard PRA over 39.5 (40+)         | OKC @ IND | draftkings |  14    | +12.0% | 0.2%          | lost     |             -1   |                          -0.23 |
| 2026-11-23  | Scottie Barnes AST over 11.5 (12+)          | MIL @ TOR | draftkings |  27    | +11.8% | 0.1%          | lost     |             -1   |                          -0.11 |
| 2026-11-23  | Scottie Barnes PRA over 49.5 (50+)          | MIL @ TOR | draftkings |   9.1  | +11.8% | 0.4%          | lost     |             -1   |                          -0.36 |
| 2026-11-23  | Luka Doncic PA over 59.5 (60+)              | UTA @ LAL | draftkings |   9.9  | +11.7% | 0.3%          | lost     |             -1   |                          -0.33 |
| 2026-11-23  | Scottie Barnes PR over 44.5 (45+)           | MIL @ TOR | draftkings |  11.8  | +10.8% | 0.2%          | lost     |             -1   |                          -0.25 |
| 2026-11-23  | Derik Queen REB over 11.5 (12+)             | PHX @ NOP | draftkings |  16    | +10.7% | 0.2%          | lost     |             -1   |                          -0.18 |
| 2026-11-23  | Jakob Poeltl AST over 3.5 (4+)              | MIL @ TOR | draftkings |   7.1  | +10.5% | 0.4%          | lost     |             -1   |                          -0.43 |
| 2026-11-23  | Scottie Barnes PR over 49.5 (50+)           | MIL @ TOR | draftkings |  21    | +10.4% | 0.1%          | lost     |             -1   |                          -0.13 |
| 2026-11-23  | Kevin Durant PA over 39.5 (40+)             | LAC @ HOU | draftkings |  17    | +10.1% | 0.2%          | lost     |             -1   |                          -0.16 |
| 2026-11-23  | Jaylen Brown PRA over 49.5 (50+)            | POR @ PHI | draftkings |  19.2  | +10.0% | 0.1%          | lost     |             -1   |                          -0.14 |
| 2026-11-23  | Jaylen Brown PA over 39.5 (40+)             | POR @ PHI | draftkings |  13.6  | +10.0% | 0.2%          | lost     |             -1   |                          -0.2  |
| 2026-11-22  | Jalen Brunson PA over 54.5 (55+)            | IND @ NYK | draftkings |  23    | +19.1% | 0.2%          | lost     |             -1   |                          -0.22 |
| 2026-11-22  | Jalen Brunson PRA over 54.5 (55+)           | IND @ NYK | draftkings |  16    | +17.5% | 0.3%          | lost     |             -1   |                          -0.29 |
| 2026-11-22  | Jalen Brunson PRA over 59.5 (60+)           | IND @ NYK | draftkings |  26    | +17.3% | 0.2%          | lost     |             -1   |                          -0.17 |
| 2026-11-22  | Jalen Brunson PTS over 49.5 (50+)           | IND @ NYK | draftkings |  31    | +16.6% | 0.1%          | lost     |             -1   |                          -0.14 |
| 2026-11-22  | Jalen Brunson PTS over 44.5 (45+)           | IND @ NYK | draftkings |  17.8  | +16.6% | 0.2%          | lost     |             -1   |                          -0.25 |
| 2026-11-22  | Jalen Brunson PR over 49.5 (50+)            | IND @ NYK | draftkings |  19.2  | +15.2% | 0.2%          | lost     |             -1   |                          -0.21 |
| 2026-11-22  | Jalen Brunson PA over 49.5 (50+)            | IND @ NYK | draftkings |  12.2  | +14.2% | 0.3%          | lost     |             -1   |                          -0.32 |
| 2026-11-22  | Karl-Anthony Towns AST over 7.5 (8+)        | IND @ NYK | draftkings |  22    | +13.4% | 0.2%          | lost     |             -1   |                          -0.16 |

</details>

## Check news first (EV ≥ 5%, odds ≤ 4)

TODAY.md's "check news first" table: bets that clear the bar but where the model and market disagree by more than 15 points, so something may be missing. Final pre-tip list at the price shown then. Kept apart from best bets; if this stays unprofitable, the flag is doing its job.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |     20 |    14 |            12.75 |           63.7 |                  29.8 |                                 22.28 |                   74.7 |
| Last 30 days |     92 |    47 |            14.4  |           15.7 |                 135   |                                 26.61 |                   19.7 |
| Whole season |    116 |    58 |            13.08 |           11.3 |                 170.1 |                                 25.18 |                   14.8 |

<details><summary>Every check-news bet (116)</summary>

| date (US)   | bet                                   | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:--------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-27  | Jusuf Nurkic PR over 19.5 (20+)       | DEN @ UTA | draftkings  |   3.67 | +10.3% | 1.0%          | lost     |            -1    |                          -0.97 |
| 2026-11-27  | Jusuf Nurkic PA over 14.5 (15+)       | DEN @ UTA | draftkings  |   3.38 | +9.5%  | 1.0%          | won      |             2.38 |                           2.38 |
| 2026-11-27  | Jusuf Nurkic PA over 10.5 (11+)       | DEN @ UTA | draftkings  |   1.94 | +6.8%  | 1.8%          | won      |             0.94 |                           1.7  |
| 2026-11-27  | Deni Avdija AST over 7.5 (8+)         | GSW @ POR | draftkings  |   3.04 | +5.1%  | 0.6%          | lost     |            -1    |                          -0.62 |
| 2026-11-25  | Sion James REB over 1.5 (2+)          | CHI @ CHA | draftkings  |   2.42 | +16.6% | 2.0%          | won      |             1.42 |                           2.84 |
| 2026-11-25  | Devin Vassell REB over 1.5 (2+)       | SAS @ POR | draftkings  |   2.26 | +13.9% | 2.0%          | won      |             1.26 |                           2.52 |
| 2026-11-25  | Julian Champagnie REB over 1.5 (2+)   | SAS @ POR | draftkings  |   1.97 | +9.9%  | 2.0%          | won      |             0.97 |                           1.94 |
| 2026-11-24  | Daniss Jenkins PA over 24.5 (25+)     | DET @ ORL | draftkings  |   3.57 | +5.9%  | 0.6%          | won      |             2.57 |                           1.49 |
| 2026-11-23  | Meleek Thomas STL over 0.5 (1+)       | CLE @ CHI | draftkings  |   2.31 | +22.1% | 2.0%          | won      |             1.31 |                           2.62 |
| 2026-11-23  | Julian Champagnie REB over 1.5 (2+)   | SAS @ SAC | draftkings  |   2.19 | +13.2% | 2.0%          | won      |             1.19 |                           2.38 |
| 2026-11-23  | Carter Bryant PTS over 7.5 (8+)       | SAS @ SAC | pointsbetau |   2.05 | +9.1%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-23  | Quentin Grimes PTS under 16.5         | UTA @ LAL | draftkings  |   1.99 | +6.4%  | 1.6%          | won      |             0.99 |                           1.59 |
| 2026-11-23  | Tyler Herro PTS under 20.5            | MIL @ TOR | tab         |   1.95 | +6.3%  | 1.7%          | lost     |            -1    |                          -1.65 |
| 2026-11-23  | Mo Bamba PTS under 9.5                | UTA @ LAL | tab         |   2    | +6.2%  | 1.5%          | won      |             1    |                           1.54 |
| 2026-11-22  | Andrew Wiggins PRA over 19.5 (20+)    | OKC @ MIA | draftkings  |   3.67 | +8.8%  | 0.8%          | lost     |            -1    |                          -0.83 |
| 2026-11-22  | Hugo Gonzalez REB over 1.5 (2+)       | BOS @ GSW | draftkings  |   2.5  | +7.3%  | 1.2%          | won      |             1.5  |                           1.83 |
| 2026-11-22  | Bennett Stirtz PTS over 11.5 (12+)    | OKC @ MIA | pointsbetau |   2    | +6.2%  | 1.5%          | won      |             1    |                           1.54 |
| 2026-11-21  | Hugo Gonzalez REB over 1.5 (2+)       | BOS @ SAC | draftkings  |   2.32 | +10.9% | 2.0%          | won      |             1.32 |                           2.64 |
| 2026-11-21  | Precious Achiuwa PTS over 4.5 (5+)    | BOS @ SAC | tab         |   1.9  | +7.6%  | 2.0%          | won      |             0.9  |                           1.8  |
| 2026-11-21  | Saddiq Bey AST over 3.5 (4+)          | NOP @ SAS | draftkings  |   3.78 | +5.3%  | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-11-20  | Mo Bamba REB over 3.5 (4+)            | PHX @ UTA | draftkings  |   2.97 | +20.2% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-19  | Jrue Holiday PA over 24.5 (25+)       | POR @ MIL | draftkings  |   3.87 | +8.1%  | 0.7%          | won      |             2.87 |                           2.01 |
| 2026-11-19  | Scoot Henderson AST over 3.5 (4+)     | POR @ MIL | draftkings  |   3.85 | +5.7%  | 0.5%          | lost     |            -1    |                          -0.5  |
| 2026-11-19  | Kasparas Jakucionis AST over 3.5 (4+) | POR @ MIL | draftkings  |   3.49 | +5.4%  | 0.5%          | lost     |            -1    |                          -0.54 |
| 2026-11-18  | Neemias Queta BLK over 1.5 (2+)       | BOS @ DEN | draftkings  |   2.72 | +24.2% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-18  | Paul Reed PTS over 11.5 (12+)         | DET @ NOP | tab         |   2    | +8.6%  | 2.0%          | won      |             1    |                           2    |
| 2026-11-18  | Jamison Battle PRA over 19.5 (20+)    | WAS @ TOR | draftkings  |   3.57 | +6.8%  | 0.7%          | won      |             2.57 |                           1.7  |
| 2026-11-18  | Jamison Battle PA over 14.5 (15+)     | WAS @ TOR | draftkings  |   3.11 | +5.8%  | 0.7%          | won      |             2.11 |                           1.43 |
| 2026-11-18  | Quentin Grimes PTS under 15.5         | UTA @ LAL | pointsbetau |   2    | +5.7%  | 1.4%          | lost     |            -1    |                          -1.41 |
| 2026-11-18  | Brayden Burries PTS under 12.5        | MIL @ MIA | draftkings  |   1.98 | +5.4%  | 1.4%          | lost     |            -1    |                          -1.37 |
| 2026-11-16  | Zach Edey REB over 9.5 (10+)          | MEM @ WAS | draftkings  |   3.62 | +8.3%  | 0.8%          | won      |             2.62 |                           2.07 |
| 2026-11-16  | Tyrese Proctor PTS over 10.5 (11+)    | CHI @ CLE | pointsbetau |   2.05 | +7.5%  | 1.8%          | won      |             1.05 |                           1.88 |
| 2026-11-16  | Luka Garza PTS under 9.5              | ORL @ BOS | pointsbetau |   1.87 | +5.1%  | 1.5%          | won      |             0.87 |                           1.26 |
| 2026-11-14  | Karlo Matkovic PTS over 9.5 (10+)     | DEN @ NOP | draftkings  |   3.98 | +7.3%  | 0.6%          | lost     |            -1    |                          -0.61 |
| 2026-11-13  | Karlo Matkovic PTS over 7.5 (8+)      | MEM @ NOP | draftkings  |   2.24 | +20.3% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-13  | Brayden Burries PTS under 11.5        | MIL @ ORL | pointsbetau |   2    | +5.8%  | 1.4%          | won      |             1    |                           1.44 |
| 2026-11-13  | Karlo Matkovic PR over 14.5 (15+)     | MEM @ NOP | draftkings  |   3    | +5.6%  | 0.7%          | lost     |            -1    |                          -0.7  |
| 2026-11-13  | Karlo Matkovic PTS over 9.5 (10+)     | MEM @ NOP | draftkings  |   3.38 | +5.5%  | 0.6%          | lost     |            -1    |                          -0.58 |
| 2026-11-11  | Jamison Battle PTS over 8.5 (9+)      | BOS @ TOR | pointsbetau |   2.1  | +5.8%  | 1.3%          | won      |             1.1  |                           1.44 |
| 2026-11-10  | Precious Achiuwa PTS over 7.5 (8+)    | ORL @ SAC | pointsbetau |   2.1  | +9.2%  | 2.0%          | won      |             1.1  |                           2.2  |
| 2026-11-02  | Khaman Maluach REB under 6.5          | PHX @ GSW | draftkings  |   2.07 | +6.0%  | 1.4%          | won      |             1.07 |                           1.49 |
| 2026-11-01  | Jarace Walker PR over 19.5 (20+)      | BKN @ IND | draftkings  |   3.42 | +9.1%  | 0.9%          | lost     |            -1    |                          -0.94 |
| 2026-11-01  | Walker Kessler PTS under 12.5         | TOR @ LAL | tab         |   1.9  | +6.1%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-01  | Brandon Williams PTS under 14.5       | LAC @ GSW | draftkings  |   1.88 | +5.0%  | 1.4%          | lost     |            -1    |                          -1.41 |
| 2026-10-31  | Tari Eason REB over 7.5 (8+)          | OKC @ HOU | draftkings  |   3.87 | +13.6% | 1.2%          | lost     |            -1    |                          -1.19 |
| 2026-10-31  | Isaiah Collier PRA over 19.5 (20+)    | POR @ UTA | draftkings  |   3.7  | +13.5% | 1.2%          | lost     |            -1    |                          -1.25 |
| 2026-10-31  | Cameron Boozer REB over 9.5 (10+)     | SAC @ MEM | draftkings  |   2.84 | +12.1% | 1.6%          | lost     |            -1    |                          -1.64 |
| 2026-10-31  | Damian Lillard PTS under 23.5         | POR @ UTA | betright    |   1.96 | +11.7% | 2.0%          | won      |             0.96 |                           1.92 |
| 2026-10-31  | Isaiah Collier PTS over 9.5 (10+)     | POR @ UTA | draftkings  |   3.09 | +9.1%  | 1.1%          | lost     |            -1    |                          -1.09 |
| 2026-10-31  | Adem Bona PR under 14.5               | PHI @ CHA | draftkings  |   1.77 | +9.1%  | 2.0%          | won      |             0.77 |                           1.54 |
| 2026-10-31  | Kevin Durant RA over 8.5 (9+)         | OKC @ HOU | draftkings  |   2    | +9.1%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Kevin Durant AST over 3.5 (4+)        | OKC @ HOU | draftkings  |   2.16 | +8.8%  | 1.9%          | won      |             1.16 |                           2.2  |
| 2026-10-31  | Adem Bona REB under 5.5               | PHI @ CHA | draftkings  |   2.14 | +8.7%  | 1.9%          | won      |             1.14 |                           2.18 |
| 2026-10-31  | AJ Green 3PM under 1.5                | CLE @ MIL | draftkings  |   2.33 | +8.7%  | 1.6%          | won      |             1.33 |                           2.17 |
| 2026-10-31  | Jerami Grant PTS over 14.5 (15+)      | SAC @ MEM | draftkings  |   3.09 | +8.4%  | 1.0%          | lost     |            -1    |                          -1    |
| 2026-10-31  | Adem Bona REB under 6.5               | PHI @ CHA | draftkings  |   1.87 | +8.4%  | 2.0%          | won      |             0.87 |                           1.74 |
| 2026-10-31  | Amen Thompson AST over 5.5 (6+)       | OKC @ HOU | draftkings  |   3.08 | +8.3%  | 1.0%          | lost     |            -1    |                          -1    |
| 2026-10-31  | Joan Beringer PR under 18.5           | MIN @ SAS | draftkings  |   1.9  | +8.2%  | 2.0%          | won      |             0.9  |                           1.8  |
| 2026-10-31  | Tari Eason PR over 19.5 (20+)         | OKC @ HOU | draftkings  |   3.03 | +7.2%  | 0.9%          | lost     |            -1    |                          -0.89 |
| 2026-10-31  | Damian Lillard PTS under 22.5         | POR @ UTA | draftkings  |   1.97 | +6.8%  | 1.7%          | won      |             0.97 |                           1.69 |
| 2026-10-31  | Scoot Henderson PTS under 14.5        | POR @ UTA | draftkings  |   1.93 | +6.4%  | 1.7%          | won      |             0.93 |                           1.6  |
| 2026-10-31  | VJ Edgecombe PTS under 15.5           | PHI @ CHA | pointsbetau |   2.05 | +5.4%  | 1.3%          | won      |             1.05 |                           1.35 |
| 2026-10-31  | Darryn Peterson PTS under 14.5        | POR @ UTA | betright    |   1.92 | +5.3%  | 1.5%          | lost     |            -1    |                          -1.45 |
| 2026-10-31  | Kevin Durant REB over 5.5 (6+)        | OKC @ HOU | draftkings  |   2.33 | +5.2%  | 1.0%          | lost     |            -1    |                          -0.98 |
| 2026-10-31  | Cameron Boozer RA over 14.5 (15+)     | SAC @ MEM | draftkings  |   2    | +5.1%  | 1.3%          | lost     |            -1    |                          -1.29 |
| 2026-10-31  | Dean Wade REB under 4.5               | PHI @ CHA | draftkings  |   2.13 | +5.0%  | 1.1%          | lost     |            -1    |                          -1.11 |
| 2026-10-30  | Quenton Jackson PR over 9.5 (10+)     | IND @ MIA | draftkings  |   2.01 | +9.6%  | 2.0%          | won      |             1.01 |                           2.02 |
| 2026-10-30  | Quenton Jackson PA over 9.5 (10+)     | IND @ MIA | draftkings  |   1.83 | +8.9%  | 2.0%          | won      |             0.83 |                           1.66 |
| 2026-10-30  | Quenton Jackson AST over 3.5 (4+)     | IND @ MIA | draftkings  |   2.29 | +8.8%  | 1.7%          | lost     |            -1    |                          -1.71 |
| 2026-10-30  | Cameron Johnson PTS under 10.5        | DEN @ PHX | unibet      |   1.97 | +8.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-30  | Khaman Maluach PR under 15.5          | DEN @ PHX | draftkings  |   1.94 | +7.7%  | 2.0%          | won      |             0.94 |                           1.88 |
| 2026-10-30  | AJ Dybantsa PTS under 15.5            | CHA @ WAS | draftkings  |   1.95 | +7.6%  | 2.0%          | lost     |            -1    |                          -1.99 |
| 2026-10-30  | Kevin Durant PRA over 39.5 (40+)      | HOU @ DAL | draftkings  |   3.14 | +7.5%  | 0.9%          | lost     |            -1    |                          -0.88 |
| 2026-10-30  | Nolan Traore PTS under 9.5            | DET @ BKN | pointsbetau |   2.05 | +7.5%  | 1.8%          | won      |             1.05 |                           1.87 |
| 2026-10-30  | Khaman Maluach REB under 7.5          | DEN @ PHX | draftkings  |   2.01 | +7.4%  | 1.8%          | won      |             1.01 |                           1.86 |
| 2026-10-30  | Cameron Johnson 3PM under 1.5         | DEN @ PHX | draftkings  |   2.1  | +7.4%  | 1.7%          | lost     |            -1    |                          -1.69 |
| 2026-10-30  | Walker Kessler PTS under 13.5         | LAL @ GSW | sportsbet   |   2.02 | +7.0%  | 1.7%          | won      |             1.02 |                           1.74 |
| 2026-10-30  | John Collins PTS under 14.5           | DET @ BKN | tab         |   1.9  | +6.8%  | 1.9%          | won      |             0.9  |                           1.71 |
| 2026-10-30  | Walker Kessler PTS under 14.5         | LAL @ GSW | neds        |   1.83 | +6.5%  | 1.9%          | won      |             0.83 |                           1.62 |
| 2026-10-30  | DeMar DeRozan AST over 3.5 (4+)       | DEN @ PHX | draftkings  |   3.1  | +6.4%  | 0.8%          | won      |             2.1  |                           1.6  |
| 2026-10-30  | Kevin Durant RA over 9.5 (10+)        | HOU @ DAL | draftkings  |   1.95 | +6.0%  | 1.6%          | lost     |            -1    |                          -1.58 |
| 2026-10-30  | Naz Reid PTS under 17.5               | CHA @ WAS | pointsbetau |   2    | +5.8%  | 1.5%          | won      |             1    |                           1.45 |
| 2026-10-30  | AJ Dybantsa PR under 20.5             | CHA @ WAS | draftkings  |   1.94 | +5.8%  | 1.5%          | lost     |            -1    |                          -1.53 |
| 2026-10-30  | Nolan Traore PTS under 10.5           | DET @ BKN | draftkings  |   1.85 | +5.7%  | 1.7%          | won      |             0.85 |                           1.42 |
| 2026-10-30  | Kevin Durant AST over 3.5 (4+)        | HOU @ DAL | draftkings  |   1.78 | +5.6%  | 1.8%          | lost     |            -1    |                          -1.79 |
| 2026-10-30  | Bilal Coulibaly PTS over 9.5 (10+)    | CHA @ WAS | draftkings  |   2.8  | +5.1%  | 0.7%          | lost     |            -1    |                          -0.71 |
| 2026-10-30  | Kevin Durant RA over 8.5 (9+)         | HOU @ DAL | draftkings  |   1.72 | +5.1%  | 1.8%          | lost     |            -1    |                          -1.78 |
| 2026-10-30  | AJ Dybantsa PRA under 23.5            | CHA @ WAS | draftkings  |   1.83 | +5.0%  | 1.5%          | lost     |            -1    |                          -1.53 |
| 2026-10-29  | Zion Williamson PTS over 24.5 (25+)   | SAC @ NOP | draftkings  |   3.63 | +10.8% | 1.0%          | lost     |            -1    |                          -1.03 |
| 2026-10-29  | Cedric Coward PTS under 13.5          | MEM @ POR | sportsbet   |   1.96 | +8.0%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-29  | Cameron Boozer PTS under 17.5         | MEM @ POR | tab         |   1.9  | +7.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-29  | Jrue Holiday PRA over 24.5 (25+)      | MEM @ POR | draftkings  |   3.38 | +7.1%  | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-10-29  | Precious Achiuwa PTS over 14.5 (15+)  | SAC @ NOP | draftkings  |   3.53 | +6.9%  | 0.7%          | won      |             2.53 |                           1.72 |
| 2026-10-29  | Jrue Holiday AST over 4.5 (5+)        | MEM @ POR | draftkings  |   2.5  | +6.6%  | 1.1%          | lost     |            -1    |                          -1.1  |
| 2026-10-29  | Jeremiah Fears PA over 16.5 (17+)     | SAC @ NOP | draftkings  |   1.95 | +5.4%  | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-29  | Jrue Holiday REB over 4.5 (5+)        | MEM @ POR | draftkings  |   2.67 | +5.4%  | 0.8%          | won      |             1.67 |                           1.34 |
| 2026-10-28  | AJ Dybantsa PA under 13.5             | WAS @ CLE | draftkings  |   1.93 | +18.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Clint Capela PR under 13.5            | HOU @ MIL | draftkings  |   1.98 | +12.0% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Clint Capela PTS under 7.5            | HOU @ MIL | draftkings  |   1.81 | +11.5% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Kevin Durant AST over 5.5 (6+)        | HOU @ MIL | draftkings  |   3.63 | +10.9% | 1.0%          | lost     |            -1    |                          -1.04 |

</details>

## Not on Sportsbet (EV ≥ 5%, odds ≤ 4)

TODAY.md's "not on Sportsbet" table: bets that meet the best-bets rules (EV ≥ 5%, odds ≤ 4, no news flag), but in a market Sportsbet doesn't list (bookie_markets.json), so only other books have them. Final pre-tip list at the price shown then.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |      2 |     1 |            -0.05 |           -2.5 |                   2.7 |                                 -0.13 |                   -4.7 |
| Last 30 days |     16 |     7 |            -1.91 |          -11.9 |                  23.4 |                                 -2.16 |                   -9.3 |
| Whole season |     17 |     7 |            -2.91 |          -17.1 |                  24   |                                 -2.8  |                  -11.7 |

<details><summary>Every not-on-Sportsbet bet (17)</summary>

| date (US)   | bet                              | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-27  | Joan Beringer PTS over 5.5 (6+)  | MEM @ MIN | tab         |   2.05 | +5.8%  | 1.4%          | lost     |            -1    |                          -1.38 |
| 2026-11-21  | Caleb Martin PTS under 6.5       | LAC @ DAL | tab         |   1.95 | +5.0%  | 1.3%          | won      |             0.95 |                           1.25 |
| 2026-11-20  | Danny Wolf PTS over 5.5 (6+)     | ORL @ BKN | tab         |   1.85 | +8.4%  | 2.0%          | won      |             0.85 |                           1.7  |
| 2026-11-20  | Marcus Smart PTS over 5.5 (6+)   | HOU @ DEN | sportsbet   |   2.05 | +5.8%  | 1.4%          | lost     |            -1    |                          -1.39 |
| 2026-11-19  | Isaiah Stewart PTS under 9.5     | GSW @ MEM | draftkings  |   1.99 | +5.9%  | 1.5%          | won      |             0.99 |                           1.47 |
| 2026-11-19  | Bones Hyland PTS under 8.5       | NYK @ MIN | tab         |   2    | +5.7%  | 1.4%          | won      |             1    |                           1.42 |
| 2026-11-18  | Jake LaRavia PTS over 7.5 (8+)   | UTA @ LAL | draftkings  |   2.79 | +9.7%  | 1.4%          | lost     |            -1    |                          -1.36 |
| 2026-11-18  | Josh Green PTS under 4.5         | UTA @ LAL | draftkings  |   1.93 | +5.3%  | 1.4%          | lost     |            -1    |                          -1.42 |
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
| Last 7 days  |     20 |    12 |             4.69 |           23.4 |                  20.7 |                                  3.13 |                   15.1 |         7.2 |             80   |                          12 |                         7.2 |                  58.3 |
| Last 30 days |    123 |    47 |           -15.42 |          -12.5 |                 106.4 |                                 -8.13 |                   -7.6 |         4.5 |             64.2 |                          57 |                         7.4 |                  61.4 |
| Whole season |    142 |    57 |            -2.38 |           -1.7 |                 113.4 |                                 -0.09 |                   -0.1 |         4   |             59.2 |                          62 |                         6.6 |                  56.5 |

<details><summary>Every bet that showed at any time (odds = first price shown) (142)</summary>

| date (US)   | bet                                       | game      | book          |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:--------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-27  | Brice Sensabaugh PTS over 11.5 (12+)      | DEN @ UTA | draftkings    |   2.38 | +8.4%  | 1.5%          | won      |             1.38 |                           2.11 |
| 2026-11-27  | Rudy Gobert PTS over 8.5 (9+)             | MEM @ MIN | pointsbetau   |   2.05 | +5.1%  | 1.2%          | won      |             1.05 |                           1.28 |
| 2026-11-27  | Zaccharie Risacher PTS under 9.5          | DAL @ PHX | draftkings    |   2.01 | +5.1%  | 1.3%          | lost     |            -1    |                          -1.26 |
| 2026-11-25  | CLE to win                                | CLE @ NYK | draftkings    |   2.45 | +14.8% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-25  | Tre Jones PTS over 11.5 (12+)             | CHI @ CHA | tab           |   2    | +6.8%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-25  | Jose Alvarado PTS over 7.5 (8+)           | CLE @ NYK | draftkings    |   2.59 | +6.4%  | 1.0%          | won      |             1.59 |                           1.61 |
| 2026-11-25  | Alperen Sengun REB over 8.5 (9+)          | PHX @ HOU | draftkings    |   2.08 | -4.3%  | 0.0%          | won      |             1.08 |                           0    |
| 2026-11-25  | PHI to win                                | MIA @ PHI | draftkings    |   2.06 | -6.1%  | 0.0%          | won      |             1.06 |                           0    |
| 2026-11-24  | DET to win                                | DET @ ORL | draftkings    |   2.19 | +22.1% | 2.0%          | won      |             1.19 |                           2.38 |
| 2026-11-24  | John Collins PTS over 10.5 (11+)          | DET @ ORL | sportsbet     |   2.05 | +6.3%  | 1.5%          | won      |             1.05 |                           1.56 |
| 2026-11-24  | Zaccharie Risacher PTS over 7.5 (8+)      | DAL @ DEN | pointsbetau   |   2    | +2.6%  | 0.7%          | won      |             1    |                           0.65 |
| 2026-11-23  | SAS to win                                | SAS @ SAC | draftkings    |   1.32 | +9.4%  | 2.0%          | won      |             0.32 |                           0.64 |
| 2026-11-23  | PHI to win                                | POR @ PHI | draftkings    |   1.87 | -0.1%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-23  | Sam Merrill PTS over 7.5 (8+)             | CLE @ CHI | tab           |   2    | -5.0%  | 0.0%          | won      |             1    |                           0    |
| 2026-11-22  | Obi Toppin PTS over 11.5 (12+)            | IND @ NYK | draftkings    |   2.29 | +5.9%  | 1.1%          | lost     |            -1    |                          -1.15 |
| 2026-11-22  | Isaiah Hartenstein PTS over 10.5 (11+)    | OKC @ MIA | pointsbetau   |   2.05 | +2.8%  | 0.7%          | lost     |            -1    |                          -0.67 |
| 2026-11-22  | Andrew Wiggins PTS over 11.5 (12+)        | OKC @ MIA | draftkings    |   2.09 | -2.7%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-22  | Dyson Daniels REB over 6.5 (7+)           | DET @ ATL | draftkings    |   2.13 | -5.8%  | 0.0%          | won      |             1.13 |                           0    |
| 2026-11-21  | Taylor Hendricks PTS over 9.5 (10+)       | MEM @ MIN | draftkings    |   2.79 | +24.3% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-21  | NYK to win                                | POR @ NYK | draftkings    |   1.84 | +18.5% | 2.0%          | won      |             0.84 |                           1.68 |
| 2026-11-20  | Malik Monk PTS over 11.5 (12+)            | SAC @ LAL | draftkings    |   2.45 | +13.0% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-20  | Jamison Battle PTS over 11.5 (12+)        | TOR @ DET | draftkings    |   2.65 | +7.9%  | 1.2%          | lost     |            -1    |                          -1.23 |
| 2026-11-20  | DEN to win                                | HOU @ DEN | draftkings    |   2.01 | +7.3%  | 1.8%          | won      |             1.01 |                           1.8  |
| 2026-11-20  | Egor Demin PTS over 11.5 (12+)            | ORL @ BKN | draftkings    |   2.52 | +6.5%  | 1.1%          | lost     |            -1    |                          -1.08 |
| 2026-11-20  | Meleek Thomas PTS over 9.5 (10+)          | IND @ CLE | tab           |   1.95 | -2.5%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-20  | BKN to win                                | ORL @ BKN | draftkings    |   3.17 | -5.0%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-20  | CHA to win                                | CHA @ ATL | draftkings    |   2.94 | -5.1%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-18  | PHI to win                                | PHI @ ORL | draftkings    |   2.46 | +11.9% | 2.0%          | won      |             1.46 |                           2.92 |
| 2026-11-18  | Javonte Green PTS over 7.5 (8+)           | DET @ NOP | tab           |   1.8  | +11.3% | 2.0%          | won      |             0.8  |                           1.6  |
| 2026-11-18  | Collin Murray-Boyles PTS over 14.5 (15+)  | WAS @ TOR | betright      |   2.05 | +8.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-18  | Kevin Huerter PTS over 14.5 (15+)         | DET @ NOP | sportsbet     |   2.05 | +5.5%  | 1.3%          | lost     |            -1    |                          -1.31 |
| 2026-11-18  | TOR to win                                | WAS @ TOR | draftkings    |   1.57 | -4.1%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-18  | Ace Bailey 3PM over 2.5 (3+)              | UTA @ LAL | draftkings    |   2.48 | -5.9%  | 0.0%          | lost     |            -1    |                          -0    |
| 2026-11-18  | IND to win                                | HOU @ IND | draftkings    |   3.93 | -6.1%  | 0.0%          | lost     |            -1    |                          -0    |
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

</details>

CLV vs Aussie close uses the Australian books' own closing prices (Sportsbet, TAB, PointsBet and others, margin removed, averaged) for the same bet, where they priced it. That's the market you bet into, so it's the more relevant test; Aussie books often only list points props, so coverage is partial.

CLV (closing-line value) compares the price taken with the final no-vig market price before tip. Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings for months.

## Best player props per game (main lines)

The "Best player props" box in each game's section of TODAY.md: every main-line prop with positive EV, no news flag and offered at Sportsbet, as listed on the last update before tip, graded at the price shown then. These include edges under 5%, so expect a thinner margin than best bets.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Last 7 days  |    138 |    62 |           -15.26 |          -11.1 |                  59.8 |                                 -1.67 |                   -2.8 |
| Last 30 days |    645 |   312 |           -24.17 |           -3.7 |                 261.3 |                                 -3.4  |                   -1.3 |
| Whole season |    664 |   318 |           -31.78 |           -4.8 |                 267.1 |                                 -2.67 |                   -1   |

<details><summary>Every graded game prop (664)</summary>

| date (US)   | bet                                        | game      | book         |   odds | EV    | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-------------------------------------------|:----------|:-------------|-------:|:------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-27  | Brice Sensabaugh PTS over 11.5 (12+)       | DEN @ UTA | draftkings   |   2.38 | +8.4% | 1.5%          | won      |             1.38 |                           2.11 |
| 2026-11-27  | Rudy Gobert PTS over 8.5 (9+)              | MEM @ MIN | pointsbetau  |   2.05 | +5.1% | 1.2%          | won      |             1.05 |                           1.28 |
| 2026-11-27  | Zaccharie Risacher PTS under 9.5           | DAL @ PHX | draftkings   |   2.01 | +5.1% | 1.3%          | lost     |            -1    |                          -1.26 |
| 2026-11-27  | Walker Kessler PTS under 11.5              | LAL @ SAS | pointsbetau  |   2.05 | +4.0% | 0.9%          | won      |             1.05 |                           1    |
| 2026-11-27  | Anfernee Simons PTS over 7.5 (8+)          | PHI @ IND | betright     |   1.7  | +3.7% | 1.3%          | won      |             0.7  |                           0.93 |
| 2026-11-27  | Gui Santos PTS under 9.5                   | GSW @ POR | tab          |   1.9  | +3.1% | 0.9%          | won      |             0.9  |                           0.77 |
| 2026-11-27  | Pelle Larsson PTS over 9.5 (10+)           | MIA @ NYK | draftkings   |   2    | +3.0% | 0.7%          | won      |             1    |                           0.74 |
| 2026-11-27  | Sidy Cissoko PTS over 8.5 (9+)             | GSW @ POR | pointsbetau  |   1.95 | +2.9% | 0.8%          | lost     |            -1    |                          -0.77 |
| 2026-11-27  | Zion Williamson PTS under 22.5             | NOP @ LAC | tab          |   1.95 | +2.9% | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-11-27  | Olivier-Maxence Prosper PTS over 9.5 (10+) | MEM @ MIN | draftkings   |   2.07 | +2.6% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-11-27  | Paul Reed PTS over 12.5 (13+)              | MIL @ DET | tab          |   2    | +2.5% | 0.6%          | won      |             1    |                           0.63 |
| 2026-11-27  | Dyson Daniels PTS over 9.5 (10+)           | ATL @ BOS | betright     |   1.98 | +2.2% | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-11-27  | Collin Sexton PTS over 7.5 (8+)            | LAL @ SAS | sportsbet    |   1.96 | +2.2% | 0.6%          | won      |             0.96 |                           0.55 |
| 2026-11-27  | Luguentz Dort PTS over 8.5 (9+)            | ATL @ BOS | betright     |   2    | +2.0% | 0.5%          | won      |             1    |                           0.5  |
| 2026-11-27  | Isaiah Joe PTS under 15.5                  | MIL @ DET | pointsbetau  |   2    | +1.9% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-11-27  | Cam Spencer PTS over 10.5 (11+)            | MEM @ MIN | pointsbetau  |   2    | +1.8% | 0.5%          | won      |             1    |                           0.46 |
| 2026-11-27  | Ayo Dosunmu PTS over 19.5 (20+)            | MEM @ MIN | pointsbetau  |   2    | +1.8% | 0.4%          | won      |             1    |                           0.44 |
| 2026-11-27  | Jakob Poeltl PTS over 9.5 (10+)            | BKN @ TOR | pointsbetau  |   1.9  | +1.6% | 0.4%          | won      |             0.9  |                           0.4  |
| 2026-11-27  | Giannis Antetokounmpo PTS under 27.5       | MIA @ NYK | draftkings   |   1.96 | +1.5% | 0.4%          | won      |             0.96 |                           0.38 |
| 2026-11-27  | Immanuel Quickley PTS under 18.5           | BKN @ TOR | pointsbetau  |   2.05 | +1.5% | 0.4%          | lost     |            -1    |                          -0.36 |
| 2026-11-27  | Quenton Jackson PTS under 8.5              | PHI @ IND | draftkings   |   1.96 | +1.4% | 0.4%          | lost     |            -1    |                          -0.36 |
| 2026-11-27  | Jose Alvarado PTS over 7.5 (8+)            | MIA @ NYK | draftkings   |   2.02 | +1.2% | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-11-27  | Kris Dunn PTS over 4.5 (5+)                | NOP @ LAC | sportsbet    |   1.8  | +1.1% | 0.3%          | lost     |            -1    |                          -0.34 |
| 2026-11-27  | Daniel Gafford PTS over 10.5 (11+)         | DAL @ PHX | pointsbetau  |   2.05 | +1.1% | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-11-27  | Stephon Castle PTS under 16.5              | LAL @ SAS | neds         |   1.91 | +1.0% | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-27  | Darius Garland PTS under 20.5              | NOP @ LAC | betright     |   1.91 | +0.9% | 0.3%          | won      |             0.91 |                           0.24 |
| 2026-11-27  | Obi Toppin PTS over 11.5 (12+)             | PHI @ IND | draftkings   |   2.06 | +0.9% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-11-27  | Ace Bailey PTS over 15.5 (16+)             | DEN @ UTA | pointsbetau  |   2.05 | +0.9% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-11-27  | Tyler Herro PTS under 20.5                 | MIL @ DET | betright     |   1.98 | +0.6% | 0.1%          | won      |             0.98 |                           0.15 |
| 2026-11-27  | Bones Hyland PTS under 12.5                | MEM @ MIN | pointsbetau  |   2    | +0.5% | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-27  | Kyle Kuzma PTS under 12.5                  | MIL @ DET | tab          |   1.95 | +0.3% | 0.1%          | won      |             0.95 |                           0.08 |
| 2026-11-27  | Charles Bassey PTS under 9.5               | GSW @ POR | betright     |   2.03 | +0.2% | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-27  | Naji Marshall PTS under 12.5               | DAL @ PHX | draftkings   |   1.96 | +0.2% | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-27  | De'Anthony Melton PTS under 11.5           | GSW @ POR | pointsbetau  |   1.9  | +0.2% | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-27  | Terrence Shannon Jr. PTS under 16.5        | MEM @ MIN | sportsbet    |   2    | +0.1% | 0.0%          | won      |             1    |                           0.02 |
| 2026-11-27  | Jalen Brunson PTS over 28.5 (29+)          | MIA @ NYK | pointsbetau  |   2    | +0.1% | 0.0%          | lost     |            -1    |                          -0.01 |
| 2026-11-25  | Tre Jones PTS over 11.5 (12+)              | CHI @ CHA | tab          |   2    | +6.8% | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-25  | Jose Alvarado PTS over 7.5 (8+)            | CLE @ NYK | draftkings   |   2.59 | +6.4% | 1.0%          | won      |             1.59 |                           1.61 |
| 2026-11-25  | Harrison Barnes PTS under 7.5              | SAS @ POR | pointsbetau  |   2.1  | +4.6% | 1.0%          | won      |             1.1  |                           1.14 |
| 2026-11-25  | Charles Bassey PTS under 10.5              | SAC @ GSW | tab          |   1.95 | +4.5% | 1.2%          | won      |             0.95 |                           1.11 |
| 2026-11-25  | Donovan Clingan PTS over 10.5 (11+)        | SAS @ POR | pointsbetau  |   2    | +3.5% | 0.9%          | lost     |            -1    |                          -0.86 |
| 2026-11-25  | Peyton Watson PTS under 11.5               | CLE @ NYK | pointsbetau  |   2    | +2.9% | 0.7%          | won      |             1    |                           0.73 |
| 2026-11-25  | Keaton Wagler PTS under 8.5                | LAC @ MEM | tab          |   2    | +2.4% | 0.6%          | lost     |            -1    |                          -0.59 |
| 2026-11-25  | Anfernee Simons PTS over 9.5 (10+)         | MIA @ PHI | sportsbet    |   2.08 | +2.2% | 0.5%          | lost     |            -1    |                          -0.51 |
| 2026-11-25  | Victor Wembanyama PTS under 30.5           | SAS @ POR | draftkings   |   1.94 | +1.9% | 0.5%          | lost     |            -1    |                          -0.5  |
| 2026-11-25  | Julian Champagnie PTS under 11.5           | SAS @ POR | sportsbet    |   1.96 | +1.7% | 0.4%          | won      |             0.96 |                           0.42 |
| 2026-11-25  | Josh Giddey PTS over 12.5 (13+)            | CHI @ CHA | betright     |   1.91 | +1.5% | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-11-25  | LaMelo Ball PTS under 18.5                 | MIN @ OKC | draftkings   |   1.96 | +1.2% | 0.3%          | lost     |            -1    |                          -0.31 |
| 2026-11-25  | Jarrett Allen PTS under 12.5               | CLE @ NYK | pointsbetau  |   2    | +1.2% | 0.3%          | won      |             1    |                           0.3  |
| 2026-11-25  | Julius Randle PTS under 21.5               | BKN @ MIL | draftkings   |   1.97 | +1.2% | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-11-25  | Klay Thompson PTS under 12.5               | MIA @ PHI | tab          |   1.9  | +1.2% | 0.3%          | won      |             0.9  |                           0.29 |
| 2026-11-25  | Mikal Bridges PTS under 12.5               | CLE @ NYK | tab          |   1.9  | +1.0% | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-11-25  | Myles Turner PTS over 9.5 (10+)            | BKN @ MIL | pointsbetau  |   2.05 | +0.7% | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-11-25  | Miles Bridges PTS under 13.5               | PHX @ HOU | tab          |   1.95 | +0.7% | 0.2%          | won      |             0.95 |                           0.16 |
| 2026-11-25  | Damian Lillard PTS under 20.5              | SAS @ POR | tab          |   1.95 | +0.5% | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-25  | Fred VanVleet PTS over 12.5 (13+)          | PHX @ HOU | pointsbetau  |   2    | +0.5% | 0.1%          | won      |             1    |                           0.12 |
| 2026-11-25  | Bam Adebayo PTS over 18.5 (19+)            | MIA @ PHI | sportsbet    |   2.02 | +0.4% | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-11-25  | Jabari Walker PTS under 6.5                | MIA @ PHI | tab          |   2    | +0.3% | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-11-25  | Giannis Antetokounmpo PTS over 28.5 (29+)  | MIA @ PHI | pointsbetau  |   2    | +0.2% | 0.1%          | won      |             1    |                           0.05 |
| 2026-11-24  | John Collins PTS over 10.5 (11+)           | DET @ ORL | sportsbet    |   2.05 | +6.3% | 1.5%          | won      |             1.05 |                           1.56 |
| 2026-11-24  | Zaccharie Risacher PTS over 7.5 (8+)       | DAL @ DEN | pointsbetau  |   2    | +2.6% | 0.7%          | won      |             1    |                           0.65 |
| 2026-11-24  | Bilal Coulibaly PTS over 6.5 (7+)          | BOS @ WAS | pointsbetau  |   2    | +1.5% | 0.4%          | won      |             1    |                           0.36 |
| 2026-11-24  | Daniss Jenkins PTS over 15.5 (16+)         | DET @ ORL | sportsbet    |   2    | +0.8% | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-11-24  | Tristan da Silva PTS under 10.5            | DET @ ORL | tab          |   1.95 | +0.3% | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-24  | AJ Dybantsa PTS under 15.5                 | BOS @ WAS | draftkings   |   1.94 | +0.1% | 0.0%          | lost     |            -1    |                          -0.04 |
| 2026-11-23  | Sion James PTS over 7.5 (8+)               | MEM @ CHA | draftkings   |   2.14 | +4.3% | 0.9%          | lost     |            -1    |                          -0.95 |
| 2026-11-23  | Ryan Kalkbrenner PTS over 4.5 (5+)         | MEM @ CHA | draftkings   |   2.01 | +4.3% | 1.1%          | lost     |            -1    |                          -1.06 |
| 2026-11-23  | Quenton Jackson PTS over 9.5 (10+)         | OKC @ IND | draftkings   |   2.04 | +3.4% | 0.8%          | lost     |            -1    |                          -0.83 |
| 2026-11-23  | Ryan Rollins PTS under 11.5                | MIL @ TOR | tab          |   2    | +3.3% | 0.8%          | won      |             1    |                           0.82 |
| 2026-11-23  | Collin Gillespie PTS under 10.5            | PHX @ NOP | draftkings   |   2    | +3.1% | 0.8%          | lost     |            -1    |                          -0.79 |
| 2026-11-23  | Cam Spencer PTS over 9.5 (10+)             | MEM @ CHA | pointsbetau  |   1.9  | +3.0% | 0.8%          | won      |             0.9  |                           0.74 |
| 2026-11-23  | Brook Lopez PTS over 11.5 (12+)            | LAC @ HOU | draftkings   |   2.03 | +2.9% | 0.7%          | lost     |            -1    |                          -0.7  |
| 2026-11-23  | Brice Sensabaugh PTS over 11.5 (12+)       | UTA @ LAL | pointsbetau  |   2.05 | +2.7% | 0.6%          | lost     |            -1    |                          -0.64 |
| 2026-11-23  | Andrew Nembhard PTS over 14.5 (15+)        | OKC @ IND | betright     |   1.96 | +2.7% | 0.7%          | won      |             0.96 |                           0.67 |
| 2026-11-23  | Walker Kessler PTS under 13.5              | UTA @ LAL | betright     |   1.98 | +2.4% | 0.6%          | won      |             0.98 |                           0.6  |
| 2026-11-23  | Scoot Henderson PTS over 9.5 (10+)         | POR @ PHI | pointsbetau  |   1.95 | +2.4% | 0.6%          | won      |             0.95 |                           0.59 |
| 2026-11-23  | Zion Williamson PTS under 21.5             | PHX @ NOP | draftkings   |   1.95 | +2.3% | 0.6%          | lost     |            -1    |                          -0.61 |
| 2026-11-23  | Darryn Peterson PTS under 17.5             | UTA @ LAL | tab          |   1.95 | +2.2% | 0.6%          | won      |             0.95 |                           0.55 |
| 2026-11-23  | Brice Sensabaugh PTS over 10.5 (11+)       | UTA @ LAL | ladbrokes_au |   1.87 | +2.1% | 0.6%          | lost     |            -1    |                          -0.61 |
| 2026-11-23  | Jrue Holiday PTS over 13.5 (14+)           | POR @ PHI | pointsbetau  |   2.05 | +1.9% | 0.5%          | won      |             1.05 |                           0.48 |
| 2026-11-23  | Egor Demin PTS over 9.5 (10+)              | BKN @ MIN | draftkings   |   2.02 | +1.9% | 0.5%          | won      |             1.02 |                           0.47 |
| 2026-11-23  | Anfernee Simons PTS over 9.5 (10+)         | POR @ PHI | sportsbet    |   2.02 | +1.8% | 0.4%          | lost     |            -1    |                          -0.45 |
| 2026-11-23  | Ziaire Williams PTS over 7.5 (8+)          | UTA @ LAL | draftkings   |   1.93 | +1.7% | 0.4%          | won      |             0.93 |                           0.42 |
| 2026-11-23  | Kenrich Williams PTS under 9.5             | OKC @ IND | betright     |   2.05 | +1.5% | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-11-23  | Darius Acuff Jr. PTS under 23.5            | SAS @ SAC | tab          |   1.95 | +1.4% | 0.4%          | won      |             0.95 |                           0.34 |
| 2026-11-23  | Derik Queen PTS over 10.5 (11+)            | PHX @ NOP | draftkings   |   2.03 | +1.1% | 0.3%          | won      |             1.03 |                           0.27 |
| 2026-11-23  | Ty Jerome PTS under 22.5                   | MEM @ CHA | pointsbetau  |   2    | +1.0% | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-11-23  | Quenton Jackson PTS under 9.5              | OKC @ IND | pointsbetau  |   2.05 | +1.0% | 0.2%          | won      |             1.05 |                           0.24 |
| 2026-11-23  | Jaylen Wells PTS over 9.5 (10+)            | MEM @ CHA | pointsbetau  |   1.95 | +0.9% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-11-23  | Jalen Smith PTS over 12.5 (13+)            | CLE @ CHI | tab          |   1.85 | +0.9% | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-23  | Harrison Barnes PTS over 9.5 (10+)         | SAS @ SAC | tab          |   2    | +0.9% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-11-23  | Day'Ron Sharpe PTS over 8.5 (9+)           | BKN @ MIN | tab          |   1.95 | +0.7% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-23  | Jonathan Kuminga PTS under 14.5            | BKN @ MIN | tab          |   1.95 | +0.7% | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-11-23  | Derik Queen PTS over 9.5 (10+)             | PHX @ NOP | betright     |   1.83 | +0.6% | 0.2%          | won      |             0.83 |                           0.15 |
| 2026-11-23  | Amen Thompson PA over 19.5 (20+)           | LAC @ HOU | draftkings   |   1.98 | +0.6% | 0.1%          | won      |             0.98 |                           0.15 |
| 2026-11-23  | Stephon Castle PTS under 22.5              | SAS @ SAC | draftkings   |   1.96 | +0.6% | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-11-23  | Immanuel Quickley PTS over 18.5 (19+)      | MIL @ TOR | draftkings   |   1.98 | +0.5% | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-11-23  | Tre Jones PTS over 9.5 (10+)               | CLE @ CHI | unibet       |   1.94 | +0.3% | 0.1%          | won      |             0.94 |                           0.07 |
| 2026-11-23  | Jalen Smith PTS over 13.5 (14+)            | CLE @ CHI | pointsbetau  |   2    | +0.2% | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-11-23  | Sandro Mamukelashvili PTS over 9.5 (10+)   | UTA @ LAL | draftkings   |   2.1  | +0.2% | 0.1%          | lost     |            -1    |                          -0.05 |

</details>

## Day by day (last 30)

Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising count means something in the inputs is going wrong.

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean | sanity flags        |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|:--------------------|
| 2026-11-27 |      11 |       199 | 4.37 / 5.01                      | 4.05 / 4.38                     |          1.27 | 0 (none)            |
| 2026-11-25 |       9 |       161 | 3.87 / 4.64                      | 4.42 / 4.55                     |          0.41 | 0 (none)            |
| 2026-11-24 |       3 |        57 | 4.01 / 4.26                      | 4.89 / 5.01                     |          0.43 | 0 (none)            |
| 2026-11-23 |      10 |       180 | 4.32 / 5.21                      | 4.61 / 4.83                     |          0.15 | 0 (none)            |
| 2026-11-22 |       7 |       121 | 5.08 / 6.04                      | 5.49 / 5.60                     |          1.01 | 0 (none)            |
| 2026-11-21 |       6 |       106 | 5.17 / 6.05                      | 5.33 / 5.28                     |          1.65 | 0 (none)            |
| 2026-11-20 |       9 |       153 | 3.80 / 4.60                      | 5.18 / 5.25                     |          0.32 | 0 (none)            |
| 2026-11-19 |       4 |        73 | 4.60 / 5.51                      | 4.05 / 4.61                     |          0.26 | 0 (none)            |
| 2026-11-18 |      12 |       210 | 5.29 / 5.80                      | 4.77 / 5.19                     |          0.88 | 0 (none)            |
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
