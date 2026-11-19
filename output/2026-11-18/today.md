# NBA model · Wed 18 Nov 2026 (US date)

Updated **Thu 19 Nov, 01:24 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-18/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ace Bailey 3PM over 2.5 (3+) | UTA @ LAL | draftkings | 2.48 | 2.36 | 2.95 | 33.9% | 43.9% | 42.4% | +5.0% | -16.1% | 0.9% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic AST over 15.5 (16+) | BOS @ DEN | draftkings | 23.00 | 20.96 | 11.59 | 8.6% | 4.1% | 4.8% | +9.6% | +98.4% | 0.1% |
| Matisse Thybulle STL over 4.5 (5+) | UTA @ LAL | draftkings | 12.80 | 11.70 | 6.49 | 15.4% | 7.3% | 8.6% | +9.4% | +97.1% | 0.2% |
| Luka Doncic PA over 59.5 (60+) | UTA @ LAL | draftkings | 8.60 | 8.00 | 4.65 | 21.5% | 10.9% | 12.5% | +7.5% | +84.8% | 0.2% |
| Nikola Jokic AST over 13.5 (14+) | BOS @ DEN | draftkings | 10.30 | 9.62 | 5.65 | 17.7% | 9.1% | 10.4% | +7.1% | +82.4% | 0.2% |
| Devin Booker AST over 9.5 (10+) | PHX @ SAC | draftkings | 14.60 | 13.62 | 8.02 | 12.5% | 6.4% | 7.3% | +7.1% | +82.0% | 0.1% |
| Matisse Thybulle STL over 5.5 (6+) | UTA @ LAL | draftkings | 23.00 | 21.65 | 12.98 | 7.7% | 4.1% | 4.6% | +6.4% | +77.2% | 0.1% |
| Matisse Thybulle STL over 3.5 (4+) | UTA @ LAL | draftkings | 5.95 | 5.67 | 3.53 | 28.3% | 15.7% | 17.6% | +5.1% | +68.7% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Neemias Queta BLK over 1.5 (2+) | BOS @ DEN | draftkings | 2.72 | 2.17 | 4.01 | 25.0% | 49.9% | 46.1% | +25.4% | -32.1% | 2.0% |
| Quentin Grimes PTS under 15.5 | UTA @ LAL | pointsbetau | 2.00 | 1.90 | 1.40 | 71.2% | 49.1% | 52.5% | +5.1% | +42.4% | 1.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| BOS @ DEN | Thu 19 Nov 13:30 | 112.7–108.4 | BOS 61% | 1.63 / 2.59 | DEN +4.5 | 221.5 | DEN +2.5 covers 45%; o218.5 55% |
| UTA @ LAL | Thu 19 Nov 14:00 | 107.8–124.5 | UTA 12% | 8.51 / 1.13 | LAL -16.5 | 232.5 | LAL -11.5 covers 64%; o229.5 56% |
| PHX @ SAC | Thu 19 Nov 14:00 | 118.5–113.5 | PHX 64% | 1.55 / 2.81 | SAC +5.5 | 231.5 | SAC +7.5 covers 56%; o227.5 59% |

