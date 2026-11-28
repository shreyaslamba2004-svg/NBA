# NBA model · Fri 27 Nov 2026 (US date)

Updated **Sat 28 Nov, 01:38 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-27/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija AST over 11.5 (12+) | GSW @ POR | draftkings | 18.80 | 15.31 | 7.37 | 13.6% | 5.0% | 6.5% | +22.7% | +155.1% | 0.3% |
| Deni Avdija PRA over 59.5 (60+) | GSW @ POR | draftkings | 21.00 | 18.73 | 10.66 | 9.4% | 4.5% | 5.3% | +12.2% | +97.0% | 0.1% |
| Jrue Holiday AST over 9.5 (10+) | GSW @ POR | draftkings | 9.80 | 8.75 | 4.99 | 20.0% | 9.5% | 11.4% | +12.1% | +96.2% | 0.3% |
| Jrue Holiday AST over 11.5 (12+) | GSW @ POR | draftkings | 24.00 | 21.41 | 12.23 | 8.2% | 3.9% | 4.7% | +12.1% | +96.2% | 0.1% |
| Sidy Cissoko AST over 5.5 (6+) | GSW @ POR | draftkings | 21.00 | 19.05 | 11.25 | 8.9% | 4.5% | 5.2% | +10.3% | +86.7% | 0.1% |
| Deni Avdija PTS over 44.5 (45+) | GSW @ POR | draftkings | 25.00 | 22.88 | 13.87 | 7.2% | 3.7% | 4.4% | +9.2% | +80.2% | 0.1% |
| Toumani Camara AST over 3.5 (4+) | GSW @ POR | draftkings | 7.50 | 7.01 | 4.45 | 22.5% | 12.5% | 14.3% | +7.1% | +68.6% | 0.3% |
| Zion Williamson AST over 5.5 (6+) | NOP @ LAC | draftkings | 11.20 | 10.50 | 6.73 | 14.8% | 8.3% | 9.5% | +6.7% | +66.3% | 0.2% |
| Donovan Clingan AST over 5.5 (6+) | GSW @ POR | draftkings | 21.00 | 19.72 | 12.67 | 7.9% | 4.5% | 5.1% | +6.5% | +65.7% | 0.1% |
| Sidy Cissoko AST over 3.5 (4+) | GSW @ POR | draftkings | 5.03 | 4.74 | 3.07 | 32.6% | 18.6% | 21.1% | +6.2% | +63.8% | 0.4% |
| Stephon Castle AST over 11.5 (12+) | LAL @ SAS | draftkings | 19.20 | 18.15 | 11.87 | 8.4% | 4.9% | 5.5% | +5.8% | +61.8% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija AST over 7.5 (8+) | GSW @ POR | draftkings | 3.04 | 2.89 | 1.93 | 51.8% | 30.7% | 34.6% | +5.1% | +57.6% | 0.6% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ SAS | Sat 28 Nov 13:30 | 109.5–113.9 | LAL 37% | 2.68 / 1.59 | SAS -4.5 | 223.5 | SAS -6.5 covers 44%; o227.5 41% |
| DEN @ UTA | Sat 28 Nov 13:30 | 122.8–116.8 | DEN 66% | 1.50 / 2.98 | UTA +5.5 | 239.5 | UTA +9.5 covers 60%; o231.5 67% |
| NOP @ LAC | Sat 28 Nov 13:30 | 110.8–116.7 | NOP 34% | 2.96 / 1.51 | LAC -6.5 | 227.5 | LAC -2.5 covers 60%; o230.5 43% |
| GSW @ POR | Sat 28 Nov 13:30 | 110.2–113.4 | GSW 41% | 2.41 / 1.71 | POR -3.5 | 223.5 | POR -8.5 covers 35%; o216.5 64% |

