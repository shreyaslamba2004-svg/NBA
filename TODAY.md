# NBA model · Wed 25 Nov 2026 (US date)

Updated **Thu 26 Nov, 12:11 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-25/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Draymond Green AST over 9.5 (10+) | SAC @ GSW | draftkings | 17.60 | 14.66 | 7.32 | 13.7% | 5.3% | 6.8% | +20.1% | +140.5% | 0.3% |
| Cam Spencer AST over 9.5 (10+) | LAC @ MEM | draftkings | 14.40 | 12.35 | 6.51 | 15.4% | 6.5% | 8.1% | +16.6% | +121.2% | 0.3% |
| Kevin Durant AST over 7.5 (8+) | PHX @ HOU | draftkings | 15.60 | 14.08 | 8.26 | 12.1% | 6.0% | 7.1% | +10.7% | +88.9% | 0.2% |
| Draymond Green AST over 7.5 (8+) | SAC @ GSW | draftkings | 6.26 | 5.70 | 3.40 | 29.4% | 14.9% | 17.5% | +9.9% | +84.1% | 0.5% |
| Cam Spencer AST over 7.5 (8+) | LAC @ MEM | draftkings | 5.36 | 4.97 | 3.09 | 32.3% | 17.4% | 20.1% | +7.9% | +73.3% | 0.4% |
| Amen Thompson AST over 5.5 (6+) | PHX @ HOU | draftkings | 6.77 | 6.33 | 4.04 | 24.8% | 13.8% | 15.8% | +6.9% | +67.7% | 0.3% |
| Kevin Durant AST over 5.5 (6+) | PHX @ HOU | draftkings | 4.98 | 4.68 | 3.03 | 33.0% | 18.8% | 21.3% | +6.3% | +64.5% | 0.4% |
| Amen Thompson AST over 7.5 (8+) | PHX @ HOU | draftkings | 21.00 | 19.96 | 13.25 | 7.5% | 4.5% | 5.0% | +5.2% | +58.5% | 0.1% |
| Egor Demin AST over 5.5 (6+) | BKN @ MIL | draftkings | 8.90 | 8.46 | 5.62 | 17.8% | 10.5% | 11.8% | +5.2% | +58.4% | 0.2% |
| Zach Edey REB over 13.5 (14+) | LAC @ MEM | draftkings | 12.60 | 12.00 | 8.01 | 12.5% | 7.4% | 8.3% | +5.0% | +57.3% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAC @ MEM | Thu 26 Nov 12:00 | 115.6–117.7 | LAC 44% | 2.27 / 1.79 | MEM -2.5 | 233.5 | MEM -7.5 covers 35%; o227.5 62% |
| BKN @ MIL | Thu 26 Nov 12:00 | 108.5–115.5 | BKN 31% | 3.24 / 1.45 | MIL -7.5 | 223.5 | MIL -1.5 covers 66%; o233.5 30% |
| PHX @ HOU | Thu 26 Nov 12:30 | 110.8–117.4 | PHX 32% | 3.14 / 1.47 | HOU -6.5 | 228.5 | HOU -9.5 covers 42%; o222.5 62% |
| SAC @ GSW | Thu 26 Nov 14:00 | 105.9–114.2 | SAC 28% | 3.62 / 1.38 | GSW -8.5 | 219.5 | GSW -8.5 covers 49%; o215.5 59% |
| SAS @ POR | Thu 26 Nov 14:00 | 111.0–113.2 | SAS 43% | 2.30 / 1.77 | POR -2.5 | 223.5 | POR +3.5 covers 65%; o227.5 43% |

