# NBA model · Wed 18 Nov 2026 (US date)

Updated **Thu 19 Nov, 11:39 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-18/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Murray-Boyles PTS over 14.5 (15+) | WAS @ TOR | betright | 2.05 | 1.89 | 1.55 | 64.5% | 50.9% | 53.0% | +8.7% | +32.1% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Murray-Boyles PTS over 29.5 (30+) | WAS @ TOR | draftkings | 27.00 | 24.10 | 12.58 | 8.0% | 3.5% | 4.2% | +12.1% | +114.6% | 0.1% |
| Nikola Jokic AST over 15.5 (16+) | BOS @ DEN | draftkings | 23.00 | 20.92 | 11.47 | 8.7% | 4.1% | 4.8% | +9.9% | +100.4% | 0.1% |
| Collin Murray-Boyles AST over 5.5 (6+) | WAS @ TOR | draftkings | 10.50 | 9.65 | 5.45 | 18.4% | 8.9% | 10.4% | +8.8% | +92.7% | 0.2% |
| Aday Mara BLK over 3.5 (4+) | ATL @ OKC | draftkings | 12.60 | 11.59 | 6.54 | 15.3% | 7.4% | 8.6% | +8.7% | +92.6% | 0.2% |
| Nikola Jokic AST over 13.5 (14+) | BOS @ DEN | draftkings | 10.60 | 9.81 | 5.63 | 17.8% | 8.8% | 10.2% | +8.1% | +88.3% | 0.2% |
| Draymond Green PRA over 24.5 (25+) | GSW @ DAL | draftkings | 11.20 | 10.37 | 5.97 | 16.8% | 8.3% | 9.6% | +8.0% | +87.6% | 0.2% |
| Jakob Poeltl REB over 13.5 (14+) | WAS @ TOR | draftkings | 16.20 | 15.04 | 8.72 | 11.5% | 5.8% | 6.7% | +7.7% | +85.8% | 0.1% |
| Collin Murray-Boyles PTS over 24.5 (25+) | WAS @ TOR | draftkings | 10.10 | 9.38 | 5.44 | 18.4% | 9.2% | 10.7% | +7.6% | +85.6% | 0.2% |
| Luka Doncic STL over 3.5 (4+) | UTA @ LAL | draftkings | 13.40 | 12.48 | 7.32 | 13.7% | 7.0% | 8.0% | +7.3% | +83.2% | 0.1% |
| Derik Queen PR over 29.5 (30+) | DET @ NOP | draftkings | 17.80 | 16.72 | 10.00 | 10.0% | 5.2% | 6.0% | +6.5% | +78.0% | 0.1% |
| Derik Queen PR over 24.5 (25+) | DET @ NOP | draftkings | 7.70 | 7.25 | 4.36 | 22.9% | 12.1% | 13.8% | +6.2% | +76.5% | 0.2% |
| Devin Booker AST over 9.5 (10+) | PHX @ SAC | draftkings | 14.40 | 13.66 | 8.42 | 11.9% | 6.5% | 7.3% | +5.4% | +71.0% | 0.1% |
| Draymond Green REB over 7.5 (8+) | GSW @ DAL | draftkings | 7.50 | 7.12 | 4.39 | 22.8% | 12.5% | 14.1% | +5.4% | +70.8% | 0.2% |
| Devin Booker PRA over 54.5 (55+) | PHX @ SAC | draftkings | 22.00 | 20.92 | 13.04 | 7.7% | 4.2% | 4.8% | +5.1% | +68.7% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ausar Thompson PTS under 13.5 | DET @ NOP | draftkings | 1.97 | 1.83 | 1.45 | 68.9% | 52.0% | 54.6% | +7.7% | +35.9% | 2.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CHI @ BKN | Thu 19 Nov 11:30 | 116.4–118.6 | CHI 43% | 2.31 / 1.76 | BKN -2.5 | 234.5 | BKN -1.5 covers 54%; o239.5 40% |
| WAS @ TOR | Thu 19 Nov 11:30 | 110.2–117.8 | WAS 29% | 3.42 / 1.41 | TOR -7.5 | 227.5 | TOR -4.5 covers 59%; o223.5 59% |
| DET @ NOP | Thu 19 Nov 12:00 | 117.6–109.5 | DET 71% | 1.40 / 3.48 | NOP +8.5 | 226.5 | NOP +5.5 covers 43%; o226.5 51% |
| ATL @ OKC | Thu 19 Nov 12:00 | 108.9–118.3 | ATL 25% | 3.93 / 1.34 | OKC -9.5 | 227.5 | OKC -6.5 covers 58%; o228.5 47% |
| BOS @ DEN | Thu 19 Nov 13:30 | 112.7–108.4 | BOS 61% | 1.63 / 2.59 | DEN +4.5 | 221.5 | DEN +2.5 covers 45%; o219.5 53% |
| GSW @ DAL | Thu 19 Nov 12:00 | 114.9–116.4 | GSW 46% | 2.18 / 1.84 | DAL -1.5 | 231.5 | DAL -4.5 covers 42%; o223.5 66% |
| UTA @ LAL | Thu 19 Nov 14:00 | 107.6–125.2 | UTA 11% | 9.47 / 1.12 | LAL -17.5 | 232.5 | LAL -12.5 covers 64%; o230.5 55% |
| PHX @ SAC | Thu 19 Nov 14:00 | 119.3–113.7 | PHX 66% | 1.52 / 2.92 | SAC +5.5 | 232.5 | SAC +7.5 covers 55%; o227.5 61% |

