# NBA model · Wed 11 Nov 2026 (US date)

Updated **Wed 11 Nov, 10:35 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-11/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| GSW to win | GSW @ HOU | draftkings | 2.96 | 2.69 | 3.20 | 31.2% | 37.2% | 37.2% | +10.1% | -7.6% | 1.3% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard AST over 13.5 (14+) | WAS @ IND | draftkings | 23.00 | 17.92 | 6.42 | 15.6% | 4.1% | 5.6% | +28.4% | +258.3% | 0.3% |
| CHI to win | SAS @ CHI | draftkings | 8.50 | 7.19 | 4.71 | 21.2% | 13.9% | 13.9% | +18.2% | +80.4% | 0.6% |
| Jaime Jaquez Jr. AST over 7.5 (8+) | LAL @ MIL | draftkings | 30.00 | 25.58 | 10.93 | 9.2% | 3.1% | 3.9% | +17.4% | +174.5% | 0.1% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ POR | draftkings | 13.80 | 12.08 | 5.49 | 18.2% | 6.8% | 8.3% | +14.3% | +151.4% | 0.3% |
| Kevin Durant AST over 7.5 (8+) | GSW @ HOU | draftkings | 17.40 | 15.38 | 7.17 | 14.0% | 5.4% | 6.5% | +13.2% | +142.7% | 0.2% |
| Pascal Siakam PTS over 39.5 (40+) | WAS @ IND | draftkings | 25.00 | 22.42 | 10.84 | 9.2% | 3.7% | 4.5% | +11.6% | +130.7% | 0.1% |
| Pascal Siakam PTS over 34.5 (35+) | WAS @ IND | draftkings | 12.40 | 11.27 | 5.68 | 17.6% | 7.5% | 8.9% | +9.9% | +118.3% | 0.2% |
| Pascal Siakam PR over 44.5 (45+) | WAS @ IND | draftkings | 15.40 | 14.01 | 7.06 | 14.2% | 6.1% | 7.1% | +9.9% | +118.1% | 0.2% |
| Dejounte Murray AST over 9.5 (10+) | BKN @ NOP | draftkings | 16.80 | 15.31 | 7.76 | 12.9% | 5.6% | 6.5% | +9.7% | +116.5% | 0.1% |
| Pascal Siakam PR over 49.5 (50+) | WAS @ IND | draftkings | 27.00 | 24.94 | 13.08 | 7.6% | 3.5% | 4.0% | +8.4% | +106.4% | 0.1% |
| Desmond Bane AST over 5.5 (6+) | ORL @ UTA | draftkings | 9.20 | 8.53 | 4.53 | 22.1% | 10.2% | 11.7% | +7.9% | +103.2% | 0.2% |
| Andrew Nembhard PA over 39.5 (40+) | WAS @ IND | draftkings | 17.40 | 16.29 | 8.93 | 11.2% | 5.4% | 6.1% | +6.8% | +94.8% | 0.1% |
| Kyle Kuzma PTS over 19.5 (20+) | LAL @ MIL | draftkings | 9.90 | 9.28 | 5.11 | 19.6% | 9.4% | 10.8% | +6.7% | +93.7% | 0.2% |
| Pascal Siakam PR over 39.5 (40+) | WAS @ IND | draftkings | 7.50 | 7.12 | 4.10 | 24.4% | 12.5% | 14.0% | +5.3% | +83.1% | 0.2% |
| Kyle Kuzma PR over 24.5 (25+) | LAL @ MIL | draftkings | 8.10 | 7.69 | 4.43 | 22.6% | 11.5% | 13.0% | +5.3% | +83.0% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| WAS @ IND | Thu 12 Nov 11:00 | 114.1–119.8 | WAS 34% | 2.90 / 1.53 | IND -5.5 | 233.5 | IND -3.5 covers 57%; o226.5 65% |
| CLE @ NYK | Thu 12 Nov 11:00 | 108.9–115.0 | CLE 33% | 3.03 / 1.49 | NYK -6.5 | 223.5 | NYK -4.5 covers 55%; o221.5 55% |
| BOS @ TOR | Thu 12 Nov 11:00 | 116.6–104.4 | BOS 81% | 1.24 / 5.16 | TOR +12.5 | 220.5 | TOR +7.5 covers 37%; o216.5 59% |
| SAS @ CHI | Thu 12 Nov 12:00 | 122.9–110.3 | SAS 81% | 1.23 / 5.39 | CHI +12.5 | 233.5 | CHI +15.5 covers 58%; o239.5 36% |
| DEN @ MEM | Thu 12 Nov 12:00 | 121.4–116.5 | DEN 64% | 1.57 / 2.77 | MEM +5.5 | 237.5 | MEM +3.5 covers 45%; o229.5 67% |
| LAL @ MIL | Thu 12 Nov 12:00 | 119.7–110.3 | LAL 75% | 1.34 / 3.97 | MIL +9.5 | 229.5 | MIL +12.5 covers 59%; o231.5 47% |
| BKN @ NOP | Thu 12 Nov 12:00 | 109.5–117.3 | BKN 29% | 3.48 / 1.40 | NOP -7.5 | 226.5 | NOP -4.5 covers 60%; o229.5 43% |
| ORL @ UTA | Thu 12 Nov 13:00 | 112.9–107.9 | ORL 64% | 1.57 / 2.75 | UTA +5.5 | 220.5 | UTA +4.5 covers 48%; o217.5 57% |
| GSW @ HOU | Thu 12 Nov 13:30 | 109.8–116.5 | GSW 32% | 3.17 / 1.46 | HOU -6.5 | 226.5 | HOU -6.5 covers 51%; o222.5 58% |
| OKC @ POR | Thu 12 Nov 14:00 | 114.3–109.7 | OKC 62% | 1.60 / 2.66 | POR +4.5 | 223.5 | POR +1.5 covers 41%; o225.5 46% |

### WAS @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.1–119.8 | WAS 34% | 2.90 / 1.53 | IND -5.5 | 233.5 | IND -3.5 covers 57%; o226.5 65% |
| Expected (weighted by chance each plays) | 113.8–120.1 | WAS 33% | 3.06 / 1.49 | IND -6.5 | 233.5 | IND -3.5 covers 59%; o226.5 65% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| T.J. McConnell (IND) | Questionable | 55% | 12.3 | 6.4 | 1.7 | 4.0 | 0.1 | 0.8 | 0.1 | 0.9 | 12.2 | small |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 34.5<br><sub>34,34,37,28,38</sub> | 19.0<br><sub>15,18,23,4,20</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,2,2,5,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 9.6<br><sub>9,6,10,3,7</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.0 | 32.0 |
| Anthony Davis | 98% | 33.3<br><sub>34,30,-,-,34</sub> | 22.5<br><sub>27,26,-,-,44</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 11.7<br><sub>9,10,-,-,13</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>1,3,-,-,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8<br><sub>1,0,-,-,2</sub> |  | 1.2 | 1.6 | 2.1 | 36.9 |
| Kyshawn George | 98% | 33.0<br><sub>37,35,39,30,35</sub> | 16.2<br><sub>22,25,33,14,12</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>4,4,4,7,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.6<br><sub>5,7,7,6,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>4,3,5,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 1.0 | 2.2 | 25.9 |
| AJ Dybantsa | 96% | 32.7<br><sub>33,32,36,31,37</sub> | 15.6<br><sub>21,9,11,19,21</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>5,6,9,6,8</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>2,3,3,3,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>1,0,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1 | 0.4 | 2.0 | 24.4 |
| Alex Sarr | 98% | 25.1<br><sub>-,23,30,28,25</sub> | 11.3<br><sub>-,11,13,15,4</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>-,9,8,14,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>-,1,3,1,0</sub> |  | 0.9<br><sub>-,0,1,1,0</sub> |  | 0.8 | 1.3 | 1.3 | 20.6 |
| Bilal Coulibaly | 98% | 22.7<br><sub>33,23,24,20,-</sub> | 8.0<br><sub>7,6,9,0,-</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>1,2,5,5,-</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>2,2,0,0,-</sub> |  | 0.7<br><sub>0,0,1,0,-</sub> |  | 1.1 | 0.7 | 1.0 | 13.1 |
| Tre Johnson | 91% | 20.8<br><sub>22,14,27,28,29</sub> | 7.6<br><sub>4,3,23,4,2</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>3,2,1,0,2</sub> |  | 1.0<br><sub>0,0,1,3,0</sub> |  | 1.1<br><sub>0,1,5,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 0.8 | 10.8 |
| Bub Carrington | 98% | 18.1<br><sub>19,19,15,21,19</sub> | 5.8<br><sub>3,0,5,9,4</sub> |  | 2.1<br><sub>4,1,1,6,0</sub> |  | 2.5<br><sub>4,2,1,1,4</sub> |  | 0.8<br><sub>1,0,1,3,1</sub> |  | 0.6 | 0.1 | 1.0 | 10.5 |
| Deandre Ayton | 98% | 14.4<br><sub>24,11,23,7,13</sub> | 5.3<br><sub>4,5,8,2,2</sub> |  | 4.9<br><sub>6,4,11,1,8</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>2,1,3,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 10.8 |
| Will Riley | 91% | 9.0<br><sub>4,13,9,20,4</sub> | 3.7<br><sub>0,0,7,5,0</sub> |  | 1.1<br><sub>0,0,0,2,0</sub> |  | 0.7<br><sub>1,0,0,1,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.6 |
| Khris Middleton | 38% | 8.8<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.1 |
| Anthony Gill | 52% | 7.0<br><sub>-,-,-,9,2</sub> | 2.4<br><sub>-,-,-,1,0</sub> |  | 1.3<br><sub>-,-,-,1,2</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Tre Mann | 63% | 6.4<br><sub>-,3,-,18,2</sub> | 2.7<br><sub>-,2,-,2,0</sub> |  | 0.8<br><sub>-,0,-,0,0</sub> |  | 0.8<br><sub>-,0,-,2,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Felix Okpara | 58% | 5.9<br><sub>-,3,-,-,2</sub> | 2.5<br><sub>-,0,-,-,2</sub> |  | 1.7<br><sub>-,1,-,-,1</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.5 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 86% | 33.5<br><sub>35,-,38,31,34</sub> | 18.7<br><sub>23,-,22,9,12</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,-,2,1,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.9<br><sub>4,-,5,8,12</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,-,2,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.2 | 2.5 | 32.0 |
| Pascal Siakam | 88% | 33.0<br><sub>36,-,30,32,35</sub> | 25.5<br><sub>17,-,20,23,29</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>5,-,4,2,9</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>5,-,2,5,8</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,-,2,2,5</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.4 | 2.3 | 38.0 |
| Aaron Nesmith | 88% | 29.7<br><sub>30,-,30,27,34</sub> | 16.2<br><sub>11,-,16,8,18</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>3,-,2,5,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>4,-,2,1,2</sub> |  | 2.2<br><sub>0,-,2,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.5 | 1.7 | 22.9 |
| Ivica Zubac | 63% | 24.5<br><sub>-,-,19,19,28</sub> | 11.9<br><sub>-,-,1,10,16</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 9.6<br><sub>-,-,4,12,3</sub> | 9.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>-,-,2,5,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.8 | 1.5 | 23.5 |
| Quenton Jackson | 98% | 23.6<br><sub>24,35,22,17,25</sub> | 11.9<br><sub>12,20,13,6,10</sub> |  | 3.6<br><sub>3,7,7,4,5</sub> |  | 4.4<br><sub>2,3,2,1,4</sub> |  | 1.0<br><sub>3,1,3,0,2</sub> |  | 1.1 | 0.2 | 1.5 | 19.9 |
| Kelly Oubre Jr. | 71% | 22.9<br><sub>20,-,-,16,23</sub> | 10.2<br><sub>11,-,-,2,14</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>2,-,-,1,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,-,-,0,2</sub> |  | 0.9<br><sub>2,-,-,0,1</sub> |  | 0.9 | 0.4 | 1.0 | 15.3 |
| Jarace Walker | 98% | 20.7<br><sub>20,45,17,20,10</sub> | 9.8<br><sub>6,15,2,9,7</sub> |  | 5.0<br><sub>6,7,8,5,1</sub> |  | 2.4<br><sub>3,3,1,2,0</sub> |  | 1.2<br><sub>2,1,0,1,2</sub> |  | 0.7 | 0.4 | 1.3 | 17.2 |
| Obi Toppin | 67% | 20.5<br><sub>-,-,19,22,19</sub> | 13.5<br><sub>-,-,11,10,10</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>-,-,5,7,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>-,-,1,2,4</sub> |  | 1.6<br><sub>-,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.3 | 1.2 | 20.9 |
| Jay Huff | 72% | 16.8<br><sub>17,40,14,10,-</sub> | 8.1<br><sub>0,22,6,0,-</sub> |  | 3.5<br><sub>3,8,3,3,-</sub> |  | 1.4<br><sub>0,2,1,0,-</sub> |  | 0.9<br><sub>0,0,2,0,-</sub> |  | 0.4 | 1.2 | 0.8 | 13.0 |
| Kobe Brown | 72% | 15.4<br><sub>15,38,7,-,-</sub> | 5.8<br><sub>3,16,0,-,-</sub> |  | 2.9<br><sub>1,6,1,-,-</sub> |  | 1.6<br><sub>1,1,0,-,-</sub> |  | 0.6<br><sub>1,2,0,-,-</sub> |  | 0.5 | 0.2 | 0.8 | 10.3 |
| Larry Nance Jr. | 93% | 13.9<br><sub>26,-,14,13,14</sub> | 4.6<br><sub>4,-,4,15,4</sub> |  | 3.0<br><sub>6,-,4,2,0</sub> |  | 1.0<br><sub>1,-,1,1,0</sub> |  | 0.5<br><sub>1,-,0,5,0</sub> |  | 0.8 | 0.2 | 0.6 | 8.6 |
| Braden Smith | 91% | 13.9<br><sub>1,42,24,12,10</sub> | 4.6<br><sub>0,19,10,0,0</sub> |  | 1.5<br><sub>0,4,1,0,0</sub> |  | 2.7<br><sub>0,10,5,2,0</sub> |  | 0.2<br><sub>0,2,0,0,0</sub> |  | 0.7 | 0.3 | 0.9 | 8.8 |
| Jalen Slawson | 72% | 13.1<br><sub>18,41,6,12,-</sub> | 4.2<br><sub>3,12,2,4,-</sub> |  | 2.7<br><sub>5,7,2,1,-</sub> |  | 1.4<br><sub>0,3,1,2,-</sub> |  | 0.3<br><sub>0,2,0,0,-</sub> |  | 0.8 | 0.6 | 0.7 | 8.3 |

</details>


