# NBA model · Sat 14 Nov 2026 (US date)

Updated **Sat 14 Nov, 06:56 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-14/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

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
| DEN @ NOP | Sun 15 Nov 11:00 | 124.2–113.9 | DEN 76% | 1.31 / 4.25 | NOP +10.5 | 238.5 | NOP +11.5 covers 53%; o234.5 58% |
| DAL @ CLE | Sun 15 Nov 11:30 | 114.8–117.8 | DAL 41% | 2.41 / 1.71 | CLE -3.5 | 232.5 | CLE -3.5 covers 49%; o231.5 52% |
| DET @ MIA | Sun 15 Nov 12:00 | 118.2–112.6 | DET 66% | 1.52 / 2.91 | MIA +5.5 | 230.5 | MIA +4.5 covers 46%; o228.5 55% |
| BKN @ MEM | Sun 15 Nov 12:00 | 110.1–118.6 | BKN 27% | 3.67 / 1.37 | MEM -8.5 | 228.5 | MEM -5.5 covers 59%; o227.5 52% |
| CHI @ MIN | Sun 15 Nov 12:00 | 111.2–123.8 | CHI 19% | 5.40 / 1.23 | MIN -12.5 | 235.5 | MIN -14.5 covers 45%; o236.5 47% |

### DEN @ NOP
Out: Bryce McGowens (NOP), Yves Missi (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Julian Strawther (DEN), Cam Whitmore (DEN)

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 36.1<br><sub>39,28,34,39,32</sub> | 26.3<br><sub>35,14,16,38,30</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,5,6,2,4</sub> |  | 6.3<br><sub>6,7,8,2,8</sub> |  | 3.3<br><sub>4,2,2,5,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.6 | 2.3 | 37.1 |
| Nikola Jokic | 98% | 36.0<br><sub>36,30,36,39,37</sub> | 28.2<br><sub>26,32,19,25,27</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 12.9<br><sub>9,10,13,16,11</sub> |  | 10.4<br><sub>8,11,8,9,8</sub> |  | 1.5<br><sub>2,0,1,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6 | 1.0 | 3.4 | 51.5 |
| Christian Braun | 98% | 33.2<br><sub>37,28,29,32,37</sub> | 13.3<br><sub>14,11,6,4,12</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>3,3,4,5,5</sub> |  | 2.6<br><sub>3,3,1,3,4</sub> |  | 1.4<br><sub>1,1,0,0,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.5 | 1.0 | 20.3 |
| Cameron Johnson | 98% | 29.5<br><sub>34,30,29,31,30</sub> | 13.3<br><sub>7,12,18,8,23</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,2,4,2,4</sub> |  | 2.4<br><sub>2,2,1,1,3</sub> |  | 2.0<br><sub>1,4,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.4 | 1.1 | 19.7 |
| Aaron Gordon | 98% | 28.8<br><sub>30,25,27,30,27</sub> | 13.5<br><sub>5,17,12,3,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>6,1,5,5,3</sub> |  | 2.6<br><sub>2,0,0,2,2</sub> |  | 1.3<br><sub>1,1,0,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.4 | 1.3 | 21.7 |
| DeMar DeRozan | 88% | 21.8<br><sub>20,-,22,19,20</sub> | 11.9<br><sub>9,-,11,7,8</sub> |  | 2.1<br><sub>0,-,1,4,1</sub> |  | 3.2<br><sub>1,-,5,2,4</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.7 | 0.3 | 1.1 | 17.2 |
| Spencer Jones | 71% | 17.3<br><sub>-,-,21,14,22</sub> | 4.8<br><sub>-,-,13,0,3</sub> |  | 2.7<br><sub>-,-,6,0,1</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.6<br><sub>-,-,3,0,1</sub> |  | 0.7 | 0.6 | 0.5 | 8.3 |
| Trevon Brazile | 98% | 15.7<br><sub>18,23,14,14,13</sub> | 5.2<br><sub>6,6,3,5,7</sub> |  | 4.2<br><sub>5,7,4,2,5</sub> |  | 0.8<br><sub>1,1,2,0,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 10.2 |
| Marvin Bagley III | 98% | 13.2<br><sub>12,14,12,12,12</sub> | 6.6<br><sub>6,10,10,6,4</sub> |  | 4.1<br><sub>4,2,3,3,2</sub> |  | 0.7<br><sub>0,2,0,0,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 11.4 |
| Tyus Jones | 96% | 10.1<br><sub>8,18,13,6,11</sub> | 2.8<br><sub>2,6,3,2,0</sub> |  | 0.9<br><sub>0,1,4,0,1</sub> |  | 1.8<br><sub>1,8,4,0,4</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.5 |
| Bryce Hopkins | 63% | 8.7<br><sub>-,28,3,3,-</sub> | 2.9<br><sub>-,18,3,2,-</sub> |  | 1.5<br><sub>-,4,1,0,-</sub> |  | 0.5<br><sub>-,1,0,0,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.9 |
| Zeke Nnaji | 35% | 7.1<br><sub>-,4,-,-,-</sub> | 2.6<br><sub>-,2,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.5 |
| Alpha Diallo | 58% | 6.3<br><sub>6,4,-,1,-</sub> | 2.5<br><sub>0,0,-,0,-</sub> |  | 1.1<br><sub>1,0,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zion Williamson | 98% | 35.1<br><sub>38,36,31,-,30</sub> | 23.1<br><sub>23,13,25,-,29</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>4,8,4,-,4</sub> |  | 4.0<br><sub>2,4,2,-,2</sub> |  | 0.2<br><sub>0,0,0,-,1</sub> |  | 1.4 | 0.6 | 2.2 | 33.5 |
| Jeremiah Fears | 98% | 33.3<br><sub>34,36,29,29,28</sub> | 17.7<br><sub>19,24,25,11,14</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>6,5,6,3,4</sub> |  | 6.2<br><sub>2,5,5,8,5</sub> |  | 1.6<br><sub>1,0,3,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.5 | 2.9 | 28.8 |
| Saddiq Bey | 98% | 32.3<br><sub>29,31,26,24,29</sub> | 18.7<br><sub>22,17,13,9,15</sub> |  | 4.8<br><sub>4,5,4,0,1</sub> |  | 3.0<br><sub>3,4,3,4,2</sub> |  | 2.4<br><sub>2,3,1,1,3</sub> |  | 0.9 | 0.2 | 1.2 | 26.6 |
| Herbert Jones | 98% | 28.9<br><sub>37,14,20,24,25</sub> | 8.7<br><sub>2,0,4,10,2</sub> |  | 3.5<br><sub>5,4,0,6,2</sub> |  | 2.5<br><sub>1,0,1,1,3</sub> |  | 1.2<br><sub>0,0,0,2,0</sub> |  | 1.4 | 0.5 | 1.2 | 14.7 |
| Karlo Matkovic | 96% | 26.8<br><sub>21,18,19,17,22</sub> | 11.1<br><sub>5,18,3,4,4</sub> |  | 6.2<br><sub>4,3,3,6,4</sub> |  | 1.6<br><sub>2,1,2,2,1</sub> |  | 1.4<br><sub>1,4,1,0,0</sub> |  | 0.8 | 0.9 | 1.1 | 19.0 |
| Derik Queen | 98% | 26.6<br><sub>27,10,21,21,14</sub> | 13.8<br><sub>20,6,8,16,9</sub> |  | 7.5<br><sub>9,4,5,4,0</sub> |  | 3.5<br><sub>6,1,3,0,0</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.8 | 2.3 | 24.9 |
| Jordan Poole | 63% | 23.7<br><sub>-,-,-,34,21</sub> | 10.8<br><sub>-,-,-,7,14</sub> |  | 2.3<br><sub>-,-,-,3,0</sub> |  | 3.0<br><sub>-,-,-,2,1</sub> |  | 1.8<br><sub>-,-,-,1,2</sub> |  | 0.8 | 0.4 | 1.4 | 16.2 |
| Bennedict Mathurin | 98% | 22.1<br><sub>15,7,9,24,-</sub> | 9.7<br><sub>2,2,6,6,-</sub> |  | 3.8<br><sub>5,0,0,2,-</sub> |  | 1.9<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,0,0,0,-</sub> |  | 0.7 | 0.2 | 1.1 | 15.3 |
| DeAndre Jordan | 38% | 16.3<br><sub>-,-,-,-,11</sub> | 3.7<br><sub>-,-,-,-,0</sub> |  | 6.0<br><sub>-,-,-,-,3</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.7 | 0.7 | 10.7 |
| Jaron Pierre Jr. | 80% | 13.0<br><sub>-,-,-,-,7</sub> | 4.5<br><sub>-,-,-,-,4</sub> |  | 3.4<br><sub>-,-,-,-,4</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.5 | 0.2 | 0.6 | 8.8 |
| AJ Johnson | 58% | 12.1<br><sub>-,-,3,12,7</sub> | 3.2<br><sub>-,-,2,2,2</sub> |  | 1.6<br><sub>-,-,0,2,1</sub> |  | 1.3<br><sub>-,-,0,3,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 6.0 |
| Julian Reese | 63% | 11.2<br><sub>-,-,3,9,7</sub> | 3.4<br><sub>-,-,0,2,2</sub> |  | 1.6<br><sub>-,-,0,0,2</sub> |  | 0.9<br><sub>-,-,0,0,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.5 | 5.8 |
| Malik Dia | 3% | 8.8 | 3.6 |  | 1.6 |  | 0.7 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>


### DAL @ CLE
Out: Sam Merrill (CLE), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE), Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.8–117.8 | DAL 41% | 2.41 / 1.71 | CLE -3.5 | 232.5 | CLE -3.5 covers 49%; o231.5 52% |
| Expected (weighted by chance each plays) | 114.7–117.8 | DAL 41% | 2.43 / 1.70 | CLE -3.5 | 232.5 | CLE -3.5 covers 50%; o231.5 52% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Max Christie (DAL) | Questionable | 55% | 12.2 | 4.4 | 1.4 | 0.7 | 0.6 | 0.4 | 0.1 | 0.5 | 6.6 | small |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 33.9<br><sub>40,33,28,39,27</sub> | 22.9<br><sub>19,21,25,43,12</sub> |  | 6.7<br><sub>10,10,5,10,7</sub> |  | 5.5<br><sub>5,7,12,6,3</sub> |  | 1.3<br><sub>0,1,3,3,1</sub> |  | 1.4 | 0.7 | 2.6 | 35.2 |
| Kyrie Irving | 98% | 33.4<br><sub>36,28,29,38,27</sub> | 21.0<br><sub>29,14,21,35,10</sub> |  | 4.0<br><sub>7,2,3,0,3</sub> |  | 4.1<br><sub>5,2,4,4,4</sub> |  | 2.6<br><sub>5,0,2,7,2</sub> |  | 1.1 | 0.4 | 1.9 | 29.1 |
| P.J. Washington | 98% | 32.2<br><sub>39,33,25,35,16</sub> | 14.1<br><sub>21,26,6,13,10</sub> |  | 6.7<br><sub>10,6,5,9,3</sub> |  | 1.5<br><sub>3,1,0,1,0</sub> |  | 1.8<br><sub>3,6,2,2,1</sub> |  | 1.0 | 0.8 | 1.4 | 22.3 |
| Naji Marshall | 91% | 24.0<br><sub>26,25,15,25,23</sub> | 11.8<br><sub>22,7,8,6,13</sub> |  | 3.3<br><sub>5,1,1,5,1</sub> |  | 3.2<br><sub>3,5,2,2,4</sub> |  | 0.8<br><sub>3,0,1,0,1</sub> |  | 1.0 | 0.1 | 1.5 | 18.2 |
| Zaccharie Risacher | 97% | 21.0<br><sub>18,21,16,15,25</sub> | 7.4<br><sub>2,4,11,4,22</sub> |  | 3.9<br><sub>1,4,6,2,6</sub> |  | 1.2<br><sub>2,1,1,0,3</sub> |  | 0.8<br><sub>0,0,1,0,4</sub> |  | 0.8 | 0.6 | 0.9 | 12.5 |
| Daniel Gafford | 98% | 19.7<br><sub>18,18,19,20,16</sub> | 8.6<br><sub>2,7,18,8,3</sub> |  | 5.7<br><sub>4,1,5,2,3</sub> |  | 1.2<br><sub>1,1,2,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 15.5 |
| Walter Clayton Jr. | 91% | 17.9<br><sub>21,23,16,25,22</sub> | 6.6<br><sub>8,12,5,6,5</sub> |  | 2.7<br><sub>6,4,4,6,1</sub> |  | 3.0<br><sub>5,2,6,4,4</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.2 | 1.3 | 12.3 |
| Caleb Martin | 98% | 16.3<br><sub>20,11,19,19,21</sub> | 4.1<br><sub>0,0,2,0,7</sub> |  | 2.4<br><sub>3,0,2,3,2</sub> |  | 1.2<br><sub>2,0,2,5,5</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.7 | 0.2 | 0.6 | 7.7 |
| Santi Aldama | 98% | 15.0<br><sub>-,13,15,19,10</sub> | 7.4<br><sub>-,8,12,10,3</sub> |  | 3.5<br><sub>-,9,2,4,1</sub> |  | 1.2<br><sub>-,1,0,1,1</sub> |  | 0.8<br><sub>-,0,2,1,1</sub> |  | 0.5 | 0.3 | 0.8 | 12.0 |
| Morez Johnson Jr. | 92% | 14.1<br><sub>18,24,19,-,13</sub> | 5.6<br><sub>8,13,4,-,0</sub> |  | 2.8<br><sub>3,17,9,-,2</sub> |  | 1.1<br><sub>1,2,1,-,0</sub> |  | 0.3<br><sub>1,1,0,-,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.5 |
| Marcus Sasser | 67% | 11.1<br><sub>5,-,9,-,9</sub> | 3.9<br><sub>0,-,4,-,3</sub> |  | 0.9<br><sub>1,-,0,-,1</sub> |  | 1.2<br><sub>2,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.0 |
| Moussa Cisse | 64% | 6.9<br><sub>-,1,5,-,8</sub> | 2.3<br><sub>-,0,2,-,0</sub> |  | 2.5<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,1,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.1 |
| Tobi Lawal | 63% | 6.6<br><sub>-,1,5,-,12</sub> | 2.6<br><sub>-,0,2,-,0</sub> |  | 1.3<br><sub>-,0,0,-,6</sub> |  | 0.5<br><sub>-,0,0,-,1</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.4 |
| Jett Howard | 63% | 6.2<br><sub>-,1,3,-,5</sub> | 2.8<br><sub>-,0,5,-,3</sub> |  | 0.7<br><sub>-,0,1,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,1,-,1</sub> |  | 0.2 | 0.1 | 0.2 | 3.9 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 98% | 35.1<br><sub>33,33,37,23,36</sub> | 27.4<br><sub>27,23,37,11,23</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>3,7,4,2,7</sub> |  | 5.6<br><sub>6,8,4,4,6</sub> |  | 3.2<br><sub>5,1,5,1,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5 | 0.4 | 2.8 | 38.3 |
| James Harden | 98% | 34.8<br><sub>35,30,34,25,33</sub> | 19.8<br><sub>19,17,7,11,32</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>9,6,2,3,2</sub> |  | 6.6<br><sub>6,3,5,5,4</sub> |  | 2.7<br><sub>3,3,1,2,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.6 | 3.0 | 31.4 |
| Peyton Watson | 98% | 29.6<br><sub>-,28,29,21,30</sub> | 13.3<br><sub>-,13,12,13,7</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>-,9,6,2,5</sub> |  | 2.6<br><sub>-,2,3,1,4</sub> |  | 1.4<br><sub>-,1,1,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 1.5 | 1.5 | 21.0 |
| Jarrett Allen | 98% | 28.2<br><sub>7,-,-,19,32</sub> | 14.4<br><sub>0,-,-,12,11</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 9.4<br><sub>1,-,-,7,14</sub> |  | 1.8<br><sub>0,-,-,1,3</sub> |  | 0.1<br><sub>0,-,-,1,0</sub> |  | 1.0 | 1.5 | 1.2 | 25.5 |
| Meleek Thomas | 91% | 25.6<br><sub>18,27,24,27,22</sub> | 11.6<br><sub>9,12,9,18,14</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>1,1,4,3,4</sub> |  | 1.5<br><sub>0,3,0,3,1</sub> |  | 1.8<br><sub>3,2,3,4,2</sub> |  | 1.1 | 0.4 | 1.1 | 16.1 |
| Tyrese Proctor | 91% | 22.4<br><sub>22,19,23,23,23</sub> | 8.8<br><sub>11,3,7,6,15</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>1,6,3,1,3</sub> |  | 2.9<br><sub>0,3,3,4,1</sub> |  | 1.2<br><sub>2,0,2,0,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.1 | 1.0 | 14.8 |
| Jaylon Tyson | 97% | 22.3<br><sub>-,-,-,-,23</sub> | 9.0<br><sub>-,-,-,-,3</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,-,-,-,0</sub> |  | 2.2<br><sub>-,-,-,-,1</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.4 | 1.0 | 15.2 |
| Mario Hezonja | 98% | 18.4<br><sub>23,27,19,17,7</sub> | 7.2<br><sub>12,15,0,10,0</sub> |  | 4.8<br><sub>8,10,5,3,0</sub> |  | 1.3<br><sub>1,1,1,0,0</sub> |  | 0.9<br><sub>2,2,0,0,0</sub> |  | 0.6 | 0.3 | 0.8 | 13.3 |
| Thomas Bryant | 63% | 14.3<br><sub>13,16,15,15,-</sub> | 7.4<br><sub>8,13,5,11,-</sub> |  | 3.8<br><sub>0,6,3,2,-</sub> |  | 0.6<br><sub>0,0,1,0,-</sub> |  | 0.8<br><sub>1,1,1,2,-</sub> |  | 0.4 | 0.5 | 0.6 | 11.8 |
| Craig Porter Jr. | 67% | 13.6<br><sub>14,3,15,17,-</sub> | 3.0<br><sub>0,0,0,9,-</sub> |  | 2.5<br><sub>1,0,1,2,-</sub> |  | 2.3<br><sub>1,0,1,4,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.6 | 0.4 | 0.6 | 7.8 |
| Riley Minix | 52% | 11.8<br><sub>-,-,10,17,-</sub> | 4.2<br><sub>-,-,8,2,-</sub> |  | 2.0<br><sub>-,-,3,2,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.5<br><sub>-,-,2,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.8 |
| Khalifa Diop | 3% | 8.7 | 3.7 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Norchad Omier | 52% | 8.6<br><sub>-,3,-,12,-</sub> | 2.6<br><sub>-,0,-,0,-</sub> |  | 2.2<br><sub>-,2,-,3,-</sub> |  | 0.8<br><sub>-,1,-,2,-</sub> |  | 0.1<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.2 | 0.5 | 5.6 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |

</details>


### DET @ MIA
Out: Pelle Larsson (MIA), Klay Thompson (MIA), Jalen Duren (DET), Isaiah Joe (DET)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.2–112.6 | DET 66% | 1.52 / 2.91 | MIA +5.5 | 230.5 | MIA +4.5 covers 46%; o228.5 55% |
| Expected (weighted by chance each plays) | 118.3–112.6 | DET 66% | 1.52 / 2.93 | MIA +5.5 | 231.5 | MIA +4.5 covers 46%; o228.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Elijah Harkless (DET) | Questionable | 55% | 6.7 | 0.4 | 0.3 | 0.4 | 0.0 | 0.1 | 0.1 | 0.3 | 1.0 | small |
| Isaac Jones (DET) | Questionable | 55% | 5.7 | 5.9 | 1.6 | 0.3 | 0.1 | 0.2 | 0.3 | 0.3 | 7.8 | small |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 35.3<br><sub>27,40,38,27,48</sub> | 27.7<br><sub>33,26,14,17,52</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,7,4,3,5</sub> |  | 9.0<br><sub>7,11,8,7,11</sub> |  | 2.4<br><sub>4,1,1,0,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.7 | 3.9 | 42.0 |
| Duncan Robinson | 98% | 32.1<br><sub>32,37,27,34,41</sub> | 16.5<br><sub>24,27,12,22,13</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>2,1,0,3,3</sub> |  | 2.6<br><sub>3,2,3,2,1</sub> |  | 3.1<br><sub>6,7,3,4,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.2 | 1.1 | 22.1 |
| Daniss Jenkins | 98% | 30.9<br><sub>23,21,32,36,42</sub> | 15.3<br><sub>2,5,31,22,21</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>1,1,5,6,6</sub> |  | 5.2<br><sub>7,4,4,8,0</sub> |  | 1.9<br><sub>0,1,8,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 1.9 | 24.5 |
| Ausar Thompson | 98% | 30.2<br><sub>26,34,24,28,43</sub> | 11.3<br><sub>14,11,7,8,17</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.9<br><sub>6,17,11,5,11</sub> |  | 4.6<br><sub>4,3,3,4,11</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.9 | 1.1 | 2.0 | 23.7 |
| John Collins | 98% | 26.5<br><sub>19,26,32,28,25</sub> | 11.7<br><sub>4,16,8,24,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>3,1,4,10,4</sub> |  | 1.1<br><sub>1,0,1,3,0</sub> |  | 1.0<br><sub>0,0,1,2,2</sub> |  | 0.8 | 0.8 | 1.3 | 19.0 |
| Paul Reed | 98% | 26.5<br><sub>28,30,20,21,38</sub> | 13.1<br><sub>11,8,8,4,13</sub> |  | 8.5<br><sub>5,7,10,10,11</sub> |  | 2.3<br><sub>4,4,0,2,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.1 | 1.7 | 24.0 |
| Kevin Huerter | 98% | 24.6<br><sub>20,20,35,33,24</sub> | 10.8<br><sub>9,8,24,12,11</sub> |  | 3.2<br><sub>2,1,5,2,1</sub> |  | 2.6<br><sub>3,0,5,3,0</sub> |  | 1.6<br><sub>3,2,4,0,1</sub> |  | 1.1 | 0.6 | 1.0 | 16.6 |
| Javonte Green | 98% | 17.0<br><sub>20,15,17,11,15</sub> | 6.4<br><sub>5,1,7,7,5</sub> |  | 2.5<br><sub>2,3,2,1,1</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.9<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.3 | 0.4 | 9.7 |
| Ronald Holland II | 98% | 14.5<br><sub>20,12,14,15,14</sub> | 5.7<br><sub>11,3,5,1,2</sub> |  | 3.1<br><sub>2,2,2,5,5</sub> |  | 1.1<br><sub>0,0,1,2,2</sub> |  | 0.5<br><sub>3,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.9 | 9.9 |
| Taurean Prince | 30% | 8.4<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Tolu Smith | 52% | 5.8<br><sub>8,5,-,-,-</sub> | 2.3<br><sub>0,1,-,-,-</sub> |  | 2.1<br><sub>2,1,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.7 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 38.3<br><sub>29,43,38,40,38</sub> | 15.3<br><sub>15,11,22,17,19</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>0,2,2,3,5</sub> |  | 8.1<br><sub>7,10,8,11,8</sub> |  | 2.0<br><sub>4,0,4,2,3</sub> |  | 1.3 | 0.3 | 2.8 | 26.4 |
| Bam Adebayo | 98% | 37.0<br><sub>31,41,33,34,37</sub> | 20.9<br><sub>16,35,18,18,11</sub> | 17.5 · –<br><sub>o 53% · u 47%</sub> | 10.0<br><sub>9,10,10,8,8</sub> |  | 3.8<br><sub>4,4,0,4,4</sub> |  | 1.6<br><sub>1,1,0,1,0</sub> | 0.5<br><sub>o 68% · u 32%</sub> | 1.7 | 0.9 | 2.0 | 34.7 |
| Giannis Antetokounmpo | 98% | 36.1<br><sub>34,41,31,34,31</sub> | 30.2<br><sub>30,27,20,29,30</sub> | 28.5 · –<br><sub>o 51% · u 49%</sub> | 12.9<br><sub>12,14,14,14,11</sub> |  | 6.5<br><sub>7,6,4,3,4</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 1.1 | 1.1 | 4.0 | 49.5 |
| Andrew Wiggins | 98% | 29.0<br><sub>24,23,21,32,19</sub> | 11.8<br><sub>7,3,2,6,13</sub> |  | 4.0<br><sub>0,4,6,3,0</sub> |  | 1.8<br><sub>2,1,4,1,0</sub> |  | 1.7<br><sub>2,1,0,2,2</sub> |  | 0.9 | 1.0 | 1.3 | 17.6 |
| Ryan Conwell | 88% | 24.7<br><sub>8,17,30,19,21</sub> | 8.1<br><sub>5,0,13,6,5</sub> |  | 2.6<br><sub>1,2,1,2,4</sub> |  | 2.0<br><sub>1,2,2,2,2</sub> |  | 1.3<br><sub>1,0,3,2,1</sub> |  | 0.9 | 0.1 | 1.0 | 12.7 |
| Bobby Portis | 98% | 24.0<br><sub>18,18,14,20,17</sub> | 9.7<br><sub>2,4,0,4,5</sub> |  | 6.4<br><sub>3,10,5,1,1</sub> |  | 1.5<br><sub>2,5,0,1,1</sub> |  | 1.4<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.4 | 0.9 | 17.5 |
| Tim Hardaway Jr. | 76% | 19.4<br><sub>19,7,4,7,-</sub> | 7.7<br><sub>9,0,0,0,-</sub> |  | 1.9<br><sub>0,0,0,0,-</sub> |  | 0.8<br><sub>0,0,1,0,-</sub> |  | 1.3<br><sub>3,0,0,0,-</sub> |  | 0.5 | 0.2 | 0.8 | 10.5 |
| Dru Smith | 52% | 15.5<br><sub>11,-,1,-,-</sub> | 4.6<br><sub>3,-,0,-,-</sub> |  | 2.1<br><sub>3,-,0,-,-</sub> |  | 2.0<br><sub>2,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 1.2 | 0.3 | 0.8 | 8.7 |
| Nikola Jovic | 52% | 14.7<br><sub>7,-,12,-,-</sub> | 5.0<br><sub>2,-,1,-,-</sub> |  | 2.7<br><sub>1,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.3 | 0.8 | 8.8 |
| Keshad Johnson | 52% | 14.6<br><sub>-,-,-,-,-</sub> | 6.3<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.8 | 0.4 | 0.8 | 9.8 |
| Simone Fontecchio | 52% | 12.0<br><sub>-,5,-,-,7</sub> | 5.6<br><sub>-,0,-,-,3</sub> |  | 2.1<br><sub>-,0,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.8<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.4 |
| Myron Gardner | 58% | 11.1<br><sub>1,-,1,-,10</sub> | 4.0<br><sub>0,-,0,-,4</sub> |  | 3.0<br><sub>0,-,0,-,3</sub> |  | 1.0<br><sub>0,-,0,-,1</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 7.9 |
| Nick Richards | 52% | 9.7<br><sub>1,-,1,-,-</sub> | 3.4<br><sub>0,-,0,-,-</sub> |  | 3.3<br><sub>1,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.5 | 0.7 | 7.0 |
| Vladislav Goldin | 8% | 9.6 | 2.7 |  | 2.9 |  | 0.8 |  | 0.1 |  | 0.2 | 0.8 | 0.7 | 6.3 |
| Tre Donaldson | 5% | 8.5 | 3.4 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.7 |

