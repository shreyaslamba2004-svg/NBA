# NBA model · Fri 27 Nov 2026 (US date)

Updated **Fri 27 Nov, 08:21 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-27/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 11.5 (12+) | BKN @ TOR | draftkings | 22.00 | 19.46 | 10.88 | 9.2% | 4.2% | 5.1% | +13.1% | +102.2% | 0.2% |
| Scottie Barnes AST over 9.5 (10+) | BKN @ TOR | draftkings | 8.80 | 7.88 | 4.54 | 22.0% | 10.6% | 12.7% | +11.7% | +94.0% | 0.4% |
| Jalen Brunson PA over 54.5 (55+) | MIA @ NYK | draftkings | 22.00 | 19.80 | 11.49 | 8.7% | 4.2% | 5.1% | +11.2% | +91.5% | 0.1% |
| Pascal Siakam PRA over 49.5 (50+) | PHI @ IND | draftkings | 15.00 | 13.50 | 7.84 | 12.8% | 6.2% | 7.4% | +11.2% | +91.3% | 0.2% |
| Jalen Brunson PTS over 44.5 (45+) | MIA @ NYK | draftkings | 17.40 | 15.67 | 9.12 | 11.0% | 5.4% | 6.4% | +11.1% | +90.8% | 0.2% |
| Pascal Siakam PA over 44.5 (45+) | PHI @ IND | draftkings | 21.00 | 18.94 | 11.07 | 9.0% | 4.5% | 5.3% | +10.9% | +89.8% | 0.1% |
| Pascal Siakam PTS over 39.5 (40+) | PHI @ IND | draftkings | 20.40 | 18.45 | 10.87 | 9.2% | 4.6% | 5.4% | +10.5% | +87.6% | 0.1% |
| Pascal Siakam PA over 39.5 (40+) | PHI @ IND | draftkings | 11.20 | 10.17 | 6.04 | 16.5% | 8.3% | 9.8% | +10.1% | +85.3% | 0.2% |
| Donovan Clingan REB over 17.5 (18+) | GSW @ POR | draftkings | 11.80 | 10.75 | 6.43 | 15.6% | 7.9% | 9.3% | +9.8% | +83.5% | 0.2% |
| Jalen Brunson PR over 49.5 (50+) | MIA @ NYK | draftkings | 18.60 | 16.95 | 10.16 | 9.8% | 5.0% | 5.9% | +9.7% | +83.0% | 0.1% |
| Jalen Brunson PA over 49.5 (50+) | MIA @ NYK | draftkings | 12.20 | 11.14 | 6.68 | 15.0% | 7.7% | 9.0% | +9.6% | +82.6% | 0.2% |
| Donovan Clingan REB over 19.5 (20+) | GSW @ POR | draftkings | 21.00 | 19.27 | 11.68 | 8.6% | 4.5% | 5.2% | +9.1% | +79.8% | 0.1% |
| Scottie Barnes PTS over 44.5 (45+) | BKN @ TOR | draftkings | 30.00 | 27.47 | 16.69 | 6.0% | 3.1% | 3.6% | +9.1% | +79.8% | 0.1% |
| Pascal Siakam PRA over 54.5 (55+) | PHI @ IND | draftkings | 25.00 | 23.09 | 14.24 | 7.0% | 3.7% | 4.3% | +8.3% | +75.6% | 0.1% |
| Devin Booker AST over 9.5 (10+) | DAL @ PHX | draftkings | 11.60 | 10.76 | 6.72 | 14.9% | 8.1% | 9.3% | +7.8% | +72.5% | 0.2% |
| Pascal Siakam AST over 5.5 (6+) | PHI @ IND | draftkings | 7.10 | 6.61 | 4.16 | 24.1% | 13.2% | 15.1% | +7.5% | +70.9% | 0.3% |
| Jamal Shead AST over 11.5 (12+) | BKN @ TOR | draftkings | 18.80 | 17.57 | 11.16 | 9.0% | 5.0% | 5.7% | +7.0% | +68.5% | 0.1% |
| Jamal Shead AST over 9.5 (10+) | BKN @ TOR | draftkings | 8.00 | 7.53 | 4.88 | 20.5% | 11.7% | 13.3% | +6.2% | +64.0% | 0.2% |
| Pascal Siakam PR over 49.5 (50+) | PHI @ IND | draftkings | 23.00 | 21.69 | 14.11 | 7.1% | 4.1% | 4.6% | +6.0% | +63.0% | 0.1% |
| Devin Booker PRA over 54.5 (55+) | DAL @ PHX | draftkings | 22.00 | 20.79 | 13.63 | 7.3% | 4.2% | 4.8% | +5.8% | +61.4% | 0.1% |
| Pascal Siakam PTS over 34.5 (35+) | PHI @ IND | draftkings | 9.20 | 8.70 | 5.71 | 17.5% | 10.2% | 11.5% | +5.7% | +61.1% | 0.2% |
| Pascal Siakam PR over 44.5 (45+) | PHI @ IND | draftkings | 12.20 | 11.56 | 7.61 | 13.1% | 7.7% | 8.6% | +5.5% | +60.2% | 0.1% |
| Donovan Clingan REB over 15.5 (16+) | GSW @ POR | draftkings | 6.17 | 5.85 | 3.85 | 26.0% | 15.2% | 17.1% | +5.5% | +60.2% | 0.3% |
| Pascal Siakam AST over 7.5 (8+) | PHI @ IND | draftkings | 23.00 | 21.83 | 14.42 | 6.9% | 4.1% | 4.6% | +5.4% | +59.5% | 0.1% |
| Jalen Brunson PR over 44.5 (45+) | MIA @ NYK | draftkings | 9.50 | 9.03 | 6.00 | 16.7% | 9.8% | 11.1% | +5.2% | +58.3% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MIA @ NYK | Sat 28 Nov 11:00 | 112.0–115.9 | MIA 39% | 2.54 / 1.65 | NYK -4.5 | 227.5 | NYK -3.5 covers 51%; o222.5 61% |
| MIL @ DET | Sat 28 Nov 11:30 | 103.9–113.7 | MIL 24% | 4.11 / 1.32 | DET -9.5 | 217.5 | DET -8.5 covers 54%; o218.5 48% |
| PHI @ IND | Sat 28 Nov 11:30 | 117.5–115.5 | PHI 56% | 1.79 / 2.26 | IND +2.5 | 232.5 | IND +3.5 covers 54%; o230.5 55% |
| BKN @ TOR | Sat 28 Nov 11:30 | 104.9–113.3 | BKN 28% | 3.60 / 1.38 | TOR -8.5 | 218.5 | TOR -7.5 covers 53%; o219.5 47% |
| ATL @ BOS | Sat 28 Nov 12:00 | 108.2–116.6 | ATL 28% | 3.58 / 1.39 | BOS -8.5 | 224.5 | BOS -9.5 covers 47%; o221.5 57% |
| MEM @ MIN | Sat 28 Nov 12:30 | 110.4–116.2 | MEM 34% | 2.94 / 1.52 | MIN -5.5 | 226.5 | MIN -3.5 covers 57%; o221.5 61% |
| DAL @ PHX | Sat 28 Nov 13:00 | 113.1–116.7 | DAL 40% | 2.51 / 1.66 | PHX -3.5 | 229.5 | PHX -2.5 covers 54%; o227.5 55% |
| LAL @ SAS | Sat 28 Nov 13:30 | 109.7–112.4 | LAL 42% | 2.38 / 1.73 | SAS -2.5 | 221.5 | SAS -5.5 covers 43%; o224.5 44% |
| DEN @ UTA | Sat 28 Nov 13:30 | 124.0–114.9 | DEN 74% | 1.35 / 3.84 | UTA +8.5 | 238.5 | UTA +10.5 covers 54%; o229.5 69% |
| NOP @ LAC | Sat 28 Nov 13:30 | 111.7–118.4 | NOP 31% | 3.18 / 1.46 | LAC -6.5 | 230.5 | LAC -3.5 covers 60%; o231.5 47% |
| GSW @ POR | Sat 28 Nov 13:30 | 109.1–114.4 | GSW 36% | 2.79 / 1.56 | POR -5.5 | 223.5 | POR -9.5 covers 38%; o220.5 56% |

### MIA @ NYK
| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.0–115.9 | MIA 39% | 2.54 / 1.65 | NYK -4.5 | 227.5 | NYK -3.5 covers 51%; o222.5 61% |
| Expected (weighted by chance each plays) | 112.3–116.7 | MIA 38% | 2.61 / 1.62 | NYK -4.5 | 228.5 | NYK -3.5 covers 53%; o222.5 63% |
| if OG Anunoby plays | 112.1–117.1 | MIA 36% | 2.74 / 1.57 | NYK -5.5 | 229.5 | NYK -3.5 covers 55%; o222.5 64% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| OG Anunoby (NYK) | Doubtful | 20% | 35.5 | 18.6 | 5.9 | 2.1 | 2.3 | 1.4 | 0.9 | 1.7 | 26.6 | full tables below |
| Andre Drummond (NYK) | Questionable | 55% | 17.7 | 5.4 | 8.3 | 1.1 | 0.1 | 0.5 | 0.7 | 1.0 | 14.7 | small |
| Miles McBride (NYK) | Questionable | 55% | 17.4 | 7.3 | 1.6 | 1.4 | 1.2 | 0.6 | 0.2 | 0.4 | 10.3 | small |
| Jordan Clarkson (NYK) | Questionable | 55% | 13.9 | 6.4 | 2.0 | 0.9 | 0.5 | 0.4 | 0.1 | 0.7 | 9.3 | small |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 99% | 35.1<br><sub>39,32,33,36,34</sub> | 14.3<br><sub>22,15,16,24,14</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>5,4,3,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 7.2<br><sub>17,9,10,6,3</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>3,3,1,6,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.3 | 2.2 | 24.3 |
| Bam Adebayo | 99% | 34.1<br><sub>38,36,16,30,37</sub> | 18.6<br><sub>37,20,4,26,24</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 8.7<br><sub>14,5,1,4,15</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>3,4,2,2,12</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>2,1,0,3,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.7 | 1.7 | 30.8 |
| Giannis Antetokounmpo | 92% | 33.8<br><sub>31,31,29,32,-</sub> | 25.8<br><sub>37,34,20,27,-</sub> | 27.5 · –<br><sub>o 47% · u 53%</sub> | 11.6<br><sub>9,14,13,14,-</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>2,8,6,9,-</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.5<br><sub>1,1,0,0,-</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.2 | 3.1 | 42.3 |
| Pelle Larsson | 88% | 26.6<br><sub>-,-,-,15,30</sub> | 10.6<br><sub>-,-,-,4,21</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>-,-,-,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>-,-,-,2,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>-,-,-,1,3</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.8 | 0.2 | 1.7 | 16.6 |
| Andrew Wiggins | 92% | 24.7<br><sub>32,23,34,26,22</sub> | 9.5<br><sub>8,10,17,11,5</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>3,2,5,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>4,1,1,2,1</sub> |  | 1.2<br><sub>1,0,3,1,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.7 | 0.7 | 1.0 | 14.2 |
| Klay Thompson | 88% | 21.8<br><sub>-,20,22,23,23</sub> | 10.8<br><sub>-,26,17,13,9</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>-,1,0,1,6</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.4<br><sub>-,4,2,1,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>-,6,5,4,3</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.4 | 0.5 | 0.8 | 14.1 |
| Ryan Conwell | 93% | 20.0<br><sub>33,26,30,26,29</sub> | 7.3<br><sub>20,9,14,13,10</sub> |  | 2.0<br><sub>5,4,2,3,1</sub> |  | 1.2<br><sub>2,1,3,1,1</sub> |  | 1.1<br><sub>4,2,1,3,2</sub> |  | 0.6 | 0.2 | 0.7 | 10.5 |
| Bobby Portis | 99% | 17.7<br><sub>15,18,23,17,21</sub> | 7.4<br><sub>5,7,16,9,10</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,4,6,3,8</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>2,2,0,0,1</sub> |  | 0.9<br><sub>1,1,2,1,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.4 | 0.2 | 0.6 | 12.8 |
| Nikola Jovic | 66% | 11.9<br><sub>-,11,-,14,19</sub> | 4.0<br><sub>-,2,-,4,15</sub> |  | 2.2<br><sub>-,1,-,1,8</sub> |  | 1.1<br><sub>-,2,-,4,3</sub> |  | 0.4<br><sub>-,0,-,1,3</sub> |  | 0.3 | 0.3 | 0.6 | 7.4 |
| Simone Fontecchio | 80% | 10.9<br><sub>7,14,19,18,15</sub> | 4.7<br><sub>0,7,10,6,11</sub> |  | 1.9<br><sub>0,5,6,5,0</sub> |  | 0.7<br><sub>2,0,2,1,0</sub> |  | 0.6<br><sub>0,1,2,2,1</sub> |  | 0.3 | 0.1 | 0.4 | 7.2 |
| Tim Hardaway Jr. | 48% | 9.9<br><sub>20,-,-,-,-</sub> | 3.8<br><sub>4,-,-,-,-</sub> |  | 1.0<br><sub>3,-,-,-,-</sub> |  | 0.4<br><sub>2,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.3 |
| Myron Gardner | 67% | 9.1<br><sub>19,26,24,-,11</sub> | 2.8<br><sub>0,5,14,-,4</sub> |  | 2.0<br><sub>4,9,2,-,1</sub> |  | 0.8<br><sub>2,3,3,-,0</sub> |  | 0.2<br><sub>0,1,4,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.6 |
| Dru Smith | 38% | 6.9<br><sub>6,-,-,-,-</sub> | 2.0<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 3.9 |
| Keshad Johnson | 52% | 6.1<br><sub>-,1,3,-,-</sub> | 2.5<br><sub>-,0,0,-,-</sub> |  | 1.2<br><sub>-,0,2,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.0 |
| Nick Richards | 52% | 5.5<br><sub>-,-,3,1,-</sub> | 2.0<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 3.8 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 37.1<br><sub>41,34,35,36,32</sub> | 30.9<br><sub>28,31,21,30,22</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,5,2,7,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 7.0<br><sub>9,5,7,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>3,4,4,6,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.6 | 41.4 |
| Karl-Anthony Towns | 99% | 35.4<br><sub>43,36,33,-,29</sub> | 23.5<br><sub>28,16,22,-,30</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 14.3<br><sub>17,16,12,-,13</sub> | 12.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>3,8,4,-,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,1,2,-,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.8 | 3.0 | 42.3 |
| Josh Hart | 98% | 34.5<br><sub>26,31,28,35,39</sub> | 11.0<br><sub>0,5,11,0,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>5,4,6,8,11</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>2,2,2,6,10</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,1,3,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.7 | 24.1 |
| Landry Shamet | 99% | 33.5<br><sub>30,24,30,36,32</sub> | 14.8<br><sub>23,12,10,20,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,1,1,1,2</sub> |  | 2.0<br><sub>0,1,2,3,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>4,2,2,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 1.0 | 19.3 |
| Mikal Bridges | 99% | 33.1<br><sub>32,30,31,28,31</sub> | 13.8<br><sub>5,17,8,12,8</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>7,5,3,2,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>3,1,3,3,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.6 | 1.2 | 20.8 |
| Jose Alvarado | 84% | 20.0<br><sub>2,7,13,15,22</sub> | 7.9<br><sub>0,2,2,8,11</sub> |  | 2.4<br><sub>0,0,2,2,1</sub> |  | 3.2<br><sub>1,4,1,2,3</sub> |  | 1.2<br><sub>0,0,0,2,3</sub> |  | 0.9 | 0.2 | 1.1 | 13.5 |
| Tyler Kolek | 96% | 17.9<br><sub>16,13,12,13,11</sub> | 6.9<br><sub>0,4,6,7,8</sub> |  | 2.7<br><sub>0,1,3,3,3</sub> |  | 4.6<br><sub>7,3,5,0,0</sub> |  | 0.8<br><sub>0,0,1,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 14.2 |
| Pacome Dadiet | 52% | 16.4<br><sub>-,-,-,11,17</sub> | 6.5<br><sub>-,-,-,5,5</sub> |  | 2.9<br><sub>-,-,-,0,2</sub> |  | 1.0<br><sub>-,-,-,2,0</sub> |  | 0.8<br><sub>-,-,-,1,1</sub> |  | 0.5 | 0.1 | 0.6 | 10.4 |
| Mohamed Diawara | 52% | 15.8<br><sub>-,-,-,-,8</sub> | 5.4<br><sub>-,-,-,-,0</sub> |  | 2.8<br><sub>-,-,-,-,2</sub> |  | 1.5<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 9.8 |
| James Wiseman | 48% | 15.2<br><sub>3,-,-,25,-</sub> | 4.8<br><sub>0,-,-,5,-</sub> |  | 5.0<br><sub>3,-,-,6,-</sub> |  | 0.6<br><sub>0,-,-,2,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.7 | 0.9 | 10.4 |
| Dalton Knecht | 58% | 12.9<br><sub>-,-,-,3,-</sub> | 4.8<br><sub>-,-,-,0,-</sub> |  | 2.4<br><sub>-,-,-,0,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 7.8 |
| Jaden Akins | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.1 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>if OG Anunoby plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 35.1<br><sub>39,32,33,36,34</sub> | 14.3<br><sub>22,15,16,24,14</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>5,4,3,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 7.2<br><sub>17,9,10,6,3</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>3,3,1,6,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.3 | 2.3 | 24.4 |
| Bam Adebayo (MIA) | 99% | 34.1<br><sub>38,36,16,30,37</sub> | 18.6<br><sub>37,20,4,26,24</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 8.8<br><sub>14,5,1,4,15</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>3,4,2,2,12</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>2,1,0,3,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.7 | 1.7 | 30.8 |
| Giannis Antetokounmpo (MIA) | 92% | 33.9<br><sub>31,31,29,32,-</sub> | 25.8<br><sub>37,34,20,27,-</sub> | 27.5 · –<br><sub>o 47% · u 53%</sub> | 11.6<br><sub>9,14,13,14,-</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>2,8,6,9,-</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.5<br><sub>1,1,0,0,-</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.2 | 3.1 | 42.4 |
| Pelle Larsson (MIA) | 88% | 26.6<br><sub>-,-,-,15,30</sub> | 10.6<br><sub>-,-,-,4,21</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>-,-,-,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>-,-,-,2,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>-,-,-,1,3</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.8 | 0.2 | 1.7 | 16.5 |
| Andrew Wiggins (MIA) | 92% | 24.8<br><sub>32,23,34,26,22</sub> | 9.5<br><sub>8,10,17,11,5</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>3,2,5,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>4,1,1,2,1</sub> |  | 1.3<br><sub>1,0,3,1,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.7 | 0.7 | 1.0 | 14.2 |
| Klay Thompson (MIA) | 88% | 21.9<br><sub>-,20,22,23,23</sub> | 10.8<br><sub>-,26,17,13,9</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>-,1,0,1,6</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.4<br><sub>-,4,2,1,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>-,6,5,4,3</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.4 | 0.4 | 0.8 | 14.1 |
| Ryan Conwell (MIA) | 93% | 19.9<br><sub>33,26,30,26,29</sub> | 7.3<br><sub>20,9,14,13,10</sub> |  | 2.0<br><sub>5,4,2,3,1</sub> |  | 1.2<br><sub>2,1,3,1,1</sub> |  | 1.1<br><sub>4,2,1,3,2</sub> |  | 0.6 | 0.2 | 0.7 | 10.5 |
| Bobby Portis (MIA) | 99% | 17.7<br><sub>15,18,23,17,21</sub> | 7.4<br><sub>5,7,16,9,10</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,4,6,3,8</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>2,2,0,0,1</sub> |  | 0.9<br><sub>1,1,2,1,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.4 | 0.2 | 0.6 | 12.8 |
| Nikola Jovic (MIA) | 66% | 11.8<br><sub>-,11,-,14,19</sub> | 4.1<br><sub>-,2,-,4,15</sub> |  | 2.2<br><sub>-,1,-,1,8</sub> |  | 1.1<br><sub>-,2,-,4,3</sub> |  | 0.4<br><sub>-,0,-,1,3</sub> |  | 0.3 | 0.3 | 0.6 | 7.4 |
| Simone Fontecchio (MIA) | 80% | 10.9<br><sub>7,14,19,18,15</sub> | 4.7<br><sub>0,7,10,6,11</sub> |  | 1.9<br><sub>0,5,6,5,0</sub> |  | 0.6<br><sub>2,0,2,1,0</sub> |  | 0.6<br><sub>0,1,2,2,1</sub> |  | 0.3 | 0.1 | 0.4 | 7.2 |
| Tim Hardaway Jr. (MIA) | 48% | 10.0<br><sub>20,-,-,-,-</sub> | 3.8<br><sub>4,-,-,-,-</sub> |  | 1.0<br><sub>3,-,-,-,-</sub> |  | 0.4<br><sub>2,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.3 |
| Myron Gardner (MIA) | 67% | 9.1<br><sub>19,26,24,-,11</sub> | 2.7<br><sub>0,5,14,-,4</sub> |  | 2.0<br><sub>4,9,2,-,1</sub> |  | 0.8<br><sub>2,3,3,-,0</sub> |  | 0.2<br><sub>0,1,4,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.6 |
| Dru Smith (MIA) | 38% | 6.9<br><sub>6,-,-,-,-</sub> | 2.0<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.0 |
| Keshad Johnson (MIA) | 52% | 6.0<br><sub>-,1,3,-,-</sub> | 2.5<br><sub>-,0,0,-,-</sub> |  | 1.2<br><sub>-,0,2,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.0 |
| Nick Richards (MIA) | 52% | 5.5<br><sub>-,-,3,1,-</sub> | 2.0<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.8 |
| Jalen Brunson (NYK) | 99% | 36.3<br><sub>41,34,35,36,32</sub> | 29.9<br><sub>28,31,21,30,22</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,5,2,7,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 6.8<br><sub>9,5,7,5,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>3,4,4,6,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.2 | 2.4 | 40.1 |
| OG Anunoby (NYK) | 100% | 35.5<br><sub>44,36,36,-,-</sub> | 18.6<br><sub>21,16,15,-,-</sub> |  | 5.9<br><sub>9,4,7,-,-</sub> |  | 2.1<br><sub>1,0,2,-,-</sub> |  | 2.3<br><sub>2,1,1,-,-</sub> |  | 1.4 | 0.9 | 1.7 | 26.6 |
| Karl-Anthony Towns (NYK) | 99% | 34.5<br><sub>43,36,33,-,29</sub> | 21.5<br><sub>28,16,22,-,30</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 14.1<br><sub>17,16,12,-,13</sub> | 12.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>3,8,4,-,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,1,2,-,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.8 | 2.8 | 39.9 |
| Josh Hart (NYK) | 98% | 33.3<br><sub>26,31,28,35,39</sub> | 10.0<br><sub>0,5,11,0,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 7.9<br><sub>5,4,6,8,11</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>2,2,2,6,10</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>0,1,3,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.3 | 1.6 | 22.4 |
| Mikal Bridges (NYK) | 99% | 30.2<br><sub>32,30,31,28,31</sub> | 11.3<br><sub>5,17,8,12,8</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>7,5,3,2,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>3,1,3,3,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.5 | 1.1 | 17.5 |
| Landry Shamet (NYK) | 99% | 29.9<br><sub>30,24,30,36,32</sub> | 12.3<br><sub>23,12,10,20,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,1,1,1,2</sub> |  | 1.9<br><sub>0,1,2,3,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>4,2,2,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.2 | 0.9 | 16.2 |
| Jose Alvarado (NYK) | 84% | 15.5<br><sub>2,7,13,15,22</sub> | 5.9<br><sub>0,2,2,8,11</sub> |  | 1.9<br><sub>0,0,2,2,1</sub> |  | 2.5<br><sub>1,4,1,2,3</sub> |  | 0.8<br><sub>0,0,0,2,3</sub> |  | 0.7 | 0.2 | 0.9 | 10.3 |
| Tyler Kolek (NYK) | 96% | 14.1<br><sub>16,13,12,13,11</sub> | 5.0<br><sub>0,4,6,7,8</sub> |  | 2.0<br><sub>0,1,3,3,3</sub> |  | 3.6<br><sub>7,3,5,0,0</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 0.4 | 0.1 | 0.8 | 10.7 |
| James Wiseman (NYK) | 48% | 10.2<br><sub>3,-,-,25,-</sub> | 3.4<br><sub>0,-,-,5,-</sub> |  | 3.4<br><sub>3,-,-,6,-</sub> |  | 0.5<br><sub>0,-,-,2,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.5 | 0.6 | 7.1 |
| Pacome Dadiet (NYK) | 52% | 9.9<br><sub>-,-,-,11,17</sub> | 4.2<br><sub>-,-,-,5,5</sub> |  | 1.7<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,1,1</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Mohamed Diawara (NYK) | 52% | 9.8<br><sub>-,-,-,-,8</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 6.2 |
| Tyler Nickel (NYK) | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jaden Akins (NYK) | 38% | 6.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 0.8 |
| Dalton Knecht (NYK) | 58% | 6.5<br><sub>-,-,-,3,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.1 |

