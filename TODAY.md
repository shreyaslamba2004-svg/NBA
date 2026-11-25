# NBA model · Wed 25 Nov 2026 (US date)

Updated **Thu 26 Nov, 01:32 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-25/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cam Spencer AST over 9.5 (10+) | LAC @ MEM | draftkings | 15.80 | 13.30 | 6.77 | 14.8% | 5.9% | 7.5% | +18.8% | +133.2% | 0.3% |
| Amen Thompson PRA over 39.5 (40+) | PHX @ HOU | draftkings | 15.40 | 13.83 | 8.01 | 12.5% | 6.1% | 7.2% | +11.3% | +92.3% | 0.2% |
| Kevin Durant AST over 7.5 (8+) | PHX @ HOU | draftkings | 14.60 | 13.14 | 7.64 | 13.1% | 6.4% | 7.6% | +11.1% | +91.1% | 0.2% |
| Amen Thompson AST over 7.5 (8+) | PHX @ HOU | draftkings | 24.00 | 21.60 | 12.58 | 8.0% | 3.9% | 4.6% | +11.1% | +90.8% | 0.1% |
| Shai Gilgeous-Alexander PA over 59.5 (60+) | MIN @ OKC | draftkings | 26.00 | 23.42 | 13.64 | 7.3% | 3.6% | 4.3% | +11.1% | +90.7% | 0.1% |
| Egor Demin AST over 5.5 (6+) | BKN @ MIL | draftkings | 10.70 | 9.64 | 5.62 | 17.8% | 8.7% | 10.4% | +11.0% | +90.4% | 0.3% |
| Amen Thompson AST over 5.5 (6+) | PHX @ HOU | draftkings | 7.60 | 6.87 | 4.03 | 24.8% | 12.3% | 14.6% | +10.7% | +88.5% | 0.4% |
| Shai Gilgeous-Alexander PRA over 64.5 (65+) | MIN @ OKC | draftkings | 24.00 | 21.98 | 13.26 | 7.5% | 3.9% | 4.5% | +9.3% | +81.0% | 0.1% |
| Amen Thompson PA over 29.5 (30+) | PHX @ HOU | draftkings | 11.40 | 10.48 | 6.40 | 15.6% | 8.2% | 9.5% | +8.8% | +78.2% | 0.2% |
| Amen Thompson PRA over 34.5 (35+) | PHX @ HOU | draftkings | 6.86 | 6.37 | 3.99 | 25.1% | 13.6% | 15.7% | +7.7% | +71.9% | 0.3% |
| Jalen Brunson PA over 54.5 (55+) | CLE @ NYK | draftkings | 21.00 | 19.53 | 12.25 | 8.2% | 4.5% | 5.1% | +7.6% | +71.5% | 0.1% |
| Kevin Durant PA over 39.5 (40+) | PHX @ HOU | draftkings | 15.00 | 14.03 | 8.91 | 11.2% | 6.2% | 7.1% | +7.0% | +68.3% | 0.1% |
| Amen Thompson PA over 34.5 (35+) | PHX @ HOU | draftkings | 25.00 | 23.53 | 15.19 | 6.6% | 3.7% | 4.2% | +6.3% | +64.6% | 0.1% |
| Cam Spencer PA over 24.5 (25+) | LAC @ MEM | draftkings | 9.60 | 9.04 | 5.85 | 17.1% | 9.7% | 11.1% | +6.2% | +64.0% | 0.2% |
| Draymond Green AST over 9.5 (10+) | SAC @ GSW | draftkings | 12.40 | 11.67 | 7.56 | 13.2% | 7.5% | 8.6% | +6.2% | +64.0% | 0.1% |
| Kevin Durant AST over 5.5 (6+) | PHX @ HOU | draftkings | 4.67 | 4.42 | 2.90 | 34.5% | 20.0% | 22.6% | +5.7% | +61.2% | 0.4% |
| Zach Edey REB over 13.5 (14+) | LAC @ MEM | draftkings | 12.80 | 12.12 | 7.97 | 12.6% | 7.3% | 8.2% | +5.6% | +60.7% | 0.1% |
| Jalen Brunson PTS over 49.5 (50+) | CLE @ NYK | draftkings | 30.00 | 28.41 | 18.75 | 5.3% | 3.1% | 3.5% | +5.5% | +60.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | SAC @ GSW | draftkings | 3.17 | Yaxel Lendeborg | 31.1% | 25.6% | +5.4% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sion James REB over 1.5 (2+) | CHI @ CHA | draftkings | 2.57 | 2.18 | 1.12 | 89.0% | 36.4% | 45.9% | +17.9% | +128.8% | 2.0% |
| Devin Vassell REB over 1.5 (2+) | SAS @ POR | draftkings | 2.32 | 2.02 | 1.09 | 91.4% | 40.3% | 49.5% | +14.9% | +112.1% | 2.0% |
| Julian Champagnie REB over 1.5 (2+) | SAS @ POR | draftkings | 2.00 | 1.81 | 1.07 | 93.4% | 46.7% | 55.2% | +10.4% | +86.8% | 2.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MIA @ PHI | Thu 26 Nov 09:00 | 120.6–121.0 | MIA 49% | 2.04 / 1.96 | PHI +0.5 | 241.5 | PHI -1.5 covers 48%; o237.5 58% |
| CHI @ CHA | Thu 26 Nov 11:00 | 111.6–115.3 | CHI 39% | 2.54 / 1.65 | CHA -3.5 | 226.5 | CHA -3.5 covers 51%; o221.5 61% |
| CLE @ NYK | Thu 26 Nov 11:30 | 110.3–110.2 | CLE 50% | 1.98 / 2.02 | NYK +0.5 | 220.5 | NYK -2.5 covers 43%; o218.5 54% |
| MIN @ OKC | Thu 26 Nov 11:30 | 112.6–115.4 | MIN 42% | 2.36 / 1.74 | OKC -2.5 | 227.5 | OKC -1.5 covers 55%; o222.5 61% |
| LAC @ MEM | Thu 26 Nov 12:00 | 115.7–118.0 | LAC 43% | 2.30 / 1.77 | MEM -2.5 | 233.5 | MEM -6.5 covers 39%; o229.5 59% |
| BKN @ MIL | Thu 26 Nov 12:00 | 108.5–115.5 | BKN 31% | 3.24 / 1.45 | MIL -7.5 | 223.5 | MIL -1.5 covers 66%; o232.5 32% |
| PHX @ HOU | Thu 26 Nov 12:30 | 111.2–117.6 | PHX 32% | 3.11 / 1.47 | HOU -6.5 | 228.5 | HOU -8.5 covers 44%; o223.5 61% |
| SAC @ GSW | Thu 26 Nov 14:00 | 106.7–113.6 | SAC 31% | 3.21 / 1.45 | GSW -6.5 | 220.5 | GSW -6.5 covers 51%; o217.5 56% |
| SAS @ POR | Thu 26 Nov 14:00 | 111.0–113.2 | SAS 43% | 2.30 / 1.77 | POR -2.5 | 223.5 | POR +2.5 covers 62%; o225.5 47% |

### MIA @ PHI
Out: Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 120.6–121.0 | MIA 49% | 2.04 / 1.96 | PHI +0.5 | 241.5 | PHI -1.5 covers 48%; o237.5 58% |
| Expected (weighted by chance each plays) | 120.6–121.1 | MIA 49% | 2.04 / 1.96 | PHI +0.5 | 241.5 | PHI -1.5 covers 48%; o237.5 59% |
| if Joel Embiid plays | 119.2–122.9 | MIA 40% | 2.51 / 1.66 | PHI -3.5 | 242.5 | PHI -1.5 covers 57%; o237.5 59% |
| if Giannis Antetokounmpo plays | 121.3–120.6 | MIA 52% | 1.93 / 2.07 | PHI +1.5 | 241.5 | PHI -1.5 covers 45%; o237.5 59% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Joel Embiid (PHI) | Doubtful | 20% | 30.5 | 22.0 | 8.2 | 4.0 | 0.9 | 0.7 | 1.1 | 2.6 | 34.2 | full tables below |
| Giannis Antetokounmpo (MIA) | Questionable | 55% | 33.8 | 30.8 | 12.6 | 5.5 | 0.5 | 0.9 | 1.2 | 3.1 | 48.9 | full tables below |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 99% | 36.2<br><sub>39,32,33,36,34</sub> | 17.4<br><sub>22,15,16,24,14</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>5,4,3,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 8.5<br><sub>17,9,10,6,3</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,3,1,6,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.4 | 2.5 | 29.3 |
| Bam Adebayo | 99% | 35.0<br><sub>38,36,16,30,37</sub> | 22.7<br><sub>37,20,4,26,24</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>14,5,1,4,15</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>3,4,2,2,12</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>2,1,0,3,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.7 | 1.7 | 37.5 |
| Pelle Larsson | 88% | 29.5<br><sub>-,-,-,15,30</sub> | 13.8<br><sub>-,-,-,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>-,-,-,2,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,-,-,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>-,-,-,1,3</sub> |  | 1.0 | 0.2 | 1.9 | 21.2 |
| Andrew Wiggins | 98% | 29.1<br><sub>32,23,34,26,22</sub> | 13.7<br><sub>8,10,17,11,5</sub> |  | 3.9<br><sub>3,2,5,2,2</sub> |  | 2.1<br><sub>4,1,1,2,1</sub> |  | 1.7<br><sub>1,0,3,1,1</sub> |  | 0.8 | 0.9 | 1.3 | 19.7 |
| Ryan Conwell | 93% | 26.1<br><sub>33,26,30,26,29</sub> | 11.1<br><sub>20,9,14,13,10</sub> |  | 3.0<br><sub>5,4,2,3,1</sub> |  | 1.8<br><sub>2,1,3,1,1</sub> |  | 1.7<br><sub>4,2,1,3,2</sub> |  | 0.8 | 0.2 | 1.1 | 15.9 |
| Klay Thompson | 88% | 25.8<br><sub>-,20,22,23,23</sub> | 13.9<br><sub>-,26,17,13,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,1,0,1,6</sub> |  | 1.9<br><sub>-,4,2,1,4</sub> |  | 2.9<br><sub>-,6,5,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.7 | 1.1 | 18.1 |
| Bobby Portis | 99% | 22.7<br><sub>15,18,23,17,21</sub> | 10.7<br><sub>5,7,16,9,10</sub> |  | 6.1<br><sub>3,4,6,3,8</sub> |  | 1.4<br><sub>2,2,0,0,1</sub> |  | 1.4<br><sub>1,1,2,1,1</sub> |  | 0.6 | 0.3 | 0.8 | 18.2 |
| Nikola Jovic | 66% | 17.1<br><sub>-,11,-,14,19</sub> | 6.6<br><sub>-,2,-,4,15</sub> |  | 3.3<br><sub>-,1,-,1,8</sub> |  | 1.9<br><sub>-,2,-,4,3</sub> |  | 0.8<br><sub>-,0,-,1,3</sub> |  | 0.5 | 0.5 | 0.9 | 11.8 |
| Simone Fontecchio | 80% | 15.8<br><sub>7,14,19,18,15</sub> | 7.7<br><sub>0,7,10,6,11</sub> |  | 2.9<br><sub>0,5,6,5,0</sub> |  | 1.1<br><sub>2,0,2,1,0</sub> |  | 1.1<br><sub>0,1,2,2,1</sub> |  | 0.4 | 0.2 | 0.6 | 11.8 |
| Myron Gardner | 67% | 14.8<br><sub>19,26,24,-,11</sub> | 5.3<br><sub>0,5,14,-,4</sub> |  | 3.9<br><sub>4,9,2,-,1</sub> |  | 1.5<br><sub>2,3,3,-,0</sub> |  | 0.6<br><sub>0,1,4,-,0</sub> |  | 0.5 | 0.4 | 0.6 | 10.7 |
| Tim Hardaway Jr. | 48% | 14.3<br><sub>20,-,-,-,-</sub> | 6.1<br><sub>4,-,-,-,-</sub> |  | 1.7<br><sub>3,-,-,-,-</sub> |  | 0.8<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 8.6 |
| Dru Smith | 38% | 9.6<br><sub>6,-,-,-,-</sub> | 3.3<br><sub>0,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 6.2 |
| Keshad Johnson | 52% | 7.9<br><sub>-,1,3,-,-</sub> | 3.8<br><sub>-,0,0,-,-</sub> |  | 1.9<br><sub>-,0,2,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.1 |
| Nick Richards | 52% | 7.0<br><sub>-,-,3,1,-</sub> | 2.7<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 5.6 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 88% | 35.4<br><sub>36,35,-,36,35</sub> | 25.7<br><sub>27,24,-,17,22</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>4,1,-,4,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>6,9,-,4,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>5,4,-,0,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.5 | 2.2 | 35.2 |
| VJ Edgecombe | 98% | 34.1<br><sub>31,33,43,38,35</sub> | 15.8<br><sub>11,14,24,16,12</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.0<br><sub>4,9,8,3,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>6,4,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.5 | 1.5 | 26.3 |
| Jaylen Brown | 99% | 33.7<br><sub>32,33,-,-,29</sub> | 24.9<br><sub>31,31,-,-,20</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>2,13,-,-,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>2,4,-,-,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>3,3,-,-,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.5 | 3.0 | 35.2 |
| LeBron James | 98% | 32.6<br><sub>33,-,31,35,30</sub> | 19.2<br><sub>15,-,22,21,23</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>7,-,3,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>11,-,6,6,3</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,-,1,0,4</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.5 | 2.7 | 32.6 |
| Dean Wade | 82% | 25.3<br><sub>35,32,-,-,28</sub> | 5.1<br><sub>12,8,-,-,2</sub> |  | 4.8<br><sub>7,11,-,-,2</sub> |  | 1.6<br><sub>3,1,-,-,2</sub> |  | 0.6<br><sub>3,1,-,-,0</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Anfernee Simons | 98% | 21.2<br><sub>15,26,38,26,18</sub> | 11.1<br><sub>12,9,18,18,3</sub> |  | 2.0<br><sub>0,1,2,0,0</sub> |  | 1.6<br><sub>0,2,2,1,0</sub> |  | 1.8<br><sub>1,1,3,4,0</sub> |  | 0.4 | 0.1 | 0.8 | 14.7 |
| Kentavious Caldwell-Pope | 99% | 20.9<br><sub>22,31,32,35,17</sub> | 6.0<br><sub>9,0,8,11,2</sub> |  | 2.5<br><sub>5,2,8,1,3</sub> |  | 1.6<br><sub>0,3,1,2,1</sub> |  | 0.8<br><sub>2,0,2,3,0</sub> |  | 0.7 | 0.3 | 0.6 | 10.1 |
| Jabari Walker | 93% | 15.3<br><sub>25,16,13,20,20</sub> | 6.8<br><sub>11,12,6,9,10</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>7,5,5,7,5</sub> |  | 1.0<br><sub>1,1,2,4,2</sub> |  | 0.6<br><sub>3,1,1,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 12.6 |
| Dominick Barlow | 91% | 14.0<br><sub>-,-,-,11,16</sub> | 4.6<br><sub>-,-,-,12,6</sub> |  | 3.1<br><sub>-,-,-,4,2</sub> |  | 0.8<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.5 | 0.5 | 8.5 |
| Adem Bona | 98% | 10.3<br><sub>-,-,-,-,5</sub> | 3.0<br><sub>-,-,-,-,4</sub> |  | 2.8<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.6 | 0.6 | 6.2 |
| Rayan Rupert | 36% | 7.0<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.6 |
| Labaron Philon Jr. | 80% | 6.9<br><sub>6,-,17,6,3</sub> | 3.2<br><sub>3,-,10,2,2</sub> |  | 0.9<br><sub>1,-,1,0,1</sub> |  | 0.8<br><sub>0,-,2,0,1</sub> |  | 0.3<br><sub>1,-,2,0,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Justin Edwards | 58% | 6.4<br><sub>-,-,13,-,3</sub> | 2.8<br><sub>-,-,2,-,5</sub> |  | 1.0<br><sub>-,-,1,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Tacko Fall | 52% | 6.4<br><sub>5,-,10,-,-</sub> | 5.2<br><sub>0,-,2,-,-</sub> |  | 1.9<br><sub>3,-,3,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.4 | 0.4 | 7.4 |
| Caleb Love | 48% | 5.4<br><sub>-,-,6,-,-</sub> | 2.2<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.5 |

</details>

