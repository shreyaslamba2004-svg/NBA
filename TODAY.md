# NBA model · Sun 22 Nov 2026 (US date)

Updated **Mon 23 Nov, 11:24 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-22/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson PTS over 49.5 (50+) | IND @ NYK | draftkings | 31.00 | 24.27 | 9.84 | 10.2% | 3.0% | 4.1% | +27.6% | +215.0% | 0.2% |
| Jayson Tatum PRA over 59.5 (60+) | BOS @ GSW | draftkings | 17.00 | 15.95 | 9.50 | 10.5% | 5.5% | 6.3% | +6.6% | +79.0% | 0.1% |
| Jayson Tatum REB over 11.5 (12+) | BOS @ GSW | draftkings | 9.60 | 9.12 | 5.65 | 17.7% | 9.7% | 11.0% | +5.2% | +70.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Landry Shamet PTS over 11.5 (12+) | IND @ NYK | draftkings | 2.11 | Karl-Anthony Towns | 68.7% | 55.8% | +5.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| IND @ NYK | Mon 23 Nov 12:00 | 106.0–112.9 | IND 31% | 3.22 / 1.45 | NYK -6.5 | 218.5 | NYK -7.5 covers 48%; o212.5 63% |
| BOS @ GSW | Mon 23 Nov 12:30 | 112.2–104.9 | BOS 70% | 1.43 / 3.31 | GSW +7.5 | 216.5 | GSW +7.5 covers 50%; o210.5 64% |

