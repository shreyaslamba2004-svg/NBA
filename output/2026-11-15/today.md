# NBA model · Sun 15 Nov 2026 (US date)

Updated **Mon 16 Nov, 03:04 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-15/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander REB over 3.5 (4+) | OKC @ SAC | draftkings | 2.21 | 1.99 | 1.91 | 52.5% | 50.0% | 50.3% | +11.2% | +16.0% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant PRA over 49.5 (50+) | HOU @ WAS | draftkings | 21.00 | 16.72 | 6.23 | 16.0% | 4.5% | 6.0% | +25.6% | +236.8% | 0.3% |
| Kevin Durant PR over 44.5 (45+) | HOU @ WAS | draftkings | 20.80 | 17.39 | 7.13 | 14.0% | 4.5% | 5.8% | +19.6% | +191.7% | 0.2% |
| Alperen Sengun PTS over 39.5 (40+) | HOU @ WAS | draftkings | 30.00 | 26.46 | 12.24 | 8.2% | 3.1% | 3.8% | +13.5% | +145.2% | 0.1% |
| Kevin Durant AST over 7.5 (8+) | HOU @ WAS | draftkings | 11.20 | 10.02 | 4.82 | 20.8% | 8.3% | 10.0% | +11.8% | +132.4% | 0.3% |
| Kevin Durant AST over 9.5 (10+) | HOU @ WAS | draftkings | 29.00 | 26.60 | 13.64 | 7.3% | 3.2% | 3.8% | +9.2% | +112.6% | 0.1% |
| Alperen Sengun PR over 44.5 (45+) | HOU @ WAS | draftkings | 10.40 | 9.59 | 5.03 | 19.9% | 9.0% | 10.4% | +8.4% | +106.9% | 0.2% |
| Alperen Sengun PR over 49.5 (50+) | HOU @ WAS | draftkings | 19.20 | 17.73 | 9.31 | 10.7% | 4.9% | 5.6% | +8.3% | +106.2% | 0.1% |
| Tyrese Maxey AST over 9.5 (10+) | IND @ PHI | draftkings | 14.00 | 13.07 | 7.13 | 14.0% | 6.7% | 7.6% | +7.0% | +96.5% | 0.1% |
| WAS to win | HOU @ WAS | sportsbet | 4.25 | 3.97 | 4.07 | 24.6% | 25.2% | 25.2% | +6.9% | +4.5% | 0.5% |
| UTA to win | SAS @ UTA | betfair_ex_au | 10.50 | 9.88 | 7.34 | 13.6% | 10.1% | 10.1% | +6.3% | +43.0% | 0.2% |
| Pascal Siakam PRA over 49.5 (50+) | IND @ PHI | draftkings | 17.20 | 16.18 | 9.04 | 11.1% | 5.4% | 6.2% | +6.2% | +90.3% | 0.1% |
| Tari Eason REB over 11.5 (12+) | HOU @ WAS | draftkings | 15.00 | 14.20 | 8.08 | 12.4% | 6.2% | 7.0% | +5.6% | +85.7% | 0.1% |
| Pascal Siakam PTS over 39.5 (40+) | IND @ PHI | draftkings | 28.00 | 26.53 | 15.12 | 6.6% | 3.3% | 3.8% | +5.6% | +85.2% | 0.1% |
| Pascal Siakam PTS over 34.5 (35+) | IND @ PHI | draftkings | 13.60 | 12.90 | 7.41 | 13.5% | 6.9% | 7.8% | +5.4% | +83.6% | 0.1% |
| LeBron James PTS over 34.5 (35+) | IND @ PHI | draftkings | 29.00 | 27.55 | 15.86 | 6.3% | 3.2% | 3.6% | +5.3% | +82.9% | 0.1% |
| VJ Edgecombe AST over 5.5 (6+) | IND @ PHI | draftkings | 7.30 | 6.95 | 4.03 | 24.8% | 12.8% | 14.4% | +5.0% | +81.2% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| IND @ PHI | Mon 16 Nov 05:00 | 109.5–116.0 | IND 32% | 3.09 / 1.48 | PHI -6.5 | 225.5 | PHI -7.5 covers 47%; o225.5 50% |
| LAL @ PHX | Mon 16 Nov 08:00 | 112.2–112.1 | LAL 50% | 2.00 / 2.00 | PHX +0.5 | 224.5 | PHX +2.5 covers 56%; o228.5 41% |
| CHA @ LAC | Mon 16 Nov 08:30 | 108.7–111.6 | CHA 42% | 2.37 / 1.73 | LAC -3.5 | 220.5 | LAC +1.5 covers 61%; o214.5 62% |
| SAS @ UTA | Mon 16 Nov 09:00 | 122.6–107.2 | SAS 86% | 1.16 / 7.34 | UTA +15.5 | 229.5 | UTA +16.5 covers 53%; o226.5 57% |
| DAL @ BOS | Mon 16 Nov 10:00 | 107.0–119.9 | DAL 18% | 5.67 / 1.21 | BOS -12.5 | 226.5 | BOS -13.5 covers 48%; o219.5 66% |
| NYK @ TOR | Mon 16 Nov 10:00 | 114.3–107.9 | NYK 67% | 1.48 / 3.07 | TOR +6.5 | 221.5 | TOR +4.5 covers 44%; o217.5 59% |
| HOU @ WAS | Mon 16 Nov 11:00 | 120.2–109.4 | HOU 78% | 1.28 / 4.52 | WAS +10.5 | 229.5 | WAS +8.5 covers 43%; o223.5 63% |
| ATL @ MIL | Mon 16 Nov 12:00 | 119.3–111.6 | ATL 71% | 1.41 / 3.44 | MIL +7.5 | 230.5 | MIL +7.5 covers 49%; o234.5 42% |
| OKC @ SAC | Mon 16 Nov 13:00 | 119.9–107.2 | OKC 82% | 1.23 / 5.40 | SAC +12.5 | 226.5 | SAC +10.5 covers 44%; o222.5 60% |

### IND @ PHI
Out: Dominick Barlow (PHI), Adem Bona (PHI), Joel Embiid (PHI), Ariel Hukporti (PHI), Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.5–116.0 | IND 32% | 3.09 / 1.48 | PHI -6.5 | 225.5 | PHI -7.5 covers 47%; o225.5 50% |
| Expected (weighted by chance each plays) | 110.9–115.8 | IND 37% | 2.72 / 1.58 | PHI -5.5 | 226.5 | PHI -7.5 covers 43%; o225.5 52% |
| if Andrew Nembhard plays | 111.3–115.7 | IND 38% | 2.64 / 1.61 | PHI -4.5 | 226.5 | PHI -7.5 covers 42%; o225.5 52% |
| if Aaron Nesmith plays | 110.1–115.7 | IND 35% | 2.89 / 1.53 | PHI -5.5 | 225.5 | PHI -7.5 covers 45%; o225.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | Questionable | 55% | 34.5 | 18.3 | 3.2 | 8.9 | 2.0 | 0.9 | 0.2 | 2.8 | 30.4 | full tables below |
| Aaron Nesmith (IND) | Questionable | 55% | 31.2 | 15.7 | 4.0 | 2.3 | 2.1 | 0.8 | 0.5 | 1.8 | 22.0 | full tables below |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 91% | 34.1<br><sub>30,32,35,32,32</sub> | 24.9<br><sub>20,23,29,28,19</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>4,2,9,8,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>2,5,8,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>2,2,5,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.5 | 2.7 | 36.9 |
| Kelly Oubre Jr. | 86% | 31.1<br><sub>-,16,23,34,30</sub> | 13.9<br><sub>-,2,14,14,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>-,1,2,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>-,0,2,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>-,0,1,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.6 | 1.6 | 20.5 |
| Ivica Zubac | 72% | 28.5<br><sub>19,19,28,31,26</sub> | 13.1<br><sub>1,10,16,20,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 10.6<br><sub>4,12,3,12,13</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,5,0,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 1.7 | 26.0 |
| Quenton Jackson | 98% | 26.9<br><sub>22,17,25,21,20</sub> | 12.2<br><sub>13,6,10,4,3</sub> |  | 3.8<br><sub>7,4,5,2,5</sub> |  | 4.6<br><sub>2,1,4,2,4</sub> |  | 1.2<br><sub>3,0,2,1,1</sub> |  | 1.1 | 0.2 | 2.0 | 20.6 |
| Obi Toppin | 83% | 22.0<br><sub>19,22,19,16,16</sub> | 12.9<br><sub>11,10,10,8,9</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>5,7,2,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>1,2,4,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,2,0,2,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.5 | 0.3 | 1.3 | 20.0 |
| Kobe Brown | 72% | 21.1<br><sub>7,-,-,-,-</sub> | 8.1<br><sub>0,-,-,-,-</sub> |  | 3.8<br><sub>1,-,-,-,-</sub> |  | 2.1<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.6 | 0.2 | 1.2 | 14.0 |
| Jarace Walker | 76% | 20.4<br><sub>17,20,10,7,-</sub> | 9.1<br><sub>2,9,7,1,-</sub> |  | 4.6<br><sub>8,5,1,1,-</sub> |  | 2.2<br><sub>1,2,0,0,-</sub> |  | 1.2<br><sub>0,1,2,0,-</sub> |  | 0.6 | 0.3 | 1.5 | 15.9 |
| T.J. McConnell | 91% | 19.5<br><sub>-,9,8,14,17</sub> | 10.1<br><sub>-,6,2,7,6</sub> |  | 2.6<br><sub>-,2,0,3,3</sub> |  | 6.2<br><sub>-,1,3,7,7</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.9 | 0.2 | 1.7 | 19.0 |
| Braden Smith | 67% | 18.7<br><sub>24,12,10,-,-</sub> | 6.2<br><sub>10,0,0,-,-</sub> |  | 1.8<br><sub>1,0,0,-,-</sub> |  | 3.7<br><sub>5,2,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.8 | 0.3 | 1.3 | 11.7 |
| Jay Huff | 86% | 18.6<br><sub>14,10,-,11,8</sub> | 8.1<br><sub>6,0,-,6,8</sub> |  | 3.6<br><sub>3,3,-,4,1</sub> |  | 1.5<br><sub>1,0,-,0,0</sub> |  | 1.0<br><sub>2,0,-,0,2</sub> |  | 0.4 | 1.1 | 0.9 | 13.2 |
| Jalen Slawson | 86% | 16.8<br><sub>6,12,-,12,10</sub> | 5.0<br><sub>2,4,-,2,1</sub> |  | 3.4<br><sub>2,1,-,3,4</sub> |  | 1.6<br><sub>1,2,-,1,0</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.8 | 0.6 | 0.9 | 10.0 |
| Larry Nance Jr. | 96% | 16.7<br><sub>14,13,14,5,14</sub> | 5.6<br><sub>4,15,4,5,2</sub> |  | 3.3<br><sub>4,2,0,0,2</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 0.7<br><sub>0,5,0,1,0</sub> |  | 0.7 | 0.3 | 0.7 | 9.9 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.5<br><sub>34,32,36,34,35</sub> | 28.4<br><sub>19,17,27,24,27</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>1,3,4,1,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>7,4,7,4,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>3,2,3,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6 | 0.6 | 2.3 | 39.0 |
| Jaylen Brown | 98% | 36.4<br><sub>37,34,35,26,36</sub> | 26.3<br><sub>30,20,29,13,18</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>7,5,7,5,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,5,4,2,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,2,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.5 | 3.1 | 37.8 |
| VJ Edgecombe | 96% | 36.1<br><sub>35,32,35,32,36</sub> | 14.7<br><sub>11,19,13,8,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>6,3,6,4,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>3,2,3,5,8</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 1.9<br><sub>1,3,3,0,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.5 | 1.4 | 25.4 |
| LeBron James | 98% | 35.0<br><sub>33,32,33,29,-</sub> | 20.6<br><sub>13,8,22,11,-</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>10,7,5,8,-</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.9<br><sub>8,3,5,5,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>1,0,2,1,-</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.7 | 3.0 | 35.1 |
| Dean Wade | 96% | 28.6<br><sub>22,21,18,23,34</sub> | 5.0<br><sub>3,0,0,8,6</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,5,1,9,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,1,1,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>0,0,0,2,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.0 | 0.3 | 0.8 | 11.5 |
| Kentavious Caldwell-Pope | 98% | 23.3<br><sub>21,17,21,16,27</sub> | 5.7<br><sub>5,5,6,0,11</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>1,2,6,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>0,0,3,2,5</sub> |  | 0.8<br><sub>1,1,2,0,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 0.7 | 10.2 |
| Anfernee Simons | 98% | 22.6<br><sub>10,19,16,18,23</sub> | 10.2<br><sub>0,6,3,17,17</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,2,4,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>0,2,2,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>0,1,1,3,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.1 | 0.8 | 14.3 |
| Jabari Walker | 88% | 15.2<br><sub>-,17,19,15,16</sub> | 5.6<br><sub>-,8,9,2,9</sub> |  | 4.9<br><sub>-,5,11,4,8</sub> |  | 0.7<br><sub>-,1,0,0,1</sub> |  | 0.5<br><sub>-,0,1,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 11.2 |
| Rayan Rupert | 47% | 9.6<br><sub>-,-,-,6,-</sub> | 3.3<br><sub>-,-,-,0,-</sub> |  | 1.9<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.1 | 0.5 | 5.8 |
| Tacko Fall | 67% | 8.2<br><sub>-,3,-,-,1</sub> | 0.4<br><sub>-,0,-,-,0</sub> |  | 2.2<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.4 | 0.3 | 2.9 |
| Justin Edwards | 64% | 7.9<br><sub>-,4,-,6,1</sub> | 3.0<br><sub>-,3,-,0,0</sub> |  | 1.1<br><sub>-,1,-,0,1</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.3<br><sub>-,1,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Labaron Philon Jr. | 67% | 7.9<br><sub>-,4,-,6,2</sub> | 3.2<br><sub>-,3,-,2,0</sub> |  | 1.2<br><sub>-,1,-,1,0</sub> |  | 0.8<br><sub>-,1,-,3,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Caleb Love | 48% | 7.9<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |

</details>

