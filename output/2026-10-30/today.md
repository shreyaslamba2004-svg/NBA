# NBA model · Fri 30 Oct 2026 (US date)

Updated **Sat 31 Oct, 12:24 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-30/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| DeMar DeRozan AST over 5.5 (6+) | DEN @ PHX | draftkings | 10.80 | 9.44 | 6.10 | 16.4% | 8.6% | 10.6% | +14.3% | +77.0% | 0.4% |
| DeMar DeRozan PRA over 29.5 (30+) | DEN @ PHX | draftkings | 13.20 | 11.72 | 7.76 | 12.9% | 7.1% | 8.5% | +12.6% | +70.1% | 0.3% |
| DeMar DeRozan PA over 24.5 (25+) | DEN @ PHX | draftkings | 9.30 | 8.35 | 5.63 | 17.8% | 10.1% | 12.0% | +11.4% | +65.2% | 0.3% |
| DeMar DeRozan PA over 29.5 (30+) | DEN @ PHX | draftkings | 22.00 | 20.00 | 13.79 | 7.2% | 4.2% | 5.0% | +10.0% | +59.5% | 0.1% |
| DeMar DeRozan PTS over 24.5 (25+) | DEN @ PHX | draftkings | 18.80 | 17.30 | 12.17 | 8.2% | 5.0% | 5.8% | +8.7% | +54.4% | 0.1% |
| DeMar DeRozan PRA over 24.5 (25+) | DEN @ PHX | draftkings | 5.36 | 4.95 | 3.51 | 28.4% | 17.4% | 20.2% | +8.2% | +52.5% | 0.5% |
| Nikola Jokic AST over 15.5 (16+) | DEN @ PHX | draftkings | 13.80 | 13.02 | 9.61 | 10.4% | 6.8% | 7.7% | +6.0% | +43.6% | 0.1% |
| DeMar DeRozan PR over 24.5 (25+) | DEN @ PHX | draftkings | 9.70 | 9.19 | 6.83 | 14.6% | 9.6% | 10.9% | +5.6% | +41.9% | 0.2% |
| DeMar DeRozan PRA over 34.5 (35+) | DEN @ PHX | draftkings | 26.00 | 24.69 | 18.46 | 5.4% | 3.6% | 4.0% | +5.3% | +40.8% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| DeMar DeRozan AST over 6.5 (7+) | DEN @ PHX | draftkings | 19.60 | 17.33 | 11.38 | 8.8% | 4.8% | 5.8% | +13.2% | +72.2% | 0.2% |
| DeMar DeRozan AST over 4.5 (5+) | DEN @ PHX | draftkings | 5.73 | 5.14 | 3.46 | 28.9% | 16.3% | 19.5% | +11.5% | +65.8% | 0.6% |
| Nikola Jokic AST over 14.5 (15+) | DEN @ PHX | draftkings | 9.40 | 8.94 | 6.71 | 14.9% | 9.9% | 11.2% | +5.1% | +40.0% | 0.1% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Khaman Maluach PR under 15.5 | DEN @ PHX | draftkings | 1.94 | 1.81 | 1.30 | 77.1% | 48.1% | 55.4% | +7.6% | +49.9% | 2.0% |
| Khaman Maluach REB under 7.5 | DEN @ PHX | draftkings | 2.01 | 1.87 | 1.34 | 74.6% | 46.5% | 53.5% | +7.6% | +49.9% | 1.9% |
| Walker Kessler PTS under 13.5 | LAL @ GSW | sportsbet | 2.02 | 1.89 | 1.42 | 70.3% | 47.3% | 53.0% | +7.1% | +41.9% | 1.8% |
| Walker Kessler PTS under 14.5 | LAL @ GSW | neds | 1.83 | 1.72 | 1.32 | 76.0% | 52.1% | 58.1% | +6.5% | +39.3% | 1.9% |
| DeMar DeRozan AST over 3.5 (4+) | DEN @ PHX | draftkings | 3.10 | 2.93 | 2.17 | 46.1% | 30.1% | 34.1% | +5.8% | +43.0% | 0.7% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play).

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ GSW | Sat 31 Oct 13:00 | 114.4–115.0 | LAL 49% | 2.04 / 1.96 | GSW +0.5 | 229.5 | GSW +3.5 covers 60%; o234.5 39% |
| DEN @ PHX | Sat 31 Oct 13:00 | 115.1–113.1 | DEN 56% | 1.80 / 2.26 | PHX +2.5 | 227.5 | PHX +3.5 covers 54%; o231.5 42% |

