# NBA model · Sat 21 Nov 2026 (US date)

Updated **Sun 22 Nov, 04:46 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-21/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cam Spencer AST over 9.5 (10+) | MEM @ MIN | draftkings | 11.20 | 9.56 | 4.53 | 22.1% | 8.3% | 10.5% | +17.2% | +147.3% | 0.4% |
| Cam Spencer AST over 11.5 (12+) | MEM @ MIN | draftkings | 25.00 | 21.46 | 10.27 | 9.7% | 3.7% | 4.7% | +16.5% | +143.4% | 0.2% |
| NOP to win | NOP @ SAS | betfair_ex_au | 10.98 | 9.96 | 6.20 | 16.1% | 10.0% | 10.0% | +10.2% | +77.0% | 0.2% |
| Cam Spencer PA over 29.5 (30+) | MEM @ MIN | draftkings | 17.00 | 15.48 | 8.53 | 11.7% | 5.5% | 6.5% | +9.8% | +99.3% | 0.1% |
| Cam Spencer PRA over 29.5 (30+) | MEM @ MIN | draftkings | 8.50 | 7.76 | 4.30 | 23.2% | 11.0% | 12.9% | +9.5% | +97.5% | 0.3% |
| Cam Spencer PRA over 34.5 (35+) | MEM @ MIN | draftkings | 18.80 | 17.18 | 9.54 | 10.5% | 5.0% | 5.8% | +9.4% | +97.0% | 0.1% |
| Kentavious Caldwell-Pope REB over 5.5 (6+) | MIL @ PHI | draftkings | 9.00 | 8.24 | 4.59 | 21.8% | 10.4% | 12.1% | +9.2% | +96.0% | 0.3% |
| Victor Wembanyama REB over 19.5 (20+) | NOP @ SAS | draftkings | 20.20 | 18.52 | 10.36 | 9.7% | 4.6% | 5.4% | +9.1% | +95.0% | 0.1% |
| Cam Spencer PA over 24.5 (25+) | MEM @ MIN | draftkings | 7.20 | 6.61 | 3.70 | 27.0% | 13.0% | 15.1% | +9.0% | +94.5% | 0.4% |
| Victor Wembanyama REB over 17.5 (18+) | NOP @ SAS | draftkings | 11.00 | 10.09 | 5.66 | 17.7% | 8.5% | 9.9% | +9.0% | +94.3% | 0.2% |
| Tyrese Maxey PTS over 39.5 (40+) | MIL @ PHI | draftkings | 18.20 | 16.72 | 9.39 | 10.6% | 5.1% | 6.0% | +8.9% | +93.7% | 0.1% |
| Tyrese Maxey PRA over 49.5 (50+) | MIL @ PHI | draftkings | 14.40 | 13.25 | 7.49 | 13.4% | 6.5% | 7.5% | +8.7% | +92.2% | 0.2% |
| Victor Wembanyama PRA over 64.5 (65+) | NOP @ SAS | draftkings | 15.40 | 14.22 | 8.11 | 12.3% | 6.1% | 7.0% | +8.3% | +90.0% | 0.1% |
| Tyrese Maxey PRA over 54.5 (55+) | MIL @ PHI | draftkings | 26.00 | 24.04 | 13.81 | 7.2% | 3.6% | 4.2% | +8.1% | +88.2% | 0.1% |
| Victor Wembanyama PRA over 69.5 (70+) | NOP @ SAS | draftkings | 24.00 | 22.37 | 13.15 | 7.6% | 3.9% | 4.5% | +7.2% | +82.5% | 0.1% |
| Darius Acuff Jr. AST over 11.5 (12+) | BOS @ SAC | draftkings | 17.00 | 15.90 | 9.38 | 10.7% | 5.5% | 6.3% | +7.0% | +81.3% | 0.1% |
| Victor Wembanyama REB over 15.5 (16+) | NOP @ SAS | draftkings | 5.85 | 5.51 | 3.33 | 30.1% | 16.0% | 18.1% | +6.2% | +75.8% | 0.3% |
| Victor Wembanyama BLK over 6.5 (7+) | NOP @ SAS | draftkings | 10.70 | 10.09 | 6.12 | 16.4% | 8.7% | 9.9% | +6.0% | +74.9% | 0.1% |
| Victor Wembanyama PTS over 49.5 (50+) | NOP @ SAS | draftkings | 24.00 | 22.68 | 13.82 | 7.2% | 3.9% | 4.4% | +5.8% | +73.7% | 0.1% |
| Victor Wembanyama BLK over 7.5 (8+) | NOP @ SAS | draftkings | 18.20 | 17.27 | 10.65 | 9.4% | 5.1% | 5.8% | +5.4% | +70.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cam Spencer PRA over 24.5 (25+) | MEM @ MIN | draftkings | 3.87 | 3.68 | 2.29 | 43.6% | 24.1% | 27.2% | +5.1% | +68.8% | 0.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MIL @ PHI | Sun 22 Nov 05:00 | 108.0–117.5 | MIL 25% | 4.00 / 1.33 | PHI -9.5 | 225.5 | PHI -11.5 covers 44%; o229.5 41% |
| POR @ NYK | Sun 22 Nov 11:30 | 107.9–111.4 | POR 40% | 2.47 / 1.68 | NYK -3.5 | 219.5 | NYK -3.5 covers 50%; o215.5 58% |
| LAC @ DAL | Sun 22 Nov 12:00 | 116.7–117.0 | LAC 49% | 2.04 / 1.97 | DAL +0.5 | 233.5 | DAL -5.5 covers 36%; o230.5 56% |
| MEM @ MIN | Sun 22 Nov 12:00 | 111.4–119.0 | MEM 29% | 3.45 / 1.41 | MIN -7.5 | 230.5 | MIN -6.5 covers 53%; o228.5 54% |
| NOP @ SAS | Sun 22 Nov 12:00 | 106.8–120.7 | NOP 16% | 6.20 / 1.19 | SAS -14.5 | 227.5 | SAS -18.5 covers 37%; o228.5 48% |
| BOS @ SAC | Sun 22 Nov 14:00 | 115.8–103.6 | BOS 80% | 1.24 / 5.09 | SAC +12.5 | 219.5 | SAC +13.5 covers 53%; o217.5 54% |