### CLE @ NYK
Out: Josh Hart (NYK), Sam Merrill (CLE)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.9–115.0 | CLE 33% | 3.03 / 1.49 | NYK -6.5 | 223.5 | NYK -4.5 covers 55%; o221.5 55% |
| Expected (weighted by chance each plays) | 108.8–114.9 | CLE 33% | 3.02 / 1.49 | NYK -6.5 | 223.5 | NYK -4.5 covers 55%; o221.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaylon Tyson (CLE) | Questionable | 55% | 15.0 | 5.5 | 2.7 | 1.3 | 0.7 | 0.4 | 0.2 | 0.8 | 9.5 | small |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 34.6<br><sub>33,35,30,34,25</sub> | 15.7<br><sub>14,19,17,7,11</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,9,6,2,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>6,6,3,5,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>3,3,3,1,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.5 | 3.2 | 25.9 |
| Donovan Mitchell | 98% | 34.5<br><sub>36,33,33,37,23</sub> | 22.5<br><sub>17,27,23,37,11</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>5,3,7,4,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>11,6,8,4,4</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>4,5,1,5,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.3 | 2.8 | 31.7 |
| Evan Mobley | 98% | 32.9<br><sub>33,33,32,33,24</sub> | 15.1<br><sub>16,16,22,12,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>7,10,6,9,2</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>4,3,4,5,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,1,3,1,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 1.3 | 1.9 | 26.1 |
| Peyton Watson | 98% | 27.8<br><sub>-,-,28,29,21</sub> | 11.5<br><sub>-,-,13,12,13</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>-,-,9,6,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>-,-,2,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>-,-,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 1.1 | 1.5 | 17.7 |
| Jarrett Allen | 98% | 25.3<br><sub>28,7,-,-,19</sub> | 11.2<br><sub>14,0,-,-,12</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>6,1,-,-,7</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,-,-,1</sub> |  | 0.1<br><sub>0,0,-,-,1</sub> |  | 0.7 | 1.1 | 1.2 | 19.4 |
| Meleek Thomas | 91% | 24.7<br><sub>26,18,27,24,27</sub> | 10.1<br><sub>17,9,12,9,18</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>5,1,1,4,3</sub> |  | 1.3<br><sub>1,0,3,0,3</sub> |  | 1.7<br><sub>3,3,2,3,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.3 | 1.1 | 14.0 |
| Tyrese Proctor | 91% | 20.9<br><sub>19,22,19,23,23</sub> | 6.9<br><sub>10,11,3,7,6</sub> |  | 2.7<br><sub>4,1,6,3,1</sub> |  | 2.4<br><sub>2,0,3,3,4</sub> |  | 1.0<br><sub>2,2,0,2,0</sub> |  | 0.8 | 0.1 | 0.9 | 11.9 |
| Mario Hezonja | 98% | 19.4<br><sub>27,23,27,19,17</sub> | 7.5<br><sub>12,12,15,0,10</sub> |  | 4.7<br><sub>8,8,10,5,3</sub> |  | 1.3<br><sub>3,1,1,1,0</sub> |  | 1.0<br><sub>3,2,2,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 13.5 |
| Craig Porter Jr. | 88% | 14.2<br><sub>8,14,3,15,17</sub> | 2.9<br><sub>0,0,0,0,9</sub> |  | 2.1<br><sub>4,1,0,1,2</sub> |  | 2.0<br><sub>1,1,0,1,4</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.7 | 7.0 |
| Thomas Bryant | 80% | 13.7<br><sub>5,13,16,15,15</sub> | 6.1<br><sub>4,8,13,5,11</sub> |  | 3.1<br><sub>0,0,6,3,2</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.7<br><sub>0,1,1,1,2</sub> |  | 0.3 | 0.4 | 0.6 | 9.8 |
| Riley Minix | 52% | 12.4<br><sub>-,-,-,10,17</sub> | 4.3<br><sub>-,-,-,8,2</sub> |  | 1.9<br><sub>-,-,-,3,2</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.3 | 0.2 | 0.4 | 6.9 |
| Norchad Omier | 63% | 9.2<br><sub>-,-,3,-,12</sub> | 3.0<br><sub>-,-,0,-,0</sub> |  | 2.1<br><sub>-,-,2,-,3</sub> |  | 1.0<br><sub>-,-,1,-,2</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 6.0 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 36.2<br><sub>35,35,34,28,34</sub> | 26.8<br><sub>38,24,19,33,31</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,5,2,2,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 6.8<br><sub>7,6,6,4,9</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>6,3,4,5,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.2 | 2.5 | 36.9 |
| OG Anunoby | 98% | 35.6<br><sub>31,34,38,24,34</sub> | 18.9<br><sub>23,9,18,18,15</sub> | 16.5 · –<br><sub>o 53% · u 47%</sub> | 5.9<br><sub>6,4,4,5,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,3,2,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.5<br><sub>2,1,3,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.9 | 1.6 | 27.0 |
| Karl-Anthony Towns | 98% | 33.6<br><sub>28,35,35,25,34</sub> | 20.0<br><sub>19,22,11,17,29</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 13.9<br><sub>13,12,16,12,13</sub> | 12.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>5,3,5,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,3,1,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.7 | 2.7 | 37.8 |
| Mikal Bridges | 98% | 29.6<br><sub>13,30,16,22,31</sub> | 10.7<br><sub>3,12,6,7,9</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>0,5,2,4,6</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>0,2,0,4,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,2,0,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.5 | 0.9 | 16.7 |
| Landry Shamet | 98% | 27.9<br><sub>32,16,30,25,29</sub> | 9.8<br><sub>14,0,22,7,9</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,0,1,2,1</sub> |  | 1.6<br><sub>5,0,1,2,1</sub> |  | 1.8<br><sub>4,0,4,1,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 0.8 | 13.4 |
| Miles McBride | 98% | 19.9<br><sub>14,24,17,11,16</sub> | 6.9<br><sub>3,10,6,7,5</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>5,3,1,1,0</sub> |  | 1.4<br><sub>0,1,2,1,0</sub> |  | 1.2<br><sub>1,2,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.2 | 0.5 | 10.1 |
| Jordan Clarkson | 91% | 15.0<br><sub>17,9,11,15,15</sub> | 7.2<br><sub>18,4,7,10,9</sub> |  | 2.0<br><sub>3,3,0,1,2</sub> |  | 1.1<br><sub>1,0,0,1,0</sub> |  | 0.6<br><sub>2,0,1,2,1</sub> |  | 0.4 | 0.1 | 0.8 | 10.2 |
| Andre Drummond | 98% | 14.6<br><sub>15,12,13,12,14</sub> | 4.8<br><sub>4,3,4,6,0</sub> |  | 6.8<br><sub>11,6,9,9,8</sub> |  | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.8 | 12.6 |
| Tyler Kolek | 88% | 14.6<br><sub>18,13,5,11,14</sub> | 4.3<br><sub>9,2,2,0,0</sub> |  | 1.9<br><sub>2,1,1,0,4</sub> |  | 4.0<br><sub>9,4,1,5,5</sub> |  | 0.5<br><sub>3,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.2 |
| Jose Alvarado | 67% | 13.3<br><sub>-,-,9,9,-</sub> | 4.7<br><sub>-,-,0,0,-</sub> |  | 1.7<br><sub>-,-,0,0,-</sub> |  | 2.1<br><sub>-,-,0,2,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.7 | 0.1 | 0.8 | 8.4 |
| Mohamed Diawara | 63% | 12.2<br><sub>-,-,6,21,14</sub> | 3.9<br><sub>-,-,0,8,2</sub> |  | 2.1<br><sub>-,-,1,6,3</sub> |  | 1.2<br><sub>-,-,0,4,3</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.3 |
| Dalton Knecht | 58% | 8.8<br><sub>-,-,-,16,5</sub> | 3.4<br><sub>-,-,-,10,0</sub> |  | 1.7<br><sub>-,-,-,7,0</sub> |  | 0.5<br><sub>-,-,-,1,0</sub> |  | 0.4<br><sub>-,-,-,2,0</sub> |  | 0.2 | 0.2 | 0.2 | 5.6 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Jaden Akins | 38% | 7.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.2 |
| James Wiseman | 52% | 7.8<br><sub>-,-,-,10,-</sub> | 2.5<br><sub>-,-,-,8,-</sub> |  | 2.5<br><sub>-,-,-,8,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.1 | 0.4 | 0.5 | 5.4 |
| Pacome Dadiet | 38% | 7.7<br><sub>-,-,-,9,-</sub> | 2.7<br><sub>-,-,-,4,-</sub> |  | 1.4<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |

</details>