<details><summary>if Giannis Antetokounmpo plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 35.1<br><sub>39,32,33,36,34</sub> | 14.5<br><sub>22,15,16,24,14</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>5,4,3,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 8.0<br><sub>17,9,10,6,3</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,3,1,6,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.3 | 2.2 | 25.5 |
| Bam Adebayo (MIA) | 99% | 33.9<br><sub>38,36,16,30,37</sub> | 19.3<br><sub>37,20,4,26,24</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 9.7<br><sub>14,5,1,4,15</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>3,4,2,2,12</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,1,0,3,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.8 | 1.6 | 33.0 |
| Giannis Antetokounmpo (MIA) | 100% | 33.8<br><sub>31,31,29,32,-</sub> | 30.8<br><sub>37,34,20,27,-</sub> | 29.5 · – | 12.6<br><sub>9,14,13,14,-</sub> | 12.5 | 5.5<br><sub>2,8,6,9,-</sub> | 5.5 | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.9 | 1.2 | 3.1 | 48.9 |
| Pelle Larsson (MIA) | 88% | 26.7<br><sub>-,-,-,15,30</sub> | 10.8<br><sub>-,-,-,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>-,-,-,2,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>-,-,-,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>-,-,-,1,3</sub> |  | 0.8 | 0.2 | 1.7 | 17.3 |
| Andrew Wiggins (MIA) | 98% | 24.9<br><sub>32,23,34,26,22</sub> | 10.1<br><sub>8,10,17,11,5</sub> |  | 3.2<br><sub>3,2,5,2,2</sub> |  | 1.7<br><sub>4,1,1,2,1</sub> |  | 1.3<br><sub>1,0,3,1,1</sub> |  | 0.6 | 0.8 | 1.1 | 15.0 |
| Klay Thompson (MIA) | 88% | 22.2<br><sub>-,20,22,23,23</sub> | 11.3<br><sub>-,26,17,13,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>-,1,0,1,6</sub> |  | 1.6<br><sub>-,4,2,1,4</sub> |  | 2.3<br><sub>-,6,5,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.5 | 0.8 | 14.8 |
| Ryan Conwell (MIA) | 93% | 21.2<br><sub>33,26,30,26,29</sub> | 7.9<br><sub>20,9,14,13,10</sub> |  | 2.4<br><sub>5,4,2,3,1</sub> |  | 1.4<br><sub>2,1,3,1,1</sub> |  | 1.2<br><sub>4,2,1,3,2</sub> |  | 0.7 | 0.2 | 0.9 | 11.7 |
| Bobby Portis (MIA) | 99% | 18.2<br><sub>15,18,23,17,21</sub> | 7.8<br><sub>5,7,16,9,10</sub> |  | 4.8<br><sub>3,4,6,3,8</sub> |  | 1.1<br><sub>2,2,0,0,1</sub> |  | 1.0<br><sub>1,1,2,1,1</sub> |  | 0.4 | 0.3 | 0.7 | 13.7 |
| Nikola Jovic (MIA) | 66% | 12.1<br><sub>-,11,-,14,19</sub> | 4.3<br><sub>-,2,-,4,15</sub> |  | 2.3<br><sub>-,1,-,1,8</sub> |  | 1.3<br><sub>-,2,-,4,3</sub> |  | 0.4<br><sub>-,0,-,1,3</sub> |  | 0.3 | 0.3 | 0.6 | 7.9 |
| Simone Fontecchio (MIA) | 80% | 11.4<br><sub>7,14,19,18,15</sub> | 5.3<br><sub>0,7,10,6,11</sub> |  | 2.1<br><sub>0,5,6,5,0</sub> |  | 0.8<br><sub>2,0,2,1,0</sub> |  | 0.7<br><sub>0,1,2,2,1</sub> |  | 0.3 | 0.1 | 0.5 | 8.1 |
| Tim Hardaway Jr. (MIA) | 48% | 9.8<br><sub>20,-,-,-,-</sub> | 3.8<br><sub>4,-,-,-,-</sub> |  | 1.2<br><sub>3,-,-,-,-</sub> |  | 0.5<br><sub>2,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Myron Gardner (MIA) | 67% | 9.3<br><sub>19,26,24,-,11</sub> | 3.1<br><sub>0,5,14,-,4</sub> |  | 2.3<br><sub>4,9,2,-,1</sub> |  | 0.9<br><sub>2,3,3,-,0</sub> |  | 0.3<br><sub>0,1,4,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Dru Smith (MIA) | 38% | 6.9<br><sub>6,-,-,-,-</sub> | 2.2<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.3 |
| Keshad Johnson (MIA) | 52% | 6.1<br><sub>-,1,3,-,-</sub> | 3.0<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,0,2,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |
| Nick Richards (MIA) | 52% | 5.4<br><sub>-,-,3,1,-</sub> | 2.1<br><sub>-,-,0,0,-</sub> |  | 2.0<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.4 |
| Tyrese Maxey (PHI) | 88% | 35.6<br><sub>36,35,-,36,35</sub> | 25.8<br><sub>27,24,-,17,22</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>4,1,-,4,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>6,9,-,4,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>5,4,-,0,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.5 | 2.2 | 35.4 |
| VJ Edgecombe (PHI) | 98% | 34.1<br><sub>31,33,43,38,35</sub> | 15.8<br><sub>11,14,24,16,12</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.0<br><sub>4,9,8,3,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>6,4,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.5 | 1.5 | 26.3 |
| Jaylen Brown (PHI) | 99% | 33.7<br><sub>32,33,-,-,29</sub> | 24.9<br><sub>31,31,-,-,20</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>2,13,-,-,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>2,4,-,-,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>3,3,-,-,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.5 | 3.0 | 35.3 |
| LeBron James (PHI) | 98% | 32.6<br><sub>33,-,31,35,30</sub> | 19.2<br><sub>15,-,22,21,23</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>7,-,3,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>11,-,6,6,3</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,-,1,0,4</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.5 | 2.7 | 32.6 |
| Dean Wade (PHI) | 82% | 25.2<br><sub>35,32,-,-,28</sub> | 5.1<br><sub>12,8,-,-,2</sub> |  | 4.8<br><sub>7,11,-,-,2</sub> |  | 1.5<br><sub>3,1,-,-,2</sub> |  | 0.6<br><sub>3,1,-,-,0</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Anfernee Simons (PHI) | 98% | 21.2<br><sub>15,26,38,26,18</sub> | 11.1<br><sub>12,9,18,18,3</sub> |  | 2.1<br><sub>0,1,2,0,0</sub> |  | 1.6<br><sub>0,2,2,1,0</sub> |  | 1.8<br><sub>1,1,3,4,0</sub> |  | 0.4 | 0.1 | 0.8 | 14.7 |
| Kentavious Caldwell-Pope (PHI) | 99% | 20.9<br><sub>22,31,32,35,17</sub> | 6.0<br><sub>9,0,8,11,2</sub> |  | 2.5<br><sub>5,2,8,1,3</sub> |  | 1.6<br><sub>0,3,1,2,1</sub> |  | 0.8<br><sub>2,0,2,3,0</sub> |  | 0.7 | 0.3 | 0.6 | 10.1 |
| Jabari Walker (PHI) | 93% | 15.2<br><sub>25,16,13,20,20</sub> | 6.8<br><sub>11,12,6,9,10</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>7,5,5,7,5</sub> |  | 1.0<br><sub>1,1,2,4,2</sub> |  | 0.6<br><sub>3,1,1,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 12.5 |
| Dominick Barlow (PHI) | 91% | 14.0<br><sub>-,-,-,11,16</sub> | 4.6<br><sub>-,-,-,12,6</sub> |  | 3.1<br><sub>-,-,-,4,2</sub> |  | 0.8<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.5 | 0.5 | 8.5 |
| Adem Bona (PHI) | 98% | 10.3<br><sub>-,-,-,-,5</sub> | 3.0<br><sub>-,-,-,-,4</sub> |  | 2.8<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.6 | 0.6 | 6.2 |
| Rayan Rupert (PHI) | 36% | 7.0<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.6 |
| Labaron Philon Jr. (PHI) | 80% | 6.9<br><sub>6,-,17,6,3</sub> | 3.2<br><sub>3,-,10,2,2</sub> |  | 0.9<br><sub>1,-,1,0,1</sub> |  | 0.8<br><sub>0,-,2,0,1</sub> |  | 0.3<br><sub>1,-,2,0,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Justin Edwards (PHI) | 58% | 6.4<br><sub>-,-,13,-,3</sub> | 2.8<br><sub>-,-,2,-,5</sub> |  | 1.0<br><sub>-,-,1,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Tacko Fall (PHI) | 52% | 6.3<br><sub>5,-,10,-,-</sub> | 5.1<br><sub>0,-,2,-,-</sub> |  | 1.8<br><sub>3,-,3,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.4 | 0.4 | 7.2 |
| Caleb Love (PHI) | 48% | 5.4<br><sub>-,-,6,-,-</sub> | 2.3<br><sub>-,-,3,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.6 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 36.3<br><sub>39,32,33,36,34</sub> | 17.4<br><sub>22,15,16,24,14</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>5,4,3,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 8.5<br><sub>17,9,10,6,3</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,3,1,6,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.1 | 0.4 | 2.5 | 29.2 |
| Bam Adebayo (MIA) | 99% | 35.0<br><sub>38,36,16,30,37</sub> | 22.6<br><sub>37,20,4,26,24</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 10.1<br><sub>14,5,1,4,15</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>3,4,2,2,12</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>2,1,0,3,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.7 | 1.7 | 37.3 |
| Pelle Larsson (MIA) | 88% | 29.5<br><sub>-,-,-,15,30</sub> | 13.7<br><sub>-,-,-,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>-,-,-,2,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,-,-,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>-,-,-,1,3</sub> |  | 1.0 | 0.2 | 1.9 | 21.2 |
| Andrew Wiggins (MIA) | 98% | 29.0<br><sub>32,23,34,26,22</sub> | 13.4<br><sub>8,10,17,11,5</sub> |  | 3.9<br><sub>3,2,5,2,2</sub> |  | 2.1<br><sub>4,1,1,2,1</sub> |  | 1.7<br><sub>1,0,3,1,1</sub> |  | 0.8 | 0.9 | 1.3 | 19.4 |
| Ryan Conwell (MIA) | 93% | 26.0<br><sub>33,26,30,26,29</sub> | 11.1<br><sub>20,9,14,13,10</sub> |  | 3.0<br><sub>5,4,2,3,1</sub> |  | 1.8<br><sub>2,1,3,1,1</sub> |  | 1.7<br><sub>4,2,1,3,2</sub> |  | 0.8 | 0.2 | 1.1 | 15.9 |
| Klay Thompson (MIA) | 88% | 25.8<br><sub>-,20,22,23,23</sub> | 13.8<br><sub>-,26,17,13,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,1,0,1,6</sub> |  | 1.9<br><sub>-,4,2,1,4</sub> |  | 2.9<br><sub>-,6,5,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.7 | 1.1 | 18.0 |
| Bobby Portis (MIA) | 99% | 22.7<br><sub>15,18,23,17,21</sub> | 10.6<br><sub>5,7,16,9,10</sub> |  | 6.1<br><sub>3,4,6,3,8</sub> |  | 1.4<br><sub>2,2,0,0,1</sub> |  | 1.4<br><sub>1,1,2,1,1</sub> |  | 0.6 | 0.3 | 0.9 | 18.2 |
| Nikola Jovic (MIA) | 66% | 17.2<br><sub>-,11,-,14,19</sub> | 6.6<br><sub>-,2,-,4,15</sub> |  | 3.3<br><sub>-,1,-,1,8</sub> |  | 1.9<br><sub>-,2,-,4,3</sub> |  | 0.8<br><sub>-,0,-,1,3</sub> |  | 0.5 | 0.5 | 0.8 | 11.8 |
| Simone Fontecchio (MIA) | 80% | 16.0<br><sub>7,14,19,18,15</sub> | 7.7<br><sub>0,7,10,6,11</sub> |  | 2.9<br><sub>0,5,6,5,0</sub> |  | 1.1<br><sub>2,0,2,1,0</sub> |  | 1.1<br><sub>0,1,2,2,1</sub> |  | 0.4 | 0.2 | 0.6 | 11.8 |
| Myron Gardner (MIA) | 67% | 14.8<br><sub>19,26,24,-,11</sub> | 5.2<br><sub>0,5,14,-,4</sub> |  | 3.9<br><sub>4,9,2,-,1</sub> |  | 1.5<br><sub>2,3,3,-,0</sub> |  | 0.6<br><sub>0,1,4,-,0</sub> |  | 0.5 | 0.4 | 0.6 | 10.7 |
| Tim Hardaway Jr. (MIA) | 48% | 14.4<br><sub>20,-,-,-,-</sub> | 6.1<br><sub>4,-,-,-,-</sub> |  | 1.8<br><sub>3,-,-,-,-</sub> |  | 0.8<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 8.6 |
| Dru Smith (MIA) | 38% | 9.7<br><sub>6,-,-,-,-</sub> | 3.3<br><sub>0,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 6.2 |
| Keshad Johnson (MIA) | 52% | 8.0<br><sub>-,1,3,-,-</sub> | 3.7<br><sub>-,0,0,-,-</sub> |  | 1.9<br><sub>-,0,2,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.1 |
| Nick Richards (MIA) | 52% | 7.0<br><sub>-,-,3,1,-</sub> | 2.7<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.4 | 5.5 |
| Tyrese Maxey (PHI) | 88% | 33.5<br><sub>36,35,-,36,35</sub> | 22.1<br><sub>27,24,-,17,22</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>4,1,-,4,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>6,9,-,4,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>5,4,-,0,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.5 | 2.0 | 31.2 |
| VJ Edgecombe (PHI) | 98% | 32.1<br><sub>31,33,43,38,35</sub> | 13.7<br><sub>11,14,24,16,12</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>4,9,8,3,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>6,4,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.4 | 1.4 | 23.5 |
| Jaylen Brown (PHI) | 99% | 31.5<br><sub>32,33,-,-,29</sub> | 21.3<br><sub>31,31,-,-,20</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>2,13,-,-,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>2,4,-,-,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>3,3,-,-,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.4 | 2.7 | 31.0 |
| Joel Embiid (PHI) | 100% | 30.5<br><sub>-,32,36,34,-</sub> | 22.0<br><sub>-,37,26,26,-</sub> |  | 8.2<br><sub>-,5,6,17,-</sub> |  | 4.0<br><sub>-,1,7,9,-</sub> |  | 0.9<br><sub>-,2,0,0,-</sub> |  | 0.7 | 1.1 | 2.6 | 34.2 |
| LeBron James (PHI) | 98% | 30.4<br><sub>33,-,31,35,30</sub> | 16.5<br><sub>15,-,22,21,23</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>7,-,3,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>11,-,6,6,3</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>0,-,1,0,4</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.5 | 2.3 | 29.1 |
| Dean Wade (PHI) | 82% | 22.2<br><sub>35,32,-,-,28</sub> | 4.4<br><sub>12,8,-,-,2</sub> |  | 4.2<br><sub>7,11,-,-,2</sub> |  | 1.3<br><sub>3,1,-,-,2</sub> |  | 0.5<br><sub>3,1,-,-,0</sub> |  | 0.7 | 0.3 | 0.5 | 9.9 |
| Kentavious Caldwell-Pope (PHI) | 99% | 18.5<br><sub>22,31,32,35,17</sub> | 5.2<br><sub>9,0,8,11,2</sub> |  | 2.2<br><sub>5,2,8,1,3</sub> |  | 1.4<br><sub>0,3,1,2,1</sub> |  | 0.7<br><sub>2,0,2,3,0</sub> |  | 0.7 | 0.2 | 0.5 | 8.8 |
| Anfernee Simons (PHI) | 98% | 18.5<br><sub>15,26,38,26,18</sub> | 9.0<br><sub>12,9,18,18,3</sub> |  | 1.7<br><sub>0,1,2,0,0</sub> |  | 1.4<br><sub>0,2,2,1,0</sub> |  | 1.4<br><sub>1,1,3,4,0</sub> |  | 0.4 | 0.1 | 0.7 | 12.2 |
| Jabari Walker (PHI) | 93% | 13.0<br><sub>25,16,13,20,20</sub> | 6.0<br><sub>11,12,6,9,10</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>7,5,5,7,5</sub> |  | 0.9<br><sub>1,1,2,4,2</sub> |  | 0.5<br><sub>3,1,1,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 11.0 |
| Dominick Barlow (PHI) | 91% | 12.3<br><sub>-,-,-,11,16</sub> | 4.1<br><sub>-,-,-,12,6</sub> |  | 2.8<br><sub>-,-,-,4,2</sub> |  | 0.7<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.4 | 0.5 | 7.6 |
| Adem Bona (PHI) | 98% | 7.5<br><sub>-,-,-,-,5</sub> | 2.3<br><sub>-,-,-,-,4</sub> |  | 2.0<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.4 | 0.4 | 4.6 |
| Rayan Rupert (PHI) | 36% | 6.7<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.3 |
| Labaron Philon Jr. (PHI) | 80% | 6.3<br><sub>6,-,17,6,3</sub> | 3.0<br><sub>3,-,10,2,2</sub> |  | 0.8<br><sub>1,-,1,0,1</sub> |  | 0.8<br><sub>0,-,2,0,1</sub> |  | 0.2<br><sub>1,-,2,0,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Justin Edwards (PHI) | 58% | 5.8<br><sub>-,-,13,-,3</sub> | 2.6<br><sub>-,-,2,-,5</sub> |  | 0.8<br><sub>-,-,1,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |
| Tacko Fall (PHI) | 52% | 5.7<br><sub>5,-,10,-,-</sub> | 4.4<br><sub>0,-,2,-,-</sub> |  | 1.8<br><sub>3,-,3,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.5 | 0.4 | 6.5 |
| Caleb Love (PHI) | 48% | 5.2<br><sub>-,-,6,-,-</sub> | 2.2<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.6 |

</details>


