# NBA model · Sun 08 Nov 2026 (US date)

Updated **Mon 09 Nov, 12:53 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-08/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | MIA @ SAC | draftkings | 5.58 | 4.47 | 4.54 | 22.0% | 22.4% | 22.4% | +24.9% | +22.8% | 1.4% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| NOP @ LAC | Mon 09 Nov 13:00 | 116.2–117.3 | NOP 47% | 2.12 / 1.89 | LAC -1.5 | 233.5 | LAC +1.5 covers 56%; o226.5 65% |
| MIA @ SAC | Mon 09 Nov 13:00 | 125.6–114.8 | MIA 78% | 1.28 / 4.54 | SAC +10.5 | 240.5 | SAC +12.5 covers 55%; o235.5 60% |

### NOP @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Isaiah Jackson (LAC), Yves Missi (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray | 100% | 32.5<br><sub>-,-,-,45,35</sub> | 16.5<br><sub>-,-,-,20,7</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>-,-,-,8,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>-,-,-,4,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.8 | 0.3 | 3.2 | 28.3 |
| Trey Murphy III | 100% | 32.4<br><sub>32,29,40,-,34</sub> | 15.3<br><sub>19,15,18,-,10</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>5,5,5,-,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>3,5,5,-,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>2,1,3,-,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 1.5 | 23.4 |
| Zion Williamson | 100% | 31.9<br><sub>31,30,35,38,36</sub> | 18.5<br><sub>22,15,25,23,13</sub> | 19.5 · 19.5<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>6,6,11,4,8</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>2,4,4,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.4 | 0.6 | 2.2 | 27.2 |
| Jeremiah Fears | 100% | 29.9<br><sub>29,31,38,34,36</sub> | 16.1<br><sub>22,20,12,19,24</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>8,5,4,6,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.3<br><sub>13,7,7,2,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 2.7 | 24.8 |
| Saddiq Bey | 98% | 26.4<br><sub>24,26,36,29,31</sub> | 13.4<br><sub>10,25,18,22,17</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>4,6,5,4,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>3,1,1,3,4</sub> |  | 1.6<br><sub>1,1,2,2,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.1 | 1.1 | 19.4 |
| Karlo Matkovic | 100% | 20.0<br><sub>28,18,29,21,18</sub> | 8.1<br><sub>12,8,25,5,18</sub> | 7.5 · 7.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>4,10,6,4,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>1,1,1,2,1</sub> |  | 0.9<br><sub>1,2,5,1,4</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.8 | 1.0 | 13.9 |
| Herbert Jones | 98% | 19.3<br><sub>32,25,28,37,14</sub> | 6.0<br><sub>16,11,9,2,0</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>4,3,4,5,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,2,3,1,0</sub> |  | 0.7<br><sub>0,1,3,0,0</sub> |  | 1.0 | 0.3 | 0.9 | 9.7 |
| Derik Queen | 98% | 18.3<br><sub>22,23,24,27,10</sub> | 8.9<br><sub>9,8,20,20,6</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>2,8,7,9,4</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>3,4,5,6,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.2<br><sub>1,0,1,0,0</sub> |  | 0.8 | 0.6 | 1.8 | 16.7 |
| Trendon Watford | 72% | 13.9<br><sub>17,18,16,20,19</sub> | 5.7<br><sub>8,7,4,7,12</sub> |  | 2.6<br><sub>1,4,4,3,6</sub> |  | 1.4<br><sub>2,0,1,2,1</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.3 | 1.0 | 9.6 |
| Bennedict Mathurin | 98% | 12.8<br><sub>19,19,13,15,7</sub> | 5.7<br><sub>10,7,4,2,2</sub> |  | 2.2<br><sub>3,1,0,5,0</sub> |  | 1.0<br><sub>2,2,0,1,0</sub> |  | 0.4<br><sub>2,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 8.9 |
| Jordan Poole | 52% | 12.4<br><sub>-,-,-,-,-</sub> | 5.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 8.6 |
| DeAndre Jordan | 30% | 8.1<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.8 |
| Bryce McGowens | 52% | 7.2<br><sub>6,15,6,-,-</sub> | 2.4<br><sub>4,3,0,-,-</sub> |  | 0.9<br><sub>1,0,1,-,-</sub> |  | 0.5<br><sub>2,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Julian Reese | 30% | 5.3<br><sub>-,3,-,-,-</sub> | 2.0<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.9 | 3.4 |
| AJ Johnson | 26% | 5.2<br><sub>-,3,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.9 | 0.9 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 100% | 31.7<br><sub>26,31,33,36,39</sub> | 21.9<br><sub>14,24,15,16,26</sub> | 21.5 · 21.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,2,0,4,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>5,5,7,8,7</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>1,4,1,1,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.2 | 3.6 | 31.5 |
| Rui Hachimura | 100% | 30.8<br><sub>-,26,30,-,37</sub> | 16.3<br><sub>-,12,24,-,21</sub> | 16.5 · 16.5<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>-,5,7,-,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>-,0,0,-,7</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>-,2,4,-,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.4 | 1.5 | 22.8 |
| Derrick Jones Jr. | 100% | 29.0<br><sub>28,26,28,-,37</sub> | 11.6<br><sub>15,10,9,-,12</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>5,1,7,-,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,1,1,-,1</sub> |  | 1.3<br><sub>3,2,1,-,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 1.0 | 1.0 | 17.7 |
| Kris Dunn | 100% | 28.3<br><sub>27,31,27,30,35</sub> | 8.3<br><sub>5,5,12,12,5</sub> | 7.5 · 7.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,5,2,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.4<br><sub>3,7,4,1,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 2.0 | 0.3 | 1.5 | 16.4 |
| Brook Lopez | 100% | 26.0<br><sub>22,21,19,22,35</sub> | 13.4<br><sub>2,13,7,12,20</sub> | 12.5 · 12.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>3,6,2,6,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>3,0,0,1,1</sub> |  | 1.6<br><sub>0,1,1,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 1.4 | 1.3 | 20.5 |
| Max Strus | 97% | 22.4<br><sub>-,-,-,23,23</sub> | 10.1<br><sub>-,-,-,11,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>-,-,-,4,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.1<br><sub>-,-,-,6,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>-,-,-,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.2 | 1.3 | 17.1 |
| Kobe Sanders | 98% | 21.3<br><sub>27,24,30,38,18</sub> | 9.6<br><sub>9,7,16,26,4</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>4,4,3,4,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>0,2,0,3,1</sub> |  | 1.3<br><sub>1,1,4,5,0</sub> |  | 0.9 | 0.2 | 1.3 | 14.0 |
| Keaton Wagler | 97% | 20.9<br><sub>28,25,19,24,16</sub> | 10.6<br><sub>21,12,7,6,11</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>4,6,4,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>2,3,4,4,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1<br><sub>3,1,0,0,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.3 | 1.7 | 16.8 |
| Gradey Dick | 96% | 12.0<br><sub>19,12,3,29,7</sub> | 5.4<br><sub>5,3,0,12,4</sub> |  | 1.9<br><sub>5,0,1,4,2</sub> |  | 0.7<br><sub>0,1,0,3,1</sub> |  | 0.5<br><sub>1,1,0,0,0</sub> |  | 0.5 | 0.1 | 0.6 | 7.9 |
| Baba Miller | 91% | 11.1<br><sub>17,5,6,12,6</sub> | 4.9<br><sub>4,0,2,4,2</sub> |  | 1.8<br><sub>7,1,2,0,1</sub> |  | 1.4<br><sub>1,0,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 8.1 |
| Jalen Pickett | 48% | 7.0<br><sub>8,-,6,-,-</sub> | 2.6<br><sub>4,-,0,-,-</sub> |  | 0.9<br><sub>1,-,2,-,-</sub> |  | 1.1<br><sub>1,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Nick Martinelli | 52% | 6.9<br><sub>6,5,6,-,-</sub> | 3.4<br><sub>2,3,10,-,-</sub> |  | 1.8<br><sub>3,0,3,-,-</sub> |  | 0.6<br><sub>1,0,0,-,-</sub> |  | 0.2<br><sub>0,0,2,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.7 |
| Cam Christie | 52% | 6.4<br><sub>14,5,6,-,-</sub> | 2.6<br><sub>2,2,3,-,-</sub> |  | 1.0<br><sub>0,1,1,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.1<br><sub>0,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.1 |
| Blake Wesley | 52% | 6.4<br><sub>-,5,4,-,-</sub> | 2.8<br><sub>-,0,2,-,-</sub> |  | 0.8<br><sub>-,4,0,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |

