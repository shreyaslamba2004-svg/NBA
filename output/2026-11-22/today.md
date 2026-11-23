# NBA model · Sun 22 Nov 2026 (US date)

Updated **Mon 23 Nov, 11:39 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-22/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Obi Toppin PTS over 11.5 (12+) | IND @ NYK | draftkings | 2.40 | 2.16 | 2.76 | 36.2% | 48.1% | 46.3% | +11.0% | -13.2% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson PR over 49.5 (50+) | IND @ NYK | draftkings | 19.60 | 16.45 | 7.53 | 13.3% | 4.8% | 6.1% | +19.2% | +160.3% | 0.3% |
| Jalen Brunson PA over 54.5 (55+) | IND @ NYK | draftkings | 23.00 | 19.31 | 8.86 | 11.3% | 4.1% | 5.2% | +19.1% | +159.7% | 0.2% |
| Jalen Brunson PTS over 44.5 (45+) | IND @ NYK | draftkings | 17.40 | 14.66 | 6.75 | 14.8% | 5.4% | 6.8% | +18.8% | +157.7% | 0.3% |
| Jalen Brunson PA over 49.5 (50+) | IND @ NYK | draftkings | 13.60 | 11.51 | 5.35 | 18.7% | 6.9% | 8.7% | +18.2% | +154.0% | 0.4% |
| Karl-Anthony Towns AST over 7.5 (8+) | IND @ NYK | draftkings | 22.00 | 19.42 | 9.88 | 10.1% | 4.2% | 5.1% | +13.4% | +122.8% | 0.2% |
| Jalen Brunson PR over 44.5 (45+) | IND @ NYK | draftkings | 9.80 | 8.80 | 4.68 | 21.4% | 9.5% | 11.4% | +11.3% | +109.4% | 0.3% |
| Jalen Brunson PTS over 39.5 (40+) | IND @ NYK | draftkings | 8.30 | 7.56 | 4.15 | 24.1% | 11.3% | 13.2% | +9.8% | +99.8% | 0.3% |
| Karl-Anthony Towns REB over 19.5 (20+) | IND @ NYK | draftkings | 12.60 | 11.64 | 6.64 | 15.0% | 7.4% | 8.6% | +8.3% | +89.7% | 0.2% |
| Jalen Brunson PA over 44.5 (45+) | IND @ NYK | draftkings | 6.50 | 6.03 | 3.48 | 28.7% | 14.4% | 16.6% | +7.8% | +86.6% | 0.4% |
| Jayson Tatum PRA over 59.5 (60+) | BOS @ GSW | draftkings | 17.00 | 15.95 | 9.50 | 10.5% | 5.5% | 6.3% | +6.6% | +79.0% | 0.1% |
| Karl-Anthony Towns REB over 17.5 (18+) | IND @ NYK | draftkings | 6.95 | 6.55 | 3.95 | 25.3% | 13.5% | 15.3% | +6.1% | +75.8% | 0.3% |
| Karl-Anthony Towns PA over 39.5 (40+) | IND @ NYK | draftkings | 15.00 | 14.16 | 8.63 | 11.6% | 6.2% | 7.1% | +5.9% | +73.9% | 0.1% |
| Jayson Tatum REB over 11.5 (12+) | BOS @ GSW | draftkings | 9.60 | 9.12 | 5.65 | 17.7% | 9.7% | 11.0% | +5.2% | +70.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| IND @ NYK | Mon 23 Nov 12:00 | 107.3–115.2 | IND 29% | 3.49 / 1.40 | NYK -7.5 | 222.5 | NYK -8.5 covers 48%; o213.5 68% |
| BOS @ GSW | Mon 23 Nov 12:30 | 112.2–104.9 | BOS 70% | 1.43 / 3.31 | GSW +7.5 | 216.5 | GSW +7.5 covers 50%; o210.5 64% |

