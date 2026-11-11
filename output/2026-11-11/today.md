# NBA model · Wed 11 Nov 2026 (US date)

Updated **Thu 12 Nov, 09:40 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-11/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| OKC to win | OKC @ POR | draftkings | 2.24 | 1.92 | 1.86 | 53.8% | 52.0% | 52.0% | +16.6% | +20.4% | 2.0% |
| GSW to win | GSW @ HOU | draftkings | 3.17 | 3.01 | 3.16 | 31.6% | 33.2% | 33.2% | +5.2% | +0.3% | 0.6% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard AST over 13.5 (14+) | WAS @ IND | draftkings | 23.00 | 17.99 | 6.48 | 15.4% | 4.1% | 5.6% | +27.9% | +254.7% | 0.3% |
| MIL to win | LAL @ MIL | draftkings | 6.80 | 5.74 | 4.00 | 25.0% | 17.4% | 17.4% | +18.4% | +69.9% | 0.8% |
| Kevin Durant AST over 7.5 (8+) | GSW @ HOU | draftkings | 18.80 | 16.34 | 7.32 | 13.7% | 5.0% | 6.1% | +15.0% | +156.9% | 0.2% |
| CHI to win | SAS @ CHI | betfair_ex_au | 9.55 | 8.34 | 5.00 | 20.0% | 12.0% | 12.0% | +14.5% | +91.0% | 0.4% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ POR | draftkings | 13.60 | 11.90 | 5.43 | 18.4% | 6.9% | 8.4% | +14.2% | +150.6% | 0.3% |
| Pascal Siakam PRA over 49.5 (50+) | WAS @ IND | draftkings | 15.00 | 13.50 | 6.58 | 15.2% | 6.2% | 7.4% | +11.2% | +128.0% | 0.2% |
| Pascal Siakam PTS over 39.5 (40+) | WAS @ IND | draftkings | 24.00 | 21.74 | 10.80 | 9.3% | 3.9% | 4.6% | +10.5% | +122.3% | 0.1% |
| Pascal Siakam PRA over 54.5 (55+) | WAS @ IND | draftkings | 25.00 | 22.68 | 11.37 | 8.8% | 3.7% | 4.4% | +10.1% | +119.8% | 0.1% |
| Andrew Nembhard PRA over 39.5 (40+) | WAS @ IND | draftkings | 11.00 | 10.13 | 5.29 | 18.9% | 8.5% | 9.9% | +8.6% | +107.9% | 0.2% |
| Dejounte Murray AST over 9.5 (10+) | BKN @ NOP | draftkings | 13.40 | 12.38 | 6.51 | 15.3% | 7.0% | 8.1% | +8.3% | +105.7% | 0.2% |
| Andrew Nembhard PRA over 44.5 (45+) | WAS @ IND | draftkings | 21.00 | 19.42 | 10.23 | 9.8% | 4.5% | 5.1% | +8.2% | +105.3% | 0.1% |
| DeMar DeRozan AST over 5.5 (6+) | DEN @ MEM | draftkings | 13.80 | 12.84 | 6.89 | 14.5% | 6.8% | 7.8% | +7.6% | +100.3% | 0.1% |
| Pascal Siakam PR over 44.5 (45+) | WAS @ IND | draftkings | 14.00 | 13.12 | 7.22 | 13.9% | 6.7% | 7.6% | +6.7% | +93.9% | 0.1% |
| Pascal Siakam PTS over 34.5 (35+) | WAS @ IND | draftkings | 11.20 | 10.50 | 5.80 | 17.2% | 8.3% | 9.5% | +6.6% | +93.0% | 0.2% |
| Pascal Siakam PRA over 44.5 (45+) | WAS @ IND | draftkings | 7.40 | 6.97 | 3.91 | 25.6% | 12.6% | 14.3% | +6.1% | +89.4% | 0.2% |
| Pascal Siakam PR over 49.5 (50+) | WAS @ IND | draftkings | 24.00 | 22.68 | 12.81 | 7.8% | 3.9% | 4.4% | +5.9% | +87.4% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| WAS @ IND | Thu 12 Nov 11:00 | 114.1–119.8 | WAS 34% | 2.90 / 1.53 | IND -5.5 | 233.5 | IND -3.5 covers 57%; o227.5 63% |
| CLE @ NYK | Thu 12 Nov 11:00 | 109.3–113.6 | CLE 38% | 2.64 / 1.61 | NYK -4.5 | 222.5 | NYK -4.5 covers 50%; o222.5 50% |
| BOS @ TOR | Thu 12 Nov 11:00 | 112.3–107.0 | BOS 65% | 1.54 / 2.86 | TOR +5.5 | 219.5 | TOR +5.5 covers 50%; o215.5 58% |
| SAS @ CHI | Thu 12 Nov 12:00 | 123.1–109.4 | SAS 84% | 1.20 / 6.10 | CHI +13.5 | 232.5 | CHI +15.5 covers 55%; o237.5 39% |
| DEN @ MEM | Thu 12 Nov 12:00 | 120.8–118.4 | DEN 57% | 1.74 / 2.34 | MEM +2.5 | 238.5 | MEM +4.5 covers 55%; o230.5 68% |
| LAL @ MIL | Thu 12 Nov 12:00 | 118.3–108.0 | LAL 77% | 1.30 / 4.36 | MIL +10.5 | 226.5 | MIL +14.5 covers 62%; o229.5 43% |
| BKN @ NOP | Thu 12 Nov 12:00 | 108.6–113.6 | BKN 36% | 2.78 / 1.56 | NOP -5.5 | 221.5 | NOP -3.5 covers 55%; o228.5 36% |
| ORL @ UTA | Thu 12 Nov 13:00 | 111.7–108.4 | ORL 59% | 1.70 / 2.44 | UTA +3.5 | 220.5 | UTA +4.5 covers 53%; o214.5 62% |
| GSW @ HOU | Thu 12 Nov 13:30 | 109.7–116.3 | GSW 32% | 3.16 / 1.46 | HOU -6.5 | 225.5 | HOU -6.5 covers 51%; o219.5 63% |
| OKC @ POR | Thu 12 Nov 14:00 | 111.9–110.4 | OKC 54% | 1.86 / 2.16 | POR +1.5 | 222.5 | POR -2.5 covers 40%; o224.5 45% |

### WAS @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.1–119.8 | WAS 34% | 2.90 / 1.53 | IND -5.5 | 233.5 | IND -3.5 covers 57%; o227.5 63% |
| Expected (weighted by chance each plays) | 113.8–120.1 | WAS 33% | 3.06 / 1.49 | IND -6.5 | 233.5 | IND -3.5 covers 59%; o227.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| T.J. McConnell (IND) | Questionable | 55% | 12.3 | 6.4 | 1.8 | 4.0 | 0.1 | 0.8 | 0.1 | 0.9 | 12.2 | small |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 34.5<br><sub>34,34,37,28,38</sub> | 19.0<br><sub>15,18,23,4,20</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>3,2,2,5,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 9.6<br><sub>9,6,10,3,7</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>2,2,3,0,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.0 | 32.0 |
| Anthony Davis | 98% | 33.3<br><sub>34,30,-,-,34</sub> | 22.5<br><sub>27,26,-,-,44</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 11.8<br><sub>9,10,-,-,13</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>1,3,-,-,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>1,0,-,-,2</sub> |  | 1.2 | 1.6 | 2.1 | 37.0 |
| Kyshawn George | 98% | 33.1<br><sub>37,35,39,30,35</sub> | 16.2<br><sub>22,25,33,14,12</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>4,4,4,7,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>5,7,7,6,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>4,3,5,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 1.0 | 2.2 | 26.0 |
| AJ Dybantsa | 96% | 32.8<br><sub>33,32,36,31,37</sub> | 15.7<br><sub>21,9,11,19,21</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>5,6,9,6,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>2,3,3,3,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>1,0,1,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.4 | 2.0 | 24.5 |
| Alex Sarr | 98% | 25.2<br><sub>-,23,30,28,25</sub> | 11.4<br><sub>-,11,13,15,4</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>-,9,8,14,8</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>-,1,3,1,0</sub> |  | 0.8<br><sub>-,0,1,1,0</sub> |  | 0.8 | 1.3 | 1.3 | 20.7 |
| Bilal Coulibaly | 98% | 22.6<br><sub>33,23,24,20,-</sub> | 7.9<br><sub>7,6,9,0,-</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 3.6<br><sub>1,2,5,5,-</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>2,2,0,0,-</sub> |  | 0.7<br><sub>0,0,1,0,-</sub> |  | 1.1 | 0.7 | 1.0 | 13.0 |
| Tre Johnson | 91% | 20.9<br><sub>22,14,27,28,29</sub> | 7.6<br><sub>4,3,23,4,2</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>3,2,1,0,2</sub> |  | 1.0<br><sub>0,0,1,3,0</sub> |  | 1.1<br><sub>0,1,5,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 0.8 | 10.8 |
| Bub Carrington | 98% | 18.0<br><sub>19,19,15,21,19</sub> | 5.8<br><sub>3,0,5,9,4</sub> |  | 2.1<br><sub>4,1,1,6,0</sub> |  | 2.5<br><sub>4,2,1,1,4</sub> |  | 0.8<br><sub>1,0,1,3,1</sub> |  | 0.6 | 0.1 | 1.0 | 10.4 |
| Deandre Ayton | 98% | 14.4<br><sub>24,11,23,7,13</sub> | 5.2<br><sub>4,5,8,2,2</sub> |  | 4.9<br><sub>6,4,11,1,8</sub> |  | 0.6<br><sub>2,1,3,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 10.8 |
| Will Riley | 91% | 9.1<br><sub>4,13,9,20,4</sub> | 3.7<br><sub>0,0,7,5,0</sub> |  | 1.1<br><sub>0,0,0,2,0</sub> |  | 0.7<br><sub>1,0,0,1,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.6 |
| Khris Middleton | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.1 |
| Anthony Gill | 52% | 6.9<br><sub>-,-,-,9,2</sub> | 2.4<br><sub>-,-,-,1,0</sub> |  | 1.3<br><sub>-,-,-,1,2</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Tre Mann | 63% | 6.3<br><sub>-,3,-,18,2</sub> | 2.7<br><sub>-,2,-,2,0</sub> |  | 0.8<br><sub>-,0,-,0,0</sub> |  | 0.8<br><sub>-,0,-,2,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Felix Okpara | 58% | 5.9<br><sub>-,3,-,-,2</sub> | 2.5<br><sub>-,0,-,-,2</sub> |  | 1.7<br><sub>-,1,-,-,1</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.6 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 86% | 33.5<br><sub>35,-,38,31,34</sub> | 18.7<br><sub>23,-,22,9,12</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>3,-,2,1,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 10.0<br><sub>4,-,5,8,12</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>4,-,2,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2 | 0.2 | 2.5 | 32.0 |
| Pascal Siakam | 88% | 33.1<br><sub>36,-,30,32,35</sub> | 25.6<br><sub>17,-,20,23,29</sub> | 21.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>5,-,4,2,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,-,2,5,8</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,-,2,2,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.4 | 2.2 | 38.1 |
| Aaron Nesmith | 88% | 29.7<br><sub>30,-,30,27,34</sub> | 16.2<br><sub>11,-,16,8,18</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>3,-,2,5,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>4,-,2,1,2</sub> |  | 2.2<br><sub>0,-,2,2,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.5 | 1.6 | 22.9 |
| Ivica Zubac | 63% | 24.5<br><sub>-,-,19,19,28</sub> | 12.0<br><sub>-,-,1,10,16</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 9.6<br><sub>-,-,4,12,3</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>-,-,2,5,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.8 | 1.5 | 23.6 |
| Quenton Jackson | 98% | 23.6<br><sub>24,35,22,17,25</sub> | 11.9<br><sub>12,20,13,6,10</sub> |  | 3.6<br><sub>3,7,7,4,5</sub> |  | 4.4<br><sub>2,3,2,1,4</sub> |  | 1.0<br><sub>3,1,3,0,2</sub> |  | 1.1 | 0.2 | 1.4 | 20.0 |
| Kelly Oubre Jr. | 71% | 22.9<br><sub>20,-,-,16,23</sub> | 10.3<br><sub>11,-,-,2,14</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>2,-,-,1,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>1,-,-,0,2</sub> |  | 0.9<br><sub>2,-,-,0,1</sub> |  | 1.0 | 0.4 | 1.0 | 15.3 |
| Jarace Walker | 98% | 20.7<br><sub>20,45,17,20,10</sub> | 9.9<br><sub>6,15,2,9,7</sub> |  | 5.0<br><sub>6,7,8,5,1</sub> |  | 2.4<br><sub>3,3,1,2,0</sub> |  | 1.2<br><sub>2,1,0,1,2</sub> |  | 0.7 | 0.4 | 1.3 | 17.3 |
| Obi Toppin | 67% | 20.5<br><sub>-,-,19,22,19</sub> | 13.5<br><sub>-,-,11,10,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>-,-,5,7,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>-,-,1,2,4</sub> |  | 1.7<br><sub>-,-,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.3 | 1.2 | 21.0 |
| Jay Huff | 72% | 16.8<br><sub>17,40,14,10,-</sub> | 8.1<br><sub>0,22,6,0,-</sub> |  | 3.6<br><sub>3,8,3,3,-</sub> |  | 1.3<br><sub>0,2,1,0,-</sub> |  | 0.9<br><sub>0,0,2,0,-</sub> |  | 0.5 | 1.2 | 0.8 | 13.0 |
| Kobe Brown | 72% | 15.4<br><sub>15,38,7,-,-</sub> | 5.7<br><sub>3,16,0,-,-</sub> |  | 2.9<br><sub>1,6,1,-,-</sub> |  | 1.6<br><sub>1,1,0,-,-</sub> |  | 0.6<br><sub>1,2,0,-,-</sub> |  | 0.5 | 0.2 | 0.8 | 10.3 |
| Larry Nance Jr. | 93% | 13.9<br><sub>26,-,14,13,14</sub> | 4.6<br><sub>4,-,4,15,4</sub> |  | 3.0<br><sub>6,-,4,2,0</sub> |  | 1.0<br><sub>1,-,1,1,0</sub> |  | 0.5<br><sub>1,-,0,5,0</sub> |  | 0.8 | 0.3 | 0.6 | 8.6 |
| Braden Smith | 91% | 13.9<br><sub>1,42,24,12,10</sub> | 4.5<br><sub>0,19,10,0,0</sub> |  | 1.5<br><sub>0,4,1,0,0</sub> |  | 2.7<br><sub>0,10,5,2,0</sub> |  | 0.2<br><sub>0,2,0,0,0</sub> |  | 0.7 | 0.3 | 0.9 | 8.7 |
| Jalen Slawson | 72% | 13.1<br><sub>18,41,6,12,-</sub> | 4.2<br><sub>3,12,2,4,-</sub> |  | 2.7<br><sub>5,7,2,1,-</sub> |  | 1.4<br><sub>0,3,1,2,-</sub> |  | 0.3<br><sub>0,2,0,0,-</sub> |  | 0.8 | 0.6 | 0.7 | 8.3 |

</details>


