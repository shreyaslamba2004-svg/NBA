# Model health

Rebuilt 2026-11-02 by the nightly grading run. Back to [TODAY.md](TODAY.md).

## Verdict: **SAME**

Last 7 days 0.9% better than baseline, 30 days 0.9%: steady.

How to read this: the model is judged against a simple rule anyone could use, each player's average over his last 10 games. "% better" is how much smaller the model's average miss is. Watch the trend, not single days: one game day is mostly noise.

## Projection accuracy (players the model had at 90%+ to play)

| window                      |   game days |   players |   minutes miss |   minutes % better than last-10 |   minutes lean (+ = too high) |   points miss |   points % better than last-10 |   points lean (+ = too high) |
|:----------------------------|------------:|----------:|---------------:|--------------------------------:|------------------------------:|--------------:|-------------------------------:|-----------------------------:|
| Last 7 days                 |           5 |       576 |           4.74 |                            16.8 |                           1.6 |          5.38 |                            0.9 |                            1 |
| Last 30 days                |           5 |       576 |           4.74 |                            16.8 |                           1.6 |          5.38 |                            0.9 |                            1 |
| Season                      |           5 |       576 |           4.74 |                            16.8 |                           1.6 |          5.38 |                            0.9 |                            1 |
| Backtest (held-out 2025-26) |             |           |                |                            15.4 |                               |               |                            5.4 |                              |

Live should sit near the backtest line. Well below it for weeks means the model is doing worse on new games than it did in testing (overfitting or something broke).

## Best bets (EV ≥ 5%, odds ≤ 4)

**Main record: the final list.** The bets still in TODAY.md's best-bets table on the last update before each game's tip (after lineups and injury news), graded at the price shown then.

Each table shows two ways of counting: units at a flat 1-unit stake on every bet (so results compare cleanly), and profit at the sheet's suggested stake, the quarter-Kelly % of bankroll capped at 2% that TODAY.md shows on every bet. ROI (sheet stakes) is that profit divided by the total staked. Rows are the last 7 days, last 30 days and whole season; a longer period only gets its own row once it holds more bets than the shorter one.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Since 28 Oct |     23 |     8 |            -2.28 |           -9.9 |                  26.5 |                                 -4.66 |                  -17.6 |

<details><summary>Every final-list bet (23)</summary>

| date (US)   | bet                                       | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
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
| Since 28 Oct |    125 |     6 |           -27.04 |          -21.6 |                    47 |                                 -2.42 |                   -5.1 |

<details><summary>Every long shot (125)</summary>

