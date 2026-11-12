# NBA model · Thu 12 Nov 2026 (US date)

Updated **Thu 12 Nov, 04:43 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-12/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

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
| TOR @ PHI | Fri 13 Nov 11:00 | 111.8–109.8 | TOR 56% | 1.80 / 2.25 | PHI +2.5 | 221.5 | PHI -9.5 covers 21%; o221.5 50% |
| DET @ WAS | Fri 13 Nov 11:00 | 119.4–109.8 | DET 76% | 1.32 / 4.09 | WAS +9.5 | 229.5 | WAS +9.5 covers 50%; o220.5 68% |
| DAL @ MIN | Fri 13 Nov 12:00 | 112.5–117.3 | DAL 36% | 2.75 / 1.57 | MIN -4.5 | 229.5 | MIN -5.5 covers 48%; o227.5 55% |
| CHA @ PHX | Fri 13 Nov 13:00 | 108.1–111.6 | CHA 40% | 2.49 / 1.67 | PHX -3.5 | 219.5 | PHX -7.5 covers 39%; o213.5 62% |

### TOR @ PHI
Out: Dominick Barlow (PHI), Adem Bona (PHI), Ariel Hukporti (PHI), Scottie Barnes (TOR), Kawhi Leonard (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.8–109.8 | TOR 56% | 1.80 / 2.25 | PHI +2.5 | 221.5 | PHI -9.5 covers 21%; o221.5 50% |
| Expected (weighted by chance each plays) | 111.8–111.9 | TOR 50% | 2.01 / 1.99 | PHI +0.5 | 223.5 | PHI -9.5 covers 26%; o221.5 54% |
| if LeBron James plays | 112.4–112.2 | TOR 51% | 1.98 / 2.03 | PHI +0.5 | 224.5 | PHI -9.5 covers 25%; o221.5 56% |
| if Joel Embiid plays | 112.5–112.3 | TOR 51% | 1.98 / 2.03 | PHI +0.5 | 224.5 | PHI -9.5 covers 25%; o221.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| LeBron James (PHI) | Questionable | 55% | 35.3 | 19.5 | 6.9 | 6.7 | 1.4 | 1.2 | 0.7 | 3.5 | 33.2 | full tables below |
| Joel Embiid (PHI) | Questionable | 55% | 34.3 | 22.9 | 8.8 | 4.6 | 1.0 | 0.8 | 1.0 | 3.1 | 36.3 | full tables below |
| Trayce Jackson-Davis (TOR) | Day-To-Day | 70% | 12.6 | 4.7 | 4.1 | 0.8 | 0.0 | 0.6 | 0.7 | 0.7 | 9.6 | small |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 35.8<br><sub>32,37,33,37,36</sub> | 24.6<br><sub>22,26,22,27,19</sub> |  | 6.7<br><sub>10,6,5,7,3</sub> |  | 4.5<br><sub>5,3,3,5,2</sub> |  | 2.0<br><sub>4,2,3,0,1</sub> |  | 0.8 | 0.5 | 2.8 | 35.9 |
| Immanuel Quickley | 72% | 32.1<br><sub>33,38,32,-,-</sub> | 17.0<br><sub>12,27,13,-,-</sub> |  | 4.0<br><sub>6,4,1,-,-</sub> |  | 6.4<br><sub>7,2,7,-,-</sub> |  | 2.5<br><sub>3,1,2,-,-</sub> |  | 1.2 | 0.1 | 1.8 | 27.4 |
| Ja'Kobe Walter | 98% | 31.7<br><sub>33,35,27,29,34</sub> | 12.5<br><sub>11,10,8,7,12</sub> |  | 4.2<br><sub>4,6,1,6,6</sub> |  | 2.2<br><sub>2,5,2,2,0</sub> |  | 2.1<br><sub>3,0,1,1,2</sub> |  | 1.3 | 0.3 | 1.1 | 18.9 |
| Jamal Shead | 98% | 30.3<br><sub>25,20,20,34,36</sub> | 10.2<br><sub>9,6,3,10,20</sub> |  | 2.5<br><sub>2,1,3,3,2</sub> |  | 7.8<br><sub>6,6,6,16,11</sub> |  | 1.4<br><sub>2,0,1,1,4</sub> |  | 1.2 | 0.2 | 2.4 | 20.5 |
| Collin Murray-Boyles | 98% | 28.5<br><sub>20,28,23,34,-</sub> | 13.5<br><sub>4,18,13,19,-</sub> |  | 6.7<br><sub>3,7,3,7,-</sub> |  | 2.4<br><sub>1,0,2,2,-</sub> |  | 0.5<br><sub>0,1,1,0,-</sub> |  | 1.1 | 1.1 | 1.8 | 22.6 |
| Jakob Poeltl | 88% | 26.5<br><sub>-,-,19,31,31</sub> | 10.8<br><sub>-,-,8,19,18</sub> |  | 8.1<br><sub>-,-,5,11,8</sub> |  | 2.2<br><sub>-,-,1,1,2</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.9 | 1.1 | 1.5 | 21.1 |
| Jamison Battle | 98% | 25.7<br><sub>17,21,19,21,29</sub> | 11.5<br><sub>20,12,9,6,18</sub> |  | 3.6<br><sub>5,0,1,2,1</sub> |  | 1.2<br><sub>0,0,0,0,2</sub> |  | 2.0<br><sub>4,4,2,1,5</sub> |  | 0.5 | 0.2 | 0.9 | 16.3 |
| Alijah Martin | 91% | 17.3<br><sub>16,6,9,31,21</sub> | 7.2<br><sub>5,2,6,27,2</sub> |  | 2.5<br><sub>2,2,1,4,3</sub> |  | 1.6<br><sub>4,0,0,1,3</sub> |  | 0.8<br><sub>1,0,0,6,0</sub> |  | 0.7 | 0.3 | 1.3 | 11.3 |
| Allen Graves | 98% | 16.5<br><sub>10,7,14,16,13</sub> | 5.4<br><sub>3,0,5,3,3</sub> |  | 2.9<br><sub>0,0,1,2,2</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.5 | 9.4 |
| Kyle Anderson | 67% | 15.1<br><sub>4,8,4,-,16</sub> | 4.3<br><sub>2,2,2,-,6</sub> |  | 2.9<br><sub>3,0,0,-,2</sub> |  | 2.6<br><sub>3,0,1,-,2</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.5 | 0.8 | 9.7 |
| Malachi Smith | 91% | 12.2<br><sub>-,-,-,-,1</sub> | 4.1<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.6 |
| Jaden Bradley | 80% | 9.2<br><sub>4,-,4,8,9</sub> | 3.1<br><sub>3,-,2,3,0</sub> |  | 1.4<br><sub>1,-,1,0,1</sub> |  | 1.6<br><sub>2,-,0,1,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 6.1 |
| Kevin McCullar Jr. | 16% | 8.8<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.8<br><sub>36,34,32,36,34</sub> | 28.8<br><sub>26,19,17,27,24</sub> |  | 4.2<br><sub>4,1,3,4,1</sub> |  | 7.1<br><sub>11,7,4,7,4</sub> |  | 2.8<br><sub>1,3,2,3,3</sub> |  | 1.5 | 0.6 | 3.4 | 40.0 |
| Jaylen Brown | 98% | 36.8<br><sub>33,37,34,35,26</sub> | 27.1<br><sub>25,30,20,29,13</sub> |  | 7.0<br><sub>11,7,5,7,5</sub> |  | 5.4<br><sub>5,1,5,4,2</sub> |  | 2.0<br><sub>4,3,2,2,1</sub> |  | 1.2 | 0.5 | 4.2 | 39.5 |
| VJ Edgecombe | 93% | 36.6<br><sub>33,35,32,35,32</sub> | 17.4<br><sub>21,11,19,13,8</sub> |  | 6.4<br><sub>3,6,3,6,4</sub> |  | 4.5<br><sub>5,3,2,3,5</sub> |  | 2.1<br><sub>2,1,3,3,0</sub> |  | 1.4 | 0.5 | 2.2 | 28.3 |
| Dean Wade | 96% | 27.9<br><sub>23,22,21,18,23</sub> | 4.8<br><sub>8,3,0,0,8</sub> |  | 4.6<br><sub>2,5,5,1,9</sub> |  | 1.7<br><sub>1,1,1,1,0</sub> |  | 0.7<br><sub>2,0,0,0,2</sub> |  | 1.0 | 0.3 | 0.7 | 11.1 |
| Anfernee Simons | 98% | 26.1<br><sub>24,10,19,16,18</sub> | 12.9<br><sub>6,0,6,3,17</sub> |  | 2.7<br><sub>2,1,2,4,3</sub> |  | 2.2<br><sub>1,0,2,2,0</sub> |  | 2.2<br><sub>1,0,1,1,3</sub> |  | 0.7 | 0.2 | 1.3 | 17.8 |
| Kentavious Caldwell-Pope | 98% | 24.4<br><sub>13,21,17,21,16</sub> | 6.3<br><sub>3,5,5,6,0</sub> |  | 2.7<br><sub>1,1,2,6,0</sub> |  | 2.0<br><sub>0,0,0,3,2</sub> |  | 0.8<br><sub>1,1,1,2,0</sub> |  | 1.0 | 0.3 | 1.0 | 11.0 |
| Jabari Walker | 88% | 20.0<br><sub>2,-,17,19,15</sub> | 7.2<br><sub>0,-,8,9,2</sub> |  | 5.3<br><sub>0,-,5,11,4</sub> |  | 0.9<br><sub>1,-,1,0,0</sub> |  | 0.6<br><sub>0,-,0,1,0</sub> |  | 0.6 | 0.3 | 0.8 | 13.5 |
| Rayan Rupert | 52% | 15.4<br><sub>2,-,-,-,6</sub> | 5.7<br><sub>2,-,-,-,0</sub> |  | 3.0<br><sub>2,-,-,-,1</sub> |  | 1.1<br><sub>0,-,-,-,1</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.8 | 0.2 | 0.9 | 9.8 |
| Justin Edwards | 58% | 14.3<br><sub>2,-,4,-,6</sub> | 5.4<br><sub>2,-,3,-,0</sub> |  | 1.9<br><sub>1,-,1,-,0</sub> |  | 0.9<br><sub>0,-,0,-,0</sub> |  | 0.6<br><sub>0,-,1,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.2 |
| Labaron Philon Jr. | 63% | 13.0<br><sub>2,-,4,-,6</sub> | 5.1<br><sub>0,-,3,-,2</sub> |  | 2.0<br><sub>0,-,1,-,1</sub> |  | 1.5<br><sub>0,-,1,-,3</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.1 | 0.8 | 8.6 |
| Tacko Fall | 58% | 12.5<br><sub>-,-,3,-,-</sub> | 0.7<br><sub>-,-,0,-,-</sub> |  | 3.1<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.7 | 0.6 | 4.3 |
| Caleb Love | 35% | 9.8<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 1.5 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey (PHI) | 98% | 38.4<br><sub>36,34,32,36,34</sub> | 25.0<br><sub>26,19,17,27,24</sub> |  | 3.9<br><sub>4,1,3,4,1</sub> |  | 6.0<br><sub>11,7,4,7,4</sub> |  | 2.7<br><sub>1,3,2,3,3</sub> |  | 1.5 | 0.6 | 2.6 | 34.9 |
| Jaylen Brown (PHI) | 98% | 36.8<br><sub>33,37,34,35,26</sub> | 23.9<br><sub>25,30,20,29,13</sub> |  | 6.5<br><sub>11,7,5,7,5</sub> |  | 4.3<br><sub>5,1,5,4,2</sub> |  | 2.0<br><sub>4,3,2,2,1</sub> |  | 1.2 | 0.5 | 3.4 | 34.8 |
| VJ Edgecombe (PHI) | 93% | 36.0<br><sub>33,35,32,35,32</sub> | 14.0<br><sub>21,11,19,13,8</sub> |  | 5.9<br><sub>3,6,3,6,4</sub> |  | 3.7<br><sub>5,3,2,3,5</sub> |  | 1.9<br><sub>2,1,3,3,0</sub> |  | 1.4 | 0.5 | 1.7 | 23.6 |
| Joel Embiid (PHI) | 100% | 34.3<br><sub>25,33,25,29,31</sub> | 22.9<br><sub>15,26,6,18,16</sub> |  | 8.8<br><sub>8,15,7,10,6</sub> |  | 4.6<br><sub>3,2,1,5,1</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.8 | 1.0 | 3.1 | 36.3 |
| Dean Wade (PHI) | 96% | 26.6<br><sub>23,22,21,18,23</sub> | 5.0<br><sub>8,3,0,0,8</sub> |  | 4.2<br><sub>2,5,5,1,9</sub> |  | 1.4<br><sub>1,1,1,1,0</sub> |  | 0.7<br><sub>2,0,0,0,2</sub> |  | 0.9 | 0.3 | 0.7 | 10.6 |
| Anfernee Simons (PHI) | 98% | 22.1<br><sub>24,10,19,16,18</sub> | 9.5<br><sub>6,0,6,3,17</sub> |  | 2.2<br><sub>2,1,2,4,3</sub> |  | 1.6<br><sub>1,0,2,2,0</sub> |  | 1.7<br><sub>1,0,1,1,3</sub> |  | 0.5 | 0.2 | 1.0 | 13.3 |
| Kentavious Caldwell-Pope (PHI) | 98% | 21.3<br><sub>13,21,17,21,16</sub> | 5.2<br><sub>3,5,5,6,0</sub> |  | 2.3<br><sub>1,1,2,6,0</sub> |  | 1.5<br><sub>0,0,0,3,2</sub> |  | 0.7<br><sub>1,1,1,2,0</sub> |  | 0.8 | 0.3 | 0.8 | 9.0 |
| Jabari Walker (PHI) | 88% | 16.5<br><sub>2,-,17,19,15</sub> | 5.7<br><sub>0,-,8,9,2</sub> |  | 4.3<br><sub>0,-,5,11,4</sub> |  | 0.7<br><sub>1,-,1,0,0</sub> |  | 0.4<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 10.7 |
| Rayan Rupert (PHI) | 52% | 11.6<br><sub>2,-,-,-,6</sub> | 3.9<br><sub>2,-,-,-,0</sub> |  | 2.2<br><sub>2,-,-,-,1</sub> |  | 0.7<br><sub>0,-,-,-,1</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.1 | 0.7 | 6.8 |
| Justin Edwards (PHI) | 58% | 10.2<br><sub>2,-,4,-,6</sub> | 3.7<br><sub>2,-,3,-,0</sub> |  | 1.3<br><sub>1,-,1,-,0</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.3<br><sub>0,-,1,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |
| Labaron Philon Jr. (PHI) | 63% | 8.8<br><sub>2,-,4,-,6</sub> | 3.3<br><sub>0,-,3,-,2</sub> |  | 1.3<br><sub>0,-,1,-,1</sub> |  | 0.9<br><sub>0,-,1,-,3</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.5 |
| Tacko Fall (PHI) | 58% | 8.6<br><sub>-,-,3,-,-</sub> | 0.5<br><sub>-,-,0,-,-</sub> |  | 2.3<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.5 | 0.4 | 3.1 |
| Caleb Love (PHI) | 35% | 8.2<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 1.3 |
| RJ Barrett (TOR) | 98% | 35.9<br><sub>32,37,33,37,36</sub> | 24.9<br><sub>22,26,22,27,19</sub> |  | 6.8<br><sub>10,6,5,7,3</sub> |  | 4.6<br><sub>5,3,3,5,2</sub> |  | 2.0<br><sub>4,2,3,0,1</sub> |  | 0.8 | 0.5 | 2.8 | 36.2 |
| Immanuel Quickley (TOR) | 72% | 32.0<br><sub>33,38,32,-,-</sub> | 17.3<br><sub>12,27,13,-,-</sub> |  | 4.0<br><sub>6,4,1,-,-</sub> |  | 6.4<br><sub>7,2,7,-,-</sub> |  | 2.5<br><sub>3,1,2,-,-</sub> |  | 1.2 | 0.1 | 1.8 | 27.6 |
| Ja'Kobe Walter (TOR) | 98% | 31.6<br><sub>33,35,27,29,34</sub> | 12.5<br><sub>11,10,8,7,12</sub> |  | 4.2<br><sub>4,6,1,6,6</sub> |  | 2.2<br><sub>2,5,2,2,0</sub> |  | 2.0<br><sub>3,0,1,1,2</sub> |  | 1.3 | 0.3 | 1.1 | 18.9 |
| Jamal Shead (TOR) | 98% | 30.3<br><sub>25,20,20,34,36</sub> | 10.2<br><sub>9,6,3,10,20</sub> |  | 2.5<br><sub>2,1,3,3,2</sub> |  | 7.8<br><sub>6,6,6,16,11</sub> |  | 1.4<br><sub>2,0,1,1,4</sub> |  | 1.2 | 0.2 | 2.4 | 20.5 |
| Collin Murray-Boyles (TOR) | 98% | 28.4<br><sub>20,28,23,34,-</sub> | 13.5<br><sub>4,18,13,19,-</sub> |  | 6.7<br><sub>3,7,3,7,-</sub> |  | 2.4<br><sub>1,0,2,2,-</sub> |  | 0.5<br><sub>0,1,1,0,-</sub> |  | 1.1 | 1.1 | 1.8 | 22.6 |
| Jakob Poeltl (TOR) | 88% | 26.4<br><sub>-,-,19,31,31</sub> | 10.8<br><sub>-,-,8,19,18</sub> |  | 8.1<br><sub>-,-,5,11,8</sub> |  | 2.2<br><sub>-,-,1,1,2</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.9 | 1.1 | 1.6 | 21.1 |
| Jamison Battle (TOR) | 98% | 25.7<br><sub>17,21,19,21,29</sub> | 11.5<br><sub>20,12,9,6,18</sub> |  | 3.5<br><sub>5,0,1,2,1</sub> |  | 1.2<br><sub>0,0,0,0,2</sub> |  | 2.0<br><sub>4,4,2,1,5</sub> |  | 0.4 | 0.2 | 0.9 | 16.2 |
| Alijah Martin (TOR) | 91% | 17.3<br><sub>16,6,9,31,21</sub> | 7.2<br><sub>5,2,6,27,2</sub> |  | 2.5<br><sub>2,2,1,4,3</sub> |  | 1.6<br><sub>4,0,0,1,3</sub> |  | 0.8<br><sub>1,0,0,6,0</sub> |  | 0.7 | 0.3 | 1.3 | 11.4 |
| Allen Graves (TOR) | 98% | 16.5<br><sub>10,7,14,16,13</sub> | 5.5<br><sub>3,0,5,3,3</sub> |  | 2.9<br><sub>0,0,1,2,2</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.5 | 9.4 |
| Kyle Anderson (TOR) | 67% | 15.1<br><sub>4,8,4,-,16</sub> | 4.3<br><sub>2,2,2,-,6</sub> |  | 2.9<br><sub>3,0,0,-,2</sub> |  | 2.6<br><sub>3,0,1,-,2</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.5 | 0.8 | 9.7 |
| Malachi Smith (TOR) | 91% | 12.3<br><sub>-,-,-,-,1</sub> | 4.1<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.6 |
| Jaden Bradley (TOR) | 80% | 9.2<br><sub>4,-,4,8,9</sub> | 3.1<br><sub>3,-,2,3,0</sub> |  | 1.4<br><sub>1,-,1,0,1</sub> |  | 1.6<br><sub>2,-,0,1,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 6.2 |
| Kevin McCullar Jr. (TOR) | 16% | 8.8<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |

</details>

<details><summary>if LeBron James plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey (PHI) | 98% | 38.6<br><sub>36,34,32,36,34</sub> | 25.7<br><sub>26,19,17,27,24</sub> |  | 3.9<br><sub>4,1,3,4,1</sub> |  | 5.8<br><sub>11,7,4,7,4</sub> |  | 2.7<br><sub>1,3,2,3,3</sub> |  | 1.5 | 0.6 | 2.7 | 35.5 |
| Jaylen Brown (PHI) | 98% | 36.7<br><sub>33,37,34,35,26</sub> | 24.8<br><sub>25,30,20,29,13</sub> |  | 6.7<br><sub>11,7,5,7,5</sub> |  | 4.3<br><sub>5,1,5,4,2</sub> |  | 2.0<br><sub>4,3,2,2,1</sub> |  | 1.1 | 0.5 | 3.4 | 35.7 |
| VJ Edgecombe (PHI) | 93% | 35.9<br><sub>33,35,32,35,32</sub> | 14.3<br><sub>21,11,19,13,8</sub> |  | 6.0<br><sub>3,6,3,6,4</sub> |  | 3.6<br><sub>5,3,2,3,5</sub> |  | 1.9<br><sub>2,1,3,3,0</sub> |  | 1.4 | 0.5 | 1.7 | 24.0 |
| LeBron James (PHI) | 100% | 35.3<br><sub>31,33,32,33,29</sub> | 19.5<br><sub>15,13,8,22,11</sub> |  | 6.9<br><sub>7,10,7,5,8</sub> |  | 6.7<br><sub>9,8,3,5,5</sub> |  | 1.4<br><sub>0,1,0,2,1</sub> |  | 1.2 | 0.7 | 3.5 | 33.2 |
| Dean Wade (PHI) | 96% | 25.2<br><sub>23,22,21,18,23</sub> | 4.9<br><sub>8,3,0,0,8</sub> |  | 4.1<br><sub>2,5,5,1,9</sub> |  | 1.4<br><sub>1,1,1,1,0</sub> |  | 0.7<br><sub>2,0,0,0,2</sub> |  | 0.9 | 0.3 | 0.7 | 10.3 |
| Anfernee Simons (PHI) | 98% | 22.4<br><sub>24,10,19,16,18</sub> | 10.1<br><sub>6,0,6,3,17</sub> |  | 2.2<br><sub>2,1,2,4,3</sub> |  | 1.5<br><sub>1,0,2,2,0</sub> |  | 1.8<br><sub>1,0,1,1,3</sub> |  | 0.6 | 0.2 | 1.0 | 13.9 |
| Kentavious Caldwell-Pope (PHI) | 98% | 21.3<br><sub>13,21,17,21,16</sub> | 5.4<br><sub>3,5,5,6,0</sub> |  | 2.3<br><sub>1,1,2,6,0</sub> |  | 1.5<br><sub>0,0,0,3,2</sub> |  | 0.7<br><sub>1,1,1,2,0</sub> |  | 0.8 | 0.3 | 0.8 | 9.3 |
| Jabari Walker (PHI) | 88% | 15.1<br><sub>2,-,17,19,15</sub> | 5.3<br><sub>0,-,8,9,2</sub> |  | 4.0<br><sub>0,-,5,11,4</sub> |  | 0.6<br><sub>1,-,1,0,0</sub> |  | 0.4<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.2 | 0.6 | 9.9 |
| Rayan Rupert (PHI) | 52% | 11.6<br><sub>2,-,-,-,6</sub> | 4.0<br><sub>2,-,-,-,0</sub> |  | 2.2<br><sub>2,-,-,-,1</sub> |  | 0.7<br><sub>0,-,-,-,1</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.1 | 0.7 | 7.0 |
| Justin Edwards (PHI) | 58% | 9.0<br><sub>2,-,4,-,6</sub> | 3.3<br><sub>2,-,3,-,0</sub> |  | 1.2<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.3<br><sub>0,-,1,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |
| Labaron Philon Jr. (PHI) | 63% | 8.7<br><sub>2,-,4,-,6</sub> | 3.4<br><sub>0,-,3,-,2</sub> |  | 1.3<br><sub>0,-,1,-,1</sub> |  | 0.9<br><sub>0,-,1,-,3</sub> |  | 0.3<br><sub>0,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 5.7 |
| Tacko Fall (PHI) | 58% | 8.5<br><sub>-,-,3,-,-</sub> | 0.5<br><sub>-,-,0,-,-</sub> |  | 2.1<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.5 | 0.4 | 2.9 |
| Caleb Love (PHI) | 35% | 7.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.3 | 1.2 |
| RJ Barrett (TOR) | 98% | 35.9<br><sub>32,37,33,37,36</sub> | 24.7<br><sub>22,26,22,27,19</sub> |  | 6.8<br><sub>10,6,5,7,3</sub> |  | 4.5<br><sub>5,3,3,5,2</sub> |  | 2.0<br><sub>4,2,3,0,1</sub> |  | 0.8 | 0.5 | 2.8 | 36.0 |
| Immanuel Quickley (TOR) | 72% | 32.1<br><sub>33,38,32,-,-</sub> | 17.2<br><sub>12,27,13,-,-</sub> |  | 4.0<br><sub>6,4,1,-,-</sub> |  | 6.4<br><sub>7,2,7,-,-</sub> |  | 2.5<br><sub>3,1,2,-,-</sub> |  | 1.2 | 0.1 | 1.8 | 27.6 |
| Ja'Kobe Walter (TOR) | 98% | 31.5<br><sub>33,35,27,29,34</sub> | 12.5<br><sub>11,10,8,7,12</sub> |  | 4.2<br><sub>4,6,1,6,6</sub> |  | 2.2<br><sub>2,5,2,2,0</sub> |  | 2.0<br><sub>3,0,1,1,2</sub> |  | 1.3 | 0.3 | 1.1 | 18.9 |
| Jamal Shead (TOR) | 98% | 30.3<br><sub>25,20,20,34,36</sub> | 10.2<br><sub>9,6,3,10,20</sub> |  | 2.5<br><sub>2,1,3,3,2</sub> |  | 7.8<br><sub>6,6,6,16,11</sub> |  | 1.4<br><sub>2,0,1,1,4</sub> |  | 1.2 | 0.2 | 2.4 | 20.6 |
| Collin Murray-Boyles (TOR) | 98% | 28.5<br><sub>20,28,23,34,-</sub> | 13.4<br><sub>4,18,13,19,-</sub> |  | 6.7<br><sub>3,7,3,7,-</sub> |  | 2.4<br><sub>1,0,2,2,-</sub> |  | 0.5<br><sub>0,1,1,0,-</sub> |  | 1.1 | 1.1 | 1.8 | 22.5 |
| Jakob Poeltl (TOR) | 88% | 26.5<br><sub>-,-,19,31,31</sub> | 10.9<br><sub>-,-,8,19,18</sub> |  | 8.1<br><sub>-,-,5,11,8</sub> |  | 2.2<br><sub>-,-,1,1,2</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.9 | 1.1 | 1.6 | 21.2 |
| Jamison Battle (TOR) | 98% | 25.7<br><sub>17,21,19,21,29</sub> | 11.5<br><sub>20,12,9,6,18</sub> |  | 3.5<br><sub>5,0,1,2,1</sub> |  | 1.2<br><sub>0,0,0,0,2</sub> |  | 2.0<br><sub>4,4,2,1,5</sub> |  | 0.5 | 0.2 | 0.9 | 16.3 |
| Alijah Martin (TOR) | 91% | 17.3<br><sub>16,6,9,31,21</sub> | 7.2<br><sub>5,2,6,27,2</sub> |  | 2.5<br><sub>2,2,1,4,3</sub> |  | 1.6<br><sub>4,0,0,1,3</sub> |  | 0.8<br><sub>1,0,0,6,0</sub> |  | 0.7 | 0.3 | 1.3 | 11.3 |
| Allen Graves (TOR) | 98% | 16.5<br><sub>10,7,14,16,13</sub> | 5.5<br><sub>3,0,5,3,3</sub> |  | 3.0<br><sub>0,0,1,2,2</sub> |  | 1.0<br><sub>0,2,1,0,1</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.4 | 9.4 |
| Kyle Anderson (TOR) | 67% | 15.0<br><sub>4,8,4,-,16</sub> | 4.3<br><sub>2,2,2,-,6</sub> |  | 2.9<br><sub>3,0,0,-,2</sub> |  | 2.6<br><sub>3,0,1,-,2</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.6 | 0.8 | 9.7 |
| Malachi Smith (TOR) | 91% | 12.3<br><sub>-,-,-,-,1</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.6 |
| Jaden Bradley (TOR) | 80% | 9.2<br><sub>4,-,4,8,9</sub> | 3.1<br><sub>3,-,2,3,0</sub> |  | 1.4<br><sub>1,-,1,0,1</sub> |  | 1.6<br><sub>2,-,0,1,3</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 6.2 |
| Kevin McCullar Jr. (TOR) | 16% | 8.8<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |

</details>


### DET @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Jalen Duren (DET), Isaiah Joe (DET)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.4–109.8 | DET 76% | 1.32 / 4.09 | WAS +9.5 | 229.5 | WAS +9.5 covers 50%; o220.5 68% |
| Expected (weighted by chance each plays) | 119.5–110.0 | DET 75% | 1.33 / 3.99 | WAS +9.5 | 229.5 | WAS +9.5 covers 51%; o220.5 68% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Elijah Harkless (DET) | Questionable | 55% | 7.3 | 0.4 | 0.3 | 0.4 | 0.0 | 0.2 | 0.2 | 0.3 | 1.1 | small |
| Isaac Jones (DET) | Questionable | 55% | 6.3 | 6.6 | 1.6 | 0.4 | 0.2 | 0.3 | 0.3 | 0.3 | 8.5 | small |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 34.0<br><sub>28,27,40,38,27</sub> | 26.2<br><sub>20,33,26,14,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,5,7,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 8.8<br><sub>4,7,11,8,7</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,4,1,1,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.6 | 3.7 | 40.4 |
| Duncan Robinson | 98% | 30.9<br><sub>26,32,37,27,34</sub> | 16.8<br><sub>17,24,27,12,22</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>4,2,1,0,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,3,2,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>2,6,7,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 1.2 | 22.2 |
| Daniss Jenkins | 98% | 28.9<br><sub>24,23,21,32,36</sub> | 14.2<br><sub>6,2,5,31,22</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>3,1,1,5,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>5,7,4,4,8</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>2,0,1,8,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.3 | 1.8 | 23.6 |
| Ausar Thompson | 98% | 28.1<br><sub>26,26,34,24,28</sub> | 10.9<br><sub>11,14,11,7,8</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>8,6,17,11,5</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>6,4,3,3,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.0 | 1.0 | 1.8 | 23.3 |
| Kevin Huerter | 97% | 27.9<br><sub>24,20,20,35,33</sub> | 12.0<br><sub>8,9,8,24,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>1,2,1,5,2</sub> |  | 3.4<br><sub>3,3,0,5,3</sub> |  | 1.7<br><sub>2,3,2,4,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.6 | 1.1 | 19.1 |
| John Collins | 98% | 27.7<br><sub>26,19,26,32,28</sub> | 13.0<br><sub>4,4,16,8,24</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>9,3,1,4,10</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>0,1,0,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>0,0,0,1,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.0 | 0.8 | 1.3 | 21.1 |
| Paul Reed | 98% | 23.7<br><sub>31,28,30,20,21</sub> | 12.6<br><sub>12,11,8,8,4</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 7.9<br><sub>4,5,7,10,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,4,4,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.2 | 1.6 | 22.7 |
| Javonte Green | 97% | 17.5<br><sub>22,20,15,17,11</sub> | 6.2<br><sub>6,5,1,7,7</sub> |  | 2.7<br><sub>3,2,3,2,1</sub> |  | 0.8<br><sub>1,0,1,2,0</sub> |  | 0.8<br><sub>1,1,0,1,0</sub> |  | 1.1 | 0.3 | 0.4 | 9.7 |
| Ronald Holland II | 98% | 16.0<br><sub>22,20,12,14,15</sub> | 6.6<br><sub>18,11,3,5,1</sub> |  | 3.5<br><sub>3,2,2,2,5</sub> |  | 1.2<br><sub>2,0,0,1,2</sub> |  | 0.6<br><sub>2,3,1,1,0</sub> |  | 0.8 | 0.5 | 0.9 | 11.3 |
| Taurean Prince | 35% | 9.5<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.9 |
| Tolu Smith | 58% | 6.5<br><sub>3,8,5,-,-</sub> | 2.6<br><sub>2,0,1,-,-</sub> |  | 2.3<br><sub>1,2,1,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.3 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 34.6<br><sub>34,34,37,28,38</sub> | 17.8<br><sub>15,18,23,4,20</sub> |  | 3.0<br><sub>3,2,2,5,1</sub> |  | 8.8<br><sub>9,6,10,3,7</sub> |  | 2.2<br><sub>2,2,3,0,3</sub> |  | 1.2 | 0.2 | 3.2 | 29.6 |
| Anthony Davis | 98% | 33.3<br><sub>34,30,-,-,34</sub> | 21.7<br><sub>27,26,-,-,44</sub> |  | 11.1<br><sub>9,10,-,-,13</sub> |  | 2.7<br><sub>1,3,-,-,1</sub> |  | 0.8<br><sub>1,0,-,-,2</sub> |  | 1.2 | 1.9 | 2.3 | 35.5 |
| Kyshawn George | 98% | 32.9<br><sub>37,35,39,30,35</sub> | 15.2<br><sub>22,25,33,14,12</sub> |  | 4.8<br><sub>4,4,4,7,3</sub> |  | 4.3<br><sub>5,7,7,6,2</sub> |  | 2.0<br><sub>4,3,5,2,2</sub> |  | 1.1 | 1.3 | 2.5 | 24.3 |
| AJ Dybantsa | 96% | 32.9<br><sub>33,32,36,31,37</sub> | 15.0<br><sub>21,9,11,19,21</sub> |  | 6.2<br><sub>5,6,9,6,8</sub> |  | 2.5<br><sub>2,3,3,3,1</sub> |  | 1.1<br><sub>1,0,1,1,1</sub> |  | 1.1 | 0.5 | 2.2 | 23.7 |
| Alex Sarr | 98% | 25.2<br><sub>-,23,30,28,25</sub> | 10.6<br><sub>-,11,13,15,4</sub> |  | 6.8<br><sub>-,9,8,14,8</sub> |  | 2.0<br><sub>-,1,3,1,0</sub> |  | 1.0<br><sub>-,0,1,1,0</sub> |  | 0.8 | 1.7 | 1.5 | 19.3 |
| Bilal Coulibaly | 98% | 22.2<br><sub>33,23,24,20,-</sub> | 7.6<br><sub>7,6,9,0,-</sub> |  | 3.2<br><sub>1,2,5,5,-</sub> |  | 1.4<br><sub>2,2,0,0,-</sub> |  | 0.7<br><sub>0,0,1,0,-</sub> |  | 1.0 | 0.8 | 1.1 | 12.3 |
| Tre Johnson | 91% | 21.1<br><sub>22,14,27,28,29</sub> | 8.1<br><sub>4,3,23,4,2</sub> |  | 1.8<br><sub>3,2,1,0,2</sub> |  | 1.0<br><sub>0,0,1,3,0</sub> |  | 1.1<br><sub>0,1,5,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 11.0 |
| Bub Carrington | 98% | 17.6<br><sub>19,19,15,21,19</sub> | 5.6<br><sub>3,0,5,9,4</sub> |  | 1.8<br><sub>4,1,1,6,0</sub> |  | 2.2<br><sub>4,2,1,1,4</sub> |  | 0.8<br><sub>1,0,1,3,1</sub> |  | 0.5 | 0.2 | 1.2 | 9.6 |
| Deandre Ayton | 98% | 14.1<br><sub>24,11,23,7,13</sub> | 4.7<br><sub>4,5,8,2,2</sub> |  | 4.6<br><sub>6,4,11,1,8</sub> |  | 0.6<br><sub>2,1,3,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.7 | 9.9 |
| Will Riley | 91% | 8.7<br><sub>4,13,9,20,4</sub> | 3.5<br><sub>0,0,7,5,0</sub> |  | 1.0<br><sub>0,0,0,2,0</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Khris Middleton | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.7 | 4.9 |
| Anthony Gill | 52% | 6.4<br><sub>-,-,-,9,2</sub> | 2.2<br><sub>-,-,-,1,0</sub> |  | 1.1<br><sub>-,-,-,1,2</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.7 |
| Tre Mann | 63% | 6.1<br><sub>-,3,-,18,2</sub> | 2.5<br><sub>-,2,-,2,0</sub> |  | 0.6<br><sub>-,0,-,0,0</sub> |  | 0.7<br><sub>-,0,-,2,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |
| Felix Okpara | 58% | 5.9<br><sub>-,3,-,-,2</sub> | 2.4<br><sub>-,0,-,-,2</sub> |  | 1.8<br><sub>-,1,-,-,1</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.3 | 0.4 | 4.5 |

</details>


### DAL @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Sergio de Larrea (DAL), Dereck Lively II (DAL)

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 33.3<br><sub>40,40,33,28,39</sub> | 22.9<br><sub>17,19,21,25,43</sub> |  | 6.6<br><sub>4,10,10,5,10</sub> |  | 5.3<br><sub>6,5,7,12,6</sub> |  | 1.2<br><sub>0,0,1,3,3</sub> |  | 1.4 | 0.8 | 2.8 | 34.8 |
| Kyrie Irving | 98% | 33.3<br><sub>-,36,28,29,38</sub> | 21.8<br><sub>-,29,14,21,35</sub> |  | 4.2<br><sub>-,7,2,3,0</sub> |  | 3.9<br><sub>-,5,2,4,4</sub> |  | 2.4<br><sub>-,5,0,2,7</sub> |  | 1.2 | 0.4 | 2.2 | 30.0 |
| P.J. Washington | 98% | 31.3<br><sub>38,39,33,25,35</sub> | 13.3<br><sub>12,21,26,6,13</sub> |  | 6.7<br><sub>5,10,6,5,9</sub> |  | 1.4<br><sub>1,3,1,0,1</sub> |  | 1.5<br><sub>2,3,6,2,2</sub> |  | 1.0 | 0.9 | 1.6 | 21.4 |
| Naji Marshall | 91% | 23.6<br><sub>24,26,25,15,25</sub> | 11.4<br><sub>5,22,7,8,6</sub> |  | 3.4<br><sub>2,5,1,1,5</sub> |  | 3.0<br><sub>7,3,5,2,2</sub> |  | 0.7<br><sub>0,3,0,1,0</sub> |  | 0.9 | 0.1 | 1.6 | 17.8 |
| Daniel Gafford | 98% | 20.0<br><sub>26,18,18,19,20</sub> | 8.9<br><sub>20,2,7,18,8</sub> |  | 5.7<br><sub>7,4,1,5,2</sub> |  | 1.2<br><sub>0,1,1,2,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.4 | 1.1 | 15.8 |
| Zaccharie Risacher | 96% | 17.5<br><sub>19,18,21,16,15</sub> | 5.5<br><sub>0,2,4,11,4</sub> |  | 3.3<br><sub>5,1,4,6,2</sub> |  | 0.9<br><sub>1,2,1,1,0</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.7 | 0.6 | 0.8 | 9.6 |
| Walter Clayton Jr. | 91% | 16.8<br><sub>24,21,23,16,25</sub> | 6.5<br><sub>20,8,12,5,6</sub> |  | 3.1<br><sub>1,6,4,4,6</sub> |  | 2.9<br><sub>2,5,2,6,4</sub> |  | 0.7<br><sub>4,2,1,1,1</sub> |  | 0.6 | 0.2 | 1.2 | 12.4 |
| Santi Aldama | 98% | 16.3<br><sub>-,-,13,15,19</sub> | 7.8<br><sub>-,-,8,12,10</sub> |  | 3.8<br><sub>-,-,9,2,4</sub> |  | 1.2<br><sub>-,-,1,0,1</sub> |  | 0.8<br><sub>-,-,0,2,1</sub> |  | 0.5 | 0.4 | 1.0 | 12.8 |
| Caleb Martin | 98% | 14.8<br><sub>21,20,11,19,19</sub> | 3.4<br><sub>5,0,0,2,0</sub> |  | 2.2<br><sub>6,3,0,2,3</sub> |  | 1.0<br><sub>0,2,0,2,5</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.6 | 0.2 | 0.7 | 6.6 |
| Max Christie | 98% | 12.4<br><sub>8,-,9,17,5</sub> | 4.1<br><sub>0,-,0,5,0</sub> |  | 1.5<br><sub>2,-,1,2,2</sub> |  | 0.7<br><sub>0,-,1,0,0</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.3 |
| Morez Johnson Jr. | 92% | 11.3<br><sub>17,18,24,19,-</sub> | 4.3<br><sub>13,8,13,4,-</sub> |  | 2.3<br><sub>2,3,17,9,-</sub> |  | 1.0<br><sub>1,1,2,1,-</sub> |  | 0.2<br><sub>0,1,1,0,-</sub> |  | 0.3 | 0.1 | 0.7 | 7.6 |
| Marcus Sasser | 64% | 8.6<br><sub>19,5,-,9,-</sub> | 3.0<br><sub>4,0,-,4,-</sub> |  | 0.8<br><sub>1,1,-,0,-</sub> |  | 1.0<br><sub>1,2,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.8 |
| Moussa Cisse | 58% | 6.7<br><sub>2,-,1,5,-</sub> | 2.6<br><sub>0,-,0,2,-</sub> |  | 2.5<br><sub>0,-,0,1,-</sub> |  | 0.2<br><sub>0,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.3 |
| Tobi Lawal | 58% | 6.1<br><sub>2,-,1,5,-</sub> | 2.4<br><sub>2,-,0,2,-</sub> |  | 2.1<br><sub>0,-,0,0,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |
| Jett Howard | 58% | 5.7<br><sub>2,-,1,3,-</sub> | 2.5<br><sub>2,-,0,5,-</sub> |  | 0.7<br><sub>0,-,0,1,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>0,-,0,1,-</sub> |  | 0.1 | 0.1 | 0.3 | 3.6 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 32.8<br><sub>39,29,37,40,33</sub> | 16.8<br><sub>19,13,14,23,16</sub> |  | 5.5<br><sub>3,6,8,6,6</sub> |  | 3.2<br><sub>3,3,4,5,3</sub> |  | 1.5<br><sub>2,2,0,2,2</sub> |  | 1.1 | 1.0 | 1.7 | 25.5 |
| Ayo Dosunmu | 98% | 31.5<br><sub>38,37,34,39,30</sub> | 18.1<br><sub>27,19,21,26,26</sub> |  | 4.4<br><sub>9,12,1,2,4</sub> |  | 4.4<br><sub>3,8,6,4,1</sub> |  | 1.8<br><sub>2,1,0,4,4</sub> |  | 1.2 | 0.4 | 1.9 | 26.9 |
| Rudy Gobert | 98% | 29.1<br><sub>-,31,33,25,31</sub> | 9.6<br><sub>-,10,8,8,10</sub> |  | 11.4<br><sub>-,10,11,11,15</sub> |  | 1.8<br><sub>-,1,2,0,2</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.4 | 22.7 |
| Jonathan Kuminga | 98% | 29.0<br><sub>40,33,32,34,25</sub> | 13.6<br><sub>19,8,16,17,4</sub> |  | 5.4<br><sub>6,10,8,8,0</sub> |  | 2.5<br><sub>3,3,5,4,0</sub> |  | 1.4<br><sub>2,2,4,1,0</sub> |  | 0.9 | 0.6 | 1.5 | 21.5 |
| LaMelo Ball | 98% | 28.9<br><sub>20,33,31,35,30</sub> | 20.9<br><sub>10,34,20,22,24</sub> |  | 4.2<br><sub>8,6,2,2,3</sub> |  | 6.5<br><sub>4,3,6,8,5</sub> |  | 3.5<br><sub>0,6,4,3,4</sub> |  | 1.4 | 0.2 | 3.1 | 31.6 |
| Terrence Shannon Jr. | 98% | 20.6<br><sub>18,-,-,-,18</sub> | 11.1<br><sub>2,-,-,-,5</sub> |  | 2.6<br><sub>3,-,-,-,3</sub> |  | 2.0<br><sub>4,-,-,-,3</sub> |  | 1.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.1 | 1.2 | 15.7 |
| Trey Lyles | 98% | 20.3<br><sub>17,21,20,29,21</sub> | 6.9<br><sub>6,12,5,5,9</sub> |  | 4.7<br><sub>0,4,2,13,6</sub> |  | 1.2<br><sub>0,0,0,2,2</sub> |  | 0.9<br><sub>1,2,1,0,1</sub> |  | 0.6 | 0.3 | 0.6 | 12.8 |
| Jaylen Clark | 91% | 17.8<br><sub>20,21,25,21,19</sub> | 5.9<br><sub>10,4,10,8,3</sub> |  | 2.3<br><sub>2,2,4,3,2</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.7<br><sub>2,1,2,1,0</sub> |  | 1.0 | 0.2 | 0.5 | 9.3 |
| Joan Beringer | 97% | 14.5<br><sub>34,14,13,7,16</sub> | 6.4<br><sub>12,2,4,2,4</sub> |  | 5.1<br><sub>6,7,7,3,3</sub> |  | 0.6<br><sub>2,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 12.1 |
| Bones Hyland | 98% | 14.2<br><sub>14,14,16,10,13</sub> | 8.6<br><sub>6,10,19,4,14</sub> |  | 1.6<br><sub>1,1,2,1,2</sub> |  | 2.5<br><sub>3,3,4,0,2</sub> |  | 1.2<br><sub>0,2,4,1,1</sub> |  | 0.6 | 0.3 | 1.0 | 12.6 |
| Rocco Zikarsky | 48% | 6.9<br><sub>-,-,-,-,2</sub> | 2.6<br><sub>-,-,-,-,0</sub> |  | 2.4<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.6 | 0.4 | 5.3 |
| Zyon Pullin | 38% | 6.2<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Cody Williams | 52% | 5.8<br><sub>-,7,-,-,2</sub> | 0.3<br><sub>-,0,-,-,0</sub> |  | 1.7<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 2.3 |

</details>


### CHA @ PHX
Out: Mark Williams (PHX), Kon Knueppel (CHA), Brandon Miller (CHA), Dennis Schroder (CHA), Hannes Steinbach (CHA)

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Grayson Allen | 98% | 31.2<br><sub>30,19,27,22,34</sub> | 18.1<br><sub>27,11,22,0,27</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>4,1,2,2,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.9<br><sub>3,0,4,3,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.0<br><sub>7,3,5,0,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 2.3 | 25.5 |
| Naz Reid | 98% | 31.1<br><sub>36,27,36,26,32</sub> | 19.8<br><sub>14,13,28,14,25</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>5,6,9,6,13</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>2,2,2,2,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>0,2,2,2,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.8 | 2.7 | 30.3 |
| Sion James | 98% | 29.9<br><sub>18,21,31,21,33</sub> | 8.7<br><sub>4,11,10,11,11</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>2,4,2,3,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>1,3,1,0,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,3,0,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.3 | 16.2 |
| Moussa Diabate | 92% | 29.0<br><sub>28,24,29,-,-</sub> | 9.1<br><sub>10,7,7,-,-</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 9.4<br><sub>8,9,6,-,-</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>3,2,2,-,-</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.0<br><sub>0,0,0,-,-</sub> |  | 1.1 | 1.0 | 1.7 | 21.0 |
| Ryan Kalkbrenner | 98% | 25.0<br><sub>19,16,19,21,35</sub> | 8.0<br><sub>6,4,6,4,8</sub> |  | 6.7<br><sub>3,6,4,5,15</sub> |  | 1.6<br><sub>4,0,2,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.5 | 1.3 | 16.3 |
| Royce O'Neale | 98% | 23.9<br><sub>23,18,18,26,23</sub> | 7.6<br><sub>8,2,0,7,10</sub> |  | 4.2<br><sub>6,4,3,4,3</sub> |  | 1.7<br><sub>1,0,2,2,1</sub> |  | 1.3<br><sub>1,0,0,2,2</sub> |  | 0.8 | 0.4 | 0.9 | 13.4 |
| Coby White | 98% | 22.6<br><sub>-,16,18,16,20</sub> | 16.1<br><sub>-,7,4,7,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>-,0,5,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>-,3,2,1,9</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>-,1,0,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.2 | 2.5 | 23.2 |
| Tidjane Salaun | 96% | 18.7<br><sub>12,19,10,23,18</sub> | 7.2<br><sub>5,1,9,13,14</sub> |  | 4.3<br><sub>2,7,1,4,3</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>1,0,3,2,3</sub> |  | 0.6 | 0.2 | 0.9 | 12.3 |
| Grant Williams | 54% | 18.7<br><sub>-,-,-,-,-</sub> | 6.8<br><sub>-,-,-,-,-</sub> |  | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.5 | 1.2 | 11.8 |
| Christian Anderson | 86% | 17.1<br><sub>8,9,-,25,16</sub> | 6.8<br><sub>2,8,-,4,9</sub> |  | 2.2<br><sub>0,2,-,3,1</sub> |  | 2.2<br><sub>0,2,-,5,1</sub> |  | 0.9<br><sub>0,1,-,0,3</sub> |  | 0.5 | 0.3 | 1.9 | 11.2 |
| Liam McNeeley | 64% | 16.8<br><sub>-,9,-,19,16</sub> | 6.8<br><sub>-,3,-,8,8</sub> |  | 3.1<br><sub>-,0,-,2,1</sub> |  | 1.3<br><sub>-,1,-,3,1</sub> |  | 0.8<br><sub>-,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.9 | 11.2 |
| PJ Hall | 38% | 8.9<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.7 | 7.0 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.1<br><sub>34,34,39,29,29</sub> | 24.6<br><sub>33,30,24,32,17</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,1,2,2,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.7<br><sub>2,8,3,4,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>2,4,2,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 2.8 | 33.7 |
| Dillon Brooks | 98% | 29.8<br><sub>35,29,37,26,22</sub> | 15.9<br><sub>15,24,11,7,8</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>6,1,4,4,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>2,1,1,0,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>0,4,3,1,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.4 | 21.4 |
| Miles Bridges | 98% | 28.4<br><sub>31,31,31,26,18</sub> | 13.5<br><sub>18,18,13,7,8</sub> | 15.5 · –<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>7,13,10,5,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>5,5,7,0,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>4,3,1,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.5 | 1.1 | 22.1 |
| Jalen Green | 98% | 27.6<br><sub>32,24,34,24,21</sub> | 14.6<br><sub>22,6,16,6,13</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>2,0,3,5,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>2,3,6,4,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>2,0,0,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 2.1 | 21.4 |
| Collin Gillespie | 98% | 22.7<br><sub>23,24,20,24,22</sub> | 8.4<br><sub>2,6,7,6,12</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,2,3,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>2,2,4,3,8</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,2,1,2,4</sub> |  | 1.1 | 0.1 | 1.0 | 14.8 |
| Oso Ighodaro | 98% | 21.5<br><sub>23,24,23,18,20</sub> | 6.4<br><sub>9,2,4,7,6</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>7,5,6,4,8</sub> |  | 2.5<br><sub>7,1,3,2,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.7 | 1.2 | 14.0 |
| Ryan Dunn | 98% | 19.0<br><sub>18,25,23,23,25</sub> | 5.6<br><sub>2,11,8,3,10</sub> |  | 3.9<br><sub>6,3,5,2,8</sub> |  | 1.3<br><sub>2,3,3,0,2</sub> |  | 0.7<br><sub>0,1,2,1,1</sub> |  | 0.8 | 0.4 | 0.6 | 10.8 |
| Khaman Maluach | 98% | 17.8<br><sub>16,22,18,20,22</sub> | 6.1<br><sub>6,8,8,11,11</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>6,6,10,5,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 0.8<br><sub>2,2,0,2,3</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 1.0 | 1.0 | 12.0 |
| Luke Kennard | 98% | 17.5<br><sub>14,21,14,14,22</sub> | 6.8<br><sub>0,12,11,3,14</sub> |  | 1.9<br><sub>0,1,1,1,1</sub> |  | 1.8<br><sub>1,5,2,0,3</sub> |  | 0.9<br><sub>0,3,3,1,3</sub> |  | 0.6 | 0.1 | 0.6 | 10.4 |
| Jordan Goodwin | 98% | 15.9<br><sub>-,-,-,-,14</sub> | 6.4<br><sub>-,-,-,-,18</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>-,-,-,-,1</sub> |  | 0.9<br><sub>-,-,-,-,6</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 0.6 | 11.1 |
| Rasheer Fleming | 58% | 9.2<br><sub>-,-,-,9,12</sub> | 3.4<br><sub>-,-,-,2,4</sub> |  | 1.5<br><sub>-,-,-,1,2</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.4 | 5.2 |
| Jamaree Bouyea | 67% | 7.3<br><sub>3,2,-,9,8</sub> | 2.9<br><sub>3,0,-,4,7</sub> |  | 0.9<br><sub>0,0,-,0,1</sub> |  | 1.1<br><sub>0,0,-,3,3</sub> |  | 0.2<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |
| Koa Peat | 66% | 6.9<br><sub>3,2,-,6,6</sub> | 2.7<br><sub>2,0,-,4,5</sub> |  | 1.3<br><sub>1,1,-,0,1</sub> |  | 0.3<br><sub>0,0,-,1,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 4.3 |
| Pat Spencer | 67% | 6.9<br><sub>3,2,-,6,-</sub> | 2.4<br><sub>0,0,-,2,-</sub> |  | 0.9<br><sub>0,0,-,2,-</sub> |  | 1.1<br><sub>2,0,-,2,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.4 |
| Drew Timme | 16% | 6.3 | 2.5 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Duop Reath | 67% | 6.2<br><sub>7,2,-,6,-</sub> | 2.6<br><sub>7,0,-,2,-</sub> |  | 1.2<br><sub>0,0,-,2,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>1,0,-,0,-</sub> |  | 0.1 | 0.2 | 0.2 | 4.1 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-12/`._