</details>


### MIL @ DET
Out: Cade Cunningham (DET), Jalen Duren (DET), Taurean Prince (DET), Duncan Robinson (DET), Kam Jones (MIL), Cormac Ryan (MIL)

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 99% | 31.0<br><sub>20,24,31,40,37</sub> | 19.4<br><sub>5,8,19,50,32</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>5,2,4,11,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>3,4,3,7,8</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>0,0,4,7,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.3 | 2.4 | 27.5 |
| Kyle Kuzma | 99% | 26.7<br><sub>22,30,-,33,32</sub> | 12.1<br><sub>14,26,-,12,18</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>6,5,-,5,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>2,1,-,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>3,2,-,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.4 | 1.8 | 18.7 |
| Brayden Burries | 99% | 24.3<br><sub>29,25,28,26,29</sub> | 10.8<br><sub>13,20,14,26,14</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>8,7,3,8,10</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>4,1,3,4,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>2,3,2,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.3 | 1.8 | 18.5 |
| Myles Turner | 99% | 24.3<br><sub>23,21,-,26,28</sub> | 8.8<br><sub>8,4,-,5,27</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>7,5,-,6,11</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,4,-,5,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,-,1,5</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.6 | 1.8 | 1.5 | 15.8 |
| Jaime Jaquez Jr. | 99% | 24.1<br><sub>30,23,22,25,25</sub> | 11.1<br><sub>6,10,9,9,3</sub> | 13.5 · –<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>5,2,1,0,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>4,5,2,1,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.2 | 1.8 | 17.8 |
| Ryan Rollins | 99% | 23.4<br><sub>-,-,21,28,22</sub> | 10.6<br><sub>-,-,15,8,6</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>-,-,3,6,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>-,-,6,1,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>-,-,1,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.3 | 2.4 | 17.6 |
| Kel'el Ware | 98% | 18.5<br><sub>25,17,26,22,23</sub> | 7.7<br><sub>8,11,11,6,9</sub> |  | 5.5<br><sub>11,3,5,8,3</sub> |  | 0.9<br><sub>2,1,0,3,0</sub> |  | 0.6<br><sub>1,1,2,0,1</sub> |  | 0.6 | 1.1 | 1.3 | 14.1 |
| Nate Ament | 98% | 18.2<br><sub>17,17,35,14,25</sub> | 6.5<br><sub>5,7,18,2,7</sub> |  | 3.0<br><sub>2,4,9,1,4</sub> |  | 0.8<br><sub>1,1,0,0,1</sub> |  | 0.7<br><sub>1,0,2,0,0</sub> |  | 0.5 | 0.3 | 1.0 | 10.2 |
| Kasparas Jakucionis | 91% | 13.0<br><sub>26,26,22,10,7</sub> | 5.3<br><sub>25,20,18,2,0</sub> |  | 1.6<br><sub>5,3,3,3,0</sub> |  | 2.2<br><sub>5,5,2,3,3</sub> |  | 0.5<br><sub>4,3,3,0,0</sub> |  | 0.5 | 0.1 | 1.2 | 9.1 |
| Pete Nance | 96% | 12.7<br><sub>-,-,28,-,-</sub> | 3.8<br><sub>-,-,7,-,-</sub> |  | 2.1<br><sub>-,-,3,-,-</sub> |  | 0.8<br><sub>-,-,3,-,-</sub> |  | 0.4<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.6 |
| AJ Green | 64% | 10.9<br><sub>6,14,-,12,-</sub> | 3.8<br><sub>0,11,-,9,-</sub> |  | 1.0<br><sub>0,0,-,0,-</sub> |  | 0.7<br><sub>0,1,-,0,-</sub> |  | 0.6<br><sub>0,3,-,3,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Gary Trent Jr. | 67% | 8.8<br><sub>30,16,7,-,5</sub> | 3.8<br><sub>18,1,0,-,0</sub> |  | 0.6<br><sub>2,1,1,-,0</sub> |  | 0.4<br><sub>1,0,0,-,0</sub> |  | 0.4<br><sub>4,0,0,-,0</sub> |  | 0.3 | 0.0 | 0.3 | 4.9 |
| Caris LeVert | 63% | 8.8<br><sub>-,8,11,5,8</sub> | 3.4<br><sub>-,8,3,0,0</sub> |  | 1.1<br><sub>-,3,3,1,0</sub> |  | 1.0<br><sub>-,2,1,0,0</sub> |  | 0.2<br><sub>-,1,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 5.5 |
| Jericho Sims | 58% | 8.5<br><sub>11,18,10,-,-</sub> | 1.9<br><sub>4,4,0,-,-</sub> |  | 2.2<br><sub>2,6,0,-,-</sub> |  | 0.6<br><sub>0,2,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.6 | 4.7 |
| Ousmane Dieng | 64% | 8.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.6 | 4.9 |

</details>

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Daniss Jenkins | 99% | 35.0<br><sub>38,36,39,38,35</sub> | 18.6<br><sub>25,17,14,11,15</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>5,4,4,5,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.9<br><sub>5,9,1,3,10</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>3,3,2,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.2 | 2.5 | 29.8 |
| Kevin Huerter | 98% | 32.1<br><sub>36,36,36,30,32</sub> | 14.6<br><sub>9,11,20,2,13</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>7,1,3,3,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>1,7,3,1,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,4,0,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.6 | 1.7 | 22.8 |
| Ausar Thompson | 99% | 31.4<br><sub>29,34,33,38,31</sub> | 12.8<br><sub>14,10,13,18,6</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 8.5<br><sub>9,7,6,11,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>12,4,3,5,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.3 | 1.1 | 2.2 | 27.3 |
| Paul Reed | 98% | 27.1<br><sub>25,20,28,26,22</sub> | 14.7<br><sub>10,17,8,16,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>6,7,7,5,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>5,1,3,2,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.5 | 1.3 | 1.8 | 25.6 |
| John Collins | 99% | 26.9<br><sub>23,30,20,22,26</sub> | 13.8<br><sub>11,20,3,18,12</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 6.0<br><sub>1,7,6,6,4</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>0,2,1,0,0</sub> |  | 1.4<br><sub>1,4,0,4,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.8 | 1.5 | 21.1 |
| Isaiah Joe | 96% | 25.8<br><sub>-,16,18,26,30</sub> | 15.0<br><sub>-,11,9,19,21</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>-,2,1,2,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>-,2,0,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.8<br><sub>-,3,1,3,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.2 | 1.1 | 19.9 |
| Javonte Green | 98% | 25.5<br><sub>23,35,23,18,27</sub> | 9.7<br><sub>6,18,12,6,6</sub> |  | 3.9<br><sub>6,7,1,3,2</sub> |  | 1.0<br><sub>0,0,0,1,1</sub> |  | 1.6<br><sub>0,3,3,2,2</sub> |  | 1.6 | 0.4 | 0.7 | 14.5 |
| Ronald Holland II | 98% | 20.2<br><sub>-,-,-,10,17</sub> | 8.6<br><sub>-,-,-,2,13</sub> |  | 4.4<br><sub>-,-,-,4,3</sub> |  | 1.8<br><sub>-,-,-,0,1</sub> |  | 0.9<br><sub>-,-,-,0,2</sub> |  | 1.0 | 0.6 | 1.1 | 14.7 |
| Elijah Harkless | 52% | 14.3<br><sub>4,14,-,-,14</sub> | 5.5<br><sub>0,6,-,-,7</sub> |  | 1.9<br><sub>1,2,-,-,1</sub> |  | 2.5<br><sub>1,4,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,2</sub> |  | 0.6 | 0.1 | 1.0 | 9.9 |
| Chaz Lanier | 66% | 13.0<br><sub>25,16,6,-,7</sub> | 4.8<br><sub>3,9,0,-,2</sub> |  | 1.2<br><sub>3,1,0,-,2</sub> |  | 0.8<br><sub>1,0,0,-,0</sub> |  | 0.8<br><sub>1,3,0,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 6.8 |
| Tolu Smith | 38% | 8.3<br><sub>-,3,-,-,-</sub> | 3.2<br><sub>-,3,-,-,-</sub> |  | 3.0<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.7 |
| Isaac Jones | 38% | 6.4<br><sub>-,-,-,-,-</sub> | 7.6<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.4 | 0.3 | 9.7 |

</details>


### PHI @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND), Jaylen Brown (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.5–115.5 | PHI 56% | 1.79 / 2.26 | IND +2.5 | 232.5 | IND +3.5 covers 54%; o230.5 55% |
| Expected (weighted by chance each plays) | 118.6–116.6 | PHI 56% | 1.80 / 2.25 | IND +2.5 | 234.5 | IND +3.5 covers 54%; o230.5 58% |
| if Kelly Oubre Jr. plays | 117.1–116.8 | PHI 51% | 1.97 / 2.04 | IND +0.5 | 233.5 | IND +3.5 covers 58%; o230.5 57% |
| if Joel Embiid plays | 119.7–116.6 | PHI 59% | 1.69 / 2.44 | IND +3.5 | 236.5 | IND +3.5 covers 50%; o230.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kelly Oubre Jr. (IND) | Questionable | 55% | 27.8 | 13.0 | 4.5 | 1.3 | 1.4 | 0.8 | 0.7 | 1.1 | 18.7 | full tables below |
| Joel Embiid (PHI) | Questionable | 55% | 32.5 | 26.2 | 9.0 | 4.5 | 0.9 | 0.8 | 1.1 | 2.9 | 39.7 | full tables below |
| T.J. McConnell (IND) | Questionable | 55% | 17.1 | 8.9 | 2.4 | 5.0 | 0.2 | 0.8 | 0.2 | 1.3 | 16.3 | small |
| Larry Nance Jr. (IND) | Questionable | 55% | 12.5 | 4.3 | 2.4 | 0.7 | 0.5 | 0.5 | 0.2 | 0.5 | 7.4 | small |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 88% | 37.3<br><sub>36,35,-,36,35</sub> | 30.0<br><sub>27,24,-,17,22</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>4,1,-,4,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>6,9,-,4,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>5,4,-,0,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4 | 0.5 | 2.4 | 40.2 |
| VJ Edgecombe | 98% | 36.6<br><sub>31,33,43,38,35</sub> | 17.9<br><sub>11,14,24,16,12</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>4,9,8,3,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 4.7<br><sub>6,4,6,6,7</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.5 | 1.9 | 29.1 |
| LeBron James | 98% | 33.9<br><sub>33,-,31,35,30</sub> | 23.0<br><sub>15,-,22,21,23</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>7,-,3,6,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>11,-,6,6,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,-,1,0,4</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.6 | 2.9 | 37.1 |
| Dean Wade | 82% | 27.8<br><sub>35,32,-,-,28</sub> | 5.6<br><sub>12,8,-,-,2</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>7,11,-,-,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,1,-,-,2</sub> |  | 0.8<br><sub>3,1,-,-,0</sub> |  | 0.9 | 0.4 | 0.6 | 12.3 |
| Anfernee Simons | 98% | 25.5<br><sub>15,26,38,26,18</sub> | 13.9<br><sub>12,9,18,18,3</sub> |  | 2.5<br><sub>0,1,2,0,0</sub> |  | 1.9<br><sub>0,2,2,1,0</sub> |  | 2.2<br><sub>1,1,3,4,0</sub> |  | 0.6 | 0.1 | 1.1 | 18.2 |
| Kentavious Caldwell-Pope | 99% | 25.5<br><sub>22,31,32,35,17</sub> | 7.4<br><sub>9,0,8,11,2</sub> |  | 3.0<br><sub>5,2,8,1,3</sub> |  | 1.8<br><sub>0,3,1,2,1</sub> |  | 1.1<br><sub>2,0,2,3,0</sub> |  | 1.0 | 0.3 | 0.7 | 12.2 |
| Jabari Walker | 93% | 18.0<br><sub>25,16,13,20,20</sub> | 8.3<br><sub>11,12,6,9,10</sub> |  | 5.7<br><sub>7,5,5,7,5</sub> |  | 1.2<br><sub>1,1,2,4,2</sub> |  | 0.7<br><sub>3,1,1,0,0</sub> |  | 0.6 | 0.2 | 0.7 | 15.2 |
| Dominick Barlow | 91% | 15.9<br><sub>-,-,-,11,16</sub> | 5.4<br><sub>-,-,-,12,6</sub> |  | 3.6<br><sub>-,-,-,4,2</sub> |  | 0.8<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,1,0</sub> |  | 0.6 | 0.6 | 0.6 | 9.8 |
| Adem Bona | 98% | 14.7<br><sub>-,-,-,-,5</sub> | 4.3<br><sub>-,-,-,-,4</sub> |  | 4.1<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.9 | 0.8 | 9.1 |
| Labaron Philon Jr. | 80% | 9.8<br><sub>6,-,17,6,3</sub> | 4.1<br><sub>3,-,10,2,2</sub> |  | 1.2<br><sub>1,-,1,0,1</sub> |  | 0.9<br><sub>0,-,2,0,1</sub> |  | 0.4<br><sub>1,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.2 |
| Justin Edwards | 58% | 8.8<br><sub>-,-,13,-,3</sub> | 3.6<br><sub>-,-,2,-,5</sub> |  | 1.3<br><sub>-,-,1,-,1</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,1</sub> |  | 0.4 | 0.1 | 0.3 | 5.5 |
| Tacko Fall | 52% | 8.4<br><sub>5,-,10,-,-</sub> | 6.5<br><sub>0,-,2,-,-</sub> |  | 2.2<br><sub>3,-,3,-,-</sub> |  | 0.5<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.6 | 0.4 | 9.2 |
| Rayan Rupert | 36% | 7.9<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.1 |
| Caleb Love | 48% | 6.6<br><sub>-,-,6,-,-</sub> | 2.5<br><sub>-,-,3,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,1,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 3.8 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 91% | 35.5<br><sub>-,-,26,32,38</sub> | 18.9<br><sub>-,-,12,16,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.0<br><sub>-,-,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>-,-,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.7 | 31.1 |
| Pascal Siakam | 96% | 35.4<br><sub>34,33,30,33,35</sub> | 27.1<br><sub>31,24,21,25,20</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>2,4,7,6,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>2,3,2,1,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.5 | 2.2 | 38.2 |
| Aaron Nesmith | 72% | 32.6<br><sub>36,29,29,32,-</sub> | 14.6<br><sub>12,2,2,9,-</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>4,3,10,2,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,3,7,2,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,0,0,0,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.6 | 1.4 | 21.5 |
| Ivica Zubac | 91% | 28.9<br><sub>22,24,27,31,26</sub> | 13.1<br><sub>8,4,21,10,14</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 10.9<br><sub>5,3,10,14,15</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.3 | 26.3 |
| Obi Toppin | 91% | 24.9<br><sub>14,17,26,22,24</sub> | 14.1<br><sub>5,6,17,9,17</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>2,1,3,5,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,1,2,1,4</sub> |  | 1.8<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.3 | 1.1 | 21.6 |
| Quenton Jackson | 99% | 24.8<br><sub>30,22,18,17,20</sub> | 11.2<br><sub>15,15,3,2,9</sub> |  | 3.6<br><sub>6,2,2,1,3</sub> |  | 3.8<br><sub>8,3,2,3,0</sub> |  | 1.2<br><sub>1,2,1,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 18.5 |
| Braden Smith | 83% | 22.7<br><sub>-,18,11,18,24</sub> | 7.4<br><sub>-,8,5,6,6</sub> |  | 2.4<br><sub>-,5,3,1,2</sub> |  | 4.6<br><sub>-,3,5,4,6</sub> |  | 0.7<br><sub>-,2,1,0,1</sub> |  | 1.0 | 0.4 | 1.2 | 14.4 |
| Jalen Slawson | 91% | 18.3<br><sub>14,12,14,14,20</sub> | 6.1<br><sub>8,5,4,7,16</sub> |  | 4.2<br><sub>5,4,2,3,10</sub> |  | 1.7<br><sub>2,2,2,0,2</sub> |  | 0.5<br><sub>1,1,0,0,3</sub> |  | 0.9 | 1.1 | 0.8 | 12.0 |
| Jarace Walker | 91% | 17.9<br><sub>14,17,11,1,14</sub> | 7.3<br><sub>2,1,8,0,4</sub> |  | 4.2<br><sub>5,3,1,0,8</sub> |  | 1.8<br><sub>2,1,3,0,3</sub> |  | 0.9<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.9 | 13.3 |
| Kobe Brown | 88% | 16.4<br><sub>3,2,-,-,7</sub> | 6.0<br><sub>0,0,-,-,4</sub> |  | 3.0<br><sub>0,0,-,-,0</sub> |  | 1.3<br><sub>0,0,-,-,1</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.8 | 10.3 |
| Jay Huff | 71% | 14.5<br><sub>18,15,1,1,-</sub> | 6.2<br><sub>11,5,0,2,-</sub> |  | 2.9<br><sub>0,3,0,0,-</sub> |  | 1.0<br><sub>2,0,0,0,-</sub> |  | 0.8<br><sub>3,0,0,0,-</sub> |  | 0.3 | 0.9 | 0.6 | 10.1 |

