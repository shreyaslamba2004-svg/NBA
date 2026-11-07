# NBA model · Fri 06 Nov 2026 (US date)

Updated **Sat 07 Nov, 01:11 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-06/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | SAS @ SAC | sportsbet | 10.00 | 8.94 | 5.46 | 18.3% | 11.2% | 11.2% | +11.8% | +83.2% | 0.3% |
| Darius Acuff Jr. AST over 11.5 (12+) | SAS @ SAC | draftkings | 17.00 | 15.95 | 6.34 | 15.8% | 5.5% | 6.3% | +6.6% | +168.3% | 0.1% |
| Precious Achiuwa PRA over 29.5 (30+) | SAS @ SAC | draftkings | 16.80 | 15.87 | 6.48 | 15.4% | 5.6% | 6.3% | +5.9% | +159.4% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| POR @ LAL | Sat 07 Nov 14:00 | 110.5–116.3 | POR 34% | 2.95 / 1.51 | LAL -6.5 | 226.5 | LAL -3.5 covers 57%; o231.5 39% |
| SAS @ SAC | Sat 07 Nov 14:00 | 120.9–108.1 | SAS 82% | 1.22 / 5.46 | SAC +12.5 | 228.5 | SAC +17.5 covers 63%; o231.5 44% |

### POR @ LAL
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.4<br><sub>33,32,30,35,35</sub> | 23.3<br><sub>23,24,24,28,21</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>4,9,5,3,7</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>9,7,2,5,12</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>4,0,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.4 | 3.9 | 36.5 |
| Damian Lillard | 98% | 32.9<br><sub>31,30,27,30,33</sub> | 19.2<br><sub>21,9,22,20,25</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,2,4,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,1,3,1,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.7 | 29.0 |
| Toumani Camara | 98% | 31.4<br><sub>24,26,31,31,32</sub> | 12.2<br><sub>12,13,14,9,11</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>1,2,4,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>4,3,4,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.3 | 1.5 | 18.2 |
| Jrue Holiday | 98% | 30.2<br><sub>30,24,22,31,28</sub> | 14.2<br><sub>22,6,14,17,15</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>4,6,4,8,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.4<br><sub>3,4,3,10,0</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,2,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 2.5 | 24.1 |
| Donovan Clingan | 98% | 26.7<br><sub>26,29,15,32,29</sub> | 11.4<br><sub>9,11,4,17,24</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 10.3<br><sub>10,8,9,18,11</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>2,1,0,1,1</sub> |  | 0.7 | 1.4 | 1.4 | 23.6 |
| Scoot Henderson | 98% | 25.8<br><sub>17,19,31,26,22</sub> | 11.9<br><sub>2,9,14,8,9</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,0,1,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,1,1,2,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.4 | 17.3 |
| Sidy Cissoko | 97% | 21.6<br><sub>20,19,19,22,21</sub> | 5.7<br><sub>6,4,1,8,7</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>2,6,3,3,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>4,2,1,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>0,0,0,2,1</sub> |  | 0.9 | 0.3 | 1.0 | 10.5 |
| Robert Williams III | 98% | 17.7<br><sub>21,-,14,15,16</sub> | 6.7<br><sub>14,-,3,2,9</sub> | 5.5 · –<br><sub>o 56% · u 44%</sub> | 6.7<br><sub>10,-,3,6,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,-,1,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.8 | 1.0 | 0.9 | 14.5 |
| Chris Youngblood | 86% | 10.2<br><sub>-,-,7,15,4</sub> | 3.8<br><sub>-,-,3,7,0</sub> |  | 1.3<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |
| Micah Potter | 64% | 7.9<br><sub>-,9,4,-,2</sub> | 3.3<br><sub>-,1,2,-,4</sub> |  | 2.1<br><sub>-,2,1,-,1</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.8 |
| Branden Carlson | 58% | 7.7<br><sub>-,12,4,-,3</sub> | 2.1<br><sub>-,2,0,-,2</sub> |  | 1.7<br><sub>-,2,2,-,0</sub> |  | 0.5<br><sub>-,1,1,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |
| Yang Hansen | 63% | 7.4<br><sub>-,5,13,-,2</sub> | 2.8<br><sub>-,3,6,-,0</sub> |  | 1.7<br><sub>-,2,5,-,0</sub> |  | 0.4<br><sub>-,1,1,-,0</sub> |  | 0.2<br><sub>-,1,2,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.9 |
| Jayson Kent | 71% | 6.6<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 35.5<br><sub>-,37,35,36,35</sub> | 33.6<br><sub>-,37,45,42,40</sub> | 35.5 · –<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>-,7,15,7,9</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>-,5,6,13,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>-,6,8,6,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8 | 0.6 | 4.2 | 48.6 |
| Austin Reaves | 98% | 34.8<br><sub>31,37,39,34,37</sub> | 20.7<br><sub>16,21,19,27,21</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,4,3,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>1,5,4,5,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 3.2 | 29.7 |
| Walker Kessler | 98% | 28.7<br><sub>26,31,31,32,29</sub> | 11.8<br><sub>11,10,16,15,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 10.5<br><sub>9,13,15,15,8</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,2,1,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.1 | 1.5 | 23.7 |
| Quentin Grimes | 98% | 23.3<br><sub>38,26,26,23,25</sub> | 7.6<br><sub>23,3,7,7,6</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,3,1,4,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>5,2,3,4,1</sub> |  | 0.8<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.3 | 1.2 | 12.3 |
| Ziaire Williams | 96% | 21.5<br><sub>-,-,-,15,23</sub> | 7.7<br><sub>-,-,-,9,10</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>-,-,-,2,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>-,-,-,2,1</sub> |  | 0.9<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 0.9 | 11.5 |
| Sandro Mamukelashvili | 98% | 20.4<br><sub>30,20,24,28,19</sub> | 8.4<br><sub>13,4,11,13,2</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>8,7,1,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>3,0,1,4,1</sub> |  | 0.9<br><sub>0,0,2,2,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 0.5 | 0.8 | 14.3 |
| Matisse Thybulle | 98% | 20.1<br><sub>28,28,25,19,23</sub> | 5.7<br><sub>15,10,6,6,3</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,3,2,1,1</sub> |  | 1.1<br><sub>0,0,3,2,2</sub> |  | 0.8<br><sub>4,1,2,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.7 | 0.8 | 8.7 |
| Jake LaRavia | 96% | 20.0<br><sub>35,28,25,26,21</sub> | 5.5<br><sub>2,10,8,7,9</sub> | 4.5 · –<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>10,2,2,4,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,0,4,2,2</sub> |  | 0.5<br><sub>0,2,2,1,2</sub> |  | 1.1 | 0.6 | 1.1 | 9.9 |
| Collin Sexton | 98% | 16.6<br><sub>21,16,19,16,16</sub> | 9.9<br><sub>21,0,14,6,10</sub> |  | 1.8<br><sub>4,2,3,1,3</sub> |  | 1.8<br><sub>2,1,3,5,1</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 0.8 | 0.2 | 1.4 | 13.6 |
| Jarred Vanderbilt | 72% | 9.3<br><sub>21,13,12,6,7</sub> | 2.7<br><sub>0,0,4,2,0</sub> |  | 2.4<br><sub>7,3,3,1,1</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 5.8 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Lawson Lovering | 91% | 6.7<br><sub>-,-,-,1,1</sub> | 2.0<br><sub>-,-,-,0,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.3 |
| Jaden Hardy | 80% | 6.4<br><sub>9,1,1,1,1</sub> | 3.4<br><sub>2,0,1,2,0</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.6<br><sub>2,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.0 | 0.4 | 4.5 |
| Kevon Looney | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.3 |
| Adou Thiero | 16% | 5.6 | 2.0 |  | 1.4 |  | 0.4 |  | 0.0 |  | 0.2 | 0.1 | 0.5 | 3.8 |
| Chris Manon | 58% | 5.3<br><sub>-,1,-,-,-</sub> | 1.8<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.1 |

