# NBA model · Mon 16 Nov 2026 (US date)

Updated **Tue 17 Nov, 06:43 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-16/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PR over 29.5 (30+) | GSW @ NOP | draftkings | 16.80 | 14.90 | 7.69 | 13.0% | 5.6% | 6.7% | +12.7% | +118.5% | 0.2% |
| Derik Queen AST over 5.5 (6+) | GSW @ NOP | draftkings | 13.00 | 11.70 | 6.24 | 16.0% | 7.2% | 8.6% | +11.2% | +108.3% | 0.2% |
| Kevin Durant AST over 7.5 (8+) | HOU @ MIA | draftkings | 11.20 | 10.11 | 5.44 | 18.4% | 8.3% | 9.9% | +10.8% | +106.0% | 0.3% |
| Derik Queen PTS over 19.5 (20+) | GSW @ NOP | draftkings | 13.00 | 11.90 | 6.64 | 15.1% | 7.2% | 8.4% | +9.2% | +95.7% | 0.2% |
| Derik Queen PR over 24.5 (25+) | GSW @ NOP | draftkings | 6.81 | 6.30 | 3.62 | 27.7% | 13.7% | 15.9% | +8.1% | +88.4% | 0.4% |
| Alperen Sengun PTS over 39.5 (40+) | HOU @ MIA | draftkings | 31.00 | 28.74 | 16.63 | 6.0% | 3.0% | 3.5% | +7.8% | +86.5% | 0.1% |
| Zion Williamson AST over 7.5 (8+) | GSW @ NOP | draftkings | 27.00 | 25.06 | 14.51 | 6.9% | 3.5% | 4.0% | +7.7% | +86.1% | 0.1% |
| Derik Queen REB over 11.5 (12+) | GSW @ NOP | draftkings | 16.20 | 15.04 | 8.72 | 11.5% | 5.8% | 6.7% | +7.7% | +85.7% | 0.1% |
| Zion Williamson AST over 5.5 (6+) | GSW @ NOP | draftkings | 8.10 | 7.52 | 4.37 | 22.9% | 11.5% | 13.3% | +7.6% | +85.5% | 0.3% |
| Draymond Green AST over 11.5 (12+) | GSW @ NOP | draftkings | 19.20 | 17.89 | 10.46 | 9.6% | 4.9% | 5.6% | +7.3% | +83.6% | 0.1% |
| Anthony Davis BLK over 3.5 (4+) | MEM @ WAS | draftkings | 12.00 | 11.21 | 6.60 | 15.2% | 7.8% | 8.9% | +7.1% | +82.0% | 0.2% |
| Kevin Durant AST over 9.5 (10+) | HOU @ MIA | draftkings | 28.00 | 26.39 | 15.87 | 6.3% | 3.3% | 3.8% | +6.2% | +76.5% | 0.1% |
| Draymond Green AST over 9.5 (10+) | GSW @ NOP | draftkings | 8.00 | 7.56 | 4.62 | 21.7% | 11.7% | 13.2% | +5.8% | +73.3% | 0.2% |
| Kevin Durant PRA over 54.5 (55+) | HOU @ MIA | draftkings | 25.00 | 23.75 | 14.69 | 6.8% | 3.7% | 4.2% | +5.3% | +70.2% | 0.1% |
| Derik Queen REB over 9.5 (10+) | GSW @ NOP | draftkings | 6.97 | 6.64 | 4.13 | 24.2% | 13.4% | 15.1% | +5.1% | +68.7% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey REB over 9.5 (10+) | MEM @ WAS | draftkings | 3.65 | Zach Edey | void | 55.9% | +9.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ORL @ BOS | Tue 17 Nov 11:00 | 106.6–114.6 | ORL 29% | 3.50 / 1.40 | BOS -8.5 | 221.5 | BOS -8.5 covers 49%; o212.5 68% |
| CHI @ CLE | Tue 17 Nov 11:00 | 114.8–122.5 | CHI 29% | 3.44 / 1.41 | CLE -7.5 | 237.5 | CLE -8.5 covers 48%; o241.5 40% |
| MEM @ WAS | Tue 17 Nov 11:00 | 124.5–120.0 | MEM 63% | 1.60 / 2.67 | WAS +4.5 | 244.5 | WAS +3.5 covers 46%; o232.5 74% |
| PHI @ BKN | Tue 17 Nov 11:30 | 112.7–112.0 | PHI 52% | 1.91 / 2.10 | BKN +1.5 | 224.5 | BKN +4.5 covers 60%; o225.5 48% |
| HOU @ MIA | Tue 17 Nov 11:30 | 118.0–118.9 | HOU 48% | 2.10 / 1.91 | MIA -1.5 | 236.5 | MIA +1.5 covers 55%; o231.5 61% |
| POR @ MIN | Tue 17 Nov 12:00 | 111.5–115.7 | POR 38% | 2.62 / 1.62 | MIN -4.5 | 227.5 | MIN -2.5 covers 56%; o227.5 49% |
| GSW @ NOP | Tue 17 Nov 12:00 | 119.8–112.8 | GSW 69% | 1.45 / 3.23 | NOP +7.5 | 232.5 | NOP +3.5 covers 40%; o223.5 69% |
| PHX @ DEN | Tue 17 Nov 13:00 | 110.8–119.0 | PHX 28% | 3.58 / 1.39 | DEN -8.5 | 229.5 | DEN -9.5 covers 46%; o229.5 51% |

### ORL @ BOS
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.6–114.6 | ORL 29% | 3.50 / 1.40 | BOS -8.5 | 221.5 | BOS -8.5 covers 49%; o212.5 68% |
| Expected (weighted by chance each plays) | 106.2–115.1 | ORL 26% | 3.80 / 1.36 | BOS -8.5 | 221.5 | BOS -8.5 covers 51%; o212.5 68% |
| if Neemias Queta plays | 105.9–115.4 | ORL 25% | 4.00 / 1.33 | BOS -9.5 | 221.5 | BOS -8.5 covers 53%; o212.5 68% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Neemias Queta (BOS) | Questionable | 55% | 20.9 | 8.3 | 7.1 | 1.7 | 0.1 | 0.6 | 1.2 | 1.1 | 17.1 | full tables below |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 32.8<br><sub>38,40,38,39,36</sub> | 20.7<br><sub>15,30,33,38,35</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>8,6,7,8,9</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>15,11,7,1,12</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>0,3,1,3,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.3 | 2.7 | 31.9 |
| Desmond Bane | 98% | 31.4<br><sub>32,-,36,34,35</sub> | 16.5<br><sub>15,-,15,25,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>6,-,6,3,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>0,-,4,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,-,4,7,6</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.8 | 23.2 |
| Anthony Black | 98% | 30.0<br><sub>31,38,33,39,37</sub> | 13.2<br><sub>10,18,26,22,5</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>7,8,7,7,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>6,6,5,8,5</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>1,2,2,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.6 | 2.0 | 20.9 |
| Wendell Carter Jr. | 98% | 29.0<br><sub>34,40,33,28,30</sub> | 10.6<br><sub>27,19,8,9,12</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>13,11,11,7,8</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,0,1,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>2,3,0,0,1</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.6 | 1.4 | 19.3 |
| Jalen Suggs | 98% | 26.9<br><sub>-,-,-,-,21</sub> | 10.5<br><sub>-,-,-,-,3</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>-,-,-,-,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 4.0<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.5 | 2.1 | 17.8 |
| Tristan da Silva | 83% | 26.1<br><sub>30,39,-,-,31</sub> | 10.8<br><sub>18,19,-,-,12</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>2,7,-,-,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>1,2,-,-,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>4,5,-,-,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.2 | 1.0 | 15.9 |
| Jevon Carter | 86% | 14.1<br><sub>3,15,4,28,17</sub> | 5.1<br><sub>0,9,0,11,5</sub> |  | 1.3<br><sub>0,1,0,3,2</sub> |  | 1.4<br><sub>0,0,0,4,2</sub> |  | 0.7<br><sub>0,3,0,3,1</sub> |  | 0.5 | 0.1 | 0.5 | 7.8 |
| Goga Bitadze | 88% | 13.3<br><sub>8,7,15,20,18</sub> | 4.4<br><sub>4,4,2,4,12</sub> |  | 3.9<br><sub>5,5,2,7,4</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.6 | 9.3 |
| Jamal Cain | 83% | 13.0<br><sub>25,36,20,-,4</sub> | 5.1<br><sub>5,18,5,-,0</sub> |  | 2.2<br><sub>5,12,3,-,4</sub> |  | 0.6<br><sub>0,1,1,-,1</sub> |  | 0.5<br><sub>1,2,1,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 8.0 |
| Jase Richardson | 72% | 12.8<br><sub>26,30,15,20,-</sub> | 4.7<br><sub>10,2,6,6,-</sub> |  | 1.3<br><sub>2,4,1,1,-</sub> |  | 1.3<br><sub>3,4,1,2,-</sub> |  | 0.4<br><sub>2,0,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.3 |
| Nikola Vucevic | 98% | 11.7<br><sub>4,6,18,14,11</sub> | 4.6<br><sub>0,0,5,3,2</sub> |  | 3.1<br><sub>0,1,4,5,3</sub> |  | 1.2<br><sub>0,2,1,1,0</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 9.0 |
| Alex Morales | 66% | 8.2<br><sub>6,15,29,18,-</sub> | 1.9<br><sub>0,0,7,5,-</sub> |  | 1.3<br><sub>0,2,7,4,-</sub> |  | 0.6<br><sub>0,1,0,3,-</sub> |  | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.2 | 0.0 | 0.4 | 3.8 |
| Colin Castleton | 48% | 5.9<br><sub>2,-,-,1,-</sub> | 2.1<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 34.1<br><sub>29,29,32,38,30</sub> | 26.9<br><sub>34,21,21,24,32</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 7.9<br><sub>8,4,6,7,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>9,6,4,8,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>5,5,3,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.6 | 2.9 | 41.0 |
| Derrick White | 98% | 31.0<br><sub>25,27,22,38,23</sub> | 13.5<br><sub>18,9,5,19,16</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>4,3,1,1,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>5,7,3,7,2</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>4,1,1,3,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 1.0 | 1.6 | 21.3 |
| Paul George | 98% | 30.8<br><sub>22,28,30,-,25</sub> | 19.3<br><sub>8,27,36,-,7</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,3,5,-,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,1,1,-,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>2,5,6,-,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.7 | 0.5 | 2.2 | 27.4 |
| Payton Pritchard | 98% | 27.7<br><sub>23,29,30,31,19</sub> | 13.8<br><sub>12,12,18,14,10</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>6,5,6,1,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.8<br><sub>5,4,5,1,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>4,4,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.1 | 1.2 | 20.9 |
| Baylor Scheierman | 98% | 20.8<br><sub>15,19,18,29,18</sub> | 6.2<br><sub>5,7,5,9,12</sub> |  | 3.9<br><sub>4,1,3,7,5</sub> |  | 1.5<br><sub>2,0,2,3,3</sub> |  | 1.0<br><sub>1,1,1,3,2</sub> |  | 0.7 | 0.1 | 0.7 | 11.7 |
| Sam Hauser | 98% | 19.2<br><sub>17,23,18,24,11</sub> | 6.9<br><sub>9,7,12,8,8</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,3,5,9,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>3,1,2,0,0</sub> |  | 1.3<br><sub>3,1,4,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.4 | 0.2 | 0.4 | 10.9 |
| Mitchell Robinson | 98% | 16.8<br><sub>15,18,17,11,15</sub> | 4.6<br><sub>6,12,2,2,0</sub> |  | 6.1<br><sub>7,7,6,2,7</sub> |  | 0.7<br><sub>0,2,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.0 | 0.8 | 11.3 |
| Jordan Walsh | 98% | 15.8<br><sub>22,11,19,18,21</sub> | 4.5<br><sub>6,0,8,6,11</sub> |  | 3.1<br><sub>3,3,2,3,1</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,0,1,0,2</sub> |  | 0.6 | 0.3 | 0.5 | 8.3 |
| Luka Garza | 98% | 14.5<br><sub>19,9,9,11,14</sub> | 6.7<br><sub>6,4,2,5,2</sub> |  | 3.4<br><sub>7,5,0,1,3</sub> |  | 1.3<br><sub>4,0,2,0,5</sub> |  | 0.8<br><sub>2,0,0,1,0</sub> |  | 0.4 | 0.4 | 0.7 | 11.4 |
| Devin Carter | 91% | 14.2<br><sub>-,-,-,-,12</sub> | 5.9<br><sub>-,-,-,-,0</sub> |  | 2.5<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.2 | 1.1 | 9.9 |
| Hugo Gonzalez | 98% | 13.8<br><sub>15,10,19,8,18</sub> | 4.1<br><sub>8,0,10,0,9</sub> |  | 2.7<br><sub>1,2,2,1,5</sub> |  | 0.6<br><sub>0,1,2,0,2</sub> |  | 0.4<br><sub>1,0,2,0,2</sub> |  | 0.5 | 0.3 | 0.6 | 7.5 |
| Mike Conley | 43% | 8.3<br><sub>11,10,-,-,-</sub> | 2.3<br><sub>0,3,-,-,-</sub> |  | 0.9<br><sub>0,3,-,-,-</sub> |  | 1.0<br><sub>1,1,-,-,-</sub> |  | 0.2<br><sub>0,1,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.2 |
| Ron Harper Jr. | 64% | 8.1<br><sub>10,4,4,-,12</sub> | 3.4<br><sub>3,2,0,-,10</sub> |  | 1.2<br><sub>0,0,1,-,1</sub> |  | 0.5<br><sub>2,0,0,-,0</sub> |  | 0.4<br><sub>1,0,0,-,2</sub> |  | 0.3 | 0.1 | 0.3 | 5.1 |
| Dillon Mitchell | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.3 | 0.9 |
| Chris Cenac Jr. | 52% | 6.1<br><sub>-,-,-,-,7</sub> | 2.6<br><sub>-,-,-,-,6</sub> |  | 1.6<br><sub>-,-,-,-,3</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Amari Williams | 30% | 5.4<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.5 |

</details>