### IND @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Miles McBride (NYK), Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.0–112.9 | IND 31% | 3.22 / 1.45 | NYK -6.5 | 218.5 | NYK -7.5 covers 48%; o212.5 63% |
| Expected (weighted by chance each plays) | 106.5–114.2 | IND 29% | 3.47 / 1.41 | NYK -7.5 | 220.5 | NYK -7.5 covers 51%; o212.5 66% |
| if Karl-Anthony Towns plays | 106.3–115.2 | IND 26% | 3.77 / 1.36 | NYK -8.5 | 221.5 | NYK -7.5 covers 54%; o212.5 68% |
| if Pascal Siakam plays | 106.7–113.5 | IND 32% | 3.17 / 1.46 | NYK -6.5 | 219.5 | NYK -7.5 covers 48%; o212.5 66% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Karl-Anthony Towns (NYK) | Questionable | 55% | 34.1 | 23.2 | 14.5 | 4.5 | 2.0 | 1.1 | 0.8 | 2.8 | 42.1 | full tables below |
| Pascal Siakam (IND) | Questionable | 55% | 33.8 | 21.6 | 6.0 | 3.8 | 1.6 | 0.9 | 0.4 | 2.0 | 31.4 | full tables below |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 91% | 34.3<br><sub>34,34,-,-,26</sub> | 17.8<br><sub>17,12,-,-,12</sub> | 14.5 · 14.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.8 | 29.0 |
| Aaron Nesmith | 93% | 31.8<br><sub>22,33,36,29,29</sub> | 13.9<br><sub>2,18,12,2,2</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.6 | 20.4 |
| Kelly Oubre Jr. | 91% | 27.8<br><sub>34,30,29,23,23</sub> | 12.8<br><sub>14,16,16,17,17</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.3<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.2 | 18.4 |
| Ivica Zubac | 88% | 27.5<br><sub>31,26,22,24,27</sub> | 12.0<br><sub>20,12,8,4,21</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 9.2<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.6 | 23.2 |
| Quenton Jackson | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 0.9 | 0.2 | 1.6 | 18.1 |
| Obi Toppin | 88% | 24.1<br><sub>16,16,14,17,26</sub> | 12.9<br><sub>8,9,5,6,17</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,3,2,1,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.2 | 19.7 |
| Jarace Walker | 88% | 20.1<br><sub>7,-,14,17,11</sub> | 8.4<br><sub>1,-,2,1,8</sub> |  | 4.1<br><sub>1,-,5,3,1</sub> |  | 2.0<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.5 |
| Jalen Slawson | 91% | 17.8<br><sub>12,10,14,12,14</sub> | 5.5<br><sub>2,1,8,5,4</sub> |  | 3.5<br><sub>3,4,5,4,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.6 |
| Braden Smith | 67% | 16.4<br><sub>-,-,-,18,11</sub> | 5.6<br><sub>-,-,-,8,5</sub> |  | 1.7<br><sub>-,-,-,5,3</sub> |  | 3.2<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 10.5 |
| Jay Huff | 91% | 15.9<br><sub>11,8,18,15,1</sub> | 6.9<br><sub>6,8,11,5,0</sub> |  | 2.9<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.9<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.8 |
| Larry Nance Jr. | 97% | 15.4<br><sub>5,14,7,9,11</sub> | 5.2<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.7<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.9 |
| Kobe Brown | 86% | 14.5<br><sub>-,-,3,2,-</sub> | 5.2<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.9 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 35.6<br><sub>36,41,34,35,36</sub> | 34.1<br><sub>33,28,31,21,30</sub> | 27.5 · 28.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,1,5,2,7</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 6.5<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>4,3,4,4,6</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 2.2 | 44.4 |
| Landry Shamet | 99% | 33.9<br><sub>21,30,24,30,36</sub> | 15.2<br><sub>5,23,12,10,20</sub> | 10.5 · 11.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>3,2,1,1,1</sub> |  | 2.3<br><sub>1,0,1,2,3</sub> |  | 2.7<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 1.1 | 20.3 |
| Josh Hart | 98% | 31.9<br><sub>23,26,31,28,35</sub> | 11.1<br><sub>0,0,5,11,0</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>5,5,4,6,8</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.3 | 1.6 | 23.3 |
| Mikal Bridges | 99% | 31.7<br><sub>29,32,30,31,28</sub> | 14.1<br><sub>18,5,17,8,12</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.6 | 1.2 | 21.5 |
| Andre Drummond | 99% | 26.3<br><sub>14,7,11,15,23</sub> | 8.3<br><sub>0,2,2,4,7</sub> |  | 12.6<br><sub>6,3,8,4,13</sub> |  | 1.8<br><sub>0,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.9 | 1.0 | 1.2 | 22.7 |
| James Wiseman | 52% | 22.4<br><sub>-,3,-,-,25</sub> | 7.7<br><sub>-,0,-,-,5</sub> |  | 7.6<br><sub>-,3,-,-,6</sub> |  | 1.3<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.5 | 1.0 | 1.1 | 16.5 |
| Tyler Kolek | 96% | 22.2<br><sub>19,16,13,12,13</sub> | 8.6<br><sub>5,0,4,6,7</sub> |  | 3.2<br><sub>6,0,1,3,3</sub> |  | 5.7<br><sub>2,7,3,5,0</sub> |  | 1.1<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.2 | 1.1 | 17.4 |
| Jose Alvarado | 80% | 20.4<br><sub>-,2,7,13,15</sub> | 8.6<br><sub>-,0,2,2,8</sub> |  | 2.7<br><sub>-,0,0,2,2</sub> |  | 3.3<br><sub>-,1,4,1,2</sub> |  | 1.2<br><sub>-,0,0,0,2</sub> |  | 1.0 | 0.2 | 1.1 | 14.6 |
| Mohamed Diawara | 38% | 18.9<br><sub>-,-,-,-,-</sub> | 7.3<br><sub>-,-,-,-,-</sub> |  | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.7 | 12.5 |
| Dalton Knecht | 67% | 17.7<br><sub>-,-,-,-,3</sub> | 6.9<br><sub>-,-,-,-,0</sub> |  | 3.4<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.4 | 11.2 |
| Pacome Dadiet | 52% | 17.0<br><sub>1,-,-,-,11</sub> | 7.0<br><sub>0,-,-,-,5</sub> |  | 3.1<br><sub>0,-,-,-,0</sub> |  | 1.1<br><sub>0,-,-,-,2</sub> |  | 0.9<br><sub>0,-,-,-,1</sub> |  | 0.5 | 0.2 | 0.5 | 11.2 |
| Jaden Akins | 38% | 11.2<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.4 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>if Karl-Anthony Towns plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 34.2<br><sub>34,34,-,-,26</sub> | 17.7<br><sub>17,12,-,-,12</sub> | 14.5 · 14.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.8 | 28.9 |
| Aaron Nesmith (IND) | 93% | 31.8<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.6 | 20.4 |
| Kelly Oubre Jr. (IND) | 91% | 27.8<br><sub>34,30,29,23,23</sub> | 12.8<br><sub>14,16,16,17,17</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.3<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.3 | 18.4 |
| Ivica Zubac (IND) | 88% | 27.4<br><sub>31,26,22,24,27</sub> | 12.0<br><sub>20,12,8,4,21</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.5 | 23.2 |
| Quenton Jackson (IND) | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 0.9 | 0.2 | 1.6 | 18.2 |
| Obi Toppin (IND) | 88% | 24.1<br><sub>16,16,14,17,26</sub> | 12.9<br><sub>8,9,5,6,17</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,3,2,1,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.2 | 19.7 |
| Jarace Walker (IND) | 88% | 20.2<br><sub>7,-,14,17,11</sub> | 8.5<br><sub>1,-,2,1,8</sub> |  | 4.1<br><sub>1,-,5,3,1</sub> |  | 2.0<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.6 |
| Jalen Slawson (IND) | 91% | 17.8<br><sub>12,10,14,12,14</sub> | 5.6<br><sub>2,1,8,5,4</sub> |  | 3.4<br><sub>3,4,5,4,2</sub> |  | 1.6<br><sub>1,0,2,2,2</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.7 |
| Braden Smith (IND) | 67% | 16.5<br><sub>-,-,-,18,11</sub> | 5.6<br><sub>-,-,-,8,5</sub> |  | 1.8<br><sub>-,-,-,5,3</sub> |  | 3.2<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 10.5 |
| Jay Huff (IND) | 91% | 15.7<br><sub>11,8,18,15,1</sub> | 6.7<br><sub>6,8,11,5,0</sub> |  | 2.8<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.8<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.6 |
| Larry Nance Jr. (IND) | 97% | 15.3<br><sub>5,14,7,9,11</sub> | 5.1<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.6<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.8 |
| Kobe Brown (IND) | 86% | 14.4<br><sub>-,-,3,2,-</sub> | 5.1<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.8 |
| Jalen Brunson (NYK) | 99% | 36.0<br><sub>36,41,34,35,36</sub> | 31.8<br><sub>33,28,31,21,30</sub> | 27.5 · 28.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,1,5,2,7</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 6.5<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>4,3,4,4,6</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 2.2 | 41.9 |
| Karl-Anthony Towns (NYK) | 100% | 34.1<br><sub>34,43,36,33,-</sub> | 23.2<br><sub>23,28,16,22,-</sub> | 21.5 · 20.5 | 14.5<br><sub>15,17,16,12,-</sub> | 12.5 | 4.5<br><sub>5,3,8,4,-</sub> | 3.5 | 2.0<br><sub>3,3,1,2,-</sub> | 1.5 | 1.1 | 0.8 | 2.8 | 42.1 |
| Josh Hart (NYK) | 98% | 32.5<br><sub>23,26,31,28,35</sub> | 9.8<br><sub>0,0,5,11,0</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>5,5,4,6,8</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.3 | 1.4 | 21.4 |
| Landry Shamet (NYK) | 99% | 32.5<br><sub>21,30,24,30,36</sub> | 13.0<br><sub>5,23,12,10,20</sub> | 10.5 · 11.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>3,2,1,1,1</sub> |  | 2.0<br><sub>1,0,1,2,3</sub> |  | 2.4<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 0.9 | 17.3 |
| Mikal Bridges (NYK) | 99% | 31.4<br><sub>29,32,30,31,28</sub> | 12.2<br><sub>18,5,17,8,12</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.5 | 1.1 | 18.7 |
| Andre Drummond (NYK) | 99% | 19.1<br><sub>14,7,11,15,23</sub> | 5.8<br><sub>0,2,2,4,7</sub> |  | 8.9<br><sub>6,3,8,4,13</sub> |  | 1.3<br><sub>0,0,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.6 | 0.7 | 0.9 | 16.0 |
| Tyler Kolek (NYK) | 96% | 17.7<br><sub>19,16,13,12,13</sub> | 6.2<br><sub>5,0,4,6,7</sub> |  | 2.4<br><sub>6,0,1,3,3</sub> |  | 4.5<br><sub>2,7,3,5,0</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.9 | 13.1 |
| Jose Alvarado (NYK) | 80% | 16.7<br><sub>-,2,7,13,15</sub> | 6.2<br><sub>-,0,2,2,8</sub> |  | 2.1<br><sub>-,0,0,2,2</sub> |  | 2.6<br><sub>-,1,4,1,2</sub> |  | 0.8<br><sub>-,0,0,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 10.9 |
| James Wiseman (NYK) | 52% | 16.1<br><sub>-,3,-,-,25</sub> | 5.2<br><sub>-,0,-,-,5</sub> |  | 5.4<br><sub>-,3,-,-,6</sub> |  | 0.8<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.8 | 0.9 | 11.3 |
| Mohamed Diawara (NYK) | 38% | 14.4<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 8.6 |
| Pacome Dadiet (NYK) | 52% | 12.1<br><sub>1,-,-,-,11</sub> | 4.8<br><sub>0,-,-,-,5</sub> |  | 2.0<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,2</sub> |  | 0.6<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 7.6 |
| Dalton Knecht (NYK) | 67% | 11.3<br><sub>-,-,-,-,3</sub> | 4.0<br><sub>-,-,-,-,0</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 6.7 |
| Tyler Nickel (NYK) | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Jaden Akins (NYK) | 38% | 8.2<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |

</details>

<details><summary>if Pascal Siakam plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam (IND) | 100% | 33.8<br><sub>32,32,34,33,30</sub> | 21.6<br><sub>28,19,31,24,21</sub> | 19.5 · 20.5 | 6.0<br><sub>8,3,2,4,7</sub> | 5.5 | 3.8<br><sub>5,2,2,3,2</sub> | 2.5 | 1.6<br><sub>2,2,0,2,2</sub> | 1.5 | 0.9 | 0.4 | 2.0 | 31.4 |
| Andrew Nembhard (IND) | 91% | 33.0<br><sub>34,34,-,-,26</sub> | 15.6<br><sub>17,12,-,-,12</sub> | 14.5 · 14.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.3 | 26.2 |
| Aaron Nesmith (IND) | 93% | 29.3<br><sub>22,33,36,29,29</sub> | 11.7<br><sub>2,18,12,2,2</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,1,4,3,7</sub> |  | 1.7<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.2 | 17.5 |
| Ivica Zubac (IND) | 88% | 26.1<br><sub>31,26,22,24,27</sub> | 11.0<br><sub>20,12,8,4,21</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.4 | 21.0 |
| Kelly Oubre Jr. (IND) | 91% | 25.3<br><sub>34,30,29,23,23</sub> | 10.9<br><sub>14,16,16,17,17</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>1,0,2,0,0</sub> |  | 1.2<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.1 | 16.0 |
| Quenton Jackson (IND) | 98% | 21.0<br><sub>21,20,30,22,18</sub> | 8.9<br><sub>4,3,15,15,3</sub> |  | 2.8<br><sub>2,5,6,2,2</sub> |  | 3.0<br><sub>2,4,8,3,2</sub> |  | 0.9<br><sub>1,1,1,2,1</sub> |  | 0.8 | 0.2 | 1.3 | 14.8 |
| Obi Toppin (IND) | 88% | 19.7<br><sub>16,16,14,17,26</sub> | 10.2<br><sub>8,9,5,6,17</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,3,2,1,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>1,1,1,1,2</sub> |  | 1.2<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.5 | 0.2 | 0.9 | 15.6 |
| Jarace Walker (IND) | 88% | 15.5<br><sub>7,-,14,17,11</sub> | 6.0<br><sub>1,-,2,1,8</sub> |  | 3.1<br><sub>1,-,5,3,1</sub> |  | 1.4<br><sub>0,-,2,1,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.2 | 0.8 | 10.5 |
| Jalen Slawson (IND) | 91% | 13.4<br><sub>12,10,14,12,14</sub> | 3.9<br><sub>2,1,8,5,4</sub> |  | 2.6<br><sub>3,4,5,4,2</sub> |  | 1.2<br><sub>1,0,2,2,2</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 0.6 | 7.8 |
| Braden Smith (IND) | 67% | 13.3<br><sub>-,-,-,18,11</sub> | 4.4<br><sub>-,-,-,8,5</sub> |  | 1.5<br><sub>-,-,-,5,3</sub> |  | 2.5<br><sub>-,-,-,3,5</sub> |  | 0.3<br><sub>-,-,-,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Jay Huff (IND) | 91% | 11.9<br><sub>11,8,18,15,1</sub> | 4.9<br><sub>6,8,11,5,0</sub> |  | 2.1<br><sub>4,1,0,3,0</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.6<br><sub>0,2,3,0,0</sub> |  | 0.2 | 0.7 | 0.5 | 7.8 |
| Larry Nance Jr. (IND) | 97% | 11.7<br><sub>5,14,7,9,11</sub> | 3.6<br><sub>5,2,4,3,7</sub> |  | 2.1<br><sub>0,2,2,1,2</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.4<br><sub>1,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.4 |
| Kobe Brown (IND) | 86% | 9.4<br><sub>-,-,3,2,-</sub> | 3.1<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Jalen Brunson (NYK) | 99% | 35.6<br><sub>36,41,34,35,36</sub> | 34.4<br><sub>33,28,31,21,30</sub> | 27.5 · 28.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,1,5,2,7</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 6.5<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>4,3,4,4,6</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 2.2 | 44.7 |
| Landry Shamet (NYK) | 99% | 33.8<br><sub>21,30,24,30,36</sub> | 15.3<br><sub>5,23,12,10,20</sub> | 10.5 · 11.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>3,2,1,1,1</sub> |  | 2.3<br><sub>1,0,1,2,3</sub> |  | 2.7<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 1.1 | 20.3 |
| Josh Hart (NYK) | 98% | 31.8<br><sub>23,26,31,28,35</sub> | 11.1<br><sub>0,0,5,11,0</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>5,5,4,6,8</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.3 | 1.6 | 23.3 |
| Mikal Bridges (NYK) | 99% | 31.7<br><sub>29,32,30,31,28</sub> | 14.2<br><sub>18,5,17,8,12</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.6 | 1.2 | 21.5 |
| Andre Drummond (NYK) | 99% | 26.3<br><sub>14,7,11,15,23</sub> | 8.4<br><sub>0,2,2,4,7</sub> |  | 12.6<br><sub>6,3,8,4,13</sub> |  | 1.8<br><sub>0,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.9 | 1.0 | 1.2 | 22.7 |
| James Wiseman (NYK) | 52% | 22.4<br><sub>-,3,-,-,25</sub> | 7.7<br><sub>-,0,-,-,5</sub> |  | 7.6<br><sub>-,3,-,-,6</sub> |  | 1.3<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.5 | 1.0 | 1.1 | 16.5 |
| Tyler Kolek (NYK) | 96% | 22.2<br><sub>19,16,13,12,13</sub> | 8.7<br><sub>5,0,4,6,7</sub> |  | 3.2<br><sub>6,0,1,3,3</sub> |  | 5.7<br><sub>2,7,3,5,0</sub> |  | 1.1<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.2 | 1.1 | 17.5 |
| Jose Alvarado (NYK) | 80% | 20.5<br><sub>-,2,7,13,15</sub> | 8.6<br><sub>-,0,2,2,8</sub> |  | 2.7<br><sub>-,0,0,2,2</sub> |  | 3.3<br><sub>-,1,4,1,2</sub> |  | 1.2<br><sub>-,0,0,0,2</sub> |  | 1.0 | 0.2 | 1.1 | 14.6 |
| Mohamed Diawara (NYK) | 38% | 18.8<br><sub>-,-,-,-,-</sub> | 7.2<br><sub>-,-,-,-,-</sub> |  | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.7 | 12.4 |
| Dalton Knecht (NYK) | 67% | 17.6<br><sub>-,-,-,-,3</sub> | 6.9<br><sub>-,-,-,-,0</sub> |  | 3.4<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.4 | 11.2 |
| Pacome Dadiet (NYK) | 52% | 17.1<br><sub>1,-,-,-,11</sub> | 7.1<br><sub>0,-,-,-,5</sub> |  | 3.1<br><sub>0,-,-,-,0</sub> |  | 1.1<br><sub>0,-,-,-,2</sub> |  | 1.0<br><sub>0,-,-,-,1</sub> |  | 0.5 | 0.2 | 0.5 | 11.3 |
| Jaden Akins (NYK) | 38% | 11.2<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.4 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>


