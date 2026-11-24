# NBA model · Mon 23 Nov 2026 (US date)

Updated **Tue 24 Nov, 01:23 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-23/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAS to win | SAS @ SAC | draftkings | 1.32 | 1.21 | 1.37 | 73.0% | 82.6% | 82.6% | +9.4% | -3.4% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PTS over 14.5 (15+) | SAS @ SAC | draftkings | 19.00 | 15.62 | 7.65 | 13.1% | 4.9% | 6.4% | +21.5% | +148.5% | 0.3% |
| Luka Doncic PRA over 69.5 (70+) | UTA @ LAL | draftkings | 14.60 | 12.22 | 6.17 | 16.2% | 6.4% | 8.2% | +19.4% | +136.7% | 0.4% |
| Keldon Johnson AST over 5.5 (6+) | SAS @ SAC | draftkings | 23.00 | 19.76 | 10.47 | 9.6% | 4.1% | 5.1% | +16.3% | +119.8% | 0.2% |
| Luka Doncic PRA over 64.5 (65+) | UTA @ LAL | draftkings | 8.00 | 7.23 | 4.25 | 23.5% | 11.7% | 13.8% | +10.6% | +88.3% | 0.4% |
| Jake LaRavia AST over 3.5 (4+) | UTA @ LAL | draftkings | 9.90 | 9.33 | 6.05 | 16.5% | 9.4% | 10.7% | +6.1% | +63.5% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Carter Bryant PTS over 7.5 (8+) | SAS @ SAC | pointsbetau | 2.05 | 1.93 | 1.43 | 69.8% | 47.9% | 51.8% | +6.2% | +43.0% | 1.5% |
| Mo Bamba PTS under 9.5 | UTA @ LAL | tab | 2.00 | 1.88 | 1.45 | 68.8% | 49.6% | 53.1% | +6.2% | +37.6% | 1.5% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| UTA @ LAL | Tue 24 Nov 14:00 | 108.5–123.5 | UTA 14% | 7.17 / 1.16 | LAL -15.5 | 232.5 | LAL -12.5 covers 57%; o224.5 66% |
| SAS @ SAC | Tue 24 Nov 14:00 | 117.5–108.7 | SAS 73% | 1.37 / 3.70 | SAC +8.5 | 226.5 | SAC +8.5 covers 49%; o223.5 56% |