### MIL @ PHI
Out: Adem Bona (PHI), Jaylen Brown (PHI), Ariel Hukporti (PHI), Dean Wade (PHI), Ousmane Dieng (MIL), Kam Jones (MIL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| LeBron James PTS over 19.5 (20+) | MIL @ PHI | draftkings | 2.44 | 2.38 | 2.80 | 35.7% | 43.1% | 42.0% | +2.5% | -13.0% | 0.4% |
| VJ Edgecombe PTS under 14.5 | MIL @ PHI | tab | 2.00 | 1.96 | 1.96 | 50.9% | 51.0% | 51.0% | +2.0% | +1.8% | 0.5% |
| Kyle Kuzma PTS under 11.5 | MIL @ PHI | sportsbet | 2.02 | 1.99 | 1.74 | 57.5% | 49.0% | 50.3% | +1.6% | +16.1% | 0.4% |
| Myles Turner PTS under 9.5 | MIL @ PHI | unibet | 1.88 | 1.87 | 1.52 | 65.6% | 51.2% | 53.4% | +0.2% | +23.2% | 0.1% |

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 100% | 27.6<br><sub>35,34,20,24,31</sub> | 16.0<br><sub>27,18,5,8,19</sub> | – · 20.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>2,1,5,2,4</sub> |  | 3.7<br><sub>7,2,3,4,3</sub> |  | 1.9<br><sub>2,2,0,0,4</sub> |  | 0.7 | 0.3 | 2.1 | 23.7 |
| Jaime Jaquez Jr. | 100% | 26.2<br><sub>30,28,30,23,22</sub> | 13.2<br><sub>25,22,6,10,9</sub> | – · 12.5<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>5,6,5,2,1</sub> |  | 3.4<br><sub>3,4,4,5,2</sub> |  | 1.3<br><sub>2,5,2,1,1</sub> |  | 0.6 | 0.2 | 1.9 | 21.1 |
| Kyle Kuzma | 100% | 24.9<br><sub>24,31,22,30,-</sub> | 11.3<br><sub>9,14,14,26,-</sub> | – · 11.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>1,4,6,5,-</sub> |  | 2.2<br><sub>1,2,2,1,-</sub> |  | 1.2<br><sub>1,1,3,2,-</sub> |  | 0.6 | 0.4 | 1.6 | 18.0 |
| Ryan Rollins | 100% | 24.5<br><sub>24,29,-,-,21</sub> | 11.7<br><sub>8,8,-,-,15</sub> |  | 4.1<br><sub>7,10,-,-,3</sub> |  | 4.2<br><sub>4,2,-,-,6</sub> |  | 1.6<br><sub>2,0,-,-,1</sub> |  | 1.0 | 0.3 | 2.3 | 20.0 |
| Myles Turner | 100% | 23.7<br><sub>-,31,23,21,-</sub> | 8.3<br><sub>-,14,8,4,-</sub> | 9.5 · 9.5<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>-,11,7,5,-</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>-,3,1,4,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>-,4,1,0,-</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.5 | 1.5 | 1.1 | 15.1 |
| Brayden Burries | 98% | 21.8<br><sub>23,19,29,25,28</sub> | 9.1<br><sub>8,3,13,20,14</sub> | – · 11.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>5,4,8,7,3</sub> |  | 2.1<br><sub>1,3,4,1,3</sub> |  | 0.9<br><sub>1,1,2,3,2</sub> |  | 0.7 | 0.2 | 1.4 | 15.9 |
| Nate Ament | 96% | 18.4<br><sub>22,22,17,17,35</sub> | 7.1<br><sub>2,9,5,7,18</sub> | – · 8.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>4,3,2,4,9</sub> |  | 0.8<br><sub>1,1,1,1,0</sub> |  | 0.8<br><sub>0,2,1,0,2</sub> |  | 0.5 | 0.3 | 0.9 | 10.9 |
| Kel'el Ware | 98% | 17.2<br><sub>23,17,25,17,26</sub> | 7.5<br><sub>8,10,8,11,11</sub> |  | 5.3<br><sub>5,6,11,3,5</sub> |  | 0.9<br><sub>1,1,2,1,0</sub> |  | 0.7<br><sub>0,2,1,1,2</sub> |  | 0.5 | 0.9 | 1.2 | 13.8 |
| Kasparas Jakucionis | 88% | 17.2<br><sub>4,-,26,26,22</sub> | 8.0<br><sub>4,-,25,20,18</sub> | 8.5 · 7.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,-,5,3,3</sub> |  | 2.9<br><sub>0,-,5,5,2</sub> |  | 0.9<br><sub>0,-,4,3,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 0.1 | 1.4 | 13.2 |
| Pete Nance | 96% | 15.8<br><sub>4,-,-,-,28</sub> | 5.0<br><sub>3,-,-,-,7</sub> |  | 2.5<br><sub>1,-,-,-,3</sub> |  | 1.1<br><sub>1,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.3 | 0.5 | 8.6 |
| Cormac Ryan | 52% | 13.9<br><sub>-,-,-,-,-</sub> | 6.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 1.1 | 9.3 |
| Gary Trent Jr. | 80% | 11.6<br><sub>4,16,30,16,7</sub> | 5.0<br><sub>6,1,18,1,0</sub> |  | 0.9<br><sub>1,0,2,1,1</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.7<br><sub>2,0,4,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.5 |
| Jericho Sims | 84% | 11.1<br><sub>18,-,11,18,10</sub> | 2.7<br><sub>0,-,4,4,0</sub> |  | 2.7<br><sub>4,-,2,6,0</sub> |  | 0.9<br><sub>1,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.3 |
| Caris LeVert | 52% | 10.3<br><sub>-,-,-,8,11</sub> | 4.0<br><sub>-,-,-,8,3</sub> |  | 1.3<br><sub>-,-,-,3,3</sub> |  | 1.2<br><sub>-,-,-,2,1</sub> |  | 0.4<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.5 |
| AJ Green | 76% | 9.6<br><sub>8,8,6,14,-</sub> | 3.3<br><sub>3,0,0,11,-</sub> |  | 1.0<br><sub>1,0,0,0,-</sub> |  | 0.6<br><sub>1,2,0,1,-</sub> |  | 0.4<br><sub>1,0,0,3,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 100% | 37.4<br><sub>34,35,36,35,-</sub> | 26.2<br><sub>24,27,27,24,-</sub> | 24.5 · 24.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,2,4,1,-</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>4,8,6,9,-</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>3,1,5,4,-</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.6 | 2.4 | 36.6 |
| VJ Edgecombe | 100% | 36.5<br><sub>32,36,31,33,43</sub> | 15.1<br><sub>8,15,11,14,24</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>4,8,4,9,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>5,8,6,4,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>0,1,0,1,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.5 | 0.5 | 1.5 | 26.3 |
| LeBron James | 100% | 34.4<br><sub>29,-,33,-,31</sub> | 17.7<br><sub>11,-,15,-,22</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>8,-,7,-,3</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 7.3<br><sub>5,-,11,-,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>1,-,0,-,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 2.9 | 32.2 |
| Joel Embiid | 100% | 33.7<br><sub>31,28,-,32,36</sub> | 25.0<br><sub>16,20,-,37,26</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>6,4,-,5,6</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>1,3,-,1,7</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.0<br><sub>1,0,-,2,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 1.3 | 3.0 | 38.7 |
| Kentavious Caldwell-Pope | 100% | 30.5<br><sub>16,27,22,31,32</sub> | 7.8<br><sub>0,11,9,0,8</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>0,4,5,2,8</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>2,5,0,3,1</sub> |  | 1.3<br><sub>0,3,2,0,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.4 | 0.9 | 14.1 |
| Anfernee Simons | 98% | 29.2<br><sub>18,23,15,26,38</sub> | 13.6<br><sub>17,17,12,9,18</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>3,3,0,1,2</sub> |  | 2.2<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.8<br><sub>3,5,1,1,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.2 | 1.0 | 18.6 |
| Jabari Walker | 91% | 17.8<br><sub>15,16,25,16,13</sub> | 7.1<br><sub>2,9,11,12,6</sub> |  | 5.4<br><sub>4,8,7,5,5</sub> |  | 1.0<br><sub>0,1,1,1,2</sub> |  | 0.7<br><sub>0,1,3,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 13.5 |
| Dominick Barlow | 88% | 14.0 | 3.9 |  | 3.0 |  | 0.8 |  | 0.1 |  | 0.6 | 0.5 | 0.5 | 7.7 |
| Labaron Philon Jr. | 67% | 12.8<br><sub>6,2,6,-,17</sub> | 4.9<br><sub>2,0,3,-,10</sub> |  | 1.6<br><sub>1,0,1,-,1</sub> |  | 1.2<br><sub>3,0,0,-,2</sub> |  | 0.6<br><sub>0,0,1,-,2</sub> |  | 0.4 | 0.1 | 0.7 | 7.7 |
| Justin Edwards | 58% | 11.8<br><sub>6,1,-,-,13</sub> | 4.1<br><sub>0,0,-,-,2</sub> |  | 1.7<br><sub>0,1,-,-,1</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.5 |
| Tacko Fall | 67% | 8.5<br><sub>-,1,5,-,10</sub> | 6.6<br><sub>-,0,0,-,2</sub> |  | 2.4<br><sub>-,0,3,-,3</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.8 | 0.4 | 9.4 |
| Rayan Rupert | 36% | 8.3<br><sub>6,-,-,-,-</sub> | 2.5<br><sub>0,-,-,-,-</sub> |  | 1.7<br><sub>1,-,-,-,-</sub> |  | 0.5<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.8 |
| Caleb Love | 52% | 6.6<br><sub>-,1,-,-,6</sub> | 2.0<br><sub>-,0,-,-,3</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.1<br><sub>-,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.3 | 3.3 |

</details>


### POR @ NYK
Out: Jordan Clarkson (NYK), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.9–111.4 | POR 40% | 2.47 / 1.68 | NYK -3.5 | 219.5 | NYK -3.5 covers 50%; o215.5 58% |
| Expected (weighted by chance each plays) | 108.4–113.3 | POR 36% | 2.78 / 1.56 | NYK -5.5 | 221.5 | NYK -3.5 covers 55%; o215.5 63% |
| if OG Anunoby plays | 107.9–113.5 | POR 34% | 2.91 / 1.52 | NYK -5.5 | 221.5 | NYK -3.5 covers 57%; o215.5 62% |
| if Deni Avdija plays | 109.4–111.6 | POR 44% | 2.29 / 1.78 | NYK -2.5 | 220.5 | NYK -3.5 covers 47%; o215.5 61% |
| if Karl-Anthony Towns plays | 106.8–114.5 | POR 29% | 3.46 / 1.41 | NYK -7.5 | 221.5 | NYK -3.5 covers 62%; o215.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| OG Anunoby (NYK) | Doubtful | 20% | 36.7 | 19.8 | 6.2 | 2.2 | 2.2 | 1.7 | 1.1 | 2.0 | 28.3 | full tables below |
| Deni Avdija (POR) | Questionable | 55% | 33.5 | 22.0 | 6.2 | 5.5 | 1.8 | 0.8 | 0.5 | 3.4 | 33.7 | full tables below |
| Karl-Anthony Towns (NYK) | Questionable | 55% | 35.6 | 24.7 | 13.7 | 4.6 | 2.0 | 1.2 | 0.8 | 3.2 | 43.0 | full tables below |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Toumani Camara | 99% | 34.2<br><sub>38,36,26,33,37</sub> | 13.8<br><sub>14,14,3,10,18</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>5,2,0,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,1,0,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,0,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.6 | 1.5 | 20.2 |
| Damian Lillard | 99% | 33.6<br><sub>32,33,24,31,35</sub> | 21.8<br><sub>18,29,9,25,33</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,2,2,3,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>3,6,4,5,0</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>2,6,2,5,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.7 | 30.1 |
| Jrue Holiday | 99% | 31.9<br><sub>30,27,25,31,31</sub> | 16.4<br><sub>19,6,10,23,22</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,5,4,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>5,5,3,6,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>5,0,2,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 2.5 | 25.7 |
| Sidy Cissoko | 98% | 30.2<br><sub>29,26,28,32,31</sub> | 9.1<br><sub>19,3,5,6,13</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>2,4,4,5,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>0,1,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.2 | 15.2 |
| Scoot Henderson | 99% | 29.4<br><sub>19,23,23,21,35</sub> | 13.8<br><sub>5,11,10,9,27</sub> |  | 2.7<br><sub>2,0,1,1,7</sub> |  | 2.8<br><sub>2,1,0,1,3</sub> |  | 1.8<br><sub>1,2,0,0,5</sub> |  | 0.8 | 0.3 | 2.6 | 19.3 |
| Donovan Clingan | 99% | 28.3<br><sub>30,27,22,32,26</sub> | 11.9<br><sub>5,13,10,12,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>12,11,10,12,13</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,2,1,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.5 | 1.7 | 1.5 | 24.6 |
| Robert Williams III | 98% | 17.4<br><sub>17,17,15,16,-</sub> | 6.1<br><sub>10,2,2,6,-</sub> |  | 6.2<br><sub>7,7,5,8,-</sub> |  | 1.2<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.6 | 1.1 | 0.8 | 13.5 |
| Jayson Kent | 80% | 17.2<br><sub>-,11,11,27,17</sub> | 5.8<br><sub>-,3,8,8,2</sub> |  | 1.9<br><sub>-,1,0,3,1</sub> |  | 0.7<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,1,2,2,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.3 |
| Branden Carlson | 88% | 12.8<br><sub>10,8,14,14,10</sub> | 3.6<br><sub>0,5,5,6,0</sub> |  | 2.7<br><sub>2,3,6,1,1</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 6.8 |
| Yang Hansen | 58% | 11.4<br><sub>-,-,7,-,12</sub> | 3.9<br><sub>-,-,0,-,2</sub> |  | 2.6<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,3,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.8 | 7.2 |
| John Tonje | 52% | 11.4<br><sub>-,-,7,-,6</sub> | 4.0<br><sub>-,-,7,-,0</sub> |  | 2.7<br><sub>-,-,4,-,3</sub> |  | 0.9<br><sub>-,-,3,-,0</sub> |  | 0.5<br><sub>-,-,1,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 7.5 |
| Micah Potter | 52% | 9.3<br><sub>-,-,7,1,-</sub> | 3.8<br><sub>-,-,2,0,-</sub> |  | 2.4<br><sub>-,-,4,0,-</sub> |  | 0.5<br><sub>-,-,1,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 31.8<br><sub>27,33,28,31,21</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>3,1,1,5,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.4<br><sub>5,11,9,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 3.0 | 41.6 |
| Mikal Bridges | 99% | 33.1<br><sub>17,29,32,30,31</sub> | 14.1<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>1,3,7,5,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,3,3,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.6 | 1.5 | 21.2 |
| Josh Hart | 98% | 32.9<br><sub>26,23,26,31,28</sub> | 11.4<br><sub>6,0,0,5,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>4,5,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,4,2,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.3 | 2.0 | 23.1 |
| Landry Shamet | 99% | 31.5<br><sub>29,21,30,24,30</sub> | 13.2<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,3,2,1,1</sub> |  | 1.8<br><sub>4,1,0,1,2</sub> |  | 2.0<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.2 | 17.3 |
| Miles McBride | 99% | 22.6<br><sub>27,22,14,9,8</sub> | 9.4<br><sub>19,9,3,3,3</sub> |  | 1.8<br><sub>2,1,1,0,0</sub> |  | 1.5<br><sub>2,1,0,1,0</sub> |  | 1.5<br><sub>5,3,1,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.8 |
| Andre Drummond | 98% | 21.5<br><sub>14,14,7,11,15</sub> | 7.2<br><sub>0,0,2,2,4</sub> |  | 9.5<br><sub>4,6,3,8,4</sub> |  | 1.4<br><sub>3,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.2 | 18.1 |
| Tyler Kolek | 96% | 19.8<br><sub>13,19,16,13,12</sub> | 7.5<br><sub>4,5,0,4,6</sub> |  | 2.6<br><sub>1,6,0,1,3</sub> |  | 4.9<br><sub>4,2,7,3,5</sub> |  | 0.9<br><sub>0,1,0,0,1</sub> |  | 0.7 | 0.1 | 1.2 | 15.0 |
| Mohamed Diawara | 47% | 18.3<br><sub>11,-,-,-,-</sub> | 6.9<br><sub>2,-,-,-,-</sub> |  | 3.0<br><sub>0,-,-,-,-</sub> |  | 1.8<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.8 | 11.8 |
| Jose Alvarado | 71% | 17.8<br><sub>-,-,2,7,13</sub> | 7.0<br><sub>-,-,0,2,2</sub> |  | 2.3<br><sub>-,-,0,0,2</sub> |  | 2.7<br><sub>-,-,1,4,1</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 1.0 | 0.1 | 1.2 | 12.0 |
| Dalton Knecht | 64% | 15.5<br><sub>-,-,-,-,-</sub> | 6.2<br><sub>-,-,-,-,-</sub> |  | 2.9<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 9.9 |
| Pacome Dadiet | 38% | 14.2<br><sub>-,1,-,-,-</sub> | 5.5<br><sub>-,0,-,-,-</sub> |  | 2.7<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 9.0 |
| James Wiseman | 43% | 13.0<br><sub>-,-,3,-,-</sub> | 4.5<br><sub>-,-,0,-,-</sub> |  | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.6 | 0.8 | 9.2 |
| Jaden Akins | 38% | 11.1<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.4 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Karl-Anthony Towns plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 29.4<br><sub>27,33,28,31,21</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,1,1,5,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>5,11,9,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 2.8 | 39.1 |
| Karl-Anthony Towns (NYK) | 100% | 35.6<br><sub>34,34,43,36,33</sub> | 24.7<br><sub>21,23,28,16,22</sub> | 21.5 · – | 13.7<br><sub>11,15,17,16,12</sub> | 12.5 | 4.6<br><sub>8,5,3,8,4</sub> | 3.5 | 2.0<br><sub>2,3,3,1,2</sub> | 1.5 | 1.2 | 0.8 | 3.2 | 43.0 |
| Josh Hart (NYK) | 98% | 32.4<br><sub>26,23,26,31,28</sub> | 9.9<br><sub>6,0,0,5,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>4,5,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,4,2,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.3 | 1.7 | 20.9 |
| Mikal Bridges (NYK) | 99% | 32.0<br><sub>17,29,32,30,31</sub> | 12.0<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>1,3,7,5,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>2,3,3,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.6 | 1.3 | 18.5 |
| Landry Shamet (NYK) | 99% | 29.7<br><sub>29,21,30,24,30</sub> | 10.9<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,3,2,1,1</sub> |  | 1.6<br><sub>4,1,0,1,2</sub> |  | 1.8<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.1 | 14.7 |
| Miles McBride (NYK) | 99% | 18.7<br><sub>27,22,14,9,8</sub> | 6.5<br><sub>19,9,3,3,3</sub> |  | 1.4<br><sub>2,1,1,0,0</sub> |  | 1.2<br><sub>2,1,0,1,0</sub> |  | 1.1<br><sub>5,3,1,1,0</sub> |  | 0.7 | 0.2 | 0.5 | 9.2 |
| Tyler Kolek (NYK) | 96% | 16.2<br><sub>13,19,16,13,12</sub> | 5.4<br><sub>4,5,0,4,6</sub> |  | 2.1<br><sub>1,6,0,1,3</sub> |  | 4.0<br><sub>4,2,7,3,5</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 11.5 |
| Andre Drummond (NYK) | 98% | 14.9<br><sub>14,14,7,11,15</sub> | 4.8<br><sub>0,0,2,2,4</sub> |  | 6.4<br><sub>4,6,3,8,4</sub> |  | 1.0<br><sub>3,0,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.6 | 0.8 | 12.2 |
| Jose Alvarado (NYK) | 71% | 13.9<br><sub>-,-,2,7,13</sub> | 5.0<br><sub>-,-,0,2,2</sub> |  | 1.7<br><sub>-,-,0,0,2</sub> |  | 2.0<br><sub>-,-,1,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.7 | 0.1 | 0.8 | 8.7 |
| Mohamed Diawara (NYK) | 47% | 13.8<br><sub>11,-,-,-,-</sub> | 4.6<br><sub>2,-,-,-,-</sub> |  | 2.2<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.2 |
| Dalton Knecht (NYK) | 64% | 10.1<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 6.3 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Pacome Dadiet (NYK) | 38% | 8.5<br><sub>-,1,-,-,-</sub> | 3.2<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.3 |
| Jaden Akins (NYK) | 38% | 8.2<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| James Wiseman (NYK) | 43% | 7.6<br><sub>-,-,3,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,3,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.4 | 0.5 | 5.4 |
| Toumani Camara (POR) | 99% | 34.1<br><sub>38,36,26,33,37</sub> | 13.7<br><sub>14,14,3,10,18</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,2,0,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,1,0,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,0,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.6 | 1.5 | 20.0 |
| Damian Lillard (POR) | 99% | 33.5<br><sub>32,33,24,31,35</sub> | 21.6<br><sub>18,29,9,25,33</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,2,2,3,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>3,6,4,5,0</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.1<br><sub>2,6,2,5,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.7 | 29.9 |
| Jrue Holiday (POR) | 99% | 31.9<br><sub>30,27,25,31,31</sub> | 16.3<br><sub>19,6,10,23,22</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,5,4,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>5,5,3,6,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>5,0,2,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 2.5 | 25.6 |
| Sidy Cissoko (POR) | 98% | 30.2<br><sub>29,26,28,32,31</sub> | 9.1<br><sub>19,3,5,6,13</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>2,4,4,5,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>0,1,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.3 | 15.1 |
| Scoot Henderson (POR) | 99% | 29.4<br><sub>19,23,23,21,35</sub> | 13.8<br><sub>5,11,10,9,27</sub> |  | 2.7<br><sub>2,0,1,1,7</sub> |  | 2.8<br><sub>2,1,0,1,3</sub> |  | 1.8<br><sub>1,2,0,0,5</sub> |  | 0.8 | 0.3 | 2.6 | 19.3 |
| Donovan Clingan (POR) | 99% | 28.3<br><sub>30,27,22,32,26</sub> | 11.7<br><sub>5,13,10,12,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>12,11,10,12,13</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,2,1,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.6 | 1.7 | 1.5 | 24.5 |
| Robert Williams III (POR) | 98% | 17.3<br><sub>17,17,15,16,-</sub> | 6.0<br><sub>10,2,2,6,-</sub> |  | 6.2<br><sub>7,7,5,8,-</sub> |  | 1.2<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 1.1 | 0.8 | 13.4 |
| Jayson Kent (POR) | 80% | 17.2<br><sub>-,11,11,27,17</sub> | 5.8<br><sub>-,3,8,8,2</sub> |  | 1.8<br><sub>-,1,0,3,1</sub> |  | 0.7<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,1,2,2,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.3 |
| Branden Carlson (POR) | 88% | 12.6<br><sub>10,8,14,14,10</sub> | 3.6<br><sub>0,5,5,6,0</sub> |  | 2.7<br><sub>2,3,6,1,1</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 6.7 |
| Yang Hansen (POR) | 58% | 11.4<br><sub>-,-,7,-,12</sub> | 3.8<br><sub>-,-,0,-,2</sub> |  | 2.5<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,3,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.8 | 7.1 |
| John Tonje (POR) | 52% | 11.4<br><sub>-,-,7,-,6</sub> | 3.9<br><sub>-,-,7,-,0</sub> |  | 2.6<br><sub>-,-,4,-,3</sub> |  | 0.9<br><sub>-,-,3,-,0</sub> |  | 0.5<br><sub>-,-,1,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 7.4 |
| Micah Potter (POR) | 52% | 9.3<br><sub>-,-,7,1,-</sub> | 3.9<br><sub>-,-,2,0,-</sub> |  | 2.4<br><sub>-,-,4,0,-</sub> |  | 0.5<br><sub>-,-,1,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.8 |

</details>

<details><summary>if OG Anunoby plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 30.1<br><sub>27,33,28,31,21</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,1,1,5,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.7<br><sub>5,11,9,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 2.9 | 40.1 |
| OG Anunoby (NYK) | 100% | 36.7<br><sub>34,33,44,36,36</sub> | 19.8<br><sub>14,11,21,16,15</sub> |  | 6.2<br><sub>6,2,9,4,7</sub> |  | 2.2<br><sub>2,1,1,0,2</sub> |  | 2.2<br><sub>2,2,2,1,1</sub> |  | 1.7 | 1.1 | 2.0 | 28.3 |
| Josh Hart (NYK) | 98% | 32.3<br><sub>26,23,26,31,28</sub> | 10.2<br><sub>6,0,0,5,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.5<br><sub>4,5,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,4,2,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.3 | 1.8 | 21.6 |
| Mikal Bridges (NYK) | 99% | 31.8<br><sub>17,29,32,30,31</sub> | 12.4<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>1,3,7,5,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,3,3,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.6 | 1.3 | 19.2 |
| Landry Shamet (NYK) | 99% | 29.6<br><sub>29,21,30,24,30</sub> | 11.1<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,3,2,1,1</sub> |  | 1.7<br><sub>4,1,0,1,2</sub> |  | 1.8<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.0 | 15.0 |
| Miles McBride (NYK) | 99% | 18.8<br><sub>27,22,14,9,8</sub> | 7.0<br><sub>19,9,3,3,3</sub> |  | 1.5<br><sub>2,1,1,0,0</sub> |  | 1.3<br><sub>2,1,0,1,0</sub> |  | 1.1<br><sub>5,3,1,1,0</sub> |  | 0.8 | 0.2 | 0.5 | 9.8 |
| Andre Drummond (NYK) | 98% | 16.9<br><sub>14,14,7,11,15</sub> | 5.6<br><sub>0,0,2,2,4</sub> |  | 7.5<br><sub>4,6,3,8,4</sub> |  | 1.2<br><sub>3,0,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.6 | 0.9 | 14.3 |
| Tyler Kolek (NYK) | 96% | 16.1<br><sub>13,19,16,13,12</sub> | 5.5<br><sub>4,5,0,4,6</sub> |  | 2.1<br><sub>1,6,0,1,3</sub> |  | 4.1<br><sub>4,2,7,3,5</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 11.7 |
| Jose Alvarado (NYK) | 71% | 13.7<br><sub>-,-,2,7,13</sub> | 5.0<br><sub>-,-,0,2,2</sub> |  | 1.7<br><sub>-,-,0,0,2</sub> |  | 2.1<br><sub>-,-,1,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.7 | 0.1 | 0.9 | 8.8 |
| Mohamed Diawara (NYK) | 47% | 12.5<br><sub>11,-,-,-,-</sub> | 4.2<br><sub>2,-,-,-,-</sub> |  | 2.1<br><sub>0,-,-,-,-</sub> |  | 1.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 7.6 |
| Dalton Knecht (NYK) | 64% | 8.9<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 5.7 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| James Wiseman (NYK) | 43% | 8.3<br><sub>-,-,3,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 2.7<br><sub>-,-,3,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.4 | 0.6 | 6.0 |
| Jaden Akins (NYK) | 38% | 8.0<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| Pacome Dadiet (NYK) | 38% | 7.6<br><sub>-,1,-,-,-</sub> | 3.0<br><sub>-,0,-,-,-</sub> |  | 1.4<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |
| Toumani Camara (POR) | 99% | 34.1<br><sub>38,36,26,33,37</sub> | 13.8<br><sub>14,14,3,10,18</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>5,2,0,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,1,0,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,0,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.6 | 1.5 | 20.1 |
| Damian Lillard (POR) | 99% | 33.5<br><sub>32,33,24,31,35</sub> | 21.7<br><sub>18,29,9,25,33</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,2,2,3,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>3,6,4,5,0</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.1<br><sub>2,6,2,5,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.7 | 30.0 |
| Jrue Holiday (POR) | 99% | 32.0<br><sub>30,27,25,31,31</sub> | 16.5<br><sub>19,6,10,23,22</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,5,4,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>5,5,3,6,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>5,0,2,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 2.5 | 25.7 |
| Sidy Cissoko (POR) | 98% | 30.2<br><sub>29,26,28,32,31</sub> | 9.1<br><sub>19,3,5,6,13</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>2,4,4,5,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>0,1,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.3 | 15.1 |
| Scoot Henderson (POR) | 99% | 29.4<br><sub>19,23,23,21,35</sub> | 13.8<br><sub>5,11,10,9,27</sub> |  | 2.7<br><sub>2,0,1,1,7</sub> |  | 2.8<br><sub>2,1,0,1,3</sub> |  | 1.8<br><sub>1,2,0,0,5</sub> |  | 0.8 | 0.3 | 2.6 | 19.3 |
| Donovan Clingan (POR) | 99% | 28.3<br><sub>30,27,22,32,26</sub> | 11.9<br><sub>5,13,10,12,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>12,11,10,12,13</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,2,1,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.6 | 1.7 | 1.5 | 24.6 |
| Robert Williams III (POR) | 98% | 17.4<br><sub>17,17,15,16,-</sub> | 6.1<br><sub>10,2,2,6,-</sub> |  | 6.1<br><sub>7,7,5,8,-</sub> |  | 1.2<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.6 | 1.1 | 0.9 | 13.4 |
| Jayson Kent (POR) | 80% | 17.1<br><sub>-,11,11,27,17</sub> | 5.8<br><sub>-,3,8,8,2</sub> |  | 1.9<br><sub>-,1,0,3,1</sub> |  | 0.6<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,1,2,2,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.3 |
| Branden Carlson (POR) | 88% | 12.7<br><sub>10,8,14,14,10</sub> | 3.6<br><sub>0,5,5,6,0</sub> |  | 2.7<br><sub>2,3,6,1,1</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 6.8 |
| Yang Hansen (POR) | 58% | 11.5<br><sub>-,-,7,-,12</sub> | 3.9<br><sub>-,-,0,-,2</sub> |  | 2.5<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,3,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.8 | 7.2 |
| John Tonje (POR) | 52% | 11.5<br><sub>-,-,7,-,6</sub> | 4.0<br><sub>-,-,7,-,0</sub> |  | 2.6<br><sub>-,-,4,-,3</sub> |  | 0.9<br><sub>-,-,3,-,0</sub> |  | 0.5<br><sub>-,-,1,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 7.5 |
| Micah Potter (POR) | 52% | 9.4<br><sub>-,-,7,1,-</sub> | 3.9<br><sub>-,-,2,0,-</sub> |  | 2.4<br><sub>-,-,4,0,-</sub> |  | 0.5<br><sub>-,-,1,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.8 |

</details>

<details><summary>if Deni Avdija plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 31.8<br><sub>27,33,28,31,21</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,1,1,5,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.4<br><sub>5,11,9,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 3.0 | 41.6 |
| Mikal Bridges (NYK) | 99% | 33.1<br><sub>17,29,32,30,31</sub> | 14.1<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>1,3,7,5,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,3,3,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.6 | 1.5 | 21.2 |
| Josh Hart (NYK) | 98% | 32.9<br><sub>26,23,26,31,28</sub> | 11.5<br><sub>6,0,0,5,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>4,5,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,4,2,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.3 | 2.0 | 23.2 |
| Landry Shamet (NYK) | 99% | 31.4<br><sub>29,21,30,24,30</sub> | 13.2<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,3,2,1,1</sub> |  | 1.8<br><sub>4,1,0,1,2</sub> |  | 2.0<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.2 | 17.3 |
| Miles McBride (NYK) | 99% | 22.7<br><sub>27,22,14,9,8</sub> | 9.5<br><sub>19,9,3,3,3</sub> |  | 1.8<br><sub>2,1,1,0,0</sub> |  | 1.5<br><sub>2,1,0,1,0</sub> |  | 1.5<br><sub>5,3,1,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.8 |
| Andre Drummond (NYK) | 98% | 21.5<br><sub>14,14,7,11,15</sub> | 7.3<br><sub>0,0,2,2,4</sub> |  | 9.4<br><sub>4,6,3,8,4</sub> |  | 1.4<br><sub>3,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.2 | 18.1 |
| Tyler Kolek (NYK) | 96% | 19.8<br><sub>13,19,16,13,12</sub> | 7.5<br><sub>4,5,0,4,6</sub> |  | 2.6<br><sub>1,6,0,1,3</sub> |  | 4.8<br><sub>4,2,7,3,5</sub> |  | 0.9<br><sub>0,1,0,0,1</sub> |  | 0.7 | 0.1 | 1.2 | 14.9 |
| Mohamed Diawara (NYK) | 47% | 18.3<br><sub>11,-,-,-,-</sub> | 6.9<br><sub>2,-,-,-,-</sub> |  | 3.1<br><sub>0,-,-,-,-</sub> |  | 1.8<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.8 | 11.9 |
| Jose Alvarado (NYK) | 71% | 17.7<br><sub>-,-,2,7,13</sub> | 7.0<br><sub>-,-,0,2,2</sub> |  | 2.2<br><sub>-,-,0,0,2</sub> |  | 2.7<br><sub>-,-,1,4,1</sub> |  | 0.8<br><sub>-,-,0,0,0</sub> |  | 1.0 | 0.1 | 1.2 | 11.9 |
| Dalton Knecht (NYK) | 64% | 15.6<br><sub>-,-,-,-,-</sub> | 6.3<br><sub>-,-,-,-,-</sub> |  | 2.9<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 10.0 |
| Pacome Dadiet (NYK) | 38% | 14.1<br><sub>-,1,-,-,-</sub> | 5.5<br><sub>-,0,-,-,-</sub> |  | 2.7<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.9 |
| James Wiseman (NYK) | 43% | 13.0<br><sub>-,-,3,-,-</sub> | 4.5<br><sub>-,-,0,-,-</sub> |  | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.6 | 0.9 | 9.3 |
| Jaden Akins (NYK) | 38% | 11.2<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.4 |
| Tyler Nickel (NYK) | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Deni Avdija (POR) | 100% | 33.5<br><sub>35,35,30,-,-</sub> | 22.0<br><sub>28,34,27,-,-</sub> | 23.5 · – | 6.2<br><sub>3,6,8,-,-</sub> | 6.5 | 5.5<br><sub>6,4,4,-,-</sub> | 5.5 | 1.8<br><sub>4,3,3,-,-</sub> | 1.5 | 0.8 | 0.5 | 3.4 | 33.7 |
| Toumani Camara (POR) | 99% | 31.7<br><sub>38,36,26,33,37</sub> | 11.6<br><sub>14,14,3,10,18</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>5,2,0,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,1,0,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,2,0,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 1.2 | 17.4 |
| Damian Lillard (POR) | 99% | 31.3<br><sub>32,33,24,31,35</sub> | 18.6<br><sub>18,29,9,25,33</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,2,2,3,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,6,4,5,0</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>2,6,2,5,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.2 | 26.0 |
| Jrue Holiday (POR) | 99% | 28.3<br><sub>30,27,25,31,31</sub> | 13.4<br><sub>19,6,10,23,22</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,5,4,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>5,5,3,6,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>5,0,2,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 2.0 | 21.2 |
| Donovan Clingan (POR) | 99% | 26.2<br><sub>30,27,22,32,26</sub> | 10.3<br><sub>5,13,10,12,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 9.6<br><sub>12,11,10,12,13</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>2,2,1,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.5 | 1.6 | 1.2 | 21.7 |
| Sidy Cissoko (POR) | 98% | 25.4<br><sub>29,26,28,32,31</sub> | 6.9<br><sub>19,3,5,6,13</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>2,4,4,5,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,1,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.4 | 1.0 | 11.9 |
| Scoot Henderson (POR) | 99% | 25.0<br><sub>19,23,23,21,35</sub> | 11.4<br><sub>5,11,10,9,27</sub> |  | 2.3<br><sub>2,0,1,1,7</sub> |  | 2.1<br><sub>2,1,0,1,3</sub> |  | 1.4<br><sub>1,2,0,0,5</sub> |  | 0.7 | 0.2 | 2.1 | 15.8 |
| Robert Williams III (POR) | 98% | 14.6<br><sub>17,17,15,16,-</sub> | 4.8<br><sub>10,2,2,6,-</sub> |  | 5.1<br><sub>7,7,5,8,-</sub> |  | 0.9<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.9 | 0.7 | 10.8 |
| Jayson Kent (POR) | 80% | 14.4<br><sub>-,11,11,27,17</sub> | 4.7<br><sub>-,3,8,8,2</sub> |  | 1.5<br><sub>-,1,0,3,1</sub> |  | 0.5<br><sub>-,0,0,0,2</sub> |  | 0.5<br><sub>-,1,2,2,0</sub> |  | 0.6 | 0.2 | 0.6 | 6.7 |
| Branden Carlson (POR) | 88% | 9.9<br><sub>10,8,14,14,10</sub> | 2.7<br><sub>0,5,5,6,0</sub> |  | 2.2<br><sub>2,3,6,1,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.2<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.4 | 0.5 | 5.2 |
| Yang Hansen (POR) | 58% | 8.0<br><sub>-,-,7,-,12</sub> | 2.7<br><sub>-,-,0,-,2</sub> |  | 1.9<br><sub>-,-,1,-,1</sub> |  | 0.5<br><sub>-,-,3,-,1</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.1 |
| John Tonje (POR) | 52% | 7.1<br><sub>-,-,7,-,6</sub> | 2.6<br><sub>-,-,7,-,0</sub> |  | 1.6<br><sub>-,-,4,-,3</sub> |  | 0.7<br><sub>-,-,3,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.9 |
| Micah Potter (POR) | 52% | 7.0<br><sub>-,-,7,1,-</sub> | 2.9<br><sub>-,-,2,0,-</sub> |  | 1.8<br><sub>-,-,4,0,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |

</details>


### LAC @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Bradley Beal (LAC), Brandon Ingram (LAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.7–117.0 | LAC 49% | 2.04 / 1.97 | DAL +0.5 | 233.5 | DAL -5.5 covers 36%; o230.5 56% |
| Expected (weighted by chance each plays) | 116.5–117.4 | LAC 47% | 2.11 / 1.90 | DAL -1.5 | 234.5 | DAL -5.5 covers 37%; o230.5 58% |
| if Walter Clayton Jr. plays | 116.3–117.3 | LAC 47% | 2.12 / 1.89 | DAL -1.5 | 233.5 | DAL -5.5 covers 37%; o230.5 56% |
| if P.J. Washington plays | 116.3–117.3 | LAC 47% | 2.13 / 1.89 | DAL -1.5 | 233.5 | DAL -5.5 covers 38%; o230.5 56% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walter Clayton Jr. (DAL) | Questionable | 55% | 21.1 | 7.8 | 3.1 | 3.8 | 1.1 | 0.7 | 0.2 | 1.7 | 14.7 | full tables below |
| Jett Howard (DAL) | Questionable | 55% | 8.0 | 2.9 | 0.9 | 0.6 | 0.3 | 0.2 | 0.1 | 0.3 | 4.4 | small |
| P.J. Washington (DAL) | Questionable | 55% | 31.5 | 14.1 | 6.7 | 1.7 | 1.8 | 0.9 | 0.9 | 1.6 | 22.5 | full tables below |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.8<br><sub>13,24,27,20,23</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>5,4,6,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>6,7,7,7,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>1,3,3,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.2 | 3.4 | 32.8 |
| Rui Hachimura | 98% | 28.5<br><sub>23,32,22,27,32</sub> | 14.1<br><sub>13,7,4,20,17</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,11,2,5,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,1,0,4,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.4 | 1.2 | 20.2 |
| Derrick Jones Jr. | 98% | 27.1<br><sub>24,29,26,28,27</sub> | 10.4<br><sub>11,14,13,5,8</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,5,4,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1<br><sub>2,4,3,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.9 | 0.9 | 15.6 |
| Brook Lopez | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>4,7,5,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,4,8,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6<br><sub>1,3,1,4,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 1.3 | 1.1 | 20.3 |
| Max Strus | 98% | 24.3<br><sub>22,23,25,21,32</sub> | 9.6<br><sub>12,3,14,3,18</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,3,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,3,4,1,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>2,0,4,1,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.1 | 16.5 |
| Kris Dunn | 98% | 23.0<br><sub>19,20,18,26,20</sub> | 6.5<br><sub>3,2,7,2,6</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,3,3,5,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>3,6,1,5,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.6 | 0.3 | 1.1 | 13.2 |
| Keaton Wagler | 98% | 20.5<br><sub>23,18,28,18,17</sub> | 10.8<br><sub>11,14,12,15,7</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>0,2,4,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,1,5,0,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.2 | 1.8 | 16.4 |
| Kobe Sanders | 98% | 18.8<br><sub>26,15,20,18,14</sub> | 7.3<br><sub>9,5,2,5,0</sub> |  | 2.2<br><sub>3,0,6,1,1</sub> |  | 2.0<br><sub>7,1,4,3,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.5 |
| Gradey Dick | 98% | 15.0<br><sub>19,19,19,17,13</sub> | 6.5<br><sub>10,13,12,0,2</sub> |  | 2.2<br><sub>3,3,2,0,2</sub> |  | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.6<br><sub>1,2,2,0,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.5 |
| Isaiah Jackson | 98% | 14.6<br><sub>16,17,15,19,9</sub> | 6.8<br><sub>4,5,13,8,6</sub> |  | 4.5<br><sub>4,3,2,5,4</sub> |  | 1.3<br><sub>0,3,2,0,2</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 12.5 |
| Yanic Konan Niederhauser | 52% | 9.8<br><sub>-,-,-,-,11</sub> | 4.1<br><sub>-,-,-,-,2</sub> |  | 2.4<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 7.0 |
| Baba Miller | 88% | 9.0<br><sub>16,-,5,4,1</sub> | 4.5<br><sub>13,-,2,3,0</sub> |  | 1.4<br><sub>4,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.9 |
| Cam Christie | 58% | 6.7<br><sub>-,-,-,4,1</sub> | 2.8<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley | 52% | 6.3<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.6 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 36.6<br><sub>39,27,38,27,34</sub> | 25.7<br><sub>43,12,18,17,33</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>10,7,8,3,5</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.6<br><sub>6,3,5,4,9</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.8 | 3.1 | 39.6 |
| Kyrie Irving | 98% | 36.0<br><sub>38,27,37,-,29</sub> | 25.1<br><sub>35,10,34,-,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>0,3,6,-,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 5.2<br><sub>4,4,5,-,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>7,2,7,-,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.5 | 2.4 | 34.8 |
| Naji Marshall | 96% | 30.6<br><sub>25,23,30,23,27</sub> | 15.3<br><sub>6,13,12,13,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>5,1,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>2,4,5,2,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>0,1,0,3,2</sub> |  | 1.3 | 0.1 | 2.0 | 23.8 |
| Caleb Martin | 98% | 25.5<br><sub>19,21,33,34,20</sub> | 7.1<br><sub>0,7,15,12,8</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>3,2,8,5,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>5,5,3,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>0,1,1,4,2</sub> |  | 1.0 | 0.4 | 1.0 | 13.3 |
| Daniel Gafford | 99% | 25.3<br><sub>20,16,17,19,24</sub> | 11.0<br><sub>8,3,10,3,6</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>2,3,3,4,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>3,1,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.6 | 1.2 | 19.9 |
| Zaccharie Risacher | 98% | 24.3<br><sub>15,25,14,27,18</sub> | 8.7<br><sub>4,22,5,18,3</sub> |  | 4.5<br><sub>2,6,2,5,3</sub> |  | 1.3<br><sub>0,3,0,0,0</sub> |  | 1.1<br><sub>0,4,1,1,1</sub> |  | 0.9 | 0.8 | 1.1 | 14.5 |
| Morez Johnson Jr. | 98% | 19.5<br><sub>-,13,15,26,15</sub> | 7.2<br><sub>-,0,4,2,3</sub> |  | 3.8<br><sub>-,2,2,6,1</sub> |  | 1.7<br><sub>-,0,0,4,1</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.1 | 12.6 |
| Max Christie | 98% | 18.9<br><sub>5,7,-,-,8</sub> | 7.0<br><sub>0,3,-,-,5</sub> |  | 2.3<br><sub>2,2,-,-,1</sub> |  | 1.3<br><sub>0,0,-,-,2</sub> |  | 1.1<br><sub>0,1,-,-,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.6 |
| Santi Aldama | 98% | 16.6<br><sub>19,10,16,-,6</sub> | 7.8<br><sub>10,3,7,-,0</sub> |  | 3.9<br><sub>4,1,2,-,0</sub> |  | 1.3<br><sub>1,1,1,-,0</sub> |  | 0.9<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.4 | 0.9 | 13.0 |
| Marcus Sasser | 67% | 15.1<br><sub>-,9,-,18,4</sub> | 5.2<br><sub>-,3,-,5,0</sub> |  | 1.4<br><sub>-,1,-,1,2</sub> |  | 1.8<br><sub>-,0,-,2,1</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 8.4 |
| Moussa Cisse | 67% | 8.9<br><sub>-,8,-,4,4</sub> | 3.1<br><sub>-,0,-,1,0</sub> |  | 3.3<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.6 | 0.4 | 6.6 |

</details>

<details><summary>if P.J. Washington plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 35.1<br><sub>39,27,38,27,34</sub> | 24.9<br><sub>43,12,18,17,33</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>10,7,8,3,5</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.4<br><sub>6,3,5,4,9</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.8 | 3.0 | 38.3 |
| Kyrie Irving (DAL) | 98% | 34.6<br><sub>38,27,37,-,29</sub> | 23.3<br><sub>35,10,34,-,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>0,3,6,-,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 4.8<br><sub>4,4,5,-,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>7,2,7,-,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.5 | 2.4 | 32.4 |
| P.J. Washington (DAL) | 100% | 31.5<br><sub>35,16,26,25,25</sub> | 14.1<br><sub>13,10,10,8,21</sub> | 12.5 · – | 6.7<br><sub>9,3,4,5,5</sub> | 6.5 | 1.7<br><sub>1,0,1,4,2</sub> | 1.5 | 1.8<br><sub>2,1,2,0,5</sub> | 1.5 | 0.9 | 0.9 | 1.6 | 22.5 |
| Naji Marshall (DAL) | 96% | 26.7<br><sub>25,23,30,23,27</sub> | 13.3<br><sub>6,13,12,13,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>5,1,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>2,4,5,2,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>0,1,0,3,2</sub> |  | 1.1 | 0.1 | 1.8 | 20.8 |
| Daniel Gafford (DAL) | 99% | 21.6<br><sub>20,16,17,19,24</sub> | 9.6<br><sub>8,3,10,3,6</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>2,3,3,4,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,1,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 1.4 | 1.1 | 17.2 |
| Caleb Martin (DAL) | 98% | 21.3<br><sub>19,21,33,34,20</sub> | 6.0<br><sub>0,7,15,12,8</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,2,8,5,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>5,5,3,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>0,1,1,4,2</sub> |  | 0.8 | 0.3 | 0.8 | 11.3 |
| Zaccharie Risacher (DAL) | 98% | 19.8<br><sub>15,25,14,27,18</sub> | 7.1<br><sub>4,22,5,18,3</sub> |  | 3.7<br><sub>2,6,2,5,3</sub> |  | 1.1<br><sub>0,3,0,0,0</sub> |  | 0.8<br><sub>0,4,1,1,1</sub> |  | 0.7 | 0.7 | 0.9 | 11.9 |
| Morez Johnson Jr. (DAL) | 98% | 15.2<br><sub>-,13,15,26,15</sub> | 5.5<br><sub>-,0,4,2,3</sub> |  | 3.0<br><sub>-,2,2,6,1</sub> |  | 1.4<br><sub>-,0,0,4,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.9 |
| Max Christie (DAL) | 98% | 14.2<br><sub>5,7,-,-,8</sub> | 5.2<br><sub>0,3,-,-,5</sub> |  | 1.7<br><sub>2,2,-,-,1</sub> |  | 1.0<br><sub>0,0,-,-,2</sub> |  | 0.7<br><sub>0,1,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 7.9 |
| Santi Aldama (DAL) | 98% | 12.2<br><sub>19,10,16,-,6</sub> | 5.9<br><sub>10,3,7,-,0</sub> |  | 2.9<br><sub>4,1,2,-,0</sub> |  | 1.0<br><sub>1,1,1,-,0</sub> |  | 0.6<br><sub>1,1,2,-,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.8 |
| Marcus Sasser (DAL) | 67% | 11.6<br><sub>-,9,-,18,4</sub> | 4.0<br><sub>-,3,-,5,0</sub> |  | 1.0<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.5 |
| Moussa Cisse (DAL) | 67% | 6.9<br><sub>-,8,-,4,4</sub> | 2.5<br><sub>-,0,-,1,0</sub> |  | 2.5<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.2 |
| Darius Garland (LAC) | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.7<br><sub>13,24,27,20,23</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>5,4,6,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>6,7,7,7,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>1,3,3,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.2 | 3.4 | 32.7 |
| Rui Hachimura (LAC) | 98% | 28.5<br><sub>23,32,22,27,32</sub> | 14.0<br><sub>13,7,4,20,17</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,11,2,5,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,1,0,4,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.4 | 1.2 | 20.1 |
| Derrick Jones Jr. (LAC) | 98% | 27.1<br><sub>24,29,26,28,27</sub> | 10.3<br><sub>11,14,13,5,8</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,5,4,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1<br><sub>2,4,3,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.9 | 0.9 | 15.6 |
| Brook Lopez (LAC) | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>4,7,5,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,4,8,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6<br><sub>1,3,1,4,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 1.2 | 1.2 | 20.3 |
| Max Strus (LAC) | 98% | 24.2<br><sub>22,23,25,21,32</sub> | 9.5<br><sub>12,3,14,3,18</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,3,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,3,4,1,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>2,0,4,1,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.0 | 16.4 |
| Kris Dunn (LAC) | 98% | 22.8<br><sub>19,20,18,26,20</sub> | 6.5<br><sub>3,2,7,2,6</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,3,3,5,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>3,6,1,5,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.2 |
| Keaton Wagler (LAC) | 98% | 20.4<br><sub>23,18,28,18,17</sub> | 10.8<br><sub>11,14,12,15,7</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>0,2,4,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,1,5,0,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.2 | 1.8 | 16.4 |
| Kobe Sanders (LAC) | 98% | 18.8<br><sub>26,15,20,18,14</sub> | 7.3<br><sub>9,5,2,5,0</sub> |  | 2.2<br><sub>3,0,6,1,1</sub> |  | 2.0<br><sub>7,1,4,3,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.6 |
| Gradey Dick (LAC) | 98% | 15.0<br><sub>19,19,19,17,13</sub> | 6.5<br><sub>10,13,12,0,2</sub> |  | 2.2<br><sub>3,3,2,0,2</sub> |  | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.6<br><sub>1,2,2,0,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.5 |
| Isaiah Jackson (LAC) | 98% | 14.6<br><sub>16,17,15,19,9</sub> | 6.7<br><sub>4,5,13,8,6</sub> |  | 4.5<br><sub>4,3,2,5,4</sub> |  | 1.3<br><sub>0,3,2,0,2</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 12.4 |
| Yanic Konan Niederhauser (LAC) | 52% | 9.7<br><sub>-,-,-,-,11</sub> | 4.0<br><sub>-,-,-,-,2</sub> |  | 2.4<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 7.0 |
| Baba Miller (LAC) | 88% | 9.1<br><sub>16,-,5,4,1</sub> | 4.5<br><sub>13,-,2,3,0</sub> |  | 1.4<br><sub>4,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Cam Christie (LAC) | 58% | 6.8<br><sub>-,-,-,4,1</sub> | 2.9<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley (LAC) | 52% | 6.3<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.5 |

</details>

<details><summary>if Walter Clayton Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 35.9<br><sub>39,27,38,27,34</sub> | 25.7<br><sub>43,12,18,17,33</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 7.2<br><sub>10,7,8,3,5</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.3<br><sub>6,3,5,4,9</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.8 | 3.0 | 39.1 |
| Kyrie Irving (DAL) | 98% | 35.0<br><sub>38,27,37,-,29</sub> | 23.7<br><sub>35,10,34,-,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>0,3,6,-,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 4.7<br><sub>4,4,5,-,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>7,2,7,-,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.5 | 2.3 | 32.9 |
| Naji Marshall (DAL) | 96% | 28.2<br><sub>25,23,30,23,27</sub> | 13.7<br><sub>6,13,12,13,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>5,1,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>2,4,5,2,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>0,1,0,3,2</sub> |  | 1.1 | 0.1 | 1.9 | 21.4 |
| Daniel Gafford (DAL) | 99% | 23.3<br><sub>20,16,17,19,24</sub> | 10.4<br><sub>8,3,10,3,6</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>2,3,3,4,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>3,1,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 1.5 | 1.1 | 18.4 |
| Caleb Martin (DAL) | 98% | 23.2<br><sub>19,21,33,34,20</sub> | 6.5<br><sub>0,7,15,12,8</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,2,8,5,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>5,5,3,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>0,1,1,4,2</sub> |  | 0.9 | 0.3 | 0.9 | 12.1 |
| Zaccharie Risacher (DAL) | 98% | 22.0<br><sub>15,25,14,27,18</sub> | 8.1<br><sub>4,22,5,18,3</sub> |  | 4.1<br><sub>2,6,2,5,3</sub> |  | 1.1<br><sub>0,3,0,0,0</sub> |  | 0.9<br><sub>0,4,1,1,1</sub> |  | 0.8 | 0.7 | 1.0 | 13.3 |
| Walter Clayton Jr. (DAL) | 100% | 21.1<br><sub>25,22,13,23,27</sub> | 7.8<br><sub>6,5,2,13,8</sub> |  | 3.1<br><sub>6,1,2,4,2</sub> |  | 3.8<br><sub>4,4,2,3,7</sub> |  | 1.1<br><sub>1,0,0,3,2</sub> |  | 0.7 | 0.2 | 1.7 | 14.7 |
| Morez Johnson Jr. (DAL) | 98% | 17.3<br><sub>-,13,15,26,15</sub> | 6.3<br><sub>-,0,4,2,3</sub> |  | 3.4<br><sub>-,2,2,6,1</sub> |  | 1.5<br><sub>-,0,0,4,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 11.2 |
| Max Christie (DAL) | 98% | 15.6<br><sub>5,7,-,-,8</sub> | 5.7<br><sub>0,3,-,-,5</sub> |  | 1.9<br><sub>2,2,-,-,1</sub> |  | 1.0<br><sub>0,0,-,-,2</sub> |  | 0.8<br><sub>0,1,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 8.6 |
| Santi Aldama (DAL) | 98% | 14.5<br><sub>19,10,16,-,6</sub> | 7.0<br><sub>10,3,7,-,0</sub> |  | 3.4<br><sub>4,1,2,-,0</sub> |  | 1.1<br><sub>1,1,1,-,0</sub> |  | 0.7<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.3 | 0.7 | 11.5 |
| Marcus Sasser (DAL) | 67% | 12.1<br><sub>-,9,-,18,4</sub> | 4.2<br><sub>-,3,-,5,0</sub> |  | 1.1<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.7 |
| Moussa Cisse (DAL) | 67% | 7.4<br><sub>-,8,-,4,4</sub> | 2.6<br><sub>-,0,-,1,0</sub> |  | 2.7<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.5 |
| Darius Garland (LAC) | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.7<br><sub>13,24,27,20,23</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>5,4,6,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>6,7,7,7,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>1,3,3,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.2 | 3.4 | 32.7 |
| Rui Hachimura (LAC) | 98% | 28.5<br><sub>23,32,22,27,32</sub> | 14.1<br><sub>13,7,4,20,17</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,11,2,5,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,1,0,4,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.4 | 1.2 | 20.2 |
| Derrick Jones Jr. (LAC) | 98% | 27.0<br><sub>24,29,26,28,27</sub> | 10.3<br><sub>11,14,13,5,8</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,4,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1<br><sub>2,4,3,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.9 | 0.9 | 15.5 |
| Brook Lopez (LAC) | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>4,7,5,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,4,8,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6<br><sub>1,3,1,4,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 1.3 | 1.1 | 20.3 |
| Max Strus (LAC) | 98% | 24.2<br><sub>22,23,25,21,32</sub> | 9.5<br><sub>12,3,14,3,18</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,3,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,3,4,1,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>2,0,4,1,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.0 | 16.4 |
| Kris Dunn (LAC) | 98% | 22.9<br><sub>19,20,18,26,20</sub> | 6.5<br><sub>3,2,7,2,6</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,3,3,5,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>3,6,1,5,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.2 |
| Keaton Wagler (LAC) | 98% | 20.5<br><sub>23,18,28,18,17</sub> | 10.7<br><sub>11,14,12,15,7</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>0,2,4,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,1,5,0,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.2 | 1.8 | 16.4 |
| Kobe Sanders (LAC) | 98% | 18.8<br><sub>26,15,20,18,14</sub> | 7.3<br><sub>9,5,2,5,0</sub> |  | 2.2<br><sub>3,0,6,1,1</sub> |  | 2.0<br><sub>7,1,4,3,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.5 |
| Gradey Dick (LAC) | 98% | 15.1<br><sub>19,19,19,17,13</sub> | 6.5<br><sub>10,13,12,0,2</sub> |  | 2.2<br><sub>3,3,2,0,2</sub> |  | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.6<br><sub>1,2,2,0,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.5 |
| Isaiah Jackson (LAC) | 98% | 14.5<br><sub>16,17,15,19,9</sub> | 6.7<br><sub>4,5,13,8,6</sub> |  | 4.5<br><sub>4,3,2,5,4</sub> |  | 1.3<br><sub>0,3,2,0,2</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 12.5 |
| Yanic Konan Niederhauser (LAC) | 52% | 9.7<br><sub>-,-,-,-,11</sub> | 4.1<br><sub>-,-,-,-,2</sub> |  | 2.4<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 7.0 |
| Baba Miller (LAC) | 88% | 9.1<br><sub>16,-,5,4,1</sub> | 4.5<br><sub>13,-,2,3,0</sub> |  | 1.4<br><sub>4,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Cam Christie (LAC) | 58% | 6.7<br><sub>-,-,-,4,1</sub> | 2.8<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley (LAC) | 52% | 6.2<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.5 |

</details>


### MEM @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM), Javon Small (MEM)

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 32.4<br><sub>30,33,27,33,25</sub> | 16.5<br><sub>14,23,18,20,19</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>7,12,8,3,4</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>6,4,6,5,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>0,4,2,4,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.6 | 2.1 | 28.2 |
| Ty Jerome | 92% | 30.3<br><sub>29,-,-,-,-</sub> | 23.1<br><sub>17,-,-,-,-</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,-,-,-,-</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.1<br><sub>9,-,-,-,-</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>2,-,-,-,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.3 | 2.8 | 33.0 |
| Jaylen Wells | 99% | 30.2<br><sub>27,25,27,26,24</sub> | 11.8<br><sub>11,5,8,5,22</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,2,4,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 1.1 | 16.9 |
| Cam Spencer | 98% | 29.1<br><sub>24,34,32,29,27</sub> | 13.3<br><sub>14,17,12,26,9</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,1,6,1,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 7.2<br><sub>5,8,9,7,11</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,3,1,5,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.2 | 1.7 | 24.0 |
| Taylor Hendricks | 88% | 24.0<br><sub>19,29,19,21,20</sub> | 10.6<br><sub>10,22,9,18,11</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>12,5,3,6,1</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,4,0,2,1</sub> |  | 1.2<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.6 | 1.1 | 16.9 |
| Zach Edey | 88% | 23.9<br><sub>-,-,21,21,-</sub> | 10.2<br><sub>-,-,23,11,-</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 8.8<br><sub>-,-,10,2,-</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>-,-,1,1,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.5 | 1.6 | 1.7 | 20.3 |
| Olivier-Maxence Prosper | 86% | 21.6<br><sub>2,20,16,16,24</sub> | 10.7<br><sub>6,11,12,5,16</sub> |  | 4.0<br><sub>1,4,0,2,5</sub> |  | 1.1<br><sub>0,0,1,0,1</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.8 | 0.3 | 1.0 | 15.9 |
| Isaiah Stewart | 98% | 20.4<br><sub>20,15,-,-,18</sub> | 9.3<br><sub>12,11,-,-,8</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,3,-,-,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>0,3,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.4 | 1.3 | 1.1 | 14.7 |
| Jahmai Mashack | 71% | 18.2<br><sub>-,2,2,13,26</sub> | 4.9<br><sub>-,0,0,3,0</sub> |  | 2.4<br><sub>-,0,0,2,3</sub> |  | 2.4<br><sub>-,0,1,2,4</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.9 | 0.4 | 1.0 | 9.7 |
| Kris Murray | 88% | 16.1<br><sub>1,19,6,6,4</sub> | 3.1<br><sub>0,3,0,5,0</sub> |  | 2.4<br><sub>1,2,1,0,1</sub> |  | 1.0<br><sub>0,3,0,0,0</sub> |  | 0.2<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 6.5 |
| Quinten Post | 96% | 14.2<br><sub>-,-,9,6,10</sub> | 5.2<br><sub>-,-,5,3,5</sub> |  | 2.8<br><sub>-,-,3,2,1</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,1,0</sub> |  | 0.4 | 0.4 | 0.7 | 8.5 |
| Karim Lopez | 58% | 11.5<br><sub>-,2,1,-,4</sub> | 3.4<br><sub>-,0,0,-,3</sub> |  | 2.1<br><sub>-,2,0,-,0</sub> |  | 0.6<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,1</sub> |  | 0.6 | 0.6 | 0.5 | 6.1 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 36.0<br><sub>25,37,31,37,39</sub> | 18.1<br><sub>16,18,13,22,17</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>9,5,6,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>3,6,3,4,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>0,2,0,2,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 1.2 | 2.0 | 27.4 |
| Ayo Dosunmu | 99% | 33.7<br><sub>27,33,30,39,32</sub> | 19.1<br><sub>18,24,8,30,6</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>2,5,5,4,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.0<br><sub>1,0,2,5,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>2,0,2,7,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.5 | 2.0 | 27.8 |
| Jonathan Kuminga | 84% | 31.9<br><sub>24,35,29,-,35</sub> | 14.8<br><sub>14,11,13,-,23</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>8,3,9,-,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>5,3,1,-,3</sub> | 2.5<br><sub>o 46% · u 53%</sub> | 1.3<br><sub>1,0,1,-,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.8 | 1.7 | 23.5 |
| LaMelo Ball | 99% | 31.3<br><sub>25,30,24,31,35</sub> | 21.2<br><sub>22,19,6,18,15</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>3,8,5,9,8</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 6.6<br><sub>9,6,0,2,8</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.6<br><sub>6,4,2,3,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7 | 0.3 | 3.0 | 32.8 |
| Rudy Gobert | 99% | 31.1<br><sub>23,27,32,22,35</sub> | 10.0<br><sub>9,1,18,0,9</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 11.6<br><sub>6,10,15,4,7</sub> | 9.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,4,3,2,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.8 | 1.5 | 23.4 |
| Terrence Shannon Jr. | 98% | 24.2<br><sub>21,22,35,24,21</sub> | 13.6<br><sub>6,14,34,12,10</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,6,3,1,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.6<br><sub>4,0,6,4,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>0,0,3,1,0</sub> |  | 0.7 | 0.2 | 1.3 | 19.3 |
| Trey Lyles | 98% | 20.4<br><sub>15,19,19,31,16</sub> | 6.5<br><sub>2,5,9,8,8</sub> |  | 4.6<br><sub>0,1,3,7,6</sub> |  | 1.2<br><sub>0,2,1,4,1</sub> |  | 0.9<br><sub>0,0,2,2,2</sub> |  | 0.6 | 0.4 | 0.7 | 12.3 |
| Joan Beringer | 98% | 16.4<br><sub>22,13,16,26,13</sub> | 6.2<br><sub>13,2,0,3,5</sub> |  | 5.9<br><sub>9,5,4,13,3</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.5 | 0.6 | 12.6 |
| Bones Hyland | 98% | 15.6<br><sub>23,21,13,17,15</sub> | 9.2<br><sub>24,12,5,13,6</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,1,1,2,1</sub> |  | 2.5<br><sub>8,2,5,1,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>5,3,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 1.1 | 13.4 |
| Cody Williams | 58% | 7.8<br><sub>7,-,4,13,-</sub> | 0.2<br><sub>0,-,0,0,-</sub> |  | 1.2<br><sub>1,-,1,1,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 1.8 |
| Zyon Pullin | 38% | 6.5<br><sub>-,-,4,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Isaiah Evans | 48% | 5.8<br><sub>8,-,4,-,-</sub> | 4.3<br><sub>2,-,0,-,-</sub> |  | 1.2<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.9 |
| Johni Broome | 3% | 5.8 | 2.3 |  | 1.3 |  | 0.4 |  | 0.1 |  | 0.3 | 0.2 | 0.3 | 4.0 |

</details>


### NOP @ SAS
Out: Dylan Harper (SAS), Tobias Harris (SAS), Bennedict Mathurin (NOP), Bryce McGowens (NOP), Dejounte Murray (NOP), Trendon Watford (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 32.0<br><sub>35,41,33,42,37</sub> | 15.1<br><sub>30,16,23,10,21</sub> |  | 4.6<br><sub>10,6,6,8,6</sub> |  | 2.7<br><sub>0,4,3,6,3</sub> |  | 2.0<br><sub>6,2,5,2,4</sub> |  | 0.8 | 0.2 | 1.0 | 22.4 |
| Trey Murphy III | 98% | 32.0<br><sub>-,-,-,-,29</sub> | 15.0<br><sub>-,-,-,-,17</sub> |  | 4.4<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,1</sub> |  | 2.3<br><sub>-,-,-,-,3</sub> |  | 1.1 | 0.4 | 1.4 | 22.6 |
| Zion Williamson | 98% | 31.6<br><sub>33,31,25,32,37</sub> | 18.8<br><sub>22,24,16,24,22</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,6,6,7,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>4,2,2,1,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.3<br><sub>0,2,0,0,0</sub> |  | 1.1 | 0.5 | 2.0 | 27.3 |
| Jeremiah Fears | 99% | 30.7<br><sub>34,33,29,31,38</sub> | 15.8<br><sub>18,13,19,16,22</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,4,10,5,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>7,7,10,4,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>0,1,1,2,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 2.7 | 25.4 |
| Herbert Jones | 98% | 26.2<br><sub>32,27,24,32,33</sub> | 8.1<br><sub>8,10,8,9,14</sub> |  | 2.7<br><sub>2,2,2,1,2</sub> |  | 2.2<br><sub>3,1,3,3,3</sub> |  | 1.1<br><sub>0,2,2,3,4</sub> |  | 1.1 | 0.4 | 1.2 | 13.1 |
| Derik Queen | 99% | 21.2<br><sub>23,25,21,19,18</sub> | 10.3<br><sub>10,10,17,9,11</sub> |  | 5.8<br><sub>6,5,10,5,7</sub> |  | 2.3<br><sub>2,4,0,0,3</sub> |  | 0.6<br><sub>0,2,4,0,0</sub> |  | 0.8 | 0.7 | 1.9 | 18.4 |
| Yves Missi | 98% | 20.5<br><sub>-,22,23,17,23</sub> | 5.9<br><sub>-,3,6,4,4</sub> |  | 6.1<br><sub>-,8,14,5,7</sub> |  | 1.4<br><sub>-,1,1,2,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.9 | 13.3 |
| Jordan Poole | 88% | 20.4<br><sub>21,24,31,30,13</sub> | 9.5<br><sub>13,14,11,22,6</sub> |  | 1.9<br><sub>2,2,2,1,0</sub> |  | 2.7<br><sub>5,5,5,5,1</sub> |  | 1.4<br><sub>1,1,1,3,2</sub> |  | 0.6 | 0.3 | 1.3 | 14.1 |
| Karlo Matkovic | 98% | 15.5<br><sub>19,14,20,10,8</sub> | 5.3<br><sub>1,5,3,0,0</sub> |  | 3.2<br><sub>3,3,2,2,2</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.5 | 0.6 | 0.7 | 9.4 |
| Jaron Pierre Jr. | 96% | 10.9<br><sub>4,23,19,17,4</sub> | 4.7<br><sub>0,13,10,7,3</sub> |  | 1.5<br><sub>0,2,4,1,2</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>0,2,2,1,1</sub> |  | 0.4 | 0.1 | 0.6 | 6.8 |
| DeAndre Jordan | 48% | 10.1<br><sub>17,-,-,10,-</sub> | 3.0<br><sub>6,-,-,8,-</sub> |  | 3.5<br><sub>8,-,-,2,-</sub> |  | 0.7<br><sub>1,-,-,1,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 7.1 |
| AJ Johnson | 52% | 6.9<br><sub>4,-,6,-,-</sub> | 2.5<br><sub>1,-,0,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.1 |
| Malik Dia | 52% | 6.6<br><sub>4,-,5,-,-</sub> | 2.8<br><sub>2,-,2,-,-</sub> |  | 0.8<br><sub>0,-,1,-,-</sub> |  | 0.9<br><sub>1,-,1,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.5 |
| Julian Reese | 52% | 6.6<br><sub>4,-,5,-,-</sub> | 2.4<br><sub>0,-,0,-,-</sub> |  | 1.3<br><sub>2,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.0 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 98% | 33.1<br><sub>-,23,32,36,32</sub> | 14.3<br><sub>-,7,6,12,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>-,2,6,5,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>-,2,1,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>-,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.5 | 1.1 | 22.0 |
| Victor Wembanyama | 99% | 32.5<br><sub>32,21,35,34,33</sub> | 30.8<br><sub>32,12,26,25,32</sub> | 29.5 · –<br><sub>o 49% · u 51%</sub> | 13.4<br><sub>9,12,10,18,11</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>1,6,6,4,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,0,4,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 4.3 | 2.4 | 48.1 |
| De'Aaron Fox | 99% | 32.1<br><sub>31,17,-,34,32</sub> | 16.4<br><sub>17,7,-,6,10</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,5,-,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>9,1,-,2,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,-,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.4 | 2.2 | 26.8 |
| Stephon Castle | 99% | 31.9<br><sub>29,25,35,31,33</sub> | 18.8<br><sub>11,32,20,10,21</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>1,5,4,2,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 7.2<br><sub>3,6,9,7,12</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,5,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 2.9 | 31.2 |
| Julian Champagnie | 99% | 29.0<br><sub>35,23,24,30,29</sub> | 11.6<br><sub>12,7,4,14,20</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>0,8,5,6,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>2,3,1,0,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,1,1,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.6 | 0.8 | 18.6 |
| Keldon Johnson | 99% | 25.6<br><sub>28,25,29,15,27</sub> | 11.3<br><sub>10,18,11,4,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>6,4,10,2,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>4,4,2,1,3</sub> |  | 0.7<br><sub>0,2,1,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 19.3 |
| Luke Kornet | 99% | 16.3<br><sub>14,16,13,14,15</sub> | 4.4<br><sub>7,6,2,2,4</sub> |  | 4.8<br><sub>5,7,2,1,0</sub> |  | 1.4<br><sub>1,2,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.5 | 10.6 |
| Harrison Barnes | 91% | 16.3<br><sub>13,21,14,10,16</sub> | 5.9<br><sub>3,11,0,0,9</sub> |  | 1.9<br><sub>1,1,0,3,2</sub> |  | 1.0<br><sub>0,1,2,4,1</sub> |  | 0.8<br><sub>1,3,0,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 8.9 |
| Jordan McLaughlin | 71% | 14.3<br><sub>2,14,19,-,11</sub> | 4.6<br><sub>4,4,10,-,0</sub> |  | 1.9<br><sub>0,6,1,-,1</sub> |  | 2.5<br><sub>0,2,2,-,5</sub> |  | 0.5<br><sub>0,0,2,-,0</sub> |  | 0.9 | 0.1 | 0.7 | 9.0 |
| Carter Bryant | 93% | 13.1<br><sub>15,19,5,2,13</sub> | 4.9<br><sub>10,8,0,0,3</sub> |  | 2.2<br><sub>1,3,1,0,1</sub> |  | 0.9<br><sub>2,2,0,0,0</sub> |  | 0.7<br><sub>2,2,0,0,1</sub> |  | 0.3 | 0.3 | 0.5 | 8.0 |
| Tarris Reed Jr. | 52% | 8.7<br><sub>2,11,-,-,-</sub> | 3.2<br><sub>0,2,-,-,-</sub> |  | 3.4<br><sub>0,4,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.5 | 7.1 |
| David Jones Garcia | 52% | 6.9<br><sub>2,-,-,-,-</sub> | 2.8<br><sub>0,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.1 |

</details>


### BOS @ SAC
Out: Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.8–103.6 | BOS 80% | 1.24 / 5.09 | SAC +12.5 | 219.5 | SAC +13.5 covers 53%; o217.5 54% |
| Expected (weighted by chance each plays) | 117.0–104.7 | BOS 79% | 1.26 / 4.87 | SAC +12.5 | 221.5 | SAC +13.5 covers 53%; o217.5 58% |
| if Derrick White plays | 117.1–103.9 | BOS 82% | 1.22 / 5.64 | SAC +13.5 | 221.5 | SAC +13.5 covers 51%; o217.5 57% |
| if Jayson Tatum plays | 117.3–104.0 | BOS 82% | 1.21 / 5.70 | SAC +13.5 | 221.5 | SAC +13.5 covers 50%; o217.5 58% |
| if Precious Achiuwa plays | 115.6–104.5 | BOS 78% | 1.28 / 4.54 | SAC +11.5 | 220.5 | SAC +13.5 covers 56%; o217.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White (BOS) | Questionable | 55% | 31.9 | 16.4 | 3.6 | 5.2 | 2.3 | 1.1 | 0.8 | 1.6 | 25.3 | full tables below |
| Jayson Tatum (BOS) | Questionable | 55% | 34.9 | 27.6 | 8.0 | 6.8 | 3.2 | 1.2 | 0.5 | 2.9 | 42.4 | full tables below |
| Precious Achiuwa (SAC) | Day-To-Day | 70% | 20.1 | 8.1 | 5.3 | 1.1 | 0.3 | 0.6 | 0.6 | 1.0 | 14.5 | full tables below |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George | 98% | 31.6<br><sub>30,-,25,36,23</sub> | 22.2<br><sub>36,-,7,22,10</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>5,-,7,8,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>1,-,6,3,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8 | 0.4 | 2.4 | 31.9 |
| Payton Pritchard | 99% | 30.4<br><sub>30,31,19,32,30</sub> | 18.4<br><sub>18,14,10,21,15</sub> |  | 3.4<br><sub>6,1,1,4,1</sub> |  | 5.5<br><sub>5,1,6,5,2</sub> |  | 2.7<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.5 | 27.4 |
| Neemias Queta | 98% | 26.1<br><sub>22,31,15,-,27</sub> | 12.4<br><sub>4,11,8,-,17</sub> |  | 9.0<br><sub>6,13,6,-,10</sub> |  | 2.4<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.1 | 1.4 | 23.7 |
| Sam Hauser | 99% | 25.5<br><sub>18,24,11,25,17</sub> | 11.1<br><sub>12,8,8,12,9</sub> |  | 3.6<br><sub>5,9,1,1,2</sub> |  | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.2<br><sub>4,2,2,4,3</sub> |  | 0.7 | 0.2 | 0.5 | 16.3 |
| Baylor Scheierman | 99% | 23.0<br><sub>18,29,18,11,13</sub> | 7.6<br><sub>5,9,12,0,0</sub> |  | 4.1<br><sub>3,7,5,1,1</sub> |  | 2.3<br><sub>2,3,3,1,1</sub> |  | 1.3<br><sub>1,3,2,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 14.0 |
| Mitchell Robinson | 98% | 19.8<br><sub>17,11,15,18,16</sub> | 6.6<br><sub>2,2,0,4,6</sub> |  | 7.4<br><sub>6,2,7,5,4</sub> |  | 1.0<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.9 | 0.9 | 15.1 |
| Jordan Walsh | 98% | 19.6<br><sub>19,18,21,17,4</sub> | 6.6<br><sub>8,6,11,6,0</sub> |  | 3.6<br><sub>2,3,1,2,0</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 0.8<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.3 | 0.6 | 11.2 |
| Hugo Gonzalez | 98% | 18.8<br><sub>19,8,18,4,16</sub> | 6.3<br><sub>10,0,9,0,2</sub> |  | 3.8<br><sub>2,1,5,2,6</sub> |  | 1.1<br><sub>2,0,2,0,0</sub> |  | 0.7<br><sub>2,0,2,0,0</sub> |  | 0.8 | 0.3 | 0.7 | 11.1 |
| Devin Carter | 91% | 18.2<br><sub>-,-,12,-,-</sub> | 8.8<br><sub>-,-,0,-,-</sub> |  | 3.4<br><sub>-,-,2,-,-</sub> |  | 2.8<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.0 | 0.2 | 1.3 | 14.9 |
| Chris Cenac Jr. | 63% | 16.8<br><sub>-,-,7,12,17</sub> | 6.9<br><sub>-,-,6,4,6</sub> |  | 4.0<br><sub>-,-,3,2,6</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,0,0,1</sub> |  | 0.7 | 0.3 | 0.8 | 11.7 |
| Luka Garza | 98% | 15.4<br><sub>9,11,14,18,5</sub> | 7.7<br><sub>2,5,2,3,0</sub> |  | 3.6<br><sub>0,1,3,0,1</sub> |  | 1.9<br><sub>2,0,5,4,1</sub> |  | 0.8<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 13.2 |
| Ron Harper Jr. | 52% | 12.7<br><sub>4,-,12,-,-</sub> | 5.4<br><sub>0,-,10,-,-</sub> |  | 1.8<br><sub>1,-,1,-,-</sub> |  | 0.8<br><sub>0,-,0,-,-</sub> |  | 0.8<br><sub>0,-,2,-,-</sub> |  | 0.5 | 0.2 | 0.4 | 8.1 |
| Mike Conley | 35% | 12.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 6.7 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 36.8<br><sub>40,35,33,35,36</sub> | 22.9<br><sub>29,17,26,36,18</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.7<br><sub>6,6,6,6,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 3.9 | 34.1 |
| De'Andre Hunter | 88% | 33.5<br><sub>34,42,-,35,37</sub> | 14.1<br><sub>15,24,-,7,30</sub> |  | 4.8<br><sub>4,5,-,1,6</sub> |  | 1.9<br><sub>2,2,-,4,2</sub> |  | 2.1<br><sub>3,2,-,1,5</sub> |  | 0.6 | 0.2 | 1.6 | 20.8 |
| Zach LaVine | 88% | 33.2<br><sub>33,36,-,32,39</sub> | 17.6<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.9<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.0 | 23.8 |
| Domantas Sabonis | 98% | 32.0<br><sub>24,35,29,24,38</sub> | 13.5<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 12.0<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>5,5,3,8,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.3 | 2.2 | 30.6 |
| Keegan Murray | 98% | 31.3<br><sub>24,40,21,31,40</sub> | 12.2<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.6<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.8 | 1.1 | 18.8 |
| Leaky Black | 88% | 20.1<br><sub>18,12,29,17,19</sub> | 4.9<br><sub>0,0,12,3,0</sub> |  | 3.3<br><sub>3,0,9,0,3</sub> |  | 1.3<br><sub>2,0,2,2,1</sub> |  | 0.7<br><sub>0,0,4,1,0</sub> |  | 0.8 | 0.5 | 0.6 | 9.5 |
| Malik Monk | 98% | 16.6<br><sub>3,18,29,20,12</sub> | 8.6<br><sub>1,7,14,8,2</sub> |  | 1.5<br><sub>0,4,1,1,0</sub> |  | 3.0<br><sub>0,3,10,2,3</sub> |  | 1.1<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.3 | 1.2 | 13.1 |
| Dylan Cardwell | 98% | 14.7<br><sub>29,13,19,12,10</sub> | 4.2<br><sub>1,6,10,6,0</sub> |  | 4.9<br><sub>11,3,6,4,4</sub> |  | 1.1<br><sub>1,3,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.7 | 10.2 |
| Emanuel Sharp | 98% | 14.2<br><sub>19,7,21,14,10</sub> | 4.8<br><sub>2,4,9,6,3</sub> |  | 1.1<br><sub>2,0,0,2,0</sub> |  | 0.7<br><sub>0,0,2,1,1</sub> |  | 0.6<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.5 |
| Alex Karaban | 52% | 9.4<br><sub>-,-,29,4,-</sub> | 1.8<br><sub>-,-,0,0,-</sub> |  | 1.4<br><sub>-,-,5,1,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.6 |
| Daeqwon Plowden | 67% | 8.9<br><sub>2,2,24,4,-</sub> | 3.2<br><sub>0,0,13,3,-</sub> |  | 1.1<br><sub>0,0,2,0,-</sub> |  | 0.4<br><sub>0,0,1,0,-</sub> |  | 0.3<br><sub>0,0,3,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Sean Pedulla | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Jonathan Mogbo | 52% | 8.0<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Mason Plumlee | 52% | 6.6<br><sub>-,-,5,4,-</sub> | 1.7<br><sub>-,-,2,0,-</sub> |  | 2.0<br><sub>-,-,0,2,-</sub> |  | 0.5<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.3 |

</details>

<details><summary>if Jayson Tatum plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 100% | 34.9<br><sub>32,38,30,36,37</sub> | 27.6<br><sub>21,24,32,24,24</sub> | 26.5 · – | 8.0<br><sub>6,7,6,12,8</sub> | 7.5 | 6.8<br><sub>4,8,6,4,3</sub> | 6.5 | 3.2<br><sub>3,2,5,3,3</sub> | 2.5 | 1.2 | 0.5 | 2.9 | 42.4 |
| Paul George (BOS) | 98% | 30.5<br><sub>30,-,25,36,23</sub> | 18.7<br><sub>36,-,7,22,10</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>5,-,7,8,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>1,-,6,3,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.4 | 2.0 | 27.2 |
| Payton Pritchard (BOS) | 99% | 29.0<br><sub>30,31,19,32,30</sub> | 15.2<br><sub>18,14,10,21,15</sub> |  | 3.2<br><sub>6,1,1,4,1</sub> |  | 4.5<br><sub>5,1,6,5,2</sub> |  | 2.4<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.1 | 22.9 |
| Neemias Queta (BOS) | 98% | 25.6<br><sub>22,31,15,-,27</sub> | 11.2<br><sub>4,11,8,-,17</sub> |  | 8.7<br><sub>6,13,6,-,10</sub> |  | 2.0<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.1 | 1.2 | 21.9 |
| Sam Hauser (BOS) | 99% | 20.9<br><sub>18,24,11,25,17</sub> | 8.1<br><sub>12,8,8,12,9</sub> |  | 2.9<br><sub>5,9,1,1,2</sub> |  | 1.3<br><sub>2,0,0,2,2</sub> |  | 1.5<br><sub>4,2,2,4,3</sub> |  | 0.5 | 0.2 | 0.4 | 12.3 |
| Baylor Scheierman (BOS) | 99% | 18.9<br><sub>18,29,18,11,13</sub> | 5.8<br><sub>5,9,12,0,0</sub> |  | 3.2<br><sub>3,7,5,1,1</sub> |  | 1.7<br><sub>2,3,3,1,1</sub> |  | 0.9<br><sub>1,3,2,0,0</sub> |  | 0.9 | 0.1 | 0.6 | 10.7 |
| Mitchell Robinson (BOS) | 98% | 16.5<br><sub>17,11,15,18,16</sub> | 5.2<br><sub>2,2,0,4,6</sub> |  | 6.1<br><sub>6,2,7,5,4</sub> |  | 0.8<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 0.7 | 12.0 |
| Jordan Walsh (BOS) | 98% | 15.3<br><sub>19,18,21,17,4</sub> | 4.6<br><sub>8,6,11,6,0</sub> |  | 2.6<br><sub>2,3,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,2,2,0</sub> |  | 0.6 | 0.2 | 0.4 | 8.0 |
| Hugo Gonzalez (BOS) | 98% | 15.2<br><sub>19,8,18,4,16</sub> | 4.5<br><sub>10,0,9,0,2</sub> |  | 3.0<br><sub>2,1,5,2,6</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.5<br><sub>2,0,2,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 8.3 |
| Devin Carter (BOS) | 91% | 15.0<br><sub>-,-,12,-,-</sub> | 6.3<br><sub>-,-,0,-,-</sub> |  | 2.6<br><sub>-,-,2,-,-</sub> |  | 2.1<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.8 | 0.2 | 1.1 | 11.0 |
| Luka Garza (BOS) | 98% | 12.9<br><sub>9,11,14,18,5</sub> | 6.0<br><sub>2,5,2,3,0</sub> |  | 2.9<br><sub>0,1,3,0,1</sub> |  | 1.4<br><sub>2,0,5,4,1</sub> |  | 0.6<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.3 | 0.6 | 10.3 |
| Chris Cenac Jr. (BOS) | 63% | 11.6<br><sub>-,-,7,12,17</sub> | 4.8<br><sub>-,-,6,4,6</sub> |  | 3.0<br><sub>-,-,3,2,6</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |
| Mike Conley (BOS) | 35% | 9.5<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.8 |
| Ron Harper Jr. (BOS) | 52% | 8.7<br><sub>4,-,12,-,-</sub> | 3.9<br><sub>0,-,10,-,-</sub> |  | 1.2<br><sub>1,-,1,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>0,-,2,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.7 |
| Darius Acuff Jr. (SAC) | 98% | 36.7<br><sub>40,35,33,35,36</sub> | 22.9<br><sub>29,17,26,36,18</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.7<br><sub>6,6,6,6,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 3.8 | 34.0 |
| De'Andre Hunter (SAC) | 88% | 33.5<br><sub>34,42,-,35,37</sub> | 14.2<br><sub>15,24,-,7,30</sub> |  | 4.8<br><sub>4,5,-,1,6</sub> |  | 1.9<br><sub>2,2,-,4,2</sub> |  | 2.0<br><sub>3,2,-,1,5</sub> |  | 0.6 | 0.2 | 1.6 | 20.9 |
| Zach LaVine (SAC) | 88% | 33.2<br><sub>33,36,-,32,39</sub> | 17.5<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.9<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.0 | 23.8 |
| Domantas Sabonis (SAC) | 98% | 32.0<br><sub>24,35,29,24,38</sub> | 13.4<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 12.0<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>5,5,3,8,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.3 | 2.2 | 30.6 |
| Keegan Murray (SAC) | 98% | 31.3<br><sub>24,40,21,31,40</sub> | 12.2<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.6<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.8 | 1.1 | 18.8 |
| Leaky Black (SAC) | 88% | 20.0<br><sub>18,12,29,17,19</sub> | 4.9<br><sub>0,0,12,3,0</sub> |  | 3.3<br><sub>3,0,9,0,3</sub> |  | 1.3<br><sub>2,0,2,2,1</sub> |  | 0.7<br><sub>0,0,4,1,0</sub> |  | 0.8 | 0.5 | 0.6 | 9.5 |
| Malik Monk (SAC) | 98% | 16.6<br><sub>3,18,29,20,12</sub> | 8.5<br><sub>1,7,14,8,2</sub> |  | 1.5<br><sub>0,4,1,1,0</sub> |  | 3.0<br><sub>0,3,10,2,3</sub> |  | 1.1<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.3 | 1.2 | 13.1 |
| Dylan Cardwell (SAC) | 98% | 14.7<br><sub>29,13,19,12,10</sub> | 4.2<br><sub>1,6,10,6,0</sub> |  | 4.9<br><sub>11,3,6,4,4</sub> |  | 1.1<br><sub>1,3,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.7 | 10.2 |
| Emanuel Sharp (SAC) | 98% | 14.2<br><sub>19,7,21,14,10</sub> | 4.8<br><sub>2,4,9,6,3</sub> |  | 1.1<br><sub>2,0,0,2,0</sub> |  | 0.7<br><sub>0,0,2,1,1</sub> |  | 0.6<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.5 |
| Alex Karaban (SAC) | 52% | 9.4<br><sub>-,-,29,4,-</sub> | 1.8<br><sub>-,-,0,0,-</sub> |  | 1.4<br><sub>-,-,5,1,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.6 |
| Daeqwon Plowden (SAC) | 67% | 8.9<br><sub>2,2,24,4,-</sub> | 3.1<br><sub>0,0,13,3,-</sub> |  | 1.0<br><sub>0,0,2,0,-</sub> |  | 0.4<br><sub>0,0,1,0,-</sub> |  | 0.3<br><sub>0,0,3,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Sean Pedulla (SAC) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jonathan Mogbo (SAC) | 52% | 8.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.4 |
| Mason Plumlee (SAC) | 52% | 6.5<br><sub>-,-,5,4,-</sub> | 1.7<br><sub>-,-,2,0,-</sub> |  | 2.0<br><sub>-,-,0,2,-</sub> |  | 0.5<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.2 |

</details>

<details><summary>if Derrick White plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White (BOS) | 100% | 31.9<br><sub>22,38,23,32,35</sub> | 16.4<br><sub>5,19,16,9,12</sub> | 14.5 · – | 3.6<br><sub>1,1,4,3,3</sub> | 3.5 | 5.2<br><sub>3,7,2,2,8</sub> | 4.5 | 2.3<br><sub>1,3,4,1,0</sub> | 2.5 | 1.1 | 0.8 | 1.6 | 25.3 |
| Paul George (BOS) | 98% | 30.8<br><sub>30,-,25,36,23</sub> | 21.0<br><sub>36,-,7,22,10</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>5,-,7,8,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,-,6,3,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8 | 0.3 | 2.2 | 29.9 |
| Payton Pritchard (BOS) | 99% | 28.8<br><sub>30,31,19,32,30</sub> | 16.9<br><sub>18,14,10,21,15</sub> |  | 3.3<br><sub>6,1,1,4,1</sub> |  | 4.7<br><sub>5,1,6,5,2</sub> |  | 2.5<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.3 | 24.9 |
| Neemias Queta (BOS) | 98% | 25.5<br><sub>22,31,15,-,27</sub> | 12.3<br><sub>4,11,8,-,17</sub> |  | 8.6<br><sub>6,13,6,-,10</sub> |  | 2.1<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.7 | 1.1 | 1.3 | 23.0 |
| Sam Hauser (BOS) | 99% | 22.9<br><sub>18,24,11,25,17</sub> | 9.6<br><sub>12,8,8,12,9</sub> |  | 3.3<br><sub>5,9,1,1,2</sub> |  | 1.4<br><sub>2,0,0,2,2</sub> |  | 1.8<br><sub>4,2,2,4,3</sub> |  | 0.6 | 0.2 | 0.5 | 14.3 |
| Baylor Scheierman (BOS) | 99% | 18.0<br><sub>18,29,18,11,13</sub> | 6.1<br><sub>5,9,12,0,0</sub> |  | 3.2<br><sub>3,7,5,1,1</sub> |  | 1.6<br><sub>2,3,3,1,1</sub> |  | 0.9<br><sub>1,3,2,0,0</sub> |  | 0.9 | 0.1 | 0.6 | 10.9 |
| Mitchell Robinson (BOS) | 98% | 16.9<br><sub>17,11,15,18,16</sub> | 5.5<br><sub>2,2,0,4,6</sub> |  | 6.2<br><sub>6,2,7,5,4</sub> |  | 0.8<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 0.8 | 12.5 |
| Devin Carter (BOS) | 91% | 15.0<br><sub>-,-,12,-,-</sub> | 7.1<br><sub>-,-,0,-,-</sub> |  | 2.7<br><sub>-,-,2,-,-</sub> |  | 2.1<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.8 | 0.2 | 1.2 | 11.9 |
| Jordan Walsh (BOS) | 98% | 14.7<br><sub>19,18,21,17,4</sub> | 4.5<br><sub>8,6,11,6,0</sub> |  | 2.7<br><sub>2,3,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,2,2,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.0 |
| Chris Cenac Jr. (BOS) | 63% | 14.3<br><sub>-,-,7,12,17</sub> | 5.9<br><sub>-,-,6,4,6</sub> |  | 3.6<br><sub>-,-,3,2,6</sub> |  | 0.7<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.2 | 0.8 | 10.2 |
| Hugo Gonzalez (BOS) | 98% | 14.0<br><sub>19,8,18,4,16</sub> | 4.4<br><sub>10,0,9,0,2</sub> |  | 2.8<br><sub>2,1,5,2,6</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.4<br><sub>2,0,2,0,0</sub> |  | 0.6 | 0.3 | 0.5 | 8.0 |
| Luka Garza (BOS) | 98% | 13.4<br><sub>9,11,14,18,5</sub> | 6.8<br><sub>2,5,2,3,0</sub> |  | 3.1<br><sub>0,1,3,0,1</sub> |  | 1.5<br><sub>2,0,5,4,1</sub> |  | 0.7<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 11.4 |
| Mike Conley (BOS) | 35% | 9.0<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |
| Ron Harper Jr. (BOS) | 52% | 8.3<br><sub>4,-,12,-,-</sub> | 3.8<br><sub>0,-,10,-,-</sub> |  | 1.2<br><sub>1,-,1,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,2,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.5 |
| Darius Acuff Jr. (SAC) | 98% | 36.8<br><sub>40,35,33,35,36</sub> | 22.9<br><sub>29,17,26,36,18</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.7<br><sub>6,6,6,6,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 3.9 | 34.0 |
| De'Andre Hunter (SAC) | 88% | 33.5<br><sub>34,42,-,35,37</sub> | 14.2<br><sub>15,24,-,7,30</sub> |  | 4.8<br><sub>4,5,-,1,6</sub> |  | 1.9<br><sub>2,2,-,4,2</sub> |  | 2.1<br><sub>3,2,-,1,5</sub> |  | 0.6 | 0.2 | 1.6 | 20.9 |
| Zach LaVine (SAC) | 88% | 33.2<br><sub>33,36,-,32,39</sub> | 17.6<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.9<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.0 | 23.9 |
| Domantas Sabonis (SAC) | 98% | 31.9<br><sub>24,35,29,24,38</sub> | 13.5<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 12.0<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>5,5,3,8,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.3 | 2.2 | 30.7 |
| Keegan Murray (SAC) | 98% | 31.2<br><sub>24,40,21,31,40</sub> | 12.2<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.6<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.9 | 1.1 | 18.8 |
| Leaky Black (SAC) | 88% | 20.1<br><sub>18,12,29,17,19</sub> | 4.9<br><sub>0,0,12,3,0</sub> |  | 3.3<br><sub>3,0,9,0,3</sub> |  | 1.3<br><sub>2,0,2,2,1</sub> |  | 0.7<br><sub>0,0,4,1,0</sub> |  | 0.8 | 0.5 | 0.6 | 9.5 |
| Malik Monk (SAC) | 98% | 16.6<br><sub>3,18,29,20,12</sub> | 8.6<br><sub>1,7,14,8,2</sub> |  | 1.5<br><sub>0,4,1,1,0</sub> |  | 3.0<br><sub>0,3,10,2,3</sub> |  | 1.1<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.3 | 1.2 | 13.1 |
| Dylan Cardwell (SAC) | 98% | 14.8<br><sub>29,13,19,12,10</sub> | 4.2<br><sub>1,6,10,6,0</sub> |  | 4.9<br><sub>11,3,6,4,4</sub> |  | 1.1<br><sub>1,3,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.7 | 10.2 |
| Emanuel Sharp (SAC) | 98% | 14.2<br><sub>19,7,21,14,10</sub> | 4.7<br><sub>2,4,9,6,3</sub> |  | 1.1<br><sub>2,0,0,2,0</sub> |  | 0.7<br><sub>0,0,2,1,1</sub> |  | 0.6<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.4 |
| Alex Karaban (SAC) | 52% | 9.5<br><sub>-,-,29,4,-</sub> | 1.8<br><sub>-,-,0,0,-</sub> |  | 1.4<br><sub>-,-,5,1,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Daeqwon Plowden (SAC) | 67% | 8.9<br><sub>2,2,24,4,-</sub> | 3.1<br><sub>0,0,13,3,-</sub> |  | 1.0<br><sub>0,0,2,0,-</sub> |  | 0.4<br><sub>0,0,1,0,-</sub> |  | 0.3<br><sub>0,0,3,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Sean Pedulla (SAC) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jonathan Mogbo (SAC) | 52% | 8.1<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Mason Plumlee (SAC) | 52% | 6.6<br><sub>-,-,5,4,-</sub> | 1.7<br><sub>-,-,2,0,-</sub> |  | 2.0<br><sub>-,-,0,2,-</sub> |  | 0.5<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.3 |

</details>

<details><summary>if Precious Achiuwa plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George (BOS) | 98% | 31.8<br><sub>30,-,25,36,23</sub> | 22.4<br><sub>36,-,7,22,10</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>5,-,7,8,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>1,-,6,3,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8 | 0.3 | 2.5 | 32.1 |
| Payton Pritchard (BOS) | 99% | 30.4<br><sub>30,31,19,32,30</sub> | 18.4<br><sub>18,14,10,21,15</sub> |  | 3.4<br><sub>6,1,1,4,1</sub> |  | 5.5<br><sub>5,1,6,5,2</sub> |  | 2.7<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.5 | 27.4 |
| Neemias Queta (BOS) | 98% | 26.1<br><sub>22,31,15,-,27</sub> | 12.4<br><sub>4,11,8,-,17</sub> |  | 9.0<br><sub>6,13,6,-,10</sub> |  | 2.4<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.1 | 1.4 | 23.8 |
| Sam Hauser (BOS) | 99% | 25.6<br><sub>18,24,11,25,17</sub> | 11.1<br><sub>12,8,8,12,9</sub> |  | 3.6<br><sub>5,9,1,1,2</sub> |  | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.2<br><sub>4,2,2,4,3</sub> |  | 0.6 | 0.2 | 0.5 | 16.4 |
| Baylor Scheierman (BOS) | 99% | 22.9<br><sub>18,29,18,11,13</sub> | 7.6<br><sub>5,9,12,0,0</sub> |  | 4.1<br><sub>3,7,5,1,1</sub> |  | 2.2<br><sub>2,3,3,1,1</sub> |  | 1.3<br><sub>1,3,2,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 14.0 |
| Mitchell Robinson (BOS) | 98% | 19.7<br><sub>17,11,15,18,16</sub> | 6.6<br><sub>2,2,0,4,6</sub> |  | 7.4<br><sub>6,2,7,5,4</sub> |  | 1.0<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.9 | 0.9 | 15.0 |
| Jordan Walsh (BOS) | 98% | 19.6<br><sub>19,18,21,17,4</sub> | 6.5<br><sub>8,6,11,6,0</sub> |  | 3.6<br><sub>2,3,1,2,0</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 0.8<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.3 | 0.6 | 11.2 |
| Hugo Gonzalez (BOS) | 98% | 18.7<br><sub>19,8,18,4,16</sub> | 6.2<br><sub>10,0,9,0,2</sub> |  | 3.8<br><sub>2,1,5,2,6</sub> |  | 1.1<br><sub>2,0,2,0,0</sub> |  | 0.7<br><sub>2,0,2,0,0</sub> |  | 0.8 | 0.3 | 0.7 | 11.1 |
| Devin Carter (BOS) | 91% | 18.3<br><sub>-,-,12,-,-</sub> | 8.9<br><sub>-,-,0,-,-</sub> |  | 3.4<br><sub>-,-,2,-,-</sub> |  | 2.8<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.0 | 0.2 | 1.3 | 15.1 |
| Chris Cenac Jr. (BOS) | 63% | 16.9<br><sub>-,-,7,12,17</sub> | 6.9<br><sub>-,-,6,4,6</sub> |  | 4.0<br><sub>-,-,3,2,6</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,0,0,1</sub> |  | 0.7 | 0.3 | 0.8 | 11.7 |
| Luka Garza (BOS) | 98% | 15.4<br><sub>9,11,14,18,5</sub> | 7.7<br><sub>2,5,2,3,0</sub> |  | 3.6<br><sub>0,1,3,0,1</sub> |  | 1.9<br><sub>2,0,5,4,1</sub> |  | 0.8<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 13.1 |
| Mike Conley (BOS) | 35% | 12.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 6.8 |
| Ron Harper Jr. (BOS) | 52% | 12.7<br><sub>4,-,12,-,-</sub> | 5.5<br><sub>0,-,10,-,-</sub> |  | 1.9<br><sub>1,-,1,-,-</sub> |  | 0.8<br><sub>0,-,0,-,-</sub> |  | 0.8<br><sub>0,-,2,-,-</sub> |  | 0.5 | 0.2 | 0.4 | 8.2 |
| Darius Acuff Jr. (SAC) | 98% | 34.6<br><sub>40,35,33,35,36</sub> | 21.4<br><sub>29,17,26,36,18</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.2<br><sub>6,6,6,6,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 3.6 | 31.8 |
| Zach LaVine (SAC) | 88% | 31.4<br><sub>33,36,-,32,39</sub> | 16.4<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.7<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.0 | 22.3 |
| De'Andre Hunter (SAC) | 88% | 30.8<br><sub>34,42,-,35,37</sub> | 12.9<br><sub>15,24,-,7,30</sub> |  | 4.3<br><sub>4,5,-,1,6</sub> |  | 1.7<br><sub>2,2,-,4,2</sub> |  | 1.8<br><sub>3,2,-,1,5</sub> |  | 0.7 | 0.2 | 1.6 | 18.9 |
| Domantas Sabonis (SAC) | 98% | 30.2<br><sub>24,35,29,24,38</sub> | 12.7<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 11.3<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>5,5,3,8,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 2.2 | 28.8 |
| Keegan Murray (SAC) | 98% | 29.4<br><sub>24,40,21,31,40</sub> | 11.5<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,4,0,3,4</sub> |  | 1.5<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.8 | 1.0 | 17.7 |
| Precious Achiuwa (SAC) | 100% | 20.1<br><sub>14,-,-,8,-</sub> | 8.1<br><sub>10,-,-,0,-</sub> |  | 5.3<br><sub>3,-,-,0,-</sub> |  | 1.1<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.6 | 0.6 | 1.0 | 14.5 |
| Leaky Black (SAC) | 88% | 17.8<br><sub>18,12,29,17,19</sub> | 4.2<br><sub>0,0,12,3,0</sub> |  | 2.9<br><sub>3,0,9,0,3</sub> |  | 1.1<br><sub>2,0,2,2,1</sub> |  | 0.6<br><sub>0,0,4,1,0</sub> |  | 0.8 | 0.4 | 0.5 | 8.2 |
| Malik Monk (SAC) | 98% | 15.6<br><sub>3,18,29,20,12</sub> | 7.9<br><sub>1,7,14,8,2</sub> |  | 1.4<br><sub>0,4,1,1,0</sub> |  | 2.9<br><sub>0,3,10,2,3</sub> |  | 0.9<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.2 | 1.2 | 12.2 |
| Dylan Cardwell (SAC) | 98% | 13.6<br><sub>29,13,19,12,10</sub> | 3.8<br><sub>1,6,10,6,0</sub> |  | 4.5<br><sub>11,3,6,4,4</sub> |  | 1.0<br><sub>1,3,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.6 | 9.3 |
| Emanuel Sharp (SAC) | 98% | 13.0<br><sub>19,7,21,14,10</sub> | 4.3<br><sub>2,4,9,6,3</sub> |  | 1.1<br><sub>2,0,0,2,0</sub> |  | 0.6<br><sub>0,0,2,1,1</sub> |  | 0.5<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.0 |
| Sean Pedulla (SAC) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.1 |
| Alex Karaban (SAC) | 52% | 8.0<br><sub>-,-,29,4,-</sub> | 1.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,5,1,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.1 |
| Daeqwon Plowden (SAC) | 67% | 7.9<br><sub>2,2,24,4,-</sub> | 2.9<br><sub>0,0,13,3,-</sub> |  | 0.9<br><sub>0,0,2,0,-</sub> |  | 0.4<br><sub>0,0,1,0,-</sub> |  | 0.3<br><sub>0,0,3,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Jonathan Mogbo (SAC) | 52% | 7.0<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Mason Plumlee (SAC) | 52% | 6.3<br><sub>-,-,5,4,-</sub> | 1.8<br><sub>-,-,2,0,-</sub> |  | 1.9<br><sub>-,-,0,2,-</sub> |  | 0.6<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-21/`._
