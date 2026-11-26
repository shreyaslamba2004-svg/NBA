# NBA model · Wed 25 Nov 2026 (US date)

Updated **Thu 26 Nov, 11:36 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-25/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| CLE to win | CLE @ NYK | draftkings | 2.51 | 2.19 | 2.78 | 35.9% | 45.8% | 45.8% | +14.8% | -9.8% | 2.0% |
| Jose Alvarado PTS over 7.5 (8+) | CLE @ NYK | draftkings | 2.59 | 2.43 | 2.52 | 39.7% | 41.4% | 41.1% | +6.4% | +2.9% | 1.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson PRA over 54.5 (55+) | CLE @ NYK | draftkings | 19.00 | 16.39 | 8.75 | 11.4% | 4.9% | 6.1% | +15.8% | +117.1% | 0.2% |
| Cam Spencer AST over 9.5 (10+) | LAC @ MEM | draftkings | 14.20 | 12.25 | 6.54 | 15.3% | 6.6% | 8.2% | +15.8% | +117.0% | 0.3% |
| Draymond Green AST over 9.5 (10+) | SAC @ GSW | draftkings | 15.60 | 13.55 | 7.32 | 13.7% | 6.0% | 7.4% | +15.1% | +113.2% | 0.3% |
| Jalen Brunson PA over 49.5 (50+) | CLE @ NYK | draftkings | 15.80 | 13.76 | 7.47 | 13.4% | 5.9% | 7.3% | +14.8% | +111.6% | 0.2% |
| Kevin Durant AST over 7.5 (8+) | PHX @ HOU | draftkings | 15.60 | 13.74 | 7.63 | 13.1% | 6.0% | 7.3% | +13.5% | +104.4% | 0.2% |
| Jalen Brunson PTS over 44.5 (45+) | CLE @ NYK | draftkings | 21.00 | 18.59 | 10.41 | 9.6% | 4.5% | 5.4% | +13.1% | +101.7% | 0.2% |
| Jalen Brunson PTS over 39.5 (40+) | CLE @ NYK | draftkings | 11.40 | 10.15 | 5.78 | 17.3% | 8.2% | 9.8% | +12.2% | +97.2% | 0.3% |
| Jalen Brunson PRA over 49.5 (50+) | CLE @ NYK | draftkings | 9.80 | 8.82 | 5.13 | 19.5% | 9.5% | 11.3% | +11.1% | +91.2% | 0.3% |
| Shai Gilgeous-Alexander PA over 59.5 (60+) | MIN @ OKC | draftkings | 26.00 | 23.42 | 13.64 | 7.3% | 3.6% | 4.3% | +11.1% | +90.7% | 0.1% |
| Jalen Brunson PA over 54.5 (55+) | CLE @ NYK | draftkings | 25.00 | 22.52 | 13.17 | 7.6% | 3.7% | 4.4% | +10.9% | +89.9% | 0.1% |
| Jalen Brunson PR over 44.5 (45+) | CLE @ NYK | draftkings | 12.60 | 11.45 | 6.83 | 14.6% | 7.4% | 8.7% | +9.9% | +84.5% | 0.2% |
| Jalen Brunson PR over 49.5 (50+) | CLE @ NYK | draftkings | 22.00 | 20.04 | 11.96 | 8.4% | 4.2% | 5.0% | +9.8% | +83.9% | 0.1% |
| Amen Thompson PRA over 39.5 (40+) | PHX @ HOU | draftkings | 15.20 | 13.87 | 8.33 | 12.0% | 6.2% | 7.2% | +9.6% | +82.5% | 0.2% |
| Shai Gilgeous-Alexander PRA over 64.5 (65+) | MIN @ OKC | draftkings | 24.00 | 21.98 | 13.26 | 7.5% | 3.9% | 4.5% | +9.3% | +81.0% | 0.1% |
| Amen Thompson PA over 29.5 (30+) | PHX @ HOU | draftkings | 12.00 | 10.99 | 6.66 | 15.0% | 7.8% | 9.1% | +9.2% | +80.2% | 0.2% |
| Jalen Brunson PA over 44.5 (45+) | CLE @ NYK | draftkings | 8.00 | 7.36 | 4.51 | 22.2% | 11.7% | 13.6% | +8.7% | +77.5% | 0.3% |
| Zach Edey REB over 13.5 (14+) | LAC @ MEM | draftkings | 13.20 | 12.17 | 7.47 | 13.4% | 7.1% | 8.2% | +8.5% | +76.8% | 0.2% |
| Cam Spencer AST over 7.5 (8+) | LAC @ MEM | draftkings | 5.40 | 5.01 | 3.12 | 32.0% | 17.3% | 20.0% | +7.8% | +72.9% | 0.4% |
| Amen Thompson AST over 5.5 (6+) | PHX @ HOU | draftkings | 6.77 | 6.29 | 3.93 | 25.4% | 13.8% | 15.9% | +7.7% | +72.1% | 0.3% |
| Amen Thompson PRA over 34.5 (35+) | PHX @ HOU | draftkings | 7.00 | 6.51 | 4.08 | 24.5% | 13.4% | 15.4% | +7.6% | +71.4% | 0.3% |
| Draymond Green AST over 7.5 (8+) | SAC @ GSW | draftkings | 5.75 | 5.36 | 3.40 | 29.4% | 16.2% | 18.6% | +7.1% | +69.1% | 0.4% |
| Amen Thompson AST over 7.5 (8+) | PHX @ HOU | draftkings | 21.00 | 19.65 | 12.53 | 8.0% | 4.5% | 5.1% | +6.9% | +67.6% | 0.1% |
| Zach Edey REB over 15.5 (16+) | LAC @ MEM | draftkings | 25.00 | 23.47 | 15.15 | 6.6% | 3.7% | 4.3% | +6.4% | +65.0% | 0.1% |
| Jalen Brunson PR over 39.5 (40+) | CLE @ NYK | draftkings | 6.58 | 6.20 | 4.02 | 24.9% | 14.2% | 16.1% | +6.1% | +63.5% | 0.3% |
| Amen Thompson PA over 34.5 (35+) | PHX @ HOU | draftkings | 25.00 | 23.70 | 15.58 | 6.4% | 3.7% | 4.2% | +5.6% | +60.4% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CLE @ NYK | Thu 26 Nov 11:30 | 108.9–113.8 | CLE 36% | 2.78 / 1.56 | NYK -5.5 | 222.5 | NYK -4.5 covers 52%; o221.5 53% |
| MIN @ OKC | Thu 26 Nov 11:30 | 112.6–115.4 | MIN 42% | 2.36 / 1.74 | OKC -2.5 | 227.5 | OKC -2.5 covers 51%; o223.5 59% |
| LAC @ MEM | Thu 26 Nov 12:00 | 115.6–117.7 | LAC 44% | 2.27 / 1.79 | MEM -2.5 | 233.5 | MEM -7.5 covers 35%; o227.5 62% |
| BKN @ MIL | Thu 26 Nov 12:00 | 108.5–115.5 | BKN 31% | 3.24 / 1.45 | MIL -7.5 | 223.5 | MIL -1.5 covers 66%; o234.5 28% |
| PHX @ HOU | Thu 26 Nov 12:30 | 110.8–117.4 | PHX 32% | 3.14 / 1.47 | HOU -6.5 | 228.5 | HOU -9.5 covers 42%; o222.5 62% |
| SAC @ GSW | Thu 26 Nov 14:00 | 105.9–114.2 | SAC 28% | 3.62 / 1.38 | GSW -8.5 | 219.5 | GSW -7.5 covers 52%; o215.5 59% |
| SAS @ POR | Thu 26 Nov 14:00 | 111.0–113.2 | SAS 43% | 2.30 / 1.77 | POR -2.5 | 223.5 | POR +3.5 covers 65%; o227.5 43% |

