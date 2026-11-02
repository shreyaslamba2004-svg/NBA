# NBA model · Sun 01 Nov 2026 (US date)

Updated **Mon 02 Nov, 12:23 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-01/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos PTS over 9.5 (10+) | LAC @ GSW | draftkings | 2.40 | 1.97 | 1.97 | 50.7% | 50.7% | 50.7% | +21.8% | +21.8% | 2.0% |
| Rui Hachimura PTS under 15.5 | LAC @ GSW | tab | 1.95 | 1.85 | 1.56 | 64.2% | 50.7% | 54.1% | +5.6% | +25.4% | 1.5% |
| Scottie Barnes AST over 7.5 (8+) | TOR @ LAL | draftkings | 3.68 | 3.49 | 2.60 | 38.4% | 25.4% | 28.7% | +5.5% | +41.4% | 0.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 9.5 (10+) | TOR @ LAL | draftkings | 9.30 | 8.19 | 5.35 | 18.7% | 10.1% | 12.2% | +13.5% | +73.7% | 0.4% |
| Scottie Barnes AST over 11.5 (12+) | TOR @ LAL | draftkings | 23.00 | 20.45 | 13.58 | 7.4% | 4.1% | 4.9% | +12.4% | +69.4% | 0.1% |
| Gui Santos REB over 7.5 (8+) | LAC @ GSW | draftkings | 10.30 | 9.43 | 6.56 | 15.2% | 9.1% | 10.6% | +9.3% | +56.9% | 0.2% |
| Gui Santos PA over 19.5 (20+) | LAC @ GSW | draftkings | 11.40 | 10.50 | 7.40 | 13.5% | 8.2% | 9.5% | +8.6% | +53.9% | 0.2% |
| Gui Santos PA over 14.5 (15+) | LAC @ GSW | draftkings | 4.02 | 3.81 | 2.84 | 35.2% | 23.2% | 26.2% | +5.5% | +41.7% | 0.5% |
| Gui Santos 3PM over 1.5 (2+) | LAC @ GSW | draftkings | 4.25 | 4.04 | 3.02 | 33.1% | 22.0% | 24.8% | +5.3% | +40.7% | 0.4% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walker Kessler PTS under 12.5 | TOR @ LAL | tab | 1.90 | 1.79 | 1.49 | 67.2% | 51.9% | 55.7% | +6.0% | +27.8% | 1.7% |
| Brandon Williams PTS under 13.5 | LAC @ GSW | betright | 1.95 | 1.86 | 1.50 | 66.6% | 49.6% | 53.8% | +5.1% | +30.0% | 1.4% |
| Brandon Williams PTS under 14.5 | LAC @ GSW | draftkings | 1.88 | 1.80 | 1.40 | 71.6% | 50.4% | 55.7% | +5.0% | +35.0% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAC @ GSW | Mon 02 Nov 12:30 | 113.7–113.9 | LAC 50% | 2.01 / 1.99 | GSW +0.5 | 227.5 | GSW -1.5 covers 47%; o220.5 65% |
| TOR @ LAL | Mon 02 Nov 13:00 | 112.1–113.1 | TOR 47% | 2.12 / 1.89 | LAL -1.5 | 225.5 | LAL -3.5 covers 44%; o223.5 53% |

