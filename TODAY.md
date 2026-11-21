# NBA model · Sat 21 Nov 2026 (US date)

Updated **Sat 21 Nov, 05:41 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-21/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| MIL @ PHI | player points | Anfernee Simons projected 18.6 pts vs DraftKings line 12.5 | minutes 34 vs 23 this season; new team (was BOS last season); scoring 0.55/min vs 0.48 this season, 0.57 last season; teammates out: Bona, Brown, Wade (~76 min a game) |

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
| MIL @ PHI | Sun 22 Nov 05:00 | 108.0–114.7 | MIL 32% | 3.15 / 1.47 | PHI -6.5 | 222.5 | PHI -12.5 covers 34%; o229.5 35% |
| POR @ NYK | Sun 22 Nov 11:30 | 106.7–114.6 | POR 29% | 3.50 / 1.40 | NYK -7.5 | 221.5 | NYK -5.5 covers 57%; o217.5 58% |
| LAC @ DAL | Sun 22 Nov 12:00 | 116.7–117.0 | LAC 49% | 2.03 / 1.97 | DAL +0.5 | 233.5 | DAL -5.5 covers 36%; o229.5 59% |
| MEM @ MIN | Sun 22 Nov 12:00 | 111.4–119.0 | MEM 29% | 3.43 / 1.41 | MIN -7.5 | 230.5 | MIN -5.5 covers 56%; o227.5 56% |
| NOP @ SAS | Sun 22 Nov 12:00 | 108.0–119.0 | NOP 22% | 4.55 / 1.28 | SAS -11.5 | 226.5 | SAS -16.5 covers 35%; o227.5 49% |
| BOS @ SAC | Sun 22 Nov 14:00 | 116.6–104.5 | BOS 80% | 1.25 / 5.05 | SAC +12.5 | 221.5 | SAC +12.5 covers 51%; o217.5 57% |