### BOS @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White PTS under 13.5 | BOS @ DEN | tab | 1.95 | 1.87 | 1.62 | 61.8% | 51.9% | 53.4% | +4.3% | +20.6% | 1.1% |
| Payton Pritchard PTS under 13.5 | BOS @ DEN | pointsbetau | 2.00 | 1.95 | 1.65 | 60.5% | 49.6% | 51.3% | +2.6% | +21.0% | 0.6% |
| Aaron Gordon PTS over 11.5 (12+) | BOS @ DEN | pointsbetau | 2.05 | 2.01 | 2.05 | 48.8% | 50.0% | 49.8% | +2.1% | -0.0% | 0.5% |
| Jamal Murray PTS under 21.5 | BOS @ DEN | unibet | 2.00 | 1.98 | 2.00 | 50.1% | 50.6% | 50.5% | +1.0% | +0.2% | 0.3% |
| Baylor Scheierman PTS over 4.5 (5+) | BOS @ DEN | sportsbet | 1.96 | 1.95 | 2.07 | 48.4% | 51.9% | 51.3% | +0.7% | -5.1% | 0.2% |
| Jayson Tatum PTS under 24.5 | BOS @ DEN | unibet | 2.00 | 1.99 | 1.71 | 58.6% | 48.7% | 50.3% | +0.5% | +17.2% | 0.1% |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 100% | 33.5<br><sub>29,32,38,30,36</sub> | 23.7<br><sub>21,21,24,32,24</sub> | 24.5 · 24.5<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>4,6,7,6,12</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>6,4,8,6,4</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>5,3,2,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.5 | 2.6 | 38.3 |
| Paul George | 100% | 30.3<br><sub>28,30,-,25,36</sub> | 17.8<br><sub>27,36,-,7,22</sub> | 18.5 · 18.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>3,5,-,7,8</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>1,1,-,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>5,6,-,1,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.4 | 2.0 | 26.5 |
| Derrick White | 100% | 29.9<br><sub>27,22,38,23,32</sub> | 12.5<br><sub>9,5,19,16,9</sub> | 12.5 · 13.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,1,1,4,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.3<br><sub>7,3,7,2,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,1,3,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.8 | 1.3 | 20.1 |
| Payton Pritchard | 98% | 26.2<br><sub>29,30,31,19,32</sub> | 12.8<br><sub>12,18,14,10,21</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,6,1,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.8<br><sub>4,5,1,6,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>4,4,2,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.0 | 19.7 |
| Neemias Queta | 100% | 22.3<br><sub>22,22,31,15,-</sub> | 8.6<br><sub>13,4,11,8,-</sub> | 8.5 · 9.5<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>9,6,13,6,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>4,3,3,2,-</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.6 | 1.0 | 1.0 | 17.6 |
| Sam Hauser | 98% | 19.9<br><sub>23,18,24,11,25</sub> | 7.7<br><sub>7,12,8,8,12</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,5,9,1,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,2,0,0,2</sub> |  | 1.4<br><sub>1,4,2,2,4</sub> | 2.5<br><sub>o 35% · u 65%</sub> | 0.4 | 0.2 | 0.3 | 11.9 |
| Jordan Walsh | 100% | 16.8<br><sub>11,19,18,21,17</sub> | 5.0<br><sub>0,8,6,11,6</sub> | – · 4.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,2,3,1,2</sub> |  | 0.8<br><sub>0,2,0,0,0</sub> |  | 0.6<br><sub>0,1,0,2,2</sub> |  | 0.6 | 0.3 | 0.5 | 9.0 |
| Baylor Scheierman | 98% | 15.7<br><sub>19,18,29,18,11</sub> | 4.9<br><sub>7,5,9,12,0</sub> | 4.5 · 4.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>1,3,7,5,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>0,2,3,3,1</sub> |  | 0.7<br><sub>1,1,3,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.6 | 0.1 | 0.5 | 9.1 |
| Mitchell Robinson | 98% | 15.3<br><sub>18,17,11,15,18</sub> | 4.3<br><sub>12,2,2,0,4</sub> |  | 5.8<br><sub>7,6,2,7,5</sub> |  | 0.7<br><sub>2,2,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 0.6 | 10.8 |
| Luka Garza | 98% | 13.2<br><sub>9,9,11,14,18</sub> | 6.2<br><sub>4,2,5,2,3</sub> |  | 3.1<br><sub>5,0,1,3,0</sub> |  | 1.3<br><sub>0,2,0,5,4</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.4 | 0.5 | 10.7 |
| Devin Carter | 91% | 12.3<br><sub>-,-,-,12,-</sub> | 4.8<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,2,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.2 | 0.9 | 8.6 |
| Hugo Gonzalez | 98% | 8.7<br><sub>10,19,8,18,4</sub> | 2.8<br><sub>0,10,0,9,0</sub> |  | 1.8<br><sub>2,2,1,5,2</sub> |  | 0.4<br><sub>1,2,0,2,0</sub> |  | 0.2<br><sub>0,2,0,2,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.0 |
| Chris Cenac Jr. | 58% | 7.5<br><sub>-,-,-,7,12</sub> | 2.8<br><sub>-,-,-,6,4</sub> |  | 1.6<br><sub>-,-,-,3,2</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Mike Conley | 38% | 7.1<br><sub>10,-,-,-,-</sub> | 1.9<br><sub>3,-,-,-,-</sub> |  | 0.8<br><sub>3,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |
| Ron Harper Jr. | 58% | 6.7<br><sub>4,4,-,12,-</sub> | 3.1<br><sub>2,0,-,10,-</sub> |  | 1.0<br><sub>0,1,-,1,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,2,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.6 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 100% | 37.1<br><sub>36,39,37,37,38</sub> | 24.5<br><sub>19,25,27,26,28</sub> | 23.5 · 24.5<br><sub>o 49% · u 51%</sub> | 12.0<br><sub>13,16,11,8,15</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 10.1<br><sub>8,9,8,10,7</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.8 | 3.7 | 46.5 |
| Jamal Murray | 100% | 36.8<br><sub>34,39,32,38,35</sub> | 22.6<br><sub>16,38,30,23,28</sub> | 20.5 · 21.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,2,4,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>8,2,8,9,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>2,5,4,0,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.5 | 2.5 | 33.6 |
| Christian Braun | 100% | 32.7<br><sub>29,32,37,28,33</sub> | 11.9<br><sub>6,4,12,17,10</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,5,5,7,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>1,3,4,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.4 | 0.9 | 18.6 |
| Cameron Johnson | 100% | 30.0<br><sub>29,31,30,31,27</sub> | 12.4<br><sub>18,8,23,12,9</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,2,4,5,0</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,1,3,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>2,2,4,1,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.3 | 1.0 | 18.4 |
| Aaron Gordon | 100% | 29.5<br><sub>27,30,27,33,24</sub> | 12.1<br><sub>12,3,9,11,11</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,5,3,5,1</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>0,2,2,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.4 | 1.2 | 19.6 |
| DeMar DeRozan | 91% | 20.1<br><sub>22,19,20,24,14</sub> | 9.3<br><sub>11,7,8,9,2</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,4,1,3,1</sub> |  | 2.6<br><sub>5,2,4,2,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 13.8 |
| Trevon Brazile | 98% | 17.8<br><sub>14,14,13,16,23</sub> | 5.2<br><sub>3,5,7,5,9</sub> | 5.5 · 5.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>4,2,5,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.4 | 0.3 | 0.7 | 9.9 |
| Spencer Jones | 86% | 16.4<br><sub>21,14,22,12,21</sub> | 4.1<br><sub>13,0,3,4,4</sub> | 3.5 · 3.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>6,0,1,2,3</sub> |  | 0.8<br><sub>0,1,0,1,3</sub> |  | 0.4<br><sub>3,0,1,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.2 |
| Marvin Bagley III | 98% | 12.5<br><sub>12,12,12,13,10</sub> | 5.8<br><sub>10,6,4,7,4</sub> |  | 3.7<br><sub>3,3,2,7,2</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 10.1 |
| Tyus Jones | 97% | 9.9<br><sub>13,6,11,10,10</sub> | 2.4<br><sub>3,2,0,2,0</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 1.7<br><sub>4,0,4,3,2</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.0 |
| Bryce Hopkins | 58% | 7.8<br><sub>3,3,-,-,4</sub> | 2.5<br><sub>3,2,-,-,0</sub> |  | 1.2<br><sub>1,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Zeke Nnaji | 26% | 6.4<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.6 |
| Alpha Diallo | 48% | 6.1<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### UTA @ LAL
Out: Austin Reaves (LAL), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ace Bailey 3PM over 2.5 (3+) | UTA @ LAL | draftkings | 2.48 | 2.36 | 2.95 | 33.9% | 43.9% | 42.4% | +5.0% | -16.1% | 0.9% |
| Darryn Peterson PTS under 18.5 | UTA @ LAL | tab | 1.95 | 1.92 | 1.72 | 58.0% | 50.9% | 52.0% | +1.6% | +13.2% | 0.4% |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 33.5<br><sub>-,33,38,34,35</sub> | 20.9<br><sub>-,13,27,13,30</sub> | 21.5 · 22.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.2 | 3.3 | 31.1 |
| Darryn Peterson | 98% | 32.7<br><sub>31,33,34,34,31</sub> | 18.0<br><sub>25,22,28,17,13</sub> | 18.5 · 18.5<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.9<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.6 | 2.2 | 26.4 |
| Ace Bailey | 99% | 31.5<br><sub>35,31,35,30,23</sub> | 14.6<br><sub>23,18,21,7,5</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,2,1,4,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>3,3,3,1,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.8 | 1.8 | 21.7 |
| Brice Sensabaugh | 99% | 26.5<br><sub>14,23,27,30,35</sub> | 15.7<br><sub>5,19,7,14,40</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>4,3,3,7,11</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>4,1,1,2,5</sub> |  | 2.3<br><sub>1,3,1,0,8</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 2.3 | 22.1 |
| Mo Bamba | 88% | 24.6<br><sub>17,18,20,36,31</sub> | 9.1<br><sub>7,5,9,26,15</sub> | – · 8.5<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>7,1,9,5,10</sub> |  | 1.2<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.5 | 1.1 | 18.1 |
| Josh Okogie | 97% | 22.4<br><sub>21,15,22,27,22</sub> | 6.1<br><sub>6,7,7,7,9</sub> | 5.5 · 5.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,3,2,6,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.3<br><sub>4,0,1,0,4</sub> |  | 0.7<br><sub>0,1,2,2,1</sub> |  | 1.1 | 0.2 | 0.9 | 10.8 |
| Jaxson Hayes | 76% | 21.9<br><sub>17,30,13,-,-</sub> | 8.2<br><sub>6,11,12,-,-</sub> |  | 5.2<br><sub>2,8,5,-,-</sub> |  | 1.1<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.7 | 0.8 | 1.0 | 14.5 |
| Svi Mykhailiuk | 97% | 20.1<br><sub>21,20,7,21,33</sub> | 7.3<br><sub>7,3,0,6,8</sub> |  | 2.2<br><sub>2,0,1,2,7</sub> |  | 1.6<br><sub>3,2,0,3,5</sub> |  | 1.2<br><sub>1,1,0,2,2</sub> |  | 0.6 | 0.1 | 0.8 | 11.1 |
| Josh Green | 96% | 18.1<br><sub>30,26,14,15,13</sub> | 4.1<br><sub>2,3,2,6,9</sub> | 4.5 · 4.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>5,2,0,1,1</sub> |  | 0.9<br><sub>4,1,0,1,0</sub> |  | 0.5<br><sub>0,1,0,2,1</sub> |  | 0.6 | 0.1 | 0.7 | 6.7 |
| Isaiah Collier | 63% | 16.4<br><sub>24,12,16,-,-</sub> | 7.9<br><sub>17,7,3,-,-</sub> |  | 2.3<br><sub>5,3,2,-,-</sub> |  | 4.2<br><sub>5,2,5,-,-</sub> |  | 0.4<br><sub>4,1,1,-,-</sub> |  | 0.7 | 0.2 | 1.6 | 14.4 |
| Tony Bradley | 72% | 13.7<br><sub>14,-,12,12,17</sub> | 4.4<br><sub>4,-,0,6,3</sub> |  | 4.0<br><sub>5,-,5,2,7</sub> |  | 0.6<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 9.0 |
| Kyle Filipowski | 52% | 12.1<br><sub>15,-,2,-,-</sub> | 6.0<br><sub>7,-,2,-,-</sub> |  | 3.6<br><sub>4,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.8 |
| Jonas Aidoo | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.7 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 34.5<br><sub>-,39,32,36,42</sub> | 39.9<br><sub>-,32,32,43,36</sub> | 36.5 · 37.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 8.0<br><sub>-,10,5,9,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.6 | 4.0 | 54.9 |
| Quentin Grimes | 98% | 29.4<br><sub>32,-,-,37,42</sub> | 12.9<br><sub>12,-,-,22,47</sub> | 16.5 · 15.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>1,-,-,6,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>4,-,-,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,-,-,5,10</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.4 | 1.5 | 19.5 |
| Walker Kessler | 98% | 28.4<br><sub>29,30,29,32,-</sub> | 12.2<br><sub>12,21,10,14,-</sub> | 13.5 · 13.5<br><sub>o 47% · u 53%</sub> | 11.8<br><sub>16,10,11,12,-</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>4,4,3,3,-</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 25.9 |
| Matisse Thybulle | 98% | 24.5<br><sub>28,23,23,26,31</sub> | 7.9<br><sub>4,6,8,12,7</sub> | 6.5 · 6.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>2,0,5,8,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.6 | 0.9 | 1.1 | 12.2 |
| Jake LaRavia | 98% | 23.1<br><sub>29,32,21,32,23</sub> | 6.6<br><sub>5,4,0,12,4</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,3,9,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.7 | 1.1 | 12.6 |
| Sandro Mamukelashvili | 99% | 22.1<br><sub>18,32,26,21,23</sub> | 10.5<br><sub>7,23,23,4,3</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,8,3,2,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.4<br><sub>1,5,5,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.5 | 0.8 | 17.1 |
| Ziaire Williams | 98% | 21.6<br><sub>21,28,20,19,24</sub> | 8.8<br><sub>17,12,9,6,0</sub> |  | 2.6<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> |  | 1.3 | 0.3 | 0.8 | 12.8 |
| Collin Sexton | 98% | 21.2<br><sub>24,27,13,24,25</sub> | 13.8<br><sub>17,18,10,16,10</sub> | 13.5 · 13.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.7 | 19.0 |
| Jarred Vanderbilt | 88% | 13.2<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.1<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.7 |
| Carson Cooper | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 8.2 |
| Kevon Looney | 52% | 9.9<br><sub>-,-,4,-,17</sub> | 2.2<br><sub>-,-,0,-,4</sub> |  | 3.8<br><sub>-,-,2,-,8</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 6.9 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Adou Thiero | 72% | 7.9<br><sub>8,7,14,-,6</sub> | 2.6<br><sub>2,2,2,-,0</sub> |  | 2.0<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Cameron Carr | 63% | 7.0<br><sub>-,7,13,-,-</sub> | 3.8<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Jaden Hardy | 48% | 7.0<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| Chris Manon | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.2 |
| Bronny James | 48% | 5.6<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.8 |

