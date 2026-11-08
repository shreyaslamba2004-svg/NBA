# NBA model · Sun 08 Nov 2026 (US date)

Updated **Sun 08 Nov, 05:49 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-08/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| LAL to win | LAL @ DET | draftkings | 2.55 | 2.16 | 2.40 | 41.6% | 46.3% | 46.3% | +18.1% | +6.2% | 2.0% |

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
| PHI @ CHI | Mon 09 Nov 07:30 | 118.3–110.5 | PHI 71% | 1.41 / 3.43 | CHI +7.5 | 228.5 | CHI +9.5 covers 55%; o238.5 30% |
| LAL @ DET | Mon 09 Nov 10:00 | 108.8–112.7 | LAL 39% | 2.58 / 1.63 | DET -4.5 | 221.5 | DET -4.5 covers 49%; o222.5 47% |
| UTA @ MIN | Mon 09 Nov 11:00 | 107.9–121.9 | UTA 16% | 6.21 / 1.19 | MIN -13.5 | 229.5 | MIN -11.5 covers 57%; o224.5 61% |
| BKN @ DAL | Mon 09 Nov 11:30 | 107.7–117.0 | BKN 26% | 3.88 / 1.35 | DAL -9.5 | 224.5 | DAL -9.5 covers 49%; o219.5 61% |
| BOS @ MIL | Mon 09 Nov 12:00 | 117.0–104.8 | BOS 81% | 1.23 / 5.26 | MIL +12.5 | 221.5 | MIL +12.5 covers 51%; o222.5 48% |
| NOP @ LAC | Mon 09 Nov 13:00 | 116.3–117.5 | NOP 47% | 2.14 / 1.88 | LAC -1.5 | 233.5 | LAC +1.5 covers 56%; o228.5 61% |
| MIA @ SAC | Mon 09 Nov 13:00 | 124.5–117.5 | MIA 69% | 1.45 / 3.24 | SAC +7.5 | 241.5 | SAC +8.5 covers 54%; o238.5 57% |

