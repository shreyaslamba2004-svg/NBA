# NBA model · Fri 20 Nov 2026 (US date)

Updated **Sat 21 Nov, 12:16 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-20/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic PA over 59.5 (60+) | SAC @ LAL | draftkings | 9.30 | 8.56 | 4.84 | 20.6% | 10.1% | 11.7% | +8.6% | +92.0% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Mo Bamba REB over 3.5 (4+) | PHX @ UTA | draftkings | 2.97 | 2.46 | 1.10 | 90.8% | 31.5% | 40.6% | +20.6% | +169.8% | 2.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| PHX @ UTA | Sat 21 Nov 13:30 | 120.5–115.1 | PHX 65% | 1.55 / 2.83 | UTA +5.5 | 235.5 | UTA +4.5 covers 47%; o225.5 71% |
| HOU @ DEN | Sat 21 Nov 14:00 | 111.2–115.6 | HOU 38% | 2.67 / 1.60 | DEN -4.5 | 226.5 | DEN -1.5 covers 59%; o227.5 48% |
| SAC @ LAL | Sat 21 Nov 14:00 | 105.7–122.8 | SAC 11% | 8.85 / 1.13 | LAL -17.5 | 228.5 | LAL -14.5 covers 57%; o229.5 48% |

### PHX @ UTA
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Drew Timme (PHX), Mark Williams (PHX)

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 35.2<br><sub>29,35,28,37,33</sub> | 27.3<br><sub>17,30,17,20,29</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,1,4,4,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>5,7,7,8,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,4,0,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.3 | 2.6 | 37.2 |
| Dillon Brooks | 98% | 29.6<br><sub>22,30,22,27,31</sub> | 16.8<br><sub>8,15,1,15,29</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,3,2,4,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,1,0,4,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>0,3,0,3,5</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.4 | 22.7 |
| Miles Bridges | 98% | 28.7<br><sub>18,25,24,29,29</sub> | 14.4<br><sub>8,11,14,16,13</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>4,6,3,8,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>2,3,3,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,0,2,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.6 | 1.1 | 23.6 |
| Jalen Green | 98% | 27.5<br><sub>21,21,21,27,30</sub> | 16.2<br><sub>13,12,9,16,18</sub> | 13.5 · –<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>5,4,2,5,7</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,0,1,3,7</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.8<br><sub>3,1,1,2,4</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.3 | 2.2 | 23.2 |
| Oso Ighodaro | 98% | 23.5<br><sub>20,32,17,33,21</sub> | 6.6<br><sub>6,2,4,8,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>8,3,2,11,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,7,3,3,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.2 | 15.3 |
| Collin Gillespie | 98% | 23.4<br><sub>22,27,28,26,17</sub> | 9.5<br><sub>12,13,26,10,9</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,2,4,3,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.6<br><sub>8,1,4,3,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>4,3,5,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.1 | 1.1 | 16.1 |
| Jordan Goodwin | 98% | 19.8<br><sub>14,24,31,20,17</sub> | 7.7<br><sub>18,6,14,11,2</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>3,5,7,6,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>1,2,6,2,3</sub> |  | 1.2<br><sub>6,2,1,1,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.2 | 0.8 | 14.1 |
| Luke Kennard | 98% | 18.0<br><sub>22,21,23,17,17</sub> | 7.2<br><sub>14,8,18,12,3</sub> |  | 2.1<br><sub>1,1,6,2,3</sub> |  | 1.8<br><sub>3,1,4,0,1</sub> |  | 1.0<br><sub>3,0,3,4,1</sub> |  | 0.5 | 0.1 | 0.6 | 11.1 |
| Khaman Maluach | 98% | 17.4<br><sub>22,16,13,11,21</sub> | 6.3<br><sub>11,4,7,4,10</sub> |  | 5.3<br><sub>7,2,4,6,2</sub> |  | 0.7<br><sub>3,1,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.0 | 1.0 | 12.3 |
| Ryan Dunn | 98% | 15.9<br><sub>25,10,24,12,13</sub> | 4.4<br><sub>10,0,3,5,6</sub> |  | 3.7<br><sub>8,4,6,1,5</sub> |  | 1.1<br><sub>2,0,1,0,2</sub> |  | 0.5<br><sub>1,0,1,1,0</sub> |  | 0.7 | 0.4 | 0.5 | 9.2 |
| Rasheer Fleming | 52% | 8.0<br><sub>12,-,-,-,4</sub> | 3.1<br><sub>4,-,-,-,0</sub> |  | 1.5<br><sub>2,-,-,-,1</sub> |  | 0.3<br><sub>0,-,-,-,1</sub> |  | 0.3<br><sub>1,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Pat Spencer | 52% | 7.2<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.0 |
| Koa Peat | 72% | 7.0<br><sub>6,-,8,1,4</sub> | 3.3<br><sub>5,-,10,0,2</sub> |  | 1.6<br><sub>1,-,2,1,0</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 5.3 |
| Jamaree Bouyea | 52% | 6.8<br><sub>8,-,-,-,4</sub> | 2.9<br><sub>7,-,-,-,0</sub> |  | 0.9<br><sub>1,-,-,-,1</sub> |  | 1.1<br><sub>3,-,-,-,1</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 4.9 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 34.9<br><sub>33,38,34,35,39</sub> | 23.8<br><sub>13,27,13,30,30</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>7,4,4,2,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 7.0<br><sub>7,7,8,11,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,4,1,4,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 3.6 | 34.9 |
| Ace Bailey | 99% | 31.4<br><sub>31,35,30,23,27</sub> | 15.5<br><sub>18,21,7,5,19</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 5.4<br><sub>7,3,8,1,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>2,1,4,4,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>3,3,1,1,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.9 | 1.9 | 23.1 |
| Darryn Peterson | 98% | 30.9<br><sub>33,34,34,31,19</sub> | 17.2<br><sub>22,28,17,13,11</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,7,5,5,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>5,2,4,2,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>2,4,3,2,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.6 | 2.3 | 25.1 |
| Jaxson Hayes | 84% | 24.6<br><sub>30,13,-,-,25</sub> | 9.6<br><sub>11,12,-,-,6</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>8,5,-,-,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>0,1,-,-,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.7 | 1.1 | 1.2 | 17.0 |
| Svi Mykhailiuk | 98% | 23.4<br><sub>20,7,21,33,34</sub> | 8.9<br><sub>3,0,6,8,15</sub> |  | 2.5<br><sub>0,1,2,7,3</sub> |  | 2.0<br><sub>2,0,3,5,5</sub> |  | 1.6<br><sub>1,0,2,2,4</sub> |  | 0.7 | 0.1 | 1.1 | 13.4 |
| Mo Bamba | 91% | 23.2<br><sub>18,20,36,31,23</sub> | 9.2<br><sub>5,9,26,15,6</sub> |  | 8.2<br><sub>1,9,5,10,16</sub> |  | 1.1<br><sub>1,1,4,3,0</sub> |  | 0.6<br><sub>0,0,6,1,0</sub> |  | 0.5 | 1.7 | 1.1 | 18.5 |
| Josh Green | 96% | 22.6<br><sub>26,14,15,13,28</sub> | 5.3<br><sub>3,2,6,9,11</sub> | 5.5 · –<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,0,1,1,2</sub> |  | 1.2<br><sub>1,0,1,0,2</sub> |  | 0.7<br><sub>1,0,2,1,2</sub> |  | 0.8 | 0.2 | 0.8 | 8.7 |
| Brice Sensabaugh | 99% | 21.5<br><sub>23,27,30,35,14</sub> | 13.3<br><sub>19,7,14,40,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>3,3,7,11,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>1,1,2,5,2</sub> |  | 1.8<br><sub>3,1,0,8,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 1.9 | 18.7 |
| Josh Okogie | 98% | 20.2<br><sub>15,22,27,22,15</sub> | 5.7<br><sub>7,7,7,9,3</sub> |  | 3.0<br><sub>3,2,6,2,0</sub> |  | 1.1<br><sub>0,1,0,4,0</sub> |  | 0.6<br><sub>1,2,2,1,0</sub> |  | 0.9 | 0.3 | 0.8 | 9.8 |
| Isaiah Collier | 67% | 15.8<br><sub>12,16,-,-,10</sub> | 7.8<br><sub>7,3,-,-,0</sub> |  | 2.2<br><sub>3,2,-,-,1</sub> |  | 3.9<br><sub>2,5,-,-,2</sub> |  | 0.4<br><sub>1,1,-,-,0</sub> |  | 0.6 | 0.2 | 1.5 | 13.9 |
| Kyle Filipowski | 58% | 11.9<br><sub>-,2,-,-,6</sub> | 6.1<br><sub>-,2,-,-,0</sub> |  | 3.6<br><sub>-,0,-,-,3</sub> |  | 1.2<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.9 | 10.9 |
| Tony Bradley | 63% | 11.0<br><sub>-,12,12,17,-</sub> | 3.7<br><sub>-,0,6,3,-</sub> |  | 3.5<br><sub>-,5,2,7,-</sub> |  | 0.5<br><sub>-,1,0,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.3 | 0.6 | 7.7 |

