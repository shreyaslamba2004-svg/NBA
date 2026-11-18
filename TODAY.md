# NBA model · Tue 17 Nov 2026 (US date)

Updated **Wed 18 Nov, 01:25 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-17/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

_No long shots clear the edge threshold right now._

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CHA @ LAL | Wed 18 Nov 15:00 | 106.6–112.1 | CHA 35% | 2.86 / 1.54 | LAL -5.5 | 218.5 | LAL -6.5 covers 48%; o222.5 42% |
| UTA @ LAC | Wed 18 Nov 14:30 | 108.1–122.5 | UTA 15% | 6.62 / 1.18 | LAC -14.5 | 230.5 | LAC -5.5 covers 74%; o227.5 57% |

### CHA @ LAL
Out: Walker Kessler (LAL), Austin Reaves (LAL), Grayson Allen (CHA), Kon Knueppel (CHA), Dennis Schroder (CHA), Hannes Steinbach (CHA)

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sion James | 98% | 32.0<br><sub>31,21,33,32,35</sub> | 8.3<br><sub>10,11,11,3,3</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>2,3,4,8,8</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.7<br><sub>1,0,4,6,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,3,3,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.2 | 1.5 | 16.4 |
| Naz Reid | 98% | 30.9<br><sub>36,26,32,34,27</sub> | 18.6<br><sub>28,14,25,16,17</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>9,6,13,8,4</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,2,4,3,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,2,4,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.7 | 2.7 | 28.7 |
| Brandon Miller | 98% | 30.7<br><sub>26,14,-,-,24</sub> | 19.8<br><sub>10,8,-,-,5</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>4,2,-,-,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.3<br><sub>1,1,-,-,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>1,0,-,-,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.5 | 2.7 | 27.5 |
| Moussa Diabate | 98% | 29.7<br><sub>29,-,-,32,26</sub> | 9.1<br><sub>7,-,-,7,12</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 9.5<br><sub>6,-,-,13,12</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>2,-,-,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.1 | 0.8 | 1.7 | 21.1 |
| Coby White | 98% | 22.7<br><sub>18,16,20,20,20</sub> | 15.3<br><sub>4,7,10,21,21</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>5,1,2,3,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>2,1,9,3,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>0,1,0,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.5 | 0.1 | 2.6 | 21.8 |
| Royce O'Neale | 98% | 22.1<br><sub>18,26,23,22,19</sub> | 6.6<br><sub>0,7,10,7,3</sub> |  | 3.6<br><sub>3,4,3,4,3</sub> |  | 1.4<br><sub>2,2,1,0,1</sub> |  | 1.1<br><sub>0,2,2,2,1</sub> |  | 0.9 | 0.3 | 0.9 | 11.6 |
| Ryan Kalkbrenner | 98% | 20.9<br><sub>19,21,35,16,18</sub> | 6.0<br><sub>6,4,8,2,5</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>4,5,15,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,0,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.1 | 12.6 |
| Grant Williams | 76% | 20.3<br><sub>-,-,-,16,20</sub> | 8.0<br><sub>-,-,-,11,11</sub> |  | 3.4<br><sub>-,-,-,2,2</sub> |  | 1.5<br><sub>-,-,-,1,1</sub> |  | 1.1<br><sub>-,-,-,2,3</sub> |  | 0.6 | 0.4 | 1.1 | 12.9 |
| Christian Anderson | 88% | 18.5<br><sub>-,25,16,18,18</sub> | 8.3<br><sub>-,4,9,13,16</sub> |  | 2.2<br><sub>-,3,1,0,3</sub> |  | 2.4<br><sub>-,5,1,2,2</sub> |  | 1.2<br><sub>-,0,3,3,4</sub> |  | 0.6 | 0.2 | 1.6 | 12.9 |
| Tidjane Salaun | 96% | 14.7<br><sub>10,23,18,16,5</sub> | 5.6<br><sub>9,13,14,2,0</sub> |  | 3.2<br><sub>1,4,3,4,2</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.6<br><sub>3,2,3,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.4 |
| Liam McNeeley | 63% | 13.2<br><sub>-,19,16,-,2</sub> | 5.1<br><sub>-,8,8,-,0</sub> |  | 2.2<br><sub>-,2,1,-,0</sub> |  | 1.0<br><sub>-,3,1,-,0</sub> |  | 0.6<br><sub>-,1,2,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 8.4 |
| PJ Hall | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.6 | 6.4 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 37.7<br><sub>38,-,39,32,36</sub> | 39.0<br><sub>53,-,32,32,43</sub> | 36.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>5,-,8,5,3</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>5,-,10,5,9</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 4.8<br><sub>5,-,3,5,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.9 | 0.7 | 4.5 | 54.7 |
| Quentin Grimes | 98% | 33.6<br><sub>20,32,-,-,37</sub> | 11.6<br><sub>2,12,-,-,22</sub> | 13.5 · –<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>0,1,-,-,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>0,4,-,-,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,2,-,-,5</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.4 | 1.6 | 18.3 |
| Jake LaRavia | 98% | 29.9<br><sub>25,29,32,21,32</sub> | 7.7<br><sub>7,5,4,0,12</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>8,1,3,9,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>3,2,3,6,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>2,0,0,0,2</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.8 | 1.2 | 14.5 |
| Matisse Thybulle | 98% | 27.8<br><sub>24,28,23,23,26</sub> | 7.9<br><sub>2,4,6,8,12</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>2,2,0,5,8</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>0,0,1,1,0</sub> |  | 1.4<br><sub>0,0,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 2.6 | 0.9 | 1.0 | 12.4 |
| Sandro Mamukelashvili | 98% | 25.9<br><sub>20,18,32,26,21</sub> | 11.1<br><sub>7,7,23,23,4</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>3,3,8,3,2</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,0,3,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>1,1,5,5,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.5 | 0.9 | 18.2 |
| Collin Sexton | 98% | 25.8<br><sub>11,24,27,13,24</sub> | 14.9<br><sub>0,17,18,10,16</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>0,2,2,1,0</sub> |  | 3.1<br><sub>1,2,6,3,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>0,0,3,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.2 | 1.8 | 20.6 |
| Ziaire Williams | 98% | 25.8<br><sub>20,21,28,20,19</sub> | 9.8<br><sub>8,17,12,9,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,2,2,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,0,2,5,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,4,2,1,0</sub> |  | 1.5 | 0.3 | 0.9 | 14.4 |
| Jarred Vanderbilt | 86% | 14.4<br><sub>-,14,13,9,12</sub> | 3.0<br><sub>-,2,4,4,2</sub> |  | 3.8<br><sub>-,10,2,3,4</sub> |  | 1.0<br><sub>-,3,0,1,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.3 | 0.6 | 7.8 |
| Adou Thiero | 67% | 11.6<br><sub>7,8,7,14,-</sub> | 3.3<br><sub>4,2,2,2,-</sub> |  | 2.8<br><sub>4,2,2,2,-</sub> |  | 0.7<br><sub>2,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.8 |
| Cameron Carr | 80% | 9.5<br><sub>-,-,7,13,-</sub> | 4.2<br><sub>-,-,2,0,-</sub> |  | 1.5<br><sub>-,-,3,2,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.4 |
| Jaden Hardy | 52% | 9.5<br><sub>-,-,-,4,-</sub> | 4.1<br><sub>-,-,-,3,-</sub> |  | 0.9<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,1,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.7 |
| Kevon Looney | 38% | 9.0<br><sub>-,-,-,4,-</sub> | 1.6<br><sub>-,-,-,0,-</sub> |  | 2.7<br><sub>-,-,-,2,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.9 |
| AK Okereke | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Carson Cooper | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 1.3 | 7.6 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Chris Manon | 52% | 7.6<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 3.5 |
| Bronny James | 52% | 7.0<br><sub>-,-,-,4,-</sub> | 2.0<br><sub>-,-,-,4,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 2.8 |

