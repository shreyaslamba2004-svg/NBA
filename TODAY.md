# NBA model · Fri 30 Oct 2026 (US date)

Updated **Sat 31 Oct, 12:58 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-30/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Khaman Maluach PTS under 7.5 | DEN @ PHX | pointsbetau | 2.05 | 1.92 | 1.62 | 61.7% | 48.9% | 52.1% | +6.8% | +26.6% | 1.6% |
| Aaron Gordon PTS under 14.5 | DEN @ PHX | pointsbetau | 2.00 | 1.90 | 1.62 | 61.9% | 49.6% | 52.7% | +5.3% | +23.8% | 1.3% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| DeMar DeRozan AST over 5.5 (6+) | DEN @ PHX | draftkings | 10.80 | 9.17 | 5.66 | 17.7% | 8.6% | 10.9% | +17.8% | +90.7% | 0.4% |
| Nikola Jokic AST over 15.5 (16+) | DEN @ PHX | draftkings | 13.80 | 12.44 | 8.46 | 11.8% | 6.8% | 8.0% | +10.9% | +63.2% | 0.2% |
| DeMar DeRozan PRA over 29.5 (30+) | DEN @ PHX | draftkings | 13.20 | 11.95 | 8.16 | 12.3% | 7.1% | 8.4% | +10.5% | +61.8% | 0.2% |
| Nikola Jokic AST over 13.5 (14+) | DEN @ PHX | draftkings | 6.54 | 6.08 | 4.35 | 23.0% | 14.3% | 16.5% | +7.6% | +50.2% | 0.4% |
| DeMar DeRozan PRA over 24.5 (25+) | DEN @ PHX | draftkings | 5.36 | 5.04 | 3.69 | 27.1% | 17.4% | 19.9% | +6.5% | +45.5% | 0.4% |
| Nikola Jokic AST over 17.5 (18+) | DEN @ PHX | draftkings | 27.00 | 25.45 | 18.74 | 5.3% | 3.5% | 3.9% | +6.1% | +44.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| DeMar DeRozan AST over 6.5 (7+) | DEN @ PHX | draftkings | 19.60 | 16.95 | 10.75 | 9.3% | 4.8% | 5.9% | +15.7% | +82.4% | 0.2% |
| DeMar DeRozan AST over 4.5 (5+) | DEN @ PHX | draftkings | 5.73 | 5.08 | 3.35 | 29.9% | 16.3% | 19.7% | +12.9% | +71.1% | 0.7% |
| Nikola Jokic AST over 16.5 (17+) | DEN @ PHX | draftkings | 19.60 | 17.83 | 12.32 | 8.1% | 4.8% | 5.6% | +9.9% | +59.2% | 0.1% |
| Nikola Jokic AST over 14.5 (15+) | DEN @ PHX | draftkings | 9.40 | 8.60 | 5.99 | 16.7% | 9.9% | 11.6% | +9.3% | +57.0% | 0.3% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walker Kessler PTS under 13.5 | LAL @ GSW | sportsbet | 2.02 | 1.87 | 1.39 | 72.1% | 47.2% | 53.4% | +7.9% | +45.6% | 1.9% |
| Walker Kessler PTS under 14.5 | LAL @ GSW | ladbrokes_au | 1.83 | 1.71 | 1.29 | 77.3% | 52.1% | 58.4% | +7.1% | +41.7% | 2.0% |
| DeMar DeRozan AST over 3.5 (4+) | DEN @ PHX | draftkings | 3.10 | 2.91 | 2.14 | 46.8% | 30.1% | 34.3% | +6.4% | +45.1% | 0.8% |
| Cameron Johnson PTS under 10.5 | DEN @ PHX | unibet | 1.97 | 1.87 | 1.49 | 67.3% | 48.9% | 53.5% | +5.5% | +32.7% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play).

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ GSW | Sat 31 Oct 13:00 | 114.4–115.0 | LAL 49% | 2.04 / 1.96 | GSW +0.5 | 229.5 | GSW +2.5 covers 57%; o234.5 39% |
| DEN @ PHX | Sat 31 Oct 13:00 | 115.6–113.3 | DEN 56% | 1.77 / 2.30 | PHX +2.5 | 228.5 | PHX +3.5 covers 53%; o231.5 44% |

