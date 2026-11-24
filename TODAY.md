# NBA model · Mon 23 Nov 2026 (US date)

Updated **Tue 24 Nov, 11:33 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-23/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic PA over 59.5 (60+) | UTA @ LAL | draftkings | 9.90 | 8.87 | 5.10 | 19.6% | 9.4% | 11.3% | +11.7% | +93.9% | 0.3% |
| Scottie Barnes AST over 9.5 (10+) | MIL @ TOR | draftkings | 11.40 | 10.22 | 5.90 | 16.9% | 8.2% | 9.8% | +11.5% | +93.1% | 0.3% |
| Andrew Nembhard AST over 13.5 (14+) | OKC @ IND | draftkings | 23.00 | 20.83 | 12.26 | 8.2% | 4.1% | 4.8% | +10.5% | +87.6% | 0.1% |
| Amen Thompson AST over 5.5 (6+) | LAC @ HOU | draftkings | 7.40 | 6.71 | 3.96 | 25.2% | 12.6% | 14.9% | +10.4% | +86.9% | 0.4% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ IND | draftkings | 13.20 | 11.99 | 7.11 | 14.1% | 7.1% | 8.3% | +10.1% | +85.6% | 0.2% |
| Amen Thompson AST over 7.5 (8+) | LAC @ HOU | draftkings | 24.00 | 21.88 | 13.09 | 7.6% | 3.9% | 4.6% | +9.7% | +83.3% | 0.1% |
| Quenton Jackson AST over 5.5 (6+) | OKC @ IND | draftkings | 10.10 | 9.22 | 5.53 | 18.1% | 9.2% | 10.8% | +9.6% | +82.5% | 0.3% |
| Andrew Nembhard AST over 11.5 (12+) | OKC @ IND | draftkings | 10.00 | 9.16 | 5.54 | 18.0% | 9.3% | 10.9% | +9.2% | +80.4% | 0.3% |
| Scottie Barnes PA over 44.5 (45+) | MIL @ TOR | draftkings | 16.00 | 14.66 | 8.89 | 11.2% | 5.8% | 6.8% | +9.1% | +79.9% | 0.1% |
| Scottie Barnes AST over 11.5 (12+) | MIL @ TOR | draftkings | 27.00 | 24.88 | 15.23 | 6.6% | 3.5% | 4.0% | +8.6% | +77.3% | 0.1% |
| Derik Queen REB over 11.5 (12+) | PHX @ NOP | draftkings | 14.40 | 13.42 | 8.47 | 11.8% | 6.5% | 7.4% | +7.3% | +69.9% | 0.1% |
| Jakob Poeltl AST over 3.5 (4+) | MIL @ TOR | draftkings | 6.97 | 6.50 | 4.11 | 24.3% | 13.4% | 15.4% | +7.3% | +69.7% | 0.3% |
| Scottie Barnes PRA over 54.5 (55+) | MIL @ TOR | draftkings | 17.60 | 16.53 | 10.61 | 9.4% | 5.3% | 6.0% | +6.6% | +65.9% | 0.1% |
| Andrew Nembhard PRA over 39.5 (40+) | OKC @ IND | draftkings | 14.00 | 13.18 | 8.51 | 11.8% | 6.7% | 7.6% | +6.3% | +64.5% | 0.1% |
| Derik Queen AST over 5.5 (6+) | PHX @ NOP | draftkings | 17.40 | 16.39 | 10.62 | 9.4% | 5.4% | 6.1% | +6.2% | +63.9% | 0.1% |
| Derik Queen REB over 9.5 (10+) | PHX @ NOP | draftkings | 6.48 | 6.13 | 4.03 | 24.8% | 14.4% | 16.3% | +5.7% | +61.0% | 0.3% |
| Kevin Durant AST over 7.5 (8+) | LAC @ HOU | draftkings | 12.00 | 11.38 | 7.51 | 13.3% | 7.8% | 8.8% | +5.5% | +59.7% | 0.1% |
| Jake LaRavia AST over 3.5 (4+) | UTA @ LAL | draftkings | 9.60 | 9.12 | 6.05 | 16.5% | 9.7% | 11.0% | +5.2% | +58.6% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Murray-Boyles PTS under 11.5 | MIL @ TOR | pointsbetau | 2.05 | 1.95 | 1.61 | 62.1% | 48.9% | 51.3% | +5.2% | +27.2% | 1.2% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro PTS under 20.5 | MIL @ TOR | tab | 1.95 | 1.83 | 1.43 | 69.9% | 51.3% | 54.7% | +6.7% | +36.5% | 1.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ IND | Tue 24 Nov 11:30 | 116.7–112.4 | OKC 62% | 1.61 / 2.64 | IND +4.5 | 229.5 | IND +4.5 covers 50%; o226.5 55% |
| MIL @ TOR | Tue 24 Nov 11:30 | 107.4–115.7 | MIL 28% | 3.63 / 1.38 | TOR -8.5 | 223.5 | TOR -10.5 covers 44%; o222.5 51% |
| BKN @ MIN | Tue 24 Nov 11:30 | 104.8–115.4 | BKN 23% | 4.42 / 1.29 | MIN -10.5 | 219.5 | MIN -10.5 covers 51%; o222.5 44% |
| CLE @ CHI | Tue 24 Nov 12:00 | 124.3–118.3 | CLE 66% | 1.52 / 2.93 | CHI +6.5 | 242.5 | CHI +8.5 covers 57%; o240.5 54% |
| PHX @ NOP | Tue 24 Nov 12:00 | 121.4–115.5 | PHX 66% | 1.51 / 2.95 | NOP +5.5 | 236.5 | NOP +3.5 covers 43%; o232.5 59% |
| LAC @ HOU | Tue 24 Nov 12:30 | 109.0–118.0 | LAC 26% | 3.80 / 1.36 | HOU -8.5 | 226.5 | HOU -13.5 covers 38%; o223.5 57% |
| UTA @ LAL | Tue 24 Nov 14:00 | 108.5–123.5 | UTA 14% | 7.17 / 1.16 | LAL -15.5 | 232.5 | LAL -13.5 covers 54%; o225.5 64% |
| SAS @ SAC | Tue 24 Nov 14:00 | 116.9–108.2 | SAS 73% | 1.37 / 3.70 | SAC +8.5 | 225.5 | SAC +12.5 covers 61%; o224.5 51% |

### OKC @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Aaron Nesmith (IND), Ben Sheppard (IND), Alex Caruso (OKC), Chet Holmgren (OKC), Aday Mara (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quenton Jackson PTS under 9.5 | OKC @ IND | pointsbetau | 2.05 | 1.98 | 1.81 | 55.3% | 49.5% | 50.6% | +3.7% | +13.3% | 0.9% |
| Kenrich Williams PTS under 9.5 | OKC @ IND | betright | 2.05 | 2.01 | 1.86 | 53.7% | 49.0% | 49.8% | +2.1% | +10.0% | 0.5% |
| Andrew Nembhard PTS over 14.5 (15+) | OKC @ IND | betright | 1.96 | 1.93 | 1.67 | 60.0% | 49.9% | 51.7% | +1.5% | +17.8% | 0.4% |
| Quenton Jackson PTS over 9.5 (10+) | OKC @ IND | draftkings | 2.04 | 2.03 | 2.24 | 44.7% | 50.4% | 49.4% | +0.7% | -8.8% | 0.2% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 34.7<br><sub>39,30,36,37,-</sub> | 34.5<br><sub>40,37,34,40,-</sub> | 32.5 · 32.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>4,2,5,3,-</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.4<br><sub>5,2,3,8,-</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,4,1,4,-</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.7 | 2.6 | 45.4 |
| Jared McCain | 100% | 31.3<br><sub>31,30,33,30,29</sub> | 17.5<br><sub>23,12,18,18,20</sub> | 16.5 · 15.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,3,3,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,1,1,0,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.7<br><sub>7,1,4,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 1.6 | 23.5 |
| Ajay Mitchell | 100% | 30.9<br><sub>-,27,34,31,22</sub> | 18.6<br><sub>-,14,13,8,17</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>-,3,6,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>-,5,6,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>-,1,0,1,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.5 | 0.3 | 1.8 | 27.2 |
| Isaiah Hartenstein | 100% | 28.1<br><sub>30,18,27,28,23</sub> | 9.3<br><sub>21,3,6,5,2</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 12.0<br><sub>16,11,17,8,8</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>6,2,6,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.7 | 25.7 |
| Micah Peavy | 100% | 27.8<br><sub>-,13,-,9,31</sub> | 7.4<br><sub>-,5,-,2,9</sub> |  | 5.5<br><sub>-,3,-,2,6</sub> |  | 0.8<br><sub>-,1,-,0,1</sub> |  | 0.9<br><sub>-,1,-,0,1</sub> |  | 1.2 | 0.3 | 0.9 | 13.8 |
| Kenrich Williams | 98% | 27.2<br><sub>35,19,23,28,26</sub> | 9.7<br><sub>8,10,10,6,12</sub> | 8.5 · 9.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>8,1,5,2,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>4,2,1,4,2</sub> |  | 1.3<br><sub>0,2,0,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 0.9 | 17.2 |
| Bennett Stirtz | 98% | 27.0<br><sub>12,17,17,25,32</sub> | 9.5<br><sub>5,0,6,18,21</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,1,0,2,3</sub> |  | 2.1<br><sub>0,2,2,2,5</sub> |  | 1.8<br><sub>1,0,2,4,5</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 0.9 | 13.9 |
| Josh Dix | 64% | 24.6<br><sub>17,-,-,-,32</sub> | 5.9<br><sub>0,-,-,-,13</sub> |  | 3.1<br><sub>4,-,-,-,5</sub> |  | 1.6<br><sub>3,-,-,-,4</sub> |  | 0.8<br><sub>0,-,-,-,3</sub> |  | 0.9 | 0.2 | 0.6 | 10.6 |
| Nique Clifford | 97% | 23.0<br><sub>12,24,13,15,26</sub> | 7.7<br><sub>0,9,7,4,11</sub> |  | 3.6<br><sub>0,3,0,5,3</sub> |  | 1.8<br><sub>0,0,0,1,0</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.0 | 13.2 |
| Brooks Barnhizer | 52% | 15.0<br><sub>-,4,-,-,19</sub> | 3.8<br><sub>-,0,-,-,8</sub> |  | 3.5<br><sub>-,0,-,-,4</sub> |  | 1.2<br><sub>-,0,-,-,2</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 8.5 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 100% | 33.8<br><sub>34,-,-,26,32</sub> | 17.2<br><sub>12,-,-,12,16</sub> | 14.5 · 14.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>4,-,-,3,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 8.4<br><sub>6,-,-,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>1,-,-,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 2.9 | 28.7 |
| Pascal Siakam | 100% | 33.7<br><sub>32,34,33,30,33</sub> | 21.7<br><sub>19,31,24,21,25</sub> | 22.5 · 21.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>3,2,4,7,6</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 4.1<br><sub>2,2,3,2,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,0,2,2,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.3 | 2.3 | 32.5 |
| Ivica Zubac | 100% | 28.3<br><sub>26,22,24,27,31</sub> | 12.3<br><sub>12,8,4,21,10</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 10.1<br><sub>13,5,3,10,14</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,2,4,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 1.6 | 24.4 |
| Kelly Oubre Jr. | 100% | 28.3<br><sub>30,29,23,23,27</sub> | 12.6<br><sub>16,16,17,17,15</sub> | 13.5 · 12.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,4,4,6,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>0,2,0,0,0</sub> |  | 1.4<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.6 | 1.3 | 18.5 |
| Braden Smith | 100% | 22.9<br><sub>-,-,18,11,18</sub> | 7.6<br><sub>-,-,8,5,6</sub> |  | 2.4<br><sub>-,-,5,3,1</sub> |  | 4.4<br><sub>-,-,3,5,4</sub> |  | 0.7<br><sub>-,-,2,1,0</sub> |  | 1.1 | 0.4 | 1.3 | 14.4 |
| Quenton Jackson | 99% | 22.6<br><sub>20,30,22,18,17</sub> | 9.6<br><sub>3,15,15,3,2</sub> | 8.5 · 9.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,6,2,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>4,8,3,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>1,1,2,1,0</sub> |  | 1.1 | 0.2 | 1.5 | 16.3 |
| Obi Toppin | 91% | 21.2<br><sub>16,14,17,26,22</sub> | 11.7<br><sub>9,5,6,17,9</sub> | 10.5 · 11.5<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>3,2,1,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>1,1,1,2,1</sub> |  | 1.6<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.5 | 0.3 | 1.1 | 18.1 |
| Jarace Walker | 88% | 15.6<br><sub>-,14,17,11,1</sub> | 6.6<br><sub>-,2,1,8,0</sub> |  | 3.5<br><sub>-,5,3,1,0</sub> |  | 1.6<br><sub>-,2,1,3,0</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 0.9 | 11.7 |
| Jalen Slawson | 91% | 14.4<br><sub>10,14,12,14,14</sub> | 4.6<br><sub>1,8,5,4,7</sub> |  | 3.1<br><sub>4,5,4,2,3</sub> |  | 1.4<br><sub>0,2,2,2,0</sub> |  | 0.4<br><sub>0,1,1,0,0</sub> |  | 0.7 | 0.7 | 0.7 | 9.1 |
| Kobe Brown | 86% | 13.3<br><sub>-,3,2,-,-</sub> | 4.9<br><sub>-,0,0,-,-</sub> |  | 2.5<br><sub>-,0,0,-,-</sub> |  | 1.2<br><sub>-,0,0,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.5 |
| Larry Nance Jr. | 98% | 12.7<br><sub>14,7,9,11,11</sub> | 4.4<br><sub>2,4,3,7,5</sub> |  | 2.6<br><sub>2,2,1,2,3</sub> |  | 0.8<br><sub>1,2,0,0,0</sub> |  | 0.5<br><sub>0,1,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 7.7 |
| Jay Huff | 91% | 12.7<br><sub>8,18,15,1,1</sub> | 5.6<br><sub>8,11,5,0,2</sub> |  | 2.4<br><sub>1,0,3,0,0</sub> |  | 0.9<br><sub>0,2,0,0,0</sub> |  | 0.6<br><sub>2,3,0,0,0</sub> |  | 0.2 | 0.8 | 0.6 | 8.9 |

