# NBA model · Wed 18 Nov 2026 (US date)

Updated **Thu 19 Nov, 01:44 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-18/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matisse Thybulle STL over 4.5 (5+) | UTA @ LAL | draftkings | 11.80 | 10.94 | 6.31 | 15.8% | 7.9% | 9.1% | +7.9% | +87.0% | 0.2% |
| Devin Booker AST over 9.5 (10+) | PHX @ SAC | draftkings | 14.80 | 13.74 | 7.96 | 12.6% | 6.3% | 7.3% | +7.7% | +85.9% | 0.1% |
| Nikola Jokic AST over 15.5 (16+) | BOS @ DEN | draftkings | 21.00 | 19.57 | 11.47 | 8.7% | 4.5% | 5.1% | +7.2% | +83.0% | 0.1% |
| Nikola Jokic AST over 13.5 (14+) | BOS @ DEN | draftkings | 10.30 | 9.61 | 5.63 | 17.8% | 9.1% | 10.4% | +7.2% | +82.9% | 0.2% |
| Matisse Thybulle STL over 5.5 (6+) | UTA @ LAL | draftkings | 22.00 | 20.58 | 12.17 | 8.2% | 4.2% | 4.9% | +6.9% | +80.8% | 0.1% |
| Matisse Thybulle STL over 3.5 (4+) | UTA @ LAL | draftkings | 6.04 | 5.68 | 3.41 | 29.3% | 15.5% | 17.6% | +6.3% | +76.9% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Neemias Queta BLK over 1.5 (2+) | BOS @ DEN | draftkings | 2.72 | 2.19 | 4.51 | 22.2% | 49.9% | 45.7% | +24.2% | -39.7% | 2.0% |
| Quentin Grimes PTS under 15.5 | UTA @ LAL | betright | 2.00 | 1.90 | 1.41 | 70.8% | 49.5% | 52.8% | +5.5% | +41.7% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| BOS @ DEN | Thu 19 Nov 13:30 | 112.7–108.4 | BOS 61% | 1.63 / 2.59 | DEN +4.5 | 221.5 | DEN +2.5 covers 45%; o218.5 55% |
| UTA @ LAL | Thu 19 Nov 14:00 | 107.8–124.5 | UTA 12% | 8.51 / 1.13 | LAL -16.5 | 232.5 | LAL -11.5 covers 64%; o229.5 56% |
| PHX @ SAC | Thu 19 Nov 14:00 | 118.5–113.5 | PHX 64% | 1.55 / 2.81 | SAC +5.5 | 231.5 | SAC +7.5 covers 56%; o226.5 61% |

