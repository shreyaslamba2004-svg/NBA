# NBA model · Sun 22 Nov 2026 (US date)

Updated **Mon 23 Nov, 09:30 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-22/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Wiggins PTS over 11.5 (12+) | OKC @ MIA | draftkings | 2.09 | 1.96 | 1.61 | 62.3% | 49.0% | 51.0% | +6.7% | +30.2% | 1.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Wiggins PA over 24.5 (25+) | OKC @ MIA | draftkings | 16.20 | 14.79 | 8.21 | 12.2% | 5.8% | 6.8% | +9.4% | +97.3% | 0.2% |
| Jamal Murray PTS over 39.5 (40+) | DEN @ CHI | draftkings | 18.40 | 16.86 | 9.41 | 10.6% | 5.1% | 5.9% | +9.2% | +95.5% | 0.1% |
| Andrew Wiggins PA over 19.5 (20+) | OKC @ MIA | draftkings | 6.25 | 5.85 | 3.46 | 28.9% | 14.9% | 17.1% | +6.9% | +80.5% | 0.3% |
| Jamal Murray PA over 44.5 (45+) | DEN @ CHI | draftkings | 12.80 | 12.00 | 7.16 | 14.0% | 7.3% | 8.3% | +6.6% | +78.8% | 0.1% |
| Jamal Murray PA over 49.5 (50+) | DEN @ CHI | draftkings | 23.00 | 21.60 | 12.88 | 7.8% | 4.1% | 4.6% | +6.6% | +78.6% | 0.1% |
| Jamal Murray PRA over 54.5 (55+) | DEN @ CHI | draftkings | 22.00 | 20.66 | 12.41 | 8.1% | 4.2% | 4.8% | +6.4% | +77.3% | 0.1% |
| Andrew Wiggins PR over 24.5 (25+) | OKC @ MIA | draftkings | 9.60 | 9.03 | 5.41 | 18.5% | 9.7% | 11.1% | +6.4% | +77.3% | 0.2% |
| Jamal Murray PRA over 49.5 (50+) | DEN @ CHI | draftkings | 12.00 | 11.31 | 6.84 | 14.6% | 7.8% | 8.8% | +6.1% | +75.4% | 0.1% |
| Andrew Wiggins PTS over 19.5 (20+) | OKC @ MIA | draftkings | 9.40 | 8.90 | 5.44 | 18.4% | 9.9% | 11.2% | +5.7% | +72.9% | 0.2% |
| Brice Sensabaugh PTS over 24.5 (25+) | DAL @ UTA | draftkings | 14.00 | 13.28 | 8.19 | 12.2% | 6.7% | 7.5% | +5.4% | +70.9% | 0.1% |
| Andrew Wiggins AST over 3.5 (4+) | OKC @ MIA | draftkings | 8.00 | 7.61 | 4.73 | 21.1% | 11.7% | 13.1% | +5.1% | +69.2% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ MIA | Mon 23 Nov 10:00 | 117.3–118.2 | OKC 48% | 2.09 / 1.92 | MIA -1.5 | 235.5 | MIA -4.5 covers 40%; o226.5 69% |
| ORL @ WAS | Mon 23 Nov 11:00 | 119.5–111.9 | ORL 70% | 1.42 / 3.38 | WAS +7.5 | 231.5 | WAS +4.5 covers 41%; o220.5 72% |
| DEN @ CHI | Mon 23 Nov 11:00 | 123.6–115.8 | DEN 71% | 1.40 / 3.48 | CHI +7.5 | 239.5 | CHI +9.5 covers 55%; o236.5 55% |
| DAL @ UTA | Mon 23 Nov 11:00 | 119.4–117.9 | DAL 54% | 1.84 / 2.19 | UTA +1.5 | 236.5 | UTA +2.5 covers 52%; o225.5 73% |
| IND @ NYK | Mon 23 Nov 12:00 | 105.9–113.6 | IND 29% | 3.43 / 1.41 | NYK -7.5 | 219.5 | NYK -7.5 covers 51%; o213.5 62% |
| BOS @ GSW | Mon 23 Nov 12:30 | 112.2–104.9 | BOS 70% | 1.43 / 3.31 | GSW +7.5 | 216.5 | GSW +8.5 covers 53%; o210.5 64% |

