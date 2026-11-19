# NBA model · Thu 19 Nov 2026 (US date)

Updated **Thu 19 Nov, 11:53 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-19/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

2 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| POR @ MIL | player points | Jrue Holiday projected 20.2 pts vs DraftKings line 13.5 | minutes 32 vs 26 this season; scoring 0.62/min vs 0.50 this season, 0.56 last season; teammates out: Krejci, Morant, Sharpe, III (~95 min a game) |
| POR @ MIL | player points | Scoot Henderson projected 17.2 pts vs DraftKings line 11.5 | minutes 29 vs 22 this season; scoring 0.59/min vs 0.39 this season, 0.57 last season; teammates out: Krejci, Morant, Sharpe, III (~95 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey REB over 13.5 (14+) | GSW @ MEM | draftkings | 15.60 | 13.21 | 6.15 | 16.2% | 6.0% | 7.6% | +18.1% | +153.5% | 0.3% |
| Cameron Boozer AST over 9.5 (10+) | GSW @ MEM | draftkings | 19.60 | 17.36 | 8.93 | 11.2% | 4.8% | 5.8% | +12.9% | +119.5% | 0.2% |
| Devin Vassell PA over 24.5 (25+) | LAC @ SAS | draftkings | 13.00 | 11.89 | 6.62 | 15.1% | 7.2% | 8.4% | +9.3% | +96.5% | 0.2% |
| Victor Wembanyama PA over 54.5 (55+) | LAC @ SAS | draftkings | 26.00 | 24.04 | 13.73 | 7.3% | 3.6% | 4.2% | +8.2% | +89.4% | 0.1% |
| Victor Wembanyama PTS over 49.5 (50+) | LAC @ SAS | draftkings | 25.00 | 23.15 | 13.28 | 7.5% | 3.7% | 4.3% | +8.1% | +88.3% | 0.1% |
| Cameron Boozer AST over 7.5 (8+) | GSW @ MEM | draftkings | 6.68 | 6.18 | 3.55 | 28.1% | 14.0% | 16.2% | +8.0% | +88.0% | 0.4% |
| Devin Vassell AST over 5.5 (6+) | LAC @ SAS | draftkings | 12.80 | 12.03 | 7.21 | 13.9% | 7.3% | 8.3% | +6.4% | +77.5% | 0.1% |
| Victor Wembanyama PTS over 44.5 (45+) | LAC @ SAS | draftkings | 13.20 | 12.42 | 7.48 | 13.4% | 7.1% | 8.1% | +6.2% | +76.4% | 0.1% |
| Yaxel Lendeborg REB over 11.5 (12+) | GSW @ MEM | draftkings | 12.00 | 11.40 | 7.05 | 14.2% | 7.8% | 8.8% | +5.3% | +70.3% | 0.1% |
| Zach Edey PRA over 29.5 (30+) | GSW @ MEM | draftkings | 11.00 | 10.45 | 6.47 | 15.4% | 8.5% | 9.6% | +5.2% | +69.9% | 0.1% |
| Yaxel Lendeborg PRA over 49.5 (50+) | GSW @ MEM | draftkings | 15.40 | 14.66 | 9.12 | 11.0% | 6.1% | 6.8% | +5.1% | +68.8% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| GSW @ MEM | Fri 20 Nov 12:00 | 114.9–116.3 | GSW 46% | 2.16 / 1.86 | MEM -1.5 | 231.5 | MEM -6.5 covers 36%; o227.5 58% |
| POR @ MIL | Fri 20 Nov 12:00 | 115.0–111.1 | POR 61% | 1.64 / 2.56 | MIL +4.5 | 225.5 | MIL +10.5 covers 68%; o229.5 42% |
| NYK @ MIN | Fri 20 Nov 12:00 | 113.4–108.8 | NYK 63% | 1.59 / 2.68 | MIN +4.5 | 221.5 | MIN +1.5 covers 40%; o217.5 59% |
| LAC @ SAS | Fri 20 Nov 12:00 | 107.4–118.1 | LAC 22% | 4.48 / 1.29 | SAS -10.5 | 225.5 | SAS -15.5 covers 37%; o226.5 48% |

### GSW @ MEM
Out: GG Jackson (MEM), Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM), Jimmy Butler III (GSW), Stephen Curry (GSW), Al Horford (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 34.5<br><sub>37,27,36,24,33</sub> | 23.6<br><sub>23,23,25,3,28</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 8.0<br><sub>8,7,10,7,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>3,4,0,1,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>2,4,2,0,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.9 | 3.5 | 35.5 |
| Brandin Podziemski | 96% | 34.2<br><sub>39,26,37,22,30</sub> | 19.4<br><sub>15,25,22,8,15</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>7,2,6,3,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.8<br><sub>1,4,4,0,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,5,4,2,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.4 | 2.0 | 29.9 |
| Draymond Green | 96% | 28.8<br><sub>34,21,27,16,25</sub> | 6.8<br><sub>2,2,7,4,2</sub> |  | 6.0<br><sub>6,3,5,3,8</sub> |  | 6.7<br><sub>13,6,7,3,5</sub> |  | 0.8<br><sub>0,0,1,0,0</sub> |  | 1.1 | 0.9 | 2.7 | 19.4 |
| De'Anthony Melton | 98% | 25.1<br><sub>17,26,25,18,21</sub> | 13.8<br><sub>4,16,11,8,8</sub> |  | 4.2<br><sub>1,4,4,4,2</sub> |  | 3.0<br><sub>1,3,4,3,1</sub> |  | 1.9<br><sub>1,4,3,2,2</sub> |  | 1.5 | 0.5 | 1.8 | 21.1 |
| Will Richard | 98% | 23.9<br><sub>12,-,19,30,23</sub> | 7.6<br><sub>4,-,9,7,11</sub> |  | 3.0<br><sub>2,-,4,4,3</sub> |  | 1.6<br><sub>1,-,0,1,1</sub> |  | 0.9<br><sub>0,-,2,1,2</sub> |  | 1.2 | 0.3 | 0.9 | 12.2 |
| Georges Niang | 98% | 20.8<br><sub>25,19,19,15,14</sub> | 8.9<br><sub>11,9,5,5,0</sub> |  | 3.3<br><sub>2,2,5,3,4</sub> |  | 1.4<br><sub>1,2,0,2,2</sub> |  | 1.4<br><sub>3,1,1,1,0</sub> |  | 0.5 | 0.2 | 1.0 | 13.6 |
| LJ Cryer | 84% | 20.7<br><sub>-,20,18,24,24</sub> | 10.1<br><sub>-,10,13,20,7</sub> |  | 1.9<br><sub>-,0,1,2,1</sub> |  | 2.2<br><sub>-,3,1,6,3</sub> |  | 1.7<br><sub>-,2,3,6,1</sub> |  | 0.6 | 0.1 | 1.0 | 14.1 |
| Gui Santos | 91% | 20.4<br><sub>12,21,12,21,19</sub> | 9.1<br><sub>3,3,0,7,12</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>1,7,3,4,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>0,4,1,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8<br><sub>0,0,0,1,1</sub> |  | 0.8 | 0.4 | 1.4 | 15.3 |
| Charles Bassey | 98% | 17.0<br><sub>11,18,13,20,16</sub> | 8.3<br><sub>8,12,7,11,4</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>4,10,6,5,0</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 1.1 | 15.9 |
| Gary Payton II | 88% | 16.4<br><sub>13,-,-,13,8</sub> | 7.5<br><sub>4,-,-,2,2</sub> |  | 3.0<br><sub>0,-,-,2,0</sub> |  | 1.4<br><sub>0,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.9 | 0.2 | 0.8 | 11.8 |
| Graham Ike | 91% | 11.6<br><sub>-,12,4,13,8</sub> | 4.9<br><sub>-,4,4,5,3</sub> |  | 3.0<br><sub>-,5,0,2,5</sub> |  | 1.2<br><sub>-,2,1,3,1</sub> |  | 0.3<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.4 | 0.6 | 9.2 |
| Malevy Leons | 67% | 10.1<br><sub>-,12,4,14,6</sub> | 3.0<br><sub>-,0,0,5,2</sub> |  | 1.9<br><sub>-,3,3,1,1</sub> |  | 0.6<br><sub>-,0,0,0,0</sub> |  | 0.1<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.4 | 0.4 | 5.4 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 33.1<br><sub>33,33,25,29,29</sub> | 18.3<br><sub>22,13,12,15,29</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 9.2<br><sub>7,11,10,8,7</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>8,5,3,5,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>0,2,1,0,7</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.7 | 3.5 | 33.6 |
| Cedric Coward | 98% | 30.5<br><sub>28,27,30,33,27</sub> | 16.0<br><sub>3,15,14,23,18</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>6,11,7,12,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,4,6,4,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.5 | 2.0 | 27.7 |
| Cam Spencer | 98% | 29.2<br><sub>17,20,24,34,32</sub> | 13.6<br><sub>7,15,14,17,12</sub> |  | 3.5<br><sub>2,3,2,1,6</sub> |  | 7.3<br><sub>4,3,5,8,9</sub> |  | 2.1<br><sub>1,3,3,3,1</sub> |  | 1.0 | 0.2 | 1.9 | 24.4 |
| Jaylen Wells | 98% | 28.9<br><sub>26,31,27,25,27</sub> | 12.5<br><sub>14,22,11,5,8</sub> | 9.5 · –<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>4,2,2,2,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>4,5,2,1,2</sub> |  | 0.9 | 0.1 | 1.1 | 17.6 |
| Javon Small | 97% | 27.3<br><sub>24,15,15,30,29</sub> | 13.3<br><sub>9,3,10,19,12</sub> |  | 3.9<br><sub>2,1,2,2,5</sub> |  | 5.5<br><sub>5,4,5,5,12</sub> |  | 1.8<br><sub>1,1,2,3,0</sub> |  | 1.0 | 0.3 | 1.9 | 22.7 |
| Jerami Grant | 98% | 25.9<br><sub>22,20,26,-,23</sub> | 13.2<br><sub>17,14,22,-,8</sub> |  | 2.6<br><sub>3,2,1,-,1</sub> |  | 2.0<br><sub>2,2,1,-,2</sub> |  | 1.7<br><sub>3,2,3,-,2</sub> |  | 0.7 | 0.7 | 1.5 | 17.8 |
| Zach Edey | 83% | 23.5<br><sub>23,20,-,-,21</sub> | 10.7<br><sub>8,2,-,-,23</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 9.5<br><sub>9,5,-,-,10</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>1,0,-,-,1</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.6 | 1.5 | 1.7 | 21.3 |
| Taylor Hendricks | 86% | 19.4<br><sub>16,11,19,29,19</sub> | 8.9<br><sub>9,7,10,22,9</sub> |  | 4.2<br><sub>3,2,12,5,3</sub> |  | 1.1<br><sub>0,1,2,4,0</sub> |  | 1.1<br><sub>1,1,2,0,1</sub> |  | 1.0 | 0.5 | 1.1 | 14.2 |
| Olivier-Maxence Prosper | 72% | 14.8<br><sub>1,-,2,20,16</sub> | 7.9<br><sub>0,-,6,11,12</sub> |  | 2.8<br><sub>0,-,1,4,0</sub> |  | 0.9<br><sub>0,-,0,0,1</sub> |  | 0.8<br><sub>0,-,0,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 11.6 |
| Kris Murray | 84% | 12.7<br><sub>1,-,1,19,6</sub> | 2.8<br><sub>0,-,0,3,0</sub> |  | 2.0<br><sub>0,-,1,2,1</sub> |  | 0.9<br><sub>0,-,0,3,0</sub> |  | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.3 | 0.5 | 5.8 |
| Quinten Post | 96% | 12.1<br><sub>2,-,-,-,9</sub> | 4.6<br><sub>0,-,-,-,5</sub> |  | 2.6<br><sub>1,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.7 |
| Jahmai Mashack | 58% | 9.3<br><sub>-,-,-,2,2</sub> | 3.0<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.4 |
| Karim Lopez | 63% | 7.3<br><sub>-,-,-,2,1</sub> | 2.9<br><sub>-,-,-,0,0</sub> |  | 1.6<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.0 |

</details>


### POR @ MIL
Out: Ousmane Dieng (MIL), Ryan Rollins (MIL), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Robert Williams III (POR), Chris Youngblood (POR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.0–111.1 | POR 61% | 1.64 / 2.56 | MIL +4.5 | 225.5 | MIL +10.5 covers 68%; o229.5 42% |
| Expected (weighted by chance each plays) | 116.5–110.6 | POR 66% | 1.51 / 2.98 | MIL +5.5 | 226.5 | MIL +10.5 covers 63%; o229.5 45% |
| if Toumani Camara plays | 115.3–110.7 | POR 63% | 1.59 / 2.70 | MIL +4.5 | 225.5 | MIL +10.5 covers 67%; o229.5 42% |
| if Deni Avdija plays | 117.8–110.5 | POR 70% | 1.43 / 3.30 | MIL +7.5 | 228.5 | MIL +10.5 covers 59%; o229.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Toumani Camara (POR) | Questionable | 55% | 33.7 | 14.8 | 5.1 | 2.3 | 2.5 | 1.3 | 0.6 | 1.5 | 22.3 | full tables below |
| Deni Avdija (POR) | Questionable | 55% | 35.2 | 27.7 | 7.0 | 6.7 | 2.1 | 1.0 | 0.6 | 3.5 | 41.5 | full tables below |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard | 98% | 33.8<br><sub>24,32,33,24,31</sub> | 25.5<br><sub>25,18,29,9,25</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>3,3,6,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.2 | 2.9 | 35.7 |
| Sidy Cissoko | 98% | 33.2<br><sub>33,29,26,28,32</sub> | 11.3<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,0,1,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.6<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.5 | 1.4 | 18.9 |
| Jrue Holiday | 98% | 32.5<br><sub>25,30,27,25,31</sub> | 20.2<br><sub>11,19,6,10,23</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>1,3,5,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.4<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.3 | 2.6 | 31.3 |
| Donovan Clingan | 98% | 30.3<br><sub>26,30,27,22,32</sub> | 15.9<br><sub>7,5,13,10,12</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 13.5<br><sub>13,12,11,10,12</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>1,1,1,0,0</sub> |  | 0.8 | 1.9 | 1.7 | 32.3 |
| Scoot Henderson | 98% | 29.1<br><sub>23,19,23,23,21</sub> | 17.2<br><sub>11,5,11,10,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.6 | 24.1 |
| Jayson Kent | 72% | 27.3<br><sub>-,-,11,11,27</sub> | 10.5<br><sub>-,-,3,8,8</sub> |  | 3.5<br><sub>-,-,1,0,3</sub> |  | 1.6<br><sub>-,-,0,0,0</sub> |  | 1.5<br><sub>-,-,1,2,2</sub> |  | 1.3 | 0.4 | 1.1 | 15.7 |
| Branden Carlson | 88% | 20.7<br><sub>8,10,8,14,14</sub> | 6.7<br><sub>2,0,5,5,6</sub> |  | 5.1<br><sub>5,2,3,6,1</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.7 | 0.8 | 0.9 | 12.8 |
| Micah Potter | 64% | 17.9<br><sub>5,-,-,7,1</sub> | 8.7<br><sub>0,-,-,2,0</sub> |  | 5.2<br><sub>3,-,-,4,0</sub> |  | 1.1<br><sub>0,-,-,1,0</sub> |  | 1.0<br><sub>0,-,-,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 15.1 |
| Yang Hansen | 52% | 17.8<br><sub>5,-,-,7,-</sub> | 7.2<br><sub>0,-,-,0,-</sub> |  | 4.7<br><sub>1,-,-,1,-</sub> |  | 1.2<br><sub>0,-,-,3,-</sub> |  | 0.6<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.5 | 1.2 | 13.1 |
| John Tonje | 47% | 17.6<br><sub>-,-,-,7,-</sub> | 9.5<br><sub>-,-,-,7,-</sub> |  | 3.6<br><sub>-,-,-,4,-</sub> |  | 1.7<br><sub>-,-,-,3,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.8 | 0.3 | 0.9 | 14.9 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 32.2<br><sub>27,-,35,34,20</sub> | 20.4<br><sub>13,-,27,18,5</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>1,-,2,1,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.8<br><sub>2,-,7,2,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,-,2,2,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.3 | 2.6 | 29.7 |
| Jaime Jaquez Jr. | 98% | 30.0<br><sub>23,25,30,28,30</sub> | 16.4<br><sub>4,16,25,22,6</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>2,5,5,6,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>2,3,3,4,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,2,2,5,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.4 | 26.2 |
| Myles Turner | 98% | 28.2<br><sub>24,27,-,31,23</sub> | 11.4<br><sub>3,3,-,14,8</sub> | 8.5 · –<br><sub>o 55% · u 45%</sub> | 5.8<br><sub>5,3,-,11,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>7,2,-,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>0,1,-,4,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 1.9 | 1.6 | 19.4 |
| Kyle Kuzma | 98% | 28.1<br><sub>31,26,24,31,22</sub> | 12.4<br><sub>27,5,9,14,14</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>4,5,1,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>0,3,1,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>6,1,1,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 2.1 | 20.2 |
| Brayden Burries | 98% | 26.2<br><sub>29,26,23,19,29</sub> | 10.7<br><sub>13,3,8,3,13</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>8,3,5,4,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>4,3,1,3,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.3 | 1.6 | 19.2 |
| Kel'el Ware | 97% | 20.7<br><sub>9,17,23,17,25</sub> | 10.2<br><sub>0,8,8,10,8</sub> |  | 6.9<br><sub>0,4,5,6,11</sub> |  | 1.2<br><sub>1,1,1,1,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6 | 1.3 | 1.6 | 18.3 |
| Gary Trent Jr. | 67% | 19.1<br><sub>-,6,4,16,30</sub> | 8.4<br><sub>-,5,6,1,18</sub> |  | 1.3<br><sub>-,0,1,0,2</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 1.3<br><sub>-,1,2,0,4</sub> |  | 0.8 | 0.1 | 0.7 | 10.6 |
| Kasparas Jakucionis | 80% | 18.8<br><sub>7,23,4,-,26</sub> | 7.8<br><sub>1,11,4,-,25</sub> |  | 2.5<br><sub>2,0,2,-,5</sub> |  | 3.2<br><sub>0,4,0,-,5</sub> |  | 0.8<br><sub>0,2,0,-,4</sub> |  | 0.8 | 0.2 | 1.6 | 13.5 |
| Nate Ament | 96% | 18.0<br><sub>23,22,22,22,17</sub> | 6.7<br><sub>12,10,2,9,5</sub> |  | 2.6<br><sub>5,2,4,3,2</sub> |  | 0.9<br><sub>1,1,1,1,1</sub> |  | 0.7<br><sub>2,2,0,2,1</sub> |  | 0.8 | 0.3 | 0.9 | 10.2 |
| AJ Green | 98% | 15.9<br><sub>18,8,8,8,6</sub> | 5.2<br><sub>5,0,3,0,0</sub> |  | 1.6<br><sub>1,0,1,0,0</sub> |  | 1.1<br><sub>1,0,1,2,0</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.9 |
| Cormac Ryan | 8% | 15.5 | 7.4 |  | 1.7 |  | 1.1 |  | 0.9 |  | 0.7 | 0.2 | 1.1 | 10.2 |
| Caris LeVert | 8% | 13.8<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.4 | 0.8 | 8.2 |
| Jericho Sims | 71% | 12.8<br><sub>15,8,18,-,11</sub> | 3.5<br><sub>2,2,0,-,4</sub> |  | 3.2<br><sub>2,0,4,-,2</sub> |  | 1.0<br><sub>0,0,1,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.8 | 7.7 |
| Kam Jones | 8% | 11.4 | 3.0 |  | 1.2 |  | 2.1 |  | 0.2 |  | 0.4 | 0.1 | 0.8 | 6.3 |
| Pete Nance | 93% | 9.4<br><sub>-,-,4,-,-</sub> | 3.0<br><sub>-,-,3,-,-</sub> |  | 1.5<br><sub>-,-,1,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.2 |
| Bogoljub Markovic | 51% | 6.8<br><sub>-,4,4,-,-</sub> | 3.0<br><sub>-,0,0,-,-</sub> |  | 1.6<br><sub>-,2,0,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>if Deni Avdija plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 32.1<br><sub>27,-,35,34,20</sub> | 20.4<br><sub>13,-,27,18,5</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>1,-,2,1,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.8<br><sub>2,-,7,2,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,-,2,2,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.3 | 2.6 | 29.5 |
| Jaime Jaquez Jr. (MIL) | 98% | 30.0<br><sub>23,25,30,28,30</sub> | 16.4<br><sub>4,16,25,22,6</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>2,5,5,6,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>2,3,3,4,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,2,2,5,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.4 | 26.3 |
| Myles Turner (MIL) | 98% | 28.1<br><sub>24,27,-,31,23</sub> | 11.3<br><sub>3,3,-,14,8</sub> | 8.5 · –<br><sub>o 55% · u 45%</sub> | 5.8<br><sub>5,3,-,11,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>7,2,-,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>0,1,-,4,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 1.9 | 1.6 | 19.2 |
| Kyle Kuzma (MIL) | 98% | 28.0<br><sub>31,26,24,31,22</sub> | 12.2<br><sub>27,5,9,14,14</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>4,5,1,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>0,3,1,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>6,1,1,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 2.1 | 20.1 |
| Brayden Burries (MIL) | 98% | 26.2<br><sub>29,26,23,19,29</sub> | 10.6<br><sub>13,3,8,3,13</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>8,3,5,4,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>4,3,1,3,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.3 | 1.6 | 19.2 |
| Kel'el Ware (MIL) | 97% | 20.8<br><sub>9,17,23,17,25</sub> | 10.2<br><sub>0,8,8,10,8</sub> |  | 6.9<br><sub>0,4,5,6,11</sub> |  | 1.1<br><sub>1,1,1,1,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6 | 1.3 | 1.6 | 18.2 |
| Gary Trent Jr. (MIL) | 67% | 19.1<br><sub>-,6,4,16,30</sub> | 8.4<br><sub>-,5,6,1,18</sub> |  | 1.2<br><sub>-,0,1,0,2</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 1.3<br><sub>-,1,2,0,4</sub> |  | 0.8 | 0.1 | 0.7 | 10.5 |
| Kasparas Jakucionis (MIL) | 80% | 18.8<br><sub>7,23,4,-,26</sub> | 7.8<br><sub>1,11,4,-,25</sub> |  | 2.5<br><sub>2,0,2,-,5</sub> |  | 3.2<br><sub>0,4,0,-,5</sub> |  | 0.8<br><sub>0,2,0,-,4</sub> |  | 0.8 | 0.2 | 1.6 | 13.5 |
| Nate Ament (MIL) | 96% | 18.1<br><sub>23,22,22,22,17</sub> | 6.7<br><sub>12,10,2,9,5</sub> |  | 2.6<br><sub>5,2,4,3,2</sub> |  | 0.9<br><sub>1,1,1,1,1</sub> |  | 0.7<br><sub>2,2,0,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 10.2 |
| AJ Green (MIL) | 98% | 15.9<br><sub>18,8,8,8,6</sub> | 5.2<br><sub>5,0,3,0,0</sub> |  | 1.6<br><sub>1,0,1,0,0</sub> |  | 1.1<br><sub>1,0,1,2,0</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.9 |
| Cormac Ryan (MIL) | 8% | 15.8 | 7.6 |  | 1.7 |  | 1.1 |  | 1.0 |  | 0.7 | 0.2 | 1.1 | 10.4 |
| Caris LeVert (MIL) | 8% | 13.8<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.4 | 0.8 | 8.3 |
| Jericho Sims (MIL) | 71% | 12.7<br><sub>15,8,18,-,11</sub> | 3.5<br><sub>2,2,0,-,4</sub> |  | 3.2<br><sub>2,0,4,-,2</sub> |  | 1.0<br><sub>0,0,1,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.8 | 7.7 |
| Kam Jones (MIL) | 8% | 11.7 | 3.2 |  | 1.2 |  | 2.2 |  | 0.2 |  | 0.4 | 0.1 | 0.8 | 6.6 |
| Pete Nance (MIL) | 93% | 9.3<br><sub>-,-,4,-,-</sub> | 3.0<br><sub>-,-,3,-,-</sub> |  | 1.5<br><sub>-,-,1,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.2 |
| Bogoljub Markovic (MIL) | 51% | 6.8<br><sub>-,4,4,-,-</sub> | 3.0<br><sub>-,0,0,-,-</sub> |  | 1.6<br><sub>-,2,0,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 5.0 |
| Deni Avdija (POR) | 100% | 35.2<br><sub>34,35,35,30,-</sub> | 27.7<br><sub>24,28,34,27,-</sub> | 23.5 · – | 7.0<br><sub>6,3,6,8,-</sub> | 6.5 | 6.7<br><sub>8,6,4,4,-</sub> | 5.5 | 2.1<br><sub>2,4,3,3,-</sub> | 1.5 | 1.0 | 0.6 | 3.5 | 41.5 |
| Damian Lillard (POR) | 98% | 33.6<br><sub>24,32,33,24,31</sub> | 22.2<br><sub>25,18,29,9,25</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>3,3,6,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 2.3 | 31.4 |
| Jrue Holiday (POR) | 98% | 32.2<br><sub>25,30,27,25,31</sub> | 16.3<br><sub>11,19,6,10,23</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>1,3,5,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 5.5<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.3 | 2.0 | 26.5 |
| Sidy Cissoko (POR) | 98% | 31.7<br><sub>33,29,26,28,32</sub> | 9.3<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>3,0,1,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.5 | 1.1 | 16.2 |
| Donovan Clingan (POR) | 98% | 31.1<br><sub>26,30,27,22,32</sub> | 14.0<br><sub>7,5,13,10,12</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 13.6<br><sub>13,12,11,10,12</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,1,1,0,0</sub> |  | 0.8 | 2.2 | 1.3 | 30.0 |
| Scoot Henderson (POR) | 98% | 27.6<br><sub>23,19,23,23,21</sub> | 13.4<br><sub>11,5,11,10,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.2 | 2.1 | 19.0 |
| Jayson Kent (POR) | 72% | 21.6<br><sub>-,-,11,11,27</sub> | 7.7<br><sub>-,-,3,8,8</sub> |  | 2.8<br><sub>-,-,1,0,3</sub> |  | 1.3<br><sub>-,-,0,0,0</sub> |  | 1.0<br><sub>-,-,1,2,2</sub> |  | 1.0 | 0.3 | 0.7 | 11.8 |
| Branden Carlson (POR) | 88% | 16.1<br><sub>8,10,8,14,14</sub> | 4.7<br><sub>2,0,5,5,6</sub> |  | 3.9<br><sub>5,2,3,6,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.7 | 0.6 | 9.3 |
| Micah Potter (POR) | 64% | 12.9<br><sub>5,-,-,7,1</sub> | 5.5<br><sub>0,-,-,2,0</sub> |  | 3.8<br><sub>3,-,-,4,0</sub> |  | 0.7<br><sub>0,-,-,1,0</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.0 |
| Yang Hansen (POR) | 52% | 12.8<br><sub>5,-,-,7,-</sub> | 4.5<br><sub>0,-,-,0,-</sub> |  | 3.5<br><sub>1,-,-,1,-</sub> |  | 0.8<br><sub>0,-,-,3,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.8 | 8.8 |
| John Tonje (POR) | 47% | 11.7<br><sub>-,-,-,7,-</sub> | 4.5<br><sub>-,-,-,7,-</sub> |  | 2.6<br><sub>-,-,-,4,-</sub> |  | 1.3<br><sub>-,-,-,3,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.4 |

</details>

<details><summary>if Toumani Camara plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 32.2<br><sub>27,-,35,34,20</sub> | 20.3<br><sub>13,-,27,18,5</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>1,-,2,1,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.8<br><sub>2,-,7,2,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,-,2,2,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.3 | 2.6 | 29.5 |
| Jaime Jaquez Jr. (MIL) | 98% | 29.9<br><sub>23,25,30,28,30</sub> | 16.3<br><sub>4,16,25,22,6</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>2,5,5,6,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>2,3,3,4,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,2,2,5,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.4 | 26.1 |
| Myles Turner (MIL) | 98% | 28.2<br><sub>24,27,-,31,23</sub> | 11.4<br><sub>3,3,-,14,8</sub> | 8.5 · –<br><sub>o 55% · u 45%</sub> | 5.8<br><sub>5,3,-,11,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>7,2,-,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>0,1,-,4,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 1.9 | 1.6 | 19.4 |
| Kyle Kuzma (MIL) | 98% | 28.1<br><sub>31,26,24,31,22</sub> | 12.2<br><sub>27,5,9,14,14</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>4,5,1,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>0,3,1,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>6,1,1,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 2.1 | 20.1 |
| Brayden Burries (MIL) | 98% | 26.2<br><sub>29,26,23,19,29</sub> | 10.6<br><sub>13,3,8,3,13</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>8,3,5,4,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>4,3,1,3,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.3 | 1.5 | 19.1 |
| Kel'el Ware (MIL) | 97% | 20.7<br><sub>9,17,23,17,25</sub> | 10.1<br><sub>0,8,8,10,8</sub> |  | 6.9<br><sub>0,4,5,6,11</sub> |  | 1.1<br><sub>1,1,1,1,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6 | 1.3 | 1.6 | 18.2 |
| Gary Trent Jr. (MIL) | 67% | 19.2<br><sub>-,6,4,16,30</sub> | 8.4<br><sub>-,5,6,1,18</sub> |  | 1.3<br><sub>-,0,1,0,2</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 1.3<br><sub>-,1,2,0,4</sub> |  | 0.7 | 0.1 | 0.7 | 10.6 |
| Kasparas Jakucionis (MIL) | 80% | 18.9<br><sub>7,23,4,-,26</sub> | 7.9<br><sub>1,11,4,-,25</sub> |  | 2.5<br><sub>2,0,2,-,5</sub> |  | 3.2<br><sub>0,4,0,-,5</sub> |  | 0.8<br><sub>0,2,0,-,4</sub> |  | 0.8 | 0.2 | 1.6 | 13.6 |
| Nate Ament (MIL) | 96% | 18.1<br><sub>23,22,22,22,17</sub> | 6.7<br><sub>12,10,2,9,5</sub> |  | 2.6<br><sub>5,2,4,3,2</sub> |  | 0.9<br><sub>1,1,1,1,1</sub> |  | 0.7<br><sub>2,2,0,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 10.2 |
| AJ Green (MIL) | 98% | 15.9<br><sub>18,8,8,8,6</sub> | 5.2<br><sub>5,0,3,0,0</sub> |  | 1.6<br><sub>1,0,1,0,0</sub> |  | 1.1<br><sub>1,0,1,2,0</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.9 |
| Cormac Ryan (MIL) | 8% | 15.5 | 7.4 |  | 1.7 |  | 1.1 |  | 0.9 |  | 0.6 | 0.2 | 1.1 | 10.2 |
| Caris LeVert (MIL) | 8% | 13.9<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.4 | 0.8 | 8.2 |
| Jericho Sims (MIL) | 71% | 12.7<br><sub>15,8,18,-,11</sub> | 3.5<br><sub>2,2,0,-,4</sub> |  | 3.2<br><sub>2,0,4,-,2</sub> |  | 1.0<br><sub>0,0,1,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.8 | 7.7 |
| Kam Jones (MIL) | 8% | 11.5 | 3.2 |  | 1.2 |  | 2.1 |  | 0.2 |  | 0.4 | 0.1 | 0.8 | 6.5 |
| Pete Nance (MIL) | 93% | 9.4<br><sub>-,-,4,-,-</sub> | 3.0<br><sub>-,-,3,-,-</sub> |  | 1.5<br><sub>-,-,1,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.3 |
| Bogoljub Markovic (MIL) | 51% | 6.9<br><sub>-,4,4,-,-</sub> | 3.1<br><sub>-,0,0,-,-</sub> |  | 1.6<br><sub>-,2,0,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 5.1 |
| Toumani Camara (POR) | 100% | 33.7<br><sub>30,38,36,26,33</sub> | 14.8<br><sub>12,14,14,3,10</sub> | 13.5 · – | 5.1<br><sub>3,5,2,0,8</sub> | 4.5 | 2.3<br><sub>3,3,1,0,1</sub> |  | 2.5<br><sub>2,2,2,0,2</sub> | 2.5 | 1.3 | 0.6 | 1.5 | 22.3 |
| Damian Lillard (POR) | 98% | 33.4<br><sub>24,32,33,24,31</sub> | 23.8<br><sub>25,18,29,9,25</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>3,3,2,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>3,3,6,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>4,2,6,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 2.6 | 33.7 |
| Jrue Holiday (POR) | 98% | 32.2<br><sub>25,30,27,25,31</sub> | 18.7<br><sub>11,19,6,10,23</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>1,3,5,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.2<br><sub>2,5,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>2,5,0,2,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.3 | 2.4 | 29.6 |
| Sidy Cissoko (POR) | 98% | 31.9<br><sub>33,29,26,28,32</sub> | 10.0<br><sub>17,19,3,5,6</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>3,2,4,4,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>3,0,1,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>3,4,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.5 | 1.3 | 17.2 |
| Donovan Clingan (POR) | 98% | 30.6<br><sub>26,30,27,22,32</sub> | 14.8<br><sub>7,5,13,10,12</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 13.2<br><sub>13,12,11,10,12</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>3,2,2,1,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,1,1,0,0</sub> |  | 0.8 | 2.2 | 1.5 | 30.7 |
| Scoot Henderson (POR) | 98% | 28.2<br><sub>23,19,23,23,21</sub> | 15.3<br><sub>11,5,11,10,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>1,2,0,1,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,2,1,0,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>3,1,2,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.3 | 21.7 |
| Jayson Kent (POR) | 72% | 22.9<br><sub>-,-,11,11,27</sub> | 8.5<br><sub>-,-,3,8,8</sub> |  | 3.0<br><sub>-,-,1,0,3</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 1.1<br><sub>-,-,1,2,2</sub> |  | 1.1 | 0.3 | 0.9 | 12.9 |
| Branden Carlson (POR) | 88% | 16.6<br><sub>8,10,8,14,14</sub> | 5.3<br><sub>2,0,5,5,6</sub> |  | 4.2<br><sub>5,2,3,6,1</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 0.4<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.7 | 0.7 | 10.3 |
| Micah Potter (POR) | 64% | 13.1<br><sub>5,-,-,7,1</sub> | 5.8<br><sub>0,-,-,2,0</sub> |  | 3.9<br><sub>3,-,-,4,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.5 |
| Yang Hansen (POR) | 52% | 13.0<br><sub>5,-,-,7,-</sub> | 5.0<br><sub>0,-,-,0,-</sub> |  | 3.6<br><sub>1,-,-,1,-</sub> |  | 0.9<br><sub>0,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.9 | 9.4 |
| John Tonje (POR) | 47% | 12.1<br><sub>-,-,-,7,-</sub> | 4.9<br><sub>-,-,-,7,-</sub> |  | 2.7<br><sub>-,-,-,4,-</sub> |  | 1.4<br><sub>-,-,-,3,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.2 | 0.7 | 9.0 |

</details>


### NYK @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.4–108.8 | NYK 63% | 1.59 / 2.68 | MIN +4.5 | 221.5 | MIN +1.5 covers 40%; o217.5 59% |
| Expected (weighted by chance each plays) | 113.3–109.0 | NYK 62% | 1.62 / 2.61 | MIN +4.5 | 221.5 | MIN +1.5 covers 41%; o217.5 60% |
| if Jonathan Kuminga plays | 113.3–109.4 | NYK 61% | 1.64 / 2.55 | MIN +4.5 | 222.5 | MIN +1.5 covers 42%; o217.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jonathan Kuminga (MIN) | Questionable | 55% | 30.4 | 12.9 | 5.5 | 2.1 | 1.3 | 0.8 | 0.6 | 1.4 | 20.5 | full tables below |
| Zyon Pullin (MIN) | Questionable | 55% | 8.1 | 3.0 | 0.8 | 0.9 | 0.1 | 0.2 | 0.1 | 0.5 | 4.7 | small |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 35.4<br><sub>28,35,36,41,34</sub> | 27.4<br><sub>23,27,33,28,31</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,3,1,1,5</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 6.1<br><sub>2,5,11,9,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>1,3,4,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 2.6 | 36.8 |
| OG Anunoby | 98% | 34.6<br><sub>29,34,33,44,36</sub> | 16.3<br><sub>19,14,11,21,16</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>3,6,2,9,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>2,2,1,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>5,2,2,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.5 | 1.0 | 1.9 | 23.5 |
| Karl-Anthony Towns | 98% | 34.2<br><sub>27,34,34,43,36</sub> | 20.7<br><sub>21,21,23,28,16</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 13.3<br><sub>16,11,15,17,16</sub> | 12.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>3,8,5,3,8</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>2,2,3,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.8 | 3.0 | 38.2 |
| Josh Hart | 98% | 29.1<br><sub>-,26,23,26,31</sub> | 8.5<br><sub>-,6,0,0,5</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 6.7<br><sub>-,4,5,5,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 3.4<br><sub>-,3,4,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>-,0,0,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.3 | 1.4 | 18.6 |
| Mikal Bridges | 98% | 27.5<br><sub>17,17,29,32,30</sub> | 9.6<br><sub>4,2,18,5,17</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,1,3,7,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>1,2,3,3,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.5 | 1.0 | 15.2 |
| Landry Shamet | 98% | 23.6<br><sub>28,29,21,30,24</sub> | 8.2<br><sub>10,12,5,23,12</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,2,3,2,1</sub> |  | 1.3<br><sub>2,4,1,0,1</sub> |  | 1.3<br><sub>2,2,1,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 0.2 | 0.7 | 11.3 |
| Miles McBride | 98% | 15.3<br><sub>25,27,22,14,9</sub> | 5.2<br><sub>8,19,9,3,3</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 1.1<br><sub>3,2,1,0,1</sub> |  | 0.8<br><sub>2,5,3,1,1</sub> |  | 0.5 | 0.1 | 0.4 | 7.5 |
| Tyler Kolek | 93% | 13.3<br><sub>15,13,19,16,13</sub> | 4.2<br><sub>12,4,5,0,4</sub> |  | 1.7<br><sub>3,1,6,0,1</sub> |  | 3.5<br><sub>4,4,2,7,3</sub> |  | 0.4<br><sub>2,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.5 |
| Andre Drummond | 98% | 12.2<br><sub>16,14,14,7,11</sub> | 3.7<br><sub>2,0,0,2,2</sub> |  | 5.3<br><sub>14,4,6,3,8</sub> |  | 0.9<br><sub>3,3,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.8 |
| Jordan Clarkson | 88% | 9.6<br><sub>11,-,9,7,8</sub> | 4.3<br><sub>2,-,0,2,3</sub> |  | 1.4<br><sub>4,-,1,2,0</sub> |  | 0.6<br><sub>2,-,0,0,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 6.3 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jose Alvarado | 66% | 7.9<br><sub>6,-,-,2,7</sub> | 3.1<br><sub>0,-,-,0,2</sub> |  | 1.1<br><sub>1,-,-,0,0</sub> |  | 1.3<br><sub>1,-,-,1,4</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.6 |
| Mohamed Diawara | 52% | 7.8<br><sub>18,11,-,-,-</sub> | 2.6<br><sub>5,2,-,-,-</sub> |  | 1.3<br><sub>3,0,-,-,-</sub> |  | 0.8<br><sub>3,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.7 |
| Jaden Akins | 38% | 6.7<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 0.8 |
| Dalton Knecht | 64% | 6.7<br><sub>8,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.5 |
| James Wiseman | 48% | 6.1<br><sub>5,-,-,3,-</sub> | 2.2<br><sub>0,-,-,0,-</sub> |  | 2.0<br><sub>1,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.6 |
| Pacome Dadiet | 43% | 5.8<br><sub>6,-,1,-,-</sub> | 2.5<br><sub>8,-,0,-,-</sub> |  | 1.1<br><sub>2,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 37.0<br><sub>33,25,37,31,37</sub> | 17.6<br><sub>16,16,18,13,22</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>6,9,5,6,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,3,6,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.0 | 1.9 | 26.6 |
| Ayo Dosunmu | 99% | 35.9<br><sub>30,27,33,30,39</sub> | 19.3<br><sub>26,18,24,8,30</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>4,2,5,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.9<br><sub>1,1,0,2,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>4,2,0,2,7</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.4 | 2.1 | 27.8 |
| LaMelo Ball | 99% | 32.3<br><sub>30,25,30,24,31</sub> | 20.3<br><sub>24,22,19,6,18</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>3,3,8,5,9</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.9<br><sub>5,9,6,0,2</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,6,4,2,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.3 | 3.2 | 31.0 |
| Rudy Gobert | 98% | 31.3<br><sub>31,23,27,32,22</sub> | 8.7<br><sub>10,9,1,18,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 10.5<br><sub>15,6,10,15,4</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,1,4,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.2 | 1.3 | 21.1 |
| Terrence Shannon Jr. | 98% | 27.5<br><sub>18,21,22,35,24</sub> | 13.8<br><sub>5,6,14,34,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,2,6,3,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>3,4,0,6,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.2 | 1.4 | 19.5 |
| Trey Lyles | 98% | 27.0<br><sub>21,15,19,19,31</sub> | 8.1<br><sub>9,2,5,9,8</sub> |  | 5.3<br><sub>6,0,1,3,7</sub> |  | 1.4<br><sub>2,0,2,1,4</sub> |  | 1.2<br><sub>1,0,0,2,2</sub> |  | 0.6 | 0.5 | 0.8 | 14.8 |
| Joan Beringer | 98% | 23.0<br><sub>16,22,13,16,26</sub> | 7.7<br><sub>4,13,2,0,3</sub> |  | 7.5<br><sub>3,9,5,4,13</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.6 | 0.9 | 15.8 |
| Bones Hyland | 98% | 18.3<br><sub>13,23,21,13,17</sub> | 9.6<br><sub>14,24,12,5,13</sub> |  | 1.8<br><sub>2,3,1,1,2</sub> |  | 2.7<br><sub>2,8,2,5,1</sub> |  | 1.5<br><sub>1,5,3,0,3</sub> |  | 0.7 | 0.3 | 1.1 | 14.2 |
| Cody Williams | 64% | 11.9<br><sub>2,7,-,4,13</sub> | 0.3<br><sub>0,0,-,0,0</sub> |  | 1.5<br><sub>0,1,-,1,1</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 2.4 |
| Rocco Zikarsky | 38% | 9.4<br><sub>2,-,-,-,-</sub> | 2.8<br><sub>0,-,-,-,-</sub> |  | 2.7<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.8 | 0.5 | 5.9 |
| Johni Broome | 3% | 7.6 | 2.5 |  | 1.8 |  | 0.5 |  | 0.2 |  | 0.2 | 0.2 | 0.3 | 4.8 |
| Isaiah Evans | 52% | 7.5<br><sub>2,8,-,4,-</sub> | 5.5<br><sub>0,2,-,0,-</sub> |  | 1.1<br><sub>0,1,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 7.0 |

</details>

<details><summary>if Jonathan Kuminga plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels (MIN) | 99% | 34.8<br><sub>33,25,37,31,37</sub> | 16.0<br><sub>16,16,18,13,22</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>6,9,5,6,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>3,3,6,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.0 | 1.7 | 24.6 |
| Ayo Dosunmu (MIN) | 99% | 33.8<br><sub>30,27,33,30,39</sub> | 17.6<br><sub>26,18,24,8,30</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>4,2,5,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>1,1,0,2,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,2,0,2,7</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.4 | 2.0 | 25.5 |
| Jonathan Kuminga (MIN) | 100% | 30.4<br><sub>25,24,35,29,-</sub> | 12.9<br><sub>4,14,11,13,-</sub> | 13.5 · – | 5.5<br><sub>0,8,3,9,-</sub> | 5.5 | 2.1<br><sub>0,5,3,1,-</sub> | 2.5 | 1.3<br><sub>0,1,0,1,-</sub> | 1.5 | 0.8 | 0.6 | 1.4 | 20.5 |
| LaMelo Ball (MIN) | 99% | 29.9<br><sub>30,25,30,24,31</sub> | 18.6<br><sub>24,22,19,6,18</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>3,3,8,5,9</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>5,9,6,0,2</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>4,6,4,2,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 2.9 | 28.6 |
| Rudy Gobert (MIN) | 98% | 29.0<br><sub>31,23,27,32,22</sub> | 8.2<br><sub>10,9,1,18,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 9.7<br><sub>15,6,10,15,4</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>2,1,4,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.2 | 19.6 |
| Terrence Shannon Jr. (MIN) | 98% | 24.2<br><sub>18,21,22,35,24</sub> | 12.2<br><sub>5,6,14,34,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,2,6,3,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>3,4,0,6,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.1 | 1.2 | 17.2 |
| Trey Lyles (MIN) | 98% | 21.9<br><sub>21,15,19,19,31</sub> | 6.4<br><sub>9,2,5,9,8</sub> |  | 4.3<br><sub>6,0,1,3,7</sub> |  | 1.2<br><sub>2,0,2,1,4</sub> |  | 0.9<br><sub>1,0,0,2,2</sub> |  | 0.5 | 0.4 | 0.6 | 12.0 |
| Joan Beringer (MIN) | 98% | 17.8<br><sub>16,22,13,16,26</sub> | 6.1<br><sub>4,13,2,0,3</sub> |  | 5.8<br><sub>3,9,5,4,13</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 12.4 |
| Bones Hyland (MIN) | 98% | 15.9<br><sub>13,23,21,13,17</sub> | 8.6<br><sub>14,24,12,5,13</sub> |  | 1.6<br><sub>2,3,1,1,2</sub> |  | 2.4<br><sub>2,8,2,5,1</sub> |  | 1.3<br><sub>1,5,3,0,3</sub> |  | 0.6 | 0.2 | 1.0 | 12.6 |
| Cody Williams (MIN) | 64% | 8.4<br><sub>2,7,-,4,13</sub> | 0.2<br><sub>0,0,-,0,0</sub> |  | 1.1<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 1.7 |
| Rocco Zikarsky (MIN) | 38% | 7.0<br><sub>2,-,-,-,-</sub> | 2.3<br><sub>0,-,-,-,-</sub> |  | 2.1<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.6 | 0.4 | 4.7 |
| Isaiah Evans (MIN) | 52% | 5.7<br><sub>2,8,-,4,-</sub> | 4.1<br><sub>0,2,-,0,-</sub> |  | 0.8<br><sub>0,1,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 5.3 |
| Johni Broome (MIN) | 3% | 5.5 | 2.1 |  | 1.3 |  | 0.3 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Jalen Brunson (NYK) | 98% | 35.5<br><sub>28,35,36,41,34</sub> | 27.5<br><sub>23,27,33,28,31</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,3,1,1,5</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>2,5,11,9,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,3,4,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 2.6 | 37.0 |
| OG Anunoby (NYK) | 98% | 34.7<br><sub>29,34,33,44,36</sub> | 16.3<br><sub>19,14,11,21,16</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>3,6,2,9,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>2,2,1,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>5,2,2,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.5 | 1.0 | 1.9 | 23.4 |
| Karl-Anthony Towns (NYK) | 98% | 34.2<br><sub>27,34,34,43,36</sub> | 20.8<br><sub>21,21,23,28,16</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 13.2<br><sub>16,11,15,17,16</sub> | 12.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>3,8,5,3,8</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>2,2,3,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.8 | 2.9 | 38.2 |
| Josh Hart (NYK) | 98% | 29.1<br><sub>-,26,23,26,31</sub> | 8.5<br><sub>-,6,0,0,5</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 6.7<br><sub>-,4,5,5,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>-,3,4,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>-,0,0,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.3 | 1.4 | 18.7 |
| Mikal Bridges (NYK) | 98% | 27.6<br><sub>17,17,29,32,30</sub> | 9.7<br><sub>4,2,18,5,17</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,1,3,7,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>1,2,3,3,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>0,0,2,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.5 | 1.0 | 15.3 |
| Landry Shamet (NYK) | 98% | 23.7<br><sub>28,29,21,30,24</sub> | 8.2<br><sub>10,12,5,23,12</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,2,3,2,1</sub> |  | 1.3<br><sub>2,4,1,0,1</sub> |  | 1.3<br><sub>2,2,1,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 0.2 | 0.7 | 11.3 |
| Miles McBride (NYK) | 98% | 15.4<br><sub>25,27,22,14,9</sub> | 5.1<br><sub>8,19,9,3,3</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 1.1<br><sub>3,2,1,0,1</sub> |  | 0.8<br><sub>2,5,3,1,1</sub> |  | 0.5 | 0.1 | 0.5 | 7.5 |
| Tyler Kolek (NYK) | 93% | 13.3<br><sub>15,13,19,16,13</sub> | 4.3<br><sub>12,4,5,0,4</sub> |  | 1.8<br><sub>3,1,6,0,1</sub> |  | 3.6<br><sub>4,4,2,7,3</sub> |  | 0.4<br><sub>2,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 9.6 |
| Andre Drummond (NYK) | 98% | 12.2<br><sub>16,14,14,7,11</sub> | 3.7<br><sub>2,0,0,2,2</sub> |  | 5.3<br><sub>14,4,6,3,8</sub> |  | 0.9<br><sub>3,3,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.9 |
| Jordan Clarkson (NYK) | 88% | 9.7<br><sub>11,-,9,7,8</sub> | 4.3<br><sub>2,-,0,2,3</sub> |  | 1.4<br><sub>4,-,1,2,0</sub> |  | 0.6<br><sub>2,-,0,0,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 6.3 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Jose Alvarado (NYK) | 66% | 7.9<br><sub>6,-,-,2,7</sub> | 3.1<br><sub>0,-,-,0,2</sub> |  | 1.1<br><sub>1,-,-,0,0</sub> |  | 1.3<br><sub>1,-,-,1,4</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.6 |
| Mohamed Diawara (NYK) | 52% | 7.8<br><sub>18,11,-,-,-</sub> | 2.6<br><sub>5,2,-,-,-</sub> |  | 1.3<br><sub>3,0,-,-,-</sub> |  | 0.8<br><sub>3,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.7 |
| Dalton Knecht (NYK) | 64% | 6.7<br><sub>8,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.4 |
| Jaden Akins (NYK) | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 0.8 |
| James Wiseman (NYK) | 48% | 6.1<br><sub>5,-,-,3,-</sub> | 2.2<br><sub>0,-,-,0,-</sub> |  | 2.0<br><sub>1,-,-,3,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.6 |
| Pacome Dadiet (NYK) | 43% | 5.8<br><sub>6,-,1,-,-</sub> | 2.6<br><sub>8,-,0,-,-</sub> |  | 1.2<br><sub>2,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |

</details>


### LAC @ SAS
Out: Dylan Harper (SAS), Tobias Harris (SAS), Bradley Beal (LAC), Brandon Ingram (LAC)

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.1<br><sub>32,25,37,35,30</sub> | 20.4<br><sub>24,13,24,27,20</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>0,5,4,6,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 6.6<br><sub>10,6,7,7,7</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>3,1,3,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 3.4 | 29.8 |
| Rui Hachimura | 98% | 27.7<br><sub>26,23,32,22,27</sub> | 12.6<br><sub>14,13,7,4,20</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,5,11,2,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>2,1,3,0,1</sub> |  | 1.6<br><sub>2,3,1,0,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.3 | 1.2 | 18.1 |
| Derrick Jones Jr. | 98% | 26.9<br><sub>29,24,29,26,28</sub> | 9.2<br><sub>8,11,14,13,5</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,3,5,4,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>3,0,0,1,1</sub> |  | 1.1<br><sub>0,2,4,3,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.8 | 0.9 | 14.2 |
| Brook Lopez | 98% | 24.4<br><sub>26,19,31,29,23</sub> | 12.6<br><sub>20,8,26,7,23</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>7,4,7,5,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>1,1,4,8,2</sub> |  | 1.4<br><sub>1,1,3,1,4</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.9 | 1.0 | 18.9 |
| Kris Dunn | 98% | 23.6<br><sub>24,19,20,18,26</sub> | 6.0<br><sub>14,3,2,7,2</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>5,2,3,3,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.4<br><sub>4,3,6,1,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>2,1,0,0,0</sub> |  | 1.4 | 0.3 | 1.0 | 12.6 |
| Max Strus | 98% | 21.7<br><sub>19,22,23,25,21</sub> | 7.8<br><sub>7,12,3,14,3</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>4,3,2,3,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>2,3,3,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,2,0,4,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.2 | 0.8 | 13.7 |
| Keaton Wagler | 98% | 21.0<br><sub>18,23,18,28,18</sub> | 10.3<br><sub>15,11,14,12,15</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>2,0,2,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>4,4,1,5,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>3,1,2,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.2 | 1.6 | 15.8 |
| Kobe Sanders | 98% | 19.6<br><sub>22,26,15,20,18</sub> | 7.0<br><sub>8,9,5,2,5</sub> |  | 2.2<br><sub>2,3,0,6,1</sub> |  | 1.9<br><sub>4,7,1,4,3</sub> |  | 0.8<br><sub>2,1,1,0,0</sub> |  | 0.7 | 0.1 | 1.1 | 11.2 |
| Isaiah Jackson | 98% | 17.0<br><sub>-,16,17,15,19</sub> | 7.0<br><sub>-,4,5,13,8</sub> |  | 4.6<br><sub>-,4,3,2,5</sub> |  | 1.3<br><sub>-,0,3,2,0</sub> |  | 0.1<br><sub>-,0,0,1,0</sub> |  | 0.7 | 0.9 | 1.0 | 12.9 |
| Gradey Dick | 98% | 15.7<br><sub>17,19,19,19,17</sub> | 6.5<br><sub>15,10,13,12,0</sub> |  | 2.2<br><sub>4,3,3,2,0</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.5<br><sub>2,1,2,2,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.5 |
| Yanic Konan Niederhauser | 3% | 12.7 | 5.6 |  | 2.3 |  | 1.2 |  | 0.4 |  | 0.4 | 0.3 | 0.7 | 9.1 |
| Baba Miller | 86% | 9.8<br><sub>20,16,-,5,4</sub> | 4.4<br><sub>12,13,-,2,3</sub> |  | 1.6<br><sub>5,4,-,0,0</sub> |  | 1.0<br><sub>4,0,-,0,0</sub> |  | 0.2<br><sub>0,1,-,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 6.9 |
| Jalen Pickett | 48% | 7.1<br><sub>2,8,-,-,-</sub> | 2.8<br><sub>0,3,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.0<br><sub>0,1,-,-,-</sub> |  | 0.2<br><sub>0,1,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.7 |
| Cam Christie | 52% | 6.7<br><sub>2,-,-,-,4</sub> | 2.9<br><sub>0,-,-,-,3</sub> |  | 1.0<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley | 52% | 6.3<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 98% | 34.1<br><sub>-,-,23,32,36</sub> | 14.2<br><sub>-,-,7,6,12</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>-,-,2,6,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 3.3<br><sub>-,-,2,1,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>-,-,0,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.4 | 1.1 | 22.1 |
| Victor Wembanyama | 99% | 33.5<br><sub>25,32,21,35,34</sub> | 31.1<br><sub>40,32,12,26,25</sub> | 29.5 · –<br><sub>o 50% · u 50%</sub> | 13.1<br><sub>11,9,12,10,18</sub> | 11.5<br><sub>o 55% · u 45%</sub> | 4.0<br><sub>3,1,6,6,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>2,2,0,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 4.0 | 3.0 | 48.1 |
| Stephon Castle | 99% | 33.0<br><sub>30,29,25,35,31</sub> | 18.6<br><sub>4,11,32,20,10</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>8,1,5,4,2</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 7.2<br><sub>7,3,6,9,7</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,1,5,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 3.1 | 31.0 |
| De'Aaron Fox | 98% | 33.0<br><sub>29,31,17,-,34</sub> | 16.6<br><sub>15,17,7,-,6</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>9,4,5,-,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.5<br><sub>6,9,1,-,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,2,0,-,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.4 | 2.6 | 27.3 |
| Julian Champagnie | 99% | 29.1<br><sub>27,35,23,24,30</sub> | 10.6<br><sub>11,12,7,4,14</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>3,0,8,5,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,3,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>3,3,1,1,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.5 | 0.8 | 17.4 |
| Keldon Johnson | 99% | 24.9<br><sub>26,28,25,29,15</sub> | 10.6<br><sub>4,10,18,11,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,6,4,10,2</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>3,4,4,2,1</sub> |  | 0.7<br><sub>0,0,2,1,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 1.2 | 18.0 |
| Luke Kornet | 99% | 16.3<br><sub>13,14,16,13,14</sub> | 4.4<br><sub>2,7,6,2,2</sub> |  | 4.6<br><sub>4,5,7,2,1</sub> |  | 1.2<br><sub>1,1,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.6 | 10.2 |
| Harrison Barnes | 91% | 15.7<br><sub>21,13,21,14,10</sub> | 5.4<br><sub>11,3,11,0,0</sub> |  | 1.7<br><sub>2,1,1,0,3</sub> |  | 0.9<br><sub>0,0,1,2,4</sub> |  | 0.7<br><sub>2,1,3,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 8.1 |
| Jordan McLaughlin | 66% | 13.9<br><sub>11,2,14,19,-</sub> | 4.5<br><sub>4,4,4,10,-</sub> |  | 2.0<br><sub>4,0,6,1,-</sub> |  | 2.0<br><sub>2,0,2,2,-</sub> |  | 0.5<br><sub>0,0,0,2,-</sub> |  | 0.8 | 0.1 | 0.7 | 8.5 |
| Carter Bryant | 91% | 11.9<br><sub>14,15,19,5,2</sub> | 4.2<br><sub>8,10,8,0,0</sub> |  | 2.0<br><sub>1,1,3,1,0</sub> |  | 0.8<br><sub>1,2,2,0,0</sub> |  | 0.5<br><sub>2,2,2,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 6.9 |
| Tarris Reed Jr. | 58% | 8.7<br><sub>9,2,11,-,-</sub> | 3.1<br><sub>4,0,2,-,-</sub> |  | 3.2<br><sub>3,0,4,-,-</sub> |  | 0.4<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.7 |
| David Jones Garcia | 58% | 6.8<br><sub>8,2,-,-,-</sub> | 2.5<br><sub>2,0,-,-,-</sub> |  | 1.1<br><sub>0,0,-,-,-</sub> |  | 1.0<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 4.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-19/`._