### PHI @ CHI
Out: Zach Collins (CHI), Jaylin Sellers (CHI), Dailyn Swain (CHI), Dominick Barlow (PHI), Adem Bona (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.3–110.5 | PHI 71% | 1.41 / 3.43 | CHI +7.5 | 228.5 | CHI +9.5 covers 55%; o238.5 30% |
| Expected (weighted by chance each plays) | 118.4–110.5 | PHI 71% | 1.41 / 3.43 | CHI +7.5 | 228.5 | CHI +9.5 covers 55%; o238.5 30% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tobe Awaka (CHI) | Questionable | 55% | 7.4 | 2.4 | 2.9 | 0.4 | 0.0 | 0.2 | 0.5 | 0.4 | 5.7 | small |
| Nic Claxton (CHI) | Questionable | 55% | 16.4 | 6.1 | 4.3 | 1.8 | 0.1 | 0.3 | 0.8 | 0.9 | 12.2 | small |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 37.7<br><sub>38,38,36,34,32</sub> | 25.1<br><sub>27,38,26,19,17</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,4,4,1,3</sub> |  | 5.9<br><sub>4,4,11,7,4</sub> |  | 2.9<br><sub>3,4,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.6 | 2.4 | 35.2 |
| Jaylen Brown | 98% | 36.2<br><sub>-,38,33,37,34</sub> | 24.0<br><sub>-,16,25,30,20</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>-,4,11,7,5</sub> |  | 4.4<br><sub>-,4,5,1,5</sub> |  | 2.2<br><sub>-,0,4,3,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.6 | 3.0 | 35.0 |
| LeBron James | 98% | 34.5<br><sub>34,-,31,33,32</sub> | 18.5<br><sub>20,-,15,13,8</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 7.1<br><sub>9,-,7,10,7</sub> |  | 7.1<br><sub>8,-,9,8,3</sub> |  | 1.3<br><sub>2,-,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.7 | 2.7 | 32.7 |
| VJ Edgecombe | 91% | 34.0<br><sub>36,37,33,35,32</sub> | 13.5<br><sub>13,10,21,11,19</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>8,8,3,6,3</sub> |  | 3.5<br><sub>2,3,5,3,2</sub> |  | 1.9<br><sub>1,2,2,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.5 | 1.4 | 22.9 |
| Joel Embiid | 91% | 33.3<br><sub>33,-,25,33,25</sub> | 24.1<br><sub>10,-,15,26,6</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 9.3<br><sub>7,-,8,15,7</sub> |  | 4.2<br><sub>7,-,3,2,1</sub> |  | 1.2<br><sub>0,-,0,0,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 1.2 | 2.8 | 37.6 |
| Dean Wade | 93% | 21.1<br><sub>27,30,23,22,21</sub> | 3.7<br><sub>0,4,8,3,0</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,5,2,5,5</sub> |  | 1.2<br><sub>1,10,1,1,1</sub> |  | 0.4<br><sub>0,0,2,0,0</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.3 | 0.5 | 8.4 |
| Anfernee Simons | 98% | 20.5<br><sub>31,25,24,10,19</sub> | 9.1<br><sub>21,19,6,0,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,0,2,1,2</sub> |  | 1.5<br><sub>1,2,1,0,2</sub> |  | 1.6<br><sub>5,5,1,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.7 | 0.1 | 0.8 | 12.6 |
| Kentavious Caldwell-Pope | 98% | 17.7<br><sub>21,18,13,21,17</sub> | 4.5<br><sub>5,3,3,5,5</sub> |  | 1.9<br><sub>3,2,1,1,2</sub> |  | 1.1<br><sub>3,1,0,0,0</sub> |  | 0.6<br><sub>1,1,1,1,1</sub> |  | 0.7 | 0.2 | 0.5 | 7.5 |
| Jabari Walker | 76% | 10.9<br><sub>-,19,2,-,17</sub> | 4.3<br><sub>-,12,0,-,8</sub> |  | 2.8<br><sub>-,6,0,-,5</sub> |  | 0.5<br><sub>-,0,1,-,1</sub> |  | 0.3<br><sub>-,1,0,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.6 |
| Justin Edwards | 58% | 6.6<br><sub>-,2,2,-,4</sub> | 2.6<br><sub>-,0,2,-,3</sub> |  | 0.9<br><sub>-,1,1,-,1</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.3 | 0.1 | 0.2 | 3.9 |
| Tacko Fall | 58% | 6.6<br><sub>-,-,-,-,3</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.7<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.4 | 0.3 | 2.4 |
| Caleb Love | 35% | 6.5<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 0.9 |
| Rayan Rupert | 43% | 6.3<br><sub>-,-,2,-,-</sub> | 2.3<br><sub>-,-,2,-,-</sub> |  | 1.2<br><sub>-,-,2,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.0 |
| Labaron Philon Jr. | 66% | 6.0<br><sub>6,10,2,-,4</sub> | 2.3<br><sub>2,5,0,-,3</sub> |  | 0.8<br><sub>2,1,0,-,1</sub> |  | 0.4<br><sub>0,0,0,-,1</sub> |  | 0.2<br><sub>0,1,0,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 3.5 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson | 97% | 34.4<br><sub>32,38,31,34,22</sub> | 19.9<br><sub>17,20,23,24,5</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>5,6,5,7,5</sub> |  | 3.0<br><sub>3,4,4,4,0</sub> |  | 2.3<br><sub>1,3,6,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 1.1 | 2.9 | 29.9 |
| Norman Powell | 98% | 31.0<br><sub>24,37,31,29,22</sub> | 18.8<br><sub>20,30,16,18,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>1,2,2,3,1</sub> |  | 2.4<br><sub>2,2,3,0,1</sub> |  | 2.1<br><sub>4,4,1,1,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 2.3 | 24.6 |
| Josh Giddey | 98% | 30.6<br><sub>24,31,25,32,27</sub> | 13.1<br><sub>11,10,13,13,10</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>1,8,4,4,1</sub> |  | 8.7<br><sub>4,11,5,10,6</sub> |  | 1.4<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.6 | 2.9 | 28.8 |
| Matas Buzelis | 98% | 27.8<br><sub>22,33,20,23,26</sub> | 14.7<br><sub>11,17,14,4,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>1,5,5,3,5</sub> |  | 2.2<br><sub>2,3,1,2,3</sub> |  | 1.8<br><sub>2,3,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 1.4 | 2.4 | 22.6 |
| Jalen Smith | 91% | 22.7<br><sub>20,30,27,28,7</sub> | 10.2<br><sub>7,17,5,13,3</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>6,11,12,7,2</sub> |  | 1.5<br><sub>1,5,1,4,0</sub> |  | 1.4<br><sub>2,3,0,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5 | 0.8 | 1.0 | 19.1 |
| Tre Jones | 98% | 20.1<br><sub>15,18,20,19,18</sub> | 10.5<br><sub>8,11,12,8,14</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>1,4,4,3,3</sub> |  | 3.9<br><sub>0,3,4,3,4</sub> |  | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.8 | 0.2 | 1.3 | 17.3 |
| Isaac Okoro | 98% | 18.9<br><sub>11,18,18,21,15</sub> | 6.0<br><sub>1,7,6,4,6</sub> |  | 2.0<br><sub>1,0,3,1,1</sub> |  | 1.2<br><sub>4,1,2,0,0</sub> |  | 0.5<br><sub>0,1,1,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 9.1 |
| Patrick Williams | 52% | 18.8<br><sub>-,-,-,-,20</sub> | 6.0<br><sub>-,-,-,-,4</sub> |  | 2.9<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.4 | 1.1 | 10.3 |
| Leonard Miller | 98% | 16.2<br><sub>14,17,11,9,19</sub> | 7.3<br><sub>9,10,2,2,4</sub> |  | 4.2<br><sub>9,0,2,3,6</sub> |  | 0.9<br><sub>0,1,1,0,3</sub> |  | 0.7<br><sub>1,1,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 12.4 |
| Noa Essengue | 91% | 13.4<br><sub>16,10,16,14,14</sub> | 5.0<br><sub>0,3,10,8,6</sub> |  | 2.8<br><sub>4,0,4,6,3</sub> |  | 0.5<br><sub>0,1,0,0,0</sub> |  | 0.4<br><sub>0,1,1,1,0</sub> |  | 0.5 | 0.3 | 0.8 | 8.2 |
| Buddy Hield | 93% | 13.2<br><sub>13,9,17,12,8</sub> | 5.4<br><sub>3,2,5,6,7</sub> |  | 1.9<br><sub>0,3,3,1,1</sub> |  | 1.2<br><sub>1,1,1,3,1</sub> |  | 0.7<br><sub>1,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.8 | 8.6 |
| Jordan Hawkins | 72% | 7.7<br><sub>7,-,6,2,7</sub> | 3.0<br><sub>4,-,0,2,2</sub> |  | 1.1<br><sub>1,-,0,0,1</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.7 |

</details>


### LAL @ DET
Out: Jalen Duren (DET), Isaiah Joe (DET)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.8–112.7 | LAL 39% | 2.58 / 1.63 | DET -4.5 | 221.5 | DET -4.5 covers 49%; o222.5 47% |
| Expected (weighted by chance each plays) | 109.9–113.0 | LAL 42% | 2.40 / 1.71 | DET -3.5 | 222.5 | DET -4.5 covers 46%; o222.5 51% |
| if Luka Doncic plays | 110.8–113.5 | LAL 42% | 2.36 / 1.74 | DET -2.5 | 224.5 | DET -4.5 covers 45%; o222.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | Questionable | 55% | 35.5 | 31.5 | 7.1 | 7.0 | 4.1 | 1.8 | 0.5 | 3.9 | 45.6 | full tables below |
| Elijah Harkless (DET) | Questionable | 55% | 6.8 | 0.4 | 0.2 | 0.4 | 0.0 | 0.1 | 0.2 | 0.3 | 1.0 | small |
| Isaac Jones (DET) | Questionable | 55% | 6.1 | 3.1 | 1.3 | 0.3 | 0.1 | 0.2 | 0.5 | 0.3 | 4.7 | small |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Austin Reaves | 98% | 37.6<br><sub>37,39,34,37,38</sub> | 25.4<br><sub>21,19,27,21,25</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>4,3,2,3,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.5<br><sub>5,4,5,4,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,2,4,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.6 | 3.8 | 35.1 |
| Walker Kessler | 98% | 32.6<br><sub>31,31,32,29,37</sub> | 12.8<br><sub>10,16,15,15,16</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 10.8<br><sub>13,15,15,8,12</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>2,1,2,0,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.7 | 2.2 | 25.3 |
| Quentin Grimes | 98% | 26.0<br><sub>26,26,23,25,20</sub> | 9.9<br><sub>3,7,7,6,2</sub> |  | 2.8<br><sub>3,1,4,1,0</sub> |  | 2.3<br><sub>2,3,4,1,0</sub> |  | 1.1<br><sub>1,1,1,0,0</sub> |  | 0.9 | 0.3 | 1.4 | 15.0 |
| Matisse Thybulle | 98% | 25.1<br><sub>28,25,19,23,24</sub> | 7.5<br><sub>10,6,6,3,2</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,2,1,1,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>0,3,2,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2<br><sub>1,2,2,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.9 | 0.9 | 1.2 | 11.2 |
| Ziaire Williams | 97% | 24.0<br><sub>-,-,15,23,20</sub> | 10.0<br><sub>-,-,9,10,8</sub> |  | 2.9<br><sub>-,-,2,4,3</sub> |  | 1.4<br><sub>-,-,2,1,1</sub> |  | 1.3<br><sub>-,-,3,1,2</sub> |  | 1.4 | 0.3 | 1.2 | 14.2 |
| Jake LaRavia | 97% | 23.5<br><sub>28,25,26,21,25</sub> | 6.9<br><sub>10,8,7,9,7</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>2,2,4,2,8</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,4,2,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>2,2,1,2,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.3 | 0.8 | 1.4 | 12.2 |
| Sandro Mamukelashvili | 98% | 22.9<br><sub>20,24,28,19,20</sub> | 10.3<br><sub>4,11,13,2,7</sub> |  | 4.8<br><sub>7,1,3,6,3</sub> |  | 1.6<br><sub>0,1,4,1,1</sub> |  | 1.2<br><sub>0,2,2,0,1</sub> |  | 0.9 | 0.6 | 1.1 | 16.8 |
| Collin Sexton | 98% | 18.9<br><sub>16,19,16,16,11</sub> | 11.7<br><sub>0,14,6,10,0</sub> |  | 2.0<br><sub>2,3,1,3,0</sub> |  | 2.1<br><sub>1,3,5,1,1</sub> |  | 1.1<br><sub>0,1,0,1,0</sub> |  | 0.8 | 0.2 | 1.6 | 15.7 |
| Jarred Vanderbilt | 63% | 11.8<br><sub>13,12,6,7,-</sub> | 2.9<br><sub>0,4,2,0,-</sub> |  | 3.0<br><sub>3,3,1,1,-</sub> |  | 0.9<br><sub>3,1,0,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.6 | 0.2 | 0.6 | 6.8 |
| Lawson Lovering | 63% | 9.9<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,1,0,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.3 | 0.5 | 6.0 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Adou Thiero | 83% | 8.6<br><sub>-,-,-,-,7</sub> | 3.2<br><sub>-,-,-,-,4</sub> |  | 2.3<br><sub>-,-,-,-,4</sub> |  | 0.6<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 6.1 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Jaden Hardy | 64% | 7.5<br><sub>1,1,1,1,-</sub> | 4.3<br><sub>0,1,2,0,-</sub> |  | 0.7<br><sub>1,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,1,-</sub> |  | 0.4<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.5 |
| Kevon Looney | 35% | 7.3<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |
| Chris Manon | 58% | 6.6<br><sub>1,-,-,-,-</sub> | 1.7<br><sub>0,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.2 |
| Cameron Carr | 91% | 6.1<br><sub>-,1,1,1,-</sub> | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.2 | 1.1 |
| Bronny James | 66% | 6.1<br><sub>1,2,1,1,-</sub> | 2.5<br><sub>0,0,2,0,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.2 |

</details>

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 35.2<br><sub>36,39,28,27,40</sub> | 25.1<br><sub>19,30,20,33,26</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>9,5,5,5,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 8.6<br><sub>8,7,4,7,11</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>2,4,1,4,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.8 | 4.4 | 38.8 |
| Duncan Robinson | 98% | 31.9<br><sub>33,32,26,32,37</sub> | 15.8<br><sub>12,13,17,24,27</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>0,2,4,2,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>2,2,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 3.0<br><sub>2,3,2,6,7</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.2 | 1.3 | 20.9 |
| Ausar Thompson | 98% | 29.7<br><sub>25,29,26,26,34</sub> | 10.7<br><sub>11,7,11,14,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>6,9,8,6,17</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>2,8,6,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.0 | 0.9 | 2.0 | 22.2 |
| Paul Reed | 96% | 28.3<br><sub>26,38,31,28,30</sub> | 14.6<br><sub>22,16,12,11,8</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>9,4,4,5,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,0,1,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.5<br><sub>1,2,0,0,0</sub> | 0.5<br><sub>o 36% · u 64%</sub> | 1.8 | 1.1 | 1.9 | 25.0 |
| John Collins | 98% | 26.4<br><sub>27,18,26,19,26</sub> | 10.8<br><sub>2,4,4,4,16</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>9,2,9,3,1</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>1,0,0,1,0</sub> |  | 1.0<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 0.7 | 1.3 | 17.6 |
| Daniss Jenkins | 98% | 24.9<br><sub>24,24,24,23,21</sub> | 10.4<br><sub>11,14,6,2,5</sub> |  | 3.0<br><sub>3,2,3,1,1</sub> |  | 4.5<br><sub>2,3,5,7,4</sub> |  | 1.2<br><sub>1,2,2,0,1</sub> |  | 0.9 | 0.2 | 1.7 | 17.8 |
| Kevin Huerter | 96% | 21.9<br><sub>16,19,24,20,20</sub> | 8.5<br><sub>7,3,8,9,8</sub> |  | 2.8<br><sub>1,2,1,2,1</sub> |  | 2.3<br><sub>0,3,3,3,0</sub> |  | 1.3<br><sub>1,1,2,3,2</sub> |  | 1.0 | 0.3 | 0.9 | 13.6 |
| Javonte Green | 96% | 18.7<br><sub>17,21,22,20,15</sub> | 6.5<br><sub>3,7,6,5,1</sub> |  | 2.8<br><sub>1,2,3,2,3</sub> |  | 0.8<br><sub>0,2,1,0,1</sub> |  | 1.0<br><sub>1,1,1,1,0</sub> |  | 1.2 | 0.4 | 0.5 | 10.0 |
| Ronald Holland II | 97% | 16.5<br><sub>12,12,22,20,12</sub> | 6.6<br><sub>4,0,18,11,3</sub> |  | 3.2<br><sub>3,2,3,2,2</sub> |  | 1.0<br><sub>2,1,2,0,0</sub> |  | 0.6<br><sub>0,0,2,3,1</sub> |  | 1.0 | 0.5 | 1.0 | 10.9 |
| Taurean Prince | 43% | 9.0<br><sub>7,6,-,-,-</sub> | 3.1<br><sub>3,1,-,-,-</sub> |  | 1.3<br><sub>0,2,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>1,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Tolu Smith | 88% | 6.7<br><sub>6,1,3,8,5</sub> | 2.5<br><sub>1,2,2,0,1</sub> |  | 2.2<br><sub>4,1,1,2,1</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 5.0 |
| Chaz Lanier | 52% | 6.2<br><sub>2,-,3,7,-</sub> | 2.6<br><sub>2,-,6,5,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.3<br><sub>0,-,2,1,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.6 |
| Ebuka Okorie | 58% | 5.6<br><sub>4,-,3,6,-</sub> | 2.1<br><sub>0,-,0,4,-</sub> |  | 0.7<br><sub>0,-,0,2,-</sub> |  | 0.6<br><sub>2,-,0,1,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |

</details>

<details><summary>if Luka Doncic plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | 98% | 35.2<br><sub>36,39,28,27,40</sub> | 25.4<br><sub>19,30,20,33,26</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>9,5,5,5,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 8.6<br><sub>8,7,4,7,11</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>2,4,1,4,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.8 | 4.4 | 39.1 |
| Duncan Robinson (DET) | 98% | 32.0<br><sub>33,32,26,32,37</sub> | 15.9<br><sub>12,13,17,24,27</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>0,2,4,2,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>2,2,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 3.0<br><sub>2,3,2,6,7</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.3 | 1.3 | 21.0 |
| Ausar Thompson (DET) | 98% | 29.6<br><sub>25,29,26,26,34</sub> | 10.7<br><sub>11,7,11,14,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>6,9,8,6,17</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>2,8,6,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.0 | 0.9 | 2.0 | 22.2 |
| Paul Reed (DET) | 96% | 28.3<br><sub>26,38,31,28,30</sub> | 14.7<br><sub>22,16,12,11,8</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>9,4,4,5,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,0,1,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.5<br><sub>1,2,0,0,0</sub> | 0.5<br><sub>o 36% · u 64%</sub> | 1.8 | 1.1 | 1.9 | 25.0 |
| John Collins (DET) | 98% | 26.4<br><sub>27,18,26,19,26</sub> | 11.0<br><sub>2,4,4,4,16</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>9,2,9,3,1</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>1,0,0,1,0</sub> |  | 1.0<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 0.7 | 1.3 | 17.8 |
| Daniss Jenkins (DET) | 98% | 24.8<br><sub>24,24,24,23,21</sub> | 10.4<br><sub>11,14,6,2,5</sub> |  | 3.0<br><sub>3,2,3,1,1</sub> |  | 4.5<br><sub>2,3,5,7,4</sub> |  | 1.2<br><sub>1,2,2,0,1</sub> |  | 0.9 | 0.2 | 1.7 | 17.9 |
| Kevin Huerter (DET) | 96% | 21.9<br><sub>16,19,24,20,20</sub> | 8.5<br><sub>7,3,8,9,8</sub> |  | 2.9<br><sub>1,2,1,2,1</sub> |  | 2.3<br><sub>0,3,3,3,0</sub> |  | 1.3<br><sub>1,1,2,3,2</sub> |  | 1.0 | 0.3 | 1.0 | 13.6 |
| Javonte Green (DET) | 96% | 18.7<br><sub>17,21,22,20,15</sub> | 6.5<br><sub>3,7,6,5,1</sub> |  | 2.8<br><sub>1,2,3,2,3</sub> |  | 0.8<br><sub>0,2,1,0,1</sub> |  | 1.0<br><sub>1,1,1,1,0</sub> |  | 1.2 | 0.4 | 0.5 | 10.0 |
| Ronald Holland II (DET) | 97% | 16.4<br><sub>12,12,22,20,12</sub> | 6.6<br><sub>4,0,18,11,3</sub> |  | 3.3<br><sub>3,2,3,2,2</sub> |  | 1.1<br><sub>2,1,2,0,0</sub> |  | 0.6<br><sub>0,0,2,3,1</sub> |  | 0.9 | 0.5 | 1.0 | 10.9 |
| Taurean Prince (DET) | 43% | 8.9<br><sub>7,6,-,-,-</sub> | 3.1<br><sub>3,1,-,-,-</sub> |  | 1.2<br><sub>0,2,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>1,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Tolu Smith (DET) | 88% | 6.6<br><sub>6,1,3,8,5</sub> | 2.5<br><sub>1,2,2,0,1</sub> |  | 2.1<br><sub>4,1,1,2,1</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 5.0 |
| Chaz Lanier (DET) | 52% | 6.2<br><sub>2,-,3,7,-</sub> | 2.5<br><sub>2,-,6,5,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.3<br><sub>0,-,2,1,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.5 |
| Ebuka Okorie (DET) | 58% | 5.6<br><sub>4,-,3,6,-</sub> | 2.1<br><sub>0,-,0,4,-</sub> |  | 0.7<br><sub>0,-,0,2,-</sub> |  | 0.6<br><sub>2,-,0,1,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.5 |
| Luka Doncic (LAL) | 100% | 35.5<br><sub>37,35,36,35,38</sub> | 31.5<br><sub>37,45,42,40,53</sub> | 33.5 · – | 7.1<br><sub>7,15,7,9,5</sub> | 7.5 | 7.0<br><sub>5,6,13,7,5</sub> | 6.5 | 4.1<br><sub>6,8,6,6,5</sub> | 4.5 | 1.8 | 0.5 | 3.9 | 45.6 |
| Austin Reaves (LAL) | 98% | 35.0<br><sub>37,39,34,37,38</sub> | 19.6<br><sub>21,19,27,21,25</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,3,2,3,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.3<br><sub>5,4,5,4,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>1,2,4,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.5 | 3.2 | 27.6 |
| Walker Kessler (LAL) | 98% | 29.1<br><sub>31,31,32,29,37</sub> | 10.6<br><sub>10,16,15,15,16</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 9.6<br><sub>13,15,15,8,12</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>2,1,2,0,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.4 | 1.7 | 21.4 |
| Quentin Grimes (LAL) | 98% | 21.8<br><sub>26,26,23,25,20</sub> | 7.1<br><sub>3,7,7,6,2</sub> |  | 2.3<br><sub>3,1,4,1,0</sub> |  | 1.5<br><sub>2,3,4,1,0</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.3 | 1.1 | 10.9 |
| Jake LaRavia (LAL) | 97% | 20.7<br><sub>28,25,26,21,25</sub> | 5.4<br><sub>10,8,7,9,7</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>2,2,4,2,8</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>0,4,2,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6<br><sub>2,2,1,2,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.7 | 1.1 | 9.8 |
| Ziaire Williams (LAL) | 97% | 20.1<br><sub>-,-,15,23,20</sub> | 7.6<br><sub>-,-,9,10,8</sub> |  | 2.2<br><sub>-,-,2,4,3</sub> |  | 0.9<br><sub>-,-,2,1,1</sub> |  | 1.0<br><sub>-,-,3,1,2</sub> |  | 1.2 | 0.3 | 0.9 | 10.7 |
| Matisse Thybulle (LAL) | 98% | 20.0<br><sub>28,25,19,23,24</sub> | 5.5<br><sub>10,6,6,3,2</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>3,2,1,1,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8<br><sub>0,3,2,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>1,2,2,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.7 | 0.8 | 8.1 |
| Sandro Mamukelashvili (LAL) | 98% | 19.8<br><sub>20,24,28,19,20</sub> | 7.8<br><sub>4,11,13,2,7</sub> |  | 4.1<br><sub>7,1,3,6,3</sub> |  | 1.2<br><sub>0,1,4,1,1</sub> |  | 0.9<br><sub>0,2,2,0,1</sub> |  | 0.7 | 0.5 | 0.9 | 13.1 |
| Collin Sexton (LAL) | 98% | 14.5<br><sub>16,19,16,16,11</sub> | 7.9<br><sub>0,14,6,10,0</sub> |  | 1.4<br><sub>2,3,1,3,0</sub> |  | 1.4<br><sub>1,3,5,1,1</sub> |  | 0.7<br><sub>0,1,0,1,0</sub> |  | 0.6 | 0.1 | 1.2 | 10.7 |
| AK Okereke (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.1 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Jarred Vanderbilt (LAL) | 63% | 7.9<br><sub>13,12,6,7,-</sub> | 2.0<br><sub>0,4,2,0,-</sub> |  | 2.0<br><sub>3,3,1,1,-</sub> |  | 0.6<br><sub>3,1,0,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.5 |
| Lawson Lovering (LAL) | 63% | 6.3<br><sub>-,-,1,1,-</sub> | 1.7<br><sub>-,-,0,0,-</sub> |  | 1.6<br><sub>-,-,1,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Jaden Hardy (LAL) | 64% | 6.2<br><sub>1,1,1,1,-</sub> | 3.3<br><sub>0,1,2,0,-</sub> |  | 0.6<br><sub>1,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,1,-</sub> |  | 0.3<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.3 |
| Kevon Looney (LAL) | 35% | 6.1<br><sub>-,-,-,-,-</sub> | 1.3<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.9 |
| Adou Thiero (LAL) | 83% | 6.0<br><sub>-,-,-,-,7</sub> | 2.2<br><sub>-,-,-,-,4</sub> |  | 1.6<br><sub>-,-,-,-,4</sub> |  | 0.4<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.3 |
| Cameron Carr (LAL) | 91% | 5.6<br><sub>-,1,1,1,-</sub> | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 1.0 |
| Bronny James (LAL) | 66% | 5.6<br><sub>1,2,1,1,-</sub> | 2.3<br><sub>0,0,2,0,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.9 |
| Chris Manon (LAL) | 58% | 5.3<br><sub>1,-,-,-,-</sub> | 1.4<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 2.6 |

</details>


### UTA @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Jusuf Nurkic (UTA)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.9–121.9 | UTA 16% | 6.21 / 1.19 | MIN -13.5 | 229.5 | MIN -11.5 covers 57%; o224.5 61% |
| Expected (weighted by chance each plays) | 107.8–121.5 | UTA 16% | 6.22 / 1.19 | MIN -13.5 | 229.5 | MIN -11.5 covers 56%; o224.5 60% |
| if Lauri Markkanen plays | 108.1–120.4 | UTA 19% | 5.24 / 1.24 | MIN -12.5 | 228.5 | MIN -11.5 covers 53%; o224.5 59% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Joan Beringer (MIN) | Questionable | 55% | 13.2 | 6.0 | 5.0 | 0.5 | 0.0 | 0.4 | 1.2 | 0.6 | 11.5 | small |
| Lauri Markkanen (UTA) | Questionable | 55% | 31.5 | 20.3 | 6.3 | 1.9 | 2.3 | 0.9 | 0.5 | 1.9 | 28.5 | full tables below |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 33.4<br><sub>37,29,22,44,32</sub> | 23.6<br><sub>31,8,7,39,16</sub> |  | 4.2<br><sub>4,3,7,2,6</sub> |  | 6.2<br><sub>3,4,0,9,9</sub> |  | 2.3<br><sub>5,0,1,2,1</sub> |  | 1.0 | 0.2 | 3.4 | 34.0 |
| Ace Bailey | 98% | 32.6<br><sub>40,37,24,35,29</sub> | 15.4<br><sub>19,9,5,15,12</sub> |  | 6.2<br><sub>6,7,6,5,6</sub> |  | 2.2<br><sub>0,1,2,1,0</sub> |  | 2.0<br><sub>1,1,1,1,0</sub> |  | 0.9 | 1.0 | 2.2 | 23.8 |
| Darryn Peterson | 98% | 32.2<br><sub>26,36,33,30,30</sub> | 15.1<br><sub>18,16,14,7,21</sub> |  | 4.1<br><sub>5,4,4,2,2</sub> |  | 4.5<br><sub>3,4,6,7,5</sub> |  | 1.5<br><sub>3,3,2,0,3</sub> |  | 1.1 | 0.8 | 2.0 | 23.6 |
| Jaxson Hayes | 98% | 26.8<br><sub>37,20,22,21,28</sub> | 9.2<br><sub>2,7,9,2,8</sub> |  | 6.5<br><sub>11,7,5,7,6</sub> |  | 2.0<br><sub>4,2,0,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.6 | 1.3 | 17.6 |
| Josh Okogie | 91% | 23.8<br><sub>28,14,19,26,24</sub> | 5.7<br><sub>5,0,9,3,12</sub> |  | 4.1<br><sub>9,1,3,6,4</sub> |  | 1.2<br><sub>3,0,2,1,0</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 1.1 | 0.4 | 0.9 | 10.9 |
| Josh Green | 88% | 22.3<br><sub>24,2,15,23,24</sub> | 4.7<br><sub>2,0,3,7,3</sub> |  | 2.3<br><sub>2,0,1,1,3</sub> |  | 1.1<br><sub>2,0,0,0,1</sub> |  | 0.6<br><sub>0,0,1,1,1</sub> |  | 0.9 | 0.2 | 0.7 | 8.1 |
| Svi Mykhailiuk | 91% | 18.7<br><sub>15,18,14,17,14</sub> | 7.0<br><sub>3,6,3,6,0</sub> |  | 2.2<br><sub>2,1,2,3,0</sub> |  | 1.3<br><sub>1,3,0,0,1</sub> |  | 1.0<br><sub>1,2,1,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.6 |
| Brice Sensabaugh | 98% | 18.5<br><sub>18,19,14,12,10</sub> | 10.7<br><sub>16,12,7,6,0</sub> |  | 2.8<br><sub>3,3,2,2,2</sub> |  | 1.5<br><sub>1,2,1,0,2</sub> |  | 1.4<br><sub>4,2,1,1,0</sub> |  | 0.6 | 0.1 | 1.5 | 15.0 |
| Isaiah Collier | 98% | 18.5<br><sub>24,20,12,3,13</sub> | 9.2<br><sub>7,8,7,0,4</sub> |  | 2.7<br><sub>7,1,2,1,3</sub> |  | 4.8<br><sub>6,4,2,0,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.2 | 1.8 | 16.7 |
| Mo Bamba | 63% | 16.0<br><sub>16,11,18,15,-</sub> | 5.7<br><sub>8,6,8,7,-</sub> |  | 6.0<br><sub>4,4,8,10,-</sub> |  | 0.7<br><sub>1,0,0,1,-</sub> |  | 0.3<br><sub>0,0,0,0,-</sub> |  | 0.4 | 1.3 | 0.9 | 12.4 |
| Kyle Filipowski | 66% | 14.1<br><sub>-,6,8,-,1</sub> | 6.5<br><sub>-,5,1,-,0</sub> |  | 4.2<br><sub>-,0,2,-,0</sub> |  | 1.5<br><sub>-,2,0,-,0</sub> |  | 0.5<br><sub>-,1,0,-,0</sub> |  | 0.6 | 0.3 | 1.1 | 12.2 |
| Kobe Bufkin | 35% | 13.2<br><sub>-,-,-,-,-</sub> | 5.2<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.8 | 8.6 |
| Tony Bradley | 52% | 10.2<br><sub>-,-,7,-,1</sub> | 3.8<br><sub>-,-,2,-,0</sub> |  | 3.0<br><sub>-,-,3,-,1</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.6 | 7.4 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 33.2<br><sub>33,39,29,37,40</sub> | 18.5<br><sub>23,19,13,14,23</sub> |  | 5.9<br><sub>6,3,6,8,6</sub> |  | 3.3<br><sub>7,3,3,4,5</sub> |  | 1.5<br><sub>1,2,2,0,2</sub> |  | 1.2 | 1.0 | 1.9 | 27.7 |
| Ayo Dosunmu | 98% | 32.2<br><sub>30,38,37,34,39</sub> | 18.2<br><sub>15,27,19,21,26</sub> |  | 4.7<br><sub>7,9,12,1,2</sub> |  | 4.8<br><sub>2,3,8,6,4</sub> |  | 1.8<br><sub>3,2,1,0,4</sub> |  | 1.4 | 0.4 | 2.0 | 27.7 |
| Jonathan Kuminga | 98% | 30.5<br><sub>22,40,33,32,34</sub> | 15.4<br><sub>5,19,8,16,17</sub> |  | 6.1<br><sub>1,6,10,8,8</sub> |  | 2.7<br><sub>0,3,3,5,4</sub> |  | 1.6<br><sub>1,2,2,4,1</sub> |  | 1.0 | 0.8 | 1.6 | 24.3 |
| LaMelo Ball | 98% | 29.0<br><sub>29,20,33,31,35</sub> | 22.1<br><sub>24,10,34,20,22</sub> |  | 4.5<br><sub>4,8,6,2,2</sub> |  | 6.8<br><sub>7,4,3,6,8</sub> |  | 4.0<br><sub>6,0,6,4,3</sub> |  | 1.6 | 0.3 | 3.3 | 33.4 |
| Rudy Gobert | 98% | 28.5<br><sub>30,-,31,33,25</sub> | 9.5<br><sub>9,-,10,8,8</sub> |  | 10.9<br><sub>13,-,10,11,11</sub> |  | 1.6<br><sub>4,-,1,2,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.9 | 1.6 | 1.3 | 22.1 |
| Trey Lyles | 98% | 22.3<br><sub>17,17,21,20,29</sub> | 7.7<br><sub>10,6,12,5,5</sub> |  | 5.2<br><sub>5,0,4,2,13</sub> |  | 1.2<br><sub>0,0,0,0,2</sub> |  | 1.1<br><sub>1,1,2,1,0</sub> |  | 0.8 | 0.4 | 0.7 | 14.1 |
| Terrence Shannon Jr. | 98% | 20.4<br><sub>20,18,-,-,-</sub> | 11.7<br><sub>11,2,-,-,-</sub> |  | 2.7<br><sub>3,3,-,-,-</sub> |  | 1.9<br><sub>2,4,-,-,-</sub> |  | 1.3<br><sub>2,0,-,-,-</sub> |  | 0.6 | 0.1 | 1.1 | 16.4 |
| Jaylen Clark | 91% | 20.0<br><sub>17,20,21,25,21</sub> | 7.3<br><sub>5,10,4,10,8</sub> |  | 2.7<br><sub>0,2,2,4,3</sub> |  | 1.2<br><sub>2,1,0,1,0</sub> |  | 0.9<br><sub>1,2,1,2,1</sub> |  | 1.3 | 0.2 | 0.6 | 11.2 |
| Bones Hyland | 98% | 15.2<br><sub>20,14,14,16,10</sub> | 9.6<br><sub>19,6,10,19,4</sub> |  | 1.7<br><sub>0,1,1,2,1</sub> |  | 2.8<br><sub>8,3,3,4,0</sub> |  | 1.5<br><sub>3,0,2,4,1</sub> |  | 0.8 | 0.2 | 1.0 | 14.1 |
| Zyon Pullin | 38% | 7.0<br><sub>2,-,-,-,-</sub> | 3.0<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Rocco Zikarsky | 26% | 6.8<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.7 | 0.3 | 4.9 |
| Cody Williams | 48% | 6.3<br><sub>2,-,7,-,-</sub> | 0.2<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 1.7 |
| Isaiah Evans | 38% | 5.7<br><sub>2,-,-,-,-</sub> | 0.3<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 1.9 |

</details>

<details><summary>if Lauri Markkanen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels (MIN) | 98% | 33.2<br><sub>33,39,29,37,40</sub> | 18.4<br><sub>23,19,13,14,23</sub> |  | 5.9<br><sub>6,3,6,8,6</sub> |  | 3.3<br><sub>7,3,3,4,5</sub> |  | 1.5<br><sub>1,2,2,0,2</sub> |  | 1.2 | 1.0 | 1.9 | 27.7 |
| Ayo Dosunmu (MIN) | 98% | 32.1<br><sub>30,38,37,34,39</sub> | 18.0<br><sub>15,27,19,21,26</sub> |  | 4.7<br><sub>7,9,12,1,2</sub> |  | 4.8<br><sub>2,3,8,6,4</sub> |  | 1.8<br><sub>3,2,1,0,4</sub> |  | 1.4 | 0.4 | 2.0 | 27.5 |
| Jonathan Kuminga (MIN) | 98% | 30.5<br><sub>22,40,33,32,34</sub> | 15.4<br><sub>5,19,8,16,17</sub> |  | 6.2<br><sub>1,6,10,8,8</sub> |  | 2.8<br><sub>0,3,3,5,4</sub> |  | 1.6<br><sub>1,2,2,4,1</sub> |  | 1.0 | 0.7 | 1.6 | 24.3 |
| LaMelo Ball (MIN) | 98% | 29.1<br><sub>29,20,33,31,35</sub> | 21.9<br><sub>24,10,34,20,22</sub> |  | 4.5<br><sub>4,8,6,2,2</sub> |  | 6.8<br><sub>7,4,3,6,8</sub> |  | 4.0<br><sub>6,0,6,4,3</sub> |  | 1.6 | 0.3 | 3.3 | 33.2 |
| Rudy Gobert (MIN) | 98% | 28.5<br><sub>30,-,31,33,25</sub> | 9.5<br><sub>9,-,10,8,8</sub> |  | 11.0<br><sub>13,-,10,11,11</sub> |  | 1.6<br><sub>4,-,1,2,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.9 | 1.6 | 1.3 | 22.2 |
| Trey Lyles (MIN) | 98% | 22.3<br><sub>17,17,21,20,29</sub> | 7.7<br><sub>10,6,12,5,5</sub> |  | 5.1<br><sub>5,0,4,2,13</sub> |  | 1.2<br><sub>0,0,0,0,2</sub> |  | 1.1<br><sub>1,1,2,1,0</sub> |  | 0.8 | 0.4 | 0.7 | 14.0 |
| Terrence Shannon Jr. (MIN) | 98% | 20.4<br><sub>20,18,-,-,-</sub> | 11.6<br><sub>11,2,-,-,-</sub> |  | 2.7<br><sub>3,3,-,-,-</sub> |  | 1.9<br><sub>2,4,-,-,-</sub> |  | 1.3<br><sub>2,0,-,-,-</sub> |  | 0.6 | 0.1 | 1.1 | 16.2 |
| Jaylen Clark (MIN) | 91% | 20.1<br><sub>17,20,21,25,21</sub> | 7.2<br><sub>5,10,4,10,8</sub> |  | 2.7<br><sub>0,2,2,4,3</sub> |  | 1.2<br><sub>2,1,0,1,0</sub> |  | 0.9<br><sub>1,2,1,2,1</sub> |  | 1.3 | 0.2 | 0.6 | 11.1 |
| Bones Hyland (MIN) | 98% | 15.2<br><sub>20,14,14,16,10</sub> | 9.5<br><sub>19,6,10,19,4</sub> |  | 1.7<br><sub>0,1,1,2,1</sub> |  | 2.8<br><sub>8,3,3,4,0</sub> |  | 1.4<br><sub>3,0,2,4,1</sub> |  | 0.8 | 0.2 | 1.0 | 14.1 |
| Rocco Zikarsky (MIN) | 26% | 7.0<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.7 | 0.3 | 5.0 |
| Zyon Pullin (MIN) | 38% | 6.9<br><sub>2,-,-,-,-</sub> | 2.9<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.7 |
| Cody Williams (MIN) | 48% | 6.2<br><sub>2,-,7,-,-</sub> | 0.2<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 1.7 |
| Isaiah Evans (MIN) | 38% | 5.7<br><sub>2,-,-,-,-</sub> | 0.3<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 1.9 |
| Keyonte George (UTA) | 98% | 31.7<br><sub>37,29,22,44,32</sub> | 21.2<br><sub>31,8,7,39,16</sub> |  | 3.8<br><sub>4,3,7,2,6</sub> |  | 5.6<br><sub>3,4,0,9,9</sub> |  | 2.1<br><sub>5,0,1,2,1</sub> |  | 0.9 | 0.2 | 3.3 | 30.6 |
| Lauri Markkanen (UTA) | 100% | 31.5<br><sub>-,29,31,39,34</sub> | 20.3<br><sub>-,13,22,21,24</sub> |  | 6.3<br><sub>-,6,8,10,8</sub> |  | 1.9<br><sub>-,1,3,4,1</sub> |  | 2.3<br><sub>-,2,4,5,8</sub> |  | 0.9 | 0.5 | 1.9 | 28.5 |
| Ace Bailey (UTA) | 98% | 30.5<br><sub>40,37,24,35,29</sub> | 12.3<br><sub>19,9,5,15,12</sub> |  | 5.6<br><sub>6,7,6,5,6</sub> |  | 1.9<br><sub>0,1,2,1,0</sub> |  | 1.6<br><sub>1,1,1,1,0</sub> |  | 0.9 | 1.0 | 1.9 | 19.8 |
| Darryn Peterson (UTA) | 98% | 30.0<br><sub>26,36,33,30,30</sub> | 12.6<br><sub>18,16,14,7,21</sub> |  | 3.8<br><sub>5,4,4,2,2</sub> |  | 3.9<br><sub>3,4,6,7,5</sub> |  | 1.3<br><sub>3,3,2,0,3</sub> |  | 1.1 | 0.8 | 1.9 | 20.2 |
| Jaxson Hayes (UTA) | 98% | 24.0<br><sub>37,20,22,21,28</sub> | 7.9<br><sub>2,7,9,2,8</sub> |  | 5.6<br><sub>11,7,5,7,6</sub> |  | 1.6<br><sub>4,2,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.1 | 15.1 |
| Josh Okogie (UTA) | 91% | 19.6<br><sub>28,14,19,26,24</sub> | 4.5<br><sub>5,0,9,3,12</sub> |  | 3.2<br><sub>9,1,3,6,4</sub> |  | 1.0<br><sub>3,0,2,1,0</sub> |  | 0.4<br><sub>1,0,1,1,2</sub> |  | 0.9 | 0.3 | 0.8 | 8.7 |
| Josh Green (UTA) | 88% | 17.9<br><sub>24,2,15,23,24</sub> | 3.7<br><sub>2,0,3,7,3</sub> |  | 1.9<br><sub>2,0,1,1,3</sub> |  | 0.8<br><sub>2,0,0,0,1</sub> |  | 0.4<br><sub>0,0,1,1,1</sub> |  | 0.7 | 0.2 | 0.6 | 6.4 |
| Svi Mykhailiuk (UTA) | 91% | 16.0<br><sub>15,18,14,17,14</sub> | 5.3<br><sub>3,6,3,6,0</sub> |  | 1.9<br><sub>2,1,2,3,0</sub> |  | 1.1<br><sub>1,3,0,0,1</sub> |  | 0.7<br><sub>1,2,1,0,0</sub> |  | 0.5 | 0.1 | 0.6 | 8.3 |
| Isaiah Collier (UTA) | 98% | 15.4<br><sub>24,20,12,3,13</sub> | 7.0<br><sub>7,8,7,0,4</sub> |  | 2.2<br><sub>7,1,2,1,3</sub> |  | 4.1<br><sub>6,4,2,0,3</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.2 | 1.5 | 13.3 |
| Brice Sensabaugh (UTA) | 98% | 15.4<br><sub>18,19,14,12,10</sub> | 8.6<br><sub>16,12,7,6,0</sub> |  | 2.2<br><sub>3,3,2,2,2</sub> |  | 1.2<br><sub>1,2,1,0,2</sub> |  | 1.0<br><sub>4,2,1,1,0</sub> |  | 0.4 | 0.1 | 1.3 | 12.1 |
| Mo Bamba (UTA) | 63% | 13.2<br><sub>16,11,18,15,-</sub> | 4.7<br><sub>8,6,8,7,-</sub> |  | 4.8<br><sub>4,4,8,10,-</sub> |  | 0.6<br><sub>1,0,0,1,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.4 | 1.1 | 0.7 | 10.2 |
| Kyle Filipowski (UTA) | 66% | 9.7<br><sub>-,6,8,-,1</sub> | 4.4<br><sub>-,5,1,-,0</sub> |  | 2.7<br><sub>-,0,2,-,0</sub> |  | 0.9<br><sub>-,2,0,-,0</sub> |  | 0.2<br><sub>-,1,0,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 8.1 |
| Kobe Bufkin (UTA) | 35% | 8.9<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.8 |
| Tony Bradley (UTA) | 52% | 7.4<br><sub>-,-,7,-,1</sub> | 2.8<br><sub>-,-,2,-,0</sub> |  | 2.2<br><sub>-,-,3,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 5.4 |

</details>


### BKN @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Mikel Brown Jr. (BKN), Egor Demin (BKN)

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 98% | 34.4<br><sub>40,26,36,37,38</sub> | 22.6<br><sub>27,13,23,18,26</sub> |  | 7.7<br><sub>12,7,9,5,10</sub> |  | 2.6<br><sub>2,1,3,2,0</sub> |  | 2.9<br><sub>6,2,3,4,4</sub> |  | 1.1 | 0.4 | 2.5 | 33.0 |
| Julius Randle | 98% | 34.3<br><sub>44,25,37,36,31</sub> | 21.6<br><sub>24,15,20,21,22</sub> |  | 7.6<br><sub>9,8,5,11,3</sub> |  | 4.6<br><sub>4,3,6,2,4</sub> |  | 1.7<br><sub>0,3,4,0,2</sub> |  | 1.0 | 0.2 | 3.6 | 33.8 |
| Nolan Traore | 98% | 24.8<br><sub>24,26,30,24,27</sub> | 12.2<br><sub>15,9,16,17,16</sub> |  | 2.6<br><sub>1,2,2,3,4</sub> |  | 3.9<br><sub>3,2,6,4,2</sub> |  | 1.4<br><sub>1,0,4,5,2</sub> |  | 1.1 | 0.5 | 2.3 | 18.7 |
| Day'Ron Sharpe | 98% | 23.1<br><sub>17,24,26,22,27</sub> | 9.4<br><sub>4,3,15,4,6</sub> |  | 8.2<br><sub>6,7,13,6,5</sub> |  | 3.0<br><sub>0,1,4,3,8</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 1.1 | 0.8 | 1.7 | 20.6 |
| Noah Clowney | 98% | 21.1<br><sub>24,22,24,20,17</sub> | 7.8<br><sub>3,3,8,2,7</sub> |  | 3.9<br><sub>4,8,3,6,1</sub> |  | 1.2<br><sub>1,1,0,2,1</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.5 | 1.0 | 12.9 |
| Chaney Johnson | 93% | 18.8<br><sub>29,19,31,28,9</sub> | 5.3<br><sub>15,6,2,4,0</sub> |  | 2.8<br><sub>3,2,2,3,2</sub> |  | 1.0<br><sub>2,0,0,2,1</sub> |  | 0.6<br><sub>3,0,0,1,0</sub> |  | 0.6 | 0.4 | 0.9 | 9.2 |
| Keon Ellis | 96% | 18.5<br><sub>25,21,20,25,10</sub> | 5.0<br><sub>2,6,0,5,1</sub> |  | 2.0<br><sub>3,2,2,1,2</sub> |  | 1.2<br><sub>4,1,1,0,0</sub> |  | 0.6<br><sub>0,2,0,1,0</sub> |  | 1.0 | 0.6 | 0.6 | 8.3 |
| Moritz Wagner | 93% | 18.4<br><sub>22,23,21,20,20</sub> | 9.3<br><sub>15,16,14,6,6</sub> |  | 4.7<br><sub>4,8,6,1,1</sub> |  | 1.2<br><sub>3,1,0,2,0</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.3 | 1.1 | 15.2 |
| Danny Wolf | 52% | 17.4<br><sub>-,12,-,-,19</sub> | 7.8<br><sub>-,9,-,-,12</sub> |  | 4.5<br><sub>-,6,-,-,5</sub> |  | 1.9<br><sub>-,2,-,-,3</sub> |  | 0.9<br><sub>-,3,-,-,2</sub> |  | 0.5 | 0.5 | 1.1 | 14.2 |
| Terance Mann | 58% | 15.8<br><sub>-,12,15,-,16</sub> | 4.4<br><sub>-,2,0,-,0</sub> |  | 2.1<br><sub>-,0,1,-,2</sub> |  | 1.6<br><sub>-,2,1,-,2</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 8.1 |
| Josh Minott | 52% | 12.0<br><sub>-,3,-,-,6</sub> | 5.9<br><sub>-,2,-,-,0</sub> |  | 2.3<br><sub>-,0,-,-,1</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.6 | 0.4 | 0.7 | 8.9 |
| Ben Saraf | 58% | 11.9<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 1.2 | 8.0 |
| Drake Powell | 52% | 9.4<br><sub>-,6,-,-,-</sub> | 3.1<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,2,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.8 |
| Grant Nelson | 16% | 8.7 | 3.3 |  | 2.2 |  | 0.5 |  | 0.1 |  | 0.3 | 0.9 | 0.5 | 6.0 |
| Tyler Bilodeau | 8% | 8.6 | 3.8 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Joshua Jefferson | 80% | 5.9<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 0.9 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 32.9<br><sub>33,39,40,40,33</sub> | 22.9<br><sub>26,33,17,19,21</sub> |  | 6.7<br><sub>5,9,4,10,10</sub> |  | 6.0<br><sub>8,6,6,5,7</sub> |  | 1.1<br><sub>2,0,0,0,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 1.0 | 2.8 | 35.6 |
| Kyrie Irving | 98% | 32.3<br><sub>27,35,-,36,28</sub> | 22.0<br><sub>15,35,-,29,14</sub> |  | 4.4<br><sub>2,4,-,7,2</sub> |  | 4.7<br><sub>4,9,-,5,2</sub> |  | 2.9<br><sub>3,5,-,5,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.5 | 2.4 | 31.1 |
| P.J. Washington | 98% | 31.9<br><sub>27,34,38,39,33</sub> | 15.4<br><sub>18,3,12,21,26</sub> |  | 7.0<br><sub>9,10,5,10,6</sub> |  | 1.8<br><sub>0,1,1,3,1</sub> |  | 1.7<br><sub>2,1,2,3,6</sub> |  | 1.1 | 0.9 | 1.7 | 24.1 |
| Naji Marshall | 88% | 24.7<br><sub>-,-,24,26,25</sub> | 12.8<br><sub>-,-,5,22,7</sub> |  | 3.8<br><sub>-,-,2,5,1</sub> |  | 3.9<br><sub>-,-,7,3,5</sub> |  | 0.8<br><sub>-,-,0,3,0</sub> |  | 1.1 | 0.1 | 1.8 | 20.5 |
| Daniel Gafford | 98% | 20.5<br><sub>27,29,26,18,18</sub> | 9.7<br><sub>7,18,20,2,7</sub> |  | 6.4<br><sub>11,7,7,4,1</sub> |  | 1.3<br><sub>2,2,0,1,1</sub> |  | 0.0<br><sub>1,0,0,0,0</sub> |  | 0.7 | 1.5 | 1.1 | 17.4 |
| Zaccharie Risacher | 96% | 20.4<br><sub>29,28,19,18,21</sub> | 6.2<br><sub>13,12,0,2,4</sub> |  | 3.7<br><sub>6,6,5,1,4</sub> |  | 1.2<br><sub>1,3,1,2,1</sub> |  | 0.6<br><sub>2,3,0,0,0</sub> |  | 0.9 | 0.9 | 0.9 | 11.2 |
| Walter Clayton Jr. | 88% | 16.5<br><sub>15,9,24,21,23</sub> | 6.9<br><sub>0,3,20,8,12</sub> |  | 2.6<br><sub>2,2,1,6,4</sub> |  | 3.0<br><sub>5,1,2,5,2</sub> |  | 0.9<br><sub>0,1,4,2,1</sub> |  | 0.6 | 0.2 | 1.2 | 12.6 |
| Max Christie | 98% | 15.2<br><sub>22,18,8,-,9</sub> | 6.0<br><sub>11,2,0,-,0</sub> |  | 1.8<br><sub>5,1,2,-,1</sub> |  | 1.1<br><sub>2,0,0,-,1</sub> |  | 0.8<br><sub>3,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.8 | 8.8 |
| Morez Johnson Jr. | 98% | 14.4<br><sub>18,17,17,18,24</sub> | 6.2<br><sub>10,2,13,8,13</sub> |  | 2.8<br><sub>6,2,2,3,17</sub> |  | 1.5<br><sub>3,1,1,1,2</sub> |  | 0.3<br><sub>0,0,0,1,1</sub> |  | 0.4 | 0.2 | 0.9 | 10.5 |
| Santi Aldama | 96% | 14.2<br><sub>-,-,-,-,13</sub> | 6.4<br><sub>-,-,-,-,8</sub> |  | 3.6<br><sub>-,-,-,-,9</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.4 | 0.8 | 11.3 |
| Caleb Martin | 96% | 13.0<br><sub>14,25,21,20,11</sub> | 3.7<br><sub>10,8,5,0,0</sub> |  | 2.0<br><sub>2,0,6,3,0</sub> |  | 0.9<br><sub>0,0,0,2,0</sub> |  | 0.3<br><sub>2,2,1,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 6.6 |
| Marcus Sasser | 72% | 8.7<br><sub>22,7,19,5,-</sub> | 3.3<br><sub>10,0,4,0,-</sub> |  | 0.8<br><sub>1,0,1,1,-</sub> |  | 1.4<br><sub>4,1,1,2,-</sub> |  | 0.4<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.5 |
| Moussa Cisse | 64% | 6.9<br><sub>3,-,2,-,1</sub> | 2.6<br><sub>0,-,0,-,0</sub> |  | 2.5<br><sub>0,-,0,-,0</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.0<br><sub>0,-,0,-,0</sub> |  | 0.3 | 0.5 | 0.4 | 5.3 |
| Tobi Lawal | 58% | 5.8<br><sub>3,-,2,-,1</sub> | 2.0<br><sub>0,-,2,-,0</sub> |  | 1.1<br><sub>0,-,0,-,0</sub> |  | 0.7<br><sub>1,-,0,-,0</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Jett Howard | 58% | 5.6<br><sub>3,-,2,-,1</sub> | 2.4<br><sub>0,-,2,-,0</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.1 | 0.3 | 3.5 |

</details>


### BOS @ MIL
Out: Kam Jones (MIL), Pete Nance (MIL), Cormac Ryan (MIL), Devin Carter (BOS)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 32.9<br><sub>35,34,32,-,29</sub> | 25.4<br><sub>26,32,19,-,34</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 8.2<br><sub>7,4,6,-,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>7,7,9,-,9</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>2,1,1,-,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.4 | 2.6 | 40.7 |
| Derrick White | 98% | 30.4<br><sub>26,34,30,36,25</sub> | 14.5<br><sub>9,12,7,24,18</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>2,2,2,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>4,2,3,7,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,2,1,1,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.8 | 1.5 | 23.2 |
| Paul George | 98% | 29.9<br><sub>27,33,-,35,22</sub> | 17.8<br><sub>18,17,-,25,8</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>6,6,-,3,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>8,8,-,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,3,-,5,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.7 | 0.4 | 2.4 | 26.9 |
| Payton Pritchard | 98% | 25.6<br><sub>35,27,30,18,23</sub> | 14.1<br><sub>30,7,4,10,12</sub> |  | 3.1<br><sub>3,7,3,1,6</sub> |  | 4.5<br><sub>3,3,3,5,5</sub> |  | 2.1<br><sub>3,0,0,0,4</sub> |  | 0.8 | 0.1 | 1.1 | 21.6 |
| Neemias Queta | 98% | 21.2<br><sub>20,27,26,29,15</sub> | 9.1<br><sub>13,8,16,9,4</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>6,8,6,12,3</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,1,1,3,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.7 | 1.0 | 0.9 | 17.6 |
| Sam Hauser | 98% | 20.6<br><sub>18,17,19,30,17</sub> | 7.8<br><sub>6,3,2,11,9</sub> |  | 3.1<br><sub>3,2,2,2,3</sub> |  | 1.2<br><sub>2,0,1,0,3</sub> |  | 1.5<br><sub>2,1,0,3,3</sub> |  | 0.4 | 0.2 | 0.3 | 12.1 |
| Baylor Scheierman | 98% | 19.8<br><sub>23,20,27,29,15</sub> | 6.4<br><sub>2,10,11,9,5</sub> |  | 3.8<br><sub>3,2,5,11,4</sub> |  | 1.6<br><sub>3,1,2,1,2</sub> |  | 1.0<br><sub>0,2,3,3,1</sub> |  | 0.8 | 0.1 | 0.6 | 11.9 |
| Mitchell Robinson | 98% | 16.5<br><sub>19,-,15,20,15</sub> | 5.5<br><sub>11,-,4,3,6</sub> |  | 6.4<br><sub>4,-,4,10,7</sub> |  | 0.6<br><sub>0,-,0,1,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.7 | 0.6 | 12.5 |
| Luka Garza | 98% | 15.5<br><sub>7,21,18,18,19</sub> | 8.9<br><sub>5,12,14,11,6</sub> |  | 4.0<br><sub>1,6,3,5,7</sub> |  | 1.4<br><sub>1,4,0,2,4</sub> |  | 0.9<br><sub>0,2,4,3,2</sub> |  | 0.5 | 0.3 | 0.7 | 14.3 |
| Jordan Walsh | 98% | 15.5<br><sub>11,13,12,12,22</sub> | 4.5<br><sub>2,0,5,3,6</sub> |  | 3.3<br><sub>2,3,3,4,3</sub> |  | 0.8<br><sub>0,2,0,0,0</sub> |  | 0.5<br><sub>0,0,1,1,1</sub> |  | 0.7 | 0.3 | 0.4 | 8.6 |
| Hugo Gonzalez | 96% | 13.6<br><sub>15,14,16,14,15</sub> | 4.3<br><sub>0,7,6,4,8</sub> |  | 2.8<br><sub>2,1,3,2,1</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.8 |
| Mike Conley | 52% | 8.6<br><sub>-,-,4,-,11</sub> | 2.6<br><sub>-,-,3,-,0</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 1.4<br><sub>-,-,0,-,1</sub> |  | 0.3<br><sub>-,-,1,-,0</sub> |  | 0.5 | 0.1 | 0.3 | 4.9 |
| Ron Harper Jr. | 58% | 8.2<br><sub>3,-,7,-,10</sub> | 3.5<br><sub>0,-,0,-,3</sub> |  | 1.2<br><sub>0,-,1,-,0</sub> |  | 0.7<br><sub>0,-,1,-,2</sub> |  | 0.4<br><sub>0,-,0,-,1</sub> |  | 0.4 | 0.1 | 0.3 | 5.4 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 32.5<br><sub>27,27,31,33,35</sub> | 18.7<br><sub>23,15,21,25,23</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>3,3,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>0,2,3,3,10</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>4,4,4,4,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.2 | 2.1 | 27.9 |
| Jaime Jaquez Jr. | 98% | 28.4<br><sub>27,23,28,31,28</sub> | 14.2<br><sub>19,8,19,18,14</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>4,7,8,2,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>2,5,2,2,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>3,1,2,4,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 0.2 | 1.9 | 23.2 |
| Kyle Kuzma | 98% | 27.8<br><sub>18,23,22,27,32</sub> | 11.4<br><sub>4,14,2,6,13</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>6,3,2,5,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>1,3,3,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>0,2,0,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.3 | 1.6 | 19.3 |
| Myles Turner | 98% | 27.2<br><sub>22,24,31,36,24</sub> | 9.9<br><sub>4,10,13,12,0</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>2,7,5,9,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>2,2,2,6,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>0,1,3,4,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.6 | 1.8 | 1.3 | 16.9 |
| Brayden Burries | 98% | 25.3<br><sub>17,21,26,22,38</sub> | 10.8<br><sub>10,14,9,9,21</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>5,3,9,5,11</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>1,1,1,3,6</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,1,0,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.2 | 1.5 | 18.8 |
| Ryan Rollins | 98% | 22.8<br><sub>17,26,17,24,14</sub> | 11.7<br><sub>4,9,10,13,10</sub> |  | 3.2<br><sub>4,3,3,9,1</sub> |  | 4.2<br><sub>5,7,2,5,1</sub> |  | 1.5<br><sub>0,1,1,2,1</sub> |  | 0.8 | 0.3 | 2.0 | 19.1 |
| AJ Green | 98% | 22.2<br><sub>24,20,24,20,24</sub> | 7.6<br><sub>9,0,13,5,12</sub> |  | 2.2<br><sub>1,3,3,2,1</sub> |  | 1.6<br><sub>2,2,3,3,0</sub> |  | 1.4<br><sub>3,0,4,1,4</sub> |  | 0.4 | 0.1 | 0.6 | 11.4 |
| Kel'el Ware | 93% | 16.2<br><sub>17,24,17,16,13</sub> | 7.4<br><sub>6,19,2,2,4</sub> |  | 5.5<br><sub>8,10,9,5,3</sub> |  | 0.8<br><sub>0,3,0,1,0</sub> |  | 0.8<br><sub>0,3,0,0,0</sub> |  | 0.3 | 0.7 | 1.1 | 13.6 |
| Kasparas Jakucionis | 91% | 15.5<br><sub>19,21,22,12,10</sub> | 5.3<br><sub>4,5,7,3,3</sub> |  | 1.8<br><sub>2,3,5,1,0</sub> |  | 3.0<br><sub>6,3,7,1,2</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.1 | 1.0 | 10.1 |
| Nate Ament | 88% | 13.8<br><sub>20,19,8,18,15</sub> | 5.6<br><sub>8,14,4,9,7</sub> |  | 2.0<br><sub>4,1,1,2,1</sub> |  | 0.5<br><sub>0,2,0,0,0</sub> |  | 0.6<br><sub>1,2,0,2,0</sub> |  | 0.3 | 0.3 | 0.7 | 8.1 |
| Caris LeVert | 16% | 13.6<br><sub>-,-,-,-,-</sub> | 4.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.4 | 0.7 | 7.7 |
| Jericho Sims | 67% | 9.9<br><sub>7,-,15,1,7</sub> | 2.0<br><sub>0,-,0,0,0</sub> |  | 2.6<br><sub>0,-,2,0,1</sub> |  | 0.8<br><sub>0,-,1,0,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.4 |
| Gary Trent Jr. | 38% | 9.2<br><sub>7,6,-,-,-</sub> | 3.6<br><sub>3,3,-,-,-</sub> |  | 0.8<br><sub>0,1,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.5<br><sub>1,1,-,-,-</sub> |  | 0.2 | 0.0 | 0.3 | 4.8 |
| Ousmane Dieng | 58% | 7.7<br><sub>13,6,-,2,-</sub> | 2.6<br><sub>4,0,-,0,-</sub> |  | 1.2<br><sub>0,1,-,0,-</sub> |  | 0.9<br><sub>0,2,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |

</details>


### NOP @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Isaiah Jackson (LAC), Yves Missi (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray | 98% | 32.5<br><sub>-,-,-,45,35</sub> | 16.8<br><sub>-,-,-,20,7</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>-,-,-,8,2</sub> |  | 6.1<br><sub>-,-,-,4,4</sub> |  | 1.6<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.8 | 0.3 | 3.2 | 28.5 |
| Trey Murphy III | 98% | 32.3<br><sub>32,29,40,-,34</sub> | 15.5<br><sub>19,15,18,-,10</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>5,5,5,-,4</sub> |  | 3.3<br><sub>3,5,5,-,5</sub> |  | 2.3<br><sub>2,1,3,-,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.5 | 1.4 | 23.6 |
| Zion Williamson | 98% | 31.8<br><sub>31,30,35,38,36</sub> | 18.9<br><sub>22,15,25,23,13</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>6,6,11,4,8</sub> |  | 3.0<br><sub>2,4,4,2,4</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.4 | 0.6 | 2.2 | 27.7 |
| Jeremiah Fears | 98% | 29.9<br><sub>29,31,38,34,36</sub> | 16.5<br><sub>22,20,12,19,24</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>8,5,4,6,5</sub> |  | 4.3<br><sub>13,7,7,2,5</sub> |  | 1.4<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 2.7 | 25.1 |
| Saddiq Bey | 98% | 26.8<br><sub>24,26,36,29,31</sub> | 13.6<br><sub>10,25,18,22,17</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>4,6,5,4,5</sub> |  | 2.0<br><sub>3,1,1,3,4</sub> |  | 1.6<br><sub>1,1,2,2,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.2 | 1.1 | 19.8 |
| Herbert Jones | 98% | 19.6<br><sub>32,25,28,37,14</sub> | 6.1<br><sub>16,11,9,2,0</sub> |  | 2.3<br><sub>4,3,4,5,4</sub> |  | 1.4<br><sub>1,2,3,1,0</sub> |  | 0.7<br><sub>0,1,3,0,0</sub> |  | 1.0 | 0.3 | 0.9 | 9.8 |
| Derik Queen | 98% | 18.3<br><sub>22,23,24,27,10</sub> | 8.9<br><sub>9,8,20,20,6</sub> |  | 5.5<br><sub>2,8,7,9,4</sub> |  | 2.3<br><sub>3,4,5,6,1</sub> |  | 0.2<br><sub>1,0,1,0,0</sub> |  | 0.8 | 0.6 | 1.8 | 16.8 |
| Karlo Matkovic | 91% | 16.2<br><sub>28,18,29,21,18</sub> | 6.7<br><sub>12,8,25,5,18</sub> |  | 3.8<br><sub>4,10,6,4,3</sub> |  | 0.8<br><sub>1,1,1,2,1</sub> |  | 0.7<br><sub>1,2,5,1,4</sub> |  | 0.6 | 0.7 | 0.8 | 11.3 |
| Trendon Watford | 72% | 13.9<br><sub>17,18,16,20,19</sub> | 5.8<br><sub>8,7,4,7,12</sub> |  | 2.7<br><sub>1,4,4,3,6</sub> |  | 1.4<br><sub>2,0,1,2,1</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.5 | 0.3 | 0.9 | 9.8 |
| Bennedict Mathurin | 98% | 12.9<br><sub>19,19,13,15,7</sub> | 5.7<br><sub>10,7,4,2,2</sub> |  | 2.3<br><sub>3,1,0,5,0</sub> |  | 1.1<br><sub>2,2,0,1,0</sub> |  | 0.4<br><sub>2,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.1 |
| Jordan Poole | 52% | 12.4<br><sub>-,-,-,-,-</sub> | 5.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.0 | 8.7 |
| DeAndre Jordan | 30% | 8.2<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.8 |
| Bryce McGowens | 52% | 7.3<br><sub>6,15,6,-,-</sub> | 2.5<br><sub>4,3,0,-,-</sub> |  | 0.9<br><sub>1,0,1,-,-</sub> |  | 0.5<br><sub>2,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |
| AJ Johnson | 26% | 5.3<br><sub>-,3,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.9 | 0.9 |
| Julian Reese | 30% | 5.3<br><sub>-,3,-,-,-</sub> | 2.0<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.9 | 3.4 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.1<br><sub>26,31,33,36,39</sub> | 22.3<br><sub>14,24,15,16,26</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,2,0,4,1</sub> |  | 7.2<br><sub>5,5,7,8,7</sub> |  | 2.8<br><sub>1,4,1,1,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.2 | 3.6 | 31.9 |
| Rui Hachimura | 98% | 31.1<br><sub>-,26,30,-,37</sub> | 16.4<br><sub>-,12,24,-,21</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>-,5,7,-,9</sub> |  | 1.6<br><sub>-,0,0,-,7</sub> |  | 2.1<br><sub>-,2,4,-,1</sub> |  | 0.9 | 0.4 | 1.5 | 23.0 |
| Derrick Jones Jr. | 98% | 29.0<br><sub>28,26,28,-,37</sub> | 11.7<br><sub>15,10,9,-,12</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>5,1,7,-,8</sub> |  | 1.6<br><sub>0,1,1,-,1</sub> |  | 1.3<br><sub>3,2,1,-,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 1.0 | 1.0 | 17.9 |
| Kris Dunn | 98% | 28.4<br><sub>27,31,27,30,35</sub> | 8.4<br><sub>5,5,12,12,5</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,5,2,4,5</sub> |  | 4.4<br><sub>3,7,4,1,3</sub> |  | 0.9<br><sub>1,0,0,1,1</sub> |  | 2.0 | 0.3 | 1.5 | 16.4 |
| Brook Lopez | 98% | 24.8<br><sub>22,21,19,22,35</sub> | 12.9<br><sub>2,13,7,12,20</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>3,6,2,6,8</sub> |  | 1.6<br><sub>3,0,0,1,1</sub> |  | 1.6<br><sub>0,1,1,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 1.4 | 1.2 | 19.6 |
| Max Strus | 97% | 22.6<br><sub>-,-,-,23,23</sub> | 10.3<br><sub>-,-,-,11,9</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>-,-,-,4,5</sub> |  | 3.1<br><sub>-,-,-,6,5</sub> |  | 1.8<br><sub>-,-,-,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.2 | 1.3 | 17.3 |
| Kobe Sanders | 98% | 21.5<br><sub>27,24,30,38,18</sub> | 10.0<br><sub>9,7,16,26,4</sub> |  | 2.4<br><sub>4,4,3,4,2</sub> |  | 2.0<br><sub>0,2,0,3,1</sub> |  | 1.4<br><sub>1,1,4,5,0</sub> |  | 0.9 | 0.2 | 1.3 | 14.4 |
| Keaton Wagler | 97% | 21.0<br><sub>28,25,19,24,16</sub> | 10.6<br><sub>21,12,7,6,11</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>4,6,4,4,2</sub> |  | 3.0<br><sub>2,3,4,4,1</sub> |  | 1.1<br><sub>3,1,0,0,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.3 | 1.7 | 16.8 |
| Gradey Dick | 96% | 12.2<br><sub>19,12,3,29,7</sub> | 5.5<br><sub>5,3,0,12,4</sub> |  | 1.9<br><sub>5,0,1,4,2</sub> |  | 0.7<br><sub>0,1,0,3,1</sub> |  | 0.5<br><sub>1,1,0,0,0</sub> |  | 0.5 | 0.1 | 0.6 | 8.1 |
| Baba Miller | 91% | 11.2<br><sub>17,5,6,12,6</sub> | 4.9<br><sub>4,0,2,4,2</sub> |  | 1.8<br><sub>7,1,2,0,1</sub> |  | 1.4<br><sub>1,0,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 8.0 |
| Jalen Pickett | 48% | 7.0<br><sub>8,-,6,-,-</sub> | 2.6<br><sub>4,-,0,-,-</sub> |  | 0.9<br><sub>1,-,2,-,-</sub> |  | 1.1<br><sub>1,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Nick Martinelli | 52% | 7.0<br><sub>6,5,6,-,-</sub> | 3.4<br><sub>2,3,10,-,-</sub> |  | 1.9<br><sub>3,0,3,-,-</sub> |  | 0.6<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>0,0,2,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Cam Christie | 52% | 6.7<br><sub>14,5,6,-,-</sub> | 2.7<br><sub>2,2,3,-,-</sub> |  | 1.1<br><sub>0,1,1,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.1<br><sub>0,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Blake Wesley | 52% | 6.3<br><sub>-,5,4,-,-</sub> | 2.7<br><sub>-,0,2,-,-</sub> |  | 0.8<br><sub>-,4,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.4 |

</details>


### MIA @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 124.5–117.5 | MIA 69% | 1.45 / 3.24 | SAC +7.5 | 241.5 | SAC +8.5 covers 54%; o238.5 57% |
| Expected (weighted by chance each plays) | 124.4–117.8 | MIA 68% | 1.46 / 3.16 | SAC +6.5 | 242.5 | SAC +8.5 covers 56%; o238.5 57% |
| if Keegan Murray plays | 124.2–118.0 | MIA 67% | 1.49 / 3.02 | SAC +6.5 | 242.5 | SAC +8.5 covers 57%; o238.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keegan Murray (SAC) | Questionable | 55% | 23.9 | 9.4 | 4.1 | 1.2 | 1.0 | 0.7 | 0.8 | 0.9 | 14.8 | full tables below |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 34.5<br><sub>34,35,29,43,38</sub> | 13.1<br><sub>10,15,15,11,22</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,6,0,2,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 8.1<br><sub>10,11,7,10,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,3,4,0,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.3 | 1.9 | 24.0 |
| Bam Adebayo | 98% | 33.9<br><sub>33,33,31,41,33</sub> | 21.1<br><sub>24,27,16,35,18</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>9,9,9,10,10</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>3,3,4,4,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.7 | 0.7 | 1.8 | 35.0 |
| Giannis Antetokounmpo | 98% | 33.4<br><sub>31,31,34,41,31</sub> | 29.5<br><sub>24,31,30,27,20</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>18,18,12,14,14</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>3,10,7,6,4</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 1.1 | 0.9 | 3.3 | 48.1 |
| Pelle Larsson | 98% | 29.6<br><sub>31,24,30,35,29</sub> | 11.7<br><sub>17,18,9,7,13</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>6,3,3,3,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>8,3,2,4,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.9<br><sub>2,1,1,0,3</sub> |  | 1.1 | 0.3 | 1.6 | 19.0 |
| Andrew Wiggins | 98% | 25.6<br><sub>29,30,24,23,21</sub> | 11.4<br><sub>18,12,7,3,2</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>2,2,0,4,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.8 | 1.1 | 17.2 |
| Klay Thompson | 98% | 23.6<br><sub>17,26,27,35,23</sub> | 12.2<br><sub>3,25,19,30,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,0,1,5,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.8<br><sub>2,3,1,3,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>1,7,4,8,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.4 | 1.0 | 16.0 |
| Bobby Portis | 98% | 17.6<br><sub>23,17,18,18,14</sub> | 7.7<br><sub>11,8,2,4,0</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>9,3,3,10,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>4,1,2,5,0</sub> |  | 1.0<br><sub>1,2,0,0,0</sub> |  | 0.6 | 0.3 | 0.7 | 13.9 |
| Ryan Conwell | 80% | 14.4<br><sub>-,7,8,17,30</sub> | 5.0<br><sub>-,4,5,0,13</sub> |  | 1.3<br><sub>-,0,1,2,1</sub> |  | 1.3<br><sub>-,0,1,2,2</sub> |  | 0.7<br><sub>-,1,1,0,3</sub> |  | 0.6 | 0.1 | 0.5 | 7.6 |
| Tim Hardaway Jr. | 98% | 12.7<br><sub>22,12,19,7,4</sub> | 5.5<br><sub>14,2,9,0,0</sub> |  | 1.4<br><sub>3,1,0,0,0</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.8<br><sub>2,0,3,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.6 |
| Nikola Jovic | 67% | 11.8<br><sub>7,16,7,-,12</sub> | 4.4<br><sub>5,0,2,-,1</sub> |  | 2.1<br><sub>3,4,1,-,0</sub> |  | 1.1<br><sub>0,3,0,-,1</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 7.6 |
| Dru Smith | 67% | 8.4<br><sub>14,4,11,-,1</sub> | 2.8<br><sub>3,0,3,-,0</sub> |  | 1.2<br><sub>0,0,3,-,0</sub> |  | 1.4<br><sub>3,1,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.8 | 0.2 | 0.4 | 5.3 |
| Simone Fontecchio | 52% | 7.5<br><sub>-,2,-,5,-</sub> | 3.8<br><sub>-,3,-,0,-</sub> |  | 1.4<br><sub>-,1,-,0,-</sub> |  | 0.6<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.8 |
| Keshad Johnson | 16% | 6.4 | 3.0 |  | 1.4 |  | 0.3 |  | 0.2 |  | 0.4 | 0.2 | 0.3 | 4.7 |
| Nick Richards | 63% | 6.3<br><sub>-,2,1,-,1</sub> | 2.6<br><sub>-,0,0,-,0</sub> |  | 2.3<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 5.1 |
| Myron Gardner | 58% | 6.1<br><sub>-,2,1,-,1</sub> | 2.5<br><sub>-,0,0,-,0</sub> |  | 1.7<br><sub>-,1,0,-,0</sub> |  | 0.7<br><sub>-,1,0,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.8 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 35.6<br><sub>41,37,37,42,33</sub> | 24.8<br><sub>34,38,25,22,22</sub> |  | 4.2<br><sub>6,5,5,3,3</sub> |  | 7.4<br><sub>14,5,6,12,8</sub> |  | 2.7<br><sub>3,9,2,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.3 | 3.1 | 36.4 |
| Zach LaVine | 98% | 32.5<br><sub>39,21,28,35,35</sub> | 21.1<br><sub>21,11,23,21,14</sub> |  | 3.4<br><sub>3,0,4,4,4</sub> |  | 3.0<br><sub>5,1,1,1,3</sub> |  | 2.7<br><sub>3,0,5,3,1</sub> |  | 0.8 | 0.3 | 2.4 | 27.5 |
| Domantas Sabonis | 98% | 32.5<br><sub>40,38,31,35,31</sub> | 15.7<br><sub>9,11,9,16,17</sub> |  | 12.7<br><sub>15,14,7,17,12</sub> |  | 5.5<br><sub>7,8,4,1,5</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.9 | 0.3 | 2.6 | 33.9 |
| De'Andre Hunter | 98% | 30.6<br><sub>37,32,36,38,-</sub> | 14.8<br><sub>24,19,6,14,-</sub> |  | 4.9<br><sub>5,3,7,2,-</sub> |  | 1.8<br><sub>1,0,2,2,-</sub> |  | 1.9<br><sub>4,2,0,1,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.6 | 21.4 |
| Leaky Black | 64% | 26.0<br><sub>-,-,25,22,40</sub> | 6.2<br><sub>-,-,12,3,12</sub> |  | 4.3<br><sub>-,-,3,6,3</sub> |  | 1.8<br><sub>-,-,1,1,5</sub> |  | 0.9<br><sub>-,-,4,0,4</sub> |  | 1.1 | 0.5 | 0.8 | 12.4 |
| Precious Achiuwa | 98% | 25.9<br><sub>41,25,27,17,22</sub> | 11.2<br><sub>24,6,6,7,9</sub> |  | 7.0<br><sub>9,5,10,3,4</sub> |  | 1.5<br><sub>2,1,3,1,0</sub> |  | 0.4<br><sub>0,0,0,1,1</sub> |  | 1.1 | 0.8 | 1.2 | 19.7 |
| Malik Monk | 98% | 19.1<br><sub>8,14,30,24,18</sub> | 10.8<br><sub>2,8,24,13,12</sub> |  | 1.8<br><sub>1,0,1,2,0</sub> |  | 3.6<br><sub>1,3,7,3,7</sub> |  | 1.5<br><sub>0,0,5,3,2</sub> |  | 0.5 | 0.3 | 1.5 | 16.2 |
| Emanuel Sharp | 98% | 18.8<br><sub>18,24,20,10,31</sub> | 5.6<br><sub>0,2,9,3,9</sub> |  | 1.8<br><sub>0,1,3,1,5</sub> |  | 1.0<br><sub>0,1,1,2,0</sub> |  | 0.7<br><sub>0,0,3,1,3</sub> |  | 0.6 | 0.3 | 0.7 | 8.4 |
| Dylan Cardwell | 97% | 15.9<br><sub>-,-,-,13,15</sub> | 4.5<br><sub>-,-,-,4,9</sub> |  | 5.9<br><sub>-,-,-,6,2</sub> |  | 1.1<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.6 | 1.0 | 0.8 | 11.6 |
| Alex Karaban | 58% | 11.1<br><sub>12,10,-,-,11</sub> | 3.8<br><sub>6,0,-,-,0</sub> |  | 1.6<br><sub>0,1,-,-,1</sub> |  | 0.6<br><sub>0,1,-,-,0</sub> |  | 0.3<br><sub>2,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 6.0 |
| Nique Clifford | 91% | 9.4<br><sub>4,11,3,3,5</sub> | 3.6<br><sub>0,0,0,0,5</sub> |  | 1.5<br><sub>0,1,1,2,2</sub> |  | 1.1<br><sub>1,2,0,0,2</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Daeqwon Plowden | 64% | 8.3<br><sub>-,4,3,-,-</sub> | 3.1<br><sub>-,4,1,-,-</sub> |  | 1.0<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |

</details>

<details><summary>if Keegan Murray plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell (MIA) | 98% | 34.5<br><sub>34,35,29,43,38</sub> | 13.1<br><sub>10,15,15,11,22</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,6,0,2,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 8.0<br><sub>10,11,7,10,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,3,4,0,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.3 | 1.9 | 23.9 |
| Bam Adebayo (MIA) | 98% | 34.0<br><sub>33,33,31,41,33</sub> | 21.1<br><sub>24,27,16,35,18</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>9,9,9,10,10</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>3,3,4,4,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.7 | 0.7 | 1.9 | 35.1 |
| Giannis Antetokounmpo (MIA) | 98% | 33.4<br><sub>31,31,34,41,31</sub> | 29.4<br><sub>24,31,30,27,20</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>18,18,12,14,14</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>3,10,7,6,4</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 1.2 | 0.9 | 3.4 | 48.1 |
| Pelle Larsson (MIA) | 98% | 29.5<br><sub>31,24,30,35,29</sub> | 11.7<br><sub>17,18,9,7,13</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>6,3,3,3,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>8,3,2,4,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.9<br><sub>2,1,1,0,3</sub> |  | 1.1 | 0.3 | 1.5 | 19.0 |
| Andrew Wiggins (MIA) | 98% | 25.6<br><sub>29,30,24,23,21</sub> | 11.4<br><sub>18,12,7,3,2</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>2,2,0,4,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,1,2,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>4,2,2,1,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.8 | 1.1 | 17.2 |
| Klay Thompson (MIA) | 98% | 23.6<br><sub>17,26,27,35,23</sub> | 12.1<br><sub>3,25,19,30,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,0,1,5,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.8<br><sub>2,3,1,3,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.6<br><sub>1,7,4,8,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.4 | 1.0 | 16.0 |
| Bobby Portis (MIA) | 98% | 17.6<br><sub>23,17,18,18,14</sub> | 7.8<br><sub>11,8,2,4,0</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>9,3,3,10,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>4,1,2,5,0</sub> |  | 1.0<br><sub>1,2,0,0,0</sub> |  | 0.6 | 0.3 | 0.7 | 14.1 |
| Ryan Conwell (MIA) | 80% | 14.3<br><sub>-,7,8,17,30</sub> | 4.9<br><sub>-,4,5,0,13</sub> |  | 1.3<br><sub>-,0,1,2,1</sub> |  | 1.3<br><sub>-,0,1,2,2</sub> |  | 0.7<br><sub>-,1,1,0,3</sub> |  | 0.6 | 0.1 | 0.5 | 7.5 |
| Tim Hardaway Jr. (MIA) | 98% | 12.5<br><sub>22,12,19,7,4</sub> | 5.4<br><sub>14,2,9,0,0</sub> |  | 1.3<br><sub>3,1,0,0,0</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.8<br><sub>2,0,3,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.5 |
| Nikola Jovic (MIA) | 67% | 11.8<br><sub>7,16,7,-,12</sub> | 4.3<br><sub>5,0,2,-,1</sub> |  | 2.1<br><sub>3,4,1,-,0</sub> |  | 1.1<br><sub>0,3,0,-,1</sub> |  | 0.5<br><sub>1,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 7.6 |
| Dru Smith (MIA) | 67% | 8.3<br><sub>14,4,11,-,1</sub> | 2.7<br><sub>3,0,3,-,0</sub> |  | 1.1<br><sub>0,0,3,-,0</sub> |  | 1.4<br><sub>3,1,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.8 | 0.1 | 0.4 | 5.2 |
| Simone Fontecchio (MIA) | 52% | 7.6<br><sub>-,2,-,5,-</sub> | 3.9<br><sub>-,3,-,0,-</sub> |  | 1.4<br><sub>-,1,-,0,-</sub> |  | 0.6<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.8 |
| Keshad Johnson (MIA) | 16% | 6.4 | 3.0 |  | 1.3 |  | 0.3 |  | 0.2 |  | 0.4 | 0.2 | 0.3 | 4.6 |
| Nick Richards (MIA) | 63% | 6.4<br><sub>-,2,1,-,1</sub> | 2.6<br><sub>-,0,0,-,0</sub> |  | 2.3<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 5.1 |
| Myron Gardner (MIA) | 58% | 6.2<br><sub>-,2,1,-,1</sub> | 2.5<br><sub>-,0,0,-,0</sub> |  | 1.7<br><sub>-,1,0,-,0</sub> |  | 0.7<br><sub>-,1,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.9 |
| Darius Acuff Jr. (SAC) | 98% | 34.2<br><sub>41,37,37,42,33</sub> | 23.1<br><sub>34,38,25,22,22</sub> |  | 4.1<br><sub>6,5,5,3,3</sub> |  | 7.3<br><sub>14,5,6,12,8</sub> |  | 2.4<br><sub>3,9,2,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.3 | 3.0 | 34.4 |
| Zach LaVine (SAC) | 98% | 31.1<br><sub>39,21,28,35,35</sub> | 19.5<br><sub>21,11,23,21,14</sub> |  | 3.2<br><sub>3,0,4,4,4</sub> |  | 2.9<br><sub>5,1,1,1,3</sub> |  | 2.4<br><sub>3,0,5,3,1</sub> |  | 0.8 | 0.2 | 2.2 | 25.5 |
| Domantas Sabonis (SAC) | 98% | 30.8<br><sub>40,38,31,35,31</sub> | 14.9<br><sub>9,11,9,16,17</sub> |  | 11.6<br><sub>15,14,7,17,12</sub> |  | 5.3<br><sub>7,8,4,1,5</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.9 | 0.3 | 2.4 | 31.8 |
| De'Andre Hunter (SAC) | 98% | 28.4<br><sub>37,32,36,38,-</sub> | 13.1<br><sub>24,19,6,14,-</sub> |  | 4.5<br><sub>5,3,7,2,-</sub> |  | 1.6<br><sub>1,0,2,2,-</sub> |  | 1.6<br><sub>4,2,0,1,-</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.4 | 19.2 |
| Precious Achiuwa (SAC) | 98% | 23.9<br><sub>41,25,27,17,22</sub> | 10.2<br><sub>24,6,6,7,9</sub> |  | 6.4<br><sub>9,5,10,3,4</sub> |  | 1.4<br><sub>2,1,3,1,0</sub> |  | 0.3<br><sub>0,0,0,1,1</sub> |  | 0.9 | 0.7 | 1.1 | 18.0 |
| Keegan Murray (SAC) | 100% | 23.9<br><sub>-,-,-,-,-</sub> | 9.4<br><sub>-,-,-,-,-</sub> |  | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> | 1.5 | 0.7 | 0.8 | 0.9 | 14.8 |
| Leaky Black (SAC) | 64% | 22.6<br><sub>-,-,25,22,40</sub> | 5.6<br><sub>-,-,12,3,12</sub> |  | 3.9<br><sub>-,-,3,6,3</sub> |  | 1.6<br><sub>-,-,1,1,5</sub> |  | 0.7<br><sub>-,-,4,0,4</sub> |  | 1.0 | 0.4 | 0.7 | 11.0 |
| Malik Monk (SAC) | 98% | 17.5<br><sub>8,14,30,24,18</sub> | 9.9<br><sub>2,8,24,13,12</sub> |  | 1.7<br><sub>1,0,1,2,0</sub> |  | 3.5<br><sub>1,3,7,3,7</sub> |  | 1.3<br><sub>0,0,5,3,2</sub> |  | 0.5 | 0.3 | 1.3 | 15.1 |
| Emanuel Sharp (SAC) | 98% | 17.2<br><sub>18,24,20,10,31</sub> | 4.9<br><sub>0,2,9,3,9</sub> |  | 1.7<br><sub>0,1,3,1,5</sub> |  | 0.9<br><sub>0,1,1,2,0</sub> |  | 0.6<br><sub>0,0,3,1,3</sub> |  | 0.5 | 0.2 | 0.7 | 7.5 |
| Dylan Cardwell (SAC) | 97% | 15.1<br><sub>-,-,-,13,15</sub> | 4.4<br><sub>-,-,-,4,9</sub> |  | 5.5<br><sub>-,-,-,6,2</sub> |  | 1.1<br><sub>-,-,-,0,3</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.0 | 0.8 | 11.0 |
| Nique Clifford (SAC) | 91% | 8.6<br><sub>4,11,3,3,5</sub> | 3.6<br><sub>0,0,0,0,5</sub> |  | 1.4<br><sub>0,1,1,2,2</sub> |  | 1.1<br><sub>1,2,0,0,2</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.6 | 6.1 |
| Alex Karaban (SAC) | 58% | 8.6<br><sub>12,10,-,-,11</sub> | 3.3<br><sub>6,0,-,-,0</sub> |  | 1.2<br><sub>0,1,-,-,1</sub> |  | 0.5<br><sub>0,1,-,-,0</sub> |  | 0.2<br><sub>2,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.0 |
| Daeqwon Plowden (SAC) | 64% | 7.3<br><sub>-,4,3,-,-</sub> | 3.0<br><sub>-,4,1,-,-</sub> |  | 0.9<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-08/`._