### IND @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Miles McBride (NYK), Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Obi Toppin PTS over 11.5 (12+) | IND @ NYK | draftkings | 2.40 | 2.16 | 2.76 | 36.2% | 48.1% | 46.3% | +11.0% | -13.2% | 2.0% |
| Ivica Zubac PTS over 11.5 (12+) | IND @ NYK | draftkings | 2.17 | 2.08 | 2.44 | 41.0% | 49.5% | 48.2% | +4.5% | -11.1% | 1.0% |
| Jalen Brunson PTS over 29.5 (30+) | IND @ NYK | draftkings | 2.24 | 2.19 | 1.90 | 52.7% | 44.5% | 45.8% | +2.5% | +18.1% | 0.5% |
| Jalen Brunson PTS over 28.5 (29+) | IND @ NYK | pointsbetau | 2.00 | 1.99 | 1.77 | 56.4% | 49.1% | 50.2% | +0.4% | +12.7% | 0.1% |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 93% | 33.7<br><sub>32,32,34,33,30</sub> | 21.7<br><sub>28,19,31,24,21</sub> | 19.5 · 20.5<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>8,3,2,4,7</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>5,2,2,3,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>2,2,0,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.4 | 2.0 | 31.5 |
| Andrew Nembhard | 91% | 33.2<br><sub>34,34,-,-,26</sub> | 15.9<br><sub>17,12,-,-,12</sub> | 13.5 · 14.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 7.8<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.4 | 26.6 |
| Aaron Nesmith | 93% | 29.4<br><sub>22,33,36,29,29</sub> | 11.9<br><sub>2,18,12,2,2</sub> | 11.5 · 12.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>1,1,4,3,7</sub> |  | 1.7<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 0.5 | 1.2 | 17.8 |
| Ivica Zubac | 88% | 26.1<br><sub>31,26,22,24,27</sub> | 11.1<br><sub>20,12,8,4,21</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.4 | 21.1 |
| Kelly Oubre Jr. | 91% | 25.3<br><sub>34,30,29,23,23</sub> | 10.9<br><sub>14,16,16,17,17</sub> | 11.5 · 12.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>6,5,4,4,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>1,0,2,0,0</sub> |  | 1.2<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.0 | 16.0 |
| Quenton Jackson | 98% | 21.3<br><sub>21,20,30,22,18</sub> | 9.2<br><sub>4,3,15,15,3</sub> |  | 2.9<br><sub>2,5,6,2,2</sub> |  | 3.1<br><sub>2,4,8,3,2</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> |  | 0.8 | 0.2 | 1.3 | 15.1 |
| Obi Toppin | 88% | 19.8<br><sub>16,16,14,17,26</sub> | 10.3<br><sub>8,9,5,6,17</sub> | 9.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>3,3,2,1,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,1,1,1,2</sub> |  | 1.3<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.2 | 0.9 | 15.8 |
| Jarace Walker | 88% | 15.7<br><sub>7,-,14,17,11</sub> | 6.2<br><sub>1,-,2,1,8</sub> |  | 3.2<br><sub>1,-,5,3,1</sub> |  | 1.4<br><sub>0,-,2,1,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.3 | 0.8 | 10.8 |
| Jalen Slawson | 91% | 13.5<br><sub>12,10,14,12,14</sub> | 4.0<br><sub>2,1,8,5,4</sub> |  | 2.7<br><sub>3,4,5,4,2</sub> |  | 1.2<br><sub>1,0,2,2,2</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 0.6 | 7.8 |
| Braden Smith | 67% | 13.3<br><sub>-,-,-,18,11</sub> | 4.3<br><sub>-,-,-,8,5</sub> |  | 1.5<br><sub>-,-,-,5,3</sub> |  | 2.5<br><sub>-,-,-,3,5</sub> |  | 0.3<br><sub>-,-,-,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Jay Huff | 91% | 11.9<br><sub>11,8,18,15,1</sub> | 4.8<br><sub>6,8,11,5,0</sub> |  | 2.1<br><sub>4,1,0,3,0</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.6<br><sub>0,2,3,0,0</sub> |  | 0.2 | 0.7 | 0.5 | 7.8 |
| Larry Nance Jr. | 97% | 11.7<br><sub>5,14,7,9,11</sub> | 3.7<br><sub>5,2,4,3,7</sub> |  | 2.1<br><sub>0,2,2,1,2</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.4<br><sub>1,0,1,1,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.5 |
| Kobe Brown | 86% | 9.6<br><sub>-,-,3,2,-</sub> | 3.2<br><sub>-,-,0,0,-</sub> |  | 1.7<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.6 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 36.0<br><sub>36,41,34,35,36</sub> | 31.9<br><sub>33,28,31,21,30</sub> | 27.5 · 28.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>1,1,5,2,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 6.6<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 3.2<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.2 | 2.3 | 42.0 |
| Karl-Anthony Towns | 99% | 34.1<br><sub>34,43,36,33,-</sub> | 23.1<br><sub>23,28,16,22,-</sub> | 20.5 · 20.5<br><sub>o 52% · u 48%</sub> | 14.6<br><sub>15,17,16,12,-</sub> | 12.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>5,3,8,4,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>3,3,1,2,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.8 | 2.8 | 42.2 |
| Josh Hart | 98% | 32.5<br><sub>23,26,31,28,35</sub> | 9.8<br><sub>0,0,5,11,0</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>5,5,4,6,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.3 | 1.4 | 21.4 |
| Landry Shamet | 99% | 32.5<br><sub>21,30,24,30,36</sub> | 13.0<br><sub>5,23,12,10,20</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>3,2,1,1,1</sub> |  | 2.0<br><sub>1,0,1,2,3</sub> |  | 2.4<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.2 | 0.9 | 17.3 |
| Mikal Bridges | 99% | 31.4<br><sub>29,32,30,31,28</sub> | 12.2<br><sub>18,5,17,8,12</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.5 | 1.1 | 18.8 |
| Andre Drummond | 99% | 19.2<br><sub>14,7,11,15,23</sub> | 5.9<br><sub>0,2,2,4,7</sub> |  | 9.0<br><sub>6,3,8,4,13</sub> |  | 1.3<br><sub>0,0,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.6 | 0.8 | 0.9 | 16.1 |
| Tyler Kolek | 96% | 17.9<br><sub>19,16,13,12,13</sub> | 6.2<br><sub>5,0,4,6,7</sub> |  | 2.4<br><sub>6,0,1,3,3</sub> |  | 4.6<br><sub>2,7,3,5,0</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.5 | 0.2 | 0.9 | 13.2 |
| Jose Alvarado | 80% | 16.7<br><sub>-,2,7,13,15</sub> | 6.2<br><sub>-,0,2,2,8</sub> |  | 2.1<br><sub>-,0,0,2,2</sub> |  | 2.7<br><sub>-,1,4,1,2</sub> |  | 0.9<br><sub>-,0,0,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 11.0 |
| James Wiseman | 52% | 16.4<br><sub>-,3,-,-,25</sub> | 5.2<br><sub>-,0,-,-,5</sub> |  | 5.5<br><sub>-,3,-,-,6</sub> |  | 0.8<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.8 | 0.9 | 11.6 |
| Mohamed Diawara | 38% | 14.6<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 8.8 |
| Pacome Dadiet | 52% | 12.3<br><sub>1,-,-,-,11</sub> | 4.8<br><sub>0,-,-,-,5</sub> |  | 2.0<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,2</sub> |  | 0.6<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 7.6 |
| Dalton Knecht | 67% | 11.7<br><sub>-,-,-,-,3</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 7.0 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Jaden Akins | 38% | 8.2<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.1 |

