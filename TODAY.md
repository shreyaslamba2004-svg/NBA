# NBA model · Mon 16 Nov 2026 (US date)

Updated **Tue 17 Nov, 02:48 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-16/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PR over 29.5 (30+) | GSW @ NOP | draftkings | 16.20 | 13.91 | 6.68 | 15.0% | 5.8% | 7.2% | +16.4% | +142.5% | 0.3% |
| Derik Queen PTS over 19.5 (20+) | GSW @ NOP | draftkings | 12.80 | 11.24 | 5.66 | 17.6% | 7.3% | 8.9% | +13.9% | +126.0% | 0.3% |
| Saddiq Bey AST over 5.5 (6+) | GSW @ NOP | draftkings | 16.40 | 14.73 | 7.84 | 12.8% | 5.7% | 6.8% | +11.3% | +109.3% | 0.2% |
| Derik Queen REB over 11.5 (12+) | GSW @ NOP | draftkings | 15.80 | 14.51 | 8.17 | 12.2% | 5.9% | 6.9% | +8.9% | +93.5% | 0.1% |
| Donovan Mitchell PA over 49.5 (50+) | CHI @ CLE | draftkings | 20.40 | 18.87 | 10.78 | 9.3% | 4.6% | 5.3% | +8.2% | +89.2% | 0.1% |
| Zion Williamson AST over 7.5 (8+) | GSW @ NOP | draftkings | 24.00 | 22.22 | 12.74 | 7.8% | 3.9% | 4.5% | +8.1% | +88.4% | 0.1% |
| Donovan Mitchell PTS over 44.5 (45+) | CHI @ CLE | draftkings | 24.00 | 22.42 | 13.25 | 7.5% | 3.9% | 4.5% | +7.0% | +81.1% | 0.1% |
| Zion Williamson AST over 5.5 (6+) | GSW @ NOP | draftkings | 7.20 | 6.75 | 4.02 | 24.9% | 13.0% | 14.8% | +6.6% | +79.0% | 0.3% |
| Derik Queen REB over 9.5 (10+) | GSW @ NOP | draftkings | 6.95 | 6.52 | 3.90 | 25.7% | 13.5% | 15.3% | +6.5% | +78.4% | 0.3% |
| Donovan Mitchell PR over 49.5 (50+) | CHI @ CLE | draftkings | 20.20 | 19.16 | 11.80 | 8.5% | 4.6% | 5.2% | +5.4% | +71.2% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey REB over 9.5 (10+) | MEM @ WAS | draftkings | 3.77 | Zach Edey | void | 51.3% | +6.8% |
| Derik Queen AST over 3.5 (4+) | GSW @ NOP | draftkings | 3.58 | Jaron Pierre Jr. | 53.8% | 47.9% | +6.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ORL @ BOS | Tue 17 Nov 11:00 | 106.3–115.1 | ORL 27% | 3.73 / 1.37 | BOS -8.5 | 221.5 | BOS -8.5 covers 51%; o212.5 68% |
| CHI @ CLE | Tue 17 Nov 11:00 | 114.2–122.0 | CHI 29% | 3.46 / 1.41 | CLE -7.5 | 236.5 | CLE -8.5 covers 48%; o241.5 38% |
| MEM @ WAS | Tue 17 Nov 11:00 | 124.4–118.9 | MEM 65% | 1.53 / 2.89 | WAS +5.5 | 243.5 | WAS +3.5 covers 43%; o232.5 72% |
| PHI @ BKN | Tue 17 Nov 11:30 | 115.1–111.9 | PHI 60% | 1.68 / 2.47 | BKN +3.5 | 226.5 | BKN +5.5 covers 56%; o226.5 51% |
| HOU @ MIA | Tue 17 Nov 11:30 | 118.2–117.6 | HOU 52% | 1.94 / 2.07 | MIA +1.5 | 235.5 | MIA +2.5 covers 54%; o231.5 59% |
| POR @ MIN | Tue 17 Nov 12:00 | 111.2–115.6 | POR 38% | 2.65 / 1.61 | MIN -4.5 | 226.5 | MIN -2.5 covers 56%; o227.5 48% |
| GSW @ NOP | Tue 17 Nov 12:00 | 119.8–112.5 | GSW 70% | 1.44 / 3.30 | NOP +7.5 | 232.5 | NOP +3.5 covers 39%; o223.5 68% |
| PHX @ DEN | Tue 17 Nov 13:00 | 110.6–119.7 | PHX 26% | 3.87 / 1.35 | DEN -9.5 | 230.5 | DEN -9.5 covers 49%; o228.5 54% |

### ORL @ BOS
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL)

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 32.8<br><sub>38,40,38,39,36</sub> | 20.8<br><sub>15,30,33,38,35</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>8,6,7,8,9</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 5.8<br><sub>15,11,7,1,12</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>0,3,1,3,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 2.7 | 32.1 |
| Desmond Bane | 98% | 31.5<br><sub>32,-,36,34,35</sub> | 16.3<br><sub>15,-,15,25,21</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>6,-,6,3,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>0,-,4,2,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.5<br><sub>3,-,4,7,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.3 | 1.9 | 22.8 |
| Anthony Black | 98% | 30.2<br><sub>31,38,33,39,37</sub> | 13.7<br><sub>10,18,26,22,5</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>7,8,7,7,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,6,5,8,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>1,2,2,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3 | 0.6 | 2.1 | 21.6 |
| Wendell Carter Jr. | 98% | 28.7<br><sub>34,40,33,28,30</sub> | 10.5<br><sub>27,19,8,9,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>13,11,11,7,8</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>2,0,1,3,0</sub> |  | 0.8<br><sub>2,3,0,0,1</sub> |  | 0.6 | 0.7 | 1.4 | 19.0 |
| Jalen Suggs | 98% | 27.1<br><sub>-,-,-,-,21</sub> | 10.3<br><sub>-,-,-,-,3</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 4.0<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.5 | 2.1 | 17.6 |
| Tristan da Silva | 83% | 26.1<br><sub>30,39,-,-,31</sub> | 10.8<br><sub>18,19,-,-,12</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>2,7,-,-,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,2,-,-,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>4,5,-,-,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.2 | 1.0 | 15.8 |
| Jevon Carter | 86% | 14.0<br><sub>3,15,4,28,17</sub> | 5.1<br><sub>0,9,0,11,5</sub> |  | 1.2<br><sub>0,1,0,3,2</sub> |  | 1.4<br><sub>0,0,0,4,2</sub> |  | 0.7<br><sub>0,3,0,3,1</sub> |  | 0.6 | 0.1 | 0.4 | 7.7 |
| Goga Bitadze | 88% | 13.2<br><sub>8,7,15,20,18</sub> | 4.6<br><sub>4,4,2,4,12</sub> |  | 3.9<br><sub>5,5,2,7,4</sub> |  | 0.9<br><sub>0,2,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.6 | 9.4 |
| Jamal Cain | 83% | 12.9<br><sub>25,36,20,-,4</sub> | 5.1<br><sub>5,18,5,-,0</sub> |  | 2.2<br><sub>5,12,3,-,4</sub> |  | 0.6<br><sub>0,1,1,-,1</sub> |  | 0.5<br><sub>1,2,1,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 7.9 |
| Jase Richardson | 72% | 12.9<br><sub>26,30,15,20,-</sub> | 4.8<br><sub>10,2,6,6,-</sub> |  | 1.3<br><sub>2,4,1,1,-</sub> |  | 1.3<br><sub>3,4,1,2,-</sub> |  | 0.4<br><sub>2,0,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.4 |
| Nikola Vucevic | 98% | 11.8<br><sub>4,6,18,14,11</sub> | 4.6<br><sub>0,0,5,3,2</sub> |  | 3.1<br><sub>0,1,4,5,3</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 9.0 |
| Alex Morales | 66% | 8.0<br><sub>6,15,29,18,-</sub> | 1.9<br><sub>0,0,7,5,-</sub> |  | 1.3<br><sub>0,2,7,4,-</sub> |  | 0.6<br><sub>0,1,0,3,-</sub> |  | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.2 | 0.0 | 0.4 | 3.8 |
| Colin Castleton | 48% | 5.9<br><sub>2,-,-,1,-</sub> | 2.1<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 32.3<br><sub>29,29,32,38,30</sub> | 25.7<br><sub>34,21,21,24,32</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>8,4,6,7,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>9,6,4,8,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>5,5,3,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.6 | 2.7 | 39.7 |
| Paul George | 98% | 29.5<br><sub>22,28,30,-,25</sub> | 17.6<br><sub>8,27,36,-,7</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>5,3,5,-,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,1,1,-,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,5,6,-,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.6 | 0.5 | 2.1 | 25.6 |
| Derrick White | 98% | 29.3<br><sub>25,27,22,38,23</sub> | 12.8<br><sub>18,9,5,19,16</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>4,3,1,1,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.2<br><sub>5,7,3,7,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>4,1,1,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 1.1 | 1.5 | 20.4 |
| Payton Pritchard | 98% | 25.7<br><sub>23,29,30,31,19</sub> | 12.9<br><sub>12,12,18,14,10</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>6,5,6,1,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.6<br><sub>5,4,5,1,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>4,4,4,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.1 | 1.2 | 19.6 |
| Neemias Queta | 98% | 20.6<br><sub>15,22,22,31,15</sub> | 8.2<br><sub>4,13,4,11,8</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>3,9,6,13,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>1,4,3,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.1<br><sub>0,0,0,1,1</sub> |  | 0.6 | 1.1 | 1.1 | 16.8 |
| Baylor Scheierman | 98% | 19.4<br><sub>15,19,18,29,18</sub> | 6.1<br><sub>5,7,5,9,12</sub> |  | 3.8<br><sub>4,1,3,7,5</sub> |  | 1.5<br><sub>2,0,2,3,3</sub> |  | 0.9<br><sub>1,1,1,3,2</sub> |  | 0.7 | 0.1 | 0.7 | 11.3 |
| Sam Hauser | 98% | 18.0<br><sub>17,23,18,24,11</sub> | 6.7<br><sub>9,7,12,8,8</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,3,5,9,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>3,1,2,0,0</sub> |  | 1.2<br><sub>3,1,4,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.3 | 0.2 | 0.3 | 10.5 |
| Mitchell Robinson | 98% | 15.0<br><sub>15,18,17,11,15</sub> | 4.2<br><sub>6,12,2,2,0</sub> |  | 5.7<br><sub>7,7,6,2,7</sub> |  | 0.6<br><sub>0,2,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.7 | 10.6 |
| Jordan Walsh | 98% | 14.6<br><sub>22,11,19,18,21</sub> | 4.4<br><sub>6,0,8,6,11</sub> |  | 2.9<br><sub>3,3,2,3,1</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,0,1,0,2</sub> |  | 0.5 | 0.3 | 0.5 | 8.1 |
| Devin Carter | 91% | 13.4<br><sub>-,-,-,-,12</sub> | 5.5<br><sub>-,-,-,-,0</sub> |  | 2.5<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.2 | 1.1 | 9.6 |
| Luka Garza | 98% | 12.8<br><sub>19,9,9,11,14</sub> | 6.2<br><sub>6,4,2,5,2</sub> |  | 3.1<br><sub>7,5,0,1,3</sub> |  | 1.3<br><sub>4,0,2,0,5</sub> |  | 0.7<br><sub>2,0,0,1,0</sub> |  | 0.3 | 0.4 | 0.6 | 10.6 |
| Hugo Gonzalez | 98% | 12.6<br><sub>15,10,19,8,18</sub> | 4.1<br><sub>8,0,10,0,9</sub> |  | 2.6<br><sub>1,2,2,1,5</sub> |  | 0.6<br><sub>0,1,2,0,2</sub> |  | 0.4<br><sub>1,0,2,0,2</sub> |  | 0.5 | 0.2 | 0.6 | 7.3 |
| Ron Harper Jr. | 64% | 7.3<br><sub>10,4,4,-,12</sub> | 3.3<br><sub>3,2,0,-,10</sub> |  | 1.0<br><sub>0,0,1,-,1</sub> |  | 0.5<br><sub>2,0,0,-,0</sub> |  | 0.4<br><sub>1,0,0,-,2</sub> |  | 0.3 | 0.1 | 0.3 | 4.8 |
| Mike Conley | 43% | 7.3<br><sub>11,10,-,-,-</sub> | 2.0<br><sub>0,3,-,-,-</sub> |  | 0.8<br><sub>0,3,-,-,-</sub> |  | 1.1<br><sub>1,1,-,-,-</sub> |  | 0.2<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |
| Dillon Mitchell | 38% | 6.4<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 0.9 |
| Chris Cenac Jr. | 52% | 6.1<br><sub>-,-,-,-,7</sub> | 3.0<br><sub>-,-,-,-,6</sub> |  | 1.6<br><sub>-,-,-,-,3</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 5.0 |
| Amari Williams | 30% | 5.1<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.4 |

</details>


