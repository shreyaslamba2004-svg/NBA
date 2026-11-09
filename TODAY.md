# NBA model · Sun 08 Nov 2026 (US date)

Updated **Mon 09 Nov, 11:58 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-08/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| MIL to win | BOS @ MIL | betfair_ex_au | 6.89 | 6.09 | 5.30 | 18.9% | 16.4% | 16.4% | +13.2% | +30.0% | 0.6% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| BOS @ MIL | Mon 09 Nov 12:00 | 116.7–104.4 | BOS 81% | 1.23 / 5.30 | MIL +12.5 | 221.5 | MIL +13.5 covers 53%; o222.5 47% |
| NOP @ LAC | Mon 09 Nov 13:00 | 116.2–117.3 | NOP 47% | 2.12 / 1.89 | LAC -1.5 | 233.5 | LAC +1.5 covers 56%; o226.5 65% |
| MIA @ SAC | Mon 09 Nov 13:00 | 125.6–115.6 | MIA 76% | 1.31 / 4.22 | SAC +10.5 | 241.5 | SAC +11.5 covers 54%; o236.5 60% |

### BOS @ MIL
Out: Kam Jones (MIL), Pete Nance (MIL), Cormac Ryan (MIL), Gary Trent Jr. (MIL), Devin Carter (BOS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Rollins PTS over 9.5 (10+) | BOS @ MIL | pointsbetau | 2.05 | 2.00 | 1.65 | 60.5% | 49.1% | 49.9% | +2.4% | +24.0% | 0.6% |
| Tyler Herro PTS under 20.5 | BOS @ MIL | tab | 1.87 | 1.86 | 1.54 | 64.7% | 52.9% | 53.8% | +0.5% | +21.0% | 0.2% |
| Myles Turner PTS over 9.5 (10+) | BOS @ MIL | pointsbetau | 2.05 | 2.05 | 2.10 | 47.7% | 49.0% | 48.9% | +0.2% | -2.2% | 0.1% |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 100% | 32.2<br><sub>35,34,32,-,29</sub> | 24.3<br><sub>26,32,19,-,34</sub> | 26.5 · 26.5<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>7,4,6,-,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>7,7,9,-,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,1,1,-,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.4 | 2.5 | 39.5 |
| Paul George | 100% | 29.8<br><sub>27,33,-,35,22</sub> | 17.4<br><sub>18,17,-,25,8</sub> | 16.5 · 17.5<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,6,-,3,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 3.9<br><sub>8,8,-,5,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>2,3,-,5,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7 | 0.4 | 2.4 | 26.5 |
| Derrick White | 100% | 29.7<br><sub>26,34,30,36,25</sub> | 14.1<br><sub>9,12,7,24,18</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>2,2,2,4,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>4,2,3,7,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,2,1,1,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.8 | 1.5 | 22.7 |
| Payton Pritchard | 98% | 25.2<br><sub>35,27,30,18,23</sub> | 13.6<br><sub>30,7,4,10,12</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,7,3,1,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>3,3,3,5,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>3,0,0,0,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.1 | 1.1 | 21.0 |
| Neemias Queta | 100% | 23.1<br><sub>20,27,26,29,15</sub> | 9.9<br><sub>13,8,16,9,4</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>6,8,6,12,3</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,1,1,3,1</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.1 | 1.0 | 19.1 |
| Sam Hauser | 98% | 20.6<br><sub>18,17,19,30,17</sub> | 7.8<br><sub>6,3,2,11,9</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>3,2,2,2,3</sub> |  | 1.2<br><sub>2,0,1,0,3</sub> |  | 1.5<br><sub>2,1,0,3,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.4 | 0.2 | 0.3 | 12.1 |
| Baylor Scheierman | 98% | 19.8<br><sub>23,20,27,29,15</sub> | 6.3<br><sub>2,10,11,9,5</sub> |  | 3.7<br><sub>3,2,5,11,4</sub> |  | 1.7<br><sub>3,1,2,1,2</sub> |  | 1.0<br><sub>0,2,3,3,1</sub> |  | 0.8 | 0.1 | 0.6 | 11.7 |
| Mitchell Robinson | 98% | 16.5<br><sub>19,-,15,20,15</sub> | 5.5<br><sub>11,-,4,3,6</sub> | 4.5 · 5.5<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>4,-,4,10,7</sub> |  | 0.6<br><sub>0,-,0,1,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.7 | 0.6 | 12.5 |
| Jordan Walsh | 98% | 15.5<br><sub>11,13,12,12,22</sub> | 4.5<br><sub>2,0,5,3,6</sub> | – · 4.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,3,3,4,3</sub> |  | 0.9<br><sub>0,2,0,0,0</sub> |  | 0.5<br><sub>0,0,1,1,1</sub> |  | 0.7 | 0.3 | 0.4 | 8.6 |
| Luka Garza | 98% | 15.4<br><sub>7,21,18,18,19</sub> | 8.8<br><sub>5,12,14,11,6</sub> |  | 4.0<br><sub>1,6,3,5,7</sub> |  | 1.4<br><sub>1,4,0,2,4</sub> |  | 0.9<br><sub>0,2,4,3,2</sub> |  | 0.5 | 0.3 | 0.7 | 14.2 |
| Mike Conley | 100% | 13.6<br><sub>-,-,4,-,11</sub> | 4.2<br><sub>-,-,3,-,0</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 2.2<br><sub>-,-,0,-,1</sub> |  | 0.6<br><sub>-,-,1,-,0</sub> |  | 0.8 | 0.1 | 0.5 | 7.7 |
| Hugo Gonzalez | 96% | 13.4<br><sub>15,14,16,14,15</sub> | 4.2<br><sub>0,7,6,4,8</sub> |  | 2.8<br><sub>2,1,3,2,1</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.6 |
| Ron Harper Jr. | 58% | 8.1<br><sub>3,-,7,-,10</sub> | 3.4<br><sub>0,-,0,-,3</sub> |  | 1.2<br><sub>0,-,1,-,0</sub> |  | 0.7<br><sub>0,-,1,-,2</sub> |  | 0.4<br><sub>0,-,0,-,1</sub> |  | 0.4 | 0.1 | 0.3 | 5.2 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 100% | 33.0<br><sub>27,27,31,33,35</sub> | 18.5<br><sub>23,15,21,25,23</sub> | 19.5 · 20.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>3,3,6,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>0,2,3,3,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,4,4,4,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.2 | 2.1 | 27.8 |
| Jaime Jaquez Jr. | 100% | 29.4<br><sub>27,23,28,31,28</sub> | 14.6<br><sub>19,8,19,18,14</sub> | 13.5 · 13.5<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>4,7,8,2,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>2,5,2,2,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,1,2,4,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.3 | 1.9 | 23.8 |
| Kyle Kuzma | 100% | 28.5<br><sub>18,23,22,27,32</sub> | 11.6<br><sub>4,14,2,6,13</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>6,3,2,5,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>1,3,3,4,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,0,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.3 | 1.6 | 19.8 |
| Brayden Burries | 100% | 28.2<br><sub>17,21,26,22,38</sub> | 11.6<br><sub>10,14,9,9,21</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>5,3,9,5,11</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>1,1,1,3,6</sub> |  | 1.4<br><sub>0,1,1,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.6 | 20.2 |
| Myles Turner | 100% | 27.6<br><sub>22,24,31,36,24</sub> | 9.9<br><sub>4,10,13,12,0</sub> | 9.5 · 8.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>2,7,5,9,7</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,2,2,6,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,1,3,4,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 1.8 | 1.3 | 17.0 |
| Ryan Rollins | 98% | 23.4<br><sub>17,26,17,24,14</sub> | 11.8<br><sub>4,9,10,13,10</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>4,3,3,9,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 4.2<br><sub>5,7,2,5,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>0,1,1,2,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 1.9 | 19.4 |
| AJ Green | 98% | 23.2<br><sub>24,20,24,20,24</sub> | 7.6<br><sub>9,0,13,5,12</sub> | 6.5 · 7.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>1,3,3,2,1</sub> |  | 1.6<br><sub>2,2,3,3,0</sub> |  | 1.5<br><sub>3,0,4,1,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.4 | 0.1 | 0.7 | 11.5 |
| Kel'el Ware | 93% | 16.5<br><sub>17,24,17,16,13</sub> | 7.3<br><sub>6,19,2,2,4</sub> |  | 5.5<br><sub>8,10,9,5,3</sub> |  | 0.8<br><sub>0,3,0,1,0</sub> |  | 0.8<br><sub>0,3,0,0,0</sub> |  | 0.3 | 0.7 | 1.1 | 13.6 |
| Kasparas Jakucionis | 91% | 16.3<br><sub>19,21,22,12,10</sub> | 5.6<br><sub>4,5,7,3,3</sub> |  | 1.9<br><sub>2,3,5,1,0</sub> |  | 3.0<br><sub>6,3,7,1,2</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.1 | 1.0 | 10.5 |
| Caris LeVert | 16% | 14.5<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.4 | 0.7 | 8.0 |
| Nate Ament | 88% | 13.9<br><sub>20,19,8,18,15</sub> | 5.6<br><sub>8,14,4,9,7</sub> |  | 2.0<br><sub>4,1,1,2,1</sub> |  | 0.5<br><sub>0,2,0,0,0</sub> |  | 0.6<br><sub>1,2,0,2,0</sub> |  | 0.3 | 0.3 | 0.7 | 8.1 |
| Jericho Sims | 67% | 9.8<br><sub>7,-,15,1,7</sub> | 2.0<br><sub>0,-,0,0,0</sub> |  | 2.6<br><sub>0,-,2,0,1</sub> |  | 0.7<br><sub>0,-,1,0,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.4 |
| Ousmane Dieng | 58% | 8.3<br><sub>13,6,-,2,-</sub> | 2.7<br><sub>4,0,-,0,-</sub> |  | 1.3<br><sub>0,1,-,0,-</sub> |  | 1.0<br><sub>0,2,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.0 |

</details>


### NOP @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Isaiah Jackson (LAC), Yves Missi (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray | 98% | 32.5<br><sub>-,-,-,45,35</sub> | 17.0<br><sub>-,-,-,20,7</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>-,-,-,8,2</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 6.2<br><sub>-,-,-,4,4</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.8 | 0.3 | 3.2 | 28.9 |
| Trey Murphy III | 98% | 32.3<br><sub>32,29,40,-,34</sub> | 15.6<br><sub>19,15,18,-,10</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>5,5,5,-,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>3,5,5,-,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>2,1,3,-,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.4 | 1.5 | 23.6 |
| Zion Williamson | 98% | 31.9<br><sub>31,30,35,38,36</sub> | 19.1<br><sub>22,15,25,23,13</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>6,6,11,4,8</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>2,4,4,2,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.4 | 0.6 | 2.2 | 27.9 |
| Jeremiah Fears | 98% | 29.9<br><sub>29,31,38,34,36</sub> | 16.4<br><sub>22,20,12,19,24</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>8,5,4,6,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 4.4<br><sub>13,7,7,2,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 2.7 | 25.1 |
| Saddiq Bey | 98% | 26.7<br><sub>24,26,36,29,31</sub> | 13.6<br><sub>10,25,18,22,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>4,6,5,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,1,1,3,4</sub> |  | 1.6<br><sub>1,1,2,2,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.2 | 1.2 | 19.8 |
| Herbert Jones | 98% | 19.3<br><sub>32,25,28,37,14</sub> | 6.0<br><sub>16,11,9,2,0</sub> |  | 2.4<br><sub>4,3,4,5,4</sub> |  | 1.4<br><sub>1,2,3,1,0</sub> |  | 0.7<br><sub>0,1,3,0,0</sub> |  | 1.0 | 0.3 | 0.9 | 9.7 |
| Derik Queen | 98% | 18.4<br><sub>22,23,24,27,10</sub> | 9.0<br><sub>9,8,20,20,6</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>2,8,7,9,4</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>3,4,5,6,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.2<br><sub>1,0,1,0,0</sub> |  | 0.8 | 0.6 | 1.8 | 16.8 |
| Karlo Matkovic | 91% | 16.1<br><sub>28,18,29,21,18</sub> | 6.7<br><sub>12,8,25,5,18</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>4,10,6,4,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>1,1,1,2,1</sub> |  | 0.7<br><sub>1,2,5,1,4</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.6 | 0.8 | 11.3 |
| Trendon Watford | 72% | 13.9<br><sub>17,18,16,20,19</sub> | 5.7<br><sub>8,7,4,7,12</sub> |  | 2.6<br><sub>1,4,4,3,6</sub> |  | 1.4<br><sub>2,0,1,2,1</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.3 | 0.9 | 9.7 |
| Bennedict Mathurin | 98% | 12.8<br><sub>19,19,13,15,7</sub> | 5.7<br><sub>10,7,4,2,2</sub> |  | 2.2<br><sub>3,1,0,5,0</sub> |  | 1.1<br><sub>2,2,0,1,0</sub> |  | 0.4<br><sub>2,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.0 |
| Jordan Poole | 52% | 12.5<br><sub>-,-,-,-,-</sub> | 5.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 8.7 |
| DeAndre Jordan | 30% | 8.0<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.7 |
| Bryce McGowens | 52% | 7.2<br><sub>6,15,6,-,-</sub> | 2.5<br><sub>4,3,0,-,-</sub> |  | 0.9<br><sub>1,0,1,-,-</sub> |  | 0.5<br><sub>2,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |
| AJ Johnson | 26% | 5.3<br><sub>-,3,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.9 | 0.9 |
| Julian Reese | 30% | 5.3<br><sub>-,3,-,-,-</sub> | 2.0<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.9 | 3.5 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.1<br><sub>26,31,33,36,39</sub> | 22.2<br><sub>14,24,15,16,26</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,2,0,4,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>5,5,7,8,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>1,4,1,1,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.2 | 3.7 | 31.8 |
| Rui Hachimura | 98% | 31.1<br><sub>-,26,30,-,37</sub> | 16.4<br><sub>-,12,24,-,21</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>-,5,7,-,9</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>-,0,0,-,7</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>-,2,4,-,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.4 | 1.5 | 23.0 |
| Derrick Jones Jr. | 98% | 29.1<br><sub>28,26,28,-,37</sub> | 11.7<br><sub>15,10,9,-,12</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,1,7,-,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,1,1,-,1</sub> |  | 1.3<br><sub>3,2,1,-,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 1.0 | 1.0 | 17.9 |
| Kris Dunn | 98% | 28.4<br><sub>27,31,27,30,35</sub> | 8.4<br><sub>5,5,12,12,5</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,5,2,4,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.4<br><sub>3,7,4,1,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 2.0 | 0.3 | 1.5 | 16.4 |
| Brook Lopez | 98% | 24.8<br><sub>22,21,19,22,35</sub> | 12.9<br><sub>2,13,7,12,20</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>3,6,2,6,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>3,0,0,1,1</sub> |  | 1.5<br><sub>0,1,1,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 1.4 | 1.2 | 19.7 |
| Max Strus | 97% | 22.5<br><sub>-,-,-,23,23</sub> | 10.2<br><sub>-,-,-,11,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>-,-,-,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.1<br><sub>-,-,-,6,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>-,-,-,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.2 | 1.3 | 17.2 |
| Kobe Sanders | 98% | 21.5<br><sub>27,24,30,38,18</sub> | 9.9<br><sub>9,7,16,26,4</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>4,4,3,4,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>0,2,0,3,1</sub> |  | 1.3<br><sub>1,1,4,5,0</sub> |  | 0.9 | 0.2 | 1.3 | 14.3 |
| Keaton Wagler | 97% | 21.0<br><sub>28,25,19,24,16</sub> | 10.6<br><sub>21,12,7,6,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>4,6,4,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>2,3,4,4,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1<br><sub>3,1,0,0,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.3 | 1.8 | 16.9 |
| Gradey Dick | 96% | 12.1<br><sub>19,12,3,29,7</sub> | 5.5<br><sub>5,3,0,12,4</sub> |  | 1.9<br><sub>5,0,1,4,2</sub> |  | 0.7<br><sub>0,1,0,3,1</sub> |  | 0.5<br><sub>1,1,0,0,0</sub> |  | 0.5 | 0.1 | 0.6 | 8.0 |
| Baba Miller | 91% | 11.1<br><sub>17,5,6,12,6</sub> | 5.0<br><sub>4,0,2,4,2</sub> |  | 1.8<br><sub>7,1,2,0,1</sub> |  | 1.4<br><sub>1,0,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 8.1 |
| Jalen Pickett | 48% | 7.1<br><sub>8,-,6,-,-</sub> | 2.6<br><sub>4,-,0,-,-</sub> |  | 0.9<br><sub>1,-,2,-,-</sub> |  | 1.1<br><sub>1,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Nick Martinelli | 52% | 7.0<br><sub>6,5,6,-,-</sub> | 3.4<br><sub>2,3,10,-,-</sub> |  | 1.8<br><sub>3,0,3,-,-</sub> |  | 0.6<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>0,0,2,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.7 |
| Cam Christie | 52% | 6.6<br><sub>14,5,6,-,-</sub> | 2.6<br><sub>2,2,3,-,-</sub> |  | 1.1<br><sub>0,1,1,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.1<br><sub>0,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Blake Wesley | 52% | 6.4<br><sub>-,5,4,-,-</sub> | 2.8<br><sub>-,0,2,-,-</sub> |  | 0.8<br><sub>-,4,0,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |

</details>


### MIA @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 125.6–115.6 | MIA 76% | 1.31 / 4.22 | SAC +10.5 | 241.5 | SAC +11.5 covers 54%; o236.5 60% |
| Expected (weighted by chance each plays) | 125.0–116.6 | MIA 73% | 1.38 / 3.66 | SAC +8.5 | 241.5 | SAC +11.5 covers 59%; o236.5 60% |
| if Domantas Sabonis plays | 124.5–117.5 | MIA 69% | 1.45 / 3.23 | SAC +7.5 | 241.5 | SAC +11.5 covers 63%; o236.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Domantas Sabonis (SAC) | Questionable | 55% | 30.9 | 14.9 | 11.9 | 5.4 | 0.3 | 0.9 | 0.3 | 2.4 | 32.1 | full tables below |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 34.5<br><sub>34,35,29,43,38</sub> | 13.2<br><sub>10,15,15,11,22</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,6,0,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.0<br><sub>10,11,7,10,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>0,3,4,0,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.3 | 1.9 | 24.0 |
| Bam Adebayo | 98% | 34.0<br><sub>33,33,31,41,33</sub> | 21.4<br><sub>24,27,16,35,18</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 10.2<br><sub>9,9,9,10,10</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,3,4,4,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 1.7 | 0.7 | 1.8 | 35.3 |
| Giannis Antetokounmpo | 98% | 33.4<br><sub>31,31,34,41,31</sub> | 29.6<br><sub>24,31,30,27,20</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.2<br><sub>18,18,12,14,14</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>3,10,7,6,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>0,1,0,0,1</sub> |  | 1.1 | 0.9 | 3.3 | 48.1 |
| Pelle Larsson | 98% | 29.5<br><sub>31,24,30,35,29</sub> | 11.7<br><sub>17,18,9,7,13</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>6,3,3,3,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>8,3,2,4,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>2,1,1,0,3</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.3 | 1.6 | 19.0 |
| Andrew Wiggins | 98% | 25.5<br><sub>29,30,24,23,21</sub> | 11.4<br><sub>18,12,7,3,2</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>2,2,0,4,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.8 | 1.1 | 17.1 |
| Klay Thompson | 98% | 23.6<br><sub>17,26,27,35,23</sub> | 12.2<br><sub>3,25,19,30,11</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,0,1,5,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,3,1,3,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>1,7,4,8,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.4 | 1.0 | 16.0 |
| Bobby Portis | 98% | 17.7<br><sub>23,17,18,18,14</sub> | 7.8<br><sub>11,8,2,4,0</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>9,3,3,10,5</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>4,1,2,5,0</sub> |  | 1.0<br><sub>1,2,0,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.3 | 0.7 | 14.1 |
| Ryan Conwell | 80% | 14.4<br><sub>-,7,8,17,30</sub> | 5.0<br><sub>-,4,5,0,13</sub> |  | 1.4<br><sub>-,0,1,2,1</sub> |  | 1.3<br><sub>-,0,1,2,2</sub> |  | 0.7<br><sub>-,1,1,0,3</sub> |  | 0.6 | 0.1 | 0.5 | 7.6 |
| Tim Hardaway Jr. | 98% | 12.6<br><sub>22,12,19,7,4</sub> | 5.5<br><sub>14,2,9,0,0</sub> |  | 1.3<br><sub>3,1,0,0,0</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.8<br><sub>2,0,3,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.6 |
| Nikola Jovic | 67% | 11.7<br><sub>7,16,7,-,12</sub> | 4.4<br><sub>5,0,2,-,1</sub> |  | 2.1<br><sub>3,4,1,-,0</sub> |  | 1.1<br><sub>0,3,0,-,1</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 7.7 |
| Dru Smith | 67% | 8.3<br><sub>14,4,11,-,1</sub> | 2.8<br><sub>3,0,3,-,0</sub> |  | 1.1<br><sub>0,0,3,-,0</sub> |  | 1.4<br><sub>3,1,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.8 | 0.1 | 0.5 | 5.3 |
| Simone Fontecchio | 52% | 7.5<br><sub>-,2,-,5,-</sub> | 3.9<br><sub>-,3,-,0,-</sub> |  | 1.4<br><sub>-,1,-,0,-</sub> |  | 0.6<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.9 |
| Keshad Johnson | 16% | 6.3 | 3.0 |  | 1.3 |  | 0.3 |  | 0.2 |  | 0.3 | 0.2 | 0.3 | 4.6 |
| Nick Richards | 63% | 6.3<br><sub>-,2,1,-,1</sub> | 2.6<br><sub>-,0,0,-,0</sub> |  | 2.3<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 5.1 |
| Myron Gardner | 58% | 6.1<br><sub>-,2,1,-,1</sub> | 2.5<br><sub>-,0,0,-,0</sub> |  | 1.7<br><sub>-,1,0,-,0</sub> |  | 0.7<br><sub>-,1,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.9 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 36.7<br><sub>41,37,37,42,33</sub> | 25.8<br><sub>34,38,25,22,22</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>6,5,5,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>14,5,6,12,8</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>3,9,2,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.4 | 3.5 | 38.2 |
| Zach LaVine | 98% | 33.5<br><sub>39,21,28,35,35</sub> | 21.7<br><sub>21,11,23,21,14</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>3,0,4,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.2<br><sub>5,1,1,1,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>3,0,5,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.2 | 2.6 | 28.4 |
| De'Andre Hunter | 98% | 32.0<br><sub>37,32,36,38,-</sub> | 15.0<br><sub>24,19,6,14,-</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>5,3,7,2,-</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>1,0,2,2,-</sub> |  | 1.9<br><sub>4,2,0,1,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 1.7 | 22.3 |
| Precious Achiuwa | 98% | 27.2<br><sub>41,25,27,17,22</sub> | 12.2<br><sub>24,6,6,7,9</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 7.4<br><sub>9,5,10,3,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,1,3,1,0</sub> |  | 0.5<br><sub>0,0,0,1,1</sub> |  | 1.1 | 0.8 | 1.2 | 21.4 |
| Leaky Black | 64% | 27.0<br><sub>-,-,25,22,40</sub> | 6.6<br><sub>-,-,12,3,12</sub> |  | 4.5<br><sub>-,-,3,6,3</sub> |  | 1.9<br><sub>-,-,1,1,5</sub> |  | 0.9<br><sub>-,-,4,0,4</sub> |  | 1.2 | 0.5 | 0.8 | 13.1 |
| Keegan Murray | 97% | 26.3<br><sub>-,-,-,-,-</sub> | 10.8<br><sub>-,-,-,-,-</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.8 | 1.0 | 16.8 |
| Malik Monk | 98% | 21.1<br><sub>8,14,30,24,18</sub> | 12.1<br><sub>2,8,24,13,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>1,0,1,2,0</sub> |  | 4.2<br><sub>1,3,7,3,7</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,0,5,3,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.4 | 1.6 | 18.3 |
| Emanuel Sharp | 98% | 21.0<br><sub>18,24,20,10,31</sub> | 6.3<br><sub>0,2,9,3,9</sub> |  | 1.9<br><sub>0,1,3,1,5</sub> |  | 1.2<br><sub>0,1,1,2,0</sub> |  | 0.8<br><sub>0,0,3,1,3</sub> |  | 0.7 | 0.3 | 0.8 | 9.4 |
| Dylan Cardwell | 97% | 16.5<br><sub>-,-,-,13,15</sub> | 4.8<br><sub>-,-,-,4,9</sub> |  | 6.2<br><sub>-,-,-,6,2</sub> |  | 1.2<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.6 | 1.1 | 0.8 | 12.2 |
| Alex Karaban | 58% | 12.4<br><sub>12,10,-,-,11</sub> | 4.4<br><sub>6,0,-,-,0</sub> |  | 1.7<br><sub>0,1,-,-,1</sub> |  | 0.7<br><sub>0,1,-,-,0</sub> |  | 0.4<br><sub>2,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 6.8 |
| Daeqwon Plowden | 64% | 10.1<br><sub>-,4,3,-,-</sub> | 3.8<br><sub>-,4,1,-,-</sub> |  | 1.2<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.6 |

</details>

<details><summary>if Domantas Sabonis plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 98% | 34.4<br><sub>34,35,29,43,38</sub> | 13.1<br><sub>10,15,15,11,22</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,6,0,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.0<br><sub>10,11,7,10,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,3,4,0,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.3 | 1.9 | 23.9 |
| Bam Adebayo (MIA) | 98% | 34.0<br><sub>33,33,31,41,33</sub> | 21.2<br><sub>24,27,16,35,18</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 10.2<br><sub>9,9,9,10,10</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,3,4,4,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 1.7 | 0.7 | 1.9 | 35.2 |
| Giannis Antetokounmpo (MIA) | 98% | 33.4<br><sub>31,31,34,41,31</sub> | 29.6<br><sub>24,31,30,27,20</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.3<br><sub>18,18,12,14,14</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>3,10,7,6,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>0,1,0,0,1</sub> |  | 1.1 | 0.9 | 3.3 | 48.2 |
| Pelle Larsson (MIA) | 98% | 29.6<br><sub>31,24,30,35,29</sub> | 11.7<br><sub>17,18,9,7,13</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>6,3,3,3,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>8,3,2,4,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>2,1,1,0,3</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.3 | 1.6 | 18.9 |
| Andrew Wiggins (MIA) | 98% | 25.6<br><sub>29,30,24,23,21</sub> | 11.4<br><sub>18,12,7,3,2</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>2,2,0,4,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.8 | 1.1 | 17.1 |
| Klay Thompson (MIA) | 98% | 23.6<br><sub>17,26,27,35,23</sub> | 12.1<br><sub>3,25,19,30,11</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,0,1,5,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,3,1,3,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>1,7,4,8,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.4 | 1.0 | 16.0 |
| Bobby Portis (MIA) | 98% | 17.7<br><sub>23,17,18,18,14</sub> | 7.8<br><sub>11,8,2,4,0</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>9,3,3,10,5</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>4,1,2,5,0</sub> |  | 1.0<br><sub>1,2,0,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.3 | 0.7 | 14.1 |
| Ryan Conwell (MIA) | 80% | 14.3<br><sub>-,7,8,17,30</sub> | 4.9<br><sub>-,4,5,0,13</sub> |  | 1.3<br><sub>-,0,1,2,1</sub> |  | 1.4<br><sub>-,0,1,2,2</sub> |  | 0.7<br><sub>-,1,1,0,3</sub> |  | 0.6 | 0.1 | 0.5 | 7.6 |
| Tim Hardaway Jr. (MIA) | 98% | 12.7<br><sub>22,12,19,7,4</sub> | 5.4<br><sub>14,2,9,0,0</sub> |  | 1.3<br><sub>3,1,0,0,0</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.8<br><sub>2,0,3,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.5 |
| Nikola Jovic (MIA) | 67% | 11.8<br><sub>7,16,7,-,12</sub> | 4.4<br><sub>5,0,2,-,1</sub> |  | 2.1<br><sub>3,4,1,-,0</sub> |  | 1.2<br><sub>0,3,0,-,1</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 7.7 |
| Dru Smith (MIA) | 67% | 8.4<br><sub>14,4,11,-,1</sub> | 2.8<br><sub>3,0,3,-,0</sub> |  | 1.1<br><sub>0,0,3,-,0</sub> |  | 1.4<br><sub>3,1,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.8 | 0.2 | 0.4 | 5.3 |
| Simone Fontecchio (MIA) | 52% | 7.5<br><sub>-,2,-,5,-</sub> | 3.9<br><sub>-,3,-,0,-</sub> |  | 1.4<br><sub>-,1,-,0,-</sub> |  | 0.6<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.8 |
| Nick Richards (MIA) | 63% | 6.4<br><sub>-,2,1,-,1</sub> | 2.6<br><sub>-,0,0,-,0</sub> |  | 2.3<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 5.2 |
| Keshad Johnson (MIA) | 16% | 6.3 | 2.9 |  | 1.3 |  | 0.3 |  | 0.2 |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Myron Gardner (MIA) | 58% | 6.2<br><sub>-,2,1,-,1</sub> | 2.5<br><sub>-,0,0,-,0</sub> |  | 1.7<br><sub>-,1,0,-,0</sub> |  | 0.7<br><sub>-,1,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.9 |
| Darius Acuff Jr. (SAC) | 98% | 34.2<br><sub>41,37,37,42,33</sub> | 23.4<br><sub>34,38,25,22,22</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>6,5,5,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>14,5,6,12,8</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>3,9,2,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.3 | 3.0 | 34.4 |
| Zach LaVine (SAC) | 98% | 31.0<br><sub>39,21,28,35,35</sub> | 19.7<br><sub>21,11,23,21,14</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>3,0,4,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>5,1,1,1,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>3,0,5,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.2 | 2.3 | 25.6 |
| Domantas Sabonis (SAC) | 100% | 30.9<br><sub>40,38,31,35,31</sub> | 14.9<br><sub>9,11,9,16,17</sub> | 13.5 · – | 11.9<br><sub>15,14,7,17,12</sub> | 12.5 | 5.4<br><sub>7,8,4,1,5</sub> | 5.5 | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.9 | 0.3 | 2.4 | 32.1 |
| De'Andre Hunter (SAC) | 98% | 28.5<br><sub>37,32,36,38,-</sub> | 13.3<br><sub>24,19,6,14,-</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>5,3,7,2,-</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,0,2,2,-</sub> |  | 1.6<br><sub>4,2,0,1,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 1.4 | 19.3 |
| Keegan Murray (SAC) | 97% | 24.2<br><sub>-,-,-,-,-</sub> | 9.4<br><sub>-,-,-,-,-</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.8 | 0.9 | 14.8 |
| Precious Achiuwa (SAC) | 98% | 24.1<br><sub>41,25,27,17,22</sub> | 10.3<br><sub>24,6,6,7,9</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>9,5,10,3,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>2,1,3,1,0</sub> |  | 0.4<br><sub>0,0,0,1,1</sub> |  | 0.9 | 0.7 | 1.1 | 18.2 |
| Leaky Black (SAC) | 64% | 22.9<br><sub>-,-,25,22,40</sub> | 5.6<br><sub>-,-,12,3,12</sub> |  | 3.9<br><sub>-,-,3,6,3</sub> |  | 1.6<br><sub>-,-,1,1,5</sub> |  | 0.7<br><sub>-,-,4,0,4</sub> |  | 1.0 | 0.4 | 0.7 | 11.1 |
| Malik Monk (SAC) | 98% | 18.9<br><sub>8,14,30,24,18</sub> | 10.4<br><sub>2,8,24,13,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,0,1,2,0</sub> |  | 3.7<br><sub>1,3,7,3,7</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,0,5,3,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.4 | 15.9 |
| Emanuel Sharp (SAC) | 98% | 18.7<br><sub>18,24,20,10,31</sub> | 5.4<br><sub>0,2,9,3,9</sub> |  | 1.8<br><sub>0,1,3,1,5</sub> |  | 1.0<br><sub>0,1,1,2,0</sub> |  | 0.7<br><sub>0,0,3,1,3</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Dylan Cardwell (SAC) | 97% | 15.1<br><sub>-,-,-,13,15</sub> | 4.5<br><sub>-,-,-,4,9</sub> |  | 5.6<br><sub>-,-,-,6,2</sub> |  | 1.1<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.0 | 0.8 | 11.2 |
| Alex Karaban (SAC) | 58% | 8.6<br><sub>12,10,-,-,11</sub> | 3.2<br><sub>6,0,-,-,0</sub> |  | 1.2<br><sub>0,1,-,-,1</sub> |  | 0.5<br><sub>0,1,-,-,0</sub> |  | 0.2<br><sub>2,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.9 |
| Daeqwon Plowden (SAC) | 64% | 7.5<br><sub>-,4,3,-,-</sub> | 3.1<br><sub>-,4,1,-,-</sub> |  | 0.9<br><sub>-,0,1,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-08/`._