### UTA @ LAL
Out: Austin Reaves (LAL), Jaxson Hayes (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brice Sensabaugh PTS over 11.5 (12+) | UTA @ LAL | pointsbetau | 2.05 | 2.00 | 1.65 | 60.6% | 47.5% | 49.9% | +2.3% | +24.2% | 0.5% |
| Darryn Peterson PTS under 17.5 | UTA @ LAL | tab | 1.95 | 1.91 | 1.71 | 58.4% | 51.0% | 52.4% | +2.2% | +14.1% | 0.6% |
| Walker Kessler PTS under 13.5 | UTA @ LAL | betright | 1.98 | 1.94 | 1.64 | 61.1% | 49.4% | 51.5% | +2.0% | +21.0% | 0.5% |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 33.3<br><sub>34,35,39,36,26</sub> | 21.0<br><sub>13,30,30,14,15</sub> | 20.5 · 21.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,2,1,3,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>8,11,10,6,7</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>1,4,5,0,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.8 | 0.2 | 3.4 | 31.3 |
| Ace Bailey | 99% | 31.3<br><sub>30,23,27,24,33</sub> | 15.2<br><sub>7,5,19,7,16</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>8,1,8,7,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>4,4,3,1,2</sub> |  | 2.1<br><sub>1,1,2,0,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.7 | 2.0 | 22.8 |
| Darryn Peterson | 99% | 31.1<br><sub>34,31,19,32,25</sub> | 16.9<br><sub>17,13,11,20,6</sub> | 16.5 · 17.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,5,1,10,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>4,2,3,8,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,2,1,0,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 2.4 | 25.6 |
| Svi Mykhailiuk | 98% | 27.0<br><sub>21,33,34,28,32</sub> | 11.5<br><sub>6,8,15,11,39</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,7,3,7,5</sub> |  | 2.3<br><sub>3,5,5,2,3</sub> |  | 2.1<br><sub>2,2,4,3,10</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.1 | 1.3 | 16.9 |
| Josh Green | 98% | 25.5<br><sub>15,13,28,29,23</sub> | 6.0<br><sub>6,9,11,8,0</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>1,0,2,0,0</sub> |  | 0.8<br><sub>2,1,2,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.9 | 0.2 | 0.9 | 9.8 |
| Brice Sensabaugh | 99% | 23.4<br><sub>30,35,14,26,17</sub> | 14.2<br><sub>14,40,8,18,10</sub> | 11.5 · 10.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>7,11,3,3,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,5,2,1,2</sub> |  | 2.2<br><sub>0,8,0,5,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.2 | 1.9 | 19.8 |
| Mo Bamba | 91% | 22.9<br><sub>36,31,23,20,23</sub> | 7.9<br><sub>26,15,6,2,6</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>5,10,16,2,10</sub> | 9.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>4,3,0,0,1</sub> |  | 0.5<br><sub>6,1,0,0,0</sub> |  | 0.6 | 1.2 | 1.1 | 16.6 |
| Josh Okogie | 98% | 21.4<br><sub>27,22,15,17,14</sub> | 6.1<br><sub>7,9,3,3,1</sub> |  | 3.2<br><sub>6,2,0,2,4</sub> |  | 1.2<br><sub>0,4,0,2,0</sub> |  | 0.7<br><sub>2,1,0,0,0</sub> |  | 1.1 | 0.2 | 0.9 | 10.6 |
| Isaiah Collier | 64% | 16.8<br><sub>-,-,10,-,13</sub> | 7.8<br><sub>-,-,0,-,10</sub> |  | 2.3<br><sub>-,-,1,-,2</sub> |  | 4.6<br><sub>-,-,2,-,7</sub> |  | 0.4<br><sub>-,-,0,-,1</sub> |  | 0.7 | 0.2 | 1.7 | 14.7 |
| Kyle Filipowski | 58% | 14.0<br><sub>-,-,6,-,9</sub> | 6.7<br><sub>-,-,0,-,2</sub> |  | 4.2<br><sub>-,-,3,-,4</sub> |  | 1.5<br><sub>-,-,0,-,3</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 1.0 | 12.3 |
| Tony Bradley | 58% | 13.6<br><sub>12,17,-,-,13</sub> | 3.9<br><sub>6,3,-,-,1</sub> |  | 4.2<br><sub>2,7,-,-,5</sub> |  | 0.6<br><sub>0,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.3 | 0.7 | 8.6 |
| Kobe Bufkin | 23% | 11.3<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.9 |
| Jonas Aidoo | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Harrison Ingram | 8% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 99% | 35.2<br><sub>32,36,42,37,36</sub> | 38.9<br><sub>32,43,36,29,25</sub> | 35.5 · 34.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>5,3,6,5,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 8.3<br><sub>5,9,7,7,8</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 4.6<br><sub>5,5,5,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.5 | 4.3 | 53.9 |
| Quentin Grimes | 99% | 31.2<br><sub>-,37,42,35,35</sub> | 14.0<br><sub>-,22,47,20,13</sub> | 16.5 · 16.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>-,6,6,7,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>-,1,3,4,7</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>-,5,10,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.5 | 21.4 |
| Walker Kessler | 99% | 29.4<br><sub>29,32,-,31,30</sub> | 12.6<br><sub>10,14,-,10,15</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 11.7<br><sub>11,12,-,11,7</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>3,3,-,1,2</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.9 | 2.4 | 1.5 | 26.2 |
| Matisse Thybulle | 98% | 24.6<br><sub>23,26,31,21,27</sub> | 7.6<br><sub>8,12,7,2,14</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>5,8,6,1,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>1,0,0,3,1</sub> |  | 1.3<br><sub>2,2,2,0,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.4 | 0.8 | 1.0 | 11.8 |
| Jake LaRavia | 98% | 24.3<br><sub>21,32,23,30,24</sub> | 6.7<br><sub>0,12,4,4,6</sub> | 5.5 · 5.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>9,3,5,6,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>6,3,2,2,0</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 1.3 | 0.6 | 1.0 | 12.9 |
| Ziaire Williams | 98% | 22.6<br><sub>20,19,24,18,28</sub> | 8.9<br><sub>9,6,0,7,5</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,2,1,2,0</sub> |  | 1.5<br><sub>5,3,1,0,1</sub> |  | 1.2<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 0.8 | 12.8 |
| Sandro Mamukelashvili | 99% | 21.0<br><sub>26,21,23,21,20</sub> | 9.8<br><sub>23,4,3,6,9</sub> | 9.5 · 8.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>3,2,3,3,9</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,3,2,0,2</sub> |  | 1.2<br><sub>5,0,0,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.5 | 0.8 | 16.2 |
| Collin Sexton | 99% | 20.4<br><sub>13,24,25,20,18</sub> | 12.9<br><sub>10,16,10,12,10</sub> | 11.5 · 11.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>1,0,4,0,1</sub> |  | 2.9<br><sub>3,3,3,1,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>0,2,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.1 | 1.6 | 17.9 |
| Jarred Vanderbilt | 91% | 12.4<br><sub>9,12,14,12,10</sub> | 3.1<br><sub>4,2,4,0,4</sub> |  | 3.9<br><sub>3,4,7,5,4</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.1 |
| Cameron Carr | 72% | 8.8<br><sub>13,-,-,2,12</sub> | 3.8<br><sub>0,-,-,5,5</sub> |  | 1.2<br><sub>2,-,-,0,1</sub> |  | 0.6<br><sub>0,-,-,1,0</sub> |  | 0.4<br><sub>0,-,-,1,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Kevon Looney | 38% | 7.9<br><sub>4,-,17,-,-</sub> | 1.6<br><sub>0,-,4,-,-</sub> |  | 3.0<br><sub>2,-,8,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.2 | 5.2 |
| Carson Cooper | 58% | 7.3<br><sub>-,-,18,2,-</sub> | 2.4<br><sub>-,-,3,2,-</sub> |  | 2.1<br><sub>-,-,4,1,-</sub> |  | 0.4<br><sub>-,-,2,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.0 |
| Adou Thiero | 64% | 7.3<br><sub>14,-,6,6,-</sub> | 2.5<br><sub>2,-,0,0,-</sub> |  | 1.8<br><sub>2,-,0,1,-</sub> |  | 0.6<br><sub>1,-,1,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |
| Jaden Hardy | 52% | 6.7<br><sub>4,-,-,2,-</sub> | 3.7<br><sub>3,-,-,0,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.6<br><sub>0,-,-,1,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Bronny James | 52% | 5.5<br><sub>4,-,-,2,-</sub> | 2.0<br><sub>4,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.5 |
| Chris Manon | 52% | 5.4<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.3 |

</details>


### SAS @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), De'Aaron Fox (SAS), Dylan Harper (SAS), Tobias Harris (SAS), Victor Wembanyama (SAS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. PTS under 23.5 | SAS @ SAC | tab | 1.95 | 1.93 | 1.81 | 55.1% | 51.2% | 51.9% | +1.4% | +7.6% | 0.4% |
| Harrison Barnes PTS over 9.5 (10+) | SAS @ SAC | tab | 2.00 | 1.98 | 1.74 | 57.4% | 48.9% | 50.4% | +0.9% | +14.8% | 0.2% |
| Stephon Castle PTS under 22.5 | SAS @ SAC | sportsbet | 1.96 | 1.95 | 1.90 | 52.7% | 51.0% | 51.3% | +0.6% | +3.3% | 0.1% |
| Harrison Barnes PTS over 10.5 (11+) | SAS @ SAC | sportsbet | 2.08 | 2.08 | 2.01 | 49.8% | 47.7% | 48.1% | +0.1% | +3.5% | 0.0% |
| Julian Champagnie PTS under 14.5 | SAS @ SAC | tab | 1.95 | 1.95 | 1.76 | 56.8% | 50.0% | 51.2% | +0.0% | +11.0% | 0.0% |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 99% | 32.5<br><sub>23,32,36,32,26</sub> | 18.1<br><sub>7,6,12,15,10</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>2,6,5,4,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,1,4,4,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.5 | 1.4 | 26.5 |
| Stephon Castle | 99% | 32.2<br><sub>25,35,31,33,29</sub> | 23.0<br><sub>32,20,10,21,19</sub> | 22.5 · 22.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>6,9,7,12,6</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>5,0,2,2,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.3 | 3.2 | 36.0 |
| Julian Champagnie | 99% | 29.7<br><sub>23,24,30,29,25</sub> | 14.3<br><sub>7,4,14,20,9</sub> | 14.5 · 14.5<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>8,5,6,4,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>3,1,0,1,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,1,4,4,3</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.5 | 1.0 | 21.5 |
| Keldon Johnson | 99% | 27.6<br><sub>25,29,15,27,23</sub> | 14.9<br><sub>18,11,4,10,10</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>4,10,2,5,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>4,2,1,3,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.4 | 23.8 |
| Harrison Barnes | 93% | 26.0<br><sub>21,14,10,16,21</sub> | 11.2<br><sub>11,0,0,9,3</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>1,0,3,2,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>1,2,4,1,2</sub> |  | 1.6<br><sub>3,0,0,1,0</sub> |  | 0.8 | 0.2 | 0.9 | 16.2 |
| Carter Bryant | 96% | 25.2<br><sub>19,5,2,13,20</sub> | 10.7<br><sub>8,0,0,3,8</sub> | – · 7.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>3,1,0,1,3</sub> |  | 1.8<br><sub>2,0,0,0,0</sub> |  | 1.6<br><sub>2,0,0,1,2</sub> |  | 0.6 | 0.5 | 1.1 | 16.5 |
| Jordan McLaughlin | 76% | 24.8<br><sub>14,19,-,11,18</sub> | 8.7<br><sub>4,10,-,0,0</sub> |  | 3.6<br><sub>6,1,-,1,3</sub> |  | 4.5<br><sub>2,2,-,5,2</sub> |  | 1.1<br><sub>0,2,-,0,0</sub> |  | 1.7 | 0.2 | 1.2 | 16.9 |
| Luke Kornet | 99% | 19.7<br><sub>16,13,14,15,10</sub> | 5.6<br><sub>6,2,2,4,0</sub> | 7.5 · 7.5<br><sub>o 45% · u 55%</sub> | 5.7<br><sub>7,2,1,0,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 0.7 | 13.1 |
| Tarris Reed Jr. | 58% | 17.5<br><sub>11,-,-,-,6</sub> | 6.4<br><sub>2,-,-,-,0</sub> |  | 6.9<br><sub>4,-,-,-,4</sub> |  | 1.1<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.5 | 1.0 | 14.4 |
| David Jones Garcia | 58% | 15.4<br><sub>-,-,-,-,4</sub> | 7.0<br><sub>-,-,-,-,0</sub> |  | 2.5<br><sub>-,-,-,-,1</sub> |  | 2.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 1.0 | 0.2 | 0.8 | 11.7 |
| Ja'Kobi Gillespie | 88% | 13.2<br><sub>-,-,-,-,-</sub> | 8.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.5 | 10.1 |
| Maliq Brown | 80% | 12.4<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.4 | 4.7 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 35.7<br><sub>35,33,35,36,40</sub> | 23.5<br><sub>17,26,36,18,21</sub> | 23.5 · 23.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.4<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.2 | 3.6 | 34.6 |
| De'Andre Hunter | 88% | 32.9<br><sub>42,-,35,37,41</sub> | 14.1<br><sub>24,-,7,30,20</sub> | 13.5 · 13.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>5,-,1,6,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.5 | 20.7 |
| Keegan Murray | 98% | 31.7<br><sub>40,21,31,40,40</sub> | 12.2<br><sub>16,6,12,13,15</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.9 | 0.9 | 19.1 |
| Zach LaVine | 88% | 31.5<br><sub>36,-,32,39,30</sub> | 16.8<br><sub>12,-,18,19,13</sub> | 16.5 · 17.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 2.0 | 23.0 |
| Domantas Sabonis | 99% | 31.0<br><sub>35,29,24,38,32</sub> | 14.6<br><sub>21,11,8,19,15</sub> | 13.5 · 14.5<br><sub>o 48% · u 52%</sub> | 11.8<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.3 | 2.2 | 31.3 |
| Precious Achiuwa | 98% | 21.4<br><sub>-,-,8,-,22</sub> | 9.0<br><sub>-,-,0,-,5</sub> | 5.5 · 5.5<br><sub>o 54% · u 46%</sub> | 5.6<br><sub>-,-,0,-,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.7 |
| Malik Monk | 98% | 14.4<br><sub>18,29,20,12,10</sub> | 7.5<br><sub>7,14,8,2,3</sub> |  | 1.3<br><sub>4,1,1,0,0</sub> |  | 2.6<br><sub>3,10,2,3,1</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.2 | 1.1 | 11.4 |
| Emanuel Sharp | 98% | 14.2<br><sub>7,21,14,10,16</sub> | 4.7<br><sub>4,9,6,3,3</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Leaky Black | 91% | 12.9<br><sub>12,29,17,19,4</sub> | 3.0<br><sub>0,12,3,0,2</sub> |  | 2.0<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.7 | 0.3 | 0.3 | 5.8 |
| Dylan Cardwell | 98% | 12.1<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.3<br><sub>3,6,4,4,1</sub> |  | 1.0<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 9.0 |
| Gabe Vincent | 5% | 9.3 | 2.7 |  | 0.8 |  | 1.0 |  | 0.3 |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Daeqwon Plowden | 58% | 7.8<br><sub>2,24,4,-,-</sub> | 2.9<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Alex Karaban | 48% | 7.5<br><sub>-,29,4,-,-</sub> | 1.5<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 2.9 |
| Mason Plumlee | 48% | 6.0<br><sub>-,5,4,-,-</sub> | 1.8<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-23/`._