### CLE @ NYK
Out: Sam Merrill (CLE)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.3–113.6 | CLE 38% | 2.64 / 1.61 | NYK -4.5 | 222.5 | NYK -4.5 covers 50%; o222.5 50% |
| Expected (weighted by chance each plays) | 109.2–113.3 | CLE 38% | 2.60 / 1.63 | NYK -4.5 | 222.5 | NYK -4.5 covers 50%; o222.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaylon Tyson (CLE) | Questionable | 55% | 15.0 | 5.5 | 2.7 | 1.3 | 0.7 | 0.4 | 0.2 | 0.7 | 9.5 | small |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 34.6<br><sub>33,35,30,34,25</sub> | 15.8<br><sub>14,19,17,7,11</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>4,9,6,2,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.6<br><sub>6,6,3,5,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>3,3,3,1,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.5 | 3.1 | 25.9 |
| Donovan Mitchell | 98% | 34.6<br><sub>36,33,33,37,23</sub> | 22.6<br><sub>17,27,23,37,11</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>5,3,7,4,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>11,6,8,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,5,1,5,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 2.8 | 31.8 |
| Evan Mobley | 98% | 32.9<br><sub>33,33,32,33,24</sub> | 15.2<br><sub>16,16,22,12,9</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>7,10,6,9,2</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 3.4<br><sub>4,3,4,5,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>1,1,3,1,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 1.3 | 1.9 | 26.0 |
| Peyton Watson | 98% | 27.8<br><sub>-,-,28,29,21</sub> | 11.5<br><sub>-,-,13,12,13</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>-,-,9,6,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>-,-,2,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>-,-,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 1.1 | 1.5 | 17.7 |
| Jarrett Allen | 98% | 25.3<br><sub>28,7,-,-,19</sub> | 11.2<br><sub>14,0,-,-,12</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>6,1,-,-,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,0,-,-,1</sub> |  | 0.1<br><sub>0,0,-,-,1</sub> |  | 0.7 | 1.1 | 1.2 | 19.2 |
| Meleek Thomas | 91% | 24.6<br><sub>26,18,27,24,27</sub> | 10.2<br><sub>17,9,12,9,18</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>5,1,1,4,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>1,0,3,0,3</sub> |  | 1.7<br><sub>3,3,2,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.3 | 1.1 | 14.1 |
| Tyrese Proctor | 91% | 20.9<br><sub>19,22,19,23,23</sub> | 6.9<br><sub>10,11,3,7,6</sub> |  | 2.7<br><sub>4,1,6,3,1</sub> |  | 2.4<br><sub>2,0,3,3,4</sub> |  | 1.0<br><sub>2,2,0,2,0</sub> |  | 0.8 | 0.1 | 0.9 | 12.0 |
| Mario Hezonja | 98% | 19.4<br><sub>27,23,27,19,17</sub> | 7.6<br><sub>12,12,15,0,10</sub> |  | 4.8<br><sub>8,8,10,5,3</sub> |  | 1.3<br><sub>3,1,1,1,0</sub> |  | 1.0<br><sub>3,2,2,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 13.6 |
| Craig Porter Jr. | 88% | 14.1<br><sub>8,14,3,15,17</sub> | 2.9<br><sub>0,0,0,0,9</sub> |  | 2.1<br><sub>4,1,0,1,2</sub> |  | 2.0<br><sub>1,1,0,1,4</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.7 | 7.0 |
| Thomas Bryant | 80% | 13.6<br><sub>5,13,16,15,15</sub> | 6.0<br><sub>4,8,13,5,11</sub> |  | 3.1<br><sub>0,0,6,3,2</sub> |  | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.7<br><sub>0,1,1,1,2</sub> |  | 0.3 | 0.4 | 0.6 | 9.7 |
| Riley Minix | 52% | 12.4<br><sub>-,-,-,10,17</sub> | 4.4<br><sub>-,-,-,8,2</sub> |  | 1.9<br><sub>-,-,-,3,2</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.3 | 0.2 | 0.4 | 6.9 |
| Norchad Omier | 63% | 9.0<br><sub>-,-,3,-,12</sub> | 2.9<br><sub>-,-,0,-,0</sub> |  | 2.0<br><sub>-,-,2,-,3</sub> |  | 1.0<br><sub>-,-,1,-,2</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 5.9 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 33.8<br><sub>35,34,28,34,28</sub> | 24.3<br><sub>24,19,33,31,23</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,2,2,6,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.0<br><sub>6,6,4,9,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>3,4,5,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.1 | 2.2 | 33.4 |
| OG Anunoby | 98% | 33.0<br><sub>34,38,24,34,29</sub> | 17.4<br><sub>9,18,18,15,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>4,4,5,6,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.3<br><sub>1,3,1,3,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.7 | 1.4 | 24.7 |
| Karl-Anthony Towns | 98% | 30.9<br><sub>35,35,25,34,27</sub> | 18.9<br><sub>22,11,17,29,21</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 12.5<br><sub>12,16,12,13,16</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>3,5,1,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>3,1,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.6 | 2.6 | 34.9 |
| Josh Hart | 98% | 29.4<br><sub>31,27,-,-,-</sub> | 9.6<br><sub>7,8,-,-,-</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>6,6,-,-,-</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>3,7,-,-,-</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>2,2,-,-,-</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.2 | 1.5 | 20.3 |
| Mikal Bridges | 98% | 25.9<br><sub>30,16,22,31,17</sub> | 9.7<br><sub>12,6,7,9,4</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>5,2,4,6,5</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>2,0,4,4,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>2,0,1,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.4 | 0.8 | 14.8 |
| Landry Shamet | 98% | 24.0<br><sub>16,30,25,29,28</sub> | 8.5<br><sub>0,22,7,9,10</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>0,1,2,1,3</sub> |  | 1.3<br><sub>0,1,2,1,2</sub> |  | 1.6<br><sub>0,4,1,3,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 0.1 | 0.7 | 11.5 |
| Miles McBride | 98% | 18.2<br><sub>24,17,11,16,25</sub> | 6.4<br><sub>10,6,7,5,8</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,1,1,0,0</sub> |  | 1.4<br><sub>1,2,1,0,3</sub> |  | 1.1<br><sub>2,2,2,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.1 | 0.5 | 9.3 |
| Andre Drummond | 98% | 13.4<br><sub>12,13,12,14,16</sub> | 4.3<br><sub>3,4,6,0,2</sub> |  | 6.3<br><sub>6,9,9,8,14</sub> |  | 1.0<br><sub>1,0,0,0,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.4 | 0.7 | 11.6 |
| Mohamed Diawara | 67% | 12.6<br><sub>-,6,21,14,18</sub> | 4.3<br><sub>-,0,8,2,5</sub> |  | 2.1<br><sub>-,1,6,3,3</sub> |  | 1.5<br><sub>-,0,4,3,3</sub> |  | 0.5<br><sub>-,0,1,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.9 |
| Tyler Kolek | 88% | 12.5<br><sub>13,5,11,14,15</sub> | 4.1<br><sub>2,2,0,0,12</sub> |  | 1.6<br><sub>1,1,0,4,3</sub> |  | 3.5<br><sub>4,1,5,5,4</sub> |  | 0.5<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.1 | 0.7 | 9.2 |
| Jordan Clarkson | 91% | 11.8<br><sub>9,11,15,15,11</sub> | 5.8<br><sub>4,7,10,9,2</sub> |  | 1.6<br><sub>3,0,1,2,4</sub> |  | 0.8<br><sub>0,0,1,0,2</sub> |  | 0.5<br><sub>0,1,2,1,0</sub> |  | 0.3 | 0.1 | 0.7 | 8.3 |
| Jose Alvarado | 80% | 9.0<br><sub>-,9,9,-,6</sub> | 3.4<br><sub>-,0,0,-,0</sub> |  | 1.1<br><sub>-,0,0,-,1</sub> |  | 1.4<br><sub>-,0,2,-,1</sub> |  | 0.3<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.1 | 0.5 | 5.9 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Dalton Knecht | 64% | 8.1<br><sub>-,-,16,5,8</sub> | 3.4<br><sub>-,-,10,0,3</sub> |  | 1.6<br><sub>-,-,7,0,0</sub> |  | 0.5<br><sub>-,-,1,0,0</sub> |  | 0.4<br><sub>-,-,2,0,1</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| Jaden Akins | 38% | 6.5<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.0 |
| James Wiseman | 58% | 6.5<br><sub>-,-,10,-,5</sub> | 2.3<br><sub>-,-,8,-,0</sub> |  | 2.1<br><sub>-,-,8,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.1 | 0.3 | 0.4 | 4.8 |
| Pacome Dadiet | 52% | 6.1<br><sub>-,-,9,-,6</sub> | 2.7<br><sub>-,-,4,-,8</sub> |  | 1.2<br><sub>-,-,0,-,2</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,1</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |

</details>


### BOS @ TOR
Out: Scottie Barnes (TOR), Kawhi Leonard (TOR), Malachi Smith (TOR), Devin Carter (BOS), Paul George (BOS)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 35.7<br><sub>32,-,29,29,32</sub> | 27.8<br><sub>19,-,34,21,21</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 8.2<br><sub>6,-,8,4,6</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>9,-,9,6,4</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>1,-,5,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.5 | 3.4 | 42.4 |
| Derrick White | 98% | 31.9<br><sub>30,36,25,27,22</sub> | 14.4<br><sub>7,24,18,9,5</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>2,4,4,3,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>3,7,5,7,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,1,4,1,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.8 | 2.1 | 22.5 |
| Payton Pritchard | 98% | 29.5<br><sub>30,18,23,29,30</sub> | 15.7<br><sub>4,10,12,12,18</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>3,1,6,5,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>3,5,5,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>0,0,4,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.1 | 1.5 | 23.1 |
| Neemias Queta | 98% | 24.7<br><sub>26,29,15,22,22</sub> | 10.4<br><sub>16,9,4,13,4</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>6,12,3,9,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,3,1,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.6 | 1.1 | 1.3 | 19.8 |
| Sam Hauser | 98% | 24.0<br><sub>19,30,17,23,18</sub> | 9.1<br><sub>2,11,9,7,12</sub> |  | 3.4<br><sub>2,2,3,3,5</sub> |  | 1.1<br><sub>1,0,3,1,2</sub> |  | 1.7<br><sub>0,3,3,1,4</sub> |  | 0.5 | 0.2 | 0.4 | 13.6 |
| Baylor Scheierman | 98% | 22.0<br><sub>27,29,15,19,18</sub> | 7.0<br><sub>11,9,5,7,5</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>5,11,4,1,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,1,2,0,2</sub> |  | 1.1<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.1 | 0.8 | 12.2 |
| Mitchell Robinson | 98% | 19.3<br><sub>15,20,15,18,17</sub> | 6.1<br><sub>4,3,6,12,2</sub> |  | 7.3<br><sub>4,10,7,7,6</sub> |  | 0.7<br><sub>0,1,0,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.9 | 0.9 | 14.1 |
| Jordan Walsh | 98% | 17.3<br><sub>12,12,22,11,19</sub> | 5.0<br><sub>5,3,6,0,8</sub> |  | 3.3<br><sub>3,4,3,3,2</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.6<br><sub>1,1,1,0,1</sub> |  | 0.6 | 0.3 | 0.6 | 9.1 |
| Hugo Gonzalez | 97% | 15.8<br><sub>16,14,15,10,19</sub> | 4.7<br><sub>6,4,8,0,10</sub> |  | 2.9<br><sub>3,2,1,2,2</sub> |  | 0.7<br><sub>0,0,0,1,2</sub> |  | 0.5<br><sub>0,0,1,0,2</sub> |  | 0.6 | 0.3 | 0.7 | 8.2 |
| Luka Garza | 98% | 14.3<br><sub>18,18,19,9,9</sub> | 6.8<br><sub>14,11,6,4,2</sub> |  | 3.4<br><sub>3,5,7,5,0</sub> |  | 1.0<br><sub>0,2,4,0,2</sub> |  | 0.7<br><sub>4,3,2,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 11.2 |
| Mike Conley | 52% | 9.4<br><sub>4,-,11,10,-</sub> | 2.8<br><sub>3,-,0,3,-</sub> |  | 0.9<br><sub>0,-,0,3,-</sub> |  | 1.0<br><sub>0,-,1,1,-</sub> |  | 0.3<br><sub>1,-,0,1,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.8 |
| Ron Harper Jr. | 67% | 9.2<br><sub>7,-,10,4,4</sub> | 3.5<br><sub>0,-,3,2,0</sub> |  | 1.3<br><sub>1,-,0,0,1</sub> |  | 0.6<br><sub>1,-,2,0,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.4 |
| Dillon Mitchell | 48% | 7.9<br><sub>2,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.1 |
| Chris Cenac Jr. | 47% | 7.3<br><sub>2,-,-,-,-</sub> | 2.9<br><sub>2,-,-,-,-</sub> |  | 1.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.8 | 5.0 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 35.7<br><sub>32,37,33,37,36</sub> | 23.6<br><sub>22,26,22,27,19</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>10,6,5,7,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,3,3,5,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>4,2,3,0,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.7 | 0.4 | 2.8 | 34.3 |
| Immanuel Quickley | 72% | 31.9<br><sub>33,38,32,-,-</sub> | 16.6<br><sub>12,27,13,-,-</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>6,4,1,-,-</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>7,2,7,-,-</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>3,1,2,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.1 | 1.6 | 26.9 |
| Ja'Kobe Walter | 98% | 31.4<br><sub>33,35,27,29,34</sub> | 11.8<br><sub>11,10,8,7,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>4,6,1,6,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>2,5,2,2,0</sub> |  | 2.0<br><sub>3,0,1,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 1.0 | 18.0 |
| Jamal Shead | 98% | 30.3<br><sub>25,20,20,34,36</sub> | 10.2<br><sub>9,6,3,10,20</sub> |  | 2.3<br><sub>2,1,3,3,2</sub> |  | 7.7<br><sub>6,6,6,16,11</sub> |  | 1.4<br><sub>2,0,1,1,4</sub> |  | 1.1 | 0.2 | 2.1 | 20.2 |
| Collin Murray-Boyles | 98% | 28.6<br><sub>20,28,23,34,-</sub> | 12.8<br><sub>4,18,13,19,-</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,7,3,7,-</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,0,2,2,-</sub> |  | 0.5<br><sub>0,1,1,0,-</sub> |  | 1.1 | 0.9 | 1.8 | 21.6 |
| Jakob Poeltl | 88% | 26.5<br><sub>-,-,19,31,31</sub> | 10.6<br><sub>-,-,8,19,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 7.4<br><sub>-,-,5,11,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>-,-,1,1,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.8 | 0.8 | 1.6 | 20.0 |
| Jamison Battle | 98% | 25.6<br><sub>17,21,19,21,29</sub> | 11.4<br><sub>20,12,9,6,18</sub> |  | 3.3<br><sub>5,0,1,2,1</sub> |  | 1.2<br><sub>0,0,0,0,2</sub> |  | 2.1<br><sub>4,4,2,1,5</sub> |  | 0.4 | 0.2 | 0.8 | 15.8 |
| Alijah Martin | 91% | 17.7<br><sub>16,6,9,31,21</sub> | 6.7<br><sub>5,2,6,27,2</sub> |  | 2.5<br><sub>2,2,1,4,3</sub> |  | 1.7<br><sub>4,0,0,1,3</sub> |  | 0.7<br><sub>1,0,0,6,0</sub> |  | 0.7 | 0.3 | 1.1 | 10.9 |
| Allen Graves | 98% | 17.2<br><sub>10,7,14,16,13</sub> | 5.5<br><sub>3,0,5,3,3</sub> |  | 2.8<br><sub>0,0,1,2,2</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 0.4 | 0.4 | 0.4 | 9.3 |
| Kyle Anderson | 67% | 15.4<br><sub>4,8,4,-,16</sub> | 4.3<br><sub>2,2,2,-,6</sub> |  | 2.8<br><sub>3,0,0,-,2</sub> |  | 2.4<br><sub>3,0,1,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.4 | 0.7 | 9.5 |
| Jaden Bradley | 80% | 9.4<br><sub>4,-,4,8,9</sub> | 3.2<br><sub>3,-,2,3,0</sub> |  | 1.4<br><sub>1,-,1,0,1</sub> |  | 1.6<br><sub>2,-,0,1,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 6.2 |

</details>


### SAS @ CHI
Out: Tobe Awaka (CHI), Jaylin Sellers (CHI), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 123.1–109.4 | SAS 84% | 1.20 / 6.10 | CHI +13.5 | 232.5 | CHI +15.5 covers 55%; o237.5 39% |
| Expected (weighted by chance each plays) | 123.3–111.6 | SAS 80% | 1.25 / 5.00 | CHI +11.5 | 234.5 | CHI +15.5 covers 60%; o237.5 44% |
| if Norman Powell plays | 122.7–110.1 | SAS 81% | 1.23 / 5.38 | CHI +12.5 | 232.5 | CHI +15.5 covers 58%; o237.5 40% |
| if Devin Vassell plays | 123.6–110.2 | SAS 83% | 1.20 / 5.90 | CHI +13.5 | 233.5 | CHI +15.5 covers 56%; o237.5 42% |
| if Caleb Wilson plays | 122.9–110.2 | SAS 82% | 1.23 / 5.42 | CHI +12.5 | 232.5 | CHI +15.5 covers 58%; o237.5 40% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell (CHI) | Questionable | 55% | 30.8 | 19.5 | 3.4 | 2.3 | 2.5 | 1.1 | 0.2 | 2.1 | 25.2 | full tables below |
| Devin Vassell (SAS) | Questionable | 55% | 30.4 | 13.0 | 4.3 | 2.9 | 2.0 | 1.4 | 0.4 | 0.9 | 20.1 | full tables below |
| Zach Collins (CHI) | Questionable | 55% | 13.7 | 5.6 | 3.9 | 1.2 | 0.4 | 0.4 | 0.4 | 0.7 | 10.8 | small |
| Caleb Wilson (CHI) | Questionable | 55% | 34.1 | 19.8 | 6.5 | 2.6 | 2.3 | 1.1 | 0.8 | 2.7 | 28.9 | full tables below |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 32.5<br><sub>27,36,28,28,26</sub> | 18.5<br><sub>17,21,19,13,17</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>7,5,2,7,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 4.5<br><sub>8,0,3,3,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,1,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.4 | 0.3 | 1.9 | 28.8 |
| Victor Wembanyama | 98% | 31.9<br><sub>24,34,26,24,25</sub> | 31.0<br><sub>12,52,30,29,40</sub> | 29.5 · –<br><sub>o 51% · u 49%</sub> | 13.0<br><sub>11,24,14,7,11</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,2,2,3,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 3.7 | 2.6 | 47.3 |
| Stephon Castle | 98% | 31.6<br><sub>26,35,28,24,30</sub> | 18.4<br><sub>16,17,19,14,4</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>5,10,3,7,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 6.6<br><sub>4,3,7,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 2.9 | 30.7 |
| De'Aaron Fox | 98% | 31.5<br><sub>22,33,26,22,29</sub> | 16.3<br><sub>12,10,9,8,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>2,3,2,3,9</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>3,4,4,6,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>1,0,0,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 2.1 | 26.7 |
| Julian Champagnie | 98% | 27.3<br><sub>22,21,22,21,27</sub> | 10.3<br><sub>8,0,8,14,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>6,4,7,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,3,2,0,2</sub> |  | 1.9<br><sub>2,0,2,4,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 0.7 | 16.9 |
| Keldon Johnson | 98% | 26.2<br><sub>27,19,27,27,26</sub> | 11.2<br><sub>15,4,3,10,4</sub> |  | 5.9<br><sub>7,5,6,7,5</sub> |  | 1.8<br><sub>1,2,6,4,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 18.9 |
| Harrison Barnes | 86% | 18.8<br><sub>21,13,19,19,21</sub> | 6.8<br><sub>13,4,13,5,11</sub> |  | 2.2<br><sub>0,2,1,3,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>3,1,2,1,2</sub> |  | 0.5 | 0.2 | 0.5 | 9.9 |
| Luke Kornet | 98% | 17.1<br><sub>17,14,18,15,13</sub> | 4.4<br><sub>8,2,2,6,2</sub> |  | 5.3<br><sub>5,1,6,4,4</sub> |  | 1.1<br><sub>2,2,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.5 | 10.8 |
| Carter Bryant | 88% | 14.1<br><sub>14,-,3,17,14</sub> | 4.7<br><sub>3,-,0,6,8</sub> |  | 2.3<br><sub>0,-,0,4,1</sub> |  | 0.9<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>1,-,0,2,2</sub> |  | 0.3 | 0.4 | 0.6 | 7.9 |
| Jordan McLaughlin | 67% | 13.3<br><sub>8,-,8,12,11</sub> | 3.9<br><sub>0,-,2,3,4</sub> |  | 1.8<br><sub>1,-,2,0,4</sub> |  | 2.0<br><sub>3,-,1,0,2</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 1.0 | 0.1 | 0.6 | 7.7 |
| Tarris Reed Jr. | 67% | 10.0<br><sub>7,-,3,9,9</sub> | 3.7<br><sub>4,-,0,2,4</sub> |  | 4.1<br><sub>7,-,1,3,3</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.7 | 8.2 |
| David Jones Garcia | 64% | 8.2<br><sub>-,-,3,-,8</sub> | 3.3<br><sub>-,-,0,-,2</sub> |  | 1.5<br><sub>-,-,0,-,0</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.1 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 32.9<br><sub>31,25,32,27,34</sub> | 16.3<br><sub>10,13,13,10,19</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>8,4,4,1,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 9.7<br><sub>11,5,10,6,15</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.5 | 3.3 | 33.6 |
| Matas Buzelis | 98% | 30.8<br><sub>33,20,23,26,31</sub> | 17.5<br><sub>17,14,4,12,19</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>5,5,3,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>3,1,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.2<br><sub>3,2,0,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 1.1 | 2.4 | 25.9 |
| Jalen Smith | 98% | 27.7<br><sub>30,27,28,7,30</sub> | 13.3<br><sub>17,5,13,3,17</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 8.5<br><sub>11,12,7,2,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>5,1,4,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 1.0 | 1.1 | 23.7 |
| Patrick Williams | 58% | 27.4<br><sub>-,-,-,20,25</sub> | 9.8<br><sub>-,-,-,4,7</sub> |  | 3.8<br><sub>-,-,-,0,3</sub> |  | 2.2<br><sub>-,-,-,2,3</sub> |  | 1.5<br><sub>-,-,-,0,1</sub> |  | 0.8 | 0.5 | 1.2 | 15.9 |
| Isaac Okoro | 98% | 25.4<br><sub>18,18,21,15,25</sub> | 8.9<br><sub>7,6,4,6,12</sub> |  | 2.7<br><sub>0,3,1,1,2</sub> |  | 1.7<br><sub>1,2,0,0,1</sub> |  | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.4 | 0.8 | 13.3 |
| Tre Jones | 98% | 22.9<br><sub>18,20,19,18,14</sub> | 13.1<br><sub>11,12,8,14,6</sub> |  | 3.3<br><sub>4,4,3,3,1</sub> |  | 4.5<br><sub>3,4,3,4,1</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 1.0 | 0.2 | 1.3 | 20.9 |
| Nic Claxton | 96% | 22.0<br><sub>-,-,-,-,18</sub> | 9.5<br><sub>-,-,-,-,4</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>-,-,-,-,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>-,-,-,-,4</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.9 | 1.2 | 18.1 |
| Leonard Miller | 72% | 20.1<br><sub>17,11,9,19,-</sub> | 9.1<br><sub>10,2,2,4,-</sub> |  | 4.9<br><sub>0,2,3,6,-</sub> |  | 1.1<br><sub>1,1,0,3,-</sub> |  | 0.9<br><sub>1,0,0,0,-</sub> |  | 0.5 | 0.5 | 0.8 | 15.2 |
| Noa Essengue | 91% | 18.1<br><sub>10,16,14,14,15</sub> | 7.2<br><sub>3,10,8,6,10</sub> |  | 4.1<br><sub>0,4,6,3,7</sub> |  | 0.9<br><sub>1,0,0,0,1</sub> |  | 0.7<br><sub>1,1,1,0,0</sub> |  | 0.5 | 0.3 | 0.9 | 12.2 |
| Jordan Hawkins | 80% | 16.7<br><sub>-,6,2,7,17</sub> | 6.9<br><sub>-,0,2,2,9</sub> |  | 2.3<br><sub>-,0,0,1,0</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 0.8<br><sub>-,0,0,0,1</sub> |  | 0.4 | 0.3 | 0.8 | 10.2 |
| Buddy Hield | 71% | 16.0<br><sub>9,17,12,8,-</sub> | 6.9<br><sub>2,5,6,7,-</sub> |  | 2.3<br><sub>3,3,1,1,-</sub> |  | 1.5<br><sub>1,1,3,1,-</sub> |  | 1.0<br><sub>0,1,1,1,-</sub> |  | 0.6 | 0.2 | 0.8 | 10.7 |
| Dailyn Swain | 52% | 11.6<br><sub>-,-,-,7,-</sub> | 3.5<br><sub>-,-,-,3,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.2 | 1.1 | 6.8 |

