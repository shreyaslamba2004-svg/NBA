# NBA model · Sat 21 Nov 2026 (US date)

Updated **Sun 22 Nov, 08:56 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-21/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cam Spencer AST over 11.5 (12+) | MEM @ MIN | draftkings | 27.00 | 22.47 | 10.13 | 9.9% | 3.5% | 4.5% | +20.1% | +166.5% | 0.2% |
| Cam Spencer AST over 9.5 (10+) | MEM @ MIN | draftkings | 11.60 | 9.81 | 4.57 | 21.9% | 8.1% | 10.2% | +18.2% | +153.9% | 0.4% |
| Cam Spencer PRA over 29.5 (30+) | MEM @ MIN | draftkings | 9.90 | 8.72 | 4.42 | 22.6% | 9.4% | 11.5% | +13.6% | +124.0% | 0.4% |
| Zion Williamson AST over 5.5 (6+) | NOP @ SAS | draftkings | 12.20 | 10.75 | 5.46 | 18.3% | 7.7% | 9.3% | +13.5% | +123.4% | 0.3% |
| Cam Spencer PA over 29.5 (30+) | MEM @ MIN | draftkings | 19.40 | 17.09 | 8.69 | 11.5% | 4.8% | 5.9% | +13.4% | +123.1% | 0.2% |
| Cam Spencer PRA over 34.5 (35+) | MEM @ MIN | draftkings | 21.00 | 18.66 | 9.66 | 10.3% | 4.5% | 5.4% | +12.6% | +117.4% | 0.2% |
| Cam Spencer PA over 24.5 (25+) | MEM @ MIN | draftkings | 8.00 | 7.19 | 3.82 | 26.2% | 11.7% | 13.9% | +11.3% | +109.3% | 0.4% |
| Darius Acuff Jr. AST over 11.5 (12+) | BOS @ SAC | draftkings | 18.00 | 16.26 | 8.77 | 11.4% | 5.2% | 6.2% | +10.7% | +105.2% | 0.2% |
| Victor Wembanyama PRA over 64.5 (65+) | NOP @ SAS | draftkings | 15.80 | 14.33 | 7.79 | 12.8% | 5.9% | 7.0% | +10.3% | +102.9% | 0.2% |
| NOP to win | NOP @ SAS | betfair_ex_au | 10.98 | 9.96 | 8.76 | 11.4% | 10.0% | 10.0% | +10.2% | +25.2% | 0.2% |
| Victor Wembanyama REB over 17.5 (18+) | NOP @ SAS | draftkings | 11.60 | 10.62 | 5.91 | 16.9% | 8.1% | 9.4% | +9.3% | +96.4% | 0.2% |
| Victor Wembanyama REB over 19.5 (20+) | NOP @ SAS | draftkings | 20.80 | 19.16 | 10.89 | 9.2% | 4.5% | 5.2% | +8.5% | +91.0% | 0.1% |
| Victor Wembanyama PTS over 49.5 (50+) | NOP @ SAS | draftkings | 25.00 | 23.09 | 13.23 | 7.6% | 3.7% | 4.3% | +8.2% | +89.0% | 0.1% |
| Victor Wembanyama PRA over 69.5 (70+) | NOP @ SAS | draftkings | 24.00 | 22.22 | 12.77 | 7.8% | 3.9% | 4.5% | +8.0% | +87.9% | 0.1% |
| Victor Wembanyama REB over 15.5 (16+) | NOP @ SAS | draftkings | 6.06 | 5.69 | 3.42 | 29.3% | 15.4% | 17.6% | +6.4% | +77.4% | 0.3% |
| Victor Wembanyama PA over 54.5 (55+) | NOP @ SAS | draftkings | 24.00 | 22.57 | 13.56 | 7.4% | 3.9% | 4.4% | +6.3% | +77.0% | 0.1% |
| Victor Wembanyama PRA over 59.5 (60+) | NOP @ SAS | draftkings | 8.80 | 8.29 | 5.01 | 20.0% | 10.6% | 12.1% | +6.1% | +75.8% | 0.2% |
| Victor Wembanyama BLK over 6.5 (7+) | NOP @ SAS | draftkings | 10.60 | 10.02 | 6.11 | 16.4% | 8.8% | 10.0% | +5.8% | +73.5% | 0.1% |
| Victor Wembanyama PTS over 44.5 (45+) | NOP @ SAS | draftkings | 13.20 | 12.48 | 7.63 | 13.1% | 7.1% | 8.0% | +5.7% | +72.9% | 0.1% |
| Saddiq Bey AST over 5.5 (6+) | NOP @ SAS | draftkings | 16.20 | 15.36 | 9.47 | 10.6% | 5.8% | 6.5% | +5.4% | +71.0% | 0.1% |
| Victor Wembanyama BLK over 7.5 (8+) | NOP @ SAS | draftkings | 18.20 | 17.30 | 10.75 | 9.3% | 5.1% | 5.8% | +5.1% | +69.3% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| POR @ NYK | Sun 22 Nov 11:30 | 107.9–111.4 | POR 40% | 2.47 / 1.68 | NYK -3.5 | 219.5 | NYK -2.5 covers 53%; o215.5 58% |
| LAC @ DAL | Sun 22 Nov 12:00 | 116.7–117.0 | LAC 49% | 2.04 / 1.97 | DAL +0.5 | 233.5 | DAL -4.5 covers 39%; o230.5 56% |
| MEM @ MIN | Sun 22 Nov 12:00 | 111.5–119.1 | MEM 29% | 3.43 / 1.41 | MIN -7.5 | 230.5 | MIN -6.5 covers 53%; o228.5 54% |
| NOP @ SAS | Sun 22 Nov 12:00 | 104.8–121.8 | NOP 11% | 8.76 / 1.13 | SAS -17.5 | 226.5 | SAS -18.5 covers 46%; o228.5 46% |
| BOS @ SAC | Sun 22 Nov 14:00 | 115.0–104.6 | BOS 77% | 1.31 / 4.26 | SAC +10.5 | 219.5 | SAC +12.5 covers 56%; o216.5 56% |

