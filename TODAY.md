# NBA model · Sat 21 Nov 2026 (US date)

Updated **Sun 22 Nov, 12:05 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-21/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| NOP @ SAS | player minutes | Derik Queen projected 32 min; most in his last 10 games is 27 | minutes 32 vs 21 this season; teammates out: Mathurin, McGowens, III, Murray (~140 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Taylor Hendricks PTS over 9.5 (10+) | MEM @ MIN | draftkings | 2.44 | 2.00 | 2.08 | 48.1% | 50.4% | 50.0% | +22.1% | +17.3% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PRA over 39.5 (40+) | NOP @ SAS | draftkings | 18.80 | 15.70 | 7.12 | 14.0% | 5.0% | 6.4% | +19.7% | +163.9% | 0.3% |
| Cam Spencer AST over 11.5 (12+) | MEM @ MIN | draftkings | 24.00 | 20.75 | 10.12 | 9.9% | 3.9% | 4.8% | +15.6% | +137.1% | 0.2% |
| Derik Queen PR over 34.5 (35+) | NOP @ SAS | draftkings | 16.00 | 13.87 | 6.78 | 14.8% | 5.8% | 7.2% | +15.4% | +136.0% | 0.3% |
| Saddiq Bey AST over 5.5 (6+) | NOP @ SAS | draftkings | 15.00 | 13.11 | 6.54 | 15.3% | 6.2% | 7.6% | +14.4% | +129.4% | 0.3% |
| Cam Spencer AST over 9.5 (10+) | MEM @ MIN | draftkings | 10.20 | 8.99 | 4.57 | 21.9% | 9.2% | 11.1% | +13.5% | +123.3% | 0.4% |
| Cam Spencer PRA over 34.5 (35+) | MEM @ MIN | draftkings | 20.00 | 18.12 | 9.86 | 10.1% | 4.7% | 5.5% | +10.3% | +102.9% | 0.1% |
| Cam Spencer PA over 29.5 (30+) | MEM @ MIN | draftkings | 17.80 | 16.13 | 8.78 | 11.4% | 5.2% | 6.2% | +10.3% | +102.6% | 0.1% |
| NOP to win | NOP @ SAS | betfair_ex_au | 10.98 | 9.96 | 10.67 | 9.4% | 10.0% | 10.0% | +10.2% | +2.8% | 0.2% |
| Cam Spencer PRA over 29.5 (30+) | MEM @ MIN | draftkings | 8.80 | 8.04 | 4.45 | 22.4% | 10.6% | 12.4% | +9.5% | +97.5% | 0.3% |
| Darius Acuff Jr. AST over 11.5 (12+) | BOS @ SAC | draftkings | 17.20 | 15.75 | 8.77 | 11.4% | 5.4% | 6.3% | +9.3% | +96.1% | 0.1% |
| Victor Wembanyama REB over 17.5 (18+) | NOP @ SAS | draftkings | 12.00 | 11.01 | 6.17 | 16.2% | 7.8% | 9.1% | +9.0% | +94.4% | 0.2% |
| Cam Spencer PA over 24.5 (25+) | MEM @ MIN | draftkings | 7.40 | 6.80 | 3.82 | 26.2% | 12.6% | 14.7% | +8.9% | +93.6% | 0.4% |
| Victor Wembanyama PRA over 64.5 (65+) | NOP @ SAS | draftkings | 16.20 | 14.93 | 8.47 | 11.8% | 5.8% | 6.7% | +8.5% | +91.2% | 0.1% |
| Victor Wembanyama REB over 19.5 (20+) | NOP @ SAS | draftkings | 22.00 | 20.33 | 11.59 | 8.6% | 4.2% | 4.9% | +8.3% | +89.9% | 0.1% |
| Derik Queen REB over 11.5 (12+) | NOP @ SAS | draftkings | 8.40 | 7.77 | 4.46 | 22.4% | 11.1% | 12.9% | +8.1% | +88.5% | 0.3% |
| Victor Wembanyama REB over 15.5 (16+) | NOP @ SAS | draftkings | 6.39 | 5.97 | 3.52 | 28.4% | 14.6% | 16.8% | +7.0% | +81.5% | 0.3% |
| Derik Queen REB over 13.5 (14+) | NOP @ SAS | draftkings | 16.80 | 15.75 | 9.35 | 10.7% | 5.6% | 6.3% | +6.7% | +79.7% | 0.1% |
| Victor Wembanyama PRA over 69.5 (70+) | NOP @ SAS | draftkings | 25.00 | 23.53 | 14.11 | 7.1% | 3.7% | 4.2% | +6.3% | +77.1% | 0.1% |
| Victor Wembanyama PTS over 49.5 (50+) | NOP @ SAS | draftkings | 25.00 | 23.58 | 14.30 | 7.0% | 3.7% | 4.2% | +6.0% | +74.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PR over 24.5 (25+) | NOP @ SAS | draftkings | 3.51 | 3.31 | 2.00 | 50.1% | 26.6% | 30.2% | +6.1% | +75.8% | 0.6% |
| Derik Queen PTS over 9.5 (10+) | NOP @ SAS | sportsbet | 1.88 | 1.78 | 1.18 | 84.5% | 50.9% | 56.1% | +5.3% | +58.7% | 1.5% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAC @ DAL | Sun 22 Nov 12:00 | 116.3–117.3 | LAC 47% | 2.12 / 1.89 | DAL -1.5 | 233.5 | DAL -4.5 covers 40%; o230.5 56% |
| MEM @ MIN | Sun 22 Nov 12:00 | 111.4–119.0 | MEM 29% | 3.45 / 1.41 | MIN -7.5 | 230.5 | MIN -5.5 covers 56%; o227.5 56% |
| NOP @ SAS | Sun 22 Nov 12:00 | 103.9–122.6 | NOP 9% | 10.67 / 1.10 | SAS -18.5 | 226.5 | SAS -19.5 covers 48%; o226.5 50% |
| BOS @ SAC | Sun 22 Nov 14:00 | 115.0–104.6 | BOS 77% | 1.31 / 4.26 | SAC +10.5 | 219.5 | SAC +11.5 covers 53%; o215.5 58% |

### LAC @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), P.J. Washington (DAL), Bradley Beal (LAC), Brandon Ingram (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naji Marshall PTS under 13.5 | LAC @ DAL | tab | 1.95 | 1.91 | 1.82 | 55.1% | 51.9% | 52.4% | +2.3% | +7.5% | 0.6% |
| Cooper Flagg PTS under 24.5 | LAC @ DAL | pointsbetau | 2.00 | 1.99 | 1.93 | 51.8% | 49.9% | 50.2% | +0.4% | +3.7% | 0.1% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 100% | 32.5<br><sub>25,37,35,30,35</sub> | 22.3<br><sub>13,24,27,20,23</sub> | 21.5 · 21.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>5,4,6,3,0</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>6,7,7,7,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>1,3,3,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.2 | 3.4 | 32.3 |
| Rui Hachimura | 100% | 28.4<br><sub>23,32,22,27,32</sub> | 13.9<br><sub>13,7,4,20,17</sub> | 14.5 · 14.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>5,11,2,5,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,1,0,4,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.4 | 1.2 | 19.9 |
| Derrick Jones Jr. | 100% | 26.8<br><sub>24,29,26,28,27</sub> | 10.2<br><sub>11,14,13,5,8</sub> | 9.5 · 9.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>3,5,4,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1<br><sub>2,4,3,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.9 | 0.9 | 15.4 |
| Max Strus | 100% | 26.5<br><sub>22,23,25,21,32</sub> | 10.4<br><sub>12,3,14,3,18</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 4.4<br><sub>3,2,3,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>3,3,4,1,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,0,4,1,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.2 | 1.1 | 18.0 |
| Brook Lopez | 100% | 25.6<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>4,7,5,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,4,8,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.6<br><sub>1,3,1,4,5</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 1.3 | 1.1 | 20.4 |
| Kris Dunn | 98% | 22.8<br><sub>19,20,18,26,20</sub> | 6.4<br><sub>3,2,7,2,6</sub> | 5.5 · 5.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>2,3,3,5,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>3,6,1,5,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.1 |
| Keaton Wagler | 98% | 20.3<br><sub>23,18,28,18,17</sub> | 10.6<br><sub>11,14,12,15,7</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>0,2,4,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,1,5,0,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.2 | 1.8 | 16.2 |
| Kobe Sanders | 98% | 18.8<br><sub>26,15,20,18,14</sub> | 7.3<br><sub>9,5,2,5,0</sub> |  | 2.2<br><sub>3,0,6,1,1</sub> |  | 2.0<br><sub>7,1,4,3,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.6 |
| Gradey Dick | 98% | 14.9<br><sub>19,19,19,17,13</sub> | 6.4<br><sub>10,13,12,0,2</sub> |  | 2.2<br><sub>3,3,2,0,2</sub> |  | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.6<br><sub>1,2,2,0,0</sub> |  | 0.6 | 0.1 | 0.6 | 9.4 |
| Isaiah Jackson | 98% | 14.6<br><sub>16,17,15,19,9</sub> | 6.7<br><sub>4,5,13,8,6</sub> |  | 4.5<br><sub>4,3,2,5,4</sub> |  | 1.3<br><sub>0,3,2,0,2</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 12.5 |
| Yanic Konan Niederhauser | 52% | 9.7<br><sub>-,-,-,-,11</sub> | 4.0<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 7.0 |
| Baba Miller | 88% | 8.9<br><sub>16,-,5,4,1</sub> | 4.4<br><sub>13,-,2,3,0</sub> |  | 1.4<br><sub>4,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.8 |
| Cam Christie | 58% | 6.7<br><sub>-,-,-,4,1</sub> | 2.8<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley | 52% | 6.2<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.4 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 100% | 35.9<br><sub>39,27,38,27,34</sub> | 25.2<br><sub>43,12,18,17,33</sub> | 24.5 · 24.5<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>10,7,8,3,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>6,3,5,4,9</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.8 | 2.9 | 38.8 |
| Kyrie Irving | 100% | 35.2<br><sub>38,27,37,-,29</sub> | 23.4<br><sub>35,10,34,-,17</sub> | 22.5 · 23.5<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>0,3,6,-,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.7<br><sub>4,4,5,-,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>7,2,7,-,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.4 | 2.4 | 32.7 |
| Naji Marshall | 96% | 28.2<br><sub>25,23,30,23,27</sub> | 13.5<br><sub>6,13,12,13,12</sub> | 12.5 · 13.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>5,1,3,2,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.7<br><sub>2,4,5,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>0,1,0,3,2</sub> |  | 1.1 | 0.1 | 1.9 | 21.3 |
| Zaccharie Risacher | 100% | 27.7<br><sub>15,25,14,27,18</sub> | 9.9<br><sub>4,22,5,18,3</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>2,6,2,5,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,3,0,0,0</sub> |  | 1.2<br><sub>0,4,1,1,1</sub> |  | 1.1 | 0.9 | 1.2 | 16.5 |
| Caleb Martin | 100% | 25.1<br><sub>19,21,33,34,20</sub> | 6.9<br><sub>0,7,15,12,8</sub> | 5.5 · 6.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,8,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>5,5,3,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>0,1,1,4,2</sub> |  | 1.0 | 0.4 | 0.9 | 13.0 |
| Daniel Gafford | 100% | 24.1<br><sub>20,16,17,19,24</sub> | 10.5<br><sub>8,3,10,3,6</sub> | 9.5 · 8.5<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>2,3,3,4,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>3,1,1,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.6 | 1.1 | 18.9 |
| Walter Clayton Jr. | 96% | 20.8<br><sub>25,22,13,23,27</sub> | 7.6<br><sub>6,5,2,13,8</sub> |  | 3.1<br><sub>6,1,2,4,2</sub> |  | 3.7<br><sub>4,4,2,3,7</sub> |  | 1.0<br><sub>1,0,0,3,2</sub> |  | 0.7 | 0.2 | 1.6 | 14.4 |
| Morez Johnson Jr. | 98% | 17.1<br><sub>-,13,15,26,15</sub> | 6.1<br><sub>-,0,4,2,3</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>-,2,2,6,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>-,0,0,4,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 10.8 |
| Max Christie | 98% | 15.6<br><sub>5,7,-,-,8</sub> | 5.6<br><sub>0,3,-,-,5</sub> |  | 1.9<br><sub>2,2,-,-,1</sub> |  | 1.0<br><sub>0,0,-,-,2</sub> |  | 0.8<br><sub>0,1,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 8.5 |
| Santi Aldama | 98% | 14.5<br><sub>19,10,16,-,6</sub> | 6.9<br><sub>10,3,7,-,0</sub> |  | 3.4<br><sub>4,1,2,-,0</sub> |  | 1.1<br><sub>1,1,1,-,0</sub> |  | 0.7<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.3 | 0.8 | 11.5 |
| Marcus Sasser | 67% | 12.0<br><sub>-,9,-,18,4</sub> | 4.0<br><sub>-,3,-,5,0</sub> |  | 1.1<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.6 |
| Moussa Cisse | 67% | 7.5<br><sub>-,8,-,4,4</sub> | 2.6<br><sub>-,0,-,1,0</sub> |  | 2.7<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.5 |

</details>


### MEM @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM), Javon Small (MEM)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Taylor Hendricks PTS over 9.5 (10+) | MEM @ MIN | draftkings | 2.44 | 2.00 | 2.08 | 48.1% | 50.4% | 50.0% | +22.1% | +17.3% | 2.0% |
| Rudy Gobert PTS over 9.5 (10+) | MEM @ MIN | pointsbetau | 2.10 | 2.09 | 2.09 | 47.9% | 47.9% | 47.9% | +0.5% | +0.6% | 0.1% |
| Jaylen Wells PTS over 10.5 (11+) | MEM @ MIN | pointsbetau | 2.00 | 2.00 | 1.89 | 52.9% | 49.6% | 50.1% | +0.2% | +5.8% | 0.1% |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 100% | 32.0<br><sub>30,33,27,33,25</sub> | 14.9<br><sub>14,23,18,20,19</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>7,12,8,3,4</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>6,4,6,5,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>0,4,2,4,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.6 | 2.0 | 26.6 |
| Ty Jerome | 100% | 30.6<br><sub>29,-,-,-,-</sub> | 23.0<br><sub>17,-,-,-,-</sub> | 23.5 · 22.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>2,-,-,-,-</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.0<br><sub>9,-,-,-,-</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>2,-,-,-,-</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.3 | 2.8 | 32.9 |
| Jaylen Wells | 100% | 29.9<br><sub>27,25,27,26,24</sub> | 11.6<br><sub>11,5,8,5,22</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,2,4,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 1.1 | 16.8 |
| Cam Spencer | 98% | 29.1<br><sub>24,34,32,29,27</sub> | 13.2<br><sub>14,17,12,26,9</sub> | 10.5 · 9.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,1,6,1,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 7.2<br><sub>5,8,9,7,11</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>3,3,1,5,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.2 | 1.7 | 23.8 |
| Jahmai Mashack | 100% | 24.3<br><sub>-,2,2,13,26</sub> | 6.5<br><sub>-,0,0,3,0</sub> |  | 3.2<br><sub>-,0,0,2,3</sub> |  | 3.2<br><sub>-,0,1,2,4</sub> |  | 0.6<br><sub>-,0,0,1,0</sub> |  | 1.2 | 0.5 | 1.4 | 12.8 |
| Zach Edey | 100% | 23.9<br><sub>-,-,21,21,-</sub> | 10.2<br><sub>-,-,23,11,-</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 8.8<br><sub>-,-,10,2,-</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>-,-,1,1,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.5 | 1.6 | 1.7 | 20.2 |
| Taylor Hendricks | 88% | 22.8<br><sub>19,29,19,21,20</sub> | 9.9<br><sub>10,22,9,18,11</sub> | 7.5 · 9.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>12,5,3,6,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>2,4,0,2,1</sub> |  | 1.1<br><sub>2,0,1,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.6 | 1.1 | 15.9 |
| Olivier-Maxence Prosper | 86% | 21.2<br><sub>2,20,16,16,24</sub> | 10.2<br><sub>6,11,12,5,16</sub> |  | 4.0<br><sub>1,4,0,2,5</sub> |  | 1.1<br><sub>0,0,1,0,1</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.8 | 0.3 | 1.0 | 15.2 |
| Isaiah Stewart | 98% | 18.9<br><sub>20,15,-,-,18</sub> | 8.5<br><sub>12,11,-,-,8</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>5,3,-,-,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>0,3,-,-,1</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.4 | 1.2 | 1.0 | 13.5 |
| Kris Murray | 88% | 15.7<br><sub>1,19,6,6,4</sub> | 3.0<br><sub>0,3,0,5,0</sub> |  | 2.3<br><sub>1,2,1,0,1</sub> |  | 1.0<br><sub>0,3,0,0,0</sub> |  | 0.2<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 6.3 |
| Quinten Post | 96% | 13.8<br><sub>-,-,9,6,10</sub> | 4.9<br><sub>-,-,5,3,5</sub> |  | 2.7<br><sub>-,-,3,2,1</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.4 | 0.4 | 0.7 | 8.1 |
| Karim Lopez | 58% | 9.9<br><sub>-,2,1,-,4</sub> | 2.9<br><sub>-,0,0,-,3</sub> |  | 1.9<br><sub>-,2,0,-,0</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.5 | 0.5 | 0.4 | 5.2 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 35.1<br><sub>25,37,31,37,39</sub> | 17.4<br><sub>16,18,13,22,17</sub> | 17.5 · 17.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>9,5,6,5,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,6,3,4,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>0,2,0,2,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 1.2 | 1.9 | 26.5 |
| Ayo Dosunmu | 100% | 33.0<br><sub>27,33,30,39,32</sub> | 18.5<br><sub>18,24,8,30,6</sub> | 17.5 · 17.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>2,5,5,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.1<br><sub>1,0,2,5,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>2,0,2,7,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.3 | 0.5 | 1.9 | 27.1 |
| Jonathan Kuminga | 100% | 31.9<br><sub>24,35,29,-,35</sub> | 15.0<br><sub>14,11,13,-,23</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>8,3,9,-,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>5,3,1,-,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,0,1,-,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.8 | 1.7 | 23.6 |
| LaMelo Ball | 100% | 30.6<br><sub>25,30,24,31,35</sub> | 20.6<br><sub>22,19,6,18,15</sub> | 20.5 · 20.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>3,8,5,9,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>9,6,0,2,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.5<br><sub>6,4,2,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6 | 0.3 | 2.9 | 31.9 |
| Rudy Gobert | 100% | 30.2<br><sub>23,27,32,22,35</sub> | 9.9<br><sub>9,1,18,0,9</sub> | 9.5 · 8.5<br><sub>o 52% · u 48%</sub> | 11.3<br><sub>6,10,15,4,7</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,4,3,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.7 | 1.4 | 22.9 |
| Terrence Shannon Jr. | 98% | 23.5<br><sub>21,22,35,24,21</sub> | 13.2<br><sub>6,14,34,12,10</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,6,3,1,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>4,0,6,4,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,0,3,1,0</sub> |  | 0.7 | 0.2 | 1.2 | 18.8 |
| Trey Lyles | 98% | 19.7<br><sub>15,19,19,31,16</sub> | 6.2<br><sub>2,5,9,8,8</sub> |  | 4.4<br><sub>0,1,3,7,6</sub> |  | 1.2<br><sub>0,2,1,4,1</sub> |  | 0.8<br><sub>0,0,2,2,2</sub> |  | 0.6 | 0.4 | 0.6 | 11.8 |
| Joan Beringer | 98% | 16.2<br><sub>22,13,16,26,13</sub> | 6.2<br><sub>13,2,0,3,5</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 5.8<br><sub>9,5,4,13,3</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.5 | 0.6 | 12.5 |
| Bones Hyland | 98% | 15.5<br><sub>23,21,13,17,15</sub> | 9.3<br><sub>24,12,5,13,6</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,1,1,2,1</sub> |  | 2.6<br><sub>8,2,5,1,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>5,3,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 1.0 | 13.6 |
| Cody Williams | 58% | 7.2<br><sub>7,-,4,13,-</sub> | 0.2<br><sub>0,-,0,0,-</sub> |  | 1.1<br><sub>1,-,1,1,-</sub> |  | 0.3<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 1.7 |
| Zyon Pullin | 38% | 6.2<br><sub>-,-,4,-,-</sub> | 2.7<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |
| Isaiah Evans | 48% | 5.6<br><sub>8,-,4,-,-</sub> | 4.2<br><sub>2,-,0,-,-</sub> |  | 1.2<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.7 |
| Johni Broome | 3% | 5.3 | 2.0 |  | 1.3 |  | 0.4 |  | 0.1 |  | 0.3 | 0.2 | 0.3 | 3.7 |

</details>


### NOP @ SAS
Out: Dylan Harper (SAS), Tobias Harris (SAS), Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Zion Williamson (NOP)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jeremiah Fears PTS over 16.5 (17+) | NOP @ SAS | betright | 2.00 | 1.97 | 1.69 | 59.3% | 49.1% | 50.7% | +1.4% | +18.6% | 0.3% |
| Julian Champagnie PTS over 11.5 (12+) | NOP @ SAS | pointsbetau | 2.05 | 2.04 | 2.02 | 49.6% | 49.0% | 49.1% | +0.6% | +1.7% | 0.1% |
| Stephon Castle PTS over 17.5 (18+) | NOP @ SAS | pointsbetau | 2.00 | 1.99 | 1.97 | 50.7% | 50.1% | 50.2% | +0.5% | +1.5% | 0.1% |
| Jeremiah Fears PTS over 15.5 (16+) | NOP @ SAS | pointsbetau | 1.87 | 1.87 | 1.55 | 64.6% | 51.6% | 53.6% | +0.2% | +20.7% | 0.1% |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 100% | 36.5<br><sub>35,41,33,42,37</sub> | 19.5<br><sub>30,16,23,10,21</sub> | 17.5 · 16.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>10,6,6,8,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 3.4<br><sub>0,4,3,6,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>6,2,5,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 1.4 | 28.5 |
| Jeremiah Fears | 100% | 33.8<br><sub>34,33,29,31,38</sub> | 19.2<br><sub>18,13,19,16,22</sub> | 16.5 · 15.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>5,4,10,5,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.0<br><sub>7,7,10,4,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>0,1,1,2,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.5 | 3.4 | 30.3 |
| Herbert Jones | 100% | 31.9<br><sub>32,27,24,32,33</sub> | 11.1<br><sub>8,10,8,9,14</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.9<br><sub>3,1,3,3,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,2,2,3,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.5 | 1.7 | 17.4 |
| Derik Queen | 100% | 31.7<br><sub>23,25,21,19,18</sub> | 16.5<br><sub>10,10,17,9,11</sub> | 12.5 · 9.5<br><sub>o 56% · u 44%</sub> | 9.0<br><sub>6,5,10,5,7</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 3.9<br><sub>2,4,0,0,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>0,2,4,0,0</sub> |  | 1.2 | 1.1 | 2.8 | 29.4 |
| Jordan Poole | 88% | 27.8<br><sub>21,24,31,30,13</sub> | 13.8<br><sub>13,14,11,22,6</sub> | 11.5 · 10.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>2,2,2,1,0</sub> |  | 3.9<br><sub>5,5,5,5,1</sub> |  | 2.2<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 1.8 | 20.4 |
| Yves Missi | 100% | 26.1<br><sub>-,22,23,17,23</sub> | 8.5<br><sub>-,3,6,4,4</sub> | 6.5 · 5.5<br><sub>o 54% · u 46%</sub> | 7.8<br><sub>-,8,14,5,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>-,1,1,2,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.5 | 1.5 | 1.2 | 18.2 |
| Karlo Matkovic | 98% | 25.2<br><sub>19,14,20,10,8</sub> | 9.2<br><sub>1,5,3,0,0</sub> |  | 5.3<br><sub>3,3,2,2,2</sub> |  | 1.5<br><sub>0,1,0,0,0</sub> |  | 1.2<br><sub>0,1,0,0,0</sub> |  | 0.7 | 0.9 | 1.1 | 16.0 |
| Jaron Pierre Jr. | 96% | 19.3<br><sub>4,23,19,17,4</sub> | 7.4<br><sub>0,13,10,7,3</sub> |  | 2.5<br><sub>0,2,4,1,2</sub> |  | 1.1<br><sub>0,0,0,1,0</sub> |  | 1.1<br><sub>0,2,2,1,1</sub> |  | 0.6 | 0.2 | 1.0 | 11.1 |
| DeAndre Jordan | 48% | 16.0<br><sub>17,-,-,10,-</sub> | 4.8<br><sub>6,-,-,8,-</sub> |  | 5.7<br><sub>8,-,-,2,-</sub> |  | 1.1<br><sub>1,-,-,1,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.6 | 0.8 | 11.5 |
| AJ Johnson | 52% | 13.7<br><sub>4,-,6,-,-</sub> | 4.4<br><sub>1,-,0,-,-</sub> |  | 2.0<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.3 | 0.6 | 7.5 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 100% | 32.6<br><sub>-,23,32,36,32</sub> | 14.0<br><sub>-,7,6,12,15</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>-,2,6,5,4</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 3.2<br><sub>-,2,1,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>-,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.5 | 1.1 | 21.5 |
| Victor Wembanyama | 100% | 32.1<br><sub>32,21,35,34,33</sub> | 30.6<br><sub>32,12,26,25,32</sub> | 29.5 · 28.5<br><sub>o 49% · u 51%</sub> | 13.1<br><sub>9,12,10,18,11</sub> | 10.5<br><sub>o 56% · u 44%</sub> | 3.8<br><sub>1,6,6,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>2,0,4,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 4.2 | 2.4 | 47.4 |
| De'Aaron Fox | 100% | 31.8<br><sub>31,17,-,34,32</sub> | 16.4<br><sub>17,7,-,6,10</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>4,5,-,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>9,1,-,2,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,-,0,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.4 | 2.2 | 26.7 |
| Stephon Castle | 100% | 31.5<br><sub>29,25,35,31,33</sub> | 18.7<br><sub>11,32,20,10,21</sub> | 17.5 · 17.5<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>1,5,4,2,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 7.2<br><sub>3,6,9,7,12</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,5,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 2.9 | 31.0 |
| Julian Champagnie | 100% | 30.4<br><sub>35,23,24,30,29</sub> | 12.2<br><sub>12,7,4,14,20</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>0,8,5,6,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>2,3,1,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>3,1,1,4,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.7 | 0.9 | 19.5 |
| Keldon Johnson | 99% | 25.6<br><sub>28,25,29,15,27</sub> | 11.4<br><sub>10,18,11,4,10</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>6,4,10,2,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>4,4,2,1,3</sub> |  | 0.7<br><sub>0,2,1,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 19.4 |
| Harrison Barnes | 91% | 16.2<br><sub>13,21,14,10,16</sub> | 5.9<br><sub>3,11,0,0,9</sub> | 6.5 · 5.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>1,1,0,3,2</sub> |  | 1.0<br><sub>0,1,2,4,1</sub> |  | 0.8<br><sub>1,3,0,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 8.8 |
| Luke Kornet | 99% | 16.0<br><sub>14,16,13,14,15</sub> | 4.3<br><sub>7,6,2,2,4</sub> |  | 4.7<br><sub>5,7,2,1,0</sub> |  | 1.4<br><sub>1,2,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.5 | 10.4 |
| Jordan McLaughlin | 71% | 13.8<br><sub>2,14,19,-,11</sub> | 4.5<br><sub>4,4,10,-,0</sub> |  | 1.9<br><sub>0,6,1,-,1</sub> |  | 2.4<br><sub>0,2,2,-,5</sub> |  | 0.5<br><sub>0,0,2,-,0</sub> |  | 0.9 | 0.1 | 0.6 | 8.8 |
| Carter Bryant | 93% | 13.0<br><sub>15,19,5,2,13</sub> | 4.8<br><sub>10,8,0,0,3</sub> |  | 2.1<br><sub>1,3,1,0,1</sub> |  | 0.9<br><sub>2,2,0,0,0</sub> |  | 0.7<br><sub>2,2,0,0,1</sub> |  | 0.3 | 0.4 | 0.5 | 7.8 |
| Tarris Reed Jr. | 52% | 8.7<br><sub>2,11,-,-,-</sub> | 3.2<br><sub>0,2,-,-,-</sub> |  | 3.4<br><sub>0,4,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.5 | 7.1 |
| David Jones Garcia | 52% | 6.9<br><sub>2,-,-,-,-</sub> | 2.8<br><sub>0,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.2 |

</details>


### BOS @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Mitchell Robinson (BOS), Jayson Tatum (BOS), Derrick White (BOS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.0–104.6 | BOS 77% | 1.31 / 4.26 | SAC +10.5 | 219.5 | SAC +11.5 covers 53%; o215.5 58% |
| Expected (weighted by chance each plays) | 115.1–104.8 | BOS 76% | 1.31 / 4.20 | SAC +10.5 | 220.5 | SAC +11.5 covers 53%; o215.5 59% |
| if Precious Achiuwa plays | 115.1–105.0 | BOS 76% | 1.32 / 4.12 | SAC +10.5 | 220.5 | SAC +11.5 covers 54%; o215.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa (SAC) | Questionable | 55% | 20.4 | 8.0 | 5.4 | 1.1 | 0.3 | 0.7 | 0.6 | 1.0 | 14.5 | full tables below |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George | 98% | 31.9<br><sub>30,-,25,36,23</sub> | 22.3<br><sub>36,-,7,22,10</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,-,7,8,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>1,-,6,3,1</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 3.1<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.4 | 2.5 | 32.1 |
| Payton Pritchard | 99% | 31.0<br><sub>30,31,19,32,30</sub> | 19.5<br><sub>18,14,10,21,15</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>6,1,1,4,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,1,6,5,2</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.1 | 1.6 | 28.5 |
| Neemias Queta | 98% | 27.2<br><sub>22,31,15,-,27</sub> | 13.0<br><sub>4,11,8,-,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 9.7<br><sub>6,13,6,-,10</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>3,3,2,-,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.2 | 1.4 | 25.2 |
| Sam Hauser | 99% | 26.5<br><sub>18,24,11,25,17</sub> | 11.2<br><sub>12,8,8,12,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>5,9,1,1,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.3<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 0.5 | 16.8 |
| Baylor Scheierman | 99% | 24.3<br><sub>18,29,18,11,13</sub> | 8.3<br><sub>5,9,12,0,0</sub> | 9.5 · –<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>3,7,5,1,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>2,3,3,1,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,3,2,0,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.1 | 0.8 | 15.0 |
| Jordan Walsh | 98% | 22.0<br><sub>19,18,21,17,4</sub> | 7.2<br><sub>8,6,11,6,0</sub> |  | 4.1<br><sub>2,3,1,2,0</sub> |  | 1.2<br><sub>2,0,0,0,0</sub> |  | 0.9<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.3 | 0.7 | 12.5 |
| Hugo Gonzalez | 98% | 21.7<br><sub>19,8,18,4,16</sub> | 7.3<br><sub>10,0,9,0,2</sub> |  | 4.3<br><sub>2,1,5,2,6</sub> |  | 1.2<br><sub>2,0,2,0,0</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.9 | 0.4 | 0.8 | 12.8 |
| Devin Carter | 91% | 19.9<br><sub>-,-,12,-,-</sub> | 9.5<br><sub>-,-,0,-,-</sub> |  | 3.6<br><sub>-,-,2,-,-</sub> |  | 2.9<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.0 | 0.2 | 1.3 | 16.0 |
| Chris Cenac Jr. | 63% | 18.9<br><sub>-,-,7,12,17</sub> | 7.4<br><sub>-,-,6,4,6</sub> |  | 4.7<br><sub>-,-,3,2,6</sub> |  | 0.9<br><sub>-,-,0,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.8 | 0.3 | 0.8 | 13.1 |
| Luka Garza | 98% | 18.1<br><sub>9,11,14,18,5</sub> | 8.9<br><sub>2,5,2,3,0</sub> |  | 4.4<br><sub>0,1,3,0,1</sub> |  | 2.0<br><sub>2,0,5,4,1</sub> |  | 0.9<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.5 | 0.8 | 15.3 |
| Mike Conley | 35% | 14.8<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.2 | 0.6 | 8.0 |
| Ron Harper Jr. | 52% | 14.5<br><sub>4,-,12,-,-</sub> | 6.1<br><sub>0,-,10,-,-</sub> |  | 2.1<br><sub>1,-,1,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 9.2 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 36.8<br><sub>40,35,33,35,36</sub> | 23.2<br><sub>29,17,26,36,18</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.7<br><sub>6,6,6,6,12</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 3.8 | 34.3 |
| De'Andre Hunter | 88% | 33.8<br><sub>34,42,-,35,37</sub> | 14.4<br><sub>15,24,-,7,30</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>4,5,-,1,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,2,-,4,2</sub> |  | 2.1<br><sub>3,2,-,1,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 1.6 | 21.1 |
| Zach LaVine | 88% | 33.6<br><sub>33,36,-,32,39</sub> | 17.7<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.0 | 23.9 |
| Domantas Sabonis | 98% | 32.3<br><sub>24,35,29,24,38</sub> | 13.4<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 12.1<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,5,3,8,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.3 | 2.3 | 30.6 |
| Keegan Murray | 98% | 31.8<br><sub>24,40,21,31,40</sub> | 12.5<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.7<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.9 | 1.1 | 19.2 |
| Leaky Black | 88% | 20.5<br><sub>18,12,29,17,19</sub> | 5.0<br><sub>0,0,12,3,0</sub> |  | 3.4<br><sub>3,0,9,0,3</sub> |  | 1.4<br><sub>2,0,2,2,1</sub> |  | 0.8<br><sub>0,0,4,1,0</sub> |  | 0.8 | 0.5 | 0.6 | 9.7 |
| Malik Monk | 98% | 16.6<br><sub>3,18,29,20,12</sub> | 8.6<br><sub>1,7,14,8,2</sub> |  | 1.5<br><sub>0,4,1,1,0</sub> |  | 3.0<br><sub>0,3,10,2,3</sub> |  | 1.1<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.3 | 1.2 | 13.1 |
| Dylan Cardwell | 98% | 15.1<br><sub>29,13,19,12,10</sub> | 4.3<br><sub>1,6,10,6,0</sub> |  | 5.0<br><sub>11,3,6,4,4</sub> |  | 1.1<br><sub>1,3,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.7 | 10.4 |
| Emanuel Sharp | 98% | 14.3<br><sub>19,7,21,14,10</sub> | 4.8<br><sub>2,4,9,6,3</sub> |  | 1.1<br><sub>2,0,0,2,0</sub> |  | 0.7<br><sub>0,0,2,1,1</sub> |  | 0.6<br><sub>0,0,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Alex Karaban | 52% | 10.9<br><sub>-,-,29,4,-</sub> | 2.2<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,5,1,-</sub> |  | 0.5<br><sub>-,-,1,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.2 |
| Daeqwon Plowden | 67% | 9.6<br><sub>2,2,24,4,-</sub> | 3.4<br><sub>0,0,13,3,-</sub> |  | 1.1<br><sub>0,0,2,0,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.4<br><sub>0,0,3,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.0 |
| Mason Plumlee | 52% | 6.8<br><sub>-,-,5,4,-</sub> | 1.8<br><sub>-,-,2,0,-</sub> |  | 2.0<br><sub>-,-,0,2,-</sub> |  | 0.5<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.3 |

</details>

<details><summary>if Precious Achiuwa plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George (BOS) | 98% | 31.9<br><sub>30,-,25,36,23</sub> | 22.5<br><sub>36,-,7,22,10</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,-,7,8,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>1,-,6,3,1</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 3.1<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.4 | 2.5 | 32.3 |
| Payton Pritchard (BOS) | 99% | 31.1<br><sub>30,31,19,32,30</sub> | 19.4<br><sub>18,14,10,21,15</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>6,1,1,4,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,1,6,5,2</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.1 | 1.6 | 28.5 |
| Neemias Queta (BOS) | 98% | 27.1<br><sub>22,31,15,-,27</sub> | 13.0<br><sub>4,11,8,-,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 9.7<br><sub>6,13,6,-,10</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>3,3,2,-,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.2 | 1.4 | 25.1 |
| Sam Hauser (BOS) | 99% | 26.5<br><sub>18,24,11,25,17</sub> | 11.2<br><sub>12,8,8,12,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>5,9,1,1,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.2<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 0.5 | 16.7 |
| Baylor Scheierman (BOS) | 99% | 24.4<br><sub>18,29,18,11,13</sub> | 8.3<br><sub>5,9,12,0,0</sub> | 9.5 · –<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>3,7,5,1,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>2,3,3,1,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,3,2,0,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.1 | 0.9 | 15.0 |
| Jordan Walsh (BOS) | 98% | 22.0<br><sub>19,18,21,17,4</sub> | 7.2<br><sub>8,6,11,6,0</sub> |  | 4.1<br><sub>2,3,1,2,0</sub> |  | 1.2<br><sub>2,0,0,0,0</sub> |  | 0.9<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.3 | 0.7 | 12.5 |
| Hugo Gonzalez (BOS) | 98% | 21.7<br><sub>19,8,18,4,16</sub> | 7.2<br><sub>10,0,9,0,2</sub> |  | 4.4<br><sub>2,1,5,2,6</sub> |  | 1.2<br><sub>2,0,2,0,0</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.9 | 0.4 | 0.8 | 12.8 |
| Devin Carter (BOS) | 91% | 19.8<br><sub>-,-,12,-,-</sub> | 9.4<br><sub>-,-,0,-,-</sub> |  | 3.6<br><sub>-,-,2,-,-</sub> |  | 2.9<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.0 | 0.2 | 1.4 | 15.9 |
| Chris Cenac Jr. (BOS) | 63% | 19.0<br><sub>-,-,7,12,17</sub> | 7.6<br><sub>-,-,6,4,6</sub> |  | 4.7<br><sub>-,-,3,2,6</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.8 | 0.3 | 0.9 | 13.3 |
| Luka Garza (BOS) | 98% | 18.0<br><sub>9,11,14,18,5</sub> | 8.9<br><sub>2,5,2,3,0</sub> |  | 4.3<br><sub>0,1,3,0,1</sub> |  | 2.0<br><sub>2,0,5,4,1</sub> |  | 0.9<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.5 | 0.8 | 15.2 |
| Mike Conley (BOS) | 35% | 14.8<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.2 | 0.7 | 8.0 |
| Ron Harper Jr. (BOS) | 52% | 14.5<br><sub>4,-,12,-,-</sub> | 6.1<br><sub>0,-,10,-,-</sub> |  | 2.1<br><sub>1,-,1,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 9.2 |
| Darius Acuff Jr. (SAC) | 98% | 35.0<br><sub>40,35,33,35,36</sub> | 21.8<br><sub>29,17,26,36,18</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.3<br><sub>6,6,6,6,12</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 3.7 | 32.4 |
| Zach LaVine (SAC) | 88% | 31.8<br><sub>33,36,-,32,39</sub> | 16.6<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.2 | 2.0 | 22.6 |
| De'Andre Hunter (SAC) | 88% | 31.5<br><sub>34,42,-,35,37</sub> | 13.2<br><sub>15,24,-,7,30</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>4,5,-,1,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,2,-,4,2</sub> |  | 1.9<br><sub>3,2,-,1,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 1.6 | 19.4 |
| Domantas Sabonis (SAC) | 98% | 30.7<br><sub>24,35,29,24,38</sub> | 13.0<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 11.6<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>5,5,3,8,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 2.3 | 29.6 |
| Keegan Murray (SAC) | 98% | 29.8<br><sub>24,40,21,31,40</sub> | 11.7<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.5<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.8 | 1.0 | 18.0 |
| Precious Achiuwa (SAC) | 100% | 20.4<br><sub>14,-,-,8,-</sub> | 8.0<br><sub>10,-,-,0,-</sub> | 5.5 · – | 5.4<br><sub>3,-,-,0,-</sub> | 4.5 | 1.1<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.7 | 0.6 | 1.0 | 14.5 |
| Leaky Black (SAC) | 88% | 18.2<br><sub>18,12,29,17,19</sub> | 4.3<br><sub>0,0,12,3,0</sub> |  | 3.0<br><sub>3,0,9,0,3</sub> |  | 1.2<br><sub>2,0,2,2,1</sub> |  | 0.6<br><sub>0,0,4,1,0</sub> |  | 0.8 | 0.4 | 0.5 | 8.5 |
| Malik Monk (SAC) | 98% | 15.8<br><sub>3,18,29,20,12</sub> | 7.9<br><sub>1,7,14,8,2</sub> |  | 1.4<br><sub>0,4,1,1,0</sub> |  | 2.9<br><sub>0,3,10,2,3</sub> |  | 1.0<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.2 | 1.2 | 12.2 |
| Dylan Cardwell (SAC) | 98% | 13.7<br><sub>29,13,19,12,10</sub> | 3.9<br><sub>1,6,10,6,0</sub> |  | 4.5<br><sub>11,3,6,4,4</sub> |  | 1.0<br><sub>1,3,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.6 | 9.5 |
| Emanuel Sharp (SAC) | 98% | 13.3<br><sub>19,7,21,14,10</sub> | 4.5<br><sub>2,4,9,6,3</sub> |  | 1.1<br><sub>2,0,0,2,0</sub> |  | 0.6<br><sub>0,0,2,1,1</sub> |  | 0.5<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.2 |
| Alex Karaban (SAC) | 52% | 8.1<br><sub>-,-,29,4,-</sub> | 1.6<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,5,1,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.2 |
| Daeqwon Plowden (SAC) | 67% | 8.1<br><sub>2,2,24,4,-</sub> | 3.0<br><sub>0,0,13,3,-</sub> |  | 0.9<br><sub>0,0,2,0,-</sub> |  | 0.4<br><sub>0,0,1,0,-</sub> |  | 0.3<br><sub>0,0,3,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Mason Plumlee (SAC) | 52% | 6.3<br><sub>-,-,5,4,-</sub> | 1.8<br><sub>-,-,2,0,-</sub> |  | 1.9<br><sub>-,-,0,2,-</sub> |  | 0.6<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-21/`._
