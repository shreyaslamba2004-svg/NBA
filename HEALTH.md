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

Each table shows two ways of counting: units at a flat 1-unit stake on every bet (so results compare cleanly), and profit at the sheet's suggested stake, the quarter-Kelly % of bankroll capped at 2% that TODAY.md shows on every bet.

| window       |   bets |   won |   profit (units) |   ROI % |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |
|:-------------|-------:|------:|-----------------:|--------:|----------------------:|--------------------------------------:|
| Last 7 days  |      7 |     4 |             3.95 |    56.4 |                   6.2 |                                  4.35 |
| Last 30 days |      7 |     4 |             3.95 |    56.4 |                   6.2 |                                  4.35 |
| Season       |      7 |     4 |             3.95 |    56.4 |                   6.2 |                                  4.35 |

<details><summary>Every final-list bet (7)</summary>

| date (US)   | bet                                | game      | book       |   odds | EV    | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:-----------------------------------|:----------|:-----------|-------:|:------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-10-29  | Kingston Flemings PTS under 8.5    | CLE @ ATL | tab        |   2    | +8.5% | 2.0%          | won      |             1    |                           2    |
| 2026-10-29  | Damian Lillard AST over 5.5 (6+)   | MEM @ POR | draftkings |   3.87 | +6.4% | 0.6%          | lost     |            -1    |                          -0.56 |
| 2026-10-29  | Ja Morant AST over 7.5 (8+)        | MEM @ POR | draftkings |   3.25 | +5.4% | 0.6%          | lost     |            -1    |                          -0.6  |
| 2026-10-28  | Darius Garland PTS over 29.5 (30+) | LAL @ LAC | draftkings |   3.67 | +5.8% | 0.5%          | lost     |            -1    |                          -0.55 |
| 2026-10-28  | Jarace Walker REB over 6.5 (7+)    | PHI @ IND | draftkings |   3.43 | +5.8% | 0.6%          | won      |             2.43 |                           1.46 |
| 2026-10-28  | IND +5.5                           | PHI @ IND | unibet     |   1.95 | +5.4% | 1.4%          | won      |             0.95 |                           1.34 |
| 2026-10-28  | Pascal Siakam PRA over 39.5 (40+)  | PHI @ IND | draftkings |   3.57 | +5.0% | 0.5%          | won      |             2.57 |                           1.26 |

</details>

## Long shots (EV ≥ 5%, odds above 4)

TODAY.md's long-shot table, graded the same way: the final pre-tip list at the price shown then, 1 unit flat. Expect long losing runs; judge it over hundreds of bets.

| window       |   bets |   won |   profit (units) |   ROI % |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |
|:-------------|-------:|------:|-----------------:|--------:|----------------------:|--------------------------------------:|
| Last 7 days  |     50 |     2 |           -34.04 |   -68.1 |                  19.1 |                                -11.97 |
| Last 30 days |     50 |     2 |           -34.04 |   -68.1 |                  19.1 |                                -11.97 |
| Season       |     50 |     2 |           -34.04 |   -68.1 |                  19.1 |                                -11.97 |

<details><summary>Every long shot (50)</summary>

| date (US)   | bet                                    | game      | book       |   odds | EV     | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------------|:----------|:-----------|-------:|:-------|:--------------|:---------|-----------------:|-------------------------------:|
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

| window       |   bets |   won |   profit (units) |   ROI % |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |   avg CLV % |   beat closing % |
|:-------------|-------:|------:|-----------------:|--------:|----------------------:|--------------------------------------:|------------:|-----------------:|
| Last 7 days  |     36 |    20 |            14.17 |    39.4 |                   9.5 |                                  4.19 |         2.7 |               25 |
| Last 30 days |     36 |    20 |            14.17 |    39.4 |                   9.5 |                                  4.19 |         2.7 |               25 |
| Season       |     36 |    20 |            14.17 |    39.4 |                   9.5 |                                  4.19 |         2.7 |               25 |

CLV (closing-line value) compares the price taken with the final no-vig market price before tip. Positive CLV over a few hundred bets is the earliest reliable sign of a real edge; ROI swings for months.

## Best player props per game (main lines)

The "Best player props" box in each game's section of TODAY.md: every main-line prop with positive EV, no news flag and offered at Sportsbet, as listed on the last update before tip, graded at the price shown then. These include edges under 5%, so expect a thinner margin than best bets.

| window       |   bets |   won |   profit (units) |   ROI % |   staked (% bankroll) |   profit at sheet stakes (% bankroll) |
|:-------------|-------:|------:|-----------------:|--------:|----------------------:|--------------------------------------:|
| Last 7 days  |     27 |    10 |            -7.62 |   -28.2 |                   9.7 |                                 -0.23 |
| Last 30 days |     27 |    10 |            -7.62 |   -28.2 |                   9.7 |                                 -0.23 |
| Season       |     27 |    10 |            -7.62 |   -28.2 |                   9.7 |                                 -0.23 |

<details><summary>Every graded game prop (27)</summary>