### BOS @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White PTS under 13.5 | BOS @ DEN | tab | 1.95 | 1.87 | 1.63 | 61.4% | 51.9% | 53.4% | +4.2% | +19.8% | 1.1% |
| Payton Pritchard PTS under 13.5 | BOS @ DEN | pointsbetau | 2.00 | 1.96 | 1.70 | 58.9% | 49.6% | 51.0% | +2.1% | +17.7% | 0.5% |
| Aaron Gordon PTS over 11.5 (12+) | BOS @ DEN | pointsbetau | 2.05 | 2.02 | 2.10 | 47.5% | 50.0% | 49.6% | +1.7% | -2.5% | 0.4% |
| Jamal Murray PTS under 21.5 | BOS @ DEN | unibet | 2.00 | 1.97 | 2.06 | 48.5% | 51.1% | 50.7% | +1.4% | -3.0% | 0.3% |
| Baylor Scheierman PTS over 4.5 (5+) | BOS @ DEN | sportsbet | 1.96 | 1.94 | 2.00 | 49.9% | 51.8% | 51.5% | +1.0% | -2.0% | 0.3% |
| Neemias Queta PTS under 8.5 | BOS @ DEN | betright | 2.00 | 2.00 | 1.65 | 60.5% | 48.2% | 50.1% | +0.2% | +21.0% | 0.1% |
| Cameron Johnson PTS under 12.5 | BOS @ DEN | tab | 1.90 | 1.90 | 1.77 | 56.5% | 51.9% | 52.6% | +0.0% | +7.4% | 0.0% |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 33.8<br><sub>29,32,38,30,36</sub> | 24.0<br><sub>21,21,24,32,24</sub> | 25.5 · 24.5<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>4,6,7,6,12</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 6.8<br><sub>6,4,8,6,4</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>5,3,2,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.5 | 2.6 | 38.6 |
| Paul George | 98% | 30.2<br><sub>28,30,-,25,36</sub> | 18.0<br><sub>27,36,-,7,22</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>3,5,-,7,8</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 3.6<br><sub>1,1,-,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>5,6,-,1,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.4 | 2.0 | 26.6 |
| Derrick White | 98% | 30.0<br><sub>27,22,38,23,32</sub> | 12.6<br><sub>9,5,19,16,9</sub> | 12.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,1,1,4,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.3<br><sub>7,3,7,2,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,1,3,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.8 | 1.3 | 20.3 |
| Payton Pritchard | 98% | 26.4<br><sub>29,30,31,19,32</sub> | 13.0<br><sub>12,18,14,10,21</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,6,1,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.8<br><sub>4,5,1,6,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>4,4,2,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.1 | 1.0 | 19.9 |
| Neemias Queta | 98% | 20.4<br><sub>22,22,31,15,-</sub> | 8.0<br><sub>13,4,11,8,-</sub> | 8.5 · 9.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>9,6,13,6,-</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>4,3,3,2,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.5 | 0.9 | 0.9 | 16.2 |
| Sam Hauser | 98% | 20.1<br><sub>23,18,24,11,25</sub> | 7.9<br><sub>7,12,8,8,12</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,5,9,1,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,2,0,0,2</sub> |  | 1.5<br><sub>1,4,2,2,4</sub> | 2.5<br><sub>o 35% · u 65%</sub> | 0.4 | 0.2 | 0.3 | 12.1 |
| Baylor Scheierman | 98% | 15.9<br><sub>19,18,29,18,11</sub> | 5.1<br><sub>7,5,9,12,0</sub> | 4.5 · 4.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>1,3,7,5,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,2,3,3,1</sub> |  | 0.7<br><sub>1,1,3,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.6 | 0.1 | 0.5 | 9.3 |
| Mitchell Robinson | 98% | 15.4<br><sub>18,17,11,15,18</sub> | 4.4<br><sub>12,2,2,0,4</sub> |  | 5.8<br><sub>7,6,2,7,5</sub> |  | 0.7<br><sub>2,2,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 0.6 | 10.9 |
| Jordan Walsh | 98% | 14.1<br><sub>11,19,18,21,17</sub> | 4.3<br><sub>0,8,6,11,6</sub> | – · 4.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>3,2,3,1,2</sub> |  | 0.7<br><sub>0,2,0,0,0</sub> |  | 0.5<br><sub>0,1,0,2,2</sub> |  | 0.5 | 0.3 | 0.4 | 7.6 |
| Luka Garza | 98% | 13.3<br><sub>9,9,11,14,18</sub> | 6.3<br><sub>4,2,5,2,3</sub> |  | 3.1<br><sub>5,0,1,3,0</sub> |  | 1.3<br><sub>0,2,0,5,4</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.3 | 0.5 | 10.8 |
| Devin Carter | 91% | 12.5<br><sub>-,-,-,12,-</sub> | 4.9<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,2,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.2 | 0.9 | 8.7 |
| Hugo Gonzalez | 98% | 8.9<br><sub>10,19,8,18,4</sub> | 2.9<br><sub>0,10,0,9,0</sub> |  | 1.8<br><sub>2,2,1,5,2</sub> |  | 0.5<br><sub>1,2,0,2,0</sub> |  | 0.2<br><sub>0,2,0,2,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.1 |
| Chris Cenac Jr. | 58% | 7.5<br><sub>-,-,-,7,12</sub> | 2.8<br><sub>-,-,-,6,4</sub> |  | 1.6<br><sub>-,-,-,3,2</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Mike Conley | 38% | 7.1<br><sub>10,-,-,-,-</sub> | 1.9<br><sub>3,-,-,-,-</sub> |  | 0.7<br><sub>3,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |
| Ron Harper Jr. | 58% | 6.7<br><sub>4,4,-,12,-</sub> | 3.1<br><sub>2,0,-,10,-</sub> |  | 1.0<br><sub>0,1,-,1,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,2,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.6 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.1<br><sub>36,39,37,37,38</sub> | 24.4<br><sub>19,25,27,26,28</sub> | 23.5 · 24.5<br><sub>o 49% · u 51%</sub> | 11.9<br><sub>13,16,11,8,15</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 10.1<br><sub>8,9,8,10,7</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.8 | 3.7 | 46.4 |
| Jamal Murray | 98% | 37.0<br><sub>34,39,32,38,35</sub> | 23.0<br><sub>16,38,30,23,28</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>6,2,4,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>8,2,8,9,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>2,5,4,0,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.6 | 2.5 | 34.1 |
| Christian Braun | 98% | 32.8<br><sub>29,32,37,28,33</sub> | 12.0<br><sub>6,4,12,17,10</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,5,5,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,3,4,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.4 | 0.9 | 18.8 |
| Cameron Johnson | 98% | 29.9<br><sub>29,31,30,31,27</sub> | 12.3<br><sub>18,8,23,12,9</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,2,4,5,0</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,1,3,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.9<br><sub>2,2,4,1,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.3 | 1.0 | 18.3 |
| Aaron Gordon | 98% | 29.3<br><sub>27,30,27,33,24</sub> | 11.9<br><sub>12,3,9,11,11</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,5,3,5,1</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>0,2,2,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.4 | 1.2 | 19.4 |
| DeMar DeRozan | 91% | 20.3<br><sub>22,19,20,24,14</sub> | 9.5<br><sub>11,7,8,9,2</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,4,1,3,1</sub> |  | 2.6<br><sub>5,2,4,2,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 14.0 |
| Trevon Brazile | 98% | 17.8<br><sub>14,14,13,16,23</sub> | 5.2<br><sub>3,5,7,5,9</sub> | 5.5 · 5.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>4,2,5,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.3 | 0.3 | 0.7 | 10.0 |
| Spencer Jones | 86% | 16.6<br><sub>21,14,22,12,21</sub> | 4.2<br><sub>13,0,3,4,4</sub> | 3.5 · 3.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>6,0,1,2,3</sub> |  | 0.8<br><sub>0,1,0,1,3</sub> |  | 0.5<br><sub>3,0,1,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.4 |
| Marvin Bagley III | 98% | 12.6<br><sub>12,12,12,13,10</sub> | 5.8<br><sub>10,6,4,7,4</sub> |  | 3.7<br><sub>3,3,2,7,2</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 10.2 |
| Tyus Jones | 97% | 10.0<br><sub>13,6,11,10,10</sub> | 2.5<br><sub>3,2,0,2,0</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 1.7<br><sub>4,0,4,3,2</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.1 |
| Bryce Hopkins | 58% | 8.0<br><sub>3,3,-,-,4</sub> | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Zeke Nnaji | 26% | 6.4<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.7 |
| Alpha Diallo | 48% | 6.1<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### UTA @ LAL
Out: Austin Reaves (LAL), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darryn Peterson PTS under 18.5 | UTA @ LAL | tab | 1.95 | 1.92 | 1.70 | 59.0% | 50.9% | 52.2% | +1.8% | +15.1% | 0.5% |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 100% | 33.3<br><sub>-,33,38,34,35</sub> | 20.6<br><sub>-,13,27,13,30</sub> | 21.5 · 22.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 3.4 | 30.8 |
| Darryn Peterson | 100% | 32.4<br><sub>31,33,34,34,31</sub> | 17.8<br><sub>25,22,28,17,13</sub> | 18.5 · 18.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.6 | 2.2 | 26.0 |
| Ace Bailey | 100% | 31.2<br><sub>35,31,35,30,23</sub> | 14.3<br><sub>23,18,21,7,5</sub> | 13.5 · 13.5<br><sub>o 53% · u 47%</sub> | 4.9<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,2,1,4,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.8 | 1.8 | 21.3 |
| Mo Bamba | 100% | 27.3<br><sub>17,18,20,36,31</sub> | 10.2<br><sub>7,5,9,26,15</sub> | – · 8.5<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>7,1,9,5,10</sub> |  | 1.4<br><sub>0,1,1,4,3</sub> |  | 0.7<br><sub>0,0,0,6,1</sub> |  | 0.7 | 1.6 | 1.2 | 20.2 |
| Brice Sensabaugh | 99% | 25.7<br><sub>14,23,27,30,35</sub> | 15.0<br><sub>5,19,7,14,40</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>4,3,3,7,11</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,1,1,2,5</sub> |  | 2.2<br><sub>1,3,1,0,8</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.2 | 2.1 | 21.2 |
| Josh Okogie | 97% | 22.0<br><sub>21,15,22,27,22</sub> | 6.0<br><sub>6,7,7,7,9</sub> | 6.5 · 5.5<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>4,3,2,6,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>4,0,1,0,4</sub> |  | 0.7<br><sub>0,1,2,2,1</sub> |  | 1.1 | 0.2 | 0.8 | 10.5 |
| Josh Green | 100% | 21.7<br><sub>30,26,14,15,13</sub> | 4.8<br><sub>2,3,2,6,9</sub> | 4.5 · 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>5,2,0,1,1</sub> |  | 1.1<br><sub>4,1,0,1,0</sub> |  | 0.6<br><sub>0,1,0,2,1</sub> |  | 0.8 | 0.2 | 0.8 | 8.0 |
| Jaxson Hayes | 76% | 20.8<br><sub>17,30,13,-,-</sub> | 7.8<br><sub>6,11,12,-,-</sub> |  | 4.9<br><sub>2,8,5,-,-</sub> |  | 1.1<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.7 | 0.8 | 0.9 | 13.8 |
| Svi Mykhailiuk | 97% | 18.8<br><sub>21,20,7,21,33</sub> | 6.6<br><sub>7,3,0,6,8</sub> |  | 2.1<br><sub>2,0,1,2,7</sub> |  | 1.5<br><sub>3,2,0,3,5</sub> |  | 1.1<br><sub>1,1,0,2,2</sub> |  | 0.5 | 0.1 | 0.8 | 10.2 |
| Isaiah Collier | 63% | 15.6<br><sub>24,12,16,-,-</sub> | 7.2<br><sub>17,7,3,-,-</sub> |  | 2.2<br><sub>5,3,2,-,-</sub> |  | 4.1<br><sub>5,2,5,-,-</sub> |  | 0.4<br><sub>4,1,1,-,-</sub> |  | 0.7 | 0.2 | 1.6 | 13.4 |
| Tony Bradley | 72% | 13.5<br><sub>14,-,12,12,17</sub> | 4.3<br><sub>4,-,0,6,3</sub> |  | 4.0<br><sub>5,-,5,2,7</sub> |  | 0.6<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.9 |
| Kyle Filipowski | 52% | 11.7<br><sub>15,-,2,-,-</sub> | 5.8<br><sub>7,-,2,-,-</sub> |  | 3.5<br><sub>4,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.4 |
| Jonas Aidoo | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 100% | 34.0<br><sub>-,39,32,36,42</sub> | 39.1<br><sub>-,32,32,43,36</sub> | 36.5 · 37.5<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>-,8,5,3,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 7.9<br><sub>-,10,5,9,7</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 5.0<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.6 | 4.0 | 53.9 |
| Quentin Grimes | 100% | 30.1<br><sub>32,-,-,37,42</sub> | 12.9<br><sub>12,-,-,22,47</sub> | 15.5 · 15.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>1,-,-,6,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>4,-,-,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,-,-,5,10</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.4 | 1.6 | 19.7 |
| Walker Kessler | 100% | 28.0<br><sub>29,30,29,32,-</sub> | 11.9<br><sub>12,21,10,14,-</sub> | 14.5 · 13.5<br><sub>o 50% · u 50%</sub> | 11.6<br><sub>16,10,11,12,-</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>4,4,3,3,-</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 25.3 |
| Ziaire Williams | 100% | 25.1<br><sub>21,28,20,19,24</sub> | 10.0<br><sub>17,12,9,6,0</sub> |  | 3.0<br><sub>2,2,1,2,1</sub> |  | 1.6<br><sub>0,2,5,3,1</sub> |  | 1.4<br><sub>4,2,1,0,0</sub> |  | 1.6 | 0.4 | 1.0 | 14.6 |
| Matisse Thybulle | 100% | 25.1<br><sub>28,23,23,26,31</sub> | 7.9<br><sub>4,6,8,12,7</sub> | 6.5 · 6.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,0,5,8,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.7 | 0.9 | 1.1 | 12.3 |
| Jake LaRavia | 98% | 22.9<br><sub>29,32,21,32,23</sub> | 6.6<br><sub>5,4,0,12,4</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,3,9,3,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.7 | 1.1 | 12.5 |
| Sandro Mamukelashvili | 99% | 22.1<br><sub>18,32,26,21,23</sub> | 10.3<br><sub>7,23,23,4,3</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,8,3,2,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.3<br><sub>1,5,5,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.5 | 0.8 | 16.9 |
| Collin Sexton | 98% | 21.1<br><sub>24,27,13,24,25</sub> | 13.6<br><sub>17,18,10,16,10</sub> | 13.5 · 13.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.7 | 18.8 |
| Jarred Vanderbilt | 88% | 13.2<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.1<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Carson Cooper | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.5 | 0.8 | 8.3 |
| Kevon Looney | 52% | 9.9<br><sub>-,-,4,-,17</sub> | 2.2<br><sub>-,-,0,-,4</sub> |  | 3.9<br><sub>-,-,2,-,8</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 7.0 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Adou Thiero | 72% | 7.9<br><sub>8,7,14,-,6</sub> | 2.6<br><sub>2,2,2,-,0</sub> |  | 2.1<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Jaden Hardy | 48% | 7.1<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.0 | 0.5 | 5.5 |
| Cameron Carr | 63% | 7.0<br><sub>-,7,13,-,-</sub> | 3.7<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Bronny James | 48% | 5.7<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 2.8 |
| Chris Manon | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 3.1 |

