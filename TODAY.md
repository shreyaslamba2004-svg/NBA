# NBA model · Fri 27 Nov 2026 (US date)

Updated **Sat 28 Nov, 09:44 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-27/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija AST over 11.5 (12+) | GSW @ POR | draftkings | 16.40 | 14.04 | 7.37 | 13.6% | 5.7% | 7.1% | +16.8% | +122.5% | 0.3% |
| Scottie Barnes AST over 9.5 (10+) | BKN @ TOR | draftkings | 10.10 | 8.77 | 4.73 | 21.1% | 9.2% | 11.4% | +15.2% | +113.4% | 0.4% |
| Scottie Barnes AST over 11.5 (12+) | BKN @ TOR | draftkings | 24.00 | 21.05 | 11.61 | 8.6% | 3.9% | 4.8% | +14.0% | +106.8% | 0.1% |
| Deni Avdija PRA over 59.5 (60+) | GSW @ POR | draftkings | 21.00 | 18.73 | 10.66 | 9.4% | 4.5% | 5.3% | +12.2% | +97.0% | 0.1% |
| Jrue Holiday AST over 11.5 (12+) | GSW @ POR | draftkings | 24.00 | 21.41 | 12.23 | 8.2% | 3.9% | 4.7% | +12.1% | +96.2% | 0.1% |
| Jrue Holiday AST over 9.5 (10+) | GSW @ POR | draftkings | 9.70 | 8.68 | 4.99 | 20.0% | 9.6% | 11.5% | +11.7% | +94.2% | 0.3% |
| Devin Booker AST over 9.5 (10+) | DAL @ PHX | draftkings | 12.00 | 10.78 | 6.24 | 16.0% | 7.8% | 9.3% | +11.4% | +92.4% | 0.3% |
| Deni Avdija AST over 9.5 (10+) | GSW @ POR | draftkings | 6.54 | 5.91 | 3.47 | 28.8% | 14.3% | 16.9% | +10.6% | +88.3% | 0.5% |
| Pascal Siakam PA over 44.5 (45+) | PHI @ IND | draftkings | 20.60 | 18.83 | 11.38 | 8.8% | 4.5% | 5.3% | +9.3% | +81.0% | 0.1% |
| MIL to win | MIL @ DET | draftkings | 4.51 | 4.15 | 4.33 | 23.1% | 24.1% | 24.1% | +8.8% | +4.2% | 0.6% |
| Devin Booker PRA over 54.5 (55+) | DAL @ PHX | draftkings | 24.00 | 22.17 | 13.67 | 7.3% | 3.9% | 4.5% | +8.3% | +75.5% | 0.1% |
| Jamal Shead AST over 11.5 (12+) | BKN @ TOR | draftkings | 19.80 | 18.35 | 11.39 | 8.8% | 4.7% | 5.5% | +8.0% | +73.8% | 0.1% |
| Deni Avdija PTS over 44.5 (45+) | GSW @ POR | draftkings | 24.00 | 22.27 | 13.87 | 7.2% | 3.9% | 4.5% | +7.9% | +73.0% | 0.1% |
| Devin Booker PRA over 49.5 (50+) | DAL @ PHX | draftkings | 13.00 | 12.08 | 7.56 | 13.2% | 7.2% | 8.3% | +7.7% | +72.0% | 0.2% |
| Pascal Siakam PTS over 39.5 (40+) | PHI @ IND | draftkings | 19.20 | 17.83 | 11.17 | 8.9% | 4.9% | 5.6% | +7.7% | +71.9% | 0.1% |
| Devin Booker AST over 11.5 (12+) | DAL @ PHX | draftkings | 29.00 | 26.95 | 16.95 | 5.9% | 3.2% | 3.7% | +7.5% | +71.1% | 0.1% |
| Rudy Gobert PR over 29.5 (30+) | MEM @ MIN | draftkings | 10.50 | 9.79 | 6.20 | 16.1% | 8.9% | 10.2% | +7.2% | +69.4% | 0.2% |
| Scottie Barnes PTS over 44.5 (45+) | BKN @ TOR | draftkings | 28.00 | 26.18 | 16.64 | 6.0% | 3.3% | 3.8% | +7.0% | +68.3% | 0.1% |
| Pascal Siakam PRA over 49.5 (50+) | PHI @ IND | draftkings | 13.80 | 12.90 | 8.23 | 12.2% | 6.8% | 7.8% | +6.9% | +67.7% | 0.1% |
| Ayo Dosunmu PTS over 34.5 (35+) | MEM @ MIN | draftkings | 17.40 | 16.39 | 10.63 | 9.4% | 5.4% | 6.1% | +6.2% | +63.6% | 0.1% |
| Toumani Camara AST over 3.5 (4+) | GSW @ POR | draftkings | 7.20 | 6.80 | 4.45 | 22.5% | 13.0% | 14.7% | +5.8% | +61.9% | 0.2% |
| Sidy Cissoko AST over 5.5 (6+) | GSW @ POR | draftkings | 18.20 | 17.21 | 11.25 | 8.9% | 5.1% | 5.8% | +5.8% | +61.8% | 0.1% |
| Jamal Shead AST over 9.5 (10+) | BKN @ TOR | draftkings | 8.20 | 7.75 | 5.07 | 19.7% | 11.4% | 12.9% | +5.8% | +61.7% | 0.2% |
| Jakob Poeltl PRA over 29.5 (30+) | BKN @ TOR | draftkings | 8.60 | 8.14 | 5.36 | 18.7% | 10.9% | 12.3% | +5.6% | +60.5% | 0.2% |
| Jakob Poeltl PRA over 34.5 (35+) | BKN @ TOR | draftkings | 19.40 | 18.38 | 12.14 | 8.2% | 4.8% | 5.4% | +5.5% | +59.7% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 7.5 (8+) | BKN @ TOR | draftkings | 3.77 | 3.58 | 2.38 | 42.0% | 24.8% | 27.9% | +5.2% | +58.3% | 0.5% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MIA @ NYK | Sat 28 Nov 11:00 | 112.1–114.2 | MIA 44% | 2.27 / 1.79 | NYK -2.5 | 226.5 | NYK -2.5 covers 50%; o221.5 60% |
| MIL @ DET | Sat 28 Nov 11:30 | 103.3–113.7 | MIL 23% | 4.33 / 1.30 | DET -10.5 | 216.5 | DET -9.5 covers 53%; o219.5 44% |
| PHI @ IND | Sat 28 Nov 11:30 | 116.8–116.4 | PHI 51% | 1.95 / 2.06 | IND +0.5 | 233.5 | IND +3.5 covers 58%; o228.5 60% |
| BKN @ TOR | Sat 28 Nov 11:30 | 105.4–113.4 | BKN 29% | 3.45 / 1.41 | TOR -7.5 | 218.5 | TOR -9.5 covers 46%; o218.5 51% |
| ATL @ BOS | Sat 28 Nov 12:00 | 108.2–116.6 | ATL 28% | 3.58 / 1.39 | BOS -8.5 | 224.5 | BOS -8.5 covers 50%; o223.5 53% |
| MEM @ MIN | Sat 28 Nov 12:30 | 110.3–115.7 | MEM 35% | 2.85 / 1.54 | MIN -5.5 | 225.5 | MIN -2.5 covers 59%; o220.5 62% |
| DAL @ PHX | Sat 28 Nov 13:00 | 112.1–117.3 | DAL 36% | 2.81 / 1.55 | PHX -5.5 | 229.5 | PHX -3.5 covers 55%; o225.5 58% |
| LAL @ SAS | Sat 28 Nov 13:30 | 110.5–112.5 | LAL 44% | 2.26 / 1.79 | SAS -2.5 | 222.5 | SAS -6.5 covers 38%; o226.5 42% |
| DEN @ UTA | Sat 28 Nov 13:30 | 124.7–115.2 | DEN 75% | 1.33 / 3.99 | UTA +9.5 | 239.5 | UTA +9.5 covers 50%; o232.5 65% |
| NOP @ LAC | Sat 28 Nov 13:30 | 110.9–116.6 | NOP 34% | 2.92 / 1.52 | LAC -5.5 | 227.5 | LAC -2.5 covers 60%; o229.5 46% |
| GSW @ POR | Sat 28 Nov 13:30 | 110.2–113.4 | GSW 41% | 2.41 / 1.71 | POR -3.5 | 223.5 | POR -7.5 covers 38%; o217.5 62% |

### MIA @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Andre Drummond (NYK), Miles McBride (NYK)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.1–114.2 | MIA 44% | 2.27 / 1.79 | NYK -2.5 | 226.5 | NYK -2.5 covers 50%; o221.5 60% |
| Expected (weighted by chance each plays) | 111.6–114.8 | MIA 41% | 2.44 / 1.70 | NYK -3.5 | 226.5 | NYK -2.5 covers 53%; o221.5 60% |
| if Karl-Anthony Towns plays | 111.1–115.5 | MIA 38% | 2.62 / 1.62 | NYK -4.5 | 226.5 | NYK -2.5 covers 56%; o221.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Karl-Anthony Towns (NYK) | Questionable | 55% | 35.3 | 23.0 | 14.3 | 4.7 | 2.0 | 1.0 | 1.0 | 2.8 | 42.0 | full tables below |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 99% | 35.8<br><sub>32,33,36,34,40</sub> | 14.6<br><sub>15,16,24,14,20</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>4,3,2,4,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>9,10,6,3,10</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>3,1,6,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 2.3 | 25.0 |
| Giannis Antetokounmpo | 99% | 34.7<br><sub>31,29,32,-,36</sub> | 26.6<br><sub>34,20,27,-,32</sub> | 27.5 · –<br><sub>o 46% · u 54%</sub> | 11.8<br><sub>14,13,14,-,14</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>8,6,9,-,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>1,0,0,-,0</sub> | 0.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.3 | 3.4 | 43.6 |
| Bam Adebayo | 99% | 34.6<br><sub>36,16,30,37,35</sub> | 18.3<br><sub>20,4,26,24,17</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 8.8<br><sub>5,1,4,15,11</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>4,2,2,12,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>1,0,3,0,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.7 | 1.6 | 30.6 |
| Pelle Larsson | 88% | 26.6<br><sub>-,-,15,30,28</sub> | 10.3<br><sub>-,-,4,21,8</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>-,-,2,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>-,-,2,5,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>-,-,1,3,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 1.6 | 16.2 |
| Klay Thompson | 91% | 24.9<br><sub>20,22,23,23,31</sub> | 12.0<br><sub>26,17,13,9,7</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,0,1,6,0</sub> |  | 1.6<br><sub>4,2,1,4,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>6,5,4,3,1</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.5 | 0.5 | 1.0 | 15.7 |
| Andrew Wiggins | 99% | 24.9<br><sub>23,34,26,22,24</sub> | 9.1<br><sub>10,17,11,5,8</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,5,2,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,1,2,1,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,3,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.6 | 0.7 | 1.0 | 13.8 |
| Ryan Conwell | 96% | 18.7<br><sub>26,30,26,29,18</sub> | 6.9<br><sub>9,14,13,10,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,3,1,1</sub> |  | 1.1<br><sub>1,3,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>2,1,3,2,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.2 | 0.8 | 9.9 |
| Bobby Portis | 99% | 16.4<br><sub>18,23,17,21,15</sub> | 6.8<br><sub>7,16,9,10,5</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>4,6,3,8,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>2,0,0,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9<br><sub>1,2,1,1,1</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.4 | 0.2 | 0.6 | 11.8 |
| Tim Hardaway Jr. | 38% | 10.0<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.3 |
| Nikola Jovic | 58% | 9.6<br><sub>11,-,14,19,-</sub> | 3.3<br><sub>2,-,4,15,-</sub> |  | 1.7<br><sub>1,-,1,8,-</sub> |  | 0.9<br><sub>2,-,4,3,-</sub> |  | 0.3<br><sub>0,-,1,3,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Simone Fontecchio | 86% | 9.0<br><sub>14,19,18,15,6</sub> | 3.8<br><sub>7,10,6,11,0</sub> |  | 1.5<br><sub>5,6,5,0,1</sub> |  | 0.6<br><sub>0,2,1,0,1</sub> |  | 0.4<br><sub>1,2,2,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |
| Myron Gardner | 72% | 8.4<br><sub>26,24,-,11,5</sub> | 2.5<br><sub>5,14,-,4,0</sub> |  | 1.9<br><sub>9,2,-,1,2</sub> |  | 0.7<br><sub>3,3,-,0,0</sub> |  | 0.2<br><sub>1,4,-,0,0</sub> |  | 0.2 | 0.2 | 0.4 | 5.1 |
| Dru Smith | 35% | 7.0<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.0 |
| Keshad Johnson | 52% | 6.3<br><sub>1,3,-,-,-</sub> | 2.6<br><sub>0,0,-,-,-</sub> |  | 1.3<br><sub>0,2,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Nick Richards | 48% | 5.6<br><sub>-,3,1,-,-</sub> | 2.0<br><sub>-,0,0,-,-</sub> |  | 1.7<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.9 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 36.6<br><sub>34,35,36,32,36</sub> | 34.6<br><sub>31,21,30,22,19</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,2,7,3,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>5,7,5,7,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,4,6,1,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.2 | 2.6 | 45.2 |
| Josh Hart | 99% | 34.5<br><sub>31,28,35,39,36</sub> | 12.6<br><sub>5,11,0,10,15</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 8.4<br><sub>4,6,8,11,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>2,2,6,10,11</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>1,3,0,0,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.3 | 1.9 | 26.6 |
| Mikal Bridges | 99% | 33.3<br><sub>30,31,28,31,37</sub> | 16.7<br><sub>17,8,12,8,19</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>5,3,2,3,8</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>1,3,3,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.6 | 1.4 | 24.5 |
| Landry Shamet | 99% | 33.0<br><sub>24,30,36,32,30</sub> | 16.3<br><sub>12,10,20,17,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>1,2,3,3,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.9<br><sub>2,2,6,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.2 | 1.1 | 21.0 |
| Jose Alvarado | 88% | 24.6<br><sub>7,13,15,22,19</sub> | 10.9<br><sub>2,2,8,11,21</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>0,2,2,1,1</sub> |  | 4.1<br><sub>4,1,2,3,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.7<br><sub>0,0,2,3,5</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 1.2 | 17.9 |
| Pacome Dadiet | 63% | 20.3<br><sub>-,-,11,17,14</sub> | 8.2<br><sub>-,-,5,5,7</sub> |  | 3.4<br><sub>-,-,0,2,1</sub> |  | 1.5<br><sub>-,-,2,0,2</sub> |  | 1.1<br><sub>-,-,1,1,1</sub> |  | 0.6 | 0.2 | 0.7 | 13.2 |
| Tyler Kolek | 96% | 20.2<br><sub>13,12,13,11,7</sub> | 8.0<br><sub>4,6,7,8,0</sub> |  | 3.0<br><sub>1,3,3,3,1</sub> |  | 5.1<br><sub>3,5,0,0,2</sub> |  | 1.0<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.1 | 1.1 | 16.1 |
| Mohamed Diawara | 52% | 18.6<br><sub>-,-,-,8,4</sub> | 7.3<br><sub>-,-,-,0,3</sub> |  | 3.4<br><sub>-,-,-,2,1</sub> |  | 2.0<br><sub>-,-,-,0,1</sub> |  | 1.0<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.7 | 12.7 |
| James Wiseman | 52% | 18.3<br><sub>-,-,25,-,6</sub> | 6.9<br><sub>-,-,5,-,6</sub> |  | 6.1<br><sub>-,-,6,-,7</sub> |  | 0.9<br><sub>-,-,2,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.8 | 1.1 | 13.8 |
| Tyler Nickel | 58% | 15.9<br><sub>-,-,-,-,9</sub> | 5.0<br><sub>-,-,-,-,5</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.5 | 0.3 | 0.5 | 6.1 |
| Dalton Knecht | 58% | 15.2<br><sub>-,-,3,-,-</sub> | 6.2<br><sub>-,-,0,-,-</sub> |  | 2.8<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 9.8 |
| Jaden Akins | 36% | 11.2<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 1.4 |

</details>

<details><summary>if Karl-Anthony Towns plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 35.8<br><sub>32,33,36,34,40</sub> | 14.5<br><sub>15,16,24,14,20</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>4,3,2,4,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>9,10,6,3,10</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>3,1,6,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 2.3 | 24.9 |
| Giannis Antetokounmpo (MIA) | 99% | 34.8<br><sub>31,29,32,-,36</sub> | 26.6<br><sub>34,20,27,-,32</sub> | 27.5 · –<br><sub>o 46% · u 54%</sub> | 11.7<br><sub>14,13,14,-,14</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>8,6,9,-,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>1,0,0,-,0</sub> | 0.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.3 | 3.3 | 43.6 |
| Bam Adebayo (MIA) | 99% | 34.6<br><sub>36,16,30,37,35</sub> | 18.3<br><sub>20,4,26,24,17</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 8.8<br><sub>5,1,4,15,11</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>4,2,2,12,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>1,0,3,0,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.7 | 1.7 | 30.6 |
| Pelle Larsson (MIA) | 88% | 26.6<br><sub>-,-,15,30,28</sub> | 10.2<br><sub>-,-,4,21,8</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>-,-,2,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>-,-,2,5,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>-,-,1,3,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 1.6 | 16.1 |
| Andrew Wiggins (MIA) | 99% | 25.0<br><sub>23,34,26,22,24</sub> | 9.2<br><sub>10,17,11,5,8</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,5,2,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,1,2,1,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,3,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.6 | 0.7 | 1.0 | 13.8 |
| Klay Thompson (MIA) | 91% | 24.8<br><sub>20,22,23,23,31</sub> | 11.8<br><sub>26,17,13,9,7</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,0,1,6,0</sub> |  | 1.6<br><sub>4,2,1,4,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>6,5,4,3,1</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.5 | 0.5 | 0.9 | 15.5 |
| Ryan Conwell (MIA) | 96% | 18.7<br><sub>26,30,26,29,18</sub> | 6.9<br><sub>9,14,13,10,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>4,2,3,1,1</sub> |  | 1.1<br><sub>1,3,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>2,1,3,2,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.2 | 0.8 | 9.8 |
| Bobby Portis (MIA) | 99% | 16.3<br><sub>18,23,17,21,15</sub> | 6.8<br><sub>7,16,9,10,5</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>4,6,3,8,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>2,0,0,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9<br><sub>1,2,1,1,1</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.4 | 0.2 | 0.6 | 11.7 |
| Tim Hardaway Jr. (MIA) | 38% | 9.9<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.3 |
| Nikola Jovic (MIA) | 58% | 9.6<br><sub>11,-,14,19,-</sub> | 3.3<br><sub>2,-,4,15,-</sub> |  | 1.7<br><sub>1,-,1,8,-</sub> |  | 0.9<br><sub>2,-,4,3,-</sub> |  | 0.3<br><sub>0,-,1,3,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Simone Fontecchio (MIA) | 86% | 9.0<br><sub>14,19,18,15,6</sub> | 3.8<br><sub>7,10,6,11,0</sub> |  | 1.5<br><sub>5,6,5,0,1</sub> |  | 0.6<br><sub>0,2,1,0,1</sub> |  | 0.4<br><sub>1,2,2,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |
| Myron Gardner (MIA) | 72% | 8.3<br><sub>26,24,-,11,5</sub> | 2.5<br><sub>5,14,-,4,0</sub> |  | 1.9<br><sub>9,2,-,1,2</sub> |  | 0.7<br><sub>3,3,-,0,0</sub> |  | 0.2<br><sub>1,4,-,0,0</sub> |  | 0.2 | 0.2 | 0.4 | 5.0 |
| Dru Smith (MIA) | 35% | 7.1<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.0 |
| Keshad Johnson (MIA) | 52% | 6.2<br><sub>1,3,-,-,-</sub> | 2.5<br><sub>0,0,-,-,-</sub> |  | 1.3<br><sub>0,2,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Nick Richards (MIA) | 48% | 5.7<br><sub>-,3,1,-,-</sub> | 2.0<br><sub>-,0,0,-,-</sub> |  | 1.7<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.9 |
| Jalen Brunson (NYK) | 99% | 37.3<br><sub>34,35,36,32,36</sub> | 30.4<br><sub>31,21,30,22,19</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,2,7,3,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>5,7,5,7,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,4,6,1,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.2 | 2.5 | 40.9 |
| Karl-Anthony Towns (NYK) | 100% | 35.3<br><sub>36,33,-,29,33</sub> | 23.0<br><sub>16,22,-,30,12</sub> | 21.5 · – | 14.3<br><sub>16,12,-,13,10</sub> | 13.5 | 4.7<br><sub>8,4,-,5,7</sub> | 3.5 | 2.0<br><sub>1,2,-,4,1</sub> | 1.5 | 1.0 | 1.0 | 2.8 | 42.0 |
| Josh Hart (NYK) | 99% | 34.9<br><sub>31,28,35,39,36</sub> | 10.8<br><sub>5,11,0,10,15</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 8.4<br><sub>4,6,8,11,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>2,2,6,10,11</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>1,3,0,0,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.3 | 1.6 | 24.6 |
| Mikal Bridges (NYK) | 99% | 33.5<br><sub>30,31,28,31,37</sub> | 13.8<br><sub>17,8,12,8,19</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>5,3,2,3,8</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>1,3,3,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.6 | 1.2 | 21.1 |
| Landry Shamet (NYK) | 99% | 32.6<br><sub>24,30,36,32,30</sub> | 13.9<br><sub>12,10,20,17,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,2,3,3,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>2,2,6,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.2 | 0.9 | 18.2 |
| Jose Alvarado (NYK) | 88% | 19.5<br><sub>7,13,15,22,19</sub> | 8.3<br><sub>2,2,8,11,21</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>0,2,2,1,1</sub> |  | 3.1<br><sub>4,1,2,3,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,0,2,3,5</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 1.0 | 13.7 |
| Pacome Dadiet (NYK) | 63% | 16.4<br><sub>-,-,11,17,14</sub> | 6.3<br><sub>-,-,5,5,7</sub> |  | 2.7<br><sub>-,-,0,2,1</sub> |  | 1.1<br><sub>-,-,2,0,2</sub> |  | 0.8<br><sub>-,-,1,1,1</sub> |  | 0.5 | 0.2 | 0.6 | 10.1 |
| Tyler Kolek (NYK) | 96% | 16.4<br><sub>13,12,13,11,7</sub> | 5.9<br><sub>4,6,7,8,0</sub> |  | 2.4<br><sub>1,3,3,3,1</sub> |  | 4.1<br><sub>3,5,0,0,2</sub> |  | 0.7<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.1 | 0.9 | 12.4 |
| Mohamed Diawara (NYK) | 52% | 13.4<br><sub>-,-,-,8,4</sub> | 4.7<br><sub>-,-,-,0,3</sub> |  | 2.4<br><sub>-,-,-,2,1</sub> |  | 1.3<br><sub>-,-,-,0,1</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 8.4 |
| Tyler Nickel (NYK) | 58% | 13.0<br><sub>-,-,-,-,9</sub> | 4.0<br><sub>-,-,-,-,5</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.3 | 0.4 | 5.0 |
| James Wiseman (NYK) | 52% | 12.8<br><sub>-,-,25,-,6</sub> | 4.5<br><sub>-,-,5,-,6</sub> |  | 4.3<br><sub>-,-,6,-,7</sub> |  | 0.6<br><sub>-,-,2,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.6 | 0.8 | 9.4 |
| Dalton Knecht (NYK) | 58% | 10.8<br><sub>-,-,3,-,-</sub> | 4.0<br><sub>-,-,0,-,-</sub> |  | 2.0<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 6.5 |
| Jaden Akins (NYK) | 36% | 8.3<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |

