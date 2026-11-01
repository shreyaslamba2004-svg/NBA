# NBA model · Sun 01 Nov 2026 (US date)

Updated **Mon 02 Nov, 09:14 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-01/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 7.5 (8+) | TOR @ LAL | draftkings | 3.74 | 3.53 | 2.60 | 38.4% | 25.0% | 28.3% | +6.0% | +43.8% | 0.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 11.5 (12+) | TOR @ LAL | draftkings | 24.00 | 21.01 | 13.58 | 7.4% | 3.9% | 4.8% | +14.3% | +76.7% | 0.2% |
| Scottie Barnes AST over 9.5 (10+) | TOR @ LAL | draftkings | 9.30 | 8.19 | 5.35 | 18.7% | 10.1% | 12.2% | +13.5% | +73.7% | 0.4% |
| Brandin Podziemski AST over 7.5 (8+) | LAC @ GSW | draftkings | 9.50 | 8.80 | 6.28 | 15.9% | 9.8% | 11.4% | +7.9% | +51.2% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAC @ GSW | Mon 02 Nov 12:30 | 113.7–113.9 | LAC 50% | 2.01 / 1.99 | GSW +0.5 | 227.5 | GSW -2.5 covers 44%; o220.5 65% |
| TOR @ LAL | Mon 02 Nov 13:00 | 112.1–113.1 | TOR 47% | 2.12 / 1.89 | LAL -1.5 | 225.5 | LAL -2.5 covers 47%; o224.5 51% |