### CLE @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Miles McBride (NYK), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jose Alvarado PTS over 7.5 (8+) | CLE @ NYK | draftkings | 2.59 | 2.43 | 2.52 | 39.7% | 41.4% | 41.1% | +6.4% | +2.9% | 1.0% |
| Peyton Watson PTS under 11.5 | CLE @ NYK | pointsbetau | 2.00 | 1.94 | 1.67 | 59.9% | 49.6% | 51.5% | +2.9% | +19.8% | 0.7% |
| Jarrett Allen PTS under 12.5 | CLE @ NYK | pointsbetau | 2.00 | 1.98 | 1.68 | 59.7% | 48.6% | 50.6% | +1.2% | +19.4% | 0.3% |
| Mikal Bridges PTS under 12.5 | CLE @ NYK | tab | 1.90 | 1.88 | 1.88 | 53.1% | 53.1% | 53.1% | +1.0% | +1.0% | 0.3% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 99% | 33.4<br><sub>-,34,36,40,37</sub> | 17.8<br><sub>-,9,14,51,21</sub> | 16.5 · 17.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>-,4,6,6,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>-,10,9,6,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>-,2,3,7,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.5 | 3.1 | 27.9 |
| Donovan Mitchell | 99% | 32.4<br><sub>-,36,35,29,37</sub> | 22.2<br><sub>-,39,34,20,28</sub> | 24.5 · 24.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>-,4,4,3,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>-,4,3,3,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>-,2,2,2,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 2.6 | 30.6 |
| Jarrett Allen | 88% | 26.3<br><sub>-,30,30,31,29</sub> | 11.9<br><sub>-,13,19,6,16</sub> | 13.5 · 12.5<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>-,14,9,8,4</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>-,3,4,4,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.2 | 20.2 |
| Peyton Watson | 88% | 25.8<br><sub>-,22,-,29,29</sub> | 10.9<br><sub>-,14,-,15,8</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,4,-,4,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>-,0,-,3,3</sub> |  | 1.1<br><sub>-,2,-,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.2 | 1.5 | 16.8 |
| Sam Merrill | 98% | 21.2<br><sub>-,-,23,25,25</sub> | 7.3<br><sub>-,-,7,6,12</sub> | 8.5 · 8.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>-,-,2,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>-,-,3,1,2</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.1 | 0.6 | 10.8 |
| Meleek Thomas | 97% | 21.0<br><sub>34,30,22,20,21</sub> | 9.4<br><sub>20,10,14,4,13</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>4,6,2,1,3</sub> |  | 1.4<br><sub>2,3,2,4,2</sub> |  | 1.4<br><sub>3,1,4,0,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 0.9 | 13.2 |
| Tyrese Proctor | 97% | 20.3<br><sub>34,29,26,24,21</sub> | 7.8<br><sub>24,17,8,5,4</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>11,3,1,1,2</sub> |  | 2.1<br><sub>10,2,1,2,2</sub> |  | 1.1<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.1 | 0.9 | 12.4 |
| Jaylon Tyson | 98% | 16.9<br><sub>34,-,-,-,12</sub> | 6.3<br><sub>18,-,-,-,0</sub> |  | 2.7<br><sub>4,-,-,-,2</sub> |  | 1.3<br><sub>4,-,-,-,0</sub> |  | 0.8<br><sub>3,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.8 | 10.3 |
| Mario Hezonja | 99% | 14.3<br><sub>34,15,28,20,12</sub> | 6.0<br><sub>22,9,16,10,4</sub> |  | 3.4<br><sub>7,4,7,10,5</sub> |  | 1.1<br><sub>4,2,5,3,0</sub> |  | 0.6<br><sub>2,1,2,2,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.6 |
| Thomas Bryant | 88% | 12.5<br><sub>27,18,12,16,8</sub> | 5.8<br><sub>19,9,5,9,0</sub> |  | 2.9<br><sub>11,5,4,6,2</sub> |  | 0.6<br><sub>3,4,0,0,0</sub> |  | 0.6<br><sub>2,0,1,2,0</sub> |  | 0.3 | 0.4 | 0.5 | 9.3 |
| Norchad Omier | 80% | 10.0<br><sub>27,13,16,6,8</sub> | 2.9<br><sub>13,4,2,2,2</sub> |  | 2.8<br><sub>8,6,7,1,4</sub> |  | 0.9<br><sub>2,2,0,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 6.6 |
| Craig Porter Jr. | 58% | 8.8<br><sub>28,14,12,-,-</sub> | 2.1<br><sub>9,2,2,-,-</sub> |  | 1.6<br><sub>9,1,3,-,-</sub> |  | 1.4<br><sub>6,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 5.0 |
| Riley Minix | 48% | 6.6<br><sub>22,-,-,-,-</sub> | 2.0<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.2 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 36.8<br><sub>41,34,35,36,32</sub> | 29.1<br><sub>28,31,21,30,22</sub> | 25.5 · 25.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>1,5,2,7,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 6.9<br><sub>9,5,7,5,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,4,4,6,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.2 | 2.4 | 39.3 |
| Karl-Anthony Towns | 99% | 34.8<br><sub>43,36,33,-,29</sub> | 23.0<br><sub>28,16,22,-,30</sub> | 22.5 · 22.5<br><sub>o 49% · u 51%</sub> | 14.0<br><sub>17,16,12,-,13</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>3,8,4,-,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>3,1,2,-,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.8 | 2.6 | 41.3 |
| Josh Hart | 98% | 34.3<br><sub>26,31,28,35,39</sub> | 10.2<br><sub>0,5,11,0,10</sub> | 9.5 · 8.5<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>5,4,6,8,11</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>2,2,2,6,10</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>0,1,3,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.3 | 1.5 | 22.6 |
| Landry Shamet | 99% | 32.6<br><sub>30,24,30,36,32</sub> | 13.7<br><sub>23,12,10,20,17</sub> | 13.5 · 12.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,1,1,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>0,1,2,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.6<br><sub>4,2,2,6,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 0.9 | 18.0 |
| Mikal Bridges | 99% | 32.4<br><sub>32,30,31,28,31</sub> | 12.9<br><sub>5,17,8,12,8</sub> | 11.5 · 11.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>7,5,3,2,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>3,1,3,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.5 | 1.2 | 19.4 |
| Jose Alvarado | 84% | 18.7<br><sub>2,7,13,15,22</sub> | 7.0<br><sub>0,2,2,8,11</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>0,0,2,2,1</sub> |  | 3.0<br><sub>1,4,1,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>0,0,0,2,3</sub> |  | 0.8 | 0.2 | 1.0 | 12.3 |
| Andre Drummond | 99% | 18.0<br><sub>7,11,15,23,19</sub> | 5.3<br><sub>2,2,4,7,2</sub> | 4.5 · 4.5<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>3,8,4,13,10</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>0,0,0,1,1</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.7 | 0.9 | 14.6 |
| Tyler Kolek | 96% | 15.8<br><sub>16,13,12,13,11</sub> | 5.4<br><sub>0,4,6,7,8</sub> |  | 2.2<br><sub>0,1,3,3,3</sub> |  | 4.0<br><sub>7,3,5,0,0</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 11.6 |
| Pacome Dadiet | 52% | 15.1<br><sub>-,-,-,11,17</sub> | 5.8<br><sub>-,-,-,5,5</sub> |  | 2.3<br><sub>-,-,-,0,2</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.7<br><sub>-,-,-,1,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.9 |
| Mohamed Diawara | 52% | 14.0<br><sub>-,-,-,-,8</sub> | 4.8<br><sub>-,-,-,-,0</sub> |  | 2.2<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 8.3 |
| James Wiseman | 48% | 13.9<br><sub>3,-,-,25,-</sub> | 4.3<br><sub>0,-,-,5,-</sub> |  | 4.3<br><sub>3,-,-,6,-</sub> |  | 0.6<br><sub>0,-,-,2,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.7 | 0.8 | 9.3 |
| Dalton Knecht | 58% | 9.9<br><sub>-,-,-,3,-</sub> | 3.7<br><sub>-,-,-,0,-</sub> |  | 1.7<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 5.8 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Jaden Akins | 38% | 8.1<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |

</details>


### MIN @ OKC
Out: Chet Holmgren (OKC), Aday Mara (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC), Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| LaMelo Ball PTS under 18.5 | MIN @ OKC | draftkings | 1.96 | 1.94 | 1.73 | 57.6% | 50.3% | 51.6% | +1.2% | +13.1% | 0.3% |

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 35.7<br><sub>31,37,39,36,34</sub> | 18.9<br><sub>13,22,17,25,34</sub> | 17.5 · 17.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>6,5,3,5,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,4,1,4,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>0,2,4,1,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.9 | 2.4 | 28.1 |
| Ayo Dosunmu | 99% | 33.6<br><sub>30,39,32,34,30</sub> | 17.9<br><sub>8,30,6,19,23</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>5,4,4,2,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.6<br><sub>2,5,4,2,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,7,2,1,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.3 | 2.3 | 25.9 |
| Jonathan Kuminga | 88% | 31.8<br><sub>29,-,35,37,26</sub> | 14.1<br><sub>13,-,23,16,15</sub> | 13.5 · 14.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>9,-,3,4,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,-,3,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>1,-,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.6 | 2.0 | 22.3 |
| LaMelo Ball | 99% | 31.3<br><sub>24,31,35,32,30</sub> | 18.1<br><sub>6,18,15,12,17</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>5,9,8,5,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>0,2,8,7,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>2,3,3,1,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 3.0 | 28.4 |
| Rudy Gobert | 99% | 30.9<br><sub>32,22,35,32,27</sub> | 8.6<br><sub>18,0,9,7,7</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>15,4,7,11,6</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>3,2,0,2,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.1 | 1.6 | 20.7 |
| Terrence Shannon Jr. | 98% | 23.9<br><sub>35,24,21,26,24</sub> | 12.7<br><sub>34,12,10,15,17</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>3,1,4,5,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>6,4,3,2,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,1,0,3,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.1 | 1.4 | 17.9 |
| Trey Lyles | 99% | 19.5<br><sub>19,31,16,12,24</sub> | 6.4<br><sub>9,8,8,3,9</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>3,7,6,3,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,4,1,1,2</sub> |  | 0.9<br><sub>2,2,2,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 11.7 |
| Joan Beringer | 98% | 16.1<br><sub>16,26,13,16,19</sub> | 4.8<br><sub>0,3,5,0,0</sub> |  | 5.2<br><sub>4,13,3,4,4</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.3 | 0.7 | 10.4 |
| Bones Hyland | 98% | 15.6<br><sub>13,17,15,16,16</sub> | 8.6<br><sub>5,13,6,7,14</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,2,1,0,2</sub> |  | 2.5<br><sub>5,1,1,4,6</sub> |  | 1.3<br><sub>0,3,1,1,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.2 | 1.1 | 12.7 |
| Cody Williams | 58% | 6.6<br><sub>4,13,-,-,2</sub> | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.9<br><sub>1,1,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 1.3 |
| Zyon Pullin | 52% | 6.4<br><sub>4,-,-,-,2</sub> | 2.9<br><sub>0,-,-,-,4</sub> |  | 0.9<br><sub>1,-,-,-,2</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.7 |
| Isaiah Evans | 52% | 5.9<br><sub>4,-,-,-,2</sub> | 3.2<br><sub>0,-,-,-,2</sub> |  | 1.3<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.1 | 0.4 | 4.8 |
| Johni Broome | 52% | 5.6<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 99% | 36.0<br><sub>30,36,37,-,38</sub> | 32.6<br><sub>37,34,40,-,38</sub> | 32.5 · 32.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,5,3,-,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>2,3,8,-,7</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>4,1,4,-,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.9 | 2.9 | 43.5 |
| Jared McCain | 99% | 31.6<br><sub>30,33,30,29,36</sub> | 16.0<br><sub>12,18,18,20,13</sub> | 13.5 · 15.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,3,3,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,1,0,3,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>1,4,3,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.2 | 1.6 | 21.8 |
| Ajay Mitchell | 99% | 31.2<br><sub>27,34,31,22,35</sub> | 17.6<br><sub>14,13,8,17,12</sub> | 17.5 · 16.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,6,2,3,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.0<br><sub>5,6,4,3,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>1,0,1,2,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.4 | 1.7 | 25.7 |
| Isaiah Hartenstein | 99% | 28.3<br><sub>18,27,28,23,30</sub> | 10.2<br><sub>3,6,5,2,18</sub> | 8.5 · 8.5<br><sub>o 52% · u 48%</sub> | 10.8<br><sub>11,17,8,8,9</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>2,6,4,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.0 | 1.8 | 25.2 |
| Kenrich Williams | 98% | 25.6<br><sub>19,23,28,26,26</sub> | 9.7<br><sub>10,10,6,12,20</sub> | 8.5 · 7.5<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>1,5,2,4,9</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>2,1,4,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>2,0,1,2,4</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.3 | 0.8 | 16.7 |
| Bennett Stirtz | 99% | 21.8<br><sub>17,17,25,32,19</sub> | 8.1<br><sub>0,6,18,21,5</sub> | 8.5 · 6.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,0,2,3,9</sub> |  | 1.7<br><sub>2,2,2,5,3</sub> |  | 1.3<br><sub>0,2,4,5,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.3 | 0.8 | 12.1 |
| Micah Peavy | 93% | 20.2<br><sub>13,-,9,31,24</sub> | 5.2<br><sub>5,-,2,9,7</sub> |  | 3.7<br><sub>3,-,2,6,3</sub> |  | 0.9<br><sub>1,-,0,1,2</sub> |  | 0.5<br><sub>1,-,0,1,1</sub> |  | 0.7 | 0.3 | 0.7 | 9.8 |
| Josh Dix | 67% | 18.4<br><sub>-,-,-,32,16</sub> | 5.3<br><sub>-,-,-,13,0</sub> |  | 2.1<br><sub>-,-,-,5,1</sub> |  | 1.1<br><sub>-,-,-,4,1</sub> |  | 0.6<br><sub>-,-,-,3,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.6 |
| Alex Caruso | 63% | 18.1<br><sub>18,9,-,-,-</sub> | 7.0<br><sub>11,5,-,-,-</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>2,0,-,-,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>3,1,-,-,-</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9<br><sub>1,0,-,-,-</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.4 | 0.8 | 11.9 |
| Nique Clifford | 98% | 14.8<br><sub>24,13,15,26,6</sub> | 5.1<br><sub>9,7,4,11,0</sub> |  | 2.3<br><sub>3,0,5,3,0</sub> |  | 1.0<br><sub>0,0,1,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Brooks Barnhizer | 63% | 11.3<br><sub>4,-,-,19,9</sub> | 3.0<br><sub>0,-,-,8,7</sub> |  | 2.5<br><sub>0,-,-,4,4</sub> |  | 0.8<br><sub>0,-,-,2,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.3 |

</details>


