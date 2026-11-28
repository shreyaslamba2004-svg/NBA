# NBA model · Fri 27 Nov 2026 (US date)

Updated **Sat 28 Nov, 12:13 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-27/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija AST over 11.5 (12+) | GSW @ POR | draftkings | 17.20 | 14.47 | 7.37 | 13.6% | 5.4% | 6.9% | +18.8% | +133.4% | 0.3% |
| Jrue Holiday AST over 9.5 (10+) | GSW @ POR | draftkings | 10.10 | 8.93 | 4.99 | 20.0% | 9.2% | 11.2% | +13.2% | +102.3% | 0.4% |
| Deni Avdija PRA over 59.5 (60+) | GSW @ POR | draftkings | 21.00 | 18.73 | 10.66 | 9.4% | 4.5% | 5.3% | +12.2% | +97.0% | 0.1% |
| Jrue Holiday AST over 11.5 (12+) | GSW @ POR | draftkings | 24.00 | 21.41 | 12.23 | 8.2% | 3.9% | 4.7% | +12.1% | +96.2% | 0.1% |
| Deni Avdija AST over 9.5 (10+) | GSW @ POR | draftkings | 6.67 | 5.99 | 3.47 | 28.8% | 14.0% | 16.7% | +11.3% | +92.0% | 0.5% |
| Deni Avdija PTS over 44.5 (45+) | GSW @ POR | draftkings | 25.00 | 22.88 | 13.87 | 7.2% | 3.7% | 4.4% | +9.2% | +80.2% | 0.1% |
| Rudy Gobert AST over 3.5 (4+) | MEM @ MIN | draftkings | 9.40 | 8.67 | 5.33 | 18.8% | 9.9% | 11.5% | +8.5% | +76.5% | 0.2% |
| Rudy Gobert PA over 19.5 (20+) | MEM @ MIN | draftkings | 15.60 | 14.60 | 9.32 | 10.7% | 6.0% | 6.9% | +6.8% | +67.3% | 0.1% |
| Sidy Cissoko AST over 5.5 (6+) | GSW @ POR | draftkings | 18.80 | 17.61 | 11.25 | 8.9% | 5.0% | 5.7% | +6.8% | +67.1% | 0.1% |
| Toumani Camara AST over 3.5 (4+) | GSW @ POR | draftkings | 7.30 | 6.87 | 4.45 | 22.5% | 12.8% | 14.5% | +6.2% | +64.1% | 0.2% |
| P.J. Washington AST over 3.5 (4+) | DAL @ PHX | draftkings | 17.20 | 16.29 | 10.71 | 9.3% | 5.4% | 6.1% | +5.6% | +60.6% | 0.1% |
| Rudy Gobert REB over 15.5 (16+) | MEM @ MIN | draftkings | 8.40 | 7.97 | 5.28 | 18.9% | 11.1% | 12.5% | +5.3% | +59.1% | 0.2% |
| Zion Williamson AST over 5.5 (6+) | NOP @ LAC | draftkings | 10.80 | 10.26 | 6.80 | 14.7% | 8.6% | 9.8% | +5.3% | +58.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MEM @ MIN | Sat 28 Nov 12:30 | 111.5–115.4 | MEM 39% | 2.56 / 1.64 | MIN -4.5 | 226.5 | MIN -2.5 covers 55%; o220.5 63% |
| DAL @ PHX | Sat 28 Nov 13:00 | 112.0–116.7 | DAL 37% | 2.72 / 1.58 | PHX -4.5 | 228.5 | PHX -4.5 covers 51%; o225.5 57% |
| LAL @ SAS | Sat 28 Nov 13:30 | 110.2–112.9 | LAL 42% | 2.36 / 1.73 | SAS -2.5 | 222.5 | SAS -6.5 covers 39%; o226.5 42% |
| DEN @ UTA | Sat 28 Nov 13:30 | 124.7–115.2 | DEN 75% | 1.33 / 3.99 | UTA +9.5 | 239.5 | UTA +9.5 covers 50%; o232.5 65% |
| NOP @ LAC | Sat 28 Nov 13:30 | 110.9–116.6 | NOP 34% | 2.92 / 1.52 | LAC -5.5 | 227.5 | LAC -2.5 covers 60%; o229.5 46% |
| GSW @ POR | Sat 28 Nov 13:30 | 110.2–113.4 | GSW 41% | 2.41 / 1.71 | POR -3.5 | 223.5 | POR -8.5 covers 35%; o216.5 64% |

### MEM @ MIN
Out: LaMelo Ball (MIN), Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Rudy Gobert PTS over 8.5 (9+) | MEM @ MIN | pointsbetau | 2.05 | 1.96 | 1.62 | 61.8% | 48.7% | 51.1% | +4.7% | +26.8% | 1.1% |
| Bones Hyland PTS under 12.5 | MEM @ MIN | pointsbetau | 2.00 | 1.97 | 1.79 | 55.7% | 49.7% | 50.8% | +1.6% | +11.5% | 0.4% |
| Cam Spencer PTS over 10.5 (11+) | MEM @ MIN | pointsbetau | 2.00 | 1.98 | 1.75 | 57.0% | 49.1% | 50.5% | +1.1% | +14.0% | 0.3% |
| Ayo Dosunmu PTS over 19.5 (20+) | MEM @ MIN | pointsbetau | 2.00 | 1.99 | 1.85 | 54.1% | 49.4% | 50.2% | +0.4% | +8.2% | 0.1% |
| Cedric Coward PTS under 16.5 | MEM @ MIN | pointsbetau | 1.90 | 1.90 | 1.67 | 59.9% | 51.0% | 52.6% | +0.0% | +13.9% | 0.0% |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 100% | 30.5<br><sub>33,25,30,30,26</sub> | 15.7<br><sub>20,19,23,16,14</sub> | 16.5 · 16.5<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>3,4,7,9,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>5,4,2,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>4,5,4,0,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.5 | 2.0 | 26.2 |
| Ty Jerome | 100% | 29.9<br><sub>-,-,27,29,25</sub> | 22.4<br><sub>-,-,18,29,17</sub> | 21.5 · 22.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>-,-,4,4,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>-,-,6,3,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>-,-,3,7,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 2.6 | 31.1 |
| Jaylen Wells | 100% | 28.4<br><sub>26,24,25,20,27</sub> | 11.6<br><sub>5,22,8,8,19</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>4,7,1,2,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>2,0,0,0,1</sub> |  | 1.6<br><sub>1,4,0,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.2 | 0.9 | 16.2 |
| Kris Murray | 100% | 28.3<br><sub>6,4,12,32,32</sub> | 6.3<br><sub>5,0,7,9,8</sub> | 5.5 · 5.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>0,1,0,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>1,0,1,1,0</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.6 | 0.9 | 11.7 |
| Cam Spencer | 99% | 25.9<br><sub>29,27,30,21,24</sub> | 12.3<br><sub>26,9,9,24,16</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>1,2,5,1,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>7,11,5,5,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>5,1,0,3,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.4 | 20.6 |
| Taylor Hendricks | 91% | 23.9<br><sub>21,20,27,24,25</sub> | 9.5<br><sub>18,11,5,3,5</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>6,1,7,4,0</sub> |  | 1.1<br><sub>2,1,2,1,1</sub> |  | 1.0<br><sub>1,0,0,1,0</sub> |  | 1.0 | 0.7 | 1.1 | 15.2 |
| Zach Edey | 100% | 23.1<br><sub>21,-,23,23,9</sub> | 9.2<br><sub>11,-,8,8,7</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 8.2<br><sub>2,-,2,11,4</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>1,-,0,1,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.4 | 1.5 | 18.5 |
| Javon Small | 98% | 21.9<br><sub>21,25,-,19,17</sub> | 9.9<br><sub>2,14,-,3,8</sub> |  | 3.3<br><sub>4,7,-,3,2</sub> |  | 3.7<br><sub>5,7,-,5,1</sub> |  | 1.2<br><sub>0,2,-,0,2</sub> |  | 0.8 | 0.2 | 1.4 | 16.8 |
| Olivier-Maxence Prosper | 91% | 20.4<br><sub>16,24,23,19,19</sub> | 10.3<br><sub>5,16,7,6,9</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,5,6,3,4</sub> |  | 1.0<br><sub>0,1,0,0,2</sub> |  | 0.9<br><sub>0,1,0,0,1</sub> |  | 0.9 | 0.3 | 1.1 | 15.1 |
| Jahmai Mashack | 67% | 12.7<br><sub>13,26,22,-,4</sub> | 3.1<br><sub>3,0,0,-,0</sub> |  | 1.6<br><sub>2,3,2,-,0</sub> |  | 1.4<br><sub>2,4,1,-,0</sub> |  | 0.2<br><sub>1,0,0,-,0</sub> |  | 0.6 | 0.3 | 0.7 | 6.0 |
| Quinten Post | 86% | 12.7<br><sub>6,10,-,3,14</sub> | 4.3<br><sub>3,5,-,0,0</sub> |  | 2.5<br><sub>2,1,-,0,4</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 7.2 |
| Lawson Lovering | 48% | 8.5<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 5.4 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 36.5<br><sub>37,39,36,34,37</sub> | 20.9<br><sub>22,17,25,34,32</sub> | 19.5 · 19.5<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>5,3,5,10,10</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,1,4,6,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>2,4,1,4,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3 | 1.1 | 2.3 | 31.5 |
| Ayo Dosunmu | 100% | 35.2<br><sub>39,32,34,30,35</sub> | 21.5<br><sub>30,6,19,23,16</sub> | 19.5 · 18.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>4,4,2,3,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>5,4,2,5,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>7,2,1,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.4 | 2.7 | 30.9 |
| Jonathan Kuminga | 100% | 32.9<br><sub>-,35,37,26,32</sub> | 15.7<br><sub>-,23,16,15,7</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>-,3,4,5,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>-,3,2,4,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>-,2,2,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.8 | 2.2 | 24.7 |
| Rudy Gobert | 100% | 32.4<br><sub>22,35,32,27,32</sub> | 10.5<br><sub>0,9,7,7,9</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 11.9<br><sub>4,7,11,6,7</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,0,2,3,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.6 | 1.6 | 24.6 |
| Terrence Shannon Jr. | 100% | 30.3<br><sub>24,21,26,24,20</sub> | 18.4<br><sub>12,10,15,17,8</sub> | 16.5 · 16.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>1,4,5,1,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.9<br><sub>4,3,2,5,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,0,3,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 1.9 | 26.1 |
| Trey Lyles | 99% | 22.1<br><sub>31,16,12,24,23</sub> | 7.4<br><sub>8,8,3,9,9</sub> | 6.5 · 7.5<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>7,6,3,3,10</sub> |  | 1.4<br><sub>4,1,1,2,1</sub> |  | 1.0<br><sub>2,2,1,0,3</sub> |  | 0.7 | 0.4 | 0.8 | 13.8 |
| Bones Hyland | 98% | 20.4<br><sub>17,15,16,16,17</sub> | 12.5<br><sub>13,6,7,14,9</sub> | 12.5 · 13.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,1,0,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 3.9<br><sub>1,1,4,6,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>3,1,1,4,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 1.3 | 18.6 |
| Joan Beringer | 98% | 17.6<br><sub>26,13,16,19,16</sub> | 5.6<br><sub>3,5,0,0,4</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>13,3,4,4,5</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.8 | 0.7 | 12.4 |
| Zyon Pullin | 52% | 8.6<br><sub>-,-,-,2,-</sub> | 3.6<br><sub>-,-,-,4,-</sub> |  | 1.2<br><sub>-,-,-,2,-</sub> |  | 1.2<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.1 |
| Cody Williams | 52% | 7.8<br><sub>13,-,-,2,-</sub> | 0.1<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 1.5 |
| Isaiah Evans | 48% | 6.8<br><sub>-,-,-,2,-</sub> | 3.6<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.3 |
| Johni Broome | 48% | 6.4<br><sub>-,-,-,2,-</sub> | 2.5<br><sub>-,-,-,0,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |

</details>


### DAL @ PHX
Out: Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX), Sergio de Larrea (DAL), Kyrie Irving (DAL), Dereck Lively II (DAL)

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 99% | 34.9<br><sub>27,34,36,31,31</sub> | 25.5<br><sub>17,33,22,28,24</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>3,5,6,3,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>4,9,8,4,12</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,3,3,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.7 | 3.1 | 38.5 |
| P.J. Washington | 99% | 31.0<br><sub>25,25,-,-,25</sub> | 14.3<br><sub>8,21,-,-,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.6<br><sub>5,5,-,-,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>4,2,-,-,0</sub> |  | 1.7<br><sub>0,5,-,-,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.9 | 1.7 | 22.5 |
| Daniel Gafford | 99% | 26.3<br><sub>19,24,31,28,27</sub> | 11.9<br><sub>3,6,10,10,13</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>4,6,10,4,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,2,3,4,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.4 | 21.1 |
| Caleb Martin | 98% | 25.5<br><sub>34,20,20,29,30</sub> | 7.4<br><sub>12,8,0,13,13</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>5,5,4,6,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>5,3,3,4,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>4,2,0,3,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.3 | 1.0 | 13.8 |
| Naji Marshall | 97% | 25.2<br><sub>23,27,14,25,22</sub> | 12.5<br><sub>13,12,4,6,14</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,5,3,0,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>2,2,1,4,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>3,2,0,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 1.1 | 0.1 | 1.7 | 19.0 |
| Zaccharie Risacher | 98% | 23.8<br><sub>27,18,29,28,21</sub> | 9.3<br><sub>18,3,11,15,12</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>5,3,7,8,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.3<br><sub>0,0,1,2,1</sub> |  | 0.9<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.7 | 1.2 | 15.4 |
| Walter Clayton Jr. | 97% | 20.7<br><sub>23,27,25,21,14</sub> | 8.2<br><sub>13,8,16,9,5</sub> |  | 2.9<br><sub>4,2,5,0,2</sub> |  | 3.2<br><sub>3,7,1,3,2</sub> |  | 1.2<br><sub>3,2,2,2,1</sub> |  | 0.7 | 0.1 | 1.7 | 14.3 |
| Morez Johnson Jr. | 99% | 17.7<br><sub>26,15,17,20,19</sub> | 6.6<br><sub>2,3,9,7,9</sub> |  | 3.8<br><sub>6,1,7,6,10</sub> |  | 1.5<br><sub>4,1,2,2,1</sub> |  | 0.4<br><sub>0,0,1,1,1</sub> |  | 0.6 | 0.1 | 1.1 | 11.9 |
| Max Christie | 99% | 16.6<br><sub>-,8,24,16,4</sub> | 6.2<br><sub>-,5,13,3,2</sub> |  | 2.0<br><sub>-,1,4,2,1</sub> |  | 1.0<br><sub>-,2,0,0,0</sub> |  | 0.9<br><sub>-,1,3,1,0</sub> |  | 0.5 | 0.2 | 0.8 | 9.2 |
| Santi Aldama | 98% | 13.8<br><sub>-,6,9,16,10</sub> | 6.2<br><sub>-,0,0,9,3</sub> |  | 3.0<br><sub>-,0,1,4,1</sub> |  | 1.0<br><sub>-,0,0,1,0</sub> |  | 0.7<br><sub>-,0,0,1,1</sub> |  | 0.4 | 0.3 | 0.7 | 10.2 |
| Marcus Sasser | 48% | 12.6<br><sub>18,4,-,-,-</sub> | 4.4<br><sub>5,0,-,-,-</sub> |  | 1.2<br><sub>1,2,-,-,-</sub> |  | 1.5<br><sub>2,1,-,-,-</sub> |  | 0.6<br><sub>1,0,-,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 7.2 |
| Moussa Cisse | 58% | 7.3<br><sub>4,4,-,-,2</sub> | 2.5<br><sub>1,0,-,-,0</sub> |  | 2.8<br><sub>1,1,-,-,0</sub> |  | 0.2<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.5 |
| Jett Howard | 52% | 7.1<br><sub>7,-,-,-,-</sub> | 2.9<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 99% | 35.8<br><sub>37,33,38,42,36</sub> | 25.6<br><sub>20,29,23,22,25</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>4,2,2,5,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>8,6,3,8,5</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>1,2,1,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 3.0 | 35.8 |
| Dillon Brooks | 99% | 30.3<br><sub>27,31,25,34,31</sub> | 17.1<br><sub>15,29,18,16,12</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,3,3,5,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>4,5,3,7,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.1<br><sub>3,5,2,2,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.5 | 23.7 |
| Jalen Green | 98% | 30.0<br><sub>27,30,25,37,35</sub> | 17.0<br><sub>16,18,14,25,16</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,7,4,3,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.4<br><sub>3,7,3,0,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,4,1,3,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.4 | 2.4 | 24.7 |
| Miles Bridges | 99% | 28.7<br><sub>29,29,25,35,25</sub> | 13.6<br><sub>16,13,18,14,2</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 6.6<br><sub>8,6,9,11,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,5,4,5,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>2,1,1,2,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.5 | 1.1 | 23.5 |
| Collin Gillespie | 99% | 24.6<br><sub>26,17,27,30,22</sub> | 10.3<br><sub>10,9,16,18,5</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>3,3,4,3,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.7<br><sub>3,1,5,3,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>2,2,3,3,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.1 | 1.2 | 17.3 |
| Oso Ighodaro | 99% | 23.8<br><sub>33,21,27,30,20</sub> | 6.9<br><sub>8,7,3,7,13</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>11,4,7,4,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.1 | 15.5 |
| Jordan Goodwin | 98% | 19.6<br><sub>20,17,28,18,17</sub> | 7.7<br><sub>11,2,5,6,11</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>6,5,9,2,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>2,3,4,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,0,1,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.2 | 0.7 | 14.2 |
| Khaman Maluach | 98% | 18.6<br><sub>11,21,18,16,25</sub> | 7.5<br><sub>4,10,9,8,12</sub> |  | 5.9<br><sub>6,2,6,6,6</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.1 | 1.1 | 14.2 |
| Luke Kennard | 99% | 17.4<br><sub>17,17,15,14,19</sub> | 7.0<br><sub>12,3,5,4,8</sub> |  | 2.0<br><sub>2,3,0,1,1</sub> |  | 1.7<br><sub>0,1,0,2,2</sub> |  | 1.0<br><sub>4,1,1,0,1</sub> |  | 0.5 | 0.1 | 0.6 | 10.8 |
| Ryan Dunn | 98% | 13.2<br><sub>12,13,9,9,10</sub> | 3.9<br><sub>5,6,0,3,0</sub> |  | 3.1<br><sub>1,5,5,2,2</sub> |  | 0.9<br><sub>0,2,0,0,1</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.5 | 0.3 | 0.4 | 8.0 |
| Rasheer Fleming | 38% | 7.2<br><sub>-,4,-,-,-</sub> | 2.6<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Jamaree Bouyea | 38% | 6.6<br><sub>-,4,-,-,-</sub> | 2.7<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,1,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Koa Peat | 52% | 6.1<br><sub>1,4,3,-,-</sub> | 3.0<br><sub>0,2,0,-,-</sub> |  | 1.4<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |

</details>


### LAL @ SAS
Out: Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.2–112.9 | LAL 42% | 2.36 / 1.73 | SAS -2.5 | 222.5 | SAS -6.5 covers 39%; o226.5 42% |
| Expected (weighted by chance each plays) | 109.9–113.8 | LAL 39% | 2.57 / 1.64 | SAS -4.5 | 223.5 | SAS -6.5 covers 44%; o226.5 43% |
| if De'Aaron Fox plays | 110.2–113.7 | LAL 40% | 2.51 / 1.66 | SAS -3.5 | 223.5 | SAS -6.5 covers 42%; o226.5 44% |
| if Dylan Harper plays | 110.3–113.8 | LAL 40% | 2.49 / 1.67 | SAS -3.5 | 223.5 | SAS -6.5 covers 42%; o226.5 44% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 28.9 | 13.5 | 3.5 | 6.1 | 1.2 | 1.3 | 0.3 | 2.5 | 23.0 | full tables below |
| Dylan Harper (SAS) | Questionable | 55% | 29.1 | 16.1 | 4.8 | 4.5 | 1.2 | 1.0 | 0.3 | 1.9 | 25.4 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 99% | 34.5<br><sub>36,42,37,36,33</sub> | 29.9<br><sub>43,36,29,25,28</sub> | 33.5 · –<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.5 | 3.9 | 43.5 |
| Austin Reaves | 98% | 31.0<br><sub>-,-,-,-,-</sub> | 18.2<br><sub>-,-,-,-,-</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 2.6 | 25.8 |
| Walker Kessler | 99% | 28.0<br><sub>32,-,31,30,36</sub> | 10.8<br><sub>14,-,10,15,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 9.4<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.5 | 21.7 |
| Quentin Grimes | 99% | 26.8<br><sub>37,42,35,35,30</sub> | 10.1<br><sub>22,47,20,13,9</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.3 | 15.9 |
| Jake LaRavia | 98% | 23.1<br><sub>32,23,30,24,37</sub> | 5.7<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.4 | 0.9 | 11.0 |
| Matisse Thybulle | 98% | 20.9<br><sub>26,31,21,27,27</sub> | 5.7<br><sub>12,7,2,14,14</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7 | 0.7 | 0.7 | 8.9 |
| Ziaire Williams | 98% | 17.9<br><sub>19,24,18,28,19</sub> | 6.0<br><sub>6,0,7,5,9</sub> |  | 2.0<br><sub>2,1,2,0,4</sub> |  | 1.0<br><sub>3,1,0,1,0</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.0 |
| Collin Sexton | 99% | 17.9<br><sub>24,25,20,18,23</sub> | 9.9<br><sub>16,10,12,10,12</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.0<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.2 | 1.4 | 13.7 |
| Sandro Mamukelashvili | 99% | 16.0<br><sub>21,23,21,20,13</sub> | 6.2<br><sub>4,3,6,9,2</sub> |  | 3.4<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.7 |
| Jarred Vanderbilt | 91% | 9.2<br><sub>12,14,12,10,12</sub> | 2.4<br><sub>2,4,0,4,1</sub> |  | 2.7<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.9 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 36% | 6.7<br><sub>-,17,-,-,-</sub> | 1.4<br><sub>-,4,-,-,-</sub> |  | 2.3<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.2 |
| Cameron Carr | 80% | 6.2<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.2<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Carson Cooper | 52% | 6.1<br><sub>-,18,2,-,-</sub> | 1.9<br><sub>-,3,2,-,-</sub> |  | 1.7<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.3 | 4.1 |
| Adou Thiero | 52% | 5.9<br><sub>-,6,6,-,-</sub> | 2.2<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Jaden Hardy | 43% | 5.9<br><sub>-,-,2,-,-</sub> | 3.5<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.0 | 0.3 | 4.6 |
| Bronny James | 47% | 5.2<br><sub>-,-,2,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.6 |
| Chris Manon | 52% | 5.2<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.8 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 99% | 34.7<br><sub>36,32,26,34,38</sub> | 15.7<br><sub>12,15,10,16,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>5,4,3,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>4,4,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,1,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.4 | 1.3 | 23.7 |
| Victor Wembanyama | 99% | 33.4<br><sub>34,33,32,-,35</sub> | 30.6<br><sub>25,32,50,-,44</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.5<br><sub>18,11,19,-,16</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>4,3,1,-,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.2<br><sub>1,2,5,-,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2 | 3.5 | 3.1 | 47.5 |
| Stephon Castle | 99% | 33.3<br><sub>31,33,29,37,34</sub> | 18.9<br><sub>10,21,19,28,20</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>2,6,3,8,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 8.1<br><sub>7,12,6,11,9</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,2,5,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 3.5 | 32.5 |
| Julian Champagnie | 99% | 31.7<br><sub>30,29,25,30,37</sub> | 12.7<br><sub>14,20,9,22,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>6,4,3,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>4,4,3,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.5 | 1.0 | 19.8 |
| Keldon Johnson | 99% | 28.2<br><sub>15,27,23,26,33</sub> | 11.6<br><sub>4,10,10,12,3</sub> |  | 5.9<br><sub>2,5,4,4,12</sub> |  | 2.6<br><sub>1,3,4,5,2</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.8 | 0.2 | 1.3 | 20.1 |
| Harrison Barnes | 96% | 18.4<br><sub>10,16,21,26,15</sub> | 6.5<br><sub>0,9,3,9,5</sub> |  | 2.1<br><sub>3,2,5,2,0</sub> |  | 1.1<br><sub>4,1,2,2,1</sub> |  | 0.9<br><sub>0,1,0,1,1</sub> |  | 0.4 | 0.1 | 0.7 | 9.8 |
| Jordan McLaughlin | 88% | 17.2<br><sub>-,11,18,14,15</sub> | 4.9<br><sub>-,0,0,6,4</sub> |  | 2.3<br><sub>-,1,3,2,2</sub> |  | 2.7<br><sub>-,5,2,0,0</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 1.1 | 0.1 | 0.9 | 9.9 |
| Luke Kornet | 99% | 17.1<br><sub>14,15,10,29,13</sub> | 4.5<br><sub>2,4,0,18,4</sub> |  | 5.0<br><sub>1,0,3,11,5</sub> |  | 1.4<br><sub>1,3,0,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.6 | 10.8 |
| Carter Bryant | 96% | 14.6<br><sub>2,13,20,12,14</sub> | 5.2<br><sub>0,3,8,0,2</sub> |  | 2.4<br><sub>0,1,3,3,6</sub> |  | 0.9<br><sub>0,0,0,2,1</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.5 |
| Ja'Kobi Gillespie | 93% | 12.4<br><sub>-,-,-,15,7</sub> | 4.0<br><sub>-,-,-,3,0</sub> |  | 1.7<br><sub>-,-,-,2,1</sub> |  | 1.3<br><sub>-,-,-,4,0</sub> |  | 0.5<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.1 | 0.4 | 7.0 |
| Tarris Reed Jr. | 52% | 10.1<br><sub>-,-,6,15,-</sub> | 3.2<br><sub>-,-,0,7,-</sub> |  | 4.2<br><sub>-,-,4,7,-</sub> |  | 0.6<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.5 | 0.7 | 8.0 |
| David Jones Garcia | 52% | 7.1<br><sub>-,-,4,2,-</sub> | 2.6<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,1,0,-</sub> |  | 1.0<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.7 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 99% | 34.6<br><sub>36,42,37,36,33</sub> | 29.9<br><sub>43,36,29,25,28</sub> | 33.5 · –<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.5 | 3.9 | 43.5 |
| Austin Reaves (LAL) | 98% | 31.0<br><sub>-,-,-,-,-</sub> | 18.1<br><sub>-,-,-,-,-</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.9<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 2.6 | 25.7 |
| Walker Kessler (LAL) | 99% | 28.1<br><sub>32,-,31,30,36</sub> | 10.8<br><sub>14,-,10,15,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 9.4<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.4 | 21.7 |
| Quentin Grimes (LAL) | 99% | 26.8<br><sub>37,42,35,35,30</sub> | 10.1<br><sub>22,47,20,13,9</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.3 | 15.8 |
| Jake LaRavia (LAL) | 98% | 23.3<br><sub>32,23,30,24,37</sub> | 5.8<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.4 | 0.9 | 11.1 |
| Matisse Thybulle (LAL) | 98% | 20.9<br><sub>26,31,21,27,27</sub> | 5.7<br><sub>12,7,2,14,14</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7 | 0.7 | 0.7 | 9.0 |
| Ziaire Williams (LAL) | 98% | 18.1<br><sub>19,24,18,28,19</sub> | 6.1<br><sub>6,0,7,5,9</sub> |  | 2.0<br><sub>2,1,2,0,4</sub> |  | 1.0<br><sub>3,1,0,1,0</sub> |  | 0.8<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.1 |
| Collin Sexton (LAL) | 99% | 17.9<br><sub>24,25,20,18,23</sub> | 9.8<br><sub>16,10,12,10,12</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.0<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.2 | 1.4 | 13.6 |
| Sandro Mamukelashvili (LAL) | 99% | 16.0<br><sub>21,23,21,20,13</sub> | 6.2<br><sub>4,3,6,9,2</sub> |  | 3.4<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.7 |
| Jarred Vanderbilt (LAL) | 91% | 9.2<br><sub>12,14,12,10,12</sub> | 2.5<br><sub>2,4,0,4,1</sub> |  | 2.7<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 6.0 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Kevon Looney (LAL) | 36% | 6.6<br><sub>-,17,-,-,-</sub> | 1.4<br><sub>-,4,-,-,-</sub> |  | 2.3<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.2 |
| Cameron Carr (LAL) | 80% | 6.3<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.3<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Carson Cooper (LAL) | 52% | 6.1<br><sub>-,18,2,-,-</sub> | 1.9<br><sub>-,3,2,-,-</sub> |  | 1.7<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |
| Jaden Hardy (LAL) | 43% | 6.0<br><sub>-,-,2,-,-</sub> | 3.5<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.0 | 0.3 | 4.7 |
| Adou Thiero (LAL) | 52% | 5.9<br><sub>-,6,6,-,-</sub> | 2.2<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Bronny James (LAL) | 47% | 5.3<br><sub>-,-,2,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 2.8 |
| Chris Manon (LAL) | 52% | 5.2<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.9 |
| Devin Vassell (SAS) | 99% | 32.0<br><sub>36,32,26,34,38</sub> | 13.7<br><sub>12,15,10,16,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>5,4,3,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>4,4,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,1,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.4 | 1.1 | 20.8 |
| Victor Wembanyama (SAS) | 99% | 32.0<br><sub>34,33,32,-,35</sub> | 28.7<br><sub>25,32,50,-,44</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.4<br><sub>18,11,19,-,16</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>4,3,1,-,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.2<br><sub>1,2,5,-,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2 | 3.2 | 2.8 | 44.6 |
| Stephon Castle (SAS) | 99% | 31.2<br><sub>31,33,29,37,34</sub> | 17.4<br><sub>10,21,19,28,20</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>2,6,3,8,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>7,12,6,11,9</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,2,5,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 3.2 | 29.8 |
| De'Aaron Fox (SAS) | 100% | 28.9<br><sub>34,32,26,-,-</sub> | 13.5<br><sub>6,10,5,-,-</sub> | 13.5 · – | 3.5<br><sub>2,2,2,-,-</sub> | 3.5 | 6.1<br><sub>2,5,10,-,-</sub> | 5.5 | 1.2<br><sub>0,0,0,-,-</sub> | 0.5 | 1.3 | 0.3 | 2.5 | 23.0 |
| Julian Champagnie (SAS) | 99% | 28.7<br><sub>30,29,25,30,37</sub> | 11.6<br><sub>14,20,9,22,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,4,3,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>4,4,3,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 0.9 | 18.0 |
| Keldon Johnson (SAS) | 99% | 25.1<br><sub>15,27,23,26,33</sub> | 10.1<br><sub>4,10,10,12,3</sub> |  | 5.3<br><sub>2,5,4,4,12</sub> |  | 2.2<br><sub>1,3,4,5,2</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 17.6 |
| Harrison Barnes (SAS) | 96% | 16.0<br><sub>10,16,21,26,15</sub> | 5.9<br><sub>0,9,3,9,5</sub> |  | 1.8<br><sub>3,2,5,2,0</sub> |  | 0.9<br><sub>4,1,2,2,1</sub> |  | 0.7<br><sub>0,1,0,1,1</sub> |  | 0.3 | 0.1 | 0.5 | 8.7 |
| Luke Kornet (SAS) | 99% | 15.0<br><sub>14,15,10,29,13</sub> | 4.1<br><sub>2,4,0,18,4</sub> |  | 4.4<br><sub>1,0,3,11,5</sub> |  | 1.2<br><sub>1,3,0,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 9.7 |
| Jordan McLaughlin (SAS) | 88% | 14.0<br><sub>-,11,18,14,15</sub> | 4.1<br><sub>-,0,0,6,4</sub> |  | 1.8<br><sub>-,1,3,2,2</sub> |  | 2.1<br><sub>-,5,2,0,0</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.9 | 0.1 | 0.7 | 8.0 |
| Carter Bryant (SAS) | 96% | 12.4<br><sub>2,13,20,12,14</sub> | 4.5<br><sub>0,3,8,0,2</sub> |  | 2.1<br><sub>0,1,3,3,6</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>0,1,2,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.4 |
| Ja'Kobi Gillespie (SAS) | 93% | 8.1<br><sub>-,-,-,15,7</sub> | 2.8<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,2,1</sub> |  | 0.8<br><sub>-,-,-,4,0</sub> |  | 0.2<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Tarris Reed Jr. (SAS) | 52% | 7.5<br><sub>-,-,6,15,-</sub> | 2.5<br><sub>-,-,0,7,-</sub> |  | 3.1<br><sub>-,-,4,7,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.1 |
| David Jones Garcia (SAS) | 52% | 5.8<br><sub>-,-,4,2,-</sub> | 2.2<br><sub>-,-,0,2,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.1 |

