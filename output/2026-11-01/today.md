# NBA model · Sun 01 Nov 2026 (US date)

Updated **Sun 01 Nov, 03:42 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-01/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle PTS over 39.5 (40+) | BKN @ IND | draftkings | 29.00 | 25.91 | 17.35 | 5.8% | 3.2% | 3.9% | +11.9% | +67.1% | 0.1% |
| Michael Porter Jr. PA over 39.5 (40+) | BKN @ IND | draftkings | 14.60 | 13.50 | 9.58 | 10.4% | 6.4% | 7.4% | +8.2% | +52.5% | 0.1% |
| Paul George REB over 7.5 (8+) | BOS @ ORL | draftkings | 7.60 | 7.16 | 5.27 | 19.0% | 12.3% | 14.0% | +6.2% | +44.3% | 0.2% |
| Julius Randle PR over 49.5 (50+) | BKN @ IND | draftkings | 26.00 | 24.57 | 18.24 | 5.5% | 3.6% | 4.1% | +5.7% | +42.5% | 0.1% |
| Michael Porter Jr. PR over 44.5 (45+) | BKN @ IND | draftkings | 12.20 | 11.57 | 8.65 | 11.6% | 7.7% | 8.6% | +5.3% | +41.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George REB over 8.5 (9+) | BOS @ ORL | draftkings | 12.60 | 11.89 | 8.78 | 11.4% | 7.4% | 8.4% | +6.0% | +43.6% | 0.1% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kris Dunn RA under 9.5 | LAC @ GSW | draftkings | 1.94 | 1.84 | 1.37 | 73.1% | 48.2% | 54.4% | +5.7% | +42.0% | 1.5% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| BOS @ ORL | Mon 02 Nov 07:30 | 115.8–107.2 | BOS 73% | 1.38 / 3.67 | ORL +8.5 | 222.5 | ORL +6.5 covers 44%; o222.5 51% |
| BKN @ IND | Mon 02 Nov 09:00 | 114.0–115.8 | BKN 45% | 2.24 / 1.81 | IND -2.5 | 229.5 | IND -4.5 covers 43%; o230.5 48% |
| LAC @ GSW | Mon 02 Nov 12:30 | 113.7–113.9 | LAC 50% | 2.01 / 1.99 | GSW +0.5 | 227.5 | GSW -2.5 covers 44%; o219.5 67% |
| TOR @ LAL | Mon 02 Nov 13:00 | 112.1–113.1 | TOR 47% | 2.12 / 1.89 | LAL -1.5 | 225.5 | LAL -4.5 covers 41%; o227.5 45% |

