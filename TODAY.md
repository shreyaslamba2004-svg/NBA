# NBA model · Tue 10 Nov 2026 (US date)

Updated **Wed 11 Nov, 02:40 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-10/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ POR | draftkings | 13.60 | 12.00 | 5.58 | 17.9% | 6.9% | 8.3% | +13.3% | +143.6% | 0.3% |
| Damian Lillard AST over 7.5 (8+) | OKC @ POR | draftkings | 10.10 | 9.57 | 5.46 | 18.3% | 9.2% | 10.4% | +5.5% | +84.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ POR | Wed 11 Nov 15:00 | 114.0–109.2 | OKC 63% | 1.58 / 2.71 | POR +5.5 | 222.5 | POR +1.5 covers 40%; o226.5 43% |

### OKC @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aday Mara PTS over 7.5 (8+) | OKC @ POR | draftkings | 1.93 | 1.87 | 1.60 | 62.4% | 52.1% | 53.5% | +3.0% | +20.1% | 0.8% |
| Donovan Clingan PTS over 10.5 (11+) | OKC @ POR | tab | 1.95 | 1.95 | 1.94 | 51.5% | 51.3% | 51.3% | +0.2% | +0.5% | 0.1% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 34.3<br><sub>31,39,35,30,29</sub> | 30.0<br><sub>26,43,42,28,30</sub> | – · 32.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,3,4,3,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 6.8<br><sub>3,8,8,4,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,4,5,3,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.5 | 0.9 | 3.0 | 40.7 |
| Ajay Mitchell | 100% | 29.0<br><sub>26,35,32,30,22</sub> | 17.2<br><sub>6,20,23,35,12</sub> | 18.5 · 19.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>3,5,7,1,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>5,1,4,5,0</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,0,1,4,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.4 | 1.9 | 24.7 |
| Jared McCain | 100% | 28.5<br><sub>28,27,25,29,23</sub> | 13.8<br><sub>10,7,9,21,19</sub> | 14.5 · 12.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>4,9,1,5,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,2,0,0,2</sub> |  | 2.0<br><sub>0,0,1,3,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.8 | 19.0 |
| Isaiah Hartenstein | 100% | 26.3<br><sub>25,28,26,26,18</sub> | 9.6<br><sub>10,5,3,2,2</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 10.1<br><sub>7,14,12,6,14</sub> |  | 3.5<br><sub>0,4,4,7,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.3 | 0.8 | 1.6 | 23.2 |
| Kenrich Williams | 100% | 24.4<br><sub>21,31,29,19,23</sub> | 8.7<br><sub>11,12,13,4,9</sub> | 6.5 · 7.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>7,3,4,6,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>3,1,2,3,2</sub> |  | 1.2<br><sub>3,2,3,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 0.2 | 0.9 | 15.7 |
| Aday Mara | 98% | 24.1<br><sub>28,20,25,18,27</sub> | 9.6<br><sub>7,10,9,9,18</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>9,9,5,7,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>3,0,2,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.5 | 1.8 | 1.7 | 18.1 |
| Bennett Stirtz | 98% | 23.5<br><sub>26,12,22,24,29</sub> | 7.8<br><sub>11,9,16,12,11</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,2,1,1,5</sub> |  | 1.6<br><sub>3,0,1,2,3</sub> |  | 1.2<br><sub>3,3,4,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.9 | 11.2 |
| Micah Peavy | 86% | 20.6<br><sub>14,16,26,18,23</sub> | 5.5<br><sub>2,8,2,7,7</sub> |  | 3.9<br><sub>1,5,9,4,3</sub> |  | 1.0<br><sub>0,0,1,0,0</sub> |  | 0.6<br><sub>0,2,0,1,1</sub> |  | 0.8 | 0.3 | 0.7 | 10.3 |
| Alex Caruso | 98% | 20.3<br><sub>-,-,20,20,13</sub> | 7.0<br><sub>-,-,7,5,0</sub> | 7.5 · 6.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>-,-,4,6,3</sub> | 3.5<br><sub>o 44% · u 55%</sub> | 2.4<br><sub>-,-,3,2,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>-,-,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.4 | 0.8 | 12.6 |
| Josh Dix | 76% | 18.4<br><sub>9,12,-,15,21</sub> | 4.1<br><sub>7,0,-,5,2</sub> |  | 1.7<br><sub>0,1,-,2,1</sub> |  | 0.8<br><sub>0,0,-,1,2</sub> |  | 0.4<br><sub>1,0,-,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 6.6 |
| Brooks Barnhizer | 67% | 9.8<br><sub>6,-,-,5,8</sub> | 2.4<br><sub>5,-,-,0,2</sub> |  | 2.1<br><sub>2,-,-,0,4</sub> |  | 0.7<br><sub>0,-,-,0,3</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.3 |
| Nique Clifford | 91% | 9.3<br><sub>11,3,3,5,-</sub> | 3.2<br><sub>0,0,0,5,-</sub> |  | 1.4<br><sub>1,1,2,2,-</sub> |  | 1.0<br><sub>2,0,0,2,-</sub> |  | 0.2<br><sub>0,0,0,1,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.7 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 100% | 33.2<br><sub>30,35,35,39,24</sub> | 20.5<br><sub>24,28,21,22,15</sub> | 23.5 · 22.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>5,3,7,9,4</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.5<br><sub>2,5,12,11,1</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 3.7 | 33.6 |
| Damian Lillard | 100% | 30.7<br><sub>27,30,33,37,20</sub> | 16.3<br><sub>22,20,25,22,12</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,6,3,0,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>4,6,5,4,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,1,2,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.2 | 2.5 | 25.1 |
| Toumani Camara | 100% | 29.5<br><sub>31,31,32,30,21</sub> | 11.5<br><sub>14,9,11,18,4</sub> | 13.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>4,5,4,6,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,1,2,1,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>4,3,1,4,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.4 | 1.5 | 17.4 |
| Jrue Holiday | 98% | 27.4<br><sub>22,31,28,31,20</sub> | 12.7<br><sub>14,17,15,12,11</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>4,8,4,1,0</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.5<br><sub>3,10,0,7,0</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,3,5,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.9 | 21.2 |
| Donovan Clingan | 100% | 26.3<br><sub>15,32,29,28,22</sub> | 11.5<br><sub>4,17,24,17,6</sub> | 11.5 · 10.5<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>9,18,11,11,5</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>0,3,1,1,0</sub> |  | 1.1<br><sub>0,1,1,3,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.5 | 1.4 | 1.4 | 23.4 |
| Sidy Cissoko | 100% | 25.2<br><sub>19,22,21,22,16</sub> | 7.2<br><sub>1,8,7,7,4</sub> | 5.5 · 4.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>3,3,4,2,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,0,4,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9<br><sub>0,2,1,2,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.4 | 1.2 | 12.8 |
| Scoot Henderson | 98% | 24.7<br><sub>31,26,22,23,24</sub> | 11.1<br><sub>14,8,9,2,13</sub> | 8.5 · 10.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>3,2,2,2,2</sub> |  | 2.5<br><sub>1,2,1,0,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>1,2,1,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.8 | 0.2 | 2.3 | 16.1 |
| Chris Youngblood | 88% | 19.2<br><sub>7,15,4,11,30</sub> | 7.5<br><sub>3,7,0,7,11</sub> |  | 2.4<br><sub>0,2,0,1,4</sub> |  | 1.5<br><sub>0,1,1,0,4</sub> |  | 1.3<br><sub>1,1,0,2,2</sub> |  | 0.5 | 0.3 | 0.8 | 11.4 |
| Robert Williams III | 98% | 16.1<br><sub>14,15,16,16,-</sub> | 5.9<br><sub>3,2,9,9,-</sub> | 5.5 · 5.5<br><sub>o 51% · u 49%</sub> | 6.0<br><sub>3,6,8,5,-</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,2,1,2,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.6 | 1.0 | 0.8 | 13.1 |
| Yang Hansen | 72% | 12.1<br><sub>13,-,2,3,26</sub> | 4.9<br><sub>6,-,0,2,12</sub> |  | 3.1<br><sub>5,-,0,0,10</sub> |  | 0.7<br><sub>1,-,0,0,1</sub> |  | 0.4<br><sub>2,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.9 | 8.6 |
| Micah Potter | 63% | 10.2<br><sub>4,-,2,-,14</sub> | 4.3<br><sub>2,-,4,-,7</sub> |  | 2.6<br><sub>1,-,1,-,3</sub> |  | 0.6<br><sub>0,-,0,-,1</sub> |  | 0.5<br><sub>0,-,1,-,1</sub> |  | 0.2 | 0.2 | 0.6 | 7.5 |
| Branden Carlson | 58% | 9.0<br><sub>4,-,3,-,12</sub> | 2.9<br><sub>0,-,2,-,4</sub> |  | 1.9<br><sub>2,-,0,-,2</sub> |  | 0.5<br><sub>1,-,0,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.4 | 0.5 | 5.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-10/`._