</details>


### SAS @ SAC
Out: De'Andre Hunter (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 32.8<br><sub>27,39,34,24,34</sub> | 28.2<br><sub>29,36,43,12,52</sub> | 28.5 · –<br><sub>o 48% · u 52%</sub> | 11.3<br><sub>10,14,7,11,24</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,5,4,5,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>0,4,3,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 3.9 | 2.5 | 43.0 |
| Dylan Harper | 98% | 32.5<br><sub>30,37,39,27,36</sub> | 17.1<br><sub>13,13,25,17,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>6,5,7,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>6,8,6,8,0</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.4 | 1.9 | 27.5 |
| Devin Vassell | 98% | 32.4<br><sub>24,38,34,25,36</sub> | 13.5<br><sub>14,21,9,11,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>4,5,5,2,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>8,2,2,1,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>4,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.5 | 1.1 | 20.9 |
| De'Aaron Fox | 98% | 31.5<br><sub>26,39,35,22,33</sub> | 15.9<br><sub>11,14,22,12,10</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,3,8,2,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>6,4,7,3,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,1,0,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.4 | 2.1 | 26.0 |
| Stephon Castle | 98% | 30.9<br><sub>27,38,22,26,35</sub> | 17.1<br><sub>15,14,0,16,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,6,5,5,10</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 6.4<br><sub>5,8,4,4,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.9 | 28.8 |
| Julian Champagnie | 98% | 25.6<br><sub>25,31,27,22,21</sub> | 9.4<br><sub>26,6,12,8,0</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,6,3,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,0,1,0,3</sub> |  | 1.8<br><sub>8,2,3,2,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.5 | 0.8 | 15.3 |
| Keldon Johnson | 98% | 21.2<br><sub>22,23,24,27,19</sub> | 9.3<br><sub>14,9,2,15,4</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,2,0,1,2</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 15.1 |
| Luke Kornet | 98% | 14.7<br><sub>17,14,14,17,14</sub> | 3.9<br><sub>0,1,2,8,2</sub> |  | 4.4<br><sub>4,6,8,5,1</sub> |  | 1.0<br><sub>1,1,0,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.3 |
| Harrison Barnes | 67% | 13.4<br><sub>14,-,-,21,13</sub> | 4.8<br><sub>3,-,-,13,4</sub> |  | 1.6<br><sub>0,-,-,0,2</sub> |  | 0.7<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>0,-,-,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.1 |
| Carter Bryant | 72% | 9.5<br><sub>17,5,11,14,-</sub> | 3.4<br><sub>1,3,6,3,-</sub> |  | 1.6<br><sub>1,0,0,0,-</sub> |  | 0.6<br><sub>2,0,0,0,-</sub> |  | 0.3<br><sub>0,1,2,1,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.6 |
| Jordan McLaughlin | 48% | 7.2<br><sub>7,-,-,8,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 1.3<br><sub>2,-,-,3,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.8 |
| Tarris Reed Jr. | 52% | 7.0<br><sub>5,-,-,7,-</sub> | 2.9<br><sub>4,-,-,4,-</sub> |  | 4.1<br><sub>5,-,-,7,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.5 | 7.3 |
| David Jones Garcia | 48% | 5.9<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.8 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 97% | 38.7<br><sub>33,41,37,37,42</sub> | 25.6<br><sub>19,34,38,25,22</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>3,6,5,5,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 8.2<br><sub>5,14,5,6,12</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>3,3,9,2,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.5 | 38.5 |
| Domantas Sabonis | 98% | 35.0<br><sub>37,40,38,31,35</sub> | 16.2<br><sub>20,9,11,9,16</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 13.6<br><sub>14,15,14,7,17</sub> | 12.5<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>8,7,8,4,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.3 | 2.6 | 35.8 |
| Zach LaVine | 98% | 34.6<br><sub>31,39,21,28,35</sub> | 20.4<br><sub>22,21,11,23,21</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>3,3,0,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>3,5,1,1,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,3,0,5,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 2.6 | 27.1 |
| Precious Achiuwa | 98% | 29.3<br><sub>14,41,25,27,17</sub> | 12.4<br><sub>4,24,6,6,7</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>1,9,5,10,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>0,2,1,3,1</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.8 | 1.1 | 21.9 |
| Malik Monk | 98% | 22.2<br><sub>13,8,14,30,24</sub> | 11.7<br><sub>3,2,8,24,13</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>2,1,0,1,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.7<br><sub>6,1,3,7,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>1,0,0,5,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.4 | 1.6 | 17.7 |
| Leaky Black | 58% | 22.0<br><sub>8,-,-,25,22</sub> | 5.8<br><sub>2,-,-,12,3</sub> |  | 3.6<br><sub>1,-,-,3,6</sub> |  | 1.1<br><sub>1,-,-,1,1</sub> |  | 0.7<br><sub>0,-,-,4,0</sub> |  | 0.9 | 0.4 | 0.7 | 10.5 |
| Jonathan Mogbo | 48% | 17.0<br><sub>18,-,25,-,-</sub> | 5.3<br><sub>2,-,6,-,-</sub> |  | 2.7<br><sub>5,-,3,-,-</sub> |  | 0.9<br><sub>0,-,3,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.6 | 0.4 | 0.6 | 8.9 |
| Emanuel Sharp | 97% | 16.6<br><sub>20,18,24,20,10</sub> | 4.5<br><sub>5,0,2,9,3</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>0,0,1,3,1</sub> |  | 0.9<br><sub>2,0,1,1,2</sub> |  | 0.5<br><sub>1,0,0,3,1</sub> |  | 0.5 | 0.2 | 0.6 | 6.8 |
| Dylan Cardwell | 96% | 16.5<br><sub>-,-,-,-,13</sub> | 4.7<br><sub>-,-,-,-,4</sub> | 4.5 · –<br><sub>o 42% · u 58%</sub> | 5.9<br><sub>-,-,-,-,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 1.0 | 0.7 | 11.7 |
| Daeqwon Plowden | 86% | 12.9<br><sub>17,-,4,3,-</sub> | 4.2<br><sub>0,-,4,1,-</sub> |  | 1.6<br><sub>2,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.4 |
| Alex Karaban | 52% | 11.6<br><sub>11,12,10,-,-</sub> | 3.9<br><sub>0,6,0,-,-</sub> |  | 1.6<br><sub>1,0,1,-,-</sub> |  | 0.6<br><sub>1,0,1,-,-</sub> |  | 0.3<br><sub>0,2,0,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 6.0 |
| Nique Clifford | 91% | 11.1<br><sub>5,4,11,3,3</sub> | 4.1<br><sub>2,0,0,0,0</sub> |  | 1.7<br><sub>0,0,1,1,2</sub> |  | 1.1<br><sub>0,1,2,0,0</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-06/`._