### POR @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.9–111.4 | POR 40% | 2.47 / 1.68 | NYK -3.5 | 219.5 | NYK -2.5 covers 53%; o215.5 58% |
| Expected (weighted by chance each plays) | 108.3–113.0 | POR 37% | 2.70 / 1.59 | NYK -4.5 | 221.5 | NYK -2.5 covers 57%; o215.5 62% |
| if Karl-Anthony Towns plays | 106.8–114.5 | POR 29% | 3.46 / 1.41 | NYK -7.5 | 221.5 | NYK -2.5 covers 65%; o215.5 62% |
| if Deni Avdija plays | 109.4–111.6 | POR 44% | 2.29 / 1.78 | NYK -2.5 | 220.5 | NYK -2.5 covers 50%; o215.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Karl-Anthony Towns (NYK) | Questionable | 55% | 35.6 | 24.7 | 13.7 | 4.6 | 2.0 | 1.2 | 0.8 | 3.2 | 43.0 | full tables below |
| Deni Avdija (POR) | Questionable | 55% | 33.5 | 22.0 | 6.2 | 5.5 | 1.8 | 0.8 | 0.5 | 3.4 | 33.7 | full tables below |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Toumani Camara | 99% | 34.2<br><sub>38,36,26,33,37</sub> | 13.8<br><sub>14,14,3,10,18</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>5,2,0,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,1,0,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,0,2,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.6 | 1.5 | 20.2 |
| Damian Lillard | 99% | 33.6<br><sub>32,33,24,31,35</sub> | 21.8<br><sub>18,29,9,25,33</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,2,2,3,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>3,6,4,5,0</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>2,6,2,5,5</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 2.7 | 30.1 |
| Jrue Holiday | 99% | 31.9<br><sub>30,27,25,31,31</sub> | 16.4<br><sub>19,6,10,23,22</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>3,5,4,5,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.1<br><sub>5,5,3,6,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>5,0,2,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 2.5 | 25.7 |
| Sidy Cissoko | 98% | 30.2<br><sub>29,26,28,32,31</sub> | 9.1<br><sub>19,3,5,6,13</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>2,4,4,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,1,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.4 | 1.2 | 15.2 |
| Scoot Henderson | 99% | 29.4<br><sub>19,23,23,21,35</sub> | 13.8<br><sub>5,11,10,9,27</sub> |  | 2.7<br><sub>2,0,1,1,7</sub> |  | 2.8<br><sub>2,1,0,1,3</sub> |  | 1.8<br><sub>1,2,0,0,5</sub> |  | 0.8 | 0.3 | 2.6 | 19.3 |
| Donovan Clingan | 99% | 28.3<br><sub>30,27,22,32,26</sub> | 11.9<br><sub>5,13,10,12,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>12,11,10,12,13</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>2,2,1,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.5 | 1.7 | 1.5 | 24.6 |
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
| Jalen Brunson | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 31.8<br><sub>27,33,28,31,21</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>3,1,1,5,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.4<br><sub>5,11,9,5,7</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.2 | 3.0 | 41.6 |
| Mikal Bridges | 99% | 33.1<br><sub>17,29,32,30,31</sub> | 14.1<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>1,3,7,5,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,3,3,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.6 | 1.5 | 21.2 |
| Josh Hart | 98% | 32.9<br><sub>26,23,26,31,28</sub> | 11.4<br><sub>6,0,0,5,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>4,5,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,4,2,2,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.3 | 2.0 | 23.1 |
| Landry Shamet | 99% | 31.5<br><sub>29,21,30,24,30</sub> | 13.2<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,3,2,1,1</sub> |  | 1.8<br><sub>4,1,0,1,2</sub> |  | 2.0<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.2 | 17.3 |
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
| Jalen Brunson (NYK) | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 29.4<br><sub>27,33,28,31,21</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,1,1,5,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>5,11,9,5,7</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.2 | 2.8 | 39.1 |
| Karl-Anthony Towns (NYK) | 100% | 35.6<br><sub>34,34,43,36,33</sub> | 24.7<br><sub>21,23,28,16,22</sub> | 20.5 · – | 13.7<br><sub>11,15,17,16,12</sub> | 12.5 | 4.6<br><sub>8,5,3,8,4</sub> | 3.5 | 2.0<br><sub>2,3,3,1,2</sub> | 1.5 | 1.2 | 0.8 | 3.2 | 43.0 |
| Josh Hart (NYK) | 98% | 32.4<br><sub>26,23,26,31,28</sub> | 9.9<br><sub>6,0,0,5,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>4,5,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,4,2,2,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.3 | 1.7 | 20.9 |
| Mikal Bridges (NYK) | 99% | 32.0<br><sub>17,29,32,30,31</sub> | 12.0<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>1,3,7,5,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>2,3,3,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.6 | 1.3 | 18.5 |
| Landry Shamet (NYK) | 99% | 29.7<br><sub>29,21,30,24,30</sub> | 10.9<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,3,2,1,1</sub> |  | 1.6<br><sub>4,1,0,1,2</sub> |  | 1.8<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.1 | 14.7 |
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
| Toumani Camara (POR) | 99% | 34.1<br><sub>38,36,26,33,37</sub> | 13.7<br><sub>14,14,3,10,18</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>5,2,0,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,1,0,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,0,2,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.6 | 1.5 | 20.0 |
| Damian Lillard (POR) | 99% | 33.5<br><sub>32,33,24,31,35</sub> | 21.6<br><sub>18,29,9,25,33</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,2,2,3,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>3,6,4,5,0</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.1<br><sub>2,6,2,5,5</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 2.7 | 29.9 |
| Jrue Holiday (POR) | 99% | 31.9<br><sub>30,27,25,31,31</sub> | 16.3<br><sub>19,6,10,23,22</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>3,5,4,5,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.1<br><sub>5,5,3,6,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>5,0,2,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 2.5 | 25.6 |
| Sidy Cissoko (POR) | 98% | 30.2<br><sub>29,26,28,32,31</sub> | 9.1<br><sub>19,3,5,6,13</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>2,4,4,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,1,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.4 | 1.3 | 15.1 |
| Scoot Henderson (POR) | 99% | 29.4<br><sub>19,23,23,21,35</sub> | 13.8<br><sub>5,11,10,9,27</sub> |  | 2.7<br><sub>2,0,1,1,7</sub> |  | 2.8<br><sub>2,1,0,1,3</sub> |  | 1.8<br><sub>1,2,0,0,5</sub> |  | 0.8 | 0.3 | 2.6 | 19.3 |
| Donovan Clingan (POR) | 99% | 28.3<br><sub>30,27,22,32,26</sub> | 11.7<br><sub>5,13,10,12,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>12,11,10,12,13</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>2,2,1,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.6 | 1.7 | 1.5 | 24.5 |
| Robert Williams III (POR) | 98% | 17.3<br><sub>17,17,15,16,-</sub> | 6.0<br><sub>10,2,2,6,-</sub> |  | 6.2<br><sub>7,7,5,8,-</sub> |  | 1.2<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 1.1 | 0.8 | 13.4 |
| Jayson Kent (POR) | 80% | 17.2<br><sub>-,11,11,27,17</sub> | 5.8<br><sub>-,3,8,8,2</sub> |  | 1.8<br><sub>-,1,0,3,1</sub> |  | 0.7<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,1,2,2,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.3 |
| Branden Carlson (POR) | 88% | 12.6<br><sub>10,8,14,14,10</sub> | 3.6<br><sub>0,5,5,6,0</sub> |  | 2.7<br><sub>2,3,6,1,1</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 6.7 |
| Yang Hansen (POR) | 58% | 11.4<br><sub>-,-,7,-,12</sub> | 3.8<br><sub>-,-,0,-,2</sub> |  | 2.5<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,3,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.8 | 7.1 |
| John Tonje (POR) | 52% | 11.4<br><sub>-,-,7,-,6</sub> | 3.9<br><sub>-,-,7,-,0</sub> |  | 2.6<br><sub>-,-,4,-,3</sub> |  | 0.9<br><sub>-,-,3,-,0</sub> |  | 0.5<br><sub>-,-,1,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 7.4 |
| Micah Potter (POR) | 52% | 9.3<br><sub>-,-,7,1,-</sub> | 3.9<br><sub>-,-,2,0,-</sub> |  | 2.4<br><sub>-,-,4,0,-</sub> |  | 0.5<br><sub>-,-,1,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.8 |