</details>


### MIL @ DET
Out: Cade Cunningham (DET), Jalen Duren (DET), Taurean Prince (DET), Duncan Robinson (DET), Kasparas Jakucionis (MIL), Kam Jones (MIL), Cormac Ryan (MIL)

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 99% | 32.9<br><sub>24,31,40,37,37</sub> | 20.7<br><sub>8,19,50,32,28</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>2,4,11,6,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.6<br><sub>4,3,7,8,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>0,4,7,4,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 2.6 | 29.5 |
| Kyle Kuzma | 99% | 28.1<br><sub>30,-,33,32,31</sub> | 12.7<br><sub>26,-,12,18,13</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>5,-,5,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>1,-,1,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,-,2,2,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.4 | 1.9 | 19.7 |
| Jaime Jaquez Jr. | 99% | 27.0<br><sub>23,22,25,25,35</sub> | 12.6<br><sub>10,9,9,3,21</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>2,1,0,4,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,2,1,2,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 2.1 | 20.2 |
| Myles Turner | 99% | 25.3<br><sub>21,-,26,28,26</sub> | 9.0<br><sub>4,-,5,27,3</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,-,6,11,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>4,-,5,1,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>0,-,1,5,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 1.8 | 1.6 | 16.2 |
| Brayden Burries | 99% | 23.9<br><sub>25,28,26,29,22</sub> | 10.2<br><sub>20,14,26,14,3</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>7,3,8,10,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>1,3,4,4,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>3,2,2,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.3 | 1.7 | 17.9 |
| Ryan Rollins | 99% | 23.2<br><sub>-,21,28,22,19</sub> | 10.3<br><sub>-,15,8,6,2</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>-,3,6,1,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,6,1,3,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>-,1,0,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.3 | 2.3 | 17.4 |
| Kel'el Ware | 98% | 19.8<br><sub>17,26,22,23,22</sub> | 8.4<br><sub>11,11,6,9,13</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>3,5,8,3,14</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.1<br><sub>1,0,3,0,2</sub> |  | 0.7<br><sub>1,2,0,1,1</sub> |  | 0.6 | 1.2 | 1.3 | 15.9 |
| Nate Ament | 98% | 18.7<br><sub>17,35,14,25,21</sub> | 6.7<br><sub>7,18,2,7,8</sub> |  | 3.0<br><sub>4,9,1,4,3</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.7<br><sub>0,2,0,0,2</sub> |  | 0.5 | 0.3 | 1.0 | 10.5 |
| Pete Nance | 96% | 14.0<br><sub>-,28,-,-,-</sub> | 4.1<br><sub>-,7,-,-,-</sub> |  | 2.2<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,3,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.3 | 0.3 | 0.6 | 7.3 |
| AJ Green | 67% | 11.7<br><sub>14,-,12,-,5</sub> | 3.9<br><sub>11,-,9,-,0</sub> |  | 1.0<br><sub>0,-,0,-,0</sub> |  | 0.7<br><sub>1,-,0,-,0</sub> |  | 0.6<br><sub>3,-,3,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 5.7 |
| Caris LeVert | 66% | 11.3<br><sub>8,11,5,8,12</sub> | 4.1<br><sub>8,3,0,0,2</sub> |  | 1.4<br><sub>3,3,1,0,1</sub> |  | 1.2<br><sub>2,1,0,0,2</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 6.7 |
| Gary Trent Jr. | 58% | 9.1<br><sub>16,7,-,5,-</sub> | 3.8<br><sub>1,0,-,0,-</sub> |  | 0.6<br><sub>1,1,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.8 |
| Jericho Sims | 52% | 8.9<br><sub>18,10,-,-,-</sub> | 2.0<br><sub>4,0,-,-,-</sub> |  | 2.3<br><sub>6,0,-,-,-</sub> |  | 0.6<br><sub>2,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.6 | 4.8 |
| Ousmane Dieng | 58% | 8.8<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.6 | 5.5 |

</details>

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Daniss Jenkins | 99% | 35.0<br><sub>38,36,39,38,35</sub> | 18.6<br><sub>25,17,14,11,15</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>5,4,4,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.9<br><sub>5,9,1,3,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>3,3,2,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.2 | 2.4 | 29.8 |
| Kevin Huerter | 98% | 32.0<br><sub>36,36,36,30,32</sub> | 14.6<br><sub>9,11,20,2,13</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>7,1,3,3,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>1,7,3,1,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>0,1,4,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.6 | 1.7 | 22.9 |
| Ausar Thompson | 99% | 31.4<br><sub>29,34,33,38,31</sub> | 12.8<br><sub>14,10,13,18,6</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 8.6<br><sub>9,7,6,11,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>12,4,3,5,7</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.2 | 1.1 | 2.2 | 27.5 |
| Paul Reed | 98% | 27.0<br><sub>25,20,28,26,22</sub> | 14.6<br><sub>10,17,8,16,9</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 8.3<br><sub>6,7,7,5,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>5,1,3,2,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.5 | 1.2 | 1.7 | 25.6 |
| John Collins | 99% | 26.9<br><sub>23,30,20,22,26</sub> | 13.9<br><sub>11,20,3,18,12</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 6.1<br><sub>1,7,6,6,4</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>0,2,1,0,0</sub> |  | 1.4<br><sub>1,4,0,4,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.8 | 1.5 | 21.2 |
| Isaiah Joe | 96% | 25.8<br><sub>-,16,18,26,30</sub> | 15.0<br><sub>-,11,9,19,21</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>-,2,1,2,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.0<br><sub>-,2,0,3,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.8<br><sub>-,3,1,3,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.2 | 1.1 | 20.0 |
| Javonte Green | 98% | 25.6<br><sub>23,35,23,18,27</sub> | 9.7<br><sub>6,18,12,6,6</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>6,7,1,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>0,0,0,1,1</sub> |  | 1.6<br><sub>0,3,3,2,2</sub> |  | 1.6 | 0.4 | 0.7 | 14.6 |
| Ronald Holland II | 98% | 20.2<br><sub>-,-,-,10,17</sub> | 8.5<br><sub>-,-,-,2,13</sub> |  | 4.5<br><sub>-,-,-,4,3</sub> |  | 1.7<br><sub>-,-,-,0,1</sub> |  | 0.9<br><sub>-,-,-,0,2</sub> |  | 1.0 | 0.6 | 1.1 | 14.6 |
| Elijah Harkless | 52% | 14.3<br><sub>4,14,-,-,14</sub> | 5.5<br><sub>0,6,-,-,7</sub> |  | 1.9<br><sub>1,2,-,-,1</sub> |  | 2.5<br><sub>1,4,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,2</sub> |  | 0.6 | 0.1 | 1.0 | 9.9 |
| Chaz Lanier | 66% | 12.9<br><sub>25,16,6,-,7</sub> | 4.8<br><sub>3,9,0,-,2</sub> |  | 1.2<br><sub>3,1,0,-,2</sub> |  | 0.8<br><sub>1,0,0,-,0</sub> |  | 0.7<br><sub>1,3,0,-,0</sub> |  | 0.2 | 0.1 | 0.2 | 6.8 |
| Tolu Smith | 38% | 8.2<br><sub>-,3,-,-,-</sub> | 3.2<br><sub>-,3,-,-,-</sub> |  | 2.9<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 6.6 |
| Isaac Jones | 38% | 6.5<br><sub>-,-,-,-,-</sub> | 7.6<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.3 | 9.7 |

</details>


### PHI @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND), Jaylen Brown (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.8–116.4 | PHI 51% | 1.95 / 2.06 | IND +0.5 | 233.5 | IND +3.5 covers 58%; o228.5 60% |
| Expected (weighted by chance each plays) | 118.5–116.8 | PHI 55% | 1.83 / 2.20 | IND +1.5 | 234.5 | IND +3.5 covers 55%; o228.5 62% |
| if Kelly Oubre Jr. plays | 117.1–116.9 | PHI 50% | 1.98 / 2.02 | IND +0.5 | 233.5 | IND +3.5 covers 59%; o228.5 61% |
| if Dean Wade plays | 117.1–115.9 | PHI 54% | 1.87 / 2.15 | IND +1.5 | 232.5 | IND +3.5 covers 56%; o228.5 59% |
| if Joel Embiid plays | 120.2–117.0 | PHI 59% | 1.69 / 2.46 | IND +3.5 | 237.5 | IND +3.5 covers 50%; o228.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kelly Oubre Jr. (IND) | Questionable | 55% | 27.0 | 12.6 | 4.4 | 1.3 | 1.3 | 0.8 | 0.6 | 1.1 | 18.4 | full tables below |
| Dean Wade (PHI) | Questionable | 55% | 27.3 | 5.5 | 5.0 | 1.6 | 0.8 | 0.9 | 0.4 | 0.6 | 12.1 | full tables below |
| Joel Embiid (PHI) | Questionable | 55% | 33.2 | 26.0 | 9.2 | 4.6 | 1.0 | 0.8 | 1.2 | 2.8 | 39.8 | full tables below |
| T.J. McConnell (IND) | Questionable | 55% | 15.6 | 8.4 | 2.2 | 4.7 | 0.2 | 0.8 | 0.2 | 1.1 | 15.2 | small |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 88% | 38.7<br><sub>35,-,36,35,37</sub> | 30.5<br><sub>24,-,17,22,30</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>1,-,4,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>9,-,4,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>4,-,0,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.5 | 2.6 | 41.0 |
| VJ Edgecombe | 98% | 37.8<br><sub>33,43,38,35,36</sub> | 18.2<br><sub>14,24,16,12,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>9,8,3,7,6</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 5.1<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>1,4,1,1,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.5 | 1.9 | 30.1 |
| LeBron James | 99% | 35.9<br><sub>-,31,35,30,35</sub> | 23.3<br><sub>-,22,21,23,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>-,3,6,6,10</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>-,6,6,3,12</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>-,1,0,4,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.6 | 3.1 | 38.4 |
| Kentavious Caldwell-Pope | 99% | 29.6<br><sub>31,32,35,17,28</sub> | 8.1<br><sub>0,8,11,2,5</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>2,8,1,3,1</sub> |  | 2.1<br><sub>3,1,2,1,3</sub> |  | 1.2<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 0.8 | 13.7 |
| Anfernee Simons | 99% | 26.3<br><sub>26,38,26,18,15</sub> | 13.3<br><sub>9,18,18,3,6</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>1,2,0,0,1</sub> |  | 1.9<br><sub>2,2,1,0,1</sub> |  | 2.2<br><sub>1,3,4,0,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.1 | 1.0 | 17.9 |
| Jabari Walker | 96% | 21.0<br><sub>16,13,20,20,17</sub> | 9.2<br><sub>12,6,9,10,7</sub> |  | 6.3<br><sub>5,5,7,5,2</sub> |  | 1.4<br><sub>1,2,4,2,1</sub> |  | 0.9<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.7 | 16.9 |
| Dominick Barlow | 93% | 19.7<br><sub>-,-,11,16,16</sub> | 7.0<br><sub>-,-,12,6,9</sub> |  | 4.5<br><sub>-,-,4,2,8</sub> |  | 1.0<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.8 | 0.7 | 0.7 | 12.6 |
| Adem Bona | 98% | 18.0<br><sub>-,-,-,5,13</sub> | 4.9<br><sub>-,-,-,4,0</sub> |  | 5.0<br><sub>-,-,-,2,6</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.1 | 0.8 | 10.7 |
| Labaron Philon Jr. | 64% | 12.3<br><sub>-,17,6,3,-</sub> | 4.7<br><sub>-,10,2,2,-</sub> |  | 1.6<br><sub>-,1,0,1,-</sub> |  | 1.1<br><sub>-,2,0,1,-</sub> |  | 0.5<br><sub>-,2,0,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 7.5 |
| Justin Edwards | 52% | 11.9<br><sub>-,13,-,3,-</sub> | 4.7<br><sub>-,2,-,5,-</sub> |  | 1.7<br><sub>-,1,-,1,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,1,-</sub> |  | 0.5 | 0.2 | 0.4 | 7.1 |
| Rayan Rupert | 36% | 11.4<br><sub>-,-,-,-,-</sub> | 4.2<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.6 | 7.1 |
| Tacko Fall | 48% | 9.1<br><sub>-,10,-,-,-</sub> | 6.8<br><sub>-,2,-,-,-</sub> |  | 2.5<br><sub>-,3,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.7 | 0.5 | 9.8 |
| Caleb Love | 48% | 7.6<br><sub>-,6,-,-,-</sub> | 2.5<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,1,-,-,-</sub> |  | 0.6<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,1,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 91% | 35.4<br><sub>-,-,26,32,38</sub> | 19.0<br><sub>-,-,12,16,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 9.0<br><sub>-,-,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>-,-,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.7 | 31.2 |
| Pascal Siakam | 96% | 34.9<br><sub>34,33,30,33,35</sub> | 26.6<br><sub>31,24,21,25,20</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>2,4,7,6,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,3,2,1,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 2.2 | 37.5 |
| Aaron Nesmith | 72% | 31.7<br><sub>36,29,29,32,-</sub> | 13.8<br><sub>12,2,2,9,-</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>4,3,10,2,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>4,3,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>0,0,0,0,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.6 | 1.4 | 20.5 |
| Ivica Zubac | 91% | 28.4<br><sub>22,24,27,31,26</sub> | 12.9<br><sub>8,4,21,10,14</sub> | 12.5 · –<br><sub>o 46% · u 53%</sub> | 10.8<br><sub>5,3,10,14,15</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.4 | 25.9 |
| Quenton Jackson | 99% | 23.8<br><sub>30,22,18,17,20</sub> | 10.7<br><sub>15,15,3,2,9</sub> |  | 3.4<br><sub>6,2,2,1,3</sub> |  | 3.6<br><sub>8,3,2,3,0</sub> |  | 1.1<br><sub>1,2,1,0,1</sub> |  | 1.0 | 0.2 | 1.5 | 17.8 |
| Obi Toppin | 91% | 23.4<br><sub>14,17,26,22,24</sub> | 13.1<br><sub>5,6,17,9,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>2,1,3,5,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,1,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.1 | 20.2 |
| Braden Smith | 83% | 21.7<br><sub>-,18,11,18,24</sub> | 7.0<br><sub>-,8,5,6,6</sub> |  | 2.4<br><sub>-,5,3,1,2</sub> |  | 4.4<br><sub>-,3,5,4,6</sub> |  | 0.7<br><sub>-,2,1,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 13.8 |
| Jalen Slawson | 91% | 17.5<br><sub>14,12,14,14,20</sub> | 6.0<br><sub>8,5,4,7,16</sub> |  | 4.0<br><sub>5,4,2,3,10</sub> |  | 1.6<br><sub>2,2,2,0,2</sub> |  | 0.5<br><sub>1,1,0,0,3</sub> |  | 0.8 | 1.1 | 0.8 | 11.6 |
| Jarace Walker | 91% | 16.6<br><sub>14,17,11,1,14</sub> | 7.1<br><sub>2,1,8,0,4</sub> |  | 3.9<br><sub>5,3,1,0,8</sub> |  | 1.6<br><sub>2,1,3,0,3</sub> |  | 0.8<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.3 | 0.9 | 12.6 |
| Kobe Brown | 88% | 14.7<br><sub>3,2,-,-,7</sub> | 5.4<br><sub>0,0,-,-,4</sub> |  | 2.7<br><sub>0,0,-,-,0</sub> |  | 1.2<br><sub>0,0,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.3 |
| Jay Huff | 71% | 13.3<br><sub>18,15,1,1,-</sub> | 5.8<br><sub>11,5,0,2,-</sub> |  | 2.7<br><sub>0,3,0,0,-</sub> |  | 0.9<br><sub>2,0,0,0,-</sub> |  | 0.7<br><sub>3,0,0,0,-</sub> |  | 0.2 | 0.8 | 0.6 | 9.4 |
| Larry Nance Jr. | 91% | 12.5<br><sub>7,9,11,11,4</sub> | 4.3<br><sub>4,3,7,5,0</sub> |  | 2.5<br><sub>2,1,2,3,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 7.5 |

</details>

