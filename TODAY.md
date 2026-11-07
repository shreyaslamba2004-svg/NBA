# NBA model · Sat 07 Nov 2026 (US date)

Updated **Sat 07 Nov, 09:11 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-07/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

_No long shots clear the edge threshold right now._

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DEN @ IND | Sun 08 Nov 09:00 | 122.3–115.7 | DEN 68% | 1.46 / 3.16 | IND +6.5 | 238.5 | IND +7.5 covers 52%; o229.5 68% |
| BKN @ ATL | Sun 08 Nov 11:30 | 105.0–114.5 | BKN 25% | 3.97 / 1.34 | ATL -9.5 | 219.5 | ATL -6.5 covers 58%; o226.5 35% |
| NYK @ CLE | Sun 08 Nov 12:00 | 114.9–108.0 | NYK 69% | 1.46 / 3.19 | CLE +6.5 | 222.5 | CLE +4.5 covers 43%; o224.5 46% |
| WAS @ OKC | Sun 08 Nov 12:00 | 111.3–118.3 | WAS 31% | 3.20 / 1.45 | OKC -6.5 | 229.5 | OKC -11.5 covers 37%; o219.5 71% |
| ORL @ GSW | Sun 08 Nov 12:30 | 108.9–114.6 | ORL 34% | 2.96 / 1.51 | GSW -5.5 | 223.5 | GSW -6.5 covers 48%; o221.5 54% |
| HOU @ PHX | Sun 08 Nov 13:00 | 115.9–109.8 | HOU 67% | 1.50 / 2.99 | PHX +6.5 | 225.5 | PHX +7.5 covers 54%; o221.5 59% |
| SAS @ POR | Sun 08 Nov 14:00 | 114.1–109.3 | SAS 64% | 1.57 / 2.74 | POR +5.5 | 223.5 | POR +6.5 covers 54%; o227.5 41% |

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
| T.J. McConnell (IND) | Questionable | 55% | 13.0 | 6.6 | 1.8 | 3.9 | 0.2 | 0.7 | 0.2 | 0.8 | 12.3 | small |
| Kelly Oubre Jr. (IND) | Questionable | 55% | 22.6 | 9.8 | 3.4 | 1.3 | 0.9 | 0.8 | 0.4 | 0.9 | 14.4 | full tables below |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 36.1<br><sub>36,38,37,39,28</sub> | 26.1<br><sub>19,23,39,35,14</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,1,8,5,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>8,6,5,6,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,5,7,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.5 | 37.3 |
| Nikola Jokic | 98% | 35.2<br><sub>35,34,37,36,30</sub> | 27.2<br><sub>19,21,18,26,32</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 12.7<br><sub>7,13,7,9,10</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 10.0<br><sub>11,10,10,8,11</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7 | 0.9 | 3.5 | 49.9 |
| Christian Braun | 98% | 33.2<br><sub>34,36,37,37,28</sub> | 13.3<br><sub>9,15,31,14,11</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>4,0,3,3,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,4,1,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>1,3,7,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.4 | 1.1 | 20.2 |
| Cameron Johnson | 98% | 28.7<br><sub>-,-,34,34,30</sub> | 12.1<br><sub>-,-,12,7,12</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>-,-,9,4,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.8<br><sub>-,-,2,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.4 | 1.0 | 18.3 |
| Aaron Gordon | 98% | 28.3<br><sub>25,31,29,30,25</sub> | 13.2<br><sub>7,15,15,5,17</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>4,11,4,6,1</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,3,5,2,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.4 | 1.2 | 21.5 |
| DeMar DeRozan | 67% | 24.2<br><sub>29,26,24,20,-</sub> | 12.8<br><sub>21,6,3,9,-</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,2,1,0,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>2,5,5,1,-</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.5<br><sub>2,0,0,0,-</sub> |  | 0.9 | 0.3 | 1.4 | 18.6 |
| Trevon Brazile | 96% | 19.9<br><sub>17,32,19,18,23</sub> | 6.2<br><sub>6,11,6,6,6</sub> |  | 5.0<br><sub>1,8,3,5,7</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.9 | 12.1 |
| Bryce Hopkins | 64% | 18.6<br><sub>31,14,-,-,28</sub> | 5.9<br><sub>13,0,-,-,18</sub> |  | 2.8<br><sub>3,2,-,-,4</sub> |  | 1.0<br><sub>1,0,-,-,1</sub> |  | 0.4<br><sub>1,0,-,-,1</sub> |  | 0.8 | 0.3 | 1.0 | 9.7 |
| Marvin Bagley III | 98% | 13.2<br><sub>11,19,11,12,14</sub> | 6.4<br><sub>7,8,0,6,10</sub> |  | 4.2<br><sub>2,5,5,4,2</sub> |  | 0.8<br><sub>0,1,0,0,2</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 11.3 |
| Tyus Jones | 93% | 12.7<br><sub>9,11,11,8,18</sub> | 3.4<br><sub>0,5,3,2,6</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 2.1<br><sub>2,1,0,1,8</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.5 |
| Spencer Jones | 3% | 8.5 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.5 | 5.8 |
| Alpha Diallo | 91% | 7.6<br><sub>-,-,-,6,4</sub> | 3.5<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.2 |
| Cam Whitmore | 58% | 7.2<br><sub>4,-,-,-,-</sub> | 3.8<br><sub>4,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |
| Ryan Nembhard | 52% | 6.4<br><sub>4,-,-,-,4</sub> | 2.8<br><sub>4,-,-,-,0</sub> |  | 1.0<br><sub>0,-,-,-,0</sub> |  | 0.7<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Zeke Nnaji | 48% | 6.3<br><sub>4,-,-,-,4</sub> | 2.1<br><sub>5,-,-,-,2</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.3 | 4.0 |
| DaRon Holmes II | 52% | 5.7<br><sub>4,-,-,-,4</sub> | 2.5<br><sub>0,-,-,-,0</sub> |  | 1.2<br><sub>0,-,-,-,1</sub> |  | 0.4<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 71% | 34.5<br><sub>35,30,35,-,38</sub> | 19.8<br><sub>18,22,23,-,22</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,2,3,-,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 9.0<br><sub>14,9,4,-,5</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>1,5,4,-,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 2.5 | 31.9 |
| Pascal Siakam | 80% | 33.0<br><sub>34,29,36,-,30</sub> | 23.4<br><sub>26,13,17,-,20</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 6.7<br><sub>11,5,5,-,4</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>3,4,5,-,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>0,0,0,-,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.3 | 2.4 | 34.5 |
| Aaron Nesmith | 80% | 28.5<br><sub>27,21,30,-,30</sub> | 14.9<br><sub>18,9,11,-,16</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,3,3,-,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>1,2,4,-,2</sub> |  | 2.1<br><sub>3,1,0,-,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.5 | 1.4 | 20.5 |
| Quenton Jackson | 98% | 26.2<br><sub>14,24,24,35,22</sub> | 13.1<br><sub>2,24,12,20,13</sub> |  | 3.5<br><sub>2,4,3,7,7</sub> |  | 4.3<br><sub>6,1,2,3,2</sub> |  | 1.2<br><sub>0,2,3,1,3</sub> |  | 1.2 | 0.2 | 1.5 | 20.9 |
| Jarace Walker | 98% | 25.8<br><sub>22,28,20,45,17</sub> | 12.3<br><sub>7,14,6,15,2</sub> |  | 5.6<br><sub>8,6,6,7,8</sub> |  | 2.8<br><sub>1,4,3,3,1</sub> |  | 1.5<br><sub>1,3,2,1,0</sub> |  | 0.8 | 0.3 | 1.6 | 20.8 |
| Ivica Zubac | 52% | 23.8<br><sub>-,-,-,-,19</sub> | 11.0<br><sub>-,-,-,-,1</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 8.7<br><sub>-,-,-,-,4</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.7 | 1.2 | 21.4 |
| Braden Smith | 88% | 22.2<br><sub>5,12,1,42,24</sub> | 8.5<br><sub>0,1,0,19,10</sub> |  | 2.2<br><sub>0,0,0,4,1</sub> |  | 4.3<br><sub>1,1,0,10,5</sub> |  | 0.6<br><sub>0,0,0,2,0</sub> |  | 1.0 | 0.4 | 1.4 | 15.1 |
| Obi Toppin | 58% | 21.1<br><sub>22,-,-,-,19</sub> | 13.1<br><sub>13,-,-,-,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>6,-,-,-,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,-,-,-,1</sub> |  | 1.7<br><sub>1,-,-,-,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.2 | 1.1 | 19.7 |
| Jay Huff | 93% | 20.6<br><sub>16,19,17,40,14</sub> | 9.2<br><sub>3,13,0,22,6</sub> |  | 4.0<br><sub>6,1,3,8,3</sub> |  | 1.5<br><sub>2,0,0,2,1</sub> |  | 1.2<br><sub>1,3,0,0,2</sub> |  | 0.5 | 1.2 | 0.9 | 14.7 |
| Kobe Brown | 72% | 18.4<br><sub>-,20,15,38,7</sub> | 7.1<br><sub>-,9,3,16,0</sub> |  | 3.3<br><sub>-,6,1,6,1</sub> |  | 1.6<br><sub>-,4,1,1,0</sub> |  | 0.8<br><sub>-,0,1,2,0</sub> |  | 0.5 | 0.2 | 0.8 | 12.0 |
| Jalen Slawson | 91% | 16.8<br><sub>12,18,18,41,6</sub> | 5.3<br><sub>2,4,3,12,2</sub> |  | 3.2<br><sub>1,4,5,7,2</sub> |  | 1.5<br><sub>1,1,0,3,1</sub> |  | 0.4<br><sub>0,0,0,2,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.0 |
| Larry Nance Jr. | 91% | 16.0<br><sub>23,18,26,-,14</sub> | 5.0<br><sub>5,6,4,-,4</sub> |  | 3.3<br><sub>5,2,6,-,4</sub> |  | 1.0<br><sub>0,1,1,-,1</sub> |  | 0.5<br><sub>1,2,1,-,0</sub> |  | 0.8 | 0.3 | 0.6 | 9.3 |

</details>