</details>


### HOU @ DEN
Out: Bryce Hopkins (DEN), Julian Strawther (DEN), Cam Whitmore (DEN), Clint Capela (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.2–115.6 | HOU 38% | 2.67 / 1.60 | DEN -4.5 | 226.5 | DEN -1.5 covers 59%; o227.5 48% |
| Expected (weighted by chance each plays) | 112.2–114.8 | HOU 43% | 2.34 / 1.75 | DEN -3.5 | 226.5 | DEN -1.5 covers 54%; o227.5 49% |
| if Alperen Sengun plays | 112.7–114.5 | HOU 45% | 2.23 / 1.81 | DEN -2.5 | 227.5 | DEN -1.5 covers 52%; o227.5 49% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alperen Sengun (HOU) | Questionable | 55% | 33.7 | 18.7 | 9.4 | 6.3 | 0.7 | 1.1 | 0.8 | 2.5 | 34.4 | full tables below |
| Steven Adams (HOU) | Questionable | 55% | 19.6 | 5.5 | 6.8 | 1.4 | 0.0 | 0.6 | 0.6 | 1.0 | 13.7 | small |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 84% | 36.7<br><sub>29,41,29,-,31</sub> | 17.9<br><sub>19,12,26,-,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>7,10,7,-,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 4.5<br><sub>4,3,7,-,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.4<br><sub>0,0,3,-,0</sub> | 0.5<br><sub>o 28% · u 72%</sub> | 1.5 | 0.7 | 2.1 | 30.1 |
| Kevin Durant | 99% | 36.6<br><sub>34,33,30,29,32</sub> | 24.3<br><sub>20,22,25,22,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>4,3,4,2,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 5.3<br><sub>5,6,5,3,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,2,2,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.8 | 3.0 | 35.5 |
| Jabari Smith Jr. | 99% | 36.0<br><sub>35,24,28,32,26</sub> | 17.4<br><sub>14,6,9,12,17</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>8,3,6,10,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>0,0,5,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>2,1,1,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.8 | 1.2 | 27.0 |
| Fred VanVleet | 84% | 34.0<br><sub>30,34,-,26,27</sub> | 15.0<br><sub>18,17,-,8,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,2,-,5,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 5.6<br><sub>6,3,-,6,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>4,3,-,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.4 | 1.3 | 24.1 |
| Tari Eason | 99% | 29.7<br><sub>22,33,30,27,25</sub> | 13.3<br><sub>6,14,25,7,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>3,11,7,7,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>0,2,1,3,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.6 | 1.4 | 22.2 |
| Reed Sheppard | 91% | 27.0<br><sub>20,19,26,19,25</sub> | 12.2<br><sub>13,0,11,5,20</sub> |  | 2.5<br><sub>1,0,1,2,4</sub> |  | 3.5<br><sub>1,3,6,2,2</sub> |  | 2.2<br><sub>3,0,3,1,6</sub> |  | 1.3 | 0.6 | 1.1 | 18.1 |
| Marcus Smart | 58% | 23.9<br><sub>17,-,-,-,18</sub> | 8.3<br><sub>6,-,-,-,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>2,-,-,-,2</sub> |  | 2.7<br><sub>1,-,-,-,4</sub> |  | 1.2<br><sub>2,-,-,-,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.3 | 1.3 | 13.7 |
| Bogdan Bogdanovic | 98% | 18.2<br><sub>10,12,22,26,11</sub> | 6.9<br><sub>0,11,12,6,1</sub> |  | 2.2<br><sub>0,1,3,0,3</sub> |  | 1.6<br><sub>0,3,4,1,0</sub> |  | 1.0<br><sub>0,3,2,2,0</sub> |  | 0.5 | 0.1 | 0.7 | 10.8 |
| Oscar Tshiebwe | 96% | 14.8<br><sub>1,6,12,6,11</sub> | 5.8<br><sub>0,0,4,6,4</sub> |  | 6.2<br><sub>0,5,9,6,4</sub> |  | 1.1<br><sub>0,0,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 13.2 |
| Isaiah Crawford | 72% | 11.4<br><sub>1,-,9,21,2</sub> | 3.9<br><sub>0,-,4,11,0</sub> |  | 2.4<br><sub>0,-,2,10,0</sub> |  | 0.6<br><sub>0,-,0,3,0</sub> |  | 0.4<br><sub>0,-,0,1,0</sub> |  | 0.3 | 0.2 | 0.4 | 6.8 |
| Jae'Sean Tate | 67% | 10.9<br><sub>1,-,8,12,1</sub> | 3.3<br><sub>0,-,4,3,0</sub> |  | 2.5<br><sub>0,-,2,3,0</sub> |  | 0.7<br><sub>0,-,0,2,1</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.5 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.6<br><sub>39,37,37,38,39</sub> | 26.1<br><sub>25,27,26,28,24</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 11.9<br><sub>16,11,8,15,8</sub> | 10.5<br><sub>o 56% · u 44%</sub> | 9.8<br><sub>9,8,10,7,9</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.9 | 3.5 | 47.7 |
| Jamal Murray | 98% | 37.0<br><sub>39,32,38,35,38</sub> | 25.4<br><sub>38,30,23,28,21</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>2,4,7,4,7</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 6.1<br><sub>2,8,9,4,2</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>5,4,0,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.6 | 2.4 | 36.0 |
| Christian Braun | 98% | 33.6<br><sub>32,37,28,33,35</sub> | 12.7<br><sub>4,12,17,10,15</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>5,5,7,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>3,4,1,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>0,2,1,2,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.4 | 1.1 | 19.3 |
| Aaron Gordon | 98% | 30.5<br><sub>30,27,33,24,31</sub> | 12.8<br><sub>3,9,11,11,13</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>5,3,5,1,8</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.4 | 1.2 | 20.3 |
| Cameron Johnson | 98% | 30.0<br><sub>31,30,31,27,26</sub> | 12.3<br><sub>8,23,12,9,8</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>2,4,5,0,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,3,2,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>2,4,1,0,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.3 | 1.0 | 17.9 |
| DeMar DeRozan | 91% | 22.6<br><sub>19,20,24,14,25</sub> | 11.4<br><sub>7,8,9,2,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>4,1,3,1,2</sub> |  | 2.7<br><sub>2,4,2,1,2</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 0.7 | 0.3 | 1.0 | 16.0 |
| Spencer Jones | 88% | 16.0<br><sub>14,22,12,21,17</sub> | 3.9<br><sub>0,3,4,4,2</sub> |  | 2.1<br><sub>0,1,2,3,2</sub> |  | 0.8<br><sub>1,0,1,3,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 6.8 |
| Trevon Brazile | 98% | 15.4<br><sub>14,13,16,23,11</sub> | 4.3<br><sub>5,7,5,9,0</sub> |  | 3.5<br><sub>2,5,3,4,6</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.3 |
| Marvin Bagley III | 98% | 12.4<br><sub>12,12,13,10,9</sub> | 5.7<br><sub>6,4,7,4,4</sub> |  | 3.5<br><sub>3,2,7,2,3</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 9.8 |
| Tyus Jones | 98% | 9.8<br><sub>6,11,10,10,9</sub> | 2.6<br><sub>2,0,2,0,0</sub> |  | 0.8<br><sub>0,1,0,1,0</sub> |  | 1.6<br><sub>0,4,3,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 5.0 |
| Zeke Nnaji | 23% | 6.8<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.8 |
| Alpha Diallo | 38% | 6.5<br><sub>1,-,-,-,-</sub> | 2.6<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Ryan Nembhard | 52% | 5.8<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.0 |

</details>

<details><summary>if Alperen Sengun plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 98% | 37.6<br><sub>39,37,37,38,39</sub> | 25.9<br><sub>25,27,26,28,24</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 11.9<br><sub>16,11,8,15,8</sub> | 10.5<br><sub>o 56% · u 44%</sub> | 9.8<br><sub>9,8,10,7,9</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 0.9 | 3.5 | 47.5 |
| Jamal Murray (DEN) | 98% | 37.1<br><sub>39,32,38,35,38</sub> | 25.2<br><sub>38,30,23,28,21</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,4,7,4,7</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 6.1<br><sub>2,8,9,4,2</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>5,4,0,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.6 | 2.4 | 35.7 |
| Christian Braun (DEN) | 98% | 33.6<br><sub>32,37,28,33,35</sub> | 12.6<br><sub>4,12,17,10,15</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>5,5,7,3,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>3,4,1,3,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>0,2,1,2,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.4 | 1.1 | 19.2 |
| Aaron Gordon (DEN) | 98% | 30.4<br><sub>30,27,33,24,31</sub> | 12.8<br><sub>3,9,11,11,13</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>5,3,5,1,8</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.4 | 1.2 | 20.3 |
| Cameron Johnson (DEN) | 98% | 30.0<br><sub>31,30,31,27,26</sub> | 12.3<br><sub>8,23,12,9,8</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>2,4,5,0,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,3,2,1,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>2,4,1,0,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.3 | 1.0 | 17.9 |
| DeMar DeRozan (DEN) | 91% | 22.6<br><sub>19,20,24,14,25</sub> | 11.3<br><sub>7,8,9,2,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>4,1,3,1,2</sub> |  | 2.7<br><sub>2,4,2,1,2</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.7 | 0.3 | 1.0 | 15.9 |
| Spencer Jones (DEN) | 88% | 16.1<br><sub>14,22,12,21,17</sub> | 3.9<br><sub>0,3,4,4,2</sub> |  | 2.1<br><sub>0,1,2,3,2</sub> |  | 0.8<br><sub>1,0,1,3,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 6.8 |
| Trevon Brazile (DEN) | 98% | 15.3<br><sub>14,13,16,23,11</sub> | 4.3<br><sub>5,7,5,9,0</sub> |  | 3.5<br><sub>2,5,3,4,6</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 8.3 |
| Marvin Bagley III (DEN) | 98% | 12.5<br><sub>12,12,13,10,9</sub> | 5.7<br><sub>6,4,7,4,4</sub> |  | 3.5<br><sub>3,2,7,2,3</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 9.8 |
| Tyus Jones (DEN) | 98% | 9.7<br><sub>6,11,10,10,9</sub> | 2.5<br><sub>2,0,2,0,0</sub> |  | 0.8<br><sub>0,1,0,1,0</sub> |  | 1.6<br><sub>0,4,3,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 5.0 |
| Zeke Nnaji (DEN) | 23% | 6.7<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.8 |
| Alpha Diallo (DEN) | 38% | 6.5<br><sub>1,-,-,-,-</sub> | 2.6<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Ryan Nembhard (DEN) | 52% | 5.8<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Kevin Durant (HOU) | 99% | 35.9<br><sub>34,33,30,29,32</sub> | 22.1<br><sub>20,22,25,22,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>4,3,4,2,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.5<br><sub>5,6,5,3,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,2,2,2,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.8 | 2.8 | 32.1 |
| Amen Thompson (HOU) | 84% | 35.7<br><sub>29,41,29,-,31</sub> | 16.1<br><sub>19,12,26,-,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>7,10,7,-,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 4.2<br><sub>4,3,7,-,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>0,0,3,-,0</sub> | 0.5<br><sub>o 28% · u 72%</sub> | 1.4 | 0.7 | 1.8 | 27.8 |
| Jabari Smith Jr. (HOU) | 99% | 35.0<br><sub>35,24,28,32,26</sub> | 14.9<br><sub>14,6,9,12,17</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>8,3,6,10,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>0,0,5,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>2,1,1,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.8 | 1.0 | 23.8 |
| Alperen Sengun (HOU) | 100% | 33.7<br><sub>37,37,28,30,14</sub> | 18.7<br><sub>19,43,19,23,7</sub> | 19.5 · – | 9.4<br><sub>13,12,8,7,7</sub> | 9.5 | 6.3<br><sub>9,5,8,2,1</sub> | 6.5 | 0.7<br><sub>1,1,1,1,1</sub> | 0.5 | 1.1 | 0.8 | 2.5 | 34.4 |
| Fred VanVleet (HOU) | 84% | 32.5<br><sub>30,34,-,26,27</sub> | 12.8<br><sub>18,17,-,8,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,2,-,5,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 5.0<br><sub>6,3,-,6,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>4,3,-,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.4 | 1.1 | 21.1 |
| Tari Eason (HOU) | 99% | 26.5<br><sub>22,33,30,27,25</sub> | 10.8<br><sub>6,14,25,7,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>3,11,7,7,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,2,1,3,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 1.1 | 18.4 |
| Reed Sheppard (HOU) | 91% | 22.8<br><sub>20,19,26,19,25</sub> | 9.8<br><sub>13,0,11,5,20</sub> |  | 2.0<br><sub>1,0,1,2,4</sub> |  | 2.6<br><sub>1,3,6,2,2</sub> |  | 1.8<br><sub>3,0,3,1,6</sub> |  | 1.1 | 0.5 | 0.9 | 14.4 |
| Marcus Smart (HOU) | 58% | 20.3<br><sub>17,-,-,-,18</sub> | 6.8<br><sub>6,-,-,-,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,-,-,-,2</sub> |  | 2.1<br><sub>1,-,-,-,4</sub> |  | 0.9<br><sub>2,-,-,-,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.3 | 1.0 | 11.1 |
| Bogdan Bogdanovic (HOU) | 98% | 13.9<br><sub>10,12,22,26,11</sub> | 4.9<br><sub>0,11,12,6,1</sub> |  | 1.6<br><sub>0,1,3,0,3</sub> |  | 1.1<br><sub>0,3,4,1,0</sub> |  | 0.7<br><sub>0,3,2,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.7 |
| Oscar Tshiebwe (HOU) | 96% | 11.4<br><sub>1,6,12,6,11</sub> | 4.4<br><sub>0,0,4,6,4</sub> |  | 4.7<br><sub>0,5,9,6,4</sub> |  | 0.8<br><sub>0,0,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 9.8 |
| Isaiah Crawford (HOU) | 72% | 8.4<br><sub>1,-,9,21,2</sub> | 2.8<br><sub>0,-,4,11,0</sub> |  | 1.8<br><sub>0,-,2,10,0</sub> |  | 0.4<br><sub>0,-,0,3,0</sub> |  | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.9 |
| Jae'Sean Tate (HOU) | 67% | 7.1<br><sub>1,-,8,12,1</sub> | 2.3<br><sub>0,-,4,3,0</sub> |  | 1.6<br><sub>0,-,2,3,0</sub> |  | 0.5<br><sub>0,-,0,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.4 |

</details>


### SAC @ LAL
Out: Austin Reaves (LAL), Precious Achiuwa (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.7–122.8 | SAC 11% | 8.85 / 1.13 | LAL -17.5 | 228.5 | LAL -14.5 covers 57%; o229.5 48% |
| Expected (weighted by chance each plays) | 106.0–122.4 | SAC 13% | 7.98 / 1.14 | LAL -16.5 | 228.5 | LAL -14.5 covers 55%; o229.5 47% |
| if De'Andre Hunter plays | 106.3–121.9 | SAC 14% | 7.37 / 1.16 | LAL -15.5 | 228.5 | LAL -14.5 covers 53%; o229.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Andre Hunter (SAC) | Questionable | 55% | 33.6 | 14.5 | 4.5 | 1.9 | 2.0 | 0.8 | 0.2 | 1.9 | 21.0 | full tables below |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 37.8<br><sub>39,40,35,33,35</sub> | 26.1<br><sub>32,29,17,26,36</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>5,4,4,0,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.4<br><sub>10,6,6,6,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>3,4,3,3,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.4 | 4.7 | 37.0 |
| Zach LaVine | 84% | 33.9<br><sub>25,33,36,-,32</sub> | 20.9<br><sub>15,31,12,-,18</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>4,3,3,-,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.2<br><sub>2,2,6,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>1,6,3,-,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 2.9 | 27.4 |
| Domantas Sabonis | 98% | 33.3<br><sub>-,24,35,29,24</sub> | 15.2<br><sub>-,0,21,11,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 12.0<br><sub>-,2,12,13,13</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>-,5,5,3,8</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 0.4<br><sub>-,0,1,0,0</sub> |  | 0.8 | 0.2 | 2.7 | 32.5 |
| Keegan Murray | 98% | 32.7<br><sub>23,24,40,21,31</sub> | 12.9<br><sub>10,11,16,6,12</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>1,2,7,1,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>2,1,4,0,3</sub> |  | 1.6<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.9 | 1.3 | 19.3 |
| Leaky Black | 88% | 24.8<br><sub>20,18,12,29,17</sub> | 6.1<br><sub>6,0,0,12,3</sub> |  | 3.8<br><sub>5,3,0,9,0</sub> |  | 1.6<br><sub>1,2,0,2,2</sub> |  | 0.9<br><sub>2,0,0,4,1</sub> |  | 1.2 | 0.5 | 0.8 | 11.4 |
| Malik Monk | 98% | 22.3<br><sub>21,3,18,29,20</sub> | 11.7<br><sub>9,1,7,14,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>2,0,4,1,1</sub> |  | 4.2<br><sub>3,0,3,10,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>0,0,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.3 | 2.0 | 17.9 |
| Dylan Cardwell | 98% | 18.7<br><sub>18,29,13,19,12</sub> | 5.7<br><sub>4,1,6,10,6</sub> |  | 6.6<br><sub>9,11,3,6,4</sub> |  | 1.4<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 13.8 |
| Emanuel Sharp | 98% | 18.2<br><sub>12,19,7,21,14</sub> | 5.9<br><sub>5,2,4,9,6</sub> |  | 1.5<br><sub>1,2,0,0,2</sub> |  | 1.0<br><sub>0,0,0,2,1</sub> |  | 0.8<br><sub>1,0,0,1,1</sub> |  | 0.8 | 0.2 | 0.8 | 8.4 |
| Alex Karaban | 58% | 16.4<br><sub>-,-,-,29,4</sub> | 3.4<br><sub>-,-,-,0,0</sub> |  | 2.3<br><sub>-,-,-,5,1</sub> |  | 0.7<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 6.4 |
| Daeqwon Plowden | 88% | 14.8<br><sub>12,2,2,24,4</sub> | 5.7<br><sub>6,0,0,13,3</sub> |  | 1.6<br><sub>0,0,0,2,0</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.9<br><sub>2,0,0,3,1</sub> |  | 0.4 | 0.1 | 0.6 | 8.0 |
| Mason Plumlee | 63% | 9.7<br><sub>-,-,-,5,4</sub> | 2.4<br><sub>-,-,-,2,0</sub> |  | 3.1<br><sub>-,-,-,0,2</sub> |  | 0.8<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.4 | 0.6 | 6.4 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 35.3<br><sub>39,32,36,42,37</sub> | 39.5<br><sub>32,32,43,36,29</sub> | 36.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>8,5,3,6,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 8.1<br><sub>10,5,9,7,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>3,5,5,5,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.6 | 4.1 | 54.3 |
| Quentin Grimes | 98% | 30.4<br><sub>-,-,37,42,35</sub> | 14.2<br><sub>-,-,22,47,20</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>-,-,6,6,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>-,-,1,3,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.0<br><sub>-,-,5,10,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.3 | 1.4 | 20.8 |
| Walker Kessler | 98% | 28.9<br><sub>30,29,32,-,31</sub> | 12.5<br><sub>21,10,14,-,10</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 11.4<br><sub>10,11,12,-,11</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>4,3,3,-,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.1<br><sub>0,0,0,-,0</sub> |  | 1.0 | 2.0 | 1.6 | 25.7 |
| Jake LaRavia | 98% | 25.3<br><sub>32,21,32,23,30</sub> | 7.0<br><sub>4,0,12,4,4</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,9,3,5,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>3,6,3,2,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.7 | 1.2 | 13.1 |
| Matisse Thybulle | 98% | 23.1<br><sub>23,23,26,31,21</sub> | 7.0<br><sub>6,8,12,7,2</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>0,5,8,6,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>1,1,0,0,3</sub> |  | 1.1<br><sub>2,2,2,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.4 | 0.8 | 0.9 | 10.9 |
| Sandro Mamukelashvili | 99% | 21.5<br><sub>32,26,21,23,21</sub> | 9.7<br><sub>23,23,4,3,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>8,3,2,3,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,2,3,2,0</sub> |  | 1.3<br><sub>5,5,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 0.8 | 15.6 |
| Collin Sexton | 99% | 21.3<br><sub>27,13,24,25,20</sub> | 13.8<br><sub>18,10,16,10,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,1,0,4,0</sub> |  | 2.9<br><sub>6,3,3,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 1.6 | 18.8 |
| Ziaire Williams | 98% | 20.1<br><sub>28,20,19,24,18</sub> | 8.4<br><sub>12,9,6,0,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,1,2,1,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>2,5,3,1,0</sub> |  | 1.1<br><sub>2,1,0,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.2 | 0.2 | 0.8 | 11.8 |
| Jarred Vanderbilt | 88% | 13.0<br><sub>13,9,12,14,12</sub> | 2.9<br><sub>4,4,2,4,0</sub> |  | 3.7<br><sub>2,3,4,7,5</sub> |  | 1.2<br><sub>0,1,0,0,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.3 | 0.6 | 7.7 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 47% | 8.7<br><sub>-,4,-,17,-</sub> | 2.0<br><sub>-,0,-,4,-</sub> |  | 3.0<br><sub>-,2,-,8,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.3 | 5.6 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Adou Thiero | 80% | 8.1<br><sub>7,14,-,6,6</sub> | 2.6<br><sub>2,2,-,0,0</sub> |  | 1.9<br><sub>2,2,-,0,1</sub> |  | 0.7<br><sub>1,1,-,1,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |
| Carson Cooper | 58% | 7.9<br><sub>-,-,-,18,2</sub> | 2.4<br><sub>-,-,-,3,2</sub> |  | 2.3<br><sub>-,-,-,4,1</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 5.3 |
| Jaden Hardy | 52% | 6.9<br><sub>-,4,-,-,2</sub> | 3.8<br><sub>-,3,-,-,0</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,1</sub> |  | 0.4<br><sub>-,1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Cameron Carr | 67% | 6.5<br><sub>7,13,-,-,2</sub> | 2.5<br><sub>2,0,-,-,5</sub> |  | 1.0<br><sub>3,2,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,1</sub> |  | 0.2<br><sub>0,0,-,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Bronny James | 52% | 5.7<br><sub>-,4,-,-,2</sub> | 2.0<br><sub>-,4,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 2.6 |
| Chris Manon | 52% | 5.5<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.0 |

</details>

<details><summary>if De'Andre Hunter plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 35.2<br><sub>39,32,36,42,37</sub> | 39.2<br><sub>32,32,43,36,29</sub> | 36.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>8,5,3,6,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 8.1<br><sub>10,5,9,7,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>3,5,5,5,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.5 | 4.1 | 54.0 |
| Quentin Grimes (LAL) | 98% | 30.3<br><sub>-,-,37,42,35</sub> | 14.0<br><sub>-,-,22,47,20</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>-,-,6,6,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>-,-,1,3,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.0<br><sub>-,-,5,10,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.3 | 1.4 | 20.6 |
| Walker Kessler (LAL) | 98% | 29.1<br><sub>30,29,32,-,31</sub> | 12.5<br><sub>21,10,14,-,10</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 11.5<br><sub>10,11,12,-,11</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>4,3,3,-,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.1<br><sub>0,0,0,-,0</sub> |  | 1.0 | 2.0 | 1.6 | 25.8 |
| Jake LaRavia (LAL) | 98% | 25.4<br><sub>32,21,32,23,30</sub> | 7.0<br><sub>4,0,12,4,4</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,9,3,5,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>3,6,3,2,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.7 | 1.2 | 13.2 |
| Matisse Thybulle (LAL) | 98% | 23.1<br><sub>23,23,26,31,21</sub> | 7.0<br><sub>6,8,12,7,2</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>0,5,8,6,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>1,1,0,0,3</sub> |  | 1.1<br><sub>2,2,2,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 2.4 | 0.8 | 1.0 | 10.9 |
| Sandro Mamukelashvili (LAL) | 99% | 21.5<br><sub>32,26,21,23,21</sub> | 9.7<br><sub>23,23,4,3,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>8,3,2,3,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,2,3,2,0</sub> |  | 1.3<br><sub>5,5,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 0.8 | 15.7 |
| Collin Sexton (LAL) | 99% | 21.3<br><sub>27,13,24,25,20</sub> | 13.7<br><sub>18,10,16,10,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,1,0,4,0</sub> |  | 2.9<br><sub>6,3,3,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 1.6 | 18.7 |
| Ziaire Williams (LAL) | 98% | 20.3<br><sub>28,20,19,24,18</sub> | 8.3<br><sub>12,9,6,0,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,1,2,1,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>2,5,3,1,0</sub> |  | 1.1<br><sub>2,1,0,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.2 | 0.2 | 0.8 | 11.8 |
| Jarred Vanderbilt (LAL) | 88% | 13.1<br><sub>13,9,12,14,12</sub> | 2.9<br><sub>4,4,2,4,0</sub> |  | 3.7<br><sub>2,3,4,7,5</sub> |  | 1.2<br><sub>0,1,0,0,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.3 | 0.6 | 7.8 |
| Arthur Kaluma (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney (LAL) | 47% | 8.6<br><sub>-,4,-,17,-</sub> | 1.9<br><sub>-,0,-,4,-</sub> |  | 3.0<br><sub>-,2,-,8,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.3 | 5.6 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Adou Thiero (LAL) | 80% | 8.1<br><sub>7,14,-,6,6</sub> | 2.6<br><sub>2,2,-,0,0</sub> |  | 1.9<br><sub>2,2,-,0,1</sub> |  | 0.7<br><sub>1,1,-,1,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |
| Carson Cooper (LAL) | 58% | 7.8<br><sub>-,-,-,18,2</sub> | 2.3<br><sub>-,-,-,3,2</sub> |  | 2.3<br><sub>-,-,-,4,1</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 5.2 |
| Jaden Hardy (LAL) | 52% | 6.9<br><sub>-,4,-,-,2</sub> | 3.8<br><sub>-,3,-,-,0</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,1</sub> |  | 0.4<br><sub>-,1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Cameron Carr (LAL) | 67% | 6.5<br><sub>7,13,-,-,2</sub> | 2.5<br><sub>2,0,-,-,5</sub> |  | 1.1<br><sub>3,2,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,1</sub> |  | 0.2<br><sub>0,0,-,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Bronny James (LAL) | 52% | 5.6<br><sub>-,4,-,-,2</sub> | 2.0<br><sub>-,4,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 2.5 |
| Chris Manon (LAL) | 52% | 5.6<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.0 |
| Darius Acuff Jr. (SAC) | 98% | 36.4<br><sub>39,40,35,33,35</sub> | 24.1<br><sub>32,29,17,26,36</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>5,4,4,0,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.2<br><sub>10,6,6,6,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,4,3,3,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.3 | 4.3 | 34.8 |
| De'Andre Hunter (SAC) | 100% | 33.6<br><sub>31,34,42,-,35</sub> | 14.5<br><sub>14,15,24,-,7</sub> | 13.5 · – | 4.5<br><sub>3,4,5,-,1</sub> | 3.5 | 1.9<br><sub>1,2,2,-,4</sub> |  | 2.0<br><sub>2,3,2,-,1</sub> | 1.5 | 0.8 | 0.2 | 1.9 | 21.0 |
| Zach LaVine (SAC) | 84% | 32.2<br><sub>25,33,36,-,32</sub> | 18.8<br><sub>15,31,12,-,18</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,3,3,-,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>2,2,6,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>1,6,3,-,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 2.6 | 24.8 |
| Domantas Sabonis (SAC) | 98% | 31.1<br><sub>-,24,35,29,24</sub> | 13.3<br><sub>-,0,21,11,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 11.1<br><sub>-,2,12,13,13</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>-,5,5,3,8</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.8 | 0.2 | 2.5 | 29.3 |
| Keegan Murray (SAC) | 98% | 29.7<br><sub>23,24,40,21,31</sub> | 11.2<br><sub>10,11,16,6,12</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>1,2,7,1,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>2,1,4,0,3</sub> |  | 1.4<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.8 | 1.1 | 17.2 |
| Leaky Black (SAC) | 88% | 20.0<br><sub>20,18,12,29,17</sub> | 4.8<br><sub>6,0,0,12,3</sub> |  | 3.1<br><sub>5,3,0,9,0</sub> |  | 1.2<br><sub>1,2,0,2,2</sub> |  | 0.6<br><sub>2,0,0,4,1</sub> |  | 1.0 | 0.4 | 0.7 | 9.1 |
| Malik Monk (SAC) | 98% | 19.2<br><sub>21,3,18,29,20</sub> | 9.9<br><sub>9,1,7,14,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,0,4,1,1</sub> |  | 3.6<br><sub>3,0,3,10,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>0,0,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.2 | 1.7 | 15.2 |
| Dylan Cardwell (SAC) | 98% | 15.6<br><sub>18,29,13,19,12</sub> | 4.8<br><sub>4,1,6,10,6</sub> |  | 5.5<br><sub>9,11,3,6,4</sub> |  | 1.1<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.8 | 11.3 |
| Emanuel Sharp (SAC) | 98% | 15.6<br><sub>12,19,7,21,14</sub> | 4.8<br><sub>5,2,4,9,6</sub> |  | 1.2<br><sub>1,2,0,0,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.7 | 0.2 | 0.7 | 6.8 |
| Alex Karaban (SAC) | 58% | 11.6<br><sub>-,-,-,29,4</sub> | 2.2<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,5,1</sub> |  | 0.4<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 4.3 |
| Daeqwon Plowden (SAC) | 88% | 11.5<br><sub>12,2,2,24,4</sub> | 4.3<br><sub>6,0,0,13,3</sub> |  | 1.2<br><sub>0,0,0,2,0</sub> |  | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>2,0,0,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Mason Plumlee (SAC) | 63% | 7.1<br><sub>-,-,-,5,4</sub> | 1.9<br><sub>-,-,-,2,0</sub> |  | 2.4<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 4.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-20/`._