<details><summary>if Neemias Queta plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 32.3<br><sub>29,29,32,38,30</sub> | 25.3<br><sub>34,21,21,24,32</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>8,4,6,7,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>9,6,4,8,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>5,5,3,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.6 | 2.8 | 39.4 |
| Derrick White (BOS) | 98% | 29.1<br><sub>25,27,22,38,23</sub> | 12.9<br><sub>18,9,5,19,16</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>4,3,1,1,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>5,7,3,7,2</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>4,1,1,3,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 1.0 | 1.5 | 20.4 |
| Paul George (BOS) | 98% | 28.9<br><sub>22,28,30,-,25</sub> | 17.7<br><sub>8,27,36,-,7</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>5,3,5,-,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,1,1,-,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>2,5,6,-,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.6 | 0.4 | 2.1 | 25.5 |
| Payton Pritchard (BOS) | 98% | 25.3<br><sub>23,29,30,31,19</sub> | 12.8<br><sub>12,12,18,14,10</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>6,5,6,1,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.7<br><sub>5,4,5,1,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>4,4,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.1 | 1.1 | 19.5 |
| Neemias Queta (BOS) | 100% | 20.9<br><sub>15,22,22,31,15</sub> | 8.3<br><sub>4,13,4,11,8</sub> | 8.5 · – | 7.1<br><sub>3,9,6,13,6</sub> | 6.5 | 1.7<br><sub>1,4,3,3,2</sub> | 1.5 | 0.1<br><sub>0,0,0,1,1</sub> |  | 0.6 | 1.2 | 1.1 | 17.1 |
| Baylor Scheierman (BOS) | 98% | 19.0<br><sub>15,19,18,29,18</sub> | 5.8<br><sub>5,7,5,9,12</sub> |  | 3.6<br><sub>4,1,3,7,5</sub> |  | 1.5<br><sub>2,0,2,3,3</sub> |  | 0.9<br><sub>1,1,1,3,2</sub> |  | 0.7 | 0.1 | 0.7 | 10.9 |
| Sam Hauser (BOS) | 98% | 17.8<br><sub>17,23,18,24,11</sub> | 6.7<br><sub>9,7,12,8,8</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,3,5,9,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>3,1,2,0,0</sub> |  | 1.2<br><sub>3,1,4,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.4 | 0.2 | 0.4 | 10.6 |
| Mitchell Robinson (BOS) | 98% | 15.2<br><sub>15,18,17,11,15</sub> | 4.4<br><sub>6,12,2,2,0</sub> |  | 5.8<br><sub>7,7,6,2,7</sub> |  | 0.6<br><sub>0,2,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.9 | 0.7 | 10.8 |
| Jordan Walsh (BOS) | 98% | 14.2<br><sub>22,11,19,18,21</sub> | 4.2<br><sub>6,0,8,6,11</sub> |  | 2.8<br><sub>3,3,2,3,1</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.4<br><sub>1,0,1,0,2</sub> |  | 0.5 | 0.3 | 0.5 | 7.6 |
| Devin Carter (BOS) | 91% | 13.3<br><sub>-,-,-,-,12</sub> | 5.6<br><sub>-,-,-,-,0</sub> |  | 2.4<br><sub>-,-,-,-,2</sub> |  | 1.7<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.2 | 1.1 | 9.7 |
| Luka Garza (BOS) | 98% | 12.9<br><sub>19,9,9,11,14</sub> | 6.3<br><sub>6,4,2,5,2</sub> |  | 3.1<br><sub>7,5,0,1,3</sub> |  | 1.3<br><sub>4,0,2,0,5</sub> |  | 0.7<br><sub>2,0,0,1,0</sub> |  | 0.3 | 0.4 | 0.6 | 10.7 |
| Hugo Gonzalez (BOS) | 98% | 12.6<br><sub>15,10,19,8,18</sub> | 4.0<br><sub>8,0,10,0,9</sub> |  | 2.5<br><sub>1,2,2,1,5</sub> |  | 0.7<br><sub>0,1,2,0,2</sub> |  | 0.4<br><sub>1,0,2,0,2</sub> |  | 0.5 | 0.2 | 0.6 | 7.2 |
| Ron Harper Jr. (BOS) | 64% | 7.7<br><sub>10,4,4,-,12</sub> | 3.6<br><sub>3,2,0,-,10</sub> |  | 1.1<br><sub>0,0,1,-,1</sub> |  | 0.5<br><sub>2,0,0,-,0</sub> |  | 0.4<br><sub>1,0,0,-,2</sub> |  | 0.3 | 0.1 | 0.3 | 5.2 |
| Mike Conley (BOS) | 43% | 7.6<br><sub>11,10,-,-,-</sub> | 2.3<br><sub>0,3,-,-,-</sub> |  | 0.8<br><sub>0,3,-,-,-</sub> |  | 1.1<br><sub>1,1,-,-,-</sub> |  | 0.2<br><sub>0,1,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.3 |
| Dillon Mitchell (BOS) | 38% | 6.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 1.0 |
| Chris Cenac Jr. (BOS) | 52% | 6.2<br><sub>-,-,-,-,7</sub> | 3.1<br><sub>-,-,-,-,6</sub> |  | 1.7<br><sub>-,-,-,-,3</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Amari Williams (BOS) | 30% | 5.3<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 3.5 |
| Franz Wagner (ORL) | 98% | 32.8<br><sub>38,40,38,39,36</sub> | 20.7<br><sub>15,30,33,38,35</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>8,6,7,8,9</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>15,11,7,1,12</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>0,3,1,3,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.3 | 2.7 | 31.9 |
| Desmond Bane (ORL) | 98% | 31.5<br><sub>32,-,36,34,35</sub> | 16.5<br><sub>15,-,15,25,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>6,-,6,3,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>0,-,4,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>3,-,4,7,6</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.8 | 23.1 |
| Anthony Black (ORL) | 98% | 30.1<br><sub>31,38,33,39,37</sub> | 13.2<br><sub>10,18,26,22,5</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>7,8,7,7,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>6,6,5,8,5</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>1,2,2,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.6 | 2.0 | 20.9 |
| Wendell Carter Jr. (ORL) | 98% | 28.8<br><sub>34,40,33,28,30</sub> | 10.6<br><sub>27,19,8,9,12</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>13,11,11,7,8</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>2,0,1,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>2,3,0,0,1</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.6 | 1.4 | 19.2 |
| Jalen Suggs (ORL) | 98% | 26.9<br><sub>-,-,-,-,21</sub> | 10.5<br><sub>-,-,-,-,3</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>-,-,-,-,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 4.0<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.5 | 2.1 | 17.8 |
| Tristan da Silva (ORL) | 83% | 26.1<br><sub>30,39,-,-,31</sub> | 10.6<br><sub>18,19,-,-,12</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>2,7,-,-,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>1,2,-,-,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>4,5,-,-,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.2 | 1.0 | 15.8 |
| Jevon Carter (ORL) | 86% | 14.2<br><sub>3,15,4,28,17</sub> | 5.1<br><sub>0,9,0,11,5</sub> |  | 1.4<br><sub>0,1,0,3,2</sub> |  | 1.4<br><sub>0,0,0,4,2</sub> |  | 0.7<br><sub>0,3,0,3,1</sub> |  | 0.6 | 0.1 | 0.5 | 7.8 |
| Goga Bitadze (ORL) | 88% | 13.3<br><sub>8,7,15,20,18</sub> | 4.5<br><sub>4,4,2,4,12</sub> |  | 3.9<br><sub>5,5,2,7,4</sub> |  | 0.9<br><sub>0,2,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.6 | 9.3 |
| Jamal Cain (ORL) | 83% | 13.0<br><sub>25,36,20,-,4</sub> | 5.2<br><sub>5,18,5,-,0</sub> |  | 2.2<br><sub>5,12,3,-,4</sub> |  | 0.6<br><sub>0,1,1,-,1</sub> |  | 0.5<br><sub>1,2,1,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 8.0 |
| Jase Richardson (ORL) | 72% | 12.7<br><sub>26,30,15,20,-</sub> | 4.7<br><sub>10,2,6,6,-</sub> |  | 1.3<br><sub>2,4,1,1,-</sub> |  | 1.3<br><sub>3,4,1,2,-</sub> |  | 0.4<br><sub>2,0,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.2 |
| Nikola Vucevic (ORL) | 98% | 11.8<br><sub>4,6,18,14,11</sub> | 4.7<br><sub>0,0,5,3,2</sub> |  | 3.1<br><sub>0,1,4,5,3</sub> |  | 1.2<br><sub>0,2,1,1,0</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 9.0 |
| Alex Morales (ORL) | 66% | 8.2<br><sub>6,15,29,18,-</sub> | 1.9<br><sub>0,0,7,5,-</sub> |  | 1.3<br><sub>0,2,7,4,-</sub> |  | 0.6<br><sub>0,1,0,3,-</sub> |  | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.8 |
| Colin Castleton (ORL) | 48% | 6.0<br><sub>2,-,-,1,-</sub> | 2.1<br><sub>0,-,-,0,-</sub> |  | 1.7<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.2 |

</details>