### LAC @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Draymond Green (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Rui Hachimura REB under 4.5 | LAC @ GSW | draftkings | 2.13 | 2.10 | 1.71 | 58.5% | 43.9% | 47.5% | +1.2% | +24.6% | 0.3% |
| Rui Hachimura PTS under 15.5 | LAC @ GSW | draftkings | 1.93 | 1.92 | 1.58 | 63.1% | 48.3% | 52.0% | +0.6% | +22.2% | 0.2% |
| Darius Garland PR under 25.5 | LAC @ GSW | draftkings | 1.93 | 1.93 | 1.61 | 62.1% | 48.3% | 51.7% | +0.1% | +20.1% | 0.0% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 30.2<br><sub>32,37,36,26,31</sub> | 21.4<br><sub>30,26,16,14,24</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,0,4,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>4,6,11,5,5</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,4,2,1,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.2 | 3.6 | 30.1 |
| Rui Hachimura | 98% | 29.6<br><sub>32,33,29,-,26</sub> | 14.2<br><sub>10,16,5,-,12</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>8,6,4,-,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>2,1,0,-,0</sub> |  | 1.7<br><sub>2,3,1,-,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 1.5 | 19.6 |
| Derrick Jones Jr. | 98% | 27.4<br><sub>26,35,30,28,26</sub> | 10.7<br><sub>8,16,11,15,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,4,6,5,1</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>5,1,1,0,1</sub> |  | 1.1<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.7 | 1.0 | 16.0 |
| Kris Dunn | 98% | 27.3<br><sub>27,34,33,27,31</sub> | 7.2<br><sub>7,7,15,5,5</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>5,5,4,3,5</sub> | 4.5<br><sub>o 39% · u 61%</sub> | 4.2<br><sub>7,5,6,3,7</sub> | 5.5<br><sub>o 39% · u 61%</sub> | 0.8<br><sub>2,1,1,1,0</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.9 | 0.3 | 1.7 | 14.9 |
| Keaton Wagler | 96% | 24.9<br><sub>29,24,26,28,25</sub> | 13.3<br><sub>15,13,11,21,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>5,3,5,4,6</sub> | 4.5<br><sub>o 38% · u 62%</sub> | 3.2<br><sub>5,3,4,2,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>3,2,1,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.3 | 20.1 |
| Brook Lopez | 98% | 21.9<br><sub>27,20,23,22,21</sub> | 10.3<br><sub>17,22,15,2,13</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>11,4,1,3,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>1,0,2,3,0</sub> |  | 1.2<br><sub>1,2,3,0,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.0 | 1.0 | 15.7 |
| Kobe Sanders | 96% | 20.6<br><sub>19,19,20,27,24</sub> | 8.5<br><sub>2,5,12,9,7</sub> |  | 2.4<br><sub>0,3,4,4,4</sub> |  | 1.9<br><sub>3,5,2,0,2</sub> |  | 1.1<br><sub>0,1,2,1,1</sub> |  | 1.1 | 0.2 | 1.3 | 12.7 |
| Isaiah Jackson | 97% | 20.0<br><sub>15,28,24,19,22</sub> | 8.8<br><sub>13,6,10,4,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>5,6,6,5,7</sub> | 7.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>0,3,4,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.1 | 1.5 | 16.5 |
| Gradey Dick | 91% | 14.2<br><sub>19,12,18,19,12</sub> | 6.3<br><sub>12,6,6,5,3</sub> |  | 2.0<br><sub>4,4,3,5,0</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 0.6<br><sub>1,0,2,1,1</sub> |  | 0.6 | 0.1 | 0.8 | 9.1 |
| Baba Miller | 86% | 10.1<br><sub>9,-,2,17,5</sub> | 4.4<br><sub>4,-,0,4,0</sub> |  | 1.6<br><sub>3,-,1,7,1</sub> |  | 1.1<br><sub>1,-,0,1,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 7.1 |
| Cam Christie | 64% | 8.2<br><sub>2,-,-,14,5</sub> | 3.0<br><sub>0,-,-,2,2</sub> |  | 1.2<br><sub>0,-,-,0,1</sub> |  | 0.6<br><sub>0,-,-,0,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.8 |
| Jalen Pickett | 52% | 7.2<br><sub>2,-,-,8,-</sub> | 2.7<br><sub>3,-,-,4,-</sub> |  | 0.9<br><sub>0,-,-,1,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 0.2<br><sub>1,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |
| Nick Martinelli | 64% | 7.1<br><sub>2,-,-,6,5</sub> | 2.9<br><sub>0,-,-,2,3</sub> |  | 1.9<br><sub>1,-,-,3,0</sub> |  | 0.5<br><sub>1,-,-,1,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.7 | 5.3 |
| Blake Wesley | 86% | 6.7<br><sub>-,-,-,-,5</sub> | 2.7<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,4</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.6 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 96% | 34.2<br><sub>37,36,31,35,24</sub> | 20.8<br><sub>18,26,31,26,6</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>13,9,12,9,1</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>6,5,6,1,0</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,6,1,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.6 | 3.4 | 32.2 |
| Brandin Podziemski | 86% | 33.6<br><sub>33,-,33,32,33</sub> | 18.4<br><sub>18,-,18,8,21</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>2,-,7,5,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>3,-,5,6,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,-,3,0,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.2 | 2.3 | 28.9 |
| Gui Santos | 74% | 25.8<br><sub>20,23,28,-,16</sub> | 10.5<br><sub>5,7,13,-,2</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>4,4,3,-,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>2,3,1,-,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>1,1,1,-,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.1 | 0.3 | 1.7 | 18.2 |
| De'Anthony Melton | 98% | 24.9<br><sub>20,27,19,20,21</sub> | 12.1<br><sub>10,25,3,8,16</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>1,5,4,6,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>0,5,3,0,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>2,4,1,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.4 | 1.8 | 18.8 |
| Georges Niang | 96% | 23.1<br><sub>13,23,18,23,19</sub> | 9.4<br><sub>4,4,9,7,11</sub> | 7.5 · –<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>3,4,2,3,5</sub> |  | 1.4<br><sub>0,2,0,2,1</sub> |  | 1.6<br><sub>0,0,3,1,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.5 | 0.2 | 1.2 | 14.1 |
| Al Horford | 98% | 22.3<br><sub>19,-,19,18,17</sub> | 7.2<br><sub>3,-,11,4,3</sub> |  | 4.6<br><sub>5,-,3,5,2</sub> |  | 1.9<br><sub>0,-,0,2,0</sub> |  | 1.2<br><sub>1,-,3,0,1</sub> |  | 0.7 | 0.9 | 0.9 | 13.6 |
| Brandon Williams | 98% | 21.4<br><sub>9,24,15,14,17</sub> | 13.3<br><sub>4,20,6,11,9</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>2,3,3,3,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.8<br><sub>1,5,3,1,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.7<br><sub>0,2,2,0,0</sub> |  | 1.0 | 0.3 | 2.0 | 20.1 |
| Will Richard | 98% | 19.8<br><sub>3,31,3,23,13</sub> | 5.6<br><sub>0,11,0,6,3</sub> |  | 2.4<br><sub>0,0,0,3,3</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>0,3,0,0,1</sub> |  | 1.1 | 0.2 | 0.7 | 9.2 |
| Gary Payton II | 98% | 17.8<br><sub>11,17,12,10,8</sub> | 8.6<br><sub>7,2,7,2,2</sub> |  | 3.5<br><sub>2,1,2,2,4</sub> |  | 1.5<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>1,0,1,0,0</sub> |  | 1.1 | 0.2 | 0.9 | 13.6 |
| Graham Ike | 67% | 16.0<br><sub>12,26,3,-,-</sub> | 6.9<br><sub>10,12,3,-,-</sub> |  | 3.8<br><sub>2,10,0,-,-</sub> |  | 1.4<br><sub>1,2,1,-,-</sub> |  | 0.5<br><sub>2,0,1,-,-</sub> |  | 0.7 | 0.3 | 0.9 | 12.1 |
| Charles Bassey | 91% | 13.0<br><sub>-,13,2,2,9</sub> | 5.4<br><sub>-,10,0,0,6</sub> |  | 4.8<br><sub>-,7,1,0,4</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 10.9 |
| LJ Cryer | 52% | 13.0<br><sub>-,14,3,-,-</sub> | 5.4<br><sub>-,3,6,-,-</sub> |  | 1.2<br><sub>-,1,0,-,-</sub> |  | 1.0<br><sub>-,1,2,-,-</sub> |  | 0.8<br><sub>-,1,2,-,-</sub> |  | 0.3 | 0.1 | 0.7 | 7.6 |
| Malevy Leons | 52% | 11.3<br><sub>-,4,3,-,-</sub> | 3.4<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,1,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.6 | 0.3 | 0.6 | 6.3 |