<details><summary>if Kelly Oubre Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray (DEN) | 98% | 36.1<br><sub>36,38,37,39,28</sub> | 25.9<br><sub>19,23,39,35,14</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,1,8,5,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>8,6,5,6,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,5,7,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.5 | 37.2 |
| Nikola Jokic (DEN) | 98% | 35.2<br><sub>35,34,37,36,30</sub> | 27.0<br><sub>19,21,18,26,32</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 12.6<br><sub>7,13,7,9,10</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 10.1<br><sub>11,10,10,8,11</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7 | 0.9 | 3.5 | 49.8 |
| Christian Braun (DEN) | 98% | 33.2<br><sub>34,36,37,37,28</sub> | 13.2<br><sub>9,15,31,14,11</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>4,0,3,3,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,4,1,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>1,3,7,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.4 | 1.1 | 20.2 |
| Cameron Johnson (DEN) | 98% | 28.6<br><sub>-,-,34,34,30</sub> | 12.0<br><sub>-,-,12,7,12</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>-,-,9,4,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.8<br><sub>-,-,2,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.4 | 1.0 | 18.3 |
| Aaron Gordon (DEN) | 98% | 28.3<br><sub>25,31,29,30,25</sub> | 13.1<br><sub>7,15,15,5,17</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>4,11,4,6,1</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,3,5,2,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.4 | 1.2 | 21.4 |
| DeMar DeRozan (DEN) | 67% | 24.1<br><sub>29,26,24,20,-</sub> | 12.7<br><sub>21,6,3,9,-</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,2,1,0,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>2,5,5,1,-</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.4<br><sub>2,0,0,0,-</sub> |  | 0.9 | 0.3 | 1.4 | 18.5 |
| Trevon Brazile (DEN) | 96% | 19.8<br><sub>17,32,19,18,23</sub> | 6.2<br><sub>6,11,6,6,6</sub> |  | 5.0<br><sub>1,8,3,5,7</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.8 | 12.1 |
| Bryce Hopkins (DEN) | 64% | 18.5<br><sub>31,14,-,-,28</sub> | 5.8<br><sub>13,0,-,-,18</sub> |  | 2.8<br><sub>3,2,-,-,4</sub> |  | 1.0<br><sub>1,0,-,-,1</sub> |  | 0.4<br><sub>1,0,-,-,1</sub> |  | 0.8 | 0.3 | 1.0 | 9.6 |
| Marvin Bagley III (DEN) | 98% | 13.0<br><sub>11,19,11,12,14</sub> | 6.3<br><sub>7,8,0,6,10</sub> |  | 4.1<br><sub>2,5,5,4,2</sub> |  | 0.8<br><sub>0,1,0,0,2</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 11.2 |
| Tyus Jones (DEN) | 93% | 12.7<br><sub>9,11,11,8,18</sub> | 3.4<br><sub>0,5,3,2,6</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 2.1<br><sub>2,1,0,1,8</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.5 |
| Spencer Jones (DEN) | 3% | 8.5 | 3.4 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.7 |
| Alpha Diallo (DEN) | 91% | 7.7<br><sub>-,-,-,6,4</sub> | 3.5<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Cam Whitmore (DEN) | 58% | 7.2<br><sub>4,-,-,-,-</sub> | 3.7<br><sub>4,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |
| Ryan Nembhard (DEN) | 52% | 6.4<br><sub>4,-,-,-,4</sub> | 2.8<br><sub>4,-,-,-,0</sub> |  | 1.0<br><sub>0,-,-,-,0</sub> |  | 0.6<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Zeke Nnaji (DEN) | 48% | 6.4<br><sub>4,-,-,-,4</sub> | 2.1<br><sub>5,-,-,-,2</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.3 | 4.0 |
| DaRon Holmes II (DEN) | 52% | 5.8<br><sub>4,-,-,-,4</sub> | 2.5<br><sub>0,-,-,-,0</sub> |  | 1.2<br><sub>0,-,-,-,1</sub> |  | 0.4<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.1 |
| Andrew Nembhard (IND) | 71% | 32.6<br><sub>35,30,35,-,38</sub> | 18.3<br><sub>18,22,23,-,22</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>3,2,3,-,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 8.8<br><sub>14,9,4,-,5</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,5,4,-,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.1 | 2.3 | 29.9 |
| Pascal Siakam (IND) | 80% | 32.0<br><sub>34,29,36,-,30</sub> | 22.5<br><sub>26,13,17,-,20</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>11,5,5,-,4</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>3,4,5,-,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,0,0,-,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.3 | 2.2 | 33.4 |
| Aaron Nesmith (IND) | 80% | 26.8<br><sub>27,21,30,-,30</sub> | 14.0<br><sub>18,9,11,-,16</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,3,3,-,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,2,4,-,2</sub> |  | 1.9<br><sub>3,1,0,-,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.4 | 1.3 | 19.4 |
| Jarace Walker (IND) | 98% | 23.5<br><sub>22,28,20,45,17</sub> | 10.9<br><sub>7,14,6,15,2</sub> |  | 5.2<br><sub>8,6,6,7,8</sub> |  | 2.6<br><sub>1,4,3,3,1</sub> |  | 1.4<br><sub>1,3,2,1,0</sub> |  | 0.8 | 0.3 | 1.4 | 18.8 |
| Quenton Jackson (IND) | 98% | 23.3<br><sub>14,24,24,35,22</sub> | 11.6<br><sub>2,24,12,20,13</sub> |  | 3.1<br><sub>2,4,3,7,7</sub> |  | 3.8<br><sub>6,1,2,3,2</sub> |  | 1.0<br><sub>0,2,3,1,3</sub> |  | 1.0 | 0.2 | 1.3 | 18.6 |
| Kelly Oubre Jr. (IND) | 100% | 22.6<br><sub>30,22,20,-,-</sub> | 9.8<br><sub>15,10,11,-,-</sub> | 9.5 · – | 3.4<br><sub>3,4,2,-,-</sub> | 3.5 | 1.3<br><sub>1,1,1,-,-</sub> |  | 0.9<br><sub>1,1,2,-,-</sub> | 1.5 | 0.8 | 0.4 | 0.9 | 14.4 |
| Ivica Zubac (IND) | 52% | 22.0<br><sub>-,-,-,-,19</sub> | 10.2<br><sub>-,-,-,-,1</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 8.0<br><sub>-,-,-,-,4</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.6 | 1.2 | 19.8 |
| Obi Toppin (IND) | 58% | 19.9<br><sub>22,-,-,-,19</sub> | 12.9<br><sub>13,-,-,-,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>6,-,-,-,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>0,-,-,-,1</sub> |  | 1.6<br><sub>1,-,-,-,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.2 | 1.1 | 19.4 |
| Braden Smith (IND) | 88% | 19.0<br><sub>5,12,1,42,24</sub> | 7.2<br><sub>0,1,0,19,10</sub> |  | 1.8<br><sub>0,0,0,4,1</sub> |  | 3.6<br><sub>1,1,0,10,5</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.4 | 1.2 | 12.7 |
| Jay Huff (IND) | 93% | 18.0<br><sub>16,19,17,40,14</sub> | 8.2<br><sub>3,13,0,22,6</sub> |  | 3.5<br><sub>6,1,3,8,3</sub> |  | 1.4<br><sub>2,0,0,2,1</sub> |  | 1.0<br><sub>1,3,0,0,2</sub> |  | 0.4 | 1.1 | 0.8 | 13.1 |
| Kobe Brown (IND) | 72% | 15.1<br><sub>-,20,15,38,7</sub> | 5.8<br><sub>-,9,3,16,0</sub> |  | 2.7<br><sub>-,6,1,6,1</sub> |  | 1.3<br><sub>-,4,1,1,0</sub> |  | 0.6<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.9 |
| Larry Nance Jr. (IND) | 91% | 14.4<br><sub>23,18,26,-,14</sub> | 4.5<br><sub>5,6,4,-,4</sub> |  | 3.0<br><sub>5,2,6,-,4</sub> |  | 0.9<br><sub>0,1,1,-,1</sub> |  | 0.4<br><sub>1,2,1,-,0</sub> |  | 0.7 | 0.2 | 0.5 | 8.4 |
| Jalen Slawson (IND) | 91% | 14.0<br><sub>12,18,18,41,6</sub> | 4.5<br><sub>2,4,3,12,2</sub> |  | 2.6<br><sub>1,4,5,7,2</sub> |  | 1.3<br><sub>1,1,0,3,1</sub> |  | 0.4<br><sub>0,0,0,2,0</sub> |  | 0.7 | 0.5 | 0.7 | 8.4 |

</details>