| date (US)   | bet                                         | game      | book       |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:--------------------------------------------|:----------|:-----------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-01  | Pascal Siakam PTS over 44.5 (45+)           | BKN @ IND | draftkings |  29    | +26.1% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-11-01  | Noah Clowney REB over 7.5 (8+)              | BKN @ IND | draftkings |  11.8  | +25.3% | 0.6%          | lost     |            -1    |                          -0.59 |
| 2026-11-01  | Pascal Siakam PA over 44.5 (45+)            | BKN @ IND | draftkings |  15.2  | +25.2% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-11-01  | Pascal Siakam PA over 49.5 (50+)            | BKN @ IND | draftkings |  26    | +24.5% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-11-01  | Pascal Siakam PRA over 54.5 (55+)           | BKN @ IND | draftkings |  16.8  | +22.8% | 0.4%          | lost     |            -1    |                          -0.36 |
| 2026-11-01  | Pascal Siakam PTS over 39.5 (40+)           | BKN @ IND | draftkings |  14.8  | +21.9% | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-11-01  | Julius Randle PTS over 34.5 (35+)           | BKN @ IND | draftkings |  17.2  | +21.6% | 0.3%          | lost     |            -1    |                          -0.33 |
| 2026-11-01  | Jayson Tatum PTS over 44.5 (45+)            | BOS @ ORL | draftkings |  22    | +20.0% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-11-01  | Noah Clowney REB over 9.5 (10+)             | BKN @ IND | draftkings |  28    | +17.8% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-11-01  | Jayson Tatum PTS over 39.5 (40+)            | BOS @ ORL | draftkings |  11.2  | +16.0% | 0.4%          | lost     |            -1    |                          -0.39 |
| 2026-11-01  | Pascal Siakam PRA over 49.5 (50+)           | BKN @ IND | draftkings |   8.8  | +15.6% | 0.5%          | lost     |            -1    |                          -0.5  |
| 2026-11-01  | Jarace Walker PR over 24.5 (25+)            | BKN @ IND | draftkings |   7.9  | +15.2% | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-11-01  | Jarace Walker PR over 29.5 (30+)            | BKN @ IND | draftkings |  18.4  | +14.8% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-11-01  | Gui Santos PRA over 24.5 (25+)              | LAC @ GSW | draftkings |  10    | +14.4% | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-11-01  | Jayson Tatum PR over 54.5 (55+)             | BOS @ ORL | draftkings |  18.2  | +14.1% | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-11-01  | Scottie Barnes AST over 9.5 (10+)           | TOR @ LAL | draftkings |   9.5  | +14.1% | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-11-01  | Pascal Siakam PA over 39.5 (40+)            | BKN @ IND | draftkings |   7.1  | +12.9% | 0.5%          | lost     |            -1    |                          -0.53 |
| 2026-11-01  | Scottie Barnes AST over 11.5 (12+)          | TOR @ LAL | draftkings |  23    | +12.6% | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-11-01  | Scottie Barnes PA over 44.5 (45+)           | TOR @ LAL | draftkings |  17.2  | +12.4% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-01  | Julius Randle PTS over 29.5 (30+)           | BKN @ IND | draftkings |   7.2  | +11.8% | 0.5%          | lost     |            -1    |                          -0.48 |
| 2026-11-01  | Jayson Tatum PR over 49.5 (50+)             | BOS @ ORL | draftkings |   9.9  | +11.7% | 0.3%          | lost     |            -1    |                          -0.33 |
| 2026-11-01  | Julius Randle PTS over 39.5 (40+)           | BKN @ IND | draftkings |  28    | +10.2% | 0.1%          | lost     |            -1    |                          -0.09 |
| 2026-11-01  | Pascal Siakam PTS over 34.5 (35+)           | BKN @ IND | draftkings |   6.61 | +9.6%  | 0.4%          | lost     |            -1    |                          -0.43 |
| 2026-11-01  | Jayson Tatum REB over 13.5 (14+)            | BOS @ ORL | draftkings |  13    | +9.2%  | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-01  | Pascal Siakam AST over 7.5 (8+)             | BKN @ IND | draftkings |  12.2  | +8.8%  | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-10-31  | Kevin Durant AST over 7.5 (8+)              | OKC @ HOU | draftkings |  21    | +57.8% | 0.7%          | lost     |            -1    |                          -0.72 |
| 2026-10-31  | Cameron Boozer REB over 13.5 (14+)          | SAC @ MEM | draftkings |  10.6  | +28.9% | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-10-31  | Jaylen Brown PTS over 39.5 (40+)            | PHI @ CHA | draftkings |  21    | +28.1% | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-10-31  | Tari Eason REB over 11.5 (12+)              | OKC @ HOU | draftkings |  21    | +28.0% | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-10-31  | Cameron Boozer REB over 15.5 (16+)          | SAC @ MEM | draftkings |  20    | +26.3% | 0.4%          | lost     |            -1    |                          -0.35 |
| 2026-10-31  | Tari Eason REB over 9.5 (10+)               | OKC @ HOU | draftkings |   9.2  | +25.9% | 0.8%          | lost     |            -1    |                          -0.79 |
| 2026-10-31  | Isaiah Collier PRA over 29.5 (30+)          | POR @ UTA | draftkings |  18.6  | +22.1% | 0.3%          | lost     |            -1    |                          -0.31 |
| 2026-10-31  | Kevin Durant REB over 9.5 (10+)             | OKC @ HOU | draftkings |  14.6  | +21.6% | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-10-31  | Isaiah Collier PRA over 24.5 (25+)          | POR @ UTA | draftkings |   8.3  | +21.2% | 0.7%          | lost     |            -1    |                          -0.72 |
| 2026-10-31  | Amen Thompson AST over 7.5 (8+)             | OKC @ HOU | draftkings |   8.6  | +20.5% | 0.7%          | lost     |            -1    |                          -0.68 |
| 2026-10-31  | Shai Gilgeous-Alexander PA over 54.5 (55+)  | OKC @ HOU | draftkings |  21    | +20.3% | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-10-31  | Amen Thompson AST over 9.5 (10+)            | OKC @ HOU | draftkings |  23    | +20.0% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-10-31  | Kevin Durant PTS over 39.5 (40+)            | OKC @ HOU | draftkings |  19.8  | +19.5% | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-10-31  | Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings |  28    | +19.3% | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-10-31  | Isaiah Collier AST over 9.5 (10+)           | POR @ UTA | draftkings |  11.8  | +18.4% | 0.4%          | lost     |            -1    |                          -0.43 |
| 2026-10-31  | Jaylen Brown PTS over 34.5 (35+)            | PHI @ CHA | draftkings |   9.7  | +18.2% | 0.5%          | lost     |            -1    |                          -0.52 |
| 2026-10-31  | Jaylen Brown PRA over 54.5 (55+)            | PHI @ CHA | draftkings |  20.6  | +17.3% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-10-31  | Jerami Grant PTS over 24.5 (25+)            | SAC @ MEM | draftkings |  19    | +17.3% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-10-31  | Zion Williamson PRA over 49.5 (50+)         | ATL @ NOP | draftkings |  24    | +17.1% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-10-31  | Zion Williamson PRA over 44.5 (45+)         | ATL @ NOP | draftkings |  13    | +17.1% | 0.4%          | lost     |            -1    |                          -0.36 |
| 2026-10-31  | Jaylen Brown PRA over 49.5 (50+)            | PHI @ CHA | draftkings |  11.2  | +16.5% | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-10-31  | Ace Bailey BLK over 2.5 (3+)                | POR @ UTA | draftkings |  12.2  | +16.4% | 0.4%          | won      |            11.2  |                           4.14 |
| 2026-10-31  | Amen Thompson PRA over 44.5 (45+)           | OKC @ HOU | draftkings |  19.2  | +16.4% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-10-31  | Amen Thompson PTS over 29.5 (30+)           | OKC @ HOU | draftkings |  20.2  | +15.8% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-31  | Isaiah Collier PTS over 14.5 (15+)          | POR @ UTA | draftkings |   9.4  | +15.8% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-10-30  | Quenton Jackson PA over 24.5 (25+)          | IND @ MIA | draftkings |  26    | +47.6% | 0.5%          | won      |            25    |                          12    |
| 2026-10-30  | Quenton Jackson PR over 19.5 (20+)          | IND @ MIA | draftkings |  13.8  | +42.4% | 0.8%          | won      |            12.8  |                          10.62 |
| 2026-10-30  | Quenton Jackson AST over 7.5 (8+)           | IND @ MIA | draftkings |  17.6  | +41.6% | 0.6%          | lost     |            -1    |                          -0.63 |
| 2026-10-30  | Quenton Jackson PRA over 29.5 (30+)         | IND @ MIA | draftkings |  27    | +40.5% | 0.4%          | lost     |            -1    |                          -0.39 |
| 2026-10-30  | Kevin Durant PRA over 54.5 (55+)            | HOU @ DAL | draftkings |  21    | +35.5% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-10-30  | Quenton Jackson PTS over 19.5 (20+)         | IND @ MIA | draftkings |  30    | +35.1% | 0.3%          | won      |            29    |                           8.7  |
| 2026-10-30  | Kevin Durant PA over 49.5 (50+)             | HOU @ DAL | draftkings |  27    | +32.9% | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-10-30  | Kevin Durant AST over 9.5 (10+)             | HOU @ DAL | draftkings |  26    | +28.2% | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-10-30  | Kevin Durant PRA over 49.5 (50+)            | HOU @ DAL | draftkings |  11.2  | +27.7% | 0.7%          | lost     |            -1    |                          -0.68 |
| 2026-10-30  | Pascal Siakam PA over 49.5 (50+)            | IND @ MIA | draftkings |  24    | +24.9% | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-10-30  | Pascal Siakam PTS over 44.5 (45+)           | IND @ MIA | draftkings |  27    | +24.4% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-10-30  | Kevin Durant PR over 49.5 (50+)             | HOU @ DAL | draftkings |  20.8  | +24.0% | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-10-30  | Pascal Siakam PR over 49.5 (50+)            | IND @ MIA | draftkings |  16    | +23.5% | 0.4%          | lost     |            -1    |                          -0.39 |
| 2026-10-30  | Kevin Durant PTS over 44.5 (45+)            | HOU @ DAL | draftkings |  28    | +23.3% | 0.2%          | lost     |            -1    |                          -0.22 |
| 2026-10-30  | Pascal Siakam PA over 44.5 (45+)            | IND @ MIA | draftkings |  13.2  | +22.9% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-10-30  | Pascal Siakam PR over 54.5 (55+)            | IND @ MIA | draftkings |  27    | +22.1% | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-30  | Kevin Durant PTS over 39.5 (40+)            | HOU @ DAL | draftkings |  14    | +19.0% | 0.4%          | lost     |            -1    |                          -0.37 |
| 2026-10-30  | Pascal Siakam PTS over 39.5 (40+)           | IND @ MIA | draftkings |  13.2  | +18.7% | 0.4%          | lost     |            -1    |                          -0.38 |
| 2026-10-30  | Pascal Siakam AST over 7.5 (8+)             | IND @ MIA | draftkings |  11.2  | +16.6% | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-10-30  | DeMar DeRozan AST over 5.5 (6+)             | DEN @ PHX | draftkings |  10.8  | +16.5% | 0.4%          | lost     |            -1    |                          -0.42 |
| 2026-10-30  | Kevin Durant PR over 44.5 (45+)             | HOU @ DAL | draftkings |  10.3  | +16.2% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-10-30  | DeMar DeRozan PRA over 29.5 (30+)           | DEN @ PHX | draftkings |  13.2  | +14.1% | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-10-30  | Pascal Siakam PR over 44.5 (45+)            | IND @ MIA | draftkings |   7.9  | +13.5% | 0.5%          | lost     |            -1    |                          -0.49 |
| 2026-10-30  | Bam Adebayo PR over 44.5 (45+)              | IND @ MIA | draftkings |  18.2  | +12.8% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-10-30  | Yaxel Lendeborg PRA over 44.5 (45+)         | LAL @ GSW | draftkings |  12.8  | +12.7% | 0.3%          | lost     |            -1    |                          -0.27 |
| 2026-10-29  | Zion Williamson PTS over 34.5 (35+)         | SAC @ NOP | draftkings |  19.6  | +44.5% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-29  | Jrue Holiday AST over 8.5 (9+)              | MEM @ POR | draftkings |  20.8  | +32.1% | 0.4%          | lost     |            -1    |                          -0.41 |
| 2026-10-29  | Jrue Holiday AST over 7.5 (8+)              | MEM @ POR | draftkings |  12.2  | +29.3% | 0.7%          | lost     |            -1    |                          -0.65 |
| 2026-10-29  | Ja Morant AST over 11.5 (12+)               | MEM @ POR | draftkings |  20.8  | +25.2% | 0.3%          | lost     |            -1    |                          -0.32 |
| 2026-10-29  | Ja Morant AST over 10.5 (11+)               | MEM @ POR | draftkings |  13.4  | +23.2% | 0.5%          | lost     |            -1    |                          -0.47 |
| 2026-10-29  | Jrue Holiday AST over 9.5 (10+)             | MEM @ POR | draftkings |  30    | +22.1% | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-10-29  | Damian Lillard AST over 8.5 (9+)            | MEM @ POR | draftkings |  21    | +19.0% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-10-29  | Jrue Holiday REB over 7.5 (8+)              | MEM @ POR | draftkings |  12.8  | +18.1% | 0.4%          | lost     |            -1    |                          -0.38 |
| 2026-10-29  | Ja Morant AST over 12.5 (13+)               | MEM @ POR | draftkings |  29    | +17.6% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-29  | Ja Morant AST over 9.5 (10+)                | MEM @ POR | draftkings |   8.2  | +17.0% | 0.6%          | lost     |            -1    |                          -0.59 |
| 2026-10-29  | Jrue Holiday PRA over 39.5 (40+)            | MEM @ POR | draftkings |  27    | +16.4% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-29  | Jrue Holiday REB over 6.5 (7+)              | MEM @ POR | draftkings |   7.5  | +16.3% | 0.6%          | lost     |            -1    |                          -0.63 |
| 2026-10-29  | Damian Lillard AST over 7.5 (8+)            | MEM @ POR | draftkings |  11.8  | +16.2% | 0.4%          | lost     |            -1    |                          -0.38 |
| 2026-10-29  | Jrue Holiday PRA over 34.5 (35+)            | MEM @ POR | draftkings |  16.4  | +16.0% | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-10-29  | Jrue Holiday REB over 8.5 (9+)              | MEM @ POR | draftkings |  21    | +16.0% | 0.2%          | lost     |            -1    |                          -0.2  |
| 2026-10-29  | Jrue Holiday PRA over 29.5 (30+)            | MEM @ POR | draftkings |   7.4  | +14.4% | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-10-29  | Precious Achiuwa PTS over 19.5 (20+)        | SAC @ NOP | draftkings |   9.6  | +13.6% | 0.4%          | won      |             8.6  |                           3.35 |
| 2026-10-29  | Derik Queen PTS over 24.5 (25+)             | SAC @ NOP | draftkings |  22    | +13.2% | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-29  | Derik Queen REB over 13.5 (14+)             | SAC @ NOP | draftkings |  14.6  | +12.5% | 0.2%          | lost     |            -1    |                          -0.23 |
| 2026-10-29  | Derik Queen REB over 12.5 (13+)             | SAC @ NOP | draftkings |   9.7  | +11.9% | 0.3%          | lost     |            -1    |                          -0.34 |
| 2026-10-29  | Damian Lillard AST over 6.5 (7+)            | MEM @ POR | draftkings |   6.69 | +11.7% | 0.5%          | lost     |            -1    |                          -0.51 |
| 2026-10-29  | Precious Achiuwa PTS over 17.5 (18+)        | SAC @ NOP | draftkings |   6.36 | +11.4% | 0.5%          | won      |             5.36 |                           2.84 |
| 2026-10-29  | Ja Morant AST over 8.5 (9+)                 | MEM @ POR | draftkings |   5.04 | +10.5% | 0.7%          | lost     |            -1    |                          -0.65 |
| 2026-10-29  | Trey Murphy III PRA over 44.5 (45+)         | SAC @ NOP | draftkings |  19.2  | +10.2% | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-10-29  | Derik Queen PTS over 19.5 (20+)             | SAC @ NOP | draftkings |   7.9  | +9.9%  | 0.4%          | lost     |            -1    |                          -0.36 |