### CHI @ CHA
Out: Kon Knueppel (CHA), Dennis Schroder (CHA), Tobe Awaka (CHI), Norman Powell (CHI), Orlando Robinson (CHI), Jaylin Sellers (CHI), Caleb Wilson (CHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.6–115.3 | CHI 39% | 2.54 / 1.65 | CHA -3.5 | 226.5 | CHA -3.5 covers 51%; o221.5 61% |
| Expected (weighted by chance each plays) | 112.0–116.5 | CHI 37% | 2.72 / 1.58 | CHA -4.5 | 228.5 | CHA -3.5 covers 54%; o221.5 64% |
| if Grayson Allen plays | 111.0–117.8 | CHI 32% | 3.16 / 1.46 | CHA -6.5 | 228.5 | CHA -3.5 covers 60%; o221.5 65% |
| if Jalen Smith plays | 112.2–114.7 | CHI 43% | 2.35 / 1.74 | CHA -2.5 | 226.5 | CHA -3.5 covers 48%; o221.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Grayson Allen (CHA) | Questionable | 55% | 24.6 | 13.5 | 3.1 | 3.3 | 2.3 | 1.1 | 0.3 | 1.6 | 19.9 | full tables below |
| Ryan Kalkbrenner (CHA) | Doubtful | 20% | 15.4 | 4.8 | 4.5 | 0.8 | 0.0 | 0.4 | 1.2 | 0.8 | 10.1 | small |
| Jalen Smith (CHI) | Questionable | 55% | 28.4 | 14.2 | 7.4 | 1.9 | 2.0 | 0.7 | 0.9 | 1.2 | 23.5 | full tables below |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaac Okoro | 99% | 31.9<br><sub>32,25,29,42,27</sub> | 10.7<br><sub>13,12,9,11,12</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>6,3,7,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>2,4,1,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4<br><sub>3,4,1,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 1.1 | 16.0 |
| Matas Buzelis | 99% | 31.7<br><sub>31,30,25,38,27</sub> | 18.2<br><sub>23,25,9,21,15</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>3,5,5,5,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,4,1,3,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>3,5,1,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 1.0 | 2.4 | 25.6 |
| Josh Giddey | 99% | 31.2<br><sub>24,28,23,41,22</sub> | 15.7<br><sub>4,18,2,23,4</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>4,14,6,14,2</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 9.0<br><sub>8,9,7,22,11</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>1,1,0,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 3.2 | 31.6 |
| Buddy Hield | 88% | 28.7<br><sub>19,19,23,40,27</sub> | 15.4<br><sub>6,11,15,33,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,4,7,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>2,2,0,6,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.9<br><sub>2,3,4,7,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.3 | 1.3 | 21.6 |
| Tre Jones | 99% | 25.8<br><sub>23,16,25,12,27</sub> | 14.8<br><sub>16,10,12,9,16</sub> |  | 3.0<br><sub>2,2,1,2,4</sub> |  | 5.2<br><sub>6,6,7,4,9</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 23.0 |
| Nic Claxton | 98% | 24.8<br><sub>17,22,29,-,23</sub> | 9.8<br><sub>8,14,11,-,6</sub> |  | 5.7<br><sub>2,4,7,-,6</sub> |  | 2.2<br><sub>1,1,1,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.9 | 1.2 | 17.7 |
| Patrick Williams | 91% | 24.6<br><sub>13,13,23,16,19</sub> | 8.7<br><sub>0,2,6,2,7</sub> |  | 3.2<br><sub>0,1,3,2,5</sub> |  | 1.8<br><sub>0,2,1,0,2</sub> |  | 1.2<br><sub>0,0,0,0,1</sub> |  | 0.9 | 0.4 | 1.1 | 13.7 |
| Jordan Hawkins | 66% | 17.8<br><sub>4,-,-,14,18</sub> | 8.6<br><sub>0,-,-,6,19</sub> |  | 2.1<br><sub>0,-,-,1,1</sub> |  | 1.1<br><sub>1,-,-,1,2</sub> |  | 1.2<br><sub>0,-,-,2,4</sub> |  | 0.5 | 0.2 | 0.7 | 11.9 |
| Zach Collins | 63% | 17.7<br><sub>-,11,15,17,-</sub> | 7.0<br><sub>-,3,6,5,-</sub> |  | 4.3<br><sub>-,2,2,1,-</sub> |  | 1.6<br><sub>-,0,4,0,-</sub> |  | 0.5<br><sub>-,1,0,1,-</sub> |  | 0.5 | 0.4 | 0.9 | 13.0 |
| Leonard Miller | 52% | 16.5<br><sub>1,7,-,-,-</sub> | 7.1<br><sub>0,4,-,-,-</sub> |  | 3.6<br><sub>0,2,-,-,-</sub> |  | 0.9<br><sub>0,0,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.5 | 0.4 | 0.8 | 11.6 |
| Noa Essengue | 98% | 15.9<br><sub>14,15,15,11,4</sub> | 6.5<br><sub>1,5,8,9,6</sub> |  | 3.2<br><sub>2,3,4,4,2</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.6<br><sub>0,0,2,1,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.3 |
| Dailyn Swain | 52% | 10.2<br><sub>2,6,-,-,-</sub> | 3.8<br><sub>0,2,-,-,-</sub> |  | 1.5<br><sub>1,1,-,-,-</sub> |  | 0.9<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.1 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 99% | 33.7<br><sub>34,27,42,39,38</sub> | 20.4<br><sub>16,17,23,12,24</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 9.0<br><sub>8,4,11,10,6</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.9<br><sub>3,3,4,3,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>1,3,4,2,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 1.1 | 2.5 | 32.3 |
| Brandon Miller | 98% | 31.5<br><sub>-,24,32,33,35</sub> | 22.3<br><sub>-,5,28,19,20</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>-,2,2,8,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>-,4,4,3,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>-,1,5,5,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.7 | 2.4 | 30.7 |
| Moussa Diabate | 98% | 30.7<br><sub>32,26,38,30,35</sub> | 10.2<br><sub>7,12,5,21,10</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 11.2<br><sub>13,12,16,15,10</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.2 | 1.6 | 24.0 |
| Sion James | 92% | 30.0<br><sub>32,35,30,32,28</sub> | 7.9<br><sub>3,3,3,9,5</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>8,8,6,1,4</sub> |  | 3.3<br><sub>6,4,4,2,4</sub> |  | 1.2<br><sub>0,1,0,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.2 | 1.2 | 15.7 |
| Coby White | 98% | 25.6<br><sub>20,20,26,26,28</sub> | 18.9<br><sub>21,21,19,11,21</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,0,3,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.6<br><sub>3,1,4,9,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>2,2,2,0,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 2.6 | 26.9 |
| Grant Williams | 86% | 22.3<br><sub>16,20,30,-,-</sub> | 9.4<br><sub>11,11,12,-,-</sub> |  | 4.1<br><sub>2,2,4,-,-</sub> |  | 1.7<br><sub>1,1,0,-,-</sub> |  | 1.4<br><sub>2,3,2,-,-</sub> |  | 0.8 | 0.6 | 1.0 | 15.2 |
| Christian Anderson | 91% | 21.0<br><sub>18,18,14,21,25</sub> | 9.7<br><sub>13,16,5,4,25</sub> |  | 2.4<br><sub>0,3,1,1,2</sub> |  | 2.9<br><sub>2,2,4,2,3</sub> |  | 1.5<br><sub>3,4,1,0,6</sub> |  | 0.7 | 0.3 | 1.4 | 15.0 |
| Royce O'Neale | 99% | 20.9<br><sub>22,19,34,21,13</sub> | 6.4<br><sub>7,3,13,9,0</sub> |  | 3.6<br><sub>4,3,4,1,1</sub> |  | 1.3<br><sub>0,1,1,0,1</sub> |  | 1.1<br><sub>2,1,4,3,0</sub> |  | 0.7 | 0.3 | 0.7 | 11.3 |
| Tidjane Salaun | 98% | 14.4<br><sub>16,5,5,13,17</sub> | 5.2<br><sub>2,0,0,4,0</sub> |  | 3.5<br><sub>4,2,1,2,5</sub> |  | 0.7<br><sub>0,0,0,1,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 9.5 |
| Liam McNeeley | 66% | 12.7<br><sub>-,2,-,7,9</sub> | 5.2<br><sub>-,0,-,2,3</sub> |  | 2.3<br><sub>-,0,-,1,2</sub> |  | 0.9<br><sub>-,0,-,0,0</sub> |  | 0.6<br><sub>-,0,-,0,1</sub> |  | 0.4 | 0.1 | 0.6 | 8.4 |
| Hannes Steinbach | 58% | 9.8<br><sub>-,-,-,-,4</sub> | 3.1<br><sub>-,-,-,-,3</sub> |  | 2.8<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.5 | 0.5 | 6.5 |
| PJ Hall | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.6 | 7.0 |

</details>

<details><summary>if Grayson Allen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid (CHA) | 99% | 31.0<br><sub>34,27,42,39,38</sub> | 18.5<br><sub>16,17,23,12,24</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>8,4,11,10,6</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>3,3,4,3,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>1,3,4,2,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.9 | 2.2 | 29.4 |
| Brandon Miller (CHA) | 98% | 29.4<br><sub>-,24,32,33,35</sub> | 20.7<br><sub>-,5,28,19,20</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>-,2,2,8,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>-,4,4,3,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>-,1,5,5,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.7 | 2.2 | 28.5 |
| Moussa Diabate (CHA) | 98% | 28.9<br><sub>32,26,38,30,35</sub> | 9.8<br><sub>7,12,5,21,10</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 10.6<br><sub>13,12,16,15,10</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.4 | 22.9 |
| Sion James (CHA) | 92% | 26.5<br><sub>32,35,30,32,28</sub> | 6.8<br><sub>3,3,3,9,5</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>8,8,6,1,4</sub> |  | 3.1<br><sub>6,4,4,2,4</sub> |  | 1.0<br><sub>0,1,0,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.2 | 1.0 | 13.8 |
| Grayson Allen (CHA) | 100% | 24.6<br><sub>34,25,-,-,-</sub> | 13.5<br><sub>14,12,-,-,-</sub> | 12.5 · – | 3.1<br><sub>4,5,-,-,-</sub> | 2.5 | 3.3<br><sub>6,4,-,-,-</sub> |  | 2.3<br><sub>4,2,-,-,-</sub> | 2.5 | 1.1 | 0.3 | 1.6 | 19.9 |
| Coby White (CHA) | 98% | 23.6<br><sub>20,20,26,26,28</sub> | 17.1<br><sub>21,21,19,11,21</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>3,0,3,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.2<br><sub>3,1,4,9,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>2,2,2,0,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 2.2 | 24.4 |
| Grant Williams (CHA) | 86% | 19.6<br><sub>16,20,30,-,-</sub> | 8.2<br><sub>11,11,12,-,-</sub> |  | 3.5<br><sub>2,2,4,-,-</sub> |  | 1.5<br><sub>1,1,0,-,-</sub> |  | 1.2<br><sub>2,3,2,-,-</sub> |  | 0.7 | 0.5 | 0.9 | 13.2 |
| Royce O'Neale (CHA) | 99% | 18.3<br><sub>22,19,34,21,13</sub> | 5.4<br><sub>7,3,13,9,0</sub> |  | 3.0<br><sub>4,3,4,1,1</sub> |  | 1.1<br><sub>0,1,1,0,1</sub> |  | 0.9<br><sub>2,1,4,3,0</sub> |  | 0.6 | 0.3 | 0.6 | 9.6 |
| Christian Anderson (CHA) | 91% | 18.2<br><sub>18,18,14,21,25</sub> | 8.9<br><sub>13,16,5,4,25</sub> |  | 2.1<br><sub>0,3,1,1,2</sub> |  | 2.6<br><sub>2,2,4,2,3</sub> |  | 1.3<br><sub>3,4,1,0,6</sub> |  | 0.7 | 0.3 | 1.3 | 13.6 |
| Tidjane Salaun (CHA) | 98% | 12.8<br><sub>16,5,5,13,17</sub> | 4.9<br><sub>2,0,0,4,0</sub> |  | 3.2<br><sub>4,2,1,2,5</sub> |  | 0.6<br><sub>0,0,0,1,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 8.7 |
| Liam McNeeley (CHA) | 66% | 9.2<br><sub>-,2,-,7,9</sub> | 4.1<br><sub>-,0,-,2,3</sub> |  | 1.8<br><sub>-,0,-,1,2</sub> |  | 0.7<br><sub>-,0,-,0,0</sub> |  | 0.4<br><sub>-,0,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 6.7 |
| Hannes Steinbach (CHA) | 58% | 8.2<br><sub>-,-,-,-,4</sub> | 2.8<br><sub>-,-,-,-,3</sub> |  | 2.5<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.5 | 0.5 | 5.7 |
| PJ Hall (CHA) | 35% | 7.2<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.4 | 0.5 | 6.0 |
| Isaac Okoro (CHI) | 99% | 31.9<br><sub>32,25,29,42,27</sub> | 10.6<br><sub>13,12,9,11,12</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>6,3,7,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>2,4,1,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4<br><sub>3,4,1,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 1.1 | 15.9 |
| Matas Buzelis (CHI) | 99% | 31.6<br><sub>31,30,25,38,27</sub> | 18.1<br><sub>23,25,9,21,15</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>3,5,5,5,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,4,1,3,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>3,5,1,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 1.0 | 2.4 | 25.5 |
| Josh Giddey (CHI) | 99% | 31.2<br><sub>24,28,23,41,22</sub> | 15.5<br><sub>4,18,2,23,4</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>4,14,6,14,2</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>8,9,7,22,11</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>1,1,0,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 3.2 | 31.5 |
| Buddy Hield (CHI) | 88% | 28.6<br><sub>19,19,23,40,27</sub> | 15.2<br><sub>6,11,15,33,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,4,7,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>2,2,0,6,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.9<br><sub>2,3,4,7,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.3 | 1.3 | 21.4 |
| Tre Jones (CHI) | 99% | 25.9<br><sub>23,16,25,12,27</sub> | 14.9<br><sub>16,10,12,9,16</sub> |  | 3.0<br><sub>2,2,1,2,4</sub> |  | 5.2<br><sub>6,6,7,4,9</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 23.1 |
| Nic Claxton (CHI) | 98% | 24.7<br><sub>17,22,29,-,23</sub> | 9.9<br><sub>8,14,11,-,6</sub> |  | 5.7<br><sub>2,4,7,-,6</sub> |  | 2.2<br><sub>1,1,1,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.9 | 1.2 | 17.7 |
| Patrick Williams (CHI) | 91% | 24.5<br><sub>13,13,23,16,19</sub> | 8.6<br><sub>0,2,6,2,7</sub> |  | 3.2<br><sub>0,1,3,2,5</sub> |  | 1.8<br><sub>0,2,1,0,2</sub> |  | 1.2<br><sub>0,0,0,0,1</sub> |  | 0.9 | 0.4 | 1.1 | 13.6 |
| Zach Collins (CHI) | 63% | 17.8<br><sub>-,11,15,17,-</sub> | 7.1<br><sub>-,3,6,5,-</sub> |  | 4.3<br><sub>-,2,2,1,-</sub> |  | 1.6<br><sub>-,0,4,0,-</sub> |  | 0.5<br><sub>-,1,0,1,-</sub> |  | 0.5 | 0.4 | 0.9 | 13.0 |
| Jordan Hawkins (CHI) | 66% | 17.8<br><sub>4,-,-,14,18</sub> | 8.6<br><sub>0,-,-,6,19</sub> |  | 2.1<br><sub>0,-,-,1,1</sub> |  | 1.1<br><sub>1,-,-,1,2</sub> |  | 1.2<br><sub>0,-,-,2,4</sub> |  | 0.5 | 0.2 | 0.7 | 11.9 |
| Leonard Miller (CHI) | 52% | 16.5<br><sub>1,7,-,-,-</sub> | 7.0<br><sub>0,4,-,-,-</sub> |  | 3.6<br><sub>0,2,-,-,-</sub> |  | 0.9<br><sub>0,0,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 0.5 | 0.4 | 0.8 | 11.6 |
| Noa Essengue (CHI) | 98% | 15.8<br><sub>14,15,15,11,4</sub> | 6.4<br><sub>1,5,8,9,6</sub> |  | 3.2<br><sub>2,3,4,4,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.6<br><sub>0,0,2,1,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.3 |
| Dailyn Swain (CHI) | 52% | 10.2<br><sub>2,6,-,-,-</sub> | 3.7<br><sub>0,2,-,-,-</sub> |  | 1.5<br><sub>1,1,-,-,-</sub> |  | 0.9<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.1 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid (CHA) | 99% | 33.7<br><sub>34,27,42,39,38</sub> | 20.4<br><sub>16,17,23,12,24</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 9.0<br><sub>8,4,11,10,6</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.9<br><sub>3,3,4,3,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>1,3,4,2,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 1.1 | 2.5 | 32.3 |
| Brandon Miller (CHA) | 98% | 31.4<br><sub>-,24,32,33,35</sub> | 22.3<br><sub>-,5,28,19,20</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>-,2,2,8,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>-,4,4,3,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>-,1,5,5,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.7 | 2.4 | 30.7 |
| Moussa Diabate (CHA) | 98% | 30.9<br><sub>32,26,38,30,35</sub> | 10.2<br><sub>7,12,5,21,10</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 11.3<br><sub>13,12,16,15,10</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.2 | 1.6 | 24.0 |
| Sion James (CHA) | 92% | 30.0<br><sub>32,35,30,32,28</sub> | 7.9<br><sub>3,3,3,9,5</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>8,8,6,1,4</sub> |  | 3.3<br><sub>6,4,4,2,4</sub> |  | 1.2<br><sub>0,1,0,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.2 | 1.2 | 15.7 |
| Coby White (CHA) | 98% | 25.5<br><sub>20,20,26,26,28</sub> | 18.8<br><sub>21,21,19,11,21</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,0,3,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.6<br><sub>3,1,4,9,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>2,2,2,0,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 2.6 | 26.8 |
| Grant Williams (CHA) | 86% | 22.4<br><sub>16,20,30,-,-</sub> | 9.5<br><sub>11,11,12,-,-</sub> |  | 4.1<br><sub>2,2,4,-,-</sub> |  | 1.7<br><sub>1,1,0,-,-</sub> |  | 1.4<br><sub>2,3,2,-,-</sub> |  | 0.8 | 0.6 | 1.0 | 15.3 |
| Christian Anderson (CHA) | 91% | 21.0<br><sub>18,18,14,21,25</sub> | 9.5<br><sub>13,16,5,4,25</sub> |  | 2.4<br><sub>0,3,1,1,2</sub> |  | 2.9<br><sub>2,2,4,2,3</sub> |  | 1.5<br><sub>3,4,1,0,6</sub> |  | 0.7 | 0.3 | 1.4 | 14.9 |
| Royce O'Neale (CHA) | 99% | 20.9<br><sub>22,19,34,21,13</sub> | 6.4<br><sub>7,3,13,9,0</sub> |  | 3.6<br><sub>4,3,4,1,1</sub> |  | 1.3<br><sub>0,1,1,0,1</sub> |  | 1.2<br><sub>2,1,4,3,0</sub> |  | 0.7 | 0.3 | 0.7 | 11.3 |
| Tidjane Salaun (CHA) | 98% | 14.5<br><sub>16,5,5,13,17</sub> | 5.2<br><sub>2,0,0,4,0</sub> |  | 3.6<br><sub>4,2,1,2,5</sub> |  | 0.7<br><sub>0,0,0,1,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 9.6 |
| Liam McNeeley (CHA) | 66% | 12.6<br><sub>-,2,-,7,9</sub> | 5.2<br><sub>-,0,-,2,3</sub> |  | 2.3<br><sub>-,0,-,1,2</sub> |  | 0.9<br><sub>-,0,-,0,0</sub> |  | 0.6<br><sub>-,0,-,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.4 |
| Hannes Steinbach (CHA) | 58% | 9.7<br><sub>-,-,-,-,4</sub> | 3.1<br><sub>-,-,-,-,3</sub> |  | 2.8<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.6 | 0.5 | 6.5 |
| PJ Hall (CHA) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.6 | 7.0 |
| Matas Buzelis (CHI) | 99% | 30.4<br><sub>31,30,25,38,27</sub> | 17.1<br><sub>23,25,9,21,15</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>3,5,5,5,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>0,4,1,3,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>3,5,1,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.9 | 2.1 | 24.1 |
| Josh Giddey (CHI) | 99% | 30.0<br><sub>24,28,23,41,22</sub> | 14.2<br><sub>4,18,2,23,4</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>4,14,6,14,2</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>8,9,7,22,11</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,1,0,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 3.0 | 30.2 |
| Isaac Okoro (CHI) | 99% | 29.8<br><sub>32,25,29,42,27</sub> | 10.0<br><sub>13,12,9,11,12</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>6,3,7,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>2,4,1,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>3,4,1,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.4 | 1.0 | 14.8 |
| Jalen Smith (CHI) | 100% | 28.4<br><sub>28,21,-,34,25</sub> | 14.2<br><sub>17,14,-,26,11</sub> | 13.5 · – | 7.4<br><sub>11,6,-,4,6</sub> | 6.5 | 1.9<br><sub>3,3,-,1,4</sub> | 2.5 | 2.0<br><sub>3,2,-,6,1</sub> | 1.5 | 0.7 | 0.9 | 1.2 | 23.5 |
| Buddy Hield (CHI) | 88% | 26.6<br><sub>19,19,23,40,27</sub> | 14.1<br><sub>6,11,15,33,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,1,4,7,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>2,2,0,6,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>2,3,4,7,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.3 | 1.3 | 19.9 |
| Tre Jones (CHI) | 99% | 23.8<br><sub>23,16,25,12,27</sub> | 13.6<br><sub>16,10,12,9,16</sub> |  | 2.7<br><sub>2,2,1,2,4</sub> |  | 4.9<br><sub>6,6,7,4,9</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 21.2 |
| Nic Claxton (CHI) | 98% | 22.5<br><sub>17,22,29,-,23</sub> | 8.9<br><sub>8,14,11,-,6</sub> |  | 5.1<br><sub>2,4,7,-,6</sub> |  | 2.0<br><sub>1,1,1,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.9 | 1.1 | 16.0 |
| Patrick Williams (CHI) | 91% | 21.5<br><sub>13,13,23,16,19</sub> | 7.3<br><sub>0,2,6,2,7</sub> |  | 2.7<br><sub>0,1,3,2,5</sub> |  | 1.6<br><sub>0,2,1,0,2</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.8 | 0.3 | 0.9 | 11.6 |
| Jordan Hawkins (CHI) | 66% | 15.6<br><sub>4,-,-,14,18</sub> | 7.4<br><sub>0,-,-,6,19</sub> |  | 1.9<br><sub>0,-,-,1,1</sub> |  | 1.0<br><sub>1,-,-,1,2</sub> |  | 1.0<br><sub>0,-,-,2,4</sub> |  | 0.4 | 0.2 | 0.6 | 10.3 |
| Zach Collins (CHI) | 63% | 14.2<br><sub>-,11,15,17,-</sub> | 5.5<br><sub>-,3,6,5,-</sub> |  | 3.3<br><sub>-,2,2,1,-</sub> |  | 1.3<br><sub>-,0,4,0,-</sub> |  | 0.3<br><sub>-,1,0,1,-</sub> |  | 0.4 | 0.3 | 0.7 | 10.1 |
| Leonard Miller (CHI) | 52% | 12.5<br><sub>1,7,-,-,-</sub> | 5.5<br><sub>0,4,-,-,-</sub> |  | 2.7<br><sub>0,2,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 8.9 |
| Noa Essengue (CHI) | 98% | 12.2<br><sub>14,15,15,11,4</sub> | 5.1<br><sub>1,5,8,9,6</sub> |  | 2.4<br><sub>2,3,4,4,2</sub> |  | 0.5<br><sub>1,0,0,0,0</sub> |  | 0.4<br><sub>0,0,2,1,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.1 |
| Dailyn Swain (CHI) | 52% | 6.6<br><sub>2,6,-,-,-</sub> | 2.8<br><sub>0,2,-,-,-</sub> |  | 0.9<br><sub>1,1,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>


### CLE @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.3–110.2 | CLE 50% | 1.98 / 2.02 | NYK +0.5 | 220.5 | NYK -2.5 covers 43%; o218.5 54% |
| Expected (weighted by chance each plays) | 109.2–112.3 | CLE 41% | 2.42 / 1.71 | NYK -3.5 | 221.5 | NYK -2.5 covers 52%; o218.5 56% |
| if Josh Hart plays | 109.6–112.3 | CLE 42% | 2.37 / 1.73 | NYK -3.5 | 221.5 | NYK -2.5 covers 52%; o218.5 57% |
| if Miles McBride plays | 110.2–111.1 | CLE 48% | 2.10 / 1.91 | NYK -1.5 | 221.5 | NYK -2.5 covers 46%; o218.5 56% |
| if Karl-Anthony Towns plays | 108.9–112.1 | CLE 41% | 2.45 / 1.69 | NYK -3.5 | 220.5 | NYK -2.5 covers 53%; o218.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Hart (NYK) | Questionable | 55% | 33.8 | 11.3 | 7.8 | 4.9 | 1.5 | 1.4 | 0.3 | 1.6 | 24.0 | full tables below |
| Miles McBride (NYK) | Questionable | 55% | 24.3 | 10.6 | 2.0 | 2.1 | 2.0 | 0.8 | 0.2 | 0.7 | 14.8 | full tables below |
| Karl-Anthony Towns (NYK) | Questionable | 55% | 35.2 | 23.7 | 14.1 | 4.6 | 2.3 | 1.1 | 0.8 | 2.9 | 42.4 | full tables below |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 99% | 33.4<br><sub>-,34,36,40,37</sub> | 17.9<br><sub>-,9,14,51,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>-,4,6,6,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>-,10,9,6,5</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>-,2,3,7,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.5 | 3.1 | 28.0 |
| Donovan Mitchell | 99% | 32.4<br><sub>-,36,35,29,37</sub> | 22.4<br><sub>-,39,34,20,28</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>-,4,4,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>-,4,3,3,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,2,2,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.6 | 30.8 |
| Jarrett Allen | 88% | 26.2<br><sub>-,30,30,31,29</sub> | 11.9<br><sub>-,13,19,6,16</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>-,14,9,8,4</sub> | 8.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>-,3,4,4,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.2 | 20.2 |
| Peyton Watson | 88% | 25.7<br><sub>-,22,-,29,29</sub> | 10.9<br><sub>-,14,-,15,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,4,-,4,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>-,0,-,3,3</sub> |  | 1.1<br><sub>-,2,-,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.2 | 1.5 | 16.7 |
| Sam Merrill | 98% | 21.2<br><sub>-,-,23,25,25</sub> | 7.5<br><sub>-,-,7,6,12</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>-,-,2,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>-,-,3,1,2</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.6 | 10.9 |
| Meleek Thomas | 97% | 21.0<br><sub>34,30,22,20,21</sub> | 9.5<br><sub>20,10,14,4,13</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>4,6,2,1,3</sub> |  | 1.4<br><sub>2,3,2,4,2</sub> |  | 1.4<br><sub>3,1,4,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 0.9 | 13.3 |
| Tyrese Proctor | 97% | 20.4<br><sub>34,29,26,24,21</sub> | 7.9<br><sub>24,17,8,5,4</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>11,3,1,1,2</sub> |  | 2.1<br><sub>10,2,1,2,2</sub> |  | 1.1<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 0.9 | 12.5 |
| Jaylon Tyson | 98% | 16.9<br><sub>34,-,-,-,12</sub> | 6.3<br><sub>18,-,-,-,0</sub> |  | 2.7<br><sub>4,-,-,-,2</sub> |  | 1.3<br><sub>4,-,-,-,0</sub> |  | 0.8<br><sub>3,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 10.2 |
| Mario Hezonja | 99% | 14.4<br><sub>34,15,28,20,12</sub> | 6.2<br><sub>22,9,16,10,4</sub> |  | 3.4<br><sub>7,4,7,10,5</sub> |  | 1.1<br><sub>4,2,5,3,0</sub> |  | 0.6<br><sub>2,1,2,2,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.8 |
| Thomas Bryant | 88% | 12.5<br><sub>27,18,12,16,8</sub> | 5.9<br><sub>19,9,5,9,0</sub> |  | 2.9<br><sub>11,5,4,6,2</sub> |  | 0.6<br><sub>3,4,0,0,0</sub> |  | 0.6<br><sub>2,0,1,2,0</sub> |  | 0.3 | 0.4 | 0.5 | 9.4 |
| Norchad Omier | 80% | 10.0<br><sub>27,13,16,6,8</sub> | 2.9<br><sub>13,4,2,2,2</sub> |  | 2.8<br><sub>8,6,7,1,4</sub> |  | 0.9<br><sub>2,2,0,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 6.6 |
| Craig Porter Jr. | 58% | 8.8<br><sub>28,14,12,-,-</sub> | 2.1<br><sub>9,2,2,-,-</sub> |  | 1.6<br><sub>9,1,3,-,-</sub> |  | 1.3<br><sub>6,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 5.0 |
| Riley Minix | 48% | 6.6<br><sub>22,-,-,-,-</sub> | 2.1<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.2 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 35.8<br><sub>41,34,35,36,32</sub> | 30.8<br><sub>28,31,21,30,22</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>1,5,2,7,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 7.5<br><sub>9,5,7,5,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>3,4,4,6,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.2 | 2.6 | 41.9 |
| Landry Shamet | 99% | 33.9<br><sub>30,24,30,36,32</sub> | 16.7<br><sub>23,12,10,20,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>2,1,1,1,2</sub> |  | 2.7<br><sub>0,1,2,3,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>4,2,2,6,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.2 | 1.4 | 21.9 |
| Mikal Bridges | 99% | 32.4<br><sub>32,30,31,28,31</sub> | 15.4<br><sub>5,17,8,12,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>7,5,3,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.8<br><sub>3,1,3,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 1.6 | 23.0 |
| Andre Drummond | 99% | 27.3<br><sub>7,11,15,23,19</sub> | 8.9<br><sub>2,2,4,7,2</sub> |  | 13.3<br><sub>3,8,4,13,10</sub> |  | 1.8<br><sub>0,0,0,1,1</sub> |  | 0.3<br><sub>0,0,0,1,0</sub> |  | 0.9 | 0.9 | 1.6 | 24.0 |
| Jose Alvarado | 84% | 26.4<br><sub>2,7,13,15,22</sub> | 11.2<br><sub>0,2,2,8,11</sub> |  | 3.3<br><sub>0,0,2,2,1</sub> |  | 4.8<br><sub>1,4,1,2,3</sub> |  | 1.7<br><sub>0,0,0,2,3</sub> |  | 1.2 | 0.3 | 1.4 | 19.3 |
| Tyler Kolek | 96% | 24.6<br><sub>16,13,12,13,11</sub> | 10.1<br><sub>0,4,6,7,8</sub> |  | 3.5<br><sub>0,1,3,3,3</sub> |  | 6.9<br><sub>7,3,5,0,0</sub> |  | 1.3<br><sub>0,0,1,0,1</sub> |  | 0.8 | 0.2 | 1.3 | 20.5 |
| James Wiseman | 48% | 23.9<br><sub>3,-,-,25,-</sub> | 8.4<br><sub>0,-,-,5,-</sub> |  | 7.6<br><sub>3,-,-,6,-</sub> |  | 1.2<br><sub>0,-,-,2,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.4 | 1.1 | 1.3 | 17.2 |
| Pacome Dadiet | 52% | 23.8<br><sub>-,-,-,11,17</sub> | 9.5<br><sub>-,-,-,5,5</sub> |  | 3.6<br><sub>-,-,-,0,2</sub> |  | 1.4<br><sub>-,-,-,2,0</sub> |  | 1.4<br><sub>-,-,-,1,1</sub> |  | 0.7 | 0.2 | 0.8 | 14.6 |
| Mohamed Diawara | 52% | 23.2<br><sub>-,-,-,-,8</sub> | 9.0<br><sub>-,-,-,-,0</sub> |  | 3.8<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 15.2 |
| Dalton Knecht | 58% | 18.7<br><sub>-,-,-,3,-</sub> | 7.5<br><sub>-,-,-,0,-</sub> |  | 3.1<br><sub>-,-,-,0,-</sub> |  | 1.0<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.6 | 11.6 |
| Jaden Akins | 38% | 14.9<br><sub>-,-,-,-,-</sub> | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.8 |
| Tyler Nickel | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Karl-Anthony Towns plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 99% | 33.5<br><sub>-,34,36,40,37</sub> | 17.8<br><sub>-,9,14,51,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>-,4,6,6,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>-,10,9,6,5</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>-,2,3,7,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.5 | 3.1 | 28.0 |
| Donovan Mitchell (CLE) | 99% | 32.5<br><sub>-,36,35,29,37</sub> | 22.4<br><sub>-,39,34,20,28</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>-,4,4,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>-,4,3,3,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,2,2,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.6 | 30.7 |
| Jarrett Allen (CLE) | 88% | 26.2<br><sub>-,30,30,31,29</sub> | 11.8<br><sub>-,13,19,6,16</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>-,14,9,8,4</sub> | 8.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>-,3,4,4,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.9 | 1.2 | 20.2 |
| Peyton Watson (CLE) | 88% | 25.8<br><sub>-,22,-,29,29</sub> | 10.8<br><sub>-,14,-,15,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,4,-,4,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>-,0,-,3,3</sub> |  | 1.1<br><sub>-,2,-,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.2 | 1.5 | 16.7 |
| Sam Merrill (CLE) | 98% | 21.2<br><sub>-,-,23,25,25</sub> | 7.4<br><sub>-,-,7,6,12</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>-,-,2,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>-,-,3,1,2</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.6 | 10.9 |
| Meleek Thomas (CLE) | 97% | 21.0<br><sub>34,30,22,20,21</sub> | 9.4<br><sub>20,10,14,4,13</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>4,6,2,1,3</sub> |  | 1.4<br><sub>2,3,2,4,2</sub> |  | 1.4<br><sub>3,1,4,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 0.9 | 13.2 |
| Tyrese Proctor (CLE) | 97% | 20.3<br><sub>34,29,26,24,21</sub> | 7.8<br><sub>24,17,8,5,4</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>11,3,1,1,2</sub> |  | 2.1<br><sub>10,2,1,2,2</sub> |  | 1.1<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 0.9 | 12.5 |
| Jaylon Tyson (CLE) | 98% | 17.0<br><sub>34,-,-,-,12</sub> | 6.4<br><sub>18,-,-,-,0</sub> |  | 2.7<br><sub>4,-,-,-,2</sub> |  | 1.3<br><sub>4,-,-,-,0</sub> |  | 0.8<br><sub>3,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.8 | 10.3 |
| Mario Hezonja (CLE) | 99% | 14.3<br><sub>34,15,28,20,12</sub> | 6.1<br><sub>22,9,16,10,4</sub> |  | 3.4<br><sub>7,4,7,10,5</sub> |  | 1.1<br><sub>4,2,5,3,0</sub> |  | 0.6<br><sub>2,1,2,2,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.6 |
| Thomas Bryant (CLE) | 88% | 12.5<br><sub>27,18,12,16,8</sub> | 5.8<br><sub>19,9,5,9,0</sub> |  | 2.9<br><sub>11,5,4,6,2</sub> |  | 0.6<br><sub>3,4,0,0,0</sub> |  | 0.6<br><sub>2,0,1,2,0</sub> |  | 0.3 | 0.4 | 0.5 | 9.4 |
| Norchad Omier (CLE) | 80% | 9.8<br><sub>27,13,16,6,8</sub> | 2.9<br><sub>13,4,2,2,2</sub> |  | 2.8<br><sub>8,6,7,1,4</sub> |  | 0.9<br><sub>2,2,0,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 6.5 |
| Craig Porter Jr. (CLE) | 58% | 8.8<br><sub>28,14,12,-,-</sub> | 2.2<br><sub>9,2,2,-,-</sub> |  | 1.5<br><sub>9,1,3,-,-</sub> |  | 1.4<br><sub>6,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 5.1 |
| Riley Minix (CLE) | 48% | 6.6<br><sub>22,-,-,-,-</sub> | 2.0<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.2 |
| Jalen Brunson (NYK) | 99% | 37.1<br><sub>41,34,35,36,32</sub> | 28.5<br><sub>28,31,21,30,22</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>1,5,2,7,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 7.2<br><sub>9,5,7,5,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>3,4,4,6,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.2 | 2.6 | 39.0 |
| Karl-Anthony Towns (NYK) | 100% | 35.2<br><sub>43,36,33,-,29</sub> | 23.7<br><sub>28,16,22,-,30</sub> | 21.5 · – | 14.1<br><sub>17,16,12,-,13</sub> | 12.5 | 4.6<br><sub>3,8,4,-,5</sub> | 3.5 | 2.3<br><sub>3,1,2,-,4</sub> | 1.5 | 1.1 | 0.8 | 2.9 | 42.4 |
| Landry Shamet (NYK) | 99% | 34.1<br><sub>30,24,30,36,32</sub> | 14.8<br><sub>23,12,10,20,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>2,1,1,1,2</sub> |  | 2.3<br><sub>0,1,2,3,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>4,2,2,6,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.2 | 1.0 | 19.4 |
| Mikal Bridges (NYK) | 99% | 33.2<br><sub>32,30,31,28,31</sub> | 13.8<br><sub>5,17,8,12,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>7,5,3,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.2<br><sub>3,1,3,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 1.2 | 20.7 |
| Jose Alvarado (NYK) | 84% | 23.4<br><sub>2,7,13,15,22</sub> | 8.6<br><sub>0,2,2,8,11</sub> |  | 2.8<br><sub>0,0,2,2,1</sub> |  | 3.9<br><sub>1,4,1,2,3</sub> |  | 1.4<br><sub>0,0,0,2,3</sub> |  | 1.0 | 0.2 | 1.1 | 15.3 |
| Andre Drummond (NYK) | 99% | 22.6<br><sub>7,11,15,23,19</sub> | 6.4<br><sub>2,2,4,7,2</sub> |  | 10.4<br><sub>3,8,4,13,10</sub> |  | 1.4<br><sub>0,0,0,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.8 | 0.8 | 1.1 | 18.2 |
| Tyler Kolek (NYK) | 96% | 20.9<br><sub>16,13,12,13,11</sub> | 7.2<br><sub>0,4,6,7,8</sub> |  | 2.9<br><sub>0,1,3,3,3</sub> |  | 5.4<br><sub>7,3,5,0,0</sub> |  | 0.9<br><sub>0,0,1,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 15.4 |
| Pacome Dadiet (NYK) | 52% | 18.6<br><sub>-,-,-,11,17</sub> | 6.8<br><sub>-,-,-,5,5</sub> |  | 2.8<br><sub>-,-,-,0,2</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 0.9<br><sub>-,-,-,1,1</sub> |  | 0.6 | 0.1 | 0.6 | 10.6 |
| Mohamed Diawara (NYK) | 52% | 17.4<br><sub>-,-,-,-,8</sub> | 5.8<br><sub>-,-,-,-,0</sub> |  | 2.7<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.1 |
| James Wiseman (NYK) | 48% | 17.2<br><sub>3,-,-,25,-</sub> | 5.2<br><sub>0,-,-,5,-</sub> |  | 5.4<br><sub>3,-,-,6,-</sub> |  | 0.8<br><sub>0,-,-,2,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.8 | 0.9 | 11.3 |
| Dalton Knecht (NYK) | 58% | 14.8<br><sub>-,-,-,3,-</sub> | 5.2<br><sub>-,-,-,0,-</sub> |  | 2.5<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.3 | 0.4 | 8.4 |
| Jaden Akins (NYK) | 38% | 10.9<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.3 |
| Tyler Nickel (NYK) | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>if Josh Hart plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 99% | 33.4<br><sub>-,34,36,40,37</sub> | 17.8<br><sub>-,9,14,51,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>-,4,6,6,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>-,10,9,6,5</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>-,2,3,7,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.5 | 3.1 | 27.9 |
| Donovan Mitchell (CLE) | 99% | 32.4<br><sub>-,36,35,29,37</sub> | 22.4<br><sub>-,39,34,20,28</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>-,4,4,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>-,4,3,3,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,2,2,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.6 | 30.8 |
| Jarrett Allen (CLE) | 88% | 26.2<br><sub>-,30,30,31,29</sub> | 11.8<br><sub>-,13,19,6,16</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>-,14,9,8,4</sub> | 8.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>-,3,4,4,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.2 | 20.2 |
| Peyton Watson (CLE) | 88% | 25.8<br><sub>-,22,-,29,29</sub> | 10.8<br><sub>-,14,-,15,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,4,-,4,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>-,0,-,3,3</sub> |  | 1.1<br><sub>-,2,-,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.2 | 1.5 | 16.7 |
| Sam Merrill (CLE) | 98% | 21.1<br><sub>-,-,23,25,25</sub> | 7.4<br><sub>-,-,7,6,12</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>-,-,2,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>-,-,3,1,2</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.6 | 10.8 |
| Meleek Thomas (CLE) | 97% | 21.0<br><sub>34,30,22,20,21</sub> | 9.5<br><sub>20,10,14,4,13</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>4,6,2,1,3</sub> |  | 1.4<br><sub>2,3,2,4,2</sub> |  | 1.4<br><sub>3,1,4,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 0.9 | 13.2 |
| Tyrese Proctor (CLE) | 97% | 20.3<br><sub>34,29,26,24,21</sub> | 7.8<br><sub>24,17,8,5,4</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>11,3,1,1,2</sub> |  | 2.0<br><sub>10,2,1,2,2</sub> |  | 1.1<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 0.9 | 12.4 |
| Jaylon Tyson (CLE) | 98% | 17.0<br><sub>34,-,-,-,12</sub> | 6.4<br><sub>18,-,-,-,0</sub> |  | 2.7<br><sub>4,-,-,-,2</sub> |  | 1.3<br><sub>4,-,-,-,0</sub> |  | 0.8<br><sub>3,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.8 | 10.4 |
| Mario Hezonja (CLE) | 99% | 14.4<br><sub>34,15,28,20,12</sub> | 6.2<br><sub>22,9,16,10,4</sub> |  | 3.4<br><sub>7,4,7,10,5</sub> |  | 1.1<br><sub>4,2,5,3,0</sub> |  | 0.6<br><sub>2,1,2,2,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.7 |
| Thomas Bryant (CLE) | 88% | 12.5<br><sub>27,18,12,16,8</sub> | 5.9<br><sub>19,9,5,9,0</sub> |  | 2.9<br><sub>11,5,4,6,2</sub> |  | 0.6<br><sub>3,4,0,0,0</sub> |  | 0.6<br><sub>2,0,1,2,0</sub> |  | 0.3 | 0.4 | 0.5 | 9.4 |
| Norchad Omier (CLE) | 80% | 9.9<br><sub>27,13,16,6,8</sub> | 2.9<br><sub>13,4,2,2,2</sub> |  | 2.8<br><sub>8,6,7,1,4</sub> |  | 0.9<br><sub>2,2,0,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 6.6 |
| Craig Porter Jr. (CLE) | 58% | 8.8<br><sub>28,14,12,-,-</sub> | 2.1<br><sub>9,2,2,-,-</sub> |  | 1.6<br><sub>9,1,3,-,-</sub> |  | 1.4<br><sub>6,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 5.1 |
| Riley Minix (CLE) | 48% | 6.6<br><sub>22,-,-,-,-</sub> | 2.0<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.2 |
| Jalen Brunson (NYK) | 99% | 36.3<br><sub>41,34,35,36,32</sub> | 30.3<br><sub>28,31,21,30,22</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>1,5,2,7,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 6.7<br><sub>9,5,7,5,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>3,4,4,6,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.2 | 2.5 | 40.4 |
| Josh Hart (NYK) | 100% | 33.8<br><sub>26,31,28,35,39</sub> | 11.3<br><sub>0,5,11,0,10</sub> | 9.5 · – | 7.8<br><sub>5,4,6,8,11</sub> | 7.5 | 4.9<br><sub>2,2,2,6,10</sub> | 3.5 | 1.5<br><sub>0,1,3,0,0</sub> | 1.5 | 1.4 | 0.3 | 1.6 | 24.0 |
| Landry Shamet (NYK) | 99% | 33.5<br><sub>30,24,30,36,32</sub> | 16.0<br><sub>23,12,10,20,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>2,1,1,1,2</sub> |  | 2.2<br><sub>0,1,2,3,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.9<br><sub>4,2,2,6,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.2 | 1.1 | 20.5 |
| Mikal Bridges (NYK) | 99% | 32.3<br><sub>32,30,31,28,31</sub> | 14.8<br><sub>5,17,8,12,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>7,5,3,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.1<br><sub>3,1,3,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.5 | 1.3 | 21.7 |
| Andre Drummond (NYK) | 99% | 24.7<br><sub>7,11,15,23,19</sub> | 8.2<br><sub>2,2,4,7,2</sub> |  | 11.6<br><sub>3,8,4,13,10</sub> |  | 1.5<br><sub>0,0,0,1,1</sub> |  | 0.3<br><sub>0,0,0,1,0</sub> |  | 0.8 | 0.9 | 1.2 | 21.3 |
| Jose Alvarado (NYK) | 84% | 22.5<br><sub>2,7,13,15,22</sub> | 9.4<br><sub>0,2,2,8,11</sub> |  | 2.8<br><sub>0,0,2,2,1</sub> |  | 3.7<br><sub>1,4,1,2,3</sub> |  | 1.4<br><sub>0,0,0,2,3</sub> |  | 1.0 | 0.2 | 1.1 | 15.9 |
| Tyler Kolek (NYK) | 96% | 19.5<br><sub>16,13,12,13,11</sub> | 7.7<br><sub>0,4,6,7,8</sub> |  | 2.8<br><sub>0,1,3,3,3</sub> |  | 5.0<br><sub>7,3,5,0,0</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 15.6 |
| James Wiseman (NYK) | 48% | 19.4<br><sub>3,-,-,25,-</sub> | 6.6<br><sub>0,-,-,5,-</sub> |  | 6.1<br><sub>3,-,-,6,-</sub> |  | 0.9<br><sub>0,-,-,2,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.8 | 1.0 | 13.6 |
| Pacome Dadiet (NYK) | 52% | 19.1<br><sub>-,-,-,11,17</sub> | 7.2<br><sub>-,-,-,5,5</sub> |  | 2.9<br><sub>-,-,-,0,2</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 1.0<br><sub>-,-,-,1,1</sub> |  | 0.6 | 0.1 | 0.6 | 11.2 |
| Mohamed Diawara (NYK) | 52% | 17.4<br><sub>-,-,-,-,8</sub> | 6.7<br><sub>-,-,-,-,0</sub> |  | 2.8<br><sub>-,-,-,-,2</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.7 | 11.2 |
| Dalton Knecht (NYK) | 58% | 14.8<br><sub>-,-,-,3,-</sub> | 5.6<br><sub>-,-,-,0,-</sub> |  | 2.5<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.9<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 8.7 |
| Jaden Akins (NYK) | 38% | 9.7<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.2 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |

</details>

<details><summary>if Miles McBride plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 99% | 33.4<br><sub>-,34,36,40,37</sub> | 17.9<br><sub>-,9,14,51,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>-,4,6,6,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>-,10,9,6,5</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>-,2,3,7,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.5 | 3.1 | 28.0 |
| Donovan Mitchell (CLE) | 99% | 32.4<br><sub>-,36,35,29,37</sub> | 22.5<br><sub>-,39,34,20,28</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>-,4,4,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>-,4,3,3,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,2,2,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.6 | 30.9 |
| Jarrett Allen (CLE) | 88% | 26.3<br><sub>-,30,30,31,29</sub> | 11.9<br><sub>-,13,19,6,16</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>-,14,9,8,4</sub> | 8.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>-,3,4,4,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.2 | 20.3 |
| Peyton Watson (CLE) | 88% | 25.8<br><sub>-,22,-,29,29</sub> | 10.9<br><sub>-,14,-,15,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,4,-,4,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>-,0,-,3,3</sub> |  | 1.1<br><sub>-,2,-,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 1.2 | 1.5 | 16.8 |
| Sam Merrill (CLE) | 98% | 21.3<br><sub>-,-,23,25,25</sub> | 7.5<br><sub>-,-,7,6,12</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>-,-,2,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>-,-,3,1,2</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.6 | 10.9 |
| Meleek Thomas (CLE) | 97% | 20.9<br><sub>34,30,22,20,21</sub> | 9.5<br><sub>20,10,14,4,13</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>4,6,2,1,3</sub> |  | 1.4<br><sub>2,3,2,4,2</sub> |  | 1.4<br><sub>3,1,4,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 0.9 | 13.2 |
| Tyrese Proctor (CLE) | 97% | 20.3<br><sub>34,29,26,24,21</sub> | 7.8<br><sub>24,17,8,5,4</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>11,3,1,1,2</sub> |  | 2.1<br><sub>10,2,1,2,2</sub> |  | 1.1<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 0.9 | 12.5 |
| Jaylon Tyson (CLE) | 98% | 16.9<br><sub>34,-,-,-,12</sub> | 6.3<br><sub>18,-,-,-,0</sub> |  | 2.7<br><sub>4,-,-,-,2</sub> |  | 1.3<br><sub>4,-,-,-,0</sub> |  | 0.8<br><sub>3,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.8 | 10.3 |
| Mario Hezonja (CLE) | 99% | 14.3<br><sub>34,15,28,20,12</sub> | 6.1<br><sub>22,9,16,10,4</sub> |  | 3.4<br><sub>7,4,7,10,5</sub> |  | 1.1<br><sub>4,2,5,3,0</sub> |  | 0.6<br><sub>2,1,2,2,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.6 |
| Thomas Bryant (CLE) | 88% | 12.5<br><sub>27,18,12,16,8</sub> | 5.9<br><sub>19,9,5,9,0</sub> |  | 2.9<br><sub>11,5,4,6,2</sub> |  | 0.6<br><sub>3,4,0,0,0</sub> |  | 0.6<br><sub>2,0,1,2,0</sub> |  | 0.3 | 0.4 | 0.5 | 9.3 |
| Norchad Omier (CLE) | 80% | 9.9<br><sub>27,13,16,6,8</sub> | 2.9<br><sub>13,4,2,2,2</sub> |  | 2.8<br><sub>8,6,7,1,4</sub> |  | 0.9<br><sub>2,2,0,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 6.6 |
| Craig Porter Jr. (CLE) | 58% | 8.7<br><sub>28,14,12,-,-</sub> | 2.2<br><sub>9,2,2,-,-</sub> |  | 1.5<br><sub>9,1,3,-,-</sub> |  | 1.4<br><sub>6,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 5.0 |
| Riley Minix (CLE) | 48% | 6.5<br><sub>22,-,-,-,-</sub> | 2.1<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 3.2 |
| Jalen Brunson (NYK) | 99% | 36.0<br><sub>41,34,35,36,32</sub> | 30.2<br><sub>28,31,21,30,22</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,5,2,7,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 7.5<br><sub>9,5,7,5,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>3,4,4,6,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.2 | 2.5 | 41.3 |
| Landry Shamet (NYK) | 99% | 34.0<br><sub>30,24,30,36,32</sub> | 16.2<br><sub>23,12,10,20,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,1,1,1,2</sub> |  | 2.6<br><sub>0,1,2,3,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>4,2,2,6,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.2 | 1.2 | 21.2 |
| Mikal Bridges (NYK) | 99% | 32.4<br><sub>32,30,31,28,31</sub> | 14.7<br><sub>5,17,8,12,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>7,5,3,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.6<br><sub>3,1,3,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 1.4 | 22.1 |
| Andre Drummond (NYK) | 99% | 26.4<br><sub>7,11,15,23,19</sub> | 8.1<br><sub>2,2,4,7,2</sub> |  | 12.7<br><sub>3,8,4,13,10</sub> |  | 1.7<br><sub>0,0,0,1,1</sub> |  | 0.3<br><sub>0,0,0,1,0</sub> |  | 0.9 | 0.9 | 1.3 | 22.5 |
| Jose Alvarado (NYK) | 84% | 24.4<br><sub>2,7,13,15,22</sub> | 9.9<br><sub>0,2,2,8,11</sub> |  | 3.0<br><sub>0,0,2,2,1</sub> |  | 4.2<br><sub>1,4,1,2,3</sub> |  | 1.5<br><sub>0,0,0,2,3</sub> |  | 1.1 | 0.2 | 1.2 | 17.2 |
| Miles McBride (NYK) | 100% | 24.3<br><sub>14,9,8,14,-</sub> | 10.6<br><sub>3,3,3,3,-</sub> |  | 2.0<br><sub>1,0,0,0,-</sub> |  | 2.1<br><sub>0,1,0,1,-</sub> |  | 2.0<br><sub>1,1,0,1,-</sub> |  | 0.8 | 0.2 | 0.7 | 14.8 |
| James Wiseman (NYK) | 48% | 22.1<br><sub>3,-,-,25,-</sub> | 7.5<br><sub>0,-,-,5,-</sub> |  | 6.8<br><sub>3,-,-,6,-</sub> |  | 1.1<br><sub>0,-,-,2,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.4 | 1.0 | 1.1 | 15.5 |
| Pacome Dadiet (NYK) | 52% | 21.9<br><sub>-,-,-,11,17</sub> | 8.2<br><sub>-,-,-,5,5</sub> |  | 3.3<br><sub>-,-,-,0,2</sub> |  | 1.3<br><sub>-,-,-,2,0</sub> |  | 1.2<br><sub>-,-,-,1,1</sub> |  | 0.6 | 0.2 | 0.7 | 12.8 |
| Tyler Kolek (NYK) | 96% | 21.9<br><sub>16,13,12,13,11</sub> | 8.5<br><sub>0,4,6,7,8</sub> |  | 3.1<br><sub>0,1,3,3,3</sub> |  | 5.8<br><sub>7,3,5,0,0</sub> |  | 1.1<br><sub>0,0,1,0,1</sub> |  | 0.7 | 0.1 | 1.0 | 17.4 |
| Mohamed Diawara (NYK) | 52% | 20.7<br><sub>-,-,-,-,8</sub> | 7.8<br><sub>-,-,-,-,0</sub> |  | 3.3<br><sub>-,-,-,-,2</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.8 | 13.2 |
| Dalton Knecht (NYK) | 58% | 16.2<br><sub>-,-,-,3,-</sub> | 6.2<br><sub>-,-,-,0,-</sub> |  | 2.7<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 1.0<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.5 | 9.7 |
| Jaden Akins (NYK) | 38% | 11.3<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 1.4 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |

</details>


### MIN @ OKC
Out: Chet Holmgren (OKC), Aday Mara (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC), Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 35.7<br><sub>31,37,39,36,34</sub> | 18.9<br><sub>13,22,17,25,34</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>6,5,3,5,10</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,4,1,4,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>0,2,4,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.9 | 2.4 | 28.1 |
| Ayo Dosunmu | 99% | 33.6<br><sub>30,39,32,34,30</sub> | 17.9<br><sub>8,30,6,19,23</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>5,4,4,2,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>2,5,4,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>2,7,2,1,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.3 | 2.3 | 25.9 |
| Jonathan Kuminga | 88% | 31.8<br><sub>29,-,35,37,26</sub> | 14.1<br><sub>13,-,23,16,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>9,-,3,4,5</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>1,-,3,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,-,2,2,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.6 | 2.0 | 22.3 |
| LaMelo Ball | 99% | 31.3<br><sub>24,31,35,32,30</sub> | 18.1<br><sub>6,18,15,12,17</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>5,9,8,5,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>0,2,8,7,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,3,3,1,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.3 | 3.0 | 28.4 |
| Rudy Gobert | 99% | 30.9<br><sub>32,22,35,32,27</sub> | 8.6<br><sub>18,0,9,7,7</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>15,4,7,11,6</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>3,2,0,2,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.1 | 1.6 | 20.7 |
| Terrence Shannon Jr. | 98% | 23.9<br><sub>35,24,21,26,24</sub> | 12.7<br><sub>34,12,10,15,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,1,4,5,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.3<br><sub>6,4,3,2,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,1,0,3,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.5 | 0.1 | 1.4 | 17.9 |
| Trey Lyles | 99% | 19.5<br><sub>19,31,16,12,24</sub> | 6.4<br><sub>9,8,8,3,9</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>3,7,6,3,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>1,4,1,1,2</sub> |  | 0.9<br><sub>2,2,2,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 11.7 |
| Joan Beringer | 98% | 16.1<br><sub>16,26,13,16,19</sub> | 4.8<br><sub>0,3,5,0,0</sub> |  | 5.2<br><sub>4,13,3,4,4</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.3 | 0.7 | 10.4 |
| Bones Hyland | 98% | 15.6<br><sub>13,17,15,16,16</sub> | 8.6<br><sub>5,13,6,7,14</sub> |  | 1.6<br><sub>1,2,1,0,2</sub> |  | 2.5<br><sub>5,1,1,4,6</sub> |  | 1.3<br><sub>0,3,1,1,4</sub> |  | 0.6 | 0.2 | 1.1 | 12.7 |
| Cody Williams | 58% | 6.6<br><sub>4,13,-,-,2</sub> | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.9<br><sub>1,1,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 1.3 |
| Zyon Pullin | 52% | 6.4<br><sub>4,-,-,-,2</sub> | 2.9<br><sub>0,-,-,-,4</sub> |  | 0.9<br><sub>1,-,-,-,2</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.7 |
| Isaiah Evans | 52% | 5.9<br><sub>4,-,-,-,2</sub> | 3.2<br><sub>0,-,-,-,2</sub> |  | 1.3<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.1 | 0.4 | 4.8 |
| Johni Broome | 52% | 5.6<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 99% | 36.0<br><sub>30,36,37,-,38</sub> | 32.6<br><sub>37,34,40,-,38</sub> | 32.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,5,3,-,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>2,3,8,-,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>4,1,4,-,4</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.9 | 2.9 | 43.5 |
| Jared McCain | 99% | 31.6<br><sub>30,33,30,29,36</sub> | 16.0<br><sub>12,18,18,20,13</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,3,3,2,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>1,1,0,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>1,4,3,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 1.6 | 21.8 |
| Ajay Mitchell | 99% | 31.2<br><sub>27,34,31,22,35</sub> | 17.6<br><sub>14,13,8,17,12</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,6,2,3,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.0<br><sub>5,6,4,3,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,0,1,2,2</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.3 | 0.4 | 1.7 | 25.7 |
| Isaiah Hartenstein | 99% | 28.3<br><sub>18,27,28,23,30</sub> | 10.2<br><sub>3,6,5,2,18</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 10.8<br><sub>11,17,8,8,9</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>2,6,4,4,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.0 | 1.8 | 25.2 |
| Kenrich Williams | 98% | 25.6<br><sub>19,23,28,26,26</sub> | 9.7<br><sub>10,10,6,12,20</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>1,5,2,4,9</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>2,1,4,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>2,0,1,2,4</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 0.8 | 16.7 |
| Bennett Stirtz | 99% | 21.8<br><sub>17,17,25,32,19</sub> | 8.1<br><sub>0,6,18,21,5</sub> |  | 2.3<br><sub>1,0,2,3,9</sub> |  | 1.7<br><sub>2,2,2,5,3</sub> |  | 1.3<br><sub>0,2,4,5,1</sub> |  | 0.8 | 0.3 | 0.8 | 12.1 |
| Micah Peavy | 93% | 20.2<br><sub>13,-,9,31,24</sub> | 5.2<br><sub>5,-,2,9,7</sub> |  | 3.7<br><sub>3,-,2,6,3</sub> |  | 0.9<br><sub>1,-,0,1,2</sub> |  | 0.5<br><sub>1,-,0,1,1</sub> |  | 0.7 | 0.3 | 0.7 | 9.8 |
| Josh Dix | 67% | 18.4<br><sub>-,-,-,32,16</sub> | 5.3<br><sub>-,-,-,13,0</sub> |  | 2.1<br><sub>-,-,-,5,1</sub> |  | 1.1<br><sub>-,-,-,4,1</sub> |  | 0.6<br><sub>-,-,-,3,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.6 |
| Alex Caruso | 63% | 18.1<br><sub>18,9,-,-,-</sub> | 7.0<br><sub>11,5,-,-,-</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,0,-,-,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>3,1,-,-,-</sub> |  | 0.9<br><sub>1,0,-,-,-</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1 | 0.4 | 0.8 | 11.9 |
| Nique Clifford | 98% | 14.8<br><sub>24,13,15,26,6</sub> | 5.1<br><sub>9,7,4,11,0</sub> |  | 2.3<br><sub>3,0,5,3,0</sub> |  | 1.0<br><sub>0,0,1,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Brooks Barnhizer | 63% | 11.3<br><sub>4,-,-,19,9</sub> | 3.0<br><sub>0,-,-,8,7</sub> |  | 2.5<br><sub>0,-,-,4,4</sub> |  | 0.8<br><sub>0,-,-,2,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.3 |

</details>


### LAC @ MEM
Out: Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM), Bradley Beal (LAC)

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 99% | 30.3<br><sub>35,30,35,32,34</sub> | 19.4<br><sub>27,20,23,16,26</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>6,3,0,1,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 6.4<br><sub>7,7,5,2,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>3,2,3,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.3 | 3.0 | 28.2 |
| Brandon Ingram | 96% | 27.5<br><sub>-,-,-,-,27</sub> | 15.6<br><sub>-,-,-,-,16</sub> | 17.5 · –<br><sub>o 45% · u 55%</sub> | 4.6<br><sub>-,-,-,-,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>-,-,-,-,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>-,-,-,-,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.7 | 2.1 | 23.1 |
| Rui Hachimura | 98% | 26.8<br><sub>22,27,32,29,29</sub> | 13.2<br><sub>4,20,17,19,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>2,5,7,8,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,4,2,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.4 | 1.2 | 19.1 |
| Derrick Jones Jr. | 99% | 24.9<br><sub>26,28,27,26,23</sub> | 8.9<br><sub>13,5,8,4,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>4,1,2,7,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>1,1,1,1,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0<br><sub>3,0,0,1,1</sub> |  | 0.9 | 0.9 | 0.9 | 13.9 |
| Max Strus | 98% | 23.2<br><sub>25,21,32,29,26</sub> | 8.8<br><sub>14,3,18,5,8</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>3,2,5,6,0</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>4,1,4,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>4,1,5,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.2 | 1.0 | 15.1 |
| Brook Lopez | 99% | 22.8<br><sub>29,23,27,25,21</sub> | 12.1<br><sub>7,23,23,21,3</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>5,6,3,6,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>8,2,4,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,4,5,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 1.1 | 1.1 | 18.4 |
| Kris Dunn | 99% | 21.6<br><sub>18,26,20,19,23</sub> | 6.0<br><sub>7,2,6,3,9</sub> |  | 3.1<br><sub>3,5,2,4,5</sub> |  | 3.4<br><sub>1,5,2,5,4</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 1.5 | 0.3 | 1.1 | 12.5 |
| Keaton Wagler | 98% | 18.3<br><sub>28,18,17,19,17</sub> | 9.3<br><sub>12,15,7,7,2</sub> |  | 2.7<br><sub>4,2,5,7,1</sub> |  | 2.5<br><sub>5,0,2,3,2</sub> |  | 1.0<br><sub>2,1,1,1,0</sub> |  | 0.7 | 0.2 | 1.5 | 14.5 |
| Kobe Sanders | 98% | 15.6<br><sub>20,18,14,19,12</sub> | 6.3<br><sub>2,5,0,9,6</sub> |  | 1.8<br><sub>6,1,1,3,0</sub> |  | 1.5<br><sub>4,3,1,1,0</sub> |  | 0.8<br><sub>0,0,0,3,2</sub> |  | 0.7 | 0.1 | 0.8 | 9.5 |
| Isaiah Jackson | 98% | 13.9<br><sub>15,19,9,4,18</sub> | 6.0<br><sub>13,8,6,0,6</sub> |  | 4.3<br><sub>2,5,4,0,6</sub> |  | 1.2<br><sub>2,0,2,0,2</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.7 | 1.0 | 1.0 | 11.4 |
| Gradey Dick | 76% | 10.9<br><sub>19,17,13,16,-</sub> | 4.7<br><sub>12,0,2,6,-</sub> |  | 1.7<br><sub>2,0,2,5,-</sub> |  | 0.6<br><sub>0,1,1,2,-</sub> |  | 0.4<br><sub>2,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.9 |
| Yanic Konan Niederhauser | 72% | 9.3<br><sub>-,-,11,16,8</sub> | 3.4<br><sub>-,-,2,6,2</sub> |  | 2.6<br><sub>-,-,3,6,1</sub> |  | 0.6<br><sub>-,-,0,1,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 6.6 |
| Baba Miller | 91% | 7.6<br><sub>5,4,1,3,1</sub> | 3.8<br><sub>2,3,0,1,0</sub> |  | 1.3<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.0 |
| Cam Christie | 66% | 5.9<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,3,0,3,-</sub> |  | 1.0<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,1,-</sub> |  | 0.1<br><sub>-,1,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Jalen Pickett | 52% | 5.9<br><sub>-,-,1,-,-</sub> | 2.3<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Blake Wesley | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.9 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 30.8<br><sub>27,33,25,30,30</sub> | 17.0<br><sub>18,20,19,23,16</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>8,3,4,7,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 3.8<br><sub>6,5,4,2,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,4,5,4,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.4 | 1.9 | 28.6 |
| Ty Jerome | 98% | 30.1<br><sub>-,-,-,27,29</sub> | 23.4<br><sub>-,-,-,18,29</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>-,-,-,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>-,-,-,6,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>-,-,-,3,7</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.2 | 2.8 | 32.7 |
| Jaylen Wells | 99% | 27.2<br><sub>27,26,24,25,20</sub> | 12.1<br><sub>8,5,22,8,8</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>4,4,7,1,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.1 | 0.8 | 16.7 |
| Cam Spencer | 98% | 25.0<br><sub>32,29,27,30,21</sub> | 11.7<br><sub>12,26,9,9,24</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>6,1,2,5,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>9,7,11,5,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,5,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.4 | 20.9 |
| Zach Edey | 88% | 23.2<br><sub>21,21,-,23,23</sub> | 10.7<br><sub>23,11,-,8,8</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 8.9<br><sub>10,2,-,2,11</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,1,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 1.2 | 1.5 | 20.7 |
| Javon Small | 98% | 22.9<br><sub>29,21,25,-,19</sub> | 10.1<br><sub>12,2,14,-,3</sub> |  | 3.4<br><sub>5,4,7,-,3</sub> |  | 4.6<br><sub>12,5,7,-,5</sub> |  | 1.3<br><sub>0,0,2,-,0</sub> |  | 0.8 | 0.2 | 1.5 | 18.2 |
| Taylor Hendricks | 91% | 22.8<br><sub>19,21,20,27,24</sub> | 10.0<br><sub>9,18,11,5,3</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>3,6,1,7,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>0,2,1,2,1</sub> |  | 1.2<br><sub>1,1,0,0,1</sub> |  | 0.9 | 0.5 | 1.1 | 16.2 |
| Olivier-Maxence Prosper | 88% | 19.5<br><sub>16,16,24,23,19</sub> | 10.1<br><sub>12,5,16,7,6</sub> |  | 3.8<br><sub>0,2,5,6,3</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.7 | 0.2 | 0.8 | 14.9 |
| Isaiah Stewart | 98% | 18.7<br><sub>-,-,18,21,21</sub> | 9.0<br><sub>-,-,8,10,11</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>-,-,4,2,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>-,-,1,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.3 | 0.9 | 0.9 | 13.7 |
| Kris Murray | 91% | 18.0<br><sub>6,6,4,12,32</sub> | 4.2<br><sub>0,5,0,7,9</sub> | 5.5 · –<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>1,0,1,0,3</sub> |  | 1.1<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,1</sub> |  | 0.8 | 0.3 | 0.6 | 7.9 |
| Jahmai Mashack | 63% | 13.5<br><sub>2,13,26,22,-</sub> | 3.4<br><sub>0,3,0,0,-</sub> |  | 1.7<br><sub>0,2,3,2,-</sub> |  | 1.7<br><sub>1,2,4,1,-</sub> |  | 0.2<br><sub>0,1,0,0,-</sub> |  | 0.6 | 0.2 | 0.8 | 6.7 |
| Quinten Post | 80% | 8.9<br><sub>9,6,10,-,3</sub> | 3.3<br><sub>5,3,5,-,0</sub> |  | 1.7<br><sub>3,2,1,-,0</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,1,0,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.4 |
| Karim Lopez | 48% | 6.7<br><sub>1,-,4,-,-</sub> | 2.2<br><sub>0,-,3,-,-</sub> |  | 1.3<br><sub>0,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,1,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 3.8 |