</details>


### TOR @ LAL
Out: Ziaire Williams (LAL), Kawhi Leonard (TOR), Malachi Smith (TOR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walker Kessler PA under 13.5 | TOR @ LAL | draftkings | 1.91 | 1.90 | 1.58 | 63.5% | 49.0% | 52.6% | +0.4% | +21.1% | 0.1% |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 35.7<br><sub>26,37,28,31,39</sub> | 22.4<br><sub>23,28,0,28,41</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>6,14,3,6,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.9<br><sub>5,5,3,4,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 2.0 | 1.1 | 3.4 | 36.1 |
| RJ Barrett | 98% | 34.7<br><sub>26,34,32,32,34</sub> | 21.4<br><sub>20,23,20,25,9</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>4,9,2,9,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,4,2,6,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.3 | 2.6 | 31.2 |
| Immanuel Quickley | 98% | 32.5<br><sub>28,29,28,29,37</sub> | 17.4<br><sub>23,12,19,16,17</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>4,1,3,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>7,6,2,7,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>4,0,3,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.1 | 1.8 | 27.3 |
| Ja'Kobe Walter | 98% | 30.3<br><sub>23,24,31,28,32</sub> | 11.3<br><sub>10,7,22,14,9</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>3,4,4,5,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>1,2,5,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.2 | 1.0 | 16.7 |
| Jamal Shead | 98% | 24.8<br><sub>16,24,21,23,23</sub> | 7.5<br><sub>2,5,4,13,2</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,2,1,4,1</sub> |  | 5.1<br><sub>5,5,0,7,8</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.2 | 0.2 | 1.9 | 14.5 |
| Collin Murray-Boyles | 98% | 23.4<br><sub>20,18,19,15,23</sub> | 10.1<br><sub>6,8,3,10,15</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 5.6<br><sub>8,3,7,2,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,2,1</sub> | 0.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.8 | 1.3 | 17.5 |
| Jakob Poeltl | 98% | 21.8<br><sub>22,27,19,10,23</sub> | 8.2<br><sub>3,6,0,2,12</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 6.2<br><sub>6,9,1,2,11</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,2,0,0,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.6 | 1.2 | 15.9 |
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
| Luka Doncic | 98% | 36.7<br><sub>37,38,37,-,37</sub> | 31.6<br><sub>23,52,41,-,37</sub> | 33.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>6,8,5,-,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 7.4<br><sub>7,10,9,-,5</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 4.2<br><sub>2,8,6,-,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.5 | 4.7 | 46.0 |
| Austin Reaves | 98% | 35.9<br><sub>38,36,39,31,37</sub> | 20.4<br><sub>28,29,26,16,21</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,1,4,6,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.0<br><sub>9,4,7,1,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,4,4,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 3.6 | 29.6 |
| Walker Kessler | 98% | 30.3<br><sub>35,28,33,26,31</sub> | 10.8<br><sub>22,2,13,11,10</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 10.2<br><sub>8,7,8,9,13</sub> | 10.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>3,0,0,1,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.2 | 1.6 | 22.4 |
| Quentin Grimes | 98% | 26.7<br><sub>31,20,19,38,26</sub> | 9.2<br><sub>13,3,2,23,3</sub> |  | 3.2<br><sub>8,1,4,3,3</sub> |  | 2.2<br><sub>4,1,0,5,2</sub> |  | 1.1<br><sub>3,0,0,0,1</sub> |  | 0.8 | 0.3 | 1.2 | 14.7 |
| Matisse Thybulle | 96% | 24.4<br><sub>24,26,22,28,28</sub> | 7.7<br><sub>13,11,5,15,10</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,1,2,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>2,1,1,0,0</sub> |  | 1.2<br><sub>3,3,1,4,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.8 | 0.7 | 1.0 | 11.2 |
| Jake LaRavia | 93% | 24.1<br><sub>-,15,19,35,28</sub> | 6.5<br><sub>-,0,5,2,10</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>-,4,1,10,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>-,1,1,0,0</sub> |  | 0.7<br><sub>-,0,1,0,2</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.6 | 1.3 | 11.4 |
| Sandro Mamukelashvili | 98% | 23.1<br><sub>24,21,24,30,20</sub> | 9.0<br><sub>7,9,17,13,4</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>5,3,4,8,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,0,2,3,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,1,3,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.5 | 1.0 | 15.8 |
| Collin Sexton | 98% | 18.2<br><sub>16,20,14,21,16</sub> | 10.2<br><sub>5,13,9,21,0</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>1,2,1,4,2</sub> |  | 1.8<br><sub>2,1,4,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,1,0,4,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.2 | 1.6 | 13.9 |
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
