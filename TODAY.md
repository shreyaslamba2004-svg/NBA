# NBA model · Sat 07 Nov 2026 (US date)

Updated **Sun 08 Nov, 03:29 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-07/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| IND to win | DEN @ IND | betfair_ex_au | 3.61 | 3.42 | 3.11 | 32.2% | 29.2% | 29.2% | +5.6% | +16.3% | 0.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| WAS to win | WAS @ OKC | betfair_ex_au | 5.28 | 4.83 | 3.62 | 27.7% | 20.7% | 20.7% | +9.1% | +45.9% | 0.5% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DEN @ IND | Sun 08 Nov 09:00 | 122.3–115.7 | DEN 68% | 1.46 / 3.16 | IND +6.5 | 238.5 | IND +7.5 covers 52%; o229.5 68% |
| BKN @ ATL | Sun 08 Nov 11:30 | 105.6–114.5 | BKN 26% | 3.78 / 1.36 | ATL -8.5 | 219.5 | ATL -7.5 covers 54%; o227.5 34% |
| NYK @ CLE | Sun 08 Nov 12:00 | 115.3–107.5 | NYK 71% | 1.41 / 3.43 | CLE +7.5 | 222.5 | CLE +4.5 covers 40%; o224.5 46% |
| WAS @ OKC | Sun 08 Nov 12:00 | 111.0–119.2 | WAS 28% | 3.58 / 1.39 | OKC -8.5 | 229.5 | OKC -12.5 covers 38%; o222.5 66% |
| ORL @ GSW | Sun 08 Nov 12:30 | 108.9–114.7 | ORL 34% | 2.97 / 1.51 | GSW -5.5 | 223.5 | GSW -5.5 covers 51%; o222.5 52% |
| HOU @ PHX | Sun 08 Nov 13:00 | 115.9–109.8 | HOU 67% | 1.50 / 2.99 | PHX +6.5 | 225.5 | PHX +6.5 covers 51%; o223.5 54% |
| SAS @ POR | Sun 08 Nov 14:00 | 113.9–109.6 | SAS 62% | 1.62 / 2.62 | POR +4.5 | 223.5 | POR +5.5 covers 53%; o226.5 43% |

### DEN @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND), Julian Strawther (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 122.3–115.7 | DEN 68% | 1.46 / 3.16 | IND +6.5 | 238.5 | IND +7.5 covers 52%; o229.5 68% |
| Expected (weighted by chance each plays) | 121.7–115.3 | DEN 68% | 1.47 / 3.11 | IND +6.5 | 237.5 | IND +7.5 covers 53%; o229.5 67% |
| if Kelly Oubre Jr. plays | 121.7–115.3 | DEN 68% | 1.48 / 3.09 | IND +6.5 | 236.5 | IND +7.5 covers 53%; o229.5 66% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| T.J. McConnell (IND) | Questionable | 55% | 13.0 | 6.6 | 1.8 | 3.9 | 0.2 | 0.7 | 0.2 | 0.8 | 12.2 | small |
| Kelly Oubre Jr. (IND) | Questionable | 55% | 22.6 | 9.8 | 3.4 | 1.3 | 0.9 | 0.8 | 0.4 | 0.9 | 14.5 | full tables below |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 36.1<br><sub>36,38,37,39,28</sub> | 26.0<br><sub>19,23,39,35,14</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,1,8,5,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>8,6,5,6,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>3,5,7,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.5 | 37.3 |
| Nikola Jokic | 98% | 35.2<br><sub>35,34,37,36,30</sub> | 27.4<br><sub>19,21,18,26,32</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.7<br><sub>7,13,7,9,10</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 10.1<br><sub>11,10,10,8,11</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7 | 0.9 | 3.6 | 50.1 |
| Christian Braun | 98% | 33.2<br><sub>34,36,37,37,28</sub> | 13.2<br><sub>9,15,31,14,11</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>4,0,3,3,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,4,1,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>1,3,7,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.4 | 1.1 | 20.2 |
| Cameron Johnson | 98% | 28.6<br><sub>-,-,34,34,30</sub> | 12.0<br><sub>-,-,12,7,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>-,-,9,4,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>-,-,2,1,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.4 | 1.0 | 18.3 |
| Aaron Gordon | 98% | 28.3<br><sub>25,31,29,30,25</sub> | 13.1<br><sub>7,15,15,5,17</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>4,11,4,6,1</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,3,5,2,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.4 | 1.2 | 21.5 |
| DeMar DeRozan | 67% | 24.1<br><sub>29,26,24,20,-</sub> | 12.7<br><sub>21,6,3,9,-</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,2,1,0,-</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>2,5,5,1,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.5<br><sub>2,0,0,0,-</sub> |  | 0.9 | 0.3 | 1.4 | 18.5 |
| Trevon Brazile | 96% | 19.9<br><sub>17,32,19,18,23</sub> | 6.2<br><sub>6,11,6,6,6</sub> |  | 5.0<br><sub>1,8,3,5,7</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.8 | 12.1 |
| Bryce Hopkins | 64% | 18.6<br><sub>31,14,-,-,28</sub> | 5.9<br><sub>13,0,-,-,18</sub> |  | 2.9<br><sub>3,2,-,-,4</sub> |  | 1.0<br><sub>1,0,-,-,1</sub> |  | 0.4<br><sub>1,0,-,-,1</sub> |  | 0.8 | 0.3 | 1.0 | 9.7 |
| Marvin Bagley III | 98% | 13.1<br><sub>11,19,11,12,14</sub> | 6.4<br><sub>7,8,0,6,10</sub> |  | 4.1<br><sub>2,5,5,4,2</sub> |  | 0.8<br><sub>0,1,0,0,2</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 11.3 |
| Tyus Jones | 93% | 12.7<br><sub>9,11,11,8,18</sub> | 3.5<br><sub>0,5,3,2,6</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 2.1<br><sub>2,1,0,1,8</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.5 |
| Spencer Jones | 3% | 9.0 | 3.7 |  | 1.7 |  | 0.9 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Alpha Diallo | 91% | 7.7<br><sub>-,-,-,6,4</sub> | 3.6<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Cam Whitmore | 58% | 7.3<br><sub>4,-,-,-,-</sub> | 3.8<br><sub>4,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.6 |
| Ryan Nembhard | 52% | 6.5<br><sub>4,-,-,-,4</sub> | 2.8<br><sub>4,-,-,-,0</sub> |  | 1.0<br><sub>0,-,-,-,0</sub> |  | 0.6<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Zeke Nnaji | 48% | 6.5<br><sub>4,-,-,-,4</sub> | 2.2<br><sub>5,-,-,-,2</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.3 | 4.1 |
| DaRon Holmes II | 52% | 5.8<br><sub>4,-,-,-,4</sub> | 2.5<br><sub>0,-,-,-,0</sub> |  | 1.2<br><sub>0,-,-,-,1</sub> |  | 0.4<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 71% | 34.5<br><sub>35,30,35,-,38</sub> | 19.9<br><sub>18,22,23,-,22</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>3,2,3,-,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 9.0<br><sub>14,9,4,-,5</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,5,4,-,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.2 | 2.4 | 31.9 |
| Pascal Siakam | 80% | 33.0<br><sub>34,29,36,-,30</sub> | 23.3<br><sub>26,13,17,-,20</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>11,5,5,-,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>3,4,5,-,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>0,0,0,-,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 2.4 | 34.5 |
| Aaron Nesmith | 80% | 28.5<br><sub>27,21,30,-,30</sub> | 14.9<br><sub>18,9,11,-,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,3,3,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,2,4,-,2</sub> |  | 2.1<br><sub>3,1,0,-,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.5 | 1.4 | 20.4 |
| Quenton Jackson | 98% | 26.2<br><sub>14,24,24,35,22</sub> | 13.2<br><sub>2,24,12,20,13</sub> |  | 3.5<br><sub>2,4,3,7,7</sub> |  | 4.3<br><sub>6,1,2,3,2</sub> |  | 1.2<br><sub>0,2,3,1,3</sub> |  | 1.1 | 0.2 | 1.5 | 21.0 |
| Jarace Walker | 98% | 25.8<br><sub>22,28,20,45,17</sub> | 12.3<br><sub>7,14,6,15,2</sub> |  | 5.6<br><sub>8,6,6,7,8</sub> |  | 2.8<br><sub>1,4,3,3,1</sub> |  | 1.5<br><sub>1,3,2,1,0</sub> |  | 0.8 | 0.3 | 1.6 | 20.8 |
| Ivica Zubac | 52% | 23.8<br><sub>-,-,-,-,19</sub> | 10.9<br><sub>-,-,-,-,1</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 8.6<br><sub>-,-,-,-,4</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.7 | 1.3 | 21.3 |
| Braden Smith | 88% | 22.2<br><sub>5,12,1,42,24</sub> | 8.5<br><sub>0,1,0,19,10</sub> |  | 2.2<br><sub>0,0,0,4,1</sub> |  | 4.3<br><sub>1,1,0,10,5</sub> |  | 0.6<br><sub>0,0,0,2,0</sub> |  | 1.0 | 0.4 | 1.4 | 15.0 |
| Obi Toppin | 58% | 21.1<br><sub>22,-,-,-,19</sub> | 13.1<br><sub>13,-,-,-,11</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,-,-,-,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,-,-,-,1</sub> |  | 1.7<br><sub>1,-,-,-,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.2 | 1.1 | 19.7 |
| Jay Huff | 93% | 20.6<br><sub>16,19,17,40,14</sub> | 9.3<br><sub>3,13,0,22,6</sub> |  | 4.0<br><sub>6,1,3,8,3</sub> |  | 1.5<br><sub>2,0,0,2,1</sub> |  | 1.2<br><sub>1,3,0,0,2</sub> |  | 0.5 | 1.2 | 0.9 | 14.7 |
| Kobe Brown | 72% | 18.4<br><sub>-,20,15,38,7</sub> | 7.1<br><sub>-,9,3,16,0</sub> |  | 3.3<br><sub>-,6,1,6,1</sub> |  | 1.6<br><sub>-,4,1,1,0</sub> |  | 0.8<br><sub>-,0,1,2,0</sub> |  | 0.5 | 0.2 | 0.8 | 12.0 |
| Jalen Slawson | 91% | 16.8<br><sub>12,18,18,41,6</sub> | 5.3<br><sub>2,4,3,12,2</sub> |  | 3.2<br><sub>1,4,5,7,2</sub> |  | 1.5<br><sub>1,1,0,3,1</sub> |  | 0.4<br><sub>0,0,0,2,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.0 |
| Larry Nance Jr. | 91% | 16.0<br><sub>23,18,26,-,14</sub> | 5.0<br><sub>5,6,4,-,4</sub> |  | 3.3<br><sub>5,2,6,-,4</sub> |  | 1.0<br><sub>0,1,1,-,1</sub> |  | 0.5<br><sub>1,2,1,-,0</sub> |  | 0.7 | 0.2 | 0.6 | 9.3 |

</details>