</details>

<details><summary>if Deni Avdija plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 31.8<br><sub>27,33,28,31,21</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,1,1,5,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.4<br><sub>5,11,9,5,7</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.2 | 3.0 | 41.6 |
| Mikal Bridges (NYK) | 99% | 33.1<br><sub>17,29,32,30,31</sub> | 14.1<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>1,3,7,5,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,3,3,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.6 | 1.5 | 21.2 |
| Josh Hart (NYK) | 98% | 32.9<br><sub>26,23,26,31,28</sub> | 11.5<br><sub>6,0,0,5,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>4,5,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,4,2,2,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.3 | 2.0 | 23.2 |
| Landry Shamet (NYK) | 99% | 31.4<br><sub>29,21,30,24,30</sub> | 13.2<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,3,2,1,1</sub> |  | 1.8<br><sub>4,1,0,1,2</sub> |  | 2.0<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.2 | 17.3 |
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
| Deni Avdija (POR) | 100% | 33.5<br><sub>35,35,30,-,-</sub> | 22.0<br><sub>28,34,27,-,-</sub> | 22.5 · – | 6.2<br><sub>3,6,8,-,-</sub> | 6.5 | 5.5<br><sub>6,4,4,-,-</sub> | 5.5 | 1.8<br><sub>4,3,3,-,-</sub> | 1.5 | 0.8 | 0.5 | 3.4 | 33.7 |
| Toumani Camara (POR) | 99% | 31.7<br><sub>38,36,26,33,37</sub> | 11.6<br><sub>14,14,3,10,18</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>5,2,0,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,1,0,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,2,0,2,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.5 | 1.2 | 17.4 |
| Damian Lillard (POR) | 99% | 31.3<br><sub>32,33,24,31,35</sub> | 18.6<br><sub>18,29,9,25,33</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,2,2,3,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>3,6,4,5,0</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>2,6,2,5,5</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 2.2 | 26.0 |
| Jrue Holiday (POR) | 99% | 28.3<br><sub>30,27,25,31,31</sub> | 13.4<br><sub>19,6,10,23,22</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,5,4,5,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>5,5,3,6,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>5,0,2,5,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 2.0 | 21.2 |
| Donovan Clingan (POR) | 99% | 26.2<br><sub>30,27,22,32,26</sub> | 10.3<br><sub>5,13,10,12,7</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 9.6<br><sub>12,11,10,12,13</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>2,2,1,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.5 | 1.6 | 1.2 | 21.7 |
| Sidy Cissoko (POR) | 98% | 25.4<br><sub>29,26,28,32,31</sub> | 6.9<br><sub>19,3,5,6,13</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>2,4,4,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>0,1,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.4 | 1.0 | 11.9 |
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
| Confirmed players only | 116.7–117.0 | LAC 49% | 2.04 / 1.97 | DAL +0.5 | 233.5 | DAL -4.5 covers 39%; o230.5 56% |
| Expected (weighted by chance each plays) | 116.6–117.2 | LAC 48% | 2.10 / 1.91 | DAL -1.5 | 233.5 | DAL -4.5 covers 40%; o230.5 58% |
| if Walter Clayton Jr. plays | 116.3–117.3 | LAC 47% | 2.12 / 1.89 | DAL -1.5 | 233.5 | DAL -4.5 covers 40%; o230.5 56% |
| if P.J. Washington plays | 116.3–117.3 | LAC 47% | 2.13 / 1.89 | DAL -1.5 | 233.5 | DAL -4.5 covers 41%; o230.5 56% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walter Clayton Jr. (DAL) | Questionable | 55% | 21.1 | 7.8 | 3.1 | 3.8 | 1.1 | 0.7 | 0.2 | 1.7 | 14.7 | full tables below |
| Jett Howard (DAL) | Questionable | 55% | 8.0 | 2.9 | 0.9 | 0.6 | 0.3 | 0.2 | 0.1 | 0.3 | 4.4 | small |
| P.J. Washington (DAL) | Doubtful | 20% | 31.5 | 14.1 | 6.7 | 1.7 | 1.8 | 0.9 | 0.9 | 1.6 | 22.5 | full tables below |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.8<br><sub>13,24,27,20,23</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>5,4,6,3,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>6,7,7,7,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,3,3,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.2 | 3.4 | 32.8 |
| Rui Hachimura | 98% | 28.5<br><sub>23,32,22,27,32</sub> | 14.1<br><sub>13,7,4,20,17</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>5,11,2,5,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,1,0,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 1.2 | 20.2 |
| Derrick Jones Jr. | 98% | 27.1<br><sub>24,29,26,28,27</sub> | 10.4<br><sub>11,14,13,5,8</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,5,4,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1<br><sub>2,4,3,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.9 | 0.9 | 15.6 |
| Brook Lopez | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>4,7,5,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,4,8,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6<br><sub>1,3,1,4,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 1.3 | 1.1 | 20.3 |
| Max Strus | 98% | 24.3<br><sub>22,23,25,21,32</sub> | 9.6<br><sub>12,3,14,3,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,2,3,2,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>3,3,4,1,4</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.6<br><sub>2,0,4,1,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.1 | 16.5 |
| Kris Dunn | 98% | 23.0<br><sub>19,20,18,26,20</sub> | 6.5<br><sub>3,2,7,2,6</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,3,3,5,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>3,6,1,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.6 | 0.3 | 1.1 | 13.2 |
| Keaton Wagler | 98% | 20.5<br><sub>23,18,28,18,17</sub> | 10.8<br><sub>11,14,12,15,7</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>0,2,4,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,1,5,0,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.2 | 1.8 | 16.4 |
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
| Cooper Flagg | 98% | 36.6<br><sub>39,27,38,27,34</sub> | 25.7<br><sub>43,12,18,17,33</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>10,7,8,3,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.6<br><sub>6,3,5,4,9</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.8 | 3.1 | 39.6 |
| Kyrie Irving | 98% | 36.0<br><sub>38,27,37,-,29</sub> | 25.1<br><sub>35,10,34,-,17</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>0,3,6,-,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 5.2<br><sub>4,4,5,-,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>7,2,7,-,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.5 | 2.4 | 34.8 |
| Naji Marshall | 96% | 30.6<br><sub>25,23,30,23,27</sub> | 15.3<br><sub>6,13,12,13,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>5,1,3,2,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.1<br><sub>2,4,5,2,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,1,0,3,2</sub> |  | 1.3 | 0.1 | 2.0 | 23.8 |
| Caleb Martin | 98% | 25.5<br><sub>19,21,33,34,20</sub> | 7.1<br><sub>0,7,15,12,8</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>3,2,8,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>5,5,3,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>0,1,1,4,2</sub> |  | 1.0 | 0.4 | 1.0 | 13.3 |
| Daniel Gafford | 99% | 25.3<br><sub>20,16,17,19,24</sub> | 11.0<br><sub>8,3,10,3,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>2,3,3,4,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>3,1,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.6 | 1.2 | 19.9 |
| Zaccharie Risacher | 98% | 24.3<br><sub>15,25,14,27,18</sub> | 8.7<br><sub>4,22,5,18,3</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,6,2,5,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>0,3,0,0,0</sub> |  | 1.1<br><sub>0,4,1,1,1</sub> |  | 0.9 | 0.8 | 1.1 | 14.5 |
| Morez Johnson Jr. | 98% | 19.5<br><sub>-,13,15,26,15</sub> | 7.2<br><sub>-,0,4,2,3</sub> |  | 3.8<br><sub>-,2,2,6,1</sub> |  | 1.7<br><sub>-,0,0,4,1</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.1 | 12.6 |
| Max Christie | 98% | 18.9<br><sub>5,7,-,-,8</sub> | 7.0<br><sub>0,3,-,-,5</sub> |  | 2.3<br><sub>2,2,-,-,1</sub> |  | 1.3<br><sub>0,0,-,-,2</sub> |  | 1.1<br><sub>0,1,-,-,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.6 |
| Santi Aldama | 98% | 16.6<br><sub>19,10,16,-,6</sub> | 7.8<br><sub>10,3,7,-,0</sub> |  | 3.9<br><sub>4,1,2,-,0</sub> |  | 1.3<br><sub>1,1,1,-,0</sub> |  | 0.9<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.4 | 0.9 | 13.0 |
| Marcus Sasser | 67% | 15.1<br><sub>-,9,-,18,4</sub> | 5.2<br><sub>-,3,-,5,0</sub> |  | 1.4<br><sub>-,1,-,1,2</sub> |  | 1.8<br><sub>-,0,-,2,1</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 8.4 |
| Moussa Cisse | 67% | 8.9<br><sub>-,8,-,4,4</sub> | 3.1<br><sub>-,0,-,1,0</sub> |  | 3.3<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.6 | 0.4 | 6.6 |