### LAC @ MEM
Out: Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM), Bradley Beal (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keaton Wagler PTS under 8.5 | LAC @ MEM | tab | 2.00 | 1.95 | 1.98 | 50.6% | 51.3% | 51.2% | +2.4% | +1.3% | 0.6% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 99% | 30.7<br><sub>35,30,35,32,34</sub> | 19.8<br><sub>27,20,23,16,26</sub> | 19.5 · 19.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>6,3,0,1,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>7,7,5,2,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,2,3,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.3 | 3.0 | 28.7 |
| Brandon Ingram | 96% | 27.7<br><sub>-,-,-,-,27</sub> | 15.6<br><sub>-,-,-,-,16</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>-,-,-,-,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>-,-,-,-,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>-,-,-,-,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.7 | 2.1 | 23.3 |
| Rui Hachimura | 98% | 26.9<br><sub>22,27,32,29,29</sub> | 13.2<br><sub>4,20,17,19,19</sub> | 12.5 · 13.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>2,5,7,8,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>0,4,2,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.4 | 1.2 | 19.1 |
| Derrick Jones Jr. | 99% | 24.9<br><sub>26,28,27,26,23</sub> | 8.9<br><sub>13,5,8,4,7</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>4,1,2,7,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,1,1,1,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0<br><sub>3,0,0,1,1</sub> |  | 0.9 | 0.9 | 0.9 | 14.0 |
| Max Strus | 98% | 23.3<br><sub>25,21,32,29,26</sub> | 8.6<br><sub>14,3,18,5,8</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>3,2,5,6,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,1,4,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>4,1,5,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.2 | 1.0 | 14.9 |
| Brook Lopez | 99% | 22.9<br><sub>29,23,27,25,21</sub> | 12.1<br><sub>7,23,23,21,3</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>5,6,3,6,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>8,2,4,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,4,5,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.7 | 1.1 | 1.1 | 18.6 |
| Kris Dunn | 99% | 21.7<br><sub>18,26,20,19,23</sub> | 6.1<br><sub>7,2,6,3,9</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>3,5,2,4,5</sub> |  | 3.3<br><sub>1,5,2,5,4</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 1.5 | 0.3 | 1.1 | 12.5 |
| Keaton Wagler | 98% | 18.2<br><sub>28,18,17,19,17</sub> | 9.3<br><sub>12,15,7,7,2</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,2,5,7,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>5,0,2,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0<br><sub>2,1,1,1,0</sub> |  | 0.7 | 0.2 | 1.5 | 14.5 |
| Kobe Sanders | 98% | 15.9<br><sub>20,18,14,19,12</sub> | 6.4<br><sub>2,5,0,9,6</sub> |  | 1.8<br><sub>6,1,1,3,0</sub> |  | 1.5<br><sub>4,3,1,1,0</sub> |  | 0.8<br><sub>0,0,0,3,2</sub> |  | 0.7 | 0.1 | 0.9 | 9.8 |
| Isaiah Jackson | 98% | 13.9<br><sub>15,19,9,4,18</sub> | 6.0<br><sub>13,8,6,0,6</sub> |  | 4.2<br><sub>2,5,4,0,6</sub> |  | 1.2<br><sub>2,0,2,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.7 | 1.0 | 1.0 | 11.4 |
| Gradey Dick | 76% | 11.1<br><sub>19,17,13,16,-</sub> | 4.8<br><sub>12,0,2,6,-</sub> |  | 1.7<br><sub>2,0,2,5,-</sub> |  | 0.6<br><sub>0,1,1,2,-</sub> |  | 0.4<br><sub>2,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 7.2 |
| Yanic Konan Niederhauser | 72% | 9.3<br><sub>-,-,11,16,8</sub> | 3.4<br><sub>-,-,2,6,2</sub> |  | 2.6<br><sub>-,-,3,6,1</sub> |  | 0.6<br><sub>-,-,0,1,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 6.5 |
| Baba Miller | 91% | 7.6<br><sub>5,4,1,3,1</sub> | 3.8<br><sub>2,3,0,1,0</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Cam Christie | 66% | 6.0<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,3,0,3,-</sub> |  | 1.0<br><sub>-,0,0,0,-</sub> |  | 0.5<br><sub>-,0,0,1,-</sub> |  | 0.1<br><sub>-,1,0,1,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.1 |
| Blake Wesley | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.9 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 30.8<br><sub>27,33,25,30,30</sub> | 17.0<br><sub>18,20,19,23,16</sub> | 16.5 · 16.5<br><sub>o 48% · u 52%</sub> | 7.9<br><sub>8,3,4,7,9</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>6,5,4,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,4,5,4,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 1.9 | 28.6 |
| Ty Jerome | 98% | 30.2<br><sub>-,-,-,27,29</sub> | 23.5<br><sub>-,-,-,18,29</sub> | 23.5 · 23.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.9<br><sub>-,-,-,6,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>-,-,-,3,7</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.2 | 2.8 | 32.9 |
| Jaylen Wells | 99% | 27.1<br><sub>27,26,24,25,20</sub> | 11.9<br><sub>8,5,22,8,8</sub> | 10.5 · 9.5<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>4,4,7,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.1 | 0.9 | 16.6 |
| Cam Spencer | 98% | 25.1<br><sub>32,29,27,30,21</sub> | 11.8<br><sub>12,26,9,9,24</sub> | 10.5 · 9.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>6,1,2,5,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>9,7,11,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>1,5,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.4 | 21.1 |
| Zach Edey | 88% | 23.1<br><sub>21,21,-,23,23</sub> | 10.6<br><sub>23,11,-,8,8</sub> | 8.5 · 8.5<br><sub>o 53% · u 47%</sub> | 8.8<br><sub>10,2,-,2,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>1,1,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 1.2 | 1.5 | 20.6 |
| Javon Small | 98% | 23.0<br><sub>29,21,25,-,19</sub> | 10.2<br><sub>12,2,14,-,3</sub> |  | 3.5<br><sub>5,4,7,-,3</sub> |  | 4.7<br><sub>12,5,7,-,5</sub> |  | 1.3<br><sub>0,0,2,-,0</sub> |  | 0.8 | 0.2 | 1.5 | 18.3 |
| Taylor Hendricks | 91% | 22.9<br><sub>19,21,20,27,24</sub> | 10.1<br><sub>9,18,11,5,3</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>3,6,1,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,2,1,2,1</sub> |  | 1.2<br><sub>1,1,0,0,1</sub> |  | 0.9 | 0.5 | 1.0 | 16.3 |
| Olivier-Maxence Prosper | 88% | 19.3<br><sub>16,16,24,23,19</sub> | 10.1<br><sub>12,5,16,7,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>0,2,5,6,3</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.7 | 0.2 | 0.9 | 14.9 |
| Isaiah Stewart | 98% | 18.7<br><sub>-,-,18,21,21</sub> | 9.0<br><sub>-,-,8,10,11</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>-,-,4,2,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>-,-,1,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.3 | 0.9 | 0.9 | 13.7 |
| Kris Murray | 91% | 18.1<br><sub>6,6,4,12,32</sub> | 4.3<br><sub>0,5,0,7,9</sub> | 5.5 · 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>1,0,1,0,3</sub> |  | 1.1<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,1</sub> |  | 0.8 | 0.3 | 0.6 | 8.0 |
| Jahmai Mashack | 63% | 13.5<br><sub>2,13,26,22,-</sub> | 3.3<br><sub>0,3,0,0,-</sub> |  | 1.6<br><sub>0,2,3,2,-</sub> |  | 1.7<br><sub>1,2,4,1,-</sub> |  | 0.2<br><sub>0,1,0,0,-</sub> |  | 0.7 | 0.3 | 0.8 | 6.7 |
| Quinten Post | 80% | 8.9<br><sub>9,6,10,-,3</sub> | 3.3<br><sub>5,3,5,-,0</sub> |  | 1.7<br><sub>3,2,1,-,0</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,1,0,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.4 |
| Karim Lopez | 48% | 6.7<br><sub>1,-,4,-,-</sub> | 2.2<br><sub>0,-,3,-,-</sub> |  | 1.2<br><sub>0,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,1,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 3.8 |

</details>


### BKN @ MIL
Out: Chaney Johnson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Nolan Traore (BKN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle PTS under 21.5 | BKN @ MIL | draftkings | 1.97 | 1.95 | 1.73 | 57.8% | 49.9% | 51.3% | +1.2% | +13.9% | 0.3% |
| Myles Turner PTS over 9.5 (10+) | BKN @ MIL | pointsbetau | 2.05 | 2.04 | 2.07 | 48.4% | 49.3% | 49.1% | +0.7% | -0.8% | 0.2% |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 99% | 34.0<br><sub>31,34,27,39,35</sub> | 20.9<br><sub>22,33,17,27,29</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>4,6,0,9,4</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>5,1,4,6,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>3,2,3,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 3.3 | 32.2 |
| Michael Porter Jr. | 88% | 33.8<br><sub>-,40,27,34,31</sub> | 20.5<br><sub>-,25,5,16,11</sub> | 22.5 · 21.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>-,6,3,4,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>-,2,1,5,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.9<br><sub>-,2,1,3,0</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.4 | 2.2 | 29.8 |
| Egor Demin | 98% | 26.3<br><sub>27,26,31,21,25</sub> | 11.5<br><sub>11,9,22,6,10</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>1,3,4,3,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>2,4,4,2,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>3,2,3,0,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.7 | 18.1 |
| Mikel Brown Jr. | 98% | 26.0<br><sub>20,18,27,24,29</sub> | 13.3<br><sub>6,3,15,18,17</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>1,1,1,1,5</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>2,5,4,0,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,1,2,3,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 2.2 | 20.0 |
| Day'Ron Sharpe | 99% | 25.4<br><sub>28,25,22,26,26</sub> | 10.6<br><sub>16,6,6,17,6</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>11,9,5,11,5</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>5,5,1,2,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 23.4 |
| Noah Clowney | 99% | 23.9<br><sub>35,24,19,22,26</sub> | 8.9<br><sub>15,9,7,0,13</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>7,3,3,2,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>3,3,1,2,1</sub> |  | 1.4<br><sub>3,1,1,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.6 | 1.0 | 14.4 |
| Danny Wolf | 91% | 23.3<br><sub>28,11,23,26,25</sub> | 10.0<br><sub>14,3,6,20,11</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>6,2,6,5,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,1,2,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>4,1,1,4,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.6 | 1.2 | 17.9 |
| Moritz Wagner | 98% | 17.6<br><sub>18,10,20,22,14</sub> | 9.0<br><sub>10,4,11,3,11</sub> |  | 4.0<br><sub>6,5,2,5,0</sub> |  | 1.5<br><sub>4,1,3,2,1</sub> |  | 0.8<br><sub>2,0,2,1,2</sub> |  | 0.7 | 0.2 | 1.0 | 14.6 |
| Keon Ellis | 91% | 17.4<br><sub>7,20,6,8,16</sub> | 4.3<br><sub>0,8,3,0,6</sub> |  | 1.7<br><sub>0,2,1,1,0</sub> |  | 1.2<br><sub>1,0,0,1,0</sub> |  | 0.6<br><sub>0,2,1,0,2</sub> |  | 0.9 | 0.5 | 0.5 | 7.2 |
| Terance Mann | 64% | 13.3<br><sub>9,-,5,-,3</sub> | 3.2<br><sub>2,-,0,-,0</sub> |  | 1.6<br><sub>1,-,1,-,0</sub> |  | 1.3<br><sub>1,-,0,-,0</sub> |  | 0.3<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.1 |
| Grant Nelson | 84% | 9.3<br><sub>-,-,-,-,8</sub> | 2.9<br><sub>-,-,-,-,2</sub> |  | 2.2<br><sub>-,-,-,-,1</sub> |  | 0.9<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.7 | 0.6 | 6.0 |
| Josh Minott | 63% | 9.2<br><sub>2,-,4,-,2</sub> | 4.7<br><sub>0,-,0,-,0</sub> |  | 1.7<br><sub>0,-,0,-,0</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 6.9 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 99% | 29.5<br><sub>20,24,31,40,37</sub> | 20.1<br><sub>5,8,19,50,32</sub> | 21.5 · 22.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>5,2,4,11,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>3,4,3,7,8</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>0,0,4,7,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.3 | 2.3 | 29.3 |
| Kyle Kuzma | 99% | 24.4<br><sub>22,30,-,33,32</sub> | 13.2<br><sub>14,26,-,12,18</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,5,-,5,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,1,-,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>3,2,-,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.4 | 1.5 | 20.1 |
| Myles Turner | 99% | 23.1<br><sub>23,21,-,26,28</sub> | 10.1<br><sub>8,4,-,5,27</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>7,5,-,6,11</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>1,4,-,5,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>1,0,-,1,5</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 2.0 | 1.3 | 17.1 |
| Jaime Jaquez Jr. | 99% | 22.7<br><sub>30,23,22,25,25</sub> | 12.1<br><sub>6,10,9,9,3</sub> | 12.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>5,2,1,0,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.2<br><sub>4,5,2,1,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 1.5 | 19.2 |
| Brayden Burries | 99% | 21.8<br><sub>29,25,28,26,29</sub> | 10.9<br><sub>13,20,14,26,14</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>8,7,3,8,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>4,1,3,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1<br><sub>2,3,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 1.5 | 18.6 |
| Ryan Rollins | 99% | 21.2<br><sub>-,-,21,28,22</sub> | 10.9<br><sub>-,-,15,8,6</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>-,-,3,6,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>-,-,6,1,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>-,-,1,0,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.3 | 1.9 | 18.3 |
| Kel'el Ware | 98% | 16.7<br><sub>25,17,26,22,23</sub> | 7.6<br><sub>8,11,11,6,9</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>11,3,5,8,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>2,1,0,3,0</sub> |  | 0.5<br><sub>1,1,2,0,1</sub> |  | 0.6 | 1.1 | 1.2 | 13.6 |
| Nate Ament | 98% | 16.3<br><sub>17,17,35,14,25</sub> | 7.1<br><sub>5,7,18,2,7</sub> | 7.5 · 7.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>2,4,9,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.6<br><sub>1,0,2,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 10.5 |
| Cormac Ryan | 52% | 14.0<br><sub>-,-,-,-,-</sub> | 7.2<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 10.1 |
| Pete Nance | 96% | 11.7<br><sub>-,-,28,-,-</sub> | 4.1<br><sub>-,-,7,-,-</sub> |  | 1.9<br><sub>-,-,3,-,-</sub> |  | 1.0<br><sub>-,-,3,-,-</sub> |  | 0.4<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 7.0 |
| Kasparas Jakucionis | 91% | 11.6<br><sub>26,26,22,10,7</sub> | 5.2<br><sub>25,20,18,2,0</sub> |  | 1.6<br><sub>5,3,3,3,0</sub> |  | 2.2<br><sub>5,5,2,3,3</sub> |  | 0.6<br><sub>4,3,3,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 9.1 |
| AJ Green | 64% | 9.2<br><sub>6,14,-,12,-</sub> | 3.9<br><sub>0,11,-,9,-</sub> |  | 0.9<br><sub>0,0,-,0,-</sub> |  | 0.7<br><sub>0,1,-,0,-</sub> |  | 0.6<br><sub>0,3,-,3,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.6 |
| Caris LeVert | 63% | 8.4<br><sub>-,8,11,5,8</sub> | 3.5<br><sub>-,8,3,0,0</sub> |  | 1.3<br><sub>-,3,3,1,0</sub> |  | 1.2<br><sub>-,2,1,0,0</sub> |  | 0.2<br><sub>-,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 6.0 |
| Kam Jones | 52% | 8.3<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.2 |
| Gary Trent Jr. | 67% | 8.3<br><sub>30,16,7,-,5</sub> | 4.0<br><sub>18,1,0,-,0</sub> |  | 0.7<br><sub>2,1,1,-,0</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.5<br><sub>4,0,0,-,0</sub> |  | 0.3 | 0.0 | 0.3 | 5.2 |
| Jericho Sims | 58% | 8.0<br><sub>11,18,10,-,-</sub> | 2.1<br><sub>4,4,0,-,-</sub> |  | 2.1<br><sub>2,6,0,-,-</sub> |  | 0.7<br><sub>0,2,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Ousmane Dieng | 64% | 7.5<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Bogoljub Markovic | 43% | 5.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.2 |

</details>


### PHX @ HOU
Out: Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Miles Bridges PTS under 13.5 | PHX @ HOU | tab | 1.95 | 1.94 | 1.83 | 54.6% | 50.9% | 51.6% | +0.7% | +6.7% | 0.2% |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 100% | 35.6<br><sub>28,37,33,38,42</sub> | 24.5<br><sub>17,20,29,23,22</sub> | 23.5 · 23.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>4,4,2,2,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.8<br><sub>7,8,6,3,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,1,2,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 2.9 | 33.7 |
| Dillon Brooks | 100% | 30.1<br><sub>22,27,31,25,34</sub> | 15.6<br><sub>1,15,29,18,16</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>2,4,3,3,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>0,4,5,3,7</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,3,5,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 1.4 | 21.3 |
| Miles Bridges | 100% | 29.3<br><sub>24,29,29,25,35</sub> | 13.6<br><sub>14,16,13,18,14</sub> | 12.5 · 13.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>3,8,6,9,11</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.9<br><sub>3,2,5,4,5</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.5 | 1.0 | 22.6 |
| Jalen Green | 100% | 29.1<br><sub>21,27,30,25,37</sub> | 15.7<br><sub>9,16,18,14,25</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>2,5,7,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>1,3,7,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,2,4,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 2.3 | 22.3 |
| Oso Ighodaro | 100% | 25.9<br><sub>17,33,21,27,30</sub> | 6.6<br><sub>4,8,7,3,7</sub> | 5.5 · 5.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>2,11,4,7,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,3,2,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.3 | 15.3 |
| Collin Gillespie | 99% | 25.2<br><sub>28,26,17,27,30</sub> | 10.2<br><sub>26,10,9,16,18</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,3,3,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.4<br><sub>4,3,1,5,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>5,2,2,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.2 | 1.2 | 16.6 |
| Jordan Goodwin | 98% | 19.8<br><sub>31,20,17,28,18</sub> | 7.2<br><sub>14,11,2,5,6</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>7,6,5,9,2</sub> |  | 2.0<br><sub>6,2,3,4,2</sub> |  | 1.1<br><sub>1,1,0,1,2</sub> |  | 1.2 | 0.2 | 0.7 | 13.1 |
| Luke Kennard | 99% | 16.5<br><sub>23,17,17,15,14</sub> | 6.2<br><sub>18,12,3,5,4</sub> | 6.5 · 6.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>6,2,3,0,1</sub> |  | 1.4<br><sub>4,0,1,0,2</sub> |  | 0.8<br><sub>3,4,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.5 | 0.1 | 0.6 | 9.3 |
| Khaman Maluach | 98% | 16.1<br><sub>13,11,21,18,16</sub> | 5.7<br><sub>7,4,10,9,8</sub> | 5.5 · 5.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>4,6,2,6,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 0.9 | 11.1 |
| Ryan Dunn | 98% | 13.4<br><sub>24,12,13,9,9</sub> | 3.8<br><sub>3,5,6,0,3</sub> |  | 2.9<br><sub>6,1,5,5,2</sub> |  | 0.8<br><sub>1,0,2,0,0</sub> |  | 0.3<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.4 | 7.5 |
| Rasheer Fleming | 38% | 7.2<br><sub>-,-,4,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 1.2<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.1 |
| Jamaree Bouyea | 47% | 6.7<br><sub>-,-,4,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 1.1<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Koa Peat | 64% | 6.1<br><sub>8,1,4,3,-</sub> | 2.9<br><sub>10,0,2,0,-</sub> |  | 1.3<br><sub>2,1,0,0,-</sub> |  | 0.3<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.5 |
| Duop Reath | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.9 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 100% | 35.1<br><sub>30,29,32,35,33</sub> | 22.4<br><sub>25,22,21,16,32</sub> | 21.5 · 21.5<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>4,2,2,4,9</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.7<br><sub>5,3,3,4,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,2,4,0,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.9 | 3.0 | 32.7 |
| Alperen Sengun | 100% | 33.9<br><sub>28,30,14,36,31</sub> | 21.0<br><sub>19,23,7,28,20</sub> | 20.5 · 20.5<br><sub>o 49% · u 51%</sub> | 9.8<br><sub>8,7,7,11,8</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 6.6<br><sub>8,2,1,10,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>1,1,1,1,1</sub> |  | 1.1 | 1.0 | 2.9 | 37.4 |
| Amen Thompson | 100% | 33.9<br><sub>29,-,31,26,28</sub> | 16.7<br><sub>26,-,15,22,20</sub> | 14.5 · 15.5<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>7,-,9,6,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>7,-,3,0,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>3,-,0,0,1</sub> |  | 1.4 | 0.7 | 2.3 | 28.1 |
| Jabari Smith Jr. | 100% | 33.2<br><sub>28,32,26,32,28</sub> | 14.3<br><sub>9,12,17,21,13</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>6,10,4,4,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>5,1,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,1,3,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.7 | 0.8 | 1.3 | 22.7 |
| Fred VanVleet | 100% | 32.3<br><sub>-,26,27,33,31</sub> | 14.0<br><sub>-,8,15,25,6</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>-,5,2,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>-,6,6,9,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>-,2,3,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.4 | 1.5 | 22.5 |
| Tari Eason | 99% | 23.2<br><sub>30,27,25,23,22</sub> | 9.4<br><sub>25,7,11,7,10</sub> | 9.5 · 9.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>7,7,4,6,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>1,3,3,1,4</sub> |  | 1.0<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.6 | 1.2 | 16.3 |
| Marcus Smart | 67% | 20.8<br><sub>-,-,18,23,25</sub> | 6.6<br><sub>-,-,4,3,4</sub> | 5.5 · 5.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>-,-,2,2,3</sub> |  | 2.3<br><sub>-,-,4,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9<br><sub>-,-,1,1,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.1 | 0.4 | 1.4 | 11.2 |
| Reed Sheppard | 96% | 18.3<br><sub>26,19,25,14,17</sub> | 8.3<br><sub>11,5,20,0,5</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,2,4,2,3</sub> |  | 2.4<br><sub>6,2,2,0,5</sub> |  | 1.4<br><sub>3,1,6,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 0.9 | 12.4 |
| Steven Adams | 63% | 14.2<br><sub>12,-,16,12,16</sub> | 4.1<br><sub>6,-,4,2,4</sub> |  | 5.3<br><sub>7,-,5,2,6</sub> |  | 0.9<br><sub>1,-,2,2,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 10.3 |
| Bogdan Bogdanovic | 98% | 9.9<br><sub>22,26,11,5,9</sub> | 3.6<br><sub>12,6,1,0,2</sub> |  | 1.2<br><sub>3,0,3,1,1</sub> |  | 1.0<br><sub>4,1,0,0,2</sub> |  | 0.4<br><sub>2,2,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.8 |
| Clint Capela | 35% | 9.5<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 3.8<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.6 | 0.5 | 7.5 |
| Oscar Tshiebwe | 72% | 7.4<br><sub>12,6,11,-,-</sub> | 3.3<br><sub>4,6,4,-,-</sub> |  | 3.4<br><sub>9,6,4,-,-</sub> |  | 0.5<br><sub>3,0,3,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 7.1 |
| Isaiah Crawford | 52% | 6.3<br><sub>9,21,2,-,-</sub> | 2.2<br><sub>4,11,0,-,-</sub> |  | 1.3<br><sub>2,10,0,-,-</sub> |  | 0.3<br><sub>0,3,0,-,-</sub> |  | 0.1<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Jae'Sean Tate | 52% | 5.8<br><sub>8,12,1,-,-</sub> | 1.8<br><sub>4,3,0,-,-</sub> |  | 1.3<br><sub>2,3,0,-,-</sub> |  | 0.4<br><sub>0,2,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.5 |
| Bruce Thornton | 63% | 5.6<br><sub>6,12,1,-,-</sub> | 2.4<br><sub>2,7,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.1 |

</details>


### SAC @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Zach LaVine (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.9–114.2 | SAC 28% | 3.62 / 1.38 | GSW -8.5 | 219.5 | GSW -8.5 covers 49%; o215.5 59% |
| Expected (weighted by chance each plays) | 105.8–116.1 | SAC 23% | 4.31 / 1.30 | GSW -10.5 | 221.5 | GSW -8.5 covers 55%; o215.5 63% |
| if Yaxel Lendeborg plays | 105.5–115.9 | SAC 23% | 4.43 / 1.29 | GSW -10.5 | 221.5 | GSW -8.5 covers 55%; o215.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | Questionable | 55% | 32.5 | 20.6 | 7.2 | 4.2 | 1.8 | 1.0 | 0.8 | 3.0 | 32.0 | full tables below |
| Brandon Williams (GSW) | Questionable | 55% | 17.9 | 12.0 | 2.3 | 3.1 | 0.6 | 0.8 | 0.3 | 1.5 | 17.5 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 37.3<br><sub>33,35,36,40,33</sub> | 24.3<br><sub>26,36,18,21,12</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>0,4,1,6,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 7.9<br><sub>6,6,12,8,4</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,6,2,2,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 4.0 | 35.7 |
| De'Andre Hunter | 88% | 36.4<br><sub>-,35,37,41,38</sub> | 17.1<br><sub>-,7,30,20,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>-,1,6,6,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>-,4,2,2,8</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.2<br><sub>-,1,5,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.2 | 2.0 | 24.6 |
| Keegan Murray | 98% | 35.4<br><sub>21,31,40,40,39</sub> | 14.1<br><sub>6,12,13,15,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>1,7,7,12,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,3,4,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.9 | 1.4 | 21.5 |
| Domantas Sabonis | 99% | 33.1<br><sub>29,24,38,32,30</sub> | 16.0<br><sub>11,8,19,15,20</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 12.5<br><sub>13,13,16,17,12</sub> | 13.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>3,8,1,4,8</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.8 | 0.3 | 3.0 | 34.2 |
| Precious Achiuwa | 98% | 20.0<br><sub>-,8,-,22,10</sub> | 8.5<br><sub>-,0,-,5,9</sub> |  | 5.2<br><sub>-,0,-,7,3</sub> |  | 1.1<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.8 | 0.7 | 1.0 | 14.8 |
| Malik Monk | 98% | 19.1<br><sub>29,20,12,10,16</sub> | 10.1<br><sub>14,8,2,3,15</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,0,0,3</sub> |  | 3.7<br><sub>10,2,3,1,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,2,0,0,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.3 | 1.7 | 15.6 |
| Leaky Black | 91% | 16.9<br><sub>29,17,19,4,13</sub> | 3.9<br><sub>12,3,0,2,3</sub> |  | 2.7<br><sub>9,0,3,0,3</sub> |  | 1.2<br><sub>2,2,1,0,3</sub> |  | 0.5<br><sub>4,1,0,0,1</sub> |  | 0.9 | 0.4 | 0.5 | 7.8 |
| Emanuel Sharp | 98% | 16.5<br><sub>21,14,10,16,13</sub> | 5.4<br><sub>9,6,3,3,0</sub> |  | 1.2<br><sub>0,2,0,0,1</sub> |  | 0.9<br><sub>2,1,1,0,2</sub> |  | 0.8<br><sub>1,1,1,1,0</sub> |  | 0.7 | 0.2 | 0.6 | 7.5 |
| Dylan Cardwell | 98% | 14.8<br><sub>19,12,10,6,11</sub> | 4.3<br><sub>10,6,0,0,0</sub> |  | 5.4<br><sub>6,4,4,1,7</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 0.8 | 10.8 |
| Daeqwon Plowden | 64% | 11.8<br><sub>24,4,-,-,1</sub> | 4.6<br><sub>13,3,-,-,1</sub> |  | 1.2<br><sub>2,0,-,-,0</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 0.6<br><sub>3,1,-,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.5 |
| Alex Karaban | 52% | 11.0<br><sub>29,4,-,-,1</sub> | 2.0<br><sub>0,0,-,-,0</sub> |  | 1.8<br><sub>5,1,-,-,0</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.2<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.2 |
| Gabe Vincent | 96% | 10.9<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.5 |
| Sean Pedulla | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Mason Plumlee | 38% | 7.9<br><sub>5,4,-,-,-</sub> | 1.9<br><sub>2,0,-,-,-</sub> |  | 2.5<br><sub>0,2,-,-,-</sub> |  | 0.7<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 5.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 98% | 34.0<br><sub>22,30,29,32,38</sub> | 20.4<br><sub>8,15,10,15,18</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>0,3,4,2,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 2.2 | 30.8 |
| Draymond Green | 97% | 27.8<br><sub>16,25,23,-,27</sub> | 7.0<br><sub>4,2,3,-,9</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>3,5,2,-,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.8<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.7 | 2.6 | 18.6 |
| De'Anthony Melton | 99% | 27.0<br><sub>18,21,19,25,27</sub> | 14.2<br><sub>8,8,0,9,2</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,2,2,1,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>3,1,2,5,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.6 | 0.4 | 2.0 | 22.3 |
| Will Richard | 99% | 25.5<br><sub>30,23,27,27,17</sub> | 10.2<br><sub>7,11,20,15,3</sub> |  | 3.0<br><sub>4,3,0,5,2</sub> |  | 1.9<br><sub>1,1,3,0,2</sub> |  | 1.2<br><sub>1,2,1,1,1</sub> |  | 1.3 | 0.2 | 1.1 | 15.1 |
| Gui Santos | 96% | 24.4<br><sub>21,19,17,23,23</sub> | 11.7<br><sub>7,12,6,8,13</sub> |  | 4.9<br><sub>4,7,6,3,5</sub> |  | 3.3<br><sub>1,2,6,0,3</sub> |  | 1.1<br><sub>1,1,0,0,3</sub> |  | 0.9 | 0.4 | 1.8 | 19.8 |
| Charles Bassey | 98% | 24.2<br><sub>20,16,22,25,26</sub> | 12.8<br><sub>11,4,10,16,13</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 9.5<br><sub>5,0,8,13,9</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.5 | 1.4 | 23.8 |
| Georges Niang | 98% | 21.0<br><sub>15,14,14,15,8</sub> | 9.8<br><sub>5,0,11,5,0</sub> |  | 3.0<br><sub>3,4,1,2,1</sub> |  | 1.6<br><sub>2,2,1,0,0</sub> |  | 1.5<br><sub>1,0,2,1,0</sub> |  | 0.4 | 0.2 | 1.1 | 14.4 |
| Al Horford | 98% | 20.3<br><sub>10,14,-,17,18</sub> | 7.8<br><sub>0,0,-,3,7</sub> |  | 4.5<br><sub>3,5,-,2,3</sub> |  | 2.4<br><sub>1,0,-,2,2</sub> |  | 1.1<br><sub>0,0,-,0,1</sub> |  | 0.6 | 1.0 | 0.7 | 14.7 |
| Gary Payton II | 91% | 18.4<br><sub>13,8,16,24,13</sub> | 8.6<br><sub>2,2,8,2,8</sub> |  | 3.3<br><sub>2,0,8,1,1</sub> |  | 1.5<br><sub>0,0,2,1,0</sub> |  | 0.6<br><sub>0,0,2,0,0</sub> |  | 1.2 | 0.2 | 0.8 | 13.5 |
| LJ Cryer | 88% | 17.3<br><sub>24,24,19,12,11</sub> | 9.1<br><sub>20,7,9,9,3</sub> |  | 1.4<br><sub>2,1,0,0,0</sub> |  | 2.1<br><sub>6,3,2,1,2</sub> |  | 1.6<br><sub>6,1,3,1,1</sub> |  | 0.4 | 0.1 | 0.8 | 12.7 |
| Graham Ike | 72% | 13.4<br><sub>13,8,15,4,-</sub> | 6.2<br><sub>5,3,2,5,-</sub> |  | 3.1<br><sub>2,5,2,0,-</sub> |  | 1.6<br><sub>3,1,2,0,-</sub> |  | 0.4<br><sub>1,0,0,0,-</sub> |  | 0.5 | 0.6 | 0.8 | 10.9 |
| Malevy Leons | 64% | 11.5<br><sub>14,6,7,4,-</sub> | 3.5<br><sub>5,2,2,0,-</sub> |  | 2.2<br><sub>1,1,1,2,-</sub> |  | 0.8<br><sub>0,0,0,1,-</sub> |  | 0.1<br><sub>1,0,0,0,-</sub> |  | 0.5 | 0.4 | 0.6 | 6.5 |

</details>

<details><summary>if Yaxel Lendeborg plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 98% | 33.6<br><sub>22,30,29,32,38</sub> | 18.8<br><sub>8,15,10,15,18</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>0,3,4,2,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 1.9 | 28.6 |
| Yaxel Lendeborg (GSW) | 100% | 32.5<br><sub>24,33,30,33,34</sub> | 20.6<br><sub>3,28,13,11,12</sub> | 21.5 · – | 7.2<br><sub>7,8,5,8,8</sub> | 7.5 | 4.2<br><sub>1,3,4,7,3</sub> | 3.5 | 1.8<br><sub>0,2,0,1,1</sub> | 1.5 | 1.0 | 0.8 | 3.0 | 32.0 |
| Draymond Green (GSW) | 97% | 26.4<br><sub>16,25,23,-,27</sub> | 6.5<br><sub>4,2,3,-,9</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.2<br><sub>3,5,2,-,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.8<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.7 | 2.3 | 17.7 |
| De'Anthony Melton (GSW) | 99% | 24.7<br><sub>18,21,19,25,27</sub> | 11.5<br><sub>8,8,0,9,2</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,2,2,1,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>3,1,2,5,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.4 | 1.8 | 18.6 |
| Will Richard (GSW) | 99% | 21.5<br><sub>30,23,27,27,17</sub> | 8.1<br><sub>7,11,20,15,3</sub> |  | 2.5<br><sub>4,3,0,5,2</sub> |  | 1.5<br><sub>1,1,3,0,2</sub> |  | 1.0<br><sub>1,2,1,1,1</sub> |  | 1.1 | 0.2 | 0.9 | 12.1 |
| Charles Bassey (GSW) | 98% | 20.1<br><sub>20,16,22,25,26</sub> | 10.3<br><sub>11,4,10,16,13</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.9<br><sub>5,0,8,13,9</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.3 | 1.2 | 19.2 |
| Gui Santos (GSW) | 96% | 19.9<br><sub>21,19,17,23,23</sub> | 9.2<br><sub>7,12,6,8,13</sub> |  | 4.0<br><sub>4,7,6,3,5</sub> |  | 2.3<br><sub>1,2,6,0,3</sub> |  | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.7 | 0.3 | 1.3 | 15.5 |
| Al Horford (GSW) | 98% | 17.7<br><sub>10,14,-,17,18</sub> | 6.3<br><sub>0,0,-,3,7</sub> |  | 3.8<br><sub>3,5,-,2,3</sub> |  | 1.9<br><sub>1,0,-,2,2</sub> |  | 0.9<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.8 | 0.6 | 12.1 |
| Gary Payton II (GSW) | 91% | 16.1<br><sub>13,8,16,24,13</sub> | 7.6<br><sub>2,2,8,2,8</sub> |  | 2.8<br><sub>2,0,8,1,1</sub> |  | 1.3<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>0,0,2,0,0</sub> |  | 1.0 | 0.2 | 0.7 | 11.7 |
| Georges Niang (GSW) | 98% | 16.0<br><sub>15,14,14,15,8</sub> | 7.3<br><sub>5,0,11,5,0</sub> |  | 2.3<br><sub>3,4,1,2,1</sub> |  | 1.1<br><sub>2,2,1,0,0</sub> |  | 1.1<br><sub>1,0,2,1,0</sub> |  | 0.3 | 0.1 | 0.8 | 10.8 |
| LJ Cryer (GSW) | 88% | 14.3<br><sub>24,24,19,12,11</sub> | 7.1<br><sub>20,7,9,9,3</sub> |  | 1.1<br><sub>2,1,0,0,0</sub> |  | 1.8<br><sub>6,3,2,1,2</sub> |  | 1.2<br><sub>6,1,3,1,1</sub> |  | 0.3 | 0.1 | 0.6 | 10.0 |
| Graham Ike (GSW) | 72% | 8.9<br><sub>13,8,15,4,-</sub> | 4.1<br><sub>5,3,2,5,-</sub> |  | 2.1<br><sub>2,5,2,0,-</sub> |  | 1.0<br><sub>3,1,2,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.4 | 0.5 | 7.2 |
| Malevy Leons (GSW) | 64% | 7.6<br><sub>14,6,7,4,-</sub> | 2.3<br><sub>5,2,2,0,-</sub> |  | 1.4<br><sub>1,1,1,2,-</sub> |  | 0.5<br><sub>0,0,0,1,-</sub> |  | 0.1<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.1 |
| Darius Acuff Jr. (SAC) | 98% | 37.3<br><sub>33,35,36,40,33</sub> | 24.3<br><sub>26,36,18,21,12</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>0,4,1,6,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 7.9<br><sub>6,6,12,8,4</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,6,2,2,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 4.0 | 35.7 |
| De'Andre Hunter (SAC) | 88% | 36.4<br><sub>-,35,37,41,38</sub> | 17.1<br><sub>-,7,30,20,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>-,1,6,6,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>-,4,2,2,8</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.2<br><sub>-,1,5,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.2 | 2.0 | 24.6 |
| Keegan Murray (SAC) | 98% | 35.5<br><sub>21,31,40,40,39</sub> | 14.1<br><sub>6,12,13,15,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>1,7,7,12,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,3,4,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.9 | 1.4 | 21.6 |
| Domantas Sabonis (SAC) | 99% | 33.1<br><sub>29,24,38,32,30</sub> | 15.8<br><sub>11,8,19,15,20</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 12.4<br><sub>13,13,16,17,12</sub> | 13.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>3,8,1,4,8</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.8 | 0.3 | 3.0 | 33.9 |
| Precious Achiuwa (SAC) | 98% | 20.1<br><sub>-,8,-,22,10</sub> | 8.5<br><sub>-,0,-,5,9</sub> |  | 5.2<br><sub>-,0,-,7,3</sub> |  | 1.1<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.8 | 0.7 | 1.0 | 14.8 |
| Malik Monk (SAC) | 98% | 19.2<br><sub>29,20,12,10,16</sub> | 10.1<br><sub>14,8,2,3,15</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,0,0,3</sub> |  | 3.7<br><sub>10,2,3,1,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,2,0,0,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.3 | 1.7 | 15.6 |
| Leaky Black (SAC) | 91% | 16.9<br><sub>29,17,19,4,13</sub> | 3.9<br><sub>12,3,0,2,3</sub> |  | 2.7<br><sub>9,0,3,0,3</sub> |  | 1.2<br><sub>2,2,1,0,3</sub> |  | 0.5<br><sub>4,1,0,0,1</sub> |  | 0.9 | 0.4 | 0.5 | 7.9 |
| Emanuel Sharp (SAC) | 98% | 16.4<br><sub>21,14,10,16,13</sub> | 5.4<br><sub>9,6,3,3,0</sub> |  | 1.2<br><sub>0,2,0,0,1</sub> |  | 0.9<br><sub>2,1,1,0,2</sub> |  | 0.8<br><sub>1,1,1,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.5 |
| Dylan Cardwell (SAC) | 98% | 14.8<br><sub>19,12,10,6,11</sub> | 4.2<br><sub>10,6,0,0,0</sub> |  | 5.3<br><sub>6,4,4,1,7</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 0.8 | 10.7 |
| Daeqwon Plowden (SAC) | 64% | 11.7<br><sub>24,4,-,-,1</sub> | 4.5<br><sub>13,3,-,-,1</sub> |  | 1.3<br><sub>2,0,-,-,0</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 0.6<br><sub>3,1,-,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.4 |
| Alex Karaban (SAC) | 52% | 11.0<br><sub>29,4,-,-,1</sub> | 2.0<br><sub>0,0,-,-,0</sub> |  | 1.7<br><sub>5,1,-,-,0</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.2 |
| Gabe Vincent (SAC) | 96% | 10.9<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.6 |
| Sean Pedulla (SAC) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Mason Plumlee (SAC) | 38% | 7.9<br><sub>5,4,-,-,-</sub> | 2.0<br><sub>2,0,-,-,-</sub> |  | 2.5<br><sub>0,2,-,-,-</sub> |  | 0.7<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 5.2 |

</details>


### SAS @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), Dylan Harper (SAS), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.0–113.2 | SAS 43% | 2.30 / 1.77 | POR -2.5 | 223.5 | POR +3.5 covers 65%; o227.5 43% |
| Expected (weighted by chance each plays) | 112.9–111.6 | SAS 54% | 1.85 / 2.17 | POR +1.5 | 224.5 | POR +3.5 covers 56%; o227.5 44% |
| if De'Aaron Fox plays | 111.9–111.9 | SAS 50% | 1.98 / 2.02 | POR +0.5 | 223.5 | POR +3.5 covers 59%; o227.5 42% |
| if Victor Wembanyama plays | 113.0–111.4 | SAS 55% | 1.81 / 2.23 | POR +2.5 | 224.5 | POR +3.5 covers 55%; o227.5 43% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 31.7 | 16.5 | 3.9 | 5.8 | 1.3 | 1.4 | 0.4 | 2.9 | 26.2 | full tables below |
| Victor Wembanyama (SAS) | Questionable | 55% | 32.6 | 30.6 | 12.0 | 3.9 | 2.2 | 1.4 | 3.7 | 3.0 | 46.5 | full tables below |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephon Castle | 99% | 33.8<br><sub>35,31,33,29,37</sub> | 22.0<br><sub>20,10,21,19,28</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 7.4<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 3.9 | 34.9 |
| Devin Vassell | 99% | 33.5<br><sub>32,36,32,26,34</sub> | 17.2<br><sub>6,12,15,10,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>6,5,4,3,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.3<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.5 | 1.5 | 25.1 |
| Julian Champagnie | 99% | 31.4<br><sub>24,30,29,25,30</sub> | 13.8<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,6,4,3,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>1,0,1,3,3</sub> |  | 2.4<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.6 | 1.2 | 21.2 |
| Keldon Johnson | 99% | 28.6<br><sub>29,15,27,23,26</sub> | 15.2<br><sub>11,4,10,10,12</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>10,2,5,4,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>2,1,3,4,5</sub> |  | 1.1<br><sub>1,0,0,2,0</sub> |  | 1.0 | 0.2 | 1.5 | 24.4 |
| Harrison Barnes | 96% | 26.8<br><sub>14,10,16,21,26</sub> | 10.6<br><sub>0,0,9,3,9</sub> |  | 3.1<br><sub>0,3,2,5,2</sub> |  | 1.6<br><sub>2,4,1,2,2</sub> |  | 1.5<br><sub>0,0,1,0,1</sub> |  | 0.7 | 0.2 | 1.0 | 15.4 |
| Luke Kornet | 99% | 22.9<br><sub>13,14,15,10,29</sub> | 7.1<br><sub>2,2,4,0,18</sub> |  | 6.6<br><sub>2,1,0,3,11</sub> |  | 2.1<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.0 | 0.7 | 15.8 |
| Jordan McLaughlin | 83% | 21.4<br><sub>19,-,11,18,14</sub> | 7.2<br><sub>10,-,0,0,6</sub> |  | 3.0<br><sub>1,-,1,3,2</sub> |  | 3.1<br><sub>2,-,5,2,0</sub> |  | 0.8<br><sub>2,-,0,0,0</sub> |  | 1.4 | 0.1 | 1.1 | 13.4 |
| Carter Bryant | 96% | 19.8<br><sub>5,2,13,20,12</sub> | 7.5<br><sub>0,0,3,8,0</sub> |  | 3.2<br><sub>1,0,1,3,3</sub> |  | 1.2<br><sub>0,0,0,0,2</sub> |  | 1.1<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.4 | 0.9 | 11.9 |
| Ja'Kobi Gillespie | 91% | 17.1<br><sub>-,-,-,-,15</sub> | 6.0<br><sub>-,-,-,-,3</sub> |  | 2.1<br><sub>-,-,-,-,2</sub> |  | 2.0<br><sub>-,-,-,-,4</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.2 | 0.5 | 10.1 |
| Tarris Reed Jr. | 63% | 14.5<br><sub>-,-,-,6,15</sub> | 5.3<br><sub>-,-,-,0,7</sub> |  | 5.9<br><sub>-,-,-,4,7</sub> |  | 0.8<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.6 | 1.1 | 11.9 |
| Maliq Brown | 88% | 10.8<br><sub>-,-,-,-,1</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 2.2 |
| David Jones Garcia | 64% | 10.2<br><sub>-,-,-,4,2</sub> | 4.2<br><sub>-,-,-,0,2</sub> |  | 1.7<br><sub>-,-,-,1,0</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.6 | 7.1 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 72% | 34.3<br><sub>30,-,-,36,30</sub> | 23.9<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.2 | 36.8 |
| Damian Lillard | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.3<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.1 | 28.7 |
| Toumani Camara | 99% | 32.8<br><sub>26,33,37,35,29</sub> | 11.9<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.5 | 1.1 | 18.4 |
| Jrue Holiday | 99% | 29.7<br><sub>25,31,31,31,28</sub> | 14.7<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 2.1 | 23.7 |
| Donovan Clingan | 99% | 28.7<br><sub>22,32,26,31,29</sub> | 12.6<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 11.9<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.6 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson | 99% | 25.3<br><sub>23,21,35,23,26</sub> | 12.0<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.9 | 16.8 |
| Sidy Cissoko | 98% | 24.8<br><sub>28,32,31,23,24</sub> | 7.3<br><sub>5,6,13,11,5</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,1,3,1,0</sub> |  | 1.0<br><sub>1,2,1,3,1</sub> |  | 0.8 | 0.3 | 0.9 | 12.4 |
| Robert Williams III | 98% | 17.0<br><sub>15,16,-,17,16</sub> | 6.4<br><sub>2,6,-,4,6</sub> |  | 6.5<br><sub>5,8,-,3,6</sub> |  | 1.1<br><sub>2,4,-,0,1</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 14.0 |
| Jayson Kent | 88% | 12.2<br><sub>11,27,17,3,14</sub> | 4.1<br><sub>8,8,2,0,9</sub> |  | 1.5<br><sub>0,3,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>2,2,0,0,3</sub> |  | 0.5 | 0.1 | 0.5 | 6.1 |
| Branden Carlson | 91% | 8.7<br><sub>14,14,10,9,6</sub> | 2.5<br><sub>5,6,0,2,0</sub> |  | 2.2<br><sub>6,1,1,1,3</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Yang Hansen | 58% | 7.2<br><sub>7,-,12,-,3</sub> | 2.8<br><sub>0,-,2,-,2</sub> |  | 1.8<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>3,-,1,-,1</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.1 |
| Micah Potter | 58% | 7.1<br><sub>7,1,-,-,3</sub> | 3.2<br><sub>2,0,-,-,0</sub> |  | 2.0<br><sub>4,0,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.6 |
| John Tonje | 52% | 6.7<br><sub>7,-,6,-,3</sub> | 2.7<br><sub>7,-,0,-,2</sub> |  | 1.7<br><sub>4,-,3,-,0</sub> |  | 0.7<br><sub>3,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 5.1 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija (POR) | 72% | 34.3<br><sub>30,-,-,36,30</sub> | 23.8<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.3<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.2 | 36.7 |
| Damian Lillard (POR) | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.2<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.2 | 28.6 |
| Toumani Camara (POR) | 99% | 32.8<br><sub>26,33,37,35,29</sub> | 11.8<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.5 | 1.1 | 18.3 |
| Jrue Holiday (POR) | 99% | 29.8<br><sub>25,31,31,31,28</sub> | 14.6<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 2.1 | 23.6 |
| Donovan Clingan (POR) | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.5<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 12.0<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.7 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson (POR) | 99% | 25.4<br><sub>23,21,35,23,26</sub> | 12.0<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.9 | 16.9 |
| Sidy Cissoko (POR) | 98% | 25.0<br><sub>28,32,31,23,24</sub> | 7.3<br><sub>5,6,13,11,5</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,1,3,1,0</sub> |  | 1.0<br><sub>1,2,1,3,1</sub> |  | 0.8 | 0.3 | 0.9 | 12.5 |
| Robert Williams III (POR) | 98% | 17.0<br><sub>15,16,-,17,16</sub> | 6.3<br><sub>2,6,-,4,6</sub> |  | 6.5<br><sub>5,8,-,3,6</sub> |  | 1.1<br><sub>2,4,-,0,1</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 13.9 |
| Jayson Kent (POR) | 88% | 12.1<br><sub>11,27,17,3,14</sub> | 4.0<br><sub>8,8,2,0,9</sub> |  | 1.4<br><sub>0,3,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>2,2,0,0,3</sub> |  | 0.5 | 0.1 | 0.5 | 6.0 |
| Branden Carlson (POR) | 91% | 8.7<br><sub>14,14,10,9,6</sub> | 2.5<br><sub>5,6,0,2,0</sub> |  | 2.2<br><sub>6,1,1,1,3</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Yang Hansen (POR) | 58% | 7.2<br><sub>7,-,12,-,3</sub> | 2.8<br><sub>0,-,2,-,2</sub> |  | 1.8<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>3,-,1,-,1</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.1 |
| Micah Potter (POR) | 58% | 7.0<br><sub>7,1,-,-,3</sub> | 3.1<br><sub>2,0,-,-,0</sub> |  | 2.0<br><sub>4,0,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| John Tonje (POR) | 52% | 6.8<br><sub>7,-,6,-,3</sub> | 2.7<br><sub>7,-,0,-,2</sub> |  | 1.7<br><sub>4,-,3,-,0</sub> |  | 0.7<br><sub>3,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 5.1 |
| Stephon Castle (SAS) | 99% | 33.0<br><sub>35,31,33,29,37</sub> | 20.7<br><sub>20,10,21,19,28</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 6.5<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 3.4 | 32.6 |
| Devin Vassell (SAS) | 99% | 32.7<br><sub>32,36,32,26,34</sub> | 15.4<br><sub>6,12,15,10,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>6,5,4,3,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.5 | 1.2 | 22.8 |
| De'Aaron Fox (SAS) | 100% | 31.7<br><sub>-,34,32,26,-</sub> | 16.5<br><sub>-,6,10,5,-</sub> | 14.5 · – | 3.9<br><sub>-,2,2,2,-</sub> | 3.5 | 5.8<br><sub>-,2,5,10,-</sub> | 5.5 | 1.3<br><sub>-,0,0,0,-</sub> | 1.5 | 1.4 | 0.4 | 2.9 | 26.2 |
| Julian Champagnie (SAS) | 99% | 30.3<br><sub>24,30,29,25,30</sub> | 12.9<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>5,6,4,3,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,0,1,3,3</sub> |  | 2.2<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.6 | 0.9 | 19.9 |
| Keldon Johnson (SAS) | 99% | 27.0<br><sub>29,15,27,23,26</sub> | 13.2<br><sub>11,4,10,10,12</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>10,2,5,4,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>2,1,3,4,5</sub> |  | 1.0<br><sub>1,0,0,2,0</sub> |  | 0.9 | 0.2 | 1.3 | 21.5 |
| Harrison Barnes (SAS) | 96% | 23.6<br><sub>14,10,16,21,26</sub> | 8.9<br><sub>0,0,9,3,9</sub> |  | 2.8<br><sub>0,3,2,5,2</sub> |  | 1.4<br><sub>2,4,1,2,2</sub> |  | 1.2<br><sub>0,0,1,0,1</sub> |  | 0.6 | 0.2 | 0.7 | 13.1 |
| Luke Kornet (SAS) | 99% | 20.7<br><sub>13,14,15,10,29</sub> | 6.3<br><sub>2,2,4,0,18</sub> |  | 6.0<br><sub>2,1,0,3,11</sub> |  | 1.7<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.0 | 0.6 | 14.0 |
| Jordan McLaughlin (SAS) | 83% | 16.5<br><sub>19,-,11,18,14</sub> | 5.0<br><sub>10,-,0,0,6</sub> |  | 2.3<br><sub>1,-,1,3,2</sub> |  | 2.2<br><sub>2,-,5,2,0</sub> |  | 0.5<br><sub>2,-,0,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 9.5 |
| Carter Bryant (SAS) | 96% | 16.3<br><sub>5,2,13,20,12</sub> | 6.0<br><sub>0,0,3,8,0</sub> |  | 2.6<br><sub>1,0,1,3,3</sub> |  | 1.0<br><sub>0,0,0,0,2</sub> |  | 0.8<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.4 | 0.7 | 9.6 |
| Ja'Kobi Gillespie (SAS) | 91% | 13.9<br><sub>-,-,-,-,15</sub> | 4.9<br><sub>-,-,-,-,3</sub> |  | 1.7<br><sub>-,-,-,-,2</sub> |  | 1.4<br><sub>-,-,-,-,4</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.1 | 0.4 | 8.0 |
| Tarris Reed Jr. (SAS) | 63% | 12.1<br><sub>-,-,-,6,15</sub> | 4.4<br><sub>-,-,-,0,7</sub> |  | 4.9<br><sub>-,-,-,4,7</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.6 | 0.9 | 9.9 |
| David Jones Garcia (SAS) | 64% | 8.2<br><sub>-,-,-,4,2</sub> | 3.2<br><sub>-,-,-,0,2</sub> |  | 1.3<br><sub>-,-,-,1,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.1 | 0.5 | 5.5 |
| Maliq Brown (SAS) | 88% | 8.1<br><sub>-,-,-,-,1</sub> | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 1.8 |

</details>

<details><summary>if Victor Wembanyama plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija (POR) | 72% | 34.4<br><sub>30,-,-,36,30</sub> | 23.8<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.2 | 36.8 |
| Damian Lillard (POR) | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.1<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.1 | 28.6 |
| Toumani Camara (POR) | 99% | 32.7<br><sub>26,33,37,35,29</sub> | 11.8<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.5 | 1.1 | 18.3 |
| Jrue Holiday (POR) | 99% | 29.6<br><sub>25,31,31,31,28</sub> | 14.5<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 2.1 | 23.4 |
| Donovan Clingan (POR) | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.5<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 12.0<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.7 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson (POR) | 99% | 25.3<br><sub>23,21,35,23,26</sub> | 11.9<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.9 | 16.7 |
| Sidy Cissoko (POR) | 98% | 24.9<br><sub>28,32,31,23,24</sub> | 7.4<br><sub>5,6,13,11,5</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.7<br><sub>3,1,3,1,0</sub> |  | 1.0<br><sub>1,2,1,3,1</sub> |  | 0.8 | 0.3 | 0.9 | 12.5 |
| Robert Williams III (POR) | 98% | 17.0<br><sub>15,16,-,17,16</sub> | 6.3<br><sub>2,6,-,4,6</sub> |  | 6.5<br><sub>5,8,-,3,6</sub> |  | 1.1<br><sub>2,4,-,0,1</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 13.9 |
| Jayson Kent (POR) | 88% | 12.1<br><sub>11,27,17,3,14</sub> | 4.0<br><sub>8,8,2,0,9</sub> |  | 1.4<br><sub>0,3,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>2,2,0,0,3</sub> |  | 0.5 | 0.1 | 0.5 | 6.0 |
| Branden Carlson (POR) | 91% | 8.8<br><sub>14,14,10,9,6</sub> | 2.5<br><sub>5,6,0,2,0</sub> |  | 2.2<br><sub>6,1,1,1,3</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Yang Hansen (POR) | 58% | 7.2<br><sub>7,-,12,-,3</sub> | 2.8<br><sub>0,-,2,-,2</sub> |  | 1.8<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>3,-,1,-,1</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.0 |
| Micah Potter (POR) | 58% | 7.1<br><sub>7,1,-,-,3</sub> | 3.1<br><sub>2,0,-,-,0</sub> |  | 2.0<br><sub>4,0,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| John Tonje (POR) | 52% | 6.8<br><sub>7,-,6,-,3</sub> | 2.7<br><sub>7,-,0,-,2</sub> |  | 1.7<br><sub>4,-,3,-,0</sub> |  | 0.7<br><sub>3,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 5.1 |
| Stephon Castle (SAS) | 99% | 33.3<br><sub>35,31,33,29,37</sub> | 19.2<br><sub>20,10,21,19,28</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 6.8<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 3.3 | 31.3 |
| Devin Vassell (SAS) | 99% | 33.1<br><sub>32,36,32,26,34</sub> | 13.8<br><sub>6,12,15,10,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>6,5,4,3,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.5 | 1.1 | 21.2 |
| Victor Wembanyama (SAS) | 100% | 32.6<br><sub>35,34,33,32,-</sub> | 30.6<br><sub>26,25,32,50,-</sub> | 29.5 · – | 12.0<br><sub>10,18,11,19,-</sub> | 12.5 | 3.9<br><sub>6,4,3,1,-</sub> | 3.5 | 2.2<br><sub>4,1,2,5,-</sub> | 2.5 | 1.4 | 3.7 | 3.0 | 46.5 |
| Julian Champagnie (SAS) | 99% | 29.4<br><sub>24,30,29,25,30</sub> | 11.3<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>5,6,4,3,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,0,1,3,3</sub> |  | 2.0<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.6 | 0.8 | 17.9 |
| Keldon Johnson (SAS) | 99% | 25.7<br><sub>29,15,27,23,26</sub> | 11.1<br><sub>11,4,10,10,12</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>10,2,5,4,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>2,1,3,4,5</sub> |  | 0.8<br><sub>1,0,0,2,0</sub> |  | 0.8 | 0.2 | 1.1 | 18.9 |
| Harrison Barnes (SAS) | 96% | 21.1<br><sub>14,10,16,21,26</sub> | 7.2<br><sub>0,0,9,3,9</sub> |  | 2.4<br><sub>0,3,2,5,2</sub> |  | 1.2<br><sub>2,4,1,2,2</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> |  | 0.4 | 0.2 | 0.7 | 10.8 |
| Luke Kornet (SAS) | 99% | 20.6<br><sub>13,14,15,10,29</sub> | 5.7<br><sub>2,2,4,0,18</sub> |  | 5.8<br><sub>2,1,0,3,11</sub> |  | 1.7<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.9 | 0.7 | 13.2 |
| Jordan McLaughlin (SAS) | 83% | 16.8<br><sub>19,-,11,18,14</sub> | 4.7<br><sub>10,-,0,0,6</sub> |  | 2.3<br><sub>1,-,1,3,2</sub> |  | 2.4<br><sub>2,-,5,2,0</sub> |  | 0.5<br><sub>2,-,0,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 9.4 |
| Carter Bryant (SAS) | 96% | 14.1<br><sub>5,2,13,20,12</sub> | 4.6<br><sub>0,0,3,8,0</sub> |  | 2.2<br><sub>1,0,1,3,3</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 0.6<br><sub>0,0,1,2,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.7 |
| Ja'Kobi Gillespie (SAS) | 91% | 14.1<br><sub>-,-,-,-,15</sub> | 4.3<br><sub>-,-,-,-,3</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.1 | 0.4 | 7.6 |
| Tarris Reed Jr. (SAS) | 63% | 11.7<br><sub>-,-,-,6,15</sub> | 3.9<br><sub>-,-,-,0,7</sub> |  | 4.7<br><sub>-,-,-,4,7</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.5 | 0.9 | 9.2 |
| Maliq Brown (SAS) | 88% | 7.7<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 1.9 |
| David Jones Garcia (SAS) | 64% | 7.4<br><sub>-,-,-,4,2</sub> | 2.7<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-25/`._
