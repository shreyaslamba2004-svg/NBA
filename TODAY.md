# NBA model · Sun 01 Nov 2026 (US date)

Updated **Mon 02 Nov, 01:08 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-01/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 7.5 (8+) | TOR @ LAL | draftkings | 3.73 | 3.50 | 2.56 | 39.0% | 25.1% | 28.5% | +6.5% | +45.5% | 0.6% |
| Jamal Shead PTS over 6.5 (7+) | TOR @ LAL | pointsbetau | 2.05 | 1.94 | 1.60 | 62.7% | 47.9% | 51.6% | +5.8% | +28.5% | 1.4% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 9.5 (10+) | TOR @ LAL | draftkings | 9.50 | 8.33 | 5.40 | 18.5% | 9.8% | 12.0% | +14.1% | +75.9% | 0.4% |
| Scottie Barnes AST over 11.5 (12+) | TOR @ LAL | draftkings | 23.00 | 20.41 | 13.52 | 7.4% | 4.1% | 4.9% | +12.6% | +70.1% | 0.1% |
| Scottie Barnes PA over 44.5 (45+) | TOR @ LAL | draftkings | 17.20 | 15.29 | 10.16 | 9.8% | 5.4% | 6.5% | +12.4% | +69.3% | 0.2% |
| RJ Barrett REB over 9.5 (10+) | TOR @ LAL | draftkings | 13.00 | 11.99 | 8.47 | 11.8% | 7.2% | 8.3% | +8.5% | +53.4% | 0.2% |
| RJ Barrett REB over 7.5 (8+) | TOR @ LAL | draftkings | 5.01 | 4.71 | 3.46 | 28.9% | 18.6% | 21.2% | +6.3% | +44.8% | 0.4% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walker Kessler PTS under 12.5 | TOR @ LAL | tab | 1.90 | 1.79 | 1.48 | 67.5% | 51.9% | 55.8% | +6.1% | +28.4% | 1.7% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| TOR @ LAL | Mon 02 Nov 13:00 | 110.5–114.1 | TOR 40% | 2.49 / 1.67 | LAL -3.5 | 224.5 | LAL -3.5 covers 51%; o224.5 50% |