</details>


### MIL @ TOR
Out: RJ Barrett (TOR), Kawhi Leonard (TOR), Kam Jones (MIL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Rollins PTS under 11.5 | MIL @ TOR | tab | 2.00 | 1.97 | 1.82 | 55.0% | 49.8% | 50.7% | +1.5% | +10.0% | 0.4% |
| Allen Graves PTS under 8.5 | MIL @ TOR | pointsbetau | 2.05 | 2.04 | 2.05 | 48.8% | 49.0% | 48.9% | +0.4% | +0.1% | 0.1% |
| Jamison Battle PTS over 7.5 (8+) | MIL @ TOR | tab | 1.85 | 1.85 | 1.56 | 64.2% | 51.9% | 54.1% | +0.0% | +18.6% | 0.0% |

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 100% | 29.2<br><sub>34,20,24,31,40</sub> | 17.4<br><sub>18,5,8,19,50</sub> | 19.5 · 20.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,5,2,4,11</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.9<br><sub>2,3,4,3,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,0,0,4,7</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 2.3 | 25.4 |
| Jaime Jaquez Jr. | 100% | 25.3<br><sub>28,30,23,22,25</sub> | 12.8<br><sub>22,6,10,9,9</sub> | 12.5 · 11.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>6,5,2,1,0</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>4,4,5,2,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>5,2,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.2 | 2.0 | 19.9 |
| Kyle Kuzma | 100% | 25.2<br><sub>31,22,30,-,33</sub> | 11.2<br><sub>14,14,26,-,12</sub> | 10.5 · 11.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>4,6,5,-,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,2,1,-,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1<br><sub>1,3,2,-,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.3 | 1.9 | 17.6 |
| Ryan Rollins | 100% | 24.1<br><sub>29,-,-,21,28</sub> | 11.6<br><sub>8,-,-,15,8</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>10,-,-,3,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>2,-,-,6,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>0,-,-,1,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.3 | 2.3 | 19.1 |
| Myles Turner | 100% | 23.5<br><sub>31,23,21,-,26</sub> | 8.1<br><sub>14,8,4,-,5</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>11,7,5,-,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>3,1,4,-,5</sub> |  | 1.0<br><sub>4,1,0,-,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 1.5 | 1.2 | 14.7 |
| Brayden Burries | 98% | 21.3<br><sub>19,29,25,28,26</sub> | 9.5<br><sub>3,13,20,14,26</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>4,8,7,3,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>3,4,1,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>1,2,3,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.2 | 1.4 | 16.2 |
| Kel'el Ware | 98% | 16.5<br><sub>17,25,17,26,22</sub> | 7.1<br><sub>10,8,11,11,6</sub> | 9.5 · 9.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>6,11,3,5,8</sub> |  | 0.9<br><sub>1,2,1,0,3</sub> |  | 0.5<br><sub>2,1,1,2,0</sub> |  | 0.5 | 0.8 | 1.3 | 13.2 |
| Nate Ament | 97% | 14.5<br><sub>22,17,17,35,14</sub> | 6.0<br><sub>9,5,7,18,2</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,2,4,9,1</sub> |  | 0.6<br><sub>1,1,1,0,0</sub> |  | 0.5<br><sub>2,1,0,2,0</sub> |  | 0.4 | 0.2 | 0.8 | 8.9 |
| Cormac Ryan | 52% | 14.1<br><sub>-,-,-,-,-</sub> | 6.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 9.5 |
| Kasparas Jakucionis | 88% | 13.7<br><sub>-,26,26,22,10</sub> | 6.2<br><sub>-,25,20,18,2</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>-,5,3,3,3</sub> |  | 2.3<br><sub>-,5,5,2,3</sub> |  | 0.6<br><sub>-,4,3,3,0</sub> |  | 0.5 | 0.1 | 1.2 | 10.2 |
| Pete Nance | 96% | 12.9<br><sub>-,-,-,28,-</sub> | 4.1<br><sub>-,-,-,7,-</sub> |  | 2.0<br><sub>-,-,-,3,-</sub> |  | 0.9<br><sub>-,-,-,3,-</sub> |  | 0.4<br><sub>-,-,-,1,-</sub> |  | 0.2 | 0.2 | 0.5 | 7.0 |
| AJ Green | 84% | 11.9<br><sub>8,6,14,-,12</sub> | 4.2<br><sub>0,0,11,-,9</sub> |  | 1.1<br><sub>0,0,0,-,0</sub> |  | 0.8<br><sub>2,0,1,-,0</sub> |  | 0.7<br><sub>0,0,3,-,3</sub> |  | 0.2 | 0.1 | 0.5 | 6.1 |
| Gary Trent Jr. | 64% | 8.6<br><sub>16,30,16,7,-</sub> | 3.8<br><sub>1,18,1,0,-</sub> |  | 0.6<br><sub>0,2,1,1,-</sub> |  | 0.4<br><sub>0,1,0,0,-</sub> |  | 0.4<br><sub>0,4,0,0,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.8 |
| Jericho Sims | 64% | 8.3<br><sub>-,11,18,10,-</sub> | 2.0<br><sub>-,4,4,0,-</sub> |  | 2.0<br><sub>-,2,6,0,-</sub> |  | 0.6<br><sub>-,0,2,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.7 |
| Caris LeVert | 52% | 8.2<br><sub>-,-,8,11,5</sub> | 3.2<br><sub>-,-,8,3,0</sub> |  | 1.2<br><sub>-,-,3,3,1</sub> |  | 1.0<br><sub>-,-,2,1,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 5.4 |
| Ousmane Dieng | 84% | 7.9<br><sub>5,-,-,-,-</sub> | 2.9<br><sub>0,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.6 | 5.0 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 100% | 34.5<br><sub>-,36,34,-,37</sub> | 24.6<br><sub>-,30,20,-,29</sub> | 23.5 · 23.5<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>-,9,4,-,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.7<br><sub>-,4,2,-,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>-,4,1,-,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.6 | 1.1 | 3.0 | 38.7 |
| Ja'Kobe Walter | 100% | 32.1<br><sub>32,36,33,38,33</sub> | 13.3<br><sub>6,7,25,18,8</sub> | 12.5 · 13.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>5,2,1,7,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,1,2,6,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>1,1,7,3,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.3 | 1.0 | 19.6 |
| Immanuel Quickley | 100% | 31.9<br><sub>28,38,34,34,33</sub> | 18.7<br><sub>26,17,14,24,18</sub> | 18.5 · 18.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,6,1,3,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>6,6,7,5,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,3,2,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.1 | 1.6 | 29.0 |
| Jakob Poeltl | 100% | 26.5<br><sub>25,17,18,29,32</sub> | 11.3<br><sub>9,11,3,8,10</sub> | 10.5 · 9.5<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>5,5,6,9,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,1,1,5,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.0 | 1.3 | 22.0 |
| Allen Graves | 100% | 26.4<br><sub>13,16,13,31,33</sub> | 9.3<br><sub>0,2,3,9,20</sub> | 9.5 · 8.5<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>2,5,2,4,10</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,3,1,0,1</sub> |  | 1.2<br><sub>0,0,1,1,2</sub> |  | 0.9 | 0.6 | 0.9 | 15.7 |
| Collin Murray-Boyles | 76% | 23.2<br><sub>32,40,33,5,-</sub> | 10.6<br><sub>14,6,8,1,-</sub> | 10.5 · 11.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>0,13,1,2,-</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>4,2,3,1,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.4<br><sub>1,0,0,0,-</sub> | 0.5<br><sub>o 28% · u 72%</sub> | 1.0 | 1.2 | 1.4 | 18.1 |
| Jamal Shead | 99% | 22.6<br><sub>22,26,20,24,15</sub> | 8.1<br><sub>5,19,7,15,0</sub> | 7.5 · 7.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>1,2,0,1,1</sub> |  | 6.0<br><sub>5,4,6,6,4</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>1,3,1,1,0</sub> |  | 1.0 | 0.2 | 1.5 | 16.1 |
| Jamison Battle | 98% | 21.0<br><sub>25,8,7,33,20</sub> | 10.0<br><sub>13,0,0,19,10</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>1,3,1,5,5</sub> |  | 0.9<br><sub>1,0,0,0,0</sub> |  | 1.9<br><sub>3,0,0,5,2</sub> |  | 0.4 | 0.1 | 0.6 | 13.7 |
| Trayce Jackson-Davis | 63% | 14.3<br><sub>-,-,-,17,16</sub> | 5.7<br><sub>-,-,-,3,8</sub> |  | 4.8<br><sub>-,-,-,7,2</sub> |  | 1.1<br><sub>-,-,-,1,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.9 | 0.8 | 0.7 | 11.6 |
| Alijah Martin | 96% | 14.3<br><sub>18,12,8,17,16</sub> | 5.4<br><sub>7,2,0,2,0</sub> |  | 2.2<br><sub>4,3,2,2,2</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.6 | 0.2 | 0.8 | 8.6 |
| Malachi Smith | 96% | 8.7<br><sub>2,-,-,8,5</sub> | 3.0<br><sub>0,-,-,0,2</sub> |  | 1.3<br><sub>0,-,-,1,0</sub> |  | 1.3<br><sub>0,-,-,3,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.6 |
| Kyle Anderson | 52% | 8.6<br><sub>5,-,-,4,-</sub> | 2.6<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.3 | 0.4 | 5.8 |
| Kevin McCullar Jr. | 16% | 7.6<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.0 |
| Jaden Bradley | 48% | 6.7<br><sub>2,-,-,-,-</sub> | 2.4<br><sub>1,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |

</details>


### BKN @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Chaney Johnson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Nolan Traore (BKN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ayo Dosunmu PTS under 17.5 | BKN @ MIN | tab | 1.95 | 1.93 | 1.73 | 57.9% | 50.4% | 51.8% | +1.1% | +13.0% | 0.3% |
| Michael Porter Jr. PTS under 19.5 | BKN @ MIN | pointsbetau | 1.95 | 1.94 | 1.67 | 59.7% | 49.8% | 51.5% | +0.7% | +16.6% | 0.2% |
| Egor Demin PTS over 9.5 (10+) | BKN @ MIN | draftkings | 2.02 | 2.01 | 2.05 | 48.8% | 50.0% | 49.8% | +0.6% | -1.5% | 0.1% |
| Mikel Brown Jr. PTS under 14.5 | BKN @ MIN | pointsbetau | 1.90 | 1.89 | 1.59 | 62.7% | 50.6% | 52.8% | +0.4% | +19.2% | 0.1% |
| Jaden McDaniels PTS under 17.5 | BKN @ MIN | pointsbetau | 2.00 | 1.99 | 1.81 | 55.2% | 49.0% | 50.1% | +0.3% | +10.3% | 0.1% |
| Jonathan Kuminga PTS under 14.5 | BKN @ MIN | tab | 1.95 | 1.95 | 1.92 | 52.0% | 51.2% | 51.3% | +0.2% | +1.5% | 0.1% |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 100% | 33.8<br><sub>29,31,34,27,39</sub> | 19.6<br><sub>17,22,33,17,27</sub> | 20.5 · 20.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>4,4,6,0,9</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.4<br><sub>5,5,1,4,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,3,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.3 | 3.5 | 30.1 |
| Michael Porter Jr. | 100% | 33.7<br><sub>28,-,40,27,34</sub> | 18.6<br><sub>22,-,25,5,16</sub> | 19.5 · 19.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>6,-,6,3,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>3,-,2,1,5</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.6<br><sub>4,-,2,1,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.4 | 2.4 | 27.5 |
| Mikel Brown Jr. | 100% | 28.5<br><sub>-,20,18,27,24</sub> | 13.3<br><sub>-,6,3,15,18</sub> | 14.5 · 14.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>-,1,1,1,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 4.0<br><sub>-,2,5,4,0</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>-,2,1,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 2.4 | 19.9 |
| Egor Demin | 98% | 25.2<br><sub>23,27,26,31,21</sub> | 10.1<br><sub>22,11,9,22,6</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,1,3,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>1,2,4,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>4,3,2,3,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 1.8 | 16.1 |
| Day'Ron Sharpe | 100% | 25.2<br><sub>19,28,25,22,26</sub> | 9.7<br><sub>15,16,6,6,17</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 7.9<br><sub>4,11,9,5,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>5,5,5,1,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.3<br><sub>2,0,0,0,0</sub> |  | 1.2 | 1.0 | 2.0 | 21.4 |
| Danny Wolf | 100% | 24.6<br><sub>29,28,11,23,26</sub> | 9.5<br><sub>10,14,3,6,20</sub> | 8.5 · 8.5<br><sub>o 54% · u 46%</sub> | 5.8<br><sub>11,6,2,6,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>4,1,1,2,2</sub> |  | 1.2<br><sub>1,4,1,1,4</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.6 | 1.6 | 17.5 |
| Noah Clowney | 99% | 22.8<br><sub>19,35,24,19,22</sub> | 7.9<br><sub>16,15,9,7,0</sub> |  | 3.9<br><sub>3,7,3,3,2</sub> |  | 1.1<br><sub>0,3,3,1,2</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 0.7 | 0.6 | 1.1 | 12.9 |
| Moritz Wagner | 98% | 18.4<br><sub>19,18,10,20,22</sub> | 8.9<br><sub>16,10,4,11,3</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,6,5,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>4,4,1,3,2</sub> |  | 0.7<br><sub>2,2,0,2,1</sub> |  | 0.7 | 0.3 | 1.2 | 14.4 |
| Keon Ellis | 91% | 16.6<br><sub>26,7,20,6,8</sub> | 3.7<br><sub>11,0,8,3,0</sub> |  | 1.7<br><sub>4,0,2,1,1</sub> |  | 1.1<br><sub>3,1,0,0,1</sub> |  | 0.4<br><sub>2,0,2,1,0</sub> |  | 0.9 | 0.5 | 0.5 | 6.5 |
| Terance Mann | 58% | 13.2<br><sub>18,9,-,5,-</sub> | 3.1<br><sub>6,2,-,0,-</sub> |  | 1.6<br><sub>1,1,-,1,-</sub> |  | 1.3<br><sub>3,1,-,0,-</sub> |  | 0.2<br><sub>2,0,-,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 6.0 |
| Josh Minott | 52% | 9.1<br><sub>7,2,-,4,-</sub> | 4.2<br><sub>0,0,-,0,-</sub> |  | 1.6<br><sub>2,0,-,0,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.3 | 0.5 | 6.3 |
| Grant Nelson | 67% | 8.1 | 2.9 |  | 1.7 |  | 0.8 |  | 0.0 |  | 0.3 | 0.7 | 0.5 | 5.4 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 33.3<br><sub>37,31,37,39,36</sub> | 17.6<br><sub>18,13,22,17,25</sub> | 17.5 · 18.5<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>5,6,5,3,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>6,3,4,1,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>2,0,2,4,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 1.0 | 1.9 | 26.4 |
| Ayo Dosunmu | 100% | 31.7<br><sub>33,30,39,32,34</sub> | 17.1<br><sub>24,8,30,6,19</sub> | 17.5 · 17.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>5,5,4,4,2</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>0,2,5,4,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>0,2,7,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.4 | 2.3 | 25.2 |
| Jonathan Kuminga | 100% | 31.3<br><sub>35,29,-,35,37</sub> | 15.0<br><sub>11,13,-,23,16</sub> | 14.5 · 14.5<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>3,9,-,3,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>3,1,-,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,1,-,2,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.7 | 1.8 | 23.2 |
| LaMelo Ball | 100% | 29.4<br><sub>30,24,31,35,32</sub> | 20.1<br><sub>19,6,18,15,12</sub> | 18.5 · 18.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>8,5,9,8,5</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 6.3<br><sub>6,0,2,8,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 3.5<br><sub>4,2,3,3,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.5 | 0.2 | 3.0 | 31.1 |
| Rudy Gobert | 100% | 29.3<br><sub>27,32,22,35,32</sub> | 9.2<br><sub>1,18,0,9,7</sub> | 8.5 · 9.5<br><sub>o 47% · u 53%</sub> | 10.5<br><sub>10,15,4,7,11</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,3,2,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.4 | 21.4 |
| Terrence Shannon Jr. | 98% | 23.6<br><sub>22,35,24,21,26</sub> | 13.0<br><sub>14,34,12,10,15</sub> | 12.5 · 13.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>6,3,1,4,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>0,6,4,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,3,1,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.1 | 1.4 | 18.6 |
| Trey Lyles | 99% | 18.0<br><sub>19,19,31,16,12</sub> | 5.9<br><sub>5,9,8,8,3</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,3,7,6,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>2,1,4,1,1</sub> |  | 0.8<br><sub>0,2,2,2,1</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.5 | 0.3 | 0.6 | 10.8 |
| Joan Beringer | 98% | 16.9<br><sub>13,16,26,13,16</sub> | 6.5<br><sub>2,0,3,5,0</sub> |  | 5.7<br><sub>5,4,13,3,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 0.8 | 12.7 |
| Bones Hyland | 98% | 16.3<br><sub>21,13,17,15,16</sub> | 9.6<br><sub>12,5,13,6,7</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>1,1,2,1,0</sub> |  | 3.0<br><sub>2,5,1,1,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>3,0,3,1,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 1.0 | 14.3 |
| Cody Williams | 52% | 7.2<br><sub>-,4,13,-,-</sub> | 0.2<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,1,1,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 1.5 |
| Zyon Pullin | 38% | 6.2<br><sub>-,4,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.1 |
| Isaiah Evans | 38% | 5.8<br><sub>-,4,-,-,-</sub> | 4.5<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |
| Johni Broome | 38% | 5.2<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.7 |

</details>


### CLE @ CHI
Out: Norman Powell (CHI), Caleb Wilson (CHI), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Smith PTS over 13.5 (14+) | CLE @ CHI | pointsbetau | 2.00 | 1.98 | 1.72 | 58.0% | 48.7% | 50.4% | +0.8% | +16.1% | 0.2% |
| Donovan Mitchell PTS under 26.5 | CLE @ CHI | betright | 1.95 | 1.94 | 1.62 | 61.9% | 49.3% | 51.6% | +0.7% | +20.8% | 0.2% |
| Isaac Okoro PTS under 10.5 | CLE @ CHI | tab | 1.95 | 1.95 | 1.82 | 55.1% | 50.6% | 51.4% | +0.3% | +7.5% | 0.1% |
| Jalen Smith PTS over 12.5 (13+) | CLE @ CHI | tab | 1.85 | 1.85 | 1.55 | 64.4% | 51.9% | 54.2% | +0.1% | +18.9% | 0.0% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 100% | 31.7<br><sub>35,-,34,36,40</sub> | 19.1<br><sub>20,-,9,14,51</sub> | 18.5 · 17.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>6,-,4,6,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>8,-,10,9,6</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,-,2,3,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.4 | 2.6 | 30.0 |
| Donovan Mitchell | 100% | 30.7<br><sub>33,-,36,35,29</sub> | 24.7<br><sub>25,-,39,34,20</sub> | 26.5 · 26.5<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,-,4,4,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>7,-,4,3,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>5,-,2,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4 | 0.3 | 2.3 | 33.9 |
| Jarrett Allen | 100% | 26.0<br><sub>32,-,30,30,31</sub> | 13.6<br><sub>9,-,13,19,6</sub> | 14.5 · 14.5<br><sub>o 47% · u 53%</sub> | 8.6<br><sub>8,-,14,9,8</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,-,3,4,4</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 1.0 | 1.1 | 1.3 | 23.9 |
| Peyton Watson | 100% | 25.4<br><sub>30,-,22,-,29</sub> | 11.9<br><sub>4,-,14,-,15</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>4,-,4,-,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,-,0,-,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2<br><sub>0,-,2,-,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 1.2 | 1.6 | 18.2 |
| Sam Merrill | 100% | 24.3<br><sub>-,-,-,23,25</sub> | 9.9<br><sub>-,-,-,7,6</sub> |  | 2.7<br><sub>-,-,-,2,1</sub> |  | 2.1<br><sub>-,-,-,3,1</sub> |  | 1.8<br><sub>-,-,-,1,2</sub> |  | 1.0 | 0.1 | 0.7 | 14.8 |
| Tyrese Proctor | 97% | 20.4<br><sub>27,34,29,26,24</sub> | 9.3<br><sub>22,24,17,8,5</sub> | 9.5 · 8.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>4,11,3,1,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.8<br><sub>3,10,2,1,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>5,4,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.1 | 0.9 | 15.1 |
| Meleek Thomas | 96% | 20.3<br><sub>18,34,30,22,20</sub> | 10.2<br><sub>12,20,10,14,4</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>0,4,6,2,1</sub> |  | 1.8<br><sub>3,2,3,2,4</sub> |  | 1.5<br><sub>2,3,1,4,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.2 | 1.0 | 14.6 |
| Mario Hezonja | 98% | 17.3<br><sub>9,34,15,28,20</sub> | 7.6<br><sub>4,22,9,16,10</sub> |  | 5.0<br><sub>4,7,4,7,10</sub> |  | 1.7<br><sub>0,4,2,5,3</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> |  | 0.6 | 0.2 | 0.8 | 14.3 |
| Jaylon Tyson | 98% | 15.7<br><sub>30,34,-,-,-</sub> | 6.8<br><sub>16,18,-,-,-</sub> | 8.5 · 9.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,4,-,-,-</sub> | 4.5<br><sub>o 38% · u 62%</sub> | 1.5<br><sub>1,4,-,-,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9<br><sub>4,3,-,-,-</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.2 | 0.8 | 11.2 |
| Thomas Bryant | 88% | 14.5<br><sub>16,27,18,12,16</sub> | 8.1<br><sub>9,19,9,5,9</sub> |  | 4.0<br><sub>1,11,5,4,6</sub> |  | 0.8<br><sub>1,3,4,0,0</sub> |  | 0.8<br><sub>0,2,0,1,2</sub> |  | 0.4 | 0.4 | 0.6 | 12.9 |
| Norchad Omier | 72% | 9.7<br><sub>-,27,13,16,6</sub> | 3.2<br><sub>-,13,4,2,2</sub> |  | 3.2<br><sub>-,8,6,7,1</sub> |  | 0.9<br><sub>-,2,2,0,0</sub> |  | 0.1<br><sub>-,1,0,0,0</sub> |  | 0.4 | 0.2 | 0.3 | 7.3 |
| Craig Porter Jr. | 67% | 9.1<br><sub>9,28,14,12,-</sub> | 2.5<br><sub>0,9,2,2,-</sub> |  | 1.8<br><sub>2,9,1,3,-</sub> |  | 1.8<br><sub>2,6,3,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.3 | 0.6 | 6.1 |
| Riley Minix | 48% | 6.3<br><sub>-,22,-,-,-</sub> | 2.2<br><sub>-,2,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.5 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 100% | 30.8<br><sub>26,24,28,23,41</sub> | 15.1<br><sub>8,4,18,2,23</sub> | 13.5 · 13.5<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>8,4,14,6,14</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 9.6<br><sub>5,8,9,7,22</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>2,1,1,0,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.5 | 3.1 | 32.0 |
| Matas Buzelis | 100% | 30.3<br><sub>30,31,30,25,38</sub> | 18.0<br><sub>18,23,25,9,21</sub> | 17.5 · 17.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>9,3,5,5,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>2,0,4,1,3</sub> |  | 2.5<br><sub>2,3,5,1,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 1.0 | 2.2 | 25.5 |
| Isaac Okoro | 100% | 29.8<br><sub>31,32,25,29,42</sub> | 10.5<br><sub>9,13,12,9,11</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>7,6,3,7,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>4,2,4,1,2</sub> |  | 1.3<br><sub>0,3,4,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.3 | 1.0 | 15.5 |
| Jalen Smith | 100% | 28.8<br><sub>-,28,21,-,34</sub> | 15.7<br><sub>-,17,14,-,26</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 8.1<br><sub>-,11,6,-,4</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>-,3,3,-,1</sub> |  | 2.1<br><sub>-,3,2,-,6</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.9 | 1.2 | 25.8 |
| Buddy Hield | 100% | 26.7<br><sub>20,19,19,23,40</sub> | 14.5<br><sub>16,6,11,15,33</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>4,4,1,4,7</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,2,2,0,6</sub> |  | 2.6<br><sub>4,2,3,4,7</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.3 | 1.4 | 20.7 |
| Nic Claxton | 98% | 20.7<br><sub>-,17,22,29,-</sub> | 8.6<br><sub>-,8,14,11,-</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>-,2,4,7,-</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>-,1,1,1,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 1.1 | 15.9 |
| Patrick Williams | 88% | 19.5<br><sub>26,13,13,23,16</sub> | 6.9<br><sub>14,0,2,6,2</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>5,0,1,3,2</sub> |  | 1.4<br><sub>1,0,2,1,0</sub> |  | 0.9<br><sub>2,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.9 | 10.8 |
| Tre Jones | 99% | 18.8<br><sub>24,23,16,25,12</sub> | 10.7<br><sub>16,16,10,12,9</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>0,2,2,1,2</sub> |  | 3.9<br><sub>4,6,6,7,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.2 | 1.1 | 16.7 |
| Zach Collins | 76% | 14.9<br><sub>28,-,11,15,17</sub> | 6.2<br><sub>8,-,3,6,5</sub> |  | 3.8<br><sub>5,-,2,2,1</sub> |  | 1.5<br><sub>4,-,0,4,0</sub> |  | 0.4<br><sub>0,-,1,0,1</sub> |  | 0.4 | 0.4 | 0.8 | 11.5 |
| Jordan Hawkins | 63% | 12.4<br><sub>-,4,-,-,14</sub> | 5.3<br><sub>-,0,-,-,6</sub> |  | 1.6<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,1,-,-,1</sub> |  | 0.6<br><sub>-,0,-,-,2</sub> |  | 0.3 | 0.2 | 0.5 | 7.6 |
| Noa Essengue | 98% | 12.2<br><sub>7,14,15,15,11</sub> | 5.2<br><sub>0,1,5,8,9</sub> |  | 2.5<br><sub>1,2,3,4,4</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.5<br><sub>0,0,0,2,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |
| Leonard Miller | 58% | 10.3<br><sub>17,1,7,-,-</sub> | 4.8<br><sub>4,0,4,-,-</sub> |  | 2.4<br><sub>3,0,2,-,-</sub> |  | 0.6<br><sub>4,0,0,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 7.8 |
| Orlando Robinson | 25% | 7.9<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.2 |
| Tobe Awaka | 52% | 7.0<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 5.3 |
| Jaylin Sellers | 76% | 6.7<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Dailyn Swain | 58% | 5.6<br><sub>-,2,6,-,-</sub> | 2.5<br><sub>-,0,2,-,-</sub> |  | 0.8<br><sub>-,1,1,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |

</details>


### PHX @ NOP
Out: Bennedict Mathurin (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PTS over 10.5 (11+) | PHX @ NOP | draftkings | 2.03 | 1.98 | 1.75 | 57.2% | 49.0% | 50.5% | +2.5% | +16.2% | 0.6% |
| Derik Queen PTS over 9.5 (10+) | PHX @ NOP | betright | 1.83 | 1.81 | 1.56 | 64.1% | 53.2% | 55.2% | +1.2% | +17.5% | 0.4% |
| Zion Williamson PTS under 21.5 | PHX @ NOP | betright | 1.91 | 1.91 | 1.57 | 63.7% | 49.9% | 52.4% | +0.1% | +21.6% | 0.0% |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 99% | 35.4<br><sub>35,28,37,33,38</sub> | 26.9<br><sub>30,17,20,29,23</sub> | 26.5 · 25.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>1,4,4,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.3<br><sub>7,7,8,6,3</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>4,0,1,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.9 | 36.5 |
| Dillon Brooks | 99% | 29.1<br><sub>30,22,27,31,25</sub> | 17.0<br><sub>15,1,15,29,18</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>3,2,4,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>1,0,4,5,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>3,0,3,5,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.4 | 23.0 |
| Miles Bridges | 99% | 28.3<br><sub>25,24,29,29,25</sub> | 14.8<br><sub>11,14,16,13,18</sub> | 14.5 · 14.5<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>6,3,8,6,9</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>3,3,2,5,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.6 | 1.0 | 24.3 |
| Jalen Green | 98% | 27.3<br><sub>21,21,27,30,25</sub> | 16.0<br><sub>12,9,16,18,14</sub> | 14.5 · 14.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>4,2,5,7,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>0,1,3,7,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.8<br><sub>1,1,2,4,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.3 | 2.2 | 23.0 |
| Collin Gillespie | 99% | 25.0<br><sub>27,28,26,17,27</sub> | 10.6<br><sub>13,26,10,9,16</sub> | 10.5 · 10.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>2,4,3,3,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.9<br><sub>1,4,3,1,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>3,5,2,2,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.2 | 1.2 | 17.8 |
| Oso Ighodaro | 98% | 24.6<br><sub>32,17,33,21,27</sub> | 6.8<br><sub>2,4,8,7,3</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>3,2,11,4,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>7,3,3,2,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.0 | 1.3 | 16.5 |
| Jordan Goodwin | 98% | 21.6<br><sub>24,31,20,17,28</sub> | 8.5<br><sub>6,14,11,2,5</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>5,7,6,5,9</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>2,6,2,3,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,1,1,0,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.2 | 0.8 | 15.6 |
| Luke Kennard | 98% | 17.0<br><sub>21,23,17,17,15</sub> | 7.0<br><sub>8,18,12,3,5</sub> | 8.5 · 7.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,6,2,3,0</sub> |  | 1.7<br><sub>1,4,0,1,0</sub> |  | 1.0<br><sub>0,3,4,1,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.5 | 0.1 | 0.6 | 10.5 |
| Khaman Maluach | 98% | 16.5<br><sub>16,13,11,21,18</sub> | 6.7<br><sub>4,7,4,10,9</sub> |  | 5.3<br><sub>2,4,6,2,6</sub> |  | 0.8<br><sub>1,0,0,0,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.1 | 0.9 | 12.7 |
| Ryan Dunn | 98% | 14.2<br><sub>10,24,12,13,9</sub> | 4.3<br><sub>0,3,5,6,0</sub> |  | 3.4<br><sub>4,6,1,5,5</sub> |  | 1.0<br><sub>0,1,0,2,0</sub> |  | 0.4<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.4 | 0.5 | 8.8 |
| Rasheer Fleming | 48% | 7.4<br><sub>-,-,-,4,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.4 |
| Jamaree Bouyea | 52% | 6.9<br><sub>-,-,-,4,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 0.9<br><sub>-,-,-,1,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 4.8 |
| Koa Peat | 80% | 6.5<br><sub>-,8,1,4,3</sub> | 3.4<br><sub>-,10,0,2,0</sub> |  | 1.5<br><sub>-,2,1,0,0</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.3 | 0.3 | 5.2 |
| Duop Reath | 48% | 6.2<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.4 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 31.9<br><sub>-,-,-,29,-</sub> | 16.2<br><sub>-,-,-,17,-</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>-,-,-,4,-</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>-,-,-,1,-</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.4<br><sub>-,-,-,3,-</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 1.6 | 24.7 |
| Saddiq Bey | 98% | 31.4<br><sub>41,33,42,37,32</sub> | 15.5<br><sub>16,23,10,21,2</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>6,6,8,6,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>4,3,6,3,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,5,2,4,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.2 | 1.0 | 23.2 |
| Jeremiah Fears | 99% | 30.9<br><sub>33,29,31,38,34</sub> | 17.8<br><sub>13,19,16,22,29</sub> | 17.5 · 17.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>4,10,5,7,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>7,10,4,5,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.5 | 3.1 | 28.3 |
| Zion Williamson | 76% | 30.6<br><sub>31,25,32,37,-</sub> | 19.7<br><sub>24,16,24,22,-</sub> | 21.5 · 21.5<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>6,6,7,6,-</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>2,2,1,7,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.2<br><sub>2,0,0,0,-</sub> |  | 1.2 | 0.6 | 2.1 | 28.8 |
| Derik Queen | 99% | 24.5<br><sub>25,21,19,18,35</sub> | 12.4<br><sub>10,17,9,11,15</sub> | 10.5 · 9.5<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>5,10,5,7,15</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.9<br><sub>4,0,0,3,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.5<br><sub>2,4,0,0,0</sub> |  | 1.0 | 0.8 | 2.4 | 22.6 |
| Herbert Jones | 98% | 24.4<br><sub>27,24,32,33,25</sub> | 7.5<br><sub>10,8,9,14,2</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>2,2,1,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0<br><sub>2,2,3,4,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.1 | 0.4 | 1.3 | 12.4 |
| Yves Missi | 98% | 23.5<br><sub>22,23,17,23,35</sub> | 7.2<br><sub>3,6,4,4,9</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 8.0<br><sub>8,14,5,7,13</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,1,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 1.1 | 16.6 |
| Jordan Poole | 88% | 23.3<br><sub>24,31,30,13,31</sub> | 12.2<br><sub>14,11,22,6,25</sub> |  | 2.2<br><sub>2,2,1,0,3</sub> |  | 3.2<br><sub>5,5,5,1,2</sub> |  | 1.9<br><sub>1,1,3,2,3</sub> |  | 0.7 | 0.3 | 1.8 | 17.7 |
| Jaron Pierre Jr. | 96% | 15.5<br><sub>23,19,17,4,25</sub> | 6.7<br><sub>13,10,7,3,6</sub> |  | 2.2<br><sub>2,4,1,2,5</sub> |  | 0.9<br><sub>0,0,1,0,0</sub> |  | 0.8<br><sub>2,2,1,1,2</sub> |  | 0.5 | 0.2 | 0.9 | 9.8 |
| Karlo Matkovic | 98% | 14.6<br><sub>14,20,10,8,15</sub> | 5.0<br><sub>5,3,0,0,3</sub> |  | 3.3<br><sub>3,2,2,2,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.5<br><sub>1,0,0,0,1</sub> |  | 0.4 | 0.6 | 0.8 | 9.1 |
| Bryce McGowens | 67% | 9.0<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 5.0 |
| DeAndre Jordan | 38% | 8.8<br><sub>-,-,10,-,-</sub> | 2.6<br><sub>-,-,8,-,-</sub> |  | 3.5<br><sub>-,-,2,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 6.6 |
| AJ Johnson | 52% | 6.6<br><sub>-,6,-,-,8</sub> | 2.5<br><sub>-,0,-,-,0</sub> |  | 0.8<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.8 |
| Malik Dia | 52% | 5.6<br><sub>-,5,-,-,-</sub> | 2.3<br><sub>-,2,-,-,-</sub> |  | 0.7<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### LAC @ HOU
Out: Bradley Beal (LAC)

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 99% | 32.7<br><sub>37,35,30,35,32</sub> | 21.0<br><sub>24,27,20,23,16</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>4,6,3,0,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 6.3<br><sub>7,7,7,5,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>3,3,2,3,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 3.4 | 29.8 |
| Rui Hachimura | 98% | 28.6<br><sub>32,22,27,32,29</sub> | 13.6<br><sub>7,4,20,17,19</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>11,2,5,7,8</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>3,0,1,2,1</sub> |  | 1.7<br><sub>1,0,4,2,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.3 | 1.2 | 19.4 |
| Derrick Jones Jr. | 98% | 26.8<br><sub>29,26,28,27,26</sub> | 9.5<br><sub>14,13,5,8,4</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>5,4,1,2,7</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>0,1,1,1,1</sub> |  | 1.1<br><sub>4,3,0,0,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.0 | 0.8 | 0.9 | 14.3 |
| Brook Lopez | 99% | 25.1<br><sub>31,29,23,27,25</sub> | 13.1<br><sub>26,7,23,23,21</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>7,5,6,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>4,8,2,4,0</sub> |  | 1.5<br><sub>3,1,4,5,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 1.1 | 1.2 | 19.6 |
| Max Strus | 98% | 24.6<br><sub>23,25,21,32,29</sub> | 9.0<br><sub>3,14,3,18,5</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>2,3,2,5,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>3,4,1,4,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,4,1,5,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.2 | 1.1 | 15.4 |
| Brandon Ingram | 8% | 23.5 | 13.7 | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.7 | 2.5<br><sub>o 60% · u 40%</sub> | 2.4 | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.5 | 1.7 | 19.7 |
| Kris Dunn | 99% | 22.3<br><sub>20,18,26,20,19</sub> | 6.1<br><sub>2,7,2,6,3</sub> |  | 2.9<br><sub>3,3,5,2,4</sub> |  | 3.1<br><sub>6,1,5,2,5</sub> |  | 0.6<br><sub>0,0,0,1,1</sub> |  | 1.5 | 0.3 | 1.1 | 12.0 |
| Keaton Wagler | 98% | 19.7<br><sub>18,28,18,17,19</sub> | 9.8<br><sub>14,12,15,7,7</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>2,4,2,5,7</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>1,5,0,2,3</sub> |  | 1.1<br><sub>2,2,1,1,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.7 | 0.2 | 1.7 | 15.2 |
| Kobe Sanders | 98% | 18.7<br><sub>15,20,18,14,19</sub> | 7.0<br><sub>5,2,5,0,9</sub> |  | 2.0<br><sub>0,6,1,1,3</sub> |  | 1.7<br><sub>1,4,3,1,1</sub> |  | 0.9<br><sub>1,0,0,0,3</sub> |  | 0.8 | 0.1 | 1.1 | 10.7 |
| Gradey Dick | 98% | 15.1<br><sub>19,19,17,13,16</sub> | 6.5<br><sub>13,12,0,2,6</sub> |  | 2.2<br><sub>3,2,0,2,5</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.6<br><sub>2,2,0,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 9.4 |
| Yanic Konan Niederhauser | 64% | 12.8<br><sub>-,-,-,11,16</sub> | 4.2<br><sub>-,-,-,2,6</sub> |  | 3.4<br><sub>-,-,-,3,6</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.7 | 0.8 | 8.3 |
| Isaiah Jackson | 98% | 11.8<br><sub>17,15,19,9,4</sub> | 4.9<br><sub>5,13,8,6,0</sub> |  | 3.3<br><sub>3,2,5,4,0</sub> |  | 0.9<br><sub>3,2,0,2,0</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.5 | 0.8 | 0.8 | 9.0 |
| Baba Miller | 88% | 8.4<br><sub>-,5,4,1,3</sub> | 3.9<br><sub>-,2,3,0,1</sub> |  | 1.2<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,0,0,0,1</sub> |  | 0.2<br><sub>-,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.0 |
| Jalen Pickett | 52% | 6.2<br><sub>-,-,-,1,-</sub> | 2.3<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.9<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Blake Wesley | 52% | 6.1<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.3 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 99% | 36.0<br><sub>33,30,29,32,35</sub> | 22.7<br><sub>22,25,22,21,16</sub> | 20.5 · –<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>3,4,2,2,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>6,5,3,3,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>2,2,2,4,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.9 | 3.1 | 33.0 |
| Amen Thompson | 88% | 34.9<br><sub>41,29,-,31,26</sub> | 17.1<br><sub>12,26,-,15,22</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>10,7,-,9,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>3,7,-,3,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.3<br><sub>0,3,-,0,0</sub> |  | 1.5 | 0.8 | 2.2 | 28.6 |
| Alperen Sengun | 96% | 34.6<br><sub>37,28,30,14,36</sub> | 21.5<br><sub>43,19,23,7,28</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 9.8<br><sub>12,8,7,7,11</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>5,8,2,1,10</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>1,1,1,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.2 | 1.0 | 3.0 | 38.1 |
| Jabari Smith Jr. | 99% | 34.5<br><sub>24,28,32,26,32</sub> | 15.6<br><sub>6,9,12,17,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>3,6,10,4,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>0,5,1,2,3</sub> |  | 2.2<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.8 | 1.3 | 24.5 |
| Fred VanVleet | 88% | 32.8<br><sub>34,-,26,27,33</sub> | 14.3<br><sub>17,-,8,15,25</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>2,-,5,2,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 5.6<br><sub>3,-,6,6,9</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>3,-,2,3,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.4 | 1.5 | 23.1 |
| Tari Eason | 99% | 24.4<br><sub>33,30,27,25,23</sub> | 9.9<br><sub>14,25,7,11,7</sub> |  | 5.8<br><sub>11,7,7,4,6</sub> |  | 1.5<br><sub>2,1,3,3,1</sub> |  | 1.1<br><sub>2,3,0,1,1</sub> |  | 1.2 | 0.6 | 1.2 | 17.1 |
| Marcus Smart | 64% | 20.0<br><sub>-,-,-,18,23</sub> | 7.0<br><sub>-,-,-,4,3</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>-,-,-,2,2</sub> |  | 2.2<br><sub>-,-,-,4,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0<br><sub>-,-,-,1,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.1 | 0.4 | 1.3 | 11.3 |
| Reed Sheppard | 93% | 18.5<br><sub>19,26,19,25,14</sub> | 8.4<br><sub>0,11,5,20,0</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,1,2,4,2</sub> |  | 2.3<br><sub>3,6,2,2,0</sub> |  | 1.5<br><sub>0,3,1,6,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.4 | 0.9 | 12.5 |
| Steven Adams | 52% | 13.3<br><sub>-,12,-,16,12</sub> | 3.9<br><sub>-,6,-,4,2</sub> |  | 4.7<br><sub>-,7,-,5,2</sub> |  | 0.9<br><sub>-,1,-,2,2</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 9.5 |
| Bogdan Bogdanovic | 98% | 11.0<br><sub>12,22,26,11,5</sub> | 4.1<br><sub>11,12,6,1,0</sub> |  | 1.3<br><sub>1,3,0,3,1</sub> |  | 1.0<br><sub>3,4,1,0,0</sub> |  | 0.5<br><sub>3,2,2,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.4 |
| Clint Capela | 38% | 9.8<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.6 | 0.5 | 7.4 |
| Oscar Tshiebwe | 72% | 7.7<br><sub>6,12,6,11,-</sub> | 3.4<br><sub>0,4,6,4,-</sub> |  | 3.3<br><sub>5,9,6,4,-</sub> |  | 0.6<br><sub>0,3,0,3,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 7.2 |
| Isaiah Crawford | 63% | 6.5<br><sub>-,9,21,2,-</sub> | 2.3<br><sub>-,4,11,0,-</sub> |  | 1.4<br><sub>-,2,10,0,-</sub> |  | 0.3<br><sub>-,0,3,0,-</sub> |  | 0.1<br><sub>-,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Jae'Sean Tate | 58% | 5.8<br><sub>-,8,12,1,-</sub> | 1.8<br><sub>-,4,3,0,-</sub> |  | 1.4<br><sub>-,2,3,0,-</sub> |  | 0.4<br><sub>-,0,2,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |
| Bruce Thornton | 72% | 5.8<br><sub>-,6,12,1,-</sub> | 2.6<br><sub>-,2,7,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |

</details>


### UTA @ LAL
Out: Austin Reaves (LAL), Jaxson Hayes (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 33.3<br><sub>34,35,39,36,26</sub> | 21.0<br><sub>13,30,30,14,15</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>4,2,1,3,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>8,11,10,6,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>1,4,5,0,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.8 | 0.2 | 3.4 | 31.3 |
| Ace Bailey | 99% | 31.3<br><sub>30,23,27,24,33</sub> | 15.2<br><sub>7,5,19,7,16</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>8,1,8,7,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>4,4,3,1,2</sub> |  | 2.1<br><sub>1,1,2,0,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.7 | 2.0 | 22.8 |
| Darryn Peterson | 99% | 31.1<br><sub>34,31,19,32,25</sub> | 16.9<br><sub>17,13,11,20,6</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>5,5,1,10,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>4,2,3,8,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,2,1,0,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 0.5 | 2.4 | 25.6 |
| Svi Mykhailiuk | 98% | 27.0<br><sub>21,33,34,28,32</sub> | 11.5<br><sub>6,8,15,11,39</sub> |  | 3.1<br><sub>2,7,3,7,5</sub> |  | 2.3<br><sub>3,5,5,2,3</sub> |  | 2.1<br><sub>2,2,4,3,10</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.1 | 1.3 | 16.9 |
| Josh Green | 98% | 25.5<br><sub>15,13,28,29,23</sub> | 6.0<br><sub>6,9,11,8,0</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>1,0,2,0,0</sub> |  | 0.8<br><sub>2,1,2,2,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.9 | 0.2 | 0.9 | 9.8 |
| Brice Sensabaugh | 99% | 23.4<br><sub>30,35,14,26,17</sub> | 14.2<br><sub>14,40,8,18,10</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>7,11,3,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,5,2,1,2</sub> |  | 2.2<br><sub>0,8,0,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.2 | 1.9 | 19.8 |
| Mo Bamba | 91% | 22.9<br><sub>36,31,23,20,23</sub> | 7.9<br><sub>26,15,6,2,6</sub> |  | 7.7<br><sub>5,10,16,2,10</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>4,3,0,0,1</sub> |  | 0.5<br><sub>6,1,0,0,0</sub> |  | 0.6 | 1.2 | 1.1 | 16.6 |
| Josh Okogie | 98% | 21.4<br><sub>27,22,15,17,14</sub> | 6.1<br><sub>7,9,3,3,1</sub> |  | 3.2<br><sub>6,2,0,2,4</sub> |  | 1.2<br><sub>0,4,0,2,0</sub> |  | 0.7<br><sub>2,1,0,0,0</sub> |  | 1.1 | 0.2 | 0.9 | 10.6 |
| Isaiah Collier | 64% | 16.8<br><sub>-,-,10,-,13</sub> | 7.8<br><sub>-,-,0,-,10</sub> |  | 2.3<br><sub>-,-,1,-,2</sub> |  | 4.6<br><sub>-,-,2,-,7</sub> |  | 0.4<br><sub>-,-,0,-,1</sub> |  | 0.7 | 0.2 | 1.7 | 14.7 |
| Kyle Filipowski | 58% | 14.0<br><sub>-,-,6,-,9</sub> | 6.7<br><sub>-,-,0,-,2</sub> |  | 4.2<br><sub>-,-,3,-,4</sub> |  | 1.5<br><sub>-,-,0,-,3</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 1.0 | 12.3 |
| Tony Bradley | 58% | 13.6<br><sub>12,17,-,-,13</sub> | 3.9<br><sub>6,3,-,-,1</sub> |  | 4.2<br><sub>2,7,-,-,5</sub> |  | 0.6<br><sub>0,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.3 | 0.7 | 8.6 |
| Kobe Bufkin | 23% | 11.3<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.9 |
| Jonas Aidoo | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Harrison Ingram | 8% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 99% | 35.2<br><sub>32,36,42,37,36</sub> | 38.9<br><sub>32,43,36,29,25</sub> | 35.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>5,3,6,5,4</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 8.3<br><sub>5,9,7,7,8</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 4.6<br><sub>5,5,5,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.5 | 4.3 | 53.9 |
| Quentin Grimes | 99% | 31.2<br><sub>-,37,42,35,35</sub> | 14.0<br><sub>-,22,47,20,13</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>-,6,6,7,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>-,1,3,4,7</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>-,5,10,4,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.3 | 1.5 | 21.4 |
| Walker Kessler | 99% | 29.4<br><sub>29,32,-,31,30</sub> | 12.6<br><sub>10,14,-,10,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 11.7<br><sub>11,12,-,11,7</sub> | 11.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>3,3,-,1,2</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.9 | 2.4 | 1.5 | 26.2 |
| Matisse Thybulle | 98% | 24.6<br><sub>23,26,31,21,27</sub> | 7.6<br><sub>8,12,7,2,14</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>5,8,6,1,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>1,0,0,3,1</sub> |  | 1.3<br><sub>2,2,2,0,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.4 | 0.8 | 1.0 | 11.8 |
| Jake LaRavia | 98% | 24.3<br><sub>21,32,23,30,24</sub> | 6.7<br><sub>0,12,4,4,6</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>9,3,5,6,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>6,3,2,2,0</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 1.3 | 0.6 | 1.0 | 12.9 |
| Ziaire Williams | 98% | 22.6<br><sub>20,19,24,18,28</sub> | 8.9<br><sub>9,6,0,7,5</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>1,2,1,2,0</sub> |  | 1.5<br><sub>5,3,1,0,1</sub> |  | 1.2<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 0.8 | 12.8 |
| Sandro Mamukelashvili | 99% | 21.0<br><sub>26,21,23,21,20</sub> | 9.8<br><sub>23,4,3,6,9</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>3,2,3,3,9</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,3,2,0,2</sub> |  | 1.2<br><sub>5,0,0,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.5 | 0.8 | 16.2 |
| Collin Sexton | 99% | 20.4<br><sub>13,24,25,20,18</sub> | 12.9<br><sub>10,16,10,12,10</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>1,0,4,0,1</sub> |  | 2.9<br><sub>3,3,3,1,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>0,2,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.1 | 1.6 | 17.9 |
| Jarred Vanderbilt | 91% | 12.4<br><sub>9,12,14,12,10</sub> | 3.1<br><sub>4,2,4,0,4</sub> |  | 3.9<br><sub>3,4,7,5,4</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.1 |
| Cameron Carr | 72% | 8.8<br><sub>13,-,-,2,12</sub> | 3.8<br><sub>0,-,-,5,5</sub> |  | 1.2<br><sub>2,-,-,0,1</sub> |  | 0.6<br><sub>0,-,-,1,0</sub> |  | 0.4<br><sub>0,-,-,1,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Kevon Looney | 38% | 7.9<br><sub>4,-,17,-,-</sub> | 1.6<br><sub>0,-,4,-,-</sub> |  | 3.0<br><sub>2,-,8,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.2 | 5.2 |
| Carson Cooper | 58% | 7.3<br><sub>-,-,18,2,-</sub> | 2.4<br><sub>-,-,3,2,-</sub> |  | 2.1<br><sub>-,-,4,1,-</sub> |  | 0.4<br><sub>-,-,2,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.0 |
| Adou Thiero | 64% | 7.3<br><sub>14,-,6,6,-</sub> | 2.5<br><sub>2,-,0,0,-</sub> |  | 1.8<br><sub>2,-,0,1,-</sub> |  | 0.6<br><sub>1,-,1,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |
| Jaden Hardy | 52% | 6.7<br><sub>4,-,-,2,-</sub> | 3.7<br><sub>3,-,-,0,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.6<br><sub>0,-,-,1,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Bronny James | 52% | 5.5<br><sub>4,-,-,2,-</sub> | 2.0<br><sub>4,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.5 |
| Chris Manon | 52% | 5.4<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.3 |

</details>


### SAS @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Dylan Harper (SAS), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.9–108.2 | SAS 73% | 1.37 / 3.70 | SAC +8.5 | 225.5 | SAC +12.5 covers 61%; o224.5 51% |
| Expected (weighted by chance each plays) | 118.3–107.6 | SAS 78% | 1.29 / 4.48 | SAC +10.5 | 225.5 | SAC +12.5 covers 55%; o224.5 53% |
| if De'Aaron Fox plays | 117.7–108.4 | SAS 74% | 1.34 / 3.91 | SAC +9.5 | 226.5 | SAC +12.5 covers 59%; o224.5 53% |
| if Victor Wembanyama plays | 118.0–106.8 | SAS 79% | 1.27 / 4.71 | SAC +11.5 | 224.5 | SAC +12.5 covers 54%; o224.5 51% |
| if Jordan McLaughlin plays | 117.4–108.7 | SAS 73% | 1.37 / 3.70 | SAC +8.5 | 226.5 | SAC +12.5 covers 60%; o224.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 31.9 | 17.9 | 4.1 | 6.9 | 1.3 | 1.4 | 0.3 | 2.7 | 28.9 | full tables below |
| Victor Wembanyama (SAS) | Questionable | 55% | 32.6 | 32.0 | 12.1 | 4.5 | 2.3 | 1.2 | 3.3 | 2.9 | 48.6 | full tables below |
| Jordan McLaughlin (SAS) | Questionable | 55% | 24.7 | 8.6 | 3.6 | 4.5 | 1.1 | 1.7 | 0.2 | 1.2 | 16.8 | full tables below |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 99% | 32.6<br><sub>23,32,36,32,26</sub> | 18.3<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>2,6,5,4,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 4.0<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.5 | 1.4 | 26.8 |
| Stephon Castle | 99% | 32.5<br><sub>25,35,31,33,29</sub> | 23.7<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 8.3<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>5,0,2,2,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 3.2 | 37.4 |
| Julian Champagnie | 99% | 30.0<br><sub>23,24,30,29,25</sub> | 14.7<br><sub>7,4,14,20,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>8,5,6,4,3</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>3,1,0,1,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>1,1,4,4,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.5 | 1.0 | 22.0 |
| Keldon Johnson | 99% | 27.9<br><sub>25,29,15,27,23</sub> | 15.2<br><sub>18,11,4,10,10</sub> |  | 5.9<br><sub>4,10,2,5,4</sub> |  | 3.0<br><sub>4,2,1,3,4</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.4 | 24.1 |
| Harrison Barnes | 93% | 26.5<br><sub>21,14,10,16,21</sub> | 11.7<br><sub>11,0,0,9,3</sub> |  | 3.1<br><sub>1,0,3,2,5</sub> |  | 1.9<br><sub>1,2,4,1,2</sub> |  | 1.7<br><sub>3,0,0,1,0</sub> |  | 0.8 | 0.2 | 0.9 | 16.7 |
| Carter Bryant | 96% | 26.1<br><sub>19,5,2,13,20</sub> | 11.1<br><sub>8,0,0,3,8</sub> |  | 4.0<br><sub>3,1,0,1,3</sub> |  | 1.9<br><sub>2,0,0,0,0</sub> |  | 1.8<br><sub>2,0,0,1,2</sub> |  | 0.6 | 0.6 | 1.1 | 17.0 |
| Luke Kornet | 99% | 20.5<br><sub>16,13,14,15,10</sub> | 5.9<br><sub>6,2,2,4,0</sub> |  | 5.8<br><sub>7,2,1,0,3</sub> |  | 1.9<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.9 | 0.7 | 13.6 |
| Tarris Reed Jr. | 58% | 19.0<br><sub>11,-,-,-,6</sub> | 6.9<br><sub>2,-,-,-,0</sub> |  | 7.5<br><sub>4,-,-,-,4</sub> |  | 1.1<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.6 | 1.1 | 15.4 |
| David Jones Garcia | 58% | 16.7<br><sub>-,-,-,-,4</sub> | 7.5<br><sub>-,-,-,-,0</sub> |  | 2.6<br><sub>-,-,-,-,1</sub> |  | 2.7<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 1.0 | 0.2 | 0.9 | 12.8 |
| Ja'Kobi Gillespie | 88% | 15.3<br><sub>-,-,-,-,-</sub> | 10.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.1 | 0.6 | 11.7 |
| Maliq Brown | 80% | 14.2<br><sub>-,-,-,-,-</sub> | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 5.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 6.6 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 35.7<br><sub>35,33,35,36,40</sub> | 23.3<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.5<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.2 | 3.6 | 34.6 |
| De'Andre Hunter | 88% | 32.9<br><sub>42,-,35,37,41</sub> | 14.1<br><sub>24,-,7,30,20</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,-,1,6,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.5 | 20.7 |
| Keegan Murray | 98% | 31.7<br><sub>40,21,31,40,40</sub> | 12.2<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.9 | 0.9 | 19.1 |
| Zach LaVine | 88% | 31.5<br><sub>36,-,32,39,30</sub> | 16.8<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 2.0 | 23.0 |
| Domantas Sabonis | 99% | 31.0<br><sub>35,29,24,38,32</sub> | 14.6<br><sub>21,11,8,19,15</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 11.8<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.3 | 2.3 | 31.3 |
| Precious Achiuwa | 98% | 21.4<br><sub>-,-,8,-,22</sub> | 9.0<br><sub>-,-,0,-,5</sub> |  | 5.6<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.7 |
| Malik Monk | 98% | 14.4<br><sub>18,29,20,12,10</sub> | 7.4<br><sub>7,14,8,2,3</sub> |  | 1.3<br><sub>4,1,1,0,0</sub> |  | 2.6<br><sub>3,10,2,3,1</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.2 | 1.1 | 11.3 |
| Emanuel Sharp | 98% | 14.2<br><sub>7,21,14,10,16</sub> | 4.7<br><sub>4,9,6,3,3</sub> |  | 1.2<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Leaky Black | 91% | 12.9<br><sub>12,29,17,19,4</sub> | 3.0<br><sub>0,12,3,0,2</sub> |  | 2.0<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.7 | 0.3 | 0.3 | 5.8 |
| Dylan Cardwell | 98% | 12.1<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.2<br><sub>3,6,4,4,1</sub> |  | 1.0<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 9.0 |
| Gabe Vincent | 5% | 9.3 | 2.7 |  | 0.8 |  | 1.0 |  | 0.3 |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Daeqwon Plowden | 58% | 7.8<br><sub>2,24,4,-,-</sub> | 2.9<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Alex Karaban | 48% | 7.5<br><sub>-,29,4,-,-</sub> | 1.5<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.0 |
| Mason Plumlee | 48% | 6.0<br><sub>-,5,4,-,-</sub> | 1.8<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.4 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. (SAC) | 98% | 35.7<br><sub>35,33,35,36,40</sub> | 23.4<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.5<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.2 | 3.6 | 34.6 |
| De'Andre Hunter (SAC) | 88% | 33.0<br><sub>42,-,35,37,41</sub> | 14.1<br><sub>24,-,7,30,20</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,-,1,6,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.3 | 1.4 | 20.7 |
| Keegan Murray (SAC) | 98% | 31.6<br><sub>40,21,31,40,40</sub> | 12.2<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.9 | 0.9 | 19.1 |
| Zach LaVine (SAC) | 88% | 31.4<br><sub>36,-,32,39,30</sub> | 16.8<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 2.0 | 22.9 |
| Domantas Sabonis (SAC) | 99% | 31.1<br><sub>35,29,24,38,32</sub> | 14.5<br><sub>21,11,8,19,15</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 11.8<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.3 | 2.3 | 31.3 |
| Precious Achiuwa (SAC) | 98% | 21.4<br><sub>-,-,8,-,22</sub> | 9.0<br><sub>-,-,0,-,5</sub> |  | 5.6<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.7 |
| Malik Monk (SAC) | 98% | 14.4<br><sub>18,29,20,12,10</sub> | 7.4<br><sub>7,14,8,2,3</sub> |  | 1.3<br><sub>4,1,1,0,0</sub> |  | 2.6<br><sub>3,10,2,3,1</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.2 | 1.1 | 11.3 |
| Emanuel Sharp (SAC) | 98% | 14.2<br><sub>7,21,14,10,16</sub> | 4.7<br><sub>4,9,6,3,3</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Leaky Black (SAC) | 91% | 13.0<br><sub>12,29,17,19,4</sub> | 3.0<br><sub>0,12,3,0,2</sub> |  | 2.0<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.7 | 0.3 | 0.3 | 5.8 |
| Dylan Cardwell (SAC) | 98% | 12.1<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.2<br><sub>3,6,4,4,1</sub> |  | 0.9<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 9.0 |
| Gabe Vincent (SAC) | 5% | 9.3 | 2.7 |  | 0.7 |  | 1.0 |  | 0.2 |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Daeqwon Plowden (SAC) | 58% | 7.8<br><sub>2,24,4,-,-</sub> | 2.9<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Alex Karaban (SAC) | 48% | 7.5<br><sub>-,29,4,-,-</sub> | 1.5<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.0 |
| Mason Plumlee (SAC) | 48% | 6.1<br><sub>-,5,4,-,-</sub> | 1.9<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.5 |
| Devin Vassell (SAS) | 99% | 32.7<br><sub>23,32,36,32,26</sub> | 17.2<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>2,6,5,4,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.6<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.4 | 1.3 | 25.5 |
| Stephon Castle (SAS) | 99% | 32.3<br><sub>25,35,31,33,29</sub> | 21.6<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 7.5<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>5,0,2,2,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.2 | 3.1 | 34.5 |
| De'Aaron Fox (SAS) | 100% | 31.9<br><sub>17,-,34,32,26</sub> | 17.9<br><sub>7,-,6,10,5</sub> | 15.5 · – | 4.1<br><sub>5,-,2,2,2</sub> | 3.5 | 6.9<br><sub>1,-,2,5,10</sub> | 6.5 | 1.3<br><sub>0,-,0,0,0</sub> | 1.5 | 1.4 | 0.3 | 2.7 | 28.9 |
| Julian Champagnie (SAS) | 99% | 29.9<br><sub>23,24,30,29,25</sub> | 13.5<br><sub>7,4,14,20,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>8,5,6,4,3</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>3,1,0,1,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,1,4,4,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.5 | 0.9 | 20.6 |
| Keldon Johnson (SAS) | 99% | 27.5<br><sub>25,29,15,27,23</sub> | 14.2<br><sub>18,11,4,10,10</sub> |  | 5.8<br><sub>4,10,2,5,4</sub> |  | 2.8<br><sub>4,2,1,3,4</sub> |  | 0.9<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.2 | 22.8 |
| Harrison Barnes (SAS) | 93% | 23.4<br><sub>21,14,10,16,21</sub> | 9.5<br><sub>11,0,0,9,3</sub> |  | 2.8<br><sub>1,0,3,2,5</sub> |  | 1.6<br><sub>1,2,4,1,2</sub> |  | 1.4<br><sub>3,0,0,1,0</sub> |  | 0.7 | 0.2 | 0.7 | 13.9 |
| Carter Bryant (SAS) | 96% | 20.5<br><sub>19,5,2,13,20</sub> | 8.0<br><sub>8,0,0,3,8</sub> |  | 3.2<br><sub>3,1,0,1,3</sub> |  | 1.3<br><sub>2,0,0,0,0</sub> |  | 1.2<br><sub>2,0,0,1,2</sub> |  | 0.5 | 0.5 | 0.8 | 12.6 |
| Luke Kornet (SAS) | 99% | 18.0<br><sub>16,13,14,15,10</sub> | 5.0<br><sub>6,2,2,4,0</sub> |  | 5.3<br><sub>7,2,1,0,3</sub> |  | 1.5<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.6 | 11.7 |
| Tarris Reed Jr. (SAS) | 58% | 13.1<br><sub>11,-,-,-,6</sub> | 4.8<br><sub>2,-,-,-,0</sub> |  | 5.5<br><sub>4,-,-,-,4</sub> |  | 0.8<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.5 | 0.7 | 11.1 |
| David Jones Garcia (SAS) | 58% | 11.9<br><sub>-,-,-,-,4</sub> | 4.9<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,1</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.2 | 0.6 | 8.6 |
| Maliq Brown (SAS) | 80% | 9.5<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 3.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.3 |
| Ja'Kobi Gillespie (SAS) | 88% | 9.5<br><sub>-,-,-,-,-</sub> | 6.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 7.6 |

</details>

<details><summary>if Jordan McLaughlin plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. (SAC) | 98% | 35.7<br><sub>35,33,35,36,40</sub> | 23.4<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.5<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.2 | 3.6 | 34.6 |
| De'Andre Hunter (SAC) | 88% | 32.8<br><sub>42,-,35,37,41</sub> | 14.1<br><sub>24,-,7,30,20</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,-,1,6,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.4 | 20.7 |
| Keegan Murray (SAC) | 98% | 31.7<br><sub>40,21,31,40,40</sub> | 12.3<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.9 | 0.9 | 19.2 |
| Zach LaVine (SAC) | 88% | 31.4<br><sub>36,-,32,39,30</sub> | 16.8<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 2.0 | 23.0 |
| Domantas Sabonis (SAC) | 99% | 30.9<br><sub>35,29,24,38,32</sub> | 14.6<br><sub>21,11,8,19,15</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 11.8<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.3 | 2.2 | 31.3 |
| Precious Achiuwa (SAC) | 98% | 21.5<br><sub>-,-,8,-,22</sub> | 9.0<br><sub>-,-,0,-,5</sub> |  | 5.6<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.6 | 0.9 | 15.7 |
| Malik Monk (SAC) | 98% | 14.5<br><sub>18,29,20,12,10</sub> | 7.5<br><sub>7,14,8,2,3</sub> |  | 1.3<br><sub>4,1,1,0,0</sub> |  | 2.6<br><sub>3,10,2,3,1</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.3 | 1.1 | 11.5 |
| Emanuel Sharp (SAC) | 98% | 14.3<br><sub>7,21,14,10,16</sub> | 4.7<br><sub>4,9,6,3,3</sub> |  | 1.2<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Leaky Black (SAC) | 91% | 12.9<br><sub>12,29,17,19,4</sub> | 3.0<br><sub>0,12,3,0,2</sub> |  | 2.0<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.7 | 0.3 | 0.3 | 5.8 |
| Dylan Cardwell (SAC) | 98% | 12.1<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.2<br><sub>3,6,4,4,1</sub> |  | 0.9<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 9.0 |
| Gabe Vincent (SAC) | 5% | 9.3 | 2.8 |  | 0.8 |  | 0.9 |  | 0.3 |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Daeqwon Plowden (SAC) | 58% | 7.7<br><sub>2,24,4,-,-</sub> | 2.8<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Alex Karaban (SAC) | 48% | 7.6<br><sub>-,29,4,-,-</sub> | 1.5<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.0 |
| Mason Plumlee (SAC) | 48% | 6.1<br><sub>-,5,4,-,-</sub> | 1.9<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.5 |
| Devin Vassell (SAS) | 99% | 32.5<br><sub>23,32,36,32,26</sub> | 17.9<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>2,6,5,4,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.8<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.5 | 1.4 | 26.2 |
| Stephon Castle (SAS) | 99% | 32.2<br><sub>25,35,31,33,29</sub> | 22.9<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 7.7<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>5,0,2,2,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 3.2 | 36.0 |
| Julian Champagnie (SAS) | 99% | 29.8<br><sub>23,24,30,29,25</sub> | 14.3<br><sub>7,4,14,20,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>8,5,6,4,3</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>3,1,0,1,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,1,4,4,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.5 | 1.0 | 21.5 |
| Keldon Johnson (SAS) | 99% | 27.7<br><sub>25,29,15,27,23</sub> | 14.9<br><sub>18,11,4,10,10</sub> |  | 5.9<br><sub>4,10,2,5,4</sub> |  | 3.0<br><sub>4,2,1,3,4</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.9 | 0.2 | 1.4 | 23.8 |
| Harrison Barnes (SAS) | 93% | 25.9<br><sub>21,14,10,16,21</sub> | 11.1<br><sub>11,0,0,9,3</sub> |  | 3.1<br><sub>1,0,3,2,5</sub> |  | 1.9<br><sub>1,2,4,1,2</sub> |  | 1.6<br><sub>3,0,0,1,0</sub> |  | 0.8 | 0.2 | 0.9 | 16.0 |
| Carter Bryant (SAS) | 96% | 24.9<br><sub>19,5,2,13,20</sub> | 10.5<br><sub>8,0,0,3,8</sub> |  | 3.9<br><sub>3,1,0,1,3</sub> |  | 1.9<br><sub>2,0,0,0,0</sub> |  | 1.6<br><sub>2,0,0,1,2</sub> |  | 0.6 | 0.5 | 1.1 | 16.2 |
| Jordan McLaughlin (SAS) | 100% | 24.7<br><sub>14,19,-,11,18</sub> | 8.6<br><sub>4,10,-,0,0</sub> |  | 3.6<br><sub>6,1,-,1,3</sub> |  | 4.5<br><sub>2,2,-,5,2</sub> |  | 1.1<br><sub>0,2,-,0,0</sub> |  | 1.7 | 0.2 | 1.2 | 16.8 |
| Luke Kornet (SAS) | 99% | 19.0<br><sub>16,13,14,15,10</sub> | 5.4<br><sub>6,2,2,4,0</sub> |  | 5.4<br><sub>7,2,1,0,3</sub> |  | 1.8<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.6 | 12.6 |
| Tarris Reed Jr. (SAS) | 58% | 16.5<br><sub>11,-,-,-,6</sub> | 6.1<br><sub>2,-,-,-,0</sub> |  | 6.6<br><sub>4,-,-,-,4</sub> |  | 1.0<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.5 | 1.0 | 13.7 |
| David Jones Garcia (SAS) | 58% | 14.8<br><sub>-,-,-,-,4</sub> | 6.6<br><sub>-,-,-,-,0</sub> |  | 2.4<br><sub>-,-,-,-,1</sub> |  | 2.2<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 11.2 |
| Ja'Kobi Gillespie (SAS) | 88% | 12.9<br><sub>-,-,-,-,-</sub> | 8.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.5 | 9.8 |
| Maliq Brown (SAS) | 80% | 12.0<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.4 | 4.6 |

</details>

<details><summary>if Victor Wembanyama plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. (SAC) | 98% | 35.7<br><sub>35,33,35,36,40</sub> | 23.2<br><sub>17,26,36,18,21</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,0,4,1,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.5<br><sub>6,6,6,12,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,6,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.2 | 3.6 | 34.4 |
| De'Andre Hunter (SAC) | 88% | 32.9<br><sub>42,-,35,37,41</sub> | 13.9<br><sub>24,-,7,30,20</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,-,1,6,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>2,-,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,-,1,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.3 | 1.4 | 20.5 |
| Keegan Murray (SAC) | 98% | 31.6<br><sub>40,21,31,40,40</sub> | 12.2<br><sub>16,6,12,13,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>7,1,7,7,12</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>4,0,3,4,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.9 | 0.9 | 19.0 |
| Zach LaVine (SAC) | 88% | 31.5<br><sub>36,-,32,39,30</sub> | 16.7<br><sub>12,-,18,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,-,5,7,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>6,-,2,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,-,2,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 2.0 | 22.8 |
| Domantas Sabonis (SAC) | 99% | 31.0<br><sub>35,29,24,38,32</sub> | 14.4<br><sub>21,11,8,19,15</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 11.8<br><sub>12,13,13,16,17</sub> | 12.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>5,3,8,1,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.3 | 2.3 | 31.2 |
| Precious Achiuwa (SAC) | 98% | 21.3<br><sub>-,-,8,-,22</sub> | 8.9<br><sub>-,-,0,-,5</sub> |  | 5.5<br><sub>-,-,0,-,7</sub> |  | 1.1<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.7 | 0.9 | 15.5 |
| Malik Monk (SAC) | 98% | 14.4<br><sub>18,29,20,12,10</sub> | 7.4<br><sub>7,14,8,2,3</sub> |  | 1.3<br><sub>4,1,1,0,0</sub> |  | 2.6<br><sub>3,10,2,3,1</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.4 | 0.2 | 1.1 | 11.4 |
| Emanuel Sharp (SAC) | 98% | 14.2<br><sub>7,21,14,10,16</sub> | 4.7<br><sub>4,9,6,3,3</sub> |  | 1.2<br><sub>0,0,2,0,0</sub> |  | 0.7<br><sub>0,2,1,1,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Leaky Black (SAC) | 91% | 12.9<br><sub>12,29,17,19,4</sub> | 3.0<br><sub>0,12,3,0,2</sub> |  | 2.0<br><sub>0,9,0,3,0</sub> |  | 0.8<br><sub>0,2,2,1,0</sub> |  | 0.3<br><sub>0,4,1,0,0</sub> |  | 0.7 | 0.3 | 0.3 | 5.7 |
| Dylan Cardwell (SAC) | 98% | 12.0<br><sub>13,19,12,10,6</sub> | 3.8<br><sub>6,10,6,0,0</sub> |  | 4.2<br><sub>3,6,4,4,1</sub> |  | 0.9<br><sub>3,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 8.9 |
| Gabe Vincent (SAC) | 5% | 9.3 | 2.7 |  | 0.8 |  | 1.0 |  | 0.3 |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Daeqwon Plowden (SAC) | 58% | 7.8<br><sub>2,24,4,-,-</sub> | 2.9<br><sub>0,13,3,-,-</sub> |  | 0.9<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.3<br><sub>0,3,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Alex Karaban (SAC) | 48% | 7.6<br><sub>-,29,4,-,-</sub> | 1.5<br><sub>-,0,0,-,-</sub> |  | 1.1<br><sub>-,5,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.0 |
| Mason Plumlee (SAC) | 48% | 6.1<br><sub>-,5,4,-,-</sub> | 1.8<br><sub>-,2,0,-,-</sub> |  | 2.0<br><sub>-,0,2,-,-</sub> |  | 0.6<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.5 |
| Devin Vassell (SAS) | 99% | 33.4<br><sub>23,32,36,32,26</sub> | 15.9<br><sub>7,6,12,15,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>2,6,5,4,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.7<br><sub>2,1,4,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.5 | 1.1 | 24.1 |
| Stephon Castle (SAS) | 99% | 32.7<br><sub>25,35,31,33,29</sub> | 20.4<br><sub>32,20,10,21,19</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,4,2,6,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 8.0<br><sub>6,9,7,12,6</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>5,0,2,2,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.2 | 3.0 | 33.6 |
| Victor Wembanyama (SAS) | 100% | 32.6<br><sub>21,35,34,33,32</sub> | 32.0<br><sub>12,26,25,32,50</sub> | 29.5 · – | 12.1<br><sub>12,10,18,11,19</sub> | 11.5 | 4.5<br><sub>6,6,4,3,1</sub> | 3.5 | 2.3<br><sub>0,4,1,2,5</sub> | 1.5 | 1.2 | 3.3 | 2.9 | 48.6 |
| Julian Champagnie (SAS) | 99% | 29.5<br><sub>23,24,30,29,25</sub> | 11.9<br><sub>7,4,14,20,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>8,5,6,4,3</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>3,1,0,1,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>1,1,4,4,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.5 | 0.8 | 18.7 |
| Keldon Johnson (SAS) | 99% | 26.5<br><sub>25,29,15,27,23</sub> | 12.2<br><sub>18,11,4,10,10</sub> |  | 5.4<br><sub>4,10,2,5,4</sub> |  | 2.7<br><sub>4,2,1,3,4</sub> |  | 0.8<br><sub>2,1,0,0,2</sub> |  | 0.8 | 0.2 | 1.1 | 20.3 |
| Harrison Barnes (SAS) | 93% | 22.2<br><sub>21,14,10,16,21</sub> | 7.9<br><sub>11,0,0,9,3</sub> |  | 2.5<br><sub>1,0,3,2,5</sub> |  | 1.6<br><sub>1,2,4,1,2</sub> |  | 1.1<br><sub>3,0,0,1,0</sub> |  | 0.5 | 0.2 | 0.6 | 12.0 |
| Carter Bryant (SAS) | 96% | 18.9<br><sub>19,5,2,13,20</sub> | 6.7<br><sub>8,0,0,3,8</sub> |  | 2.8<br><sub>3,1,0,1,3</sub> |  | 1.3<br><sub>2,0,0,0,0</sub> |  | 1.0<br><sub>2,0,0,1,2</sub> |  | 0.4 | 0.4 | 0.8 | 10.7 |
| Luke Kornet (SAS) | 99% | 18.6<br><sub>16,13,14,15,10</sub> | 4.4<br><sub>6,2,2,4,0</sub> |  | 5.1<br><sub>7,2,1,0,3</sub> |  | 1.7<br><sub>2,0,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.5 | 11.2 |
| Tarris Reed Jr. (SAS) | 58% | 12.7<br><sub>11,-,-,-,6</sub> | 4.1<br><sub>2,-,-,-,0</sub> |  | 5.3<br><sub>4,-,-,-,4</sub> |  | 0.8<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.7 | 10.1 |
| David Jones Garcia (SAS) | 58% | 11.0<br><sub>-,-,-,-,4</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.2 | 0.6 | 7.7 |
| Ja'Kobi Gillespie (SAS) | 88% | 10.8<br><sub>-,-,-,-,-</sub> | 5.7<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.9 |
| Maliq Brown (SAS) | 80% | 9.2<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-23/`._