<details><summary>if Kelly Oubre Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam (IND) | 96% | 34.7<br><sub>34,33,30,33,35</sub> | 25.3<br><sub>31,24,21,25,20</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>2,4,7,6,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,3,2,1,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.5 | 2.1 | 36.3 |
| Andrew Nembhard (IND) | 91% | 34.2<br><sub>-,-,26,32,38</sub> | 17.6<br><sub>-,-,12,16,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 8.8<br><sub>-,-,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>-,-,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.6 | 29.5 |
| Aaron Nesmith (IND) | 72% | 29.4<br><sub>36,29,29,32,-</sub> | 12.5<br><sub>12,2,2,9,-</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,3,10,2,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>4,3,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,0,0,0,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.2 | 18.8 |
| Kelly Oubre Jr. (IND) | 100% | 27.0<br><sub>29,23,23,27,28</sub> | 12.6<br><sub>16,17,17,15,20</sub> | 11.5 · – | 4.4<br><sub>4,4,6,5,4</sub> | 3.5 | 1.3<br><sub>2,0,0,0,2</sub> |  | 1.3<br><sub>2,2,3,0,4</sub> | 1.5 | 0.8 | 0.6 | 1.1 | 18.4 |
| Ivica Zubac (IND) | 91% | 26.9<br><sub>22,24,27,31,26</sub> | 12.4<br><sub>8,4,21,10,14</sub> | 12.5 · –<br><sub>o 46% · u 53%</sub> | 10.3<br><sub>5,3,10,14,15</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.3 | 24.8 |
| Obi Toppin (IND) | 91% | 21.5<br><sub>14,17,26,22,24</sub> | 12.3<br><sub>5,6,17,9,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>2,1,3,5,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,1,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.2 | 1.1 | 18.9 |
| Quenton Jackson (IND) | 99% | 20.9<br><sub>30,22,18,17,20</sub> | 9.3<br><sub>15,15,3,2,9</sub> |  | 3.0<br><sub>6,2,2,1,3</sub> |  | 3.1<br><sub>8,3,2,3,0</sub> |  | 1.0<br><sub>1,2,1,0,1</sub> |  | 0.9 | 0.2 | 1.3 | 15.5 |
| Braden Smith (IND) | 83% | 17.8<br><sub>-,18,11,18,24</sub> | 5.6<br><sub>-,8,5,6,6</sub> |  | 1.9<br><sub>-,5,3,1,2</sub> |  | 3.7<br><sub>-,3,5,4,6</sub> |  | 0.5<br><sub>-,2,1,0,1</sub> |  | 0.8 | 0.3 | 1.0 | 11.2 |
| Jalen Slawson (IND) | 91% | 15.1<br><sub>14,12,14,14,20</sub> | 5.2<br><sub>8,5,4,7,16</sub> |  | 3.5<br><sub>5,4,2,3,10</sub> |  | 1.5<br><sub>2,2,2,0,2</sub> |  | 0.4<br><sub>1,1,0,0,3</sub> |  | 0.7 | 0.9 | 0.7 | 10.1 |
| Jarace Walker (IND) | 91% | 14.6<br><sub>14,17,11,1,14</sub> | 6.2<br><sub>2,1,8,0,4</sub> |  | 3.4<br><sub>5,3,1,0,8</sub> |  | 1.5<br><sub>2,1,3,0,3</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.3 | 0.8 | 11.1 |
| Kobe Brown (IND) | 88% | 11.0<br><sub>3,2,-,-,7</sub> | 4.1<br><sub>0,0,-,-,4</sub> |  | 2.0<br><sub>0,0,-,-,0</sub> |  | 0.9<br><sub>0,0,-,-,1</sub> |  | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 7.1 |
| Larry Nance Jr. (IND) | 91% | 10.0<br><sub>7,9,11,11,4</sub> | 3.5<br><sub>4,3,7,5,0</sub> |  | 2.0<br><sub>2,1,2,3,0</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.3<br><sub>1,1,1,1,0</sub> |  | 0.4 | 0.2 | 0.3 | 6.0 |
| Jay Huff (IND) | 71% | 9.9<br><sub>18,15,1,1,-</sub> | 4.5<br><sub>11,5,0,2,-</sub> |  | 2.0<br><sub>0,3,0,0,-</sub> |  | 0.7<br><sub>2,0,0,0,-</sub> |  | 0.5<br><sub>3,0,0,0,-</sub> |  | 0.2 | 0.6 | 0.4 | 7.2 |
| Tyrese Maxey (PHI) | 88% | 38.7<br><sub>35,-,36,35,37</sub> | 30.5<br><sub>24,-,17,22,30</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>1,-,4,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>9,-,4,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>4,-,0,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.5 | 2.6 | 41.0 |
| VJ Edgecombe (PHI) | 98% | 37.8<br><sub>33,43,38,35,36</sub> | 18.3<br><sub>14,24,16,12,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>9,8,3,7,6</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 5.1<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>1,4,1,1,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.5 | 2.0 | 30.1 |
| LeBron James (PHI) | 99% | 35.9<br><sub>-,31,35,30,35</sub> | 23.4<br><sub>-,22,21,23,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>-,3,6,6,10</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>-,6,6,3,12</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>-,1,0,4,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.6 | 3.1 | 38.4 |
| Kentavious Caldwell-Pope (PHI) | 99% | 29.6<br><sub>31,32,35,17,28</sub> | 8.0<br><sub>0,8,11,2,5</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>2,8,1,3,1</sub> |  | 2.1<br><sub>3,1,2,1,3</sub> |  | 1.2<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 0.8 | 13.6 |
| Anfernee Simons (PHI) | 99% | 26.3<br><sub>26,38,26,18,15</sub> | 13.3<br><sub>9,18,18,3,6</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>1,2,0,0,1</sub> |  | 1.9<br><sub>2,2,1,0,1</sub> |  | 2.2<br><sub>1,3,4,0,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.6 | 0.1 | 1.0 | 17.9 |
| Jabari Walker (PHI) | 96% | 21.1<br><sub>16,13,20,20,17</sub> | 9.3<br><sub>12,6,9,10,7</sub> |  | 6.3<br><sub>5,5,7,5,2</sub> |  | 1.4<br><sub>1,2,4,2,1</sub> |  | 0.9<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.7 | 17.0 |
| Dominick Barlow (PHI) | 93% | 19.6<br><sub>-,-,11,16,16</sub> | 7.0<br><sub>-,-,12,6,9</sub> |  | 4.5<br><sub>-,-,4,2,8</sub> |  | 1.0<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.8 | 0.7 | 0.7 | 12.6 |
| Adem Bona (PHI) | 98% | 18.0<br><sub>-,-,-,5,13</sub> | 4.8<br><sub>-,-,-,4,0</sub> |  | 5.1<br><sub>-,-,-,2,6</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.1 | 0.8 | 10.7 |
| Labaron Philon Jr. (PHI) | 64% | 12.4<br><sub>-,17,6,3,-</sub> | 4.7<br><sub>-,10,2,2,-</sub> |  | 1.6<br><sub>-,1,0,1,-</sub> |  | 1.1<br><sub>-,2,0,1,-</sub> |  | 0.5<br><sub>-,2,0,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 7.5 |
| Justin Edwards (PHI) | 52% | 12.0<br><sub>-,13,-,3,-</sub> | 4.7<br><sub>-,2,-,5,-</sub> |  | 1.8<br><sub>-,1,-,1,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,1,-</sub> |  | 0.5 | 0.2 | 0.4 | 7.2 |
| Rayan Rupert (PHI) | 36% | 11.2<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.6 | 7.0 |
| Tacko Fall (PHI) | 48% | 9.1<br><sub>-,10,-,-,-</sub> | 6.8<br><sub>-,2,-,-,-</sub> |  | 2.5<br><sub>-,3,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.7 | 0.4 | 9.8 |
| Caleb Love (PHI) | 48% | 7.6<br><sub>-,6,-,-,-</sub> | 2.5<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,1,-,-,-</sub> |  | 0.6<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,1,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>if Dean Wade plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 35.4<br><sub>-,-,26,32,38</sub> | 19.1<br><sub>-,-,12,16,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 8.9<br><sub>-,-,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>-,-,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.7 | 31.2 |
| Pascal Siakam (IND) | 96% | 34.9<br><sub>34,33,30,33,35</sub> | 26.4<br><sub>31,24,21,25,20</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>2,4,7,6,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,3,2,1,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.5 | 2.2 | 37.2 |
| Aaron Nesmith (IND) | 72% | 31.7<br><sub>36,29,29,32,-</sub> | 13.8<br><sub>12,2,2,9,-</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>4,3,10,2,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>4,3,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>0,0,0,0,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.6 | 1.4 | 20.5 |
| Ivica Zubac (IND) | 91% | 28.3<br><sub>22,24,27,31,26</sub> | 12.7<br><sub>8,4,21,10,14</sub> | 12.5 · –<br><sub>o 46% · u 53%</sub> | 10.8<br><sub>5,3,10,14,15</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.4 | 25.6 |
| Quenton Jackson (IND) | 99% | 23.8<br><sub>30,22,18,17,20</sub> | 10.7<br><sub>15,15,3,2,9</sub> |  | 3.4<br><sub>6,2,2,1,3</sub> |  | 3.6<br><sub>8,3,2,3,0</sub> |  | 1.1<br><sub>1,2,1,0,1</sub> |  | 1.0 | 0.2 | 1.5 | 17.7 |
| Obi Toppin (IND) | 91% | 23.5<br><sub>14,17,26,22,24</sub> | 13.2<br><sub>5,6,17,9,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>2,1,3,5,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,1,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.1 | 20.2 |
| Braden Smith (IND) | 83% | 21.6<br><sub>-,18,11,18,24</sub> | 7.0<br><sub>-,8,5,6,6</sub> |  | 2.4<br><sub>-,5,3,1,2</sub> |  | 4.3<br><sub>-,3,5,4,6</sub> |  | 0.7<br><sub>-,2,1,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 13.7 |
| Jalen Slawson (IND) | 91% | 17.4<br><sub>14,12,14,14,20</sub> | 6.0<br><sub>8,5,4,7,16</sub> |  | 4.0<br><sub>5,4,2,3,10</sub> |  | 1.6<br><sub>2,2,2,0,2</sub> |  | 0.5<br><sub>1,1,0,0,3</sub> |  | 0.8 | 1.1 | 0.8 | 11.6 |
| Jarace Walker (IND) | 91% | 16.6<br><sub>14,17,11,1,14</sub> | 7.1<br><sub>2,1,8,0,4</sub> |  | 3.9<br><sub>5,3,1,0,8</sub> |  | 1.6<br><sub>2,1,3,0,3</sub> |  | 0.8<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.3 | 0.9 | 12.7 |
| Kobe Brown (IND) | 88% | 14.7<br><sub>3,2,-,-,7</sub> | 5.4<br><sub>0,0,-,-,4</sub> |  | 2.7<br><sub>0,0,-,-,0</sub> |  | 1.2<br><sub>0,0,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.3 |
| Jay Huff (IND) | 71% | 13.4<br><sub>18,15,1,1,-</sub> | 5.8<br><sub>11,5,0,2,-</sub> |  | 2.7<br><sub>0,3,0,0,-</sub> |  | 1.0<br><sub>2,0,0,0,-</sub> |  | 0.7<br><sub>3,0,0,0,-</sub> |  | 0.2 | 0.8 | 0.6 | 9.5 |
| Larry Nance Jr. (IND) | 91% | 12.5<br><sub>7,9,11,11,4</sub> | 4.3<br><sub>4,3,7,5,0</sub> |  | 2.4<br><sub>2,1,2,3,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.4 |
| Tyrese Maxey (PHI) | 88% | 37.0<br><sub>35,-,36,35,37</sub> | 30.7<br><sub>24,-,17,22,30</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>1,-,4,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 6.1<br><sub>9,-,4,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>4,-,0,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.5 | 2.4 | 40.7 |
| VJ Edgecombe (PHI) | 98% | 35.9<br><sub>33,43,38,35,36</sub> | 17.5<br><sub>14,24,16,12,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>9,8,3,7,6</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 4.7<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>1,4,1,1,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.4 | 1.8 | 28.5 |
| LeBron James (PHI) | 99% | 33.8<br><sub>-,31,35,30,35</sub> | 23.8<br><sub>-,22,21,23,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>-,3,6,6,10</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>-,6,6,3,12</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>-,1,0,4,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.5 | 2.9 | 38.0 |
| Dean Wade (PHI) | 100% | 27.3<br><sub>32,-,-,28,26</sub> | 5.5<br><sub>8,-,-,2,5</sub> | 5.5 · – | 5.0<br><sub>11,-,-,2,4</sub> | 4.5 | 1.6<br><sub>1,-,-,2,0</sub> |  | 0.8<br><sub>1,-,-,0,1</sub> | 0.5 | 0.9 | 0.4 | 0.6 | 12.1 |
| Kentavious Caldwell-Pope (PHI) | 99% | 26.8<br><sub>31,32,35,17,28</sub> | 7.4<br><sub>0,8,11,2,5</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>2,8,1,3,1</sub> |  | 2.0<br><sub>3,1,2,1,3</sub> |  | 1.1<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 0.8 | 12.5 |
| Anfernee Simons (PHI) | 99% | 23.0<br><sub>26,38,26,18,15</sub> | 12.3<br><sub>9,18,18,3,6</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>1,2,0,0,1</sub> |  | 1.7<br><sub>2,2,1,0,1</sub> |  | 1.9<br><sub>1,3,4,0,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.6 | 0.1 | 1.0 | 16.2 |
| Jabari Walker (PHI) | 96% | 17.0<br><sub>16,13,20,20,17</sub> | 7.9<br><sub>12,6,9,10,7</sub> |  | 5.2<br><sub>5,5,7,5,2</sub> |  | 1.1<br><sub>1,2,4,2,1</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.2 | 0.6 | 14.2 |
| Dominick Barlow (PHI) | 93% | 16.1<br><sub>-,-,11,16,16</sub> | 6.0<br><sub>-,-,12,6,9</sub> |  | 3.9<br><sub>-,-,4,2,8</sub> |  | 0.8<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.6 | 0.6 | 0.6 | 10.7 |
| Adem Bona (PHI) | 98% | 15.4<br><sub>-,-,-,5,13</sub> | 4.5<br><sub>-,-,-,4,0</sub> |  | 4.3<br><sub>-,-,-,2,6</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 9.5 |
| Labaron Philon Jr. (PHI) | 64% | 8.9<br><sub>-,17,6,3,-</sub> | 3.7<br><sub>-,10,2,2,-</sub> |  | 1.1<br><sub>-,1,0,1,-</sub> |  | 0.8<br><sub>-,2,0,1,-</sub> |  | 0.3<br><sub>-,2,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Justin Edwards (PHI) | 52% | 8.3<br><sub>-,13,-,3,-</sub> | 3.6<br><sub>-,2,-,5,-</sub> |  | 1.2<br><sub>-,1,-,1,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,0,-,1,-</sub> |  | 0.4 | 0.1 | 0.3 | 5.4 |
| Tacko Fall (PHI) | 48% | 7.8<br><sub>-,10,-,-,-</sub> | 6.0<br><sub>-,2,-,-,-</sub> |  | 2.1<br><sub>-,3,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.6 | 0.4 | 8.6 |
| Rayan Rupert (PHI) | 36% | 7.5<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.9 |
| Caleb Love (PHI) | 48% | 6.0<br><sub>-,6,-,-,-</sub> | 2.3<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,1,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 3.5 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 35.4<br><sub>-,-,26,32,38</sub> | 19.1<br><sub>-,-,12,16,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,-,3,2,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 9.0<br><sub>-,-,8,8,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>-,-,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.8 | 31.4 |
| Pascal Siakam (IND) | 96% | 35.0<br><sub>34,33,30,33,35</sub> | 26.5<br><sub>31,24,21,25,20</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>2,4,7,6,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,3,2,1,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 2.1 | 37.5 |
| Aaron Nesmith (IND) | 72% | 31.8<br><sub>36,29,29,32,-</sub> | 13.8<br><sub>12,2,2,9,-</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>4,3,10,2,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,3,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>0,0,0,0,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.6 | 1.4 | 20.7 |
| Ivica Zubac (IND) | 91% | 28.3<br><sub>22,24,27,31,26</sub> | 12.8<br><sub>8,4,21,10,14</sub> | 12.5 · –<br><sub>o 46% · u 53%</sub> | 10.9<br><sub>5,3,10,14,15</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.3 | 25.8 |
| Quenton Jackson (IND) | 99% | 23.8<br><sub>30,22,18,17,20</sub> | 10.7<br><sub>15,15,3,2,9</sub> |  | 3.4<br><sub>6,2,2,1,3</sub> |  | 3.6<br><sub>8,3,2,3,0</sub> |  | 1.1<br><sub>1,2,1,0,1</sub> |  | 1.0 | 0.2 | 1.5 | 17.7 |
| Obi Toppin (IND) | 91% | 23.4<br><sub>14,17,26,22,24</sub> | 13.2<br><sub>5,6,17,9,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>2,1,3,5,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,1,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.1 | 20.2 |
| Braden Smith (IND) | 83% | 21.7<br><sub>-,18,11,18,24</sub> | 7.0<br><sub>-,8,5,6,6</sub> |  | 2.4<br><sub>-,5,3,1,2</sub> |  | 4.3<br><sub>-,3,5,4,6</sub> |  | 0.7<br><sub>-,2,1,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 13.8 |
| Jalen Slawson (IND) | 91% | 17.3<br><sub>14,12,14,14,20</sub> | 6.0<br><sub>8,5,4,7,16</sub> |  | 3.9<br><sub>5,4,2,3,10</sub> |  | 1.6<br><sub>2,2,2,0,2</sub> |  | 0.5<br><sub>1,1,0,0,3</sub> |  | 0.8 | 1.1 | 0.8 | 11.5 |
| Jarace Walker (IND) | 91% | 16.6<br><sub>14,17,11,1,14</sub> | 7.2<br><sub>2,1,8,0,4</sub> |  | 3.9<br><sub>5,3,1,0,8</sub> |  | 1.7<br><sub>2,1,3,0,3</sub> |  | 0.8<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.3 | 0.9 | 12.7 |
| Kobe Brown (IND) | 88% | 14.7<br><sub>3,2,-,-,7</sub> | 5.4<br><sub>0,0,-,-,4</sub> |  | 2.7<br><sub>0,0,-,-,0</sub> |  | 1.2<br><sub>0,0,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.3 |
| Jay Huff (IND) | 71% | 13.4<br><sub>18,15,1,1,-</sub> | 5.8<br><sub>11,5,0,2,-</sub> |  | 2.7<br><sub>0,3,0,0,-</sub> |  | 1.0<br><sub>2,0,0,0,-</sub> |  | 0.7<br><sub>3,0,0,0,-</sub> |  | 0.2 | 0.8 | 0.5 | 9.4 |
| Larry Nance Jr. (IND) | 91% | 12.5<br><sub>7,9,11,11,4</sub> | 4.4<br><sub>4,3,7,5,0</sub> |  | 2.5<br><sub>2,1,2,3,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.5 |
| Tyrese Maxey (PHI) | 88% | 37.3<br><sub>35,-,36,35,37</sub> | 26.6<br><sub>24,-,17,22,30</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,-,4,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>9,-,4,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>4,-,0,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.5 | 2.2 | 36.1 |
| VJ Edgecombe (PHI) | 98% | 36.5<br><sub>33,43,38,35,36</sub> | 15.1<br><sub>14,24,16,12,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>9,8,3,7,6</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 4.5<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>1,4,1,1,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.4 | 1.5 | 26.1 |
| LeBron James (PHI) | 99% | 34.7<br><sub>-,31,35,30,35</sub> | 20.1<br><sub>-,22,21,23,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>-,3,6,6,10</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>-,6,6,3,12</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>-,1,0,4,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.6 | 2.6 | 34.1 |
| Joel Embiid (PHI) | 100% | 33.2<br><sub>32,36,34,-,-</sub> | 26.0<br><sub>37,26,26,-,-</sub> | 23.5 · – | 9.2<br><sub>5,6,17,-,-</sub> | 8.5 | 4.6<br><sub>1,7,9,-,-</sub> | 4.5 | 1.0<br><sub>2,0,0,-,-</sub> | 0.5 | 0.8 | 1.2 | 2.8 | 39.8 |
| Kentavious Caldwell-Pope (PHI) | 99% | 26.5<br><sub>31,32,35,17,28</sub> | 6.5<br><sub>0,8,11,2,5</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>2,8,1,3,1</sub> |  | 1.8<br><sub>3,1,2,1,3</sub> |  | 1.0<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.3 | 0.7 | 11.3 |
| Anfernee Simons (PHI) | 99% | 22.2<br><sub>26,38,26,18,15</sub> | 10.3<br><sub>9,18,18,3,6</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>1,2,0,0,1</sub> |  | 1.4<br><sub>2,2,1,0,1</sub> |  | 1.7<br><sub>1,3,4,0,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.5 | 0.1 | 0.7 | 13.9 |
| Jabari Walker (PHI) | 96% | 17.4<br><sub>16,13,20,20,17</sub> | 7.2<br><sub>12,6,9,10,7</sub> |  | 5.2<br><sub>5,5,7,5,2</sub> |  | 1.0<br><sub>1,2,4,2,1</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.2 | 0.6 | 13.4 |
| Dominick Barlow (PHI) | 93% | 16.5<br><sub>-,-,11,16,16</sub> | 5.5<br><sub>-,-,12,6,9</sub> |  | 3.9<br><sub>-,-,4,2,8</sub> |  | 0.8<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.6 | 0.6 | 0.6 | 10.2 |
| Adem Bona (PHI) | 98% | 13.5<br><sub>-,-,-,5,13</sub> | 3.6<br><sub>-,-,-,4,0</sub> |  | 3.8<br><sub>-,-,-,2,6</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.9 | 0.7 | 7.9 |
| Justin Edwards (PHI) | 52% | 8.1<br><sub>-,13,-,3,-</sub> | 3.2<br><sub>-,2,-,5,-</sub> |  | 1.2<br><sub>-,1,-,1,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,0,-,1,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.8 |
| Labaron Philon Jr. (PHI) | 64% | 8.0<br><sub>-,17,6,3,-</sub> | 3.1<br><sub>-,10,2,2,-</sub> |  | 1.0<br><sub>-,1,0,1,-</sub> |  | 0.7<br><sub>-,2,0,1,-</sub> |  | 0.2<br><sub>-,2,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Rayan Rupert (PHI) | 36% | 7.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.3 |
| Tacko Fall (PHI) | 48% | 7.0<br><sub>-,10,-,-,-</sub> | 5.3<br><sub>-,2,-,-,-</sub> |  | 2.1<br><sub>-,3,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.6 | 0.4 | 7.8 |
| Caleb Love (PHI) | 48% | 5.6<br><sub>-,6,-,-,-</sub> | 2.0<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,1,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.1 |