### LAC @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Draymond Green (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos PTS over 9.5 (10+) | LAC @ GSW | draftkings | 2.40 | 1.97 | 1.97 | 50.7% | 50.7% | 50.7% | +21.8% | +21.8% | 2.0% |
| Rui Hachimura PTS under 15.5 | LAC @ GSW | tab | 1.95 | 1.85 | 1.56 | 64.2% | 50.7% | 54.1% | +5.6% | +25.4% | 1.5% |
| Yaxel Lendeborg PTS under 19.5 | LAC @ GSW | pointsbetau | 2.05 | 1.98 | 1.76 | 56.8% | 48.4% | 50.5% | +3.4% | +16.4% | 0.8% |
| Darius Garland PTS under 22.5 | LAC @ GSW | betright | 2.00 | 1.95 | 1.61 | 61.9% | 47.8% | 51.3% | +2.7% | +23.9% | 0.7% |
| Derrick Jones Jr. PTS under 10.5 | LAC @ GSW | draftkings | 2.00 | 1.97 | 1.78 | 56.3% | 48.9% | 50.7% | +1.5% | +12.5% | 0.4% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 100% | 29.7<br><sub>32,37,36,26,31</sub> | 21.0<br><sub>30,26,16,14,24</sub> | 23.5 · 22.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>1,0,4,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>4,6,11,5,5</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>3,4,2,1,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.2 | 3.6 | 29.6 |
| Rui Hachimura | 100% | 29.4<br><sub>32,33,29,-,26</sub> | 14.0<br><sub>10,16,5,-,12</sub> | – · 15.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>8,6,4,-,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>2,1,0,-,0</sub> |  | 1.7<br><sub>2,3,1,-,2</sub> | 2.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.3 | 1.5 | 19.4 |
| Derrick Jones Jr. | 100% | 27.3<br><sub>26,35,30,28,26</sub> | 10.4<br><sub>8,16,11,15,10</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>6,4,6,5,1</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>5,1,1,0,1</sub> |  | 1.1<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 1.0 | 15.7 |
| Kris Dunn | 100% | 27.2<br><sub>27,34,33,27,31</sub> | 7.1<br><sub>7,7,15,5,5</sub> | 8.5 · 8.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>5,5,4,3,5</sub> | 4.5<br><sub>o 39% · u 61%</sub> | 4.2<br><sub>7,5,6,3,7</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 0.8<br><sub>2,1,1,1,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 1.9 | 0.3 | 1.6 | 14.8 |
| Keaton Wagler | 96% | 24.5<br><sub>29,24,26,28,25</sub> | 12.9<br><sub>15,13,11,21,12</sub> | 12.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,3,5,4,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>5,3,4,2,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>3,2,1,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.3 | 2.2 | 19.6 |
| Isaiah Jackson | 100% | 22.3<br><sub>15,28,24,19,22</sub> | 9.8<br><sub>13,6,10,4,10</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>5,6,6,5,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,3,4,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.2 | 1.6 | 18.4 |
| Brook Lopez | 98% | 21.8<br><sub>27,20,23,22,21</sub> | 10.2<br><sub>17,22,15,2,13</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>11,4,1,3,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>1,0,2,3,0</sub> |  | 1.2<br><sub>1,2,3,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 1.0 | 1.0 | 15.5 |
| Kobe Sanders | 96% | 20.6<br><sub>19,19,20,27,24</sub> | 8.4<br><sub>2,5,12,9,7</sub> |  | 2.3<br><sub>0,3,4,4,4</sub> |  | 1.9<br><sub>3,5,2,0,2</sub> |  | 1.1<br><sub>0,1,2,1,1</sub> |  | 1.1 | 0.1 | 1.3 | 12.6 |
| Gradey Dick | 91% | 14.2<br><sub>19,12,18,19,12</sub> | 6.3<br><sub>12,6,6,5,3</sub> |  | 2.0<br><sub>4,4,3,5,0</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 0.6<br><sub>1,0,2,1,1</sub> |  | 0.6 | 0.1 | 0.8 | 9.1 |
| Baba Miller | 86% | 10.0<br><sub>9,-,2,17,5</sub> | 4.3<br><sub>4,-,0,4,0</sub> |  | 1.6<br><sub>3,-,1,7,1</sub> |  | 1.0<br><sub>1,-,0,1,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 7.0 |
| Cam Christie | 64% | 8.2<br><sub>2,-,-,14,5</sub> | 3.0<br><sub>0,-,-,2,2</sub> |  | 1.3<br><sub>0,-,-,0,1</sub> |  | 0.6<br><sub>0,-,-,0,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.9 |
| Jalen Pickett | 52% | 7.2<br><sub>2,-,-,8,-</sub> | 2.7<br><sub>3,-,-,4,-</sub> |  | 0.9<br><sub>0,-,-,1,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 0.2<br><sub>1,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Nick Martinelli | 64% | 7.1<br><sub>2,-,-,6,5</sub> | 2.9<br><sub>0,-,-,2,3</sub> |  | 1.9<br><sub>1,-,-,3,0</sub> |  | 0.5<br><sub>1,-,-,1,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.6 | 5.3 |
| Blake Wesley | 86% | 6.7<br><sub>-,-,-,-,5</sub> | 2.7<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,4</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.5 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 100% | 34.1<br><sub>37,36,31,35,24</sub> | 19.2<br><sub>18,26,31,26,6</sub> | 20.5 · 19.5<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>13,9,12,9,1</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>6,5,6,1,0</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 1.8<br><sub>1,6,1,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.6 | 3.4 | 30.6 |
| Brandin Podziemski | 100% | 33.3<br><sub>33,-,33,32,33</sub> | 17.6<br><sub>18,-,18,8,21</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>2,-,7,5,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>3,-,5,6,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,-,3,0,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.2 | 2.2 | 27.9 |
| Georges Niang | 100% | 26.7<br><sub>13,23,18,23,19</sub> | 10.6<br><sub>4,4,9,7,11</sub> | 10.5 · 7.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>3,4,2,3,5</sub> |  | 1.6<br><sub>0,2,0,2,1</sub> |  | 1.9<br><sub>0,0,3,1,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.6 | 0.2 | 1.5 | 16.0 |
| De'Anthony Melton | 100% | 26.0<br><sub>20,27,19,20,21</sub> | 12.2<br><sub>10,25,3,8,16</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>1,5,4,6,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>0,5,3,0,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>2,4,1,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.6 | 0.4 | 1.9 | 19.1 |
| Gui Santos | 80% | 25.6<br><sub>20,23,28,-,16</sub> | 10.4<br><sub>5,7,13,-,2</sub> | 7.5 · 9.5<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>4,4,3,-,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>2,3,1,-,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>1,1,1,-,0</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.3 | 1.7 | 17.9 |
| Charles Bassey | 100% | 21.4<br><sub>-,13,2,2,9</sub> | 8.8<br><sub>-,10,0,0,6</sub> |  | 7.9<br><sub>-,7,1,0,4</sub> |  | 1.0<br><sub>-,0,0,0,1</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.7 | 1.5 | 1.2 | 17.7 |
| Al Horford | 98% | 21.2<br><sub>19,-,19,18,17</sub> | 6.9<br><sub>3,-,11,4,3</sub> |  | 4.4<br><sub>5,-,3,5,2</sub> |  | 1.8<br><sub>0,-,0,2,0</sub> |  | 1.1<br><sub>1,-,3,0,1</sub> |  | 0.6 | 0.8 | 0.8 | 13.1 |
| Brandon Williams | 98% | 19.7<br><sub>9,24,15,14,17</sub> | 11.7<br><sub>4,20,6,11,9</sub> | 14.5 · 13.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,3,3,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>1,5,3,1,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>0,2,2,0,0</sub> |  | 0.9 | 0.3 | 1.8 | 17.8 |
| Will Richard | 98% | 18.8<br><sub>3,31,3,23,13</sub> | 5.1<br><sub>0,11,0,6,3</sub> |  | 2.2<br><sub>0,0,0,3,3</sub> |  | 1.1<br><sub>0,1,0,0,2</sub> |  | 0.6<br><sub>0,3,0,0,1</sub> |  | 1.1 | 0.2 | 0.7 | 8.5 |
| Gary Payton II | 98% | 16.5<br><sub>11,17,12,10,8</sub> | 7.7<br><sub>7,2,7,2,2</sub> |  | 3.2<br><sub>2,1,2,2,4</sub> |  | 1.3<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>1,0,1,0,0</sub> |  | 1.1 | 0.2 | 0.8 | 12.2 |
| Graham Ike | 67% | 15.4<br><sub>12,26,3,-,-</sub> | 6.6<br><sub>10,12,3,-,-</sub> |  | 3.6<br><sub>2,10,0,-,-</sub> |  | 1.3<br><sub>1,2,1,-,-</sub> |  | 0.5<br><sub>2,0,1,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 11.5 |
| LJ Cryer | 52% | 12.6<br><sub>-,14,3,-,-</sub> | 5.1<br><sub>-,3,6,-,-</sub> |  | 1.2<br><sub>-,1,0,-,-</sub> |  | 0.9<br><sub>-,1,2,-,-</sub> |  | 0.8<br><sub>-,1,2,-,-</sub> |  | 0.2 | 0.1 | 0.7 | 7.3 |
| Malevy Leons | 52% | 9.9<br><sub>-,4,3,-,-</sub> | 2.9<br><sub>-,2,0,-,-</sub> |  | 1.8<br><sub>-,0,1,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.5 | 0.3 | 0.5 | 5.4 |

