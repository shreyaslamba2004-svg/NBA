# NBA model · Fri 30 Oct 2026 (US date)

Updated **Sat 31 Oct, 11:14 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-30/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sandro Mamukelashvili REB over 7.5 (8+) | LAL @ GSW | draftkings | 7.10 | 6.67 | 4.88 | 20.5% | 13.2% | 15.0% | +6.5% | +45.6% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sandro Mamukelashvili REB over 8.5 (9+) | LAL @ GSW | draftkings | 11.20 | 10.56 | 7.78 | 12.9% | 8.3% | 9.5% | +6.1% | +44.0% | 0.1% |
| Sandro Mamukelashvili REB over 6.5 (7+) | LAL @ GSW | draftkings | 4.57 | 4.32 | 3.20 | 31.3% | 20.4% | 23.2% | +5.8% | +42.9% | 0.4% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Khaman Maluach PR under 16.5 | DEN @ PHX | draftkings | 1.88 | Oso Ighodaro | 77.0% | 81.1% | +7.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play).

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ GSW | Sat 31 Oct 13:00 | 114.7–114.0 | LAL 52% | 1.91 / 2.10 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| DEN @ PHX | Sat 31 Oct 13:00 | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +4.5 covers 56%; o231.5 43% |

### LAL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Ziaire Williams (LAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sandro Mamukelashvili REB over 4.5 (5+) | LAL @ GSW | draftkings | 2.11 | 2.08 | 1.69 | 59.2% | 44.4% | 48.1% | +1.5% | +25.0% | 0.3% |
| Austin Reaves PRA under 33.5 | LAL @ GSW | draftkings | 1.90 | 1.89 | 1.56 | 64.0% | 49.2% | 52.9% | +0.5% | +21.7% | 0.1% |
| Austin Reaves PR under 27.5 | LAL @ GSW | draftkings | 1.91 | 1.90 | 1.58 | 63.4% | 48.9% | 52.6% | +0.4% | +21.1% | 0.1% |
| Austin Reaves PA under 29.5 | LAL @ GSW | draftkings | 1.84 | 1.84 | 1.53 | 65.5% | 50.8% | 54.4% | +0.2% | +20.4% | 0.1% |
| Austin Reaves PTS under 23.5 | LAL @ GSW | draftkings | 1.85 | 1.85 | 1.54 | 64.9% | 50.4% | 54.0% | +0.2% | +20.4% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.7–114.0 | LAL 52% | 1.91 / 2.10 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| Expected (weighted by chance each plays) | 114.5–114.5 | LAL 50% | 1.99 / 2.01 | GSW +0.5 | 228.5 | GSW +3.5 covers 59%; o234.5 38% |
| if Gui Santos plays | 114.4–115.0 | LAL 49% | 2.04 / 1.96 | GSW +0.5 | 229.5 | GSW +3.5 covers 60%; o234.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 23.4 | 9.2 | 4.2 | 2.2 | 1.1 | 1.0 | 0.3 | 1.5 | 15.6 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.5<br><sub>30,37,38,37,-</sub> | 34.4<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 6.5 | 8.0<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.5 |
| Austin Reaves | 98% | 35.5<br><sub>32,38,36,39,31</sub> | 21.4<br><sub>23,28,29,26,16</sub> | 23.5 · – | 4.1<br><sub>4,2,1,4,6</sub> | 4.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 31.1 |
| Walker Kessler | 98% | 29.8<br><sub>30,35,28,33,26</sub> | 11.2<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.8<br><sub>9,8,7,8,9</sub> | 9.5 | 1.5<br><sub>1,3,0,0,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.6 |
| Quentin Grimes | 98% | 27.2<br><sub>27,31,20,19,38</sub> | 10.0<br><sub>10,13,3,2,23</sub> | 9.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 3.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.7 |
| Sandro Mamukelashvili | 98% | 24.9<br><sub>22,24,21,24,30</sub> | 9.8<br><sub>5,7,9,17,13</sub> | 9.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> | 1.5 | 1.0 | 0.5 | 1.0 | 17.0 |
| Jake LaRavia | 91% | 23.9<br><sub>18,-,15,19,35</sub> | 5.8<br><sub>10,-,0,5,2</sub> |  | 3.8<br><sub>2,-,4,1,10</sub> |  | 1.4<br><sub>2,-,1,1,0</sub> |  | 0.5<br><sub>2,-,0,1,0</sub> |  | 1.4 | 0.6 | 1.2 | 11.0 |
| Matisse Thybulle | 96% | 23.2<br><sub>23,24,26,22,28</sub> | 6.4<br><sub>3,13,11,5,15</sub> | 6.5 · – | 2.2<br><sub>3,1,1,2,1</sub> | 2.5 | 1.2<br><sub>1,2,1,1,0</sub> |  | 1.1<br><sub>1,3,3,1,4</sub> | 1.5 | 2.0 | 0.7 | 1.0 | 9.9 |
| Collin Sexton | 98% | 19.2<br><sub>-,16,20,14,21</sub> | 11.5<br><sub>-,5,13,9,21</sub> | 11.5 · – | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> | 2.5 | 1.3<br><sub>-,1,1,0,4</sub> | 1.5 | 1.1 | 0.1 | 1.8 | 15.6 |
| Jarred Vanderbilt | 48% | 16.7<br><sub>-,-,-,-,21</sub> | 4.3<br><sub>-,-,-,-,0</sub> |  | 4.3<br><sub>-,-,-,-,7</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 9.9 |
| Lawson Lovering | 23% | 13.9 | 4.2 |  | 3.4 |  | 1.0 |  | 0.1 |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Jaden Hardy | 52% | 9.3<br><sub>7,-,-,-,9</sub> | 4.4<br><sub>3,-,-,-,2</sub> |  | 0.8<br><sub>2,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 5.9 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.1 |
| AK Okereke | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Kevon Looney | 64% | 8.1<br><sub>15,5,5,5,-</sub> | 2.0<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.3 |
| Bronny James | 26% | 6.2<br><sub>7,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 2.7 |
| Chris Manon | 52% | 5.8<br><sub>6,-,-,-,-</sub> | 1.6<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 96% | 34.6<br><sub>29,37,36,31,35</sub> | 20.9<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.3<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.1 | 33.1 |
| Brandin Podziemski | 80% | 31.7<br><sub>-,33,-,33,32</sub> | 15.0<br><sub>-,18,-,18,8</sub> | 14.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 4.5 | 4.1<br><sub>-,3,-,5,6</sub> | 3.5 | 1.9<br><sub>-,2,-,3,0</sub> | 1.5 | 1.2 | 0.2 | 1.9 | 23.9 |
| Stephen Curry | 98% | 31.1<br><sub>21,30,-,27,32</sub> | 24.3<br><sub>23,24,-,24,44</sub> | 24.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.7<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 3.0 | 32.5 |
| Draymond Green | 83% | 28.7<br><sub>21,31,-,27,32</sub> | 8.1<br><sub>2,5,-,3,3</sub> | 5.5 · – | 5.2<br><sub>4,5,-,4,9</sub> | 5.5 | 6.0<br><sub>8,6,-,7,6</sub> | 5.5 | 1.0<br><sub>0,1,-,1,0</sub> | 0.5 | 1.2 | 0.6 | 2.5 | 19.3 |
| De'Anthony Melton | 98% | 21.6<br><sub>21,20,27,19,20</sub> | 9.3<br><sub>0,10,25,3,8</sub> | 9.5 · – | 3.0<br><sub>2,1,5,4,6</sub> | 2.5 | 2.3<br><sub>2,0,5,3,0</sub> | 1.5 | 1.3<br><sub>0,2,4,1,2</sub> | 1.5 | 1.4 | 0.3 | 1.5 | 14.6 |
| Georges Niang | 93% | 20.0<br><sub>20,13,23,18,23</sub> | 7.9<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.5<br><sub>2,3,4,2,3</sub> |  | 1.1<br><sub>2,0,2,0,2</sub> |  | 1.3<br><sub>0,0,0,3,1</sub> | 1.5 | 0.6 | 0.1 | 1.0 | 11.6 |
| Al Horford | 98% | 19.4<br><sub>17,19,-,19,18</sub> | 6.0<br><sub>0,3,-,11,4</sub> | 5.5 · – | 4.2<br><sub>4,5,-,3,5</sub> | 3.5 | 1.6<br><sub>2,0,-,0,2</sub> |  | 0.9<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.7 | 0.7 | 11.7 |
| Will Richard | 98% | 16.8<br><sub>20,3,31,3,23</sub> | 4.7<br><sub>8,0,11,0,6</sub> |  | 1.9<br><sub>5,0,0,0,3</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>0,0,3,0,0</sub> |  | 1.1 | 0.1 | 0.6 | 7.5 |
| Brandon Williams | 98% | 16.5<br><sub>18,9,24,15,14</sub> | 9.4<br><sub>14,4,20,6,11</sub> |  | 2.2<br><sub>4,2,3,3,3</sub> |  | 2.9<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.2 | 1.5 | 14.5 |
| Gary Payton II | 98% | 14.2<br><sub>18,11,17,12,10</sub> | 6.5<br><sub>10,7,2,7,2</sub> |  | 2.7<br><sub>1,2,1,2,2</sub> |  | 1.1<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 10.2 |
| Graham Ike | 67% | 12.5<br><sub>12,12,26,3,-</sub> | 6.0<br><sub>8,10,12,3,-</sub> |  | 2.8<br><sub>2,2,10,0,-</sub> |  | 1.0<br><sub>1,1,2,1,-</sub> |  | 0.3<br><sub>1,2,0,1,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.8 |
| Charles Bassey | 91% | 9.3<br><sub>-,-,13,2,2</sub> | 3.9<br><sub>-,-,10,0,0</sub> |  | 3.4<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 7.7 |
| LJ Cryer | 63% | 8.2<br><sub>9,-,14,3,-</sub> | 3.5<br><sub>9,-,3,6,-</sub> |  | 0.8<br><sub>1,-,1,0,-</sub> |  | 0.7<br><sub>3,-,1,2,-</sub> |  | 0.5<br><sub>2,-,1,2,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Malevy Leons | 58% | 8.0<br><sub>9,-,4,3,-</sub> | 2.4<br><sub>0,-,2,0,-</sub> |  | 1.4<br><sub>1,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 4.4 |