</details>


### BKN @ TOR
Out: RJ Barrett (TOR), Kawhi Leonard (TOR), Malachi Smith (TOR), Drake Powell (BKN), Nolan Traore (BKN), Moritz Wagner (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.4–113.4 | BKN 29% | 3.45 / 1.41 | TOR -7.5 | 218.5 | TOR -9.5 covers 46%; o218.5 51% |
| Expected (weighted by chance each plays) | 105.7–114.1 | BKN 28% | 3.57 / 1.39 | TOR -8.5 | 219.5 | TOR -9.5 covers 47%; o218.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alijah Martin (TOR) | Questionable | 55% | 13.3 | 4.8 | 1.9 | 0.9 | 0.5 | 0.6 | 0.2 | 0.8 | 7.7 | small |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 99% | 34.4<br><sub>34,27,39,35,39</sub> | 21.4<br><sub>33,17,27,29,28</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>6,0,9,4,9</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.4<br><sub>1,4,6,4,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,3,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 3.8 | 32.0 |
| Michael Porter Jr. | 91% | 32.9<br><sub>40,27,34,31,34</sub> | 19.1<br><sub>25,5,16,11,12</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 6.6<br><sub>6,3,4,6,11</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,1,5,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>2,1,3,0,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.3 | 2.3 | 27.9 |
| Day'Ron Sharpe | 99% | 26.3<br><sub>25,22,26,26,31</sub> | 10.7<br><sub>6,6,17,6,11</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>9,5,11,5,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>5,1,2,7,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.4<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.9 | 2.0 | 23.2 |
| Egor Demin | 98% | 25.4<br><sub>26,31,21,25,25</sub> | 11.2<br><sub>9,22,6,10,15</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>3,4,3,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,4,2,4,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>2,3,0,2,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.3 | 2.0 | 17.2 |
| Mikel Brown Jr. | 98% | 23.9<br><sub>18,27,24,29,23</sub> | 11.4<br><sub>3,15,18,17,6</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>1,1,1,5,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>5,4,0,7,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,2,3,4,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 2.4 | 17.0 |
| Noah Clowney | 99% | 23.0<br><sub>24,19,22,26,27</sub> | 8.8<br><sub>9,7,0,13,17</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,3,2,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.1<br><sub>3,1,2,1,1</sub> |  | 1.2<br><sub>1,1,0,3,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.6 | 1.1 | 13.7 |
| Danny Wolf | 91% | 21.1<br><sub>11,23,26,25,19</sub> | 8.5<br><sub>3,6,20,11,5</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>2,6,5,5,0</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,2,2,4,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>1,1,4,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.5 | 0.5 | 1.4 | 15.0 |
| Keon Ellis | 93% | 18.8<br><sub>20,6,8,16,23</sub> | 4.7<br><sub>8,3,0,6,7</sub> |  | 1.9<br><sub>2,1,1,0,2</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 0.6<br><sub>2,1,0,2,1</sub> |  | 0.9 | 0.6 | 0.7 | 7.8 |
| Ben Saraf | 52% | 11.6<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.6 | 7.5 |
| Grant Nelson | 88% | 11.5<br><sub>-,-,-,8,13</sub> | 3.8<br><sub>-,-,-,2,1</sub> |  | 2.6<br><sub>-,-,-,1,6</sub> |  | 0.8<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.6 | 0.8 | 7.3 |
| Terance Mann | 67% | 10.9<br><sub>-,5,-,3,2</sub> | 2.9<br><sub>-,0,-,0,0</sub> |  | 1.3<br><sub>-,1,-,0,0</sub> |  | 1.0<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Chaney Johnson | 76% | 9.8<br><sub>1,6,-,-,-</sub> | 2.8<br><sub>0,2,-,-,-</sub> |  | 1.6<br><sub>0,2,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.6 | 4.8 |
| Josh Minott | 52% | 8.0<br><sub>-,4,-,2,-</sub> | 3.9<br><sub>-,0,-,0,-</sub> |  | 1.4<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.2 | 0.5 | 5.7 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 36.0<br><sub>36,34,-,37,38</sub> | 26.9<br><sub>30,20,-,29,31</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>9,4,-,5,5</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 7.2<br><sub>4,2,-,5,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>4,1,-,0,2</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.8 | 1.3 | 3.3 | 41.4 |
| Ja'Kobe Walter | 99% | 34.0<br><sub>36,33,38,33,36</sub> | 14.6<br><sub>7,25,18,8,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>2,1,7,3,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>1,2,6,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.5<br><sub>1,7,3,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.7 | 0.3 | 1.2 | 21.3 |
| Immanuel Quickley | 91% | 33.2<br><sub>38,34,34,33,32</sub> | 19.4<br><sub>17,14,24,18,13</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>6,1,3,3,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>6,7,5,10,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>3,2,4,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.1 | 1.9 | 30.3 |
| Jakob Poeltl | 96% | 28.2<br><sub>17,18,29,32,28</sub> | 12.0<br><sub>11,3,8,10,15</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>5,6,9,9,10</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>1,1,5,3,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 1.3 | 1.6 | 23.2 |
| Allen Graves | 98% | 27.0<br><sub>16,13,31,33,31</sub> | 9.0<br><sub>2,3,9,20,7</sub> | 10.5 · –<br><sub>o 44% · u 56%</sub> | 4.7<br><sub>5,2,4,10,2</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>0,1,1,2,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.6 | 1.0 | 15.1 |
| Collin Murray-Boyles | 84% | 26.6<br><sub>40,33,5,-,24</sub> | 11.5<br><sub>6,8,1,-,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>13,1,2,-,10</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,3,1,-,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.4<br><sub>0,0,0,-,0</sub> |  | 1.2 | 1.2 | 1.8 | 19.8 |
| Jamal Shead | 99% | 26.1<br><sub>26,20,24,15,26</sub> | 9.4<br><sub>19,7,15,0,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,0,1,1,2</sub> |  | 6.9<br><sub>4,6,6,4,6</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>3,1,1,0,3</sub> |  | 1.1 | 0.2 | 2.0 | 18.4 |
| Jamison Battle | 98% | 22.0<br><sub>8,7,33,20,13</sub> | 10.7<br><sub>0,0,19,10,13</sub> |  | 2.9<br><sub>3,1,5,5,2</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 1.9<br><sub>0,0,5,2,3</sub> |  | 0.5 | 0.1 | 0.7 | 14.4 |
| Trayce Jackson-Davis | 67% | 13.3<br><sub>-,-,17,16,5</sub> | 4.9<br><sub>-,-,3,8,0</sub> |  | 4.1<br><sub>-,-,7,2,2</sub> |  | 0.9<br><sub>-,-,1,1,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.9 | 0.8 | 0.6 | 9.9 |
| Kyle Anderson | 52% | 11.0<br><sub>-,-,4,-,-</sub> | 3.2<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 2.0<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.4 | 0.6 | 7.2 |
| Jaden Bradley | 43% | 8.2<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 5.2 |

</details>


### ATL @ BOS
Out: Devin Carter (BOS), Mitchell Robinson (BOS), Mouhamed Gueye (ATL), Jock Landale (ATL), CJ McCollum (ATL), Asa Newell (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.2–116.6 | ATL 28% | 3.58 / 1.39 | BOS -8.5 | 224.5 | BOS -8.5 covers 50%; o223.5 53% |
| Expected (weighted by chance each plays) | 108.3–116.5 | ATL 28% | 3.58 / 1.39 | BOS -8.5 | 225.5 | BOS -8.5 covers 49%; o223.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 9.6 | 3.5 | 1.6 | 0.6 | 0.3 | 0.2 | 0.1 | 0.4 | 5.7 | small |
| Rafael Castro (ATL) | Doubtful | 20% | 8.6 | 3.7 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 | small |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 36.0<br><sub>40,35,34,36,30</sub> | 20.1<br><sub>27,14,16,26,12</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 9.5<br><sub>11,11,12,6,11</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 6.5<br><sub>10,5,11,6,0</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 3.3 | 36.0 |
| Dyson Daniels | 99% | 35.0<br><sub>36,27,37,35,39</sub> | 11.3<br><sub>6,9,10,11,5</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 8.0<br><sub>9,10,10,8,14</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>4,5,4,10,8</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 0.5<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 36% · u 64%</sub> | 2.2 | 0.5 | 1.8 | 25.0 |
| Nickeil Alexander-Walker | 99% | 34.2<br><sub>41,33,32,32,28</sub> | 20.1<br><sub>16,20,19,17,27</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>6,5,4,4,2</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 3.1<br><sub>3,4,7,3,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>1,2,3,2,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.5 | 2.0 | 26.8 |
| Onyeka Okongwu | 99% | 33.7<br><sub>35,36,36,34,29</sub> | 14.9<br><sub>17,16,28,16,6</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 8.4<br><sub>6,11,9,7,9</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>1,0,2,1,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>2,3,5,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.9 | 1.7 | 25.8 |
| Luguentz Dort | 99% | 28.4<br><sub>20,18,31,23,31</sub> | 10.4<br><sub>10,3,16,2,16</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>1,4,3,1,7</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>2,0,0,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.6<br><sub>1,0,3,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 0.8 | 15.3 |
| Aaron Wiggins | 98% | 26.1<br><sub>26,24,26,34,19</sub> | 12.1<br><sub>9,7,14,19,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>4,3,3,2,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>3,3,1,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>1,1,4,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.3 | 1.3 | 17.5 |
| Kingston Flemings | 58% | 23.5<br><sub>17,-,-,-,27</sub> | 8.7<br><sub>0,-,-,-,10</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>1,-,-,-,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.9<br><sub>1,-,-,-,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.7<br><sub>0,-,-,-,1</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.3 | 1.8 | 15.4 |
| Corey Kispert | 71% | 15.5<br><sub>-,16,17,16,19</sub> | 7.2<br><sub>-,14,8,7,18</sub> |  | 2.1<br><sub>-,3,1,3,4</sub> |  | 1.1<br><sub>-,1,2,0,3</sub> |  | 1.1<br><sub>-,3,2,1,4</sub> |  | 0.2 | 0.1 | 0.6 | 10.4 |
| Zuby Ejiofor | 86% | 14.6<br><sub>-,12,12,14,19</sub> | 4.9<br><sub>-,4,3,5,4</sub> |  | 3.2<br><sub>-,3,3,2,4</sub> |  | 1.1<br><sub>-,0,0,2,1</sub> |  | 0.4<br><sub>-,1,1,0,0</sub> |  | 0.3 | 0.3 | 0.7 | 9.2 |
| RayJ Dennis | 63% | 11.6<br><sub>-,10,10,13,-</sub> | 4.9<br><sub>-,6,3,8,-</sub> |  | 1.8<br><sub>-,1,3,4,-</sub> |  | 1.9<br><sub>-,3,5,2,-</sub> |  | 0.5<br><sub>-,1,1,0,-</sub> |  | 0.4 | 0.2 | 0.7 | 8.6 |
| Dorian Finney-Smith | 48% | 6.9<br><sub>-,-,5,3,-</sub> | 1.9<br><sub>-,-,0,0,-</sub> |  | 1.1<br><sub>-,-,2,0,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 99% | 34.8<br><sub>36,37,-,38,37</sub> | 27.2<br><sub>24,24,-,27,41</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 8.9<br><sub>12,8,-,10,6</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 6.5<br><sub>4,3,-,6,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>3,3,-,4,6</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 3.3 | 42.7 |
| Paul George | 99% | 31.2<br><sub>36,23,37,-,33</sub> | 19.4<br><sub>22,10,19,-,28</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>8,4,8,-,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,1,5,-,9</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>5,1,2,-,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8 | 0.5 | 2.2 | 28.4 |
| Derrick White | 88% | 31.1<br><sub>32,35,-,32,30</sub> | 13.6<br><sub>9,12,-,14,6</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,3,-,3,7</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.6<br><sub>2,8,-,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,0,-,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.9 | 1.4 | 21.9 |
| Payton Pritchard | 99% | 28.6<br><sub>32,30,34,28,28</sub> | 13.9<br><sub>21,15,9,5,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>4,1,6,1,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.1<br><sub>5,2,8,4,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>4,3,0,1,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.1 | 1.2 | 21.3 |
| Neemias Queta | 99% | 25.5<br><sub>-,27,30,30,25</sub> | 11.6<br><sub>-,17,15,6,21</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 8.7<br><sub>-,10,7,10,5</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>-,3,1,4,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.2<br><sub>-,0,1,0,0</sub> | 0.5<br><sub>o 15% · u 85%</sub> | 0.7 | 1.3 | 1.4 | 22.4 |
| Sam Hauser | 99% | 21.8<br><sub>25,17,31,22,22</sub> | 7.8<br><sub>12,9,14,3,4</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>1,2,6,1,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.5<br><sub>4,3,4,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.4 | 0.2 | 0.3 | 12.1 |
| Baylor Scheierman | 99% | 18.1<br><sub>11,13,18,15,19</sub> | 5.5<br><sub>0,0,4,3,8</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>1,1,3,4,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>1,1,1,1,1</sub> |  | 0.8<br><sub>0,0,0,1,2</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.7 | 0.1 | 0.6 | 10.1 |
| Luka Garza | 98% | 15.3<br><sub>18,5,17,17,18</sub> | 7.3<br><sub>3,0,5,10,7</sub> |  | 3.8<br><sub>0,1,5,5,4</sub> |  | 1.4<br><sub>4,1,1,0,0</sub> |  | 0.7<br><sub>1,0,0,0,1</sub> |  | 0.4 | 0.4 | 0.7 | 12.4 |
| Hugo Gonzalez | 98% | 12.5<br><sub>4,16,17,22,9</sub> | 3.8<br><sub>0,2,5,6,0</sub> |  | 2.6<br><sub>2,6,4,2,5</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.4<br><sub>0,0,1,2,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.9 |
| Jordan Walsh | 99% | 9.9<br><sub>17,4,8,9,5</sub> | 3.0<br><sub>6,0,1,2,0</sub> |  | 1.9<br><sub>2,0,4,0,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.2<br><sub>2,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.3 |
| Mike Conley | 52% | 9.7<br><sub>-,-,18,16,-</sub> | 3.3<br><sub>-,-,19,6,-</sub> |  | 1.1<br><sub>-,-,4,2,-</sub> |  | 1.4<br><sub>-,-,2,4,-</sub> |  | 0.4<br><sub>-,-,4,2,-</sub> |  | 0.5 | 0.1 | 0.5 | 5.8 |
| Ron Harper Jr. | 67% | 8.2<br><sub>-,-,13,6,8</sub> | 3.5<br><sub>-,-,3,5,2</sub> |  | 1.1<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,1,0,0</sub> |  | 0.4<br><sub>-,-,1,1,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.1 |
| Chris Cenac Jr. | 80% | 8.0<br><sub>12,17,12,5,6</sub> | 3.1<br><sub>4,6,2,0,0</sub> |  | 2.1<br><sub>2,6,3,2,2</sub> |  | 0.4<br><sub>1,0,0,0,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |

</details>


### MEM @ MIN
Out: LaMelo Ball (MIN), Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.3–115.7 | MEM 35% | 2.85 / 1.54 | MIN -5.5 | 225.5 | MIN -2.5 covers 59%; o220.5 62% |
| Expected (weighted by chance each plays) | 111.2–115.3 | MEM 39% | 2.58 / 1.63 | MIN -4.5 | 226.5 | MIN -2.5 covers 55%; o220.5 63% |
| if Zach Edey plays | 111.4–115.4 | MEM 39% | 2.58 / 1.63 | MIN -4.5 | 226.5 | MIN -2.5 covers 55%; o220.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey (MEM) | Questionable | 55% | 21.5 | 8.7 | 7.6 | 1.1 | 0.0 | 0.6 | 1.3 | 1.4 | 17.3 | full tables below |
| Isaiah Stewart (MEM) | Questionable | 55% | 19.3 | 8.9 | 3.9 | 1.0 | 0.6 | 0.4 | 1.2 | 0.9 | 13.8 | small |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 31.9<br><sub>33,25,30,30,26</sub> | 17.5<br><sub>20,19,23,16,14</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>3,4,7,9,10</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,4,2,3,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.9<br><sub>4,5,4,0,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 2.3 | 28.9 |
| Ty Jerome | 98% | 30.3<br><sub>-,-,27,29,25</sub> | 24.0<br><sub>-,-,18,29,17</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>-,-,4,4,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>-,-,6,3,7</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>-,-,3,7,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 2.6 | 32.8 |
| Jaylen Wells | 99% | 29.0<br><sub>26,24,25,20,27</sub> | 12.1<br><sub>5,22,8,8,19</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,7,1,2,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>2,0,0,0,1</sub> |  | 1.6<br><sub>1,4,0,2,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 1.0 | 16.8 |
| Kris Murray | 91% | 27.8<br><sub>6,4,12,32,32</sub> | 6.1<br><sub>5,0,7,9,8</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>0,1,0,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>1,0,1,1,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.6 | 0.9 | 11.4 |
| Cam Spencer | 99% | 27.0<br><sub>29,27,30,21,24</sub> | 13.2<br><sub>26,9,9,24,16</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>1,2,5,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>7,11,5,5,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>5,1,0,3,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 1.6 | 21.9 |
| Taylor Hendricks | 91% | 26.8<br><sub>21,20,27,24,25</sub> | 10.3<br><sub>18,11,5,3,5</sub> |  | 5.2<br><sub>6,1,7,4,0</sub> |  | 1.3<br><sub>2,1,2,1,1</sub> |  | 1.1<br><sub>1,0,0,1,0</sub> |  | 1.1 | 0.7 | 1.3 | 16.8 |
| Javon Small | 98% | 23.8<br><sub>21,25,-,19,17</sub> | 11.0<br><sub>2,14,-,3,8</sub> |  | 3.6<br><sub>4,7,-,3,2</sub> |  | 3.9<br><sub>5,7,-,5,1</sub> |  | 1.4<br><sub>0,2,-,0,2</sub> |  | 0.9 | 0.2 | 1.5 | 18.4 |
| Olivier-Maxence Prosper | 91% | 23.7<br><sub>16,24,23,19,19</sub> | 11.8<br><sub>5,16,7,6,9</sub> |  | 4.5<br><sub>2,5,6,3,4</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 1.1<br><sub>0,1,0,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 17.5 |
| Quinten Post | 86% | 16.7<br><sub>6,10,-,3,14</sub> | 5.7<br><sub>3,5,-,0,0</sub> |  | 3.3<br><sub>2,1,-,0,4</sub> |  | 0.5<br><sub>0,0,-,0,0</sub> |  | 0.7<br><sub>1,0,-,0,0</sub> |  | 0.5 | 0.4 | 0.7 | 9.5 |
| Jahmai Mashack | 67% | 15.4<br><sub>13,26,22,-,4</sub> | 3.6<br><sub>3,0,0,-,0</sub> |  | 2.0<br><sub>2,3,2,-,0</sub> |  | 1.6<br><sub>2,4,1,-,0</sub> |  | 0.3<br><sub>1,0,0,-,0</sub> |  | 0.7 | 0.3 | 0.8 | 7.3 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 36.5<br><sub>37,39,36,34,37</sub> | 21.7<br><sub>22,17,25,34,32</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>5,3,5,10,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>4,1,4,6,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>2,4,1,4,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3 | 1.1 | 2.3 | 32.3 |
| Ayo Dosunmu | 99% | 35.4<br><sub>39,32,34,30,35</sub> | 22.3<br><sub>30,6,19,23,16</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>4,4,2,3,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>5,4,2,5,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>7,2,1,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.4 | 2.7 | 31.9 |
| Jonathan Kuminga | 88% | 33.2<br><sub>-,35,37,26,32</sub> | 16.3<br><sub>-,23,16,15,7</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>-,3,4,5,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>-,3,2,4,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>-,2,2,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.8 | 2.2 | 25.3 |
| Rudy Gobert | 99% | 32.7<br><sub>22,35,32,27,32</sub> | 10.7<br><sub>0,9,7,7,9</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 12.0<br><sub>4,7,11,6,7</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,0,2,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.6 | 1.6 | 24.9 |
| Terrence Shannon Jr. | 98% | 27.0<br><sub>24,21,26,24,20</sub> | 16.6<br><sub>12,10,15,17,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>1,4,5,1,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,3,2,5,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,0,3,2,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.2 | 1.7 | 23.4 |
| Trey Lyles | 99% | 22.7<br><sub>31,16,12,24,23</sub> | 7.7<br><sub>8,8,3,9,9</sub> |  | 5.2<br><sub>7,6,3,3,10</sub> |  | 1.5<br><sub>4,1,1,2,1</sub> |  | 1.1<br><sub>2,2,1,0,3</sub> |  | 0.7 | 0.4 | 0.8 | 14.4 |
| Bones Hyland | 98% | 21.0<br><sub>17,15,16,16,17</sub> | 13.0<br><sub>13,6,7,14,9</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,1,0,2,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 4.0<br><sub>1,1,4,6,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>3,1,1,4,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.3 | 1.3 | 19.2 |
| Joan Beringer | 98% | 18.3<br><sub>26,13,16,19,16</sub> | 6.0<br><sub>3,5,0,0,4</sub> |  | 6.5<br><sub>13,3,4,4,5</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.9 | 0.8 | 13.1 |
| Zyon Pullin | 52% | 9.0<br><sub>-,-,-,2,-</sub> | 3.8<br><sub>-,-,-,4,-</sub> |  | 1.2<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 6.3 |
| Cody Williams | 52% | 8.0<br><sub>13,-,-,2,-</sub> | 0.1<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 1.5 |
| Isaiah Evans | 48% | 6.8<br><sub>-,-,-,2,-</sub> | 3.6<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.3 |
| Johni Broome | 48% | 6.7<br><sub>-,-,-,2,-</sub> | 2.5<br><sub>-,-,-,0,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.6 |

</details>

<details><summary>if Zach Edey plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward (MEM) | 99% | 31.6<br><sub>33,25,30,30,26</sub> | 16.4<br><sub>20,19,23,16,14</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>3,4,7,9,10</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,4,2,3,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.8<br><sub>4,5,4,0,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 2.1 | 27.2 |
| Ty Jerome (MEM) | 98% | 30.4<br><sub>-,-,27,29,25</sub> | 23.0<br><sub>-,-,18,29,17</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>-,-,4,4,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>-,-,6,3,7</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>-,-,3,7,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.3 | 2.7 | 31.8 |
| Jaylen Wells (MEM) | 99% | 28.2<br><sub>26,24,25,20,27</sub> | 11.6<br><sub>5,22,8,8,19</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,7,1,2,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>2,0,0,0,1</sub> |  | 1.6<br><sub>1,4,0,2,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 0.9 | 16.2 |
| Cam Spencer (MEM) | 99% | 26.3<br><sub>29,27,30,21,24</sub> | 12.6<br><sub>26,9,9,24,16</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,2,5,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>7,11,5,5,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>5,1,0,3,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 1.4 | 21.0 |
| Kris Murray (MEM) | 91% | 25.1<br><sub>6,4,12,32,32</sub> | 5.7<br><sub>5,0,7,9,8</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>0,1,0,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>1,0,1,1,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.5 | 0.8 | 10.5 |
| Taylor Hendricks (MEM) | 91% | 24.6<br><sub>21,20,27,24,25</sub> | 9.8<br><sub>18,11,5,3,5</sub> |  | 4.8<br><sub>6,1,7,4,0</sub> |  | 1.2<br><sub>2,1,2,1,1</sub> |  | 1.0<br><sub>1,0,0,1,0</sub> |  | 1.0 | 0.7 | 1.2 | 15.7 |
| Javon Small (MEM) | 98% | 22.4<br><sub>21,25,-,19,17</sub> | 10.1<br><sub>2,14,-,3,8</sub> |  | 3.3<br><sub>4,7,-,3,2</sub> |  | 3.7<br><sub>5,7,-,5,1</sub> |  | 1.2<br><sub>0,2,-,0,2</sub> |  | 0.8 | 0.2 | 1.4 | 17.2 |
| Zach Edey (MEM) | 100% | 21.5<br><sub>21,-,23,23,9</sub> | 8.7<br><sub>11,-,8,8,7</sub> | 8.5 · – | 7.6<br><sub>2,-,2,11,4</sub> | 7.5 | 1.1<br><sub>1,-,0,1,2</sub> | 1.5 | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.3 | 1.4 | 17.3 |
| Olivier-Maxence Prosper (MEM) | 91% | 20.7<br><sub>16,24,23,19,19</sub> | 10.4<br><sub>5,16,7,6,9</sub> |  | 3.9<br><sub>2,5,6,3,4</sub> |  | 1.0<br><sub>0,1,0,0,2</sub> |  | 0.9<br><sub>0,1,0,0,1</sub> |  | 0.8 | 0.3 | 1.1 | 15.3 |
| Jahmai Mashack (MEM) | 67% | 13.6<br><sub>13,26,22,-,4</sub> | 3.3<br><sub>3,0,0,-,0</sub> |  | 1.8<br><sub>2,3,2,-,0</sub> |  | 1.4<br><sub>2,4,1,-,0</sub> |  | 0.2<br><sub>1,0,0,-,0</sub> |  | 0.6 | 0.3 | 0.8 | 6.5 |
| Quinten Post (MEM) | 86% | 13.3<br><sub>6,10,-,3,14</sub> | 4.5<br><sub>3,5,-,0,0</sub> |  | 2.6<br><sub>2,1,-,0,4</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.5<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.5 |
| Jaden McDaniels (MIN) | 99% | 36.5<br><sub>37,39,36,34,37</sub> | 21.7<br><sub>22,17,25,34,32</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>5,3,5,10,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>4,1,4,6,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>2,4,1,4,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3 | 1.1 | 2.3 | 32.2 |
| Ayo Dosunmu (MIN) | 99% | 35.4<br><sub>39,32,34,30,35</sub> | 22.4<br><sub>30,6,19,23,16</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>4,4,2,3,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>5,4,2,5,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>7,2,1,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.4 | 2.7 | 32.0 |
| Jonathan Kuminga (MIN) | 88% | 33.1<br><sub>-,35,37,26,32</sub> | 16.2<br><sub>-,23,16,15,7</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>-,3,4,5,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>-,3,2,4,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>-,2,2,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.8 | 2.2 | 25.3 |
| Rudy Gobert (MIN) | 99% | 32.7<br><sub>22,35,32,27,32</sub> | 10.7<br><sub>0,9,7,7,9</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 12.0<br><sub>4,7,11,6,7</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,0,2,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.6 | 1.6 | 24.9 |
| Terrence Shannon Jr. (MIN) | 98% | 27.0<br><sub>24,21,26,24,20</sub> | 16.5<br><sub>12,10,15,17,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>1,4,5,1,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>4,3,2,5,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,0,3,2,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.2 | 1.7 | 23.4 |
| Trey Lyles (MIN) | 99% | 22.7<br><sub>31,16,12,24,23</sub> | 7.7<br><sub>8,8,3,9,9</sub> |  | 5.2<br><sub>7,6,3,3,10</sub> |  | 1.5<br><sub>4,1,1,2,1</sub> |  | 1.1<br><sub>2,2,1,0,3</sub> |  | 0.7 | 0.4 | 0.8 | 14.4 |
| Bones Hyland (MIN) | 98% | 21.0<br><sub>17,15,16,16,17</sub> | 13.0<br><sub>13,6,7,14,9</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,1,0,2,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 4.0<br><sub>1,1,4,6,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>3,1,1,4,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.4 | 1.3 | 19.2 |
| Joan Beringer (MIN) | 98% | 18.4<br><sub>26,13,16,19,16</sub> | 6.0<br><sub>3,5,0,0,4</sub> |  | 6.5<br><sub>13,3,4,4,5</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.9 | 0.8 | 13.1 |
| Zyon Pullin (MIN) | 52% | 9.0<br><sub>-,-,-,2,-</sub> | 3.8<br><sub>-,-,-,4,-</sub> |  | 1.3<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 6.3 |
| Cody Williams (MIN) | 52% | 7.9<br><sub>13,-,-,2,-</sub> | 0.1<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 1.5 |
| Isaiah Evans (MIN) | 48% | 6.9<br><sub>-,-,-,2,-</sub> | 3.6<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.3 |
| Johni Broome (MIN) | 48% | 6.6<br><sub>-,-,-,2,-</sub> | 2.5<br><sub>-,-,-,0,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.6 |

</details>


### DAL @ PHX
Out: Mark Williams (PHX), Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.1–117.3 | DAL 36% | 2.81 / 1.55 | PHX -5.5 | 229.5 | PHX -3.5 covers 55%; o225.5 58% |
| Expected (weighted by chance each plays) | 112.8–116.7 | DAL 39% | 2.55 / 1.64 | PHX -4.5 | 229.5 | PHX -3.5 covers 52%; o225.5 58% |
| if Kyrie Irving plays | 113.4–116.2 | DAL 42% | 2.37 / 1.73 | PHX -3.5 | 229.5 | PHX -3.5 covers 49%; o225.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving (DAL) | Questionable | 55% | 32.4 | 21.0 | 4.2 | 4.4 | 2.7 | 1.2 | 0.4 | 2.0 | 29.6 | full tables below |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 99% | 34.9<br><sub>27,34,36,31,31</sub> | 25.5<br><sub>17,33,22,28,24</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>3,5,6,3,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>4,9,8,4,12</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>2,3,3,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.7 | 3.1 | 38.6 |
| P.J. Washington | 99% | 31.0<br><sub>25,25,-,-,25</sub> | 14.4<br><sub>8,21,-,-,14</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>5,5,-,-,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>4,2,-,-,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.7<br><sub>0,5,-,-,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.9 | 1.7 | 22.7 |
| Daniel Gafford | 99% | 26.3<br><sub>19,24,31,28,27</sub> | 11.9<br><sub>3,6,10,10,13</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>4,6,10,4,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,2,3,4,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.4 | 21.1 |
| Caleb Martin | 98% | 25.6<br><sub>34,20,20,29,30</sub> | 7.5<br><sub>12,8,0,13,13</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,5,4,6,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>5,3,3,4,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.9<br><sub>4,2,0,3,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.3 | 1.0 | 13.8 |
| Naji Marshall | 97% | 25.2<br><sub>23,27,14,25,22</sub> | 12.6<br><sub>13,12,4,6,14</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,5,3,0,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>2,2,1,4,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.9<br><sub>3,2,0,1,1</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.1 | 1.7 | 19.1 |
| Zaccharie Risacher | 98% | 23.9<br><sub>27,18,29,28,21</sub> | 9.3<br><sub>18,3,11,15,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,3,7,8,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,0,1,2,1</sub> |  | 0.9<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.7 | 1.2 | 15.4 |
| Walter Clayton Jr. | 97% | 20.7<br><sub>23,27,25,21,14</sub> | 8.3<br><sub>13,8,16,9,5</sub> |  | 2.9<br><sub>4,2,5,0,2</sub> |  | 3.2<br><sub>3,7,1,3,2</sub> |  | 1.2<br><sub>3,2,2,2,1</sub> |  | 0.6 | 0.1 | 1.7 | 14.3 |
| Morez Johnson Jr. | 99% | 17.6<br><sub>26,15,17,20,19</sub> | 6.5<br><sub>2,3,9,7,9</sub> |  | 3.7<br><sub>6,1,7,6,10</sub> |  | 1.5<br><sub>4,1,2,2,1</sub> |  | 0.4<br><sub>0,0,1,1,1</sub> |  | 0.6 | 0.1 | 1.1 | 11.7 |
| Max Christie | 99% | 16.6<br><sub>-,8,24,16,4</sub> | 6.3<br><sub>-,5,13,3,2</sub> |  | 2.0<br><sub>-,1,4,2,1</sub> |  | 1.0<br><sub>-,2,0,0,0</sub> |  | 0.9<br><sub>-,1,3,1,0</sub> |  | 0.5 | 0.2 | 0.8 | 9.2 |
| Santi Aldama | 98% | 13.8<br><sub>-,6,9,16,10</sub> | 6.2<br><sub>-,0,0,9,3</sub> |  | 3.0<br><sub>-,0,1,4,1</sub> |  | 1.1<br><sub>-,0,0,1,0</sub> |  | 0.7<br><sub>-,0,0,1,1</sub> |  | 0.4 | 0.3 | 0.7 | 10.2 |
| Marcus Sasser | 48% | 12.5<br><sub>18,4,-,-,-</sub> | 4.5<br><sub>5,0,-,-,-</sub> |  | 1.2<br><sub>1,2,-,-,-</sub> |  | 1.5<br><sub>2,1,-,-,-</sub> |  | 0.6<br><sub>1,0,-,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 7.2 |
| Moussa Cisse | 58% | 7.3<br><sub>4,4,-,-,2</sub> | 2.5<br><sub>1,0,-,-,0</sub> |  | 2.8<br><sub>1,1,-,-,0</sub> |  | 0.2<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.4 |
| Jett Howard | 52% | 7.1<br><sub>7,-,-,-,-</sub> | 2.9<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 99% | 36.1<br><sub>37,33,38,42,36</sub> | 26.5<br><sub>20,29,23,22,25</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>4,2,2,5,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.6<br><sub>8,6,3,8,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>1,2,1,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 3.0 | 36.8 |
| Dillon Brooks | 99% | 30.3<br><sub>27,31,25,34,31</sub> | 17.1<br><sub>15,29,18,16,12</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,3,3,5,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,5,3,7,4</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 2.1<br><sub>3,5,2,2,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.5 | 23.7 |
| Jalen Green | 98% | 30.1<br><sub>27,30,25,37,35</sub> | 17.0<br><sub>16,18,14,25,16</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>5,7,4,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>3,7,3,0,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,4,1,3,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.4 | 24.7 |
| Miles Bridges | 99% | 28.6<br><sub>29,29,25,35,25</sub> | 13.7<br><sub>16,13,18,14,2</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>8,6,9,11,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,5,4,5,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>2,1,1,2,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.5 | 1.1 | 23.5 |
| Collin Gillespie | 99% | 24.0<br><sub>26,17,27,30,22</sub> | 10.1<br><sub>10,9,16,18,5</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,3,4,3,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.6<br><sub>3,1,5,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>2,2,3,3,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.1 | 1.2 | 17.0 |
| Oso Ighodaro | 99% | 23.2<br><sub>33,21,27,30,20</sub> | 6.6<br><sub>8,7,3,7,13</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>11,4,7,4,2</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.9 | 1.2 | 15.1 |
| Jordan Goodwin | 98% | 18.9<br><sub>20,17,28,18,17</sub> | 7.6<br><sub>11,2,5,6,11</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>6,5,9,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>2,3,4,2,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>1,0,1,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.2 | 0.7 | 13.9 |
| Khaman Maluach | 98% | 18.0<br><sub>11,21,18,16,25</sub> | 7.3<br><sub>4,10,9,8,12</sub> |  | 5.8<br><sub>6,2,6,6,6</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.1 | 1.1 | 13.8 |
| Luke Kennard | 99% | 16.8<br><sub>17,17,15,14,19</sub> | 6.9<br><sub>12,3,5,4,8</sub> |  | 1.9<br><sub>2,3,0,1,1</sub> |  | 1.6<br><sub>0,1,0,2,2</sub> |  | 1.0<br><sub>4,1,1,0,1</sub> |  | 0.5 | 0.1 | 0.6 | 10.5 |
| Ryan Dunn | 98% | 12.9<br><sub>12,13,9,9,10</sub> | 3.7<br><sub>5,6,0,3,0</sub> |  | 3.1<br><sub>1,5,5,2,2</sub> |  | 0.9<br><sub>0,2,0,0,1</sub> |  | 0.3<br><sub>1,0,0,1,0</sub> |  | 0.5 | 0.3 | 0.4 | 7.7 |
| Rasheer Fleming | 38% | 6.9<br><sub>-,4,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.0 |
| Pat Spencer | 48% | 6.4<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.4 |
| Jamaree Bouyea | 38% | 6.3<br><sub>-,4,-,-,-</sub> | 2.6<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,1,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Drew Timme | 3% | 6.2 | 2.4 |  | 1.2 |  | 0.7 |  | 0.2 |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Duop Reath | 38% | 6.0<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |
| Koa Peat | 52% | 6.0<br><sub>1,4,3,-,-</sub> | 3.0<br><sub>0,2,0,-,-</sub> |  | 1.4<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |

</details>

<details><summary>if Kyrie Irving plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 99% | 32.8<br><sub>27,34,36,31,31</sub> | 22.5<br><sub>17,33,22,28,24</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>3,5,6,3,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>4,9,8,4,12</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>2,3,3,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.7 | 2.9 | 34.6 |
| Kyrie Irving (DAL) | 100% | 32.4<br><sub>-,29,35,27,34</sub> | 21.0<br><sub>-,17,25,16,11</sub> | 22.5 · – | 4.2<br><sub>-,6,6,1,5</sub> | 4.5 | 4.4<br><sub>-,5,4,8,6</sub> | 4.5 | 2.7<br><sub>-,1,3,4,1</sub> | 3.5 | 1.2 | 0.4 | 2.0 | 29.6 |
| P.J. Washington (DAL) | 99% | 28.4<br><sub>25,25,-,-,25</sub> | 12.4<br><sub>8,21,-,-,14</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>5,5,-,-,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>4,2,-,-,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.5<br><sub>0,5,-,-,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.8 | 1.5 | 19.9 |
| Daniel Gafford (DAL) | 99% | 23.2<br><sub>19,24,31,28,27</sub> | 10.0<br><sub>3,6,10,10,13</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 6.4<br><sub>4,6,10,4,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>2,2,3,4,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.2 | 17.9 |
| Naji Marshall (DAL) | 97% | 22.5<br><sub>23,27,14,25,22</sub> | 10.5<br><sub>13,12,4,6,14</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>2,5,3,0,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>2,2,1,4,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.8<br><sub>3,2,0,1,1</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.1 | 1.5 | 16.2 |
| Caleb Martin (DAL) | 98% | 21.9<br><sub>34,20,20,29,30</sub> | 6.0<br><sub>12,8,0,13,13</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>5,5,4,6,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>5,3,3,4,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.7<br><sub>4,2,0,3,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.3 | 0.8 | 11.4 |
| Zaccharie Risacher (DAL) | 98% | 21.0<br><sub>27,18,29,28,21</sub> | 8.0<br><sub>18,3,11,15,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>5,3,7,8,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>0,0,1,2,1</sub> |  | 0.8<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.7 | 0.6 | 1.0 | 13.4 |
| Walter Clayton Jr. (DAL) | 97% | 16.4<br><sub>23,27,25,21,14</sub> | 6.3<br><sub>13,8,16,9,5</sub> |  | 2.4<br><sub>4,2,5,0,2</sub> |  | 2.5<br><sub>3,7,1,3,2</sub> |  | 0.8<br><sub>3,2,2,2,1</sub> |  | 0.5 | 0.1 | 1.3 | 11.2 |
| Morez Johnson Jr. (DAL) | 99% | 15.2<br><sub>26,15,17,20,19</sub> | 5.5<br><sub>2,3,9,7,9</sub> |  | 3.3<br><sub>6,1,7,6,10</sub> |  | 1.2<br><sub>4,1,2,2,1</sub> |  | 0.3<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.1 | 1.0 | 9.9 |
| Max Christie (DAL) | 99% | 12.5<br><sub>-,8,24,16,4</sub> | 4.5<br><sub>-,5,13,3,2</sub> |  | 1.6<br><sub>-,1,4,2,1</sub> |  | 0.7<br><sub>-,2,0,0,0</sub> |  | 0.6<br><sub>-,1,3,1,0</sub> |  | 0.3 | 0.2 | 0.6 | 6.8 |
| Santi Aldama (DAL) | 98% | 12.3<br><sub>-,6,9,16,10</sub> | 5.3<br><sub>-,0,0,9,3</sub> |  | 2.7<br><sub>-,0,1,4,1</sub> |  | 0.9<br><sub>-,0,0,1,0</sub> |  | 0.6<br><sub>-,0,0,1,1</sub> |  | 0.4 | 0.2 | 0.7 | 9.0 |
| Marcus Sasser (DAL) | 48% | 8.1<br><sub>18,4,-,-,-</sub> | 2.8<br><sub>5,0,-,-,-</sub> |  | 0.8<br><sub>1,2,-,-,-</sub> |  | 1.0<br><sub>2,1,-,-,-</sub> |  | 0.3<br><sub>1,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Moussa Cisse (DAL) | 58% | 6.3<br><sub>4,4,-,-,2</sub> | 2.3<br><sub>1,0,-,-,0</sub> |  | 2.4<br><sub>1,1,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.4 | 0.4 | 4.8 |
| Jett Howard (DAL) | 52% | 6.0<br><sub>7,-,-,-,-</sub> | 2.5<br><sub>0,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.7 |
| Devin Booker (PHX) | 99% | 36.1<br><sub>37,33,38,42,36</sub> | 26.3<br><sub>20,29,23,22,25</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>4,2,2,5,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.6<br><sub>8,6,3,8,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>1,2,1,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 3.0 | 36.5 |
| Dillon Brooks (PHX) | 99% | 30.3<br><sub>27,31,25,34,31</sub> | 16.9<br><sub>15,29,18,16,12</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,3,3,5,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,5,3,7,4</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 2.1<br><sub>3,5,2,2,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.5 | 23.5 |
| Jalen Green (PHX) | 98% | 30.0<br><sub>27,30,25,37,35</sub> | 17.1<br><sub>16,18,14,25,16</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,7,4,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>3,7,3,0,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,4,1,3,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.3 | 2.4 | 24.7 |
| Miles Bridges (PHX) | 99% | 28.5<br><sub>29,29,25,35,25</sub> | 13.7<br><sub>16,13,18,14,2</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>8,6,9,11,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,5,4,5,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>2,1,1,2,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.5 | 1.1 | 23.5 |
| Collin Gillespie (PHX) | 99% | 24.1<br><sub>26,17,27,30,22</sub> | 10.0<br><sub>10,9,16,18,5</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,3,4,3,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.7<br><sub>3,1,5,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>2,2,3,3,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.2 | 1.2 | 17.0 |
| Oso Ighodaro (PHX) | 99% | 23.2<br><sub>33,21,27,30,20</sub> | 6.6<br><sub>8,7,3,7,13</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>11,4,7,4,2</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.9 | 1.2 | 15.0 |
| Jordan Goodwin (PHX) | 98% | 18.9<br><sub>20,17,28,18,17</sub> | 7.5<br><sub>11,2,5,6,11</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>6,5,9,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>2,3,4,2,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>1,0,1,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.2 | 0.7 | 13.9 |
| Khaman Maluach (PHX) | 98% | 18.0<br><sub>11,21,18,16,25</sub> | 7.2<br><sub>4,10,9,8,12</sub> |  | 5.8<br><sub>6,2,6,6,6</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.1 | 1.1 | 13.8 |
| Luke Kennard (PHX) | 99% | 16.8<br><sub>17,17,15,14,19</sub> | 6.8<br><sub>12,3,5,4,8</sub> |  | 1.9<br><sub>2,3,0,1,1</sub> |  | 1.6<br><sub>0,1,0,2,2</sub> |  | 1.0<br><sub>4,1,1,0,1</sub> |  | 0.5 | 0.1 | 0.6 | 10.3 |
| Ryan Dunn (PHX) | 98% | 12.9<br><sub>12,13,9,9,10</sub> | 3.7<br><sub>5,6,0,3,0</sub> |  | 3.1<br><sub>1,5,5,2,2</sub> |  | 0.9<br><sub>0,2,0,0,1</sub> |  | 0.3<br><sub>1,0,0,1,0</sub> |  | 0.5 | 0.3 | 0.4 | 7.7 |
| Rasheer Fleming (PHX) | 38% | 6.8<br><sub>-,4,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.0 |
| Pat Spencer (PHX) | 48% | 6.5<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.4 |
| Jamaree Bouyea (PHX) | 38% | 6.4<br><sub>-,4,-,-,-</sub> | 2.6<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,1,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Koa Peat (PHX) | 52% | 6.0<br><sub>1,4,3,-,-</sub> | 3.0<br><sub>0,2,0,-,-</sub> |  | 1.4<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |
| Duop Reath (PHX) | 38% | 5.9<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.0 |
| Drew Timme (PHX) | 3% | 5.9 | 2.4 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.4 | 4.1 |

</details>


### LAL @ SAS
Out: Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.5–112.5 | LAL 44% | 2.26 / 1.79 | SAS -2.5 | 222.5 | SAS -6.5 covers 38%; o226.5 42% |
| Expected (weighted by chance each plays) | 110.2–113.5 | LAL 40% | 2.48 / 1.67 | SAS -3.5 | 223.5 | SAS -6.5 covers 42%; o226.5 43% |
| if De'Aaron Fox plays | 110.4–113.4 | LAL 41% | 2.42 / 1.70 | SAS -3.5 | 223.5 | SAS -6.5 covers 40%; o226.5 44% |
| if Dylan Harper plays | 110.5–113.5 | LAL 41% | 2.43 / 1.70 | SAS -3.5 | 223.5 | SAS -6.5 covers 41%; o226.5 44% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 28.9 | 13.4 | 3.5 | 6.1 | 1.2 | 1.4 | 0.3 | 2.4 | 22.9 | full tables below |
| Dylan Harper (SAS) | Questionable | 55% | 29.1 | 16.0 | 4.8 | 4.5 | 1.2 | 1.0 | 0.3 | 1.9 | 25.4 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 99% | 34.6<br><sub>36,42,37,36,33</sub> | 29.9<br><sub>43,36,29,25,28</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.5 | 4.0 | 43.4 |
| Austin Reaves | 98% | 31.1<br><sub>-,-,-,-,-</sub> | 18.2<br><sub>-,-,-,-,-</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 2.6 | 25.8 |
| Walker Kessler | 99% | 28.0<br><sub>32,-,31,30,36</sub> | 10.8<br><sub>14,-,10,15,10</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.6<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.4 | 21.8 |
| Quentin Grimes | 99% | 26.9<br><sub>37,42,35,35,30</sub> | 10.1<br><sub>22,47,20,13,9</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.6<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.3 | 16.0 |
| Jake LaRavia | 98% | 23.1<br><sub>32,23,30,24,37</sub> | 5.7<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.4 | 0.9 | 11.0 |
| Matisse Thybulle | 98% | 21.0<br><sub>26,31,21,27,27</sub> | 5.7<br><sub>12,7,2,14,14</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7 | 0.7 | 0.7 | 9.0 |
| Ziaire Williams | 98% | 18.0<br><sub>19,24,18,28,19</sub> | 6.0<br><sub>6,0,7,5,9</sub> |  | 2.0<br><sub>2,1,2,0,4</sub> |  | 1.0<br><sub>3,1,0,1,0</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.0 |
| Collin Sexton | 99% | 17.9<br><sub>24,25,20,18,23</sub> | 9.9<br><sub>16,10,12,10,12</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.1<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.2 | 1.3 | 13.7 |
| Sandro Mamukelashvili | 99% | 16.0<br><sub>21,23,21,20,13</sub> | 6.2<br><sub>4,3,6,9,2</sub> |  | 3.5<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.7 |
| Jarred Vanderbilt | 91% | 9.2<br><sub>12,14,12,10,12</sub> | 2.5<br><sub>2,4,0,4,1</sub> |  | 2.6<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 5.8 |
| AK Okereke | 23% | 8.8<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 36% | 6.7<br><sub>-,17,-,-,-</sub> | 1.4<br><sub>-,4,-,-,-</sub> |  | 2.3<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.2 |
| Cameron Carr | 80% | 6.2<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Carson Cooper | 52% | 6.1<br><sub>-,18,2,-,-</sub> | 1.9<br><sub>-,3,2,-,-</sub> |  | 1.7<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.0 |
| Jaden Hardy | 43% | 6.0<br><sub>-,-,2,-,-</sub> | 3.5<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.5 |
| Adou Thiero | 52% | 5.7<br><sub>-,6,6,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.3<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Bronny James | 47% | 5.2<br><sub>-,-,2,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 2.6 |
| Chris Manon | 52% | 5.1<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 2.8 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 99% | 34.8<br><sub>36,32,26,34,38</sub> | 15.8<br><sub>12,15,10,16,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>5,4,3,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>4,4,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,1,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.5 | 1.3 | 23.8 |
| Stephon Castle | 99% | 33.3<br><sub>31,33,29,37,34</sub> | 18.9<br><sub>10,21,19,28,20</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>2,6,3,8,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 8.2<br><sub>7,12,6,11,9</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,2,5,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 3.5 | 32.5 |
| Victor Wembanyama | 99% | 33.3<br><sub>34,33,32,-,35</sub> | 30.6<br><sub>25,32,50,-,44</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.4<br><sub>18,11,19,-,16</sub> | 12.5<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>4,3,1,-,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>1,2,5,-,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 3.5 | 3.1 | 47.3 |
| Julian Champagnie | 99% | 31.7<br><sub>30,29,25,30,37</sub> | 12.7<br><sub>14,20,9,22,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>6,4,3,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>4,4,3,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 1.0 | 19.8 |
| Keldon Johnson | 99% | 28.2<br><sub>15,27,23,26,33</sub> | 11.6<br><sub>4,10,10,12,3</sub> |  | 5.9<br><sub>2,5,4,4,12</sub> |  | 2.6<br><sub>1,3,4,5,2</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.8 | 0.2 | 1.3 | 20.1 |
| Harrison Barnes | 96% | 18.5<br><sub>10,16,21,26,15</sub> | 6.6<br><sub>0,9,3,9,5</sub> |  | 2.1<br><sub>3,2,5,2,0</sub> |  | 1.1<br><sub>4,1,2,2,1</sub> |  | 0.9<br><sub>0,1,0,1,1</sub> |  | 0.4 | 0.1 | 0.7 | 9.8 |
| Jordan McLaughlin | 88% | 17.2<br><sub>-,11,18,14,15</sub> | 4.9<br><sub>-,0,0,6,4</sub> |  | 2.3<br><sub>-,1,3,2,2</sub> |  | 2.7<br><sub>-,5,2,0,0</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 1.1 | 0.1 | 0.9 | 9.9 |
| Luke Kornet | 99% | 17.1<br><sub>14,15,10,29,13</sub> | 4.4<br><sub>2,4,0,18,4</sub> |  | 5.0<br><sub>1,0,3,11,5</sub> |  | 1.4<br><sub>1,3,0,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.5 | 10.8 |
| Carter Bryant | 96% | 14.6<br><sub>2,13,20,12,14</sub> | 5.2<br><sub>0,3,8,0,2</sub> |  | 2.4<br><sub>0,1,3,3,6</sub> |  | 0.9<br><sub>0,0,0,2,1</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.5 |
| Ja'Kobi Gillespie | 93% | 12.5<br><sub>-,-,-,15,7</sub> | 4.1<br><sub>-,-,-,3,0</sub> |  | 1.7<br><sub>-,-,-,2,1</sub> |  | 1.3<br><sub>-,-,-,4,0</sub> |  | 0.5<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.1 | 0.4 | 7.0 |
| Tarris Reed Jr. | 52% | 10.1<br><sub>-,-,6,15,-</sub> | 3.2<br><sub>-,-,0,7,-</sub> |  | 4.2<br><sub>-,-,4,7,-</sub> |  | 0.6<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.5 | 0.7 | 8.0 |
| David Jones Garcia | 52% | 7.1<br><sub>-,-,4,2,-</sub> | 2.6<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,1,0,-</sub> |  | 1.0<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.7 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 99% | 34.6<br><sub>36,42,37,36,33</sub> | 30.1<br><sub>43,36,29,25,28</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.5 | 4.0 | 43.6 |
| Austin Reaves (LAL) | 98% | 31.1<br><sub>-,-,-,-,-</sub> | 18.3<br><sub>-,-,-,-,-</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 2.6 | 25.9 |
| Walker Kessler (LAL) | 99% | 28.1<br><sub>32,-,31,30,36</sub> | 10.9<br><sub>14,-,10,15,10</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.6<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.4 | 21.9 |
| Quentin Grimes (LAL) | 99% | 26.9<br><sub>37,42,35,35,30</sub> | 10.1<br><sub>22,47,20,13,9</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.3 | 15.9 |
| Jake LaRavia (LAL) | 98% | 23.3<br><sub>32,23,30,24,37</sub> | 5.7<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.5 | 0.9 | 11.1 |
| Matisse Thybulle (LAL) | 98% | 21.0<br><sub>26,31,21,27,27</sub> | 5.7<br><sub>12,7,2,14,14</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7 | 0.7 | 0.7 | 9.0 |
| Ziaire Williams (LAL) | 98% | 18.0<br><sub>19,24,18,28,19</sub> | 6.1<br><sub>6,0,7,5,9</sub> |  | 2.0<br><sub>2,1,2,0,4</sub> |  | 1.0<br><sub>3,1,0,1,0</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.6 | 9.1 |
| Collin Sexton (LAL) | 99% | 17.9<br><sub>24,25,20,18,23</sub> | 9.9<br><sub>16,10,12,10,12</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.1<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.1 | 1.4 | 13.8 |
| Sandro Mamukelashvili (LAL) | 99% | 16.0<br><sub>21,23,21,20,13</sub> | 6.2<br><sub>4,3,6,9,2</sub> |  | 3.5<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.8 |
| Jarred Vanderbilt (LAL) | 91% | 9.3<br><sub>12,14,12,10,12</sub> | 2.5<br><sub>2,4,0,4,1</sub> |  | 2.6<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.9 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Kevon Looney (LAL) | 36% | 6.6<br><sub>-,17,-,-,-</sub> | 1.4<br><sub>-,4,-,-,-</sub> |  | 2.2<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.2 |
| Cameron Carr (LAL) | 80% | 6.2<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Carson Cooper (LAL) | 52% | 6.0<br><sub>-,18,2,-,-</sub> | 1.9<br><sub>-,3,2,-,-</sub> |  | 1.7<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.0 |
| Jaden Hardy (LAL) | 43% | 6.0<br><sub>-,-,2,-,-</sub> | 3.5<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.5 |
| Adou Thiero (LAL) | 52% | 5.8<br><sub>-,6,6,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Bronny James (LAL) | 47% | 5.3<br><sub>-,-,2,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.7 |
| Chris Manon (LAL) | 52% | 5.1<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 2.9 |
| Devin Vassell (SAS) | 99% | 32.0<br><sub>36,32,26,34,38</sub> | 13.8<br><sub>12,15,10,16,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>5,4,3,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>4,4,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,1,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.4 | 1.1 | 20.8 |
| Victor Wembanyama (SAS) | 99% | 32.0<br><sub>34,33,32,-,35</sub> | 28.7<br><sub>25,32,50,-,44</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.4<br><sub>18,11,19,-,16</sub> | 12.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>4,3,1,-,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>1,2,5,-,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 3.2 | 2.8 | 44.5 |
| Stephon Castle (SAS) | 99% | 31.2<br><sub>31,33,29,37,34</sub> | 17.4<br><sub>10,21,19,28,20</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>2,6,3,8,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>7,12,6,11,9</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,2,5,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 3.1 | 29.8 |
| De'Aaron Fox (SAS) | 100% | 28.9<br><sub>34,32,26,-,-</sub> | 13.4<br><sub>6,10,5,-,-</sub> | 13.5 · – | 3.5<br><sub>2,2,2,-,-</sub> | 3.5 | 6.1<br><sub>2,5,10,-,-</sub> | 5.5 | 1.2<br><sub>0,0,0,-,-</sub> | 0.5 | 1.4 | 0.3 | 2.4 | 22.9 |
| Julian Champagnie (SAS) | 99% | 28.6<br><sub>30,29,25,30,37</sub> | 11.6<br><sub>14,20,9,22,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,4,3,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>4,4,3,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.5 | 0.9 | 17.9 |
| Keldon Johnson (SAS) | 99% | 25.1<br><sub>15,27,23,26,33</sub> | 10.2<br><sub>4,10,10,12,3</sub> |  | 5.3<br><sub>2,5,4,4,12</sub> |  | 2.2<br><sub>1,3,4,5,2</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 17.7 |
| Harrison Barnes (SAS) | 96% | 16.0<br><sub>10,16,21,26,15</sub> | 5.9<br><sub>0,9,3,9,5</sub> |  | 1.8<br><sub>3,2,5,2,0</sub> |  | 0.9<br><sub>4,1,2,2,1</sub> |  | 0.7<br><sub>0,1,0,1,1</sub> |  | 0.3 | 0.1 | 0.5 | 8.7 |
| Luke Kornet (SAS) | 99% | 15.1<br><sub>14,15,10,29,13</sub> | 4.1<br><sub>2,4,0,18,4</sub> |  | 4.5<br><sub>1,0,3,11,5</sub> |  | 1.2<br><sub>1,3,0,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 9.7 |
| Jordan McLaughlin (SAS) | 88% | 14.0<br><sub>-,11,18,14,15</sub> | 4.0<br><sub>-,0,0,6,4</sub> |  | 1.8<br><sub>-,1,3,2,2</sub> |  | 2.1<br><sub>-,5,2,0,0</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.9 | 0.1 | 0.7 | 8.0 |
| Carter Bryant (SAS) | 96% | 12.5<br><sub>2,13,20,12,14</sub> | 4.5<br><sub>0,3,8,0,2</sub> |  | 2.1<br><sub>0,1,3,3,6</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>0,1,2,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.3 |
| Ja'Kobi Gillespie (SAS) | 93% | 8.1<br><sub>-,-,-,15,7</sub> | 2.9<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,2,1</sub> |  | 0.8<br><sub>-,-,-,4,0</sub> |  | 0.2<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Tarris Reed Jr. (SAS) | 52% | 7.6<br><sub>-,-,6,15,-</sub> | 2.5<br><sub>-,-,0,7,-</sub> |  | 3.2<br><sub>-,-,4,7,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.1 |
| David Jones Garcia (SAS) | 52% | 5.8<br><sub>-,-,4,2,-</sub> | 2.2<br><sub>-,-,0,2,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.0 |

</details>

<details><summary>if Dylan Harper plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 99% | 34.6<br><sub>36,42,37,36,33</sub> | 30.0<br><sub>43,36,29,25,28</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.4 | 4.0 | 43.5 |
| Austin Reaves (LAL) | 98% | 31.1<br><sub>-,-,-,-,-</sub> | 18.3<br><sub>-,-,-,-,-</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 2.6 | 25.9 |
| Walker Kessler (LAL) | 99% | 28.1<br><sub>32,-,31,30,36</sub> | 10.8<br><sub>14,-,10,15,10</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.5<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.5 | 21.8 |
| Quentin Grimes (LAL) | 99% | 26.8<br><sub>37,42,35,35,30</sub> | 10.1<br><sub>22,47,20,13,9</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.3 | 15.9 |
| Jake LaRavia (LAL) | 98% | 23.3<br><sub>32,23,30,24,37</sub> | 5.8<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.4 | 0.9 | 11.1 |
| Matisse Thybulle (LAL) | 98% | 21.0<br><sub>26,31,21,27,27</sub> | 5.6<br><sub>12,7,2,14,14</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7 | 0.7 | 0.7 | 8.9 |
| Ziaire Williams (LAL) | 98% | 18.1<br><sub>19,24,18,28,19</sub> | 6.1<br><sub>6,0,7,5,9</sub> |  | 2.0<br><sub>2,1,2,0,4</sub> |  | 1.0<br><sub>3,1,0,1,0</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.1 |
| Collin Sexton (LAL) | 99% | 17.9<br><sub>24,25,20,18,23</sub> | 9.9<br><sub>16,10,12,10,12</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.1<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.2 | 1.4 | 13.8 |
| Sandro Mamukelashvili (LAL) | 99% | 16.0<br><sub>21,23,21,20,13</sub> | 6.2<br><sub>4,3,6,9,2</sub> |  | 3.5<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.8 |
| Jarred Vanderbilt (LAL) | 91% | 9.3<br><sub>12,14,12,10,12</sub> | 2.5<br><sub>2,4,0,4,1</sub> |  | 2.6<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 5.9 |
| Arthur Kaluma (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| AK Okereke (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Kevon Looney (LAL) | 36% | 6.6<br><sub>-,17,-,-,-</sub> | 1.5<br><sub>-,4,-,-,-</sub> |  | 2.3<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.2 |
| Cameron Carr (LAL) | 80% | 6.2<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Carson Cooper (LAL) | 52% | 6.1<br><sub>-,18,2,-,-</sub> | 1.9<br><sub>-,3,2,-,-</sub> |  | 1.7<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |
| Jaden Hardy (LAL) | 43% | 6.0<br><sub>-,-,2,-,-</sub> | 3.5<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.5 |
| Adou Thiero (LAL) | 52% | 5.8<br><sub>-,6,6,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.3<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Bronny James (LAL) | 47% | 5.3<br><sub>-,-,2,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 2.7 |
| Chris Manon (LAL) | 52% | 5.2<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 2.9 |
| Devin Vassell (SAS) | 99% | 31.4<br><sub>36,32,26,34,38</sub> | 13.2<br><sub>12,15,10,16,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,4,3,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>4,4,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,1,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.4 | 1.1 | 20.1 |
| Victor Wembanyama (SAS) | 99% | 31.3<br><sub>34,33,32,-,35</sub> | 27.7<br><sub>25,32,50,-,44</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 11.9<br><sub>18,11,19,-,16</sub> | 12.5<br><sub>o 44% · u 56%</sub> | 3.4<br><sub>4,3,1,-,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>1,2,5,-,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 3.2 | 2.7 | 43.1 |
| Stephon Castle (SAS) | 99% | 30.7<br><sub>31,33,29,37,34</sub> | 17.2<br><sub>10,21,19,28,20</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>2,6,3,8,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>7,12,6,11,9</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,2,5,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 3.1 | 29.5 |
| Dylan Harper (SAS) | 100% | 29.1<br><sub>35,-,-,-,-</sub> | 16.0<br><sub>20,-,-,-,-</sub> | 14.5 · – | 4.8<br><sub>4,-,-,-,-</sub> | 4.5 | 4.5<br><sub>2,-,-,-,-</sub> | 3.5 | 1.2<br><sub>0,-,-,-,-</sub> | 0.5 | 1.0 | 0.3 | 1.9 | 25.4 |
| Julian Champagnie (SAS) | 99% | 28.1<br><sub>30,29,25,30,37</sub> | 11.1<br><sub>14,20,9,22,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>6,4,3,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>4,4,3,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.4 | 0.9 | 17.4 |
| Keldon Johnson (SAS) | 99% | 24.6<br><sub>15,27,23,26,33</sub> | 9.7<br><sub>4,10,10,12,3</sub> |  | 5.2<br><sub>2,5,4,4,12</sub> |  | 2.1<br><sub>1,3,4,5,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 17.0 |
| Harrison Barnes (SAS) | 96% | 15.9<br><sub>10,16,21,26,15</sub> | 5.8<br><sub>0,9,3,9,5</sub> |  | 1.8<br><sub>3,2,5,2,0</sub> |  | 1.0<br><sub>4,1,2,2,1</sub> |  | 0.7<br><sub>0,1,0,1,1</sub> |  | 0.3 | 0.1 | 0.5 | 8.6 |
| Luke Kornet (SAS) | 99% | 14.8<br><sub>14,15,10,29,13</sub> | 3.9<br><sub>2,4,0,18,4</sub> |  | 4.3<br><sub>1,0,3,11,5</sub> |  | 1.2<br><sub>1,3,0,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 9.4 |
| Jordan McLaughlin (SAS) | 88% | 13.8<br><sub>-,11,18,14,15</sub> | 3.9<br><sub>-,0,0,6,4</sub> |  | 1.9<br><sub>-,1,3,2,2</sub> |  | 2.1<br><sub>-,5,2,0,0</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.9 | 0.1 | 0.7 | 7.9 |
| Carter Bryant (SAS) | 96% | 12.3<br><sub>2,13,20,12,14</sub> | 4.5<br><sub>0,3,8,0,2</sub> |  | 2.1<br><sub>0,1,3,3,6</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>0,1,2,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.3 |
| Ja'Kobi Gillespie (SAS) | 93% | 8.1<br><sub>-,-,-,15,7</sub> | 2.9<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,2,1</sub> |  | 0.8<br><sub>-,-,-,4,0</sub> |  | 0.2<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Tarris Reed Jr. (SAS) | 52% | 7.4<br><sub>-,-,6,15,-</sub> | 2.4<br><sub>-,-,0,7,-</sub> |  | 3.1<br><sub>-,-,4,7,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.4 | 0.5 | 5.9 |
| David Jones Garcia (SAS) | 52% | 5.9<br><sub>-,-,4,2,-</sub> | 2.3<br><sub>-,-,0,2,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.2 |

</details>


### DEN @ UTA
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Bryce Hopkins (DEN), Cam Whitmore (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 124.7–115.2 | DEN 75% | 1.33 / 3.99 | UTA +9.5 | 239.5 | UTA +9.5 covers 50%; o232.5 65% |
| Expected (weighted by chance each plays) | 123.5–115.2 | DEN 72% | 1.39 / 3.59 | UTA +8.5 | 238.5 | UTA +9.5 covers 53%; o232.5 62% |
| if Mo Bamba plays | 123.9–114.9 | DEN 74% | 1.36 / 3.81 | UTA +8.5 | 238.5 | UTA +9.5 covers 52%; o232.5 63% |
| if Jaxson Hayes plays | 123.9–115.0 | DEN 74% | 1.36 / 3.78 | UTA +8.5 | 238.5 | UTA +9.5 covers 52%; o232.5 63% |
| if Jusuf Nurkic plays | 124.7–115.2 | DEN 75% | 1.33 / 3.99 | UTA +9.5 | 239.5 | UTA +9.5 covers 50%; o232.5 65% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Mo Bamba (UTA) | Questionable | 55% | 25.7 | 8.9 | 8.7 | 1.4 | 0.6 | 0.6 | 1.5 | 1.1 | 19.0 | full tables below |
| Jaxson Hayes (UTA) | Questionable | 55% | 22.2 | 9.2 | 5.9 | 1.3 | 0.0 | 0.6 | 0.9 | 0.9 | 16.4 | full tables below |
| Jusuf Nurkic (UTA) | Questionable | 55% | 21.3 | 9.5 | 8.3 | 4.1 | 0.5 | 1.0 | 0.5 | 1.6 | 21.9 | full tables below |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 99% | 36.4<br><sub>38,39,38,42,33</sub> | 27.9<br><sub>28,24,26,37,18</sub> | 25.5 · –<br><sub>o 52% · u 48%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.1 | 49.9 |
| Jamal Murray | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 26.0<br><sub>28,21,14,45,20</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 2.2 | 36.5 |
| Christian Braun | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.9<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.5 |
| Cameron Johnson | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.3<br><sub>9,8,19,16,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.0 | 20.9 |
| Aaron Gordon | 99% | 29.3<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan | 96% | 19.5<br><sub>14,25,22,18,17</sub> | 10.4<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.5<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 27% · u 73%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile | 98% | 13.7<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.5 |
| Marvin Bagley III | 99% | 12.1<br><sub>10,9,10,11,12</sub> | 6.2<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.5 |
| Tyus Jones | 98% | 10.9<br><sub>10,9,14,8,12</sub> | 2.9<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Julian Strawther | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Zeke Nnaji | 38% | 6.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.3 |
| Alpha Diallo | 48% | 6.2<br><sub>-,-,-,-,3</sub> | 2.2<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.8 |
| Ryan Nembhard | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 34.8<br><sub>35,39,36,26,33</sub> | 22.9<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 34.1 |
| Ace Bailey | 99% | 33.7<br><sub>23,27,24,33,33</sub> | 17.0<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.8 | 1.8 | 25.5 |
| Darryn Peterson | 99% | 33.0<br><sub>31,19,32,25,29</sub> | 17.8<br><sub>13,11,20,6,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.5 | 2.0 | 27.6 |
| Svi Mykhailiuk | 98% | 27.7<br><sub>33,34,28,32,25</sub> | 11.8<br><sub>8,15,11,39,4</sub> |  | 3.5<br><sub>7,3,7,5,3</sub> |  | 2.5<br><sub>5,5,2,3,2</sub> |  | 2.1<br><sub>2,4,3,10,0</sub> |  | 0.7 | 0.1 | 1.1 | 17.7 |
| Josh Green | 98% | 24.9<br><sub>13,28,29,23,19</sub> | 6.1<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.9<br><sub>1,2,2,0,2</sub> |  | 0.8 | 0.3 | 0.7 | 10.1 |
| Brice Sensabaugh | 99% | 24.0<br><sub>35,14,26,17,17</sub> | 15.4<br><sub>40,8,18,10,6</sub> |  | 4.1<br><sub>11,3,3,3,4</sub> |  | 2.1<br><sub>5,2,1,2,1</sub> |  | 2.2<br><sub>8,0,5,2,0</sub> |  | 0.7 | 0.2 | 1.6 | 21.6 |
| Josh Okogie | 98% | 21.4<br><sub>22,15,17,14,9</sub> | 6.3<br><sub>9,3,3,1,0</sub> |  | 3.4<br><sub>2,0,2,4,0</sub> |  | 1.2<br><sub>4,0,2,0,0</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 1.0 | 0.3 | 0.8 | 10.9 |
| Isaiah Collier | 67% | 20.0<br><sub>-,10,-,13,18</sub> | 9.7<br><sub>-,0,-,10,4</sub> |  | 2.8<br><sub>-,1,-,2,2</sub> |  | 5.1<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.8 | 0.2 | 1.5 | 17.6 |
| Kyle Filipowski | 64% | 19.9<br><sub>-,6,-,9,24</sub> | 11.3<br><sub>-,0,-,2,21</sub> |  | 6.5<br><sub>-,3,-,4,12</sub> |  | 2.4<br><sub>-,0,-,3,4</sub> |  | 0.9<br><sub>-,0,-,0,1</sub> |  | 0.8 | 0.4 | 1.2 | 20.2 |
| Tony Bradley | 52% | 14.7<br><sub>17,-,-,13,-</sub> | 4.3<br><sub>3,-,-,1,-</sub> |  | 4.6<br><sub>7,-,-,5,-</sub> |  | 0.7<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.6 | 9.6 |

</details>

<details><summary>if Mo Bamba plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.8<br><sub>28,24,26,37,18</sub> | 25.5 · –<br><sub>o 52% · u 48%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 1.0 | 3.2 | 49.9 |
| Jamal Murray (DEN) | 99% | 36.4<br><sub>35,38,36,45,36</sub> | 25.9<br><sub>28,21,14,45,20</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 2.2 | 36.5 |
| Christian Braun (DEN) | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.8<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.5 |
| Cameron Johnson (DEN) | 98% | 30.4<br><sub>27,26,29,36,34</sub> | 14.3<br><sub>9,8,19,16,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.0 | 20.9 |
| Aaron Gordon (DEN) | 99% | 29.2<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan (DEN) | 96% | 19.4<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 27% · u 73%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones (DEN) | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile (DEN) | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.5 |
| Marvin Bagley III (DEN) | 99% | 12.0<br><sub>10,9,10,11,12</sub> | 6.1<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.4 |
| Tyus Jones (DEN) | 98% | 10.8<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.8<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.6 |
| Julian Strawther (DEN) | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 4.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Zeke Nnaji (DEN) | 38% | 6.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.3 |
| Alpha Diallo (DEN) | 48% | 6.2<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Ryan Nembhard (DEN) | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Keyonte George (UTA) | 99% | 34.6<br><sub>35,39,36,26,33</sub> | 21.3<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 32.4 |
| Ace Bailey (UTA) | 99% | 32.9<br><sub>23,27,24,33,33</sub> | 16.2<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.9 | 1.7 | 24.4 |
| Darryn Peterson (UTA) | 99% | 32.0<br><sub>31,19,32,25,29</sub> | 16.8<br><sub>13,11,20,6,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.5 | 2.0 | 26.3 |
| Mo Bamba (UTA) | 100% | 25.7<br><sub>31,23,20,23,29</sub> | 8.9<br><sub>15,6,2,6,6</sub> |  | 8.7<br><sub>10,16,2,10,7</sub> |  | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.6 | 1.5 | 1.1 | 19.0 |
| Svi Mykhailiuk (UTA) | 98% | 25.5<br><sub>33,34,28,32,25</sub> | 11.4<br><sub>8,15,11,39,4</sub> |  | 3.1<br><sub>7,3,7,5,3</sub> |  | 2.2<br><sub>5,5,2,3,2</sub> |  | 1.9<br><sub>2,4,3,10,0</sub> |  | 0.6 | 0.1 | 1.0 | 16.7 |
| Josh Green (UTA) | 98% | 23.3<br><sub>13,28,29,23,19</sub> | 5.8<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>1,2,2,0,2</sub> |  | 0.7 | 0.3 | 0.6 | 9.4 |
| Brice Sensabaugh (UTA) | 99% | 22.1<br><sub>35,14,26,17,17</sub> | 14.0<br><sub>40,8,18,10,6</sub> |  | 3.8<br><sub>11,3,3,3,4</sub> |  | 2.0<br><sub>5,2,1,2,1</sub> |  | 2.0<br><sub>8,0,5,2,0</sub> |  | 0.6 | 0.2 | 1.6 | 19.8 |
| Josh Okogie (UTA) | 98% | 18.2<br><sub>22,15,17,14,9</sub> | 5.4<br><sub>9,3,3,1,0</sub> |  | 2.8<br><sub>2,0,2,4,0</sub> |  | 1.0<br><sub>4,0,2,0,0</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.2 | 0.7 | 9.2 |
| Isaiah Collier (UTA) | 67% | 17.5<br><sub>-,10,-,13,18</sub> | 8.4<br><sub>-,0,-,10,4</sub> |  | 2.4<br><sub>-,1,-,2,2</sub> |  | 4.6<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.7 | 0.2 | 1.4 | 15.3 |
| Kyle Filipowski (UTA) | 64% | 17.5<br><sub>-,6,-,9,24</sub> | 9.7<br><sub>-,0,-,2,21</sub> |  | 5.8<br><sub>-,3,-,4,12</sub> |  | 2.1<br><sub>-,0,-,3,4</sub> |  | 0.7<br><sub>-,0,-,0,1</sub> |  | 0.7 | 0.3 | 1.2 | 17.6 |
| Tony Bradley (UTA) | 52% | 11.6<br><sub>17,-,-,13,-</sub> | 3.4<br><sub>3,-,-,1,-</sub> |  | 3.5<br><sub>7,-,-,5,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 7.5 |

</details>

<details><summary>if Jaxson Hayes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.9<br><sub>28,24,26,37,18</sub> | 25.5 · –<br><sub>o 52% · u 48%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.2 | 50.0 |
| Jamal Murray (DEN) | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 25.9<br><sub>28,21,14,45,20</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.8 | 2.2 | 36.4 |
| Christian Braun (DEN) | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.8<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.4 |
| Cameron Johnson (DEN) | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.2<br><sub>9,8,19,16,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.0 | 20.8 |
| Aaron Gordon (DEN) | 99% | 29.3<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan (DEN) | 96% | 19.4<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 27% · u 73%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones (DEN) | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile (DEN) | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.6 |
| Marvin Bagley III (DEN) | 99% | 12.2<br><sub>10,9,10,11,12</sub> | 6.2<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.5 |
| Tyus Jones (DEN) | 98% | 10.8<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Julian Strawther (DEN) | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.4 |
| Zeke Nnaji (DEN) | 38% | 7.0<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.3 |
| Ryan Nembhard (DEN) | 38% | 6.2<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Alpha Diallo (DEN) | 48% | 6.1<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Keyonte George (UTA) | 99% | 34.8<br><sub>35,39,36,26,33</sub> | 21.3<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 32.4 |
| Ace Bailey (UTA) | 99% | 33.1<br><sub>23,27,24,33,33</sub> | 16.4<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.9 | 1.7 | 24.6 |
| Darryn Peterson (UTA) | 99% | 32.4<br><sub>31,19,32,25,29</sub> | 17.0<br><sub>13,11,20,6,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.6 | 2.0 | 26.6 |
| Svi Mykhailiuk (UTA) | 98% | 25.7<br><sub>33,34,28,32,25</sub> | 11.5<br><sub>8,15,11,39,4</sub> |  | 3.1<br><sub>7,3,7,5,3</sub> |  | 2.2<br><sub>5,5,2,3,2</sub> |  | 1.9<br><sub>2,4,3,10,0</sub> |  | 0.6 | 0.1 | 1.0 | 16.8 |
| Josh Green (UTA) | 98% | 22.9<br><sub>13,28,29,23,19</sub> | 5.7<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>1,2,2,0,2</sub> |  | 0.7 | 0.2 | 0.6 | 9.2 |
| Jaxson Hayes (UTA) | 100% | 22.2<br><sub>-,25,28,12,-</sub> | 9.2<br><sub>-,6,18,8,-</sub> | 8.5 · – | 5.9<br><sub>-,7,14,3,-</sub> | 5.5 | 1.3<br><sub>-,2,0,1,-</sub> | 1.5 | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.9 | 0.9 | 16.4 |
| Brice Sensabaugh (UTA) | 99% | 21.6<br><sub>35,14,26,17,17</sub> | 13.8<br><sub>40,8,18,10,6</sub> |  | 3.7<br><sub>11,3,3,3,4</sub> |  | 1.9<br><sub>5,2,1,2,1</sub> |  | 1.9<br><sub>8,0,5,2,0</sub> |  | 0.6 | 0.2 | 1.6 | 19.5 |
| Isaiah Collier (UTA) | 67% | 17.8<br><sub>-,10,-,13,18</sub> | 8.4<br><sub>-,0,-,10,4</sub> |  | 2.4<br><sub>-,1,-,2,2</sub> |  | 4.7<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.7 | 0.2 | 1.4 | 15.5 |
| Josh Okogie (UTA) | 98% | 17.7<br><sub>22,15,17,14,9</sub> | 5.2<br><sub>9,3,3,1,0</sub> |  | 2.7<br><sub>2,0,2,4,0</sub> |  | 1.0<br><sub>4,0,2,0,0</sub> |  | 0.5<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.2 | 0.6 | 8.9 |
| Kyle Filipowski (UTA) | 64% | 16.9<br><sub>-,6,-,9,24</sub> | 9.4<br><sub>-,0,-,2,21</sub> |  | 5.6<br><sub>-,3,-,4,12</sub> |  | 2.0<br><sub>-,0,-,3,4</sub> |  | 0.7<br><sub>-,0,-,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 17.0 |
| Tony Bradley (UTA) | 52% | 12.1<br><sub>17,-,-,13,-</sub> | 3.4<br><sub>3,-,-,1,-</sub> |  | 3.7<br><sub>7,-,-,5,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 7.8 |

</details>

<details><summary>if Jusuf Nurkic plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.9<br><sub>28,24,26,37,18</sub> | 25.5 · –<br><sub>o 52% · u 48%</sub> | 12.2<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.2 | 49.9 |
| Jamal Murray (DEN) | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 26.1<br><sub>28,21,14,45,20</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 2.2 | 36.6 |
| Christian Braun (DEN) | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.9<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.5 |
| Cameron Johnson (DEN) | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.2<br><sub>9,8,19,16,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.0 | 20.9 |
| Aaron Gordon (DEN) | 99% | 29.2<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan (DEN) | 96% | 19.4<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.5<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 27% · u 73%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones (DEN) | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile (DEN) | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.7<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.6 |
| Marvin Bagley III (DEN) | 99% | 12.1<br><sub>10,9,10,11,12</sub> | 6.2<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.5 |
| Tyus Jones (DEN) | 98% | 10.8<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Julian Strawther (DEN) | 38% | 9.1<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Zeke Nnaji (DEN) | 38% | 6.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.4 |
| Alpha Diallo (DEN) | 48% | 6.1<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Ryan Nembhard (DEN) | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Keyonte George (UTA) | 99% | 34.9<br><sub>35,39,36,26,33</sub> | 22.0<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 33.3 |
| Ace Bailey (UTA) | 99% | 33.7<br><sub>23,27,24,33,33</sub> | 16.4<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.8 | 1.8 | 25.0 |
| Darryn Peterson (UTA) | 99% | 33.0<br><sub>31,19,32,25,29</sub> | 17.1<br><sub>13,11,20,6,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.5 | 2.0 | 26.8 |
| Svi Mykhailiuk (UTA) | 98% | 27.6<br><sub>33,34,28,32,25</sub> | 11.2<br><sub>8,15,11,39,4</sub> |  | 3.5<br><sub>7,3,7,5,3</sub> |  | 2.5<br><sub>5,5,2,3,2</sub> |  | 2.0<br><sub>2,4,3,10,0</sub> |  | 0.7 | 0.1 | 1.1 | 17.1 |
| Josh Green (UTA) | 98% | 24.9<br><sub>13,28,29,23,19</sub> | 5.9<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.9<br><sub>1,2,2,0,2</sub> |  | 0.8 | 0.2 | 0.7 | 9.8 |
| Brice Sensabaugh (UTA) | 99% | 24.0<br><sub>35,14,26,17,17</sub> | 14.8<br><sub>40,8,18,10,6</sub> |  | 4.1<br><sub>11,3,3,3,4</sub> |  | 2.1<br><sub>5,2,1,2,1</sub> |  | 2.2<br><sub>8,0,5,2,0</sub> |  | 0.7 | 0.2 | 1.6 | 21.0 |
| Josh Okogie (UTA) | 98% | 21.4<br><sub>22,15,17,14,9</sub> | 6.1<br><sub>9,3,3,1,0</sub> |  | 3.4<br><sub>2,0,2,4,0</sub> |  | 1.2<br><sub>4,0,2,0,0</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 1.0 | 0.3 | 0.8 | 10.7 |
| Jusuf Nurkic (UTA) | 100% | 21.3 | 9.5 | 7.5 · – | 8.3 | 6.5 | 4.1 | 2.5 | 0.5 |  | 1.0 | 0.5 | 1.6 | 21.9 |
| Isaiah Collier (UTA) | 67% | 20.0<br><sub>-,10,-,13,18</sub> | 9.2<br><sub>-,0,-,10,4</sub> |  | 2.8<br><sub>-,1,-,2,2</sub> |  | 5.2<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.7 | 0.2 | 1.5 | 17.2 |
| Kyle Filipowski (UTA) | 64% | 19.7<br><sub>-,6,-,9,24</sub> | 10.7<br><sub>-,0,-,2,21</sub> |  | 6.5<br><sub>-,3,-,4,12</sub> |  | 2.4<br><sub>-,0,-,3,4</sub> |  | 0.8<br><sub>-,0,-,0,1</sub> |  | 0.7 | 0.4 | 1.2 | 19.6 |
| Tony Bradley (UTA) | 52% | 14.7<br><sub>17,-,-,13,-</sub> | 4.2<br><sub>3,-,-,1,-</sub> |  | 4.7<br><sub>7,-,-,5,-</sub> |  | 0.7<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.6 | 9.6 |

</details>


### NOP @ LAC
Out: Bradley Beal (LAC), Dejounte Murray (NOP), Jaron Pierre Jr. (NOP)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.9–116.6 | NOP 34% | 2.92 / 1.52 | LAC -5.5 | 227.5 | LAC -2.5 covers 60%; o229.5 46% |
| Expected (weighted by chance each plays) | 111.4–117.1 | NOP 34% | 2.91 / 1.52 | LAC -6.5 | 228.5 | LAC -2.5 covers 60%; o229.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cam Christie (LAC) | Questionable | 55% | 6.1 | 2.6 | 1.0 | 0.5 | 0.1 | 0.2 | 0.1 | 0.3 | 4.1 | small |
| Jalen Pickett (LAC) | Questionable | 55% | 6.0 | 2.2 | 0.8 | 0.9 | 0.2 | 0.2 | 0.1 | 0.3 | 3.9 | small |
| Nick Martinelli (LAC) | Questionable | 55% | 6.1 | 2.6 | 1.5 | 0.5 | 0.1 | 0.2 | 0.2 | 0.3 | 4.5 | small |
| Bennedict Mathurin (NOP) | Doubtful | 20% | 11.0 | 4.8 | 1.8 | 0.9 | 0.3 | 0.3 | 0.1 | 0.7 | 7.5 | small |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 99% | 32.3<br><sub>33,42,37,32,40</sub> | 15.9<br><sub>23,10,21,2,21</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>6,8,6,5,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>3,6,3,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>5,2,4,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 1.0 | 23.7 |
| Jeremiah Fears | 99% | 32.0<br><sub>29,31,38,34,40</sub> | 17.7<br><sub>19,16,22,29,7</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>10,5,7,5,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.2<br><sub>10,4,5,4,11</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 3.1 | 28.7 |
| Trey Murphy III | 98% | 32.0<br><sub>-,-,29,-,35</sub> | 16.2<br><sub>-,-,17,-,9</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>-,-,4,-,9</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>-,-,1,-,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>-,-,3,-,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.3 | 1.5 | 24.6 |
| Zion Williamson | 84% | 31.8<br><sub>25,32,37,-,40</sub> | 20.4<br><sub>16,24,22,-,25</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>6,7,6,-,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,1,7,-,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.2<br><sub>0,0,0,-,0</sub> |  | 1.4 | 0.5 | 2.3 | 29.6 |
| Jordan Poole | 91% | 23.3<br><sub>31,30,13,31,27</sub> | 12.4<br><sub>11,22,6,25,28</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>2,1,0,3,0</sub> |  | 3.3<br><sub>5,5,1,2,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,3,2,3,6</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 1.7 | 17.7 |
| Herbert Jones | 99% | 23.1<br><sub>24,32,33,25,21</sub> | 7.1<br><sub>8,9,14,2,7</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>3,3,3,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9<br><sub>2,3,4,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.4 | 1.2 | 11.9 |
| Derik Queen | 99% | 22.1<br><sub>21,19,18,35,21</sub> | 11.1<br><sub>17,9,11,15,11</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>10,5,7,15,9</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,0,3,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.4<br><sub>4,0,0,0,0</sub> | 0.5<br><sub>o 32% · u 68%</sub> | 1.0 | 0.6 | 2.1 | 20.2 |
| Yves Missi | 98% | 19.3<br><sub>23,17,23,35,22</sub> | 5.7<br><sub>6,4,4,9,4</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 6.1<br><sub>14,5,7,13,8</sub> | 8.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>1,2,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.9 | 13.0 |
| Karlo Matkovic | 98% | 13.5<br><sub>20,10,8,15,13</sub> | 4.6<br><sub>3,0,0,3,5</sub> |  | 3.2<br><sub>2,2,2,3,4</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.5<br><sub>0,0,0,1,1</sub> |  | 0.4 | 0.5 | 0.7 | 8.5 |
| Trendon Watford | 74% | 11.2<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.8 | 7.5 |
| DeAndre Jordan | 38% | 9.2<br><sub>-,10,-,-,-</sub> | 2.7<br><sub>-,8,-,-,-</sub> |  | 3.5<br><sub>-,2,-,-,-</sub> |  | 0.6<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 6.8 |
| Bryce McGowens | 76% | 9.2<br><sub>-,-,-,-,6</sub> | 3.3<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |
| AJ Johnson | 52% | 6.2<br><sub>6,-,-,8,-</sub> | 2.3<br><sub>0,-,-,0,-</sub> |  | 0.8<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 99% | 30.4<br><sub>30,35,32,34,29</sub> | 19.7<br><sub>20,23,16,26,12</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,0,1,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 6.7<br><sub>7,5,2,8,4</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>2,3,2,4,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 2.9 | 28.8 |
| Rui Hachimura | 99% | 28.4<br><sub>27,32,29,29,37</sub> | 14.2<br><sub>20,17,19,19,14</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>5,7,8,3,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>1,2,1,3,5</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,4,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.4 | 1.1 | 21.0 |
| Brandon Ingram | 97% | 26.2<br><sub>-,-,-,27,26</sub> | 16.4<br><sub>-,-,-,16,18</sub> | 18.5 · –<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>-,-,-,7,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>-,-,-,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.6 | 2.0 | 24.4 |
| Derrick Jones Jr. | 99% | 24.7<br><sub>28,27,26,23,23</sub> | 9.0<br><sub>5,8,4,7,4</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 3.8<br><sub>1,2,7,4,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,1,1,3,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.9 | 1.0 | 0.8 | 14.2 |
| Max Strus | 98% | 22.5<br><sub>21,32,29,26,21</sub> | 8.2<br><sub>3,18,5,8,0</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>2,5,6,0,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,4,3,2,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>1,5,1,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 0.9 | 14.4 |
| Brook Lopez | 99% | 21.9<br><sub>23,27,25,21,18</sub> | 11.8<br><sub>23,23,21,3,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,3,6,4,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,4,0,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>4,5,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 1.2 | 1.0 | 18.0 |
| Kris Dunn | 99% | 21.8<br><sub>26,20,19,23,22</sub> | 6.5<br><sub>2,6,3,9,12</sub> | 4.5 · –<br><sub>o 57% · u 43%</sub> | 3.3<br><sub>5,2,4,5,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.6<br><sub>5,2,5,4,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.7<br><sub>0,1,1,0,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.3 | 1.0 | 13.4 |
| Keaton Wagler | 98% | 19.6<br><sub>18,17,19,17,21</sub> | 10.0<br><sub>15,7,7,2,12</sub> |  | 3.0<br><sub>2,5,7,1,2</sub> |  | 2.5<br><sub>0,2,3,2,0</sub> |  | 1.2<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.1 | 1.5 | 15.5 |
| Kobe Sanders | 98% | 13.6<br><sub>18,14,19,12,5</sub> | 5.7<br><sub>5,0,9,6,0</sub> |  | 1.6<br><sub>1,1,3,0,0</sub> |  | 1.4<br><sub>3,1,1,0,0</sub> |  | 0.7<br><sub>0,0,3,2,0</sub> |  | 0.6 | 0.1 | 0.7 | 8.7 |
| Yanic Konan Niederhauser | 80% | 13.0<br><sub>-,11,16,8,18</sub> | 4.4<br><sub>-,2,6,2,4</sub> |  | 3.6<br><sub>-,3,6,1,4</sub> |  | 0.6<br><sub>-,0,1,1,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.7 | 8.6 |
| Isaiah Jackson | 98% | 12.5<br><sub>19,9,4,18,7</sub> | 5.9<br><sub>8,6,0,6,4</sub> |  | 4.0<br><sub>5,4,0,6,1</sub> |  | 1.1<br><sub>0,2,0,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.0 | 0.8 | 10.9 |
| Gradey Dick | 83% | 11.1<br><sub>17,13,16,-,5</sub> | 5.0<br><sub>0,2,6,-,2</sub> |  | 1.8<br><sub>0,2,5,-,2</sub> |  | 0.7<br><sub>1,1,2,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.5 |
| Baba Miller | 91% | 8.1<br><sub>4,1,3,1,5</sub> | 4.1<br><sub>3,0,1,0,9</sub> |  | 1.3<br><sub>0,0,0,0,1</sub> |  | 1.1<br><sub>0,0,1,0,1</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.5 |
| Blake Wesley | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.8 |

</details>


### GSW @ POR
Out: Vit Krejci (POR), Damian Lillard (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sidy Cissoko AST over 2.5 (3+) | GSW @ POR | draftkings | 2.42 | 2.41 | 1.87 | 53.4% | 38.9% | 41.5% | +0.4% | +29.2% | 0.1% |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 99% | 32.6<br><sub>33,30,33,34,31</sub> | 19.7<br><sub>28,13,11,12,15</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>8,5,8,8,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>3,4,7,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.7 | 2.9 | 30.1 |
| Brandin Podziemski | 98% | 32.6<br><sub>30,29,32,38,32</sub> | 15.8<br><sub>15,10,15,18,13</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>6,3,3,7,2</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>3,4,2,2,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,0,0,4,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.3 | 1.8 | 24.0 |
| Draymond Green | 97% | 25.7<br><sub>25,23,-,27,26</sub> | 6.2<br><sub>2,3,-,9,6</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>8,1,-,6,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,2,-,3,11</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.7<br><sub>0,1,-,3,2</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.6 | 2.1 | 16.1 |
| De'Anthony Melton | 99% | 24.0<br><sub>21,19,25,27,27</sub> | 10.4<br><sub>8,0,9,2,24</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,2,1,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>1,2,5,7,7</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>2,0,1,0,8</sub> | 2.5<br><sub>o 35% · u 65%</sub> | 1.5 | 0.5 | 1.9 | 16.7 |
| Gui Santos | 96% | 20.3<br><sub>19,17,23,23,24</sub> | 8.6<br><sub>12,6,8,13,22</sub> | 9.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>7,6,3,5,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,6,0,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8<br><sub>1,0,0,3,2</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.4 | 14.4 |
| Will Richard | 99% | 19.1<br><sub>23,27,27,17,17</sub> | 6.1<br><sub>11,20,15,3,3</sub> |  | 2.2<br><sub>3,0,5,2,2</sub> |  | 1.1<br><sub>1,3,0,2,1</sub> |  | 0.7<br><sub>2,1,1,1,1</sub> |  | 1.0 | 0.2 | 0.8 | 9.4 |
| Charles Bassey | 98% | 18.6<br><sub>16,22,25,26,22</sub> | 9.5<br><sub>4,10,16,13,10</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>0,8,13,9,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>0,0,1,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.0 | 1.3 | 17.2 |
| Georges Niang | 98% | 15.8<br><sub>14,14,15,8,19</sub> | 6.6<br><sub>0,11,5,0,11</sub> |  | 2.2<br><sub>4,1,2,1,3</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9<br><sub>0,2,1,0,3</sub> |  | 0.4 | 0.2 | 0.8 | 9.8 |
| Al Horford | 99% | 15.8<br><sub>14,-,17,18,13</sub> | 5.1<br><sub>0,-,3,7,2</sub> |  | 3.1<br><sub>5,-,2,3,2</sub> |  | 1.7<br><sub>0,-,2,2,2</sub> |  | 0.7<br><sub>0,-,0,1,0</sub> |  | 0.4 | 0.7 | 0.5 | 9.8 |
| Gary Payton II | 91% | 15.8<br><sub>8,16,24,13,17</sub> | 6.4<br><sub>2,8,2,8,9</sub> |  | 2.7<br><sub>0,8,1,1,3</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.4<br><sub>0,2,0,0,1</sub> |  | 0.9 | 0.2 | 0.8 | 10.1 |
| Brandon Williams | 88% | 15.6<br><sub>-,-,-,-,13</sub> | 9.6<br><sub>-,-,-,-,14</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,3</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.3 | 1.4 | 13.8 |
| LJ Cryer | 67% | 10.0<br><sub>24,19,12,11,-</sub> | 4.6<br><sub>7,9,9,3,-</sub> |  | 0.8<br><sub>1,0,0,0,-</sub> |  | 1.0<br><sub>3,2,1,2,-</sub> |  | 0.6<br><sub>1,3,1,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.4 |
| Graham Ike | 72% | 7.3<br><sub>8,15,4,-,-</sub> | 3.3<br><sub>3,2,5,-,-</sub> |  | 1.7<br><sub>5,2,0,-,-</sub> |  | 0.8<br><sub>1,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 5.8 |
| Malevy Leons | 58% | 6.3<br><sub>6,7,4,-,-</sub> | 2.0<br><sub>2,2,0,-,-</sub> |  | 1.2<br><sub>1,1,2,-,-</sub> |  | 0.3<br><sub>0,0,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.6 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 80% | 34.8<br><sub>-,-,36,30,36</sub> | 27.4<br><sub>-,-,20,31,33</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>-,-,9,3,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 7.9<br><sub>-,-,5,7,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>-,-,2,5,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.5 | 4.1 | 42.0 |
| Jrue Holiday | 99% | 33.4<br><sub>31,31,31,28,32</sub> | 18.1<br><sub>23,22,13,18,11</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>5,2,9,2,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>6,7,7,5,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>5,2,1,4,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.2 | 3.1 | 29.8 |
| Toumani Camara | 99% | 33.3<br><sub>33,37,35,29,31</sub> | 13.4<br><sub>10,18,6,5,8</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>8,6,5,5,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>1,4,0,3,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>2,4,1,1,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.5 | 1.9 | 20.4 |
| Sidy Cissoko | 98% | 30.2<br><sub>32,31,23,24,30</sub> | 10.6<br><sub>6,13,11,5,16</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>5,5,2,4,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,3,1,0,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>2,1,3,1,4</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.5 | 1.6 | 17.3 |
| Scoot Henderson | 99% | 28.5<br><sub>21,35,23,26,23</sub> | 15.5<br><sub>9,27,3,17,10</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,7,1,3,5</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>1,3,1,3,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>0,5,0,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 2.9 | 21.8 |
| Donovan Clingan | 99% | 27.6<br><sub>32,26,31,29,21</sub> | 12.9<br><sub>12,7,22,15,5</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 11.8<br><sub>12,13,13,18,8</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>5,2,4,5,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0<br><sub>0,0,3,1,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.7 | 1.8 | 1.5 | 27.5 |
| Robert Williams III | 99% | 20.2<br><sub>16,-,17,16,21</sub> | 7.3<br><sub>6,-,4,6,4</sub> |  | 7.6<br><sub>8,-,3,6,3</sub> |  | 1.5<br><sub>4,-,0,1,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.7 | 1.3 | 1.0 | 16.4 |
| Jayson Kent | 88% | 15.9<br><sub>27,17,3,14,6</sub> | 5.5<br><sub>8,2,0,9,0</sub> |  | 2.1<br><sub>3,1,1,2,3</sub> |  | 0.8<br><sub>0,2,0,1,0</sub> |  | 0.7<br><sub>2,0,0,3,0</sub> |  | 0.7 | 0.1 | 0.8 | 8.4 |
| Branden Carlson | 71% | 11.2<br><sub>14,10,9,6,-</sub> | 3.1<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>1,1,1,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.5 | 0.6 | 6.3 |
| Yang Hansen | 64% | 10.2<br><sub>-,12,-,3,5</sub> | 3.5<br><sub>-,2,-,2,0</sub> |  | 2.6<br><sub>-,1,-,0,2</sub> |  | 0.8<br><sub>-,1,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.3 | 0.8 | 6.9 |
| Micah Potter | 52% | 8.7<br><sub>1,-,-,3,-</sub> | 3.9<br><sub>0,-,-,0,-</sub> |  | 2.4<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| John Tonje | 52% | 8.2<br><sub>-,6,-,3,-</sub> | 2.8<br><sub>-,0,-,2,-</sub> |  | 1.8<br><sub>-,3,-,0,-</sub> |  | 0.9<br><sub>-,0,-,1,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-27/`._