### CHI @ BKN
Out: Grant Nelson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Tobe Awaka (CHI), Orlando Robinson (CHI), Caleb Wilson (CHI)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaac Okoro PTS under 9.5 | CHI @ BKN | tab | 1.95 | 1.93 | 1.76 | 56.9% | 51.0% | 51.9% | +1.4% | +11.0% | 0.4% |
| Egor Demin PTS under 10.5 | CHI @ BKN | pointsbetau | 2.05 | 2.02 | 1.81 | 55.1% | 48.4% | 49.4% | +1.3% | +13.0% | 0.3% |
| Josh Giddey PTS under 12.5 | CHI @ BKN | tab | 1.90 | 1.89 | 1.86 | 53.7% | 52.6% | 52.8% | +0.4% | +2.0% | 0.1% |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell | 98% | 30.6<br><sub>-,-,31,30,33</sub> | 21.1<br><sub>-,-,33,24,27</sub> | 23.5 · 22.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>-,-,5,5,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>-,-,2,3,6</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>-,-,4,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.3 | 2.4 | 27.1 |
| Matas Buzelis | 98% | 29.2<br><sub>31,31,29,30,31</sub> | 17.5<br><sub>19,13,11,18,23</sub> | 16.5 · 15.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>5,3,6,9,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,2,2,2,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.1<br><sub>3,3,3,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.1 | 2.5 | 25.1 |
| Josh Giddey | 98% | 29.0<br><sub>34,25,39,26,24</sub> | 12.7<br><sub>19,9,15,8,4</sub> | 12.5 · 11.5<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>7,2,10,8,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 8.1<br><sub>15,7,14,5,8</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,1,3,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.6 | 3.0 | 27.2 |
| Jalen Smith | 98% | 27.9<br><sub>30,30,32,-,28</sub> | 14.5<br><sub>17,23,15,-,17</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 8.7<br><sub>8,4,12,-,11</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,3,3,-,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.8<br><sub>2,5,1,-,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 1.1 | 1.2 | 25.1 |
| Isaac Okoro | 98% | 27.8<br><sub>25,23,41,31,32</sub> | 9.3<br><sub>12,0,15,9,13</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,2,3,7,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>1,4,2,4,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.0 | 14.1 |
| Tre Jones | 98% | 20.3<br><sub>14,28,15,24,23</sub> | 11.1<br><sub>6,13,4,16,16</sub> | 12.5 · 11.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,1,0,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>1,3,3,4,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.4<br><sub>0,1,0,1,0</sub> |  | 1.0 | 0.2 | 1.4 | 17.2 |
| Patrick Williams | 80% | 20.3<br><sub>25,28,24,26,13</sub> | 7.2<br><sub>7,9,13,14,0</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,7,4,5,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>3,4,2,1,0</sub> |  | 0.9<br><sub>1,0,4,2,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.8 | 0.4 | 1.0 | 11.5 |
| Nic Claxton | 98% | 18.0<br><sub>18,16,22,-,17</sub> | 7.1<br><sub>4,17,2,-,8</sub> |  | 4.8<br><sub>4,6,6,-,2</sub> |  | 2.0<br><sub>4,1,2,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.8 | 0.9 | 13.8 |
| Buddy Hield | 76% | 16.8<br><sub>-,-,25,20,19</sub> | 8.1<br><sub>-,-,12,16,6</sub> |  | 2.4<br><sub>-,-,3,4,4</sub> |  | 1.7<br><sub>-,-,3,2,2</sub> |  | 1.3<br><sub>-,-,2,4,2</sub> |  | 0.7 | 0.2 | 1.0 | 12.2 |
| Noa Essengue | 96% | 12.3<br><sub>15,11,8,7,14</sub> | 4.9<br><sub>10,8,5,0,1</sub> |  | 2.6<br><sub>7,4,1,1,2</sub> |  | 0.7<br><sub>1,3,1,0,1</sub> |  | 0.4<br><sub>0,1,1,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.2 |
| Zach Collins | 58% | 11.9<br><sub>-,3,-,28,-</sub> | 5.1<br><sub>-,2,-,8,-</sub> |  | 3.5<br><sub>-,2,-,5,-</sub> |  | 1.2<br><sub>-,1,-,4,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.7 | 9.8 |
| Leonard Miller | 76% | 10.9<br><sub>-,2,-,17,1</sub> | 5.1<br><sub>-,0,-,4,0</sub> |  | 2.6<br><sub>-,0,-,3,0</sub> |  | 0.7<br><sub>-,0,-,4,0</sub> |  | 0.4<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.4 |
| Jordan Hawkins | 63% | 8.8<br><sub>17,24,-,-,4</sub> | 3.8<br><sub>9,7,-,-,0</sub> |  | 1.1<br><sub>0,4,-,-,0</sub> |  | 0.6<br><sub>1,2,-,-,1</sub> |  | 0.3<br><sub>1,1,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |
| Dailyn Swain | 63% | 6.0<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 4.0 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 83% | 33.3<br><sub>36,29,28,-,40</sub> | 23.0<br><sub>25,19,22,-,25</sub> | 23.5 · 23.5<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>9,9,6,-,6</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,0,3,-,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 3.2<br><sub>3,4,4,-,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.1 | 32.6 |
| Julius Randle | 98% | 32.4<br><sub>34,30,29,31,34</sub> | 20.8<br><sub>19,13,17,22,33</sub> | 22.5 · 22.5<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>7,4,4,4,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>8,4,5,5,1</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,0,0,3,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.2 | 3.0 | 32.1 |
| Egor Demin | 98% | 24.2<br><sub>-,-,23,27,26</sub> | 10.6<br><sub>-,-,22,11,9</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>-,-,1,1,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 3.1<br><sub>-,-,1,2,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>-,-,4,3,2</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.3 | 1.5 | 16.6 |
| Day'Ron Sharpe | 98% | 24.1<br><sub>32,20,19,28,25</sub> | 10.9<br><sub>12,6,15,16,6</sub> | 10.5 · 10.5<br><sub>o 48% · u 52%</sub> | 8.7<br><sub>10,4,4,11,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>13,6,5,5,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.3<br><sub>0,0,2,0,0</sub> |  | 1.2 | 1.1 | 1.8 | 23.4 |
| Nolan Traore | 98% | 24.0<br><sub>23,21,-,20,30</sub> | 12.7<br><sub>19,14,-,11,23</sub> | 13.5 · 13.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,1,-,1,1</sub> |  | 3.5<br><sub>2,2,-,2,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,2,-,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.5 | 2.1 | 18.5 |
| Noah Clowney | 98% | 21.6<br><sub>21,8,19,35,24</sub> | 9.0<br><sub>3,2,16,15,9</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>10,0,3,7,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>0,0,0,3,3</sub> |  | 1.2<br><sub>1,0,2,3,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.7 | 0.7 | 0.9 | 14.3 |
| Mikel Brown Jr. | 98% | 20.3<br><sub>25,-,-,20,18</sub> | 9.6<br><sub>18,-,-,6,3</sub> | 10.5 · 10.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>1,-,-,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.4<br><sub>3,-,-,2,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>3,-,-,2,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.5 | 15.3 |
| Danny Wolf | 84% | 18.0<br><sub>31,36,29,28,11</sub> | 7.8<br><sub>11,10,10,14,3</sub> |  | 4.7<br><sub>9,3,11,6,2</sub> |  | 1.8<br><sub>1,2,4,1,1</sub> |  | 0.9<br><sub>2,1,1,4,1</sub> |  | 0.5 | 0.5 | 0.9 | 14.4 |
| Keon Ellis | 88% | 17.4<br><sub>-,22,26,7,20</sub> | 4.7<br><sub>-,3,11,0,8</sub> |  | 1.9<br><sub>-,1,4,0,2</sub> |  | 1.1<br><sub>-,4,3,1,0</sub> |  | 0.6<br><sub>-,1,2,0,2</sub> |  | 1.1 | 0.6 | 0.5 | 7.8 |
| Moritz Wagner | 97% | 15.0<br><sub>16,16,19,18,10</sub> | 8.7<br><sub>9,12,16,10,4</sub> |  | 4.0<br><sub>2,3,3,6,5</sub> |  | 1.2<br><sub>0,1,4,4,1</sub> |  | 0.7<br><sub>1,1,2,2,0</sub> |  | 0.5 | 0.2 | 0.8 | 13.9 |
| Terance Mann | 64% | 10.9<br><sub>13,22,18,9,-</sub> | 2.8<br><sub>0,0,6,2,-</sub> |  | 1.4<br><sub>2,1,1,1,-</sub> |  | 1.1<br><sub>0,1,3,1,-</sub> |  | 0.2<br><sub>0,0,2,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.3 |
| Chaney Johnson | 98% | 9.8<br><sub>8,15,15,12,1</sub> | 3.0<br><sub>5,2,4,1,0</sub> |  | 1.7<br><sub>2,0,3,5,0</sub> |  | 0.6<br><sub>1,1,2,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.2 |
| Josh Minott | 58% | 7.6<br><sub>-,12,7,2,-</sub> | 4.2<br><sub>-,10,0,0,-</sub> |  | 1.5<br><sub>-,2,2,0,-</sub> |  | 0.4<br><sub>-,1,0,0,-</sub> |  | 0.4<br><sub>-,2,0,0,-</sub> |  | 0.5 | 0.3 | 0.4 | 6.2 |

</details>