</details>

## Check news first (EV ≥ 5%, odds ≤ 4)

TODAY.md's "check news first" table: bets that clear the bar but where the model and market disagree by more than 15 points, so something may be missing. Final pre-tip list at the price shown then. Kept apart from best bets; if this stays unprofitable, the flag is doing its job.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Since 28 Oct |     75 |    33 |            -7.03 |           -9.4 |                 114.3 |                                  -4.3 |                   -3.8 |

<details><summary>Every check-news bet (75)</summary>

| date (US)   | bet                                  | game      | book        |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-------------------------------------|:----------|:------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-01  | Jarace Walker PR over 19.5 (20+)     | BKN @ IND | draftkings  |   3.42 | +9.1%  | 0.9%          | lost     |            -1    |                          -0.94 |
| 2026-11-01  | Walker Kessler PTS under 12.5        | TOR @ LAL | tab         |   1.9  | +6.1%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-01  | Brandon Williams PTS under 14.5      | LAC @ GSW | draftkings  |   1.88 | +5.0%  | 1.4%          | lost     |            -1    |                          -1.41 |
| 2026-10-31  | Tari Eason REB over 7.5 (8+)         | OKC @ HOU | draftkings  |   3.87 | +13.6% | 1.2%          | lost     |            -1    |                          -1.19 |
| 2026-10-31  | Isaiah Collier PRA over 19.5 (20+)   | POR @ UTA | draftkings  |   3.7  | +13.5% | 1.2%          | lost     |            -1    |                          -1.25 |
| 2026-10-31  | Cameron Boozer REB over 9.5 (10+)    | SAC @ MEM | draftkings  |   2.84 | +12.1% | 1.6%          | lost     |            -1    |                          -1.64 |
| 2026-10-31  | Damian Lillard PTS under 23.5        | POR @ UTA | betright    |   1.96 | +11.7% | 2.0%          | won      |             0.96 |                           1.92 |
| 2026-10-31  | Isaiah Collier PTS over 9.5 (10+)    | POR @ UTA | draftkings  |   3.09 | +9.1%  | 1.1%          | lost     |            -1    |                          -1.09 |
| 2026-10-31  | Adem Bona PR under 14.5              | PHI @ CHA | draftkings  |   1.77 | +9.1%  | 2.0%          | won      |             0.77 |                           1.54 |
| 2026-10-31  | Kevin Durant RA over 8.5 (9+)        | OKC @ HOU | draftkings  |   2    | +9.1%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Kevin Durant AST over 3.5 (4+)       | OKC @ HOU | draftkings  |   2.16 | +8.8%  | 1.9%          | won      |             1.16 |                           2.2  |
| 2026-10-31  | Adem Bona REB under 5.5              | PHI @ CHA | draftkings  |   2.14 | +8.7%  | 1.9%          | won      |             1.14 |                           2.18 |
| 2026-10-31  | AJ Green 3PM under 1.5               | CLE @ MIL | draftkings  |   2.33 | +8.7%  | 1.6%          | won      |             1.33 |                           2.17 |
| 2026-10-31  | Jerami Grant PTS over 14.5 (15+)     | SAC @ MEM | draftkings  |   3.09 | +8.4%  | 1.0%          | lost     |            -1    |                          -1    |
| 2026-10-31  | Adem Bona REB under 6.5              | PHI @ CHA | draftkings  |   1.87 | +8.4%  | 2.0%          | won      |             0.87 |                           1.74 |
| 2026-10-31  | Amen Thompson AST over 5.5 (6+)      | OKC @ HOU | draftkings  |   3.08 | +8.3%  | 1.0%          | lost     |            -1    |                          -1    |
| 2026-10-31  | Joan Beringer PR under 18.5          | MIN @ SAS | draftkings  |   1.9  | +8.2%  | 2.0%          | won      |             0.9  |                           1.8  |
| 2026-10-31  | Tari Eason PR over 19.5 (20+)        | OKC @ HOU | draftkings  |   3.03 | +7.2%  | 0.9%          | lost     |            -1    |                          -0.89 |
| 2026-10-31  | Damian Lillard PTS under 22.5        | POR @ UTA | draftkings  |   1.97 | +6.8%  | 1.7%          | won      |             0.97 |                           1.69 |
| 2026-10-31  | Scoot Henderson PTS under 14.5       | POR @ UTA | draftkings  |   1.93 | +6.4%  | 1.7%          | won      |             0.93 |                           1.6  |
| 2026-10-31  | VJ Edgecombe PTS under 15.5          | PHI @ CHA | pointsbetau |   2.05 | +5.4%  | 1.3%          | won      |             1.05 |                           1.35 |
| 2026-10-31  | Darryn Peterson PTS under 14.5       | POR @ UTA | betright    |   1.92 | +5.3%  | 1.5%          | lost     |            -1    |                          -1.45 |
| 2026-10-31  | Kevin Durant REB over 5.5 (6+)       | OKC @ HOU | draftkings  |   2.33 | +5.2%  | 1.0%          | lost     |            -1    |                          -0.98 |
| 2026-10-31  | Cameron Boozer RA over 14.5 (15+)    | SAC @ MEM | draftkings  |   2    | +5.1%  | 1.3%          | lost     |            -1    |                          -1.29 |
| 2026-10-31  | Dean Wade REB under 4.5              | PHI @ CHA | draftkings  |   2.13 | +5.0%  | 1.1%          | lost     |            -1    |                          -1.11 |
| 2026-10-30  | Quenton Jackson PR over 9.5 (10+)    | IND @ MIA | draftkings  |   2.01 | +9.6%  | 2.0%          | won      |             1.01 |                           2.02 |
| 2026-10-30  | Quenton Jackson PA over 9.5 (10+)    | IND @ MIA | draftkings  |   1.83 | +8.9%  | 2.0%          | won      |             0.83 |                           1.66 |
| 2026-10-30  | Quenton Jackson AST over 3.5 (4+)    | IND @ MIA | draftkings  |   2.29 | +8.8%  | 1.7%          | lost     |            -1    |                          -1.71 |
| 2026-10-30  | Cameron Johnson PTS under 10.5       | DEN @ PHX | unibet      |   1.97 | +8.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-30  | Khaman Maluach PR under 15.5         | DEN @ PHX | draftkings  |   1.94 | +7.7%  | 2.0%          | won      |             0.94 |                           1.88 |
| 2026-10-30  | AJ Dybantsa PTS under 15.5           | CHA @ WAS | draftkings  |   1.95 | +7.6%  | 2.0%          | lost     |            -1    |                          -1.99 |
| 2026-10-30  | Kevin Durant PRA over 39.5 (40+)     | HOU @ DAL | draftkings  |   3.14 | +7.5%  | 0.9%          | lost     |            -1    |                          -0.88 |
| 2026-10-30  | Nolan Traore PTS under 9.5           | DET @ BKN | pointsbetau |   2.05 | +7.5%  | 1.8%          | won      |             1.05 |                           1.87 |
| 2026-10-30  | Khaman Maluach REB under 7.5         | DEN @ PHX | draftkings  |   2.01 | +7.4%  | 1.8%          | won      |             1.01 |                           1.86 |
| 2026-10-30  | Cameron Johnson 3PM under 1.5        | DEN @ PHX | draftkings  |   2.1  | +7.4%  | 1.7%          | lost     |            -1    |                          -1.69 |
| 2026-10-30  | Walker Kessler PTS under 13.5        | LAL @ GSW | sportsbet   |   2.02 | +7.0%  | 1.7%          | won      |             1.02 |                           1.74 |
| 2026-10-30  | John Collins PTS under 14.5          | DET @ BKN | tab         |   1.9  | +6.8%  | 1.9%          | won      |             0.9  |                           1.71 |
| 2026-10-30  | Walker Kessler PTS under 14.5        | LAL @ GSW | neds        |   1.83 | +6.5%  | 1.9%          | won      |             0.83 |                           1.62 |
| 2026-10-30  | DeMar DeRozan AST over 3.5 (4+)      | DEN @ PHX | draftkings  |   3.1  | +6.4%  | 0.8%          | won      |             2.1  |                           1.6  |
| 2026-10-30  | Kevin Durant RA over 9.5 (10+)       | HOU @ DAL | draftkings  |   1.95 | +6.0%  | 1.6%          | lost     |            -1    |                          -1.58 |
| 2026-10-30  | Naz Reid PTS under 17.5              | CHA @ WAS | pointsbetau |   2    | +5.8%  | 1.5%          | won      |             1    |                           1.45 |
| 2026-10-30  | AJ Dybantsa PR under 20.5            | CHA @ WAS | draftkings  |   1.94 | +5.8%  | 1.5%          | lost     |            -1    |                          -1.53 |
| 2026-10-30  | Nolan Traore PTS under 10.5          | DET @ BKN | draftkings  |   1.85 | +5.7%  | 1.7%          | won      |             0.85 |                           1.42 |
| 2026-10-30  | Kevin Durant AST over 3.5 (4+)       | HOU @ DAL | draftkings  |   1.78 | +5.6%  | 1.8%          | lost     |            -1    |                          -1.79 |
| 2026-10-30  | Bilal Coulibaly PTS over 9.5 (10+)   | CHA @ WAS | draftkings  |   2.8  | +5.1%  | 0.7%          | lost     |            -1    |                          -0.71 |
| 2026-10-30  | Kevin Durant RA over 8.5 (9+)        | HOU @ DAL | draftkings  |   1.72 | +5.1%  | 1.8%          | lost     |            -1    |                          -1.78 |
| 2026-10-30  | AJ Dybantsa PRA under 23.5           | CHA @ WAS | draftkings  |   1.83 | +5.0%  | 1.5%          | lost     |            -1    |                          -1.53 |
| 2026-10-29  | Zion Williamson PTS over 24.5 (25+)  | SAC @ NOP | draftkings  |   3.63 | +10.8% | 1.0%          | lost     |            -1    |                          -1.03 |
| 2026-10-29  | Cedric Coward PTS under 13.5         | MEM @ POR | sportsbet   |   1.96 | +8.0%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-29  | Cameron Boozer PTS under 17.5        | MEM @ POR | tab         |   1.9  | +7.7%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-29  | Jrue Holiday PRA over 24.5 (25+)     | MEM @ POR | draftkings  |   3.38 | +7.1%  | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-10-29  | Precious Achiuwa PTS over 14.5 (15+) | SAC @ NOP | draftkings  |   3.53 | +6.9%  | 0.7%          | won      |             2.53 |                           1.72 |
| 2026-10-29  | Jrue Holiday AST over 4.5 (5+)       | MEM @ POR | draftkings  |   2.5  | +6.6%  | 1.1%          | lost     |            -1    |                          -1.1  |
| 2026-10-29  | Jeremiah Fears PA over 16.5 (17+)    | SAC @ NOP | draftkings  |   1.95 | +5.4%  | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-29  | Jrue Holiday REB over 4.5 (5+)       | MEM @ POR | draftkings  |   2.67 | +5.4%  | 0.8%          | won      |             1.67 |                           1.34 |
| 2026-10-28  | AJ Dybantsa PA under 13.5            | WAS @ CLE | draftkings  |   1.93 | +18.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Clint Capela PR under 13.5           | HOU @ MIL | draftkings  |   1.98 | +12.0% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Clint Capela PTS under 7.5           | HOU @ MIL | draftkings  |   1.81 | +11.5% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Kevin Durant AST over 5.5 (6+)       | HOU @ MIL | draftkings  |   3.63 | +10.9% | 1.0%          | lost     |            -1    |                          -1.04 |
| 2026-10-28  | Saddiq Bey PR over 19.5 (20+)        | DEN @ NOP | draftkings  |   3.49 | +10.1% | 1.0%          | lost     |            -1    |                          -1.01 |
| 2026-10-28  | Klay Thompson 3PM under 2.5          | MIA @ ATL | draftkings  |   1.87 | +9.3%  | 2.0%          | won      |             0.87 |                           1.74 |
| 2026-10-28  | LAC +4.5                             | LAL @ LAC | tab         |   1.9  | +8.4%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Saddiq Bey PTS over 14.5 (15+)       | DEN @ NOP | draftkings  |   3.01 | +7.9%  | 1.0%          | lost     |            -1    |                          -0.99 |
| 2026-10-28  | Trae Young PA under 30.5             | WAS @ CLE | draftkings  |   1.94 | +6.8%  | 1.8%          | won      |             0.94 |                           1.68 |
| 2026-10-28  | Trae Young PTS under 20.5            | WAS @ CLE | draftkings  |   1.94 | +6.7%  | 1.8%          | won      |             0.94 |                           1.67 |
| 2026-10-28  | Clint Capela REB under 7.5           | HOU @ MIL | draftkings  |   1.72 | +6.6%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-28  | Trae Young PRA under 32.5            | WAS @ CLE | draftkings  |   1.93 | +6.3%  | 1.7%          | won      |             0.93 |                           1.56 |
| 2026-10-28  | Kobe Sanders 3PM under 1.5           | LAL @ LAC | draftkings  |   2.17 | +6.1%  | 1.3%          | won      |             1.17 |                           1.53 |
| 2026-10-28  | Daniss Jenkins REB over 3.5 (4+)     | CHA @ DET | draftkings  |   3.03 | +5.9%  | 0.7%          | lost     |            -1    |                          -0.73 |
| 2026-10-28  | Tim Hardaway Jr. 3PM under 1.5       | MIA @ ATL | draftkings  |   2.04 | +5.8%  | 1.4%          | lost     |            -1    |                          -1.39 |
| 2026-10-28  | Trae Young AST under 10.5            | WAS @ CLE | draftkings  |   1.72 | +5.6%  | 1.9%          | won      |             0.72 |                           1.4  |
| 2026-10-28  | Paul Reed REB under 9.5              | CHA @ DET | draftkings  |   1.71 | +5.4%  | 1.9%          | won      |             0.71 |                           1.33 |
| 2026-10-28  | Kevin Durant AST over 4.5 (5+)       | HOU @ MIL | draftkings  |   2.31 | +5.2%  | 1.0%          | lost     |            -1    |                          -0.99 |
| 2026-10-28  | Trae Young PR under 22.5             | WAS @ CLE | draftkings  |   1.93 | +5.1%  | 1.4%          | won      |             0.93 |                           1.26 |
| 2026-10-28  | Myles Turner 3PM under 1.5           | HOU @ MIL | draftkings  |   1.99 | +5.0%  | 1.3%          | won      |             0.99 |                           1.26 |

