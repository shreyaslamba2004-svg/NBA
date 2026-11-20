# NBA model · Thu 19 Nov 2026 (US date)

Updated **Fri 20 Nov, 11:33 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-19/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday PA over 34.5 (35+) | POR @ MIL | draftkings | 17.60 | 15.02 | 7.10 | 14.1% | 5.3% | 6.7% | +17.2% | +147.8% | 0.3% |
| Victor Wembanyama PR over 59.5 (60+) | LAC @ SAS | draftkings | 18.00 | 15.60 | 7.62 | 13.1% | 5.2% | 6.4% | +15.4% | +136.3% | 0.2% |
| Jrue Holiday PTS over 29.5 (30+) | POR @ MIL | draftkings | 23.00 | 20.04 | 9.92 | 10.1% | 4.1% | 5.0% | +14.8% | +131.9% | 0.2% |
| Jrue Holiday PTS over 24.5 (25+) | POR @ MIL | draftkings | 10.20 | 8.98 | 4.56 | 21.9% | 9.2% | 11.1% | +13.5% | +123.7% | 0.4% |
| Jrue Holiday PRA over 39.5 (40+) | POR @ MIL | draftkings | 14.40 | 12.84 | 6.71 | 14.9% | 6.5% | 7.8% | +12.1% | +114.6% | 0.2% |
| Victor Wembanyama PR over 54.5 (55+) | LAC @ SAS | draftkings | 9.90 | 8.94 | 4.82 | 20.7% | 9.4% | 11.2% | +10.7% | +105.4% | 0.3% |
| LAC to win | LAC @ SAS | betfair_ex_au | 8.60 | 7.82 | 4.48 | 22.3% | 12.8% | 12.8% | +10.0% | +91.9% | 0.3% |
| Jaime Jaquez Jr. AST over 7.5 (8+) | POR @ MIL | draftkings | 20.80 | 18.98 | 10.46 | 9.6% | 4.5% | 5.3% | +9.7% | +98.9% | 0.1% |
| Jrue Holiday AST over 9.5 (10+) | POR @ MIL | draftkings | 15.20 | 14.14 | 8.25 | 12.1% | 6.2% | 7.1% | +7.4% | +84.3% | 0.1% |
| Jaime Jaquez Jr. AST over 5.5 (6+) | POR @ MIL | draftkings | 6.50 | 6.07 | 3.57 | 28.0% | 14.4% | 16.5% | +7.1% | +82.2% | 0.3% |
| MIL to win | POR @ MIL | pointsbetau | 5.00 | 4.67 | 3.47 | 28.8% | 21.4% | 21.4% | +7.1% | +44.0% | 0.4% |
| Devin Vassell AST over 5.5 (6+) | LAC @ SAS | draftkings | 13.20 | 12.38 | 7.36 | 13.6% | 7.1% | 8.1% | +6.7% | +79.4% | 0.1% |
| Jrue Holiday PRA over 44.5 (45+) | POR @ MIL | draftkings | 25.00 | 23.47 | 13.98 | 7.1% | 3.7% | 4.3% | +6.6% | +78.8% | 0.1% |
| Jalen Brunson PRA over 54.5 (55+) | NYK @ MIN | draftkings | 21.00 | 19.88 | 12.15 | 8.2% | 4.5% | 5.0% | +5.7% | +72.8% | 0.1% |
| Scoot Henderson AST over 5.5 (6+) | POR @ MIL | draftkings | 10.80 | 10.24 | 6.30 | 15.9% | 8.6% | 9.8% | +5.5% | +71.4% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Bones Hyland PTS under 8.5 | NYK @ MIN | tab | 2.00 | 1.89 | 1.66 | 60.3% | 51.7% | 53.0% | +6.0% | +20.7% | 1.5% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kasparas Jakucionis PTS over 11.5 (12+) | POR @ MIL | draftkings | 3.56 | 2.12 | 3.21 | 31.2% | 50.0% | 47.1% | +67.7% | +11.0% | 2.0% |
| Jrue Holiday PA over 24.5 (25+) | POR @ MIL | draftkings | 3.67 | 3.44 | 2.06 | 48.6% | 25.5% | 29.0% | +6.6% | +78.5% | 0.6% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| GSW @ MEM | Fri 20 Nov 12:00 | 114.9–117.2 | GSW 44% | 2.28 / 1.78 | MEM -2.5 | 231.5 | MEM -6.5 covers 38%; o224.5 66% |
| POR @ MIL | Fri 20 Nov 12:00 | 117.6–109.8 | POR 71% | 1.40 / 3.47 | MIL +7.5 | 227.5 | MIL +10.5 covers 58%; o229.5 45% |
| NYK @ MIN | Fri 20 Nov 12:00 | 113.7–109.5 | NYK 62% | 1.62 / 2.60 | MIN +4.5 | 222.5 | MIN +1.5 covers 41%; o216.5 64% |
| LAC @ SAS | Fri 20 Nov 12:00 | 107.4–118.1 | LAC 22% | 4.48 / 1.29 | SAS -10.5 | 225.5 | SAS -15.5 covers 37%; o224.5 52% |

