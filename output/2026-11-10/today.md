# NBA model · Tue 10 Nov 2026 (US date)

Updated **Wed 11 Nov, 12:40 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-10/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ POR | draftkings | 14.40 | 12.32 | 5.30 | 18.9% | 6.5% | 8.1% | +17.0% | +171.8% | 0.3% |
| Giannis Antetokounmpo PTS over 49.5 (50+) | MIA @ UTA | draftkings | 31.00 | 28.49 | 14.85 | 6.7% | 3.0% | 3.5% | +8.7% | +108.8% | 0.1% |
| Giannis Antetokounmpo PA over 54.5 (55+) | MIA @ UTA | draftkings | 23.00 | 21.23 | 11.17 | 8.9% | 4.1% | 4.7% | +8.3% | +105.8% | 0.1% |
| Josh Okogie REB over 7.5 (8+) | MIA @ UTA | draftkings | 12.20 | 11.34 | 6.08 | 16.4% | 7.7% | 8.8% | +7.6% | +100.6% | 0.2% |
| Precious Achiuwa PRA over 24.5 (25+) | ORL @ SAC | draftkings | 9.20 | 8.56 | 4.61 | 21.7% | 10.2% | 11.7% | +7.5% | +99.6% | 0.2% |
| Giannis Antetokounmpo PA over 49.5 (50+) | MIA @ UTA | draftkings | 12.80 | 12.00 | 6.61 | 15.1% | 7.3% | 8.3% | +6.7% | +93.5% | 0.1% |
| Precious Achiuwa PTS over 14.5 (15+) | ORL @ SAC | draftkings | 8.70 | 8.16 | 4.50 | 22.2% | 10.7% | 12.2% | +6.6% | +93.2% | 0.2% |
| Damian Lillard AST over 7.5 (8+) | OKC @ POR | draftkings | 10.20 | 9.68 | 5.56 | 18.0% | 9.2% | 10.3% | +5.3% | +83.4% | 0.1% |
| Precious Achiuwa PRA over 29.5 (30+) | ORL @ SAC | draftkings | 20.60 | 19.57 | 11.27 | 8.9% | 4.5% | 5.1% | +5.2% | +82.8% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAC @ PHX | Wed 11 Nov 13:00 | 114.8–111.4 | LAC 60% | 1.67 / 2.48 | PHX +3.5 | 226.5 | PHX -3.5 covers 32%; o224.5 53% |
| MIA @ UTA | Wed 11 Nov 13:00 | 125.8–113.7 | MIA 81% | 1.24 / 5.14 | UTA +12.5 | 239.5 | UTA +8.5 covers 39%; o227.5 74% |
| ORL @ SAC | Wed 11 Nov 14:00 | 112.1–112.0 | ORL 50% | 1.98 / 2.02 | SAC +0.5 | 224.5 | SAC +5.5 covers 64%; o222.5 53% |
| OKC @ POR | Wed 11 Nov 15:00 | 114.0–109.2 | OKC 63% | 1.58 / 2.71 | POR +5.5 | 222.5 | POR +1.5 covers 40%; o226.5 43% |