</details>

<details><summary>if P.J. Washington plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 35.1<br><sub>39,27,38,27,34</sub> | 24.9<br><sub>43,12,18,17,33</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>10,7,8,3,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.4<br><sub>6,3,5,4,9</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.8 | 3.0 | 38.3 |
| Kyrie Irving (DAL) | 98% | 34.6<br><sub>38,27,37,-,29</sub> | 23.3<br><sub>35,10,34,-,17</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>0,3,6,-,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 4.8<br><sub>4,4,5,-,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>7,2,7,-,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.5 | 2.4 | 32.4 |
| P.J. Washington (DAL) | 100% | 31.5<br><sub>35,16,26,25,25</sub> | 14.1<br><sub>13,10,10,8,21</sub> |  | 6.7<br><sub>9,3,4,5,5</sub> |  | 1.7<br><sub>1,0,1,4,2</sub> |  | 1.8<br><sub>2,1,2,0,5</sub> |  | 0.9 | 0.9 | 1.6 | 22.5 |
| Naji Marshall (DAL) | 96% | 26.7<br><sub>25,23,30,23,27</sub> | 13.3<br><sub>6,13,12,13,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>5,1,3,2,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.7<br><sub>2,4,5,2,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.9<br><sub>0,1,0,3,2</sub> |  | 1.1 | 0.1 | 1.8 | 20.8 |
| Daniel Gafford (DAL) | 99% | 21.6<br><sub>20,16,17,19,24</sub> | 9.6<br><sub>8,3,10,3,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>2,3,3,4,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>3,1,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 1.4 | 1.1 | 17.2 |
| Caleb Martin (DAL) | 98% | 21.3<br><sub>19,21,33,34,20</sub> | 6.0<br><sub>0,7,15,12,8</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,2,8,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>5,5,3,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>0,1,1,4,2</sub> |  | 0.8 | 0.3 | 0.8 | 11.3 |
| Zaccharie Risacher (DAL) | 98% | 19.8<br><sub>15,25,14,27,18</sub> | 7.1<br><sub>4,22,5,18,3</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>2,6,2,5,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,3,0,0,0</sub> |  | 0.8<br><sub>0,4,1,1,1</sub> |  | 0.7 | 0.7 | 0.9 | 11.9 |
| Morez Johnson Jr. (DAL) | 98% | 15.2<br><sub>-,13,15,26,15</sub> | 5.5<br><sub>-,0,4,2,3</sub> |  | 3.0<br><sub>-,2,2,6,1</sub> |  | 1.4<br><sub>-,0,0,4,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.9 |
| Max Christie (DAL) | 98% | 14.2<br><sub>5,7,-,-,8</sub> | 5.2<br><sub>0,3,-,-,5</sub> |  | 1.7<br><sub>2,2,-,-,1</sub> |  | 1.0<br><sub>0,0,-,-,2</sub> |  | 0.7<br><sub>0,1,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 7.9 |
| Santi Aldama (DAL) | 98% | 12.2<br><sub>19,10,16,-,6</sub> | 5.9<br><sub>10,3,7,-,0</sub> |  | 2.9<br><sub>4,1,2,-,0</sub> |  | 1.0<br><sub>1,1,1,-,0</sub> |  | 0.6<br><sub>1,1,2,-,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.8 |
| Marcus Sasser (DAL) | 67% | 11.6<br><sub>-,9,-,18,4</sub> | 4.0<br><sub>-,3,-,5,0</sub> |  | 1.0<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.5 |
| Moussa Cisse (DAL) | 67% | 6.9<br><sub>-,8,-,4,4</sub> | 2.5<br><sub>-,0,-,1,0</sub> |  | 2.5<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.2 |
| Darius Garland (LAC) | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.7<br><sub>13,24,27,20,23</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>5,4,6,3,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>6,7,7,7,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,3,3,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.2 | 3.4 | 32.7 |
| Rui Hachimura (LAC) | 98% | 28.5<br><sub>23,32,22,27,32</sub> | 14.0<br><sub>13,7,4,20,17</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>5,11,2,5,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,1,0,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 1.2 | 20.1 |
| Derrick Jones Jr. (LAC) | 98% | 27.1<br><sub>24,29,26,28,27</sub> | 10.3<br><sub>11,14,13,5,8</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,5,4,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1<br><sub>2,4,3,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.9 | 0.9 | 15.6 |
| Brook Lopez (LAC) | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>4,7,5,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,4,8,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6<br><sub>1,3,1,4,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 1.2 | 1.2 | 20.3 |
| Max Strus (LAC) | 98% | 24.2<br><sub>22,23,25,21,32</sub> | 9.5<br><sub>12,3,14,3,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,2,3,2,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>3,3,4,1,4</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.6<br><sub>2,0,4,1,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.0 | 16.4 |
| Kris Dunn (LAC) | 98% | 22.8<br><sub>19,20,18,26,20</sub> | 6.5<br><sub>3,2,7,2,6</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,3,3,5,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>3,6,1,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.2 |
| Keaton Wagler (LAC) | 98% | 20.4<br><sub>23,18,28,18,17</sub> | 10.8<br><sub>11,14,12,15,7</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>0,2,4,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,1,5,0,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.2 | 1.8 | 16.4 |
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
| Cooper Flagg (DAL) | 98% | 35.9<br><sub>39,27,38,27,34</sub> | 25.7<br><sub>43,12,18,17,33</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>10,7,8,3,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.3<br><sub>6,3,5,4,9</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.8 | 3.0 | 39.1 |
| Kyrie Irving (DAL) | 98% | 35.0<br><sub>38,27,37,-,29</sub> | 23.7<br><sub>35,10,34,-,17</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>0,3,6,-,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 4.7<br><sub>4,4,5,-,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>7,2,7,-,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.5 | 2.3 | 32.9 |
| Naji Marshall (DAL) | 96% | 28.2<br><sub>25,23,30,23,27</sub> | 13.7<br><sub>6,13,12,13,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>5,1,3,2,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.7<br><sub>2,4,5,2,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.9<br><sub>0,1,0,3,2</sub> |  | 1.1 | 0.1 | 1.9 | 21.4 |
| Daniel Gafford (DAL) | 99% | 23.3<br><sub>20,16,17,19,24</sub> | 10.4<br><sub>8,3,10,3,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>2,3,3,4,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>3,1,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 1.5 | 1.1 | 18.4 |
| Caleb Martin (DAL) | 98% | 23.2<br><sub>19,21,33,34,20</sub> | 6.5<br><sub>0,7,15,12,8</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>3,2,8,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>5,5,3,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>0,1,1,4,2</sub> |  | 0.9 | 0.3 | 0.9 | 12.1 |
| Zaccharie Risacher (DAL) | 98% | 22.0<br><sub>15,25,14,27,18</sub> | 8.1<br><sub>4,22,5,18,3</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>2,6,2,5,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,3,0,0,0</sub> |  | 0.9<br><sub>0,4,1,1,1</sub> |  | 0.8 | 0.7 | 1.0 | 13.3 |
| Walter Clayton Jr. (DAL) | 100% | 21.1<br><sub>25,22,13,23,27</sub> | 7.8<br><sub>6,5,2,13,8</sub> |  | 3.1<br><sub>6,1,2,4,2</sub> |  | 3.8<br><sub>4,4,2,3,7</sub> |  | 1.1<br><sub>1,0,0,3,2</sub> |  | 0.7 | 0.2 | 1.7 | 14.7 |
| Morez Johnson Jr. (DAL) | 98% | 17.3<br><sub>-,13,15,26,15</sub> | 6.3<br><sub>-,0,4,2,3</sub> |  | 3.4<br><sub>-,2,2,6,1</sub> |  | 1.5<br><sub>-,0,0,4,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 11.2 |
| Max Christie (DAL) | 98% | 15.6<br><sub>5,7,-,-,8</sub> | 5.7<br><sub>0,3,-,-,5</sub> |  | 1.9<br><sub>2,2,-,-,1</sub> |  | 1.0<br><sub>0,0,-,-,2</sub> |  | 0.8<br><sub>0,1,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 8.6 |
| Santi Aldama (DAL) | 98% | 14.5<br><sub>19,10,16,-,6</sub> | 7.0<br><sub>10,3,7,-,0</sub> |  | 3.4<br><sub>4,1,2,-,0</sub> |  | 1.1<br><sub>1,1,1,-,0</sub> |  | 0.7<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.3 | 0.7 | 11.5 |
| Marcus Sasser (DAL) | 67% | 12.1<br><sub>-,9,-,18,4</sub> | 4.2<br><sub>-,3,-,5,0</sub> |  | 1.1<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.7 |
| Moussa Cisse (DAL) | 67% | 7.4<br><sub>-,8,-,4,4</sub> | 2.6<br><sub>-,0,-,1,0</sub> |  | 2.7<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.5 |
| Darius Garland (LAC) | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.7<br><sub>13,24,27,20,23</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>5,4,6,3,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>6,7,7,7,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,3,3,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.2 | 3.4 | 32.7 |
| Rui Hachimura (LAC) | 98% | 28.5<br><sub>23,32,22,27,32</sub> | 14.1<br><sub>13,7,4,20,17</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>5,11,2,5,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,1,0,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 1.2 | 20.2 |
| Derrick Jones Jr. (LAC) | 98% | 27.0<br><sub>24,29,26,28,27</sub> | 10.3<br><sub>11,14,13,5,8</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,4,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1<br><sub>2,4,3,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.9 | 0.9 | 15.5 |
| Brook Lopez (LAC) | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>4,7,5,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,4,8,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6<br><sub>1,3,1,4,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 1.3 | 1.1 | 20.3 |
| Max Strus (LAC) | 98% | 24.2<br><sub>22,23,25,21,32</sub> | 9.5<br><sub>12,3,14,3,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,2,3,2,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>3,3,4,1,4</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.6<br><sub>2,0,4,1,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.0 | 16.4 |
| Kris Dunn (LAC) | 98% | 22.9<br><sub>19,20,18,26,20</sub> | 6.5<br><sub>3,2,7,2,6</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,3,3,5,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>3,6,1,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.2 |
| Keaton Wagler (LAC) | 98% | 20.5<br><sub>23,18,28,18,17</sub> | 10.7<br><sub>11,14,12,15,7</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>0,2,4,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,1,5,0,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.2 | 1.8 | 16.4 |
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

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.5–119.1 | MEM 29% | 3.43 / 1.41 | MIN -7.5 | 230.5 | MIN -6.5 covers 53%; o228.5 54% |
| Expected (weighted by chance each plays) | 111.5–119.1 | MEM 29% | 3.46 / 1.41 | MIN -7.5 | 230.5 | MIN -6.5 covers 53%; o228.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaiah Evans (MIN) | Questionable | 55% | 5.8 | 4.4 | 1.2 | 0.4 | 0.3 | 0.2 | 0.1 | 0.3 | 6.0 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 32.5<br><sub>30,33,27,33,25</sub> | 16.3<br><sub>14,23,18,20,19</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>7,12,8,3,4</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>6,4,6,5,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>0,4,2,4,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.6 | 2.1 | 28.1 |
| Ty Jerome | 98% | 30.4<br><sub>29,-,-,-,-</sub> | 23.0<br><sub>17,-,-,-,-</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,-,-,-,-</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>9,-,-,-,-</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,-,-,-,-</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 2.7 | 32.9 |
| Jaylen Wells | 99% | 30.1<br><sub>27,25,27,26,24</sub> | 11.7<br><sub>11,5,8,5,22</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,2,4,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 1.1 | 16.9 |
| Cam Spencer | 98% | 29.1<br><sub>24,34,32,29,27</sub> | 13.2<br><sub>14,17,12,26,9</sub> | 9.5 · –<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>2,1,6,1,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 7.2<br><sub>5,8,9,7,11</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>3,3,1,5,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.2 | 1.7 | 23.9 |
| Taylor Hendricks | 88% | 24.0<br><sub>19,29,19,21,20</sub> | 10.5<br><sub>10,22,9,18,11</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>12,5,3,6,1</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,4,0,2,1</sub> |  | 1.2<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.6 | 1.1 | 16.8 |
| Zach Edey | 88% | 23.9<br><sub>-,-,21,21,-</sub> | 10.1<br><sub>-,-,23,11,-</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 8.8<br><sub>-,-,10,2,-</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>-,-,1,1,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.5 | 1.6 | 1.7 | 20.2 |
| Olivier-Maxence Prosper | 86% | 21.7<br><sub>2,20,16,16,24</sub> | 10.8<br><sub>6,11,12,5,16</sub> |  | 4.0<br><sub>1,4,0,2,5</sub> |  | 1.2<br><sub>0,0,1,0,1</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.8 | 0.3 | 1.0 | 16.0 |
| Isaiah Stewart | 98% | 20.3<br><sub>20,15,-,-,18</sub> | 9.2<br><sub>12,11,-,-,8</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>5,3,-,-,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>0,3,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.4 | 1.3 | 1.1 | 14.6 |
| Jahmai Mashack | 71% | 18.3<br><sub>-,2,2,13,26</sub> | 4.9<br><sub>-,0,0,3,0</sub> |  | 2.4<br><sub>-,0,0,2,3</sub> |  | 2.4<br><sub>-,0,1,2,4</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.8 | 0.4 | 1.1 | 9.7 |
| Kris Murray | 88% | 16.1<br><sub>1,19,6,6,4</sub> | 3.1<br><sub>0,3,0,5,0</sub> |  | 2.4<br><sub>1,2,1,0,1</sub> |  | 1.0<br><sub>0,3,0,0,0</sub> |  | 0.2<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 6.5 |
| Quinten Post | 96% | 14.2<br><sub>-,-,9,6,10</sub> | 5.2<br><sub>-,-,5,3,5</sub> |  | 2.8<br><sub>-,-,3,2,1</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.4 | 0.3 | 0.7 | 8.4 |
| Karim Lopez | 58% | 11.4<br><sub>-,2,1,-,4</sub> | 3.4<br><sub>-,0,0,-,3</sub> |  | 2.1<br><sub>-,2,0,-,0</sub> |  | 0.6<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,1</sub> |  | 0.6 | 0.5 | 0.5 | 6.1 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 36.1<br><sub>25,37,31,37,39</sub> | 18.0<br><sub>16,18,13,22,17</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>9,5,6,5,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>3,6,3,4,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,2,0,2,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 1.2 | 1.9 | 27.3 |
| Ayo Dosunmu | 99% | 33.9<br><sub>27,33,30,39,32</sub> | 19.4<br><sub>18,24,8,30,6</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,5,5,4,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>1,0,2,5,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>2,0,2,7,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.5 | 2.0 | 28.2 |
| Jonathan Kuminga | 84% | 31.9<br><sub>24,35,29,-,35</sub> | 14.7<br><sub>14,11,13,-,23</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>8,3,9,-,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>5,3,1,-,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,0,1,-,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.8 | 1.7 | 23.4 |
| LaMelo Ball | 99% | 31.4<br><sub>25,30,24,31,35</sub> | 21.5<br><sub>22,19,6,18,15</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>3,8,5,9,8</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>9,6,0,2,8</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 3.6<br><sub>6,4,2,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.7 | 0.3 | 3.0 | 33.1 |
| Rudy Gobert | 99% | 31.2<br><sub>23,27,32,22,35</sub> | 10.1<br><sub>9,1,18,0,9</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 11.6<br><sub>6,10,15,4,7</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,4,3,2,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.8 | 1.5 | 23.4 |
| Terrence Shannon Jr. | 98% | 24.7<br><sub>21,22,35,24,21</sub> | 13.8<br><sub>6,14,34,12,10</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>2,6,3,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>4,0,6,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,0,3,1,0</sub> |  | 0.7 | 0.2 | 1.3 | 19.6 |
| Trey Lyles | 98% | 20.4<br><sub>15,19,19,31,16</sub> | 6.7<br><sub>2,5,9,8,8</sub> |  | 4.6<br><sub>0,1,3,7,6</sub> |  | 1.2<br><sub>0,2,1,4,1</sub> |  | 0.9<br><sub>0,0,2,2,2</sub> |  | 0.6 | 0.4 | 0.6 | 12.4 |
| Joan Beringer | 98% | 16.4<br><sub>22,13,16,26,13</sub> | 6.2<br><sub>13,2,0,3,5</sub> |  | 5.9<br><sub>9,5,4,13,3</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.5 | 0.6 | 12.6 |
| Bones Hyland | 98% | 15.7<br><sub>23,21,13,17,15</sub> | 9.3<br><sub>24,12,5,13,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,1,1,2,1</sub> |  | 2.5<br><sub>8,2,5,1,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>5,3,0,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.2 | 1.0 | 13.6 |
| Cody Williams | 58% | 7.9<br><sub>7,-,4,13,-</sub> | 0.2<br><sub>0,-,0,0,-</sub> |  | 1.2<br><sub>1,-,1,1,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 1.8 |
| Zyon Pullin | 38% | 6.5<br><sub>-,-,4,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Johni Broome | 3% | 6.4 | 2.4 |  | 1.4 |  | 0.5 |  | 0.1 |  | 0.3 | 0.2 | 0.3 | 4.2 |