### TOR @ LAL
Out: Ziaire Williams (LAL), Kawhi Leonard (TOR), Jakob Poeltl (TOR), Malachi Smith (TOR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Shead PTS over 6.5 (7+) | TOR @ LAL | pointsbetau | 2.05 | 1.94 | 1.60 | 62.7% | 47.9% | 51.6% | +5.8% | +28.5% | 1.4% |
| Luka Doncic PTS under 33.5 | TOR @ LAL | pointsbetau | 1.87 | 1.85 | 1.63 | 61.2% | 51.6% | 54.0% | +0.9% | +14.4% | 0.2% |
| Walker Kessler PTS under 11.5 | TOR @ LAL | unibet | 2.00 | 1.99 | 1.66 | 60.3% | 46.8% | 50.2% | +0.3% | +20.7% | 0.1% |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 36.4<br><sub>26,37,28,31,39</sub> | 23.7<br><sub>23,28,0,28,41</sub> | 22.5 · 22.5<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>6,14,3,6,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.9<br><sub>5,5,3,4,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 2.0 | 1.0 | 3.5 | 37.6 |
| RJ Barrett | 98% | 35.4<br><sub>26,34,32,32,34</sub> | 21.6<br><sub>20,23,20,25,9</sub> | 20.5 · 20.5<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>4,9,2,9,3</sub> | 4.5<br><sub>o 61% · u 39%</sub> | 4.2<br><sub>3,4,2,6,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.3 | 2.7 | 31.9 |
| Immanuel Quickley | 98% | 33.1<br><sub>28,29,28,29,37</sub> | 17.4<br><sub>23,12,19,16,17</sub> | 16.5 · 17.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>4,1,3,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>7,6,2,7,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>4,0,3,4,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.5 | 0.1 | 1.8 | 27.4 |
| Ja'Kobe Walter | 98% | 31.4<br><sub>23,24,31,28,32</sub> | 12.1<br><sub>10,7,22,14,9</sub> | 11.5 · 11.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>3,4,4,5,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>4,2,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>1,2,5,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.8 | 0.3 | 1.1 | 17.7 |
| Jamal Shead | 98% | 27.0<br><sub>16,24,21,23,23</sub> | 8.4<br><sub>2,5,4,13,2</sub> | 6.5 · 6.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,2,1,4,1</sub> |  | 5.5<br><sub>5,5,0,7,8</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>0,0,0,1,0</sub> |  | 1.3 | 0.2 | 2.0 | 16.0 |
| Collin Murray-Boyles | 98% | 25.3<br><sub>20,18,19,15,23</sub> | 10.7<br><sub>6,8,3,10,15</sub> | 10.5 · 9.5<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>8,3,7,2,5</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.3<br><sub>0,0,0,2,1</sub> | 0.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.8 | 1.4 | 18.8 |
| Jamison Battle | 96% | 19.8<br><sub>11,12,13,20,19</sub> | 6.9<br><sub>8,5,4,7,2</sub> |  | 2.7<br><sub>5,0,1,0,0</sub> |  | 0.9<br><sub>0,0,2,1,0</sub> |  | 1.1<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 10.6 |
| Allen Graves | 96% | 17.0<br><sub>19,6,20,18,9</sub> | 5.2<br><sub>5,2,11,3,7</sub> |  | 3.6<br><sub>5,2,6,1,4</sub> |  | 0.8<br><sub>0,0,4,0,0</sub> |  | 0.5<br><sub>0,0,1,0,1</sub> |  | 0.6 | 0.6 | 0.9 | 9.6 |
| Kyle Anderson | 58% | 13.6<br><sub>5,-,11,5,-</sub> | 3.9<br><sub>0,-,0,0,-</sub> |  | 2.5<br><sub>1,-,2,0,-</sub> |  | 2.0<br><sub>2,-,0,1,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.7 | 0.3 | 0.8 | 8.4 |
| Trayce Jackson-Davis | 91% | 11.7<br><sub>10,1,6,20,1</sub> | 4.2<br><sub>9,0,3,6,0</sub> |  | 3.5<br><sub>1,0,1,11,0</sub> |  | 0.9<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.5 | 8.7 |
| Alijah Martin | 67% | 7.7<br><sub>5,1,7,5,-</sub> | 2.9<br><sub>3,0,2,5,-</sub> |  | 1.1<br><sub>0,0,2,1,-</sub> |  | 0.7<br><sub>0,0,1,1,-</sub> |  | 0.2<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.6 | 4.7 |
| Jaden Bradley | 67% | 7.5<br><sub>5,1,5,5,-</sub> | 2.2<br><sub>0,0,6,0,-</sub> |  | 1.2<br><sub>0,0,1,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.0 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.8<br><sub>37,38,37,-,37</sub> | 31.7<br><sub>23,52,41,-,37</sub> | 33.5 · 32.5<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>6,8,5,-,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 7.4<br><sub>7,10,9,-,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>2,8,6,-,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.5 | 4.7 | 46.0 |
| Austin Reaves | 98% | 36.0<br><sub>38,36,39,31,37</sub> | 20.7<br><sub>28,29,26,16,21</sub> | 22.5 · 22.5<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>2,1,4,6,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.0<br><sub>9,4,7,1,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,4,4,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 3.6 | 29.9 |
| Walker Kessler | 98% | 30.1<br><sub>35,28,33,26,31</sub> | 10.8<br><sub>22,2,13,11,10</sub> | 12.5 · 12.5<br><sub>o 44% · u 56%</sub> | 10.2<br><sub>8,7,8,9,13</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.2 | 1.6 | 22.4 |
| Quentin Grimes | 98% | 26.6<br><sub>31,20,19,38,26</sub> | 9.3<br><sub>13,3,2,23,3</sub> |  | 3.2<br><sub>8,1,4,3,3</sub> |  | 2.2<br><sub>4,1,0,5,2</sub> |  | 1.1<br><sub>3,0,0,0,1</sub> |  | 0.8 | 0.3 | 1.2 | 14.7 |
| Matisse Thybulle | 96% | 24.4<br><sub>24,26,22,28,28</sub> | 7.8<br><sub>13,11,5,15,10</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,1,2,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>2,1,1,0,0</sub> |  | 1.2<br><sub>3,3,1,4,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.8 | 0.7 | 1.0 | 11.2 |
| Jake LaRavia | 93% | 24.2<br><sub>-,15,19,35,28</sub> | 6.6<br><sub>-,0,5,2,10</sub> | 6.5 · 6.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>-,4,1,10,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>-,1,1,0,0</sub> |  | 0.7<br><sub>-,0,1,0,2</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.6 | 1.3 | 11.5 |
| Sandro Mamukelashvili | 98% | 23.2<br><sub>24,21,24,30,20</sub> | 9.1<br><sub>7,9,17,13,4</sub> | 7.5 · 8.5<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,3,4,8,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,0,2,3,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,1,3,0,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.5 | 1.0 | 15.9 |
| Collin Sexton | 98% | 18.1<br><sub>16,20,14,21,16</sub> | 10.2<br><sub>5,13,9,21,0</sub> | 8.5 · 8.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>1,2,1,4,2</sub> |  | 1.8<br><sub>2,1,4,2,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>1,1,0,4,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 1.6 | 13.9 |
| Lawson Lovering | 16% | 14.4 | 4.3 |  | 3.6 |  | 0.9 |  | 0.1 |  | 0.5 | 0.4 | 0.6 | 8.8 |
| Jarred Vanderbilt | 52% | 14.2<br><sub>-,-,-,21,13</sub> | 3.4<br><sub>-,-,-,0,0</sub> |  | 3.6<br><sub>-,-,-,7,3</sub> |  | 1.1<br><sub>-,-,-,2,3</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.1 |
| Cameron Carr | 16% | 12.5 | 5.3 |  | 2.3 |  | 1.1 |  | 0.4 |  | 0.4 | 0.2 | 0.7 | 8.7 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 52% | 8.0<br><sub>5,5,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 2.7<br><sub>1,2,0,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.1 |
| Jaden Hardy | 63% | 7.7<br><sub>-,-,-,9,1</sub> | 3.9<br><sub>-,-,-,2,0</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.1 |
| Bronny James | 48% | 5.7<br><sub>-,-,-,-,1</sub> | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 2.7 |
| Chris Manon | 58% | 5.7<br><sub>-,-,-,-,1</sub> | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-01/`._