</details>


### BKN @ MIL
Out: Chaney Johnson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Nolan Traore (BKN)

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 99% | 34.0<br><sub>31,34,27,39,35</sub> | 20.9<br><sub>22,33,17,27,29</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>4,6,0,9,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>5,1,4,6,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>3,2,3,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.2 | 3.3 | 32.2 |
| Michael Porter Jr. | 88% | 33.8<br><sub>-,40,27,34,31</sub> | 20.5<br><sub>-,25,5,16,11</sub> | 21.5 · –<br><sub>o 46% · u 53%</sub> | 6.7<br><sub>-,6,3,4,6</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>-,2,1,5,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.9<br><sub>-,2,1,3,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.4 | 2.2 | 29.8 |
| Egor Demin | 98% | 26.3<br><sub>27,26,31,21,25</sub> | 11.5<br><sub>11,9,22,6,10</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>1,3,4,3,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>2,4,4,2,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>3,2,3,0,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 1.7 | 18.1 |
| Mikel Brown Jr. | 98% | 26.0<br><sub>20,18,27,24,29</sub> | 13.3<br><sub>6,3,15,18,17</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>1,1,1,1,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>2,5,4,0,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>2,1,2,3,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 2.2 | 20.0 |
| Day'Ron Sharpe | 99% | 25.4<br><sub>28,25,22,26,26</sub> | 10.6<br><sub>16,6,6,17,6</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 8.5<br><sub>11,9,5,11,5</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>5,5,1,2,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 23.4 |
| Noah Clowney | 99% | 23.9<br><sub>35,24,19,22,26</sub> | 8.9<br><sub>15,9,7,0,13</sub> | 6.5 · –<br><sub>o 55% · u 45%</sub> | 4.0<br><sub>7,3,3,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,3,1,2,1</sub> |  | 1.4<br><sub>3,1,1,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.6 | 1.0 | 14.4 |
| Danny Wolf | 91% | 23.3<br><sub>28,11,23,26,25</sub> | 10.0<br><sub>14,3,6,20,11</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>6,2,6,5,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>1,1,2,2,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>4,1,1,4,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.6 | 1.2 | 17.9 |
| Moritz Wagner | 98% | 17.6<br><sub>18,10,20,22,14</sub> | 9.0<br><sub>10,4,11,3,11</sub> |  | 4.0<br><sub>6,5,2,5,0</sub> |  | 1.5<br><sub>4,1,3,2,1</sub> |  | 0.8<br><sub>2,0,2,1,2</sub> |  | 0.7 | 0.2 | 1.0 | 14.6 |
| Keon Ellis | 91% | 17.4<br><sub>7,20,6,8,16</sub> | 4.3<br><sub>0,8,3,0,6</sub> |  | 1.7<br><sub>0,2,1,1,0</sub> |  | 1.2<br><sub>1,0,0,1,0</sub> |  | 0.6<br><sub>0,2,1,0,2</sub> |  | 0.9 | 0.5 | 0.5 | 7.2 |
| Terance Mann | 64% | 13.3<br><sub>9,-,5,-,3</sub> | 3.2<br><sub>2,-,0,-,0</sub> |  | 1.6<br><sub>1,-,1,-,0</sub> |  | 1.3<br><sub>1,-,0,-,0</sub> |  | 0.3<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.1 |
| Grant Nelson | 84% | 9.3<br><sub>-,-,-,-,8</sub> | 2.9<br><sub>-,-,-,-,2</sub> |  | 2.2<br><sub>-,-,-,-,1</sub> |  | 0.9<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.7 | 0.6 | 6.0 |
| Josh Minott | 63% | 9.2<br><sub>2,-,4,-,2</sub> | 4.7<br><sub>0,-,0,-,0</sub> |  | 1.7<br><sub>0,-,0,-,0</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 6.9 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 99% | 29.5<br><sub>20,24,31,40,37</sub> | 20.1<br><sub>5,8,19,50,32</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>5,2,4,11,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>3,4,3,7,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>0,0,4,7,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.3 | 2.3 | 29.3 |
| Kyle Kuzma | 99% | 24.4<br><sub>22,30,-,33,32</sub> | 13.2<br><sub>14,26,-,12,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>6,5,-,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>2,1,-,1,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>3,2,-,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.4 | 1.5 | 20.1 |
| Myles Turner | 99% | 23.1<br><sub>23,21,-,26,28</sub> | 10.1<br><sub>8,4,-,5,27</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>7,5,-,6,11</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,4,-,5,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>1,0,-,1,5</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 2.0 | 1.3 | 17.1 |
| Jaime Jaquez Jr. | 99% | 22.7<br><sub>30,23,22,25,25</sub> | 12.1<br><sub>6,10,9,9,3</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>5,2,1,0,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>4,5,2,1,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 1.5 | 19.2 |
| Brayden Burries | 99% | 21.8<br><sub>29,25,28,26,29</sub> | 10.9<br><sub>13,20,14,26,14</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>8,7,3,8,10</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,1,3,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>2,3,2,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 1.5 | 18.6 |
| Ryan Rollins | 99% | 21.2<br><sub>-,-,21,28,22</sub> | 10.9<br><sub>-,-,15,8,6</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>-,-,3,6,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>-,-,6,1,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>-,-,1,0,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.3 | 1.9 | 18.3 |
| Kel'el Ware | 98% | 16.7<br><sub>25,17,26,22,23</sub> | 7.6<br><sub>8,11,11,6,9</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>11,3,5,8,3</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>2,1,0,3,0</sub> |  | 0.5<br><sub>1,1,2,0,1</sub> |  | 0.6 | 1.1 | 1.2 | 13.6 |
| Nate Ament | 98% | 16.3<br><sub>17,17,35,14,25</sub> | 7.1<br><sub>5,7,18,2,7</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>2,4,9,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.6<br><sub>1,0,2,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 10.5 |
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
Out: Mark Williams (PHX)

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 99% | 36.0<br><sub>28,37,33,38,42</sub> | 25.2<br><sub>17,20,29,23,22</sub> | 23.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,4,2,2,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.9<br><sub>7,8,6,3,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>0,1,2,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.3 | 2.9 | 34.4 |
| Dillon Brooks | 99% | 30.2<br><sub>22,27,31,25,34</sub> | 15.8<br><sub>1,15,29,18,16</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>2,4,3,3,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>0,4,5,3,7</sub> |  | 1.9<br><sub>0,3,5,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 1.4 | 21.6 |
| Miles Bridges | 99% | 29.5<br><sub>24,29,29,25,35</sub> | 13.6<br><sub>14,16,13,18,14</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>3,8,6,9,11</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,2,5,4,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.5 | 1.1 | 22.7 |
| Jalen Green | 98% | 29.0<br><sub>21,27,30,25,37</sub> | 15.8<br><sub>9,16,18,14,25</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>2,5,7,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>1,3,7,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,2,4,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 2.3 | 22.3 |
| Oso Ighodaro | 98% | 25.1<br><sub>17,33,21,27,30</sub> | 6.2<br><sub>4,8,7,3,7</sub> | 5.5 · –<br><sub>o 54% · u 46%</sub> | 5.6<br><sub>2,11,4,7,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,3,2,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.3 | 14.5 |
| Collin Gillespie | 99% | 25.0<br><sub>28,26,17,27,30</sub> | 10.1<br><sub>26,10,9,16,18</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>4,3,3,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,3,1,5,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>5,2,2,3,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 1.2 | 16.6 |
| Jordan Goodwin | 98% | 19.3<br><sub>31,20,17,28,18</sub> | 7.0<br><sub>14,11,2,5,6</sub> |  | 3.9<br><sub>7,6,5,9,2</sub> |  | 1.9<br><sub>6,2,3,4,2</sub> |  | 1.0<br><sub>1,1,0,1,2</sub> |  | 1.2 | 0.2 | 0.7 | 12.8 |
| Khaman Maluach | 98% | 16.0<br><sub>13,11,21,18,16</sub> | 5.7<br><sub>7,4,10,9,8</sub> | 6.5 · –<br><sub>o 43% · u 57%</sub> | 4.7<br><sub>4,6,2,6,6</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.9 | 0.9 | 11.1 |
| Luke Kennard | 99% | 15.8<br><sub>23,17,17,15,14</sub> | 5.9<br><sub>18,12,3,5,4</sub> |  | 1.7<br><sub>6,2,3,0,1</sub> |  | 1.3<br><sub>4,0,1,0,2</sub> |  | 0.8<br><sub>3,4,1,1,0</sub> |  | 0.5 | 0.1 | 0.5 | 8.9 |
| Ryan Dunn | 98% | 12.9<br><sub>24,12,13,9,9</sub> | 3.7<br><sub>3,5,6,0,3</sub> |  | 2.8<br><sub>6,1,5,5,2</sub> |  | 0.8<br><sub>1,0,2,0,0</sub> |  | 0.3<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.4 | 7.3 |
| Rasheer Fleming | 38% | 7.0<br><sub>-,-,4,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 1.2<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.0 |
| Pat Spencer | 48% | 6.7<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.4 |
| Jamaree Bouyea | 47% | 6.4<br><sub>-,-,4,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Koa Peat | 64% | 6.2<br><sub>8,1,4,3,-</sub> | 3.1<br><sub>10,0,2,0,-</sub> |  | 1.3<br><sub>2,1,0,0,-</sub> |  | 0.3<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.7 |
| Duop Reath | 38% | 6.0<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.2 | 3.9 |
| Drew Timme | 5% | 6.0 | 2.3 |  | 1.1 |  | 0.7 |  | 0.1 |  | 0.2 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 99% | 35.8<br><sub>30,29,32,35,33</sub> | 22.7<br><sub>25,22,21,16,32</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>4,2,2,4,9</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>5,3,3,4,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>2,2,4,0,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.9 | 3.1 | 33.2 |
| Amen Thompson | 88% | 34.5<br><sub>29,-,31,26,28</sub> | 17.5<br><sub>26,-,15,22,20</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>7,-,9,6,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>7,-,3,0,5</sub> | 2.5<br><sub>o 62% · u 38%</sub> | 0.3<br><sub>3,-,0,0,1</sub> |  | 1.4 | 0.7 | 2.2 | 29.1 |
| Alperen Sengun | 96% | 34.4<br><sub>28,30,14,36,31</sub> | 21.3<br><sub>19,23,7,28,20</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 9.9<br><sub>8,7,7,11,8</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 6.6<br><sub>8,2,1,10,7</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 0.7<br><sub>1,1,1,1,1</sub> |  | 1.2 | 1.0 | 3.0 | 37.9 |
| Jabari Smith Jr. | 99% | 34.0<br><sub>28,32,26,32,28</sub> | 14.8<br><sub>9,12,17,21,13</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 6.6<br><sub>6,10,4,4,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>5,1,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>1,1,3,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.8 | 1.3 | 23.4 |
| Fred VanVleet | 88% | 32.3<br><sub>-,26,27,33,31</sub> | 14.4<br><sub>-,8,15,25,6</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>-,5,2,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>-,6,6,9,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.5<br><sub>-,2,3,3,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.4 | 1.5 | 22.9 |
| Tari Eason | 99% | 24.1<br><sub>30,27,25,23,22</sub> | 9.8<br><sub>25,7,11,7,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>7,7,4,6,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>1,3,3,1,4</sub> |  | 1.1<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.6 | 1.2 | 16.9 |
| Marcus Smart | 67% | 21.4<br><sub>-,-,18,23,25</sub> | 6.8<br><sub>-,-,4,3,4</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>-,-,2,2,3</sub> |  | 2.3<br><sub>-,-,4,2,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0<br><sub>-,-,1,1,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.1 | 0.4 | 1.4 | 11.4 |
| Reed Sheppard | 96% | 18.8<br><sub>26,19,25,14,17</sub> | 8.5<br><sub>11,5,20,0,5</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>1,2,4,2,3</sub> |  | 2.5<br><sub>6,2,2,0,5</sub> |  | 1.4<br><sub>3,1,6,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.4 | 0.9 | 12.7 |
| Steven Adams | 63% | 14.3<br><sub>12,-,16,12,16</sub> | 4.0<br><sub>6,-,4,2,4</sub> |  | 5.3<br><sub>7,-,5,2,6</sub> |  | 0.9<br><sub>1,-,2,2,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 10.2 |
| Bogdan Bogdanovic | 98% | 11.0<br><sub>22,26,11,5,9</sub> | 4.0<br><sub>12,6,1,0,2</sub> |  | 1.3<br><sub>3,0,3,1,1</sub> |  | 1.1<br><sub>4,1,0,0,2</sub> |  | 0.5<br><sub>2,2,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.3 |
| Clint Capela | 35% | 10.0<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 3.9<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.6 | 0.5 | 7.7 |
| Oscar Tshiebwe | 72% | 7.8<br><sub>12,6,11,-,-</sub> | 3.4<br><sub>4,6,4,-,-</sub> |  | 3.5<br><sub>9,6,4,-,-</sub> |  | 0.5<br><sub>3,0,3,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 7.4 |
| Isaiah Crawford | 52% | 6.5<br><sub>9,21,2,-,-</sub> | 2.2<br><sub>4,11,0,-,-</sub> |  | 1.3<br><sub>2,10,0,-,-</sub> |  | 0.3<br><sub>0,3,0,-,-</sub> |  | 0.1<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.9 |
| Jae'Sean Tate | 52% | 6.0<br><sub>8,12,1,-,-</sub> | 1.9<br><sub>4,3,0,-,-</sub> |  | 1.4<br><sub>2,3,0,-,-</sub> |  | 0.4<br><sub>0,2,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.6 |
| Bruce Thornton | 63% | 5.8<br><sub>6,12,1,-,-</sub> | 2.5<br><sub>2,7,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.3 |