| date (US)   | bet                                    | game      | book       |   odds | EV    | sheet stake   | result   |   units (1 flat) |   profit at stake (% bankroll) |
|:------------|:---------------------------------------|:----------|:-----------|-------:|:------|:--------------|:---------|-----------------:|-------------------------------:|
| 2026-10-29  | Kingston Flemings PTS under 8.5        | CLE @ ATL | tab        |   2    | +8.5% | 2.0%          | won      |             1    |                           2    |
| 2026-10-29  | Cedric Coward PTS under 12.5           | MEM @ POR | draftkings |   1.94 | +4.4% | 1.1%          | lost     |            -1    |                          -1.15 |
| 2026-10-29  | Jalen Johnson PTS under 22.5           | CLE @ ATL | unibet     |   1.91 | +3.2% | 0.9%          | won      |             0.91 |                           0.8  |
| 2026-10-29  | Sam Merrill PTS under 8.5              | CLE @ ATL | tab        |   1.95 | +2.9% | 0.8%          | lost     |            -1    |                          -0.75 |
| 2026-10-29  | Ty Jerome PTS under 23.5               | MEM @ POR | tab        |   1.95 | +2.6% | 0.7%          | won      |             0.95 |                           0.66 |
| 2026-10-29  | Jrue Holiday PTS over 12.5 (13+)       | MEM @ POR | tab        |   1.95 | +2.5% | 0.7%          | lost     |            -1    |                          -0.65 |
| 2026-10-29  | Derik Queen PTS over 11.5 (12+)        | SAC @ NOP | sportsbet  |   1.92 | +2.4% | 0.7%          | lost     |            -1    |                          -0.67 |
| 2026-10-29  | Ty Jerome PTS under 24.5               | MEM @ POR | betright   |   1.86 | +2.0% | 0.6%          | won      |             0.86 |                           0.51 |
| 2026-10-29  | Aaron Wiggins PTS under 11.5           | CLE @ ATL | draftkings |   1.99 | +1.7% | 0.4%          | lost     |            -1    |                          -0.44 |
| 2026-10-29  | Scoot Henderson PTS over 8.5 (9+)      | MEM @ POR | tab        |   1.9  | +0.9% | 0.2%          | won      |             0.9  |                           0.22 |
| 2026-10-29  | Zach Edey PTS under 8.5                | MEM @ POR | draftkings |   1.9  | +0.9% | 0.2%          | lost     |            -1    |                          -0.25 |
| 2026-10-29  | Dyson Daniels PTS under 11.5           | CLE @ ATL | tab        |   1.87 | +0.7% | 0.2%          | won      |             0.87 |                           0.18 |
| 2026-10-29  | Damian Lillard RA over 8.5 (9+)        | MEM @ POR | draftkings |   2.1  | +0.6% | 0.1%          | lost     |            -1    |                          -0.13 |
| 2026-10-29  | Donovan Mitchell PTS over 24.5 (25+)   | CLE @ ATL | sportsbet  |   2.02 | +0.4% | 0.1%          | lost     |            -1    |                          -0.1  |
| 2026-10-29  | Derik Queen REB over 7.5 (8+)          | SAC @ NOP | draftkings |   1.92 | +0.3% | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-10-29  | Cedric Coward PA under 15.5            | MEM @ POR | draftkings |   1.88 | +0.2% | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-10-29  | Darius Acuff Jr. PA under 28.5         | SAC @ NOP | draftkings |   1.81 | +0.2% | 0.1%          | lost     |            -1    |                          -0.07 |
| 2026-10-29  | De'Andre Hunter PTS under 12.5         | SAC @ NOP | tab        |   1.85 | +0.2% | 0.1%          | lost     |            -1    |                          -0.06 |
| 2026-10-29  | Damian Lillard 3PM under 2.5           | MEM @ POR | draftkings |   2.28 | +0.2% | 0.0%          | won      |             1.28 |                           0.05 |
| 2026-10-29  | Zion Williamson PTS over 21.5 (22+)    | SAC @ NOP | draftkings |   1.89 | +0.1% | 0.0%          | won      |             0.89 |                           0.03 |
| 2026-10-29  | Darius Acuff Jr. PTS under 22.5        | SAC @ NOP | draftkings |   1.86 | +0.0% | 0.0%          | lost     |            -1    |                          -0.01 |
| 2026-10-28  | Kevin Durant RA over 10.5 (11+)        | HOU @ MIL | draftkings |   1.97 | +0.9% | 0.2%          | lost     |            -1    |                          -0.24 |
| 2026-10-28  | Karl-Anthony Towns RA under 16.5       | NYK @ CHI | draftkings |   1.94 | +0.5% | 0.1%          | lost     |            -1    |                          -0.12 |
| 2026-10-28  | Kel'el Ware PR under 17.5              | HOU @ MIL | draftkings |   1.86 | +0.4% | 0.1%          | won      |             0.86 |                           0.09 |
| 2026-10-28  | Dejounte Murray PTS under 17.5         | DEN @ NOP | draftkings |   1.86 | +0.2% | 0.1%          | won      |             0.86 |                           0.06 |
| 2026-10-28  | Wendell Carter Jr. PTS over 10.5 (11+) | ORL @ TOR | draftkings |   1.84 | +0.1% | 0.0%          | lost     |            -1    |                          -0.04 |
| 2026-10-28  | Aaron Gordon 3PM under 1.5             | DEN @ NOP | draftkings |   2.08 | +0.1% | 0.0%          | lost     |            -1    |                          -0.02 |

</details>

## Day by day (last 30)

Sanity flags are the automatic checks on the day's last projections (see TODAY.md): a rising count means something in the inputs is going wrong.

| date       |   games |   players | minutes miss (model / last-10)   | points miss (model / last-10)   |   points lean | sanity flags   |
|:-----------|--------:|----------:|:---------------------------------|:--------------------------------|--------------:|:---------------|
| 2026-10-29 |       3 |        53 | 4.86 / 5.88                      | 6.06 / 5.94                     |          1.13 | 0 (none)       |
| 2026-10-28 |      12 |       164 | 4.99 / 5.61                      | 5.21 / 5.43                     |          1.23 |                |