</details>

<details><summary>if Dylan Harper plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 99% | 34.5<br><sub>36,42,37,36,33</sub> | 29.7<br><sub>43,36,29,25,28</sub> | 33.5 · –<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>3,6,5,4,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>9,7,7,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>5,5,2,2,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.5 | 3.9 | 43.2 |
| Austin Reaves (LAL) | 98% | 31.1<br><sub>-,-,-,-,-</sub> | 18.3<br><sub>-,-,-,-,-</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.9<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 2.6 | 25.9 |
| Walker Kessler (LAL) | 99% | 28.1<br><sub>32,-,31,30,36</sub> | 10.9<br><sub>14,-,10,15,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>12,-,11,7,12</sub> | 10.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.8 | 1.6 | 1.5 | 21.9 |
| Quentin Grimes (LAL) | 99% | 26.8<br><sub>37,42,35,35,30</sub> | 10.1<br><sub>22,47,20,13,9</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>6,6,7,5,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>1,3,4,7,8</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>5,10,4,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.3 | 15.9 |
| Jake LaRavia (LAL) | 98% | 23.2<br><sub>32,23,30,24,37</sub> | 5.7<br><sub>12,4,4,6,15</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,5,6,3,10</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>2,0,0,1,1</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.4 | 0.9 | 10.9 |
| Matisse Thybulle (LAL) | 98% | 21.1<br><sub>26,31,21,27,27</sub> | 5.7<br><sub>12,7,2,14,14</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>8,6,1,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,3,1,0</sub> |  | 0.8<br><sub>2,2,0,4,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7 | 0.7 | 0.7 | 9.0 |
| Ziaire Williams (LAL) | 98% | 18.0<br><sub>19,24,18,28,19</sub> | 6.1<br><sub>6,0,7,5,9</sub> |  | 2.0<br><sub>2,1,2,0,4</sub> |  | 1.0<br><sub>3,1,0,1,0</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.1 |
| Collin Sexton (LAL) | 99% | 17.9<br><sub>24,25,20,18,23</sub> | 9.9<br><sub>16,10,12,10,12</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,4,0,1,2</sub> |  | 2.0<br><sub>3,3,1,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>2,1,1,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.2 | 1.4 | 13.7 |
| Sandro Mamukelashvili (LAL) | 99% | 16.1<br><sub>21,23,21,20,13</sub> | 6.3<br><sub>4,3,6,9,2</sub> |  | 3.4<br><sub>2,3,3,9,4</sub> |  | 1.1<br><sub>3,2,0,2,2</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.8 |
| Jarred Vanderbilt (LAL) | 91% | 9.2<br><sub>12,14,12,10,12</sub> | 2.5<br><sub>2,4,0,4,1</sub> |  | 2.7<br><sub>4,7,5,4,2</sub> |  | 0.8<br><sub>0,0,3,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 5.9 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.0 |
| Kevon Looney (LAL) | 36% | 6.7<br><sub>-,17,-,-,-</sub> | 1.4<br><sub>-,4,-,-,-</sub> |  | 2.3<br><sub>-,8,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.2 |
| Cameron Carr (LAL) | 80% | 6.3<br><sub>-,-,2,12,10</sub> | 3.0<br><sub>-,-,5,5,9</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.3<br><sub>-,-,1,1,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Carson Cooper (LAL) | 52% | 6.1<br><sub>-,18,2,-,-</sub> | 1.9<br><sub>-,3,2,-,-</sub> |  | 1.7<br><sub>-,4,1,-,-</sub> |  | 0.4<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |
| Jaden Hardy (LAL) | 43% | 5.9<br><sub>-,-,2,-,-</sub> | 3.5<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.5 |
| Adou Thiero (LAL) | 52% | 5.8<br><sub>-,6,6,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Bronny James (LAL) | 47% | 5.2<br><sub>-,-,2,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.7 |
| Chris Manon (LAL) | 52% | 5.2<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.9 |
| Devin Vassell (SAS) | 99% | 31.4<br><sub>36,32,26,34,38</sub> | 13.2<br><sub>12,15,10,16,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,4,3,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>4,4,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,1,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.4 | 1.1 | 20.1 |
| Victor Wembanyama (SAS) | 99% | 31.3<br><sub>34,33,32,-,35</sub> | 27.9<br><sub>25,32,50,-,44</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.0<br><sub>18,11,19,-,16</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>4,3,1,-,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,2,5,-,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2 | 3.2 | 2.7 | 43.3 |
| Stephon Castle (SAS) | 99% | 30.7<br><sub>31,33,29,37,34</sub> | 17.2<br><sub>10,21,19,28,20</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>2,6,3,8,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>7,12,6,11,9</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,2,5,4,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 3.1 | 29.5 |
| Dylan Harper (SAS) | 100% | 29.1<br><sub>35,-,-,-,-</sub> | 16.1<br><sub>20,-,-,-,-</sub> | 14.5 · – | 4.8<br><sub>4,-,-,-,-</sub> | 4.5 | 4.5<br><sub>2,-,-,-,-</sub> | 3.5 | 1.2<br><sub>0,-,-,-,-</sub> | 0.5 | 1.0 | 0.3 | 1.9 | 25.4 |
| Julian Champagnie (SAS) | 99% | 28.2<br><sub>30,29,25,30,37</sub> | 11.2<br><sub>14,20,9,22,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>6,4,3,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>4,4,3,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.4 | 0.9 | 17.4 |
| Keldon Johnson (SAS) | 99% | 24.6<br><sub>15,27,23,26,33</sub> | 9.7<br><sub>4,10,10,12,3</sub> |  | 5.2<br><sub>2,5,4,4,12</sub> |  | 2.1<br><sub>1,3,4,5,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 17.0 |
| Harrison Barnes (SAS) | 96% | 16.1<br><sub>10,16,21,26,15</sub> | 5.8<br><sub>0,9,3,9,5</sub> |  | 1.8<br><sub>3,2,5,2,0</sub> |  | 1.0<br><sub>4,1,2,2,1</sub> |  | 0.7<br><sub>0,1,0,1,1</sub> |  | 0.3 | 0.1 | 0.6 | 8.6 |
| Luke Kornet (SAS) | 99% | 14.8<br><sub>14,15,10,29,13</sub> | 3.9<br><sub>2,4,0,18,4</sub> |  | 4.4<br><sub>1,0,3,11,5</sub> |  | 1.2<br><sub>1,3,0,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 9.5 |
| Jordan McLaughlin (SAS) | 88% | 13.8<br><sub>-,11,18,14,15</sub> | 4.0<br><sub>-,0,0,6,4</sub> |  | 1.9<br><sub>-,1,3,2,2</sub> |  | 2.1<br><sub>-,5,2,0,0</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.9 | 0.1 | 0.7 | 8.0 |
| Carter Bryant (SAS) | 96% | 12.3<br><sub>2,13,20,12,14</sub> | 4.5<br><sub>0,3,8,0,2</sub> |  | 2.0<br><sub>0,1,3,3,6</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>0,1,2,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.3 |
| Ja'Kobi Gillespie (SAS) | 93% | 8.1<br><sub>-,-,-,15,7</sub> | 2.9<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,2,1</sub> |  | 0.8<br><sub>-,-,-,4,0</sub> |  | 0.3<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Tarris Reed Jr. (SAS) | 52% | 7.4<br><sub>-,-,6,15,-</sub> | 2.4<br><sub>-,-,0,7,-</sub> |  | 3.1<br><sub>-,-,4,7,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.0 |
| David Jones Garcia (SAS) | 52% | 5.9<br><sub>-,-,4,2,-</sub> | 2.3<br><sub>-,-,0,2,-</sub> |  | 1.0<br><sub>-,-,1,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

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
| Nikola Jokic | 99% | 36.4<br><sub>38,39,38,42,33</sub> | 27.9<br><sub>28,24,26,37,18</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.1 | 49.9 |
| Jamal Murray | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 26.0<br><sub>28,21,14,45,20</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 2.2 | 36.5 |
| Christian Braun | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.9<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.5 |
| Cameron Johnson | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.3<br><sub>9,8,19,16,17</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.0 | 20.9 |
| Aaron Gordon | 99% | 29.3<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan | 96% | 19.5<br><sub>14,25,22,18,17</sub> | 10.4<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.5<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
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
| Keyonte George | 99% | 34.8<br><sub>35,39,36,26,33</sub> | 22.9<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 34.1 |
| Ace Bailey | 99% | 33.7<br><sub>23,27,24,33,33</sub> | 17.0<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.2<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.8 | 1.8 | 25.5 |
| Darryn Peterson | 99% | 33.0<br><sub>31,19,32,25,29</sub> | 17.8<br><sub>13,11,20,6,13</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.5 | 2.0 | 27.6 |
| Svi Mykhailiuk | 98% | 27.7<br><sub>33,34,28,32,25</sub> | 11.8<br><sub>8,15,11,39,4</sub> |  | 3.5<br><sub>7,3,7,5,3</sub> |  | 2.5<br><sub>5,5,2,3,2</sub> |  | 2.1<br><sub>2,4,3,10,0</sub> |  | 0.7 | 0.1 | 1.1 | 17.7 |
| Josh Green | 98% | 24.9<br><sub>13,28,29,23,19</sub> | 6.1<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.9<br><sub>1,2,2,0,2</sub> |  | 0.8 | 0.3 | 0.7 | 10.1 |
| Brice Sensabaugh | 99% | 24.0<br><sub>35,14,26,17,17</sub> | 15.4<br><sub>40,8,18,10,6</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>11,3,3,3,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>5,2,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>8,0,5,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 1.6 | 21.6 |
| Josh Okogie | 98% | 21.4<br><sub>22,15,17,14,9</sub> | 6.3<br><sub>9,3,3,1,0</sub> |  | 3.4<br><sub>2,0,2,4,0</sub> |  | 1.2<br><sub>4,0,2,0,0</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 1.0 | 0.3 | 0.8 | 10.9 |
| Isaiah Collier | 67% | 20.0<br><sub>-,10,-,13,18</sub> | 9.7<br><sub>-,0,-,10,4</sub> |  | 2.8<br><sub>-,1,-,2,2</sub> |  | 5.1<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.8 | 0.2 | 1.5 | 17.6 |
| Kyle Filipowski | 64% | 19.9<br><sub>-,6,-,9,24</sub> | 11.3<br><sub>-,0,-,2,21</sub> |  | 6.5<br><sub>-,3,-,4,12</sub> |  | 2.4<br><sub>-,0,-,3,4</sub> |  | 0.9<br><sub>-,0,-,0,1</sub> |  | 0.8 | 0.4 | 1.2 | 20.2 |
| Tony Bradley | 52% | 14.7<br><sub>17,-,-,13,-</sub> | 4.3<br><sub>3,-,-,1,-</sub> |  | 4.6<br><sub>7,-,-,5,-</sub> |  | 0.7<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.6 | 9.6 |

