# NBA model · Wed 11 Nov 2026 (US date)

Updated **Thu 12 Nov, 12:33 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-11/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ POR | draftkings | 14.80 | 12.64 | 5.43 | 18.4% | 6.3% | 7.9% | +17.1% | +172.7% | 0.3% |
| Kevin Durant AST over 7.5 (8+) | GSW @ HOU | draftkings | 16.80 | 15.08 | 7.32 | 13.7% | 5.6% | 6.6% | +11.4% | +129.6% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ORL @ UTA | Thu 12 Nov 13:00 | 111.6–110.4 | ORL 53% | 1.89 / 2.13 | UTA +1.5 | 221.5 | UTA +3.5 covers 56%; o216.5 61% |
| GSW @ HOU | Thu 12 Nov 13:30 | 109.7–116.3 | GSW 32% | 3.16 / 1.46 | HOU -6.5 | 225.5 | HOU -6.5 covers 51%; o219.5 63% |
| OKC @ POR | Thu 12 Nov 14:00 | 111.9–110.4 | OKC 54% | 1.86 / 2.16 | POR +1.5 | 222.5 | POR -2.5 covers 40%; o224.5 45% |

### ORL @ UTA
Out: Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Paolo Banchero (ORL), Jamal Cain (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.6–110.4 | ORL 53% | 1.89 / 2.13 | UTA +1.5 | 221.5 | UTA +3.5 covers 56%; o216.5 61% |
| Expected (weighted by chance each plays) | 112.9–110.5 | ORL 57% | 1.77 / 2.30 | UTA +2.5 | 223.5 | UTA +3.5 covers 52%; o216.5 64% |
| if Tristan da Silva plays | 113.4–110.4 | ORL 58% | 1.72 / 2.38 | UTA +3.5 | 223.5 | UTA +3.5 covers 51%; o216.5 65% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tristan da Silva (ORL) | Day-To-Day | 70% | 31.4 | 14.2 | 4.7 | 2.1 | 2.4 | 1.0 | 0.4 | 1.5 | 21.0 | full tables below |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 36.3<br><sub>40,38,38,40,38</sub> | 26.8<br><sub>14,24,15,30,33</sub> | 24.5 · 24.5<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>6,3,8,6,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 7.1<br><sub>12,6,15,11,7</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.4 | 3.5 | 40.1 |
| Desmond Bane | 98% | 35.8<br><sub>40,36,32,-,36</sub> | 23.7<br><sub>19,20,15,-,15</sub> | 19.5 · 19.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>2,3,6,-,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.9<br><sub>1,3,0,-,4</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 3.4<br><sub>5,4,3,-,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.5 | 0.5 | 2.6 | 32.3 |
| Wendell Carter Jr. | 98% | 33.8<br><sub>35,34,34,40,33</sub> | 14.8<br><sub>7,6,27,19,8</sub> | 13.5 · 12.5<br><sub>o 51% · u 49%</sub> | 8.7<br><sub>10,9,13,11,11</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>0,0,2,0,1</sub> |  | 1.0<br><sub>1,0,2,3,0</sub> |  | 1.1 | 1.1 | 1.8 | 25.6 |
| Anthony Black | 98% | 33.7<br><sub>33,-,31,38,33</sub> | 19.0<br><sub>23,-,10,18,26</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>8,-,7,8,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.1<br><sub>3,-,6,6,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,-,1,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.1 | 0.7 | 2.6 | 29.1 |
| Jase Richardson | 96% | 26.8<br><sub>26,29,26,30,15</sub> | 10.4<br><sub>4,9,10,2,6</sub> |  | 3.0<br><sub>1,1,2,4,1</sub> |  | 3.0<br><sub>3,5,3,4,1</sub> |  | 1.0<br><sub>0,0,2,0,0</sub> |  | 1.1 | 0.4 | 1.2 | 16.3 |
| Alex Morales | 80% | 22.4<br><sub>-,14,6,15,29</sub> | 5.0<br><sub>-,3,0,0,7</sub> |  | 3.5<br><sub>-,2,0,2,7</sub> |  | 1.3<br><sub>-,0,0,1,0</sub> |  | 0.4<br><sub>-,0,0,0,1</sub> |  | 0.8 | 0.3 | 1.1 | 9.8 |
| Jevon Carter | 71% | 16.3<br><sub>-,18,3,15,4</sub> | 6.2<br><sub>-,5,0,9,0</sub> |  | 1.5<br><sub>-,1,0,1,0</sub> |  | 1.6<br><sub>-,4,0,0,0</sub> |  | 1.0<br><sub>-,1,0,3,0</sub> |  | 0.8 | 0.2 | 0.6 | 9.3 |
| Nikola Vucevic | 98% | 15.7<br><sub>7,14,4,6,18</sub> | 6.8<br><sub>2,7,0,0,5</sub> |  | 4.4<br><sub>4,6,0,1,4</sub> |  | 1.7<br><sub>2,1,0,2,1</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.4 | 0.5 | 0.6 | 12.9 |
| Goga Bitadze | 84% | 14.8<br><sub>5,-,8,7,15</sub> | 5.4<br><sub>0,-,4,4,2</sub> |  | 4.9<br><sub>1,-,5,5,2</sub> |  | 1.2<br><sub>0,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.0 | 0.7 | 11.6 |
| Colin Castleton | 38% | 8.8<br><sub>-,-,2,-,-</sub> | 3.0<br><sub>-,-,0,-,-</sub> |  | 2.7<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 6.3 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 31.9<br><sub>22,44,32,30,-</sub> | 22.3<br><sub>7,39,16,19,-</sub> | 21.5 · 20.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>7,2,6,5,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>0,9,9,8,-</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>1,2,1,0,-</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 3.3 | 31.6 |
| Ace Bailey | 98% | 31.2<br><sub>24,35,29,32,35</sub> | 15.1<br><sub>5,15,12,7,23</sub> | 14.5 · 15.5<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,5,6,2,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,1,0,3,2</sub> |  | 2.0<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 1.0 | 1.9 | 22.1 |
| Darryn Peterson | 98% | 30.9<br><sub>33,30,30,35,31</sub> | 16.2<br><sub>14,7,21,26,25</sub> | 18.5 · 18.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,2,2,6,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.7<br><sub>6,7,5,4,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>2,0,3,4,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.7 | 2.1 | 23.8 |
| Jaxson Hayes | 98% | 25.2<br><sub>22,21,28,29,17</sub> | 8.8<br><sub>9,2,8,18,6</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>5,7,6,6,2</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.1 | 16.0 |
| Josh Green | 91% | 24.8<br><sub>15,23,24,28,30</sub> | 5.3<br><sub>3,7,3,10,2</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,1,3,0,5</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,0,1,1,4</sub> |  | 0.7<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9 | 0.2 | 0.8 | 9.1 |
| Josh Okogie | 96% | 21.9<br><sub>19,26,24,17,21</sub> | 5.5<br><sub>9,3,12,0,6</sub> | 5.5 · 4.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>3,6,4,1,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>2,1,0,0,4</sub> |  | 0.6<br><sub>1,1,2,0,0</sub> |  | 1.0 | 0.4 | 0.8 | 10.2 |
| Isaiah Collier | 98% | 20.1<br><sub>12,3,13,16,24</sub> | 9.4<br><sub>7,0,4,6,17</sub> |  | 2.6<br><sub>2,1,3,4,5</sub> |  | 5.0<br><sub>2,0,3,2,5</sub> |  | 0.4<br><sub>0,0,0,0,4</sub> |  | 0.8 | 0.3 | 2.0 | 17.1 |
| Brice Sensabaugh | 98% | 18.3<br><sub>14,12,10,13,14</sub> | 11.6<br><sub>7,6,0,2,5</sub> |  | 2.9<br><sub>2,2,2,3,4</sub> |  | 1.5<br><sub>1,0,2,0,4</sub> |  | 1.6<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.2 | 1.5 | 16.1 |
| Svi Mykhailiuk | 96% | 17.2<br><sub>14,17,14,6,21</sub> | 6.6<br><sub>3,6,0,0,7</sub> |  | 1.9<br><sub>2,3,0,0,2</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.7 | 9.8 |
| Kyle Filipowski | 76% | 16.5<br><sub>8,-,1,15,15</sub> | 8.4<br><sub>1,-,0,9,7</sub> |  | 4.9<br><sub>2,-,0,6,4</sub> |  | 1.7<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>0,-,0,1,0</sub> |  | 0.7 | 0.4 | 1.2 | 14.9 |
| Mo Bamba | 71% | 16.4<br><sub>18,15,-,17,17</sub> | 5.4<br><sub>8,7,-,3,7</sub> |  | 5.8<br><sub>8,10,-,3,7</sub> |  | 0.7<br><sub>0,1,-,1,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 1.4 | 0.8 | 11.9 |
| Tony Bradley | 67% | 11.3<br><sub>7,-,1,2,14</sub> | 3.5<br><sub>2,-,0,0,4</sub> |  | 3.3<br><sub>3,-,1,1,5</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.3 |
| Kobe Bufkin | 23% | 9.7<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.2 |
| Harrison Ingram | 8% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.8 |

</details>

<details><summary>if Tristan da Silva plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner (ORL) | 98% | 35.0<br><sub>40,38,38,40,38</sub> | 25.5<br><sub>14,24,15,30,33</sub> | 24.5 · 24.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>6,3,8,6,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 7.0<br><sub>12,6,15,11,7</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.4 | 3.2 | 38.4 |
| Desmond Bane (ORL) | 98% | 34.1<br><sub>40,36,32,-,36</sub> | 21.5<br><sub>19,20,15,-,15</sub> | 19.5 · 19.5<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>2,3,6,-,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.7<br><sub>1,3,0,-,4</sub> | 2.5<br><sub>o 61% · u 39%</sub> | 3.1<br><sub>5,4,3,-,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.5 | 2.4 | 29.7 |
| Wendell Carter Jr. (ORL) | 98% | 32.5<br><sub>35,34,34,40,33</sub> | 13.5<br><sub>7,6,27,19,8</sub> | 13.5 · 12.5<br><sub>o 51% · u 49%</sub> | 8.5<br><sub>10,9,13,11,11</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>0,0,2,0,1</sub> |  | 0.9<br><sub>1,0,2,3,0</sub> |  | 0.9 | 1.1 | 1.7 | 24.0 |
| Anthony Black (ORL) | 98% | 31.4<br><sub>33,-,31,38,33</sub> | 16.4<br><sub>23,-,10,18,26</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>8,-,7,8,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.7<br><sub>3,-,6,6,5</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>1,-,1,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.0 | 0.7 | 2.3 | 25.7 |
| Tristan da Silva (ORL) | 100% | 31.4<br><sub>35,32,30,39,-</sub> | 14.2<br><sub>23,10,18,19,-</sub> | 12.5 · 12.5 | 4.7<br><sub>10,4,2,7,-</sub> | 4.5 | 2.1<br><sub>2,3,1,2,-</sub> |  | 2.4<br><sub>5,2,4,5,-</sub> | 2.5 | 1.0 | 0.4 | 1.5 | 21.0 |
| Jase Richardson (ORL) | 96% | 22.7<br><sub>26,29,26,30,15</sub> | 8.3<br><sub>4,9,10,2,6</sub> |  | 2.5<br><sub>1,1,2,4,1</sub> |  | 2.6<br><sub>3,5,3,4,1</sub> |  | 0.8<br><sub>0,0,2,0,0</sub> |  | 0.9 | 0.3 | 1.0 | 13.4 |
| Alex Morales (ORL) | 80% | 18.0<br><sub>-,14,6,15,29</sub> | 4.3<br><sub>-,3,0,0,7</sub> |  | 2.8<br><sub>-,2,0,2,7</sub> |  | 1.1<br><sub>-,0,0,1,0</sub> |  | 0.3<br><sub>-,0,0,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 8.2 |
| Nikola Vucevic (ORL) | 98% | 13.2<br><sub>7,14,4,6,18</sub> | 5.7<br><sub>2,7,0,0,5</sub> |  | 3.6<br><sub>4,6,0,1,4</sub> |  | 1.4<br><sub>2,1,0,2,1</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.3 | 0.5 | 0.6 | 10.7 |
| Goga Bitadze (ORL) | 84% | 13.1<br><sub>5,-,8,7,15</sub> | 4.9<br><sub>0,-,4,4,2</sub> |  | 4.3<br><sub>1,-,5,5,2</sub> |  | 1.1<br><sub>0,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 1.0 | 0.7 | 10.3 |
| Jevon Carter (ORL) | 71% | 12.8<br><sub>-,18,3,15,4</sub> | 4.9<br><sub>-,5,0,9,0</sub> |  | 1.2<br><sub>-,1,0,1,0</sub> |  | 1.4<br><sub>-,4,0,0,0</sub> |  | 0.7<br><sub>-,1,0,3,0</sub> |  | 0.6 | 0.2 | 0.5 | 7.4 |
| Colin Castleton (ORL) | 38% | 6.4<br><sub>-,-,2,-,-</sub> | 2.4<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Keyonte George (UTA) | 98% | 31.8<br><sub>22,44,32,30,-</sub> | 22.2<br><sub>7,39,16,19,-</sub> | 21.5 · 20.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>7,2,6,5,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>0,9,9,8,-</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>1,2,1,0,-</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 3.4 | 31.4 |
| Ace Bailey (UTA) | 98% | 31.3<br><sub>24,35,29,32,35</sub> | 15.1<br><sub>5,15,12,7,23</sub> | 14.5 · 15.5<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,5,6,2,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,1,0,3,2</sub> |  | 2.0<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 1.0 | 1.9 | 22.2 |
| Darryn Peterson (UTA) | 98% | 31.0<br><sub>33,30,30,35,31</sub> | 16.1<br><sub>14,7,21,26,25</sub> | 18.5 · 18.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,2,2,6,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.7<br><sub>6,7,5,4,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>2,0,3,4,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.7 | 2.1 | 23.7 |
| Jaxson Hayes (UTA) | 98% | 25.1<br><sub>22,21,28,29,17</sub> | 8.7<br><sub>9,2,8,18,6</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>5,7,6,6,2</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.1 | 15.9 |
| Josh Green (UTA) | 91% | 24.7<br><sub>15,23,24,28,30</sub> | 5.3<br><sub>3,7,3,10,2</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,1,3,0,5</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,0,1,1,4</sub> |  | 0.7<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9 | 0.2 | 0.8 | 9.1 |
| Josh Okogie (UTA) | 96% | 21.8<br><sub>19,26,24,17,21</sub> | 5.4<br><sub>9,3,12,0,6</sub> | 5.5 · 4.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>3,6,4,1,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>2,1,0,0,4</sub> |  | 0.6<br><sub>1,1,2,0,0</sub> |  | 1.0 | 0.4 | 0.8 | 10.1 |
| Isaiah Collier (UTA) | 98% | 20.0<br><sub>12,3,13,16,24</sub> | 9.4<br><sub>7,0,4,6,17</sub> |  | 2.6<br><sub>2,1,3,4,5</sub> |  | 5.0<br><sub>2,0,3,2,5</sub> |  | 0.4<br><sub>0,0,0,0,4</sub> |  | 0.8 | 0.3 | 2.0 | 17.0 |
| Brice Sensabaugh (UTA) | 98% | 18.4<br><sub>14,12,10,13,14</sub> | 11.7<br><sub>7,6,0,2,5</sub> |  | 2.9<br><sub>2,2,2,3,4</sub> |  | 1.6<br><sub>1,0,2,0,4</sub> |  | 1.6<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.2 | 1.4 | 16.1 |
| Svi Mykhailiuk (UTA) | 96% | 17.2<br><sub>14,17,14,6,21</sub> | 6.6<br><sub>3,6,0,0,7</sub> |  | 1.9<br><sub>2,3,0,0,2</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.7 | 9.7 |
| Mo Bamba (UTA) | 71% | 16.5<br><sub>18,15,-,17,17</sub> | 5.5<br><sub>8,7,-,3,7</sub> |  | 5.8<br><sub>8,10,-,3,7</sub> |  | 0.7<br><sub>0,1,-,1,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 1.4 | 0.8 | 12.0 |
| Kyle Filipowski (UTA) | 76% | 16.5<br><sub>8,-,1,15,15</sub> | 8.5<br><sub>1,-,0,9,7</sub> |  | 4.9<br><sub>2,-,0,6,4</sub> |  | 1.6<br><sub>0,-,0,1,1</sub> |  | 0.6<br><sub>0,-,0,1,0</sub> |  | 0.7 | 0.4 | 1.2 | 15.0 |
| Tony Bradley (UTA) | 67% | 11.3<br><sub>7,-,1,2,14</sub> | 3.5<br><sub>2,-,0,0,4</sub> |  | 3.3<br><sub>3,-,1,1,5</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 7.4 |
| Kobe Bufkin (UTA) | 23% | 9.7<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.2 |
| Harrison Ingram (UTA) | 8% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>


### GSW @ HOU
Out: Steven Adams (HOU), Clint Capela (HOU), Jimmy Butler III (GSW), Moses Moody (GSW), Gary Payton II (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 93% | 33.9<br><sub>37,33,32,39,26</sub> | 15.8<br><sub>17,20,9,15,25</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>8,3,6,7,2</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>8,2,3,1,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>2,3,2,4,5</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.2 | 1.7 | 24.5 |
| Yaxel Lendeborg | 98% | 33.2<br><sub>34,29,30,37,27</sub> | 19.9<br><sub>37,16,17,23,23</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>4,5,8,8,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>6,5,6,3,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>6,2,1,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.7 | 3.1 | 30.0 |
| Stephen Curry | 98% | 31.9<br><sub>-,33,28,36,21</sub> | 27.1<br><sub>-,34,29,41,25</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>-,6,1,6,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>-,7,4,6,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>-,5,6,5,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.3 | 2.9 | 35.3 |
| Draymond Green | 91% | 27.9<br><sub>-,17,27,34,21</sub> | 6.7<br><sub>-,4,2,2,2</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>-,4,5,6,3</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 5.8<br><sub>-,2,11,13,6</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>-,0,0,0,0</sub> |  | 1.1 | 0.6 | 2.3 | 17.2 |
| De'Anthony Melton | 98% | 22.6<br><sub>28,28,17,17,26</sub> | 9.4<br><sub>21,2,5,4,16</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>6,7,6,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>3,2,2,1,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>6,0,0,1,4</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.4 | 1.5 | 14.8 |
| Georges Niang | 98% | 20.4<br><sub>21,22,22,25,19</sub> | 7.7<br><sub>3,13,13,11,9</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>2,3,3,1,2</sub> |  | 1.2<br><sub>1,1,2,3,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.2 | 1.0 | 11.5 |
| Gui Santos | 88% | 17.8<br><sub>9,-,-,12,21</sub> | 6.4<br><sub>4,-,-,3,3</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,-,-,1,7</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,-,-,0,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 11.2 |
| Al Horford | 98% | 17.1<br><sub>22,-,18,13,15</sub> | 5.2<br><sub>9,-,8,2,5</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>5,-,5,5,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>2,-,1,4,6</sub> |  | 0.7<br><sub>3,-,2,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.5 | 0.8 | 0.6 | 10.2 |
| Will Richard | 98% | 15.9<br><sub>22,28,16,12,-</sub> | 4.2<br><sub>3,6,10,4,-</sub> |  | 1.7<br><sub>0,5,0,2,-</sub> |  | 0.9<br><sub>3,0,2,1,-</sub> |  | 0.5<br><sub>1,2,2,0,-</sub> |  | 0.8 | 0.1 | 0.5 | 6.8 |
| Charles Bassey | 97% | 13.7<br><sub>20,23,14,11,18</sub> | 6.0<br><sub>6,19,8,8,12</sub> |  | 5.3<br><sub>10,8,7,4,10</sub> |  | 0.6<br><sub>2,1,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 11.9 |
| LJ Cryer | 66% | 11.8<br><sub>2,1,1,-,20</sub> | 5.2<br><sub>0,0,0,-,10</sub> |  | 1.0<br><sub>0,0,0,-,0</sub> |  | 0.9<br><sub>0,0,0,-,3</sub> |  | 0.8<br><sub>0,0,0,-,2</sub> |  | 0.3 | 0.1 | 0.6 | 7.1 |
| Graham Ike | 88% | 9.3<br><sub>6,7,1,-,12</sub> | 3.5<br><sub>2,0,0,-,4</sub> |  | 2.2<br><sub>2,0,1,-,5</sub> |  | 0.6<br><sub>0,0,0,-,2</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.3 |
| Malevy Leons | 52% | 7.6<br><sub>-,-,1,-,12</sub> | 2.0<br><sub>-,-,0,-,0</sub> |  | 1.3<br><sub>-,-,0,-,3</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 3.8 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.8<br><sub>33,36,35,39,38</sub> | 16.2<br><sub>30,14,11,15,14</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>9,10,4,9,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>5,0,2,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>6,4,2,1,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.9 | 1.4 | 25.6 |
| Kevin Durant | 98% | 36.3<br><sub>27,33,35,38,36</sub> | 23.1<br><sub>14,12,21,21,23</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>3,3,5,10,12</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>4,3,2,3,8</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>0,0,2,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 3.4 | 34.3 |
| Alperen Sengun | 88% | 35.8<br><sub>33,38,39,32,35</sub> | 20.6<br><sub>16,26,17,15,20</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 9.9<br><sub>9,7,12,6,12</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>9,10,10,5,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 0.7<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 46% · u 54%</sub> | 1.4 | 1.2 | 3.0 | 37.3 |
| Amen Thompson | 98% | 35.5<br><sub>28,25,32,39,35</sub> | 16.0<br><sub>8,14,11,17,8</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>3,3,8,7,9</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>1,3,1,0,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.7 | 0.7 | 2.2 | 27.4 |
| Fred VanVleet | 88% | 32.5<br><sub>-,27,30,31,30</sub> | 13.8<br><sub>-,8,18,16,12</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>-,2,3,3,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.2<br><sub>-,9,3,4,2</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>-,2,4,4,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.4 | 1.7 | 22.2 |
| Tari Eason | 98% | 23.2<br><sub>19,27,24,23,19</sub> | 9.4<br><sub>8,13,9,2,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>3,4,6,7,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>2,3,1,2,2</sub> |  | 1.1<br><sub>2,3,1,0,2</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.3 | 0.7 | 1.1 | 16.3 |
| Marcus Smart | 88% | 20.4<br><sub>36,20,18,20,17</sub> | 7.3<br><sub>24,8,4,5,5</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>5,4,1,2,2</sub> |  | 2.2<br><sub>3,4,1,0,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>7,2,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.3 | 1.3 | 11.7 |
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
| Shai Gilgeous-Alexander | 98% | 34.7<br><sub>39,35,30,29,29</sub> | 32.2<br><sub>43,42,28,30,26</sub> | 33.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>3,4,3,2,8</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 6.9<br><sub>8,8,4,9,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>4,5,3,3,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.4 | 1.0 | 3.4 | 43.2 |
| Jared McCain | 98% | 30.4<br><sub>27,25,29,23,31</sub> | 15.4<br><sub>7,9,21,19,21</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>9,1,5,5,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,0,0,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>0,1,3,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 2.0 | 21.1 |
| Aday Mara | 98% | 26.7<br><sub>20,25,18,27,26</sub> | 11.0<br><sub>10,9,9,18,10</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 8.0<br><sub>9,5,7,8,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,2,0,3,2</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.5 | 1.9 | 1.7 | 20.6 |
| Isaiah Hartenstein | 98% | 26.5<br><sub>28,26,26,18,24</sub> | 9.9<br><sub>5,3,2,2,7</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 9.9<br><sub>14,12,6,14,9</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>4,4,7,6,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.6 | 23.5 |
| Bennett Stirtz | 98% | 25.6<br><sub>12,22,24,29,18</sub> | 9.4<br><sub>9,16,12,11,13</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>2,1,1,5,1</sub> |  | 1.7<br><sub>0,1,2,3,1</sub> |  | 1.4<br><sub>3,4,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.0 | 13.2 |
| Kenrich Williams | 98% | 25.5<br><sub>31,29,19,23,19</sub> | 9.4<br><sub>12,13,4,9,3</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>3,4,6,4,2</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,2,3,2,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>2,3,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.3 | 1.0 | 16.4 |
| Alex Caruso | 98% | 23.8<br><sub>-,20,20,13,19</sub> | 9.1<br><sub>-,7,5,0,5</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>-,4,6,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>-,3,2,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>-,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.5 | 1.1 | 15.4 |
| Micah Peavy | 88% | 23.6<br><sub>16,26,18,23,21</sub> | 6.4<br><sub>8,2,7,7,0</sub> |  | 4.1<br><sub>5,9,4,3,2</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 0.7<br><sub>2,0,1,1,0</sub> |  | 0.9 | 0.3 | 0.6 | 11.3 |
| Josh Dix | 76% | 19.4<br><sub>12,-,15,21,-</sub> | 4.5<br><sub>0,-,5,2,-</sub> |  | 1.9<br><sub>1,-,2,1,-</sub> |  | 0.9<br><sub>0,-,1,2,-</sub> |  | 0.5<br><sub>0,-,1,0,-</sub> |  | 0.6 | 0.3 | 0.6 | 7.3 |
| Nique Clifford | 91% | 18.3<br><sub>-,-,-,-,20</sub> | 6.7<br><sub>-,-,-,-,4</sub> |  | 2.8<br><sub>-,-,-,-,4</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.3 | 1.2 | 11.4 |
| Brooks Barnhizer | 72% | 11.7<br><sub>-,-,5,8,5</sub> | 3.0<br><sub>-,-,0,2,0</sub> |  | 2.5<br><sub>-,-,0,4,1</sub> |  | 0.8<br><sub>-,-,0,3,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 33.7<br><sub>35,35,39,24,34</sub> | 21.4<br><sub>28,21,22,15,24</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>3,7,9,4,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>5,12,11,1,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>2,1,1,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.4 | 3.6 | 35.0 |
| Damian Lillard | 98% | 30.5<br><sub>30,33,37,20,24</sub> | 17.3<br><sub>20,25,22,12,25</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>6,3,0,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>6,5,4,7,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,2,4,2,4</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 2.3 | 25.8 |
| Toumani Camara | 98% | 30.0<br><sub>31,32,30,21,30</sub> | 11.9<br><sub>9,11,18,4,12</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>5,4,6,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,2,1,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,1,4,0,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 1.4 | 17.9 |
| Jrue Holiday | 98% | 28.3<br><sub>31,28,31,20,25</sub> | 12.9<br><sub>17,15,12,11,11</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>8,4,1,0,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>10,0,7,0,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>3,5,3,1,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 1.9 | 21.4 |
| Donovan Clingan | 98% | 26.3<br><sub>32,29,28,22,26</sub> | 10.8<br><sub>17,24,17,6,7</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 10.4<br><sub>18,11,11,5,13</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>3,1,1,0,3</sub> |  | 1.1<br><sub>1,1,3,0,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.5 | 1.4 | 1.4 | 23.1 |
| Scoot Henderson | 98% | 25.8<br><sub>26,22,23,24,23</sub> | 11.5<br><sub>8,9,2,13,11</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>2,2,2,2,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>2,1,0,1,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 2.3 | 16.7 |
| Sidy Cissoko | 98% | 25.6<br><sub>22,21,22,16,33</sub> | 7.5<br><sub>8,7,7,4,17</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,4,2,3,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>0,4,3,1,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>2,1,2,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.4 | 1.1 | 13.1 |
| Robert Williams III | 98% | 17.8<br><sub>15,16,16,-,15</sub> | 6.5<br><sub>2,9,9,-,6</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>6,8,5,-,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,1,2,-,0</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.6 | 1.0 | 0.9 | 14.2 |
| Jayson Kent | 64% | 11.8<br><sub>-,-,-,12,-</sub> | 4.7<br><sub>-,-,-,4,-</sub> |  | 1.7<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.0 |
| Yang Hansen | 80% | 9.9<br><sub>-,2,3,26,5</sub> | 3.9<br><sub>-,0,2,12,0</sub> |  | 2.6<br><sub>-,0,0,10,1</sub> |  | 0.5<br><sub>-,0,0,1,0</sub> |  | 0.3<br><sub>-,0,0,1,0</sub> |  | 0.2 | 0.3 | 0.7 | 6.9 |
| Micah Potter | 67% | 9.6<br><sub>-,2,-,14,5</sub> | 4.0<br><sub>-,4,-,7,0</sub> |  | 2.5<br><sub>-,1,-,3,3</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4<br><sub>-,1,-,1,0</sub> |  | 0.2 | 0.2 | 0.5 | 7.0 |
| Branden Carlson | 64% | 9.5<br><sub>-,3,-,12,8</sub> | 2.8<br><sub>-,2,-,4,2</sub> |  | 2.3<br><sub>-,0,-,2,5</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.5 | 5.6 |
| John Tonje | 52% | 6.8<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-11/`._