</details>

<details><summary>if Gui Santos plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | 96% | 34.0<br><sub>29,37,36,31,35</sub> | 21.1<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.1<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.0 | 33.1 |
| Brandin Podziemski (GSW) | 80% | 30.3<br><sub>-,33,-,33,32</sub> | 14.3<br><sub>-,18,-,18,8</sub> | 14.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 4.5 | 3.8<br><sub>-,3,-,5,6</sub> | 3.5 | 1.8<br><sub>-,2,-,3,0</sub> | 1.5 | 1.2 | 0.2 | 1.8 | 22.9 |
| Stephen Curry (GSW) | 98% | 30.0<br><sub>21,30,-,27,32</sub> | 23.6<br><sub>23,24,-,24,44</sub> | 24.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.4<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 2.9 | 31.5 |
| Draymond Green (GSW) | 83% | 26.4<br><sub>21,31,-,27,32</sub> | 7.3<br><sub>2,5,-,3,3</sub> | 5.5 · – | 4.9<br><sub>4,5,-,4,9</sub> | 5.5 | 5.5<br><sub>8,6,-,7,6</sub> | 5.5 | 0.9<br><sub>0,1,-,1,0</sub> | 0.5 | 1.1 | 0.6 | 2.4 | 17.7 |
| Gui Santos (GSW) | 100% | 23.4<br><sub>25,20,23,28,-</sub> | 9.2<br><sub>12,5,7,13,-</sub> |  | 4.2<br><sub>5,4,4,3,-</sub> |  | 2.2<br><sub>0,2,3,1,-</sub> |  | 1.1<br><sub>1,1,1,1,-</sub> |  | 1.0 | 0.3 | 1.5 | 15.6 |
| De'Anthony Melton (GSW) | 98% | 19.6<br><sub>21,20,27,19,20</sub> | 8.4<br><sub>0,10,25,3,8</sub> | 9.5 · – | 2.8<br><sub>2,1,5,4,6</sub> | 2.5 | 2.0<br><sub>2,0,5,3,0</sub> | 1.5 | 1.1<br><sub>0,2,4,1,2</sub> | 1.5 | 1.3 | 0.3 | 1.3 | 13.3 |
| Al Horford (GSW) | 98% | 17.5<br><sub>17,19,-,19,18</sub> | 5.3<br><sub>0,3,-,11,4</sub> | 5.5 · – | 3.8<br><sub>4,5,-,3,5</sub> | 3.5 | 1.4<br><sub>2,0,-,0,2</sub> |  | 0.8<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.6 | 0.6 | 10.5 |
| Georges Niang (GSW) | 93% | 17.2<br><sub>20,13,23,18,23</sub> | 7.0<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.3<br><sub>2,3,4,2,3</sub> |  | 0.9<br><sub>2,0,2,0,2</sub> |  | 1.1<br><sub>0,0,0,3,1</sub> | 1.5 | 0.5 | 0.1 | 0.9 | 10.3 |
| Brandon Williams (GSW) | 98% | 15.3<br><sub>18,9,24,15,14</sub> | 8.8<br><sub>14,4,20,6,11</sub> |  | 2.1<br><sub>4,2,3,3,3</sub> |  | 2.6<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.2 | 1.4 | 13.5 |
| Will Richard (GSW) | 98% | 14.7<br><sub>20,3,31,3,23</sub> | 4.2<br><sub>8,0,11,0,6</sub> |  | 1.7<br><sub>5,0,0,0,3</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4<br><sub>0,0,3,0,0</sub> |  | 0.9 | 0.1 | 0.5 | 6.7 |
| Gary Payton II (GSW) | 98% | 12.6<br><sub>18,11,17,12,10</sub> | 6.1<br><sub>10,7,2,7,2</sub> |  | 2.4<br><sub>1,2,1,2,2</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.6 | 9.5 |
| Graham Ike (GSW) | 67% | 8.7<br><sub>12,12,26,3,-</sub> | 4.1<br><sub>8,10,12,3,-</sub> |  | 2.0<br><sub>2,2,10,0,-</sub> |  | 0.8<br><sub>1,1,2,1,-</sub> |  | 0.2<br><sub>1,2,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.9 |
| Charles Bassey (GSW) | 91% | 7.8<br><sub>-,-,13,2,2</sub> | 3.3<br><sub>-,-,10,0,0</sub> |  | 3.0<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 6.6 |
| LJ Cryer (GSW) | 63% | 6.7<br><sub>9,-,14,3,-</sub> | 3.0<br><sub>9,-,3,6,-</sub> |  | 0.7<br><sub>1,-,1,0,-</sub> |  | 0.6<br><sub>3,-,1,2,-</sub> |  | 0.3<br><sub>2,-,1,2,-</sub> |  | 0.1 | 0.0 | 0.4 | 4.3 |
| Malevy Leons (GSW) | 58% | 6.1<br><sub>9,-,4,3,-</sub> | 2.0<br><sub>0,-,2,0,-</sub> |  | 1.1<br><sub>1,-,0,1,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.6 |
| Luka Doncic (LAL) | 98% | 36.5<br><sub>30,37,38,37,-</sub> | 34.3<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 6.5 | 8.0<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.4 |
| Austin Reaves (LAL) | 98% | 35.5<br><sub>32,38,36,39,31</sub> | 21.3<br><sub>23,28,29,26,16</sub> | 23.5 · – | 4.1<br><sub>4,2,1,4,6</sub> | 4.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 31.0 |
| Walker Kessler (LAL) | 98% | 29.7<br><sub>30,35,28,33,26</sub> | 11.3<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.9<br><sub>9,8,7,8,9</sub> | 9.5 | 1.5<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.7 |
| Quentin Grimes (LAL) | 98% | 27.2<br><sub>27,31,20,19,38</sub> | 9.9<br><sub>10,13,3,2,23</sub> | 9.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 3.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.6 |
| Sandro Mamukelashvili (LAL) | 98% | 24.8<br><sub>22,24,21,24,30</sub> | 9.7<br><sub>5,7,9,17,13</sub> | 9.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> | 1.5 | 1.0 | 0.5 | 1.0 | 16.9 |
| Jake LaRavia (LAL) | 91% | 23.9<br><sub>18,-,15,19,35</sub> | 5.8<br><sub>10,-,0,5,2</sub> |  | 3.8<br><sub>2,-,4,1,10</sub> |  | 1.4<br><sub>2,-,1,1,0</sub> |  | 0.5<br><sub>2,-,0,1,0</sub> |  | 1.4 | 0.6 | 1.2 | 11.0 |
| Matisse Thybulle (LAL) | 96% | 23.2<br><sub>23,24,26,22,28</sub> | 6.5<br><sub>3,13,11,5,15</sub> | 6.5 · – | 2.2<br><sub>3,1,1,2,1</sub> | 2.5 | 1.2<br><sub>1,2,1,1,0</sub> |  | 1.1<br><sub>1,3,3,1,4</sub> | 1.5 | 2.0 | 0.7 | 1.0 | 9.9 |
| Collin Sexton (LAL) | 98% | 19.3<br><sub>-,16,20,14,21</sub> | 11.6<br><sub>-,5,13,9,21</sub> | 11.5 · – | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> | 2.5 | 1.3<br><sub>-,1,1,0,4</sub> | 1.5 | 1.1 | 0.1 | 1.8 | 15.8 |
| Jarred Vanderbilt (LAL) | 48% | 16.5<br><sub>-,-,-,-,21</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 4.2<br><sub>-,-,-,-,7</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.2 | 0.8 | 9.7 |
| Lawson Lovering (LAL) | 23% | 13.9 | 4.2 |  | 3.4 |  | 1.0 |  | 0.1 |  | 0.7 | 0.3 | 0.6 | 8.5 |
| Jaden Hardy (LAL) | 52% | 9.2<br><sub>7,-,-,-,9</sub> | 4.4<br><sub>3,-,-,-,2</sub> |  | 0.8<br><sub>2,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 5.8 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| AK Okereke (LAL) | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Kevon Looney (LAL) | 64% | 8.1<br><sub>15,5,5,5,-</sub> | 2.0<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.3 |
| Bronny James (LAL) | 26% | 6.4<br><sub>7,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 2.8 |
| Chris Manon (LAL) | 52% | 5.9<br><sub>6,-,-,-,-</sub> | 1.7<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.2 |