</details>

<details><summary>if Mo Bamba plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.8<br><sub>28,24,26,37,18</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 1.0 | 3.2 | 49.9 |
| Jamal Murray (DEN) | 99% | 36.4<br><sub>35,38,36,45,36</sub> | 25.9<br><sub>28,21,14,45,20</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 2.2 | 36.5 |
| Christian Braun (DEN) | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.8<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.5 |
| Cameron Johnson (DEN) | 98% | 30.4<br><sub>27,26,29,36,34</sub> | 14.3<br><sub>9,8,19,16,17</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.0 | 20.9 |
| Aaron Gordon (DEN) | 99% | 29.2<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan (DEN) | 96% | 19.4<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones (DEN) | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile (DEN) | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.5 |
| Marvin Bagley III (DEN) | 99% | 12.0<br><sub>10,9,10,11,12</sub> | 6.1<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.4 |
| Tyus Jones (DEN) | 98% | 10.8<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.8<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.6 |
| Julian Strawther (DEN) | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 4.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Zeke Nnaji (DEN) | 38% | 6.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.3 |
| Alpha Diallo (DEN) | 48% | 6.2<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Ryan Nembhard (DEN) | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Keyonte George (UTA) | 99% | 34.6<br><sub>35,39,36,26,33</sub> | 21.3<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 32.4 |
| Ace Bailey (UTA) | 99% | 32.9<br><sub>23,27,24,33,33</sub> | 16.2<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.0<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.9 | 1.7 | 24.4 |
| Darryn Peterson (UTA) | 99% | 32.0<br><sub>31,19,32,25,29</sub> | 16.8<br><sub>13,11,20,6,13</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.5 | 2.0 | 26.3 |
| Mo Bamba (UTA) | 100% | 25.7<br><sub>31,23,20,23,29</sub> | 8.9<br><sub>15,6,2,6,6</sub> |  | 8.7<br><sub>10,16,2,10,7</sub> |  | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.6 | 1.5 | 1.1 | 19.0 |
| Svi Mykhailiuk (UTA) | 98% | 25.5<br><sub>33,34,28,32,25</sub> | 11.4<br><sub>8,15,11,39,4</sub> |  | 3.1<br><sub>7,3,7,5,3</sub> |  | 2.2<br><sub>5,5,2,3,2</sub> |  | 1.9<br><sub>2,4,3,10,0</sub> |  | 0.6 | 0.1 | 1.0 | 16.7 |
| Josh Green (UTA) | 98% | 23.3<br><sub>13,28,29,23,19</sub> | 5.8<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>1,2,2,0,2</sub> |  | 0.7 | 0.3 | 0.6 | 9.4 |
| Brice Sensabaugh (UTA) | 99% | 22.1<br><sub>35,14,26,17,17</sub> | 14.0<br><sub>40,8,18,10,6</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>11,3,3,3,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>5,2,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>8,0,5,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.2 | 1.6 | 19.8 |
| Josh Okogie (UTA) | 98% | 18.2<br><sub>22,15,17,14,9</sub> | 5.4<br><sub>9,3,3,1,0</sub> |  | 2.8<br><sub>2,0,2,4,0</sub> |  | 1.0<br><sub>4,0,2,0,0</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.2 | 0.7 | 9.2 |
| Isaiah Collier (UTA) | 67% | 17.5<br><sub>-,10,-,13,18</sub> | 8.4<br><sub>-,0,-,10,4</sub> |  | 2.4<br><sub>-,1,-,2,2</sub> |  | 4.6<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.7 | 0.2 | 1.4 | 15.3 |
| Kyle Filipowski (UTA) | 64% | 17.5<br><sub>-,6,-,9,24</sub> | 9.7<br><sub>-,0,-,2,21</sub> |  | 5.8<br><sub>-,3,-,4,12</sub> |  | 2.1<br><sub>-,0,-,3,4</sub> |  | 0.7<br><sub>-,0,-,0,1</sub> |  | 0.7 | 0.3 | 1.2 | 17.6 |
| Tony Bradley (UTA) | 52% | 11.6<br><sub>17,-,-,13,-</sub> | 3.4<br><sub>3,-,-,1,-</sub> |  | 3.5<br><sub>7,-,-,5,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 7.5 |