</details>


### PHX @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. PTS under 24.5 | PHX @ SAC | draftkings | 1.89 | 1.89 | 1.54 | 64.9% | 50.9% | 53.0% | +0.4% | +22.8% | 0.1% |
| Zach LaVine PTS over 17.5 (18+) | PHX @ SAC | draftkings | 1.97 | 1.97 | 2.28 | 43.9% | 52.1% | 50.9% | +0.3% | -13.5% | 0.1% |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 100% | 34.4<br><sub>29,29,35,28,37</sub> | 26.7<br><sub>32,17,30,17,20</sub> | 25.5 · 26.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.2<br><sub>4,5,7,7,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,2,4,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 2.7 | 36.3 |
| Dillon Brooks | 100% | 29.0<br><sub>26,22,30,22,27</sub> | 16.1<br><sub>7,8,15,1,15</sub> | 13.5 · 13.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 1.4 | 21.6 |
| Miles Bridges | 100% | 28.1<br><sub>26,18,25,24,29</sub> | 14.3<br><sub>7,8,11,14,16</sub> | 14.5 · 14.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>5,4,6,3,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.5 | 1.2 | 22.9 |
| Jalen Green | 100% | 27.0<br><sub>24,21,21,21,27</sub> | 15.6<br><sub>6,13,12,9,16</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.3 | 2.0 | 22.3 |
| Oso Ighodaro | 100% | 25.6<br><sub>18,20,32,17,33</sub> | 6.7<br><sub>7,6,2,4,8</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.4 | 16.1 |
| Collin Gillespie | 98% | 25.2<br><sub>24,22,27,28,26</sub> | 10.4<br><sub>6,12,13,26,10</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,2,2,4,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.2 | 1.0 | 17.5 |
| Jordan Goodwin | 98% | 21.1<br><sub>-,14,24,31,20</sub> | 8.8<br><sub>-,18,6,14,11</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.2 | 0.8 | 15.3 |
| Luke Kennard | 98% | 18.5<br><sub>14,22,21,23,17</sub> | 7.7<br><sub>3,14,8,18,12</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,1,6,2</sub> |  | 1.9<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.7 | 11.6 |
| Ryan Dunn | 98% | 15.9<br><sub>23,25,10,24,12</sub> | 4.8<br><sub>3,10,0,3,5</sub> |  | 3.4<br><sub>2,8,4,6,1</sub> |  | 1.1<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.4 | 0.6 | 9.3 |
| Khaman Maluach | 98% | 14.8<br><sub>20,22,16,13,11</sub> | 5.5<br><sub>11,11,4,7,4</sub> |  | 4.8<br><sub>5,7,2,4,6</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.8 | 11.0 |
| Rasheer Fleming | 43% | 8.7<br><sub>9,12,-,-,-</sub> | 3.2<br><sub>2,4,-,-,-</sub> |  | 1.5<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.4 | 0.3 | 0.4 | 4.9 |
| Jamaree Bouyea | 48% | 7.3<br><sub>9,8,-,-,-</sub> | 3.0<br><sub>4,7,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.1 |
| Koa Peat | 67% | 6.7<br><sub>6,6,-,8,1</sub> | 3.1<br><sub>4,5,-,10,0</sub> |  | 1.6<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.0 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 100% | 33.8<br><sub>33,39,40,35,33</sub> | 22.1<br><sub>22,32,29,17,26</sub> | 24.5 · 24.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.6<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,3,4,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 4.0 | 32.3 |
| De'Andre Hunter | 100% | 30.6<br><sub>-,31,34,42,-</sub> | 13.6<br><sub>-,14,15,24,-</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>-,3,4,5,-</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>-,1,2,2,-</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>-,2,3,2,-</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.7 | 19.6 |
| Zach LaVine | 100% | 30.0<br><sub>35,25,33,36,-</sub> | 17.3<br><sub>14,15,31,12,-</sub> | 18.5 · 17.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,4,3,3,-</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.6<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 2.4 | 23.0 |
| Domantas Sabonis | 100% | 29.6<br><sub>31,-,24,35,29</sub> | 13.6<br><sub>17,-,0,21,11</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 11.3<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.3<br><sub>1,-,0,1,0</sub> |  | 0.8 | 0.3 | 2.5 | 29.9 |
| Keegan Murray | 100% | 27.1<br><sub>-,23,24,40,21</sub> | 10.5<br><sub>-,10,11,16,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>-,1,2,7,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>-,2,1,4,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>-,0,2,2,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.9 | 1.0 | 16.0 |
| Precious Achiuwa | 98% | 22.9<br><sub>22,36,14,-,-</sub> | 9.6<br><sub>9,7,10,-,-</sub> | 8.5 · 7.5<br><sub>o 53% · u 47%</sub> | 6.2<br><sub>4,14,3,-,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>0,2,0,-,-</sub> |  | 0.3<br><sub>1,0,1,-,-</sub> |  | 0.9 | 0.8 | 1.1 | 16.9 |
| Leaky Black | 86% | 18.7<br><sub>40,20,18,12,29</sub> | 4.5<br><sub>12,6,0,0,12</sub> |  | 3.2<br><sub>3,5,3,0,9</sub> |  | 1.2<br><sub>5,1,2,0,2</sub> |  | 0.6<br><sub>4,2,0,0,4</sub> |  | 0.9 | 0.5 | 0.6 | 8.9 |
| Malik Monk | 98% | 17.0<br><sub>18,21,3,18,29</sub> | 9.0<br><sub>12,9,1,7,14</sub> |  | 1.8<br><sub>0,2,0,4,1</sub> |  | 3.3<br><sub>7,3,0,3,10</sub> |  | 1.1<br><sub>2,0,0,0,1</sub> |  | 0.5 | 0.3 | 1.4 | 14.1 |
| Dylan Cardwell | 98% | 16.6<br><sub>15,18,29,13,19</sub> | 5.2<br><sub>9,4,1,6,10</sub> | 4.5 · 4.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>2,9,11,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 12.7 |
| Emanuel Sharp | 98% | 14.6<br><sub>31,12,19,7,21</sub> | 4.4<br><sub>9,5,2,4,9</sub> |  | 1.4<br><sub>5,1,2,0,0</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>3,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.6 | 6.5 |
| Alex Karaban | 52% | 13.0<br><sub>11,-,-,-,29</sub> | 2.5<br><sub>0,-,-,-,0</sub> |  | 1.8<br><sub>1,-,-,-,5</sub> |  | 0.7<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 5.1 |
| Daeqwon Plowden | 88% | 12.4<br><sub>-,12,2,2,24</sub> | 5.0<br><sub>-,6,0,0,13</sub> |  | 1.5<br><sub>-,0,0,0,2</sub> |  | 0.6<br><sub>-,0,0,0,1</sub> |  | 0.7<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.1 |
| Mason Plumlee | 52% | 6.4<br><sub>-,-,-,-,5</sub> | 2.0<br><sub>-,-,-,-,2</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-18/`._