</details>


### TOR @ LAL
Out: Ziaire Williams (LAL), Kawhi Leonard (TOR), Malachi Smith (TOR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic PTS under 33.5 | TOR @ LAL | pointsbetau | 1.87 | 1.85 | 1.64 | 61.0% | 51.6% | 53.9% | +0.8% | +14.0% | 0.2% |
| Walker Kessler PTS under 11.5 | TOR @ LAL | unibet | 2.00 | 1.99 | 1.66 | 60.2% | 46.8% | 50.1% | +0.3% | +20.4% | 0.1% |
| Austin Reaves PR under 26.5 | TOR @ LAL | draftkings | 1.91 | 1.91 | 1.59 | 63.0% | 48.9% | 52.5% | +0.2% | +20.3% | 0.0% |
| Collin Sexton PTS over 8.5 (9+) | TOR @ LAL | unibet | 1.91 | 1.91 | 1.78 | 56.0% | 51.2% | 52.4% | +0.0% | +7.0% | 0.0% |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 35.7<br><sub>26,37,28,31,39</sub> | 22.4<br><sub>23,28,0,28,41</sub> | 22.5 · 22.5<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>6,14,3,6,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.9<br><sub>5,5,3,4,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 2.0 | 1.1 | 3.4 | 36.1 |
| RJ Barrett | 98% | 34.7<br><sub>26,34,32,32,34</sub> | 21.4<br><sub>20,23,20,25,9</sub> | 20.5 · 20.5<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>4,9,2,9,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,4,2,6,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.3 | 2.6 | 31.2 |
| Immanuel Quickley | 98% | 32.5<br><sub>28,29,28,29,37</sub> | 17.4<br><sub>23,12,19,16,17</sub> | 16.5 · 17.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>4,1,3,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>7,6,2,7,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>4,0,3,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.1 | 1.8 | 27.3 |
| Ja'Kobe Walter | 98% | 30.3<br><sub>23,24,31,28,32</sub> | 11.3<br><sub>10,7,22,14,9</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>3,4,4,5,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>1,2,5,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.2 | 1.0 | 16.7 |
| Jamal Shead | 98% | 24.8<br><sub>16,24,21,23,23</sub> | 7.5<br><sub>2,5,4,13,2</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>2,2,1,4,1</sub> |  | 5.1<br><sub>5,5,0,7,8</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.2 | 0.2 | 1.9 | 14.5 |
| Collin Murray-Boyles | 98% | 23.4<br><sub>20,18,19,15,23</sub> | 10.1<br><sub>6,8,3,10,15</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>8,3,7,2,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,2,1</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.8 | 1.3 | 17.5 |
| Jakob Poeltl | 98% | 21.8<br><sub>22,27,19,10,23</sub> | 8.2<br><sub>3,6,0,2,12</sub> | 6.5 · 6.5<br><sub>o 54% · u 46%</sub> | 6.2<br><sub>6,9,1,2,11</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>0,2,0,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.6 | 1.2 | 15.9 |
| Jamison Battle | 96% | 16.8<br><sub>11,12,13,20,19</sub> | 5.9<br><sub>8,5,4,7,2</sub> |  | 2.2<br><sub>5,0,1,0,0</sub> |  | 0.8<br><sub>0,0,2,1,0</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.1 | 0.5 | 9.0 |
| Allen Graves | 96% | 14.1<br><sub>19,6,20,18,9</sub> | 4.5<br><sub>5,2,11,3,7</sub> |  | 3.0<br><sub>5,2,6,1,4</sub> |  | 0.7<br><sub>0,0,4,0,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.5 | 0.8 | 8.2 |
| Kyle Anderson | 58% | 9.8<br><sub>5,-,11,5,-</sub> | 2.8<br><sub>0,-,0,0,-</sub> |  | 1.9<br><sub>1,-,2,0,-</sub> |  | 1.5<br><sub>2,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 6.2 |
| Trayce Jackson-Davis | 91% | 8.1<br><sub>10,1,6,20,1</sub> | 3.2<br><sub>9,0,3,6,0</sub> |  | 2.4<br><sub>1,0,1,11,0</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 6.3 |
| Jaden Bradley | 67% | 6.0<br><sub>5,1,5,5,-</sub> | 2.0<br><sub>0,0,6,0,-</sub> |  | 1.0<br><sub>0,0,1,1,-</sub> |  | 0.5<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.5 |
| Alijah Martin | 67% | 6.0<br><sub>5,1,7,5,-</sub> | 2.3<br><sub>3,0,2,5,-</sub> |  | 0.9<br><sub>0,0,2,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.7<br><sub>37,38,37,-,37</sub> | 31.6<br><sub>23,52,41,-,37</sub> | 33.5 · 32.5<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>6,8,5,-,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 7.4<br><sub>7,10,9,-,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>2,8,6,-,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.5 | 4.7 | 46.0 |
| Austin Reaves | 98% | 35.9<br><sub>38,36,39,31,37</sub> | 20.4<br><sub>28,29,26,16,21</sub> | 22.5 · 22.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,1,4,6,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.0<br><sub>9,4,7,1,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>3,4,4,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 3.6 | 29.6 |
| Walker Kessler | 98% | 30.3<br><sub>35,28,33,26,31</sub> | 10.8<br><sub>22,2,13,11,10</sub> | 12.5 · 12.5<br><sub>o 44% · u 56%</sub> | 10.2<br><sub>8,7,8,9,13</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.2 | 1.6 | 22.4 |
| Quentin Grimes | 98% | 26.7<br><sub>31,20,19,38,26</sub> | 9.2<br><sub>13,3,2,23,3</sub> |  | 3.2<br><sub>8,1,4,3,3</sub> |  | 2.2<br><sub>4,1,0,5,2</sub> |  | 1.1<br><sub>3,0,0,0,1</sub> |  | 0.8 | 0.3 | 1.2 | 14.7 |
| Matisse Thybulle | 96% | 24.4<br><sub>24,26,22,28,28</sub> | 7.7<br><sub>13,11,5,15,10</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,1,2,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>2,1,1,0,0</sub> |  | 1.2<br><sub>3,3,1,4,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.8 | 0.7 | 1.0 | 11.2 |
| Jake LaRavia | 93% | 24.1<br><sub>-,15,19,35,28</sub> | 6.5<br><sub>-,0,5,2,10</sub> | 6.5 · 6.5<br><sub>o 45% · u 55%</sub> | 3.7<br><sub>-,4,1,10,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>-,1,1,0,0</sub> |  | 0.7<br><sub>-,0,1,0,2</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.6 | 1.3 | 11.4 |
| Sandro Mamukelashvili | 98% | 23.1<br><sub>24,21,24,30,20</sub> | 9.0<br><sub>7,9,17,13,4</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>5,3,4,8,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,0,2,3,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,1,3,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.5 | 1.0 | 15.8 |
| Collin Sexton | 98% | 18.2<br><sub>16,20,14,21,16</sub> | 10.2<br><sub>5,13,9,21,0</sub> | 8.5 · 8.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>1,2,1,4,2</sub> |  | 1.8<br><sub>2,1,4,2,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>1,1,0,4,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.2 | 1.6 | 13.9 |
| Lawson Lovering | 16% | 14.5 | 4.3 |  | 3.6 |  | 0.9 |  | 0.1 |  | 0.5 | 0.4 | 0.7 | 8.8 |
| Jarred Vanderbilt | 52% | 14.2<br><sub>-,-,-,21,13</sub> | 3.4<br><sub>-,-,-,0,0</sub> |  | 3.6<br><sub>-,-,-,7,3</sub> |  | 1.1<br><sub>-,-,-,2,3</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.1 |
| Cameron Carr | 16% | 12.5 | 5.4 |  | 2.3 |  | 1.1 |  | 0.4 |  | 0.4 | 0.2 | 0.6 | 8.7 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Kevon Looney | 52% | 8.0<br><sub>5,5,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 2.7<br><sub>1,2,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.1 |
| Jaden Hardy | 63% | 7.6<br><sub>-,-,-,9,1</sub> | 3.7<br><sub>-,-,-,2,0</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Chris Manon | 58% | 5.7<br><sub>-,-,-,-,1</sub> | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.2 |
| Bronny James | 48% | 5.6<br><sub>-,-,-,-,1</sub> | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 2.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-01/`._
