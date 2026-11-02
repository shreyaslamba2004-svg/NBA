# NBA model · Sun 01 Nov 2026 (US date)

Updated **Mon 02 Nov, 12:43 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-01/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 7.5 (8+) | TOR @ LAL | draftkings | 3.68 | 3.48 | 2.58 | 38.8% | 25.4% | 28.7% | +5.7% | +42.6% | 0.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 11.5 (12+) | TOR @ LAL | draftkings | 23.00 | 19.96 | 12.76 | 7.8% | 4.1% | 5.0% | +15.1% | +80.2% | 0.2% |
| Scottie Barnes AST over 9.5 (10+) | TOR @ LAL | draftkings | 9.30 | 8.13 | 5.25 | 19.0% | 10.1% | 12.3% | +14.3% | +77.0% | 0.4% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walker Kessler PTS under 12.5 | TOR @ LAL | tab | 1.90 | 1.79 | 1.46 | 68.3% | 51.9% | 56.0% | +6.5% | +29.9% | 1.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| TOR @ LAL | Mon 02 Nov 13:00 | 110.4–113.4 | TOR 42% | 2.40 / 1.72 | LAL -3.5 | 223.5 | LAL -3.5 covers 49%; o223.5 51% |

### TOR @ LAL
Out: Ziaire Williams (LAL), Kawhi Leonard (TOR), Malachi Smith (TOR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic PTS under 33.5 | TOR @ LAL | pointsbetau | 1.87 | 1.84 | 1.62 | 61.7% | 52.0% | 54.4% | +1.8% | +15.4% | 0.5% |
| Scottie Barnes PTS under 22.5 | TOR @ LAL | pointsbetau | 1.95 | 1.93 | 1.70 | 58.9% | 49.3% | 51.7% | +0.9% | +15.0% | 0.2% |
| Walker Kessler PTS under 11.5 | TOR @ LAL | unibet | 2.00 | 1.98 | 1.63 | 61.2% | 46.8% | 50.4% | +0.8% | +22.4% | 0.2% |
| Jakob Poeltl PTS over 6.5 (7+) | TOR @ LAL | draftkings | 1.84 | 1.83 | 1.58 | 63.3% | 51.6% | 54.6% | +0.4% | +16.6% | 0.1% |
| Walker Kessler PA under 13.5 | TOR @ LAL | draftkings | 1.86 | 1.86 | 1.55 | 64.6% | 50.2% | 53.8% | +0.2% | +20.4% | 0.1% |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 100% | 35.4<br><sub>26,37,28,31,39</sub> | 21.7<br><sub>23,28,0,28,41</sub> | 22.5 · 22.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>6,14,3,6,5</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 6.9<br><sub>5,5,3,4,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.9 | 1.0 | 3.4 | 35.4 |
| RJ Barrett | 100% | 34.3<br><sub>26,34,32,32,34</sub> | 20.8<br><sub>20,23,20,25,9</sub> | 20.5 · 20.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>4,9,2,9,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>3,4,2,6,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.3 | 2.7 | 30.6 |
| Immanuel Quickley | 100% | 32.1<br><sub>28,29,28,29,37</sub> | 17.0<br><sub>23,12,19,16,17</sub> | 16.5 · 17.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>4,1,3,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>7,6,2,7,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>4,0,3,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.1 | 1.8 | 26.9 |
| Ja'Kobe Walter | 100% | 30.0<br><sub>23,24,31,28,32</sub> | 11.5<br><sub>10,7,22,14,9</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>3,4,4,5,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>1,2,5,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.2 | 1.0 | 16.9 |
| Jamal Shead | 98% | 24.5<br><sub>16,24,21,23,23</sub> | 7.5<br><sub>2,5,4,13,2</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,2,1,4,1</sub> |  | 5.0<br><sub>5,5,0,7,8</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>0,0,0,1,0</sub> |  | 1.1 | 0.2 | 1.9 | 14.3 |
| Jakob Poeltl | 100% | 22.9<br><sub>22,27,19,10,23</sub> | 8.6<br><sub>3,6,0,2,12</sub> | 6.5 · 6.5<br><sub>o 55% · u 45%</sub> | 6.4<br><sub>6,9,1,2,11</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,2,0,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.6 | 1.2 | 16.5 |
| Collin Murray-Boyles | 98% | 22.9<br><sub>20,18,19,15,23</sub> | 9.6<br><sub>6,8,3,10,15</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>8,3,7,2,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,2,1</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.7 | 1.3 | 16.8 |
| Jamison Battle | 96% | 16.9<br><sub>11,12,13,20,19</sub> | 5.9<br><sub>8,5,4,7,2</sub> |  | 2.2<br><sub>5,0,1,0,0</sub> |  | 0.8<br><sub>0,0,2,1,0</sub> |  | 0.9<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.1 | 0.5 | 9.0 |
| Allen Graves | 96% | 14.2<br><sub>19,6,20,18,9</sub> | 4.4<br><sub>5,2,11,3,7</sub> |  | 2.9<br><sub>5,2,6,1,4</sub> |  | 0.7<br><sub>0,0,4,0,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.5 | 0.8 | 8.0 |
| Kyle Anderson | 58% | 9.9<br><sub>5,-,11,5,-</sub> | 2.9<br><sub>0,-,0,0,-</sub> |  | 1.8<br><sub>1,-,2,0,-</sub> |  | 1.5<br><sub>2,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.5 | 0.2 | 0.7 | 6.2 |
| Trayce Jackson-Davis | 91% | 9.1<br><sub>10,1,6,20,1</sub> | 3.5<br><sub>9,0,3,6,0</sub> |  | 2.6<br><sub>1,0,1,11,0</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.5 | 6.8 |
| Alijah Martin | 67% | 5.9<br><sub>5,1,7,5,-</sub> | 2.3<br><sub>3,0,2,5,-</sub> |  | 0.8<br><sub>0,0,2,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.7 |
| Jaden Bradley | 67% | 5.8<br><sub>5,1,5,5,-</sub> | 2.0<br><sub>0,0,6,0,-</sub> |  | 0.9<br><sub>0,0,1,1,-</sub> |  | 0.5<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.4 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 100% | 36.4<br><sub>37,38,37,-,37</sub> | 31.3<br><sub>23,52,41,-,37</sub> | 32.5 · 32.5<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>6,8,5,-,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 7.3<br><sub>7,10,9,-,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 4.1<br><sub>2,8,6,-,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.5 | 4.7 | 45.6 |
| Austin Reaves | 100% | 35.7<br><sub>38,36,39,31,37</sub> | 20.0<br><sub>28,29,26,16,21</sub> | 22.5 · 22.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,1,4,6,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.0<br><sub>9,4,7,1,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>3,4,4,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 3.6 | 29.2 |
| Walker Kessler | 100% | 30.0<br><sub>35,28,33,26,31</sub> | 10.8<br><sub>22,2,13,11,10</sub> | 12.5 · 12.5<br><sub>o 44% · u 56%</sub> | 10.1<br><sub>8,7,8,9,13</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.2 | 1.6 | 22.2 |
| Jake LaRavia | 100% | 27.1<br><sub>-,15,19,35,28</sub> | 7.3<br><sub>-,0,5,2,10</sub> | 6.5 · 6.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>-,4,1,10,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>-,1,1,0,0</sub> |  | 0.8<br><sub>-,0,1,0,2</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.7 | 1.4 | 12.8 |
| Quentin Grimes | 98% | 25.9<br><sub>31,20,19,38,26</sub> | 8.8<br><sub>13,3,2,23,3</sub> |  | 3.1<br><sub>8,1,4,3,3</sub> |  | 2.2<br><sub>4,1,0,5,2</sub> |  | 1.0<br><sub>3,0,0,0,1</sub> |  | 0.8 | 0.3 | 1.1 | 14.0 |
| Matisse Thybulle | 100% | 25.2<br><sub>24,26,22,28,28</sub> | 7.9<br><sub>13,11,5,15,10</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>1,1,2,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>2,1,1,0,0</sub> |  | 1.3<br><sub>3,3,1,4,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.9 | 0.7 | 1.1 | 11.6 |
| Sandro Mamukelashvili | 98% | 22.8<br><sub>24,21,24,30,20</sub> | 8.8<br><sub>7,9,17,13,4</sub> | 7.5 · 8.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>5,3,4,8,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,0,2,3,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,1,3,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.5 | 0.9 | 15.5 |
| Collin Sexton | 98% | 18.0<br><sub>16,20,14,21,16</sub> | 9.9<br><sub>5,13,9,21,0</sub> | 8.5 · 8.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>1,2,1,4,2</sub> |  | 1.8<br><sub>2,1,4,2,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>1,1,0,4,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 1.6 | 13.6 |
| Jarred Vanderbilt | 52% | 14.2<br><sub>-,-,-,21,13</sub> | 3.3<br><sub>-,-,-,0,0</sub> |  | 3.7<br><sub>-,-,-,7,3</sub> |  | 1.1<br><sub>-,-,-,2,3</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.1 |
| Lawson Lovering | 16% | 13.9 | 4.2 |  | 3.5 |  | 0.8 |  | 0.1 |  | 0.5 | 0.4 | 0.6 | 8.6 |
| Cameron Carr | 16% | 12.3 | 5.2 |  | 2.2 |  | 1.1 |  | 0.4 |  | 0.4 | 0.2 | 0.6 | 8.5 |
| AK Okereke | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.1 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.1 |
| Kevon Looney | 52% | 7.7<br><sub>5,5,5,-,-</sub> | 1.8<br><sub>0,2,0,-,-</sub> |  | 2.6<br><sub>1,2,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.0 |
| Jaden Hardy | 63% | 7.3<br><sub>-,-,-,9,1</sub> | 3.7<br><sub>-,-,-,2,0</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Bronny James | 48% | 5.5<br><sub>-,-,-,-,1</sub> | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 2.6 |
| Chris Manon | 58% | 5.5<br><sub>-,-,-,-,1</sub> | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-01/`._