### LAL @ SAS
Out: Tobias Harris (SAS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walker Kessler PTS under 11.5 | LAL @ SAS | pointsbetau | 2.05 | 1.97 | 1.66 | 60.1% | 48.6% | 50.7% | +4.0% | +23.2% | 0.9% |
| Collin Sexton PTS over 7.5 (8+) | LAL @ SAS | sportsbet | 1.96 | 1.92 | 1.65 | 60.7% | 50.2% | 52.1% | +2.2% | +19.1% | 0.6% |
| Stephon Castle PTS under 16.5 | LAL @ SAS | neds | 1.91 | 1.89 | 1.64 | 61.0% | 51.1% | 52.9% | +1.0% | +16.5% | 0.3% |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 99% | 34.5<br><sub>36,42,37,36,33</sub> | 29.7<br><sub>43,36,29,25,28</sub> | 32.5 · 32.5<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.4 | 4.0 | 43.1 |
| Austin Reaves | 98% | 31.1<br><sub>-,-,-,-,-</sub> | 18.2<br><sub>-,-,-,-,-</sub> | 19.5 · 19.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.4 | 2.6 | 25.8 |
| Walker Kessler | 99% | 28.1<br><sub>32,-,31,30,36</sub> | 10.8<br><sub>14,-,10,15,10</sub> | 11.5 · 12.5<br><sub>o 49% · u 51%</sub> | 9.6<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.5 | 21.8 |
| Quentin Grimes | 99% | 26.8<br><sub>37,42,35,35,30</sub> | 10.0<br><sub>22,47,20,13,9</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.3 | 1.3 | 15.9 |
| Jake LaRavia | 98% | 23.1<br><sub>32,23,30,24,37</sub> | 5.7<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.4 | 0.9 | 11.0 |
| Matisse Thybulle | 98% | 21.0<br><sub>26,31,21,27,27</sub> | 5.6<br><sub>12,7,2,14,14</sub> | 5.5 · 5.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.8 | 0.7 | 0.7 | 9.0 |
| Ziaire Williams | 98% | 17.9<br><sub>19,24,18,28,19</sub> | 6.0<br><sub>6,0,7,5,9</sub> | 5.5 · 5.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>2,1,2,0,4</sub> |  | 1.0<br><sub>3,1,0,1,0</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.6 | 8.9 |
| Collin Sexton | 99% | 17.9<br><sub>24,25,20,18,23</sub> | 9.8<br><sub>16,10,12,10,12</sub> | 7.5 · 7.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.1<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.2 | 1.4 | 13.6 |
| Sandro Mamukelashvili | 99% | 16.0<br><sub>21,23,21,20,13</sub> | 6.2<br><sub>4,3,6,9,2</sub> |  | 3.5<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.7 |
| Jarred Vanderbilt | 91% | 9.3<br><sub>12,14,12,10,12</sub> | 2.5<br><sub>2,4,0,4,1</sub> |  | 2.6<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.8 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Kevon Looney | 36% | 6.6<br><sub>-,17,-,-,-</sub> | 1.4<br><sub>-,4,-,-,-</sub> |  | 2.3<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.2 |
| Cameron Carr | 80% | 6.2<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Carson Cooper | 52% | 6.1<br><sub>-,18,2,-,-</sub> | 2.0<br><sub>-,3,2,-,-</sub> |  | 1.7<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.3 | 4.1 |
| Jaden Hardy | 43% | 6.0<br><sub>-,-,2,-,-</sub> | 3.5<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.5 |
| Adou Thiero | 52% | 5.7<br><sub>-,6,6,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.3<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Bronny James | 47% | 5.1<br><sub>-,-,2,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.6 |
| Chris Manon | 52% | 5.1<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 2.8 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 99% | 29.4<br><sub>34,33,32,-,35</sub> | 25.8<br><sub>25,32,50,-,44</sub> | 28.5 · 28.5<br><sub>o 46% · u 54%</sub> | 11.3<br><sub>18,11,19,-,16</sub> | 12.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>4,3,1,-,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>1,2,5,-,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 3.0 | 2.5 | 40.2 |
| Devin Vassell | 99% | 28.9<br><sub>36,32,26,34,38</sub> | 12.1<br><sub>12,15,10,16,18</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>5,4,3,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>4,4,2,2,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>2,1,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.4 | 1.0 | 18.5 |
| Stephon Castle | 99% | 28.5<br><sub>31,33,29,37,34</sub> | 15.5<br><sub>10,21,19,28,20</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,6,3,8,6</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 6.9<br><sub>7,12,6,11,9</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,5,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.2 | 2.7 | 27.0 |
| Dylan Harper | 99% | 26.7<br><sub>35,-,-,-,-</sub> | 14.6<br><sub>20,-,-,-,-</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>4,-,-,-,-</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>2,-,-,-,-</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>0,-,-,-,-</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.0 | 0.3 | 1.7 | 23.2 |
| De'Aaron Fox | 99% | 25.8<br><sub>34,32,26,-,-</sub> | 11.9<br><sub>6,10,5,-,-</sub> | 12.5 · 12.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,2,2,-,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.4<br><sub>2,5,10,-,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>0,0,0,-,-</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.3 | 2.1 | 20.6 |
| Julian Champagnie | 99% | 24.9<br><sub>30,29,25,30,37</sub> | 10.3<br><sub>14,20,9,22,11</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>6,4,3,7,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>4,4,3,6,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.4 | 0.7 | 15.8 |
| Keldon Johnson | 99% | 22.4<br><sub>15,27,23,26,33</sub> | 9.1<br><sub>4,10,10,12,3</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>2,5,4,4,12</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>1,3,4,5,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 1.0 | 15.9 |
| Harrison Barnes | 96% | 13.8<br><sub>10,16,21,26,15</sub> | 5.2<br><sub>0,9,3,9,5</sub> |  | 1.6<br><sub>3,2,5,2,0</sub> |  | 0.9<br><sub>4,1,2,2,1</sub> |  | 0.6<br><sub>0,1,0,1,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.7 |
| Luke Kornet | 99% | 13.4<br><sub>14,15,10,29,13</sub> | 3.9<br><sub>2,4,0,18,4</sub> |  | 4.0<br><sub>1,0,3,11,5</sub> |  | 1.1<br><sub>1,3,0,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 9.0 |
| Jordan McLaughlin | 88% | 11.2<br><sub>-,11,18,14,15</sub> | 3.5<br><sub>-,0,0,6,4</sub> |  | 1.5<br><sub>-,1,3,2,2</sub> |  | 1.8<br><sub>-,5,2,0,0</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.1 | 0.6 | 6.9 |
| Carter Bryant | 96% | 11.0<br><sub>2,13,20,12,14</sub> | 4.3<br><sub>0,3,8,0,2</sub> |  | 1.9<br><sub>0,1,3,3,6</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.5<br><sub>0,1,2,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 6.9 |
| Ja'Kobi Gillespie | 93% | 7.0<br><sub>-,-,-,15,7</sub> | 2.7<br><sub>-,-,-,3,0</sub> |  | 0.9<br><sub>-,-,-,2,1</sub> |  | 0.8<br><sub>-,-,-,4,0</sub> |  | 0.2<br><sub>-,-,-,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.5 |
| Tarris Reed Jr. | 52% | 6.7<br><sub>-,-,6,15,-</sub> | 2.5<br><sub>-,-,0,7,-</sub> |  | 2.8<br><sub>-,-,4,7,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 5.7 |

</details>


### DEN @ UTA
Out: Mo Bamba (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Bryce Hopkins (DEN), Cam Whitmore (DEN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ace Bailey PTS over 15.5 (16+) | DEN @ UTA | pointsbetau | 2.05 | 2.03 | 2.04 | 48.9% | 49.3% | 49.2% | +0.9% | +0.3% | 0.2% |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 99% | 36.6<br><sub>38,39,38,42,33</sub> | 27.9<br><sub>28,24,26,37,18</sub> | 25.5 · 26.5<br><sub>o 50% · u 50%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.9 | 3.2 | 49.9 |
| Jamal Murray | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 25.9<br><sub>28,21,14,45,20</sub> | 24.5 · 25.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.7 | 2.2 | 36.4 |
| Christian Braun | 99% | 32.3<br><sub>33,35,31,38,29</sub> | 13.8<br><sub>10,15,19,21,15</sub> | 12.5 · 12.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.5 | 1.0 | 21.4 |
| Cameron Johnson | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.2<br><sub>9,8,19,16,17</sub> | 13.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.0 | 20.8 |
| Aaron Gordon | 99% | 29.2<br><sub>24,31,31,33,24</sub> | 13.3<br><sub>11,13,18,18,1</sub> | 12.5 · 12.5<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.5 | 1.1 | 21.2 |
| DeMar DeRozan | 96% | 19.4<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 8.5 · 9.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 28% · u 72%</sub> | 0.6 | 0.2 | 1.0 | 14.7 |
| Spencer Jones | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile | 98% | 13.7<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.5 |
| Marvin Bagley III | 99% | 12.1<br><sub>10,9,10,11,12</sub> | 6.1<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.4 |
| Tyus Jones | 98% | 10.9<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Julian Strawther | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Zeke Nnaji | 38% | 6.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.3 |
| Alpha Diallo | 48% | 6.1<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Ryan Nembhard | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 34.4<br><sub>35,39,36,26,33</sub> | 21.2<br><sub>30,30,14,15,14</sub> | 20.5 · 19.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.1<br><sub>11,10,6,7,2</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 32.2 |
| Ace Bailey | 99% | 32.3<br><sub>23,27,24,33,33</sub> | 16.2<br><sub>5,19,7,16,18</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.8 | 1.6 | 24.1 |
| Darryn Peterson | 99% | 31.4<br><sub>31,19,32,25,29</sub> | 16.4<br><sub>13,11,20,6,13</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.4<br><sub>2,3,8,5,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.7<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.6 | 1.9 | 25.6 |
| Svi Mykhailiuk | 98% | 24.3<br><sub>33,34,28,32,25</sub> | 10.8<br><sub>8,15,11,39,4</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>7,3,7,5,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>5,5,2,3,2</sub> |  | 1.8<br><sub>2,4,3,10,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.6 | 0.1 | 0.9 | 15.8 |
| Josh Green | 98% | 20.8<br><sub>13,28,29,23,19</sub> | 5.2<br><sub>9,11,8,0,8</sub> | 5.5 · 5.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>1,2,4,1,2</sub> |  | 1.1<br><sub>0,2,0,0,1</sub> |  | 0.7<br><sub>1,2,2,0,2</sub> |  | 0.7 | 0.2 | 0.6 | 8.5 |
| Jaxson Hayes | 88% | 20.6<br><sub>-,25,28,12,-</sub> | 8.6<br><sub>-,6,18,8,-</sub> | 8.5 · 7.5<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>-,7,14,3,-</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>-,2,0,1,-</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.8 | 15.2 |
| Brice Sensabaugh | 99% | 20.1<br><sub>35,14,26,17,17</sub> | 13.1<br><sub>40,8,18,10,6</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>11,3,3,3,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>5,2,1,2,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>8,0,5,2,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.5 | 0.2 | 1.4 | 18.2 |
| Jusuf Nurkic | 64% | 19.2 | 9.2 | 8.5 · 7.5<br><sub>o 54% · u 46%</sub> | 7.3 | 6.5<br><sub>o 55% · u 45%</sub> | 3.7 | 3.5<br><sub>o 42% · u 58%</sub> | 0.5 |  | 0.9 | 0.5 | 1.6 | 20.3 |
| Isaiah Collier | 67% | 16.5<br><sub>-,10,-,13,18</sub> | 7.9<br><sub>-,0,-,10,4</sub> |  | 2.3<br><sub>-,1,-,2,2</sub> |  | 4.3<br><sub>-,2,-,7,1</sub> |  | 0.3<br><sub>-,0,-,1,0</sub> |  | 0.6 | 0.2 | 1.3 | 14.5 |
| Josh Okogie | 98% | 15.5<br><sub>22,15,17,14,9</sub> | 4.6<br><sub>9,3,3,1,0</sub> |  | 2.4<br><sub>2,0,2,4,0</sub> |  | 0.9<br><sub>4,0,2,0,0</sub> |  | 0.5<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 7.9 |
| Kyle Filipowski | 64% | 14.8<br><sub>-,6,-,9,24</sub> | 8.7<br><sub>-,0,-,2,21</sub> |  | 5.0<br><sub>-,3,-,4,12</sub> |  | 1.8<br><sub>-,0,-,3,4</sub> |  | 0.6<br><sub>-,0,-,0,1</sub> |  | 0.6 | 0.3 | 1.0 | 15.4 |
| Tony Bradley | 52% | 10.0<br><sub>17,-,-,13,-</sub> | 2.9<br><sub>3,-,-,1,-</sub> |  | 3.0<br><sub>7,-,-,5,-</sub> |  | 0.5<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.4 |

</details>


### NOP @ LAC
Out: Bradley Beal (LAC), Bennedict Mathurin (NOP), Dejounte Murray (NOP), Jaron Pierre Jr. (NOP)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zion Williamson PTS under 22.5 | NOP @ LAC | tab | 1.95 | 1.90 | 1.55 | 64.4% | 50.1% | 52.7% | +2.9% | +25.7% | 0.8% |
| Kris Dunn PTS over 4.5 (5+) | NOP @ LAC | sportsbet | 1.80 | 1.78 | 1.51 | 66.1% | 53.9% | 56.2% | +1.1% | +19.0% | 0.3% |
| Darius Garland PTS under 20.5 | NOP @ LAC | betright | 1.91 | 1.89 | 1.67 | 60.0% | 51.3% | 52.9% | +0.9% | +14.5% | 0.3% |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 99% | 32.3<br><sub>33,42,37,32,40</sub> | 16.0<br><sub>23,10,21,2,21</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>6,8,6,5,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,6,3,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>5,2,4,0,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 1.0 | 23.7 |
| Trey Murphy III | 98% | 32.1<br><sub>-,-,29,-,35</sub> | 16.3<br><sub>-,-,17,-,9</sub> | 15.5 · 16.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>-,-,4,-,9</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>-,-,1,-,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>-,-,3,-,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.3 | 1.5 | 24.7 |
| Jeremiah Fears | 99% | 32.0<br><sub>29,31,38,34,40</sub> | 17.6<br><sub>19,16,22,29,7</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>10,5,7,5,7</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 6.2<br><sub>10,4,5,4,11</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 3.1 | 28.6 |
| Zion Williamson | 84% | 31.8<br><sub>25,32,37,-,40</sub> | 20.4<br><sub>16,24,22,-,25</sub> | 22.5 · 22.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>6,7,6,-,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,1,7,-,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.2<br><sub>0,0,0,-,0</sub> |  | 1.4 | 0.5 | 2.3 | 29.5 |
| Jordan Poole | 91% | 23.3<br><sub>31,30,13,31,27</sub> | 12.4<br><sub>11,22,6,25,28</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>2,1,0,3,0</sub> |  | 3.3<br><sub>5,5,1,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>1,3,2,3,6</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.3 | 1.8 | 17.8 |
| Herbert Jones | 99% | 23.2<br><sub>24,32,33,25,21</sub> | 7.1<br><sub>8,9,14,2,7</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>3,3,3,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9<br><sub>2,3,4,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.4 | 1.2 | 12.0 |
| Derik Queen | 99% | 22.2<br><sub>21,19,18,35,21</sub> | 11.2<br><sub>17,9,11,15,11</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>10,5,7,15,9</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>0,0,3,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.4<br><sub>4,0,0,0,0</sub> | 0.5<br><sub>o 32% · u 68%</sub> | 1.0 | 0.6 | 2.2 | 20.4 |
| Yves Missi | 98% | 19.2<br><sub>23,17,23,35,22</sub> | 5.6<br><sub>6,4,4,9,4</sub> | 6.5 · 6.5<br><sub>o 45% · u 55%</sub> | 6.1<br><sub>14,5,7,13,8</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,2,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.9 | 12.9 |
| Karlo Matkovic | 98% | 13.4<br><sub>20,10,8,15,13</sub> | 4.6<br><sub>3,0,0,3,5</sub> |  | 3.1<br><sub>2,2,2,3,4</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.5<br><sub>0,0,0,1,1</sub> |  | 0.4 | 0.5 | 0.6 | 8.4 |
| Trendon Watford | 80% | 11.2<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.8 | 7.5 |
| Bryce McGowens | 76% | 9.2<br><sub>-,-,-,-,6</sub> | 3.3<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |
| DeAndre Jordan | 38% | 9.1<br><sub>-,10,-,-,-</sub> | 2.6<br><sub>-,8,-,-,-</sub> |  | 3.4<br><sub>-,2,-,-,-</sub> |  | 0.6<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 6.6 |
| AJ Johnson | 52% | 6.3<br><sub>6,-,-,8,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 0.8<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 99% | 30.1<br><sub>30,35,32,34,29</sub> | 19.5<br><sub>20,23,16,26,12</sub> | 20.5 · 20.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,0,1,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 6.7<br><sub>7,5,2,8,4</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>2,3,2,4,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 2.8 | 28.6 |
| Rui Hachimura | 99% | 28.2<br><sub>27,32,29,29,37</sub> | 14.2<br><sub>20,17,19,19,14</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>5,7,8,3,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>1,2,1,3,5</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>4,2,4,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.4 | 1.1 | 20.9 |
| Brandon Ingram | 97% | 25.9<br><sub>-,-,-,27,26</sub> | 16.1<br><sub>-,-,-,16,18</sub> | 19.5 · 18.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>-,-,-,7,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>-,-,-,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.6 | 1.9 | 24.1 |
| Derrick Jones Jr. | 99% | 24.4<br><sub>28,27,26,23,23</sub> | 9.0<br><sub>5,8,4,7,4</sub> | 7.5 · 8.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,2,7,4,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,1,1,3,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.9 | 1.0 | 0.8 | 14.1 |
| Max Strus | 98% | 22.4<br><sub>21,32,29,26,21</sub> | 8.2<br><sub>3,18,5,8,0</sub> | 7.5 · 8.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>2,5,6,0,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,4,3,2,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>1,5,1,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.2 | 0.9 | 14.5 |
| Brook Lopez | 99% | 21.8<br><sub>23,27,25,21,18</sub> | 11.9<br><sub>23,23,21,3,6</sub> | 10.5 · 9.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,3,6,4,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>2,4,0,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>4,5,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 1.2 | 1.0 | 18.0 |
| Kris Dunn | 99% | 21.7<br><sub>26,20,19,23,22</sub> | 6.5<br><sub>2,6,3,9,12</sub> | 4.5 · 4.5<br><sub>o 56% · u 44%</sub> | 3.3<br><sub>5,2,4,5,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.6<br><sub>5,2,5,4,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.7<br><sub>0,1,1,0,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.3 | 1.0 | 13.4 |
| Keaton Wagler | 98% | 19.4<br><sub>18,17,19,17,21</sub> | 10.0<br><sub>15,7,7,2,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>2,5,7,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>0,2,3,2,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1<br><sub>1,1,1,0,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.7 | 0.1 | 1.5 | 15.4 |
| Kobe Sanders | 98% | 13.5<br><sub>18,14,19,12,5</sub> | 5.6<br><sub>5,0,9,6,0</sub> |  | 1.6<br><sub>1,1,3,0,0</sub> |  | 1.4<br><sub>3,1,1,0,0</sub> |  | 0.7<br><sub>0,0,3,2,0</sub> |  | 0.6 | 0.1 | 0.7 | 8.6 |
| Yanic Konan Niederhauser | 80% | 12.8<br><sub>-,11,16,8,18</sub> | 4.3<br><sub>-,2,6,2,4</sub> |  | 3.5<br><sub>-,3,6,1,4</sub> |  | 0.6<br><sub>-,0,1,1,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.7 | 8.5 |
| Isaiah Jackson | 98% | 12.2<br><sub>19,9,4,18,7</sub> | 5.8<br><sub>8,6,0,6,4</sub> |  | 3.9<br><sub>5,4,0,6,1</sub> |  | 1.1<br><sub>0,2,0,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.9 | 0.7 | 10.7 |
| Gradey Dick | 83% | 10.8<br><sub>17,13,16,-,5</sub> | 4.9<br><sub>0,2,6,-,2</sub> |  | 1.8<br><sub>0,2,5,-,2</sub> |  | 0.7<br><sub>1,1,2,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.3 |
| Baba Miller | 91% | 7.9<br><sub>4,1,3,1,5</sub> | 4.0<br><sub>3,0,1,0,9</sub> |  | 1.3<br><sub>0,0,0,0,1</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.3 |
| Nick Martinelli | 64% | 6.0<br><sub>4,-,-,-,-</sub> | 2.6<br><sub>0,-,-,-,-</sub> |  | 1.5<br><sub>1,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.5 |
| Blake Wesley | 52% | 5.6<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.8 |

</details>


### GSW @ POR
Out: Vit Krejci (POR), Damian Lillard (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos PTS under 9.5 | GSW @ POR | tab | 1.90 | 1.84 | 1.58 | 63.5% | 52.2% | 54.2% | +3.1% | +20.7% | 0.9% |
| Sidy Cissoko PTS over 8.5 (9+) | GSW @ POR | pointsbetau | 1.95 | 1.90 | 1.61 | 62.1% | 50.7% | 52.7% | +2.9% | +21.2% | 0.8% |
| Charles Bassey PTS under 9.5 | GSW @ POR | betright | 2.03 | 2.03 | 1.78 | 56.3% | 47.8% | 49.4% | +0.2% | +14.2% | 0.1% |
| De'Anthony Melton PTS under 11.5 | GSW @ POR | pointsbetau | 1.90 | 1.90 | 1.58 | 63.1% | 50.4% | 52.7% | +0.2% | +20.0% | 0.1% |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 99% | 32.6<br><sub>33,30,33,34,31</sub> | 19.7<br><sub>28,13,11,12,15</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>8,5,8,8,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>3,4,7,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.7 | 2.9 | 30.1 |
| Brandin Podziemski | 98% | 32.6<br><sub>30,29,32,38,32</sub> | 15.8<br><sub>15,10,15,18,13</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>6,3,3,7,2</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>3,4,2,2,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,0,0,4,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.3 | 1.8 | 24.0 |
| Draymond Green | 97% | 25.7<br><sub>25,23,-,27,26</sub> | 6.2<br><sub>2,3,-,9,6</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>8,1,-,6,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,2,-,3,11</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>0,1,-,3,2</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.6 | 2.1 | 16.1 |
| De'Anthony Melton | 99% | 24.0<br><sub>21,19,25,27,27</sub> | 10.4<br><sub>8,0,9,2,24</sub> | 10.5 · 11.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,1,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>1,2,5,7,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>2,0,1,0,8</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.5 | 0.5 | 1.9 | 16.7 |
| Gui Santos | 96% | 20.3<br><sub>19,17,23,23,24</sub> | 8.6<br><sub>12,6,8,13,22</sub> | 9.5 · 9.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>7,6,3,5,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>2,6,0,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8<br><sub>1,0,0,3,2</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.4 | 14.4 |
| Will Richard | 99% | 19.1<br><sub>23,27,27,17,17</sub> | 6.1<br><sub>11,20,15,3,3</sub> |  | 2.2<br><sub>3,0,5,2,2</sub> |  | 1.1<br><sub>1,3,0,2,1</sub> |  | 0.7<br><sub>2,1,1,1,1</sub> |  | 1.0 | 0.2 | 0.8 | 9.4 |
| Charles Bassey | 98% | 18.6<br><sub>16,22,25,26,22</sub> | 9.5<br><sub>4,10,16,13,10</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>0,8,13,9,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>0,0,1,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.0 | 1.3 | 17.2 |
| Georges Niang | 98% | 15.8<br><sub>14,14,15,8,19</sub> | 6.6<br><sub>0,11,5,0,11</sub> |  | 2.2<br><sub>4,1,2,1,3</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9<br><sub>0,2,1,0,3</sub> |  | 0.4 | 0.2 | 0.8 | 9.8 |
| Al Horford | 99% | 15.8<br><sub>14,-,17,18,13</sub> | 5.1<br><sub>0,-,3,7,2</sub> |  | 3.1<br><sub>5,-,2,3,2</sub> |  | 1.7<br><sub>0,-,2,2,2</sub> |  | 0.7<br><sub>0,-,0,1,0</sub> |  | 0.4 | 0.7 | 0.5 | 9.8 |
| Gary Payton II | 91% | 15.8<br><sub>8,16,24,13,17</sub> | 6.4<br><sub>2,8,2,8,9</sub> |  | 2.7<br><sub>0,8,1,1,3</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.4<br><sub>0,2,0,0,1</sub> |  | 0.9 | 0.2 | 0.8 | 10.1 |
| Brandon Williams | 88% | 15.6<br><sub>-,-,-,-,13</sub> | 9.6<br><sub>-,-,-,-,14</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,3</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.3 | 1.4 | 13.8 |
| LJ Cryer | 67% | 10.0<br><sub>24,19,12,11,-</sub> | 4.6<br><sub>7,9,9,3,-</sub> |  | 0.8<br><sub>1,0,0,0,-</sub> |  | 1.0<br><sub>3,2,1,2,-</sub> |  | 0.6<br><sub>1,3,1,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.4 |
| Graham Ike | 72% | 7.3<br><sub>8,15,4,-,-</sub> | 3.3<br><sub>3,2,5,-,-</sub> |  | 1.7<br><sub>5,2,0,-,-</sub> |  | 0.8<br><sub>1,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 5.8 |
| Malevy Leons | 58% | 6.3<br><sub>6,7,4,-,-</sub> | 2.0<br><sub>2,2,0,-,-</sub> |  | 1.2<br><sub>1,1,2,-,-</sub> |  | 0.3<br><sub>0,0,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.6 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 80% | 34.8<br><sub>-,-,36,30,36</sub> | 27.4<br><sub>-,-,20,31,33</sub> | 25.5 · 26.5<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>-,-,9,3,12</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>-,-,5,7,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,-,2,5,5</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.5 | 4.1 | 42.0 |
| Jrue Holiday | 99% | 33.4<br><sub>31,31,31,28,32</sub> | 18.1<br><sub>23,22,13,18,11</sub> | 16.5 · 16.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>5,2,9,2,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>6,7,7,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>5,2,1,4,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.2 | 3.1 | 29.8 |
| Toumani Camara | 99% | 33.3<br><sub>33,37,35,29,31</sub> | 13.4<br><sub>10,18,6,5,8</sub> | 11.5 · 12.5<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>8,6,5,5,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,4,0,3,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,4,1,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.5 | 1.9 | 20.4 |
| Sidy Cissoko | 98% | 30.2<br><sub>32,31,23,24,30</sub> | 10.6<br><sub>6,13,11,5,16</sub> | 8.5 · 8.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>5,5,2,4,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,3,1,0,2</sub> | 1.5<br><sub>o 64% · u 36%</sub> | 1.6<br><sub>2,1,3,1,4</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.5 | 1.6 | 17.3 |
| Scoot Henderson | 99% | 28.5<br><sub>21,35,23,26,23</sub> | 15.5<br><sub>9,27,3,17,10</sub> | 13.5 · 14.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>1,7,1,3,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,3,1,3,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>0,5,0,3,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.2 | 2.9 | 21.8 |
| Donovan Clingan | 99% | 27.6<br><sub>32,26,31,29,21</sub> | 12.9<br><sub>12,7,22,15,5</sub> | 10.5 · 11.5<br><sub>o 53% · u 47%</sub> | 11.8<br><sub>12,13,13,18,8</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>5,2,4,5,2</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 1.0<br><sub>0,0,3,1,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.7 | 1.8 | 1.5 | 27.5 |
| Robert Williams III | 99% | 20.2<br><sub>16,-,17,16,21</sub> | 7.3<br><sub>6,-,4,6,4</sub> |  | 7.6<br><sub>8,-,3,6,3</sub> |  | 1.5<br><sub>4,-,0,1,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.7 | 1.3 | 1.0 | 16.4 |
| Jayson Kent | 88% | 15.9<br><sub>27,17,3,14,6</sub> | 5.5<br><sub>8,2,0,9,0</sub> |  | 2.1<br><sub>3,1,1,2,3</sub> |  | 0.8<br><sub>0,2,0,1,0</sub> |  | 0.7<br><sub>2,0,0,3,0</sub> |  | 0.7 | 0.1 | 0.8 | 8.4 |
| Branden Carlson | 71% | 11.2<br><sub>14,10,9,6,-</sub> | 3.1<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>1,1,1,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.5 | 0.6 | 6.3 |
| Yang Hansen | 64% | 10.2<br><sub>-,12,-,3,5</sub> | 3.5<br><sub>-,2,-,2,0</sub> |  | 2.6<br><sub>-,1,-,0,2</sub> |  | 0.8<br><sub>-,1,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.3 | 0.8 | 6.9 |
| Micah Potter | 52% | 8.7<br><sub>1,-,-,3,-</sub> | 3.9<br><sub>0,-,-,0,-</sub> |  | 2.4<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| John Tonje | 52% | 8.2<br><sub>-,6,-,3,-</sub> | 2.8<br><sub>-,0,-,2,-</sub> |  | 1.8<br><sub>-,3,-,0,-</sub> |  | 0.9<br><sub>-,0,-,1,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-27/`._