</details>


### NOP @ SAS
Out: Dylan Harper (SAS), Tobias Harris (SAS), Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 34.6<br><sub>35,41,33,42,37</sub> | 16.4<br><sub>30,16,23,10,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>10,6,6,8,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>0,4,3,6,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>6,2,5,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.2 | 1.2 | 24.6 |
| Zion Williamson | 98% | 33.7<br><sub>33,31,25,32,37</sub> | 20.6<br><sub>22,24,16,24,22</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>5,6,6,7,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,2,2,1,7</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>0,2,0,0,0</sub> |  | 1.2 | 0.6 | 2.2 | 30.2 |
| Jeremiah Fears | 99% | 32.8<br><sub>34,33,29,31,38</sub> | 17.1<br><sub>18,13,19,16,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>5,4,10,5,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>7,7,10,4,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,1,1,2,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.5 | 2.8 | 27.8 |
| Herbert Jones | 98% | 30.3<br><sub>32,27,24,32,33</sub> | 10.0<br><sub>8,10,8,9,14</sub> |  | 3.3<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>3,1,3,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>0,2,2,3,4</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.5 | 1.4 | 16.0 |
| Derik Queen | 99% | 24.8<br><sub>23,25,21,19,18</sub> | 12.1<br><sub>10,10,17,9,11</sub> |  | 6.8<br><sub>6,5,10,5,7</sub> |  | 3.0<br><sub>2,4,0,0,3</sub> |  | 0.7<br><sub>0,2,4,0,0</sub> |  | 1.0 | 0.8 | 2.1 | 21.9 |
| Jordan Poole | 88% | 24.3<br><sub>21,24,31,30,13</sub> | 11.3<br><sub>13,14,11,22,6</sub> |  | 2.3<br><sub>2,2,2,1,0</sub> |  | 3.6<br><sub>5,5,5,5,1</sub> |  | 1.8<br><sub>1,1,1,3,2</sub> |  | 0.7 | 0.3 | 1.6 | 17.2 |
| Yves Missi | 98% | 22.9<br><sub>-,22,23,17,23</sub> | 6.8<br><sub>-,3,6,4,4</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>-,8,14,5,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,1,1,2,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 1.3 | 1.0 | 15.2 |
| Karlo Matkovic | 98% | 20.4<br><sub>19,14,20,10,8</sub> | 7.4<br><sub>1,5,3,0,0</sub> |  | 4.3<br><sub>3,3,2,2,2</sub> |  | 1.0<br><sub>0,1,0,0,0</sub> |  | 0.9<br><sub>0,1,0,0,0</sub> |  | 0.6 | 0.7 | 0.8 | 12.7 |
| DeAndre Jordan | 48% | 14.0<br><sub>17,-,-,10,-</sub> | 4.2<br><sub>6,-,-,8,-</sub> |  | 4.9<br><sub>8,-,-,2,-</sub> |  | 0.8<br><sub>1,-,-,1,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.5 | 0.6 | 9.9 |
| Jaron Pierre Jr. | 96% | 13.9<br><sub>4,23,19,17,4</sub> | 5.3<br><sub>0,13,10,7,3</sub> |  | 1.9<br><sub>0,2,4,1,2</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 0.7<br><sub>0,2,2,1,1</sub> |  | 0.5 | 0.2 | 0.8 | 8.1 |
| AJ Johnson | 52% | 9.5<br><sub>4,-,6,-,-</sub> | 3.2<br><sub>1,-,0,-,-</sub> |  | 1.3<br><sub>0,-,0,-,-</sub> |  | 0.8<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.2 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 98% | 33.1<br><sub>-,23,32,36,32</sub> | 14.3<br><sub>-,7,6,12,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>-,2,6,5,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.3<br><sub>-,2,1,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>-,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.5 | 1.1 | 22.0 |
| Victor Wembanyama | 99% | 32.5<br><sub>32,21,35,34,33</sub> | 30.9<br><sub>32,12,26,25,32</sub> | 29.5 · –<br><sub>o 49% · u 51%</sub> | 13.3<br><sub>9,12,10,18,11</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>1,6,6,4,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,0,4,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 4.3 | 2.4 | 48.1 |
| De'Aaron Fox | 99% | 32.1<br><sub>31,17,-,34,32</sub> | 16.5<br><sub>17,7,-,6,10</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>4,5,-,2,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>9,1,-,2,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,0,-,0,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.4 | 2.2 | 27.0 |
| Stephon Castle | 99% | 31.9<br><sub>29,25,35,31,33</sub> | 18.9<br><sub>11,32,20,10,21</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>1,5,4,2,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 7.3<br><sub>3,6,9,7,12</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,5,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 3.0 | 31.3 |
| Julian Champagnie | 99% | 29.0<br><sub>35,23,24,30,29</sub> | 11.6<br><sub>12,7,4,14,20</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>0,8,5,6,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>2,3,1,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>3,1,1,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.6 | 0.8 | 18.6 |
| Keldon Johnson | 99% | 25.6<br><sub>28,25,29,15,27</sub> | 11.3<br><sub>10,18,11,4,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>6,4,10,2,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>4,4,2,1,3</sub> |  | 0.7<br><sub>0,2,1,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 19.3 |
| Luke Kornet | 99% | 16.3<br><sub>14,16,13,14,15</sub> | 4.4<br><sub>7,6,2,2,4</sub> |  | 4.8<br><sub>5,7,2,1,0</sub> |  | 1.4<br><sub>1,2,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.5 | 10.6 |
| Harrison Barnes | 91% | 16.3<br><sub>13,21,14,10,16</sub> | 6.0<br><sub>3,11,0,0,9</sub> |  | 1.9<br><sub>1,1,0,3,2</sub> |  | 1.0<br><sub>0,1,2,4,1</sub> |  | 0.8<br><sub>1,3,0,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 8.9 |
| Jordan McLaughlin | 71% | 14.3<br><sub>2,14,19,-,11</sub> | 4.6<br><sub>4,4,10,-,0</sub> |  | 1.9<br><sub>0,6,1,-,1</sub> |  | 2.5<br><sub>0,2,2,-,5</sub> |  | 0.5<br><sub>0,0,2,-,0</sub> |  | 1.0 | 0.1 | 0.7 | 9.0 |
| Carter Bryant | 93% | 13.1<br><sub>15,19,5,2,13</sub> | 4.9<br><sub>10,8,0,0,3</sub> |  | 2.2<br><sub>1,3,1,0,1</sub> |  | 0.9<br><sub>2,2,0,0,0</sub> |  | 0.7<br><sub>2,2,0,0,1</sub> |  | 0.3 | 0.4 | 0.5 | 8.0 |
| Tarris Reed Jr. | 52% | 8.7<br><sub>2,11,-,-,-</sub> | 3.2<br><sub>0,2,-,-,-</sub> |  | 3.4<br><sub>0,4,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.5 | 7.0 |
| David Jones Garcia | 52% | 6.9<br><sub>2,-,-,-,-</sub> | 2.7<br><sub>0,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.1 |