<details><summary>if Andrew Nembhard plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 100% | 34.5<br><sub>38,31,34,34,34</sub> | 18.3<br><sub>22,9,12,17,12</sub> | 15.5 · – | 3.2<br><sub>2,1,3,2,4</sub> | 2.5 | 8.9<br><sub>5,8,12,10,6</sub> | 7.5 | 2.0<br><sub>2,3,1,3,1</sub> | 2.5 | 0.9 | 0.2 | 2.8 | 30.4 |
| Pascal Siakam (IND) | 91% | 33.4<br><sub>30,32,35,32,32</sub> | 24.2<br><sub>20,23,29,28,19</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>4,2,9,8,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>2,5,8,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>2,2,5,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.4 | 2.3 | 35.6 |
| Kelly Oubre Jr. (IND) | 86% | 28.2<br><sub>-,16,23,34,30</sub> | 12.0<br><sub>-,2,14,14,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>-,1,2,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>-,0,2,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>-,0,1,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 1.2 | 17.9 |
| Ivica Zubac (IND) | 72% | 26.6<br><sub>19,19,28,31,26</sub> | 12.2<br><sub>1,10,16,20,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 9.9<br><sub>4,12,3,12,13</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>2,5,0,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.5 | 24.0 |
| Quenton Jackson (IND) | 98% | 23.4<br><sub>22,17,25,21,20</sub> | 10.2<br><sub>13,6,10,4,3</sub> |  | 3.4<br><sub>7,4,5,2,5</sub> |  | 3.5<br><sub>2,1,4,2,4</sub> |  | 0.9<br><sub>3,0,2,1,1</sub> |  | 0.9 | 0.2 | 1.5 | 17.1 |
| Obi Toppin (IND) | 83% | 19.0<br><sub>19,22,19,16,16</sub> | 11.3<br><sub>11,10,10,8,9</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>5,7,2,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>1,2,4,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,2,0,2,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.4 | 0.2 | 1.1 | 17.4 |
| Jarace Walker (IND) | 76% | 16.9<br><sub>17,20,10,7,-</sub> | 7.4<br><sub>2,9,7,1,-</sub> |  | 3.8<br><sub>8,5,1,1,-</sub> |  | 1.6<br><sub>1,2,0,0,-</sub> |  | 0.9<br><sub>0,1,2,0,-</sub> |  | 0.5 | 0.3 | 1.1 | 12.8 |
| T.J. McConnell (IND) | 91% | 16.5<br><sub>-,9,8,14,17</sub> | 8.4<br><sub>-,6,2,7,6</sub> |  | 2.3<br><sub>-,2,0,3,3</sub> |  | 5.1<br><sub>-,1,3,7,7</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.2 | 1.3 | 15.8 |
| Kobe Brown (IND) | 72% | 15.9<br><sub>7,-,-,-,-</sub> | 5.9<br><sub>0,-,-,-,-</sub> |  | 2.9<br><sub>1,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.6<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.9 | 10.2 |
| Jay Huff (IND) | 86% | 15.0<br><sub>14,10,-,11,8</sub> | 6.5<br><sub>6,0,-,6,8</sub> |  | 3.0<br><sub>3,3,-,4,1</sub> |  | 1.1<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>2,0,-,0,2</sub> |  | 0.3 | 1.0 | 0.7 | 10.5 |
| Larry Nance Jr. (IND) | 96% | 13.5<br><sub>14,13,14,5,14</sub> | 4.3<br><sub>4,15,4,5,2</sub> |  | 2.7<br><sub>4,2,0,0,2</sub> |  | 0.8<br><sub>1,1,0,0,1</sub> |  | 0.5<br><sub>0,5,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.7 |
| Jalen Slawson (IND) | 86% | 13.2<br><sub>6,12,-,12,10</sub> | 3.9<br><sub>2,4,-,2,1</sub> |  | 2.7<br><sub>2,1,-,3,4</sub> |  | 1.2<br><sub>1,2,-,1,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.6 | 0.5 | 0.7 | 7.8 |
| Braden Smith (IND) | 67% | 13.0<br><sub>24,12,10,-,-</sub> | 4.1<br><sub>10,0,0,-,-</sub> |  | 1.3<br><sub>1,0,0,-,-</sub> |  | 2.3<br><sub>5,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.6 | 0.2 | 0.9 | 7.7 |
| Tyrese Maxey (PHI) | 98% | 38.5<br><sub>34,32,36,34,35</sub> | 28.3<br><sub>19,17,27,24,27</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>1,3,4,1,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>7,4,7,4,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>3,2,3,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6 | 0.6 | 2.3 | 38.9 |
| Jaylen Brown (PHI) | 98% | 36.4<br><sub>37,34,35,26,36</sub> | 26.4<br><sub>30,20,29,13,18</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>7,5,7,5,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,5,4,2,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,2,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.5 | 3.1 | 37.7 |
| VJ Edgecombe (PHI) | 96% | 36.1<br><sub>35,32,35,32,36</sub> | 14.7<br><sub>11,19,13,8,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>6,3,6,4,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>3,2,3,5,8</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 1.9<br><sub>1,3,3,0,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.5 | 1.4 | 25.3 |
| LeBron James (PHI) | 98% | 34.9<br><sub>33,32,33,29,-</sub> | 20.5<br><sub>13,8,22,11,-</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>10,7,5,8,-</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.9<br><sub>8,3,5,5,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,0,2,1,-</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.7 | 3.0 | 35.0 |
| Dean Wade (PHI) | 96% | 28.7<br><sub>22,21,18,23,34</sub> | 5.0<br><sub>3,0,0,8,6</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,5,1,9,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,1,1,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>0,0,0,2,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.0 | 0.3 | 0.8 | 11.6 |
| Kentavious Caldwell-Pope (PHI) | 98% | 23.4<br><sub>21,17,21,16,27</sub> | 5.7<br><sub>5,5,6,0,11</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>1,2,6,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>0,0,3,2,5</sub> |  | 0.8<br><sub>1,1,2,0,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 0.7 | 10.2 |
| Anfernee Simons (PHI) | 98% | 22.5<br><sub>10,19,16,18,23</sub> | 10.0<br><sub>0,6,3,17,17</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,2,4,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>0,2,2,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>0,1,1,3,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.1 | 0.8 | 14.2 |
| Jabari Walker (PHI) | 88% | 15.2<br><sub>-,17,19,15,16</sub> | 5.6<br><sub>-,8,9,2,9</sub> |  | 4.8<br><sub>-,5,11,4,8</sub> |  | 0.7<br><sub>-,1,0,0,1</sub> |  | 0.4<br><sub>-,0,1,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 11.1 |
| Rayan Rupert (PHI) | 47% | 9.6<br><sub>-,-,-,6,-</sub> | 3.3<br><sub>-,-,-,0,-</sub> |  | 1.9<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.1 | 0.5 | 5.8 |
| Tacko Fall (PHI) | 67% | 8.2<br><sub>-,3,-,-,1</sub> | 0.4<br><sub>-,0,-,-,0</sub> |  | 2.2<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.4 | 0.3 | 2.9 |
| Justin Edwards (PHI) | 64% | 8.0<br><sub>-,4,-,6,1</sub> | 3.0<br><sub>-,3,-,0,0</sub> |  | 1.1<br><sub>-,1,-,0,1</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.3<br><sub>-,1,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Labaron Philon Jr. (PHI) | 67% | 8.0<br><sub>-,4,-,6,2</sub> | 3.3<br><sub>-,3,-,2,0</sub> |  | 1.2<br><sub>-,1,-,1,0</sub> |  | 0.8<br><sub>-,1,-,3,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Caleb Love (PHI) | 48% | 7.9<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |

</details>

<details><summary>if Aaron Nesmith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam (IND) | 91% | 33.6<br><sub>30,32,35,32,32</sub> | 24.0<br><sub>20,23,29,28,19</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>4,2,9,8,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>2,5,8,5,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>2,2,5,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.4 | 2.5 | 36.1 |
| Aaron Nesmith (IND) | 100% | 31.2<br><sub>30,27,34,22,33</sub> | 15.7<br><sub>16,8,18,2,18</sub> | 13.5 · – | 4.0<br><sub>2,5,2,1,7</sub> | 3.5 | 2.3<br><sub>2,1,2,1,1</sub> | 1.5 | 2.1<br><sub>2,2,4,0,2</sub> | 2.5 | 0.8 | 0.5 | 1.8 | 22.0 |
| Kelly Oubre Jr. (IND) | 86% | 28.8<br><sub>-,16,23,34,30</sub> | 12.6<br><sub>-,2,14,14,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>-,1,2,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>-,0,2,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>-,0,1,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 1.3 | 18.8 |
| Ivica Zubac (IND) | 72% | 27.2<br><sub>19,19,28,31,26</sub> | 12.2<br><sub>1,10,16,20,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>4,12,3,12,13</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,5,0,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 1.6 | 24.5 |
| Quenton Jackson (IND) | 98% | 24.1<br><sub>22,17,25,21,20</sub> | 10.7<br><sub>13,6,10,4,3</sub> |  | 3.5<br><sub>7,4,5,2,5</sub> |  | 4.0<br><sub>2,1,4,2,4</sub> |  | 1.0<br><sub>3,0,2,1,1</sub> |  | 0.9 | 0.2 | 1.6 | 18.2 |
| Obi Toppin (IND) | 83% | 19.9<br><sub>19,22,19,16,16</sub> | 11.7<br><sub>11,10,10,8,9</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>5,7,2,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,2,4,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>1,2,0,2,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.4 | 0.3 | 1.2 | 18.3 |
| Jarace Walker (IND) | 76% | 17.8<br><sub>17,20,10,7,-</sub> | 7.8<br><sub>2,9,7,1,-</sub> |  | 4.0<br><sub>8,5,1,1,-</sub> |  | 1.8<br><sub>1,2,0,0,-</sub> |  | 1.0<br><sub>0,1,2,0,-</sub> |  | 0.5 | 0.3 | 1.2 | 13.6 |
| Kobe Brown (IND) | 72% | 17.5<br><sub>7,-,-,-,-</sub> | 6.6<br><sub>0,-,-,-,-</sub> |  | 3.2<br><sub>1,-,-,-,-</sub> |  | 1.6<br><sub>0,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 11.4 |
| T.J. McConnell (IND) | 91% | 16.9<br><sub>-,9,8,14,17</sub> | 8.7<br><sub>-,6,2,7,6</sub> |  | 2.4<br><sub>-,2,0,3,3</sub> |  | 5.5<br><sub>-,1,3,7,7</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.2 | 1.5 | 16.5 |
| Jay Huff (IND) | 86% | 15.8<br><sub>14,10,-,11,8</sub> | 6.7<br><sub>6,0,-,6,8</sub> |  | 3.1<br><sub>3,3,-,4,1</sub> |  | 1.2<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>2,0,-,0,2</sub> |  | 0.3 | 1.0 | 0.8 | 10.9 |
| Braden Smith (IND) | 67% | 14.2<br><sub>24,12,10,-,-</sub> | 4.6<br><sub>10,0,0,-,-</sub> |  | 1.4<br><sub>1,0,0,-,-</sub> |  | 2.8<br><sub>5,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.7 | 0.3 | 1.0 | 8.8 |
| Larry Nance Jr. (IND) | 96% | 14.0<br><sub>14,13,14,5,14</sub> | 4.5<br><sub>4,15,4,5,2</sub> |  | 2.8<br><sub>4,2,0,0,2</sub> |  | 0.8<br><sub>1,1,0,0,1</sub> |  | 0.5<br><sub>0,5,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.1 |
| Jalen Slawson (IND) | 86% | 13.7<br><sub>6,12,-,12,10</sub> | 4.0<br><sub>2,4,-,2,1</sub> |  | 2.8<br><sub>2,1,-,3,4</sub> |  | 1.3<br><sub>1,2,-,1,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.6 | 0.5 | 0.7 | 8.0 |
| Tyrese Maxey (PHI) | 98% | 38.5<br><sub>34,32,36,34,35</sub> | 28.3<br><sub>19,17,27,24,27</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>1,3,4,1,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>7,4,7,4,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>3,2,3,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6 | 0.6 | 2.3 | 38.9 |
| Jaylen Brown (PHI) | 98% | 36.4<br><sub>37,34,35,26,36</sub> | 26.4<br><sub>30,20,29,13,18</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>7,5,7,5,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,5,4,2,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,2,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.5 | 3.1 | 37.8 |
| VJ Edgecombe (PHI) | 96% | 36.2<br><sub>35,32,35,32,36</sub> | 14.6<br><sub>11,19,13,8,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>6,3,6,4,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>3,2,3,5,8</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 1.9<br><sub>1,3,3,0,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.5 | 1.5 | 25.4 |
| LeBron James (PHI) | 98% | 35.0<br><sub>33,32,33,29,-</sub> | 20.5<br><sub>13,8,22,11,-</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>10,7,5,8,-</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.9<br><sub>8,3,5,5,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,0,2,1,-</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.7 | 3.0 | 35.0 |
| Dean Wade (PHI) | 96% | 28.6<br><sub>22,21,18,23,34</sub> | 5.0<br><sub>3,0,0,8,6</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,5,1,9,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,1,1,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>0,0,0,2,2</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.0 | 0.3 | 0.8 | 11.5 |
| Kentavious Caldwell-Pope (PHI) | 98% | 23.3<br><sub>21,17,21,16,27</sub> | 5.7<br><sub>5,5,6,0,11</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>1,2,6,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>0,0,3,2,5</sub> |  | 0.8<br><sub>1,1,2,0,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.3 | 0.7 | 10.2 |
| Anfernee Simons (PHI) | 98% | 22.5<br><sub>10,19,16,18,23</sub> | 10.1<br><sub>0,6,3,17,17</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,2,4,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>0,2,2,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>0,1,1,3,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.1 | 0.8 | 14.2 |
| Jabari Walker (PHI) | 88% | 15.3<br><sub>-,17,19,15,16</sub> | 5.7<br><sub>-,8,9,2,9</sub> |  | 4.9<br><sub>-,5,11,4,8</sub> |  | 0.7<br><sub>-,1,0,0,1</sub> |  | 0.4<br><sub>-,0,1,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 11.3 |
| Rayan Rupert (PHI) | 47% | 9.6<br><sub>-,-,-,6,-</sub> | 3.3<br><sub>-,-,-,0,-</sub> |  | 1.9<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.1 | 0.5 | 5.9 |
| Tacko Fall (PHI) | 67% | 8.2<br><sub>-,3,-,-,1</sub> | 0.4<br><sub>-,0,-,-,0</sub> |  | 2.2<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.4 | 0.3 | 2.9 |
| Justin Edwards (PHI) | 64% | 7.9<br><sub>-,4,-,6,1</sub> | 3.0<br><sub>-,3,-,0,0</sub> |  | 1.1<br><sub>-,1,-,0,1</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.3<br><sub>-,1,-,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 4.5 |
| Caleb Love (PHI) | 48% | 7.9<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |
| Labaron Philon Jr. (PHI) | 67% | 7.9<br><sub>-,4,-,6,2</sub> | 3.2<br><sub>-,3,-,2,0</sub> |  | 1.2<br><sub>-,1,-,1,0</sub> |  | 0.8<br><sub>-,1,-,3,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |

</details>