</details>


### SAC @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.7–113.6 | SAC 31% | 3.21 / 1.45 | GSW -6.5 | 220.5 | GSW -6.5 covers 51%; o217.5 56% |
| Expected (weighted by chance each plays) | 106.8–115.4 | SAC 27% | 3.71 / 1.37 | GSW -8.5 | 222.5 | GSW -6.5 covers 56%; o217.5 60% |
| if Yaxel Lendeborg plays | 106.3–115.4 | SAC 26% | 3.91 / 1.34 | GSW -9.5 | 221.5 | GSW -6.5 covers 57%; o217.5 59% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | Questionable | 55% | 32.4 | 20.6 | 7.2 | 4.2 | 1.8 | 1.0 | 0.8 | 3.0 | 32.1 | full tables below |
| Brandon Williams (GSW) | Questionable | 55% | 18.0 | 12.1 | 2.3 | 3.1 | 0.6 | 0.8 | 0.3 | 1.5 | 17.5 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 36.0<br><sub>33,35,36,40,33</sub> | 22.9<br><sub>26,36,18,21,12</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>0,4,1,6,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 7.5<br><sub>6,6,12,8,4</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>3,6,2,2,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.3 | 3.8 | 33.8 |
| De'Andre Hunter | 88% | 33.5<br><sub>-,35,37,41,38</sub> | 15.0<br><sub>-,7,30,20,15</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>-,1,6,6,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>-,4,2,2,8</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>-,1,5,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.8 | 22.0 |
| Keegan Murray | 98% | 33.2<br><sub>21,31,40,40,39</sub> | 12.5<br><sub>6,12,13,15,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>1,7,7,12,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>0,3,4,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.9 | 1.3 | 19.8 |
| Zach LaVine | 88% | 31.6<br><sub>-,32,39,30,30</sub> | 17.3<br><sub>-,18,19,13,18</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>-,5,7,3,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>-,2,4,0,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>-,2,2,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 2.2 | 23.4 |
| Domantas Sabonis | 99% | 31.3<br><sub>29,24,38,32,30</sub> | 14.5<br><sub>11,8,19,15,20</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 11.8<br><sub>13,13,16,17,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>3,8,1,4,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.8 | 0.3 | 2.8 | 31.8 |
| Precious Achiuwa | 98% | 17.5<br><sub>-,8,-,22,10</sub> | 7.1<br><sub>-,0,-,5,9</sub> |  | 4.6<br><sub>-,0,-,7,3</sub> |  | 1.0<br><sub>-,0,-,1,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.7 | 0.6 | 0.9 | 12.6 |
| Malik Monk | 98% | 15.6<br><sub>29,20,12,10,16</sub> | 7.9<br><sub>14,8,2,3,15</sub> |  | 1.5<br><sub>1,1,0,0,3</sub> |  | 3.0<br><sub>10,2,3,1,4</sub> |  | 1.0<br><sub>1,2,0,0,4</sub> |  | 0.5 | 0.3 | 1.3 | 12.4 |
| Leaky Black | 91% | 14.5<br><sub>29,17,19,4,13</sub> | 3.4<br><sub>12,3,0,2,3</sub> |  | 2.3<br><sub>9,0,3,0,3</sub> |  | 1.0<br><sub>2,2,1,0,3</sub> |  | 0.4<br><sub>4,1,0,0,1</sub> |  | 0.8 | 0.3 | 0.4 | 6.8 |
| Emanuel Sharp | 98% | 14.0<br><sub>21,14,10,16,13</sub> | 4.4<br><sub>9,6,3,3,0</sub> |  | 1.1<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>2,1,1,0,2</sub> |  | 0.6<br><sub>1,1,1,1,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.3 |
| Dylan Cardwell | 98% | 13.3<br><sub>19,12,10,6,11</sub> | 3.7<br><sub>10,6,0,0,0</sub> |  | 4.8<br><sub>6,4,4,1,7</sub> |  | 1.0<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.7 | 9.4 |
| Sean Pedulla | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Daeqwon Plowden | 64% | 8.4<br><sub>24,4,-,-,1</sub> | 3.2<br><sub>13,3,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,0</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>3,1,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.6 |
| Gabe Vincent | 96% | 8.2<br><sub>-,-,-,-,3</sub> | 2.8<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Alex Karaban | 52% | 7.8<br><sub>29,4,-,-,1</sub> | 1.4<br><sub>0,0,-,-,0</sub> |  | 1.2<br><sub>5,1,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 2.9 |
| Mason Plumlee | 38% | 6.6<br><sub>5,4,-,-,-</sub> | 1.9<br><sub>2,0,-,-,-</sub> |  | 2.2<br><sub>0,2,-,-,-</sub> |  | 0.7<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 98% | 34.0<br><sub>22,30,29,32,38</sub> | 20.4<br><sub>8,15,10,15,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 5.1<br><sub>0,3,4,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.3 | 2.2 | 30.8 |
| Draymond Green | 97% | 27.8<br><sub>16,25,23,-,27</sub> | 7.0<br><sub>4,2,3,-,9</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.4<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>3,5,2,-,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 0.8<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.7 | 2.6 | 18.6 |
| De'Anthony Melton | 99% | 27.0<br><sub>18,21,19,25,27</sub> | 14.2<br><sub>8,8,0,9,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,2,2,1,3</sub> |  | 4.1<br><sub>3,1,2,5,7</sub> |  | 2.2<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.6 | 0.5 | 1.9 | 22.3 |
| Will Richard | 99% | 25.5<br><sub>30,23,27,27,17</sub> | 10.2<br><sub>7,11,20,15,3</sub> |  | 3.0<br><sub>4,3,0,5,2</sub> |  | 1.9<br><sub>1,1,3,0,2</sub> |  | 1.3<br><sub>1,2,1,1,1</sub> |  | 1.3 | 0.2 | 1.1 | 15.1 |
| Charles Bassey | 98% | 24.3<br><sub>20,16,22,25,26</sub> | 12.8<br><sub>11,4,10,16,13</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>5,0,8,13,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.5 | 1.5 | 23.7 |
| Gui Santos | 96% | 24.3<br><sub>21,19,17,23,23</sub> | 11.7<br><sub>7,12,6,8,13</sub> |  | 4.9<br><sub>4,7,6,3,5</sub> |  | 3.3<br><sub>1,2,6,0,3</sub> |  | 1.1<br><sub>1,1,0,0,3</sub> |  | 0.9 | 0.3 | 1.8 | 19.9 |
| Georges Niang | 98% | 21.0<br><sub>15,14,14,15,8</sub> | 9.7<br><sub>5,0,11,5,0</sub> |  | 3.0<br><sub>3,4,1,2,1</sub> |  | 1.6<br><sub>2,2,1,0,0</sub> |  | 1.5<br><sub>1,0,2,1,0</sub> |  | 0.4 | 0.2 | 1.1 | 14.3 |
| Al Horford | 98% | 20.3<br><sub>10,14,-,17,18</sub> | 7.8<br><sub>0,0,-,3,7</sub> |  | 4.5<br><sub>3,5,-,2,3</sub> |  | 2.4<br><sub>1,0,-,2,2</sub> |  | 1.1<br><sub>0,0,-,0,1</sub> |  | 0.6 | 1.0 | 0.7 | 14.7 |
| Gary Payton II | 91% | 18.4<br><sub>13,8,16,24,13</sub> | 8.6<br><sub>2,2,8,2,8</sub> |  | 3.4<br><sub>2,0,8,1,1</sub> |  | 1.5<br><sub>0,0,2,1,0</sub> |  | 0.6<br><sub>0,0,2,0,0</sub> |  | 1.2 | 0.2 | 0.8 | 13.5 |
| LJ Cryer | 88% | 17.4<br><sub>24,24,19,12,11</sub> | 9.1<br><sub>20,7,9,9,3</sub> |  | 1.4<br><sub>2,1,0,0,0</sub> |  | 2.1<br><sub>6,3,2,1,2</sub> |  | 1.6<br><sub>6,1,3,1,1</sub> |  | 0.4 | 0.1 | 0.8 | 12.7 |
| Graham Ike | 72% | 13.4<br><sub>13,8,15,4,-</sub> | 6.2<br><sub>5,3,2,5,-</sub> |  | 3.2<br><sub>2,5,2,0,-</sub> |  | 1.6<br><sub>3,1,2,0,-</sub> |  | 0.4<br><sub>1,0,0,0,-</sub> |  | 0.5 | 0.6 | 0.8 | 10.9 |
| Malevy Leons | 64% | 11.4<br><sub>14,6,7,4,-</sub> | 3.5<br><sub>5,2,2,0,-</sub> |  | 2.1<br><sub>1,1,1,2,-</sub> |  | 0.8<br><sub>0,0,0,1,-</sub> |  | 0.1<br><sub>1,0,0,0,-</sub> |  | 0.5 | 0.4 | 0.6 | 6.4 |