</details>

<details><summary>if Norman Powell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 31.3<br><sub>31,25,32,27,34</sub> | 13.8<br><sub>10,13,13,10,19</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>8,4,4,1,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 9.2<br><sub>11,5,10,6,15</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.6 | 2.9 | 30.1 |
| Norman Powell (CHI) | 100% | 30.8<br><sub>37,31,29,22,-</sub> | 19.5<br><sub>30,16,18,12,-</sub> | 19.5 · – | 3.4<br><sub>2,2,3,1,-</sub> | 2.5 | 2.3<br><sub>2,3,0,1,-</sub> | 1.5 | 2.5<br><sub>4,1,1,0,-</sub> | 2.5 | 1.1 | 0.2 | 2.1 | 25.2 |
| Matas Buzelis (CHI) | 98% | 29.0<br><sub>33,20,23,26,31</sub> | 15.1<br><sub>17,14,4,12,19</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>5,5,3,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,1,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>3,2,0,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 1.1 | 2.0 | 22.8 |
| Jalen Smith (CHI) | 98% | 26.9<br><sub>30,27,28,7,30</sub> | 12.7<br><sub>17,5,13,3,17</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 8.2<br><sub>11,12,7,2,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>5,1,4,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.5 | 1.1 | 1.0 | 22.6 |
| Patrick Williams (CHI) | 58% | 24.3<br><sub>-,-,-,20,25</sub> | 8.4<br><sub>-,-,-,4,7</sub> |  | 3.2<br><sub>-,-,-,0,3</sub> |  | 1.8<br><sub>-,-,-,2,3</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.7 | 0.5 | 1.0 | 13.4 |
| Isaac Okoro (CHI) | 98% | 22.8<br><sub>18,18,21,15,25</sub> | 7.6<br><sub>7,6,4,6,12</sub> |  | 2.4<br><sub>0,3,1,1,2</sub> |  | 1.4<br><sub>1,2,0,0,1</sub> |  | 0.8<br><sub>1,1,0,0,0</sub> |  | 0.7 | 0.4 | 0.7 | 11.3 |
| Nic Claxton (CHI) | 96% | 19.1<br><sub>-,-,-,-,18</sub> | 7.7<br><sub>-,-,-,-,4</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>-,-,-,-,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>-,-,-,-,4</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.8 | 1.0 | 15.0 |
| Tre Jones (CHI) | 98% | 18.6<br><sub>18,20,19,18,14</sub> | 10.1<br><sub>11,12,8,14,6</sub> |  | 2.6<br><sub>4,4,3,3,1</sub> |  | 3.6<br><sub>3,4,3,4,1</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.2 | 1.0 | 16.3 |
| Leonard Miller (CHI) | 72% | 16.1<br><sub>17,11,9,19,-</sub> | 7.1<br><sub>10,2,2,4,-</sub> |  | 4.0<br><sub>0,2,3,6,-</sub> |  | 0.9<br><sub>1,1,0,3,-</sub> |  | 0.6<br><sub>1,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 12.0 |
| Noa Essengue (CHI) | 91% | 14.5<br><sub>10,16,14,14,15</sub> | 5.8<br><sub>3,10,8,6,10</sub> |  | 3.2<br><sub>0,4,6,3,7</sub> |  | 0.7<br><sub>1,0,0,0,1</sub> |  | 0.5<br><sub>1,1,1,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.7 |
| Buddy Hield (CHI) | 71% | 12.0<br><sub>9,17,12,8,-</sub> | 5.1<br><sub>2,5,6,7,-</sub> |  | 1.8<br><sub>3,3,1,1,-</sub> |  | 1.1<br><sub>1,1,3,1,-</sub> |  | 0.6<br><sub>0,1,1,1,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.9 |
| Jordan Hawkins (CHI) | 80% | 11.7<br><sub>-,6,2,7,17</sub> | 4.6<br><sub>-,0,2,2,9</sub> |  | 1.7<br><sub>-,0,0,1,0</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.5<br><sub>-,0,0,0,1</sub> |  | 0.3 | 0.2 | 0.6 | 7.0 |
| Dailyn Swain (CHI) | 52% | 8.1<br><sub>-,-,-,7,-</sub> | 2.5<br><sub>-,-,-,3,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.8 | 4.8 |
| Dylan Harper (SAS) | 98% | 32.5<br><sub>27,36,28,28,26</sub> | 18.4<br><sub>17,21,19,13,17</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>7,5,2,7,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 4.5<br><sub>8,0,3,3,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,1,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.4 | 0.4 | 1.9 | 28.7 |
| Victor Wembanyama (SAS) | 98% | 31.8<br><sub>24,34,26,24,25</sub> | 30.9<br><sub>12,52,30,29,40</sub> | 29.5 · –<br><sub>o 51% · u 49%</sub> | 12.9<br><sub>11,24,14,7,11</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,2,2,3,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.2<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 3.7 | 2.6 | 47.2 |
| Stephon Castle (SAS) | 98% | 31.7<br><sub>26,35,28,24,30</sub> | 18.4<br><sub>16,17,19,14,4</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>5,10,3,7,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>4,3,7,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 2.9 | 30.8 |
| De'Aaron Fox (SAS) | 98% | 31.5<br><sub>22,33,26,22,29</sub> | 16.3<br><sub>12,10,9,8,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>2,3,2,3,9</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>3,4,4,6,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>1,0,0,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 2.1 | 26.6 |
| Julian Champagnie (SAS) | 98% | 27.3<br><sub>22,21,22,21,27</sub> | 10.3<br><sub>8,0,8,14,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>6,4,7,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,3,2,0,2</sub> |  | 1.9<br><sub>2,0,2,4,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 0.7 | 16.9 |
| Keldon Johnson (SAS) | 98% | 26.2<br><sub>27,19,27,27,26</sub> | 11.2<br><sub>15,4,3,10,4</sub> |  | 5.9<br><sub>7,5,6,7,5</sub> |  | 1.8<br><sub>1,2,6,4,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.2 | 1.1 | 18.9 |
| Harrison Barnes (SAS) | 86% | 18.7<br><sub>21,13,19,19,21</sub> | 6.8<br><sub>13,4,13,5,11</sub> |  | 2.2<br><sub>0,2,1,3,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>3,1,2,1,2</sub> |  | 0.5 | 0.2 | 0.4 | 9.9 |
| Luke Kornet (SAS) | 98% | 17.1<br><sub>17,14,18,15,13</sub> | 4.4<br><sub>8,2,2,6,2</sub> |  | 5.4<br><sub>5,1,6,4,4</sub> |  | 1.1<br><sub>2,2,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.5 | 10.8 |
| Carter Bryant (SAS) | 88% | 14.0<br><sub>14,-,3,17,14</sub> | 4.8<br><sub>3,-,0,6,8</sub> |  | 2.3<br><sub>0,-,0,4,1</sub> |  | 0.9<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>1,-,0,2,2</sub> |  | 0.3 | 0.4 | 0.6 | 7.9 |
| Jordan McLaughlin (SAS) | 67% | 13.3<br><sub>8,-,8,12,11</sub> | 3.9<br><sub>0,-,2,3,4</sub> |  | 1.8<br><sub>1,-,2,0,4</sub> |  | 2.0<br><sub>3,-,1,0,2</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 1.0 | 0.1 | 0.6 | 7.7 |
| Tarris Reed Jr. (SAS) | 67% | 10.0<br><sub>7,-,3,9,9</sub> | 3.6<br><sub>4,-,0,2,4</sub> |  | 4.1<br><sub>7,-,1,3,3</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.8 | 8.1 |
| David Jones Garcia (SAS) | 64% | 8.2<br><sub>-,-,3,-,8</sub> | 3.3<br><sub>-,-,0,-,2</sub> |  | 1.6<br><sub>-,-,0,-,0</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.2 |

</details>

<details><summary>if Devin Vassell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 32.8<br><sub>31,25,32,27,34</sub> | 16.4<br><sub>10,13,13,10,19</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>8,4,4,1,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 9.7<br><sub>11,5,10,6,15</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.5 | 3.2 | 33.7 |
| Matas Buzelis (CHI) | 98% | 30.8<br><sub>33,20,23,26,31</sub> | 17.5<br><sub>17,14,4,12,19</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>5,5,3,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>3,1,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.2<br><sub>3,2,0,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 1.1 | 2.4 | 25.9 |
| Jalen Smith (CHI) | 98% | 27.8<br><sub>30,27,28,7,30</sub> | 13.3<br><sub>17,5,13,3,17</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 8.6<br><sub>11,12,7,2,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>5,1,4,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 1.0 | 1.2 | 23.8 |
| Patrick Williams (CHI) | 58% | 27.3<br><sub>-,-,-,20,25</sub> | 9.9<br><sub>-,-,-,4,7</sub> |  | 3.8<br><sub>-,-,-,0,3</sub> |  | 2.2<br><sub>-,-,-,2,3</sub> |  | 1.5<br><sub>-,-,-,0,1</sub> |  | 0.8 | 0.5 | 1.2 | 15.9 |
| Isaac Okoro (CHI) | 98% | 25.4<br><sub>18,18,21,15,25</sub> | 8.9<br><sub>7,6,4,6,12</sub> |  | 2.7<br><sub>0,3,1,1,2</sub> |  | 1.7<br><sub>1,2,0,0,1</sub> |  | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.4 | 0.8 | 13.3 |
| Tre Jones (CHI) | 98% | 22.9<br><sub>18,20,19,18,14</sub> | 13.2<br><sub>11,12,8,14,6</sub> |  | 3.4<br><sub>4,4,3,3,1</sub> |  | 4.5<br><sub>3,4,3,4,1</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 1.0 | 0.2 | 1.3 | 21.1 |
| Nic Claxton (CHI) | 96% | 21.9<br><sub>-,-,-,-,18</sub> | 9.6<br><sub>-,-,-,-,4</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>-,-,-,-,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>-,-,-,-,4</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.9 | 1.2 | 18.1 |
| Leonard Miller (CHI) | 72% | 20.0<br><sub>17,11,9,19,-</sub> | 9.2<br><sub>10,2,2,4,-</sub> |  | 4.9<br><sub>0,2,3,6,-</sub> |  | 1.1<br><sub>1,1,0,3,-</sub> |  | 0.9<br><sub>1,0,0,0,-</sub> |  | 0.5 | 0.5 | 0.9 | 15.2 |
| Noa Essengue (CHI) | 91% | 18.1<br><sub>10,16,14,14,15</sub> | 7.2<br><sub>3,10,8,6,10</sub> |  | 4.1<br><sub>0,4,6,3,7</sub> |  | 0.9<br><sub>1,0,0,0,1</sub> |  | 0.7<br><sub>1,1,1,0,0</sub> |  | 0.5 | 0.3 | 0.9 | 12.1 |
| Jordan Hawkins (CHI) | 80% | 16.7<br><sub>-,6,2,7,17</sub> | 6.9<br><sub>-,0,2,2,9</sub> |  | 2.3<br><sub>-,0,0,1,0</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 0.8<br><sub>-,0,0,0,1</sub> |  | 0.4 | 0.3 | 0.8 | 10.2 |
| Buddy Hield (CHI) | 71% | 16.1<br><sub>9,17,12,8,-</sub> | 7.0<br><sub>2,5,6,7,-</sub> |  | 2.3<br><sub>3,3,1,1,-</sub> |  | 1.5<br><sub>1,1,3,1,-</sub> |  | 1.0<br><sub>0,1,1,1,-</sub> |  | 0.6 | 0.2 | 0.8 | 10.8 |
| Dailyn Swain (CHI) | 52% | 11.6<br><sub>-,-,-,7,-</sub> | 3.4<br><sub>-,-,-,3,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.2 | 1.1 | 6.8 |
| Devin Vassell (SAS) | 100% | 30.4<br><sub>25,36,27,21,-</sub> | 13.0<br><sub>11,2,19,15,-</sub> | 10.5 · – | 4.3<br><sub>2,7,2,2,-</sub> | 3.5 | 2.9<br><sub>1,4,2,3,-</sub> | 2.5 | 2.0<br><sub>0,0,5,2,-</sub> | 1.5 | 1.4 | 0.4 | 0.9 | 20.1 |
| Dylan Harper (SAS) | 98% | 30.2<br><sub>27,36,28,28,26</sub> | 16.4<br><sub>17,21,19,13,17</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>7,5,2,7,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 4.3<br><sub>8,0,3,3,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>1,1,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.2 | 0.4 | 1.8 | 26.0 |
| Victor Wembanyama (SAS) | 98% | 30.1<br><sub>24,34,26,24,25</sub> | 28.9<br><sub>12,52,30,29,40</sub> | 29.5 · –<br><sub>o 51% · u 49%</sub> | 12.4<br><sub>11,24,14,7,11</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,2,2,3,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 3.8 | 2.4 | 44.4 |
| Stephon Castle (SAS) | 98% | 29.3<br><sub>26,35,28,24,30</sub> | 16.5<br><sub>16,17,19,14,4</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>5,10,3,7,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 6.3<br><sub>4,3,7,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 2.6 | 28.2 |
| De'Aaron Fox (SAS) | 98% | 29.1<br><sub>22,33,26,22,29</sub> | 14.7<br><sub>12,10,9,8,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>2,3,2,3,9</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>3,4,4,6,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,0,0,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.9 | 24.2 |
| Julian Champagnie (SAS) | 98% | 24.5<br><sub>22,21,22,21,27</sub> | 9.3<br><sub>8,0,8,14,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>6,4,7,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,3,2,0,2</sub> |  | 1.7<br><sub>2,0,2,4,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.4 | 0.6 | 15.3 |
| Keldon Johnson (SAS) | 98% | 23.3<br><sub>27,19,27,27,26</sub> | 10.1<br><sub>15,4,3,10,4</sub> |  | 5.2<br><sub>7,5,6,7,5</sub> |  | 1.7<br><sub>1,2,6,4,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.0 | 17.0 |
| Harrison Barnes (SAS) | 86% | 15.9<br><sub>21,13,19,19,21</sub> | 6.1<br><sub>13,4,13,5,11</sub> |  | 1.9<br><sub>0,2,1,3,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 0.8<br><sub>3,1,2,1,2</sub> |  | 0.5 | 0.1 | 0.4 | 8.8 |
| Luke Kornet (SAS) | 98% | 14.7<br><sub>17,14,18,15,13</sub> | 3.9<br><sub>8,2,2,6,2</sub> |  | 4.8<br><sub>5,1,6,4,4</sub> |  | 0.9<br><sub>2,2,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.4 | 9.6 |
| Carter Bryant (SAS) | 88% | 12.0<br><sub>14,-,3,17,14</sub> | 4.3<br><sub>3,-,0,6,8</sub> |  | 2.1<br><sub>0,-,0,4,1</sub> |  | 0.8<br><sub>0,-,0,1,1</sub> |  | 0.5<br><sub>1,-,0,2,2</sub> |  | 0.3 | 0.3 | 0.5 | 7.2 |
| Jordan McLaughlin (SAS) | 67% | 9.6<br><sub>8,-,8,12,11</sub> | 3.2<br><sub>0,-,2,3,4</sub> |  | 1.4<br><sub>1,-,2,0,4</sub> |  | 1.6<br><sub>3,-,1,0,2</sub> |  | 0.3<br><sub>0,-,0,1,0</sub> |  | 0.7 | 0.1 | 0.5 | 6.2 |
| Tarris Reed Jr. (SAS) | 67% | 8.2<br><sub>7,-,3,9,9</sub> | 3.4<br><sub>4,-,0,2,4</sub> |  | 3.5<br><sub>7,-,1,3,3</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 7.3 |
| David Jones Garcia (SAS) | 64% | 6.8<br><sub>-,-,3,-,8</sub> | 3.1<br><sub>-,-,0,-,2</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 1.2<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.1 | 0.4 | 5.6 |

</details>