### LAL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Ziaire Williams (LAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski PTS under 15.5 | LAL @ GSW | tab | 1.87 | 1.81 | 1.53 | 65.6% | 51.8% | 55.2% | +3.2% | +22.6% | 0.9% |
| Austin Reaves PTS under 22.5 | LAL @ GSW | sportsbet | 2.00 | 1.95 | 1.64 | 61.1% | 48.1% | 51.4% | +2.8% | +22.3% | 0.7% |
| De'Anthony Melton PTS under 8.5 | LAL @ GSW | pointsbetau | 2.05 | 2.00 | 1.71 | 58.5% | 47.2% | 50.0% | +2.6% | +20.0% | 0.6% |
| Austin Reaves PTS under 23.5 | LAL @ GSW | pointsbetau | 1.87 | 1.83 | 1.53 | 65.3% | 51.0% | 54.6% | +2.0% | +22.1% | 0.6% |
| Stephen Curry PR under 27.5 | LAL @ GSW | draftkings | 1.93 | 1.93 | 1.60 | 62.3% | 48.3% | 51.8% | +0.2% | +20.6% | 0.1% |
| Brandin Podziemski PRA under 24.5 | LAL @ GSW | draftkings | 1.87 | 1.87 | 1.55 | 64.5% | 50.0% | 53.6% | +0.2% | +20.5% | 0.1% |
| Gui Santos PTS under 9.5 | LAL @ GSW | tab | 1.85 | 1.84 | 1.76 | 56.8% | 53.4% | 54.2% | +0.2% | +5.0% | 0.1% |
| Austin Reaves PRA under 33.5 | LAL @ GSW | draftkings | 1.87 | 1.87 | 1.55 | 64.4% | 50.0% | 53.6% | +0.2% | +20.4% | 0.1% |
| Austin Reaves PR under 27.5 | LAL @ GSW | draftkings | 1.88 | 1.87 | 1.56 | 64.1% | 49.8% | 53.4% | +0.2% | +20.3% | 0.1% |
| Austin Reaves PA under 29.5 | LAL @ GSW | draftkings | 1.83 | 1.83 | 1.53 | 65.4% | 51.0% | 54.6% | +0.1% | +19.8% | 0.0% |
| Brandin Podziemski PR under 20.5 | LAL @ GSW | draftkings | 1.84 | 1.84 | 1.54 | 65.1% | 50.8% | 54.4% | +0.0% | +19.8% | 0.0% |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 100% | 36.4<br><sub>30,37,38,37,-</sub> | 33.8<br><sub>28,23,52,41,-</sub> | 34.5 · 34.5 | 7.1<br><sub>8,6,8,5,-</sub> | 6.5 | 8.0<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.0 |
| Austin Reaves | 100% | 35.3<br><sub>32,38,36,39,31</sub> | 21.1<br><sub>23,28,29,26,16</sub> | 23.5 · 22.5 | 4.1<br><sub>4,2,1,4,6</sub> | 3.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.2<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.4 | 30.8 |
| Walker Kessler | 100% | 29.5<br><sub>30,35,28,33,26</sub> | 11.0<br><sub>26,22,2,13,11</sub> | 13.5 · 13.5 | 9.6<br><sub>9,8,7,8,9</sub> | 9.5 | 1.6<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.2 |
| Jake LaRavia | 100% | 26.8<br><sub>18,-,15,19,35</sub> | 6.5<br><sub>10,-,0,5,2</sub> | 6.5 · – | 4.3<br><sub>2,-,4,1,10</sub> |  | 1.6<br><sub>2,-,1,1,0</sub> |  | 0.6<br><sub>2,-,0,1,0</sub> | 0.5 | 1.5 | 0.7 | 1.4 | 12.4 |
| Quentin Grimes | 98% | 26.5<br><sub>27,31,20,19,38</sub> | 9.6<br><sub>10,13,3,2,23</sub> | 8.5 · 9.5 | 3.2<br><sub>2,8,1,4,3</sub> | 2.5 | 2.4<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.2 |
| Matisse Thybulle | 100% | 25.5<br><sub>23,24,26,22,28</sub> | 7.1<br><sub>3,13,11,5,15</sub> | 6.5 · 6.5 | 2.5<br><sub>3,1,1,2,1</sub> | 2.5 | 1.4<br><sub>1,2,1,1,0</sub> |  | 1.2<br><sub>1,3,3,1,4</sub> | 1.5 | 2.2 | 0.7 | 1.1 | 11.0 |
| Sandro Mamukelashvili | 98% | 24.3<br><sub>22,24,21,24,30</sub> | 9.3<br><sub>5,7,9,17,13</sub> | 9.5 · 9.5 | 5.3<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.1<br><sub>0,1,1,3,0</sub> | 1.5 | 0.9 | 0.5 | 1.0 | 16.4 |
| Collin Sexton | 98% | 19.0<br><sub>-,16,20,14,21</sub> | 11.2<br><sub>-,5,13,9,21</sub> | 11.5 · 11.5 | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> | 2.5 | 1.3<br><sub>-,1,1,0,4</sub> | 1.5 | 1.0 | 0.1 | 1.7 | 15.3 |
| Jarred Vanderbilt | 48% | 16.4<br><sub>-,-,-,-,21</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 4.2<br><sub>-,-,-,-,7</sub> |  | 1.2<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 9.6 |
| Lawson Lovering | 23% | 13.7 | 4.1 |  | 3.4 |  | 0.9 |  | 0.1 |  | 0.7 | 0.3 | 0.6 | 8.4 |
| Jaden Hardy | 52% | 8.8<br><sub>7,-,-,-,9</sub> | 4.2<br><sub>3,-,-,-,2</sub> |  | 0.8<br><sub>2,-,-,-,0</sub> |  | 0.6<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.7 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| AK Okereke | 30% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Kevon Looney | 64% | 8.1<br><sub>15,5,5,5,-</sub> | 2.0<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>5,1,2,0,-</sub> |  | 0.6<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.2 |
| Bronny James | 26% | 6.2<br><sub>7,-,-,-,-</sub> | 2.1<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 2.6 |
| Chris Manon | 52% | 5.8<br><sub>6,-,-,-,-</sub> | 1.7<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 3.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 100% | 33.5<br><sub>29,37,36,31,35</sub> | 20.8<br><sub>12,18,26,31,26</sub> | 19.5 · 19.5 | 8.1<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.8<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 2.9 | 32.8 |
| Brandin Podziemski | 100% | 30.2<br><sub>-,33,-,33,32</sub> | 13.8<br><sub>-,18,-,18,8</sub> | 15.5 · 14.5 | 4.8<br><sub>-,2,-,7,5</sub> | 5.5 | 3.8<br><sub>-,3,-,5,6</sub> | 3.5 | 1.8<br><sub>-,2,-,3,0</sub> | 2.5 | 1.2 | 0.2 | 1.8 | 22.4 |
| Stephen Curry | 100% | 29.1<br><sub>21,30,-,27,32</sub> | 22.2<br><sub>23,24,-,24,44</sub> | 24.5 · 24.5 | 3.4<br><sub>2,2,-,3,8</sub> | 3.5 | 4.3<br><sub>1,4,-,3,6</sub> | 3.5 | 3.5<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 2.8 | 29.9 |
| Draymond Green | 100% | 26.2<br><sub>21,31,-,27,32</sub> | 7.3<br><sub>2,5,-,3,3</sub> | 5.5 · 5.5 | 4.9<br><sub>4,5,-,4,9</sub> | 5.5 | 5.4<br><sub>8,6,-,7,6</sub> | 5.5 | 0.9<br><sub>0,1,-,1,0</sub> | 0.5 | 1.1 | 0.6 | 2.4 | 17.7 |
| Gui Santos | 100% | 24.1<br><sub>25,20,23,28,-</sub> | 9.4<br><sub>12,5,7,13,-</sub> | 8.5 · 9.5 | 4.3<br><sub>5,4,4,3,-</sub> | 4.5 | 2.3<br><sub>0,2,3,1,-</sub> |  | 1.1<br><sub>1,1,1,1,-</sub> | 0.5 | 1.1 | 0.3 | 1.6 | 16.0 |
| De'Anthony Melton | 98% | 19.0<br><sub>21,20,27,19,20</sub> | 8.2<br><sub>0,10,25,3,8</sub> | 8.5 · 8.5 | 2.8<br><sub>2,1,5,4,6</sub> | 2.5 | 2.0<br><sub>2,0,5,3,0</sub> | 2.5 | 1.1<br><sub>0,2,4,1,2</sub> | 1.5 | 1.2 | 0.3 | 1.3 | 13.0 |
| Al Horford | 98% | 17.2<br><sub>17,19,-,19,18</sub> | 5.3<br><sub>0,3,-,11,4</sub> | 5.5 · 5.5 | 3.8<br><sub>4,5,-,3,5</sub> | 3.5 | 1.4<br><sub>2,0,-,0,2</sub> |  | 0.8<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.6 | 0.6 | 10.5 |
| Georges Niang | 93% | 17.0<br><sub>20,13,23,18,23</sub> | 6.8<br><sub>7,4,4,9,7</sub> | 6.5 · 6.5 | 2.3<br><sub>2,3,4,2,3</sub> |  | 0.9<br><sub>2,0,2,0,2</sub> |  | 1.0<br><sub>0,0,0,3,1</sub> | 1.5 | 0.5 | 0.1 | 1.0 | 10.1 |
| Brandon Williams | 98% | 15.0<br><sub>18,9,24,15,14</sub> | 8.7<br><sub>14,4,20,6,11</sub> |  | 2.1<br><sub>4,2,3,3,3</sub> |  | 2.7<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.2 | 1.4 | 13.5 |
| Will Richard | 98% | 14.4<br><sub>20,3,31,3,23</sub> | 4.1<br><sub>8,0,11,0,6</sub> |  | 1.7<br><sub>5,0,0,0,3</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4<br><sub>0,0,3,0,0</sub> |  | 1.0 | 0.1 | 0.5 | 6.5 |
| Gary Payton II | 98% | 12.5<br><sub>18,11,17,12,10</sub> | 6.1<br><sub>10,7,2,7,2</sub> |  | 2.4<br><sub>1,2,1,2,2</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.6 | 9.5 |
| Graham Ike | 67% | 8.3<br><sub>12,12,26,3,-</sub> | 4.0<br><sub>8,10,12,3,-</sub> |  | 2.0<br><sub>2,2,10,0,-</sub> |  | 0.7<br><sub>1,1,2,1,-</sub> |  | 0.2<br><sub>1,2,0,1,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.7 |
| Charles Bassey | 91% | 7.6<br><sub>-,-,13,2,2</sub> | 3.3<br><sub>-,-,10,0,0</sub> |  | 2.8<br><sub>-,-,7,1,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.4 | 6.5 |
| LJ Cryer | 63% | 6.3<br><sub>9,-,14,3,-</sub> | 2.9<br><sub>9,-,3,6,-</sub> |  | 0.6<br><sub>1,-,1,0,-</sub> |  | 0.5<br><sub>3,-,1,2,-</sub> |  | 0.3<br><sub>2,-,1,2,-</sub> |  | 0.1 | 0.0 | 0.3 | 4.0 |
| Malevy Leons | 58% | 5.9<br><sub>9,-,4,3,-</sub> | 1.9<br><sub>0,-,2,0,-</sub> |  | 1.1<br><sub>1,-,0,1,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.4 |