### CHI @ CLE
Out: Sam Merrill (CLE), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE), Tobe Awaka (CHI), Orlando Robinson (CHI), Caleb Wilson (CHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.2–122.0 | CHI 29% | 3.46 / 1.41 | CLE -7.5 | 236.5 | CLE -8.5 covers 48%; o241.5 38% |
| Expected (weighted by chance each plays) | 114.0–122.5 | CHI 27% | 3.73 / 1.37 | CLE -8.5 | 236.5 | CLE -8.5 covers 51%; o241.5 39% |
| if Peyton Watson plays | 113.6–123.7 | CHI 23% | 4.31 / 1.30 | CLE -10.5 | 237.5 | CLE -8.5 covers 55%; o241.5 40% |
| if Jaylon Tyson plays | 114.4–122.9 | CHI 27% | 3.68 / 1.37 | CLE -8.5 | 237.5 | CLE -8.5 covers 50%; o241.5 40% |
| if Jalen Smith plays | 114.4–121.0 | CHI 32% | 3.14 / 1.47 | CLE -6.5 | 235.5 | CLE -8.5 covers 45%; o241.5 37% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Peyton Watson (CLE) | Questionable | 55% | 29.4 | 13.3 | 5.0 | 2.7 | 1.4 | 1.0 | 1.5 | 1.6 | 21.0 | full tables below |
| Jaylon Tyson (CLE) | Questionable | 55% | 28.8 | 12.7 | 5.0 | 2.9 | 1.9 | 0.9 | 0.4 | 1.4 | 20.6 | full tables below |
| Jalen Smith (CHI) | Questionable | 55% | 26.5 | 12.9 | 8.1 | 1.7 | 1.6 | 0.6 | 0.8 | 1.1 | 22.6 | full tables below |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 31.1<br><sub>27,34,25,39,26</sub> | 14.8<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 8.5<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 2.8 | 30.2 |
| Norman Powell | 98% | 30.9<br><sub>22,-,-,31,30</sub> | 21.3<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 26.9 |
| Matas Buzelis | 98% | 30.3<br><sub>26,31,31,29,30</sub> | 17.0<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.1<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.0 | 2.3 | 24.7 |
| Isaac Okoro | 98% | 29.1<br><sub>15,25,23,41,31</sub> | 9.5<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.4 | 0.9 | 14.3 |
| Patrick Williams | 76% | 25.9<br><sub>20,25,28,24,26</sub> | 9.2<br><sub>4,7,9,13,14</sub> |  | 3.7<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.7 |
| Tre Jones | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.3<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.3 | 18.9 |
| Nic Claxton | 98% | 20.2<br><sub>-,18,16,22,-</sub> | 7.8<br><sub>-,4,17,2,-</sub> |  | 5.8<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.9 | 15.7 |
| Zach Collins | 71% | 18.4<br><sub>14,-,3,-,28</sub> | 7.2<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.4 |
| Leonard Miller | 67% | 17.5<br><sub>19,-,2,-,17</sub> | 7.9<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.0<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.1 |
| Buddy Hield | 71% | 17.4<br><sub>8,-,-,25,20</sub> | 8.3<br><sub>7,-,-,12,16</sub> |  | 2.4<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.3<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 1.0 | 12.3 |
| Noa Essengue | 96% | 13.8<br><sub>14,15,11,8,7</sub> | 5.6<br><sub>6,10,8,5,0</sub> |  | 3.1<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 9.4 |
| Jordan Hawkins | 58% | 12.7<br><sub>7,17,24,-,-</sub> | 5.3<br><sub>2,9,7,-,-</sub> |  | 1.7<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.7 |
| Dailyn Swain | 52% | 8.4<br><sub>7,-,-,-,-</sub> | 2.7<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 5.1 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.2<br><sub>34,25,33,35,-</sub> | 21.8<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.6 | 3.4 | 33.9 |
| Donovan Mitchell | 98% | 35.2<br><sub>37,23,36,33,-</sub> | 29.6<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 2.9 | 40.9 |
| Meleek Thomas | 93% | 31.4<br><sub>24,27,22,18,34</sub> | 17.4<br><sub>9,18,14,12,20</sub> |  | 3.9<br><sub>4,3,4,0,4</sub> |  | 2.3<br><sub>0,3,1,3,2</sub> |  | 2.9<br><sub>3,4,2,2,3</sub> |  | 1.4 | 0.5 | 1.5 | 23.7 |
| Tyrese Proctor | 96% | 31.2<br><sub>23,23,23,27,34</sub> | 15.6<br><sub>7,6,15,22,24</sub> |  | 5.3<br><sub>3,1,3,4,11</sub> |  | 5.0<br><sub>3,4,1,3,10</sub> |  | 2.5<br><sub>2,0,3,5,4</sub> |  | 1.4 | 0.1 | 1.5 | 25.9 |
| Jarrett Allen | 76% | 29.6<br><sub>-,19,32,32,-</sub> | 15.3<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 10.1<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.1 | 1.5 | 1.4 | 27.1 |
| Mario Hezonja | 98% | 25.1<br><sub>19,17,7,9,34</sub> | 11.1<br><sub>0,10,0,4,22</sub> |  | 6.5<br><sub>5,3,0,4,7</sub> |  | 2.0<br><sub>1,0,0,0,4</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 0.9 | 0.4 | 1.1 | 19.6 |
| Thomas Bryant | 72% | 23.6<br><sub>15,15,-,16,27</sub> | 12.6<br><sub>5,11,-,9,19</sub> |  | 6.2<br><sub>3,2,-,1,11</sub> |  | 1.1<br><sub>1,0,-,1,3</sub> |  | 1.5<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.8 | 1.1 | 20.0 |
| Craig Porter Jr. | 80% | 23.5<br><sub>15,17,-,9,28</sub> | 5.5<br><sub>0,9,-,0,9</sub> |  | 4.7<br><sub>1,2,-,2,9</sub> |  | 4.1<br><sub>1,4,-,2,6</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.7 | 1.1 | 14.4 |
| Norchad Omier | 52% | 23.3<br><sub>-,12,-,-,27</sub> | 7.0<br><sub>-,0,-,-,13</sub> |  | 5.7<br><sub>-,3,-,-,8</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.9 | 0.2 | 0.7 | 15.1 |
| Riley Minix | 52% | 17.9<br><sub>10,17,-,-,22</sub> | 6.1<br><sub>8,2,-,-,2</sub> |  | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.0<br><sub>0,0,-,-,0</sub> |  | 0.8<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 9.7 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell (CHI) | 98% | 29.4<br><sub>22,-,-,31,30</sub> | 19.6<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 24.9 |
| Josh Giddey (CHI) | 98% | 28.9<br><sub>27,34,25,39,26</sub> | 12.8<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 7.9<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.6 | 27.2 |
| Matas Buzelis (CHI) | 98% | 27.8<br><sub>26,31,31,29,30</sub> | 15.3<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.9<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.9 | 2.0 | 22.4 |
| Jalen Smith (CHI) | 100% | 26.5<br><sub>7,30,30,32,-</sub> | 12.9<br><sub>3,17,23,15,-</sub> | 13.5 · – | 8.1<br><sub>2,8,4,12,-</sub> | 8.5 | 1.7<br><sub>0,2,3,3,-</sub> | 1.5 | 1.6<br><sub>1,2,5,1,-</sub> | 1.5 | 0.6 | 0.8 | 1.1 | 22.6 |
| Isaac Okoro (CHI) | 98% | 25.3<br><sub>15,25,23,41,31</sub> | 8.3<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.7 | 0.3 | 0.8 | 12.4 |
| Patrick Williams (CHI) | 76% | 23.4<br><sub>20,25,28,24,26</sub> | 8.2<br><sub>4,7,9,13,14</sub> |  | 3.3<br><sub>0,3,7,4,5</sub> |  | 1.7<br><sub>2,3,4,2,1</sub> |  | 1.1<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.4 | 1.0 | 13.2 |
| Tre Jones (CHI) | 98% | 20.6<br><sub>18,14,28,15,24</sub> | 11.4<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.2 | 17.5 |
| Nic Claxton (CHI) | 98% | 18.1<br><sub>-,18,16,22,-</sub> | 7.0<br><sub>-,4,17,2,-</sub> |  | 5.1<br><sub>-,4,6,6,-</sub> |  | 1.9<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.7 | 0.8 | 14.0 |
| Buddy Hield (CHI) | 71% | 15.6<br><sub>8,-,-,25,20</sub> | 7.4<br><sub>7,-,-,12,16</sub> |  | 2.2<br><sub>1,-,-,3,4</sub> |  | 1.4<br><sub>1,-,-,3,2</sub> |  | 1.1<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 0.9 | 11.0 |
| Zach Collins (CHI) | 71% | 15.2<br><sub>14,-,3,-,28</sub> | 6.2<br><sub>3,-,2,-,8</sub> |  | 4.4<br><sub>1,-,2,-,5</sub> |  | 1.6<br><sub>3,-,1,-,4</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.8 | 12.1 |
| Leonard Miller (CHI) | 67% | 14.8<br><sub>19,-,2,-,17</sub> | 6.8<br><sub>4,-,0,-,4</sub> |  | 3.6<br><sub>6,-,0,-,3</sub> |  | 0.9<br><sub>3,-,0,-,4</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.7 | 11.2 |
| Noa Essengue (CHI) | 96% | 10.3<br><sub>14,15,11,8,7</sub> | 4.2<br><sub>6,10,8,5,0</sub> |  | 2.3<br><sub>3,7,4,1,1</sub> |  | 0.5<br><sub>0,1,3,1,0</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Jordan Hawkins (CHI) | 58% | 8.7<br><sub>7,17,24,-,-</sub> | 3.7<br><sub>2,9,7,-,-</sub> |  | 1.1<br><sub>1,0,4,-,-</sub> |  | 0.5<br><sub>0,1,2,-,-</sub> |  | 0.3<br><sub>0,1,1,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |
| Dailyn Swain (CHI) | 52% | 6.4<br><sub>7,-,-,-,-</sub> | 2.1<br><sub>3,-,-,-,-</sub> |  | 0.9<br><sub>1,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 4.1 |
| James Harden (CLE) | 98% | 35.1<br><sub>34,25,33,35,-</sub> | 21.7<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.6 | 3.3 | 33.7 |
| Donovan Mitchell (CLE) | 98% | 35.1<br><sub>37,23,36,33,-</sub> | 29.5<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 2.9 | 40.7 |
| Meleek Thomas (CLE) | 93% | 31.4<br><sub>24,27,22,18,34</sub> | 17.4<br><sub>9,18,14,12,20</sub> |  | 3.9<br><sub>4,3,4,0,4</sub> |  | 2.3<br><sub>0,3,1,3,2</sub> |  | 2.9<br><sub>3,4,2,2,3</sub> |  | 1.4 | 0.5 | 1.5 | 23.7 |
| Tyrese Proctor (CLE) | 96% | 31.2<br><sub>23,23,23,27,34</sub> | 15.5<br><sub>7,6,15,22,24</sub> |  | 5.3<br><sub>3,1,3,4,11</sub> |  | 5.0<br><sub>3,4,1,3,10</sub> |  | 2.5<br><sub>2,0,3,5,4</sub> |  | 1.4 | 0.1 | 1.5 | 25.8 |
| Jarrett Allen (CLE) | 76% | 29.7<br><sub>-,19,32,32,-</sub> | 15.5<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 10.1<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.1 | 1.5 | 1.4 | 27.3 |
| Mario Hezonja (CLE) | 98% | 25.2<br><sub>19,17,7,9,34</sub> | 11.0<br><sub>0,10,0,4,22</sub> |  | 6.5<br><sub>5,3,0,4,7</sub> |  | 2.0<br><sub>1,0,0,0,4</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 0.9 | 0.4 | 1.1 | 19.6 |
| Thomas Bryant (CLE) | 72% | 23.6<br><sub>15,15,-,16,27</sub> | 12.6<br><sub>5,11,-,9,19</sub> |  | 6.3<br><sub>3,2,-,1,11</sub> |  | 1.1<br><sub>1,0,-,1,3</sub> |  | 1.5<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.8 | 1.1 | 20.0 |
| Craig Porter Jr. (CLE) | 80% | 23.5<br><sub>15,17,-,9,28</sub> | 5.5<br><sub>0,9,-,0,9</sub> |  | 4.7<br><sub>1,2,-,2,9</sub> |  | 4.1<br><sub>1,4,-,2,6</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.7 | 1.1 | 14.4 |
| Norchad Omier (CLE) | 52% | 23.3<br><sub>-,12,-,-,27</sub> | 6.9<br><sub>-,0,-,-,13</sub> |  | 5.8<br><sub>-,3,-,-,8</sub> |  | 2.5<br><sub>-,2,-,-,2</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.9 | 0.2 | 0.8 | 15.1 |
| Riley Minix (CLE) | 52% | 18.1<br><sub>10,17,-,-,22</sub> | 6.1<br><sub>8,2,-,-,2</sub> |  | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.0<br><sub>0,0,-,-,0</sub> |  | 0.8<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 9.7 |
| Ernest Udeh Jr. (CLE) | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>if Peyton Watson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 31.1<br><sub>27,34,25,39,26</sub> | 14.6<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 8.5<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 2.7 | 30.1 |
| Norman Powell (CHI) | 98% | 31.0<br><sub>22,-,-,31,30</sub> | 21.2<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 26.8 |
| Matas Buzelis (CHI) | 98% | 30.3<br><sub>26,31,31,29,30</sub> | 16.9<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.1<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.0 | 2.3 | 24.6 |
| Isaac Okoro (CHI) | 98% | 29.1<br><sub>15,25,23,41,31</sub> | 9.4<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.4 | 0.9 | 14.2 |
| Patrick Williams (CHI) | 76% | 26.0<br><sub>20,25,28,24,26</sub> | 9.1<br><sub>4,7,9,13,14</sub> |  | 3.7<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.7 |
| Tre Jones (CHI) | 98% | 22.2<br><sub>18,14,28,15,24</sub> | 12.2<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.3 | 18.8 |
| Nic Claxton (CHI) | 98% | 20.2<br><sub>-,18,16,22,-</sub> | 7.8<br><sub>-,4,17,2,-</sub> |  | 5.7<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.9 | 15.7 |
| Zach Collins (CHI) | 71% | 18.4<br><sub>14,-,3,-,28</sub> | 7.2<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.4 |
| Leonard Miller (CHI) | 67% | 17.5<br><sub>19,-,2,-,17</sub> | 7.8<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.0<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.1 |
| Buddy Hield (CHI) | 71% | 17.4<br><sub>8,-,-,25,20</sub> | 8.4<br><sub>7,-,-,12,16</sub> |  | 2.4<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.3<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 1.0 | 12.5 |
| Noa Essengue (CHI) | 96% | 13.8<br><sub>14,15,11,8,7</sub> | 5.6<br><sub>6,10,8,5,0</sub> |  | 3.0<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 9.3 |
| Jordan Hawkins (CHI) | 58% | 12.7<br><sub>7,17,24,-,-</sub> | 5.3<br><sub>2,9,7,-,-</sub> |  | 1.6<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.7 |
| Dailyn Swain (CHI) | 52% | 8.4<br><sub>7,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 5.2 |
| James Harden (CLE) | 98% | 34.4<br><sub>34,25,33,35,-</sub> | 19.7<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.6 | 3.0 | 31.4 |
| Donovan Mitchell (CLE) | 98% | 34.3<br><sub>37,23,36,33,-</sub> | 27.5<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 2.7 | 38.2 |
| Peyton Watson (CLE) | 100% | 29.4<br><sub>29,21,30,30,-</sub> | 13.3<br><sub>12,13,7,4,-</sub> | 13.5 · – | 5.0<br><sub>6,2,5,4,-</sub> | 4.5 | 2.7<br><sub>3,1,4,2,-</sub> | 2.5 | 1.4<br><sub>1,2,2,0,-</sub> | 1.5 | 1.0 | 1.5 | 1.6 | 21.0 |
| Meleek Thomas (CLE) | 93% | 28.6<br><sub>24,27,22,18,34</sub> | 14.9<br><sub>9,18,14,12,20</sub> |  | 3.4<br><sub>4,3,4,0,4</sub> |  | 2.1<br><sub>0,3,1,3,2</sub> |  | 2.6<br><sub>3,4,2,2,3</sub> |  | 1.2 | 0.4 | 1.4 | 20.4 |
| Tyrese Proctor (CLE) | 96% | 28.1<br><sub>23,23,23,27,34</sub> | 13.2<br><sub>7,6,15,22,24</sub> |  | 4.7<br><sub>3,1,3,4,11</sub> |  | 4.3<br><sub>3,4,1,3,10</sub> |  | 2.2<br><sub>2,0,3,5,4</sub> |  | 1.2 | 0.1 | 1.3 | 22.3 |
| Jarrett Allen (CLE) | 76% | 27.6<br><sub>-,19,32,32,-</sub> | 14.2<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 9.3<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.5 | 1.2 | 25.1 |
| Mario Hezonja (CLE) | 98% | 22.2<br><sub>19,17,7,9,34</sub> | 9.6<br><sub>0,10,0,4,22</sub> |  | 5.7<br><sub>5,3,0,4,7</sub> |  | 1.7<br><sub>1,0,0,0,4</sub> |  | 1.1<br><sub>0,0,0,0,2</sub> |  | 0.8 | 0.4 | 1.0 | 17.0 |
| Norchad Omier (CLE) | 52% | 20.8<br><sub>-,12,-,-,27</sub> | 6.1<br><sub>-,0,-,-,13</sub> |  | 5.0<br><sub>-,3,-,-,8</sub> |  | 2.1<br><sub>-,2,-,-,2</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.8 | 0.2 | 0.7 | 13.1 |
| Thomas Bryant (CLE) | 72% | 20.7<br><sub>15,15,-,16,27</sub> | 11.4<br><sub>5,11,-,9,19</sub> |  | 5.5<br><sub>3,2,-,1,11</sub> |  | 1.0<br><sub>1,0,-,1,3</sub> |  | 1.3<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.7 | 1.0 | 17.9 |
| Craig Porter Jr. (CLE) | 80% | 19.3<br><sub>15,17,-,9,28</sub> | 4.5<br><sub>0,9,-,0,9</sub> |  | 3.9<br><sub>1,2,-,2,9</sub> |  | 3.4<br><sub>1,4,-,2,6</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 1.0 | 0.6 | 1.0 | 11.8 |
| Riley Minix (CLE) | 52% | 16.1<br><sub>10,17,-,-,22</sub> | 5.3<br><sub>8,2,-,-,2</sub> |  | 2.3<br><sub>3,2,-,-,0</sub> |  | 0.8<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.5 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>if Jaylon Tyson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 31.1<br><sub>27,34,25,39,26</sub> | 14.7<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 8.4<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.7 | 30.2 |
| Norman Powell (CHI) | 98% | 31.0<br><sub>22,-,-,31,30</sub> | 21.4<br><sub>12,-,-,33,24</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,-,-,5,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 27.0 |
| Matas Buzelis (CHI) | 98% | 30.4<br><sub>26,31,31,29,30</sub> | 17.0<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.2<br><sub>1,3,3,3,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.1 | 2.3 | 24.7 |
| Isaac Okoro (CHI) | 98% | 29.1<br><sub>15,25,23,41,31</sub> | 9.5<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.4 | 0.9 | 14.3 |
| Patrick Williams (CHI) | 76% | 26.0<br><sub>20,25,28,24,26</sub> | 9.2<br><sub>4,7,9,13,14</sub> |  | 3.7<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.8 |
| Tre Jones (CHI) | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.2<br><sub>14,6,13,4,16</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>3,1,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,3,3,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.3 | 18.8 |
| Nic Claxton (CHI) | 98% | 20.2<br><sub>-,18,16,22,-</sub> | 7.9<br><sub>-,4,17,2,-</sub> |  | 5.8<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.9 | 15.8 |
| Zach Collins (CHI) | 71% | 18.4<br><sub>14,-,3,-,28</sub> | 7.3<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.4 |
| Leonard Miller (CHI) | 67% | 17.5<br><sub>19,-,2,-,17</sub> | 7.9<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.0<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.2 |
| Buddy Hield (CHI) | 71% | 17.3<br><sub>8,-,-,25,20</sub> | 8.3<br><sub>7,-,-,12,16</sub> |  | 2.4<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.2<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 1.0 | 12.3 |
| Noa Essengue (CHI) | 96% | 13.8<br><sub>14,15,11,8,7</sub> | 5.6<br><sub>6,10,8,5,0</sub> |  | 3.0<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 9.3 |
| Jordan Hawkins (CHI) | 58% | 12.8<br><sub>7,17,24,-,-</sub> | 5.3<br><sub>2,9,7,-,-</sub> |  | 1.7<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.7 |
| Dailyn Swain (CHI) | 52% | 8.5<br><sub>7,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 5.2 |
| Donovan Mitchell (CLE) | 98% | 34.7<br><sub>37,23,36,33,-</sub> | 28.3<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 2.9 | 39.3 |
| James Harden (CLE) | 98% | 34.6<br><sub>34,25,33,35,-</sub> | 20.2<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.6 | 3.2 | 32.0 |
| Meleek Thomas (CLE) | 93% | 28.8<br><sub>24,27,22,18,34</sub> | 14.9<br><sub>9,18,14,12,20</sub> |  | 3.5<br><sub>4,3,4,0,4</sub> |  | 2.1<br><sub>0,3,1,3,2</sub> |  | 2.6<br><sub>3,4,2,2,3</sub> |  | 1.2 | 0.4 | 1.4 | 20.4 |
| Jaylon Tyson (CLE) | 100% | 28.8<br><sub>-,-,23,30,34</sub> | 12.7<br><sub>-,-,3,16,18</sub> | 13.5 · – | 5.0<br><sub>-,-,0,3,4</sub> | 4.5 | 2.9<br><sub>-,-,1,1,4</sub> | 2.5 | 1.9<br><sub>-,-,1,4,3</sub> | 2.5 | 0.9 | 0.4 | 1.4 | 20.6 |
| Tyrese Proctor (CLE) | 96% | 28.2<br><sub>23,23,23,27,34</sub> | 13.5<br><sub>7,6,15,22,24</sub> |  | 4.8<br><sub>3,1,3,4,11</sub> |  | 4.3<br><sub>3,4,1,3,10</sub> |  | 2.3<br><sub>2,0,3,5,4</sub> |  | 1.3 | 0.1 | 1.3 | 22.7 |
| Jarrett Allen (CLE) | 76% | 27.8<br><sub>-,19,32,32,-</sub> | 13.9<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 9.5<br><sub>-,7,14,8,-</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>-,1,3,1,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.5 | 1.2 | 24.9 |
| Mario Hezonja (CLE) | 98% | 22.6<br><sub>19,17,7,9,34</sub> | 9.9<br><sub>0,10,0,4,22</sub> |  | 5.8<br><sub>5,3,0,4,7</sub> |  | 1.7<br><sub>1,0,0,0,4</sub> |  | 1.1<br><sub>0,0,0,0,2</sub> |  | 0.8 | 0.4 | 1.1 | 17.4 |
| Thomas Bryant (CLE) | 72% | 21.4<br><sub>15,15,-,16,27</sub> | 11.5<br><sub>5,11,-,9,19</sub> |  | 5.7<br><sub>3,2,-,1,11</sub> |  | 1.0<br><sub>1,0,-,1,3</sub> |  | 1.3<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.8 | 1.1 | 18.3 |
| Norchad Omier (CLE) | 52% | 20.7<br><sub>-,12,-,-,27</sub> | 6.0<br><sub>-,0,-,-,13</sub> |  | 5.0<br><sub>-,3,-,-,8</sub> |  | 2.2<br><sub>-,2,-,-,2</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.8 | 0.2 | 0.7 | 13.2 |
| Craig Porter Jr. (CLE) | 80% | 19.9<br><sub>15,17,-,9,28</sub> | 4.7<br><sub>0,9,-,0,9</sub> |  | 4.0<br><sub>1,2,-,2,9</sub> |  | 3.6<br><sub>1,4,-,2,6</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 1.0 | 0.6 | 1.0 | 12.3 |
| Riley Minix (CLE) | 52% | 16.6<br><sub>10,17,-,-,22</sub> | 5.5<br><sub>8,2,-,-,2</sub> |  | 2.4<br><sub>3,2,-,-,0</sub> |  | 0.9<br><sub>0,0,-,-,0</sub> |  | 0.7<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.8 |
| Ernest Udeh Jr. (CLE) | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>


### MEM @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), GG Jackson (MEM), Ty Jerome (MEM), Scotty Pippen Jr. (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 124.4–118.9 | MEM 65% | 1.53 / 2.89 | WAS +5.5 | 243.5 | WAS +3.5 covers 43%; o232.5 72% |
| Expected (weighted by chance each plays) | 124.7–119.3 | MEM 65% | 1.53 / 2.89 | WAS +5.5 | 243.5 | WAS +3.5 covers 44%; o232.5 73% |
| if Zach Edey plays | 124.3–118.7 | MEM 65% | 1.53 / 2.89 | WAS +5.5 | 242.5 | WAS +3.5 covers 43%; o232.5 71% |
| if Tre Johnson plays | 124.6–119.0 | MEM 65% | 1.53 / 2.89 | WAS +5.5 | 243.5 | WAS +3.5 covers 43%; o232.5 72% |
| if Isaiah Stewart plays | 124.6–118.8 | MEM 66% | 1.52 / 2.94 | WAS +6.5 | 243.5 | WAS +3.5 covers 43%; o232.5 72% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey (MEM) | Questionable | 55% | 24.0 | 11.1 | 10.1 | 1.3 | 0.1 | 0.6 | 1.6 | 1.7 | 22.5 | full tables below |
| Tre Johnson (WAS) | Day-To-Day | 70% | 21.3 | 8.8 | 2.2 | 1.1 | 1.2 | 0.7 | 0.2 | 0.9 | 12.1 | full tables below |
| Quinten Post (MEM) | Questionable | 55% | 15.1 | 5.5 | 3.1 | 0.8 | 0.7 | 0.5 | 0.3 | 0.6 | 9.5 | small |
| Isaiah Stewart (MEM) | Questionable | 55% | 21.1 | 11.0 | 4.8 | 1.2 | 0.7 | 0.4 | 1.2 | 1.1 | 17.0 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 34.1<br><sub>31,33,33,25,29</sub> | 20.1<br><sub>8,22,13,12,15</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 10.8<br><sub>12,7,11,10,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 5.9<br><sub>4,8,5,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.6 | 3.3 | 36.7 |
| Cedric Coward | 98% | 32.1<br><sub>23,28,27,30,33</sub> | 19.5<br><sub>10,3,15,14,23</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>9,6,11,7,12</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>0,4,4,6,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.6 | 2.1 | 32.0 |
| Jaylen Wells | 98% | 30.3<br><sub>25,26,31,27,25</sub> | 16.1<br><sub>7,14,22,11,5</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>0,4,2,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,1,1,1,2</sub> |  | 2.2<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 1.3 | 21.5 |
| Cam Spencer | 98% | 29.6<br><sub>19,17,20,24,34</sub> | 15.6<br><sub>7,7,15,14,17</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>1,2,3,2,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 7.4<br><sub>0,4,3,5,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,3,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 1.8 | 26.6 |
| Javon Small | 96% | 28.0<br><sub>21,24,15,15,30</sub> | 15.8<br><sub>10,9,3,10,19</sub> |  | 4.1<br><sub>4,2,1,2,2</sub> |  | 4.9<br><sub>2,5,4,5,5</sub> |  | 1.7<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.6 | 24.9 |
| Jerami Grant | 98% | 27.9<br><sub>22,22,20,26,-</sub> | 16.8<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>0,3,2,1,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,2,2,1,-</sub> |  | 2.0<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.6 | 1.7 | 21.9 |
| Taylor Hendricks | 80% | 24.8<br><sub>4,16,11,19,29</sub> | 11.9<br><sub>4,9,7,10,22</sub> |  | 5.8<br><sub>2,3,2,12,5</sub> |  | 1.4<br><sub>0,0,1,2,4</sub> |  | 1.4<br><sub>1,1,1,2,0</sub> |  | 1.3 | 0.7 | 1.2 | 19.1 |
| Olivier-Maxence Prosper | 67% | 18.1<br><sub>11,1,-,2,20</sub> | 10.8<br><sub>2,0,-,6,11</sub> |  | 3.9<br><sub>3,0,-,1,4</sub> |  | 1.1<br><sub>1,0,-,0,0</sub> |  | 1.0<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.3 | 0.9 | 15.8 |
| Kris Murray | 80% | 17.7<br><sub>13,1,-,1,19</sub> | 4.0<br><sub>2,0,-,0,3</sub> |  | 3.2<br><sub>2,0,-,1,2</sub> |  | 1.2<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.4 | 0.6 | 8.4 |
| Jahmai Mashack | 52% | 13.3<br><sub>4,-,-,-,2</sub> | 4.4<br><sub>0,-,-,-,0</sub> |  | 1.8<br><sub>0,-,-,-,0</sub> |  | 1.7<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.8 | 0.2 | 0.9 | 7.9 |
| Karim Lopez | 52% | 10.1<br><sub>4,-,-,-,2</sub> | 3.1<br><sub>2,-,-,-,0</sub> |  | 2.5<br><sub>0,-,-,-,2</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.4 | 0.5 | 6.2 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.6<br><sub>28,38,34,45,26</sub> | 19.4<br><sub>4,20,15,37,0</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>3,7,4,14,8</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,3,3,4,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.4 | 32.5 |
| Anthony Davis | 98% | 35.2<br><sub>-,34,34,44,31</sub> | 23.9<br><sub>-,44,21,30,14</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 12.1<br><sub>-,13,13,15,8</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>-,1,0,4,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>-,2,0,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.3 | 2.0 | 2.4 | 39.1 |
| AJ Dybantsa | 98% | 34.3<br><sub>31,37,34,44,30</sub> | 15.7<br><sub>19,21,13,5,16</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>6,8,4,8,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.7 | 2.4 | 24.5 |
| Kyshawn George | 98% | 33.3<br><sub>30,35,39,26,30</sub> | 16.9<br><sub>14,12,25,14,11</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,3,9,1,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,2,3,5,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>2,2,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.3 | 2.4 | 26.5 |
| Alex Sarr | 98% | 29.0<br><sub>28,25,25,44,27</sub> | 14.7<br><sub>15,4,5,30,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>14,8,8,9,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>1,0,0,2,2</sub> |  | 1.3<br><sub>1,0,1,4,3</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.9 | 2.0 | 1.6 | 25.1 |
| Bilal Coulibaly | 98% | 25.5<br><sub>20,-,25,29,21</sub> | 9.4<br><sub>0,-,5,4,9</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,-,6,7,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>0,-,2,0,0</sub> |  | 0.8<br><sub>0,-,0,0,1</sub> |  | 1.2 | 1.0 | 1.2 | 15.2 |
| Bub Carrington | 98% | 19.2<br><sub>21,19,10,16,23</sub> | 6.7<br><sub>9,4,0,2,11</sub> |  | 2.0<br><sub>6,0,0,0,0</sub> |  | 2.8<br><sub>1,4,0,2,4</sub> |  | 1.0<br><sub>3,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.1 | 11.5 |
| Deandre Ayton | 98% | 13.7<br><sub>7,13,9,9,10</sub> | 4.9<br><sub>2,2,2,2,2</sub> |  | 4.5<br><sub>1,8,2,4,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.6 | 9.9 |
| Will Riley | 80% | 12.5<br><sub>20,4,-,3,16</sub> | 5.7<br><sub>5,0,-,3,14</sub> |  | 1.5<br><sub>2,0,-,0,3</sub> |  | 1.0<br><sub>1,1,-,0,0</sub> |  | 0.5<br><sub>0,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.7 | 8.3 |
| Khris Middleton | 48% | 12.2<br><sub>-,-,-,-,9</sub> | 4.5<br><sub>-,-,-,-,8</sub> |  | 1.9<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 7.5 |
| Tre Mann | 52% | 8.2<br><sub>18,2,-,-,11</sub> | 3.6<br><sub>2,0,-,-,4</sub> |  | 1.1<br><sub>0,0,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |
| Anthony Gill | 52% | 7.9<br><sub>9,2,-,-,6</sub> | 2.9<br><sub>1,0,-,-,5</sub> |  | 1.4<br><sub>1,2,-,-,1</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Felix Okpara | 58% | 6.0<br><sub>-,2,-,-,-</sub> | 2.5<br><sub>-,2,-,-,-</sub> |  | 1.8<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.6 |

</details>

<details><summary>if Isaiah Stewart plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 33.7<br><sub>31,33,33,25,29</sub> | 19.3<br><sub>8,22,13,12,15</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>12,7,11,10,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 5.8<br><sub>4,8,5,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.6 | 3.2 | 35.2 |
| Cedric Coward (MEM) | 98% | 31.8<br><sub>23,28,27,30,33</sub> | 18.6<br><sub>10,3,15,14,23</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 8.5<br><sub>9,6,11,7,12</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>0,4,4,6,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.0 | 31.1 |
| Jaylen Wells (MEM) | 98% | 29.4<br><sub>25,26,31,27,25</sub> | 14.5<br><sub>7,14,22,11,5</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>0,4,2,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,1,1,1,2</sub> |  | 2.1<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.1 | 1.2 | 19.7 |
| Cam Spencer (MEM) | 98% | 28.9<br><sub>19,17,20,24,34</sub> | 14.7<br><sub>7,7,15,14,17</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>1,2,3,2,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 7.6<br><sub>0,4,3,5,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,3,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 1.7 | 25.8 |
| Javon Small (MEM) | 96% | 27.1<br><sub>21,24,15,15,30</sub> | 14.4<br><sub>10,9,3,10,19</sub> |  | 3.9<br><sub>4,2,1,2,2</sub> |  | 5.1<br><sub>2,5,4,5,5</sub> |  | 1.6<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.6 | 23.4 |
| Jerami Grant (MEM) | 98% | 27.0<br><sub>22,22,20,26,-</sub> | 15.3<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>0,3,2,1,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,2,2,1,-</sub> |  | 1.8<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.6 | 1.6 | 20.3 |
| Taylor Hendricks (MEM) | 80% | 22.7<br><sub>4,16,11,19,29</sub> | 10.6<br><sub>4,9,7,10,22</sub> |  | 5.3<br><sub>2,3,2,12,5</sub> |  | 1.4<br><sub>0,0,1,2,4</sub> |  | 1.2<br><sub>1,1,1,2,0</sub> |  | 1.2 | 0.6 | 1.1 | 17.2 |
| Isaiah Stewart (MEM) | 100% | 21.1<br><sub>-,-,18,20,15</sub> | 11.0<br><sub>-,-,3,12,11</sub> |  | 4.8<br><sub>-,-,1,5,3</sub> |  | 1.2<br><sub>-,-,2,0,3</sub> |  | 0.7<br><sub>-,-,1,0,0</sub> |  | 0.4 | 1.2 | 1.1 | 17.0 |
| Olivier-Maxence Prosper (MEM) | 67% | 16.6<br><sub>11,1,-,2,20</sub> | 9.3<br><sub>2,0,-,6,11</sub> |  | 3.6<br><sub>3,0,-,1,4</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 13.8 |
| Kris Murray (MEM) | 80% | 15.9<br><sub>13,1,-,1,19</sub> | 3.8<br><sub>2,0,-,0,3</sub> |  | 2.8<br><sub>2,0,-,1,2</sub> |  | 1.1<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.3 | 0.6 | 7.7 |
| Jahmai Mashack (MEM) | 52% | 11.4<br><sub>4,-,-,-,2</sub> | 3.7<br><sub>0,-,-,-,0</sub> |  | 1.5<br><sub>0,-,-,-,0</sub> |  | 1.4<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.7 | 0.2 | 0.8 | 6.6 |
| Karim Lopez (MEM) | 52% | 8.3<br><sub>4,-,-,-,2</sub> | 2.6<br><sub>2,-,-,-,0</sub> |  | 2.0<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.5 | 5.1 |
| Trae Young (WAS) | 98% | 35.6<br><sub>28,38,34,45,26</sub> | 19.4<br><sub>4,20,15,37,0</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>3,7,4,14,8</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,3,3,4,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.5 | 32.4 |
| Anthony Davis (WAS) | 98% | 35.2<br><sub>-,34,34,44,31</sub> | 23.9<br><sub>-,44,21,30,14</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 12.2<br><sub>-,13,13,15,8</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>-,1,0,4,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>-,2,0,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.3 | 2.0 | 2.4 | 39.2 |
| AJ Dybantsa (WAS) | 98% | 34.3<br><sub>31,37,34,44,30</sub> | 15.7<br><sub>19,21,13,5,16</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>6,8,4,8,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.7 | 2.4 | 24.5 |
| Kyshawn George (WAS) | 98% | 33.3<br><sub>30,35,39,26,30</sub> | 16.9<br><sub>14,12,25,14,11</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,3,9,1,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,2,3,5,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>2,2,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.3 | 2.4 | 26.4 |
| Alex Sarr (WAS) | 98% | 29.0<br><sub>28,25,25,44,27</sub> | 14.6<br><sub>15,4,5,30,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>14,8,8,9,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>1,0,0,2,2</sub> |  | 1.3<br><sub>1,0,1,4,3</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.9 | 2.0 | 1.6 | 25.0 |
| Bilal Coulibaly (WAS) | 98% | 25.5<br><sub>20,-,25,29,21</sub> | 9.3<br><sub>0,-,5,4,9</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,-,6,7,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>0,-,2,0,0</sub> |  | 0.8<br><sub>0,-,0,0,1</sub> |  | 1.2 | 1.0 | 1.2 | 15.1 |
| Bub Carrington (WAS) | 98% | 19.2<br><sub>21,19,10,16,23</sub> | 6.7<br><sub>9,4,0,2,11</sub> |  | 2.0<br><sub>6,0,0,0,0</sub> |  | 2.8<br><sub>1,4,0,2,4</sub> |  | 1.0<br><sub>3,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.1 | 11.5 |
| Deandre Ayton (WAS) | 98% | 13.7<br><sub>7,13,9,9,10</sub> | 4.9<br><sub>2,2,2,2,2</sub> |  | 4.5<br><sub>1,8,2,4,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.6 | 9.9 |
| Will Riley (WAS) | 80% | 12.5<br><sub>20,4,-,3,16</sub> | 5.7<br><sub>5,0,-,3,14</sub> |  | 1.5<br><sub>2,0,-,0,3</sub> |  | 1.0<br><sub>1,1,-,0,0</sub> |  | 0.5<br><sub>0,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.7 | 8.2 |
| Khris Middleton (WAS) | 48% | 12.2<br><sub>-,-,-,-,9</sub> | 4.5<br><sub>-,-,-,-,8</sub> |  | 1.9<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 7.4 |
| Tre Mann (WAS) | 52% | 8.2<br><sub>18,2,-,-,11</sub> | 3.5<br><sub>2,0,-,-,4</sub> |  | 1.1<br><sub>0,0,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |
| Anthony Gill (WAS) | 52% | 7.9<br><sub>9,2,-,-,6</sub> | 2.9<br><sub>1,0,-,-,5</sub> |  | 1.4<br><sub>1,2,-,-,1</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |
| Felix Okpara (WAS) | 58% | 6.0<br><sub>-,2,-,-,-</sub> | 2.5<br><sub>-,2,-,-,-</sub> |  | 1.8<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.6 |

</details>

<details><summary>if Zach Edey plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 33.8<br><sub>31,33,33,25,29</sub> | 19.3<br><sub>8,22,13,12,15</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>12,7,11,10,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 5.9<br><sub>4,8,5,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.6 | 3.2 | 35.4 |
| Cedric Coward (MEM) | 98% | 31.9<br><sub>23,28,27,30,33</sub> | 18.2<br><sub>10,3,15,14,23</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 8.4<br><sub>9,6,11,7,12</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>0,4,4,6,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 2.1 | 30.6 |
| Jaylen Wells (MEM) | 98% | 29.5<br><sub>25,26,31,27,25</sub> | 14.5<br><sub>7,14,22,11,5</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>0,4,2,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,1,1,1,2</sub> |  | 2.1<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 1.2 | 19.7 |
| Cam Spencer (MEM) | 98% | 28.9<br><sub>19,17,20,24,34</sub> | 14.7<br><sub>7,7,15,14,17</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>1,2,3,2,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 7.7<br><sub>0,4,3,5,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,3,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 1.7 | 25.7 |
| Javon Small (MEM) | 96% | 27.3<br><sub>21,24,15,15,30</sub> | 14.3<br><sub>10,9,3,10,19</sub> |  | 3.8<br><sub>4,2,1,2,2</sub> |  | 5.2<br><sub>2,5,4,5,5</sub> |  | 1.6<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.7 | 23.4 |
| Jerami Grant (MEM) | 98% | 26.8<br><sub>22,22,20,26,-</sub> | 15.4<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>0,3,2,1,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,2,2,1,-</sub> |  | 1.8<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.6 | 1.6 | 20.3 |
| Zach Edey (MEM) | 100% | 24.0<br><sub>20,23,20,-,-</sub> | 11.1<br><sub>14,8,2,-,-</sub> | 8.5 · – | 10.1<br><sub>6,9,5,-,-</sub> | 6.5 | 1.3<br><sub>1,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.6 | 1.6 | 1.7 | 22.5 |
| Taylor Hendricks (MEM) | 80% | 22.3<br><sub>4,16,11,19,29</sub> | 10.4<br><sub>4,9,7,10,22</sub> |  | 5.2<br><sub>2,3,2,12,5</sub> |  | 1.3<br><sub>0,0,1,2,4</sub> |  | 1.2<br><sub>1,1,1,2,0</sub> |  | 1.1 | 0.6 | 1.1 | 16.8 |
| Olivier-Maxence Prosper (MEM) | 67% | 16.2<br><sub>11,1,-,2,20</sub> | 9.1<br><sub>2,0,-,6,11</sub> |  | 3.5<br><sub>3,0,-,1,4</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 13.5 |
| Kris Murray (MEM) | 80% | 15.7<br><sub>13,1,-,1,19</sub> | 3.8<br><sub>2,0,-,0,3</sub> |  | 2.7<br><sub>2,0,-,1,2</sub> |  | 1.1<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.3 | 0.6 | 7.5 |
| Jahmai Mashack (MEM) | 52% | 10.8<br><sub>4,-,-,-,2</sub> | 3.5<br><sub>0,-,-,-,0</sub> |  | 1.4<br><sub>0,-,-,-,0</sub> |  | 1.4<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.8 | 6.3 |
| Karim Lopez (MEM) | 52% | 7.8<br><sub>4,-,-,-,2</sub> | 2.6<br><sub>2,-,-,-,0</sub> |  | 1.9<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.4 | 4.9 |
| Trae Young (WAS) | 98% | 35.6<br><sub>28,38,34,45,26</sub> | 19.4<br><sub>4,20,15,37,0</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>3,7,4,14,8</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,3,3,4,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.5 | 32.3 |
| Anthony Davis (WAS) | 98% | 35.1<br><sub>-,34,34,44,31</sub> | 23.9<br><sub>-,44,21,30,14</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 12.1<br><sub>-,13,13,15,8</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>-,1,0,4,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>-,2,0,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.3 | 2.0 | 2.4 | 39.1 |
| AJ Dybantsa (WAS) | 98% | 34.3<br><sub>31,37,34,44,30</sub> | 15.7<br><sub>19,21,13,5,16</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>6,8,4,8,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.7 | 2.4 | 24.6 |
| Kyshawn George (WAS) | 98% | 33.3<br><sub>30,35,39,26,30</sub> | 16.9<br><sub>14,12,25,14,11</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,3,9,1,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,2,3,5,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>2,2,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.3 | 2.4 | 26.4 |
| Alex Sarr (WAS) | 98% | 28.9<br><sub>28,25,25,44,27</sub> | 14.6<br><sub>15,4,5,30,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 8.0<br><sub>14,8,8,9,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>1,0,0,2,2</sub> |  | 1.3<br><sub>1,0,1,4,3</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.9 | 2.0 | 1.6 | 25.0 |
| Bilal Coulibaly (WAS) | 98% | 25.5<br><sub>20,-,25,29,21</sub> | 9.3<br><sub>0,-,5,4,9</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,-,6,7,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>0,-,2,0,0</sub> |  | 0.8<br><sub>0,-,0,0,1</sub> |  | 1.2 | 1.0 | 1.1 | 15.1 |
| Bub Carrington (WAS) | 98% | 19.2<br><sub>21,19,10,16,23</sub> | 6.7<br><sub>9,4,0,2,11</sub> |  | 2.0<br><sub>6,0,0,0,0</sub> |  | 2.8<br><sub>1,4,0,2,4</sub> |  | 1.0<br><sub>3,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.1 | 11.5 |
| Deandre Ayton (WAS) | 98% | 13.6<br><sub>7,13,9,9,10</sub> | 4.8<br><sub>2,2,2,2,2</sub> |  | 4.4<br><sub>1,8,2,4,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.6 | 9.8 |
| Will Riley (WAS) | 80% | 12.5<br><sub>20,4,-,3,16</sub> | 5.7<br><sub>5,0,-,3,14</sub> |  | 1.5<br><sub>2,0,-,0,3</sub> |  | 1.0<br><sub>1,1,-,0,0</sub> |  | 0.5<br><sub>0,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.7 | 8.3 |
| Khris Middleton (WAS) | 48% | 12.2<br><sub>-,-,-,-,9</sub> | 4.5<br><sub>-,-,-,-,8</sub> |  | 1.9<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 7.4 |
| Tre Mann (WAS) | 52% | 8.2<br><sub>18,2,-,-,11</sub> | 3.6<br><sub>2,0,-,-,4</sub> |  | 1.1<br><sub>0,0,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 5.6 |
| Anthony Gill (WAS) | 52% | 7.9<br><sub>9,2,-,-,6</sub> | 2.9<br><sub>1,0,-,-,5</sub> |  | 1.4<br><sub>1,2,-,-,1</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |
| Felix Okpara (WAS) | 58% | 5.9<br><sub>-,2,-,-,-</sub> | 2.4<br><sub>-,2,-,-,-</sub> |  | 1.7<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.5 |

</details>

<details><summary>if Tre Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 34.1<br><sub>31,33,33,25,29</sub> | 20.0<br><sub>8,22,13,12,15</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 10.8<br><sub>12,7,11,10,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 5.9<br><sub>4,8,5,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.7 | 3.3 | 36.6 |
| Cedric Coward (MEM) | 98% | 32.1<br><sub>23,28,27,30,33</sub> | 19.4<br><sub>10,3,15,14,23</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 8.7<br><sub>9,6,11,7,12</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>0,4,4,6,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.5 | 2.1 | 31.9 |
| Jaylen Wells (MEM) | 98% | 30.3<br><sub>25,26,31,27,25</sub> | 16.1<br><sub>7,14,22,11,5</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>0,4,2,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,1,1,1,2</sub> |  | 2.2<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 1.3 | 21.6 |
| Cam Spencer (MEM) | 98% | 29.6<br><sub>19,17,20,24,34</sub> | 15.7<br><sub>7,7,15,14,17</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>1,2,3,2,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 7.4<br><sub>0,4,3,5,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,3,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 1.8 | 26.7 |
| Javon Small (MEM) | 96% | 28.1<br><sub>21,24,15,15,30</sub> | 15.9<br><sub>10,9,3,10,19</sub> |  | 4.1<br><sub>4,2,1,2,2</sub> |  | 4.9<br><sub>2,5,4,5,5</sub> |  | 1.7<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.7 | 24.9 |
| Jerami Grant (MEM) | 98% | 28.0<br><sub>22,22,20,26,-</sub> | 17.0<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>0,3,2,1,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,2,2,1,-</sub> |  | 2.0<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.6 | 1.7 | 22.1 |
| Taylor Hendricks (MEM) | 80% | 24.8<br><sub>4,16,11,19,29</sub> | 11.9<br><sub>4,9,7,10,22</sub> |  | 5.8<br><sub>2,3,2,12,5</sub> |  | 1.4<br><sub>0,0,1,2,4</sub> |  | 1.4<br><sub>1,1,1,2,0</sub> |  | 1.3 | 0.7 | 1.2 | 19.1 |
| Olivier-Maxence Prosper (MEM) | 67% | 18.0<br><sub>11,1,-,2,20</sub> | 10.7<br><sub>2,0,-,6,11</sub> |  | 3.9<br><sub>3,0,-,1,4</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 1.0<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.3 | 0.9 | 15.7 |
| Kris Murray (MEM) | 80% | 17.8<br><sub>13,1,-,1,19</sub> | 4.0<br><sub>2,0,-,0,3</sub> |  | 3.1<br><sub>2,0,-,1,2</sub> |  | 1.2<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.4 | 0.6 | 8.4 |
| Jahmai Mashack (MEM) | 52% | 13.5<br><sub>4,-,-,-,2</sub> | 4.5<br><sub>0,-,-,-,0</sub> |  | 1.9<br><sub>0,-,-,-,0</sub> |  | 1.7<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.8 | 0.2 | 0.9 | 8.1 |
| Karim Lopez (MEM) | 52% | 10.1<br><sub>4,-,-,-,2</sub> | 3.2<br><sub>2,-,-,-,0</sub> |  | 2.5<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.4 | 0.6 | 6.2 |
| Anthony Davis (WAS) | 98% | 33.3<br><sub>-,34,34,44,31</sub> | 23.4<br><sub>-,44,21,30,14</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 11.5<br><sub>-,13,13,15,8</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>-,1,0,4,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>-,2,0,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.2 | 1.9 | 2.2 | 37.8 |
| Trae Young (WAS) | 98% | 33.3<br><sub>28,38,34,45,26</sub> | 18.2<br><sub>4,20,15,37,0</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.5<br><sub>3,7,4,14,8</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>0,3,3,4,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 3.2 | 30.8 |
| AJ Dybantsa (WAS) | 98% | 32.0<br><sub>31,37,34,44,30</sub> | 15.1<br><sub>19,21,13,5,16</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>6,8,4,8,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.6 | 2.2 | 23.5 |
| Kyshawn George (WAS) | 98% | 30.7<br><sub>30,35,39,26,30</sub> | 15.4<br><sub>14,12,25,14,11</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>7,3,9,1,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,2,3,5,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,2,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 1.3 | 2.1 | 24.2 |
| Alex Sarr (WAS) | 98% | 26.3<br><sub>28,25,25,44,27</sub> | 13.4<br><sub>15,4,5,30,25</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>14,8,8,9,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>1,0,0,2,2</sub> |  | 1.2<br><sub>1,0,1,4,3</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.8 | 1.8 | 1.5 | 22.8 |
| Bilal Coulibaly (WAS) | 98% | 22.9<br><sub>20,-,25,29,21</sub> | 8.4<br><sub>0,-,5,4,9</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 3.7<br><sub>5,-,6,7,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,-,2,0,0</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 1.1 | 0.9 | 1.1 | 13.6 |
| Tre Johnson (WAS) | 100% | 21.3<br><sub>28,29,29,30,-</sub> | 8.8<br><sub>4,2,15,13,-</sub> |  | 2.2<br><sub>0,2,3,4,-</sub> |  | 1.1<br><sub>3,0,1,2,-</sub> |  | 1.2<br><sub>0,0,2,1,-</sub> |  | 0.7 | 0.2 | 0.9 | 12.1 |
| Bub Carrington (WAS) | 98% | 17.1<br><sub>21,19,10,16,23</sub> | 6.2<br><sub>9,4,0,2,11</sub> |  | 1.8<br><sub>6,0,0,0,0</sub> |  | 2.6<br><sub>1,4,0,2,4</sub> |  | 0.9<br><sub>3,1,0,0,3</sub> |  | 0.5 | 0.2 | 1.0 | 10.6 |
| Deandre Ayton (WAS) | 98% | 12.8<br><sub>7,13,9,9,10</sub> | 4.8<br><sub>2,2,2,2,2</sub> |  | 4.3<br><sub>1,8,2,4,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.6 | 9.6 |
| Khris Middleton (WAS) | 48% | 11.1<br><sub>-,-,-,-,9</sub> | 4.0<br><sub>-,-,-,-,8</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 6.9 |
| Will Riley (WAS) | 80% | 10.1<br><sub>20,4,-,3,16</sub> | 4.7<br><sub>5,0,-,3,14</sub> |  | 1.2<br><sub>2,0,-,0,3</sub> |  | 0.9<br><sub>1,1,-,0,0</sub> |  | 0.4<br><sub>0,0,-,1,2</sub> |  | 0.4 | 0.1 | 0.6 | 6.9 |
| Anthony Gill (WAS) | 52% | 7.2<br><sub>9,2,-,-,6</sub> | 2.7<br><sub>1,0,-,-,5</sub> |  | 1.2<br><sub>1,2,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Tre Mann (WAS) | 52% | 6.7<br><sub>18,2,-,-,11</sub> | 3.1<br><sub>2,0,-,-,4</sub> |  | 0.9<br><sub>0,0,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,1</sub> |  | 0.2<br><sub>0,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.4 | 4.8 |
| Felix Okpara (WAS) | 58% | 5.8<br><sub>-,2,-,-,-</sub> | 2.5<br><sub>-,2,-,-,-</sub> |  | 1.7<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.5 |

</details>


### PHI @ BKN
Out: Grant Nelson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Dominick Barlow (PHI), Adem Bona (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.1–111.9 | PHI 60% | 1.68 / 2.47 | BKN +3.5 | 226.5 | BKN +5.5 covers 56%; o226.5 51% |
| Expected (weighted by chance each plays) | 115.5–111.6 | PHI 62% | 1.63 / 2.60 | BKN +4.5 | 226.5 | BKN +5.5 covers 54%; o226.5 51% |
| if Joel Embiid plays | 115.6–111.5 | PHI 62% | 1.62 / 2.62 | BKN +4.5 | 226.5 | BKN +5.5 covers 54%; o226.5 51% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Joel Embiid (PHI) | Day-To-Day | 70% | 32.1 | 21.9 | 8.2 | 4.2 | 1.0 | 0.8 | 1.1 | 2.9 | 34.4 | full tables below |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 37.7<br><sub>32,36,34,35,36</sub> | 26.9<br><sub>17,27,24,27,27</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>3,4,1,2,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>4,7,4,8,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>2,3,3,1,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.5 | 0.6 | 2.5 | 36.8 |
| Jaylen Brown | 98% | 35.8<br><sub>34,35,26,36,32</sub> | 25.1<br><sub>20,29,13,18,31</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>5,7,5,6,2</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 4.1<br><sub>5,4,2,2,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>2,2,1,0,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.5 | 3.3 | 35.3 |
| VJ Edgecombe | 96% | 35.2<br><sub>32,35,32,36,31</sub> | 14.8<br><sub>19,13,8,15,11</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 5.9<br><sub>3,6,4,8,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>2,3,5,8,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>3,3,0,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.5 | 1.6 | 24.9 |
| LeBron James | 98% | 34.5<br><sub>32,33,29,-,33</sub> | 18.6<br><sub>8,22,11,-,15</sub> |  | 6.8<br><sub>7,5,8,-,7</sub> |  | 7.0<br><sub>3,5,5,-,11</sub> |  | 1.3<br><sub>0,2,1,-,0</sub> |  | 1.2 | 0.6 | 3.0 | 32.4 |
| Dean Wade | 96% | 29.6<br><sub>21,18,23,34,35</sub> | 5.9<br><sub>0,0,8,6,12</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>5,1,9,5,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,1,0,2,3</sub> |  | 0.9<br><sub>0,0,2,2,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.4 | 0.9 | 12.3 |
| Kentavious Caldwell-Pope | 98% | 22.6<br><sub>17,21,16,27,22</sub> | 5.8<br><sub>5,6,0,11,9</sub> |  | 2.5<br><sub>2,6,0,4,5</sub> |  | 1.7<br><sub>0,3,2,5,0</sub> |  | 0.8<br><sub>1,2,0,3,2</sub> |  | 1.0 | 0.3 | 0.8 | 10.0 |
| Anfernee Simons | 98% | 21.6<br><sub>19,16,18,23,15</sub> | 10.4<br><sub>6,3,17,17,12</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,4,3,3,0</sub> |  | 1.6<br><sub>2,2,0,2,0</sub> |  | 1.8<br><sub>1,1,3,5,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.5 | 0.1 | 0.9 | 14.2 |
| Jabari Walker | 88% | 19.4<br><sub>17,19,15,16,25</sub> | 7.5<br><sub>8,9,2,9,11</sub> |  | 5.4<br><sub>5,11,4,8,7</sub> |  | 0.9<br><sub>1,0,0,1,1</sub> |  | 0.7<br><sub>0,1,0,1,3</sub> |  | 0.6 | 0.3 | 0.8 | 13.9 |
| Rayan Rupert | 47% | 9.4<br><sub>-,-,6,-,-</sub> | 3.2<br><sub>-,-,0,-,-</sub> |  | 1.8<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.1 | 0.6 | 5.6 |
| Tacko Fall | 76% | 9.2<br><sub>3,-,-,1,5</sub> | 0.5<br><sub>0,-,-,0,0</sub> |  | 2.1<br><sub>1,-,-,0,3</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.5 | 0.4 | 3.0 |
| Justin Edwards | 52% | 8.9<br><sub>4,-,6,1,-</sub> | 3.6<br><sub>3,-,0,0,-</sub> |  | 1.2<br><sub>1,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.3<br><sub>1,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.3 |
| Labaron Philon Jr. | 72% | 8.7<br><sub>4,-,6,2,6</sub> | 3.2<br><sub>3,-,2,0,3</sub> |  | 1.3<br><sub>1,-,1,0,1</sub> |  | 0.8<br><sub>1,-,3,0,0</sub> |  | 0.3<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Caleb Love | 38% | 7.7<br><sub>-,-,-,1,-</sub> | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.2 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 76% | 32.0<br><sub>38,36,29,28,-</sub> | 20.2<br><sub>26,25,19,22,-</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>10,9,9,6,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>0,1,0,3,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>4,3,4,4,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.4 | 2.0 | 29.2 |
| Julius Randle | 98% | 31.4<br><sub>31,34,30,29,31</sub> | 18.5<br><sub>22,19,13,17,22</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>3,7,4,4,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>4,8,4,5,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.2 | 3.1 | 29.3 |
| Day'Ron Sharpe | 98% | 24.0<br><sub>27,32,20,19,28</sub> | 10.3<br><sub>6,12,6,15,16</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 7.9<br><sub>5,10,4,4,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>8,13,6,5,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.9 | 1.9 | 22.3 |
| Egor Demin | 98% | 23.2<br><sub>-,-,-,23,27</sub> | 9.7<br><sub>-,-,-,22,11</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>-,-,-,1,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>-,-,-,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>-,-,-,4,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.3 | 1.4 | 15.4 |
| Danny Wolf | 76% | 23.0<br><sub>19,31,36,29,28</sub> | 9.8<br><sub>12,11,10,10,14</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>5,9,3,11,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>2,2,1,1,4</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.5 | 0.6 | 1.3 | 17.7 |
| Mikel Brown Jr. | 97% | 22.0<br><sub>20,25,-,-,20</sub> | 10.8<br><sub>18,18,-,-,6</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,1,-,-,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>4,3,-,-,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>3,3,-,-,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.2 | 1.8 | 16.5 |
| Nolan Traore | 98% | 21.6<br><sub>27,23,21,-,20</sub> | 10.8<br><sub>16,19,14,-,11</sub> |  | 2.0<br><sub>4,1,1,-,1</sub> |  | 3.2<br><sub>2,2,2,-,2</sub> |  | 1.2<br><sub>2,2,2,-,0</sub> |  | 0.8 | 0.4 | 2.2 | 16.0 |
| Noah Clowney | 98% | 21.4<br><sub>17,21,8,19,35</sub> | 8.4<br><sub>7,3,2,16,15</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,10,0,3,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>1,0,0,0,3</sub> |  | 1.1<br><sub>1,1,0,2,3</sub> |  | 0.5 | 0.6 | 1.0 | 13.6 |
| Moritz Wagner | 96% | 17.0<br><sub>20,16,16,19,18</sub> | 9.3<br><sub>6,9,12,16,10</sub> |  | 4.0<br><sub>1,2,3,3,6</sub> |  | 1.3<br><sub>0,0,1,4,4</sub> |  | 0.8<br><sub>0,1,1,2,2</sub> |  | 0.5 | 0.3 | 0.9 | 14.7 |
| Keon Ellis | 88% | 14.8<br><sub>10,-,22,26,7</sub> | 3.6<br><sub>1,-,3,11,0</sub> |  | 1.6<br><sub>2,-,1,4,0</sub> |  | 1.1<br><sub>0,-,4,3,1</sub> |  | 0.4<br><sub>0,-,1,2,0</sub> |  | 0.8 | 0.4 | 0.5 | 6.3 |
| Chaney Johnson | 97% | 13.1<br><sub>9,8,15,15,12</sub> | 3.7<br><sub>0,5,2,4,1</sub> |  | 2.2<br><sub>2,2,0,3,5</sub> |  | 0.8<br><sub>1,1,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 6.6 |
| Terance Mann | 80% | 12.6<br><sub>16,13,22,18,9</sub> | 3.0<br><sub>0,0,0,6,2</sub> |  | 1.5<br><sub>2,2,1,1,1</sub> |  | 1.2<br><sub>2,0,1,3,1</sub> |  | 0.2<br><sub>0,0,0,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.7 |
| Josh Minott | 67% | 7.8<br><sub>6,-,12,7,2</sub> | 4.2<br><sub>0,-,10,0,0</sub> |  | 1.5<br><sub>1,-,2,2,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.4<br><sub>0,-,2,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.1 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. (BKN) | 76% | 31.9<br><sub>38,36,29,28,-</sub> | 20.1<br><sub>26,25,19,22,-</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>10,9,9,6,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>0,1,0,3,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>4,3,4,4,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.4 | 2.0 | 29.0 |
| Julius Randle (BKN) | 98% | 31.5<br><sub>31,34,30,29,31</sub> | 18.4<br><sub>22,19,13,17,22</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>3,7,4,4,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,8,4,5,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 3.1 | 29.3 |
| Day'Ron Sharpe (BKN) | 98% | 24.1<br><sub>27,32,20,19,28</sub> | 10.2<br><sub>6,12,6,15,16</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 8.0<br><sub>5,10,4,4,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>8,13,6,5,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.9 | 1.9 | 22.4 |
| Egor Demin (BKN) | 98% | 23.1<br><sub>-,-,-,23,27</sub> | 9.6<br><sub>-,-,-,22,11</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>-,-,-,1,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>-,-,-,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>-,-,-,4,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.3 | 1.4 | 15.2 |
| Danny Wolf (BKN) | 76% | 23.1<br><sub>19,31,36,29,28</sub> | 9.8<br><sub>12,11,10,10,14</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>5,9,3,11,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>2,2,1,1,4</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.5 | 0.6 | 1.2 | 17.8 |
| Mikel Brown Jr. (BKN) | 97% | 22.0<br><sub>20,25,-,-,20</sub> | 10.8<br><sub>18,18,-,-,6</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,1,-,-,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>4,3,-,-,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>3,3,-,-,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.2 | 1.8 | 16.5 |
| Nolan Traore (BKN) | 98% | 21.6<br><sub>27,23,21,-,20</sub> | 10.7<br><sub>16,19,14,-,11</sub> |  | 2.0<br><sub>4,1,1,-,1</sub> |  | 3.1<br><sub>2,2,2,-,2</sub> |  | 1.2<br><sub>2,2,2,-,0</sub> |  | 0.8 | 0.4 | 2.2 | 15.9 |
| Noah Clowney (BKN) | 98% | 21.5<br><sub>17,21,8,19,35</sub> | 8.4<br><sub>7,3,2,16,15</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>1,10,0,3,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>1,0,0,0,3</sub> |  | 1.1<br><sub>1,1,0,2,3</sub> |  | 0.6 | 0.6 | 1.0 | 13.6 |
| Moritz Wagner (BKN) | 96% | 16.9<br><sub>20,16,16,19,18</sub> | 9.3<br><sub>6,9,12,16,10</sub> |  | 4.0<br><sub>1,2,3,3,6</sub> |  | 1.3<br><sub>0,0,1,4,4</sub> |  | 0.8<br><sub>0,1,1,2,2</sub> |  | 0.5 | 0.3 | 0.9 | 14.7 |
| Keon Ellis (BKN) | 88% | 14.9<br><sub>10,-,22,26,7</sub> | 3.6<br><sub>1,-,3,11,0</sub> |  | 1.6<br><sub>2,-,1,4,0</sub> |  | 1.1<br><sub>0,-,4,3,1</sub> |  | 0.4<br><sub>0,-,1,2,0</sub> |  | 0.8 | 0.4 | 0.5 | 6.3 |
| Chaney Johnson (BKN) | 97% | 13.2<br><sub>9,8,15,15,12</sub> | 3.7<br><sub>0,5,2,4,1</sub> |  | 2.2<br><sub>2,2,0,3,5</sub> |  | 0.8<br><sub>1,1,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 6.6 |
| Terance Mann (BKN) | 80% | 12.6<br><sub>16,13,22,18,9</sub> | 3.0<br><sub>0,0,0,6,2</sub> |  | 1.5<br><sub>2,2,1,1,1</sub> |  | 1.2<br><sub>2,0,1,3,1</sub> |  | 0.2<br><sub>0,0,0,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.7 |
| Josh Minott (BKN) | 67% | 7.7<br><sub>6,-,12,7,2</sub> | 4.2<br><sub>0,-,10,0,0</sub> |  | 1.5<br><sub>1,-,2,2,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.4<br><sub>0,-,2,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.1 |
| Tyrese Maxey (PHI) | 98% | 36.5<br><sub>32,36,34,35,36</sub> | 23.4<br><sub>17,27,24,27,27</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>3,4,1,2,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,7,4,8,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>2,3,3,1,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.5 | 0.5 | 2.2 | 32.8 |
| Jaylen Brown (PHI) | 98% | 34.8<br><sub>34,35,26,36,32</sub> | 22.1<br><sub>20,29,13,18,31</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>5,7,5,6,2</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 3.8<br><sub>5,4,2,2,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>2,2,1,0,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.5 | 3.0 | 31.7 |
| VJ Edgecombe (PHI) | 96% | 33.6<br><sub>32,35,32,36,31</sub> | 12.7<br><sub>19,13,8,15,11</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>3,6,4,8,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>2,3,5,8,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,3,0,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.5 | 1.5 | 22.1 |
| LeBron James (PHI) | 98% | 33.3<br><sub>32,33,29,-,33</sub> | 16.2<br><sub>8,22,11,-,15</sub> |  | 6.4<br><sub>7,5,8,-,7</sub> |  | 6.6<br><sub>3,5,5,-,11</sub> |  | 1.2<br><sub>0,2,1,-,0</sub> |  | 1.2 | 0.6 | 2.7 | 29.3 |
| Joel Embiid (PHI) | 100% | 32.1<br><sub>25,29,31,28,-</sub> | 21.9<br><sub>6,18,16,20,-</sub> | 22.5 · – | 8.2<br><sub>7,10,6,4,-</sub> | 7.5 | 4.2<br><sub>1,5,1,3,-</sub> | 3.5 | 1.0<br><sub>0,0,1,0,-</sub> |  | 0.8 | 1.1 | 2.9 | 34.4 |
| Dean Wade (PHI) | 96% | 24.5<br><sub>21,18,23,34,35</sub> | 4.6<br><sub>0,0,8,6,12</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>5,1,9,5,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,1,0,2,3</sub> |  | 0.6<br><sub>0,0,2,2,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 0.3 | 0.6 | 9.8 |
| Kentavious Caldwell-Pope (PHI) | 98% | 19.7<br><sub>17,21,16,27,22</sub> | 4.7<br><sub>5,6,0,11,9</sub> |  | 2.2<br><sub>2,6,0,4,5</sub> |  | 1.5<br><sub>0,3,2,5,0</sub> |  | 0.6<br><sub>1,2,0,3,2</sub> |  | 0.8 | 0.3 | 0.7 | 8.4 |
| Anfernee Simons (PHI) | 98% | 18.5<br><sub>19,16,18,23,15</sub> | 8.4<br><sub>6,3,17,17,12</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,4,3,3,0</sub> |  | 1.4<br><sub>2,2,0,2,0</sub> |  | 1.5<br><sub>1,1,3,5,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.5 | 0.1 | 0.8 | 11.5 |
| Jabari Walker (PHI) | 88% | 15.2<br><sub>17,19,15,16,25</sub> | 5.8<br><sub>8,9,2,9,11</sub> |  | 4.2<br><sub>5,11,4,8,7</sub> |  | 0.7<br><sub>1,0,0,1,1</sub> |  | 0.5<br><sub>0,1,0,1,3</sub> |  | 0.5 | 0.2 | 0.6 | 10.8 |
| Rayan Rupert (PHI) | 47% | 7.6<br><sub>-,-,6,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 1.5<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 4.8 |
| Tacko Fall (PHI) | 76% | 7.1<br><sub>3,-,-,1,5</sub> | 0.4<br><sub>0,-,-,0,0</sub> |  | 1.6<br><sub>1,-,-,0,3</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.4 | 0.4 | 2.3 |
| Labaron Philon Jr. (PHI) | 72% | 6.8<br><sub>4,-,6,2,6</sub> | 2.7<br><sub>3,-,2,0,3</sub> |  | 1.1<br><sub>1,-,1,0,1</sub> |  | 0.6<br><sub>1,-,3,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Justin Edwards (PHI) | 52% | 6.7<br><sub>4,-,6,1,-</sub> | 2.9<br><sub>3,-,0,0,-</sub> |  | 0.9<br><sub>1,-,0,1,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>1,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Caleb Love (PHI) | 38% | 6.7<br><sub>-,-,-,1,-</sub> | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.0 |

</details>


### HOU @ MIA
Out: Clint Capela (HOU), Marcus Smart (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.2–117.6 | HOU 52% | 1.94 / 2.07 | MIA +1.5 | 235.5 | MIA +2.5 covers 54%; o231.5 59% |
| Expected (weighted by chance each plays) | 118.1–117.9 | HOU 51% | 1.97 / 2.03 | MIA +0.5 | 235.5 | MIA +2.5 covers 56%; o231.5 59% |
| if Pelle Larsson plays | 117.3–119.0 | HOU 45% | 2.20 / 1.83 | MIA -2.5 | 236.5 | MIA +2.5 covers 61%; o231.5 60% |
| if Fred VanVleet plays | 118.6–117.2 | HOU 54% | 1.85 / 2.18 | MIA +1.5 | 235.5 | MIA +2.5 covers 52%; o231.5 59% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julian Phillips (HOU) | Day-To-Day | 70% | 10.8 | 3.3 | 1.3 | 0.6 | 0.3 | 0.5 | 0.2 | 0.4 | 5.2 | small |
| Pelle Larsson (MIA) | Questionable | 55% | 27.5 | 10.8 | 3.3 | 3.0 | 1.0 | 0.9 | 0.2 | 1.6 | 17.1 | full tables below |
| Fred VanVleet (HOU) | Day-To-Day | 70% | 34.2 | 14.2 | 3.6 | 5.3 | 2.6 | 1.4 | 0.4 | 1.6 | 23.1 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.6<br><sub>39,35,29,41,29</sub> | 18.2<br><sub>17,8,19,12,26</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>7,9,7,10,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>0,3,4,3,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.5<br><sub>0,0,0,0,3</sub> |  | 1.6 | 0.7 | 2.4 | 31.2 |
| Kevin Durant | 98% | 37.1<br><sub>38,36,34,33,30</sub> | 24.9<br><sub>21,23,20,22,25</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>10,12,4,3,4</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 5.4<br><sub>3,8,5,6,5</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.9 | 3.5 | 36.5 |
| Alperen Sengun | 91% | 37.0<br><sub>32,35,37,37,28</sub> | 23.5<br><sub>15,20,19,43,19</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>6,12,13,12,8</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>5,8,9,5,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.3 | 1.1 | 3.3 | 40.8 |
| Jabari Smith Jr. | 98% | 36.6<br><sub>39,38,35,24,28</sub> | 16.5<br><sub>15,14,14,6,9</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>9,7,8,3,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,3,0,0,5</sub> |  | 2.5<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.9 | 1.4 | 26.2 |
| Tari Eason | 98% | 30.5<br><sub>23,19,22,33,30</sub> | 12.2<br><sub>2,12,6,14,25</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>7,5,3,11,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>2,2,0,2,1</sub> |  | 1.5<br><sub>0,2,0,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.8 | 1.4 | 21.2 |
| Reed Sheppard | 91% | 28.6<br><sub>13,17,20,19,26</sub> | 13.2<br><sub>6,8,13,0,11</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>0,0,1,0,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 4.0<br><sub>0,0,1,3,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.7 | 1.4 | 20.0 |
| Bogdan Bogdanovic | 97% | 19.9<br><sub>2,12,10,12,22</sub> | 7.5<br><sub>0,8,0,11,12</sub> |  | 2.4<br><sub>1,3,0,1,3</sub> |  | 2.1<br><sub>0,1,0,3,4</sub> |  | 1.2<br><sub>0,2,0,3,2</sub> |  | 0.5 | 0.2 | 0.8 | 12.0 |
| Steven Adams | 43% | 16.2<br><sub>-,-,-,-,12</sub> | 4.1<br><sub>-,-,-,-,6</sub> |  | 6.3<br><sub>-,-,-,-,7</sub> |  | 1.0<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.5 | 0.9 | 11.3 |
| Oscar Tshiebwe | 93% | 12.5<br><sub>3,-,1,6,12</sub> | 4.6<br><sub>2,-,0,0,4</sub> |  | 5.5<br><sub>0,-,0,5,9</sub> |  | 0.8<br><sub>0,-,0,0,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 10.9 |
| Bruce Thornton | 63% | 10.9<br><sub>-,1,3,-,6</sub> | 3.4<br><sub>-,0,0,-,2</sub> |  | 1.8<br><sub>-,0,0,-,0</sub> |  | 0.7<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.1 | 0.6 | 5.8 |
| Jae'Sean Tate | 58% | 10.2<br><sub>-,-,1,-,8</sub> | 2.9<br><sub>-,-,0,-,4</sub> |  | 2.4<br><sub>-,-,0,-,2</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.0 |
| Isaiah Crawford | 63% | 9.9<br><sub>-,1,1,-,9</sub> | 2.9<br><sub>-,0,0,-,4</sub> |  | 1.6<br><sub>-,0,0,-,2</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.3 | 5.0 |
| Quadir Copeland | 3% | 9.1 | 3.6 |  | 1.7 |  | 0.8 |  | 0.3 |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 37.5<br><sub>38,40,38,39,32</sub> | 15.5<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.4<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.3 | 2.2 | 26.9 |
| Bam Adebayo | 98% | 36.9<br><sub>33,34,37,38,36</sub> | 20.2<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 10.1<br><sub>10,8,8,14,5</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.7<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,1,0,2,1</sub> |  | 1.7 | 0.8 | 1.8 | 34.0 |
| Giannis Antetokounmpo | 98% | 34.9<br><sub>31,34,31,31,31</sub> | 28.8<br><sub>20,29,30,37,34</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 12.0<br><sub>14,14,11,9,14</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>4,3,4,2,8</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.1 | 3.4 | 46.4 |
| Andrew Wiggins | 98% | 27.8<br><sub>21,32,19,32,23</sub> | 10.4<br><sub>2,6,13,8,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.8 | 1.1 | 15.6 |
| Klay Thompson | 83% | 27.0<br><sub>23,32,30,-,20</sub> | 13.3<br><sub>11,23,11,-,26</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>0,2,1,-,1</sub> |  | 1.8<br><sub>3,4,2,-,4</sub> |  | 2.7<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.6 | 1.1 | 17.1 |
| Ryan Conwell | 91% | 23.8<br><sub>30,19,21,33,26</sub> | 8.3<br><sub>13,6,5,20,9</sub> |  | 2.6<br><sub>1,2,4,5,4</sub> |  | 1.7<br><sub>2,2,2,2,1</sub> |  | 1.4<br><sub>3,2,1,4,2</sub> |  | 0.8 | 0.1 | 0.9 | 12.6 |
| Bobby Portis | 98% | 20.2<br><sub>14,20,17,15,18</sub> | 8.0<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,1,1,2,2</sub> |  | 1.1<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.6 | 0.3 | 0.7 | 14.3 |
| Myron Gardner | 67% | 16.7<br><sub>1,-,10,19,26</sub> | 4.6<br><sub>0,-,4,0,5</sub> |  | 4.3<br><sub>0,-,3,4,9</sub> |  | 1.6<br><sub>0,-,1,2,3</sub> |  | 0.5<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.4 | 0.7 | 10.5 |
| Tim Hardaway Jr. | 64% | 15.9<br><sub>4,7,-,20,-</sub> | 6.0<br><sub>0,0,-,4,-</sub> |  | 1.6<br><sub>0,0,-,3,-</sub> |  | 0.7<br><sub>1,0,-,2,-</sub> |  | 0.8<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 8.3 |
| Nikola Jovic | 52% | 12.6<br><sub>12,-,-,-,11</sub> | 4.0<br><sub>1,-,-,-,2</sub> |  | 2.2<br><sub>0,-,-,-,1</sub> |  | 1.1<br><sub>1,-,-,-,2</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.3 |
| Simone Fontecchio | 64% | 11.8<br><sub>-,-,7,7,14</sub> | 5.1<br><sub>-,-,3,0,7</sub> |  | 2.0<br><sub>-,-,0,0,5</sub> |  | 0.8<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 7.9 |
| Dru Smith | 52% | 11.2<br><sub>1,-,-,6,-</sub> | 3.4<br><sub>0,-,-,0,-</sub> |  | 1.5<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,1,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.8 | 0.2 | 0.6 | 6.5 |
| Keshad Johnson | 52% | 7.8<br><sub>-,-,-,-,1</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.0 |
| Nick Richards | 38% | 7.2<br><sub>1,-,-,-,-</sub> | 2.4<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.1 |
| Tre Donaldson | 58% | 7.0<br><sub>-,-,-,-,1</sub> | 6.0<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 3.7 | 6.7 |

</details>

<details><summary>if Fred VanVleet plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant (HOU) | 98% | 36.2<br><sub>38,36,34,33,30</sub> | 23.2<br><sub>21,23,20,22,25</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>10,12,4,3,4</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 4.9<br><sub>3,8,5,6,5</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.9 | 3.2 | 34.2 |
| Amen Thompson (HOU) | 98% | 36.2<br><sub>39,35,29,41,29</sub> | 16.5<br><sub>17,8,19,12,26</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>7,9,7,10,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>0,3,4,3,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.3<br><sub>0,0,0,0,3</sub> |  | 1.5 | 0.8 | 2.2 | 28.5 |
| Alperen Sengun (HOU) | 91% | 36.1<br><sub>32,35,37,37,28</sub> | 21.6<br><sub>15,20,19,43,19</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>6,12,13,12,8</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>5,8,9,5,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.2 | 1.0 | 2.9 | 38.7 |
| Jabari Smith Jr. (HOU) | 98% | 35.6<br><sub>39,38,35,24,28</sub> | 15.6<br><sub>15,14,14,6,9</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>9,7,8,3,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,3,0,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.7 | 0.9 | 1.3 | 24.9 |
| Fred VanVleet (HOU) | 100% | 34.2<br><sub>31,30,30,34,-</sub> | 14.2<br><sub>16,12,18,17,-</sub> | 12.5 · – | 3.6<br><sub>3,1,2,2,-</sub> | 3.5 | 5.3<br><sub>4,2,6,3,-</sub> | 4.5 | 2.6<br><sub>4,3,4,3,-</sub> | 2.5 | 1.4 | 0.4 | 1.6 | 23.1 |
| Tari Eason (HOU) | 98% | 27.4<br><sub>23,19,22,33,30</sub> | 10.8<br><sub>2,12,6,14,25</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>7,5,3,11,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,2,0,2,1</sub> |  | 1.3<br><sub>0,2,0,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.7 | 1.2 | 19.0 |
| Reed Sheppard (HOU) | 91% | 23.1<br><sub>13,17,20,19,26</sub> | 10.8<br><sub>6,8,13,0,11</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,0,1,0,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>0,0,1,3,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.5 | 1.1 | 15.9 |
| Bogdan Bogdanovic (HOU) | 97% | 14.9<br><sub>2,12,10,12,22</sub> | 5.9<br><sub>0,8,0,11,12</sub> |  | 1.8<br><sub>1,3,0,1,3</sub> |  | 1.5<br><sub>0,1,0,3,4</sub> |  | 0.9<br><sub>0,2,0,3,2</sub> |  | 0.4 | 0.1 | 0.6 | 9.1 |
| Steven Adams (HOU) | 43% | 13.4<br><sub>-,-,-,-,12</sub> | 3.5<br><sub>-,-,-,-,6</sub> |  | 5.2<br><sub>-,-,-,-,7</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 9.5 |
| Oscar Tshiebwe (HOU) | 93% | 9.1<br><sub>3,-,1,6,12</sub> | 3.4<br><sub>2,-,0,0,4</sub> |  | 4.0<br><sub>0,-,0,5,9</sub> |  | 0.6<br><sub>0,-,0,0,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 8.1 |
| Quadir Copeland (HOU) | 3% | 8.4 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford (HOU) | 63% | 6.6<br><sub>-,1,1,-,9</sub> | 2.1<br><sub>-,0,0,-,4</sub> |  | 1.1<br><sub>-,0,0,-,2</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.2 | 3.6 |
| Jae'Sean Tate (HOU) | 58% | 6.5<br><sub>-,-,1,-,8</sub> | 2.0<br><sub>-,-,0,-,4</sub> |  | 1.6<br><sub>-,-,0,-,2</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Bruce Thornton (HOU) | 63% | 6.1<br><sub>-,1,3,-,6</sub> | 2.1<br><sub>-,0,0,-,2</sub> |  | 1.0<br><sub>-,0,0,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 3.5 |
| Davion Mitchell (MIA) | 98% | 37.5<br><sub>38,40,38,39,32</sub> | 15.4<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.4<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.3 | 2.2 | 26.8 |
| Bam Adebayo (MIA) | 98% | 36.9<br><sub>33,34,37,38,36</sub> | 20.2<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 10.1<br><sub>10,8,8,14,5</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.8<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,1,0,2,1</sub> |  | 1.7 | 0.8 | 1.8 | 34.0 |
| Giannis Antetokounmpo (MIA) | 98% | 34.9<br><sub>31,34,31,31,31</sub> | 28.9<br><sub>20,29,30,37,34</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 12.0<br><sub>14,14,11,9,14</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>4,3,4,2,8</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.0 | 3.4 | 46.6 |
| Andrew Wiggins (MIA) | 98% | 27.8<br><sub>21,32,19,32,23</sub> | 10.4<br><sub>2,6,13,8,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.8 | 1.1 | 15.7 |
| Klay Thompson (MIA) | 83% | 27.1<br><sub>23,32,30,-,20</sub> | 13.2<br><sub>11,23,11,-,26</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>0,2,1,-,1</sub> |  | 1.8<br><sub>3,4,2,-,4</sub> |  | 2.7<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.6 | 1.1 | 17.0 |
| Ryan Conwell (MIA) | 91% | 23.8<br><sub>30,19,21,33,26</sub> | 8.3<br><sub>13,6,5,20,9</sub> |  | 2.6<br><sub>1,2,4,5,4</sub> |  | 1.7<br><sub>2,2,2,2,1</sub> |  | 1.4<br><sub>3,2,1,4,2</sub> |  | 0.8 | 0.1 | 0.9 | 12.6 |
| Bobby Portis (MIA) | 98% | 20.1<br><sub>14,20,17,15,18</sub> | 8.0<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,1,1,2,2</sub> |  | 1.1<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.6 | 0.3 | 0.7 | 14.3 |
| Myron Gardner (MIA) | 67% | 16.6<br><sub>1,-,10,19,26</sub> | 4.6<br><sub>0,-,4,0,5</sub> |  | 4.3<br><sub>0,-,3,4,9</sub> |  | 1.6<br><sub>0,-,1,2,3</sub> |  | 0.5<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.4 | 0.7 | 10.4 |
| Tim Hardaway Jr. (MIA) | 64% | 15.9<br><sub>4,7,-,20,-</sub> | 6.0<br><sub>0,0,-,4,-</sub> |  | 1.5<br><sub>0,0,-,3,-</sub> |  | 0.8<br><sub>1,0,-,2,-</sub> |  | 0.9<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 8.3 |
| Nikola Jovic (MIA) | 52% | 12.6<br><sub>12,-,-,-,11</sub> | 3.9<br><sub>1,-,-,-,2</sub> |  | 2.2<br><sub>0,-,-,-,1</sub> |  | 1.1<br><sub>1,-,-,-,2</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 7.2 |
| Simone Fontecchio (MIA) | 64% | 11.6<br><sub>-,-,7,7,14</sub> | 5.0<br><sub>-,-,3,0,7</sub> |  | 1.9<br><sub>-,-,0,0,5</sub> |  | 0.8<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 7.7 |
| Dru Smith (MIA) | 52% | 11.3<br><sub>1,-,-,6,-</sub> | 3.4<br><sub>0,-,-,0,-</sub> |  | 1.5<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,1,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.8 | 0.2 | 0.6 | 6.5 |
| Keshad Johnson (MIA) | 52% | 7.8<br><sub>-,-,-,-,1</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.0 |
| Nick Richards (MIA) | 38% | 7.2<br><sub>1,-,-,-,-</sub> | 2.4<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.1 |
| Tre Donaldson (MIA) | 58% | 7.0<br><sub>-,-,-,-,1</sub> | 6.0<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 3.7 | 6.7 |

</details>

<details><summary>if Pelle Larsson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 37.5<br><sub>39,35,29,41,29</sub> | 18.2<br><sub>17,8,19,12,26</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>7,9,7,10,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>0,3,4,3,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.5<br><sub>0,0,0,0,3</sub> |  | 1.6 | 0.7 | 2.4 | 31.1 |
| Kevin Durant (HOU) | 98% | 37.1<br><sub>38,36,34,33,30</sub> | 24.9<br><sub>21,23,20,22,25</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>10,12,4,3,4</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 5.5<br><sub>3,8,5,6,5</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.9 | 3.5 | 36.6 |
| Alperen Sengun (HOU) | 91% | 37.0<br><sub>32,35,37,37,28</sub> | 23.5<br><sub>15,20,19,43,19</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>6,12,13,12,8</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>5,8,9,5,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.3 | 1.1 | 3.2 | 40.8 |
| Jabari Smith Jr. (HOU) | 98% | 36.6<br><sub>39,38,35,24,28</sub> | 16.4<br><sub>15,14,14,6,9</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>9,7,8,3,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,3,0,0,5</sub> |  | 2.5<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.9 | 1.4 | 26.1 |
| Tari Eason (HOU) | 98% | 30.6<br><sub>23,19,22,33,30</sub> | 12.2<br><sub>2,12,6,14,25</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>7,5,3,11,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,2,0,2,1</sub> |  | 1.5<br><sub>0,2,0,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.8 | 1.4 | 21.3 |
| Reed Sheppard (HOU) | 91% | 28.5<br><sub>13,17,20,19,26</sub> | 13.2<br><sub>6,8,13,0,11</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>0,0,1,0,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 4.0<br><sub>0,0,1,3,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.7 | 1.4 | 19.9 |
| Bogdan Bogdanovic (HOU) | 97% | 20.0<br><sub>2,12,10,12,22</sub> | 7.5<br><sub>0,8,0,11,12</sub> |  | 2.4<br><sub>1,3,0,1,3</sub> |  | 2.1<br><sub>0,1,0,3,4</sub> |  | 1.2<br><sub>0,2,0,3,2</sub> |  | 0.5 | 0.2 | 0.8 | 12.0 |
| Steven Adams (HOU) | 43% | 16.2<br><sub>-,-,-,-,12</sub> | 4.0<br><sub>-,-,-,-,6</sub> |  | 6.2<br><sub>-,-,-,-,7</sub> |  | 1.0<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.5 | 0.9 | 11.3 |
| Oscar Tshiebwe (HOU) | 93% | 12.5<br><sub>3,-,1,6,12</sub> | 4.5<br><sub>2,-,0,0,4</sub> |  | 5.5<br><sub>0,-,0,5,9</sub> |  | 0.8<br><sub>0,-,0,0,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 10.9 |
| Bruce Thornton (HOU) | 63% | 10.9<br><sub>-,1,3,-,6</sub> | 3.3<br><sub>-,0,0,-,2</sub> |  | 1.8<br><sub>-,0,0,-,0</sub> |  | 0.7<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.1 | 0.6 | 5.8 |
| Jae'Sean Tate (HOU) | 58% | 10.1<br><sub>-,-,1,-,8</sub> | 2.9<br><sub>-,-,0,-,4</sub> |  | 2.4<br><sub>-,-,0,-,2</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.9 |
| Isaiah Crawford (HOU) | 63% | 9.9<br><sub>-,1,1,-,9</sub> | 2.9<br><sub>-,0,0,-,4</sub> |  | 1.6<br><sub>-,0,0,-,2</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.3 | 5.0 |
| Quadir Copeland (HOU) | 3% | 8.7 | 3.5 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Davion Mitchell (MIA) | 98% | 35.8<br><sub>38,40,38,39,32</sub> | 14.4<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.2<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.3 | 2.0 | 25.4 |
| Bam Adebayo (MIA) | 98% | 35.6<br><sub>33,34,37,38,36</sub> | 19.9<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 9.7<br><sub>10,8,8,14,5</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,1,0,2,1</sub> |  | 1.7 | 0.8 | 1.7 | 33.2 |
| Giannis Antetokounmpo (MIA) | 98% | 34.3<br><sub>31,34,31,31,31</sub> | 28.9<br><sub>20,29,30,37,34</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 12.0<br><sub>14,14,11,9,14</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>4,3,4,2,8</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.0 | 3.4 | 46.4 |
| Pelle Larsson (MIA) | 100% | 27.5<br><sub>29,22,31,-,-</sub> | 10.8<br><sub>13,11,14,-,-</sub> | 10.5 · – | 3.3<br><sub>1,3,7,-,-</sub> | 3.5 | 3.0<br><sub>4,3,2,-,-</sub> | 3.5 | 1.0<br><sub>3,3,2,-,-</sub> | 1.5 | 0.9 | 0.2 | 1.6 | 17.1 |
| Andrew Wiggins (MIA) | 98% | 24.8<br><sub>21,32,19,32,23</sub> | 9.4<br><sub>2,6,13,8,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.7<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.7 | 1.1 | 14.2 |
| Klay Thompson (MIA) | 83% | 22.7<br><sub>23,32,30,-,20</sub> | 11.3<br><sub>11,23,11,-,26</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>0,2,1,-,1</sub> |  | 1.6<br><sub>3,4,2,-,4</sub> |  | 2.2<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.4 | 1.0 | 14.6 |
| Ryan Conwell (MIA) | 91% | 18.8<br><sub>30,19,21,33,26</sub> | 6.8<br><sub>13,6,5,20,9</sub> |  | 2.1<br><sub>1,2,4,5,4</sub> |  | 1.4<br><sub>2,2,2,2,1</sub> |  | 1.0<br><sub>3,2,1,4,2</sub> |  | 0.6 | 0.1 | 0.8 | 10.3 |
| Bobby Portis (MIA) | 98% | 17.6<br><sub>14,20,17,15,18</sub> | 7.1<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>0,1,1,2,2</sub> |  | 0.9<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.5 | 0.2 | 0.6 | 12.7 |
| Myron Gardner (MIA) | 67% | 11.9<br><sub>1,-,10,19,26</sub> | 3.4<br><sub>0,-,4,0,5</sub> |  | 3.2<br><sub>0,-,3,4,9</sub> |  | 1.2<br><sub>0,-,1,2,3</sub> |  | 0.3<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.3 | 0.5 | 7.8 |
| Tim Hardaway Jr. (MIA) | 64% | 10.1<br><sub>4,7,-,20,-</sub> | 4.0<br><sub>0,0,-,4,-</sub> |  | 1.0<br><sub>0,0,-,3,-</sub> |  | 0.5<br><sub>1,0,-,2,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Nikola Jovic (MIA) | 52% | 9.9<br><sub>12,-,-,-,11</sub> | 3.2<br><sub>1,-,-,-,2</sub> |  | 1.7<br><sub>0,-,-,-,1</sub> |  | 0.9<br><sub>1,-,-,-,2</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.8 |
| Simone Fontecchio (MIA) | 64% | 9.5<br><sub>-,-,7,7,14</sub> | 4.3<br><sub>-,-,3,0,7</sub> |  | 1.6<br><sub>-,-,0,0,5</sub> |  | 0.7<br><sub>-,-,0,2,0</sub> |  | 0.5<br><sub>-,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 6.6 |
| Dru Smith (MIA) | 52% | 7.3<br><sub>1,-,-,6,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.4 |
| Keshad Johnson (MIA) | 52% | 6.5<br><sub>-,-,-,-,1</sub> | 2.8<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Tre Donaldson (MIA) | 58% | 5.7<br><sub>-,-,-,-,1</sub> | 6.0<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 3.2 | 6.6 |
| Nick Richards (MIA) | 38% | 5.7<br><sub>1,-,-,-,-</sub> | 2.2<br><sub>0,-,-,-,-</sub> |  | 2.0<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.5 |

</details>


### POR @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.2<br><sub>39,24,34,35,35</sub> | 23.7<br><sub>22,15,24,28,34</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>9,4,6,3,6</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.1<br><sub>11,1,8,6,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,2,2,4,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.6 | 3.7 | 36.3 |
| Toumani Camara | 98% | 32.3<br><sub>30,21,30,38,36</sub> | 11.9<br><sub>18,4,12,14,14</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>6,4,3,5,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,0,3,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>4,0,2,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.5 | 1.4 | 18.1 |
| Damian Lillard | 98% | 31.9<br><sub>37,20,24,32,33</sub> | 19.6<br><sub>22,12,25,18,29</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>0,0,3,3,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>4,7,3,3,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.7<br><sub>4,2,4,2,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.2 | 2.5 | 28.2 |
| Jrue Holiday | 98% | 28.7<br><sub>31,20,25,30,27</sub> | 13.5<br><sub>12,11,11,19,6</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,0,1,3,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,0,2,5,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>3,1,2,5,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 2.4 | 22.1 |
| Donovan Clingan | 98% | 26.4<br><sub>28,22,26,30,27</sub> | 10.8<br><sub>17,6,7,5,13</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>11,5,13,12,11</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>1,0,3,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>3,0,1,1,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.6 | 1.9 | 1.4 | 22.9 |
| Scoot Henderson | 98% | 25.2<br><sub>23,24,23,19,23</sub> | 11.3<br><sub>2,13,11,5,11</sub> |  | 2.5<br><sub>2,2,1,2,0</sub> |  | 2.7<br><sub>0,1,4,2,1</sub> |  | 1.3<br><sub>0,0,3,1,2</sub> |  | 0.9 | 0.2 | 2.2 | 16.5 |
| Sidy Cissoko | 98% | 25.0<br><sub>22,16,33,29,26</sub> | 7.1<br><sub>7,4,17,19,3</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,3,3,2,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>3,1,3,0,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.1 | 12.4 |
| Robert Williams III | 98% | 17.1<br><sub>16,-,15,17,17</sub> | 6.3<br><sub>9,-,6,10,2</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>5,-,4,7,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.0<br><sub>2,-,0,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.3 | 0.8 | 13.8 |
| Jayson Kent | 63% | 12.3<br><sub>-,12,-,-,11</sub> | 4.0<br><sub>-,4,-,-,3</sub> |  | 1.6<br><sub>-,1,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.5 | 0.2 | 0.7 | 6.1 |
| Branden Carlson | 76% | 9.6<br><sub>-,12,8,10,8</sub> | 2.8<br><sub>-,4,2,0,5</sub> |  | 2.4<br><sub>-,2,5,2,3</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 0.2<br><sub>-,0,0,0,1</sub> |  | 0.2 | 0.6 | 0.5 | 5.6 |
| Micah Potter | 52% | 8.4<br><sub>-,14,5,-,-</sub> | 3.6<br><sub>-,7,0,-,-</sub> |  | 2.3<br><sub>-,3,3,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.3 |
| Yang Hansen | 52% | 8.0<br><sub>3,26,5,-,-</sub> | 3.1<br><sub>2,12,0,-,-</sub> |  | 2.1<br><sub>0,10,1,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.1 | 0.2 | 0.6 | 5.6 |
| John Tonje | 36% | 6.8<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.4 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 35.2<br><sub>37,40,33,25,37</sub> | 16.8<br><sub>14,23,16,16,18</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>8,6,6,9,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,5,3,3,6</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,2,2,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3 | 1.0 | 2.1 | 25.8 |
| Ayo Dosunmu | 98% | 33.4<br><sub>34,39,30,27,33</sub> | 18.7<br><sub>21,26,26,18,24</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>1,2,4,2,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.7<br><sub>6,4,1,1,0</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>0,4,4,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 2.3 | 26.8 |
| Jonathan Kuminga | 98% | 31.7<br><sub>32,34,25,24,35</sub> | 14.1<br><sub>16,17,4,14,11</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>8,8,0,8,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>5,4,0,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>4,1,0,1,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.6 | 1.7 | 22.2 |
| LaMelo Ball | 98% | 30.6<br><sub>31,35,30,25,30</sub> | 21.0<br><sub>20,22,24,22,19</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>2,2,3,3,8</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.2<br><sub>6,8,5,9,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.5<br><sub>4,3,4,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.7 | 0.2 | 3.3 | 31.5 |
| Rudy Gobert | 98% | 29.9<br><sub>33,25,31,23,27</sub> | 9.9<br><sub>8,8,10,9,1</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 10.8<br><sub>11,11,15,6,10</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>2,0,2,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.4 | 1.4 | 22.5 |
| Terrence Shannon Jr. | 98% | 22.4<br><sub>-,-,18,21,22</sub> | 10.8<br><sub>-,-,5,6,14</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>-,-,3,2,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>-,-,3,4,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 1.2 | 15.4 |
| Trey Lyles | 98% | 19.6<br><sub>20,29,21,15,19</sub> | 6.0<br><sub>5,5,9,2,5</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>2,13,6,0,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>0,2,2,0,2</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 11.1 |
| Bones Hyland | 98% | 18.1<br><sub>16,10,13,23,21</sub> | 10.0<br><sub>19,4,14,24,12</sub> |  | 1.9<br><sub>2,1,2,3,1</sub> |  | 2.8<br><sub>4,0,2,8,2</sub> |  | 1.4<br><sub>4,1,1,5,3</sub> |  | 0.8 | 0.3 | 1.3 | 14.7 |
| Joan Beringer | 98% | 14.7<br><sub>13,7,16,22,13</sub> | 6.0<br><sub>4,2,4,13,2</sub> |  | 5.1<br><sub>7,3,3,9,5</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 11.6 |
| Zyon Pullin | 35% | 7.2<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Rocco Zikarsky | 38% | 7.1<br><sub>-,-,2,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.2<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.1 |
| Cody Williams | 52% | 6.3<br><sub>-,-,2,7,-</sub> | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.5 |
| Isaiah Evans | 52% | 5.8<br><sub>-,-,2,8,-</sub> | 6.0<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 7.5 |
| Johni Broome | 5% | 5.6 | 2.1 |  | 1.3 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.8 |

</details>


### GSW @ NOP
Out: Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.8–112.5 | GSW 70% | 1.44 / 3.30 | NOP +7.5 | 232.5 | NOP +3.5 covers 39%; o223.5 68% |
| Expected (weighted by chance each plays) | 120.4–113.7 | GSW 68% | 1.47 / 3.11 | NOP +6.5 | 234.5 | NOP +3.5 covers 41%; o223.5 73% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 19.4 | 8.5 | 3.9 | 2.2 | 0.8 | 0.8 | 0.4 | 1.3 | 14.6 | small |
| Jaron Pierre Jr. (NOP) | Questionable | 55% | 16.6 | 7.1 | 2.4 | 1.0 | 0.9 | 0.6 | 0.3 | 1.1 | 10.5 | small |
| Malik Dia (NOP) | Questionable | 55% | 8.1 | 2.8 | 0.3 | 1.1 | 0.3 | 0.4 | 0.2 | 0.4 | 4.2 | small |
| Julian Reese (NOP) | Questionable | 55% | 9.8 | 3.2 | 1.8 | 0.7 | 0.1 | 0.3 | 0.5 | 0.6 | 5.7 | small |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 96% | 33.9<br><sub>32,39,26,37,22</sub> | 20.8<br><sub>9,15,25,22,8</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>6,7,2,6,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>3,1,4,4,0</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,4,5,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.3 | 1.9 | 31.0 |
| Yaxel Lendeborg | 98% | 33.8<br><sub>30,37,27,36,24</sub> | 23.5<br><sub>17,23,23,25,3</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>8,8,7,10,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>6,3,4,0,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,2,4,2,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.9 | 3.5 | 35.3 |
| Draymond Green | 96% | 28.7<br><sub>27,34,21,27,16</sub> | 6.8<br><sub>2,2,2,7,4</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>5,6,3,5,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 7.2<br><sub>11,13,6,7,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.8 | 2.7 | 19.7 |
| De'Anthony Melton | 98% | 25.8<br><sub>17,17,26,25,18</sub> | 14.7<br><sub>5,4,16,11,8</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>6,1,4,4,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.2<br><sub>2,1,3,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>0,1,4,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.6 | 0.5 | 1.8 | 21.9 |
| Will Richard | 98% | 25.4<br><sub>16,12,-,19,30</sub> | 7.9<br><sub>10,4,-,9,7</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>0,2,-,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,1,-,0,1</sub> |  | 1.0<br><sub>2,0,-,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.3 | 1.0 | 12.8 |
| Georges Niang | 98% | 22.2<br><sub>22,25,19,19,15</sub> | 9.7<br><sub>13,11,9,5,5</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,2,2,5,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>3,1,2,0,2</sub> |  | 1.6<br><sub>2,3,1,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5 | 0.2 | 1.0 | 14.6 |
| Al Horford | 98% | 19.4<br><sub>18,13,15,21,10</sub> | 7.3<br><sub>8,2,5,2,0</sub> |  | 4.3<br><sub>5,5,2,1,3</sub> |  | 2.4<br><sub>1,4,6,4,1</sub> |  | 1.0<br><sub>2,0,1,0,0</sub> |  | 0.6 | 0.9 | 0.7 | 14.0 |
| LJ Cryer | 76% | 18.6<br><sub>1,-,20,18,24</sub> | 9.7<br><sub>0,-,10,13,20</sub> |  | 1.6<br><sub>0,-,0,1,2</sub> |  | 2.0<br><sub>0,-,3,1,6</sub> |  | 1.7<br><sub>0,-,2,3,6</sub> |  | 0.5 | 0.1 | 0.9 | 13.2 |
| Gary Payton II | 83% | 17.5<br><sub>10,13,-,-,13</sub> | 8.6<br><sub>9,4,-,-,2</sub> |  | 3.2<br><sub>0,0,-,-,2</sub> |  | 1.5<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 1.1 | 0.2 | 0.8 | 13.2 |
| Charles Bassey | 98% | 17.2<br><sub>14,11,18,13,20</sub> | 8.9<br><sub>8,8,12,7,11</sub> |  | 7.3<br><sub>7,4,10,6,5</sub> |  | 1.0<br><sub>0,0,1,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 1.0 | 17.1 |
| Graham Ike | 91% | 13.1<br><sub>1,-,12,4,13</sub> | 5.8<br><sub>0,-,4,4,5</sub> |  | 3.2<br><sub>1,-,5,0,2</sub> |  | 1.3<br><sub>0,-,2,1,3</sub> |  | 0.4<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.5 | 0.7 | 10.3 |
| Malevy Leons | 64% | 12.3<br><sub>1,-,12,4,14</sub> | 3.8<br><sub>0,-,0,0,5</sub> |  | 2.4<br><sub>0,-,3,3,1</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.5 | 0.6 | 7.0 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 35.3<br><sub>26,24,29,35,41</sub> | 19.8<br><sub>13,9,15,30,16</sub> | 16.5 · –<br><sub>o 53% · u 47%</sub> | 5.7<br><sub>4,0,1,10,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>3,4,2,0,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>1,1,3,6,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 1.7 | 28.8 |
| Zion Williamson | 98% | 35.0<br><sub>31,-,30,33,31</sub> | 23.6<br><sub>25,-,29,22,24</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>2,-,2,4,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.4<br><sub>0,-,1,0,2</sub> |  | 1.4 | 0.7 | 2.9 | 34.2 |
| Jeremiah Fears | 98% | 33.6<br><sub>29,29,28,34,33</sub> | 19.6<br><sub>25,11,14,18,13</sub> | 16.5 · –<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>6,3,4,5,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 6.0<br><sub>5,8,5,7,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>3,1,2,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.6 | 3.1 | 30.5 |
| Herbert Jones | 98% | 28.5<br><sub>20,24,25,32,27</sub> | 9.3<br><sub>4,10,2,8,10</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>0,6,2,2,2</sub> | 3.5<br><sub>o 42% · u 57%</sub> | 2.5<br><sub>1,1,3,3,1</sub> |  | 1.2<br><sub>0,2,0,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.4 | 0.5 | 1.4 | 15.1 |
| Derik Queen | 98% | 27.5<br><sub>21,21,14,23,25</sub> | 14.3<br><sub>8,16,9,10,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>5,4,0,6,5</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 4.0<br><sub>3,0,0,2,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>0,0,1,0,2</sub> |  | 1.3 | 1.0 | 2.9 | 26.0 |
| Jordan Poole | 72% | 24.8<br><sub>-,34,21,21,24</sub> | 12.8<br><sub>-,7,14,13,14</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>-,3,0,2,2</sub> |  | 3.5<br><sub>-,2,1,5,5</sub> |  | 2.0<br><sub>-,1,2,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.4 | 1.9 | 18.8 |
| Yves Missi | 98% | 24.2<br><sub>-,-,-,-,22</sub> | 7.6<br><sub>-,-,-,-,3</sub> | 5.5 · –<br><sub>o 57% · u 43%</sub> | 7.8<br><sub>-,-,-,-,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 1.8 | 1.1 | 17.1 |
| Karlo Matkovic | 97% | 23.8<br><sub>19,17,22,19,14</sub> | 9.4<br><sub>3,4,4,1,5</sub> |  | 5.3<br><sub>3,6,4,3,3</sub> |  | 1.5<br><sub>2,2,1,0,1</sub> |  | 1.1<br><sub>1,0,0,0,1</sub> |  | 0.8 | 0.9 | 1.1 | 16.2 |
| DeAndre Jordan | 48% | 15.7<br><sub>-,-,11,17,-</sub> | 4.3<br><sub>-,-,0,6,-</sub> |  | 6.0<br><sub>-,-,3,8,-</sub> |  | 0.9<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.7 | 0.7 | 11.2 |
| AJ Johnson | 52% | 10.0<br><sub>3,12,7,4,-</sub> | 3.0<br><sub>2,2,2,1,-</sub> |  | 1.4<br><sub>0,2,1,0,-</sub> |  | 1.0<br><sub>0,3,0,0,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 5.4 |

</details>


### PHX @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN), Mark Williams (PHX)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.6–119.7 | PHX 26% | 3.87 / 1.35 | DEN -9.5 | 230.5 | DEN -9.5 covers 49%; o228.5 54% |
| Expected (weighted by chance each plays) | 110.6–119.6 | PHX 26% | 3.88 / 1.35 | DEN -9.5 | 230.5 | DEN -9.5 covers 49%; o228.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Drew Timme (PHX) | Day-To-Day | 70% | 6.8 | 2.6 | 1.2 | 0.7 | 0.2 | 0.2 | 0.1 | 0.4 | 4.5 | small |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 33.7<br><sub>39,29,29,35,28</sub> | 22.5<br><sub>24,32,17,30,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>2,2,3,1,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 5.8<br><sub>3,4,5,7,7</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,3,2,4,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.5 | 31.6 |
| Dillon Brooks | 98% | 29.1<br><sub>37,26,22,30,22</sub> | 15.6<br><sub>11,7,8,15,1</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,4,4,3,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>1,0,2,1,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.9<br><sub>3,1,0,3,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.2 | 1.2 | 20.9 |
| Miles Bridges | 98% | 27.3<br><sub>31,26,18,25,24</sub> | 13.5<br><sub>13,7,8,11,14</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>10,5,4,6,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>7,0,2,3,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.4 | 1.0 | 21.8 |
| Jalen Green | 98% | 25.7<br><sub>34,24,21,21,21</sub> | 12.6<br><sub>16,6,13,12,9</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>3,5,5,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.6<br><sub>6,4,1,0,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>0,0,3,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 1.9 | 18.5 |
| Collin Gillespie | 98% | 24.6<br><sub>20,24,22,27,28</sub> | 9.5<br><sub>7,6,12,13,26</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>3,2,2,2,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.8<br><sub>4,3,8,1,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,2,4,3,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.1 | 1.1 | 16.2 |
| Oso Ighodaro | 98% | 21.5<br><sub>23,18,20,32,17</sub> | 5.9<br><sub>4,7,6,2,4</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>6,4,8,3,2</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>3,2,2,7,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.6 | 1.0 | 13.7 |
| Jordan Goodwin | 98% | 21.2<br><sub>-,-,14,24,31</sub> | 8.4<br><sub>-,-,18,6,14</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>-,-,3,5,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>-,-,1,2,6</sub> |  | 1.3<br><sub>-,-,6,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.2 | 0.8 | 14.7 |
| Luke Kennard | 98% | 19.5<br><sub>14,14,22,21,23</sub> | 8.0<br><sub>11,3,14,8,18</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,1,1,1,6</sub> |  | 1.9<br><sub>2,0,3,1,4</sub> |  | 1.1<br><sub>3,1,3,0,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.6 | 0.1 | 0.7 | 12.0 |
| Ryan Dunn | 98% | 18.0<br><sub>23,23,25,10,24</sub> | 5.2<br><sub>8,3,10,0,3</sub> |  | 3.7<br><sub>5,2,8,4,6</sub> |  | 1.3<br><sub>3,0,2,0,1</sub> |  | 0.6<br><sub>2,1,1,0,1</sub> |  | 0.7 | 0.4 | 0.5 | 10.1 |
| Khaman Maluach | 98% | 15.7<br><sub>18,20,22,16,13</sub> | 5.3<br><sub>8,11,11,4,7</sub> |  | 4.7<br><sub>10,5,7,2,4</sub> |  | 0.7<br><sub>0,2,3,1,0</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.8 | 0.8 | 10.7 |
| Rasheer Fleming | 48% | 8.6<br><sub>-,9,12,-,-</sub> | 3.3<br><sub>-,2,4,-,-</sub> |  | 1.4<br><sub>-,1,2,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,1,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.0 |
| Koa Peat | 63% | 8.2<br><sub>-,6,6,-,8</sub> | 4.5<br><sub>-,4,5,-,10</sub> |  | 1.8<br><sub>-,0,1,-,2</sub> |  | 0.3<br><sub>-,1,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.7 |
| Pat Spencer | 58% | 7.4<br><sub>-,6,-,-,-</sub> | 2.8<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,2,-,-,-</sub> |  | 1.3<br><sub>-,2,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.1 |
| Jamaree Bouyea | 52% | 7.2<br><sub>-,9,8,-,-</sub> | 2.9<br><sub>-,4,7,-,-</sub> |  | 1.0<br><sub>-,0,1,-,-</sub> |  | 1.2<br><sub>-,3,3,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.2 |
| Duop Reath | 52% | 6.7<br><sub>-,6,-,-,-</sub> | 2.9<br><sub>-,2,-,-,-</sub> |  | 1.4<br><sub>-,2,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.6 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.0<br><sub>30,36,39,37,37</sub> | 26.9<br><sub>32,19,25,27,26</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 12.8<br><sub>10,13,16,11,8</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 10.8<br><sub>11,8,9,8,10</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.9 | 3.8 | 50.5 |
| Jamal Murray | 98% | 36.8<br><sub>28,34,39,32,38</sub> | 25.2<br><sub>14,16,38,30,23</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>5,6,2,4,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>7,8,2,8,9</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>2,2,5,4,0</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.6 | 2.5 | 36.8 |
| Christian Braun | 98% | 32.7<br><sub>28,29,32,37,28</sub> | 12.5<br><sub>11,6,4,12,17</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>3,4,5,5,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.4 | 1.1 | 19.6 |
| Cameron Johnson | 98% | 30.4<br><sub>30,29,31,30,31</sub> | 13.0<br><sub>12,18,8,23,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>2,4,2,4,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>2,1,1,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.8<br><sub>4,2,2,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.1 | 19.5 |
| Aaron Gordon | 98% | 30.1<br><sub>25,27,30,27,33</sub> | 13.5<br><sub>17,12,3,9,11</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>1,5,5,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>0,0,2,2,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.4 | 1.3 | 21.8 |
| DeMar DeRozan | 88% | 22.9<br><sub>-,22,19,20,24</sub> | 11.8<br><sub>-,11,7,8,9</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>-,1,4,1,3</sub> |  | 3.1<br><sub>-,5,2,4,2</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.3 | 1.2 | 17.3 |
| Trevon Brazile | 98% | 16.1<br><sub>23,14,14,13,16</sub> | 5.1<br><sub>6,3,5,7,5</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>7,4,2,5,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.7<br><sub>1,2,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 9.8 |
| Spencer Jones | 80% | 13.9<br><sub>-,21,14,22,12</sub> | 3.8<br><sub>-,13,0,3,4</sub> |  | 2.0<br><sub>-,6,0,1,2</sub> |  | 0.7<br><sub>-,0,1,0,1</sub> |  | 0.4<br><sub>-,3,0,1,0</sub> |  | 0.4 | 0.4 | 0.5 | 6.5 |
| Marvin Bagley III | 98% | 13.5<br><sub>14,12,12,12,13</sub> | 6.6<br><sub>10,10,6,4,7</sub> |  | 4.2<br><sub>2,3,3,2,7</sub> |  | 0.7<br><sub>2,0,0,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 11.5 |
| Tyus Jones | 97% | 9.7<br><sub>18,13,6,11,10</sub> | 2.5<br><sub>6,3,2,0,2</sub> |  | 0.9<br><sub>1,4,0,1,0</sub> |  | 1.7<br><sub>8,4,0,4,3</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.2 |
| Bryce Hopkins | 52% | 8.2<br><sub>28,3,3,-,-</sub> | 2.8<br><sub>18,3,2,-,-</sub> |  | 1.2<br><sub>4,1,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.1<br><sub>1,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Zeke Nnaji | 30% | 6.9<br><sub>4,-,-,-,-</sub> | 2.3<br><sub>2,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.1 |
| Alpha Diallo | 52% | 6.1<br><sub>4,-,1,-,-</sub> | 2.5<br><sub>0,-,0,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-16/`._