### LAL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Ziaire Williams (LAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Austin Reaves PTS under 22.5 | LAL @ GSW | sportsbet | 2.00 | 1.95 | 1.66 | 60.2% | 48.1% | 51.2% | +2.4% | +20.5% | 0.6% |
| De'Anthony Melton PTS over 9.5 (10+) | LAL @ GSW | draftkings | 2.18 | 2.14 | 2.58 | 38.8% | 49.3% | 46.7% | +1.7% | -15.4% | 0.4% |
| Austin Reaves PTS under 23.5 | LAL @ GSW | pointsbetau | 1.87 | 1.84 | 1.56 | 64.2% | 51.1% | 54.4% | +1.7% | +20.1% | 0.5% |
| Stephen Curry PTS under 24.5 | LAL @ GSW | sportsbet | 1.96 | 1.94 | 1.69 | 59.3% | 49.1% | 51.6% | +1.3% | +16.4% | 0.3% |
| Brandin Podziemski PTS under 15.5 | LAL @ GSW | tab | 1.87 | 1.85 | 1.66 | 60.3% | 51.9% | 54.0% | +1.0% | +12.7% | 0.3% |
| Stephen Curry PTS under 25.5 | LAL @ GSW | tab | 1.85 | 1.83 | 1.58 | 63.2% | 51.7% | 54.6% | +0.8% | +16.7% | 0.2% |
| Yaxel Lendeborg PTS over 19.5 (20+) | LAL @ GSW | pointsbetau | 2.00 | 1.99 | 1.91 | 52.5% | 49.6% | 50.3% | +0.6% | +5.0% | 0.2% |
| Gui Santos PTS under 9.5 | LAL @ GSW | tab | 1.85 | 1.84 | 1.74 | 57.4% | 53.4% | 54.4% | +0.5% | +6.1% | 0.1% |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.5<br><sub>30,37,38,37,-</sub> | 34.2<br><sub>28,23,52,41,-</sub> | 33.5 · 34.5 | 7.1<br><sub>8,6,8,5,-</sub> | 7.5 | 8.1<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.4 |
| Austin Reaves | 98% | 35.6<br><sub>32,38,36,39,31</sub> | 21.4<br><sub>23,28,29,26,16</sub> | 23.5 · 22.5 | 4.1<br><sub>4,2,1,4,6</sub> | 4.5 | 5.5<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 31.1 |
| Walker Kessler | 98% | 29.7<br><sub>30,35,28,33,26</sub> | 11.2<br><sub>26,22,2,13,11</sub> | 13.5 · 13.5 | 9.9<br><sub>9,8,7,8,9</sub> | 9.5 | 1.5<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.6 |
| Quentin Grimes | 98% | 27.0<br><sub>27,31,20,19,38</sub> | 10.0<br><sub>10,13,3,2,23</sub> | 9.5 · 9.5 | 3.2<br><sub>2,8,1,4,3</sub> | 3.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.6 |
| Sandro Mamukelashvili | 98% | 24.8<br><sub>22,24,21,24,30</sub> | 9.7<br><sub>5,7,9,17,13</sub> | 9.5 · 9.5 | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> | 1.5 | 0.9 | 0.5 | 1.0 | 16.9 |
| Jake LaRavia | 91% | 23.9<br><sub>18,-,15,19,35</sub> | 5.8<br><sub>10,-,0,5,2</sub> |  | 3.8<br><sub>2,-,4,1,10</sub> |  | 1.4<br><sub>2,-,1,1,0</sub> |  | 0.5<br><sub>2,-,0,1,0</sub> |  | 1.4 | 0.6 | 1.2 | 11.1 |
| Matisse Thybulle | 96% | 23.2<br><sub>23,24,26,22,28</sub> | 6.5<br><sub>3,13,11,5,15</sub> | 6.5 · 6.5 | 2.2<br><sub>3,1,1,2,1</sub> | 2.5 | 1.2<br><sub>1,2,1,1,0</sub> |  | 1.1<br><sub>1,3,3,1,4</sub> | 1.5 | 2.0 | 0.7 | 1.0 | 9.9 |
| Collin Sexton | 98% | 19.2<br><sub>-,16,20,14,21</sub> | 11.5<br><sub>-,5,13,9,21</sub> | 11.5 · 11.5 | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> | 2.5 | 1.3<br><sub>-,1,1,0,4</sub> | 1.5 | 1.1 | 0.1 | 1.7 | 15.7 |
| Jarred Vanderbilt | 48% | 16.6<br><sub>-,-,-,-,21</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 4.2<br><sub>-,-,-,-,7</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 9.7 |
| Lawson Lovering | 23% | 14.0 | 4.2 |  | 3.4 |  | 1.0 |  | 0.1 |  | 0.7 | 0.3 | 0.7 | 8.5 |
| Jaden Hardy | 52% | 9.2<br><sub>7,-,-,-,9</sub> | 4.4<br><sub>3,-,-,-,2</sub> |  | 0.8<br><sub>2,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 5.9 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke | 30% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 64% | 8.1<br><sub>15,5,5,5,-</sub> | 2.0<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.2 |
| Bronny James | 26% | 6.2<br><sub>7,-,-,-,-</sub> | 2.1<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 2.7 |
| Chris Manon | 52% | 5.9<br><sub>6,-,-,-,-</sub> | 1.6<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 96% | 34.3<br><sub>29,37,36,31,35</sub> | 21.1<br><sub>12,18,26,31,26</sub> | 19.5 · 19.5 | 8.2<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.0 | 33.2 |
| Brandin Podziemski | 80% | 30.7<br><sub>-,33,-,33,32</sub> | 14.7<br><sub>-,18,-,18,8</sub> | 14.5 · 14.5 | 4.8<br><sub>-,2,-,7,5</sub> | 5.5 | 4.0<br><sub>-,3,-,5,6</sub> | 3.5 | 1.8<br><sub>-,2,-,3,0</sub> | 2.5 | 1.2 | 0.2 | 1.8 | 23.4 |
| Stephen Curry | 98% | 30.3<br><sub>21,30,-,27,32</sub> | 23.4<br><sub>23,24,-,24,44</sub> | 24.5 · 24.5 | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.4<br><sub>1,4,-,3,6</sub> | 4.5 | 3.6<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 2.9 | 31.3 |
| Draymond Green | 83% | 26.9<br><sub>21,31,-,27,32</sub> | 7.5<br><sub>2,5,-,3,3</sub> | 5.5 · 5.5 | 5.1<br><sub>4,5,-,4,9</sub> | 5.5 | 5.6<br><sub>8,6,-,7,6</sub> | 5.5 | 0.9<br><sub>0,1,-,1,0</sub> | 0.5 | 1.1 | 0.6 | 2.4 | 18.2 |
| Gui Santos | 71% | 23.5<br><sub>25,20,23,28,-</sub> | 9.3<br><sub>12,5,7,13,-</sub> | 8.5 · 9.5 | 4.2<br><sub>5,4,4,3,-</sub> | 4.5 | 2.3<br><sub>0,2,3,1,-</sub> |  | 1.1<br><sub>1,1,1,1,-</sub> | 0.5 | 1.1 | 0.3 | 1.5 | 15.7 |
| De'Anthony Melton | 98% | 20.0<br><sub>21,20,27,19,20</sub> | 8.8<br><sub>0,10,25,3,8</sub> | 8.5 · 8.5 | 2.9<br><sub>2,1,5,4,6</sub> | 2.5 | 2.1<br><sub>2,0,5,3,0</sub> | 2.5 | 1.2<br><sub>0,2,4,1,2</sub> | 1.5 | 1.3 | 0.3 | 1.4 | 13.8 |
| Al Horford | 98% | 17.6<br><sub>17,19,-,19,18</sub> | 5.4<br><sub>0,3,-,11,4</sub> | 5.5 · 5.5 | 3.9<br><sub>4,5,-,3,5</sub> | 3.5 | 1.4<br><sub>2,0,-,0,2</sub> |  | 0.8<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.7 | 0.6 | 10.7 |
| Georges Niang | 93% | 17.5<br><sub>20,13,23,18,23</sub> | 7.1<br><sub>7,4,4,9,7</sub> | 6.5 · 6.5 | 2.3<br><sub>2,3,4,2,3</sub> |  | 0.9<br><sub>2,0,2,0,2</sub> |  | 1.1<br><sub>0,0,0,3,1</sub> | 1.5 | 0.5 | 0.1 | 0.9 | 10.3 |
| Brandon Williams | 98% | 15.4<br><sub>18,9,24,15,14</sub> | 9.1<br><sub>14,4,20,6,11</sub> |  | 2.1<br><sub>4,2,3,3,3</sub> |  | 2.6<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.2 | 1.4 | 13.8 |
| Will Richard | 98% | 15.3<br><sub>20,3,31,3,23</sub> | 4.5<br><sub>8,0,11,0,6</sub> |  | 1.7<br><sub>5,0,0,0,3</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>0,0,3,0,0</sub> |  | 1.0 | 0.1 | 0.5 | 7.0 |
| Gary Payton II | 98% | 12.7<br><sub>18,11,17,12,10</sub> | 6.1<br><sub>10,7,2,7,2</sub> |  | 2.5<br><sub>1,2,1,2,2</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.6 | 9.6 |
| Graham Ike | 67% | 8.8<br><sub>12,12,26,3,-</sub> | 4.2<br><sub>8,10,12,3,-</sub> |  | 2.1<br><sub>2,2,10,0,-</sub> |  | 0.8<br><sub>1,1,2,1,-</sub> |  | 0.2<br><sub>1,2,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.0 |
| Charles Bassey | 91% | 7.9<br><sub>-,-,13,2,2</sub> | 3.4<br><sub>-,-,10,0,0</sub> |  | 3.0<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 6.8 |
| LJ Cryer | 63% | 6.9<br><sub>9,-,14,3,-</sub> | 3.1<br><sub>9,-,3,6,-</sub> |  | 0.7<br><sub>1,-,1,0,-</sub> |  | 0.6<br><sub>3,-,1,2,-</sub> |  | 0.4<br><sub>2,-,1,2,-</sub> |  | 0.1 | 0.0 | 0.4 | 4.3 |
| Malevy Leons | 58% | 6.4<br><sub>9,-,4,3,-</sub> | 2.1<br><sub>0,-,2,0,-</sub> |  | 1.1<br><sub>1,-,0,1,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.3 | 3.7 |

