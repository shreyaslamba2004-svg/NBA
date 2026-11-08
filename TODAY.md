# NBA model · Sat 07 Nov 2026 (US date)

Updated **Sun 08 Nov, 01:13 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-07/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

_No long shots clear the edge threshold right now._

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| SAS @ POR | Sun 08 Nov 14:00 | 114.3–108.7 | SAS 65% | 1.54 / 2.87 | POR +5.5 | 222.5 | POR +5.5 covers 49%; o228.5 38% |

### SAS @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Robert Williams III (POR), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 32.7<br><sub>39,34,24,34,26</sub> | 27.2<br><sub>36,43,12,52,30</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 11.1<br><sub>14,7,11,24,14</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>5,4,5,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,3,0,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 3.5 | 2.7 | 41.5 |
| Devin Vassell | 98% | 32.3<br><sub>38,34,25,36,27</sub> | 11.3<br><sub>21,9,11,2,19</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>5,5,2,7,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>2,2,1,4,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>1,0,0,0,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.3 | 0.5 | 1.2 | 18.0 |
| Dylan Harper | 98% | 32.0<br><sub>37,39,27,36,28</sub> | 16.8<br><sub>13,25,17,21,19</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,7,7,5,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>8,6,8,0,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.3 | 2.0 | 25.7 |
| De'Aaron Fox | 98% | 31.6<br><sub>39,35,22,33,26</sub> | 14.9<br><sub>14,22,12,10,9</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>3,8,2,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>4,7,3,4,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,1,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.4 | 2.3 | 23.8 |
| Stephon Castle | 98% | 31.1<br><sub>38,22,26,35,28</sub> | 16.7<br><sub>14,0,16,17,19</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>6,5,5,10,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>8,4,4,3,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,0,2,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.3 | 2.9 | 27.2 |
| Julian Champagnie | 98% | 25.0<br><sub>31,27,22,21,22</sub> | 8.2<br><sub>6,12,8,0,8</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>6,3,6,4,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,1,0,3,2</sub> |  | 1.5<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.5 | 0.7 | 13.9 |
| Keldon Johnson | 98% | 22.1<br><sub>23,24,27,19,27</sub> | 9.4<br><sub>9,2,15,4,3</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>6,6,7,5,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,1,2,6</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.2 | 0.9 | 15.3 |
| Luke Kornet | 98% | 15.5<br><sub>14,14,17,14,18</sub> | 4.0<br><sub>1,2,8,2,2</sub> |  | 4.4<br><sub>6,8,5,1,6</sub> |  | 1.0<br><sub>1,0,2,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.5 | 9.3 |
| Harrison Barnes | 72% | 14.1<br><sub>-,-,21,13,19</sub> | 4.7<br><sub>-,-,13,4,13</sub> |  | 1.6<br><sub>-,-,0,2,1</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,3,1,2</sub> |  | 0.3 | 0.1 | 0.5 | 6.9 |
| Carter Bryant | 80% | 8.9<br><sub>5,11,14,-,3</sub> | 2.8<br><sub>3,6,3,-,0</sub> |  | 1.5<br><sub>0,0,0,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.2<br><sub>1,2,1,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.9 |
| Jordan McLaughlin | 52% | 7.7<br><sub>-,-,8,-,8</sub> | 2.5<br><sub>-,-,0,-,2</sub> |  | 1.1<br><sub>-,-,1,-,2</sub> |  | 1.1<br><sub>-,-,3,-,1</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Tarris Reed Jr. | 58% | 6.5<br><sub>-,-,7,-,3</sub> | 2.5<br><sub>-,-,4,-,0</sub> |  | 3.3<br><sub>-,-,7,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 6.1 |
| David Jones Garcia | 58% | 6.0<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 35.1<br><sub>32,30,35,35,39</sub> | 23.4<br><sub>24,24,28,21,22</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>9,5,3,7,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>7,2,5,12,11</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.8 | 37.4 |
| Damian Lillard | 98% | 34.4<br><sub>30,27,30,33,37</sub> | 20.1<br><sub>9,22,20,25,22</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>2,5,6,3,0</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>2,4,6,5,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>1,3,1,2,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 2.7 | 30.2 |
| Jrue Holiday | 98% | 31.7<br><sub>24,22,31,28,31</sub> | 13.8<br><sub>6,14,17,15,12</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>6,4,8,4,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.4<br><sub>4,3,10,0,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,2,3,5,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.2 | 2.1 | 23.9 |
| Toumani Camara | 98% | 31.6<br><sub>26,31,31,32,30</sub> | 12.2<br><sub>13,14,9,11,18</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>2,4,5,4,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,4,3,1,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.4 | 1.2 | 18.4 |
| Donovan Clingan | 98% | 28.8<br><sub>29,15,32,29,28</sub> | 12.2<br><sub>11,4,17,24,17</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 10.9<br><sub>8,9,18,11,11</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>1,0,3,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>1,0,1,1,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 1.9 | 1.4 | 25.2 |
| Scoot Henderson | 98% | 27.0<br><sub>19,31,26,22,23</sub> | 12.2<br><sub>9,14,8,9,2</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>0,1,2,1,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,1,2,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 2.3 | 18.0 |
| Sidy Cissoko | 98% | 23.7<br><sub>19,19,22,21,22</sub> | 6.4<br><sub>4,1,8,7,7</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>6,3,3,4,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,1,0,4,3</sub> |  | 0.8<br><sub>0,0,2,1,2</sub> |  | 0.8 | 0.4 | 1.0 | 11.7 |
| Chris Youngblood | 88% | 13.6<br><sub>-,7,15,4,11</sub> | 5.0<br><sub>-,3,7,0,7</sub> |  | 1.7<br><sub>-,0,2,0,1</sub> |  | 0.8<br><sub>-,0,1,1,0</sub> |  | 0.8<br><sub>-,1,1,0,2</sub> |  | 0.4 | 0.2 | 0.5 | 7.6 |
| Micah Potter | 52% | 9.4<br><sub>9,4,-,2,-</sub> | 4.0<br><sub>1,2,-,4,-</sub> |  | 2.7<br><sub>2,1,-,1,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,1,-</sub> |  | 0.2 | 0.2 | 0.5 | 7.3 |
| Branden Carlson | 52% | 9.2<br><sub>12,4,-,3,-</sub> | 2.8<br><sub>2,0,-,2,-</sub> |  | 2.0<br><sub>2,2,-,0,-</sub> |  | 0.6<br><sub>1,1,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.5 | 0.6 | 5.3 |
| Yang Hansen | 67% | 9.1<br><sub>5,13,-,2,3</sub> | 3.5<br><sub>3,6,-,0,2</sub> |  | 2.1<br><sub>2,5,-,0,0</sub> |  | 0.5<br><sub>1,1,-,0,0</sub> |  | 0.2<br><sub>1,2,-,0,0</sub> |  | 0.2 | 0.3 | 0.6 | 6.1 |
| Jayson Kent | 52% | 7.8<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-07/`._