</details>

<details><summary>if Yaxel Lendeborg plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 98% | 33.5<br><sub>22,30,29,32,38</sub> | 18.6<br><sub>8,15,10,15,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.6<br><sub>0,3,4,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.3 | 1.9 | 28.4 |
| Yaxel Lendeborg (GSW) | 100% | 32.4<br><sub>24,33,30,33,34</sub> | 20.6<br><sub>3,28,13,11,12</sub> | 22.5 · – | 7.2<br><sub>7,8,5,8,8</sub> | 7.5 | 4.2<br><sub>1,3,4,7,3</sub> | 3.5 | 1.8<br><sub>0,2,0,1,1</sub> | 1.5 | 1.0 | 0.8 | 3.0 | 32.1 |
| Draymond Green (GSW) | 97% | 26.5<br><sub>16,25,23,-,27</sub> | 6.5<br><sub>4,2,3,-,9</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>3,5,2,-,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 0.8<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.7 | 2.3 | 17.8 |
| De'Anthony Melton (GSW) | 99% | 24.9<br><sub>18,21,19,25,27</sub> | 11.6<br><sub>8,8,0,9,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,2,2,1,3</sub> |  | 3.5<br><sub>3,1,2,5,7</sub> |  | 1.9<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.5 | 0.4 | 1.8 | 18.8 |
| Will Richard (GSW) | 99% | 21.6<br><sub>30,23,27,27,17</sub> | 8.1<br><sub>7,11,20,15,3</sub> |  | 2.5<br><sub>4,3,0,5,2</sub> |  | 1.5<br><sub>1,1,3,0,2</sub> |  | 1.0<br><sub>1,2,1,1,1</sub> |  | 1.1 | 0.2 | 0.9 | 12.1 |
| Charles Bassey (GSW) | 98% | 20.1<br><sub>20,16,22,25,26</sub> | 10.3<br><sub>11,4,10,16,13</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.9<br><sub>5,0,8,13,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.3 | 1.2 | 19.2 |
| Gui Santos (GSW) | 96% | 19.8<br><sub>21,19,17,23,23</sub> | 9.2<br><sub>7,12,6,8,13</sub> |  | 3.9<br><sub>4,7,6,3,5</sub> |  | 2.3<br><sub>1,2,6,0,3</sub> |  | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.7 | 0.3 | 1.3 | 15.5 |
| Al Horford (GSW) | 98% | 17.7<br><sub>10,14,-,17,18</sub> | 6.3<br><sub>0,0,-,3,7</sub> |  | 3.8<br><sub>3,5,-,2,3</sub> |  | 1.9<br><sub>1,0,-,2,2</sub> |  | 0.9<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.8 | 0.6 | 12.0 |
| Gary Payton II (GSW) | 91% | 16.2<br><sub>13,8,16,24,13</sub> | 7.6<br><sub>2,2,8,2,8</sub> |  | 2.8<br><sub>2,0,8,1,1</sub> |  | 1.4<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>0,0,2,0,0</sub> |  | 1.0 | 0.2 | 0.7 | 11.8 |
| Georges Niang (GSW) | 98% | 16.0<br><sub>15,14,14,15,8</sub> | 7.3<br><sub>5,0,11,5,0</sub> |  | 2.3<br><sub>3,4,1,2,1</sub> |  | 1.1<br><sub>2,2,1,0,0</sub> |  | 1.1<br><sub>1,0,2,1,0</sub> |  | 0.3 | 0.1 | 0.8 | 10.7 |
| LJ Cryer (GSW) | 88% | 14.2<br><sub>24,24,19,12,11</sub> | 7.1<br><sub>20,7,9,9,3</sub> |  | 1.1<br><sub>2,1,0,0,0</sub> |  | 1.8<br><sub>6,3,2,1,2</sub> |  | 1.2<br><sub>6,1,3,1,1</sub> |  | 0.3 | 0.1 | 0.6 | 10.0 |
| Graham Ike (GSW) | 72% | 8.9<br><sub>13,8,15,4,-</sub> | 4.1<br><sub>5,3,2,5,-</sub> |  | 2.1<br><sub>2,5,2,0,-</sub> |  | 1.1<br><sub>3,1,2,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.4 | 0.5 | 7.3 |
| Malevy Leons (GSW) | 64% | 7.5<br><sub>14,6,7,4,-</sub> | 2.3<br><sub>5,2,2,0,-</sub> |  | 1.4<br><sub>1,1,1,2,-</sub> |  | 0.5<br><sub>0,0,0,1,-</sub> |  | 0.1<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.1 |
| Darius Acuff Jr. (SAC) | 98% | 36.0<br><sub>33,35,36,40,33</sub> | 22.9<br><sub>26,36,18,21,12</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>0,4,1,6,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 7.5<br><sub>6,6,12,8,4</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>3,6,2,2,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.3 | 3.8 | 33.8 |
| De'Andre Hunter (SAC) | 88% | 33.4<br><sub>-,35,37,41,38</sub> | 15.0<br><sub>-,7,30,20,15</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>-,1,6,6,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>-,4,2,2,8</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>-,1,5,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.8 | 21.9 |
| Keegan Murray (SAC) | 98% | 33.2<br><sub>21,31,40,40,39</sub> | 12.4<br><sub>6,12,13,15,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>1,7,7,12,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>0,3,4,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.9 | 1.3 | 19.7 |
| Zach LaVine (SAC) | 88% | 31.7<br><sub>-,32,39,30,30</sub> | 17.4<br><sub>-,18,19,13,18</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>-,5,7,3,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>-,2,4,0,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>-,2,2,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 2.2 | 23.5 |
| Domantas Sabonis (SAC) | 99% | 31.4<br><sub>29,24,38,32,30</sub> | 14.4<br><sub>11,8,19,15,20</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 11.8<br><sub>13,13,16,17,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>3,8,1,4,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.8 | 0.3 | 2.8 | 31.8 |
| Precious Achiuwa (SAC) | 98% | 17.5<br><sub>-,8,-,22,10</sub> | 7.1<br><sub>-,0,-,5,9</sub> |  | 4.6<br><sub>-,0,-,7,3</sub> |  | 1.0<br><sub>-,0,-,1,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.7 | 0.6 | 0.9 | 12.6 |
| Malik Monk (SAC) | 98% | 15.6<br><sub>29,20,12,10,16</sub> | 7.8<br><sub>14,8,2,3,15</sub> |  | 1.5<br><sub>1,1,0,0,3</sub> |  | 3.0<br><sub>10,2,3,1,4</sub> |  | 1.0<br><sub>1,2,0,0,4</sub> |  | 0.5 | 0.3 | 1.3 | 12.3 |
| Leaky Black (SAC) | 91% | 14.5<br><sub>29,17,19,4,13</sub> | 3.4<br><sub>12,3,0,2,3</sub> |  | 2.3<br><sub>9,0,3,0,3</sub> |  | 1.0<br><sub>2,2,1,0,3</sub> |  | 0.4<br><sub>4,1,0,0,1</sub> |  | 0.8 | 0.3 | 0.4 | 6.7 |
| Emanuel Sharp (SAC) | 98% | 14.0<br><sub>21,14,10,16,13</sub> | 4.5<br><sub>9,6,3,3,0</sub> |  | 1.1<br><sub>0,2,0,0,1</sub> |  | 0.8<br><sub>2,1,1,0,2</sub> |  | 0.6<br><sub>1,1,1,1,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.3 |
| Dylan Cardwell (SAC) | 98% | 13.3<br><sub>19,12,10,6,11</sub> | 3.7<br><sub>10,6,0,0,0</sub> |  | 4.8<br><sub>6,4,4,1,7</sub> |  | 1.0<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.7 | 9.4 |
| Sean Pedulla (SAC) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Daeqwon Plowden (SAC) | 64% | 8.4<br><sub>24,4,-,-,1</sub> | 3.2<br><sub>13,3,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,0</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>3,1,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.6 |
| Gabe Vincent (SAC) | 96% | 8.2<br><sub>-,-,-,-,3</sub> | 2.8<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Alex Karaban (SAC) | 52% | 7.9<br><sub>29,4,-,-,1</sub> | 1.4<br><sub>0,0,-,-,0</sub> |  | 1.3<br><sub>5,1,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.0 |
| Mason Plumlee (SAC) | 38% | 6.7<br><sub>5,4,-,-,-</sub> | 1.9<br><sub>2,0,-,-,-</sub> |  | 2.2<br><sub>0,2,-,-,-</sub> |  | 0.7<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.8 |