### WAS @ TOR
Out: Scottie Barnes (TOR), RJ Barrett (TOR), Kawhi Leonard (TOR), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Murray-Boyles PTS over 14.5 (15+) | WAS @ TOR | betright | 2.05 | 1.89 | 1.55 | 64.5% | 50.9% | 53.0% | +8.7% | +32.1% | 2.0% |
| Tre Johnson PTS under 9.5 | WAS @ TOR | tab | 1.95 | 1.90 | 1.61 | 62.3% | 50.7% | 52.5% | +2.5% | +21.5% | 0.7% |
| Ja'Kobe Walter PTS over 14.5 (15+) | WAS @ TOR | sportsbet | 2.05 | 2.00 | 1.82 | 54.9% | 49.1% | 50.0% | +2.5% | +12.6% | 0.6% |
| Anthony Davis PTS under 22.5 | WAS @ TOR | betright | 1.96 | 1.92 | 1.57 | 63.7% | 50.0% | 52.1% | +2.2% | +24.9% | 0.6% |
| AJ Dybantsa PTS under 16.5 | WAS @ TOR | tab | 1.90 | 1.88 | 1.54 | 65.1% | 51.0% | 53.2% | +1.1% | +23.7% | 0.3% |
| Trae Young PTS under 17.5 | WAS @ TOR | betright | 1.95 | 1.95 | 1.82 | 54.9% | 50.7% | 51.3% | +0.3% | +7.1% | 0.1% |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 99% | 34.2<br><sub>38,34,45,26,33</sub> | 17.6<br><sub>20,15,37,0,13</sub> | 17.5 · 17.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,3,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 8.8<br><sub>7,4,14,8,12</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>3,3,4,0,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 3.6 | 29.2 |
| Anthony Davis | 98% | 33.8<br><sub>34,34,44,31,35</sub> | 20.6<br><sub>44,21,30,14,23</sub> | 22.5 · 22.5<br><sub>o 48% · u 52%</sub> | 10.6<br><sub>13,13,15,8,4</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>1,0,4,5,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 1.1 | 1.6 | 2.3 | 33.8 |
| AJ Dybantsa | 98% | 33.1<br><sub>37,34,44,30,32</sub> | 14.8<br><sub>21,13,5,16,21</sub> | 16.5 · 15.5<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>8,4,8,7,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,2,4,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.5 | 2.4 | 23.1 |
| Kyshawn George | 99% | 32.5<br><sub>35,39,26,30,38</sub> | 15.4<br><sub>12,25,14,11,18</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>3,9,1,2,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>2,3,5,4,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>2,5,3,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 1.1 | 2.6 | 24.1 |
| Alex Sarr | 98% | 27.7<br><sub>25,25,44,27,31</sub> | 12.2<br><sub>4,5,30,25,6</sub> | 11.5 · 10.5<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>8,8,9,9,4</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,0,2,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1<br><sub>0,1,4,3,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 1.3 | 1.5 | 21.3 |
| Tre Johnson | 96% | 21.3<br><sub>29,29,30,-,21</sub> | 8.7<br><sub>2,15,13,-,9</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,3,4,-,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>0,1,2,-,3</sub> |  | 1.2<br><sub>0,2,1,-,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.2 | 1.3 | 11.9 |
| Bilal Coulibaly | 98% | 20.9<br><sub>-,25,29,21,16</sub> | 7.4<br><sub>-,5,4,9,11</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>-,6,7,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>-,2,0,0,0</sub> |  | 0.7<br><sub>-,0,0,1,1</sub> |  | 0.8 | 0.7 | 1.1 | 11.8 |
| Khris Middleton | 52% | 13.1<br><sub>-,-,-,9,18</sub> | 4.7<br><sub>-,-,-,8,9</sub> |  | 2.0<br><sub>-,-,-,0,3</sub> |  | 1.2<br><sub>-,-,-,2,3</sub> |  | 0.4<br><sub>-,-,-,2,2</sub> |  | 0.4 | 0.1 | 1.0 | 7.8 |
| Deandre Ayton | 99% | 12.0<br><sub>13,9,9,10,8</sub> | 3.9<br><sub>2,2,2,2,4</sub> |  | 3.7<br><sub>8,2,4,1,0</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 8.0 |
| Bub Carrington | 99% | 11.8<br><sub>19,10,16,23,2</sub> | 3.7<br><sub>4,0,2,11,0</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 1.5<br><sub>4,0,2,4,0</sub> |  | 0.4<br><sub>1,0,0,3,0</sub> |  | 0.3 | 0.1 | 0.8 | 6.4 |
| Will Riley | 86% | 8.2<br><sub>4,-,3,16,2</sub> | 3.7<br><sub>0,-,3,14,2</sub> |  | 1.0<br><sub>0,-,0,3,1</sub> |  | 0.6<br><sub>1,-,0,0,0</sub> |  | 0.2<br><sub>0,-,1,2,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Anthony Gill | 58% | 7.2<br><sub>2,-,-,6,2</sub> | 2.7<br><sub>0,-,-,5,2</sub> |  | 1.2<br><sub>2,-,-,1,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Tre Mann | 63% | 6.0<br><sub>2,-,-,11,2</sub> | 2.6<br><sub>0,-,-,4,2</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.7<br><sub>0,-,-,1,1</sub> |  | 0.2<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Murray-Boyles | 98% | 34.1<br><sub>-,20,32,40,33</sub> | 18.1<br><sub>-,5,14,6,8</sub> | 14.5 · 13.5<br><sub>o 53% · u 47%</sub> | 7.7<br><sub>-,4,0,13,1</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>-,3,4,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.5<br><sub>-,1,1,0,0</sub> |  | 1.6 | 1.5 | 2.3 | 29.4 |
| Immanuel Quickley | 88% | 33.2<br><sub>-,28,28,38,34</sub> | 22.2<br><sub>-,11,26,17,14</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>-,4,4,6,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 7.4<br><sub>-,4,6,6,7</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>-,1,3,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.1 | 1.7 | 33.8 |
| Ja'Kobe Walter | 98% | 33.1<br><sub>34,35,32,36,33</sub> | 16.1<br><sub>12,17,6,7,25</sub> | 13.5 · 14.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>6,3,5,2,1</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>0,1,0,1,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>2,5,1,1,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.6 | 0.3 | 1.2 | 23.0 |
| Jamal Shead | 98% | 28.1<br><sub>36,22,22,26,20</sub> | 11.4<br><sub>20,3,5,19,7</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>2,3,1,2,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 8.0<br><sub>11,6,5,4,6</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>4,0,1,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.2 | 2.1 | 21.8 |
| Jakob Poeltl | 91% | 25.8<br><sub>31,32,25,17,18</sub> | 12.8<br><sub>18,6,9,11,3</sub> | 12.5 · 11.5<br><sub>o 52% · u 48%</sub> | 8.8<br><sub>8,9,5,5,6</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>2,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.0 | 1.4 | 23.9 |
| Jamison Battle | 98% | 24.7<br><sub>29,25,25,8,7</sub> | 11.9<br><sub>18,12,13,0,0</sub> | 10.5 · 9.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>1,2,1,3,1</sub> |  | 1.1<br><sub>2,0,1,0,0</sub> |  | 1.9<br><sub>5,2,3,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 16.4 |
| Allen Graves | 98% | 22.8<br><sub>13,18,13,16,13</sub> | 8.7<br><sub>3,13,0,2,3</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>2,5,2,5,2</sub> |  | 1.6<br><sub>1,0,0,3,1</sub> |  | 1.0<br><sub>1,3,0,0,1</sub> |  | 0.8 | 0.5 | 0.8 | 14.9 |
| Alijah Martin | 96% | 17.7<br><sub>21,16,18,12,8</sub> | 7.8<br><sub>2,12,7,2,0</sub> |  | 2.7<br><sub>3,1,4,3,2</sub> |  | 1.6<br><sub>3,0,1,0,0</sub> |  | 0.8<br><sub>0,4,1,0,0</sub> |  | 0.9 | 0.3 | 1.1 | 12.1 |
| Kyle Anderson | 52% | 15.8<br><sub>16,11,5,-,-</sub> | 5.4<br><sub>6,2,0,-,-</sub> |  | 3.1<br><sub>2,3,0,-,-</sub> |  | 3.0<br><sub>2,4,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.8 | 0.5 | 0.8 | 11.5 |
| Trayce Jackson-Davis | 52% | 15.0<br><sub>14,-,-,-,-</sub> | 6.3<br><sub>4,-,-,-,-</sub> |  | 5.2<br><sub>6,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.9 | 0.8 | 0.8 | 12.7 |
| Kevin McCullar Jr. | 16% | 12.3<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.1 | 0.8 | 8.0 |
| Malachi Smith | 96% | 12.1<br><sub>1,-,2,-,-</sub> | 4.6<br><sub>0,-,0,-,-</sub> |  | 2.0<br><sub>0,-,0,-,-</sub> |  | 1.8<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.4 |
| Jaden Bradley | 52% | 9.8<br><sub>9,-,2,-,-</sub> | 3.6<br><sub>0,-,1,-,-</sub> |  | 1.6<br><sub>1,-,0,-,-</sub> |  | 1.4<br><sub>3,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.6 |

</details>


### DET @ NOP
Out: Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Jalen Duren (DET), Ronald Holland II (DET), Taurean Prince (DET), Duncan Robinson (DET)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul Reed PTS over 11.5 (12+) | DET @ NOP | tab | 2.00 | 1.93 | 1.59 | 63.0% | 49.8% | 51.8% | +3.6% | +26.0% | 0.9% |
| Zion Williamson PTS under 21.5 | DET @ NOP | pointsbetau | 2.00 | 1.96 | 1.67 | 59.9% | 49.3% | 50.9% | +1.8% | +19.9% | 0.5% |
| John Collins PTS under 13.5 | DET @ NOP | betright | 1.92 | 1.91 | 1.66 | 60.1% | 50.9% | 52.3% | +0.3% | +15.2% | 0.1% |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 100% | 36.1<br><sub>38,27,48,36,38</sub> | 28.7<br><sub>14,17,52,33,27</sub> | – · 24.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>4,3,5,5,5</sub> |  | 8.9<br><sub>8,7,11,8,6</sub> |  | 2.6<br><sub>1,0,3,3,1</sub> |  | 1.2 | 0.8 | 3.9 | 42.8 |
| Daniss Jenkins | 100% | 34.2<br><sub>32,36,42,35,38</sub> | 17.4<br><sub>31,22,21,10,25</sub> | 19.5 · 16.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>5,6,6,1,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.7<br><sub>4,8,0,5,5</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>8,2,3,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.3 | 2.1 | 27.1 |
| Kevin Huerter | 100% | 32.8<br><sub>35,33,24,38,36</sub> | 13.5<br><sub>24,12,11,20,9</sub> | 15.5 · 14.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>5,2,1,4,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>5,3,0,7,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>4,0,1,2,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.7 | 1.5 | 21.1 |
| Ausar Thompson | 100% | 29.9<br><sub>24,28,43,18,29</sub> | 11.5<br><sub>7,8,17,10,14</sub> | 13.5 · 12.5<br><sub>o 47% · u 53%</sub> | 7.8<br><sub>11,5,11,8,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 5.4<br><sub>3,4,11,5,12</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.0 | 1.1 | 2.0 | 24.7 |
| Paul Reed | 98% | 29.2<br><sub>20,21,38,23,25</sub> | 14.4<br><sub>8,4,13,9,10</sub> | 11.5 · 11.5<br><sub>o 52% · u 48%</sub> | 9.2<br><sub>10,10,11,9,6</sub> |  | 2.7<br><sub>0,2,3,1,5</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.5 | 1.6 | 1.6 | 26.3 |
| John Collins | 100% | 28.9<br><sub>32,28,25,26,23</sub> | 12.8<br><sub>8,24,10,8,11</sub> | 14.5 · 13.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>4,10,4,7,1</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>1,3,0,0,0</sub> |  | 1.1<br><sub>1,2,2,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.9 | 1.4 | 20.3 |
| Javonte Green | 98% | 18.9<br><sub>17,11,15,12,23</sub> | 6.7<br><sub>7,7,5,5,6</sub> |  | 2.7<br><sub>2,1,1,1,6</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 1.1 | 0.4 | 0.5 | 10.1 |
| Chaz Lanier | 58% | 14.1<br><sub>-,2,-,-,25</sub> | 4.5<br><sub>-,0,-,-,3</sub> |  | 1.2<br><sub>-,0,-,-,3</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.7<br><sub>-,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.3 | 6.5 |
| Isaiah Joe | 91% | 12.3<br><sub>-,-,-,-,-</sub> | 6.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.6 | 8.8 |
| Tolu Smith | 52% | 8.8<br><sub>-,-,-,1,-</sub> | 3.2<br><sub>-,-,-,3,-</sub> |  | 3.1<br><sub>-,-,-,2,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.9 |
| Elijah Harkless | 52% | 7.0<br><sub>-,-,-,2,4</sub> | 1.8<br><sub>-,-,-,2,0</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 3.4 |
| Isaac Jones | 52% | 6.8<br><sub>-,2,-,2,-</sub> | 8.2<br><sub>-,0,-,0,-</sub> |  | 1.8<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.5 | 0.4 | 10.3 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 100% | 33.7<br><sub>24,29,35,41,33</sub> | 17.6<br><sub>9,15,30,16,23</sub> | 19.5 · 19.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>0,1,10,6,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>4,2,0,4,3</sub> |  | 2.3<br><sub>1,3,6,2,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 1.5 | 25.4 |
| Zion Williamson | 100% | 32.6<br><sub>-,30,33,31,25</sub> | 20.5<br><sub>-,29,22,24,16</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>-,4,5,6,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>-,2,4,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.3<br><sub>-,1,0,2,0</sub> |  | 1.3 | 0.8 | 2.3 | 29.8 |
| Jeremiah Fears | 100% | 31.8<br><sub>29,28,34,33,29</sub> | 17.2<br><sub>11,14,18,13,19</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>3,4,5,4,10</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>8,5,7,7,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>1,2,0,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.6 | 2.8 | 27.2 |
| Herbert Jones | 100% | 26.6<br><sub>24,25,32,27,24</sub> | 8.3<br><sub>10,2,8,10,8</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>6,2,2,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>1,3,3,1,3</sub> |  | 1.1<br><sub>2,0,0,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.5 | 1.2 | 13.2 |
| Jordan Poole | 80% | 24.8<br><sub>34,21,21,24,31</sub> | 11.8<br><sub>7,14,13,14,11</sub> | 10.5 · 11.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>3,0,2,2,2</sub> |  | 3.4<br><sub>2,1,5,5,5</sub> |  | 1.9<br><sub>1,2,1,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.4 | 1.7 | 17.4 |
| Derik Queen | 99% | 24.8<br><sub>21,14,23,25,21</sub> | 12.2<br><sub>16,9,10,10,17</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 7.1<br><sub>4,0,6,5,10</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>0,0,2,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>0,1,0,2,4</sub> |  | 1.1 | 1.0 | 2.4 | 22.2 |
| Yves Missi | 100% | 24.1<br><sub>-,-,-,22,23</sub> | 7.1<br><sub>-,-,-,3,6</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>-,-,-,8,14</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>-,-,-,1,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.5 | 2.2 | 1.2 | 16.2 |
| Karlo Matkovic | 98% | 21.4<br><sub>17,22,19,14,20</sub> | 7.8<br><sub>4,4,1,5,3</sub> |  | 4.7<br><sub>6,4,3,3,2</sub> |  | 1.1<br><sub>2,1,0,1,0</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.9 | 0.9 | 13.6 |
| Jaron Pierre Jr. | 93% | 16.8<br><sub>-,7,4,23,19</sub> | 7.2<br><sub>-,4,0,13,10</sub> |  | 2.5<br><sub>-,4,0,2,4</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,1,0,2,2</sub> |  | 0.5 | 0.2 | 1.1 | 10.5 |
| DeAndre Jordan | 38% | 12.9<br><sub>-,11,17,-,-</sub> | 3.4<br><sub>-,0,6,-,-</sub> |  | 4.7<br><sub>-,3,8,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.7 | 0.7 | 8.7 |
| AJ Johnson | 63% | 7.8<br><sub>12,7,4,-,6</sub> | 2.7<br><sub>2,2,1,-,0</sub> |  | 1.0<br><sub>2,1,0,-,0</sub> |  | 0.6<br><sub>3,0,0,-,0</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.3 |
| Malik Dia | 64% | 7.6<br><sub>-,-,4,-,5</sub> | 3.0<br><sub>-,-,2,-,2</sub> |  | 0.9<br><sub>-,-,0,-,1</sub> |  | 1.0<br><sub>-,-,1,-,1</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |
| Julian Reese | 64% | 7.4<br><sub>9,7,4,-,5</sub> | 2.6<br><sub>2,2,0,-,0</sub> |  | 1.5<br><sub>0,2,2,-,1</sub> |  | 0.3<br><sub>0,1,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.4 |