### GSW @ MEM
Out: Zach Edey (MEM), GG Jackson (MEM), Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Jimmy Butler III (GSW), Stephen Curry (GSW), Draymond Green (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer PTS under 18.5 | GSW @ MEM | pointsbetau | 2.05 | 2.02 | 1.73 | 57.8% | 48.0% | 49.5% | +1.4% | +18.5% | 0.3% |
| Jaylen Wells PTS over 10.5 (11+) | GSW @ MEM | betright | 2.00 | 1.99 | 1.73 | 57.7% | 48.9% | 50.3% | +0.5% | +15.3% | 0.1% |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 33.5<br><sub>27,36,24,33,30</sub> | 21.8<br><sub>23,25,3,28,13</sub> | 21.5 · 22.5<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>7,10,7,8,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>4,0,1,3,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>4,2,0,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.8 | 3.2 | 33.3 |
| Brandin Podziemski | 96% | 32.7<br><sub>26,37,22,30,29</sub> | 18.1<br><sub>25,22,8,15,10</sub> | 15.5 · 16.5<br><sub>o 53% · u 47%</sub> | 5.4<br><sub>2,6,3,6,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>4,4,0,3,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>5,4,2,3,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 1.8 | 28.2 |
| Will Richard | 98% | 26.7<br><sub>-,19,30,23,27</sub> | 8.6<br><sub>-,9,7,11,20</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>-,4,4,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>-,0,1,1,3</sub> |  | 1.1<br><sub>-,2,1,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.1 | 13.7 |
| De'Anthony Melton | 99% | 24.4<br><sub>26,25,18,21,19</sub> | 12.3<br><sub>16,11,8,8,0</sub> | 11.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,4,4,2,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>3,4,3,1,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.5 | 1.7 | 19.2 |
| Gui Santos | 93% | 21.1<br><sub>21,12,21,19,17</sub> | 9.0<br><sub>3,0,7,12,6</sub> | 8.5 · 7.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>7,3,4,7,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>4,1,1,2,6</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.4 | 1.4 | 15.8 |
| Georges Niang | 98% | 20.8<br><sub>19,19,15,14,14</sub> | 9.3<br><sub>9,5,5,0,11</sub> |  | 3.1<br><sub>2,5,3,4,1</sub> |  | 1.5<br><sub>2,0,2,2,1</sub> |  | 1.4<br><sub>1,1,1,0,2</sub> |  | 0.5 | 0.2 | 0.9 | 13.9 |
| LJ Cryer | 88% | 20.5<br><sub>20,18,24,24,19</sub> | 9.6<br><sub>10,13,20,7,9</sub> |  | 1.8<br><sub>0,1,2,1,0</sub> |  | 2.3<br><sub>3,1,6,3,2</sub> |  | 1.7<br><sub>2,3,6,1,3</sub> |  | 0.5 | 0.1 | 1.0 | 13.7 |
| Charles Bassey | 98% | 19.1<br><sub>18,13,20,16,22</sub> | 9.2<br><sub>12,7,11,4,10</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>10,6,5,0,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,0,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 1.3 | 17.6 |
| Al Horford | 98% | 18.4<br><sub>15,21,10,14,-</sub> | 6.1<br><sub>5,2,0,0,-</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>2,1,3,5,-</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>6,4,1,0,-</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>1,0,0,0,-</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.5 | 1.0 | 0.6 | 12.6 |
| Gary Payton II | 88% | 17.9<br><sub>-,-,13,8,16</sub> | 8.0<br><sub>-,-,2,2,8</sub> |  | 3.4<br><sub>-,-,2,0,8</sub> |  | 1.5<br><sub>-,-,0,0,2</sub> |  | 0.6<br><sub>-,-,0,0,2</sub> |  | 1.0 | 0.3 | 0.8 | 12.8 |
| Graham Ike | 93% | 15.1<br><sub>12,4,13,8,15</sub> | 6.1<br><sub>4,4,5,3,2</sub> |  | 3.8<br><sub>5,0,2,5,2</sub> |  | 1.7<br><sub>2,1,3,1,2</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.8 | 0.8 | 11.5 |
| Malevy Leons | 76% | 12.0<br><sub>12,4,14,6,7</sub> | 3.4<br><sub>0,0,5,2,2</sub> |  | 2.2<br><sub>3,3,1,1,1</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.5 | 0.5 | 6.3 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 31.7<br><sub>33,25,29,29,28</sub> | 18.0<br><sub>13,12,15,29,18</sub> | 18.5 · 19.5<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>11,10,8,7,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 5.7<br><sub>5,3,5,7,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>2,1,0,7,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.7 | 2.9 | 32.8 |
| Cedric Coward | 98% | 30.5<br><sub>27,30,33,27,33</sub> | 16.3<br><sub>15,14,23,18,20</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>11,7,12,8,3</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>4,6,4,6,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,0,4,2,4</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.5 | 2.0 | 27.8 |
| Jaylen Wells | 99% | 28.1<br><sub>31,27,25,27,26</sub> | 12.3<br><sub>22,11,5,8,5</sub> | 10.5 · 9.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,2,2,4,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>5,2,1,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.1 | 1.0 | 17.2 |
| Cam Spencer | 98% | 28.0<br><sub>20,24,34,32,29</sub> | 13.5<br><sub>15,14,17,12,26</sub> | 13.5 · 12.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,2,1,6,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.9<br><sub>3,5,8,9,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>3,3,3,1,5</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.2 | 1.7 | 23.8 |
| Javon Small | 98% | 25.9<br><sub>15,15,30,29,21</sub> | 12.2<br><sub>3,10,19,12,2</sub> |  | 3.8<br><sub>1,2,2,5,4</sub> |  | 4.9<br><sub>4,5,5,12,5</sub> |  | 1.6<br><sub>1,2,3,0,0</sub> |  | 0.9 | 0.3 | 1.7 | 20.8 |
| Jerami Grant | 98% | 24.1<br><sub>20,26,-,23,20</sub> | 12.3<br><sub>14,22,-,8,8</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,1,-,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>2,1,-,2,1</sub> |  | 1.6<br><sub>2,3,-,2,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.6 | 1.4 | 16.5 |
| Taylor Hendricks | 88% | 19.9<br><sub>11,19,29,19,21</sub> | 9.5<br><sub>7,10,22,9,18</sub> | 8.5 · 7.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>2,12,5,3,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,2,4,0,2</sub> |  | 1.1<br><sub>1,2,0,1,1</sub> |  | 0.8 | 0.5 | 1.0 | 15.2 |
| Isaiah Stewart | 98% | 17.8<br><sub>18,20,15,-,-</sub> | 8.6<br><sub>3,12,11,-,-</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>1,5,3,-,-</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.9<br><sub>2,0,3,-,-</sub> |  | 0.5<br><sub>1,0,0,-,-</sub> |  | 0.3 | 1.0 | 0.9 | 13.5 |
| Olivier-Maxence Prosper | 80% | 15.4<br><sub>-,2,20,16,16</sub> | 8.1<br><sub>-,6,11,12,5</sub> |  | 3.0<br><sub>-,1,4,0,2</sub> |  | 0.9<br><sub>-,0,0,1,0</sub> |  | 0.8<br><sub>-,0,2,1,0</sub> |  | 0.6 | 0.2 | 0.7 | 12.0 |
| Quinten Post | 96% | 12.5<br><sub>-,-,-,9,6</sub> | 5.1<br><sub>-,-,-,5,3</sub> |  | 2.6<br><sub>-,-,-,3,2</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.4 | 0.5 | 8.2 |
| Kris Murray | 88% | 12.5<br><sub>-,1,19,6,6</sub> | 2.9<br><sub>-,0,3,0,5</sub> |  | 2.0<br><sub>-,1,2,1,0</sub> |  | 0.8<br><sub>-,0,3,0,0</sub> |  | 0.2<br><sub>-,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.4 | 5.8 |
| Jahmai Mashack | 66% | 12.4<br><sub>-,-,2,2,13</sub> | 4.0<br><sub>-,-,0,0,3</sub> |  | 1.6<br><sub>-,-,0,0,2</sub> |  | 1.6<br><sub>-,-,0,1,2</sub> |  | 0.3<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.3 | 0.9 | 7.3 |
| Karim Lopez | 52% | 6.7<br><sub>-,-,2,1,-</sub> | 2.8<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,2,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.7 |

</details>


### POR @ MIL
Out: Ousmane Dieng (MIL), Kyle Kuzma (MIL), Myles Turner (MIL), Deni Avdija (POR), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Robert Williams III (POR), Chris Youngblood (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Rollins PTS over 11.5 (12+) | POR @ MIL | sportsbet | 1.96 | 1.93 | 1.63 | 61.5% | 50.2% | 51.9% | +1.9% | +20.7% | 0.5% |
| Tyler Herro PTS under 20.5 | POR @ MIL | draftkings | 1.98 | 1.96 | 1.64 | 60.9% | 49.2% | 51.0% | +1.0% | +20.6% | 0.3% |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Toumani Camara | 98% | 33.8<br><sub>30,38,36,26,33</sub> | 15.0<br><sub>12,14,14,3,10</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>3,5,2,0,8</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>3,3,1,0,1</sub> |  | 2.5<br><sub>2,2,2,0,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.6 | 1.5 | 22.4 |
| Damian Lillard | 98% | 33.4<br><sub>24,32,33,24,31</sub> | 24.0<br><sub>25,18,29,9,25</sub> | 24.5 · 23.5<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>3,3,6,4,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 2.6 | 33.9 |
| Jrue Holiday | 98% | 32.2<br><sub>25,30,27,25,31</sub> | 18.9<br><sub>11,19,6,10,23</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>1,3,5,4,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.1<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 3.0<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.3 | 2.4 | 29.8 |
| Sidy Cissoko | 98% | 31.9<br><sub>33,29,26,28,32</sub> | 10.1<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.6<br><sub>3,0,1,3,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 1.4 | 17.2 |
| Donovan Clingan | 98% | 30.7<br><sub>26,30,27,22,32</sub> | 15.2<br><sub>7,5,13,10,12</sub> | 13.5 · 13.5<br><sub>o 52% · u 48%</sub> | 13.2<br><sub>13,12,11,10,12</sub> | 13.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>1,1,1,0,0</sub> |  | 0.8 | 2.2 | 1.5 | 31.2 |
| Scoot Henderson | 98% | 28.2<br><sub>23,19,23,23,21</sub> | 15.4<br><sub>11,5,11,10,9</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.3 | 2.5 | 21.8 |
| Jayson Kent | 72% | 23.0<br><sub>-,-,11,11,27</sub> | 8.8<br><sub>-,-,3,8,8</sub> |  | 3.0<br><sub>-,-,1,0,3</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> |  | 1.1 | 0.3 | 0.9 | 13.2 |
| Branden Carlson | 88% | 16.6<br><sub>8,10,8,14,14</sub> | 5.3<br><sub>2,0,5,5,6</sub> |  | 4.1<br><sub>5,2,3,6,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 0.4<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.7 | 0.7 | 10.3 |
| Yang Hansen | 52% | 13.2<br><sub>5,-,-,7,-</sub> | 5.1<br><sub>0,-,-,0,-</sub> |  | 3.6<br><sub>1,-,-,1,-</sub> |  | 0.9<br><sub>0,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.3 | 0.9 | 9.6 |
| Micah Potter | 64% | 13.1<br><sub>5,-,-,7,1</sub> | 5.9<br><sub>0,-,-,2,0</sub> |  | 3.9<br><sub>3,-,-,4,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 10.5 |
| John Tonje | 47% | 12.2<br><sub>-,-,-,7,-</sub> | 5.0<br><sub>-,-,-,7,-</sub> |  | 2.7<br><sub>-,-,-,4,-</sub> |  | 1.4<br><sub>-,-,-,3,-</sub> |  | 0.7<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.2 | 0.7 | 9.2 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 32.1<br><sub>-,35,34,20,24</sub> | 19.3<br><sub>-,27,18,5,8</sub> | 20.5 · 20.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>-,2,1,5,2</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.6<br><sub>-,7,2,3,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>-,2,2,0,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.4 | 2.5 | 28.2 |
| Jaime Jaquez Jr. | 99% | 30.4<br><sub>25,30,28,30,23</sub> | 16.0<br><sub>16,25,22,6,10</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>5,5,6,5,2</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>3,3,4,4,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,5,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.3 | 2.4 | 25.8 |
| Ryan Rollins | 98% | 27.7<br><sub>24,24,29,-,-</sub> | 14.2<br><sub>14,8,8,-,-</sub> | 11.5 · 11.5<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>5,7,10,-,-</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 4.5<br><sub>2,4,2,-,-</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>4,2,0,-,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.4 | 2.7 | 23.3 |
| Brayden Burries | 98% | 27.0<br><sub>26,23,19,29,25</sub> | 11.7<br><sub>3,8,3,13,20</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>3,5,4,8,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.3 | 1.6 | 20.3 |
| Nate Ament | 96% | 22.4<br><sub>22,22,22,17,17</sub> | 8.5<br><sub>10,2,9,5,7</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,4,3,2,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>1,1,1,1,1</sub> |  | 0.9<br><sub>2,0,2,1,0</sub> |  | 0.9 | 0.3 | 1.2 | 12.9 |
| Kel'el Ware | 98% | 22.1<br><sub>17,23,17,25,17</sub> | 10.9<br><sub>8,8,10,8,11</sub> | 11.5 · 10.5<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>4,5,6,11,3</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>1,1,1,2,1</sub> |  | 1.0<br><sub>0,0,2,1,1</sub> |  | 0.7 | 1.2 | 1.5 | 19.4 |
| Kasparas Jakucionis | 86% | 21.9<br><sub>23,4,-,26,26</sub> | 9.6<br><sub>11,4,-,25,20</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>0,2,-,5,3</sub> |  | 3.8<br><sub>4,0,-,5,5</sub> |  | 1.0<br><sub>2,0,-,4,3</sub> |  | 0.9 | 0.2 | 1.8 | 16.1 |
| Cormac Ryan | 5% | 20.9 | 9.5 |  | 2.3 |  | 1.4 |  | 1.3 |  | 0.9 | 0.3 | 1.5 | 13.2 |
| Gary Trent Jr. | 72% | 19.5<br><sub>6,4,16,30,16</sub> | 8.4<br><sub>5,6,1,18,1</sub> |  | 1.2<br><sub>0,1,0,2,1</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 1.4<br><sub>1,2,0,4,0</sub> |  | 0.8 | 0.1 | 0.7 | 10.5 |
| AJ Green | 99% | 18.0<br><sub>8,8,8,6,14</sub> | 5.7<br><sub>0,3,0,0,11</sub> |  | 1.8<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>0,1,2,0,1</sub> |  | 1.0<br><sub>0,1,0,0,3</sub> |  | 0.4 | 0.2 | 0.6 | 8.6 |
| Jericho Sims | 76% | 17.7<br><sub>8,18,-,11,18</sub> | 4.3<br><sub>2,0,-,4,4</sub> |  | 4.4<br><sub>0,4,-,2,6</sub> |  | 1.4<br><sub>0,1,-,0,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.3 | 1.1 | 10.2 |
| Kam Jones | 5% | 13.8 | 3.7 |  | 1.4 |  | 2.4 |  | 0.3 |  | 0.5 | 0.1 | 1.1 | 7.5 |
| Pete Nance | 93% | 13.7<br><sub>-,4,-,-,-</sub> | 4.0<br><sub>-,3,-,-,-</sub> |  | 2.3<br><sub>-,1,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 7.3 |
| Caris LeVert | 38% | 13.5<br><sub>-,-,-,-,8</sub> | 4.9<br><sub>-,-,-,-,8</sub> |  | 1.8<br><sub>-,-,-,-,3</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.7 | 0.4 | 0.8 | 8.1 |
| Bogoljub Markovic | 51% | 9.8<br><sub>4,4,-,-,-</sub> | 3.6<br><sub>0,0,-,-,-</sub> |  | 2.2<br><sub>2,0,-,-,-</sub> |  | 0.4<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 6.3 |

</details>


### NYK @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Joan Beringer PTS over 4.5 (5+) | NYK @ MIN | draftkings | 2.02 | 1.97 | 1.66 | 60.2% | 49.1% | 50.8% | +2.6% | +21.6% | 0.6% |
| Landry Shamet PTS over 9.5 (10+) | NYK @ MIN | draftkings | 2.47 | 2.41 | 2.99 | 33.4% | 42.9% | 41.4% | +2.4% | -17.5% | 0.4% |
| Karl-Anthony Towns PTS under 20.5 | NYK @ MIN | betright | 1.98 | 1.98 | 1.86 | 53.9% | 50.0% | 50.6% | +0.2% | +6.7% | 0.1% |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 100% | 35.3<br><sub>28,35,36,41,34</sub> | 27.5<br><sub>23,27,33,28,31</sub> | 25.5 · 25.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>4,3,1,1,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 6.1<br><sub>2,5,11,9,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>1,3,4,3,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 2.6 | 36.9 |
| OG Anunoby | 100% | 34.4<br><sub>29,34,33,44,36</sub> | 16.2<br><sub>19,14,11,21,16</sub> | 14.5 · 15.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>3,6,2,9,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,2,1,1,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>5,2,2,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.5 | 0.9 | 1.8 | 23.2 |
| Karl-Anthony Towns | 100% | 34.2<br><sub>27,34,34,43,36</sub> | 20.7<br><sub>21,21,23,28,16</sub> | 20.5 · 20.5<br><sub>o 49% · u 51%</sub> | 13.2<br><sub>16,11,15,17,16</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>3,8,5,3,8</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,2,3,3,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.8 | 2.9 | 38.1 |
| Josh Hart | 100% | 28.6<br><sub>-,26,23,26,31</sub> | 8.4<br><sub>-,6,0,0,5</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>-,4,5,5,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>-,3,4,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>-,0,0,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 1.4 | 18.4 |
| Mikal Bridges | 100% | 27.3<br><sub>17,17,29,32,30</sub> | 9.5<br><sub>4,2,18,5,17</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>5,1,3,7,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>1,2,3,3,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.0 | 0.5 | 1.0 | 15.2 |
| Landry Shamet | 98% | 23.4<br><sub>28,29,21,30,24</sub> | 8.2<br><sub>10,12,5,23,12</sub> | 7.5 · 8.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,2,3,2,1</sub> |  | 1.3<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3<br><sub>2,2,1,4,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.2 | 0.7 | 11.2 |
| Miles McBride | 98% | 15.2<br><sub>25,27,22,14,9</sub> | 5.1<br><sub>8,19,9,3,3</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,2,1,1,0</sub> |  | 1.1<br><sub>3,2,1,0,1</sub> |  | 0.7<br><sub>2,5,3,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.5 | 0.1 | 0.4 | 7.5 |
| Tyler Kolek | 93% | 13.3<br><sub>15,13,19,16,13</sub> | 4.3<br><sub>12,4,5,0,4</sub> |  | 1.7<br><sub>3,1,6,0,1</sub> |  | 3.6<br><sub>4,4,2,7,3</sub> |  | 0.4<br><sub>2,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.6 |
| Andre Drummond | 98% | 12.3<br><sub>16,14,14,7,11</sub> | 3.7<br><sub>2,0,0,2,2</sub> |  | 5.4<br><sub>14,4,6,3,8</sub> |  | 0.9<br><sub>3,3,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 10.0 |
| Jordan Clarkson | 88% | 9.5<br><sub>11,-,9,7,8</sub> | 4.2<br><sub>2,-,0,2,3</sub> |  | 1.3<br><sub>4,-,1,2,0</sub> |  | 0.7<br><sub>2,-,0,0,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 6.2 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Jose Alvarado | 66% | 7.9<br><sub>6,-,-,2,7</sub> | 3.1<br><sub>0,-,-,0,2</sub> |  | 1.1<br><sub>1,-,-,0,0</sub> |  | 1.3<br><sub>1,-,-,1,4</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |
| Mohamed Diawara | 52% | 7.6<br><sub>18,11,-,-,-</sub> | 2.5<br><sub>5,2,-,-,-</sub> |  | 1.3<br><sub>3,0,-,-,-</sub> |  | 0.8<br><sub>3,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Jaden Akins | 38% | 6.7<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 0.8 |
| Dalton Knecht | 64% | 6.6<br><sub>8,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.5 |
| James Wiseman | 48% | 6.1<br><sub>5,-,-,3,-</sub> | 2.2<br><sub>0,-,-,0,-</sub> |  | 2.0<br><sub>1,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.6 |
| Pacome Dadiet | 43% | 5.7<br><sub>6,-,1,-,-</sub> | 2.5<br><sub>8,-,0,-,-</sub> |  | 1.1<br><sub>2,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 34.8<br><sub>33,25,37,31,37</sub> | 16.2<br><sub>16,16,18,13,22</sub> | 16.5 · 15.5<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>6,9,5,6,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>3,3,6,3,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 1.0 | 1.7 | 24.8 |
| Ayo Dosunmu | 100% | 33.4<br><sub>30,27,33,30,39</sub> | 17.4<br><sub>26,18,24,8,30</sub> | 17.5 · 17.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>4,2,5,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>1,1,0,2,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>4,2,0,2,7</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.4 | 1.9 | 25.3 |
| Jonathan Kuminga | 100% | 30.4<br><sub>25,24,35,29,-</sub> | 12.9<br><sub>4,14,11,13,-</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>0,8,3,9,-</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>0,5,3,1,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,1,0,1,-</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.6 | 1.4 | 20.6 |
| LaMelo Ball | 100% | 29.9<br><sub>30,25,30,24,31</sub> | 18.7<br><sub>24,22,19,6,18</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>3,3,8,5,9</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>5,9,6,0,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>4,6,4,2,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.3 | 2.9 | 28.7 |
| Rudy Gobert | 100% | 29.1<br><sub>31,23,27,32,22</sub> | 8.1<br><sub>10,9,1,18,0</sub> | 8.5 · 8.5<br><sub>o 46% · u 54%</sub> | 9.7<br><sub>15,6,10,15,4</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>2,1,4,3,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.2 | 1.2 | 19.6 |
| Terrence Shannon Jr. | 98% | 23.5<br><sub>18,21,22,35,24</sub> | 11.8<br><sub>5,6,14,34,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>3,2,6,3,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>3,4,0,6,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.5 | 0.1 | 1.3 | 16.6 |
| Trey Lyles | 98% | 21.2<br><sub>21,15,19,19,31</sub> | 6.3<br><sub>9,2,5,9,8</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>6,0,1,3,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>2,0,2,1,4</sub> |  | 0.8<br><sub>1,0,0,2,2</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.5 | 0.4 | 0.6 | 11.6 |
| Joan Beringer | 98% | 17.6<br><sub>16,22,13,16,26</sub> | 6.0<br><sub>4,13,2,0,3</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>3,9,5,4,13</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 12.3 |
| Bones Hyland | 98% | 15.3<br><sub>13,23,21,13,17</sub> | 8.0<br><sub>14,24,12,5,13</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>2,3,1,1,2</sub> |  | 2.3<br><sub>2,8,2,5,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>1,5,3,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.2 | 1.0 | 11.8 |
| Cody Williams | 64% | 8.2<br><sub>2,7,-,4,13</sub> | 0.2<br><sub>0,0,-,0,0</sub> |  | 1.1<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 1.7 |
| Rocco Zikarsky | 38% | 6.9<br><sub>2,-,-,-,-</sub> | 2.3<br><sub>0,-,-,-,-</sub> |  | 2.0<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.6 | 0.3 | 4.7 |
| Zyon Pullin | 48% | 6.1<br><sub>-,-,-,4,-</sub> | 2.4<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,1,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Isaiah Evans | 52% | 5.7<br><sub>2,8,-,4,-</sub> | 4.1<br><sub>0,2,-,0,-</sub> |  | 0.9<br><sub>0,1,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 5.3 |
| Johni Broome | 3% | 5.3 | 1.9 |  | 1.2 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.2 | 3.5 |

</details>


### LAC @ SAS
Out: Dylan Harper (SAS), Tobias Harris (SAS), Bradley Beal (LAC), Brandon Ingram (LAC)

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.1<br><sub>32,25,37,35,30</sub> | 20.4<br><sub>24,13,24,27,20</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>0,5,4,6,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>10,6,7,7,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>3,1,3,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 3.4 | 29.8 |
| Rui Hachimura | 98% | 27.7<br><sub>26,23,32,22,27</sub> | 12.5<br><sub>14,13,7,4,20</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>3,5,11,2,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,1,3,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.6<br><sub>2,3,1,0,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.3 | 1.2 | 17.9 |
| Derrick Jones Jr. | 98% | 26.8<br><sub>29,24,29,26,28</sub> | 9.3<br><sub>8,11,14,13,5</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>4,3,5,4,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>3,0,0,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0<br><sub>0,2,4,3,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.8 | 0.9 | 14.1 |
| Brook Lopez | 98% | 24.3<br><sub>26,19,31,29,23</sub> | 12.6<br><sub>20,8,26,7,23</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>7,4,7,5,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,1,4,8,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,1,3,1,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.9 | 1.0 | 18.8 |
| Kris Dunn | 98% | 23.6<br><sub>24,19,20,18,26</sub> | 6.0<br><sub>14,3,2,7,2</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,2,3,3,5</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.4<br><sub>4,3,6,1,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.6<br><sub>2,1,0,0,0</sub> |  | 1.4 | 0.3 | 1.0 | 12.6 |
| Max Strus | 98% | 21.7<br><sub>19,22,23,25,21</sub> | 7.7<br><sub>7,12,3,14,3</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>4,3,2,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>2,3,3,4,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>1,2,0,4,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.2 | 0.8 | 13.6 |
| Keaton Wagler | 98% | 21.0<br><sub>18,23,18,28,18</sub> | 10.3<br><sub>15,11,14,12,15</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>2,0,2,4,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>4,4,1,5,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>3,1,2,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.2 | 1.6 | 15.8 |
| Kobe Sanders | 98% | 19.7<br><sub>22,26,15,20,18</sub> | 7.1<br><sub>8,9,5,2,5</sub> | – · 5.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,3,0,6,1</sub> |  | 1.9<br><sub>4,7,1,4,3</sub> |  | 0.9<br><sub>2,1,1,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.2 |
| Isaiah Jackson | 98% | 16.9<br><sub>-,16,17,15,19</sub> | 7.0<br><sub>-,4,5,13,8</sub> |  | 4.6<br><sub>-,4,3,2,5</sub> |  | 1.3<br><sub>-,0,3,2,0</sub> |  | 0.1<br><sub>-,0,0,1,0</sub> |  | 0.7 | 0.9 | 1.0 | 12.9 |
| Gradey Dick | 98% | 15.8<br><sub>17,19,19,19,17</sub> | 6.5<br><sub>15,10,13,12,0</sub> |  | 2.3<br><sub>4,3,3,2,0</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.6<br><sub>2,1,2,2,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.5 |
| Yanic Konan Niederhauser | 3% | 12.8 | 5.7 |  | 2.4 |  | 1.2 |  | 0.4 |  | 0.3 | 0.3 | 0.6 | 9.3 |
| Baba Miller | 86% | 9.7<br><sub>20,16,-,5,4</sub> | 4.3<br><sub>12,13,-,2,3</sub> |  | 1.6<br><sub>5,4,-,0,0</sub> |  | 1.0<br><sub>4,0,-,0,0</sub> |  | 0.2<br><sub>0,1,-,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 6.9 |
| Jalen Pickett | 48% | 7.1<br><sub>2,8,-,-,-</sub> | 2.8<br><sub>0,3,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.0<br><sub>0,1,-,-,-</sub> |  | 0.2<br><sub>0,1,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.7 |
| Cam Christie | 52% | 6.8<br><sub>2,-,-,-,4</sub> | 2.9<br><sub>0,-,-,-,3</sub> |  | 1.0<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley | 52% | 6.4<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 98% | 34.2<br><sub>-,-,23,32,36</sub> | 14.2<br><sub>-,-,7,6,12</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>-,-,2,6,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>-,-,2,1,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>-,-,0,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.4 | 1.1 | 22.1 |
| Victor Wembanyama | 99% | 33.6<br><sub>25,32,21,35,34</sub> | 31.1<br><sub>40,32,12,26,25</sub> | 27.5 · 27.5<br><sub>o 51% · u 49%</sub> | 13.1<br><sub>11,9,12,10,18</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 4.0<br><sub>3,1,6,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,2,0,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 4.0 | 3.0 | 48.1 |
| Stephon Castle | 99% | 33.0<br><sub>30,29,25,35,31</sub> | 18.6<br><sub>4,11,32,20,10</sub> | 17.5 · 17.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>8,1,5,4,2</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 7.2<br><sub>7,3,6,9,7</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,1,5,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.3 | 3.1 | 31.0 |
| De'Aaron Fox | 98% | 33.0<br><sub>29,31,17,-,34</sub> | 16.5<br><sub>15,17,7,-,6</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>9,4,5,-,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.5<br><sub>6,9,1,-,2</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,2,0,-,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.4 | 2.6 | 27.2 |
| Julian Champagnie | 99% | 29.0<br><sub>27,35,23,24,30</sub> | 10.5<br><sub>11,12,7,4,14</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>3,0,8,5,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>2,2,3,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,3,1,1,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.5 | 0.8 | 17.3 |
| Keldon Johnson | 99% | 24.9<br><sub>26,28,25,29,15</sub> | 10.7<br><sub>4,10,18,11,4</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,6,4,10,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>3,4,4,2,1</sub> |  | 0.7<br><sub>0,0,2,1,0</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.2 | 1.2 | 18.1 |
| Luke Kornet | 99% | 16.3<br><sub>13,14,16,13,14</sub> | 4.4<br><sub>2,7,6,2,2</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>4,5,7,2,1</sub> |  | 1.2<br><sub>1,1,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.6 | 10.2 |
| Harrison Barnes | 91% | 15.6<br><sub>21,13,21,14,10</sub> | 5.4<br><sub>11,3,11,0,0</sub> |  | 1.7<br><sub>2,1,1,0,3</sub> |  | 0.9<br><sub>0,0,1,2,4</sub> |  | 0.7<br><sub>2,1,3,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 8.0 |
| Jordan McLaughlin | 66% | 13.9<br><sub>11,2,14,19,-</sub> | 4.5<br><sub>4,4,4,10,-</sub> |  | 2.0<br><sub>4,0,6,1,-</sub> |  | 2.0<br><sub>2,0,2,2,-</sub> |  | 0.5<br><sub>0,0,0,2,-</sub> |  | 0.8 | 0.1 | 0.7 | 8.6 |
| Carter Bryant | 91% | 11.8<br><sub>14,15,19,5,2</sub> | 4.2<br><sub>8,10,8,0,0</sub> |  | 2.0<br><sub>1,1,3,1,0</sub> |  | 0.8<br><sub>1,2,2,0,0</sub> |  | 0.5<br><sub>2,2,2,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 6.9 |
| Tarris Reed Jr. | 58% | 8.8<br><sub>9,2,11,-,-</sub> | 3.1<br><sub>4,0,2,-,-</sub> |  | 3.2<br><sub>3,0,4,-,-</sub> |  | 0.4<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.7 |
| David Jones Garcia | 58% | 6.8<br><sub>8,2,-,-,-</sub> | 2.5<br><sub>2,0,-,-,-</sub> |  | 1.1<br><sub>0,0,-,-,-</sub> |  | 1.0<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 4.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-19/`._