### BKN @ ATL
Out: Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Jalen Johnson (ATL), Jock Landale (ATL), Asa Newell (ATL), Egor Demin (BKN), Grant Nelson (BKN), Ben Saraf (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.0–114.5 | BKN 25% | 3.97 / 1.34 | ATL -9.5 | 219.5 | ATL -6.5 covers 58%; o226.5 35% |
| Expected (weighted by chance each plays) | 106.2–112.8 | BKN 32% | 3.12 / 1.47 | ATL -6.5 | 218.5 | ATL -6.5 covers 50%; o226.5 34% |
| if Day'Ron Sharpe plays | 107.0–113.1 | BKN 33% | 3.01 / 1.50 | ATL -6.5 | 219.5 | ATL -6.5 covers 49%; o226.5 36% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Drake Powell (BKN) | Questionable | 55% | 12.7 | 4.0 | 1.2 | 0.8 | 0.3 | 0.4 | 0.2 | 0.7 | 6.1 | small |
| Day'Ron Sharpe (BKN) | Day-To-Day | 70% | 22.9 | 9.1 | 7.9 | 2.9 | 0.3 | 1.0 | 0.8 | 2.0 | 19.8 | full tables below |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 98% | 34.9<br><sub>40,26,36,37,38</sub> | 23.1<br><sub>27,13,23,18,26</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>12,7,9,5,10</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>2,1,3,2,0</sub> |  | 3.0<br><sub>6,2,3,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.4 | 2.7 | 33.8 |
| Julius Randle | 98% | 34.5<br><sub>44,25,37,36,31</sub> | 20.9<br><sub>24,15,20,21,22</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>9,8,5,11,3</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.9<br><sub>4,3,6,2,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,3,4,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 3.9 | 33.5 |
| Nolan Traore | 98% | 26.7<br><sub>24,26,30,24,27</sub> | 13.0<br><sub>15,9,16,17,16</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>1,2,2,3,4</sub> |  | 4.1<br><sub>3,2,6,4,2</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,0,4,5,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.5 | 3.0 | 19.7 |
| Mikel Brown Jr. | 96% | 26.1<br><sub>28,23,-,27,20</sub> | 11.6<br><sub>17,10,-,13,18</sub> |  | 3.0<br><sub>5,0,-,2,2</sub> |  | 4.0<br><sub>5,4,-,3,4</sub> |  | 1.7<br><sub>4,0,-,1,3</sub> |  | 0.8 | 0.3 | 2.1 | 18.6 |
| Noah Clowney | 98% | 23.1<br><sub>24,22,24,20,17</sub> | 8.6<br><sub>3,3,8,2,7</sub> |  | 4.3<br><sub>4,8,3,6,1</sub> |  | 1.3<br><sub>1,1,0,2,1</sub> |  | 1.1<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.6 | 1.1 | 14.2 |
| Chaney Johnson | 93% | 22.3<br><sub>29,19,31,28,9</sub> | 6.3<br><sub>15,6,2,4,0</sub> |  | 3.1<br><sub>3,2,2,3,2</sub> |  | 1.2<br><sub>2,0,0,2,1</sub> |  | 0.7<br><sub>3,0,0,1,0</sub> |  | 0.7 | 0.5 | 1.2 | 10.6 |
| Keon Ellis | 96% | 22.1<br><sub>25,21,20,25,10</sub> | 5.9<br><sub>2,6,0,5,1</sub> |  | 2.2<br><sub>3,2,2,1,2</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 0.8<br><sub>0,2,0,1,0</sub> |  | 1.1 | 0.7 | 0.8 | 9.6 |
| Moritz Wagner | 93% | 21.3<br><sub>22,23,21,20,20</sub> | 10.4<br><sub>15,16,14,6,6</sub> |  | 5.3<br><sub>4,8,6,1,1</sub> |  | 1.4<br><sub>3,1,0,2,0</sub> |  | 0.9<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.4 | 1.3 | 17.1 |
| Danny Wolf | 52% | 18.7<br><sub>-,12,-,-,19</sub> | 8.2<br><sub>-,9,-,-,12</sub> |  | 4.9<br><sub>-,6,-,-,5</sub> |  | 1.9<br><sub>-,2,-,-,3</sub> |  | 1.0<br><sub>-,3,-,-,2</sub> |  | 0.5 | 0.5 | 1.2 | 15.0 |
| Terance Mann | 58% | 18.4<br><sub>-,12,15,-,16</sub> | 4.8<br><sub>-,2,0,-,0</sub> |  | 2.4<br><sub>-,0,1,-,2</sub> |  | 1.8<br><sub>-,2,1,-,2</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.9 | 8.9 |
| Josh Minott | 52% | 12.9<br><sub>-,3,-,-,6</sub> | 6.0<br><sub>-,2,-,-,0</sub> |  | 2.5<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,0,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.5 | 0.7 | 9.3 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker | 98% | 32.7<br><sub>32,31,29,31,32</sub> | 23.2<br><sub>23,25,12,34,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>1,1,1,4,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.5<br><sub>5,4,0,9,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.6 | 2.8 | 30.3 |
| Onyeka Okongwu | 98% | 32.3<br><sub>31,33,28,33,31</sub> | 15.7<br><sub>11,29,6,13,14</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 8.6<br><sub>4,12,10,10,16</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>4,2,1,3,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,4,0,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 1.0 | 1.7 | 27.5 |
| Dyson Daniels | 98% | 32.2<br><sub>28,32,27,31,34</sub> | 12.7<br><sub>7,4,8,6,8</sub> |  | 7.2<br><sub>4,6,4,9,16</sub> |  | 5.8<br><sub>7,5,3,4,8</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 2.5 | 0.5 | 1.9 | 25.6 |
| Luguentz Dort | 98% | 30.5<br><sub>24,22,29,31,31</sub> | 10.6<br><sub>8,6,11,14,6</sub> |  | 3.8<br><sub>3,3,3,2,3</sub> |  | 1.9<br><sub>3,2,0,0,3</sub> |  | 1.7<br><sub>2,1,1,4,2</sub> |  | 1.1 | 0.4 | 1.0 | 16.3 |
| CJ McCollum | 98% | 29.8<br><sub>20,31,24,32,25</sub> | 18.9<br><sub>13,5,14,13,15</sub> |  | 3.5<br><sub>2,3,2,9,5</sub> |  | 4.5<br><sub>1,8,2,12,5</sub> |  | 2.5<br><sub>1,0,2,2,2</sub> |  | 1.1 | 0.6 | 2.5 | 26.9 |
| Aaron Wiggins | 96% | 26.5<br><sub>24,24,23,24,29</sub> | 12.8<br><sub>10,20,10,7,15</sub> |  | 3.5<br><sub>4,7,2,3,4</sub> |  | 2.1<br><sub>3,3,1,2,2</sub> |  | 2.0<br><sub>2,4,2,1,3</sub> |  | 1.0 | 0.5 | 1.5 | 18.5 |
| Kingston Flemings | 80% | 22.8<br><sub>28,16,25,-,23</sub> | 8.9<br><sub>23,2,12,-,14</sub> |  | 3.4<br><sub>5,1,2,-,3</sub> |  | 4.8<br><sub>5,5,6,-,4</sub> |  | 0.7<br><sub>3,0,1,-,2</sub> |  | 0.8 | 0.4 | 1.6 | 17.1 |
| Zuby Ejiofor | 58% | 16.4<br><sub>-,-,-,15,17</sub> | 6.2<br><sub>-,-,-,3,11</sub> |  | 3.4<br><sub>-,-,-,5,3</sub> |  | 1.3<br><sub>-,-,-,2,2</sub> |  | 0.5<br><sub>-,-,-,1,1</sub> |  | 0.5 | 0.2 | 1.0 | 10.9 |
| Corey Kispert | 67% | 15.1<br><sub>-,-,5,18,8</sub> | 8.0<br><sub>-,-,0,14,9</sub> |  | 1.9<br><sub>-,-,0,1,0</sub> |  | 1.3<br><sub>-,-,1,0,1</sub> |  | 1.1<br><sub>-,-,0,4,1</sub> |  | 0.3 | 0.2 | 0.8 | 11.2 |
| Jalen Wilson | 16% | 12.9 | 5.5 |  | 2.1 |  | 1.0 |  | 0.5 |  | 0.4 | 0.1 | 0.7 | 8.7 |
| RayJ Dennis | 72% | 12.0<br><sub>-,-,-,8,-</sub> | 4.0<br><sub>-,-,-,4,-</sub> |  | 1.6<br><sub>-,-,-,2,-</sub> |  | 2.0<br><sub>-,-,-,2,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.8 | 7.6 |
| Dorian Finney-Smith | 43% | 8.6<br><sub>-,-,3,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>if Day'Ron Sharpe plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker (ATL) | 98% | 32.7<br><sub>32,31,29,31,32</sub> | 23.1<br><sub>23,25,12,34,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>1,1,1,4,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.5<br><sub>5,4,0,9,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.6 | 2.7 | 30.2 |
| Onyeka Okongwu (ATL) | 98% | 32.3<br><sub>31,33,28,33,31</sub> | 15.5<br><sub>11,29,6,13,14</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 8.5<br><sub>4,12,10,10,16</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,2,1,3,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,4,0,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 1.0 | 1.7 | 27.3 |
| Dyson Daniels (ATL) | 98% | 32.1<br><sub>28,32,27,31,34</sub> | 12.6<br><sub>7,4,8,6,8</sub> |  | 7.2<br><sub>4,6,4,9,16</sub> |  | 5.8<br><sub>7,5,3,4,8</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 2.5 | 0.5 | 1.9 | 25.5 |
| Luguentz Dort (ATL) | 98% | 30.5<br><sub>24,22,29,31,31</sub> | 10.6<br><sub>8,6,11,14,6</sub> |  | 3.8<br><sub>3,3,3,2,3</sub> |  | 1.9<br><sub>3,2,0,0,3</sub> |  | 1.7<br><sub>2,1,1,4,2</sub> |  | 1.1 | 0.4 | 1.0 | 16.3 |
| CJ McCollum (ATL) | 98% | 29.8<br><sub>20,31,24,32,25</sub> | 18.9<br><sub>13,5,14,13,15</sub> |  | 3.5<br><sub>2,3,2,9,5</sub> |  | 4.4<br><sub>1,8,2,12,5</sub> |  | 2.4<br><sub>1,0,2,2,2</sub> |  | 1.1 | 0.6 | 2.5 | 26.9 |
| Aaron Wiggins (ATL) | 96% | 26.6<br><sub>24,24,23,24,29</sub> | 12.8<br><sub>10,20,10,7,15</sub> |  | 3.5<br><sub>4,7,2,3,4</sub> |  | 2.1<br><sub>3,3,1,2,2</sub> |  | 2.0<br><sub>2,4,2,1,3</sub> |  | 1.0 | 0.5 | 1.5 | 18.5 |
| Kingston Flemings (ATL) | 80% | 22.8<br><sub>28,16,25,-,23</sub> | 8.9<br><sub>23,2,12,-,14</sub> |  | 3.3<br><sub>5,1,2,-,3</sub> |  | 4.8<br><sub>5,5,6,-,4</sub> |  | 0.7<br><sub>3,0,1,-,2</sub> |  | 0.8 | 0.4 | 1.6 | 17.0 |
| Zuby Ejiofor (ATL) | 58% | 16.5<br><sub>-,-,-,15,17</sub> | 6.2<br><sub>-,-,-,3,11</sub> |  | 3.4<br><sub>-,-,-,5,3</sub> |  | 1.3<br><sub>-,-,-,2,2</sub> |  | 0.5<br><sub>-,-,-,1,1</sub> |  | 0.6 | 0.2 | 1.0 | 10.9 |
| Corey Kispert (ATL) | 67% | 15.0<br><sub>-,-,5,18,8</sub> | 7.9<br><sub>-,-,0,14,9</sub> |  | 1.9<br><sub>-,-,0,1,0</sub> |  | 1.3<br><sub>-,-,1,0,1</sub> |  | 1.1<br><sub>-,-,0,4,1</sub> |  | 0.3 | 0.2 | 0.8 | 11.1 |
| Jalen Wilson (ATL) | 16% | 13.2 | 5.4 |  | 2.1 |  | 1.1 |  | 0.5 |  | 0.4 | 0.1 | 0.7 | 8.6 |
| RayJ Dennis (ATL) | 72% | 11.8<br><sub>-,-,-,8,-</sub> | 4.0<br><sub>-,-,-,4,-</sub> |  | 1.6<br><sub>-,-,-,2,-</sub> |  | 1.9<br><sub>-,-,-,2,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.8 | 7.5 |
| Dorian Finney-Smith (ATL) | 43% | 8.6<br><sub>-,-,3,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.0 |
| Michael Porter Jr. (BKN) | 98% | 33.9<br><sub>40,26,36,37,38</sub> | 21.4<br><sub>27,13,23,18,26</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>12,7,9,5,10</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,1,3,2,0</sub> |  | 3.0<br><sub>6,2,3,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.4 | 2.4 | 31.3 |
| Julius Randle (BKN) | 98% | 33.3<br><sub>44,25,37,36,31</sub> | 19.8<br><sub>24,15,20,21,22</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>9,8,5,11,3</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>4,3,6,2,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>0,3,4,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 3.5 | 31.3 |
| Nolan Traore (BKN) | 98% | 24.6<br><sub>24,26,30,24,27</sub> | 11.2<br><sub>15,9,16,17,16</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,2,2,3,4</sub> |  | 3.8<br><sub>3,2,6,4,2</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,0,4,5,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.5 | 2.8 | 17.4 |
| Mikel Brown Jr. (BKN) | 96% | 24.1<br><sub>28,23,-,27,20</sub> | 10.9<br><sub>17,10,-,13,18</sub> |  | 2.8<br><sub>5,0,-,2,2</sub> |  | 3.7<br><sub>5,4,-,3,4</sub> |  | 1.5<br><sub>4,0,-,1,3</sub> |  | 0.7 | 0.3 | 2.1 | 17.5 |
| Day'Ron Sharpe (BKN) | 100% | 22.9<br><sub>17,24,26,22,27</sub> | 9.1<br><sub>4,3,15,4,6</sub> | 8.5 · – | 7.9<br><sub>6,7,13,6,5</sub> | 8.5 | 2.9<br><sub>0,1,4,3,8</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 1.0 | 0.8 | 2.0 | 19.8 |
| Noah Clowney (BKN) | 98% | 20.9<br><sub>24,22,24,20,17</sub> | 7.8<br><sub>3,3,8,2,7</sub> |  | 3.7<br><sub>4,8,3,6,1</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.6 | 0.5 | 1.0 | 12.7 |
| Chaney Johnson (BKN) | 93% | 19.4<br><sub>29,19,31,28,9</sub> | 5.7<br><sub>15,6,2,4,0</sub> |  | 2.7<br><sub>3,2,2,3,2</sub> |  | 1.1<br><sub>2,0,0,2,1</sub> |  | 0.6<br><sub>3,0,0,1,0</sub> |  | 0.6 | 0.4 | 1.0 | 9.5 |
| Keon Ellis (BKN) | 96% | 18.9<br><sub>25,21,20,25,10</sub> | 5.0<br><sub>2,6,0,5,1</sub> |  | 1.9<br><sub>3,2,2,1,2</sub> |  | 1.2<br><sub>4,1,1,0,0</sub> |  | 0.6<br><sub>0,2,0,1,0</sub> |  | 0.9 | 0.6 | 0.7 | 8.2 |
| Moritz Wagner (BKN) | 93% | 18.9<br><sub>22,23,21,20,20</sub> | 9.6<br><sub>15,16,14,6,6</sub> |  | 4.7<br><sub>4,8,6,1,1</sub> |  | 1.3<br><sub>3,1,0,2,0</sub> |  | 0.7<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.3 | 1.1 | 15.6 |
| Danny Wolf (BKN) | 52% | 16.9<br><sub>-,12,-,-,19</sub> | 7.3<br><sub>-,9,-,-,12</sub> |  | 4.2<br><sub>-,6,-,-,5</sub> |  | 1.7<br><sub>-,2,-,-,3</sub> |  | 0.8<br><sub>-,3,-,-,2</sub> |  | 0.5 | 0.4 | 1.0 | 13.2 |
| Terance Mann (BKN) | 58% | 16.5<br><sub>-,12,15,-,16</sub> | 4.4<br><sub>-,2,0,-,0</sub> |  | 2.1<br><sub>-,0,1,-,2</sub> |  | 1.6<br><sub>-,2,1,-,2</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.8 | 8.0 |
| Josh Minott (BKN) | 52% | 11.7<br><sub>-,3,-,-,6</sub> | 5.6<br><sub>-,2,-,-,0</sub> |  | 2.2<br><sub>-,0,-,-,1</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.4 | 0.6 | 8.5 |

</details>


### NYK @ CLE
Out: Jarrett Allen (CLE), Sam Merrill (CLE), Jaylon Tyson (CLE), Josh Hart (NYK)

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 37.0<br><sub>36,35,35,34,28</sub> | 26.5<br><sub>23,38,24,19,33</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>1,1,5,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.4<br><sub>7,7,6,6,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>0,6,3,4,5</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 2.6 | 36.2 |
| OG Anunoby | 98% | 35.6<br><sub>36,31,34,38,24</sub> | 18.4<br><sub>13,23,9,18,18</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>7,6,4,4,5</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,1,3,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>1,2,1,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.8 | 1.6 | 26.5 |
| Karl-Anthony Towns | 98% | 33.7<br><sub>33,28,35,35,25</sub> | 19.2<br><sub>27,19,22,11,17</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 13.2<br><sub>20,13,12,16,12</sub> | 12.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>3,5,3,5,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,3,3,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.7 | 2.9 | 36.1 |
| Mikal Bridges | 98% | 28.6<br><sub>32,13,30,16,22</sub> | 9.6<br><sub>12,3,12,6,7</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>3,0,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.5<br><sub>4,0,2,0,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>4,1,2,0,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.4 | 1.0 | 15.2 |
| Landry Shamet | 98% | 27.4<br><sub>28,32,16,30,25</sub> | 9.9<br><sub>13,14,0,22,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,1,0,1,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>3,5,0,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>3,4,0,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.7 | 0.2 | 0.8 | 13.5 |
| Miles McBride | 98% | 20.6<br><sub>17,14,24,17,11</sub> | 7.6<br><sub>5,3,10,6,7</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,5,3,1,1</sub> |  | 1.6<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.6 | 11.1 |
| Jordan Clarkson | 88% | 15.1<br><sub>-,17,9,11,15</sub> | 7.2<br><sub>-,18,4,7,10</sub> |  | 2.0<br><sub>-,3,3,0,1</sub> |  | 1.0<br><sub>-,1,0,0,1</sub> |  | 0.6<br><sub>-,2,0,1,2</sub> |  | 0.4 | 0.1 | 0.8 | 10.2 |
| Jose Alvarado | 97% | 14.6<br><sub>-,-,-,9,9</sub> | 5.0<br><sub>-,-,-,0,0</sub> |  | 1.8<br><sub>-,-,-,0,0</sub> |  | 2.2<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.8 | 0.1 | 0.8 | 9.0 |
| Tyler Kolek | 86% | 14.6<br><sub>11,18,13,5,11</sub> | 4.3<br><sub>2,9,2,2,0</sub> |  | 1.8<br><sub>1,2,1,1,0</sub> |  | 3.6<br><sub>3,9,4,1,5</sub> |  | 0.5<br><sub>0,3,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 9.7 |
| Andre Drummond | 98% | 14.4<br><sub>14,15,12,13,12</sub> | 4.9<br><sub>10,4,3,4,6</sub> |  | 6.5<br><sub>8,11,6,9,9</sub> |  | 1.1<br><sub>1,1,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 12.4 |
| Mohamed Diawara | 52% | 13.1<br><sub>1,-,-,6,21</sub> | 4.3<br><sub>0,-,-,0,8</sub> |  | 2.3<br><sub>0,-,-,1,6</sub> |  | 1.2<br><sub>0,-,-,0,4</sub> |  | 0.5<br><sub>0,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.6 | 7.8 |
| Dalton Knecht | 52% | 12.6<br><sub>-,-,-,-,16</sub> | 5.5<br><sub>-,-,-,-,10</sub> |  | 2.5<br><sub>-,-,-,-,7</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,2</sub> |  | 0.3 | 0.2 | 0.4 | 8.8 |
| James Wiseman | 52% | 8.7<br><sub>1,-,-,-,10</sub> | 2.9<br><sub>0,-,-,-,8</sub> |  | 2.8<br><sub>1,-,-,-,8</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.6 | 6.1 |
| Jaden Akins | 38% | 8.7<br><sub>2,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.3 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Pacome Dadiet | 48% | 8.3<br><sub>1,-,-,-,9</sub> | 3.1<br><sub>0,-,-,-,4</sub> |  | 1.6<br><sub>1,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.9<br><sub>34,36,26,33,35</sub> | 17.9<br><sub>16,24,13,14,19</sub> |  | 4.9<br><sub>2,5,6,4,9</sub> |  | 6.4<br><sub>6,4,7,6,6</sub> |  | 2.5<br><sub>2,3,3,3,3</sub> |  | 1.2 | 0.6 | 3.6 | 29.3 |
| Donovan Mitchell | 98% | 36.8<br><sub>31,33,24,36,33</sub> | 24.0<br><sub>19,22,15,17,27</sub> |  | 5.0<br><sub>5,3,4,5,3</sub> |  | 5.0<br><sub>7,3,3,11,6</sub> |  | 2.8<br><sub>2,1,2,4,5</sub> |  | 1.3 | 0.4 | 3.0 | 34.0 |
| Evan Mobley | 98% | 35.8<br><sub>32,33,25,33,33</sub> | 17.3<br><sub>24,11,27,16,16</sub> |  | 8.5<br><sub>12,4,5,7,10</sub> |  | 3.6<br><sub>2,7,3,4,3</sub> |  | 1.6<br><sub>5,0,3,1,1</sub> |  | 0.8 | 1.8 | 1.9 | 29.5 |
| Peyton Watson | 98% | 30.3<br><sub>28,22,22,-,-</sub> | 12.6<br><sub>22,4,5,-,-</sub> |  | 4.5<br><sub>6,4,2,-,-</sub> |  | 2.3<br><sub>2,3,6,-,-</sub> |  | 1.4<br><sub>1,0,1,-,-</sub> |  | 0.9 | 1.4 | 1.8 | 19.4 |
| Meleek Thomas | 84% | 24.4<br><sub>20,-,23,26,18</sub> | 10.4<br><sub>10,-,13,17,9</sub> |  | 3.0<br><sub>4,-,1,5,1</sub> |  | 1.2<br><sub>1,-,2,1,0</sub> |  | 1.7<br><sub>0,-,3,3,3</sub> |  | 0.9 | 0.3 | 1.1 | 14.6 |
| Mario Hezonja | 97% | 23.8<br><sub>17,17,20,27,23</sub> | 9.0<br><sub>5,10,8,12,12</sub> |  | 5.7<br><sub>3,6,11,8,8</sub> |  | 1.8<br><sub>2,2,4,3,1</sub> |  | 1.2<br><sub>1,2,1,3,2</sub> |  | 0.7 | 0.3 | 0.9 | 16.4 |
| Tyrese Proctor | 88% | 22.8<br><sub>6,20,18,19,22</sub> | 8.6<br><sub>2,7,9,10,11</sub> |  | 3.0<br><sub>1,6,4,4,1</sub> |  | 2.5<br><sub>1,2,5,2,0</sub> |  | 1.4<br><sub>0,1,3,2,2</sub> |  | 0.9 | 0.1 | 1.0 | 14.0 |
| Craig Porter Jr. | 80% | 15.2<br><sub>-,4,16,8,14</sub> | 3.5<br><sub>-,0,2,0,0</sub> |  | 2.6<br><sub>-,1,2,4,1</sub> |  | 2.1<br><sub>-,0,4,1,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.5 | 0.8 | 8.2 |
| Tristan Enaruna | 52% | 14.5<br><sub>-,-,6,-,16</sub> | 5.1<br><sub>-,-,2,-,4</sub> |  | 2.3<br><sub>-,-,1,-,4</sub> |  | 0.8<br><sub>-,-,0,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 8.3 |
| Thomas Bryant | 58% | 14.4<br><sub>-,-,11,5,13</sub> | 6.6<br><sub>-,-,11,4,8</sub> |  | 3.4<br><sub>-,-,2,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,3,0,1</sub> |  | 0.3 | 0.5 | 0.7 | 10.5 |
| Norchad Omier | 16% | 8.8 | 2.8 |  | 1.8 |  | 0.7 |  | 0.1 |  | 0.2 | 0.2 | 0.6 | 5.3 |
| Ernest Udeh Jr. | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |

</details>


### WAS @ OKC
Out: Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC), Justin Champagnie (WAS), Anthony Davis (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.2<br><sub>38,34,38,34,34</sub> | 19.5<br><sub>22,14,21,15,18</sub> |  | 3.6<br><sub>6,5,7,3,2</sub> |  | 9.8<br><sub>10,8,9,9,6</sub> |  | 2.3<br><sub>1,1,1,2,2</sub> |  | 1.1 | 0.2 | 4.0 | 32.9 |
| Kyshawn George | 98% | 34.0<br><sub>29,38,32,37,35</sub> | 18.0<br><sub>20,8,12,22,25</sub> |  | 5.8<br><sub>4,2,3,4,4</sub> |  | 4.8<br><sub>2,11,3,5,7</sub> |  | 2.4<br><sub>2,0,4,4,3</sub> |  | 1.1 | 0.9 | 2.9 | 28.5 |
| AJ Dybantsa | 93% | 32.6<br><sub>-,27,30,33,32</sub> | 15.8<br><sub>-,19,17,21,9</sub> |  | 5.8<br><sub>-,2,8,5,6</sub> |  | 2.2<br><sub>-,2,1,2,3</sub> |  | 1.2<br><sub>-,1,1,1,0</sub> |  | 1.0 | 0.3 | 2.1 | 23.9 |
| Bilal Coulibaly | 98% | 27.3<br><sub>29,27,22,33,23</sub> | 10.5<br><sub>3,17,1,7,6</sub> |  | 4.2<br><sub>5,2,5,1,2</sub> |  | 1.9<br><sub>1,0,1,2,2</sub> |  | 0.9<br><sub>0,1,0,0,0</sub> |  | 1.1 | 0.9 | 1.3 | 16.6 |
| Alex Sarr | 97% | 26.5<br><sub>26,26,29,-,23</sub> | 12.4<br><sub>12,18,3,-,11</sub> |  | 6.9<br><sub>6,4,8,-,9</sub> |  | 2.4<br><sub>1,2,0,-,1</sub> |  | 1.0<br><sub>0,2,1,-,0</sub> |  | 0.8 | 1.4 | 1.7 | 21.7 |
| Bub Carrington | 98% | 22.9<br><sub>28,20,20,19,19</sub> | 8.3<br><sub>6,3,9,3,0</sub> |  | 2.6<br><sub>0,1,4,4,1</sub> |  | 3.3<br><sub>3,3,2,4,2</sub> |  | 1.2<br><sub>2,0,3,1,0</sub> |  | 0.5 | 0.2 | 1.7 | 14.2 |
| Tre Johnson | 86% | 20.1<br><sub>23,-,13,22,14</sub> | 8.3<br><sub>7,-,4,4,3</sub> |  | 2.4<br><sub>3,-,2,3,2</sub> |  | 1.0<br><sub>2,-,0,0,0</sub> |  | 1.1<br><sub>1,-,0,0,1</sub> |  | 0.6 | 0.2 | 1.2 | 11.7 |
| Deandre Ayton | 98% | 17.3<br><sub>12,12,17,24,11</sub> | 5.9<br><sub>0,10,3,4,5</sub> |  | 5.2<br><sub>4,3,3,6,4</sub> |  | 0.7<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.9 | 11.8 |
| Khris Middleton | 58% | 14.9<br><sub>13,23,5,-,-</sub> | 5.2<br><sub>0,4,0,-,-</sub> |  | 2.4<br><sub>1,3,0,-,-</sub> |  | 1.1<br><sub>0,2,0,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.4 | 0.1 | 1.2 | 8.6 |
| Will Riley | 83% | 13.8<br><sub>4,-,1,4,13</sub> | 6.2<br><sub>2,-,0,0,0</sub> |  | 1.9<br><sub>0,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,1,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 1.0 | 9.2 |
| Anthony Gill | 35% | 12.7<br><sub>-,-,-,-,-</sub> | 4.6<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.8 |
| Tre Mann | 52% | 8.2<br><sub>-,-,1,-,3</sub> | 3.4<br><sub>-,-,0,-,2</sub> |  | 1.1<br><sub>-,-,0,-,0</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Felix Okpara | 52% | 7.9<br><sub>-,-,-,-,3</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.2 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 32.8<br><sub>30,28,31,39,35</sub> | 32.4<br><sub>26,21,26,43,42</sub> | 31.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 7.0<br><sub>3,2,3,8,8</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>1,1,3,4,5</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.6 | 0.9 | 2.6 | 43.8 |
| Ajay Mitchell | 98% | 29.8<br><sub>25,28,26,35,32</sub> | 18.2<br><sub>30,29,6,20,23</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>2,4,3,5,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.7<br><sub>5,3,5,1,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.1<br><sub>1,2,0,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.5 | 0.3 | 1.8 | 27.0 |
| Jared McCain | 98% | 26.6<br><sub>30,29,28,27,25</sub> | 14.6<br><sub>18,10,10,7,9</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>3,4,4,9,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>4,4,2,2,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>4,0,0,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.1 | 1.4 | 20.0 |
| Isaiah Hartenstein | 98% | 26.2<br><sub>26,26,25,28,26</sub> | 10.4<br><sub>15,10,10,5,3</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 10.7<br><sub>13,14,7,14,12</sub> | 9.5<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>3,3,0,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.9 | 1.5 | 24.6 |
| Kenrich Williams | 96% | 25.3<br><sub>24,17,21,31,29</sub> | 10.3<br><sub>3,7,11,12,13</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>7,3,7,3,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,0,3,1,2</sub> |  | 1.4<br><sub>0,1,3,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.2 | 1.0 | 18.1 |
| Aday Mara | 97% | 24.0<br><sub>20,21,28,20,25</sub> | 8.6<br><sub>11,6,7,10,9</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>10,3,9,9,5</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>2,1,3,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 2.0 | 1.7 | 17.4 |
| Bennett Stirtz | 97% | 22.1<br><sub>25,28,26,12,22</sub> | 7.5<br><sub>7,8,11,9,16</sub> |  | 2.0<br><sub>1,0,1,2,1</sub> |  | 1.6<br><sub>1,3,3,0,1</sub> |  | 1.2<br><sub>1,1,3,3,4</sub> |  | 0.7 | 0.1 | 0.8 | 11.1 |
| Alex Caruso | 98% | 21.8<br><sub>9,-,-,-,20</sub> | 9.1<br><sub>9,-,-,-,7</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>2,-,-,-,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,-,-,-,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>3,-,-,-,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.4 | 0.9 | 15.5 |
| Micah Peavy | 72% | 21.2<br><sub>-,5,14,16,26</sub> | 5.3<br><sub>-,0,2,8,2</sub> |  | 4.4<br><sub>-,0,1,5,9</sub> |  | 1.2<br><sub>-,0,0,0,1</sub> |  | 0.5<br><sub>-,0,0,2,0</sub> |  | 0.7 | 0.2 | 0.8 | 10.9 |
| Josh Dix | 64% | 15.2<br><sub>22,24,9,12,-</sub> | 5.2<br><sub>0,2,7,0,-</sub> |  | 1.4<br><sub>1,2,0,1,-</sub> |  | 0.8<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.5 | 0.2 | 0.4 | 7.3 |
| Dalen Terry | 52% | 9.8<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.5 | 6.0 |
| Brooks Barnhizer | 52% | 9.6<br><sub>3,14,6,-,-</sub> | 2.6<br><sub>0,3,5,-,-</sub> |  | 2.1<br><sub>0,2,2,-,-</sub> |  | 0.7<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 5.4 |

</details>


### ORL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.9–114.6 | ORL 34% | 2.96 / 1.51 | GSW -5.5 | 223.5 | GSW -6.5 covers 48%; o221.5 54% |
| Expected (weighted by chance each plays) | 108.8–115.5 | ORL 31% | 3.27 / 1.44 | GSW -6.5 | 224.5 | GSW -6.5 covers 51%; o221.5 56% |
| if Draymond Green plays | 108.5–115.4 | ORL 31% | 3.25 / 1.45 | GSW -7.5 | 223.5 | GSW -6.5 covers 52%; o221.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 19.2 | 7.8 | 3.7 | 1.8 | 0.8 | 0.8 | 0.3 | 1.2 | 13.3 | small |
| Gary Payton II (GSW) | Questionable | 55% | 15.2 | 6.2 | 2.8 | 1.1 | 0.4 | 0.9 | 0.2 | 0.7 | 10.1 | small |
| Draymond Green (GSW) | Questionable | 55% | 27.0 | 6.7 | 5.1 | 5.3 | 0.8 | 1.1 | 0.8 | 2.2 | 17.2 | full tables below |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 35.2<br><sub>34,39,40,38,38</sub> | 21.7<br><sub>15,26,14,24,15</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>4,5,6,3,8</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>5,11,12,6,15</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,1,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.4 | 3.5 | 34.6 |
| Desmond Bane | 98% | 34.7<br><sub>34,39,40,36,32</sub> | 20.5<br><sub>13,28,19,20,15</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,2,2,3,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>4,6,1,3,0</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.8<br><sub>2,6,5,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.5 | 2.6 | 28.6 |
| Wendell Carter Jr. | 98% | 32.5<br><sub>26,39,35,34,34</sub> | 12.5<br><sub>3,20,7,6,27</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 8.3<br><sub>10,7,10,9,13</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>3,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>0,1,1,0,2</sub> |  | 1.1 | 0.7 | 1.8 | 23.0 |
| Anthony Black | 98% | 30.6<br><sub>22,31,33,-,31</sub> | 14.9<br><sub>8,17,23,-,10</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,6,8,-,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.4<br><sub>1,10,3,-,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,3,1,-,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.8 | 0.6 | 2.4 | 23.4 |
| Tristan da Silva | 98% | 29.7<br><sub>31,23,35,32,30</sub> | 12.7<br><sub>20,8,23,10,18</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,0,10,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,2,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>4,2,5,2,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 1.5 | 18.9 |
| Jase Richardson | 91% | 24.6<br><sub>14,33,26,29,26</sub> | 9.1<br><sub>10,4,4,9,10</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,6,1,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,2,3,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>2,0,0,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 1.2 | 14.2 |
| Jamal Cain | 98% | 22.8<br><sub>16,15,18,25,25</sub> | 8.7<br><sub>9,13,5,10,5</sub> |  | 3.5<br><sub>1,0,1,3,5</sub> |  | 1.3<br><sub>0,0,1,1,0</sub> |  | 1.0<br><sub>0,3,1,2,1</sub> |  | 0.7 | 0.2 | 1.2 | 13.6 |
| Jevon Carter | 63% | 12.9<br><sub>22,-,-,18,3</sub> | 4.2<br><sub>6,-,-,5,0</sub> |  | 1.2<br><sub>0,-,-,1,0</sub> |  | 1.4<br><sub>3,-,-,4,0</sub> |  | 0.6<br><sub>2,-,-,1,0</sub> |  | 0.6 | 0.1 | 0.5 | 6.8 |
| Nikola Vucevic | 98% | 11.2<br><sub>16,6,7,14,4</sub> | 4.6<br><sub>5,3,2,7,0</sub> |  | 3.1<br><sub>4,1,4,6,0</sub> |  | 1.3<br><sub>2,0,2,1,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.3 | 0.5 | 8.9 |
| Goga Bitadze | 67% | 11.0<br><sub>11,6,5,-,8</sub> | 4.3<br><sub>6,2,0,-,4</sub> |  | 3.5<br><sub>0,4,1,-,5</sub> |  | 0.8<br><sub>1,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.6 | 0.7 | 8.7 |
| Alex Morales | 67% | 10.3<br><sub>7,9,-,14,6</sub> | 2.9<br><sub>2,0,-,3,0</sub> |  | 1.4<br><sub>2,1,-,2,0</sub> |  | 0.8<br><sub>1,0,-,0,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 5.1 |
| Colin Castleton | 52% | 6.8<br><sub>7,-,-,-,2</sub> | 2.4<br><sub>2,-,-,-,0</sub> |  | 1.9<br><sub>2,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,1</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.8 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 91% | 33.7<br><sub>32,33,37,33,32</sub> | 15.9<br><sub>8,21,17,20,9</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>5,5,8,3,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>6,6,8,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>0,4,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.3 | 1.7 | 25.9 |
| Yaxel Lendeborg | 98% | 33.2<br><sub>35,24,34,29,30</sub> | 20.1<br><sub>26,6,37,16,17</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>9,1,4,5,8</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.4<br><sub>1,0,6,5,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>2,1,6,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.6 | 2.9 | 31.3 |
| Stephen Curry | 98% | 32.2<br><sub>32,31,-,33,28</sub> | 26.4<br><sub>44,31,-,34,29</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>8,4,-,6,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.3<br><sub>6,6,-,7,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>6,8,-,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.4 | 2.9 | 35.5 |
| De'Anthony Melton | 98% | 25.3<br><sub>20,21,28,28,17</sub> | 10.8<br><sub>8,16,21,2,5</sub> |  | 4.3<br><sub>6,5,6,7,6</sub> |  | 2.8<br><sub>0,3,3,2,2</sub> |  | 1.6<br><sub>2,4,6,0,0</sub> |  | 1.6 | 0.5 | 1.7 | 17.8 |
| Georges Niang | 97% | 24.1<br><sub>23,19,21,22,22</sub> | 9.2<br><sub>7,11,3,13,13</sub> |  | 3.4<br><sub>3,5,1,4,4</sub> |  | 1.5<br><sub>2,1,2,3,3</sub> |  | 1.6<br><sub>1,3,1,1,2</sub> |  | 0.6 | 0.2 | 1.1 | 14.2 |
| Brandon Williams | 80% | 22.4<br><sub>14,17,25,-,21</sub> | 12.5<br><sub>11,9,17,-,10</sub> |  | 3.0<br><sub>3,2,3,-,1</sub> |  | 3.6<br><sub>1,1,3,-,4</sub> |  | 0.7<br><sub>0,0,2,-,0</sub> |  | 0.9 | 0.4 | 1.9 | 19.0 |
| Al Horford | 98% | 21.9<br><sub>18,17,22,-,18</sub> | 6.7<br><sub>4,3,9,-,8</sub> |  | 4.8<br><sub>5,2,5,-,5</sub> |  | 1.9<br><sub>2,0,2,-,1</sub> |  | 1.0<br><sub>0,1,3,-,2</sub> |  | 0.6 | 0.9 | 0.7 | 13.3 |
| Will Richard | 98% | 21.5<br><sub>23,13,22,28,16</sub> | 5.6<br><sub>6,3,3,6,10</sub> |  | 2.5<br><sub>3,3,0,5,0</sub> |  | 1.3<br><sub>0,2,3,0,2</sub> |  | 0.7<br><sub>0,1,1,2,2</sub> |  | 1.0 | 0.2 | 0.6 | 9.4 |
| Charles Bassey | 96% | 16.1<br><sub>2,9,20,23,14</sub> | 6.7<br><sub>0,6,6,19,8</sub> |  | 6.1<br><sub>0,4,10,8,7</sub> |  | 0.8<br><sub>0,1,2,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.9 | 13.6 |
| Graham Ike | 88% | 13.0<br><sub>-,-,6,7,1</sub> | 4.8<br><sub>-,-,2,0,0</sub> |  | 3.0<br><sub>-,-,2,0,1</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 8.6 |
| LJ Cryer | 71% | 9.9<br><sub>-,-,2,1,1</sub> | 4.1<br><sub>-,-,0,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.9 |
| Malevy Leons | 52% | 9.8<br><sub>-,-,-,-,1</sub> | 2.8<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 5.3 |

</details>

<details><summary>if Draymond Green plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 91% | 32.8<br><sub>32,33,37,33,32</sub> | 16.1<br><sub>8,21,17,20,9</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,5,8,3,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>6,6,8,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>0,4,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.3 | 1.7 | 25.4 |
| Yaxel Lendeborg (GSW) | 98% | 32.2<br><sub>35,24,34,29,30</sub> | 19.8<br><sub>26,6,37,16,17</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>9,1,4,5,8</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>1,0,6,5,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,6,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.6 | 2.7 | 30.1 |
| Stephen Curry (GSW) | 98% | 31.1<br><sub>32,31,-,33,28</sub> | 26.1<br><sub>44,31,-,34,29</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>8,4,-,6,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.6<br><sub>6,6,-,7,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>6,8,-,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 2.8 | 34.5 |
| Draymond Green (GSW) | 100% | 27.0<br><sub>32,32,-,17,27</sub> | 6.7<br><sub>3,2,-,4,2</sub> | 5.5 · – | 5.1<br><sub>9,4,-,4,5</sub> | 5.5 | 5.3<br><sub>6,9,-,2,11</sub> | 6.5 | 0.8<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.8 | 2.2 | 17.2 |
| De'Anthony Melton (GSW) | 98% | 22.5<br><sub>20,21,28,28,17</sub> | 9.8<br><sub>8,16,21,2,5</sub> |  | 3.7<br><sub>6,5,6,7,6</sub> |  | 2.3<br><sub>0,3,3,2,2</sub> |  | 1.4<br><sub>2,4,6,0,0</sub> |  | 1.4 | 0.4 | 1.5 | 15.8 |
| Georges Niang (GSW) | 97% | 21.3<br><sub>23,19,21,22,22</sub> | 8.6<br><sub>7,11,3,13,13</sub> |  | 3.1<br><sub>3,5,1,4,4</sub> |  | 1.3<br><sub>2,1,2,3,3</sub> |  | 1.4<br><sub>1,3,1,1,2</sub> |  | 0.5 | 0.2 | 1.0 | 13.0 |
| Brandon Williams (GSW) | 80% | 20.2<br><sub>14,17,25,-,21</sub> | 11.3<br><sub>11,9,17,-,10</sub> |  | 2.7<br><sub>3,2,3,-,1</sub> |  | 3.0<br><sub>1,1,3,-,4</sub> |  | 0.7<br><sub>0,0,2,-,0</sub> |  | 0.8 | 0.4 | 1.7 | 16.9 |
| Al Horford (GSW) | 98% | 19.0<br><sub>18,17,22,-,18</sub> | 6.2<br><sub>4,3,9,-,8</sub> |  | 4.1<br><sub>5,2,5,-,5</sub> |  | 1.5<br><sub>2,0,2,-,1</sub> |  | 0.9<br><sub>0,1,3,-,2</sub> |  | 0.5 | 0.8 | 0.6 | 11.7 |
| Will Richard (GSW) | 98% | 18.3<br><sub>23,13,22,28,16</sub> | 5.0<br><sub>6,3,3,6,10</sub> |  | 2.1<br><sub>3,3,0,5,0</sub> |  | 1.0<br><sub>0,2,3,0,2</sub> |  | 0.6<br><sub>0,1,1,2,2</sub> |  | 0.9 | 0.2 | 0.5 | 8.2 |
| Charles Bassey (GSW) | 96% | 14.4<br><sub>2,9,20,23,14</sub> | 6.1<br><sub>0,6,6,19,8</sub> |  | 5.3<br><sub>0,4,10,8,7</sub> |  | 0.7<br><sub>0,1,2,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.8 | 12.2 |
| Graham Ike (GSW) | 88% | 9.1<br><sub>-,-,6,7,1</sub> | 3.6<br><sub>-,-,2,0,0</sub> |  | 2.1<br><sub>-,-,2,0,1</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.2 |
| LJ Cryer (GSW) | 71% | 7.6<br><sub>-,-,2,1,1</sub> | 3.5<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.0 | 0.4 | 4.9 |
| Malevy Leons (GSW) | 52% | 7.2<br><sub>-,-,-,-,1</sub> | 2.2<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 4.0 |
| Franz Wagner (ORL) | 98% | 35.2<br><sub>34,39,40,38,38</sub> | 21.7<br><sub>15,26,14,24,15</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>4,5,6,3,8</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>5,11,12,6,15</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,1,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.3 | 3.4 | 34.6 |
| Desmond Bane (ORL) | 98% | 34.8<br><sub>34,39,40,36,32</sub> | 20.5<br><sub>13,28,19,20,15</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,2,2,3,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>4,6,1,3,0</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.8<br><sub>2,6,5,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.5 | 2.6 | 28.6 |
| Wendell Carter Jr. (ORL) | 98% | 32.5<br><sub>26,39,35,34,34</sub> | 12.5<br><sub>3,20,7,6,27</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 8.3<br><sub>10,7,10,9,13</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>0,1,1,0,2</sub> |  | 1.1 | 0.7 | 1.8 | 22.9 |
| Anthony Black (ORL) | 98% | 30.7<br><sub>22,31,33,-,31</sub> | 15.0<br><sub>8,17,23,-,10</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,6,8,-,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>1,10,3,-,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,3,1,-,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.8 | 0.6 | 2.4 | 23.5 |
| Tristan da Silva (ORL) | 98% | 29.7<br><sub>31,23,35,32,30</sub> | 12.7<br><sub>20,8,23,10,18</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,0,10,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,2,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>4,2,5,2,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 1.5 | 18.8 |
| Jase Richardson (ORL) | 91% | 24.6<br><sub>14,33,26,29,26</sub> | 9.0<br><sub>10,4,4,9,10</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,6,1,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,2,3,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>2,0,0,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 1.2 | 14.2 |
| Jamal Cain (ORL) | 98% | 22.9<br><sub>16,15,18,25,25</sub> | 8.7<br><sub>9,13,5,10,5</sub> |  | 3.5<br><sub>1,0,1,3,5</sub> |  | 1.3<br><sub>0,0,1,1,0</sub> |  | 1.0<br><sub>0,3,1,2,1</sub> |  | 0.7 | 0.3 | 1.2 | 13.5 |
| Jevon Carter (ORL) | 63% | 12.9<br><sub>22,-,-,18,3</sub> | 4.2<br><sub>6,-,-,5,0</sub> |  | 1.2<br><sub>0,-,-,1,0</sub> |  | 1.4<br><sub>3,-,-,4,0</sub> |  | 0.6<br><sub>2,-,-,1,0</sub> |  | 0.6 | 0.1 | 0.5 | 6.8 |
| Nikola Vucevic (ORL) | 98% | 11.2<br><sub>16,6,7,14,4</sub> | 4.6<br><sub>5,3,2,7,0</sub> |  | 3.1<br><sub>4,1,4,6,0</sub> |  | 1.3<br><sub>2,0,2,1,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.9 |
| Goga Bitadze (ORL) | 67% | 11.0<br><sub>11,6,5,-,8</sub> | 4.2<br><sub>6,2,0,-,4</sub> |  | 3.6<br><sub>0,4,1,-,5</sub> |  | 0.8<br><sub>1,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.6 | 0.7 | 8.6 |
| Alex Morales (ORL) | 67% | 10.3<br><sub>7,9,-,14,6</sub> | 2.8<br><sub>2,0,-,3,0</sub> |  | 1.4<br><sub>2,1,-,2,0</sub> |  | 0.8<br><sub>1,0,-,0,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 5.0 |
| Colin Castleton (ORL) | 52% | 6.8<br><sub>7,-,-,-,2</sub> | 2.4<br><sub>2,-,-,-,0</sub> |  | 2.0<br><sub>2,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,1</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.8 |

</details>


### HOU @ PHX
Out: Mark Williams (PHX), Steven Adams (HOU), Clint Capela (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.9–109.8 | HOU 67% | 1.50 / 2.99 | PHX +6.5 | 225.5 | PHX +7.5 covers 54%; o221.5 59% |
| Expected (weighted by chance each plays) | 115.5–109.9 | HOU 66% | 1.52 / 2.93 | PHX +5.5 | 225.5 | PHX +7.5 covers 56%; o221.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Goodwin (PHX) | Doubtful | 20% | 14.6 | 5.5 | 2.8 | 1.4 | 0.7 | 1.0 | 0.1 | 0.6 | 9.6 | small |
| Rasheer Fleming (PHX) | Questionable | 55% | 7.9 | 2.7 | 1.3 | 0.3 | 0.2 | 0.3 | 0.2 | 0.3 | 4.4 | small |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.2<br><sub>30,35,33,36,35</sub> | 16.0<br><sub>14,22,30,14,11</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>2,3,9,10,4</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>2,2,5,0,2</sub> |  | 2.3<br><sub>3,3,6,4,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.9 | 1.5 | 25.2 |
| Alperen Sengun | 76% | 36.2<br><sub>-,-,33,38,39</sub> | 21.9<br><sub>-,-,16,26,17</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 10.1<br><sub>-,-,9,7,12</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>-,-,9,10,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 0.7<br><sub>-,-,0,1,0</sub> |  | 1.4 | 1.2 | 3.4 | 38.6 |
| Kevin Durant | 98% | 36.0<br><sub>31,37,27,33,35</sub> | 22.9<br><sub>18,28,14,12,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>5,5,3,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,1,4,3,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 3.4 | 33.1 |
| Amen Thompson | 98% | 35.6<br><sub>33,39,28,25,32</sub> | 17.5<br><sub>23,15,8,14,11</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>4,3,3,3,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>3,6,1,3,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.5 | 29.1 |
| Fred VanVleet | 86% | 33.0<br><sub>29,33,-,27,30</sub> | 13.5<br><sub>24,16,-,8,18</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>6,5,-,2,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.0<br><sub>5,6,-,9,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,3,-,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 1.7 | 22.1 |
| Tari Eason | 98% | 25.7<br><sub>31,26,19,27,24</sub> | 10.1<br><sub>5,11,8,13,9</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>9,13,3,4,6</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>1,2,2,3,1</sub> |  | 1.1<br><sub>1,0,2,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.7 | 1.2 | 17.7 |
| Reed Sheppard | 71% | 23.2<br><sub>23,-,-,17,21</sub> | 10.7<br><sub>7,-,-,8,14</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>3,-,-,1,2</sub> |  | 3.0<br><sub>4,-,-,1,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.5 | 1.3 | 16.0 |
| Marcus Smart | 83% | 23.0<br><sub>-,17,36,20,18</sub> | 8.5<br><sub>-,8,24,8,4</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>-,2,5,4,1</sub> |  | 2.5<br><sub>-,4,3,4,1</sub> |  | 1.2<br><sub>-,0,7,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.3 | 1.6 | 13.7 |
| Bogdan Bogdanovic | 93% | 12.2<br><sub>15,11,19,5,5</sub> | 4.5<br><sub>16,6,4,0,0</sub> |  | 1.4<br><sub>2,1,2,0,0</sub> |  | 1.0<br><sub>4,0,1,1,0</sub> |  | 0.6<br><sub>4,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.9 |
| Oscar Tshiebwe | 88% | 9.0<br><sub>14,11,4,7,2</sub> | 3.8<br><sub>7,0,2,4,2</sub> |  | 3.6<br><sub>5,5,1,1,0</sub> |  | 0.5<br><sub>2,0,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 7.8 |
| Isaiah Crawford | 58% | 7.2<br><sub>5,-,19,2,-</sub> | 2.3<br><sub>3,-,8,0,-</sub> |  | 1.1<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>1,-,2,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Jae'Sean Tate | 63% | 6.2<br><sub>4,-,6,2,-</sub> | 2.0<br><sub>0,-,0,0,-</sub> |  | 1.5<br><sub>0,-,3,1,-</sub> |  | 0.4<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 35.6<br><sub>34,39,35,34,34</sub> | 25.8<br><sub>3,20,26,33,30</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>2,2,3,1,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.9<br><sub>7,5,5,2,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>0,3,2,2,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.3 | 3.3 | 35.3 |
| Miles Bridges | 98% | 32.8<br><sub>32,37,35,31,31</sub> | 15.4<br><sub>17,24,21,18,18</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>8,10,6,7,13</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,2,3,5,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>2,2,3,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.5 | 1.4 | 25.1 |
| Dillon Brooks | 98% | 32.1<br><sub>33,21,34,35,29</sub> | 17.8<br><sub>19,22,18,15,24</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>5,1,8,6,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>5,2,4,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>3,4,2,0,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.2 | 1.8 | 23.8 |
| Jalen Green | 98% | 30.5<br><sub>31,25,36,32,24</sub> | 16.2<br><sub>20,2,11,22,6</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,2,8,2,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>4,2,8,2,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.4 | 2.5 | 23.2 |
| Collin Gillespie | 98% | 26.3<br><sub>23,33,24,23,24</sub> | 9.9<br><sub>9,16,3,2,6</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>1,3,1,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.9<br><sub>2,10,2,2,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>3,4,1,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.2 | 1.3 | 16.9 |
| Oso Ighodaro | 98% | 24.4<br><sub>-,21,24,23,24</sub> | 6.9<br><sub>-,2,14,9,2</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>-,9,2,7,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>-,5,2,7,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.3 | 15.5 |
| Luke Kennard | 98% | 19.3<br><sub>16,12,18,14,21</sub> | 6.3<br><sub>9,9,6,0,12</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,1,2,0,1</sub> |  | 1.8<br><sub>2,2,1,1,5</sub> |  | 0.8<br><sub>3,1,2,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.1 | 0.8 | 10.1 |
| Ryan Dunn | 97% | 18.1<br><sub>14,11,10,18,25</sub> | 5.2<br><sub>6,5,5,2,11</sub> |  | 3.7<br><sub>2,3,3,6,3</sub> |  | 1.2<br><sub>1,1,1,2,3</sub> |  | 0.5<br><sub>1,1,1,0,1</sub> |  | 0.8 | 0.5 | 0.6 | 10.1 |
| Khaman Maluach | 98% | 17.9<br><sub>26,17,13,16,22</sub> | 5.7<br><sub>12,9,5,6,8</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>7,6,2,6,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>1,0,0,2,2</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 1.0 | 11.7 |
| Drew Timme | 16% | 8.2 | 3.0 |  | 1.4 |  | 0.7 |  | 0.2 |  | 0.2 | 0.1 | 0.5 | 5.0 |
| Pat Spencer | 80% | 7.3<br><sub>-,-,-,3,2</sub> | 2.6<br><sub>-,-,-,0,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Duop Reath | 80% | 7.0<br><sub>7,-,-,7,2</sub> | 2.6<br><sub>5,-,-,7,0</sub> |  | 1.3<br><sub>3,-,-,0,0</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.2<br><sub>1,-,-,1,0</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea | 64% | 6.8<br><sub>3,-,-,3,2</sub> | 2.6<br><sub>2,-,-,3,0</sub> |  | 0.9<br><sub>0,-,-,0,0</sub> |  | 0.9<br><sub>1,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Koa Peat | 63% | 6.4<br><sub>3,-,-,3,2</sub> | 2.1<br><sub>0,-,-,2,0</sub> |  | 1.6<br><sub>0,-,-,1,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.4 | 3.9 |

</details>


### SAS @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 33.6<br><sub>27,39,34,24,34</sub> | 27.4<br><sub>29,36,43,12,52</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 11.1<br><sub>10,14,7,11,24</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,5,4,5,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,4,3,0,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.4 | 3.8 | 2.7 | 41.7 |
| Devin Vassell | 98% | 32.8<br><sub>24,38,34,25,36</sub> | 11.3<br><sub>14,21,9,11,2</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,5,5,2,7</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.6<br><sub>8,2,2,1,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>4,1,0,0,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.5 | 1.2 | 18.2 |
| Dylan Harper | 98% | 32.5<br><sub>30,37,39,27,36</sub> | 16.4<br><sub>13,13,25,17,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>6,5,7,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>6,8,6,8,0</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.4 | 2.0 | 25.9 |
| De'Aaron Fox | 98% | 32.2<br><sub>26,39,35,22,33</sub> | 15.4<br><sub>11,14,22,12,10</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,3,8,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>6,4,7,3,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>2,1,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.4 | 2.3 | 24.7 |
| Stephon Castle | 98% | 31.3<br><sub>27,38,22,26,35</sub> | 16.4<br><sub>15,14,0,16,17</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,6,5,5,10</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 5.5<br><sub>5,8,4,4,3</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 3.0 | 27.2 |
| Julian Champagnie | 98% | 25.6<br><sub>25,31,27,22,21</sub> | 8.4<br><sub>26,6,12,8,0</sub> |  | 4.3<br><sub>3,6,3,6,4</sub> |  | 1.3<br><sub>3,0,1,0,3</sub> |  | 1.5<br><sub>8,2,3,2,0</sub> |  | 1.0 | 0.5 | 0.7 | 14.0 |
| Keldon Johnson | 98% | 20.9<br><sub>22,23,24,27,19</sub> | 9.2<br><sub>14,9,2,15,4</sub> |  | 4.3<br><sub>4,6,6,7,5</sub> |  | 1.1<br><sub>0,2,0,1,2</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 14.7 |
| Luke Kornet | 98% | 14.2<br><sub>17,14,14,17,14</sub> | 3.8<br><sub>0,1,2,8,2</sub> |  | 4.2<br><sub>4,6,8,5,1</sub> |  | 0.9<br><sub>1,1,0,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 8.9 |
| Harrison Barnes | 67% | 12.7<br><sub>14,-,-,21,13</sub> | 4.1<br><sub>3,-,-,13,4</sub> |  | 1.5<br><sub>0,-,-,0,2</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>0,-,-,3,1</sub> |  | 0.3 | 0.1 | 0.4 | 6.2 |
| Carter Bryant | 72% | 8.4<br><sub>17,5,11,14,-</sub> | 2.8<br><sub>1,3,6,3,-</sub> |  | 1.4<br><sub>1,0,0,0,-</sub> |  | 0.5<br><sub>2,0,0,0,-</sub> |  | 0.2<br><sub>0,1,2,1,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.6 |
| Maliq Brown | 80% | 6.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 2.9 |
| Jordan McLaughlin | 48% | 6.6<br><sub>7,-,-,8,-</sub> | 2.1<br><sub>0,-,-,0,-</sub> |  | 0.9<br><sub>0,-,-,1,-</sub> |  | 1.0<br><sub>2,-,-,3,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.1 |
| Tarris Reed Jr. | 52% | 6.6<br><sub>5,-,-,7,-</sub> | 2.7<br><sub>4,-,-,4,-</sub> |  | 3.7<br><sub>5,-,-,7,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.6 | 6.8 |
| David Jones Garcia | 48% | 5.8<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.8 |
| Ja'Kobi Gillespie | 88% | 5.7<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.3<br><sub>33,32,30,35,35</sub> | 23.3<br><sub>23,24,24,28,21</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>4,9,5,3,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.6<br><sub>9,7,2,5,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,0,2,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.5 | 3.7 | 36.8 |
| Damian Lillard | 98% | 32.9<br><sub>31,30,27,30,33</sub> | 18.8<br><sub>21,9,22,20,25</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>4,2,4,6,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>4,1,3,1,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.2 | 2.5 | 28.4 |
| Toumani Camara | 98% | 30.9<br><sub>24,26,31,31,32</sub> | 11.5<br><sub>12,13,14,9,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>1,2,4,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>4,3,4,3,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.4 | 1.2 | 17.6 |
| Jrue Holiday | 98% | 29.8<br><sub>30,24,22,31,28</sub> | 13.4<br><sub>22,6,14,17,15</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>4,6,4,8,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.0<br><sub>3,4,3,10,0</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,2,2,3,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.3 | 2.1 | 23.2 |
| Donovan Clingan | 98% | 26.6<br><sub>26,29,15,32,29</sub> | 11.1<br><sub>9,11,4,17,24</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 10.4<br><sub>10,8,9,18,11</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>2,1,0,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.5 | 1.8 | 1.3 | 23.6 |
| Scoot Henderson | 98% | 25.7<br><sub>17,19,31,26,22</sub> | 12.1<br><sub>2,9,14,8,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,0,1,2,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>0,1,1,2,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.2 | 2.3 | 17.7 |
| Sidy Cissoko | 97% | 21.2<br><sub>20,19,19,22,21</sub> | 5.4<br><sub>6,4,1,8,7</sub> |  | 3.2<br><sub>2,6,3,3,4</sub> |  | 1.7<br><sub>4,2,1,0,4</sub> |  | 0.6<br><sub>0,0,0,2,1</sub> |  | 0.8 | 0.4 | 0.9 | 10.3 |
| Robert Williams III | 98% | 17.6<br><sub>21,-,14,15,16</sub> | 6.3<br><sub>14,-,3,2,9</sub> |  | 6.8<br><sub>10,-,3,6,8</sub> |  | 1.2<br><sub>1,-,1,2,1</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.2 | 0.8 | 14.3 |
| Chris Youngblood | 86% | 9.7<br><sub>-,-,7,15,4</sub> | 3.4<br><sub>-,-,3,7,0</sub> |  | 1.4<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.2 | 0.1 | 0.2 | 5.4 |
| Branden Carlson | 58% | 7.6<br><sub>-,12,4,-,3</sub> | 2.5<br><sub>-,2,0,-,2</sub> |  | 1.8<br><sub>-,2,2,-,0</sub> |  | 0.5<br><sub>-,1,1,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 4.7 |
| Micah Potter | 64% | 7.6<br><sub>-,9,4,-,2</sub> | 3.2<br><sub>-,1,2,-,4</sub> |  | 2.2<br><sub>-,2,1,-,1</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.2 | 0.1 | 0.4 | 5.8 |
| Yang Hansen | 63% | 7.3<br><sub>-,5,13,-,2</sub> | 2.8<br><sub>-,3,6,-,0</sub> |  | 1.8<br><sub>-,2,5,-,0</sub> |  | 0.4<br><sub>-,1,1,-,0</sub> |  | 0.2<br><sub>-,1,2,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.0 |
| John Tonje | 52% | 7.0<br><sub>-,5,-,-,-</sub> | 3.5<br><sub>-,5,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,1,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |
| Jayson Kent | 71% | 6.7<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-07/`._