<details><summary>if Kelly Oubre Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray (DEN) | 98% | 36.2<br><sub>36,38,37,39,28</sub> | 26.0<br><sub>19,23,39,35,14</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,1,8,5,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>8,6,5,6,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>3,5,7,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.5 | 37.3 |
| Nikola Jokic (DEN) | 98% | 35.2<br><sub>35,34,37,36,30</sub> | 27.2<br><sub>19,21,18,26,32</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.6<br><sub>7,13,7,9,10</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 10.1<br><sub>11,10,10,8,11</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7 | 0.9 | 3.6 | 49.9 |
| Christian Braun (DEN) | 98% | 33.1<br><sub>34,36,37,37,28</sub> | 13.2<br><sub>9,15,31,14,11</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>4,0,3,3,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,4,1,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>1,3,7,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.4 | 1.1 | 20.2 |
| Cameron Johnson (DEN) | 98% | 28.6<br><sub>-,-,34,34,30</sub> | 12.0<br><sub>-,-,12,7,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>-,-,9,4,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>-,-,2,1,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.4 | 1.0 | 18.3 |
| Aaron Gordon (DEN) | 98% | 28.3<br><sub>25,31,29,30,25</sub> | 13.1<br><sub>7,15,15,5,17</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>4,11,4,6,1</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,3,5,2,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.4 | 1.2 | 21.4 |
| DeMar DeRozan (DEN) | 67% | 24.0<br><sub>29,26,24,20,-</sub> | 12.7<br><sub>21,6,3,9,-</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,2,1,0,-</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>2,5,5,1,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>2,0,0,0,-</sub> |  | 0.9 | 0.3 | 1.4 | 18.4 |
| Trevon Brazile (DEN) | 96% | 19.9<br><sub>17,32,19,18,23</sub> | 6.2<br><sub>6,11,6,6,6</sub> |  | 5.0<br><sub>1,8,3,5,7</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.8 | 12.1 |
| Bryce Hopkins (DEN) | 64% | 18.5<br><sub>31,14,-,-,28</sub> | 5.8<br><sub>13,0,-,-,18</sub> |  | 2.9<br><sub>3,2,-,-,4</sub> |  | 1.0<br><sub>1,0,-,-,1</sub> |  | 0.4<br><sub>1,0,-,-,1</sub> |  | 0.8 | 0.3 | 1.0 | 9.7 |
| Marvin Bagley III (DEN) | 98% | 13.1<br><sub>11,19,11,12,14</sub> | 6.3<br><sub>7,8,0,6,10</sub> |  | 4.1<br><sub>2,5,5,4,2</sub> |  | 0.7<br><sub>0,1,0,0,2</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 11.2 |
| Tyus Jones (DEN) | 93% | 12.7<br><sub>9,11,11,8,18</sub> | 3.4<br><sub>0,5,3,2,6</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 2.1<br><sub>2,1,0,1,8</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.5 |
| Spencer Jones (DEN) | 3% | 8.5 | 3.3 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.7 |
| Alpha Diallo (DEN) | 91% | 7.7<br><sub>-,-,-,6,4</sub> | 3.5<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Cam Whitmore (DEN) | 58% | 7.2<br><sub>4,-,-,-,-</sub> | 3.8<br><sub>4,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |
| Ryan Nembhard (DEN) | 52% | 6.5<br><sub>4,-,-,-,4</sub> | 2.8<br><sub>4,-,-,-,0</sub> |  | 1.0<br><sub>0,-,-,-,0</sub> |  | 0.6<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Zeke Nnaji (DEN) | 48% | 6.4<br><sub>4,-,-,-,4</sub> | 2.2<br><sub>5,-,-,-,2</sub> |  | 1.4<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.3 | 4.0 |
| DaRon Holmes II (DEN) | 52% | 5.8<br><sub>4,-,-,-,4</sub> | 2.5<br><sub>0,-,-,-,0</sub> |  | 1.2<br><sub>0,-,-,-,1</sub> |  | 0.4<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |
| Andrew Nembhard (IND) | 71% | 32.6<br><sub>35,30,35,-,38</sub> | 18.3<br><sub>18,22,23,-,22</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>3,2,3,-,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 8.7<br><sub>14,9,4,-,5</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,5,4,-,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.1 | 2.3 | 29.8 |
| Pascal Siakam (IND) | 80% | 32.0<br><sub>34,29,36,-,30</sub> | 22.5<br><sub>26,13,17,-,20</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>11,5,5,-,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>3,4,5,-,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,0,0,-,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.3 | 2.3 | 33.4 |
| Aaron Nesmith (IND) | 80% | 26.8<br><sub>27,21,30,-,30</sub> | 14.0<br><sub>18,9,11,-,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,3,3,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>1,2,4,-,2</sub> |  | 1.9<br><sub>3,1,0,-,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.4 | 1.3 | 19.4 |
| Jarace Walker (IND) | 98% | 23.5<br><sub>22,28,20,45,17</sub> | 10.9<br><sub>7,14,6,15,2</sub> |  | 5.2<br><sub>8,6,6,7,8</sub> |  | 2.6<br><sub>1,4,3,3,1</sub> |  | 1.4<br><sub>1,3,2,1,0</sub> |  | 0.8 | 0.3 | 1.4 | 18.8 |
| Quenton Jackson (IND) | 98% | 23.3<br><sub>14,24,24,35,22</sub> | 11.6<br><sub>2,24,12,20,13</sub> |  | 3.1<br><sub>2,4,3,7,7</sub> |  | 3.9<br><sub>6,1,2,3,2</sub> |  | 1.0<br><sub>0,2,3,1,3</sub> |  | 1.0 | 0.2 | 1.3 | 18.6 |
| Kelly Oubre Jr. (IND) | 100% | 22.6<br><sub>30,22,20,-,-</sub> | 9.8<br><sub>15,10,11,-,-</sub> | 9.5 · – | 3.4<br><sub>3,4,2,-,-</sub> | 3.5 | 1.3<br><sub>1,1,1,-,-</sub> |  | 0.9<br><sub>1,1,2,-,-</sub> | 1.5 | 0.8 | 0.4 | 0.9 | 14.5 |
| Ivica Zubac (IND) | 52% | 22.0<br><sub>-,-,-,-,19</sub> | 10.2<br><sub>-,-,-,-,1</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 8.0<br><sub>-,-,-,-,4</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.6 | 1.2 | 19.8 |
| Obi Toppin (IND) | 58% | 19.9<br><sub>22,-,-,-,19</sub> | 12.9<br><sub>13,-,-,-,11</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>6,-,-,-,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>0,-,-,-,1</sub> |  | 1.6<br><sub>1,-,-,-,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.2 | 1.1 | 19.4 |
| Braden Smith (IND) | 88% | 19.0<br><sub>5,12,1,42,24</sub> | 7.2<br><sub>0,1,0,19,10</sub> |  | 1.8<br><sub>0,0,0,4,1</sub> |  | 3.6<br><sub>1,1,0,10,5</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.8 | 0.4 | 1.2 | 12.7 |
| Jay Huff (IND) | 93% | 18.0<br><sub>16,19,17,40,14</sub> | 8.2<br><sub>3,13,0,22,6</sub> |  | 3.5<br><sub>6,1,3,8,3</sub> |  | 1.4<br><sub>2,0,0,2,1</sub> |  | 1.0<br><sub>1,3,0,0,2</sub> |  | 0.4 | 1.1 | 0.8 | 13.1 |
| Kobe Brown (IND) | 72% | 15.1<br><sub>-,20,15,38,7</sub> | 5.8<br><sub>-,9,3,16,0</sub> |  | 2.7<br><sub>-,6,1,6,1</sub> |  | 1.4<br><sub>-,4,1,1,0</sub> |  | 0.6<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.9 |
| Larry Nance Jr. (IND) | 91% | 14.4<br><sub>23,18,26,-,14</sub> | 4.5<br><sub>5,6,4,-,4</sub> |  | 3.0<br><sub>5,2,6,-,4</sub> |  | 0.9<br><sub>0,1,1,-,1</sub> |  | 0.4<br><sub>1,2,1,-,0</sub> |  | 0.7 | 0.2 | 0.5 | 8.4 |
| Jalen Slawson (IND) | 91% | 14.0<br><sub>12,18,18,41,6</sub> | 4.5<br><sub>2,4,3,12,2</sub> |  | 2.6<br><sub>1,4,5,7,2</sub> |  | 1.3<br><sub>1,1,0,3,1</sub> |  | 0.3<br><sub>0,0,0,2,0</sub> |  | 0.7 | 0.6 | 0.7 | 8.4 |

</details>


