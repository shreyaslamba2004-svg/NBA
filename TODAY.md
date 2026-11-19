# NBA model · Wed 18 Nov 2026 (US date)

Updated **Thu 19 Nov, 12:39 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-18/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matisse Thybulle STL over 4.5 (5+) | UTA @ LAL | draftkings | 13.00 | 11.86 | 6.55 | 15.3% | 7.2% | 8.4% | +9.6% | +98.3% | 0.2% |
| Nikola Jokic AST over 15.5 (16+) | BOS @ DEN | draftkings | 22.00 | 20.24 | 11.47 | 8.7% | 4.2% | 4.9% | +8.6% | +91.7% | 0.1% |
| Nikola Jokic AST over 13.5 (14+) | BOS @ DEN | draftkings | 10.10 | 9.47 | 5.63 | 17.8% | 9.2% | 10.6% | +6.7% | +79.4% | 0.2% |
| Devin Booker AST over 9.5 (10+) | PHX @ SAC | draftkings | 15.00 | 14.08 | 8.42 | 11.9% | 6.2% | 7.1% | +6.5% | +78.2% | 0.1% |
| Matisse Thybulle STL over 5.5 (6+) | UTA @ LAL | draftkings | 23.00 | 21.69 | 13.14 | 7.6% | 4.1% | 4.6% | +6.0% | +75.1% | 0.1% |
| Matisse Thybulle STL over 3.5 (4+) | UTA @ LAL | draftkings | 6.20 | 5.85 | 3.56 | 28.1% | 15.1% | 17.1% | +5.9% | +74.2% | 0.3% |
| Devin Booker PRA over 54.5 (55+) | PHX @ SAC | draftkings | 22.00 | 20.92 | 13.04 | 7.7% | 4.2% | 4.8% | +5.1% | +68.7% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| BOS @ DEN | Thu 19 Nov 13:30 | 112.7–108.4 | BOS 61% | 1.63 / 2.59 | DEN +4.5 | 221.5 | DEN +2.5 covers 45%; o218.5 55% |
| UTA @ LAL | Thu 19 Nov 14:00 | 107.6–125.2 | UTA 11% | 9.47 / 1.12 | LAL -17.5 | 232.5 | LAL -11.5 covers 67%; o229.5 57% |
| PHX @ SAC | Thu 19 Nov 14:00 | 119.3–113.7 | PHX 66% | 1.52 / 2.92 | SAC +5.5 | 232.5 | SAC +7.5 covers 55%; o226.5 63% |