</details>


### BOS @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Mitchell Robinson (BOS), Jayson Tatum (BOS), Derrick White (BOS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.0–104.6 | BOS 77% | 1.31 / 4.26 | SAC +10.5 | 219.5 | SAC +12.5 covers 56%; o216.5 56% |
| Expected (weighted by chance each plays) | 115.1–104.8 | BOS 76% | 1.31 / 4.20 | SAC +10.5 | 220.5 | SAC +12.5 covers 56%; o216.5 57% |
| if Precious Achiuwa plays | 115.1–105.0 | BOS 76% | 1.32 / 4.12 | SAC +10.5 | 220.5 | SAC +12.5 covers 56%; o216.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa (SAC) | Questionable | 55% | 20.4 | 8.0 | 5.4 | 1.1 | 0.3 | 0.7 | 0.6 | 1.0 | 14.5 | full tables below |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George | 98% | 31.9<br><sub>30,-,25,36,23</sub> | 22.3<br><sub>36,-,7,22,10</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,-,7,8,4</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 4.4<br><sub>1,-,6,3,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.4 | 2.5 | 32.1 |
| Payton Pritchard | 99% | 31.0<br><sub>30,31,19,32,30</sub> | 19.5<br><sub>18,14,10,21,15</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>6,1,1,4,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>5,1,6,5,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.1 | 1.6 | 28.5 |
| Neemias Queta | 98% | 27.2<br><sub>22,31,15,-,27</sub> | 13.0<br><sub>4,11,8,-,17</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 9.7<br><sub>6,13,6,-,10</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>3,3,2,-,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.2 | 1.4 | 25.2 |
| Sam Hauser | 99% | 26.5<br><sub>18,24,11,25,17</sub> | 11.2<br><sub>12,8,8,12,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>5,9,1,1,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.3<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 0.5 | 16.8 |
| Baylor Scheierman | 99% | 24.3<br><sub>18,29,18,11,13</sub> | 8.3<br><sub>5,9,12,0,0</sub> | 10.5 · –<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>3,7,5,1,1</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,3,3,1,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,3,2,0,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.1 | 0.8 | 15.0 |
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
| Darius Acuff Jr. | 98% | 36.8<br><sub>40,35,33,35,36</sub> | 23.2<br><sub>29,17,26,36,18</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 7.7<br><sub>6,6,6,6,12</sub> | 5.5<br><sub>o 59% · u 41%</sub> | 2.6<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.3 | 3.8 | 34.3 |
| De'Andre Hunter | 88% | 33.8<br><sub>34,42,-,35,37</sub> | 14.4<br><sub>15,24,-,7,30</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>4,5,-,1,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,2,-,4,2</sub> |  | 2.1<br><sub>3,2,-,1,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 1.6 | 21.1 |
| Zach LaVine | 88% | 33.6<br><sub>33,36,-,32,39</sub> | 17.7<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.0 | 23.9 |
| Domantas Sabonis | 98% | 32.3<br><sub>24,35,29,24,38</sub> | 13.4<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 12.1<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>5,5,3,8,1</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.3 | 2.3 | 30.6 |
| Keegan Murray | 98% | 31.8<br><sub>24,40,21,31,40</sub> | 12.5<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.7<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.9 | 1.1 | 19.2 |
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
| Paul George (BOS) | 98% | 31.9<br><sub>30,-,25,36,23</sub> | 22.5<br><sub>36,-,7,22,10</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,-,7,8,4</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 4.4<br><sub>1,-,6,3,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.4 | 2.5 | 32.3 |
| Payton Pritchard (BOS) | 99% | 31.1<br><sub>30,31,19,32,30</sub> | 19.4<br><sub>18,14,10,21,15</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>6,1,1,4,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>5,1,6,5,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.1 | 1.6 | 28.5 |
| Neemias Queta (BOS) | 98% | 27.1<br><sub>22,31,15,-,27</sub> | 13.0<br><sub>4,11,8,-,17</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 9.7<br><sub>6,13,6,-,10</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>3,3,2,-,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.2 | 1.4 | 25.1 |
| Sam Hauser (BOS) | 99% | 26.5<br><sub>18,24,11,25,17</sub> | 11.2<br><sub>12,8,8,12,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>5,9,1,1,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.2<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 0.5 | 16.7 |
| Baylor Scheierman (BOS) | 99% | 24.4<br><sub>18,29,18,11,13</sub> | 8.3<br><sub>5,9,12,0,0</sub> | 10.5 · –<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>3,7,5,1,1</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,3,3,1,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,3,2,0,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.1 | 0.9 | 15.0 |
| Jordan Walsh (BOS) | 98% | 22.0<br><sub>19,18,21,17,4</sub> | 7.2<br><sub>8,6,11,6,0</sub> |  | 4.1<br><sub>2,3,1,2,0</sub> |  | 1.2<br><sub>2,0,0,0,0</sub> |  | 0.9<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.3 | 0.7 | 12.5 |
| Hugo Gonzalez (BOS) | 98% | 21.7<br><sub>19,8,18,4,16</sub> | 7.2<br><sub>10,0,9,0,2</sub> |  | 4.4<br><sub>2,1,5,2,6</sub> |  | 1.2<br><sub>2,0,2,0,0</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.9 | 0.4 | 0.8 | 12.8 |
| Devin Carter (BOS) | 91% | 19.8<br><sub>-,-,12,-,-</sub> | 9.4<br><sub>-,-,0,-,-</sub> |  | 3.6<br><sub>-,-,2,-,-</sub> |  | 2.9<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.0 | 0.2 | 1.4 | 15.9 |
| Chris Cenac Jr. (BOS) | 63% | 19.0<br><sub>-,-,7,12,17</sub> | 7.6<br><sub>-,-,6,4,6</sub> |  | 4.7<br><sub>-,-,3,2,6</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.8 | 0.3 | 0.9 | 13.3 |
| Luka Garza (BOS) | 98% | 18.0<br><sub>9,11,14,18,5</sub> | 8.9<br><sub>2,5,2,3,0</sub> |  | 4.3<br><sub>0,1,3,0,1</sub> |  | 2.0<br><sub>2,0,5,4,1</sub> |  | 0.9<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.5 | 0.8 | 15.2 |
| Mike Conley (BOS) | 35% | 14.8<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.2 | 0.7 | 8.0 |
| Ron Harper Jr. (BOS) | 52% | 14.5<br><sub>4,-,12,-,-</sub> | 6.1<br><sub>0,-,10,-,-</sub> |  | 2.1<br><sub>1,-,1,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 9.2 |
| Darius Acuff Jr. (SAC) | 98% | 35.0<br><sub>40,35,33,35,36</sub> | 21.8<br><sub>29,17,26,36,18</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 7.3<br><sub>6,6,6,6,12</sub> | 5.5<br><sub>o 59% · u 41%</sub> | 2.4<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.3 | 3.7 | 32.4 |
| Zach LaVine (SAC) | 88% | 31.8<br><sub>33,36,-,32,39</sub> | 16.6<br><sub>31,12,-,18,19</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,3,-,5,7</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.2 | 2.0 | 22.6 |
| De'Andre Hunter (SAC) | 88% | 31.5<br><sub>34,42,-,35,37</sub> | 13.2<br><sub>15,24,-,7,30</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>4,5,-,1,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,2,-,4,2</sub> |  | 1.9<br><sub>3,2,-,1,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 1.6 | 19.4 |
| Domantas Sabonis (SAC) | 98% | 30.7<br><sub>24,35,29,24,38</sub> | 13.0<br><sub>0,21,11,8,19</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 11.6<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>5,5,3,8,1</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 2.3 | 29.6 |
| Keegan Murray (SAC) | 98% | 29.8<br><sub>24,40,21,31,40</sub> | 11.7<br><sub>11,16,6,12,13</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.5<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.8 | 1.0 | 18.0 |
| Precious Achiuwa (SAC) | 100% | 20.4<br><sub>14,-,-,8,-</sub> | 8.0<br><sub>10,-,-,0,-</sub> |  | 5.4<br><sub>3,-,-,0,-</sub> |  | 1.1<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.7 | 0.6 | 1.0 | 14.5 |
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