</details>

<details><summary>if Jaxson Hayes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.9<br><sub>28,24,26,37,18</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.2 | 50.0 |
| Jamal Murray (DEN) | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 25.9<br><sub>28,21,14,45,20</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.8 | 2.2 | 36.4 |
| Christian Braun (DEN) | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.8<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.4 |
| Cameron Johnson (DEN) | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.2<br><sub>9,8,19,16,17</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.0 | 20.8 |
| Aaron Gordon (DEN) | 99% | 29.3<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan (DEN) | 96% | 19.4<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.4<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones (DEN) | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile (DEN) | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.6<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.6 |
| Marvin Bagley III (DEN) | 99% | 12.2<br><sub>10,9,10,11,12</sub> | 6.2<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.5 |
| Tyus Jones (DEN) | 98% | 10.8<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Julian Strawther (DEN) | 38% | 9.2<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.4 |
| Zeke Nnaji (DEN) | 38% | 7.0<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.3 |
| Ryan Nembhard (DEN) | 38% | 6.2<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Alpha Diallo (DEN) | 48% | 6.1<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Keyonte George (UTA) | 99% | 34.8<br><sub>35,39,36,26,33</sub> | 21.3<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 32.4 |
| Ace Bailey (UTA) | 99% | 33.1<br><sub>23,27,24,33,33</sub> | 16.4<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.0<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.9 | 1.7 | 24.6 |
| Darryn Peterson (UTA) | 99% | 32.4<br><sub>31,19,32,25,29</sub> | 17.0<br><sub>13,11,20,6,13</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.6 | 2.0 | 26.6 |
| Svi Mykhailiuk (UTA) | 98% | 25.7<br><sub>33,34,28,32,25</sub> | 11.5<br><sub>8,15,11,39,4</sub> |  | 3.1<br><sub>7,3,7,5,3</sub> |  | 2.2<br><sub>5,5,2,3,2</sub> |  | 1.9<br><sub>2,4,3,10,0</sub> |  | 0.6 | 0.1 | 1.0 | 16.8 |
| Josh Green (UTA) | 98% | 22.9<br><sub>13,28,29,23,19</sub> | 5.7<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>1,2,2,0,2</sub> |  | 0.7 | 0.2 | 0.6 | 9.2 |
| Jaxson Hayes (UTA) | 100% | 22.2<br><sub>-,25,28,12,-</sub> | 9.2<br><sub>-,6,18,8,-</sub> | 8.5 · – | 5.9<br><sub>-,7,14,3,-</sub> | 5.5 | 1.3<br><sub>-,2,0,1,-</sub> | 1.5 | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.9 | 0.9 | 16.4 |
| Brice Sensabaugh (UTA) | 99% | 21.6<br><sub>35,14,26,17,17</sub> | 13.8<br><sub>40,8,18,10,6</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>11,3,3,3,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>5,2,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>8,0,5,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.2 | 1.6 | 19.5 |
| Isaiah Collier (UTA) | 67% | 17.8<br><sub>-,10,-,13,18</sub> | 8.4<br><sub>-,0,-,10,4</sub> |  | 2.4<br><sub>-,1,-,2,2</sub> |  | 4.7<br><sub>-,2,-,7,1</sub> |  | 0.4<br><sub>-,0,-,1,0</sub> |  | 0.7 | 0.2 | 1.4 | 15.5 |
| Josh Okogie (UTA) | 98% | 17.7<br><sub>22,15,17,14,9</sub> | 5.2<br><sub>9,3,3,1,0</sub> |  | 2.7<br><sub>2,0,2,4,0</sub> |  | 1.0<br><sub>4,0,2,0,0</sub> |  | 0.5<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.2 | 0.6 | 8.9 |
| Kyle Filipowski (UTA) | 64% | 16.9<br><sub>-,6,-,9,24</sub> | 9.4<br><sub>-,0,-,2,21</sub> |  | 5.6<br><sub>-,3,-,4,12</sub> |  | 2.0<br><sub>-,0,-,3,4</sub> |  | 0.7<br><sub>-,0,-,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 17.0 |
| Tony Bradley (UTA) | 52% | 12.1<br><sub>17,-,-,13,-</sub> | 3.4<br><sub>3,-,-,1,-</sub> |  | 3.7<br><sub>7,-,-,5,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 7.8 |