</details>

<details><summary>if Kelly Oubre Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 34.9<br><sub>-,-,26,32,38</sub> | 17.8<br><sub>-,-,12,16,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 8.7<br><sub>-,-,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>-,-,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.7 | 29.7 |
| Pascal Siakam (IND) | 96% | 34.8<br><sub>34,33,30,33,35</sub> | 25.6<br><sub>31,24,21,25,20</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>2,4,7,6,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>2,3,2,1,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.5 | 2.1 | 36.7 |
| Aaron Nesmith (IND) | 72% | 30.4<br><sub>36,29,29,32,-</sub> | 12.9<br><sub>12,2,2,9,-</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,3,10,2,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>4,3,7,2,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>0,0,0,0,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.5 | 1.2 | 19.3 |
| Kelly Oubre Jr. (IND) | 100% | 27.8<br><sub>29,23,23,27,28</sub> | 13.0<br><sub>16,17,17,15,20</sub> | 11.5 · – | 4.5<br><sub>4,4,6,5,4</sub> | 3.5 | 1.3<br><sub>2,0,0,0,2</sub> |  | 1.4<br><sub>2,2,3,0,4</sub> | 1.5 | 0.8 | 0.7 | 1.1 | 18.7 |
| Ivica Zubac (IND) | 91% | 27.5<br><sub>22,24,27,31,26</sub> | 12.2<br><sub>8,4,21,10,14</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 10.5<br><sub>5,3,10,14,15</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.3 | 24.9 |
| Obi Toppin (IND) | 91% | 22.2<br><sub>14,17,26,22,24</sub> | 12.7<br><sub>5,6,17,9,17</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>2,1,3,5,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,2,1,4</sub> |  | 1.6<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.3 | 1.1 | 19.4 |
| Quenton Jackson (IND) | 99% | 21.1<br><sub>30,22,18,17,20</sub> | 9.2<br><sub>15,15,3,2,9</sub> |  | 3.1<br><sub>6,2,2,1,3</sub> |  | 3.1<br><sub>8,3,2,3,0</sub> |  | 1.0<br><sub>1,2,1,0,1</sub> |  | 0.9 | 0.2 | 1.3 | 15.5 |
| Braden Smith (IND) | 83% | 18.5<br><sub>-,18,11,18,24</sub> | 5.8<br><sub>-,8,5,6,6</sub> |  | 2.0<br><sub>-,5,3,1,2</sub> |  | 3.9<br><sub>-,3,5,4,6</sub> |  | 0.5<br><sub>-,2,1,0,1</sub> |  | 0.9 | 0.3 | 1.0 | 11.7 |
| Jalen Slawson (IND) | 91% | 15.7<br><sub>14,12,14,14,20</sub> | 5.3<br><sub>8,5,4,7,16</sub> |  | 3.6<br><sub>5,4,2,3,10</sub> |  | 1.5<br><sub>2,2,2,0,2</sub> |  | 0.4<br><sub>1,1,0,0,3</sub> |  | 0.7 | 1.0 | 0.7 | 10.4 |
| Jarace Walker (IND) | 91% | 15.4<br><sub>14,17,11,1,14</sub> | 6.4<br><sub>2,1,8,0,4</sub> |  | 3.6<br><sub>5,3,1,0,8</sub> |  | 1.6<br><sub>2,1,3,0,3</sub> |  | 0.8<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.3 | 0.8 | 11.6 |
| Kobe Brown (IND) | 88% | 11.5<br><sub>3,2,-,-,7</sub> | 4.3<br><sub>0,0,-,-,4</sub> |  | 2.1<br><sub>0,0,-,-,0</sub> |  | 1.0<br><sub>0,0,-,-,1</sub> |  | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 7.3 |
| Jay Huff (IND) | 71% | 11.4<br><sub>18,15,1,1,-</sub> | 5.1<br><sub>11,5,0,2,-</sub> |  | 2.3<br><sub>0,3,0,0,-</sub> |  | 0.8<br><sub>2,0,0,0,-</sub> |  | 0.6<br><sub>3,0,0,0,-</sub> |  | 0.2 | 0.7 | 0.5 | 8.2 |
| Tyrese Maxey (PHI) | 88% | 37.3<br><sub>36,35,-,36,35</sub> | 29.8<br><sub>27,24,-,17,22</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>4,1,-,4,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>6,9,-,4,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>5,4,-,0,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4 | 0.5 | 2.4 | 39.9 |
| VJ Edgecombe (PHI) | 98% | 36.6<br><sub>31,33,43,38,35</sub> | 17.9<br><sub>11,14,24,16,12</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>4,9,8,3,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 4.8<br><sub>6,4,6,6,7</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.6 | 0.5 | 1.9 | 29.2 |
| LeBron James (PHI) | 98% | 34.0<br><sub>33,-,31,35,30</sub> | 22.9<br><sub>15,-,22,21,23</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>7,-,3,6,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>11,-,6,6,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,-,1,0,4</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.6 | 3.0 | 37.1 |
| Dean Wade (PHI) | 82% | 27.7<br><sub>35,32,-,-,28</sub> | 5.6<br><sub>12,8,-,-,2</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>7,11,-,-,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,1,-,-,2</sub> |  | 0.8<br><sub>3,1,-,-,0</sub> |  | 0.9 | 0.4 | 0.6 | 12.3 |
| Anfernee Simons (PHI) | 98% | 25.6<br><sub>15,26,38,26,18</sub> | 13.9<br><sub>12,9,18,18,3</sub> |  | 2.5<br><sub>0,1,2,0,0</sub> |  | 1.9<br><sub>0,2,2,1,0</sub> |  | 2.2<br><sub>1,1,3,4,0</sub> |  | 0.6 | 0.1 | 1.1 | 18.3 |
| Kentavious Caldwell-Pope (PHI) | 99% | 25.5<br><sub>22,31,32,35,17</sub> | 7.3<br><sub>9,0,8,11,2</sub> |  | 3.0<br><sub>5,2,8,1,3</sub> |  | 1.8<br><sub>0,3,1,2,1</sub> |  | 1.1<br><sub>2,0,2,3,0</sub> |  | 1.0 | 0.3 | 0.7 | 12.2 |
| Jabari Walker (PHI) | 93% | 18.0<br><sub>25,16,13,20,20</sub> | 8.4<br><sub>11,12,6,9,10</sub> |  | 5.7<br><sub>7,5,5,7,5</sub> |  | 1.2<br><sub>1,1,2,4,2</sub> |  | 0.7<br><sub>3,1,1,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 15.3 |
| Dominick Barlow (PHI) | 91% | 15.9<br><sub>-,-,-,11,16</sub> | 5.3<br><sub>-,-,-,12,6</sub> |  | 3.5<br><sub>-,-,-,4,2</sub> |  | 0.8<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.6 | 0.6 | 0.6 | 9.7 |
| Adem Bona (PHI) | 98% | 14.7<br><sub>-,-,-,-,5</sub> | 4.3<br><sub>-,-,-,-,4</sub> |  | 4.1<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.9 | 0.8 | 9.0 |
| Labaron Philon Jr. (PHI) | 80% | 9.8<br><sub>6,-,17,6,3</sub> | 4.1<br><sub>3,-,10,2,2</sub> |  | 1.3<br><sub>1,-,1,0,1</sub> |  | 0.9<br><sub>0,-,2,0,1</sub> |  | 0.4<br><sub>1,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.3 |
| Justin Edwards (PHI) | 58% | 8.8<br><sub>-,-,13,-,3</sub> | 3.6<br><sub>-,-,2,-,5</sub> |  | 1.3<br><sub>-,-,1,-,1</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,1</sub> |  | 0.4 | 0.1 | 0.3 | 5.5 |
| Tacko Fall (PHI) | 52% | 8.4<br><sub>5,-,10,-,-</sub> | 6.5<br><sub>0,-,2,-,-</sub> |  | 2.3<br><sub>3,-,3,-,-</sub> |  | 0.5<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.6 | 0.4 | 9.2 |
| Rayan Rupert (PHI) | 36% | 8.0<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.2 |
| Caleb Love (PHI) | 48% | 6.6<br><sub>-,-,6,-,-</sub> | 2.4<br><sub>-,-,3,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.7 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 35.5<br><sub>-,-,26,32,38</sub> | 19.0<br><sub>-,-,12,16,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.0<br><sub>-,-,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>-,-,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.7 | 31.1 |
| Pascal Siakam (IND) | 96% | 35.4<br><sub>34,33,30,33,35</sub> | 27.2<br><sub>31,24,21,25,20</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>2,4,7,6,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>2,3,2,1,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.5 | 2.2 | 38.3 |
| Aaron Nesmith (IND) | 72% | 32.6<br><sub>36,29,29,32,-</sub> | 14.7<br><sub>12,2,2,9,-</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>4,3,10,2,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,3,7,2,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,0,0,0,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.6 | 1.4 | 21.6 |
| Ivica Zubac (IND) | 91% | 29.0<br><sub>22,24,27,31,26</sub> | 13.2<br><sub>8,4,21,10,14</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 10.9<br><sub>5,3,10,14,15</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.3 | 26.3 |
| Obi Toppin (IND) | 91% | 24.9<br><sub>14,17,26,22,24</sub> | 14.2<br><sub>5,6,17,9,17</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>2,1,3,5,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,1,2,1,4</sub> |  | 1.8<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.3 | 1.1 | 21.7 |
| Quenton Jackson (IND) | 99% | 24.8<br><sub>30,22,18,17,20</sub> | 11.2<br><sub>15,15,3,2,9</sub> |  | 3.6<br><sub>6,2,2,1,3</sub> |  | 3.8<br><sub>8,3,2,3,0</sub> |  | 1.2<br><sub>1,2,1,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 18.6 |
| Braden Smith (IND) | 83% | 22.8<br><sub>-,18,11,18,24</sub> | 7.5<br><sub>-,8,5,6,6</sub> |  | 2.5<br><sub>-,5,3,1,2</sub> |  | 4.7<br><sub>-,3,5,4,6</sub> |  | 0.7<br><sub>-,2,1,0,1</sub> |  | 1.0 | 0.4 | 1.2 | 14.6 |
| Jalen Slawson (IND) | 91% | 18.2<br><sub>14,12,14,14,20</sub> | 6.1<br><sub>8,5,4,7,16</sub> |  | 4.1<br><sub>5,4,2,3,10</sub> |  | 1.7<br><sub>2,2,2,0,2</sub> |  | 0.5<br><sub>1,1,0,0,3</sub> |  | 0.9 | 1.1 | 0.8 | 11.9 |
| Jarace Walker (IND) | 91% | 17.9<br><sub>14,17,11,1,14</sub> | 7.4<br><sub>2,1,8,0,4</sub> |  | 4.1<br><sub>5,3,1,0,8</sub> |  | 1.8<br><sub>2,1,3,0,3</sub> |  | 0.9<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.9 | 13.4 |
| Kobe Brown (IND) | 88% | 16.5<br><sub>3,2,-,-,7</sub> | 6.0<br><sub>0,0,-,-,4</sub> |  | 3.0<br><sub>0,0,-,-,0</sub> |  | 1.3<br><sub>0,0,-,-,1</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.8 | 10.3 |
| Jay Huff (IND) | 71% | 14.5<br><sub>18,15,1,1,-</sub> | 6.3<br><sub>11,5,0,2,-</sub> |  | 2.9<br><sub>0,3,0,0,-</sub> |  | 1.0<br><sub>2,0,0,0,-</sub> |  | 0.8<br><sub>3,0,0,0,-</sub> |  | 0.3 | 0.9 | 0.6 | 10.2 |
| Tyrese Maxey (PHI) | 88% | 35.8<br><sub>36,35,-,36,35</sub> | 26.5<br><sub>27,24,-,17,22</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>4,1,-,4,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>6,9,-,4,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>5,4,-,0,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.5 | 2.1 | 35.8 |
| VJ Edgecombe (PHI) | 98% | 34.6<br><sub>31,33,43,38,35</sub> | 14.7<br><sub>11,14,24,16,12</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>4,9,8,3,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 4.3<br><sub>6,4,6,6,7</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.4 | 0.4 | 1.4 | 25.2 |
| LeBron James (PHI) | 98% | 32.8<br><sub>33,-,31,35,30</sub> | 19.5<br><sub>15,-,22,21,23</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>7,-,3,6,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>11,-,6,6,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>0,-,1,0,4</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 2.6 | 32.6 |
| Joel Embiid (PHI) | 100% | 32.5<br><sub>-,32,36,34,-</sub> | 26.2<br><sub>-,37,26,26,-</sub> | 23.5 · – | 9.0<br><sub>-,5,6,17,-</sub> | 8.5 | 4.5<br><sub>-,1,7,9,-</sub> | 3.5 | 0.9<br><sub>-,2,0,0,-</sub> | 0.5 | 0.8 | 1.1 | 2.9 | 39.7 |
| Dean Wade (PHI) | 82% | 25.4<br><sub>35,32,-,-,28</sub> | 4.9<br><sub>12,8,-,-,2</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>7,11,-,-,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>3,1,-,-,2</sub> |  | 0.7<br><sub>3,1,-,-,0</sub> |  | 0.8 | 0.4 | 0.5 | 11.1 |
| Anfernee Simons (PHI) | 98% | 22.1<br><sub>15,26,38,26,18</sub> | 10.5<br><sub>12,9,18,18,3</sub> |  | 2.1<br><sub>0,1,2,0,0</sub> |  | 1.5<br><sub>0,2,2,1,0</sub> |  | 1.8<br><sub>1,1,3,4,0</sub> |  | 0.5 | 0.1 | 0.8 | 14.2 |
| Kentavious Caldwell-Pope (PHI) | 99% | 21.4<br><sub>22,31,32,35,17</sub> | 5.5<br><sub>9,0,8,11,2</sub> |  | 2.5<br><sub>5,2,8,1,3</sub> |  | 1.4<br><sub>0,3,1,2,1</sub> |  | 0.8<br><sub>2,0,2,3,0</sub> |  | 0.8 | 0.3 | 0.5 | 9.5 |
| Jabari Walker (PHI) | 93% | 14.7<br><sub>25,16,13,20,20</sub> | 6.4<br><sub>11,12,6,9,10</sub> |  | 4.7<br><sub>7,5,5,7,5</sub> |  | 0.9<br><sub>1,1,2,4,2</sub> |  | 0.5<br><sub>3,1,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 11.9 |
| Dominick Barlow (PHI) | 91% | 13.9<br><sub>-,-,-,11,16</sub> | 4.5<br><sub>-,-,-,12,6</sub> |  | 3.1<br><sub>-,-,-,4,2</sub> |  | 0.8<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.5 | 0.5 | 8.3 |
| Adem Bona (PHI) | 98% | 9.4<br><sub>-,-,-,-,5</sub> | 2.8<br><sub>-,-,-,-,4</sub> |  | 2.6<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.6 | 0.5 | 5.8 |
| Labaron Philon Jr. (PHI) | 80% | 7.1<br><sub>6,-,17,6,3</sub> | 2.9<br><sub>3,-,10,2,2</sub> |  | 0.9<br><sub>1,-,1,0,1</sub> |  | 0.8<br><sub>0,-,2,0,1</sub> |  | 0.2<br><sub>1,-,2,0,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Justin Edwards (PHI) | 58% | 6.7<br><sub>-,-,13,-,3</sub> | 2.9<br><sub>-,-,2,-,5</sub> |  | 1.0<br><sub>-,-,1,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.3 |
| Rayan Rupert (PHI) | 36% | 6.7<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.3 |
| Tacko Fall (PHI) | 52% | 6.1<br><sub>5,-,10,-,-</sub> | 4.7<br><sub>0,-,2,-,-</sub> |  | 1.8<br><sub>3,-,3,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.5 | 0.3 | 6.8 |
| Caleb Love (PHI) | 48% | 5.6<br><sub>-,-,6,-,-</sub> | 2.2<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.3 |

</details>


