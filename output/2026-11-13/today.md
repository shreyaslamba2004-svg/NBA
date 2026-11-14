# NBA model · Fri 13 Nov 2026 (US date)

Updated **Sat 14 Nov, 02:31 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-13/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aday Mara PTS under 11.5 | OKC @ LAC | draftkings | 2.06 | 1.95 | 1.82 | 54.9% | 50.7% | 51.3% | +5.6% | +13.0% | 1.3% |

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
| OKC @ LAC | Sat 14 Nov 14:30 | 113.1–109.4 | OKC 61% | 1.65 / 2.53 | LAC +3.5 | 222.5 | LAC +6.5 covers 58%; o221.5 52% |

### OKC @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Chet Holmgren (OKC), Ajay Mitchell (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aday Mara PTS under 11.5 | OKC @ LAC | draftkings | 2.06 | 1.95 | 1.82 | 54.9% | 50.7% | 51.3% | +5.6% | +13.0% | 1.3% |
| Alex Caruso PTS over 7.5 (8+) | OKC @ LAC | draftkings | 1.91 | 1.88 | 1.54 | 64.8% | 51.3% | 53.1% | +1.4% | +23.8% | 0.4% |
| Keaton Wagler PTS under 10.5 | OKC @ LAC | tab | 1.87 | 1.86 | 1.55 | 64.4% | 52.2% | 53.8% | +0.5% | +20.3% | 0.2% |
| Alex Caruso PTS under 8.5 | OKC @ LAC | tab | 1.95 | 1.94 | 2.28 | 43.9% | 52.6% | 51.4% | +0.4% | -14.2% | 0.1% |
| Jared McCain PTS over 15.5 (16+) | OKC @ LAC | pointsbetau | 2.00 | 1.99 | 1.90 | 52.6% | 49.8% | 50.2% | +0.3% | +5.2% | 0.1% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 34.9<br><sub>35,30,29,29,36</sub> | 31.4<br><sub>42,28,30,26,31</sub> | 32.5 · 33.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,3,2,8,4</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 7.0<br><sub>8,4,9,3,2</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>5,3,3,0,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.7 | 3.3 | 42.6 |
| Jared McCain | 100% | 31.2<br><sub>25,29,23,31,31</sub> | 16.9<br><sub>9,21,19,21,10</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>1,5,5,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>0,0,2,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.5<br><sub>1,3,2,4,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.2 | 2.1 | 23.0 |
| Aday Mara | 100% | 29.8<br><sub>25,18,27,26,32</sub> | 11.6<br><sub>9,9,18,10,11</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>5,7,8,10,6</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>2,0,3,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.5 | 1.7 | 1.9 | 21.9 |
| Isaiah Hartenstein | 100% | 28.5<br><sub>26,26,18,24,34</sub> | 10.5<br><sub>3,2,2,7,20</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 10.6<br><sub>12,6,14,9,11</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 4.0<br><sub>4,7,6,5,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.9 | 25.1 |
| Kenrich Williams | 100% | 25.6<br><sub>29,19,23,19,26</sub> | 9.8<br><sub>13,4,9,3,11</sub> | 7.5 · 8.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>4,6,4,2,2</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>3,1,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 1.1 | 16.8 |
| Alex Caruso | 98% | 25.5<br><sub>20,20,13,19,29</sub> | 10.0<br><sub>7,5,0,5,14</sub> | 7.5 · 8.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>4,6,3,2,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.4 | 1.2 | 17.0 |
| Bennett Stirtz | 98% | 24.6<br><sub>22,24,29,18,25</sub> | 9.6<br><sub>16,12,11,13,6</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,1,5,1,1</sub> |  | 1.7<br><sub>1,2,3,1,1</sub> |  | 1.6<br><sub>4,2,2,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 1.0 | 13.2 |
| Micah Peavy | 88% | 19.1<br><sub>26,18,23,21,12</sub> | 4.9<br><sub>2,7,7,0,0</sub> |  | 3.2<br><sub>9,4,3,2,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.5<br><sub>0,1,1,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 8.8 |
| Nique Clifford | 93% | 18.0<br><sub>-,-,-,20,16</sub> | 6.3<br><sub>-,-,-,4,5</sub> |  | 2.8<br><sub>-,-,-,4,3</sub> |  | 1.8<br><sub>-,-,-,1,1</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 10.9 |
| Josh Dix | 63% | 17.4<br><sub>-,15,21,-,-</sub> | 4.4<br><sub>-,5,2,-,-</sub> |  | 1.6<br><sub>-,2,1,-,-</sub> |  | 0.9<br><sub>-,1,2,-,-</sub> |  | 0.5<br><sub>-,1,0,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.0 |
| Brooks Barnhizer | 63% | 9.5<br><sub>-,5,8,5,-</sub> | 2.2<br><sub>-,0,2,0,-</sub> |  | 2.0<br><sub>-,0,4,1,-</sub> |  | 0.7<br><sub>-,0,3,1,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.9 |
| Nikola Topic | 63% | 8.8 | 2.7 |  | 1.0 |  | 2.0 |  | 0.2 |  | 0.4 | 0.1 | 1.0 | 5.7 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 100% | 30.8<br><sub>33,36,39,32,25</sub> | 17.9<br><sub>15,16,26,24,13</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>0,4,1,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>7,8,7,10,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>1,1,4,3,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 3.2 | 26.6 |
| Rui Hachimura | 100% | 28.2<br><sub>30,-,37,26,23</sub> | 14.1<br><sub>24,-,21,14,13</sub> | 14.5 · 15.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,-,9,3,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>0,-,7,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 2.0<br><sub>4,-,1,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.3 | 1.4 | 20.1 |
| Derrick Jones Jr. | 100% | 26.8<br><sub>28,-,37,29,24</sub> | 10.1<br><sub>9,-,12,8,11</sub> | 10.5 · 9.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>7,-,8,4,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,-,1,3,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4<br><sub>1,-,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.7 | 1.1 | 15.5 |
| Kris Dunn | 100% | 25.7<br><sub>27,30,35,24,19</sub> | 7.5<br><sub>12,12,5,14,3</sub> | 7.5 · 7.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,4,5,5,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>4,1,3,4,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>0,1,1,2,1</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.3 | 1.4 | 14.4 |
| Brook Lopez | 100% | 24.4<br><sub>19,22,35,26,19</sub> | 11.7<br><sub>7,12,20,20,8</sub> | 10.5 · 10.5<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>2,6,8,7,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.5<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 1.0 | 1.2 | 17.8 |
| Kobe Sanders | 98% | 22.0<br><sub>30,38,18,22,26</sub> | 9.2<br><sub>16,26,4,8,9</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>0,3,1,4,7</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>4,5,0,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 1.4 | 13.9 |
| Keaton Wagler | 98% | 20.9<br><sub>19,24,16,18,23</sub> | 9.4<br><sub>7,6,11,15,11</sub> | 10.5 · 10.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>4,4,2,2,0</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>4,4,1,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,0,3,3,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.2 | 1.7 | 15.4 |
| Max Strus | 98% | 20.9<br><sub>-,23,23,19,22</sub> | 8.4<br><sub>-,11,9,7,12</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>-,4,5,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>-,6,5,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>-,3,3,1,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.5 | 0.2 | 1.0 | 14.5 |
| Isaiah Jackson | 98% | 17.1<br><sub>22,26,13,-,16</sub> | 6.9<br><sub>5,19,2,-,4</sub> |  | 5.2<br><sub>8,8,4,-,4</sub> |  | 1.2<br><sub>2,2,2,-,0</sub> |  | 0.0<br><sub>0,1,0,-,0</sub> |  | 0.8 | 0.8 | 1.3 | 13.3 |
| Gradey Dick | 96% | 14.4<br><sub>3,29,7,17,19</sub> | 6.6<br><sub>0,12,4,15,10</sub> |  | 2.3<br><sub>1,4,2,4,3</sub> |  | 0.7<br><sub>0,3,1,0,2</sub> |  | 0.7<br><sub>0,0,0,2,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.6 |
| Baba Miller | 93% | 14.3<br><sub>6,12,6,20,16</sub> | 6.2<br><sub>2,4,2,12,13</sub> |  | 2.4<br><sub>2,0,1,5,4</sub> |  | 1.5<br><sub>1,1,1,4,0</sub> |  | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.9 | 10.1 |
| Jalen Pickett | 58% | 7.6<br><sub>6,-,-,2,8</sub> | 2.8<br><sub>0,-,-,0,3</sub> |  | 1.0<br><sub>2,-,-,0,1</sub> |  | 1.1<br><sub>3,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,1</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Blake Wesley | 52% | 6.1<br><sub>4,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Cam Christie | 58% | 6.0<br><sub>6,-,-,2,-</sub> | 2.3<br><sub>3,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-13/`._