</details>

<details><summary>if Jusuf Nurkic plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 99% | 36.5<br><sub>38,39,38,42,33</sub> | 27.9<br><sub>28,24,26,37,18</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 12.2<br><sub>15,8,7,18,11</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 9.8<br><sub>7,9,11,11,5</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.2 | 49.9 |
| Jamal Murray (DEN) | 99% | 36.3<br><sub>35,38,36,45,36</sub> | 26.1<br><sub>28,21,14,45,20</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,7,2,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.1<br><sub>4,2,7,7,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>1,2,1,6,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 2.2 | 36.6 |
| Christian Braun (DEN) | 99% | 32.4<br><sub>33,35,31,38,29</sub> | 13.9<br><sub>10,15,19,21,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,5,5,8,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,1,3,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.5 | 1.0 | 21.5 |
| Cameron Johnson (DEN) | 98% | 30.5<br><sub>27,26,29,36,34</sub> | 14.2<br><sub>9,8,19,16,17</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>0,5,3,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,1,6,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,0,2,4,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.0 | 20.9 |
| Aaron Gordon (DEN) | 99% | 29.2<br><sub>24,31,31,33,24</sub> | 13.4<br><sub>11,13,18,18,1</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>1,8,3,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,2,5,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.5 | 1.1 | 21.4 |
| DeMar DeRozan (DEN) | 96% | 19.4<br><sub>14,25,22,18,17</sub> | 10.3<br><sub>2,18,15,4,9</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,0,5</sub> |  | 2.5<br><sub>1,2,2,1,1</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones (DEN) | 91% | 17.0<br><sub>21,17,18,20,22</sub> | 4.3<br><sub>4,2,3,0,7</sub> | 3.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,2,1,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 7.8 |
| Trevon Brazile (DEN) | 98% | 13.8<br><sub>23,11,11,15,12</sub> | 4.3<br><sub>9,0,4,8,0</sub> |  | 3.7<br><sub>4,6,4,0,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.4 | 0.5 | 8.6 |
| Marvin Bagley III (DEN) | 99% | 12.1<br><sub>10,9,10,11,12</sub> | 6.2<br><sub>4,4,10,2,9</sub> |  | 3.7<br><sub>2,3,6,2,3</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.5 | 10.5 |
| Tyus Jones (DEN) | 98% | 10.8<br><sub>10,9,14,8,12</sub> | 2.8<br><sub>0,0,5,0,2</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Julian Strawther (DEN) | 38% | 9.1<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Zeke Nnaji (DEN) | 38% | 6.9<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.3 | 4.4 |
| Alpha Diallo (DEN) | 48% | 6.1<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Ryan Nembhard (DEN) | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Keyonte George (UTA) | 99% | 34.9<br><sub>35,39,36,26,33</sub> | 22.0<br><sub>30,30,14,15,14</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>2,1,3,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>11,10,6,7,2</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>4,5,0,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 2.9 | 33.3 |
| Ace Bailey (UTA) | 99% | 33.7<br><sub>23,27,24,33,33</sub> | 16.4<br><sub>5,19,7,16,18</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>1,8,7,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,3,1,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.2<br><sub>1,2,0,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.8 | 1.8 | 25.0 |
| Darryn Peterson (UTA) | 99% | 33.0<br><sub>31,19,32,25,29</sub> | 17.1<br><sub>13,11,20,6,13</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>5,1,10,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,3,8,5,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,1,0,0,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.5 | 2.0 | 26.8 |
| Svi Mykhailiuk (UTA) | 98% | 27.6<br><sub>33,34,28,32,25</sub> | 11.2<br><sub>8,15,11,39,4</sub> |  | 3.5<br><sub>7,3,7,5,3</sub> |  | 2.5<br><sub>5,5,2,3,2</sub> |  | 2.0<br><sub>2,4,3,10,0</sub> |  | 0.7 | 0.1 | 1.1 | 17.1 |
| Josh Green (UTA) | 98% | 24.9<br><sub>13,28,29,23,19</sub> | 5.9<br><sub>9,11,8,0,8</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>1,2,4,1,2</sub> |  | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.9<br><sub>1,2,2,0,2</sub> |  | 0.8 | 0.2 | 0.7 | 9.8 |
| Brice Sensabaugh (UTA) | 99% | 24.0<br><sub>35,14,26,17,17</sub> | 14.8<br><sub>40,8,18,10,6</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>11,3,3,3,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>5,2,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>8,0,5,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 1.6 | 21.0 |
| Josh Okogie (UTA) | 98% | 21.4<br><sub>22,15,17,14,9</sub> | 6.1<br><sub>9,3,3,1,0</sub> |  | 3.4<br><sub>2,0,2,4,0</sub> |  | 1.2<br><sub>4,0,2,0,0</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 1.0 | 0.3 | 0.8 | 10.7 |
| Jusuf Nurkic (UTA) | 100% | 21.3 | 9.5 | 7.5 · – | 8.3 | 6.5 | 4.1 | 3.5 | 0.5 |  | 1.0 | 0.5 | 1.6 | 21.9 |
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
| Saddiq Bey | 99% | 32.3<br><sub>33,42,37,32,40</sub> | 15.9<br><sub>23,10,21,2,21</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>6,8,6,5,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,6,3,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>5,2,4,0,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 1.0 | 23.7 |
| Jeremiah Fears | 99% | 32.0<br><sub>29,31,38,34,40</sub> | 17.7<br><sub>19,16,22,29,7</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>10,5,7,5,7</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 6.2<br><sub>10,4,5,4,11</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 3.1 | 28.7 |
| Trey Murphy III | 98% | 32.0<br><sub>-,-,29,-,35</sub> | 16.2<br><sub>-,-,17,-,9</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>-,-,4,-,9</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>-,-,1,-,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>-,-,3,-,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.3 | 1.5 | 24.6 |
| Zion Williamson | 84% | 31.8<br><sub>25,32,37,-,40</sub> | 20.4<br><sub>16,24,22,-,25</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>6,7,6,-,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,1,7,-,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.2<br><sub>0,0,0,-,0</sub> |  | 1.4 | 0.5 | 2.3 | 29.6 |
| Jordan Poole | 91% | 23.3<br><sub>31,30,13,31,27</sub> | 12.4<br><sub>11,22,6,25,28</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>2,1,0,3,0</sub> |  | 3.3<br><sub>5,5,1,2,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,3,2,3,6</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 1.7 | 17.7 |
| Herbert Jones | 99% | 23.1<br><sub>24,32,33,25,21</sub> | 7.1<br><sub>8,9,14,2,7</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>3,3,3,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9<br><sub>2,3,4,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.4 | 1.2 | 11.9 |
| Derik Queen | 99% | 22.1<br><sub>21,19,18,35,21</sub> | 11.1<br><sub>17,9,11,15,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>10,5,7,15,9</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,0,3,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.4<br><sub>4,0,0,0,0</sub> | 0.5<br><sub>o 32% · u 68%</sub> | 1.0 | 0.6 | 2.1 | 20.2 |
| Yves Missi | 98% | 19.3<br><sub>23,17,23,35,22</sub> | 5.7<br><sub>6,4,4,9,4</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>14,5,7,13,8</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,2,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.9 | 13.0 |
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
| Brandon Ingram | 97% | 26.2<br><sub>-,-,-,27,26</sub> | 16.4<br><sub>-,-,-,16,18</sub> | 18.5 · –<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>-,-,-,7,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>-,-,-,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.6 | 2.0 | 24.4 |
| Derrick Jones Jr. | 99% | 24.7<br><sub>28,27,26,23,23</sub> | 9.0<br><sub>5,8,4,7,4</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>1,2,7,4,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,1,1,3,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.9 | 1.0 | 0.8 | 14.2 |
| Max Strus | 98% | 22.5<br><sub>21,32,29,26,21</sub> | 8.2<br><sub>3,18,5,8,0</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>2,5,6,0,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,4,3,2,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>1,5,1,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 0.9 | 14.4 |
| Brook Lopez | 99% | 21.9<br><sub>23,27,25,21,18</sub> | 11.8<br><sub>23,23,21,3,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,3,6,4,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,4,0,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>4,5,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 1.2 | 1.0 | 18.0 |
| Kris Dunn | 99% | 21.8<br><sub>26,20,19,23,22</sub> | 6.5<br><sub>2,6,3,9,12</sub> | 4.5 · –<br><sub>o 57% · u 43%</sub> | 3.3<br><sub>5,2,4,5,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.6<br><sub>5,2,5,4,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.7<br><sub>0,1,1,0,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.3 | 1.0 | 13.4 |
| Keaton Wagler | 98% | 19.6<br><sub>18,17,19,17,21</sub> | 10.0<br><sub>15,7,7,2,12</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,5,7,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>0,2,3,2,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2<br><sub>1,1,1,0,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.7 | 0.1 | 1.5 | 15.5 |
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
| Sidy Cissoko AST over 2.5 (3+) | GSW @ POR | draftkings | 2.43 | 2.43 | 1.87 | 53.4% | 38.5% | 41.2% | +0.2% | +29.7% | 0.0% |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 99% | 32.6<br><sub>33,30,33,34,31</sub> | 19.7<br><sub>28,13,11,12,15</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>8,5,8,8,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>3,4,7,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.7 | 2.9 | 30.1 |
| Brandin Podziemski | 98% | 32.6<br><sub>30,29,32,38,32</sub> | 15.8<br><sub>15,10,15,18,13</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>6,3,3,7,2</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>3,4,2,2,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,0,0,4,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.3 | 1.8 | 24.0 |
| Draymond Green | 97% | 25.7<br><sub>25,23,-,27,26</sub> | 6.2<br><sub>2,3,-,9,6</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>8,1,-,6,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,2,-,3,11</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>0,1,-,3,2</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.6 | 2.1 | 16.1 |
| De'Anthony Melton | 99% | 24.0<br><sub>21,19,25,27,27</sub> | 10.4<br><sub>8,0,9,2,24</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>2,2,1,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>1,2,5,7,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>2,0,1,0,8</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.5 | 0.5 | 1.9 | 16.7 |
| Gui Santos | 96% | 20.3<br><sub>19,17,23,23,24</sub> | 8.6<br><sub>12,6,8,13,22</sub> | 9.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>7,6,3,5,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,6,0,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8<br><sub>1,0,0,3,2</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.4 | 14.4 |
| Will Richard | 99% | 19.1<br><sub>23,27,27,17,17</sub> | 6.1<br><sub>11,20,15,3,3</sub> |  | 2.2<br><sub>3,0,5,2,2</sub> |  | 1.1<br><sub>1,3,0,2,1</sub> |  | 0.7<br><sub>2,1,1,1,1</sub> |  | 1.0 | 0.2 | 0.8 | 9.4 |
| Charles Bassey | 98% | 18.6<br><sub>16,22,25,26,22</sub> | 9.5<br><sub>4,10,16,13,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>0,8,13,9,7</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 0.9<br><sub>0,0,1,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.0 | 1.3 | 17.2 |
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
| Deni Avdija | 80% | 34.8<br><sub>-,-,36,30,36</sub> | 27.4<br><sub>-,-,20,31,33</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>-,-,9,3,12</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>-,-,5,7,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>-,-,2,5,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.5 | 4.1 | 42.0 |
| Jrue Holiday | 99% | 33.4<br><sub>31,31,31,28,32</sub> | 18.1<br><sub>23,22,13,18,11</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>5,2,9,2,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>6,7,7,5,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>5,2,1,4,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.2 | 3.1 | 29.8 |
| Toumani Camara | 99% | 33.3<br><sub>33,37,35,29,31</sub> | 13.4<br><sub>10,18,6,5,8</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>8,6,5,5,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>1,4,0,3,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>2,4,1,1,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.5 | 1.9 | 20.4 |
| Sidy Cissoko | 98% | 30.2<br><sub>32,31,23,24,30</sub> | 10.6<br><sub>6,13,11,5,16</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>5,5,2,4,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,3,1,0,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>2,1,3,1,4</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.5 | 1.6 | 17.3 |
| Scoot Henderson | 99% | 28.5<br><sub>21,35,23,26,23</sub> | 15.5<br><sub>9,27,3,17,10</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,7,1,3,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>1,3,1,3,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>0,5,0,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 2.9 | 21.8 |
| Donovan Clingan | 99% | 27.6<br><sub>32,26,31,29,21</sub> | 12.9<br><sub>12,7,22,15,5</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 11.8<br><sub>12,13,13,18,8</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>5,2,4,5,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0<br><sub>0,0,3,1,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.7 | 1.8 | 1.5 | 27.5 |
| Robert Williams III | 99% | 20.2<br><sub>16,-,17,16,21</sub> | 7.3<br><sub>6,-,4,6,4</sub> |  | 7.6<br><sub>8,-,3,6,3</sub> |  | 1.5<br><sub>4,-,0,1,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.7 | 1.3 | 1.0 | 16.4 |
| Jayson Kent | 88% | 15.9<br><sub>27,17,3,14,6</sub> | 5.5<br><sub>8,2,0,9,0</sub> |  | 2.1<br><sub>3,1,1,2,3</sub> |  | 0.8<br><sub>0,2,0,1,0</sub> |  | 0.7<br><sub>2,0,0,3,0</sub> |  | 0.7 | 0.1 | 0.8 | 8.4 |
| Branden Carlson | 71% | 11.2<br><sub>14,10,9,6,-</sub> | 3.1<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>1,1,1,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.5 | 0.6 | 6.3 |
| Yang Hansen | 64% | 10.2<br><sub>-,12,-,3,5</sub> | 3.5<br><sub>-,2,-,2,0</sub> |  | 2.6<br><sub>-,1,-,0,2</sub> |  | 0.8<br><sub>-,1,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.3 | 0.8 | 6.9 |
| Micah Potter | 52% | 8.7<br><sub>1,-,-,3,-</sub> | 3.9<br><sub>0,-,-,0,-</sub> |  | 2.4<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| John Tonje | 52% | 8.2<br><sub>-,6,-,3,-</sub> | 2.8<br><sub>-,0,-,2,-</sub> |  | 1.8<br><sub>-,3,-,0,-</sub> |  | 0.9<br><sub>-,0,-,1,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-27/`._
