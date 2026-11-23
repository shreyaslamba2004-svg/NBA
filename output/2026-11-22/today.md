# NBA model · Sun 22 Nov 2026 (US date)

Updated **Mon 23 Nov, 12:29 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-22/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum REB over 11.5 (12+) | BOS @ GSW | draftkings | 10.60 | 9.89 | 5.80 | 17.2% | 8.8% | 10.1% | +7.2% | +82.7% | 0.2% |
| Jayson Tatum REB over 13.5 (14+) | BOS @ GSW | draftkings | 23.00 | 21.88 | 13.64 | 7.3% | 4.1% | 4.6% | +5.0% | +68.6% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| BOS @ GSW | Mon 23 Nov 12:30 | 112.2–104.9 | BOS 70% | 1.43 / 3.31 | GSW +7.5 | 216.5 | GSW +8.5 covers 53%; o211.5 62% |

### BOS @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW), Paul George (BOS), Mitchell Robinson (BOS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Hugo Gonzalez PTS over 4.5 (5+) | BOS @ GSW | pointsbetau | 2.00 | 1.92 | 1.67 | 59.8% | 50.6% | 52.0% | +4.0% | +19.7% | 1.0% |
| Sam Hauser PTS over 8.5 (9+) | BOS @ GSW | unibet | 1.97 | 1.93 | 1.63 | 61.5% | 50.0% | 51.8% | +2.0% | +21.3% | 0.5% |
| Neemias Queta PTS over 10.5 (11+) | BOS @ GSW | sportsbet | 2.02 | 2.01 | 1.94 | 51.6% | 49.3% | 49.6% | +0.3% | +4.2% | 0.1% |
| Derrick White PTS under 14.5 | BOS @ GSW | pointsbetau | 2.00 | 2.00 | 1.85 | 54.0% | 49.3% | 50.0% | +0.0% | +8.1% | 0.0% |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 100% | 35.4<br><sub>38,30,36,37,-</sub> | 27.0<br><sub>24,32,24,24,-</sub> | 26.5 · 26.5<br><sub>o 51% · u 49%</sub> | 8.4<br><sub>7,6,12,8,-</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 6.7<br><sub>8,6,4,3,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>2,5,3,3,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.5 | 3.2 | 42.1 |
| Derrick White | 100% | 32.5<br><sub>38,23,32,35,-</sub> | 14.6<br><sub>19,16,9,12,-</sub> | 14.5 · 14.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,4,3,3,-</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.8<br><sub>7,2,2,8,-</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,4,1,0,-</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.9 | 1.7 | 23.2 |
| Payton Pritchard | 99% | 31.5<br><sub>31,19,32,30,34</sub> | 16.0<br><sub>14,10,21,15,9</sub> | 16.5 · 15.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>1,1,4,1,6</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 4.8<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.4 | 24.4 |
| Sam Hauser | 100% | 29.0<br><sub>24,11,25,17,31</sub> | 10.5<br><sub>8,8,12,9,14</sub> | 9.5 · 8.5<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>0,0,2,2,2</sub> |  | 2.3<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.3 | 0.5 | 16.5 |
| Neemias Queta | 100% | 27.5<br><sub>31,15,-,27,30</sub> | 11.5<br><sub>11,8,-,17,15</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 9.0<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>3,2,-,3,1</sub> |  | 0.2<br><sub>1,1,-,0,1</sub> |  | 0.7 | 1.2 | 1.4 | 22.6 |
| Hugo Gonzalez | 100% | 19.9<br><sub>8,18,4,16,17</sub> | 5.9<br><sub>0,9,0,2,5</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>1,5,2,6,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>0,2,0,0,1</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.8 | 0.4 | 0.9 | 11.0 |
| Baylor Scheierman | 99% | 18.8<br><sub>29,18,11,13,18</sub> | 5.5<br><sub>9,12,0,0,4</sub> | 6.5 · 7.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>7,5,1,1,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.1 | 0.7 | 10.3 |
| Luka Garza | 98% | 15.7<br><sub>11,14,18,5,17</sub> | 7.0<br><sub>5,2,3,0,5</sub> | 7.5 · 6.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>1,3,0,1,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,5,4,1,1</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 12.1 |
| Jordan Walsh | 98% | 14.2<br><sub>18,21,17,4,8</sub> | 4.1<br><sub>6,11,6,0,1</sub> | – · 4.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,1,2,0,4</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,2,2,0,0</sub> |  | 0.6 | 0.2 | 0.5 | 7.6 |
| Mike Conley | 48% | 13.2<br><sub>-,-,-,-,18</sub> | 4.5<br><sub>-,-,-,-,19</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,4</sub> |  | 0.7 | 0.2 | 0.6 | 7.8 |
| Chris Cenac Jr. | 67% | 13.2<br><sub>-,7,12,17,12</sub> | 5.0<br><sub>-,6,4,6,2</sub> |  | 3.0<br><sub>-,3,2,6,3</sub> |  | 0.5<br><sub>-,0,1,0,0</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.8 | 8.5 |
| Devin Carter | 93% | 12.0<br><sub>-,12,-,-,4</sub> | 4.8<br><sub>-,0,-,-,0</sub> |  | 2.2<br><sub>-,2,-,-,2</sub> |  | 1.4<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.1 | 0.9 | 8.5 |
| Ron Harper Jr. | 58% | 11.0<br><sub>-,12,-,-,13</sub> | 4.1<br><sub>-,10,-,-,3</sub> |  | 1.4<br><sub>-,1,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,1</sub> |  | 0.5<br><sub>-,2,-,-,1</sub> |  | 0.4 | 0.2 | 0.3 | 6.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 100% | 32.7<br><sub>36,24,33,30,33</sub> | 18.1<br><sub>25,3,28,13,11</sub> | 19.5 · 19.5<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.7 | 2.8 | 29.0 |
| Brandin Podziemski | 100% | 32.7<br><sub>37,22,30,29,32</sub> | 15.9<br><sub>22,8,15,10,15</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.2 | 1.6 | 24.9 |
| De'Anthony Melton | 100% | 26.2<br><sub>25,18,21,19,25</sub> | 11.7<br><sub>11,8,8,0,9</sub> | 10.5 · 10.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.5 | 1.7 | 18.5 |
| Draymond Green | 100% | 26.0<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · 4.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 46% · u 53%</sub> | 5.8<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 0.7<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.7 | 2.2 | 16.2 |
| Will Richard | 98% | 23.0<br><sub>19,30,23,27,27</sub> | 8.1<br><sub>9,7,11,20,15</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.8 | 12.0 |
| Charles Bassey | 100% | 21.5<br><sub>13,20,16,22,25</sub> | 9.6<br><sub>7,11,4,10,16</sub> | 7.5 · 7.5<br><sub>o 54% · u 46%</sub> | 7.5<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.3 | 18.1 |
| Gui Santos | 96% | 18.8<br><sub>12,21,19,17,23</sub> | 7.8<br><sub>0,7,12,6,8</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>1,1,2,6,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.7<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.3 | 1.2 | 13.5 |
| Gary Payton II | 88% | 17.3<br><sub>-,13,8,16,24</sub> | 7.3<br><sub>-,2,2,8,2</sub> |  | 3.0<br><sub>-,2,0,8,1</sub> |  | 1.4<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 11.6 |
| Georges Niang | 98% | 17.1<br><sub>19,15,14,14,15</sub> | 7.2<br><sub>5,5,0,11,5</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>5,3,4,1,2</sub> |  | 1.1<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.3 | 0.1 | 0.8 | 10.8 |
| Al Horford | 98% | 16.8<br><sub>21,10,14,-,17</sub> | 5.4<br><sub>2,0,0,-,3</sub> | 5.5 · 5.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>1,3,5,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.7<br><sub>0,0,0,-,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.3 | 0.7 | 0.5 | 10.7 |
| LJ Cryer | 88% | 14.4<br><sub>18,24,24,19,12</sub> | 6.5<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.5<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.7 | 9.2 |
| Graham Ike | 96% | 10.0<br><sub>4,13,8,15,4</sub> | 4.0<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.4 |
| Malevy Leons | 83% | 7.9<br><sub>4,14,6,7,4</sub> | 2.2<br><sub>0,5,2,2,0</sub> |  | 1.5<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.1 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-22/`._