</details>

## Not on Sportsbet (EV ≥ 5%, odds ≤ 4)

TODAY.md's "not on Sportsbet" table: bets that meet the best-bets rules (EV ≥ 5%, odds ≤ 4, no news flag), but in a market Sportsbet doesn't list (bookie_markets.json), so only other books have them. Final pre-tip list at the price shown then.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|
| Since 29 Oct |      5 |     1 |            -2.95 |            -59 |                   5.9 |                                 -3.01 |                  -51.2 |

<details><summary>Every not-on-Sportsbet bet (5)</summary>

| date (US)   | bet                              | game      | book        |   odds | EV    | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------|:----------|:------------|-------:|:------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-01  | Keon Ellis PTS over 6.5 (7+)     | BKN @ IND | pointsbetau |   2.05 | +7.6% | 1.8%          | lost     |            -1    |                          -1.82 |
| 2026-10-31  | Jrue Holiday AST over 6.5 (7+)   | POR @ UTA | draftkings  |   3.61 | +6.2% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-31  | Julian Champagnie PTS under 10.5 | MIN @ SAS | tab         |   2    | +5.7% | 1.4%          | lost     |            -1    |                          -1.42 |
| 2026-10-30  | Leonard Miller PTS under 8.5     | CHI @ BOS | pointsbetau |   2.05 | +5.9% | 1.4%          | won      |             1.05 |                           1.47 |
| 2026-10-29  | Derik Queen PR over 24.5 (25+)   | SAC @ NOP | draftkings  |   3.58 | +6.6% | 0.6%          | lost     |            -1    |                          -0.64 |