### MIL @ PHI
Out: Adem Bona (PHI), Jaylen Brown (PHI), Ariel Hukporti (PHI), Dean Wade (PHI), Ousmane Dieng (MIL), Kam Jones (MIL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.0–114.7 | MIL 32% | 3.15 / 1.47 | PHI -6.5 | 222.5 | PHI -12.5 covers 34%; o229.5 35% |
| Expected (weighted by chance each plays) | 108.1–116.2 | MIL 28% | 3.54 / 1.39 | PHI -8.5 | 224.5 | PHI -12.5 covers 38%; o229.5 39% |
| if Tyrese Maxey plays | 108.1–117.4 | MIL 25% | 3.97 / 1.34 | PHI -9.5 | 225.5 | PHI -12.5 covers 41%; o229.5 41% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey (PHI) | Questionable | 55% | 37.6 | 26.4 | 3.9 | 6.5 | 3.1 | 1.5 | 0.6 | 2.4 | 36.8 | full tables below |

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 27.6<br><sub>35,34,20,24,31</sub> | 16.2<br><sub>27,18,5,8,19</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>2,1,5,2,4</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.7<br><sub>7,2,3,4,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>2,2,0,0,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.1 | 23.9 |
| Kyle Kuzma | 98% | 24.8<br><sub>24,31,22,30,-</sub> | 11.5<br><sub>9,14,14,26,-</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>1,4,6,5,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,2,2,1,-</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>1,1,3,2,-</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.6 | 0.4 | 1.6 | 18.1 |
| Jaime Jaquez Jr. | 99% | 23.7<br><sub>30,28,30,23,22</sub> | 12.2<br><sub>25,22,6,10,9</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>5,6,5,2,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>3,4,4,5,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>2,5,2,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.2 | 1.7 | 19.4 |
| Myles Turner | 98% | 23.2<br><sub>-,31,23,21,-</sub> | 8.3<br><sub>-,14,8,4,-</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>-,11,7,5,-</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>-,3,1,4,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>-,4,1,0,-</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.5 | 1.5 | 1.1 | 15.0 |
| Ryan Rollins | 98% | 22.0<br><sub>24,29,-,-,21</sub> | 10.8<br><sub>8,8,-,-,15</sub> |  | 3.7<br><sub>7,10,-,-,3</sub> |  | 3.8<br><sub>4,2,-,-,6</sub> |  | 1.4<br><sub>2,0,-,-,1</sub> |  | 0.9 | 0.3 | 2.1 | 18.2 |
| Brayden Burries | 98% | 21.9<br><sub>23,19,29,25,28</sub> | 9.2<br><sub>8,3,13,20,14</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 4.7<br><sub>5,4,8,7,3</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>1,3,4,1,3</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.9<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 1.4 | 16.1 |
| Nate Ament | 96% | 18.6<br><sub>22,22,17,17,35</sub> | 7.3<br><sub>2,9,5,7,18</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,3,2,4,9</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>1,1,1,1,0</sub> |  | 0.8<br><sub>0,2,1,0,2</sub> |  | 0.5 | 0.3 | 0.9 | 11.1 |
| Kel'el Ware | 98% | 17.5<br><sub>23,17,25,17,26</sub> | 7.7<br><sub>8,10,8,11,11</sub> |  | 5.5<br><sub>5,6,11,3,5</sub> |  | 1.0<br><sub>1,1,2,1,0</sub> |  | 0.7<br><sub>0,2,1,1,2</sub> |  | 0.5 | 0.9 | 1.2 | 14.1 |
| Kasparas Jakucionis | 88% | 17.3<br><sub>4,-,26,26,22</sub> | 8.2<br><sub>4,-,25,20,18</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,-,5,3,3</sub> |  | 2.9<br><sub>0,-,5,5,2</sub> |  | 0.9<br><sub>0,-,4,3,3</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.6 | 0.1 | 1.4 | 13.4 |
| Pete Nance | 96% | 15.9<br><sub>4,-,-,-,28</sub> | 5.0<br><sub>3,-,-,-,7</sub> |  | 2.5<br><sub>1,-,-,-,3</sub> |  | 1.1<br><sub>1,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.3 | 0.5 | 8.6 |
| Cormac Ryan | 52% | 13.9<br><sub>-,-,-,-,-</sub> | 7.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 1.0 | 9.4 |
| Gary Trent Jr. | 80% | 11.7<br><sub>4,16,30,16,7</sub> | 5.2<br><sub>6,1,18,1,0</sub> |  | 0.9<br><sub>1,0,2,1,1</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.8<br><sub>2,0,4,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.7 |
| Jericho Sims | 84% | 11.2<br><sub>18,-,11,18,10</sub> | 2.7<br><sub>0,-,4,4,0</sub> |  | 2.8<br><sub>4,-,2,6,0</sub> |  | 0.9<br><sub>1,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.4 |
| Caris LeVert | 52% | 10.2<br><sub>-,-,-,8,11</sub> | 4.1<br><sub>-,-,-,8,3</sub> |  | 1.4<br><sub>-,-,-,3,3</sub> |  | 1.2<br><sub>-,-,-,2,1</sub> |  | 0.4<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.6 |
| AJ Green | 76% | 9.6<br><sub>8,8,6,14,-</sub> | 3.3<br><sub>3,0,0,11,-</sub> |  | 1.0<br><sub>1,0,0,0,-</sub> |  | 0.6<br><sub>1,2,0,1,-</sub> |  | 0.5<br><sub>1,0,0,3,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| VJ Edgecombe | 97% | 38.4<br><sub>32,36,31,33,43</sub> | 18.4<br><sub>8,15,11,14,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>4,8,4,9,8</sub> |  | 5.3<br><sub>5,8,6,4,6</sub> |  | 2.5<br><sub>0,1,0,1,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.6 | 0.5 | 2.1 | 30.8 |
| LeBron James | 98% | 35.4<br><sub>29,-,33,-,31</sub> | 21.3<br><sub>11,-,15,-,22</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>8,-,7,-,3</sub> |  | 7.9<br><sub>5,-,11,-,6</sub> |  | 1.5<br><sub>1,-,0,-,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.6 | 3.3 | 36.8 |
| Joel Embiid | 98% | 35.0<br><sub>31,28,-,32,36</sub> | 28.6<br><sub>16,20,-,37,26</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 9.7<br><sub>6,4,-,5,6</sub> |  | 5.4<br><sub>1,3,-,1,7</sub> |  | 1.2<br><sub>1,0,-,2,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 1.2 | 3.6 | 43.8 |
| Anfernee Simons | 98% | 33.9<br><sub>18,23,15,26,38</sub> | 18.6<br><sub>17,17,12,9,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>3,3,0,1,2</sub> |  | 2.9<br><sub>0,2,0,2,2</sub> |  | 3.7<br><sub>3,5,1,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 1.4 | 24.9 |
| Kentavious Caldwell-Pope | 99% | 32.1<br><sub>16,27,22,31,32</sub> | 8.6<br><sub>0,11,9,0,8</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>0,4,5,2,8</sub> |  | 2.6<br><sub>2,5,0,3,1</sub> |  | 1.4<br><sub>0,3,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.4 | 1.1 | 15.3 |
| Jabari Walker | 91% | 22.8<br><sub>15,16,25,16,13</sub> | 9.3<br><sub>2,9,11,12,6</sub> |  | 7.0<br><sub>4,8,7,5,5</sub> |  | 1.3<br><sub>0,1,1,1,2</sub> |  | 1.0<br><sub>0,1,3,1,1</sub> |  | 0.6 | 0.3 | 0.9 | 17.6 |
| Labaron Philon Jr. | 67% | 18.7<br><sub>6,2,6,-,17</sub> | 7.3<br><sub>2,0,3,-,10</sub> |  | 2.3<br><sub>1,0,1,-,1</sub> |  | 1.9<br><sub>3,0,0,-,2</sub> |  | 1.0<br><sub>0,0,1,-,2</sub> |  | 0.7 | 0.2 | 0.9 | 11.5 |
| Dominick Barlow | 82% | 16.1 | 4.6 |  | 3.4 |  | 0.9 |  | 0.1 |  | 0.7 | 0.6 | 0.6 | 8.9 |
| Justin Edwards | 58% | 14.7<br><sub>6,1,-,-,13</sub> | 5.5<br><sub>0,0,-,-,2</sub> |  | 2.1<br><sub>0,1,-,-,1</sub> |  | 0.9<br><sub>0,0,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.7 | 0.2 | 0.6 | 8.5 |
| Rayan Rupert | 36% | 13.9<br><sub>6,-,-,-,-</sub> | 4.7<br><sub>0,-,-,-,-</sub> |  | 2.9<br><sub>1,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.9 | 0.2 | 0.8 | 8.6 |
| Tacko Fall | 67% | 12.0<br><sub>-,1,5,-,10</sub> | 9.4<br><sub>-,0,0,-,2</sub> |  | 3.3<br><sub>-,0,3,-,3</sub> |  | 0.6<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.9 | 0.5 | 13.3 |
| Caleb Love | 52% | 11.7<br><sub>-,1,-,-,6</sub> | 3.4<br><sub>-,0,-,-,3</sub> |  | 1.4<br><sub>-,0,-,-,1</sub> |  | 0.9<br><sub>-,0,-,-,1</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.7 | 0.2 | 0.4 | 5.7 |

</details>

<details><summary>if Tyrese Maxey plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 27.6<br><sub>35,34,20,24,31</sub> | 16.2<br><sub>27,18,5,8,19</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>2,1,5,2,4</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.7<br><sub>7,2,3,4,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>2,2,0,0,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.3 | 2.1 | 23.8 |
| Kyle Kuzma (MIL) | 98% | 24.8<br><sub>24,31,22,30,-</sub> | 11.4<br><sub>9,14,14,26,-</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>1,4,6,5,-</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,2,2,1,-</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>1,1,3,2,-</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.6 | 0.4 | 1.6 | 18.1 |
| Jaime Jaquez Jr. (MIL) | 99% | 23.7<br><sub>30,28,30,23,22</sub> | 12.3<br><sub>25,22,6,10,9</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>5,6,5,2,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>3,4,4,5,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>2,5,2,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.2 | 1.7 | 19.5 |
| Myles Turner (MIL) | 98% | 23.2<br><sub>-,31,23,21,-</sub> | 8.3<br><sub>-,14,8,4,-</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>-,11,7,5,-</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>-,3,1,4,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>-,4,1,0,-</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.5 | 1.5 | 1.1 | 14.9 |
| Ryan Rollins (MIL) | 98% | 22.1<br><sub>24,29,-,-,21</sub> | 10.8<br><sub>8,8,-,-,15</sub> |  | 3.7<br><sub>7,10,-,-,3</sub> |  | 3.8<br><sub>4,2,-,-,6</sub> |  | 1.4<br><sub>2,0,-,-,1</sub> |  | 0.9 | 0.3 | 2.1 | 18.3 |
| Brayden Burries (MIL) | 98% | 21.9<br><sub>23,19,29,25,28</sub> | 9.2<br><sub>8,3,13,20,14</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 4.7<br><sub>5,4,8,7,3</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>1,3,4,1,3</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.9<br><sub>1,1,2,3,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 1.4 | 16.0 |
| Nate Ament (MIL) | 96% | 18.7<br><sub>22,22,17,17,35</sub> | 7.4<br><sub>2,9,5,7,18</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,3,2,4,9</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>1,1,1,1,0</sub> |  | 0.8<br><sub>0,2,1,0,2</sub> |  | 0.5 | 0.3 | 1.0 | 11.3 |
| Kel'el Ware (MIL) | 98% | 17.5<br><sub>23,17,25,17,26</sub> | 7.8<br><sub>8,10,8,11,11</sub> |  | 5.4<br><sub>5,6,11,3,5</sub> |  | 1.0<br><sub>1,1,2,1,0</sub> |  | 0.7<br><sub>0,2,1,1,2</sub> |  | 0.5 | 0.9 | 1.2 | 14.1 |
| Kasparas Jakucionis (MIL) | 88% | 17.4<br><sub>4,-,26,26,22</sub> | 8.1<br><sub>4,-,25,20,18</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,-,5,3,3</sub> |  | 2.9<br><sub>0,-,5,5,2</sub> |  | 0.9<br><sub>0,-,4,3,3</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.6 | 0.1 | 1.4 | 13.3 |
| Pete Nance (MIL) | 96% | 15.9<br><sub>4,-,-,-,28</sub> | 5.0<br><sub>3,-,-,-,7</sub> |  | 2.5<br><sub>1,-,-,-,3</sub> |  | 1.1<br><sub>1,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.3 | 0.5 | 8.6 |
| Cormac Ryan (MIL) | 52% | 13.8<br><sub>-,-,-,-,-</sub> | 6.8<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 1.0 | 9.2 |
| Gary Trent Jr. (MIL) | 80% | 11.6<br><sub>4,16,30,16,7</sub> | 5.2<br><sub>6,1,18,1,0</sub> |  | 0.9<br><sub>1,0,2,1,1</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.8<br><sub>2,0,4,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.7 |
| Jericho Sims (MIL) | 84% | 11.3<br><sub>18,-,11,18,10</sub> | 2.8<br><sub>0,-,4,4,0</sub> |  | 2.8<br><sub>4,-,2,6,0</sub> |  | 0.9<br><sub>1,-,0,2,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.4 |
| Caris LeVert (MIL) | 52% | 10.2<br><sub>-,-,-,8,11</sub> | 4.1<br><sub>-,-,-,8,3</sub> |  | 1.3<br><sub>-,-,-,3,3</sub> |  | 1.2<br><sub>-,-,-,2,1</sub> |  | 0.4<br><sub>-,-,-,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.6 |
| AJ Green (MIL) | 76% | 9.7<br><sub>8,8,6,14,-</sub> | 3.3<br><sub>3,0,0,11,-</sub> |  | 1.0<br><sub>1,0,0,0,-</sub> |  | 0.7<br><sub>1,2,0,1,-</sub> |  | 0.5<br><sub>1,0,0,3,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.0 |
| Tyrese Maxey (PHI) | 100% | 37.6<br><sub>34,35,36,35,-</sub> | 26.4<br><sub>24,27,27,24,-</sub> | 24.5 · – | 3.9<br><sub>1,2,4,1,-</sub> |  | 6.5<br><sub>4,8,6,9,-</sub> |  | 3.1<br><sub>3,1,5,4,-</sub> | 2.5 | 1.5 | 0.6 | 2.4 | 36.8 |
| VJ Edgecombe (PHI) | 97% | 36.4<br><sub>32,36,31,33,43</sub> | 15.2<br><sub>8,15,11,14,24</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>4,8,4,9,8</sub> |  | 4.5<br><sub>5,8,6,4,6</sub> |  | 2.1<br><sub>0,1,0,1,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.5 | 0.5 | 1.5 | 26.2 |
| LeBron James (PHI) | 98% | 34.5<br><sub>29,-,33,-,31</sub> | 18.0<br><sub>11,-,15,-,22</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>8,-,7,-,3</sub> |  | 7.2<br><sub>5,-,11,-,6</sub> |  | 1.3<br><sub>1,-,0,-,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.6 | 2.9 | 32.5 |
| Joel Embiid (PHI) | 98% | 33.8<br><sub>31,28,-,32,36</sub> | 25.1<br><sub>16,20,-,37,26</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>6,4,-,5,6</sub> |  | 4.7<br><sub>1,3,-,1,7</sub> |  | 1.1<br><sub>1,0,-,2,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 1.3 | 3.0 | 38.9 |
| Anfernee Simons (PHI) | 98% | 29.8<br><sub>18,23,15,26,38</sub> | 13.8<br><sub>17,17,12,9,18</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>3,3,0,1,2</sub> |  | 2.2<br><sub>0,2,0,2,2</sub> |  | 2.8<br><sub>3,5,1,1,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.2 | 1.0 | 19.0 |
| Kentavious Caldwell-Pope (PHI) | 99% | 28.9<br><sub>16,27,22,31,32</sub> | 7.4<br><sub>0,11,9,0,8</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>0,4,5,2,8</sub> |  | 2.2<br><sub>2,5,0,3,1</sub> |  | 1.2<br><sub>0,3,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.4 | 0.9 | 13.3 |
| Jabari Walker (PHI) | 91% | 18.0<br><sub>15,16,25,16,13</sub> | 7.2<br><sub>2,9,11,12,6</sub> |  | 5.5<br><sub>4,8,7,5,5</sub> |  | 1.0<br><sub>0,1,1,1,2</sub> |  | 0.7<br><sub>0,1,3,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 13.8 |
| Dominick Barlow (PHI) | 82% | 14.5 | 4.1 |  | 3.1 |  | 0.8 |  | 0.1 |  | 0.6 | 0.6 | 0.5 | 8.0 |
| Labaron Philon Jr. (PHI) | 67% | 12.9<br><sub>6,2,6,-,17</sub> | 4.9<br><sub>2,0,3,-,10</sub> |  | 1.7<br><sub>1,0,1,-,1</sub> |  | 1.2<br><sub>3,0,0,-,2</sub> |  | 0.7<br><sub>0,0,1,-,2</sub> |  | 0.5 | 0.1 | 0.7 | 7.8 |
| Justin Edwards (PHI) | 58% | 11.8<br><sub>6,1,-,-,13</sub> | 4.2<br><sub>0,0,-,-,2</sub> |  | 1.7<br><sub>0,1,-,-,1</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 6.6 |
| Tacko Fall (PHI) | 67% | 8.5<br><sub>-,1,5,-,10</sub> | 6.6<br><sub>-,0,0,-,2</sub> |  | 2.4<br><sub>-,0,3,-,3</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.8 | 0.4 | 9.4 |
| Rayan Rupert (PHI) | 36% | 8.5<br><sub>6,-,-,-,-</sub> | 2.6<br><sub>0,-,-,-,-</sub> |  | 1.8<br><sub>1,-,-,-,-</sub> |  | 0.6<br><sub>1,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.5 | 4.9 |
| Caleb Love (PHI) | 52% | 7.2<br><sub>-,1,-,-,6</sub> | 2.1<br><sub>-,0,-,-,3</sub> |  | 0.9<br><sub>-,0,-,-,1</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.2<br><sub>-,0,-,-,1</sub> |  | 0.4 | 0.1 | 0.3 | 3.5 |

</details>


### POR @ NYK
Out: Jordan Clarkson (NYK), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.7–114.6 | POR 29% | 3.50 / 1.40 | NYK -7.5 | 221.5 | NYK -5.5 covers 57%; o217.5 58% |
| Expected (weighted by chance each plays) | 107.8–114.5 | POR 32% | 3.15 / 1.46 | NYK -6.5 | 222.5 | NYK -5.5 covers 54%; o217.5 60% |
| if OG Anunoby plays | 106.3–115.6 | POR 25% | 3.96 / 1.34 | NYK -9.5 | 221.5 | NYK -5.5 covers 61%; o217.5 59% |
| if Deni Avdija plays | 108.8–114.2 | POR 35% | 2.84 / 1.54 | NYK -5.5 | 222.5 | NYK -5.5 covers 50%; o217.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| OG Anunoby (NYK) | Questionable | 55% | 35.0 | 16.6 | 5.5 | 2.0 | 2.1 | 1.8 | 1.0 | 1.8 | 24.1 | full tables below |
| Deni Avdija (POR) | Questionable | 55% | 33.5 | 21.9 | 6.2 | 5.4 | 1.8 | 0.9 | 0.5 | 3.4 | 33.5 | full tables below |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Toumani Camara | 99% | 34.2<br><sub>38,36,26,33,37</sub> | 13.7<br><sub>14,14,3,10,18</sub> |  | 4.5<br><sub>5,2,0,8,6</sub> |  | 1.9<br><sub>3,1,0,1,4</sub> |  | 2.2<br><sub>2,2,0,2,4</sub> |  | 1.0 | 0.6 | 1.5 | 20.0 |
| Damian Lillard | 99% | 33.5<br><sub>32,33,24,31,35</sub> | 21.6<br><sub>18,29,9,25,33</sub> |  | 3.8<br><sub>3,2,2,3,6</sub> |  | 4.6<br><sub>3,6,4,5,0</sub> |  | 3.0<br><sub>2,6,2,5,5</sub> |  | 0.8 | 0.2 | 2.7 | 29.9 |
| Jrue Holiday | 99% | 31.9<br><sub>30,27,25,31,31</sub> | 16.4<br><sub>19,6,10,23,22</sub> |  | 4.2<br><sub>3,5,4,5,2</sub> |  | 5.1<br><sub>5,5,3,6,7</sub> |  | 2.5<br><sub>5,0,2,5,2</sub> |  | 0.9 | 0.2 | 2.5 | 25.7 |
| Sidy Cissoko | 98% | 30.3<br><sub>29,26,28,32,31</sub> | 9.1<br><sub>19,3,5,6,13</sub> |  | 3.9<br><sub>2,4,4,5,5</sub> |  | 2.2<br><sub>0,1,3,1,3</sub> |  | 1.3<br><sub>4,1,1,2,1</sub> |  | 0.9 | 0.4 | 1.2 | 15.2 |
| Scoot Henderson | 99% | 29.3<br><sub>19,23,23,21,35</sub> | 13.8<br><sub>5,11,10,9,27</sub> |  | 2.7<br><sub>2,0,1,1,7</sub> |  | 2.8<br><sub>2,1,0,1,3</sub> |  | 1.8<br><sub>1,2,0,0,5</sub> |  | 0.8 | 0.3 | 2.6 | 19.3 |
| Donovan Clingan | 99% | 28.3<br><sub>30,27,22,32,26</sub> | 11.7<br><sub>5,13,10,12,7</sub> |  | 10.6<br><sub>12,11,10,12,13</sub> |  | 2.1<br><sub>2,2,1,5,2</sub> |  | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.6 | 1.7 | 1.5 | 24.4 |
| Robert Williams III | 98% | 17.4<br><sub>17,17,15,16,-</sub> | 6.0<br><sub>10,2,2,6,-</sub> |  | 6.2<br><sub>7,7,5,8,-</sub> |  | 1.2<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.6 | 1.1 | 0.9 | 13.4 |
| Jayson Kent | 80% | 17.1<br><sub>-,11,11,27,17</sub> | 5.7<br><sub>-,3,8,8,2</sub> |  | 1.9<br><sub>-,1,0,3,1</sub> |  | 0.6<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,1,2,2,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.2 |
| Branden Carlson | 88% | 12.8<br><sub>10,8,14,14,10</sub> | 3.6<br><sub>0,5,5,6,0</sub> |  | 2.7<br><sub>2,3,6,1,1</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 6.8 |
| John Tonje | 52% | 11.5<br><sub>-,-,7,-,6</sub> | 4.0<br><sub>-,-,7,-,0</sub> |  | 2.6<br><sub>-,-,4,-,3</sub> |  | 0.9<br><sub>-,-,3,-,0</sub> |  | 0.5<br><sub>-,-,1,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 7.5 |
| Yang Hansen | 58% | 11.4<br><sub>-,-,7,-,12</sub> | 3.8<br><sub>-,-,0,-,2</sub> |  | 2.5<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,3,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.8 | 7.0 |
| Micah Potter | 52% | 9.3<br><sub>-,-,7,1,-</sub> | 3.8<br><sub>-,-,2,0,-</sub> |  | 2.4<br><sub>-,-,4,0,-</sub> |  | 0.5<br><sub>-,-,1,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 99% | 37.1<br><sub>35,36,41,34,35</sub> | 29.6<br><sub>27,33,28,31,21</sub> |  | 3.2<br><sub>3,1,1,5,2</sub> |  | 6.6<br><sub>5,11,9,5,7</sub> |  | 2.7<br><sub>3,4,3,4,4</sub> |  | 1.1 | 0.2 | 2.8 | 39.3 |
| Karl-Anthony Towns | 99% | 35.6<br><sub>34,34,43,36,33</sub> | 24.7<br><sub>21,23,28,16,22</sub> |  | 13.8<br><sub>11,15,17,16,12</sub> |  | 4.5<br><sub>8,5,3,8,4</sub> |  | 2.0<br><sub>2,3,3,1,2</sub> |  | 1.2 | 0.8 | 3.2 | 43.0 |
| Josh Hart | 98% | 32.5<br><sub>26,23,26,31,28</sub> | 10.0<br><sub>6,0,0,5,11</sub> |  | 7.3<br><sub>4,5,5,4,6</sub> |  | 3.7<br><sub>3,4,2,2,2</sub> |  | 1.3<br><sub>0,0,0,1,3</sub> |  | 1.5 | 0.3 | 1.7 | 21.0 |
| Mikal Bridges | 99% | 32.1<br><sub>17,29,32,30,31</sub> | 12.1<br><sub>2,18,5,17,8</sub> |  | 3.7<br><sub>1,3,7,5,3</sub> |  | 2.7<br><sub>2,3,3,1,3</sub> |  | 1.3<br><sub>0,2,0,2,2</sub> |  | 1.3 | 0.6 | 1.2 | 18.6 |
| Landry Shamet | 99% | 29.9<br><sub>29,21,30,24,30</sub> | 10.9<br><sub>12,5,23,12,10</sub> |  | 2.2<br><sub>2,3,2,1,1</sub> |  | 1.6<br><sub>4,1,0,1,2</sub> |  | 1.8<br><sub>2,1,4,2,2</sub> |  | 0.8 | 0.2 | 1.1 | 14.8 |
| Miles McBride | 99% | 18.7<br><sub>27,22,14,9,8</sub> | 6.7<br><sub>19,9,3,3,3</sub> |  | 1.4<br><sub>2,1,1,0,0</sub> |  | 1.2<br><sub>2,1,0,1,0</sub> |  | 1.1<br><sub>5,3,1,1,0</sub> |  | 0.7 | 0.2 | 0.5 | 9.3 |
| Tyler Kolek | 96% | 16.2<br><sub>13,19,16,13,12</sub> | 5.4<br><sub>4,5,0,4,6</sub> |  | 2.1<br><sub>1,6,0,1,3</sub> |  | 4.0<br><sub>4,2,7,3,5</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 11.4 |
| Andre Drummond | 98% | 14.9<br><sub>14,14,7,11,15</sub> | 4.8<br><sub>0,0,2,2,4</sub> |  | 6.4<br><sub>4,6,3,8,4</sub> |  | 1.0<br><sub>3,0,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.6 | 0.8 | 12.2 |
| Mohamed Diawara | 47% | 14.0<br><sub>11,-,-,-,-</sub> | 4.7<br><sub>2,-,-,-,-</sub> |  | 2.2<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |
| Jose Alvarado | 71% | 14.0<br><sub>-,-,2,7,13</sub> | 5.0<br><sub>-,-,0,2,2</sub> |  | 1.7<br><sub>-,-,0,0,2</sub> |  | 2.1<br><sub>-,-,1,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.8 | 0.1 | 0.8 | 8.8 |
| Dalton Knecht | 64% | 10.1<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 6.3 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Pacome Dadiet | 38% | 8.4<br><sub>-,1,-,-,-</sub> | 3.2<br><sub>-,0,-,-,-</sub> |  | 1.5<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.2 |
| Jaden Akins | 38% | 8.1<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| James Wiseman | 43% | 7.7<br><sub>-,-,3,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,3,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.4 | 0.6 | 5.5 |

</details>

<details><summary>if OG Anunoby plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 99% | 35.6<br><sub>35,36,41,34,35</sub> | 27.2<br><sub>27,33,28,31,21</sub> |  | 3.1<br><sub>3,1,1,5,2</sub> |  | 6.3<br><sub>5,11,9,5,7</sub> |  | 2.6<br><sub>3,4,3,4,4</sub> |  | 1.1 | 0.2 | 2.6 | 36.6 |
| OG Anunoby (NYK) | 100% | 35.0<br><sub>34,33,44,36,36</sub> | 16.6<br><sub>14,11,21,16,15</sub> |  | 5.5<br><sub>6,2,9,4,7</sub> |  | 2.0<br><sub>2,1,1,0,2</sub> |  | 2.1<br><sub>2,2,2,1,1</sub> |  | 1.8 | 1.0 | 1.8 | 24.1 |
| Karl-Anthony Towns (NYK) | 99% | 34.1<br><sub>34,34,43,36,33</sub> | 22.7<br><sub>21,23,28,16,22</sub> |  | 13.0<br><sub>11,15,17,16,12</sub> |  | 4.5<br><sub>8,5,3,8,4</sub> |  | 1.9<br><sub>2,3,3,1,2</sub> |  | 1.2 | 0.8 | 3.0 | 40.2 |
| Josh Hart (NYK) | 98% | 29.5<br><sub>26,23,26,31,28</sub> | 8.9<br><sub>6,0,0,5,11</sub> |  | 6.5<br><sub>4,5,5,4,6</sub> |  | 3.4<br><sub>3,4,2,2,2</sub> |  | 1.1<br><sub>0,0,0,1,3</sub> |  | 1.4 | 0.3 | 1.5 | 18.9 |
| Mikal Bridges (NYK) | 99% | 28.7<br><sub>17,29,32,30,31</sub> | 10.3<br><sub>2,18,5,17,8</sub> |  | 3.3<br><sub>1,3,7,5,3</sub> |  | 2.5<br><sub>2,3,3,1,3</sub> |  | 1.1<br><sub>0,2,0,2,2</sub> |  | 1.2 | 0.5 | 1.1 | 16.1 |
| Landry Shamet (NYK) | 99% | 25.8<br><sub>29,21,30,24,30</sub> | 9.3<br><sub>12,5,23,12,10</sub> |  | 1.9<br><sub>2,3,2,1,1</sub> |  | 1.4<br><sub>4,1,0,1,2</sub> |  | 1.5<br><sub>2,1,4,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 12.7 |
| Miles McBride (NYK) | 99% | 14.7<br><sub>27,22,14,9,8</sub> | 5.3<br><sub>19,9,3,3,3</sub> |  | 1.1<br><sub>2,1,1,0,0</sub> |  | 1.0<br><sub>2,1,0,1,0</sub> |  | 0.8<br><sub>5,3,1,1,0</sub> |  | 0.6 | 0.1 | 0.4 | 7.5 |
| Tyler Kolek (NYK) | 96% | 13.2<br><sub>13,19,16,13,12</sub> | 4.4<br><sub>4,5,0,4,6</sub> |  | 1.7<br><sub>1,6,0,1,3</sub> |  | 3.4<br><sub>4,2,7,3,5</sub> |  | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.5 |
| Andre Drummond (NYK) | 98% | 12.8<br><sub>14,14,7,11,15</sub> | 4.1<br><sub>0,0,2,2,4</sub> |  | 5.6<br><sub>4,6,3,8,4</sub> |  | 0.8<br><sub>3,0,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.7 | 10.6 |
| Jose Alvarado (NYK) | 71% | 10.0<br><sub>-,-,2,7,13</sub> | 3.7<br><sub>-,-,0,2,2</sub> |  | 1.2<br><sub>-,-,0,0,2</sub> |  | 1.6<br><sub>-,-,1,4,1</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.6 | 0.1 | 0.6 | 6.5 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Mohamed Diawara (NYK) | 47% | 8.0<br><sub>11,-,-,-,-</sub> | 2.7<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |
| Dalton Knecht (NYK) | 64% | 6.8<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.4 |
| Jaden Akins (NYK) | 38% | 6.5<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 0.8 |
| James Wiseman (NYK) | 43% | 6.2<br><sub>-,-,3,-,-</sub> | 2.4<br><sub>-,-,0,-,-</sub> |  | 2.0<br><sub>-,-,3,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 4.7 |
| Pacome Dadiet (NYK) | 38% | 5.7<br><sub>-,1,-,-,-</sub> | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Toumani Camara (POR) | 99% | 34.1<br><sub>38,36,26,33,37</sub> | 13.6<br><sub>14,14,3,10,18</sub> |  | 4.5<br><sub>5,2,0,8,6</sub> |  | 1.9<br><sub>3,1,0,1,4</sub> |  | 2.2<br><sub>2,2,0,2,4</sub> |  | 1.0 | 0.6 | 1.4 | 20.0 |
| Damian Lillard (POR) | 99% | 33.5<br><sub>32,33,24,31,35</sub> | 21.5<br><sub>18,29,9,25,33</sub> |  | 3.8<br><sub>3,2,2,3,6</sub> |  | 4.6<br><sub>3,6,4,5,0</sub> |  | 3.0<br><sub>2,6,2,5,5</sub> |  | 0.8 | 0.2 | 2.7 | 29.9 |
| Jrue Holiday (POR) | 99% | 31.9<br><sub>30,27,25,31,31</sub> | 16.2<br><sub>19,6,10,23,22</sub> |  | 4.2<br><sub>3,5,4,5,2</sub> |  | 5.1<br><sub>5,5,3,6,7</sub> |  | 2.5<br><sub>5,0,2,5,2</sub> |  | 0.9 | 0.2 | 2.5 | 25.5 |
| Sidy Cissoko (POR) | 98% | 30.3<br><sub>29,26,28,32,31</sub> | 9.1<br><sub>19,3,5,6,13</sub> |  | 3.9<br><sub>2,4,4,5,5</sub> |  | 2.2<br><sub>0,1,3,1,3</sub> |  | 1.3<br><sub>4,1,1,2,1</sub> |  | 0.9 | 0.4 | 1.2 | 15.2 |
| Scoot Henderson (POR) | 99% | 29.4<br><sub>19,23,23,21,35</sub> | 13.7<br><sub>5,11,10,9,27</sub> |  | 2.7<br><sub>2,0,1,1,7</sub> |  | 2.8<br><sub>2,1,0,1,3</sub> |  | 1.8<br><sub>1,2,0,0,5</sub> |  | 0.8 | 0.3 | 2.6 | 19.2 |
| Donovan Clingan (POR) | 99% | 28.2<br><sub>30,27,22,32,26</sub> | 11.7<br><sub>5,13,10,12,7</sub> |  | 10.6<br><sub>12,11,10,12,13</sub> |  | 2.1<br><sub>2,2,1,5,2</sub> |  | 1.0<br><sub>1,1,0,0,0</sub> |  | 0.6 | 1.7 | 1.5 | 24.4 |
| Robert Williams III (POR) | 98% | 17.4<br><sub>17,17,15,16,-</sub> | 6.0<br><sub>10,2,2,6,-</sub> |  | 6.1<br><sub>7,7,5,8,-</sub> |  | 1.2<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 1.1 | 0.9 | 13.4 |
| Jayson Kent (POR) | 80% | 17.1<br><sub>-,11,11,27,17</sub> | 5.8<br><sub>-,3,8,8,2</sub> |  | 1.9<br><sub>-,1,0,3,1</sub> |  | 0.7<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,1,2,2,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.3 |
| Branden Carlson (POR) | 88% | 12.6<br><sub>10,8,14,14,10</sub> | 3.6<br><sub>0,5,5,6,0</sub> |  | 2.7<br><sub>2,3,6,1,1</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 6.7 |
| Yang Hansen (POR) | 58% | 11.4<br><sub>-,-,7,-,12</sub> | 3.8<br><sub>-,-,0,-,2</sub> |  | 2.5<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,3,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.8 | 7.1 |
| John Tonje (POR) | 52% | 11.4<br><sub>-,-,7,-,6</sub> | 4.0<br><sub>-,-,7,-,0</sub> |  | 2.6<br><sub>-,-,4,-,3</sub> |  | 0.9<br><sub>-,-,3,-,0</sub> |  | 0.5<br><sub>-,-,1,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 7.5 |
| Micah Potter (POR) | 52% | 9.3<br><sub>-,-,7,1,-</sub> | 3.8<br><sub>-,-,2,0,-</sub> |  | 2.4<br><sub>-,-,4,0,-</sub> |  | 0.5<br><sub>-,-,1,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>if Deni Avdija plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 99% | 37.2<br><sub>35,36,41,34,35</sub> | 29.5<br><sub>27,33,28,31,21</sub> |  | 3.2<br><sub>3,1,1,5,2</sub> |  | 6.5<br><sub>5,11,9,5,7</sub> |  | 2.8<br><sub>3,4,3,4,4</sub> |  | 1.1 | 0.2 | 2.8 | 39.2 |
| Karl-Anthony Towns (NYK) | 99% | 35.7<br><sub>34,34,43,36,33</sub> | 24.7<br><sub>21,23,28,16,22</sub> |  | 13.7<br><sub>11,15,17,16,12</sub> |  | 4.6<br><sub>8,5,3,8,4</sub> |  | 2.1<br><sub>2,3,3,1,2</sub> |  | 1.2 | 0.8 | 3.2 | 43.0 |
| Josh Hart (NYK) | 98% | 32.5<br><sub>26,23,26,31,28</sub> | 9.9<br><sub>6,0,0,5,11</sub> |  | 7.3<br><sub>4,5,5,4,6</sub> |  | 3.7<br><sub>3,4,2,2,2</sub> |  | 1.3<br><sub>0,0,0,1,3</sub> |  | 1.5 | 0.3 | 1.7 | 20.9 |
| Mikal Bridges (NYK) | 99% | 32.1<br><sub>17,29,32,30,31</sub> | 12.1<br><sub>2,18,5,17,8</sub> |  | 3.7<br><sub>1,3,7,5,3</sub> |  | 2.8<br><sub>2,3,3,1,3</sub> |  | 1.3<br><sub>0,2,0,2,2</sub> |  | 1.3 | 0.6 | 1.2 | 18.5 |
| Landry Shamet (NYK) | 99% | 29.9<br><sub>29,21,30,24,30</sub> | 10.9<br><sub>12,5,23,12,10</sub> |  | 2.2<br><sub>2,3,2,1,1</sub> |  | 1.6<br><sub>4,1,0,1,2</sub> |  | 1.8<br><sub>2,1,4,2,2</sub> |  | 0.8 | 0.2 | 1.0 | 14.7 |
| Miles McBride (NYK) | 99% | 18.7<br><sub>27,22,14,9,8</sub> | 6.7<br><sub>19,9,3,3,3</sub> |  | 1.4<br><sub>2,1,1,0,0</sub> |  | 1.2<br><sub>2,1,0,1,0</sub> |  | 1.1<br><sub>5,3,1,1,0</sub> |  | 0.7 | 0.2 | 0.5 | 9.3 |
| Tyler Kolek (NYK) | 96% | 16.2<br><sub>13,19,16,13,12</sub> | 5.4<br><sub>4,5,0,4,6</sub> |  | 2.1<br><sub>1,6,0,1,3</sub> |  | 4.0<br><sub>4,2,7,3,5</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 11.4 |
| Andre Drummond (NYK) | 98% | 15.0<br><sub>14,14,7,11,15</sub> | 4.8<br><sub>0,0,2,2,4</sub> |  | 6.5<br><sub>4,6,3,8,4</sub> |  | 1.0<br><sub>3,0,0,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.6 | 0.8 | 12.3 |
| Jose Alvarado (NYK) | 71% | 14.0<br><sub>-,-,2,7,13</sub> | 5.0<br><sub>-,-,0,2,2</sub> |  | 1.7<br><sub>-,-,0,0,2</sub> |  | 2.0<br><sub>-,-,1,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.8 | 0.1 | 0.8 | 8.8 |
| Mohamed Diawara (NYK) | 47% | 13.9<br><sub>11,-,-,-,-</sub> | 4.7<br><sub>2,-,-,-,-</sub> |  | 2.2<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |
| Dalton Knecht (NYK) | 64% | 10.2<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 6.4 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Pacome Dadiet (NYK) | 38% | 8.5<br><sub>-,1,-,-,-</sub> | 3.2<br><sub>-,0,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.2 |
| Jaden Akins (NYK) | 38% | 8.1<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| James Wiseman (NYK) | 43% | 7.7<br><sub>-,-,3,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.5<br><sub>-,-,3,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.4 | 0.6 | 5.4 |
| Deni Avdija (POR) | 100% | 33.5<br><sub>35,35,30,-,-</sub> | 21.9<br><sub>28,34,27,-,-</sub> |  | 6.2<br><sub>3,6,8,-,-</sub> |  | 5.4<br><sub>6,4,4,-,-</sub> |  | 1.8<br><sub>4,3,3,-,-</sub> |  | 0.9 | 0.5 | 3.4 | 33.5 |
| Toumani Camara (POR) | 99% | 31.7<br><sub>38,36,26,33,37</sub> | 11.5<br><sub>14,14,3,10,18</sub> |  | 4.2<br><sub>5,2,0,8,6</sub> |  | 1.6<br><sub>3,1,0,1,4</sub> |  | 1.9<br><sub>2,2,0,2,4</sub> |  | 0.9 | 0.5 | 1.2 | 17.3 |
| Damian Lillard (POR) | 99% | 31.3<br><sub>32,33,24,31,35</sub> | 18.4<br><sub>18,29,9,25,33</sub> |  | 3.5<br><sub>3,2,2,3,6</sub> |  | 4.0<br><sub>3,6,4,5,0</sub> |  | 2.6<br><sub>2,6,2,5,5</sub> |  | 0.8 | 0.2 | 2.2 | 25.9 |
| Jrue Holiday (POR) | 99% | 28.3<br><sub>30,27,25,31,31</sub> | 13.3<br><sub>19,6,10,23,22</sub> |  | 3.6<br><sub>3,5,4,5,2</sub> |  | 4.2<br><sub>5,5,3,6,7</sub> |  | 2.0<br><sub>5,0,2,5,2</sub> |  | 0.8 | 0.2 | 2.0 | 21.1 |
| Donovan Clingan (POR) | 99% | 26.2<br><sub>30,27,22,32,26</sub> | 10.2<br><sub>5,13,10,12,7</sub> |  | 9.6<br><sub>12,11,10,12,13</sub> |  | 1.8<br><sub>2,2,1,5,2</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.5 | 1.6 | 1.2 | 21.7 |
| Sidy Cissoko (POR) | 98% | 25.4<br><sub>29,26,28,32,31</sub> | 6.9<br><sub>19,3,5,6,13</sub> |  | 3.2<br><sub>2,4,4,5,5</sub> |  | 1.7<br><sub>0,1,3,1,3</sub> |  | 0.9<br><sub>4,1,1,2,1</sub> |  | 0.7 | 0.4 | 1.0 | 11.8 |
| Scoot Henderson (POR) | 99% | 25.1<br><sub>19,23,23,21,35</sub> | 11.4<br><sub>5,11,10,9,27</sub> |  | 2.3<br><sub>2,0,1,1,7</sub> |  | 2.1<br><sub>2,1,0,1,3</sub> |  | 1.4<br><sub>1,2,0,0,5</sub> |  | 0.7 | 0.2 | 2.1 | 15.8 |
| Robert Williams III (POR) | 98% | 14.5<br><sub>17,17,15,16,-</sub> | 4.8<br><sub>10,2,2,6,-</sub> |  | 5.0<br><sub>7,7,5,8,-</sub> |  | 0.9<br><sub>0,1,2,4,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.9 | 0.7 | 10.8 |
| Jayson Kent (POR) | 80% | 14.3<br><sub>-,11,11,27,17</sub> | 4.7<br><sub>-,3,8,8,2</sub> |  | 1.5<br><sub>-,1,0,3,1</sub> |  | 0.5<br><sub>-,0,0,0,2</sub> |  | 0.5<br><sub>-,1,2,2,0</sub> |  | 0.6 | 0.2 | 0.7 | 6.7 |
| Branden Carlson (POR) | 88% | 9.9<br><sub>10,8,14,14,10</sub> | 2.7<br><sub>0,5,5,6,0</sub> |  | 2.2<br><sub>2,3,6,1,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.2<br><sub>0,1,1,0,0</sub> |  | 0.3 | 0.4 | 0.5 | 5.2 |
| Yang Hansen (POR) | 58% | 8.1<br><sub>-,-,7,-,12</sub> | 2.7<br><sub>-,-,0,-,2</sub> |  | 1.9<br><sub>-,-,1,-,1</sub> |  | 0.5<br><sub>-,-,3,-,1</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.0 |
| John Tonje (POR) | 52% | 7.1<br><sub>-,-,7,-,6</sub> | 2.7<br><sub>-,-,7,-,0</sub> |  | 1.6<br><sub>-,-,4,-,3</sub> |  | 0.7<br><sub>-,-,3,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.2 | 0.4 | 5.0 |
| Micah Potter (POR) | 52% | 6.9<br><sub>-,-,7,1,-</sub> | 2.9<br><sub>-,-,2,0,-</sub> |  | 1.8<br><sub>-,-,4,0,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.1 | 0.4 | 5.1 |

</details>


### LAC @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Bradley Beal (LAC), Brandon Ingram (LAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.7–117.0 | LAC 49% | 2.03 / 1.97 | DAL +0.5 | 233.5 | DAL -5.5 covers 36%; o229.5 59% |
| Expected (weighted by chance each plays) | 116.5–117.4 | LAC 47% | 2.12 / 1.90 | DAL -1.5 | 234.5 | DAL -5.5 covers 37%; o229.5 61% |
| if Walter Clayton Jr. plays | 116.3–117.3 | LAC 47% | 2.12 / 1.90 | DAL -1.5 | 233.5 | DAL -5.5 covers 37%; o229.5 58% |
| if P.J. Washington plays | 116.2–117.3 | LAC 47% | 2.13 / 1.89 | DAL -1.5 | 233.5 | DAL -5.5 covers 38%; o229.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Walter Clayton Jr. (DAL) | Questionable | 55% | 21.1 | 7.8 | 3.1 | 3.8 | 1.0 | 0.7 | 0.2 | 1.7 | 14.7 | full tables below |
| Jett Howard (DAL) | Questionable | 55% | 8.0 | 2.9 | 0.9 | 0.6 | 0.3 | 0.2 | 0.1 | 0.3 | 4.4 | small |
| P.J. Washington (DAL) | Questionable | 55% | 31.5 | 14.2 | 6.7 | 1.7 | 1.8 | 0.9 | 0.9 | 1.6 | 22.6 | full tables below |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 33.0<br><sub>25,37,35,30,35</sub> | 22.8<br><sub>13,24,27,20,23</sub> |  | 2.7<br><sub>5,4,6,3,0</sub> |  | 7.2<br><sub>6,7,7,7,5</sub> |  | 2.9<br><sub>1,3,3,2,3</sub> |  | 1.2 | 0.2 | 3.4 | 32.7 |
| Rui Hachimura | 98% | 28.6<br><sub>23,32,22,27,32</sub> | 14.1<br><sub>13,7,4,20,17</sub> |  | 4.6<br><sub>5,11,2,5,7</sub> |  | 1.5<br><sub>1,3,0,1,2</sub> |  | 1.7<br><sub>3,1,0,4,2</sub> |  | 0.8 | 0.4 | 1.2 | 20.2 |
| Derrick Jones Jr. | 98% | 27.1<br><sub>24,29,26,28,27</sub> | 10.4<br><sub>11,14,13,5,8</sub> |  | 3.9<br><sub>3,5,4,1,2</sub> |  | 1.4<br><sub>0,0,1,1,1</sub> |  | 1.1<br><sub>2,4,3,0,0</sub> |  | 1.0 | 0.9 | 0.9 | 15.6 |
| Brook Lopez | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.2<br><sub>8,26,7,23,23</sub> |  | 5.0<br><sub>4,7,5,6,3</sub> |  | 2.1<br><sub>1,4,8,2,4</sub> |  | 1.6<br><sub>1,3,1,4,5</sub> |  | 0.7 | 1.3 | 1.2 | 20.3 |
| Max Strus | 98% | 24.3<br><sub>22,23,25,21,32</sub> | 9.6<br><sub>12,3,14,3,18</sub> |  | 4.0<br><sub>3,2,3,2,5</sub> |  | 2.9<br><sub>3,3,4,1,4</sub> |  | 1.6<br><sub>2,0,4,1,5</sub> |  | 0.8 | 0.1 | 1.1 | 16.5 |
| Kris Dunn | 98% | 22.9<br><sub>19,20,18,26,20</sub> | 6.4<br><sub>3,2,7,2,6</sub> |  | 3.2<br><sub>2,3,3,5,2</sub> |  | 3.5<br><sub>3,6,1,5,2</sub> |  | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.1 |
| Keaton Wagler | 98% | 20.4<br><sub>23,18,28,18,17</sub> | 10.7<br><sub>11,14,12,15,7</sub> |  | 2.8<br><sub>0,2,4,2,5</sub> |  | 2.8<br><sub>4,1,5,0,2</sub> |  | 1.3<br><sub>1,2,2,1,1</sub> |  | 0.7 | 0.2 | 1.8 | 16.3 |
| Kobe Sanders | 98% | 18.7<br><sub>26,15,20,18,14</sub> | 7.2<br><sub>9,5,2,5,0</sub> |  | 2.2<br><sub>3,0,6,1,1</sub> |  | 2.0<br><sub>7,1,4,3,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.4 |
| Gradey Dick | 98% | 14.9<br><sub>19,19,19,17,13</sub> | 6.5<br><sub>10,13,12,0,2</sub> |  | 2.2<br><sub>3,3,2,0,2</sub> |  | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.6<br><sub>1,2,2,0,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.5 |
| Isaiah Jackson | 98% | 14.6<br><sub>16,17,15,19,9</sub> | 6.8<br><sub>4,5,13,8,6</sub> |  | 4.5<br><sub>4,3,2,5,4</sub> |  | 1.3<br><sub>0,3,2,0,2</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 12.6 |
| Yanic Konan Niederhauser | 52% | 9.6<br><sub>-,-,-,-,11</sub> | 4.1<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,3</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 6.9 |
| Baba Miller | 88% | 9.1<br><sub>16,-,5,4,1</sub> | 4.5<br><sub>13,-,2,3,0</sub> |  | 1.4<br><sub>4,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Cam Christie | 58% | 6.7<br><sub>-,-,-,4,1</sub> | 2.9<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley | 52% | 6.3<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 36.6<br><sub>39,27,38,27,34</sub> | 25.7<br><sub>43,12,18,17,33</sub> |  | 7.3<br><sub>10,7,8,3,5</sub> |  | 6.5<br><sub>6,3,5,4,9</sub> |  | 1.5<br><sub>3,1,0,2,3</sub> |  | 1.6 | 0.9 | 3.1 | 39.6 |
| Kyrie Irving | 98% | 36.0<br><sub>38,27,37,-,29</sub> | 25.1<br><sub>35,10,34,-,17</sub> |  | 4.5<br><sub>0,3,6,-,6</sub> |  | 5.2<br><sub>4,4,5,-,5</sub> |  | 3.2<br><sub>7,2,7,-,1</sub> |  | 1.5 | 0.5 | 2.5 | 34.8 |
| Naji Marshall | 96% | 30.6<br><sub>25,23,30,23,27</sub> | 15.3<br><sub>6,13,12,13,12</sub> |  | 4.3<br><sub>5,1,3,2,5</sub> |  | 4.1<br><sub>2,4,5,2,2</sub> |  | 1.1<br><sub>0,1,0,3,2</sub> |  | 1.2 | 0.1 | 2.0 | 23.8 |
| Caleb Martin | 98% | 25.5<br><sub>19,21,33,34,20</sub> | 7.1<br><sub>0,7,15,12,8</sub> |  | 4.0<br><sub>3,2,8,5,5</sub> |  | 2.2<br><sub>5,5,3,5,3</sub> |  | 0.8<br><sub>0,1,1,4,2</sub> |  | 1.0 | 0.4 | 1.0 | 13.3 |
| Daniel Gafford | 99% | 25.3<br><sub>20,16,17,19,24</sub> | 10.9<br><sub>8,3,10,3,6</sub> |  | 7.3<br><sub>2,3,3,4,6</sub> |  | 1.7<br><sub>3,1,1,2,2</sub> |  | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.6 | 1.2 | 19.9 |
| Zaccharie Risacher | 98% | 24.3<br><sub>15,25,14,27,18</sub> | 8.7<br><sub>4,22,5,18,3</sub> |  | 4.6<br><sub>2,6,2,5,3</sub> |  | 1.3<br><sub>0,3,0,0,0</sub> |  | 1.1<br><sub>0,4,1,1,1</sub> |  | 0.9 | 0.8 | 1.1 | 14.6 |
| Morez Johnson Jr. | 98% | 19.5<br><sub>-,13,15,26,15</sub> | 7.2<br><sub>-,0,4,2,3</sub> |  | 3.8<br><sub>-,2,2,6,1</sub> |  | 1.7<br><sub>-,0,0,4,1</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.1 | 12.6 |
| Max Christie | 98% | 18.9<br><sub>5,7,-,-,8</sub> | 7.0<br><sub>0,3,-,-,5</sub> |  | 2.3<br><sub>2,2,-,-,1</sub> |  | 1.3<br><sub>0,0,-,-,2</sub> |  | 1.1<br><sub>0,1,-,-,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.6 |
| Santi Aldama | 98% | 16.6<br><sub>19,10,16,-,6</sub> | 7.8<br><sub>10,3,7,-,0</sub> |  | 3.9<br><sub>4,1,2,-,0</sub> |  | 1.3<br><sub>1,1,1,-,0</sub> |  | 0.9<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.4 | 0.9 | 13.0 |
| Marcus Sasser | 67% | 15.1<br><sub>-,9,-,18,4</sub> | 5.2<br><sub>-,3,-,5,0</sub> |  | 1.4<br><sub>-,1,-,1,2</sub> |  | 1.8<br><sub>-,0,-,2,1</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 8.4 |
| Moussa Cisse | 67% | 8.9<br><sub>-,8,-,4,4</sub> | 3.1<br><sub>-,0,-,1,0</sub> |  | 3.2<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.6 | 0.4 | 6.5 |

</details>

<details><summary>if P.J. Washington plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 35.1<br><sub>39,27,38,27,34</sub> | 24.8<br><sub>43,12,18,17,33</sub> |  | 7.0<br><sub>10,7,8,3,5</sub> |  | 6.4<br><sub>6,3,5,4,9</sub> |  | 1.4<br><sub>3,1,0,2,3</sub> |  | 1.6 | 0.8 | 2.9 | 38.2 |
| Kyrie Irving (DAL) | 98% | 34.6<br><sub>38,27,37,-,29</sub> | 23.3<br><sub>35,10,34,-,17</sub> |  | 4.3<br><sub>0,3,6,-,6</sub> |  | 4.8<br><sub>4,4,5,-,5</sub> |  | 3.0<br><sub>7,2,7,-,1</sub> |  | 1.4 | 0.5 | 2.4 | 32.4 |
| P.J. Washington (DAL) | 100% | 31.5<br><sub>35,16,26,25,25</sub> | 14.2<br><sub>13,10,10,8,21</sub> |  | 6.7<br><sub>9,3,4,5,5</sub> |  | 1.7<br><sub>1,0,1,4,2</sub> |  | 1.8<br><sub>2,1,2,0,5</sub> |  | 0.9 | 0.9 | 1.6 | 22.6 |
| Naji Marshall (DAL) | 96% | 26.8<br><sub>25,23,30,23,27</sub> | 13.3<br><sub>6,13,12,13,12</sub> |  | 3.8<br><sub>5,1,3,2,5</sub> |  | 3.7<br><sub>2,4,5,2,2</sub> |  | 0.9<br><sub>0,1,0,3,2</sub> |  | 1.1 | 0.1 | 1.9 | 20.8 |
| Daniel Gafford (DAL) | 99% | 21.5<br><sub>20,16,17,19,24</sub> | 9.6<br><sub>8,3,10,3,6</sub> |  | 6.1<br><sub>2,3,3,4,6</sub> |  | 1.4<br><sub>3,1,1,2,2</sub> |  | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 1.4 | 1.1 | 17.2 |
| Caleb Martin (DAL) | 98% | 21.3<br><sub>19,21,33,34,20</sub> | 5.9<br><sub>0,7,15,12,8</sub> |  | 3.4<br><sub>3,2,8,5,5</sub> |  | 1.9<br><sub>5,5,3,5,3</sub> |  | 0.6<br><sub>0,1,1,4,2</sub> |  | 0.9 | 0.3 | 0.8 | 11.2 |
| Zaccharie Risacher (DAL) | 98% | 19.8<br><sub>15,25,14,27,18</sub> | 7.1<br><sub>4,22,5,18,3</sub> |  | 3.7<br><sub>2,6,2,5,3</sub> |  | 1.1<br><sub>0,3,0,0,0</sub> |  | 0.8<br><sub>0,4,1,1,1</sub> |  | 0.7 | 0.7 | 0.9 | 11.9 |
| Morez Johnson Jr. (DAL) | 98% | 15.2<br><sub>-,13,15,26,15</sub> | 5.5<br><sub>-,0,4,2,3</sub> |  | 3.0<br><sub>-,2,2,6,1</sub> |  | 1.3<br><sub>-,0,0,4,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.8 |
| Max Christie (DAL) | 98% | 14.3<br><sub>5,7,-,-,8</sub> | 5.3<br><sub>0,3,-,-,5</sub> |  | 1.7<br><sub>2,2,-,-,1</sub> |  | 1.0<br><sub>0,0,-,-,2</sub> |  | 0.7<br><sub>0,1,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 8.0 |
| Santi Aldama (DAL) | 98% | 12.2<br><sub>19,10,16,-,6</sub> | 5.9<br><sub>10,3,7,-,0</sub> |  | 2.9<br><sub>4,1,2,-,0</sub> |  | 1.0<br><sub>1,1,1,-,0</sub> |  | 0.6<br><sub>1,1,2,-,0</sub> |  | 0.4 | 0.3 | 0.7 | 9.8 |
| Marcus Sasser (DAL) | 67% | 11.5<br><sub>-,9,-,18,4</sub> | 4.0<br><sub>-,3,-,5,0</sub> |  | 1.0<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.4 |
| Moussa Cisse (DAL) | 67% | 6.9<br><sub>-,8,-,4,4</sub> | 2.5<br><sub>-,0,-,1,0</sub> |  | 2.5<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.3 |
| Darius Garland (LAC) | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.7<br><sub>13,24,27,20,23</sub> |  | 2.7<br><sub>5,4,6,3,0</sub> |  | 7.3<br><sub>6,7,7,7,5</sub> |  | 2.9<br><sub>1,3,3,2,3</sub> |  | 1.2 | 0.2 | 3.4 | 32.6 |
| Rui Hachimura (LAC) | 98% | 28.5<br><sub>23,32,22,27,32</sub> | 14.0<br><sub>13,7,4,20,17</sub> |  | 4.5<br><sub>5,11,2,5,7</sub> |  | 1.5<br><sub>1,3,0,1,2</sub> |  | 1.7<br><sub>3,1,0,4,2</sub> |  | 0.8 | 0.4 | 1.1 | 20.1 |
| Derrick Jones Jr. (LAC) | 98% | 27.0<br><sub>24,29,26,28,27</sub> | 10.3<br><sub>11,14,13,5,8</sub> |  | 3.8<br><sub>3,5,4,1,2</sub> |  | 1.4<br><sub>0,0,1,1,1</sub> |  | 1.1<br><sub>2,4,3,0,0</sub> |  | 1.0 | 0.9 | 0.9 | 15.5 |
| Brook Lopez (LAC) | 98% | 25.3<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> |  | 5.1<br><sub>4,7,5,6,3</sub> |  | 2.2<br><sub>1,4,8,2,4</sub> |  | 1.6<br><sub>1,3,1,4,5</sub> |  | 0.7 | 1.3 | 1.2 | 20.3 |
| Max Strus (LAC) | 98% | 24.3<br><sub>22,23,25,21,32</sub> | 9.6<br><sub>12,3,14,3,18</sub> |  | 4.0<br><sub>3,2,3,2,5</sub> |  | 2.9<br><sub>3,3,4,1,4</sub> |  | 1.7<br><sub>2,0,4,1,5</sub> |  | 0.8 | 0.1 | 1.1 | 16.5 |
| Kris Dunn (LAC) | 98% | 22.8<br><sub>19,20,18,26,20</sub> | 6.4<br><sub>3,2,7,2,6</sub> |  | 3.2<br><sub>2,3,3,5,2</sub> |  | 3.5<br><sub>3,6,1,5,2</sub> |  | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.0 |
| Keaton Wagler (LAC) | 98% | 20.5<br><sub>23,18,28,18,17</sub> | 10.8<br><sub>11,14,12,15,7</sub> |  | 2.9<br><sub>0,2,4,2,5</sub> |  | 2.8<br><sub>4,1,5,0,2</sub> |  | 1.3<br><sub>1,2,2,1,1</sub> |  | 0.7 | 0.2 | 1.8 | 16.4 |
| Kobe Sanders (LAC) | 98% | 18.7<br><sub>26,15,20,18,14</sub> | 7.3<br><sub>9,5,2,5,0</sub> |  | 2.2<br><sub>3,0,6,1,1</sub> |  | 2.0<br><sub>7,1,4,3,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.5 |
| Gradey Dick (LAC) | 98% | 14.9<br><sub>19,19,19,17,13</sub> | 6.4<br><sub>10,13,12,0,2</sub> |  | 2.2<br><sub>3,3,2,0,2</sub> |  | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.6<br><sub>1,2,2,0,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.4 |
| Isaiah Jackson (LAC) | 98% | 14.6<br><sub>16,17,15,19,9</sub> | 6.7<br><sub>4,5,13,8,6</sub> |  | 4.5<br><sub>4,3,2,5,4</sub> |  | 1.3<br><sub>0,3,2,0,2</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 12.5 |
| Yanic Konan Niederhauser (LAC) | 52% | 9.8<br><sub>-,-,-,-,11</sub> | 4.1<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 7.0 |
| Baba Miller (LAC) | 88% | 9.1<br><sub>16,-,5,4,1</sub> | 4.5<br><sub>13,-,2,3,0</sub> |  | 1.4<br><sub>4,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Cam Christie (LAC) | 58% | 6.8<br><sub>-,-,-,4,1</sub> | 2.9<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Blake Wesley (LAC) | 52% | 6.3<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |

</details>

<details><summary>if Walter Clayton Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 36.0<br><sub>39,27,38,27,34</sub> | 25.5<br><sub>43,12,18,17,33</sub> |  | 7.2<br><sub>10,7,8,3,5</sub> |  | 6.3<br><sub>6,3,5,4,9</sub> |  | 1.5<br><sub>3,1,0,2,3</sub> |  | 1.6 | 0.8 | 3.0 | 39.1 |
| Kyrie Irving (DAL) | 98% | 35.1<br><sub>38,27,37,-,29</sub> | 23.7<br><sub>35,10,34,-,17</sub> |  | 4.5<br><sub>0,3,6,-,6</sub> |  | 4.7<br><sub>4,4,5,-,5</sub> |  | 3.0<br><sub>7,2,7,-,1</sub> |  | 1.4 | 0.5 | 2.4 | 32.9 |
| Naji Marshall (DAL) | 96% | 28.1<br><sub>25,23,30,23,27</sub> | 13.8<br><sub>6,13,12,13,12</sub> |  | 4.0<br><sub>5,1,3,2,5</sub> |  | 3.7<br><sub>2,4,5,2,2</sub> |  | 0.9<br><sub>0,1,0,3,2</sub> |  | 1.1 | 0.1 | 1.9 | 21.5 |
| Daniel Gafford (DAL) | 99% | 23.2<br><sub>20,16,17,19,24</sub> | 10.2<br><sub>8,3,10,3,6</sub> |  | 6.5<br><sub>2,3,3,4,6</sub> |  | 1.5<br><sub>3,1,1,2,2</sub> |  | 0.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 1.5 | 1.1 | 18.2 |
| Caleb Martin (DAL) | 98% | 23.2<br><sub>19,21,33,34,20</sub> | 6.5<br><sub>0,7,15,12,8</sub> |  | 3.6<br><sub>3,2,8,5,5</sub> |  | 2.0<br><sub>5,5,3,5,3</sub> |  | 0.7<br><sub>0,1,1,4,2</sub> |  | 0.9 | 0.3 | 0.9 | 12.1 |
| Zaccharie Risacher (DAL) | 98% | 22.0<br><sub>15,25,14,27,18</sub> | 8.1<br><sub>4,22,5,18,3</sub> |  | 4.1<br><sub>2,6,2,5,3</sub> |  | 1.1<br><sub>0,3,0,0,0</sub> |  | 0.9<br><sub>0,4,1,1,1</sub> |  | 0.8 | 0.7 | 1.0 | 13.3 |
| Walter Clayton Jr. (DAL) | 100% | 21.1<br><sub>25,22,13,23,27</sub> | 7.8<br><sub>6,5,2,13,8</sub> |  | 3.1<br><sub>6,1,2,4,2</sub> |  | 3.8<br><sub>4,4,2,3,7</sub> |  | 1.0<br><sub>1,0,0,3,2</sub> |  | 0.7 | 0.2 | 1.7 | 14.7 |
| Morez Johnson Jr. (DAL) | 98% | 17.3<br><sub>-,13,15,26,15</sub> | 6.3<br><sub>-,0,4,2,3</sub> |  | 3.4<br><sub>-,2,2,6,1</sub> |  | 1.5<br><sub>-,0,0,4,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 11.2 |
| Max Christie (DAL) | 98% | 15.6<br><sub>5,7,-,-,8</sub> | 5.8<br><sub>0,3,-,-,5</sub> |  | 1.9<br><sub>2,2,-,-,1</sub> |  | 1.0<br><sub>0,0,-,-,2</sub> |  | 0.8<br><sub>0,1,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 8.7 |
| Santi Aldama (DAL) | 98% | 14.6<br><sub>19,10,16,-,6</sub> | 7.1<br><sub>10,3,7,-,0</sub> |  | 3.4<br><sub>4,1,2,-,0</sub> |  | 1.1<br><sub>1,1,1,-,0</sub> |  | 0.8<br><sub>1,1,2,-,0</sub> |  | 0.5 | 0.3 | 0.8 | 11.6 |
| Marcus Sasser (DAL) | 67% | 12.0<br><sub>-,9,-,18,4</sub> | 4.1<br><sub>-,3,-,5,0</sub> |  | 1.1<br><sub>-,1,-,1,2</sub> |  | 1.4<br><sub>-,0,-,2,1</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.6 |
| Moussa Cisse (DAL) | 67% | 7.5<br><sub>-,8,-,4,4</sub> | 2.7<br><sub>-,0,-,1,0</sub> |  | 2.7<br><sub>-,0,-,1,1</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.6 |
| Darius Garland (LAC) | 98% | 32.9<br><sub>25,37,35,30,35</sub> | 22.6<br><sub>13,24,27,20,23</sub> |  | 2.7<br><sub>5,4,6,3,0</sub> |  | 7.3<br><sub>6,7,7,7,5</sub> |  | 2.9<br><sub>1,3,3,2,3</sub> |  | 1.2 | 0.2 | 3.4 | 32.5 |
| Rui Hachimura (LAC) | 98% | 28.4<br><sub>23,32,22,27,32</sub> | 13.9<br><sub>13,7,4,20,17</sub> |  | 4.6<br><sub>5,11,2,5,7</sub> |  | 1.5<br><sub>1,3,0,1,2</sub> |  | 1.7<br><sub>3,1,0,4,2</sub> |  | 0.8 | 0.4 | 1.2 | 20.0 |
| Derrick Jones Jr. (LAC) | 98% | 27.0<br><sub>24,29,26,28,27</sub> | 10.3<br><sub>11,14,13,5,8</sub> |  | 3.8<br><sub>3,5,4,1,2</sub> |  | 1.4<br><sub>0,0,1,1,1</sub> |  | 1.1<br><sub>2,4,3,0,0</sub> |  | 1.0 | 0.9 | 0.9 | 15.6 |
| Brook Lopez (LAC) | 98% | 25.2<br><sub>19,31,29,23,27</sub> | 13.1<br><sub>8,26,7,23,23</sub> |  | 5.0<br><sub>4,7,5,6,3</sub> |  | 2.1<br><sub>1,4,8,2,4</sub> |  | 1.6<br><sub>1,3,1,4,5</sub> |  | 0.7 | 1.3 | 1.1 | 20.3 |
| Max Strus (LAC) | 98% | 24.3<br><sub>22,23,25,21,32</sub> | 9.5<br><sub>12,3,14,3,18</sub> |  | 4.0<br><sub>3,2,3,2,5</sub> |  | 2.9<br><sub>3,3,4,1,4</sub> |  | 1.7<br><sub>2,0,4,1,5</sub> |  | 0.8 | 0.1 | 1.1 | 16.4 |
| Kris Dunn (LAC) | 98% | 22.9<br><sub>19,20,18,26,20</sub> | 6.5<br><sub>3,2,7,2,6</sub> |  | 3.2<br><sub>2,3,3,5,2</sub> |  | 3.5<br><sub>3,6,1,5,2</sub> |  | 0.6<br><sub>1,0,0,0,1</sub> |  | 1.5 | 0.3 | 1.1 | 13.2 |
| Keaton Wagler (LAC) | 98% | 20.4<br><sub>23,18,28,18,17</sub> | 10.7<br><sub>11,14,12,15,7</sub> |  | 2.9<br><sub>0,2,4,2,5</sub> |  | 2.8<br><sub>4,1,5,0,2</sub> |  | 1.3<br><sub>1,2,2,1,1</sub> |  | 0.7 | 0.2 | 1.8 | 16.3 |
| Kobe Sanders (LAC) | 98% | 18.8<br><sub>26,15,20,18,14</sub> | 7.3<br><sub>9,5,2,5,0</sub> |  | 2.2<br><sub>3,0,6,1,1</sub> |  | 2.0<br><sub>7,1,4,3,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.8 | 0.1 | 1.1 | 11.5 |
| Gradey Dick (LAC) | 98% | 14.9<br><sub>19,19,19,17,13</sub> | 6.5<br><sub>10,13,12,0,2</sub> |  | 2.2<br><sub>3,3,2,0,2</sub> |  | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.6<br><sub>1,2,2,0,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.5 |
| Isaiah Jackson (LAC) | 98% | 14.6<br><sub>16,17,15,19,9</sub> | 6.7<br><sub>4,5,13,8,6</sub> |  | 4.5<br><sub>4,3,2,5,4</sub> |  | 1.2<br><sub>0,3,2,0,2</sub> |  | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 12.4 |
| Yanic Konan Niederhauser (LAC) | 52% | 9.7<br><sub>-,-,-,-,11</sub> | 4.1<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 7.0 |
| Baba Miller (LAC) | 88% | 9.1<br><sub>16,-,5,4,1</sub> | 4.5<br><sub>13,-,2,3,0</sub> |  | 1.4<br><sub>4,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Cam Christie (LAC) | 58% | 6.7<br><sub>-,-,-,4,1</sub> | 2.8<br><sub>-,-,-,3,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Blake Wesley (LAC) | 52% | 6.2<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |

</details>


### MEM @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Cameron Boozer (MEM), Jerami Grant (MEM), GG Jackson (MEM), Scotty Pippen Jr. (MEM), Javon Small (MEM)

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cedric Coward | 99% | 32.5<br><sub>30,33,27,33,25</sub> | 16.4<br><sub>14,23,18,20,19</sub> |  | 7.7<br><sub>7,12,8,3,4</sub> |  | 4.0<br><sub>6,4,6,5,4</sub> |  | 1.9<br><sub>0,4,2,4,5</sub> |  | 1.1 | 0.6 | 2.1 | 28.2 |
| Ty Jerome | 92% | 30.4<br><sub>29,-,-,-,-</sub> | 23.2<br><sub>17,-,-,-,-</sub> |  | 3.8<br><sub>2,-,-,-,-</sub> |  | 6.1<br><sub>9,-,-,-,-</sub> |  | 2.4<br><sub>2,-,-,-,-</sub> |  | 1.1 | 0.3 | 2.7 | 33.0 |
| Jaylen Wells | 99% | 30.2<br><sub>27,25,27,26,24</sub> | 11.8<br><sub>11,5,8,5,22</sub> |  | 3.6<br><sub>2,2,4,4,7</sub> |  | 1.6<br><sub>1,2,3,2,0</sub> |  | 1.7<br><sub>2,1,2,1,4</sub> |  | 0.9 | 0.2 | 1.1 | 17.0 |
| Cam Spencer | 98% | 29.1<br><sub>24,34,32,29,27</sub> | 13.3<br><sub>14,17,12,26,9</sub> |  | 3.5<br><sub>2,1,6,1,2</sub> |  | 7.2<br><sub>5,8,9,7,11</sub> |  | 1.7<br><sub>3,3,1,5,1</sub> |  | 0.9 | 0.2 | 1.8 | 24.0 |
| Taylor Hendricks | 88% | 24.0<br><sub>19,29,19,21,20</sub> | 10.6<br><sub>10,22,9,18,11</sub> |  | 4.9<br><sub>12,5,3,6,1</sub> |  | 1.4<br><sub>2,4,0,2,1</sub> |  | 1.2<br><sub>2,0,1,1,0</sub> |  | 1.1 | 0.6 | 1.1 | 16.8 |
| Zach Edey | 88% | 23.8<br><sub>-,-,21,21,-</sub> | 10.2<br><sub>-,-,23,11,-</sub> |  | 8.7<br><sub>-,-,10,2,-</sub> |  | 1.2<br><sub>-,-,1,1,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.5 | 1.6 | 1.7 | 20.1 |
| Olivier-Maxence Prosper | 86% | 21.6<br><sub>2,20,16,16,24</sub> | 10.8<br><sub>6,11,12,5,16</sub> |  | 4.0<br><sub>1,4,0,2,5</sub> |  | 1.2<br><sub>0,0,1,0,1</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.8 | 0.3 | 1.0 | 15.9 |
| Isaiah Stewart | 98% | 20.3<br><sub>20,15,-,-,18</sub> | 9.3<br><sub>12,11,-,-,8</sub> |  | 4.2<br><sub>5,3,-,-,4</sub> |  | 1.2<br><sub>0,3,-,-,1</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.4 | 1.3 | 1.1 | 14.7 |
| Jahmai Mashack | 71% | 18.2<br><sub>-,2,2,13,26</sub> | 4.9<br><sub>-,0,0,3,0</sub> |  | 2.4<br><sub>-,0,0,2,3</sub> |  | 2.4<br><sub>-,0,1,2,4</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.8 | 0.4 | 1.0 | 9.6 |
| Kris Murray | 88% | 16.2<br><sub>1,19,6,6,4</sub> | 3.1<br><sub>0,3,0,5,0</sub> |  | 2.4<br><sub>1,2,1,0,1</sub> |  | 1.0<br><sub>0,3,0,0,0</sub> |  | 0.3<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 6.6 |
| Quinten Post | 96% | 14.1<br><sub>-,-,9,6,10</sub> | 5.2<br><sub>-,-,5,3,5</sub> |  | 2.7<br><sub>-,-,3,2,1</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.4 | 0.4 | 0.7 | 8.4 |
| Karim Lopez | 58% | 11.5<br><sub>-,2,1,-,4</sub> | 3.4<br><sub>-,0,0,-,3</sub> |  | 2.1<br><sub>-,2,0,-,0</sub> |  | 0.6<br><sub>-,0,0,-,0</sub> |  | 0.3<br><sub>-,0,0,-,1</sub> |  | 0.6 | 0.6 | 0.5 | 6.1 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 99% | 36.0<br><sub>25,37,31,37,39</sub> | 18.1<br><sub>16,18,13,22,17</sub> |  | 6.0<br><sub>9,5,6,5,3</sub> |  | 3.3<br><sub>3,6,3,4,1</sub> |  | 1.6<br><sub>0,2,0,2,4</sub> |  | 1.3 | 1.2 | 2.0 | 27.4 |
| Ayo Dosunmu | 99% | 33.7<br><sub>27,33,30,39,32</sub> | 19.1<br><sub>18,24,8,30,6</sub> |  | 4.7<br><sub>2,5,5,4,4</sub> |  | 4.1<br><sub>1,0,2,5,4</sub> |  | 2.2<br><sub>2,0,2,7,2</sub> |  | 1.3 | 0.5 | 2.0 | 27.8 |
| Jonathan Kuminga | 84% | 31.9<br><sub>24,35,29,-,35</sub> | 14.8<br><sub>14,11,13,-,23</sub> |  | 6.1<br><sub>8,3,9,-,3</sub> |  | 2.6<br><sub>5,3,1,-,3</sub> |  | 1.4<br><sub>1,0,1,-,2</sub> |  | 1.0 | 0.8 | 1.7 | 23.5 |
| LaMelo Ball | 99% | 31.4<br><sub>25,30,24,31,35</sub> | 21.2<br><sub>22,19,6,18,15</sub> |  | 5.0<br><sub>3,8,5,9,8</sub> |  | 6.5<br><sub>9,6,0,2,8</sub> |  | 3.6<br><sub>6,4,2,3,3</sub> |  | 1.7 | 0.3 | 3.0 | 32.7 |
| Rudy Gobert | 99% | 31.1<br><sub>23,27,32,22,35</sub> | 10.0<br><sub>9,1,18,0,9</sub> |  | 11.6<br><sub>6,10,15,4,7</sub> |  | 1.8<br><sub>1,4,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.8 | 1.5 | 23.4 |
| Terrence Shannon Jr. | 98% | 24.2<br><sub>21,22,35,24,21</sub> | 13.6<br><sub>6,14,34,12,10</sub> |  | 3.1<br><sub>2,6,3,1,4</sub> |  | 2.5<br><sub>4,0,6,4,3</sub> |  | 1.2<br><sub>0,0,3,1,0</sub> |  | 0.7 | 0.2 | 1.2 | 19.3 |
| Trey Lyles | 98% | 20.4<br><sub>15,19,19,31,16</sub> | 6.5<br><sub>2,5,9,8,8</sub> |  | 4.6<br><sub>0,1,3,7,6</sub> |  | 1.2<br><sub>0,2,1,4,1</sub> |  | 0.9<br><sub>0,0,2,2,2</sub> |  | 0.7 | 0.4 | 0.7 | 12.3 |
| Joan Beringer | 98% | 16.5<br><sub>22,13,16,26,13</sub> | 6.3<br><sub>13,2,0,3,5</sub> |  | 5.9<br><sub>9,5,4,13,3</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.5 | 0.6 | 12.7 |
| Bones Hyland | 98% | 15.6<br><sub>23,21,13,17,15</sub> | 9.2<br><sub>24,12,5,13,6</sub> |  | 1.7<br><sub>3,1,1,2,1</sub> |  | 2.6<br><sub>8,2,5,1,1</sub> |  | 1.3<br><sub>5,3,0,3,1</sub> |  | 0.7 | 0.2 | 1.0 | 13.4 |
| Cody Williams | 58% | 7.9<br><sub>7,-,4,13,-</sub> | 0.2<br><sub>0,-,0,0,-</sub> |  | 1.2<br><sub>1,-,1,1,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 1.8 |
| Zyon Pullin | 38% | 6.5<br><sub>-,-,4,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Johni Broome | 3% | 5.9 | 2.3 |  | 1.5 |  | 0.5 |  | 0.1 |  | 0.3 | 0.2 | 0.3 | 4.2 |
| Isaiah Evans | 48% | 5.7<br><sub>8,-,4,-,-</sub> | 4.3<br><sub>2,-,0,-,-</sub> |  | 1.2<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |

</details>


### NOP @ SAS
Out: Dylan Harper (SAS), Tobias Harris (SAS), Bennedict Mathurin (NOP), Bryce McGowens (NOP), Dejounte Murray (NOP), Trendon Watford (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 31.5<br><sub>29,35,41,33,42</sub> | 14.8<br><sub>15,30,16,23,10</sub> |  | 4.7<br><sub>1,10,6,6,8</sub> |  | 2.6<br><sub>2,0,4,3,6</sub> |  | 2.0<br><sub>3,6,2,5,2</sub> |  | 0.8 | 0.2 | 1.0 | 22.1 |
| Zion Williamson | 98% | 30.4<br><sub>30,33,31,25,32</sub> | 18.4<br><sub>29,22,24,16,24</sub> |  | 5.4<br><sub>4,5,6,6,7</sub> |  | 2.8<br><sub>2,4,2,2,1</sub> |  | 0.3<br><sub>1,0,2,0,0</sub> |  | 1.1 | 0.5 | 2.0 | 26.6 |
| Trey Murphy III | 98% | 30.3<br><sub>-,-,-,-,-</sub> | 14.5<br><sub>-,-,-,-,-</sub> |  | 4.3<br><sub>-,-,-,-,-</sub> |  | 3.1<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.0 | 0.4 | 1.4 | 22.0 |
| Jeremiah Fears | 99% | 29.5<br><sub>28,34,33,29,31</sub> | 15.1<br><sub>14,18,13,19,16</sub> |  | 4.4<br><sub>4,5,4,10,5</sub> |  | 4.9<br><sub>5,7,7,10,4</sub> |  | 1.4<br><sub>2,0,1,1,2</sub> |  | 1.1 | 0.5 | 2.6 | 24.4 |
| Herbert Jones | 98% | 24.6<br><sub>25,32,27,24,32</sub> | 7.7<br><sub>2,8,10,8,9</sub> |  | 2.8<br><sub>2,2,2,2,1</sub> |  | 2.0<br><sub>3,3,1,3,3</sub> |  | 1.0<br><sub>0,0,2,2,3</sub> |  | 1.1 | 0.4 | 1.1 | 12.5 |
| Jordan Poole | 86% | 23.6<br><sub>21,21,24,31,30</sub> | 11.0<br><sub>14,13,14,11,22</sub> |  | 2.3<br><sub>0,2,2,2,1</sub> |  | 3.3<br><sub>1,5,5,5,5</sub> |  | 1.6<br><sub>2,1,1,1,3</sub> |  | 0.7 | 0.4 | 1.6 | 16.6 |
| Derik Queen | 99% | 21.5<br><sub>14,23,25,21,19</sub> | 10.4<br><sub>9,10,10,17,9</sub> |  | 5.9<br><sub>0,6,5,10,5</sub> |  | 2.4<br><sub>0,2,4,0,0</sub> |  | 0.6<br><sub>1,0,2,4,0</sub> |  | 0.9 | 0.7 | 1.9 | 18.7 |
| Yves Missi | 98% | 18.1<br><sub>-,-,22,23,17</sub> | 5.6<br><sub>-,-,3,6,4</sub> |  | 5.4<br><sub>-,-,8,14,5</sub> |  | 1.3<br><sub>-,-,1,1,2</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 1.1 | 0.8 | 12.3 |
| Karlo Matkovic | 98% | 14.9<br><sub>22,19,14,20,10</sub> | 5.1<br><sub>4,1,5,3,0</sub> |  | 3.1<br><sub>4,3,3,2,2</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.6 | 0.6 | 9.0 |
| Jaron Pierre Jr. | 96% | 14.5<br><sub>7,4,23,19,17</sub> | 6.0<br><sub>4,0,13,10,7</sub> |  | 1.8<br><sub>4,0,2,4,1</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>1,0,2,2,1</sub> |  | 0.4 | 0.2 | 0.9 | 8.6 |
| DeAndre Jordan | 52% | 11.4<br><sub>11,17,-,-,10</sub> | 3.5<br><sub>0,6,-,-,8</sub> |  | 4.0<br><sub>3,8,-,-,2</sub> |  | 0.7<br><sub>0,1,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.4 | 0.5 | 8.1 |
| Malik Dia | 52% | 6.3<br><sub>-,4,-,5,-</sub> | 2.6<br><sub>-,2,-,2,-</sub> |  | 0.8<br><sub>-,0,-,1,-</sub> |  | 0.9<br><sub>-,1,-,1,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| AJ Johnson | 52% | 6.3<br><sub>7,4,-,6,-</sub> | 2.4<br><sub>2,1,-,0,-</sub> |  | 0.9<br><sub>1,0,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Julian Reese | 52% | 6.1<br><sub>7,4,-,5,-</sub> | 2.3<br><sub>2,0,-,0,-</sub> |  | 1.3<br><sub>2,2,-,1,-</sub> |  | 0.3<br><sub>1,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.9 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 98% | 33.1<br><sub>-,23,32,36,32</sub> | 14.2<br><sub>-,7,6,12,15</sub> |  | 4.4<br><sub>-,2,6,5,4</sub> |  | 3.3<br><sub>-,2,1,4,4</sub> |  | 2.1<br><sub>-,0,0,2,1</sub> |  | 1.4 | 0.5 | 1.1 | 21.8 |
| Victor Wembanyama | 99% | 32.6<br><sub>32,21,35,34,33</sub> | 30.7<br><sub>32,12,26,25,32</sub> |  | 13.3<br><sub>9,12,10,18,11</sub> |  | 3.9<br><sub>1,6,6,4,3</sub> |  | 2.2<br><sub>2,0,4,1,2</sub> |  | 1.2 | 4.3 | 2.4 | 47.8 |
| De'Aaron Fox | 99% | 32.1<br><sub>31,17,-,34,32</sub> | 16.6<br><sub>17,7,-,6,10</sub> |  | 4.0<br><sub>4,5,-,2,2</sub> |  | 6.5<br><sub>9,1,-,2,5</sub> |  | 1.4<br><sub>2,0,-,0,0</sub> |  | 1.4 | 0.4 | 2.3 | 27.1 |
| Stephon Castle | 99% | 31.9<br><sub>29,25,35,31,33</sub> | 18.7<br><sub>11,32,20,10,21</sub> |  | 5.2<br><sub>1,5,4,2,6</sub> |  | 7.3<br><sub>3,6,9,7,12</sub> |  | 1.8<br><sub>1,5,0,2,2</sub> |  | 1.1 | 0.3 | 3.0 | 31.1 |
| Julian Champagnie | 99% | 29.1<br><sub>35,23,24,30,29</sub> | 11.5<br><sub>12,7,4,14,20</sub> |  | 5.4<br><sub>0,8,5,6,4</sub> |  | 1.7<br><sub>2,3,1,0,1</sub> |  | 2.2<br><sub>3,1,1,4,4</sub> |  | 0.9 | 0.6 | 0.8 | 18.6 |
| Keldon Johnson | 99% | 25.6<br><sub>28,25,29,15,27</sub> | 11.2<br><sub>10,18,11,4,10</sub> |  | 5.7<br><sub>6,4,10,2,5</sub> |  | 2.3<br><sub>4,4,2,1,3</sub> |  | 0.7<br><sub>0,2,1,0,0</sub> |  | 0.8 | 0.2 | 1.1 | 19.2 |
| Luke Kornet | 99% | 16.3<br><sub>14,16,13,14,15</sub> | 4.3<br><sub>7,6,2,2,4</sub> |  | 4.8<br><sub>5,7,2,1,0</sub> |  | 1.4<br><sub>1,2,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.5 | 10.5 |
| Harrison Barnes | 91% | 16.3<br><sub>13,21,14,10,16</sub> | 5.9<br><sub>3,11,0,0,9</sub> |  | 1.9<br><sub>1,1,0,3,2</sub> |  | 1.0<br><sub>0,1,2,4,1</sub> |  | 0.8<br><sub>1,3,0,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 8.8 |
| Jordan McLaughlin | 71% | 14.3<br><sub>2,14,19,-,11</sub> | 4.7<br><sub>4,4,10,-,0</sub> |  | 1.9<br><sub>0,6,1,-,1</sub> |  | 2.5<br><sub>0,2,2,-,5</sub> |  | 0.5<br><sub>0,0,2,-,0</sub> |  | 1.0 | 0.1 | 0.7 | 9.1 |
| Carter Bryant | 93% | 13.1<br><sub>15,19,5,2,13</sub> | 4.8<br><sub>10,8,0,0,3</sub> |  | 2.2<br><sub>1,3,1,0,1</sub> |  | 0.9<br><sub>2,2,0,0,0</sub> |  | 0.7<br><sub>2,2,0,0,1</sub> |  | 0.3 | 0.3 | 0.5 | 7.9 |
| Tarris Reed Jr. | 52% | 8.7<br><sub>2,11,-,-,-</sub> | 3.1<br><sub>0,2,-,-,-</sub> |  | 3.5<br><sub>0,4,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.5 | 7.1 |
| David Jones Garcia | 52% | 6.9<br><sub>2,-,-,-,-</sub> | 2.8<br><sub>0,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.1 |

</details>


### BOS @ SAC
Out: Precious Achiuwa (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.6–104.5 | BOS 80% | 1.25 / 5.05 | SAC +12.5 | 221.5 | SAC +12.5 covers 51%; o217.5 57% |
| Expected (weighted by chance each plays) | 118.1–105.1 | BOS 81% | 1.23 / 5.36 | SAC +12.5 | 223.5 | SAC +12.5 covers 49%; o217.5 62% |
| if Derrick White plays | 118.0–104.8 | BOS 82% | 1.22 / 5.64 | SAC +13.5 | 222.5 | SAC +12.5 covers 48%; o217.5 61% |
| if Jayson Tatum plays | 118.2–105.0 | BOS 82% | 1.22 / 5.63 | SAC +13.5 | 223.5 | SAC +12.5 covers 48%; o217.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White (BOS) | Questionable | 55% | 31.8 | 16.4 | 3.7 | 5.2 | 2.3 | 1.1 | 0.8 | 1.6 | 25.3 | full tables below |
| Jayson Tatum (BOS) | Questionable | 55% | 34.9 | 27.8 | 8.2 | 6.7 | 3.2 | 1.2 | 0.5 | 2.9 | 42.7 | full tables below |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George | 98% | 31.6<br><sub>30,-,25,36,23</sub> | 22.5<br><sub>36,-,7,22,10</sub> |  | 5.1<br><sub>5,-,7,8,4</sub> |  | 4.6<br><sub>1,-,6,3,1</sub> |  | 3.1<br><sub>6,-,1,5,1</sub> |  | 1.8 | 0.3 | 2.5 | 32.2 |
| Payton Pritchard | 99% | 30.3<br><sub>30,31,19,32,30</sub> | 18.6<br><sub>18,14,10,21,15</sub> |  | 3.4<br><sub>6,1,1,4,1</sub> |  | 5.5<br><sub>5,1,6,5,2</sub> |  | 2.6<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.5 | 27.5 |
| Neemias Queta | 98% | 26.1<br><sub>22,31,15,-,27</sub> | 12.4<br><sub>4,11,8,-,17</sub> |  | 9.1<br><sub>6,13,6,-,10</sub> |  | 2.4<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.1 | 1.4 | 23.8 |
| Sam Hauser | 99% | 25.5<br><sub>18,24,11,25,17</sub> | 11.0<br><sub>12,8,8,12,9</sub> |  | 3.7<br><sub>5,9,1,1,2</sub> |  | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.2<br><sub>4,2,2,4,3</sub> |  | 0.6 | 0.2 | 0.5 | 16.3 |
| Baylor Scheierman | 99% | 23.0<br><sub>18,29,18,11,13</sub> | 7.8<br><sub>5,9,12,0,0</sub> |  | 4.2<br><sub>3,7,5,1,1</sub> |  | 2.2<br><sub>2,3,3,1,1</sub> |  | 1.3<br><sub>1,3,2,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 14.2 |
| Mitchell Robinson | 98% | 19.8<br><sub>17,11,15,18,16</sub> | 6.6<br><sub>2,2,0,4,6</sub> |  | 7.6<br><sub>6,2,7,5,4</sub> |  | 1.0<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.9 | 0.9 | 15.3 |
| Jordan Walsh | 98% | 19.5<br><sub>19,18,21,17,4</sub> | 6.7<br><sub>8,6,11,6,0</sub> |  | 3.6<br><sub>2,3,1,2,0</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 0.8<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.3 | 0.6 | 11.3 |
| Hugo Gonzalez | 98% | 18.8<br><sub>19,8,18,4,16</sub> | 6.3<br><sub>10,0,9,0,2</sub> |  | 3.8<br><sub>2,1,5,2,6</sub> |  | 1.1<br><sub>2,0,2,0,0</sub> |  | 0.7<br><sub>2,0,2,0,0</sub> |  | 0.8 | 0.3 | 0.7 | 11.2 |
| Devin Carter | 91% | 18.2<br><sub>-,-,12,-,-</sub> | 8.9<br><sub>-,-,0,-,-</sub> |  | 3.3<br><sub>-,-,2,-,-</sub> |  | 2.8<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.0 | 0.2 | 1.3 | 15.0 |
| Chris Cenac Jr. | 63% | 16.8<br><sub>-,-,7,12,17</sub> | 6.7<br><sub>-,-,6,4,6</sub> |  | 4.1<br><sub>-,-,3,2,6</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,0,0,1</sub> |  | 0.7 | 0.3 | 0.8 | 11.6 |
| Luka Garza | 98% | 15.4<br><sub>9,11,14,18,5</sub> | 7.6<br><sub>2,5,2,3,0</sub> |  | 3.6<br><sub>0,1,3,0,1</sub> |  | 1.9<br><sub>2,0,5,4,1</sub> |  | 0.8<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 13.1 |
| Ron Harper Jr. | 52% | 12.8<br><sub>4,-,12,-,-</sub> | 5.5<br><sub>0,-,10,-,-</sub> |  | 1.9<br><sub>1,-,1,-,-</sub> |  | 0.8<br><sub>0,-,0,-,-</sub> |  | 0.8<br><sub>0,-,2,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 8.2 |
| Mike Conley | 35% | 12.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 6.8 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 36.9<br><sub>39,40,35,33,35</sub> | 23.2<br><sub>32,29,17,26,36</sub> |  | 3.8<br><sub>5,4,4,0,4</sub> |  | 7.4<br><sub>10,6,6,6,6</sub> |  | 2.7<br><sub>3,4,3,3,6</sub> |  | 0.9 | 0.3 | 3.9 | 34.4 |
| De'Andre Hunter | 83% | 33.3<br><sub>31,34,42,-,35</sub> | 13.8<br><sub>14,15,24,-,7</sub> |  | 4.7<br><sub>3,4,5,-,1</sub> |  | 2.0<br><sub>1,2,2,-,4</sub> |  | 2.0<br><sub>2,3,2,-,1</sub> |  | 0.6 | 0.2 | 1.6 | 20.6 |
| Zach LaVine | 84% | 32.8<br><sub>25,33,36,-,32</sub> | 17.3<br><sub>15,31,12,-,18</sub> |  | 3.4<br><sub>4,3,3,-,5</sub> |  | 2.9<br><sub>2,2,6,-,2</sub> |  | 2.7<br><sub>1,6,3,-,2</sub> |  | 0.7 | 0.2 | 2.1 | 23.6 |
| Domantas Sabonis | 98% | 31.7<br><sub>-,24,35,29,24</sub> | 13.0<br><sub>-,0,21,11,8</sub> |  | 11.8<br><sub>-,2,12,13,13</sub> |  | 5.5<br><sub>-,5,5,3,8</sub> |  | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.6 | 0.3 | 2.2 | 30.3 |
| Keegan Murray | 98% | 29.8<br><sub>23,24,40,21,31</sub> | 11.6<br><sub>10,11,16,6,12</sub> |  | 4.7<br><sub>1,2,7,1,7</sub> |  | 1.6<br><sub>2,1,4,0,3</sub> |  | 1.6<br><sub>0,2,2,2,0</sub> |  | 0.7 | 0.9 | 1.0 | 17.9 |
| Leaky Black | 88% | 19.6<br><sub>20,18,12,29,17</sub> | 5.0<br><sub>6,0,0,12,3</sub> |  | 3.2<br><sub>5,3,0,9,0</sub> |  | 1.3<br><sub>1,2,0,2,2</sub> |  | 0.8<br><sub>2,0,0,4,1</sub> |  | 0.8 | 0.5 | 0.5 | 9.5 |
| Malik Monk | 98% | 19.4<br><sub>21,3,18,29,20</sub> | 10.1<br><sub>9,1,7,14,8</sub> |  | 1.8<br><sub>2,0,4,1,1</sub> |  | 3.5<br><sub>3,0,3,10,2</sub> |  | 1.3<br><sub>0,0,0,1,2</sub> |  | 0.5 | 0.3 | 1.4 | 15.4 |
| Dylan Cardwell | 98% | 15.5<br><sub>18,29,13,19,12</sub> | 4.6<br><sub>4,1,6,10,6</sub> |  | 5.2<br><sub>9,11,3,6,4</sub> |  | 1.2<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.7 | 11.1 |
| Emanuel Sharp | 98% | 15.2<br><sub>12,19,7,21,14</sub> | 4.8<br><sub>5,2,4,9,6</sub> |  | 1.3<br><sub>1,2,0,0,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.6 | 6.9 |
| Alex Karaban | 58% | 11.3<br><sub>-,-,-,29,4</sub> | 2.2<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,5,1</sub> |  | 0.5<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.4 |
| Daeqwon Plowden | 88% | 10.9<br><sub>12,2,2,24,4</sub> | 3.9<br><sub>6,0,0,13,3</sub> |  | 1.3<br><sub>0,0,0,2,0</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>2,0,0,3,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| Sean Pedulla | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jonathan Mogbo | 52% | 8.4<br><sub>2,-,-,-,-</sub> | 2.5<br><sub>0,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Mason Plumlee | 63% | 6.8<br><sub>-,-,-,5,4</sub> | 1.8<br><sub>-,-,-,2,0</sub> |  | 2.2<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 4.5 |

</details>

<details><summary>if Jayson Tatum plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 100% | 34.9<br><sub>32,38,30,36,37</sub> | 27.8<br><sub>21,24,32,24,24</sub> |  | 8.2<br><sub>6,7,6,12,8</sub> |  | 6.7<br><sub>4,8,6,4,3</sub> |  | 3.2<br><sub>3,2,5,3,3</sub> |  | 1.2 | 0.5 | 2.9 | 42.7 |
| Paul George (BOS) | 98% | 30.5<br><sub>30,-,25,36,23</sub> | 19.1<br><sub>36,-,7,22,10</sub> |  | 4.8<br><sub>5,-,7,8,4</sub> |  | 3.7<br><sub>1,-,6,3,1</sub> |  | 2.8<br><sub>6,-,1,5,1</sub> |  | 1.7 | 0.4 | 2.0 | 27.6 |
| Payton Pritchard (BOS) | 99% | 29.0<br><sub>30,31,19,32,30</sub> | 15.3<br><sub>18,14,10,21,15</sub> |  | 3.2<br><sub>6,1,1,4,1</sub> |  | 4.5<br><sub>5,1,6,5,2</sub> |  | 2.4<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.2 | 23.0 |
| Neemias Queta (BOS) | 98% | 25.6<br><sub>22,31,15,-,27</sub> | 11.1<br><sub>4,11,8,-,17</sub> |  | 8.8<br><sub>6,13,6,-,10</sub> |  | 2.0<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.2 | 1.2 | 22.0 |
| Sam Hauser (BOS) | 99% | 20.9<br><sub>18,24,11,25,17</sub> | 8.1<br><sub>12,8,8,12,9</sub> |  | 3.0<br><sub>5,9,1,1,2</sub> |  | 1.2<br><sub>2,0,0,2,2</sub> |  | 1.5<br><sub>4,2,2,4,3</sub> |  | 0.5 | 0.2 | 0.4 | 12.3 |
| Baylor Scheierman (BOS) | 99% | 18.9<br><sub>18,29,18,11,13</sub> | 5.8<br><sub>5,9,12,0,0</sub> |  | 3.3<br><sub>3,7,5,1,1</sub> |  | 1.6<br><sub>2,3,3,1,1</sub> |  | 0.9<br><sub>1,3,2,0,0</sub> |  | 0.9 | 0.1 | 0.6 | 10.8 |
| Mitchell Robinson (BOS) | 98% | 16.6<br><sub>17,11,15,18,16</sub> | 5.2<br><sub>2,2,0,4,6</sub> |  | 6.3<br><sub>6,2,7,5,4</sub> |  | 0.8<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 0.7 | 12.2 |
| Jordan Walsh (BOS) | 98% | 15.2<br><sub>19,18,21,17,4</sub> | 4.6<br><sub>8,6,11,6,0</sub> |  | 2.7<br><sub>2,3,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,2,2,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.1 |
| Hugo Gonzalez (BOS) | 98% | 15.1<br><sub>19,8,18,4,16</sub> | 4.5<br><sub>10,0,9,0,2</sub> |  | 3.0<br><sub>2,1,5,2,6</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.5<br><sub>2,0,2,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 8.4 |
| Devin Carter (BOS) | 91% | 15.0<br><sub>-,-,12,-,-</sub> | 6.4<br><sub>-,-,0,-,-</sub> |  | 2.6<br><sub>-,-,2,-,-</sub> |  | 2.0<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.8 | 0.2 | 1.1 | 11.0 |
| Luka Garza (BOS) | 98% | 12.9<br><sub>9,11,14,18,5</sub> | 6.1<br><sub>2,5,2,3,0</sub> |  | 3.0<br><sub>0,1,3,0,1</sub> |  | 1.4<br><sub>2,0,5,4,1</sub> |  | 0.6<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 10.4 |
| Chris Cenac Jr. (BOS) | 63% | 11.6<br><sub>-,-,7,12,17</sub> | 4.8<br><sub>-,-,6,4,6</sub> |  | 3.0<br><sub>-,-,3,2,6</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |
| Mike Conley (BOS) | 35% | 9.5<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |
| Ron Harper Jr. (BOS) | 52% | 8.7<br><sub>4,-,12,-,-</sub> | 3.8<br><sub>0,-,10,-,-</sub> |  | 1.2<br><sub>1,-,1,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>0,-,2,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 5.6 |
| Darius Acuff Jr. (SAC) | 98% | 36.9<br><sub>39,40,35,33,35</sub> | 23.4<br><sub>32,29,17,26,36</sub> |  | 3.8<br><sub>5,4,4,0,4</sub> |  | 7.3<br><sub>10,6,6,6,6</sub> |  | 2.8<br><sub>3,4,3,3,6</sub> |  | 0.9 | 0.4 | 3.9 | 34.5 |
| De'Andre Hunter (SAC) | 83% | 33.3<br><sub>31,34,42,-,35</sub> | 13.9<br><sub>14,15,24,-,7</sub> |  | 4.7<br><sub>3,4,5,-,1</sub> |  | 2.0<br><sub>1,2,2,-,4</sub> |  | 2.0<br><sub>2,3,2,-,1</sub> |  | 0.6 | 0.2 | 1.6 | 20.6 |
| Zach LaVine (SAC) | 84% | 32.8<br><sub>25,33,36,-,32</sub> | 17.3<br><sub>15,31,12,-,18</sub> |  | 3.4<br><sub>4,3,3,-,5</sub> |  | 2.9<br><sub>2,2,6,-,2</sub> |  | 2.7<br><sub>1,6,3,-,2</sub> |  | 0.7 | 0.2 | 2.1 | 23.6 |
| Domantas Sabonis (SAC) | 98% | 31.6<br><sub>-,24,35,29,24</sub> | 13.0<br><sub>-,0,21,11,8</sub> |  | 11.8<br><sub>-,2,12,13,13</sub> |  | 5.5<br><sub>-,5,5,3,8</sub> |  | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.6 | 0.3 | 2.2 | 30.3 |
| Keegan Murray (SAC) | 98% | 29.7<br><sub>23,24,40,21,31</sub> | 11.7<br><sub>10,11,16,6,12</sub> |  | 4.7<br><sub>1,2,7,1,7</sub> |  | 1.6<br><sub>2,1,4,0,3</sub> |  | 1.6<br><sub>0,2,2,2,0</sub> |  | 0.7 | 0.9 | 1.0 | 17.9 |
| Leaky Black (SAC) | 88% | 19.6<br><sub>20,18,12,29,17</sub> | 5.0<br><sub>6,0,0,12,3</sub> |  | 3.2<br><sub>5,3,0,9,0</sub> |  | 1.3<br><sub>1,2,0,2,2</sub> |  | 0.8<br><sub>2,0,0,4,1</sub> |  | 0.8 | 0.5 | 0.5 | 9.5 |
| Malik Monk (SAC) | 98% | 19.4<br><sub>21,3,18,29,20</sub> | 10.0<br><sub>9,1,7,14,8</sub> |  | 1.8<br><sub>2,0,4,1,1</sub> |  | 3.5<br><sub>3,0,3,10,2</sub> |  | 1.3<br><sub>0,0,0,1,2</sub> |  | 0.5 | 0.3 | 1.4 | 15.4 |
| Dylan Cardwell (SAC) | 98% | 15.5<br><sub>18,29,13,19,12</sub> | 4.7<br><sub>4,1,6,10,6</sub> |  | 5.2<br><sub>9,11,3,6,4</sub> |  | 1.2<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.7 | 11.1 |
| Emanuel Sharp (SAC) | 98% | 15.2<br><sub>12,19,7,21,14</sub> | 4.8<br><sub>5,2,4,9,6</sub> |  | 1.3<br><sub>1,2,0,0,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.6 | 7.0 |
| Alex Karaban (SAC) | 58% | 11.4<br><sub>-,-,-,29,4</sub> | 2.2<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,5,1</sub> |  | 0.5<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.4 |
| Daeqwon Plowden (SAC) | 88% | 10.8<br><sub>12,2,2,24,4</sub> | 3.9<br><sub>6,0,0,13,3</sub> |  | 1.3<br><sub>0,0,0,2,0</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>2,0,0,3,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| Sean Pedulla (SAC) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Jonathan Mogbo (SAC) | 52% | 8.5<br><sub>2,-,-,-,-</sub> | 2.5<br><sub>0,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Mason Plumlee (SAC) | 63% | 6.9<br><sub>-,-,-,5,4</sub> | 1.8<br><sub>-,-,-,2,0</sub> |  | 2.2<br><sub>-,-,-,0,2</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 4.5 |

</details>

<details><summary>if Derrick White plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White (BOS) | 100% | 31.8<br><sub>22,38,23,32,35</sub> | 16.4<br><sub>5,19,16,9,12</sub> |  | 3.7<br><sub>1,1,4,3,3</sub> |  | 5.2<br><sub>3,7,2,2,8</sub> |  | 2.3<br><sub>1,3,4,1,0</sub> |  | 1.1 | 0.8 | 1.6 | 25.3 |
| Paul George (BOS) | 98% | 30.8<br><sub>30,-,25,36,23</sub> | 21.0<br><sub>36,-,7,22,10</sub> |  | 5.0<br><sub>5,-,7,8,4</sub> |  | 3.8<br><sub>1,-,6,3,1</sub> |  | 3.0<br><sub>6,-,1,5,1</sub> |  | 1.8 | 0.3 | 2.2 | 29.8 |
| Payton Pritchard (BOS) | 99% | 28.9<br><sub>30,31,19,32,30</sub> | 17.2<br><sub>18,14,10,21,15</sub> |  | 3.3<br><sub>6,1,1,4,1</sub> |  | 4.7<br><sub>5,1,6,5,2</sub> |  | 2.5<br><sub>4,2,2,4,3</sub> |  | 0.8 | 0.1 | 1.3 | 25.2 |
| Neemias Queta (BOS) | 98% | 25.5<br><sub>22,31,15,-,27</sub> | 12.3<br><sub>4,11,8,-,17</sub> |  | 8.8<br><sub>6,13,6,-,10</sub> |  | 2.1<br><sub>3,3,2,-,3</sub> |  | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.7 | 1.1 | 1.3 | 23.3 |
| Sam Hauser (BOS) | 99% | 22.9<br><sub>18,24,11,25,17</sub> | 9.5<br><sub>12,8,8,12,9</sub> |  | 3.3<br><sub>5,9,1,1,2</sub> |  | 1.4<br><sub>2,0,0,2,2</sub> |  | 1.8<br><sub>4,2,2,4,3</sub> |  | 0.6 | 0.2 | 0.5 | 14.2 |
| Baylor Scheierman (BOS) | 99% | 18.0<br><sub>18,29,18,11,13</sub> | 6.2<br><sub>5,9,12,0,0</sub> |  | 3.2<br><sub>3,7,5,1,1</sub> |  | 1.6<br><sub>2,3,3,1,1</sub> |  | 0.9<br><sub>1,3,2,0,0</sub> |  | 0.9 | 0.1 | 0.6 | 11.0 |
| Mitchell Robinson (BOS) | 98% | 16.9<br><sub>17,11,15,18,16</sub> | 5.5<br><sub>2,2,0,4,6</sub> |  | 6.4<br><sub>6,2,7,5,4</sub> |  | 0.8<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 0.8 | 12.7 |
| Devin Carter (BOS) | 91% | 15.0<br><sub>-,-,12,-,-</sub> | 7.2<br><sub>-,-,0,-,-</sub> |  | 2.7<br><sub>-,-,2,-,-</sub> |  | 2.1<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.8 | 0.2 | 1.2 | 11.9 |
| Jordan Walsh (BOS) | 98% | 14.7<br><sub>19,18,21,17,4</sub> | 4.7<br><sub>8,6,11,6,0</sub> |  | 2.7<br><sub>2,3,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,2,2,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.2 |
| Chris Cenac Jr. (BOS) | 63% | 14.3<br><sub>-,-,7,12,17</sub> | 5.8<br><sub>-,-,6,4,6</sub> |  | 3.6<br><sub>-,-,3,2,6</sub> |  | 0.7<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.2 | 0.8 | 10.2 |
| Hugo Gonzalez (BOS) | 98% | 13.9<br><sub>19,8,18,4,16</sub> | 4.5<br><sub>10,0,9,0,2</sub> |  | 2.9<br><sub>2,1,5,2,6</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.4<br><sub>2,0,2,0,0</sub> |  | 0.6 | 0.3 | 0.5 | 8.1 |
| Luka Garza (BOS) | 98% | 13.4<br><sub>9,11,14,18,5</sub> | 6.8<br><sub>2,5,2,3,0</sub> |  | 3.1<br><sub>0,1,3,0,1</sub> |  | 1.5<br><sub>2,0,5,4,1</sub> |  | 0.7<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 11.3 |
| Mike Conley (BOS) | 35% | 9.0<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |
| Ron Harper Jr. (BOS) | 52% | 8.4<br><sub>4,-,12,-,-</sub> | 3.8<br><sub>0,-,10,-,-</sub> |  | 1.2<br><sub>1,-,1,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>0,-,2,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.7 |
| Darius Acuff Jr. (SAC) | 98% | 36.8<br><sub>39,40,35,33,35</sub> | 23.2<br><sub>32,29,17,26,36</sub> |  | 3.8<br><sub>5,4,4,0,4</sub> |  | 7.3<br><sub>10,6,6,6,6</sub> |  | 2.8<br><sub>3,4,3,3,6</sub> |  | 0.9 | 0.4 | 3.9 | 34.3 |
| De'Andre Hunter (SAC) | 83% | 33.3<br><sub>31,34,42,-,35</sub> | 13.8<br><sub>14,15,24,-,7</sub> |  | 4.7<br><sub>3,4,5,-,1</sub> |  | 2.0<br><sub>1,2,2,-,4</sub> |  | 2.0<br><sub>2,3,2,-,1</sub> |  | 0.6 | 0.2 | 1.6 | 20.4 |
| Zach LaVine (SAC) | 84% | 32.8<br><sub>25,33,36,-,32</sub> | 17.3<br><sub>15,31,12,-,18</sub> |  | 3.4<br><sub>4,3,3,-,5</sub> |  | 2.9<br><sub>2,2,6,-,2</sub> |  | 2.7<br><sub>1,6,3,-,2</sub> |  | 0.7 | 0.2 | 2.1 | 23.6 |
| Domantas Sabonis (SAC) | 98% | 31.6<br><sub>-,24,35,29,24</sub> | 13.0<br><sub>-,0,21,11,8</sub> |  | 11.8<br><sub>-,2,12,13,13</sub> |  | 5.5<br><sub>-,5,5,3,8</sub> |  | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.6 | 0.3 | 2.2 | 30.3 |
| Keegan Murray (SAC) | 98% | 29.8<br><sub>23,24,40,21,31</sub> | 11.7<br><sub>10,11,16,6,12</sub> |  | 4.7<br><sub>1,2,7,1,7</sub> |  | 1.6<br><sub>2,1,4,0,3</sub> |  | 1.6<br><sub>0,2,2,2,0</sub> |  | 0.7 | 0.9 | 1.0 | 17.9 |
| Leaky Black (SAC) | 88% | 19.6<br><sub>20,18,12,29,17</sub> | 5.0<br><sub>6,0,0,12,3</sub> |  | 3.2<br><sub>5,3,0,9,0</sub> |  | 1.3<br><sub>1,2,0,2,2</sub> |  | 0.8<br><sub>2,0,0,4,1</sub> |  | 0.8 | 0.5 | 0.5 | 9.5 |
| Malik Monk (SAC) | 98% | 19.3<br><sub>21,3,18,29,20</sub> | 10.1<br><sub>9,1,7,14,8</sub> |  | 1.8<br><sub>2,0,4,1,1</sub> |  | 3.5<br><sub>3,0,3,10,2</sub> |  | 1.4<br><sub>0,0,0,1,2</sub> |  | 0.5 | 0.3 | 1.4 | 15.4 |
| Dylan Cardwell (SAC) | 98% | 15.5<br><sub>18,29,13,19,12</sub> | 4.7<br><sub>4,1,6,10,6</sub> |  | 5.2<br><sub>9,11,3,6,4</sub> |  | 1.2<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.7 | 11.1 |
| Emanuel Sharp (SAC) | 98% | 15.2<br><sub>12,19,7,21,14</sub> | 4.8<br><sub>5,2,4,9,6</sub> |  | 1.3<br><sub>1,2,0,0,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.6 | 6.9 |
| Alex Karaban (SAC) | 58% | 11.4<br><sub>-,-,-,29,4</sub> | 2.2<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,5,1</sub> |  | 0.5<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.5 |
| Daeqwon Plowden (SAC) | 88% | 10.9<br><sub>12,2,2,24,4</sub> | 3.9<br><sub>6,0,0,13,3</sub> |  | 1.3<br><sub>0,0,0,2,0</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>2,0,0,3,1</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| Sean Pedulla (SAC) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Jonathan Mogbo (SAC) | 52% | 8.4<br><sub>2,-,-,-,-</sub> | 2.5<br><sub>0,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Mason Plumlee (SAC) | 63% | 6.9<br><sub>-,-,-,5,4</sub> | 1.8<br><sub>-,-,-,2,0</sub> |  | 2.2<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 4.5 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-21/`._
