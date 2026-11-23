# NBA model · Sun 22 Nov 2026 (US date)

Updated **Mon 23 Nov, 11:54 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-22/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson PRA over 54.5 (55+) | IND @ NYK | draftkings | 16.00 | 13.62 | 6.41 | 15.6% | 5.8% | 7.3% | +17.5% | +149.6% | 0.3% |
| Jalen Brunson PA over 54.5 (55+) | IND @ NYK | draftkings | 24.00 | 20.45 | 9.64 | 10.4% | 3.9% | 4.9% | +17.4% | +148.9% | 0.2% |
| Jalen Brunson PRA over 59.5 (60+) | IND @ NYK | draftkings | 26.00 | 22.17 | 10.48 | 9.5% | 3.6% | 4.5% | +17.3% | +148.2% | 0.2% |
| Jalen Brunson PTS over 49.5 (50+) | IND @ NYK | draftkings | 31.00 | 26.60 | 12.71 | 7.9% | 3.0% | 3.8% | +16.6% | +144.0% | 0.1% |
| Jalen Brunson PTS over 44.5 (45+) | IND @ NYK | draftkings | 17.80 | 15.27 | 7.31 | 13.7% | 5.2% | 6.6% | +16.6% | +143.5% | 0.2% |
| Jalen Brunson PA over 49.5 (50+) | IND @ NYK | draftkings | 13.80 | 11.88 | 5.72 | 17.5% | 6.8% | 8.4% | +16.2% | +141.4% | 0.3% |
| Jalen Brunson PR over 49.5 (50+) | IND @ NYK | draftkings | 19.20 | 16.67 | 8.18 | 12.2% | 4.9% | 6.0% | +15.2% | +134.8% | 0.2% |
| Karl-Anthony Towns AST over 7.5 (8+) | IND @ NYK | draftkings | 22.00 | 19.49 | 10.05 | 10.0% | 4.2% | 5.1% | +12.8% | +118.9% | 0.1% |
| Jalen Brunson PR over 44.5 (45+) | IND @ NYK | draftkings | 10.00 | 9.04 | 4.89 | 20.5% | 9.3% | 11.1% | +10.6% | +104.6% | 0.3% |
| Jalen Brunson PRA over 49.5 (50+) | IND @ NYK | draftkings | 8.10 | 7.35 | 4.02 | 24.9% | 11.5% | 13.6% | +10.1% | +101.7% | 0.4% |
| Karl-Anthony Towns AST over 5.5 (6+) | IND @ NYK | draftkings | 6.77 | 6.21 | 3.48 | 28.7% | 13.8% | 16.1% | +9.0% | +94.4% | 0.4% |
| Jalen Brunson PTS over 39.5 (40+) | IND @ NYK | draftkings | 8.40 | 7.71 | 4.33 | 23.1% | 11.1% | 13.0% | +8.9% | +94.0% | 0.3% |
| Karl-Anthony Towns REB over 19.5 (20+) | IND @ NYK | draftkings | 12.00 | 11.16 | 6.49 | 15.4% | 7.8% | 9.0% | +7.5% | +84.9% | 0.2% |
| Jalen Brunson PA over 44.5 (45+) | IND @ NYK | draftkings | 6.57 | 6.14 | 3.62 | 27.6% | 14.2% | 16.3% | +7.0% | +81.3% | 0.3% |
| Jayson Tatum PRA over 59.5 (60+) | BOS @ GSW | draftkings | 17.00 | 15.95 | 9.50 | 10.5% | 5.5% | 6.3% | +6.6% | +79.0% | 0.1% |
| Karl-Anthony Towns REB over 17.5 (18+) | IND @ NYK | draftkings | 6.61 | 6.28 | 3.88 | 25.8% | 14.1% | 15.9% | +5.3% | +70.3% | 0.2% |
| Jayson Tatum REB over 11.5 (12+) | BOS @ GSW | draftkings | 9.60 | 9.12 | 5.65 | 17.7% | 9.7% | 11.0% | +5.2% | +70.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Obi Toppin PTS over 11.5 (12+) | IND @ NYK | draftkings | 2.38 | 2.19 | 3.10 | 32.3% | 48.1% | 45.7% | +8.7% | -23.2% | 1.6% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| IND @ NYK | Mon 23 Nov 12:00 | 107.3–115.2 | IND 29% | 3.49 / 1.40 | NYK -7.5 | 222.5 | NYK -6.5 covers 54%; o215.5 64% |
| BOS @ GSW | Mon 23 Nov 12:30 | 112.2–104.9 | BOS 70% | 1.43 / 3.31 | GSW +7.5 | 216.5 | GSW +8.5 covers 53%; o211.5 62% |

