# NBA model · Sun 22 Nov 2026 (US date)

Updated **Sun 22 Nov, 07:45 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-22/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brice Sensabaugh PTS over 24.5 (25+) | DAL @ UTA | draftkings | 16.20 | 14.77 | 8.14 | 12.3% | 5.8% | 6.8% | +9.7% | +99.0% | 0.2% |
| Jamal Murray PA over 44.5 (45+) | DEN @ CHI | draftkings | 14.00 | 12.85 | 7.23 | 13.8% | 6.7% | 7.8% | +8.9% | +93.5% | 0.2% |
| Jamal Murray PA over 49.5 (50+) | DEN @ CHI | draftkings | 25.00 | 23.20 | 13.41 | 7.5% | 3.7% | 4.3% | +7.8% | +86.5% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DET @ ATL | Mon 23 Nov 07:30 | 112.9–108.7 | DET 62% | 1.62 / 2.62 | ATL +4.5 | 221.5 | ATL +2.5 covers 44%; o226.5 40% |
| OKC @ MIA | Mon 23 Nov 10:00 | 117.2–117.4 | OKC 50% | 2.02 / 1.98 | MIA +0.5 | 234.5 | MIA -2.5 covers 44%; o231.5 56% |
| ORL @ WAS | Mon 23 Nov 11:00 | 119.2–113.0 | ORL 67% | 1.49 / 3.02 | WAS +6.5 | 232.5 | WAS +5.5 covers 48%; o222.5 69% |
| DEN @ CHI | Mon 23 Nov 11:00 | 124.9–114.2 | DEN 78% | 1.28 / 4.53 | CHI +10.5 | 238.5 | CHI +8.5 covers 43%; o237.5 53% |
| DAL @ UTA | Mon 23 Nov 11:00 | 120.6–116.7 | DAL 61% | 1.64 / 2.56 | UTA +4.5 | 237.5 | UTA +1.5 covers 42%; o225.5 73% |
| IND @ NYK | Mon 23 Nov 12:00 | 105.7–113.7 | IND 28% | 3.51 / 1.40 | NYK -8.5 | 219.5 | NYK -9.5 covers 46%; o216.5 56% |
| BOS @ GSW | Mon 23 Nov 12:30 | 110.6–105.0 | BOS 66% | 1.52 / 2.92 | GSW +5.5 | 215.5 | GSW +9.5 covers 61%; o212.5 57% |

### DET @ ATL
Out: Mouhamed Gueye (ATL), Jock Landale (ATL), CJ McCollum (ATL), Asa Newell (ATL), Jalen Duren (DET), Taurean Prince (DET), Duncan Robinson (DET)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.9–108.7 | DET 62% | 1.62 / 2.62 | ATL +4.5 | 221.5 | ATL +2.5 covers 44%; o226.5 40% |
| Expected (weighted by chance each plays) | 113.8–110.4 | DET 60% | 1.68 / 2.48 | ATL +3.5 | 224.5 | ATL +2.5 covers 46%; o226.5 46% |
| if Kingston Flemings plays | 113.1–109.9 | DET 59% | 1.69 / 2.45 | ATL +3.5 | 222.5 | ATL +2.5 covers 47%; o226.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Questionable | 55% | 13.7 | 5.2 | 2.2 | 0.9 | 0.5 | 0.3 | 0.1 | 0.7 | 8.4 | small |
| Ronald Holland II (DET) | Questionable | 55% | 15.7 | 6.0 | 3.3 | 1.2 | 0.5 | 0.8 | 0.5 | 0.9 | 10.4 | small |
| RayJ Dennis (ATL) | Questionable | 55% | 14.4 | 6.0 | 2.1 | 2.6 | 0.7 | 0.5 | 0.2 | 1.1 | 10.6 | small |
| Kingston Flemings (ATL) | Questionable | 55% | 21.9 | 7.8 | 2.5 | 3.4 | 0.7 | 0.7 | 0.3 | 2.1 | 13.7 | full tables below |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 78% | 36.4<br><sub>48,36,38,-,36</sub> | 27.5<br><sub>52,33,27,-,23</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,5,5,-,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 8.6<br><sub>11,8,6,-,9</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>3,3,1,-,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3 | 0.8 | 4.3 | 41.4 |
| Daniss Jenkins | 98% | 34.5<br><sub>42,35,38,36,39</sub> | 17.1<br><sub>21,10,25,17,14</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>6,1,5,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.3<br><sub>0,5,5,9,1</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,1,3,3,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.3 | 2.3 | 26.6 |
| Kevin Huerter | 98% | 32.2<br><sub>24,38,36,36,36</sub> | 13.7<br><sub>11,20,9,11,20</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,4,7,1,3</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 3.5<br><sub>0,7,1,7,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>1,2,0,1,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.7 | 1.7 | 20.9 |
| Ausar Thompson | 98% | 30.9<br><sub>43,18,29,34,33</sub> | 11.8<br><sub>17,10,14,10,13</sub> | 12.5 · –<br><sub>o 44% · u 56%</sub> | 7.9<br><sub>11,8,9,7,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>11,5,12,4,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.1 | 1.0 | 2.4 | 24.6 |
| John Collins | 98% | 27.9<br><sub>25,26,23,30,20</sub> | 12.8<br><sub>10,8,11,20,3</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 6.0<br><sub>4,7,1,7,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,0,0,2,1</sub> |  | 1.3<br><sub>2,2,1,4,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9 | 0.8 | 1.5 | 19.9 |
| Paul Reed | 98% | 27.7<br><sub>38,23,25,20,28</sub> | 13.8<br><sub>13,9,10,17,8</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 8.7<br><sub>11,9,6,7,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,1,5,1,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.4 | 1.2 | 1.8 | 24.9 |
| Javonte Green | 98% | 22.4<br><sub>15,12,23,35,23</sub> | 8.1<br><sub>5,5,6,18,12</sub> |  | 3.2<br><sub>1,1,6,7,1</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 1.1<br><sub>1,0,0,3,3</sub> |  | 1.3 | 0.5 | 0.5 | 12.0 |
| Isaiah Joe | 96% | 15.3<br><sub>-,-,-,16,18</sub> | 7.8<br><sub>-,-,-,11,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>-,-,-,2,1</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 1.2<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.1 | 0.7 | 10.5 |
| Chaz Lanier | 71% | 11.4<br><sub>-,-,25,16,6</sub> | 4.0<br><sub>-,-,3,9,0</sub> |  | 0.9<br><sub>-,-,3,1,0</sub> |  | 0.6<br><sub>-,-,1,0,0</sub> |  | 0.5<br><sub>-,-,1,3,0</sub> |  | 0.3 | 0.1 | 0.2 | 5.5 |
| Elijah Harkless | 52% | 8.9<br><sub>-,2,4,14,-</sub> | 2.9<br><sub>-,2,0,6,-</sub> |  | 1.4<br><sub>-,0,1,2,-</sub> |  | 0.9<br><sub>-,0,1,4,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.6 | 5.1 |
| Tolu Smith | 52% | 8.3<br><sub>-,1,-,3,-</sub> | 3.4<br><sub>-,3,-,3,-</sub> |  | 2.9<br><sub>-,2,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 6.7 |
| Isaac Jones | 21% | 6.3<br><sub>-,2,-,-,-</sub> | 7.4<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 9.4 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 37.3<br><sub>38,40,35,34,36</sub> | 22.9<br><sub>15,27,14,16,26</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>7,11,11,12,6</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 8.1<br><sub>4,10,5,11,6</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.7 | 3.7 | 40.5 |
| Nickeil Alexander-Walker | 99% | 35.4<br><sub>34,41,33,32,32</sub> | 21.8<br><sub>20,16,20,19,17</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,6,5,4,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,3,4,7,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.2<br><sub>4,1,2,3,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 2.5 | 29.1 |
| Onyeka Okongwu | 99% | 34.7<br><sub>30,35,36,36,34</sub> | 16.6<br><sub>16,17,16,28,16</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>9,6,11,9,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>3,1,0,2,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,2,3,5,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 1.2 | 2.0 | 28.0 |
| Dyson Daniels | 99% | 34.7<br><sub>31,36,27,37,35</sub> | 11.4<br><sub>10,6,9,10,11</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>6,9,10,10,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.5<br><sub>8,4,5,4,10</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.5<br><sub>1,0,0,0,1</sub> |  | 2.4 | 0.4 | 2.0 | 25.4 |
| Aaron Wiggins | 98% | 32.1<br><sub>23,26,24,26,34</sub> | 15.1<br><sub>15,9,7,14,19</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>3,4,3,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,3,3,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.5<br><sub>4,1,1,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 1.8 | 21.7 |
| Luguentz Dort | 99% | 28.9<br><sub>18,20,18,31,23</sub> | 10.0<br><sub>4,10,3,16,2</sub> |  | 3.3<br><sub>3,1,4,3,1</sub> |  | 1.6<br><sub>2,2,0,0,0</sub> |  | 1.6<br><sub>1,1,0,3,0</sub> |  | 1.0 | 0.4 | 1.0 | 14.9 |
| Corey Kispert | 67% | 16.7<br><sub>-,-,16,17,16</sub> | 7.6<br><sub>-,-,14,8,7</sub> |  | 2.1<br><sub>-,-,3,1,3</sub> |  | 1.2<br><sub>-,-,1,2,0</sub> |  | 1.1<br><sub>-,-,3,2,1</sub> |  | 0.3 | 0.2 | 0.8 | 10.9 |
| Zuby Ejiofor | 80% | 14.7<br><sub>4,-,12,12,14</sub> | 5.3<br><sub>0,-,4,3,5</sub> |  | 3.1<br><sub>0,-,3,3,2</sub> |  | 1.2<br><sub>0,-,0,0,2</sub> |  | 0.4<br><sub>0,-,1,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 9.6 |
| Dorian Finney-Smith | 52% | 9.2<br><sub>-,-,-,5,3</sub> | 2.1<br><sub>-,-,-,0,0</sub> |  | 1.4<br><sub>-,-,-,2,0</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.0 |
| Rafael Castro | 19% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Kingston Flemings plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 36.3<br><sub>38,40,35,34,36</sub> | 21.7<br><sub>15,27,14,16,26</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 9.4<br><sub>7,11,11,12,6</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 7.1<br><sub>4,10,5,11,6</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.6 | 3.6 | 38.3 |
| Nickeil Alexander-Walker (ATL) | 99% | 34.3<br><sub>34,41,33,32,32</sub> | 20.6<br><sub>20,16,20,19,17</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,6,5,4,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>4,3,4,7,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>4,1,2,3,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.5 | 2.4 | 27.4 |
| Onyeka Okongwu (ATL) | 99% | 33.9<br><sub>30,35,36,36,34</sub> | 16.2<br><sub>16,17,16,28,16</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>9,6,11,9,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>3,1,0,2,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,2,3,5,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 1.1 | 1.8 | 27.2 |
| Dyson Daniels (ATL) | 99% | 33.8<br><sub>31,36,27,37,35</sub> | 11.2<br><sub>10,6,9,10,11</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>6,9,10,10,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>8,4,5,4,10</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.4<br><sub>1,0,0,0,1</sub> |  | 2.4 | 0.4 | 1.8 | 24.3 |
| Aaron Wiggins (ATL) | 98% | 30.3<br><sub>23,26,24,26,34</sub> | 14.2<br><sub>15,9,7,14,19</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,4,3,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>3,3,3,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.3<br><sub>4,1,1,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 1.6 | 20.3 |
| Luguentz Dort (ATL) | 99% | 25.9<br><sub>18,20,18,31,23</sub> | 8.8<br><sub>4,10,3,16,2</sub> |  | 3.1<br><sub>3,1,4,3,1</sub> |  | 1.3<br><sub>2,2,0,0,0</sub> |  | 1.4<br><sub>1,1,0,3,0</sub> |  | 0.9 | 0.3 | 0.8 | 13.2 |
| Kingston Flemings (ATL) | 100% | 21.9<br><sub>24,17,-,-,-</sub> | 7.8<br><sub>8,0,-,-,-</sub> | 7.5 · – | 2.5<br><sub>3,1,-,-,-</sub> | 2.5 | 3.4<br><sub>4,1,-,-,-</sub> | 3.5 | 0.7<br><sub>1,0,-,-,-</sub> | 0.5 | 0.7 | 0.3 | 2.1 | 13.7 |
| Corey Kispert (ATL) | 67% | 14.9<br><sub>-,-,16,17,16</sub> | 7.0<br><sub>-,-,14,8,7</sub> |  | 1.9<br><sub>-,-,3,1,3</sub> |  | 1.0<br><sub>-,-,1,2,0</sub> |  | 1.0<br><sub>-,-,3,2,1</sub> |  | 0.3 | 0.2 | 0.7 | 9.9 |
| Zuby Ejiofor (ATL) | 80% | 13.4<br><sub>4,-,12,12,14</sub> | 4.8<br><sub>0,-,4,3,5</sub> |  | 2.9<br><sub>0,-,3,3,2</sub> |  | 1.0<br><sub>0,-,0,0,2</sub> |  | 0.4<br><sub>0,-,1,1,0</sub> |  | 0.4 | 0.4 | 0.7 | 8.8 |
| Rafael Castro (ATL) | 19% | 8.6 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Dorian Finney-Smith (ATL) | 52% | 7.3<br><sub>-,-,-,5,3</sub> | 1.7<br><sub>-,-,-,0,0</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |
| Cade Cunningham (DET) | 78% | 36.5<br><sub>48,36,38,-,36</sub> | 27.5<br><sub>52,33,27,-,23</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,5,5,-,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 8.6<br><sub>11,8,6,-,9</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>3,3,1,-,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3 | 0.8 | 4.3 | 41.3 |
| Daniss Jenkins (DET) | 98% | 34.5<br><sub>42,35,38,36,39</sub> | 17.2<br><sub>21,10,25,17,14</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>6,1,5,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.3<br><sub>0,5,5,9,1</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>3,1,3,3,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.3 | 2.3 | 26.6 |
| Kevin Huerter (DET) | 98% | 32.2<br><sub>24,38,36,36,36</sub> | 13.9<br><sub>11,20,9,11,20</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,4,7,1,3</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 3.5<br><sub>0,7,1,7,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>1,2,0,1,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.7 | 1.7 | 21.1 |
| Ausar Thompson (DET) | 98% | 30.9<br><sub>43,18,29,34,33</sub> | 11.7<br><sub>17,10,14,10,13</sub> | 12.5 · –<br><sub>o 44% · u 56%</sub> | 7.9<br><sub>11,8,9,7,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>11,5,12,4,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.1 | 1.0 | 2.4 | 24.6 |
| John Collins (DET) | 98% | 27.9<br><sub>25,26,23,30,20</sub> | 12.8<br><sub>10,8,11,20,3</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 6.1<br><sub>4,7,1,7,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,0,0,2,1</sub> |  | 1.3<br><sub>2,2,1,4,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9 | 0.8 | 1.5 | 20.0 |
| Paul Reed (DET) | 98% | 27.7<br><sub>38,23,25,20,28</sub> | 13.9<br><sub>13,9,10,17,8</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 8.7<br><sub>11,9,6,7,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,1,5,1,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.4 | 1.2 | 1.8 | 24.9 |
| Javonte Green (DET) | 98% | 22.4<br><sub>15,12,23,35,23</sub> | 8.1<br><sub>5,5,6,18,12</sub> |  | 3.2<br><sub>1,1,6,7,1</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 1.1<br><sub>1,0,0,3,3</sub> |  | 1.3 | 0.5 | 0.5 | 11.9 |
| Isaiah Joe (DET) | 96% | 15.4<br><sub>-,-,-,16,18</sub> | 7.9<br><sub>-,-,-,11,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>-,-,-,2,1</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 1.2<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.1 | 0.7 | 10.6 |
| Chaz Lanier (DET) | 71% | 11.4<br><sub>-,-,25,16,6</sub> | 4.0<br><sub>-,-,3,9,0</sub> |  | 0.9<br><sub>-,-,3,1,0</sub> |  | 0.6<br><sub>-,-,1,0,0</sub> |  | 0.5<br><sub>-,-,1,3,0</sub> |  | 0.3 | 0.1 | 0.2 | 5.5 |
| Elijah Harkless (DET) | 52% | 9.0<br><sub>-,2,4,14,-</sub> | 2.9<br><sub>-,2,0,6,-</sub> |  | 1.4<br><sub>-,0,1,2,-</sub> |  | 0.9<br><sub>-,0,1,4,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.6 | 5.2 |
| Tolu Smith (DET) | 52% | 8.4<br><sub>-,1,-,3,-</sub> | 3.5<br><sub>-,3,-,3,-</sub> |  | 3.0<br><sub>-,2,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.4 | 0.5 | 7.0 |
| Isaac Jones (DET) | 21% | 6.2<br><sub>-,2,-,-,-</sub> | 7.5<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 9.4 |