</details>


### ATL @ OKC
Out: Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Kingston Flemings (ATL), Mouhamed Gueye (ATL), Jock Landale (ATL), CJ McCollum (ATL), Asa Newell (ATL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dyson Daniels PTS over 10.5 (11+) | ATL @ OKC | pointsbetau | 2.05 | 2.04 | 1.84 | 54.4% | 48.0% | 48.9% | +0.4% | +11.4% | 0.1% |
| Shai Gilgeous-Alexander PTS under 31.5 | ATL @ OKC | sportsbet | 1.96 | 1.96 | 1.61 | 62.0% | 49.0% | 51.0% | +0.0% | +21.7% | 0.0% |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 100% | 36.7<br><sub>-,36,38,40,35</sub> | 20.6<br><sub>-,30,15,27,14</sub> | 19.5 · 19.5<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>-,7,7,11,11</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 7.7<br><sub>-,6,4,10,5</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>-,0,0,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 3.9 | 37.9 |
| Nickeil Alexander-Walker | 100% | 35.3<br><sub>33,31,34,41,33</sub> | 21.8<br><sub>28,20,20,16,20</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>2,3,4,6,5</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>2,1,4,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.4<br><sub>4,2,4,1,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.5 | 2.8 | 29.0 |
| Onyeka Okongwu | 100% | 34.0<br><sub>33,30,30,35,36</sub> | 15.8<br><sub>22,16,16,17,16</sub> | 13.5 · 13.5<br><sub>o 51% · u 49%</sub> | 8.5<br><sub>10,2,9,6,11</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>1,5,3,1,0</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 1.0 | 1.9 | 27.3 |
| Dyson Daniels | 100% | 33.3<br><sub>35,31,31,36,27</sub> | 11.7<br><sub>13,9,10,6,9</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,10,6,9,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>12,7,8,4,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.5<br><sub>0,0,1,0,0</sub> |  | 2.0 | 0.4 | 2.1 | 25.3 |
| Aaron Wiggins | 100% | 31.2<br><sub>29,26,23,26,24</sub> | 14.7<br><sub>19,20,15,9,7</sub> | 14.5 · 13.5<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>4,4,3,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>3,6,3,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,5,4,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.4 | 1.9 | 21.9 |
| Luguentz Dort | 98% | 25.5<br><sub>32,20,18,20,18</sub> | 9.1<br><sub>25,3,4,10,3</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>7,2,3,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>4,1,2,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>5,1,1,1,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 1.1 | 13.8 |
| Corey Kispert | 52% | 14.8<br><sub>16,-,-,-,16</sub> | 7.4<br><sub>7,-,-,-,14</sub> |  | 1.9<br><sub>2,-,-,-,3</sub> |  | 1.1<br><sub>1,-,-,-,1</sub> |  | 1.1<br><sub>1,-,-,-,3</sub> |  | 0.3 | 0.1 | 0.8 | 10.5 |
| Jalen Wilson | 47% | 14.0<br><sub>-,-,-,-,-</sub> | 5.6<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.8 | 8.9 |
| RayJ Dennis | 64% | 13.6<br><sub>-,-,-,-,10</sub> | 5.0<br><sub>-,-,-,-,6</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 2.2<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.2 | 0.9 | 9.1 |
| Zuby Ejiofor | 67% | 13.1<br><sub>15,18,4,-,12</sub> | 4.4<br><sub>10,7,0,-,4</sub> |  | 2.9<br><sub>5,6,0,-,3</sub> |  | 1.2<br><sub>5,0,0,-,0</sub> |  | 0.4<br><sub>0,1,0,-,1</sub> |  | 0.4 | 0.3 | 0.7 | 8.5 |
| Dorian Finney-Smith | 23% | 7.6<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 31.1<br><sub>29,29,36,39,30</sub> | 29.4<br><sub>30,26,31,40,37</sub> | 32.5 · 31.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,8,4,4,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.7<br><sub>9,3,2,5,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,0,0,2,4</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.7 | 2.6 | 38.9 |
| Jared McCain | 100% | 25.9<br><sub>23,31,31,31,30</sub> | 14.1<br><sub>19,21,10,23,12</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,3,6,4,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,3,3,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>2,4,2,7,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.1 | 1.5 | 19.0 |
| Ajay Mitchell | 100% | 25.7<br><sub>22,28,-,-,27</sub> | 14.9<br><sub>12,14,-,-,14</sub> | 18.5 · 17.5<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>4,3,-,-,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>0,3,-,-,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>0,0,-,-,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 1.7 | 21.9 |
| Aday Mara | 100% | 24.9<br><sub>27,26,32,21,26</sub> | 10.9<br><sub>18,10,11,10,16</sub> | 9.5 · 8.5<br><sub>o 50% · u 50%</sub> | 7.9<br><sub>8,10,6,3,13</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>3,2,2,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 2.0 | 2.0 | 20.7 |
| Isaiah Hartenstein | 100% | 23.5<br><sub>18,24,34,30,18</sub> | 9.2<br><sub>2,7,20,21,3</sub> | 9.5 · 8.5<br><sub>o 48% · u 52%</sub> | 10.0<br><sub>14,9,11,16,11</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,5,6,6,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.8 | 1.7 | 23.1 |
| Alex Caruso | 98% | 19.3<br><sub>13,19,29,27,18</sub> | 8.1<br><sub>0,5,14,5,11</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>3,2,7,1,2</sub> |  | 2.3<br><sub>3,1,2,4,3</sub> |  | 1.1<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.4 | 1.0 | 13.4 |
| Kenrich Williams | 98% | 18.8<br><sub>23,19,26,35,19</sub> | 7.2<br><sub>9,3,11,8,10</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>4,2,2,8,1</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>2,0,2,4,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>1,1,2,0,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.1 | 0.8 | 12.5 |
| Bennett Stirtz | 98% | 16.6<br><sub>29,18,25,12,17</sub> | 6.5<br><sub>11,13,6,5,0</sub> |  | 1.3<br><sub>5,1,1,1,1</sub> |  | 1.1<br><sub>3,1,1,0,2</sub> |  | 0.9<br><sub>2,2,2,1,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.9 |
| Nique Clifford | 96% | 14.3<br><sub>-,20,16,12,24</sub> | 4.9<br><sub>-,4,5,0,9</sub> |  | 2.1<br><sub>-,4,3,0,3</sub> |  | 1.3<br><sub>-,1,1,0,0</sub> |  | 0.4<br><sub>-,0,1,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 8.4 |
| Micah Peavy | 91% | 13.6<br><sub>23,21,12,-,13</sub> | 4.2<br><sub>7,0,0,-,5</sub> |  | 2.5<br><sub>3,2,3,-,3</sub> |  | 0.5<br><sub>0,0,0,-,1</sub> |  | 0.4<br><sub>1,0,0,-,1</sub> |  | 0.5 | 0.2 | 0.4 | 7.1 |
| Jaylin Williams | 98% | 12.7<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> | 5.5 · 5.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 35% · u 65%</sub> | 0.5<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.4 | 0.3 | 0.5 | 8.7 |
| Nikola Topic | 86% | 9.7<br><sub>-,-,-,16,13</sub> | 3.2<br><sub>-,-,-,0,8</sub> |  | 1.1<br><sub>-,-,-,4,0</sub> |  | 2.1<br><sub>-,-,-,3,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.0 | 1.2 | 6.4 |
| Josh Dix | 67% | 9.6<br><sub>21,-,-,17,-</sub> | 3.4<br><sub>2,-,-,0,-</sub> |  | 1.2<br><sub>1,-,-,4,-</sub> |  | 0.6<br><sub>2,-,-,3,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.1 |
| Brooks Barnhizer | 58% | 6.1<br><sub>8,5,-,-,4</sub> | 1.9<br><sub>2,0,-,-,0</sub> |  | 1.4<br><sub>4,1,-,-,0</sub> |  | 0.5<br><sub>3,1,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### BOS @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 33.8<br><sub>29,32,38,30,36</sub> | 24.0<br><sub>21,21,24,32,24</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 7.8<br><sub>4,6,7,6,12</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>6,4,8,6,4</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>5,3,2,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.5 | 2.6 | 38.6 |
| Paul George | 98% | 30.2<br><sub>28,30,-,25,36</sub> | 18.0<br><sub>27,36,-,7,22</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>3,5,-,7,8</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>1,1,-,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>5,6,-,1,5</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.4 | 2.0 | 26.6 |
| Derrick White | 98% | 30.0<br><sub>27,22,38,23,32</sub> | 12.6<br><sub>9,5,19,16,9</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,1,1,4,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.3<br><sub>7,3,7,2,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,1,3,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.8 | 1.3 | 20.3 |
| Payton Pritchard | 98% | 26.4<br><sub>29,30,31,19,32</sub> | 13.0<br><sub>12,18,14,10,21</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,6,1,1,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.8<br><sub>4,5,1,6,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>4,4,2,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.0 | 19.9 |
| Neemias Queta | 98% | 20.4<br><sub>22,22,31,15,-</sub> | 8.0<br><sub>13,4,11,8,-</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>9,6,13,6,-</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>4,3,3,2,-</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.5 | 0.9 | 0.9 | 16.2 |
| Sam Hauser | 98% | 20.1<br><sub>23,18,24,11,25</sub> | 7.9<br><sub>7,12,8,8,12</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>3,5,9,1,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>1,2,0,0,2</sub> |  | 1.5<br><sub>1,4,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.4 | 0.2 | 0.3 | 12.1 |
| Baylor Scheierman | 98% | 15.9<br><sub>19,18,29,18,11</sub> | 5.1<br><sub>7,5,9,12,0</sub> |  | 2.9<br><sub>1,3,7,5,1</sub> |  | 1.2<br><sub>0,2,3,3,1</sub> |  | 0.7<br><sub>1,1,3,2,0</sub> |  | 0.6 | 0.1 | 0.5 | 9.3 |
| Mitchell Robinson | 98% | 15.4<br><sub>18,17,11,15,18</sub> | 4.4<br><sub>12,2,2,0,4</sub> |  | 5.8<br><sub>7,6,2,7,5</sub> |  | 0.7<br><sub>2,2,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 0.6 | 10.9 |
| Jordan Walsh | 98% | 14.1<br><sub>11,19,18,21,17</sub> | 4.3<br><sub>0,8,6,11,6</sub> |  | 2.6<br><sub>3,2,3,1,2</sub> |  | 0.7<br><sub>0,2,0,0,0</sub> |  | 0.5<br><sub>0,1,0,2,2</sub> |  | 0.5 | 0.3 | 0.4 | 7.6 |
| Luka Garza | 98% | 13.3<br><sub>9,9,11,14,18</sub> | 6.3<br><sub>4,2,5,2,3</sub> |  | 3.1<br><sub>5,0,1,3,0</sub> |  | 1.3<br><sub>0,2,0,5,4</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.3 | 0.5 | 10.8 |
| Devin Carter | 91% | 12.5<br><sub>-,-,-,12,-</sub> | 4.9<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,2,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.2 | 0.9 | 8.7 |
| Hugo Gonzalez | 98% | 8.9<br><sub>10,19,8,18,4</sub> | 2.9<br><sub>0,10,0,9,0</sub> |  | 1.8<br><sub>2,2,1,5,2</sub> |  | 0.5<br><sub>1,2,0,2,0</sub> |  | 0.2<br><sub>0,2,0,2,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.1 |
| Chris Cenac Jr. | 58% | 7.5<br><sub>-,-,-,7,12</sub> | 2.8<br><sub>-,-,-,6,4</sub> |  | 1.6<br><sub>-,-,-,3,2</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Mike Conley | 38% | 7.1<br><sub>10,-,-,-,-</sub> | 1.9<br><sub>3,-,-,-,-</sub> |  | 0.7<br><sub>3,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |
| Ron Harper Jr. | 58% | 6.7<br><sub>4,4,-,12,-</sub> | 3.1<br><sub>2,0,-,10,-</sub> |  | 1.0<br><sub>0,1,-,1,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,2,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.6 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.1<br><sub>36,39,37,37,38</sub> | 24.4<br><sub>19,25,27,26,28</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 11.9<br><sub>13,16,11,8,15</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 10.1<br><sub>8,9,8,10,7</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.8 | 3.7 | 46.4 |
| Jamal Murray | 98% | 37.0<br><sub>34,39,32,38,35</sub> | 23.0<br><sub>16,38,30,23,28</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>6,2,4,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>8,2,8,9,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>2,5,4,0,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.6 | 2.5 | 34.1 |
| Christian Braun | 98% | 32.8<br><sub>29,32,37,28,33</sub> | 12.0<br><sub>6,4,12,17,10</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,5,5,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,3,4,1,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.4 | 0.9 | 18.8 |
| Cameron Johnson | 98% | 29.9<br><sub>29,31,30,31,27</sub> | 12.3<br><sub>18,8,23,12,9</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>4,2,4,5,0</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,1,3,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.9<br><sub>2,2,4,1,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.3 | 1.0 | 18.3 |
| Aaron Gordon | 98% | 29.3<br><sub>27,30,27,33,24</sub> | 11.9<br><sub>12,3,9,11,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,5,3,5,1</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>0,2,2,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.5 | 0.4 | 1.2 | 19.4 |
| DeMar DeRozan | 91% | 20.3<br><sub>22,19,20,24,14</sub> | 9.5<br><sub>11,7,8,9,2</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,4,1,3,1</sub> |  | 2.6<br><sub>5,2,4,2,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 14.0 |
| Trevon Brazile | 98% | 17.8<br><sub>14,14,13,16,23</sub> | 5.2<br><sub>3,5,7,5,9</sub> | 5.5 · –<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>4,2,5,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.3 | 0.3 | 0.7 | 10.0 |
| Spencer Jones | 86% | 16.6<br><sub>21,14,22,12,21</sub> | 4.2<br><sub>13,0,3,4,4</sub> |  | 2.4<br><sub>6,0,1,2,3</sub> |  | 0.8<br><sub>0,1,0,1,3</sub> |  | 0.5<br><sub>3,0,1,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.4 |
| Marvin Bagley III | 98% | 12.6<br><sub>12,12,12,13,10</sub> | 5.8<br><sub>10,6,4,7,4</sub> |  | 3.7<br><sub>3,3,2,7,2</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 10.2 |
| Tyus Jones | 97% | 10.0<br><sub>13,6,11,10,10</sub> | 2.5<br><sub>3,2,0,2,0</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 1.7<br><sub>4,0,4,3,2</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.1 |
| Bryce Hopkins | 58% | 8.0<br><sub>3,3,-,-,4</sub> | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Zeke Nnaji | 26% | 6.4<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.7 |
| Alpha Diallo | 48% | 6.1<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### GSW @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Jimmy Butler III (GSW), Stephen Curry (GSW), Al Horford (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg PTS under 23.5 | GSW @ DAL | pointsbetau | 2.00 | 1.94 | 1.62 | 61.8% | 49.6% | 51.5% | +3.0% | +23.6% | 0.7% |
| Draymond Green PTS over 4.5 (5+) | GSW @ DAL | pointsbetau | 1.90 | 1.89 | 1.52 | 65.6% | 50.7% | 53.0% | +0.8% | +24.8% | 0.2% |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 100% | 34.3<br><sub>37,27,36,24,33</sub> | 23.2<br><sub>23,23,25,3,28</sub> | 23.5 · 23.5<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>8,7,10,7,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>3,4,0,1,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>2,4,2,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.8 | 3.5 | 35.2 |
| Brandin Podziemski | 100% | 34.1<br><sub>39,26,37,22,30</sub> | 18.6<br><sub>15,25,22,8,15</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>7,2,6,3,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 5.0<br><sub>1,4,4,0,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,5,4,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.3 | 2.1 | 29.3 |
| Draymond Green | 100% | 28.8<br><sub>34,21,27,16,25</sub> | 6.2<br><sub>2,2,7,4,2</sub> | 4.5 · 4.5<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>6,3,5,3,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>13,6,7,3,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>0,0,1,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.8 | 2.6 | 18.6 |
| LJ Cryer | 100% | 25.7<br><sub>-,20,18,24,24</sub> | 12.2<br><sub>-,10,13,20,7</sub> |  | 2.2<br><sub>-,0,1,2,1</sub> |  | 2.8<br><sub>-,3,1,6,3</sub> |  | 2.1<br><sub>-,2,3,6,1</sub> |  | 0.6 | 0.1 | 1.3 | 17.2 |
| De'Anthony Melton | 98% | 24.5<br><sub>17,26,25,18,21</sub> | 12.4<br><sub>4,16,11,8,8</sub> | 10.5 · 11.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>1,4,4,4,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>1,3,4,3,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,4,3,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.4 | 1.8 | 19.4 |
| Charles Bassey | 100% | 24.1<br><sub>11,18,13,20,16</sub> | 11.3<br><sub>8,12,7,11,4</sub> |  | 9.4<br><sub>4,10,6,5,0</sub> |  | 1.5<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.7 | 1.4 | 22.1 |
| Will Richard | 98% | 23.2<br><sub>12,-,19,30,23</sub> | 7.0<br><sub>4,-,9,7,11</sub> |  | 2.9<br><sub>2,-,4,4,3</sub> |  | 1.5<br><sub>1,-,0,1,1</sub> |  | 0.9<br><sub>0,-,2,1,2</sub> |  | 1.2 | 0.2 | 0.9 | 11.4 |
| Georges Niang | 98% | 20.4<br><sub>25,19,19,15,14</sub> | 8.6<br><sub>11,9,5,5,0</sub> |  | 3.1<br><sub>2,2,5,3,4</sub> |  | 1.5<br><sub>1,2,0,2,2</sub> |  | 1.3<br><sub>3,1,1,1,0</sub> |  | 0.4 | 0.2 | 0.9 | 13.2 |
| Gui Santos | 91% | 19.9<br><sub>12,21,12,21,19</sub> | 8.4<br><sub>3,3,0,7,12</sub> | 7.5 · 8.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>1,7,3,4,7</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>0,4,1,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8<br><sub>0,0,0,1,1</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.3 | 1.4 | 14.5 |
| Gary Payton II | 88% | 15.8<br><sub>13,-,-,13,8</sub> | 6.9<br><sub>4,-,-,2,2</sub> |  | 2.9<br><sub>0,-,-,2,0</sub> |  | 1.3<br><sub>0,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.9 | 0.2 | 0.8 | 11.0 |
| Graham Ike | 91% | 11.1<br><sub>-,12,4,13,8</sub> | 4.7<br><sub>-,4,4,5,3</sub> |  | 2.9<br><sub>-,5,0,2,5</sub> |  | 1.2<br><sub>-,2,1,3,1</sub> |  | 0.3<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.7 |
| Malevy Leons | 67% | 9.8<br><sub>-,12,4,14,6</sub> | 2.8<br><sub>-,0,0,5,2</sub> |  | 1.8<br><sub>-,3,3,1,1</sub> |  | 0.6<br><sub>-,0,0,0,0</sub> |  | 0.1<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.4 | 0.5 | 5.3 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving | 100% | 33.0<br><sub>29,38,27,37,-</sub> | 22.1<br><sub>21,35,10,34,-</sub> | 22.5 · 22.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,0,3,6,-</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>4,4,4,5,-</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>2,7,2,7,-</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.4 | 2.3 | 30.9 |
| Cooper Flagg | 100% | 32.4<br><sub>28,39,27,38,27</sub> | 21.9<br><sub>25,43,12,18,17</sub> | 23.5 · 23.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>5,10,7,8,3</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 5.8<br><sub>12,6,3,5,4</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>3,3,1,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.8 | 2.8 | 34.4 |
| P.J. Washington | 100% | 29.6<br><sub>25,35,16,26,25</sub> | 12.8<br><sub>6,13,10,10,8</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>5,9,3,4,5</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,1,0,1,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.9 | 1.6 | 21.0 |
| Naji Marshall | 93% | 23.8<br><sub>15,25,23,30,23</sub> | 11.8<br><sub>8,6,13,12,13</sub> |  | 3.5<br><sub>1,5,1,3,2</sub> |  | 3.6<br><sub>2,2,4,5,2</sub> |  | 0.8<br><sub>1,0,1,0,3</sub> |  | 0.9 | 0.1 | 1.8 | 18.9 |
| Caleb Martin | 100% | 22.5<br><sub>19,19,21,33,34</sub> | 6.3<br><sub>2,0,7,15,12</sub> | 5.5 · 5.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,3,2,8,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>2,5,5,3,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7<br><sub>0,0,1,1,4</sub> |  | 0.9 | 0.3 | 0.9 | 11.9 |
| Daniel Gafford | 100% | 19.8<br><sub>19,20,16,17,19</sub> | 9.2<br><sub>18,8,3,10,3</sub> | 7.5 · 7.5<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>5,2,3,3,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>2,3,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.6 | 1.4 | 1.1 | 16.4 |
| Zaccharie Risacher | 98% | 19.3<br><sub>16,15,25,14,27</sub> | 7.5<br><sub>11,4,22,5,18</sub> | 5.5 · 5.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>6,2,6,2,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>1,0,3,0,0</sub> |  | 0.8<br><sub>1,0,4,1,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.6 | 0.9 | 12.4 |
| Walter Clayton Jr. | 96% | 16.7<br><sub>16,25,22,13,23</sub> | 6.4<br><sub>5,6,5,2,13</sub> |  | 2.8<br><sub>4,6,1,2,4</sub> |  | 3.1<br><sub>6,4,4,2,3</sub> |  | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.4 | 12.3 |
| Morez Johnson Jr. | 98% | 15.0<br><sub>19,-,13,15,26</sub> | 5.7<br><sub>4,-,0,4,2</sub> |  | 3.1<br><sub>9,-,2,2,6</sub> |  | 1.4<br><sub>1,-,0,0,4</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 10.2 |
| Santi Aldama | 98% | 13.1<br><sub>15,19,10,16,-</sub> | 6.5<br><sub>12,10,3,7,-</sub> | 7.5 · 7.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,4,1,2,-</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>0,1,1,1,-</sub> |  | 0.7<br><sub>2,1,1,2,-</sub> |  | 0.4 | 0.3 | 0.8 | 10.9 |
| Marcus Sasser | 64% | 13.0<br><sub>9,-,9,-,18</sub> | 4.7<br><sub>4,-,3,-,5</sub> |  | 1.2<br><sub>0,-,1,-,1</sub> |  | 1.7<br><sub>0,-,0,-,2</sub> |  | 0.6<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.1 | 0.8 | 7.5 |
| Max Christie | 98% | 11.1<br><sub>17,5,7,-,-</sub> | 4.0<br><sub>5,0,3,-,-</sub> |  | 1.4<br><sub>2,2,2,-,-</sub> |  | 0.7<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>1,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Moussa Cisse | 63% | 6.5<br><sub>5,-,8,-,4</sub> | 2.6<br><sub>2,-,0,-,1</sub> |  | 2.5<br><sub>1,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.0<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.3 |

</details>


### UTA @ LAL
Out: Austin Reaves (LAL), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.6–125.2 | UTA 11% | 9.47 / 1.12 | LAL -17.5 | 232.5 | LAL -12.5 covers 64%; o230.5 55% |
| Expected (weighted by chance each plays) | 107.7–124.6 | UTA 11% | 8.74 / 1.13 | LAL -16.5 | 232.5 | LAL -12.5 covers 62%; o230.5 54% |
| if Jaxson Hayes plays | 107.7–124.4 | UTA 12% | 8.54 / 1.13 | LAL -16.5 | 232.5 | LAL -12.5 covers 62%; o230.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaxson Hayes (UTA) | Questionable | 55% | 21.9 | 8.2 | 5.2 | 1.1 | 0.0 | 0.7 | 0.8 | 1.0 | 14.6 | full tables below |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 33.9<br><sub>-,33,38,34,35</sub> | 21.1<br><sub>-,13,27,13,30</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 3.4 | 31.4 |
| Darryn Peterson | 98% | 33.5<br><sub>31,33,34,34,31</sub> | 18.4<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.0<br><sub>4,5,2,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.6 | 2.2 | 26.9 |
| Ace Bailey | 99% | 32.5<br><sub>35,31,35,30,23</sub> | 15.6<br><sub>23,18,21,7,5</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>7,7,3,8,1</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,2,1,4,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.1<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.8 | 1.7 | 23.0 |
| Brice Sensabaugh | 99% | 29.0<br><sub>14,23,27,30,35</sub> | 16.7<br><sub>5,19,7,14,40</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>4,3,3,7,11</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>4,1,1,2,5</sub> |  | 2.6<br><sub>1,3,1,0,8</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 2.3 | 23.7 |
| Mo Bamba | 88% | 26.2<br><sub>17,18,20,36,31</sub> | 9.5<br><sub>7,5,9,26,15</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 8.4<br><sub>7,1,9,5,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.6 | 1.2 | 19.2 |
| Josh Okogie | 97% | 25.4<br><sub>21,15,22,27,22</sub> | 7.0<br><sub>6,7,7,7,9</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>4,3,2,6,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>4,0,1,0,4</sub> |  | 0.8<br><sub>0,1,2,2,1</sub> |  | 1.3 | 0.3 | 1.0 | 12.2 |
| Svi Mykhailiuk | 97% | 22.5<br><sub>21,20,7,21,33</sub> | 8.1<br><sub>7,3,0,6,8</sub> |  | 2.5<br><sub>2,0,1,2,7</sub> |  | 1.8<br><sub>3,2,0,3,5</sub> |  | 1.4<br><sub>1,1,0,2,2</sub> |  | 0.6 | 0.1 | 0.9 | 12.4 |
| Josh Green | 96% | 20.5<br><sub>30,26,14,15,13</sub> | 4.7<br><sub>2,3,2,6,9</sub> |  | 1.9<br><sub>5,2,0,1,1</sub> |  | 1.1<br><sub>4,1,0,1,0</sub> |  | 0.6<br><sub>0,1,0,2,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.7 |
| Isaiah Collier | 63% | 18.4<br><sub>24,12,16,-,-</sub> | 8.7<br><sub>17,7,3,-,-</sub> |  | 2.6<br><sub>5,3,2,-,-</sub> |  | 4.8<br><sub>5,2,5,-,-</sub> |  | 0.5<br><sub>4,1,1,-,-</sub> |  | 0.8 | 0.2 | 1.9 | 16.1 |
| Kyle Filipowski | 52% | 15.4<br><sub>15,-,2,-,-</sub> | 7.5<br><sub>7,-,2,-,-</sub> |  | 4.7<br><sub>4,-,0,-,-</sub> |  | 1.5<br><sub>1,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.7 | 0.2 | 1.1 | 13.7 |
| Tony Bradley | 72% | 15.3<br><sub>14,-,12,12,17</sub> | 4.8<br><sub>4,-,0,6,3</sub> |  | 4.4<br><sub>5,-,5,2,7</sub> |  | 0.7<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.4 | 0.7 | 9.9 |
| Jonas Aidoo | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 34.5<br><sub>-,39,32,36,42</sub> | 40.1<br><sub>-,32,32,43,36</sub> | 37.5 · –<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>-,10,5,9,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.6 | 4.0 | 55.0 |
| Quentin Grimes | 98% | 29.3<br><sub>32,-,-,37,42</sub> | 12.9<br><sub>12,-,-,22,47</sub> | 16.5 · –<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>1,-,-,6,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>4,-,-,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,-,-,5,10</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.3 | 1.5 | 19.4 |
| Walker Kessler | 98% | 28.5<br><sub>29,30,29,32,-</sub> | 12.3<br><sub>12,21,10,14,-</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 11.8<br><sub>16,10,11,12,-</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>4,4,3,3,-</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 26.0 |
| Matisse Thybulle | 98% | 24.6<br><sub>28,23,23,26,31</sub> | 7.9<br><sub>4,6,8,12,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,0,5,8,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 2.7 | 0.9 | 1.1 | 12.2 |
| Jake LaRavia | 98% | 23.2<br><sub>29,32,21,32,23</sub> | 6.6<br><sub>5,4,0,12,4</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>1,3,9,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.7 | 1.1 | 12.7 |
| Sandro Mamukelashvili | 99% | 22.2<br><sub>18,32,26,21,23</sub> | 10.5<br><sub>7,23,23,4,3</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,8,3,2,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.4<br><sub>1,5,5,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.5 | 0.8 | 17.2 |
| Ziaire Williams | 98% | 21.6<br><sub>21,28,20,19,24</sub> | 8.8<br><sub>17,12,9,6,0</sub> |  | 2.6<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> |  | 1.3 | 0.3 | 0.8 | 12.8 |
| Collin Sexton | 98% | 21.1<br><sub>24,27,13,24,25</sub> | 13.8<br><sub>17,18,10,16,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.7 | 18.9 |
| Jarred Vanderbilt | 88% | 13.2<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.2<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.7 |
| Carson Cooper | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 8.2 |
| Kevon Looney | 52% | 10.0<br><sub>-,-,4,-,17</sub> | 2.3<br><sub>-,-,0,-,4</sub> |  | 3.9<br><sub>-,-,2,-,8</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 7.0 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.0 |
| Adou Thiero | 72% | 7.8<br><sub>8,7,14,-,6</sub> | 2.6<br><sub>2,2,2,-,0</sub> |  | 2.0<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Cameron Carr | 63% | 7.1<br><sub>-,7,13,-,-</sub> | 3.9<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.6 |
| Jaden Hardy | 48% | 7.1<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.4 |
| Chris Manon | 52% | 5.8<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.2 |
| Bronny James | 48% | 5.6<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.8 |

</details>

<details><summary>if Jaxson Hayes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 34.5<br><sub>-,39,32,36,42</sub> | 39.8<br><sub>-,32,32,43,36</sub> | 37.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>-,10,5,9,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.1<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.6 | 4.0 | 54.8 |
| Quentin Grimes (LAL) | 98% | 29.3<br><sub>32,-,-,37,42</sub> | 13.0<br><sub>12,-,-,22,47</sub> | 16.5 · –<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>1,-,-,6,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>4,-,-,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,-,-,5,10</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.3 | 1.5 | 19.6 |
| Walker Kessler (LAL) | 98% | 28.5<br><sub>29,30,29,32,-</sub> | 12.2<br><sub>12,21,10,14,-</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 11.8<br><sub>16,10,11,12,-</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>4,4,3,3,-</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 25.9 |
| Matisse Thybulle (LAL) | 98% | 24.4<br><sub>28,23,23,26,31</sub> | 7.8<br><sub>4,6,8,12,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,0,5,8,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 2.6 | 0.9 | 1.1 | 12.1 |
| Jake LaRavia (LAL) | 98% | 23.2<br><sub>29,32,21,32,23</sub> | 6.6<br><sub>5,4,0,12,4</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>1,3,9,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.7 | 1.1 | 12.6 |
| Sandro Mamukelashvili (LAL) | 99% | 22.1<br><sub>18,32,26,21,23</sub> | 10.4<br><sub>7,23,23,4,3</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,8,3,2,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.3<br><sub>1,5,5,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.5 | 0.8 | 17.0 |
| Ziaire Williams (LAL) | 98% | 21.6<br><sub>21,28,20,19,24</sub> | 8.7<br><sub>17,12,9,6,0</sub> |  | 2.6<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> |  | 1.4 | 0.3 | 0.8 | 12.8 |
| Collin Sexton (LAL) | 98% | 21.1<br><sub>24,27,13,24,25</sub> | 13.8<br><sub>17,18,10,16,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.7 | 19.0 |
| Jarred Vanderbilt (LAL) | 88% | 13.1<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.1<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Carson Cooper (LAL) | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 8.2 |
| Kevon Looney (LAL) | 52% | 9.9<br><sub>-,-,4,-,17</sub> | 2.2<br><sub>-,-,0,-,4</sub> |  | 3.9<br><sub>-,-,2,-,8</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 7.0 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| AK Okereke (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Adou Thiero (LAL) | 72% | 7.9<br><sub>8,7,14,-,6</sub> | 2.7<br><sub>2,2,2,-,0</sub> |  | 2.0<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Jaden Hardy (LAL) | 48% | 7.1<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Cameron Carr (LAL) | 63% | 7.0<br><sub>-,7,13,-,-</sub> | 3.8<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Chris Manon (LAL) | 52% | 5.9<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.3 |
| Bronny James (LAL) | 48% | 5.6<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.8 |
| Keyonte George (UTA) | 98% | 33.2<br><sub>-,33,38,34,35</sub> | 21.0<br><sub>-,13,27,13,30</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.4<br><sub>-,7,7,8,11</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 3.3 | 31.2 |
| Darryn Peterson (UTA) | 98% | 32.4<br><sub>31,33,34,34,31</sub> | 17.8<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>4,5,2,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.6 | 2.2 | 26.0 |
| Ace Bailey (UTA) | 99% | 31.2<br><sub>35,31,35,30,23</sub> | 14.5<br><sub>23,18,21,7,5</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>7,7,3,8,1</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>2,2,1,4,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.0<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.8 | 1.8 | 21.4 |
| Brice Sensabaugh (UTA) | 99% | 25.3<br><sub>14,23,27,30,35</sub> | 15.0<br><sub>5,19,7,14,40</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,3,3,7,11</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>4,1,1,2,5</sub> |  | 2.2<br><sub>1,3,1,0,8</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 2.1 | 21.0 |
| Mo Bamba (UTA) | 88% | 23.7<br><sub>17,18,20,36,31</sub> | 8.9<br><sub>7,5,9,26,15</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>7,1,9,5,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.4 | 1.1 | 17.6 |
| Josh Okogie (UTA) | 97% | 22.0<br><sub>21,15,22,27,22</sub> | 6.1<br><sub>6,7,7,7,9</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>4,3,2,6,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>4,0,1,0,4</sub> |  | 0.7<br><sub>0,1,2,2,1</sub> |  | 1.1 | 0.2 | 0.8 | 10.6 |
| Jaxson Hayes (UTA) | 100% | 21.9<br><sub>17,30,13,-,-</sub> | 8.2<br><sub>6,11,12,-,-</sub> |  | 5.2<br><sub>2,8,5,-,-</sub> |  | 1.1<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.7 | 0.8 | 1.0 | 14.6 |
| Svi Mykhailiuk (UTA) | 97% | 18.7<br><sub>21,20,7,21,33</sub> | 6.7<br><sub>7,3,0,6,8</sub> |  | 2.1<br><sub>2,0,1,2,7</sub> |  | 1.5<br><sub>3,2,0,3,5</sub> |  | 1.1<br><sub>1,1,0,2,2</sub> |  | 0.5 | 0.1 | 0.8 | 10.2 |
| Josh Green (UTA) | 96% | 17.1<br><sub>30,26,14,15,13</sub> | 3.8<br><sub>2,3,2,6,9</sub> |  | 1.6<br><sub>5,2,0,1,1</sub> |  | 0.9<br><sub>4,1,0,1,0</sub> |  | 0.4<br><sub>0,1,0,2,1</sub> |  | 0.6 | 0.1 | 0.6 | 6.3 |
| Isaiah Collier (UTA) | 63% | 15.5<br><sub>24,12,16,-,-</sub> | 7.2<br><sub>17,7,3,-,-</sub> |  | 2.2<br><sub>5,3,2,-,-</sub> |  | 4.1<br><sub>5,2,5,-,-</sub> |  | 0.4<br><sub>4,1,1,-,-</sub> |  | 0.7 | 0.2 | 1.6 | 13.5 |
| Tony Bradley (UTA) | 72% | 13.4<br><sub>14,-,12,12,17</sub> | 4.3<br><sub>4,-,0,6,3</sub> |  | 4.0<br><sub>5,-,5,2,7</sub> |  | 0.6<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.8 |
| Kyle Filipowski (UTA) | 52% | 11.5<br><sub>15,-,2,-,-</sub> | 5.7<br><sub>7,-,2,-,-</sub> |  | 3.5<br><sub>4,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.3 |
| Jonas Aidoo (UTA) | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.7 |

</details>


### PHX @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Mark Williams (PHX)

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.4<br><sub>29,29,35,28,37</sub> | 27.1<br><sub>32,17,30,17,20</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.2<br><sub>4,5,7,7,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>3,2,4,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 2.8 | 36.7 |
| Dillon Brooks | 98% | 29.0<br><sub>26,22,30,22,27</sub> | 16.1<br><sub>7,8,15,1,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 1.4 | 21.5 |
| Miles Bridges | 98% | 28.2<br><sub>26,18,25,24,29</sub> | 14.4<br><sub>7,8,11,14,16</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>5,4,6,3,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.5 | 1.2 | 23.0 |
| Jalen Green | 98% | 26.4<br><sub>24,21,21,21,27</sub> | 15.3<br><sub>6,13,12,9,16</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.3 | 2.0 | 21.9 |
| Oso Ighodaro | 98% | 24.9<br><sub>18,20,32,17,33</sub> | 6.5<br><sub>7,6,2,4,8</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 5.9<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.4 | 15.7 |
| Collin Gillespie | 98% | 24.9<br><sub>24,22,27,28,26</sub> | 10.3<br><sub>6,12,13,26,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,2,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.1 | 1.0 | 17.2 |
| Jordan Goodwin | 98% | 20.4<br><sub>-,14,24,31,20</sub> | 8.4<br><sub>-,18,6,14,11</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 44% · u 55%</sub> | 2.2<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.2 | 0.8 | 14.8 |
| Luke Kennard | 98% | 17.7<br><sub>14,22,21,23,17</sub> | 7.4<br><sub>3,14,8,18,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,1,6,2</sub> |  | 1.8<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.6 | 11.1 |
| Ryan Dunn | 98% | 15.4<br><sub>23,25,10,24,12</sub> | 4.5<br><sub>3,10,0,3,5</sub> |  | 3.3<br><sub>2,8,4,6,1</sub> |  | 1.0<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.4 | 0.5 | 8.9 |
| Khaman Maluach | 98% | 14.4<br><sub>20,22,16,13,11</sub> | 5.4<br><sub>11,11,4,7,4</sub> |  | 4.7<br><sub>5,7,2,4,6</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 10.7 |
| Rasheer Fleming | 43% | 8.5<br><sub>9,12,-,-,-</sub> | 3.2<br><sub>2,4,-,-,-</sub> |  | 1.4<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Jamaree Bouyea | 48% | 6.9<br><sub>9,8,-,-,-</sub> | 2.9<br><sub>4,7,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.0 |
| Pat Spencer | 52% | 6.8<br><sub>6,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>2,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Koa Peat | 67% | 6.6<br><sub>6,6,-,8,1</sub> | 3.3<br><sub>4,5,-,10,0</sub> |  | 1.6<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| Duop Reath | 48% | 6.4<br><sub>6,-,-,-,-</sub> | 2.8<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>2,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.5 |
| Drew Timme | 8% | 6.3 | 2.6 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 34.8<br><sub>33,39,40,35,33</sub> | 23.8<br><sub>22,32,29,17,26</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,4,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 4.0 | 34.7 |
| Domantas Sabonis | 98% | 31.0<br><sub>31,-,24,35,29</sub> | 14.5<br><sub>17,-,0,21,11</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 11.9<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 0.3<br><sub>1,-,0,1,0</sub> |  | 0.8 | 0.3 | 2.6 | 31.6 |
| Zach LaVine | 76% | 30.7<br><sub>35,25,33,36,-</sub> | 18.1<br><sub>14,15,31,12,-</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,4,3,3,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.7<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 2.5 | 24.0 |
| De'Andre Hunter | 76% | 30.5<br><sub>-,31,34,42,-</sub> | 13.7<br><sub>-,14,15,24,-</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>-,3,4,5,-</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>-,1,2,2,-</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>-,2,3,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 1.7 | 19.7 |
| Keegan Murray | 98% | 27.1<br><sub>-,23,24,40,21</sub> | 10.8<br><sub>-,10,11,16,6</sub> |  | 4.1<br><sub>-,1,2,7,1</sub> |  | 1.4<br><sub>-,2,1,4,0</sub> |  | 1.3<br><sub>-,0,2,2,2</sub> |  | 0.8 | 0.9 | 1.1 | 16.4 |
| Precious Achiuwa | 98% | 23.5<br><sub>22,36,14,-,-</sub> | 10.1<br><sub>9,7,10,-,-</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>4,14,3,-,-</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>0,2,0,-,-</sub> |  | 0.3<br><sub>1,0,1,-,-</sub> |  | 0.9 | 0.8 | 1.2 | 17.8 |
| Leaky Black | 86% | 20.1<br><sub>40,20,18,12,29</sub> | 4.8<br><sub>12,6,0,0,12</sub> |  | 3.5<br><sub>3,5,3,0,9</sub> |  | 1.3<br><sub>5,1,2,0,2</sub> |  | 0.6<br><sub>4,2,0,0,4</sub> |  | 1.0 | 0.5 | 0.6 | 9.5 |
| Malik Monk | 98% | 17.9<br><sub>18,21,3,18,29</sub> | 9.8<br><sub>12,9,1,7,14</sub> |  | 1.9<br><sub>0,2,0,4,1</sub> |  | 3.5<br><sub>7,3,0,3,10</sub> |  | 1.2<br><sub>2,0,0,0,1</sub> |  | 0.5 | 0.3 | 1.5 | 15.2 |
| Dylan Cardwell | 98% | 17.1<br><sub>15,18,29,13,19</sub> | 5.6<br><sub>9,4,1,6,10</sub> |  | 6.3<br><sub>2,9,11,3,6</sub> |  | 1.4<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 13.2 |
| Emanuel Sharp | 98% | 15.5<br><sub>31,12,19,7,21</sub> | 4.7<br><sub>9,5,2,4,9</sub> |  | 1.4<br><sub>5,1,2,0,0</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>3,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.6 | 6.9 |
| Alex Karaban | 52% | 14.1<br><sub>11,-,-,-,29</sub> | 2.9<br><sub>0,-,-,-,0</sub> |  | 2.0<br><sub>1,-,-,-,5</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.6 |
| Daeqwon Plowden | 88% | 13.4<br><sub>-,12,2,2,24</sub> | 5.4<br><sub>-,6,0,0,13</sub> |  | 1.6<br><sub>-,0,0,0,2</sub> |  | 0.6<br><sub>-,0,0,0,1</sub> |  | 0.7<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.6 |
| Mason Plumlee | 52% | 6.5<br><sub>-,-,-,-,5</sub> | 2.0<br><sub>-,-,-,-,2</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-18/`._
