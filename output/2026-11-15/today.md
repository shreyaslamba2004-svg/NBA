# NBA model · Sun 15 Nov 2026 (US date)

Updated **Mon 16 Nov, 01:02 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-15/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Cardwell REB over 13.5 (14+) | OKC @ SAC | draftkings | 20.40 | 15.82 | 5.64 | 17.7% | 4.6% | 6.3% | +28.9% | +261.8% | 0.4% |
| SAC to win | OKC @ SAC | draftkings | 5.58 | 4.72 | 7.23 | 13.8% | 21.2% | 21.2% | +18.2% | -22.8% | 1.0% |
| Domantas Sabonis PA over 34.5 (35+) | OKC @ SAC | draftkings | 23.00 | 20.75 | 10.19 | 9.8% | 4.1% | 4.8% | +10.9% | +125.6% | 0.1% |
| Domantas Sabonis PA over 29.5 (30+) | OKC @ SAC | draftkings | 10.20 | 9.25 | 4.62 | 21.7% | 9.2% | 10.8% | +10.3% | +120.9% | 0.3% |
| Domantas Sabonis PTS over 29.5 (30+) | OKC @ SAC | draftkings | 30.00 | 27.70 | 14.58 | 6.9% | 3.1% | 3.6% | +8.3% | +105.8% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Cardwell PTS over 5.5 (6+) | OKC @ SAC | pointsbetau | 2.05 | 1.88 | 1.37 | 73.0% | 50.3% | 53.3% | +9.3% | +49.7% | 2.0% |

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
| Keegan Murray PTS over 13.5 (14+) | OKC @ SAC | sportsbet | 2.00 | 1.94 | 1.61 | 62.0% | 50.1% | 51.7% | +3.3% | +23.9% | 0.8% |
| Isaiah Hartenstein PTS under 9.5 | OKC @ SAC | pointsbetau | 2.05 | 2.02 | 1.99 | 50.3% | 49.4% | 49.5% | +1.5% | +3.2% | 0.4% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 32.0<br><sub>30,29,29,36,39</sub> | 30.7<br><sub>28,30,26,31,40</sub> | 31.5 · 32.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>3,2,8,4,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.8<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.8 | 2.3 | 40.2 |
| Jared McCain | 100% | 26.9<br><sub>29,23,31,31,31</sub> | 15.3<br><sub>21,19,21,10,23</sub> | 14.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.1 | 1.4 | 20.5 |
| Ajay Mitchell | 100% | 26.4<br><sub>30,22,28,-,-</sub> | 15.5<br><sub>35,12,14,-,-</sub> | 18.5 · 17.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,4,3,-,-</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>5,0,3,-,-</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>4,0,0,-,-</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 1.6 | 22.5 |
| Isaiah Hartenstein | 100% | 25.5<br><sub>26,18,24,34,30</sub> | 10.2<br><sub>2,2,7,20,21</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 10.0<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>7,6,5,6,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.5 | 23.9 |
| Kenrich Williams | 100% | 24.3<br><sub>19,23,19,26,35</sub> | 9.6<br><sub>4,9,3,11,8</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>6,4,2,2,8</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.2 | 0.8 | 16.3 |
| Alex Caruso | 98% | 21.7<br><sub>20,13,19,29,27</sub> | 8.8<br><sub>5,0,5,14,5</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>6,3,2,7,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>2,3,1,2,4</sub> |  | 1.3<br><sub>1,0,1,4,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.5 | 0.5 | 0.9 | 14.7 |
| Aday Mara | 98% | 21.6<br><sub>18,27,26,32,21</sub> | 8.8<br><sub>9,18,10,11,10</sub> | 8.5 · 9.5<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>7,8,10,6,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.6 | 1.3 | 16.1 |
| Bennett Stirtz | 98% | 16.2<br><sub>24,29,18,25,12</sub> | 6.5<br><sub>12,11,13,6,5</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,5,1,1,1</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.0<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.1 | 0.5 | 8.9 |
| Josh Dix | 67% | 15.1<br><sub>15,21,-,-,17</sub> | 5.6<br><sub>5,2,-,-,0</sub> |  | 1.9<br><sub>2,1,-,-,4</sub> |  | 0.8<br><sub>1,2,-,-,3</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.2 |
| Nique Clifford | 96% | 13.3<br><sub>-,-,20,16,12</sub> | 4.9<br><sub>-,-,4,5,0</sub> |  | 2.0<br><sub>-,-,4,3,0</sub> |  | 1.3<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.2 |
| Micah Peavy | 88% | 13.0<br><sub>18,23,21,12,-</sub> | 3.7<br><sub>7,7,0,0,-</sub> |  | 2.3<br><sub>4,3,2,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.3<br><sub>1,1,0,0,-</sub> |  | 0.5 | 0.2 | 0.3 | 6.4 |
| Nikola Topic | 72% | 11.5<br><sub>-,-,-,-,16</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 2.6<br><sub>-,-,-,-,3</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.1 | 1.1 | 7.6 |
| Brooks Barnhizer | 52% | 7.0<br><sub>5,8,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 1.6<br><sub>0,4,1,-,-</sub> |  | 0.6<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 100% | 39.5<br><sub>42,33,39,40,35</sub> | 25.9<br><sub>22,22,32,29,17</sub> | 26.5 · 26.5<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 7.8<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>3,3,3,4,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.3 | 4.1 | 37.7 |
| Keegan Murray | 100% | 35.9<br><sub>-,-,23,24,40</sub> | 16.3<br><sub>-,-,10,11,16</sub> | 13.5 · 13.5<br><sub>o 52% · u 48%</sub> | 5.9<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>-,-,2,1,4</sub> |  | 2.2<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 1.3 | 1.7 | 24.3 |
| Domantas Sabonis | 100% | 35.1<br><sub>35,31,-,24,35</sub> | 17.7<br><sub>16,17,-,0,21</sub> | 13.5 · 13.5<br><sub>o 53% · u 47%</sub> | 13.5<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>1,5,-,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.6<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.4 | 3.3 | 37.1 |
| Malik Monk | 100% | 29.8<br><sub>24,18,21,3,18</sub> | 17.3<br><sub>13,12,9,1,7</sub> | 14.5 · 13.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,0,2,0,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>3,7,3,0,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.5 | 2.3 | 25.3 |
| Dylan Cardwell | 100% | 27.5<br><sub>13,15,18,29,13</sub> | 8.4<br><sub>4,9,4,1,6</sub> | 5.5 · 5.5<br><sub>o 53% · u 47%</sub> | 9.9<br><sub>6,2,9,11,3</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.5 | 20.6 |
| Leaky Black | 80% | 25.0<br><sub>22,40,20,18,12</sub> | 6.7<br><sub>3,12,6,0,0</sub> |  | 4.1<br><sub>6,3,5,3,0</sub> |  | 1.5<br><sub>1,5,1,2,0</sub> |  | 1.1<br><sub>0,4,2,0,0</sub> |  | 1.1 | 0.5 | 0.9 | 12.3 |
| Emanuel Sharp | 98% | 22.6<br><sub>10,31,12,19,7</sub> | 6.6<br><sub>3,9,5,2,4</sub> |  | 2.1<br><sub>1,5,1,2,0</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 1.0<br><sub>1,3,1,0,0</sub> |  | 0.7 | 0.3 | 0.8 | 9.8 |
| Daeqwon Plowden | 83% | 17.0<br><sub>-,-,12,2,2</sub> | 6.3<br><sub>-,-,6,0,0</sub> |  | 1.9<br><sub>-,-,0,0,0</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 1.0<br><sub>-,-,2,0,0</sub> |  | 0.5 | 0.1 | 0.6 | 8.9 |
| Alex Karaban | 48% | 16.6<br><sub>-,11,-,-,-</sub> | 5.2<br><sub>-,0,-,-,-</sub> |  | 2.3<br><sub>-,1,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.8 | 8.4 |
| Mason Plumlee | 30% | 15.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.6 | 0.9 | 10.1 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-15/`._