### LAC @ PHX
Out: Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX), Bradley Beal (LAC), Brandon Ingram (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kobe Sanders PTS over 7.5 (8+) | LAC @ PHX | pointsbetau | 2.00 | 1.96 | 1.69 | 59.3% | 49.9% | 51.1% | +2.3% | +18.5% | 0.6% |
| Miles Bridges PTS under 16.5 | LAC @ PHX | betright | 1.90 | 1.89 | 1.53 | 65.5% | 51.0% | 52.9% | +0.7% | +24.4% | 0.2% |
| Khaman Maluach PTS over 6.5 (7+) | LAC @ PHX | pointsbetau | 2.05 | 2.04 | 2.22 | 45.1% | 49.5% | 48.9% | +0.4% | -7.6% | 0.1% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 31.7<br><sub>31,33,36,39,32</sub> | 21.3<br><sub>24,15,16,26,24</sub> | 21.5 · 21.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,0,4,1,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 6.8<br><sub>5,7,8,7,10</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 2.7<br><sub>4,1,1,4,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 3.6 | 30.3 |
| Rui Hachimura | 98% | 29.6<br><sub>26,30,-,37,26</sub> | 14.6<br><sub>12,24,-,21,14</sub> | 16.5 · 16.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>5,7,-,9,3</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>0,0,-,7,2</sub> |  | 1.8<br><sub>2,4,-,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.4 | 1.3 | 20.6 |
| Derrick Jones Jr. | 98% | 27.9<br><sub>26,28,-,37,29</sub> | 10.1<br><sub>10,9,-,12,8</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,7,-,8,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,1,-,1,3</sub> |  | 1.1<br><sub>2,1,-,2,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.8 | 1.0 | 15.6 |
| Kris Dunn | 98% | 26.6<br><sub>31,27,30,35,24</sub> | 7.5<br><sub>5,12,12,5,14</sub> | 7.5 · 7.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>5,2,4,5,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>7,4,1,3,4</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.8<br><sub>0,0,1,1,2</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 1.6 | 0.3 | 1.4 | 14.4 |
| Brook Lopez | 98% | 24.0<br><sub>21,19,22,35,26</sub> | 12.0<br><sub>13,7,12,20,20</sub> | 12.5 · 11.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,2,6,8,7</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 1.1 | 1.1 | 18.0 |
| Kobe Sanders | 98% | 21.9<br><sub>24,30,38,18,22</sub> | 9.3<br><sub>7,16,26,4,8</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,3,4,2,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,0,3,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>1,4,5,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.2 | 1.4 | 13.6 |
| Max Strus | 98% | 20.9<br><sub>-,-,23,23,19</sub> | 8.6<br><sub>-,-,11,9,7</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>-,-,4,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>-,-,6,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>-,-,3,3,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Keaton Wagler | 98% | 20.4<br><sub>25,19,24,16,18</sub> | 10.1<br><sub>12,7,6,11,15</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>6,4,4,2,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.9<br><sub>3,4,4,1,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,0,3,3</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.7 | 0.2 | 1.6 | 15.9 |
| Isaiah Jackson | 98% | 16.1<br><sub>22,22,26,13,-</sub> | 6.9<br><sub>10,5,19,2,-</sub> |  | 4.8<br><sub>7,8,8,4,-</sub> |  | 1.3<br><sub>4,2,2,2,-</sub> |  | 0.0<br><sub>0,0,1,0,-</sub> |  | 0.8 | 0.8 | 1.2 | 13.0 |
| Gradey Dick | 96% | 14.5<br><sub>12,3,29,7,17</sub> | 6.7<br><sub>3,0,12,4,15</sub> |  | 2.3<br><sub>0,1,4,2,4</sub> |  | 0.8<br><sub>1,0,3,1,0</sub> |  | 0.6<br><sub>1,0,0,0,2</sub> |  | 0.6 | 0.1 | 0.7 | 9.7 |
| Baba Miller | 91% | 14.2<br><sub>5,6,12,6,20</sub> | 6.3<br><sub>0,2,4,2,12</sub> |  | 2.3<br><sub>1,2,0,1,5</sub> |  | 1.6<br><sub>0,1,1,1,4</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.8 | 10.2 |
| Jalen Pickett | 52% | 6.8<br><sub>-,6,-,-,2</sub> | 2.6<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,2,-,-,0</sub> |  | 1.0<br><sub>-,3,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Blake Wesley | 52% | 6.1<br><sub>5,4,-,-,-</sub> | 2.6<br><sub>0,2,-,-,-</sub> |  | 0.8<br><sub>4,0,-,-,-</sub> |  | 0.9<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.3 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.8<br><sub>35,34,34,39,29</sub> | 25.5<br><sub>26,33,30,24,32</sub> | 26.5 · 25.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>3,1,1,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 5.8<br><sub>5,2,8,3,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>2,2,4,2,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.3 | 3.3 | 34.7 |
| Dillon Brooks | 98% | 31.3<br><sub>34,35,29,37,26</sub> | 16.8<br><sub>18,15,24,11,7</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>8,6,1,4,4</sub> |  | 1.9<br><sub>4,2,1,1,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 2.0<br><sub>2,0,4,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 1.6 | 22.5 |
| Miles Bridges | 98% | 31.1<br><sub>35,31,31,31,26</sub> | 14.7<br><sub>21,18,18,13,7</sub> | 16.5 · 16.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>6,7,13,10,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>3,5,5,7,0</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>3,4,3,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.5 | 1.4 | 24.3 |
| Jalen Green | 98% | 30.2<br><sub>36,32,24,34,24</sub> | 15.8<br><sub>11,22,6,16,6</sub> | 15.5 · 14.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>8,2,0,3,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.5<br><sub>8,2,3,6,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.3 | 2.6 | 23.2 |
| Collin Gillespie | 98% | 23.8<br><sub>24,23,24,20,24</sub> | 8.8<br><sub>3,2,6,7,6</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>1,3,2,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.7<br><sub>2,2,2,4,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>1,0,2,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2 | 0.1 | 1.2 | 15.4 |
| Oso Ighodaro | 98% | 21.5<br><sub>24,23,24,23,18</sub> | 6.3<br><sub>14,9,2,4,7</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>2,7,5,6,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,7,1,3,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.7 | 1.2 | 13.9 |
| Ryan Dunn | 98% | 18.5<br><sub>10,18,25,23,23</sub> | 5.3<br><sub>5,2,11,8,3</sub> |  | 3.7<br><sub>3,6,3,5,2</sub> |  | 1.2<br><sub>1,2,3,3,0</sub> |  | 0.6<br><sub>1,0,1,2,1</sub> |  | 0.7 | 0.5 | 0.6 | 10.2 |
| Khaman Maluach | 98% | 17.8<br><sub>13,16,22,18,20</sub> | 6.7<br><sub>5,6,8,8,11</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>2,6,6,10,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>0,2,2,0,2</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.4 | 0.9 | 1.1 | 13.0 |
| Luke Kennard | 98% | 16.9<br><sub>18,14,21,14,14</sub> | 6.2<br><sub>6,0,12,11,3</sub> |  | 1.8<br><sub>2,0,1,1,1</sub> |  | 1.7<br><sub>1,1,5,2,0</sub> |  | 0.8<br><sub>2,0,3,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.6 | 9.6 |
| Jordan Goodwin | 98% | 16.0<br><sub>10,-,-,-,-</sub> | 5.9<br><sub>4,-,-,-,-</sub> |  | 3.2<br><sub>2,-,-,-,-</sub> |  | 1.6<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 1.1 | 0.1 | 0.7 | 10.7 |
| Rasheer Fleming | 52% | 8.5<br><sub>-,-,-,-,9</sub> | 3.1<br><sub>-,-,-,-,2</sub> |  | 1.5<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Jamaree Bouyea | 63% | 7.6<br><sub>-,3,2,-,9</sub> | 2.8<br><sub>-,3,0,-,4</sub> |  | 1.0<br><sub>-,0,0,-,0</sub> |  | 1.0<br><sub>-,0,0,-,3</sub> |  | 0.2<br><sub>-,1,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.8 |
| Koa Peat | 58% | 6.8<br><sub>-,3,2,-,6</sub> | 2.3<br><sub>-,2,0,-,4</sub> |  | 1.4<br><sub>-,1,1,-,0</sub> |  | 0.3<br><sub>-,0,0,-,1</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.0 |

</details>


### MIA @ UTA
Out: Trey Alexander (UTA), Keyonte George (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 100% | 35.2<br><sub>35,29,43,38,40</sub> | 13.4<br><sub>15,15,11,22,17</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>6,0,2,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>11,7,10,8,11</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,4,0,4,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.3 | 2.1 | 24.4 |
| Bam Adebayo | 100% | 34.0<br><sub>33,31,41,33,34</sub> | 20.5<br><sub>27,16,35,18,18</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>9,9,10,10,8</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>3,4,4,0,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.5<br><sub>0,1,1,0,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.7 | 1.9 | 33.5 |
| Giannis Antetokounmpo | 100% | 33.9<br><sub>31,34,41,31,34</sub> | 30.5<br><sub>31,30,27,20,29</sub> | – · 28.5<br><sub>o 51% · u 49%</sub> | 12.4<br><sub>18,12,14,14,14</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>10,7,6,4,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.6<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 40% · u 60%</sub> | 1.1 | 1.0 | 3.4 | 49.1 |
| Pelle Larsson | 100% | 29.8<br><sub>24,30,35,29,22</sub> | 11.5<br><sub>18,9,7,13,11</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>3,3,3,1,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>3,2,4,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.0<br><sub>1,1,0,3,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1 | 0.2 | 1.6 | 18.8 |
| Klay Thompson | 100% | 27.1<br><sub>26,27,35,23,32</sub> | 13.8<br><sub>25,19,30,11,23</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>0,1,5,0,2</sub> |  | 2.0<br><sub>3,1,3,3,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>7,4,8,2,7</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.5 | 1.2 | 18.0 |
| Andrew Wiggins | 98% | 26.3<br><sub>30,24,23,21,32</sub> | 10.6<br><sub>12,7,3,2,6</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>2,0,4,6,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,2,1,4,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>2,2,1,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.9 | 1.2 | 16.3 |
| Bobby Portis | 98% | 19.1<br><sub>17,18,18,14,20</sub> | 8.4<br><sub>8,2,4,0,4</sub> | 8.5 · 7.5<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>3,3,10,5,1</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,2,5,0,1</sub> |  | 1.2<br><sub>2,0,0,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.3 | 0.7 | 15.2 |
| Ryan Conwell | 86% | 14.3<br><sub>7,8,17,30,19</sub> | 5.0<br><sub>4,5,0,13,6</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>0,1,2,1,2</sub> |  | 1.3<br><sub>0,1,2,2,2</sub> |  | 0.7<br><sub>1,1,0,3,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.6 | 0.1 | 0.6 | 7.8 |
| Tim Hardaway Jr. | 98% | 11.7<br><sub>12,19,7,4,7</sub> | 4.9<br><sub>2,9,0,0,0</sub> |  | 1.3<br><sub>1,0,0,0,0</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 0.7<br><sub>0,3,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.8 |
| Nikola Jovic | 58% | 9.3<br><sub>16,7,-,12,-</sub> | 3.3<br><sub>0,2,-,1,-</sub> |  | 1.8<br><sub>4,1,-,0,-</sub> |  | 0.9<br><sub>3,0,-,1,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Tre Donaldson | 5% | 8.4 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.1 | 0.4 | 6.1 |
| Dru Smith | 58% | 7.6<br><sub>4,11,-,1,-</sub> | 2.6<br><sub>0,3,-,0,-</sub> |  | 1.1<br><sub>0,3,-,0,-</sub> |  | 1.1<br><sub>1,2,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.7 | 0.1 | 0.4 | 4.8 |
| Simone Fontecchio | 48% | 7.1<br><sub>2,-,5,-,-</sub> | 3.9<br><sub>3,-,0,-,-</sub> |  | 1.2<br><sub>1,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.7 |
| Keshad Johnson | 16% | 6.4 | 3.2 |  | 1.3 |  | 0.3 |  | 0.2 |  | 0.4 | 0.2 | 0.3 | 4.8 |
| Nick Richards | 52% | 6.4<br><sub>2,1,-,1,-</sub> | 2.8<br><sub>0,0,-,0,-</sub> |  | 2.3<br><sub>0,1,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.4 |
| Myron Gardner | 52% | 6.1<br><sub>2,1,-,1,-</sub> | 2.7<br><sub>0,0,-,0,-</sub> |  | 1.8<br><sub>1,0,-,0,-</sub> |  | 0.7<br><sub>1,0,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.3 |
| Vladislav Goldin | 8% | 5.6 | 2.1 |  | 1.9 |  | 0.5 |  | 0.0 |  | 0.2 | 0.5 | 0.4 | 4.4 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darryn Peterson | 100% | 33.8<br><sub>36,33,30,30,35</sub> | 21.0<br><sub>16,14,7,21,26</sub> | 19.5 · 19.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>4,4,2,2,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>4,6,7,5,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>3,2,0,3,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.8 | 2.2 | 31.0 |
| Ace Bailey | 100% | 33.7<br><sub>37,24,35,29,32</sub> | 19.5<br><sub>9,5,15,12,7</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>7,6,5,6,2</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>1,2,1,0,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.5<br><sub>1,1,1,0,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.9 | 2.2 | 28.3 |
| Josh Green | 100% | 29.1<br><sub>2,15,23,24,28</sub> | 7.0<br><sub>0,3,7,3,10</sub> | 7.5 · 7.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>0,1,1,3,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,0,0,1,1</sub> |  | 1.0<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 1.2 | 11.4 |
| Jaxson Hayes | 100% | 29.0<br><sub>20,22,21,28,29</sub> | 11.3<br><sub>7,9,2,8,18</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>7,5,7,6,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>2,0,1,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.3 | 1.6 | 20.5 |
| Josh Okogie | 100% | 28.9<br><sub>14,19,26,24,17</sub> | 7.4<br><sub>0,9,3,12,0</sub> |  | 5.0<br><sub>1,3,6,4,1</sub> |  | 1.6<br><sub>0,2,1,0,0</sub> |  | 0.9<br><sub>0,1,1,2,0</sub> |  | 1.4 | 0.5 | 1.2 | 14.1 |
| Isaiah Collier | 98% | 22.1<br><sub>20,12,3,13,16</sub> | 12.0<br><sub>8,7,0,4,6</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>1,2,1,3,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>4,2,0,3,2</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 2.1 | 21.2 |
| Brice Sensabaugh | 98% | 21.6<br><sub>19,14,12,10,13</sub> | 15.0<br><sub>12,7,6,0,2</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>3,2,2,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,1,0,2,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>2,1,1,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.2 | 1.8 | 20.5 |
| Mo Bamba | 67% | 19.8<br><sub>11,18,15,-,17</sub> | 7.6<br><sub>6,8,7,-,3</sub> | – · 5.5<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>4,8,10,-,3</sub> |  | 0.9<br><sub>0,0,1,-,1</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.5 | 1.3 | 1.1 | 15.7 |
| Svi Mykhailiuk | 93% | 19.5<br><sub>18,14,17,14,6</sub> | 8.6<br><sub>6,3,6,0,0</sub> |  | 2.4<br><sub>1,2,3,0,0</sub> |  | 1.5<br><sub>3,0,0,1,0</sub> |  | 1.3<br><sub>2,1,0,0,0</sub> |  | 0.6 | 0.1 | 0.9 | 12.4 |
| Kyle Filipowski | 71% | 18.3<br><sub>6,8,-,1,15</sub> | 9.8<br><sub>5,1,-,0,9</sub> |  | 5.8<br><sub>0,2,-,0,6</sub> |  | 2.1<br><sub>2,0,-,0,1</sub> |  | 0.9<br><sub>1,0,-,0,1</sub> |  | 0.8 | 0.4 | 1.4 | 17.6 |
| Kobe Bufkin | 26% | 15.2<br><sub>-,-,-,-,-</sub> | 7.0<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.8 | 11.0 |
| Tony Bradley | 63% | 11.3<br><sub>-,7,-,1,2</sub> | 3.9<br><sub>-,2,-,0,0</sub> |  | 3.4<br><sub>-,3,-,1,1</sub> |  | 0.6<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.0 |
| Harrison Ingram | 16% | 8.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.8 |

</details>


### ORL @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Paolo Banchero (ORL), Tristan da Silva (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 36.6<br><sub>39,40,38,38,40</sub> | 25.7<br><sub>26,14,24,15,30</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>5,6,3,8,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>11,12,6,15,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>2,1,1,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.4 | 3.5 | 38.5 |
| Desmond Bane | 98% | 35.4<br><sub>39,40,36,32,-</sub> | 21.7<br><sub>28,19,20,15,-</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>2,2,3,6,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>6,1,3,0,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>6,5,4,3,-</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.5 | 2.5 | 29.6 |
| Wendell Carter Jr. | 98% | 34.9<br><sub>39,35,34,34,40</sub> | 15.0<br><sub>20,7,6,27,19</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 8.9<br><sub>7,10,9,13,11</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,2,3</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.9 | 1.9 | 26.2 |
| Anthony Black | 98% | 33.8<br><sub>31,33,-,31,38</sub> | 17.2<br><sub>17,23,-,10,18</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>6,8,-,7,8</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.9<br><sub>10,3,-,6,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,1,-,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0 | 0.8 | 2.3 | 26.6 |
| Jamal Cain | 98% | 30.3<br><sub>15,18,25,25,36</sub> | 12.1<br><sub>13,5,10,5,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>0,1,3,5,12</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>0,1,1,0,1</sub> |  | 1.5<br><sub>3,1,2,1,2</sub> |  | 0.9 | 0.4 | 1.4 | 18.6 |
| Jase Richardson | 93% | 27.9<br><sub>33,26,29,26,30</sub> | 10.1<br><sub>4,4,9,10,2</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>6,1,1,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.3<br><sub>2,3,5,3,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.3 | 1.2 | 16.1 |
| Jevon Carter | 67% | 16.5<br><sub>-,-,18,3,15</sub> | 6.1<br><sub>-,-,5,0,9</sub> |  | 1.5<br><sub>-,-,1,0,1</sub> |  | 1.9<br><sub>-,-,4,0,0</sub> |  | 1.0<br><sub>-,-,1,0,3</sub> |  | 0.8 | 0.2 | 0.6 | 9.5 |
| Alex Morales | 72% | 14.1<br><sub>9,-,14,6,15</sub> | 3.2<br><sub>0,-,3,0,0</sub> |  | 2.0<br><sub>1,-,2,0,2</sub> |  | 1.0<br><sub>0,-,0,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.2 | 0.8 | 6.2 |
| Goga Bitadze | 76% | 11.9<br><sub>6,5,-,8,7</sub> | 4.7<br><sub>2,0,-,4,4</sub> |  | 4.3<br><sub>4,1,-,5,5</sub> |  | 1.0<br><sub>0,0,-,0,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.8 | 0.6 | 10.0 |
| Nikola Vucevic | 98% | 11.2<br><sub>6,7,14,4,6</sub> | 4.5<br><sub>3,2,7,0,0</sub> |  | 3.1<br><sub>1,4,6,0,1</sub> |  | 1.3<br><sub>0,2,1,0,2</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 8.9 |
| Colin Castleton | 48% | 7.2<br><sub>-,-,-,2,-</sub> | 2.4<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.0 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 34.9<br><sub>37,37,42,33,39</sub> | 24.3<br><sub>38,25,22,22,32</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,5,3,3,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 7.4<br><sub>5,6,12,8,10</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>9,2,3,3,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.2 | 3.4 | 35.3 |
| Domantas Sabonis | 98% | 31.2<br><sub>38,31,35,31,-</sub> | 14.7<br><sub>11,9,16,17,-</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 12.1<br><sub>14,7,17,12,-</sub> | 12.5<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>8,4,1,5,-</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 0.2<br><sub>0,0,0,1,-</sub> |  | 0.8 | 0.3 | 2.7 | 32.1 |
| Zach LaVine | 98% | 30.6<br><sub>21,28,35,35,25</sub> | 18.1<br><sub>11,23,21,14,15</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>0,4,4,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,1,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>0,5,3,1,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.3 | 2.2 | 23.6 |
| De'Andre Hunter | 98% | 28.8<br><sub>32,36,38,-,31</sub> | 12.8<br><sub>19,6,14,-,14</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>3,7,2,-,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,2,2,-,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>2,0,1,-,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.4 | 18.5 |
| Keegan Murray | 98% | 26.7<br><sub>-,-,-,-,23</sub> | 10.0<br><sub>-,-,-,-,10</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>-,-,-,-,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>-,-,-,-,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1<br><sub>-,-,-,-,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.8 | 1.0 | 0.9 | 15.4 |
| Precious Achiuwa | 98% | 26.2<br><sub>25,27,17,22,36</sub> | 10.9<br><sub>6,6,7,9,7</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 7.0<br><sub>5,10,3,4,14</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,3,1,0,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.3<br><sub>0,0,1,1,0</sub> |  | 1.0 | 1.0 | 1.3 | 19.4 |
| Leaky Black | 67% | 19.7<br><sub>-,25,22,40,20</sub> | 4.5<br><sub>-,12,3,12,6</sub> |  | 3.2<br><sub>-,3,6,3,5</sub> |  | 1.3<br><sub>-,1,1,5,1</sub> |  | 0.6<br><sub>-,4,0,4,2</sub> |  | 0.9 | 0.5 | 0.7 | 9.0 |
| Malik Monk | 98% | 18.3<br><sub>14,30,24,18,21</sub> | 9.5<br><sub>8,24,13,12,9</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,1,2,0,2</sub> |  | 3.2<br><sub>3,7,3,7,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,5,3,2,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.3 | 1.4 | 14.3 |
| Dylan Cardwell | 98% | 15.7<br><sub>-,-,13,15,18</sub> | 4.4<br><sub>-,-,4,9,4</sub> |  | 5.7<br><sub>-,-,6,2,9</sub> |  | 1.4<br><sub>-,-,0,3,3</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 11.4 |
| Emanuel Sharp | 98% | 13.8<br><sub>24,20,10,31,12</sub> | 3.7<br><sub>2,9,3,9,5</sub> |  | 1.2<br><sub>1,3,1,5,1</sub> |  | 0.7<br><sub>1,1,2,0,0</sub> |  | 0.4<br><sub>0,3,1,3,1</sub> |  | 0.5 | 0.2 | 0.5 | 5.6 |
| Daeqwon Plowden | 67% | 10.9<br><sub>4,3,-,-,12</sub> | 3.8<br><sub>4,1,-,-,6</sub> |  | 1.1<br><sub>0,1,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.4<br><sub>0,0,-,-,2</sub> |  | 0.4 | 0.1 | 0.4 | 5.5 |
| Alex Karaban | 52% | 6.8<br><sub>10,-,-,11,-</sub> | 2.3<br><sub>0,-,-,0,-</sub> |  | 0.9<br><sub>1,-,-,1,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.6 |

</details>


### OKC @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.7<br><sub>31,39,35,30,29</sub> | 30.6<br><sub>26,43,42,28,30</sub> | 32.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>4,3,4,3,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.9<br><sub>3,8,8,4,9</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,4,5,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5 | 1.0 | 3.0 | 41.3 |
| Ajay Mitchell | 98% | 28.6<br><sub>26,35,32,30,22</sub> | 17.1<br><sub>6,20,23,35,12</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>3,5,7,1,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,1,4,5,0</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>0,0,1,4,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.4 | 0.4 | 1.9 | 24.4 |
| Jared McCain | 98% | 26.6<br><sub>28,27,25,29,23</sub> | 12.9<br><sub>10,7,9,21,19</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>4,9,1,5,5</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>2,2,0,0,2</sub> |  | 1.8<br><sub>0,0,1,3,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 1.7 | 17.8 |
| Isaiah Hartenstein | 98% | 26.2<br><sub>25,28,26,26,18</sub> | 9.5<br><sub>10,5,3,2,2</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 10.2<br><sub>7,14,12,6,14</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 3.6<br><sub>0,4,4,7,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.3 | 0.8 | 1.6 | 23.2 |
| Aday Mara | 98% | 24.0<br><sub>28,20,25,18,27</sub> | 9.7<br><sub>7,10,9,9,18</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>9,9,5,7,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>3,0,2,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.5 | 1.8 | 1.7 | 18.1 |
| Bennett Stirtz | 98% | 23.8<br><sub>26,12,22,24,29</sub> | 8.0<br><sub>11,9,16,12,11</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,2,1,1,5</sub> |  | 1.6<br><sub>3,0,1,2,3</sub> |  | 1.3<br><sub>3,3,4,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.2 | 0.9 | 11.5 |
| Kenrich Williams | 98% | 23.4<br><sub>21,31,29,19,23</sub> | 8.3<br><sub>11,12,13,4,9</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>7,3,4,6,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>3,1,2,3,2</sub> |  | 1.1<br><sub>3,2,3,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 0.9 | 14.9 |
| Alex Caruso | 98% | 20.9<br><sub>-,-,20,20,13</sub> | 7.4<br><sub>-,-,7,5,0</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>-,-,4,6,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>-,-,3,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0<br><sub>-,-,1,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.4 | 0.9 | 13.1 |
| Micah Peavy | 86% | 20.8<br><sub>14,16,26,18,23</sub> | 5.5<br><sub>2,8,2,7,7</sub> |  | 3.8<br><sub>1,5,9,4,3</sub> |  | 1.1<br><sub>0,0,1,0,0</sub> |  | 0.6<br><sub>0,2,0,1,1</sub> |  | 0.8 | 0.3 | 0.7 | 10.4 |
| Josh Dix | 76% | 18.5<br><sub>9,12,-,15,21</sub> | 4.3<br><sub>7,0,-,5,2</sub> |  | 1.7<br><sub>0,1,-,2,1</sub> |  | 0.8<br><sub>0,0,-,1,2</sub> |  | 0.4<br><sub>1,0,-,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 6.8 |
| Brooks Barnhizer | 67% | 10.2<br><sub>6,-,-,5,8</sub> | 2.5<br><sub>5,-,-,0,2</sub> |  | 2.2<br><sub>2,-,-,0,4</sub> |  | 0.7<br><sub>0,-,-,0,3</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.4 |
| Nique Clifford | 91% | 9.9<br><sub>11,3,3,5,-</sub> | 3.5<br><sub>0,0,0,5,-</sub> |  | 1.5<br><sub>1,1,2,2,-</sub> |  | 1.1<br><sub>2,0,0,2,-</sub> |  | 0.2<br><sub>0,0,0,1,-</sub> |  | 0.5 | 0.1 | 0.6 | 6.2 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 33.2<br><sub>30,35,35,39,24</sub> | 20.5<br><sub>24,28,21,22,15</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>5,3,7,9,4</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>2,5,12,11,1</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 3.7 | 33.6 |
| Damian Lillard | 98% | 30.5<br><sub>27,30,33,37,20</sub> | 16.6<br><sub>22,20,25,22,12</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>5,6,3,0,0</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>4,6,5,4,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,1,2,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.2 | 2.5 | 25.4 |
| Toumani Camara | 98% | 29.3<br><sub>31,31,32,30,21</sub> | 11.7<br><sub>14,9,11,18,4</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>4,5,4,6,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,1,2,1,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>4,3,1,4,0</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.4 | 1.5 | 17.6 |
| Jrue Holiday | 98% | 27.6<br><sub>22,31,28,31,20</sub> | 12.8<br><sub>14,17,15,12,11</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>4,8,4,1,0</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.6<br><sub>3,10,0,7,0</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,3,5,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.2 | 2.0 | 21.4 |
| Donovan Clingan | 98% | 25.8<br><sub>15,32,29,28,22</sub> | 11.2<br><sub>4,17,24,17,6</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 10.0<br><sub>9,18,11,11,5</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,3,1,1,0</sub> |  | 1.1<br><sub>0,1,1,3,0</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.5 | 1.4 | 1.4 | 22.9 |
| Scoot Henderson | 98% | 25.2<br><sub>31,26,22,23,24</sub> | 11.3<br><sub>14,8,9,2,13</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>1,2,1,0,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>1,2,1,0,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 2.4 | 16.4 |
| Sidy Cissoko | 98% | 19.8<br><sub>19,22,21,22,16</sub> | 5.8<br><sub>1,8,7,7,4</sub> |  | 2.7<br><sub>3,3,4,2,3</sub> |  | 1.7<br><sub>1,0,4,3,1</sub> |  | 0.6<br><sub>0,2,1,2,0</sub> |  | 0.7 | 0.3 | 0.9 | 10.1 |
| Chris Youngblood | 88% | 19.5<br><sub>7,15,4,11,30</sub> | 7.8<br><sub>3,7,0,7,11</sub> |  | 2.4<br><sub>0,2,0,1,4</sub> |  | 1.5<br><sub>0,1,1,0,4</sub> |  | 1.4<br><sub>1,1,0,2,2</sub> |  | 0.5 | 0.3 | 0.8 | 11.7 |
| Robert Williams III | 98% | 16.0<br><sub>14,15,16,16,-</sub> | 6.0<br><sub>3,2,9,9,-</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>3,6,8,5,-</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,2,1,2,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 1.0 | 0.8 | 13.1 |
| Yang Hansen | 72% | 12.4<br><sub>13,-,2,3,26</sub> | 5.0<br><sub>6,-,0,2,12</sub> |  | 3.2<br><sub>5,-,0,0,10</sub> |  | 0.7<br><sub>1,-,0,0,1</sub> |  | 0.4<br><sub>2,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.9 | 8.9 |
| Micah Potter | 63% | 10.8<br><sub>4,-,2,-,14</sub> | 4.6<br><sub>2,-,4,-,7</sub> |  | 2.8<br><sub>1,-,1,-,3</sub> |  | 0.6<br><sub>0,-,0,-,1</sub> |  | 0.5<br><sub>0,-,1,-,1</sub> |  | 0.2 | 0.2 | 0.7 | 8.0 |
| Branden Carlson | 58% | 9.2<br><sub>4,-,3,-,12</sub> | 2.9<br><sub>0,-,2,-,4</sub> |  | 1.9<br><sub>2,-,0,-,2</sub> |  | 0.5<br><sub>1,-,0,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.4 | 0.5 | 5.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-10/`._