<details><summary>if Caleb Wilson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson (CHI) | 100% | 34.1<br><sub>38,31,34,22,32</sub> | 19.8<br><sub>20,23,24,5,18</sub> | 18.5 · – | 6.5<br><sub>6,5,7,5,5</sub> | 5.5 | 2.6<br><sub>4,4,4,0,0</sub> | 2.5 | 2.3<br><sub>3,6,4,1,2</sub> | 2.5 | 1.1 | 0.8 | 2.7 | 28.9 |
| Josh Giddey (CHI) | 98% | 31.5<br><sub>31,25,32,27,34</sub> | 13.7<br><sub>10,13,13,10,19</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>8,4,4,1,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 9.2<br><sub>11,5,10,6,15</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.6 | 2.9 | 29.9 |
| Matas Buzelis (CHI) | 98% | 28.7<br><sub>33,20,23,26,31</sub> | 14.6<br><sub>17,14,4,12,19</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>5,5,3,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,1,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>3,2,0,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 1.1 | 2.0 | 22.1 |
| Jalen Smith (CHI) | 98% | 26.6<br><sub>30,27,28,7,30</sub> | 12.3<br><sub>17,5,13,3,17</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 8.0<br><sub>11,12,7,2,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>5,1,4,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.5 | 1.1 | 1.1 | 21.9 |
| Patrick Williams (CHI) | 58% | 23.9<br><sub>-,-,-,20,25</sub> | 8.0<br><sub>-,-,-,4,7</sub> |  | 3.1<br><sub>-,-,-,0,3</sub> |  | 1.8<br><sub>-,-,-,2,3</sub> |  | 1.1<br><sub>-,-,-,0,1</sub> |  | 0.7 | 0.4 | 1.0 | 12.9 |
| Isaac Okoro (CHI) | 98% | 22.1<br><sub>18,18,21,15,25</sub> | 7.2<br><sub>7,6,4,6,12</sub> |  | 2.2<br><sub>0,3,1,1,2</sub> |  | 1.3<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>1,1,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 10.7 |
| Tre Jones (CHI) | 98% | 19.2<br><sub>18,20,19,18,14</sub> | 10.4<br><sub>11,12,8,14,6</sub> |  | 2.7<br><sub>4,4,3,3,1</sub> |  | 3.6<br><sub>3,4,3,4,1</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.2 | 1.1 | 16.7 |
| Nic Claxton (CHI) | 96% | 19.1<br><sub>-,-,-,-,18</sub> | 7.4<br><sub>-,-,-,-,4</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>-,-,-,-,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>-,-,-,-,4</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.8 | 1.0 | 14.7 |
| Leonard Miller (CHI) | 72% | 15.4<br><sub>17,11,9,19,-</sub> | 6.7<br><sub>10,2,2,4,-</sub> |  | 3.7<br><sub>0,2,3,6,-</sub> |  | 0.8<br><sub>1,1,0,3,-</sub> |  | 0.6<br><sub>1,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 11.3 |
| Noa Essengue (CHI) | 91% | 14.3<br><sub>10,16,14,14,15</sub> | 5.7<br><sub>3,10,8,6,10</sub> |  | 3.2<br><sub>0,4,6,3,7</sub> |  | 0.7<br><sub>1,0,0,0,1</sub> |  | 0.5<br><sub>1,1,1,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.6 |
| Jordan Hawkins (CHI) | 80% | 13.3<br><sub>-,6,2,7,17</sub> | 5.4<br><sub>-,0,2,2,9</sub> |  | 1.8<br><sub>-,0,0,1,0</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.6<br><sub>-,0,0,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.0 |
| Buddy Hield (CHI) | 71% | 13.2<br><sub>9,17,12,8,-</sub> | 5.5<br><sub>2,5,6,7,-</sub> |  | 1.9<br><sub>3,3,1,1,-</sub> |  | 1.2<br><sub>1,1,3,1,-</sub> |  | 0.7<br><sub>0,1,1,1,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.6 |
| Dailyn Swain (CHI) | 52% | 8.2<br><sub>-,-,-,7,-</sub> | 2.6<br><sub>-,-,-,3,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 1.2<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.8 | 5.0 |
| Dylan Harper (SAS) | 98% | 32.6<br><sub>27,36,28,28,26</sub> | 18.5<br><sub>17,21,19,13,17</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>7,5,2,7,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 4.5<br><sub>8,0,3,3,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,1,1,1,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.4 | 0.4 | 1.9 | 28.8 |
| Victor Wembanyama (SAS) | 98% | 31.9<br><sub>24,34,26,24,25</sub> | 30.8<br><sub>12,52,30,29,40</sub> | 29.5 · –<br><sub>o 51% · u 49%</sub> | 13.0<br><sub>11,24,14,7,11</sub> | 11.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,2,2,3,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 3.7 | 2.6 | 47.1 |
| Stephon Castle (SAS) | 98% | 31.6<br><sub>26,35,28,24,30</sub> | 18.4<br><sub>16,17,19,14,4</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>5,10,3,7,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>4,3,7,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 2.9 | 30.8 |
| De'Aaron Fox (SAS) | 98% | 31.4<br><sub>22,33,26,22,29</sub> | 16.3<br><sub>12,10,9,8,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>2,3,2,3,9</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>3,4,4,6,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>1,0,0,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 2.1 | 26.5 |
| Julian Champagnie (SAS) | 98% | 27.3<br><sub>22,21,22,21,27</sub> | 10.3<br><sub>8,0,8,14,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>6,4,7,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,3,2,0,2</sub> |  | 1.9<br><sub>2,0,2,4,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 0.7 | 16.9 |
| Keldon Johnson (SAS) | 98% | 26.2<br><sub>27,19,27,27,26</sub> | 11.1<br><sub>15,4,3,10,4</sub> |  | 5.8<br><sub>7,5,6,7,5</sub> |  | 1.8<br><sub>1,2,6,4,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 18.8 |
| Harrison Barnes (SAS) | 86% | 18.7<br><sub>21,13,19,19,21</sub> | 6.8<br><sub>13,4,13,5,11</sub> |  | 2.2<br><sub>0,2,1,3,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>3,1,2,1,2</sub> |  | 0.5 | 0.2 | 0.5 | 9.9 |
| Luke Kornet (SAS) | 98% | 17.0<br><sub>17,14,18,15,13</sub> | 4.4<br><sub>8,2,2,6,2</sub> |  | 5.3<br><sub>5,1,6,4,4</sub> |  | 1.1<br><sub>2,2,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.5 | 10.7 |
| Carter Bryant (SAS) | 88% | 14.1<br><sub>14,-,3,17,14</sub> | 4.8<br><sub>3,-,0,6,8</sub> |  | 2.3<br><sub>0,-,0,4,1</sub> |  | 0.9<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>1,-,0,2,2</sub> |  | 0.3 | 0.4 | 0.5 | 8.0 |
| Jordan McLaughlin (SAS) | 67% | 13.3<br><sub>8,-,8,12,11</sub> | 3.9<br><sub>0,-,2,3,4</sub> |  | 1.8<br><sub>1,-,2,0,4</sub> |  | 2.0<br><sub>3,-,1,0,2</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 1.0 | 0.1 | 0.6 | 7.8 |
| Tarris Reed Jr. (SAS) | 67% | 9.9<br><sub>7,-,3,9,9</sub> | 3.6<br><sub>4,-,0,2,4</sub> |  | 4.0<br><sub>7,-,1,3,3</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.8 | 8.1 |
| David Jones Garcia (SAS) | 64% | 8.3<br><sub>-,-,3,-,8</sub> | 3.3<br><sub>-,-,0,-,2</sub> |  | 1.6<br><sub>-,-,0,-,0</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.2 |

</details>


