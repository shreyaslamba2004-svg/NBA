# NBA model · Tue 24 Nov 2026 (US date)

Updated **Tue 24 Nov, 09:57 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-24/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic AST over 15.5 (16+) | DAL @ DEN | draftkings | 14.20 | 12.77 | 7.43 | 13.5% | 6.6% | 7.8% | +11.2% | +91.2% | 0.2% |
| Nikola Jokic AST over 17.5 (18+) | DAL @ DEN | draftkings | 28.00 | 25.45 | 15.15 | 6.6% | 3.3% | 3.9% | +10.0% | +84.8% | 0.1% |
| Ausar Thompson AST over 7.5 (8+) | DET @ ORL | draftkings | 10.90 | 10.32 | 6.79 | 14.7% | 8.6% | 9.7% | +5.6% | +60.6% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DET @ ORL | Wed 25 Nov 11:00 | 111.0–108.7 | DET 57% | 1.76 / 2.31 | ORL +2.5 | 219.5 | ORL +2.5 covers 49%; o211.5 67% |
| BOS @ WAS | Wed 25 Nov 12:00 | 115.7–107.2 | BOS 73% | 1.37 / 3.68 | WAS +8.5 | 222.5 | WAS +10.5 covers 56%; o217.5 61% |
| DAL @ DEN | Wed 25 Nov 14:00 | 113.3–121.8 | DAL 28% | 3.62 / 1.38 | DEN -8.5 | 234.5 | DEN -7.5 covers 53%; o233.5 53% |

