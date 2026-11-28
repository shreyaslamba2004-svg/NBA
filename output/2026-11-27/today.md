# NBA model · Fri 27 Nov 2026 (US date)

Updated **Sat 28 Nov, 01:43 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-27/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephon Castle AST over 11.5 (12+) | LAL @ SAS | draftkings | 19.20 | 18.15 | 11.87 | 8.4% | 4.9% | 5.5% | +5.8% | +61.8% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ SAS | Sat 28 Nov 13:30 | 109.5–113.9 | LAL 37% | 2.68 / 1.59 | SAS -4.5 | 223.5 | SAS -6.5 covers 44%; o227.5 41% |

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


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-27/`._