### DEN @ MEM
Out: Scotty Pippen Jr. (MEM), Quinten Post (MEM), Julian Strawther (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 120.8–118.4 | DEN 57% | 1.74 / 2.34 | MEM +2.5 | 238.5 | MEM +4.5 covers 55%; o230.5 68% |
| Expected (weighted by chance each plays) | 120.8–118.4 | DEN 57% | 1.75 / 2.33 | MEM +2.5 | 239.5 | MEM +4.5 covers 55%; o230.5 68% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaiah Stewart (MEM) | Questionable | 55% | 11.7 | 5.5 | 2.6 | 0.5 | 0.3 | 0.2 | 0.6 | 0.5 | 8.7 | small |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 36.4<br><sub>37,39,28,34,39</sub> | 25.6<br><sub>39,35,14,16,38</sub> | 23.5 · –<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>8,5,5,6,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>5,6,7,8,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>7,4,2,2,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.6 | 2.5 | 37.0 |
| Nikola Jokic | 98% | 35.8<br><sub>37,36,30,36,39</sub> | 26.5<br><sub>18,26,32,19,25</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 13.2<br><sub>7,9,10,13,16</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 10.6<br><sub>10,8,11,8,9</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>0,2,0,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 1.1 | 3.7 | 50.3 |
| Christian Braun | 98% | 31.7<br><sub>37,37,28,29,32</sub> | 12.1<br><sub>31,14,11,6,4</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>3,3,3,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.4<br><sub>1,3,3,1,3</sub> |  | 1.2<br><sub>7,1,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.5 | 1.0 | 19.0 |
| Cameron Johnson | 98% | 28.3<br><sub>34,34,30,29,31</sub> | 12.2<br><sub>12,7,12,18,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>9,4,2,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>3,2,2,1,1</sub> |  | 1.6<br><sub>2,1,4,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.4 | 1.0 | 18.4 |
| Aaron Gordon | 98% | 28.1<br><sub>29,30,25,27,30</sub> | 13.1<br><sub>15,5,17,12,3</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>4,6,1,5,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.7<br><sub>5,2,0,0,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>2,1,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.4 | 1.3 | 21.4 |
| DeMar DeRozan | 86% | 22.0<br><sub>24,20,-,22,19</sub> | 11.4<br><sub>3,9,-,11,7</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,0,-,1,4</sub> |  | 3.3<br><sub>5,1,-,5,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.8 | 0.3 | 1.2 | 17.0 |
| Trevon Brazile | 98% | 15.3<br><sub>19,18,23,14,14</sub> | 5.0<br><sub>6,6,6,3,5</sub> |  | 3.8<br><sub>3,5,7,4,2</sub> |  | 0.8<br><sub>1,1,1,2,0</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.3 | 0.7 | 9.5 |
| Spencer Jones | 64% | 14.0<br><sub>-,-,-,21,14</sub> | 4.3<br><sub>-,-,-,13,0</sub> | 4.5 · –<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>-,-,-,6,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,3,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.5 | 0.6 | 0.7 | 7.6 |
| Marvin Bagley III | 98% | 12.6<br><sub>11,12,14,12,12</sub> | 6.4<br><sub>0,6,10,10,6</sub> |  | 4.0<br><sub>5,4,2,3,3</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 11.1 |
| Tyus Jones | 96% | 10.0<br><sub>11,8,18,13,6</sub> | 3.0<br><sub>3,2,6,3,2</sub> |  | 1.0<br><sub>0,0,1,4,0</sub> |  | 1.8<br><sub>0,1,8,4,0</sub> |  | 0.3<br><sub>1,0,0,1,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.8 |
| Bryce Hopkins | 76% | 9.3<br><sub>-,-,28,3,3</sub> | 3.2<br><sub>-,-,18,3,2</sub> |  | 1.6<br><sub>-,-,4,1,0</sub> |  | 0.5<br><sub>-,-,1,0,0</sub> |  | 0.1<br><sub>-,-,1,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.3 |
| Cam Whitmore | 58% | 7.2<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.6 |
| Zeke Nnaji | 38% | 6.5<br><sub>-,-,4,-,-</sub> | 2.3<br><sub>-,-,2,-,-</sub> |  | 1.5<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.2 |
| Alpha Diallo | 71% | 6.2<br><sub>-,6,4,-,1</sub> | 2.6<br><sub>-,0,0,-,0</sub> |  | 1.0<br><sub>-,1,0,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Ryan Nembhard | 52% | 6.2<br><sub>-,-,4,-,-</sub> | 3.0<br><sub>-,-,0,-,-</sub> |  | 1.0<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| DaRon Holmes II | 52% | 5.8<br><sub>-,-,4,-,1</sub> | 2.6<br><sub>-,-,0,-,0</sub> |  | 1.2<br><sub>-,-,1,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 32.7<br><sub>26,38,33,31,33</sub> | 16.6<br><sub>27,18,10,8,22</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 9.5<br><sub>9,9,6,12,7</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 5.3<br><sub>3,5,4,4,8</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,2,2,0,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.5 | 2.6 | 31.4 |
| Ty Jerome | 98% | 30.2<br><sub>-,37,29,28,32</sub> | 21.8<br><sub>-,40,23,21,27</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>-,5,4,2,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 5.3<br><sub>-,5,3,5,2</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>-,5,2,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.3 | 2.0 | 30.7 |
| Cedric Coward | 98% | 28.2<br><sub>23,31,33,23,28</sub> | 13.7<br><sub>10,10,23,10,3</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>7,9,9,9,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,3,4,0,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>2,2,4,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.4 | 1.4 | 23.3 |
| Jaylen Wells | 98% | 26.5<br><sub>22,34,21,25,26</sub> | 11.1<br><sub>4,16,0,7,14</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,3,1,0,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>0,3,3,0,1</sub> |  | 1.7<br><sub>0,3,0,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.1 | 0.7 | 15.5 |
| Jerami Grant | 98% | 23.0<br><sub>23,24,24,22,22</sub> | 11.4<br><sub>14,11,11,10,17</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,4,1,0,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>1,2,2,2,2</sub> |  | 1.5<br><sub>1,2,2,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.6 | 1.1 | 15.4 |
| Zach Edey | 98% | 22.4<br><sub>18,19,25,20,23</sub> | 9.4<br><sub>4,6,11,14,8</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 8.8<br><sub>6,9,13,6,9</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,1,1,1,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.3 | 19.3 |
| Javon Small | 93% | 21.8<br><sub>20,-,-,21,24</sub> | 9.6<br><sub>7,-,-,10,9</sub> |  | 3.1<br><sub>1,-,-,4,2</sub> |  | 3.4<br><sub>5,-,-,2,5</sub> |  | 1.2<br><sub>2,-,-,1,1</sub> |  | 0.8 | 0.2 | 1.1 | 16.1 |
| Cam Spencer | 98% | 18.8<br><sub>25,19,24,19,17</sub> | 7.8<br><sub>10,13,7,7,7</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>5,1,6,1,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>13,7,9,0,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.9 | 14.5 |
| GG Jackson | 80% | 15.3<br><sub>21,16,7,-,17</sub> | 8.4<br><sub>21,6,1,-,2</sub> |  | 3.1<br><sub>3,0,2,-,1</sub> |  | 0.9<br><sub>2,1,0,-,0</sub> |  | 0.9<br><sub>5,0,0,-,0</sub> |  | 0.4 | 0.4 | 1.1 | 12.4 |
| Taylor Hendricks | 63% | 11.1<br><sub>4,-,-,4,16</sub> | 4.8<br><sub>6,-,-,4,9</sub> |  | 2.2<br><sub>1,-,-,2,3</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>2,-,-,1,1</sub> |  | 0.5 | 0.3 | 0.4 | 7.5 |
| Kris Murray | 88% | 8.5<br><sub>21,19,15,13,1</sub> | 2.4<br><sub>2,0,5,2,0</sub> |  | 1.4<br><sub>1,4,1,2,0</sub> |  | 0.5<br><sub>1,1,1,1,0</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Olivier-Maxence Prosper | 67% | 7.9<br><sub>4,-,7,11,1</sub> | 4.4<br><sub>2,-,4,2,0</sub> |  | 1.7<br><sub>1,-,3,3,0</sub> |  | 0.4<br><sub>1,-,1,1,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 6.5 |
| Jahmai Mashack | 52% | 7.6<br><sub>4,-,-,4,-</sub> | 2.5<br><sub>2,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,2,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |
| Karim Lopez | 52% | 5.7<br><sub>4,-,-,4,-</sub> | 2.2<br><sub>2,-,-,2,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.6 |

</details>


### LAL @ MIL
Out: Myles Turner (MIL), Quentin Grimes (LAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.3–108.0 | LAL 77% | 1.30 / 4.36 | MIL +10.5 | 226.5 | MIL +14.5 covers 62%; o229.5 43% |
| Expected (weighted by chance each plays) | 118.7–109.2 | LAL 75% | 1.33 / 4.00 | MIL +9.5 | 227.5 | MIL +14.5 covers 64%; o229.5 46% |
| if Tyler Herro plays | 118.9–110.0 | LAL 74% | 1.36 / 3.82 | MIL +8.5 | 228.5 | MIL +14.5 covers 66%; o229.5 48% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | Questionable | 55% | 32.6 | 20.4 | 4.6 | 5.2 | 2.6 | 0.8 | 0.2 | 2.6 | 30.1 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.2<br><sub>36,35,38,-,39</sub> | 35.3<br><sub>42,40,53,-,32</sub> | 35.5 · –<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>7,9,5,-,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>13,7,5,-,10</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>6,6,5,-,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.6 | 4.0 | 51.5 |
| Austin Reaves | 98% | 36.0<br><sub>34,37,38,37,-</sub> | 22.2<br><sub>27,21,25,43,-</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,3,3,5,-</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.2<br><sub>5,4,2,4,-</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>4,1,1,4,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 3.0 | 32.0 |
| Walker Kessler | 98% | 30.2<br><sub>32,29,37,29,30</sub> | 11.8<br><sub>15,15,16,12,21</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 11.9<br><sub>15,8,12,16,10</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>2,0,2,4,4</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.0 | 1.5 | 25.8 |
| Jake LaRavia | 98% | 25.6<br><sub>26,21,25,29,32</sub> | 6.5<br><sub>7,9,7,5,4</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>4,2,8,1,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,2,3,2,3</sub> |  | 0.7<br><sub>1,2,2,0,0</sub> |  | 1.4 | 0.6 | 1.1 | 12.4 |
| Sandro Mamukelashvili | 98% | 23.8<br><sub>28,19,20,18,32</sub> | 9.4<br><sub>13,2,7,7,23</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>3,6,3,3,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>4,1,1,0,3</sub> |  | 1.3<br><sub>2,0,1,1,5</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.5 | 0.8 | 16.5 |
| Ziaire Williams | 98% | 23.6<br><sub>15,23,20,21,28</sub> | 8.9<br><sub>9,10,8,17,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>2,1,1,0,2</sub> |  | 1.4<br><sub>3,1,2,4,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.3 | 0.9 | 13.2 |
| Matisse Thybulle | 98% | 23.4<br><sub>19,23,24,28,23</sub> | 5.8<br><sub>6,3,2,4,6</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,1,2,2,0</sub> |  | 1.2<br><sub>2,2,0,0,1</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 2.3 | 0.7 | 0.7 | 9.2 |
| Collin Sexton | 98% | 20.7<br><sub>16,16,11,24,27</sub> | 11.3<br><sub>6,10,0,17,18</sub> |  | 2.2<br><sub>1,3,0,2,2</sub> |  | 2.6<br><sub>5,1,1,2,6</sub> |  | 1.2<br><sub>0,1,0,0,3</sub> |  | 1.0 | 0.2 | 1.4 | 16.2 |
| Jarred Vanderbilt | 71% | 12.7<br><sub>6,7,-,14,13</sub> | 3.0<br><sub>2,0,-,2,4</sub> |  | 3.5<br><sub>1,1,-,10,2</sub> |  | 1.1<br><sub>0,0,-,3,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 7.6 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke | 23% | 8.4<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Adou Thiero | 91% | 8.2<br><sub>-,-,7,8,7</sub> | 2.7<br><sub>-,-,4,2,2</sub> |  | 2.2<br><sub>-,-,4,2,2</sub> |  | 0.6<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.6 |
| Jaden Hardy | 52% | 6.7<br><sub>1,1,-,-,-</sub> | 3.7<br><sub>2,0,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Kevon Looney | 26% | 6.6<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.4 |
| Cameron Carr | 71% | 6.0<br><sub>1,1,-,-,7</sub> | 2.0<br><sub>0,0,-,-,2</sub> |  | 1.0<br><sub>0,0,-,-,3</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.5 |
| Chris Manon | 58% | 5.7<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.0 |
| Carson Cooper | 48% | 5.6<br><sub>3,-,-,-,-</sub> | 2.4<br><sub>1,-,-,-,-</sub> |  | 2.8<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 1.0 | 6.1 |
| Bronny James | 52% | 5.5<br><sub>1,1,-,-,-</sub> | 2.1<br><sub>2,0,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.6 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyle Kuzma | 98% | 30.4<br><sub>22,27,32,31,26</sub> | 14.0<br><sub>2,6,13,27,5</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>2,5,4,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>3,4,3,0,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>0,1,1,6,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.3 | 2.2 | 22.7 |
| Brayden Burries | 98% | 29.6<br><sub>26,22,38,29,26</sub> | 13.9<br><sub>9,9,21,13,3</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>9,5,11,8,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>1,3,6,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>1,0,1,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 1.8 | 23.4 |
| Jaime Jaquez Jr. | 98% | 29.4<br><sub>28,31,28,23,25</sub> | 16.3<br><sub>19,18,14,4,16</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>8,2,3,2,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>2,2,3,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.5<br><sub>2,4,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 2.5 | 26.0 |
| Ryan Rollins | 98% | 27.5<br><sub>17,24,14,20,24</sub> | 15.2<br><sub>10,13,10,7,14</sub> |  | 4.1<br><sub>3,9,1,5,5</sub> |  | 5.4<br><sub>2,5,1,6,2</sub> |  | 2.2<br><sub>1,2,1,2,4</sub> |  | 1.1 | 0.3 | 2.7 | 24.7 |
| AJ Green | 98% | 23.9<br><sub>24,20,24,18,8</sub> | 9.3<br><sub>13,5,12,5,0</sub> |  | 2.2<br><sub>3,2,1,1,0</sub> |  | 1.7<br><sub>3,3,0,1,0</sub> |  | 1.9<br><sub>4,1,4,1,0</sub> |  | 0.4 | 0.1 | 0.9 | 13.3 |
| Cormac Ryan | 16% | 20.9 | 10.0 |  | 2.1 |  | 1.7 |  | 1.5 |  | 0.8 | 0.3 | 1.5 | 13.9 |
| Kasparas Jakucionis | 96% | 20.8<br><sub>22,12,10,7,23</sub> | 7.8<br><sub>7,3,3,1,11</sub> |  | 2.4<br><sub>5,1,0,2,0</sub> |  | 3.8<br><sub>7,1,2,0,4</sub> |  | 0.8<br><sub>0,1,0,0,2</sub> |  | 0.7 | 0.2 | 1.6 | 14.0 |
| Nate Ament | 91% | 19.6<br><sub>8,18,15,23,22</sub> | 8.2<br><sub>4,9,7,12,10</sub> |  | 2.9<br><sub>1,2,1,5,2</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.8<br><sub>0,2,0,2,2</sub> |  | 0.6 | 0.3 | 1.0 | 12.0 |
| Kel'el Ware | 96% | 19.1<br><sub>17,16,13,9,17</sub> | 8.8<br><sub>2,2,4,0,8</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>9,5,3,0,4</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>0,1,0,1,1</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 1.5 | 15.7 |
| Caris LeVert | 16% | 18.2<br><sub>-,-,-,-,-</sub> | 7.2<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.8 | 0.5 | 1.2 | 11.9 |
| Ousmane Dieng | 71% | 17.8<br><sub>-,2,-,15,24</sub> | 6.8<br><sub>-,0,-,10,8</sub> |  | 2.7<br><sub>-,0,-,1,3</sub> |  | 2.0<br><sub>-,0,-,0,0</sub> |  | 0.8<br><sub>-,0,-,2,2</sub> |  | 0.5 | 0.2 | 1.2 | 11.6 |
| Pete Nance | 16% | 15.5 | 4.9 |  | 2.6 |  | 1.2 |  | 0.6 |  | 0.4 | 0.3 | 0.6 | 8.7 |
| Kam Jones | 16% | 14.6 | 3.8 |  | 1.5 |  | 3.3 |  | 0.4 |  | 0.5 | 0.1 | 1.1 | 8.6 |
| Jericho Sims | 80% | 14.6<br><sub>15,1,7,15,8</sub> | 3.0<br><sub>0,0,0,2,2</sub> |  | 3.8<br><sub>2,0,1,2,0</sub> |  | 1.2<br><sub>1,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.2 | 0.8 | 8.1 |
| Gary Trent Jr. | 52% | 14.0<br><sub>-,-,-,-,6</sub> | 6.2<br><sub>-,-,-,-,5</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 8.0 |
| Bogoljub Markovic | 48% | 9.0<br><sub>-,-,-,-,4</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 2.1<br><sub>-,-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.5 | 6.0 |

</details>

<details><summary>if Tyler Herro plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 36.1<br><sub>36,35,38,-,39</sub> | 35.3<br><sub>42,40,53,-,32</sub> | 35.5 · –<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>7,9,5,-,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>13,7,5,-,10</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>6,6,5,-,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.6 | 4.0 | 51.5 |
| Austin Reaves (LAL) | 98% | 35.9<br><sub>34,37,38,37,-</sub> | 22.1<br><sub>27,21,25,43,-</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,3,3,5,-</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.3<br><sub>5,4,2,4,-</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>4,1,1,4,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 3.0 | 31.8 |
| Walker Kessler (LAL) | 98% | 30.3<br><sub>32,29,37,29,30</sub> | 11.8<br><sub>15,15,16,12,21</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 12.0<br><sub>15,8,12,16,10</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>2,0,2,4,4</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.9 | 1.6 | 25.9 |
| Jake LaRavia (LAL) | 98% | 25.5<br><sub>26,21,25,29,32</sub> | 6.5<br><sub>7,9,7,5,4</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>4,2,8,1,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,2,3,2,3</sub> |  | 0.7<br><sub>1,2,2,0,0</sub> |  | 1.4 | 0.6 | 1.1 | 12.4 |
| Sandro Mamukelashvili (LAL) | 98% | 23.8<br><sub>28,19,20,18,32</sub> | 9.3<br><sub>13,2,7,7,23</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>3,6,3,3,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>4,1,1,0,3</sub> |  | 1.3<br><sub>2,0,1,1,5</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.6 | 0.8 | 16.4 |
| Ziaire Williams (LAL) | 98% | 23.7<br><sub>15,23,20,21,28</sub> | 8.9<br><sub>9,10,8,17,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>2,1,1,0,2</sub> |  | 1.4<br><sub>3,1,2,4,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.3 | 0.9 | 13.2 |
| Matisse Thybulle (LAL) | 98% | 23.4<br><sub>19,23,24,28,23</sub> | 5.8<br><sub>6,3,2,4,6</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,1,2,2,0</sub> |  | 1.2<br><sub>2,2,0,0,1</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 2.3 | 0.7 | 0.7 | 9.2 |
| Collin Sexton (LAL) | 98% | 20.7<br><sub>16,16,11,24,27</sub> | 11.4<br><sub>6,10,0,17,18</sub> |  | 2.2<br><sub>1,3,0,2,2</sub> |  | 2.6<br><sub>5,1,1,2,6</sub> |  | 1.2<br><sub>0,1,0,0,3</sub> |  | 1.0 | 0.2 | 1.4 | 16.2 |
| Jarred Vanderbilt (LAL) | 71% | 12.6<br><sub>6,7,-,14,13</sub> | 3.0<br><sub>2,0,-,2,4</sub> |  | 3.5<br><sub>1,1,-,10,2</sub> |  | 1.1<br><sub>0,0,-,3,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 7.6 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Adou Thiero (LAL) | 91% | 8.2<br><sub>-,-,7,8,7</sub> | 2.7<br><sub>-,-,4,2,2</sub> |  | 2.2<br><sub>-,-,4,2,2</sub> |  | 0.6<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.6 |
| Jaden Hardy (LAL) | 52% | 6.7<br><sub>1,1,-,-,-</sub> | 3.8<br><sub>2,0,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Kevon Looney (LAL) | 26% | 6.5<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.4 |
| Cameron Carr (LAL) | 71% | 6.1<br><sub>1,1,-,-,7</sub> | 2.0<br><sub>0,0,-,-,2</sub> |  | 1.0<br><sub>0,0,-,-,3</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.5 |
| Chris Manon (LAL) | 58% | 5.6<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 2.9 |
| Carson Cooper (LAL) | 48% | 5.5<br><sub>3,-,-,-,-</sub> | 2.4<br><sub>1,-,-,-,-</sub> |  | 2.8<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.9 | 6.0 |
| Bronny James (LAL) | 52% | 5.5<br><sub>1,1,-,-,-</sub> | 2.1<br><sub>2,0,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.7 |
| Tyler Herro (MIL) | 100% | 32.6<br><sub>31,33,35,27,-</sub> | 20.4<br><sub>21,25,23,13,-</sub> | 19.5 · – | 4.6<br><sub>6,5,5,1,-</sub> | 4.5 | 5.2<br><sub>3,3,10,2,-</sub> | 3.5 | 2.6<br><sub>4,4,1,1,-</sub> | 2.5 | 0.8 | 0.2 | 2.6 | 30.1 |
| Kyle Kuzma (MIL) | 98% | 28.3<br><sub>22,27,32,31,26</sub> | 12.7<br><sub>2,6,13,27,5</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>2,5,4,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>3,4,3,0,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,1,1,6,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.4 | 1.9 | 20.7 |
| Jaime Jaquez Jr. (MIL) | 98% | 27.8<br><sub>28,31,28,23,25</sub> | 14.9<br><sub>19,18,14,4,16</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>8,2,3,2,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.8<br><sub>2,2,3,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>2,4,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 2.1 | 23.7 |
| Brayden Burries (MIL) | 98% | 25.5<br><sub>26,22,38,29,26</sub> | 11.2<br><sub>9,9,21,13,3</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>9,5,11,8,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>1,3,6,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,0,1,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.3 | 1.4 | 19.4 |
| Ryan Rollins (MIL) | 98% | 24.5<br><sub>17,24,14,20,24</sub> | 13.1<br><sub>10,13,10,7,14</sub> |  | 3.7<br><sub>3,9,1,5,5</sub> |  | 4.7<br><sub>2,5,1,6,2</sub> |  | 1.8<br><sub>1,2,1,2,4</sub> |  | 1.0 | 0.3 | 2.4 | 21.4 |
| AJ Green (MIL) | 98% | 18.7<br><sub>24,20,24,18,8</sub> | 6.9<br><sub>13,5,12,5,0</sub> |  | 1.8<br><sub>3,2,1,1,0</sub> |  | 1.3<br><sub>3,3,0,1,0</sub> |  | 1.3<br><sub>4,1,4,1,0</sub> |  | 0.3 | 0.1 | 0.7 | 9.9 |
| Kasparas Jakucionis (MIL) | 96% | 17.1<br><sub>22,12,10,7,23</sub> | 6.1<br><sub>7,3,3,1,11</sub> |  | 2.0<br><sub>5,1,0,2,0</sub> |  | 3.0<br><sub>7,1,2,0,4</sub> |  | 0.6<br><sub>0,1,0,0,2</sub> |  | 0.6 | 0.1 | 1.3 | 11.1 |
| Nate Ament (MIL) | 91% | 16.5<br><sub>8,18,15,23,22</sub> | 6.8<br><sub>4,9,7,12,10</sub> |  | 2.4<br><sub>1,2,1,5,2</sub> |  | 0.7<br><sub>0,0,0,1,1</sub> |  | 0.7<br><sub>0,2,0,2,2</sub> |  | 0.6 | 0.2 | 0.9 | 10.0 |
| Kel'el Ware (MIL) | 96% | 15.9<br><sub>17,16,13,9,17</sub> | 7.1<br><sub>2,2,4,0,8</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>9,5,3,0,4</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>0,1,0,1,1</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 1.2 | 13.0 |
| Cormac Ryan (MIL) | 16% | 14.8 | 7.3 |  | 1.6 |  | 1.1 |  | 0.9 |  | 0.5 | 0.2 | 1.0 | 10.0 |
| Ousmane Dieng (MIL) | 71% | 13.9<br><sub>-,2,-,15,24</sub> | 5.3<br><sub>-,0,-,10,8</sub> |  | 2.2<br><sub>-,0,-,1,3</sub> |  | 1.5<br><sub>-,0,-,0,0</sub> |  | 0.5<br><sub>-,0,-,2,2</sub> |  | 0.4 | 0.1 | 1.0 | 8.9 |
| Caris LeVert (MIL) | 16% | 12.7<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 7.8 |
| Jericho Sims (MIL) | 80% | 11.9<br><sub>15,1,7,15,8</sub> | 2.6<br><sub>0,0,0,2,2</sub> |  | 3.0<br><sub>2,0,1,2,0</sub> |  | 0.9<br><sub>1,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.1 | 0.7 | 6.5 |
| Pete Nance (MIL) | 16% | 11.5 | 3.7 |  | 1.9 |  | 0.8 |  | 0.4 |  | 0.3 | 0.2 | 0.5 | 6.4 |
| Kam Jones (MIL) | 16% | 10.0 | 2.6 |  | 1.0 |  | 2.2 |  | 0.2 |  | 0.4 | 0.1 | 0.7 | 5.8 |
| Gary Trent Jr. (MIL) | 52% | 9.2<br><sub>-,-,-,-,6</sub> | 4.0<br><sub>-,-,-,-,5</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.2 |
| Bogoljub Markovic (MIL) | 48% | 6.7<br><sub>-,-,-,-,4</sub> | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.7 |

</details>


### BKN @ NOP
Out: Bennedict Mathurin (NOP), Yves Missi (NOP), Trendon Watford (NOP), Mikel Brown Jr. (BKN), Grant Nelson (BKN), Ben Saraf (BKN), Nolan Traore (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.6–113.6 | BKN 36% | 2.78 / 1.56 | NOP -5.5 | 221.5 | NOP -3.5 covers 55%; o228.5 36% |
| Expected (weighted by chance each plays) | 108.5–114.2 | BKN 34% | 2.94 / 1.52 | NOP -5.5 | 222.5 | NOP -3.5 covers 57%; o228.5 38% |
| if Trey Murphy III plays | 108.2–116.0 | BKN 29% | 3.44 / 1.41 | NOP -7.5 | 223.5 | NOP -3.5 covers 63%; o228.5 40% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III (NOP) | Doubtful | 20% | 33.8 | 18.5 | 5.1 | 3.8 | 2.8 | 1.3 | 0.5 | 1.8 | 27.4 | full tables below |
| Malik Dia (NOP) | Doubtful | 20% | 8.6 | 3.4 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.7 | small |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 98% | 35.0<br><sub>36,37,38,36,29</sub> | 23.3<br><sub>23,18,26,25,19</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,5,10,9,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>3,2,0,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>3,4,4,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 2.7 | 33.2 |
| Julius Randle | 98% | 34.8<br><sub>37,36,31,34,30</sub> | 21.6<br><sub>20,21,22,19,13</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>5,11,3,7,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>6,2,4,8,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>4,0,2,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.3 | 3.8 | 34.4 |
| Danny Wolf | 66% | 26.4<br><sub>-,-,19,31,36</sub> | 10.8<br><sub>-,-,12,11,10</sub> |  | 6.3<br><sub>-,-,5,9,3</sub> |  | 2.9<br><sub>-,-,3,1,2</sub> |  | 1.4<br><sub>-,-,2,2,1</sub> |  | 0.7 | 0.7 | 1.6 | 20.0 |
| Day'Ron Sharpe | 98% | 25.6<br><sub>26,22,27,32,20</sub> | 11.1<br><sub>15,4,6,12,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 9.3<br><sub>13,6,5,10,4</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 4.4<br><sub>4,3,8,13,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 0.3<br><sub>1,0,0,0,0</sub> |  | 1.2 | 1.1 | 2.1 | 24.9 |
| Egor Demin | 98% | 23.5<br><sub>-,-,-,-,-</sub> | 9.9<br><sub>-,-,-,-,-</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.3 | 1.6 | 16.1 |
| Keon Ellis | 80% | 22.6<br><sub>20,25,10,-,22</sub> | 6.2<br><sub>0,5,1,-,3</sub> |  | 2.2<br><sub>2,1,2,-,1</sub> |  | 1.8<br><sub>1,0,0,-,4</sub> |  | 0.9<br><sub>0,1,0,-,1</sub> |  | 1.3 | 0.7 | 0.8 | 10.2 |
| Noah Clowney | 98% | 20.5<br><sub>24,20,17,21,8</sub> | 7.6<br><sub>8,2,7,3,2</sub> |  | 3.9<br><sub>3,6,1,10,0</sub> |  | 1.2<br><sub>0,2,1,0,0</sub> |  | 1.0<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 1.1 | 12.6 |
| Terance Mann | 67% | 19.3<br><sub>15,-,16,13,22</sub> | 4.6<br><sub>0,-,0,0,0</sub> |  | 2.3<br><sub>1,-,2,2,1</sub> |  | 2.0<br><sub>1,-,2,0,1</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.2 | 0.8 | 8.9 |
| Moritz Wagner | 96% | 19.1<br><sub>21,20,20,16,16</sub> | 10.6<br><sub>14,6,6,9,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>6,1,1,2,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>1,1,0,1,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.3 | 1.2 | 16.4 |
| Chaney Johnson | 96% | 17.7<br><sub>31,28,9,8,15</sub> | 5.3<br><sub>2,4,0,5,2</sub> |  | 2.4<br><sub>2,3,2,2,0</sub> |  | 1.1<br><sub>0,2,1,1,1</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.3 | 1.0 | 8.7 |
| Drake Powell | 52% | 14.2<br><sub>-,-,-,-,9</sub> | 4.4<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.9 |
| Josh Minott | 58% | 12.1<br><sub>-,-,6,-,12</sub> | 6.3<br><sub>-,-,0,-,10</sub> |  | 2.2<br><sub>-,-,1,-,2</sub> |  | 0.7<br><sub>-,-,0,-,1</sub> |  | 0.8<br><sub>-,-,0,-,2</sub> |  | 0.7 | 0.4 | 0.7 | 9.2 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zion Williamson | 98% | 34.8<br><sub>35,38,36,31,-</sub> | 22.0<br><sub>25,23,13,25,-</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>11,4,8,4,-</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>4,2,4,2,-</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 1.6 | 0.7 | 2.3 | 32.0 |
| Dejounte Murray | 98% | 33.9<br><sub>-,45,35,28,18</sub> | 17.9<br><sub>-,20,7,6,12</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 6.0<br><sub>-,8,2,3,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>-,4,4,3,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>-,1,1,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.9 | 0.5 | 3.0 | 30.4 |
| Jeremiah Fears | 98% | 32.5<br><sub>38,34,36,29,29</sub> | 18.2<br><sub>12,19,24,25,11</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>4,6,5,6,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>7,2,5,5,8</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.5 | 0.6 | 2.8 | 28.6 |
| Saddiq Bey | 98% | 31.7<br><sub>36,29,31,26,24</sub> | 17.2<br><sub>18,22,17,13,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,4,5,4,0</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>1,3,4,3,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.1<br><sub>2,2,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 1.4 | 24.9 |
| Herbert Jones | 98% | 27.3<br><sub>28,37,14,20,24</sub> | 8.3<br><sub>9,2,0,4,10</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,5,4,0,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>3,1,0,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>3,0,0,0,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.6 | 1.2 | 13.8 |
| Derik Queen | 98% | 26.2<br><sub>24,27,10,21,21</sub> | 13.4<br><sub>20,20,6,8,16</sub> | 9.5 · –<br><sub>o 55% · u 45%</sub> | 7.8<br><sub>7,9,4,5,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>5,6,1,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.1 | 1.0 | 2.3 | 24.6 |
| Karlo Matkovic | 96% | 24.0<br><sub>29,21,18,19,17</sub> | 10.0<br><sub>25,5,18,3,4</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>6,4,3,3,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,2,1,2,2</sub> |  | 1.1<br><sub>5,1,4,1,0</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 1.1 | 1.0 | 17.1 |
| Jordan Poole | 58% | 22.7<br><sub>-,-,-,-,34</sub> | 10.5<br><sub>-,-,-,-,7</sub> |  | 2.5<br><sub>-,-,-,-,3</sub> |  | 3.0<br><sub>-,-,-,-,2</sub> |  | 1.7<br><sub>-,-,-,-,1</sub> |  | 0.8 | 0.5 | 1.7 | 16.0 |
| Bryce McGowens | 64% | 18.2<br><sub>6,-,-,3,28</sub> | 5.9<br><sub>0,-,-,0,8</sub> |  | 1.9<br><sub>1,-,-,0,2</sub> |  | 1.2<br><sub>0,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,0,1</sub> |  | 0.8 | 0.3 | 0.7 | 9.1 |
| DeAndre Jordan | 23% | 14.8<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 5.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.9 | 0.8 | 10.2 |
| AJ Johnson | 52% | 9.4<br><sub>-,-,-,3,12</sub> | 2.8<br><sub>-,-,-,2,2</sub> |  | 1.5<br><sub>-,-,-,0,2</sub> |  | 0.9<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 5.1 |
| Jaron Pierre Jr. | 37% | 8.7 | 3.5 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Julian Reese | 52% | 8.5<br><sub>-,-,-,3,9</sub> | 2.7<br><sub>-,-,-,0,2</sub> |  | 1.8<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.3 | 0.5 | 5.1 |

</details>

<details><summary>if Trey Murphy III plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. (BKN) | 98% | 35.0<br><sub>36,37,38,36,29</sub> | 23.2<br><sub>23,18,26,25,19</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,5,10,9,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>3,2,0,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>3,4,4,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 2.7 | 33.1 |
| Julius Randle (BKN) | 98% | 34.8<br><sub>37,36,31,34,30</sub> | 21.6<br><sub>20,21,22,19,13</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>5,11,3,7,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>6,2,4,8,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>4,0,2,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.3 | 3.8 | 34.4 |
| Danny Wolf (BKN) | 66% | 26.5<br><sub>-,-,19,31,36</sub> | 10.8<br><sub>-,-,12,11,10</sub> |  | 6.3<br><sub>-,-,5,9,3</sub> |  | 2.9<br><sub>-,-,3,1,2</sub> |  | 1.4<br><sub>-,-,2,2,1</sub> |  | 0.7 | 0.7 | 1.7 | 20.0 |
| Day'Ron Sharpe (BKN) | 98% | 25.4<br><sub>26,22,27,32,20</sub> | 11.0<br><sub>15,4,6,12,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 9.3<br><sub>13,6,5,10,4</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 4.4<br><sub>4,3,8,13,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 0.3<br><sub>1,0,0,0,0</sub> |  | 1.2 | 1.1 | 2.1 | 24.6 |
| Egor Demin (BKN) | 98% | 23.6<br><sub>-,-,-,-,-</sub> | 9.9<br><sub>-,-,-,-,-</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.3 | 1.6 | 16.2 |
| Keon Ellis (BKN) | 80% | 22.6<br><sub>20,25,10,-,22</sub> | 6.1<br><sub>0,5,1,-,3</sub> |  | 2.2<br><sub>2,1,2,-,1</sub> |  | 1.8<br><sub>1,0,0,-,4</sub> |  | 0.9<br><sub>0,1,0,-,1</sub> |  | 1.2 | 0.7 | 0.8 | 10.1 |
| Noah Clowney (BKN) | 98% | 20.4<br><sub>24,20,17,21,8</sub> | 7.5<br><sub>8,2,7,3,2</sub> |  | 3.9<br><sub>3,6,1,10,0</sub> |  | 1.2<br><sub>0,2,1,0,0</sub> |  | 1.0<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 1.1 | 12.6 |
| Terance Mann (BKN) | 67% | 19.3<br><sub>15,-,16,13,22</sub> | 4.6<br><sub>0,-,0,0,0</sub> |  | 2.3<br><sub>1,-,2,2,1</sub> |  | 2.0<br><sub>1,-,2,0,1</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 8.9 |
| Moritz Wagner (BKN) | 96% | 19.2<br><sub>21,20,20,16,16</sub> | 10.7<br><sub>14,6,6,9,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>6,1,1,2,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>1,1,0,1,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.3 | 1.2 | 16.5 |
| Chaney Johnson (BKN) | 96% | 17.8<br><sub>31,28,9,8,15</sub> | 5.3<br><sub>2,4,0,5,2</sub> |  | 2.4<br><sub>2,3,2,2,0</sub> |  | 1.1<br><sub>0,2,1,1,1</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.3 | 1.1 | 8.8 |
| Drake Powell (BKN) | 52% | 14.3<br><sub>-,-,-,-,9</sub> | 4.5<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.8 | 7.0 |
| Josh Minott (BKN) | 58% | 12.1<br><sub>-,-,6,-,12</sub> | 6.4<br><sub>-,-,0,-,10</sub> |  | 2.2<br><sub>-,-,1,-,2</sub> |  | 0.7<br><sub>-,-,0,-,1</sub> |  | 0.8<br><sub>-,-,0,-,2</sub> |  | 0.7 | 0.4 | 0.7 | 9.3 |
| Trey Murphy III (NOP) | 100% | 33.8<br><sub>40,-,34,30,-</sub> | 18.5<br><sub>18,-,10,26,-</sub> |  | 5.1<br><sub>5,-,4,7,-</sub> |  | 3.8<br><sub>5,-,5,3,-</sub> |  | 2.8<br><sub>3,-,1,4,-</sub> |  | 1.3 | 0.5 | 1.8 | 27.4 |
| Zion Williamson (NOP) | 98% | 32.8<br><sub>35,38,36,31,-</sub> | 20.0<br><sub>25,23,13,25,-</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>11,4,8,4,-</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>4,2,4,2,-</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 1.5 | 0.7 | 2.2 | 29.4 |
| Dejounte Murray (NOP) | 98% | 32.4<br><sub>-,45,35,28,18</sub> | 16.3<br><sub>-,20,7,6,12</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>-,8,2,3,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>-,4,4,3,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>-,1,1,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.9 | 0.5 | 3.0 | 28.4 |
| Jeremiah Fears (NOP) | 98% | 30.5<br><sub>38,34,36,29,29</sub> | 16.3<br><sub>12,19,24,25,11</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>4,6,5,6,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>7,2,5,5,8</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.6 | 2.6 | 25.9 |
| Saddiq Bey (NOP) | 98% | 28.4<br><sub>36,29,31,26,24</sub> | 15.6<br><sub>18,22,17,13,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>5,4,5,4,0</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>1,3,4,3,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.9<br><sub>2,2,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 1.2 | 22.5 |
| Herbert Jones (NOP) | 98% | 23.0<br><sub>28,37,14,20,24</sub> | 6.7<br><sub>9,2,0,4,10</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>4,5,4,0,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>3,1,0,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>3,0,0,0,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.5 | 1.0 | 11.4 |
| Derik Queen (NOP) | 98% | 22.6<br><sub>24,27,10,21,21</sub> | 11.1<br><sub>20,20,6,8,16</sub> | 9.5 · –<br><sub>o 55% · u 45%</sub> | 6.7<br><sub>7,9,4,5,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>5,6,1,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>1,0,0,0,0</sub> |  | 1.0 | 0.9 | 2.0 | 20.8 |
| Karlo Matkovic (NOP) | 96% | 19.6<br><sub>29,21,18,19,17</sub> | 7.8<br><sub>25,5,18,3,4</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>6,4,3,3,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>1,2,1,2,2</sub> |  | 0.9<br><sub>5,1,4,1,0</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.7 | 0.9 | 0.8 | 13.6 |
| Jordan Poole (NOP) | 58% | 18.8<br><sub>-,-,-,-,34</sub> | 8.6<br><sub>-,-,-,-,7</sub> |  | 2.1<br><sub>-,-,-,-,3</sub> |  | 2.4<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.7 | 0.4 | 1.4 | 13.0 |
| Bryce McGowens (NOP) | 64% | 15.1<br><sub>6,-,-,3,28</sub> | 5.2<br><sub>0,-,-,0,8</sub> |  | 1.6<br><sub>1,-,-,0,2</sub> |  | 1.0<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>0,-,-,0,1</sub> |  | 0.7 | 0.2 | 0.5 | 7.7 |
| DeAndre Jordan (NOP) | 23% | 11.8<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 4.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.7 | 0.7 | 8.4 |
| Jaron Pierre Jr. (NOP) | 37% | 8.5 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.8 |
| AJ Johnson (NOP) | 52% | 7.2<br><sub>-,-,-,3,12</sub> | 2.3<br><sub>-,-,-,2,2</sub> |  | 1.1<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.1 |
| Julian Reese (NOP) | 52% | 6.6<br><sub>-,-,-,3,9</sub> | 2.3<br><sub>-,-,-,0,2</sub> |  | 1.4<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.1 |

</details>


### ORL @ UTA
Out: Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.7–108.4 | ORL 59% | 1.70 / 2.44 | UTA +3.5 | 220.5 | UTA +4.5 covers 53%; o214.5 62% |
| Expected (weighted by chance each plays) | 113.4–109.3 | ORL 62% | 1.62 / 2.61 | UTA +4.5 | 222.5 | UTA +4.5 covers 50%; o214.5 67% |
| if Keyonte George plays | 111.6–110.4 | ORL 53% | 1.89 / 2.13 | UTA +1.5 | 221.5 | UTA +4.5 covers 59%; o214.5 65% |
| if Tristan da Silva plays | 114.1–108.4 | ORL 65% | 1.53 / 2.90 | UTA +5.5 | 222.5 | UTA +4.5 covers 47%; o214.5 66% |
| if Jamal Cain plays | 112.9–107.8 | ORL 64% | 1.57 / 2.75 | UTA +5.5 | 220.5 | UTA +4.5 covers 48%; o214.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George (UTA) | Questionable | 55% | 32.0 | 22.3 | 3.6 | 5.7 | 2.2 | 0.9 | 0.2 | 3.4 | 31.6 | full tables below |
| Tristan da Silva (ORL) | Day-To-Day | 70% | 31.4 | 14.3 | 4.7 | 2.2 | 2.4 | 1.0 | 0.4 | 1.5 | 21.1 | full tables below |
| Jamal Cain (ORL) | Questionable | 55% | 25.4 | 10.1 | 4.5 | 1.2 | 1.2 | 0.8 | 0.4 | 1.2 | 15.8 | full tables below |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 36.4<br><sub>40,38,38,40,38</sub> | 26.8<br><sub>14,24,15,30,33</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>6,3,8,6,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 7.1<br><sub>12,6,15,11,7</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.4 | 3.5 | 40.1 |
| Desmond Bane | 98% | 35.9<br><sub>40,36,32,-,36</sub> | 23.8<br><sub>19,20,15,-,15</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>2,3,6,-,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>1,3,0,-,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.5<br><sub>5,4,3,-,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.5 | 0.5 | 2.5 | 32.4 |
| Wendell Carter Jr. | 98% | 33.8<br><sub>35,34,34,40,33</sub> | 14.7<br><sub>7,6,27,19,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 8.7<br><sub>10,9,13,11,11</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>0,0,2,0,1</sub> |  | 1.0<br><sub>1,0,2,3,0</sub> |  | 1.1 | 1.1 | 1.8 | 25.6 |
| Anthony Black | 98% | 33.7<br><sub>33,-,31,38,33</sub> | 19.1<br><sub>23,-,10,18,26</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>8,-,7,8,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>3,-,6,6,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,-,1,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.1 | 0.8 | 2.5 | 29.1 |
| Jase Richardson | 96% | 26.8<br><sub>26,29,26,30,15</sub> | 10.4<br><sub>4,9,10,2,6</sub> |  | 3.0<br><sub>1,1,2,4,1</sub> |  | 3.0<br><sub>3,5,3,4,1</sub> |  | 1.0<br><sub>0,0,2,0,0</sub> |  | 1.1 | 0.4 | 1.2 | 16.3 |
| Alex Morales | 80% | 22.4<br><sub>-,14,6,15,29</sub> | 5.0<br><sub>-,3,0,0,7</sub> |  | 3.5<br><sub>-,2,0,2,7</sub> |  | 1.4<br><sub>-,0,0,1,0</sub> |  | 0.4<br><sub>-,0,0,0,1</sub> |  | 0.8 | 0.2 | 1.1 | 9.9 |
| Jevon Carter | 71% | 16.2<br><sub>-,18,3,15,4</sub> | 6.1<br><sub>-,5,0,9,0</sub> |  | 1.5<br><sub>-,1,0,1,0</sub> |  | 1.6<br><sub>-,4,0,0,0</sub> |  | 1.0<br><sub>-,1,0,3,0</sub> |  | 0.8 | 0.2 | 0.6 | 9.2 |
| Nikola Vucevic | 98% | 15.7<br><sub>7,14,4,6,18</sub> | 6.8<br><sub>2,7,0,0,5</sub> |  | 4.5<br><sub>4,6,0,1,4</sub> |  | 1.7<br><sub>2,1,0,2,1</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.4 | 0.5 | 0.7 | 12.9 |
| Goga Bitadze | 84% | 14.8<br><sub>5,-,8,7,15</sub> | 5.5<br><sub>0,-,4,4,2</sub> |  | 5.0<br><sub>1,-,5,5,2</sub> |  | 1.2<br><sub>0,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.0 | 0.7 | 11.7 |
| Colin Castleton | 38% | 8.8<br><sub>-,-,2,-,-</sub> | 3.0<br><sub>-,-,0,-,-</sub> |  | 2.6<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 6.3 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ace Bailey | 98% | 33.0<br><sub>24,35,29,32,35</sub> | 17.9<br><sub>5,15,12,7,23</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>6,5,6,2,7</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,1,0,3,2</sub> |  | 2.2<br><sub>1,1,0,1,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.1 | 2.3 | 25.6 |
| Darryn Peterson | 98% | 32.7<br><sub>33,30,30,35,31</sub> | 18.4<br><sub>14,7,21,26,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,2,2,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>6,7,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,0,3,4,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.8 | 2.4 | 26.6 |
| Josh Green | 91% | 27.4<br><sub>15,23,24,28,30</sub> | 5.8<br><sub>3,7,3,10,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>1,1,3,0,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,0,1,1,4</sub> |  | 0.7<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 1.0 | 10.0 |
| Jaxson Hayes | 98% | 26.5<br><sub>22,21,28,29,17</sub> | 10.1<br><sub>9,2,8,18,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>5,7,6,6,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.4 | 17.9 |
| Josh Okogie | 96% | 25.9<br><sub>19,26,24,17,21</sub> | 6.6<br><sub>9,3,12,0,6</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>3,6,4,1,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,1,0,0,4</sub> |  | 0.7<br><sub>1,1,2,0,0</sub> |  | 1.2 | 0.4 | 1.1 | 12.4 |
| Isaiah Collier | 98% | 24.8<br><sub>12,3,13,16,24</sub> | 12.5<br><sub>7,0,4,6,17</sub> |  | 3.3<br><sub>2,1,3,4,5</sub> |  | 6.2<br><sub>2,0,3,2,5</sub> |  | 0.5<br><sub>0,0,0,0,4</sub> |  | 1.0 | 0.3 | 2.6 | 22.0 |
| Brice Sensabaugh | 98% | 21.9<br><sub>14,12,10,13,14</sub> | 14.4<br><sub>7,6,0,2,5</sub> |  | 3.3<br><sub>2,2,2,3,4</sub> |  | 2.0<br><sub>1,0,2,0,4</sub> |  | 2.0<br><sub>1,1,0,0,1</sub> |  | 0.7 | 0.2 | 1.8 | 19.7 |
| Svi Mykhailiuk | 96% | 21.8<br><sub>14,17,14,6,21</sub> | 9.1<br><sub>3,6,0,0,7</sub> |  | 2.4<br><sub>2,3,0,0,2</sub> |  | 1.6<br><sub>0,0,1,0,3</sub> |  | 1.4<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 13.1 |
| Mo Bamba | 71% | 19.2<br><sub>18,15,-,17,17</sub> | 6.4<br><sub>8,7,-,3,7</sub> |  | 6.7<br><sub>8,10,-,3,7</sub> |  | 0.9<br><sub>0,1,-,1,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 1.5 | 1.0 | 14.0 |
| Kyle Filipowski | 76% | 18.8<br><sub>8,-,1,15,15</sub> | 10.0<br><sub>1,-,0,9,7</sub> |  | 5.7<br><sub>2,-,0,6,4</sub> |  | 2.1<br><sub>0,-,0,1,1</sub> |  | 0.8<br><sub>0,-,0,1,0</sub> |  | 0.8 | 0.5 | 1.4 | 17.8 |
| Kobe Bufkin | 23% | 15.2<br><sub>-,-,-,-,-</sub> | 6.5<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.9 | 10.2 |
| Tony Bradley | 67% | 13.9<br><sub>7,-,1,2,14</sub> | 4.3<br><sub>2,-,0,0,4</sub> |  | 4.1<br><sub>3,-,1,1,5</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.1 |
| Harrison Ingram | 8% | 8.8<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |

</details>

<details><summary>if Jamal Cain plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner (ORL) | 98% | 35.8<br><sub>40,38,38,40,38</sub> | 25.9<br><sub>14,24,15,30,33</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>6,3,8,6,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 7.2<br><sub>12,6,15,11,7</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.4 | 3.3 | 39.2 |
| Desmond Bane (ORL) | 98% | 35.0<br><sub>40,36,32,-,36</sub> | 22.7<br><sub>19,20,15,-,15</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>2,3,6,-,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>1,3,0,-,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.2<br><sub>5,4,3,-,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.5 | 2.5 | 31.1 |
| Wendell Carter Jr. (ORL) | 98% | 33.4<br><sub>35,34,34,40,33</sub> | 14.1<br><sub>7,6,27,19,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 8.8<br><sub>10,9,13,11,11</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>0,0,2,0,1</sub> |  | 1.0<br><sub>1,0,2,3,0</sub> |  | 1.0 | 1.1 | 1.7 | 24.9 |
| Anthony Black (ORL) | 98% | 32.4<br><sub>33,-,31,38,33</sub> | 17.6<br><sub>23,-,10,18,26</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>8,-,7,8,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.9<br><sub>3,-,6,6,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,-,1,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.0 | 0.7 | 2.4 | 27.3 |
| Jamal Cain (ORL) | 100% | 25.4<br><sub>18,25,25,36,20</sub> | 10.1<br><sub>5,10,5,18,5</sub> |  | 4.5<br><sub>1,3,5,12,3</sub> |  | 1.2<br><sub>1,1,0,1,1</sub> |  | 1.2<br><sub>1,2,1,2,1</sub> |  | 0.8 | 0.4 | 1.2 | 15.8 |
| Jase Richardson (ORL) | 96% | 23.9<br><sub>26,29,26,30,15</sub> | 8.6<br><sub>4,9,10,2,6</sub> |  | 2.7<br><sub>1,1,2,4,1</sub> |  | 2.7<br><sub>3,5,3,4,1</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 1.0 | 0.3 | 1.0 | 13.9 |
| Alex Morales (ORL) | 80% | 20.1<br><sub>-,14,6,15,29</sub> | 4.7<br><sub>-,3,0,0,7</sub> |  | 3.2<br><sub>-,2,0,2,7</sub> |  | 1.2<br><sub>-,0,0,1,0</sub> |  | 0.3<br><sub>-,0,0,0,1</sub> |  | 0.7 | 0.2 | 1.2 | 9.1 |
| Nikola Vucevic (ORL) | 98% | 14.2<br><sub>7,14,4,6,18</sub> | 6.1<br><sub>2,7,0,0,5</sub> |  | 3.9<br><sub>4,6,0,1,4</sub> |  | 1.5<br><sub>2,1,0,2,1</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.4 | 0.5 | 0.7 | 11.6 |
| Jevon Carter (ORL) | 71% | 14.0<br><sub>-,18,3,15,4</sub> | 5.3<br><sub>-,5,0,9,0</sub> |  | 1.3<br><sub>-,1,0,1,0</sub> |  | 1.4<br><sub>-,4,0,0,0</sub> |  | 0.8<br><sub>-,1,0,3,0</sub> |  | 0.7 | 0.2 | 0.5 | 8.1 |
| Goga Bitadze (ORL) | 84% | 13.6<br><sub>5,-,8,7,15</sub> | 5.0<br><sub>0,-,4,4,2</sub> |  | 4.6<br><sub>1,-,5,5,2</sub> |  | 1.1<br><sub>0,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 1.0 | 0.7 | 10.7 |
| Colin Castleton (ORL) | 38% | 7.1<br><sub>-,-,2,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 2.1<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.1 |
| Ace Bailey (UTA) | 98% | 33.0<br><sub>24,35,29,32,35</sub> | 18.0<br><sub>5,15,12,7,23</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>6,5,6,2,7</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,1,0,3,2</sub> |  | 2.2<br><sub>1,1,0,1,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.1 | 2.3 | 25.6 |
| Darryn Peterson (UTA) | 98% | 32.7<br><sub>33,30,30,35,31</sub> | 18.4<br><sub>14,7,21,26,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,2,2,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>6,7,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,0,3,4,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.8 | 2.4 | 26.6 |
| Josh Green (UTA) | 91% | 27.4<br><sub>15,23,24,28,30</sub> | 5.8<br><sub>3,7,3,10,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>1,1,3,0,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,0,1,1,4</sub> |  | 0.7<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 1.0 | 10.0 |
| Jaxson Hayes (UTA) | 98% | 26.6<br><sub>22,21,28,29,17</sub> | 10.1<br><sub>9,2,8,18,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>5,7,6,6,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.4 | 17.9 |
| Josh Okogie (UTA) | 96% | 25.9<br><sub>19,26,24,17,21</sub> | 6.6<br><sub>9,3,12,0,6</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>3,6,4,1,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,1,0,0,4</sub> |  | 0.7<br><sub>1,1,2,0,0</sub> |  | 1.2 | 0.4 | 1.1 | 12.4 |
| Isaiah Collier (UTA) | 98% | 24.8<br><sub>12,3,13,16,24</sub> | 12.4<br><sub>7,0,4,6,17</sub> |  | 3.3<br><sub>2,1,3,4,5</sub> |  | 6.2<br><sub>2,0,3,2,5</sub> |  | 0.5<br><sub>0,0,0,0,4</sub> |  | 1.0 | 0.3 | 2.6 | 21.9 |
| Svi Mykhailiuk (UTA) | 96% | 21.9<br><sub>14,17,14,6,21</sub> | 9.1<br><sub>3,6,0,0,7</sub> |  | 2.4<br><sub>2,3,0,0,2</sub> |  | 1.6<br><sub>0,0,1,0,3</sub> |  | 1.4<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 13.1 |
| Brice Sensabaugh (UTA) | 98% | 21.8<br><sub>14,12,10,13,14</sub> | 14.1<br><sub>7,6,0,2,5</sub> |  | 3.3<br><sub>2,2,2,3,4</sub> |  | 2.0<br><sub>1,0,2,0,4</sub> |  | 2.0<br><sub>1,1,0,0,1</sub> |  | 0.7 | 0.2 | 1.8 | 19.4 |
| Mo Bamba (UTA) | 71% | 19.3<br><sub>18,15,-,17,17</sub> | 6.4<br><sub>8,7,-,3,7</sub> |  | 6.7<br><sub>8,10,-,3,7</sub> |  | 0.9<br><sub>0,1,-,1,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 1.5 | 1.0 | 14.0 |
| Kyle Filipowski (UTA) | 76% | 18.8<br><sub>8,-,1,15,15</sub> | 10.0<br><sub>1,-,0,9,7</sub> |  | 5.7<br><sub>2,-,0,6,4</sub> |  | 2.1<br><sub>0,-,0,1,1</sub> |  | 0.8<br><sub>0,-,0,1,0</sub> |  | 0.7 | 0.5 | 1.4 | 17.8 |
| Kobe Bufkin (UTA) | 23% | 15.1<br><sub>-,-,-,-,-</sub> | 6.3<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.9 | 10.1 |
| Tony Bradley (UTA) | 67% | 13.8<br><sub>7,-,1,2,14</sub> | 4.3<br><sub>2,-,0,0,4</sub> |  | 4.1<br><sub>3,-,1,1,5</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.0 |
| Harrison Ingram (UTA) | 8% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Keyonte George plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner (ORL) | 98% | 36.3<br><sub>40,38,38,40,38</sub> | 26.7<br><sub>14,24,15,30,33</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>6,3,8,6,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 7.1<br><sub>12,6,15,11,7</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.4 | 3.5 | 40.0 |
| Desmond Bane (ORL) | 98% | 35.8<br><sub>40,36,32,-,36</sub> | 23.7<br><sub>19,20,15,-,15</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>2,3,6,-,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>1,3,0,-,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.4<br><sub>5,4,3,-,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.5 | 2.5 | 32.3 |
| Wendell Carter Jr. (ORL) | 98% | 33.9<br><sub>35,34,34,40,33</sub> | 14.7<br><sub>7,6,27,19,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 8.8<br><sub>10,9,13,11,11</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>0,0,2,0,1</sub> |  | 1.0<br><sub>1,0,2,3,0</sub> |  | 1.1 | 1.1 | 1.8 | 25.6 |
| Anthony Black (ORL) | 98% | 33.6<br><sub>33,-,31,38,33</sub> | 19.0<br><sub>23,-,10,18,26</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>8,-,7,8,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>3,-,6,6,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,-,1,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.1 | 0.7 | 2.5 | 29.1 |
| Jase Richardson (ORL) | 96% | 26.8<br><sub>26,29,26,30,15</sub> | 10.3<br><sub>4,9,10,2,6</sub> |  | 3.0<br><sub>1,1,2,4,1</sub> |  | 2.9<br><sub>3,5,3,4,1</sub> |  | 1.0<br><sub>0,0,2,0,0</sub> |  | 1.1 | 0.4 | 1.2 | 16.2 |
| Alex Morales (ORL) | 80% | 22.5<br><sub>-,14,6,15,29</sub> | 5.0<br><sub>-,3,0,0,7</sub> |  | 3.5<br><sub>-,2,0,2,7</sub> |  | 1.4<br><sub>-,0,0,1,0</sub> |  | 0.4<br><sub>-,0,0,0,1</sub> |  | 0.8 | 0.2 | 1.1 | 9.9 |
| Jevon Carter (ORL) | 71% | 16.3<br><sub>-,18,3,15,4</sub> | 6.2<br><sub>-,5,0,9,0</sub> |  | 1.5<br><sub>-,1,0,1,0</sub> |  | 1.6<br><sub>-,4,0,0,0</sub> |  | 1.0<br><sub>-,1,0,3,0</sub> |  | 0.8 | 0.2 | 0.6 | 9.3 |
| Nikola Vucevic (ORL) | 98% | 15.7<br><sub>7,14,4,6,18</sub> | 6.8<br><sub>2,7,0,0,5</sub> |  | 4.4<br><sub>4,6,0,1,4</sub> |  | 1.7<br><sub>2,1,0,2,1</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.4 | 0.6 | 0.7 | 12.9 |
| Goga Bitadze (ORL) | 84% | 14.9<br><sub>5,-,8,7,15</sub> | 5.5<br><sub>0,-,4,4,2</sub> |  | 5.0<br><sub>1,-,5,5,2</sub> |  | 1.2<br><sub>0,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.0 | 0.7 | 11.7 |
| Colin Castleton (ORL) | 38% | 8.9<br><sub>-,-,2,-,-</sub> | 3.1<br><sub>-,-,0,-,-</sub> |  | 2.7<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 6.4 |
| Keyonte George (UTA) | 100% | 32.0<br><sub>22,44,32,30,-</sub> | 22.3<br><sub>7,39,16,19,-</sub> |  | 3.6<br><sub>7,2,6,5,-</sub> |  | 5.7<br><sub>0,9,9,8,-</sub> |  | 2.2<br><sub>1,2,1,0,-</sub> |  | 0.9 | 0.2 | 3.4 | 31.6 |
| Ace Bailey (UTA) | 98% | 31.3<br><sub>24,35,29,32,35</sub> | 15.0<br><sub>5,15,12,7,23</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>6,5,6,2,7</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>2,1,0,3,2</sub> |  | 2.0<br><sub>1,1,0,1,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.0 | 1.9 | 22.1 |
| Darryn Peterson (UTA) | 98% | 30.9<br><sub>33,30,30,35,31</sub> | 16.2<br><sub>14,7,21,26,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>4,2,2,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.7<br><sub>6,7,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,0,3,4,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.7 | 2.1 | 23.8 |
| Jaxson Hayes (UTA) | 98% | 25.1<br><sub>22,21,28,29,17</sub> | 8.7<br><sub>9,2,8,18,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>5,7,6,6,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.1 | 15.9 |
| Josh Green (UTA) | 91% | 24.6<br><sub>15,23,24,28,30</sub> | 5.3<br><sub>3,7,3,10,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>1,1,3,0,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,0,1,1,4</sub> |  | 0.7<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.8 | 9.0 |
| Josh Okogie (UTA) | 96% | 21.5<br><sub>19,26,24,17,21</sub> | 5.3<br><sub>9,3,12,0,6</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,6,4,1,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>2,1,0,0,4</sub> |  | 0.6<br><sub>1,1,2,0,0</sub> |  | 1.0 | 0.3 | 0.8 | 10.0 |
| Isaiah Collier (UTA) | 98% | 20.0<br><sub>12,3,13,16,24</sub> | 9.4<br><sub>7,0,4,6,17</sub> |  | 2.6<br><sub>2,1,3,4,5</sub> |  | 5.0<br><sub>2,0,3,2,5</sub> |  | 0.4<br><sub>0,0,0,0,4</sub> |  | 0.8 | 0.3 | 2.0 | 17.1 |
| Brice Sensabaugh (UTA) | 98% | 18.3<br><sub>14,12,10,13,14</sub> | 11.6<br><sub>7,6,0,2,5</sub> |  | 2.9<br><sub>2,2,2,3,4</sub> |  | 1.5<br><sub>1,0,2,0,4</sub> |  | 1.6<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.2 | 1.4 | 16.0 |
| Svi Mykhailiuk (UTA) | 96% | 17.2<br><sub>14,17,14,6,21</sub> | 6.6<br><sub>3,6,0,0,7</sub> |  | 1.9<br><sub>2,3,0,0,2</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.7 | 9.7 |
| Mo Bamba (UTA) | 71% | 16.4<br><sub>18,15,-,17,17</sub> | 5.4<br><sub>8,7,-,3,7</sub> |  | 5.7<br><sub>8,10,-,3,7</sub> |  | 0.7<br><sub>0,1,-,1,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 1.4 | 0.8 | 11.8 |
| Kyle Filipowski (UTA) | 76% | 16.4<br><sub>8,-,1,15,15</sub> | 8.4<br><sub>1,-,0,9,7</sub> |  | 4.8<br><sub>2,-,0,6,4</sub> |  | 1.6<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>0,-,0,1,0</sub> |  | 0.7 | 0.4 | 1.2 | 14.9 |
| Tony Bradley (UTA) | 67% | 11.2<br><sub>7,-,1,2,14</sub> | 3.5<br><sub>2,-,0,0,4</sub> |  | 3.3<br><sub>3,-,1,1,5</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 7.3 |
| Kobe Bufkin (UTA) | 23% | 9.4<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Harrison Ingram (UTA) | 8% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.1 |

</details>

<details><summary>if Tristan da Silva plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner (ORL) | 98% | 35.1<br><sub>40,38,38,40,38</sub> | 25.6<br><sub>14,24,15,30,33</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>6,3,8,6,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 7.0<br><sub>12,6,15,11,7</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.4 | 3.3 | 38.5 |
| Desmond Bane (ORL) | 98% | 34.1<br><sub>40,36,32,-,36</sub> | 21.6<br><sub>19,20,15,-,15</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>2,3,6,-,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.7<br><sub>1,3,0,-,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.1<br><sub>5,4,3,-,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.5 | 2.4 | 29.8 |
| Wendell Carter Jr. (ORL) | 98% | 32.5<br><sub>35,34,34,40,33</sub> | 13.4<br><sub>7,6,27,19,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 8.5<br><sub>10,9,13,11,11</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>0,0,2,0,1</sub> |  | 0.9<br><sub>1,0,2,3,0</sub> |  | 1.0 | 1.0 | 1.7 | 23.9 |
| Anthony Black (ORL) | 98% | 31.4<br><sub>33,-,31,38,33</sub> | 16.3<br><sub>23,-,10,18,26</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>8,-,7,8,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.7<br><sub>3,-,6,6,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.7<br><sub>1,-,1,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.0 | 0.7 | 2.4 | 25.6 |
| Tristan da Silva (ORL) | 100% | 31.4<br><sub>35,32,30,39,-</sub> | 14.3<br><sub>23,10,18,19,-</sub> |  | 4.7<br><sub>10,4,2,7,-</sub> |  | 2.2<br><sub>2,3,1,2,-</sub> |  | 2.4<br><sub>5,2,4,5,-</sub> |  | 1.0 | 0.4 | 1.5 | 21.1 |
| Jase Richardson (ORL) | 96% | 22.6<br><sub>26,29,26,30,15</sub> | 8.3<br><sub>4,9,10,2,6</sub> |  | 2.5<br><sub>1,1,2,4,1</sub> |  | 2.5<br><sub>3,5,3,4,1</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.9 | 0.3 | 1.0 | 13.4 |
| Alex Morales (ORL) | 80% | 18.1<br><sub>-,14,6,15,29</sub> | 4.3<br><sub>-,3,0,0,7</sub> |  | 2.9<br><sub>-,2,0,2,7</sub> |  | 1.1<br><sub>-,0,0,1,0</sub> |  | 0.3<br><sub>-,0,0,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 8.3 |
| Nikola Vucevic (ORL) | 98% | 13.2<br><sub>7,14,4,6,18</sub> | 5.7<br><sub>2,7,0,0,5</sub> |  | 3.7<br><sub>4,6,0,1,4</sub> |  | 1.4<br><sub>2,1,0,2,1</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.3 | 0.5 | 0.6 | 10.8 |
| Goga Bitadze (ORL) | 84% | 13.1<br><sub>5,-,8,7,15</sub> | 4.9<br><sub>0,-,4,4,2</sub> |  | 4.3<br><sub>1,-,5,5,2</sub> |  | 1.1<br><sub>0,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 1.0 | 0.7 | 10.3 |
| Jevon Carter (ORL) | 71% | 12.9<br><sub>-,18,3,15,4</sub> | 4.9<br><sub>-,5,0,9,0</sub> |  | 1.2<br><sub>-,1,0,1,0</sub> |  | 1.4<br><sub>-,4,0,0,0</sub> |  | 0.7<br><sub>-,1,0,3,0</sub> |  | 0.7 | 0.2 | 0.5 | 7.5 |
| Colin Castleton (ORL) | 38% | 6.4<br><sub>-,-,2,-,-</sub> | 2.4<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.7 |
| Ace Bailey (UTA) | 98% | 33.0<br><sub>24,35,29,32,35</sub> | 17.9<br><sub>5,15,12,7,23</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>6,5,6,2,7</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,1,0,3,2</sub> |  | 2.2<br><sub>1,1,0,1,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.1 | 2.3 | 25.5 |
| Darryn Peterson (UTA) | 98% | 32.7<br><sub>33,30,30,35,31</sub> | 18.4<br><sub>14,7,21,26,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,2,2,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>6,7,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,0,3,4,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.8 | 2.4 | 26.6 |
| Josh Green (UTA) | 91% | 27.3<br><sub>15,23,24,28,30</sub> | 5.7<br><sub>3,7,3,10,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>1,1,3,0,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,0,1,1,4</sub> |  | 0.7<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 1.0 | 9.9 |
| Jaxson Hayes (UTA) | 98% | 26.6<br><sub>22,21,28,29,17</sub> | 10.1<br><sub>9,2,8,18,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>5,7,6,6,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.4 | 17.9 |
| Josh Okogie (UTA) | 96% | 25.9<br><sub>19,26,24,17,21</sub> | 6.7<br><sub>9,3,12,0,6</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>3,6,4,1,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,1,0,0,4</sub> |  | 0.7<br><sub>1,1,2,0,0</sub> |  | 1.2 | 0.4 | 1.1 | 12.4 |
| Isaiah Collier (UTA) | 98% | 24.8<br><sub>12,3,13,16,24</sub> | 12.5<br><sub>7,0,4,6,17</sub> |  | 3.3<br><sub>2,1,3,4,5</sub> |  | 6.2<br><sub>2,0,3,2,5</sub> |  | 0.5<br><sub>0,0,0,0,4</sub> |  | 1.0 | 0.3 | 2.6 | 22.0 |
| Svi Mykhailiuk (UTA) | 96% | 21.9<br><sub>14,17,14,6,21</sub> | 9.2<br><sub>3,6,0,0,7</sub> |  | 2.4<br><sub>2,3,0,0,2</sub> |  | 1.7<br><sub>0,0,1,0,3</sub> |  | 1.4<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 13.2 |
| Brice Sensabaugh (UTA) | 98% | 21.9<br><sub>14,12,10,13,14</sub> | 14.3<br><sub>7,6,0,2,5</sub> |  | 3.3<br><sub>2,2,2,3,4</sub> |  | 2.0<br><sub>1,0,2,0,4</sub> |  | 2.0<br><sub>1,1,0,0,1</sub> |  | 0.7 | 0.2 | 1.8 | 19.6 |
| Mo Bamba (UTA) | 71% | 19.3<br><sub>18,15,-,17,17</sub> | 6.5<br><sub>8,7,-,3,7</sub> |  | 6.7<br><sub>8,10,-,3,7</sub> |  | 0.9<br><sub>0,1,-,1,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 1.5 | 1.0 | 14.1 |
| Kyle Filipowski (UTA) | 76% | 18.8<br><sub>8,-,1,15,15</sub> | 10.0<br><sub>1,-,0,9,7</sub> |  | 5.7<br><sub>2,-,0,6,4</sub> |  | 2.1<br><sub>0,-,0,1,1</sub> |  | 0.7<br><sub>0,-,0,1,0</sub> |  | 0.7 | 0.5 | 1.4 | 17.7 |
| Kobe Bufkin (UTA) | 23% | 15.0<br><sub>-,-,-,-,-</sub> | 6.5<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.9 | 10.1 |
| Tony Bradley (UTA) | 67% | 13.9<br><sub>7,-,1,2,14</sub> | 4.3<br><sub>2,-,0,0,4</sub> |  | 4.1<br><sub>3,-,1,1,5</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.1 |
| Harrison Ingram (UTA) | 8% | 8.5<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |

</details>


### GSW @ HOU
Out: Steven Adams (HOU), Clint Capela (HOU), Jimmy Butler III (GSW), Moses Moody (GSW), Gary Payton II (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 93% | 33.9<br><sub>37,33,32,39,26</sub> | 15.8<br><sub>17,20,9,15,25</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>8,3,6,7,2</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>8,2,3,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>2,3,2,4,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.2 | 1.7 | 24.6 |
| Yaxel Lendeborg | 98% | 33.2<br><sub>34,29,30,37,27</sub> | 19.9<br><sub>37,16,17,23,23</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>4,5,8,8,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>6,5,6,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>6,2,1,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.7 | 3.1 | 30.0 |
| Stephen Curry | 98% | 31.9<br><sub>-,33,28,36,21</sub> | 27.1<br><sub>-,34,29,41,25</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>-,6,1,6,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>-,7,4,6,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,5,6,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.4 | 2.9 | 35.5 |
| Draymond Green | 91% | 27.9<br><sub>-,17,27,34,21</sub> | 6.7<br><sub>-,4,2,2,2</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>-,4,5,6,3</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 5.8<br><sub>-,2,11,13,6</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.8<br><sub>-,0,0,0,0</sub> |  | 1.1 | 0.7 | 2.3 | 17.2 |
| De'Anthony Melton | 98% | 22.6<br><sub>28,28,17,17,26</sub> | 9.5<br><sub>21,2,5,4,16</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>6,7,6,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>3,2,2,1,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>6,0,0,1,4</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.3 | 1.5 | 14.8 |
| Georges Niang | 98% | 20.4<br><sub>21,22,22,25,19</sub> | 7.8<br><sub>3,13,13,11,9</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>2,3,3,1,2</sub> |  | 1.2<br><sub>1,1,2,3,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.5 | 0.2 | 1.0 | 11.6 |
| Gui Santos | 88% | 17.8<br><sub>9,-,-,12,21</sub> | 6.3<br><sub>4,-,-,3,3</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>3,-,-,1,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>1,-,-,0,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.8 | 0.2 | 1.2 | 11.2 |
| Al Horford | 98% | 17.1<br><sub>22,-,18,13,15</sub> | 5.2<br><sub>9,-,8,2,5</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>5,-,5,5,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>2,-,1,4,6</sub> |  | 0.7<br><sub>3,-,2,0,1</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.5 | 0.8 | 0.6 | 10.3 |
| Will Richard | 92% | 15.9<br><sub>22,28,16,12,-</sub> | 4.2<br><sub>3,6,10,4,-</sub> |  | 1.7<br><sub>0,5,0,2,-</sub> |  | 0.9<br><sub>3,0,2,1,-</sub> |  | 0.5<br><sub>1,2,2,0,-</sub> |  | 0.8 | 0.1 | 0.5 | 6.8 |
| Charles Bassey | 97% | 13.7<br><sub>20,23,14,11,18</sub> | 6.0<br><sub>6,19,8,8,12</sub> |  | 5.3<br><sub>10,8,7,4,10</sub> |  | 0.6<br><sub>2,1,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 11.9 |
| LJ Cryer | 66% | 11.8<br><sub>2,1,1,-,20</sub> | 5.2<br><sub>0,0,0,-,10</sub> |  | 1.0<br><sub>0,0,0,-,0</sub> |  | 0.9<br><sub>0,0,0,-,3</sub> |  | 0.8<br><sub>0,0,0,-,2</sub> |  | 0.3 | 0.1 | 0.6 | 7.1 |
| Graham Ike | 88% | 9.3<br><sub>6,7,1,-,12</sub> | 3.5<br><sub>2,0,0,-,4</sub> |  | 2.2<br><sub>2,0,1,-,5</sub> |  | 0.6<br><sub>0,0,0,-,2</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.3 |
| Malevy Leons | 52% | 7.6<br><sub>-,-,1,-,12</sub> | 2.0<br><sub>-,-,0,-,0</sub> |  | 1.4<br><sub>-,-,0,-,3</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 3.8 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.8<br><sub>33,36,35,39,38</sub> | 16.2<br><sub>30,14,11,15,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>9,10,4,9,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>5,0,2,2,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>6,4,2,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.9 | 1.4 | 25.6 |
| Kevin Durant | 98% | 36.3<br><sub>27,33,35,38,36</sub> | 23.1<br><sub>14,12,21,21,23</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>3,3,5,10,12</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.8<br><sub>4,3,2,3,8</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,0,2,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 3.4 | 34.3 |
| Alperen Sengun | 88% | 35.8<br><sub>33,38,39,32,35</sub> | 20.6<br><sub>16,26,17,15,20</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 9.9<br><sub>9,7,12,6,12</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>9,10,10,5,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 0.7<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 46% · u 54%</sub> | 1.4 | 1.2 | 3.0 | 37.3 |
| Amen Thompson | 98% | 35.5<br><sub>28,25,32,39,35</sub> | 16.0<br><sub>8,14,11,17,8</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 7.2<br><sub>3,3,8,7,9</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>1,3,1,0,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.7 | 0.7 | 2.2 | 27.4 |
| Fred VanVleet | 88% | 32.5<br><sub>-,27,30,31,30</sub> | 13.8<br><sub>-,8,18,16,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>-,2,3,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.2<br><sub>-,9,3,4,2</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>-,2,4,4,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.4 | 1.7 | 22.2 |
| Tari Eason | 98% | 23.2<br><sub>19,27,24,23,19</sub> | 9.4<br><sub>8,13,9,2,12</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>3,4,6,7,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,3,1,2,2</sub> |  | 1.1<br><sub>2,3,1,0,2</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 1.3 | 0.7 | 1.1 | 16.3 |
| Marcus Smart | 88% | 20.4<br><sub>36,20,18,20,17</sub> | 7.3<br><sub>24,8,4,5,5</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>5,4,1,2,2</sub> |  | 2.2<br><sub>3,4,1,0,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>7,2,1,1,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.2 | 0.3 | 1.3 | 11.7 |
| Reed Sheppard | 84% | 19.3<br><sub>-,17,21,13,17</sub> | 8.9<br><sub>-,8,14,6,8</sub> |  | 1.7<br><sub>-,1,2,0,0</sub> |  | 2.4<br><sub>-,1,2,0,0</sub> |  | 1.6<br><sub>-,2,3,2,2</sub> |  | 1.2 | 0.4 | 1.1 | 13.0 |
| Bogdan Bogdanovic | 96% | 11.1<br><sub>19,5,5,2,12</sub> | 4.2<br><sub>4,0,0,0,8</sub> |  | 1.4<br><sub>2,0,0,1,3</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 0.5<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.1 | 0.6 | 6.6 |
| Oscar Tshiebwe | 91% | 7.7<br><sub>4,7,2,3,-</sub> | 3.2<br><sub>2,4,2,2,-</sub> |  | 3.0<br><sub>1,1,0,0,-</sub> |  | 0.4<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.6 |
| Isaiah Crawford | 58% | 6.5<br><sub>19,2,-,-,1</sub> | 2.2<br><sub>8,0,-,-,0</sub> |  | 1.0<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>2,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 3.5 |
| Jae'Sean Tate | 52% | 6.0<br><sub>6,2,-,-,-</sub> | 2.1<br><sub>0,0,-,-,-</sub> |  | 1.4<br><sub>3,1,-,-,-</sub> |  | 0.4<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Bruce Thornton | 58% | 5.8<br><sub>6,2,-,-,1</sub> | 2.1<br><sub>5,2,-,-,0</sub> |  | 1.6<br><sub>1,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>1,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |

</details>


### OKC @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), Chet Holmgren (OKC), Ajay Mitchell (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.7<br><sub>39,35,30,29,29</sub> | 32.2<br><sub>43,42,28,30,26</sub> | 33.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>3,4,3,2,8</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.9<br><sub>8,8,4,9,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>4,5,3,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4 | 1.0 | 3.4 | 43.2 |
| Jared McCain | 98% | 30.4<br><sub>27,25,29,23,31</sub> | 15.4<br><sub>7,9,21,19,21</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>9,1,5,5,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,0,0,2,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>0,1,3,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 2.0 | 21.1 |
| Aday Mara | 98% | 26.7<br><sub>20,25,18,27,26</sub> | 11.0<br><sub>10,9,9,18,10</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 8.0<br><sub>9,5,7,8,10</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>0,2,0,3,2</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.5 | 1.9 | 1.7 | 20.6 |
| Isaiah Hartenstein | 98% | 26.5<br><sub>28,26,26,18,24</sub> | 9.9<br><sub>5,3,2,2,7</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 9.9<br><sub>14,12,6,14,9</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>4,4,7,6,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.6 | 23.5 |
| Bennett Stirtz | 98% | 25.6<br><sub>12,22,24,29,18</sub> | 9.4<br><sub>9,16,12,11,13</sub> |  | 2.1<br><sub>2,1,1,5,1</sub> |  | 1.7<br><sub>0,1,2,3,1</sub> |  | 1.4<br><sub>3,4,2,2,2</sub> |  | 0.8 | 0.2 | 1.0 | 13.2 |
| Kenrich Williams | 98% | 25.5<br><sub>31,29,19,23,19</sub> | 9.4<br><sub>12,13,4,9,3</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>3,4,6,4,2</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>1,2,3,2,0</sub> |  | 1.3<br><sub>2,3,1,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.0 | 16.4 |
| Alex Caruso | 98% | 23.8<br><sub>-,20,20,13,19</sub> | 9.1<br><sub>-,7,5,0,5</sub> |  | 3.6<br><sub>-,4,6,3,2</sub> |  | 2.7<br><sub>-,3,2,3,1</sub> |  | 1.2<br><sub>-,1,1,0,1</sub> |  | 1.5 | 0.5 | 1.1 | 15.4 |
| Micah Peavy | 88% | 23.6<br><sub>16,26,18,23,21</sub> | 6.4<br><sub>8,2,7,7,0</sub> |  | 4.1<br><sub>5,9,4,3,2</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 0.7<br><sub>2,0,1,1,0</sub> |  | 0.9 | 0.3 | 0.6 | 11.3 |
| Josh Dix | 76% | 19.4<br><sub>12,-,15,21,-</sub> | 4.5<br><sub>0,-,5,2,-</sub> |  | 1.9<br><sub>1,-,2,1,-</sub> |  | 0.9<br><sub>0,-,1,2,-</sub> |  | 0.5<br><sub>0,-,1,0,-</sub> |  | 0.6 | 0.3 | 0.6 | 7.3 |
| Nique Clifford | 91% | 18.3<br><sub>-,-,-,-,20</sub> | 6.7<br><sub>-,-,-,-,4</sub> |  | 2.8<br><sub>-,-,-,-,4</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.3 | 1.2 | 11.4 |
| Brooks Barnhizer | 72% | 11.7<br><sub>-,-,5,8,5</sub> | 3.0<br><sub>-,-,0,2,0</sub> |  | 2.5<br><sub>-,-,0,4,1</sub> |  | 0.8<br><sub>-,-,0,3,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 33.7<br><sub>35,35,39,24,34</sub> | 21.4<br><sub>28,21,22,15,24</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>3,7,9,4,6</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 6.9<br><sub>5,12,11,1,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 3.6 | 35.0 |
| Damian Lillard | 98% | 30.5<br><sub>30,33,37,20,24</sub> | 17.3<br><sub>20,25,22,12,25</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>6,3,0,0,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>6,5,4,7,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>1,2,4,2,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 2.3 | 25.8 |
| Toumani Camara | 98% | 30.0<br><sub>31,32,30,21,30</sub> | 11.9<br><sub>9,11,18,4,12</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>5,4,6,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.7<br><sub>1,2,1,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,1,4,0,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 1.4 | 17.9 |
| Jrue Holiday | 98% | 28.3<br><sub>31,28,31,20,25</sub> | 12.9<br><sub>17,15,12,11,11</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>8,4,1,0,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.5<br><sub>10,0,7,0,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>3,5,3,1,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.2 | 1.9 | 21.4 |
| Donovan Clingan | 98% | 26.3<br><sub>32,29,28,22,26</sub> | 10.8<br><sub>17,24,17,6,7</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 10.4<br><sub>18,11,11,5,13</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>3,1,1,0,3</sub> |  | 1.1<br><sub>1,1,3,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.5 | 1.4 | 1.4 | 23.1 |
| Scoot Henderson | 98% | 25.8<br><sub>26,22,23,24,23</sub> | 11.5<br><sub>8,9,2,13,11</sub> |  | 2.5<br><sub>2,2,2,2,1</sub> |  | 2.8<br><sub>2,1,0,1,4</sub> |  | 1.5<br><sub>2,1,0,0,3</sub> |  | 0.8 | 0.2 | 2.3 | 16.7 |
| Sidy Cissoko | 98% | 25.6<br><sub>22,21,22,16,33</sub> | 7.5<br><sub>8,7,7,4,17</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,4,2,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>0,4,3,1,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1<br><sub>2,1,2,0,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.4 | 1.1 | 13.1 |
| Robert Williams III | 98% | 17.8<br><sub>15,16,16,-,15</sub> | 6.5<br><sub>2,9,9,-,6</sub> |  | 6.5<br><sub>6,8,5,-,4</sub> |  | 1.2<br><sub>2,1,2,-,0</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.6 | 1.0 | 0.9 | 14.2 |
| Jayson Kent | 64% | 11.8<br><sub>-,-,-,12,-</sub> | 4.7<br><sub>-,-,-,4,-</sub> |  | 1.7<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.0 |
| Yang Hansen | 80% | 9.9<br><sub>-,2,3,26,5</sub> | 3.9<br><sub>-,0,2,12,0</sub> |  | 2.6<br><sub>-,0,0,10,1</sub> |  | 0.5<br><sub>-,0,0,1,0</sub> |  | 0.3<br><sub>-,0,0,1,0</sub> |  | 0.2 | 0.3 | 0.7 | 6.9 |
| Micah Potter | 67% | 9.6<br><sub>-,2,-,14,5</sub> | 4.0<br><sub>-,4,-,7,0</sub> |  | 2.5<br><sub>-,1,-,3,3</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4<br><sub>-,1,-,1,0</sub> |  | 0.2 | 0.2 | 0.5 | 7.0 |
| Branden Carlson | 64% | 9.5<br><sub>-,3,-,12,8</sub> | 2.8<br><sub>-,2,-,4,2</sub> |  | 2.3<br><sub>-,0,-,2,5</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.5 | 5.6 |
| John Tonje | 52% | 6.8<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-11/`._