### OKC @ MIA
Out: Giannis Antetokounmpo (MIA), Alex Caruso (OKC), Shai Gilgeous-Alexander (OKC), Chet Holmgren (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Wiggins PTS over 11.5 (12+) | OKC @ MIA | draftkings | 2.09 | 1.96 | 1.61 | 62.3% | 49.0% | 51.0% | +6.7% | +30.2% | 1.5% |
| Bennett Stirtz PTS over 11.5 (12+) | OKC @ MIA | pointsbetau | 2.00 | 1.93 | 1.89 | 52.9% | 51.5% | 51.7% | +3.4% | +5.8% | 0.8% |
| Bam Adebayo PTS under 21.5 | OKC @ MIA | ladbrokes_au | 1.95 | 1.93 | 1.60 | 62.6% | 49.9% | 51.8% | +1.2% | +22.2% | 0.3% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jared McCain | 99% | 33.0<br><sub>31,31,30,33,30</sub> | 21.7<br><sub>10,23,12,18,18</sub> | 19.5 · 19.5<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>6,4,1,3,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>3,2,1,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,7,1,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.2 | 2.1 | 28.5 |
| Ajay Mitchell | 98% | 32.4<br><sub>-,-,27,34,31</sub> | 22.7<br><sub>-,-,14,13,8</sub> | 23.5 · 23.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>-,-,3,6,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>-,-,5,6,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.3 | 2.1 | 32.6 |
| Kenrich Williams | 98% | 29.3<br><sub>26,35,19,23,28</sub> | 12.9<br><sub>11,8,10,10,6</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>2,8,1,5,2</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>2,4,2,1,4</sub> |  | 1.7<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.3 | 1.2 | 21.1 |
| Aday Mara | 98% | 28.5<br><sub>32,21,26,27,29</sub> | 13.7<br><sub>11,10,16,10,22</sub> | 12.5 · 12.5<br><sub>o 49% · u 51%</sub> | 9.4<br><sub>6,3,13,6,16</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>2,0,3,8,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.7 | 2.0 | 25.7 |
| Bennett Stirtz | 98% | 27.6<br><sub>25,12,17,17,25</sub> | 12.7<br><sub>6,5,0,6,18</sub> | 11.5 · 11.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>1,1,1,0,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>1,0,2,2,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,1,0,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 1.0 | 17.1 |
| Isaiah Hartenstein | 99% | 27.0<br><sub>34,30,18,27,28</sub> | 11.1<br><sub>20,21,3,6,5</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 11.7<br><sub>11,16,11,17,8</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>6,6,2,6,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.9 | 27.3 |
| Nique Clifford | 97% | 22.6<br><sub>16,12,24,13,15</sub> | 9.0<br><sub>5,0,9,7,4</sub> |  | 3.4<br><sub>3,0,3,0,5</sub> |  | 2.2<br><sub>1,0,0,0,1</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.3 | 1.1 | 14.6 |
| Micah Peavy | 91% | 20.6<br><sub>12,-,13,-,9</sub> | 7.0<br><sub>0,-,5,-,2</sub> |  | 3.7<br><sub>3,-,3,-,2</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.7 | 0.3 | 0.5 | 11.5 |
| Josh Dix | 58% | 19.3<br><sub>-,17,-,-,-</sub> | 7.7<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,4,-,-,-</sub> |  | 1.4<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Brooks Barnhizer | 48% | 11.2<br><sub>-,-,4,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.2 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 99% | 36.5<br><sub>38,39,32,33,36</sub> | 16.3<br><sub>19,22,15,16,24</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>5,5,4,3,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 8.7<br><sub>8,17,9,10,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>3,3,3,1,6</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.3 | 2.7 | 28.3 |
| Bam Adebayo | 99% | 34.4<br><sub>37,38,36,16,30</sub> | 19.8<br><sub>11,37,20,4,26</sub> | 21.5 · 21.5<br><sub>o 48% · u 52%</sub> | 9.4<br><sub>8,14,5,1,4</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>4,3,4,2,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>0,2,1,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.6 | 1.9 | 32.8 |
| Andrew Wiggins | 98% | 30.9<br><sub>19,32,23,34,26</sub> | 14.1<br><sub>13,8,10,17,11</sub> | 10.5 · 11.5<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>0,3,2,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>0,4,1,1,2</sub> |  | 2.0<br><sub>2,1,0,3,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.9 | 1.5 | 20.7 |
| Pelle Larsson | 83% | 28.0<br><sub>31,-,-,-,15</sub> | 12.0<br><sub>14,-,-,-,4</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>7,-,-,-,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,-,-,-,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>2,-,-,-,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.2 | 1.9 | 19.0 |
| Klay Thompson | 88% | 26.0<br><sub>30,-,20,22,23</sub> | 14.2<br><sub>11,-,26,17,13</sub> | 14.5 · 15.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,-,1,0,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,-,4,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>2,-,6,5,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.6 | 1.1 | 18.1 |
| Ryan Conwell | 91% | 25.0<br><sub>21,33,26,30,26</sub> | 10.5<br><sub>5,20,9,14,13</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>4,5,4,2,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,2,1,3,1</sub> |  | 1.8<br><sub>1,4,2,1,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.0 | 15.2 |
| Bobby Portis | 99% | 22.3<br><sub>17,15,18,23,17</sub> | 10.9<br><sub>5,5,7,16,9</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>1,3,4,6,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>1,2,2,0,0</sub> |  | 1.6<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.3 | 0.9 | 18.5 |
| Myron Gardner | 63% | 18.5<br><sub>10,19,26,24,-</sub> | 6.4<br><sub>4,0,5,14,-</sub> |  | 5.0<br><sub>3,4,9,2,-</sub> |  | 1.9<br><sub>1,2,3,3,-</sub> |  | 0.9<br><sub>0,0,1,4,-</sub> |  | 0.6 | 0.4 | 0.9 | 13.4 |
| Simone Fontecchio | 76% | 17.0<br><sub>7,7,14,19,18</sub> | 8.0<br><sub>3,0,7,10,6</sub> |  | 3.5<br><sub>0,0,5,6,5</sub> |  | 1.2<br><sub>0,2,0,2,1</sub> |  | 1.3<br><sub>0,0,1,2,2</sub> |  | 0.5 | 0.2 | 0.7 | 12.7 |
| Nikola Jovic | 58% | 15.5<br><sub>-,-,11,-,14</sub> | 5.9<br><sub>-,-,2,-,4</sub> |  | 2.9<br><sub>-,-,1,-,1</sub> |  | 1.7<br><sub>-,-,2,-,4</sub> |  | 0.8<br><sub>-,-,0,-,1</sub> |  | 0.5 | 0.4 | 0.8 | 10.4 |
| Tim Hardaway Jr. | 52% | 15.3<br><sub>-,20,-,-,-</sub> | 6.7<br><sub>-,4,-,-,-</sub> |  | 1.7<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 9.1 |
| Dru Smith | 38% | 11.1<br><sub>-,6,-,-,-</sub> | 4.0<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 7.3 |
| Keshad Johnson | 63% | 8.2<br><sub>-,-,1,3,-</sub> | 3.8<br><sub>-,-,0,0,-</sub> |  | 1.9<br><sub>-,-,0,2,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Nick Richards | 52% | 7.3<br><sub>-,-,-,3,1</sub> | 2.8<br><sub>-,-,-,0,0</sub> |  | 2.5<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.1 | 0.3 | 0.5 | 5.5 |
| Tre Donaldson | 76% | 6.6<br><sub>-,-,1,3,1</sub> | 2.8<br><sub>-,-,2,0,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 1.1 | 3.6 |

</details>


### ORL @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.5–111.9 | ORL 70% | 1.42 / 3.38 | WAS +7.5 | 231.5 | WAS +4.5 covers 41%; o220.5 72% |
| Expected (weighted by chance each plays) | 119.6–112.6 | ORL 69% | 1.46 / 3.20 | WAS +6.5 | 231.5 | WAS +4.5 covers 43%; o220.5 74% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Questionable | 55% | 6.4 | 2.4 | 1.8 | 0.4 | 0.1 | 0.2 | 0.2 | 0.4 | 4.6 | small |
| Deandre Ayton (WAS) | Questionable | 55% | 13.1 | 4.0 | 3.9 | 0.5 | 0.0 | 0.3 | 0.5 | 0.5 | 8.5 | small |
| Bub Carrington (WAS) | Questionable | 55% | 13.8 | 4.2 | 1.6 | 1.7 | 0.6 | 0.3 | 0.1 | 0.8 | 7.5 | small |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 99% | 33.8<br><sub>39,36,38,36,36</sub> | 26.4<br><sub>38,35,21,27,35</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>8,9,8,8,5</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>1,12,9,11,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 2.7 | 39.3 |
| Desmond Bane | 98% | 32.8<br><sub>34,35,39,38,31</sub> | 19.9<br><sub>25,21,24,15,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,5,8,3,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>2,3,5,3,3</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 3.1<br><sub>7,6,3,5,7</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 1.7 | 27.5 |
| Anthony Black | 98% | 32.2<br><sub>39,37,33,37,37</sub> | 15.9<br><sub>22,5,20,15,13</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>7,2,2,2,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>8,5,7,6,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>3,1,3,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.7 | 2.3 | 25.2 |
| Wendell Carter Jr. | 99% | 30.0<br><sub>28,30,28,32,35</sub> | 13.2<br><sub>9,12,10,15,8</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 8.3<br><sub>7,8,3,8,8</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>3,0,1,3,2</sub> |  | 0.8<br><sub>0,1,1,2,0</sub> |  | 0.8 | 0.8 | 1.4 | 23.4 |
| Jalen Suggs | 98% | 28.1<br><sub>-,21,25,31,30</sub> | 12.1<br><sub>-,3,12,18,8</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>-,2,6,8,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.7<br><sub>-,3,4,4,2</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.7<br><sub>-,1,2,5,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.6 | 0.6 | 2.2 | 20.7 |
| Tristan da Silva | 88% | 26.2<br><sub>-,31,31,27,24</sub> | 11.7<br><sub>-,12,13,12,6</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>-,6,6,2,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>-,2,3,0,2</sub> |  | 1.8<br><sub>-,2,3,2,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.0 | 17.3 |
| Goga Bitadze | 91% | 15.6<br><sub>20,18,20,20,15</sub> | 6.4<br><sub>4,12,10,8,4</sub> |  | 5.5<br><sub>7,4,6,3,4</sub> |  | 1.2<br><sub>0,1,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 13.1 |
| Jevon Carter | 91% | 13.5<br><sub>28,17,12,16,10</sub> | 5.2<br><sub>11,5,3,6,3</sub> |  | 1.4<br><sub>3,2,2,2,0</sub> |  | 1.6<br><sub>4,2,1,3,0</sub> |  | 0.8<br><sub>3,1,1,2,1</sub> |  | 0.7 | 0.2 | 0.4 | 8.2 |
| Nikola Vucevic | 67% | 13.4<br><sub>14,11,-,-,23</sub> | 6.3<br><sub>3,2,-,-,15</sub> |  | 4.2<br><sub>5,3,-,-,8</sub> |  | 1.4<br><sub>1,0,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,3</sub> |  | 0.3 | 0.4 | 0.6 | 11.9 |
| Jase Richardson | 52% | 13.2<br><sub>20,-,-,-,-</sub> | 5.0<br><sub>6,-,-,-,-</sub> |  | 1.5<br><sub>1,-,-,-,-</sub> |  | 1.5<br><sub>2,-,-,-,-</sub> |  | 0.4<br><sub>1,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 8.0 |
| Jamal Cain | 67% | 9.6<br><sub>-,4,15,4,-</sub> | 3.9<br><sub>-,0,2,0,-</sub> |  | 1.9<br><sub>-,4,5,1,-</sub> |  | 0.5<br><sub>-,1,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.2 |
| Alex Morales | 48% | 7.6<br><sub>18,-,-,-,-</sub> | 1.9<br><sub>5,-,-,-,-</sub> |  | 1.4<br><sub>4,-,-,-,-</sub> |  | 0.5<br><sub>3,-,-,-,-</sub> |  | 0.1<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Colin Castleton | 48% | 6.0<br><sub>1,-,-,-,-</sub> | 2.3<br><sub>0,-,-,-,-</sub> |  | 1.9<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.7 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 36.3<br><sub>44,30,32,38,37</sub> | 16.9<br><sub>5,16,21,23,20</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>8,7,5,12,10</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>4,1,3,2,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>1,2,1,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.6 | 2.4 | 27.0 |
| Trae Young | 99% | 35.9<br><sub>45,26,33,32,35</sub> | 19.2<br><sub>37,0,13,11,16</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>2,1,2,1,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>14,8,12,8,5</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,0,2,1,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.2 | 3.4 | 31.3 |
| Anthony Davis | 99% | 35.7<br><sub>44,31,35,34,34</sub> | 23.3<br><sub>30,14,23,25,36</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 11.2<br><sub>15,8,4,14,11</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>4,5,0,2,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.7<br><sub>0,0,0,2,0</sub> |  | 1.2 | 1.7 | 2.3 | 37.3 |
| Kyshawn George | 99% | 35.3<br><sub>26,30,38,40,35</sub> | 17.3<br><sub>14,11,18,20,11</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>1,2,6,2,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>5,4,1,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 1.3 | 2.4 | 26.6 |
| Alex Sarr | 98% | 28.0<br><sub>44,27,31,22,20</sub> | 11.9<br><sub>30,25,6,13,3</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>9,9,4,2,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,2,1,3,0</sub> |  | 1.3<br><sub>4,3,1,3,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 1.8 | 1.5 | 20.8 |
| Bilal Coulibaly | 99% | 25.6<br><sub>29,21,16,26,24</sub> | 8.2<br><sub>4,9,11,3,2</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>7,2,5,8,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,0,0,2,0</sub> |  | 0.7<br><sub>0,1,1,0,0</sub> |  | 1.1 | 0.9 | 1.1 | 13.9 |
| Khris Middleton | 64% | 20.2<br><sub>-,9,18,20,28</sub> | 6.8<br><sub>-,8,9,8,5</sub> |  | 2.9<br><sub>-,0,3,4,2</sub> |  | 1.9<br><sub>-,2,3,1,3</sub> |  | 0.8<br><sub>-,2,2,1,0</sub> |  | 0.6 | 0.1 | 1.2 | 11.6 |
| Tre Johnson | 96% | 16.5<br><sub>30,-,21,8,4</sub> | 6.6<br><sub>13,-,9,0,2</sub> |  | 1.6<br><sub>4,-,1,2,1</sub> |  | 0.8<br><sub>2,-,3,0,0</sub> |  | 0.8<br><sub>1,-,2,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 9.0 |
| Will Riley | 88% | 10.9<br><sub>3,16,2,10,6</sub> | 4.7<br><sub>3,14,2,0,0</sub> |  | 1.4<br><sub>0,3,1,3,1</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>1,2,0,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.8 |
| Anthony Gill | 48% | 8.0<br><sub>-,6,2,-,-</sub> | 2.9<br><sub>-,5,2,-,-</sub> |  | 1.3<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |
| Tre Mann | 52% | 6.8<br><sub>-,11,2,-,-</sub> | 2.6<br><sub>-,4,2,-,-</sub> |  | 0.8<br><sub>-,1,0,-,-</sub> |  | 0.7<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.2 |

</details>


### DEN @ CHI
Out: Nic Claxton (CHI), Norman Powell (CHI), Caleb Wilson (CHI), Bryce Hopkins (DEN), Julian Strawther (DEN), Cam Whitmore (DEN)

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.2<br><sub>37,37,38,39,38</sub> | 28.9<br><sub>27,26,28,24,26</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 12.6<br><sub>11,8,15,8,7</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>8,10,7,9,11</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.7 | 0.8 | 3.4 | 51.7 |
| Jamal Murray | 98% | 36.6<br><sub>32,38,35,38,36</sub> | 26.2<br><sub>30,23,28,21,14</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>4,7,4,7,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>8,9,4,2,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,0,1,2,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.6 | 2.1 | 37.4 |
| Christian Braun | 98% | 33.2<br><sub>37,28,33,35,31</sub> | 12.7<br><sub>12,17,10,15,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,7,3,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>4,1,3,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>2,1,2,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.4 | 0.9 | 20.0 |
| Aaron Gordon | 98% | 30.1<br><sub>27,33,24,31,31</sub> | 14.0<br><sub>9,11,11,13,18</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>3,5,1,8,3</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.3<br><sub>1,1,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.4 | 1.2 | 22.1 |
| Cameron Johnson | 98% | 30.0<br><sub>30,31,27,26,29</sub> | 14.0<br><sub>23,12,9,8,19</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,5,0,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,2,1,1,6</sub> |  | 1.8<br><sub>4,1,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.0 | 20.4 |
| DeMar DeRozan | 91% | 22.5<br><sub>20,24,14,25,22</sub> | 11.8<br><sub>8,9,2,18,15</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>1,3,1,2,2</sub> |  | 3.0<br><sub>4,2,1,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.0 | 16.9 |
| Spencer Jones | 91% | 16.5<br><sub>22,12,21,17,18</sub> | 4.0<br><sub>3,4,4,2,3</sub> |  | 2.3<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>0,1,3,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.6 | 7.2 |
| Trevon Brazile | 98% | 14.8<br><sub>13,16,23,11,11</sub> | 4.6<br><sub>7,5,9,0,4</sub> |  | 3.8<br><sub>5,3,4,6,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 8.9 |
| Marvin Bagley III | 98% | 12.7<br><sub>12,13,10,9,10</sub> | 6.5<br><sub>4,7,4,4,10</sub> |  | 4.0<br><sub>2,7,2,3,6</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.6 | 0.6 | 11.2 |
| Tyus Jones | 98% | 11.6<br><sub>11,10,10,9,14</sub> | 3.0<br><sub>0,2,0,0,5</sub> |  | 1.0<br><sub>1,0,1,0,3</sub> |  | 2.1<br><sub>4,3,2,0,4</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.4 | 6.1 |
| Zeke Nnaji | 23% | 7.1<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.4 |
| Alpha Diallo | 38% | 6.7<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Ryan Nembhard | 48% | 6.0<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matas Buzelis | 99% | 30.6<br><sub>29,30,31,30,25</sub> | 18.2<br><sub>11,18,23,25,9</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>6,9,3,5,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,2,0,4,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>3,2,3,5,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7 | 1.1 | 2.3 | 26.3 |
| Josh Giddey | 99% | 30.0<br><sub>39,26,24,28,23</sub> | 14.7<br><sub>15,8,4,18,2</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>10,8,4,14,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 8.7<br><sub>14,5,8,9,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,2,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.6 | 2.9 | 30.2 |
| Isaac Okoro | 99% | 30.0<br><sub>41,31,32,25,29</sub> | 11.1<br><sub>15,9,13,12,9</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,7,6,3,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,4,2,4,1</sub> |  | 1.3<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.4 | 1.0 | 16.7 |
| Jalen Smith | 98% | 28.4<br><sub>32,-,28,21,-</sub> | 15.8<br><sub>15,-,17,14,-</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 8.8<br><sub>12,-,11,6,-</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,-,3,3,-</sub> |  | 2.0<br><sub>1,-,3,2,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.6 | 0.9 | 1.3 | 26.8 |
| Patrick Williams | 88% | 24.2<br><sub>24,26,13,13,23</sub> | 8.8<br><sub>13,14,0,2,6</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>4,5,0,1,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,1,0,2,1</sub> |  | 1.2<br><sub>4,2,0,0,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 0.5 | 1.1 | 14.1 |
| Tre Jones | 99% | 24.2<br><sub>15,24,23,16,25</sub> | 13.9<br><sub>4,16,16,10,12</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>1,0,2,2,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>3,4,6,6,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 1.0 | 0.2 | 1.4 | 21.6 |
| Buddy Hield | 88% | 21.3<br><sub>25,20,19,19,23</sub> | 10.4<br><sub>12,16,6,11,15</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>3,4,4,1,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>3,2,2,2,0</sub> |  | 1.8<br><sub>2,4,2,3,4</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.1 | 15.1 |
| Zach Collins | 71% | 17.0<br><sub>-,28,-,11,15</sub> | 7.2<br><sub>-,8,-,3,6</sub> |  | 4.8<br><sub>-,5,-,2,2</sub> |  | 1.8<br><sub>-,4,-,0,4</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.5 | 0.5 | 0.9 | 13.8 |
| Noa Essengue | 98% | 15.4<br><sub>8,7,14,15,15</sub> | 6.0<br><sub>5,0,1,5,8</sub> |  | 3.4<br><sub>1,1,2,3,4</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.6<br><sub>1,0,0,0,2</sub> |  | 0.5 | 0.2 | 0.8 | 10.2 |
| Leonard Miller | 64% | 15.0<br><sub>-,17,1,7,-</sub> | 7.0<br><sub>-,4,0,4,-</sub> |  | 3.6<br><sub>-,3,0,2,-</sub> |  | 0.9<br><sub>-,4,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 11.6 |
| Jordan Hawkins | 52% | 12.7<br><sub>-,-,4,-,-</sub> | 5.6<br><sub>-,-,0,-,-</sub> |  | 1.6<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 8.1 |
| Orlando Robinson | 30% | 12.6<br><sub>-,-,-,-,-</sub> | 5.1<br><sub>-,-,-,-,-</sub> |  | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 9.9 |
| Tobe Awaka | 58% | 9.7<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.4 | 0.4 | 7.3 |
| Jaylin Sellers | 76% | 9.1<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 6.4 |
| Dailyn Swain | 67% | 8.1<br><sub>-,-,2,6,-</sub> | 3.2<br><sub>-,-,0,2,-</sub> |  | 1.3<br><sub>-,-,1,1,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.6 | 5.2 |

</details>


### DAL @ UTA
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.4–117.9 | DAL 54% | 1.84 / 2.19 | UTA +1.5 | 236.5 | UTA +2.5 covers 52%; o225.5 73% |
| Expected (weighted by chance each plays) | 119.8–117.8 | DAL 55% | 1.82 / 2.22 | UTA +2.5 | 237.5 | UTA +2.5 covers 51%; o225.5 74% |
| if Walter Clayton Jr. plays | 119.9–117.8 | DAL 56% | 1.79 / 2.27 | UTA +2.5 | 237.5 | UTA +2.5 covers 50%; o225.5 74% |
| if P.J. Washington plays | 119.6–117.7 | DAL 55% | 1.81 / 2.24 | UTA +2.5 | 237.5 | UTA +2.5 covers 51%; o225.5 74% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walter Clayton Jr. (DAL) | Questionable | 55% | 22.1 | 8.6 | 3.5 | 3.4 | 1.2 | 0.9 | 0.2 | 1.5 | 15.5 | full tables below |
| P.J. Washington (DAL) | Doubtful | 20% | 31.2 | 14.3 | 7.0 | 1.6 | 1.8 | 1.0 | 1.0 | 1.4 | 22.9 | full tables below |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 99% | 35.9<br><sub>27,38,27,34,36</sub> | 26.2<br><sub>12,18,17,33,22</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>7,8,3,5,6</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 6.2<br><sub>3,5,4,9,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,0,2,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.7 | 0.9 | 2.8 | 39.5 |
| Kyrie Irving | 98% | 35.7<br><sub>27,37,-,29,35</sub> | 26.6<br><sub>10,34,-,17,25</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,6,-,6,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 4.7<br><sub>4,5,-,5,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>2,7,-,1,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.5 | 2.2 | 35.7 |
| Daniel Gafford | 99% | 27.8<br><sub>16,17,19,24,31</sub> | 11.7<br><sub>3,10,3,6,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>3,3,4,6,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>1,1,2,2,3</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.9 | 2.1 | 1.2 | 21.4 |
| Naji Marshall | 96% | 27.3<br><sub>23,30,23,27,14</sub> | 13.6<br><sub>13,12,13,12,4</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,3,2,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,5,2,2,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,0,3,2,0</sub> |  | 1.3 | 0.1 | 1.6 | 21.2 |
| Zaccharie Risacher | 98% | 26.9<br><sub>25,14,27,18,29</sub> | 9.8<br><sub>22,5,18,3,11</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>6,2,5,3,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>3,0,0,0,1</sub> |  | 1.2<br><sub>4,1,1,1,1</sub> |  | 1.1 | 0.9 | 1.0 | 16.7 |
| Caleb Martin | 98% | 24.6<br><sub>21,33,34,20,20</sub> | 6.5<br><sub>7,15,12,8,0</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,8,5,5,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>5,3,5,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7<br><sub>1,1,4,2,0</sub> |  | 1.1 | 0.4 | 0.8 | 12.8 |
| Max Christie | 98% | 21.3<br><sub>7,-,-,8,24</sub> | 8.4<br><sub>3,-,-,5,13</sub> |  | 2.6<br><sub>2,-,-,1,4</sub> |  | 1.3<br><sub>0,-,-,2,0</sub> |  | 1.3<br><sub>1,-,-,1,3</sub> |  | 0.7 | 0.3 | 0.8 | 12.3 |
| Morez Johnson Jr. | 99% | 19.9<br><sub>13,15,26,15,17</sub> | 7.6<br><sub>0,4,2,3,9</sub> |  | 4.1<br><sub>2,2,6,1,7</sub> |  | 1.8<br><sub>0,0,4,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.6 | 0.2 | 1.1 | 13.4 |
| Santi Aldama | 98% | 15.9<br><sub>10,16,-,6,9</sub> | 7.4<br><sub>3,7,-,0,0</sub> |  | 3.7<br><sub>1,2,-,0,1</sub> |  | 1.3<br><sub>1,1,-,0,0</sub> |  | 0.9<br><sub>1,2,-,0,0</sub> |  | 0.6 | 0.4 | 0.8 | 12.4 |
| Marcus Sasser | 58% | 14.6<br><sub>9,-,18,4,-</sub> | 5.3<br><sub>3,-,5,0,-</sub> |  | 1.4<br><sub>1,-,1,2,-</sub> |  | 1.7<br><sub>0,-,2,1,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.6 | 0.1 | 0.7 | 8.4 |
| Moussa Cisse | 58% | 9.1<br><sub>8,-,4,4,-</sub> | 2.9<br><sub>0,-,1,0,-</sub> |  | 3.4<br><sub>0,-,1,1,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.7 | 0.4 | 6.5 |
| Jett Howard | 63% | 8.4<br><sub>5,-,7,-,-</sub> | 3.4<br><sub>3,-,0,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>0,-,1,-,-</sub> |  | 0.3<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 35.0<br><sub>38,34,35,39,36</sub> | 24.1<br><sub>27,13,30,30,14</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>4,4,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.5<br><sub>7,8,11,10,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,1,4,5,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 3.2 | 35.9 |
| Darryn Peterson | 98% | 31.6<br><sub>34,34,31,19,32</sub> | 18.6<br><sub>28,17,13,11,20</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>7,5,5,1,10</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>2,4,2,3,8</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>4,3,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 2.0 | 27.8 |
| Ace Bailey | 99% | 30.7<br><sub>35,30,23,27,24</sub> | 15.5<br><sub>21,7,5,19,7</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,8,1,8,7</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,4,4,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.1<br><sub>3,1,1,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.9 | 1.8 | 23.3 |
| Jaxson Hayes | 88% | 25.4<br><sub>13,-,-,25,28</sub> | 10.7<br><sub>12,-,-,6,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>5,-,-,7,14</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,-,-,2,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.9 |
| Josh Green | 97% | 24.4<br><sub>14,15,13,28,29</sub> | 6.2<br><sub>2,6,9,11,8</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 31% · u 69%</sub> | 0.9 | 0.2 | 0.8 | 10.0 |
| Brice Sensabaugh | 99% | 23.9<br><sub>27,30,35,14,26</sub> | 15.6<br><sub>7,14,40,8,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.2<br><sub>1,0,8,0,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.3 | 1.9 | 21.8 |
| Svi Mykhailiuk | 98% | 23.3<br><sub>7,21,33,34,28</sub> | 8.9<br><sub>0,6,8,15,11</sub> |  | 2.8<br><sub>1,2,7,3,7</sub> |  | 2.1<br><sub>0,3,5,5,2</sub> |  | 1.5<br><sub>0,2,2,4,3</sub> |  | 0.7 | 0.1 | 0.9 | 13.8 |
| Mo Bamba | 91% | 21.4<br><sub>20,36,31,23,20</sub> | 8.0<br><sub>9,26,15,6,2</sub> |  | 7.5<br><sub>9,5,10,16,2</sub> |  | 1.1<br><sub>1,4,3,0,0</sub> |  | 0.5<br><sub>0,6,1,0,0</sub> |  | 0.5 | 1.7 | 0.9 | 16.6 |
| Josh Okogie | 98% | 19.5<br><sub>22,27,22,15,17</sub> | 5.6<br><sub>7,7,9,3,3</sub> |  | 3.1<br><sub>2,6,2,0,2</sub> |  | 1.2<br><sub>1,0,4,0,2</sub> |  | 0.6<br><sub>2,2,1,0,0</sub> |  | 1.0 | 0.3 | 0.7 | 9.9 |
| Isaiah Collier | 58% | 14.3<br><sub>16,-,-,10,-</sub> | 7.0<br><sub>3,-,-,0,-</sub> |  | 2.0<br><sub>2,-,-,1,-</sub> |  | 3.9<br><sub>5,-,-,2,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.6 | 0.2 | 1.3 | 13.0 |
| Kyle Filipowski | 52% | 11.5<br><sub>2,-,-,6,-</sub> | 6.4<br><sub>2,-,-,0,-</sub> |  | 3.6<br><sub>0,-,-,3,-</sub> |  | 1.2<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.8 | 11.2 |
| Tony Bradley | 52% | 9.2<br><sub>12,12,17,-,-</sub> | 3.1<br><sub>0,6,3,-,-</sub> |  | 3.0<br><sub>5,2,7,-,-</sub> |  | 0.5<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 6.5 |

</details>

<details><summary>if P.J. Washington plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 99% | 34.9<br><sub>27,38,27,34,36</sub> | 25.2<br><sub>12,18,17,33,22</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>7,8,3,5,6</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 6.0<br><sub>3,5,4,9,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,0,2,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.8 | 0.9 | 2.7 | 38.1 |
| Kyrie Irving (DAL) | 98% | 34.5<br><sub>27,37,-,29,35</sub> | 24.5<br><sub>10,34,-,17,25</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>3,6,-,6,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 4.4<br><sub>4,5,-,5,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,7,-,1,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.5 | 2.1 | 33.3 |
| P.J. Washington (DAL) | 100% | 31.2<br><sub>16,26,25,25,-</sub> | 14.3<br><sub>10,10,8,21,-</sub> |  | 7.0<br><sub>3,4,5,5,-</sub> |  | 1.6<br><sub>0,1,4,2,-</sub> |  | 1.8<br><sub>1,2,0,5,-</sub> |  | 1.0 | 1.0 | 1.4 | 22.9 |
| Daniel Gafford (DAL) | 99% | 23.9<br><sub>16,17,19,24,31</sub> | 10.1<br><sub>3,10,3,6,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>3,3,4,6,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,1,2,2,3</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.8 | 1.8 | 1.1 | 18.6 |
| Naji Marshall (DAL) | 96% | 23.0<br><sub>23,30,23,27,14</sub> | 11.0<br><sub>13,12,13,12,4</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>1,3,2,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>4,5,2,2,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.8<br><sub>1,0,3,2,0</sub> |  | 1.0 | 0.1 | 1.5 | 17.3 |
| Zaccharie Risacher (DAL) | 98% | 22.1<br><sub>25,14,27,18,29</sub> | 8.0<br><sub>22,5,18,3,11</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>6,2,5,3,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>3,0,0,0,1</sub> |  | 0.9<br><sub>4,1,1,1,1</sub> |  | 0.9 | 0.8 | 0.9 | 13.6 |
| Caleb Martin (DAL) | 98% | 20.2<br><sub>21,33,34,20,20</sub> | 5.0<br><sub>7,15,12,8,0</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,8,5,5,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>5,3,5,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.5<br><sub>1,1,4,2,0</sub> |  | 0.9 | 0.4 | 0.7 | 10.2 |
| Max Christie (DAL) | 98% | 17.6<br><sub>7,-,-,8,24</sub> | 6.8<br><sub>3,-,-,5,13</sub> |  | 2.2<br><sub>2,-,-,1,4</sub> |  | 1.0<br><sub>0,-,-,2,0</sub> |  | 1.0<br><sub>1,-,-,1,3</sub> |  | 0.5 | 0.3 | 0.7 | 10.0 |
| Morez Johnson Jr. (DAL) | 99% | 15.8<br><sub>13,15,26,15,17</sub> | 5.9<br><sub>0,4,2,3,9</sub> |  | 3.3<br><sub>2,2,6,1,7</sub> |  | 1.4<br><sub>0,0,4,1,2</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.2 | 0.9 | 10.6 |
| Santi Aldama (DAL) | 98% | 12.9<br><sub>10,16,-,6,9</sub> | 6.1<br><sub>3,7,-,0,0</sub> |  | 3.1<br><sub>1,2,-,0,1</sub> |  | 1.0<br><sub>1,1,-,0,0</sub> |  | 0.7<br><sub>1,2,-,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 10.2 |
| Marcus Sasser (DAL) | 58% | 11.0<br><sub>9,-,18,4,-</sub> | 4.0<br><sub>3,-,5,0,-</sub> |  | 1.0<br><sub>1,-,1,2,-</sub> |  | 1.3<br><sub>0,-,2,1,-</sub> |  | 0.5<br><sub>0,-,1,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Moussa Cisse (DAL) | 58% | 7.0<br><sub>8,-,4,4,-</sub> | 2.5<br><sub>0,-,1,0,-</sub> |  | 2.7<br><sub>0,-,1,1,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.6 | 0.3 | 5.4 |
| Jett Howard (DAL) | 63% | 6.5<br><sub>5,-,7,-,-</sub> | 2.9<br><sub>3,-,0,-,-</sub> |  | 0.8<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |
| Keyonte George (UTA) | 99% | 35.0<br><sub>38,34,35,39,36</sub> | 24.2<br><sub>27,13,30,30,14</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>4,4,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.5<br><sub>7,8,11,10,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>4,1,4,5,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 3.2 | 36.0 |
| Darryn Peterson (UTA) | 98% | 31.7<br><sub>34,34,31,19,32</sub> | 18.6<br><sub>28,17,13,11,20</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>7,5,5,1,10</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>2,4,2,3,8</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>4,3,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 2.0 | 27.8 |
| Ace Bailey (UTA) | 99% | 30.7<br><sub>35,30,23,27,24</sub> | 15.6<br><sub>21,7,5,19,7</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,8,1,8,7</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,4,4,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.1<br><sub>3,1,1,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.9 | 1.7 | 23.4 |
| Jaxson Hayes (UTA) | 88% | 25.3<br><sub>13,-,-,25,28</sub> | 10.6<br><sub>12,-,-,6,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>5,-,-,7,14</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,-,-,2,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.8 |
| Josh Green (UTA) | 97% | 24.3<br><sub>14,15,13,28,29</sub> | 6.3<br><sub>2,6,9,11,8</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 31% · u 69%</sub> | 0.9 | 0.2 | 0.8 | 10.0 |
| Brice Sensabaugh (UTA) | 99% | 23.9<br><sub>27,30,35,14,26</sub> | 15.5<br><sub>7,14,40,8,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.2<br><sub>1,0,8,0,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.9 | 21.7 |
| Svi Mykhailiuk (UTA) | 98% | 23.3<br><sub>7,21,33,34,28</sub> | 8.9<br><sub>0,6,8,15,11</sub> |  | 2.8<br><sub>1,2,7,3,7</sub> |  | 2.1<br><sub>0,3,5,5,2</sub> |  | 1.5<br><sub>0,2,2,4,3</sub> |  | 0.7 | 0.1 | 0.9 | 13.8 |
| Mo Bamba (UTA) | 91% | 21.4<br><sub>20,36,31,23,20</sub> | 7.9<br><sub>9,26,15,6,2</sub> |  | 7.5<br><sub>9,5,10,16,2</sub> |  | 1.1<br><sub>1,4,3,0,0</sub> |  | 0.5<br><sub>0,6,1,0,0</sub> |  | 0.5 | 1.7 | 0.9 | 16.5 |
| Josh Okogie (UTA) | 98% | 19.5<br><sub>22,27,22,15,17</sub> | 5.6<br><sub>7,7,9,3,3</sub> |  | 3.1<br><sub>2,6,2,0,2</sub> |  | 1.2<br><sub>1,0,4,0,2</sub> |  | 0.6<br><sub>2,2,1,0,0</sub> |  | 1.0 | 0.3 | 0.7 | 9.9 |
| Isaiah Collier (UTA) | 58% | 14.3<br><sub>16,-,-,10,-</sub> | 7.0<br><sub>3,-,-,0,-</sub> |  | 2.0<br><sub>2,-,-,1,-</sub> |  | 3.8<br><sub>5,-,-,2,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.6 | 0.2 | 1.3 | 12.9 |
| Kyle Filipowski (UTA) | 52% | 11.4<br><sub>2,-,-,6,-</sub> | 6.3<br><sub>2,-,-,0,-</sub> |  | 3.6<br><sub>0,-,-,3,-</sub> |  | 1.2<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.8 | 11.2 |
| Tony Bradley (UTA) | 52% | 9.2<br><sub>12,12,17,-,-</sub> | 3.0<br><sub>0,6,3,-,-</sub> |  | 3.0<br><sub>5,2,7,-,-</sub> |  | 0.5<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 6.5 |

</details>

<details><summary>if Walter Clayton Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 99% | 35.4<br><sub>27,38,27,34,36</sub> | 25.6<br><sub>12,18,17,33,22</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>7,8,3,5,6</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 6.0<br><sub>3,5,4,9,8</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,0,2,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.7 | 0.9 | 2.7 | 38.7 |
| Kyrie Irving (DAL) | 98% | 34.7<br><sub>27,37,-,29,35</sub> | 24.4<br><sub>10,34,-,17,25</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,6,-,6,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 4.3<br><sub>4,5,-,5,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,7,-,1,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.5 | 2.1 | 33.1 |
| Daniel Gafford (DAL) | 99% | 25.9<br><sub>16,17,19,24,31</sub> | 11.1<br><sub>3,10,3,6,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>3,3,4,6,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>1,1,2,2,3</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.8 | 2.0 | 1.2 | 20.2 |
| Naji Marshall (DAL) | 96% | 24.9<br><sub>23,30,23,27,14</sub> | 12.3<br><sub>13,12,13,12,4</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>1,3,2,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>4,5,2,2,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>1,0,3,2,0</sub> |  | 1.1 | 0.1 | 1.5 | 19.1 |
| Zaccharie Risacher (DAL) | 98% | 24.3<br><sub>25,14,27,18,29</sub> | 8.9<br><sub>22,5,18,3,11</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>6,2,5,3,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>3,0,0,0,1</sub> |  | 1.1<br><sub>4,1,1,1,1</sub> |  | 1.0 | 0.8 | 0.9 | 15.2 |
| Caleb Martin (DAL) | 98% | 22.3<br><sub>21,33,34,20,20</sub> | 5.7<br><sub>7,15,12,8,0</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>2,8,5,5,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>5,3,5,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.6<br><sub>1,1,4,2,0</sub> |  | 1.0 | 0.4 | 0.8 | 11.3 |
| Walter Clayton Jr. (DAL) | 100% | 22.1<br><sub>22,13,23,27,25</sub> | 8.6<br><sub>5,2,13,8,16</sub> |  | 3.5<br><sub>1,2,4,2,5</sub> |  | 3.4<br><sub>4,2,3,7,1</sub> |  | 1.2<br><sub>0,0,3,2,2</sub> |  | 0.9 | 0.2 | 1.5 | 15.5 |
| Max Christie (DAL) | 98% | 18.1<br><sub>7,-,-,8,24</sub> | 6.8<br><sub>3,-,-,5,13</sub> |  | 2.2<br><sub>2,-,-,1,4</sub> |  | 1.0<br><sub>0,-,-,2,0</sub> |  | 1.0<br><sub>1,-,-,1,3</sub> |  | 0.6 | 0.3 | 0.7 | 10.1 |
| Morez Johnson Jr. (DAL) | 99% | 17.4<br><sub>13,15,26,15,17</sub> | 6.5<br><sub>0,4,2,3,9</sub> |  | 3.6<br><sub>2,2,6,1,7</sub> |  | 1.5<br><sub>0,0,4,1,2</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.2 | 0.9 | 11.6 |
| Santi Aldama (DAL) | 98% | 14.2<br><sub>10,16,-,6,9</sub> | 6.6<br><sub>3,7,-,0,0</sub> |  | 3.4<br><sub>1,2,-,0,1</sub> |  | 1.1<br><sub>1,1,-,0,0</sub> |  | 0.7<br><sub>1,2,-,0,0</sub> |  | 0.5 | 0.4 | 0.7 | 11.1 |
| Marcus Sasser (DAL) | 58% | 11.9<br><sub>9,-,18,4,-</sub> | 4.4<br><sub>3,-,5,0,-</sub> |  | 1.1<br><sub>1,-,1,2,-</sub> |  | 1.4<br><sub>0,-,2,1,-</sub> |  | 0.5<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.1 | 0.6 | 6.9 |
| Moussa Cisse (DAL) | 58% | 7.7<br><sub>8,-,4,4,-</sub> | 2.5<br><sub>0,-,1,0,-</sub> |  | 2.9<br><sub>0,-,1,1,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 5.6 |
| Jett Howard (DAL) | 63% | 6.9<br><sub>5,-,7,-,-</sub> | 2.9<br><sub>3,-,0,-,-</sub> |  | 0.9<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.3<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.2 |
| Keyonte George (UTA) | 99% | 35.0<br><sub>38,34,35,39,36</sub> | 24.1<br><sub>27,13,30,30,14</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>4,4,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.5<br><sub>7,8,11,10,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>4,1,4,5,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 3.2 | 35.9 |
| Darryn Peterson (UTA) | 98% | 31.6<br><sub>34,34,31,19,32</sub> | 18.6<br><sub>28,17,13,11,20</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>7,5,5,1,10</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>2,4,2,3,8</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>4,3,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 2.0 | 27.7 |
| Ace Bailey (UTA) | 99% | 30.7<br><sub>35,30,23,27,24</sub> | 15.5<br><sub>21,7,5,19,7</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,8,1,8,7</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,4,4,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>3,1,1,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.9 | 1.8 | 23.3 |
| Jaxson Hayes (UTA) | 88% | 25.4<br><sub>13,-,-,25,28</sub> | 10.7<br><sub>12,-,-,6,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>5,-,-,7,14</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,-,-,2,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.8 |
| Josh Green (UTA) | 97% | 24.4<br><sub>14,15,13,28,29</sub> | 6.2<br><sub>2,6,9,11,8</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 31% · u 69%</sub> | 0.9 | 0.2 | 0.8 | 9.9 |
| Brice Sensabaugh (UTA) | 99% | 23.9<br><sub>27,30,35,14,26</sub> | 15.6<br><sub>7,14,40,8,18</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.2<br><sub>1,0,8,0,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.9 | 21.8 |
| Svi Mykhailiuk (UTA) | 98% | 23.3<br><sub>7,21,33,34,28</sub> | 8.9<br><sub>0,6,8,15,11</sub> |  | 2.8<br><sub>1,2,7,3,7</sub> |  | 2.1<br><sub>0,3,5,5,2</sub> |  | 1.5<br><sub>0,2,2,4,3</sub> |  | 0.7 | 0.1 | 0.9 | 13.8 |
| Mo Bamba (UTA) | 91% | 21.4<br><sub>20,36,31,23,20</sub> | 8.0<br><sub>9,26,15,6,2</sub> |  | 7.5<br><sub>9,5,10,16,2</sub> |  | 1.1<br><sub>1,4,3,0,0</sub> |  | 0.5<br><sub>0,6,1,0,0</sub> |  | 0.5 | 1.7 | 0.9 | 16.6 |
| Josh Okogie (UTA) | 98% | 19.5<br><sub>22,27,22,15,17</sub> | 5.6<br><sub>7,7,9,3,3</sub> |  | 3.1<br><sub>2,6,2,0,2</sub> |  | 1.2<br><sub>1,0,4,0,2</sub> |  | 0.6<br><sub>2,2,1,0,0</sub> |  | 1.0 | 0.3 | 0.7 | 9.9 |
| Isaiah Collier (UTA) | 58% | 14.3<br><sub>16,-,-,10,-</sub> | 7.1<br><sub>3,-,-,0,-</sub> |  | 2.0<br><sub>2,-,-,1,-</sub> |  | 3.9<br><sub>5,-,-,2,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.6 | 0.2 | 1.3 | 13.0 |
| Kyle Filipowski (UTA) | 52% | 11.5<br><sub>2,-,-,6,-</sub> | 6.3<br><sub>2,-,-,0,-</sub> |  | 3.6<br><sub>0,-,-,3,-</sub> |  | 1.2<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.8 | 11.2 |
| Tony Bradley (UTA) | 52% | 9.2<br><sub>12,12,17,-,-</sub> | 3.0<br><sub>0,6,3,-,-</sub> |  | 3.0<br><sub>5,2,7,-,-</sub> |  | 0.5<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 6.5 |

</details>


### IND @ NYK
Out: OG Anunoby (NYK), Jordan Clarkson (NYK), Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.9–113.6 | IND 29% | 3.43 / 1.41 | NYK -7.5 | 219.5 | NYK -7.5 covers 51%; o213.5 62% |
| Expected (weighted by chance each plays) | 106.5–114.7 | IND 28% | 3.63 / 1.38 | NYK -8.5 | 220.5 | NYK -7.5 covers 53%; o213.5 65% |
| if Karl-Anthony Towns plays | 106.3–115.6 | IND 25% | 3.93 / 1.34 | NYK -9.5 | 221.5 | NYK -7.5 covers 55%; o213.5 67% |
| if Pascal Siakam plays | 106.8–114.1 | IND 30% | 3.31 / 1.43 | NYK -7.5 | 220.5 | NYK -7.5 covers 49%; o213.5 65% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Karl-Anthony Towns (NYK) | Questionable | 55% | 33.8 | 22.2 | 14.5 | 4.5 | 1.9 | 1.1 | 0.7 | 2.7 | 41.1 | full tables below |
| Pascal Siakam (IND) | Questionable | 55% | 33.8 | 21.5 | 6.1 | 3.8 | 1.6 | 0.9 | 0.4 | 2.0 | 31.4 | full tables below |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 91% | 34.2<br><sub>34,34,-,-,26</sub> | 17.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 2.8 | 28.8 |
| Aaron Nesmith | 93% | 31.8<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.6 | 20.3 |
| Kelly Oubre Jr. | 91% | 27.8<br><sub>34,30,29,23,23</sub> | 12.7<br><sub>14,16,16,17,17</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.3<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.3 | 18.3 |
| Ivica Zubac | 88% | 27.4<br><sub>31,26,22,24,27</sub> | 11.9<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.5 | 23.1 |
| Quenton Jackson | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 0.9 | 0.2 | 1.6 | 18.1 |
| Obi Toppin | 88% | 24.0<br><sub>16,16,14,17,26</sub> | 12.8<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,3,2,1,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.2 | 19.5 |
| Jarace Walker | 88% | 20.2<br><sub>7,-,14,17,11</sub> | 8.4<br><sub>1,-,2,1,8</sub> |  | 4.2<br><sub>1,-,5,3,1</sub> |  | 2.0<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.7 |
| Jalen Slawson | 91% | 17.8<br><sub>12,10,14,12,14</sub> | 5.5<br><sub>2,1,8,5,4</sub> |  | 3.5<br><sub>3,4,5,4,2</sub> |  | 1.6<br><sub>1,0,2,2,2</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.9 | 10.7 |
| Braden Smith | 67% | 16.5<br><sub>-,-,-,18,11</sub> | 5.6<br><sub>-,-,-,8,5</sub> |  | 1.7<br><sub>-,-,-,5,3</sub> |  | 3.2<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 10.5 |
| Jay Huff | 91% | 15.8<br><sub>11,8,18,15,1</sub> | 6.8<br><sub>6,8,11,5,0</sub> |  | 2.8<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.9<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.7 |
| Larry Nance Jr. | 97% | 15.4<br><sub>5,14,7,9,11</sub> | 5.1<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.6<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.8 |
| Kobe Brown | 86% | 14.4<br><sub>-,-,3,2,-</sub> | 5.1<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.8 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 35.5<br><sub>36,41,34,35,36</sub> | 31.8<br><sub>33,28,31,21,30</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>1,1,5,2,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 6.4<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 2.3 | 41.9 |
| Landry Shamet | 99% | 33.3<br><sub>21,30,24,30,36</sub> | 14.9<br><sub>5,23,12,10,20</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,2,1,1,1</sub> |  | 2.1<br><sub>1,0,1,2,3</sub> |  | 2.6<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.0 | 19.5 |
| Josh Hart | 98% | 32.1<br><sub>23,26,31,28,35</sub> | 10.9<br><sub>0,0,5,11,0</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>5,5,4,6,8</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.6 | 22.8 |
| Mikal Bridges | 99% | 31.3<br><sub>29,32,30,31,28</sub> | 13.5<br><sub>18,5,17,8,12</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 1.2 | 20.3 |
| Andre Drummond | 99% | 24.0<br><sub>14,7,11,15,23</sub> | 7.9<br><sub>0,2,2,4,7</sub> |  | 11.3<br><sub>6,3,8,4,13</sub> |  | 1.6<br><sub>0,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.8 | 0.9 | 1.1 | 20.8 |
| Miles McBride | 99% | 21.0<br><sub>22,14,9,8,14</sub> | 8.6<br><sub>9,3,3,3,3</sub> |  | 2.0<br><sub>1,1,0,0,0</sub> |  | 1.6<br><sub>1,0,1,0,1</sub> |  | 1.5<br><sub>3,1,1,0,1</sub> |  | 0.7 | 0.2 | 0.5 | 12.2 |
| James Wiseman | 52% | 20.4<br><sub>-,3,-,-,25</sub> | 7.0<br><sub>-,0,-,-,5</sub> |  | 6.9<br><sub>-,3,-,-,6</sub> |  | 1.1<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.4 | 1.0 | 1.0 | 15.0 |
| Tyler Kolek | 96% | 18.4<br><sub>19,16,13,12,13</sub> | 7.2<br><sub>5,0,4,6,7</sub> |  | 2.6<br><sub>6,0,1,3,3</sub> |  | 4.7<br><sub>2,7,3,5,0</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 14.5 |
| Jose Alvarado | 80% | 17.2<br><sub>-,2,7,13,15</sub> | 7.0<br><sub>-,0,2,2,8</sub> |  | 2.2<br><sub>-,0,0,2,2</sub> |  | 2.8<br><sub>-,1,4,1,2</sub> |  | 0.9<br><sub>-,0,0,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 12.0 |
| Mohamed Diawara | 38% | 16.0<br><sub>-,-,-,-,-</sub> | 6.2<br><sub>-,-,-,-,-</sub> |  | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 10.6 |
| Dalton Knecht | 67% | 14.6<br><sub>-,-,-,-,3</sub> | 5.8<br><sub>-,-,-,-,0</sub> |  | 2.7<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 9.3 |
| Pacome Dadiet | 52% | 14.3<br><sub>1,-,-,-,11</sub> | 5.9<br><sub>0,-,-,-,5</sub> |  | 2.5<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,2</sub> |  | 0.7<br><sub>0,-,-,-,1</sub> |  | 0.4 | 0.1 | 0.4 | 9.3 |
| Jaden Akins | 38% | 9.0<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.2 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Karl-Anthony Towns plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 34.2<br><sub>34,34,-,-,26</sub> | 17.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.2 | 2.8 | 28.9 |
| Aaron Nesmith (IND) | 93% | 31.7<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.6 | 20.4 |
| Kelly Oubre Jr. (IND) | 91% | 27.7<br><sub>34,30,29,23,23</sub> | 12.7<br><sub>14,16,16,17,17</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.3<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.3 | 18.4 |
| Ivica Zubac (IND) | 88% | 27.4<br><sub>31,26,22,24,27</sub> | 12.0<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.5 | 23.1 |
| Quenton Jackson (IND) | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.1<br><sub>1,1,1,2,1</sub> |  | 0.9 | 0.2 | 1.6 | 18.1 |
| Obi Toppin (IND) | 88% | 24.1<br><sub>16,16,14,17,26</sub> | 12.9<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,3,2,1,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.2 | 19.6 |
| Jarace Walker (IND) | 88% | 20.1<br><sub>7,-,14,17,11</sub> | 8.4<br><sub>1,-,2,1,8</sub> |  | 4.1<br><sub>1,-,5,3,1</sub> |  | 2.0<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.5 |
| Jalen Slawson (IND) | 91% | 17.8<br><sub>12,10,14,12,14</sub> | 5.5<br><sub>2,1,8,5,4</sub> |  | 3.5<br><sub>3,4,5,4,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.6 |
| Braden Smith (IND) | 67% | 16.4<br><sub>-,-,-,18,11</sub> | 5.6<br><sub>-,-,-,8,5</sub> |  | 1.7<br><sub>-,-,-,5,3</sub> |  | 3.1<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.8 | 10.5 |
| Jay Huff (IND) | 91% | 15.8<br><sub>11,8,18,15,1</sub> | 6.8<br><sub>6,8,11,5,0</sub> |  | 2.8<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.9<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.7 |
| Larry Nance Jr. (IND) | 97% | 15.3<br><sub>5,14,7,9,11</sub> | 5.1<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.6<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.8 |
| Kobe Brown (IND) | 86% | 14.4<br><sub>-,-,3,2,-</sub> | 5.1<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.8 |
| Jalen Brunson (NYK) | 99% | 35.5<br><sub>36,41,34,35,36</sub> | 31.1<br><sub>33,28,31,21,30</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>1,1,5,2,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 6.7<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 2.2 | 41.4 |
| Karl-Anthony Towns (NYK) | 100% | 33.8<br><sub>34,43,36,33,-</sub> | 22.2<br><sub>23,28,16,22,-</sub> | 20.5 · – | 14.5<br><sub>15,17,16,12,-</sub> | 12.5 | 4.5<br><sub>5,3,8,4,-</sub> | 3.5 | 1.9<br><sub>3,3,1,2,-</sub> | 1.5 | 1.1 | 0.7 | 2.7 | 41.1 |
| Josh Hart (NYK) | 98% | 30.9<br><sub>23,26,31,28,35</sub> | 9.3<br><sub>0,0,5,11,0</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>5,5,4,6,8</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.3 | 20.5 |
| Landry Shamet (NYK) | 99% | 30.6<br><sub>21,30,24,30,36</sub> | 12.1<br><sub>5,23,12,10,20</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>3,2,1,1,1</sub> |  | 1.9<br><sub>1,0,1,2,3</sub> |  | 2.2<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.8 | 16.1 |
| Mikal Bridges (NYK) | 99% | 29.4<br><sub>29,32,30,31,28</sub> | 11.5<br><sub>18,5,17,8,12</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 1.0 | 17.8 |
| Andre Drummond (NYK) | 99% | 17.7<br><sub>14,7,11,15,23</sub> | 5.5<br><sub>0,2,2,4,7</sub> |  | 8.4<br><sub>6,3,8,4,13</sub> |  | 1.2<br><sub>0,0,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.6 | 0.7 | 0.9 | 15.2 |
| Miles McBride (NYK) | 99% | 17.7<br><sub>22,14,9,8,14</sub> | 6.6<br><sub>9,3,3,3,3</sub> |  | 1.5<br><sub>1,1,0,0,0</sub> |  | 1.3<br><sub>1,0,1,0,1</sub> |  | 1.1<br><sub>3,1,1,0,1</sub> |  | 0.6 | 0.2 | 0.4 | 9.4 |
| Tyler Kolek (NYK) | 96% | 14.6<br><sub>19,16,13,12,13</sub> | 5.1<br><sub>5,0,4,6,7</sub> |  | 2.0<br><sub>6,0,1,3,3</sub> |  | 3.8<br><sub>2,7,3,5,0</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 10.9 |
| James Wiseman (NYK) | 52% | 14.6<br><sub>-,3,-,-,25</sub> | 4.9<br><sub>-,0,-,-,5</sub> |  | 4.9<br><sub>-,3,-,-,6</sub> |  | 0.8<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.7 | 0.8 | 10.5 |
| Jose Alvarado (NYK) | 80% | 14.1<br><sub>-,2,7,13,15</sub> | 5.4<br><sub>-,0,2,2,8</sub> |  | 1.8<br><sub>-,0,0,2,2</sub> |  | 2.3<br><sub>-,1,4,1,2</sub> |  | 0.7<br><sub>-,0,0,0,2</sub> |  | 0.7 | 0.1 | 0.8 | 9.5 |
| Mohamed Diawara (NYK) | 38% | 12.0<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 7.2 |
| Pacome Dadiet (NYK) | 52% | 11.2<br><sub>1,-,-,-,11</sub> | 4.7<br><sub>0,-,-,-,5</sub> |  | 1.9<br><sub>0,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 7.3 |
| Dalton Knecht (NYK) | 67% | 9.2<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 5.6 |
| Tyler Nickel (NYK) | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jaden Akins (NYK) | 38% | 7.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |

</details>

<details><summary>if Pascal Siakam plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam (IND) | 100% | 33.8<br><sub>32,32,34,33,30</sub> | 21.5<br><sub>28,19,31,24,21</sub> | 20.5 · – | 6.1<br><sub>8,3,2,4,7</sub> | 5.5 | 3.8<br><sub>5,2,2,3,2</sub> | 2.5 | 1.6<br><sub>2,2,0,2,2</sub> | 1.5 | 0.9 | 0.4 | 2.0 | 31.4 |
| Andrew Nembhard (IND) | 91% | 33.1<br><sub>34,34,-,-,26</sub> | 15.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 2.3 | 26.3 |
| Aaron Nesmith (IND) | 93% | 29.2<br><sub>22,33,36,29,29</sub> | 11.7<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,1,4,3,7</sub> |  | 1.7<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.2 | 17.6 |
| Ivica Zubac (IND) | 88% | 26.1<br><sub>31,26,22,24,27</sub> | 11.1<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.4 | 21.1 |
| Kelly Oubre Jr. (IND) | 91% | 25.3<br><sub>34,30,29,23,23</sub> | 10.8<br><sub>14,16,16,17,17</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>1,0,2,0,0</sub> |  | 1.1<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.5 | 1.1 | 15.9 |
| Quenton Jackson (IND) | 98% | 21.1<br><sub>21,20,30,22,18</sub> | 8.9<br><sub>4,3,15,15,3</sub> |  | 2.9<br><sub>2,5,6,2,2</sub> |  | 3.0<br><sub>2,4,8,3,2</sub> |  | 0.9<br><sub>1,1,1,2,1</sub> |  | 0.8 | 0.2 | 1.3 | 14.8 |
| Obi Toppin (IND) | 88% | 19.6<br><sub>16,16,14,17,26</sub> | 10.1<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,3,2,1,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>1,1,1,1,2</sub> |  | 1.2<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.5 | 0.2 | 0.9 | 15.5 |
| Jarace Walker (IND) | 88% | 15.6<br><sub>7,-,14,17,11</sub> | 6.0<br><sub>1,-,2,1,8</sub> |  | 3.2<br><sub>1,-,5,3,1</sub> |  | 1.4<br><sub>0,-,2,1,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.3 | 0.8 | 10.5 |
| Jalen Slawson (IND) | 91% | 13.4<br><sub>12,10,14,12,14</sub> | 3.9<br><sub>2,1,8,5,4</sub> |  | 2.7<br><sub>3,4,5,4,2</sub> |  | 1.2<br><sub>1,0,2,2,2</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 0.6 | 7.7 |
| Braden Smith (IND) | 67% | 13.3<br><sub>-,-,-,18,11</sub> | 4.3<br><sub>-,-,-,8,5</sub> |  | 1.4<br><sub>-,-,-,5,3</sub> |  | 2.5<br><sub>-,-,-,3,5</sub> |  | 0.3<br><sub>-,-,-,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Jay Huff (IND) | 91% | 11.9<br><sub>11,8,18,15,1</sub> | 4.9<br><sub>6,8,11,5,0</sub> |  | 2.1<br><sub>4,1,0,3,0</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.6<br><sub>0,2,3,0,0</sub> |  | 0.2 | 0.7 | 0.5 | 7.7 |
| Larry Nance Jr. (IND) | 97% | 11.7<br><sub>5,14,7,9,11</sub> | 3.7<br><sub>5,2,4,3,7</sub> |  | 2.1<br><sub>0,2,2,1,2</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.4<br><sub>1,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Kobe Brown (IND) | 86% | 9.3<br><sub>-,-,3,2,-</sub> | 3.1<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| Jalen Brunson (NYK) | 99% | 35.6<br><sub>36,41,34,35,36</sub> | 31.9<br><sub>33,28,31,21,30</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>1,1,5,2,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 6.4<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 2.3 | 42.0 |
| Landry Shamet (NYK) | 99% | 33.3<br><sub>21,30,24,30,36</sub> | 15.0<br><sub>5,23,12,10,20</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,2,1,1,1</sub> |  | 2.1<br><sub>1,0,1,2,3</sub> |  | 2.7<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.0 | 19.6 |
| Josh Hart (NYK) | 98% | 32.0<br><sub>23,26,31,28,35</sub> | 10.8<br><sub>0,0,5,11,0</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>5,5,4,6,8</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.5 | 22.7 |
| Mikal Bridges (NYK) | 99% | 31.3<br><sub>29,32,30,31,28</sub> | 13.6<br><sub>18,5,17,8,12</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.6 | 1.2 | 20.4 |
| Andre Drummond (NYK) | 99% | 24.0<br><sub>14,7,11,15,23</sub> | 7.9<br><sub>0,2,2,4,7</sub> |  | 11.4<br><sub>6,3,8,4,13</sub> |  | 1.6<br><sub>0,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.8 | 0.9 | 1.1 | 21.0 |
| Miles McBride (NYK) | 99% | 21.0<br><sub>22,14,9,8,14</sub> | 8.6<br><sub>9,3,3,3,3</sub> |  | 2.0<br><sub>1,1,0,0,0</sub> |  | 1.5<br><sub>1,0,1,0,1</sub> |  | 1.5<br><sub>3,1,1,0,1</sub> |  | 0.7 | 0.2 | 0.5 | 12.1 |
| James Wiseman (NYK) | 52% | 20.5<br><sub>-,3,-,-,25</sub> | 7.0<br><sub>-,0,-,-,5</sub> |  | 6.9<br><sub>-,3,-,-,6</sub> |  | 1.1<br><sub>-,0,-,-,2</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.9 | 1.0 | 15.1 |
| Tyler Kolek (NYK) | 96% | 18.4<br><sub>19,16,13,12,13</sub> | 7.2<br><sub>5,0,4,6,7</sub> |  | 2.6<br><sub>6,0,1,3,3</sub> |  | 4.8<br><sub>2,7,3,5,0</sub> |  | 0.9<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 14.6 |
| Jose Alvarado (NYK) | 80% | 17.2<br><sub>-,2,7,13,15</sub> | 7.1<br><sub>-,0,2,2,8</sub> |  | 2.3<br><sub>-,0,0,2,2</sub> |  | 2.9<br><sub>-,1,4,1,2</sub> |  | 0.9<br><sub>-,0,0,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 12.2 |
| Mohamed Diawara (NYK) | 38% | 16.0<br><sub>-,-,-,-,-</sub> | 6.2<br><sub>-,-,-,-,-</sub> |  | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 10.6 |
| Dalton Knecht (NYK) | 67% | 14.8<br><sub>-,-,-,-,3</sub> | 5.8<br><sub>-,-,-,-,0</sub> |  | 2.8<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 9.4 |
| Pacome Dadiet (NYK) | 52% | 14.1<br><sub>1,-,-,-,11</sub> | 5.8<br><sub>0,-,-,-,5</sub> |  | 2.5<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,2</sub> |  | 0.7<br><sub>0,-,-,-,1</sub> |  | 0.4 | 0.1 | 0.4 | 9.2 |
| Jaden Akins (NYK) | 38% | 8.9<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.2 |
| Tyler Nickel (NYK) | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |

</details>


### BOS @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW), Paul George (BOS), Mitchell Robinson (BOS)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 35.9<br><sub>38,30,36,37,-</sub> | 27.9<br><sub>24,32,24,24,-</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 8.5<br><sub>7,6,12,8,-</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>8,6,4,3,-</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,5,3,3,-</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.6 | 3.3 | 43.1 |
| Derrick White | 76% | 32.6<br><sub>38,23,32,35,-</sub> | 14.7<br><sub>19,16,9,12,-</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,4,3,3,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>7,2,2,8,-</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>3,4,1,0,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.9 | 1.7 | 23.3 |
| Payton Pritchard | 99% | 32.4<br><sub>31,19,32,30,34</sub> | 16.9<br><sub>14,10,21,15,9</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>1,1,4,1,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.9<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.4 | 25.5 |
| Neemias Queta | 99% | 28.2<br><sub>31,15,-,27,30</sub> | 12.1<br><sub>11,8,-,17,15</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 9.3<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>3,2,-,3,1</sub> |  | 0.2<br><sub>1,1,-,0,1</sub> |  | 0.8 | 1.3 | 1.4 | 23.6 |
| Sam Hauser | 99% | 27.9<br><sub>24,11,25,17,31</sub> | 10.4<br><sub>8,8,12,9,14</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,0,2,2,2</sub> |  | 2.2<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.3 | 0.5 | 16.2 |
| Baylor Scheierman | 99% | 19.8<br><sub>29,18,11,13,18</sub> | 5.8<br><sub>9,12,0,0,4</sub> | 7.5 · –<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>7,5,1,1,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.1 | 0.7 | 10.9 |
| Luka Garza | 98% | 16.3<br><sub>11,14,18,5,17</sub> | 7.4<br><sub>5,2,3,0,5</sub> |  | 3.8<br><sub>1,3,0,1,5</sub> |  | 1.5<br><sub>0,5,4,1,1</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 12.6 |
| Jordan Walsh | 98% | 15.1<br><sub>18,21,17,4,8</sub> | 4.4<br><sub>6,11,6,0,1</sub> |  | 2.9<br><sub>3,1,2,0,4</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.5<br><sub>0,2,2,0,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.1 |
| Hugo Gonzalez | 98% | 15.0<br><sub>8,18,4,16,17</sub> | 4.4<br><sub>0,9,0,2,5</sub> |  | 3.1<br><sub>1,5,2,6,4</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.5<br><sub>0,2,0,0,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.2 |
| Mike Conley | 48% | 14.1<br><sub>-,-,-,-,18</sub> | 4.9<br><sub>-,-,-,-,19</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,4</sub> |  | 0.7 | 0.2 | 0.6 | 8.4 |
| Chris Cenac Jr. | 67% | 13.9<br><sub>-,7,12,17,12</sub> | 5.2<br><sub>-,6,4,6,2</sub> |  | 3.1<br><sub>-,3,2,6,3</sub> |  | 0.5<br><sub>-,0,1,0,0</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.7 | 8.8 |
| Devin Carter | 93% | 13.0<br><sub>-,12,-,-,4</sub> | 5.3<br><sub>-,0,-,-,0</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 1.5<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 9.2 |
| Ron Harper Jr. | 58% | 11.6<br><sub>-,12,-,-,13</sub> | 4.3<br><sub>-,10,-,-,3</sub> |  | 1.6<br><sub>-,1,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,1</sub> |  | 0.6<br><sub>-,2,-,-,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.6 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 32.8<br><sub>36,24,33,30,33</sub> | 18.4<br><sub>25,3,28,13,11</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.7 | 2.7 | 29.3 |
| Brandin Podziemski | 97% | 32.7<br><sub>37,22,30,29,32</sub> | 16.2<br><sub>22,8,15,10,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.2 | 1.6 | 25.3 |
| Draymond Green | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.7 | 2.2 | 16.0 |
| Will Richard | 98% | 23.4<br><sub>19,30,23,27,27</sub> | 8.3<br><sub>9,7,11,20,15</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.2 | 0.8 | 12.4 |
| De'Anthony Melton | 99% | 23.2<br><sub>25,18,21,19,25</sub> | 10.5<br><sub>11,8,8,0,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.4 | 1.5 | 16.5 |
| Gui Santos | 96% | 19.0<br><sub>12,21,19,17,23</sub> | 8.0<br><sub>0,7,12,6,8</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>1,1,2,6,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.3 | 1.2 | 13.9 |
| Charles Bassey | 98% | 17.8<br><sub>13,20,16,22,25</sub> | 8.0<br><sub>7,11,4,10,16</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.2 |
| Gary Payton II | 88% | 17.6<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.1<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.1 |
| Georges Niang | 98% | 17.5<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> |  | 2.6<br><sub>5,3,4,1,2</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> |  | 0.3 | 0.1 | 0.8 | 11.3 |
| Al Horford | 98% | 16.8<br><sub>21,10,14,-,17</sub> | 5.5<br><sub>2,0,0,-,3</sub> | 5.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>1,3,5,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.3 | 0.7 | 0.6 | 10.8 |
| LJ Cryer | 88% | 14.7<br><sub>18,24,24,19,12</sub> | 6.7<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.5<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.7 | 9.4 |
| Graham Ike | 96% | 10.2<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.6 |
| Malevy Leons | 83% | 8.2<br><sub>4,14,6,7,4</sub> | 2.2<br><sub>0,5,2,2,0</sub> |  | 1.6<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-22/`._