### BOS @ TOR
Out: Scottie Barnes (TOR), Kawhi Leonard (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.6–104.4 | BOS 81% | 1.24 / 5.16 | TOR +12.5 | 220.5 | TOR +7.5 covers 37%; o216.5 59% |
| Expected (weighted by chance each plays) | 115.3–106.2 | BOS 73% | 1.37 / 3.74 | TOR +8.5 | 221.5 | TOR +7.5 covers 46%; o216.5 61% |
| if Immanuel Quickley plays | 114.9–106.3 | BOS 73% | 1.37 / 3.69 | TOR +8.5 | 221.5 | TOR +7.5 covers 47%; o216.5 60% |
| if Collin Murray-Boyles plays | 115.7–105.2 | BOS 77% | 1.30 / 4.35 | TOR +10.5 | 220.5 | TOR +7.5 covers 41%; o216.5 59% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Immanuel Quickley (TOR) | Questionable | 55% | 33.4 | 17.9 | 4.0 | 6.7 | 2.8 | 1.1 | 0.1 | 1.6 | 28.6 | full tables below |
| Trayce Jackson-Davis (TOR) | Questionable | 55% | 17.1 | 6.1 | 5.5 | 1.1 | 0.1 | 0.7 | 0.7 | 0.7 | 12.7 | small |
| Collin Murray-Boyles (TOR) | Questionable | 55% | 30.0 | 13.7 | 6.6 | 2.7 | 0.5 | 1.1 | 0.8 | 2.0 | 23.0 | full tables below |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 33.9<br><sub>34,32,-,29,29</sub> | 26.0<br><sub>32,19,-,34,21</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>4,6,-,8,4</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>7,9,-,9,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,1,-,5,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.4 | 3.0 | 40.2 |
| Paul George | 98% | 30.8<br><sub>33,-,35,22,28</sub> | 18.7<br><sub>17,-,25,8,27</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>6,-,3,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>8,-,5,1,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>3,-,5,2,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.5 | 2.6 | 26.6 |
| Derrick White | 98% | 30.7<br><sub>34,30,36,25,27</sub> | 13.3<br><sub>12,7,24,18,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,2,4,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>2,3,7,5,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,1,1,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 1.0 | 1.9 | 21.2 |
| Payton Pritchard | 98% | 26.7<br><sub>27,30,18,23,29</sub> | 13.0<br><sub>7,4,10,12,12</sub> |  | 3.1<br><sub>7,3,1,6,5</sub> |  | 3.7<br><sub>3,3,5,5,4</sub> |  | 1.9<br><sub>0,0,0,4,4</sub> |  | 0.7 | 0.1 | 1.3 | 19.8 |
| Neemias Queta | 98% | 21.8<br><sub>27,26,29,15,22</sub> | 9.2<br><sub>8,16,9,4,13</sub> |  | 7.1<br><sub>8,6,12,3,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,1,3,1,4</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.1 | 1.1 | 17.6 |
| Sam Hauser | 98% | 21.4<br><sub>17,19,30,17,23</sub> | 7.7<br><sub>3,2,11,9,7</sub> |  | 3.0<br><sub>2,2,2,3,3</sub> |  | 1.0<br><sub>0,1,0,3,1</sub> |  | 1.4<br><sub>1,0,3,3,1</sub> |  | 0.4 | 0.2 | 0.4 | 11.8 |
| Baylor Scheierman | 98% | 18.9<br><sub>20,27,29,15,19</sub> | 6.1<br><sub>10,11,9,5,7</sub> |  | 3.4<br><sub>2,5,11,4,1</sub> |  | 1.2<br><sub>1,2,1,2,0</sub> |  | 0.9<br><sub>2,3,3,1,1</sub> |  | 0.6 | 0.1 | 0.7 | 10.7 |
| Mitchell Robinson | 98% | 16.7<br><sub>-,15,20,15,18</sub> | 5.3<br><sub>-,4,3,6,12</sub> |  | 6.3<br><sub>-,4,10,7,7</sub> |  | 0.6<br><sub>-,0,1,0,2</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.8 | 12.3 |
| Luka Garza | 98% | 12.5<br><sub>21,18,18,19,9</sub> | 6.1<br><sub>12,14,11,6,4</sub> |  | 3.1<br><sub>6,3,5,7,5</sub> |  | 0.8<br><sub>4,0,2,4,0</sub> |  | 0.6<br><sub>2,4,3,2,0</sub> |  | 0.3 | 0.3 | 0.7 | 10.1 |
| Jordan Walsh | 98% | 12.4<br><sub>13,12,12,22,11</sub> | 3.4<br><sub>0,5,3,6,0</sub> |  | 2.5<br><sub>3,3,4,3,3</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.3<br><sub>0,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Hugo Gonzalez | 97% | 10.2<br><sub>14,16,14,15,10</sub> | 3.1<br><sub>7,6,4,8,0</sub> |  | 2.0<br><sub>1,3,2,1,2</sub> |  | 0.4<br><sub>1,0,0,0,1</sub> |  | 0.2<br><sub>1,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.6 |
| Devin Carter | 16% | 8.5 | 3.6 |  | 1.6 |  | 1.1 |  | 0.3 |  | 0.4 | 0.1 | 0.7 | 6.2 |
| Mike Conley | 58% | 7.8<br><sub>-,4,-,11,10</sub> | 2.2<br><sub>-,3,-,0,3</sub> |  | 0.8<br><sub>-,0,-,0,3</sub> |  | 1.0<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,1,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.0 |
| Dillon Mitchell | 52% | 6.5<br><sub>-,2,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 0.9 |
| Ron Harper Jr. | 64% | 6.3<br><sub>-,7,-,10,4</sub> | 2.7<br><sub>-,0,-,3,2</sub> |  | 0.8<br><sub>-,1,-,0,0</sub> |  | 0.5<br><sub>-,1,-,2,0</sub> |  | 0.3<br><sub>-,0,-,1,0</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |
| Chris Cenac Jr. | 52% | 5.9<br><sub>-,2,-,-,-</sub> | 2.8<br><sub>-,2,-,-,-</sub> |  | 1.5<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.1 | 0.7 | 4.7 |
| Amari Williams | 30% | 4.9<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 3.2 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 36.8<br><sub>32,37,33,37,36</sub> | 24.2<br><sub>22,26,22,27,19</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>10,6,5,7,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>5,3,3,5,2</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>4,2,3,0,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.4 | 3.1 | 35.7 |
| Jamal Shead | 98% | 33.6<br><sub>25,20,20,34,36</sub> | 12.3<br><sub>9,6,3,10,20</sub> |  | 2.6<br><sub>2,1,3,3,2</sub> |  | 9.5<br><sub>6,6,6,16,11</sub> |  | 1.7<br><sub>2,0,1,1,4</sub> |  | 1.2 | 0.2 | 2.7 | 24.5 |
| Ja'Kobe Walter | 98% | 33.4<br><sub>33,35,27,29,34</sub> | 14.0<br><sub>11,10,8,7,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>4,6,1,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>2,5,2,2,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.4<br><sub>3,0,1,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 1.2 | 20.9 |
| Jamison Battle | 98% | 30.8<br><sub>17,21,19,21,29</sub> | 14.6<br><sub>20,12,9,6,18</sub> |  | 4.0<br><sub>5,0,1,2,1</sub> |  | 1.5<br><sub>0,0,0,0,2</sub> |  | 2.8<br><sub>4,4,2,1,5</sub> |  | 0.4 | 0.2 | 1.1 | 20.1 |
| Jakob Poeltl | 88% | 27.6<br><sub>-,-,19,31,31</sub> | 12.2<br><sub>-,-,8,19,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>-,-,5,11,8</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>-,-,1,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.8 | 0.9 | 1.7 | 22.4 |
| Alijah Martin | 91% | 24.2<br><sub>16,6,9,31,21</sub> | 9.9<br><sub>5,2,6,27,2</sub> |  | 3.2<br><sub>2,2,1,4,3</sub> |  | 2.5<br><sub>4,0,0,1,3</sub> |  | 1.2<br><sub>1,0,0,6,0</sub> |  | 0.9 | 0.4 | 1.6 | 15.7 |
| Allen Graves | 98% | 23.4<br><sub>10,7,14,16,13</sub> | 7.7<br><sub>3,0,5,3,3</sub> |  | 3.8<br><sub>0,0,1,2,2</sub> |  | 1.5<br><sub>0,2,1,0,1</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> |  | 0.6 | 0.5 | 0.6 | 13.0 |
| Kyle Anderson | 67% | 19.9<br><sub>4,8,4,-,16</sub> | 5.7<br><sub>2,2,2,-,6</sub> |  | 3.6<br><sub>3,0,0,-,2</sub> |  | 3.2<br><sub>3,0,1,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.8 | 0.5 | 1.0 | 12.4 |
| Malachi Smith | 91% | 19.9<br><sub>-,-,-,-,1</sub> | 6.2<br><sub>-,-,-,-,0</sub> |  | 3.0<br><sub>-,-,-,-,0</sub> |  | 2.6<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.8 | 11.8 |
| Jaden Bradley | 80% | 14.2<br><sub>4,-,4,8,9</sub> | 4.6<br><sub>3,-,2,3,0</sub> |  | 2.2<br><sub>1,-,1,0,1</sub> |  | 2.2<br><sub>2,-,0,1,3</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.3 | 0.9 | 9.0 |
| Kevin McCullar Jr. | 16% | 13.9<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.7 | 8.2 |

</details>

<details><summary>if Immanuel Quickley plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 33.9<br><sub>34,32,-,29,29</sub> | 25.7<br><sub>32,19,-,34,21</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>4,6,-,8,4</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>7,9,-,9,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,1,-,5,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.4 | 3.0 | 39.8 |
| Paul George (BOS) | 98% | 30.9<br><sub>33,-,35,22,28</sub> | 18.8<br><sub>17,-,25,8,27</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>6,-,3,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>8,-,5,1,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>3,-,5,2,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.5 | 2.6 | 26.7 |
| Derrick White (BOS) | 98% | 30.7<br><sub>34,30,36,25,27</sub> | 13.3<br><sub>12,7,24,18,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>2,2,4,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>2,3,7,5,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,1,1,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 1.0 | 1.9 | 21.2 |
| Payton Pritchard (BOS) | 98% | 26.8<br><sub>27,30,18,23,29</sub> | 12.9<br><sub>7,4,10,12,12</sub> |  | 3.2<br><sub>7,3,1,6,5</sub> |  | 3.7<br><sub>3,3,5,5,4</sub> |  | 1.9<br><sub>0,0,0,4,4</sub> |  | 0.7 | 0.1 | 1.3 | 19.8 |
| Neemias Queta (BOS) | 98% | 21.6<br><sub>27,26,29,15,22</sub> | 9.1<br><sub>8,16,9,4,13</sub> |  | 7.0<br><sub>8,6,12,3,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,1,3,1,4</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.0 | 1.1 | 17.4 |
| Sam Hauser (BOS) | 98% | 21.4<br><sub>17,19,30,17,23</sub> | 7.7<br><sub>3,2,11,9,7</sub> |  | 3.1<br><sub>2,2,2,3,3</sub> |  | 1.0<br><sub>0,1,0,3,1</sub> |  | 1.4<br><sub>1,0,3,3,1</sub> |  | 0.4 | 0.2 | 0.4 | 11.7 |
| Baylor Scheierman (BOS) | 98% | 18.9<br><sub>20,27,29,15,19</sub> | 6.0<br><sub>10,11,9,5,7</sub> |  | 3.4<br><sub>2,5,11,4,1</sub> |  | 1.2<br><sub>1,2,1,2,0</sub> |  | 0.9<br><sub>2,3,3,1,1</sub> |  | 0.6 | 0.1 | 0.7 | 10.5 |
| Mitchell Robinson (BOS) | 98% | 16.6<br><sub>-,15,20,15,18</sub> | 5.3<br><sub>-,4,3,6,12</sub> |  | 6.4<br><sub>-,4,10,7,7</sub> |  | 0.6<br><sub>-,0,1,0,2</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.8 | 12.3 |
| Luka Garza (BOS) | 98% | 12.6<br><sub>21,18,18,19,9</sub> | 6.1<br><sub>12,14,11,6,4</sub> |  | 3.1<br><sub>6,3,5,7,5</sub> |  | 0.9<br><sub>4,0,2,4,0</sub> |  | 0.6<br><sub>2,4,3,2,0</sub> |  | 0.3 | 0.3 | 0.7 | 10.1 |
| Jordan Walsh (BOS) | 98% | 12.6<br><sub>13,12,12,22,11</sub> | 3.4<br><sub>0,5,3,6,0</sub> |  | 2.6<br><sub>3,3,4,3,3</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.3<br><sub>0,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.6 |
| Hugo Gonzalez (BOS) | 97% | 10.2<br><sub>14,16,14,15,10</sub> | 3.1<br><sub>7,6,4,8,0</sub> |  | 2.0<br><sub>1,3,2,1,2</sub> |  | 0.4<br><sub>1,0,0,0,1</sub> |  | 0.2<br><sub>1,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.6 |
| Devin Carter (BOS) | 16% | 8.8 | 3.7 |  | 1.6 |  | 1.1 |  | 0.3 |  | 0.5 | 0.1 | 0.8 | 6.4 |
| Mike Conley (BOS) | 58% | 7.7<br><sub>-,4,-,11,10</sub> | 2.1<br><sub>-,3,-,0,3</sub> |  | 0.8<br><sub>-,0,-,0,3</sub> |  | 0.9<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,1,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |
| Dillon Mitchell (BOS) | 52% | 6.6<br><sub>-,2,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 0.9 |
| Ron Harper Jr. (BOS) | 64% | 6.3<br><sub>-,7,-,10,4</sub> | 2.6<br><sub>-,0,-,3,2</sub> |  | 0.8<br><sub>-,1,-,0,0</sub> |  | 0.5<br><sub>-,1,-,2,0</sub> |  | 0.3<br><sub>-,0,-,1,0</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |
| Chris Cenac Jr. (BOS) | 52% | 5.8<br><sub>-,2,-,-,-</sub> | 2.8<br><sub>-,2,-,-,-</sub> |  | 1.4<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.7 | 4.6 |
| Amari Williams (BOS) | 30% | 5.0<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 3.3 |
| RJ Barrett (TOR) | 98% | 36.6<br><sub>32,37,33,37,36</sub> | 23.7<br><sub>22,26,22,27,19</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>10,6,5,7,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>5,3,3,5,2</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>4,2,3,0,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.4 | 2.8 | 34.4 |
| Immanuel Quickley (TOR) | 100% | 33.4<br><sub>33,38,32,-,-</sub> | 17.9<br><sub>12,27,13,-,-</sub> | 18.5 · – | 4.0<br><sub>6,4,1,-,-</sub> | 3.5 | 6.7<br><sub>7,2,7,-,-</sub> | 6.5 | 2.8<br><sub>3,1,2,-,-</sub> | 2.5 | 1.1 | 0.1 | 1.6 | 28.6 |
| Ja'Kobe Walter (TOR) | 98% | 32.5<br><sub>33,35,27,29,34</sub> | 12.2<br><sub>11,10,8,7,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,6,1,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>2,5,2,2,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.2<br><sub>3,0,1,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 1.0 | 18.5 |
| Jamal Shead (TOR) | 98% | 32.0<br><sub>25,20,20,34,36</sub> | 10.8<br><sub>9,6,3,10,20</sub> |  | 2.4<br><sub>2,1,3,3,2</sub> |  | 7.8<br><sub>6,6,6,16,11</sub> |  | 1.6<br><sub>2,0,1,1,4</sub> |  | 1.2 | 0.2 | 2.2 | 21.0 |
| Jamison Battle (TOR) | 98% | 28.1<br><sub>17,21,19,21,29</sub> | 12.4<br><sub>20,12,9,6,18</sub> |  | 3.6<br><sub>5,0,1,2,1</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 2.3<br><sub>4,4,2,1,5</sub> |  | 0.4 | 0.2 | 0.9 | 17.3 |
| Jakob Poeltl (TOR) | 88% | 27.2<br><sub>-,-,19,31,31</sub> | 11.0<br><sub>-,-,8,19,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>-,-,5,11,8</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>-,-,1,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.8 | 0.8 | 1.5 | 20.7 |
| Allen Graves (TOR) | 98% | 19.0<br><sub>10,7,14,16,13</sub> | 6.0<br><sub>3,0,5,3,3</sub> |  | 3.0<br><sub>0,0,1,2,2</sub> |  | 1.2<br><sub>0,2,1,0,1</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.5 | 10.2 |
| Alijah Martin (TOR) | 91% | 18.5<br><sub>16,6,9,31,21</sub> | 6.9<br><sub>5,2,6,27,2</sub> |  | 2.5<br><sub>2,2,1,4,3</sub> |  | 1.8<br><sub>4,0,0,1,3</sub> |  | 0.8<br><sub>1,0,0,6,0</sub> |  | 0.7 | 0.3 | 1.1 | 11.2 |
| Kyle Anderson (TOR) | 67% | 16.7<br><sub>4,8,4,-,16</sub> | 4.6<br><sub>2,2,2,-,6</sub> |  | 3.0<br><sub>3,0,0,-,2</sub> |  | 2.6<br><sub>3,0,1,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.5 | 0.7 | 10.2 |
| Malachi Smith (TOR) | 91% | 16.1<br><sub>-,-,-,-,1</sub> | 4.8<br><sub>-,-,-,-,0</sub> |  | 2.4<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 9.2 |
| Jaden Bradley (TOR) | 80% | 9.8<br><sub>4,-,4,8,9</sub> | 3.1<br><sub>3,-,2,3,0</sub> |  | 1.5<br><sub>1,-,1,0,1</sub> |  | 1.5<br><sub>2,-,0,1,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 6.1 |
| Kevin McCullar Jr. (TOR) | 16% | 9.8<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |

</details>

<details><summary>if Collin Murray-Boyles plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 33.9<br><sub>34,32,-,29,29</sub> | 25.9<br><sub>32,19,-,34,21</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>4,6,-,8,4</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>7,9,-,9,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,1,-,5,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.5 | 3.0 | 40.1 |
| Paul George (BOS) | 98% | 30.8<br><sub>33,-,35,22,28</sub> | 18.6<br><sub>17,-,25,8,27</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>6,-,3,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>8,-,5,1,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>3,-,5,2,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.5 | 2.6 | 26.5 |
| Derrick White (BOS) | 98% | 30.7<br><sub>34,30,36,25,27</sub> | 13.3<br><sub>12,7,24,18,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,2,4,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>2,3,7,5,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,1,1,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 1.0 | 1.9 | 21.2 |
| Payton Pritchard (BOS) | 98% | 26.7<br><sub>27,30,18,23,29</sub> | 12.9<br><sub>7,4,10,12,12</sub> |  | 3.1<br><sub>7,3,1,6,5</sub> |  | 3.7<br><sub>3,3,5,5,4</sub> |  | 1.9<br><sub>0,0,0,4,4</sub> |  | 0.7 | 0.1 | 1.4 | 19.7 |
| Neemias Queta (BOS) | 98% | 21.7<br><sub>27,26,29,15,22</sub> | 9.1<br><sub>8,16,9,4,13</sub> |  | 7.0<br><sub>8,6,12,3,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,1,3,1,4</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.0 | 1.1 | 17.4 |
| Sam Hauser (BOS) | 98% | 21.3<br><sub>17,19,30,17,23</sub> | 7.7<br><sub>3,2,11,9,7</sub> |  | 3.0<br><sub>2,2,2,3,3</sub> |  | 1.0<br><sub>0,1,0,3,1</sub> |  | 1.4<br><sub>1,0,3,3,1</sub> |  | 0.4 | 0.2 | 0.4 | 11.8 |
| Baylor Scheierman (BOS) | 98% | 19.1<br><sub>20,27,29,15,19</sub> | 6.1<br><sub>10,11,9,5,7</sub> |  | 3.4<br><sub>2,5,11,4,1</sub> |  | 1.2<br><sub>1,2,1,2,0</sub> |  | 0.9<br><sub>2,3,3,1,1</sub> |  | 0.6 | 0.1 | 0.7 | 10.7 |
| Mitchell Robinson (BOS) | 98% | 16.6<br><sub>-,15,20,15,18</sub> | 5.3<br><sub>-,4,3,6,12</sub> |  | 6.3<br><sub>-,4,10,7,7</sub> |  | 0.6<br><sub>-,0,1,0,2</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.8 | 12.2 |
| Jordan Walsh (BOS) | 98% | 12.6<br><sub>13,12,12,22,11</sub> | 3.4<br><sub>0,5,3,6,0</sub> |  | 2.6<br><sub>3,3,4,3,3</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.3<br><sub>0,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.6 |
| Luka Garza (BOS) | 98% | 12.5<br><sub>21,18,18,19,9</sub> | 6.0<br><sub>12,14,11,6,4</sub> |  | 3.1<br><sub>6,3,5,7,5</sub> |  | 0.9<br><sub>4,0,2,4,0</sub> |  | 0.6<br><sub>2,4,3,2,0</sub> |  | 0.3 | 0.3 | 0.7 | 9.9 |
| Hugo Gonzalez (BOS) | 97% | 10.1<br><sub>14,16,14,15,10</sub> | 3.1<br><sub>7,6,4,8,0</sub> |  | 2.0<br><sub>1,3,2,1,2</sub> |  | 0.4<br><sub>1,0,0,0,1</sub> |  | 0.2<br><sub>1,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.5 |
| Devin Carter (BOS) | 16% | 8.6 | 3.5 |  | 1.6 |  | 1.1 |  | 0.3 |  | 0.4 | 0.1 | 0.7 | 6.2 |
| Mike Conley (BOS) | 58% | 7.7<br><sub>-,4,-,11,10</sub> | 2.1<br><sub>-,3,-,0,3</sub> |  | 0.8<br><sub>-,0,-,0,3</sub> |  | 1.0<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,1,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 3.9 |
| Dillon Mitchell (BOS) | 52% | 6.5<br><sub>-,2,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 0.9 |
| Ron Harper Jr. (BOS) | 64% | 6.4<br><sub>-,7,-,10,4</sub> | 2.7<br><sub>-,0,-,3,2</sub> |  | 0.8<br><sub>-,1,-,0,0</sub> |  | 0.5<br><sub>-,1,-,2,0</sub> |  | 0.3<br><sub>-,0,-,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Chris Cenac Jr. (BOS) | 52% | 5.9<br><sub>-,2,-,-,-</sub> | 2.7<br><sub>-,2,-,-,-</sub> |  | 1.4<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.1 | 0.7 | 4.6 |
| Amari Williams (BOS) | 30% | 5.0<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 3.4 |
| RJ Barrett (TOR) | 98% | 36.7<br><sub>32,37,33,37,36</sub> | 23.9<br><sub>22,26,22,27,19</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>10,6,5,7,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>5,3,3,5,2</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>4,2,3,0,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.4 | 3.0 | 35.1 |
| Ja'Kobe Walter (TOR) | 98% | 33.7<br><sub>33,35,27,29,34</sub> | 13.5<br><sub>11,10,8,7,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>4,6,1,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,5,2,2,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.4<br><sub>3,0,1,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 1.2 | 20.1 |
| Jamal Shead (TOR) | 98% | 33.3<br><sub>25,20,20,34,36</sub> | 11.6<br><sub>9,6,3,10,20</sub> |  | 2.5<br><sub>2,1,3,3,2</sub> |  | 8.6<br><sub>6,6,6,16,11</sub> |  | 1.7<br><sub>2,0,1,1,4</sub> |  | 1.2 | 0.2 | 2.4 | 22.7 |
| Collin Murray-Boyles (TOR) | 100% | 30.0<br><sub>20,28,23,34,-</sub> | 13.7<br><sub>4,18,13,19,-</sub> | 11.5 · – | 6.6<br><sub>3,7,3,7,-</sub> | 5.5 | 2.7<br><sub>1,0,2,2,-</sub> | 1.5 | 0.5<br><sub>0,1,1,0,-</sub> |  | 1.1 | 0.8 | 2.0 | 23.0 |
| Jamison Battle (TOR) | 98% | 28.6<br><sub>17,21,19,21,29</sub> | 12.6<br><sub>20,12,9,6,18</sub> |  | 3.5<br><sub>5,0,1,2,1</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 2.5<br><sub>4,4,2,1,5</sub> |  | 0.4 | 0.2 | 0.9 | 17.5 |
| Jakob Poeltl (TOR) | 88% | 27.5<br><sub>-,-,19,31,31</sub> | 11.0<br><sub>-,-,8,19,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>-,-,5,11,8</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>-,-,1,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.9 | 0.8 | 1.6 | 21.0 |
| Alijah Martin (TOR) | 91% | 21.2<br><sub>16,6,9,31,21</sub> | 7.8<br><sub>5,2,6,27,2</sub> |  | 2.8<br><sub>2,2,1,4,3</sub> |  | 2.2<br><sub>4,0,0,1,3</sub> |  | 0.9<br><sub>1,0,0,6,0</sub> |  | 0.8 | 0.4 | 1.3 | 12.9 |
| Allen Graves (TOR) | 98% | 19.5<br><sub>10,7,14,16,13</sub> | 6.2<br><sub>3,0,5,3,3</sub> |  | 3.1<br><sub>0,0,1,2,2</sub> |  | 1.2<br><sub>0,2,1,0,1</sub> |  | 0.8<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.5 | 10.5 |
| Kyle Anderson (TOR) | 67% | 16.7<br><sub>4,8,4,-,16</sub> | 4.6<br><sub>2,2,2,-,6</sub> |  | 3.0<br><sub>3,0,0,-,2</sub> |  | 2.6<br><sub>3,0,1,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.4 | 0.8 | 10.2 |
| Malachi Smith (TOR) | 91% | 16.7<br><sub>-,-,-,-,1</sub> | 5.0<br><sub>-,-,-,-,0</sub> |  | 2.5<br><sub>-,-,-,-,0</sub> |  | 2.2<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.7 |
| Jaden Bradley (TOR) | 80% | 11.3<br><sub>4,-,4,8,9</sub> | 3.7<br><sub>3,-,2,3,0</sub> |  | 1.6<br><sub>1,-,1,0,1</sub> |  | 1.8<br><sub>2,-,0,1,3</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 7.1 |
| Kevin McCullar Jr. (TOR) | 16% | 11.3<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.6 | 6.4 |

</details>


### SAS @ CHI
Out: Jaylin Sellers (CHI), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 122.9–110.3 | SAS 81% | 1.23 / 5.39 | CHI +12.5 | 233.5 | CHI +15.5 covers 58%; o239.5 36% |
| Expected (weighted by chance each plays) | 123.1–112.1 | SAS 79% | 1.27 / 4.71 | CHI +10.5 | 235.5 | CHI +15.5 covers 62%; o239.5 40% |
| if Norman Powell plays | 122.8–111.0 | SAS 80% | 1.25 / 4.99 | CHI +11.5 | 233.5 | CHI +15.5 covers 60%; o239.5 38% |
| if Devin Vassell plays | 123.5–110.8 | SAS 82% | 1.22 / 5.50 | CHI +12.5 | 234.5 | CHI +15.5 covers 57%; o239.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tobe Awaka (CHI) | Questionable | 55% | 8.7 | 3.0 | 3.4 | 0.5 | 0.0 | 0.2 | 0.4 | 0.4 | 6.9 | small |
| Norman Powell (CHI) | Questionable | 55% | 28.5 | 17.3 | 3.2 | 2.1 | 2.0 | 1.0 | 0.2 | 1.8 | 22.6 | full tables below |
| Devin Vassell (SAS) | Questionable | 55% | 30.5 | 13.0 | 4.3 | 2.9 | 2.0 | 1.4 | 0.4 | 1.0 | 20.2 | full tables below |
| Zach Collins (CHI) | Questionable | 55% | 9.7 | 3.9 | 2.8 | 0.9 | 0.2 | 0.2 | 0.3 | 0.5 | 7.6 | small |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 32.5<br><sub>27,36,28,28,26</sub> | 18.4<br><sub>17,21,19,13,17</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>7,5,2,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>8,0,3,3,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 1.9 | 28.7 |
| Victor Wembanyama | 98% | 31.8<br><sub>24,34,26,24,25</sub> | 31.0<br><sub>12,52,30,29,40</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 13.0<br><sub>11,24,14,7,11</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,2,2,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 3.7 | 2.5 | 47.3 |
| Stephon Castle | 98% | 31.6<br><sub>26,35,28,24,30</sub> | 18.3<br><sub>16,17,19,14,4</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>5,10,3,7,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.7<br><sub>4,3,7,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 2.9 | 30.7 |
| De'Aaron Fox | 98% | 31.5<br><sub>22,33,26,22,29</sub> | 16.3<br><sub>12,10,9,8,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>2,3,2,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>3,4,4,6,6</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,0,0,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 2.1 | 26.6 |
| Julian Champagnie | 98% | 27.2<br><sub>22,21,22,21,27</sub> | 10.2<br><sub>8,0,8,14,11</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>6,4,7,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,3,2,0,2</sub> |  | 1.9<br><sub>2,0,2,4,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 0.7 | 16.8 |
| Keldon Johnson | 98% | 26.2<br><sub>27,19,27,27,26</sub> | 11.2<br><sub>15,4,3,10,4</sub> |  | 5.8<br><sub>7,5,6,7,5</sub> |  | 1.9<br><sub>1,2,6,4,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 18.9 |
| Harrison Barnes | 86% | 18.8<br><sub>21,13,19,19,21</sub> | 6.9<br><sub>13,4,13,5,11</sub> |  | 2.2<br><sub>0,2,1,3,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>3,1,2,1,2</sub> |  | 0.5 | 0.2 | 0.5 | 10.0 |
| Luke Kornet | 98% | 17.1<br><sub>17,14,18,15,13</sub> | 4.4<br><sub>8,2,2,6,2</sub> |  | 5.3<br><sub>5,1,6,4,4</sub> |  | 1.1<br><sub>2,2,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.5 | 10.8 |
| Carter Bryant | 88% | 14.1<br><sub>14,-,3,17,14</sub> | 4.8<br><sub>3,-,0,6,8</sub> |  | 2.3<br><sub>0,-,0,4,1</sub> |  | 0.9<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>1,-,0,2,2</sub> |  | 0.3 | 0.4 | 0.6 | 7.9 |
| Jordan McLaughlin | 67% | 13.3<br><sub>8,-,8,12,11</sub> | 3.9<br><sub>0,-,2,3,4</sub> |  | 1.8<br><sub>1,-,2,0,4</sub> |  | 2.0<br><sub>3,-,1,0,2</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 1.0 | 0.1 | 0.6 | 7.7 |
| Tarris Reed Jr. | 67% | 10.0<br><sub>7,-,3,9,9</sub> | 3.6<br><sub>4,-,0,2,4</sub> |  | 4.1<br><sub>7,-,1,3,3</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.7 | 8.2 |
| David Jones Garcia | 64% | 8.2<br><sub>-,-,3,-,8</sub> | 3.3<br><sub>-,-,0,-,2</sub> |  | 1.6<br><sub>-,-,0,-,0</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.2 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson | 98% | 34.0<br><sub>38,31,34,22,32</sub> | 19.8<br><sub>20,23,24,5,18</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>6,5,7,5,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>4,4,4,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>3,6,4,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.8 | 2.7 | 28.9 |
| Josh Giddey | 98% | 31.6<br><sub>31,25,32,27,34</sub> | 14.1<br><sub>10,13,13,10,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>8,4,4,1,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 9.3<br><sub>11,5,10,6,15</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.6 | 2.8 | 30.4 |
| Matas Buzelis | 98% | 28.7<br><sub>33,20,23,26,31</sub> | 14.8<br><sub>17,14,4,12,19</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>5,5,3,5,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,1,2,3,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>3,2,0,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 1.2 | 2.0 | 22.3 |
| Jalen Smith | 98% | 26.6<br><sub>30,27,28,7,30</sub> | 12.4<br><sub>17,5,13,3,17</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>11,12,7,2,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>5,1,4,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.5 | 1.1 | 1.1 | 22.1 |
| Patrick Williams | 58% | 24.0<br><sub>-,-,-,20,25</sub> | 8.1<br><sub>-,-,-,4,7</sub> |  | 3.2<br><sub>-,-,-,0,3</sub> |  | 1.8<br><sub>-,-,-,2,3</sub> |  | 1.1<br><sub>-,-,-,0,1</sub> |  | 0.7 | 0.4 | 1.0 | 13.0 |
| Isaac Okoro | 98% | 22.2<br><sub>18,18,21,15,25</sub> | 7.3<br><sub>7,6,4,6,12</sub> |  | 2.2<br><sub>0,3,1,1,2</sub> |  | 1.3<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>1,1,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 10.8 |
| Tre Jones | 98% | 19.3<br><sub>18,20,19,18,14</sub> | 10.4<br><sub>11,12,8,14,6</sub> |  | 2.7<br><sub>4,4,3,3,1</sub> |  | 3.6<br><sub>3,4,3,4,1</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.2 | 1.1 | 16.7 |
| Nic Claxton | 96% | 19.1<br><sub>-,-,-,-,18</sub> | 7.4<br><sub>-,-,-,-,4</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>-,-,-,-,4</sub> | 5.5<br><sub>o 42% · u 57%</sub> | 2.2<br><sub>-,-,-,-,4</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.8 | 1.0 | 14.7 |
| Leonard Miller | 72% | 15.5<br><sub>17,11,9,19,-</sub> | 6.8<br><sub>10,2,2,4,-</sub> |  | 3.7<br><sub>0,2,3,6,-</sub> |  | 0.8<br><sub>1,1,0,3,-</sub> |  | 0.6<br><sub>1,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 11.4 |
| Noa Essengue | 91% | 14.3<br><sub>10,16,14,14,15</sub> | 5.7<br><sub>3,10,8,6,10</sub> |  | 3.2<br><sub>0,4,6,3,7</sub> |  | 0.7<br><sub>1,0,0,0,1</sub> |  | 0.5<br><sub>1,1,1,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.6 |
| Jordan Hawkins | 80% | 13.3<br><sub>-,6,2,7,17</sub> | 5.3<br><sub>-,0,2,2,9</sub> |  | 1.8<br><sub>-,0,0,1,0</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.6<br><sub>-,0,0,0,1</sub> |  | 0.3 | 0.2 | 0.6 | 7.9 |
| Buddy Hield | 71% | 13.2<br><sub>9,17,12,8,-</sub> | 5.5<br><sub>2,5,6,7,-</sub> |  | 1.9<br><sub>3,3,1,1,-</sub> |  | 1.2<br><sub>1,1,3,1,-</sub> |  | 0.7<br><sub>0,1,1,1,-</sub> |  | 0.5 | 0.2 | 0.7 | 8.6 |
| Dailyn Swain | 52% | 8.4<br><sub>-,-,-,7,-</sub> | 2.7<br><sub>-,-,-,3,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.8 | 5.1 |

</details>

<details><summary>if Norman Powell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson (CHI) | 98% | 31.8<br><sub>38,31,34,22,32</sub> | 17.8<br><sub>20,23,24,5,18</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>6,5,7,5,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>4,4,4,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>3,6,4,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.8 | 2.4 | 26.4 |
| Josh Giddey (CHI) | 98% | 29.2<br><sub>31,25,32,27,34</sub> | 11.9<br><sub>10,13,13,10,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>8,4,4,1,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 7.9<br><sub>11,5,10,6,15</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.5 | 2.5 | 26.2 |
| Norman Powell (CHI) | 100% | 28.5<br><sub>37,31,29,22,-</sub> | 17.3<br><sub>30,16,18,12,-</sub> | 18.5 · – | 3.2<br><sub>2,2,3,1,-</sub> | 2.5 | 2.1<br><sub>2,3,0,1,-</sub> | 1.5 | 2.0<br><sub>4,1,1,0,-</sub> | 2.5 | 1.0 | 0.2 | 1.8 | 22.6 |
| Matas Buzelis (CHI) | 98% | 26.5<br><sub>33,20,23,26,31</sub> | 12.6<br><sub>17,14,4,12,19</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,5,3,5,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>3,1,2,3,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>3,2,0,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 1.1 | 1.8 | 19.4 |
| Jalen Smith (CHI) | 98% | 24.1<br><sub>30,27,28,7,30</sub> | 10.6<br><sub>17,5,13,3,17</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>11,12,7,2,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>5,1,4,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.5 | 0.9 | 0.9 | 19.2 |
| Patrick Williams (CHI) | 58% | 21.0<br><sub>-,-,-,20,25</sub> | 6.8<br><sub>-,-,-,4,7</sub> |  | 2.8<br><sub>-,-,-,0,3</sub> |  | 1.5<br><sub>-,-,-,2,3</sub> |  | 0.9<br><sub>-,-,-,0,1</sub> |  | 0.7 | 0.4 | 0.9 | 11.1 |
| Isaac Okoro (CHI) | 98% | 18.9<br><sub>18,18,21,15,25</sub> | 6.1<br><sub>7,6,4,6,12</sub> |  | 1.9<br><sub>0,3,1,1,2</sub> |  | 1.0<br><sub>1,2,0,0,1</sub> |  | 0.5<br><sub>1,1,0,0,0</sub> |  | 0.6 | 0.3 | 0.5 | 9.0 |
| Nic Claxton (CHI) | 96% | 17.8<br><sub>-,-,-,-,18</sub> | 6.8<br><sub>-,-,-,-,4</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>-,-,-,-,4</sub> | 5.5<br><sub>o 42% · u 57%</sub> | 2.1<br><sub>-,-,-,-,4</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.8 | 0.9 | 13.6 |
| Tre Jones (CHI) | 98% | 17.3<br><sub>18,20,19,18,14</sub> | 9.0<br><sub>11,12,8,14,6</sub> |  | 2.4<br><sub>4,4,3,3,1</sub> |  | 3.2<br><sub>3,4,3,4,1</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.2 | 0.9 | 14.6 |
| Leonard Miller (CHI) | 72% | 12.4<br><sub>17,11,9,19,-</sub> | 5.6<br><sub>10,2,2,4,-</sub> |  | 3.0<br><sub>0,2,3,6,-</sub> |  | 0.7<br><sub>1,1,0,3,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.5 | 9.3 |
| Noa Essengue (CHI) | 91% | 11.9<br><sub>10,16,14,14,15</sub> | 5.0<br><sub>3,10,8,6,10</sub> |  | 2.7<br><sub>0,4,6,3,7</sub> |  | 0.6<br><sub>1,0,0,0,1</sub> |  | 0.4<br><sub>1,1,1,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |
| Jordan Hawkins (CHI) | 80% | 9.0<br><sub>-,6,2,7,17</sub> | 4.0<br><sub>-,0,2,2,9</sub> |  | 1.2<br><sub>-,0,0,1,0</sub> |  | 0.5<br><sub>-,0,0,0,1</sub> |  | 0.4<br><sub>-,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Buddy Hield (CHI) | 71% | 8.8<br><sub>9,17,12,8,-</sub> | 3.7<br><sub>2,5,6,7,-</sub> |  | 1.3<br><sub>3,3,1,1,-</sub> |  | 0.8<br><sub>1,1,3,1,-</sub> |  | 0.4<br><sub>0,1,1,1,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.8 |
| Dailyn Swain (CHI) | 52% | 6.3<br><sub>-,-,-,7,-</sub> | 2.0<br><sub>-,-,-,3,-</sub> |  | 0.9<br><sub>-,-,-,1,-</sub> |  | 1.0<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.7 | 3.9 |
| Dylan Harper (SAS) | 98% | 32.5<br><sub>27,36,28,28,26</sub> | 18.6<br><sub>17,21,19,13,17</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>7,5,2,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>8,0,3,3,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.3 | 1.9 | 28.9 |
| Victor Wembanyama (SAS) | 98% | 31.8<br><sub>24,34,26,24,25</sub> | 30.9<br><sub>12,52,30,29,40</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 13.0<br><sub>11,24,14,7,11</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,2,2,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 3.7 | 2.6 | 47.2 |
| Stephon Castle (SAS) | 98% | 31.6<br><sub>26,35,28,24,30</sub> | 18.4<br><sub>16,17,19,14,4</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>5,10,3,7,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.7<br><sub>4,3,7,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 2.9 | 30.8 |
| De'Aaron Fox (SAS) | 98% | 31.5<br><sub>22,33,26,22,29</sub> | 16.3<br><sub>12,10,9,8,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>2,3,2,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>3,4,4,6,6</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,0,0,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 2.1 | 26.6 |
| Julian Champagnie (SAS) | 98% | 27.3<br><sub>22,21,22,21,27</sub> | 10.3<br><sub>8,0,8,14,11</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>6,4,7,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,3,2,0,2</sub> |  | 1.9<br><sub>2,0,2,4,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 0.7 | 16.9 |
| Keldon Johnson (SAS) | 98% | 26.3<br><sub>27,19,27,27,26</sub> | 11.2<br><sub>15,4,3,10,4</sub> |  | 5.8<br><sub>7,5,6,7,5</sub> |  | 1.8<br><sub>1,2,6,4,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 18.9 |
| Harrison Barnes (SAS) | 86% | 18.8<br><sub>21,13,19,19,21</sub> | 6.9<br><sub>13,4,13,5,11</sub> |  | 2.2<br><sub>0,2,1,3,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>3,1,2,1,2</sub> |  | 0.5 | 0.2 | 0.5 | 10.0 |
| Luke Kornet (SAS) | 98% | 17.0<br><sub>17,14,18,15,13</sub> | 4.3<br><sub>8,2,2,6,2</sub> |  | 5.3<br><sub>5,1,6,4,4</sub> |  | 1.0<br><sub>2,2,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.5 | 10.7 |
| Carter Bryant (SAS) | 88% | 14.1<br><sub>14,-,3,17,14</sub> | 4.8<br><sub>3,-,0,6,8</sub> |  | 2.3<br><sub>0,-,0,4,1</sub> |  | 0.9<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>1,-,0,2,2</sub> |  | 0.3 | 0.4 | 0.6 | 7.9 |
| Jordan McLaughlin (SAS) | 67% | 13.2<br><sub>8,-,8,12,11</sub> | 3.9<br><sub>0,-,2,3,4</sub> |  | 1.8<br><sub>1,-,2,0,4</sub> |  | 1.9<br><sub>3,-,1,0,2</sub> |  | 0.4<br><sub>0,-,0,1,0</sub> |  | 1.0 | 0.1 | 0.6 | 7.7 |
| Tarris Reed Jr. (SAS) | 67% | 10.0<br><sub>7,-,3,9,9</sub> | 3.7<br><sub>4,-,0,2,4</sub> |  | 4.1<br><sub>7,-,1,3,3</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.8 | 8.2 |
| David Jones Garcia (SAS) | 64% | 8.2<br><sub>-,-,3,-,8</sub> | 3.3<br><sub>-,-,0,-,2</sub> |  | 1.6<br><sub>-,-,0,-,0</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.2 |

</details>

<details><summary>if Devin Vassell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson (CHI) | 98% | 34.0<br><sub>38,31,34,22,32</sub> | 19.8<br><sub>20,23,24,5,18</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>6,5,7,5,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>4,4,4,0,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>3,6,4,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.8 | 2.7 | 28.9 |
| Josh Giddey (CHI) | 98% | 31.7<br><sub>31,25,32,27,34</sub> | 14.1<br><sub>10,13,13,10,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 7.1<br><sub>8,4,4,1,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 9.3<br><sub>11,5,10,6,15</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.6 | 2.8 | 30.5 |
| Matas Buzelis (CHI) | 98% | 28.7<br><sub>33,20,23,26,31</sub> | 14.7<br><sub>17,14,4,12,19</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,5,3,5,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,1,2,3,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>3,2,0,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 1.2 | 2.0 | 22.2 |
| Jalen Smith (CHI) | 98% | 26.6<br><sub>30,27,28,7,30</sub> | 12.4<br><sub>17,5,13,3,17</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>11,12,7,2,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>5,1,4,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.5 | 1.1 | 1.0 | 22.1 |
| Patrick Williams (CHI) | 58% | 24.0<br><sub>-,-,-,20,25</sub> | 8.1<br><sub>-,-,-,4,7</sub> |  | 3.1<br><sub>-,-,-,0,3</sub> |  | 1.8<br><sub>-,-,-,2,3</sub> |  | 1.1<br><sub>-,-,-,0,1</sub> |  | 0.7 | 0.4 | 1.0 | 13.0 |
| Isaac Okoro (CHI) | 98% | 22.2<br><sub>18,18,21,15,25</sub> | 7.4<br><sub>7,6,4,6,12</sub> |  | 2.2<br><sub>0,3,1,1,2</sub> |  | 1.3<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>1,1,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 10.9 |
| Tre Jones (CHI) | 98% | 19.4<br><sub>18,20,19,18,14</sub> | 10.4<br><sub>11,12,8,14,6</sub> |  | 2.7<br><sub>4,4,3,3,1</sub> |  | 3.6<br><sub>3,4,3,4,1</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.9 | 0.2 | 1.1 | 16.8 |
| Nic Claxton (CHI) | 96% | 19.1<br><sub>-,-,-,-,18</sub> | 7.5<br><sub>-,-,-,-,4</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>-,-,-,-,4</sub> | 5.5<br><sub>o 42% · u 57%</sub> | 2.3<br><sub>-,-,-,-,4</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.8 | 1.0 | 14.8 |
| Leonard Miller (CHI) | 72% | 15.4<br><sub>17,11,9,19,-</sub> | 6.8<br><sub>10,2,2,4,-</sub> |  | 3.7<br><sub>0,2,3,6,-</sub> |  | 0.8<br><sub>1,1,0,3,-</sub> |  | 0.6<br><sub>1,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 11.3 |
| Noa Essengue (CHI) | 91% | 14.2<br><sub>10,16,14,14,15</sub> | 5.7<br><sub>3,10,8,6,10</sub> |  | 3.1<br><sub>0,4,6,3,7</sub> |  | 0.7<br><sub>1,0,0,0,1</sub> |  | 0.5<br><sub>1,1,1,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.5 |
| Jordan Hawkins (CHI) | 80% | 13.3<br><sub>-,6,2,7,17</sub> | 5.3<br><sub>-,0,2,2,9</sub> |  | 1.8<br><sub>-,0,0,1,0</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.6<br><sub>-,0,0,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 7.8 |
| Buddy Hield (CHI) | 71% | 13.2<br><sub>9,17,12,8,-</sub> | 5.5<br><sub>2,5,6,7,-</sub> |  | 1.9<br><sub>3,3,1,1,-</sub> |  | 1.2<br><sub>1,1,3,1,-</sub> |  | 0.7<br><sub>0,1,1,1,-</sub> |  | 0.5 | 0.2 | 0.7 | 8.6 |
| Dailyn Swain (CHI) | 52% | 8.4<br><sub>-,-,-,7,-</sub> | 2.7<br><sub>-,-,-,3,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.8 | 5.1 |
| Devin Vassell (SAS) | 100% | 30.5<br><sub>25,36,27,21,-</sub> | 13.0<br><sub>11,2,19,15,-</sub> | 10.5 · – | 4.3<br><sub>2,7,2,2,-</sub> | 3.5 | 2.9<br><sub>1,4,2,3,-</sub> | 2.5 | 2.0<br><sub>0,0,5,2,-</sub> | 1.5 | 1.4 | 0.4 | 1.0 | 20.2 |
| Dylan Harper (SAS) | 98% | 30.2<br><sub>27,36,28,28,26</sub> | 16.5<br><sub>17,21,19,13,17</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>7,5,2,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>8,0,3,3,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.2 | 0.4 | 1.8 | 26.1 |
| Victor Wembanyama (SAS) | 98% | 30.1<br><sub>24,34,26,24,25</sub> | 28.8<br><sub>12,52,30,29,40</sub> | 30.5 · –<br><sub>o 47% · u 53%</sub> | 12.5<br><sub>11,24,14,7,11</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,2,2,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 3.7 | 2.4 | 44.4 |
| Stephon Castle (SAS) | 98% | 29.3<br><sub>26,35,28,24,30</sub> | 16.5<br><sub>16,17,19,14,4</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>5,10,3,7,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.3<br><sub>4,3,7,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 2.6 | 28.2 |
| De'Aaron Fox (SAS) | 98% | 29.0<br><sub>22,33,26,22,29</sub> | 14.7<br><sub>12,10,9,8,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>2,3,2,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>3,4,4,6,6</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,0,0,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.9 | 24.2 |
| Julian Champagnie (SAS) | 98% | 24.4<br><sub>22,21,22,21,27</sub> | 9.3<br><sub>8,0,8,14,11</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>6,4,7,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,3,2,0,2</sub> |  | 1.7<br><sub>2,0,2,4,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.4 | 0.6 | 15.3 |
| Keldon Johnson (SAS) | 98% | 23.2<br><sub>27,19,27,27,26</sub> | 10.1<br><sub>15,4,3,10,4</sub> |  | 5.2<br><sub>7,5,6,7,5</sub> |  | 1.7<br><sub>1,2,6,4,3</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.6 | 0.2 | 1.0 | 16.9 |
| Harrison Barnes (SAS) | 86% | 16.0<br><sub>21,13,19,19,21</sub> | 6.1<br><sub>13,4,13,5,11</sub> |  | 1.9<br><sub>0,2,1,3,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 0.8<br><sub>3,1,2,1,2</sub> |  | 0.4 | 0.2 | 0.4 | 8.8 |
| Luke Kornet (SAS) | 98% | 14.7<br><sub>17,14,18,15,13</sub> | 3.9<br><sub>8,2,2,6,2</sub> |  | 4.7<br><sub>5,1,6,4,4</sub> |  | 0.9<br><sub>2,2,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.4 | 9.5 |
| Carter Bryant (SAS) | 88% | 11.9<br><sub>14,-,3,17,14</sub> | 4.3<br><sub>3,-,0,6,8</sub> |  | 2.1<br><sub>0,-,0,4,1</sub> |  | 0.8<br><sub>0,-,0,1,1</sub> |  | 0.5<br><sub>1,-,0,2,2</sub> |  | 0.3 | 0.3 | 0.5 | 7.2 |
| Jordan McLaughlin (SAS) | 67% | 9.7<br><sub>8,-,8,12,11</sub> | 3.2<br><sub>0,-,2,3,4</sub> |  | 1.4<br><sub>1,-,2,0,4</sub> |  | 1.6<br><sub>3,-,1,0,2</sub> |  | 0.3<br><sub>0,-,0,1,0</sub> |  | 0.7 | 0.1 | 0.5 | 6.3 |
| Tarris Reed Jr. (SAS) | 67% | 8.2<br><sub>7,-,3,9,9</sub> | 3.4<br><sub>4,-,0,2,4</sub> |  | 3.5<br><sub>7,-,1,3,3</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 7.3 |
| David Jones Garcia (SAS) | 64% | 6.7<br><sub>-,-,3,-,8</sub> | 3.1<br><sub>-,-,0,-,2</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 1.2<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.1 | 0.5 | 5.6 |

</details>


### DEN @ MEM
Out: Scotty Pippen Jr. (MEM), Quinten Post (MEM), Julian Strawther (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 121.4–116.5 | DEN 64% | 1.57 / 2.77 | MEM +5.5 | 237.5 | MEM +3.5 covers 45%; o229.5 67% |
| Expected (weighted by chance each plays) | 121.0–117.8 | DEN 60% | 1.68 / 2.48 | MEM +3.5 | 238.5 | MEM +3.5 covers 50%; o229.5 69% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jahmai Mashack (MEM) | Questionable | 55% | 7.7 | 2.5 | 1.0 | 1.0 | 0.1 | 0.4 | 0.1 | 0.5 | 4.5 | small |
| Isaiah Stewart (MEM) | Questionable | 55% | 13.4 | 6.2 | 3.0 | 0.6 | 0.4 | 0.2 | 0.7 | 0.6 | 9.8 | small |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 36.3<br><sub>37,39,28,34,39</sub> | 25.6<br><sub>39,35,14,16,38</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>8,5,5,6,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>5,6,7,8,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>7,4,2,2,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.6 | 2.5 | 37.1 |
| Nikola Jokic | 98% | 35.8<br><sub>37,36,30,36,39</sub> | 26.5<br><sub>18,26,32,19,25</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 13.2<br><sub>7,9,10,13,16</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 10.7<br><sub>10,8,11,8,9</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,2,0,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 1.1 | 3.7 | 50.3 |
| Christian Braun | 98% | 31.6<br><sub>37,37,28,29,32</sub> | 12.1<br><sub>31,14,11,6,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,3,3,4,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.4<br><sub>1,3,3,1,3</sub> |  | 1.2<br><sub>7,1,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.5 | 1.0 | 18.9 |
| Cameron Johnson | 98% | 28.3<br><sub>34,34,30,29,31</sub> | 12.2<br><sub>12,7,12,18,8</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>9,4,2,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>3,2,2,1,1</sub> |  | 1.6<br><sub>2,1,4,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.4 | 1.0 | 18.5 |
| Aaron Gordon | 98% | 28.0<br><sub>29,30,25,27,30</sub> | 13.2<br><sub>15,5,17,12,3</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>4,6,1,5,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>5,2,0,0,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>2,1,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.4 | 1.3 | 21.4 |
| DeMar DeRozan | 86% | 21.8<br><sub>24,20,-,22,19</sub> | 11.4<br><sub>3,9,-,11,7</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,0,-,1,4</sub> |  | 3.3<br><sub>5,1,-,5,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.3 | 1.2 | 16.9 |
| Trevon Brazile | 98% | 15.4<br><sub>19,18,23,14,14</sub> | 5.0<br><sub>6,6,6,3,5</sub> |  | 3.8<br><sub>3,5,7,4,2</sub> |  | 0.8<br><sub>1,1,1,2,0</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.3 | 0.7 | 9.6 |
| Spencer Jones | 64% | 14.0<br><sub>-,-,-,21,14</sub> | 4.3<br><sub>-,-,-,13,0</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>-,-,-,6,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,3,0</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 0.5 | 0.6 | 0.7 | 7.6 |
| Marvin Bagley III | 98% | 12.6<br><sub>11,12,14,12,12</sub> | 6.5<br><sub>0,6,10,10,6</sub> |  | 4.0<br><sub>5,4,2,3,3</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 11.1 |
| Tyus Jones | 96% | 10.0<br><sub>11,8,18,13,6</sub> | 3.0<br><sub>3,2,6,3,2</sub> |  | 1.0<br><sub>0,0,1,4,0</sub> |  | 1.8<br><sub>0,1,8,4,0</sub> |  | 0.3<br><sub>1,0,0,1,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.8 |
| Bryce Hopkins | 76% | 9.4<br><sub>-,-,28,3,3</sub> | 3.2<br><sub>-,-,18,3,2</sub> |  | 1.6<br><sub>-,-,4,1,0</sub> |  | 0.5<br><sub>-,-,1,0,0</sub> |  | 0.1<br><sub>-,-,1,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.3 |
| Cam Whitmore | 58% | 7.3<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.8 |
| Zeke Nnaji | 38% | 6.6<br><sub>-,-,4,-,-</sub> | 2.4<br><sub>-,-,2,-,-</sub> |  | 1.5<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.3 |
| Alpha Diallo | 71% | 6.2<br><sub>-,6,4,-,1</sub> | 2.6<br><sub>-,0,0,-,0</sub> |  | 1.0<br><sub>-,1,0,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Ryan Nembhard | 52% | 6.2<br><sub>-,-,4,-,-</sub> | 3.0<br><sub>-,-,0,-,-</sub> |  | 1.0<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| DaRon Holmes II | 52% | 5.8<br><sub>-,-,4,-,1</sub> | 2.6<br><sub>-,-,0,-,0</sub> |  | 1.2<br><sub>-,-,1,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.3 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 33.3<br><sub>26,38,33,31,33</sub> | 16.7<br><sub>27,18,10,8,22</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>9,9,6,12,7</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 5.5<br><sub>3,5,4,4,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>3,2,2,0,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.6 | 2.7 | 31.7 |
| Ty Jerome | 98% | 31.3<br><sub>-,37,29,28,32</sub> | 21.9<br><sub>-,40,23,21,27</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>-,5,4,2,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.7<br><sub>-,5,3,5,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>-,5,2,2,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 2.3 | 31.3 |
| Cedric Coward | 98% | 28.8<br><sub>23,31,33,23,28</sub> | 14.2<br><sub>10,10,23,10,3</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>7,9,9,9,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>2,3,4,0,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,2,4,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 1.4 | 24.0 |
| Jaylen Wells | 98% | 27.3<br><sub>22,34,21,25,26</sub> | 11.1<br><sub>4,16,0,7,14</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>2,3,1,0,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>0,3,3,0,1</sub> |  | 1.7<br><sub>0,3,0,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.1 | 0.8 | 15.7 |
| Jerami Grant | 98% | 24.4<br><sub>23,24,24,22,22</sub> | 12.1<br><sub>14,11,11,10,17</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,4,1,0,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,2,2,2,2</sub> |  | 1.6<br><sub>1,2,2,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.6 | 1.1 | 16.4 |
| Javon Small | 93% | 23.8<br><sub>20,-,-,21,24</sub> | 10.3<br><sub>7,-,-,10,9</sub> |  | 3.4<br><sub>1,-,-,4,2</sub> |  | 3.8<br><sub>5,-,-,2,5</sub> |  | 1.4<br><sub>2,-,-,1,1</sub> |  | 0.9 | 0.2 | 1.2 | 17.5 |
| Zach Edey | 98% | 23.6<br><sub>18,19,25,20,23</sub> | 9.4<br><sub>4,6,11,14,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 9.4<br><sub>6,9,13,6,9</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>0,1,1,1,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.3 | 1.4 | 20.0 |
| Cam Spencer | 98% | 20.3<br><sub>25,19,24,19,17</sub> | 8.3<br><sub>10,13,7,7,7</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>5,1,6,1,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>13,7,9,0,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 1.0 | 15.7 |
| GG Jackson | 80% | 15.6<br><sub>21,16,7,-,17</sub> | 8.3<br><sub>21,6,1,-,2</sub> |  | 3.2<br><sub>3,0,2,-,1</sub> |  | 1.0<br><sub>2,1,0,-,0</sub> |  | 0.9<br><sub>5,0,0,-,0</sub> |  | 0.4 | 0.4 | 1.1 | 12.4 |
| Taylor Hendricks | 63% | 11.8<br><sub>4,-,-,4,16</sub> | 5.0<br><sub>6,-,-,4,9</sub> |  | 2.3<br><sub>1,-,-,2,3</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>2,-,-,1,1</sub> |  | 0.5 | 0.3 | 0.5 | 7.8 |
| Kris Murray | 88% | 10.2<br><sub>21,19,15,13,1</sub> | 2.8<br><sub>2,0,5,2,0</sub> |  | 1.6<br><sub>1,4,1,2,0</sub> |  | 0.6<br><sub>1,1,1,1,0</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 5.0 |
| Olivier-Maxence Prosper | 67% | 8.7<br><sub>4,-,7,11,1</sub> | 4.7<br><sub>2,-,4,2,0</sub> |  | 1.8<br><sub>1,-,3,3,0</sub> |  | 0.5<br><sub>1,-,1,1,0</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.0 |

</details>


### LAL @ MIL
Out: Tyler Herro (MIL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.7–110.3 | LAL 75% | 1.34 / 3.97 | MIL +9.5 | 229.5 | MIL +12.5 covers 59%; o231.5 47% |
| Expected (weighted by chance each plays) | 119.6–110.5 | LAL 74% | 1.35 / 3.87 | MIL +8.5 | 230.5 | MIL +12.5 covers 60%; o231.5 47% |
| if Quentin Grimes plays | 119.4–110.4 | LAL 74% | 1.35 / 3.84 | MIL +8.5 | 229.5 | MIL +12.5 covers 60%; o231.5 46% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quentin Grimes (LAL) | Questionable | 55% | 22.8 | 8.0 | 2.7 | 2.3 | 0.9 | 0.8 | 0.3 | 1.1 | 13.1 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.2<br><sub>36,35,38,-,39</sub> | 35.3<br><sub>42,40,53,-,32</sub> | 35.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>7,9,5,-,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 8.3<br><sub>13,7,5,-,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>6,6,5,-,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9 | 0.6 | 4.0 | 51.5 |
| Austin Reaves | 98% | 36.0<br><sub>34,37,38,37,-</sub> | 22.1<br><sub>27,21,25,43,-</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>2,3,3,5,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>5,4,2,4,-</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>4,1,1,4,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 3.0 | 31.8 |
| Walker Kessler | 98% | 30.3<br><sub>32,29,37,29,30</sub> | 12.1<br><sub>15,15,16,12,21</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 11.7<br><sub>15,8,12,16,10</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>2,0,2,4,4</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.9 | 1.5 | 25.8 |
| Jake LaRavia | 98% | 25.6<br><sub>26,21,25,29,32</sub> | 6.6<br><sub>7,9,7,5,4</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>4,2,8,1,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,2,3,2,3</sub> |  | 0.7<br><sub>1,2,2,0,0</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.6 | 1.1 | 12.5 |
| Sandro Mamukelashvili | 98% | 23.7<br><sub>28,19,20,18,32</sub> | 9.3<br><sub>13,2,7,7,23</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>3,6,3,3,8</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>4,1,1,0,3</sub> |  | 1.3<br><sub>2,0,1,1,5</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.5 | 0.8 | 16.2 |
| Ziaire Williams | 98% | 23.6<br><sub>15,23,20,21,28</sub> | 8.9<br><sub>9,10,8,17,12</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>2,1,1,0,2</sub> |  | 1.4<br><sub>3,1,2,4,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.3 | 0.9 | 13.1 |
| Matisse Thybulle | 98% | 23.4<br><sub>19,23,24,28,23</sub> | 5.9<br><sub>6,3,2,4,6</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>1,1,2,2,0</sub> |  | 1.2<br><sub>2,2,0,0,1</sub> |  | 1.1<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 2.2 | 0.7 | 0.7 | 9.3 |
| Collin Sexton | 98% | 20.6<br><sub>16,16,11,24,27</sub> | 11.3<br><sub>6,10,0,17,18</sub> |  | 2.2<br><sub>1,3,0,2,2</sub> |  | 2.6<br><sub>5,1,1,2,6</sub> |  | 1.2<br><sub>0,1,0,0,3</sub> |  | 0.9 | 0.2 | 1.4 | 16.2 |
| Jarred Vanderbilt | 71% | 12.5<br><sub>6,7,-,14,13</sub> | 3.0<br><sub>2,0,-,2,4</sub> |  | 3.3<br><sub>1,1,-,10,2</sub> |  | 1.1<br><sub>0,0,-,3,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 7.3 |
| AK Okereke | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Adou Thiero | 91% | 8.0<br><sub>-,-,7,8,7</sub> | 2.7<br><sub>-,-,4,2,2</sub> |  | 2.2<br><sub>-,-,4,2,2</sub> |  | 0.6<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Jaden Hardy | 52% | 6.7<br><sub>1,1,-,-,-</sub> | 3.7<br><sub>2,0,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Kevon Looney | 26% | 6.5<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.5 |
| Cameron Carr | 71% | 6.1<br><sub>1,1,-,-,7</sub> | 2.1<br><sub>0,0,-,-,2</sub> |  | 1.0<br><sub>0,0,-,-,3</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.5 |
| Chris Manon | 58% | 5.7<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.0 |
| Carson Cooper | 48% | 5.5<br><sub>3,-,-,-,-</sub> | 2.5<br><sub>1,-,-,-,-</sub> |  | 3.0<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 1.0 | 6.3 |
| Bronny James | 52% | 5.5<br><sub>1,1,-,-,-</sub> | 2.0<br><sub>2,0,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.7 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyle Kuzma | 98% | 29.4<br><sub>23,22,27,32,31</sub> | 14.3<br><sub>14,2,6,13,27</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>3,2,5,4,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,3,4,3,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,1,1,6</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.3 | 2.2 | 22.8 |
| Jaime Jaquez Jr. | 98% | 28.1<br><sub>23,28,31,28,23</sub> | 15.7<br><sub>8,19,18,14,4</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,8,2,3,2</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>5,2,2,3,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,2,4,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.3 | 2.2 | 25.0 |
| Brayden Burries | 98% | 27.6<br><sub>21,26,22,38,29</sub> | 13.4<br><sub>14,9,9,21,13</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>3,9,5,11,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>1,1,3,6,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>1,1,0,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.8 | 23.1 |
| Myles Turner | 98% | 27.3<br><sub>24,31,36,24,24</sub> | 11.0<br><sub>10,13,12,0,3</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 5.4<br><sub>7,5,9,7,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>2,2,6,0,7</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>1,3,4,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 1.6 | 1.5 | 18.6 |
| Ryan Rollins | 98% | 25.0<br><sub>26,17,24,14,20</sub> | 14.1<br><sub>9,10,13,10,7</sub> |  | 3.6<br><sub>3,3,9,1,5</sub> |  | 5.2<br><sub>7,2,5,1,6</sub> |  | 1.8<br><sub>1,1,2,1,2</sub> |  | 1.1 | 0.3 | 2.7 | 23.0 |
| AJ Green | 98% | 22.8<br><sub>20,24,20,24,18</sub> | 9.4<br><sub>0,13,5,12,5</sub> |  | 2.2<br><sub>3,3,2,1,1</sub> |  | 1.7<br><sub>2,3,3,0,1</sub> |  | 1.8<br><sub>0,4,1,4,1</sub> |  | 0.4 | 0.1 | 0.9 | 13.3 |
| Cormac Ryan | 16% | 17.5 | 9.3 |  | 1.9 |  | 1.4 |  | 1.2 |  | 0.6 | 0.2 | 1.2 | 12.7 |
| Nate Ament | 91% | 17.1<br><sub>19,8,18,15,23</sub> | 7.4<br><sub>14,4,9,7,12</sub> |  | 2.6<br><sub>1,1,2,1,5</sub> |  | 0.7<br><sub>2,0,0,0,1</sub> |  | 0.7<br><sub>2,0,2,0,2</sub> |  | 0.5 | 0.3 | 1.0 | 10.8 |
| Caris LeVert | 16% | 15.9<br><sub>-,-,-,-,-</sub> | 6.6<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.8 | 0.4 | 0.9 | 10.5 |
| Kasparas Jakucionis | 93% | 15.4<br><sub>21,22,12,10,7</sub> | 5.4<br><sub>5,7,3,3,1</sub> |  | 1.9<br><sub>3,5,1,0,2</sub> |  | 3.0<br><sub>3,7,1,2,0</sub> |  | 0.5<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.1 | 1.3 | 10.4 |
| Kel'el Ware | 96% | 15.4<br><sub>24,17,16,13,9</sub> | 7.3<br><sub>19,2,2,4,0</sub> |  | 5.2<br><sub>10,9,5,3,0</sub> |  | 0.8<br><sub>3,0,1,0,1</sub> |  | 0.6<br><sub>3,0,0,0,0</sub> |  | 0.5 | 0.6 | 1.2 | 13.2 |
| Pete Nance | 16% | 12.9 | 4.3 |  | 1.9 |  | 0.9 |  | 0.5 |  | 0.3 | 0.2 | 0.5 | 7.1 |
| Ousmane Dieng | 66% | 12.7<br><sub>6,-,2,-,15</sub> | 4.9<br><sub>0,-,0,-,10</sub> |  | 1.9<br><sub>1,-,0,-,1</sub> |  | 1.6<br><sub>2,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,2</sub> |  | 0.4 | 0.2 | 0.9 | 8.3 |
| Kam Jones | 16% | 12.3 | 3.4 |  | 1.2 |  | 2.9 |  | 0.3 |  | 0.5 | 0.1 | 0.8 | 7.5 |
| Jericho Sims | 72% | 11.9<br><sub>-,15,1,7,15</sub> | 2.7<br><sub>-,0,0,0,2</sub> |  | 3.2<br><sub>-,2,0,1,2</sub> |  | 0.9<br><sub>-,1,0,0,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.8 |
| Gary Trent Jr. | 38% | 10.2<br><sub>6,-,-,-,-</sub> | 4.7<br><sub>3,-,-,-,-</sub> |  | 0.7<br><sub>1,-,-,-,-</sub> |  | 0.7<br><sub>1,-,-,-,-</sub> |  | 0.6<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.1 |
| Bogoljub Markovic | 30% | 6.9<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.8 |

</details>

<details><summary>if Quentin Grimes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 34.4<br><sub>36,35,38,-,39</sub> | 33.0<br><sub>42,40,53,-,32</sub> | 35.5 · –<br><sub>o 48% · u 52%</sub> | 7.4<br><sub>7,9,5,-,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 8.1<br><sub>13,7,5,-,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>6,6,5,-,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9 | 0.5 | 3.9 | 48.5 |
| Austin Reaves (LAL) | 98% | 33.8<br><sub>34,37,38,37,-</sub> | 20.6<br><sub>27,21,25,43,-</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>2,3,3,5,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>5,4,2,4,-</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>4,1,1,4,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 2.9 | 29.9 |
| Walker Kessler (LAL) | 98% | 28.2<br><sub>32,29,37,29,30</sub> | 12.0<br><sub>15,15,16,12,21</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 11.1<br><sub>15,8,12,16,10</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>2,0,2,4,4</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.5 | 24.9 |
| Quentin Grimes (LAL) | 100% | 22.8<br><sub>23,25,20,32,-</sub> | 8.0<br><sub>7,6,2,12,-</sub> |  | 2.7<br><sub>4,1,0,1,-</sub> |  | 2.3<br><sub>4,1,0,4,-</sub> |  | 0.9<br><sub>1,0,0,2,-</sub> |  | 0.8 | 0.3 | 1.1 | 13.1 |
| Jake LaRavia (LAL) | 98% | 22.5<br><sub>26,21,25,29,32</sub> | 6.3<br><sub>7,9,7,5,4</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>4,2,8,1,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>2,2,3,2,3</sub> |  | 0.7<br><sub>1,2,2,0,0</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 1.2 | 0.5 | 1.0 | 11.7 |
| Ziaire Williams (LAL) | 98% | 21.6<br><sub>15,23,20,21,28</sub> | 8.6<br><sub>9,10,8,17,12</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,1,1,0,2</sub> |  | 1.4<br><sub>3,1,2,4,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.3 | 0.8 | 12.6 |
| Sandro Mamukelashvili (LAL) | 98% | 21.5<br><sub>28,19,20,18,32</sub> | 9.0<br><sub>13,2,7,7,23</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>3,6,3,3,8</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>4,1,1,0,3</sub> |  | 1.3<br><sub>2,0,1,1,5</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.5 | 0.8 | 15.6 |
| Matisse Thybulle (LAL) | 98% | 20.3<br><sub>19,23,24,28,23</sub> | 5.5<br><sub>6,3,2,4,6</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,1,2,2,0</sub> |  | 1.0<br><sub>2,2,0,0,1</sub> |  | 0.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.9 | 0.6 | 0.7 | 8.5 |
| Collin Sexton (LAL) | 98% | 18.6<br><sub>16,16,11,24,27</sub> | 10.9<br><sub>6,10,0,17,18</sub> |  | 2.0<br><sub>1,3,0,2,2</sub> |  | 2.5<br><sub>5,1,1,2,6</sub> |  | 1.2<br><sub>0,1,0,0,3</sub> |  | 0.9 | 0.1 | 1.4 | 15.5 |
| Jarred Vanderbilt (LAL) | 71% | 11.3<br><sub>6,7,-,14,13</sub> | 3.0<br><sub>2,0,-,2,4</sub> |  | 3.0<br><sub>1,1,-,10,2</sub> |  | 1.1<br><sub>0,0,-,3,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 0.2 | 0.5 | 7.1 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.8 |
| Adou Thiero (LAL) | 91% | 7.0<br><sub>-,-,7,8,7</sub> | 2.5<br><sub>-,-,4,2,2</sub> |  | 1.9<br><sub>-,-,4,2,2</sub> |  | 0.6<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Kevon Looney (LAL) | 26% | 6.4<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.7 |
| Jaden Hardy (LAL) | 52% | 6.3<br><sub>1,1,-,-,-</sub> | 3.9<br><sub>2,0,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 0.6<br><sub>0,1,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.2 |
| Cameron Carr (LAL) | 71% | 5.6<br><sub>1,1,-,-,7</sub> | 2.0<br><sub>0,0,-,-,2</sub> |  | 1.0<br><sub>0,0,-,-,3</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.2 | 3.5 |
| Carson Cooper (LAL) | 48% | 5.5<br><sub>3,-,-,-,-</sub> | 2.5<br><sub>1,-,-,-,-</sub> |  | 3.0<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.2 | 1.1 | 6.5 |
| Bronny James (LAL) | 52% | 5.4<br><sub>1,1,-,-,-</sub> | 2.1<br><sub>2,0,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.7 |
| Chris Manon (LAL) | 58% | 5.4<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 2.9 |
| Kyle Kuzma (MIL) | 98% | 29.4<br><sub>23,22,27,32,31</sub> | 14.3<br><sub>14,2,6,13,27</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>3,2,5,4,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,3,4,3,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,1,1,6</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.3 | 2.2 | 22.8 |
| Jaime Jaquez Jr. (MIL) | 98% | 28.1<br><sub>23,28,31,28,23</sub> | 15.7<br><sub>8,19,18,14,4</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,8,2,3,2</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>5,2,2,3,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,2,4,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.3 | 2.2 | 24.9 |
| Brayden Burries (MIL) | 98% | 27.7<br><sub>21,26,22,38,29</sub> | 13.4<br><sub>14,9,9,21,13</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>3,9,5,11,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>1,1,3,6,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>1,1,0,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.8 | 23.1 |
| Myles Turner (MIL) | 98% | 27.4<br><sub>24,31,36,24,24</sub> | 11.1<br><sub>10,13,12,0,3</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 5.4<br><sub>7,5,9,7,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>2,2,6,0,7</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>1,3,4,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 1.6 | 1.5 | 18.6 |
| Ryan Rollins (MIL) | 98% | 25.1<br><sub>26,17,24,14,20</sub> | 14.2<br><sub>9,10,13,10,7</sub> |  | 3.7<br><sub>3,3,9,1,5</sub> |  | 5.2<br><sub>7,2,5,1,6</sub> |  | 1.8<br><sub>1,1,2,1,2</sub> |  | 1.1 | 0.3 | 2.7 | 23.1 |
| AJ Green (MIL) | 98% | 22.8<br><sub>20,24,20,24,18</sub> | 9.3<br><sub>0,13,5,12,5</sub> |  | 2.2<br><sub>3,3,2,1,1</sub> |  | 1.7<br><sub>2,3,3,0,1</sub> |  | 1.8<br><sub>0,4,1,4,1</sub> |  | 0.4 | 0.1 | 0.9 | 13.3 |
| Cormac Ryan (MIL) | 16% | 17.3 | 9.2 |  | 1.9 |  | 1.4 |  | 1.2 |  | 0.7 | 0.2 | 1.3 | 12.4 |
| Nate Ament (MIL) | 91% | 17.1<br><sub>19,8,18,15,23</sub> | 7.4<br><sub>14,4,9,7,12</sub> |  | 2.6<br><sub>1,1,2,1,5</sub> |  | 0.7<br><sub>2,0,0,0,1</sub> |  | 0.7<br><sub>2,0,2,0,2</sub> |  | 0.5 | 0.3 | 1.0 | 10.8 |
| Caris LeVert (MIL) | 16% | 15.7<br><sub>-,-,-,-,-</sub> | 6.3<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.4 | 0.9 | 10.2 |
| Kel'el Ware (MIL) | 96% | 15.4<br><sub>24,17,16,13,9</sub> | 7.3<br><sub>19,2,2,4,0</sub> |  | 5.1<br><sub>10,9,5,3,0</sub> |  | 0.8<br><sub>3,0,1,0,1</sub> |  | 0.6<br><sub>3,0,0,0,0</sub> |  | 0.5 | 0.6 | 1.2 | 13.2 |
| Kasparas Jakucionis (MIL) | 93% | 15.2<br><sub>21,22,12,10,7</sub> | 5.4<br><sub>5,7,3,3,1</sub> |  | 1.9<br><sub>3,5,1,0,2</sub> |  | 3.0<br><sub>3,7,1,2,0</sub> |  | 0.5<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.1 | 1.3 | 10.3 |
| Pete Nance (MIL) | 16% | 13.0 | 4.3 |  | 2.0 |  | 0.9 |  | 0.5 |  | 0.3 | 0.2 | 0.6 | 7.2 |
| Ousmane Dieng (MIL) | 66% | 12.7<br><sub>6,-,2,-,15</sub> | 4.9<br><sub>0,-,0,-,10</sub> |  | 1.9<br><sub>1,-,0,-,1</sub> |  | 1.6<br><sub>2,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,2</sub> |  | 0.4 | 0.2 | 0.9 | 8.4 |
| Kam Jones (MIL) | 16% | 12.4 | 3.4 |  | 1.2 |  | 2.8 |  | 0.3 |  | 0.5 | 0.1 | 0.8 | 7.4 |
| Jericho Sims (MIL) | 72% | 12.0<br><sub>-,15,1,7,15</sub> | 2.7<br><sub>-,0,0,0,2</sub> |  | 3.2<br><sub>-,2,0,1,2</sub> |  | 0.9<br><sub>-,1,0,0,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.2 | 0.1 | 0.6 | 6.7 |
| Gary Trent Jr. (MIL) | 38% | 10.3<br><sub>6,-,-,-,-</sub> | 4.7<br><sub>3,-,-,-,-</sub> |  | 0.7<br><sub>1,-,-,-,-</sub> |  | 0.7<br><sub>1,-,-,-,-</sub> |  | 0.6<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Bogoljub Markovic (MIL) | 30% | 7.1<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.9 |

</details>


### BKN @ NOP
Out: Yves Missi (NOP), Trendon Watford (NOP), Grant Nelson (BKN), Ben Saraf (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.5–117.3 | BKN 29% | 3.48 / 1.40 | NOP -7.5 | 226.5 | NOP -4.5 covers 60%; o229.5 43% |
| Expected (weighted by chance each plays) | 109.7–117.3 | BKN 29% | 3.47 / 1.40 | NOP -7.5 | 226.5 | NOP -4.5 covers 60%; o229.5 44% |
| if Nolan Traore plays | 109.9–117.0 | BKN 31% | 3.27 / 1.44 | NOP -7.5 | 226.5 | NOP -4.5 covers 58%; o229.5 44% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nolan Traore (BKN) | Questionable | 55% | 21.0 | 10.4 | 1.9 | 3.3 | 1.2 | 0.9 | 0.4 | 2.0 | 15.6 | full tables below |
| Jaron Pierre Jr. (NOP) | Doubtful | 20% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 5.8 | small |
| Malik Dia (NOP) | Doubtful | 20% | 8.5 | 3.5 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.8 | small |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 98% | 33.8<br><sub>36,37,38,36,29</sub> | 21.8<br><sub>23,18,26,25,19</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>9,5,10,9,9</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>3,2,0,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 3.1<br><sub>3,4,4,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.4 | 2.4 | 31.4 |
| Julius Randle | 98% | 33.5<br><sub>37,36,31,34,30</sub> | 19.9<br><sub>20,21,22,19,13</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>5,11,3,7,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>6,2,4,8,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>4,0,2,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.3 | 3.4 | 31.9 |
| Day'Ron Sharpe | 98% | 23.7<br><sub>26,22,27,32,20</sub> | 10.2<br><sub>15,4,6,12,6</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 8.4<br><sub>13,6,5,10,4</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>4,3,8,13,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.3<br><sub>1,0,0,0,0</sub> |  | 1.1 | 1.0 | 1.8 | 22.5 |
| Mikel Brown Jr. | 96% | 23.6<br><sub>-,27,20,25,-</sub> | 12.3<br><sub>-,13,18,18,-</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>-,2,2,1,-</sub> |  | 3.7<br><sub>-,3,4,3,-</sub> |  | 1.7<br><sub>-,1,3,3,-</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 2.1 | 18.4 |
| Danny Wolf | 66% | 23.2<br><sub>-,-,19,31,36</sub> | 9.4<br><sub>-,-,12,11,10</sub> |  | 5.6<br><sub>-,-,5,9,3</sub> |  | 2.4<br><sub>-,-,3,1,2</sub> |  | 1.2<br><sub>-,-,2,2,1</sub> |  | 0.6 | 0.6 | 1.4 | 17.4 |
| Egor Demin | 91% | 20.9<br><sub>-,-,-,-,-</sub> | 8.4<br><sub>-,-,-,-,-</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.3 | 1.2 | 13.7 |
| Keon Ellis | 80% | 19.6<br><sub>20,25,10,-,22</sub> | 5.3<br><sub>0,5,1,-,3</sub> |  | 1.9<br><sub>2,1,2,-,1</sub> |  | 1.5<br><sub>1,0,0,-,4</sub> |  | 0.7<br><sub>0,1,0,-,1</sub> |  | 1.1 | 0.6 | 0.6 | 8.7 |
| Noah Clowney | 98% | 17.6<br><sub>24,20,17,21,8</sub> | 6.3<br><sub>8,2,7,3,2</sub> |  | 3.4<br><sub>3,6,1,10,0</sub> |  | 1.0<br><sub>0,2,1,0,0</sub> |  | 0.8<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.4 | 0.8 | 10.7 |
| Moritz Wagner | 96% | 17.5<br><sub>21,20,20,16,16</sub> | 9.7<br><sub>14,6,6,9,12</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>6,1,1,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>0,2,0,0,1</sub> |  | 0.7<br><sub>1,1,0,1,1</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 1.0 | 15.1 |
| Terance Mann | 67% | 17.2<br><sub>15,-,16,13,22</sub> | 4.1<br><sub>0,-,0,0,0</sub> |  | 2.1<br><sub>1,-,2,2,1</sub> |  | 1.8<br><sub>1,-,2,0,1</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 8.0 |
| Chaney Johnson | 96% | 15.1<br><sub>31,28,9,8,15</sub> | 4.4<br><sub>2,4,0,5,2</sub> |  | 2.1<br><sub>2,3,2,2,0</sub> |  | 0.9<br><sub>0,2,1,1,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.8 | 7.3 |
| Josh Minott | 58% | 11.2<br><sub>-,-,6,-,12</sub> | 5.8<br><sub>-,-,0,-,10</sub> |  | 2.1<br><sub>-,-,1,-,2</sub> |  | 0.7<br><sub>-,-,0,-,1</sub> |  | 0.8<br><sub>-,-,0,-,2</sub> |  | 0.7 | 0.4 | 0.6 | 8.6 |
| Drake Powell | 52% | 11.0<br><sub>-,-,-,-,9</sub> | 3.5<br><sub>-,-,-,-,2</sub> |  | 1.0<br><sub>-,-,-,-,2</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 5.4 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 92% | 32.9<br><sub>40,-,34,30,-</sub> | 17.9<br><sub>18,-,10,26,-</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>5,-,4,7,-</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 3.8<br><sub>5,-,5,3,-</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.6<br><sub>3,-,1,4,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.5 | 1.6 | 26.7 |
| Zion Williamson | 98% | 32.1<br><sub>35,38,36,31,-</sub> | 19.6<br><sub>25,23,13,25,-</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>11,4,8,4,-</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,2,4,2,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 1.4 | 0.7 | 2.1 | 28.8 |
| Dejounte Murray | 98% | 31.5<br><sub>-,45,35,28,18</sub> | 15.8<br><sub>-,20,7,6,12</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>-,8,2,3,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>-,4,4,3,1</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>-,1,1,0,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.8 | 0.4 | 2.7 | 27.5 |
| Jeremiah Fears | 98% | 29.7<br><sub>38,34,36,29,29</sub> | 15.8<br><sub>12,19,24,25,11</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>4,6,5,6,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>7,2,5,5,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.5 | 2.6 | 25.0 |
| Saddiq Bey | 98% | 27.0<br><sub>36,29,31,26,24</sub> | 14.7<br><sub>18,22,17,13,9</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,4,5,4,0</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>1,3,4,3,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>2,2,3,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.1 | 21.2 |
| Herbert Jones | 98% | 21.3<br><sub>28,37,14,20,24</sub> | 6.3<br><sub>9,2,0,4,10</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>4,5,4,0,6</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>3,1,0,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>3,0,0,0,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.1 | 0.4 | 1.0 | 10.6 |
| Derik Queen | 98% | 20.9<br><sub>24,27,10,21,21</sub> | 10.8<br><sub>20,20,6,8,16</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>7,9,4,5,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>5,6,1,3,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.9 | 0.9 | 1.9 | 19.7 |
| Jordan Poole | 58% | 17.8<br><sub>-,-,-,-,34</sub> | 8.3<br><sub>-,-,-,-,7</sub> |  | 2.0<br><sub>-,-,-,-,3</sub> |  | 2.3<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.7 | 0.3 | 1.4 | 12.5 |
| Karlo Matkovic | 96% | 17.1<br><sub>29,21,18,19,17</sub> | 6.9<br><sub>25,5,18,3,4</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>6,4,3,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>1,2,1,2,2</sub> |  | 0.7<br><sub>5,1,4,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.6 | 0.8 | 0.8 | 12.0 |
| Bennedict Mathurin | 98% | 15.0<br><sub>13,15,7,9,24</sub> | 6.9<br><sub>4,2,2,6,6</sub> |  | 2.6<br><sub>0,5,0,0,2</sub> |  | 1.2<br><sub>0,1,0,1,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 0.9 | 10.7 |
| Bryce McGowens | 64% | 13.2<br><sub>6,-,-,3,28</sub> | 4.6<br><sub>0,-,-,0,8</sub> |  | 1.5<br><sub>1,-,-,0,2</sub> |  | 0.8<br><sub>0,-,-,0,0</sub> |  | 0.3<br><sub>0,-,-,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.9 |
| DeAndre Jordan | 23% | 9.3<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.6 | 6.8 |
| AJ Johnson | 52% | 6.8<br><sub>-,-,-,3,12</sub> | 2.3<br><sub>-,-,-,2,2</sub> |  | 1.1<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,3</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.0 |
| Julian Reese | 52% | 6.3<br><sub>-,-,-,3,9</sub> | 2.3<br><sub>-,-,-,0,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.1 |

</details>

<details><summary>if Nolan Traore plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. (BKN) | 98% | 32.0<br><sub>36,37,38,36,29</sub> | 20.1<br><sub>23,18,26,25,19</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>9,5,10,9,9</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,2,0,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.9<br><sub>3,4,4,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.4 | 2.1 | 29.1 |
| Julius Randle (BKN) | 98% | 31.8<br><sub>37,36,31,34,30</sub> | 18.5<br><sub>20,21,22,19,13</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 6.7<br><sub>5,11,3,7,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>6,2,4,8,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>4,0,2,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.3 | 3.1 | 29.6 |
| Day'Ron Sharpe (BKN) | 98% | 22.2<br><sub>26,22,27,32,20</sub> | 9.5<br><sub>15,4,6,12,6</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 8.0<br><sub>13,6,5,10,4</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,3,8,13,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.2<br><sub>1,0,0,0,0</sub> |  | 1.1 | 0.9 | 1.7 | 20.9 |
| Mikel Brown Jr. (BKN) | 96% | 21.5<br><sub>-,27,20,25,-</sub> | 11.4<br><sub>-,13,18,18,-</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>-,2,2,1,-</sub> |  | 3.4<br><sub>-,3,4,3,-</sub> |  | 1.5<br><sub>-,1,3,3,-</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 1.8 | 17.0 |
| Nolan Traore (BKN) | 100% | 21.0<br><sub>30,24,27,23,21</sub> | 10.4<br><sub>16,17,16,19,14</sub> | 11.5 · – | 1.9<br><sub>2,3,4,1,1</sub> | 2.5 | 3.3<br><sub>6,4,2,2,2</sub> | 3.5 | 1.2<br><sub>4,5,2,2,2</sub> | 1.5 | 0.9 | 0.4 | 2.0 | 15.6 |
| Danny Wolf (BKN) | 66% | 20.9<br><sub>-,-,19,31,36</sub> | 8.1<br><sub>-,-,12,11,10</sub> |  | 5.1<br><sub>-,-,5,9,3</sub> |  | 2.1<br><sub>-,-,3,1,2</sub> |  | 1.0<br><sub>-,-,2,2,1</sub> |  | 0.6 | 0.5 | 1.2 | 15.3 |
| Egor Demin (BKN) | 91% | 19.0<br><sub>-,-,-,-,-</sub> | 7.2<br><sub>-,-,-,-,-</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.2 | 1.1 | 12.0 |
| Keon Ellis (BKN) | 80% | 17.3<br><sub>20,25,10,-,22</sub> | 4.4<br><sub>0,5,1,-,3</sub> |  | 1.7<br><sub>2,1,2,-,1</sub> |  | 1.2<br><sub>1,0,0,-,4</sub> |  | 0.6<br><sub>0,1,0,-,1</sub> |  | 1.0 | 0.5 | 0.6 | 7.3 |
| Moritz Wagner (BKN) | 96% | 16.2<br><sub>21,20,20,16,16</sub> | 9.3<br><sub>14,6,6,9,12</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>6,1,1,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>0,2,0,0,1</sub> |  | 0.7<br><sub>1,1,0,1,1</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 0.9 | 14.3 |
| Noah Clowney (BKN) | 98% | 15.6<br><sub>24,20,17,21,8</sub> | 5.4<br><sub>8,2,7,3,2</sub> |  | 3.0<br><sub>3,6,1,10,0</sub> |  | 0.8<br><sub>0,2,1,0,0</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 9.2 |
| Terance Mann (BKN) | 67% | 15.2<br><sub>15,-,16,13,22</sub> | 3.7<br><sub>0,-,0,0,0</sub> |  | 1.8<br><sub>1,-,2,2,1</sub> |  | 1.6<br><sub>1,-,2,0,1</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.6 | 7.1 |
| Chaney Johnson (BKN) | 96% | 13.8<br><sub>31,28,9,8,15</sub> | 3.9<br><sub>2,4,0,5,2</sub> |  | 1.9<br><sub>2,3,2,2,0</sub> |  | 0.8<br><sub>0,2,1,1,1</sub> |  | 0.3<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 6.6 |
| Josh Minott (BKN) | 58% | 9.9<br><sub>-,-,6,-,12</sub> | 5.4<br><sub>-,-,0,-,10</sub> |  | 1.9<br><sub>-,-,1,-,2</sub> |  | 0.6<br><sub>-,-,0,-,1</sub> |  | 0.6<br><sub>-,-,0,-,2</sub> |  | 0.6 | 0.3 | 0.6 | 7.8 |
| Drake Powell (BKN) | 52% | 8.6<br><sub>-,-,-,-,9</sub> | 2.7<br><sub>-,-,-,-,2</sub> |  | 0.8<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.1 |
| Trey Murphy III (NOP) | 92% | 33.0<br><sub>40,-,34,30,-</sub> | 18.0<br><sub>18,-,10,26,-</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>5,-,4,7,-</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 3.8<br><sub>5,-,5,3,-</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.6<br><sub>3,-,1,4,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.5 | 1.6 | 26.7 |
| Zion Williamson (NOP) | 98% | 32.2<br><sub>35,38,36,31,-</sub> | 19.8<br><sub>25,23,13,25,-</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>11,4,8,4,-</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,2,4,2,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 1.4 | 0.7 | 2.1 | 29.0 |
| Dejounte Murray (NOP) | 98% | 31.6<br><sub>-,45,35,28,18</sub> | 15.8<br><sub>-,20,7,6,12</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>-,8,2,3,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>-,4,4,3,1</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>-,1,1,0,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.8 | 0.4 | 2.7 | 27.5 |
| Jeremiah Fears (NOP) | 98% | 29.7<br><sub>38,34,36,29,29</sub> | 15.8<br><sub>12,19,24,25,11</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>4,6,5,6,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>7,2,5,5,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.5 | 2.6 | 25.0 |
| Saddiq Bey (NOP) | 98% | 27.0<br><sub>36,29,31,26,24</sub> | 14.6<br><sub>18,22,17,13,9</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,4,5,4,0</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>1,3,4,3,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>2,2,3,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.1 | 21.2 |
| Herbert Jones (NOP) | 98% | 21.3<br><sub>28,37,14,20,24</sub> | 6.3<br><sub>9,2,0,4,10</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>4,5,4,0,6</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>3,1,0,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>3,0,0,0,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.2 | 0.4 | 1.0 | 10.5 |
| Derik Queen (NOP) | 98% | 20.8<br><sub>24,27,10,21,21</sub> | 10.7<br><sub>20,20,6,8,16</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>7,9,4,5,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>5,6,1,3,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.9 | 0.9 | 1.9 | 19.6 |
| Jordan Poole (NOP) | 58% | 17.7<br><sub>-,-,-,-,34</sub> | 8.1<br><sub>-,-,-,-,7</sub> |  | 1.9<br><sub>-,-,-,-,3</sub> |  | 2.3<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.7 | 0.3 | 1.4 | 12.4 |
| Karlo Matkovic (NOP) | 96% | 17.0<br><sub>29,21,18,19,17</sub> | 6.9<br><sub>25,5,18,3,4</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>6,4,3,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.0<br><sub>1,2,1,2,2</sub> |  | 0.7<br><sub>5,1,4,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.6 | 0.8 | 0.8 | 11.9 |
| Bennedict Mathurin (NOP) | 98% | 15.1<br><sub>13,15,7,9,24</sub> | 6.9<br><sub>4,2,2,6,6</sub> |  | 2.6<br><sub>0,5,0,0,2</sub> |  | 1.2<br><sub>0,1,0,1,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 0.9 | 10.7 |
| Bryce McGowens (NOP) | 64% | 13.2<br><sub>6,-,-,3,28</sub> | 4.6<br><sub>0,-,-,0,8</sub> |  | 1.5<br><sub>1,-,-,0,2</sub> |  | 0.9<br><sub>0,-,-,0,0</sub> |  | 0.3<br><sub>0,-,-,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.0 |
| DeAndre Jordan (NOP) | 23% | 9.4<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.6 | 6.8 |
| AJ Johnson (NOP) | 52% | 6.7<br><sub>-,-,-,3,12</sub> | 2.2<br><sub>-,-,-,2,2</sub> |  | 1.0<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 3.9 |
| Julian Reese (NOP) | 52% | 6.2<br><sub>-,-,-,3,9</sub> | 2.3<br><sub>-,-,-,0,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.0 |

</details>


### ORL @ UTA
Out: Keyonte George (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Paolo Banchero (ORL), Tristan da Silva (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 36.7<br><sub>39,40,38,38,40</sub> | 26.2<br><sub>26,14,24,15,30</sub> | 23.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>5,6,3,8,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>11,12,6,15,11</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,1,1,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.4 | 3.5 | 39.9 |
| Desmond Bane | 98% | 35.4<br><sub>39,40,36,32,-</sub> | 22.5<br><sub>28,19,20,15,-</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>2,2,3,6,-</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>6,1,3,0,-</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>6,5,4,3,-</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.5 | 0.5 | 2.6 | 31.3 |
| Wendell Carter Jr. | 98% | 34.9<br><sub>39,35,34,34,40</sub> | 15.3<br><sub>20,7,6,27,19</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 9.6<br><sub>7,10,9,13,11</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,0,0,2,0</sub> |  | 1.1<br><sub>1,1,0,2,3</sub> |  | 1.1 | 1.0 | 1.9 | 27.2 |
| Anthony Black | 98% | 33.8<br><sub>31,33,-,31,38</sub> | 17.6<br><sub>17,23,-,10,18</sub> |  | 5.2<br><sub>6,8,-,7,8</sub> |  | 5.2<br><sub>10,3,-,6,6</sub> |  | 1.8<br><sub>3,1,-,1,2</sub> |  | 2.1 | 0.8 | 2.5 | 27.9 |
| Jamal Cain | 98% | 30.0<br><sub>15,18,25,25,36</sub> | 12.3<br><sub>13,5,10,5,18</sub> |  | 5.4<br><sub>0,1,3,5,12</sub> |  | 1.4<br><sub>0,1,1,0,1</sub> |  | 1.5<br><sub>3,1,2,1,2</sub> |  | 1.0 | 0.4 | 1.5 | 19.1 |
| Jase Richardson | 93% | 27.8<br><sub>33,26,29,26,30</sub> | 10.2<br><sub>4,4,9,10,2</sub> |  | 3.2<br><sub>6,1,1,2,4</sub> |  | 3.3<br><sub>2,3,5,3,4</sub> |  | 1.1<br><sub>0,0,0,2,0</sub> |  | 1.1 | 0.3 | 1.3 | 16.7 |
| Jevon Carter | 67% | 16.4<br><sub>-,-,18,3,15</sub> | 6.3<br><sub>-,-,5,0,9</sub> |  | 1.6<br><sub>-,-,1,0,1</sub> |  | 1.8<br><sub>-,-,4,0,0</sub> |  | 1.0<br><sub>-,-,1,0,3</sub> |  | 0.8 | 0.2 | 0.6 | 9.7 |
| Alex Morales | 72% | 14.0<br><sub>9,-,14,6,15</sub> | 3.0<br><sub>0,-,3,0,0</sub> |  | 2.1<br><sub>1,-,2,0,2</sub> |  | 1.0<br><sub>0,-,0,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.9 | 6.0 |
| Goga Bitadze | 76% | 12.0<br><sub>6,5,-,8,7</sub> | 4.6<br><sub>2,0,-,4,4</sub> |  | 4.4<br><sub>4,1,-,5,5</sub> |  | 1.0<br><sub>0,0,-,0,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.9 | 0.6 | 10.0 |
| Nikola Vucevic | 98% | 11.2<br><sub>6,7,14,4,6</sub> | 4.7<br><sub>3,2,7,0,0</sub> |  | 3.2<br><sub>1,4,6,0,1</sub> |  | 1.3<br><sub>0,2,1,0,2</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 9.2 |
| Colin Castleton | 48% | 7.5<br><sub>-,-,-,2,-</sub> | 2.5<br><sub>-,-,-,0,-</sub> |  | 2.3<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.3 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ace Bailey | 98% | 34.1<br><sub>37,24,35,29,32</sub> | 18.3<br><sub>9,5,15,12,7</sub> |  | 5.7<br><sub>7,6,5,6,2</sub> |  | 2.5<br><sub>1,2,1,0,3</sub> |  | 2.2<br><sub>1,1,1,0,1</sub> |  | 1.0 | 1.1 | 2.5 | 26.5 |
| Darryn Peterson | 98% | 34.0<br><sub>36,33,30,30,35</sub> | 19.0<br><sub>16,14,7,21,26</sub> |  | 4.4<br><sub>4,4,2,2,6</sub> |  | 4.7<br><sub>4,6,7,5,4</sub> |  | 2.0<br><sub>3,2,0,3,4</sub> |  | 1.1 | 1.0 | 2.3 | 28.0 |
| Jaxson Hayes | 98% | 29.3<br><sub>20,22,21,28,29</sub> | 11.5<br><sub>7,9,2,8,18</sub> |  | 6.9<br><sub>7,5,7,6,6</sub> |  | 1.8<br><sub>2,0,1,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.6 | 1.6 | 20.2 |
| Josh Green | 91% | 27.8<br><sub>2,15,23,24,28</sub> | 6.8<br><sub>0,3,7,3,10</sub> |  | 2.8<br><sub>0,1,1,3,0</sub> |  | 1.3<br><sub>0,0,0,1,1</sub> |  | 0.8<br><sub>0,1,1,1,1</sub> |  | 1.0 | 0.3 | 1.0 | 10.9 |
| Josh Okogie | 93% | 26.9<br><sub>14,19,26,24,17</sub> | 7.1<br><sub>0,9,3,12,0</sub> |  | 4.5<br><sub>1,3,6,4,1</sub> |  | 1.4<br><sub>0,2,1,0,0</sub> |  | 0.8<br><sub>0,1,1,2,0</sub> |  | 1.3 | 0.5 | 1.1 | 13.1 |
| Isaiah Collier | 98% | 22.5<br><sub>20,12,3,13,16</sub> | 11.2<br><sub>8,7,0,4,6</sub> |  | 3.0<br><sub>1,2,1,3,4</sub> |  | 5.6<br><sub>4,2,0,3,2</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.3 | 2.3 | 19.8 |
| Brice Sensabaugh | 98% | 21.9<br><sub>19,14,12,10,13</sub> | 14.4<br><sub>12,7,6,0,2</sub> |  | 3.4<br><sub>3,2,2,2,3</sub> |  | 1.8<br><sub>2,1,0,2,0</sub> |  | 2.0<br><sub>2,1,1,0,0</sub> |  | 0.7 | 0.3 | 1.9 | 19.6 |
| Svi Mykhailiuk | 93% | 20.1<br><sub>18,14,17,14,6</sub> | 8.4<br><sub>6,3,6,0,0</sub> |  | 2.3<br><sub>1,2,3,0,0</sub> |  | 1.5<br><sub>3,0,0,1,0</sub> |  | 1.3<br><sub>2,1,0,0,0</sub> |  | 0.6 | 0.1 | 0.9 | 12.2 |
| Mo Bamba | 67% | 19.9<br><sub>11,18,15,-,17</sub> | 6.7<br><sub>6,8,7,-,3</sub> |  | 7.0<br><sub>4,8,10,-,3</sub> |  | 1.0<br><sub>0,0,1,-,1</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.5 | 1.5 | 1.1 | 14.7 |
| Kyle Filipowski | 71% | 18.9<br><sub>6,8,-,1,15</sub> | 10.3<br><sub>5,1,-,0,9</sub> |  | 5.8<br><sub>0,2,-,0,6</sub> |  | 2.1<br><sub>2,0,-,0,1</sub> |  | 0.8<br><sub>1,0,-,0,1</sub> |  | 0.8 | 0.5 | 1.5 | 18.2 |
| Trey Alexander | 8% | 16.9 | 6.0 |  | 2.0 |  | 1.3 |  | 0.5 |  | 0.6 | 0.3 | 0.8 | 9.2 |
| Kobe Bufkin | 26% | 15.8<br><sub>-,-,-,-,-</sub> | 6.7<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.9 | 10.5 |
| Tony Bradley | 63% | 12.0<br><sub>-,7,-,1,2</sub> | 3.8<br><sub>-,2,-,0,0</sub> |  | 3.6<br><sub>-,3,-,1,1</sub> |  | 0.6<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.9 |
| Harrison Ingram | 16% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |

</details>


### GSW @ HOU
Out: Steven Adams (HOU), Clint Capela (HOU), Jimmy Butler III (GSW), Moses Moody (GSW), Gary Payton II (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.8–116.5 | GSW 32% | 3.17 / 1.46 | HOU -6.5 | 226.5 | HOU -6.5 covers 51%; o222.5 58% |
| Expected (weighted by chance each plays) | 109.7–116.4 | GSW 31% | 3.20 / 1.45 | HOU -6.5 | 225.5 | HOU -6.5 covers 51%; o222.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Will Richard (GSW) | Questionable | 55% | 15.8 | 4.1 | 1.8 | 0.9 | 0.5 | 0.8 | 0.1 | 0.5 | 6.8 | small |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 93% | 34.8<br><sub>37,33,32,39,26</sub> | 16.1<br><sub>17,20,9,15,25</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>8,3,6,7,2</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>8,2,3,1,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,3,2,4,5</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.3 | 1.8 | 25.0 |
| Yaxel Lendeborg | 98% | 34.0<br><sub>34,29,30,37,27</sub> | 20.1<br><sub>37,16,17,23,23</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>4,5,8,8,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>6,5,6,3,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>6,2,1,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.7 | 3.1 | 30.5 |
| Stephen Curry | 98% | 32.7<br><sub>-,33,28,36,21</sub> | 27.8<br><sub>-,34,29,41,25</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>-,6,1,6,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.6<br><sub>-,7,4,6,2</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>-,5,6,5,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.4 | 3.0 | 36.2 |
| Draymond Green | 91% | 28.9<br><sub>-,17,27,34,21</sub> | 6.8<br><sub>-,4,2,2,2</sub> |  | 5.0<br><sub>-,4,5,6,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.1<br><sub>-,2,11,13,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.8<br><sub>-,0,0,0,0</sub> |  | 1.1 | 0.7 | 2.4 | 17.8 |
| De'Anthony Melton | 98% | 24.2<br><sub>28,28,17,17,26</sub> | 10.1<br><sub>21,2,5,4,16</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>6,7,6,1,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>3,2,2,1,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5<br><sub>6,0,0,1,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.5 | 0.4 | 1.6 | 15.8 |
| Georges Niang | 98% | 22.5<br><sub>21,22,22,25,19</sub> | 8.4<br><sub>3,13,13,11,9</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,3,3,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4<br><sub>1,1,2,3,1</sub> | 1.5<br><sub>o 44% · u 55%</sub> | 0.5 | 0.2 | 1.0 | 12.5 |
| Gui Santos | 88% | 19.0<br><sub>9,-,-,12,21</sub> | 6.8<br><sub>4,-,-,3,3</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,-,-,1,7</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,-,-,0,4</sub> |  | 0.7<br><sub>0,-,-,0,0</sub> |  | 0.8 | 0.3 | 1.2 | 11.9 |
| Al Horford | 98% | 18.3<br><sub>22,-,18,13,15</sub> | 5.6<br><sub>9,-,8,2,5</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>5,-,5,5,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>2,-,1,4,6</sub> |  | 0.8<br><sub>3,-,2,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.5 | 0.8 | 0.6 | 11.0 |
| Charles Bassey | 97% | 15.1<br><sub>20,23,14,11,18</sub> | 6.6<br><sub>6,19,8,8,12</sub> |  | 5.8<br><sub>10,8,7,4,10</sub> |  | 0.6<br><sub>2,1,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.8 | 13.0 |
| LJ Cryer | 66% | 13.4<br><sub>2,1,1,-,20</sub> | 5.5<br><sub>0,0,0,-,10</sub> |  | 1.1<br><sub>0,0,0,-,0</sub> |  | 1.0<br><sub>0,0,0,-,3</sub> |  | 0.9<br><sub>0,0,0,-,2</sub> |  | 0.3 | 0.1 | 0.7 | 7.6 |
| Graham Ike | 88% | 11.5<br><sub>6,7,1,-,12</sub> | 4.0<br><sub>2,0,0,-,4</sub> |  | 2.8<br><sub>2,0,1,-,5</sub> |  | 0.7<br><sub>0,0,0,-,2</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.5 |
| Malevy Leons | 52% | 8.5<br><sub>-,-,1,-,12</sub> | 2.1<br><sub>-,-,0,-,0</sub> |  | 1.6<br><sub>-,-,0,-,3</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 4.1 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.7<br><sub>33,36,35,39,38</sub> | 16.2<br><sub>30,14,11,15,14</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>9,10,4,9,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>5,0,2,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>6,4,2,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.9 | 1.4 | 25.7 |
| Kevin Durant | 98% | 36.3<br><sub>27,33,35,38,36</sub> | 23.0<br><sub>14,12,21,21,23</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>3,3,5,10,12</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>4,3,2,3,8</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>0,0,2,1,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 1.1 | 3.4 | 34.1 |
| Alperen Sengun | 88% | 35.8<br><sub>33,38,39,32,35</sub> | 20.7<br><sub>16,26,17,15,20</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 9.8<br><sub>9,7,12,6,12</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>9,10,10,5,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 46% · u 54%</sub> | 1.4 | 1.2 | 3.0 | 37.3 |
| Amen Thompson | 98% | 35.5<br><sub>28,25,32,39,35</sub> | 16.1<br><sub>8,14,11,17,8</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>3,3,8,7,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>1,3,1,0,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.7 | 2.2 | 27.5 |
| Fred VanVleet | 88% | 32.5<br><sub>-,27,30,31,30</sub> | 13.7<br><sub>-,8,18,16,12</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>-,2,3,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.2<br><sub>-,9,3,4,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>-,2,4,4,3</sub> | 2.5<br><sub>o 46% · u 53%</sub> | 1.5 | 0.4 | 1.7 | 22.2 |
| Tari Eason | 98% | 23.2<br><sub>19,27,24,23,19</sub> | 9.4<br><sub>8,13,9,2,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>3,4,6,7,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>2,3,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>2,3,1,0,2</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.3 | 0.7 | 1.1 | 16.3 |
| Marcus Smart | 88% | 20.3<br><sub>36,20,18,20,17</sub> | 7.2<br><sub>24,8,4,5,5</sub> | 5.5 · –<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>5,4,1,2,2</sub> |  | 2.2<br><sub>3,4,1,0,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0<br><sub>7,2,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.2 | 0.3 | 1.3 | 11.6 |
| Reed Sheppard | 84% | 19.4<br><sub>-,17,21,13,17</sub> | 9.1<br><sub>-,8,14,6,8</sub> |  | 1.7<br><sub>-,1,2,0,0</sub> |  | 2.4<br><sub>-,1,2,0,0</sub> |  | 1.6<br><sub>-,2,3,2,2</sub> |  | 1.2 | 0.4 | 1.1 | 13.2 |
| Bogdan Bogdanovic | 96% | 11.2<br><sub>19,5,5,2,12</sub> | 4.2<br><sub>4,0,0,0,8</sub> |  | 1.4<br><sub>2,0,0,1,3</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 0.5<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.1 | 0.6 | 6.6 |
| Oscar Tshiebwe | 91% | 7.7<br><sub>4,7,2,3,-</sub> | 3.2<br><sub>2,4,2,2,-</sub> |  | 3.0<br><sub>1,1,0,0,-</sub> |  | 0.4<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.6 |
| Isaiah Crawford | 58% | 6.4<br><sub>19,2,-,-,1</sub> | 2.2<br><sub>8,0,-,-,0</sub> |  | 0.9<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>2,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.2 | 3.4 |
| Jae'Sean Tate | 52% | 6.0<br><sub>6,2,-,-,-</sub> | 2.0<br><sub>0,0,-,-,-</sub> |  | 1.4<br><sub>3,1,-,-,-</sub> |  | 0.4<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Bruce Thornton | 58% | 5.8<br><sub>6,2,-,-,1</sub> | 2.1<br><sub>5,2,-,-,0</sub> |  | 1.6<br><sub>1,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>1,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |

</details>


### OKC @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.4<br><sub>31,39,35,30,29</sub> | 30.7<br><sub>26,43,42,28,30</sub> | 32.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,3,4,3,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>3,8,8,4,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>3,4,5,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.5 | 1.0 | 3.0 | 41.4 |
| Ajay Mitchell | 98% | 28.5<br><sub>26,35,32,30,22</sub> | 17.2<br><sub>6,20,23,35,12</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>3,5,7,1,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>5,1,4,5,0</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>0,0,1,4,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.5 | 0.4 | 1.9 | 24.6 |
| Jared McCain | 98% | 26.5<br><sub>28,27,25,29,23</sub> | 12.9<br><sub>10,7,9,21,19</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>4,9,1,5,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.7<br><sub>2,2,0,0,2</sub> |  | 1.8<br><sub>0,0,1,3,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 1.7 | 17.7 |
| Isaiah Hartenstein | 98% | 26.2<br><sub>25,28,26,26,18</sub> | 9.6<br><sub>10,5,3,2,2</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 10.1<br><sub>7,14,12,6,14</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>0,4,4,7,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.3 | 0.8 | 1.6 | 23.3 |
| Aday Mara | 98% | 24.0<br><sub>28,20,25,18,27</sub> | 9.7<br><sub>7,10,9,9,18</sub> |  | 7.0<br><sub>9,9,5,7,8</sub> |  | 1.4<br><sub>3,0,2,0,3</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.5 | 1.8 | 1.7 | 18.1 |
| Bennett Stirtz | 98% | 23.7<br><sub>26,12,22,24,29</sub> | 8.0<br><sub>11,9,16,12,11</sub> |  | 1.9<br><sub>1,2,1,1,5</sub> |  | 1.6<br><sub>3,0,1,2,3</sub> |  | 1.2<br><sub>3,3,4,2,2</sub> |  | 0.7 | 0.2 | 0.9 | 11.5 |
| Kenrich Williams | 98% | 23.2<br><sub>21,31,29,19,23</sub> | 8.3<br><sub>11,12,13,4,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>7,3,4,6,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>3,1,2,3,2</sub> |  | 1.1<br><sub>3,2,3,1,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.7 | 0.2 | 0.9 | 15.0 |
| Micah Peavy | 86% | 20.7<br><sub>14,16,26,18,23</sub> | 5.5<br><sub>2,8,2,7,7</sub> |  | 3.8<br><sub>1,5,9,4,3</sub> |  | 1.1<br><sub>0,0,1,0,0</sub> |  | 0.5<br><sub>0,2,0,1,1</sub> |  | 0.8 | 0.3 | 0.7 | 10.4 |
| Alex Caruso | 98% | 20.7<br><sub>-,-,20,20,13</sub> | 7.3<br><sub>-,-,7,5,0</sub> |  | 3.2<br><sub>-,-,4,6,3</sub> |  | 2.4<br><sub>-,-,3,2,3</sub> |  | 1.0<br><sub>-,-,1,1,0</sub> |  | 1.3 | 0.4 | 0.9 | 12.9 |
| Josh Dix | 76% | 18.4<br><sub>9,12,-,15,21</sub> | 4.2<br><sub>7,0,-,5,2</sub> |  | 1.7<br><sub>0,1,-,2,1</sub> |  | 0.8<br><sub>0,0,-,1,2</sub> |  | 0.4<br><sub>1,0,-,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 6.7 |
| Brooks Barnhizer | 67% | 9.9<br><sub>6,-,-,5,8</sub> | 2.5<br><sub>5,-,-,0,2</sub> |  | 2.2<br><sub>2,-,-,0,4</sub> |  | 0.7<br><sub>0,-,-,0,3</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 5.4 |
| Nique Clifford | 91% | 9.7<br><sub>11,3,3,5,-</sub> | 3.5<br><sub>0,0,0,5,-</sub> |  | 1.5<br><sub>1,1,2,2,-</sub> |  | 1.1<br><sub>2,0,0,2,-</sub> |  | 0.2<br><sub>0,0,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.1 |
| Nikola Topic | 16% | 7.6 | 2.5 |  | 0.9 |  | 1.6 |  | 0.1 |  | 0.3 | 0.1 | 0.8 | 4.9 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 32.6<br><sub>30,35,35,39,24</sub> | 20.7<br><sub>24,28,21,22,15</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>5,3,7,9,4</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 6.4<br><sub>2,5,12,11,1</sub> |  | 1.7<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 3.6 | 33.7 |
| Damian Lillard | 98% | 30.0<br><sub>27,30,33,37,20</sub> | 16.5<br><sub>22,20,25,22,12</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>5,6,3,0,0</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.2<br><sub>4,6,5,4,7</sub> |  | 2.1<br><sub>3,1,2,4,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 2.4 | 25.3 |
| Toumani Camara | 98% | 28.4<br><sub>31,31,32,30,21</sub> | 11.5<br><sub>14,9,11,18,4</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>4,5,4,6,4</sub> |  | 1.6<br><sub>0,1,2,1,0</sub> |  | 2.0<br><sub>4,3,1,4,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.4 | 1.4 | 17.3 |
| Jrue Holiday | 98% | 26.9<br><sub>22,31,28,31,20</sub> | 12.5<br><sub>14,17,15,12,11</sub> |  | 3.9<br><sub>4,8,4,1,0</sub> |  | 4.5<br><sub>3,10,0,7,0</sub> |  | 1.8<br><sub>2,3,5,3,1</sub> |  | 0.8 | 0.2 | 2.0 | 21.0 |
| Donovan Clingan | 98% | 24.8<br><sub>15,32,29,28,22</sub> | 10.8<br><sub>4,17,24,17,6</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 9.6<br><sub>9,18,11,11,5</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,3,1,1,0</sub> |  | 1.1<br><sub>0,1,1,3,0</sub> |  | 0.5 | 1.4 | 1.3 | 22.1 |
| Scoot Henderson | 98% | 24.1<br><sub>31,26,22,23,24</sub> | 10.8<br><sub>14,8,9,2,13</sub> |  | 2.5<br><sub>3,2,2,2,2</sub> |  | 2.5<br><sub>1,2,1,0,1</sub> |  | 1.3<br><sub>1,2,1,0,0</sub> |  | 0.8 | 0.2 | 2.4 | 15.8 |
| Sidy Cissoko | 98% | 18.1<br><sub>19,22,21,22,16</sub> | 5.3<br><sub>1,8,7,7,4</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,3,4,2,3</sub> |  | 1.6<br><sub>1,0,4,3,1</sub> |  | 0.6<br><sub>0,2,1,2,0</sub> |  | 0.6 | 0.3 | 0.9 | 9.5 |
| Chris Youngblood | 88% | 18.1<br><sub>7,15,4,11,30</sub> | 7.2<br><sub>3,7,0,7,11</sub> |  | 2.3<br><sub>0,2,0,1,4</sub> |  | 1.5<br><sub>0,1,1,0,4</sub> |  | 1.3<br><sub>1,1,0,2,2</sub> |  | 0.5 | 0.3 | 0.8 | 11.1 |
| Robert Williams III | 98% | 14.7<br><sub>14,15,16,16,-</sub> | 5.7<br><sub>3,2,9,9,-</sub> |  | 5.4<br><sub>3,6,8,5,-</sub> |  | 1.0<br><sub>1,2,1,2,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 1.0 | 0.8 | 12.1 |
| Yang Hansen | 72% | 11.0<br><sub>13,-,2,3,26</sub> | 4.6<br><sub>6,-,0,2,12</sub> |  | 2.9<br><sub>5,-,0,0,10</sub> |  | 0.6<br><sub>1,-,0,0,1</sub> |  | 0.4<br><sub>2,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.8 | 8.1 |
| Jayson Kent | 64% | 9.9<br><sub>-,-,-,-,12</sub> | 4.0<br><sub>-,-,-,-,4</sub> |  | 1.5<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 6.0 |
| Micah Potter | 63% | 9.5<br><sub>4,-,2,-,14</sub> | 4.2<br><sub>2,-,4,-,7</sub> |  | 2.5<br><sub>1,-,1,-,3</sub> |  | 0.5<br><sub>0,-,0,-,1</sub> |  | 0.4<br><sub>0,-,1,-,1</sub> |  | 0.2 | 0.2 | 0.6 | 7.2 |
| Branden Carlson | 58% | 7.8<br><sub>4,-,3,-,12</sub> | 2.6<br><sub>0,-,2,-,4</sub> |  | 1.7<br><sub>2,-,0,-,2</sub> |  | 0.4<br><sub>1,-,0,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.3 | 0.4 | 4.7 |
| John Tonje | 52% | 5.9<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-11/`._