</details>


### DEN @ PHX
Out: Drew Timme (PHX), Mark Williams (PHX), Alpha Diallo (DEN), Julian Strawther (DEN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Khaman Maluach PTS under 7.5 | DEN @ PHX | pointsbetau | 2.05 | 1.92 | 1.62 | 61.7% | 48.9% | 52.1% | +6.8% | +26.6% | 1.6% |
| Aaron Gordon PTS under 14.5 | DEN @ PHX | pointsbetau | 2.00 | 1.90 | 1.62 | 61.9% | 49.6% | 52.7% | +5.3% | +23.8% | 1.3% |
| Miles Bridges PTS under 15.5 | DEN @ PHX | tab | 1.95 | 1.86 | 1.59 | 62.7% | 50.7% | 53.7% | +4.9% | +22.5% | 1.3% |
| Devin Booker PTS under 23.5 | DEN @ PHX | pointsbetau | 1.90 | 1.88 | 1.60 | 62.4% | 50.0% | 53.1% | +1.0% | +18.7% | 0.3% |
| Miles Bridges PR under 21.5 | DEN @ PHX | draftkings | 1.97 | 1.96 | 1.61 | 62.1% | 47.4% | 51.1% | +0.7% | +22.3% | 0.2% |
| Miles Bridges PRA under 24.5 | DEN @ PHX | draftkings | 1.93 | 1.92 | 1.59 | 62.9% | 48.3% | 52.0% | +0.5% | +21.8% | 0.1% |
| Miles Bridges 3PM under 1.5 | DEN @ PHX | draftkings | 2.13 | 2.12 | 1.76 | 56.7% | 43.9% | 47.1% | +0.3% | +20.9% | 0.1% |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 100% | 37.7<br><sub>37,43,36,38</sub> | 23.1<br><sub>6,42,19,23</sub> | 22.5 · 22.5 | 4.5<br><sub>10,3,6,1</sub> | 4.5 | 6.5<br><sub>3,6,8,6</sub> | 6.5 | 3.3<br><sub>0,8,3,5</sub> | 2.5 | 1.1 | 0.5 | 2.7 | 34.0 |
| Nikola Jokic | 100% | 37.3<br><sub>35,44,35,34</sub> | 25.4<br><sub>13,35,19,21</sub> | 25.5 · 25.5 | 12.7<br><sub>7,15,7,13</sub> | 11.5 | 10.7<br><sub>5,10,11,10</sub> | 9.5 | 1.7<br><sub>1,3,1,0</sub> | 1.5 | 1.6 | 0.9 | 4.0 | 48.9 |
| Christian Braun | 100% | 34.1<br><sub>33,40,34,36</sub> | 11.6<br><sub>7,15,9,15</sub> | 11.5 · 11.5 | 4.7<br><sub>6,8,4,0</sub> | 4.5 | 2.5<br><sub>1,2,2,4</sub> |  | 1.2<br><sub>1,0,1,3</sub> | 1.5 | 1.1 | 0.4 | 1.1 | 18.8 |
| Aaron Gordon | 100% | 30.5<br><sub>29,37,25,31</sub> | 13.5<br><sub>20,7,7,15</sub> | 14.5 · 14.5 | 6.0<br><sub>6,5,4,11</sub> | 5.5 | 2.7<br><sub>1,4,2,3</sub> | 2.5 | 1.5<br><sub>3,1,0,2</sub> | 1.5 | 0.7 | 0.3 | 1.4 | 22.1 |
| DeMar DeRozan | 98% | 27.4<br><sub>28,24,29,26</sub> | 14.2<br><sub>13,12,21,6</sub> | 12.5 · 12.5 | 2.6<br><sub>2,3,4,2</sub> | 2.5 | 3.6<br><sub>0,3,2,5</sub> | 2.5 | 0.6<br><sub>0,0,2,0</sub> | 0.5 | 0.9 | 0.3 | 1.7 | 20.4 |
| Trevon Brazile | 93% | 23.5<br><sub>18,28,17,32</sub> | 7.8<br><sub>4,17,6,11</sub> | 6.5 · 7.5 | 5.9<br><sub>12,9,1,8</sub> | 4.5 | 0.9<br><sub>0,0,0,0</sub> |  | 1.0<br><sub>0,3,1,1</sub> |  | 0.7 | 0.5 | 1.2 | 14.6 |
| Cameron Johnson | 100% | 22.6<br><sub>11,-,-,-</sub> | 9.0<br><sub>5,-,-,-</sub> | 10.5 · 10.5 | 3.1<br><sub>2,-,-,-</sub> | 3.5 | 1.8<br><sub>1,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-</sub> | 1.5 | 0.7 | 0.3 | 0.9 | 13.9 |
| Marvin Bagley III | 98% | 14.6<br><sub>11,9,11,19</sub> | 6.3<br><sub>2,5,7,8</sub> |  | 4.2<br><sub>3,4,2,5</sub> |  | 0.8<br><sub>1,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 11.3 |
| Bryce Hopkins | 93% | 14.6<br><sub>2,19,31,14</sub> | 3.6<br><sub>0,2,13,0</sub> |  | 2.1<br><sub>1,2,3,2</sub> |  | 0.7<br><sub>0,1,1,0</sub> |  | 0.2<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.4 |
| Tyus Jones | 88% | 10.8<br><sub>10,10,9,11</sub> | 2.9<br><sub>2,2,0,5</sub> |  | 1.0<br><sub>0,0,0,0</sub> |  | 1.4<br><sub>0,0,2,1</sub> |  | 0.3<br><sub>0,0,0,1</sub> |  | 0.5 | 0.0 | 0.4 | 5.3 |
| Cam Whitmore | 58% | 7.7<br><sub>-,11,4,-</sub> | 3.7<br><sub>-,4,4,-</sub> |  | 1.4<br><sub>-,2,0,-</sub> |  | 0.4<br><sub>-,0,1,-</sub> |  | 0.3<br><sub>-,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |
| Zeke Nnaji | 47% | 7.2<br><sub>-,-,4,-</sub> | 2.4<br><sub>-,-,5,-</sub> |  | 1.6<br><sub>-,-,1,-</sub> |  | 0.4<br><sub>-,-,0,-</sub> |  | 0.1<br><sub>-,-,1,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |
| Ryan Nembhard | 52% | 6.2<br><sub>2,-,4,-</sub> | 4.2<br><sub>5,-,4,-</sub> |  | 0.8<br><sub>1,-,0,-</sub> |  | 0.8<br><sub>1,-,1,-</sub> |  | 0.2<br><sub>1,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.8 |
| DaRon Holmes II | 52% | 5.9<br><sub>2,-,4,-</sub> | 2.3<br><sub>3,-,0,-</sub> |  | 1.2<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>1,-,1,-</sub> |  | 0.2<br><sub>1,-,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 3.9 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 100% | 32.3<br><sub>29,36,34</sub> | 21.9<br><sub>23,43,3</sub> | 23.5 · 23.5 | 4.0<br><sub>4,7,2</sub> | 4.5 | 5.7<br><sub>2,7,7</sub> | 5.5 | 1.7<br><sub>0,2,0</sub> | 1.5 | 0.9 | 0.3 | 2.7 | 31.6 |
| Dillon Brooks | 100% | 30.3<br><sub>27,34,33</sub> | 17.7<br><sub>10,15,19</sub> | 16.5 · 16.5 | 4.1<br><sub>4,2,5</sub> | 3.5 | 2.0<br><sub>0,5,5</sub> | 2.5 | 2.0<br><sub>1,1,3</sub> | 1.5 | 0.9 | 0.2 | 1.4 | 23.9 |
| Miles Bridges | 100% | 28.6<br><sub>29,33,32</sub> | 14.3<br><sub>8,16,17</sub> | 15.5 · 15.5 | 5.8<br><sub>4,7,8</sub> | 5.5 | 2.6<br><sub>0,3,4</sub> | 2.5 | 1.5<br><sub>0,2,2</sub> | 1.5 | 0.8 | 0.4 | 1.3 | 22.6 |
| Jalen Green | 100% | 27.9<br><sub>25,26,31</sub> | 15.5<br><sub>10,12,20</sub> | 15.5 · 15.5 | 4.1<br><sub>2,2,4</sub> | 3.5 | 2.9<br><sub>3,1,4</sub> | 3.5 | 1.8<br><sub>2,1,1</sub> | 2.5 | 1.0 | 0.3 | 1.9 | 22.5 |
| Collin Gillespie | 98% | 23.0<br><sub>21,28,23</sub> | 9.1<br><sub>0,11,9</sub> | 8.5 · 8.5 | 3.1<br><sub>1,4,1</sub> | 2.5 | 3.5<br><sub>2,9,2</sub> | 3.5 | 1.5<br><sub>0,2,3</sub> | 2.5 | 1.0 | 0.2 | 1.2 | 15.6 |
| Khaman Maluach | 100% | 21.1<br><sub>17,28,26</sub> | 6.9<br><sub>2,9,12</sub> | 7.5 · 7.5 | 6.5<br><sub>6,9,7</sub> | 7.5 | 0.7<br><sub>1,3,1</sub> |  | 0.3<br><sub>0,1,0</sub> |  | 0.4 | 1.2 | 1.2 | 14.1 |
| Jordan Goodwin | 98% | 16.8<br><sub>22,20,17</sub> | 6.4<br><sub>3,9,12</sub> | 6.5 · – | 3.4<br><sub>4,2,4</sub> | 3.5 | 1.5<br><sub>0,4,2</sub> | 1.5 | 0.9<br><sub>1,1,4</sub> | 1.5 | 1.1 | 0.2 | 0.7 | 11.2 |
| Oso Ighodaro | 96% | 16.6<br><sub>15,-,-</sub> | 5.2<br><sub>8,-,-</sub> |  | 4.2<br><sub>3,-,-</sub> |  | 2.1<br><sub>3,-,-</sub> |  | 0.0<br><sub>0,-,-</sub> |  | 0.6 | 0.6 | 0.8 | 11.5 |
| Luke Kennard | 97% | 16.4<br><sub>-,18,16</sub> | 6.3<br><sub>-,11,9</sub> |  | 2.1<br><sub>-,4,1</sub> |  | 1.4<br><sub>-,1,2</sub> |  | 0.8<br><sub>-,3,3</sub> |  | 0.6 | 0.1 | 0.6 | 9.9 |
| Ryan Dunn | 93% | 11.2<br><sub>14,13,14</sub> | 3.6<br><sub>3,5,6</sub> |  | 2.5<br><sub>2,5,2</sub> |  | 0.8<br><sub>0,0,1</sub> |  | 0.3<br><sub>0,1,1</sub> |  | 0.4 | 0.3 | 0.4 | 6.9 |
| Pat Spencer | 64% | 7.6<br><sub>7,-,-</sub> | 2.7<br><sub>3,-,-</sub> |  | 1.0<br><sub>3,-,-</sub> |  | 1.3<br><sub>1,-,-</sub> |  | 0.2<br><sub>1,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.0 |
| Duop Reath | 88% | 6.8<br><sub>9,3,7</sub> | 2.5<br><sub>5,0,5</sub> |  | 1.4<br><sub>1,0,3</sub> |  | 0.4<br><sub>0,0,0</sub> |  | 0.2<br><sub>1,0,1</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |
| Rasheer Fleming | 67% | 6.6<br><sub>12,-,3</sub> | 2.4<br><sub>1,-,0</sub> |  | 1.2<br><sub>2,-,1</sub> |  | 0.3<br><sub>0,-,0</sub> |  | 0.2<br><sub>0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 3.9 |
| Jamaree Bouyea | 67% | 6.3<br><sub>7,-,3</sub> | 2.8<br><sub>3,-,2</sub> |  | 0.9<br><sub>2,-,0</sub> |  | 1.0<br><sub>2,-,1</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |
| Koa Peat | 64% | 5.9<br><sub>7,-,3</sub> | 2.3<br><sub>4,-,0</sub> |  | 1.4<br><sub>1,-,0</sub> |  | 0.4<br><sub>0,-,0</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.1 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-30/`._
