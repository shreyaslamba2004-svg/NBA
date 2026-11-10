# NBA model · Mon 09 Nov 2026 (US date)

Updated **Tue 10 Nov, 12:56 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-09/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

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
| SAS @ PHX | Tue 10 Nov 13:00 | 117.3–109.0 | SAS 72% | 1.38 / 3.62 | PHX +8.5 | 226.5 | PHX +9.5 covers 53%; o225.5 52% |
| NOP @ GSW | Tue 10 Nov 14:00 | 112.6–123.8 | NOP 22% | 4.64 / 1.27 | GSW -11.5 | 236.5 | GSW -11.5 covers 49%; o228.5 66% |

### SAS @ PHX
Out: Jordan Goodwin (PHX), Drew Timme (PHX), Mark Williams (PHX), Tobias Harris (SAS), Devin Vassell (SAS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julian Champagnie PTS under 11.5 | SAS @ PHX | tab | 1.90 | 1.89 | 1.58 | 63.2% | 51.3% | 52.9% | +0.5% | +20.1% | 0.1% |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 100% | 33.9<br><sub>39,27,36,28,28</sub> | 18.5<br><sub>25,17,21,19,13</sub> | 16.5 · 16.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>7,7,5,2,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>6,8,0,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>2,1,1,1,1</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.1 | 0.3 | 2.2 | 28.2 |
| Victor Wembanyama | 100% | 32.8<br><sub>34,24,34,26,24</sub> | 27.2<br><sub>43,12,52,30,29</sub> | 26.5 · 26.5<br><sub>o 51% · u 49%</sub> | 12.5<br><sub>7,11,24,14,7</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>4,5,2,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>3,0,1,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 3.3 | 2.9 | 43.0 |
| Stephon Castle | 100% | 32.7<br><sub>22,26,35,28,24</sub> | 17.9<br><sub>0,16,17,19,14</sub> | 16.5 · 16.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>5,5,10,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.0<br><sub>4,4,3,7,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>0,2,2,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.3 | 3.1 | 29.6 |
| De'Aaron Fox | 100% | 32.1<br><sub>35,22,33,26,22</sub> | 16.0<br><sub>22,12,10,9,8</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>8,2,3,2,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>7,3,4,4,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>0,1,0,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.4 | 2.3 | 25.2 |
| Julian Champagnie | 100% | 30.8<br><sub>27,22,21,22,21</sub> | 10.5<br><sub>12,8,0,8,14</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>3,6,4,7,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,0,3,2,0</sub> |  | 2.0<br><sub>3,2,0,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.5 | 0.8 | 17.5 |
| Keldon Johnson | 98% | 25.8<br><sub>24,27,19,27,27</sub> | 10.6<br><sub>2,15,4,3,10</sub> | 10.5 · 11.5<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>6,7,5,6,7</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>0,1,2,6,4</sub> |  | 0.9<br><sub>0,1,0,0,0</sub> |  | 0.8 | 0.2 | 1.2 | 17.8 |
| Luke Kornet | 98% | 17.8<br><sub>14,17,14,18,15</sub> | 4.3<br><sub>2,8,2,2,6</sub> | 3.5 · 3.5<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>8,5,1,6,4</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,2,2,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 0.7 | 10.6 |
| Harrison Barnes | 80% | 17.4<br><sub>-,21,13,19,19</sub> | 5.4<br><sub>-,13,4,13,5</sub> | 6.5 · 5.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>-,0,2,1,3</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.7<br><sub>-,3,1,2,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.2 |
| Carter Bryant | 86% | 14.6<br><sub>11,14,-,3,17</sub> | 4.5<br><sub>6,3,-,0,6</sub> |  | 2.3<br><sub>0,0,-,0,4</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.6<br><sub>2,1,-,0,2</sub> |  | 0.4 | 0.4 | 0.6 | 7.6 |
| Jordan McLaughlin | 63% | 13.4<br><sub>-,8,-,8,12</sub> | 4.1<br><sub>-,0,-,2,3</sub> |  | 1.6<br><sub>-,1,-,2,0</sub> |  | 1.6<br><sub>-,3,-,1,0</sub> |  | 0.5<br><sub>-,0,-,0,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.4 |
| Tarris Reed Jr. | 64% | 9.6<br><sub>-,7,-,3,9</sub> | 3.3<br><sub>-,4,-,0,2</sub> |  | 4.4<br><sub>-,7,-,1,3</sub> |  | 0.4<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.4 | 0.8 | 8.0 |
| David Jones Garcia | 58% | 7.2<br><sub>-,-,-,3,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.1 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 100% | 36.2<br><sub>39,35,34,34,39</sub> | 25.2<br><sub>20,26,33,30,24</sub> | 23.5 · 24.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>2,3,1,1,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>5,5,2,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 3.0 | 34.8 |
| Dillon Brooks | 100% | 33.1<br><sub>21,34,35,29,37</sub> | 17.0<br><sub>22,18,15,24,11</sub> | 14.5 · 14.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>1,8,6,1,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>4,2,0,4,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.5 | 23.2 |
| Miles Bridges | 100% | 32.5<br><sub>37,35,31,31,31</sub> | 15.0<br><sub>24,21,18,18,13</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>10,6,7,13,10</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 3.2<br><sub>2,3,5,5,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,3,4,3,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 1.3 | 24.9 |
| Jalen Green | 100% | 31.5<br><sub>25,36,32,24,34</sub> | 16.0<br><sub>2,11,22,6,16</sub> | 14.5 · 14.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>2,8,2,0,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>2,8,2,3,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>0,0,2,0,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.4 | 2.4 | 23.7 |
| Oso Ighodaro | 100% | 25.7<br><sub>21,24,23,24,23</sub> | 7.3<br><sub>2,14,9,2,4</sub> | 5.5 · 5.5<br><sub>o 54% · u 46%</sub> | 5.9<br><sub>9,2,7,5,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>5,2,7,1,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.2 | 16.5 |
| Collin Gillespie | 98% | 24.3<br><sub>33,24,23,24,20</sub> | 8.8<br><sub>16,3,2,6,7</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.6<br><sub>10,2,2,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>4,1,0,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 1.1 | 15.5 |
| Ryan Dunn | 98% | 18.4<br><sub>11,10,18,25,23</sub> | 5.2<br><sub>5,5,2,11,8</sub> |  | 3.8<br><sub>3,3,6,3,5</sub> |  | 1.3<br><sub>1,1,2,3,3</sub> |  | 0.6<br><sub>1,1,0,1,2</sub> |  | 0.7 | 0.5 | 0.6 | 10.3 |
| Khaman Maluach | 98% | 17.8<br><sub>17,13,16,22,18</sub> | 5.9<br><sub>9,5,6,8,8</sub> | 6.5 · 6.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>6,2,6,6,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>0,0,2,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.9 | 12.1 |
| Luke Kennard | 98% | 17.1<br><sub>12,18,14,21,14</sub> | 6.1<br><sub>9,6,0,12,11</sub> |  | 1.9<br><sub>1,2,0,1,1</sub> |  | 1.7<br><sub>2,1,1,5,2</sub> |  | 0.8<br><sub>1,2,0,3,3</sub> |  | 0.5 | 0.1 | 0.6 | 9.7 |
| Rasheer Fleming | 47% | 7.6<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Pat Spencer | 63% | 7.0<br><sub>-,-,3,2,-</sub> | 2.4<br><sub>-,-,0,0,-</sub> |  | 1.0<br><sub>-,-,0,0,-</sub> |  | 1.1<br><sub>-,-,2,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.0 | 0.5 | 4.4 |
| Duop Reath | 63% | 6.8<br><sub>-,-,7,2,-</sub> | 2.5<br><sub>-,-,7,0,-</sub> |  | 1.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea | 52% | 6.6<br><sub>-,-,3,2,-</sub> | 2.5<br><sub>-,-,3,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Koa Peat | 52% | 6.1<br><sub>-,-,3,2,-</sub> | 2.1<br><sub>-,-,2,0,-</sub> |  | 1.5<br><sub>-,-,1,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.0 |

</details>


### NOP @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Gary Payton II (GSW), Kristaps Porzingis (GSW), Will Richard (GSW), Yves Missi (NOP), Trey Murphy III (NOP), Trendon Watford (NOP), Zion Williamson (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray | 98% | 34.7<br><sub>-,-,45,35,28</sub> | 19.5<br><sub>-,-,20,7,6</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>-,-,8,2,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>-,-,4,4,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,-,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 2.0 | 0.4 | 3.4 | 32.1 |
| Saddiq Bey | 98% | 33.5<br><sub>26,36,29,31,26</sub> | 19.3<br><sub>25,18,22,17,13</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>6,5,4,5,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,1,3,4,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,2,2,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 1.6 | 27.7 |
| Jeremiah Fears | 98% | 32.8<br><sub>31,38,34,36,29</sub> | 20.0<br><sub>20,12,19,24,25</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,4,6,5,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 5.1<br><sub>7,7,2,5,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>1,0,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.5 | 3.1 | 29.8 |
| Derik Queen | 98% | 28.4<br><sub>23,24,27,10,21</sub> | 14.2<br><sub>8,20,20,6,8</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 8.4<br><sub>8,7,9,4,5</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>4,5,6,1,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 1.2 | 0.8 | 2.8 | 26.7 |
| Herbert Jones | 98% | 28.3<br><sub>25,28,37,14,20</sub> | 9.0<br><sub>11,9,2,0,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>3,4,5,4,0</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>2,3,1,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>1,3,0,0,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.4 | 1.4 | 14.6 |
| Karlo Matkovic | 96% | 27.3<br><sub>18,29,21,18,19</sub> | 11.2<br><sub>8,25,5,18,3</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>10,6,4,3,3</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>1,1,2,1,2</sub> |  | 1.4<br><sub>2,5,1,4,1</sub> |  | 0.9 | 1.1 | 1.3 | 19.1 |
| Bennedict Mathurin | 98% | 22.5<br><sub>19,13,15,7,9</sub> | 10.5<br><sub>7,4,2,2,6</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>1,0,5,0,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,0,1,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 1.5 | 16.4 |
| Jordan Poole | 52% | 18.9<br><sub>-,-,-,-,-</sub> | 9.6<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.3 | 1.5 | 13.9 |
| Bryce McGowens | 58% | 17.3<br><sub>15,6,-,-,3</sub> | 5.9<br><sub>3,0,-,-,0</sub> |  | 2.0<br><sub>0,1,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.7 | 0.2 | 0.7 | 9.2 |
| DeAndre Jordan | 26% | 16.1<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 5.9<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.7 | 0.7 | 11.3 |
| Julian Reese | 48% | 10.3<br><sub>3,-,-,-,3</sub> | 3.2<br><sub>2,-,-,-,0</sub> |  | 1.6<br><sub>1,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 5.7 |
| AJ Johnson | 47% | 9.9<br><sub>3,-,-,-,3</sub> | 3.3<br><sub>0,-,-,-,2</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.6 | 0.6 | 4.5 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 91% | 34.3<br><sub>33,37,33,32,39</sub> | 16.9<br><sub>21,17,20,9,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>5,8,3,6,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.1<br><sub>6,8,2,3,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>4,2,3,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.3 | 1.7 | 26.5 |
| Yaxel Lendeborg | 98% | 33.9<br><sub>24,34,29,30,37</sub> | 21.3<br><sub>6,37,16,17,23</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>1,4,5,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>0,6,5,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>1,6,2,1,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 1.0 | 3.2 | 32.8 |
| Stephen Curry | 98% | 32.9<br><sub>31,-,33,28,36</sub> | 28.1<br><sub>31,-,34,29,41</sub> | 27.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,-,6,1,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,-,7,4,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>8,-,5,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.4 | 2.7 | 37.2 |
| Draymond Green | 91% | 28.6<br><sub>32,-,17,27,34</sub> | 7.2<br><sub>2,-,4,2,2</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>9,-,2,11,13</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 0.8<br><sub>0,-,0,0,0</sub> |  | 1.1 | 0.8 | 2.4 | 19.4 |
| Georges Niang | 97% | 21.8<br><sub>19,21,22,22,25</sub> | 8.8<br><sub>11,3,13,13,11</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>5,1,4,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,2,3,3,1</sub> |  | 1.5<br><sub>3,1,1,2,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.5 | 0.2 | 1.0 | 13.3 |
| De'Anthony Melton | 98% | 21.3<br><sub>21,28,28,17,17</sub> | 9.7<br><sub>16,21,2,5,4</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>5,6,7,6,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>3,3,2,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>4,6,0,0,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.3 | 15.2 |
| Brandon Williams | 86% | 18.8<br><sub>17,25,-,21,17</sub> | 10.8<br><sub>9,17,-,10,9</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>2,3,-,1,0</sub> |  | 2.8<br><sub>1,3,-,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.6<br><sub>0,2,-,0,0</sub> |  | 0.8 | 0.3 | 1.6 | 16.0 |
| Al Horford | 98% | 17.0<br><sub>17,22,-,18,13</sub> | 5.9<br><sub>3,9,-,8,2</sub> |  | 3.8<br><sub>2,5,-,5,5</sub> |  | 1.5<br><sub>0,2,-,1,4</sub> |  | 0.9<br><sub>1,3,-,2,0</sub> |  | 0.4 | 0.8 | 0.5 | 11.3 |
| Gui Santos | 88% | 16.5<br><sub>16,9,-,-,12</sub> | 6.9<br><sub>2,4,-,-,3</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>5,3,-,-,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>1,1,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.7 | 0.3 | 1.1 | 11.7 |
| Charles Bassey | 96% | 12.8<br><sub>9,20,23,14,11</sub> | 6.2<br><sub>6,6,19,8,8</sub> |  | 5.3<br><sub>4,10,8,7,4</sub> |  | 0.6<br><sub>1,2,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.1 | 0.7 | 12.2 |
| Graham Ike | 88% | 8.1<br><sub>-,6,7,1,-</sub> | 3.5<br><sub>-,2,0,0,-</sub> |  | 2.0<br><sub>-,2,0,1,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| LJ Cryer | 58% | 7.4<br><sub>-,2,1,1,-</sub> | 3.6<br><sub>-,0,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.0 | 0.3 | 4.8 |
| Malevy Leons | 48% | 6.8<br><sub>-,-,-,1,-</sub> | 2.1<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.3 | 4.0 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-09/`._