</details>

## Best bets: any time in the day (secondary)

**Any time in the day.** Every bet that showed in the table at any point, graded at the first price it showed at. Bets that dropped off before tip (news, price moves) count here.

| period       |   bets |   won |   profit (units) |   ROI % (flat) |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   ROI % (sheet stakes) |   avg CLV % |   beat closing % |   bets with an Aussie close |   avg CLV vs Aussie close % |   beat Aussie close % |
|:-------------|-------:|------:|-----------------:|---------------:|----------------------:|--------------------------------------:|-----------------------:|------------:|-----------------:|----------------------------:|----------------------------:|----------------------:|
| Since 28 Oct |     61 |    19 |            -4.09 |           -6.7 |                  43.4 |                                -10.06 |                  -23.2 |         0.5 |             39.3 |                          23 |                           1 |                  30.4 |

<details><summary>Every bet that showed at any time (odds = first price shown) (61)</summary>

| date (US)   | bet                                       | game      | book          |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:------------------------------------------|:----------|:--------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
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
| Since 28 Oct |    213 |    88 |           -40.73 |          -19.1 |                  80.8 |                                -15.51 |                  -19.2 |

<details><summary>Every graded game prop (213)</summary>

| date (US)   | bet                                    | game      | book         |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------------|:----------|:-------------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-11-01  | Gui Santos PTS over 9.5 (10+)          | LAC @ GSW | draftkings   |   2.4  | +21.8% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-11-01  | Nolan Traore PTS under 12.5            | BKN @ IND | draftkings   |   1.99 | +7.0%  | 1.8%          | lost     |            -1    |                          -1.75 |
| 2026-11-01  | Rui Hachimura PTS under 15.5           | LAC @ GSW | draftkings   |   1.97 | +6.6%  | 1.7%          | lost     |            -1    |                          -1.7  |
| 2026-11-01  | Jamal Shead PTS over 6.5 (7+)          | TOR @ LAL | pointsbetau  |   2.05 | +5.8%  | 1.4%          | won      |             1.05 |                           1.45 |
| 2026-11-01  | Aaron Nesmith PTS over 12.5 (13+)      | BKN @ IND | pointsbetau  |   2.05 | +5.5%  | 1.3%          | lost     |            -1    |                          -1.32 |
| 2026-11-01  | Neemias Queta PTS under 9.5            | BOS @ ORL | tab          |   1.95 | +4.1%  | 1.1%          | won      |             0.95 |                           1.04 |
| 2026-11-01  | Pascal Siakam PTS over 23.5 (24+)      | BKN @ IND | pointsbetau  |   1.95 | +2.9%  | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-11-01  | Darius Garland PTS under 22.5          | LAC @ GSW | betright     |   2    | +1.5%  | 0.4%          | won      |             1    |                           0.38 |
| 2026-11-01  | Derrick Jones Jr. PTS under 10.5       | LAC @ GSW | draftkings   |   2    | +1.5%  | 0.4%          | won      |             1    |                           0.38 |
| 2026-11-01  | Noah Clowney PTS over 7.5 (8+)         | BKN @ IND | draftkings   |   1.93 | +1.4%  | 0.4%          | won      |             0.93 |                           0.34 |
| 2026-11-01  | Wendell Carter Jr. PTS over 11.5 (12+) | BOS @ ORL | unibet       |   2    | +1.2%  | 0.3%          | lost     |            -1    |                          -0.31 |
| 2026-11-01  | Georges Niang PTS over 8.5 (9+)        | LAC @ GSW | ladbrokes_au |   2.02 | +1.1%  | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-01  | De'Anthony Melton PTS under 12.5       | LAC @ GSW | draftkings   |   1.93 | +1.1%  | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-11-01  | Payton Pritchard PTS over 14.5 (15+)   | BOS @ ORL | pointsbetau  |   1.95 | +1.0%  | 0.3%          | lost     |            -1    |                          -0.26 |
| 2026-11-01  | Darius Garland PTS under 23.5          | LAC @ GSW | draftkings   |   1.87 | +0.9%  | 0.3%          | won      |             0.87 |                           0.23 |
| 2026-11-01  | Luka Doncic PTS under 33.5             | TOR @ LAL | pointsbetau  |   1.87 | +0.9%  | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-11-01  | Isaiah Jackson PTS under 8.5           | LAC @ GSW | pointsbetau  |   2.05 | +0.8%  | 0.2%          | won      |             1.05 |                           0.19 |
| 2026-11-01  | Jarace Walker PTS over 10.5 (11+)      | BKN @ IND | unibet       |   1.88 | +0.7%  | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-11-01  | Brandin Podziemski PTS over 16.5 (17+) | LAC @ GSW | betright     |   1.96 | +0.5%  | 0.1%          | won      |             0.96 |                           0.13 |
| 2026-11-01  | Derrick White PTS under 14.5           | BOS @ ORL | tab          |   1.9  | +0.5%  | 0.1%          | won      |             0.9  |                           0.13 |
| 2026-11-01  | Brandon Williams PTS under 13.5        | LAC @ GSW | betright     |   1.95 | +0.4%  | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-11-01  | Jase Richardson PTS under 8.5          | BOS @ ORL | tab          |   1.95 | +0.4%  | 0.1%          | won      |             0.95 |                           0.1  |
| 2026-11-01  | Darius Garland PR under 25.5           | LAC @ GSW | draftkings   |   1.95 | +0.4%  | 0.1%          | won      |             0.95 |                           0.09 |
| 2026-11-01  | Walker Kessler PTS under 11.5          | TOR @ LAL | unibet       |   2    | +0.3%  | 0.1%          | lost     |            -1    |                          -0.08 |
| 2026-11-01  | Walker Kessler PR under 23.5           | TOR @ LAL | draftkings   |   1.81 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-11-01  | Andrew Nembhard PTS under 18.5         | BKN @ IND | tab          |   1.95 | +0.1%  | 0.0%          | lost     |            -1    |                          -0.03 |
| 2026-11-01  | Darius Garland PR under 26.5           | LAC @ GSW | draftkings   |   1.82 | +0.1%  | 0.0%          | won      |             0.82 |                           0.02 |
| 2026-11-01  | Jarace Walker AST over 2.5 (3+)        | BKN @ IND | draftkings   |   1.98 | +0.0%  | 0.0%          | won      |             0.98 |                           0.01 |
| 2026-10-31  | Zach Edey PTS over 8.5 (9+)            | SAC @ MEM | pointsbetau  |   2.05 | +11.1% | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Donovan Clingan PTS over 11.5 (12+)    | POR @ UTA | draftkings   |   2.26 | +8.2%  | 1.6%          | lost     |            -1    |                          -1.63 |
| 2026-10-31  | Jaylen Wells PTS over 11.5 (12+)       | SAC @ MEM | unibet       |   1.66 | +6.2%  | 2.0%          | lost     |            -1    |                          -2    |
| 2026-10-31  | Trey Murphy III AST over 3.5 (4+)      | ATL @ NOP | draftkings   |   2.22 | +6.1%  | 1.3%          | won      |             1.22 |                           1.54 |
| 2026-10-31  | Kel'el Ware PTS under 9.5              | CLE @ MIL | pointsbetau  |   2    | +4.9%  | 1.2%          | lost     |            -1    |                          -1.22 |
| 2026-10-31  | Joan Beringer PTS under 9.5            | MIN @ SAS | draftkings   |   2.03 | +4.2%  | 1.0%          | lost     |            -1    |                          -1.01 |
| 2026-10-31  | Jaime Jaquez Jr. PTS under 15.5        | CLE @ MIL | pointsbetau  |   2    | +4.1%  | 1.0%          | won      |             1    |                           1.02 |
| 2026-10-31  | Saddiq Bey PTS over 12.5 (13+)         | ATL @ NOP | pointsbetau  |   1.9  | +3.8%  | 1.1%          | won      |             0.9  |                           0.95 |
| 2026-10-31  | Jrue Holiday PTS over 14.5 (15+)       | POR @ UTA | draftkings   |   2.1  | +3.8%  | 0.9%          | lost     |            -1    |                          -0.85 |
| 2026-10-31  | Ace Bailey PTS under 15.5              | POR @ UTA | pointsbetau  |   1.83 | +3.6%  | 1.1%          | won      |             0.83 |                           0.9  |
| 2026-10-31  | Jaylen Wells PTS over 13.5 (14+)       | SAC @ MEM | sportsbet    |   1.96 | +3.1%  | 0.8%          | lost     |            -1    |                          -0.81 |
| 2026-10-31  | Tari Eason PTS over 10.5 (11+)         | OKC @ HOU | pointsbetau  |   2    | +2.9%  | 0.7%          | lost     |            -1    |                          -0.73 |
| 2026-10-31  | Lauri Markkanen PTS under 21.5         | POR @ UTA | tab          |   1.95 | +2.9%  | 0.8%          | won      |             0.95 |                           0.71 |
| 2026-10-31  | Brandon Miller PTS under 26.5          | PHI @ CHA | betright     |   1.85 | +2.6%  | 0.8%          | won      |             0.85 |                           0.66 |
| 2026-10-31  | Victor Wembanyama PTS under 24.5       | MIN @ SAS | pointsbetau  |   2    | +2.6%  | 0.6%          | lost     |            -1    |                          -0.64 |
| 2026-10-31  | Naz Reid PTS under 17.5                | PHI @ CHA | betright     |   1.96 | +2.6%  | 0.7%          | won      |             0.96 |                           0.64 |
| 2026-10-31  | Myles Turner PTS under 10.5            | CLE @ MIL | tab          |   1.87 | +2.6%  | 0.7%          | won      |             0.87 |                           0.64 |
| 2026-10-31  | Myles Turner PTS under 9.5             | CLE @ MIL | pointsbetau  |   2.1  | +2.6%  | 0.6%          | lost     |            -1    |                          -0.58 |
| 2026-10-31  | Zach LaVine PTS under 21.5             | SAC @ MEM | betright     |   1.98 | +2.1%  | 0.5%          | won      |             0.98 |                           0.51 |
| 2026-10-31  | Jared McCain PTS over 14.5 (15+)       | OKC @ HOU | pointsbetau  |   2    | +2.1%  | 0.5%          | lost     |            -1    |                          -0.51 |
| 2026-10-31  | Aaron Wiggins PTS under 12.5           | ATL @ NOP | tab          |   1.9  | +2.0%  | 0.5%          | won      |             0.9  |                           0.49 |
| 2026-10-31  | Jaylen Brown PTS over 22.5 (23+)       | PHI @ CHA | draftkings   |   1.89 | +1.9%  | 0.5%          | lost     |            -1    |                          -0.53 |
| 2026-10-31  | Evan Mobley PTS under 17.5             | CLE @ MIL | pointsbetau  |   2    | +1.6%  | 0.4%          | lost     |            -1    |                          -0.4  |
| 2026-10-31  | De'Aaron Fox PTS over 14.5 (15+)       | MIN @ SAS | draftkings   |   1.97 | +1.6%  | 0.4%          | won      |             0.97 |                           0.39 |
| 2026-10-31  | Cam Spencer 3PM under 1.5              | SAC @ MEM | draftkings   |   2.43 | +1.4%  | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-10-31  | Brandon Miller PTS under 25.5          | PHI @ CHA | sportsbet    |   1.96 | +1.4%  | 0.4%          | won      |             0.96 |                           0.36 |
| 2026-10-31  | CJ McCollum PTS over 16.5 (17+)        | ATL @ NOP | pointsbetau  |   2.05 | +1.2%  | 0.3%          | lost     |            -1    |                          -0.3  |
| 2026-10-31  | Saddiq Bey RA over 6.5 (7+)            | ATL @ NOP | draftkings   |   2.12 | +1.2%  | 0.3%          | won      |             1.12 |                           0.31 |
| 2026-10-31  | Myles Turner RA under 6.5              | CLE @ MIL | draftkings   |   2.05 | +1.2%  | 0.3%          | lost     |            -1    |                          -0.28 |
| 2026-10-31  | Jaylen Brown PTS over 23.5 (24+)       | PHI @ CHA | pointsbetau  |   2    | +1.2%  | 0.3%          | lost     |            -1    |                          -0.29 |
| 2026-10-31  | Sam Merrill PTS under 9.5              | CLE @ MIL | tab          |   1.95 | +1.1%  | 0.3%          | won      |             0.95 |                           0.27 |
| 2026-10-31  | Devin Vassell PTS under 12.5           | MIN @ SAS | tab          |   1.95 | +0.9%  | 0.2%          | won      |             0.95 |                           0.24 |
| 2026-10-31  | Kyle Kuzma PTS under 11.5              | CLE @ MIL | unibet       |   2    | +0.8%  | 0.2%          | lost     |            -1    |                          -0.21 |
| 2026-10-31  | Jrue Holiday RA over 9.5 (10+)         | POR @ UTA | draftkings   |   2.08 | +0.8%  | 0.2%          | lost     |            -1    |                          -0.18 |
| 2026-10-31  | Derik Queen PTS over 11.5 (12+)        | ATL @ NOP | sportsbet    |   2.05 | +0.8%  | 0.2%          | lost     |            -1    |                          -0.19 |
| 2026-10-31  | Jabari Smith Jr. PTS over 14.5 (15+)   | OKC @ HOU | draftkings   |   1.88 | +0.8%  | 0.2%          | won      |             0.88 |                           0.19 |
| 2026-10-31  | Trey Murphy III RA over 8.5 (9+)       | ATL @ NOP | draftkings   |   2.03 | +0.7%  | 0.2%          | won      |             1.03 |                           0.18 |
| 2026-10-31  | Bones Hyland PTS over 8.5 (9+)         | MIN @ SAS | pointsbetau  |   2.05 | +0.6%  | 0.1%          | lost     |            -1    |                          -0.15 |
| 2026-10-31  | Donovan Clingan PTS over 10.5 (11+)    | POR @ UTA | draftkings   |   1.94 | +0.6%  | 0.2%          | lost     |            -1    |                          -0.16 |
| 2026-10-31  | Zach Edey PRA over 18.5 (19+)          | SAC @ MEM | draftkings   |   1.9  | +0.6%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-10-31  | Amen Thompson PRA over 27.5 (28+)      | OKC @ HOU | draftkings   |   1.85 | +0.6%  | 0.2%          | lost     |            -1    |                          -0.17 |
| 2026-10-31  | Kevin Durant PA over 26.5 (27+)        | OKC @ HOU | draftkings   |   1.95 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.14 |
| 2026-10-31  | Damian Lillard 3PM under 2.5           | POR @ UTA | draftkings   |   2.31 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-10-31  | Cam Spencer AST under 6.5              | SAC @ MEM | draftkings   |   1.95 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-10-31  | Domantas Sabonis PTS over 15.5 (16+)   | SAC @ MEM | unibet       |   1.88 | +0.5%  | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-10-31  | Scoot Henderson AST under 3.5          | POR @ UTA | draftkings   |   2    | +0.5%  | 0.1%          | won      |             1    |                           0.11 |
| 2026-10-31  | Donovan Mitchell PTS over 24.5 (25+)   | CLE @ MIL | pointsbetau  |   2    | +0.4%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-10-31  | Zion Williamson RA over 8.5 (9+)       | ATL @ NOP | draftkings   |   1.88 | +0.4%  | 0.1%          | won      |             0.88 |                           0.11 |
| 2026-10-31  | Zach Edey RA over 9.5 (10+)            | SAC @ MEM | draftkings   |   1.98 | +0.4%  | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-10-31  | Tyler Herro PRA under 30.5             | CLE @ MIL | draftkings   |   1.92 | +0.4%  | 0.1%          | won      |             0.92 |                           0.09 |
| 2026-10-31  | Precious Achiuwa RA over 9.5 (10+)     | SAC @ MEM | draftkings   |   1.99 | +0.3%  | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-10-31  | LaMelo Ball PTS under 19.5             | MIN @ SAS | betright     |   1.95 | +0.2%  | 0.1%          | won      |             0.95 |                           0.07 |
| 2026-10-31  | Dean Wade PR under 10.5                | PHI @ CHA | draftkings   |   1.93 | +0.2%  | 0.1%          | won      |             0.93 |                           0.07 |
| 2026-10-31  | Darius Acuff Jr. RA over 9.5 (10+)     | SAC @ MEM | draftkings   |   1.94 | +0.2%  | 0.1%          | won      |             0.94 |                           0.06 |
| 2026-10-31  | Brandon Miller PR under 31.5           | PHI @ CHA | draftkings   |   1.92 | +0.2%  | 0.1%          | won      |             0.92 |                           0.06 |
| 2026-10-31  | Zach Edey PR over 17.5 (18+)           | SAC @ MEM | draftkings   |   1.94 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-10-31  | De'Andre Hunter REB over 4.5 (5+)      | SAC @ MEM | draftkings   |   1.92 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-10-31  | Scoot Henderson PTS under 13.5         | POR @ UTA | ladbrokes_au |   1.94 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-10-31  | Marcus Smart 3PM under 1.5             | OKC @ HOU | draftkings   |   1.92 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-10-31  | Saddiq Bey PR over 17.5 (18+)          | ATL @ NOP | draftkings   |   1.91 | +0.2%  | 0.1%          | won      |             0.91 |                           0.05 |
| 2026-10-31  | Naz Reid PA under 20.5                 | PHI @ CHA | draftkings   |   1.88 | +0.2%  | 0.1%          | won      |             0.88 |                           0.04 |
| 2026-10-31  | Zion Williamson PRA over 28.5 (29+)    | ATL @ NOP | draftkings   |   1.87 | +0.2%  | 0.1%          | lost     |            -1    |                          -0.05 |
| 2026-10-31  | Kyle Kuzma REB under 5.5               | CLE @ MIL | draftkings   |   1.86 | +0.2%  | 0.1%          | won      |             0.86 |                           0.04 |
| 2026-10-31  | Ace Bailey PTS under 14.5              | POR @ UTA | betright     |   2    | +0.1%  | 0.0%          | won      |             1    |                           0.03 |
| 2026-10-31  | Jaylen Wells PRA over 19.5 (20+)       | SAC @ MEM | draftkings   |   1.96 | +0.1%  | 0.0%          | lost     |            -1    |                          -0.03 |
| 2026-10-31  | Cedric Coward REB over 6.5 (7+)        | SAC @ MEM | draftkings   |   2.05 | +0.1%  | 0.0%          | won      |             1.05 |                           0.02 |
| 2026-10-31  | Zion Williamson REB over 5.5 (6+)      | ATL @ NOP | draftkings   |   1.97 | +0.1%  | 0.0%          | won      |             0.97 |                           0.02 |
| 2026-10-31  | Stephon Castle PTS over 17.5 (18+)     | MIN @ SAS | draftkings   |   2.21 | +0.1%  | 0.0%          | lost     |            -1    |                          -0.02 |
| 2026-10-31  | Jalen Johnson PTS under 22.5           | ATL @ NOP | betright     |   1.9  | +0.1%  | 0.0%          | won      |             0.9  |                           0.02 |
| 2026-10-31  | Jaxson Hayes REB over 5.5 (6+)         | POR @ UTA | draftkings   |   1.88 | +0.1%  | 0.0%          | won      |             0.88 |                           0.02 |
| 2026-10-31  | Saddiq Bey PA over 15.5 (16+)          | ATL @ NOP | draftkings   |   1.94 | +0.0%  | 0.0%          | won      |             0.94 |                           0    |
| 2026-10-30  | Jarace Walker PTS over 10.5 (11+)      | IND @ MIA | pointsbetau  |   2    | +7.3%  | 1.8%          | won      |             1    |                           1.82 |

</details>

## Day by day (last 30)

Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising count means something in the inputs is going wrong.

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean | sanity flags   |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|:---------------|
| 2026-11-01 |       4 |        68 | 3.57 / 5.07                      | 4.79 / 4.52                     |          0.21 | 0 (none)       |
| 2026-10-31 |       7 |       115 | 6.06 / 6.77                      | 6.29 / 6.17                     |          1.87 | 0 (none)       |
| 2026-10-30 |      10 |       176 | 4.05 / 5.25                      | 4.96 / 5.12                     |          0.5  | 0 (none)       |
| 2026-10-29 |       3 |        53 | 4.86 / 5.88                      | 6.06 / 5.94                     |          1.13 | 0 (none)       |
| 2026-10-28 |      12 |       164 | 4.99 / 5.61                      | 5.21 / 5.43                     |          1.23 |                |