### BOS @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 33.8<br><sub>29,32,38,30,36</sub> | 24.0<br><sub>21,21,24,32,24</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>4,6,7,6,12</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>6,4,8,6,4</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>5,3,2,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.5 | 2.6 | 38.6 |
| Paul George | 98% | 30.2<br><sub>28,30,-,25,36</sub> | 18.0<br><sub>27,36,-,7,22</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>3,5,-,7,8</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.6<br><sub>1,1,-,6,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>5,6,-,1,5</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.4 | 2.0 | 26.6 |
| Derrick White | 98% | 30.0<br><sub>27,22,38,23,32</sub> | 12.6<br><sub>9,5,19,16,9</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>3,1,1,4,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.3<br><sub>7,3,7,2,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,1,3,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.8 | 1.3 | 20.3 |
| Payton Pritchard | 98% | 26.4<br><sub>29,30,31,19,32</sub> | 13.0<br><sub>12,18,14,10,21</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,6,1,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.8<br><sub>4,5,1,6,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>4,4,2,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.0 | 19.9 |
| Neemias Queta | 98% | 20.4<br><sub>22,22,31,15,-</sub> | 8.0<br><sub>13,4,11,8,-</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>9,6,13,6,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>4,3,3,2,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.5 | 0.9 | 0.9 | 16.2 |
| Sam Hauser | 98% | 20.1<br><sub>23,18,24,11,25</sub> | 7.9<br><sub>7,12,8,8,12</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,5,9,1,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,2,0,0,2</sub> |  | 1.5<br><sub>1,4,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.4 | 0.2 | 0.3 | 12.1 |
| Baylor Scheierman | 98% | 15.9<br><sub>19,18,29,18,11</sub> | 5.1<br><sub>7,5,9,12,0</sub> | 5.5 · –<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>1,3,7,5,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>0,2,3,3,1</sub> |  | 0.7<br><sub>1,1,3,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.6 | 0.1 | 0.5 | 9.3 |
| Mitchell Robinson | 98% | 15.4<br><sub>18,17,11,15,18</sub> | 4.4<br><sub>12,2,2,0,4</sub> |  | 5.8<br><sub>7,6,2,7,5</sub> |  | 0.7<br><sub>2,2,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 0.6 | 10.9 |
| Jordan Walsh | 98% | 14.1<br><sub>11,19,18,21,17</sub> | 4.3<br><sub>0,8,6,11,6</sub> |  | 2.6<br><sub>3,2,3,1,2</sub> |  | 0.7<br><sub>0,2,0,0,0</sub> |  | 0.5<br><sub>0,1,0,2,2</sub> |  | 0.5 | 0.3 | 0.4 | 7.6 |
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
| Nikola Jokic | 98% | 37.1<br><sub>36,39,37,37,38</sub> | 24.4<br><sub>19,25,27,26,28</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 11.9<br><sub>13,16,11,8,15</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 10.1<br><sub>8,9,8,10,7</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.8 | 3.7 | 46.4 |
| Jamal Murray | 98% | 37.0<br><sub>34,39,32,38,35</sub> | 23.0<br><sub>16,38,30,23,28</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>6,2,4,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>8,2,8,9,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>2,5,4,0,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.6 | 2.5 | 34.1 |
| Christian Braun | 98% | 32.8<br><sub>29,32,37,28,33</sub> | 12.0<br><sub>6,4,12,17,10</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>4,5,5,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,3,4,1,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.4 | 0.9 | 18.8 |
| Cameron Johnson | 98% | 29.9<br><sub>29,31,30,31,27</sub> | 12.3<br><sub>18,8,23,12,9</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>4,2,4,5,0</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,1,3,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.9<br><sub>2,2,4,1,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.3 | 1.0 | 18.3 |
| Aaron Gordon | 98% | 29.3<br><sub>27,30,27,33,24</sub> | 11.9<br><sub>12,3,9,11,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,5,3,5,1</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>0,2,2,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.4 | 1.2 | 19.4 |
| DeMar DeRozan | 91% | 20.3<br><sub>22,19,20,24,14</sub> | 9.5<br><sub>11,7,8,9,2</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,4,1,3,1</sub> |  | 2.6<br><sub>5,2,4,2,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 14.0 |
| Trevon Brazile | 98% | 17.8<br><sub>14,14,13,16,23</sub> | 5.2<br><sub>3,5,7,5,9</sub> | 5.5 · –<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>4,2,5,3,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.3 | 0.3 | 0.7 | 10.0 |
| Spencer Jones | 86% | 16.6<br><sub>21,14,22,12,21</sub> | 4.2<br><sub>13,0,3,4,4</sub> | 3.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>6,0,1,2,3</sub> |  | 0.8<br><sub>0,1,0,1,3</sub> |  | 0.5<br><sub>3,0,1,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.4 |
| Marvin Bagley III | 98% | 12.6<br><sub>12,12,12,13,10</sub> | 5.8<br><sub>10,6,4,7,4</sub> |  | 3.7<br><sub>3,3,2,7,2</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 10.2 |
| Tyus Jones | 97% | 10.0<br><sub>13,6,11,10,10</sub> | 2.5<br><sub>3,2,0,2,0</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 1.7<br><sub>4,0,4,3,2</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.1 |
| Bryce Hopkins | 58% | 8.0<br><sub>3,3,-,-,4</sub> | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Zeke Nnaji | 26% | 6.4<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.7 |
| Alpha Diallo | 48% | 6.1<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### UTA @ LAL
Out: Austin Reaves (LAL), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.6–125.2 | UTA 11% | 9.47 / 1.12 | LAL -17.5 | 232.5 | LAL -11.5 covers 67%; o229.5 57% |
| Expected (weighted by chance each plays) | 107.7–124.6 | UTA 11% | 8.74 / 1.13 | LAL -16.5 | 232.5 | LAL -11.5 covers 65%; o229.5 56% |
| if Jaxson Hayes plays | 107.7–124.4 | UTA 12% | 8.54 / 1.13 | LAL -16.5 | 232.5 | LAL -11.5 covers 64%; o229.5 56% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaxson Hayes (UTA) | Questionable | 55% | 21.9 | 8.2 | 5.2 | 1.1 | 0.0 | 0.7 | 0.8 | 1.0 | 14.6 | full tables below |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 33.9<br><sub>-,33,38,34,35</sub> | 21.1<br><sub>-,13,27,13,30</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 3.4 | 31.4 |
| Darryn Peterson | 98% | 33.5<br><sub>31,33,34,34,31</sub> | 18.4<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.6 | 2.2 | 26.9 |
| Ace Bailey | 99% | 32.5<br><sub>35,31,35,30,23</sub> | 15.6<br><sub>23,18,21,7,5</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>2,2,1,4,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.1<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.8 | 1.7 | 23.0 |
| Brice Sensabaugh | 99% | 29.0<br><sub>14,23,27,30,35</sub> | 16.7<br><sub>5,19,7,14,40</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,3,3,7,11</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>4,1,1,2,5</sub> |  | 2.6<br><sub>1,3,1,0,8</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.3 | 2.3 | 23.7 |
| Mo Bamba | 88% | 26.2<br><sub>17,18,20,36,31</sub> | 9.5<br><sub>7,5,9,26,15</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 8.4<br><sub>7,1,9,5,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.6 | 1.2 | 19.2 |
| Josh Okogie | 97% | 25.4<br><sub>21,15,22,27,22</sub> | 7.0<br><sub>6,7,7,7,9</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>4,3,2,6,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>4,0,1,0,4</sub> |  | 0.8<br><sub>0,1,2,2,1</sub> |  | 1.3 | 0.3 | 1.0 | 12.2 |
| Svi Mykhailiuk | 97% | 22.5<br><sub>21,20,7,21,33</sub> | 8.1<br><sub>7,3,0,6,8</sub> |  | 2.5<br><sub>2,0,1,2,7</sub> |  | 1.8<br><sub>3,2,0,3,5</sub> |  | 1.4<br><sub>1,1,0,2,2</sub> |  | 0.6 | 0.1 | 0.9 | 12.4 |
| Josh Green | 96% | 20.5<br><sub>30,26,14,15,13</sub> | 4.7<br><sub>2,3,2,6,9</sub> | 3.5 · –<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>5,2,0,1,1</sub> |  | 1.1<br><sub>4,1,0,1,0</sub> |  | 0.6<br><sub>0,1,0,2,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.7 |
| Isaiah Collier | 63% | 18.4<br><sub>24,12,16,-,-</sub> | 8.7<br><sub>17,7,3,-,-</sub> |  | 2.6<br><sub>5,3,2,-,-</sub> |  | 4.8<br><sub>5,2,5,-,-</sub> |  | 0.5<br><sub>4,1,1,-,-</sub> |  | 0.8 | 0.2 | 1.9 | 16.1 |
| Kyle Filipowski | 52% | 15.4<br><sub>15,-,2,-,-</sub> | 7.5<br><sub>7,-,2,-,-</sub> |  | 4.7<br><sub>4,-,0,-,-</sub> |  | 1.5<br><sub>1,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.7 | 0.2 | 1.1 | 13.7 |
| Tony Bradley | 72% | 15.3<br><sub>14,-,12,12,17</sub> | 4.8<br><sub>4,-,0,6,3</sub> |  | 4.4<br><sub>5,-,5,2,7</sub> |  | 0.7<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.4 | 0.7 | 9.9 |
| Jonas Aidoo | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 34.5<br><sub>-,39,32,36,42</sub> | 40.1<br><sub>-,32,32,43,36</sub> | 36.5 · –<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 8.0<br><sub>-,10,5,9,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.6 | 4.0 | 55.0 |
| Quentin Grimes | 98% | 29.3<br><sub>32,-,-,37,42</sub> | 12.9<br><sub>12,-,-,22,47</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>1,-,-,6,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>4,-,-,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,-,-,5,10</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.3 | 1.5 | 19.4 |
| Walker Kessler | 98% | 28.5<br><sub>29,30,29,32,-</sub> | 12.3<br><sub>12,21,10,14,-</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 11.8<br><sub>16,10,11,12,-</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>4,4,3,3,-</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 26.0 |
| Matisse Thybulle | 98% | 24.6<br><sub>28,23,23,26,31</sub> | 7.9<br><sub>4,6,8,12,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,0,5,8,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 2.7 | 0.9 | 1.1 | 12.2 |
| Jake LaRavia | 98% | 23.2<br><sub>29,32,21,32,23</sub> | 6.6<br><sub>5,4,0,12,4</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>1,3,9,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.7 | 1.1 | 12.7 |
| Sandro Mamukelashvili | 99% | 22.2<br><sub>18,32,26,21,23</sub> | 10.5<br><sub>7,23,23,4,3</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,8,3,2,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.4<br><sub>1,5,5,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.5 | 0.8 | 17.2 |
| Ziaire Williams | 98% | 21.6<br><sub>21,28,20,19,24</sub> | 8.8<br><sub>17,12,9,6,0</sub> |  | 2.6<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> |  | 1.3 | 0.3 | 0.8 | 12.8 |
| Collin Sexton | 98% | 21.1<br><sub>24,27,13,24,25</sub> | 13.8<br><sub>17,18,10,16,10</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.7 | 18.9 |
| Jarred Vanderbilt | 88% | 13.2<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.2<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.7 |
| Carson Cooper | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 8.2 |
| Kevon Looney | 52% | 10.0<br><sub>-,-,4,-,17</sub> | 2.3<br><sub>-,-,0,-,4</sub> |  | 3.9<br><sub>-,-,2,-,8</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 7.0 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.0 |
| Adou Thiero | 72% | 7.8<br><sub>8,7,14,-,6</sub> | 2.6<br><sub>2,2,2,-,0</sub> |  | 2.0<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Cameron Carr | 63% | 7.1<br><sub>-,7,13,-,-</sub> | 3.9<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.6 |
| Jaden Hardy | 48% | 7.1<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.4 |
| Chris Manon | 52% | 5.8<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.2 |
| Bronny James | 48% | 5.6<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.8 |