### LAL @ PHX
Out: Mark Williams (PHX), Austin Reaves (LAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.2–112.1 | LAL 50% | 2.00 / 2.00 | PHX +0.5 | 224.5 | PHX +2.5 covers 56%; o228.5 41% |
| Expected (weighted by chance each plays) | 113.6–111.6 | LAL 55% | 1.80 / 2.24 | PHX +2.5 | 224.5 | PHX +2.5 covers 51%; o228.5 43% |
| if Collin Sexton plays | 113.8–111.2 | LAL 57% | 1.75 / 2.34 | PHX +2.5 | 224.5 | PHX +2.5 covers 49%; o228.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Sexton (LAL) | Questionable | 55% | 21.1 | 12.3 | 2.3 | 2.6 | 1.3 | 0.9 | 0.2 | 1.8 | 17.3 | full tables below |
| Adou Thiero (LAL) | Questionable | 55% | 12.8 | 4.1 | 3.3 | 0.8 | 0.1 | 0.5 | 0.2 | 0.8 | 8.2 | small |
| Drew Timme (PHX) | Day-To-Day | 70% | 6.4 | 2.5 | 1.1 | 0.6 | 0.1 | 0.2 | 0.1 | 0.4 | 4.2 | small |
| Bronny James (LAL) | Questionable | 55% | 7.6 | 2.1 | 0.2 | 0.6 | 0.1 | 0.3 | 0.2 | 0.4 | 2.9 | small |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 37.7<br><sub>35,38,-,39,32</sub> | 38.6<br><sub>40,53,-,32,32</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>9,5,-,8,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>7,5,-,10,5</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>6,5,-,3,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.9 | 0.6 | 5.5 | 54.6 |
| Walker Kessler | 98% | 32.4<br><sub>29,37,29,30,29</sub> | 14.1<br><sub>15,16,12,21,10</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.4<br><sub>8,12,16,10,11</sub> | 10.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>0,2,4,4,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.9 | 2.2 | 2.2 | 28.5 |
| Quentin Grimes | 98% | 29.3<br><sub>25,20,32,-,-</sub> | 11.2<br><sub>6,2,12,-,-</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>1,0,1,-,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>1,0,4,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>0,0,2,-,-</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.8 | 17.4 |
| Matisse Thybulle | 98% | 27.9<br><sub>23,24,28,23,23</sub> | 8.2<br><sub>3,2,4,6,8</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>1,2,2,0,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,0,0,1,1</sub> |  | 1.4<br><sub>1,0,0,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.4 | 0.7 | 1.3 | 12.4 |
| Jake LaRavia | 98% | 27.5<br><sub>21,25,29,32,21</sub> | 7.3<br><sub>9,7,5,4,0</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>2,8,1,3,9</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>2,3,2,3,6</sub> |  | 0.7<br><sub>2,2,0,0,0</sub> |  | 1.3 | 0.6 | 1.4 | 14.1 |
| Sandro Mamukelashvili | 98% | 26.4<br><sub>19,20,18,32,26</sub> | 12.0<br><sub>2,7,7,23,23</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>6,3,3,8,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>1,1,0,3,2</sub> |  | 1.5<br><sub>0,1,1,5,5</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 1.1 | 19.6 |
| Ziaire Williams | 98% | 26.1<br><sub>23,20,21,28,20</sub> | 10.6<br><sub>10,8,17,12,9</sub> |  | 3.1<br><sub>4,3,2,2,1</sub> |  | 1.7<br><sub>1,1,0,2,5</sub> |  | 1.4<br><sub>1,2,4,2,1</sub> |  | 1.5 | 0.3 | 1.1 | 15.5 |
| Jarred Vanderbilt | 80% | 14.7<br><sub>7,-,14,13,9</sub> | 3.1<br><sub>0,-,2,4,4</sub> |  | 4.0<br><sub>1,-,10,2,3</sub> |  | 1.1<br><sub>0,-,3,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.2 | 0.8 | 8.2 |
| Jaden Hardy | 58% | 11.5<br><sub>1,-,-,-,4</sub> | 6.0<br><sub>0,-,-,-,3</sub> |  | 1.1<br><sub>0,-,-,-,1</sub> |  | 0.8<br><sub>1,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.8 | 7.8 |
| Kevon Looney | 43% | 9.5<br><sub>-,-,-,-,4</sub> | 1.9<br><sub>-,-,-,-,0</sub> |  | 3.4<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Chris Manon | 58% | 8.8<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 4.5 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Carson Cooper | 38% | 8.3<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 1.5 | 8.5 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.5<br><sub>34,39,29,29,35</sub> | 24.4<br><sub>30,24,32,17,30</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,2,2,3,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 5.9<br><sub>8,3,4,5,7</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>4,2,3,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 3.1 | 33.8 |
| Dillon Brooks | 98% | 30.4<br><sub>29,37,26,22,30</sub> | 16.4<br><sub>24,11,7,8,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,4,4,4,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>4,3,1,0,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 1.5 | 22.0 |
| Miles Bridges | 98% | 28.2<br><sub>31,31,26,18,25</sub> | 13.3<br><sub>18,13,7,8,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>13,10,5,4,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>5,7,0,2,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>3,1,0,2,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.4 | 1.3 | 22.0 |
| Jalen Green | 98% | 26.4<br><sub>24,34,24,21,21</sub> | 14.0<br><sub>6,16,6,13,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>0,3,5,5,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.9<br><sub>3,6,4,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 2.3 | 20.5 |
| Oso Ighodaro | 98% | 24.2<br><sub>24,23,18,20,32</sub> | 6.5<br><sub>2,4,7,6,2</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>5,6,4,8,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>1,3,2,2,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.4 | 15.3 |
| Collin Gillespie | 98% | 23.9<br><sub>24,20,24,22,27</sub> | 9.2<br><sub>6,7,6,12,13</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>2,3,2,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>2,4,3,8,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.2 | 1.2 | 15.8 |
| Luke Kennard | 98% | 18.6<br><sub>21,14,14,22,21</sub> | 7.4<br><sub>12,11,3,14,8</sub> |  | 1.8<br><sub>1,1,1,1,1</sub> |  | 1.8<br><sub>5,2,0,3,1</sub> |  | 1.0<br><sub>3,3,1,3,0</sub> |  | 0.7 | 0.1 | 0.8 | 11.1 |
| Jordan Goodwin | 98% | 18.0<br><sub>-,-,-,14,24</sub> | 7.2<br><sub>-,-,-,18,6</sub> |  | 3.6<br><sub>-,-,-,3,5</sub> |  | 1.7<br><sub>-,-,-,1,2</sub> |  | 1.1<br><sub>-,-,-,6,2</sub> |  | 1.3 | 0.1 | 0.8 | 12.4 |
| Khaman Maluach | 98% | 16.7<br><sub>22,18,20,22,16</sub> | 6.2<br><sub>8,8,11,11,4</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>6,10,5,7,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>2,0,2,3,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.8 | 1.0 | 12.0 |
| Ryan Dunn | 98% | 15.2<br><sub>25,23,23,25,10</sub> | 4.3<br><sub>11,8,3,10,0</sub> |  | 3.2<br><sub>3,5,2,8,4</sub> |  | 1.0<br><sub>3,3,0,2,0</sub> |  | 0.4<br><sub>1,2,1,1,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.6 |
| Rasheer Fleming | 52% | 8.1<br><sub>-,-,9,12,-</sub> | 3.1<br><sub>-,-,2,4,-</sub> |  | 1.4<br><sub>-,-,1,2,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,1,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.7 |
| Pat Spencer | 67% | 7.0<br><sub>2,-,6,-,-</sub> | 2.5<br><sub>0,-,2,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Jamaree Bouyea | 58% | 6.9<br><sub>2,-,9,8,-</sub> | 2.8<br><sub>0,-,4,7,-</sub> |  | 0.9<br><sub>0,-,0,1,-</sub> |  | 1.2<br><sub>0,-,3,3,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.9 |
| Koa Peat | 58% | 6.4<br><sub>2,-,6,6,-</sub> | 2.6<br><sub>0,-,4,5,-</sub> |  | 1.3<br><sub>1,-,0,1,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |
| Duop Reath | 58% | 6.2<br><sub>2,-,6,-,-</sub> | 2.7<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>

<details><summary>if Collin Sexton plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 37.1<br><sub>35,38,-,39,32</sub> | 37.2<br><sub>40,53,-,32,32</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>9,5,-,8,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.2<br><sub>7,5,-,10,5</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>6,5,-,3,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8 | 0.6 | 5.0 | 53.0 |
| Walker Kessler (LAL) | 98% | 31.7<br><sub>29,37,29,30,29</sub> | 12.9<br><sub>15,16,12,21,10</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.3<br><sub>8,12,16,10,11</sub> | 10.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,2,4,4,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.9 | 2.2 | 2.0 | 27.1 |
| Quentin Grimes (LAL) | 98% | 27.7<br><sub>25,20,32,-,-</sub> | 9.9<br><sub>6,2,12,-,-</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,0,1,-,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>1,0,4,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>0,0,2,-,-</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.5 | 15.6 |
| Jake LaRavia (LAL) | 98% | 26.7<br><sub>21,25,29,32,21</sub> | 7.1<br><sub>9,7,5,4,0</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>2,8,1,3,9</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,3,2,3,6</sub> |  | 0.7<br><sub>2,2,0,0,0</sub> |  | 1.3 | 0.6 | 1.4 | 13.6 |
| Matisse Thybulle (LAL) | 98% | 26.6<br><sub>23,24,28,23,23</sub> | 7.2<br><sub>3,2,4,6,8</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,2,2,0,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>2,0,0,1,1</sub> |  | 1.2<br><sub>1,0,0,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.2 | 0.7 | 1.1 | 11.2 |
| Sandro Mamukelashvili (LAL) | 98% | 25.3<br><sub>19,20,18,32,26</sub> | 11.0<br><sub>2,7,7,23,23</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>6,3,3,8,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>1,1,0,3,2</sub> |  | 1.5<br><sub>0,1,1,5,5</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 1.0 | 18.2 |
| Ziaire Williams (LAL) | 98% | 25.1<br><sub>23,20,21,28,20</sub> | 9.9<br><sub>10,8,17,12,9</sub> |  | 3.0<br><sub>4,3,2,2,1</sub> |  | 1.6<br><sub>1,1,0,2,5</sub> |  | 1.4<br><sub>1,2,4,2,1</sub> |  | 1.4 | 0.3 | 1.0 | 14.4 |
| Collin Sexton (LAL) | 100% | 21.1<br><sub>16,11,24,27,13</sub> | 12.3<br><sub>10,0,17,18,10</sub> | 13.5 · – | 2.3<br><sub>3,0,2,2,1</sub> |  | 2.6<br><sub>1,1,2,6,3</sub> | 2.5 | 1.3<br><sub>1,0,0,3,0</sub> | 1.5 | 0.9 | 0.2 | 1.8 | 17.3 |
| Jarred Vanderbilt (LAL) | 80% | 12.7<br><sub>7,-,14,13,9</sub> | 2.8<br><sub>0,-,2,4,4</sub> |  | 3.5<br><sub>1,-,10,2,3</sub> |  | 1.0<br><sub>0,-,3,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 7.2 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jaden Hardy (LAL) | 58% | 8.0<br><sub>1,-,-,-,4</sub> | 4.0<br><sub>0,-,-,-,3</sub> |  | 0.7<br><sub>0,-,-,-,1</sub> |  | 0.6<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.3 |
| Kevon Looney (LAL) | 43% | 7.8<br><sub>-,-,-,-,4</sub> | 1.6<br><sub>-,-,-,-,0</sub> |  | 2.9<br><sub>-,-,-,-,2</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 5.0 |
| Carson Cooper (LAL) | 38% | 7.2<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 1.4 | 7.5 |
| Chris Manon (LAL) | 58% | 6.8<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.4 |
| Devin Booker (PHX) | 98% | 34.5<br><sub>34,39,29,29,35</sub> | 24.4<br><sub>30,24,32,17,30</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,2,2,3,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 5.9<br><sub>8,3,4,5,7</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>4,2,3,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 3.1 | 33.6 |
| Dillon Brooks (PHX) | 98% | 30.4<br><sub>29,37,26,22,30</sub> | 16.4<br><sub>24,11,7,8,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,4,4,4,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>4,3,1,0,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 1.5 | 22.1 |
| Miles Bridges (PHX) | 98% | 28.1<br><sub>31,31,26,18,25</sub> | 13.3<br><sub>18,13,7,8,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>13,10,5,4,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>5,7,0,2,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>3,1,0,2,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.4 | 1.3 | 21.9 |
| Jalen Green (PHX) | 98% | 26.4<br><sub>24,34,24,21,21</sub> | 14.0<br><sub>6,16,6,13,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>0,3,5,5,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.9<br><sub>3,6,4,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 2.3 | 20.5 |
| Oso Ighodaro (PHX) | 98% | 24.3<br><sub>24,23,18,20,32</sub> | 6.5<br><sub>2,4,7,6,2</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>5,6,4,8,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>1,3,2,2,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.4 | 15.2 |
| Collin Gillespie (PHX) | 98% | 23.9<br><sub>24,20,24,22,27</sub> | 9.2<br><sub>6,7,6,12,13</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>2,3,2,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>2,4,3,8,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.2 | 1.2 | 15.8 |
| Luke Kennard (PHX) | 98% | 18.5<br><sub>21,14,14,22,21</sub> | 7.3<br><sub>12,11,3,14,8</sub> |  | 1.8<br><sub>1,1,1,1,1</sub> |  | 1.8<br><sub>5,2,0,3,1</sub> |  | 1.0<br><sub>3,3,1,3,0</sub> |  | 0.7 | 0.1 | 0.8 | 11.0 |
| Jordan Goodwin (PHX) | 98% | 18.0<br><sub>-,-,-,14,24</sub> | 7.2<br><sub>-,-,-,18,6</sub> |  | 3.5<br><sub>-,-,-,3,5</sub> |  | 1.7<br><sub>-,-,-,1,2</sub> |  | 1.1<br><sub>-,-,-,6,2</sub> |  | 1.3 | 0.1 | 0.8 | 12.4 |
| Khaman Maluach (PHX) | 98% | 16.8<br><sub>22,18,20,22,16</sub> | 6.2<br><sub>8,8,11,11,4</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>6,10,5,7,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>2,0,2,3,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.8 | 1.0 | 12.0 |
| Ryan Dunn (PHX) | 98% | 15.2<br><sub>25,23,23,25,10</sub> | 4.3<br><sub>11,8,3,10,0</sub> |  | 3.2<br><sub>3,5,2,8,4</sub> |  | 1.0<br><sub>3,3,0,2,0</sub> |  | 0.4<br><sub>1,2,1,1,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.6 |
| Rasheer Fleming (PHX) | 52% | 8.1<br><sub>-,-,9,12,-</sub> | 3.0<br><sub>-,-,2,4,-</sub> |  | 1.4<br><sub>-,-,1,2,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,1,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.6 |
| Jamaree Bouyea (PHX) | 58% | 7.0<br><sub>2,-,9,8,-</sub> | 2.8<br><sub>0,-,4,7,-</sub> |  | 0.9<br><sub>0,-,0,1,-</sub> |  | 1.2<br><sub>0,-,3,3,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Pat Spencer (PHX) | 67% | 7.0<br><sub>2,-,6,-,-</sub> | 2.5<br><sub>0,-,2,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Koa Peat (PHX) | 58% | 6.4<br><sub>2,-,6,6,-</sub> | 2.6<br><sub>0,-,4,5,-</sub> |  | 1.3<br><sub>1,-,0,1,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |
| Duop Reath (PHX) | 58% | 6.2<br><sub>2,-,6,-,-</sub> | 2.7<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>


### CHA @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Kon Knueppel (CHA), Dennis Schroder (CHA), Hannes Steinbach (CHA)

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 31.4<br><sub>31,26,14,-,-</sub> | 20.2<br><sub>17,10,8,-,-</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>1,4,2,-,-</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>4,1,1,-,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>3,1,0,-,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.5 | 2.5 | 28.0 |
| Naz Reid | 98% | 30.0<br><sub>27,36,26,32,34</sub> | 17.5<br><sub>13,28,14,25,16</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 7.5<br><sub>6,9,6,13,8</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,2,2,4,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 2.1<br><sub>2,2,2,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.8 | 2.5 | 27.5 |
| Grayson Allen | 98% | 29.0<br><sub>19,27,22,34,34</sub> | 14.8<br><sub>11,22,0,27,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>1,2,2,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.9<br><sub>0,4,3,6,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>3,5,0,6,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 2.1 | 21.8 |
| Moussa Diabate | 98% | 28.5<br><sub>24,29,-,-,32</sub> | 8.5<br><sub>7,7,-,-,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 8.8<br><sub>9,6,-,-,13</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,2,-,-,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,-,-,0</sub> |  | 1.0 | 0.8 | 1.5 | 19.6 |
| Sion James | 98% | 26.1<br><sub>21,31,21,33,32</sub> | 7.2<br><sub>11,10,11,11,3</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,2,3,4,8</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,1,0,4,6</sub> |  | 1.0<br><sub>3,0,3,3,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.2 | 1.1 | 13.9 |
| Royce O'Neale | 98% | 20.5<br><sub>18,18,26,23,22</sub> | 6.0<br><sub>2,0,7,10,7</sub> |  | 3.5<br><sub>4,3,4,3,4</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.0<br><sub>0,0,2,2,2</sub> |  | 0.7 | 0.3 | 0.7 | 10.7 |
| Coby White | 98% | 20.4<br><sub>16,18,16,20,20</sub> | 13.2<br><sub>7,4,7,10,21</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>0,5,1,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>3,2,1,9,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,0,1,0,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.5 | 0.1 | 2.3 | 19.3 |
| Ryan Kalkbrenner | 98% | 18.4<br><sub>16,19,21,35,16</sub> | 5.7<br><sub>4,6,4,8,2</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 4.9<br><sub>6,4,5,15,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>0,2,0,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 11.7 |
| Grant Williams | 67% | 17.1<br><sub>-,-,-,-,16</sub> | 6.2<br><sub>-,-,-,-,11</sub> |  | 3.2<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.8<br><sub>-,-,-,-,2</sub> |  | 0.6 | 0.5 | 0.9 | 10.7 |
| Tidjane Salaun | 96% | 15.2<br><sub>19,10,23,18,16</sub> | 5.7<br><sub>1,9,13,14,2</sub> |  | 3.3<br><sub>7,1,4,3,4</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6<br><sub>0,3,2,3,0</sub> |  | 0.5 | 0.2 | 0.7 | 9.7 |
| Christian Anderson | 88% | 14.8<br><sub>9,-,25,16,18</sub> | 6.0<br><sub>8,-,4,9,13</sub> |  | 1.6<br><sub>2,-,3,1,0</sub> |  | 2.0<br><sub>2,-,5,1,2</sub> |  | 0.7<br><sub>1,-,0,3,3</sub> |  | 0.4 | 0.2 | 1.5 | 9.6 |
| Liam McNeeley | 52% | 8.8<br><sub>9,-,19,16,-</sub> | 3.6<br><sub>3,-,8,8,-</sub> |  | 1.6<br><sub>0,-,2,1,-</sub> |  | 0.7<br><sub>1,-,3,1,-</sub> |  | 0.3<br><sub>0,-,1,2,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.9 |
| PJ Hall | 38% | 7.4<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.6 | 5.8 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 31.6<br><sub>36,39,32,25,37</sub> | 20.3<br><sub>16,26,24,13,24</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,1,0,5,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 6.9<br><sub>8,7,10,6,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>1,4,3,1,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.2 | 3.1 | 29.7 |
| Rui Hachimura | 98% | 28.8<br><sub>-,37,26,23,32</sub> | 13.8<br><sub>-,21,14,13,7</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>-,9,3,5,11</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>-,7,2,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.8<br><sub>-,1,2,3,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.8 | 0.3 | 1.1 | 19.8 |
| Derrick Jones Jr. | 98% | 27.0<br><sub>-,37,29,24,29</sub> | 10.4<br><sub>-,12,8,11,14</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>-,8,4,3,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>-,1,3,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2<br><sub>-,2,0,2,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.8 | 0.9 | 15.4 |
| Brook Lopez | 98% | 24.5<br><sub>22,35,26,19,31</sub> | 12.0<br><sub>12,20,20,8,26</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>6,8,7,4,7</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>1,1,1,1,4</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,2,1,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.6 | 1.1 | 1.1 | 18.0 |
| Kris Dunn | 98% | 23.8<br><sub>30,35,24,19,20</sub> | 6.6<br><sub>12,5,14,3,2</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,5,5,2,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.5<br><sub>1,3,4,3,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>1,1,2,1,0</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 1.5 | 0.2 | 1.0 | 13.2 |
| Max Strus | 98% | 21.0<br><sub>23,23,19,22,23</sub> | 8.4<br><sub>11,9,7,12,3</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>4,5,4,3,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>6,5,2,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>3,3,1,2,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.1 | 0.8 | 14.4 |
| Kobe Sanders | 98% | 19.9<br><sub>38,18,22,26,15</sub> | 8.4<br><sub>26,4,8,9,5</sub> |  | 2.1<br><sub>4,2,2,3,0</sub> |  | 1.9<br><sub>3,1,4,7,1</sub> |  | 1.1<br><sub>5,0,2,1,1</sub> |  | 0.9 | 0.1 | 1.1 | 12.3 |
| Keaton Wagler | 98% | 19.9<br><sub>24,16,18,23,18</sub> | 10.5<br><sub>6,11,15,11,14</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>4,2,2,0,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>4,1,4,4,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>0,3,3,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 1.6 | 15.9 |
| Isaiah Jackson | 98% | 16.8<br><sub>26,13,-,16,17</sub> | 6.8<br><sub>19,2,-,4,5</sub> |  | 4.6<br><sub>8,4,-,4,3</sub> |  | 1.3<br><sub>2,2,-,0,3</sub> |  | 0.1<br><sub>1,0,-,0,0</sub> |  | 0.8 | 0.8 | 1.0 | 12.7 |
| Gradey Dick | 97% | 15.4<br><sub>29,7,17,19,19</sub> | 7.3<br><sub>12,4,15,10,13</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>4,2,4,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>3,1,0,2,0</sub> |  | 0.7<br><sub>0,0,2,1,2</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.6 | 0.1 | 0.7 | 10.5 |
| Baba Miller | 72% | 11.2<br><sub>12,6,20,16,-</sub> | 5.1<br><sub>4,2,12,13,-</sub> |  | 1.8<br><sub>0,1,5,4,-</sub> |  | 1.2<br><sub>1,1,4,0,-</sub> |  | 0.3<br><sub>1,0,0,1,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.1 |
| Jalen Pickett | 52% | 6.8<br><sub>-,-,2,8,-</sub> | 2.5<br><sub>-,-,0,3,-</sub> |  | 0.8<br><sub>-,-,0,1,-</sub> |  | 1.0<br><sub>-,-,0,1,-</sub> |  | 0.2<br><sub>-,-,0,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Nick Martinelli | 58% | 6.3<br><sub>-,-,2,-,-</sub> | 3.0<br><sub>-,-,2,-,-</sub> |  | 1.4<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.9 |
| Cam Christie | 52% | 6.0<br><sub>-,-,2,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.5 |
| Blake Wesley | 52% | 5.9<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.9 |

</details>


### SAS @ UTA
Out: Trey Alexander (UTA), Jaxson Hayes (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 29.8<br><sub>28,28,26,36,25</sub> | 16.1<br><sub>19,13,17,18,9</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>2,7,5,6,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.6<br><sub>3,3,4,10,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.4 | 1.6 | 25.9 |
| Victor Wembanyama | 98% | 29.6<br><sub>26,24,25,32,21</sub> | 25.8<br><sub>30,29,40,32,12</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 11.4<br><sub>14,7,11,9,12</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>2,3,3,1,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 3.5 | 2.2 | 40.4 |
| Devin Vassell | 98% | 28.9<br><sub>27,21,-,-,23</sub> | 12.0<br><sub>19,15,-,-,7</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,2,-,-,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>2,3,-,-,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>5,2,-,-,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.4 | 0.9 | 18.6 |
| Stephon Castle | 98% | 28.5<br><sub>28,24,30,29,25</sub> | 16.9<br><sub>19,14,4,11,32</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>3,7,8,1,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.7<br><sub>7,5,7,3,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>1,2,0,1,5</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.4 | 27.7 |
| De'Aaron Fox | 98% | 28.2<br><sub>26,22,29,31,17</sub> | 14.3<br><sub>9,8,15,17,7</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>2,3,9,4,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>4,6,6,9,1</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>0,1,2,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.4 | 1.9 | 23.7 |
| Julian Champagnie | 98% | 25.5<br><sub>22,21,27,35,23</sub> | 9.7<br><sub>8,14,11,12,7</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>7,4,3,0,8</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>2,0,2,2,3</sub> |  | 1.9<br><sub>2,4,3,3,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.5 | 0.6 | 15.8 |
| Keldon Johnson | 98% | 23.2<br><sub>27,27,26,28,25</sub> | 10.0<br><sub>3,10,4,10,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>6,7,5,6,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>6,4,3,4,4</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.7 | 0.2 | 1.1 | 16.9 |
| Harrison Barnes | 88% | 15.9<br><sub>19,19,21,13,21</sub> | 6.0<br><sub>13,5,11,3,11</sub> |  | 1.8<br><sub>1,3,2,1,1</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>2,1,2,1,3</sub> |  | 0.4 | 0.2 | 0.5 | 8.6 |
| Luke Kornet | 98% | 15.2<br><sub>18,15,13,14,16</sub> | 4.0<br><sub>2,6,2,7,6</sub> |  | 4.8<br><sub>6,4,4,5,7</sub> |  | 1.2<br><sub>1,2,1,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.5 | 9.9 |
| Carter Bryant | 91% | 13.2<br><sub>3,17,14,15,19</sub> | 5.2<br><sub>0,6,8,10,8</sub> |  | 2.2<br><sub>0,4,1,1,3</sub> |  | 1.0<br><sub>0,1,1,2,2</sub> |  | 0.7<br><sub>0,2,2,2,2</sub> |  | 0.3 | 0.3 | 0.5 | 8.5 |
| Jordan McLaughlin | 80% | 9.9<br><sub>8,12,11,2,14</sub> | 3.5<br><sub>2,3,4,4,4</sub> |  | 1.8<br><sub>2,0,4,0,6</sub> |  | 1.7<br><sub>1,0,2,0,2</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.7 | 0.1 | 0.5 | 7.0 |
| Tarris Reed Jr. | 80% | 8.2<br><sub>3,9,9,2,11</sub> | 3.2<br><sub>0,2,4,0,2</sub> |  | 3.1<br><sub>1,3,3,0,4</sub> |  | 0.5<br><sub>0,1,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.4 | 6.7 |
| David Jones Garcia | 67% | 6.3<br><sub>3,-,8,2,-</sub> | 2.7<br><sub>0,-,2,0,-</sub> |  | 1.2<br><sub>0,-,0,0,-</sub> |  | 1.2<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.1 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 34.2<br><sub>32,30,-,33,38</sub> | 21.5<br><sub>16,19,-,13,27</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,5,-,7,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.9<br><sub>9,8,-,7,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>1,0,-,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.2 | 3.2 | 31.5 |
| Ace Bailey | 98% | 33.3<br><sub>29,32,35,31,35</sub> | 15.5<br><sub>12,7,23,18,21</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>6,2,7,7,3</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>0,3,2,2,1</sub> |  | 2.2<br><sub>0,1,3,3,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 1.0 | 1.8 | 23.2 |
| Darryn Peterson | 98% | 32.9<br><sub>30,35,31,33,34</sub> | 17.3<br><sub>21,26,25,22,28</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>2,6,4,4,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.9<br><sub>5,4,4,5,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>3,4,4,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.8 | 2.0 | 25.9 |
| Brice Sensabaugh | 98% | 25.4<br><sub>10,13,14,23,27</sub> | 14.0<br><sub>0,2,5,19,7</sub> |  | 3.9<br><sub>2,3,4,3,3</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 2.1<br><sub>0,0,1,3,1</sub> |  | 0.7 | 0.3 | 1.8 | 19.8 |
| Josh Green | 93% | 24.1<br><sub>24,28,30,26,14</sub> | 5.2<br><sub>3,10,2,3,2</sub> |  | 2.5<br><sub>3,0,5,2,0</sub> |  | 1.1<br><sub>1,1,4,1,0</sub> |  | 0.7<br><sub>1,1,0,1,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.8 |
| Josh Okogie | 96% | 23.6<br><sub>24,17,21,15,22</sub> | 6.3<br><sub>12,0,6,7,7</sub> | 4.5 · –<br><sub>o 55% · u 45%</sub> | 3.8<br><sub>4,1,4,3,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>0,0,4,0,1</sub> |  | 0.7<br><sub>2,0,0,1,2</sub> |  | 1.0 | 0.4 | 0.8 | 11.4 |
| Mo Bamba | 86% | 19.1<br><sub>-,17,17,18,20</sub> | 6.3<br><sub>-,3,7,5,9</sub> |  | 6.7<br><sub>-,3,7,1,9</sub> |  | 0.9<br><sub>-,1,0,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.4 | 1.5 | 0.8 | 13.9 |
| Isaiah Collier | 98% | 19.0<br><sub>13,16,24,12,16</sub> | 8.5<br><sub>4,6,17,7,3</sub> |  | 2.9<br><sub>3,4,5,3,2</sub> |  | 4.5<br><sub>3,2,5,2,5</sub> |  | 0.4<br><sub>0,0,4,1,1</sub> |  | 0.7 | 0.2 | 1.5 | 15.9 |
| Svi Mykhailiuk | 96% | 17.3<br><sub>14,6,21,20,7</sub> | 6.0<br><sub>0,0,7,3,0</sub> |  | 1.9<br><sub>0,0,2,0,1</sub> |  | 1.2<br><sub>1,0,3,2,0</sub> |  | 0.9<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 9.1 |
| Kyle Filipowski | 67% | 15.2<br><sub>1,15,15,-,2</sub> | 7.9<br><sub>0,9,7,-,2</sub> |  | 4.6<br><sub>0,6,4,-,0</sub> |  | 1.5<br><sub>0,1,1,-,0</sub> |  | 0.6<br><sub>0,1,0,-,0</sub> |  | 0.6 | 0.3 | 1.0 | 14.0 |
| Tony Bradley | 63% | 12.4<br><sub>1,2,14,-,12</sub> | 3.3<br><sub>0,0,4,-,0</sub> |  | 3.7<br><sub>1,1,5,-,5</sub> |  | 0.6<br><sub>0,0,0,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.6 |

</details>


### DAL @ BOS
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.0–119.9 | DAL 18% | 5.67 / 1.21 | BOS -12.5 | 226.5 | BOS -13.5 covers 48%; o219.5 66% |
| Expected (weighted by chance each plays) | 107.7–118.2 | DAL 23% | 4.31 / 1.30 | BOS -10.5 | 226.5 | BOS -13.5 covers 41%; o219.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Max Christie (DAL) | Day-To-Day | 70% | 12.7 | 4.4 | 1.5 | 0.7 | 0.6 | 0.3 | 0.2 | 0.6 | 6.6 | small |
| Daniel Gafford (DAL) | Day-To-Day | 70% | 19.6 | 8.0 | 5.2 | 1.1 | 0.0 | 0.5 | 1.0 | 1.0 | 14.3 | small |
| Amari Williams (BOS) | Questionable | 55% | 5.1 | 1.6 | 1.6 | 0.4 | 0.0 | 0.1 | 0.3 | 0.4 | 3.6 | small |
| Devin Carter (BOS) | Questionable | 55% | 8.6 | 3.8 | 1.6 | 1.3 | 0.3 | 0.5 | 0.1 | 0.7 | 6.7 | small |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 35.6<br><sub>33,28,39,27,38</sub> | 22.1<br><sub>21,25,43,12,18</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>10,5,10,7,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>7,12,6,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>1,3,3,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.8 | 2.6 | 34.7 |
| Kyrie Irving | 98% | 35.0<br><sub>28,29,38,27,37</sub> | 21.1<br><sub>14,21,35,10,34</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,3,0,3,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>2,4,4,4,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.6<br><sub>0,2,7,2,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.4 | 2.2 | 29.4 |
| P.J. Washington | 98% | 32.6<br><sub>33,25,35,16,26</sub> | 13.2<br><sub>26,6,13,10,10</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>6,5,9,3,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,0,1,0,1</sub> |  | 1.8<br><sub>6,2,2,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.8 | 1.6 | 21.7 |
| Naji Marshall | 91% | 27.7<br><sub>25,15,25,23,30</sub> | 12.8<br><sub>7,8,6,13,12</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>1,1,5,1,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>5,2,2,4,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.9<br><sub>0,1,0,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.1 | 1.6 | 20.2 |
| Caleb Martin | 98% | 23.8<br><sub>11,19,19,21,33</sub> | 6.4<br><sub>0,2,0,7,15</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>0,2,3,2,8</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.7<br><sub>0,2,5,5,3</sub> |  | 0.7<br><sub>0,0,0,1,1</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.3 | 0.9 | 11.7 |
| Zaccharie Risacher | 98% | 20.8<br><sub>21,16,15,25,14</sub> | 7.3<br><sub>4,11,4,22,5</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>4,6,2,6,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,1,0,3,0</sub> |  | 0.9<br><sub>0,1,0,4,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.6 | 0.8 | 12.2 |
| Walter Clayton Jr. | 93% | 18.0<br><sub>23,16,25,22,13</sub> | 6.5<br><sub>12,5,6,5,2</sub> |  | 2.6<br><sub>4,4,6,1,2</sub> |  | 2.9<br><sub>2,6,4,4,2</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 0.5 | 0.2 | 1.2 | 12.0 |
| Santi Aldama | 98% | 17.8<br><sub>13,15,19,10,16</sub> | 7.8<br><sub>8,12,10,3,7</sub> |  | 3.9<br><sub>9,2,4,1,2</sub> |  | 1.4<br><sub>1,0,1,1,1</sub> |  | 0.9<br><sub>0,2,1,1,2</sub> |  | 0.5 | 0.4 | 0.9 | 13.1 |
| Morez Johnson Jr. | 98% | 17.0<br><sub>24,19,-,13,15</sub> | 6.1<br><sub>13,4,-,0,4</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>17,9,-,2,2</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>2,1,-,0,0</sub> |  | 0.4<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.8 | 10.7 |
| Marcus Sasser | 58% | 13.0<br><sub>-,9,-,9,-</sub> | 4.3<br><sub>-,4,-,3,-</sub> |  | 1.1<br><sub>-,0,-,1,-</sub> |  | 1.5<br><sub>-,0,-,0,-</sub> |  | 0.6<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.6 | 6.9 |
| Tobi Lawal | 52% | 7.6<br><sub>1,5,-,12,-</sub> | 2.6<br><sub>0,2,-,0,-</sub> |  | 1.4<br><sub>0,0,-,6,-</sub> |  | 0.5<br><sub>0,0,-,1,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.5 |
| Moussa Cisse | 58% | 7.5<br><sub>1,5,-,8,-</sub> | 2.3<br><sub>0,2,-,0,-</sub> |  | 2.5<br><sub>0,1,-,0,-</sub> |  | 0.1<br><sub>0,1,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.5 | 0.4 | 5.0 |
| Jett Howard | 52% | 6.7<br><sub>1,3,-,5,-</sub> | 2.7<br><sub>0,5,-,3,-</sub> |  | 0.7<br><sub>0,1,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>0,1,-,1,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.8 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 32.8<br><sub>-,29,29,32,38</sub> | 25.9<br><sub>-,34,21,21,24</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>-,8,4,6,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>-,9,6,4,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>-,5,5,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.6 | 2.6 | 40.6 |
| Derrick White | 98% | 30.1<br><sub>36,25,27,22,38</sub> | 13.4<br><sub>24,18,9,5,19</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,4,3,1,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>7,5,7,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,4,1,1,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.0 | 1.6 | 22.1 |
| Paul George | 98% | 30.1<br><sub>35,22,28,30,-</sub> | 19.4<br><sub>25,8,27,36,-</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>3,5,3,5,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>5,1,1,1,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>5,2,5,6,-</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6 | 0.5 | 2.4 | 27.8 |
| Payton Pritchard | 98% | 27.2<br><sub>18,23,29,30,31</sub> | 14.2<br><sub>10,12,12,18,14</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>1,6,5,6,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.3<br><sub>5,5,4,5,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>0,4,4,4,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.1 | 1.3 | 21.9 |
| Neemias Queta | 98% | 23.9<br><sub>29,15,22,22,31</sub> | 10.4<br><sub>9,4,13,4,11</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>12,3,9,6,13</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>3,1,4,3,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.6 | 1.3 | 1.2 | 20.7 |
| Sam Hauser | 98% | 21.5<br><sub>30,17,23,18,24</sub> | 8.1<br><sub>11,9,7,12,8</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>2,3,3,5,9</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,3,1,2,0</sub> |  | 1.6<br><sub>3,3,1,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.4 | 0.2 | 0.4 | 13.0 |
| Baylor Scheierman | 98% | 21.3<br><sub>29,15,19,18,29</sub> | 6.6<br><sub>9,5,7,5,9</sub> |  | 4.3<br><sub>11,4,1,3,7</sub> |  | 1.7<br><sub>1,2,0,2,3</sub> |  | 1.0<br><sub>3,1,1,1,3</sub> |  | 0.8 | 0.1 | 0.7 | 12.6 |
| Mitchell Robinson | 98% | 14.9<br><sub>20,15,18,17,11</sub> | 5.2<br><sub>3,6,12,2,2</sub> |  | 6.0<br><sub>10,7,7,6,2</sub> |  | 0.7<br><sub>1,0,2,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.7 | 11.9 |
| Jordan Walsh | 98% | 14.7<br><sub>12,22,11,19,18</sub> | 4.2<br><sub>3,6,0,8,6</sub> |  | 3.2<br><sub>4,3,3,2,3</sub> |  | 0.8<br><sub>0,0,0,2,0</sub> |  | 0.4<br><sub>1,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.4 | 8.1 |
| Luka Garza | 98% | 12.8<br><sub>18,19,9,9,11</sub> | 7.0<br><sub>11,6,4,2,5</sub> |  | 3.4<br><sub>5,7,5,0,1</sub> |  | 1.1<br><sub>2,4,0,2,0</sub> |  | 0.7<br><sub>3,2,0,0,1</sub> |  | 0.3 | 0.3 | 0.6 | 11.4 |
| Hugo Gonzalez | 98% | 11.7<br><sub>14,15,10,19,8</sub> | 3.6<br><sub>4,8,0,10,0</sub> |  | 2.4<br><sub>2,1,2,2,1</sub> |  | 0.6<br><sub>0,0,1,2,0</sub> |  | 0.3<br><sub>0,1,0,2,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.6 |
| Mike Conley | 48% | 7.9<br><sub>-,11,10,-,-</sub> | 2.4<br><sub>-,0,3,-,-</sub> |  | 0.8<br><sub>-,0,3,-,-</sub> |  | 1.2<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Ron Harper Jr. | 58% | 6.9<br><sub>-,10,4,4,-</sub> | 3.1<br><sub>-,3,2,0,-</sub> |  | 1.0<br><sub>-,0,0,1,-</sub> |  | 0.6<br><sub>-,2,0,0,-</sub> |  | 0.3<br><sub>-,1,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Dillon Mitchell | 21% | 6.8<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 0.9 |
| Chris Cenac Jr. | 38% | 5.8<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.7 | 4.9 |

</details>


### NYK @ TOR
Out: Kawhi Leonard (TOR), Malachi Smith (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.3–107.9 | NYK 67% | 1.48 / 3.07 | TOR +6.5 | 221.5 | TOR +4.5 covers 44%; o217.5 59% |
| Expected (weighted by chance each plays) | 113.9–108.0 | NYK 66% | 1.52 / 2.94 | TOR +5.5 | 221.5 | TOR +4.5 covers 46%; o217.5 58% |
| if Scottie Barnes plays | 113.4–108.4 | NYK 64% | 1.57 / 2.77 | TOR +5.5 | 221.5 | TOR +4.5 covers 48%; o217.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes (TOR) | Questionable | 55% | 31.5 | 18.7 | 6.3 | 6.1 | 0.7 | 1.5 | 1.1 | 2.8 | 31.1 | full tables below |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 35.1<br><sub>28,34,28,35,36</sub> | 26.8<br><sub>33,31,23,27,33</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>2,6,4,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 6.1<br><sub>4,9,2,5,11</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>5,3,1,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.1 | 2.9 | 35.9 |
| OG Anunoby | 98% | 33.5<br><sub>24,34,29,34,33</sub> | 17.1<br><sub>18,15,19,14,11</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>5,6,3,6,2</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,3,5,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.8 | 1.9 | 24.1 |
| Karl-Anthony Towns | 98% | 32.4<br><sub>25,34,27,34,34</sub> | 18.7<br><sub>17,29,21,21,23</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 12.3<br><sub>12,13,16,11,15</sub> | 12.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,3,3,8,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.8 | 2.9 | 34.6 |
| Josh Hart | 98% | 29.6<br><sub>-,-,-,26,23</sub> | 9.3<br><sub>-,-,-,6,0</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>-,-,-,4,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>-,-,-,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.3 | 1.7 | 19.8 |
| Mikal Bridges | 98% | 25.7<br><sub>22,31,17,17,29</sub> | 9.3<br><sub>7,9,4,2,18</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>4,6,5,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>4,4,1,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.4 | 1.0 | 14.5 |
| Landry Shamet | 98% | 23.4<br><sub>25,29,28,29,21</sub> | 8.0<br><sub>7,9,10,12,5</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,3,2,3</sub> |  | 1.3<br><sub>2,1,2,4,1</sub> |  | 1.4<br><sub>1,3,2,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.5 | 0.2 | 0.9 | 11.1 |
| Miles McBride | 98% | 19.6<br><sub>11,16,25,27,22</sub> | 7.4<br><sub>7,5,8,19,9</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,0,0,2,1</sub> |  | 1.4<br><sub>1,0,3,2,1</sub> |  | 1.3<br><sub>2,1,2,5,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 0.7 | 10.4 |
| Tyler Kolek | 91% | 13.7<br><sub>11,14,15,13,19</sub> | 4.3<br><sub>0,0,12,4,5</sub> |  | 1.9<br><sub>0,4,3,1,6</sub> |  | 3.4<br><sub>5,5,4,4,2</sub> |  | 0.5<br><sub>0,0,2,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.7 |
| Andre Drummond | 98% | 13.5<br><sub>12,14,16,14,14</sub> | 4.2<br><sub>6,0,2,0,0</sub> |  | 6.0<br><sub>9,8,14,4,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.0<br><sub>0,0,3,3,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.8 | 11.1 |
| Jordan Clarkson | 76% | 10.2<br><sub>15,15,11,-,9</sub> | 4.7<br><sub>10,9,2,-,0</sub> |  | 1.4<br><sub>1,2,4,-,1</sub> |  | 0.7<br><sub>1,0,2,-,0</sub> |  | 0.3<br><sub>2,1,0,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.8 |
| Mohamed Diawara | 63% | 8.6<br><sub>21,14,18,11,-</sub> | 2.9<br><sub>8,2,5,2,-</sub> |  | 1.4<br><sub>6,3,3,0,-</sub> |  | 0.9<br><sub>4,3,3,0,-</sub> |  | 0.2<br><sub>1,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Jose Alvarado | 52% | 8.3<br><sub>9,-,6,-,-</sub> | 3.2<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 1.2<br><sub>2,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.6 |
| Dalton Knecht | 64% | 6.7<br><sub>16,5,8,-,-</sub> | 3.0<br><sub>10,0,3,-,-</sub> |  | 1.3<br><sub>7,0,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>2,0,1,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.7 |
| Jaden Akins | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.0 |
| James Wiseman | 48% | 6.4<br><sub>10,-,5,-,-</sub> | 2.3<br><sub>8,-,0,-,-</sub> |  | 2.1<br><sub>8,-,1,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 4.7 |
| Pacome Dadiet | 52% | 6.3<br><sub>9,-,6,-,1</sub> | 2.7<br><sub>4,-,8,-,0</sub> |  | 1.2<br><sub>0,-,2,-,0</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.2<br><sub>0,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 35.5<br><sub>33,37,36,31,37</sub> | 22.5<br><sub>22,27,19,12,31</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>5,7,3,8,14</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 4.6<br><sub>3,5,2,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,0,1,0,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.4 | 2.6 | 33.5 |
| Immanuel Quickley | 86% | 31.8<br><sub>32,-,-,28,28</sub> | 16.8<br><sub>13,-,-,11,26</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>1,-,-,4,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>7,-,-,4,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>2,-,-,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.1 | 1.7 | 26.9 |
| Ja'Kobe Walter | 98% | 31.5<br><sub>27,29,34,35,32</sub> | 11.9<br><sub>8,7,12,17,6</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>1,6,6,3,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,2,5,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.3 | 1.1 | 17.6 |
| Collin Murray-Boyles | 98% | 28.7<br><sub>23,34,-,20,32</sub> | 12.7<br><sub>13,19,-,5,14</sub> |  | 5.6<br><sub>3,7,-,4,0</sub> |  | 2.6<br><sub>2,2,-,3,4</sub> |  | 0.6<br><sub>1,0,-,1,1</sub> |  | 1.1 | 1.2 | 1.8 | 20.9 |
| Jakob Poeltl | 91% | 26.7<br><sub>19,31,31,32,25</sub> | 10.3<br><sub>8,19,18,6,9</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>5,11,8,9,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>1,1,2,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.0 | 1.5 | 19.6 |
| Jamal Shead | 98% | 25.7<br><sub>20,34,36,22,22</sub> | 8.4<br><sub>3,10,20,3,5</sub> |  | 1.9<br><sub>3,3,2,3,1</sub> |  | 6.2<br><sub>6,16,11,6,5</sub> |  | 1.1<br><sub>1,1,4,0,1</sub> |  | 1.0 | 0.2 | 1.9 | 16.5 |
| Jamison Battle | 98% | 24.1<br><sub>19,21,29,25,25</sub> | 10.8<br><sub>9,6,18,12,13</sub> |  | 2.7<br><sub>1,2,1,2,1</sub> |  | 1.0<br><sub>0,0,2,0,1</sub> |  | 1.9<br><sub>2,1,5,2,3</sub> |  | 0.4 | 0.2 | 0.8 | 14.6 |
| Alijah Martin | 91% | 16.1<br><sub>9,31,21,16,18</sub> | 6.5<br><sub>6,27,2,12,7</sub> |  | 2.1<br><sub>1,4,3,1,4</sub> |  | 1.3<br><sub>0,1,3,0,1</sub> |  | 0.8<br><sub>0,6,0,4,1</sub> |  | 0.6 | 0.3 | 1.0 | 9.9 |
| Allen Graves | 98% | 15.1<br><sub>14,16,13,18,13</sub> | 5.0<br><sub>5,3,3,13,0</sub> |  | 2.4<br><sub>1,2,2,5,2</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>1,0,1,3,0</sub> |  | 0.4 | 0.4 | 0.6 | 8.2 |
| Kyle Anderson | 80% | 11.8<br><sub>4,-,16,11,5</sub> | 3.2<br><sub>2,-,6,2,0</sub> |  | 2.0<br><sub>0,-,2,3,0</sub> |  | 2.0<br><sub>1,-,2,4,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 7.2 |
| Trayce Jackson-Davis | 64% | 9.9<br><sub>4,-,14,-,-</sub> | 3.6<br><sub>1,-,4,-,-</sub> |  | 2.9<br><sub>0,-,6,-,-</sub> |  | 0.6<br><sub>0,-,1,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.5 | 0.5 | 7.1 |
| Jaden Bradley | 67% | 7.7<br><sub>4,8,9,-,2</sub> | 2.7<br><sub>2,3,0,-,1</sub> |  | 1.1<br><sub>1,0,1,-,0</sub> |  | 1.2<br><sub>0,1,3,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.0 |

</details>

<details><summary>if Scottie Barnes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 98% | 35.0<br><sub>28,34,28,35,36</sub> | 26.7<br><sub>33,31,23,27,33</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>2,6,4,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 6.1<br><sub>4,9,2,5,11</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>5,3,1,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.1 | 2.9 | 35.9 |
| OG Anunoby (NYK) | 98% | 33.5<br><sub>24,34,29,34,33</sub> | 17.1<br><sub>18,15,19,14,11</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>5,6,3,6,2</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>1,3,5,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.8 | 1.9 | 24.1 |
| Karl-Anthony Towns (NYK) | 98% | 32.5<br><sub>25,34,27,34,34</sub> | 18.6<br><sub>17,29,21,21,23</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 12.3<br><sub>12,13,16,11,15</sub> | 12.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,3,3,8,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.7 | 3.0 | 34.6 |
| Josh Hart (NYK) | 98% | 29.6<br><sub>-,-,-,26,23</sub> | 9.3<br><sub>-,-,-,6,0</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>-,-,-,4,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>-,-,-,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.3 | 1.7 | 19.7 |
| Mikal Bridges (NYK) | 98% | 25.6<br><sub>22,31,17,17,29</sub> | 9.3<br><sub>7,9,4,2,18</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>4,6,5,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>4,4,1,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.4 | 1.0 | 14.4 |
| Landry Shamet (NYK) | 98% | 23.4<br><sub>25,29,28,29,21</sub> | 8.0<br><sub>7,9,10,12,5</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,3,2,3</sub> |  | 1.4<br><sub>2,1,2,4,1</sub> |  | 1.4<br><sub>1,3,2,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.5 | 0.2 | 0.9 | 11.1 |
| Miles McBride (NYK) | 98% | 19.6<br><sub>11,16,25,27,22</sub> | 7.3<br><sub>7,5,8,19,9</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,0,0,2,1</sub> |  | 1.4<br><sub>1,0,3,2,1</sub> |  | 1.3<br><sub>2,1,2,5,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 0.7 | 10.4 |
| Tyler Kolek (NYK) | 91% | 13.8<br><sub>11,14,15,13,19</sub> | 4.3<br><sub>0,0,12,4,5</sub> |  | 1.9<br><sub>0,4,3,1,6</sub> |  | 3.4<br><sub>5,5,4,4,2</sub> |  | 0.5<br><sub>0,0,2,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.7 |
| Andre Drummond (NYK) | 98% | 13.7<br><sub>12,14,16,14,14</sub> | 4.2<br><sub>6,0,2,0,0</sub> |  | 6.1<br><sub>9,8,14,4,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.0<br><sub>0,0,3,3,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.8 | 11.3 |
| Jordan Clarkson (NYK) | 76% | 10.1<br><sub>15,15,11,-,9</sub> | 4.7<br><sub>10,9,2,-,0</sub> |  | 1.4<br><sub>1,2,4,-,1</sub> |  | 0.7<br><sub>1,0,2,-,0</sub> |  | 0.3<br><sub>2,1,0,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.8 |
| Mohamed Diawara (NYK) | 63% | 8.7<br><sub>21,14,18,11,-</sub> | 3.0<br><sub>8,2,5,2,-</sub> |  | 1.4<br><sub>6,3,3,0,-</sub> |  | 0.9<br><sub>4,3,3,0,-</sub> |  | 0.3<br><sub>1,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Jose Alvarado (NYK) | 52% | 8.4<br><sub>9,-,6,-,-</sub> | 3.3<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 1.3<br><sub>2,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.6 |
| Jaden Akins (NYK) | 38% | 6.8<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.0 |
| Dalton Knecht (NYK) | 64% | 6.6<br><sub>16,5,8,-,-</sub> | 3.0<br><sub>10,0,3,-,-</sub> |  | 1.2<br><sub>7,0,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>2,0,1,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.6 |
| James Wiseman (NYK) | 48% | 6.4<br><sub>10,-,5,-,-</sub> | 2.2<br><sub>8,-,0,-,-</sub> |  | 2.1<br><sub>8,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 4.7 |
| Pacome Dadiet (NYK) | 52% | 6.2<br><sub>9,-,6,-,1</sub> | 2.6<br><sub>4,-,8,-,0</sub> |  | 1.2<br><sub>0,-,2,-,0</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.2<br><sub>0,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| RJ Barrett (TOR) | 98% | 32.5<br><sub>33,37,36,31,37</sub> | 19.3<br><sub>22,27,19,12,31</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>5,7,3,8,14</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.9<br><sub>3,5,2,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>3,0,1,0,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.4 | 2.2 | 29.2 |
| Scottie Barnes (TOR) | 100% | 31.5<br><sub>32,-,-,-,-</sub> | 18.7<br><sub>17,-,-,-,-</sub> | 18.5 · – | 6.3<br><sub>6,-,-,-,-</sub> | 6.5 | 6.1<br><sub>6,-,-,-,-</sub> | 4.5 | 0.7<br><sub>1,-,-,-,-</sub> | 0.5 | 1.5 | 1.1 | 2.8 | 31.1 |
| Immanuel Quickley (TOR) | 86% | 29.1<br><sub>32,-,-,28,28</sub> | 14.7<br><sub>13,-,-,11,26</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>1,-,-,4,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>7,-,-,4,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>2,-,-,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.1 | 1.5 | 23.2 |
| Ja'Kobe Walter (TOR) | 98% | 28.4<br><sub>27,29,34,35,32</sub> | 10.0<br><sub>8,7,12,17,6</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>1,6,6,3,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,1,2,5,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.3 | 0.8 | 15.0 |
| Collin Murray-Boyles (TOR) | 98% | 24.2<br><sub>23,34,-,20,32</sub> | 10.5<br><sub>13,19,-,5,14</sub> |  | 4.9<br><sub>3,7,-,4,0</sub> |  | 1.9<br><sub>2,2,-,3,4</sub> |  | 0.5<br><sub>1,0,-,1,1</sub> |  | 1.0 | 1.1 | 1.4 | 17.3 |
| Jakob Poeltl (TOR) | 91% | 23.4<br><sub>19,31,31,32,25</sub> | 8.8<br><sub>8,19,18,6,9</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>5,11,8,9,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>1,1,2,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.3 | 16.7 |
| Jamal Shead (TOR) | 98% | 22.9<br><sub>20,34,36,22,22</sub> | 7.0<br><sub>3,10,20,3,5</sub> |  | 1.7<br><sub>3,3,2,3,1</sub> |  | 5.1<br><sub>6,16,11,6,5</sub> |  | 0.9<br><sub>1,1,4,0,1</sub> |  | 0.9 | 0.2 | 1.6 | 13.7 |
| Jamison Battle (TOR) | 98% | 19.5<br><sub>19,21,29,25,25</sub> | 8.3<br><sub>9,6,18,12,13</sub> |  | 2.2<br><sub>1,2,1,2,1</sub> |  | 0.8<br><sub>0,0,2,0,1</sub> |  | 1.4<br><sub>2,1,5,2,3</sub> |  | 0.3 | 0.2 | 0.6 | 11.2 |
| Alijah Martin (TOR) | 91% | 14.1<br><sub>9,31,21,16,18</sub> | 5.7<br><sub>6,27,2,12,7</sub> |  | 1.9<br><sub>1,4,3,1,4</sub> |  | 1.2<br><sub>0,1,3,0,1</sub> |  | 0.6<br><sub>0,6,0,4,1</sub> |  | 0.6 | 0.2 | 0.8 | 8.7 |
| Allen Graves (TOR) | 98% | 12.9<br><sub>14,16,13,18,13</sub> | 4.2<br><sub>5,3,3,13,0</sub> |  | 2.1<br><sub>1,2,2,5,2</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.4<br><sub>1,0,1,3,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.9 |
| Kyle Anderson (TOR) | 80% | 8.1<br><sub>4,-,16,11,5</sub> | 2.2<br><sub>2,-,6,2,0</sub> |  | 1.4<br><sub>0,-,2,3,0</sub> |  | 1.4<br><sub>1,-,2,4,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 5.0 |
| Trayce Jackson-Davis (TOR) | 64% | 7.0<br><sub>4,-,14,-,-</sub> | 2.6<br><sub>1,-,4,-,-</sub> |  | 2.1<br><sub>0,-,6,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.4 | 0.3 | 5.1 |
| Jaden Bradley (TOR) | 67% | 6.4<br><sub>4,8,9,-,2</sub> | 2.3<br><sub>2,3,0,-,1</sub> |  | 0.9<br><sub>1,0,1,-,0</sub> |  | 1.1<br><sub>0,1,3,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |

</details>


### HOU @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Clint Capela (HOU), Marcus Smart (HOU), Fred VanVleet (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 120.2–109.4 | HOU 78% | 1.28 / 4.52 | WAS +10.5 | 229.5 | WAS +8.5 covers 43%; o223.5 63% |
| Expected (weighted by chance each plays) | 119.6–110.1 | HOU 75% | 1.33 / 4.07 | WAS +9.5 | 229.5 | WAS +8.5 covers 47%; o223.5 63% |
| if Alex Sarr plays | 119.8–110.5 | HOU 74% | 1.34 / 3.91 | WAS +9.5 | 230.5 | WAS +8.5 covers 48%; o223.5 64% |
| if Tre Johnson plays | 119.8–109.6 | HOU 77% | 1.30 / 4.28 | WAS +10.5 | 229.5 | WAS +8.5 covers 45%; o223.5 62% |
| if Bub Carrington plays | 119.7–109.5 | HOU 77% | 1.30 / 4.30 | WAS +10.5 | 229.5 | WAS +8.5 covers 45%; o223.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Questionable | 55% | 9.1 | 2.6 | 2.5 | 0.5 | 0.1 | 0.3 | 0.4 | 0.6 | 5.7 | small |
| Alex Sarr (WAS) | Questionable | 55% | 31.5 | 13.1 | 8.2 | 2.3 | 1.3 | 1.0 | 1.7 | 1.5 | 23.6 | full tables below |
| Tre Johnson (WAS) | Questionable | 55% | 28.9 | 11.8 | 2.5 | 1.5 | 1.8 | 0.9 | 0.2 | 1.4 | 15.8 | full tables below |
| Bub Carrington (WAS) | Questionable | 55% | 20.9 | 7.1 | 2.2 | 2.6 | 1.1 | 0.6 | 0.2 | 1.2 | 11.8 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.3<br><sub>32,39,35,29,41</sub> | 19.0<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.7 | 0.7 | 2.2 | 32.3 |
| Kevin Durant | 98% | 36.7<br><sub>35,38,36,34,33</sub> | 26.4<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 1.0 | 3.4 | 38.3 |
| Alperen Sengun | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.2<br><sub>17,15,20,19,43</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.6 | 1.1 | 3.2 | 43.4 |
| Jabari Smith Jr. | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.2<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.9 | 1.4 | 26.6 |
| Tari Eason | 98% | 30.5<br><sub>24,23,19,22,33</sub> | 13.0<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 7.6<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7 | 0.8 | 1.3 | 22.5 |
| Reed Sheppard | 88% | 26.3<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.5 | 1.2 | 19.2 |
| Bogdan Bogdanovic | 97% | 16.7<br><sub>5,2,12,10,12</sub> | 6.3<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams | 21% | 15.2<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 5.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.6 | 0.9 | 10.8 |
| Oscar Tshiebwe | 91% | 12.1<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.4<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.7 |
| Jae'Sean Tate | 52% | 10.8<br><sub>-,-,-,1,-</sub> | 3.0<br><sub>-,-,-,0,-</sub> |  | 2.5<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.3 |
| Bruce Thornton | 58% | 10.8<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Isaiah Crawford | 58% | 9.8<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.8 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 38.1<br><sub>36,31,37,34,44</sub> | 16.6<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.6 | 2.6 | 25.8 |
| Trae Young | 98% | 38.0<br><sub>37,28,38,34,45</sub> | 22.6<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 9.3<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 4.1 | 35.2 |
| Anthony Davis | 98% | 37.6<br><sub>-,-,34,34,44</sub> | 25.5<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 11.8<br><sub>-,-,13,13,15</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.3 | 1.6 | 2.5 | 40.2 |
| Kyshawn George | 98% | 35.7<br><sub>39,30,35,39,26</sub> | 18.4<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 1.1 | 2.7 | 28.2 |
| Bilal Coulibaly | 98% | 30.4<br><sub>24,20,-,25,29</sub> | 11.0<br><sub>9,0,-,5,4</sub> |  | 4.5<br><sub>5,5,-,6,7</sub> |  | 1.9<br><sub>0,0,-,2,0</sub> |  | 1.1<br><sub>1,0,-,0,0</sub> |  | 1.4 | 1.0 | 1.3 | 17.5 |
| Deandre Ayton | 98% | 19.6<br><sub>23,7,13,9,9</sub> | 6.3<br><sub>8,2,2,2,2</sub> |  | 6.3<br><sub>11,1,8,2,4</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.7 | 13.4 |
| Khris Middleton | 35% | 16.6<br><sub>-,-,-,-,-</sub> | 5.4<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 1.0 | 9.0 |
| Will Riley | 76% | 15.0<br><sub>9,20,4,-,3</sub> | 6.1<br><sub>7,5,0,-,3</sub> |  | 1.7<br><sub>0,2,0,-,0</sub> |  | 1.0<br><sub>0,1,1,-,0</sub> |  | 0.6<br><sub>1,0,0,-,1</sub> |  | 0.5 | 0.1 | 0.7 | 8.9 |
| Anthony Gill | 43% | 11.6<br><sub>-,9,2,-,-</sub> | 3.9<br><sub>-,1,0,-,-</sub> |  | 1.9<br><sub>-,1,2,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 6.5 |
| Tre Mann | 52% | 11.0<br><sub>-,18,2,-,-</sub> | 3.9<br><sub>-,2,0,-,-</sub> |  | 1.1<br><sub>-,0,0,-,-</sub> |  | 1.0<br><sub>-,2,0,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.5 | 0.1 | 0.6 | 6.1 |

</details>

<details><summary>if Alex Sarr plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 37.4<br><sub>32,39,35,29,41</sub> | 18.9<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.8 | 0.7 | 2.2 | 32.2 |
| Alperen Sengun (HOU) | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.1<br><sub>17,15,20,19,43</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.6 | 1.1 | 3.2 | 43.3 |
| Kevin Durant (HOU) | 98% | 36.6<br><sub>35,38,36,34,33</sub> | 26.3<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 1.0 | 3.4 | 38.1 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.3<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.8 | 1.4 | 26.7 |
| Tari Eason (HOU) | 98% | 30.5<br><sub>24,23,19,22,33</sub> | 12.9<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 7.7<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7 | 0.8 | 1.3 | 22.4 |
| Reed Sheppard (HOU) | 88% | 26.2<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.5 | 1.2 | 19.2 |
| Bogdan Bogdanovic (HOU) | 97% | 16.8<br><sub>5,2,12,10,12</sub> | 6.3<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams (HOU) | 21% | 15.5<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 6.0<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.5 | 0.9 | 11.0 |
| Oscar Tshiebwe (HOU) | 91% | 12.1<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.4<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.7 |
| Jae'Sean Tate (HOU) | 52% | 10.9<br><sub>-,-,-,1,-</sub> | 3.1<br><sub>-,-,-,0,-</sub> |  | 2.5<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.3 |
| Bruce Thornton (HOU) | 58% | 10.9<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Isaiah Crawford (HOU) | 58% | 9.8<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.7 |
| Trae Young (WAS) | 98% | 37.5<br><sub>37,28,38,34,45</sub> | 21.5<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 9.6<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.6 | 34.3 |
| Anthony Davis (WAS) | 98% | 36.9<br><sub>-,-,34,34,44</sub> | 23.5<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 11.8<br><sub>-,-,13,13,15</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.3 | 1.7 | 2.3 | 38.2 |
| AJ Dybantsa (WAS) | 98% | 36.6<br><sub>36,31,37,34,44</sub> | 15.5<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 2.4 | 24.4 |
| Kyshawn George (WAS) | 98% | 34.7<br><sub>39,30,35,39,26</sub> | 16.8<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 1.1 | 2.5 | 26.1 |
| Alex Sarr (WAS) | 100% | 31.5<br><sub>30,28,25,25,44</sub> | 13.1<br><sub>13,15,4,5,30</sub> | 10.5 · – | 8.2<br><sub>8,14,8,8,9</sub> | 6.5 | 2.3<br><sub>3,1,0,0,2</sub> | 1.5 | 1.3<br><sub>1,1,0,1,4</sub> | 0.5 | 1.0 | 1.7 | 1.5 | 23.6 |
| Bilal Coulibaly (WAS) | 98% | 27.9<br><sub>24,20,-,25,29</sub> | 9.8<br><sub>9,0,-,5,4</sub> |  | 4.1<br><sub>5,5,-,6,7</sub> |  | 1.7<br><sub>0,0,-,2,0</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 1.3 | 0.9 | 1.3 | 15.6 |
| Deandre Ayton (WAS) | 98% | 15.5<br><sub>23,7,13,9,9</sub> | 5.0<br><sub>8,2,2,2,2</sub> |  | 4.9<br><sub>11,1,8,2,4</sub> |  | 0.6<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 10.6 |
| Khris Middleton (WAS) | 35% | 13.6<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.9 | 7.2 |
| Will Riley (WAS) | 76% | 11.5<br><sub>9,20,4,-,3</sub> | 4.5<br><sub>7,5,0,-,3</sub> |  | 1.3<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.4<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 6.7 |
| Anthony Gill (WAS) | 43% | 8.5<br><sub>-,9,2,-,-</sub> | 2.8<br><sub>-,1,0,-,-</sub> |  | 1.3<br><sub>-,1,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |
| Tre Mann (WAS) | 52% | 8.4<br><sub>-,18,2,-,-</sub> | 3.0<br><sub>-,2,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,2,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.6 |

</details>

<details><summary>if Bub Carrington plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 37.4<br><sub>32,39,35,29,41</sub> | 18.9<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.8 | 0.7 | 2.2 | 32.2 |
| Alperen Sengun (HOU) | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.1<br><sub>17,15,20,19,43</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.6 | 1.1 | 3.2 | 43.3 |
| Kevin Durant (HOU) | 98% | 36.6<br><sub>35,38,36,34,33</sub> | 26.3<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 1.0 | 3.4 | 38.2 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.2<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.9 | 1.4 | 26.6 |
| Tari Eason (HOU) | 98% | 30.5<br><sub>24,23,19,22,33</sub> | 12.8<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 7.6<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7 | 0.8 | 1.3 | 22.4 |
| Reed Sheppard (HOU) | 88% | 26.3<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.5 | 1.3 | 19.2 |
| Bogdan Bogdanovic (HOU) | 97% | 16.8<br><sub>5,2,12,10,12</sub> | 6.3<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams (HOU) | 21% | 15.2<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 5.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.6 | 0.9 | 10.9 |
| Oscar Tshiebwe (HOU) | 91% | 12.1<br><sub>2,3,-,1,6</sub> | 4.5<br><sub>2,2,-,0,0</sub> |  | 5.3<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.5 | 10.5 |
| Jae'Sean Tate (HOU) | 52% | 11.0<br><sub>-,-,-,1,-</sub> | 3.1<br><sub>-,-,-,0,-</sub> |  | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 6.4 |
| Bruce Thornton (HOU) | 58% | 10.9<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.3 |
| Isaiah Crawford (HOU) | 58% | 9.9<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.8 |
| Trae Young (WAS) | 98% | 37.5<br><sub>37,28,38,34,45</sub> | 21.8<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 9.3<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.7 | 34.4 |
| Anthony Davis (WAS) | 98% | 37.2<br><sub>-,-,34,34,44</sub> | 24.3<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 11.9<br><sub>-,-,13,13,15</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.4 | 1.6 | 2.4 | 39.1 |
| AJ Dybantsa (WAS) | 98% | 37.2<br><sub>36,31,37,34,44</sub> | 15.7<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.6 | 2.5 | 24.7 |
| Kyshawn George (WAS) | 98% | 35.2<br><sub>39,30,35,39,26</sub> | 17.3<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 1.1 | 2.5 | 27.0 |
| Bilal Coulibaly (WAS) | 98% | 29.0<br><sub>24,20,-,25,29</sub> | 10.8<br><sub>9,0,-,5,4</sub> |  | 4.4<br><sub>5,5,-,6,7</sub> |  | 1.7<br><sub>0,0,-,2,0</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 1.3 | 1.0 | 1.3 | 16.9 |
| Bub Carrington (WAS) | 100% | 20.9<br><sub>15,21,19,10,16</sub> | 7.1<br><sub>5,9,4,0,2</sub> |  | 2.2<br><sub>1,6,0,0,0</sub> |  | 2.6<br><sub>1,1,4,0,2</sub> |  | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6 | 0.2 | 1.2 | 11.8 |
| Deandre Ayton (WAS) | 98% | 17.6<br><sub>23,7,13,9,9</sub> | 5.8<br><sub>8,2,2,2,2</sub> |  | 5.7<br><sub>11,1,8,2,4</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 12.2 |
| Khris Middleton (WAS) | 35% | 14.9<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 8.2 |
| Will Riley (WAS) | 76% | 12.2<br><sub>9,20,4,-,3</sub> | 4.9<br><sub>7,5,0,-,3</sub> |  | 1.4<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.5<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 7.2 |
| Anthony Gill (WAS) | 43% | 9.4<br><sub>-,9,2,-,-</sub> | 3.2<br><sub>-,1,0,-,-</sub> |  | 1.5<br><sub>-,1,2,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |
| Tre Mann (WAS) | 52% | 8.9<br><sub>-,18,2,-,-</sub> | 3.2<br><sub>-,2,0,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,2,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.9 |

</details>

<details><summary>if Tre Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 37.3<br><sub>32,39,35,29,41</sub> | 18.9<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.9<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.8 | 0.7 | 2.2 | 32.1 |
| Alperen Sengun (HOU) | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.1<br><sub>17,15,20,19,43</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.6 | 1.1 | 3.2 | 43.4 |
| Kevin Durant (HOU) | 98% | 36.6<br><sub>35,38,36,34,33</sub> | 26.3<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 1.0 | 3.5 | 38.2 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.3<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.9 | 1.4 | 26.6 |
| Tari Eason (HOU) | 98% | 30.6<br><sub>24,23,19,22,33</sub> | 12.9<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 7.7<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7 | 0.9 | 1.3 | 22.5 |
| Reed Sheppard (HOU) | 88% | 26.3<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7 | 0.5 | 1.2 | 19.2 |
| Bogdan Bogdanovic (HOU) | 97% | 16.7<br><sub>5,2,12,10,12</sub> | 6.3<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams (HOU) | 21% | 15.3<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 6.0<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.5 | 0.9 | 10.9 |
| Oscar Tshiebwe (HOU) | 91% | 12.0<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.3<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.6 |
| Jae'Sean Tate (HOU) | 52% | 10.9<br><sub>-,-,-,1,-</sub> | 3.0<br><sub>-,-,-,0,-</sub> |  | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.3 |
| Bruce Thornton (HOU) | 58% | 10.9<br><sub>-,-,1,3,-</sub> | 3.0<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.3 |
| Isaiah Crawford (HOU) | 58% | 9.8<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.8 |
| Trae Young (WAS) | 98% | 37.3<br><sub>37,28,38,34,45</sub> | 21.1<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 9.4<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.5 | 33.7 |
| Anthony Davis (WAS) | 98% | 36.9<br><sub>-,-,34,34,44</sub> | 23.2<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 11.9<br><sub>-,-,13,13,15</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.4 | 1.7 | 2.4 | 38.0 |
| AJ Dybantsa (WAS) | 98% | 36.8<br><sub>36,31,37,34,44</sub> | 15.4<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 2.4 | 24.3 |
| Kyshawn George (WAS) | 98% | 34.9<br><sub>39,30,35,39,26</sub> | 17.1<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 1.1 | 2.5 | 26.7 |
| Tre Johnson (WAS) | 100% | 28.9<br><sub>27,28,29,29,30</sub> | 11.8<br><sub>23,4,2,15,13</sub> | 9.5 · – | 2.5<br><sub>1,0,2,3,4</sub> | 2.5 | 1.5<br><sub>1,3,0,1,2</sub> | 1.5 | 1.8<br><sub>5,0,0,2,1</sub> | 1.5 | 0.9 | 0.2 | 1.4 | 15.8 |
| Bilal Coulibaly (WAS) | 98% | 28.2<br><sub>24,20,-,25,29</sub> | 10.0<br><sub>9,0,-,5,4</sub> |  | 4.3<br><sub>5,5,-,6,7</sub> |  | 1.7<br><sub>0,0,-,2,0</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 1.3 | 0.9 | 1.2 | 16.0 |
| Deandre Ayton (WAS) | 98% | 16.6<br><sub>23,7,13,9,9</sub> | 5.4<br><sub>8,2,2,2,2</sub> |  | 5.4<br><sub>11,1,8,2,4</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.6 | 11.5 |
| Khris Middleton (WAS) | 35% | 14.2<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.9 | 7.6 |
| Will Riley (WAS) | 76% | 11.7<br><sub>9,20,4,-,3</sub> | 4.6<br><sub>7,5,0,-,3</sub> |  | 1.3<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.4<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 6.8 |
| Anthony Gill (WAS) | 43% | 8.6<br><sub>-,9,2,-,-</sub> | 2.9<br><sub>-,1,0,-,-</sub> |  | 1.4<br><sub>-,1,2,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Tre Mann (WAS) | 52% | 8.4<br><sub>-,18,2,-,-</sub> | 3.0<br><sub>-,2,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,2,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.6 |

</details>


### ATL @ MIL
Out: Ousmane Dieng (MIL), Kam Jones (MIL), Pete Nance (MIL), Cormac Ryan (MIL), Kingston Flemings (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Asa Newell (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.3–111.6 | ATL 71% | 1.41 / 3.44 | MIL +7.5 | 230.5 | MIL +7.5 covers 49%; o234.5 42% |
| Expected (weighted by chance each plays) | 119.4–111.5 | ATL 71% | 1.40 / 3.49 | MIL +8.5 | 230.5 | MIL +7.5 covers 48%; o234.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 8.5 | 3.6 | 1.4 | 0.7 | 0.3 | 0.2 | 0.1 | 0.4 | 5.7 | small |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 34.7<br><sub>-,-,36,38,40</sub> | 21.9<br><sub>-,-,30,15,27</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 9.3<br><sub>-,-,7,7,11</sub> | 9.5<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>-,-,6,4,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.5 | 3.0 | 38.9 |
| Nickeil Alexander-Walker | 98% | 33.5<br><sub>32,33,31,34,41</sub> | 22.1<br><sub>26,28,20,20,16</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>4,2,3,4,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>2,2,1,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.6<br><sub>6,4,2,4,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.5 | 2.1 | 29.1 |
| Dyson Daniels | 98% | 31.9<br><sub>34,35,31,31,36</sub> | 10.3<br><sub>8,13,9,10,6</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 7.6<br><sub>16,9,10,6,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 6.1<br><sub>8,12,7,8,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 2.4 | 0.4 | 1.4 | 24.0 |
| Onyeka Okongwu | 98% | 31.4<br><sub>31,33,30,30,35</sub> | 14.7<br><sub>14,22,16,16,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>16,10,2,9,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>4,1,5,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 1.0 | 1.4 | 25.6 |
| CJ McCollum | 98% | 27.4<br><sub>25,23,21,24,32</sub> | 16.8<br><sub>15,4,9,21,20</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>5,3,4,0,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.2<br><sub>5,4,3,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>2,0,1,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.6 | 1.9 | 24.1 |
| Aaron Wiggins | 98% | 24.7<br><sub>29,29,26,23,26</sub> | 12.6<br><sub>15,19,20,15,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>4,4,4,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>2,3,6,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>3,3,5,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.4 | 1.1 | 18.3 |
| Luguentz Dort | 98% | 22.2<br><sub>31,32,20,18,20</sub> | 7.6<br><sub>6,25,3,4,10</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>3,7,2,3,1</sub> |  | 1.6<br><sub>3,4,1,2,2</sub> |  | 1.2<br><sub>2,5,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 0.6 | 12.1 |
| Jock Landale | 86% | 14.9<br><sub>-,-,-,14,18</sub> | 7.0<br><sub>-,-,-,5,12</sub> |  | 4.1<br><sub>-,-,-,5,5</sub> |  | 1.4<br><sub>-,-,-,1,0</sub> |  | 0.6<br><sub>-,-,-,1,1</sub> |  | 0.4 | 0.4 | 0.7 | 12.4 |
| Corey Kispert | 52% | 10.1<br><sub>8,16,-,-,-</sub> | 5.7<br><sub>9,7,-,-,-</sub> |  | 1.3<br><sub>0,2,-,-,-</sub> |  | 0.9<br><sub>1,1,-,-,-</sub> |  | 0.7<br><sub>1,1,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 7.8 |
| Zuby Ejiofor | 63% | 9.8<br><sub>17,15,18,4,-</sub> | 3.6<br><sub>11,10,7,0,-</sub> |  | 2.3<br><sub>3,5,6,0,-</sub> |  | 1.0<br><sub>2,5,0,0,-</sub> |  | 0.3<br><sub>1,0,1,0,-</sub> |  | 0.4 | 0.2 | 0.5 | 6.9 |
| RayJ Dennis | 52% | 8.4<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.6 |
| Dorian Finney-Smith | 26% | 6.5<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.5 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 33.2<br><sub>35,27,-,35,34</sub> | 21.4<br><sub>23,13,-,27,18</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>5,1,-,2,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>10,2,-,7,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,1,-,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 2.7 | 31.4 |
| Kyle Kuzma | 98% | 29.1<br><sub>32,31,26,24,31</sub> | 13.3<br><sub>13,27,5,9,14</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>4,4,5,1,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>3,0,3,1,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>1,6,1,1,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.5 | 2.1 | 21.8 |
| Jaime Jaquez Jr. | 98% | 28.8<br><sub>28,23,25,30,28</sub> | 15.9<br><sub>14,4,16,25,22</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>3,2,5,5,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>3,2,3,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>2,0,2,2,5</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.2 | 2.2 | 25.9 |
| Myles Turner | 98% | 27.9<br><sub>24,24,27,-,31</sub> | 10.5<br><sub>0,3,3,-,14</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>7,5,3,-,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>0,7,2,-,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>0,0,1,-,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 1.8 | 1.8 | 19.1 |
| Ryan Rollins | 98% | 26.4<br><sub>14,20,24,24,29</sub> | 13.3<br><sub>10,7,14,8,8</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>1,5,5,7,10</sub> |  | 5.2<br><sub>1,6,2,4,2</sub> |  | 1.8<br><sub>1,2,4,2,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.4 | 2.7 | 23.1 |
| Brayden Burries | 98% | 23.4<br><sub>38,29,26,23,19</sub> | 9.5<br><sub>21,13,3,8,3</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>11,8,3,5,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>6,4,3,1,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.9<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.3 | 1.4 | 17.3 |
| Nate Ament | 93% | 20.0<br><sub>15,23,22,22,22</sub> | 8.1<br><sub>7,12,10,2,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>1,5,2,4,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.0<br><sub>0,1,1,1,1</sub> |  | 0.9<br><sub>0,2,2,0,2</sub> |  | 0.7 | 0.3 | 1.0 | 12.3 |
| Kel'el Ware | 96% | 17.1<br><sub>13,9,17,23,17</sub> | 8.0<br><sub>4,0,8,8,10</sub> |  | 6.1<br><sub>3,0,4,5,6</sub> |  | 1.0<br><sub>0,1,1,1,1</sub> |  | 0.6<br><sub>0,0,0,0,2</sub> |  | 0.5 | 0.9 | 1.4 | 15.2 |
| AJ Green | 98% | 16.0<br><sub>24,18,8,8,8</sub> | 5.6<br><sub>12,5,0,3,0</sub> |  | 1.6<br><sub>1,1,0,1,0</sub> |  | 1.1<br><sub>0,1,0,1,2</sub> |  | 1.0<br><sub>4,1,0,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 8.4 |
| Gary Trent Jr. | 63% | 13.9<br><sub>-,-,6,4,16</sub> | 6.2<br><sub>-,-,5,6,1</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,1,2,0</sub> |  | 0.5 | 0.1 | 0.6 | 7.7 |
| Caris LeVert | 8% | 13.2<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 8.2 |
| Kasparas Jakucionis | 72% | 12.7<br><sub>10,7,23,4,-</sub> | 4.7<br><sub>3,1,11,4,-</sub> |  | 1.6<br><sub>0,2,0,2,-</sub> |  | 2.2<br><sub>2,0,4,0,-</sub> |  | 0.4<br><sub>0,0,2,0,-</sub> |  | 0.5 | 0.1 | 1.1 | 8.5 |
| Jericho Sims | 66% | 11.5<br><sub>7,15,8,18,-</sub> | 2.5<br><sub>0,2,2,0,-</sub> |  | 3.1<br><sub>1,2,0,4,-</sub> |  | 1.1<br><sub>0,0,0,1,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.2 | 0.8 | 6.7 |

</details>


### OKC @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander REB over 3.5 (4+) | OKC @ SAC | draftkings | 2.21 | 1.99 | 1.91 | 52.5% | 50.0% | 50.3% | +11.2% | +16.0% | 2.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.9–107.2 | OKC 82% | 1.23 / 5.40 | SAC +12.5 | 226.5 | SAC +10.5 covers 44%; o222.5 60% |
| Expected (weighted by chance each plays) | 119.8–108.0 | OKC 78% | 1.27 / 4.65 | SAC +11.5 | 227.5 | SAC +10.5 covers 46%; o222.5 62% |
| if Precious Achiuwa plays | 119.4–107.4 | OKC 80% | 1.25 / 5.05 | SAC +11.5 | 226.5 | SAC +10.5 covers 46%; o222.5 59% |
| if Keegan Murray plays | 119.4–107.3 | OKC 80% | 1.24 / 5.11 | SAC +12.5 | 226.5 | SAC +10.5 covers 46%; o222.5 59% |
| if Ajay Mitchell plays | 120.8–107.2 | OKC 83% | 1.20 / 5.90 | SAC +13.5 | 227.5 | SAC +10.5 covers 41%; o222.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa (SAC) | Questionable | 55% | 25.5 | 10.8 | 7.1 | 1.5 | 0.5 | 0.9 | 0.9 | 1.2 | 19.5 | full tables below |
| Keegan Murray (SAC) | Questionable | 55% | 31.1 | 12.1 | 5.0 | 1.7 | 1.7 | 0.8 | 1.1 | 1.2 | 18.8 | full tables below |
| Ajay Mitchell (OKC) | Questionable | 55% | 26.0 | 15.4 | 3.3 | 3.6 | 0.9 | 1.3 | 0.3 | 1.5 | 22.3 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.7<br><sub>28,30,26,31,40</sub> | 33.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.5 | 0.8 | 2.6 | 46.2 |
| Jared McCain | 98% | 29.7<br><sub>29,23,31,31,31</sub> | 16.8<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.6 | 22.5 |
| Isaiah Hartenstein | 98% | 28.4<br><sub>26,18,24,34,30</sub> | 11.5<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 11.3<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.9 |
| Kenrich Williams | 98% | 27.2<br><sub>19,23,19,26,35</sub> | 10.9<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,4,2,2,8</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.0 | 18.5 |
| Alex Caruso | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.3<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 10.1<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.3 |
| Bennett Stirtz | 98% | 19.6<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.3<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix | 67% | 17.8<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 9.8 |
| Micah Peavy | 88% | 17.0<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford | 96% | 15.0<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.9 |
| Nikola Topic | 72% | 14.2<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.2 |
| Brooks Barnhizer | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 38.4<br><sub>42,33,39,40,35</sub> | 23.9<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.3 | 3.8 | 35.6 |
| De'Andre Hunter | 98% | 36.6<br><sub>38,-,31,34,42</sub> | 16.9<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.1 | 24.4 |
| Zach LaVine | 98% | 35.0<br><sub>35,35,25,33,36</sub> | 20.1<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.6 | 26.6 |
| Domantas Sabonis | 98% | 34.3<br><sub>35,31,-,24,35</sub> | 15.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.9<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>1,5,-,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.6<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.3 | 3.0 | 34.7 |
| Leaky Black | 80% | 22.0<br><sub>22,40,20,18,12</sub> | 5.6<br><sub>3,12,6,0,0</sub> |  | 3.6<br><sub>6,3,5,3,0</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.9<br><sub>0,4,2,0,0</sub> |  | 1.0 | 0.5 | 0.7 | 10.6 |
| Dylan Cardwell | 98% | 19.5<br><sub>13,15,18,29,13</sub> | 5.6<br><sub>4,9,4,1,6</sub> |  | 7.0<br><sub>6,2,9,11,3</sub> |  | 1.6<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 14.2 |
| Malik Monk | 98% | 18.2<br><sub>24,18,21,3,18</sub> | 10.1<br><sub>13,12,9,1,7</sub> |  | 1.8<br><sub>2,0,2,0,4</sub> |  | 3.0<br><sub>3,7,3,0,3</sub> |  | 1.4<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.4 | 14.8 |
| Emanuel Sharp | 98% | 16.4<br><sub>10,31,12,19,7</sub> | 5.0<br><sub>3,9,5,2,4</sub> |  | 1.5<br><sub>1,5,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.7<br><sub>1,3,1,0,0</sub> |  | 0.5 | 0.2 | 0.6 | 7.3 |
| Alex Karaban | 48% | 13.1<br><sub>-,11,-,-,-</sub> | 4.3<br><sub>-,0,-,-,-</sub> |  | 1.9<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 7.0 |
| Daeqwon Plowden | 83% | 12.0<br><sub>-,-,12,2,2</sub> | 4.3<br><sub>-,-,6,0,0</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,2,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.2 |
| Mason Plumlee | 30% | 11.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.5 | 0.7 | 7.2 |

</details>

<details><summary>if Precious Achiuwa plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.7<br><sub>28,30,26,31,40</sub> | 33.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.5 | 0.8 | 2.6 | 46.3 |
| Jared McCain (OKC) | 98% | 29.8<br><sub>29,23,31,31,31</sub> | 16.9<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 1.6 | 22.7 |
| Isaiah Hartenstein (OKC) | 98% | 28.3<br><sub>26,18,24,34,30</sub> | 11.4<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 11.2<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.7 |
| Kenrich Williams (OKC) | 98% | 27.3<br><sub>19,23,19,26,35</sub> | 10.9<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,4,2,2,8</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.0 | 18.5 |
| Alex Caruso (OKC) | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.3<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara (OKC) | 98% | 24.6<br><sub>18,27,26,32,21</sub> | 10.1<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.3 |
| Bennett Stirtz (OKC) | 98% | 19.7<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix (OKC) | 67% | 17.8<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 9.7 |
| Micah Peavy (OKC) | 88% | 16.9<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford (OKC) | 96% | 15.1<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 9.0 |
| Nikola Topic (OKC) | 72% | 14.3<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.2 |
| Brooks Barnhizer (OKC) | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Darius Acuff Jr. (SAC) | 98% | 37.0<br><sub>42,33,39,40,35</sub> | 22.6<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.7 | 33.9 |
| De'Andre Hunter (SAC) | 98% | 34.2<br><sub>38,-,31,34,42</sub> | 14.9<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 1.9 | 21.8 |
| Zach LaVine (SAC) | 98% | 33.4<br><sub>35,35,25,33,36</sub> | 18.9<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.5 | 25.0 |
| Domantas Sabonis (SAC) | 98% | 33.0<br><sub>35,31,-,24,35</sub> | 14.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.5<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>1,5,-,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.8 | 33.1 |
| Precious Achiuwa (SAC) | 100% | 25.5<br><sub>17,22,36,14,-</sub> | 10.8<br><sub>7,9,7,10,-</sub> |  | 7.1<br><sub>3,4,14,3,-</sub> |  | 1.5<br><sub>1,0,2,0,-</sub> |  | 0.5<br><sub>1,1,0,1,-</sub> |  | 0.9 | 0.9 | 1.2 | 19.5 |
| Leaky Black (SAC) | 80% | 18.0<br><sub>22,40,20,18,12</sub> | 4.6<br><sub>3,12,6,0,0</sub> |  | 2.9<br><sub>6,3,5,3,0</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.6 |
| Dylan Cardwell (SAC) | 98% | 17.5<br><sub>13,15,18,29,13</sub> | 5.0<br><sub>4,9,4,1,6</sub> |  | 6.2<br><sub>6,2,9,11,3</sub> |  | 1.4<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.9 | 12.6 |
| Malik Monk (SAC) | 98% | 16.6<br><sub>24,18,21,3,18</sub> | 8.9<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.1<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.3 | 13.2 |
| Emanuel Sharp (SAC) | 98% | 13.7<br><sub>10,31,12,19,7</sub> | 4.1<br><sub>3,9,5,2,4</sub> |  | 1.2<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.0 |
| Alex Karaban (SAC) | 48% | 9.2<br><sub>-,11,-,-,-</sub> | 2.9<br><sub>-,0,-,-,-</sub> |  | 1.4<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Daeqwon Plowden (SAC) | 83% | 9.1<br><sub>-,-,12,2,2</sub> | 3.3<br><sub>-,-,6,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Mason Plumlee (SAC) | 30% | 7.6<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>if Keegan Murray plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.6<br><sub>28,30,26,31,40</sub> | 33.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.8 | 2.6 | 46.1 |
| Jared McCain (OKC) | 98% | 29.7<br><sub>29,23,31,31,31</sub> | 16.8<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.6 | 22.6 |
| Isaiah Hartenstein (OKC) | 98% | 28.4<br><sub>26,18,24,34,30</sub> | 11.5<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 11.3<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.9 |
| Kenrich Williams (OKC) | 98% | 27.2<br><sub>19,23,19,26,35</sub> | 10.8<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,4,2,2,8</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.0 | 18.4 |
| Alex Caruso (OKC) | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.2<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara (OKC) | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 10.1<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.3 |
| Bennett Stirtz (OKC) | 98% | 19.6<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix (OKC) | 67% | 17.7<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 9.7 |
| Micah Peavy (OKC) | 88% | 17.0<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford (OKC) | 96% | 14.9<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 9.0 |
| Nikola Topic (OKC) | 72% | 14.4<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.3 |
| Brooks Barnhizer (OKC) | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Darius Acuff Jr. (SAC) | 98% | 36.8<br><sub>42,33,39,40,35</sub> | 22.2<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.7 | 33.5 |
| De'Andre Hunter (SAC) | 98% | 34.0<br><sub>38,-,31,34,42</sub> | 15.0<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 1.9 | 21.8 |
| Zach LaVine (SAC) | 98% | 33.0<br><sub>35,35,25,33,36</sub> | 19.0<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.4 | 25.1 |
| Domantas Sabonis (SAC) | 98% | 32.7<br><sub>35,31,-,24,35</sub> | 14.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.3<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>1,5,-,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.7 | 32.8 |
| Keegan Murray (SAC) | 100% | 31.1<br><sub>-,-,23,24,40</sub> | 12.1<br><sub>-,-,10,11,16</sub> | 11.5 · – | 5.0<br><sub>-,-,1,2,7</sub> | 4.5 | 1.7<br><sub>-,-,2,1,4</sub> |  | 1.7<br><sub>-,-,0,2,2</sub> | 1.5 | 0.8 | 1.1 | 1.2 | 18.8 |
| Leaky Black (SAC) | 80% | 17.3<br><sub>22,40,20,18,12</sub> | 4.4<br><sub>3,12,6,0,0</sub> |  | 2.8<br><sub>6,3,5,3,0</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.6<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.3 |
| Dylan Cardwell (SAC) | 98% | 17.3<br><sub>13,15,18,29,13</sub> | 5.0<br><sub>4,9,4,1,6</sub> |  | 6.2<br><sub>6,2,9,11,3</sub> |  | 1.4<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 12.7 |
| Malik Monk (SAC) | 98% | 16.5<br><sub>24,18,21,3,18</sub> | 8.9<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.1<br><sub>3,2,0,0,0</sub> |  | 0.4 | 0.3 | 1.3 | 13.2 |
| Emanuel Sharp (SAC) | 98% | 13.5<br><sub>10,31,12,19,7</sub> | 4.0<br><sub>3,9,5,2,4</sub> |  | 1.2<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.8 |
| Daeqwon Plowden (SAC) | 83% | 9.0<br><sub>-,-,12,2,2</sub> | 3.2<br><sub>-,-,6,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.3<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.6 |
| Alex Karaban (SAC) | 48% | 8.4<br><sub>-,11,-,-,-</sub> | 2.7<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.4 |
| Mason Plumlee (SAC) | 30% | 7.5<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>if Ajay Mitchell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 32.2<br><sub>30,29,29,36,39</sub> | 31.4<br><sub>28,30,26,31,40</sub> | 33.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.8 | 2.4 | 41.1 |
| Jared McCain (OKC) | 98% | 26.2<br><sub>29,23,31,31,31</sub> | 14.9<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.6<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.1 | 1.4 | 20.0 |
| Ajay Mitchell (OKC) | 100% | 26.0<br><sub>30,22,28,-,-</sub> | 15.4<br><sub>35,12,14,-,-</sub> | 17.5 · – | 3.3<br><sub>1,4,3,-,-</sub> | 3.5 | 3.6<br><sub>5,0,3,-,-</sub> | 3.5 | 0.9<br><sub>4,0,0,-,-</sub> | 1.5 | 1.3 | 0.3 | 1.5 | 22.3 |
| Isaiah Hartenstein (OKC) | 98% | 25.4<br><sub>26,18,24,34,30</sub> | 10.1<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 10.0<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.5 | 23.7 |
| Kenrich Williams (OKC) | 98% | 22.5<br><sub>19,23,19,26,35</sub> | 9.0<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>6,4,2,2,8</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.8 | 15.2 |
| Alex Caruso (OKC) | 98% | 21.7<br><sub>20,13,19,29,27</sub> | 8.9<br><sub>5,0,5,14,5</sub> |  | 3.2<br><sub>6,3,2,7,1</sub> |  | 2.6<br><sub>2,3,1,2,4</sub> |  | 1.3<br><sub>1,0,1,4,1</sub> |  | 1.4 | 0.5 | 0.9 | 14.7 |
| Aday Mara (OKC) | 98% | 21.7<br><sub>18,27,26,32,21</sub> | 8.8<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.6 | 1.6 | 1.3 | 16.2 |
| Bennett Stirtz (OKC) | 98% | 16.3<br><sub>24,29,18,25,12</sub> | 6.6<br><sub>12,11,13,6,5</sub> |  | 1.3<br><sub>1,5,1,1,1</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.0<br><sub>2,2,2,2,1</sub> |  | 0.6 | 0.1 | 0.5 | 9.0 |
| Josh Dix (OKC) | 67% | 15.2<br><sub>15,21,-,-,17</sub> | 5.6<br><sub>5,2,-,-,0</sub> |  | 1.9<br><sub>2,1,-,-,4</sub> |  | 0.8<br><sub>1,2,-,-,3</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.3 |
| Nique Clifford (OKC) | 96% | 13.2<br><sub>-,-,20,16,12</sub> | 4.9<br><sub>-,-,4,5,0</sub> |  | 2.0<br><sub>-,-,4,3,0</sub> |  | 1.3<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.2 |
| Micah Peavy (OKC) | 88% | 13.1<br><sub>18,23,21,12,-</sub> | 3.7<br><sub>7,7,0,0,-</sub> |  | 2.3<br><sub>4,3,2,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.3<br><sub>1,1,0,0,-</sub> |  | 0.5 | 0.2 | 0.3 | 6.4 |
| Nikola Topic (OKC) | 72% | 11.5<br><sub>-,-,-,-,16</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 2.7<br><sub>-,-,-,-,3</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.1 | 1.1 | 7.7 |
| Brooks Barnhizer (OKC) | 52% | 7.0<br><sub>5,8,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 1.6<br><sub>0,4,1,-,-</sub> |  | 0.6<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Darius Acuff Jr. (SAC) | 98% | 38.4<br><sub>42,33,39,40,35</sub> | 23.8<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.3 | 3.8 | 35.5 |
| De'Andre Hunter (SAC) | 98% | 36.6<br><sub>38,-,31,34,42</sub> | 16.8<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.1 | 24.3 |
| Zach LaVine (SAC) | 98% | 34.9<br><sub>35,35,25,33,36</sub> | 20.1<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.6 | 26.6 |
| Domantas Sabonis (SAC) | 98% | 34.4<br><sub>35,31,-,24,35</sub> | 15.8<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 13.0<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>1,5,-,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.3 | 2.9 | 34.6 |
| Leaky Black (SAC) | 80% | 22.0<br><sub>22,40,20,18,12</sub> | 5.6<br><sub>3,12,6,0,0</sub> |  | 3.6<br><sub>6,3,5,3,0</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.9<br><sub>0,4,2,0,0</sub> |  | 1.0 | 0.5 | 0.7 | 10.6 |
| Dylan Cardwell (SAC) | 98% | 19.5<br><sub>13,15,18,29,13</sub> | 5.5<br><sub>4,9,4,1,6</sub> |  | 7.0<br><sub>6,2,9,11,3</sub> |  | 1.6<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 14.1 |
| Malik Monk (SAC) | 98% | 18.3<br><sub>24,18,21,3,18</sub> | 10.2<br><sub>13,12,9,1,7</sub> |  | 1.8<br><sub>2,0,2,0,4</sub> |  | 3.0<br><sub>3,7,3,0,3</sub> |  | 1.4<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.4 | 15.0 |
| Emanuel Sharp (SAC) | 98% | 16.5<br><sub>10,31,12,19,7</sub> | 5.0<br><sub>3,9,5,2,4</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.7<br><sub>1,3,1,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.2 |
| Alex Karaban (SAC) | 48% | 13.1<br><sub>-,11,-,-,-</sub> | 4.4<br><sub>-,0,-,-,-</sub> |  | 1.9<br><sub>-,1,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 7.0 |
| Daeqwon Plowden (SAC) | 83% | 12.0<br><sub>-,-,12,2,2</sub> | 4.3<br><sub>-,-,6,0,0</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.2 |
| Mason Plumlee (SAC) | 30% | 11.1<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.5 | 0.6 | 7.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-15/`._