</details>


### PHX @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Cardwell PTS over 4.5 (5+) | PHX @ SAC | sportsbet | 2.05 | 2.01 | 1.82 | 55.1% | 48.7% | 49.7% | +1.8% | +12.9% | 0.4% |
| Zach LaVine PTS over 17.5 (18+) | PHX @ SAC | draftkings | 1.97 | 1.94 | 2.10 | 47.7% | 52.1% | 51.5% | +1.4% | -6.1% | 0.4% |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.6<br><sub>29,29,35,28,37</sub> | 26.8<br><sub>32,17,30,17,20</sub> | 26.5 · 26.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.2<br><sub>4,5,7,7,8</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>3,2,4,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.3 | 2.8 | 36.4 |
| Dillon Brooks | 98% | 29.0<br><sub>26,22,30,22,27</sub> | 16.1<br><sub>7,8,15,1,15</sub> | 13.5 · 13.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 1.4 | 21.5 |
| Miles Bridges | 98% | 28.2<br><sub>26,18,25,24,29</sub> | 14.5<br><sub>7,8,11,14,16</sub> | 14.5 · 14.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>5,4,6,3,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.5 | 1.2 | 23.1 |
| Jalen Green | 98% | 26.8<br><sub>24,21,21,21,27</sub> | 15.6<br><sub>6,13,12,9,16</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.3 | 2.0 | 22.2 |
| Oso Ighodaro | 98% | 25.4<br><sub>18,20,32,17,33</sub> | 6.7<br><sub>7,6,2,4,8</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.4 | 16.1 |
| Collin Gillespie | 98% | 25.3<br><sub>24,22,27,28,26</sub> | 10.5<br><sub>6,12,13,26,10</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,2,2,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.2 | 1.0 | 17.6 |
| Jordan Goodwin | 98% | 21.5<br><sub>-,14,24,31,20</sub> | 8.9<br><sub>-,18,6,14,11</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.2 | 0.8 | 15.6 |
| Luke Kennard | 98% | 18.5<br><sub>14,22,21,23,17</sub> | 7.8<br><sub>3,14,8,18,12</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,1,6,2</sub> |  | 1.9<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.7 | 11.7 |
| Ryan Dunn | 98% | 16.1<br><sub>23,25,10,24,12</sub> | 4.8<br><sub>3,10,0,3,5</sub> |  | 3.5<br><sub>2,8,4,6,1</sub> |  | 1.1<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.4 | 0.6 | 9.4 |
| Khaman Maluach | 98% | 14.9<br><sub>20,22,16,13,11</sub> | 5.5<br><sub>11,11,4,7,4</sub> |  | 4.8<br><sub>5,7,2,4,6</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.8 | 11.0 |
| Rasheer Fleming | 43% | 8.7<br><sub>9,12,-,-,-</sub> | 3.2<br><sub>2,4,-,-,-</sub> |  | 1.5<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.9 |
| Jamaree Bouyea | 48% | 7.3<br><sub>9,8,-,-,-</sub> | 3.0<br><sub>4,7,-,-,-</sub> |  | 1.0<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.1 |
| Koa Peat | 67% | 6.7<br><sub>6,6,-,8,1</sub> | 3.2<br><sub>4,5,-,10,0</sub> |  | 1.6<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 34.8<br><sub>33,39,40,35,33</sub> | 23.7<br><sub>22,32,29,17,26</sub> | 24.5 · 24.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>3,3,4,3,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 4.0 | 34.6 |
| Domantas Sabonis | 98% | 30.9<br><sub>31,-,24,35,29</sub> | 14.5<br><sub>17,-,0,21,11</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 11.8<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 0.3<br><sub>1,-,0,1,0</sub> |  | 0.8 | 0.3 | 2.6 | 31.6 |
| De'Andre Hunter | 76% | 30.7<br><sub>-,31,34,42,-</sub> | 13.7<br><sub>-,14,15,24,-</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>-,3,4,5,-</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>-,1,2,2,-</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>-,2,3,2,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.7 | 19.7 |
| Zach LaVine | 76% | 30.6<br><sub>35,25,33,36,-</sub> | 18.1<br><sub>14,15,31,12,-</sub> | 18.5 · 17.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,4,3,3,-</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 2.5 | 23.9 |
| Keegan Murray | 98% | 27.1<br><sub>-,23,24,40,21</sub> | 10.8<br><sub>-,10,11,16,6</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>-,1,2,7,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>-,2,1,4,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>-,0,2,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.9 | 1.0 | 16.3 |
| Precious Achiuwa | 98% | 23.5<br><sub>22,36,14,-,-</sub> | 10.1<br><sub>9,7,10,-,-</sub> | 8.5 · 7.5<br><sub>o 54% · u 46%</sub> | 6.4<br><sub>4,14,3,-,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,0,-,-</sub> |  | 0.3<br><sub>1,0,1,-,-</sub> |  | 0.9 | 0.8 | 1.2 | 17.7 |
| Leaky Black | 86% | 20.0<br><sub>40,20,18,12,29</sub> | 4.8<br><sub>12,6,0,0,12</sub> |  | 3.5<br><sub>3,5,3,0,9</sub> |  | 1.3<br><sub>5,1,2,0,2</sub> |  | 0.6<br><sub>4,2,0,0,4</sub> |  | 1.0 | 0.5 | 0.6 | 9.5 |
| Malik Monk | 98% | 17.9<br><sub>18,21,3,18,29</sub> | 9.8<br><sub>12,9,1,7,14</sub> |  | 1.9<br><sub>0,2,0,4,1</sub> |  | 3.5<br><sub>7,3,0,3,10</sub> |  | 1.2<br><sub>2,0,0,0,1</sub> |  | 0.5 | 0.3 | 1.5 | 15.2 |
| Dylan Cardwell | 98% | 17.0<br><sub>15,18,29,13,19</sub> | 5.5<br><sub>9,4,1,6,10</sub> | 4.5 · 4.5<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>2,9,11,3,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 13.2 |
| Emanuel Sharp | 98% | 15.5<br><sub>31,12,19,7,21</sub> | 4.7<br><sub>9,5,2,4,9</sub> |  | 1.5<br><sub>5,1,2,0,0</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>3,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.6 | 6.9 |
| Alex Karaban | 52% | 14.2<br><sub>11,-,-,-,29</sub> | 2.9<br><sub>0,-,-,-,0</sub> |  | 2.0<br><sub>1,-,-,-,5</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.6 |
| Daeqwon Plowden | 88% | 13.5<br><sub>-,12,2,2,24</sub> | 5.4<br><sub>-,6,0,0,13</sub> |  | 1.6<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.7<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.7 |
| Mason Plumlee | 52% | 6.5<br><sub>-,-,-,-,5</sub> | 2.0<br><sub>-,-,-,-,2</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 4.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-18/`._
