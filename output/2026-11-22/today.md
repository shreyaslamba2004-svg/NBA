# NBA model · Sun 22 Nov 2026 (US date)

Updated **Mon 23 Nov, 07:05 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-22/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray PTS over 39.5 (40+) | DEN @ CHI | draftkings | 18.40 | 16.92 | 9.55 | 10.5% | 5.1% | 5.9% | +8.7% | +92.7% | 0.1% |
| Jamal Murray PA over 44.5 (45+) | DEN @ CHI | draftkings | 13.20 | 12.32 | 7.22 | 13.9% | 7.1% | 8.1% | +7.2% | +82.9% | 0.1% |
| Jamal Murray PA over 49.5 (50+) | DEN @ CHI | draftkings | 24.00 | 22.42 | 13.21 | 7.6% | 3.9% | 4.5% | +7.0% | +81.7% | 0.1% |
| Jamal Murray PRA over 49.5 (50+) | DEN @ CHI | draftkings | 12.40 | 11.63 | 6.94 | 14.4% | 7.5% | 8.6% | +6.6% | +78.7% | 0.1% |
| Jamal Murray PRA over 54.5 (55+) | DEN @ CHI | draftkings | 22.00 | 20.70 | 12.45 | 8.0% | 4.2% | 4.8% | +6.3% | +76.7% | 0.1% |
| Anthony Davis AST over 5.5 (6+) | ORL @ WAS | draftkings | 19.80 | 18.83 | 11.67 | 8.6% | 4.7% | 5.3% | +5.2% | +69.7% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DET @ ATL | Mon 23 Nov 07:30 | 114.6–111.5 | DET 59% | 1.69 / 2.44 | ATL +3.5 | 225.5 | ATL +1.5 covers 44%; o223.5 55% |
| OKC @ MIA | Mon 23 Nov 10:00 | 117.2–117.4 | OKC 50% | 2.02 / 1.98 | MIA +0.5 | 234.5 | MIA -3.5 covers 41%; o231.5 56% |
| ORL @ WAS | Mon 23 Nov 11:00 | 119.5–111.9 | ORL 70% | 1.42 / 3.38 | WAS +7.5 | 231.5 | WAS +4.5 covers 41%; o220.5 72% |
| DEN @ CHI | Mon 23 Nov 11:00 | 123.8–115.9 | DEN 71% | 1.40 / 3.50 | CHI +8.5 | 239.5 | CHI +9.5 covers 54%; o235.5 58% |
| DAL @ UTA | Mon 23 Nov 11:00 | 119.4–117.9 | DAL 54% | 1.84 / 2.19 | UTA +1.5 | 236.5 | UTA +1.5 covers 49%; o226.5 72% |
| IND @ NYK | Mon 23 Nov 12:00 | 105.9–113.6 | IND 29% | 3.43 / 1.41 | NYK -7.5 | 219.5 | NYK -7.5 covers 51%; o213.5 62% |
| BOS @ GSW | Mon 23 Nov 12:30 | 109.3–105.5 | BOS 61% | 1.64 / 2.56 | GSW +4.5 | 214.5 | GSW +8.5 covers 63%; o210.5 59% |

### DET @ ATL
Out: Mouhamed Gueye (ATL), Jock Landale (ATL), CJ McCollum (ATL), Asa Newell (ATL), Jalen Wilson (ATL), Jalen Duren (DET), Taurean Prince (DET), Duncan Robinson (DET)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ausar Thompson PTS under 11.5 | DET @ ATL | tab | 1.95 | 1.93 | 1.61 | 62.0% | 50.0% | 51.8% | +1.1% | +21.1% | 0.3% |
| Dyson Daniels PTS under 10.5 | DET @ ATL | tab | 2.00 | 1.99 | 1.93 | 51.8% | 50.0% | 50.3% | +0.5% | +3.6% | 0.1% |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 100% | 35.3<br><sub>48,36,38,-,36</sub> | 26.7<br><sub>52,33,27,-,23</sub> | 25.5 · 25.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,5,5,-,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 8.4<br><sub>11,8,6,-,9</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,3,1,-,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3 | 0.8 | 4.0 | 40.0 |
| Daniss Jenkins | 100% | 33.0<br><sub>42,35,38,36,39</sub> | 15.3<br><sub>21,10,25,17,14</sub> | 15.5 · 16.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>6,1,5,4,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>0,5,5,9,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>3,1,3,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3 | 0.3 | 2.2 | 24.3 |
| Kevin Huerter | 100% | 31.3<br><sub>24,38,36,36,36</sub> | 12.7<br><sub>11,20,9,11,20</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>1,4,7,1,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>0,7,1,7,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.7<br><sub>1,2,0,1,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2 | 0.7 | 1.6 | 19.5 |
| Ausar Thompson | 100% | 29.0<br><sub>43,18,29,34,33</sub> | 10.6<br><sub>17,10,14,10,13</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>11,8,9,7,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>11,5,12,4,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.0 | 1.0 | 2.2 | 22.6 |
| John Collins | 100% | 25.9<br><sub>25,26,23,30,20</sub> | 11.6<br><sub>10,8,11,20,3</sub> | 11.5 · 10.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>4,7,1,7,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>0,0,0,2,1</sub> |  | 1.1<br><sub>2,2,1,4,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.7 | 1.4 | 18.3 |
| Paul Reed | 98% | 25.3<br><sub>38,23,25,20,28</sub> | 12.4<br><sub>13,9,10,17,8</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>11,9,6,7,7</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>3,1,5,1,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.1 | 1.7 | 22.4 |
| Javonte Green | 98% | 20.0<br><sub>15,12,23,35,23</sub> | 7.2<br><sub>5,5,6,18,12</sub> |  | 2.8<br><sub>1,1,6,7,1</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>1,0,0,3,3</sub> |  | 1.2 | 0.4 | 0.4 | 10.7 |
| Ronald Holland II | 98% | 15.1<br><sub>14,22,-,-,-</sub> | 5.7<br><sub>2,5,-,-,-</sub> |  | 3.2<br><sub>5,7,-,-,-</sub> |  | 1.1<br><sub>2,3,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.8 | 0.4 | 0.9 | 10.0 |
| Isaiah Joe | 96% | 14.6<br><sub>-,-,-,16,18</sub> | 7.6<br><sub>-,-,-,11,9</sub> | 8.5 · 9.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>-,-,-,2,1</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 1.1<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.5 | 0.1 | 0.7 | 10.1 |
| Chaz Lanier | 71% | 9.5<br><sub>-,-,25,16,6</sub> | 3.3<br><sub>-,-,3,9,0</sub> |  | 0.7<br><sub>-,-,3,1,0</sub> |  | 0.5<br><sub>-,-,1,0,0</sub> |  | 0.4<br><sub>-,-,1,3,0</sub> |  | 0.2 | 0.1 | 0.2 | 4.6 |
| Elijah Harkless | 52% | 7.4<br><sub>-,2,4,14,-</sub> | 2.5<br><sub>-,2,0,6,-</sub> |  | 1.1<br><sub>-,0,1,2,-</sub> |  | 0.8<br><sub>-,0,1,4,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 4.5 |
| Tolu Smith | 52% | 7.0<br><sub>-,1,-,3,-</sub> | 3.0<br><sub>-,3,-,3,-</sub> |  | 2.5<br><sub>-,2,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.9 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 100% | 35.7<br><sub>38,40,35,34,36</sub> | 21.4<br><sub>15,27,14,16,26</sub> | 20.5 · 21.5<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>7,11,11,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>4,10,5,11,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.6 | 3.5 | 37.5 |
| Nickeil Alexander-Walker | 100% | 33.8<br><sub>34,41,33,32,32</sub> | 19.7<br><sub>20,16,20,19,17</sub> | 19.5 · 20.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,6,5,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,3,4,7,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>4,1,2,3,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.5 | 2.2 | 26.1 |
| Onyeka Okongwu | 100% | 33.5<br><sub>30,35,36,36,34</sub> | 15.6<br><sub>16,17,16,28,16</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 8.2<br><sub>9,6,11,9,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>3,1,0,2,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 1.9<br><sub>2,2,3,5,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 1.1 | 1.8 | 26.3 |
| Dyson Daniels | 100% | 33.2<br><sub>31,36,27,37,35</sub> | 10.9<br><sub>10,6,9,10,11</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>6,9,10,10,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.5<br><sub>8,4,5,4,10</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 0.4<br><sub>1,0,0,0,1</sub> |  | 2.4 | 0.4 | 1.7 | 23.7 |
| Aaron Wiggins | 98% | 28.7<br><sub>23,26,24,26,34</sub> | 13.6<br><sub>15,9,7,14,19</sub> | 13.5 · 13.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>3,4,3,3,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>3,3,3,1,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.2<br><sub>4,1,1,4,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.4 | 1.5 | 19.2 |
| Luguentz Dort | 99% | 23.8<br><sub>18,20,18,31,23</sub> | 8.2<br><sub>4,10,3,16,2</sub> | 7.5 · 7.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,1,4,3,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>2,2,0,0,0</sub> |  | 1.2<br><sub>1,1,0,3,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.3 | 0.8 | 12.2 |
| Kingston Flemings | 100% | 23.0<br><sub>24,17,-,-,-</sub> | 8.2<br><sub>8,0,-,-,-</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,1,-,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>4,1,-,-,-</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>1,0,-,-,-</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.4 | 2.1 | 14.4 |
| Corey Kispert | 67% | 14.1<br><sub>-,-,16,17,16</sub> | 6.8<br><sub>-,-,14,8,7</sub> |  | 1.8<br><sub>-,-,3,1,3</sub> |  | 0.9<br><sub>-,-,1,2,0</sub> |  | 0.9<br><sub>-,-,3,2,1</sub> |  | 0.3 | 0.2 | 0.7 | 9.5 |
| RayJ Dennis | 80% | 12.9<br><sub>-,-,10,10,13</sub> | 5.5<br><sub>-,-,6,3,8</sub> |  | 1.9<br><sub>-,-,1,3,4</sub> |  | 2.2<br><sub>-,-,3,5,2</sub> |  | 0.6<br><sub>-,-,1,1,0</sub> |  | 0.5 | 0.2 | 0.9 | 9.6 |
| Zuby Ejiofor | 80% | 12.8<br><sub>4,-,12,12,14</sub> | 4.7<br><sub>0,-,4,3,5</sub> |  | 2.8<br><sub>0,-,3,3,2</sub> |  | 1.0<br><sub>0,-,0,0,2</sub> |  | 0.4<br><sub>0,-,1,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.4 |
| Dorian Finney-Smith | 52% | 6.4<br><sub>-,-,-,5,3</sub> | 1.6<br><sub>-,-,-,0,0</sub> |  | 1.0<br><sub>-,-,-,2,0</sub> |  | 0.3<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 2.9 |

</details>