</details>


### DEN @ PHX
Out: Drew Timme (PHX), Mark Williams (PHX), Julian Strawther (DEN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Miles Bridges PTS under 15.5 | DEN @ PHX | tab | 1.95 | 1.87 | 1.61 | 62.0% | 50.7% | 53.5% | +4.5% | +21.0% | 1.2% |
| Aaron Gordon PTS under 14.5 | DEN @ PHX | pointsbetau | 2.00 | 1.92 | 1.66 | 60.1% | 49.6% | 52.2% | +4.4% | +20.2% | 1.1% |
| DeMar DeRozan PRA over 17.5 (18+) | DEN @ PHX | draftkings | 1.91 | 1.90 | 1.58 | 63.4% | 49.2% | 52.7% | +0.7% | +21.1% | 0.2% |
| Miles Bridges PR under 21.5 | DEN @ PHX | draftkings | 1.97 | 1.96 | 1.63 | 61.4% | 47.4% | 50.9% | +0.3% | +21.0% | 0.1% |
| Miles Bridges PRA under 24.5 | DEN @ PHX | draftkings | 1.93 | 1.93 | 1.60 | 62.5% | 48.3% | 51.9% | +0.3% | +21.0% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.1–113.1 | DEN 56% | 1.80 / 2.26 | PHX +2.5 | 227.5 | PHX +3.5 covers 54%; o231.5 42% |
| Expected (weighted by chance each plays) | 115.3–113.5 | DEN 55% | 1.83 / 2.20 | PHX +2.5 | 228.5 | PHX +3.5 covers 55%; o231.5 44% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Johnson (DEN) | Questionable | 55% | 19.9 | 8.1 | 2.8 | 1.5 | 1.1 | 0.6 | 0.3 | 0.8 | 12.4 | small |
| Alpha Diallo (DEN) | Doubtful | 20% | 14.4 | 3.6 | 1.8 | 1.1 | 0.3 | 0.7 | 0.3 | 0.9 | 6.5 | small |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 37.7<br><sub>37,43,36,38</sub> | 23.8<br><sub>6,42,19,23</sub> | 22.5 · 22.5 | 4.3<br><sub>10,3,6,1</sub> | 4.5 | 6.1<br><sub>3,6,8,6</sub> | 6.5 | 3.4<br><sub>0,8,3,5</sub> | 2.5 | 1.1 | 0.5 | 2.7 | 34.3 |
| Nikola Jokic | 98% | 37.0<br><sub>35,44,35,34</sub> | 25.5<br><sub>13,35,19,21</sub> | 25.5 · 25.5 | 12.8<br><sub>7,15,7,13</sub> | 11.5 | 10.2<br><sub>5,10,11,10</sub> | 9.5 | 1.6<br><sub>1,3,1,0</sub> | 1.5 | 1.6 | 0.9 | 4.0 | 48.5 |
| Christian Braun | 98% | 34.7<br><sub>33,40,34,36</sub> | 12.3<br><sub>7,15,9,15</sub> | 11.5 · 11.5 | 4.7<br><sub>6,8,4,0</sub> | 4.5 | 2.4<br><sub>1,2,2,4</sub> |  | 1.2<br><sub>1,0,1,3</sub> | 1.5 | 1.1 | 0.4 | 1.3 | 19.5 |
| Aaron Gordon | 98% | 31.2<br><sub>29,37,25,31</sub> | 14.1<br><sub>20,7,7,15</sub> | 14.5 · 14.5 | 6.1<br><sub>6,5,4,11</sub> | 5.5 | 2.7<br><sub>1,4,2,3</sub> | 2.5 | 1.5<br><sub>3,1,0,2</sub> | 1.5 | 0.8 | 0.3 | 1.5 | 22.9 |
| DeMar DeRozan | 98% | 28.1<br><sub>28,24,29,26</sub> | 14.9<br><sub>13,12,21,6</sub> | 12.5 · 12.5 | 2.7<br><sub>2,3,4,2</sub> | 2.5 | 3.5<br><sub>0,3,2,5</sub> | 2.5 | 0.6<br><sub>0,0,2,0</sub> | 0.5 | 0.9 | 0.3 | 1.8 | 21.2 |
| Trevon Brazile | 93% | 25.9<br><sub>18,28,17,32</sub> | 8.7<br><sub>4,17,6,11</sub> | 6.5 · 7.5 | 6.3<br><sub>12,9,1,8</sub> | 4.5 | 1.1<br><sub>0,0,0,0</sub> |  | 1.1<br><sub>0,3,1,1</sub> |  | 0.8 | 0.5 | 1.3 | 16.1 |
| Marvin Bagley III | 98% | 16.3<br><sub>11,9,11,19</sub> | 7.0<br><sub>2,5,7,8</sub> |  | 4.8<br><sub>3,4,2,5</sub> |  | 0.9<br><sub>1,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0</sub> |  | 0.5 | 0.5 | 0.8 | 12.7 |
| Bryce Hopkins | 93% | 16.1<br><sub>2,19,31,14</sub> | 3.8<br><sub>0,2,13,0</sub> |  | 2.2<br><sub>1,2,3,2</sub> |  | 0.8<br><sub>0,1,1,0</sub> |  | 0.3<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.8 |
| Tyus Jones | 88% | 11.7<br><sub>10,10,9,11</sub> | 3.1<br><sub>2,2,0,5</sub> |  | 1.1<br><sub>0,0,0,0</sub> |  | 1.5<br><sub>0,0,2,1</sub> |  | 0.3<br><sub>0,0,0,1</sub> |  | 0.5 | 0.1 | 0.5 | 5.7 |
| Cam Whitmore | 58% | 8.9<br><sub>-,11,4,-</sub> | 4.2<br><sub>-,4,4,-</sub> |  | 1.6<br><sub>-,2,0,-</sub> |  | 0.5<br><sub>-,0,1,-</sub> |  | 0.3<br><sub>-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |
| Zeke Nnaji | 47% | 8.6<br><sub>-,-,4,-</sub> | 2.8<br><sub>-,-,5,-</sub> |  | 1.8<br><sub>-,-,1,-</sub> |  | 0.4<br><sub>-,-,0,-</sub> |  | 0.1<br><sub>-,-,1,-</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Ryan Nembhard | 52% | 6.8<br><sub>2,-,4,-</sub> | 4.1<br><sub>5,-,4,-</sub> |  | 0.9<br><sub>1,-,0,-</sub> |  | 0.7<br><sub>1,-,1,-</sub> |  | 0.2<br><sub>1,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.8 |
| DaRon Holmes II | 52% | 6.6<br><sub>2,-,4,-</sub> | 2.7<br><sub>3,-,0,-</sub> |  | 1.3<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>1,-,1,-</sub> |  | 0.3<br><sub>1,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.4 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 32.4<br><sub>29,36,34</sub> | 22.2<br><sub>23,43,3</sub> | 23.5 · 23.5 | 4.0<br><sub>4,7,2</sub> | 4.5 | 5.7<br><sub>2,7,7</sub> | 5.5 | 1.7<br><sub>0,2,0</sub> | 1.5 | 0.9 | 0.3 | 2.6 | 31.9 |
| Dillon Brooks | 98% | 30.5<br><sub>27,34,33</sub> | 18.1<br><sub>10,15,19</sub> | 16.5 · 16.5 | 4.1<br><sub>4,2,5</sub> | 3.5 | 2.1<br><sub>0,5,5</sub> | 2.5 | 2.1<br><sub>1,1,3</sub> | 1.5 | 0.9 | 0.2 | 1.4 | 24.2 |
| Miles Bridges | 98% | 28.5<br><sub>29,33,32</sub> | 14.3<br><sub>8,16,17</sub> | 15.5 · 15.5 | 5.8<br><sub>4,7,8</sub> | 5.5 | 2.6<br><sub>0,3,4</sub> | 2.5 | 1.5<br><sub>0,2,2</sub> | 1.5 | 0.7 | 0.4 | 1.3 | 22.7 |
| Jalen Green | 96% | 28.1<br><sub>25,26,31</sub> | 15.9<br><sub>10,12,20</sub> | 15.5 · 15.5 | 4.1<br><sub>2,2,4</sub> | 3.5 | 2.9<br><sub>3,1,4</sub> | 3.5 | 1.9<br><sub>2,1,1</sub> | 2.5 | 1.0 | 0.3 | 2.0 | 22.9 |
| Collin Gillespie | 98% | 23.4<br><sub>21,28,23</sub> | 9.2<br><sub>0,11,9</sub> | 8.5 · 8.5 | 3.2<br><sub>1,4,1</sub> | 2.5 | 3.5<br><sub>2,9,2</sub> | 3.5 | 1.6<br><sub>0,2,3</sub> | 2.5 | 1.0 | 0.2 | 1.2 | 15.9 |
| Khaman Maluach | 96% | 18.2<br><sub>17,28,26</sub> | 6.0<br><sub>2,9,12</sub> | 7.5 · 7.5 | 5.7<br><sub>6,9,7</sub> | 7.5 | 0.6<br><sub>1,3,1</sub> |  | 0.3<br><sub>0,1,0</sub> |  | 0.3 | 1.0 | 1.1 | 12.3 |
| Jordan Goodwin | 98% | 17.0<br><sub>22,20,17</sub> | 6.6<br><sub>3,9,12</sub> | 6.5 · – | 3.4<br><sub>4,2,4</sub> | 3.5 | 1.5<br><sub>0,4,2</sub> | 1.5 | 0.9<br><sub>1,1,4</sub> | 1.5 | 1.1 | 0.2 | 0.7 | 11.5 |
| Oso Ighodaro | 96% | 16.8<br><sub>15,-,-</sub> | 5.3<br><sub>8,-,-</sub> |  | 4.3<br><sub>3,-,-</sub> |  | 2.0<br><sub>3,-,-</sub> |  | 0.0<br><sub>0,-,-</sub> |  | 0.6 | 0.6 | 0.8 | 11.7 |
| Luke Kennard | 97% | 16.4<br><sub>-,18,16</sub> | 6.5<br><sub>-,11,9</sub> |  | 2.1<br><sub>-,4,1</sub> |  | 1.5<br><sub>-,1,2</sub> |  | 0.8<br><sub>-,3,3</sub> |  | 0.6 | 0.1 | 0.6 | 10.1 |
| Ryan Dunn | 93% | 11.5<br><sub>14,13,14</sub> | 3.8<br><sub>3,5,6</sub> |  | 2.6<br><sub>2,5,2</sub> |  | 0.8<br><sub>0,0,1</sub> |  | 0.3<br><sub>0,1,1</sub> |  | 0.5 | 0.3 | 0.4 | 7.2 |
| Pat Spencer | 64% | 7.6<br><sub>7,-,-</sub> | 2.8<br><sub>3,-,-</sub> |  | 1.0<br><sub>3,-,-</sub> |  | 1.3<br><sub>1,-,-</sub> |  | 0.2<br><sub>1,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.0 |
| Duop Reath | 88% | 6.8<br><sub>9,3,7</sub> | 2.6<br><sub>5,0,5</sub> |  | 1.3<br><sub>1,0,3</sub> |  | 0.4<br><sub>0,0,0</sub> |  | 0.2<br><sub>1,0,1</sub> |  | 0.2 | 0.2 | 0.2 | 4.3 |
| Rasheer Fleming | 67% | 6.6<br><sub>12,-,3</sub> | 2.5<br><sub>1,-,0</sub> |  | 1.2<br><sub>2,-,1</sub> |  | 0.2<br><sub>0,-,0</sub> |  | 0.2<br><sub>0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.0 |
| Jamaree Bouyea | 67% | 6.3<br><sub>7,-,3</sub> | 2.7<br><sub>3,-,2</sub> |  | 0.9<br><sub>2,-,0</sub> |  | 0.9<br><sub>2,-,1</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Koa Peat | 64% | 5.9<br><sub>7,-,3</sub> | 2.4<br><sub>4,-,0</sub> |  | 1.4<br><sub>1,-,0</sub> |  | 0.4<br><sub>0,-,0</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-30/`._