</details>


### OKC @ MIA
Out: Keshad Johnson (MIA), Alex Caruso (OKC), Chet Holmgren (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.2–117.4 | OKC 50% | 2.02 / 1.98 | MIA +0.5 | 234.5 | MIA -2.5 covers 44%; o231.5 56% |
| Expected (weighted by chance each plays) | 119.2–117.8 | OKC 54% | 1.87 / 2.15 | MIA +1.5 | 236.5 | MIA -2.5 covers 41%; o231.5 61% |
| if Giannis Antetokounmpo plays | 117.3–119.5 | OKC 44% | 2.27 / 1.79 | MIA -2.5 | 236.5 | MIA -2.5 covers 50%; o231.5 61% |
| if Shai Gilgeous-Alexander plays | 121.2–115.7 | OKC 65% | 1.53 / 2.89 | MIA +5.5 | 236.5 | MIA -2.5 covers 29%; o231.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Giannis Antetokounmpo (MIA) | Questionable | 55% | 33.6 | 26.0 | 12.9 | 5.6 | 0.5 | 0.9 | 1.1 | 3.3 | 44.5 | full tables below |
| Shai Gilgeous-Alexander (OKC) | Questionable | 55% | 36.0 | 35.8 | 4.4 | 6.8 | 2.0 | 1.3 | 0.8 | 2.7 | 47.0 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jared McCain | 99% | 33.0<br><sub>31,31,30,33,30</sub> | 21.7<br><sub>10,23,12,18,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>6,4,1,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>3,2,1,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 3.2<br><sub>2,7,1,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 2.1 | 28.4 |
| Ajay Mitchell | 98% | 32.4<br><sub>-,-,27,34,31</sub> | 22.8<br><sub>-,-,14,13,8</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>-,-,3,6,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.7<br><sub>-,-,5,6,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.3 | 2.2 | 32.7 |
| Kenrich Williams | 98% | 29.3<br><sub>26,35,19,23,28</sub> | 12.8<br><sub>11,8,10,10,6</sub> |  | 5.4<br><sub>2,8,1,5,2</sub> |  | 2.8<br><sub>2,4,2,1,4</sub> |  | 1.7<br><sub>2,0,2,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 21.1 |
| Aday Mara | 98% | 28.5<br><sub>32,21,26,27,29</sub> | 13.7<br><sub>11,10,16,10,22</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 9.4<br><sub>6,3,13,6,16</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,0,3,8,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.7 | 2.0 | 25.8 |
| Bennett Stirtz | 98% | 27.7<br><sub>25,12,17,17,25</sub> | 12.8<br><sub>6,5,0,6,18</sub> |  | 2.2<br><sub>1,1,1,0,2</sub> |  | 2.3<br><sub>1,0,2,2,2</sub> |  | 2.1<br><sub>2,1,0,2,4</sub> |  | 1.0 | 0.2 | 1.1 | 17.2 |
| Isaiah Hartenstein | 99% | 27.0<br><sub>34,30,18,27,28</sub> | 11.1<br><sub>20,21,3,6,5</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 11.7<br><sub>11,16,11,17,8</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>6,6,2,6,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.9 | 27.3 |
| Nique Clifford | 97% | 22.5<br><sub>16,12,24,13,15</sub> | 8.9<br><sub>5,0,9,7,4</sub> |  | 3.4<br><sub>3,0,3,0,5</sub> |  | 2.1<br><sub>1,0,0,0,1</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.3 | 1.1 | 14.5 |
| Micah Peavy | 91% | 20.5<br><sub>12,-,13,-,9</sub> | 6.9<br><sub>0,-,5,-,2</sub> |  | 3.7<br><sub>3,-,3,-,2</sub> |  | 0.9<br><sub>0,-,1,-,0</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.7 | 0.3 | 0.4 | 11.5 |
| Josh Dix | 58% | 19.4<br><sub>-,17,-,-,-</sub> | 7.6<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,4,-,-,-</sub> |  | 1.4<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Brooks Barnhizer | 48% | 11.3<br><sub>-,-,4,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 99% | 36.5<br><sub>38,39,32,33,36</sub> | 16.5<br><sub>19,22,15,16,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,5,4,3,2</sub> |  | 8.6<br><sub>8,17,9,10,6</sub> |  | 2.3<br><sub>3,3,3,1,6</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 2.7 | 28.4 |
| Bam Adebayo | 99% | 34.5<br><sub>37,38,36,16,30</sub> | 19.8<br><sub>11,37,20,4,26</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 9.6<br><sub>8,14,5,1,4</sub> |  | 3.6<br><sub>4,3,4,2,2</sub> |  | 1.5<br><sub>0,2,1,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.6 | 2.0 | 33.0 |
| Andrew Wiggins | 98% | 31.3<br><sub>19,32,23,34,26</sub> | 14.5<br><sub>13,8,10,17,11</sub> |  | 4.4<br><sub>0,3,2,5,2</sub> |  | 2.3<br><sub>0,4,1,1,2</sub> |  | 2.1<br><sub>2,1,0,3,1</sub> |  | 0.9 | 0.9 | 1.5 | 21.2 |
| Pelle Larsson | 83% | 28.0<br><sub>31,-,-,-,15</sub> | 12.2<br><sub>14,-,-,-,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>7,-,-,-,2</sub> |  | 3.3<br><sub>2,-,-,-,2</sub> |  | 1.2<br><sub>2,-,-,-,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 0.2 | 1.9 | 19.3 |
| Klay Thompson | 88% | 26.2<br><sub>30,-,20,22,23</sub> | 14.2<br><sub>11,-,26,17,13</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,-,1,0,1</sub> |  | 1.9<br><sub>2,-,4,2,1</sub> |  | 3.1<br><sub>2,-,6,5,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.6 | 1.1 | 18.1 |
| Ryan Conwell | 91% | 25.0<br><sub>21,33,26,30,26</sub> | 10.8<br><sub>5,20,9,14,13</sub> |  | 3.0<br><sub>4,5,4,2,3</sub> |  | 1.8<br><sub>2,2,1,3,1</sub> |  | 1.9<br><sub>1,4,2,1,3</sub> |  | 0.8 | 0.2 | 1.0 | 15.5 |
| Bobby Portis | 99% | 22.6<br><sub>17,15,18,23,17</sub> | 11.3<br><sub>5,5,7,16,9</sub> |  | 6.3<br><sub>1,3,4,6,3</sub> |  | 1.5<br><sub>1,2,2,0,0</sub> |  | 1.6<br><sub>1,1,1,2,1</sub> |  | 0.6 | 0.3 | 0.9 | 19.1 |
| Myron Gardner | 58% | 19.0<br><sub>10,19,26,24,-</sub> | 6.6<br><sub>4,0,5,14,-</sub> |  | 5.2<br><sub>3,4,9,2,-</sub> |  | 1.9<br><sub>1,2,3,3,-</sub> |  | 0.9<br><sub>0,0,1,4,-</sub> |  | 0.6 | 0.4 | 0.9 | 13.7 |
| Simone Fontecchio | 76% | 17.6<br><sub>7,7,14,19,18</sub> | 8.2<br><sub>3,0,7,10,6</sub> |  | 3.7<br><sub>0,0,5,6,5</sub> |  | 1.3<br><sub>0,2,0,2,1</sub> |  | 1.4<br><sub>0,0,1,2,2</sub> |  | 0.5 | 0.2 | 0.7 | 13.2 |
| Nikola Jovic | 58% | 16.0<br><sub>-,-,11,-,14</sub> | 6.2<br><sub>-,-,2,-,4</sub> |  | 3.0<br><sub>-,-,1,-,1</sub> |  | 1.7<br><sub>-,-,2,-,4</sub> |  | 0.8<br><sub>-,-,0,-,1</sub> |  | 0.5 | 0.4 | 0.8 | 10.9 |
| Tim Hardaway Jr. | 52% | 15.5<br><sub>-,20,-,-,-</sub> | 6.8<br><sub>-,4,-,-,-</sub> |  | 1.8<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 9.3 |
| Dru Smith | 38% | 11.3<br><sub>-,6,-,-,-</sub> | 4.1<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.2 | 0.6 | 7.5 |
| Nick Richards | 52% | 7.8<br><sub>-,-,-,3,1</sub> | 2.9<br><sub>-,-,-,0,0</sub> |  | 2.6<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.1 | 0.3 | 0.6 | 5.8 |
| Tre Donaldson | 76% | 6.9<br><sub>-,-,1,3,1</sub> | 2.9<br><sub>-,-,2,0,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 1.2 | 3.8 |

</details>

<details><summary>if Shai Gilgeous-Alexander plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 36.5<br><sub>38,39,32,33,36</sub> | 16.4<br><sub>19,22,15,16,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,5,4,3,2</sub> |  | 8.6<br><sub>8,17,9,10,6</sub> |  | 2.3<br><sub>3,3,3,1,6</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 2.7 | 28.2 |
| Bam Adebayo (MIA) | 99% | 34.5<br><sub>37,38,36,16,30</sub> | 19.6<br><sub>11,37,20,4,26</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 9.6<br><sub>8,14,5,1,4</sub> |  | 3.6<br><sub>4,3,4,2,2</sub> |  | 1.5<br><sub>0,2,1,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.6 | 2.0 | 32.8 |
| Andrew Wiggins (MIA) | 98% | 31.3<br><sub>19,32,23,34,26</sub> | 14.3<br><sub>13,8,10,17,11</sub> |  | 4.4<br><sub>0,3,2,5,2</sub> |  | 2.3<br><sub>0,4,1,1,2</sub> |  | 2.1<br><sub>2,1,0,3,1</sub> |  | 0.9 | 0.9 | 1.5 | 21.0 |
| Pelle Larsson (MIA) | 83% | 28.1<br><sub>31,-,-,-,15</sub> | 12.1<br><sub>14,-,-,-,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>7,-,-,-,2</sub> |  | 3.3<br><sub>2,-,-,-,2</sub> |  | 1.2<br><sub>2,-,-,-,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 0.2 | 1.9 | 19.2 |
| Klay Thompson (MIA) | 88% | 26.2<br><sub>30,-,20,22,23</sub> | 14.1<br><sub>11,-,26,17,13</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,-,1,0,1</sub> |  | 1.9<br><sub>2,-,4,2,1</sub> |  | 3.1<br><sub>2,-,6,5,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.6 | 1.1 | 18.1 |
| Ryan Conwell (MIA) | 91% | 25.0<br><sub>21,33,26,30,26</sub> | 10.6<br><sub>5,20,9,14,13</sub> |  | 2.9<br><sub>4,5,4,2,3</sub> |  | 1.8<br><sub>2,2,1,3,1</sub> |  | 1.9<br><sub>1,4,2,1,3</sub> |  | 0.8 | 0.2 | 1.0 | 15.4 |
| Bobby Portis (MIA) | 99% | 22.6<br><sub>17,15,18,23,17</sub> | 11.2<br><sub>5,5,7,16,9</sub> |  | 6.3<br><sub>1,3,4,6,3</sub> |  | 1.6<br><sub>1,2,2,0,0</sub> |  | 1.6<br><sub>1,1,1,2,1</sub> |  | 0.6 | 0.3 | 0.9 | 19.1 |
| Myron Gardner (MIA) | 58% | 19.0<br><sub>10,19,26,24,-</sub> | 6.6<br><sub>4,0,5,14,-</sub> |  | 5.2<br><sub>3,4,9,2,-</sub> |  | 1.9<br><sub>1,2,3,3,-</sub> |  | 0.9<br><sub>0,0,1,4,-</sub> |  | 0.6 | 0.4 | 0.9 | 13.7 |
| Simone Fontecchio (MIA) | 76% | 17.6<br><sub>7,7,14,19,18</sub> | 8.2<br><sub>3,0,7,10,6</sub> |  | 3.6<br><sub>0,0,5,6,5</sub> |  | 1.3<br><sub>0,2,0,2,1</sub> |  | 1.4<br><sub>0,0,1,2,2</sub> |  | 0.5 | 0.2 | 0.7 | 13.1 |
| Nikola Jovic (MIA) | 58% | 15.9<br><sub>-,-,11,-,14</sub> | 6.0<br><sub>-,-,2,-,4</sub> |  | 3.0<br><sub>-,-,1,-,1</sub> |  | 1.7<br><sub>-,-,2,-,4</sub> |  | 0.8<br><sub>-,-,0,-,1</sub> |  | 0.5 | 0.4 | 0.8 | 10.7 |
| Tim Hardaway Jr. (MIA) | 52% | 15.5<br><sub>-,20,-,-,-</sub> | 6.7<br><sub>-,4,-,-,-</sub> |  | 1.8<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 9.2 |
| Dru Smith (MIA) | 38% | 11.2<br><sub>-,6,-,-,-</sub> | 4.0<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 7.3 |
| Nick Richards (MIA) | 52% | 7.8<br><sub>-,-,-,3,1</sub> | 2.9<br><sub>-,-,-,0,0</sub> |  | 2.6<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.1 | 0.3 | 0.6 | 5.7 |
| Tre Donaldson (MIA) | 76% | 7.0<br><sub>-,-,1,3,1</sub> | 2.9<br><sub>-,-,2,0,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 1.2 | 3.8 |
| Shai Gilgeous-Alexander (OKC) | 100% | 36.0<br><sub>36,39,30,36,37</sub> | 35.8<br><sub>31,40,37,34,40</sub> | 31.5 · – | 4.4<br><sub>4,4,2,5,3</sub> | 3.5 | 6.8<br><sub>2,5,2,3,8</sub> | 5.5 | 2.0<br><sub>0,2,4,1,4</sub> | 1.5 | 1.3 | 0.8 | 2.7 | 47.0 |
| Ajay Mitchell (OKC) | 98% | 31.2<br><sub>-,-,27,34,31</sub> | 18.0<br><sub>-,-,14,13,8</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>-,-,3,6,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.7<br><sub>-,-,5,6,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.3 | 1.8 | 26.7 |
| Jared McCain (OKC) | 99% | 30.9<br><sub>31,31,30,33,30</sub> | 16.9<br><sub>10,23,12,18,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>6,4,1,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,2,1,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.7<br><sub>2,7,1,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.2 | 1.6 | 22.7 |
| Isaiah Hartenstein (OKC) | 99% | 27.5<br><sub>34,30,18,27,28</sub> | 9.6<br><sub>20,21,3,6,5</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 11.7<br><sub>11,16,11,17,8</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 3.9<br><sub>6,6,2,6,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.7 | 25.2 |
| Aday Mara (OKC) | 98% | 27.2<br><sub>32,21,26,27,29</sub> | 11.0<br><sub>11,10,16,10,22</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 8.9<br><sub>6,3,13,6,16</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,0,3,8,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.6 | 1.7 | 22.1 |
| Kenrich Williams (OKC) | 98% | 25.8<br><sub>26,35,19,23,28</sub> | 9.6<br><sub>11,8,10,10,6</sub> |  | 4.9<br><sub>2,8,1,5,2</sub> |  | 2.3<br><sub>2,4,2,1,4</sub> |  | 1.3<br><sub>2,0,2,0,1</sub> |  | 0.9 | 0.2 | 1.0 | 16.7 |
| Bennett Stirtz (OKC) | 98% | 22.6<br><sub>25,12,17,17,25</sub> | 9.1<br><sub>6,5,0,6,18</sub> |  | 1.7<br><sub>1,1,1,0,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 1.5<br><sub>2,1,0,2,4</sub> |  | 0.8 | 0.2 | 0.8 | 12.6 |
| Nique Clifford (OKC) | 97% | 16.8<br><sub>16,12,24,13,15</sub> | 5.7<br><sub>5,0,9,7,4</sub> |  | 2.6<br><sub>3,0,3,0,5</sub> |  | 1.4<br><sub>1,0,0,0,1</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.8 | 9.6 |
| Micah Peavy (OKC) | 91% | 15.1<br><sub>12,-,13,-,9</sub> | 4.1<br><sub>0,-,5,-,2</sub> |  | 2.8<br><sub>3,-,3,-,2</sub> |  | 0.6<br><sub>0,-,1,-,0</sub> |  | 0.4<br><sub>0,-,1,-,0</sub> |  | 0.5 | 0.2 | 0.4 | 7.6 |
| Josh Dix (OKC) | 58% | 14.9<br><sub>-,17,-,-,-</sub> | 5.4<br><sub>-,0,-,-,-</sub> |  | 1.8<br><sub>-,4,-,-,-</sub> |  | 0.9<br><sub>-,3,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 8.0 |
| Brooks Barnhizer (OKC) | 48% | 8.4<br><sub>-,-,4,-,-</sub> | 2.0<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |

</details>

<details><summary>if Giannis Antetokounmpo plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 99% | 35.3<br><sub>38,39,32,33,36</sub> | 14.8<br><sub>19,22,15,16,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,5,4,3,2</sub> |  | 8.2<br><sub>8,17,9,10,6</sub> |  | 2.0<br><sub>3,3,3,1,6</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 2.4 | 26.1 |
| Bam Adebayo (MIA) | 99% | 33.6<br><sub>37,38,36,16,30</sub> | 18.0<br><sub>11,37,20,4,26</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 9.1<br><sub>8,14,5,1,4</sub> |  | 3.3<br><sub>4,3,4,2,2</sub> |  | 1.4<br><sub>0,2,1,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.6 | 1.8 | 30.3 |
| Giannis Antetokounmpo (MIA) | 100% | 33.6<br><sub>31,31,31,29,32</sub> | 26.0<br><sub>30,37,34,20,27</sub> | 27.5 · – | 12.9<br><sub>11,9,14,13,14</sub> |  | 5.6<br><sub>4,2,8,6,9</sub> |  | 0.5<br><sub>1,1,1,0,0</sub> | 0.5 | 0.9 | 1.1 | 3.3 | 44.5 |
| Andrew Wiggins (MIA) | 98% | 26.6<br><sub>19,32,23,34,26</sub> | 11.2<br><sub>13,8,10,17,11</sub> |  | 3.7<br><sub>0,3,2,5,2</sub> |  | 1.8<br><sub>0,4,1,1,2</sub> |  | 1.5<br><sub>2,1,0,3,1</sub> |  | 0.8 | 0.8 | 1.2 | 16.7 |
| Pelle Larsson (MIA) | 83% | 24.6<br><sub>31,-,-,-,15</sub> | 9.9<br><sub>14,-,-,-,4</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>7,-,-,-,2</sub> |  | 2.7<br><sub>2,-,-,-,2</sub> |  | 0.9<br><sub>2,-,-,-,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.7 | 0.2 | 1.7 | 15.9 |
| Klay Thompson (MIA) | 88% | 22.4<br><sub>30,-,20,22,23</sub> | 12.1<br><sub>11,-,26,17,13</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,-,1,0,1</sub> |  | 1.5<br><sub>2,-,4,2,1</sub> |  | 2.5<br><sub>2,-,6,5,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.5 | 0.5 | 1.0 | 15.4 |
| Ryan Conwell (MIA) | 91% | 21.2<br><sub>21,33,26,30,26</sub> | 8.3<br><sub>5,20,9,14,13</sub> |  | 2.5<br><sub>4,5,4,2,3</sub> |  | 1.4<br><sub>2,2,1,3,1</sub> |  | 1.3<br><sub>1,4,2,1,3</sub> |  | 0.7 | 0.2 | 0.9 | 12.2 |
| Bobby Portis (MIA) | 99% | 18.1<br><sub>17,15,18,23,17</sub> | 8.5<br><sub>5,5,7,16,9</sub> |  | 4.9<br><sub>1,3,4,6,3</sub> |  | 1.2<br><sub>1,2,2,0,0</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 0.5 | 0.3 | 0.7 | 14.6 |
| Simone Fontecchio (MIA) | 76% | 11.9<br><sub>7,7,14,19,18</sub> | 5.5<br><sub>3,0,7,10,6</sub> |  | 2.4<br><sub>0,0,5,6,5</sub> |  | 0.9<br><sub>0,2,0,2,1</sub> |  | 0.8<br><sub>0,0,1,2,2</sub> |  | 0.3 | 0.1 | 0.5 | 8.8 |
| Nikola Jovic (MIA) | 58% | 11.4<br><sub>-,-,11,-,14</sub> | 4.4<br><sub>-,-,2,-,4</sub> |  | 2.1<br><sub>-,-,1,-,1</sub> |  | 1.2<br><sub>-,-,2,-,4</sub> |  | 0.5<br><sub>-,-,0,-,1</sub> |  | 0.3 | 0.3 | 0.6 | 7.6 |
| Tim Hardaway Jr. (MIA) | 52% | 10.1<br><sub>-,20,-,-,-</sub> | 4.2<br><sub>-,4,-,-,-</sub> |  | 1.2<br><sub>-,3,-,-,-</sub> |  | 0.5<br><sub>-,2,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.8 |
| Myron Gardner (MIA) | 58% | 9.3<br><sub>10,19,26,24,-</sub> | 3.1<br><sub>4,0,5,14,-</sub> |  | 2.5<br><sub>3,4,9,2,-</sub> |  | 1.0<br><sub>1,2,3,3,-</sub> |  | 0.3<br><sub>0,0,1,4,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.6 |
| Dru Smith (MIA) | 38% | 7.5<br><sub>-,6,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Nick Richards (MIA) | 52% | 5.7<br><sub>-,-,-,3,1</sub> | 2.2<br><sub>-,-,-,0,0</sub> |  | 2.0<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.4 |
| Tre Donaldson (MIA) | 76% | 5.3<br><sub>-,-,1,3,1</sub> | 2.4<br><sub>-,-,2,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.1 | 0.1 | 1.0 | 3.1 |
| Jared McCain (OKC) | 99% | 33.0<br><sub>31,31,30,33,30</sub> | 21.7<br><sub>10,23,12,18,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>6,4,1,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>3,2,1,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 3.2<br><sub>2,7,1,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 2.1 | 28.4 |
| Ajay Mitchell (OKC) | 98% | 32.5<br><sub>-,-,27,34,31</sub> | 22.7<br><sub>-,-,14,13,8</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>-,-,3,6,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.7<br><sub>-,-,5,6,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.3 | 2.1 | 32.7 |
| Kenrich Williams (OKC) | 98% | 29.3<br><sub>26,35,19,23,28</sub> | 12.8<br><sub>11,8,10,10,6</sub> |  | 5.4<br><sub>2,8,1,5,2</sub> |  | 2.8<br><sub>2,4,2,1,4</sub> |  | 1.6<br><sub>2,0,2,0,1</sub> |  | 1.0 | 0.3 | 1.2 | 21.0 |
| Aday Mara (OKC) | 98% | 28.6<br><sub>32,21,26,27,29</sub> | 13.7<br><sub>11,10,16,10,22</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 9.4<br><sub>6,3,13,6,16</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,0,3,8,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.7 | 2.0 | 25.8 |
| Bennett Stirtz (OKC) | 98% | 27.6<br><sub>25,12,17,17,25</sub> | 12.7<br><sub>6,5,0,6,18</sub> |  | 2.1<br><sub>1,1,1,0,2</sub> |  | 2.3<br><sub>1,0,2,2,2</sub> |  | 2.1<br><sub>2,1,0,2,4</sub> |  | 1.0 | 0.2 | 1.0 | 17.1 |
| Isaiah Hartenstein (OKC) | 99% | 27.1<br><sub>34,30,18,27,28</sub> | 11.1<br><sub>20,21,3,6,5</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 11.7<br><sub>11,16,11,17,8</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>6,6,2,6,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.9 | 27.3 |
| Nique Clifford (OKC) | 97% | 22.5<br><sub>16,12,24,13,15</sub> | 9.0<br><sub>5,0,9,7,4</sub> |  | 3.4<br><sub>3,0,3,0,5</sub> |  | 2.1<br><sub>1,0,0,0,1</sub> |  | 0.8<br><sub>1,0,0,1,0</sub> |  | 0.8 | 0.3 | 1.1 | 14.6 |
| Micah Peavy (OKC) | 91% | 20.4<br><sub>12,-,13,-,9</sub> | 6.9<br><sub>0,-,5,-,2</sub> |  | 3.7<br><sub>3,-,3,-,2</sub> |  | 0.9<br><sub>0,-,1,-,0</sub> |  | 0.8<br><sub>0,-,1,-,0</sub> |  | 0.7 | 0.3 | 0.4 | 11.4 |
| Josh Dix (OKC) | 58% | 19.3<br><sub>-,17,-,-,-</sub> | 7.7<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,4,-,-,-</sub> |  | 1.4<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.3 | 0.5 | 11.4 |
| Brooks Barnhizer (OKC) | 48% | 11.4<br><sub>-,-,4,-,-</sub> | 3.0<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.4 |

</details>


### ORL @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.2–113.0 | ORL 67% | 1.49 / 3.02 | WAS +6.5 | 232.5 | WAS +5.5 covers 48%; o222.5 69% |
| Expected (weighted by chance each plays) | 119.2–113.1 | ORL 67% | 1.50 / 2.99 | WAS +6.5 | 232.5 | WAS +5.5 covers 48%; o222.5 70% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Questionable | 55% | 5.7 | 2.4 | 1.7 | 0.4 | 0.1 | 0.2 | 0.2 | 0.4 | 4.4 | small |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 99% | 33.8<br><sub>39,36,38,36,36</sub> | 26.4<br><sub>38,35,21,27,35</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>8,9,8,8,5</sub> |  | 6.8<br><sub>1,12,9,11,7</sub> |  | 1.5<br><sub>3,3,0,1,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.4 | 2.6 | 39.3 |
| Desmond Bane | 98% | 32.9<br><sub>34,35,39,38,31</sub> | 20.0<br><sub>25,21,24,15,21</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>3,5,8,3,2</sub> |  | 3.5<br><sub>2,3,5,3,3</sub> |  | 3.1<br><sub>7,6,3,5,7</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.4 | 1.7 | 27.6 |
| Anthony Black | 98% | 32.2<br><sub>39,37,33,37,37</sub> | 16.0<br><sub>22,5,20,15,13</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>7,2,2,2,7</sub> |  | 5.0<br><sub>8,5,7,6,6</sub> |  | 1.6<br><sub>3,1,3,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.9 | 0.7 | 2.2 | 25.2 |
| Wendell Carter Jr. | 99% | 30.1<br><sub>28,30,28,32,35</sub> | 13.3<br><sub>9,12,10,15,8</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 8.3<br><sub>7,8,3,8,8</sub> |  | 1.9<br><sub>3,0,1,3,2</sub> |  | 0.8<br><sub>0,1,1,2,0</sub> |  | 0.8 | 0.8 | 1.4 | 23.5 |
| Jalen Suggs | 98% | 28.0<br><sub>-,21,25,31,30</sub> | 12.0<br><sub>-,3,12,18,8</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>-,2,6,8,6</sub> |  | 4.7<br><sub>-,3,4,4,2</sub> |  | 1.7<br><sub>-,1,2,5,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6 | 0.6 | 2.2 | 20.5 |
| Tristan da Silva | 88% | 26.2<br><sub>-,31,31,27,24</sub> | 11.6<br><sub>-,12,13,12,6</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>-,6,6,2,1</sub> |  | 1.8<br><sub>-,2,3,0,2</sub> |  | 1.8<br><sub>-,2,3,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.3 | 1.0 | 17.2 |
| Goga Bitadze | 91% | 15.6<br><sub>20,18,20,20,15</sub> | 6.5<br><sub>4,12,10,8,4</sub> |  | 5.5<br><sub>7,4,6,3,4</sub> |  | 1.2<br><sub>0,1,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 13.1 |
| Jevon Carter | 91% | 13.5<br><sub>28,17,12,16,10</sub> | 5.2<br><sub>11,5,3,6,3</sub> |  | 1.4<br><sub>3,2,2,2,0</sub> |  | 1.6<br><sub>4,2,1,3,0</sub> |  | 0.8<br><sub>3,1,1,2,1</sub> |  | 0.7 | 0.2 | 0.4 | 8.2 |
| Nikola Vucevic | 67% | 13.4<br><sub>14,11,-,-,23</sub> | 6.3<br><sub>3,2,-,-,15</sub> |  | 4.2<br><sub>5,3,-,-,8</sub> |  | 1.4<br><sub>1,0,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,3</sub> |  | 0.3 | 0.4 | 0.6 | 11.9 |
| Jase Richardson | 52% | 13.2<br><sub>20,-,-,-,-</sub> | 5.0<br><sub>6,-,-,-,-</sub> |  | 1.4<br><sub>1,-,-,-,-</sub> |  | 1.5<br><sub>2,-,-,-,-</sub> |  | 0.4<br><sub>1,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 7.9 |
| Jamal Cain | 67% | 9.7<br><sub>-,4,15,4,-</sub> | 3.9<br><sub>-,0,2,0,-</sub> |  | 2.0<br><sub>-,4,5,1,-</sub> |  | 0.5<br><sub>-,1,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.3 |
| Alex Morales | 48% | 7.6<br><sub>18,-,-,-,-</sub> | 1.9<br><sub>5,-,-,-,-</sub> |  | 1.3<br><sub>4,-,-,-,-</sub> |  | 0.5<br><sub>3,-,-,-,-</sub> |  | 0.1<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Colin Castleton | 48% | 6.1<br><sub>1,-,-,-,-</sub> | 2.4<br><sub>0,-,-,-,-</sub> |  | 1.9<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.8 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 35.1<br><sub>44,30,32,38,37</sub> | 16.6<br><sub>5,16,21,23,20</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>8,7,5,12,10</sub> |  | 2.8<br><sub>4,1,3,2,6</sub> |  | 1.2<br><sub>1,2,1,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 2.3 | 26.5 |
| Anthony Davis | 99% | 34.6<br><sub>44,31,35,34,34</sub> | 23.5<br><sub>30,14,23,25,36</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 10.9<br><sub>15,8,4,14,11</sub> |  | 2.9<br><sub>4,5,0,2,3</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> |  | 1.2 | 1.7 | 2.2 | 37.3 |
| Trae Young | 99% | 34.6<br><sub>45,26,33,32,35</sub> | 18.3<br><sub>37,0,13,11,16</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>2,1,2,1,2</sub> |  | 8.7<br><sub>14,8,12,8,5</sub> |  | 2.2<br><sub>4,0,2,1,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.3 | 0.2 | 3.2 | 29.7 |
| Kyshawn George | 99% | 34.0<br><sub>26,30,38,40,35</sub> | 16.7<br><sub>14,11,18,20,11</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>1,2,6,2,7</sub> |  | 4.3<br><sub>5,4,1,4,5</sub> |  | 2.3<br><sub>3,1,2,4,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 1.2 | 2.3 | 25.6 |
| Alex Sarr | 98% | 26.2<br><sub>44,27,31,22,20</sub> | 11.5<br><sub>30,25,6,13,3</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>9,9,4,2,3</sub> |  | 2.0<br><sub>2,2,1,3,0</sub> |  | 1.2<br><sub>4,3,1,3,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 1.7 | 1.4 | 19.8 |
| Bilal Coulibaly | 99% | 23.0<br><sub>29,21,16,26,24</sub> | 7.6<br><sub>4,9,11,3,2</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>7,2,5,8,5</sub> |  | 1.3<br><sub>0,0,0,2,0</sub> |  | 0.6<br><sub>0,1,1,0,0</sub> |  | 1.0 | 0.9 | 1.1 | 12.8 |
| Khris Middleton | 64% | 17.6<br><sub>-,9,18,20,28</sub> | 6.0<br><sub>-,8,9,8,5</sub> |  | 2.5<br><sub>-,0,3,4,2</sub> |  | 1.6<br><sub>-,2,3,1,3</sub> |  | 0.6<br><sub>-,2,2,1,0</sub> |  | 0.6 | 0.1 | 1.1 | 10.1 |
| Tre Johnson | 96% | 13.1<br><sub>30,-,21,8,4</sub> | 5.3<br><sub>13,-,9,0,2</sub> |  | 1.3<br><sub>4,-,1,2,1</sub> |  | 0.6<br><sub>2,-,3,0,0</sub> |  | 0.6<br><sub>1,-,2,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.2 |
| Bub Carrington | 84% | 12.6<br><sub>16,23,2,-,6</sub> | 3.9<br><sub>2,11,0,-,3</sub> |  | 1.4<br><sub>0,0,0,-,0</sub> |  | 1.6<br><sub>2,4,0,-,0</sub> |  | 0.5<br><sub>0,3,0,-,1</sub> |  | 0.3 | 0.1 | 0.8 | 6.9 |
| Deandre Ayton | 99% | 12.2<br><sub>9,10,8,9,11</sub> | 3.6<br><sub>2,2,4,0,0</sub> |  | 3.6<br><sub>4,1,0,3,4</sub> |  | 0.5<br><sub>0,0,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 7.7 |
| Will Riley | 88% | 8.8<br><sub>3,16,2,10,6</sub> | 3.9<br><sub>3,14,2,0,0</sub> |  | 1.1<br><sub>0,3,1,3,1</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.3<br><sub>1,2,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.6 |
| Anthony Gill | 48% | 6.6<br><sub>-,6,2,-,-</sub> | 2.5<br><sub>-,5,2,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Tre Mann | 52% | 5.7<br><sub>-,11,2,-,-</sub> | 2.4<br><sub>-,4,2,-,-</sub> |  | 0.7<br><sub>-,1,0,-,-</sub> |  | 0.7<br><sub>-,1,1,-,-</sub> |  | 0.1<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |

</details>


### DEN @ CHI
Out: Tobe Awaka (CHI), Orlando Robinson (CHI), Caleb Wilson (CHI), Bryce Hopkins (DEN), Julian Strawther (DEN), Cam Whitmore (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 124.9–114.2 | DEN 78% | 1.28 / 4.53 | CHI +10.5 | 238.5 | CHI +8.5 covers 43%; o237.5 53% |
| Expected (weighted by chance each plays) | 124.2–116.6 | DEN 71% | 1.42 / 3.40 | CHI +7.5 | 240.5 | CHI +8.5 covers 53%; o237.5 57% |
| if Jalen Smith plays | 123.5–116.0 | DEN 71% | 1.41 / 3.42 | CHI +7.5 | 239.5 | CHI +8.5 covers 52%; o237.5 54% |
| if Norman Powell plays | 124.2–117.1 | DEN 70% | 1.44 / 3.29 | CHI +7.5 | 241.5 | CHI +8.5 covers 54%; o237.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Smith (CHI) | Questionable | 55% | 28.2 | 15.4 | 8.9 | 2.1 | 2.0 | 0.6 | 0.9 | 1.2 | 26.4 | full tables below |
| Norman Powell (CHI) | Questionable | 55% | 32.1 | 20.7 | 3.5 | 2.8 | 2.5 | 1.1 | 0.2 | 2.0 | 26.9 | full tables below |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.2<br><sub>37,37,38,39,38</sub> | 29.0<br><sub>27,26,28,24,26</sub> | 25.5 · –<br><sub>o 52% · u 48%</sub> | 12.6<br><sub>11,8,15,8,7</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 10.1<br><sub>8,10,7,9,11</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7 | 0.9 | 3.4 | 51.7 |
| Jamal Murray | 98% | 36.5<br><sub>32,38,35,38,36</sub> | 26.2<br><sub>30,23,28,21,14</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>4,7,4,7,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>8,9,4,2,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,0,1,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.6 | 2.1 | 37.4 |
| Christian Braun | 98% | 33.2<br><sub>37,28,33,35,31</sub> | 12.7<br><sub>12,17,10,15,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,7,3,5,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>4,1,3,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>2,1,2,1,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.4 | 0.9 | 20.0 |
| Aaron Gordon | 98% | 30.2<br><sub>27,33,24,31,31</sub> | 14.2<br><sub>9,11,11,13,18</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>3,5,1,8,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.3<br><sub>1,1,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.4 | 1.2 | 22.2 |
| Cameron Johnson | 98% | 30.0<br><sub>30,31,27,26,29</sub> | 14.1<br><sub>23,12,9,8,19</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,5,0,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,2,1,1,6</sub> |  | 1.8<br><sub>4,1,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.0 | 20.5 |
| DeMar DeRozan | 91% | 22.4<br><sub>20,24,14,25,22</sub> | 11.9<br><sub>8,9,2,18,15</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,3,1,2,2</sub> |  | 3.0<br><sub>4,2,1,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.3<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.0 | 17.0 |
| Spencer Jones | 91% | 16.4<br><sub>22,12,21,17,18</sub> | 4.0<br><sub>3,4,4,2,3</sub> |  | 2.3<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>0,1,3,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.6 | 7.2 |
| Trevon Brazile | 98% | 14.9<br><sub>13,16,23,11,11</sub> | 4.7<br><sub>7,5,9,0,4</sub> |  | 3.8<br><sub>5,3,4,6,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 9.0 |
| Marvin Bagley III | 98% | 12.5<br><sub>12,13,10,9,10</sub> | 6.5<br><sub>4,7,4,4,10</sub> |  | 4.0<br><sub>2,7,2,3,6</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.6 | 0.6 | 11.2 |
| Tyus Jones | 98% | 11.7<br><sub>11,10,10,9,14</sub> | 3.0<br><sub>0,2,0,0,5</sub> |  | 1.1<br><sub>1,0,1,0,3</sub> |  | 2.1<br><sub>4,3,2,0,4</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Zeke Nnaji | 23% | 7.2<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.5 |
| Alpha Diallo | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Ryan Nembhard | 48% | 6.0<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaac Okoro | 99% | 32.5<br><sub>41,31,32,25,29</sub> | 12.1<br><sub>15,9,13,12,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>3,7,6,3,7</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>2,4,2,4,1</sub> |  | 1.4<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.4 | 1.1 | 18.4 |
| Matas Buzelis | 99% | 31.7<br><sub>29,30,31,30,25</sub> | 19.6<br><sub>11,18,23,25,9</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>6,9,3,5,5</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,2,0,4,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>3,2,3,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 1.1 | 2.3 | 28.0 |
| Josh Giddey | 99% | 30.5<br><sub>39,26,24,28,23</sub> | 15.9<br><sub>15,8,4,18,2</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>10,8,4,14,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 8.6<br><sub>14,5,8,9,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>3,2,1,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.5 | 2.9 | 31.4 |
| Patrick Williams | 82% | 26.7<br><sub>24,26,13,13,23</sub> | 10.0<br><sub>13,14,0,2,6</sub> |  | 4.0<br><sub>4,5,0,1,3</sub> |  | 2.1<br><sub>2,1,0,2,1</sub> |  | 1.4<br><sub>4,2,0,0,0</sub> |  | 0.8 | 0.5 | 1.1 | 16.1 |
| Tre Jones | 99% | 26.6<br><sub>15,24,23,16,25</sub> | 15.0<br><sub>4,16,16,10,12</sub> |  | 3.1<br><sub>1,0,2,2,1</sub> |  | 5.1<br><sub>3,4,6,6,7</sub> |  | 0.7<br><sub>0,1,0,0,0</sub> |  | 1.1 | 0.2 | 1.4 | 23.2 |
| Nic Claxton | 98% | 26.0<br><sub>22,-,17,22,29</sub> | 11.3<br><sub>2,-,8,14,11</sub> |  | 6.8<br><sub>6,-,2,4,7</sub> |  | 2.6<br><sub>2,-,1,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.7 | 0.9 | 1.2 | 20.6 |
| Buddy Hield | 88% | 24.8<br><sub>25,20,19,19,23</sub> | 11.9<br><sub>12,16,6,11,15</sub> |  | 3.4<br><sub>3,4,4,1,4</sub> |  | 2.1<br><sub>3,2,2,2,0</sub> |  | 2.1<br><sub>2,4,2,3,4</sub> |  | 0.9 | 0.3 | 1.1 | 17.5 |
| Zach Collins | 71% | 18.9<br><sub>-,28,-,11,15</sub> | 8.0<br><sub>-,8,-,3,6</sub> |  | 5.2<br><sub>-,5,-,2,2</sub> |  | 2.1<br><sub>-,4,-,0,4</sub> |  | 0.6<br><sub>-,0,-,1,0</sub> |  | 0.5 | 0.5 | 1.0 | 15.2 |
| Noa Essengue | 98% | 18.5<br><sub>8,7,14,15,15</sub> | 7.2<br><sub>5,0,1,5,8</sub> |  | 3.9<br><sub>1,1,2,3,4</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.6 | 0.2 | 0.9 | 12.1 |
| Leonard Miller | 64% | 17.6<br><sub>-,17,1,7,-</sub> | 8.2<br><sub>-,4,0,4,-</sub> |  | 4.3<br><sub>-,3,0,2,-</sub> |  | 1.1<br><sub>-,4,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.5 | 0.8 | 13.6 |
| Jordan Hawkins | 52% | 14.8<br><sub>-,-,4,-,-</sub> | 6.5<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 9.3 |
| Dailyn Swain | 67% | 11.0<br><sub>-,-,2,6,-</sub> | 4.0<br><sub>-,-,0,2,-</sub> |  | 1.8<br><sub>-,-,1,1,-</sub> |  | 1.1<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.7 | 6.9 |

</details>

<details><summary>if Norman Powell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell (CHI) | 100% | 32.1<br><sub>31,30,33,26,33</sub> | 20.7<br><sub>33,24,27,17,16</sub> | 21.5 · – | 3.5<br><sub>5,5,2,2,3</sub> | 2.5 | 2.8<br><sub>2,3,6,5,2</sub> | 2.5 | 2.5<br><sub>4,3,0,5,1</sub> | 2.5 | 1.1 | 0.2 | 2.0 | 26.9 |
| Matas Buzelis (CHI) | 99% | 30.0<br><sub>29,30,31,30,25</sub> | 17.7<br><sub>11,18,23,25,9</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 6.0<br><sub>6,9,3,5,5</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,2,0,4,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,2,3,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 1.1 | 2.1 | 25.7 |
| Isaac Okoro (CHI) | 99% | 29.2<br><sub>41,31,32,25,29</sub> | 10.5<br><sub>15,9,13,12,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,7,6,3,7</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.0<br><sub>2,4,2,4,1</sub> |  | 1.2<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.4 | 0.9 | 15.8 |
| Josh Giddey (CHI) | 99% | 28.9<br><sub>39,26,24,28,23</sub> | 13.1<br><sub>15,8,4,18,2</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>10,8,4,14,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 8.2<br><sub>14,5,8,9,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>3,2,1,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.6 | 2.6 | 28.0 |
| Nic Claxton (CHI) | 98% | 23.4<br><sub>22,-,17,22,29</sub> | 9.7<br><sub>2,-,8,14,11</sub> |  | 6.3<br><sub>6,-,2,4,7</sub> |  | 2.4<br><sub>2,-,1,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.8 | 1.1 | 18.4 |
| Patrick Williams (CHI) | 82% | 23.1<br><sub>24,26,13,13,23</sub> | 8.3<br><sub>13,14,0,2,6</sub> |  | 3.3<br><sub>4,5,0,1,3</sub> |  | 1.8<br><sub>2,1,0,2,1</sub> |  | 1.1<br><sub>4,2,0,0,0</sub> |  | 0.7 | 0.5 | 0.9 | 13.3 |
| Tre Jones (CHI) | 99% | 22.4<br><sub>15,24,23,16,25</sub> | 12.4<br><sub>4,16,16,10,12</sub> |  | 2.7<br><sub>1,0,2,2,1</sub> |  | 4.4<br><sub>3,4,6,6,7</sub> |  | 0.5<br><sub>0,1,0,0,0</sub> |  | 0.9 | 0.2 | 1.1 | 19.5 |
| Buddy Hield (CHI) | 88% | 18.9<br><sub>25,20,19,19,23</sub> | 9.4<br><sub>12,16,6,11,15</sub> |  | 2.6<br><sub>3,4,4,1,4</sub> |  | 1.6<br><sub>3,2,2,2,0</sub> |  | 1.5<br><sub>2,4,2,3,4</sub> |  | 0.7 | 0.2 | 0.9 | 13.6 |
| Zach Collins (CHI) | 71% | 16.3<br><sub>-,28,-,11,15</sub> | 7.0<br><sub>-,8,-,3,6</sub> |  | 4.5<br><sub>-,5,-,2,2</sub> |  | 1.7<br><sub>-,4,-,0,4</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.4 | 0.8 | 13.2 |
| Noa Essengue (CHI) | 98% | 14.6<br><sub>8,7,14,15,15</sub> | 5.7<br><sub>5,0,1,5,8</sub> |  | 3.2<br><sub>1,1,2,3,4</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>1,0,0,0,2</sub> |  | 0.5 | 0.2 | 0.7 | 9.7 |
| Leonard Miller (CHI) | 64% | 13.5<br><sub>-,17,1,7,-</sub> | 6.3<br><sub>-,4,0,4,-</sub> |  | 3.3<br><sub>-,3,0,2,-</sub> |  | 0.8<br><sub>-,4,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.6 | 10.5 |
| Jordan Hawkins (CHI) | 52% | 9.8<br><sub>-,-,4,-,-</sub> | 4.2<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Dailyn Swain (CHI) | 67% | 7.0<br><sub>-,-,2,6,-</sub> | 3.0<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,1,1,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.7 |
| Nikola Jokic (DEN) | 98% | 37.3<br><sub>37,37,38,39,38</sub> | 29.0<br><sub>27,26,28,24,26</sub> | 25.5 · –<br><sub>o 52% · u 48%</sub> | 12.6<br><sub>11,8,15,8,7</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 10.1<br><sub>8,10,7,9,11</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7 | 0.8 | 3.4 | 51.7 |
| Jamal Murray (DEN) | 98% | 36.5<br><sub>32,38,35,38,36</sub> | 26.3<br><sub>30,23,28,21,14</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>4,7,4,7,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>8,9,4,2,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,0,1,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.6 | 2.1 | 37.5 |
| Christian Braun (DEN) | 98% | 33.2<br><sub>37,28,33,35,31</sub> | 12.7<br><sub>12,17,10,15,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,7,3,5,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>4,1,3,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>2,1,2,1,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.4 | 0.9 | 20.0 |
| Aaron Gordon (DEN) | 98% | 30.2<br><sub>27,33,24,31,31</sub> | 14.2<br><sub>9,11,11,13,18</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>3,5,1,8,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.3<br><sub>1,1,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.4 | 1.2 | 22.3 |
| Cameron Johnson (DEN) | 98% | 30.0<br><sub>30,31,27,26,29</sub> | 14.0<br><sub>23,12,9,8,19</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,5,0,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,2,1,1,6</sub> |  | 1.8<br><sub>4,1,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.0 | 20.5 |
| DeMar DeRozan (DEN) | 91% | 22.4<br><sub>20,24,14,25,22</sub> | 11.8<br><sub>8,9,2,18,15</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,3,1,2,2</sub> |  | 3.0<br><sub>4,2,1,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.3<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.0 | 16.9 |
| Spencer Jones (DEN) | 91% | 16.6<br><sub>22,12,21,17,18</sub> | 4.0<br><sub>3,4,4,2,3</sub> |  | 2.3<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>0,1,3,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.6 | 7.2 |
| Trevon Brazile (DEN) | 98% | 14.9<br><sub>13,16,23,11,11</sub> | 4.7<br><sub>7,5,9,0,4</sub> |  | 3.8<br><sub>5,3,4,6,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 9.0 |
| Marvin Bagley III (DEN) | 98% | 12.6<br><sub>12,13,10,9,10</sub> | 6.5<br><sub>4,7,4,4,10</sub> |  | 4.0<br><sub>2,7,2,3,6</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.6 | 0.6 | 11.2 |
| Tyus Jones (DEN) | 98% | 11.7<br><sub>11,10,10,9,14</sub> | 3.0<br><sub>0,2,0,0,5</sub> |  | 1.1<br><sub>1,0,1,0,3</sub> |  | 2.1<br><sub>4,3,2,0,4</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Zeke Nnaji (DEN) | 23% | 7.0<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.3 |
| Alpha Diallo (DEN) | 38% | 6.7<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Ryan Nembhard (DEN) | 48% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matas Buzelis (CHI) | 99% | 29.9<br><sub>29,30,31,30,25</sub> | 18.0<br><sub>11,18,23,25,9</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>6,9,3,5,5</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,0,4,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,2,3,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 1.0 | 2.2 | 26.1 |
| Josh Giddey (CHI) | 99% | 29.6<br><sub>39,26,24,28,23</sub> | 14.0<br><sub>15,8,4,18,2</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>10,8,4,14,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>14,5,8,9,7</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>3,2,1,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.5 | 2.9 | 29.4 |
| Isaac Okoro (CHI) | 99% | 29.4<br><sub>41,31,32,25,29</sub> | 10.7<br><sub>15,9,13,12,9</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,7,6,3,7</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.0<br><sub>2,4,2,4,1</sub> |  | 1.2<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.4 | 0.9 | 16.2 |
| Jalen Smith (CHI) | 100% | 28.2<br><sub>32,-,28,21,-</sub> | 15.4<br><sub>15,-,17,14,-</sub> | 12.5 · – | 8.9<br><sub>12,-,11,6,-</sub> | 7.5 | 2.1<br><sub>3,-,3,3,-</sub> |  | 2.0<br><sub>1,-,3,2,-</sub> | 1.5 | 0.6 | 0.9 | 1.2 | 26.4 |
| Tre Jones (CHI) | 99% | 24.1<br><sub>15,24,23,16,25</sub> | 14.0<br><sub>4,16,16,10,12</sub> |  | 2.8<br><sub>1,0,2,2,1</sub> |  | 4.9<br><sub>3,4,6,6,7</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 1.0 | 0.2 | 1.3 | 21.6 |
| Nic Claxton (CHI) | 98% | 24.0<br><sub>22,-,17,22,29</sub> | 10.2<br><sub>2,-,8,14,11</sub> |  | 6.3<br><sub>6,-,2,4,7</sub> |  | 2.4<br><sub>2,-,1,1,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.9 | 1.1 | 18.9 |
| Patrick Williams (CHI) | 82% | 23.5<br><sub>24,26,13,13,23</sub> | 8.5<br><sub>13,14,0,2,6</sub> |  | 3.3<br><sub>4,5,0,1,3</sub> |  | 1.8<br><sub>2,1,0,2,1</sub> |  | 1.1<br><sub>4,2,0,0,0</sub> |  | 0.7 | 0.5 | 1.1 | 13.6 |
| Buddy Hield (CHI) | 88% | 20.9<br><sub>25,20,19,19,23</sub> | 10.3<br><sub>12,16,6,11,15</sub> |  | 2.8<br><sub>3,4,4,1,4</sub> |  | 1.8<br><sub>3,2,2,2,0</sub> |  | 1.7<br><sub>2,4,2,3,4</sub> |  | 0.7 | 0.2 | 1.1 | 14.9 |
| Zach Collins (CHI) | 71% | 16.3<br><sub>-,28,-,11,15</sub> | 7.1<br><sub>-,8,-,3,6</sub> |  | 4.6<br><sub>-,5,-,2,2</sub> |  | 1.7<br><sub>-,4,-,0,4</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.4 | 0.8 | 13.4 |
| Noa Essengue (CHI) | 98% | 15.0<br><sub>8,7,14,15,15</sub> | 5.9<br><sub>5,0,1,5,8</sub> |  | 3.3<br><sub>1,1,2,3,4</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.6<br><sub>1,0,0,0,2</sub> |  | 0.5 | 0.2 | 0.7 | 10.1 |
| Leonard Miller (CHI) | 64% | 14.5<br><sub>-,17,1,7,-</sub> | 6.9<br><sub>-,4,0,4,-</sub> |  | 3.6<br><sub>-,3,0,2,-</sub> |  | 0.9<br><sub>-,4,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.4 | 0.6 | 11.3 |
| Jordan Hawkins (CHI) | 52% | 11.3<br><sub>-,-,4,-,-</sub> | 5.0<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 7.2 |
| Dailyn Swain (CHI) | 67% | 7.3<br><sub>-,-,2,6,-</sub> | 2.9<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,1,1,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Nikola Jokic (DEN) | 98% | 37.2<br><sub>37,37,38,39,38</sub> | 29.0<br><sub>27,26,28,24,26</sub> | 25.5 · –<br><sub>o 52% · u 48%</sub> | 12.6<br><sub>11,8,15,8,7</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 10.1<br><sub>8,10,7,9,11</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7 | 0.9 | 3.4 | 51.7 |
| Jamal Murray (DEN) | 98% | 36.5<br><sub>32,38,35,38,36</sub> | 26.3<br><sub>30,23,28,21,14</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>4,7,4,7,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>8,9,4,2,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,0,1,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.6 | 2.1 | 37.4 |
| Christian Braun (DEN) | 98% | 33.2<br><sub>37,28,33,35,31</sub> | 12.7<br><sub>12,17,10,15,19</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,7,3,5,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>4,1,3,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>2,1,2,1,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.4 | 0.9 | 20.0 |
| Aaron Gordon (DEN) | 98% | 30.2<br><sub>27,33,24,31,31</sub> | 14.2<br><sub>9,11,11,13,18</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>3,5,1,8,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.3<br><sub>1,1,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.4 | 1.2 | 22.2 |
| Cameron Johnson (DEN) | 98% | 30.1<br><sub>30,31,27,26,29</sub> | 14.1<br><sub>23,12,9,8,19</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,5,0,5,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,2,1,1,6</sub> |  | 1.8<br><sub>4,1,0,0,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.0 | 20.6 |
| DeMar DeRozan (DEN) | 91% | 22.4<br><sub>20,24,14,25,22</sub> | 11.8<br><sub>8,9,2,18,15</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,3,1,2,2</sub> |  | 3.0<br><sub>4,2,1,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.3<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.0 | 16.9 |
| Spencer Jones (DEN) | 91% | 16.4<br><sub>22,12,21,17,18</sub> | 4.0<br><sub>3,4,4,2,3</sub> |  | 2.3<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>0,1,3,0,1</sub> |  | 0.4<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.3 | 0.6 | 7.2 |
| Trevon Brazile (DEN) | 98% | 15.0<br><sub>13,16,23,11,11</sub> | 4.7<br><sub>7,5,9,0,4</sub> |  | 3.8<br><sub>5,3,4,6,4</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 9.1 |
| Marvin Bagley III (DEN) | 98% | 12.6<br><sub>12,13,10,9,10</sub> | 6.5<br><sub>4,7,4,4,10</sub> |  | 4.0<br><sub>2,7,2,3,6</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,2</sub> |  | 0.4 | 0.6 | 0.6 | 11.1 |
| Tyus Jones (DEN) | 98% | 11.7<br><sub>11,10,10,9,14</sub> | 3.0<br><sub>0,2,0,0,5</sub> |  | 1.1<br><sub>1,0,1,0,3</sub> |  | 2.1<br><sub>4,3,2,0,4</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Zeke Nnaji (DEN) | 23% | 7.1<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.4 |
| Alpha Diallo (DEN) | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Ryan Nembhard (DEN) | 48% | 6.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |

</details>


### DAL @ UTA
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Sergio de Larrea (DAL), Dereck Lively II (DAL), P.J. Washington (DAL)

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 35.8<br><sub>39,27,38,27,34</sub> | 26.6<br><sub>43,12,18,17,33</sub> | 24.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>10,7,8,3,5</sub> |  | 6.1<br><sub>6,3,5,4,9</sub> |  | 1.4<br><sub>3,1,0,2,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.9 | 2.9 | 40.1 |
| Kyrie Irving | 98% | 34.9<br><sub>38,27,37,-,29</sub> | 24.6<br><sub>35,10,34,-,17</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>0,3,6,-,6</sub> |  | 4.5<br><sub>4,4,5,-,5</sub> |  | 3.1<br><sub>7,2,7,-,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.5 | 0.6 | 2.1 | 33.6 |
| Naji Marshall | 96% | 28.1<br><sub>25,23,30,23,27</sub> | 14.4<br><sub>6,13,12,13,12</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,1,3,2,5</sub> |  | 3.7<br><sub>2,4,5,2,2</sub> |  | 1.0<br><sub>0,1,0,3,2</sub> |  | 1.2 | 0.1 | 1.8 | 22.2 |
| Daniel Gafford | 99% | 23.2<br><sub>20,16,17,19,24</sub> | 10.0<br><sub>8,3,10,3,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>2,3,3,4,6</sub> |  | 1.6<br><sub>3,1,1,2,2</sub> |  | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.8 | 1.1 | 18.1 |
| Caleb Martin | 98% | 22.9<br><sub>19,21,33,34,20</sub> | 6.0<br><sub>0,7,15,12,8</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>3,2,8,5,5</sub> |  | 1.9<br><sub>5,5,3,5,3</sub> |  | 0.6<br><sub>0,1,1,4,2</sub> |  | 1.0 | 0.4 | 0.8 | 11.7 |
| Zaccharie Risacher | 98% | 21.9<br><sub>15,25,14,27,18</sub> | 8.0<br><sub>4,22,5,18,3</sub> |  | 4.5<br><sub>2,6,2,5,3</sub> |  | 1.1<br><sub>0,3,0,0,0</sub> |  | 0.9<br><sub>0,4,1,1,1</sub> |  | 0.8 | 0.8 | 0.9 | 13.5 |
| Walter Clayton Jr. | 96% | 20.9<br><sub>25,22,13,23,27</sub> | 7.8<br><sub>6,5,2,13,8</sub> |  | 3.2<br><sub>6,1,2,4,2</sub> |  | 3.6<br><sub>4,4,2,3,7</sub> |  | 1.1<br><sub>1,0,0,3,2</sub> |  | 0.7 | 0.2 | 1.6 | 14.6 |
| Morez Johnson Jr. | 98% | 16.6<br><sub>-,13,15,26,15</sub> | 6.0<br><sub>-,0,4,2,3</sub> |  | 3.4<br><sub>-,2,2,6,1</sub> |  | 1.4<br><sub>-,0,0,4,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.9 | 10.8 |
| Max Christie | 98% | 15.7<br><sub>5,7,-,-,8</sub> | 5.7<br><sub>0,3,-,-,5</sub> |  | 2.0<br><sub>2,2,-,-,1</sub> |  | 0.9<br><sub>0,0,-,-,2</sub> |  | 0.8<br><sub>0,1,-,-,1</sub> |  | 0.5 | 0.2 | 0.6 | 8.6 |
| Santi Aldama | 98% | 14.3<br><sub>19,10,16,-,6</sub> | 6.9<br><sub>10,3,7,-,0</sub> |  | 3.4<br><sub>4,1,2,-,0</sub> |  | 1.1<br><sub>1,1,1,-,0</sub> |  | 0.8<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.4 | 0.7 | 11.4 |
| Marcus Sasser | 67% | 11.8<br><sub>-,9,-,18,4</sub> | 4.3<br><sub>-,3,-,5,0</sub> |  | 1.1<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.8 |
| Moussa Cisse | 67% | 7.5<br><sub>-,8,-,4,4</sub> | 2.5<br><sub>-,0,-,1,0</sub> |  | 2.9<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.6 | 0.4 | 5.5 |
| Jett Howard | 63% | 6.6<br><sub>-,5,-,7,-</sub> | 2.8<br><sub>-,3,-,0,-</sub> |  | 0.8<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,1,-,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.0 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 35.0<br><sub>38,34,35,39,36</sub> | 24.3<br><sub>27,13,30,30,14</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>4,4,2,1,3</sub> |  | 7.5<br><sub>7,8,11,10,6</sub> |  | 2.6<br><sub>4,1,4,5,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 3.2 | 35.9 |
| Darryn Peterson | 98% | 31.6<br><sub>34,34,31,19,32</sub> | 18.5<br><sub>28,17,13,11,20</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>7,5,5,1,10</sub> |  | 4.4<br><sub>2,4,2,3,8</sub> |  | 2.0<br><sub>4,3,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.7 | 2.0 | 27.6 |
| Ace Bailey | 99% | 30.7<br><sub>35,30,23,27,24</sub> | 15.5<br><sub>21,7,5,19,7</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,8,1,8,7</sub> |  | 2.2<br><sub>1,4,4,3,1</sub> |  | 2.1<br><sub>3,1,1,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.9 | 1.8 | 23.3 |
| Jaxson Hayes | 88% | 25.2<br><sub>13,-,-,25,28</sub> | 10.5<br><sub>12,-,-,6,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,-,-,7,14</sub> |  | 1.4<br><sub>1,-,-,2,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.6 |
| Josh Green | 97% | 24.3<br><sub>14,15,13,28,29</sub> | 6.0<br><sub>2,6,9,11,8</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>0,1,1,2,4</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.7<br><sub>0,2,1,2,2</sub> |  | 0.9 | 0.2 | 0.8 | 9.7 |
| Brice Sensabaugh | 99% | 23.9<br><sub>27,30,35,14,26</sub> | 15.6<br><sub>7,14,40,8,18</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 4.0<br><sub>3,7,11,3,3</sub> |  | 2.2<br><sub>1,2,5,2,1</sub> |  | 2.2<br><sub>1,0,8,0,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.3 | 1.9 | 21.8 |
| Svi Mykhailiuk | 98% | 23.3<br><sub>7,21,33,34,28</sub> | 8.9<br><sub>0,6,8,15,11</sub> |  | 2.7<br><sub>1,2,7,3,7</sub> |  | 2.1<br><sub>0,3,5,5,2</sub> |  | 1.5<br><sub>0,2,2,4,3</sub> |  | 0.7 | 0.1 | 1.0 | 13.8 |
| Mo Bamba | 91% | 21.4<br><sub>20,36,31,23,20</sub> | 7.9<br><sub>9,26,15,6,2</sub> |  | 7.4<br><sub>9,5,10,16,2</sub> |  | 1.2<br><sub>1,4,3,0,0</sub> |  | 0.5<br><sub>0,6,1,0,0</sub> |  | 0.6 | 1.7 | 0.9 | 16.5 |
| Josh Okogie | 98% | 19.5<br><sub>22,27,22,15,17</sub> | 5.6<br><sub>7,7,9,3,3</sub> |  | 3.0<br><sub>2,6,2,0,2</sub> |  | 1.2<br><sub>1,0,4,0,2</sub> |  | 0.6<br><sub>2,2,1,0,0</sub> |  | 1.0 | 0.3 | 0.7 | 9.8 |
| Isaiah Collier | 58% | 14.4<br><sub>16,-,-,10,-</sub> | 7.2<br><sub>3,-,-,0,-</sub> |  | 2.1<br><sub>2,-,-,1,-</sub> |  | 3.9<br><sub>5,-,-,2,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.7 | 0.2 | 1.3 | 13.1 |
| Kyle Filipowski | 52% | 11.4<br><sub>2,-,-,6,-</sub> | 6.3<br><sub>2,-,-,0,-</sub> |  | 3.6<br><sub>0,-,-,3,-</sub> |  | 1.2<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.8 | 11.2 |
| Tony Bradley | 52% | 9.2<br><sub>12,12,17,-,-</sub> | 3.0<br><sub>0,6,3,-,-</sub> |  | 3.1<br><sub>5,2,7,-,-</sub> |  | 0.5<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 6.6 |

</details>


### IND @ NYK
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.7–113.7 | IND 28% | 3.51 / 1.40 | NYK -8.5 | 219.5 | NYK -9.5 covers 46%; o216.5 56% |
| Expected (weighted by chance each plays) | 106.0–116.5 | IND 23% | 4.37 / 1.30 | NYK -10.5 | 222.5 | NYK -9.5 covers 53%; o216.5 62% |
| if OG Anunoby plays | 105.7–115.6 | IND 24% | 4.14 / 1.32 | NYK -10.5 | 221.5 | NYK -9.5 covers 51%; o216.5 60% |
| if Pascal Siakam plays | 106.6–113.9 | IND 30% | 3.33 / 1.43 | NYK -7.5 | 220.5 | NYK -9.5 covers 44%; o216.5 58% |
| if Karl-Anthony Towns plays | 105.4–116.0 | IND 23% | 4.37 / 1.30 | NYK -10.5 | 221.5 | NYK -9.5 covers 53%; o216.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| OG Anunoby (NYK) | Day-To-Day | 70% | 35.6 | 20.3 | 6.2 | 2.2 | 2.4 | 1.6 | 0.9 | 1.8 | 28.7 | full tables below |
| Pascal Siakam (IND) | Questionable | 55% | 33.8 | 21.9 | 6.1 | 3.8 | 1.6 | 1.0 | 0.3 | 2.0 | 31.8 | full tables below |
| Karl-Anthony Towns (NYK) | Day-To-Day | 70% | 34.6 | 23.2 | 14.9 | 4.5 | 2.0 | 1.1 | 0.7 | 2.8 | 42.5 | full tables below |
| Jordan Clarkson (NYK) | Day-To-Day | 70% | 16.1 | 8.0 | 2.4 | 1.1 | 0.7 | 0.5 | 0.1 | 0.8 | 11.5 | small |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 91% | 34.2<br><sub>34,34,-,-,26</sub> | 17.7<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> |  | 8.2<br><sub>10,6,-,-,8</sub> |  | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.8 | 28.8 |
| Aaron Nesmith | 93% | 31.8<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,7,4,3,10</sub> |  | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.5 | 1.6 | 20.4 |
| Kelly Oubre Jr. | 91% | 27.8<br><sub>34,30,29,23,23</sub> | 12.7<br><sub>14,16,16,17,17</sub> | 13.5 · –<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>6,5,4,4,6</sub> |  | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.4<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 57%</sub> | 0.8 | 0.6 | 1.3 | 18.4 |
| Ivica Zubac | 88% | 27.4<br><sub>31,26,22,24,27</sub> | 11.8<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>12,13,5,3,10</sub> |  | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.6 | 22.8 |
| Quenton Jackson | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 1.0 | 0.2 | 1.6 | 18.1 |
| Obi Toppin | 88% | 24.1<br><sub>16,16,14,17,26</sub> | 12.9<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>3,3,2,1,3</sub> |  | 2.3<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.3 | 1.2 | 19.7 |
| Jarace Walker | 88% | 20.2<br><sub>7,-,14,17,11</sub> | 8.5<br><sub>1,-,2,1,8</sub> |  | 4.1<br><sub>1,-,5,3,1</sub> |  | 2.1<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.6 |
| Jalen Slawson | 91% | 17.8<br><sub>12,10,14,12,14</sub> | 5.5<br><sub>2,1,8,5,4</sub> |  | 3.5<br><sub>3,4,5,4,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.7 |
| Braden Smith | 67% | 16.5<br><sub>-,-,-,18,11</sub> | 5.6<br><sub>-,-,-,8,5</sub> |  | 1.8<br><sub>-,-,-,5,3</sub> |  | 3.2<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.8 | 10.5 |
| Jay Huff | 91% | 15.7<br><sub>11,8,18,15,1</sub> | 6.7<br><sub>6,8,11,5,0</sub> |  | 2.8<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.8<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.6 |
| Larry Nance Jr. | 97% | 15.3<br><sub>5,14,7,9,11</sub> | 5.1<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.6<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.8 |
| Kobe Brown | 86% | 14.4<br><sub>-,-,3,2,-</sub> | 5.1<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.8 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 36.0<br><sub>35,36,41,34,35</sub> | 34.0<br><sub>27,33,28,31,21</sub> | 27.5 · –<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>3,1,1,5,2</sub> |  | 6.7<br><sub>5,11,9,5,7</sub> |  | 3.2<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.4 | 44.4 |
| Mikal Bridges | 99% | 32.4<br><sub>17,29,32,30,31</sub> | 14.7<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,3,7,5,3</sub> |  | 3.2<br><sub>2,3,3,1,3</sub> |  | 1.6<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 1.3 | 22.2 |
| Josh Hart | 98% | 32.0<br><sub>26,23,26,31,28</sub> | 11.9<br><sub>6,0,0,5,11</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 8.0<br><sub>4,5,5,4,6</sub> |  | 4.2<br><sub>3,4,2,2,2</sub> |  | 1.5<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.3 | 1.7 | 24.1 |
| Landry Shamet | 99% | 31.2<br><sub>29,21,30,24,30</sub> | 13.6<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>2,3,2,1,1</sub> |  | 1.9<br><sub>4,1,0,1,2</sub> |  | 2.4<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 1.1 | 18.0 |
| Miles McBride | 99% | 22.7<br><sub>27,22,14,9,8</sub> | 9.4<br><sub>19,9,3,3,3</sub> |  | 2.1<br><sub>2,1,1,0,0</sub> |  | 1.7<br><sub>2,1,0,1,0</sub> |  | 1.7<br><sub>5,3,1,1,0</sub> |  | 0.8 | 0.2 | 0.6 | 13.2 |
| Andre Drummond | 98% | 21.8<br><sub>14,14,7,11,15</sub> | 6.8<br><sub>0,0,2,2,4</sub> |  | 10.5<br><sub>4,6,3,8,4</sub> |  | 1.5<br><sub>3,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.0 | 18.8 |
| Tyler Kolek | 96% | 19.8<br><sub>13,19,16,13,12</sub> | 7.6<br><sub>4,5,0,4,6</sub> |  | 2.7<br><sub>1,6,0,1,3</sub> |  | 5.2<br><sub>4,2,7,3,5</sub> |  | 0.9<br><sub>0,1,0,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 15.5 |
| Mohamed Diawara | 47% | 18.5<br><sub>11,-,-,-,-</sub> | 7.2<br><sub>2,-,-,-,-</sub> |  | 3.2<br><sub>0,-,-,-,-</sub> |  | 1.8<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.7 | 12.2 |
| Jose Alvarado | 71% | 17.9<br><sub>-,-,2,7,13</sub> | 7.2<br><sub>-,-,0,2,2</sub> |  | 2.4<br><sub>-,-,0,0,2</sub> |  | 2.9<br><sub>-,-,1,4,1</sub> |  | 0.9<br><sub>-,-,0,0,0</sub> |  | 0.9 | 0.1 | 1.0 | 12.5 |
| Dalton Knecht | 64% | 15.5<br><sub>-,-,-,-,-</sub> | 6.4<br><sub>-,-,-,-,-</sub> |  | 2.9<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.4 | 10.1 |
| Pacome Dadiet | 38% | 14.3<br><sub>-,1,-,-,-</sub> | 5.6<br><sub>-,0,-,-,-</sub> |  | 2.6<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 9.0 |
| James Wiseman | 43% | 13.1<br><sub>-,-,3,-,-</sub> | 4.4<br><sub>-,-,0,-,-</sub> |  | 4.5<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.6 | 0.8 | 9.6 |
| Jaden Akins | 38% | 10.9<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.4 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>if Karl-Anthony Towns plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 34.2<br><sub>34,34,-,-,26</sub> | 17.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> |  | 8.2<br><sub>10,6,-,-,8</sub> |  | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.8 | 28.8 |
| Aaron Nesmith (IND) | 93% | 31.8<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,7,4,3,10</sub> |  | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.5 | 1.6 | 20.4 |
| Kelly Oubre Jr. (IND) | 91% | 27.8<br><sub>34,30,29,23,23</sub> | 12.7<br><sub>14,16,16,17,17</sub> | 13.5 · –<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>6,5,4,4,6</sub> |  | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.4<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 57%</sub> | 0.9 | 0.6 | 1.3 | 18.4 |
| Ivica Zubac (IND) | 88% | 27.3<br><sub>31,26,22,24,27</sub> | 11.7<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>12,13,5,3,10</sub> |  | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.6 | 22.8 |
| Quenton Jackson (IND) | 98% | 24.2<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 1.0 | 0.2 | 1.7 | 18.0 |
| Obi Toppin (IND) | 88% | 24.1<br><sub>16,16,14,17,26</sub> | 12.8<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>3,3,2,1,3</sub> |  | 2.3<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.3 | 1.2 | 19.6 |
| Jarace Walker (IND) | 88% | 20.2<br><sub>7,-,14,17,11</sub> | 8.4<br><sub>1,-,2,1,8</sub> |  | 4.1<br><sub>1,-,5,3,1</sub> |  | 2.0<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.6 |
| Jalen Slawson (IND) | 91% | 17.7<br><sub>12,10,14,12,14</sub> | 5.5<br><sub>2,1,8,5,4</sub> |  | 3.4<br><sub>3,4,5,4,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.7 |
| Braden Smith (IND) | 67% | 16.6<br><sub>-,-,-,18,11</sub> | 5.7<br><sub>-,-,-,8,5</sub> |  | 1.8<br><sub>-,-,-,5,3</sub> |  | 3.2<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 10.6 |
| Jay Huff (IND) | 91% | 15.9<br><sub>11,8,18,15,1</sub> | 6.8<br><sub>6,8,11,5,0</sub> |  | 2.9<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.8<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.8 |
| Larry Nance Jr. (IND) | 97% | 15.3<br><sub>5,14,7,9,11</sub> | 5.1<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.6<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.8 |
| Kobe Brown (IND) | 86% | 14.4<br><sub>-,-,3,2,-</sub> | 5.1<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.8 |
| Jalen Brunson (NYK) | 99% | 36.2<br><sub>35,36,41,34,35</sub> | 31.5<br><sub>27,33,28,31,21</sub> | 27.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>3,1,1,5,2</sub> |  | 6.8<br><sub>5,11,9,5,7</sub> |  | 3.0<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.4 | 41.7 |
| Karl-Anthony Towns (NYK) | 100% | 34.6<br><sub>34,34,43,36,33</sub> | 23.2<br><sub>21,23,28,16,22</sub> | 20.5 · – | 14.9<br><sub>11,15,17,16,12</sub> |  | 4.5<br><sub>8,5,3,8,4</sub> |  | 2.0<br><sub>2,3,3,1,2</sub> | 1.5 | 1.1 | 0.7 | 2.8 | 42.5 |
| Josh Hart (NYK) | 98% | 31.8<br><sub>26,23,26,31,28</sub> | 10.2<br><sub>6,0,0,5,11</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 7.5<br><sub>4,5,5,4,6</sub> |  | 4.0<br><sub>3,4,2,2,2</sub> |  | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.3 | 1.6 | 21.7 |
| Mikal Bridges (NYK) | 99% | 31.4<br><sub>17,29,32,30,31</sub> | 12.5<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>1,3,7,5,3</sub> |  | 2.9<br><sub>2,3,3,1,3</sub> |  | 1.4<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.5 | 1.2 | 19.3 |
| Landry Shamet (NYK) | 99% | 29.4<br><sub>29,21,30,24,30</sub> | 11.7<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,3,2,1,1</sub> |  | 1.7<br><sub>4,1,0,1,2</sub> |  | 2.1<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 0.9 | 15.7 |
| Miles McBride (NYK) | 99% | 18.8<br><sub>27,22,14,9,8</sub> | 7.0<br><sub>19,9,3,3,3</sub> |  | 1.6<br><sub>2,1,1,0,0</sub> |  | 1.4<br><sub>2,1,0,1,0</sub> |  | 1.2<br><sub>5,3,1,1,0</sub> |  | 0.7 | 0.2 | 0.4 | 10.0 |
| Tyler Kolek (NYK) | 96% | 16.4<br><sub>13,19,16,13,12</sub> | 5.5<br><sub>4,5,0,4,6</sub> |  | 2.2<br><sub>1,6,0,1,3</sub> |  | 4.3<br><sub>4,2,7,3,5</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 12.1 |
| Andre Drummond (NYK) | 98% | 15.3<br><sub>14,14,7,11,15</sub> | 4.7<br><sub>0,0,2,2,4</sub> |  | 7.4<br><sub>4,6,3,8,4</sub> |  | 1.0<br><sub>3,0,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.7 | 13.1 |
| Mohamed Diawara (NYK) | 47% | 14.2<br><sub>11,-,-,-,-</sub> | 4.9<br><sub>2,-,-,-,-</sub> |  | 2.4<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.6<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 8.6 |
| Jose Alvarado (NYK) | 71% | 14.1<br><sub>-,-,2,7,13</sub> | 5.3<br><sub>-,-,0,2,2</sub> |  | 1.8<br><sub>-,-,0,0,2</sub> |  | 2.2<br><sub>-,-,1,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.7 | 0.1 | 0.8 | 9.3 |
| Dalton Knecht (NYK) | 64% | 11.0<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 7.1 |
| Pacome Dadiet (NYK) | 38% | 8.8<br><sub>-,1,-,-,-</sub> | 3.4<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| Tyler Nickel (NYK) | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Jaden Akins (NYK) | 38% | 8.0<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| James Wiseman (NYK) | 43% | 8.0<br><sub>-,-,3,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.7<br><sub>-,-,3,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.7 |

</details>

<details><summary>if Pascal Siakam plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam (IND) | 100% | 33.8<br><sub>32,32,34,33,30</sub> | 21.9<br><sub>28,19,31,24,21</sub> | 20.5 · – | 6.1<br><sub>8,3,2,4,7</sub> |  | 3.8<br><sub>5,2,2,3,2</sub> |  | 1.6<br><sub>2,2,0,2,2</sub> | 1.5 | 1.0 | 0.3 | 2.0 | 31.8 |
| Andrew Nembhard (IND) | 91% | 33.0<br><sub>34,34,-,-,26</sub> | 15.6<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> |  | 7.7<br><sub>10,6,-,-,8</sub> |  | 1.9<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.3 | 26.2 |
| Aaron Nesmith (IND) | 93% | 29.2<br><sub>22,33,36,29,29</sub> | 11.7<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>1,7,4,3,10</sub> |  | 2.0<br><sub>1,1,4,3,7</sub> |  | 1.7<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.2 | 17.5 |
| Ivica Zubac (IND) | 88% | 26.1<br><sub>31,26,22,24,27</sub> | 10.9<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 8.2<br><sub>12,13,5,3,10</sub> |  | 1.7<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.4 | 20.9 |
| Kelly Oubre Jr. (IND) | 91% | 25.3<br><sub>34,30,29,23,23</sub> | 10.8<br><sub>14,16,16,17,17</sub> | 13.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>6,5,4,4,6</sub> |  | 1.2<br><sub>1,0,2,0,0</sub> |  | 1.2<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 57%</sub> | 0.8 | 0.5 | 1.1 | 15.9 |
| Quenton Jackson (IND) | 98% | 21.1<br><sub>21,20,30,22,18</sub> | 8.9<br><sub>4,3,15,15,3</sub> |  | 2.9<br><sub>2,5,6,2,2</sub> |  | 3.0<br><sub>2,4,8,3,2</sub> |  | 0.9<br><sub>1,1,1,2,1</sub> |  | 0.8 | 0.2 | 1.4 | 14.8 |
| Obi Toppin (IND) | 88% | 19.6<br><sub>16,16,14,17,26</sub> | 10.2<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,3,2,1,3</sub> |  | 1.7<br><sub>1,1,1,1,2</sub> |  | 1.3<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5 | 0.2 | 0.9 | 15.6 |
| Jarace Walker (IND) | 88% | 15.6<br><sub>7,-,14,17,11</sub> | 6.0<br><sub>1,-,2,1,8</sub> |  | 3.1<br><sub>1,-,5,3,1</sub> |  | 1.4<br><sub>0,-,2,1,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.2 | 0.8 | 10.5 |
| Jalen Slawson (IND) | 91% | 13.4<br><sub>12,10,14,12,14</sub> | 3.9<br><sub>2,1,8,5,4</sub> |  | 2.7<br><sub>3,4,5,4,2</sub> |  | 1.2<br><sub>1,0,2,2,2</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.6 | 0.5 | 0.6 | 7.8 |
| Braden Smith (IND) | 67% | 13.3<br><sub>-,-,-,18,11</sub> | 4.3<br><sub>-,-,-,8,5</sub> |  | 1.4<br><sub>-,-,-,5,3</sub> |  | 2.5<br><sub>-,-,-,3,5</sub> |  | 0.3<br><sub>-,-,-,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 8.3 |
| Jay Huff (IND) | 91% | 11.9<br><sub>11,8,18,15,1</sub> | 4.9<br><sub>6,8,11,5,0</sub> |  | 2.1<br><sub>4,1,0,3,0</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.6<br><sub>0,2,3,0,0</sub> |  | 0.2 | 0.7 | 0.5 | 7.8 |
| Larry Nance Jr. (IND) | 97% | 11.7<br><sub>5,14,7,9,11</sub> | 3.7<br><sub>5,2,4,3,7</sub> |  | 2.1<br><sub>0,2,2,1,2</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.4<br><sub>1,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Kobe Brown (IND) | 86% | 9.4<br><sub>-,-,3,2,-</sub> | 3.1<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| Jalen Brunson (NYK) | 99% | 36.0<br><sub>35,36,41,34,35</sub> | 34.1<br><sub>27,33,28,31,21</sub> | 27.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>3,1,1,5,2</sub> |  | 6.7<br><sub>5,11,9,5,7</sub> |  | 3.2<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.4 | 44.5 |
| Mikal Bridges (NYK) | 99% | 32.4<br><sub>17,29,32,30,31</sub> | 14.7<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>1,3,7,5,3</sub> |  | 3.2<br><sub>2,3,3,1,3</sub> |  | 1.6<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 1.3 | 22.2 |
| Josh Hart (NYK) | 98% | 32.0<br><sub>26,23,26,31,28</sub> | 11.9<br><sub>6,0,0,5,11</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 8.0<br><sub>4,5,5,4,6</sub> |  | 4.2<br><sub>3,4,2,2,2</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.3 | 1.7 | 24.1 |
| Landry Shamet (NYK) | 99% | 31.1<br><sub>29,21,30,24,30</sub> | 13.5<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>2,3,2,1,1</sub> |  | 1.9<br><sub>4,1,0,1,2</sub> |  | 2.4<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 1.1 | 18.0 |
| Miles McBride (NYK) | 99% | 22.7<br><sub>27,22,14,9,8</sub> | 9.5<br><sub>19,9,3,3,3</sub> |  | 2.1<br><sub>2,1,1,0,0</sub> |  | 1.7<br><sub>2,1,0,1,0</sub> |  | 1.7<br><sub>5,3,1,1,0</sub> |  | 0.8 | 0.2 | 0.6 | 13.3 |
| Andre Drummond (NYK) | 98% | 21.8<br><sub>14,14,7,11,15</sub> | 6.8<br><sub>0,0,2,2,4</sub> |  | 10.4<br><sub>4,6,3,8,4</sub> |  | 1.5<br><sub>3,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.0 | 18.8 |
| Tyler Kolek (NYK) | 96% | 19.8<br><sub>13,19,16,13,12</sub> | 7.6<br><sub>4,5,0,4,6</sub> |  | 2.8<br><sub>1,6,0,1,3</sub> |  | 5.2<br><sub>4,2,7,3,5</sub> |  | 1.0<br><sub>0,1,0,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 15.5 |
| Mohamed Diawara (NYK) | 47% | 18.4<br><sub>11,-,-,-,-</sub> | 7.3<br><sub>2,-,-,-,-</sub> |  | 3.2<br><sub>0,-,-,-,-</sub> |  | 1.8<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.7 | 12.3 |
| Jose Alvarado (NYK) | 71% | 17.9<br><sub>-,-,2,7,13</sub> | 7.2<br><sub>-,-,0,2,2</sub> |  | 2.4<br><sub>-,-,0,0,2</sub> |  | 2.9<br><sub>-,-,1,4,1</sub> |  | 0.9<br><sub>-,-,0,0,0</sub> |  | 0.9 | 0.1 | 1.0 | 12.5 |
| Dalton Knecht (NYK) | 64% | 15.5<br><sub>-,-,-,-,-</sub> | 6.5<br><sub>-,-,-,-,-</sub> |  | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.4 | 10.1 |
| Pacome Dadiet (NYK) | 38% | 14.3<br><sub>-,1,-,-,-</sub> | 5.7<br><sub>-,0,-,-,-</sub> |  | 2.7<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 9.1 |
| James Wiseman (NYK) | 43% | 13.1<br><sub>-,-,3,-,-</sub> | 4.4<br><sub>-,-,0,-,-</sub> |  | 4.5<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.6 | 0.7 | 9.5 |
| Jaden Akins (NYK) | 38% | 11.0<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 1.4 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |

</details>

<details><summary>if OG Anunoby plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 91% | 34.1<br><sub>34,34,-,-,26</sub> | 17.7<br><sub>17,12,-,-,12</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,4,-,-,3</sub> |  | 8.2<br><sub>10,6,-,-,8</sub> |  | 2.1<br><sub>3,1,-,-,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 2.8 | 28.8 |
| Aaron Nesmith (IND) | 93% | 31.9<br><sub>22,33,36,29,29</sub> | 13.8<br><sub>2,18,12,2,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,7,4,3,10</sub> |  | 2.4<br><sub>1,1,4,3,7</sub> |  | 2.0<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.5 | 1.6 | 20.4 |
| Kelly Oubre Jr. (IND) | 91% | 27.7<br><sub>34,30,29,23,23</sub> | 12.7<br><sub>14,16,16,17,17</sub> | 13.5 · –<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>6,5,4,4,6</sub> |  | 1.5<br><sub>1,0,2,0,0</sub> |  | 1.4<br><sub>0,1,2,2,3</sub> | 1.5<br><sub>o 42% · u 57%</sub> | 0.9 | 0.6 | 1.2 | 18.4 |
| Ivica Zubac (IND) | 88% | 27.3<br><sub>31,26,22,24,27</sub> | 11.8<br><sub>20,12,8,4,21</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>12,13,5,3,10</sub> |  | 2.0<br><sub>1,1,2,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 1.6 | 22.8 |
| Quenton Jackson (IND) | 98% | 24.3<br><sub>21,20,30,22,18</sub> | 11.0<br><sub>4,3,15,15,3</sub> |  | 3.3<br><sub>2,5,6,2,2</sub> |  | 3.8<br><sub>2,4,8,3,2</sub> |  | 1.2<br><sub>1,1,1,2,1</sub> |  | 1.0 | 0.2 | 1.7 | 18.0 |
| Obi Toppin (IND) | 88% | 24.0<br><sub>16,16,14,17,26</sub> | 12.8<br><sub>8,9,5,6,17</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>3,3,2,1,3</sub> |  | 2.2<br><sub>1,1,1,1,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.3 | 1.2 | 19.5 |
| Jarace Walker (IND) | 88% | 20.2<br><sub>7,-,14,17,11</sub> | 8.4<br><sub>1,-,2,1,8</sub> |  | 4.1<br><sub>1,-,5,3,1</sub> |  | 2.0<br><sub>0,-,2,1,3</sub> |  | 1.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.6 |
| Jalen Slawson (IND) | 91% | 17.8<br><sub>12,10,14,12,14</sub> | 5.5<br><sub>2,1,8,5,4</sub> |  | 3.5<br><sub>3,4,5,4,2</sub> |  | 1.7<br><sub>1,0,2,2,2</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.8 | 0.7 | 0.8 | 10.7 |
| Braden Smith (IND) | 67% | 16.5<br><sub>-,-,-,18,11</sub> | 5.6<br><sub>-,-,-,8,5</sub> |  | 1.7<br><sub>-,-,-,5,3</sub> |  | 3.2<br><sub>-,-,-,3,5</sub> |  | 0.5<br><sub>-,-,-,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 10.5 |
| Jay Huff (IND) | 91% | 15.8<br><sub>11,8,18,15,1</sub> | 6.8<br><sub>6,8,11,5,0</sub> |  | 2.9<br><sub>4,1,0,3,0</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 0.8<br><sub>0,2,3,0,0</sub> |  | 0.3 | 0.9 | 0.7 | 10.7 |
| Larry Nance Jr. (IND) | 97% | 15.3<br><sub>5,14,7,9,11</sub> | 5.1<br><sub>5,2,4,3,7</sub> |  | 2.8<br><sub>0,2,2,1,2</sub> |  | 0.9<br><sub>0,1,2,0,0</sub> |  | 0.6<br><sub>1,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 8.9 |
| Kobe Brown (IND) | 86% | 14.5<br><sub>-,-,3,2,-</sub> | 5.1<br><sub>-,-,0,0,-</sub> |  | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.8 |
| Jalen Brunson (NYK) | 99% | 36.0<br><sub>35,36,41,34,35</sub> | 31.7<br><sub>27,33,28,31,21</sub> | 27.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>3,1,1,5,2</sub> |  | 7.0<br><sub>5,11,9,5,7</sub> |  | 3.0<br><sub>3,4,3,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.5 | 42.2 |
| OG Anunoby (NYK) | 100% | 35.6<br><sub>34,33,44,36,36</sub> | 20.3<br><sub>14,11,21,16,15</sub> |  | 6.2<br><sub>6,2,9,4,7</sub> |  | 2.2<br><sub>2,1,1,0,2</sub> |  | 2.4<br><sub>2,2,2,1,1</sub> |  | 1.6 | 0.9 | 1.8 | 28.7 |
| Josh Hart (NYK) | 98% | 31.6<br><sub>26,23,26,31,28</sub> | 10.6<br><sub>6,0,0,5,11</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 7.8<br><sub>4,5,5,4,6</sub> |  | 4.1<br><sub>3,4,2,2,2</sub> |  | 1.4<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.3 | 1.6 | 22.4 |
| Mikal Bridges (NYK) | 99% | 31.2<br><sub>17,29,32,30,31</sub> | 12.8<br><sub>2,18,5,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>1,3,7,5,3</sub> |  | 3.1<br><sub>2,3,3,1,3</sub> |  | 1.4<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 1.2 | 19.9 |
| Landry Shamet (NYK) | 99% | 29.3<br><sub>29,21,30,24,30</sub> | 11.8<br><sub>12,5,23,12,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,3,2,1,1</sub> |  | 1.8<br><sub>4,1,0,1,2</sub> |  | 2.1<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 0.9 | 15.9 |
| Miles McBride (NYK) | 99% | 19.0<br><sub>27,22,14,9,8</sub> | 7.5<br><sub>19,9,3,3,3</sub> |  | 1.6<br><sub>2,1,1,0,0</sub> |  | 1.5<br><sub>2,1,0,1,0</sub> |  | 1.2<br><sub>5,3,1,1,0</sub> |  | 0.7 | 0.2 | 0.5 | 10.6 |
| Andre Drummond (NYK) | 98% | 17.3<br><sub>14,14,7,11,15</sub> | 5.3<br><sub>0,0,2,2,4</sub> |  | 8.5<br><sub>4,6,3,8,4</sub> |  | 1.2<br><sub>3,0,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.6 | 0.8 | 15.0 |
| Tyler Kolek (NYK) | 96% | 16.2<br><sub>13,19,16,13,12</sub> | 5.7<br><sub>4,5,0,4,6</sub> |  | 2.2<br><sub>1,6,0,1,3</sub> |  | 4.4<br><sub>4,2,7,3,5</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.1 | 0.9 | 12.3 |
| Jose Alvarado (NYK) | 71% | 13.9<br><sub>-,-,2,7,13</sub> | 5.3<br><sub>-,-,0,2,2</sub> |  | 1.8<br><sub>-,-,0,0,2</sub> |  | 2.3<br><sub>-,-,1,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.7 | 0.1 | 0.8 | 9.4 |
| Mohamed Diawara (NYK) | 47% | 13.0<br><sub>11,-,-,-,-</sub> | 4.6<br><sub>2,-,-,-,-</sub> |  | 2.2<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.6<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 8.3 |
| Dalton Knecht (NYK) | 64% | 9.1<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 6.0 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| James Wiseman (NYK) | 43% | 8.5<br><sub>-,-,3,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 2.9<br><sub>-,-,3,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.6 | 6.2 |
| Pacome Dadiet (NYK) | 38% | 7.9<br><sub>-,1,-,-,-</sub> | 3.1<br><sub>-,0,-,-,-</sub> |  | 1.4<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.0 |
| Jaden Akins (NYK) | 38% | 7.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |

</details>


### BOS @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW), Mitchell Robinson (BOS), Jayson Tatum (BOS), Derrick White (BOS)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George | 98% | 33.1<br><sub>30,-,25,36,23</sub> | 22.7<br><sub>36,-,7,22,10</sub> |  | 5.7<br><sub>5,-,7,8,4</sub> |  | 4.6<br><sub>1,-,6,3,1</sub> |  | 3.2<br><sub>6,-,1,5,1</sub> |  | 1.9 | 0.5 | 2.9 | 33.0 |
| Payton Pritchard | 99% | 32.2<br><sub>30,31,19,32,30</sub> | 18.9<br><sub>18,14,10,21,15</sub> |  | 3.9<br><sub>6,1,1,4,1</sub> |  | 5.7<br><sub>5,1,6,5,2</sub> |  | 2.8<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.9 | 28.6 |
| Neemias Queta | 98% | 27.9<br><sub>22,31,15,-,27</sub> | 12.3<br><sub>4,11,8,-,17</sub> |  | 9.7<br><sub>6,13,6,-,10</sub> |  | 2.5<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.3 | 1.6 | 24.5 |
| Sam Hauser | 99% | 26.8<br><sub>18,24,11,25,17</sub> | 10.5<br><sub>12,8,8,12,9</sub> |  | 4.1<br><sub>5,9,1,1,2</sub> |  | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.2<br><sub>4,2,2,4,3</sub> |  | 0.7 | 0.2 | 0.5 | 16.3 |
| Baylor Scheierman | 99% | 24.1<br><sub>18,29,18,11,13</sub> | 8.0<br><sub>5,9,12,0,0</sub> |  | 4.5<br><sub>3,7,5,1,1</sub> |  | 2.2<br><sub>2,3,3,1,1</sub> |  | 1.3<br><sub>1,3,2,0,0</sub> |  | 1.1 | 0.1 | 1.1 | 14.7 |
| Jordan Walsh | 98% | 21.4<br><sub>19,18,21,17,4</sub> | 6.8<br><sub>8,6,11,6,0</sub> |  | 4.0<br><sub>2,3,1,2,0</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 0.8<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.3 | 0.8 | 11.9 |
| Hugo Gonzalez | 98% | 20.7<br><sub>19,8,18,4,16</sub> | 6.6<br><sub>10,0,9,0,2</sub> |  | 4.4<br><sub>2,1,5,2,6</sub> |  | 1.1<br><sub>2,0,2,0,0</sub> |  | 0.7<br><sub>2,0,2,0,0</sub> |  | 0.8 | 0.4 | 1.0 | 12.1 |
| Devin Carter | 91% | 20.1<br><sub>-,-,12,-,-</sub> | 8.8<br><sub>-,-,0,-,-</sub> |  | 3.7<br><sub>-,-,2,-,-</sub> |  | 2.9<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.1 | 0.3 | 1.6 | 15.4 |
| Chris Cenac Jr. | 63% | 18.2<br><sub>-,-,7,12,17</sub> | 7.1<br><sub>-,-,6,4,6</sub> |  | 4.2<br><sub>-,-,3,2,6</sub> |  | 0.9<br><sub>-,-,0,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.3 | 0.9 | 12.2 |
| Luka Garza | 98% | 17.7<br><sub>9,11,14,18,5</sub> | 8.5<br><sub>2,5,2,3,0</sub> |  | 4.2<br><sub>0,1,3,0,1</sub> |  | 2.0<br><sub>2,0,5,4,1</sub> |  | 1.0<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.5 | 0.9 | 14.7 |
| Mike Conley | 35% | 14.0<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.2 | 0.7 | 7.6 |
| Ron Harper Jr. | 52% | 13.9<br><sub>4,-,12,-,-</sub> | 5.5<br><sub>0,-,10,-,-</sub> |  | 2.0<br><sub>1,-,1,-,-</sub> |  | 0.9<br><sub>0,-,0,-,-</sub> |  | 0.8<br><sub>0,-,2,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 8.4 |
| Dillon Mitchell | 35% | 11.3<br><sub>-,-,-,-,-</sub> | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.6 | 1.5 |
| Amari Williams | 23% | 9.1<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.7 | 5.5 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 32.7<br><sub>36,24,33,30,33</sub> | 18.4<br><sub>25,3,28,13,11</sub> |  | 7.0<br><sub>10,7,8,5,8</sub> |  | 4.0<br><sub>0,1,3,4,7</sub> |  | 1.8<br><sub>2,0,2,0,1</sub> |  | 0.9 | 0.7 | 2.7 | 29.3 |
| Brandin Podziemski | 97% | 32.6<br><sub>37,22,30,29,32</sub> | 16.2<br><sub>22,8,15,10,15</sub> |  | 5.0<br><sub>6,3,6,3,3</sub> |  | 4.1<br><sub>4,0,3,4,2</sub> |  | 2.2<br><sub>4,2,3,0,0</sub> |  | 0.9 | 0.2 | 1.6 | 25.2 |
| Draymond Green | 96% | 25.7<br><sub>27,16,25,23,-</sub> | 5.7<br><sub>7,4,2,3,-</sub> |  | 4.6<br><sub>5,3,8,1,-</sub> |  | 5.7<br><sub>7,3,5,2,-</sub> |  | 0.7<br><sub>1,0,0,1,-</sub> |  | 0.8 | 0.7 | 2.1 | 16.0 |
| Will Richard | 98% | 23.4<br><sub>19,30,23,27,27</sub> | 8.3<br><sub>9,7,11,20,15</sub> |  | 2.7<br><sub>4,4,3,0,5</sub> |  | 1.4<br><sub>0,1,1,3,0</sub> |  | 1.0<br><sub>2,1,2,1,1</sub> |  | 0.9 | 0.2 | 0.9 | 12.4 |
| De'Anthony Melton | 99% | 23.2<br><sub>25,18,21,19,25</sub> | 10.4<br><sub>11,8,8,0,9</sub> |  | 3.3<br><sub>4,4,2,2,1</sub> |  | 2.7<br><sub>4,3,1,2,5</sub> |  | 1.6<br><sub>3,2,2,0,1</sub> |  | 1.1 | 0.4 | 1.6 | 16.5 |
| Gui Santos | 96% | 19.0<br><sub>12,21,19,17,23</sub> | 8.0<br><sub>0,7,12,6,8</sub> |  | 3.8<br><sub>3,4,7,6,3</sub> |  | 2.1<br><sub>1,1,2,6,0</sub> |  | 0.7<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.3 | 1.2 | 13.8 |
| Charles Bassey | 98% | 17.8<br><sub>13,20,16,22,25</sub> | 8.0<br><sub>7,11,4,10,16</sub> |  | 6.4<br><sub>6,5,0,8,13</sub> |  | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.1 | 15.2 |
| Gary Payton II | 88% | 17.6<br><sub>-,13,8,16,24</sub> | 7.7<br><sub>-,2,2,8,2</sub> |  | 3.0<br><sub>-,2,0,8,1</sub> |  | 1.3<br><sub>-,0,0,2,1</sub> |  | 0.6<br><sub>-,0,0,2,0</sub> |  | 0.9 | 0.2 | 0.7 | 12.0 |
| Georges Niang | 98% | 17.4<br><sub>19,15,14,14,15</sub> | 7.5<br><sub>5,5,0,11,5</sub> |  | 2.5<br><sub>5,3,4,1,2</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.2<br><sub>1,1,0,2,1</sub> |  | 0.3 | 0.1 | 0.8 | 11.2 |
| Al Horford | 98% | 16.9<br><sub>21,10,14,-,17</sub> | 5.6<br><sub>2,0,0,-,3</sub> |  | 3.5<br><sub>1,3,5,-,2</sub> |  | 1.8<br><sub>4,1,0,-,2</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.7 | 0.5 | 10.8 |
| LJ Cryer | 88% | 14.8<br><sub>18,24,24,19,12</sub> | 6.8<br><sub>13,20,7,9,9</sub> |  | 1.1<br><sub>1,2,1,0,0</sub> |  | 1.6<br><sub>1,6,3,2,1</sub> |  | 1.1<br><sub>3,6,1,3,1</sub> |  | 0.3 | 0.1 | 0.7 | 9.4 |
| Graham Ike | 96% | 10.3<br><sub>4,13,8,15,4</sub> | 4.2<br><sub>4,5,3,2,5</sub> |  | 2.3<br><sub>0,2,5,2,0</sub> |  | 1.1<br><sub>1,3,1,2,0</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 7.7 |
| Malevy Leons | 83% | 8.2<br><sub>4,14,6,7,4</sub> | 2.2<br><sub>0,5,2,2,0</sub> |  | 1.5<br><sub>3,1,1,1,2</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-22/`._
