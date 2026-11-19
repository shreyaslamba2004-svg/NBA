# NBA model · Thu 19 Nov 2026 (US date)

Updated **Fri 20 Nov, 05:03 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-19/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

2 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| POR @ MIL | player points | Jrue Holiday projected 20.5 pts vs DraftKings line 13.5 | minutes 33 vs 26 this season; scoring 0.63/min vs 0.50 this season, 0.56 last season; teammates out: Krejci, Morant, Sharpe, III (~95 min a game) |
| POR @ MIL | player points | Scoot Henderson projected 17.2 pts vs DraftKings line 11.5 | minutes 29 vs 22 this season; scoring 0.59/min vs 0.39 this season, 0.57 last season; teammates out: Krejci, Morant, Sharpe, III (~95 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama PTS over 49.5 (50+) | LAC @ SAS | draftkings | 31.00 | 26.74 | 12.95 | 7.7% | 3.0% | 3.7% | +15.9% | +139.4% | 0.1% |
| Jalen Brunson PRA over 54.5 (55+) | NYK @ MIN | draftkings | 22.00 | 20.53 | 12.08 | 8.3% | 4.2% | 4.9% | +7.1% | +82.1% | 0.1% |
| Devin Vassell AST over 5.5 (6+) | LAC @ SAS | draftkings | 13.00 | 12.24 | 7.36 | 13.6% | 7.2% | 8.2% | +6.3% | +76.7% | 0.1% |
| Jalen Brunson PRA over 49.5 (50+) | NYK @ MIN | draftkings | 12.00 | 11.33 | 6.87 | 14.5% | 7.8% | 8.8% | +5.9% | +74.6% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| GSW @ MEM | Fri 20 Nov 12:00 | 114.7–117.9 | GSW 41% | 2.44 / 1.69 | MEM -3.5 | 232.5 | MEM -6.5 covers 41%; o225.5 65% |
| POR @ MIL | Fri 20 Nov 12:00 | 116.9–110.2 | POR 68% | 1.46 / 3.17 | MIL +6.5 | 226.5 | MIL +10.5 covers 61%; o229.5 44% |
| NYK @ MIN | Fri 20 Nov 12:00 | 113.4–108.8 | NYK 63% | 1.59 / 2.68 | MIN +4.5 | 221.5 | MIN +1.5 covers 40%; o215.5 63% |
| LAC @ SAS | Fri 20 Nov 12:00 | 107.4–118.1 | LAC 22% | 4.48 / 1.29 | SAS -10.5 | 225.5 | SAS -15.5 covers 37%; o224.5 52% |

### GSW @ MEM
Out: GG Jackson (MEM), Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.7–117.9 | GSW 41% | 2.44 / 1.69 | MEM -3.5 | 232.5 | MEM -6.5 covers 41%; o225.5 65% |
| Expected (weighted by chance each plays) | 115.9–118.5 | GSW 42% | 2.36 / 1.74 | MEM -3.5 | 234.5 | MEM -6.5 covers 40%; o225.5 68% |
| if Draymond Green plays | 114.9–117.9 | GSW 42% | 2.39 / 1.72 | MEM -3.5 | 232.5 | MEM -6.5 covers 41%; o225.5 65% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Draymond Green (GSW) | Day-To-Day | 70% | 26.9 | 6.2 | 5.3 | 6.0 | 0.7 | 1.0 | 0.9 | 2.4 | 17.4 | full tables below |
| Al Horford (GSW) | Day-To-Day | 70% | 18.4 | 6.0 | 4.3 | 2.2 | 0.8 | 0.5 | 1.0 | 0.6 | 12.5 | small |
| Isaiah Stewart (MEM) | Day-To-Day | 70% | 13.8 | 6.8 | 3.0 | 0.8 | 0.4 | 0.2 | 0.7 | 0.8 | 10.5 | small |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 33.6<br><sub>27,36,24,33,30</sub> | 21.7<br><sub>23,25,3,28,13</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>7,10,7,8,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.2<br><sub>4,0,1,3,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>4,2,0,2,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.8 | 3.3 | 33.2 |
| Brandin Podziemski | 96% | 32.7<br><sub>26,37,22,30,29</sub> | 18.5<br><sub>25,22,8,15,10</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>2,6,3,6,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 5.0<br><sub>4,4,0,3,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>5,4,2,3,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 1.9 | 28.9 |
| Will Richard | 98% | 28.6<br><sub>-,19,30,23,27</sub> | 9.4<br><sub>-,9,7,11,20</sub> |  | 3.4<br><sub>-,4,4,3,0</sub> |  | 2.1<br><sub>-,0,1,1,3</sub> |  | 1.2<br><sub>-,2,1,2,1</sub> |  | 1.5 | 0.3 | 1.2 | 14.8 |
| De'Anthony Melton | 99% | 26.2<br><sub>26,25,18,21,19</sub> | 13.2<br><sub>16,11,8,8,0</sub> |  | 4.3<br><sub>4,4,4,2,2</sub> |  | 3.2<br><sub>3,4,3,1,2</sub> |  | 2.0<br><sub>4,3,2,2,0</sub> |  | 1.7 | 0.5 | 1.8 | 20.7 |
| LJ Cryer | 88% | 23.6<br><sub>20,18,24,24,19</sub> | 10.9<br><sub>10,13,20,7,9</sub> |  | 2.1<br><sub>0,1,2,1,0</sub> |  | 2.6<br><sub>3,1,6,3,2</sub> |  | 2.0<br><sub>2,3,6,1,3</sub> |  | 0.7 | 0.1 | 1.1 | 15.6 |
| Georges Niang | 98% | 23.1<br><sub>19,19,15,14,14</sub> | 10.5<br><sub>9,5,5,0,11</sub> |  | 3.5<br><sub>2,5,3,4,1</sub> |  | 1.8<br><sub>2,0,2,2,1</sub> |  | 1.6<br><sub>1,1,1,0,2</sub> |  | 0.5 | 0.2 | 1.1 | 15.8 |
| Gui Santos | 93% | 22.9<br><sub>21,12,21,19,17</sub> | 9.7<br><sub>3,0,7,12,6</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>7,3,4,7,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>4,1,1,2,6</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9<br><sub>0,0,1,1,0</sub> |  | 0.9 | 0.4 | 1.5 | 17.2 |
| Charles Bassey | 98% | 21.8<br><sub>18,13,20,16,22</sub> | 10.4<br><sub>12,7,11,4,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 8.3<br><sub>10,6,5,0,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>1,0,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.6 | 1.5 | 19.8 |
| Gary Payton II | 88% | 19.4<br><sub>-,-,13,8,16</sub> | 8.5<br><sub>-,-,2,2,8</sub> |  | 3.6<br><sub>-,-,2,0,8</sub> |  | 1.6<br><sub>-,-,0,0,2</sub> |  | 0.6<br><sub>-,-,0,0,2</sub> |  | 1.1 | 0.3 | 0.9 | 13.7 |
| Graham Ike | 93% | 17.0<br><sub>12,4,13,8,15</sub> | 6.6<br><sub>4,4,5,3,2</sub> |  | 4.2<br><sub>5,0,2,5,2</sub> |  | 1.9<br><sub>2,1,3,1,2</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.9 | 0.9 | 12.7 |
| Malevy Leons | 76% | 13.9<br><sub>12,4,14,6,7</sub> | 4.0<br><sub>0,0,5,2,2</sub> |  | 2.5<br><sub>3,3,1,1,1</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.5 | 0.6 | 7.3 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 32.2<br><sub>33,25,29,29,28</sub> | 18.1<br><sub>13,12,15,29,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>11,10,8,7,8</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>5,3,5,7,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,1,0,7,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.7 | 2.9 | 32.9 |
| Cedric Coward | 98% | 31.1<br><sub>27,30,33,27,33</sub> | 16.6<br><sub>15,14,23,18,20</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>11,7,12,8,3</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,6,4,6,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,0,4,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.5 | 2.0 | 28.2 |
| Jaylen Wells | 99% | 28.5<br><sub>31,27,25,27,26</sub> | 12.5<br><sub>22,11,5,8,5</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>2,2,2,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>5,2,1,2,1</sub> |  | 0.8 | 0.1 | 1.0 | 17.4 |
| Cam Spencer | 98% | 28.3<br><sub>20,24,34,32,29</sub> | 13.6<br><sub>15,14,17,12,26</sub> |  | 3.2<br><sub>3,2,1,6,1</sub> |  | 7.0<br><sub>3,5,8,9,7</sub> |  | 2.0<br><sub>3,3,3,1,5</sub> |  | 0.9 | 0.2 | 1.8 | 23.8 |
| Javon Small | 98% | 25.8<br><sub>15,15,30,29,21</sub> | 12.0<br><sub>3,10,19,12,2</sub> |  | 3.6<br><sub>1,2,2,5,4</sub> |  | 4.9<br><sub>4,5,5,12,5</sub> |  | 1.6<br><sub>1,2,3,0,0</sub> |  | 0.9 | 0.2 | 1.7 | 20.5 |
| Jerami Grant | 98% | 24.3<br><sub>20,26,-,23,20</sub> | 12.4<br><sub>14,22,-,8,8</sub> |  | 2.4<br><sub>2,1,-,1,0</sub> |  | 1.7<br><sub>2,1,-,2,1</sub> |  | 1.6<br><sub>2,3,-,2,1</sub> |  | 0.6 | 0.6 | 1.4 | 16.5 |
| Zach Edey | 88% | 23.0<br><sub>20,-,-,21,21</sub> | 10.3<br><sub>2,-,-,23,11</sub> |  | 8.9<br><sub>5,-,-,10,2</sub> |  | 1.2<br><sub>0,-,-,1,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.5 | 1.4 | 1.5 | 20.4 |
| Taylor Hendricks | 88% | 19.8<br><sub>11,19,29,19,21</sub> | 9.4<br><sub>7,10,22,9,18</sub> |  | 4.4<br><sub>2,12,5,3,6</sub> |  | 1.2<br><sub>1,2,4,0,2</sub> |  | 1.1<br><sub>1,2,0,1,1</sub> |  | 0.9 | 0.5 | 1.0 | 14.9 |
| Olivier-Maxence Prosper | 80% | 15.5<br><sub>-,2,20,16,16</sub> | 8.3<br><sub>-,6,11,12,5</sub> |  | 2.8<br><sub>-,1,4,0,2</sub> |  | 0.9<br><sub>-,0,0,1,0</sub> |  | 0.8<br><sub>-,0,2,1,0</sub> |  | 0.6 | 0.2 | 0.7 | 12.0 |
| Kris Murray | 88% | 12.4<br><sub>-,1,19,6,6</sub> | 2.9<br><sub>-,0,3,0,5</sub> |  | 1.9<br><sub>-,1,2,1,0</sub> |  | 0.8<br><sub>-,0,3,0,0</sub> |  | 0.2<br><sub>-,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.4 | 5.7 |
| Jahmai Mashack | 66% | 12.3<br><sub>-,-,2,2,13</sub> | 4.1<br><sub>-,-,0,0,3</sub> |  | 1.6<br><sub>-,-,0,0,2</sub> |  | 1.6<br><sub>-,-,0,1,2</sub> |  | 0.3<br><sub>-,-,0,0,1</sub> |  | 0.5 | 0.3 | 0.9 | 7.2 |
| Quinten Post | 96% | 11.6<br><sub>-,-,-,9,6</sub> | 4.6<br><sub>-,-,-,5,3</sub> |  | 2.4<br><sub>-,-,-,3,2</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.5 |
| Karim Lopez | 52% | 6.7<br><sub>-,-,2,1,-</sub> | 2.8<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,2,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>if Draymond Green plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | 98% | 33.3<br><sub>27,36,24,33,30</sub> | 22.2<br><sub>23,25,3,28,13</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>7,10,7,8,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.8<br><sub>4,0,1,3,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>4,2,0,2,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.9 | 3.3 | 33.3 |
| Brandin Podziemski (GSW) | 96% | 33.0<br><sub>26,37,22,30,29</sub> | 18.9<br><sub>25,22,8,15,10</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>2,6,3,6,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.7<br><sub>4,4,0,3,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>5,4,2,3,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 1.9 | 29.0 |
| Draymond Green (GSW) | 100% | 26.9<br><sub>21,27,16,25,23</sub> | 6.2<br><sub>2,7,4,2,3</sub> |  | 5.3<br><sub>3,5,3,8,1</sub> |  | 6.0<br><sub>6,7,3,5,2</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 1.0 | 0.9 | 2.4 | 17.4 |
| Will Richard (GSW) | 98% | 25.3<br><sub>-,19,30,23,27</sub> | 8.4<br><sub>-,9,7,11,20</sub> |  | 3.0<br><sub>-,4,4,3,0</sub> |  | 1.8<br><sub>-,0,1,1,3</sub> |  | 1.1<br><sub>-,2,1,2,1</sub> |  | 1.3 | 0.3 | 1.0 | 13.2 |
| De'Anthony Melton (GSW) | 99% | 23.4<br><sub>26,25,18,21,19</sub> | 11.9<br><sub>16,11,8,8,0</sub> |  | 3.8<br><sub>4,4,4,2,2</sub> |  | 2.7<br><sub>3,4,3,1,2</sub> |  | 1.8<br><sub>4,3,2,2,0</sub> |  | 1.4 | 0.4 | 1.7 | 18.4 |
| LJ Cryer (GSW) | 88% | 19.6<br><sub>20,18,24,24,19</sub> | 9.5<br><sub>10,13,20,7,9</sub> |  | 1.7<br><sub>0,1,2,1,0</sub> |  | 2.1<br><sub>3,1,6,3,2</sub> |  | 1.6<br><sub>2,3,6,1,3</sub> |  | 0.5 | 0.1 | 0.9 | 13.2 |
| Gui Santos (GSW) | 93% | 19.6<br><sub>21,12,21,19,17</sub> | 8.5<br><sub>3,0,7,12,6</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>7,3,4,7,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>4,1,1,2,6</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.4 | 1.3 | 14.8 |
| Georges Niang (GSW) | 98% | 19.4<br><sub>19,19,15,14,14</sub> | 8.9<br><sub>9,5,5,0,11</sub> |  | 2.9<br><sub>2,5,3,4,1</sub> |  | 1.3<br><sub>2,0,2,2,1</sub> |  | 1.3<br><sub>1,1,1,0,2</sub> |  | 0.4 | 0.2 | 0.9 | 13.2 |
| Charles Bassey (GSW) | 98% | 18.8<br><sub>18,13,20,16,22</sub> | 9.2<br><sub>12,7,11,4,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>10,6,5,0,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>1,0,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 1.3 | 17.4 |
| Gary Payton II (GSW) | 88% | 17.3<br><sub>-,-,13,8,16</sub> | 7.8<br><sub>-,-,2,2,8</sub> |  | 3.3<br><sub>-,-,2,0,8</sub> |  | 1.4<br><sub>-,-,0,0,2</sub> |  | 0.6<br><sub>-,-,0,0,2</sub> |  | 1.0 | 0.2 | 0.8 | 12.6 |
| Graham Ike (GSW) | 93% | 13.5<br><sub>12,4,13,8,15</sub> | 5.7<br><sub>4,4,5,3,2</sub> |  | 3.4<br><sub>5,0,2,5,2</sub> |  | 1.4<br><sub>2,1,3,1,2</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.8 | 0.7 | 10.5 |
| Malevy Leons (GSW) | 76% | 9.8<br><sub>12,4,14,6,7</sub> | 3.0<br><sub>0,0,5,2,2</sub> |  | 1.8<br><sub>3,3,1,1,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.4 | 0.4 | 5.4 |
| Cameron Boozer (MEM) | 98% | 32.2<br><sub>33,25,29,29,28</sub> | 18.1<br><sub>13,12,15,29,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>11,10,8,7,8</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>5,3,5,7,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,1,0,7,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.7 | 2.9 | 32.9 |
| Cedric Coward (MEM) | 98% | 31.1<br><sub>27,30,33,27,33</sub> | 16.7<br><sub>15,14,23,18,20</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>11,7,12,8,3</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,6,4,6,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,0,4,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.5 | 2.0 | 28.2 |
| Jaylen Wells (MEM) | 99% | 28.4<br><sub>31,27,25,27,26</sub> | 12.5<br><sub>22,11,5,8,5</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>2,2,2,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>5,2,1,2,1</sub> |  | 0.8 | 0.1 | 1.0 | 17.4 |
| Cam Spencer (MEM) | 98% | 28.3<br><sub>20,24,34,32,29</sub> | 13.6<br><sub>15,14,17,12,26</sub> |  | 3.3<br><sub>3,2,1,6,1</sub> |  | 7.0<br><sub>3,5,8,9,7</sub> |  | 2.0<br><sub>3,3,3,1,5</sub> |  | 0.9 | 0.2 | 1.8 | 23.8 |
| Javon Small (MEM) | 98% | 25.8<br><sub>15,15,30,29,21</sub> | 12.0<br><sub>3,10,19,12,2</sub> |  | 3.6<br><sub>1,2,2,5,4</sub> |  | 4.9<br><sub>4,5,5,12,5</sub> |  | 1.6<br><sub>1,2,3,0,0</sub> |  | 0.9 | 0.2 | 1.7 | 20.5 |
| Jerami Grant (MEM) | 98% | 24.3<br><sub>20,26,-,23,20</sub> | 12.4<br><sub>14,22,-,8,8</sub> |  | 2.4<br><sub>2,1,-,1,0</sub> |  | 1.7<br><sub>2,1,-,2,1</sub> |  | 1.6<br><sub>2,3,-,2,1</sub> |  | 0.6 | 0.6 | 1.4 | 16.5 |
| Zach Edey (MEM) | 88% | 23.0<br><sub>20,-,-,21,21</sub> | 10.3<br><sub>2,-,-,23,11</sub> |  | 9.0<br><sub>5,-,-,10,2</sub> |  | 1.2<br><sub>0,-,-,1,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.5 | 1.4 | 1.5 | 20.4 |
| Taylor Hendricks (MEM) | 88% | 19.9<br><sub>11,19,29,19,21</sub> | 9.5<br><sub>7,10,22,9,18</sub> |  | 4.4<br><sub>2,12,5,3,6</sub> |  | 1.1<br><sub>1,2,4,0,2</sub> |  | 1.1<br><sub>1,2,0,1,1</sub> |  | 0.9 | 0.5 | 1.1 | 15.0 |
| Olivier-Maxence Prosper (MEM) | 80% | 15.3<br><sub>-,2,20,16,16</sub> | 8.2<br><sub>-,6,11,12,5</sub> |  | 2.8<br><sub>-,1,4,0,2</sub> |  | 0.9<br><sub>-,0,0,1,0</sub> |  | 0.8<br><sub>-,0,2,1,0</sub> |  | 0.6 | 0.2 | 0.7 | 11.9 |
| Jahmai Mashack (MEM) | 66% | 12.3<br><sub>-,-,2,2,13</sub> | 4.1<br><sub>-,-,0,0,3</sub> |  | 1.6<br><sub>-,-,0,0,2</sub> |  | 1.6<br><sub>-,-,0,1,2</sub> |  | 0.3<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.2 | 0.8 | 7.2 |
| Kris Murray (MEM) | 88% | 12.3<br><sub>-,1,19,6,6</sub> | 2.9<br><sub>-,0,3,0,5</sub> |  | 1.9<br><sub>-,1,2,1,0</sub> |  | 0.8<br><sub>-,0,3,0,0</sub> |  | 0.2<br><sub>-,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.4 | 5.7 |
| Quinten Post (MEM) | 96% | 11.6<br><sub>-,-,-,9,6</sub> | 4.7<br><sub>-,-,-,5,3</sub> |  | 2.4<br><sub>-,-,-,3,2</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.5 |
| Karim Lopez (MEM) | 52% | 6.6<br><sub>-,-,2,1,-</sub> | 2.8<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,2,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.7 |

</details>


### POR @ MIL
Out: Ousmane Dieng (MIL), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Robert Williams III (POR), Chris Youngblood (POR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.9–110.2 | POR 68% | 1.46 / 3.17 | MIL +6.5 | 226.5 | MIL +10.5 covers 61%; o229.5 44% |
| Expected (weighted by chance each plays) | 118.4–110.1 | POR 72% | 1.39 / 3.57 | MIL +8.5 | 228.5 | MIL +10.5 covers 56%; o229.5 47% |
| if Ryan Rollins plays | 116.7–110.3 | POR 68% | 1.48 / 3.09 | MIL +6.5 | 226.5 | MIL +10.5 covers 62%; o229.5 44% |
| if Deni Avdija plays | 120.0–110.0 | POR 76% | 1.31 / 4.23 | MIL +9.5 | 229.5 | MIL +10.5 covers 52%; o229.5 51% |
| if Toumani Camara plays | 117.4–110.0 | POR 70% | 1.42 / 3.36 | MIL +7.5 | 227.5 | MIL +10.5 covers 59%; o229.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Rollins (MIL) | Day-To-Day | 70% | 23.9 | 11.9 | 4.0 | 3.8 | 1.5 | 1.2 | 0.4 | 2.2 | 19.8 | full tables below |
| Deni Avdija (POR) | Questionable | 55% | 35.2 | 27.8 | 7.1 | 6.9 | 2.1 | 1.0 | 0.6 | 3.6 | 41.7 | full tables below |
| Toumani Camara (POR) | Questionable | 55% | 33.7 | 15.0 | 5.0 | 2.3 | 2.5 | 1.3 | 0.5 | 1.5 | 22.4 | full tables below |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard | 98% | 33.8<br><sub>24,32,33,24,31</sub> | 25.7<br><sub>25,18,29,9,25</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.9<br><sub>3,3,6,4,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.6<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.2 | 2.9 | 35.9 |
| Sidy Cissoko | 98% | 33.0<br><sub>33,29,26,28,32</sub> | 11.2<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>3,0,1,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.5 | 1.5 | 18.8 |
| Jrue Holiday | 98% | 32.6<br><sub>25,30,27,25,31</sub> | 20.5<br><sub>11,19,6,10,23</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>1,3,5,4,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 6.4<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.3 | 2.6 | 31.6 |
| Donovan Clingan | 98% | 30.5<br><sub>26,30,27,22,32</sub> | 16.1<br><sub>7,5,13,10,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 13.5<br><sub>13,12,11,10,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,1,1,0,0</sub> |  | 0.8 | 1.9 | 1.7 | 32.6 |
| Scoot Henderson | 98% | 29.0<br><sub>23,19,23,23,21</sub> | 17.2<br><sub>11,5,11,10,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 2.7 | 24.0 |
| Jayson Kent | 72% | 27.4<br><sub>-,-,11,11,27</sub> | 10.8<br><sub>-,-,3,8,8</sub> |  | 3.6<br><sub>-,-,1,0,3</sub> |  | 1.7<br><sub>-,-,0,0,0</sub> |  | 1.6<br><sub>-,-,1,2,2</sub> |  | 1.3 | 0.4 | 1.2 | 16.0 |
| Branden Carlson | 88% | 20.7<br><sub>8,10,8,14,14</sub> | 6.8<br><sub>2,0,5,5,6</sub> |  | 5.1<br><sub>5,2,3,6,1</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.7 | 0.8 | 0.9 | 12.9 |
| Yang Hansen | 52% | 17.8<br><sub>5,-,-,7,-</sub> | 7.2<br><sub>0,-,-,0,-</sub> |  | 4.7<br><sub>1,-,-,1,-</sub> |  | 1.2<br><sub>0,-,-,3,-</sub> |  | 0.6<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.5 | 1.2 | 13.2 |
| Micah Potter | 64% | 17.8<br><sub>5,-,-,7,1</sub> | 8.7<br><sub>0,-,-,2,0</sub> |  | 5.1<br><sub>3,-,-,4,0</sub> |  | 1.1<br><sub>0,-,-,1,0</sub> |  | 1.0<br><sub>0,-,-,0,0</sub> |  | 0.6 | 0.3 | 0.8 | 15.0 |
| John Tonje | 47% | 17.7<br><sub>-,-,-,7,-</sub> | 9.6<br><sub>-,-,-,7,-</sub> |  | 3.6<br><sub>-,-,-,4,-</sub> |  | 1.8<br><sub>-,-,-,3,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.8 | 0.3 | 0.9 | 15.0 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 30.8<br><sub>-,35,34,20,24</sub> | 18.8<br><sub>-,27,18,5,8</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>-,2,1,5,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>-,7,2,3,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>-,2,2,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 2.4 | 27.4 |
| Kyle Kuzma | 98% | 28.6<br><sub>26,24,31,22,30</sub> | 12.9<br><sub>5,9,14,14,26</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>5,1,4,6,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>3,1,2,2,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.5 | 2.1 | 20.6 |
| Jaime Jaquez Jr. | 99% | 28.2<br><sub>25,30,28,30,23</sub> | 15.4<br><sub>16,25,22,6,10</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,5,6,5,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>3,3,4,4,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>2,2,5,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 2.2 | 24.4 |
| Myles Turner | 98% | 26.2<br><sub>27,-,31,23,21</sub> | 10.4<br><sub>3,-,14,8,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>3,-,11,7,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>2,-,3,1,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.5<br><sub>1,-,4,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 1.8 | 1.5 | 18.0 |
| Brayden Burries | 98% | 25.5<br><sub>26,23,19,29,25</sub> | 11.2<br><sub>3,8,3,13,20</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>3,5,4,8,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.3 | 1.6 | 19.4 |
| Kasparas Jakucionis | 86% | 20.4<br><sub>23,4,-,26,26</sub> | 9.1<br><sub>11,4,-,25,20</sub> |  | 2.6<br><sub>0,2,-,5,3</sub> |  | 3.6<br><sub>4,0,-,5,5</sub> |  | 0.9<br><sub>2,0,-,4,3</sub> |  | 0.8 | 0.2 | 1.7 | 15.2 |
| Kel'el Ware | 98% | 18.0<br><sub>17,23,17,25,17</sub> | 9.0<br><sub>8,8,10,8,11</sub> |  | 5.9<br><sub>4,5,6,11,3</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> |  | 0.8<br><sub>0,0,2,1,1</sub> |  | 0.6 | 1.0 | 1.2 | 16.0 |
| Nate Ament | 96% | 17.6<br><sub>22,22,22,17,17</sub> | 6.6<br><sub>10,2,9,5,7</sub> |  | 2.6<br><sub>2,4,3,2,4</sub> |  | 0.9<br><sub>1,1,1,1,1</sub> |  | 0.7<br><sub>2,0,2,1,0</sub> |  | 0.7 | 0.3 | 0.9 | 10.1 |
| Gary Trent Jr. | 72% | 17.0<br><sub>6,4,16,30,16</sub> | 7.5<br><sub>5,6,1,18,1</sub> |  | 1.1<br><sub>0,1,0,2,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.2<br><sub>1,2,0,4,0</sub> |  | 0.7 | 0.1 | 0.6 | 9.4 |
| AJ Green | 99% | 16.2<br><sub>8,8,8,6,14</sub> | 5.3<br><sub>0,3,0,0,11</sub> |  | 1.6<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>0,1,2,0,1</sub> |  | 0.9<br><sub>0,1,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.9 |
| Cormac Ryan | 5% | 14.9 | 7.2 |  | 1.6 |  | 1.0 |  | 0.9 |  | 0.6 | 0.3 | 1.1 | 9.8 |
| Jericho Sims | 76% | 14.6<br><sub>8,18,-,11,18</sub> | 3.7<br><sub>2,0,-,4,4</sub> |  | 3.6<br><sub>0,4,-,2,6</sub> |  | 1.2<br><sub>0,1,-,0,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.9 | 8.6 |
| Kam Jones | 5% | 11.5 | 3.2 |  | 1.2 |  | 2.0 |  | 0.2 |  | 0.5 | 0.1 | 0.8 | 6.4 |
| Caris LeVert | 38% | 11.0<br><sub>-,-,-,-,8</sub> | 4.2<br><sub>-,-,-,-,8</sub> |  | 1.4<br><sub>-,-,-,-,3</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.3 | 0.7 | 6.8 |
| Pete Nance | 93% | 9.5<br><sub>-,4,-,-,-</sub> | 3.1<br><sub>-,3,-,-,-</sub> |  | 1.6<br><sub>-,1,-,-,-</sub> |  | 0.7<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.4 |
| Bogoljub Markovic | 51% | 6.6<br><sub>4,4,-,-,-</sub> | 2.7<br><sub>0,0,-,-,-</sub> |  | 1.6<br><sub>2,0,-,-,-</sub> |  | 0.3<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.6 |

</details>

<details><summary>if Deni Avdija plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 30.9<br><sub>-,35,34,20,24</sub> | 18.7<br><sub>-,27,18,5,8</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>-,2,1,5,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>-,7,2,3,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>-,2,2,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 2.4 | 27.3 |
| Kyle Kuzma (MIL) | 98% | 28.5<br><sub>26,24,31,22,30</sub> | 12.8<br><sub>5,9,14,14,26</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>5,1,4,6,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>3,1,2,2,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.5 | 2.1 | 20.4 |
| Jaime Jaquez Jr. (MIL) | 99% | 28.1<br><sub>25,30,28,30,23</sub> | 15.2<br><sub>16,25,22,6,10</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,5,6,5,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>3,3,4,4,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>2,2,5,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 2.2 | 24.2 |
| Myles Turner (MIL) | 98% | 26.2<br><sub>27,-,31,23,21</sub> | 10.4<br><sub>3,-,14,8,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>3,-,11,7,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>2,-,3,1,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.5<br><sub>1,-,4,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 1.8 | 1.4 | 18.0 |
| Brayden Burries (MIL) | 98% | 25.4<br><sub>26,23,19,29,25</sub> | 11.2<br><sub>3,8,3,13,20</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>3,5,4,8,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.3 | 1.6 | 19.4 |
| Kasparas Jakucionis (MIL) | 86% | 20.4<br><sub>23,4,-,26,26</sub> | 9.1<br><sub>11,4,-,25,20</sub> |  | 2.6<br><sub>0,2,-,5,3</sub> |  | 3.6<br><sub>4,0,-,5,5</sub> |  | 0.9<br><sub>2,0,-,4,3</sub> |  | 0.9 | 0.2 | 1.6 | 15.3 |
| Kel'el Ware (MIL) | 98% | 18.2<br><sub>17,23,17,25,17</sub> | 9.0<br><sub>8,8,10,8,11</sub> |  | 6.0<br><sub>4,5,6,11,3</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> |  | 0.8<br><sub>0,0,2,1,1</sub> |  | 0.6 | 1.0 | 1.2 | 16.0 |
| Nate Ament (MIL) | 96% | 17.6<br><sub>22,22,22,17,17</sub> | 6.6<br><sub>10,2,9,5,7</sub> |  | 2.6<br><sub>2,4,3,2,4</sub> |  | 0.9<br><sub>1,1,1,1,1</sub> |  | 0.7<br><sub>2,0,2,1,0</sub> |  | 0.7 | 0.3 | 0.9 | 10.1 |
| Gary Trent Jr. (MIL) | 72% | 17.0<br><sub>6,4,16,30,16</sub> | 7.4<br><sub>5,6,1,18,1</sub> |  | 1.2<br><sub>0,1,0,2,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.2<br><sub>1,2,0,4,0</sub> |  | 0.7 | 0.1 | 0.6 | 9.4 |
| AJ Green (MIL) | 99% | 16.2<br><sub>8,8,8,6,14</sub> | 5.3<br><sub>0,3,0,0,11</sub> |  | 1.6<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>0,1,2,0,1</sub> |  | 0.9<br><sub>0,1,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 8.0 |
| Cormac Ryan (MIL) | 5% | 14.7 | 7.1 |  | 1.5 |  | 1.0 |  | 0.9 |  | 0.6 | 0.2 | 1.1 | 9.7 |
| Jericho Sims (MIL) | 76% | 14.5<br><sub>8,18,-,11,18</sub> | 3.7<br><sub>2,0,-,4,4</sub> |  | 3.6<br><sub>0,4,-,2,6</sub> |  | 1.2<br><sub>0,1,-,0,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.9 | 8.6 |
| Kam Jones (MIL) | 5% | 11.3 | 3.1 |  | 1.2 |  | 2.0 |  | 0.2 |  | 0.4 | 0.1 | 0.8 | 6.4 |
| Caris LeVert (MIL) | 38% | 11.0<br><sub>-,-,-,-,8</sub> | 4.2<br><sub>-,-,-,-,8</sub> |  | 1.4<br><sub>-,-,-,-,3</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.3 | 0.7 | 6.8 |
| Pete Nance (MIL) | 93% | 9.5<br><sub>-,4,-,-,-</sub> | 3.1<br><sub>-,3,-,-,-</sub> |  | 1.6<br><sub>-,1,-,-,-</sub> |  | 0.7<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.4 |
| Bogoljub Markovic (MIL) | 51% | 6.7<br><sub>4,4,-,-,-</sub> | 2.7<br><sub>0,0,-,-,-</sub> |  | 1.6<br><sub>2,0,-,-,-</sub> |  | 0.3<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.6 |
| Deni Avdija (POR) | 100% | 35.2<br><sub>34,35,35,30,-</sub> | 27.8<br><sub>24,28,34,27,-</sub> | 24.5 · – | 7.1<br><sub>6,3,6,8,-</sub> | 6.5 | 6.9<br><sub>8,6,4,4,-</sub> | 5.5 | 2.1<br><sub>2,4,3,3,-</sub> | 1.5 | 1.0 | 0.6 | 3.6 | 41.7 |
| Damian Lillard (POR) | 98% | 33.6<br><sub>24,32,33,24,31</sub> | 22.4<br><sub>25,18,29,9,25</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>3,3,6,4,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 2.4 | 31.6 |
| Jrue Holiday (POR) | 98% | 32.2<br><sub>25,30,27,25,31</sub> | 16.6<br><sub>11,19,6,10,23</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>1,3,5,4,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 5.5<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 2.1 | 26.9 |
| Sidy Cissoko (POR) | 98% | 31.6<br><sub>33,29,26,28,32</sub> | 9.3<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,0,1,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 1.2 | 16.2 |
| Donovan Clingan (POR) | 98% | 31.0<br><sub>26,30,27,22,32</sub> | 14.2<br><sub>7,5,13,10,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 13.5<br><sub>13,12,11,10,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,1,1,0,0</sub> |  | 0.8 | 2.2 | 1.3 | 30.1 |
| Scoot Henderson (POR) | 98% | 27.6<br><sub>23,19,23,23,21</sub> | 13.5<br><sub>11,5,11,10,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 2.2 | 19.0 |
| Jayson Kent (POR) | 72% | 21.6<br><sub>-,-,11,11,27</sub> | 7.8<br><sub>-,-,3,8,8</sub> |  | 2.8<br><sub>-,-,1,0,3</sub> |  | 1.3<br><sub>-,-,0,0,0</sub> |  | 1.1<br><sub>-,-,1,2,2</sub> |  | 1.0 | 0.3 | 0.8 | 11.9 |
| Branden Carlson (POR) | 88% | 16.1<br><sub>8,10,8,14,14</sub> | 4.7<br><sub>2,0,5,5,6</sub> |  | 3.9<br><sub>5,2,3,6,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 0.4<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.7 | 0.7 | 9.4 |
| Micah Potter (POR) | 64% | 12.9<br><sub>5,-,-,7,1</sub> | 5.5<br><sub>0,-,-,2,0</sub> |  | 3.7<br><sub>3,-,-,4,0</sub> |  | 0.7<br><sub>0,-,-,1,0</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 9.9 |
| Yang Hansen (POR) | 52% | 12.8<br><sub>5,-,-,7,-</sub> | 4.5<br><sub>0,-,-,0,-</sub> |  | 3.5<br><sub>1,-,-,1,-</sub> |  | 0.8<br><sub>0,-,-,3,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.8 | 8.8 |
| John Tonje (POR) | 47% | 11.6<br><sub>-,-,-,7,-</sub> | 4.5<br><sub>-,-,-,7,-</sub> |  | 2.6<br><sub>-,-,-,4,-</sub> |  | 1.3<br><sub>-,-,-,3,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.5 |

</details>

<details><summary>if Ryan Rollins plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 29.7<br><sub>-,35,34,20,24</sub> | 17.7<br><sub>-,27,18,5,8</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>-,2,1,5,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.1<br><sub>-,7,2,3,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>-,2,2,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.4 | 2.2 | 25.8 |
| Kyle Kuzma (MIL) | 98% | 26.8<br><sub>26,24,31,22,30</sub> | 11.7<br><sub>5,9,14,14,26</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>5,1,4,6,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>3,1,2,2,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.5 | 1.8 | 18.9 |
| Jaime Jaquez Jr. (MIL) | 99% | 26.1<br><sub>25,30,28,30,23</sub> | 13.8<br><sub>16,25,22,6,10</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>5,5,6,5,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,3,4,4,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>2,2,5,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.9 | 21.9 |
| Myles Turner (MIL) | 98% | 24.7<br><sub>27,-,31,23,21</sub> | 10.1<br><sub>3,-,14,8,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>3,-,11,7,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>2,-,3,1,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4<br><sub>1,-,4,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 1.7 | 1.3 | 17.3 |
| Ryan Rollins (MIL) | 100% | 23.9<br><sub>24,24,29,-,-</sub> | 11.9<br><sub>14,8,8,-,-</sub> |  | 4.0<br><sub>5,7,10,-,-</sub> |  | 3.8<br><sub>2,4,2,-,-</sub> |  | 1.5<br><sub>4,2,0,-,-</sub> |  | 1.2 | 0.4 | 2.2 | 19.8 |
| Brayden Burries (MIL) | 98% | 22.5<br><sub>26,23,19,29,25</sub> | 10.0<br><sub>3,8,3,13,20</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>3,5,4,8,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 0.2 | 1.3 | 17.0 |
| Kasparas Jakucionis (MIL) | 86% | 17.8<br><sub>23,4,-,26,26</sub> | 7.8<br><sub>11,4,-,25,20</sub> |  | 2.3<br><sub>0,2,-,5,3</sub> |  | 3.0<br><sub>4,0,-,5,5</sub> |  | 0.8<br><sub>2,0,-,4,3</sub> |  | 0.7 | 0.1 | 1.4 | 13.1 |
| Kel'el Ware (MIL) | 98% | 16.5<br><sub>17,23,17,25,17</sub> | 8.2<br><sub>8,8,10,8,11</sub> |  | 5.5<br><sub>4,5,6,11,3</sub> |  | 0.9<br><sub>1,1,1,2,1</sub> |  | 0.7<br><sub>0,0,2,1,1</sub> |  | 0.5 | 0.9 | 1.1 | 14.7 |
| Nate Ament (MIL) | 96% | 15.9<br><sub>22,22,22,17,17</sub> | 5.9<br><sub>10,2,9,5,7</sub> |  | 2.4<br><sub>2,4,3,2,4</sub> |  | 0.7<br><sub>1,1,1,1,1</sub> |  | 0.6<br><sub>2,0,2,1,0</sub> |  | 0.6 | 0.2 | 0.8 | 9.0 |
| Gary Trent Jr. (MIL) | 72% | 15.0<br><sub>6,4,16,30,16</sub> | 6.2<br><sub>5,6,1,18,1</sub> |  | 1.0<br><sub>0,1,0,2,1</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.9<br><sub>1,2,0,4,0</sub> |  | 0.6 | 0.1 | 0.6 | 7.9 |
| Cormac Ryan (MIL) | 5% | 14.4 | 6.8 |  | 1.5 |  | 1.0 |  | 0.9 |  | 0.6 | 0.2 | 1.0 | 9.3 |
| AJ Green (MIL) | 99% | 13.9<br><sub>8,8,8,6,14</sub> | 4.3<br><sub>0,3,0,0,11</sub> |  | 1.4<br><sub>0,1,0,0,0</sub> |  | 0.8<br><sub>0,1,2,0,1</sub> |  | 0.6<br><sub>0,1,0,0,3</sub> |  | 0.3 | 0.1 | 0.5 | 6.5 |
| Jericho Sims (MIL) | 76% | 12.9<br><sub>8,18,-,11,18</sub> | 3.3<br><sub>2,0,-,4,4</sub> |  | 3.3<br><sub>0,4,-,2,6</sub> |  | 1.1<br><sub>0,1,-,0,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.2 | 0.2 | 0.8 | 7.7 |
| Kam Jones (MIL) | 5% | 9.6 | 2.5 |  | 1.0 |  | 1.8 |  | 0.2 |  | 0.4 | 0.1 | 0.7 | 5.3 |
| Caris LeVert (MIL) | 38% | 9.2<br><sub>-,-,-,-,8</sub> | 3.6<br><sub>-,-,-,-,8</sub> |  | 1.2<br><sub>-,-,-,-,3</sub> |  | 0.9<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,1</sub> |  | 0.5 | 0.3 | 0.6 | 5.8 |
| Pete Nance (MIL) | 93% | 8.3<br><sub>-,4,-,-,-</sub> | 2.8<br><sub>-,3,-,-,-</sub> |  | 1.4<br><sub>-,1,-,-,-</sub> |  | 0.6<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Bogoljub Markovic (MIL) | 51% | 6.0<br><sub>4,4,-,-,-</sub> | 2.6<br><sub>0,0,-,-,-</sub> |  | 1.4<br><sub>2,0,-,-,-</sub> |  | 0.3<br><sub>1,0,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.3 |
| Damian Lillard (POR) | 98% | 33.8<br><sub>24,32,33,24,31</sub> | 25.8<br><sub>25,18,29,9,25</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>3,3,6,4,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.7<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.2 | 2.9 | 36.0 |
| Sidy Cissoko (POR) | 98% | 33.0<br><sub>33,29,26,28,32</sub> | 11.3<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>3,0,1,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.5 | 1.5 | 18.8 |
| Jrue Holiday (POR) | 98% | 32.6<br><sub>25,30,27,25,31</sub> | 20.4<br><sub>11,19,6,10,23</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>1,3,5,4,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 6.4<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.3 | 2.6 | 31.6 |
| Donovan Clingan (POR) | 98% | 30.5<br><sub>26,30,27,22,32</sub> | 16.1<br><sub>7,5,13,10,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 13.6<br><sub>13,12,11,10,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,1,1,0,0</sub> |  | 0.8 | 1.9 | 1.7 | 32.6 |
| Scoot Henderson (POR) | 98% | 29.0<br><sub>23,19,23,23,21</sub> | 17.2<br><sub>11,5,11,10,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 2.7 | 23.9 |
| Jayson Kent (POR) | 72% | 27.4<br><sub>-,-,11,11,27</sub> | 10.6<br><sub>-,-,3,8,8</sub> |  | 3.5<br><sub>-,-,1,0,3</sub> |  | 1.7<br><sub>-,-,0,0,0</sub> |  | 1.5<br><sub>-,-,1,2,2</sub> |  | 1.3 | 0.4 | 1.2 | 15.8 |
| Branden Carlson (POR) | 88% | 20.7<br><sub>8,10,8,14,14</sub> | 6.8<br><sub>2,0,5,5,6</sub> |  | 5.1<br><sub>5,2,3,6,1</sub> |  | 1.1<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.7 | 0.8 | 0.9 | 13.0 |
| Micah Potter (POR) | 64% | 17.9<br><sub>5,-,-,7,1</sub> | 8.7<br><sub>0,-,-,2,0</sub> |  | 5.2<br><sub>3,-,-,4,0</sub> |  | 1.1<br><sub>0,-,-,1,0</sub> |  | 0.9<br><sub>0,-,-,0,0</sub> |  | 0.6 | 0.3 | 0.8 | 15.1 |
| Yang Hansen (POR) | 52% | 17.7<br><sub>5,-,-,7,-</sub> | 7.2<br><sub>0,-,-,0,-</sub> |  | 4.7<br><sub>1,-,-,1,-</sub> |  | 1.2<br><sub>0,-,-,3,-</sub> |  | 0.6<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.5 | 1.2 | 13.1 |
| John Tonje (POR) | 47% | 17.7<br><sub>-,-,-,7,-</sub> | 9.5<br><sub>-,-,-,7,-</sub> |  | 3.6<br><sub>-,-,-,4,-</sub> |  | 1.8<br><sub>-,-,-,3,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.8 | 0.3 | 0.9 | 14.9 |

</details>

<details><summary>if Toumani Camara plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 30.9<br><sub>-,35,34,20,24</sub> | 18.8<br><sub>-,27,18,5,8</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>-,2,1,5,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>-,7,2,3,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>-,2,2,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 2.4 | 27.4 |
| Kyle Kuzma (MIL) | 98% | 28.6<br><sub>26,24,31,22,30</sub> | 12.9<br><sub>5,9,14,14,26</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>5,1,4,6,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>3,1,2,2,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.5 | 2.1 | 20.5 |
| Jaime Jaquez Jr. (MIL) | 99% | 28.2<br><sub>25,30,28,30,23</sub> | 15.4<br><sub>16,25,22,6,10</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,5,6,5,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>3,3,4,4,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>2,2,5,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 2.2 | 24.4 |
| Myles Turner (MIL) | 98% | 26.2<br><sub>27,-,31,23,21</sub> | 10.3<br><sub>3,-,14,8,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>3,-,11,7,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>2,-,3,1,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.5<br><sub>1,-,4,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 1.8 | 1.4 | 17.9 |
| Brayden Burries (MIL) | 98% | 25.5<br><sub>26,23,19,29,25</sub> | 11.2<br><sub>3,8,3,13,20</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>3,5,4,8,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.3 | 1.6 | 19.4 |
| Kasparas Jakucionis (MIL) | 86% | 20.4<br><sub>23,4,-,26,26</sub> | 9.0<br><sub>11,4,-,25,20</sub> |  | 2.6<br><sub>0,2,-,5,3</sub> |  | 3.6<br><sub>4,0,-,5,5</sub> |  | 0.9<br><sub>2,0,-,4,3</sub> |  | 0.8 | 0.2 | 1.7 | 15.2 |
| Kel'el Ware (MIL) | 98% | 18.1<br><sub>17,23,17,25,17</sub> | 9.1<br><sub>8,8,10,8,11</sub> |  | 6.0<br><sub>4,5,6,11,3</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> |  | 0.8<br><sub>0,0,2,1,1</sub> |  | 0.6 | 1.0 | 1.2 | 16.1 |
| Nate Ament (MIL) | 96% | 17.6<br><sub>22,22,22,17,17</sub> | 6.6<br><sub>10,2,9,5,7</sub> |  | 2.6<br><sub>2,4,3,2,4</sub> |  | 0.9<br><sub>1,1,1,1,1</sub> |  | 0.7<br><sub>2,0,2,1,0</sub> |  | 0.7 | 0.3 | 0.9 | 10.1 |
| Gary Trent Jr. (MIL) | 72% | 17.0<br><sub>6,4,16,30,16</sub> | 7.4<br><sub>5,6,1,18,1</sub> |  | 1.1<br><sub>0,1,0,2,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.2<br><sub>1,2,0,4,0</sub> |  | 0.7 | 0.1 | 0.6 | 9.3 |
| AJ Green (MIL) | 99% | 16.2<br><sub>8,8,8,6,14</sub> | 5.3<br><sub>0,3,0,0,11</sub> |  | 1.6<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>0,1,2,0,1</sub> |  | 0.9<br><sub>0,1,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.9 |
| Cormac Ryan (MIL) | 5% | 14.7 | 7.3 |  | 1.6 |  | 1.0 |  | 0.9 |  | 0.6 | 0.2 | 1.0 | 9.9 |
| Jericho Sims (MIL) | 76% | 14.6<br><sub>8,18,-,11,18</sub> | 3.8<br><sub>2,0,-,4,4</sub> |  | 3.6<br><sub>0,4,-,2,6</sub> |  | 1.2<br><sub>0,1,-,0,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.9 | 8.6 |
| Kam Jones (MIL) | 5% | 11.5 | 3.1 |  | 1.2 |  | 2.1 |  | 0.2 |  | 0.5 | 0.1 | 0.8 | 6.4 |
| Caris LeVert (MIL) | 38% | 10.9<br><sub>-,-,-,-,8</sub> | 4.2<br><sub>-,-,-,-,8</sub> |  | 1.4<br><sub>-,-,-,-,3</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.5 | 0.3 | 0.7 | 6.8 |
| Pete Nance (MIL) | 93% | 9.5<br><sub>-,4,-,-,-</sub> | 3.1<br><sub>-,3,-,-,-</sub> |  | 1.6<br><sub>-,1,-,-,-</sub> |  | 0.7<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.5 |
| Bogoljub Markovic (MIL) | 51% | 6.6<br><sub>4,4,-,-,-</sub> | 2.7<br><sub>0,0,-,-,-</sub> |  | 1.6<br><sub>2,0,-,-,-</sub> |  | 0.3<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.6 |
| Toumani Camara (POR) | 100% | 33.7<br><sub>30,38,36,26,33</sub> | 15.0<br><sub>12,14,14,3,10</sub> | 12.5 · – | 5.0<br><sub>3,5,2,0,8</sub> | 4.5 | 2.3<br><sub>3,3,1,0,1</sub> |  | 2.5<br><sub>2,2,2,0,2</sub> | 2.5 | 1.3 | 0.5 | 1.5 | 22.4 |
| Damian Lillard (POR) | 98% | 33.4<br><sub>24,32,33,24,31</sub> | 24.0<br><sub>25,18,29,9,25</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>3,3,6,4,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 2.6 | 33.9 |
| Jrue Holiday (POR) | 98% | 32.2<br><sub>25,30,27,25,31</sub> | 18.9<br><sub>11,19,6,10,23</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>1,3,5,4,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 6.2<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.3 | 2.4 | 29.8 |
| Sidy Cissoko (POR) | 98% | 31.9<br><sub>33,29,26,28,32</sub> | 10.1<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,0,1,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 1.4 | 17.3 |
| Donovan Clingan (POR) | 98% | 30.7<br><sub>26,30,27,22,32</sub> | 15.1<br><sub>7,5,13,10,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 13.1<br><sub>13,12,11,10,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,1,1,0,0</sub> |  | 0.8 | 2.2 | 1.5 | 30.9 |
| Scoot Henderson (POR) | 98% | 28.2<br><sub>23,19,23,23,21</sub> | 15.4<br><sub>11,5,11,10,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 2.4 | 21.7 |
| Jayson Kent (POR) | 72% | 22.9<br><sub>-,-,11,11,27</sub> | 8.7<br><sub>-,-,3,8,8</sub> |  | 3.0<br><sub>-,-,1,0,3</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> |  | 1.1 | 0.3 | 0.9 | 13.1 |
| Branden Carlson (POR) | 88% | 16.6<br><sub>8,10,8,14,14</sub> | 5.4<br><sub>2,0,5,5,6</sub> |  | 4.1<br><sub>5,2,3,6,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 0.4<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.7 | 0.7 | 10.3 |
| Yang Hansen (POR) | 52% | 13.0<br><sub>5,-,-,7,-</sub> | 5.0<br><sub>0,-,-,0,-</sub> |  | 3.6<br><sub>1,-,-,1,-</sub> |  | 0.9<br><sub>0,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.3 | 0.9 | 9.5 |
| Micah Potter (POR) | 64% | 13.0<br><sub>5,-,-,7,1</sub> | 5.9<br><sub>0,-,-,2,0</sub> |  | 3.8<br><sub>3,-,-,4,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.5 |
| John Tonje (POR) | 47% | 12.2<br><sub>-,-,-,7,-</sub> | 4.9<br><sub>-,-,-,7,-</sub> |  | 2.6<br><sub>-,-,-,4,-</sub> |  | 1.4<br><sub>-,-,-,3,-</sub> |  | 0.7<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.2 | 0.7 | 9.0 |

</details>


### NYK @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.4–108.8 | NYK 63% | 1.59 / 2.68 | MIN +4.5 | 221.5 | MIN +1.5 covers 40%; o215.5 63% |
| Expected (weighted by chance each plays) | 113.3–109.0 | NYK 62% | 1.62 / 2.62 | MIN +4.5 | 222.5 | MIN +1.5 covers 41%; o215.5 64% |
| if Jonathan Kuminga plays | 113.4–109.4 | NYK 61% | 1.63 / 2.58 | MIN +4.5 | 222.5 | MIN +1.5 covers 42%; o215.5 65% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jonathan Kuminga (MIN) | Questionable | 55% | 30.5 | 12.8 | 5.5 | 2.2 | 1.3 | 0.8 | 0.6 | 1.4 | 20.5 | full tables below |
| Zyon Pullin (MIN) | Questionable | 55% | 8.1 | 2.9 | 0.8 | 0.9 | 0.1 | 0.2 | 0.1 | 0.5 | 4.7 | small |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 35.5<br><sub>28,35,36,41,34</sub> | 27.6<br><sub>23,27,33,28,31</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>4,3,1,1,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 6.2<br><sub>2,5,11,9,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,3,4,3,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.6 | 37.1 |
| OG Anunoby | 98% | 34.6<br><sub>29,34,33,44,36</sub> | 16.3<br><sub>19,14,11,21,16</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>3,6,2,9,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,2,1,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>5,2,2,2,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.9 | 1.9 | 23.4 |
| Karl-Anthony Towns | 98% | 34.2<br><sub>27,34,34,43,36</sub> | 20.8<br><sub>21,21,23,28,16</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 13.3<br><sub>16,11,15,17,16</sub> | 13.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>3,8,5,3,8</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,2,3,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.8 | 2.9 | 38.2 |
| Josh Hart | 98% | 29.0<br><sub>-,26,23,26,31</sub> | 8.5<br><sub>-,6,0,0,5</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>-,4,5,5,4</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.5<br><sub>-,3,4,2,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>-,0,0,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.3 | 1.4 | 18.6 |
| Mikal Bridges | 98% | 27.5<br><sub>17,17,29,32,30</sub> | 9.6<br><sub>4,2,18,5,17</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>5,1,3,7,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>1,2,3,3,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.0 | 0.5 | 1.0 | 15.3 |
| Landry Shamet | 98% | 23.6<br><sub>28,29,21,30,24</sub> | 8.3<br><sub>10,12,5,23,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>3,2,3,2,1</sub> |  | 1.3<br><sub>2,4,1,0,1</sub> |  | 1.3<br><sub>2,2,1,4,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.2 | 0.8 | 11.3 |
| Miles McBride | 98% | 15.5<br><sub>25,27,22,14,9</sub> | 5.2<br><sub>8,19,9,3,3</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 1.1<br><sub>3,2,1,0,1</sub> |  | 0.8<br><sub>2,5,3,1,1</sub> |  | 0.5 | 0.1 | 0.5 | 7.6 |
| Tyler Kolek | 93% | 13.2<br><sub>15,13,19,16,13</sub> | 4.2<br><sub>12,4,5,0,4</sub> |  | 1.8<br><sub>3,1,6,0,1</sub> |  | 3.6<br><sub>4,4,2,7,3</sub> |  | 0.4<br><sub>2,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 9.5 |
| Andre Drummond | 98% | 12.2<br><sub>16,14,14,7,11</sub> | 3.7<br><sub>2,0,0,2,2</sub> |  | 5.3<br><sub>14,4,6,3,8</sub> |  | 0.9<br><sub>3,3,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.9 |
| Jordan Clarkson | 88% | 9.7<br><sub>11,-,9,7,8</sub> | 4.3<br><sub>2,-,0,2,3</sub> |  | 1.4<br><sub>4,-,1,2,0</sub> |  | 0.6<br><sub>2,-,0,0,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 6.3 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Jose Alvarado | 66% | 8.0<br><sub>6,-,-,2,7</sub> | 3.1<br><sub>0,-,-,0,2</sub> |  | 1.1<br><sub>1,-,-,0,0</sub> |  | 1.3<br><sub>1,-,-,1,4</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.6 |
| Mohamed Diawara | 52% | 7.8<br><sub>18,11,-,-,-</sub> | 2.7<br><sub>5,2,-,-,-</sub> |  | 1.3<br><sub>3,0,-,-,-</sub> |  | 0.8<br><sub>3,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.8 |
| Jaden Akins | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 0.8 |
| Dalton Knecht | 64% | 6.6<br><sub>8,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.4 |
| James Wiseman | 48% | 6.2<br><sub>5,-,-,3,-</sub> | 2.2<br><sub>0,-,-,0,-</sub> |  | 2.0<br><sub>1,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.6 |
| Pacome Dadiet | 43% | 5.8<br><sub>6,-,1,-,-</sub> | 2.5<br><sub>8,-,0,-,-</sub> |  | 1.1<br><sub>2,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 36.9<br><sub>33,25,37,31,37</sub> | 17.6<br><sub>16,16,18,13,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>6,9,5,6,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,3,6,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.0 | 1.9 | 26.6 |
| Ayo Dosunmu | 99% | 35.9<br><sub>30,27,33,30,39</sub> | 19.2<br><sub>26,18,24,8,30</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>4,2,5,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.9<br><sub>1,1,0,2,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>4,2,0,2,7</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.5 | 2.1 | 27.7 |
| LaMelo Ball | 99% | 32.4<br><sub>30,25,30,24,31</sub> | 20.4<br><sub>24,22,19,6,18</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>3,3,8,5,9</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.9<br><sub>5,9,6,0,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,6,4,2,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4 | 0.3 | 3.3 | 31.2 |
| Rudy Gobert | 98% | 31.3<br><sub>31,23,27,32,22</sub> | 8.7<br><sub>10,9,1,18,0</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 10.6<br><sub>15,6,10,15,4</sub> | 10.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,1,4,3,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.3 | 21.2 |
| Terrence Shannon Jr. | 98% | 27.6<br><sub>18,21,22,35,24</sub> | 13.9<br><sub>5,6,14,34,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>3,2,6,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>3,4,0,6,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.1 | 1.4 | 19.6 |
| Trey Lyles | 98% | 27.0<br><sub>21,15,19,19,31</sub> | 8.0<br><sub>9,2,5,9,8</sub> |  | 5.3<br><sub>6,0,1,3,7</sub> |  | 1.4<br><sub>2,0,2,1,4</sub> |  | 1.2<br><sub>1,0,0,2,2</sub> |  | 0.6 | 0.4 | 0.8 | 14.7 |
| Joan Beringer | 98% | 22.9<br><sub>16,22,13,16,26</sub> | 7.7<br><sub>4,13,2,0,3</sub> |  | 7.4<br><sub>3,9,5,4,13</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.6 | 0.8 | 15.8 |
| Bones Hyland | 98% | 18.4<br><sub>13,23,21,13,17</sub> | 9.6<br><sub>14,24,12,5,13</sub> |  | 1.9<br><sub>2,3,1,1,2</sub> |  | 2.7<br><sub>2,8,2,5,1</sub> |  | 1.5<br><sub>1,5,3,0,3</sub> |  | 0.7 | 0.3 | 1.1 | 14.2 |
| Cody Williams | 64% | 11.8<br><sub>2,7,-,4,13</sub> | 0.3<br><sub>0,0,-,0,0</sub> |  | 1.5<br><sub>0,1,-,1,1</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 2.4 |
| Rocco Zikarsky | 38% | 9.5<br><sub>2,-,-,-,-</sub> | 2.8<br><sub>0,-,-,-,-</sub> |  | 2.7<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.8 | 0.5 | 6.0 |
| Johni Broome | 3% | 8.3 | 2.9 |  | 2.0 |  | 0.6 |  | 0.2 |  | 0.3 | 0.2 | 0.3 | 5.5 |
| Isaiah Evans | 52% | 7.5<br><sub>2,8,-,4,-</sub> | 5.4<br><sub>0,2,-,0,-</sub> |  | 1.1<br><sub>0,1,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 6.9 |

</details>

<details><summary>if Jonathan Kuminga plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels (MIN) | 99% | 34.8<br><sub>33,25,37,31,37</sub> | 16.1<br><sub>16,16,18,13,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>6,9,5,6,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>3,3,6,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.0 | 1.7 | 24.7 |
| Ayo Dosunmu (MIN) | 99% | 33.8<br><sub>30,27,33,30,39</sub> | 17.6<br><sub>26,18,24,8,30</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>4,2,5,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>1,1,0,2,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>4,2,0,2,7</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.4 | 2.0 | 25.6 |
| Jonathan Kuminga (MIN) | 100% | 30.5<br><sub>25,24,35,29,-</sub> | 12.8<br><sub>4,14,11,13,-</sub> | 12.5 · – | 5.5<br><sub>0,8,3,9,-</sub> | 5.5 | 2.2<br><sub>0,5,3,1,-</sub> | 2.5 | 1.3<br><sub>0,1,0,1,-</sub> | 1.5 | 0.8 | 0.6 | 1.4 | 20.5 |
| LaMelo Ball (MIN) | 99% | 29.9<br><sub>30,25,30,24,31</sub> | 18.6<br><sub>24,22,19,6,18</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>3,3,8,5,9</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.5<br><sub>5,9,6,0,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>4,6,4,2,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.3 | 2.9 | 28.7 |
| Rudy Gobert (MIN) | 98% | 29.1<br><sub>31,23,27,32,22</sub> | 8.2<br><sub>10,9,1,18,0</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 9.8<br><sub>15,6,10,15,4</sub> | 10.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>2,1,4,3,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.3 | 1.3 | 19.7 |
| Terrence Shannon Jr. (MIN) | 98% | 24.3<br><sub>18,21,22,35,24</sub> | 12.2<br><sub>5,6,14,34,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,2,6,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>3,4,0,6,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.1 | 1.3 | 17.1 |
| Trey Lyles (MIN) | 98% | 21.9<br><sub>21,15,19,19,31</sub> | 6.5<br><sub>9,2,5,9,8</sub> |  | 4.3<br><sub>6,0,1,3,7</sub> |  | 1.2<br><sub>2,0,2,1,4</sub> |  | 0.9<br><sub>1,0,0,2,2</sub> |  | 0.5 | 0.4 | 0.6 | 12.0 |
| Joan Beringer (MIN) | 98% | 17.7<br><sub>16,22,13,16,26</sub> | 6.0<br><sub>4,13,2,0,3</sub> |  | 5.8<br><sub>3,9,5,4,13</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 12.3 |
| Bones Hyland (MIN) | 98% | 15.9<br><sub>13,23,21,13,17</sub> | 8.6<br><sub>14,24,12,5,13</sub> |  | 1.6<br><sub>2,3,1,1,2</sub> |  | 2.4<br><sub>2,8,2,5,1</sub> |  | 1.3<br><sub>1,5,3,0,3</sub> |  | 0.6 | 0.2 | 1.0 | 12.6 |
| Cody Williams (MIN) | 64% | 8.4<br><sub>2,7,-,4,13</sub> | 0.2<br><sub>0,0,-,0,0</sub> |  | 1.1<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 1.7 |
| Rocco Zikarsky (MIN) | 38% | 7.0<br><sub>2,-,-,-,-</sub> | 2.3<br><sub>0,-,-,-,-</sub> |  | 2.1<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.6 | 0.4 | 4.7 |
| Isaiah Evans (MIN) | 52% | 5.7<br><sub>2,8,-,4,-</sub> | 4.2<br><sub>0,2,-,0,-</sub> |  | 0.9<br><sub>0,1,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 5.4 |
| Johni Broome (MIN) | 3% | 5.5 | 2.1 |  | 1.2 |  | 0.4 |  | 0.1 |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Jalen Brunson (NYK) | 98% | 35.4<br><sub>28,35,36,41,34</sub> | 27.6<br><sub>23,27,33,28,31</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>4,3,1,1,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 6.2<br><sub>2,5,11,9,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,3,4,3,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.6 | 37.0 |
| OG Anunoby (NYK) | 98% | 34.7<br><sub>29,34,33,44,36</sub> | 16.4<br><sub>19,14,11,21,16</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>3,6,2,9,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>2,2,1,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>5,2,2,2,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.9 | 1.9 | 23.5 |
| Karl-Anthony Towns (NYK) | 98% | 34.2<br><sub>27,34,34,43,36</sub> | 20.9<br><sub>21,21,23,28,16</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 13.2<br><sub>16,11,15,17,16</sub> | 13.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>3,8,5,3,8</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,2,3,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.8 | 2.9 | 38.3 |
| Josh Hart (NYK) | 98% | 29.2<br><sub>-,26,23,26,31</sub> | 8.5<br><sub>-,6,0,0,5</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>-,4,5,5,4</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.5<br><sub>-,3,4,2,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>-,0,0,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.3 | 1.4 | 18.7 |
| Mikal Bridges (NYK) | 98% | 27.5<br><sub>17,17,29,32,30</sub> | 9.6<br><sub>4,2,18,5,17</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>5,1,3,7,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>1,2,3,3,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.0 | 0.5 | 1.0 | 15.3 |
| Landry Shamet (NYK) | 98% | 23.7<br><sub>28,29,21,30,24</sub> | 8.3<br><sub>10,12,5,23,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>3,2,3,2,1</sub> |  | 1.3<br><sub>2,4,1,0,1</sub> |  | 1.3<br><sub>2,2,1,4,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.2 | 0.7 | 11.3 |
| Miles McBride (NYK) | 98% | 15.4<br><sub>25,27,22,14,9</sub> | 5.2<br><sub>8,19,9,3,3</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 1.1<br><sub>3,2,1,0,1</sub> |  | 0.8<br><sub>2,5,3,1,1</sub> |  | 0.5 | 0.1 | 0.4 | 7.5 |
| Tyler Kolek (NYK) | 93% | 13.2<br><sub>15,13,19,16,13</sub> | 4.2<br><sub>12,4,5,0,4</sub> |  | 1.7<br><sub>3,1,6,0,1</sub> |  | 3.6<br><sub>4,4,2,7,3</sub> |  | 0.4<br><sub>2,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 9.5 |
| Andre Drummond (NYK) | 98% | 12.2<br><sub>16,14,14,7,11</sub> | 3.7<br><sub>2,0,0,2,2</sub> |  | 5.3<br><sub>14,4,6,3,8</sub> |  | 0.9<br><sub>3,3,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.9 |
| Jordan Clarkson (NYK) | 88% | 9.7<br><sub>11,-,9,7,8</sub> | 4.3<br><sub>2,-,0,2,3</sub> |  | 1.4<br><sub>4,-,1,2,0</sub> |  | 0.7<br><sub>2,-,0,0,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 6.3 |
| Tyler Nickel (NYK) | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Jose Alvarado (NYK) | 66% | 7.9<br><sub>6,-,-,2,7</sub> | 3.1<br><sub>0,-,-,0,2</sub> |  | 1.1<br><sub>1,-,-,0,0</sub> |  | 1.3<br><sub>1,-,-,1,4</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |
| Mohamed Diawara (NYK) | 52% | 7.8<br><sub>18,11,-,-,-</sub> | 2.6<br><sub>5,2,-,-,-</sub> |  | 1.3<br><sub>3,0,-,-,-</sub> |  | 0.8<br><sub>3,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.7 |
| Jaden Akins (NYK) | 38% | 6.7<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 0.8 |
| Dalton Knecht (NYK) | 64% | 6.7<br><sub>8,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.5 |
| James Wiseman (NYK) | 48% | 6.1<br><sub>5,-,-,3,-</sub> | 2.2<br><sub>0,-,-,0,-</sub> |  | 2.0<br><sub>1,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.6 |
| Pacome Dadiet (NYK) | 43% | 5.8<br><sub>6,-,1,-,-</sub> | 2.6<br><sub>8,-,0,-,-</sub> |  | 1.1<br><sub>2,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |

</details>


### LAC @ SAS
Out: Dylan Harper (SAS), Tobias Harris (SAS), Bradley Beal (LAC), Brandon Ingram (LAC)

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.1<br><sub>32,25,37,35,30</sub> | 20.4<br><sub>24,13,24,27,20</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>0,5,4,6,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>10,6,7,7,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>3,1,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.4 | 29.8 |
| Rui Hachimura | 98% | 27.7<br><sub>26,23,32,22,27</sub> | 12.5<br><sub>14,13,7,4,20</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>3,5,11,2,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>2,1,3,0,1</sub> |  | 1.6<br><sub>2,3,1,0,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.3 | 1.2 | 17.9 |
| Derrick Jones Jr. | 98% | 26.8<br><sub>29,24,29,26,28</sub> | 9.3<br><sub>8,11,14,13,5</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>4,3,5,4,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>3,0,0,1,1</sub> |  | 1.0<br><sub>0,2,4,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.8 | 0.9 | 14.1 |
| Brook Lopez | 98% | 24.3<br><sub>26,19,31,29,23</sub> | 12.6<br><sub>20,8,26,7,23</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,4,7,5,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>1,1,4,8,2</sub> |  | 1.4<br><sub>1,1,3,1,4</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.9 | 1.0 | 18.8 |
| Kris Dunn | 98% | 23.6<br><sub>24,19,20,18,26</sub> | 6.0<br><sub>14,3,2,7,2</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,2,3,3,5</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.4<br><sub>4,3,6,1,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>2,1,0,0,0</sub> |  | 1.4 | 0.3 | 1.0 | 12.6 |
| Max Strus | 98% | 21.7<br><sub>19,22,23,25,21</sub> | 7.7<br><sub>7,12,3,14,3</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>4,3,2,3,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,3,3,4,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>1,2,0,4,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.2 | 0.8 | 13.6 |
| Keaton Wagler | 98% | 21.0<br><sub>18,23,18,28,18</sub> | 10.3<br><sub>15,11,14,12,15</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>2,0,2,4,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>4,4,1,5,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>3,1,2,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.2 | 1.6 | 15.8 |
| Kobe Sanders | 98% | 19.7<br><sub>22,26,15,20,18</sub> | 7.1<br><sub>8,9,5,2,5</sub> |  | 2.2<br><sub>2,3,0,6,1</sub> |  | 1.9<br><sub>4,7,1,4,3</sub> |  | 0.9<br><sub>2,1,1,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.2 |
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
| Devin Vassell | 98% | 34.2<br><sub>-,-,23,32,36</sub> | 14.2<br><sub>-,-,7,6,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>-,-,2,6,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.4<br><sub>-,-,2,1,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>-,-,0,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.4 | 1.1 | 22.1 |
| Victor Wembanyama | 99% | 33.6<br><sub>25,32,21,35,34</sub> | 31.1<br><sub>40,32,12,26,25</sub> | 28.5 · –<br><sub>o 49% · u 51%</sub> | 13.1<br><sub>11,9,12,10,18</sub> | 11.5<br><sub>o 56% · u 44%</sub> | 4.0<br><sub>3,1,6,6,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>2,2,0,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 4.0 | 3.0 | 48.1 |
| Stephon Castle | 99% | 33.0<br><sub>30,29,25,35,31</sub> | 18.6<br><sub>4,11,32,20,10</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>8,1,5,4,2</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 7.2<br><sub>7,3,6,9,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>0,1,5,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.3 | 3.1 | 31.0 |
| De'Aaron Fox | 98% | 33.0<br><sub>29,31,17,-,34</sub> | 16.5<br><sub>15,17,7,-,6</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>9,4,5,-,2</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 6.5<br><sub>6,9,1,-,2</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,2,0,-,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.4 | 2.6 | 27.2 |
| Julian Champagnie | 99% | 29.0<br><sub>27,35,23,24,30</sub> | 10.5<br><sub>11,12,7,4,14</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>3,0,8,5,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,2,3,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>3,3,1,1,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.5 | 0.8 | 17.3 |
| Keldon Johnson | 99% | 24.9<br><sub>26,28,25,29,15</sub> | 10.7<br><sub>4,10,18,11,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,6,4,10,2</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>3,4,4,2,1</sub> |  | 0.7<br><sub>0,0,2,1,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 1.2 | 18.1 |
| Luke Kornet | 99% | 16.3<br><sub>13,14,16,13,14</sub> | 4.4<br><sub>2,7,6,2,2</sub> |  | 4.6<br><sub>4,5,7,2,1</sub> |  | 1.2<br><sub>1,1,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.6 | 10.2 |
| Harrison Barnes | 91% | 15.6<br><sub>21,13,21,14,10</sub> | 5.4<br><sub>11,3,11,0,0</sub> |  | 1.7<br><sub>2,1,1,0,3</sub> |  | 0.9<br><sub>0,0,1,2,4</sub> |  | 0.7<br><sub>2,1,3,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 8.0 |
| Jordan McLaughlin | 66% | 13.9<br><sub>11,2,14,19,-</sub> | 4.5<br><sub>4,4,4,10,-</sub> |  | 2.0<br><sub>4,0,6,1,-</sub> |  | 2.0<br><sub>2,0,2,2,-</sub> |  | 0.5<br><sub>0,0,0,2,-</sub> |  | 0.8 | 0.1 | 0.7 | 8.6 |
| Carter Bryant | 91% | 11.8<br><sub>14,15,19,5,2</sub> | 4.2<br><sub>8,10,8,0,0</sub> |  | 2.0<br><sub>1,1,3,1,0</sub> |  | 0.8<br><sub>1,2,2,0,0</sub> |  | 0.5<br><sub>2,2,2,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 6.9 |
| Tarris Reed Jr. | 58% | 8.8<br><sub>9,2,11,-,-</sub> | 3.1<br><sub>4,0,2,-,-</sub> |  | 3.2<br><sub>3,0,4,-,-</sub> |  | 0.4<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.7 |
| David Jones Garcia | 58% | 6.8<br><sub>8,2,-,-,-</sub> | 2.5<br><sub>2,0,-,-,-</sub> |  | 1.1<br><sub>0,0,-,-,-</sub> |  | 1.0<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 4.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-19/`._