### BOS @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW), Paul George (BOS), Mitchell Robinson (BOS)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 35.9<br><sub>38,30,36,37,-</sub> | 27.9<br><sub>24,32,24,24,-</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 8.5<br><sub>7,6,12,8,-</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>8,6,4,3,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>2,5,3,3,-</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.6 | 3.3 | 43.1 |
| Derrick White | 76% | 32.6<br><sub>38,23,32,35,-</sub> | 14.7<br><sub>19,16,9,12,-</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,4,3,3,-</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.8<br><sub>7,2,2,8,-</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,4,1,0,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.9 | 1.7 | 23.3 |
| Payton Pritchard | 99% | 32.4<br><sub>31,19,32,30,34</sub> | 16.9<br><sub>14,10,21,15,9</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>1,1,4,1,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.9<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.4 | 25.5 |
| Neemias Queta | 99% | 28.2<br><sub>31,15,-,27,30</sub> | 12.1<br><sub>11,8,-,17,15</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 9.3<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,-,3,1</sub> |  | 0.2<br><sub>1,1,-,0,1</sub> |  | 0.8 | 1.3 | 1.4 | 23.6 |
| Sam Hauser | 99% | 27.9<br><sub>24,11,25,17,31</sub> | 10.4<br><sub>8,8,12,9,14</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,0,2,2,2</sub> |  | 2.2<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.3 | 0.5 | 16.2 |
| Baylor Scheierman | 99% | 19.8<br><sub>29,18,11,13,18</sub> | 5.8<br><sub>9,12,0,0,4</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>7,5,1,1,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>3,3,1,1,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.1 | 0.7 | 10.9 |
| Luka Garza | 98% | 16.3<br><sub>11,14,18,5,17</sub> | 7.4<br><sub>5,2,3,0,5</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>1,3,0,1,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,5,4,1,1</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 12.6 |
| Jordan Walsh | 98% | 15.1<br><sub>18,21,17,4,8</sub> | 4.4<br><sub>6,11,6,0,1</sub> |  | 2.9<br><sub>3,1,2,0,4</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.5<br><sub>0,2,2,0,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.1 |
| Hugo Gonzalez | 98% | 15.0<br><sub>8,18,4,16,17</sub> | 4.4<br><sub>0,9,0,2,5</sub> |  | 3.1<br><sub>1,5,2,6,4</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.5<br><sub>0,2,0,0,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.2 |
| Mike Conley | 48% | 14.1<br><sub>-,-,-,-,18</sub> | 4.9<br><sub>-,-,-,-,19</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,4</sub> |  | 0.7 | 0.2 | 0.6 | 8.4 |
| Chris Cenac Jr. | 67% | 13.9<br><sub>-,7,12,17,12</sub> | 5.2<br><sub>-,6,4,6,2</sub> |  | 3.1<br><sub>-,3,2,6,3</sub> |  | 0.5<br><sub>-,0,1,0,0</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.7 | 8.8 |
| Devin Carter | 93% | 13.0<br><sub>-,12,-,-,4</sub> | 5.3<br><sub>-,0,-,-,0</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 1.5<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 9.2 |
| Ron Harper Jr. | 58% | 11.6<br><sub>-,12,-,-,13</sub> | 4.3<br><sub>-,10,-,-,3</sub> |  | 1.6<br><sub>-,1,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,1</sub> |  | 0.6<br><sub>-,2,-,-,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.6 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 32.8<br><sub>36,24,33,30,33</sub> | 18.4<br><sub>25,3,28,13,11</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.7 | 2.7 | 29.3 |
| Brandin Podziemski | 97% | 32.7<br><sub>37,22,30,29,32</sub> | 16.2<br><sub>22,8,15,10,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.6 | 25.3 |
| Draymond Green | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.7 | 2.2 | 16.0 |
| Will Richard | 98% | 23.4<br><sub>19,30,23,27,27</sub> | 8.3<br><sub>9,7,11,20,15</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.8 | 12.4 |
| De'Anthony Melton | 99% | 23.2<br><sub>25,18,21,19,25</sub> | 10.5<br><sub>11,8,8,0,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.4 | 1.5 | 16.5 |
| Gui Santos | 96% | 19.0<br><sub>12,21,19,17,23</sub> | 8.0<br><sub>0,7,12,6,8</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,1,2,6,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.3 | 1.2 | 13.9 |
| Charles Bassey | 98% | 17.8<br><sub>13,20,16,22,25</sub> | 8.0<br><sub>7,11,4,10,16</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.2 |
| Gary Payton II | 88% | 17.6<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.1<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.1 |
| Georges Niang | 98% | 17.5<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>5,3,4,1,2</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.3 | 0.1 | 0.8 | 11.3 |
| Al Horford | 98% | 16.8<br><sub>21,10,14,-,17</sub> | 5.5<br><sub>2,0,0,-,3</sub> | 5.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>1,3,5,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.3 | 0.7 | 0.6 | 10.8 |
| LJ Cryer | 88% | 14.7<br><sub>18,24,24,19,12</sub> | 6.7<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.5<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.7 | 9.4 |
| Graham Ike | 96% | 10.2<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.6 |
| Malevy Leons | 83% | 8.2<br><sub>4,14,6,7,4</sub> | 2.2<br><sub>0,5,2,2,0</sub> |  | 1.6<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-22/`._