### LAC @ MEM
Out: Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM), Bradley Beal (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keaton Wagler PTS under 8.5 | LAC @ MEM | tab | 2.00 | 1.95 | 1.94 | 51.5% | 51.3% | 51.3% | +2.7% | +3.0% | 0.7% |
| Brook Lopez PTS over 11.5 (12+) | LAC @ MEM | pointsbetau | 2.00 | 1.98 | 1.89 | 53.0% | 49.9% | 50.4% | +0.9% | +5.9% | 0.2% |
| Darius Garland PTS under 19.5 | LAC @ MEM | pointsbetau | 2.00 | 1.99 | 1.76 | 56.8% | 48.9% | 50.4% | +0.7% | +13.7% | 0.2% |
| Jaylen Wells PTS over 9.5 (10+) | LAC @ MEM | pointsbetau | 1.87 | 1.87 | 1.64 | 61.0% | 51.9% | 53.5% | +0.1% | +14.1% | 0.0% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 100% | 30.2<br><sub>35,30,35,32,34</sub> | 19.2<br><sub>27,20,23,16,26</sub> | 19.5 · 19.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>6,3,0,1,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>7,7,5,2,8</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,2,3,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.3 | 3.0 | 28.0 |
| Brandon Ingram | 100% | 27.8<br><sub>-,-,-,-,27</sub> | 15.6<br><sub>-,-,-,-,16</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>-,-,-,-,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>-,-,-,-,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>-,-,-,-,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.7 | 2.1 | 23.3 |
| Rui Hachimura | 100% | 26.9<br><sub>22,27,32,29,29</sub> | 13.2<br><sub>4,20,17,19,19</sub> | 12.5 · 13.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>2,5,7,8,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>0,4,2,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.4 | 1.2 | 19.1 |
| Derrick Jones Jr. | 100% | 25.2<br><sub>26,28,27,26,23</sub> | 9.0<br><sub>13,5,8,4,7</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>4,1,2,7,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,1,1,1,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0<br><sub>3,0,0,1,1</sub> |  | 0.9 | 0.9 | 0.9 | 14.1 |
| Brook Lopez | 100% | 24.0<br><sub>29,23,27,25,21</sub> | 12.8<br><sub>7,23,23,21,3</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,6,3,6,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>8,2,4,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,4,5,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 1.2 | 1.1 | 19.6 |
| Max Strus | 98% | 23.2<br><sub>25,21,32,29,26</sub> | 8.7<br><sub>14,3,18,5,8</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>3,2,5,6,0</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>4,1,4,3,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.4<br><sub>4,1,5,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.2 | 1.0 | 15.0 |
| Kris Dunn | 99% | 21.7<br><sub>18,26,20,19,23</sub> | 6.0<br><sub>7,2,6,3,9</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>3,5,2,4,5</sub> |  | 3.3<br><sub>1,5,2,5,4</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 1.5 | 0.3 | 1.1 | 12.5 |
| Keaton Wagler | 98% | 18.3<br><sub>28,18,17,19,17</sub> | 9.2<br><sub>12,15,7,7,2</sub> | – · 8.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>4,2,5,7,1</sub> |  | 2.5<br><sub>5,0,2,3,2</sub> |  | 1.0<br><sub>2,1,1,1,0</sub> |  | 0.7 | 0.2 | 1.5 | 14.4 |
| Kobe Sanders | 98% | 15.8<br><sub>20,18,14,19,12</sub> | 6.3<br><sub>2,5,0,9,6</sub> |  | 1.8<br><sub>6,1,1,3,0</sub> |  | 1.5<br><sub>4,3,1,1,0</sub> |  | 0.8<br><sub>0,0,0,3,2</sub> |  | 0.7 | 0.1 | 0.8 | 9.6 |
| Isaiah Jackson | 98% | 13.9<br><sub>15,19,9,4,18</sub> | 5.9<br><sub>13,8,6,0,6</sub> |  | 4.2<br><sub>2,5,4,0,6</sub> |  | 1.2<br><sub>2,0,2,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.7 | 1.0 | 1.0 | 11.2 |
| Gradey Dick | 76% | 10.8<br><sub>19,17,13,16,-</sub> | 4.6<br><sub>12,0,2,6,-</sub> |  | 1.7<br><sub>2,0,2,5,-</sub> |  | 0.6<br><sub>0,1,1,2,-</sub> |  | 0.4<br><sub>2,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.9 |
| Yanic Konan Niederhauser | 72% | 9.3<br><sub>-,-,11,16,8</sub> | 3.4<br><sub>-,-,2,6,2</sub> |  | 2.6<br><sub>-,-,3,6,1</sub> |  | 0.6<br><sub>-,-,0,1,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 6.6 |
| Baba Miller | 91% | 7.6<br><sub>5,4,1,3,1</sub> | 3.8<br><sub>2,3,0,1,0</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Cam Christie | 66% | 5.9<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,3,0,3,-</sub> |  | 1.0<br><sub>-,0,0,0,-</sub> |  | 0.5<br><sub>-,0,0,1,-</sub> |  | 0.1<br><sub>-,1,0,1,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Blake Wesley | 52% | 5.6<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.9 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 100% | 30.7<br><sub>27,33,25,30,30</sub> | 16.9<br><sub>18,20,19,23,16</sub> | 16.5 · 16.5<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>8,3,4,7,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 3.7<br><sub>6,5,4,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,4,5,4,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 1.9 | 28.4 |
| Ty Jerome | 100% | 30.4<br><sub>-,-,-,27,29</sub> | 23.5<br><sub>-,-,-,18,29</sub> | 23.5 · 23.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 5.9<br><sub>-,-,-,6,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>-,-,-,3,7</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.2 | 2.9 | 32.9 |
| Jaylen Wells | 100% | 27.3<br><sub>27,26,24,25,20</sub> | 11.7<br><sub>8,5,22,8,8</sub> | 9.5 · 9.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>4,4,7,1,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.1 | 0.9 | 16.4 |
| Cam Spencer | 98% | 24.8<br><sub>32,29,27,30,21</sub> | 11.3<br><sub>12,26,9,9,24</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>6,1,2,5,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>9,7,11,5,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>1,5,1,0,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 1.4 | 20.5 |
| Kris Murray | 100% | 24.0<br><sub>6,6,4,12,32</sub> | 5.6<br><sub>0,5,0,7,9</sub> | 5.5 · 5.5<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>1,0,1,0,3</sub> |  | 1.4<br><sub>0,0,0,0,1</sub> |  | 0.6<br><sub>0,1,0,1,1</sub> |  | 1.0 | 0.5 | 0.7 | 10.5 |
| Zach Edey | 100% | 23.5<br><sub>21,21,-,23,23</sub> | 10.8<br><sub>23,11,-,8,8</sub> | 8.5 · 8.5<br><sub>o 53% · u 47%</sub> | 9.0<br><sub>10,2,-,2,11</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,1,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.2 | 1.5 | 21.0 |
| Javon Small | 98% | 22.5<br><sub>29,21,25,-,19</sub> | 10.0<br><sub>12,2,14,-,3</sub> |  | 3.3<br><sub>5,4,7,-,3</sub> |  | 4.6<br><sub>12,5,7,-,5</sub> |  | 1.3<br><sub>0,0,2,-,0</sub> |  | 0.8 | 0.2 | 1.5 | 17.9 |
| Taylor Hendricks | 91% | 22.4<br><sub>19,21,20,27,24</sub> | 9.7<br><sub>9,18,11,5,3</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>3,6,1,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,2,1,2,1</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 0.9 | 0.5 | 1.0 | 15.8 |
| Olivier-Maxence Prosper | 88% | 18.9<br><sub>16,16,24,23,19</sub> | 9.9<br><sub>12,5,16,7,6</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>0,2,5,6,3</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.7 | 0.2 | 0.8 | 14.6 |
| Isaiah Stewart | 98% | 18.2<br><sub>-,-,18,21,21</sub> | 8.7<br><sub>-,-,8,10,11</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>-,-,4,2,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.9<br><sub>-,-,1,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.3 | 1.0 | 0.9 | 13.3 |
| Jahmai Mashack | 63% | 12.9<br><sub>2,13,26,22,-</sub> | 3.2<br><sub>0,3,0,0,-</sub> |  | 1.6<br><sub>0,2,3,2,-</sub> |  | 1.6<br><sub>1,2,4,1,-</sub> |  | 0.2<br><sub>0,1,0,0,-</sub> |  | 0.6 | 0.2 | 0.8 | 6.4 |
| Quinten Post | 80% | 8.8<br><sub>9,6,10,-,3</sub> | 3.3<br><sub>5,3,5,-,0</sub> |  | 1.7<br><sub>3,2,1,-,0</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,1,0,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.3 |
| Karim Lopez | 48% | 6.6<br><sub>1,-,4,-,-</sub> | 2.1<br><sub>0,-,3,-,-</sub> |  | 1.2<br><sub>0,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,1,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 3.7 |

</details>


### BKN @ MIL
Out: Chaney Johnson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Nolan Traore (BKN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle PTS under 21.5 | BKN @ MIL | draftkings | 1.97 | 1.93 | 1.64 | 60.9% | 49.9% | 51.9% | +2.3% | +20.0% | 0.6% |
| Myles Turner PTS over 9.5 (10+) | BKN @ MIL | pointsbetau | 2.05 | 2.04 | 2.06 | 48.6% | 49.2% | 49.1% | +0.6% | -0.3% | 0.1% |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 100% | 33.8<br><sub>-,40,27,34,31</sub> | 20.2<br><sub>-,25,5,16,11</sub> | 22.5 · 21.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>-,6,3,4,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>-,2,1,5,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.9<br><sub>-,2,1,3,0</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.4 | 2.2 | 29.4 |
| Julius Randle | 100% | 33.6<br><sub>31,34,27,39,35</sub> | 20.2<br><sub>22,33,17,27,29</sub> | 21.5 · 21.5<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>4,6,0,9,4</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>5,1,4,6,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>3,2,3,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 3.3 | 31.4 |
| Mikel Brown Jr. | 100% | 28.1<br><sub>20,18,27,24,29</sub> | 14.1<br><sub>6,3,15,18,17</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>1,1,1,1,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,5,4,0,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,1,2,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 2.4 | 21.4 |
| Egor Demin | 98% | 25.5<br><sub>27,26,31,21,25</sub> | 11.0<br><sub>11,9,22,6,10</sub> | 10.5 · 10.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>1,3,4,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,4,4,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,2,3,0,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.7 | 17.4 |
| Day'Ron Sharpe | 100% | 25.1<br><sub>28,25,22,26,26</sub> | 10.4<br><sub>16,6,6,17,6</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 8.5<br><sub>11,9,5,11,5</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>5,5,1,2,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 23.1 |
| Danny Wolf | 100% | 24.4<br><sub>28,11,23,26,25</sub> | 10.0<br><sub>14,3,6,20,11</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>6,2,6,5,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>1,1,2,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>4,1,1,4,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.6 | 1.3 | 18.3 |
| Noah Clowney | 99% | 23.1<br><sub>35,24,19,22,26</sub> | 8.4<br><sub>15,9,7,0,13</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>7,3,3,2,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>3,3,1,2,1</sub> |  | 1.3<br><sub>3,1,1,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.6 | 1.0 | 13.7 |
| Moritz Wagner | 98% | 17.2<br><sub>18,10,20,22,14</sub> | 8.5<br><sub>10,4,11,3,11</sub> |  | 4.0<br><sub>6,5,2,5,0</sub> |  | 1.5<br><sub>4,1,3,2,1</sub> |  | 0.7<br><sub>2,0,2,1,2</sub> |  | 0.7 | 0.2 | 0.9 | 14.0 |
| Keon Ellis | 91% | 16.9<br><sub>7,20,6,8,16</sub> | 4.1<br><sub>0,8,3,0,6</sub> |  | 1.7<br><sub>0,2,1,1,0</sub> |  | 1.2<br><sub>1,0,0,1,0</sub> |  | 0.6<br><sub>0,2,1,0,2</sub> |  | 0.9 | 0.5 | 0.5 | 6.9 |
| Terance Mann | 64% | 12.2<br><sub>9,-,5,-,3</sub> | 2.9<br><sub>2,-,0,-,0</sub> |  | 1.5<br><sub>1,-,1,-,0</sub> |  | 1.2<br><sub>1,-,0,-,0</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Grant Nelson | 84% | 8.6<br><sub>-,-,-,-,8</sub> | 2.8<br><sub>-,-,-,-,2</sub> |  | 2.0<br><sub>-,-,-,-,1</sub> |  | 0.9<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.6 | 0.5 | 5.7 |
| Josh Minott | 63% | 8.6<br><sub>2,-,4,-,2</sub> | 4.2<br><sub>0,-,0,-,0</sub> |  | 1.6<br><sub>0,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 6.3 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 100% | 29.6<br><sub>20,24,31,40,37</sub> | 20.0<br><sub>5,8,19,50,32</sub> | 22.5 · 22.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>5,2,4,11,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>3,4,3,7,8</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,0,4,7,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.3 | 2.3 | 29.1 |
| Jaime Jaquez Jr. | 100% | 24.8<br><sub>30,23,22,25,25</sub> | 12.9<br><sub>6,10,9,9,3</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>5,2,1,0,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.5<br><sub>4,5,2,1,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.7 | 20.7 |
| Kyle Kuzma | 100% | 24.8<br><sub>22,30,-,33,32</sub> | 13.2<br><sub>14,26,-,12,18</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>6,5,-,5,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,1,-,1,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>3,2,-,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.4 | 1.5 | 20.2 |
| Ryan Rollins | 100% | 23.8<br><sub>-,-,21,28,22</sub> | 12.0<br><sub>-,-,15,8,6</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>-,-,3,6,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>-,-,6,1,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>-,-,1,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.4 | 2.1 | 20.2 |
| Myles Turner | 100% | 23.6<br><sub>23,21,-,26,28</sub> | 10.1<br><sub>8,4,-,5,27</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>7,5,-,6,11</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,4,-,5,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>1,0,-,1,5</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 2.0 | 1.3 | 17.3 |
| Brayden Burries | 99% | 21.7<br><sub>29,25,28,26,29</sub> | 10.7<br><sub>13,20,14,26,14</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>8,7,3,8,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>4,1,3,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>2,3,2,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.4 | 18.4 |
| Kel'el Ware | 98% | 16.7<br><sub>25,17,26,22,23</sub> | 7.5<br><sub>8,11,11,6,9</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>11,3,5,8,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>2,1,0,3,0</sub> |  | 0.5<br><sub>1,1,2,0,1</sub> |  | 0.6 | 1.1 | 1.2 | 13.5 |
| Nate Ament | 98% | 16.3<br><sub>17,17,35,14,25</sub> | 7.0<br><sub>5,7,18,2,7</sub> | 7.5 · 7.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>2,4,9,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.6<br><sub>1,0,2,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 10.4 |
| Cormac Ryan | 52% | 14.0<br><sub>-,-,-,-,-</sub> | 7.1<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 10.1 |
| Pete Nance | 96% | 11.7<br><sub>-,-,28,-,-</sub> | 4.0<br><sub>-,-,7,-,-</sub> |  | 1.9<br><sub>-,-,3,-,-</sub> |  | 1.0<br><sub>-,-,3,-,-</sub> |  | 0.4<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.9 |
| Kasparas Jakucionis | 91% | 11.6<br><sub>26,26,22,10,7</sub> | 5.2<br><sub>25,20,18,2,0</sub> |  | 1.6<br><sub>5,3,3,3,0</sub> |  | 2.3<br><sub>5,5,2,3,3</sub> |  | 0.6<br><sub>4,3,3,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 9.0 |
| AJ Green | 64% | 9.2<br><sub>6,14,-,12,-</sub> | 3.9<br><sub>0,11,-,9,-</sub> |  | 0.9<br><sub>0,0,-,0,-</sub> |  | 0.7<br><sub>0,1,-,0,-</sub> |  | 0.6<br><sub>0,3,-,3,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| Caris LeVert | 63% | 8.4<br><sub>-,8,11,5,8</sub> | 3.5<br><sub>-,8,3,0,0</sub> |  | 1.3<br><sub>-,3,3,1,0</sub> |  | 1.2<br><sub>-,2,1,0,0</sub> |  | 0.2<br><sub>-,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 6.0 |
| Kam Jones | 52% | 8.3<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.2 |
| Gary Trent Jr. | 67% | 8.2<br><sub>30,16,7,-,5</sub> | 3.9<br><sub>18,1,0,-,0</sub> |  | 0.6<br><sub>2,1,1,-,0</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.5<br><sub>4,0,0,-,0</sub> |  | 0.3 | 0.0 | 0.3 | 5.0 |
| Jericho Sims | 58% | 8.0<br><sub>11,18,10,-,-</sub> | 2.0<br><sub>4,4,0,-,-</sub> |  | 2.1<br><sub>2,6,0,-,-</sub> |  | 0.6<br><sub>0,2,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 4.8 |
| Ousmane Dieng | 64% | 7.4<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.1 |
| Bogoljub Markovic | 43% | 5.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.1 |

</details>


### PHX @ HOU
Out: Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX)

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 99% | 35.7<br><sub>28,37,33,38,42</sub> | 24.8<br><sub>17,20,29,23,22</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>4,4,2,2,5</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.9<br><sub>7,8,6,3,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,1,2,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 2.9 | 34.0 |
| Dillon Brooks | 99% | 30.1<br><sub>22,27,31,25,34</sub> | 15.8<br><sub>1,15,29,18,16</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>2,4,3,3,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,4,5,3,7</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,3,5,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 1.4 | 21.6 |
| Jalen Green | 98% | 29.3<br><sub>21,27,30,25,37</sub> | 15.9<br><sub>9,16,18,14,25</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>2,5,7,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>1,3,7,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,2,4,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 2.2 | 22.5 |
| Miles Bridges | 99% | 29.2<br><sub>24,29,29,25,35</sub> | 13.6<br><sub>14,16,13,18,14</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 6.1<br><sub>3,8,6,9,11</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>3,2,5,4,5</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.5 | 1.0 | 22.5 |
| Oso Ighodaro | 98% | 25.4<br><sub>17,33,21,27,30</sub> | 6.4<br><sub>4,8,7,3,7</sub> | 5.5 · –<br><sub>o 55% · u 45%</sub> | 5.7<br><sub>2,11,4,7,4</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,2,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.3 | 14.8 |
| Collin Gillespie | 99% | 25.3<br><sub>28,26,17,27,30</sub> | 10.2<br><sub>26,10,9,16,18</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>4,3,3,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>4,3,1,5,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>5,2,2,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.2 | 1.3 | 16.7 |
| Jordan Goodwin | 98% | 20.0<br><sub>31,20,17,28,18</sub> | 7.2<br><sub>14,11,2,5,6</sub> |  | 3.9<br><sub>7,6,5,9,2</sub> |  | 2.0<br><sub>6,2,3,4,2</sub> |  | 1.1<br><sub>1,1,0,1,2</sub> |  | 1.3 | 0.2 | 0.7 | 13.1 |
| Luke Kennard | 99% | 16.5<br><sub>23,17,17,15,14</sub> | 6.1<br><sub>18,12,3,5,4</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>6,2,3,0,1</sub> |  | 1.4<br><sub>4,0,1,0,2</sub> |  | 0.8<br><sub>3,4,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.5 | 0.1 | 0.6 | 9.3 |
| Khaman Maluach | 98% | 16.3<br><sub>13,11,21,18,16</sub> | 5.8<br><sub>7,4,10,9,8</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>4,6,2,6,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 0.9 | 11.2 |
| Ryan Dunn | 98% | 13.5<br><sub>24,12,13,9,9</sub> | 3.9<br><sub>3,5,6,0,3</sub> |  | 2.9<br><sub>6,1,5,5,2</sub> |  | 0.8<br><sub>1,0,2,0,0</sub> |  | 0.3<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.4 | 7.6 |
| Rasheer Fleming | 38% | 7.3<br><sub>-,-,4,-,-</sub> | 2.7<br><sub>-,-,0,-,-</sub> |  | 1.2<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.1 |
| Jamaree Bouyea | 47% | 6.8<br><sub>-,-,4,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 1.1<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Koa Peat | 64% | 6.2<br><sub>8,1,4,3,-</sub> | 3.0<br><sub>10,0,2,0,-</sub> |  | 1.3<br><sub>2,1,0,0,-</sub> |  | 0.3<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.6 |
| Duop Reath | 38% | 6.0<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.2 | 3.9 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 99% | 36.0<br><sub>30,29,32,35,33</sub> | 22.8<br><sub>25,22,21,16,32</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>4,2,2,4,9</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>5,3,3,4,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>2,2,4,0,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.9 | 3.1 | 33.3 |
| Alperen Sengun | 96% | 34.4<br><sub>28,30,14,36,31</sub> | 21.2<br><sub>19,23,7,28,20</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 9.9<br><sub>8,7,7,11,8</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 6.7<br><sub>8,2,1,10,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>1,1,1,1,1</sub> |  | 1.1 | 1.1 | 3.0 | 37.9 |
| Amen Thompson | 88% | 34.4<br><sub>29,-,31,26,28</sub> | 17.3<br><sub>26,-,15,22,20</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>7,-,9,6,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>7,-,3,0,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>3,-,0,0,1</sub> |  | 1.4 | 0.7 | 2.2 | 28.9 |
| Jabari Smith Jr. | 99% | 34.0<br><sub>28,32,26,32,28</sub> | 14.8<br><sub>9,12,17,21,13</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>6,10,4,4,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>5,1,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>1,1,3,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.7 | 0.8 | 1.3 | 23.4 |
| Fred VanVleet | 88% | 32.5<br><sub>-,26,27,33,31</sub> | 14.4<br><sub>-,8,15,25,6</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>-,5,2,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>-,6,6,9,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>-,2,3,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.4 | 1.5 | 23.0 |
| Tari Eason | 99% | 24.0<br><sub>30,27,25,23,22</sub> | 9.8<br><sub>25,7,11,7,10</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>7,7,4,6,4</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>1,3,3,1,4</sub> |  | 1.0<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.6 | 1.2 | 16.8 |
| Marcus Smart | 67% | 21.3<br><sub>-,-,18,23,25</sub> | 6.7<br><sub>-,-,4,3,4</sub> | 5.5 · –<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>-,-,2,2,3</sub> |  | 2.3<br><sub>-,-,4,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0<br><sub>-,-,1,1,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.1 | 0.4 | 1.4 | 11.3 |
| Reed Sheppard | 96% | 18.7<br><sub>26,19,25,14,17</sub> | 8.5<br><sub>11,5,20,0,5</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,2,4,2,3</sub> |  | 2.4<br><sub>6,2,2,0,5</sub> |  | 1.4<br><sub>3,1,6,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 0.9 | 12.6 |
| Steven Adams | 63% | 14.4<br><sub>12,-,16,12,16</sub> | 4.0<br><sub>6,-,4,2,4</sub> |  | 5.3<br><sub>7,-,5,2,6</sub> |  | 0.9<br><sub>1,-,2,2,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 10.2 |
| Bogdan Bogdanovic | 98% | 10.9<br><sub>22,26,11,5,9</sub> | 4.0<br><sub>12,6,1,0,2</sub> |  | 1.3<br><sub>3,0,3,1,1</sub> |  | 1.0<br><sub>4,1,0,0,2</sub> |  | 0.5<br><sub>2,2,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.3 |
| Clint Capela | 35% | 10.0<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 4.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.6 | 0.5 | 7.8 |
| Oscar Tshiebwe | 72% | 7.8<br><sub>12,6,11,-,-</sub> | 3.4<br><sub>4,6,4,-,-</sub> |  | 3.5<br><sub>9,6,4,-,-</sub> |  | 0.5<br><sub>3,0,3,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 7.4 |
| Isaiah Crawford | 52% | 6.5<br><sub>9,21,2,-,-</sub> | 2.2<br><sub>4,11,0,-,-</sub> |  | 1.4<br><sub>2,10,0,-,-</sub> |  | 0.3<br><sub>0,3,0,-,-</sub> |  | 0.1<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Jae'Sean Tate | 52% | 5.9<br><sub>8,12,1,-,-</sub> | 1.8<br><sub>4,3,0,-,-</sub> |  | 1.4<br><sub>2,3,0,-,-</sub> |  | 0.4<br><sub>0,2,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.6 |
| Bruce Thornton | 63% | 5.7<br><sub>6,12,1,-,-</sub> | 2.5<br><sub>2,7,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |

</details>


### SAC @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Zach LaVine (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.9–114.2 | SAC 28% | 3.62 / 1.38 | GSW -8.5 | 219.5 | GSW -7.5 covers 52%; o215.5 59% |
| Expected (weighted by chance each plays) | 105.8–116.1 | SAC 23% | 4.31 / 1.30 | GSW -10.5 | 221.5 | GSW -7.5 covers 58%; o215.5 63% |
| if Yaxel Lendeborg plays | 105.5–115.9 | SAC 23% | 4.43 / 1.29 | GSW -10.5 | 221.5 | GSW -7.5 covers 58%; o215.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | Questionable | 55% | 32.5 | 20.6 | 7.2 | 4.2 | 1.8 | 1.0 | 0.8 | 3.0 | 32.0 | full tables below |
| Brandon Williams (GSW) | Questionable | 55% | 17.9 | 12.0 | 2.3 | 3.1 | 0.6 | 0.8 | 0.3 | 1.5 | 17.5 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 37.3<br><sub>33,35,36,40,33</sub> | 24.3<br><sub>26,36,18,21,12</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>0,4,1,6,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.9<br><sub>6,6,12,8,4</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,6,2,2,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 4.0 | 35.7 |
| De'Andre Hunter | 88% | 36.4<br><sub>-,35,37,41,38</sub> | 17.1<br><sub>-,7,30,20,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>-,1,6,6,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>-,4,2,2,8</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.2<br><sub>-,1,5,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.2 | 2.0 | 24.6 |
| Keegan Murray | 98% | 35.4<br><sub>21,31,40,40,39</sub> | 14.1<br><sub>6,12,13,15,14</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>1,7,7,12,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,3,4,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.9 | 1.4 | 21.5 |
| Domantas Sabonis | 99% | 33.1<br><sub>29,24,38,32,30</sub> | 16.0<br><sub>11,8,19,15,20</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 12.5<br><sub>13,13,16,17,12</sub> | 13.5<br><sub>o 45% · u 55%</sub> | 5.7<br><sub>3,8,1,4,8</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.8 | 0.3 | 3.0 | 34.2 |
| Precious Achiuwa | 98% | 20.0<br><sub>-,8,-,22,10</sub> | 8.5<br><sub>-,0,-,5,9</sub> |  | 5.2<br><sub>-,0,-,7,3</sub> |  | 1.1<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.8 | 0.7 | 1.0 | 14.8 |
| Malik Monk | 98% | 19.1<br><sub>29,20,12,10,16</sub> | 10.1<br><sub>14,8,2,3,15</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,0,0,3</sub> |  | 3.7<br><sub>10,2,3,1,4</sub> |  | 1.4<br><sub>1,2,0,0,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.3 | 1.7 | 15.6 |
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
| Brandin Podziemski | 98% | 34.0<br><sub>22,30,29,32,38</sub> | 20.4<br><sub>8,15,10,15,18</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>0,3,4,2,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 2.2 | 30.8 |
| Draymond Green | 97% | 27.8<br><sub>16,25,23,-,27</sub> | 7.0<br><sub>4,2,3,-,9</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 5.4<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.3<br><sub>3,5,2,-,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.8<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.7 | 2.6 | 18.6 |
| De'Anthony Melton | 99% | 27.0<br><sub>18,21,19,25,27</sub> | 14.2<br><sub>8,8,0,9,2</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>4,2,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>3,1,2,5,7</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.6 | 0.4 | 2.0 | 22.3 |
| Will Richard | 99% | 25.5<br><sub>30,23,27,27,17</sub> | 10.2<br><sub>7,11,20,15,3</sub> |  | 3.0<br><sub>4,3,0,5,2</sub> |  | 1.9<br><sub>1,1,3,0,2</sub> |  | 1.2<br><sub>1,2,1,1,1</sub> |  | 1.3 | 0.2 | 1.1 | 15.1 |
| Gui Santos | 96% | 24.4<br><sub>21,19,17,23,23</sub> | 11.7<br><sub>7,12,6,8,13</sub> |  | 4.9<br><sub>4,7,6,3,5</sub> |  | 3.3<br><sub>1,2,6,0,3</sub> |  | 1.1<br><sub>1,1,0,0,3</sub> |  | 0.9 | 0.4 | 1.8 | 19.8 |
| Charles Bassey | 98% | 24.2<br><sub>20,16,22,25,26</sub> | 12.8<br><sub>11,4,10,16,13</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 9.5<br><sub>5,0,8,13,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.5 | 1.4 | 23.8 |
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
| Brandin Podziemski (GSW) | 98% | 33.6<br><sub>22,30,29,32,38</sub> | 18.8<br><sub>8,15,10,15,18</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.6<br><sub>0,3,4,2,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.5<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.3 | 1.9 | 28.6 |
| Yaxel Lendeborg (GSW) | 100% | 32.5<br><sub>24,33,30,33,34</sub> | 20.6<br><sub>3,28,13,11,12</sub> | 21.5 · – | 7.2<br><sub>7,8,5,8,8</sub> | 7.5 | 4.2<br><sub>1,3,4,7,3</sub> | 3.5 | 1.8<br><sub>0,2,0,1,1</sub> | 1.5 | 1.0 | 0.8 | 3.0 | 32.0 |
| Draymond Green (GSW) | 97% | 26.4<br><sub>16,25,23,-,27</sub> | 6.5<br><sub>4,2,3,-,9</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>3,5,2,-,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.8<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.7 | 2.3 | 17.7 |
| De'Anthony Melton (GSW) | 99% | 24.7<br><sub>18,21,19,25,27</sub> | 11.5<br><sub>8,8,0,9,2</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>4,2,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>3,1,2,5,7</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.4 | 1.8 | 18.6 |
| Will Richard (GSW) | 99% | 21.5<br><sub>30,23,27,27,17</sub> | 8.1<br><sub>7,11,20,15,3</sub> |  | 2.5<br><sub>4,3,0,5,2</sub> |  | 1.5<br><sub>1,1,3,0,2</sub> |  | 1.0<br><sub>1,2,1,1,1</sub> |  | 1.1 | 0.2 | 0.9 | 12.1 |
| Charles Bassey (GSW) | 98% | 20.1<br><sub>20,16,22,25,26</sub> | 10.3<br><sub>11,4,10,16,13</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>5,0,8,13,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.3 | 1.2 | 19.2 |
| Gui Santos (GSW) | 96% | 19.9<br><sub>21,19,17,23,23</sub> | 9.2<br><sub>7,12,6,8,13</sub> |  | 4.0<br><sub>4,7,6,3,5</sub> |  | 2.3<br><sub>1,2,6,0,3</sub> |  | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.7 | 0.3 | 1.3 | 15.5 |
| Al Horford (GSW) | 98% | 17.7<br><sub>10,14,-,17,18</sub> | 6.3<br><sub>0,0,-,3,7</sub> |  | 3.8<br><sub>3,5,-,2,3</sub> |  | 1.9<br><sub>1,0,-,2,2</sub> |  | 0.9<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.8 | 0.6 | 12.1 |
| Gary Payton II (GSW) | 91% | 16.1<br><sub>13,8,16,24,13</sub> | 7.6<br><sub>2,2,8,2,8</sub> |  | 2.8<br><sub>2,0,8,1,1</sub> |  | 1.3<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>0,0,2,0,0</sub> |  | 1.0 | 0.2 | 0.7 | 11.7 |
| Georges Niang (GSW) | 98% | 16.0<br><sub>15,14,14,15,8</sub> | 7.3<br><sub>5,0,11,5,0</sub> |  | 2.3<br><sub>3,4,1,2,1</sub> |  | 1.1<br><sub>2,2,1,0,0</sub> |  | 1.1<br><sub>1,0,2,1,0</sub> |  | 0.3 | 0.1 | 0.8 | 10.8 |
| LJ Cryer (GSW) | 88% | 14.3<br><sub>24,24,19,12,11</sub> | 7.1<br><sub>20,7,9,9,3</sub> |  | 1.1<br><sub>2,1,0,0,0</sub> |  | 1.8<br><sub>6,3,2,1,2</sub> |  | 1.2<br><sub>6,1,3,1,1</sub> |  | 0.3 | 0.1 | 0.6 | 10.0 |
| Graham Ike (GSW) | 72% | 8.9<br><sub>13,8,15,4,-</sub> | 4.1<br><sub>5,3,2,5,-</sub> |  | 2.1<br><sub>2,5,2,0,-</sub> |  | 1.0<br><sub>3,1,2,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.4 | 0.5 | 7.2 |
| Malevy Leons (GSW) | 64% | 7.6<br><sub>14,6,7,4,-</sub> | 2.3<br><sub>5,2,2,0,-</sub> |  | 1.4<br><sub>1,1,1,2,-</sub> |  | 0.5<br><sub>0,0,0,1,-</sub> |  | 0.1<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.1 |
| Darius Acuff Jr. (SAC) | 98% | 37.3<br><sub>33,35,36,40,33</sub> | 24.3<br><sub>26,36,18,21,12</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>0,4,1,6,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 7.9<br><sub>6,6,12,8,4</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,6,2,2,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 4.0 | 35.7 |
| De'Andre Hunter (SAC) | 88% | 36.4<br><sub>-,35,37,41,38</sub> | 17.1<br><sub>-,7,30,20,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>-,1,6,6,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>-,4,2,2,8</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.2<br><sub>-,1,5,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.2 | 2.0 | 24.6 |
| Keegan Murray (SAC) | 98% | 35.5<br><sub>21,31,40,40,39</sub> | 14.1<br><sub>6,12,13,15,14</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>1,7,7,12,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,3,4,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.9 | 1.4 | 21.6 |
| Domantas Sabonis (SAC) | 99% | 33.1<br><sub>29,24,38,32,30</sub> | 15.8<br><sub>11,8,19,15,20</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 12.4<br><sub>13,13,16,17,12</sub> | 13.5<br><sub>o 45% · u 55%</sub> | 5.7<br><sub>3,8,1,4,8</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.8 | 0.3 | 3.0 | 33.9 |
| Precious Achiuwa (SAC) | 98% | 20.1<br><sub>-,8,-,22,10</sub> | 8.5<br><sub>-,0,-,5,9</sub> |  | 5.2<br><sub>-,0,-,7,3</sub> |  | 1.1<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.8 | 0.7 | 1.0 | 14.8 |
| Malik Monk (SAC) | 98% | 19.2<br><sub>29,20,12,10,16</sub> | 10.1<br><sub>14,8,2,3,15</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,0,0,3</sub> |  | 3.7<br><sub>10,2,3,1,4</sub> |  | 1.4<br><sub>1,2,0,0,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.3 | 1.7 | 15.6 |
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
| Julian Champagnie | 99% | 31.4<br><sub>24,30,29,25,30</sub> | 13.8<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>5,6,4,3,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>1,0,1,3,3</sub> |  | 2.4<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.6 | 1.2 | 21.2 |
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
| Deni Avdija | 72% | 34.3<br><sub>30,-,-,36,30</sub> | 23.9<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.2 | 36.8 |
| Damian Lillard | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.3<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 2.1 | 28.7 |
| Toumani Camara | 99% | 32.8<br><sub>26,33,37,35,29</sub> | 11.9<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.5 | 1.1 | 18.4 |
| Jrue Holiday | 99% | 29.7<br><sub>25,31,31,31,28</sub> | 14.7<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 2.1 | 23.7 |
| Donovan Clingan | 99% | 28.7<br><sub>22,32,26,31,29</sub> | 12.6<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 11.9<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.6 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson | 99% | 25.3<br><sub>23,21,35,23,26</sub> | 12.0<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.9 | 16.8 |
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
| Deni Avdija (POR) | 72% | 34.3<br><sub>30,-,-,36,30</sub> | 23.8<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.3<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.2 | 36.7 |
| Damian Lillard (POR) | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.2<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 2.2 | 28.6 |
| Toumani Camara (POR) | 99% | 32.8<br><sub>26,33,37,35,29</sub> | 11.8<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.5 | 1.1 | 18.3 |
| Jrue Holiday (POR) | 99% | 29.8<br><sub>25,31,31,31,28</sub> | 14.6<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 2.1 | 23.6 |
| Donovan Clingan (POR) | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.5<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 12.0<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.7 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson (POR) | 99% | 25.4<br><sub>23,21,35,23,26</sub> | 12.0<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.9 | 16.9 |
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
| Julian Champagnie (SAS) | 99% | 30.3<br><sub>24,30,29,25,30</sub> | 12.9<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,6,4,3,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,0,1,3,3</sub> |  | 2.2<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.6 | 0.9 | 19.9 |
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
| Deni Avdija (POR) | 72% | 34.4<br><sub>30,-,-,36,30</sub> | 23.8<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.2 | 36.8 |
| Damian Lillard (POR) | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.1<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 2.1 | 28.6 |
| Toumani Camara (POR) | 99% | 32.7<br><sub>26,33,37,35,29</sub> | 11.8<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.5 | 1.1 | 18.3 |
| Jrue Holiday (POR) | 99% | 29.6<br><sub>25,31,31,31,28</sub> | 14.5<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 2.1 | 23.4 |
| Donovan Clingan (POR) | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.5<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 12.0<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.7 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson (POR) | 99% | 25.3<br><sub>23,21,35,23,26</sub> | 11.9<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.9 | 16.7 |
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
| Julian Champagnie (SAS) | 99% | 29.4<br><sub>24,30,29,25,30</sub> | 11.3<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>5,6,4,3,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,0,1,3,3</sub> |  | 2.0<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.6 | 0.8 | 17.9 |
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