### CHI @ CLE
Out: Sam Merrill (CLE), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE), Tobe Awaka (CHI), Orlando Robinson (CHI), Caleb Wilson (CHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.8–122.5 | CHI 29% | 3.44 / 1.41 | CLE -7.5 | 237.5 | CLE -8.5 covers 48%; o241.5 40% |
| Expected (weighted by chance each plays) | 114.4–122.8 | CHI 27% | 3.65 / 1.38 | CLE -8.5 | 237.5 | CLE -8.5 covers 50%; o241.5 41% |
| if Peyton Watson plays | 114.0–124.3 | CHI 23% | 4.39 / 1.29 | CLE -10.5 | 238.5 | CLE -8.5 covers 55%; o241.5 43% |
| if Jaylon Tyson plays | 114.7–123.0 | CHI 27% | 3.65 / 1.38 | CLE -8.5 | 237.5 | CLE -8.5 covers 50%; o241.5 41% |
| if Jalen Smith plays | 114.7–122.0 | CHI 30% | 3.33 / 1.43 | CLE -7.5 | 236.5 | CLE -8.5 covers 47%; o241.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Peyton Watson (CLE) | Questionable | 55% | 29.4 | 13.0 | 5.0 | 2.7 | 1.3 | 1.1 | 1.6 | 1.5 | 20.7 | full tables below |
| Jaylon Tyson (CLE) | Doubtful | 20% | 29.4 | 12.5 | 5.1 | 2.9 | 2.0 | 1.0 | 0.4 | 1.3 | 20.6 | full tables below |
| Jalen Smith (CHI) | Questionable | 55% | 26.7 | 13.2 | 8.1 | 1.7 | 1.7 | 0.6 | 0.9 | 1.0 | 22.9 | full tables below |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 31.2<br><sub>27,34,25,39,26</sub> | 14.2<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.8 | 29.8 |
| Norman Powell | 98% | 31.1<br><sub>22,-,-,31,30</sub> | 21.3<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>1,-,-,2,3</sub> |  | 2.5<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.2 | 27.1 |
| Matas Buzelis | 98% | 30.7<br><sub>26,31,31,29,30</sub> | 17.2<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.2<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.0 | 2.3 | 25.1 |
| Isaac Okoro | 98% | 29.3<br><sub>15,25,23,41,31</sub> | 9.7<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.8 | 0.4 | 1.0 | 14.4 |
| Patrick Williams | 76% | 26.0<br><sub>20,25,28,24,26</sub> | 9.2<br><sub>4,7,9,13,14</sub> |  | 3.6<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.8 |
| Tre Jones | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.1<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.2 | 18.7 |
| Nic Claxton | 98% | 20.1<br><sub>-,18,16,22,-</sub> | 7.9<br><sub>-,4,17,2,-</sub> |  | 5.6<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.8 | 0.9 | 15.7 |
| Zach Collins | 71% | 18.5<br><sub>14,-,3,-,28</sub> | 7.6<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.7 |
| Leonard Miller | 67% | 17.7<br><sub>19,-,2,-,17</sub> | 8.0<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.1<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.2 |
| Buddy Hield | 71% | 17.4<br><sub>8,-,-,25,20</sub> | 8.5<br><sub>7,-,-,12,16</sub> |  | 2.5<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.4<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 1.0 | 12.7 |
| Noa Essengue | 96% | 13.3<br><sub>14,15,11,8,7</sub> | 5.3<br><sub>6,10,8,5,0</sub> |  | 2.9<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.2 | 0.6 | 8.9 |
| Jordan Hawkins | 58% | 12.8<br><sub>7,17,24,-,-</sub> | 5.5<br><sub>2,9,7,-,-</sub> |  | 1.7<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 7.9 |
| Dailyn Swain | 52% | 8.5<br><sub>7,-,-,-,-</sub> | 3.0<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 1.0 | 5.3 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.6<br><sub>34,25,33,35,-</sub> | 22.0<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.6 | 3.4 | 34.2 |
| Donovan Mitchell | 98% | 35.4<br><sub>37,23,36,33,-</sub> | 30.0<br><sub>37,11,23,25,-</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 53%</sub> | 3.5<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6 | 0.4 | 3.0 | 41.0 |
| Tyrese Proctor | 96% | 30.9<br><sub>23,23,23,27,34</sub> | 15.7<br><sub>7,6,15,22,24</sub> |  | 5.2<br><sub>3,1,3,4,11</sub> |  | 4.9<br><sub>3,4,1,3,10</sub> |  | 2.5<br><sub>2,0,3,5,4</sub> |  | 1.3 | 0.1 | 1.5 | 25.8 |
| Meleek Thomas | 93% | 30.9<br><sub>24,27,22,18,34</sub> | 16.7<br><sub>9,18,14,12,20</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>4,3,4,0,4</sub> |  | 2.3<br><sub>0,3,1,3,2</sub> |  | 2.8<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.4 | 1.5 | 22.8 |
| Jarrett Allen | 76% | 29.7<br><sub>-,19,32,32,-</sub> | 15.7<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 9.7<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.6 | 1.4 | 27.1 |
| Mario Hezonja | 98% | 25.3<br><sub>19,17,7,9,34</sub> | 10.8<br><sub>0,10,0,4,22</sub> |  | 6.6<br><sub>5,3,0,4,7</sub> |  | 2.0<br><sub>1,0,0,0,4</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 0.9 | 0.4 | 1.1 | 19.4 |
| Thomas Bryant | 72% | 23.8<br><sub>15,15,-,16,27</sub> | 13.0<br><sub>5,11,-,9,19</sub> |  | 6.4<br><sub>3,2,-,1,11</sub> |  | 1.2<br><sub>1,0,-,1,3</sub> |  | 1.6<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.8 | 1.0 | 20.6 |
| Craig Porter Jr. | 80% | 23.4<br><sub>15,17,-,9,28</sub> | 5.2<br><sub>0,9,-,0,9</sub> |  | 4.6<br><sub>1,2,-,2,9</sub> |  | 4.3<br><sub>1,4,-,2,6</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.8 | 1.1 | 14.2 |
| Norchad Omier | 52% | 22.9<br><sub>-,12,-,-,27</sub> | 7.2<br><sub>-,0,-,-,13</sub> |  | 5.9<br><sub>-,3,-,-,8</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.9 | 0.2 | 0.7 | 15.5 |
| Riley Minix | 52% | 18.0<br><sub>10,17,-,-,22</sub> | 6.5<br><sub>8,2,-,-,2</sub> |  | 2.5<br><sub>3,2,-,-,0</sub> |  | 0.9<br><sub>0,0,-,-,0</sub> |  | 0.8<br><sub>2,0,-,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 9.9 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell (CHI) | 98% | 29.6<br><sub>22,-,-,31,30</sub> | 19.8<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>1,-,-,2,3</sub> |  | 2.3<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 25.2 |
| Josh Giddey (CHI) | 98% | 29.0<br><sub>27,34,25,39,26</sub> | 12.8<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 7.9<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.6 | 27.1 |
| Matas Buzelis (CHI) | 98% | 27.9<br><sub>26,31,31,29,30</sub> | 15.1<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.9<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.9 | 2.1 | 22.3 |
| Jalen Smith (CHI) | 100% | 26.7<br><sub>7,30,30,32,-</sub> | 13.2<br><sub>3,17,23,15,-</sub> | 13.5 · – | 8.1<br><sub>2,8,4,12,-</sub> | 8.5 | 1.7<br><sub>0,2,3,3,-</sub> | 1.5 | 1.7<br><sub>1,2,5,1,-</sub> | 1.5 | 0.6 | 0.9 | 1.0 | 22.9 |
| Isaac Okoro (CHI) | 98% | 25.1<br><sub>15,25,23,41,31</sub> | 8.4<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.7 | 0.4 | 0.8 | 12.4 |
| Patrick Williams (CHI) | 76% | 23.4<br><sub>20,25,28,24,26</sub> | 8.0<br><sub>4,7,9,13,14</sub> |  | 3.2<br><sub>0,3,7,4,5</sub> |  | 1.7<br><sub>2,3,4,2,1</sub> |  | 1.1<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.4 | 1.0 | 13.0 |
| Tre Jones (CHI) | 98% | 20.6<br><sub>18,14,28,15,24</sub> | 11.2<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.8 | 0.2 | 1.1 | 17.2 |
| Nic Claxton (CHI) | 98% | 17.9<br><sub>-,18,16,22,-</sub> | 6.9<br><sub>-,4,17,2,-</sub> |  | 4.9<br><sub>-,4,6,6,-</sub> |  | 1.9<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.7 | 0.8 | 13.7 |
| Buddy Hield (CHI) | 71% | 15.6<br><sub>8,-,-,25,20</sub> | 7.6<br><sub>7,-,-,12,16</sub> |  | 2.2<br><sub>1,-,-,3,4</sub> |  | 1.4<br><sub>1,-,-,3,2</sub> |  | 1.1<br><sub>1,-,-,2,4</sub> |  | 0.6 | 0.2 | 0.9 | 11.3 |
| Zach Collins (CHI) | 71% | 15.3<br><sub>14,-,3,-,28</sub> | 6.3<br><sub>3,-,2,-,8</sub> |  | 4.4<br><sub>1,-,2,-,5</sub> |  | 1.6<br><sub>3,-,1,-,4</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.8 | 12.2 |
| Leonard Miller (CHI) | 67% | 15.0<br><sub>19,-,2,-,17</sub> | 6.8<br><sub>4,-,0,-,4</sub> |  | 3.6<br><sub>6,-,0,-,3</sub> |  | 0.9<br><sub>3,-,0,-,4</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.7 | 11.3 |
| Noa Essengue (CHI) | 96% | 10.1<br><sub>14,15,11,8,7</sub> | 4.1<br><sub>6,10,8,5,0</sub> |  | 2.2<br><sub>3,7,4,1,1</sub> |  | 0.5<br><sub>0,1,3,1,0</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.9 |
| Jordan Hawkins (CHI) | 58% | 8.8<br><sub>7,17,24,-,-</sub> | 3.8<br><sub>2,9,7,-,-</sub> |  | 1.1<br><sub>1,0,4,-,-</sub> |  | 0.5<br><sub>0,1,2,-,-</sub> |  | 0.4<br><sub>0,1,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.4 |
| Dailyn Swain (CHI) | 52% | 6.7<br><sub>7,-,-,-,-</sub> | 2.4<br><sub>3,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.9<br><sub>1,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.7 | 4.3 |
| James Harden (CLE) | 98% | 35.6<br><sub>34,25,33,35,-</sub> | 22.1<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.6 | 3.4 | 34.2 |
| Donovan Mitchell (CLE) | 98% | 35.4<br><sub>37,23,36,33,-</sub> | 29.9<br><sub>37,11,23,25,-</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 53%</sub> | 3.5<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6 | 0.4 | 3.0 | 40.9 |
| Tyrese Proctor (CLE) | 96% | 31.0<br><sub>23,23,23,27,34</sub> | 15.9<br><sub>7,6,15,22,24</sub> |  | 5.2<br><sub>3,1,3,4,11</sub> |  | 4.9<br><sub>3,4,1,3,10</sub> |  | 2.5<br><sub>2,0,3,5,4</sub> |  | 1.3 | 0.1 | 1.5 | 26.0 |
| Meleek Thomas (CLE) | 93% | 30.8<br><sub>24,27,22,18,34</sub> | 16.7<br><sub>9,18,14,12,20</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 3.9<br><sub>4,3,4,0,4</sub> |  | 2.3<br><sub>0,3,1,3,2</sub> |  | 2.8<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.4 | 1.5 | 22.8 |
| Jarrett Allen (CLE) | 76% | 29.7<br><sub>-,19,32,32,-</sub> | 15.7<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 9.7<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.1 | 1.6 | 1.4 | 27.0 |
| Mario Hezonja (CLE) | 98% | 25.4<br><sub>19,17,7,9,34</sub> | 10.9<br><sub>0,10,0,4,22</sub> |  | 6.6<br><sub>5,3,0,4,7</sub> |  | 2.0<br><sub>1,0,0,0,4</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 0.9 | 0.4 | 1.1 | 19.5 |
| Thomas Bryant (CLE) | 72% | 23.7<br><sub>15,15,-,16,27</sub> | 12.8<br><sub>5,11,-,9,19</sub> |  | 6.4<br><sub>3,2,-,1,11</sub> |  | 1.2<br><sub>1,0,-,1,3</sub> |  | 1.5<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.8 | 1.0 | 20.4 |
| Craig Porter Jr. (CLE) | 80% | 23.3<br><sub>15,17,-,9,28</sub> | 5.2<br><sub>0,9,-,0,9</sub> |  | 4.6<br><sub>1,2,-,2,9</sub> |  | 4.3<br><sub>1,4,-,2,6</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.8 | 1.1 | 14.1 |
| Norchad Omier (CLE) | 52% | 23.0<br><sub>-,12,-,-,27</sub> | 7.2<br><sub>-,0,-,-,13</sub> |  | 5.9<br><sub>-,3,-,-,8</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.9 | 0.2 | 0.7 | 15.6 |
| Riley Minix (CLE) | 52% | 17.9<br><sub>10,17,-,-,22</sub> | 6.5<br><sub>8,2,-,-,2</sub> |  | 2.5<br><sub>3,2,-,-,0</sub> |  | 0.9<br><sub>0,0,-,-,0</sub> |  | 0.8<br><sub>2,0,-,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 9.8 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>if Peyton Watson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell (CHI) | 98% | 31.2<br><sub>22,-,-,31,30</sub> | 21.2<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>1,-,-,2,3</sub> |  | 2.5<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.2 | 27.0 |
| Josh Giddey (CHI) | 98% | 31.1<br><sub>27,34,25,39,26</sub> | 14.3<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.8 | 29.8 |
| Matas Buzelis (CHI) | 98% | 30.8<br><sub>26,31,31,29,30</sub> | 17.1<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.2<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.1 | 2.3 | 25.1 |
| Isaac Okoro (CHI) | 98% | 29.3<br><sub>15,25,23,41,31</sub> | 9.7<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.8 | 0.4 | 1.0 | 14.4 |
| Patrick Williams (CHI) | 76% | 26.0<br><sub>20,25,28,24,26</sub> | 9.2<br><sub>4,7,9,13,14</sub> |  | 3.6<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.7 |
| Tre Jones (CHI) | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.0<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.2 | 18.6 |
| Nic Claxton (CHI) | 98% | 20.0<br><sub>-,18,16,22,-</sub> | 7.8<br><sub>-,4,17,2,-</sub> |  | 5.6<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.8 | 0.9 | 15.6 |
| Zach Collins (CHI) | 71% | 18.4<br><sub>14,-,3,-,28</sub> | 7.5<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.5 |
| Leonard Miller (CHI) | 67% | 17.7<br><sub>19,-,2,-,17</sub> | 7.8<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.1<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.1 |
| Buddy Hield (CHI) | 71% | 17.5<br><sub>8,-,-,25,20</sub> | 8.6<br><sub>7,-,-,12,16</sub> |  | 2.6<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.4<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 1.0 | 12.8 |
| Noa Essengue (CHI) | 96% | 13.2<br><sub>14,15,11,8,7</sub> | 5.2<br><sub>6,10,8,5,0</sub> |  | 2.8<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.2 | 0.6 | 8.7 |
| Jordan Hawkins (CHI) | 58% | 12.8<br><sub>7,17,24,-,-</sub> | 5.4<br><sub>2,9,7,-,-</sub> |  | 1.6<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 7.8 |
| Dailyn Swain (CHI) | 52% | 8.5<br><sub>7,-,-,-,-</sub> | 3.0<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.9 | 5.3 |
| James Harden (CLE) | 98% | 34.5<br><sub>34,25,33,35,-</sub> | 19.9<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.6 | 3.0 | 31.7 |
| Donovan Mitchell (CLE) | 98% | 34.4<br><sub>37,23,36,33,-</sub> | 27.8<br><sub>37,11,23,25,-</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 53%</sub> | 3.2<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6 | 0.4 | 2.8 | 38.6 |
| Peyton Watson (CLE) | 100% | 29.4<br><sub>29,21,30,30,-</sub> | 13.0<br><sub>12,13,7,4,-</sub> | 13.5 · – | 5.0<br><sub>6,2,5,4,-</sub> | 4.5 | 2.7<br><sub>3,1,4,2,-</sub> | 2.5 | 1.3<br><sub>1,2,2,0,-</sub> | 1.5 | 1.1 | 1.6 | 1.5 | 20.7 |
| Meleek Thomas (CLE) | 93% | 28.6<br><sub>24,27,22,18,34</sub> | 14.5<br><sub>9,18,14,12,20</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,3,4,0,4</sub> |  | 2.0<br><sub>0,3,1,3,2</sub> |  | 2.5<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.4 | 1.3 | 20.0 |
| Tyrese Proctor (CLE) | 96% | 27.9<br><sub>23,23,23,27,34</sub> | 13.6<br><sub>7,6,15,22,24</sub> |  | 4.6<br><sub>3,1,3,4,11</sub> |  | 4.4<br><sub>3,4,1,3,10</sub> |  | 2.2<br><sub>2,0,3,5,4</sub> |  | 1.2 | 0.1 | 1.2 | 22.7 |
| Jarrett Allen (CLE) | 76% | 27.8<br><sub>-,19,32,32,-</sub> | 14.3<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 9.1<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.5 | 1.3 | 25.0 |
| Mario Hezonja (CLE) | 98% | 22.5<br><sub>19,17,7,9,34</sub> | 9.5<br><sub>0,10,0,4,22</sub> |  | 5.9<br><sub>5,3,0,4,7</sub> |  | 1.8<br><sub>1,0,0,0,4</sub> |  | 1.1<br><sub>0,0,0,0,2</sub> |  | 0.8 | 0.4 | 1.0 | 17.2 |
| Thomas Bryant (CLE) | 72% | 21.3<br><sub>15,15,-,16,27</sub> | 11.8<br><sub>5,11,-,9,19</sub> |  | 5.8<br><sub>3,2,-,1,11</sub> |  | 1.1<br><sub>1,0,-,1,3</sub> |  | 1.4<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.7 | 0.9 | 18.7 |
| Norchad Omier (CLE) | 52% | 20.6<br><sub>-,12,-,-,27</sub> | 6.3<br><sub>-,0,-,-,13</sub> |  | 5.2<br><sub>-,3,-,-,8</sub> |  | 2.1<br><sub>-,2,-,-,2</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.8 | 0.2 | 0.7 | 13.6 |
| Craig Porter Jr. (CLE) | 80% | 19.4<br><sub>15,17,-,9,28</sub> | 4.5<br><sub>0,9,-,0,9</sub> |  | 4.0<br><sub>1,2,-,2,9</sub> |  | 3.5<br><sub>1,4,-,2,6</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.9 | 0.7 | 1.0 | 12.0 |
| Riley Minix (CLE) | 52% | 16.2<br><sub>10,17,-,-,22</sub> | 5.7<br><sub>8,2,-,-,2</sub> |  | 2.2<br><sub>3,2,-,-,0</sub> |  | 0.8<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>2,0,-,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 8.8 |
| Ernest Udeh Jr. (CLE) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Jaylon Tyson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 31.2<br><sub>27,34,25,39,26</sub> | 14.4<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.8 | 29.9 |
| Norman Powell (CHI) | 98% | 31.2<br><sub>22,-,-,31,30</sub> | 21.2<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>1,-,-,2,3</sub> |  | 2.5<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.2 | 27.0 |
| Matas Buzelis (CHI) | 98% | 30.7<br><sub>26,31,31,29,30</sub> | 17.2<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.2<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.1 | 2.3 | 25.2 |
| Isaac Okoro (CHI) | 98% | 29.3<br><sub>15,25,23,41,31</sub> | 9.7<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.8 | 0.4 | 1.0 | 14.4 |
| Patrick Williams (CHI) | 76% | 25.9<br><sub>20,25,28,24,26</sub> | 9.2<br><sub>4,7,9,13,14</sub> |  | 3.6<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.7 |
| Tre Jones (CHI) | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.0<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.2 | 18.6 |
| Nic Claxton (CHI) | 98% | 20.0<br><sub>-,18,16,22,-</sub> | 7.8<br><sub>-,4,17,2,-</sub> |  | 5.7<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.8 | 0.9 | 15.6 |
| Zach Collins (CHI) | 71% | 18.4<br><sub>14,-,3,-,28</sub> | 7.6<br><sub>3,-,2,-,8</sub> |  | 5.2<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.6 |
| Leonard Miller (CHI) | 67% | 17.7<br><sub>19,-,2,-,17</sub> | 7.9<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.1<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.1 |
| Buddy Hield (CHI) | 71% | 17.6<br><sub>8,-,-,25,20</sub> | 8.6<br><sub>7,-,-,12,16</sub> |  | 2.6<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.4<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 1.0 | 12.8 |
| Noa Essengue (CHI) | 96% | 13.2<br><sub>14,15,11,8,7</sub> | 5.3<br><sub>6,10,8,5,0</sub> |  | 2.8<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.2 | 0.6 | 8.8 |
| Jordan Hawkins (CHI) | 58% | 12.9<br><sub>7,17,24,-,-</sub> | 5.5<br><sub>2,9,7,-,-</sub> |  | 1.6<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 7.9 |
| Dailyn Swain (CHI) | 52% | 8.5<br><sub>7,-,-,-,-</sub> | 3.0<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.9 | 5.3 |
| Donovan Mitchell (CLE) | 98% | 34.8<br><sub>37,23,36,33,-</sub> | 28.3<br><sub>37,11,23,25,-</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 53%</sub> | 3.3<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5 | 0.4 | 2.9 | 39.1 |
| James Harden (CLE) | 98% | 34.7<br><sub>34,25,33,35,-</sub> | 20.7<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.6 | 3.2 | 32.6 |
| Jaylon Tyson (CLE) | 100% | 29.4<br><sub>-,-,23,30,34</sub> | 12.5<br><sub>-,-,3,16,18</sub> |  | 5.1<br><sub>-,-,0,3,4</sub> |  | 2.9<br><sub>-,-,1,1,4</sub> |  | 2.0<br><sub>-,-,1,4,3</sub> |  | 1.0 | 0.4 | 1.3 | 20.6 |
| Meleek Thomas (CLE) | 93% | 28.5<br><sub>24,27,22,18,34</sub> | 14.3<br><sub>9,18,14,12,20</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,3,4,0,4</sub> |  | 2.1<br><sub>0,3,1,3,2</sub> |  | 2.5<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 1.3 | 19.8 |
| Tyrese Proctor (CLE) | 96% | 28.4<br><sub>23,23,23,27,34</sub> | 13.8<br><sub>7,6,15,22,24</sub> |  | 4.8<br><sub>3,1,3,4,11</sub> |  | 4.5<br><sub>3,4,1,3,10</sub> |  | 2.3<br><sub>2,0,3,5,4</sub> |  | 1.2 | 0.1 | 1.3 | 23.1 |
| Jarrett Allen (CLE) | 76% | 28.2<br><sub>-,19,32,32,-</sub> | 14.4<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 9.2<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.5 | 1.3 | 25.2 |
| Mario Hezonja (CLE) | 98% | 22.7<br><sub>19,17,7,9,34</sub> | 9.5<br><sub>0,10,0,4,22</sub> |  | 6.0<br><sub>5,3,0,4,7</sub> |  | 1.8<br><sub>1,0,0,0,4</sub> |  | 1.1<br><sub>0,0,0,0,2</sub> |  | 0.8 | 0.4 | 1.0 | 17.3 |
| Thomas Bryant (CLE) | 72% | 21.4<br><sub>15,15,-,16,27</sub> | 11.8<br><sub>5,11,-,9,19</sub> |  | 5.9<br><sub>3,2,-,1,11</sub> |  | 1.1<br><sub>1,0,-,1,3</sub> |  | 1.4<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.7 | 0.9 | 18.8 |
| Norchad Omier (CLE) | 52% | 20.5<br><sub>-,12,-,-,27</sub> | 6.2<br><sub>-,0,-,-,13</sub> |  | 5.3<br><sub>-,3,-,-,8</sub> |  | 2.1<br><sub>-,2,-,-,2</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.8 | 0.2 | 0.7 | 13.6 |
| Craig Porter Jr. (CLE) | 80% | 20.2<br><sub>15,17,-,9,28</sub> | 4.6<br><sub>0,9,-,0,9</sub> |  | 4.1<br><sub>1,2,-,2,9</sub> |  | 3.8<br><sub>1,4,-,2,6</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 1.0 | 0.7 | 1.1 | 12.4 |
| Riley Minix (CLE) | 52% | 16.4<br><sub>10,17,-,-,22</sub> | 5.8<br><sub>8,2,-,-,2</sub> |  | 2.2<br><sub>3,2,-,-,0</sub> |  | 0.8<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>2,0,-,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 8.8 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>


### MEM @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), GG Jackson (MEM), Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 124.5–120.0 | MEM 63% | 1.60 / 2.67 | WAS +4.5 | 244.5 | WAS +3.5 covers 46%; o232.5 74% |
| Expected (weighted by chance each plays) | 125.3–120.3 | MEM 64% | 1.56 / 2.78 | WAS +5.5 | 244.5 | WAS +3.5 covers 45%; o232.5 76% |
| if Zach Edey plays | 124.8–119.2 | MEM 66% | 1.52 / 2.91 | WAS +5.5 | 243.5 | WAS +3.5 covers 43%; o232.5 73% |
| if Tre Johnson plays | 124.7–120.4 | MEM 62% | 1.61 / 2.65 | WAS +4.5 | 244.5 | WAS +3.5 covers 47%; o232.5 75% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey (MEM) | Questionable | 55% | 24.3 | 11.3 | 10.5 | 1.3 | 0.1 | 0.5 | 1.5 | 1.8 | 23.1 | full tables below |
| Felix Okpara (WAS) | Questionable | 55% | 6.0 | 2.3 | 1.7 | 0.4 | 0.1 | 0.2 | 0.2 | 0.4 | 4.3 | small |
| Tre Johnson (WAS) | Questionable | 55% | 21.7 | 9.0 | 2.3 | 1.2 | 1.2 | 0.8 | 0.2 | 0.9 | 12.5 | full tables below |
| Quinten Post (MEM) | Questionable | 55% | 15.8 | 5.9 | 3.2 | 0.8 | 0.7 | 0.6 | 0.3 | 0.6 | 9.9 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 34.2<br><sub>31,33,33,25,29</sub> | 20.5<br><sub>8,22,13,12,15</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>12,7,11,10,8</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 5.7<br><sub>4,8,5,3,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.6 | 3.2 | 36.9 |
| Cedric Coward | 98% | 32.7<br><sub>23,28,27,30,33</sub> | 19.3<br><sub>10,3,15,14,23</sub> | 15.5 · –<br><sub>o 54% · u 46%</sub> | 8.8<br><sub>9,6,11,7,12</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>0,4,4,6,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.1 | 32.0 |
| Jaylen Wells | 98% | 30.4<br><sub>25,26,31,27,25</sub> | 15.8<br><sub>7,14,22,11,5</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>0,4,2,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>0,1,1,1,2</sub> |  | 2.2<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 1.1 | 21.4 |
| Cam Spencer | 98% | 30.0<br><sub>19,17,20,24,34</sub> | 15.8<br><sub>7,7,15,14,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>1,2,3,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 7.3<br><sub>0,4,3,5,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,3,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.3 | 1.8 | 26.9 |
| Javon Small | 96% | 28.5<br><sub>21,24,15,15,30</sub> | 15.6<br><sub>10,9,3,10,19</sub> |  | 4.2<br><sub>4,2,1,2,2</sub> |  | 4.9<br><sub>2,5,4,5,5</sub> |  | 1.8<br><sub>1,1,1,2,3</sub> |  | 1.2 | 0.3 | 1.6 | 24.7 |
| Jerami Grant | 98% | 28.2<br><sub>22,22,20,26,-</sub> | 16.5<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>0,3,2,1,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,2,2,1,-</sub> |  | 2.0<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.6 | 1.6 | 21.7 |
| Taylor Hendricks | 80% | 24.3<br><sub>4,16,11,19,29</sub> | 11.7<br><sub>4,9,7,10,22</sub> |  | 5.6<br><sub>2,3,2,12,5</sub> |  | 1.4<br><sub>0,0,1,2,4</sub> |  | 1.5<br><sub>1,1,1,2,0</sub> |  | 1.2 | 0.7 | 1.1 | 18.7 |
| Kris Murray | 80% | 18.1<br><sub>13,1,-,1,19</sub> | 4.0<br><sub>2,0,-,0,3</sub> |  | 3.2<br><sub>2,0,-,1,2</sub> |  | 1.2<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.4 | 0.6 | 8.5 |
| Olivier-Maxence Prosper | 67% | 18.1<br><sub>11,1,-,2,20</sub> | 10.4<br><sub>2,0,-,6,11</sub> |  | 3.9<br><sub>3,0,-,1,4</sub> |  | 1.1<br><sub>1,0,-,0,0</sub> |  | 1.0<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.3 | 0.8 | 15.5 |
| Jahmai Mashack | 52% | 13.0<br><sub>4,-,-,-,2</sub> | 4.4<br><sub>0,-,-,-,0</sub> |  | 1.8<br><sub>0,-,-,-,0</sub> |  | 1.7<br><sub>2,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.7 | 0.2 | 0.9 | 7.8 |
| Karim Lopez | 52% | 9.8<br><sub>4,-,-,-,2</sub> | 3.3<br><sub>2,-,-,-,0</sub> |  | 2.5<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.3 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.8<br><sub>28,38,34,45,26</sub> | 20.1<br><sub>4,20,15,37,0</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 9.9<br><sub>3,7,4,14,8</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,3,3,4,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.2 | 3.5 | 33.1 |
| Anthony Davis | 98% | 35.5<br><sub>-,34,34,44,31</sub> | 24.6<br><sub>-,44,21,30,14</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 12.3<br><sub>-,13,13,15,8</sub> | 9.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>-,1,0,4,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>-,2,0,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.3 | 2.1 | 2.4 | 40.0 |
| AJ Dybantsa | 98% | 34.8<br><sub>31,37,34,44,30</sub> | 16.1<br><sub>19,21,13,5,16</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>6,8,4,8,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.6 | 2.4 | 25.2 |
| Kyshawn George | 98% | 33.6<br><sub>30,35,39,26,30</sub> | 17.2<br><sub>14,12,25,14,11</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>7,3,9,1,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>6,2,3,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,2,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.3 | 2.3 | 26.8 |
| Alex Sarr | 98% | 29.2<br><sub>28,25,25,44,27</sub> | 14.6<br><sub>15,4,5,30,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 8.2<br><sub>14,8,8,9,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,0,0,2,2</sub> |  | 1.3<br><sub>1,0,1,4,3</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 1.9 | 1.6 | 25.1 |
| Bilal Coulibaly | 98% | 25.6<br><sub>20,-,25,29,21</sub> | 9.3<br><sub>0,-,5,4,9</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,-,6,7,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,-,2,0,0</sub> |  | 0.8<br><sub>0,-,0,0,1</sub> |  | 1.2 | 0.9 | 1.1 | 15.1 |
| Bub Carrington | 98% | 19.2<br><sub>21,19,10,16,23</sub> | 6.6<br><sub>9,4,0,2,11</sub> |  | 2.0<br><sub>6,0,0,0,0</sub> |  | 2.7<br><sub>1,4,0,2,4</sub> |  | 1.1<br><sub>3,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.1 | 11.4 |
| Deandre Ayton | 98% | 14.0<br><sub>7,13,9,9,10</sub> | 5.1<br><sub>2,2,2,2,2</sub> |  | 4.5<br><sub>1,8,2,4,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.6 | 10.2 |
| Khris Middleton | 48% | 12.5<br><sub>-,-,-,-,9</sub> | 4.6<br><sub>-,-,-,-,8</sub> |  | 2.0<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 7.7 |
| Will Riley | 80% | 12.2<br><sub>20,4,-,3,16</sub> | 5.5<br><sub>5,0,-,3,14</sub> |  | 1.6<br><sub>2,0,-,0,3</sub> |  | 0.9<br><sub>1,1,-,0,0</sub> |  | 0.5<br><sub>0,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.7 | 8.1 |
| Tre Mann | 52% | 8.6<br><sub>18,2,-,-,11</sub> | 3.9<br><sub>2,0,-,-,4</sub> |  | 1.1<br><sub>0,0,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 6.0 |
| Anthony Gill | 52% | 7.9<br><sub>9,2,-,-,6</sub> | 2.9<br><sub>1,0,-,-,5</sub> |  | 1.4<br><sub>1,2,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |

</details>

<details><summary>if Zach Edey plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 33.7<br><sub>31,33,33,25,29</sub> | 19.7<br><sub>8,22,13,12,15</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 10.0<br><sub>12,7,11,10,8</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 5.7<br><sub>4,8,5,3,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.6 | 3.2 | 35.3 |
| Cedric Coward (MEM) | 98% | 31.9<br><sub>23,28,27,30,33</sub> | 18.2<br><sub>10,3,15,14,23</sub> | 15.5 · –<br><sub>o 54% · u 46%</sub> | 8.5<br><sub>9,6,11,7,12</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>0,4,4,6,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.0 | 30.3 |
| Jaylen Wells (MEM) | 98% | 29.9<br><sub>25,26,31,27,25</sub> | 14.7<br><sub>7,14,22,11,5</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>0,4,2,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>0,1,1,1,2</sub> |  | 2.0<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.1 | 1.1 | 20.1 |
| Cam Spencer (MEM) | 98% | 28.9<br><sub>19,17,20,24,34</sub> | 14.7<br><sub>7,7,15,14,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,2,3,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 7.5<br><sub>0,4,3,5,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,3,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 1.8 | 25.6 |
| Javon Small (MEM) | 96% | 27.4<br><sub>21,24,15,15,30</sub> | 14.3<br><sub>10,9,3,10,19</sub> |  | 4.0<br><sub>4,2,1,2,2</sub> |  | 5.0<br><sub>2,5,4,5,5</sub> |  | 1.7<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.6 | 23.4 |
| Jerami Grant (MEM) | 98% | 27.1<br><sub>22,22,20,26,-</sub> | 15.4<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>0,3,2,1,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,2,2,1,-</sub> |  | 1.8<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.6 | 1.6 | 20.3 |
| Zach Edey (MEM) | 100% | 24.3<br><sub>20,23,20,-,-</sub> | 11.3<br><sub>14,8,2,-,-</sub> | 8.5 · – | 10.5<br><sub>6,9,5,-,-</sub> | 7.5 | 1.3<br><sub>1,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.5 | 1.5 | 1.8 | 23.1 |
| Taylor Hendricks (MEM) | 80% | 22.0<br><sub>4,16,11,19,29</sub> | 10.5<br><sub>4,9,7,10,22</sub> |  | 5.0<br><sub>2,3,2,12,5</sub> |  | 1.3<br><sub>0,0,1,2,4</sub> |  | 1.2<br><sub>1,1,1,2,0</sub> |  | 1.1 | 0.6 | 1.1 | 16.8 |
| Kris Murray (MEM) | 80% | 16.1<br><sub>13,1,-,1,19</sub> | 3.7<br><sub>2,0,-,0,3</sub> |  | 2.8<br><sub>2,0,-,1,2</sub> |  | 1.1<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.6 | 0.3 | 0.6 | 7.6 |
| Olivier-Maxence Prosper (MEM) | 67% | 16.1<br><sub>11,1,-,2,20</sub> | 8.8<br><sub>2,0,-,6,11</sub> |  | 3.5<br><sub>3,0,-,1,4</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>0,0,-,0,2</sub> |  | 0.7 | 0.2 | 0.8 | 13.2 |
| Jahmai Mashack (MEM) | 52% | 11.3<br><sub>4,-,-,-,2</sub> | 3.7<br><sub>0,-,-,-,0</sub> |  | 1.5<br><sub>0,-,-,-,0</sub> |  | 1.5<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 6.6 |
| Karim Lopez (MEM) | 52% | 7.8<br><sub>4,-,-,-,2</sub> | 2.8<br><sub>2,-,-,-,0</sub> |  | 1.9<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.5 | 5.1 |
| Trae Young (WAS) | 98% | 35.8<br><sub>28,38,34,45,26</sub> | 20.0<br><sub>4,20,15,37,0</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 9.8<br><sub>3,7,4,14,8</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,3,3,4,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.2 | 3.5 | 33.0 |
| Anthony Davis (WAS) | 98% | 35.4<br><sub>-,34,34,44,31</sub> | 24.4<br><sub>-,44,21,30,14</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 12.3<br><sub>-,13,13,15,8</sub> | 9.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>-,1,0,4,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>-,2,0,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.3 | 2.1 | 2.3 | 39.8 |
| AJ Dybantsa (WAS) | 98% | 34.8<br><sub>31,37,34,44,30</sub> | 16.1<br><sub>19,21,13,5,16</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>6,8,4,8,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.6 | 2.4 | 25.1 |
| Kyshawn George (WAS) | 98% | 33.6<br><sub>30,35,39,26,30</sub> | 17.2<br><sub>14,12,25,14,11</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>7,3,9,1,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>6,2,3,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,2,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.3 | 2.3 | 26.8 |
| Alex Sarr (WAS) | 98% | 29.2<br><sub>28,25,25,44,27</sub> | 14.6<br><sub>15,4,5,30,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 8.2<br><sub>14,8,8,9,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,0,0,2,2</sub> |  | 1.3<br><sub>1,0,1,4,3</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 1.9 | 1.6 | 25.0 |
| Bilal Coulibaly (WAS) | 98% | 25.5<br><sub>20,-,25,29,21</sub> | 9.3<br><sub>0,-,5,4,9</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,-,6,7,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,-,2,0,0</sub> |  | 0.8<br><sub>0,-,0,0,1</sub> |  | 1.2 | 0.9 | 1.1 | 15.1 |
| Bub Carrington (WAS) | 98% | 19.2<br><sub>21,19,10,16,23</sub> | 6.6<br><sub>9,4,0,2,11</sub> |  | 2.0<br><sub>6,0,0,0,0</sub> |  | 2.7<br><sub>1,4,0,2,4</sub> |  | 1.1<br><sub>3,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.1 | 11.4 |
| Deandre Ayton (WAS) | 98% | 14.0<br><sub>7,13,9,9,10</sub> | 5.0<br><sub>2,2,2,2,2</sub> |  | 4.5<br><sub>1,8,2,4,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.6 | 10.1 |
| Khris Middleton (WAS) | 48% | 12.6<br><sub>-,-,-,-,9</sub> | 4.6<br><sub>-,-,-,-,8</sub> |  | 2.0<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 7.7 |
| Will Riley (WAS) | 80% | 12.4<br><sub>20,4,-,3,16</sub> | 5.6<br><sub>5,0,-,3,14</sub> |  | 1.6<br><sub>2,0,-,0,3</sub> |  | 0.9<br><sub>1,1,-,0,0</sub> |  | 0.5<br><sub>0,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.7 | 8.1 |
| Tre Mann (WAS) | 52% | 8.7<br><sub>18,2,-,-,11</sub> | 3.9<br><sub>2,0,-,-,4</sub> |  | 1.1<br><sub>0,0,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 6.0 |
| Anthony Gill (WAS) | 52% | 7.9<br><sub>9,2,-,-,6</sub> | 2.9<br><sub>1,0,-,-,5</sub> |  | 1.4<br><sub>1,2,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |

</details>

<details><summary>if Tre Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 34.3<br><sub>31,33,33,25,29</sub> | 20.6<br><sub>8,22,13,12,15</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>12,7,11,10,8</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 5.7<br><sub>4,8,5,3,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.6 | 3.2 | 36.9 |
| Cedric Coward (MEM) | 98% | 32.6<br><sub>23,28,27,30,33</sub> | 19.2<br><sub>10,3,15,14,23</sub> | 15.5 · –<br><sub>o 54% · u 46%</sub> | 8.8<br><sub>9,6,11,7,12</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>0,4,4,6,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.1 | 31.8 |
| Jaylen Wells (MEM) | 98% | 30.4<br><sub>25,26,31,27,25</sub> | 15.8<br><sub>7,14,22,11,5</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>0,4,2,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>0,1,1,1,2</sub> |  | 2.2<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.2 | 1.1 | 21.4 |
| Cam Spencer (MEM) | 98% | 30.0<br><sub>19,17,20,24,34</sub> | 15.8<br><sub>7,7,15,14,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>1,2,3,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 7.4<br><sub>0,4,3,5,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,3,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 1.8 | 27.0 |
| Javon Small (MEM) | 96% | 28.5<br><sub>21,24,15,15,30</sub> | 15.6<br><sub>10,9,3,10,19</sub> |  | 4.2<br><sub>4,2,1,2,2</sub> |  | 5.0<br><sub>2,5,4,5,5</sub> |  | 1.8<br><sub>1,1,1,2,3</sub> |  | 1.2 | 0.3 | 1.6 | 24.7 |
| Jerami Grant (MEM) | 98% | 28.1<br><sub>22,22,20,26,-</sub> | 16.4<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>0,3,2,1,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,2,2,1,-</sub> |  | 2.0<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.6 | 1.6 | 21.5 |
| Taylor Hendricks (MEM) | 80% | 24.3<br><sub>4,16,11,19,29</sub> | 11.7<br><sub>4,9,7,10,22</sub> |  | 5.6<br><sub>2,3,2,12,5</sub> |  | 1.4<br><sub>0,0,1,2,4</sub> |  | 1.5<br><sub>1,1,1,2,0</sub> |  | 1.2 | 0.7 | 1.1 | 18.8 |
| Olivier-Maxence Prosper (MEM) | 67% | 18.2<br><sub>11,1,-,2,20</sub> | 10.4<br><sub>2,0,-,6,11</sub> |  | 3.9<br><sub>3,0,-,1,4</sub> |  | 1.1<br><sub>1,0,-,0,0</sub> |  | 1.0<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.2 | 0.8 | 15.5 |
| Kris Murray (MEM) | 80% | 18.1<br><sub>13,1,-,1,19</sub> | 4.0<br><sub>2,0,-,0,3</sub> |  | 3.2<br><sub>2,0,-,1,2</sub> |  | 1.2<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.4 | 0.6 | 8.5 |
| Jahmai Mashack (MEM) | 52% | 13.0<br><sub>4,-,-,-,2</sub> | 4.4<br><sub>0,-,-,-,0</sub> |  | 1.8<br><sub>0,-,-,-,0</sub> |  | 1.7<br><sub>2,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.7 | 0.2 | 0.9 | 7.9 |
| Karim Lopez (MEM) | 52% | 9.8<br><sub>4,-,-,-,2</sub> | 3.3<br><sub>2,-,-,-,0</sub> |  | 2.5<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.3 |
| Anthony Davis (WAS) | 98% | 33.6<br><sub>-,34,34,44,31</sub> | 23.3<br><sub>-,44,21,30,14</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 11.6<br><sub>-,13,13,15,8</sub> | 9.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>-,1,0,4,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>-,2,0,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.2 | 1.9 | 2.2 | 37.9 |
| Trae Young (WAS) | 98% | 33.5<br><sub>28,38,34,45,26</sub> | 18.5<br><sub>4,20,15,37,0</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 9.3<br><sub>3,7,4,14,8</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>0,3,3,4,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.2 | 30.8 |
| AJ Dybantsa (WAS) | 98% | 32.4<br><sub>31,37,34,44,30</sub> | 15.3<br><sub>19,21,13,5,16</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>6,8,4,8,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.6 | 2.3 | 23.8 |
| Kyshawn George (WAS) | 98% | 31.1<br><sub>30,35,39,26,30</sub> | 15.6<br><sub>14,12,25,14,11</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>7,3,9,1,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>6,2,3,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,2,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 1.2 | 2.2 | 24.4 |
| Alex Sarr (WAS) | 98% | 26.8<br><sub>28,25,25,44,27</sub> | 13.9<br><sub>15,4,5,30,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>14,8,8,9,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>1,0,0,2,2</sub> |  | 1.2<br><sub>1,0,1,4,3</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 1.8 | 1.4 | 23.4 |
| Bilal Coulibaly (WAS) | 98% | 22.6<br><sub>20,-,25,29,21</sub> | 8.4<br><sub>0,-,5,4,9</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 3.7<br><sub>5,-,6,7,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>0,-,2,0,0</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 1.1 | 0.8 | 1.1 | 13.5 |
| Tre Johnson (WAS) | 100% | 21.7<br><sub>28,29,29,30,-</sub> | 9.0<br><sub>4,2,15,13,-</sub> |  | 2.3<br><sub>0,2,3,4,-</sub> |  | 1.2<br><sub>3,0,1,2,-</sub> |  | 1.2<br><sub>0,0,2,1,-</sub> |  | 0.8 | 0.2 | 0.9 | 12.5 |
| Bub Carrington (WAS) | 98% | 17.1<br><sub>21,19,10,16,23</sub> | 6.0<br><sub>9,4,0,2,11</sub> |  | 1.8<br><sub>6,0,0,0,0</sub> |  | 2.6<br><sub>1,4,0,2,4</sub> |  | 0.9<br><sub>3,1,0,0,3</sub> |  | 0.5 | 0.2 | 1.1 | 10.4 |
| Deandre Ayton (WAS) | 98% | 12.9<br><sub>7,13,9,9,10</sub> | 4.9<br><sub>2,2,2,2,2</sub> |  | 4.3<br><sub>1,8,2,4,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.6 | 9.7 |
| Khris Middleton (WAS) | 48% | 11.2<br><sub>-,-,-,-,9</sub> | 4.2<br><sub>-,-,-,-,8</sub> |  | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 7.0 |
| Will Riley (WAS) | 80% | 10.0<br><sub>20,4,-,3,16</sub> | 4.7<br><sub>5,0,-,3,14</sub> |  | 1.3<br><sub>2,0,-,0,3</sub> |  | 0.9<br><sub>1,1,-,0,0</sub> |  | 0.4<br><sub>0,0,-,1,2</sub> |  | 0.4 | 0.1 | 0.6 | 6.9 |
| Anthony Gill (WAS) | 52% | 7.3<br><sub>9,2,-,-,6</sub> | 2.8<br><sub>1,0,-,-,5</sub> |  | 1.3<br><sub>1,2,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |
| Tre Mann (WAS) | 52% | 7.2<br><sub>18,2,-,-,11</sub> | 3.4<br><sub>2,0,-,-,4</sub> |  | 1.0<br><sub>0,0,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,1</sub> |  | 0.2<br><sub>0,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |

</details>


### PHI @ BKN
Out: Grant Nelson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Dominick Barlow (PHI), Adem Bona (PHI), Ariel Hukporti (PHI), LeBron James (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.7–112.0 | PHI 52% | 1.91 / 2.10 | BKN +1.5 | 224.5 | BKN +4.5 covers 60%; o225.5 48% |
| Expected (weighted by chance each plays) | 113.8–112.0 | PHI 56% | 1.80 / 2.25 | BKN +2.5 | 225.5 | BKN +4.5 covers 57%; o225.5 51% |
| if Joel Embiid plays | 114.6–111.8 | PHI 58% | 1.71 / 2.40 | BKN +3.5 | 226.5 | BKN +4.5 covers 54%; o225.5 52% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Joel Embiid (PHI) | Questionable | 55% | 33.2 | 23.7 | 8.5 | 4.7 | 1.0 | 0.9 | 1.1 | 3.2 | 36.9 | full tables below |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.0<br><sub>32,36,34,35,36</sub> | 29.1<br><sub>17,27,24,27,27</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,4,1,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>4,7,4,8,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>2,3,3,1,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.5 | 0.7 | 2.9 | 40.0 |
| Jaylen Brown | 98% | 36.1<br><sub>34,35,26,36,32</sub> | 27.6<br><sub>20,29,13,18,31</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,7,5,6,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>5,4,2,2,2</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>2,2,1,0,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.6 | 3.9 | 39.5 |
| VJ Edgecombe | 96% | 36.0<br><sub>32,35,32,36,31</sub> | 17.3<br><sub>19,13,8,15,11</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>3,6,4,8,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 5.0<br><sub>2,3,5,8,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>3,3,0,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.6 | 1.9 | 28.6 |
| Dean Wade | 96% | 33.2<br><sub>21,18,23,34,35</sub> | 6.0<br><sub>0,0,8,6,12</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,1,9,5,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,1,0,2,3</sub> |  | 0.9<br><sub>0,0,2,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 0.8 | 13.6 |
| Kentavious Caldwell-Pope | 98% | 25.6<br><sub>17,21,16,27,22</sub> | 7.1<br><sub>5,6,0,11,9</sub> |  | 3.1<br><sub>2,6,0,4,5</sub> |  | 2.1<br><sub>0,3,2,5,0</sub> |  | 1.0<br><sub>1,2,0,3,2</sub> |  | 1.1 | 0.4 | 0.9 | 12.3 |
| Jabari Walker | 88% | 25.5<br><sub>17,19,15,16,25</sub> | 9.9<br><sub>8,9,2,9,11</sub> |  | 7.2<br><sub>5,11,4,8,7</sub> |  | 1.3<br><sub>1,0,0,1,1</sub> |  | 1.0<br><sub>0,1,0,1,3</sub> |  | 0.8 | 0.3 | 1.0 | 18.5 |
| Anfernee Simons | 98% | 24.9<br><sub>19,16,18,23,15</sub> | 13.3<br><sub>6,3,17,17,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>2,4,3,3,0</sub> |  | 2.0<br><sub>2,2,0,2,0</sub> |  | 2.3<br><sub>1,1,3,5,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.6 | 0.1 | 1.2 | 17.9 |
| Justin Edwards | 52% | 13.1<br><sub>4,-,6,1,-</sub> | 5.1<br><sub>3,-,0,0,-</sub> |  | 1.8<br><sub>1,-,0,1,-</sub> |  | 0.9<br><sub>0,-,0,0,-</sub> |  | 0.6<br><sub>1,-,0,0,-</sub> |  | 0.6 | 0.2 | 0.6 | 7.8 |
| Rayan Rupert | 47% | 13.0<br><sub>-,-,6,-,-</sub> | 4.7<br><sub>-,-,0,-,-</sub> |  | 2.6<br><sub>-,-,1,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.8 | 0.2 | 0.8 | 8.3 |
| Tacko Fall | 76% | 11.8<br><sub>3,-,-,1,5</sub> | 0.7<br><sub>0,-,-,0,0</sub> |  | 2.8<br><sub>1,-,-,0,3</sub> |  | 0.4<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 3.9 |
| Labaron Philon Jr. | 72% | 11.6<br><sub>4,-,6,2,6</sub> | 4.3<br><sub>3,-,2,0,3</sub> |  | 1.7<br><sub>1,-,1,0,1</sub> |  | 1.0<br><sub>1,-,3,0,0</sub> |  | 0.4<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.1 | 0.6 | 7.1 |
| Caleb Love | 38% | 9.7<br><sub>-,-,-,1,-</sub> | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 1.5 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 76% | 31.9<br><sub>38,36,29,28,-</sub> | 20.7<br><sub>26,25,19,22,-</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>10,9,9,6,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>0,1,0,3,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>4,3,4,4,-</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.0 | 29.6 |
| Julius Randle | 98% | 31.7<br><sub>31,34,30,29,31</sub> | 18.6<br><sub>22,19,13,17,22</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>3,7,4,4,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,8,4,5,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.8 | 0.2 | 3.1 | 29.6 |
| Day'Ron Sharpe | 98% | 24.1<br><sub>27,32,20,19,28</sub> | 10.1<br><sub>6,12,6,15,16</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 8.0<br><sub>5,10,4,4,11</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>8,13,6,5,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.9 | 1.8 | 22.1 |
| Egor Demin | 98% | 23.5<br><sub>-,-,-,23,27</sub> | 9.9<br><sub>-,-,-,22,11</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>-,-,-,1,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>-,-,-,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>-,-,-,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.3 | 1.5 | 15.5 |
| Danny Wolf | 76% | 22.8<br><sub>19,31,36,29,28</sub> | 9.7<br><sub>12,11,10,10,14</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 5.7<br><sub>5,9,3,11,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>2,2,1,1,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.5 | 0.6 | 1.2 | 17.5 |
| Mikel Brown Jr. | 97% | 21.9<br><sub>20,25,-,-,20</sub> | 10.7<br><sub>18,18,-,-,6</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>2,1,-,-,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>4,3,-,-,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,3,-,-,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.2 | 1.8 | 16.4 |
| Nolan Traore | 98% | 21.6<br><sub>27,23,21,-,20</sub> | 10.9<br><sub>16,19,14,-,11</sub> |  | 2.0<br><sub>4,1,1,-,1</sub> |  | 3.2<br><sub>2,2,2,-,2</sub> |  | 1.2<br><sub>2,2,2,-,0</sub> |  | 0.8 | 0.4 | 2.2 | 16.1 |
| Noah Clowney | 98% | 21.5<br><sub>17,21,8,19,35</sub> | 8.4<br><sub>7,3,2,16,15</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>1,10,0,3,7</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>1,0,0,0,3</sub> |  | 1.1<br><sub>1,1,0,2,3</sub> |  | 0.5 | 0.6 | 1.0 | 13.6 |
| Moritz Wagner | 96% | 17.0<br><sub>20,16,16,19,18</sub> | 9.2<br><sub>6,9,12,16,10</sub> |  | 4.1<br><sub>1,2,3,3,6</sub> |  | 1.3<br><sub>0,0,1,4,4</sub> |  | 0.7<br><sub>0,1,1,2,2</sub> |  | 0.5 | 0.2 | 0.9 | 14.5 |
| Keon Ellis | 88% | 14.9<br><sub>10,-,22,26,7</sub> | 3.8<br><sub>1,-,3,11,0</sub> |  | 1.5<br><sub>2,-,1,4,0</sub> |  | 1.1<br><sub>0,-,4,3,1</sub> |  | 0.4<br><sub>0,-,1,2,0</sub> |  | 0.8 | 0.4 | 0.4 | 6.4 |
| Chaney Johnson | 97% | 12.9<br><sub>9,8,15,15,12</sub> | 3.7<br><sub>0,5,2,4,1</sub> |  | 2.2<br><sub>2,2,0,3,5</sub> |  | 0.7<br><sub>1,1,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 6.6 |
| Terance Mann | 80% | 12.6<br><sub>16,13,22,18,9</sub> | 3.3<br><sub>0,0,0,6,2</sub> |  | 1.5<br><sub>2,2,1,1,1</sub> |  | 1.3<br><sub>2,0,1,3,1</sub> |  | 0.3<br><sub>0,0,0,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.1 |
| Josh Minott | 67% | 7.7<br><sub>6,-,12,7,2</sub> | 4.0<br><sub>0,-,10,0,0</sub> |  | 1.6<br><sub>1,-,2,2,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.4<br><sub>0,-,2,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.0 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. (BKN) | 76% | 31.8<br><sub>38,36,29,28,-</sub> | 20.6<br><sub>26,25,19,22,-</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>10,9,9,6,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>0,1,0,3,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>4,3,4,4,-</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.4 | 2.0 | 29.5 |
| Julius Randle (BKN) | 98% | 31.7<br><sub>31,34,30,29,31</sub> | 18.7<br><sub>22,19,13,17,22</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>3,7,4,4,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,8,4,5,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.8 | 0.2 | 3.1 | 29.6 |
| Day'Ron Sharpe (BKN) | 98% | 24.2<br><sub>27,32,20,19,28</sub> | 10.0<br><sub>6,12,6,15,16</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 8.0<br><sub>5,10,4,4,11</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>8,13,6,5,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.9 | 1.9 | 22.1 |
| Egor Demin (BKN) | 98% | 23.4<br><sub>-,-,-,23,27</sub> | 9.9<br><sub>-,-,-,22,11</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>-,-,-,1,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>-,-,-,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>-,-,-,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.6 | 0.3 | 1.5 | 15.4 |
| Danny Wolf (BKN) | 76% | 22.9<br><sub>19,31,36,29,28</sub> | 9.7<br><sub>12,11,10,10,14</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 5.7<br><sub>5,9,3,11,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>2,2,1,1,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.5 | 0.6 | 1.2 | 17.5 |
| Mikel Brown Jr. (BKN) | 97% | 22.0<br><sub>20,25,-,-,20</sub> | 10.7<br><sub>18,18,-,-,6</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>2,1,-,-,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>4,3,-,-,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,3,-,-,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.2 | 1.8 | 16.6 |
| Noah Clowney (BKN) | 98% | 21.6<br><sub>17,21,8,19,35</sub> | 8.4<br><sub>7,3,2,16,15</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>1,10,0,3,7</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>1,0,0,0,3</sub> |  | 1.1<br><sub>1,1,0,2,3</sub> |  | 0.5 | 0.6 | 1.0 | 13.6 |
| Nolan Traore (BKN) | 98% | 21.6<br><sub>27,23,21,-,20</sub> | 10.9<br><sub>16,19,14,-,11</sub> |  | 2.0<br><sub>4,1,1,-,1</sub> |  | 3.2<br><sub>2,2,2,-,2</sub> |  | 1.2<br><sub>2,2,2,-,0</sub> |  | 0.8 | 0.4 | 2.2 | 16.1 |
| Moritz Wagner (BKN) | 96% | 17.0<br><sub>20,16,16,19,18</sub> | 9.2<br><sub>6,9,12,16,10</sub> |  | 4.1<br><sub>1,2,3,3,6</sub> |  | 1.3<br><sub>0,0,1,4,4</sub> |  | 0.8<br><sub>0,1,1,2,2</sub> |  | 0.5 | 0.2 | 1.0 | 14.7 |
| Keon Ellis (BKN) | 88% | 14.9<br><sub>10,-,22,26,7</sub> | 3.9<br><sub>1,-,3,11,0</sub> |  | 1.5<br><sub>2,-,1,4,0</sub> |  | 1.1<br><sub>0,-,4,3,1</sub> |  | 0.4<br><sub>0,-,1,2,0</sub> |  | 0.8 | 0.4 | 0.4 | 6.4 |
| Chaney Johnson (BKN) | 97% | 12.9<br><sub>9,8,15,15,12</sub> | 3.6<br><sub>0,5,2,4,1</sub> |  | 2.2<br><sub>2,2,0,3,5</sub> |  | 0.7<br><sub>1,1,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 6.5 |
| Terance Mann (BKN) | 80% | 12.6<br><sub>16,13,22,18,9</sub> | 3.3<br><sub>0,0,0,6,2</sub> |  | 1.5<br><sub>2,2,1,1,1</sub> |  | 1.2<br><sub>2,0,1,3,1</sub> |  | 0.3<br><sub>0,0,0,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.1 |
| Josh Minott (BKN) | 67% | 7.7<br><sub>6,-,12,7,2</sub> | 4.0<br><sub>0,-,10,0,0</sub> |  | 1.5<br><sub>1,-,2,2,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.4<br><sub>0,-,2,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.0 |
| Tyrese Maxey (PHI) | 98% | 37.6<br><sub>32,36,34,35,36</sub> | 25.8<br><sub>17,27,24,27,27</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,4,1,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>4,7,4,8,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>2,3,3,1,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.6 | 2.4 | 35.7 |
| Jaylen Brown (PHI) | 98% | 35.7<br><sub>34,35,26,36,32</sub> | 24.2<br><sub>20,29,13,18,31</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>5,7,5,6,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>5,4,2,2,2</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.0<br><sub>2,2,1,0,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.5 | 3.3 | 34.5 |
| VJ Edgecombe (PHI) | 96% | 35.1<br><sub>32,35,32,36,31</sub> | 14.5<br><sub>19,13,8,15,11</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>3,6,4,8,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>2,3,5,8,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>3,3,0,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.5 | 1.7 | 24.6 |
| Joel Embiid (PHI) | 100% | 33.2<br><sub>25,29,31,28,-</sub> | 23.7<br><sub>6,18,16,20,-</sub> | 21.5 · – | 8.5<br><sub>7,10,6,4,-</sub> | 7.5 | 4.7<br><sub>1,5,1,3,-</sub> | 3.5 | 1.0<br><sub>0,0,1,0,-</sub> | 0.5 | 0.9 | 1.1 | 3.2 | 36.9 |
| Dean Wade (PHI) | 96% | 31.1<br><sub>21,18,23,34,35</sub> | 5.8<br><sub>0,0,8,6,12</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>5,1,9,5,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,1,0,2,3</sub> |  | 0.9<br><sub>0,0,2,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 0.9 | 12.6 |
| Kentavious Caldwell-Pope (PHI) | 98% | 22.4<br><sub>17,21,16,27,22</sub> | 5.6<br><sub>5,6,0,11,9</sub> |  | 2.5<br><sub>2,6,0,4,5</sub> |  | 1.8<br><sub>0,3,2,5,0</sub> |  | 0.8<br><sub>1,2,0,3,2</sub> |  | 0.9 | 0.3 | 0.7 | 9.8 |
| Anfernee Simons (PHI) | 98% | 21.8<br><sub>19,16,18,23,15</sub> | 10.3<br><sub>6,3,17,17,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,4,3,3,0</sub> |  | 1.7<br><sub>2,2,0,2,0</sub> |  | 1.8<br><sub>1,1,3,5,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.5 | 0.1 | 0.9 | 14.1 |
| Jabari Walker (PHI) | 88% | 21.6<br><sub>17,19,15,16,25</sub> | 7.9<br><sub>8,9,2,9,11</sub> |  | 5.8<br><sub>5,11,4,8,7</sub> |  | 1.1<br><sub>1,0,0,1,1</sub> |  | 0.8<br><sub>0,1,0,1,3</sub> |  | 0.7 | 0.3 | 0.9 | 14.8 |
| Justin Edwards (PHI) | 52% | 9.3<br><sub>4,-,6,1,-</sub> | 3.4<br><sub>3,-,0,0,-</sub> |  | 1.3<br><sub>1,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.3<br><sub>1,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.2 |
| Rayan Rupert (PHI) | 47% | 9.3<br><sub>-,-,6,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 1.8<br><sub>-,-,1,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.1 | 0.5 | 5.4 |
| Tacko Fall (PHI) | 76% | 8.8<br><sub>3,-,-,1,5</sub> | 0.5<br><sub>0,-,-,0,0</sub> |  | 2.2<br><sub>1,-,-,0,3</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 3.0 |
| Labaron Philon Jr. (PHI) | 72% | 8.8<br><sub>4,-,6,2,6</sub> | 3.1<br><sub>3,-,2,0,3</sub> |  | 1.2<br><sub>1,-,1,0,1</sub> |  | 0.7<br><sub>1,-,3,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.1 |
| Caleb Love (PHI) | 38% | 8.2<br><sub>-,-,-,1,-</sub> | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 1.2 |

</details>


### HOU @ MIA
Out: Steven Adams (HOU), Clint Capela (HOU), Marcus Smart (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.0–118.9 | HOU 48% | 2.10 / 1.91 | MIA -1.5 | 236.5 | MIA +1.5 covers 55%; o231.5 61% |
| Expected (weighted by chance each plays) | 118.6–118.8 | HOU 49% | 2.02 / 1.98 | MIA +0.5 | 237.5 | MIA +1.5 covers 54%; o231.5 62% |
| if Pelle Larsson plays | 117.0–120.1 | HOU 41% | 2.42 / 1.71 | MIA -3.5 | 236.5 | MIA +1.5 covers 62%; o231.5 62% |
| if Amen Thompson plays | 119.7–117.8 | HOU 56% | 1.80 / 2.25 | MIA +2.5 | 237.5 | MIA +1.5 covers 48%; o231.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jovic (MIA) | Questionable | 55% | 12.7 | 4.2 | 2.1 | 1.1 | 0.4 | 0.4 | 0.3 | 0.6 | 7.4 | small |
| Pelle Larsson (MIA) | Doubtful | 20% | 28.5 | 11.5 | 3.4 | 3.1 | 1.0 | 0.9 | 0.2 | 1.7 | 18.0 | full tables below |
| Amen Thompson (HOU) | Questionable | 55% | 36.9 | 17.5 | 7.6 | 4.8 | 0.3 | 1.5 | 0.8 | 2.2 | 29.9 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alperen Sengun | 91% | 37.2<br><sub>32,35,37,37,28</sub> | 24.4<br><sub>15,20,19,43,19</sub> | 19.5 · –<br><sub>o 53% · u 47%</sub> | 10.4<br><sub>6,12,13,12,8</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>5,8,9,5,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.2 | 1.2 | 3.2 | 42.0 |
| Jabari Smith Jr. | 98% | 36.7<br><sub>39,38,35,24,28</sub> | 17.5<br><sub>15,14,14,6,9</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>9,7,8,3,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,3,0,0,5</sub> |  | 2.6<br><sub>1,2,2,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.9 | 1.5 | 27.4 |
| Kevin Durant | 98% | 36.7<br><sub>38,36,34,33,30</sub> | 25.9<br><sub>21,23,20,22,25</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>10,12,4,3,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>3,8,5,6,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.9 | 3.4 | 37.8 |
| Fred VanVleet | 71% | 35.5<br><sub>31,30,30,34,-</sub> | 17.1<br><sub>16,12,18,17,-</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,1,2,2,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.8<br><sub>4,2,6,3,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,3,4,3,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.5 | 1.6 | 26.9 |
| Tari Eason | 98% | 31.4<br><sub>23,19,22,33,30</sub> | 13.2<br><sub>2,12,6,14,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>7,5,3,11,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,2,0,2,1</sub> |  | 1.6<br><sub>0,2,0,2,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.8 | 1.4 | 22.9 |
| Reed Sheppard | 91% | 30.7<br><sub>13,17,20,19,26</sub> | 15.4<br><sub>6,8,13,0,11</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>0,0,1,0,1</sub> |  | 4.3<br><sub>0,0,1,3,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.7 | 1.5 | 22.7 |
| Bogdan Bogdanovic | 97% | 23.4<br><sub>2,12,10,12,22</sub> | 9.3<br><sub>0,8,0,11,12</sub> |  | 3.0<br><sub>1,3,0,1,3</sub> |  | 2.4<br><sub>0,1,0,3,4</sub> |  | 1.5<br><sub>0,2,0,3,2</sub> |  | 0.7 | 0.2 | 0.9 | 14.8 |
| Oscar Tshiebwe | 93% | 15.9<br><sub>3,-,1,6,12</sub> | 5.5<br><sub>2,-,0,0,4</sub> |  | 7.1<br><sub>0,-,0,5,9</sub> |  | 1.0<br><sub>0,-,0,0,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.4 | 0.6 | 13.7 |
| Bruce Thornton | 63% | 12.8<br><sub>-,1,3,-,6</sub> | 3.6<br><sub>-,0,0,-,2</sub> |  | 2.2<br><sub>-,0,0,-,0</sub> |  | 0.8<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.1 | 0.6 | 6.5 |
| Isaiah Crawford | 63% | 12.5<br><sub>-,1,1,-,9</sub> | 3.6<br><sub>-,0,0,-,4</sub> |  | 2.1<br><sub>-,0,0,-,2</sub> |  | 0.6<br><sub>-,0,0,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.3 |
| Jae'Sean Tate | 58% | 12.3<br><sub>-,-,1,-,8</sub> | 3.6<br><sub>-,-,0,-,4</sub> |  | 3.0<br><sub>-,-,0,-,2</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.4 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 37.7<br><sub>38,40,38,39,32</sub> | 15.1<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 8.9<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.3 | 2.2 | 27.1 |
| Bam Adebayo | 98% | 37.1<br><sub>33,34,37,38,36</sub> | 20.5<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 9.9<br><sub>10,8,8,14,5</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,1,0,2,1</sub> |  | 1.7 | 0.8 | 1.7 | 34.2 |
| Giannis Antetokounmpo | 98% | 35.3<br><sub>31,34,31,31,31</sub> | 29.6<br><sub>20,29,30,37,34</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 12.2<br><sub>14,14,11,9,14</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 6.1<br><sub>4,3,4,2,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 41% · u 59%</sub> | 1.1 | 1.1 | 3.5 | 47.8 |
| Andrew Wiggins | 98% | 28.8<br><sub>21,32,19,32,23</sub> | 11.1<br><sub>2,6,13,8,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.8 | 1.1 | 16.6 |
| Klay Thompson | 83% | 28.4<br><sub>23,32,30,-,20</sub> | 13.7<br><sub>11,23,11,-,26</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>0,2,1,-,1</sub> |  | 2.0<br><sub>3,4,2,-,4</sub> |  | 2.9<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.6 | 1.3 | 18.0 |
| Ryan Conwell | 91% | 24.7<br><sub>30,19,21,33,26</sub> | 8.9<br><sub>13,6,5,20,9</sub> |  | 2.8<br><sub>1,2,4,5,4</sub> |  | 1.7<br><sub>2,2,2,2,1</sub> |  | 1.5<br><sub>3,2,1,4,2</sub> |  | 0.8 | 0.2 | 1.0 | 13.4 |
| Bobby Portis | 98% | 20.5<br><sub>14,20,17,15,18</sub> | 8.2<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 5.3<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,2,2</sub> |  | 1.1<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 0.3 | 0.7 | 14.8 |
| Myron Gardner | 67% | 16.8<br><sub>1,-,10,19,26</sub> | 4.7<br><sub>0,-,4,0,5</sub> |  | 4.3<br><sub>0,-,3,4,9</sub> |  | 1.5<br><sub>0,-,1,2,3</sub> |  | 0.5<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.5 | 0.6 | 10.6 |
| Tim Hardaway Jr. | 64% | 16.6<br><sub>4,7,-,20,-</sub> | 6.4<br><sub>0,0,-,4,-</sub> |  | 1.7<br><sub>0,0,-,3,-</sub> |  | 0.8<br><sub>1,0,-,2,-</sub> |  | 0.9<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 8.9 |
| Simone Fontecchio | 64% | 12.7<br><sub>-,-,7,7,14</sub> | 5.3<br><sub>-,-,3,0,7</sub> |  | 2.1<br><sub>-,-,0,0,5</sub> |  | 0.9<br><sub>-,-,0,2,0</sub> |  | 0.8<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.3 |
| Dru Smith | 52% | 11.8<br><sub>1,-,-,6,-</sub> | 3.6<br><sub>0,-,-,0,-</sub> |  | 1.5<br><sub>0,-,-,0,-</sub> |  | 1.7<br><sub>0,-,-,1,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.9 | 0.2 | 0.6 | 6.8 |
| Keshad Johnson | 52% | 8.6<br><sub>-,-,-,-,1</sub> | 3.4<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.6 |
| Nick Richards | 38% | 7.7<br><sub>1,-,-,-,-</sub> | 2.7<br><sub>0,-,-,-,-</sub> |  | 2.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.5 |
| Tre Donaldson | 58% | 7.3<br><sub>-,-,-,-,1</sub> | 6.6<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 3.6 | 7.3 |

</details>

<details><summary>if Amen Thompson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 100% | 36.9<br><sub>39,35,29,41,29</sub> | 17.5<br><sub>17,8,19,12,26</sub> | 16.5 · – | 7.6<br><sub>7,9,7,10,7</sub> | 7.5 | 4.8<br><sub>0,3,4,3,7</sub> | 3.5 | 0.3<br><sub>0,0,0,0,3</sub> |  | 1.5 | 0.8 | 2.2 | 29.9 |
| Alperen Sengun (HOU) | 91% | 36.8<br><sub>32,35,37,37,28</sub> | 22.7<br><sub>15,20,19,43,19</sub> | 19.5 · –<br><sub>o 53% · u 47%</sub> | 10.4<br><sub>6,12,13,12,8</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>5,8,9,5,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.2 | 1.1 | 3.0 | 40.1 |
| Kevin Durant (HOU) | 98% | 36.5<br><sub>38,36,34,33,30</sub> | 24.2<br><sub>21,23,20,22,25</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>10,12,4,3,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>3,8,5,6,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.9 | 3.2 | 35.5 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>39,38,35,24,28</sub> | 16.1<br><sub>15,14,14,6,9</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>9,7,8,3,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>2,3,0,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.9 | 1.3 | 25.7 |
| Fred VanVleet (HOU) | 71% | 34.2<br><sub>31,30,30,34,-</sub> | 14.9<br><sub>16,12,18,17,-</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>3,1,2,2,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.3<br><sub>4,2,6,3,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>4,3,4,3,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.4 | 1.5 | 23.9 |
| Tari Eason (HOU) | 98% | 28.2<br><sub>23,19,22,33,30</sub> | 11.2<br><sub>2,12,6,14,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>7,5,3,11,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>2,2,0,2,1</sub> |  | 1.4<br><sub>0,2,0,2,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.7 | 1.2 | 19.6 |
| Reed Sheppard (HOU) | 91% | 24.5<br><sub>13,17,20,19,26</sub> | 11.5<br><sub>6,8,13,0,11</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>0,0,1,0,1</sub> |  | 3.3<br><sub>0,0,1,3,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.6 | 1.2 | 17.0 |
| Bogdan Bogdanovic (HOU) | 97% | 16.7<br><sub>2,12,10,12,22</sub> | 6.6<br><sub>0,8,0,11,12</sub> |  | 2.1<br><sub>1,3,0,1,3</sub> |  | 1.6<br><sub>0,1,0,3,4</sub> |  | 1.0<br><sub>0,2,0,3,2</sub> |  | 0.5 | 0.1 | 0.7 | 10.3 |
| Oscar Tshiebwe (HOU) | 93% | 11.5<br><sub>3,-,1,6,12</sub> | 4.0<br><sub>2,-,0,0,4</sub> |  | 5.1<br><sub>0,-,0,5,9</sub> |  | 0.7<br><sub>0,-,0,0,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 9.8 |
| Isaiah Crawford (HOU) | 63% | 7.6<br><sub>-,1,1,-,9</sub> | 2.2<br><sub>-,0,0,-,4</sub> |  | 1.2<br><sub>-,0,0,-,2</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.2 | 3.8 |
| Jae'Sean Tate (HOU) | 58% | 7.5<br><sub>-,-,1,-,8</sub> | 2.3<br><sub>-,-,0,-,4</sub> |  | 1.8<br><sub>-,-,0,-,2</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Bruce Thornton (HOU) | 63% | 7.0<br><sub>-,1,3,-,6</sub> | 2.2<br><sub>-,0,0,-,2</sub> |  | 1.1<br><sub>-,0,0,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |
| Davion Mitchell (MIA) | 98% | 37.7<br><sub>38,40,38,39,32</sub> | 15.1<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 8.9<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.3 | 2.3 | 27.1 |
| Bam Adebayo (MIA) | 98% | 37.1<br><sub>33,34,37,38,36</sub> | 20.4<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 9.9<br><sub>10,8,8,14,5</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,1,0,2,1</sub> |  | 1.7 | 0.8 | 1.7 | 34.1 |
| Giannis Antetokounmpo (MIA) | 98% | 35.3<br><sub>31,34,31,31,31</sub> | 29.3<br><sub>20,29,30,37,34</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 12.2<br><sub>14,14,11,9,14</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 6.1<br><sub>4,3,4,2,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 41% · u 59%</sub> | 1.1 | 1.0 | 3.5 | 47.6 |
| Andrew Wiggins (MIA) | 98% | 28.7<br><sub>21,32,19,32,23</sub> | 11.0<br><sub>2,6,13,8,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.8 | 1.1 | 16.5 |
| Klay Thompson (MIA) | 83% | 28.4<br><sub>23,32,30,-,20</sub> | 13.7<br><sub>11,23,11,-,26</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>0,2,1,-,1</sub> |  | 2.0<br><sub>3,4,2,-,4</sub> |  | 2.9<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.6 | 1.3 | 18.0 |
| Ryan Conwell (MIA) | 91% | 24.7<br><sub>30,19,21,33,26</sub> | 8.8<br><sub>13,6,5,20,9</sub> |  | 2.8<br><sub>1,2,4,5,4</sub> |  | 1.7<br><sub>2,2,2,2,1</sub> |  | 1.5<br><sub>3,2,1,4,2</sub> |  | 0.8 | 0.2 | 1.0 | 13.3 |
| Bobby Portis (MIA) | 98% | 20.4<br><sub>14,20,17,15,18</sub> | 8.2<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 5.2<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,1,1,2,2</sub> |  | 1.0<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 0.3 | 0.7 | 14.8 |
| Myron Gardner (MIA) | 67% | 16.8<br><sub>1,-,10,19,26</sub> | 4.7<br><sub>0,-,4,0,5</sub> |  | 4.4<br><sub>0,-,3,4,9</sub> |  | 1.5<br><sub>0,-,1,2,3</sub> |  | 0.5<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.5 | 0.6 | 10.6 |
| Tim Hardaway Jr. (MIA) | 64% | 16.6<br><sub>4,7,-,20,-</sub> | 6.3<br><sub>0,0,-,4,-</sub> |  | 1.7<br><sub>0,0,-,3,-</sub> |  | 0.8<br><sub>1,0,-,2,-</sub> |  | 0.9<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 8.9 |
| Simone Fontecchio (MIA) | 64% | 12.8<br><sub>-,-,7,7,14</sub> | 5.3<br><sub>-,-,3,0,7</sub> |  | 2.1<br><sub>-,-,0,0,5</sub> |  | 0.9<br><sub>-,-,0,2,0</sub> |  | 0.8<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.4 |
| Dru Smith (MIA) | 52% | 11.8<br><sub>1,-,-,6,-</sub> | 3.6<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,0,-</sub> |  | 1.7<br><sub>0,-,-,1,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.9 | 0.2 | 0.6 | 6.9 |
| Keshad Johnson (MIA) | 52% | 8.7<br><sub>-,-,-,-,1</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.7 |
| Nick Richards (MIA) | 38% | 7.6<br><sub>1,-,-,-,-</sub> | 2.6<br><sub>0,-,-,-,-</sub> |  | 2.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.4 |
| Tre Donaldson (MIA) | 58% | 7.3<br><sub>-,-,-,-,1</sub> | 6.5<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 3.6 | 7.3 |

</details>

<details><summary>if Pelle Larsson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alperen Sengun (HOU) | 91% | 37.2<br><sub>32,35,37,37,28</sub> | 24.4<br><sub>15,20,19,43,19</sub> | 19.5 · –<br><sub>o 53% · u 47%</sub> | 10.4<br><sub>6,12,13,12,8</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>5,8,9,5,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.2 | 1.2 | 3.2 | 42.0 |
| Kevin Durant (HOU) | 98% | 36.6<br><sub>38,36,34,33,30</sub> | 25.5<br><sub>21,23,20,22,25</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>10,12,4,3,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>3,8,5,6,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.9 | 3.4 | 37.3 |
| Jabari Smith Jr. (HOU) | 98% | 36.6<br><sub>39,38,35,24,28</sub> | 17.4<br><sub>15,14,14,6,9</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>9,7,8,3,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,3,0,0,5</sub> |  | 2.6<br><sub>1,2,2,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.9 | 1.5 | 27.4 |
| Fred VanVleet (HOU) | 71% | 35.5<br><sub>31,30,30,34,-</sub> | 17.0<br><sub>16,12,18,17,-</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,1,2,2,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.8<br><sub>4,2,6,3,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,3,4,3,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.5 | 1.6 | 26.8 |
| Tari Eason (HOU) | 98% | 31.4<br><sub>23,19,22,33,30</sub> | 13.3<br><sub>2,12,6,14,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>7,5,3,11,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,2,0,2,1</sub> |  | 1.6<br><sub>0,2,0,2,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.8 | 1.4 | 23.0 |
| Reed Sheppard (HOU) | 91% | 30.6<br><sub>13,17,20,19,26</sub> | 15.3<br><sub>6,8,13,0,11</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>0,0,1,0,1</sub> |  | 4.3<br><sub>0,0,1,3,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.7 | 1.5 | 22.5 |
| Bogdan Bogdanovic (HOU) | 97% | 23.4<br><sub>2,12,10,12,22</sub> | 9.3<br><sub>0,8,0,11,12</sub> |  | 3.0<br><sub>1,3,0,1,3</sub> |  | 2.4<br><sub>0,1,0,3,4</sub> |  | 1.5<br><sub>0,2,0,3,2</sub> |  | 0.7 | 0.2 | 0.9 | 14.7 |
| Oscar Tshiebwe (HOU) | 93% | 15.8<br><sub>3,-,1,6,12</sub> | 5.5<br><sub>2,-,0,0,4</sub> |  | 7.0<br><sub>0,-,0,5,9</sub> |  | 1.0<br><sub>0,-,0,0,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 13.6 |
| Bruce Thornton (HOU) | 63% | 12.8<br><sub>-,1,3,-,6</sub> | 3.6<br><sub>-,0,0,-,2</sub> |  | 2.1<br><sub>-,0,0,-,0</sub> |  | 0.8<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.6 | 0.1 | 0.6 | 6.5 |
| Isaiah Crawford (HOU) | 63% | 12.5<br><sub>-,1,1,-,9</sub> | 3.6<br><sub>-,0,0,-,4</sub> |  | 2.2<br><sub>-,0,0,-,2</sub> |  | 0.6<br><sub>-,0,0,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.4 |
| Jae'Sean Tate (HOU) | 58% | 12.3<br><sub>-,-,1,-,8</sub> | 3.6<br><sub>-,-,0,-,4</sub> |  | 3.0<br><sub>-,-,0,-,2</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.4 |
| Davion Mitchell (MIA) | 98% | 35.8<br><sub>38,40,38,39,32</sub> | 14.7<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 8.3<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.3 | 2.1 | 26.0 |
| Bam Adebayo (MIA) | 98% | 35.6<br><sub>33,34,37,38,36</sub> | 19.8<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>10,8,8,14,5</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,1,0,2,1</sub> |  | 1.6 | 0.7 | 1.6 | 33.0 |
| Giannis Antetokounmpo (MIA) | 98% | 34.1<br><sub>31,34,31,31,31</sub> | 28.6<br><sub>20,29,30,37,34</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 11.7<br><sub>14,14,11,9,14</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 5.5<br><sub>4,3,4,2,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 41% · u 59%</sub> | 1.1 | 1.1 | 3.5 | 45.8 |
| Pelle Larsson (MIA) | 100% | 28.5<br><sub>29,22,31,-,-</sub> | 11.5<br><sub>13,11,14,-,-</sub> |  | 3.4<br><sub>1,3,7,-,-</sub> |  | 3.1<br><sub>4,3,2,-,-</sub> |  | 1.0<br><sub>3,3,2,-,-</sub> |  | 0.9 | 0.2 | 1.7 | 18.0 |
| Andrew Wiggins (MIA) | 98% | 25.2<br><sub>21,32,19,32,23</sub> | 10.0<br><sub>2,6,13,8,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.7<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.8 | 1.0 | 14.9 |
| Klay Thompson (MIA) | 83% | 23.9<br><sub>23,32,30,-,20</sub> | 12.2<br><sub>11,23,11,-,26</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>0,2,1,-,1</sub> |  | 1.6<br><sub>3,4,2,-,4</sub> |  | 2.4<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.5 | 0.5 | 1.1 | 15.9 |
| Ryan Conwell (MIA) | 91% | 20.2<br><sub>30,19,21,33,26</sub> | 7.3<br><sub>13,6,5,20,9</sub> |  | 2.3<br><sub>1,2,4,5,4</sub> |  | 1.4<br><sub>2,2,2,2,1</sub> |  | 1.1<br><sub>3,2,1,4,2</sub> |  | 0.7 | 0.1 | 0.9 | 11.1 |
| Bobby Portis (MIA) | 98% | 17.7<br><sub>14,20,17,15,18</sub> | 7.3<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.6<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>0,1,1,2,2</sub> |  | 0.9<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.5 | 0.2 | 0.6 | 13.1 |
| Myron Gardner (MIA) | 67% | 12.8<br><sub>1,-,10,19,26</sub> | 3.8<br><sub>0,-,4,0,5</sub> |  | 3.4<br><sub>0,-,3,4,9</sub> |  | 1.2<br><sub>0,-,1,2,3</sub> |  | 0.4<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.3 | 0.5 | 8.4 |
| Tim Hardaway Jr. (MIA) | 64% | 11.4<br><sub>4,7,-,20,-</sub> | 4.5<br><sub>0,0,-,4,-</sub> |  | 1.3<br><sub>0,0,-,3,-</sub> |  | 0.6<br><sub>1,0,-,2,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.3 |
| Simone Fontecchio (MIA) | 64% | 10.2<br><sub>-,-,7,7,14</sub> | 4.6<br><sub>-,-,3,0,7</sub> |  | 1.7<br><sub>-,-,0,0,5</sub> |  | 0.7<br><sub>-,-,0,2,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 7.0 |
| Dru Smith (MIA) | 52% | 7.8<br><sub>1,-,-,6,-</sub> | 2.6<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,0,-</sub> |  | 1.1<br><sub>0,-,-,1,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.6 | 0.1 | 0.4 | 4.8 |
| Keshad Johnson (MIA) | 52% | 6.5<br><sub>-,-,-,-,1</sub> | 2.9<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.6 |
| Nick Richards (MIA) | 38% | 6.0<br><sub>1,-,-,-,-</sub> | 2.3<br><sub>0,-,-,-,-</sub> |  | 2.0<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.6 |
| Tre Donaldson (MIA) | 58% | 5.6<br><sub>-,-,-,-,1</sub> | 5.9<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 2.9 | 6.5 |

</details>


### POR @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.3<br><sub>39,24,34,35,35</sub> | 23.7<br><sub>22,15,24,28,34</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>9,4,6,3,6</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>11,1,8,6,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,2,2,4,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.6 | 3.6 | 36.4 |
| Toumani Camara | 98% | 32.2<br><sub>30,21,30,38,36</sub> | 11.9<br><sub>18,4,12,14,14</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,4,3,5,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,0,3,3,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>4,0,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.5 | 1.4 | 18.0 |
| Damian Lillard | 98% | 31.9<br><sub>37,20,24,32,33</sub> | 19.8<br><sub>22,12,25,18,29</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>0,0,3,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>4,7,3,3,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>4,2,4,2,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 2.6 | 28.5 |
| Jrue Holiday | 98% | 28.9<br><sub>31,20,25,30,27</sub> | 13.7<br><sub>12,11,11,19,6</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>1,0,1,3,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,0,2,5,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>3,1,2,5,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 2.5 | 22.3 |
| Donovan Clingan | 98% | 26.8<br><sub>28,22,26,30,27</sub> | 11.0<br><sub>17,6,7,5,13</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 10.4<br><sub>11,5,13,12,11</sub> | 11.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>1,0,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>3,0,1,1,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.6 | 2.0 | 1.3 | 23.2 |
| Sidy Cissoko | 98% | 25.2<br><sub>22,16,33,29,26</sub> | 7.1<br><sub>7,4,17,19,3</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,3,3,2,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>3,1,3,0,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.4 | 1.1 | 12.5 |
| Scoot Henderson | 98% | 25.0<br><sub>23,24,23,19,23</sub> | 11.2<br><sub>2,13,11,5,11</sub> |  | 2.5<br><sub>2,2,1,2,0</sub> |  | 2.5<br><sub>0,1,4,2,1</sub> |  | 1.3<br><sub>0,0,3,1,2</sub> |  | 0.8 | 0.2 | 2.2 | 16.2 |
| Robert Williams III | 98% | 17.0<br><sub>16,-,15,17,17</sub> | 6.2<br><sub>9,-,6,10,2</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>5,-,4,7,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.0<br><sub>2,-,0,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.3 | 0.8 | 13.8 |
| Jayson Kent | 63% | 12.2<br><sub>-,12,-,-,11</sub> | 4.3<br><sub>-,4,-,-,3</sub> |  | 1.6<br><sub>-,1,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,1</sub> |  | 0.5 | 0.2 | 0.7 | 6.4 |
| Branden Carlson | 76% | 9.4<br><sub>-,12,8,10,8</sub> | 2.7<br><sub>-,4,2,0,5</sub> |  | 2.4<br><sub>-,2,5,2,3</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.2<br><sub>-,0,0,0,1</sub> |  | 0.2 | 0.6 | 0.5 | 5.5 |
| Micah Potter | 52% | 8.4<br><sub>-,14,5,-,-</sub> | 3.5<br><sub>-,7,0,-,-</sub> |  | 2.2<br><sub>-,3,3,-,-</sub> |  | 0.5<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.2 |
| Yang Hansen | 52% | 8.1<br><sub>3,26,5,-,-</sub> | 3.1<br><sub>2,12,0,-,-</sub> |  | 2.1<br><sub>0,10,1,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.2 | 0.7 | 5.6 |
| John Tonje | 36% | 6.7<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 35.2<br><sub>37,40,33,25,37</sub> | 17.3<br><sub>14,23,16,16,18</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>8,6,6,9,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>4,5,3,3,6</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>0,2,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 1.1 | 2.1 | 26.2 |
| Ayo Dosunmu | 98% | 33.3<br><sub>34,39,30,27,33</sub> | 18.6<br><sub>21,26,26,18,24</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>1,2,4,2,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.7<br><sub>6,4,1,1,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>0,4,4,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.4 | 2.3 | 26.8 |
| Jonathan Kuminga | 98% | 31.6<br><sub>32,34,25,24,35</sub> | 14.1<br><sub>16,17,4,14,11</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>8,8,0,8,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>5,4,0,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>4,1,0,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.6 | 1.7 | 22.2 |
| LaMelo Ball | 98% | 30.4<br><sub>31,35,30,25,30</sub> | 21.0<br><sub>20,22,24,22,19</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>2,2,3,3,8</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.2<br><sub>6,8,5,9,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>4,3,4,6,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7 | 0.3 | 3.3 | 31.5 |
| Rudy Gobert | 98% | 30.0<br><sub>33,25,31,23,27</sub> | 9.6<br><sub>8,8,10,9,1</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 11.0<br><sub>11,11,15,6,10</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,0,2,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.4 | 1.3 | 22.2 |
| Terrence Shannon Jr. | 98% | 22.6<br><sub>-,-,18,21,22</sub> | 11.0<br><sub>-,-,5,6,14</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>-,-,3,2,6</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>-,-,3,4,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 1.2 | 15.7 |
| Trey Lyles | 98% | 19.4<br><sub>20,29,21,15,19</sub> | 5.9<br><sub>5,5,9,2,5</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>2,13,6,0,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>0,2,2,0,2</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.8 |
| Bones Hyland | 98% | 18.4<br><sub>16,10,13,23,21</sub> | 10.2<br><sub>19,4,14,24,12</sub> |  | 1.9<br><sub>2,1,2,3,1</sub> |  | 2.8<br><sub>4,0,2,8,2</sub> |  | 1.4<br><sub>4,1,1,5,3</sub> |  | 0.9 | 0.3 | 1.3 | 14.8 |
| Joan Beringer | 98% | 14.6<br><sub>13,7,16,22,13</sub> | 5.9<br><sub>4,2,4,13,2</sub> |  | 5.0<br><sub>7,3,3,9,5</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 11.4 |
| Zyon Pullin | 35% | 7.8<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Rocco Zikarsky | 38% | 7.5<br><sub>-,-,2,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.2<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.7 | 0.4 | 5.2 |
| Cody Williams | 52% | 6.1<br><sub>-,-,2,7,-</sub> | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.4 |
| Isaiah Evans | 52% | 5.8<br><sub>-,-,2,8,-</sub> | 6.0<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,0,1,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 7.4 |
| Johni Broome | 5% | 5.7 | 2.2 |  | 1.4 |  | 0.3 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.9 |

</details>


### GSW @ NOP
Out: Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.8–112.8 | GSW 69% | 1.45 / 3.23 | NOP +7.5 | 232.5 | NOP +3.5 covers 40%; o223.5 69% |
| Expected (weighted by chance each plays) | 120.1–112.9 | GSW 69% | 1.44 / 3.28 | NOP +7.5 | 233.5 | NOP +3.5 covers 39%; o223.5 70% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 19.2 | 8.5 | 3.9 | 2.1 | 0.7 | 0.8 | 0.4 | 1.3 | 14.4 | small |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 96% | 34.1<br><sub>32,39,26,37,22</sub> | 20.8<br><sub>9,15,25,22,8</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>6,7,2,6,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>3,1,4,4,0</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>2,4,5,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.3 | 1.9 | 31.2 |
| Yaxel Lendeborg | 98% | 33.8<br><sub>30,37,27,36,24</sub> | 23.1<br><sub>17,23,23,25,3</sub> | 24.5 · –<br><sub>o 46% · u 54%</sub> | 7.8<br><sub>8,8,7,10,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>6,3,4,0,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>1,2,4,2,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.8 | 3.5 | 35.1 |
| Draymond Green | 96% | 28.5<br><sub>27,34,21,27,16</sub> | 6.7<br><sub>2,2,2,7,4</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>5,6,3,5,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 7.1<br><sub>11,13,6,7,3</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.8 | 2.8 | 19.5 |
| De'Anthony Melton | 98% | 25.9<br><sub>17,17,26,25,18</sub> | 15.0<br><sub>5,4,16,11,8</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>6,1,4,4,4</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.3<br><sub>2,1,3,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.6 | 0.5 | 1.8 | 22.3 |
| Will Richard | 98% | 25.3<br><sub>16,12,-,19,30</sub> | 8.1<br><sub>10,4,-,9,7</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>0,2,-,4,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>2,1,-,0,1</sub> |  | 1.0<br><sub>2,0,-,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 1.0 | 12.8 |
| Georges Niang | 98% | 22.3<br><sub>22,25,19,19,15</sub> | 9.9<br><sub>13,11,9,5,5</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>4,2,2,5,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>3,1,2,0,2</sub> |  | 1.6<br><sub>2,3,1,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.2 | 1.1 | 15.0 |
| Al Horford | 98% | 19.3<br><sub>18,13,15,21,10</sub> | 7.1<br><sub>8,2,5,2,0</sub> |  | 4.3<br><sub>5,5,2,1,3</sub> |  | 2.4<br><sub>1,4,6,4,1</sub> |  | 1.0<br><sub>2,0,1,0,0</sub> |  | 0.5 | 0.9 | 0.7 | 13.8 |
| LJ Cryer | 76% | 18.6<br><sub>1,-,20,18,24</sub> | 9.7<br><sub>0,-,10,13,20</sub> |  | 1.4<br><sub>0,-,0,1,2</sub> |  | 1.9<br><sub>0,-,3,1,6</sub> |  | 1.7<br><sub>0,-,2,3,6</sub> |  | 0.4 | 0.1 | 1.0 | 13.1 |
| Gary Payton II | 83% | 17.3<br><sub>10,13,-,-,13</sub> | 8.6<br><sub>9,4,-,-,2</sub> |  | 3.1<br><sub>0,0,-,-,2</sub> |  | 1.4<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 1.0 | 0.3 | 0.9 | 13.1 |
| Charles Bassey | 98% | 17.1<br><sub>14,11,18,13,20</sub> | 9.1<br><sub>8,8,12,7,11</sub> |  | 7.5<br><sub>7,4,10,6,5</sub> |  | 1.0<br><sub>0,0,1,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.4 | 1.1 | 17.5 |
| Graham Ike | 91% | 13.3<br><sub>1,-,12,4,13</sub> | 5.8<br><sub>0,-,4,4,5</sub> |  | 3.2<br><sub>1,-,5,0,2</sub> |  | 1.4<br><sub>0,-,2,1,3</sub> |  | 0.4<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.5 | 0.7 | 10.5 |
| Malevy Leons | 64% | 12.4<br><sub>1,-,12,4,14</sub> | 3.7<br><sub>0,-,0,0,5</sub> |  | 2.4<br><sub>0,-,3,3,1</sub> |  | 0.8<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.5 | 0.6 | 6.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 34.3<br><sub>26,24,29,35,41</sub> | 18.9<br><sub>13,9,15,30,16</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>4,0,1,10,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>3,4,2,0,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>1,1,3,6,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 1.5 | 27.4 |
| Zion Williamson | 98% | 34.2<br><sub>31,-,30,33,31</sub> | 22.5<br><sub>25,-,29,22,24</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>2,-,2,4,2</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 0.4<br><sub>0,-,1,0,2</sub> |  | 1.4 | 0.7 | 2.5 | 32.6 |
| Jeremiah Fears | 98% | 32.6<br><sub>29,29,28,34,33</sub> | 18.6<br><sub>25,11,14,18,13</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>6,3,4,5,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>5,8,5,7,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,1,2,0,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.6 | 3.1 | 29.5 |
| Herbert Jones | 98% | 27.3<br><sub>20,24,25,32,27</sub> | 8.7<br><sub>4,10,2,8,10</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>0,6,2,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>1,1,3,3,1</sub> |  | 1.1<br><sub>0,2,0,0,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.5 | 1.4 | 14.2 |
| Derik Queen | 98% | 25.9<br><sub>21,21,14,23,25</sub> | 13.1<br><sub>8,16,9,10,10</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>5,4,0,6,5</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>3,0,0,2,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.5<br><sub>0,0,1,0,2</sub> |  | 1.1 | 1.0 | 2.6 | 23.8 |
| Jordan Poole | 72% | 23.2<br><sub>-,34,21,21,24</sub> | 11.9<br><sub>-,7,14,13,14</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>-,3,0,2,2</sub> |  | 3.3<br><sub>-,2,1,5,5</sub> |  | 1.8<br><sub>-,1,2,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.4 | 1.8 | 17.4 |
| Yves Missi | 98% | 22.4<br><sub>-,-,-,-,22</sub> | 7.0<br><sub>-,-,-,-,3</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>-,-,-,-,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 1.8 | 1.0 | 15.8 |
| Karlo Matkovic | 97% | 21.9<br><sub>19,17,22,19,14</sub> | 8.2<br><sub>3,4,4,1,5</sub> |  | 4.9<br><sub>3,6,4,3,3</sub> |  | 1.3<br><sub>2,2,1,0,1</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.9 | 1.0 | 14.5 |
| Jaron Pierre Jr. | 84% | 17.1<br><sub>-,-,7,4,23</sub> | 7.4<br><sub>-,-,4,0,13</sub> |  | 2.5<br><sub>-,-,4,0,2</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,1,0,2</sub> |  | 0.7 | 0.3 | 1.2 | 10.9 |
| DeAndre Jordan | 48% | 14.5<br><sub>-,-,11,17,-</sub> | 3.9<br><sub>-,-,0,6,-</sub> |  | 5.8<br><sub>-,-,3,8,-</sub> |  | 0.8<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.7 | 0.7 | 10.5 |
| AJ Johnson | 52% | 8.5<br><sub>3,12,7,4,-</sub> | 2.4<br><sub>2,2,2,1,-</sub> |  | 1.2<br><sub>0,2,1,0,-</sub> |  | 0.8<br><sub>0,3,0,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 4.5 |
| Julian Reese | 54% | 8.4<br><sub>3,9,7,4,-</sub> | 2.5<br><sub>0,2,2,0,-</sub> |  | 1.6<br><sub>0,0,2,2,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.6 | 4.6 |
| Malik Dia | 48% | 7.0<br><sub>-,-,-,4,-</sub> | 2.5<br><sub>-,-,-,2,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 1.0<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.7 |

</details>


### PHX @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN), Mark Williams (PHX)

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 33.7<br><sub>39,29,29,35,28</sub> | 22.3<br><sub>24,32,17,30,17</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,3,1,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 6.0<br><sub>3,4,5,7,7</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>2,3,2,4,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 2.5 | 31.6 |
| Dillon Brooks | 98% | 28.5<br><sub>37,26,22,30,22</sub> | 15.3<br><sub>11,7,8,15,1</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>4,4,4,3,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,0,2,1,0</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.9<br><sub>3,1,0,3,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.2 | 20.6 |
| Miles Bridges | 98% | 27.2<br><sub>31,26,18,25,24</sub> | 13.6<br><sub>13,7,8,11,14</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>10,5,4,6,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>7,0,2,3,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.4 | 0.9 | 22.0 |
| Jalen Green | 98% | 25.4<br><sub>34,24,21,21,21</sub> | 12.7<br><sub>16,6,13,12,9</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>3,5,5,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.6<br><sub>6,4,1,0,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,0,3,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.3 | 1.8 | 18.7 |
| Collin Gillespie | 98% | 24.6<br><sub>20,24,22,27,28</sub> | 9.6<br><sub>7,6,12,13,26</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>3,2,2,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.8<br><sub>4,3,8,1,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>1,2,4,3,5</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 1.0 | 16.4 |
| Oso Ighodaro | 98% | 21.2<br><sub>23,18,20,32,17</sub> | 6.0<br><sub>4,7,6,2,4</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,4,8,3,2</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>3,2,2,7,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.6 | 1.1 | 13.7 |
| Jordan Goodwin | 98% | 20.8<br><sub>-,-,14,24,31</sub> | 8.2<br><sub>-,-,18,6,14</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>-,-,3,5,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>-,-,1,2,6</sub> |  | 1.3<br><sub>-,-,6,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.2 | 0.7 | 14.5 |
| Luke Kennard | 98% | 19.1<br><sub>14,14,22,21,23</sub> | 7.7<br><sub>11,3,14,8,18</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,1,1,1,6</sub> |  | 1.9<br><sub>2,0,3,1,4</sub> |  | 1.0<br><sub>3,1,3,0,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.5 | 0.1 | 0.7 | 11.6 |
| Ryan Dunn | 98% | 17.5<br><sub>23,23,25,10,24</sub> | 5.2<br><sub>8,3,10,0,3</sub> |  | 3.7<br><sub>5,2,8,4,6</sub> |  | 1.2<br><sub>3,0,2,0,1</sub> |  | 0.6<br><sub>2,1,1,0,1</sub> |  | 0.6 | 0.4 | 0.5 | 10.1 |
| Khaman Maluach | 98% | 15.6<br><sub>18,20,22,16,13</sub> | 5.4<br><sub>8,11,11,4,7</sub> |  | 4.6<br><sub>10,5,7,2,4</sub> |  | 0.8<br><sub>0,2,3,1,0</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 10.8 |
| Rasheer Fleming | 48% | 8.6<br><sub>-,9,12,-,-</sub> | 3.3<br><sub>-,2,4,-,-</sub> |  | 1.5<br><sub>-,1,2,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,1,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.0 |
| Koa Peat | 63% | 8.1<br><sub>-,6,6,-,8</sub> | 4.1<br><sub>-,4,5,-,10</sub> |  | 1.8<br><sub>-,0,1,-,2</sub> |  | 0.4<br><sub>-,1,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Pat Spencer | 58% | 7.3<br><sub>-,6,-,-,-</sub> | 2.7<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,2,-,-,-</sub> |  | 1.4<br><sub>-,2,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.0 |
| Jamaree Bouyea | 52% | 7.2<br><sub>-,9,8,-,-</sub> | 3.0<br><sub>-,4,7,-,-</sub> |  | 1.0<br><sub>-,0,1,-,-</sub> |  | 1.2<br><sub>-,3,3,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.2 |
| Drew Timme | 8% | 6.9 | 2.7 |  | 1.1 |  | 0.7 |  | 0.2 |  | 0.2 | 0.0 | 0.4 | 4.6 |
| Duop Reath | 52% | 6.7<br><sub>-,6,-,-,-</sub> | 2.8<br><sub>-,2,-,-,-</sub> |  | 1.4<br><sub>-,2,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.5 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 36.5<br><sub>30,36,39,37,37</sub> | 26.5<br><sub>32,19,25,27,26</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 12.8<br><sub>10,13,16,11,8</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 10.6<br><sub>11,8,9,8,10</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.8 | 3.7 | 49.9 |
| Jamal Murray | 98% | 36.4<br><sub>28,34,39,32,38</sub> | 25.1<br><sub>14,16,38,30,23</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>5,6,2,4,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 6.6<br><sub>7,8,2,8,9</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>2,2,5,4,0</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.6 | 2.6 | 36.6 |
| Christian Braun | 98% | 32.6<br><sub>28,29,32,37,28</sub> | 12.7<br><sub>11,6,4,12,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>3,4,5,5,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 1.1 | 19.8 |
| Cameron Johnson | 98% | 30.2<br><sub>30,29,31,30,31</sub> | 12.9<br><sub>12,18,8,23,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>2,4,2,4,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>2,1,1,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.8<br><sub>4,2,2,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.4 | 1.1 | 19.5 |
| Aaron Gordon | 98% | 29.9<br><sub>25,27,30,27,33</sub> | 13.3<br><sub>17,12,3,9,11</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>1,5,5,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>0,0,2,2,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.4 | 1.3 | 21.4 |
| DeMar DeRozan | 88% | 22.7<br><sub>-,22,19,20,24</sub> | 11.3<br><sub>-,11,7,8,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>-,1,4,1,3</sub> |  | 3.1<br><sub>-,5,2,4,2</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.3 | 1.2 | 16.7 |
| Trevon Brazile | 98% | 16.0<br><sub>23,14,14,13,16</sub> | 5.2<br><sub>6,3,5,7,5</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>7,4,2,5,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 0.7<br><sub>1,2,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 9.8 |
| Spencer Jones | 80% | 13.7<br><sub>-,21,14,22,12</sub> | 3.9<br><sub>-,13,0,3,4</sub> |  | 2.0<br><sub>-,6,0,1,2</sub> |  | 0.7<br><sub>-,0,1,0,1</sub> |  | 0.4<br><sub>-,3,0,1,0</sub> |  | 0.4 | 0.3 | 0.5 | 6.6 |
| Marvin Bagley III | 98% | 13.3<br><sub>14,12,12,12,13</sub> | 6.6<br><sub>10,10,6,4,7</sub> |  | 4.1<br><sub>2,3,3,2,7</sub> |  | 0.8<br><sub>2,0,0,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 11.4 |
| Tyus Jones | 97% | 9.9<br><sub>18,13,6,11,10</sub> | 2.6<br><sub>6,3,2,0,2</sub> |  | 1.0<br><sub>1,4,0,1,0</sub> |  | 1.8<br><sub>8,4,0,4,3</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.3 |
| Bryce Hopkins | 52% | 8.2<br><sub>28,3,3,-,-</sub> | 2.8<br><sub>18,3,2,-,-</sub> |  | 1.3<br><sub>4,1,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.1<br><sub>1,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Zeke Nnaji | 30% | 6.8<br><sub>4,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.1 |
| Alpha Diallo | 52% | 6.3<br><sub>4,-,1,-,-</sub> | 2.6<br><sub>0,-,0,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-16/`._