</details>


### SAS @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), Dylan Harper (SAS), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.0–113.2 | SAS 43% | 2.30 / 1.77 | POR -2.5 | 223.5 | POR +2.5 covers 62%; o225.5 47% |
| Expected (weighted by chance each plays) | 112.9–111.6 | SAS 54% | 1.85 / 2.17 | POR +1.5 | 224.5 | POR +2.5 covers 52%; o225.5 48% |
| if De'Aaron Fox plays | 111.9–111.9 | SAS 50% | 1.98 / 2.02 | POR +0.5 | 223.5 | POR +2.5 covers 56%; o225.5 46% |
| if Victor Wembanyama plays | 113.0–111.4 | SAS 55% | 1.81 / 2.23 | POR +2.5 | 224.5 | POR +2.5 covers 51%; o225.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 31.7 | 16.5 | 3.9 | 5.8 | 1.3 | 1.4 | 0.4 | 2.9 | 26.2 | full tables below |
| Victor Wembanyama (SAS) | Questionable | 55% | 32.6 | 30.6 | 12.0 | 3.9 | 2.2 | 1.4 | 3.7 | 3.0 | 46.5 | full tables below |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephon Castle | 99% | 33.8<br><sub>35,31,33,29,37</sub> | 22.0<br><sub>20,10,21,19,28</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.3 | 3.9 | 34.9 |
| Devin Vassell | 99% | 33.5<br><sub>32,36,32,26,34</sub> | 17.2<br><sub>6,12,15,10,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>6,5,4,3,6</sub> |  | 3.3<br><sub>1,4,4,2,2</sub> |  | 2.1<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.5 | 1.5 | 25.1 |
| Julian Champagnie | 99% | 31.4<br><sub>24,30,29,25,30</sub> | 13.8<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>5,6,4,3,7</sub> |  | 2.0<br><sub>1,0,1,3,3</sub> |  | 2.4<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.6 | 1.2 | 21.2 |
| Keldon Johnson | 99% | 28.6<br><sub>29,15,27,23,26</sub> | 15.2<br><sub>11,4,10,10,12</sub> |  | 6.2<br><sub>10,2,5,4,4</sub> |  | 3.0<br><sub>2,1,3,4,5</sub> |  | 1.1<br><sub>1,0,0,2,0</sub> |  | 1.0 | 0.2 | 1.5 | 24.4 |
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
| Deni Avdija | 72% | 34.3<br><sub>30,-,-,36,30</sub> | 23.9<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 6.2<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.5 | 3.2 | 36.8 |
| Damian Lillard | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.3<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 2.1 | 28.7 |
| Toumani Camara | 99% | 32.8<br><sub>26,33,37,35,29</sub> | 11.9<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 1.1 | 18.4 |
| Jrue Holiday | 99% | 29.7<br><sub>25,31,31,31,28</sub> | 14.7<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 2.1 | 23.7 |
| Donovan Clingan | 99% | 28.7<br><sub>22,32,26,31,29</sub> | 12.6<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 11.9<br><sub>10,12,13,13,18</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.6 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson | 99% | 25.3<br><sub>23,21,35,23,26</sub> | 12.0<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> |  | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 1.9 | 16.8 |
| Sidy Cissoko | 98% | 24.8<br><sub>28,32,31,23,24</sub> | 7.3<br><sub>5,6,13,11,5</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,1,3,1,0</sub> |  | 1.0<br><sub>1,2,1,3,1</sub> |  | 0.8 | 0.3 | 0.9 | 12.4 |
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
| Deni Avdija (POR) | 72% | 34.3<br><sub>30,-,-,36,30</sub> | 23.8<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 6.3<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.5 | 3.2 | 36.7 |
| Damian Lillard (POR) | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.2<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 2.2 | 28.6 |
| Toumani Camara (POR) | 99% | 32.8<br><sub>26,33,37,35,29</sub> | 11.8<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 1.1 | 18.3 |
| Jrue Holiday (POR) | 99% | 29.8<br><sub>25,31,31,31,28</sub> | 14.6<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 2.1 | 23.6 |
| Donovan Clingan (POR) | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.5<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 12.0<br><sub>10,12,13,13,18</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.7 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson (POR) | 99% | 25.4<br><sub>23,21,35,23,26</sub> | 12.0<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> |  | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 1.9 | 16.9 |
| Sidy Cissoko (POR) | 98% | 25.0<br><sub>28,32,31,23,24</sub> | 7.3<br><sub>5,6,13,11,5</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,1,3,1,0</sub> |  | 1.0<br><sub>1,2,1,3,1</sub> |  | 0.8 | 0.3 | 0.9 | 12.5 |
| Robert Williams III (POR) | 98% | 17.0<br><sub>15,16,-,17,16</sub> | 6.3<br><sub>2,6,-,4,6</sub> |  | 6.5<br><sub>5,8,-,3,6</sub> |  | 1.1<br><sub>2,4,-,0,1</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 13.9 |
| Jayson Kent (POR) | 88% | 12.1<br><sub>11,27,17,3,14</sub> | 4.0<br><sub>8,8,2,0,9</sub> |  | 1.4<br><sub>0,3,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>2,2,0,0,3</sub> |  | 0.5 | 0.1 | 0.5 | 6.0 |
| Branden Carlson (POR) | 91% | 8.7<br><sub>14,14,10,9,6</sub> | 2.5<br><sub>5,6,0,2,0</sub> |  | 2.2<br><sub>6,1,1,1,3</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Yang Hansen (POR) | 58% | 7.2<br><sub>7,-,12,-,3</sub> | 2.8<br><sub>0,-,2,-,2</sub> |  | 1.8<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>3,-,1,-,1</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.1 |
| Micah Potter (POR) | 58% | 7.0<br><sub>7,1,-,-,3</sub> | 3.1<br><sub>2,0,-,-,0</sub> |  | 2.0<br><sub>4,0,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| John Tonje (POR) | 52% | 6.8<br><sub>7,-,6,-,3</sub> | 2.7<br><sub>7,-,0,-,2</sub> |  | 1.7<br><sub>4,-,3,-,0</sub> |  | 0.7<br><sub>3,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 5.1 |
| Stephon Castle (SAS) | 99% | 33.0<br><sub>35,31,33,29,37</sub> | 20.7<br><sub>20,10,21,19,28</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.3 | 3.4 | 32.6 |
| Devin Vassell (SAS) | 99% | 32.7<br><sub>32,36,32,26,34</sub> | 15.4<br><sub>6,12,15,10,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>6,5,4,3,6</sub> |  | 2.8<br><sub>1,4,4,2,2</sub> |  | 1.9<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.5 | 1.2 | 22.8 |
| De'Aaron Fox (SAS) | 100% | 31.7<br><sub>-,34,32,26,-</sub> | 16.5<br><sub>-,6,10,5,-</sub> | 15.5 · – | 3.9<br><sub>-,2,2,2,-</sub> | 3.5 | 5.8<br><sub>-,2,5,10,-</sub> | 6.5 | 1.3<br><sub>-,0,0,0,-</sub> | 1.5 | 1.4 | 0.4 | 2.9 | 26.2 |
| Julian Champagnie (SAS) | 99% | 30.3<br><sub>24,30,29,25,30</sub> | 12.9<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>5,6,4,3,7</sub> |  | 1.8<br><sub>1,0,1,3,3</sub> |  | 2.2<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.6 | 0.9 | 19.9 |
| Keldon Johnson (SAS) | 99% | 27.0<br><sub>29,15,27,23,26</sub> | 13.2<br><sub>11,4,10,10,12</sub> |  | 5.8<br><sub>10,2,5,4,4</sub> |  | 2.6<br><sub>2,1,3,4,5</sub> |  | 1.0<br><sub>1,0,0,2,0</sub> |  | 0.9 | 0.2 | 1.3 | 21.5 |
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
| Deni Avdija (POR) | 72% | 34.4<br><sub>30,-,-,36,30</sub> | 23.8<br><sub>27,-,-,20,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 6.2<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.5 | 3.2 | 36.8 |
| Damian Lillard (POR) | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.1<br><sub>9,25,33,15,18</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 2.1 | 28.6 |
| Toumani Camara (POR) | 99% | 32.7<br><sub>26,33,37,35,29</sub> | 11.8<br><sub>3,10,18,6,5</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 1.1 | 18.3 |
| Jrue Holiday (POR) | 99% | 29.6<br><sub>25,31,31,31,28</sub> | 14.5<br><sub>10,23,22,13,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 2.1 | 23.4 |
| Donovan Clingan (POR) | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.5<br><sub>10,12,7,22,15</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 12.0<br><sub>10,12,13,13,18</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.7 | 1.7 | 1.1 | 26.9 |
| Scoot Henderson (POR) | 99% | 25.3<br><sub>23,21,35,23,26</sub> | 11.9<br><sub>10,9,27,3,17</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,7,1,3</sub> |  | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.2 | 1.9 | 16.7 |
| Sidy Cissoko (POR) | 98% | 24.9<br><sub>28,32,31,23,24</sub> | 7.4<br><sub>5,6,13,11,5</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.7<br><sub>3,1,3,1,0</sub> |  | 1.0<br><sub>1,2,1,3,1</sub> |  | 0.8 | 0.3 | 0.9 | 12.5 |
| Robert Williams III (POR) | 98% | 17.0<br><sub>15,16,-,17,16</sub> | 6.3<br><sub>2,6,-,4,6</sub> |  | 6.5<br><sub>5,8,-,3,6</sub> |  | 1.1<br><sub>2,4,-,0,1</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 13.9 |
| Jayson Kent (POR) | 88% | 12.1<br><sub>11,27,17,3,14</sub> | 4.0<br><sub>8,8,2,0,9</sub> |  | 1.4<br><sub>0,3,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>2,2,0,0,3</sub> |  | 0.5 | 0.1 | 0.5 | 6.0 |
| Branden Carlson (POR) | 91% | 8.8<br><sub>14,14,10,9,6</sub> | 2.5<br><sub>5,6,0,2,0</sub> |  | 2.2<br><sub>6,1,1,1,3</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Yang Hansen (POR) | 58% | 7.2<br><sub>7,-,12,-,3</sub> | 2.8<br><sub>0,-,2,-,2</sub> |  | 1.8<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>3,-,1,-,1</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.0 |
| Micah Potter (POR) | 58% | 7.1<br><sub>7,1,-,-,3</sub> | 3.1<br><sub>2,0,-,-,0</sub> |  | 2.0<br><sub>4,0,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| John Tonje (POR) | 52% | 6.8<br><sub>7,-,6,-,3</sub> | 2.7<br><sub>7,-,0,-,2</sub> |  | 1.7<br><sub>4,-,3,-,0</sub> |  | 0.7<br><sub>3,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 5.1 |
| Stephon Castle (SAS) | 99% | 33.3<br><sub>35,31,33,29,37</sub> | 19.2<br><sub>20,10,21,19,28</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.3 | 3.3 | 31.3 |
| Devin Vassell (SAS) | 99% | 33.1<br><sub>32,36,32,26,34</sub> | 13.8<br><sub>6,12,15,10,16</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>6,5,4,3,6</sub> |  | 3.0<br><sub>1,4,4,2,2</sub> |  | 1.9<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.5 | 1.1 | 21.2 |
| Victor Wembanyama (SAS) | 100% | 32.6<br><sub>35,34,33,32,-</sub> | 30.6<br><sub>26,25,32,50,-</sub> | 30.5 · – | 12.0<br><sub>10,18,11,19,-</sub> | 12.5 | 3.9<br><sub>6,4,3,1,-</sub> | 3.5 | 2.2<br><sub>4,1,2,5,-</sub> | 2.5 | 1.4 | 3.7 | 3.0 | 46.5 |
| Julian Champagnie (SAS) | 99% | 29.4<br><sub>24,30,29,25,30</sub> | 11.3<br><sub>4,14,20,9,22</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>5,6,4,3,7</sub> |  | 1.8<br><sub>1,0,1,3,3</sub> |  | 2.0<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.6 | 0.8 | 17.9 |
| Keldon Johnson (SAS) | 99% | 25.7<br><sub>29,15,27,23,26</sub> | 11.1<br><sub>11,4,10,10,12</sub> |  | 5.3<br><sub>10,2,5,4,4</sub> |  | 2.5<br><sub>2,1,3,4,5</sub> |  | 0.8<br><sub>1,0,0,2,0</sub> |  | 0.8 | 0.2 | 1.1 | 18.9 |
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