</details>


### DEN @ PHX
Out: Drew Timme (PHX), Mark Williams (PHX), Julian Strawther (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +4.5 covers 56%; o231.5 43% |
| Expected (weighted by chance each plays) | 115.6–113.6 | DEN 55% | 1.82 / 2.22 | PHX +2.5 | 229.5 | PHX +4.5 covers 58%; o231.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alpha Diallo (DEN) | Doubtful | 20% | 14.3 | 3.7 | 1.8 | 1.1 | 0.3 | 0.7 | 0.3 | 0.9 | 6.6 | small |
| Oso Ighodaro (PHX) | Questionable | 55% | 17.0 | 5.4 | 4.4 | 2.1 | 0.0 | 0.6 | 0.6 | 0.8 | 11.8 | small |
| Cameron Johnson (DEN) | Questionable | 55% | 20.1 | 8.2 | 2.8 | 1.6 | 1.1 | 0.6 | 0.3 | 0.8 | 12.6 | small |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 37.6<br><sub>37,43,36,38</sub> | 24.0<br><sub>6,42,19,23</sub> | 22.5 · – | 4.4<br><sub>10,3,6,1</sub> | 4.5 | 6.1<br><sub>3,6,8,6</sub> | 6.5 | 3.3<br><sub>0,8,3,5</sub> | 2.5 | 1.1 | 0.5 | 2.6 | 34.5 |
| Nikola Jokic | 98% | 37.0<br><sub>35,44,35,34</sub> | 25.7<br><sub>13,35,19,21</sub> | 25.5 · – | 12.8<br><sub>7,15,7,13</sub> | 12.5 | 10.1<br><sub>5,10,11,10</sub> | 9.5 | 1.6<br><sub>1,3,1,0</sub> | 1.5 | 1.6 | 1.0 | 4.0 | 48.6 |
| Christian Braun | 98% | 34.7<br><sub>33,40,34,36</sub> | 12.3<br><sub>7,15,9,15</sub> | 11.5 · – | 4.7<br><sub>6,8,4,0</sub> | 4.5 | 2.5<br><sub>1,2,2,4</sub> |  | 1.2<br><sub>1,0,1,3</sub> | 1.5 | 1.1 | 0.4 | 1.3 | 19.5 |
| Aaron Gordon | 98% | 31.3<br><sub>29,37,25,31</sub> | 14.2<br><sub>20,7,7,15</sub> | 14.5 · – | 6.1<br><sub>6,5,4,11</sub> | 5.5 | 2.7<br><sub>1,4,2,3</sub> | 2.5 | 1.5<br><sub>3,1,0,2</sub> | 1.5 | 0.8 | 0.3 | 1.5 | 23.1 |
| DeMar DeRozan | 98% | 28.2<br><sub>28,24,29,26</sub> | 15.0<br><sub>13,12,21,6</sub> | 13.5 · – | 2.7<br><sub>2,3,4,2</sub> | 2.5 | 3.5<br><sub>0,3,2,5</sub> | 2.5 | 0.6<br><sub>0,0,2,0</sub> | 0.5 | 0.9 | 0.3 | 1.8 | 21.2 |
| Trevon Brazile | 93% | 25.9<br><sub>18,28,17,32</sub> | 8.7<br><sub>4,17,6,11</sub> | 7.5 · – | 6.3<br><sub>12,9,1,8</sub> | 5.5 | 1.1<br><sub>0,0,0,0</sub> |  | 1.1<br><sub>0,3,1,1</sub> |  | 0.8 | 0.5 | 1.3 | 16.1 |
| Marvin Bagley III | 98% | 16.3<br><sub>11,9,11,19</sub> | 7.1<br><sub>2,5,7,8</sub> |  | 4.8<br><sub>3,4,2,5</sub> |  | 0.8<br><sub>1,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0</sub> |  | 0.5 | 0.6 | 0.8 | 12.7 |
| Bryce Hopkins | 93% | 16.1<br><sub>2,19,31,14</sub> | 3.8<br><sub>0,2,13,0</sub> |  | 2.2<br><sub>1,2,3,2</sub> |  | 0.8<br><sub>0,1,1,0</sub> |  | 0.3<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.8 |
| Tyus Jones | 88% | 11.7<br><sub>10,10,9,11</sub> | 3.1<br><sub>2,2,0,5</sub> |  | 1.1<br><sub>0,0,0,0</sub> |  | 1.5<br><sub>0,0,2,1</sub> |  | 0.3<br><sub>0,0,0,1</sub> |  | 0.6 | 0.1 | 0.5 | 5.7 |
| Cam Whitmore | 58% | 8.9<br><sub>-,11,4,-</sub> | 4.2<br><sub>-,4,4,-</sub> |  | 1.6<br><sub>-,2,0,-</sub> |  | 0.5<br><sub>-,0,1,-</sub> |  | 0.3<br><sub>-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |
| Zeke Nnaji | 47% | 8.5<br><sub>-,-,4,-</sub> | 2.8<br><sub>-,-,5,-</sub> |  | 1.8<br><sub>-,-,1,-</sub> |  | 0.4<br><sub>-,-,0,-</sub> |  | 0.1<br><sub>-,-,1,-</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Ryan Nembhard | 52% | 6.7<br><sub>2,-,4,-</sub> | 4.1<br><sub>5,-,4,-</sub> |  | 0.9<br><sub>1,-,0,-</sub> |  | 0.7<br><sub>1,-,1,-</sub> |  | 0.2<br><sub>1,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.7 |
| DaRon Holmes II | 52% | 6.6<br><sub>2,-,4,-</sub> | 2.7<br><sub>3,-,0,-</sub> |  | 1.3<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>1,-,1,-</sub> |  | 0.3<br><sub>1,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.4 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.0<br><sub>29,36,34</sub> | 23.2<br><sub>23,43,3</sub> | 23.5 · – | 4.1<br><sub>4,7,2</sub> | 4.5 | 6.0<br><sub>2,7,7</sub> | 5.5 | 1.8<br><sub>0,2,0</sub> | 1.5 | 0.9 | 0.3 | 2.8 | 33.3 |
| Dillon Brooks | 98% | 32.3<br><sub>27,34,33</sub> | 19.1<br><sub>10,15,19</sub> | 16.5 · – | 4.4<br><sub>4,2,5</sub> | 3.5 | 2.2<br><sub>0,5,5</sub> | 2.5 | 2.2<br><sub>1,1,3</sub> | 1.5 | 1.0 | 0.2 | 1.4 | 25.8 |
| Miles Bridges | 98% | 30.9<br><sub>29,33,32</sub> | 15.3<br><sub>8,16,17</sub> | 15.5 · – | 6.2<br><sub>4,7,8</sub> | 5.5 | 2.8<br><sub>0,3,4</sub> | 2.5 | 1.6<br><sub>0,2,2</sub> | 1.5 | 0.8 | 0.4 | 1.2 | 24.4 |
| Jalen Green | 96% | 29.5<br><sub>25,26,31</sub> | 16.0<br><sub>10,12,20</sub> | 15.5 · – | 4.2<br><sub>2,2,4</sub> | 3.5 | 3.1<br><sub>3,1,4</sub> | 3.5 | 2.0<br><sub>2,1,1</sub> | 2.5 | 1.0 | 0.3 | 1.9 | 23.4 |
| Collin Gillespie | 98% | 24.9<br><sub>21,28,23</sub> | 9.5<br><sub>0,11,9</sub> | 9.5 · – | 3.5<br><sub>1,4,1</sub> | 3.5 | 3.8<br><sub>2,9,2</sub> | 3.5 | 1.7<br><sub>0,2,3</sub> | 2.5 | 1.1 | 0.2 | 1.2 | 16.8 |
| Khaman Maluach | 96% | 20.4<br><sub>17,28,26</sub> | 6.3<br><sub>2,9,12</sub> | 8.5 · – | 6.3<br><sub>6,9,7</sub> | 8.5 | 0.7<br><sub>1,3,1</sub> |  | 0.3<br><sub>0,1,0</sub> |  | 0.4 | 1.1 | 1.1 | 13.4 |
| Jordan Goodwin | 98% | 18.0<br><sub>22,20,17</sub> | 6.8<br><sub>3,9,12</sub> | 6.5 · – | 3.8<br><sub>4,2,4</sub> | 3.5 | 1.6<br><sub>0,4,2</sub> | 1.5 | 1.0<br><sub>1,1,4</sub> | 1.5 | 1.1 | 0.2 | 0.7 | 12.2 |
| Luke Kennard | 97% | 17.4<br><sub>-,18,16</sub> | 6.5<br><sub>-,11,9</sub> |  | 2.2<br><sub>-,4,1</sub> |  | 1.6<br><sub>-,1,2</sub> |  | 0.8<br><sub>-,3,3</sub> |  | 0.6 | 0.1 | 0.6 | 10.3 |
| Ryan Dunn | 93% | 14.3<br><sub>14,13,14</sub> | 4.5<br><sub>3,5,6</sub> |  | 3.2<br><sub>2,5,2</sub> |  | 0.9<br><sub>0,0,1</sub> |  | 0.4<br><sub>0,1,1</sub> |  | 0.6 | 0.3 | 0.4 | 8.7 |
| Pat Spencer | 64% | 8.5<br><sub>7,-,-</sub> | 2.9<br><sub>3,-,-</sub> |  | 1.1<br><sub>3,-,-</sub> |  | 1.4<br><sub>1,-,-</sub> |  | 0.2<br><sub>1,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.4 |
| Rasheer Fleming | 67% | 7.9<br><sub>12,-,3</sub> | 2.9<br><sub>1,-,0</sub> |  | 1.5<br><sub>2,-,1</sub> |  | 0.3<br><sub>0,-,0</sub> |  | 0.3<br><sub>0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |
| Duop Reath | 88% | 7.7<br><sub>9,3,7</sub> | 2.8<br><sub>5,0,5</sub> |  | 1.6<br><sub>1,0,3</sub> |  | 0.4<br><sub>0,0,0</sub> |  | 0.3<br><sub>1,0,1</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |
| Jamaree Bouyea | 67% | 6.5<br><sub>7,-,3</sub> | 2.6<br><sub>3,-,2</sub> |  | 0.9<br><sub>2,-,0</sub> |  | 1.0<br><sub>2,-,1</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Koa Peat | 64% | 6.5<br><sub>7,-,3</sub> | 2.4<br><sub>4,-,0</sub> |  | 1.5<br><sub>1,-,0</sub> |  | 0.4<br><sub>0,-,0</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-30/`._