### IND @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Miles McBride (NYK), Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ivica Zubac PTS over 11.5 (12+) | IND @ NYK | draftkings | 2.16 | 2.09 | 2.56 | 39.1% | 49.5% | 47.9% | +3.4% | -15.6% | 0.7% |
| Jalen Brunson PTS over 29.5 (30+) | IND @ NYK | draftkings | 2.28 | 2.21 | 1.95 | 51.4% | 44.1% | 45.2% | +3.1% | +17.1% | 0.6% |
| Mikal Bridges PTS over 11.5 (12+) | IND @ NYK | pointsbetau | 2.00 | 2.00 | 2.00 | 50.1% | 50.0% | 50.0% | +0.0% | +0.2% | 0.0% |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 100% | 32.6<br><sub>32,32,34,33,30</sub> | 20.8<br><sub>28,19,31,24,21</sub> | 20.5 · 20.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>8,3,2,4,7</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>5,2,2,3,2</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 1.6<br><sub>2,2,0,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.4 | 2.0 | 30.2 |
| Andrew Nembhard | 100% | 31.8<br><sub>34,34,-,-,26</sub> | 14.9<br><sub>17,12,-,-,12</sub> | 13.5 · 14.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 7.5<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.2 | 25.1 |
| Aaron Nesmith | 100% | 28.5<br><sub>22,33,36,29,29</sub> | 11.4<br><sub>2,18,12,2,2</sub> | 11.5 · 12.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,1,4,3,7</sub> |  | 1.6<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 0.5 | 1.2 | 17.0 |
| Ivica Zubac | 100% | 25.7<br><sub>31,26,22,24,27</sub> | 10.8<br><sub>20,12,8,4,21</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 8.2<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 1.4 | 20.6 |
| Kelly Oubre Jr. | 100% | 25.6<br><sub>34,30,29,23,23</sub> | 10.7<br><sub>14,16,16,17,17</sub> | 11.5 · 12.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>6,5,4,4,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,0,2,0,0</sub> |  | 1.2<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.1 | 15.9 |
| Quenton Jackson | 98% | 20.6<br><sub>21,20,30,22,18</sub> | 8.7<br><sub>4,3,15,15,3</sub> |  | 2.8<br><sub>2,5,6,2,2</sub> |  | 2.9<br><sub>2,4,8,3,2</sub> |  | 0.9<br><sub>1,1,1,2,1</sub> |  | 0.8 | 0.2 | 1.3 | 14.4 |
| Obi Toppin | 88% | 19.2<br><sub>16,16,14,17,26</sub> | 9.8<br><sub>8,9,5,6,17</sub> | 9.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>3,3,2,1,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,1,1,1,2</sub> |  | 1.2<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.2 | 0.9 | 15.0 |
| Jarace Walker | 88% | 14.9<br><sub>7,-,14,17,11</sub> | 5.7<br><sub>1,-,2,1,8</sub> |  | 3.0<br><sub>1,-,5,3,1</sub> |  | 1.4<br><sub>0,-,2,1,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.2 | 0.8 | 10.1 |
| Jalen Slawson | 91% | 13.4<br><sub>12,10,14,12,14</sub> | 3.9<br><sub>2,1,8,5,4</sub> |  | 2.7<br><sub>3,4,5,4,2</sub> |  | 1.2<br><sub>1,0,2,2,2</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 0.6 | 7.8 |
| Braden Smith | 67% | 13.0<br><sub>-,-,-,18,11</sub> | 4.2<br><sub>-,-,-,8,5</sub> |  | 1.5<br><sub>-,-,-,5,3</sub> |  | 2.4<br><sub>-,-,-,3,5</sub> |  | 0.3<br><sub>-,-,-,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 8.1 |
| Larry Nance Jr. | 97% | 11.5<br><sub>5,14,7,9,11</sub> | 3.6<br><sub>5,2,4,3,7</sub> |  | 2.1<br><sub>0,2,2,1,2</sub> |  | 0.6<br><sub>0,1,2,0,0</sub> |  | 0.4<br><sub>1,0,1,1,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.4 |
| Jay Huff | 91% | 11.4<br><sub>11,8,18,15,1</sub> | 4.7<br><sub>6,8,11,5,0</sub> |  | 2.0<br><sub>4,1,0,3,0</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>0,2,3,0,0</sub> |  | 0.2 | 0.7 | 0.5 | 7.5 |
| Kobe Brown | 86% | 8.0<br><sub>-,-,3,2,-</sub> | 2.6<br><sub>-,-,0,0,-</sub> |  | 1.4<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 100% | 35.8<br><sub>36,41,34,35,36</sub> | 31.5<br><sub>33,28,31,21,30</sub> | 27.5 · 28.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,1,5,2,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 6.5<br><sub>11,9,5,7,5</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 3.1<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.2 | 2.2 | 41.5 |
| Karl-Anthony Towns | 100% | 34.0<br><sub>34,43,36,33,-</sub> | 22.9<br><sub>23,28,16,22,-</sub> | 20.5 · 20.5<br><sub>o 52% · u 48%</sub> | 14.6<br><sub>15,17,16,12,-</sub> | 12.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>5,3,8,4,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>3,3,1,2,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.8 | 2.8 | 41.9 |
| Landry Shamet | 100% | 33.1<br><sub>21,30,24,30,36</sub> | 13.1<br><sub>5,23,12,10,20</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>3,2,1,1,1</sub> |  | 2.0<br><sub>1,0,1,2,3</sub> |  | 2.4<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.2 | 0.9 | 17.4 |
| Josh Hart | 100% | 32.3<br><sub>23,26,31,28,35</sub> | 9.7<br><sub>0,0,5,11,0</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>5,5,4,6,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.5 | 21.3 |
| Mikal Bridges | 100% | 31.4<br><sub>29,32,30,31,28</sub> | 12.3<br><sub>18,5,17,8,12</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 1.1 | 18.9 |
| Andre Drummond | 99% | 18.7<br><sub>14,7,11,15,23</sub> | 5.7<br><sub>0,2,2,4,7</sub> |  | 8.7<br><sub>6,3,8,4,13</sub> |  | 1.2<br><sub>0,0,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.6 | 0.7 | 0.9 | 15.7 |
| Tyler Kolek | 96% | 17.6<br><sub>19,16,13,12,13</sub> | 6.1<br><sub>5,0,4,6,7</sub> |  | 2.4<br><sub>6,0,1,3,3</sub> |  | 4.5<br><sub>2,7,3,5,0</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.5 | 0.2 | 0.9 | 13.0 |
| Jose Alvarado | 80% | 16.7<br><sub>-,2,7,13,15</sub> | 6.2<br><sub>-,0,2,2,8</sub> |  | 2.1<br><sub>-,0,0,2,2</sub> |  | 2.6<br><sub>-,1,4,1,2</sub> |  | 0.8<br><sub>-,0,0,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 10.9 |
| James Wiseman | 52% | 16.0<br><sub>-,3,-,-,25</sub> | 5.1<br><sub>-,0,-,-,5</sub> |  | 5.3<br><sub>-,3,-,-,6</sub> |  | 0.8<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.8 | 0.9 | 11.3 |
| Mohamed Diawara | 38% | 14.2<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 8.6 |
| Pacome Dadiet | 52% | 12.0<br><sub>1,-,-,-,11</sub> | 4.7<br><sub>0,-,-,-,5</sub> |  | 2.0<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,2</sub> |  | 0.6<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 7.5 |
| Dalton Knecht | 67% | 11.2<br><sub>-,-,-,-,3</sub> | 4.0<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 6.6 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Jaden Akins | 38% | 8.1<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.1 |