</details>


### UTA @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Jalen Pickett (LAC), Jaxson Hayes (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 34.2<br><sub>30,-,33,38,34</sub> | 22.2<br><sub>19,-,13,27,13</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>5,-,7,4,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 6.2<br><sub>8,-,7,7,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>0,-,2,4,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.2 | 3.5 | 32.5 |
| Darryn Peterson | 98% | 33.6<br><sub>35,31,33,34,34</sub> | 19.2<br><sub>26,25,22,28,17</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>6,4,4,7,5</sub> | 4.5<br><sub>o 46% · u 53%</sub> | 4.3<br><sub>4,4,5,2,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>4,4,2,4,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.6 | 2.2 | 28.1 |
| Ace Bailey | 98% | 32.8<br><sub>32,35,31,35,30</sub> | 15.9<br><sub>7,23,18,21,7</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>2,7,7,3,8</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>3,2,2,1,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>1,3,3,3,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.9 | 1.9 | 23.9 |
| Brice Sensabaugh | 98% | 27.2<br><sub>13,14,23,27,30</sub> | 15.4<br><sub>2,5,19,7,14</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>3,4,3,3,7</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>0,4,1,1,2</sub> |  | 2.1<br><sub>0,1,3,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.3 | 2.3 | 22.0 |
| Mo Bamba | 88% | 26.2<br><sub>17,17,18,20,36</sub> | 9.9<br><sub>3,7,5,9,26</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>3,7,1,9,5</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,0,1,1,4</sub> |  | 0.7<br><sub>0,0,0,0,6</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 0.7 | 1.8 | 1.2 | 19.8 |
| Josh Okogie | 96% | 25.4<br><sub>17,21,15,22,27</sub> | 6.8<br><sub>0,6,7,7,7</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>1,4,3,2,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,4,0,1,0</sub> |  | 0.8<br><sub>0,0,1,2,2</sub> |  | 1.2 | 0.3 | 1.0 | 12.3 |
| Josh Green | 96% | 21.9<br><sub>28,30,26,14,15</sub> | 4.6<br><sub>10,2,3,2,6</sub> | 4.5 · –<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,5,2,0,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,4,1,0,1</sub> |  | 0.6<br><sub>1,0,1,0,2</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.1 | 0.7 | 8.0 |
| Svi Mykhailiuk | 97% | 18.4<br><sub>6,21,20,7,21</sub> | 6.8<br><sub>0,7,3,0,6</sub> |  | 1.9<br><sub>0,2,0,1,2</sub> |  | 1.4<br><sub>0,3,2,0,3</sub> |  | 1.1<br><sub>0,1,1,0,2</sub> |  | 0.5 | 0.1 | 0.7 | 10.2 |
| Isaiah Collier | 76% | 18.2<br><sub>16,24,12,16,-</sub> | 8.6<br><sub>6,17,7,3,-</sub> |  | 2.6<br><sub>4,5,3,2,-</sub> |  | 4.6<br><sub>2,5,2,5,-</sub> |  | 0.4<br><sub>0,4,1,1,-</sub> |  | 0.8 | 0.2 | 1.8 | 15.8 |
| Kyle Filipowski | 58% | 14.0<br><sub>15,15,-,2,-</sub> | 7.0<br><sub>9,7,-,2,-</sub> |  | 4.4<br><sub>6,4,-,0,-</sub> |  | 1.5<br><sub>1,1,-,0,-</sub> |  | 0.5<br><sub>1,0,-,0,-</sub> |  | 0.6 | 0.3 | 1.1 | 12.8 |
| Tony Bradley | 67% | 13.4<br><sub>2,14,-,12,12</sub> | 4.2<br><sub>0,4,-,0,6</sub> |  | 3.9<br><sub>1,5,-,5,2</sub> |  | 0.7<br><sub>0,0,-,1,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 8.8 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 30.8<br><sub>39,32,25,37,35</sub> | 22.4<br><sub>26,24,13,24,27</sub> | 24.5 · –<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>1,0,5,4,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 7.0<br><sub>7,10,6,7,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>4,3,1,3,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.2 | 3.2 | 32.0 |
| Rui Hachimura | 98% | 27.5<br><sub>37,26,23,32,22</sub> | 13.7<br><sub>21,14,13,7,4</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>9,3,5,11,2</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>7,2,1,3,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.9<br><sub>1,2,3,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.3 | 1.3 | 19.7 |
| Derrick Jones Jr. | 98% | 26.7<br><sub>37,29,24,29,26</sub> | 10.9<br><sub>12,8,11,14,13</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>8,4,3,5,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>1,3,0,0,1</sub> |  | 1.3<br><sub>2,0,2,4,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 1.0 | 0.9 | 16.6 |
| Brook Lopez | 98% | 25.3<br><sub>35,26,19,31,29</sub> | 13.4<br><sub>20,20,8,26,7</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>8,7,4,7,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>1,1,1,4,8</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,1,1,3,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 1.4 | 1.1 | 20.9 |
| Kris Dunn | 98% | 23.0<br><sub>35,24,19,20,18</sub> | 7.1<br><sub>5,14,3,2,7</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,5,2,3,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.6<br><sub>3,4,3,6,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>1,2,1,0,0</sub> |  | 1.6 | 0.3 | 1.1 | 13.8 |
| Max Strus | 98% | 22.4<br><sub>23,19,22,23,25</sub> | 9.6<br><sub>9,7,12,3,14</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>5,4,3,2,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>5,2,3,3,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>3,1,2,0,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 0.9 | 16.6 |
| Keaton Wagler | 98% | 22.2<br><sub>16,18,23,18,28</sub> | 12.1<br><sub>11,15,11,14,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,2,0,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.5<br><sub>1,4,4,1,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>3,3,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 1.7 | 18.7 |
| Kobe Sanders | 98% | 21.0<br><sub>18,22,26,15,20</sub> | 9.3<br><sub>4,8,9,5,2</sub> |  | 2.6<br><sub>2,2,3,0,6</sub> |  | 2.3<br><sub>1,4,7,1,4</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 0.9 | 0.2 | 1.2 | 14.3 |
| Isaiah Jackson | 98% | 16.7<br><sub>13,-,16,17,15</sub> | 7.7<br><sub>2,-,4,5,13</sub> |  | 5.2<br><sub>4,-,4,3,2</sub> |  | 1.5<br><sub>2,-,0,3,2</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.8 | 1.1 | 1.1 | 14.3 |
| Gradey Dick | 97% | 16.3<br><sub>7,17,19,19,19</sub> | 8.7<br><sub>4,15,10,13,12</sub> |  | 2.6<br><sub>2,4,3,3,2</sub> |  | 0.9<br><sub>1,0,2,0,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> |  | 0.7 | 0.1 | 0.8 | 12.2 |
| Baba Miller | 80% | 11.9<br><sub>6,20,16,-,5</sub> | 5.9<br><sub>2,12,13,-,2</sub> |  | 1.9<br><sub>1,5,4,-,0</sub> |  | 1.5<br><sub>1,4,0,-,0</sub> |  | 0.3<br><sub>0,0,1,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 9.3 |
| Cam Christie | 48% | 6.3<br><sub>-,2,-,-,-</sub> | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.0 |
| Nick Martinelli | 58% | 6.3<br><sub>-,2,-,-,-</sub> | 3.1<br><sub>-,2,-,-,-</sub> |  | 1.7<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.3 |
| Blake Wesley | 52% | 6.2<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-17/`._