### BOS @ ORL
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL), Devin Carter (BOS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.8–107.2 | BOS 73% | 1.38 / 3.67 | ORL +8.5 | 222.5 | ORL +6.5 covers 44%; o222.5 51% |
| Expected (weighted by chance each plays) | 116.3–107.3 | BOS 74% | 1.36 / 3.81 | ORL +8.5 | 223.5 | ORL +6.5 covers 43%; o222.5 52% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Mitchell Robinson (BOS) | Questionable | 55% | 18.1 | 5.3 | 6.3 | 0.6 | 0.0 | 0.8 | 0.9 | 0.8 | 12.2 | small |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 36.8<br><sub>38,37,28,42,35</sub> | 29.0<br><sub>13,36,23,40,26</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 9.3<br><sub>4,9,7,5,7</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>11,7,6,8,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>0,3,2,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.3 | 0.4 | 2.9 | 44.8 |
| Derrick White | 98% | 33.7<br><sub>36,33,18,33,26</sub> | 14.1<br><sub>17,12,5,16,9</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>1,4,6,5,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>8,6,4,7,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>3,2,1,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 1.0 | 1.8 | 22.8 |
| Paul George | 98% | 32.6<br><sub>31,34,25,36,27</sub> | 19.7<br><sub>38,15,16,20,18</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>5,7,5,7,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,2,2,7,8</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>7,3,3,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.7 | 0.4 | 2.2 | 28.4 |
| Payton Pritchard | 98% | 31.7<br><sub>28,30,22,24,35</sub> | 16.6<br><sub>17,4,28,4,30</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,1,1,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>1,4,4,6,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>2,1,7,0,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 1.5 | 24.4 |
| Sam Hauser | 98% | 22.6<br><sub>18,23,20,25,18</sub> | 7.7<br><sub>11,6,11,11,6</sub> |  | 3.6<br><sub>4,2,4,4,3</sub> |  | 1.0<br><sub>1,2,1,0,2</sub> |  | 1.4<br><sub>3,2,3,3,2</sub> |  | 0.4 | 0.2 | 0.5 | 12.3 |
| Neemias Queta | 98% | 22.0<br><sub>22,22,19,15,20</sub> | 8.5<br><sub>3,15,7,7,13</sub> |  | 6.9<br><sub>4,6,5,3,6</sub> |  | 1.2<br><sub>2,1,1,2,0</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 16.6 |
| Baylor Scheierman | 98% | 20.2<br><sub>18,11,18,21,23</sub> | 5.8<br><sub>8,2,2,3,2</sub> |  | 3.6<br><sub>3,0,6,4,3</sub> |  | 1.3<br><sub>0,0,2,1,3</sub> |  | 0.9<br><sub>2,0,0,1,0</sub> |  | 0.7 | 0.1 | 0.6 | 10.6 |
| Jordan Walsh | 97% | 16.7<br><sub>13,20,18,24,11</sub> | 4.5<br><sub>0,5,4,15,2</sub> |  | 3.5<br><sub>6,3,3,6,2</sub> |  | 0.7<br><sub>1,0,2,1,0</sub> |  | 0.5<br><sub>0,1,0,3,0</sub> |  | 0.7 | 0.4 | 0.5 | 8.8 |
| Hugo Gonzalez | 91% | 13.7<br><sub>10,4,24,6,15</sub> | 3.3<br><sub>0,0,13,0,0</sub> |  | 3.0<br><sub>3,0,5,2,2</sub> |  | 0.6<br><sub>0,1,2,0,0</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.5 | 6.9 |
| Luka Garza | 96% | 12.3<br><sub>8,4,13,13,7</sub> | 6.0<br><sub>2,8,6,2,5</sub> |  | 3.0<br><sub>2,1,3,4,1</sub> |  | 0.7<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>0,2,0,0,0</sub> |  | 0.3 | 0.3 | 0.7 | 9.7 |
| Mike Conley | 43% | 8.7<br><sub>-,-,7,-,-</sub> | 2.4<br><sub>-,-,6,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,2,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.4 |
| Dillon Mitchell | 16% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Ron Harper Jr. | 58% | 7.6<br><sub>-,-,7,-,3</sub> | 2.9<br><sub>-,-,3,-,0</sub> |  | 1.2<br><sub>-,-,1,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,1,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Chris Cenac Jr. | 52% | 6.2<br><sub>-,-,5,-,2</sub> | 2.6<br><sub>-,-,3,-,3</sub> |  | 1.6<br><sub>-,-,1,-,2</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 4.5 |
| Amari Williams | 16% | 6.2 | 1.6 |  | 1.8 |  | 0.4 |  | 0.0 |  | 0.2 | 0.4 | 0.5 | 3.8 |

</details>

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane | 98% | 35.4<br><sub>33,27,35,34,39</sub> | 19.5<br><sub>18,5,22,13,28</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>5,2,6,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>2,0,2,4,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,1,4,2,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.4 | 2.3 | 28.1 |
| Franz Wagner | 98% | 35.2<br><sub>29,33,37,34,39</sub> | 22.6<br><sub>22,18,23,15,26</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>6,6,13,4,5</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 6.4<br><sub>5,5,9,5,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 3.0 | 35.0 |
| Wendell Carter Jr. | 98% | 33.4<br><sub>31,29,33,26,39</sub> | 12.8<br><sub>22,20,9,3,20</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>7,9,10,10,7</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>0,1,2,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0<br><sub>1,3,0,0,1</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.7 | 1.6 | 22.9 |
| Anthony Black | 98% | 30.2<br><sub>-,-,26,22,31</sub> | 13.5<br><sub>-,-,18,8,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>-,-,3,2,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.2<br><sub>-,-,5,1,10</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>-,-,5,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.6 | 1.9 | 21.6 |
| Tristan da Silva | 98% | 27.2<br><sub>28,29,27,31,23</sub> | 11.1<br><sub>14,5,19,20,8</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>2,3,2,3,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>3,1,2,1,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>4,1,5,4,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.6 | 0.3 | 1.1 | 16.6 |
| Jase Richardson | 88% | 24.8<br><sub>14,14,17,14,33</sub> | 9.0<br><sub>2,6,6,10,4</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,1,1,1,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>3,3,0,1,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>0,1,2,2,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 1.0 | 14.2 |
| Jamal Cain | 98% | 17.2<br><sub>14,11,15,16,15</sub> | 6.6<br><sub>0,0,5,9,13</sub> |  | 2.8<br><sub>0,1,5,1,0</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.7<br><sub>0,0,1,0,3</sub> |  | 0.4 | 0.2 | 0.7 | 10.3 |
| Jevon Carter | 52% | 16.0<br><sub>-,13,-,22,-</sub> | 5.1<br><sub>-,0,-,6,-</sub> |  | 1.6<br><sub>-,1,-,0,-</sub> |  | 1.6<br><sub>-,1,-,3,-</sub> |  | 0.8<br><sub>-,0,-,2,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Goga Bitadze | 80% | 12.4<br><sub>12,12,-,11,6</sub> | 4.4<br><sub>6,4,-,6,2</sub> |  | 3.7<br><sub>6,3,-,0,4</sub> |  | 1.0<br><sub>1,0,-,1,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 9.1 |
| Nikola Vucevic | 96% | 12.3<br><sub>5,4,15,16,6</sub> | 4.5<br><sub>0,0,5,5,3</sub> |  | 3.1<br><sub>1,2,3,4,1</sub> |  | 1.4<br><sub>1,0,3,2,0</sub> |  | 0.5<br><sub>0,0,1,0,1</sub> |  | 0.2 | 0.3 | 0.5 | 9.0 |
| Alex Morales | 64% | 11.9<br><sub>-,4,-,7,9</sub> | 3.4<br><sub>-,0,-,2,0</sub> |  | 1.7<br><sub>-,1,-,2,1</sub> |  | 1.2<br><sub>-,0,-,1,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 6.3 |
| Colin Castleton | 52% | 7.8<br><sub>-,4,-,7,-</sub> | 2.5<br><sub>-,7,-,2,-</sub> |  | 2.2<br><sub>-,2,-,2,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.2 |

</details>


### BKN @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND), Ivica Zubac (IND), Mikel Brown Jr. (BKN), Egor Demin (BKN), Grant Nelson (BKN), Ben Saraf (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.0–115.8 | BKN 45% | 2.24 / 1.81 | IND -2.5 | 229.5 | IND -4.5 covers 43%; o230.5 48% |
| Expected (weighted by chance each plays) | 113.5–116.9 | BKN 40% | 2.49 / 1.67 | IND -3.5 | 230.5 | IND -4.5 covers 48%; o230.5 49% |
| if Obi Toppin plays | 112.8–117.9 | BKN 35% | 2.82 / 1.55 | IND -5.5 | 230.5 | IND -4.5 covers 52%; o230.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Obi Toppin (IND) | Questionable | 55% | 22.3 | 13.8 | 5.1 | 2.1 | 1.8 | 0.7 | 0.3 | 1.3 | 20.9 | full tables below |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 98% | 34.5<br><sub>38,35,24,44,25</sub> | 23.4<br><sub>33,23,10,24,15</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>8,6,7,9,8</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 5.2<br><sub>7,5,7,4,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>3,2,0,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.3 | 3.6 | 36.7 |
| Michael Porter Jr. | 98% | 32.9<br><sub>34,33,21,40,26</sub> | 24.1<br><sub>26,28,10,27,13</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>7,9,0,12,7</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>1,1,0,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>5,4,0,6,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.4 | 34.1 |
| Keon Ellis | 93% | 26.1<br><sub>34,22,23,25,21</sub> | 7.5<br><sub>7,6,9,2,6</sub> |  | 2.8<br><sub>2,2,1,3,2</sub> |  | 2.0<br><sub>4,1,3,4,1</sub> |  | 1.1<br><sub>1,2,1,0,2</sub> |  | 1.5 | 0.9 | 0.8 | 12.4 |
| Noah Clowney | 98% | 25.1<br><sub>22,20,20,24,22</sub> | 9.7<br><sub>9,4,9,3,3</sub> |  | 5.2<br><sub>3,4,5,4,8</sub> |  | 1.4<br><sub>1,0,1,1,1</sub> |  | 1.4<br><sub>1,1,1,1,0</sub> |  | 0.8 | 0.7 | 1.2 | 16.3 |
| Nolan Traore | 98% | 25.0<br><sub>16,5,25,24,26</sub> | 11.6<br><sub>3,3,17,15,9</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.9<br><sub>0,0,5,3,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.6 | 2.5 | 18.1 |
| Chaney Johnson | 91% | 23.4<br><sub>5,27,21,29,19</sub> | 7.8<br><sub>0,10,4,15,6</sub> |  | 4.0<br><sub>1,5,5,3,2</sub> |  | 1.4<br><sub>0,3,0,2,0</sub> |  | 1.0<br><sub>0,2,0,3,0</sub> |  | 0.9 | 0.4 | 1.1 | 13.3 |
| Day'Ron Sharpe | 98% | 23.1<br><sub>30,23,16,17,24</sub> | 10.3<br><sub>8,7,11,4,3</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 8.5<br><sub>8,8,4,6,7</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>3,1,1,0,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>0,1,1,0,0</sub> | 0.5<br><sub>o 28% · u 72%</sub> | 1.1 | 0.7 | 1.9 | 21.2 |
| Moritz Wagner | 88% | 20.0<br><sub>16,14,15,22,23</sub> | 10.9<br><sub>7,6,13,15,16</sub> |  | 5.4<br><sub>0,4,3,4,8</sub> |  | 1.5<br><sub>1,1,1,3,1</sub> |  | 0.8<br><sub>1,1,2,2,1</sub> |  | 0.7 | 0.4 | 1.2 | 17.8 |
| Terance Mann | 52% | 17.2<br><sub>-,-,-,-,12</sub> | 5.1<br><sub>-,-,-,-,2</sub> |  | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.7<br><sub>-,-,-,-,2</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.8 | 9.2 |
| Danny Wolf | 58% | 16.1<br><sub>-,-,15,-,12</sub> | 7.2<br><sub>-,-,6,-,9</sub> |  | 4.4<br><sub>-,-,2,-,6</sub> |  | 1.7<br><sub>-,-,1,-,2</sub> |  | 0.8<br><sub>-,-,2,-,3</sub> |  | 0.5 | 0.5 | 1.1 | 13.3 |
| Drake Powell | 66% | 15.3<br><sub>-,-,12,-,6</sub> | 4.9<br><sub>-,-,0,-,0</sub> |  | 1.6<br><sub>-,-,2,-,0</sub> |  | 1.1<br><sub>-,-,3,-,2</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 7.5 |
| Josh Minott | 64% | 13.9<br><sub>-,9,21,-,3</sub> | 7.1<br><sub>-,4,15,-,2</sub> |  | 2.9<br><sub>-,2,8,-,0</sub> |  | 0.8<br><sub>-,0,2,-,0</sub> |  | 0.9<br><sub>-,0,3,-,0</sub> |  | 0.8 | 0.6 | 0.8 | 10.9 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 98% | 33.8<br><sub>29,26,37,34,29</sub> | 27.7<br><sub>23,21,20,26,13</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 7.6<br><sub>3,7,13,11,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>3,6,6,3,4</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 1.5<br><sub>3,3,1,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.4 | 3.0 | 40.1 |
| Andrew Nembhard | 84% | 33.6<br><sub>32,30,-,35,30</sub> | 18.9<br><sub>16,14,-,18,22</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>2,1,-,3,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 9.5<br><sub>5,3,-,14,9</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,4,-,1,5</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.2 | 3.3 | 31.6 |
| Kelly Oubre Jr. | 98% | 27.8<br><sub>20,20,23,30,22</sub> | 11.9<br><sub>3,14,9,15,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,2,3,3,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.1 | 0.5 | 1.4 | 18.3 |
| Jarace Walker | 97% | 27.7<br><sub>17,19,29,22,28</sub> | 13.2<br><sub>2,6,10,7,14</sub> |  | 6.4<br><sub>1,7,8,8,6</sub> |  | 3.2<br><sub>1,1,2,1,4</sub> |  | 1.6<br><sub>0,0,2,1,3</sub> |  | 1.0 | 0.5 | 2.3 | 22.8 |
| Aaron Nesmith | 91% | 27.4<br><sub>20,19,21,27,21</sub> | 15.0<br><sub>9,13,13,18,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>4,1,0,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,2,1,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,2,3,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.5 | 1.7 | 20.6 |
| Quenton Jackson | 98% | 25.7<br><sub>17,18,27,14,24</sub> | 12.0<br><sub>8,5,4,2,24</sub> |  | 3.3<br><sub>1,1,2,2,4</sub> |  | 4.8<br><sub>3,2,4,6,1</sub> |  | 0.9<br><sub>1,0,0,0,2</sub> |  | 1.2 | 0.3 | 1.7 | 20.2 |
| Jay Huff | 88% | 21.5<br><sub>5,21,23,16,19</sub> | 9.6<br><sub>0,14,6,3,13</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>2,2,6,6,1</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>0,3,1,2,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>0,2,0,1,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 1.9 | 1.0 | 15.6 |
| Kobe Brown | 52% | 19.8<br><sub>1,-,-,-,20</sub> | 7.6<br><sub>0,-,-,-,9</sub> |  | 4.0<br><sub>0,-,-,-,6</sub> |  | 1.9<br><sub>0,-,-,-,4</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.3 | 1.2 | 13.5 |
| Larry Nance Jr. | 88% | 19.1<br><sub>1,22,19,23,18</sub> | 5.8<br><sub>0,6,2,5,6</sub> |  | 3.9<br><sub>0,6,3,5,2</sub> |  | 1.2<br><sub>0,1,1,0,1</sub> |  | 0.6<br><sub>0,1,0,1,2</sub> |  | 1.1 | 0.4 | 0.8 | 10.9 |
| Jalen Slawson | 88% | 17.0<br><sub>16,8,3,12,18</sub> | 5.3<br><sub>4,1,2,2,4</sub> |  | 3.4<br><sub>5,2,1,1,4</sub> |  | 1.7<br><sub>2,0,0,1,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.8 | 0.9 | 10.4 |
| Braden Smith | 67% | 13.9<br><sub>-,-,-,5,12</sub> | 2.5<br><sub>-,-,-,0,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,1,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 4.0 |

</details>

<details><summary>if Obi Toppin plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle (BKN) | 98% | 34.6<br><sub>38,35,24,44,25</sub> | 23.2<br><sub>33,23,10,24,15</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>8,6,7,9,8</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 5.2<br><sub>7,5,7,4,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>3,2,0,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.3 | 3.6 | 36.6 |
| Michael Porter Jr. (BKN) | 98% | 32.9<br><sub>34,33,21,40,26</sub> | 23.9<br><sub>26,28,10,27,13</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 7.4<br><sub>7,9,0,12,7</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>1,1,0,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>5,4,0,6,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.3 | 33.9 |
| Keon Ellis (BKN) | 93% | 26.1<br><sub>34,22,23,25,21</sub> | 7.5<br><sub>7,6,9,2,6</sub> |  | 2.9<br><sub>2,2,1,3,2</sub> |  | 2.0<br><sub>4,1,3,4,1</sub> |  | 1.1<br><sub>1,2,1,0,2</sub> |  | 1.4 | 0.9 | 0.8 | 12.3 |
| Noah Clowney (BKN) | 98% | 25.2<br><sub>22,20,20,24,22</sub> | 9.7<br><sub>9,4,9,3,3</sub> |  | 5.2<br><sub>3,4,5,4,8</sub> |  | 1.4<br><sub>1,0,1,1,1</sub> |  | 1.4<br><sub>1,1,1,1,0</sub> |  | 0.8 | 0.7 | 1.2 | 16.3 |
| Nolan Traore (BKN) | 98% | 25.0<br><sub>16,5,25,24,26</sub> | 11.5<br><sub>3,3,17,15,9</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.9<br><sub>0,0,5,3,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.6 | 2.5 | 18.0 |
| Chaney Johnson (BKN) | 91% | 23.4<br><sub>5,27,21,29,19</sub> | 7.8<br><sub>0,10,4,15,6</sub> |  | 4.0<br><sub>1,5,5,3,2</sub> |  | 1.4<br><sub>0,3,0,2,0</sub> |  | 0.9<br><sub>0,2,0,3,0</sub> |  | 0.9 | 0.4 | 1.1 | 13.3 |
| Day'Ron Sharpe (BKN) | 98% | 23.1<br><sub>30,23,16,17,24</sub> | 10.2<br><sub>8,7,11,4,3</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 8.5<br><sub>8,8,4,6,7</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>3,1,1,0,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>0,1,1,0,0</sub> | 0.5<br><sub>o 28% · u 72%</sub> | 1.1 | 0.7 | 1.9 | 21.2 |
| Moritz Wagner (BKN) | 88% | 20.0<br><sub>16,14,15,22,23</sub> | 10.8<br><sub>7,6,13,15,16</sub> |  | 5.3<br><sub>0,4,3,4,8</sub> |  | 1.5<br><sub>1,1,1,3,1</sub> |  | 0.8<br><sub>1,1,2,2,1</sub> |  | 0.7 | 0.3 | 1.2 | 17.6 |
| Terance Mann (BKN) | 52% | 17.2<br><sub>-,-,-,-,12</sub> | 5.1<br><sub>-,-,-,-,2</sub> |  | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.7<br><sub>-,-,-,-,2</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.8 | 9.3 |
| Danny Wolf (BKN) | 58% | 16.0<br><sub>-,-,15,-,12</sub> | 7.1<br><sub>-,-,6,-,9</sub> |  | 4.4<br><sub>-,-,2,-,6</sub> |  | 1.7<br><sub>-,-,1,-,2</sub> |  | 0.8<br><sub>-,-,2,-,3</sub> |  | 0.5 | 0.5 | 1.1 | 13.2 |
| Drake Powell (BKN) | 66% | 15.3<br><sub>-,-,12,-,6</sub> | 4.8<br><sub>-,-,0,-,0</sub> |  | 1.6<br><sub>-,-,2,-,0</sub> |  | 1.1<br><sub>-,-,3,-,2</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 7.5 |
| Josh Minott (BKN) | 64% | 14.0<br><sub>-,9,21,-,3</sub> | 7.1<br><sub>-,4,15,-,2</sub> |  | 2.9<br><sub>-,2,8,-,0</sub> |  | 0.9<br><sub>-,0,2,-,0</sub> |  | 0.9<br><sub>-,0,3,-,0</sub> |  | 0.8 | 0.6 | 0.8 | 10.9 |
| Andrew Nembhard (IND) | 84% | 32.8<br><sub>32,30,-,35,30</sub> | 17.3<br><sub>16,14,-,18,22</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>2,1,-,3,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 9.1<br><sub>5,3,-,14,9</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>1,4,-,1,5</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.2 | 3.0 | 29.6 |
| Pascal Siakam (IND) | 98% | 32.5<br><sub>29,26,37,34,29</sub> | 25.3<br><sub>23,21,20,26,13</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>3,7,13,11,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>3,6,6,3,4</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,3,1,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.4 | 2.7 | 36.9 |
| Kelly Oubre Jr. (IND) | 98% | 26.8<br><sub>20,20,23,30,22</sub> | 10.9<br><sub>3,14,9,15,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>2,2,3,3,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.1 | 0.5 | 1.3 | 16.9 |
| Aaron Nesmith (IND) | 91% | 26.3<br><sub>20,19,21,27,21</sub> | 13.3<br><sub>9,13,13,18,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,1,0,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>1,2,1,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>1,2,3,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.5 | 1.6 | 18.7 |
| Jarace Walker (IND) | 97% | 26.0<br><sub>17,19,29,22,28</sub> | 11.8<br><sub>2,6,10,7,14</sub> |  | 6.0<br><sub>1,7,8,8,6</sub> |  | 2.8<br><sub>1,1,2,1,4</sub> |  | 1.6<br><sub>0,0,2,1,3</sub> |  | 0.9 | 0.4 | 1.9 | 20.6 |
| Quenton Jackson (IND) | 98% | 23.5<br><sub>17,18,27,14,24</sub> | 10.6<br><sub>8,5,4,2,24</sub> |  | 3.0<br><sub>1,1,2,2,4</sub> |  | 4.2<br><sub>3,2,4,6,1</sub> |  | 0.8<br><sub>1,0,0,0,2</sub> |  | 1.1 | 0.2 | 1.6 | 17.7 |
| Obi Toppin (IND) | 100% | 22.3<br><sub>25,20,23,22,-</sub> | 13.8<br><sub>13,16,14,13,-</sub> |  | 5.1<br><sub>5,6,6,6,-</sub> |  | 2.1<br><sub>1,2,2,0,-</sub> |  | 1.8<br><sub>0,4,2,1,-</sub> |  | 0.7 | 0.3 | 1.3 | 20.9 |
| Jay Huff (IND) | 88% | 20.0<br><sub>5,21,23,16,19</sub> | 9.2<br><sub>0,14,6,3,13</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>2,2,6,6,1</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>0,3,1,2,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>0,2,0,1,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 1.7 | 0.9 | 14.7 |
| Kobe Brown (IND) | 52% | 17.5<br><sub>1,-,-,-,20</sub> | 6.5<br><sub>0,-,-,-,9</sub> |  | 3.5<br><sub>0,-,-,-,6</sub> |  | 1.6<br><sub>0,-,-,-,4</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.3 | 1.1 | 11.6 |
| Larry Nance Jr. (IND) | 88% | 16.6<br><sub>1,22,19,23,18</sub> | 5.3<br><sub>0,6,2,5,6</sub> |  | 3.4<br><sub>0,6,3,5,2</sub> |  | 1.0<br><sub>0,1,1,0,1</sub> |  | 0.5<br><sub>0,1,0,1,2</sub> |  | 0.9 | 0.4 | 0.7 | 9.7 |
| Jalen Slawson (IND) | 88% | 14.9<br><sub>16,8,3,12,18</sub> | 4.7<br><sub>4,1,2,2,4</sub> |  | 2.9<br><sub>5,2,1,1,4</sub> |  | 1.4<br><sub>2,0,0,1,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.6 | 0.8 | 9.0 |
| Braden Smith (IND) | 67% | 12.1<br><sub>-,-,-,5,12</sub> | 2.2<br><sub>-,-,-,0,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 1.0<br><sub>-,-,-,1,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.1 | 0.6 | 3.5 |

</details>


### LAC @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Draymond Green (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg RA under 12.5 | LAC @ GSW | draftkings | 1.89 | 1.89 | 1.57 | 63.6% | 49.5% | 53.0% | +0.4% | +20.4% | 0.1% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 30.2<br><sub>32,37,36,26,31</sub> | 21.5<br><sub>30,26,16,14,24</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>1,0,4,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>4,6,11,5,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,4,2,1,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.2 | 3.6 | 30.2 |
| Rui Hachimura | 98% | 29.6<br><sub>32,33,29,-,26</sub> | 14.2<br><sub>10,16,5,-,12</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>8,6,4,-,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>2,1,0,-,0</sub> |  | 1.7<br><sub>2,3,1,-,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 1.5 | 19.6 |
| Derrick Jones Jr. | 98% | 27.4<br><sub>26,35,30,28,26</sub> | 10.7<br><sub>8,16,11,15,10</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>6,4,6,5,1</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>5,1,1,0,1</sub> |  | 1.1<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.7 | 1.0 | 16.0 |
| Kris Dunn | 98% | 27.3<br><sub>27,34,33,27,31</sub> | 7.2<br><sub>7,7,15,5,5</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>5,5,4,3,5</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 4.2<br><sub>7,5,6,3,7</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>2,1,1,1,0</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.9 | 0.3 | 1.7 | 14.9 |
| Keaton Wagler | 96% | 24.9<br><sub>29,24,26,28,25</sub> | 13.3<br><sub>15,13,11,21,12</sub> |  | 3.6<br><sub>5,3,5,4,6</sub> |  | 3.2<br><sub>5,3,4,2,3</sub> |  | 1.4<br><sub>3,2,1,3,1</sub> |  | 0.9 | 0.3 | 2.3 | 20.1 |
| Brook Lopez | 98% | 21.9<br><sub>27,20,23,22,21</sub> | 10.3<br><sub>17,22,15,2,13</sub> |  | 4.0<br><sub>11,4,1,3,6</sub> |  | 1.4<br><sub>1,0,2,3,0</sub> |  | 1.2<br><sub>1,2,3,0,1</sub> |  | 0.7 | 1.0 | 1.0 | 15.7 |
| Kobe Sanders | 96% | 20.6<br><sub>19,19,20,27,24</sub> | 8.5<br><sub>2,5,12,9,7</sub> |  | 2.4<br><sub>0,3,4,4,4</sub> |  | 1.9<br><sub>3,5,2,0,2</sub> |  | 1.1<br><sub>0,1,2,1,1</sub> |  | 1.1 | 0.1 | 1.3 | 12.7 |
| Isaiah Jackson | 97% | 20.0<br><sub>15,28,24,19,22</sub> | 8.8<br><sub>13,6,10,4,10</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>5,6,6,5,7</sub> | 7.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>0,3,4,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.1 | 1.5 | 16.5 |
| Gradey Dick | 91% | 14.2<br><sub>19,12,18,19,12</sub> | 6.3<br><sub>12,6,6,5,3</sub> |  | 2.1<br><sub>4,4,3,5,0</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 0.6<br><sub>1,0,2,1,1</sub> |  | 0.6 | 0.1 | 0.8 | 9.1 |
| Baba Miller | 86% | 10.1<br><sub>9,-,2,17,5</sub> | 4.4<br><sub>4,-,0,4,0</sub> |  | 1.6<br><sub>3,-,1,7,1</sub> |  | 1.1<br><sub>1,-,0,1,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 7.1 |
| Cam Christie | 64% | 8.2<br><sub>2,-,-,14,5</sub> | 3.0<br><sub>0,-,-,2,2</sub> |  | 1.3<br><sub>0,-,-,0,1</sub> |  | 0.6<br><sub>0,-,-,0,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.9 |
| Jalen Pickett | 52% | 7.2<br><sub>2,-,-,8,-</sub> | 2.7<br><sub>3,-,-,4,-</sub> |  | 0.9<br><sub>0,-,-,1,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 0.2<br><sub>1,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |
| Nick Martinelli | 64% | 7.1<br><sub>2,-,-,6,5</sub> | 2.9<br><sub>0,-,-,2,3</sub> |  | 1.9<br><sub>1,-,-,3,0</sub> |  | 0.5<br><sub>1,-,-,1,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.7 | 5.3 |
| Blake Wesley | 86% | 6.7<br><sub>-,-,-,-,5</sub> | 2.7<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,4</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.6 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 96% | 34.2<br><sub>37,36,31,35,24</sub> | 20.8<br><sub>18,26,31,26,6</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>13,9,12,9,1</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 3.7<br><sub>6,5,6,1,0</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,6,1,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.6 | 3.4 | 32.2 |
| Brandin Podziemski | 86% | 33.6<br><sub>33,-,33,32,33</sub> | 18.4<br><sub>18,-,18,8,21</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>2,-,7,5,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>3,-,5,6,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,-,3,0,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.2 | 2.3 | 28.9 |
| Gui Santos | 74% | 25.8<br><sub>20,23,28,-,16</sub> | 10.5<br><sub>5,7,13,-,2</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>4,4,3,-,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>2,3,1,-,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>1,1,1,-,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.1 | 0.3 | 1.7 | 18.2 |
| De'Anthony Melton | 98% | 24.9<br><sub>20,27,19,20,21</sub> | 12.1<br><sub>10,25,3,8,16</sub> |  | 3.8<br><sub>1,5,4,6,5</sub> |  | 2.9<br><sub>0,5,3,0,3</sub> |  | 1.8<br><sub>2,4,1,2,4</sub> |  | 1.5 | 0.4 | 1.8 | 18.8 |
| Georges Niang | 96% | 23.1<br><sub>13,23,18,23,19</sub> | 9.4<br><sub>4,4,9,7,11</sub> |  | 3.3<br><sub>3,4,2,3,5</sub> |  | 1.4<br><sub>0,2,0,2,1</sub> |  | 1.6<br><sub>0,0,3,1,3</sub> |  | 0.5 | 0.2 | 1.2 | 14.1 |
| Al Horford | 98% | 22.3<br><sub>19,-,19,18,17</sub> | 7.2<br><sub>3,-,11,4,3</sub> |  | 4.6<br><sub>5,-,3,5,2</sub> |  | 1.9<br><sub>0,-,0,2,0</sub> |  | 1.2<br><sub>1,-,3,0,1</sub> |  | 0.7 | 0.9 | 0.9 | 13.6 |
| Brandon Williams | 98% | 21.4<br><sub>9,24,15,14,17</sub> | 13.3<br><sub>4,20,6,11,9</sub> |  | 2.9<br><sub>2,3,3,3,2</sub> |  | 3.8<br><sub>1,5,3,1,1</sub> |  | 0.7<br><sub>0,2,2,0,0</sub> |  | 1.0 | 0.3 | 2.0 | 20.1 |
| Will Richard | 98% | 19.8<br><sub>3,31,3,23,13</sub> | 5.6<br><sub>0,11,0,6,3</sub> |  | 2.4<br><sub>0,0,0,3,3</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>0,3,0,0,1</sub> |  | 1.1 | 0.2 | 0.7 | 9.2 |
| Gary Payton II | 98% | 17.8<br><sub>11,17,12,10,8</sub> | 8.6<br><sub>7,2,7,2,2</sub> |  | 3.5<br><sub>2,1,2,2,4</sub> |  | 1.5<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>1,0,1,0,0</sub> |  | 1.1 | 0.2 | 0.9 | 13.6 |
| Graham Ike | 67% | 16.0<br><sub>12,26,3,-,-</sub> | 6.9<br><sub>10,12,3,-,-</sub> |  | 3.8<br><sub>2,10,0,-,-</sub> |  | 1.4<br><sub>1,2,1,-,-</sub> |  | 0.5<br><sub>2,0,1,-,-</sub> |  | 0.7 | 0.3 | 0.9 | 12.1 |
| Charles Bassey | 91% | 13.0<br><sub>-,13,2,2,9</sub> | 5.4<br><sub>-,10,0,0,6</sub> |  | 4.8<br><sub>-,7,1,0,4</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 10.9 |
| LJ Cryer | 52% | 13.0<br><sub>-,14,3,-,-</sub> | 5.4<br><sub>-,3,6,-,-</sub> |  | 1.2<br><sub>-,1,0,-,-</sub> |  | 1.0<br><sub>-,1,2,-,-</sub> |  | 0.8<br><sub>-,1,2,-,-</sub> |  | 0.3 | 0.1 | 0.7 | 7.6 |
| Malevy Leons | 52% | 11.3<br><sub>-,4,3,-,-</sub> | 3.4<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,1,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.6 | 0.3 | 0.6 | 6.3 |

</details>


### TOR @ LAL
Out: Kawhi Leonard (TOR), Malachi Smith (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.1–113.1 | TOR 47% | 2.12 / 1.89 | LAL -1.5 | 225.5 | LAL -4.5 covers 41%; o227.5 45% |
| Expected (weighted by chance each plays) | 111.7–113.4 | TOR 46% | 2.19 / 1.84 | LAL -1.5 | 224.5 | LAL -4.5 covers 43%; o227.5 44% |
| if Ziaire Williams plays | 111.3–113.7 | TOR 43% | 2.31 / 1.76 | LAL -2.5 | 224.5 | LAL -4.5 covers 45%; o227.5 44% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ziaire Williams (LAL) | Questionable | 55% | 23.6 | 8.5 | 2.7 | 1.3 | 1.1 | 1.4 | 0.3 | 1.0 | 12.5 | full tables below |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 35.8<br><sub>26,37,28,31,39</sub> | 22.4<br><sub>23,28,0,28,41</sub> |  | 6.9<br><sub>6,14,3,6,5</sub> |  | 6.9<br><sub>5,5,3,4,5</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 2.0 | 1.1 | 3.3 | 36.2 |
| RJ Barrett | 98% | 34.6<br><sub>26,34,32,32,34</sub> | 21.1<br><sub>20,23,20,25,9</sub> |  | 5.7<br><sub>4,9,2,9,3</sub> |  | 4.0<br><sub>3,4,2,6,5</sub> |  | 1.9<br><sub>0,1,0,3,1</sub> |  | 1.0 | 0.3 | 2.6 | 30.9 |
| Immanuel Quickley | 98% | 32.4<br><sub>28,29,28,29,37</sub> | 17.4<br><sub>23,12,19,16,17</sub> |  | 3.7<br><sub>4,1,3,3,6</sub> |  | 6.1<br><sub>7,6,2,7,8</sub> |  | 2.4<br><sub>4,0,3,4,4</sub> |  | 1.4 | 0.1 | 1.8 | 27.2 |
| Ja'Kobe Walter | 98% | 30.2<br><sub>23,24,31,28,32</sub> | 11.3<br><sub>10,7,22,14,9</sub> |  | 3.5<br><sub>3,4,4,5,3</sub> |  | 1.9<br><sub>4,2,2,2,1</sub> |  | 2.0<br><sub>1,2,5,3,3</sub> |  | 1.7 | 0.3 | 1.0 | 16.7 |
| Jamal Shead | 98% | 24.8<br><sub>16,24,21,23,23</sub> | 7.4<br><sub>2,5,4,13,2</sub> |  | 1.9<br><sub>2,2,1,4,1</sub> |  | 5.1<br><sub>5,5,0,7,8</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.2 | 0.2 | 1.9 | 14.4 |
| Collin Murray-Boyles | 98% | 23.5<br><sub>20,18,19,15,23</sub> | 10.1<br><sub>6,8,3,10,15</sub> |  | 5.6<br><sub>8,3,7,2,5</sub> |  | 1.9<br><sub>3,0,2,1,1</sub> |  | 0.3<br><sub>0,0,0,2,1</sub> |  | 1.2 | 0.8 | 1.3 | 17.6 |
| Jakob Poeltl | 98% | 21.8<br><sub>22,27,19,10,23</sub> | 8.3<br><sub>3,6,0,2,12</sub> |  | 6.2<br><sub>6,9,1,2,11</sub> |  | 1.4<br><sub>0,2,0,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.6 | 1.2 | 15.9 |
| Jamison Battle | 96% | 16.8<br><sub>11,12,13,20,19</sub> | 5.8<br><sub>8,5,4,7,2</sub> |  | 2.2<br><sub>5,0,1,0,0</sub> |  | 0.8<br><sub>0,0,2,1,0</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.4 | 0.1 | 0.5 | 8.9 |
| Allen Graves | 96% | 14.1<br><sub>19,6,20,18,9</sub> | 4.5<br><sub>5,2,11,3,7</sub> |  | 3.0<br><sub>5,2,6,1,4</sub> |  | 0.7<br><sub>0,0,4,0,0</sub> |  | 0.3<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.5 | 0.8 | 8.1 |
| Kyle Anderson | 58% | 9.8<br><sub>5,-,11,5,-</sub> | 2.8<br><sub>0,-,0,0,-</sub> |  | 1.8<br><sub>1,-,2,0,-</sub> |  | 1.5<br><sub>2,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 6.1 |
| Trayce Jackson-Davis | 91% | 8.2<br><sub>10,1,6,20,1</sub> | 3.2<br><sub>9,0,3,6,0</sub> |  | 2.5<br><sub>1,0,1,11,0</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 6.4 |
| Alijah Martin | 67% | 6.1<br><sub>5,1,7,5,-</sub> | 2.4<br><sub>3,0,2,5,-</sub> |  | 0.9<br><sub>0,0,2,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.8 |
| Jaden Bradley | 67% | 5.9<br><sub>5,1,5,5,-</sub> | 2.0<br><sub>0,0,6,0,-</sub> |  | 0.9<br><sub>0,0,1,1,-</sub> |  | 0.5<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.4 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.7<br><sub>37,38,37,-,37</sub> | 31.6<br><sub>23,52,41,-,37</sub> |  | 7.0<br><sub>6,8,5,-,7</sub> |  | 7.4<br><sub>7,10,9,-,5</sub> |  | 4.2<br><sub>2,8,6,-,6</sub> |  | 1.6 | 0.5 | 4.7 | 46.0 |
| Austin Reaves | 98% | 35.9<br><sub>38,36,39,31,37</sub> | 20.4<br><sub>28,29,26,16,21</sub> |  | 4.2<br><sub>2,1,4,6,4</sub> |  | 5.0<br><sub>9,4,7,1,5</sub> |  | 2.1<br><sub>3,4,4,1,1</sub> |  | 1.0 | 0.5 | 3.6 | 29.6 |
| Walker Kessler | 98% | 30.3<br><sub>35,28,33,26,31</sub> | 10.8<br><sub>22,2,13,11,10</sub> |  | 10.2<br><sub>8,7,8,9,13</sub> |  | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.2 | 1.6 | 22.5 |
| Quentin Grimes | 98% | 26.7<br><sub>31,20,19,38,26</sub> | 9.3<br><sub>13,3,2,23,3</sub> |  | 3.2<br><sub>8,1,4,3,3</sub> |  | 2.2<br><sub>4,1,0,5,2</sub> |  | 1.1<br><sub>3,0,0,0,1</sub> |  | 0.8 | 0.3 | 1.2 | 14.7 |
| Matisse Thybulle | 96% | 24.4<br><sub>24,26,22,28,28</sub> | 7.7<br><sub>13,11,5,15,10</sub> |  | 2.4<br><sub>1,1,2,1,3</sub> |  | 1.1<br><sub>2,1,1,0,0</sub> |  | 1.2<br><sub>3,3,1,4,1</sub> |  | 1.8 | 0.7 | 1.0 | 11.2 |
| Jake LaRavia | 93% | 24.1<br><sub>-,15,19,35,28</sub> | 6.5<br><sub>-,0,5,2,10</sub> |  | 3.7<br><sub>-,4,1,10,2</sub> |  | 1.2<br><sub>-,1,1,0,0</sub> |  | 0.7<br><sub>-,0,1,0,2</sub> |  | 1.2 | 0.6 | 1.3 | 11.4 |
| Sandro Mamukelashvili | 98% | 23.1<br><sub>24,21,24,30,20</sub> | 9.0<br><sub>7,9,17,13,4</sub> |  | 5.3<br><sub>5,3,4,8,7</sub> |  | 1.4<br><sub>2,0,2,3,0</sub> |  | 1.1<br><sub>1,1,3,0,0</sub> |  | 0.8 | 0.5 | 1.0 | 15.8 |
| Collin Sexton | 98% | 18.2<br><sub>16,20,14,21,16</sub> | 10.2<br><sub>5,13,9,21,0</sub> |  | 1.9<br><sub>1,2,1,4,2</sub> |  | 1.8<br><sub>2,1,4,2,1</sub> |  | 1.1<br><sub>1,1,0,4,0</sub> |  | 0.8 | 0.2 | 1.6 | 13.9 |
| Lawson Lovering | 16% | 14.5 | 4.2 |  | 3.6 |  | 0.9 |  | 0.1 |  | 0.5 | 0.4 | 0.7 | 8.7 |
| Jarred Vanderbilt | 52% | 14.2<br><sub>-,-,-,21,13</sub> | 3.4<br><sub>-,-,-,0,0</sub> |  | 3.6<br><sub>-,-,-,7,3</sub> |  | 1.1<br><sub>-,-,-,2,3</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.1 |
| Cameron Carr | 16% | 12.5 | 5.3 |  | 2.2 |  | 1.1 |  | 0.4 |  | 0.4 | 0.3 | 0.6 | 8.7 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Kevon Looney | 52% | 8.0<br><sub>5,5,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 2.7<br><sub>1,2,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 5.2 |
| Jaden Hardy | 63% | 7.6<br><sub>-,-,-,9,1</sub> | 3.7<br><sub>-,-,-,2,0</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Chris Manon | 58% | 5.7<br><sub>-,-,-,-,1</sub> | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.2 |
| Bronny James | 48% | 5.6<br><sub>-,-,-,-,1</sub> | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 2.7 |

</details>

<details><summary>if Ziaire Williams plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 35.5<br><sub>37,38,37,-,37</sub> | 30.1<br><sub>23,52,41,-,37</sub> |  | 7.1<br><sub>6,8,5,-,7</sub> |  | 7.2<br><sub>7,10,9,-,5</sub> |  | 3.9<br><sub>2,8,6,-,6</sub> |  | 1.6 | 0.5 | 4.3 | 44.4 |
| Austin Reaves (LAL) | 98% | 34.5<br><sub>38,36,39,31,37</sub> | 19.7<br><sub>28,29,26,16,21</sub> |  | 4.1<br><sub>2,1,4,6,4</sub> |  | 5.0<br><sub>9,4,7,1,5</sub> |  | 2.1<br><sub>3,4,4,1,1</sub> |  | 1.0 | 0.5 | 3.4 | 28.8 |
| Walker Kessler (LAL) | 98% | 28.1<br><sub>35,28,33,26,31</sub> | 10.5<br><sub>22,2,13,11,10</sub> |  | 9.7<br><sub>8,7,8,9,13</sub> |  | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.7 | 2.1 | 1.6 | 21.6 |
| Quentin Grimes (LAL) | 98% | 23.6<br><sub>31,20,19,38,26</sub> | 8.3<br><sub>13,3,2,23,3</sub> |  | 2.9<br><sub>8,1,4,3,3</sub> |  | 2.1<br><sub>4,1,0,5,2</sub> |  | 0.9<br><sub>3,0,0,0,1</sub> |  | 0.8 | 0.3 | 1.1 | 13.3 |
| Ziaire Williams (LAL) | 100% | 23.6<br><sub>31,30,29,-,-</sub> | 8.5<br><sub>14,11,11,-,-</sub> |  | 2.7<br><sub>5,2,2,-,-</sub> |  | 1.3<br><sub>0,1,4,-,-</sub> |  | 1.1<br><sub>1,3,2,-,-</sub> |  | 1.4 | 0.3 | 1.0 | 12.5 |
| Matisse Thybulle (LAL) | 96% | 21.1<br><sub>24,26,22,28,28</sub> | 6.8<br><sub>13,11,5,15,10</sub> |  | 2.1<br><sub>1,1,2,1,3</sub> |  | 0.9<br><sub>2,1,1,0,0</sub> |  | 1.0<br><sub>3,3,1,4,1</sub> |  | 1.7 | 0.6 | 1.0 | 9.8 |
| Jake LaRavia (LAL) | 93% | 20.6<br><sub>-,15,19,35,28</sub> | 5.4<br><sub>-,0,5,2,10</sub> |  | 3.3<br><sub>-,4,1,10,2</sub> |  | 1.1<br><sub>-,1,1,0,0</sub> |  | 0.5<br><sub>-,0,1,0,2</sub> |  | 1.1 | 0.5 | 1.1 | 9.7 |
| Sandro Mamukelashvili (LAL) | 98% | 20.5<br><sub>24,21,24,30,20</sub> | 8.2<br><sub>7,9,17,13,4</sub> |  | 4.8<br><sub>5,3,4,8,7</sub> |  | 1.3<br><sub>2,0,2,3,0</sub> |  | 0.9<br><sub>1,1,3,0,0</sub> |  | 0.8 | 0.5 | 0.9 | 14.4 |
| Collin Sexton (LAL) | 98% | 17.0<br><sub>16,20,14,21,16</sub> | 9.8<br><sub>5,13,9,21,0</sub> |  | 1.9<br><sub>1,2,1,4,2</sub> |  | 1.8<br><sub>2,1,4,2,1</sub> |  | 1.0<br><sub>1,1,0,4,0</sub> |  | 0.8 | 0.1 | 1.6 | 13.4 |
| Lawson Lovering (LAL) | 16% | 12.4 | 3.8 |  | 3.2 |  | 0.8 |  | 0.1 |  | 0.5 | 0.3 | 0.6 | 7.8 |
| Cameron Carr (LAL) | 16% | 12.3 | 5.2 |  | 2.2 |  | 1.1 |  | 0.4 |  | 0.3 | 0.2 | 0.6 | 8.5 |
| Jarred Vanderbilt (LAL) | 52% | 12.0<br><sub>-,-,-,21,13</sub> | 3.2<br><sub>-,-,-,0,0</sub> |  | 3.2<br><sub>-,-,-,7,3</sub> |  | 0.9<br><sub>-,-,-,2,3</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.3 |
| AK Okereke (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Jaden Hardy (LAL) | 63% | 6.6<br><sub>-,-,-,9,1</sub> | 3.5<br><sub>-,-,-,2,0</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.6 |
| Kevon Looney (LAL) | 52% | 6.5<br><sub>5,5,5,-,-</sub> | 1.7<br><sub>0,2,0,-,-</sub> |  | 2.3<br><sub>1,2,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.5 |
| Bronny James (LAL) | 48% | 5.3<br><sub>-,-,-,-,1</sub> | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 2.6 |
| Chris Manon (LAL) | 58% | 5.3<br><sub>-,-,-,-,1</sub> | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 3.1 |
| Scottie Barnes (TOR) | 98% | 35.8<br><sub>26,37,28,31,39</sub> | 22.4<br><sub>23,28,0,28,41</sub> |  | 6.9<br><sub>6,14,3,6,5</sub> |  | 6.9<br><sub>5,5,3,4,5</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 2.0 | 1.1 | 3.4 | 36.2 |
| RJ Barrett (TOR) | 98% | 34.7<br><sub>26,34,32,32,34</sub> | 21.3<br><sub>20,23,20,25,9</sub> |  | 5.8<br><sub>4,9,2,9,3</sub> |  | 4.0<br><sub>3,4,2,6,5</sub> |  | 1.9<br><sub>0,1,0,3,1</sub> |  | 1.0 | 0.3 | 2.6 | 31.1 |
| Immanuel Quickley (TOR) | 98% | 32.5<br><sub>28,29,28,29,37</sub> | 17.4<br><sub>23,12,19,16,17</sub> |  | 3.8<br><sub>4,1,3,3,6</sub> |  | 6.1<br><sub>7,6,2,7,8</sub> |  | 2.4<br><sub>4,0,3,4,4</sub> |  | 1.4 | 0.1 | 1.8 | 27.2 |
| Ja'Kobe Walter (TOR) | 98% | 30.3<br><sub>23,24,31,28,32</sub> | 11.3<br><sub>10,7,22,14,9</sub> |  | 3.5<br><sub>3,4,4,5,3</sub> |  | 1.9<br><sub>4,2,2,2,1</sub> |  | 2.0<br><sub>1,2,5,3,3</sub> |  | 1.7 | 0.3 | 1.0 | 16.7 |
| Jamal Shead (TOR) | 98% | 24.8<br><sub>16,24,21,23,23</sub> | 7.4<br><sub>2,5,4,13,2</sub> |  | 1.9<br><sub>2,2,1,4,1</sub> |  | 5.1<br><sub>5,5,0,7,8</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.1 | 0.2 | 1.9 | 14.5 |
| Collin Murray-Boyles (TOR) | 98% | 23.4<br><sub>20,18,19,15,23</sub> | 10.0<br><sub>6,8,3,10,15</sub> |  | 5.6<br><sub>8,3,7,2,5</sub> |  | 1.9<br><sub>3,0,2,1,1</sub> |  | 0.3<br><sub>0,0,0,2,1</sub> |  | 1.2 | 0.7 | 1.3 | 17.5 |
| Jakob Poeltl (TOR) | 98% | 21.8<br><sub>22,27,19,10,23</sub> | 8.2<br><sub>3,6,0,2,12</sub> |  | 6.2<br><sub>6,9,1,2,11</sub> |  | 1.4<br><sub>0,2,0,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.6 | 1.2 | 15.8 |
| Jamison Battle (TOR) | 96% | 16.7<br><sub>11,12,13,20,19</sub> | 5.9<br><sub>8,5,4,7,2</sub> |  | 2.2<br><sub>5,0,1,0,0</sub> |  | 0.8<br><sub>0,0,2,1,0</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.1 | 0.5 | 8.9 |
| Allen Graves (TOR) | 96% | 14.1<br><sub>19,6,20,18,9</sub> | 4.4<br><sub>5,2,11,3,7</sub> |  | 3.0<br><sub>5,2,6,1,4</sub> |  | 0.7<br><sub>0,0,4,0,0</sub> |  | 0.3<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.5 | 0.8 | 8.1 |
| Kyle Anderson (TOR) | 58% | 9.7<br><sub>5,-,11,5,-</sub> | 2.8<br><sub>0,-,0,0,-</sub> |  | 1.9<br><sub>1,-,2,0,-</sub> |  | 1.5<br><sub>2,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 6.1 |
| Trayce Jackson-Davis (TOR) | 91% | 8.2<br><sub>10,1,6,20,1</sub> | 3.2<br><sub>9,0,3,6,0</sub> |  | 2.5<br><sub>1,0,1,11,0</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 6.4 |
| Alijah Martin (TOR) | 67% | 6.1<br><sub>5,1,7,5,-</sub> | 2.4<br><sub>3,0,2,5,-</sub> |  | 0.9<br><sub>0,0,2,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.8 |
| Jaden Bradley (TOR) | 67% | 5.9<br><sub>5,1,5,5,-</sub> | 2.0<br><sub>0,0,6,0,-</sub> |  | 1.0<br><sub>0,0,1,1,-</sub> |  | 0.5<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-01/`._