</details>


### BOS @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW), Paul George (BOS), Mitchell Robinson (BOS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sam Hauser PTS over 8.5 (9+) | BOS @ GSW | unibet | 1.97 | 1.94 | 1.66 | 60.3% | 50.0% | 51.6% | +1.7% | +18.9% | 0.4% |
| Charles Bassey PTS under 7.5 | BOS @ GSW | draftkings | 2.08 | 2.06 | 1.93 | 51.9% | 48.0% | 48.6% | +1.0% | +7.9% | 0.2% |
| Derrick White PTS under 14.5 | BOS @ GSW | pointsbetau | 2.00 | 2.00 | 1.84 | 54.2% | 49.3% | 50.0% | +0.1% | +8.5% | 0.0% |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 35.9<br><sub>38,30,36,37,-</sub> | 27.9<br><sub>24,32,24,24,-</sub> | 26.5 · 26.5<br><sub>o 51% · u 49%</sub> | 8.5<br><sub>7,6,12,8,-</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>8,6,4,3,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>2,5,3,3,-</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.6 | 3.3 | 43.1 |
| Derrick White | 76% | 32.6<br><sub>38,23,32,35,-</sub> | 14.7<br><sub>19,16,9,12,-</sub> | 14.5 · 14.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>1,4,3,3,-</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.8<br><sub>7,2,2,8,-</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,4,1,0,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.9 | 1.7 | 23.3 |
| Payton Pritchard | 99% | 32.4<br><sub>31,19,32,30,34</sub> | 16.9<br><sub>14,10,21,15,9</sub> | 15.5 · 15.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>1,1,4,1,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.9<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.4 | 25.5 |
| Neemias Queta | 99% | 28.2<br><sub>31,15,-,27,30</sub> | 12.1<br><sub>11,8,-,17,15</sub> | 10.5 · 10.5<br><sub>o 53% · u 47%</sub> | 9.3<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,-,3,1</sub> |  | 0.2<br><sub>1,1,-,0,1</sub> |  | 0.8 | 1.3 | 1.4 | 23.6 |
| Sam Hauser | 99% | 27.9<br><sub>24,11,25,17,31</sub> | 10.4<br><sub>8,8,12,9,14</sub> | 8.5 · 8.5<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,0,2,2,2</sub> |  | 2.2<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.3 | 0.5 | 16.2 |
| Baylor Scheierman | 99% | 19.8<br><sub>29,18,11,13,18</sub> | 5.8<br><sub>9,12,0,0,4</sub> | 7.5 · 7.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>7,5,1,1,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>3,3,1,1,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.1 | 0.7 | 10.9 |
| Luka Garza | 98% | 16.3<br><sub>11,14,18,5,17</sub> | 7.4<br><sub>5,2,3,0,5</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,3,0,1,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,5,4,1,1</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 12.6 |
| Jordan Walsh | 98% | 15.1<br><sub>18,21,17,4,8</sub> | 4.4<br><sub>6,11,6,0,1</sub> | – · 4.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,1,2,0,4</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.5<br><sub>0,2,2,0,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.1 |
| Hugo Gonzalez | 98% | 15.0<br><sub>8,18,4,16,17</sub> | 4.4<br><sub>0,9,0,2,5</sub> |  | 3.1<br><sub>1,5,2,6,4</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.5<br><sub>0,2,0,0,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.2 |
| Mike Conley | 48% | 14.1<br><sub>-,-,-,-,18</sub> | 4.9<br><sub>-,-,-,-,19</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,4</sub> |  | 0.7 | 0.2 | 0.6 | 8.4 |
| Chris Cenac Jr. | 67% | 13.9<br><sub>-,7,12,17,12</sub> | 5.2<br><sub>-,6,4,6,2</sub> |  | 3.1<br><sub>-,3,2,6,3</sub> |  | 0.5<br><sub>-,0,1,0,0</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.7 | 8.8 |
| Devin Carter | 93% | 13.0<br><sub>-,12,-,-,4</sub> | 5.3<br><sub>-,0,-,-,0</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 1.5<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 9.2 |
| Ron Harper Jr. | 58% | 11.6<br><sub>-,12,-,-,13</sub> | 4.3<br><sub>-,10,-,-,3</sub> |  | 1.6<br><sub>-,1,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,1</sub> |  | 0.6<br><sub>-,2,-,-,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.6 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 32.8<br><sub>36,24,33,30,33</sub> | 18.4<br><sub>25,3,28,13,11</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.7 | 2.7 | 29.3 |
| Brandin Podziemski | 97% | 32.7<br><sub>37,22,30,29,32</sub> | 16.2<br><sub>22,8,15,10,15</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.6 | 25.3 |
| Draymond Green | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · 4.5<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.6<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.7 | 2.2 | 16.0 |
| Will Richard | 98% | 23.4<br><sub>19,30,23,27,27</sub> | 8.3<br><sub>9,7,11,20,15</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.8 | 12.4 |
| De'Anthony Melton | 99% | 23.2<br><sub>25,18,21,19,25</sub> | 10.5<br><sub>11,8,8,0,9</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.4 | 1.5 | 16.5 |
| Gui Santos | 96% | 19.0<br><sub>12,21,19,17,23</sub> | 8.0<br><sub>0,7,12,6,8</sub> | 7.5 · 7.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,1,2,6,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.3 | 1.2 | 13.9 |
| Charles Bassey | 98% | 17.8<br><sub>13,20,16,22,25</sub> | 8.0<br><sub>7,11,4,10,16</sub> | 7.5 · 7.5<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.2 |
| Gary Payton II | 88% | 17.6<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.1<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.1 |
| Georges Niang | 98% | 17.5<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>5,3,4,1,2</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.3 | 0.1 | 0.8 | 11.3 |
| Al Horford | 98% | 16.8<br><sub>21,10,14,-,17</sub> | 5.5<br><sub>2,0,0,-,3</sub> | 5.5 · 5.5<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>1,3,5,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.3 | 0.7 | 0.6 | 10.8 |
| LJ Cryer | 88% | 14.7<br><sub>18,24,24,19,12</sub> | 6.7<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.5<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.7 | 9.4 |
| Graham Ike | 96% | 10.2<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.6 |
| Malevy Leons | 83% | 8.2<br><sub>4,14,6,7,4</sub> | 2.2<br><sub>0,5,2,2,0</sub> |  | 1.6<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-22/`._