### DET @ ORL
Out: Paolo Banchero (ORL), Colin Castleton (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Duren (DET), Taurean Prince (DET), Duncan Robinson (DET)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.0–108.7 | DET 57% | 1.76 / 2.31 | ORL +2.5 | 219.5 | ORL +2.5 covers 49%; o211.5 67% |
| Expected (weighted by chance each plays) | 110.8–108.8 | DET 56% | 1.79 / 2.27 | ORL +2.5 | 219.5 | ORL +2.5 covers 50%; o211.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaac Jones (DET) | Questionable | 55% | 5.5 | 6.3 | 1.2 | 0.3 | 0.1 | 0.2 | 0.3 | 0.3 | 7.9 | small |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 82% | 34.6<br><sub>36,38,-,36,33</sub> | 25.9<br><sub>33,27,-,23,5</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,5,-,5,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 8.2<br><sub>8,6,-,9,15</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,1,-,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3 | 0.8 | 3.8 | 39.0 |
| Daniss Jenkins | 99% | 33.4<br><sub>35,38,36,39,38</sub> | 14.9<br><sub>10,25,17,14,11</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>1,5,4,4,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.9<br><sub>5,5,9,1,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>1,3,3,2,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 2.0 | 23.6 |
| Ausar Thompson | 99% | 31.1<br><sub>18,29,34,33,38</sub> | 11.3<br><sub>10,14,10,13,18</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>8,9,7,6,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 4.9<br><sub>5,12,4,3,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.1 | 1.2 | 2.1 | 24.0 |
| Kevin Huerter | 98% | 29.2<br><sub>38,36,36,36,30</sub> | 11.9<br><sub>20,9,11,20,2</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>4,7,1,3,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>7,1,7,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>2,0,1,4,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.6 | 1.3 | 18.1 |
| Paul Reed | 98% | 25.7<br><sub>23,25,20,28,26</sub> | 12.6<br><sub>9,10,17,8,16</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 7.2<br><sub>9,6,7,7,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>1,5,1,3,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.2 | 1.6 | 21.9 |
| John Collins | 99% | 25.3<br><sub>26,23,30,20,22</sub> | 11.1<br><sub>8,11,20,3,18</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>7,1,7,6,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>0,0,2,1,0</sub> |  | 1.1<br><sub>2,1,4,0,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.8 | 1.3 | 17.4 |
| Javonte Green | 98% | 19.7<br><sub>12,23,35,23,18</sub> | 6.9<br><sub>5,6,18,12,6</sub> |  | 2.8<br><sub>1,6,7,1,3</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 1.0<br><sub>0,0,3,3,2</sub> |  | 1.2 | 0.4 | 0.6 | 10.4 |
| Isaiah Joe | 96% | 18.8<br><sub>-,-,16,18,26</sub> | 10.0<br><sub>-,-,11,9,19</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>-,-,2,1,2</sub> |  | 1.2<br><sub>-,-,2,0,3</sub> |  | 1.7<br><sub>-,-,3,1,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 0.8 | 13.2 |
| Ronald Holland II | 98% | 15.1<br><sub>22,-,-,-,10</sub> | 5.6<br><sub>5,-,-,-,2</sub> |  | 3.2<br><sub>7,-,-,-,4</sub> |  | 1.1<br><sub>3,-,-,-,0</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.7 | 0.4 | 0.8 | 9.8 |
| Chaz Lanier | 58% | 8.2<br><sub>-,25,16,6,-</sub> | 3.0<br><sub>-,3,9,0,-</sub> |  | 0.7<br><sub>-,3,1,0,-</sub> |  | 0.4<br><sub>-,1,0,0,-</sub> |  | 0.3<br><sub>-,1,3,0,-</sub> |  | 0.1 | 0.1 | 0.1 | 4.0 |
| Elijah Harkless | 52% | 7.2<br><sub>2,4,14,-,-</sub> | 2.5<br><sub>2,0,6,-,-</sub> |  | 1.1<br><sub>0,1,2,-,-</sub> |  | 0.7<br><sub>0,1,4,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 4.3 |
| Tolu Smith | 48% | 6.9<br><sub>1,-,3,-,-</sub> | 2.9<br><sub>3,-,3,-,-</sub> |  | 2.2<br><sub>2,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.4 |

</details>

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 99% | 34.9<br><sub>36,38,36,36,32</sub> | 24.1<br><sub>35,21,27,35,16</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>9,8,8,5,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>12,9,11,7,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>3,0,1,2,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.4 | 2.9 | 36.8 |
| Desmond Bane | 99% | 33.9<br><sub>35,39,38,31,33</sub> | 17.9<br><sub>21,24,15,21,17</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>5,8,3,2,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,5,3,3,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>6,3,5,7,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.5 | 1.9 | 25.1 |
| Anthony Black | 98% | 33.4<br><sub>37,33,37,37,35</sub> | 15.3<br><sub>5,20,15,13,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>2,2,2,7,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>5,7,6,6,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,3,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.8 | 2.4 | 24.1 |
| Wendell Carter Jr. | 99% | 30.5<br><sub>30,28,32,35,26</sub> | 11.3<br><sub>12,10,15,8,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>8,3,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,1,3,2,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8<br><sub>1,1,2,0,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.9 | 1.5 | 20.4 |
| Jalen Suggs | 98% | 27.9<br><sub>21,25,31,30,22</sub> | 10.8<br><sub>3,12,18,8,9</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>2,6,8,6,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.1<br><sub>3,4,4,2,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>1,2,5,2,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.6 | 2.4 | 18.7 |
| Tristan da Silva | 91% | 26.0<br><sub>31,31,27,24,27</sub> | 10.8<br><sub>12,13,12,6,18</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>6,6,2,1,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>2,3,0,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>2,3,2,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.3 | 1.1 | 15.9 |
| Goga Bitadze | 93% | 14.8<br><sub>18,20,20,15,15</sub> | 5.0<br><sub>12,10,8,4,1</sub> |  | 4.5<br><sub>4,6,3,4,4</sub> |  | 1.0<br><sub>1,1,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.0 | 0.7 | 10.6 |
| Nikola Vucevic | 72% | 14.3<br><sub>11,-,-,23,17</sub> | 5.6<br><sub>2,-,-,15,5</sub> |  | 3.9<br><sub>3,-,-,8,3</sub> |  | 1.5<br><sub>0,-,-,1,3</sub> |  | 0.6<br><sub>0,-,-,3,1</sub> |  | 0.3 | 0.4 | 0.6 | 11.0 |
| Jevon Carter | 91% | 13.5<br><sub>17,12,16,10,14</sub> | 5.1<br><sub>5,3,6,3,3</sub> |  | 1.3<br><sub>2,2,2,0,2</sub> |  | 1.3<br><sub>2,1,3,0,2</sub> |  | 0.7<br><sub>1,1,2,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.7 |
| Jase Richardson | 52% | 12.9<br><sub>-,-,-,-,6</sub> | 4.4<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 6.9 |
| Jamal Cain | 72% | 11.8<br><sub>4,15,4,-,9</sub> | 4.1<br><sub>0,2,0,-,2</sub> |  | 2.2<br><sub>4,5,1,-,1</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 6.9 |
| Alex Morales | 52% | 9.1<br><sub>-,-,-,-,5</sub> | 2.1<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,2</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.3 |

</details>


### BOS @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Mitchell Robinson (BOS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.7–107.2 | BOS 73% | 1.37 / 3.68 | WAS +8.5 | 222.5 | WAS +10.5 covers 56%; o217.5 61% |
| Expected (weighted by chance each plays) | 115.6–107.1 | BOS 73% | 1.37 / 3.73 | WAS +8.5 | 222.5 | WAS +10.5 covers 56%; o217.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Questionable | 55% | 5.8 | 2.4 | 1.6 | 0.4 | 0.0 | 0.1 | 0.2 | 0.3 | 4.4 | small |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 99% | 33.9<br><sub>30,36,37,-,38</sub> | 26.7<br><sub>32,24,24,-,27</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 8.6<br><sub>6,12,8,-,10</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>6,4,3,-,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,3,3,-,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.5 | 2.7 | 41.7 |
| Paul George | 98% | 30.5<br><sub>25,36,23,37,-</sub> | 19.1<br><sub>7,22,10,19,-</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>7,8,4,8,-</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 3.4<br><sub>6,3,1,5,-</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>1,5,1,2,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.4 | 2.0 | 28.0 |
| Derrick White | 84% | 29.9<br><sub>23,32,35,-,32</sub> | 13.0<br><sub>16,9,12,-,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>4,3,3,-,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.7<br><sub>2,2,8,-,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>4,1,0,-,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.8 | 1.2 | 21.4 |
| Payton Pritchard | 99% | 27.9<br><sub>19,32,30,34,28</sub> | 13.6<br><sub>10,21,15,9,5</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,4,1,6,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>6,5,2,8,4</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>2,4,3,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.1 | 1.0 | 21.5 |
| Neemias Queta | 99% | 25.6<br><sub>15,-,27,30,30</sub> | 11.1<br><sub>8,-,17,15,6</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 9.3<br><sub>6,-,10,7,10</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,-,3,1,4</sub> |  | 0.1<br><sub>1,-,0,1,0</sub> |  | 0.7 | 1.2 | 1.2 | 22.6 |
| Sam Hauser | 99% | 21.6<br><sub>11,25,17,31,22</sub> | 8.1<br><sub>8,12,9,14,3</sub> |  | 3.4<br><sub>1,1,2,6,1</sub> |  | 1.3<br><sub>0,2,2,2,2</sub> |  | 1.6<br><sub>2,4,3,4,1</sub> |  | 0.5 | 0.2 | 0.3 | 12.8 |
| Baylor Scheierman | 99% | 17.1<br><sub>18,11,13,18,15</sub> | 5.0<br><sub>12,0,0,4,3</sub> |  | 3.3<br><sub>5,1,1,3,4</sub> |  | 1.4<br><sub>3,1,1,1,1</sub> |  | 0.7<br><sub>2,0,0,0,1</sub> |  | 0.8 | 0.1 | 0.4 | 9.8 |
| Hugo Gonzalez | 98% | 14.8<br><sub>18,4,16,17,22</sub> | 4.4<br><sub>9,0,2,5,6</sub> | 5.5 · –<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>5,2,6,4,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>2,0,0,1,0</sub> |  | 0.5<br><sub>2,0,0,1,2</sub> |  | 0.6 | 0.3 | 0.5 | 8.2 |
| Luka Garza | 98% | 14.5<br><sub>14,18,5,17,17</sub> | 7.5<br><sub>2,3,0,5,10</sub> |  | 3.8<br><sub>3,0,1,5,5</sub> |  | 1.5<br><sub>5,4,1,1,0</sub> |  | 0.7<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.4 | 0.6 | 12.7 |
| Mike Conley | 52% | 13.4<br><sub>-,-,-,18,16</sub> | 4.8<br><sub>-,-,-,19,6</sub> |  | 1.6<br><sub>-,-,-,4,2</sub> |  | 2.1<br><sub>-,-,-,2,4</sub> |  | 0.7<br><sub>-,-,-,4,2</sub> |  | 0.7 | 0.2 | 0.5 | 8.4 |
| Jordan Walsh | 98% | 11.6<br><sub>21,17,4,8,9</sub> | 3.4<br><sub>11,6,0,1,2</sub> |  | 2.3<br><sub>1,2,0,4,0</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>2,2,0,0,0</sub> |  | 0.5 | 0.2 | 0.3 | 6.3 |
| Chris Cenac Jr. | 72% | 9.0<br><sub>7,12,17,12,5</sub> | 3.4<br><sub>6,4,6,2,0</sub> |  | 2.3<br><sub>3,2,6,3,2</sub> |  | 0.4<br><sub>0,1,0,0,0</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Devin Carter | 66% | 8.6<br><sub>12,-,-,4,-</sub> | 3.7<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>2,-,-,2,-</sub> |  | 1.2<br><sub>1,-,-,0,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.6 | 6.6 |
| Ron Harper Jr. | 63% | 8.1<br><sub>12,-,-,13,6</sub> | 3.6<br><sub>10,-,-,3,5</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.6<br><sub>0,-,-,1,0</sub> |  | 0.4<br><sub>2,-,-,1,1</sub> |  | 0.3 | 0.1 | 0.2 | 5.3 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 35.1<br><sub>30,32,38,37,33</sub> | 15.5<br><sub>16,21,23,20,16</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>7,5,12,10,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>1,3,2,6,6</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>2,1,0,2,0</sub> |  | 0.9 | 0.5 | 2.2 | 25.7 |
| Anthony Davis | 99% | 34.8<br><sub>31,35,34,34,33</sub> | 21.5<br><sub>14,23,25,36,22</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 11.4<br><sub>8,4,14,11,7</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>5,0,2,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.8<br><sub>0,0,2,0,2</sub> |  | 1.0 | 1.4 | 2.1 | 35.7 |
| Kyshawn George | 99% | 34.6<br><sub>30,38,40,35,36</sub> | 15.8<br><sub>11,18,20,11,24</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>2,6,2,7,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>4,1,4,5,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.4<br><sub>1,2,4,1,6</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 1.0 | 2.3 | 25.1 |
| Trae Young | 99% | 34.2<br><sub>26,33,32,35,28</sub> | 16.2<br><sub>0,13,11,16,11</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>1,2,1,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 9.0<br><sub>8,12,8,5,11</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>0,2,1,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 2.9 | 28.0 |
| Alex Sarr | 98% | 26.3<br><sub>27,31,22,20,26</sub> | 10.8<br><sub>25,6,13,3,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>9,4,2,3,9</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>2,1,3,0,2</sub> |  | 1.2<br><sub>3,1,3,1,2</sub> |  | 0.6 | 1.2 | 1.2 | 19.3 |
| Bilal Coulibaly | 99% | 23.9<br><sub>21,16,26,24,25</sub> | 8.3<br><sub>9,11,3,2,12</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>2,5,8,5,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,0,2,0,1</sub> |  | 0.8<br><sub>1,1,0,0,4</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.7 | 1.1 | 13.8 |
| Khris Middleton | 67% | 17.8<br><sub>9,18,20,28,20</sub> | 6.0<br><sub>8,9,8,5,6</sub> |  | 2.7<br><sub>0,3,4,2,2</sub> |  | 1.6<br><sub>2,3,1,3,2</sub> |  | 0.7<br><sub>2,2,1,0,2</sub> |  | 0.4 | 0.1 | 1.0 | 10.2 |
| Tre Johnson | 96% | 15.2<br><sub>-,21,8,4,15</sub> | 5.9<br><sub>-,9,0,2,11</sub> |  | 1.6<br><sub>-,1,2,1,2</sub> |  | 0.7<br><sub>-,3,0,0,0</sub> |  | 0.7<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.6 | 8.2 |
| Bub Carrington | 88% | 10.9<br><sub>23,2,-,6,3</sub> | 3.4<br><sub>11,0,-,3,0</sub> |  | 1.1<br><sub>0,0,-,0,0</sub> |  | 1.4<br><sub>4,0,-,0,0</sub> |  | 0.4<br><sub>3,0,-,1,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.9 |
| Deandre Ayton | 99% | 10.3<br><sub>10,8,9,11,5</sub> | 3.1<br><sub>2,4,0,0,0</sub> |  | 3.0<br><sub>1,0,3,4,2</sub> |  | 0.4<br><sub>0,1,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 6.5 |
| Will Riley | 91% | 10.0<br><sub>16,2,10,6,9</sub> | 4.0<br><sub>14,2,0,0,4</sub> |  | 1.3<br><sub>3,1,3,1,3</sub> |  | 0.8<br><sub>0,0,0,1,1</sub> |  | 0.3<br><sub>2,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.0 |
| Anthony Gill | 52% | 7.0<br><sub>6,2,-,-,3</sub> | 2.6<br><sub>5,2,-,-,0</sub> |  | 1.2<br><sub>1,0,-,-,2</sub> |  | 0.5<br><sub>0,0,-,-,1</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |
| Tre Mann | 52% | 5.9<br><sub>11,2,-,-,3</sub> | 2.2<br><sub>4,2,-,-,0</sub> |  | 0.8<br><sub>1,0,-,-,0</sub> |  | 0.7<br><sub>1,1,-,-,0</sub> |  | 0.1<br><sub>1,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |

</details>


### DAL @ DEN
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.3–121.8 | DAL 28% | 3.62 / 1.38 | DEN -8.5 | 234.5 | DEN -7.5 covers 53%; o233.5 53% |
| Expected (weighted by chance each plays) | 113.5–121.5 | DAL 29% | 3.47 / 1.41 | DEN -7.5 | 234.5 | DEN -7.5 covers 51%; o233.5 53% |
| if P.J. Washington plays | 113.8–121.2 | DAL 30% | 3.32 / 1.43 | DEN -7.5 | 234.5 | DEN -7.5 covers 50%; o233.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington (DAL) | Questionable | 55% | 28.0 | 12.7 | 5.9 | 1.5 | 1.6 | 0.8 | 0.8 | 1.2 | 20.1 | full tables below |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 99% | 35.1<br><sub>38,27,34,36,31</sub> | 23.6<br><sub>18,17,33,22,28</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>8,3,5,6,3</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>5,4,9,8,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,2,3,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.7 | 2.7 | 36.2 |
| Kyrie Irving | 98% | 34.1<br><sub>37,-,29,35,27</sub> | 20.8<br><sub>34,-,17,25,16</sub> | 23.5 · –<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>6,-,6,6,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.4<br><sub>5,-,5,4,8</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>7,-,1,3,4</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.4 | 1.6 | 29.6 |
| Naji Marshall | 96% | 25.8<br><sub>30,23,27,14,25</sub> | 12.3<br><sub>12,13,12,4,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>3,2,5,3,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>5,2,2,1,4</sub> |  | 0.9<br><sub>0,3,2,0,1</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.1 | 1.4 | 18.9 |
| Daniel Gafford | 99% | 25.7<br><sub>17,19,24,31,28</sub> | 10.6<br><sub>10,3,6,10,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>3,4,6,10,4</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>1,2,2,3,4</sub> |  | 0.0<br><sub>1,0,0,0,0</sub> |  | 0.8 | 1.3 | 1.0 | 19.3 |
| Zaccharie Risacher | 98% | 24.9<br><sub>14,27,18,29,28</sub> | 9.4<br><sub>5,18,3,11,15</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>2,5,3,7,8</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,0,0,1,2</sub> |  | 1.1<br><sub>1,1,1,1,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.6 | 0.9 | 15.5 |
| Caleb Martin | 98% | 23.8<br><sub>33,34,20,20,29</sub> | 6.3<br><sub>15,12,8,0,13</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>8,5,5,4,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,5,3,3,4</sub> |  | 0.8<br><sub>1,4,2,0,3</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 0.7 | 12.2 |
| Walter Clayton Jr. | 96% | 21.1<br><sub>13,23,27,25,21</sub> | 8.0<br><sub>2,13,8,16,9</sub> |  | 2.9<br><sub>2,4,2,5,0</sub> |  | 3.3<br><sub>2,3,7,1,3</sub> |  | 1.0<br><sub>0,3,2,2,2</sub> |  | 0.6 | 0.1 | 1.4 | 14.2 |
| Morez Johnson Jr. | 99% | 18.5<br><sub>15,26,15,17,20</sub> | 6.9<br><sub>4,2,3,9,7</sub> |  | 3.6<br><sub>2,6,1,7,6</sub> |  | 1.6<br><sub>0,4,1,2,2</sub> |  | 0.4<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.1 | 0.9 | 12.2 |
| Max Christie | 98% | 17.4<br><sub>-,-,8,24,16</sub> | 6.3<br><sub>-,-,5,13,3</sub> |  | 2.1<br><sub>-,-,1,4,2</sub> |  | 1.0<br><sub>-,-,2,0,0</sub> |  | 0.9<br><sub>-,-,1,3,1</sub> |  | 0.5 | 0.2 | 0.6 | 9.3 |
| Santi Aldama | 98% | 16.0<br><sub>16,-,6,9,16</sub> | 7.6<br><sub>7,-,0,0,9</sub> |  | 3.5<br><sub>2,-,0,1,4</sub> |  | 1.2<br><sub>1,-,0,0,1</sub> |  | 0.9<br><sub>2,-,0,0,1</sub> |  | 0.5 | 0.3 | 0.7 | 12.3 |
| Marcus Sasser | 52% | 11.6<br><sub>-,18,4,-,-</sub> | 4.0<br><sub>-,5,0,-,-</sub> |  | 1.1<br><sub>-,1,2,-,-</sub> |  | 1.4<br><sub>-,2,1,-,-</sub> |  | 0.5<br><sub>-,1,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.5 |
| Moussa Cisse | 52% | 7.3<br><sub>-,4,4,-,-</sub> | 2.2<br><sub>-,1,0,-,-</sub> |  | 2.6<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.5 | 0.3 | 5.0 |
| Jett Howard | 52% | 6.4<br><sub>-,7,-,-,-</sub> | 2.8<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.9 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 99% | 35.7<br><sub>37,38,39,38,42</sub> | 26.6<br><sub>26,28,24,26,37</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 12.7<br><sub>8,15,8,7,18</sub> | 11.5<br><sub>o 55% · u 45%</sub> | 11.0<br><sub>10,7,9,11,11</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,2,3,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.9 | 3.4 | 50.2 |
| Jamal Murray | 99% | 35.5<br><sub>38,35,38,36,45</sub> | 25.0<br><sub>23,28,21,14,45</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>7,4,7,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>9,4,2,7,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>0,1,2,1,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.6 | 2.3 | 36.5 |
| Christian Braun | 99% | 31.0<br><sub>28,33,35,31,38</sub> | 13.0<br><sub>17,10,15,19,21</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>7,3,5,5,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>1,3,3,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,2,1,3,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 1.0 | 20.2 |
| Cameron Johnson | 98% | 28.6<br><sub>31,27,26,29,36</sub> | 13.4<br><sub>12,9,8,19,16</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>5,0,5,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,1,1,6,5</sub> |  | 1.8<br><sub>1,0,0,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.3 | 1.1 | 19.7 |
| Aaron Gordon | 99% | 27.9<br><sub>33,24,31,31,33</sub> | 13.5<br><sub>11,11,13,18,18</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 5.3<br><sub>5,1,8,3,8</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,1,2,2,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>1,2,0,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.4 | 1.2 | 21.4 |
| DeMar DeRozan | 93% | 19.5<br><sub>24,14,25,22,18</sub> | 10.1<br><sub>9,2,18,15,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>3,1,2,2,0</sub> |  | 2.7<br><sub>2,1,2,2,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.2 | 1.0 | 14.9 |
| Spencer Jones | 91% | 15.5<br><sub>12,21,17,18,20</sub> | 4.0<br><sub>4,4,2,3,0</sub> |  | 2.5<br><sub>2,3,2,1,4</sub> |  | 0.8<br><sub>1,3,0,1,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.4 | 0.6 | 7.4 |
| Trevon Brazile | 98% | 13.5<br><sub>16,23,11,11,15</sub> | 4.9<br><sub>5,9,0,4,8</sub> |  | 3.4<br><sub>3,4,6,4,0</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,1,0,0,2</sub> |  | 0.4 | 0.4 | 0.6 | 8.9 |
| Marvin Bagley III | 98% | 11.2<br><sub>13,10,9,10,11</sub> | 6.0<br><sub>7,4,4,10,2</sub> |  | 3.7<br><sub>7,2,3,6,2</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,2,0</sub> |  | 0.3 | 0.5 | 0.6 | 10.3 |
| Tyus Jones | 98% | 8.8<br><sub>10,10,9,14,8</sub> | 2.3<br><sub>2,0,0,5,0</sub> |  | 0.8<br><sub>0,1,0,3,0</sub> |  | 1.8<br><sub>3,2,0,4,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.9 |
| Julian Strawther | 52% | 7.4<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| Bryce Hopkins | 52% | 6.7<br><sub>-,4,-,-,-</sub> | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Cam Whitmore | 58% | 6.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.1 |
| Zeke Nnaji | 16% | 6.0<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.0 |
| Ryan Nembhard | 38% | 6.0<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.7 |
| Alpha Diallo | 35% | 5.8<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.7 |
| DaRon Holmes II | 52% | 5.5<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.3 |

</details>

<details><summary>if P.J. Washington plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 99% | 32.7<br><sub>38,27,34,36,31</sub> | 21.7<br><sub>18,17,33,22,28</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>8,3,5,6,3</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>5,4,9,8,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>0,2,3,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.7 | 2.6 | 33.4 |
| Kyrie Irving (DAL) | 98% | 31.9<br><sub>37,-,29,35,27</sub> | 19.1<br><sub>34,-,17,25,16</sub> | 23.5 · –<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>6,-,6,6,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.4<br><sub>5,-,5,4,8</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>7,-,1,3,4</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.4 | 1.7 | 27.4 |
| P.J. Washington (DAL) | 100% | 28.0<br><sub>26,25,25,-,-</sub> | 12.7<br><sub>10,8,21,-,-</sub> | 12.5 · – | 5.9<br><sub>4,5,5,-,-</sub> | 5.5 | 1.5<br><sub>1,4,2,-,-</sub> |  | 1.6<br><sub>2,0,5,-,-</sub> | 1.5 | 0.8 | 0.8 | 1.2 | 20.1 |
| Naji Marshall (DAL) | 96% | 22.8<br><sub>30,23,27,14,25</sub> | 10.6<br><sub>12,13,12,4,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,2,5,3,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>5,2,2,1,4</sub> |  | 0.8<br><sub>0,3,2,0,1</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.1 | 1.3 | 16.5 |
| Daniel Gafford (DAL) | 99% | 22.2<br><sub>17,19,24,31,28</sub> | 9.3<br><sub>10,3,6,10,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>3,4,6,10,4</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>1,2,2,3,4</sub> |  | 0.0<br><sub>1,0,0,0,0</sub> |  | 0.6 | 1.1 | 1.0 | 16.9 |
| Zaccharie Risacher (DAL) | 98% | 21.2<br><sub>14,27,18,29,28</sub> | 8.2<br><sub>5,18,3,11,15</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>2,5,3,7,8</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>0,0,0,1,2</sub> |  | 0.9<br><sub>1,1,1,1,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.7 | 0.5 | 0.8 | 13.6 |
| Caleb Martin (DAL) | 98% | 19.8<br><sub>33,34,20,20,29</sub> | 5.4<br><sub>15,12,8,0,13</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>8,5,5,4,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>3,5,3,3,4</sub> |  | 0.6<br><sub>1,4,2,0,3</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 0.6 | 10.3 |
| Walter Clayton Jr. (DAL) | 96% | 18.8<br><sub>13,23,27,25,21</sub> | 7.1<br><sub>2,13,8,16,9</sub> |  | 2.6<br><sub>2,4,2,5,0</sub> |  | 3.1<br><sub>2,3,7,1,3</sub> |  | 0.9<br><sub>0,3,2,2,2</sub> |  | 0.5 | 0.1 | 1.3 | 12.8 |
| Max Christie (DAL) | 98% | 15.8<br><sub>-,-,8,24,16</sub> | 5.9<br><sub>-,-,5,13,3</sub> |  | 1.9<br><sub>-,-,1,4,2</sub> |  | 0.9<br><sub>-,-,2,0,0</sub> |  | 0.8<br><sub>-,-,1,3,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.7 |
| Morez Johnson Jr. (DAL) | 99% | 15.5<br><sub>15,26,15,17,20</sub> | 6.0<br><sub>4,2,3,9,7</sub> |  | 3.1<br><sub>2,6,1,7,6</sub> |  | 1.4<br><sub>0,4,1,2,2</sub> |  | 0.3<br><sub>0,0,0,1,1</sub> |  | 0.4 | 0.1 | 0.8 | 10.4 |
| Santi Aldama (DAL) | 98% | 13.4<br><sub>16,-,6,9,16</sub> | 6.4<br><sub>7,-,0,0,9</sub> |  | 2.9<br><sub>2,-,0,1,4</sub> |  | 1.1<br><sub>1,-,0,0,1</sub> |  | 0.7<br><sub>2,-,0,0,1</sub> |  | 0.4 | 0.3 | 0.6 | 10.4 |
| Marcus Sasser (DAL) | 52% | 7.9<br><sub>-,18,4,-,-</sub> | 2.8<br><sub>-,5,0,-,-</sub> |  | 0.7<br><sub>-,1,2,-,-</sub> |  | 1.1<br><sub>-,2,1,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |
| Moussa Cisse (DAL) | 52% | 6.5<br><sub>-,4,4,-,-</sub> | 2.2<br><sub>-,1,0,-,-</sub> |  | 2.2<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.4 | 0.3 | 4.6 |
| Jett Howard (DAL) | 52% | 5.8<br><sub>-,7,-,-,-</sub> | 2.8<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |
| Nikola Jokic (DEN) | 99% | 35.7<br><sub>37,38,39,38,42</sub> | 26.5<br><sub>26,28,24,26,37</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 12.7<br><sub>8,15,8,7,18</sub> | 11.5<br><sub>o 55% · u 45%</sub> | 11.0<br><sub>10,7,9,11,11</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,2,3,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.9 | 3.5 | 50.2 |
| Jamal Murray (DEN) | 99% | 35.6<br><sub>38,35,38,36,45</sub> | 25.0<br><sub>23,28,21,14,45</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>7,4,7,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>9,4,2,7,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>0,1,2,1,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.6 | 2.3 | 36.6 |
| Christian Braun (DEN) | 99% | 31.0<br><sub>28,33,35,31,38</sub> | 12.9<br><sub>17,10,15,19,21</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>7,3,5,5,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>1,3,3,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,2,1,3,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 1.0 | 20.1 |
| Cameron Johnson (DEN) | 98% | 28.5<br><sub>31,27,26,29,36</sub> | 13.3<br><sub>12,9,8,19,16</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>5,0,5,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,1,1,6,5</sub> |  | 1.8<br><sub>1,0,0,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.3 | 1.1 | 19.6 |
| Aaron Gordon (DEN) | 99% | 27.9<br><sub>33,24,31,31,33</sub> | 13.5<br><sub>11,11,13,18,18</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 5.3<br><sub>5,1,8,3,8</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,1,2,2,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>1,2,0,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.4 | 1.2 | 21.3 |
| DeMar DeRozan (DEN) | 93% | 19.5<br><sub>24,14,25,22,18</sub> | 10.1<br><sub>9,2,18,15,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>3,1,2,2,0</sub> |  | 2.8<br><sub>2,1,2,2,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.2 | 1.0 | 14.9 |
| Spencer Jones (DEN) | 91% | 15.4<br><sub>12,21,17,18,20</sub> | 4.0<br><sub>4,4,2,3,0</sub> |  | 2.5<br><sub>2,3,2,1,4</sub> |  | 0.8<br><sub>1,3,0,1,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.4 | 0.6 | 7.4 |
| Trevon Brazile (DEN) | 98% | 13.5<br><sub>16,23,11,11,15</sub> | 4.9<br><sub>5,9,0,4,8</sub> |  | 3.4<br><sub>3,4,6,4,0</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,1,0,0,2</sub> |  | 0.4 | 0.4 | 0.6 | 8.9 |
| Marvin Bagley III (DEN) | 98% | 11.2<br><sub>13,10,9,10,11</sub> | 6.0<br><sub>7,4,4,10,2</sub> |  | 3.7<br><sub>7,2,3,6,2</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,2,0</sub> |  | 0.3 | 0.5 | 0.6 | 10.3 |
| Tyus Jones (DEN) | 98% | 8.9<br><sub>10,10,9,14,8</sub> | 2.4<br><sub>2,0,0,5,0</sub> |  | 0.8<br><sub>0,1,0,3,0</sub> |  | 1.8<br><sub>3,2,0,4,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |
| Julian Strawther (DEN) | 52% | 7.6<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Bryce Hopkins (DEN) | 52% | 6.7<br><sub>-,4,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.0 |
| Cam Whitmore (DEN) | 58% | 6.7<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.2 |
| Zeke Nnaji (DEN) | 16% | 6.1<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.0 |
| Ryan Nembhard (DEN) | 38% | 5.9<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.6 |
| Alpha Diallo (DEN) | 35% | 5.8<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.6 |
| DaRon Holmes II (DEN) | 52% | 5.6<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-24/`._