</details>


### BKN @ MEM
Out: Zach Edey (MEM), Scotty Pippen Jr. (MEM), Quinten Post (MEM), Grant Nelson (BKN), Ben Saraf (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.1–118.6 | BKN 27% | 3.67 / 1.37 | MEM -8.5 | 228.5 | MEM -5.5 covers 59%; o227.5 52% |
| Expected (weighted by chance each plays) | 110.5–118.3 | BKN 29% | 3.49 / 1.40 | MEM -7.5 | 228.5 | MEM -5.5 covers 57%; o227.5 52% |
| if Mikel Brown Jr. plays | 110.7–118.2 | BKN 30% | 3.38 / 1.42 | MEM -7.5 | 228.5 | MEM -5.5 covers 56%; o227.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Mikel Brown Jr. (BKN) | Questionable | 55% | 20.2 | 10.7 | 2.2 | 3.2 | 1.3 | 0.8 | 0.2 | 1.7 | 16.1 | full tables below |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 98% | 34.0<br><sub>37,38,36,29,28</sub> | 22.6<br><sub>18,26,25,19,22</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 7.6<br><sub>5,10,9,9,6</sub> |  | 2.4<br><sub>2,0,1,0,3</sub> |  | 3.1<br><sub>4,4,3,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 2.3 | 32.6 |
| Julius Randle | 98% | 33.7<br><sub>36,31,34,30,29</sub> | 19.6<br><sub>21,22,19,13,17</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>11,3,7,4,4</sub> |  | 5.0<br><sub>2,4,8,4,5</sub> |  | 1.3<br><sub>0,2,1,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.3 | 3.5 | 31.6 |
| Day'Ron Sharpe | 98% | 23.1<br><sub>22,27,32,20,19</sub> | 10.4<br><sub>4,6,12,6,15</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 7.9<br><sub>6,5,10,4,4</sub> |  | 3.8<br><sub>3,8,13,6,5</sub> |  | 0.4<br><sub>0,0,0,0,2</sub> |  | 1.2 | 1.2 | 2.1 | 22.1 |
| Egor Demin | 98% | 23.1<br><sub>-,-,-,-,23</sub> | 9.9<br><sub>-,-,-,-,22</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>-,-,-,-,1</sub> |  | 3.2<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.3 | 1.5 | 16.1 |
| Danny Wolf | 71% | 22.5<br><sub>-,19,31,36,29</sub> | 9.1<br><sub>-,12,11,10,10</sub> |  | 5.8<br><sub>-,5,9,3,11</sub> |  | 2.3<br><sub>-,3,1,2,4</sub> |  | 1.1<br><sub>-,2,2,1,1</sub> |  | 0.7 | 0.6 | 1.4 | 17.2 |
| Nolan Traore | 92% | 21.9<br><sub>24,27,23,21,-</sub> | 11.4<br><sub>17,16,19,14,-</sub> |  | 2.2<br><sub>3,4,1,1,-</sub> |  | 3.6<br><sub>4,2,2,2,-</sub> |  | 1.4<br><sub>5,2,2,2,-</sub> |  | 1.0 | 0.5 | 2.4 | 17.2 |
| Keon Ellis | 86% | 20.7<br><sub>25,10,-,22,26</sub> | 5.7<br><sub>5,1,-,3,11</sub> |  | 2.2<br><sub>1,2,-,1,4</sub> |  | 1.8<br><sub>0,0,-,4,3</sub> |  | 0.8<br><sub>1,0,-,1,2</sub> |  | 1.2 | 0.6 | 0.7 | 9.7 |
| Noah Clowney | 98% | 18.9<br><sub>20,17,21,8,19</sub> | 7.1<br><sub>2,7,3,2,16</sub> |  | 3.6<br><sub>6,1,10,0,3</sub> |  | 1.0<br><sub>2,1,0,0,0</sub> |  | 0.8<br><sub>0,1,1,0,2</sub> |  | 0.6 | 0.5 | 0.9 | 11.7 |
| Moritz Wagner | 96% | 17.5<br><sub>20,20,16,16,19</sub> | 9.7<br><sub>6,6,9,12,16</sub> |  | 4.1<br><sub>1,1,2,3,3</sub> |  | 1.3<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 0.6 | 0.3 | 1.1 | 15.1 |
| Terance Mann | 72% | 16.4<br><sub>-,16,13,22,18</sub> | 4.0<br><sub>-,0,0,0,6</sub> |  | 2.0<br><sub>-,2,2,1,1</sub> |  | 1.8<br><sub>-,2,0,1,3</sub> |  | 0.4<br><sub>-,0,0,0,2</sub> |  | 0.6 | 0.2 | 0.7 | 7.8 |
| Chaney Johnson | 96% | 15.2<br><sub>28,9,8,15,15</sub> | 4.2<br><sub>4,0,5,2,4</sub> |  | 2.2<br><sub>3,2,2,0,3</sub> |  | 0.9<br><sub>2,1,1,1,2</sub> |  | 0.3<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.4 | 0.9 | 7.4 |
| Drake Powell | 58% | 11.2<br><sub>-,-,-,9,7</sub> | 3.6<br><sub>-,-,-,2,6</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 0.9<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 5.6 |
| Josh Minott | 63% | 9.8<br><sub>-,6,-,12,7</sub> | 4.9<br><sub>-,0,-,10,0</sub> |  | 1.9<br><sub>-,1,-,2,2</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.5<br><sub>-,0,-,2,0</sub> |  | 0.6 | 0.4 | 0.6 | 7.3 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 33.0<br><sub>38,33,31,33,33</sub> | 16.6<br><sub>18,10,8,22,13</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 9.5<br><sub>9,6,12,7,11</sub> |  | 5.5<br><sub>5,4,4,8,5</sub> |  | 1.8<br><sub>2,2,0,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.6 | 3.0 | 31.6 |
| Ty Jerome | 98% | 30.7<br><sub>37,29,28,32,32</sub> | 23.2<br><sub>40,23,21,27,22</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>5,4,2,6,2</sub> |  | 5.6<br><sub>5,3,5,2,5</sub> |  | 2.7<br><sub>5,2,2,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.3 | 2.7 | 32.5 |
| Jaylen Wells | 98% | 28.3<br><sub>34,21,25,26,31</sub> | 13.0<br><sub>16,0,7,14,22</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>3,1,0,4,2</sub> |  | 1.6<br><sub>3,3,0,1,1</sub> |  | 1.9<br><sub>3,0,1,4,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.1 | 17.9 |
| Cedric Coward | 98% | 27.9<br><sub>31,33,23,28,27</sub> | 15.1<br><sub>10,23,10,3,15</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 7.2<br><sub>9,9,9,6,11</sub> |  | 2.9<br><sub>3,4,0,4,4</sub> |  | 1.8<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.5 | 1.7 | 25.1 |
| Jerami Grant | 98% | 22.9<br><sub>24,24,22,22,20</sub> | 11.7<br><sub>11,11,10,17,14</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,1,0,3,2</sub> |  | 1.7<br><sub>2,2,2,2,2</sub> |  | 1.4<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.6 | 1.2 | 15.9 |
| Cam Spencer | 98% | 20.6<br><sub>19,24,19,17,20</sub> | 8.6<br><sub>13,7,7,7,15</sub> |  | 2.6<br><sub>1,6,1,2,3</sub> |  | 5.0<br><sub>7,9,0,4,3</sub> |  | 1.3<br><sub>2,1,1,1,3</sub> |  | 0.7 | 0.2 | 1.2 | 16.2 |
| Javon Small | 96% | 19.0<br><sub>-,-,21,24,15</sub> | 8.0<br><sub>-,-,10,9,3</sub> |  | 2.8<br><sub>-,-,4,2,1</sub> |  | 3.2<br><sub>-,-,2,5,4</sub> |  | 1.0<br><sub>-,-,1,1,1</sub> |  | 0.8 | 0.2 | 1.3 | 13.9 |
| Isaiah Stewart | 98% | 18.4<br><sub>28,10,-,-,18</sub> | 8.6<br><sub>14,6,-,-,3</sub> |  | 4.0<br><sub>5,1,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,2</sub> |  | 0.5<br><sub>2,0,-,-,1</sub> |  | 0.3 | 1.1 | 0.9 | 13.6 |
| GG Jackson | 86% | 14.6<br><sub>16,7,-,17,13</sub> | 8.1<br><sub>6,1,-,2,2</sub> |  | 2.9<br><sub>0,2,-,1,1</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.5 | 1.0 | 11.9 |
| Taylor Hendricks | 67% | 11.4<br><sub>-,-,4,16,11</sub> | 4.8<br><sub>-,-,4,9,7</sub> |  | 2.3<br><sub>-,-,2,3,2</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.5<br><sub>-,-,1,1,1</sub> |  | 0.6 | 0.3 | 0.5 | 7.7 |
| Kris Murray | 66% | 9.0<br><sub>19,15,13,1,-</sub> | 2.5<br><sub>0,5,2,0,-</sub> |  | 1.4<br><sub>4,1,2,0,-</sub> |  | 0.6<br><sub>1,1,1,0,-</sub> |  | 0.1<br><sub>0,1,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Jahmai Mashack | 48% | 8.4<br><sub>-,-,4,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,2,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 4.8 |
| Olivier-Maxence Prosper | 58% | 8.3<br><sub>-,7,11,1,-</sub> | 4.5<br><sub>-,4,2,0,-</sub> |  | 1.8<br><sub>-,3,3,0,-</sub> |  | 0.5<br><sub>-,1,1,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.7 |
| Karim Lopez | 48% | 5.8<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 3.6 |

</details>

<details><summary>if Mikel Brown Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. (BKN) | 98% | 31.8<br><sub>37,38,36,29,28</sub> | 20.1<br><sub>18,26,25,19,22</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 7.1<br><sub>5,10,9,9,6</sub> |  | 2.1<br><sub>2,0,1,0,3</sub> |  | 2.8<br><sub>4,4,3,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.4 | 2.0 | 29.2 |
| Julius Randle (BKN) | 98% | 31.3<br><sub>36,31,34,30,29</sub> | 17.9<br><sub>21,22,19,13,17</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 6.6<br><sub>11,3,7,4,4</sub> |  | 4.3<br><sub>2,4,8,4,5</sub> |  | 1.2<br><sub>0,2,1,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.3 | 3.0 | 28.8 |
| Egor Demin (BKN) | 98% | 21.7<br><sub>-,-,-,-,23</sub> | 9.1<br><sub>-,-,-,-,22</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>-,-,-,-,1</sub> |  | 2.8<br><sub>-,-,-,-,1</sub> |  | 1.4<br><sub>-,-,-,-,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.3 | 1.4 | 14.6 |
| Day'Ron Sharpe (BKN) | 98% | 21.3<br><sub>22,27,32,20,19</sub> | 9.3<br><sub>4,6,12,6,15</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>6,5,10,4,4</sub> |  | 3.4<br><sub>3,8,13,6,5</sub> |  | 0.4<br><sub>0,0,0,0,2</sub> |  | 1.0 | 1.1 | 1.8 | 20.0 |
| Mikel Brown Jr. (BKN) | 100% | 20.2<br><sub>27,20,25,-,-</sub> | 10.7<br><sub>13,18,18,-,-</sub> |  | 2.2<br><sub>2,2,1,-,-</sub> |  | 3.2<br><sub>3,4,3,-,-</sub> |  | 1.3<br><sub>1,3,3,-,-</sub> |  | 0.8 | 0.2 | 1.7 | 16.1 |
| Danny Wolf (BKN) | 71% | 20.1<br><sub>-,19,31,36,29</sub> | 7.9<br><sub>-,12,11,10,10</sub> |  | 5.2<br><sub>-,5,9,3,11</sub> |  | 2.0<br><sub>-,3,1,2,4</sub> |  | 0.9<br><sub>-,2,2,1,1</sub> |  | 0.6 | 0.6 | 1.2 | 15.2 |
| Nolan Traore (BKN) | 92% | 19.3<br><sub>24,27,23,21,-</sub> | 9.5<br><sub>17,16,19,14,-</sub> |  | 1.9<br><sub>3,4,1,1,-</sub> |  | 3.0<br><sub>4,2,2,2,-</sub> |  | 1.1<br><sub>5,2,2,2,-</sub> |  | 0.9 | 0.4 | 2.0 | 14.5 |
| Keon Ellis (BKN) | 86% | 18.4<br><sub>25,10,-,22,26</sub> | 4.8<br><sub>5,1,-,3,11</sub> |  | 2.0<br><sub>1,2,-,1,4</sub> |  | 1.4<br><sub>0,0,-,4,3</sub> |  | 0.6<br><sub>1,0,-,1,2</sub> |  | 1.1 | 0.6 | 0.6 | 8.2 |
| Noah Clowney (BKN) | 98% | 17.5<br><sub>20,17,21,8,19</sub> | 6.4<br><sub>2,7,3,2,16</sub> |  | 3.4<br><sub>6,1,10,0,3</sub> |  | 0.9<br><sub>2,1,0,0,0</sub> |  | 0.8<br><sub>0,1,1,0,2</sub> |  | 0.6 | 0.5 | 0.9 | 10.7 |
| Moritz Wagner (BKN) | 96% | 16.5<br><sub>20,20,16,16,19</sub> | 9.4<br><sub>6,6,9,12,16</sub> |  | 3.9<br><sub>1,1,2,3,3</sub> |  | 1.2<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 0.6 | 0.2 | 1.0 | 14.4 |
| Terance Mann (BKN) | 72% | 14.6<br><sub>-,16,13,22,18</sub> | 3.6<br><sub>-,0,0,0,6</sub> |  | 1.8<br><sub>-,2,2,1,1</sub> |  | 1.6<br><sub>-,2,0,1,3</sub> |  | 0.3<br><sub>-,0,0,0,2</sub> |  | 0.5 | 0.2 | 0.6 | 7.0 |
| Chaney Johnson (BKN) | 96% | 13.7<br><sub>28,9,8,15,15</sub> | 3.7<br><sub>4,0,5,2,4</sub> |  | 2.1<br><sub>3,2,2,0,3</sub> |  | 0.8<br><sub>2,1,1,1,2</sub> |  | 0.3<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 6.7 |
| Josh Minott (BKN) | 63% | 8.8<br><sub>-,6,-,12,7</sub> | 4.6<br><sub>-,0,-,10,0</sub> |  | 1.7<br><sub>-,1,-,2,2</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.5<br><sub>-,0,-,2,0</sub> |  | 0.5 | 0.4 | 0.5 | 6.8 |
| Drake Powell (BKN) | 58% | 8.4<br><sub>-,-,-,9,7</sub> | 2.5<br><sub>-,-,-,2,6</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.6<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.0 |
| Cameron Boozer (MEM) | 98% | 32.9<br><sub>38,33,31,33,33</sub> | 16.4<br><sub>18,10,8,22,13</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 9.5<br><sub>9,6,12,7,11</sub> |  | 5.5<br><sub>5,4,4,8,5</sub> |  | 1.8<br><sub>2,2,0,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.6 | 3.0 | 31.4 |
| Ty Jerome (MEM) | 98% | 30.7<br><sub>37,29,28,32,32</sub> | 23.1<br><sub>40,23,21,27,22</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>5,4,2,6,2</sub> |  | 5.6<br><sub>5,3,5,2,5</sub> |  | 2.7<br><sub>5,2,2,5,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.3 | 2.7 | 32.5 |
| Jaylen Wells (MEM) | 98% | 28.4<br><sub>34,21,25,26,31</sub> | 12.9<br><sub>16,0,7,14,22</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>3,1,0,4,2</sub> |  | 1.6<br><sub>3,3,0,1,1</sub> |  | 1.9<br><sub>3,0,1,4,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.1 | 17.9 |
| Cedric Coward (MEM) | 98% | 27.9<br><sub>31,33,23,28,27</sub> | 15.0<br><sub>10,23,10,3,15</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 7.1<br><sub>9,9,9,6,11</sub> |  | 2.9<br><sub>3,4,0,4,4</sub> |  | 1.8<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.5 | 1.7 | 25.0 |
| Jerami Grant (MEM) | 98% | 22.9<br><sub>24,24,22,22,20</sub> | 11.7<br><sub>11,11,10,17,14</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>4,1,0,3,2</sub> |  | 1.7<br><sub>2,2,2,2,2</sub> |  | 1.4<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.6 | 1.2 | 16.0 |
| Cam Spencer (MEM) | 98% | 20.5<br><sub>19,24,19,17,20</sub> | 8.6<br><sub>13,7,7,7,15</sub> |  | 2.6<br><sub>1,6,1,2,3</sub> |  | 5.0<br><sub>7,9,0,4,3</sub> |  | 1.2<br><sub>2,1,1,1,3</sub> |  | 0.7 | 0.2 | 1.2 | 16.2 |
| Javon Small (MEM) | 96% | 19.0<br><sub>-,-,21,24,15</sub> | 8.0<br><sub>-,-,10,9,3</sub> |  | 2.8<br><sub>-,-,4,2,1</sub> |  | 3.2<br><sub>-,-,2,5,4</sub> |  | 1.0<br><sub>-,-,1,1,1</sub> |  | 0.8 | 0.2 | 1.2 | 13.9 |
| Isaiah Stewart (MEM) | 98% | 18.3<br><sub>28,10,-,-,18</sub> | 8.6<br><sub>14,6,-,-,3</sub> |  | 4.0<br><sub>5,1,-,-,1</sub> |  | 0.9<br><sub>2,0,-,-,2</sub> |  | 0.5<br><sub>2,0,-,-,1</sub> |  | 0.3 | 1.1 | 0.9 | 13.5 |
| GG Jackson (MEM) | 86% | 14.7<br><sub>16,7,-,17,13</sub> | 8.1<br><sub>6,1,-,2,2</sub> |  | 2.9<br><sub>0,2,-,1,1</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.4 | 1.1 | 12.0 |
| Taylor Hendricks (MEM) | 67% | 11.4<br><sub>-,-,4,16,11</sub> | 4.8<br><sub>-,-,4,9,7</sub> |  | 2.3<br><sub>-,-,2,3,2</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.5<br><sub>-,-,1,1,1</sub> |  | 0.6 | 0.3 | 0.5 | 7.7 |
| Kris Murray (MEM) | 66% | 9.0<br><sub>19,15,13,1,-</sub> | 2.5<br><sub>0,5,2,0,-</sub> |  | 1.4<br><sub>4,1,2,0,-</sub> |  | 0.6<br><sub>1,1,1,0,-</sub> |  | 0.1<br><sub>0,1,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Jahmai Mashack (MEM) | 48% | 8.4<br><sub>-,-,4,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,2,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 4.7 |
| Olivier-Maxence Prosper (MEM) | 58% | 8.3<br><sub>-,7,11,1,-</sub> | 4.5<br><sub>-,4,2,0,-</sub> |  | 1.8<br><sub>-,3,3,0,-</sub> |  | 0.5<br><sub>-,1,1,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.8 |
| Karim Lopez (MEM) | 48% | 5.9<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 3.7 |

</details>


### CHI @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Tobe Awaka (CHI), Dailyn Swain (CHI), Caleb Wilson (CHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.2–123.8 | CHI 19% | 5.40 / 1.23 | MIN -12.5 | 235.5 | MIN -14.5 covers 45%; o236.5 47% |
| Expected (weighted by chance each plays) | 111.2–123.4 | CHI 19% | 5.23 / 1.24 | MIN -12.5 | 234.5 | MIN -14.5 covers 44%; o236.5 46% |
| if Jalen Smith plays | 111.3–123.1 | CHI 20% | 5.02 / 1.25 | MIN -11.5 | 234.5 | MIN -14.5 covers 43%; o236.5 46% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Smith (CHI) | Day-To-Day | 70% | 26.8 | 12.9 | 8.2 | 1.6 | 1.5 | 0.6 | 1.1 | 1.2 | 22.7 | full tables below |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 31.5<br><sub>25,32,27,34,25</sub> | 14.8<br><sub>13,13,10,19,9</sub> |  | 7.1<br><sub>4,4,1,7,2</sub> |  | 8.3<br><sub>5,10,6,15,7</sub> |  | 1.5<br><sub>2,2,1,1,1</sub> |  | 1.1 | 0.6 | 3.3 | 30.2 |
| Matas Buzelis | 98% | 31.4<br><sub>20,23,26,31,31</sub> | 16.1<br><sub>14,4,12,19,13</sub> |  | 5.9<br><sub>5,3,5,5,3</sub> |  | 2.2<br><sub>1,2,3,2,2</sub> |  | 2.0<br><sub>2,0,1,3,3</sub> |  | 0.8 | 1.4 | 2.6 | 24.2 |
| Norman Powell | 98% | 30.9<br><sub>31,29,22,-,-</sub> | 19.9<br><sub>16,18,12,-,-</sub> |  | 3.5<br><sub>2,3,1,-,-</sub> |  | 2.1<br><sub>3,0,1,-,-</sub> |  | 2.2<br><sub>1,1,0,-,-</sub> |  | 1.2 | 0.3 | 2.2 | 25.6 |
| Patrick Williams | 64% | 26.4<br><sub>-,-,20,25,28</sub> | 8.4<br><sub>-,-,4,7,9</sub> |  | 3.8<br><sub>-,-,0,3,7</sub> |  | 1.9<br><sub>-,-,2,3,4</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> |  | 0.9 | 0.6 | 1.2 | 14.2 |
| Isaac Okoro | 98% | 24.7<br><sub>18,21,15,25,23</sub> | 7.8<br><sub>6,4,6,12,0</sub> |  | 2.5<br><sub>3,1,1,2,2</sub> |  | 1.4<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.8 | 0.5 | 0.9 | 11.8 |
| Tre Jones | 98% | 23.8<br><sub>20,19,18,14,28</sub> | 13.3<br><sub>12,8,14,6,13</sub> |  | 3.3<br><sub>4,3,3,1,1</sub> |  | 4.0<br><sub>4,3,4,1,3</sub> |  | 0.5<br><sub>0,0,1,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 20.6 |
| Nic Claxton | 97% | 19.1<br><sub>-,-,-,18,16</sub> | 8.0<br><sub>-,-,-,4,17</sub> |  | 5.2<br><sub>-,-,-,4,6</sub> |  | 2.2<br><sub>-,-,-,4,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.0 | 1.0 | 15.4 |
| Jordan Hawkins | 86% | 17.3<br><sub>6,2,7,17,24</sub> | 6.9<br><sub>0,2,2,9,7</sub> |  | 2.4<br><sub>0,0,1,0,4</sub> |  | 1.0<br><sub>0,0,0,1,2</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.3 | 0.9 | 10.3 |
| Leonard Miller | 80% | 16.2<br><sub>11,9,19,-,2</sub> | 7.0<br><sub>2,2,4,-,0</sub> |  | 4.0<br><sub>2,3,6,-,0</sub> |  | 0.8<br><sub>1,0,3,-,0</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.4 | 0.9 | 11.8 |
| Noa Essengue | 96% | 16.2<br><sub>16,14,14,15,11</sub> | 6.3<br><sub>10,8,6,10,8</sub> |  | 4.0<br><sub>4,6,3,7,4</sub> |  | 0.7<br><sub>0,0,0,1,3</sub> |  | 0.6<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.4 | 0.9 | 11.0 |
| Zach Collins | 86% | 13.4<br><sub>2,10,14,-,3</sub> | 5.1<br><sub>0,2,3,-,2</sub> |  | 4.1<br><sub>0,3,1,-,2</sub> |  | 1.2<br><sub>0,0,3,-,1</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 10.4 |
| Buddy Hield | 58% | 12.9<br><sub>17,12,8,-,-</sub> | 5.3<br><sub>5,6,7,-,-</sub> |  | 1.9<br><sub>3,1,1,-,-</sub> |  | 1.2<br><sub>1,3,1,-,-</sub> |  | 0.7<br><sub>1,1,1,-,-</sub> |  | 0.5 | 0.2 | 0.7 | 8.4 |
| Orlando Robinson | 8% | 11.2 | 4.1 |  | 3.2 |  | 1.2 |  | 0.2 |  | 0.3 | 0.3 | 0.7 | 8.6 |
| Jaylin Sellers | 76% | 8.9<br><sub>3,2,14,-,2</sub> | 3.7<br><sub>3,3,14,-,3</sub> |  | 1.2<br><sub>0,0,3,-,0</sub> |  | 1.1<br><sub>1,0,1,-,3</sub> |  | 0.4<br><sub>1,0,4,-,1</sub> |  | 0.3 | 0.2 | 0.7 | 6.0 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 31.8<br><sub>29,37,40,33,25</sub> | 17.5<br><sub>13,14,23,16,16</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,8,6,6,9</sub> |  | 3.3<br><sub>3,4,5,3,3</sub> |  | 1.4<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.0 | 1.7 | 26.3 |
| Ayo Dosunmu | 98% | 30.3<br><sub>37,34,39,30,27</sub> | 18.0<br><sub>19,21,26,26,18</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>12,1,2,4,2</sub> |  | 4.2<br><sub>8,6,4,1,1</sub> |  | 1.8<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.4 | 1.8 | 26.4 |
| Jonathan Kuminga | 98% | 28.2<br><sub>33,32,34,25,24</sub> | 14.2<br><sub>8,16,17,4,14</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>10,8,8,0,8</sub> |  | 2.5<br><sub>3,5,4,0,5</sub> |  | 1.4<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.6 | 1.5 | 22.5 |
| Rudy Gobert | 98% | 28.0<br><sub>31,33,25,31,23</sub> | 9.2<br><sub>10,8,8,10,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 11.0<br><sub>10,11,11,15,6</sub> |  | 1.6<br><sub>1,2,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.3 | 21.8 |
| LaMelo Ball | 98% | 27.9<br><sub>33,31,35,30,25</sub> | 21.7<br><sub>34,20,22,24,22</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>6,2,2,3,3</sub> |  | 6.7<br><sub>3,6,8,5,9</sub> |  | 3.8<br><sub>6,4,3,4,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.5 | 0.2 | 3.1 | 32.4 |
| Terrence Shannon Jr. | 98% | 21.3<br><sub>-,-,-,18,21</sub> | 11.7<br><sub>-,-,-,5,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>-,-,-,3,2</sub> |  | 2.3<br><sub>-,-,-,3,4</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.1 | 1.2 | 16.8 |
| Trey Lyles | 98% | 18.9<br><sub>21,20,29,21,15</sub> | 6.6<br><sub>12,5,5,9,2</sub> |  | 4.3<br><sub>4,2,13,6,0</sub> |  | 1.1<br><sub>0,0,2,2,0</sub> |  | 0.8<br><sub>2,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 12.0 |
| Jaylen Clark | 91% | 18.4<br><sub>21,25,21,19,19</sub> | 6.3<br><sub>4,10,8,3,7</sub> |  | 2.5<br><sub>2,4,3,2,6</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.3 | 0.5 | 10.1 |
| Bones Hyland | 98% | 16.2<br><sub>14,16,10,13,23</sub> | 10.7<br><sub>10,19,4,14,24</sub> |  | 1.9<br><sub>1,2,1,2,3</sub> |  | 3.2<br><sub>3,4,0,2,8</sub> |  | 1.6<br><sub>2,4,1,1,5</sub> |  | 0.8 | 0.3 | 1.2 | 15.8 |
| Joan Beringer | 97% | 15.6<br><sub>14,13,7,16,22</sub> | 7.4<br><sub>2,4,2,4,13</sub> |  | 5.7<br><sub>7,7,3,3,9</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 13.7 |
| Cody Williams | 58% | 6.7<br><sub>7,-,-,2,7</sub> | 0.3<br><sub>0,-,-,0,0</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 1.8 |
| Rocco Zikarsky | 48% | 6.5<br><sub>-,-,-,2,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 2.1<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 5.0 |
| Isaiah Evans | 52% | 6.3<br><sub>-,-,-,2,8</sub> | 6.6<br><sub>-,-,-,0,2</sub> |  | 1.1<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 8.2 |
| Zyon Pullin | 38% | 6.3<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Johni Broome | 5% | 4.9 | 1.9 |  | 1.3 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.2 | 3.6 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 29.8<br><sub>25,32,27,34,25</sub> | 13.2<br><sub>13,13,10,19,9</sub> |  | 6.9<br><sub>4,4,1,7,2</sub> |  | 8.0<br><sub>5,10,6,15,7</sub> |  | 1.3<br><sub>2,2,1,1,1</sub> |  | 1.0 | 0.5 | 3.1 | 28.1 |
| Norman Powell (CHI) | 98% | 29.6<br><sub>31,29,22,-,-</sub> | 18.8<br><sub>16,18,12,-,-</sub> |  | 3.4<br><sub>2,3,1,-,-</sub> |  | 2.0<br><sub>3,0,1,-,-</sub> |  | 2.1<br><sub>1,1,0,-,-</sub> |  | 1.1 | 0.3 | 2.1 | 24.2 |
| Matas Buzelis (CHI) | 98% | 29.1<br><sub>20,23,26,31,31</sub> | 15.0<br><sub>14,4,12,19,13</sub> |  | 5.6<br><sub>5,3,5,5,3</sub> |  | 2.0<br><sub>1,2,3,2,2</sub> |  | 1.8<br><sub>2,0,1,3,3</sub> |  | 0.8 | 1.3 | 2.4 | 22.6 |
| Jalen Smith (CHI) | 100% | 26.8<br><sub>27,28,7,30,30</sub> | 12.9<br><sub>5,13,3,17,23</sub> |  | 8.2<br><sub>12,7,2,8,4</sub> |  | 1.6<br><sub>1,4,0,2,3</sub> |  | 1.5<br><sub>0,1,1,2,5</sub> |  | 0.6 | 1.1 | 1.2 | 22.7 |
| Patrick Williams (CHI) | 64% | 24.4<br><sub>-,-,20,25,28</sub> | 7.5<br><sub>-,-,4,7,9</sub> |  | 3.5<br><sub>-,-,0,3,7</sub> |  | 1.8<br><sub>-,-,2,3,4</sub> |  | 0.9<br><sub>-,-,0,1,0</sub> |  | 0.8 | 0.5 | 1.2 | 12.8 |
| Isaac Okoro (CHI) | 98% | 21.7<br><sub>18,21,15,25,23</sub> | 6.7<br><sub>6,4,6,12,0</sub> |  | 2.2<br><sub>3,1,1,2,2</sub> |  | 1.3<br><sub>2,0,0,1,4</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.4 | 0.8 | 10.2 |
| Tre Jones (CHI) | 98% | 21.5<br><sub>20,19,18,14,28</sub> | 11.6<br><sub>12,8,14,6,13</sub> |  | 2.9<br><sub>4,3,3,1,1</sub> |  | 3.6<br><sub>4,3,4,1,3</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 1.0 | 0.2 | 1.4 | 18.2 |
| Nic Claxton (CHI) | 97% | 17.7<br><sub>-,-,-,18,16</sub> | 7.3<br><sub>-,-,-,4,17</sub> |  | 4.8<br><sub>-,-,-,4,6</sub> |  | 2.0<br><sub>-,-,-,4,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.9 | 1.0 | 14.1 |
| Jordan Hawkins (CHI) | 86% | 14.0<br><sub>6,2,7,17,24</sub> | 5.5<br><sub>0,2,2,9,7</sub> |  | 1.9<br><sub>0,0,1,0,4</sub> |  | 0.8<br><sub>0,0,0,1,2</sub> |  | 0.6<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.3 | 0.8 | 8.2 |
| Noa Essengue (CHI) | 96% | 13.0<br><sub>16,14,14,15,11</sub> | 5.4<br><sub>10,8,6,10,8</sub> |  | 3.3<br><sub>4,6,3,7,4</sub> |  | 0.6<br><sub>0,0,0,1,3</sub> |  | 0.4<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.7 | 9.3 |
| Leonard Miller (CHI) | 80% | 11.9<br><sub>11,9,19,-,2</sub> | 5.4<br><sub>2,2,4,-,0</sub> |  | 3.0<br><sub>2,3,6,-,0</sub> |  | 0.6<br><sub>1,0,3,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.6 | 9.0 |
| Buddy Hield (CHI) | 58% | 10.9<br><sub>17,12,8,-,-</sub> | 4.6<br><sub>5,6,7,-,-</sub> |  | 1.6<br><sub>3,1,1,-,-</sub> |  | 1.0<br><sub>1,3,1,-,-</sub> |  | 0.5<br><sub>1,1,1,-,-</sub> |  | 0.5 | 0.1 | 0.6 | 7.1 |
| Zach Collins (CHI) | 86% | 10.0<br><sub>2,10,14,-,3</sub> | 4.1<br><sub>0,2,3,-,2</sub> |  | 3.1<br><sub>0,3,1,-,2</sub> |  | 0.9<br><sub>0,0,3,-,1</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.1 |
| Orlando Robinson (CHI) | 8% | 8.2 | 3.0 |  | 2.4 |  | 0.9 |  | 0.1 |  | 0.2 | 0.2 | 0.5 | 6.3 |
| Jaylin Sellers (CHI) | 76% | 6.8<br><sub>3,2,14,-,2</sub> | 3.3<br><sub>3,3,14,-,3</sub> |  | 0.9<br><sub>0,0,3,-,0</sub> |  | 0.9<br><sub>1,0,1,-,3</sub> |  | 0.3<br><sub>1,0,4,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.1 |
| Jaden McDaniels (MIN) | 98% | 31.8<br><sub>29,37,40,33,25</sub> | 17.5<br><sub>13,14,23,16,16</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,8,6,6,9</sub> |  | 3.3<br><sub>3,4,5,3,3</sub> |  | 1.4<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.0 | 1.7 | 26.2 |
| Ayo Dosunmu (MIN) | 98% | 30.3<br><sub>37,34,39,30,27</sub> | 18.1<br><sub>19,21,26,26,18</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>12,1,2,4,2</sub> |  | 4.2<br><sub>8,6,4,1,1</sub> |  | 1.8<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.4 | 1.8 | 26.6 |
| Jonathan Kuminga (MIN) | 98% | 28.2<br><sub>33,32,34,25,24</sub> | 14.3<br><sub>8,16,17,4,14</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>10,8,8,0,8</sub> |  | 2.5<br><sub>3,5,4,0,5</sub> |  | 1.4<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.6 | 1.5 | 22.4 |
| Rudy Gobert (MIN) | 98% | 28.0<br><sub>31,33,25,31,23</sub> | 9.3<br><sub>10,8,8,10,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 11.0<br><sub>10,11,11,15,6</sub> |  | 1.6<br><sub>1,2,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.3 | 21.8 |
| LaMelo Ball (MIN) | 98% | 27.9<br><sub>33,31,35,30,25</sub> | 21.5<br><sub>34,20,22,24,22</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>6,2,2,3,3</sub> |  | 6.7<br><sub>3,6,8,5,9</sub> |  | 3.8<br><sub>6,4,3,4,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.5 | 0.2 | 3.1 | 32.3 |
| Terrence Shannon Jr. (MIN) | 98% | 21.3<br><sub>-,-,-,18,21</sub> | 11.7<br><sub>-,-,-,5,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>-,-,-,3,2</sub> |  | 2.3<br><sub>-,-,-,3,4</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.1 | 1.2 | 16.7 |
| Trey Lyles (MIN) | 98% | 18.9<br><sub>21,20,29,21,15</sub> | 6.6<br><sub>12,5,5,9,2</sub> |  | 4.3<br><sub>4,2,13,6,0</sub> |  | 1.1<br><sub>0,0,2,2,0</sub> |  | 0.8<br><sub>2,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 12.0 |
| Jaylen Clark (MIN) | 91% | 18.4<br><sub>21,25,21,19,19</sub> | 6.3<br><sub>4,10,8,3,7</sub> |  | 2.5<br><sub>2,4,3,2,6</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.3 | 0.5 | 10.1 |
| Bones Hyland (MIN) | 98% | 16.2<br><sub>14,16,10,13,23</sub> | 10.6<br><sub>10,19,4,14,24</sub> |  | 1.9<br><sub>1,2,1,2,3</sub> |  | 3.2<br><sub>3,4,0,2,8</sub> |  | 1.5<br><sub>2,4,1,1,5</sub> |  | 0.8 | 0.3 | 1.1 | 15.7 |
| Joan Beringer (MIN) | 97% | 15.6<br><sub>14,13,7,16,22</sub> | 7.4<br><sub>2,4,2,4,13</sub> |  | 5.7<br><sub>7,7,3,3,9</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 13.7 |
| Cody Williams (MIN) | 58% | 6.7<br><sub>7,-,-,2,7</sub> | 0.3<br><sub>0,-,-,0,0</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 1.8 |
| Rocco Zikarsky (MIN) | 48% | 6.6<br><sub>-,-,-,2,-</sub> | 2.5<br><sub>-,-,-,0,-</sub> |  | 2.1<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 5.0 |
| Zyon Pullin (MIN) | 38% | 6.3<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Isaiah Evans (MIN) | 52% | 6.2<br><sub>-,-,-,2,8</sub> | 6.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 8.2 |
| Johni Broome (MIN) | 5% | 4.7 | 1.8 |  | 1.2 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-14/`._