### BKN @ TOR
Out: RJ Barrett (TOR), Kawhi Leonard (TOR), Malachi Smith (TOR), Drake Powell (BKN), Nolan Traore (BKN), Moritz Wagner (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 104.9–113.3 | BKN 28% | 3.60 / 1.38 | TOR -8.5 | 218.5 | TOR -7.5 covers 53%; o219.5 47% |
| Expected (weighted by chance each plays) | 105.0–114.0 | BKN 27% | 3.77 / 1.36 | TOR -9.5 | 219.5 | TOR -7.5 covers 54%; o219.5 49% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alijah Martin (TOR) | Questionable | 55% | 13.4 | 4.8 | 1.9 | 0.9 | 0.5 | 0.6 | 0.2 | 0.8 | 7.7 | small |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 99% | 33.8<br><sub>31,34,27,39,35</sub> | 20.5<br><sub>22,33,17,27,29</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>4,6,0,9,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>5,1,4,6,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,3,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 3.8 | 31.0 |
| Michael Porter Jr. | 88% | 33.4<br><sub>-,40,27,34,31</sub> | 19.7<br><sub>-,25,5,16,11</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>-,6,3,4,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>-,2,1,5,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>-,2,1,3,0</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.4 | 2.6 | 28.4 |
| Egor Demin | 98% | 25.9<br><sub>27,26,31,21,25</sub> | 11.3<br><sub>11,9,22,6,10</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>1,3,4,3,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>2,4,4,2,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>3,2,3,0,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.3 | 2.0 | 17.4 |
| Mikel Brown Jr. | 98% | 25.7<br><sub>20,18,27,24,29</sub> | 12.8<br><sub>6,3,15,18,17</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>1,1,1,1,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>2,5,4,0,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,1,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.8 | 19.2 |
| Day'Ron Sharpe | 99% | 25.4<br><sub>28,25,22,26,26</sub> | 9.9<br><sub>16,6,6,17,6</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 8.2<br><sub>11,9,5,11,5</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>5,5,1,2,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 1.1 | 0.9 | 2.0 | 21.8 |
| Noah Clowney | 99% | 23.1<br><sub>35,24,19,22,26</sub> | 8.5<br><sub>15,9,7,0,13</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>7,3,3,2,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.1<br><sub>3,3,1,2,1</sub> |  | 1.1<br><sub>3,1,1,0,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.6 | 0.6 | 1.1 | 13.4 |
| Danny Wolf | 91% | 22.5<br><sub>28,11,23,26,25</sub> | 9.3<br><sub>14,3,6,20,11</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 5.1<br><sub>6,2,6,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,1,2,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>4,1,1,4,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.5 | 1.4 | 16.5 |
| Keon Ellis | 91% | 16.7<br><sub>7,20,6,8,16</sub> | 4.1<br><sub>0,8,3,0,6</sub> |  | 1.6<br><sub>0,2,1,1,0</sub> |  | 1.1<br><sub>1,0,0,1,0</sub> |  | 0.5<br><sub>0,2,1,0,2</sub> |  | 0.9 | 0.6 | 0.6 | 6.8 |
| Ben Saraf | 52% | 12.7<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.7 | 8.2 |
| Terance Mann | 64% | 12.1<br><sub>9,-,5,-,3</sub> | 3.1<br><sub>2,-,0,-,0</sub> |  | 1.5<br><sub>1,-,1,-,0</sub> |  | 1.1<br><sub>1,-,0,-,0</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 5.7 |
| Chaney Johnson | 76% | 11.3<br><sub>12,1,6,-,-</sub> | 3.2<br><sub>1,0,2,-,-</sub> |  | 1.8<br><sub>5,0,2,-,-</sub> |  | 0.6<br><sub>0,0,1,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 5.6 |
| Grant Nelson | 84% | 8.7<br><sub>-,-,-,-,8</sub> | 3.0<br><sub>-,-,-,-,2</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 0.8<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.6 | 0.6 | 5.6 |
| Josh Minott | 63% | 8.6<br><sub>2,-,4,-,2</sub> | 4.2<br><sub>0,-,0,-,0</sub> |  | 1.5<br><sub>0,-,0,-,0</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.3 | 0.5 | 6.2 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 36.0<br><sub>36,34,-,37,38</sub> | 26.7<br><sub>30,20,-,29,31</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>9,4,-,5,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 7.4<br><sub>4,2,-,5,8</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.0<br><sub>4,1,-,0,2</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.8 | 1.3 | 3.3 | 41.3 |
| Ja'Kobe Walter | 99% | 34.0<br><sub>36,33,38,33,36</sub> | 14.7<br><sub>7,25,18,8,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>2,1,7,3,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>1,2,6,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>1,7,3,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7 | 0.3 | 1.2 | 21.5 |
| Immanuel Quickley | 91% | 33.1<br><sub>38,34,34,33,32</sub> | 19.5<br><sub>17,14,24,18,13</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>6,1,3,3,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>6,7,5,10,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>3,2,4,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.1 | 2.0 | 30.4 |
| Jakob Poeltl | 96% | 28.3<br><sub>17,18,29,32,28</sub> | 12.1<br><sub>11,3,8,10,15</sub> | 9.5 · –<br><sub>o 55% · u 45%</sub> | 8.4<br><sub>5,6,9,9,10</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>1,1,5,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 1.3 | 1.6 | 23.1 |
| Allen Graves | 98% | 27.2<br><sub>16,13,31,33,31</sub> | 9.0<br><sub>2,3,9,20,7</sub> | 10.5 · –<br><sub>o 44% · u 56%</sub> | 4.8<br><sub>5,2,4,10,2</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>0,1,1,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.6 | 1.0 | 15.2 |
| Collin Murray-Boyles | 84% | 26.7<br><sub>40,33,5,-,24</sub> | 11.7<br><sub>6,8,1,-,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>13,1,2,-,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>2,3,1,-,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.4<br><sub>0,0,0,-,0</sub> |  | 1.3 | 1.3 | 1.8 | 20.1 |
| Jamal Shead | 99% | 26.2<br><sub>26,20,24,15,26</sub> | 9.4<br><sub>19,7,15,0,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>2,0,1,1,2</sub> |  | 7.0<br><sub>4,6,6,4,6</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>3,1,1,0,3</sub> |  | 1.1 | 0.2 | 2.0 | 18.5 |
| Jamison Battle | 98% | 22.0<br><sub>8,7,33,20,13</sub> | 10.6<br><sub>0,0,19,10,13</sub> |  | 2.9<br><sub>3,1,5,5,2</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 1.8<br><sub>0,0,5,2,3</sub> |  | 0.5 | 0.1 | 0.7 | 14.4 |
| Trayce Jackson-Davis | 67% | 13.4<br><sub>-,-,17,16,5</sub> | 4.9<br><sub>-,-,3,8,0</sub> |  | 4.2<br><sub>-,-,7,2,2</sub> |  | 1.0<br><sub>-,-,1,1,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.9 | 0.8 | 0.6 | 10.0 |
| Kyle Anderson | 52% | 11.2<br><sub>-,-,4,-,-</sub> | 3.3<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 2.1<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.4 | 0.6 | 7.3 |
| Jaden Bradley | 43% | 8.3<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 5.2 |

</details>


### ATL @ BOS
Out: Devin Carter (BOS), Mouhamed Gueye (ATL), Jock Landale (ATL), CJ McCollum (ATL), Asa Newell (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.2–116.6 | ATL 28% | 3.58 / 1.39 | BOS -8.5 | 224.5 | BOS -9.5 covers 47%; o221.5 57% |
| Expected (weighted by chance each plays) | 108.4–116.6 | ATL 28% | 3.61 / 1.38 | BOS -8.5 | 225.5 | BOS -9.5 covers 46%; o221.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 9.7 | 3.5 | 1.6 | 0.6 | 0.3 | 0.2 | 0.1 | 0.5 | 5.7 | small |
| Mitchell Robinson (BOS) | Questionable | 55% | 11.5 | 3.6 | 4.6 | 0.6 | 0.0 | 0.5 | 0.7 | 0.6 | 8.8 | small |
| Rafael Castro (ATL) | Doubtful | 20% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 36.0<br><sub>40,35,34,36,30</sub> | 20.0<br><sub>27,14,16,26,12</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>11,11,12,6,11</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>10,5,11,6,0</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.5 | 3.3 | 36.0 |
| Dyson Daniels | 99% | 34.9<br><sub>36,27,37,35,39</sub> | 11.2<br><sub>6,9,10,11,5</sub> | 8.5 · –<br><sub>o 55% · u 45%</sub> | 8.0<br><sub>9,10,10,8,14</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>4,5,4,10,8</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 0.5<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 35% · u 65%</sub> | 2.2 | 0.5 | 1.8 | 24.9 |
| Nickeil Alexander-Walker | 99% | 34.1<br><sub>41,33,32,32,28</sub> | 20.1<br><sub>16,20,19,17,27</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>6,5,4,4,2</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 3.1<br><sub>3,4,7,3,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>1,2,3,2,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.5 | 2.0 | 26.7 |
| Onyeka Okongwu | 99% | 33.7<br><sub>35,36,36,34,29</sub> | 14.9<br><sub>17,16,28,16,6</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>6,11,9,7,9</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>1,0,2,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.9<br><sub>2,3,5,2,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.9 | 1.7 | 25.8 |
| Luguentz Dort | 99% | 28.4<br><sub>20,18,31,23,31</sub> | 10.4<br><sub>10,3,16,2,16</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>1,4,3,1,7</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>2,0,0,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6<br><sub>1,0,3,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 0.8 | 15.4 |
| Aaron Wiggins | 98% | 26.1<br><sub>26,24,26,34,19</sub> | 12.1<br><sub>9,7,14,19,9</sub> |  | 3.5<br><sub>4,3,3,2,6</sub> |  | 2.0<br><sub>3,3,1,3,1</sub> |  | 1.9<br><sub>1,1,4,4,1</sub> |  | 0.8 | 0.3 | 1.3 | 17.5 |
| Kingston Flemings | 58% | 23.6<br><sub>17,-,-,-,27</sub> | 8.7<br><sub>0,-,-,-,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,-,-,-,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.9<br><sub>1,-,-,-,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>0,-,-,-,1</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.7 | 0.3 | 1.8 | 15.4 |
| Corey Kispert | 71% | 15.5<br><sub>-,16,17,16,19</sub> | 7.3<br><sub>-,14,8,7,18</sub> |  | 2.1<br><sub>-,3,1,3,4</sub> |  | 1.1<br><sub>-,1,2,0,3</sub> |  | 1.0<br><sub>-,3,2,1,4</sub> |  | 0.2 | 0.1 | 0.6 | 10.4 |
| Zuby Ejiofor | 86% | 14.6<br><sub>-,12,12,14,19</sub> | 4.9<br><sub>-,4,3,5,4</sub> |  | 3.2<br><sub>-,3,3,2,4</sub> |  | 1.0<br><sub>-,0,0,2,1</sub> |  | 0.4<br><sub>-,1,1,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 9.2 |
| RayJ Dennis | 63% | 11.7<br><sub>-,10,10,13,-</sub> | 4.8<br><sub>-,6,3,8,-</sub> |  | 1.8<br><sub>-,1,3,4,-</sub> |  | 1.9<br><sub>-,3,5,2,-</sub> |  | 0.5<br><sub>-,1,1,0,-</sub> |  | 0.4 | 0.2 | 0.7 | 8.6 |
| Dorian Finney-Smith | 48% | 7.0<br><sub>-,-,5,3,-</sub> | 1.8<br><sub>-,-,0,0,-</sub> |  | 1.1<br><sub>-,-,2,0,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.3 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 99% | 34.8<br><sub>36,37,-,38,37</sub> | 27.3<br><sub>24,24,-,27,41</sub> | 27.5 · –<br><sub>o 49% · u 51%</sub> | 8.9<br><sub>12,8,-,10,6</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>4,3,-,6,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>3,3,-,4,6</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.7 | 3.3 | 42.7 |
| Paul George | 99% | 31.2<br><sub>36,23,37,-,33</sub> | 19.4<br><sub>22,10,19,-,28</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>8,4,8,-,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,1,5,-,9</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>5,1,2,-,6</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.7 | 0.5 | 2.2 | 28.4 |
| Derrick White | 88% | 31.1<br><sub>32,35,-,32,30</sub> | 13.6<br><sub>9,12,-,14,6</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>3,3,-,3,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.5<br><sub>2,8,-,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,0,-,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.9 | 1.4 | 21.9 |
| Payton Pritchard | 99% | 28.6<br><sub>32,30,34,28,28</sub> | 13.9<br><sub>21,15,9,5,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>4,1,6,1,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 4.1<br><sub>5,2,8,4,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,3,0,1,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.1 | 1.2 | 21.3 |
| Neemias Queta | 99% | 25.5<br><sub>-,27,30,30,25</sub> | 11.7<br><sub>-,17,15,6,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.7<br><sub>-,10,7,10,5</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>-,3,1,4,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.2<br><sub>-,0,1,0,0</sub> | 0.5<br><sub>o 13% · u 87%</sub> | 0.7 | 1.3 | 1.4 | 22.4 |
| Sam Hauser | 99% | 21.8<br><sub>25,17,31,22,22</sub> | 7.8<br><sub>12,9,14,3,4</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>1,2,6,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.5<br><sub>4,3,4,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.4 | 0.2 | 0.3 | 12.2 |
| Baylor Scheierman | 99% | 18.1<br><sub>11,13,18,15,19</sub> | 5.5<br><sub>0,0,4,3,8</sub> |  | 3.2<br><sub>1,1,3,4,4</sub> |  | 1.3<br><sub>1,1,1,1,1</sub> |  | 0.8<br><sub>0,0,0,1,2</sub> |  | 0.7 | 0.1 | 0.6 | 10.0 |
| Luka Garza | 98% | 15.3<br><sub>18,5,17,17,18</sub> | 7.3<br><sub>3,0,5,10,7</sub> |  | 3.7<br><sub>0,1,5,5,4</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 0.7<br><sub>1,0,0,0,1</sub> |  | 0.4 | 0.4 | 0.7 | 12.4 |
| Hugo Gonzalez | 98% | 12.5<br><sub>4,16,17,22,9</sub> | 3.8<br><sub>0,2,5,6,0</sub> |  | 2.6<br><sub>2,6,4,2,5</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.4<br><sub>0,0,1,2,0</sub> |  | 0.5 | 0.3 | 0.6 | 7.0 |
| Jordan Walsh | 99% | 9.9<br><sub>17,4,8,9,5</sub> | 3.0<br><sub>6,0,1,2,0</sub> |  | 1.9<br><sub>2,0,4,0,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.2<br><sub>2,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.3 |
| Mike Conley | 52% | 9.7<br><sub>-,-,18,16,-</sub> | 3.3<br><sub>-,-,19,6,-</sub> |  | 1.1<br><sub>-,-,4,2,-</sub> |  | 1.4<br><sub>-,-,2,4,-</sub> |  | 0.4<br><sub>-,-,4,2,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.8 |
| Ron Harper Jr. | 67% | 8.2<br><sub>-,-,13,6,8</sub> | 3.5<br><sub>-,-,3,5,2</sub> |  | 1.1<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,1,0,0</sub> |  | 0.4<br><sub>-,-,1,1,0</sub> |  | 0.3 | 0.2 | 0.3 | 5.1 |
| Chris Cenac Jr. | 80% | 8.0<br><sub>12,17,12,5,6</sub> | 3.1<br><sub>4,6,2,0,0</sub> |  | 2.1<br><sub>2,6,3,2,2</sub> |  | 0.4<br><sub>1,0,0,0,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |

</details>


### MEM @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.4–116.2 | MEM 34% | 2.94 / 1.52 | MIN -5.5 | 226.5 | MIN -3.5 covers 57%; o221.5 61% |
| Expected (weighted by chance each plays) | 110.9–116.3 | MEM 35% | 2.88 / 1.53 | MIN -5.5 | 227.5 | MIN -3.5 covers 56%; o221.5 63% |
| if Zach Edey plays | 111.4–115.9 | MEM 37% | 2.68 / 1.60 | MIN -4.5 | 227.5 | MIN -3.5 covers 54%; o221.5 62% |
| if LaMelo Ball plays | 109.4–118.3 | MEM 26% | 3.78 / 1.36 | MIN -8.5 | 227.5 | MIN -3.5 covers 66%; o221.5 63% |
| if Isaiah Stewart plays | 111.3–116.2 | MEM 36% | 2.74 / 1.57 | MIN -5.5 | 227.5 | MIN -3.5 covers 55%; o221.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey (MEM) | Questionable | 55% | 24.6 | 10.0 | 8.7 | 1.2 | 0.0 | 0.6 | 1.4 | 1.7 | 19.9 | full tables below |
| LaMelo Ball (MIN) | Questionable | 55% | 30.8 | 19.9 | 4.7 | 6.4 | 3.2 | 1.5 | 0.3 | 3.0 | 31.0 | full tables below |
| Isaiah Stewart (MEM) | Questionable | 55% | 21.3 | 9.5 | 4.2 | 1.1 | 0.6 | 0.5 | 1.3 | 1.1 | 14.8 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 32.0<br><sub>27,33,25,30,30</sub> | 18.1<br><sub>18,20,19,23,16</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>8,3,4,7,9</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>6,5,4,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,4,5,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.6 | 2.5 | 29.6 |
| Ty Jerome | 98% | 31.1<br><sub>-,-,-,27,29</sub> | 24.8<br><sub>-,-,-,18,29</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.3<br><sub>-,-,-,6,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>-,-,-,3,7</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 2.9 | 33.9 |
| Jaylen Wells | 99% | 28.5<br><sub>27,26,24,25,20</sub> | 11.7<br><sub>8,5,22,8,8</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,4,7,1,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.2 | 1.0 | 16.5 |
| Taylor Hendricks | 91% | 26.7<br><sub>19,21,20,27,24</sub> | 10.8<br><sub>9,18,11,5,3</sub> |  | 5.6<br><sub>3,6,1,7,4</sub> |  | 1.4<br><sub>0,2,1,2,1</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.2 | 0.7 | 1.3 | 17.8 |
| Cam Spencer | 98% | 26.4<br><sub>32,29,27,30,21</sub> | 12.5<br><sub>12,26,9,9,24</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>6,1,2,5,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>9,7,11,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,5,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.6 | 21.4 |
| Javon Small | 98% | 24.9<br><sub>29,21,25,-,19</sub> | 11.5<br><sub>12,2,14,-,3</sub> |  | 3.8<br><sub>5,4,7,-,3</sub> |  | 4.5<br><sub>12,5,7,-,5</sub> |  | 1.4<br><sub>0,0,2,-,0</sub> |  | 0.9 | 0.3 | 1.7 | 19.7 |
| Kris Murray | 91% | 24.0<br><sub>6,6,4,12,32</sub> | 5.3<br><sub>0,5,0,7,9</sub> | 6.5 · –<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>1,0,1,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,0,0,0,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.5 | 0.8 | 9.8 |
| Olivier-Maxence Prosper | 88% | 24.0<br><sub>16,16,24,23,19</sub> | 11.8<br><sub>12,5,16,7,6</sub> |  | 4.5<br><sub>0,2,5,6,3</sub> |  | 1.2<br><sub>1,0,1,0,0</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 1.0 | 0.3 | 1.2 | 17.5 |
| Jahmai Mashack | 63% | 17.8<br><sub>2,13,26,22,-</sub> | 4.2<br><sub>0,3,0,0,-</sub> |  | 2.4<br><sub>0,2,3,2,-</sub> |  | 2.0<br><sub>1,2,4,1,-</sub> |  | 0.3<br><sub>0,1,0,0,-</sub> |  | 0.9 | 0.3 | 0.9 | 8.5 |
| Quinten Post | 80% | 15.4<br><sub>9,6,10,-,3</sub> | 5.7<br><sub>5,3,5,-,0</sub> |  | 3.0<br><sub>3,2,1,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.6<br><sub>0,1,0,-,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.2 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 36.3<br><sub>31,37,39,36,34</sub> | 21.3<br><sub>13,22,17,25,34</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>6,5,3,5,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,4,1,4,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,2,4,1,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 1.1 | 2.5 | 31.5 |
| Ayo Dosunmu | 99% | 35.0<br><sub>30,39,32,34,30</sub> | 22.7<br><sub>8,30,6,19,23</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,4,4,2,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>2,5,4,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,7,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.4 | 2.6 | 32.4 |
| Jonathan Kuminga | 88% | 32.9<br><sub>29,-,35,37,26</sub> | 16.5<br><sub>13,-,23,16,15</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>9,-,3,4,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>1,-,3,2,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>1,-,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.8 | 2.2 | 25.6 |
| Rudy Gobert | 99% | 32.6<br><sub>32,22,35,32,27</sub> | 10.9<br><sub>18,0,9,7,7</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 12.1<br><sub>15,4,7,11,6</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>3,2,0,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.8 | 1.7 | 25.3 |
| Terrence Shannon Jr. | 98% | 27.7<br><sub>35,24,21,26,24</sub> | 17.1<br><sub>34,12,10,15,17</sub> |  | 3.5<br><sub>3,1,4,5,1</sub> |  | 3.6<br><sub>6,4,3,2,5</sub> |  | 1.7<br><sub>3,1,0,3,2</sub> |  | 0.8 | 0.1 | 1.7 | 24.1 |
| Trey Lyles | 99% | 22.9<br><sub>19,31,16,12,24</sub> | 7.8<br><sub>9,8,8,3,9</sub> |  | 5.0<br><sub>3,7,6,3,3</sub> |  | 1.5<br><sub>1,4,1,1,2</sub> |  | 1.0<br><sub>2,2,2,1,0</sub> |  | 0.7 | 0.4 | 0.9 | 14.3 |
| Bones Hyland | 98% | 21.0<br><sub>13,17,15,16,16</sub> | 12.8<br><sub>5,13,6,7,14</sub> |  | 2.3<br><sub>1,2,1,0,2</sub> |  | 4.2<br><sub>5,1,1,4,6</sub> |  | 2.0<br><sub>0,3,1,1,4</sub> |  | 0.9 | 0.3 | 1.4 | 19.3 |
| Joan Beringer | 98% | 18.9<br><sub>16,26,13,16,19</sub> | 6.4<br><sub>0,3,5,0,0</sub> |  | 6.7<br><sub>4,13,3,4,4</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.8 | 0.8 | 13.6 |
| Zyon Pullin | 52% | 9.5<br><sub>4,-,-,-,2</sub> | 3.9<br><sub>0,-,-,-,4</sub> |  | 1.3<br><sub>1,-,-,-,2</sub> |  | 1.3<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.5 |
| Cody Williams | 58% | 8.4<br><sub>4,13,-,-,2</sub> | 0.1<br><sub>0,0,-,-,0</sub> |  | 1.1<br><sub>1,1,-,-,0</sub> |  | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 1.6 |
| Isaiah Evans | 52% | 7.1<br><sub>4,-,-,-,2</sub> | 3.7<br><sub>0,-,-,-,2</sub> |  | 1.3<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.4 |
| Johni Broome | 52% | 6.7<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.6 |

</details>

<details><summary>if LaMelo Ball plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward (MEM) | 99% | 32.0<br><sub>27,33,25,30,30</sub> | 17.8<br><sub>18,20,19,23,16</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>8,3,4,7,9</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>6,5,4,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,4,5,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3 | 0.6 | 2.5 | 29.2 |
| Ty Jerome (MEM) | 98% | 31.1<br><sub>-,-,-,27,29</sub> | 24.6<br><sub>-,-,-,18,29</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.3<br><sub>-,-,-,6,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>-,-,-,3,7</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 2.9 | 33.8 |
| Jaylen Wells (MEM) | 99% | 28.4<br><sub>27,26,24,25,20</sub> | 11.6<br><sub>8,5,22,8,8</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,4,7,1,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.2 | 1.0 | 16.3 |
| Taylor Hendricks (MEM) | 91% | 26.8<br><sub>19,21,20,27,24</sub> | 10.8<br><sub>9,18,11,5,3</sub> |  | 5.6<br><sub>3,6,1,7,4</sub> |  | 1.4<br><sub>0,2,1,2,1</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.2 | 0.7 | 1.3 | 17.8 |
| Cam Spencer (MEM) | 98% | 26.5<br><sub>32,29,27,30,21</sub> | 12.5<br><sub>12,26,9,9,24</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>6,1,2,5,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>9,7,11,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,5,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.6 | 21.4 |
| Javon Small (MEM) | 98% | 24.7<br><sub>29,21,25,-,19</sub> | 11.3<br><sub>12,2,14,-,3</sub> |  | 3.8<br><sub>5,4,7,-,3</sub> |  | 4.4<br><sub>12,5,7,-,5</sub> |  | 1.4<br><sub>0,0,2,-,0</sub> |  | 1.0 | 0.3 | 1.7 | 19.5 |
| Kris Murray (MEM) | 91% | 24.0<br><sub>6,6,4,12,32</sub> | 5.3<br><sub>0,5,0,7,9</sub> | 6.5 · –<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>1,0,1,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>0,0,0,0,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.5 | 0.8 | 9.8 |
| Olivier-Maxence Prosper (MEM) | 88% | 23.9<br><sub>16,16,24,23,19</sub> | 11.8<br><sub>12,5,16,7,6</sub> |  | 4.5<br><sub>0,2,5,6,3</sub> |  | 1.1<br><sub>1,0,1,0,0</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 1.0 | 0.3 | 1.2 | 17.4 |
| Jahmai Mashack (MEM) | 63% | 17.8<br><sub>2,13,26,22,-</sub> | 4.2<br><sub>0,3,0,0,-</sub> |  | 2.4<br><sub>0,2,3,2,-</sub> |  | 2.0<br><sub>1,2,4,1,-</sub> |  | 0.3<br><sub>0,1,0,0,-</sub> |  | 0.9 | 0.3 | 0.9 | 8.5 |
| Quinten Post (MEM) | 80% | 15.3<br><sub>9,6,10,-,3</sub> | 5.7<br><sub>5,3,5,-,0</sub> |  | 3.0<br><sub>3,2,1,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.6<br><sub>0,1,0,-,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.2 |
| Jaden McDaniels (MIN) | 99% | 35.4<br><sub>31,37,39,36,34</sub> | 18.9<br><sub>13,22,17,25,34</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>6,5,3,5,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>3,4,1,4,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,2,4,1,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 1.1 | 2.1 | 28.6 |
| Ayo Dosunmu (MIN) | 99% | 33.3<br><sub>30,39,32,34,30</sub> | 19.1<br><sub>8,30,6,19,23</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>5,4,4,2,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>2,5,4,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,7,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.4 | 2.3 | 27.6 |
| Jonathan Kuminga (MIN) | 88% | 31.6<br><sub>29,-,35,37,26</sub> | 14.8<br><sub>13,-,23,16,15</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>9,-,3,4,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>1,-,3,2,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>1,-,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.8 | 1.9 | 23.2 |
| LaMelo Ball (MIN) | 100% | 30.8<br><sub>24,31,35,32,30</sub> | 19.9<br><sub>6,18,15,12,17</sub> | 18.5 · – | 4.7<br><sub>5,9,8,5,2</sub> | 4.5 | 6.4<br><sub>0,2,8,7,3</sub> | 5.5 | 3.2<br><sub>2,3,3,1,2</sub> | 3.5 | 1.5 | 0.3 | 3.0 | 31.0 |
| Rudy Gobert (MIN) | 99% | 30.7<br><sub>32,22,35,32,27</sub> | 9.7<br><sub>18,0,9,7,7</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 11.3<br><sub>15,4,7,11,6</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>3,2,0,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.8 | 1.5 | 22.8 |
| Terrence Shannon Jr. (MIN) | 98% | 23.8<br><sub>35,24,21,26,24</sub> | 13.5<br><sub>34,12,10,15,17</sub> |  | 3.0<br><sub>3,1,4,5,1</sub> |  | 2.6<br><sub>6,4,3,2,5</sub> |  | 1.4<br><sub>3,1,0,3,2</sub> |  | 0.7 | 0.1 | 1.3 | 19.1 |
| Trey Lyles (MIN) | 99% | 19.7<br><sub>19,31,16,12,24</sub> | 6.5<br><sub>9,8,8,3,9</sub> |  | 4.3<br><sub>3,7,6,3,3</sub> |  | 1.2<br><sub>1,4,1,1,2</sub> |  | 0.8<br><sub>2,2,2,1,0</sub> |  | 0.6 | 0.3 | 0.7 | 12.0 |
| Joan Beringer (MIN) | 98% | 16.2<br><sub>16,26,13,16,19</sub> | 5.2<br><sub>0,3,5,0,0</sub> |  | 5.7<br><sub>4,13,3,4,4</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.7 | 0.7 | 11.3 |
| Bones Hyland (MIN) | 98% | 15.8<br><sub>13,17,15,16,16</sub> | 9.2<br><sub>5,13,6,7,14</sub> |  | 1.7<br><sub>1,2,1,0,2</sub> |  | 3.0<br><sub>5,1,1,4,6</sub> |  | 1.4<br><sub>0,3,1,1,4</sub> |  | 0.7 | 0.2 | 1.1 | 13.8 |
| Cody Williams (MIN) | 58% | 6.5<br><sub>4,13,-,-,2</sub> | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.8<br><sub>1,1,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 1.2 |
| Zyon Pullin (MIN) | 52% | 6.3<br><sub>4,-,-,-,2</sub> | 2.9<br><sub>0,-,-,-,4</sub> |  | 0.9<br><sub>1,-,-,-,2</sub> |  | 0.9<br><sub>0,-,-,-,1</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Isaiah Evans (MIN) | 52% | 5.7<br><sub>4,-,-,-,2</sub> | 3.1<br><sub>0,-,-,-,2</sub> |  | 1.1<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Johni Broome (MIN) | 52% | 5.5<br><sub>-,-,-,-,2</sub> | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>

<details><summary>if Isaiah Stewart plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward (MEM) | 99% | 31.6<br><sub>27,33,25,30,30</sub> | 16.1<br><sub>18,20,19,23,16</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>8,3,4,7,9</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>6,5,4,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,4,5,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.6 | 2.2 | 27.2 |
| Ty Jerome (MEM) | 98% | 30.7<br><sub>-,-,-,27,29</sub> | 23.0<br><sub>-,-,-,18,29</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.1<br><sub>-,-,-,6,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>-,-,-,3,7</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 2.8 | 32.0 |
| Jaylen Wells (MEM) | 99% | 27.7<br><sub>27,26,24,25,20</sub> | 11.2<br><sub>8,5,22,8,8</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>4,4,7,1,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.2 | 0.9 | 15.8 |
| Cam Spencer (MEM) | 98% | 26.2<br><sub>32,29,27,30,21</sub> | 12.2<br><sub>12,26,9,9,24</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>6,1,2,5,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>9,7,11,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,5,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.4 | 21.0 |
| Taylor Hendricks (MEM) | 91% | 24.6<br><sub>19,21,20,27,24</sub> | 10.1<br><sub>9,18,11,5,3</sub> |  | 5.2<br><sub>3,6,1,7,4</sub> |  | 1.2<br><sub>0,2,1,2,1</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 1.0 | 0.6 | 1.2 | 16.5 |
| Javon Small (MEM) | 98% | 24.3<br><sub>29,21,25,-,19</sub> | 10.9<br><sub>12,2,14,-,3</sub> |  | 3.7<br><sub>5,4,7,-,3</sub> |  | 4.3<br><sub>12,5,7,-,5</sub> |  | 1.3<br><sub>0,0,2,-,0</sub> |  | 0.9 | 0.3 | 1.6 | 19.0 |
| Kris Murray (MEM) | 91% | 21.6<br><sub>6,6,4,12,32</sub> | 4.9<br><sub>0,5,0,7,9</sub> | 6.5 · –<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>1,0,1,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>0,0,0,0,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.4<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.5 | 0.7 | 9.1 |
| Isaiah Stewart (MEM) | 100% | 21.3<br><sub>-,-,18,21,21</sub> | 9.5<br><sub>-,-,8,10,11</sub> |  | 4.2<br><sub>-,-,4,2,4</sub> |  | 1.1<br><sub>-,-,1,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.5 | 1.3 | 1.1 | 14.8 |
| Olivier-Maxence Prosper (MEM) | 88% | 21.0<br><sub>16,16,24,23,19</sub> | 10.4<br><sub>12,5,16,7,6</sub> |  | 4.0<br><sub>0,2,5,6,3</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.9 | 0.3 | 1.1 | 15.3 |
| Jahmai Mashack (MEM) | 63% | 16.0<br><sub>2,13,26,22,-</sub> | 3.8<br><sub>0,3,0,0,-</sub> |  | 2.1<br><sub>0,2,3,2,-</sub> |  | 1.8<br><sub>1,2,4,1,-</sub> |  | 0.3<br><sub>0,1,0,0,-</sub> |  | 0.8 | 0.3 | 0.9 | 7.7 |
| Quinten Post (MEM) | 80% | 12.3<br><sub>9,6,10,-,3</sub> | 4.5<br><sub>5,3,5,-,0</sub> |  | 2.4<br><sub>3,2,1,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.4<br><sub>0,1,0,-,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.4 |
| Jaden McDaniels (MIN) | 99% | 36.3<br><sub>31,37,39,36,34</sub> | 21.3<br><sub>13,22,17,25,34</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>6,5,3,5,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,4,1,4,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,2,4,1,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 1.1 | 2.4 | 31.5 |
| Ayo Dosunmu (MIN) | 99% | 35.0<br><sub>30,39,32,34,30</sub> | 22.7<br><sub>8,30,6,19,23</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,4,4,2,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>2,5,4,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,7,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.4 | 2.6 | 32.3 |
| Jonathan Kuminga (MIN) | 88% | 32.9<br><sub>29,-,35,37,26</sub> | 16.4<br><sub>13,-,23,16,15</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>9,-,3,4,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>1,-,3,2,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>1,-,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.8 | 2.2 | 25.6 |
| Rudy Gobert (MIN) | 99% | 32.6<br><sub>32,22,35,32,27</sub> | 10.9<br><sub>18,0,9,7,7</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 12.1<br><sub>15,4,7,11,6</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>3,2,0,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.8 | 1.7 | 25.4 |
| Terrence Shannon Jr. (MIN) | 98% | 27.7<br><sub>35,24,21,26,24</sub> | 17.1<br><sub>34,12,10,15,17</sub> |  | 3.5<br><sub>3,1,4,5,1</sub> |  | 3.6<br><sub>6,4,3,2,5</sub> |  | 1.7<br><sub>3,1,0,3,2</sub> |  | 0.8 | 0.2 | 1.7 | 24.1 |
| Trey Lyles (MIN) | 99% | 22.9<br><sub>19,31,16,12,24</sub> | 7.8<br><sub>9,8,8,3,9</sub> |  | 5.0<br><sub>3,7,6,3,3</sub> |  | 1.6<br><sub>1,4,1,1,2</sub> |  | 1.0<br><sub>2,2,2,1,0</sub> |  | 0.7 | 0.4 | 0.9 | 14.3 |
| Bones Hyland (MIN) | 98% | 21.0<br><sub>13,17,15,16,16</sub> | 12.8<br><sub>5,13,6,7,14</sub> |  | 2.3<br><sub>1,2,1,0,2</sub> |  | 4.2<br><sub>5,1,1,4,6</sub> |  | 2.0<br><sub>0,3,1,1,4</sub> |  | 0.9 | 0.3 | 1.4 | 19.2 |
| Joan Beringer (MIN) | 98% | 18.9<br><sub>16,26,13,16,19</sub> | 6.5<br><sub>0,3,5,0,0</sub> |  | 6.7<br><sub>4,13,3,4,4</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.8 | 0.8 | 13.7 |
| Zyon Pullin (MIN) | 52% | 9.5<br><sub>4,-,-,-,2</sub> | 3.8<br><sub>0,-,-,-,4</sub> |  | 1.3<br><sub>1,-,-,-,2</sub> |  | 1.3<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.4 |
| Cody Williams (MIN) | 58% | 8.4<br><sub>4,13,-,-,2</sub> | 0.1<br><sub>0,0,-,-,0</sub> |  | 1.1<br><sub>1,1,-,-,0</sub> |  | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 1.6 |
| Isaiah Evans (MIN) | 52% | 7.1<br><sub>4,-,-,-,2</sub> | 3.7<br><sub>0,-,-,-,2</sub> |  | 1.3<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.4 |
| Johni Broome (MIN) | 52% | 6.7<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |

</details>

<details><summary>if Zach Edey plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward (MEM) | 99% | 31.6<br><sub>27,33,25,30,30</sub> | 16.2<br><sub>18,20,19,23,16</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 7.6<br><sub>8,3,4,7,9</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>6,5,4,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,4,5,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.6 | 2.3 | 27.3 |
| Ty Jerome (MEM) | 98% | 31.1<br><sub>-,-,-,27,29</sub> | 23.7<br><sub>-,-,-,18,29</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>-,-,-,6,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>-,-,-,3,7</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 2.9 | 32.8 |
| Jaylen Wells (MEM) | 99% | 27.9<br><sub>27,26,24,25,20</sub> | 11.1<br><sub>8,5,22,8,8</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>4,4,7,1,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.2 | 0.9 | 15.7 |
| Cam Spencer (MEM) | 98% | 26.2<br><sub>32,29,27,30,21</sub> | 12.2<br><sub>12,26,9,9,24</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>6,1,2,5,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>9,7,11,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,5,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.4 | 21.0 |
| Zach Edey (MEM) | 100% | 24.6<br><sub>21,21,-,23,23</sub> | 10.0<br><sub>23,11,-,8,8</sub> | 7.5 · – | 8.7<br><sub>10,2,-,2,11</sub> | 7.5 | 1.2<br><sub>1,1,-,0,1</sub> | 1.5 | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.4 | 1.7 | 19.9 |
| Javon Small (MEM) | 98% | 24.2<br><sub>29,21,25,-,19</sub> | 10.9<br><sub>12,2,14,-,3</sub> |  | 3.7<br><sub>5,4,7,-,3</sub> |  | 4.3<br><sub>12,5,7,-,5</sub> |  | 1.3<br><sub>0,0,2,-,0</sub> |  | 0.9 | 0.3 | 1.6 | 18.9 |
| Taylor Hendricks (MEM) | 91% | 24.1<br><sub>19,21,20,27,24</sub> | 10.0<br><sub>9,18,11,5,3</sub> |  | 5.1<br><sub>3,6,1,7,4</sub> |  | 1.2<br><sub>0,2,1,2,1</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 1.0 | 0.6 | 1.2 | 16.3 |
| Kris Murray (MEM) | 91% | 21.2<br><sub>6,6,4,12,32</sub> | 4.8<br><sub>0,5,0,7,9</sub> | 6.5 · –<br><sub>o 42% · u 58%</sub> | 2.9<br><sub>1,0,1,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>0,0,0,0,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.4<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.4 | 0.7 | 8.9 |
| Olivier-Maxence Prosper (MEM) | 88% | 20.8<br><sub>16,16,24,23,19</sub> | 10.2<br><sub>12,5,16,7,6</sub> |  | 4.0<br><sub>0,2,5,6,3</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.9 | 0.3 | 1.0 | 15.2 |
| Jahmai Mashack (MEM) | 63% | 15.7<br><sub>2,13,26,22,-</sub> | 3.8<br><sub>0,3,0,0,-</sub> |  | 2.0<br><sub>0,2,3,2,-</sub> |  | 1.7<br><sub>1,2,4,1,-</sub> |  | 0.3<br><sub>0,1,0,0,-</sub> |  | 0.8 | 0.3 | 0.9 | 7.6 |
| Quinten Post (MEM) | 80% | 11.6<br><sub>9,6,10,-,3</sub> | 4.2<br><sub>5,3,5,-,0</sub> |  | 2.2<br><sub>3,2,1,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.4<br><sub>0,1,0,-,0</sub> |  | 0.3 | 0.3 | 0.6 | 6.8 |
| Jaden McDaniels (MIN) | 99% | 36.3<br><sub>31,37,39,36,34</sub> | 21.4<br><sub>13,22,17,25,34</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>6,5,3,5,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,4,1,4,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,2,4,1,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 1.1 | 2.4 | 31.6 |
| Ayo Dosunmu (MIN) | 99% | 35.0<br><sub>30,39,32,34,30</sub> | 22.8<br><sub>8,30,6,19,23</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,4,4,2,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>2,5,4,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,7,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.4 | 2.6 | 32.4 |
| Jonathan Kuminga (MIN) | 88% | 32.9<br><sub>29,-,35,37,26</sub> | 16.4<br><sub>13,-,23,16,15</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>9,-,3,4,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>1,-,3,2,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>1,-,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.8 | 2.2 | 25.5 |
| Rudy Gobert (MIN) | 99% | 32.6<br><sub>32,22,35,32,27</sub> | 10.9<br><sub>18,0,9,7,7</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 12.1<br><sub>15,4,7,11,6</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>3,2,0,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.8 | 1.7 | 25.3 |
| Terrence Shannon Jr. (MIN) | 98% | 27.7<br><sub>35,24,21,26,24</sub> | 17.1<br><sub>34,12,10,15,17</sub> |  | 3.5<br><sub>3,1,4,5,1</sub> |  | 3.6<br><sub>6,4,3,2,5</sub> |  | 1.7<br><sub>3,1,0,3,2</sub> |  | 0.8 | 0.1 | 1.7 | 24.1 |
| Trey Lyles (MIN) | 99% | 22.9<br><sub>19,31,16,12,24</sub> | 7.8<br><sub>9,8,8,3,9</sub> |  | 4.9<br><sub>3,7,6,3,3</sub> |  | 1.5<br><sub>1,4,1,1,2</sub> |  | 1.0<br><sub>2,2,2,1,0</sub> |  | 0.7 | 0.4 | 0.9 | 14.3 |
| Bones Hyland (MIN) | 98% | 21.0<br><sub>13,17,15,16,16</sub> | 12.8<br><sub>5,13,6,7,14</sub> |  | 2.3<br><sub>1,2,1,0,2</sub> |  | 4.2<br><sub>5,1,1,4,6</sub> |  | 2.0<br><sub>0,3,1,1,4</sub> |  | 0.9 | 0.3 | 1.4 | 19.2 |
| Joan Beringer (MIN) | 98% | 18.9<br><sub>16,26,13,16,19</sub> | 6.4<br><sub>0,3,5,0,0</sub> |  | 6.7<br><sub>4,13,3,4,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.8 | 0.8 | 13.6 |
| Zyon Pullin (MIN) | 52% | 9.5<br><sub>4,-,-,-,2</sub> | 3.8<br><sub>0,-,-,-,4</sub> |  | 1.3<br><sub>1,-,-,-,2</sub> |  | 1.3<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.4 |
| Cody Williams (MIN) | 58% | 8.4<br><sub>4,13,-,-,2</sub> | 0.1<br><sub>0,0,-,-,0</sub> |  | 1.1<br><sub>1,1,-,-,0</sub> |  | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 1.6 |
| Isaiah Evans (MIN) | 52% | 7.1<br><sub>4,-,-,-,2</sub> | 3.6<br><sub>0,-,-,-,2</sub> |  | 1.2<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.3 |
| Johni Broome (MIN) | 52% | 6.7<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.6 |

</details>


### DAL @ PHX
Out: Mark Williams (PHX), Sergio de Larrea (DAL), Dereck Lively II (DAL)

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 99% | 32.8<br><sub>27,34,36,31,31</sub> | 22.6<br><sub>17,33,22,28,24</sub> | 24.5 · –<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>3,5,6,3,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>4,9,8,4,12</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,3,3,3,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.7 | 2.9 | 34.8 |
| Kyrie Irving | 99% | 32.2<br><sub>-,29,35,27,34</sub> | 20.8<br><sub>-,17,25,16,11</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>-,6,6,1,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.4<br><sub>-,5,4,8,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>-,1,3,4,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.4 | 2.0 | 29.4 |
| P.J. Washington | 99% | 28.4<br><sub>25,25,-,-,25</sub> | 12.5<br><sub>8,21,-,-,14</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>5,5,-,-,6</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>4,2,-,-,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>0,5,-,-,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.8 | 1.5 | 20.1 |
| Daniel Gafford | 99% | 23.4<br><sub>19,24,31,28,27</sub> | 10.0<br><sub>3,6,10,10,13</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>4,6,10,4,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>2,2,3,4,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.2 | 17.9 |
| Naji Marshall | 97% | 22.5<br><sub>23,27,14,25,22</sub> | 10.4<br><sub>13,12,4,6,14</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,5,3,0,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>2,2,1,4,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>3,2,0,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.1 | 1.5 | 16.1 |
| Caleb Martin | 98% | 22.0<br><sub>34,20,20,29,30</sub> | 6.1<br><sub>12,8,0,13,13</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,4,6,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>5,3,3,4,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7<br><sub>4,2,0,3,3</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.3 | 0.8 | 11.5 |
| Zaccharie Risacher | 98% | 21.1<br><sub>27,18,29,28,21</sub> | 8.0<br><sub>18,3,11,15,12</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,3,7,8,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>0,0,1,2,1</sub> |  | 0.8<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.7 | 0.6 | 1.0 | 13.5 |
| Walter Clayton Jr. | 97% | 16.5<br><sub>23,27,25,21,14</sub> | 6.3<br><sub>13,8,16,9,5</sub> |  | 2.4<br><sub>4,2,5,0,2</sub> |  | 2.4<br><sub>3,7,1,3,2</sub> |  | 0.8<br><sub>3,2,2,2,1</sub> |  | 0.6 | 0.1 | 1.3 | 11.2 |
| Morez Johnson Jr. | 99% | 15.2<br><sub>26,15,17,20,19</sub> | 5.4<br><sub>2,3,9,7,9</sub> |  | 3.3<br><sub>6,1,7,6,10</sub> |  | 1.2<br><sub>4,1,2,2,1</sub> |  | 0.3<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.1 | 1.0 | 9.9 |
| Santi Aldama | 98% | 12.4<br><sub>-,6,9,16,10</sub> | 5.4<br><sub>-,0,0,9,3</sub> |  | 2.8<br><sub>-,0,1,4,1</sub> |  | 0.9<br><sub>-,0,0,1,0</sub> |  | 0.6<br><sub>-,0,0,1,1</sub> |  | 0.4 | 0.2 | 0.7 | 9.1 |
| Max Christie | 99% | 12.4<br><sub>-,8,24,16,4</sub> | 4.5<br><sub>-,5,13,3,2</sub> |  | 1.6<br><sub>-,1,4,2,1</sub> |  | 0.7<br><sub>-,2,0,0,0</sub> |  | 0.6<br><sub>-,1,3,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.7 |
| Marcus Sasser | 48% | 7.9<br><sub>18,4,-,-,-</sub> | 2.7<br><sub>5,0,-,-,-</sub> |  | 0.8<br><sub>1,2,-,-,-</sub> |  | 0.9<br><sub>2,1,-,-,-</sub> |  | 0.3<br><sub>1,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Moussa Cisse | 58% | 6.2<br><sub>4,4,-,-,2</sub> | 2.3<br><sub>1,0,-,-,0</sub> |  | 2.4<br><sub>1,1,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.4 | 0.4 | 4.8 |
| Jett Howard | 52% | 5.9<br><sub>7,-,-,-,-</sub> | 2.5<br><sub>0,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.6 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 99% | 36.0<br><sub>28,37,33,38,42</sub> | 26.3<br><sub>17,20,29,23,22</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,4,2,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 6.5<br><sub>7,8,6,3,8</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>0,1,2,1,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.3 | 3.1 | 36.6 |
| Dillon Brooks | 99% | 30.3<br><sub>22,27,31,25,34</sub> | 17.2<br><sub>1,15,29,18,16</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,4,3,3,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,4,5,3,7</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>0,3,5,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.2 | 1.5 | 23.6 |
| Miles Bridges | 99% | 29.6<br><sub>24,29,29,25,35</sub> | 14.7<br><sub>14,16,13,18,14</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>3,8,6,9,11</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>3,2,5,4,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.5 | 1.1 | 24.9 |
| Jalen Green | 98% | 29.0<br><sub>21,27,30,25,37</sub> | 16.6<br><sub>9,16,18,14,25</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>2,5,7,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>1,3,7,3,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>1,2,4,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 2.4 | 23.9 |
| Oso Ighodaro | 98% | 25.1<br><sub>17,33,21,27,30</sub> | 7.0<br><sub>4,8,7,3,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>2,11,4,7,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>3,3,2,3,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.3 | 16.3 |
| Collin Gillespie | 99% | 25.1<br><sub>28,26,17,27,30</sub> | 10.6<br><sub>26,10,9,16,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,3,3,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.9<br><sub>4,3,1,5,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>5,2,2,3,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.2 | 1.3 | 17.9 |
| Jordan Goodwin | 98% | 19.2<br><sub>31,20,17,28,18</sub> | 7.4<br><sub>14,11,2,5,6</sub> |  | 4.4<br><sub>7,6,5,9,2</sub> |  | 2.1<br><sub>6,2,3,4,2</sub> |  | 1.2<br><sub>1,1,0,1,2</sub> |  | 1.2 | 0.2 | 0.7 | 14.0 |
| Luke Kennard | 99% | 15.9<br><sub>23,17,17,15,14</sub> | 6.6<br><sub>18,12,3,5,4</sub> |  | 1.9<br><sub>6,2,3,0,1</sub> |  | 1.5<br><sub>4,0,1,0,2</sub> |  | 0.9<br><sub>3,4,1,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 10.0 |
| Khaman Maluach | 98% | 15.5<br><sub>13,11,21,18,16</sub> | 6.2<br><sub>7,4,10,9,8</sub> |  | 5.1<br><sub>4,6,2,6,6</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 0.9 | 12.0 |
| Ryan Dunn | 98% | 12.8<br><sub>24,12,13,9,9</sub> | 3.8<br><sub>3,5,6,0,3</sub> |  | 3.1<br><sub>6,1,5,5,2</sub> |  | 0.9<br><sub>1,0,2,0,0</sub> |  | 0.3<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.4 | 7.7 |
| Rasheer Fleming | 38% | 6.9<br><sub>-,-,4,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.1 |
| Jamaree Bouyea | 47% | 6.4<br><sub>-,-,4,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Pat Spencer | 48% | 6.4<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.3 |
| Koa Peat | 64% | 6.0<br><sub>8,1,4,3,-</sub> | 3.1<br><sub>10,0,2,0,-</sub> |  | 1.4<br><sub>2,1,0,0,-</sub> |  | 0.3<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.7 |
| Duop Reath | 38% | 6.0<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |
| Drew Timme | 5% | 5.9 | 2.5 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.3 | 4.2 |

</details>


### LAL @ SAS
Out: Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.7–112.4 | LAL 42% | 2.38 / 1.73 | SAS -2.5 | 221.5 | SAS -5.5 covers 43%; o224.5 44% |
| Expected (weighted by chance each plays) | 109.6–114.3 | LAL 37% | 2.70 / 1.59 | SAS -5.5 | 223.5 | SAS -5.5 covers 49%; o224.5 48% |
| if De'Aaron Fox plays | 109.4–114.5 | LAL 36% | 2.80 / 1.55 | SAS -5.5 | 223.5 | SAS -5.5 covers 49%; o224.5 48% |
| if Dylan Harper plays | 109.5–114.7 | LAL 35% | 2.83 / 1.55 | SAS -5.5 | 223.5 | SAS -5.5 covers 49%; o224.5 49% |
| if Austin Reaves plays | 110.2–112.8 | LAL 43% | 2.34 / 1.74 | SAS -2.5 | 222.5 | SAS -5.5 covers 42%; o224.5 46% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 29.6 | 13.7 | 3.5 | 6.2 | 1.2 | 1.4 | 0.3 | 2.6 | 23.4 | full tables below |
| Dylan Harper (SAS) | Questionable | 55% | 29.6 | 16.4 | 4.9 | 4.6 | 1.2 | 1.1 | 0.3 | 1.9 | 25.9 | full tables below |
| Austin Reaves (LAL) | Questionable | 55% | 31.1 | 18.4 | 3.6 | 4.0 | 1.7 | 0.9 | 0.3 | 2.7 | 26.0 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 99% | 36.2<br><sub>36,42,37,36,33</sub> | 33.4<br><sub>43,36,29,25,28</sub> | 33.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.5 | 4.5 | 47.7 |
| Walker Kessler | 99% | 30.9<br><sub>32,-,31,30,36</sub> | 12.2<br><sub>14,-,10,15,10</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 10.5<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.8 | 1.6 | 24.5 |
| Quentin Grimes | 99% | 30.8<br><sub>37,42,35,35,30</sub> | 12.5<br><sub>22,47,20,13,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.0<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.3 | 1.5 | 19.2 |
| Jake LaRavia | 98% | 27.2<br><sub>32,23,30,24,37</sub> | 7.1<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.5 | 1.1 | 13.4 |
| Matisse Thybulle | 98% | 24.8<br><sub>26,31,21,27,27</sub> | 6.9<br><sub>12,7,2,14,14</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,0,3,1,0</sub> |  | 1.1<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.1 | 0.8 | 1.0 | 10.9 |
| Collin Sexton | 99% | 21.2<br><sub>24,25,20,18,23</sub> | 12.3<br><sub>16,10,12,10,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>0,4,0,1,2</sub> |  | 2.5<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.2 | 1.7 | 16.9 |
| Ziaire Williams | 98% | 20.7<br><sub>19,24,18,28,19</sub> | 7.1<br><sub>6,0,7,5,9</sub> |  | 2.3<br><sub>2,1,2,0,4</sub> |  | 1.1<br><sub>3,1,0,1,0</sub> |  | 0.9<br><sub>0,0,1,1,2</sub> |  | 1.0 | 0.2 | 0.8 | 10.5 |
| Sandro Mamukelashvili | 99% | 18.3<br><sub>21,23,21,20,13</sub> | 7.4<br><sub>4,3,6,9,2</sub> |  | 3.9<br><sub>2,3,3,9,4</sub> |  | 1.3<br><sub>3,2,0,2,2</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.7 | 12.6 |
| Jarred Vanderbilt | 91% | 11.8<br><sub>12,14,12,10,12</sub> | 2.9<br><sub>2,4,0,4,1</sub> |  | 3.3<br><sub>4,7,5,4,2</sub> |  | 0.9<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.2 |
| AK Okereke | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Cameron Carr | 80% | 8.2<br><sub>-,-,2,12,10</sub> | 3.4<br><sub>-,-,5,5,9</sub> |  | 1.1<br><sub>-,-,0,1,0</sub> |  | 0.4<br><sub>-,-,1,0,0</sub> |  | 0.4<br><sub>-,-,1,1,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.9 |
| Kevon Looney | 36% | 7.7<br><sub>-,17,-,-,-</sub> | 1.6<br><sub>-,4,-,-,-</sub> |  | 2.7<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.2 | 4.8 |
| Carson Cooper | 52% | 6.8<br><sub>-,18,2,-,-</sub> | 2.1<br><sub>-,3,2,-,-</sub> |  | 1.9<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.3 | 4.5 |
| Jaden Hardy | 43% | 6.7<br><sub>-,-,2,-,-</sub> | 3.4<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Adou Thiero | 52% | 6.5<br><sub>-,6,6,-,-</sub> | 2.2<br><sub>-,0,0,-,-</sub> |  | 1.5<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.1 |
| Bronny James | 47% | 5.4<br><sub>-,-,2,-,-</sub> | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.4 |
| Chris Manon | 52% | 5.3<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.8 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephon Castle | 99% | 33.4<br><sub>35,31,33,29,37</sub> | 19.0<br><sub>20,10,21,19,28</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 8.2<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.6 | 32.5 |
| Devin Vassell | 99% | 33.4<br><sub>32,36,32,26,34</sub> | 15.0<br><sub>6,12,15,10,16</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>6,5,4,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.5<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.5 | 1.2 | 23.1 |
| Victor Wembanyama | 99% | 32.7<br><sub>35,34,33,32,-</sub> | 29.3<br><sub>26,25,32,50,-</sub> | 31.5 · –<br><sub>o 46% · u 54%</sub> | 12.3<br><sub>10,18,11,19,-</sub> | 12.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,4,3,1,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>4,1,2,5,-</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 3.5 | 3.1 | 45.8 |
| Julian Champagnie | 99% | 29.3<br><sub>24,30,29,25,30</sub> | 12.1<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>5,6,4,3,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>1,0,1,3,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.5 | 0.9 | 18.9 |
| Keldon Johnson | 99% | 25.7<br><sub>29,15,27,23,26</sub> | 11.1<br><sub>11,4,10,10,12</sub> |  | 5.2<br><sub>10,2,5,4,4</sub> |  | 2.5<br><sub>2,1,3,4,5</sub> |  | 0.8<br><sub>1,0,0,2,0</sub> |  | 0.7 | 0.2 | 1.2 | 18.8 |
| Harrison Barnes | 96% | 21.2<br><sub>14,10,16,21,26</sub> | 7.7<br><sub>0,0,9,3,9</sub> |  | 2.5<br><sub>0,3,2,5,2</sub> |  | 1.3<br><sub>2,4,1,2,2</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> |  | 0.4 | 0.1 | 0.7 | 11.4 |
| Luke Kornet | 99% | 20.6<br><sub>13,14,15,10,29</sub> | 5.5<br><sub>2,2,4,0,18</sub> |  | 6.0<br><sub>2,1,0,3,11</sub> |  | 1.6<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 0.7 | 13.0 |
| Jordan McLaughlin | 83% | 16.7<br><sub>19,-,11,18,14</sub> | 4.9<br><sub>10,-,0,0,6</sub> |  | 2.3<br><sub>1,-,1,3,2</sub> |  | 2.8<br><sub>2,-,5,2,0</sub> |  | 0.5<br><sub>2,-,0,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 10.0 |
| Ja'Kobi Gillespie | 91% | 14.2<br><sub>-,-,-,-,15</sub> | 4.5<br><sub>-,-,-,-,3</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.5 | 0.1 | 0.5 | 8.0 |
| Carter Bryant | 96% | 14.1<br><sub>5,2,13,20,12</sub> | 4.9<br><sub>0,0,3,8,0</sub> |  | 2.2<br><sub>1,0,1,3,3</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 0.6<br><sub>0,0,1,2,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.0 |
| Tarris Reed Jr. | 63% | 11.6<br><sub>-,-,-,6,15</sub> | 3.8<br><sub>-,-,-,0,7</sub> |  | 4.9<br><sub>-,-,-,4,7</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.6 | 0.8 | 9.3 |
| David Jones Garcia | 64% | 7.3<br><sub>-,-,-,4,2</sub> | 2.8<br><sub>-,-,-,0,2</sub> |  | 1.1<br><sub>-,-,-,1,0</sub> |  | 1.1<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.0 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 99% | 36.3<br><sub>36,42,37,36,33</sub> | 33.5<br><sub>43,36,29,25,28</sub> | 33.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.5 | 4.5 | 47.8 |
| Quentin Grimes (LAL) | 99% | 30.9<br><sub>37,42,35,35,30</sub> | 12.4<br><sub>22,47,20,13,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.0<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.3 | 1.5 | 19.2 |
| Walker Kessler (LAL) | 99% | 30.9<br><sub>32,-,31,30,36</sub> | 12.3<br><sub>14,-,10,15,10</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 10.6<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.8 | 1.6 | 24.6 |
| Jake LaRavia (LAL) | 98% | 27.1<br><sub>32,23,30,24,37</sub> | 7.2<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.5 | 1.1 | 13.4 |
| Matisse Thybulle (LAL) | 98% | 24.7<br><sub>26,31,21,27,27</sub> | 6.9<br><sub>12,7,2,14,14</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,0,3,1,0</sub> |  | 1.0<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.1 | 0.8 | 0.9 | 10.9 |
| Collin Sexton (LAL) | 99% | 21.2<br><sub>24,25,20,18,23</sub> | 12.3<br><sub>16,10,12,10,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>0,4,0,1,2</sub> |  | 2.5<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.2 | 1.7 | 16.9 |
| Ziaire Williams (LAL) | 98% | 20.7<br><sub>19,24,18,28,19</sub> | 7.1<br><sub>6,0,7,5,9</sub> |  | 2.3<br><sub>2,1,2,0,4</sub> |  | 1.1<br><sub>3,1,0,1,0</sub> |  | 0.9<br><sub>0,0,1,1,2</sub> |  | 1.0 | 0.2 | 0.7 | 10.5 |
| Sandro Mamukelashvili (LAL) | 99% | 18.3<br><sub>21,23,21,20,13</sub> | 7.5<br><sub>4,3,6,9,2</sub> |  | 3.9<br><sub>2,3,3,9,4</sub> |  | 1.3<br><sub>3,2,0,2,2</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.4 | 0.7 | 12.6 |
| Jarred Vanderbilt (LAL) | 91% | 11.8<br><sub>12,14,12,10,12</sub> | 3.0<br><sub>2,4,0,4,1</sub> |  | 3.3<br><sub>4,7,5,4,2</sub> |  | 0.9<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.2 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Cameron Carr (LAL) | 80% | 8.2<br><sub>-,-,2,12,10</sub> | 3.4<br><sub>-,-,5,5,9</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> |  | 0.4<br><sub>-,-,1,0,0</sub> |  | 0.3<br><sub>-,-,1,1,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.8 |
| Kevon Looney (LAL) | 36% | 7.8<br><sub>-,17,-,-,-</sub> | 1.6<br><sub>-,4,-,-,-</sub> |  | 2.7<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.2 | 4.9 |
| Carson Cooper (LAL) | 52% | 6.8<br><sub>-,18,2,-,-</sub> | 2.1<br><sub>-,3,2,-,-</sub> |  | 1.9<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.4 |
| Jaden Hardy (LAL) | 43% | 6.7<br><sub>-,-,2,-,-</sub> | 3.4<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.0 | 0.4 | 4.5 |
| Adou Thiero (LAL) | 52% | 6.6<br><sub>-,6,6,-,-</sub> | 2.3<br><sub>-,0,0,-,-</sub> |  | 1.5<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Bronny James (LAL) | 47% | 5.4<br><sub>-,-,2,-,-</sub> | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.4 |
| Chris Manon (LAL) | 52% | 5.3<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.8 |
| Victor Wembanyama (SAS) | 99% | 31.6<br><sub>35,34,33,32,-</sub> | 28.4<br><sub>26,25,32,50,-</sub> | 31.5 · –<br><sub>o 46% · u 54%</sub> | 12.3<br><sub>10,18,11,19,-</sub> | 12.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>6,4,3,1,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>4,1,2,5,-</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 3.4 | 2.8 | 44.0 |
| Stephon Castle (SAS) | 99% | 31.2<br><sub>35,31,33,29,37</sub> | 17.4<br><sub>20,10,21,19,28</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 7.3<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 3.3 | 29.7 |
| Devin Vassell (SAS) | 99% | 31.1<br><sub>32,36,32,26,34</sub> | 13.2<br><sub>6,12,15,10,16</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>6,5,4,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.4 | 1.1 | 20.4 |
| De'Aaron Fox (SAS) | 100% | 29.6<br><sub>-,34,32,26,-</sub> | 13.7<br><sub>-,6,10,5,-</sub> | 13.5 · – | 3.5<br><sub>-,2,2,2,-</sub> | 3.5 | 6.2<br><sub>-,2,5,10,-</sub> | 5.5 | 1.2<br><sub>-,0,0,0,-</sub> | 1.5 | 1.4 | 0.3 | 2.6 | 23.4 |
| Julian Champagnie (SAS) | 99% | 27.2<br><sub>24,30,29,25,30</sub> | 11.4<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>5,6,4,3,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>1,0,1,3,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.5 | 0.8 | 17.6 |
| Keldon Johnson (SAS) | 99% | 23.5<br><sub>29,15,27,23,26</sub> | 9.9<br><sub>11,4,10,10,12</sub> |  | 4.9<br><sub>10,2,5,4,4</sub> |  | 2.1<br><sub>2,1,3,4,5</sub> |  | 0.8<br><sub>1,0,0,2,0</sub> |  | 0.7 | 0.2 | 1.1 | 16.9 |
| Harrison Barnes (SAS) | 96% | 17.3<br><sub>14,10,16,21,26</sub> | 6.4<br><sub>0,0,9,3,9</sub> |  | 2.1<br><sub>0,3,2,5,2</sub> |  | 1.0<br><sub>2,4,1,2,2</sub> |  | 0.9<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.1 | 0.6 | 9.5 |
| Luke Kornet (SAS) | 99% | 16.8<br><sub>13,14,15,10,29</sub> | 4.6<br><sub>2,2,4,0,18</sub> |  | 4.9<br><sub>2,1,0,3,11</sub> |  | 1.3<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.6 | 10.8 |
| Jordan McLaughlin (SAS) | 83% | 12.9<br><sub>19,-,11,18,14</sub> | 3.8<br><sub>10,-,0,0,6</sub> |  | 1.7<br><sub>1,-,1,3,2</sub> |  | 2.1<br><sub>2,-,5,2,0</sub> |  | 0.4<br><sub>2,-,0,0,0</sub> |  | 0.9 | 0.1 | 0.7 | 7.7 |
| Carter Bryant (SAS) | 96% | 11.5<br><sub>5,2,13,20,12</sub> | 4.1<br><sub>0,0,3,8,0</sub> |  | 1.8<br><sub>1,0,1,3,3</sub> |  | 0.7<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>0,0,1,2,0</sub> |  | 0.2 | 0.2 | 0.5 | 6.6 |
| Ja'Kobi Gillespie (SAS) | 91% | 10.1<br><sub>-,-,-,-,15</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,4</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.1 | 0.4 | 6.0 |
| Tarris Reed Jr. (SAS) | 63% | 9.0<br><sub>-,-,-,6,15</sub> | 3.1<br><sub>-,-,-,0,7</sub> |  | 3.8<br><sub>-,-,-,4,7</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.3 |
| David Jones Garcia (SAS) | 64% | 5.9<br><sub>-,-,-,4,2</sub> | 2.3<br><sub>-,-,-,0,2</sub> |  | 0.9<br><sub>-,-,-,1,0</sub> |  | 0.9<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>if Austin Reaves plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 99% | 34.6<br><sub>36,42,37,36,33</sub> | 29.4<br><sub>43,36,29,25,28</sub> | 33.5 · –<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.5 | 4.0 | 42.7 |
| Austin Reaves (LAL) | 100% | 31.1<br><sub>-,-,-,-,-</sub> | 18.4<br><sub>-,-,-,-,-</sub> | 17.5 · – | 3.6<br><sub>-,-,-,-,-</sub> | 2.5 | 4.0<br><sub>-,-,-,-,-</sub> | 3.5 | 1.7<br><sub>-,-,-,-,-</sub> | 1.5 | 0.9 | 0.3 | 2.7 | 26.0 |
| Walker Kessler (LAL) | 99% | 28.1<br><sub>32,-,31,30,36</sub> | 10.9<br><sub>14,-,10,15,10</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 9.6<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.5 | 22.0 |
| Quentin Grimes (LAL) | 99% | 26.9<br><sub>37,42,35,35,30</sub> | 10.1<br><sub>22,47,20,13,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.5<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.3 | 1.4 | 15.9 |
| Jake LaRavia (LAL) | 98% | 23.1<br><sub>32,23,30,24,37</sub> | 5.7<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.4 | 0.9 | 11.0 |
| Matisse Thybulle (LAL) | 98% | 21.0<br><sub>26,31,21,27,27</sub> | 5.7<br><sub>12,7,2,14,14</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.7 | 0.8 | 9.1 |
| Ziaire Williams (LAL) | 98% | 18.0<br><sub>19,24,18,28,19</sub> | 6.0<br><sub>6,0,7,5,9</sub> |  | 2.0<br><sub>2,1,2,0,4</sub> |  | 0.9<br><sub>3,1,0,1,0</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.6 | 9.0 |
| Collin Sexton (LAL) | 99% | 17.7<br><sub>24,25,20,18,23</sub> | 9.7<br><sub>16,10,12,10,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.0<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.7 | 0.1 | 1.4 | 13.4 |
| Sandro Mamukelashvili (LAL) | 99% | 15.8<br><sub>21,23,21,20,13</sub> | 6.1<br><sub>4,3,6,9,2</sub> |  | 3.4<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.6 |
| Jarred Vanderbilt (LAL) | 91% | 9.1<br><sub>12,14,12,10,12</sub> | 2.5<br><sub>2,4,0,4,1</sub> |  | 2.5<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.8 |
| Arthur Kaluma (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| AK Okereke (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Kevon Looney (LAL) | 36% | 6.7<br><sub>-,17,-,-,-</sub> | 1.4<br><sub>-,4,-,-,-</sub> |  | 2.3<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.3 |
| Cameron Carr (LAL) | 80% | 6.2<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Carson Cooper (LAL) | 52% | 6.0<br><sub>-,18,2,-,-</sub> | 1.9<br><sub>-,3,2,-,-</sub> |  | 1.6<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 3.9 |
| Jaden Hardy (LAL) | 43% | 6.0<br><sub>-,-,2,-,-</sub> | 3.4<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.5 |
| Adou Thiero (LAL) | 52% | 5.8<br><sub>-,6,6,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Bronny James (LAL) | 47% | 5.2<br><sub>-,-,2,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 2.7 |
| Chris Manon (LAL) | 52% | 5.1<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.8 |
| Stephon Castle (SAS) | 99% | 33.4<br><sub>35,31,33,29,37</sub> | 19.0<br><sub>20,10,21,19,28</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 8.2<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.6 | 32.5 |
| Devin Vassell (SAS) | 99% | 33.3<br><sub>32,36,32,26,34</sub> | 15.2<br><sub>6,12,15,10,16</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>6,5,4,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.5<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.5 | 1.2 | 23.2 |
| Victor Wembanyama (SAS) | 99% | 32.7<br><sub>35,34,33,32,-</sub> | 29.2<br><sub>26,25,32,50,-</sub> | 31.5 · –<br><sub>o 46% · u 54%</sub> | 12.4<br><sub>10,18,11,19,-</sub> | 12.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,4,3,1,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>4,1,2,5,-</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 3.5 | 3.1 | 45.9 |
| Julian Champagnie (SAS) | 99% | 29.4<br><sub>24,30,29,25,30</sub> | 12.1<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>5,6,4,3,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>1,0,1,3,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.5 | 0.9 | 18.9 |
| Keldon Johnson (SAS) | 99% | 25.7<br><sub>29,15,27,23,26</sub> | 11.2<br><sub>11,4,10,10,12</sub> |  | 5.2<br><sub>10,2,5,4,4</sub> |  | 2.5<br><sub>2,1,3,4,5</sub> |  | 0.8<br><sub>1,0,0,2,0</sub> |  | 0.7 | 0.2 | 1.2 | 18.8 |
| Harrison Barnes (SAS) | 96% | 21.2<br><sub>14,10,16,21,26</sub> | 7.7<br><sub>0,0,9,3,9</sub> |  | 2.5<br><sub>0,3,2,5,2</sub> |  | 1.3<br><sub>2,4,1,2,2</sub> |  | 1.1<br><sub>0,0,1,0,1</sub> |  | 0.4 | 0.1 | 0.7 | 11.4 |
| Luke Kornet (SAS) | 99% | 20.5<br><sub>13,14,15,10,29</sub> | 5.4<br><sub>2,2,4,0,18</sub> |  | 5.9<br><sub>2,1,0,3,11</sub> |  | 1.6<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 0.7 | 13.0 |
| Jordan McLaughlin (SAS) | 83% | 16.7<br><sub>19,-,11,18,14</sub> | 5.0<br><sub>10,-,0,0,6</sub> |  | 2.3<br><sub>1,-,1,3,2</sub> |  | 2.8<br><sub>2,-,5,2,0</sub> |  | 0.5<br><sub>2,-,0,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 10.1 |
| Carter Bryant (SAS) | 96% | 14.1<br><sub>5,2,13,20,12</sub> | 4.8<br><sub>0,0,3,8,0</sub> |  | 2.2<br><sub>1,0,1,3,3</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 0.6<br><sub>0,0,1,2,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.9 |
| Ja'Kobi Gillespie (SAS) | 91% | 14.0<br><sub>-,-,-,-,15</sub> | 4.5<br><sub>-,-,-,-,3</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.5 | 0.1 | 0.5 | 8.0 |
| Tarris Reed Jr. (SAS) | 63% | 11.7<br><sub>-,-,-,6,15</sub> | 3.8<br><sub>-,-,-,0,7</sub> |  | 4.9<br><sub>-,-,-,4,7</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.6 | 0.8 | 9.4 |
| David Jones Garcia (SAS) | 64% | 7.3<br><sub>-,-,-,4,2</sub> | 2.8<br><sub>-,-,-,0,2</sub> |  | 1.1<br><sub>-,-,-,1,0</sub> |  | 1.1<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.0 |

</details>

<details><summary>if Dylan Harper plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 99% | 36.3<br><sub>36,42,37,36,33</sub> | 33.4<br><sub>43,36,29,25,28</sub> | 33.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.5 | 4.6 | 47.8 |
| Quentin Grimes (LAL) | 99% | 30.9<br><sub>37,42,35,35,30</sub> | 12.5<br><sub>22,47,20,13,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.0<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.3 | 1.5 | 19.2 |
| Walker Kessler (LAL) | 99% | 30.8<br><sub>32,-,31,30,36</sub> | 12.2<br><sub>14,-,10,15,10</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 10.5<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.8 | 1.6 | 24.4 |
| Jake LaRavia (LAL) | 98% | 27.2<br><sub>32,23,30,24,37</sub> | 7.2<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.5 | 1.1 | 13.4 |
| Matisse Thybulle (LAL) | 98% | 24.8<br><sub>26,31,21,27,27</sub> | 6.9<br><sub>12,7,2,14,14</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,0,3,1,0</sub> |  | 1.0<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.1 | 0.8 | 0.9 | 10.9 |
| Collin Sexton (LAL) | 99% | 21.3<br><sub>24,25,20,18,23</sub> | 12.2<br><sub>16,10,12,10,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>0,4,0,1,2</sub> |  | 2.5<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.2 | 1.7 | 16.9 |
| Ziaire Williams (LAL) | 98% | 20.7<br><sub>19,24,18,28,19</sub> | 7.1<br><sub>6,0,7,5,9</sub> |  | 2.3<br><sub>2,1,2,0,4</sub> |  | 1.1<br><sub>3,1,0,1,0</sub> |  | 0.9<br><sub>0,0,1,1,2</sub> |  | 1.0 | 0.2 | 0.8 | 10.5 |
| Sandro Mamukelashvili (LAL) | 99% | 18.4<br><sub>21,23,21,20,13</sub> | 7.5<br><sub>4,3,6,9,2</sub> |  | 3.9<br><sub>2,3,3,9,4</sub> |  | 1.3<br><sub>3,2,0,2,2</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.4 | 0.7 | 12.7 |
| Jarred Vanderbilt (LAL) | 91% | 11.8<br><sub>12,14,12,10,12</sub> | 3.0<br><sub>2,4,0,4,1</sub> |  | 3.3<br><sub>4,7,5,4,2</sub> |  | 0.9<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.2 |
| AK Okereke (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Cameron Carr (LAL) | 80% | 8.2<br><sub>-,-,2,12,10</sub> | 3.4<br><sub>-,-,5,5,9</sub> |  | 1.1<br><sub>-,-,0,1,0</sub> |  | 0.4<br><sub>-,-,1,0,0</sub> |  | 0.3<br><sub>-,-,1,1,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.9 |
| Kevon Looney (LAL) | 36% | 7.7<br><sub>-,17,-,-,-</sub> | 1.6<br><sub>-,4,-,-,-</sub> |  | 2.7<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.2 | 4.8 |
| Carson Cooper (LAL) | 52% | 6.8<br><sub>-,18,2,-,-</sub> | 2.2<br><sub>-,3,2,-,-</sub> |  | 1.8<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.5 |
| Jaden Hardy (LAL) | 43% | 6.7<br><sub>-,-,2,-,-</sub> | 3.4<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Adou Thiero (LAL) | 52% | 6.5<br><sub>-,6,6,-,-</sub> | 2.2<br><sub>-,0,0,-,-</sub> |  | 1.5<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Bronny James (LAL) | 47% | 5.5<br><sub>-,-,2,-,-</sub> | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.5 |
| Chris Manon (LAL) | 52% | 5.3<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.8 |
| Victor Wembanyama (SAS) | 99% | 30.9<br><sub>35,34,33,32,-</sub> | 27.2<br><sub>26,25,32,50,-</sub> | 31.5 · –<br><sub>o 46% · u 54%</sub> | 11.9<br><sub>10,18,11,19,-</sub> | 12.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>6,4,3,1,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>4,1,2,5,-</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 3.2 | 2.7 | 42.5 |
| Stephon Castle (SAS) | 99% | 30.8<br><sub>35,31,33,29,37</sub> | 17.1<br><sub>20,10,21,19,28</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 7.5<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.1 | 29.5 |
| Devin Vassell (SAS) | 99% | 30.5<br><sub>32,36,32,26,34</sub> | 12.8<br><sub>6,12,15,10,16</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>6,5,4,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.4 | 1.1 | 19.9 |
| Dylan Harper (SAS) | 100% | 29.6<br><sub>34,35,-,-,-</sub> | 16.4<br><sub>31,20,-,-,-</sub> |  | 4.9<br><sub>9,4,-,-,-</sub> |  | 4.6<br><sub>4,2,-,-,-</sub> |  | 1.2<br><sub>2,0,-,-,-</sub> |  | 1.1 | 0.3 | 1.9 | 25.9 |
| Julian Champagnie (SAS) | 99% | 26.8<br><sub>24,30,29,25,30</sub> | 11.1<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,6,4,3,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>1,0,1,3,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.4 | 0.9 | 17.2 |
| Keldon Johnson (SAS) | 99% | 23.1<br><sub>29,15,27,23,26</sub> | 9.7<br><sub>11,4,10,10,12</sub> |  | 4.7<br><sub>10,2,5,4,4</sub> |  | 2.0<br><sub>2,1,3,4,5</sub> |  | 0.8<br><sub>1,0,0,2,0</sub> |  | 0.7 | 0.2 | 1.1 | 16.4 |
| Harrison Barnes (SAS) | 96% | 17.3<br><sub>14,10,16,21,26</sub> | 6.3<br><sub>0,0,9,3,9</sub> |  | 2.0<br><sub>0,3,2,5,2</sub> |  | 1.1<br><sub>2,4,1,2,2</sub> |  | 0.8<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.1 | 0.6 | 9.4 |
| Luke Kornet (SAS) | 99% | 16.4<br><sub>13,14,15,10,29</sub> | 4.5<br><sub>2,2,4,0,18</sub> |  | 4.8<br><sub>2,1,0,3,11</sub> |  | 1.3<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 10.5 |
| Jordan McLaughlin (SAS) | 83% | 12.9<br><sub>19,-,11,18,14</sub> | 3.8<br><sub>10,-,0,0,6</sub> |  | 1.7<br><sub>1,-,1,3,2</sub> |  | 2.2<br><sub>2,-,5,2,0</sub> |  | 0.3<br><sub>2,-,0,0,0</sub> |  | 0.9 | 0.1 | 0.7 | 7.7 |
| Carter Bryant (SAS) | 96% | 11.2<br><sub>5,2,13,20,12</sub> | 4.0<br><sub>0,0,3,8,0</sub> |  | 1.7<br><sub>1,0,1,3,3</sub> |  | 0.7<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>0,0,1,2,0</sub> |  | 0.2 | 0.2 | 0.5 | 6.5 |
| Ja'Kobi Gillespie (SAS) | 91% | 9.9<br><sub>-,-,-,-,15</sub> | 3.4<br><sub>-,-,-,-,3</sub> |  | 1.2<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,4</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.9 |
| Tarris Reed Jr. (SAS) | 63% | 8.8<br><sub>-,-,-,6,15</sub> | 3.0<br><sub>-,-,-,0,7</sub> |  | 3.6<br><sub>-,-,-,4,7</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.1 |
| David Jones Garcia (SAS) | 64% | 5.9<br><sub>-,-,-,4,2</sub> | 2.3<br><sub>-,-,-,0,2</sub> |  | 1.0<br><sub>-,-,-,1,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 4.2 |

</details>


### DEN @ UTA
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Bryce Hopkins (DEN), Cam Whitmore (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 124.0–114.9 | DEN 74% | 1.35 / 3.84 | UTA +8.5 | 238.5 | UTA +10.5 covers 54%; o229.5 69% |
| Expected (weighted by chance each plays) | 123.2–115.3 | DEN 71% | 1.41 / 3.44 | UTA +7.5 | 238.5 | UTA +10.5 covers 58%; o229.5 68% |
| if Jaxson Hayes plays | 122.6–116.1 | DEN 68% | 1.48 / 3.09 | UTA +6.5 | 238.5 | UTA +10.5 covers 61%; o229.5 69% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jusuf Nurkic (UTA) | Questionable | 55% | 18.7 | 8.4 | 7.2 | 3.6 | 0.5 | 0.9 | 0.5 | 1.5 | 19.1 | small |
| Jaxson Hayes (UTA) | Questionable | 55% | 20.2 | 8.3 | 5.3 | 1.2 | 0.0 | 0.6 | 0.8 | 0.8 | 14.8 | full tables below |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.8<br><sub>28,24,26,37,18</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.2 | 49.9 |
| Jamal Murray | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 25.9<br><sub>28,21,14,45,20</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.7 | 2.2 | 36.5 |
| Christian Braun | 99% | 32.3<br><sub>33,35,31,38,29</sub> | 13.8<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.5 | 1.0 | 21.4 |
| Cameron Johnson | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.2<br><sub>9,8,19,16,17</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.0 | 20.8 |
| Aaron Gordon | 99% | 29.2<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>1,8,3,8,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.5 | 1.1 | 21.3 |
| DeMar DeRozan | 96% | 19.3<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> |  | 2.6<br><sub>3,2,1,4,3</sub> |  | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.5 |
| Marvin Bagley III | 99% | 12.1<br><sub>10,9,10,11,12</sub> | 6.1<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.5 |
| Tyus Jones | 98% | 10.8<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.8<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.6 |
| Julian Strawther | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.4 |
| Zeke Nnaji | 38% | 6.8<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.3 |
| Alpha Diallo | 48% | 6.2<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Ryan Nembhard | 38% | 6.0<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 34.7<br><sub>35,39,36,26,33</sub> | 21.2<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 32.3 |
| Ace Bailey | 99% | 33.0<br><sub>23,27,24,33,33</sub> | 16.2<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.9 | 1.7 | 24.4 |
| Darryn Peterson | 99% | 32.3<br><sub>31,19,32,25,29</sub> | 17.0<br><sub>13,11,20,6,13</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.5 | 2.0 | 26.6 |
| Mo Bamba | 93% | 25.8<br><sub>31,23,20,23,29</sub> | 9.0<br><sub>15,6,2,6,6</sub> |  | 8.7<br><sub>10,16,2,10,7</sub> |  | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.6 | 1.5 | 1.1 | 19.0 |
| Svi Mykhailiuk | 98% | 25.6<br><sub>33,34,28,32,25</sub> | 11.4<br><sub>8,15,11,39,4</sub> |  | 3.1<br><sub>7,3,7,5,3</sub> |  | 2.2<br><sub>5,5,2,3,2</sub> |  | 1.9<br><sub>2,4,3,10,0</sub> |  | 0.6 | 0.1 | 1.0 | 16.8 |
| Josh Green | 98% | 23.4<br><sub>13,28,29,23,19</sub> | 5.9<br><sub>9,11,8,0,8</sub> |  | 2.3<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>1,2,2,0,2</sub> |  | 0.7 | 0.3 | 0.6 | 9.5 |
| Brice Sensabaugh | 99% | 22.2<br><sub>35,14,26,17,17</sub> | 14.1<br><sub>40,8,18,10,6</sub> |  | 3.8<br><sub>11,3,3,3,4</sub> |  | 2.0<br><sub>5,2,1,2,1</sub> |  | 2.0<br><sub>8,0,5,2,0</sub> |  | 0.6 | 0.2 | 1.6 | 19.9 |
| Josh Okogie | 98% | 18.4<br><sub>22,15,17,14,9</sub> | 5.4<br><sub>9,3,3,1,0</sub> |  | 2.8<br><sub>2,0,2,4,0</sub> |  | 1.0<br><sub>4,0,2,0,0</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.2 | 0.7 | 9.2 |
| Kyle Filipowski | 64% | 17.9<br><sub>-,6,-,9,24</sub> | 9.9<br><sub>-,0,-,2,21</sub> |  | 5.8<br><sub>-,3,-,4,12</sub> |  | 2.2<br><sub>-,0,-,3,4</sub> |  | 0.8<br><sub>-,0,-,0,1</sub> |  | 0.7 | 0.3 | 1.2 | 17.9 |
| Isaiah Collier | 67% | 17.8<br><sub>-,10,-,13,18</sub> | 8.6<br><sub>-,0,-,10,4</sub> |  | 2.4<br><sub>-,1,-,2,2</sub> |  | 4.6<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.7 | 0.2 | 1.4 | 15.5 |
| Tony Bradley | 52% | 11.8<br><sub>17,-,-,13,-</sub> | 3.4<br><sub>3,-,-,1,-</sub> |  | 3.6<br><sub>7,-,-,5,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 7.6 |

</details>

<details><summary>if Jaxson Hayes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.8<br><sub>28,24,26,37,18</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.2 | 49.9 |
| Jamal Murray (DEN) | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 25.9<br><sub>28,21,14,45,20</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.7 | 2.2 | 36.4 |
| Christian Braun (DEN) | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.8<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.5 | 1.0 | 21.4 |
| Cameron Johnson (DEN) | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.2<br><sub>9,8,19,16,17</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.0 | 20.8 |
| Aaron Gordon (DEN) | 99% | 29.2<br><sub>24,31,31,33,24</sub> | 13.3<br><sub>11,13,18,18,1</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>1,8,3,8,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.5 | 1.1 | 21.3 |
| DeMar DeRozan (DEN) | 96% | 19.5<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.5<br><sub>1,2,2,1,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones (DEN) | 91% | 17.1<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> |  | 2.6<br><sub>3,2,1,4,3</sub> |  | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile (DEN) | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.5 |
| Marvin Bagley III (DEN) | 99% | 12.2<br><sub>10,9,10,11,12</sub> | 6.2<br><sub>4,4,10,2,9</sub> |  | 3.8<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.6 |
| Tyus Jones (DEN) | 98% | 10.9<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Julian Strawther (DEN) | 38% | 9.1<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.4 |
| Zeke Nnaji (DEN) | 38% | 6.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.3 | 4.3 |
| Alpha Diallo (DEN) | 48% | 6.2<br><sub>-,-,-,-,3</sub> | 2.2<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.8 |
| Ryan Nembhard (DEN) | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |
| Keyonte George (UTA) | 99% | 34.6<br><sub>35,39,36,26,33</sub> | 21.3<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 3.0 | 32.5 |
| Ace Bailey (UTA) | 99% | 32.0<br><sub>23,27,24,33,33</sub> | 16.1<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.8 | 1.7 | 24.0 |
| Darryn Peterson (UTA) | 99% | 31.2<br><sub>31,19,32,25,29</sub> | 16.2<br><sub>13,11,20,6,13</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,3,8,5,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.6 | 1.9 | 25.4 |
| Svi Mykhailiuk (UTA) | 98% | 23.4<br><sub>33,34,28,32,25</sub> | 10.4<br><sub>8,15,11,39,4</sub> |  | 2.8<br><sub>7,3,7,5,3</sub> |  | 2.1<br><sub>5,5,2,3,2</sub> |  | 1.7<br><sub>2,4,3,10,0</sub> |  | 0.6 | 0.1 | 0.9 | 15.3 |
| Mo Bamba (UTA) | 93% | 23.3<br><sub>31,23,20,23,29</sub> | 8.1<br><sub>15,6,2,6,6</sub> |  | 7.9<br><sub>10,16,2,10,7</sub> |  | 1.3<br><sub>3,0,0,1,2</sub> |  | 0.5<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.4 | 0.9 | 17.4 |
| Josh Green (UTA) | 98% | 20.2<br><sub>13,28,29,23,19</sub> | 5.0<br><sub>9,11,8,0,8</sub> |  | 2.0<br><sub>1,2,4,1,2</sub> |  | 1.1<br><sub>0,2,0,0,1</sub> |  | 0.7<br><sub>1,2,2,0,2</sub> |  | 0.6 | 0.2 | 0.6 | 8.1 |
| Jaxson Hayes (UTA) | 100% | 20.2<br><sub>-,25,28,12,-</sub> | 8.3<br><sub>-,6,18,8,-</sub> | 9.5 · – | 5.3<br><sub>-,7,14,3,-</sub> | 5.5 | 1.2<br><sub>-,2,0,1,-</sub> | 1.5 | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.8 | 14.8 |
| Brice Sensabaugh (UTA) | 99% | 19.6<br><sub>35,14,26,17,17</sub> | 12.7<br><sub>40,8,18,10,6</sub> |  | 3.2<br><sub>11,3,3,3,4</sub> |  | 1.8<br><sub>5,2,1,2,1</sub> |  | 1.7<br><sub>8,0,5,2,0</sub> |  | 0.5 | 0.2 | 1.5 | 17.6 |
| Isaiah Collier (UTA) | 67% | 16.4<br><sub>-,10,-,13,18</sub> | 7.9<br><sub>-,0,-,10,4</sub> |  | 2.3<br><sub>-,1,-,2,2</sub> |  | 4.3<br><sub>-,2,-,7,1</sub> |  | 0.3<br><sub>-,0,-,1,0</sub> |  | 0.6 | 0.2 | 1.4 | 14.5 |
| Josh Okogie (UTA) | 98% | 15.2<br><sub>22,15,17,14,9</sub> | 4.5<br><sub>9,3,3,1,0</sub> |  | 2.4<br><sub>2,0,2,4,0</sub> |  | 0.9<br><sub>4,0,2,0,0</sub> |  | 0.4<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 7.7 |
| Kyle Filipowski (UTA) | 64% | 14.7<br><sub>-,6,-,9,24</sub> | 8.6<br><sub>-,0,-,2,21</sub> |  | 4.8<br><sub>-,3,-,4,12</sub> |  | 1.8<br><sub>-,0,-,3,4</sub> |  | 0.6<br><sub>-,0,-,0,1</sub> |  | 0.6 | 0.3 | 1.0 | 15.2 |
| Tony Bradley (UTA) | 52% | 8.8<br><sub>17,-,-,13,-</sub> | 2.6<br><sub>3,-,-,1,-</sub> |  | 2.7<br><sub>7,-,-,5,-</sub> |  | 0.5<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>


### NOP @ LAC
Out: Bradley Beal (LAC), Dejounte Murray (NOP), Jaron Pierre Jr. (NOP)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.7–118.4 | NOP 31% | 3.18 / 1.46 | LAC -6.5 | 230.5 | LAC -3.5 covers 60%; o231.5 47% |
| Expected (weighted by chance each plays) | 111.9–118.9 | NOP 31% | 3.19 / 1.46 | LAC -7.5 | 230.5 | LAC -3.5 covers 60%; o231.5 48% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cam Christie (LAC) | Questionable | 55% | 5.7 | 2.6 | 0.9 | 0.5 | 0.1 | 0.2 | 0.1 | 0.3 | 4.0 | small |
| Jalen Pickett (LAC) | Questionable | 55% | 5.9 | 2.3 | 0.8 | 0.9 | 0.2 | 0.2 | 0.1 | 0.3 | 4.0 | small |
| Nick Martinelli (LAC) | Questionable | 55% | 6.1 | 2.6 | 1.5 | 0.5 | 0.2 | 0.2 | 0.2 | 0.3 | 4.5 | small |
| Bennedict Mathurin (NOP) | Doubtful | 20% | 11.0 | 4.9 | 1.8 | 0.9 | 0.3 | 0.3 | 0.1 | 0.7 | 7.6 | small |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 99% | 32.3<br><sub>33,42,37,32,40</sub> | 15.9<br><sub>23,10,21,2,21</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>6,8,6,5,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>3,6,3,2,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>5,2,4,0,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 1.1 | 23.6 |
| Jeremiah Fears | 99% | 32.0<br><sub>29,31,38,34,40</sub> | 17.7<br><sub>19,16,22,29,7</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>10,5,7,5,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.2<br><sub>10,4,5,4,11</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.4 | 3.2 | 28.7 |
| Trey Murphy III | 98% | 32.0<br><sub>-,-,29,-,35</sub> | 16.0<br><sub>-,-,17,-,9</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>-,-,4,-,9</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>-,-,1,-,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.4<br><sub>-,-,3,-,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 1.5 | 24.5 |
| Zion Williamson | 84% | 31.9<br><sub>25,32,37,-,40</sub> | 20.5<br><sub>16,24,22,-,25</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>6,7,6,-,4</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>2,1,7,-,0</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.2<br><sub>0,0,0,-,0</sub> |  | 1.4 | 0.5 | 2.3 | 29.6 |
| Herbert Jones | 99% | 23.2<br><sub>24,32,33,25,21</sub> | 7.0<br><sub>8,9,14,2,7</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>3,3,3,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9<br><sub>2,3,4,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.2 | 0.4 | 1.2 | 11.9 |
| Jordan Poole | 91% | 23.2<br><sub>31,30,13,31,27</sub> | 12.5<br><sub>11,22,6,25,28</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,1,0,3,0</sub> |  | 3.3<br><sub>5,5,1,2,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>1,3,2,3,6</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 1.8 | 17.8 |
| Derik Queen | 99% | 22.0<br><sub>21,19,18,35,21</sub> | 11.1<br><sub>17,9,11,15,11</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>10,5,7,15,9</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,0,3,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.4<br><sub>4,0,0,0,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 1.0 | 0.6 | 2.1 | 20.2 |
| Yves Missi | 98% | 19.4<br><sub>23,17,23,35,22</sub> | 5.7<br><sub>6,4,4,9,4</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 6.1<br><sub>14,5,7,13,8</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,2,0,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.9 | 13.1 |
| Karlo Matkovic | 98% | 13.4<br><sub>20,10,8,15,13</sub> | 4.7<br><sub>3,0,0,3,5</sub> |  | 3.1<br><sub>2,2,2,3,4</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.5<br><sub>0,0,0,1,1</sub> |  | 0.4 | 0.5 | 0.7 | 8.5 |
| Trendon Watford | 74% | 11.2<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.8 | 7.5 |
| Bryce McGowens | 76% | 9.3<br><sub>-,-,-,-,6</sub> | 3.4<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.1 |
| DeAndre Jordan | 38% | 9.0<br><sub>-,10,-,-,-</sub> | 2.7<br><sub>-,8,-,-,-</sub> |  | 3.4<br><sub>-,2,-,-,-</sub> |  | 0.6<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 6.7 |
| AJ Johnson | 52% | 6.3<br><sub>6,-,-,8,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 0.8<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 99% | 30.4<br><sub>35,30,35,32,34</sub> | 20.2<br><sub>27,20,23,16,26</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>6,3,0,1,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>7,7,5,2,8</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,2,3,2,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 2.9 | 29.4 |
| Brandon Ingram | 96% | 27.3<br><sub>-,-,-,-,27</sub> | 16.0<br><sub>-,-,-,-,16</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 4.8<br><sub>-,-,-,-,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>-,-,-,-,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>-,-,-,-,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.7 | 2.0 | 23.7 |
| Rui Hachimura | 98% | 27.1<br><sub>22,27,32,29,29</sub> | 14.2<br><sub>4,20,17,19,19</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>2,5,7,8,3</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,4,2,4,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.4 | 1.1 | 20.3 |
| Derrick Jones Jr. | 99% | 24.9<br><sub>26,28,27,26,23</sub> | 9.4<br><sub>13,5,8,4,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>4,1,2,7,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,1,1,1,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1<br><sub>3,0,0,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 1.0 | 0.8 | 14.7 |
| Max Strus | 98% | 23.5<br><sub>25,21,32,29,26</sub> | 9.5<br><sub>14,3,18,5,8</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,5,6,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>4,1,4,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>4,1,5,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.2 | 1.0 | 16.2 |
| Brook Lopez | 99% | 23.0<br><sub>29,23,27,25,21</sub> | 12.8<br><sub>7,23,23,21,3</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>5,6,3,6,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>8,2,4,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>1,4,5,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 1.2 | 1.1 | 19.5 |
| Kris Dunn | 99% | 22.0<br><sub>18,26,20,19,23</sub> | 6.3<br><sub>7,2,6,3,9</sub> |  | 3.2<br><sub>3,5,2,4,5</sub> |  | 3.5<br><sub>1,5,2,5,4</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> |  | 1.5 | 0.3 | 1.0 | 13.1 |
| Keaton Wagler | 98% | 18.6<br><sub>28,18,17,19,17</sub> | 9.7<br><sub>12,15,7,7,2</sub> |  | 2.9<br><sub>4,2,5,7,1</sub> |  | 2.7<br><sub>5,0,2,3,2</sub> |  | 1.2<br><sub>2,1,1,1,0</sub> |  | 0.7 | 0.1 | 1.6 | 15.2 |
| Kobe Sanders | 98% | 15.9<br><sub>20,18,14,19,12</sub> | 6.8<br><sub>2,5,0,9,6</sub> |  | 1.9<br><sub>6,1,1,3,0</sub> |  | 1.6<br><sub>4,3,1,1,0</sub> |  | 0.9<br><sub>0,0,0,3,2</sub> |  | 0.7 | 0.1 | 0.8 | 10.3 |
| Isaiah Jackson | 98% | 13.6<br><sub>15,19,9,4,18</sub> | 6.4<br><sub>13,8,6,0,6</sub> |  | 4.4<br><sub>2,5,4,0,6</sub> |  | 1.2<br><sub>2,0,2,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.6 | 1.0 | 0.8 | 12.1 |
| Gradey Dick | 76% | 9.9<br><sub>19,17,13,16,-</sub> | 4.5<br><sub>12,0,2,6,-</sub> |  | 1.6<br><sub>2,0,2,5,-</sub> |  | 0.6<br><sub>0,1,1,2,-</sub> |  | 0.4<br><sub>2,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.7 |
| Yanic Konan Niederhauser | 72% | 8.6<br><sub>-,-,11,16,8</sub> | 3.2<br><sub>-,-,2,6,2</sub> |  | 2.5<br><sub>-,-,3,6,1</sub> |  | 0.5<br><sub>-,-,0,1,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 6.2 |
| Baba Miller | 91% | 7.4<br><sub>5,4,1,3,1</sub> | 3.5<br><sub>2,3,0,1,0</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.6 |
| Blake Wesley | 52% | 5.6<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.7 |

</details>


### GSW @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW)

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 98% | 32.9<br><sub>22,30,29,32,38</sub> | 16.2<br><sub>8,15,10,15,18</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>0,3,4,2,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.3 | 1.9 | 24.6 |
| Yaxel Lendeborg | 98% | 32.7<br><sub>24,33,30,33,34</sub> | 19.8<br><sub>3,28,13,11,12</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>7,8,5,8,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>1,3,4,7,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>0,2,0,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.8 | 2.9 | 30.4 |
| Draymond Green | 97% | 25.5<br><sub>16,25,23,-,27</sub> | 6.5<br><sub>4,2,3,-,9</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>3,5,2,-,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.7 | 2.3 | 16.4 |
| De'Anthony Melton | 99% | 22.5<br><sub>18,21,19,25,27</sub> | 9.5<br><sub>8,8,0,9,2</sub> | 11.5 · –<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>4,2,2,1,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>3,1,2,5,7</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.4 | 1.7 | 15.3 |
| Gui Santos | 96% | 18.4<br><sub>21,19,17,23,23</sub> | 7.6<br><sub>7,12,6,8,13</sub> | 9.5 · –<br><sub>o 43% · u 57%</sub> | 3.7<br><sub>4,7,6,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,2,6,0,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.7<br><sub>1,1,0,0,3</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.3 | 1.3 | 13.2 |
| Will Richard | 99% | 18.4<br><sub>30,23,27,27,17</sub> | 6.3<br><sub>7,11,20,15,3</sub> |  | 2.2<br><sub>4,3,0,5,2</sub> |  | 1.1<br><sub>1,1,3,0,2</sub> |  | 0.7<br><sub>1,2,1,1,1</sub> |  | 1.0 | 0.2 | 0.8 | 9.5 |
| Charles Bassey | 98% | 16.0<br><sub>20,16,22,25,26</sub> | 8.0<br><sub>11,4,10,16,13</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>5,0,8,13,9</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 1.1 | 14.8 |
| Al Horford | 98% | 15.9<br><sub>10,14,-,17,18</sub> | 5.3<br><sub>0,0,-,3,7</sub> |  | 3.2<br><sub>3,5,-,2,3</sub> |  | 1.6<br><sub>1,0,-,2,2</sub> |  | 0.7<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.7 | 0.5 | 10.2 |
| Gary Payton II | 91% | 14.4<br><sub>13,8,16,24,13</sub> | 6.0<br><sub>2,2,8,2,8</sub> |  | 2.5<br><sub>2,0,8,1,1</sub> |  | 1.0<br><sub>0,0,2,1,0</sub> |  | 0.3<br><sub>0,0,2,0,0</sub> |  | 0.9 | 0.2 | 0.7 | 9.4 |
| Georges Niang | 98% | 14.2<br><sub>15,14,14,15,8</sub> | 5.9<br><sub>5,0,11,5,0</sub> |  | 2.0<br><sub>3,4,1,2,1</sub> |  | 0.9<br><sub>2,2,1,0,0</sub> |  | 0.8<br><sub>1,0,2,1,0</sub> |  | 0.3 | 0.1 | 0.6 | 8.8 |
| Brandon Williams | 88% | 13.5<br><sub>-,-,-,-,-</sub> | 8.3<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 1.2 | 11.9 |
| LJ Cryer | 88% | 12.7<br><sub>24,24,19,12,11</sub> | 6.0<br><sub>20,7,9,9,3</sub> |  | 0.9<br><sub>2,1,0,0,0</sub> |  | 1.2<br><sub>6,3,2,1,2</sub> |  | 0.9<br><sub>6,1,3,1,1</sub> |  | 0.3 | 0.1 | 0.6 | 8.2 |
| Graham Ike | 72% | 7.2<br><sub>13,8,15,4,-</sub> | 3.3<br><sub>5,3,2,5,-</sub> |  | 1.6<br><sub>2,5,2,0,-</sub> |  | 0.8<br><sub>3,1,2,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 5.8 |
| Malevy Leons | 64% | 6.3<br><sub>14,6,7,4,-</sub> | 2.1<br><sub>5,2,2,0,-</sub> |  | 1.2<br><sub>1,1,1,2,-</sub> |  | 0.4<br><sub>0,0,0,1,-</sub> |  | 0.1<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.7 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 72% | 34.1<br><sub>30,-,-,36,30</sub> | 24.7<br><sub>27,-,-,20,31</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>8,-,-,9,3</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.6 | 3.7 | 38.0 |
| Toumani Camara | 99% | 32.9<br><sub>26,33,37,35,29</sub> | 12.5<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 54% · u 46%</sub> | 4.6<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,1,4,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.6 | 1.5 | 19.0 |
| Damian Lillard | 99% | 32.5<br><sub>24,31,35,33,29</sub> | 20.7<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>4,5,0,3,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>2,5,5,1,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.2 | 2.5 | 29.4 |
| Jrue Holiday | 99% | 29.8<br><sub>25,31,31,31,28</sub> | 15.0<br><sub>10,23,22,13,18</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.1<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,5,2,1,4</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 1.2 | 0.2 | 2.4 | 24.3 |
| Donovan Clingan | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.6<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 12.8<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>1,5,2,4,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.7 | 1.9 | 1.3 | 27.7 |
| Scoot Henderson | 99% | 25.3<br><sub>23,21,35,23,26</sub> | 12.7<br><sub>10,9,27,3,17</sub> |  | 2.4<br><sub>1,1,7,1,3</sub> |  | 2.6<br><sub>0,1,3,1,3</sub> |  | 1.6<br><sub>0,0,5,0,3</sub> |  | 0.8 | 0.2 | 2.1 | 17.7 |
| Sidy Cissoko | 98% | 24.8<br><sub>28,32,31,23,24</sub> | 7.7<br><sub>5,6,13,11,5</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,1,3,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1<br><sub>1,2,1,3,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.2 | 12.9 |
| Robert Williams III | 98% | 16.9<br><sub>15,16,-,17,16</sub> | 6.3<br><sub>2,6,-,4,6</sub> |  | 6.8<br><sub>5,8,-,3,6</sub> |  | 1.1<br><sub>2,4,-,0,1</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.2 | 0.8 | 14.2 |
| Jayson Kent | 88% | 11.9<br><sub>11,27,17,3,14</sub> | 4.1<br><sub>8,8,2,0,9</sub> |  | 1.4<br><sub>0,3,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>2,2,0,0,3</sub> |  | 0.5 | 0.1 | 0.6 | 6.1 |
| Branden Carlson | 91% | 8.5<br><sub>14,14,10,9,6</sub> | 2.3<br><sub>5,6,0,2,0</sub> |  | 2.2<br><sub>6,1,1,1,3</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.5 | 4.8 |
| Micah Potter | 58% | 7.2<br><sub>7,1,-,-,3</sub> | 3.0<br><sub>2,0,-,-,0</sub> |  | 2.1<br><sub>4,0,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.2<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 5.6 |
| Yang Hansen | 58% | 7.1<br><sub>7,-,12,-,3</sub> | 2.6<br><sub>0,-,2,-,2</sub> |  | 1.8<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>3,-,1,-,1</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.6 | 5.0 |
| John Tonje | 52% | 6.7<br><sub>7,-,6,-,3</sub> | 2.6<br><sub>7,-,0,-,2</sub> |  | 1.5<br><sub>4,-,3,-,0</sub> |  | 0.7<br><sub>3,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-27/`._