</details>

<details><summary>if Jaxson Hayes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 34.5<br><sub>-,39,32,36,42</sub> | 39.8<br><sub>-,32,32,43,36</sub> | 36.5 · –<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 8.0<br><sub>-,10,5,9,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.1<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.6 | 4.0 | 54.8 |
| Quentin Grimes (LAL) | 98% | 29.3<br><sub>32,-,-,37,42</sub> | 13.0<br><sub>12,-,-,22,47</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>1,-,-,6,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>4,-,-,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,-,-,5,10</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.3 | 1.5 | 19.6 |
| Walker Kessler (LAL) | 98% | 28.5<br><sub>29,30,29,32,-</sub> | 12.2<br><sub>12,21,10,14,-</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 11.8<br><sub>16,10,11,12,-</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>4,4,3,3,-</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 25.9 |
| Matisse Thybulle (LAL) | 98% | 24.4<br><sub>28,23,23,26,31</sub> | 7.8<br><sub>4,6,8,12,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,0,5,8,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 2.6 | 0.9 | 1.1 | 12.1 |
| Jake LaRavia (LAL) | 98% | 23.2<br><sub>29,32,21,32,23</sub> | 6.6<br><sub>5,4,0,12,4</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>1,3,9,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.7 | 1.1 | 12.6 |
| Sandro Mamukelashvili (LAL) | 99% | 22.1<br><sub>18,32,26,21,23</sub> | 10.4<br><sub>7,23,23,4,3</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,8,3,2,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.3<br><sub>1,5,5,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.5 | 0.8 | 17.0 |
| Ziaire Williams (LAL) | 98% | 21.6<br><sub>21,28,20,19,24</sub> | 8.7<br><sub>17,12,9,6,0</sub> |  | 2.6<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> |  | 1.4 | 0.3 | 0.8 | 12.8 |
| Collin Sexton (LAL) | 98% | 21.1<br><sub>24,27,13,24,25</sub> | 13.8<br><sub>17,18,10,16,10</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.7 | 19.0 |
| Jarred Vanderbilt (LAL) | 88% | 13.1<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.1<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Carson Cooper (LAL) | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 8.2 |
| Kevon Looney (LAL) | 52% | 9.9<br><sub>-,-,4,-,17</sub> | 2.2<br><sub>-,-,0,-,4</sub> |  | 3.9<br><sub>-,-,2,-,8</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 7.0 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| AK Okereke (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Adou Thiero (LAL) | 72% | 7.9<br><sub>8,7,14,-,6</sub> | 2.7<br><sub>2,2,2,-,0</sub> |  | 2.0<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Jaden Hardy (LAL) | 48% | 7.1<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Cameron Carr (LAL) | 63% | 7.0<br><sub>-,7,13,-,-</sub> | 3.8<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Chris Manon (LAL) | 52% | 5.9<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.3 |
| Bronny James (LAL) | 48% | 5.6<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.8 |
| Keyonte George (UTA) | 98% | 33.2<br><sub>-,33,38,34,35</sub> | 21.0<br><sub>-,13,27,13,30</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 6.4<br><sub>-,7,7,8,11</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 3.3 | 31.2 |
| Darryn Peterson (UTA) | 98% | 32.4<br><sub>31,33,34,34,31</sub> | 17.8<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.6 | 2.2 | 26.0 |
| Ace Bailey (UTA) | 99% | 31.2<br><sub>35,31,35,30,23</sub> | 14.5<br><sub>23,18,21,7,5</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,2,1,4,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.0<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.8 | 1.8 | 21.4 |
| Brice Sensabaugh (UTA) | 99% | 25.3<br><sub>14,23,27,30,35</sub> | 15.0<br><sub>5,19,7,14,40</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>4,3,3,7,11</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>4,1,1,2,5</sub> |  | 2.2<br><sub>1,3,1,0,8</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 2.1 | 21.0 |
| Mo Bamba (UTA) | 88% | 23.7<br><sub>17,18,20,36,31</sub> | 8.9<br><sub>7,5,9,26,15</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>7,1,9,5,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.4 | 1.1 | 17.6 |
| Josh Okogie (UTA) | 97% | 22.0<br><sub>21,15,22,27,22</sub> | 6.1<br><sub>6,7,7,7,9</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>4,3,2,6,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>4,0,1,0,4</sub> |  | 0.7<br><sub>0,1,2,2,1</sub> |  | 1.1 | 0.2 | 0.8 | 10.6 |
| Jaxson Hayes (UTA) | 100% | 21.9<br><sub>17,30,13,-,-</sub> | 8.2<br><sub>6,11,12,-,-</sub> |  | 5.2<br><sub>2,8,5,-,-</sub> |  | 1.1<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.7 | 0.8 | 1.0 | 14.6 |
| Svi Mykhailiuk (UTA) | 97% | 18.7<br><sub>21,20,7,21,33</sub> | 6.7<br><sub>7,3,0,6,8</sub> |  | 2.1<br><sub>2,0,1,2,7</sub> |  | 1.5<br><sub>3,2,0,3,5</sub> |  | 1.1<br><sub>1,1,0,2,2</sub> |  | 0.5 | 0.1 | 0.8 | 10.2 |
| Josh Green (UTA) | 96% | 17.1<br><sub>30,26,14,15,13</sub> | 3.8<br><sub>2,3,2,6,9</sub> | 3.5 · –<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>5,2,0,1,1</sub> |  | 0.9<br><sub>4,1,0,1,0</sub> |  | 0.4<br><sub>0,1,0,2,1</sub> |  | 0.6 | 0.1 | 0.6 | 6.3 |
| Isaiah Collier (UTA) | 63% | 15.5<br><sub>24,12,16,-,-</sub> | 7.2<br><sub>17,7,3,-,-</sub> |  | 2.2<br><sub>5,3,2,-,-</sub> |  | 4.1<br><sub>5,2,5,-,-</sub> |  | 0.4<br><sub>4,1,1,-,-</sub> |  | 0.7 | 0.2 | 1.6 | 13.5 |
| Tony Bradley (UTA) | 72% | 13.4<br><sub>14,-,12,12,17</sub> | 4.3<br><sub>4,-,0,6,3</sub> |  | 4.0<br><sub>5,-,5,2,7</sub> |  | 0.6<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.8 |
| Kyle Filipowski (UTA) | 52% | 11.5<br><sub>15,-,2,-,-</sub> | 5.7<br><sub>7,-,2,-,-</sub> |  | 3.5<br><sub>4,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.3 |
| Jonas Aidoo (UTA) | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.7 |

</details>


### PHX @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Mark Williams (PHX)

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.4<br><sub>29,29,35,28,37</sub> | 27.1<br><sub>32,17,30,17,20</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.2<br><sub>4,5,7,7,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>3,2,4,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 2.8 | 36.7 |
| Dillon Brooks | 98% | 29.0<br><sub>26,22,30,22,27</sub> | 16.1<br><sub>7,8,15,1,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 1.4 | 21.5 |
| Miles Bridges | 98% | 28.2<br><sub>26,18,25,24,29</sub> | 14.4<br><sub>7,8,11,14,16</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>5,4,6,3,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.5 | 1.2 | 23.0 |
| Jalen Green | 98% | 26.4<br><sub>24,21,21,21,27</sub> | 15.3<br><sub>6,13,12,9,16</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.3 | 2.0 | 21.9 |
| Oso Ighodaro | 98% | 24.9<br><sub>18,20,32,17,33</sub> | 6.5<br><sub>7,6,2,4,8</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 5.9<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.4 | 15.7 |
| Collin Gillespie | 98% | 24.9<br><sub>24,22,27,28,26</sub> | 10.3<br><sub>6,12,13,26,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,2,4,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.1 | 1.0 | 17.2 |
| Jordan Goodwin | 98% | 20.4<br><sub>-,14,24,31,20</sub> | 8.4<br><sub>-,18,6,14,11</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.2 | 0.8 | 14.8 |
| Luke Kennard | 98% | 17.7<br><sub>14,22,21,23,17</sub> | 7.4<br><sub>3,14,8,18,12</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,1,1,6,2</sub> |  | 1.8<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.6 | 11.1 |
| Ryan Dunn | 98% | 15.4<br><sub>23,25,10,24,12</sub> | 4.5<br><sub>3,10,0,3,5</sub> |  | 3.3<br><sub>2,8,4,6,1</sub> |  | 1.0<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.4 | 0.5 | 8.9 |
| Khaman Maluach | 98% | 14.4<br><sub>20,22,16,13,11</sub> | 5.4<br><sub>11,11,4,7,4</sub> |  | 4.7<br><sub>5,7,2,4,6</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 10.7 |
| Rasheer Fleming | 43% | 8.5<br><sub>9,12,-,-,-</sub> | 3.2<br><sub>2,4,-,-,-</sub> |  | 1.4<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Jamaree Bouyea | 48% | 6.9<br><sub>9,8,-,-,-</sub> | 2.9<br><sub>4,7,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.0 |
| Pat Spencer | 52% | 6.8<br><sub>6,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>2,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Koa Peat | 67% | 6.6<br><sub>6,6,-,8,1</sub> | 3.3<br><sub>4,5,-,10,0</sub> |  | 1.6<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| Duop Reath | 48% | 6.4<br><sub>6,-,-,-,-</sub> | 2.8<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>2,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.5 |
| Drew Timme | 8% | 6.3 | 2.6 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 34.8<br><sub>33,39,40,35,33</sub> | 23.8<br><sub>22,32,29,17,26</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 7.1<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>3,3,4,3,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.2 | 4.0 | 34.7 |
| Domantas Sabonis | 98% | 31.0<br><sub>31,-,24,35,29</sub> | 14.5<br><sub>17,-,0,21,11</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 11.9<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 0.3<br><sub>1,-,0,1,0</sub> |  | 0.8 | 0.3 | 2.6 | 31.6 |
| Zach LaVine | 76% | 30.7<br><sub>35,25,33,36,-</sub> | 18.1<br><sub>14,15,31,12,-</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>4,4,3,3,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.7<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 2.5 | 24.0 |
| De'Andre Hunter | 76% | 30.5<br><sub>-,31,34,42,-</sub> | 13.7<br><sub>-,14,15,24,-</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>-,3,4,5,-</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>-,1,2,2,-</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>-,2,3,2,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.7 | 19.7 |
| Keegan Murray | 98% | 27.1<br><sub>-,23,24,40,21</sub> | 10.8<br><sub>-,10,11,16,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>-,1,2,7,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>-,2,1,4,0</sub> |  | 1.3<br><sub>-,0,2,2,2</sub> |  | 0.8 | 0.9 | 1.1 | 16.4 |
| Precious Achiuwa | 98% | 23.5<br><sub>22,36,14,-,-</sub> | 10.1<br><sub>9,7,10,-,-</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>4,14,3,-,-</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,2,0,-,-</sub> |  | 0.3<br><sub>1,0,1,-,-</sub> |  | 0.9 | 0.8 | 1.2 | 17.8 |
| Leaky Black | 86% | 20.1<br><sub>40,20,18,12,29</sub> | 4.8<br><sub>12,6,0,0,12</sub> |  | 3.5<br><sub>3,5,3,0,9</sub> |  | 1.3<br><sub>5,1,2,0,2</sub> |  | 0.6<br><sub>4,2,0,0,4</sub> |  | 1.0 | 0.5 | 0.6 | 9.5 |
| Malik Monk | 98% | 17.9<br><sub>18,21,3,18,29</sub> | 9.8<br><sub>12,9,1,7,14</sub> |  | 1.9<br><sub>0,2,0,4,1</sub> |  | 3.5<br><sub>7,3,0,3,10</sub> |  | 1.2<br><sub>2,0,0,0,1</sub> |  | 0.5 | 0.3 | 1.5 | 15.2 |
| Dylan Cardwell | 98% | 17.1<br><sub>15,18,29,13,19</sub> | 5.6<br><sub>9,4,1,6,10</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>2,9,11,3,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 13.2 |
| Emanuel Sharp | 98% | 15.5<br><sub>31,12,19,7,21</sub> | 4.7<br><sub>9,5,2,4,9</sub> |  | 1.4<br><sub>5,1,2,0,0</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>3,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.6 | 6.9 |
| Alex Karaban | 52% | 14.1<br><sub>11,-,-,-,29</sub> | 2.9<br><sub>0,-,-,-,0</sub> |  | 2.0<br><sub>1,-,-,-,5</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.6 |
| Daeqwon Plowden | 88% | 13.4<br><sub>-,12,2,2,24</sub> | 5.4<br><sub>-,6,0,0,13</sub> |  | 1.6<br><sub>-,0,0,0,2</sub> |  | 0.6<br><sub>-,0,0,0,1</sub> |  | 0.7<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.6 |
| Mason Plumlee | 52% | 6.5<br><sub>-,-,-,-,5</sub> | 2.0<br><sub>-,-,-,-,2</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-18/`._