</details>


### BOS @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW), Paul George (BOS), Mitchell Robinson (BOS)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 35.9<br><sub>38,30,36,37,-</sub> | 27.9<br><sub>24,32,24,24,-</sub> | 27.5 · –<br><sub>o 47% · u 53%</sub> | 8.5<br><sub>7,6,12,8,-</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>8,6,4,3,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>2,5,3,3,-</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.6 | 3.3 | 43.1 |
| Derrick White | 76% | 32.6<br><sub>38,23,32,35,-</sub> | 14.7<br><sub>19,16,9,12,-</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,4,3,3,-</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.8<br><sub>7,2,2,8,-</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,4,1,0,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.9 | 1.7 | 23.3 |
| Payton Pritchard | 99% | 32.4<br><sub>31,19,32,30,34</sub> | 16.9<br><sub>14,10,21,15,9</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>1,1,4,1,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.9<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.4 | 25.5 |
| Neemias Queta | 99% | 28.2<br><sub>31,15,-,27,30</sub> | 12.1<br><sub>11,8,-,17,15</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 9.3<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,-,3,1</sub> |  | 0.2<br><sub>1,1,-,0,1</sub> |  | 0.8 | 1.3 | 1.4 | 23.6 |
| Sam Hauser | 99% | 27.9<br><sub>24,11,25,17,31</sub> | 10.4<br><sub>8,8,12,9,14</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,0,2,2,2</sub> |  | 2.2<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.3 | 0.5 | 16.2 |
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
| Yaxel Lendeborg | 98% | 32.8<br><sub>36,24,33,30,33</sub> | 18.4<br><sub>25,3,28,13,11</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.7 | 2.7 | 29.3 |
| Brandin Podziemski | 97% | 32.7<br><sub>37,22,30,29,32</sub> | 16.2<br><sub>22,8,15,10,15</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.6 | 25.3 |
| Draymond Green | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.6<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.7 | 2.2 | 16.0 |
| Will Richard | 98% | 23.4<br><sub>19,30,23,27,27</sub> | 8.3<br><sub>9,7,11,20,15</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.8 | 12.4 |
| De'Anthony Melton | 99% | 23.2<br><sub>25,18,21,19,25</sub> | 10.5<br><sub>11,8,8,0,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.4 | 1.5 | 16.5 |
| Gui Santos | 96% | 19.0<br><sub>12,21,19,17,23</sub> | 8.0<br><sub>0,7,12,6,8</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,1,2,6,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.3 | 1.2 | 13.9 |
| Charles Bassey | 98% | 17.8<br><sub>13,20,16,22,25</sub> | 8.0<br><sub>7,11,4,10,16</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.2 |
| Gary Payton II | 88% | 17.6<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.1<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.1 |
| Georges Niang | 98% | 17.5<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>5,3,4,1,2</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.3 | 0.1 | 0.8 | 11.3 |
| Al Horford | 98% | 16.8<br><sub>21,10,14,-,17</sub> | 5.5<br><sub>2,0,0,-,3</sub> | 5.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>1,3,5,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.3 | 0.7 | 0.6 | 10.8 |
| LJ Cryer | 88% | 14.7<br><sub>18,24,24,19,12</sub> | 6.7<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.5<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.7 | 9.4 |
| Graham Ike | 96% | 10.2<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.6 |
| Malevy Leons | 83% | 8.2<br><sub>4,14,6,7,4</sub> | 2.2<br><sub>0,5,2,2,0</sub> |  | 1.6<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-22/`._