### OKC @ MIA
Out: Keshad Johnson (MIA), Alex Caruso (OKC), Chet Holmgren (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.2–117.4 | OKC 50% | 2.02 / 1.98 | MIA +0.5 | 234.5 | MIA -3.5 covers 41%; o231.5 56% |
| Expected (weighted by chance each plays) | 119.2–117.8 | OKC 54% | 1.87 / 2.15 | MIA +1.5 | 236.5 | MIA -3.5 covers 38%; o231.5 61% |
| if Giannis Antetokounmpo plays | 117.3–119.5 | OKC 44% | 2.27 / 1.79 | MIA -2.5 | 236.5 | MIA -3.5 covers 47%; o231.5 61% |
| if Shai Gilgeous-Alexander plays | 121.2–115.7 | OKC 65% | 1.53 / 2.89 | MIA +5.5 | 236.5 | MIA -3.5 covers 27%; o231.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Giannis Antetokounmpo (MIA) | Questionable | 55% | 33.6 | 26.0 | 13.0 | 5.6 | 0.5 | 0.9 | 1.1 | 3.4 | 44.6 | full tables below |
| Shai Gilgeous-Alexander (OKC) | Questionable | 55% | 36.0 | 35.9 | 4.4 | 6.8 | 2.0 | 1.3 | 0.8 | 2.7 | 47.1 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jared McCain | 99% | 33.0<br><sub>31,31,30,33,30</sub> | 21.8<br><sub>10,23,12,18,18</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>6,4,1,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>3,2,1,1,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>2,7,1,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 2.1 | 28.5 |
| Ajay Mitchell | 98% | 32.4<br><sub>-,-,27,34,31</sub> | 22.8<br><sub>-,-,14,13,8</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>-,-,3,6,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.7<br><sub>-,-,5,6,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.3 | 2.2 | 32.7 |
| Kenrich Williams | 98% | 29.3<br><sub>26,35,19,23,28</sub> | 12.8<br><sub>11,8,10,10,6</sub> |  | 5.4<br><sub>2,8,1,5,2</sub> |  | 2.9<br><sub>2,4,2,1,4</sub> |  | 1.7<br><sub>2,0,2,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 21.1 |
| Aday Mara | 98% | 28.5<br><sub>32,21,26,27,29</sub> | 13.7<br><sub>11,10,16,10,22</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.4<br><sub>6,3,13,6,16</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,0,3,8,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.7 | 2.0 | 25.8 |
| Bennett Stirtz | 98% | 27.6<br><sub>25,12,17,17,25</sub> | 12.7<br><sub>6,5,0,6,18</sub> |  | 2.1<br><sub>1,1,1,0,2</sub> |  | 2.3<br><sub>1,0,2,2,2</sub> |  | 2.1<br><sub>2,1,0,2,4</sub> |  | 1.0 | 0.2 | 1.1 | 17.1 |
| Isaiah Hartenstein | 99% | 27.0<br><sub>34,30,18,27,28</sub> | 11.2<br><sub>20,21,3,6,5</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 11.6<br><sub>11,16,11,17,8</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>6,6,2,6,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.9 | 27.3 |
| Nique Clifford | 97% | 22.6<br><sub>16,12,24,13,15</sub> | 9.0<br><sub>5,0,9,7,4</sub> |  | 3.4<br><sub>3,0,3,0,5</sub> |  | 2.2<br><sub>1,0,0,0,1</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.3 | 1.1 | 14.6 |
| Micah Peavy | 91% | 20.5<br><sub>12,-,13,-,9</sub> | 6.9<br><sub>0,-,5,-,2</sub> |  | 3.7<br><sub>3,-,3,-,2</sub> |  | 0.9<br><sub>0,-,1,-,0</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Josh Dix | 58% | 19.5<br><sub>-,17,-,-,-</sub> | 7.6<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,4,-,-,-</sub> |  | 1.4<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Brooks Barnhizer | 48% | 11.4<br><sub>-,-,4,-,-</sub> | 3.0<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.4 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 99% | 36.5<br><sub>38,39,32,33,36</sub> | 16.6<br><sub>19,22,15,16,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,5,4,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 8.6<br><sub>8,17,9,10,6</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>3,3,3,1,6</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 2.6 | 28.4 |
| Bam Adebayo | 99% | 34.5<br><sub>37,38,36,16,30</sub> | 19.8<br><sub>11,37,20,4,26</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 9.5<br><sub>8,14,5,1,4</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>4,3,4,2,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,2,1,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.6 | 2.0 | 32.9 |
| Andrew Wiggins | 98% | 31.3<br><sub>19,32,23,34,26</sub> | 14.5<br><sub>13,8,10,17,11</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>0,3,2,5,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>0,4,1,1,2</sub> |  | 2.1<br><sub>2,1,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.9 | 1.5 | 21.2 |
| Pelle Larsson | 83% | 28.0<br><sub>31,-,-,-,15</sub> | 12.2<br><sub>14,-,-,-,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>7,-,-,-,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,-,-,-,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>2,-,-,-,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.2 | 1.9 | 19.3 |
| Klay Thompson | 88% | 26.2<br><sub>30,-,20,22,23</sub> | 14.2<br><sub>11,-,26,17,13</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,-,1,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.9<br><sub>2,-,4,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>2,-,6,5,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.6 | 1.1 | 18.1 |
| Ryan Conwell | 91% | 25.0<br><sub>21,33,26,30,26</sub> | 10.8<br><sub>5,20,9,14,13</sub> |  | 2.9<br><sub>4,5,4,2,3</sub> |  | 1.8<br><sub>2,2,1,3,1</sub> |  | 1.9<br><sub>1,4,2,1,3</sub> |  | 0.8 | 0.2 | 1.1 | 15.6 |
| Bobby Portis | 99% | 22.6<br><sub>17,15,18,23,17</sub> | 11.3<br><sub>5,5,7,16,9</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>1,3,4,6,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>1,2,2,0,0</sub> |  | 1.6<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.3 | 0.9 | 19.1 |
| Myron Gardner | 58% | 19.0<br><sub>10,19,26,24,-</sub> | 6.6<br><sub>4,0,5,14,-</sub> |  | 5.2<br><sub>3,4,9,2,-</sub> |  | 1.9<br><sub>1,2,3,3,-</sub> |  | 0.9<br><sub>0,0,1,4,-</sub> |  | 0.6 | 0.4 | 0.9 | 13.6 |
| Simone Fontecchio | 76% | 17.6<br><sub>7,7,14,19,18</sub> | 8.2<br><sub>3,0,7,10,6</sub> |  | 3.7<br><sub>0,0,5,6,5</sub> |  | 1.3<br><sub>0,2,0,2,1</sub> |  | 1.4<br><sub>0,0,1,2,2</sub> |  | 0.5 | 0.2 | 0.7 | 13.2 |
| Nikola Jovic | 58% | 16.0<br><sub>-,-,11,-,14</sub> | 6.1<br><sub>-,-,2,-,4</sub> |  | 3.0<br><sub>-,-,1,-,1</sub> |  | 1.7<br><sub>-,-,2,-,4</sub> |  | 0.8<br><sub>-,-,0,-,1</sub> |  | 0.5 | 0.4 | 0.8 | 10.8 |
| Tim Hardaway Jr. | 52% | 15.5<br><sub>-,20,-,-,-</sub> | 6.8<br><sub>-,4,-,-,-</sub> |  | 1.8<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 9.3 |
| Dru Smith | 38% | 11.3<br><sub>-,6,-,-,-</sub> | 4.1<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.2 | 0.6 | 7.4 |
| Nick Richards | 52% | 7.8<br><sub>-,-,-,3,1</sub> | 2.9<br><sub>-,-,-,0,0</sub> |  | 2.6<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.1 | 0.4 | 0.6 | 5.8 |
| Tre Donaldson | 76% | 6.9<br><sub>-,-,1,3,1</sub> | 2.9<br><sub>-,-,2,0,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 1.2 | 3.8 |

</details>

<details><summary>if Shai Gilgeous-Alexander plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 36.5<br><sub>38,39,32,33,36</sub> | 16.4<br><sub>19,22,15,16,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,5,4,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 8.6<br><sub>8,17,9,10,6</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>3,3,3,1,6</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 2.6 | 28.2 |
| Bam Adebayo (MIA) | 99% | 34.5<br><sub>37,38,36,16,30</sub> | 19.6<br><sub>11,37,20,4,26</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 9.5<br><sub>8,14,5,1,4</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>4,3,4,2,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,2,1,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.6 | 2.0 | 32.8 |
| Andrew Wiggins (MIA) | 98% | 31.3<br><sub>19,32,23,34,26</sub> | 14.3<br><sub>13,8,10,17,11</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>0,3,2,5,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>0,4,1,1,2</sub> |  | 2.1<br><sub>2,1,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.9 | 1.5 | 21.0 |
| Pelle Larsson (MIA) | 83% | 28.1<br><sub>31,-,-,-,15</sub> | 12.2<br><sub>14,-,-,-,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>7,-,-,-,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,-,-,-,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>2,-,-,-,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.2 | 1.9 | 19.2 |
| Klay Thompson (MIA) | 88% | 26.2<br><sub>30,-,20,22,23</sub> | 14.1<br><sub>11,-,26,17,13</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,-,1,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.9<br><sub>2,-,4,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>2,-,6,5,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.6 | 1.1 | 18.1 |
| Ryan Conwell (MIA) | 91% | 25.0<br><sub>21,33,26,30,26</sub> | 10.7<br><sub>5,20,9,14,13</sub> |  | 3.0<br><sub>4,5,4,2,3</sub> |  | 1.8<br><sub>2,2,1,3,1</sub> |  | 1.9<br><sub>1,4,2,1,3</sub> |  | 0.8 | 0.2 | 1.1 | 15.4 |
| Bobby Portis (MIA) | 99% | 22.6<br><sub>17,15,18,23,17</sub> | 11.2<br><sub>5,5,7,16,9</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>1,3,4,6,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>1,2,2,0,0</sub> |  | 1.6<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.3 | 0.9 | 19.0 |
| Myron Gardner (MIA) | 58% | 19.0<br><sub>10,19,26,24,-</sub> | 6.5<br><sub>4,0,5,14,-</sub> |  | 5.2<br><sub>3,4,9,2,-</sub> |  | 1.9<br><sub>1,2,3,3,-</sub> |  | 0.9<br><sub>0,0,1,4,-</sub> |  | 0.6 | 0.4 | 0.9 | 13.6 |
| Simone Fontecchio (MIA) | 76% | 17.6<br><sub>7,7,14,19,18</sub> | 8.2<br><sub>3,0,7,10,6</sub> |  | 3.7<br><sub>0,0,5,6,5</sub> |  | 1.3<br><sub>0,2,0,2,1</sub> |  | 1.4<br><sub>0,0,1,2,2</sub> |  | 0.5 | 0.2 | 0.7 | 13.1 |
| Nikola Jovic (MIA) | 58% | 15.9<br><sub>-,-,11,-,14</sub> | 6.1<br><sub>-,-,2,-,4</sub> |  | 3.0<br><sub>-,-,1,-,1</sub> |  | 1.7<br><sub>-,-,2,-,4</sub> |  | 0.8<br><sub>-,-,0,-,1</sub> |  | 0.5 | 0.4 | 0.8 | 10.8 |
| Tim Hardaway Jr. (MIA) | 52% | 15.5<br><sub>-,20,-,-,-</sub> | 6.8<br><sub>-,4,-,-,-</sub> |  | 1.8<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 9.3 |
| Dru Smith (MIA) | 38% | 11.2<br><sub>-,6,-,-,-</sub> | 4.0<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 7.4 |
| Nick Richards (MIA) | 52% | 7.8<br><sub>-,-,-,3,1</sub> | 2.9<br><sub>-,-,-,0,0</sub> |  | 2.6<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.1 | 0.3 | 0.6 | 5.8 |
| Tre Donaldson (MIA) | 76% | 7.0<br><sub>-,-,1,3,1</sub> | 2.9<br><sub>-,-,2,0,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 1.2 | 3.8 |
| Shai Gilgeous-Alexander (OKC) | 100% | 36.0<br><sub>36,39,30,36,37</sub> | 35.9<br><sub>31,40,37,34,40</sub> | 32.5 · – | 4.4<br><sub>4,4,2,5,3</sub> | 3.5 | 6.8<br><sub>2,5,2,3,8</sub> | 5.5 | 2.0<br><sub>0,2,4,1,4</sub> | 1.5 | 1.3 | 0.8 | 2.7 | 47.1 |
| Ajay Mitchell (OKC) | 98% | 31.2<br><sub>-,-,27,34,31</sub> | 17.9<br><sub>-,-,14,13,8</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>-,-,3,6,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.7<br><sub>-,-,5,6,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.3 | 1.8 | 26.7 |
| Jared McCain (OKC) | 99% | 30.9<br><sub>31,31,30,33,30</sub> | 16.9<br><sub>10,23,12,18,18</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>6,4,1,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>3,2,1,1,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>2,7,1,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.2 | 1.6 | 22.7 |
| Isaiah Hartenstein (OKC) | 99% | 27.5<br><sub>34,30,18,27,28</sub> | 9.6<br><sub>20,21,3,6,5</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 11.7<br><sub>11,16,11,17,8</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>6,6,2,6,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.7 | 25.1 |
| Aday Mara (OKC) | 98% | 27.2<br><sub>32,21,26,27,29</sub> | 11.0<br><sub>11,10,16,10,22</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.9<br><sub>6,3,13,6,16</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,0,3,8,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.7 | 1.7 | 22.1 |
| Kenrich Williams (OKC) | 98% | 25.8<br><sub>26,35,19,23,28</sub> | 9.7<br><sub>11,8,10,10,6</sub> |  | 4.9<br><sub>2,8,1,5,2</sub> |  | 2.3<br><sub>2,4,2,1,4</sub> |  | 1.3<br><sub>2,0,2,0,1</sub> |  | 0.9 | 0.2 | 1.0 | 16.8 |
| Bennett Stirtz (OKC) | 98% | 22.5<br><sub>25,12,17,17,25</sub> | 9.1<br><sub>6,5,0,6,18</sub> |  | 1.7<br><sub>1,1,1,0,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 1.5<br><sub>2,1,0,2,4</sub> |  | 0.9 | 0.2 | 0.8 | 12.5 |
| Nique Clifford (OKC) | 97% | 16.8<br><sub>16,12,24,13,15</sub> | 5.7<br><sub>5,0,9,7,4</sub> |  | 2.6<br><sub>3,0,3,0,5</sub> |  | 1.4<br><sub>1,0,0,0,1</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.8 | 9.7 |
| Micah Peavy (OKC) | 91% | 15.2<br><sub>12,-,13,-,9</sub> | 4.1<br><sub>0,-,5,-,2</sub> |  | 2.8<br><sub>3,-,3,-,2</sub> |  | 0.6<br><sub>0,-,1,-,0</sub> |  | 0.4<br><sub>0,-,1,-,0</sub> |  | 0.5 | 0.2 | 0.4 | 7.5 |
| Josh Dix (OKC) | 58% | 14.8<br><sub>-,17,-,-,-</sub> | 5.4<br><sub>-,0,-,-,-</sub> |  | 1.8<br><sub>-,4,-,-,-</sub> |  | 0.9<br><sub>-,3,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 8.1 |
| Brooks Barnhizer (OKC) | 48% | 8.3<br><sub>-,-,4,-,-</sub> | 2.0<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |

</details>

<details><summary>if Giannis Antetokounmpo plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 35.3<br><sub>38,39,32,33,36</sub> | 14.8<br><sub>19,22,15,16,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>5,5,4,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 8.1<br><sub>8,17,9,10,6</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>3,3,3,1,6</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 2.4 | 26.1 |
| Bam Adebayo (MIA) | 99% | 33.6<br><sub>37,38,36,16,30</sub> | 18.0<br><sub>11,37,20,4,26</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>8,14,5,1,4</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>4,3,4,2,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>0,2,1,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.6 | 1.7 | 30.4 |
| Giannis Antetokounmpo (MIA) | 100% | 33.6<br><sub>31,31,31,29,32</sub> | 26.0<br><sub>30,37,34,20,27</sub> | 26.5 · – | 13.0<br><sub>11,9,14,13,14</sub> | 12.5 | 5.6<br><sub>4,2,8,6,9</sub> | 5.5 | 0.5<br><sub>1,1,1,0,0</sub> | 0.5 | 0.9 | 1.1 | 3.4 | 44.6 |
| Andrew Wiggins (MIA) | 98% | 26.6<br><sub>19,32,23,34,26</sub> | 11.2<br><sub>13,8,10,17,11</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>0,3,2,5,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>0,4,1,1,2</sub> |  | 1.5<br><sub>2,1,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.8 | 1.2 | 16.6 |
| Pelle Larsson (MIA) | 83% | 24.6<br><sub>31,-,-,-,15</sub> | 9.9<br><sub>14,-,-,-,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>7,-,-,-,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>2,-,-,-,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>2,-,-,-,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.7 | 0.2 | 1.7 | 15.8 |
| Klay Thompson (MIA) | 88% | 22.4<br><sub>30,-,20,22,23</sub> | 12.1<br><sub>11,-,26,17,13</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,-,1,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5<br><sub>2,-,4,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>2,-,6,5,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.5 | 0.5 | 1.0 | 15.4 |
| Ryan Conwell (MIA) | 91% | 21.2<br><sub>21,33,26,30,26</sub> | 8.4<br><sub>5,20,9,14,13</sub> |  | 2.5<br><sub>4,5,4,2,3</sub> |  | 1.5<br><sub>2,2,1,3,1</sub> |  | 1.3<br><sub>1,4,2,1,3</sub> |  | 0.7 | 0.2 | 0.9 | 12.3 |
| Bobby Portis (MIA) | 99% | 18.1<br><sub>17,15,18,23,17</sub> | 8.5<br><sub>5,5,7,16,9</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>1,3,4,6,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>1,2,2,0,0</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.5 | 0.3 | 0.7 | 14.6 |
| Simone Fontecchio (MIA) | 76% | 11.9<br><sub>7,7,14,19,18</sub> | 5.5<br><sub>3,0,7,10,6</sub> |  | 2.4<br><sub>0,0,5,6,5</sub> |  | 0.9<br><sub>0,2,0,2,1</sub> |  | 0.8<br><sub>0,0,1,2,2</sub> |  | 0.3 | 0.1 | 0.5 | 8.8 |
| Nikola Jovic (MIA) | 58% | 11.4<br><sub>-,-,11,-,14</sub> | 4.4<br><sub>-,-,2,-,4</sub> |  | 2.1<br><sub>-,-,1,-,1</sub> |  | 1.2<br><sub>-,-,2,-,4</sub> |  | 0.5<br><sub>-,-,0,-,1</sub> |  | 0.3 | 0.3 | 0.6 | 7.7 |
| Tim Hardaway Jr. (MIA) | 52% | 10.1<br><sub>-,20,-,-,-</sub> | 4.2<br><sub>-,4,-,-,-</sub> |  | 1.1<br><sub>-,3,-,-,-</sub> |  | 0.5<br><sub>-,2,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.8 |
| Myron Gardner (MIA) | 58% | 9.3<br><sub>10,19,26,24,-</sub> | 3.1<br><sub>4,0,5,14,-</sub> |  | 2.5<br><sub>3,4,9,2,-</sub> |  | 0.9<br><sub>1,2,3,3,-</sub> |  | 0.3<br><sub>0,0,1,4,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.6 |
| Dru Smith (MIA) | 38% | 7.5<br><sub>-,6,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Nick Richards (MIA) | 52% | 5.7<br><sub>-,-,-,3,1</sub> | 2.1<br><sub>-,-,-,0,0</sub> |  | 2.0<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.3 |
| Tre Donaldson (MIA) | 76% | 5.3<br><sub>-,-,1,3,1</sub> | 2.4<br><sub>-,-,2,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.1 | 0.1 | 1.0 | 3.1 |
| Jared McCain (OKC) | 99% | 33.0<br><sub>31,31,30,33,30</sub> | 21.8<br><sub>10,23,12,18,18</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>6,4,1,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>3,2,1,1,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>2,7,1,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 2.1 | 28.5 |
| Ajay Mitchell (OKC) | 98% | 32.5<br><sub>-,-,27,34,31</sub> | 22.8<br><sub>-,-,14,13,8</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>-,-,3,6,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.7<br><sub>-,-,5,6,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.3 | 2.1 | 32.7 |
| Kenrich Williams (OKC) | 98% | 29.3<br><sub>26,35,19,23,28</sub> | 12.8<br><sub>11,8,10,10,6</sub> |  | 5.4<br><sub>2,8,1,5,2</sub> |  | 2.8<br><sub>2,4,2,1,4</sub> |  | 1.7<br><sub>2,0,2,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 21.0 |
| Aday Mara (OKC) | 98% | 28.6<br><sub>32,21,26,27,29</sub> | 13.7<br><sub>11,10,16,10,22</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.5<br><sub>6,3,13,6,16</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,0,3,8,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.7 | 2.0 | 25.9 |
| Bennett Stirtz (OKC) | 98% | 27.6<br><sub>25,12,17,17,25</sub> | 12.7<br><sub>6,5,0,6,18</sub> |  | 2.1<br><sub>1,1,1,0,2</sub> |  | 2.3<br><sub>1,0,2,2,2</sub> |  | 2.1<br><sub>2,1,0,2,4</sub> |  | 1.0 | 0.2 | 1.0 | 17.1 |
| Isaiah Hartenstein (OKC) | 99% | 27.1<br><sub>34,30,18,27,28</sub> | 11.1<br><sub>20,21,3,6,5</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 11.6<br><sub>11,16,11,17,8</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>6,6,2,6,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.9 | 27.3 |
| Nique Clifford (OKC) | 97% | 22.5<br><sub>16,12,24,13,15</sub> | 8.9<br><sub>5,0,9,7,4</sub> |  | 3.4<br><sub>3,0,3,0,5</sub> |  | 2.1<br><sub>1,0,0,0,1</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.3 | 1.1 | 14.5 |
| Micah Peavy (OKC) | 91% | 20.4<br><sub>12,-,13,-,9</sub> | 6.9<br><sub>0,-,5,-,2</sub> |  | 3.7<br><sub>3,-,3,-,2</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Josh Dix (OKC) | 58% | 19.4<br><sub>-,17,-,-,-</sub> | 7.7<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,4,-,-,-</sub> |  | 1.4<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Brooks Barnhizer (OKC) | 48% | 11.3<br><sub>-,-,4,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |

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
| Franz Wagner | 99% | 33.8<br><sub>39,36,38,36,36</sub> | 26.4<br><sub>38,35,21,27,35</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>8,9,8,8,5</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>1,12,9,11,7</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,3,0,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 2.7 | 39.3 |
| Desmond Bane | 98% | 32.8<br><sub>34,35,39,38,31</sub> | 19.9<br><sub>25,21,24,15,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,5,8,3,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>2,3,5,3,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.1<br><sub>7,6,3,5,7</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 1.7 | 27.5 |
| Anthony Black | 98% | 32.2<br><sub>39,37,33,37,37</sub> | 15.9<br><sub>22,5,20,15,13</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>7,2,2,2,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>8,5,7,6,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>3,1,3,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.7 | 2.3 | 25.2 |
| Wendell Carter Jr. | 99% | 30.0<br><sub>28,30,28,32,35</sub> | 13.2<br><sub>9,12,10,15,8</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 8.3<br><sub>7,8,3,8,8</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>3,0,1,3,2</sub> |  | 0.8<br><sub>0,1,1,2,0</sub> |  | 0.8 | 0.8 | 1.4 | 23.4 |
| Jalen Suggs | 98% | 28.1<br><sub>-,21,25,31,30</sub> | 12.1<br><sub>-,3,12,18,8</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>-,2,6,8,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.7<br><sub>-,3,4,4,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>-,1,2,5,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.6 | 0.6 | 2.2 | 20.7 |
| Tristan da Silva | 88% | 26.2<br><sub>-,31,31,27,24</sub> | 11.7<br><sub>-,12,13,12,6</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>-,6,6,2,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>-,2,3,0,2</sub> |  | 1.8<br><sub>-,2,3,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.3 | 1.0 | 17.3 |
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
| AJ Dybantsa | 98% | 36.3<br><sub>44,30,32,38,37</sub> | 16.9<br><sub>5,16,21,23,20</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>8,7,5,12,10</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>4,1,3,2,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,2,1,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.6 | 2.4 | 27.0 |
| Trae Young | 99% | 35.9<br><sub>45,26,33,32,35</sub> | 19.2<br><sub>37,0,13,11,16</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>2,1,2,1,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>14,8,12,8,5</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,0,2,1,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.2 | 3.4 | 31.3 |
| Anthony Davis | 99% | 35.7<br><sub>44,31,35,34,34</sub> | 23.3<br><sub>30,14,23,25,36</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 11.2<br><sub>15,8,4,14,11</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>4,5,0,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.7<br><sub>0,0,0,2,0</sub> |  | 1.2 | 1.7 | 2.3 | 37.3 |
| Kyshawn George | 99% | 35.3<br><sub>26,30,38,40,35</sub> | 17.3<br><sub>14,11,18,20,11</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>1,2,6,2,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>5,4,1,4,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 1.3 | 2.4 | 26.6 |
| Alex Sarr | 98% | 28.0<br><sub>44,27,31,22,20</sub> | 11.9<br><sub>30,25,6,13,3</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>9,9,4,2,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,2,1,3,0</sub> |  | 1.3<br><sub>4,3,1,3,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 1.8 | 1.5 | 20.8 |
| Bilal Coulibaly | 99% | 25.6<br><sub>29,21,16,26,24</sub> | 8.2<br><sub>4,9,11,3,2</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>7,2,5,8,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,0,0,2,0</sub> |  | 0.7<br><sub>0,1,1,0,0</sub> |  | 1.1 | 0.9 | 1.1 | 13.9 |
| Khris Middleton | 64% | 20.2<br><sub>-,9,18,20,28</sub> | 6.8<br><sub>-,8,9,8,5</sub> |  | 2.9<br><sub>-,0,3,4,2</sub> |  | 1.9<br><sub>-,2,3,1,3</sub> |  | 0.8<br><sub>-,2,2,1,0</sub> |  | 0.6 | 0.1 | 1.2 | 11.6 |
| Tre Johnson | 96% | 16.5<br><sub>30,-,21,8,4</sub> | 6.6<br><sub>13,-,9,0,2</sub> |  | 1.6<br><sub>4,-,1,2,1</sub> |  | 0.8<br><sub>2,-,3,0,0</sub> |  | 0.8<br><sub>1,-,2,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 9.0 |
| Will Riley | 88% | 10.9<br><sub>3,16,2,10,6</sub> | 4.7<br><sub>3,14,2,0,0</sub> |  | 1.4<br><sub>0,3,1,3,1</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>1,2,0,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.8 |
| Anthony Gill | 48% | 8.0<br><sub>-,6,2,-,-</sub> | 2.9<br><sub>-,5,2,-,-</sub> |  | 1.3<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |
| Tre Mann | 52% | 6.8<br><sub>-,11,2,-,-</sub> | 2.6<br><sub>-,4,2,-,-</sub> |  | 0.8<br><sub>-,1,0,-,-</sub> |  | 0.7<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.2 |

</details>


### DEN @ CHI
Out: Tobe Awaka (CHI), Norman Powell (CHI), Caleb Wilson (CHI), Bryce Hopkins (DEN), Julian Strawther (DEN), Cam Whitmore (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 123.8–115.9 | DEN 71% | 1.40 / 3.50 | CHI +8.5 | 239.5 | CHI +9.5 covers 54%; o235.5 58% |
| Expected (weighted by chance each plays) | 123.7–115.9 | DEN 71% | 1.40 / 3.50 | CHI +7.5 | 239.5 | CHI +9.5 covers 55%; o235.5 58% |
| if Nic Claxton plays | 123.5–115.9 | DEN 71% | 1.41 / 3.43 | CHI +7.5 | 239.5 | CHI +9.5 covers 55%; o235.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nic Claxton (CHI) | Questionable | 55% | 23.2 | 10.0 | 6.1 | 2.4 | 0.0 | 0.6 | 0.8 | 1.1 | 18.5 | full tables below |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.2<br><sub>37,37,38,39,38</sub> | 28.9<br><sub>27,26,28,24,26</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 12.6<br><sub>11,8,15,8,7</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>8,10,7,9,11</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7 | 0.8 | 3.4 | 51.6 |
| Jamal Murray | 98% | 36.5<br><sub>32,38,35,38,36</sub> | 26.2<br><sub>30,23,28,21,14</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>4,7,4,7,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>8,9,4,2,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,0,1,2,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.6 | 2.1 | 37.4 |
| Christian Braun | 98% | 33.1<br><sub>37,28,33,35,31</sub> | 12.7<br><sub>12,17,10,15,19</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>5,7,3,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>4,1,3,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>2,1,2,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.4 | 0.9 | 20.0 |
| Aaron Gordon | 98% | 30.1<br><sub>27,33,24,31,31</sub> | 14.0<br><sub>9,11,11,13,18</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>3,5,1,8,3</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>1,1,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.4 | 1.2 | 22.1 |
| Cameron Johnson | 98% | 30.0<br><sub>30,31,27,26,29</sub> | 14.0<br><sub>23,12,9,8,19</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,5,0,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,2,1,1,6</sub> |  | 1.8<br><sub>4,1,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.0 | 20.5 |
| DeMar DeRozan | 91% | 22.4<br><sub>20,24,14,25,22</sub> | 11.7<br><sub>8,9,2,18,15</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,3,1,2,2</sub> |  | 3.0<br><sub>4,2,1,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.0 | 16.8 |
| Spencer Jones | 91% | 16.4<br><sub>22,12,21,17,18</sub> | 4.0<br><sub>3,4,4,2,3</sub> |  | 2.3<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>0,1,3,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.6 | 7.2 |
| Trevon Brazile | 98% | 14.9<br><sub>13,16,23,11,11</sub> | 4.7<br><sub>7,5,9,0,4</sub> |  | 3.8<br><sub>5,3,4,6,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 9.1 |
| Marvin Bagley III | 98% | 12.7<br><sub>12,13,10,9,10</sub> | 6.5<br><sub>4,7,4,4,10</sub> |  | 4.0<br><sub>2,7,2,3,6</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.6 | 0.6 | 11.2 |
| Tyus Jones | 98% | 11.7<br><sub>11,10,10,9,14</sub> | 3.0<br><sub>0,2,0,0,5</sub> |  | 1.0<br><sub>1,0,1,0,3</sub> |  | 2.1<br><sub>4,3,2,0,4</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.4 | 6.1 |
| Zeke Nnaji | 23% | 7.2<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.4 |
| Alpha Diallo | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Ryan Nembhard | 48% | 6.0<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matas Buzelis | 99% | 31.0<br><sub>29,30,31,30,25</sub> | 18.8<br><sub>11,18,23,25,9</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>6,9,3,5,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,2,0,4,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>3,2,3,5,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 1.0 | 2.2 | 27.1 |
| Isaac Okoro | 99% | 31.0<br><sub>41,31,32,25,29</sub> | 11.6<br><sub>15,9,13,12,9</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,7,6,3,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>2,4,2,4,1</sub> |  | 1.4<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.4 | 1.0 | 17.5 |
| Josh Giddey | 99% | 30.4<br><sub>39,26,24,28,23</sub> | 15.3<br><sub>15,8,4,18,2</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>10,8,4,14,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 8.7<br><sub>14,5,8,9,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>3,2,1,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.5 | 3.0 | 30.8 |
| Jalen Smith | 92% | 28.6<br><sub>32,-,28,21,-</sub> | 16.3<br><sub>15,-,17,14,-</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 8.8<br><sub>12,-,11,6,-</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,-,3,3,-</sub> |  | 2.1<br><sub>1,-,3,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.9 | 1.2 | 27.2 |
| Tre Jones | 99% | 25.3<br><sub>15,24,23,16,25</sub> | 14.6<br><sub>4,16,16,10,12</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,0,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>3,4,6,6,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.6<br><sub>0,1,0,0,0</sub> |  | 1.0 | 0.2 | 1.3 | 22.7 |
| Patrick Williams | 82% | 25.0<br><sub>24,26,13,13,23</sub> | 9.3<br><sub>13,14,0,2,6</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>4,5,0,1,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>2,1,0,2,1</sub> |  | 1.3<br><sub>4,2,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.5 | 1.1 | 14.9 |
| Buddy Hield | 88% | 22.6<br><sub>25,20,19,19,23</sub> | 11.1<br><sub>12,16,6,11,15</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>3,4,4,1,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>3,2,2,2,0</sub> |  | 1.9<br><sub>2,4,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.3 | 1.0 | 16.2 |
| Zach Collins | 71% | 17.5<br><sub>-,28,-,11,15</sub> | 7.5<br><sub>-,8,-,3,6</sub> |  | 4.9<br><sub>-,5,-,2,2</sub> |  | 1.9<br><sub>-,4,-,0,4</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.5 | 0.4 | 0.9 | 14.2 |
| Noa Essengue | 98% | 16.2<br><sub>8,7,14,15,15</sub> | 6.4<br><sub>5,0,1,5,8</sub> |  | 3.5<br><sub>1,1,2,3,4</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.6<br><sub>1,0,0,0,2</sub> |  | 0.5 | 0.2 | 0.8 | 10.8 |
| Leonard Miller | 64% | 15.7<br><sub>-,17,1,7,-</sub> | 7.4<br><sub>-,4,0,4,-</sub> |  | 3.8<br><sub>-,3,0,2,-</sub> |  | 1.0<br><sub>-,4,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 12.2 |
| Jordan Hawkins | 52% | 13.6<br><sub>-,-,4,-,-</sub> | 6.1<br><sub>-,-,0,-,-</sub> |  | 1.7<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 8.6 |
| Orlando Robinson | 30% | 13.2<br><sub>-,-,-,-,-</sub> | 5.4<br><sub>-,-,-,-,-</sub> |  | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 10.6 |
| Dailyn Swain | 67% | 8.4<br><sub>-,-,2,6,-</sub> | 3.3<br><sub>-,-,0,2,-</sub> |  | 1.4<br><sub>-,-,1,1,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.5 |

</details>

<details><summary>if Nic Claxton plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matas Buzelis (CHI) | 99% | 29.7<br><sub>29,30,31,30,25</sub> | 17.9<br><sub>11,18,23,25,9</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>6,9,3,5,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,2,0,4,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>3,2,3,5,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 1.0 | 2.2 | 25.9 |
| Josh Giddey (CHI) | 99% | 29.2<br><sub>39,26,24,28,23</sub> | 13.8<br><sub>15,8,4,18,2</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>10,8,4,14,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 8.4<br><sub>14,5,8,9,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>3,2,1,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.5 | 2.8 | 29.0 |
| Isaac Okoro (CHI) | 99% | 28.8<br><sub>41,31,32,25,29</sub> | 10.7<br><sub>15,9,13,12,9</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,7,6,3,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>2,4,2,4,1</sub> |  | 1.2<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.4 | 0.9 | 16.0 |
| Jalen Smith (CHI) | 92% | 27.7<br><sub>32,-,28,21,-</sub> | 15.4<br><sub>15,-,17,14,-</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 8.8<br><sub>12,-,11,6,-</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>3,-,3,3,-</sub> |  | 2.0<br><sub>1,-,3,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.6 | 0.9 | 1.2 | 26.1 |
| Tre Jones (CHI) | 99% | 23.5<br><sub>15,24,23,16,25</sub> | 13.8<br><sub>4,16,16,10,12</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,0,2,2,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>3,4,6,6,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 1.0 | 0.2 | 1.3 | 21.3 |
| Nic Claxton (CHI) | 100% | 23.2<br><sub>22,-,17,22,29</sub> | 10.0<br><sub>2,-,8,14,11</sub> |  | 6.1<br><sub>6,-,2,4,7</sub> |  | 2.4<br><sub>2,-,1,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.8 | 1.1 | 18.5 |
| Patrick Williams (CHI) | 82% | 23.1<br><sub>24,26,13,13,23</sub> | 8.5<br><sub>13,14,0,2,6</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>4,5,0,1,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,1,0,2,1</sub> |  | 1.1<br><sub>4,2,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.4 | 1.0 | 13.7 |
| Buddy Hield (CHI) | 88% | 20.3<br><sub>25,20,19,19,23</sub> | 10.4<br><sub>12,16,6,11,15</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,4,4,1,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>3,2,2,2,0</sub> |  | 1.7<br><sub>2,4,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.2 | 1.0 | 14.9 |
| Zach Collins (CHI) | 71% | 15.9<br><sub>-,28,-,11,15</sub> | 6.9<br><sub>-,8,-,3,6</sub> |  | 4.5<br><sub>-,5,-,2,2</sub> |  | 1.7<br><sub>-,4,-,0,4</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.4 | 0.8 | 13.1 |
| Noa Essengue (CHI) | 98% | 14.0<br><sub>8,7,14,15,15</sub> | 5.6<br><sub>5,0,1,5,8</sub> |  | 3.1<br><sub>1,1,2,3,4</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>1,0,0,0,2</sub> |  | 0.5 | 0.2 | 0.7 | 9.4 |
| Leonard Miller (CHI) | 64% | 13.2<br><sub>-,17,1,7,-</sub> | 6.3<br><sub>-,4,0,4,-</sub> |  | 3.2<br><sub>-,3,0,2,-</sub> |  | 0.8<br><sub>-,4,0,0,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.6 | 10.4 |
| Jordan Hawkins (CHI) | 52% | 10.7<br><sub>-,-,4,-,-</sub> | 4.8<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.8 |
| Orlando Robinson (CHI) | 30% | 9.8<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 8.0 |
| Dailyn Swain (CHI) | 67% | 6.7<br><sub>-,-,2,6,-</sub> | 2.9<br><sub>-,-,0,2,-</sub> |  | 1.0<br><sub>-,-,1,1,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.5 |
| Nikola Jokic (DEN) | 98% | 37.3<br><sub>37,37,38,39,38</sub> | 28.9<br><sub>27,26,28,24,26</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 12.6<br><sub>11,8,15,8,7</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>8,10,7,9,11</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7 | 0.8 | 3.4 | 51.7 |
| Jamal Murray (DEN) | 98% | 36.6<br><sub>32,38,35,38,36</sub> | 26.3<br><sub>30,23,28,21,14</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>4,7,4,7,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>8,9,4,2,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,0,1,2,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.6 | 2.1 | 37.4 |
| Christian Braun (DEN) | 98% | 33.2<br><sub>37,28,33,35,31</sub> | 12.7<br><sub>12,17,10,15,19</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>5,7,3,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>4,1,3,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>2,1,2,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.4 | 0.9 | 20.0 |
| Aaron Gordon (DEN) | 98% | 30.1<br><sub>27,33,24,31,31</sub> | 14.0<br><sub>9,11,11,13,18</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>3,5,1,8,3</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>1,1,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.4 | 1.2 | 22.0 |
| Cameron Johnson (DEN) | 98% | 30.0<br><sub>30,31,27,26,29</sub> | 13.9<br><sub>23,12,9,8,19</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,5,0,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,2,1,1,6</sub> |  | 1.8<br><sub>4,1,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.0 | 20.4 |
| DeMar DeRozan (DEN) | 91% | 22.4<br><sub>20,24,14,25,22</sub> | 11.7<br><sub>8,9,2,18,15</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,3,1,2,2</sub> |  | 3.0<br><sub>4,2,1,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.0 | 16.8 |
| Spencer Jones (DEN) | 91% | 16.5<br><sub>22,12,21,17,18</sub> | 4.0<br><sub>3,4,4,2,3</sub> |  | 2.3<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>0,1,3,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.6 | 7.2 |
| Trevon Brazile (DEN) | 98% | 15.0<br><sub>13,16,23,11,11</sub> | 4.7<br><sub>7,5,9,0,4</sub> |  | 3.9<br><sub>5,3,4,6,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 9.1 |
| Marvin Bagley III (DEN) | 98% | 12.7<br><sub>12,13,10,9,10</sub> | 6.5<br><sub>4,7,4,4,10</sub> |  | 4.0<br><sub>2,7,2,3,6</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.6 | 0.6 | 11.2 |
| Tyus Jones (DEN) | 98% | 11.7<br><sub>11,10,10,9,14</sub> | 3.0<br><sub>0,2,0,0,5</sub> |  | 1.0<br><sub>1,0,1,0,3</sub> |  | 2.1<br><sub>4,3,2,0,4</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Zeke Nnaji (DEN) | 23% | 7.2<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.5 |
| Alpha Diallo (DEN) | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Ryan Nembhard (DEN) | 48% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>


### DAL @ UTA
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.4–117.9 | DAL 54% | 1.84 / 2.19 | UTA +1.5 | 236.5 | UTA +1.5 covers 49%; o226.5 72% |
| Expected (weighted by chance each plays) | 119.8–117.8 | DAL 55% | 1.82 / 2.22 | UTA +2.5 | 237.5 | UTA +1.5 covers 48%; o226.5 72% |
| if Walter Clayton Jr. plays | 119.9–117.8 | DAL 56% | 1.79 / 2.27 | UTA +2.5 | 237.5 | UTA +1.5 covers 47%; o226.5 72% |
| if P.J. Washington plays | 119.6–117.7 | DAL 55% | 1.81 / 2.24 | UTA +2.5 | 237.5 | UTA +1.5 covers 47%; o226.5 72% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walter Clayton Jr. (DAL) | Questionable | 55% | 22.1 | 8.6 | 3.5 | 3.4 | 1.2 | 0.9 | 0.2 | 1.5 | 15.5 | full tables below |
| P.J. Washington (DAL) | Doubtful | 20% | 31.2 | 14.3 | 7.0 | 1.6 | 1.8 | 1.0 | 1.0 | 1.4 | 22.9 | full tables below |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 99% | 35.9<br><sub>27,38,27,34,36</sub> | 26.2<br><sub>12,18,17,33,22</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 7.2<br><sub>7,8,3,5,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.2<br><sub>3,5,4,9,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,0,2,3,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.7 | 0.9 | 2.8 | 39.5 |
| Kyrie Irving | 98% | 35.7<br><sub>27,37,-,29,35</sub> | 26.6<br><sub>10,34,-,17,25</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>3,6,-,6,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 4.7<br><sub>4,5,-,5,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,7,-,1,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.5 | 2.2 | 35.7 |
| Daniel Gafford | 99% | 27.8<br><sub>16,17,19,24,31</sub> | 11.7<br><sub>3,10,3,6,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>3,3,4,6,10</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,1,2,2,3</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.9 | 2.1 | 1.2 | 21.4 |
| Naji Marshall | 96% | 27.3<br><sub>23,30,23,27,14</sub> | 13.6<br><sub>13,12,13,12,4</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>1,3,2,5,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>4,5,2,2,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,0,3,2,0</sub> |  | 1.3 | 0.1 | 1.6 | 21.2 |
| Zaccharie Risacher | 98% | 26.9<br><sub>25,14,27,18,29</sub> | 9.8<br><sub>22,5,18,3,11</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>6,2,5,3,7</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>3,0,0,0,1</sub> |  | 1.2<br><sub>4,1,1,1,1</sub> |  | 1.1 | 0.9 | 1.0 | 16.7 |
| Caleb Martin | 98% | 24.6<br><sub>21,33,34,20,20</sub> | 6.5<br><sub>7,15,12,8,0</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>2,8,5,5,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>5,3,5,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>1,1,4,2,0</sub> |  | 1.1 | 0.4 | 0.8 | 12.8 |
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
| Keyonte George | 99% | 35.0<br><sub>38,34,35,39,36</sub> | 24.1<br><sub>27,13,30,30,14</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>4,4,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.5<br><sub>7,8,11,10,6</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>4,1,4,5,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 3.2 | 35.9 |
| Darryn Peterson | 98% | 31.6<br><sub>34,34,31,19,32</sub> | 18.6<br><sub>28,17,13,11,20</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>7,5,5,1,10</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>2,4,2,3,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>4,3,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 2.0 | 27.8 |
| Ace Bailey | 99% | 30.7<br><sub>35,30,23,27,24</sub> | 15.5<br><sub>21,7,5,19,7</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>3,8,1,8,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,4,4,3,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.1<br><sub>3,1,1,2,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.9 | 1.8 | 23.3 |
| Jaxson Hayes | 88% | 25.4<br><sub>13,-,-,25,28</sub> | 10.7<br><sub>12,-,-,6,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,-,-,7,14</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,-,-,2,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.9 |
| Josh Green | 97% | 24.4<br><sub>14,15,13,28,29</sub> | 6.2<br><sub>2,6,9,11,8</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 31% · u 69%</sub> | 0.9 | 0.2 | 0.8 | 10.0 |
| Brice Sensabaugh | 99% | 23.9<br><sub>27,30,35,14,26</sub> | 15.6<br><sub>7,14,40,8,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.2<br><sub>1,0,8,0,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.3 | 1.9 | 21.8 |
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
| Cooper Flagg (DAL) | 99% | 34.9<br><sub>27,38,27,34,36</sub> | 25.2<br><sub>12,18,17,33,22</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>7,8,3,5,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.0<br><sub>3,5,4,9,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,0,2,3,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.9 | 2.7 | 38.1 |
| Kyrie Irving (DAL) | 98% | 34.5<br><sub>27,37,-,29,35</sub> | 24.5<br><sub>10,34,-,17,25</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>3,6,-,6,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 4.4<br><sub>4,5,-,5,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,7,-,1,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.5 | 2.1 | 33.3 |
| P.J. Washington (DAL) | 100% | 31.2<br><sub>16,26,25,25,-</sub> | 14.3<br><sub>10,10,8,21,-</sub> |  | 7.0<br><sub>3,4,5,5,-</sub> |  | 1.6<br><sub>0,1,4,2,-</sub> |  | 1.8<br><sub>1,2,0,5,-</sub> |  | 1.0 | 1.0 | 1.4 | 22.9 |
| Daniel Gafford (DAL) | 99% | 23.9<br><sub>16,17,19,24,31</sub> | 10.1<br><sub>3,10,3,6,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>3,3,4,6,10</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>1,1,2,2,3</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.8 | 1.8 | 1.1 | 18.6 |
| Naji Marshall (DAL) | 96% | 23.0<br><sub>23,30,23,27,14</sub> | 11.0<br><sub>13,12,13,12,4</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>1,3,2,5,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>4,5,2,2,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.8<br><sub>1,0,3,2,0</sub> |  | 1.0 | 0.1 | 1.5 | 17.3 |
| Zaccharie Risacher (DAL) | 98% | 22.1<br><sub>25,14,27,18,29</sub> | 8.0<br><sub>22,5,18,3,11</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>6,2,5,3,7</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>3,0,0,0,1</sub> |  | 0.9<br><sub>4,1,1,1,1</sub> |  | 0.9 | 0.8 | 0.9 | 13.6 |
| Caleb Martin (DAL) | 98% | 20.2<br><sub>21,33,34,20,20</sub> | 5.0<br><sub>7,15,12,8,0</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,8,5,5,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>5,3,5,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.5<br><sub>1,1,4,2,0</sub> |  | 0.9 | 0.4 | 0.7 | 10.2 |
| Max Christie (DAL) | 98% | 17.6<br><sub>7,-,-,8,24</sub> | 6.8<br><sub>3,-,-,5,13</sub> |  | 2.2<br><sub>2,-,-,1,4</sub> |  | 1.0<br><sub>0,-,-,2,0</sub> |  | 1.0<br><sub>1,-,-,1,3</sub> |  | 0.5 | 0.3 | 0.7 | 10.0 |
| Morez Johnson Jr. (DAL) | 99% | 15.8<br><sub>13,15,26,15,17</sub> | 5.9<br><sub>0,4,2,3,9</sub> |  | 3.3<br><sub>2,2,6,1,7</sub> |  | 1.4<br><sub>0,0,4,1,2</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.2 | 0.9 | 10.6 |
| Santi Aldama (DAL) | 98% | 12.9<br><sub>10,16,-,6,9</sub> | 6.1<br><sub>3,7,-,0,0</sub> |  | 3.1<br><sub>1,2,-,0,1</sub> |  | 1.0<br><sub>1,1,-,0,0</sub> |  | 0.7<br><sub>1,2,-,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 10.2 |
| Marcus Sasser (DAL) | 58% | 11.0<br><sub>9,-,18,4,-</sub> | 4.0<br><sub>3,-,5,0,-</sub> |  | 1.0<br><sub>1,-,1,2,-</sub> |  | 1.3<br><sub>0,-,2,1,-</sub> |  | 0.5<br><sub>0,-,1,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Moussa Cisse (DAL) | 58% | 7.0<br><sub>8,-,4,4,-</sub> | 2.5<br><sub>0,-,1,0,-</sub> |  | 2.7<br><sub>0,-,1,1,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.6 | 0.3 | 5.4 |
| Jett Howard (DAL) | 63% | 6.5<br><sub>5,-,7,-,-</sub> | 2.9<br><sub>3,-,0,-,-</sub> |  | 0.8<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |
| Keyonte George (UTA) | 99% | 35.0<br><sub>38,34,35,39,36</sub> | 24.2<br><sub>27,13,30,30,14</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>4,4,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.5<br><sub>7,8,11,10,6</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,1,4,5,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 3.2 | 36.0 |
| Darryn Peterson (UTA) | 98% | 31.7<br><sub>34,34,31,19,32</sub> | 18.6<br><sub>28,17,13,11,20</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>7,5,5,1,10</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>2,4,2,3,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>4,3,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 2.0 | 27.8 |
| Ace Bailey (UTA) | 99% | 30.7<br><sub>35,30,23,27,24</sub> | 15.6<br><sub>21,7,5,19,7</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>3,8,1,8,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,4,4,3,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.1<br><sub>3,1,1,2,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.9 | 1.7 | 23.4 |
| Jaxson Hayes (UTA) | 88% | 25.3<br><sub>13,-,-,25,28</sub> | 10.6<br><sub>12,-,-,6,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,-,-,7,14</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,-,-,2,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.8 |
| Josh Green (UTA) | 97% | 24.3<br><sub>14,15,13,28,29</sub> | 6.3<br><sub>2,6,9,11,8</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 31% · u 69%</sub> | 0.9 | 0.2 | 0.8 | 10.0 |
| Brice Sensabaugh (UTA) | 99% | 23.9<br><sub>27,30,35,14,26</sub> | 15.5<br><sub>7,14,40,8,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.2<br><sub>1,0,8,0,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.9 | 21.7 |
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
| Cooper Flagg (DAL) | 99% | 35.4<br><sub>27,38,27,34,36</sub> | 25.6<br><sub>12,18,17,33,22</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 7.2<br><sub>7,8,3,5,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.0<br><sub>3,5,4,9,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,0,2,3,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.7 | 0.9 | 2.7 | 38.7 |
| Kyrie Irving (DAL) | 98% | 34.7<br><sub>27,37,-,29,35</sub> | 24.4<br><sub>10,34,-,17,25</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>3,6,-,6,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 4.3<br><sub>4,5,-,5,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,7,-,1,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.5 | 2.1 | 33.1 |
| Daniel Gafford (DAL) | 99% | 25.9<br><sub>16,17,19,24,31</sub> | 11.1<br><sub>3,10,3,6,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 7.4<br><sub>3,3,4,6,10</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,1,2,2,3</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.8 | 2.0 | 1.2 | 20.2 |
| Naji Marshall (DAL) | 96% | 24.9<br><sub>23,30,23,27,14</sub> | 12.3<br><sub>13,12,13,12,4</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,3,2,5,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>4,5,2,2,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>1,0,3,2,0</sub> |  | 1.1 | 0.1 | 1.5 | 19.1 |
| Zaccharie Risacher (DAL) | 98% | 24.3<br><sub>25,14,27,18,29</sub> | 8.9<br><sub>22,5,18,3,11</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>6,2,5,3,7</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>3,0,0,0,1</sub> |  | 1.1<br><sub>4,1,1,1,1</sub> |  | 1.0 | 0.8 | 0.9 | 15.2 |
| Caleb Martin (DAL) | 98% | 22.3<br><sub>21,33,34,20,20</sub> | 5.7<br><sub>7,15,12,8,0</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>2,8,5,5,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>5,3,5,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.6<br><sub>1,1,4,2,0</sub> |  | 1.0 | 0.4 | 0.8 | 11.3 |
| Walter Clayton Jr. (DAL) | 100% | 22.1<br><sub>22,13,23,27,25</sub> | 8.6<br><sub>5,2,13,8,16</sub> |  | 3.5<br><sub>1,2,4,2,5</sub> |  | 3.4<br><sub>4,2,3,7,1</sub> |  | 1.2<br><sub>0,0,3,2,2</sub> |  | 0.9 | 0.2 | 1.5 | 15.5 |
| Max Christie (DAL) | 98% | 18.1<br><sub>7,-,-,8,24</sub> | 6.8<br><sub>3,-,-,5,13</sub> |  | 2.2<br><sub>2,-,-,1,4</sub> |  | 1.0<br><sub>0,-,-,2,0</sub> |  | 1.0<br><sub>1,-,-,1,3</sub> |  | 0.6 | 0.3 | 0.7 | 10.1 |
| Morez Johnson Jr. (DAL) | 99% | 17.4<br><sub>13,15,26,15,17</sub> | 6.5<br><sub>0,4,2,3,9</sub> |  | 3.6<br><sub>2,2,6,1,7</sub> |  | 1.5<br><sub>0,0,4,1,2</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.2 | 0.9 | 11.6 |
| Santi Aldama (DAL) | 98% | 14.2<br><sub>10,16,-,6,9</sub> | 6.6<br><sub>3,7,-,0,0</sub> |  | 3.4<br><sub>1,2,-,0,1</sub> |  | 1.1<br><sub>1,1,-,0,0</sub> |  | 0.7<br><sub>1,2,-,0,0</sub> |  | 0.5 | 0.4 | 0.7 | 11.1 |
| Marcus Sasser (DAL) | 58% | 11.9<br><sub>9,-,18,4,-</sub> | 4.4<br><sub>3,-,5,0,-</sub> |  | 1.1<br><sub>1,-,1,2,-</sub> |  | 1.4<br><sub>0,-,2,1,-</sub> |  | 0.5<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.1 | 0.6 | 6.9 |
| Moussa Cisse (DAL) | 58% | 7.7<br><sub>8,-,4,4,-</sub> | 2.5<br><sub>0,-,1,0,-</sub> |  | 2.9<br><sub>0,-,1,1,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 5.6 |
| Jett Howard (DAL) | 63% | 6.9<br><sub>5,-,7,-,-</sub> | 2.9<br><sub>3,-,0,-,-</sub> |  | 0.9<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.3<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.2 |
| Keyonte George (UTA) | 99% | 35.0<br><sub>38,34,35,39,36</sub> | 24.1<br><sub>27,13,30,30,14</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>4,4,2,1,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.5<br><sub>7,8,11,10,6</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,1,4,5,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 3.2 | 35.9 |
| Darryn Peterson (UTA) | 98% | 31.6<br><sub>34,34,31,19,32</sub> | 18.6<br><sub>28,17,13,11,20</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>7,5,5,1,10</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>2,4,2,3,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>4,3,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 2.0 | 27.7 |
| Ace Bailey (UTA) | 99% | 30.7<br><sub>35,30,23,27,24</sub> | 15.5<br><sub>21,7,5,19,7</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>3,8,1,8,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,4,4,3,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.0<br><sub>3,1,1,2,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.9 | 1.8 | 23.3 |
| Jaxson Hayes (UTA) | 88% | 25.4<br><sub>13,-,-,25,28</sub> | 10.7<br><sub>12,-,-,6,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,-,-,7,14</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,-,-,2,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.8 |
| Josh Green (UTA) | 97% | 24.4<br><sub>14,15,13,28,29</sub> | 6.2<br><sub>2,6,9,11,8</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 31% · u 69%</sub> | 0.9 | 0.2 | 0.8 | 9.9 |
| Brice Sensabaugh (UTA) | 99% | 23.9<br><sub>27,30,35,14,26</sub> | 15.6<br><sub>7,14,40,8,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.2<br><sub>1,0,8,0,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.9 | 21.8 |
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
| Andrew Nembhard | 91% | 34.2<br><sub>34,34,-,-,26</sub> | 17.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 2.8 | 28.8 |
| Aaron Nesmith | 93% | 31.8<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.6 | 20.3 |
| Kelly Oubre Jr. | 91% | 27.8<br><sub>34,30,29,23,23</sub> | 12.7<br><sub>14,16,16,17,17</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.3<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.3 | 18.3 |
| Ivica Zubac | 88% | 27.4<br><sub>31,26,22,24,27</sub> | 11.9<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.5 | 23.1 |
| Quenton Jackson | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 0.9 | 0.2 | 1.6 | 18.1 |
| Obi Toppin | 88% | 24.0<br><sub>16,16,14,17,26</sub> | 12.8<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,3,2,1,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.2 | 19.5 |
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
| Jalen Brunson | 99% | 35.5<br><sub>36,41,34,35,36</sub> | 31.8<br><sub>33,28,31,21,30</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>1,1,5,2,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.2 | 2.3 | 41.9 |
| Landry Shamet | 99% | 33.3<br><sub>21,30,24,30,36</sub> | 14.9<br><sub>5,23,12,10,20</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,2,1,1,1</sub> |  | 2.1<br><sub>1,0,1,2,3</sub> |  | 2.6<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 1.0 | 19.5 |
| Josh Hart | 98% | 32.1<br><sub>23,26,31,28,35</sub> | 10.9<br><sub>0,0,5,11,0</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>5,5,4,6,8</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.6 | 22.8 |
| Mikal Bridges | 99% | 31.3<br><sub>29,32,30,31,28</sub> | 13.5<br><sub>18,5,17,8,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.5 | 1.2 | 20.3 |
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
| Andrew Nembhard (IND) | 91% | 34.2<br><sub>34,34,-,-,26</sub> | 17.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.2 | 2.8 | 28.9 |
| Aaron Nesmith (IND) | 93% | 31.7<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.6 | 20.4 |
| Kelly Oubre Jr. (IND) | 91% | 27.7<br><sub>34,30,29,23,23</sub> | 12.7<br><sub>14,16,16,17,17</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.3<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.6 | 1.3 | 18.4 |
| Ivica Zubac (IND) | 88% | 27.4<br><sub>31,26,22,24,27</sub> | 12.0<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.5 | 23.1 |
| Quenton Jackson (IND) | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.1<br><sub>1,1,1,2,1</sub> |  | 0.9 | 0.2 | 1.6 | 18.1 |
| Obi Toppin (IND) | 88% | 24.1<br><sub>16,16,14,17,26</sub> | 12.9<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,3,2,1,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.2 | 19.6 |
| Jarace Walker (IND) | 88% | 20.1<br><sub>7,-,14,17,11</sub> | 8.4<br><sub>1,-,2,1,8</sub> |  | 4.1<br><sub>1,-,5,3,1</sub> |  | 2.0<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.5 |
| Jalen Slawson (IND) | 91% | 17.8<br><sub>12,10,14,12,14</sub> | 5.5<br><sub>2,1,8,5,4</sub> |  | 3.5<br><sub>3,4,5,4,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.6 |
| Braden Smith (IND) | 67% | 16.4<br><sub>-,-,-,18,11</sub> | 5.6<br><sub>-,-,-,8,5</sub> |  | 1.7<br><sub>-,-,-,5,3</sub> |  | 3.1<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.8 | 10.5 |
| Jay Huff (IND) | 91% | 15.8<br><sub>11,8,18,15,1</sub> | 6.8<br><sub>6,8,11,5,0</sub> |  | 2.8<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.9<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.7 |
| Larry Nance Jr. (IND) | 97% | 15.3<br><sub>5,14,7,9,11</sub> | 5.1<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.6<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.8 |
| Kobe Brown (IND) | 86% | 14.4<br><sub>-,-,3,2,-</sub> | 5.1<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.8 |
| Jalen Brunson (NYK) | 99% | 35.5<br><sub>36,41,34,35,36</sub> | 31.1<br><sub>33,28,31,21,30</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>1,1,5,2,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.2 | 2.2 | 41.4 |
| Karl-Anthony Towns (NYK) | 100% | 33.8<br><sub>34,43,36,33,-</sub> | 22.2<br><sub>23,28,16,22,-</sub> | 20.5 · – | 14.5<br><sub>15,17,16,12,-</sub> | 12.5 | 4.5<br><sub>5,3,8,4,-</sub> | 3.5 | 1.9<br><sub>3,3,1,2,-</sub> | 1.5 | 1.1 | 0.7 | 2.7 | 41.1 |
| Josh Hart (NYK) | 98% | 30.9<br><sub>23,26,31,28,35</sub> | 9.3<br><sub>0,0,5,11,0</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>5,5,4,6,8</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.3 | 20.5 |
| Landry Shamet (NYK) | 99% | 30.6<br><sub>21,30,24,30,36</sub> | 12.1<br><sub>5,23,12,10,20</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>3,2,1,1,1</sub> |  | 1.9<br><sub>1,0,1,2,3</sub> |  | 2.2<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 0.8 | 16.1 |
| Mikal Bridges (NYK) | 99% | 29.4<br><sub>29,32,30,31,28</sub> | 11.5<br><sub>18,5,17,8,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.5 | 1.0 | 17.8 |
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
| Pascal Siakam (IND) | 100% | 33.8<br><sub>32,32,34,33,30</sub> | 21.5<br><sub>28,19,31,24,21</sub> | 20.5 · – | 6.1<br><sub>8,3,2,4,7</sub> | 6.5 | 3.8<br><sub>5,2,2,3,2</sub> | 2.5 | 1.6<br><sub>2,2,0,2,2</sub> | 1.5 | 0.9 | 0.4 | 2.0 | 31.4 |
| Andrew Nembhard (IND) | 91% | 33.1<br><sub>34,34,-,-,26</sub> | 15.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>10,6,-,-,8</sub> | 6.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 2.3 | 26.3 |
| Aaron Nesmith (IND) | 93% | 29.2<br><sub>22,33,36,29,29</sub> | 11.7<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,7,4,3,10</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>1,1,4,3,7</sub> |  | 1.7<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.2 | 17.6 |
| Ivica Zubac (IND) | 88% | 26.1<br><sub>31,26,22,24,27</sub> | 11.1<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>12,13,5,3,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.4 | 21.1 |
| Kelly Oubre Jr. (IND) | 91% | 25.3<br><sub>34,30,29,23,23</sub> | 10.8<br><sub>14,16,16,17,17</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,5,4,4,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,0,2,0,0</sub> |  | 1.1<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.5 | 1.1 | 15.9 |
| Quenton Jackson (IND) | 98% | 21.1<br><sub>21,20,30,22,18</sub> | 8.9<br><sub>4,3,15,15,3</sub> |  | 2.9<br><sub>2,5,6,2,2</sub> |  | 3.0<br><sub>2,4,8,3,2</sub> |  | 0.9<br><sub>1,1,1,2,1</sub> |  | 0.8 | 0.2 | 1.3 | 14.8 |
| Obi Toppin (IND) | 88% | 19.6<br><sub>16,16,14,17,26</sub> | 10.1<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,3,2,1,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>1,1,1,1,2</sub> |  | 1.2<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.5 | 0.2 | 0.9 | 15.5 |
| Jarace Walker (IND) | 88% | 15.6<br><sub>7,-,14,17,11</sub> | 6.0<br><sub>1,-,2,1,8</sub> |  | 3.2<br><sub>1,-,5,3,1</sub> |  | 1.4<br><sub>0,-,2,1,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.3 | 0.8 | 10.5 |
| Jalen Slawson (IND) | 91% | 13.4<br><sub>12,10,14,12,14</sub> | 3.9<br><sub>2,1,8,5,4</sub> |  | 2.7<br><sub>3,4,5,4,2</sub> |  | 1.2<br><sub>1,0,2,2,2</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 0.6 | 7.7 |
| Braden Smith (IND) | 67% | 13.3<br><sub>-,-,-,18,11</sub> | 4.3<br><sub>-,-,-,8,5</sub> |  | 1.4<br><sub>-,-,-,5,3</sub> |  | 2.5<br><sub>-,-,-,3,5</sub> |  | 0.3<br><sub>-,-,-,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Jay Huff (IND) | 91% | 11.9<br><sub>11,8,18,15,1</sub> | 4.9<br><sub>6,8,11,5,0</sub> |  | 2.1<br><sub>4,1,0,3,0</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.6<br><sub>0,2,3,0,0</sub> |  | 0.2 | 0.7 | 0.5 | 7.7 |
| Larry Nance Jr. (IND) | 97% | 11.7<br><sub>5,14,7,9,11</sub> | 3.7<br><sub>5,2,4,3,7</sub> |  | 2.1<br><sub>0,2,2,1,2</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.4<br><sub>1,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Kobe Brown (IND) | 86% | 9.3<br><sub>-,-,3,2,-</sub> | 3.1<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| Jalen Brunson (NYK) | 99% | 35.6<br><sub>36,41,34,35,36</sub> | 31.9<br><sub>33,28,31,21,30</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>1,1,5,2,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>11,9,5,7,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,3,4,4,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.2 | 2.3 | 42.0 |
| Landry Shamet (NYK) | 99% | 33.3<br><sub>21,30,24,30,36</sub> | 15.0<br><sub>5,23,12,10,20</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,2,1,1,1</sub> |  | 2.1<br><sub>1,0,1,2,3</sub> |  | 2.7<br><sub>1,4,2,2,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 1.0 | 19.6 |
| Josh Hart (NYK) | 98% | 32.0<br><sub>23,26,31,28,35</sub> | 10.8<br><sub>0,0,5,11,0</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>5,5,4,6,8</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>4,2,2,2,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,0,1,3,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 1.5 | 22.7 |
| Mikal Bridges (NYK) | 99% | 31.3<br><sub>29,32,30,31,28</sub> | 13.6<br><sub>18,5,17,8,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,7,5,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,3,1,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,0,2,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.6 | 1.2 | 20.4 |
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
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.3–105.5 | BOS 61% | 1.64 / 2.56 | GSW +4.5 | 214.5 | GSW +8.5 covers 63%; o210.5 59% |
| Expected (weighted by chance each plays) | 112.3–105.3 | BOS 69% | 1.44 / 3.27 | GSW +7.5 | 217.5 | GSW +8.5 covers 54%; o210.5 65% |
| if Derrick White plays | 110.8–104.9 | BOS 66% | 1.51 / 2.96 | GSW +6.5 | 215.5 | GSW +8.5 covers 57%; o210.5 61% |
| if Jayson Tatum plays | 111.6–105.2 | BOS 68% | 1.48 / 3.10 | GSW +6.5 | 216.5 | GSW +8.5 covers 56%; o210.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White (BOS) | Day-To-Day | 70% | 32.4 | 15.6 | 3.8 | 5.3 | 2.2 | 1.1 | 0.9 | 1.9 | 24.8 | full tables below |
| Jayson Tatum (BOS) | Day-To-Day | 70% | 35.5 | 26.2 | 8.4 | 6.9 | 3.2 | 1.1 | 0.5 | 3.1 | 41.5 | full tables below |
| Mitchell Robinson (BOS) | Day-To-Day | 70% | 18.1 | 5.3 | 6.7 | 1.0 | 0.0 | 0.8 | 0.9 | 0.9 | 13.0 | small |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George | 98% | 33.4<br><sub>-,25,36,23,37</sub> | 22.7<br><sub>-,7,22,10,19</sub> |  | 5.7<br><sub>-,7,8,4,8</sub> |  | 4.5<br><sub>-,6,3,1,5</sub> |  | 3.2<br><sub>-,1,5,1,2</sub> |  | 1.8 | 0.5 | 2.9 | 32.9 |
| Payton Pritchard | 99% | 33.2<br><sub>31,19,32,30,34</sub> | 18.7<br><sub>14,10,21,15,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>1,1,4,1,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.9<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.1 | 1.8 | 28.5 |
| Sam Hauser | 99% | 30.1<br><sub>24,11,25,17,31</sub> | 12.0<br><sub>8,8,12,9,14</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,0,2,2,2</sub> |  | 2.5<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.3 | 0.5 | 18.6 |
| Neemias Queta | 99% | 28.8<br><sub>31,15,-,27,30</sub> | 12.7<br><sub>11,8,-,17,15</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.7<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,2,-,3,1</sub> |  | 0.3<br><sub>1,1,-,0,1</sub> |  | 0.8 | 1.3 | 1.6 | 24.8 |
| Baylor Scheierman | 99% | 24.3<br><sub>29,18,11,13,18</sub> | 7.8<br><sub>9,12,0,0,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,5,1,1,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>3,3,1,1,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.2<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.1 | 1.0 | 14.4 |
| Hugo Gonzalez | 98% | 20.1<br><sub>8,18,4,16,17</sub> | 6.1<br><sub>0,9,0,2,5</sub> |  | 4.2<br><sub>1,5,2,6,4</sub> |  | 1.1<br><sub>0,2,0,0,1</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.8 | 0.4 | 0.9 | 11.3 |
| Jordan Walsh | 98% | 19.8<br><sub>18,21,17,4,8</sub> | 6.0<br><sub>6,11,6,0,1</sub> |  | 3.8<br><sub>3,1,2,0,4</sub> |  | 1.1<br><sub>0,0,0,0,0</sub> |  | 0.7<br><sub>0,2,2,0,0</sub> |  | 0.8 | 0.3 | 0.7 | 10.9 |
| Luka Garza | 98% | 18.9<br><sub>11,14,18,5,17</sub> | 8.7<br><sub>5,2,3,0,5</sub> |  | 4.4<br><sub>1,3,0,1,5</sub> |  | 2.0<br><sub>0,5,4,1,1</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.5 | 0.8 | 15.1 |
| Mike Conley | 48% | 17.8<br><sub>-,-,-,-,18</sub> | 6.7<br><sub>-,-,-,-,19</sub> |  | 2.1<br><sub>-,-,-,-,4</sub> |  | 2.7<br><sub>-,-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,-,4</sub> |  | 0.9 | 0.2 | 0.8 | 11.4 |
| Chris Cenac Jr. | 67% | 16.3<br><sub>-,7,12,17,12</sub> | 6.6<br><sub>-,6,4,6,2</sub> |  | 3.7<br><sub>-,3,2,6,3</sub> |  | 0.6<br><sub>-,0,1,0,0</sub> |  | 0.5<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.9 | 10.9 |
| Ron Harper Jr. | 58% | 15.2<br><sub>-,12,-,-,13</sub> | 5.9<br><sub>-,10,-,-,3</sub> |  | 2.0<br><sub>-,1,-,-,0</sub> |  | 1.1<br><sub>-,0,-,-,1</sub> |  | 0.9<br><sub>-,2,-,-,1</sub> |  | 0.5 | 0.2 | 0.5 | 8.9 |
| Devin Carter | 93% | 15.0<br><sub>-,12,-,-,4</sub> | 6.2<br><sub>-,0,-,-,0</sub> |  | 2.7<br><sub>-,2,-,-,2</sub> |  | 2.0<br><sub>-,1,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.8 | 0.2 | 1.1 | 10.9 |
| Dillon Mitchell | 35% | 9.5<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.3 |
| Amari Williams | 23% | 7.9<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.6 | 4.8 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 32.8<br><sub>36,24,33,30,33</sub> | 18.4<br><sub>25,3,28,13,11</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.7 | 2.7 | 29.3 |
| Brandin Podziemski | 97% | 32.6<br><sub>37,22,30,29,32</sub> | 16.1<br><sub>22,8,15,10,15</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 1.6 | 25.2 |
| Draymond Green | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.7 | 2.2 | 16.1 |
| Will Richard | 98% | 23.5<br><sub>19,30,23,27,27</sub> | 8.4<br><sub>9,7,11,20,15</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.9 | 12.6 |
| De'Anthony Melton | 99% | 23.2<br><sub>25,18,21,19,25</sub> | 10.5<br><sub>11,8,8,0,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.4 | 1.5 | 16.5 |
| Gui Santos | 96% | 19.2<br><sub>12,21,19,17,23</sub> | 8.1<br><sub>0,7,12,6,8</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,1,2,6,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.3 | 1.2 | 14.0 |
| Charles Bassey | 98% | 17.8<br><sub>13,20,16,22,25</sub> | 8.0<br><sub>7,11,4,10,16</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.1 |
| Gary Payton II | 88% | 17.6<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.1<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.1 |
| Georges Niang | 98% | 17.4<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> |  | 2.5<br><sub>5,3,4,1,2</sub> |  | 1.1<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> |  | 0.3 | 0.1 | 0.8 | 11.2 |
| Al Horford | 98% | 16.7<br><sub>21,10,14,-,17</sub> | 5.5<br><sub>2,0,0,-,3</sub> |  | 3.5<br><sub>1,3,5,-,2</sub> |  | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.7 | 0.5 | 10.7 |
| LJ Cryer | 88% | 14.8<br><sub>18,24,24,19,12</sub> | 6.8<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.6<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.7 | 9.5 |
| Graham Ike | 96% | 10.2<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.6 |
| Malevy Leons | 83% | 8.2<br><sub>4,14,6,7,4</sub> | 2.3<br><sub>0,5,2,2,0</sub> |  | 1.6<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |

</details>

<details><summary>if Jayson Tatum plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 100% | 35.5<br><sub>38,30,36,37,-</sub> | 26.2<br><sub>24,32,24,24,-</sub> | 27.5 · – | 8.4<br><sub>7,6,12,8,-</sub> | 7.5 | 6.9<br><sub>8,6,4,3,-</sub> | 6.5 | 3.2<br><sub>2,5,3,3,-</sub> | 2.5 | 1.1 | 0.5 | 3.1 | 41.5 |
| Paul George (BOS) | 98% | 32.3<br><sub>-,25,36,23,37</sub> | 19.5<br><sub>-,7,22,10,19</sub> |  | 5.4<br><sub>-,7,8,4,8</sub> |  | 3.7<br><sub>-,6,3,1,5</sub> |  | 2.9<br><sub>-,1,5,1,2</sub> |  | 1.7 | 0.5 | 2.4 | 28.6 |
| Payton Pritchard (BOS) | 99% | 32.0<br><sub>31,19,32,30,34</sub> | 15.2<br><sub>14,10,21,15,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>1,1,4,1,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.1<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.1 | 1.4 | 24.1 |
| Neemias Queta (BOS) | 99% | 27.5<br><sub>31,15,-,27,30</sub> | 11.0<br><sub>11,8,-,17,15</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.0<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,-,3,1</sub> |  | 0.2<br><sub>1,1,-,0,1</sub> |  | 0.7 | 1.3 | 1.3 | 22.1 |
| Sam Hauser (BOS) | 99% | 25.9<br><sub>24,11,25,17,31</sub> | 9.3<br><sub>8,8,12,9,14</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>0,0,2,2,2</sub> |  | 1.9<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.2 | 0.4 | 14.7 |
| Baylor Scheierman (BOS) | 99% | 20.4<br><sub>29,18,11,13,18</sub> | 5.7<br><sub>9,12,0,0,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>7,5,1,1,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>3,3,1,1,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.1 | 0.7 | 11.1 |
| Hugo Gonzalez (BOS) | 98% | 15.9<br><sub>8,18,4,16,17</sub> | 4.4<br><sub>0,9,0,2,5</sub> |  | 3.2<br><sub>1,5,2,6,4</sub> |  | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.5<br><sub>0,2,0,0,1</sub> |  | 0.6 | 0.3 | 0.7 | 8.5 |
| Luka Garza (BOS) | 98% | 15.5<br><sub>11,14,18,5,17</sub> | 6.7<br><sub>5,2,3,0,5</sub> |  | 3.5<br><sub>1,3,0,1,5</sub> |  | 1.4<br><sub>0,5,4,1,1</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 11.7 |
| Jordan Walsh (BOS) | 98% | 15.3<br><sub>18,21,17,4,8</sub> | 4.2<br><sub>6,11,6,0,1</sub> |  | 2.9<br><sub>3,1,2,0,4</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.5<br><sub>0,2,2,0,0</sub> |  | 0.6 | 0.2 | 0.5 | 7.9 |
| Mike Conley (BOS) | 48% | 14.9<br><sub>-,-,-,-,18</sub> | 4.9<br><sub>-,-,-,-,19</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 2.1<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,4</sub> |  | 0.8 | 0.2 | 0.7 | 8.6 |
| Ron Harper Jr. (BOS) | 58% | 12.1<br><sub>-,12,-,-,13</sub> | 4.5<br><sub>-,10,-,-,3</sub> |  | 1.5<br><sub>-,1,-,-,0</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.6<br><sub>-,2,-,-,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.9 |
| Devin Carter (BOS) | 93% | 12.0<br><sub>-,12,-,-,4</sub> | 4.6<br><sub>-,0,-,-,0</sub> |  | 2.1<br><sub>-,2,-,-,2</sub> |  | 1.5<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.1 | 0.8 | 8.2 |
| Chris Cenac Jr. (BOS) | 67% | 11.9<br><sub>-,7,12,17,12</sub> | 4.5<br><sub>-,6,4,6,2</sub> |  | 2.7<br><sub>-,3,2,6,3</sub> |  | 0.4<br><sub>-,0,1,0,0</sub> |  | 0.3<br><sub>-,0,0,1,0</sub> |  | 0.3 | 0.2 | 0.7 | 7.6 |
| Dillon Mitchell (BOS) | 35% | 7.5<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.0 |
| Amari Williams (BOS) | 23% | 6.7<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 4.2 |
| Yaxel Lendeborg (GSW) | 98% | 32.8<br><sub>36,24,33,30,33</sub> | 18.4<br><sub>25,3,28,13,11</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.7 | 2.7 | 29.3 |
| Brandin Podziemski (GSW) | 97% | 32.6<br><sub>37,22,30,29,32</sub> | 16.1<br><sub>22,8,15,10,15</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 1.6 | 25.2 |
| Draymond Green (GSW) | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.7 | 2.2 | 16.0 |
| Will Richard (GSW) | 98% | 23.5<br><sub>19,30,23,27,27</sub> | 8.4<br><sub>9,7,11,20,15</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.8 | 12.5 |
| De'Anthony Melton (GSW) | 99% | 23.1<br><sub>25,18,21,19,25</sub> | 10.4<br><sub>11,8,8,0,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.4 | 1.5 | 16.5 |
| Gui Santos (GSW) | 96% | 19.1<br><sub>12,21,19,17,23</sub> | 8.0<br><sub>0,7,12,6,8</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>1,1,2,6,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.3 | 1.2 | 13.9 |
| Charles Bassey (GSW) | 98% | 18.0<br><sub>13,20,16,22,25</sub> | 8.1<br><sub>7,11,4,10,16</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.3 |
| Georges Niang (GSW) | 98% | 17.5<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> |  | 2.6<br><sub>5,3,4,1,2</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> |  | 0.3 | 0.1 | 0.8 | 11.2 |
| Gary Payton II (GSW) | 88% | 17.5<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.0<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.1 |
| Al Horford (GSW) | 98% | 16.9<br><sub>21,10,14,-,17</sub> | 5.5<br><sub>2,0,0,-,3</sub> |  | 3.5<br><sub>1,3,5,-,2</sub> |  | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.7 | 0.5 | 10.9 |
| LJ Cryer (GSW) | 88% | 14.8<br><sub>18,24,24,19,12</sub> | 6.8<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.5<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.7 | 9.5 |
| Graham Ike (GSW) | 96% | 10.2<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 7.6 |
| Malevy Leons (GSW) | 83% | 8.3<br><sub>4,14,6,7,4</sub> | 2.3<br><sub>0,5,2,2,0</sub> |  | 1.6<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |

</details>

<details><summary>if Derrick White plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George (BOS) | 98% | 32.6<br><sub>-,25,36,23,37</sub> | 21.8<br><sub>-,7,22,10,19</sub> |  | 5.5<br><sub>-,7,8,4,8</sub> |  | 4.1<br><sub>-,6,3,1,5</sub> |  | 3.1<br><sub>-,1,5,1,2</sub> |  | 1.8 | 0.5 | 2.6 | 31.4 |
| Derrick White (BOS) | 100% | 32.4<br><sub>38,23,32,35,-</sub> | 15.6<br><sub>19,16,9,12,-</sub> | 14.5 · – | 3.8<br><sub>1,4,3,3,-</sub> | 3.5 | 5.3<br><sub>7,2,2,8,-</sub> | 5.5 | 2.2<br><sub>3,4,1,0,-</sub> | 2.5 | 1.1 | 0.9 | 1.9 | 24.8 |
| Payton Pritchard (BOS) | 99% | 31.5<br><sub>31,19,32,30,34</sub> | 17.1<br><sub>14,10,21,15,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>1,1,4,1,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.3<br><sub>1,6,5,2,8</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,2,4,3,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.1 | 1.6 | 26.0 |
| Neemias Queta (BOS) | 99% | 27.8<br><sub>31,15,-,27,30</sub> | 12.1<br><sub>11,8,-,17,15</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>13,6,-,10,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>3,2,-,3,1</sub> |  | 0.2<br><sub>1,1,-,0,1</sub> |  | 0.8 | 1.3 | 1.5 | 23.6 |
| Sam Hauser (BOS) | 99% | 27.3<br><sub>24,11,25,17,31</sub> | 10.4<br><sub>8,8,12,9,14</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>9,1,1,2,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,0,2,2,2</sub> |  | 2.2<br><sub>2,2,4,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.2 | 0.5 | 16.4 |
| Baylor Scheierman (BOS) | 99% | 19.7<br><sub>29,18,11,13,18</sub> | 6.1<br><sub>9,12,0,0,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>7,5,1,1,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9<br><sub>3,2,0,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.1 | 0.8 | 11.4 |
| Luka Garza (BOS) | 98% | 16.2<br><sub>11,14,18,5,17</sub> | 7.5<br><sub>5,2,3,0,5</sub> |  | 3.8<br><sub>1,3,0,1,5</sub> |  | 1.6<br><sub>0,5,4,1,1</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4 | 0.4 | 0.7 | 12.9 |
| Hugo Gonzalez (BOS) | 98% | 14.6<br><sub>8,18,4,16,17</sub> | 4.4<br><sub>0,9,0,2,5</sub> |  | 3.1<br><sub>1,5,2,6,4</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.5<br><sub>0,2,0,0,1</sub> |  | 0.6 | 0.3 | 0.7 | 8.2 |
| Jordan Walsh (BOS) | 98% | 14.5<br><sub>18,21,17,4,8</sub> | 4.4<br><sub>6,11,6,0,1</sub> |  | 2.9<br><sub>3,1,2,0,4</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.5<br><sub>0,2,2,0,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.0 |
| Mike Conley (BOS) | 48% | 13.5<br><sub>-,-,-,-,18</sub> | 4.9<br><sub>-,-,-,-,19</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 2.0<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,4</sub> |  | 0.7 | 0.2 | 0.6 | 8.4 |
| Chris Cenac Jr. (BOS) | 67% | 13.3<br><sub>-,7,12,17,12</sub> | 5.1<br><sub>-,6,4,6,2</sub> |  | 3.0<br><sub>-,3,2,6,3</sub> |  | 0.5<br><sub>-,0,1,0,0</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.7 | 8.6 |
| Devin Carter (BOS) | 93% | 12.4<br><sub>-,12,-,-,4</sub> | 5.4<br><sub>-,0,-,-,0</sub> |  | 2.3<br><sub>-,2,-,-,2</sub> |  | 1.6<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.1 | 0.9 | 9.3 |
| Ron Harper Jr. (BOS) | 58% | 11.4<br><sub>-,12,-,-,13</sub> | 4.4<br><sub>-,10,-,-,3</sub> |  | 1.5<br><sub>-,1,-,-,0</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.6<br><sub>-,2,-,-,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.7 |
| Dillon Mitchell (BOS) | 35% | 7.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.1 |
| Amari Williams (BOS) | 23% | 7.2<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.6 | 4.3 |
| Yaxel Lendeborg (GSW) | 98% | 32.8<br><sub>36,24,33,30,33</sub> | 18.5<br><sub>25,3,28,13,11</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>10,7,8,5,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>0,1,3,4,7</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>2,0,2,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.7 | 2.7 | 29.4 |
| Brandin Podziemski (GSW) | 97% | 32.6<br><sub>37,22,30,29,32</sub> | 16.2<br><sub>22,8,15,10,15</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>6,3,6,3,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>4,0,3,4,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>4,2,3,0,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 1.6 | 25.2 |
| Draymond Green (GSW) | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>5,3,8,1,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>7,3,5,2,-</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>1,0,0,1,-</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.7 | 2.2 | 16.0 |
| Will Richard (GSW) | 98% | 23.4<br><sub>19,30,23,27,27</sub> | 8.4<br><sub>9,7,11,20,15</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>4,4,3,0,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.2 | 0.9 | 12.5 |
| De'Anthony Melton (GSW) | 99% | 23.3<br><sub>25,18,21,19,25</sub> | 10.4<br><sub>11,8,8,0,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,2,2,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>4,3,1,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.4 | 1.6 | 16.5 |
| Gui Santos (GSW) | 96% | 19.0<br><sub>12,21,19,17,23</sub> | 8.0<br><sub>0,7,12,6,8</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,4,7,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>1,1,2,6,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.3 | 1.2 | 13.8 |
| Charles Bassey (GSW) | 98% | 17.8<br><sub>13,20,16,22,25</sub> | 8.1<br><sub>7,11,4,10,16</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>6,5,0,8,13</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.2 |
| Gary Payton II (GSW) | 88% | 17.6<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.0<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.1 |
| Georges Niang (GSW) | 98% | 17.4<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> |  | 2.6<br><sub>5,3,4,1,2</sub> |  | 1.1<br><sub>0,2,2,1,0</sub> |  | 1.1<br><sub>1,1,0,2,1</sub> |  | 0.3 | 0.1 | 0.8 | 11.2 |
| Al Horford (GSW) | 98% | 16.8<br><sub>21,10,14,-,17</sub> | 5.5<br><sub>2,0,0,-,3</sub> |  | 3.5<br><sub>1,3,5,-,2</sub> |  | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.7 | 0.5 | 10.8 |
| LJ Cryer (GSW) | 88% | 14.7<br><sub>18,24,24,19,12</sub> | 6.8<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.5<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.2 | 0.1 | 0.6 | 9.4 |
| Graham Ike (GSW) | 96% | 10.2<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 7.6 |
| Malevy Leons (GSW) | 83% | 8.2<br><sub>4,14,6,7,4</sub> | 2.2<br><sub>0,5,2,2,0</sub> |  | 1.6<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-22/`._
