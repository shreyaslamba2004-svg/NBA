# NBA model · Sun 15 Nov 2026 (US date)

Updated **Mon 16 Nov, 12:22 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-15/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | OKC @ SAC | draftkings | 5.43 | 4.72 | 7.23 | 13.8% | 21.2% | 21.2% | +15.1% | -24.9% | 0.9% |
| Domantas Sabonis PA over 34.5 (35+) | OKC @ SAC | draftkings | 21.00 | 18.73 | 8.95 | 11.2% | 4.5% | 5.3% | +12.1% | +134.6% | 0.1% |
| Domantas Sabonis PTS over 29.5 (30+) | OKC @ SAC | draftkings | 28.00 | 25.25 | 12.40 | 8.1% | 3.3% | 4.0% | +10.9% | +125.8% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ SAC | Mon 16 Nov 13:00 | 120.5–105.1 | OKC 86% | 1.16 / 7.23 | SAC +15.5 | 225.5 | SAC +12.5 covers 42%; o221.5 59% |

### OKC @ SAC
Out: Precious Achiuwa (SAC), De'Andre Hunter (SAC), Zach LaVine (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keegan Murray PTS over 13.5 (14+) | OKC @ SAC | sportsbet | 2.00 | 1.93 | 1.56 | 64.0% | 49.8% | 51.7% | +3.4% | +28.1% | 0.8% |
| Isaiah Hartenstein PTS under 9.5 | OKC @ SAC | pointsbetau | 2.05 | 2.01 | 1.98 | 50.4% | 49.6% | 49.7% | +1.9% | +3.3% | 0.4% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 32.3<br><sub>30,29,29,36,39</sub> | 31.2<br><sub>28,30,26,31,40</sub> | 31.5 · 32.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>3,2,8,4,4</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 5.9<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.8 | 2.4 | 40.9 |
| Jared McCain | 98% | 26.2<br><sub>29,23,31,31,31</sub> | 14.8<br><sub>21,19,21,10,23</sub> | 14.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>0,2,3,3,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.1 | 1.4 | 19.9 |
| Ajay Mitchell | 98% | 26.1<br><sub>30,22,28,-,-</sub> | 15.4<br><sub>35,12,14,-,-</sub> | 18.5 · 17.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,4,3,-,-</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>5,0,3,-,-</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>4,0,0,-,-</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.3 | 1.6 | 22.3 |
| Isaiah Hartenstein | 98% | 25.4<br><sub>26,18,24,34,30</sub> | 10.1<br><sub>2,2,7,20,21</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 10.1<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>7,6,5,6,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.5 | 23.8 |
| Kenrich Williams | 98% | 22.6<br><sub>19,23,19,26,35</sub> | 9.1<br><sub>4,9,3,11,8</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 0.8 | 15.3 |
| Aday Mara | 98% | 21.7<br><sub>18,27,26,32,21</sub> | 8.9<br><sub>9,18,10,11,10</sub> | 8.5 · 9.5<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.6 | 1.3 | 16.2 |
| Alex Caruso | 98% | 21.6<br><sub>20,13,19,29,27</sub> | 8.8<br><sub>5,0,5,14,5</sub> |  | 3.2<br><sub>6,3,2,7,1</sub> |  | 2.6<br><sub>2,3,1,2,4</sub> |  | 1.3<br><sub>1,0,1,4,1</sub> |  | 1.4 | 0.5 | 0.9 | 14.6 |
| Bennett Stirtz | 98% | 16.3<br><sub>24,29,18,25,12</sub> | 6.6<br><sub>12,11,13,6,5</sub> |  | 1.3<br><sub>1,5,1,1,1</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.0<br><sub>2,2,2,2,1</sub> |  | 0.6 | 0.2 | 0.5 | 9.0 |
| Josh Dix | 67% | 15.3<br><sub>15,21,-,-,17</sub> | 5.7<br><sub>5,2,-,-,0</sub> |  | 1.9<br><sub>2,1,-,-,4</sub> |  | 0.8<br><sub>1,2,-,-,3</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.4 |
| Micah Peavy | 88% | 13.2<br><sub>18,23,21,12,-</sub> | 3.7<br><sub>7,7,0,0,-</sub> |  | 2.3<br><sub>4,3,2,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.3<br><sub>1,1,0,0,-</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Nique Clifford | 96% | 13.2<br><sub>-,-,20,16,12</sub> | 4.9<br><sub>-,-,4,5,0</sub> |  | 2.0<br><sub>-,-,4,3,0</sub> |  | 1.3<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.2 |
| Nikola Topic | 72% | 11.5<br><sub>-,-,-,-,16</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 2.7<br><sub>-,-,-,-,3</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.1 | 1.1 | 7.7 |
| Brooks Barnhizer | 52% | 7.0<br><sub>5,8,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 1.6<br><sub>0,4,1,-,-</sub> |  | 0.6<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 39.5<br><sub>42,33,39,40,35</sub> | 26.5<br><sub>22,22,32,29,17</sub> | 25.5 · 26.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.8<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.3 | 4.1 | 38.3 |
| Keegan Murray | 98% | 35.6<br><sub>-,-,23,24,40</sub> | 16.8<br><sub>-,-,10,11,16</sub> | 12.5 · 13.5<br><sub>o 52% · u 48%</sub> | 5.9<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>-,-,2,1,4</sub> |  | 2.2<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 1.3 | 1.7 | 24.7 |
| Domantas Sabonis | 98% | 34.7<br><sub>35,31,-,24,35</sub> | 18.1<br><sub>16,17,-,0,21</sub> | 13.5 · 13.5<br><sub>o 53% · u 47%</sub> | 13.6<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>1,5,-,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.6<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.4 | 3.4 | 37.6 |
| Leaky Black | 80% | 25.0<br><sub>22,40,20,18,12</sub> | 6.9<br><sub>3,12,6,0,0</sub> |  | 4.1<br><sub>6,3,5,3,0</sub> |  | 1.5<br><sub>1,5,1,2,0</sub> |  | 1.1<br><sub>0,4,2,0,0</sub> |  | 1.1 | 0.5 | 0.9 | 12.5 |
| Malik Monk | 98% | 24.7<br><sub>24,18,21,3,18</sub> | 14.9<br><sub>13,12,9,1,7</sub> | – · 13.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>2,0,2,0,4</sub> |  | 4.1<br><sub>3,7,3,0,3</sub> |  | 2.2<br><sub>3,2,0,0,0</sub> |  | 0.7 | 0.4 | 1.9 | 21.7 |
| Dylan Cardwell | 98% | 23.1<br><sub>13,15,18,29,13</sub> | 7.3<br><sub>4,9,4,1,6</sub> | – · 5.5<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>6,2,9,11,3</sub> |  | 1.9<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.2 | 17.5 |
| Emanuel Sharp | 98% | 22.9<br><sub>10,31,12,19,7</sub> | 7.1<br><sub>3,9,5,2,4</sub> |  | 2.1<br><sub>1,5,1,2,0</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.7 | 0.3 | 0.8 | 10.3 |
| Daeqwon Plowden | 83% | 17.0<br><sub>-,-,12,2,2</sub> | 6.4<br><sub>-,-,6,0,0</sub> |  | 1.9<br><sub>-,-,0,0,0</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 1.0<br><sub>-,-,2,0,0</sub> |  | 0.5 | 0.1 | 0.6 | 9.0 |
| Alex Karaban | 48% | 16.7<br><sub>-,11,-,-,-</sub> | 5.3<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,1,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.9 | 8.5 |
| Mason Plumlee | 30% | 16.1<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 5.2<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.7 | 1.0 | 10.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-15/`._
