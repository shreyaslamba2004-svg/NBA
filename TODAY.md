# NBA model · Wed 11 Nov 2026 (US date)

Updated **Thu 12 Nov, 01:53 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-11/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kenrich Williams PTS over 9.5 (10+) | OKC @ POR | draftkings | 2.92 | 2.52 | 2.43 | 41.1% | 39.4% | 39.6% | +15.7% | +20.0% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ POR | draftkings | 15.40 | 13.12 | 5.62 | 17.8% | 6.1% | 7.6% | +17.3% | +174.0% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ POR | Thu 12 Nov 14:00 | 111.9–110.4 | OKC 54% | 1.86 / 2.16 | POR +1.5 | 222.5 | POR -2.5 covers 40%; o224.5 45% |

### OKC @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), Chet Holmgren (OKC), Ajay Mitchell (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kenrich Williams PTS over 9.5 (10+) | OKC @ POR | draftkings | 2.92 | 2.52 | 2.43 | 41.1% | 39.4% | 39.6% | +15.7% | +20.0% | 2.0% |
| Toumani Camara PTS under 12.5 | OKC @ POR | tab | 1.95 | 1.94 | 1.66 | 60.3% | 50.2% | 51.5% | +0.6% | +17.8% | 0.2% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 34.6<br><sub>39,35,30,29,29</sub> | 31.5<br><sub>43,42,28,30,26</sub> | 33.5 · 33.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,4,3,2,8</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 6.8<br><sub>8,8,4,9,3</sub> | 4.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>4,5,3,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4 | 1.0 | 3.3 | 42.4 |
| Jared McCain | 100% | 31.0<br><sub>27,25,29,23,31</sub> | 15.3<br><sub>7,9,21,19,21</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>9,1,5,5,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,0,0,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>0,1,3,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.2 | 2.1 | 21.0 |
| Aday Mara | 100% | 28.7<br><sub>20,25,18,27,26</sub> | 11.8<br><sub>10,9,9,18,10</sub> | 10.5 · 9.5<br><sub>o 53% · u 47%</sub> | 8.7<br><sub>9,5,7,8,10</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,2,0,3,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.5 | 2.0 | 1.8 | 22.2 |
| Alex Caruso | 100% | 28.6<br><sub>-,20,20,13,19</sub> | 10.8<br><sub>-,7,5,0,5</sub> | 8.5 · 7.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>-,4,6,3,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>-,3,2,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>-,1,1,0,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.6 | 1.4 | 18.4 |
| Isaiah Hartenstein | 100% | 26.9<br><sub>28,26,26,18,24</sub> | 10.0<br><sub>5,3,2,2,7</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 10.1<br><sub>14,12,6,14,9</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,4,7,6,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.6 | 23.9 |
| Bennett Stirtz | 98% | 25.4<br><sub>12,22,24,29,18</sub> | 9.1<br><sub>9,16,12,11,13</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,1,1,5,1</sub> |  | 1.8<br><sub>0,1,2,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>3,4,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.0 | 13.0 |
| Kenrich Williams | 98% | 25.2<br><sub>31,29,19,23,19</sub> | 9.2<br><sub>12,13,4,9,3</sub> | 7.5 · 8.5<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>3,4,6,4,2</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>2,3,1,1,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.2 | 1.0 | 16.1 |
| Micah Peavy | 88% | 23.2<br><sub>16,26,18,23,21</sub> | 6.3<br><sub>8,2,7,7,0</sub> |  | 4.0<br><sub>5,9,4,3,2</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 0.7<br><sub>2,0,1,1,0</sub> |  | 0.8 | 0.3 | 0.6 | 11.1 |
| Josh Dix | 76% | 19.1<br><sub>12,-,15,21,-</sub> | 4.4<br><sub>0,-,5,2,-</sub> |  | 1.9<br><sub>1,-,2,1,-</sub> |  | 0.9<br><sub>0,-,1,2,-</sub> |  | 0.4<br><sub>0,-,1,0,-</sub> |  | 0.6 | 0.3 | 0.6 | 7.1 |
| Nique Clifford | 91% | 18.4<br><sub>-,-,-,-,20</sub> | 6.6<br><sub>-,-,-,-,4</sub> |  | 2.8<br><sub>-,-,-,-,4</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.3 | 1.2 | 11.2 |
| Brooks Barnhizer | 72% | 11.8<br><sub>-,-,5,8,5</sub> | 3.0<br><sub>-,-,0,2,0</sub> |  | 2.5<br><sub>-,-,0,4,1</sub> |  | 0.9<br><sub>-,-,0,3,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.4 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 100% | 33.8<br><sub>35,35,39,24,34</sub> | 21.3<br><sub>28,21,22,15,24</sub> | 22.5 · 22.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>3,7,9,4,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>5,12,11,1,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 3.5 | 34.9 |
| Damian Lillard | 100% | 30.8<br><sub>30,33,37,20,24</sub> | 17.2<br><sub>20,25,22,12,25</sub> | 20.5 · 19.5<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>6,3,0,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>6,5,4,7,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,2,4,2,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 2.3 | 25.8 |
| Toumani Camara | 100% | 30.2<br><sub>31,32,30,21,30</sub> | 11.7<br><sub>9,11,18,4,12</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>5,4,6,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,2,1,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>3,1,4,0,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.3 | 1.4 | 17.7 |
| Jrue Holiday | 98% | 28.2<br><sub>31,28,31,20,25</sub> | 12.7<br><sub>17,15,12,11,11</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>8,4,1,0,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.5<br><sub>10,0,7,0,2</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>3,5,3,1,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.2 | 1.9 | 21.2 |
| Sidy Cissoko | 100% | 28.2<br><sub>22,21,22,16,33</sub> | 8.2<br><sub>8,7,7,4,17</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>3,4,2,3,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>0,4,3,1,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>2,1,2,0,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.4 | 1.2 | 14.5 |
| Donovan Clingan | 100% | 26.7<br><sub>32,29,28,22,26</sub> | 11.0<br><sub>17,24,17,6,7</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 10.6<br><sub>18,11,11,5,13</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>3,1,1,0,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>1,1,3,0,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.5 | 1.5 | 1.4 | 23.5 |
| Scoot Henderson | 98% | 25.7<br><sub>26,22,23,24,23</sub> | 11.3<br><sub>8,9,2,13,11</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>2,2,2,2,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>2,1,0,1,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 2.3 | 16.6 |
| Robert Williams III | 98% | 17.6<br><sub>15,16,16,-,15</sub> | 6.4<br><sub>2,9,9,-,6</sub> | 5.5 · 4.5<br><sub>o 53% · u 47%</sub> | 6.4<br><sub>6,8,5,-,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,1,2,-,0</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.6 | 1.0 | 0.9 | 14.1 |
| Jayson Kent | 64% | 11.3<br><sub>-,-,-,12,-</sub> | 4.3<br><sub>-,-,-,4,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 6.5 |
| Micah Potter | 67% | 9.6<br><sub>-,2,-,14,5</sub> | 4.0<br><sub>-,4,-,7,0</sub> |  | 2.6<br><sub>-,1,-,3,3</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4<br><sub>-,1,-,1,0</sub> |  | 0.2 | 0.2 | 0.5 | 7.1 |
| Branden Carlson | 64% | 9.5<br><sub>-,3,-,12,8</sub> | 2.8<br><sub>-,2,-,4,2</sub> |  | 2.3<br><sub>-,0,-,2,5</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.5 | 5.6 |
| Yang Hansen | 80% | 9.4<br><sub>-,2,3,26,5</sub> | 3.6<br><sub>-,0,2,12,0</sub> |  | 2.4<br><sub>-,0,0,10,1</sub> |  | 0.5<br><sub>-,0,0,1,0</sub> |  | 0.2<br><sub>-,0,0,1,0</sub> |  | 0.2 | 0.2 | 0.7 | 6.5 |
| John Tonje | 52% | 6.8<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-11/`._