### BKN @ ATL
Out: Mouhamed Gueye (ATL), Jalen Johnson (ATL), Jock Landale (ATL), Egor Demin (BKN), Grant Nelson (BKN), Ben Saraf (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.6–114.5 | BKN 26% | 3.78 / 1.36 | ATL -8.5 | 219.5 | ATL -7.5 covers 54%; o227.5 34% |
| Expected (weighted by chance each plays) | 106.1–114.3 | BKN 27% | 3.64 / 1.38 | ATL -8.5 | 220.5 | ATL -7.5 covers 53%; o227.5 34% |
| if Noah Clowney plays | 105.9–114.4 | BKN 28% | 3.63 / 1.38 | ATL -8.5 | 220.5 | ATL -7.5 covers 52%; o227.5 35% |
| if Day'Ron Sharpe plays | 106.9–113.7 | BKN 32% | 3.16 / 1.46 | ATL -6.5 | 220.5 | ATL -7.5 covers 48%; o227.5 35% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Noah Clowney (BKN) | Questionable | 55% | 22.7 | 8.2 | 4.2 | 1.2 | 1.1 | 0.7 | 0.5 | 1.0 | 13.7 | full tables below |
| Keshon Gilbert (ATL) | Day-To-Day | 70% | 8.0 | 2.4 | 1.1 | 1.2 | 0.1 | 0.3 | 0.2 | 0.6 | 4.8 | small |
| Asa Newell (ATL) | Day-To-Day | 70% | 12.5 | 5.2 | 2.6 | 0.9 | 0.4 | 0.5 | 0.3 | 0.6 | 8.7 | small |
| Day'Ron Sharpe (BKN) | Day-To-Day | 70% | 23.8 | 9.2 | 8.5 | 3.0 | 0.3 | 1.1 | 0.8 | 2.1 | 20.6 | full tables below |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 98% | 34.8<br><sub>40,26,36,37,38</sub> | 23.4<br><sub>27,13,23,18,26</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>12,7,9,5,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>2,1,3,2,0</sub> |  | 3.1<br><sub>6,2,3,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.9 | 34.0 |
| Julius Randle | 98% | 34.8<br><sub>44,25,37,36,31</sub> | 21.9<br><sub>24,15,20,21,22</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>9,8,5,11,3</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 5.1<br><sub>4,3,6,2,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,3,4,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 4.1 | 34.8 |
| Nolan Traore | 98% | 27.8<br><sub>24,26,30,24,27</sub> | 13.6<br><sub>15,9,16,17,16</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>1,2,2,3,4</sub> |  | 4.2<br><sub>3,2,6,4,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>1,0,4,5,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 3.2 | 20.5 |
| Mikel Brown Jr. | 96% | 27.2<br><sub>28,23,-,27,20</sub> | 12.5<br><sub>17,10,-,13,18</sub> |  | 3.1<br><sub>5,0,-,2,2</sub> |  | 4.0<br><sub>5,4,-,3,4</sub> |  | 1.8<br><sub>4,0,-,1,3</sub> |  | 0.8 | 0.3 | 2.4 | 19.6 |
| Chaney Johnson | 93% | 24.8<br><sub>29,19,31,28,9</sub> | 7.0<br><sub>15,6,2,4,0</sub> |  | 3.5<br><sub>3,2,2,3,2</sub> |  | 1.3<br><sub>2,0,0,2,1</sub> |  | 0.8<br><sub>3,0,0,1,0</sub> |  | 0.8 | 0.5 | 1.3 | 11.8 |
| Keon Ellis | 96% | 23.5<br><sub>25,21,20,25,10</sub> | 6.2<br><sub>2,6,0,5,1</sub> |  | 2.4<br><sub>3,2,2,1,2</sub> |  | 1.5<br><sub>4,1,1,0,0</sub> |  | 0.8<br><sub>0,2,0,1,0</sub> |  | 1.3 | 0.8 | 0.9 | 10.2 |
| Moritz Wagner | 93% | 22.9<br><sub>22,23,21,20,20</sub> | 10.9<br><sub>15,16,14,6,6</sub> |  | 5.6<br><sub>4,8,6,1,1</sub> |  | 1.5<br><sub>3,1,0,2,0</sub> |  | 0.9<br><sub>2,1,1,1,0</sub> |  | 0.7 | 0.4 | 1.3 | 18.0 |
| Danny Wolf | 52% | 20.7<br><sub>-,12,-,-,19</sub> | 9.3<br><sub>-,9,-,-,12</sub> |  | 5.4<br><sub>-,6,-,-,5</sub> |  | 2.1<br><sub>-,2,-,-,3</sub> |  | 1.1<br><sub>-,3,-,-,2</sub> |  | 0.6 | 0.5 | 1.3 | 16.8 |
| Terance Mann | 58% | 19.8<br><sub>-,12,15,-,16</sub> | 5.1<br><sub>-,2,0,-,0</sub> |  | 2.5<br><sub>-,0,1,-,2</sub> |  | 1.8<br><sub>-,2,1,-,2</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.6 | 0.2 | 1.0 | 9.5 |
| Drake Powell | 52% | 15.6<br><sub>-,6,-,-,-</sub> | 5.1<br><sub>-,0,-,-,-</sub> |  | 1.5<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,2,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 7.6 |
| Josh Minott | 52% | 14.7<br><sub>-,3,-,-,6</sub> | 6.8<br><sub>-,2,-,-,0</sub> |  | 2.8<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.7 | 0.5 | 0.8 | 10.5 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker | 98% | 31.1<br><sub>31,29,31,32,33</sub> | 22.6<br><sub>25,12,34,26,28</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,2,4,4,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.5<br><sub>1,1,4,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>4,0,9,6,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.5 | 2.5 | 29.2 |
| Onyeka Okongwu | 98% | 31.0<br><sub>33,28,33,31,33</sub> | 15.1<br><sub>29,6,13,14,22</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>12,10,10,16,10</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>2,1,3,4,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>4,0,2,2,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.0 | 1.5 | 26.4 |
| Dyson Daniels | 98% | 30.7<br><sub>32,27,31,34,35</sub> | 11.5<br><sub>4,8,6,8,13</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>6,4,9,16,9</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>5,3,4,8,12</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.3 | 0.5 | 1.8 | 24.7 |
| Luguentz Dort | 98% | 28.5<br><sub>22,29,31,31,32</sub> | 10.7<br><sub>6,11,14,6,25</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,3,2,3,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,0,0,3,4</sub> |  | 1.7<br><sub>1,1,4,2,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.4 | 0.9 | 16.3 |
| CJ McCollum | 98% | 26.8<br><sub>31,24,32,25,23</sub> | 17.1<br><sub>5,14,13,15,4</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>3,2,9,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>8,2,12,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 2.3 | 24.5 |
| Aaron Wiggins | 97% | 25.5<br><sub>24,23,24,29,29</sub> | 12.9<br><sub>20,10,7,15,19</sub> |  | 3.4<br><sub>7,2,3,4,4</sub> |  | 2.2<br><sub>3,1,2,2,3</sub> |  | 1.9<br><sub>4,2,1,3,3</sub> |  | 1.0 | 0.4 | 1.5 | 18.6 |
| Kingston Flemings | 86% | 22.5<br><sub>16,25,-,23,25</sub> | 9.0<br><sub>2,12,-,14,11</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>1,2,-,3,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 5.1<br><sub>5,6,-,4,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.7<br><sub>0,1,-,2,1</sub> |  | 0.8 | 0.3 | 1.9 | 17.0 |
| Zuby Ejiofor | 66% | 15.8<br><sub>-,-,15,17,15</sub> | 6.3<br><sub>-,-,3,11,10</sub> |  | 3.4<br><sub>-,-,5,3,5</sub> |  | 2.4<br><sub>-,-,2,2,5</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.5 | 0.2 | 1.0 | 12.1 |
| Corey Kispert | 72% | 15.8<br><sub>-,5,18,8,16</sub> | 8.4<br><sub>-,0,14,9,7</sub> |  | 1.9<br><sub>-,0,1,0,2</sub> |  | 1.4<br><sub>-,1,0,1,1</sub> |  | 1.2<br><sub>-,0,4,1,1</sub> |  | 0.3 | 0.2 | 0.8 | 11.7 |
| Jalen Wilson | 52% | 11.7<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 7.6 |
| RayJ Dennis | 72% | 11.2<br><sub>-,-,8,-,-</sub> | 3.9<br><sub>-,-,4,-,-</sub> |  | 1.5<br><sub>-,-,2,-,-</sub> |  | 2.0<br><sub>-,-,2,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.8 | 7.4 |
| Dorian Finney-Smith | 38% | 7.2<br><sub>-,3,-,-,-</sub> | 2.0<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |

</details>

<details><summary>if Day'Ron Sharpe plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker (ATL) | 98% | 31.1<br><sub>31,29,31,32,33</sub> | 22.4<br><sub>25,12,34,26,28</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,2,4,4,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.5<br><sub>1,1,4,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>4,0,9,6,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.5 | 2.5 | 29.0 |
| Onyeka Okongwu (ATL) | 98% | 30.9<br><sub>33,28,33,31,33</sub> | 15.1<br><sub>29,6,13,14,22</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>12,10,10,16,10</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>2,1,3,4,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>4,0,2,2,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 1.0 | 1.5 | 26.2 |
| Dyson Daniels (ATL) | 98% | 30.7<br><sub>32,27,31,34,35</sub> | 11.6<br><sub>4,8,6,8,13</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>6,4,9,16,9</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>5,3,4,8,12</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.3 | 0.5 | 1.8 | 24.8 |
| Luguentz Dort (ATL) | 98% | 28.5<br><sub>22,29,31,31,32</sub> | 10.6<br><sub>6,11,14,6,25</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,3,2,3,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,0,0,3,4</sub> |  | 1.7<br><sub>1,1,4,2,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.4 | 0.9 | 16.2 |
| CJ McCollum (ATL) | 98% | 26.8<br><sub>31,24,32,25,23</sub> | 17.1<br><sub>5,14,13,15,4</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>3,2,9,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>8,2,12,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 2.3 | 24.6 |
| Aaron Wiggins (ATL) | 97% | 25.6<br><sub>24,23,24,29,29</sub> | 12.9<br><sub>20,10,7,15,19</sub> |  | 3.4<br><sub>7,2,3,4,4</sub> |  | 2.2<br><sub>3,1,2,2,3</sub> |  | 2.0<br><sub>4,2,1,3,3</sub> |  | 1.0 | 0.4 | 1.5 | 18.5 |
| Kingston Flemings (ATL) | 86% | 22.5<br><sub>16,25,-,23,25</sub> | 9.1<br><sub>2,12,-,14,11</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>1,2,-,3,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 5.1<br><sub>5,6,-,4,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.7<br><sub>0,1,-,2,1</sub> |  | 0.8 | 0.3 | 1.9 | 17.0 |
| Zuby Ejiofor (ATL) | 66% | 15.8<br><sub>-,-,15,17,15</sub> | 6.2<br><sub>-,-,3,11,10</sub> |  | 3.4<br><sub>-,-,5,3,5</sub> |  | 2.4<br><sub>-,-,2,2,5</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.5 | 0.2 | 1.0 | 12.1 |
| Corey Kispert (ATL) | 72% | 15.8<br><sub>-,5,18,8,16</sub> | 8.4<br><sub>-,0,14,9,7</sub> |  | 1.9<br><sub>-,0,1,0,2</sub> |  | 1.4<br><sub>-,1,0,1,1</sub> |  | 1.1<br><sub>-,0,4,1,1</sub> |  | 0.3 | 0.2 | 0.8 | 11.7 |
| Jalen Wilson (ATL) | 52% | 11.8<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 7.7 |
| RayJ Dennis (ATL) | 72% | 11.1<br><sub>-,-,8,-,-</sub> | 3.9<br><sub>-,-,4,-,-</sub> |  | 1.5<br><sub>-,-,2,-,-</sub> |  | 2.0<br><sub>-,-,2,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.8 | 7.4 |
| Dorian Finney-Smith (ATL) | 38% | 7.3<br><sub>-,3,-,-,-</sub> | 2.0<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |
| Michael Porter Jr. (BKN) | 98% | 34.8<br><sub>40,26,36,37,38</sub> | 22.7<br><sub>27,13,23,18,26</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>12,7,9,5,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,1,3,2,0</sub> |  | 3.1<br><sub>6,2,3,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.6 | 33.1 |
| Julius Randle (BKN) | 98% | 34.4<br><sub>44,25,37,36,31</sub> | 21.0<br><sub>24,15,20,21,22</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>9,8,5,11,3</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>4,3,6,2,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>0,3,4,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.7 | 33.4 |
| Nolan Traore (BKN) | 98% | 26.0<br><sub>24,26,30,24,27</sub> | 12.3<br><sub>15,9,16,17,16</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>1,2,2,3,4</sub> |  | 3.9<br><sub>3,2,6,4,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>1,0,4,5,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.5 | 2.8 | 18.6 |
| Mikel Brown Jr. (BKN) | 96% | 25.5<br><sub>28,23,-,27,20</sub> | 11.6<br><sub>17,10,-,13,18</sub> |  | 2.9<br><sub>5,0,-,2,2</sub> |  | 3.7<br><sub>5,4,-,3,4</sub> |  | 1.6<br><sub>4,0,-,1,3</sub> |  | 0.8 | 0.3 | 2.2 | 18.3 |
| Day'Ron Sharpe (BKN) | 100% | 23.8<br><sub>17,24,26,22,27</sub> | 9.2<br><sub>4,3,15,4,6</sub> | 8.5 · – | 8.5<br><sub>6,7,13,6,5</sub> | 8.5 | 3.0<br><sub>0,1,4,3,8</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 1.1 | 0.8 | 2.1 | 20.6 |
| Chaney Johnson (BKN) | 93% | 21.3<br><sub>29,19,31,28,9</sub> | 6.1<br><sub>15,6,2,4,0</sub> |  | 3.0<br><sub>3,2,2,3,2</sub> |  | 1.2<br><sub>2,0,0,2,1</sub> |  | 0.6<br><sub>3,0,0,1,0</sub> |  | 0.7 | 0.5 | 1.1 | 10.3 |
| Keon Ellis (BKN) | 96% | 21.0<br><sub>25,21,20,25,10</sub> | 5.6<br><sub>2,6,0,5,1</sub> |  | 2.1<br><sub>3,2,2,1,2</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 0.7<br><sub>0,2,0,1,0</sub> |  | 1.1 | 0.7 | 0.8 | 9.1 |
| Moritz Wagner (BKN) | 93% | 20.2<br><sub>22,23,21,20,20</sub> | 9.7<br><sub>15,16,14,6,6</sub> |  | 5.0<br><sub>4,8,6,1,1</sub> |  | 1.3<br><sub>3,1,0,2,0</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.3 | 1.2 | 16.1 |
| Danny Wolf (BKN) | 52% | 18.6<br><sub>-,12,-,-,19</sub> | 8.2<br><sub>-,9,-,-,12</sub> |  | 4.8<br><sub>-,6,-,-,5</sub> |  | 2.0<br><sub>-,2,-,-,3</sub> |  | 0.9<br><sub>-,3,-,-,2</sub> |  | 0.5 | 0.5 | 1.2 | 15.0 |
| Terance Mann (BKN) | 58% | 17.1<br><sub>-,12,15,-,16</sub> | 4.4<br><sub>-,2,0,-,0</sub> |  | 2.2<br><sub>-,0,1,-,2</sub> |  | 1.6<br><sub>-,2,1,-,2</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.8 | 8.2 |
| Josh Minott (BKN) | 52% | 12.7<br><sub>-,3,-,-,6</sub> | 6.1<br><sub>-,2,-,-,0</sub> |  | 2.4<br><sub>-,0,-,-,1</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.4 | 0.7 | 9.2 |
| Drake Powell (BKN) | 52% | 11.5<br><sub>-,6,-,-,-</sub> | 3.7<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,2,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.5 |

</details>

<details><summary>if Noah Clowney plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker (ATL) | 98% | 31.1<br><sub>31,29,31,32,33</sub> | 22.4<br><sub>25,12,34,26,28</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,2,4,4,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.5<br><sub>1,1,4,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>4,0,9,6,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.5 | 2.5 | 29.0 |
| Onyeka Okongwu (ATL) | 98% | 30.9<br><sub>33,28,33,31,33</sub> | 15.2<br><sub>29,6,13,14,22</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>12,10,10,16,10</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>2,1,3,4,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>4,0,2,2,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.0 | 1.5 | 26.4 |
| Dyson Daniels (ATL) | 98% | 30.7<br><sub>32,27,31,34,35</sub> | 11.6<br><sub>4,8,6,8,13</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>6,4,9,16,9</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>5,3,4,8,12</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.3 | 0.5 | 1.8 | 24.8 |
| Luguentz Dort (ATL) | 98% | 28.5<br><sub>22,29,31,31,32</sub> | 10.6<br><sub>6,11,14,6,25</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,3,2,3,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,0,0,3,4</sub> |  | 1.7<br><sub>1,1,4,2,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.4 | 0.9 | 16.2 |
| CJ McCollum (ATL) | 98% | 26.8<br><sub>31,24,32,25,23</sub> | 17.2<br><sub>5,14,13,15,4</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>3,2,9,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>8,2,12,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 2.3 | 24.7 |
| Aaron Wiggins (ATL) | 97% | 25.5<br><sub>24,23,24,29,29</sub> | 13.0<br><sub>20,10,7,15,19</sub> |  | 3.4<br><sub>7,2,3,4,4</sub> |  | 2.2<br><sub>3,1,2,2,3</sub> |  | 1.9<br><sub>4,2,1,3,3</sub> |  | 1.0 | 0.4 | 1.5 | 18.6 |
| Kingston Flemings (ATL) | 86% | 22.5<br><sub>16,25,-,23,25</sub> | 9.1<br><sub>2,12,-,14,11</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>1,2,-,3,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 5.1<br><sub>5,6,-,4,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.7<br><sub>0,1,-,2,1</sub> |  | 0.8 | 0.3 | 1.9 | 17.0 |
| Zuby Ejiofor (ATL) | 66% | 15.8<br><sub>-,-,15,17,15</sub> | 6.2<br><sub>-,-,3,11,10</sub> |  | 3.4<br><sub>-,-,5,3,5</sub> |  | 2.4<br><sub>-,-,2,2,5</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.5 | 0.2 | 1.0 | 12.1 |
| Corey Kispert (ATL) | 72% | 15.8<br><sub>-,5,18,8,16</sub> | 8.4<br><sub>-,0,14,9,7</sub> |  | 1.9<br><sub>-,0,1,0,2</sub> |  | 1.4<br><sub>-,1,0,1,1</sub> |  | 1.1<br><sub>-,0,4,1,1</sub> |  | 0.3 | 0.2 | 0.8 | 11.7 |
| Jalen Wilson (ATL) | 52% | 11.7<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 7.7 |
| RayJ Dennis (ATL) | 72% | 11.2<br><sub>-,-,8,-,-</sub> | 3.9<br><sub>-,-,4,-,-</sub> |  | 1.5<br><sub>-,-,2,-,-</sub> |  | 2.0<br><sub>-,-,2,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.8 | 7.4 |
| Dorian Finney-Smith (ATL) | 38% | 7.2<br><sub>-,3,-,-,-</sub> | 2.1<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |
| Michael Porter Jr. (BKN) | 98% | 35.0<br><sub>40,26,36,37,38</sub> | 22.7<br><sub>27,13,23,18,26</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>12,7,9,5,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>2,1,3,2,0</sub> |  | 3.0<br><sub>6,2,3,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.4 | 2.7 | 33.3 |
| Julius Randle (BKN) | 98% | 34.6<br><sub>44,25,37,36,31</sub> | 20.9<br><sub>24,15,20,21,22</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>9,8,5,11,3</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.9<br><sub>4,3,6,2,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>0,3,4,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.9 | 33.6 |
| Nolan Traore (BKN) | 98% | 26.4<br><sub>24,26,30,24,27</sub> | 12.7<br><sub>15,9,16,17,16</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>1,2,2,3,4</sub> |  | 3.9<br><sub>3,2,6,4,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>1,0,4,5,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 2.9 | 19.2 |
| Mikel Brown Jr. (BKN) | 96% | 25.7<br><sub>28,23,-,27,20</sub> | 11.7<br><sub>17,10,-,13,18</sub> |  | 3.0<br><sub>5,0,-,2,2</sub> |  | 3.8<br><sub>5,4,-,3,4</sub> |  | 1.6<br><sub>4,0,-,1,3</sub> |  | 0.8 | 0.3 | 2.2 | 18.4 |
| Noah Clowney (BKN) | 100% | 22.7<br><sub>24,22,24,20,17</sub> | 8.2<br><sub>3,3,8,2,7</sub> |  | 4.2<br><sub>4,8,3,6,1</sub> |  | 1.2<br><sub>1,1,0,2,1</sub> |  | 1.1<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.5 | 1.0 | 13.7 |
| Chaney Johnson (BKN) | 93% | 21.7<br><sub>29,19,31,28,9</sub> | 6.1<br><sub>15,6,2,4,0</sub> |  | 3.0<br><sub>3,2,2,3,2</sub> |  | 1.2<br><sub>2,0,0,2,1</sub> |  | 0.6<br><sub>3,0,0,1,0</sub> |  | 0.7 | 0.5 | 1.1 | 10.3 |
| Keon Ellis (BKN) | 96% | 21.4<br><sub>25,21,20,25,10</sub> | 5.7<br><sub>2,6,0,5,1</sub> |  | 2.2<br><sub>3,2,2,1,2</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 0.7<br><sub>0,2,0,1,0</sub> |  | 1.1 | 0.7 | 0.8 | 9.3 |
| Moritz Wagner (BKN) | 93% | 21.1<br><sub>22,23,21,20,20</sub> | 10.0<br><sub>15,16,14,6,6</sub> |  | 5.2<br><sub>4,8,6,1,1</sub> |  | 1.4<br><sub>3,1,0,2,0</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.7 | 0.3 | 1.3 | 16.7 |
| Danny Wolf (BKN) | 52% | 18.3<br><sub>-,12,-,-,19</sub> | 7.9<br><sub>-,9,-,-,12</sub> |  | 4.7<br><sub>-,6,-,-,5</sub> |  | 2.0<br><sub>-,2,-,-,3</sub> |  | 0.9<br><sub>-,3,-,-,2</sub> |  | 0.5 | 0.5 | 1.1 | 14.6 |
| Terance Mann (BKN) | 58% | 17.5<br><sub>-,12,15,-,16</sub> | 4.5<br><sub>-,2,0,-,0</sub> |  | 2.2<br><sub>-,0,1,-,2</sub> |  | 1.6<br><sub>-,2,1,-,2</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.8 | 8.3 |
| Josh Minott (BKN) | 52% | 12.7<br><sub>-,3,-,-,6</sub> | 6.0<br><sub>-,2,-,-,0</sub> |  | 2.4<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,0,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.4 | 0.7 | 9.2 |
| Drake Powell (BKN) | 52% | 12.6<br><sub>-,6,-,-,-</sub> | 4.1<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,2,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.7 | 6.1 |

</details>


### NYK @ CLE
Out: Jaylon Tyson (CLE), Josh Hart (NYK)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.3–107.5 | NYK 71% | 1.41 / 3.43 | CLE +7.5 | 222.5 | CLE +4.5 covers 40%; o224.5 46% |
| Expected (weighted by chance each plays) | 115.2–108.6 | NYK 68% | 1.47 / 3.13 | CLE +6.5 | 223.5 | CLE +4.5 covers 43%; o224.5 49% |
| if Sam Merrill plays | 115.9–108.2 | NYK 71% | 1.41 / 3.43 | CLE +7.5 | 223.5 | CLE +4.5 covers 41%; o224.5 49% |
| if Jarrett Allen plays | 114.9–108.6 | NYK 67% | 1.49 / 3.05 | CLE +6.5 | 223.5 | CLE +4.5 covers 44%; o224.5 48% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sam Merrill (CLE) | Day-To-Day | 70% | 22.4 | 7.8 | 2.4 | 1.4 | 1.4 | 0.6 | 0.2 | 0.6 | 11.7 | full tables below |
| Jarrett Allen (CLE) | Day-To-Day | 70% | 26.2 | 11.3 | 7.4 | 1.3 | 0.1 | 0.8 | 1.2 | 1.2 | 19.9 | full tables below |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 37.0<br><sub>36,35,35,34,28</sub> | 25.5<br><sub>23,38,24,19,33</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>1,1,5,2,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 6.5<br><sub>7,7,6,6,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>0,6,3,4,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 2.6 | 35.3 |
| OG Anunoby | 98% | 35.6<br><sub>36,31,34,38,24</sub> | 18.3<br><sub>13,23,9,18,18</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>7,6,4,4,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,1,3,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>1,2,1,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.8 | 1.6 | 26.4 |
| Karl-Anthony Towns | 98% | 33.7<br><sub>33,28,35,35,25</sub> | 19.2<br><sub>27,19,22,11,17</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 13.2<br><sub>20,13,12,16,12</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,5,3,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,3,3,1,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.7 | 3.0 | 36.1 |
| Mikal Bridges | 98% | 28.6<br><sub>32,13,30,16,22</sub> | 9.6<br><sub>12,3,12,6,7</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>3,0,5,2,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>4,0,2,0,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>4,1,2,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 1.0 | 15.1 |
| Landry Shamet | 98% | 27.5<br><sub>28,32,16,30,25</sub> | 10.0<br><sub>13,14,0,22,7</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>2,1,0,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5<br><sub>3,5,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,4,0,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 0.8 | 13.5 |
| Miles McBride | 98% | 20.6<br><sub>17,14,24,17,11</sub> | 7.8<br><sub>5,3,10,6,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>1,5,3,1,1</sub> |  | 1.6<br><sub>1,0,1,2,1</sub> |  | 1.4<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.5 | 11.2 |
| Jordan Clarkson | 88% | 15.1<br><sub>-,17,9,11,15</sub> | 7.2<br><sub>-,18,4,7,10</sub> |  | 1.9<br><sub>-,3,3,0,1</sub> |  | 1.0<br><sub>-,1,0,0,1</sub> |  | 0.6<br><sub>-,2,0,1,2</sub> |  | 0.4 | 0.1 | 0.8 | 10.2 |
| Jose Alvarado | 97% | 14.7<br><sub>-,-,-,9,9</sub> | 5.1<br><sub>-,-,-,0,0</sub> |  | 1.8<br><sub>-,-,-,0,0</sub> |  | 2.2<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.8 | 0.1 | 0.8 | 9.1 |
| Tyler Kolek | 86% | 14.6<br><sub>11,18,13,5,11</sub> | 4.4<br><sub>2,9,2,2,0</sub> |  | 1.8<br><sub>1,2,1,1,0</sub> |  | 3.6<br><sub>3,9,4,1,5</sub> |  | 0.5<br><sub>0,3,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 9.8 |
| Andre Drummond | 98% | 14.4<br><sub>14,15,12,13,12</sub> | 5.0<br><sub>10,4,3,4,6</sub> |  | 6.5<br><sub>8,11,6,9,9</sub> |  | 1.0<br><sub>1,1,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 12.5 |
| Mohamed Diawara | 52% | 13.2<br><sub>1,-,-,6,21</sub> | 4.4<br><sub>0,-,-,0,8</sub> |  | 2.3<br><sub>0,-,-,1,6</sub> |  | 1.2<br><sub>0,-,-,0,4</sub> |  | 0.5<br><sub>0,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.6 | 7.9 |
| Dalton Knecht | 52% | 12.7<br><sub>-,-,-,-,16</sub> | 5.6<br><sub>-,-,-,-,10</sub> |  | 2.5<br><sub>-,-,-,-,7</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,2</sub> |  | 0.3 | 0.2 | 0.4 | 8.9 |
| James Wiseman | 52% | 8.8<br><sub>1,-,-,-,10</sub> | 2.9<br><sub>0,-,-,-,8</sub> |  | 2.8<br><sub>1,-,-,-,8</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.3 | 0.6 | 6.1 |
| Jaden Akins | 38% | 8.6<br><sub>2,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Pacome Dadiet | 48% | 8.3<br><sub>1,-,-,-,9</sub> | 3.1<br><sub>0,-,-,-,4</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.5<br><sub>36,26,33,35,30</sub> | 17.7<br><sub>24,13,14,19,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>5,6,4,9,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>4,7,6,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 3.6 | 28.8 |
| Donovan Mitchell | 98% | 36.3<br><sub>33,24,36,33,33</sub> | 23.0<br><sub>22,15,17,27,23</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>3,4,5,3,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.1<br><sub>3,3,11,6,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>1,2,4,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 3.0 | 33.0 |
| Evan Mobley | 98% | 35.2<br><sub>33,25,33,33,32</sub> | 16.7<br><sub>11,27,16,16,22</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>4,5,7,10,6</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>7,3,4,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>0,3,1,1,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 1.7 | 1.9 | 28.3 |
| Peyton Watson | 98% | 31.3<br><sub>22,22,-,-,28</sub> | 12.8<br><sub>4,5,-,-,13</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>4,2,-,-,9</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>3,6,-,-,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4<br><sub>0,1,-,-,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 1.3 | 1.7 | 19.9 |
| Meleek Thomas | 88% | 26.8<br><sub>-,23,26,18,27</sub> | 11.1<br><sub>-,13,17,9,12</sub> |  | 2.9<br><sub>-,1,5,1,1</sub> |  | 1.5<br><sub>-,2,1,0,3</sub> |  | 1.8<br><sub>-,3,3,3,2</sub> |  | 0.8 | 0.3 | 1.4 | 15.5 |
| Mario Hezonja | 98% | 25.2<br><sub>17,20,27,23,27</sub> | 9.8<br><sub>10,8,12,12,15</sub> |  | 6.3<br><sub>6,11,8,8,10</sub> |  | 1.8<br><sub>2,4,3,1,1</sub> |  | 1.4<br><sub>2,1,3,2,2</sub> |  | 0.7 | 0.3 | 1.0 | 18.0 |
| Tyrese Proctor | 88% | 22.0<br><sub>20,18,19,22,19</sub> | 7.7<br><sub>7,9,10,11,3</sub> |  | 3.1<br><sub>6,4,4,1,6</sub> |  | 2.4<br><sub>2,5,2,0,3</sub> |  | 1.2<br><sub>1,3,2,2,0</sub> |  | 0.8 | 0.1 | 1.0 | 13.2 |
| Thomas Bryant | 66% | 16.2<br><sub>-,11,5,13,16</sub> | 8.0<br><sub>-,11,4,8,13</sub> |  | 3.9<br><sub>-,2,0,0,6</sub> |  | 0.6<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,3,0,1,1</sub> |  | 0.4 | 0.5 | 0.8 | 12.5 |
| Craig Porter Jr. | 86% | 13.3<br><sub>4,16,8,14,3</sub> | 2.9<br><sub>0,2,0,0,0</sub> |  | 2.3<br><sub>1,2,4,1,0</sub> |  | 1.8<br><sub>0,4,1,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.4 | 0.7 | 7.0 |
| Tristan Enaruna | 58% | 12.4<br><sub>-,6,-,16,8</sub> | 4.0<br><sub>-,2,-,4,1</sub> |  | 1.9<br><sub>-,1,-,4,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 6.7 |
| Ernest Udeh Jr. | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Norchad Omier | 64% | 7.8<br><sub>-,-,-,-,3</sub> | 2.2<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.8 |

</details>

<details><summary>if Jarrett Allen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 98% | 35.5<br><sub>36,26,33,35,30</sub> | 16.9<br><sub>24,13,14,19,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>5,6,4,9,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>4,7,6,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 3.6 | 27.6 |
| Donovan Mitchell (CLE) | 98% | 35.3<br><sub>33,24,36,33,33</sub> | 21.6<br><sub>22,15,17,27,23</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>3,4,5,3,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.8<br><sub>3,3,11,6,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>1,2,4,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.4 | 2.9 | 31.2 |
| Evan Mobley (CLE) | 98% | 33.9<br><sub>33,25,33,33,32</sub> | 16.1<br><sub>11,27,16,16,22</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>4,5,7,10,6</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>7,3,4,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,3,1,1,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 1.6 | 1.9 | 27.7 |
| Peyton Watson (CLE) | 98% | 29.6<br><sub>22,22,-,-,28</sub> | 12.0<br><sub>4,5,-,-,13</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>4,2,-,-,9</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,6,-,-,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>0,1,-,-,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 1.2 | 1.6 | 18.8 |
| Jarrett Allen (CLE) | 100% | 26.2<br><sub>30,24,28,7,-</sub> | 11.3<br><sub>14,25,14,0,-</sub> | 11.5 · – | 7.4<br><sub>8,11,6,1,-</sub> | 7.5 | 1.3<br><sub>1,4,1,0,-</sub> |  | 0.1<br><sub>1,0,0,0,-</sub> |  | 0.8 | 1.2 | 1.2 | 19.9 |
| Meleek Thomas (CLE) | 88% | 23.5<br><sub>-,23,26,18,27</sub> | 9.9<br><sub>-,13,17,9,12</sub> |  | 2.5<br><sub>-,1,5,1,1</sub> |  | 1.3<br><sub>-,2,1,0,3</sub> |  | 1.5<br><sub>-,3,3,3,2</sub> |  | 0.8 | 0.2 | 1.3 | 13.7 |
| Mario Hezonja (CLE) | 98% | 22.5<br><sub>17,20,27,23,27</sub> | 8.8<br><sub>10,8,12,12,15</sub> |  | 5.7<br><sub>6,11,8,8,10</sub> |  | 1.7<br><sub>2,4,3,1,1</sub> |  | 1.2<br><sub>2,1,3,2,2</sub> |  | 0.6 | 0.2 | 1.0 | 16.2 |
| Tyrese Proctor (CLE) | 88% | 19.0<br><sub>20,18,19,22,19</sub> | 6.7<br><sub>7,9,10,11,3</sub> |  | 2.7<br><sub>6,4,4,1,6</sub> |  | 2.1<br><sub>2,5,2,0,3</sub> |  | 0.9<br><sub>1,3,2,2,0</sub> |  | 0.7 | 0.1 | 0.9 | 11.5 |
| Thomas Bryant (CLE) | 66% | 13.0<br><sub>-,11,5,13,16</sub> | 6.3<br><sub>-,11,4,8,13</sub> |  | 3.2<br><sub>-,2,0,0,6</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 0.7<br><sub>-,3,0,1,1</sub> |  | 0.3 | 0.4 | 0.6 | 10.0 |
| Craig Porter Jr. (CLE) | 86% | 11.2<br><sub>4,16,8,14,3</sub> | 2.4<br><sub>0,2,0,0,0</sub> |  | 1.9<br><sub>1,2,4,1,0</sub> |  | 1.6<br><sub>0,4,1,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.0 |
| Tristan Enaruna (CLE) | 58% | 10.8<br><sub>-,6,-,16,8</sub> | 3.7<br><sub>-,2,-,4,1</sub> |  | 1.7<br><sub>-,1,-,4,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.0 |
| Ernest Udeh Jr. (CLE) | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Norchad Omier (CLE) | 64% | 6.3<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Jalen Brunson (NYK) | 98% | 37.0<br><sub>36,35,35,34,28</sub> | 25.4<br><sub>23,38,24,19,33</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>1,1,5,2,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 6.5<br><sub>7,7,6,6,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>0,6,3,4,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 2.6 | 35.2 |
| OG Anunoby (NYK) | 98% | 35.6<br><sub>36,31,34,38,24</sub> | 18.2<br><sub>13,23,9,18,18</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>7,6,4,4,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,1,3,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>1,2,1,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.8 | 1.6 | 26.3 |
| Karl-Anthony Towns (NYK) | 98% | 33.7<br><sub>33,28,35,35,25</sub> | 19.2<br><sub>27,19,22,11,17</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 13.3<br><sub>20,13,12,16,12</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,5,3,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,3,3,1,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.7 | 3.0 | 36.1 |
| Mikal Bridges (NYK) | 98% | 28.6<br><sub>32,13,30,16,22</sub> | 9.6<br><sub>12,3,12,6,7</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>3,0,5,2,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>4,0,2,0,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>4,1,2,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 0.9 | 15.2 |
| Landry Shamet (NYK) | 98% | 27.4<br><sub>28,32,16,30,25</sub> | 9.9<br><sub>13,14,0,22,7</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,1,0,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5<br><sub>3,5,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,4,0,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 0.8 | 13.5 |
| Miles McBride (NYK) | 98% | 20.5<br><sub>17,14,24,17,11</sub> | 7.8<br><sub>5,3,10,6,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>1,5,3,1,1</sub> |  | 1.6<br><sub>1,0,1,2,1</sub> |  | 1.4<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.6 | 11.2 |
| Jordan Clarkson (NYK) | 88% | 15.2<br><sub>-,17,9,11,15</sub> | 7.2<br><sub>-,18,4,7,10</sub> |  | 2.0<br><sub>-,3,3,0,1</sub> |  | 1.0<br><sub>-,1,0,0,1</sub> |  | 0.6<br><sub>-,2,0,1,2</sub> |  | 0.5 | 0.1 | 0.8 | 10.2 |
| Jose Alvarado (NYK) | 97% | 14.7<br><sub>-,-,-,9,9</sub> | 5.1<br><sub>-,-,-,0,0</sub> |  | 1.8<br><sub>-,-,-,0,0</sub> |  | 2.2<br><sub>-,-,-,0,2</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.8 | 0.1 | 0.8 | 9.2 |
| Tyler Kolek (NYK) | 86% | 14.6<br><sub>11,18,13,5,11</sub> | 4.4<br><sub>2,9,2,2,0</sub> |  | 1.8<br><sub>1,2,1,1,0</sub> |  | 3.6<br><sub>3,9,4,1,5</sub> |  | 0.5<br><sub>0,3,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 9.7 |
| Andre Drummond (NYK) | 98% | 14.3<br><sub>14,15,12,13,12</sub> | 5.0<br><sub>10,4,3,4,6</sub> |  | 6.4<br><sub>8,11,6,9,9</sub> |  | 1.0<br><sub>1,1,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 12.4 |
| Mohamed Diawara (NYK) | 52% | 13.2<br><sub>1,-,-,6,21</sub> | 4.3<br><sub>0,-,-,0,8</sub> |  | 2.3<br><sub>0,-,-,1,6</sub> |  | 1.2<br><sub>0,-,-,0,4</sub> |  | 0.5<br><sub>0,-,-,0,1</sub> |  | 0.4 | 0.1 | 0.6 | 7.8 |
| Dalton Knecht (NYK) | 52% | 12.7<br><sub>-,-,-,-,16</sub> | 5.6<br><sub>-,-,-,-,10</sub> |  | 2.5<br><sub>-,-,-,-,7</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,2</sub> |  | 0.3 | 0.2 | 0.4 | 8.9 |
| James Wiseman (NYK) | 52% | 8.8<br><sub>1,-,-,-,10</sub> | 2.9<br><sub>0,-,-,-,8</sub> |  | 2.8<br><sub>1,-,-,-,8</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.4 | 0.6 | 6.2 |
| Jaden Akins (NYK) | 38% | 8.7<br><sub>2,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Pacome Dadiet (NYK) | 48% | 8.2<br><sub>1,-,-,-,9</sub> | 3.1<br><sub>0,-,-,-,4</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |

</details>

<details><summary>if Sam Merrill plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 98% | 35.2<br><sub>36,26,33,35,30</sub> | 17.0<br><sub>24,13,14,19,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>5,6,4,9,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,7,6,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 3.5 | 27.5 |
| Donovan Mitchell (CLE) | 98% | 34.9<br><sub>33,24,36,33,33</sub> | 22.0<br><sub>22,15,17,27,23</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>3,4,5,3,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.6<br><sub>3,3,11,6,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>1,2,4,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 2.8 | 31.4 |
| Evan Mobley (CLE) | 98% | 33.9<br><sub>33,25,33,33,32</sub> | 16.5<br><sub>11,27,16,16,22</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.9<br><sub>4,5,7,10,6</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>7,3,4,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,3,1,1,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 1.7 | 1.8 | 27.8 |
| Peyton Watson (CLE) | 98% | 29.4<br><sub>22,22,-,-,28</sub> | 12.1<br><sub>4,5,-,-,13</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>4,2,-,-,9</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,6,-,-,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>0,1,-,-,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 1.2 | 1.6 | 18.7 |
| Meleek Thomas (CLE) | 88% | 23.4<br><sub>-,23,26,18,27</sub> | 10.1<br><sub>-,13,17,9,12</sub> |  | 2.5<br><sub>-,1,5,1,1</sub> |  | 1.3<br><sub>-,2,1,0,3</sub> |  | 1.5<br><sub>-,3,3,3,2</sub> |  | 0.8 | 0.2 | 1.3 | 13.9 |
| Mario Hezonja (CLE) | 98% | 22.8<br><sub>17,20,27,23,27</sub> | 9.2<br><sub>10,8,12,12,15</sub> |  | 5.8<br><sub>6,11,8,8,10</sub> |  | 1.7<br><sub>2,4,3,1,1</sub> |  | 1.2<br><sub>2,1,3,2,2</sub> |  | 0.6 | 0.3 | 1.0 | 16.7 |
| Sam Merrill (CLE) | 100% | 22.4<br><sub>27,19,26,27,13</sub> | 7.8<br><sub>16,6,8,10,0</sub> |  | 2.4<br><sub>2,4,3,7,3</sub> |  | 1.4<br><sub>3,3,2,1,0</sub> |  | 1.4<br><sub>4,1,2,2,0</sub> |  | 0.6 | 0.2 | 0.6 | 11.7 |
| Tyrese Proctor (CLE) | 88% | 18.3<br><sub>20,18,19,22,19</sub> | 6.5<br><sub>7,9,10,11,3</sub> |  | 2.6<br><sub>6,4,4,1,6</sub> |  | 1.9<br><sub>2,5,2,0,3</sub> |  | 0.9<br><sub>1,3,2,2,0</sub> |  | 0.7 | 0.1 | 0.9 | 11.1 |
| Thomas Bryant (CLE) | 66% | 14.3<br><sub>-,11,5,13,16</sub> | 7.0<br><sub>-,11,4,8,13</sub> |  | 3.6<br><sub>-,2,0,0,6</sub> |  | 0.6<br><sub>-,0,0,0,0</sub> |  | 0.8<br><sub>-,3,0,1,1</sub> |  | 0.4 | 0.4 | 0.7 | 11.1 |
| Tristan Enaruna (CLE) | 58% | 11.2<br><sub>-,6,-,16,8</sub> | 3.9<br><sub>-,2,-,4,1</sub> |  | 1.8<br><sub>-,1,-,4,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Craig Porter Jr. (CLE) | 86% | 11.0<br><sub>4,16,8,14,3</sub> | 2.5<br><sub>0,2,0,0,0</sub> |  | 1.9<br><sub>1,2,4,1,0</sub> |  | 1.6<br><sub>0,4,1,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.0 |
| Ernest Udeh Jr. (CLE) | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Norchad Omier (CLE) | 64% | 6.2<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Jalen Brunson (NYK) | 98% | 37.0<br><sub>36,35,35,34,28</sub> | 25.6<br><sub>23,38,24,19,33</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>1,1,5,2,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 6.5<br><sub>7,7,6,6,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>0,6,3,4,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 2.6 | 35.4 |
| OG Anunoby (NYK) | 98% | 35.6<br><sub>36,31,34,38,24</sub> | 18.3<br><sub>13,23,9,18,18</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>7,6,4,4,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>2,1,3,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>1,2,1,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.8 | 1.6 | 26.4 |
| Karl-Anthony Towns (NYK) | 98% | 33.8<br><sub>33,28,35,35,25</sub> | 19.3<br><sub>27,19,22,11,17</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 13.2<br><sub>20,13,12,16,12</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,5,3,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,3,3,1,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.7 | 3.0 | 36.2 |
| Mikal Bridges (NYK) | 98% | 28.6<br><sub>32,13,30,16,22</sub> | 9.6<br><sub>12,3,12,6,7</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>3,0,5,2,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>4,0,2,0,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>4,1,2,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 1.0 | 15.2 |
| Landry Shamet (NYK) | 98% | 27.4<br><sub>28,32,16,30,25</sub> | 10.0<br><sub>13,14,0,22,7</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>2,1,0,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5<br><sub>3,5,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,4,0,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 0.8 | 13.6 |
| Miles McBride (NYK) | 98% | 20.5<br><sub>17,14,24,17,11</sub> | 7.8<br><sub>5,3,10,6,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>1,5,3,1,1</sub> |  | 1.6<br><sub>1,0,1,2,1</sub> |  | 1.4<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.5 | 11.2 |
| Jordan Clarkson (NYK) | 88% | 15.1<br><sub>-,17,9,11,15</sub> | 7.2<br><sub>-,18,4,7,10</sub> |  | 1.9<br><sub>-,3,3,0,1</sub> |  | 1.1<br><sub>-,1,0,0,1</sub> |  | 0.6<br><sub>-,2,0,1,2</sub> |  | 0.4 | 0.1 | 0.9 | 10.2 |
| Jose Alvarado (NYK) | 97% | 14.6<br><sub>-,-,-,9,9</sub> | 5.1<br><sub>-,-,-,0,0</sub> |  | 1.8<br><sub>-,-,-,0,0</sub> |  | 2.2<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.8 | 0.1 | 0.8 | 9.1 |
| Tyler Kolek (NYK) | 86% | 14.6<br><sub>11,18,13,5,11</sub> | 4.4<br><sub>2,9,2,2,0</sub> |  | 1.8<br><sub>1,2,1,1,0</sub> |  | 3.6<br><sub>3,9,4,1,5</sub> |  | 0.5<br><sub>0,3,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 9.8 |
| Andre Drummond (NYK) | 98% | 14.4<br><sub>14,15,12,13,12</sub> | 5.0<br><sub>10,4,3,4,6</sub> |  | 6.4<br><sub>8,11,6,9,9</sub> |  | 1.0<br><sub>1,1,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 12.5 |
| Mohamed Diawara (NYK) | 52% | 13.3<br><sub>1,-,-,6,21</sub> | 4.5<br><sub>0,-,-,0,8</sub> |  | 2.3<br><sub>0,-,-,1,6</sub> |  | 1.2<br><sub>0,-,-,0,4</sub> |  | 0.5<br><sub>0,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.6 | 8.0 |
| Dalton Knecht (NYK) | 52% | 12.6<br><sub>-,-,-,-,16</sub> | 5.6<br><sub>-,-,-,-,10</sub> |  | 2.5<br><sub>-,-,-,-,7</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,2</sub> |  | 0.3 | 0.2 | 0.4 | 8.8 |
| Tyler Nickel (NYK) | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| James Wiseman (NYK) | 52% | 8.7<br><sub>1,-,-,-,10</sub> | 2.9<br><sub>0,-,-,-,8</sub> |  | 2.8<br><sub>1,-,-,-,8</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.4 | 0.6 | 6.1 |
| Jaden Akins (NYK) | 38% | 8.5<br><sub>2,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |
| Pacome Dadiet (NYK) | 48% | 8.2<br><sub>1,-,-,-,9</sub> | 3.1<br><sub>0,-,-,-,4</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |

</details>


### WAS @ OKC
Out: Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.0–119.2 | WAS 28% | 3.58 / 1.39 | OKC -8.5 | 229.5 | OKC -12.5 covers 38%; o222.5 66% |
| Expected (weighted by chance each plays) | 110.3–118.6 | WAS 28% | 3.62 / 1.38 | OKC -8.5 | 228.5 | OKC -12.5 covers 38%; o222.5 64% |
| if Anthony Davis plays | 109.7–118.2 | WAS 27% | 3.64 / 1.38 | OKC -8.5 | 227.5 | OKC -12.5 covers 39%; o222.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Davis (WAS) | Day-To-Day | 70% | 32.9 | 20.7 | 11.0 | 2.7 | 0.8 | 1.1 | 1.5 | 2.5 | 34.4 | full tables below |
| Jaylin Williams (OKC) | Day-To-Day | 70% | 17.2 | 5.5 | 4.8 | 1.9 | 0.8 | 0.5 | 0.4 | 0.7 | 12.2 | small |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 33.9<br><sub>34,38,34,34,37</sub> | 18.9<br><sub>14,21,15,18,23</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,7,3,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 9.3<br><sub>8,9,9,6,10</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>1,1,2,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 3.6 | 31.5 |
| Kyshawn George | 98% | 33.4<br><sub>38,32,37,35,39</sub> | 18.5<br><sub>8,12,22,25,33</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>2,3,4,4,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.9<br><sub>11,3,5,7,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>0,4,4,3,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 1.0 | 2.7 | 28.9 |
| AJ Dybantsa | 96% | 32.7<br><sub>27,30,33,32,36</sub> | 14.8<br><sub>19,17,21,9,11</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>2,8,5,6,9</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>2,1,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>1,1,1,0,1</sub> |  | 1.1 | 0.3 | 2.0 | 23.2 |
| Alex Sarr | 98% | 27.1<br><sub>26,29,-,23,30</sub> | 12.8<br><sub>18,3,-,11,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>4,8,-,9,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>2,0,-,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1<br><sub>2,1,-,0,1</sub> |  | 0.8 | 1.5 | 1.7 | 22.3 |
| Bilal Coulibaly | 98% | 26.8<br><sub>27,22,33,23,24</sub> | 10.4<br><sub>17,1,7,6,9</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>2,5,1,2,5</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.8<br><sub>0,1,2,2,0</sub> |  | 0.9<br><sub>1,0,0,0,1</sub> |  | 1.0 | 0.9 | 1.4 | 16.4 |
| Tre Johnson | 88% | 23.5<br><sub>-,13,22,14,27</sub> | 9.4<br><sub>-,4,4,3,23</sub> |  | 2.7<br><sub>-,2,3,2,1</sub> |  | 1.2<br><sub>-,0,0,0,1</sub> |  | 1.3<br><sub>-,0,0,1,5</sub> |  | 0.8 | 0.2 | 1.3 | 13.2 |
| Bub Carrington | 98% | 21.0<br><sub>20,20,19,19,15</sub> | 7.5<br><sub>3,9,3,0,5</sub> |  | 2.5<br><sub>1,4,4,1,1</sub> |  | 2.8<br><sub>3,2,4,2,1</sub> |  | 1.1<br><sub>0,3,1,0,1</sub> |  | 0.5 | 0.2 | 1.5 | 12.8 |
| Deandre Ayton | 98% | 19.4<br><sub>12,17,24,11,23</sub> | 6.5<br><sub>10,3,4,5,8</sub> |  | 5.9<br><sub>3,3,6,4,11</sub> |  | 0.9<br><sub>0,1,2,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 1.1 | 13.3 |
| Khris Middleton | 52% | 14.5<br><sub>23,5,-,-,-</sub> | 5.3<br><sub>4,0,-,-,-</sub> |  | 2.3<br><sub>3,0,-,-,-</sub> |  | 1.0<br><sub>2,0,-,-,-</sub> |  | 0.5<br><sub>1,0,-,-,-</sub> |  | 0.4 | 0.1 | 1.1 | 8.6 |
| Will Riley | 88% | 13.2<br><sub>-,1,4,13,9</sub> | 5.6<br><sub>-,0,0,0,7</sub> |  | 1.7<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,0,1,0,0</sub> |  | 0.5<br><sub>-,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 8.2 |
| Anthony Gill | 26% | 11.5<br><sub>-,-,-,-,-</sub> | 4.2<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.0 |
| Felix Okpara | 52% | 7.8<br><sub>-,-,-,3,-</sub> | 3.1<br><sub>-,-,-,0,-</sub> |  | 1.9<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.4 |
| Tre Mann | 48% | 7.6<br><sub>-,1,-,3,-</sub> | 3.2<br><sub>-,0,-,2,-</sub> |  | 1.0<br><sub>-,0,-,0,-</sub> |  | 0.9<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.1 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 32.9<br><sub>28,31,39,35,30</sub> | 32.4<br><sub>21,26,43,42,28</sub> | 32.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>6,4,3,4,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>2,3,8,8,4</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,3,4,5,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6 | 0.8 | 2.6 | 43.4 |
| Ajay Mitchell | 98% | 29.2<br><sub>28,26,35,32,30</sub> | 18.8<br><sub>29,6,20,23,35</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>4,3,5,7,1</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 4.4<br><sub>3,5,1,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>2,0,0,1,4</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.8 | 27.2 |
| Jared McCain | 98% | 26.8<br><sub>29,28,27,25,29</sub> | 14.7<br><sub>10,10,7,9,21</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>4,4,9,1,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>4,2,2,0,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.1 | 1.4 | 19.9 |
| Isaiah Hartenstein | 98% | 26.3<br><sub>26,25,28,26,26</sub> | 10.2<br><sub>10,10,5,3,2</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 10.7<br><sub>14,7,14,12,6</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>3,0,4,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.9 | 1.6 | 24.5 |
| Kenrich Williams | 97% | 23.1<br><sub>17,21,31,29,19</sub> | 9.2<br><sub>7,11,12,13,4</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 5.5<br><sub>3,7,3,4,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,3,1,2,3</sub> |  | 1.2<br><sub>1,3,2,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 0.9 | 16.8 |
| Aday Mara | 98% | 22.7<br><sub>21,28,20,25,18</sub> | 8.6<br><sub>6,7,10,9,9</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>3,9,9,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>1,3,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.7 | 1.5 | 16.8 |
| Bennett Stirtz | 98% | 22.2<br><sub>28,26,12,22,24</sub> | 7.6<br><sub>8,11,9,16,12</sub> |  | 1.8<br><sub>0,1,2,1,1</sub> |  | 1.6<br><sub>3,3,0,1,2</sub> |  | 1.1<br><sub>1,3,3,4,2</sub> |  | 0.7 | 0.2 | 0.8 | 11.0 |
| Alex Caruso | 98% | 21.7<br><sub>-,-,-,20,20</sub> | 9.3<br><sub>-,-,-,7,5</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>-,-,-,4,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.4 | 0.9 | 15.9 |
| Micah Peavy | 80% | 18.8<br><sub>5,14,16,26,18</sub> | 5.1<br><sub>0,2,8,2,7</sub> |  | 3.7<br><sub>0,1,5,9,4</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>0,0,2,0,1</sub> |  | 0.6 | 0.2 | 0.9 | 9.9 |
| Josh Dix | 67% | 16.8<br><sub>24,9,12,-,15</sub> | 5.6<br><sub>2,7,0,-,5</sub> |  | 1.8<br><sub>2,0,1,-,2</sub> |  | 0.6<br><sub>0,0,0,-,1</sub> |  | 0.5<br><sub>0,1,0,-,1</sub> |  | 0.5 | 0.2 | 0.6 | 8.1 |
| Brooks Barnhizer | 63% | 10.1<br><sub>14,6,-,-,5</sub> | 2.6<br><sub>3,5,-,-,0</sub> |  | 2.3<br><sub>2,2,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.6 |
| Dalen Terry | 63% | 8.4<br><sub>-,-,-,-,5</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.4 | 5.5 |
| Nikola Topic | 16% | 8.0 | 2.6 |  | 1.0 |  | 1.8 |  | 0.1 |  | 0.4 | 0.1 | 0.6 | 5.4 |

</details>

<details><summary>if Anthony Davis plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 32.9<br><sub>28,31,39,35,30</sub> | 32.2<br><sub>21,26,43,42,28</sub> | 32.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>6,4,3,4,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.8<br><sub>2,3,8,8,4</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,3,4,5,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.5 | 0.8 | 2.6 | 43.2 |
| Ajay Mitchell (OKC) | 98% | 29.3<br><sub>28,26,35,32,30</sub> | 18.7<br><sub>29,6,20,23,35</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>4,3,5,7,1</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 4.4<br><sub>3,5,1,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>2,0,0,1,4</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.8 | 27.2 |
| Jared McCain (OKC) | 98% | 26.8<br><sub>29,28,27,25,29</sub> | 14.7<br><sub>10,10,7,9,21</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>4,4,9,1,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>4,2,2,0,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.1 | 1.4 | 19.8 |
| Isaiah Hartenstein (OKC) | 98% | 26.3<br><sub>26,25,28,26,26</sub> | 10.1<br><sub>10,10,5,3,2</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 10.7<br><sub>14,7,14,12,6</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>3,0,4,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.9 | 1.6 | 24.4 |
| Kenrich Williams (OKC) | 97% | 23.0<br><sub>17,21,31,29,19</sub> | 9.1<br><sub>7,11,12,13,4</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 5.5<br><sub>3,7,3,4,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,3,1,2,3</sub> |  | 1.2<br><sub>1,3,2,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 0.9 | 16.6 |
| Aday Mara (OKC) | 98% | 22.7<br><sub>21,28,20,25,18</sub> | 8.5<br><sub>6,7,10,9,9</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>3,9,9,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>1,3,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.7 | 1.5 | 16.6 |
| Bennett Stirtz (OKC) | 98% | 22.2<br><sub>28,26,12,22,24</sub> | 7.5<br><sub>8,11,9,16,12</sub> |  | 1.8<br><sub>0,1,2,1,1</sub> |  | 1.6<br><sub>3,3,0,1,2</sub> |  | 1.1<br><sub>1,3,3,4,2</sub> |  | 0.7 | 0.2 | 0.8 | 10.9 |
| Alex Caruso (OKC) | 98% | 21.8<br><sub>-,-,-,20,20</sub> | 9.3<br><sub>-,-,-,7,5</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>-,-,-,4,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.4 | 0.9 | 15.8 |
| Micah Peavy (OKC) | 80% | 18.8<br><sub>5,14,16,26,18</sub> | 5.2<br><sub>0,2,8,2,7</sub> |  | 3.8<br><sub>0,1,5,9,4</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>0,0,2,0,1</sub> |  | 0.6 | 0.2 | 0.9 | 9.9 |
| Josh Dix (OKC) | 67% | 16.8<br><sub>24,9,12,-,15</sub> | 5.6<br><sub>2,7,0,-,5</sub> |  | 1.8<br><sub>2,0,1,-,2</sub> |  | 0.6<br><sub>0,0,0,-,1</sub> |  | 0.5<br><sub>0,1,0,-,1</sub> |  | 0.5 | 0.2 | 0.6 | 8.1 |
| Brooks Barnhizer (OKC) | 63% | 10.0<br><sub>14,6,-,-,5</sub> | 2.6<br><sub>3,5,-,-,0</sub> |  | 2.3<br><sub>2,2,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.6 |
| Dalen Terry (OKC) | 63% | 8.4<br><sub>-,-,-,-,5</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.4 | 5.4 |
| Nikola Topic (OKC) | 16% | 8.0 | 2.6 |  | 1.0 |  | 1.8 |  | 0.1 |  | 0.4 | 0.1 | 0.6 | 5.4 |
| Trae Young (WAS) | 98% | 33.3<br><sub>34,38,34,34,37</sub> | 16.8<br><sub>14,21,15,18,23</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,7,3,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 8.7<br><sub>8,9,9,6,10</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,1,2,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 3.5 | 28.8 |
| Anthony Davis (WAS) | 100% | 32.9<br><sub>34,34,34,30,-</sub> | 20.7<br><sub>18,25,27,26,-</sub> | 20.5 · – | 11.0<br><sub>5,13,9,10,-</sub> | 9.5 | 2.7<br><sub>3,1,1,3,-</sub> | 2.5 | 0.8<br><sub>2,0,1,0,-</sub> |  | 1.1 | 1.5 | 2.5 | 34.4 |
| Kyshawn George (WAS) | 98% | 31.4<br><sub>38,32,37,35,39</sub> | 15.7<br><sub>8,12,22,25,33</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>2,3,4,4,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.2<br><sub>11,3,5,7,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>0,4,4,3,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.9 | 2.5 | 24.8 |
| AJ Dybantsa (WAS) | 96% | 30.7<br><sub>27,30,33,32,36</sub> | 13.1<br><sub>19,17,21,9,11</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>2,8,5,6,9</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>2,1,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9<br><sub>1,1,1,0,1</sub> |  | 1.0 | 0.2 | 1.8 | 20.8 |
| Alex Sarr (WAS) | 98% | 24.9<br><sub>26,29,-,23,30</sub> | 11.3<br><sub>18,3,-,11,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>4,8,-,9,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,0,-,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0<br><sub>2,1,-,0,1</sub> |  | 0.7 | 1.3 | 1.6 | 19.7 |
| Bilal Coulibaly (WAS) | 98% | 23.7<br><sub>27,22,33,23,24</sub> | 8.1<br><sub>17,1,7,6,9</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>2,5,1,2,5</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.5<br><sub>0,1,2,2,0</sub> |  | 0.8<br><sub>1,0,0,0,1</sub> |  | 0.9 | 0.8 | 1.3 | 13.3 |
| Tre Johnson (WAS) | 88% | 19.9<br><sub>-,13,22,14,27</sub> | 7.6<br><sub>-,4,4,3,23</sub> |  | 2.4<br><sub>-,2,3,2,1</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 1.1<br><sub>-,0,0,1,5</sub> |  | 0.7 | 0.2 | 1.1 | 10.9 |
| Deandre Ayton (WAS) | 98% | 17.0<br><sub>12,17,24,11,23</sub> | 5.4<br><sub>10,3,4,5,8</sub> |  | 5.1<br><sub>3,3,6,4,11</sub> |  | 0.7<br><sub>0,1,2,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.9 | 11.2 |
| Bub Carrington (WAS) | 98% | 16.9<br><sub>20,20,19,19,15</sub> | 5.2<br><sub>3,9,3,0,5</sub> |  | 1.9<br><sub>1,4,4,1,1</sub> |  | 2.1<br><sub>3,2,4,2,1</sub> |  | 0.7<br><sub>0,3,1,0,1</sub> |  | 0.4 | 0.1 | 1.2 | 9.1 |
| Will Riley (WAS) | 88% | 11.5<br><sub>-,1,4,13,9</sub> | 4.6<br><sub>-,0,0,0,7</sub> |  | 1.5<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,0,1,0,0</sub> |  | 0.4<br><sub>-,0,0,0,1</sub> |  | 0.4 | 0.1 | 0.7 | 7.0 |
| Khris Middleton (WAS) | 52% | 9.1<br><sub>23,5,-,-,-</sub> | 3.0<br><sub>4,0,-,-,-</sub> |  | 1.4<br><sub>3,0,-,-,-</sub> |  | 0.7<br><sub>2,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.8 | 5.0 |
| Anthony Gill (WAS) | 26% | 7.5<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Tre Mann (WAS) | 48% | 5.8<br><sub>-,1,-,3,-</sub> | 2.8<br><sub>-,0,-,2,-</sub> |  | 0.8<br><sub>-,0,-,0,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.0 | 0.5 | 4.2 |
| Felix Okpara (WAS) | 52% | 5.8<br><sub>-,-,-,3,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.3 |

</details>


### ORL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.9–114.7 | ORL 34% | 2.97 / 1.51 | GSW -5.5 | 223.5 | GSW -5.5 covers 51%; o222.5 52% |
| Expected (weighted by chance each plays) | 108.7–115.6 | ORL 30% | 3.28 / 1.44 | GSW -6.5 | 224.5 | GSW -5.5 covers 54%; o222.5 54% |
| if Draymond Green plays | 108.5–115.4 | ORL 31% | 3.26 / 1.44 | GSW -7.5 | 223.5 | GSW -5.5 covers 55%; o222.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 19.3 | 7.8 | 3.7 | 1.8 | 0.8 | 0.8 | 0.3 | 1.2 | 13.4 | small |
| Gary Payton II (GSW) | Questionable | 55% | 15.2 | 6.2 | 2.8 | 1.1 | 0.4 | 0.9 | 0.2 | 0.7 | 10.1 | small |
| Draymond Green (GSW) | Questionable | 55% | 27.0 | 6.7 | 5.2 | 5.3 | 0.8 | 1.1 | 0.8 | 2.2 | 17.2 | full tables below |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 35.2<br><sub>34,39,40,38,38</sub> | 21.7<br><sub>15,26,14,24,15</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>4,5,6,3,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 7.0<br><sub>5,11,12,6,15</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.3 | 3.4 | 34.5 |
| Desmond Bane | 98% | 34.8<br><sub>34,39,40,36,32</sub> | 20.6<br><sub>13,28,19,20,15</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,2,2,3,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>4,6,1,3,0</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.8<br><sub>2,6,5,4,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.5 | 2.6 | 28.7 |
| Wendell Carter Jr. | 98% | 32.5<br><sub>26,39,35,34,34</sub> | 12.5<br><sub>3,20,7,6,27</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>10,7,10,9,13</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>0,1,1,0,2</sub> |  | 1.1 | 0.7 | 1.8 | 22.9 |
| Anthony Black | 98% | 30.7<br><sub>22,31,33,-,31</sub> | 14.9<br><sub>8,17,23,-,10</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>2,6,8,-,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>1,10,3,-,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>0,3,1,-,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.8 | 0.6 | 2.5 | 23.5 |
| Tristan da Silva | 98% | 29.6<br><sub>31,23,35,32,30</sub> | 12.7<br><sub>20,8,23,10,18</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,0,10,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,2,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>4,2,5,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.3 | 1.5 | 18.8 |
| Jase Richardson | 91% | 24.6<br><sub>14,33,26,29,26</sub> | 9.0<br><sub>10,4,4,9,10</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,6,1,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,2,3,5,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>2,0,0,0,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.3 | 1.2 | 14.2 |
| Jamal Cain | 98% | 22.9<br><sub>16,15,18,25,25</sub> | 8.8<br><sub>9,13,5,10,5</sub> |  | 3.5<br><sub>1,0,1,3,5</sub> |  | 1.3<br><sub>0,0,1,1,0</sub> |  | 1.0<br><sub>0,3,1,2,1</sub> |  | 0.7 | 0.2 | 1.2 | 13.6 |
| Jevon Carter | 63% | 12.9<br><sub>22,-,-,18,3</sub> | 4.2<br><sub>6,-,-,5,0</sub> |  | 1.2<br><sub>0,-,-,1,0</sub> |  | 1.4<br><sub>3,-,-,4,0</sub> |  | 0.6<br><sub>2,-,-,1,0</sub> |  | 0.6 | 0.1 | 0.5 | 6.8 |
| Nikola Vucevic | 98% | 11.2<br><sub>16,6,7,14,4</sub> | 4.6<br><sub>5,3,2,7,0</sub> |  | 3.1<br><sub>4,1,4,6,0</sub> |  | 1.3<br><sub>2,0,2,1,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.4 | 0.5 | 8.9 |
| Goga Bitadze | 67% | 11.1<br><sub>11,6,5,-,8</sub> | 4.2<br><sub>6,2,0,-,4</sub> |  | 3.6<br><sub>0,4,1,-,5</sub> |  | 0.8<br><sub>1,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.7 | 0.7 | 8.7 |
| Alex Morales | 67% | 10.2<br><sub>7,9,-,14,6</sub> | 2.8<br><sub>2,0,-,3,0</sub> |  | 1.4<br><sub>2,1,-,2,0</sub> |  | 0.8<br><sub>1,0,-,0,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 5.0 |
| Colin Castleton | 52% | 6.8<br><sub>7,-,-,-,2</sub> | 2.4<br><sub>2,-,-,-,0</sub> |  | 1.9<br><sub>2,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,1</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.8 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 91% | 33.7<br><sub>32,33,37,33,32</sub> | 16.0<br><sub>8,21,17,20,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>5,5,8,3,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>6,6,8,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>0,4,2,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.3 | 1.8 | 25.9 |
| Yaxel Lendeborg | 98% | 33.2<br><sub>35,24,34,29,30</sub> | 20.1<br><sub>26,6,37,16,17</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>9,1,4,5,8</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>1,0,6,5,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>2,1,6,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.6 | 2.9 | 31.2 |
| Stephen Curry | 98% | 32.2<br><sub>32,31,-,33,28</sub> | 26.6<br><sub>44,31,-,34,29</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>8,4,-,6,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.4<br><sub>6,6,-,7,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>6,8,-,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.4 | 2.9 | 35.7 |
| De'Anthony Melton | 98% | 25.3<br><sub>20,21,28,28,17</sub> | 10.7<br><sub>8,16,21,2,5</sub> |  | 4.3<br><sub>6,5,6,7,6</sub> |  | 2.8<br><sub>0,3,3,2,2</sub> |  | 1.6<br><sub>2,4,6,0,0</sub> |  | 1.6 | 0.5 | 1.6 | 17.7 |
| Georges Niang | 97% | 24.1<br><sub>23,19,21,22,22</sub> | 9.2<br><sub>7,11,3,13,13</sub> |  | 3.4<br><sub>3,5,1,4,4</sub> |  | 1.6<br><sub>2,1,2,3,3</sub> |  | 1.6<br><sub>1,3,1,1,2</sub> |  | 0.6 | 0.2 | 1.1 | 14.2 |
| Brandon Williams | 80% | 22.4<br><sub>14,17,25,-,21</sub> | 12.5<br><sub>11,9,17,-,10</sub> |  | 3.0<br><sub>3,2,3,-,1</sub> |  | 3.6<br><sub>1,1,3,-,4</sub> |  | 0.8<br><sub>0,0,2,-,0</sub> |  | 0.9 | 0.4 | 1.9 | 19.0 |
| Al Horford | 98% | 21.9<br><sub>18,17,22,-,18</sub> | 6.7<br><sub>4,3,9,-,8</sub> |  | 4.7<br><sub>5,2,5,-,5</sub> |  | 1.9<br><sub>2,0,2,-,1</sub> |  | 1.0<br><sub>0,1,3,-,2</sub> |  | 0.5 | 0.9 | 0.7 | 13.3 |
| Will Richard | 98% | 21.5<br><sub>23,13,22,28,16</sub> | 5.6<br><sub>6,3,3,6,10</sub> |  | 2.5<br><sub>3,3,0,5,0</sub> |  | 1.3<br><sub>0,2,3,0,2</sub> |  | 0.7<br><sub>0,1,1,2,2</sub> |  | 1.0 | 0.2 | 0.6 | 9.4 |
| Charles Bassey | 96% | 16.1<br><sub>2,9,20,23,14</sub> | 6.7<br><sub>0,6,6,19,8</sub> |  | 6.1<br><sub>0,4,10,8,7</sub> |  | 0.8<br><sub>0,1,2,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.9 | 13.6 |
| Graham Ike | 88% | 13.0<br><sub>-,-,6,7,1</sub> | 4.8<br><sub>-,-,2,0,0</sub> |  | 3.0<br><sub>-,-,2,0,1</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.6 |
| LJ Cryer | 71% | 9.9<br><sub>-,-,2,1,1</sub> | 4.1<br><sub>-,-,0,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.9 |
| Malevy Leons | 52% | 9.8<br><sub>-,-,-,-,1</sub> | 2.8<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 5.2 |

</details>

<details><summary>if Draymond Green plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 91% | 32.8<br><sub>32,33,37,33,32</sub> | 16.0<br><sub>8,21,17,20,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,5,8,3,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>6,6,8,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>0,4,2,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.3 | 1.7 | 25.2 |
| Yaxel Lendeborg (GSW) | 98% | 32.0<br><sub>35,24,34,29,30</sub> | 19.6<br><sub>26,6,37,16,17</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>9,1,4,5,8</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>1,0,6,5,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,1,6,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.6 | 2.7 | 29.8 |
| Stephen Curry (GSW) | 98% | 31.2<br><sub>32,31,-,33,28</sub> | 26.1<br><sub>44,31,-,34,29</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>8,4,-,6,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.6<br><sub>6,6,-,7,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>6,8,-,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 2.8 | 34.4 |
| Draymond Green (GSW) | 100% | 27.0<br><sub>32,32,-,17,27</sub> | 6.7<br><sub>3,2,-,4,2</sub> | 4.5 · – | 5.2<br><sub>9,4,-,4,5</sub> | 5.5 | 5.3<br><sub>6,9,-,2,11</sub> | 6.5 | 0.8<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.8 | 2.2 | 17.2 |
| De'Anthony Melton (GSW) | 98% | 22.4<br><sub>20,21,28,28,17</sub> | 9.8<br><sub>8,16,21,2,5</sub> |  | 3.7<br><sub>6,5,6,7,6</sub> |  | 2.2<br><sub>0,3,3,2,2</sub> |  | 1.4<br><sub>2,4,6,0,0</sub> |  | 1.4 | 0.4 | 1.5 | 15.8 |
| Georges Niang (GSW) | 97% | 21.3<br><sub>23,19,21,22,22</sub> | 8.6<br><sub>7,11,3,13,13</sub> |  | 3.1<br><sub>3,5,1,4,4</sub> |  | 1.3<br><sub>2,1,2,3,3</sub> |  | 1.4<br><sub>1,3,1,1,2</sub> |  | 0.5 | 0.2 | 1.0 | 13.0 |
| Brandon Williams (GSW) | 80% | 20.3<br><sub>14,17,25,-,21</sub> | 11.3<br><sub>11,9,17,-,10</sub> |  | 2.7<br><sub>3,2,3,-,1</sub> |  | 3.0<br><sub>1,1,3,-,4</sub> |  | 0.7<br><sub>0,0,2,-,0</sub> |  | 0.8 | 0.4 | 1.7 | 17.1 |
| Al Horford (GSW) | 98% | 19.1<br><sub>18,17,22,-,18</sub> | 6.2<br><sub>4,3,9,-,8</sub> |  | 4.1<br><sub>5,2,5,-,5</sub> |  | 1.5<br><sub>2,0,2,-,1</sub> |  | 0.9<br><sub>0,1,3,-,2</sub> |  | 0.5 | 0.8 | 0.6 | 11.8 |
| Will Richard (GSW) | 98% | 18.4<br><sub>23,13,22,28,16</sub> | 5.0<br><sub>6,3,3,6,10</sub> |  | 2.2<br><sub>3,3,0,5,0</sub> |  | 1.1<br><sub>0,2,3,0,2</sub> |  | 0.6<br><sub>0,1,1,2,2</sub> |  | 0.9 | 0.2 | 0.5 | 8.2 |
| Charles Bassey (GSW) | 96% | 14.4<br><sub>2,9,20,23,14</sub> | 6.2<br><sub>0,6,6,19,8</sub> |  | 5.3<br><sub>0,4,10,8,7</sub> |  | 0.7<br><sub>0,1,2,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.8 | 12.3 |
| Graham Ike (GSW) | 88% | 9.1<br><sub>-,-,6,7,1</sub> | 3.6<br><sub>-,-,2,0,0</sub> |  | 2.1<br><sub>-,-,2,0,1</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.2 |
| LJ Cryer (GSW) | 71% | 7.7<br><sub>-,-,2,1,1</sub> | 3.5<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.0 | 0.4 | 4.9 |
| Malevy Leons (GSW) | 52% | 7.2<br><sub>-,-,-,-,1</sub> | 2.1<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 4.0 |
| Franz Wagner (ORL) | 98% | 35.2<br><sub>34,39,40,38,38</sub> | 21.7<br><sub>15,26,14,24,15</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>4,5,6,3,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 7.1<br><sub>5,11,12,6,15</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.4 | 3.4 | 34.5 |
| Desmond Bane (ORL) | 98% | 34.8<br><sub>34,39,40,36,32</sub> | 20.5<br><sub>13,28,19,20,15</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,2,2,3,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>4,6,1,3,0</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.8<br><sub>2,6,5,4,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.5 | 2.6 | 28.5 |
| Wendell Carter Jr. (ORL) | 98% | 32.5<br><sub>26,39,35,34,34</sub> | 12.4<br><sub>3,20,7,6,27</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>10,7,10,9,13</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>3,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>0,1,1,0,2</sub> |  | 1.1 | 0.7 | 1.8 | 22.9 |
| Anthony Black (ORL) | 98% | 30.7<br><sub>22,31,33,-,31</sub> | 14.9<br><sub>8,17,23,-,10</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>2,6,8,-,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>1,10,3,-,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>0,3,1,-,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.8 | 0.6 | 2.4 | 23.4 |
| Tristan da Silva (ORL) | 98% | 29.7<br><sub>31,23,35,32,30</sub> | 12.7<br><sub>20,8,23,10,18</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,0,10,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,2,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>4,2,5,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.3 | 1.5 | 18.8 |
| Jase Richardson (ORL) | 91% | 24.6<br><sub>14,33,26,29,26</sub> | 9.0<br><sub>10,4,4,9,10</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,6,1,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,2,3,5,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>2,0,0,0,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.3 | 1.2 | 14.2 |
| Jamal Cain (ORL) | 98% | 22.9<br><sub>16,15,18,25,25</sub> | 8.7<br><sub>9,13,5,10,5</sub> |  | 3.5<br><sub>1,0,1,3,5</sub> |  | 1.3<br><sub>0,0,1,1,0</sub> |  | 1.0<br><sub>0,3,1,2,1</sub> |  | 0.7 | 0.3 | 1.2 | 13.5 |
| Jevon Carter (ORL) | 63% | 12.9<br><sub>22,-,-,18,3</sub> | 4.2<br><sub>6,-,-,5,0</sub> |  | 1.2<br><sub>0,-,-,1,0</sub> |  | 1.4<br><sub>3,-,-,4,0</sub> |  | 0.6<br><sub>2,-,-,1,0</sub> |  | 0.6 | 0.1 | 0.5 | 6.8 |
| Nikola Vucevic (ORL) | 98% | 11.2<br><sub>16,6,7,14,4</sub> | 4.5<br><sub>5,3,2,7,0</sub> |  | 3.1<br><sub>4,1,4,6,0</sub> |  | 1.3<br><sub>2,0,2,1,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.4 | 0.5 | 8.9 |
| Goga Bitadze (ORL) | 67% | 10.9<br><sub>11,6,5,-,8</sub> | 4.2<br><sub>6,2,0,-,4</sub> |  | 3.5<br><sub>0,4,1,-,5</sub> |  | 0.8<br><sub>1,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.6 | 0.7 | 8.6 |
| Alex Morales (ORL) | 67% | 10.3<br><sub>7,9,-,14,6</sub> | 2.8<br><sub>2,0,-,3,0</sub> |  | 1.4<br><sub>2,1,-,2,0</sub> |  | 0.8<br><sub>1,0,-,0,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 5.0 |
| Colin Castleton (ORL) | 52% | 6.7<br><sub>7,-,-,-,2</sub> | 2.4<br><sub>2,-,-,-,0</sub> |  | 2.0<br><sub>2,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,1</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.8 |

</details>


### HOU @ PHX
Out: Mark Williams (PHX), Steven Adams (HOU), Clint Capela (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.9–109.8 | HOU 67% | 1.50 / 2.99 | PHX +6.5 | 225.5 | PHX +6.5 covers 51%; o223.5 54% |
| Expected (weighted by chance each plays) | 115.5–109.9 | HOU 66% | 1.52 / 2.93 | PHX +5.5 | 225.5 | PHX +6.5 covers 52%; o223.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Goodwin (PHX) | Doubtful | 20% | 14.6 | 5.5 | 2.8 | 1.4 | 0.7 | 1.0 | 0.2 | 0.6 | 9.6 | small |
| Rasheer Fleming (PHX) | Questionable | 55% | 7.9 | 2.7 | 1.3 | 0.3 | 0.2 | 0.3 | 0.2 | 0.3 | 4.4 | small |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.2<br><sub>30,35,33,36,35</sub> | 15.9<br><sub>14,22,30,14,11</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>2,3,9,10,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>2,2,5,0,2</sub> |  | 2.3<br><sub>3,3,6,4,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.8 | 1.5 | 25.2 |
| Alperen Sengun | 76% | 36.2<br><sub>-,-,33,38,39</sub> | 21.9<br><sub>-,-,16,26,17</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 10.0<br><sub>-,-,9,7,12</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>-,-,9,10,10</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 0.7<br><sub>-,-,0,1,0</sub> |  | 1.4 | 1.1 | 3.3 | 38.5 |
| Kevin Durant | 98% | 35.9<br><sub>31,37,27,33,35</sub> | 22.8<br><sub>18,28,14,12,21</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 4.5<br><sub>4,1,4,3,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 1.1 | 3.4 | 33.0 |
| Amen Thompson | 98% | 35.7<br><sub>33,39,28,25,32</sub> | 17.4<br><sub>23,15,8,14,11</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>4,3,3,3,8</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 4.3<br><sub>3,6,1,3,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.5 | 29.0 |
| Fred VanVleet | 86% | 32.9<br><sub>29,33,-,27,30</sub> | 13.5<br><sub>24,16,-,8,18</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>6,5,-,2,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.0<br><sub>5,6,-,9,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>4,3,-,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.4 | 1.7 | 22.1 |
| Tari Eason | 98% | 25.8<br><sub>31,26,19,27,24</sub> | 10.3<br><sub>5,11,8,13,9</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>9,13,3,4,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,2,2,3,1</sub> |  | 1.1<br><sub>1,0,2,3,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.7 | 1.2 | 17.8 |
| Reed Sheppard | 71% | 23.3<br><sub>23,-,-,17,21</sub> | 10.8<br><sub>7,-,-,8,14</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>3,-,-,1,2</sub> |  | 3.0<br><sub>4,-,-,1,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.5 | 1.3 | 16.1 |
| Marcus Smart | 83% | 23.0<br><sub>-,17,36,20,18</sub> | 8.6<br><sub>-,8,24,8,4</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>-,2,5,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.5<br><sub>-,4,3,4,1</sub> |  | 1.2<br><sub>-,0,7,2,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.3 | 1.6 | 13.7 |
| Bogdan Bogdanovic | 93% | 12.2<br><sub>15,11,19,5,5</sub> | 4.5<br><sub>16,6,4,0,0</sub> |  | 1.4<br><sub>2,1,2,0,0</sub> |  | 1.0<br><sub>4,0,1,1,0</sub> |  | 0.6<br><sub>4,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.9 |
| Oscar Tshiebwe | 88% | 9.0<br><sub>14,11,4,7,2</sub> | 3.8<br><sub>7,0,2,4,2</sub> |  | 3.6<br><sub>5,5,1,1,0</sub> |  | 0.5<br><sub>2,0,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 7.8 |
| Isaiah Crawford | 58% | 7.3<br><sub>5,-,19,2,-</sub> | 2.3<br><sub>3,-,8,0,-</sub> |  | 1.1<br><sub>0,-,1,0,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>1,-,2,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Jae'Sean Tate | 63% | 6.3<br><sub>4,-,6,2,-</sub> | 2.0<br><sub>0,-,0,0,-</sub> |  | 1.5<br><sub>0,-,3,1,-</sub> |  | 0.4<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 35.6<br><sub>34,39,35,34,34</sub> | 25.9<br><sub>3,20,26,33,30</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,2,3,1,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.9<br><sub>7,5,5,2,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,3,2,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 3.3 | 35.3 |
| Miles Bridges | 98% | 32.8<br><sub>32,37,35,31,31</sub> | 15.5<br><sub>17,24,21,18,18</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>8,10,6,7,13</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,2,3,5,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>2,2,3,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.5 | 1.5 | 25.1 |
| Dillon Brooks | 98% | 32.1<br><sub>33,21,34,35,29</sub> | 17.8<br><sub>19,22,18,15,24</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>5,1,8,6,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>5,2,4,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.2<br><sub>3,4,2,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.2 | 1.8 | 23.8 |
| Jalen Green | 98% | 30.5<br><sub>31,25,36,32,24</sub> | 16.2<br><sub>20,2,11,22,6</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,2,8,2,0</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>4,2,8,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.4 | 2.5 | 23.2 |
| Collin Gillespie | 98% | 26.3<br><sub>23,33,24,23,24</sub> | 9.9<br><sub>9,16,3,2,6</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>1,3,1,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.9<br><sub>2,10,2,2,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,4,1,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.2 | 1.3 | 16.9 |
| Oso Ighodaro | 98% | 24.4<br><sub>-,21,24,23,24</sub> | 6.9<br><sub>-,2,14,9,2</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>-,9,2,7,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>-,5,2,7,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.3 | 15.5 |
| Luke Kennard | 98% | 19.3<br><sub>16,12,18,14,21</sub> | 6.3<br><sub>9,9,6,0,12</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,1,2,0,1</sub> |  | 1.8<br><sub>2,2,1,1,5</sub> |  | 0.8<br><sub>3,1,2,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.1 | 0.8 | 10.1 |
| Ryan Dunn | 97% | 18.1<br><sub>14,11,10,18,25</sub> | 5.2<br><sub>6,5,5,2,11</sub> |  | 3.7<br><sub>2,3,3,6,3</sub> |  | 1.2<br><sub>1,1,1,2,3</sub> |  | 0.5<br><sub>1,1,1,0,1</sub> |  | 0.8 | 0.5 | 0.6 | 10.1 |
| Khaman Maluach | 98% | 17.9<br><sub>26,17,13,16,22</sub> | 5.7<br><sub>12,9,5,6,8</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>7,6,2,6,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>1,0,0,2,2</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 1.0 | 11.7 |
| Drew Timme | 16% | 8.3 | 3.0 |  | 1.4 |  | 0.7 |  | 0.2 |  | 0.2 | 0.1 | 0.5 | 5.1 |
| Pat Spencer | 80% | 7.3<br><sub>-,-,-,3,2</sub> | 2.6<br><sub>-,-,-,0,0</sub> |  | 0.9<br><sub>-,-,-,0,0</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Duop Reath | 80% | 7.0<br><sub>7,-,-,7,2</sub> | 2.6<br><sub>5,-,-,7,0</sub> |  | 1.3<br><sub>3,-,-,0,0</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.2<br><sub>1,-,-,1,0</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea | 64% | 6.8<br><sub>3,-,-,3,2</sub> | 2.6<br><sub>2,-,-,3,0</sub> |  | 0.9<br><sub>0,-,-,0,0</sub> |  | 0.9<br><sub>1,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Koa Peat | 63% | 6.5<br><sub>3,-,-,3,2</sub> | 2.1<br><sub>0,-,-,2,0</sub> |  | 1.6<br><sub>0,-,-,1,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.0 |

</details>


### SAS @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 32.7<br><sub>39,34,24,34,26</sub> | 27.0<br><sub>36,43,12,52,30</sub> | 27.5 · –<br><sub>o 49% · u 51%</sub> | 11.2<br><sub>14,7,11,24,14</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,4,5,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>4,3,0,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 3.4 | 2.7 | 41.4 |
| Devin Vassell | 98% | 32.0<br><sub>38,34,25,36,27</sub> | 11.1<br><sub>21,9,11,2,19</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>5,5,2,7,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,2,1,4,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,0,0,0,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.3 | 0.5 | 1.1 | 17.7 |
| Dylan Harper | 98% | 31.6<br><sub>37,39,27,36,28</sub> | 16.2<br><sub>13,25,17,21,19</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>5,7,7,5,2</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>8,6,8,0,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.3 | 1.9 | 25.0 |
| De'Aaron Fox | 98% | 31.4<br><sub>39,35,22,33,26</sub> | 14.8<br><sub>14,22,12,10,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>3,8,2,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>4,7,3,4,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>1,0,1,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.4 | 2.2 | 23.6 |
| Stephon Castle | 98% | 30.6<br><sub>38,22,26,35,28</sub> | 16.4<br><sub>14,0,16,17,19</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>6,5,5,10,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 5.3<br><sub>8,4,4,3,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>1,0,2,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 2.8 | 26.6 |
| Julian Champagnie | 98% | 24.7<br><sub>31,27,22,21,22</sub> | 8.1<br><sub>6,12,8,0,8</sub> |  | 4.3<br><sub>6,3,6,4,7</sub> |  | 1.3<br><sub>0,1,0,3,2</sub> |  | 1.4<br><sub>2,3,2,0,2</sub> |  | 0.9 | 0.5 | 0.7 | 13.6 |
| Keldon Johnson | 98% | 21.9<br><sub>23,24,27,19,27</sub> | 9.2<br><sub>9,2,15,4,3</sub> |  | 4.5<br><sub>6,6,7,5,6</sub> |  | 1.3<br><sub>2,0,1,2,6</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 15.1 |
| Luke Kornet | 98% | 15.5<br><sub>14,14,17,14,18</sub> | 4.0<br><sub>1,2,8,2,2</sub> |  | 4.4<br><sub>6,8,5,1,6</sub> |  | 1.0<br><sub>1,0,2,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.5 |
| Harrison Barnes | 72% | 14.1<br><sub>-,-,21,13,19</sub> | 4.7<br><sub>-,-,13,4,13</sub> |  | 1.6<br><sub>-,-,0,2,1</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,3,1,2</sub> |  | 0.3 | 0.1 | 0.5 | 7.0 |
| Carter Bryant | 80% | 8.7<br><sub>5,11,14,-,3</sub> | 2.8<br><sub>3,6,3,-,0</sub> |  | 1.5<br><sub>0,0,0,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.2<br><sub>1,2,1,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Jordan McLaughlin | 52% | 7.5<br><sub>-,-,8,-,8</sub> | 2.4<br><sub>-,-,0,-,2</sub> |  | 1.0<br><sub>-,-,1,-,2</sub> |  | 1.1<br><sub>-,-,3,-,1</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.6 |
| Maliq Brown | 80% | 6.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 2.7 |
| Tarris Reed Jr. | 58% | 6.3<br><sub>-,-,7,-,3</sub> | 2.5<br><sub>-,-,4,-,0</sub> |  | 3.2<br><sub>-,-,7,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 5.9 |
| David Jones Garcia | 58% | 5.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Ja'Kobi Gillespie | 88% | 5.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.4<br><sub>32,30,35,35,39</sub> | 22.7<br><sub>24,24,28,21,22</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>9,5,3,7,9</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.7<br><sub>7,2,5,12,11</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.5 | 3.6 | 36.1 |
| Damian Lillard | 98% | 33.5<br><sub>30,27,30,33,37</sub> | 19.1<br><sub>9,22,20,25,22</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>2,5,6,3,0</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>2,4,6,5,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>1,3,1,2,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.2 | 2.6 | 28.4 |
| Toumani Camara | 98% | 30.3<br><sub>26,31,31,32,30</sub> | 11.6<br><sub>13,14,9,11,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>2,4,5,4,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,4,3,1,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.4 | 1.2 | 17.5 |
| Jrue Holiday | 98% | 29.8<br><sub>24,22,31,28,31</sub> | 13.1<br><sub>6,14,17,15,12</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>6,4,8,4,1</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>4,3,10,0,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,2,3,5,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 1.9 | 22.6 |
| Donovan Clingan | 98% | 27.0<br><sub>29,15,32,29,28</sub> | 11.5<br><sub>11,4,17,24,17</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 10.5<br><sub>8,9,18,11,11</sub> | 11.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,0,3,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>1,0,1,1,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.5 | 1.8 | 1.3 | 24.0 |
| Scoot Henderson | 98% | 25.3<br><sub>19,31,26,22,23</sub> | 11.6<br><sub>9,14,8,9,2</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>0,1,2,1,0</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,1,2,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 2.1 | 16.9 |
| Sidy Cissoko | 98% | 22.0<br><sub>19,19,22,21,22</sub> | 5.9<br><sub>4,1,8,7,7</sub> |  | 3.1<br><sub>6,3,3,4,2</sub> |  | 1.9<br><sub>2,1,0,4,3</sub> |  | 0.7<br><sub>0,0,2,1,2</sub> |  | 0.8 | 0.4 | 0.9 | 10.8 |
| Robert Williams III | 98% | 17.3<br><sub>-,14,15,16,16</sub> | 6.3<br><sub>-,3,2,9,9</sub> |  | 6.5<br><sub>-,3,6,8,5</sub> |  | 1.2<br><sub>-,1,2,1,2</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.6 | 1.3 | 0.8 | 14.0 |
| Chris Youngblood | 88% | 12.4<br><sub>-,7,15,4,11</sub> | 4.7<br><sub>-,3,7,0,7</sub> |  | 1.5<br><sub>-,0,2,0,1</sub> |  | 0.8<br><sub>-,0,1,1,0</sub> |  | 0.7<br><sub>-,1,1,0,2</sub> |  | 0.3 | 0.2 | 0.4 | 7.1 |
| Micah Potter | 52% | 7.5<br><sub>9,4,-,2,-</sub> | 3.4<br><sub>1,2,-,4,-</sub> |  | 2.1<br><sub>2,1,-,1,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>0,0,-,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.9 |
| Branden Carlson | 52% | 7.3<br><sub>12,4,-,3,-</sub> | 2.4<br><sub>2,0,-,2,-</sub> |  | 1.7<br><sub>2,2,-,0,-</sub> |  | 0.5<br><sub>1,1,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 4.5 |
| Yang Hansen | 67% | 7.0<br><sub>5,13,-,2,3</sub> | 3.0<br><sub>3,6,-,0,2</sub> |  | 1.7<br><sub>2,5,-,0,0</sub> |  | 0.4<br><sub>1,1,-,0,0</sub> |  | 0.2<br><sub>1,2,-,0,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.0 |
| John Tonje | 52% | 6.7<br><sub>5,-,-,-,-</sub> | 3.4<br><sub>5,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>1,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.1 |
| Jayson Kent | 52% | 6.2<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-07/`._