</details>


### MIA @ SAC
Out: Maxime Raynaud (SAC), Domantas Sabonis (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell PTS under 13.5 | MIA @ SAC | draftkings | 1.99 | 1.93 | 1.71 | 58.5% | 51.3% | 51.8% | +3.2% | +16.5% | 0.8% |
| De'Andre Hunter PTS under 13.5 | MIA @ SAC | tab | 2.00 | 1.99 | 2.16 | 46.3% | 50.5% | 50.2% | +0.4% | -7.4% | 0.1% |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 100% | 34.4<br><sub>34,35,29,43,38</sub> | 13.0<br><sub>10,15,15,11,22</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>1,6,0,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 8.0<br><sub>10,11,7,10,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>0,3,4,0,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.3 | 0.3 | 1.9 | 23.8 |
| Bam Adebayo | 100% | 33.9<br><sub>33,33,31,41,33</sub> | 21.2<br><sub>24,27,16,35,18</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 10.2<br><sub>9,9,9,10,10</sub> | 9.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>3,3,4,4,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.7 | 0.7 | 1.8 | 35.0 |
| Giannis Antetokounmpo | 100% | 33.4<br><sub>31,31,34,41,31</sub> | 29.3<br><sub>24,31,30,27,20</sub> | 30.5 · 29.5<br><sub>o 50% · u 50%</sub> | 12.2<br><sub>18,18,12,14,14</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>3,10,7,6,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>0,1,0,0,1</sub> |  | 1.2 | 0.9 | 3.3 | 47.8 |
| Pelle Larsson | 100% | 31.0<br><sub>31,24,30,35,29</sub> | 11.9<br><sub>17,18,9,7,13</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>6,3,3,3,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 4.0<br><sub>8,3,2,4,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>2,1,1,0,3</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.1 | 0.3 | 1.6 | 19.6 |
| Klay Thompson | 100% | 25.4<br><sub>17,26,27,35,23</sub> | 12.9<br><sub>3,25,19,30,11</sub> | 12.5 · 12.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>1,0,1,5,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>2,3,1,3,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>1,7,4,8,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.5 | 1.1 | 17.1 |
| Andrew Wiggins | 98% | 25.4<br><sub>29,30,24,23,21</sub> | 11.2<br><sub>18,12,7,3,2</sub> | 9.5 · 10.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>2,2,0,4,6</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.8 | 1.1 | 17.0 |
| Bobby Portis | 98% | 17.6<br><sub>23,17,18,18,14</sub> | 7.8<br><sub>11,8,2,4,0</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>9,3,3,10,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>4,1,2,5,0</sub> |  | 1.0<br><sub>1,2,0,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 0.2 | 0.7 | 14.1 |
| Ryan Conwell | 80% | 14.3<br><sub>-,7,8,17,30</sub> | 4.9<br><sub>-,4,5,0,13</sub> |  | 1.3<br><sub>-,0,1,2,1</sub> |  | 1.3<br><sub>-,0,1,2,2</sub> |  | 0.7<br><sub>-,1,1,0,3</sub> |  | 0.6 | 0.1 | 0.5 | 7.6 |
| Tim Hardaway Jr. | 98% | 12.5<br><sub>22,12,19,7,4</sub> | 5.4<br><sub>14,2,9,0,0</sub> |  | 1.3<br><sub>3,1,0,0,0</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.8<br><sub>2,0,3,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.4 |
| Nikola Jovic | 67% | 11.5<br><sub>7,16,7,-,12</sub> | 4.2<br><sub>5,0,2,-,1</sub> |  | 2.0<br><sub>3,4,1,-,0</sub> |  | 1.1<br><sub>0,3,0,-,1</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 7.4 |
| Dru Smith | 67% | 8.0<br><sub>14,4,11,-,1</sub> | 2.6<br><sub>3,0,3,-,0</sub> |  | 1.1<br><sub>0,0,3,-,0</sub> |  | 1.4<br><sub>3,1,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.8 | 0.1 | 0.4 | 5.1 |
| Simone Fontecchio | 52% | 7.4<br><sub>-,2,-,5,-</sub> | 3.8<br><sub>-,3,-,0,-</sub> |  | 1.3<br><sub>-,1,-,0,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.8 |
| Nick Richards | 63% | 6.4<br><sub>-,2,1,-,1</sub> | 2.6<br><sub>-,0,0,-,0</sub> |  | 2.3<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.3 | 0.4 | 5.2 |
| Keshad Johnson | 16% | 6.2 | 2.9 |  | 1.3 |  | 0.3 |  | 0.2 |  | 0.3 | 0.2 | 0.3 | 4.6 |
| Myron Gardner | 58% | 6.1<br><sub>-,2,1,-,1</sub> | 2.5<br><sub>-,0,0,-,0</sub> |  | 1.7<br><sub>-,1,0,-,0</sub> |  | 0.7<br><sub>-,1,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.9 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 100% | 35.9<br><sub>41,37,37,42,33</sub> | 25.0<br><sub>34,38,25,22,22</sub> | 26.5 · 25.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,5,5,3,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 7.7<br><sub>14,5,6,12,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,9,2,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.4 | 3.3 | 36.9 |
| Zach LaVine | 100% | 32.6<br><sub>39,21,28,35,35</sub> | 21.1<br><sub>21,11,23,21,14</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>3,0,4,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.1<br><sub>5,1,1,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>3,0,5,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.2 | 2.5 | 27.7 |
| De'Andre Hunter | 100% | 31.1<br><sub>37,32,36,38,-</sub> | 15.0<br><sub>24,19,6,14,-</sub> | 14.5 · 13.5<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,3,7,2,-</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>1,0,2,2,-</sub> |  | 1.8<br><sub>4,2,0,1,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.7 | 21.9 |
| Precious Achiuwa | 100% | 26.6<br><sub>41,25,27,17,22</sub> | 11.7<br><sub>24,6,6,7,9</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>9,5,10,3,4</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>2,1,3,1,0</sub> |  | 0.4<br><sub>0,0,0,1,1</sub> |  | 1.1 | 0.8 | 1.2 | 20.4 |
| Leaky Black | 64% | 25.8<br><sub>-,-,25,22,40</sub> | 6.2<br><sub>-,-,12,3,12</sub> |  | 4.4<br><sub>-,-,3,6,3</sub> |  | 1.9<br><sub>-,-,1,1,5</sub> |  | 0.9<br><sub>-,-,4,0,4</sub> |  | 1.1 | 0.5 | 0.8 | 12.4 |
| Keegan Murray | 97% | 25.1<br><sub>-,-,-,-,-</sub> | 10.1<br><sub>-,-,-,-,-</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 0.8 | 1.0 | 16.0 |
| Dylan Cardwell | 100% | 22.4<br><sub>-,-,-,13,15</sub> | 6.5<br><sub>-,-,-,4,9</sub> |  | 8.5<br><sub>-,-,-,6,2</sub> |  | 1.6<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.8 | 1.5 | 1.1 | 16.7 |
| Emanuel Sharp | 98% | 20.7<br><sub>18,24,20,10,31</sub> | 6.2<br><sub>0,2,9,3,9</sub> |  | 1.9<br><sub>0,1,3,1,5</sub> |  | 1.1<br><sub>0,1,1,2,0</sub> |  | 0.8<br><sub>0,0,3,1,3</sub> |  | 0.7 | 0.3 | 0.8 | 9.3 |
| Malik Monk | 98% | 20.5<br><sub>8,14,30,24,18</sub> | 11.4<br><sub>2,8,24,13,12</sub> | 9.5 · 10.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,0,1,2,0</sub> |  | 4.0<br><sub>1,3,7,3,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>0,0,5,3,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.4 | 1.6 | 17.5 |
| Jonathan Mogbo | 43% | 12.4<br><sub>-,25,-,-,-</sub> | 3.9<br><sub>-,6,-,-,-</sub> |  | 2.2<br><sub>-,3,-,-,-</sub> |  | 0.8<br><sub>-,3,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.3 | 0.6 | 6.9 |
| Alex Karaban | 58% | 11.4<br><sub>12,10,-,-,11</sub> | 4.0<br><sub>6,0,-,-,0</sub> |  | 1.6<br><sub>0,1,-,-,1</sub> |  | 0.7<br><sub>0,1,-,-,0</sub> |  | 0.3<br><sub>2,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 6.2 |
| Daeqwon Plowden | 64% | 8.8<br><sub>-,4,3,-,-</sub> | 3.3<br><sub>-,4,1,-,-</sub> |  | 1.1<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-08/`._
