# NBA model · Sat 14 Nov 2026 (US date)

Updated **Sun 15 Nov, 05:00 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-14/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| MEM to win | BKN @ MEM | draftkings | 1.68 | 1.59 | 1.37 | 72.9% | 63.1% | 63.1% | +5.7% | +22.1% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| CHI to win | CHI @ MIN | betfair_ex_au | 7.84 | 7.36 | 6.89 | 14.5% | 13.6% | 13.6% | +6.5% | +13.9% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| CLE to win | DAL @ CLE | draftkings | 2.20 | Evan Mobley | 52.9% | 60.0% | +11.2% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DEN @ NOP | Sun 15 Nov 11:00 | 124.0–114.3 | DEN 75% | 1.33 / 4.06 | NOP +9.5 | 238.5 | NOP +12.5 covers 57%; o234.5 58% |
| DAL @ CLE | Sun 15 Nov 11:30 | 116.2–117.3 | DAL 47% | 2.13 / 1.89 | CLE -1.5 | 233.5 | CLE +2.5 covers 59%; o231.5 54% |
| DET @ MIA | Sun 15 Nov 12:00 | 118.6–111.7 | DET 69% | 1.45 / 3.22 | MIA +7.5 | 230.5 | MIA +5.5 covers 45%; o228.5 54% |
| BKN @ MEM | Sun 15 Nov 12:00 | 110.2–118.3 | BKN 28% | 3.55 / 1.39 | MEM -8.5 | 228.5 | MEM -2.5 covers 66%; o228.5 50% |
| CHI @ MIN | Sun 15 Nov 12:00 | 108.7–126.5 | CHI 10% | 9.83 / 1.11 | MIN -17.5 | 235.5 | MIN -15.5 covers 57%; o234.5 52% |

### DEN @ NOP
Out: Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Julian Strawther (DEN), Cam Whitmore (DEN)

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 36.1<br><sub>39,28,34,39,32</sub> | 26.2<br><sub>35,14,16,38,30</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>5,5,6,2,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.6<br><sub>6,7,8,2,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,2,2,5,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.6 | 2.3 | 37.2 |
| Nikola Jokic | 98% | 35.9<br><sub>36,30,36,39,37</sub> | 28.0<br><sub>26,32,19,25,27</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 12.7<br><sub>9,10,13,16,11</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 10.6<br><sub>8,11,8,9,8</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>2,0,1,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 1.0 | 3.4 | 51.3 |
| Christian Braun | 98% | 33.1<br><sub>37,28,29,32,37</sub> | 13.2<br><sub>14,11,6,4,12</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>3,3,4,5,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.6<br><sub>3,3,1,3,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,1,0,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.5 | 1.0 | 20.2 |
| Cameron Johnson | 98% | 29.5<br><sub>34,30,29,31,30</sub> | 13.3<br><sub>7,12,18,8,23</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>4,2,4,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,2,1,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.0<br><sub>1,4,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.4 | 1.1 | 19.7 |
| Aaron Gordon | 98% | 28.8<br><sub>30,25,27,30,27</sub> | 13.6<br><sub>5,17,12,3,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>6,1,5,5,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>2,0,0,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,1,0,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.4 | 1.3 | 21.9 |
| DeMar DeRozan | 88% | 21.9<br><sub>20,-,22,19,20</sub> | 11.9<br><sub>9,-,11,7,8</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>0,-,1,4,1</sub> |  | 3.2<br><sub>1,-,5,2,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.7 | 0.3 | 1.2 | 17.2 |
| Spencer Jones | 71% | 17.3<br><sub>-,-,21,14,22</sub> | 4.7<br><sub>-,-,13,0,3</sub> |  | 2.8<br><sub>-,-,6,0,1</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,3,0,1</sub> |  | 0.7 | 0.6 | 0.5 | 8.2 |
| Trevon Brazile | 98% | 15.6<br><sub>18,23,14,14,13</sub> | 5.2<br><sub>6,6,3,5,7</sub> |  | 4.0<br><sub>5,7,4,2,5</sub> |  | 0.8<br><sub>1,1,2,0,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 10.0 |
| Marvin Bagley III | 98% | 13.1<br><sub>12,14,12,12,12</sub> | 6.6<br><sub>6,10,10,6,4</sub> |  | 4.1<br><sub>4,2,3,3,2</sub> |  | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 11.4 |
| Tyus Jones | 96% | 10.1<br><sub>8,18,13,6,11</sub> | 2.8<br><sub>2,6,3,2,0</sub> |  | 0.9<br><sub>0,1,4,0,1</sub> |  | 1.9<br><sub>1,8,4,0,4</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.5 |
| Bryce Hopkins | 63% | 8.7<br><sub>-,28,3,3,-</sub> | 3.0<br><sub>-,18,3,2,-</sub> |  | 1.5<br><sub>-,4,1,0,-</sub> |  | 0.5<br><sub>-,1,0,0,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.0 |
| Zeke Nnaji | 35% | 7.1<br><sub>-,4,-,-,-</sub> | 2.5<br><sub>-,2,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.5 |
| Alpha Diallo | 58% | 6.2<br><sub>6,4,-,1,-</sub> | 2.5<br><sub>0,0,-,0,-</sub> |  | 1.0<br><sub>1,0,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zion Williamson | 98% | 33.8<br><sub>36,31,-,30,33</sub> | 21.6<br><sub>13,25,-,29,22</sub> |  | 5.9<br><sub>8,4,-,4,5</sub> |  | 3.9<br><sub>4,2,-,2,4</sub> |  | 0.2<br><sub>0,0,-,1,0</sub> |  | 1.4 | 0.6 | 2.1 | 31.4 |
| Jeremiah Fears | 98% | 32.4<br><sub>36,29,29,28,34</sub> | 17.1<br><sub>24,25,11,14,18</sub> |  | 4.7<br><sub>5,6,3,4,5</sub> |  | 5.8<br><sub>5,5,8,5,7</sub> |  | 1.5<br><sub>0,3,1,2,0</sub> |  | 1.3 | 0.5 | 2.6 | 27.6 |
| Saddiq Bey | 98% | 31.8<br><sub>31,26,24,29,35</sub> | 18.5<br><sub>17,13,9,15,30</sub> |  | 4.9<br><sub>5,4,0,1,10</sub> |  | 2.8<br><sub>4,3,4,2,0</sub> |  | 2.4<br><sub>3,1,1,3,6</sub> |  | 0.9 | 0.2 | 1.1 | 26.2 |
| Herbert Jones | 98% | 27.7<br><sub>14,20,24,25,32</sub> | 8.6<br><sub>0,4,10,2,8</sub> |  | 3.2<br><sub>4,0,6,2,2</sub> |  | 2.2<br><sub>0,1,1,3,3</sub> |  | 1.1<br><sub>0,0,2,0,0</sub> |  | 1.3 | 0.5 | 1.1 | 14.0 |
| Derik Queen | 98% | 24.8<br><sub>10,21,21,14,23</sub> | 13.1<br><sub>6,8,16,9,10</sub> |  | 6.9<br><sub>4,5,4,0,6</sub> |  | 3.2<br><sub>1,3,0,0,2</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 1.0 | 0.8 | 2.2 | 23.2 |
| Karlo Matkovic | 96% | 22.9<br><sub>18,19,17,22,19</sub> | 9.4<br><sub>18,3,4,4,1</sub> |  | 5.1<br><sub>3,3,6,4,3</sub> |  | 1.4<br><sub>1,2,2,1,0</sub> |  | 1.1<br><sub>4,1,0,0,0</sub> |  | 0.7 | 0.8 | 1.0 | 15.9 |
| Jordan Poole | 67% | 22.1<br><sub>-,-,34,21,21</sub> | 10.5<br><sub>-,-,7,14,13</sub> |  | 2.2<br><sub>-,-,3,0,2</sub> |  | 3.0<br><sub>-,-,2,1,5</sub> |  | 1.7<br><sub>-,-,1,2,1</sub> |  | 0.7 | 0.4 | 1.3 | 15.6 |
| Yves Missi | 90% | 19.3<br><sub>-,-,-,-,-</sub> | 5.7<br><sub>-,-,-,-,-</sub> |  | 5.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 1.4 | 0.8 | 13.0 |
| Bennedict Mathurin | 98% | 18.0<br><sub>7,9,24,-,10</sub> | 7.9<br><sub>2,6,6,-,0</sub> |  | 2.9<br><sub>0,0,2,-,0</sub> |  | 1.5<br><sub>0,1,0,-,0</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.9 | 12.3 |
| DeAndre Jordan | 52% | 15.7<br><sub>-,-,-,11,17</sub> | 4.0<br><sub>-,-,-,0,6</sub> |  | 5.8<br><sub>-,-,-,3,8</sub> |  | 0.9<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 10.8 |
| Jaron Pierre Jr. | 88% | 8.8<br><sub>-,-,-,7,4</sub> | 3.5<br><sub>-,-,-,4,0</sub> |  | 1.6<br><sub>-,-,-,4,0</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.3<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.7 | 5.8 |
| AJ Johnson | 64% | 8.8<br><sub>-,3,12,7,4</sub> | 2.6<br><sub>-,2,2,2,1</sub> |  | 1.2<br><sub>-,0,2,1,0</sub> |  | 0.9<br><sub>-,0,3,0,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.7 |
| Julian Reese | 67% | 8.8<br><sub>-,3,9,7,4</sub> | 2.6<br><sub>-,0,2,2,0</sub> |  | 1.5<br><sub>-,0,0,2,2</sub> |  | 0.6<br><sub>-,0,0,1,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 4.7 |
| Malik Dia | 80% | 7.3<br><sub>-,-,-,-,4</sub> | 2.6<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>


### DAL @ CLE
Out: Sam Merrill (CLE), Nae'Qwan Tomlin (CLE), Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.2–117.3 | DAL 47% | 2.13 / 1.89 | CLE -1.5 | 233.5 | CLE +2.5 covers 59%; o231.5 54% |
| Expected (weighted by chance each plays) | 115.1–117.6 | DAL 43% | 2.34 / 1.75 | CLE -2.5 | 232.5 | CLE +2.5 covers 63%; o231.5 53% |
| if Evan Mobley plays | 114.5–118.1 | DAL 40% | 2.50 / 1.67 | CLE -3.5 | 232.5 | CLE +2.5 covers 65%; o231.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Evan Mobley (CLE) | Day-To-Day | 70% | 30.7 | 15.7 | 7.9 | 3.5 | 1.3 | 0.8 | 1.6 | 1.6 | 27.1 | full tables below |
| Max Christie (DAL) | Doubtful | 20% | 12.3 | 4.5 | 1.4 | 0.7 | 0.6 | 0.4 | 0.1 | 0.5 | 6.6 | small |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 33.9<br><sub>40,33,28,39,27</sub> | 23.3<br><sub>19,21,25,43,12</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>10,10,5,10,7</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 5.6<br><sub>5,7,12,6,3</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.7 | 2.6 | 35.7 |
| Kyrie Irving | 98% | 33.5<br><sub>36,28,29,38,27</sub> | 21.7<br><sub>29,14,21,35,10</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>7,2,3,0,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,2,4,4,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>5,0,2,7,2</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.4 | 1.9 | 29.9 |
| P.J. Washington | 98% | 32.3<br><sub>39,33,25,35,16</sub> | 14.2<br><sub>21,26,6,13,10</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>10,6,5,9,3</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,6,2,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.8 | 1.4 | 22.4 |
| Naji Marshall | 91% | 24.0<br><sub>26,25,15,25,23</sub> | 11.8<br><sub>22,7,8,6,13</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,1,1,5,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>3,5,2,2,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.8<br><sub>3,0,1,0,1</sub> |  | 0.9 | 0.1 | 1.5 | 18.4 |
| Zaccharie Risacher | 97% | 21.0<br><sub>18,21,16,15,25</sub> | 7.4<br><sub>2,4,11,4,22</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>1,4,6,2,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.1<br><sub>2,1,1,0,3</sub> |  | 0.8<br><sub>0,0,1,0,4</sub> |  | 0.8 | 0.6 | 0.9 | 12.5 |
| Daniel Gafford | 98% | 19.6<br><sub>18,18,19,20,16</sub> | 8.4<br><sub>2,7,18,8,3</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>4,1,5,2,3</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,1,2,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 15.3 |
| Walter Clayton Jr. | 91% | 17.9<br><sub>21,23,16,25,22</sub> | 6.5<br><sub>8,12,5,6,5</sub> |  | 2.7<br><sub>6,4,4,6,1</sub> |  | 3.1<br><sub>5,2,6,4,4</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.2 | 1.3 | 12.3 |
| Caleb Martin | 98% | 16.2<br><sub>20,11,19,19,21</sub> | 4.1<br><sub>0,0,2,0,7</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,0,2,3,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>2,0,2,5,5</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.7 | 0.2 | 0.6 | 7.7 |
| Santi Aldama | 98% | 14.9<br><sub>-,13,15,19,10</sub> | 7.3<br><sub>-,8,12,10,3</sub> |  | 3.4<br><sub>-,9,2,4,1</sub> |  | 1.2<br><sub>-,1,0,1,1</sub> |  | 0.7<br><sub>-,0,2,1,1</sub> |  | 0.5 | 0.3 | 0.8 | 11.9 |
| Morez Johnson Jr. | 92% | 14.1<br><sub>18,24,19,-,13</sub> | 5.6<br><sub>8,13,4,-,0</sub> |  | 2.7<br><sub>3,17,9,-,2</sub> |  | 1.1<br><sub>1,2,1,-,0</sub> |  | 0.3<br><sub>1,1,0,-,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.5 |
| Marcus Sasser | 67% | 11.3<br><sub>5,-,9,-,9</sub> | 3.9<br><sub>0,-,4,-,3</sub> |  | 0.9<br><sub>1,-,0,-,1</sub> |  | 1.3<br><sub>2,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Moussa Cisse | 64% | 6.9<br><sub>-,1,5,-,8</sub> | 2.3<br><sub>-,0,2,-,0</sub> |  | 2.6<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,1,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.2 |
| Tobi Lawal | 63% | 6.7<br><sub>-,1,5,-,12</sub> | 2.6<br><sub>-,0,2,-,0</sub> |  | 1.4<br><sub>-,0,0,-,6</sub> |  | 0.5<br><sub>-,0,0,-,1</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Jett Howard | 63% | 6.2<br><sub>-,1,3,-,5</sub> | 2.8<br><sub>-,0,5,-,3</sub> |  | 0.7<br><sub>-,0,1,-,0</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,1,-,1</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 34.5<br><sub>30,34,25,33,35</sub> | 19.5<br><sub>17,7,11,32,20</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>6,2,3,2,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>3,5,5,4,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>3,1,2,5,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.5 | 3.1 | 31.2 |
| Donovan Mitchell | 98% | 34.4<br><sub>33,37,23,36,33</sub> | 26.2<br><sub>23,37,11,23,25</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>7,4,2,7,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>8,4,4,6,7</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,5,1,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.4 | 2.8 | 37.0 |
| Peyton Watson | 98% | 29.6<br><sub>28,29,21,30,30</sub> | 13.1<br><sub>13,12,13,7,4</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>9,6,2,5,4</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,3,1,4,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4<br><sub>1,1,2,2,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 1.4 | 1.5 | 20.6 |
| Jarrett Allen | 98% | 29.0<br><sub>-,-,19,32,32</sub> | 14.0<br><sub>-,-,12,11,9</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 9.3<br><sub>-,-,7,14,8</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>-,-,1,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.1<br><sub>-,-,1,0,0</sub> |  | 0.9 | 1.5 | 1.2 | 25.0 |
| Jaylon Tyson | 97% | 25.3<br><sub>-,-,-,23,30</sub> | 10.2<br><sub>-,-,-,3,16</sub> | 11.5 · –<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>-,-,-,0,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.5<br><sub>-,-,-,1,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.4 | 1.2 | 16.8 |
| Tyrese Proctor | 93% | 24.4<br><sub>19,23,23,23,27</sub> | 10.3<br><sub>3,7,6,15,22</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>6,3,1,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>0,2,0,3,5</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.1 | 1.1 | 16.8 |
| Meleek Thomas | 91% | 23.8<br><sub>27,24,27,22,18</sub> | 11.7<br><sub>12,9,18,14,12</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>1,4,3,4,0</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>3,0,3,1,3</sub> |  | 1.8<br><sub>2,3,4,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.3 | 1.0 | 16.0 |
| Mario Hezonja | 98% | 16.4<br><sub>27,19,17,7,9</sub> | 6.4<br><sub>15,0,10,0,4</sub> |  | 4.6<br><sub>10,5,3,0,4</sub> |  | 1.1<br><sub>1,1,0,0,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5 | 0.3 | 0.7 | 12.1 |
| Thomas Bryant | 67% | 16.0<br><sub>16,15,15,-,16</sub> | 8.4<br><sub>13,5,11,-,9</sub> |  | 4.1<br><sub>6,3,2,-,1</sub> |  | 0.7<br><sub>0,1,0,-,1</sub> |  | 0.9<br><sub>1,1,2,-,0</sub> |  | 0.4 | 0.6 | 0.7 | 13.2 |
| Craig Porter Jr. | 72% | 13.2<br><sub>3,15,17,-,9</sub> | 2.7<br><sub>0,0,9,-,0</sub> |  | 2.4<br><sub>0,1,2,-,2</sub> |  | 2.3<br><sub>0,1,4,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.4 | 0.6 | 7.4 |
| Riley Minix | 47% | 11.9<br><sub>-,10,17,-,-</sub> | 4.3<br><sub>-,8,2,-,-</sub> |  | 2.1<br><sub>-,3,2,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.5<br><sub>-,2,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 7.0 |
| Norchad Omier | 48% | 8.5<br><sub>3,-,12,-,-</sub> | 2.7<br><sub>0,-,0,-,-</sub> |  | 2.2<br><sub>2,-,3,-,-</sub> |  | 0.8<br><sub>1,-,2,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.6 |
| Ernest Udeh Jr. | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Khalifa Diop | 3% | 8.4 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.7 |

</details>

<details><summary>if Evan Mobley plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell (CLE) | 98% | 32.5<br><sub>33,37,23,36,33</sub> | 24.3<br><sub>23,37,11,23,25</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>7,4,2,7,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>8,4,4,6,7</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>1,5,1,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.3 | 0.4 | 2.4 | 34.3 |
| James Harden (CLE) | 98% | 32.4<br><sub>30,34,25,33,35</sub> | 17.3<br><sub>17,7,11,32,20</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>6,2,3,2,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>3,5,5,4,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>3,1,2,5,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.5 | 2.8 | 28.0 |
| Evan Mobley (CLE) | 100% | 30.7<br><sub>32,33,24,33,-</sub> | 15.7<br><sub>22,12,9,10,-</sub> |  | 7.9<br><sub>6,9,2,5,-</sub> |  | 3.5<br><sub>4,5,3,3,-</sub> |  | 1.3<br><sub>3,1,2,0,-</sub> |  | 0.8 | 1.6 | 1.6 | 27.1 |
| Peyton Watson (CLE) | 98% | 27.1<br><sub>28,29,21,30,30</sub> | 11.9<br><sub>13,12,13,7,4</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>9,6,2,5,4</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>2,3,1,4,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>1,1,2,2,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 1.3 | 1.4 | 18.6 |
| Jarrett Allen (CLE) | 98% | 25.5<br><sub>-,-,19,32,32</sub> | 12.6<br><sub>-,-,12,11,9</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 8.0<br><sub>-,-,7,14,8</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>-,-,1,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.1<br><sub>-,-,1,0,0</sub> |  | 0.9 | 1.3 | 1.1 | 22.1 |
| Jaylon Tyson (CLE) | 97% | 21.9<br><sub>-,-,-,23,30</sub> | 8.5<br><sub>-,-,-,3,16</sub> | 11.5 · –<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>-,-,-,0,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2<br><sub>-,-,-,1,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.3 | 1.0 | 14.3 |
| Tyrese Proctor (CLE) | 93% | 21.0<br><sub>19,23,23,23,27</sub> | 8.8<br><sub>3,7,6,15,22</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>6,3,1,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,2,0,3,5</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.1 | 1.0 | 14.5 |
| Meleek Thomas (CLE) | 91% | 20.5<br><sub>27,24,27,22,18</sub> | 9.7<br><sub>12,9,18,14,12</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,4,3,4,0</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>3,0,3,1,3</sub> |  | 1.5<br><sub>2,3,4,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.3 | 0.8 | 13.3 |
| Thomas Bryant (CLE) | 67% | 13.4<br><sub>16,15,15,-,16</sub> | 7.1<br><sub>13,5,11,-,9</sub> |  | 3.5<br><sub>6,3,2,-,1</sub> |  | 0.6<br><sub>0,1,0,-,1</sub> |  | 0.8<br><sub>1,1,2,-,0</sub> |  | 0.3 | 0.5 | 0.7 | 11.2 |
| Mario Hezonja (CLE) | 98% | 13.4<br><sub>27,19,17,7,9</sub> | 5.4<br><sub>15,0,10,0,4</sub> |  | 3.7<br><sub>10,5,3,0,4</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 10.0 |
| Craig Porter Jr. (CLE) | 72% | 11.3<br><sub>3,15,17,-,9</sub> | 2.5<br><sub>0,0,9,-,0</sub> |  | 2.0<br><sub>0,1,2,-,2</sub> |  | 2.1<br><sub>0,1,4,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.7 |
| Khalifa Diop (CLE) | 3% | 8.8 | 3.7 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 6.1 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Riley Minix (CLE) | 47% | 7.8<br><sub>-,10,17,-,-</sub> | 3.0<br><sub>-,8,2,-,-</sub> |  | 1.4<br><sub>-,3,2,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.8 |
| Norchad Omier (CLE) | 48% | 6.8<br><sub>3,-,12,-,-</sub> | 2.6<br><sub>0,-,0,-,-</sub> |  | 1.8<br><sub>2,-,3,-,-</sub> |  | 0.8<br><sub>1,-,2,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.2 |
| Cooper Flagg (DAL) | 98% | 33.9<br><sub>40,33,28,39,27</sub> | 23.3<br><sub>19,21,25,43,12</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>10,10,5,10,7</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 5.6<br><sub>5,7,12,6,3</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.7 | 2.7 | 35.7 |
| Kyrie Irving (DAL) | 98% | 33.5<br><sub>36,28,29,38,27</sub> | 21.7<br><sub>29,14,21,35,10</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>7,2,3,0,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>5,2,4,4,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>5,0,2,7,2</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.4 | 1.9 | 29.9 |
| P.J. Washington (DAL) | 98% | 32.3<br><sub>39,33,25,35,16</sub> | 14.0<br><sub>21,26,6,13,10</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>10,6,5,9,3</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,6,2,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.8 | 1.4 | 22.2 |
| Naji Marshall (DAL) | 91% | 24.0<br><sub>26,25,15,25,23</sub> | 11.7<br><sub>22,7,8,6,13</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,1,1,5,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>3,5,2,2,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.8<br><sub>3,0,1,0,1</sub> |  | 0.9 | 0.1 | 1.5 | 18.3 |
| Zaccharie Risacher (DAL) | 97% | 20.9<br><sub>18,21,16,15,25</sub> | 7.4<br><sub>2,4,11,4,22</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>1,4,6,2,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>2,1,1,0,3</sub> |  | 0.8<br><sub>0,0,1,0,4</sub> |  | 0.8 | 0.6 | 0.9 | 12.5 |
| Daniel Gafford (DAL) | 98% | 19.6<br><sub>18,18,19,20,16</sub> | 8.4<br><sub>2,7,18,8,3</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>4,1,5,2,3</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,1,2,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 15.2 |
| Walter Clayton Jr. (DAL) | 91% | 17.9<br><sub>21,23,16,25,22</sub> | 6.5<br><sub>8,12,5,6,5</sub> |  | 2.7<br><sub>6,4,4,6,1</sub> |  | 3.0<br><sub>5,2,6,4,4</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.2 | 1.3 | 12.3 |
| Caleb Martin (DAL) | 98% | 16.2<br><sub>20,11,19,19,21</sub> | 4.0<br><sub>0,0,2,0,7</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,0,2,3,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>2,0,2,5,5</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.7 | 0.2 | 0.6 | 7.7 |
| Santi Aldama (DAL) | 98% | 14.8<br><sub>-,13,15,19,10</sub> | 7.2<br><sub>-,8,12,10,3</sub> |  | 3.4<br><sub>-,9,2,4,1</sub> |  | 1.2<br><sub>-,1,0,1,1</sub> |  | 0.7<br><sub>-,0,2,1,1</sub> |  | 0.5 | 0.3 | 0.8 | 11.8 |
| Morez Johnson Jr. (DAL) | 92% | 14.2<br><sub>18,24,19,-,13</sub> | 5.6<br><sub>8,13,4,-,0</sub> |  | 2.7<br><sub>3,17,9,-,2</sub> |  | 1.1<br><sub>1,2,1,-,0</sub> |  | 0.3<br><sub>1,1,0,-,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.4 |
| Marcus Sasser (DAL) | 67% | 11.2<br><sub>5,-,9,-,9</sub> | 3.9<br><sub>0,-,4,-,3</sub> |  | 0.9<br><sub>1,-,0,-,1</sub> |  | 1.3<br><sub>2,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.0 |
| Moussa Cisse (DAL) | 64% | 7.0<br><sub>-,1,5,-,8</sub> | 2.4<br><sub>-,0,2,-,0</sub> |  | 2.6<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,1,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.2 |
| Tobi Lawal (DAL) | 63% | 6.7<br><sub>-,1,5,-,12</sub> | 2.6<br><sub>-,0,2,-,0</sub> |  | 1.4<br><sub>-,0,0,-,6</sub> |  | 0.5<br><sub>-,0,0,-,1</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Jett Howard (DAL) | 63% | 6.1<br><sub>-,1,3,-,5</sub> | 2.8<br><sub>-,0,5,-,3</sub> |  | 0.7<br><sub>-,0,1,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,1,-,1</sub> |  | 0.2 | 0.1 | 0.2 | 3.9 |

</details>


### DET @ MIA
Out: Jalen Duren (DET), Isaiah Joe (DET)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.6–111.7 | DET 69% | 1.45 / 3.22 | MIA +7.5 | 230.5 | MIA +5.5 covers 45%; o228.5 54% |
| Expected (weighted by chance each plays) | 118.0–112.6 | DET 65% | 1.53 / 2.88 | MIA +5.5 | 230.5 | MIA +5.5 covers 50%; o228.5 55% |
| if Klay Thompson plays | 118.2–111.9 | DET 67% | 1.49 / 3.04 | MIA +6.5 | 230.5 | MIA +5.5 covers 47%; o228.5 53% |
| if Pelle Larsson plays | 118.0–112.4 | DET 66% | 1.52 / 2.91 | MIA +5.5 | 230.5 | MIA +5.5 covers 49%; o228.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Klay Thompson (MIA) | Day-To-Day | 70% | 28.7 | 13.5 | 2.1 | 1.8 | 2.9 | 0.7 | 0.6 | 1.1 | 17.4 | full tables below |
| Pelle Larsson (MIA) | Day-To-Day | 70% | 30.4 | 11.5 | 3.6 | 3.1 | 1.1 | 1.0 | 0.2 | 1.8 | 18.2 | full tables below |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 35.1<br><sub>27,40,38,27,48</sub> | 27.2<br><sub>33,26,14,17,52</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,7,4,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 9.0<br><sub>7,11,8,7,11</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,1,1,0,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.7 | 3.8 | 41.5 |
| Duncan Robinson | 98% | 32.0<br><sub>32,37,27,34,41</sub> | 16.6<br><sub>24,27,12,22,13</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,1,0,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,2,3,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 3.1<br><sub>6,7,3,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.1 | 22.3 |
| Daniss Jenkins | 98% | 30.8<br><sub>23,21,32,36,42</sub> | 15.2<br><sub>2,5,31,22,21</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,1,5,6,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>7,4,4,8,0</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>0,1,8,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 1.9 | 24.3 |
| Ausar Thompson | 98% | 30.0<br><sub>26,34,24,28,43</sub> | 11.0<br><sub>14,11,7,8,17</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>6,17,11,5,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>4,3,3,4,11</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.8 | 1.1 | 1.9 | 23.4 |
| John Collins | 98% | 26.4<br><sub>19,26,32,28,25</sub> | 11.6<br><sub>4,16,8,24,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>3,1,4,10,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>1,0,1,3,0</sub> |  | 1.0<br><sub>0,0,1,2,2</sub> |  | 0.8 | 0.8 | 1.3 | 18.8 |
| Paul Reed | 98% | 26.2<br><sub>28,30,20,21,38</sub> | 12.8<br><sub>11,8,8,4,13</sub> |  | 8.3<br><sub>5,7,10,10,11</sub> |  | 2.3<br><sub>4,4,0,2,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.1 | 1.7 | 23.4 |
| Kevin Huerter | 98% | 24.5<br><sub>20,20,35,33,24</sub> | 10.8<br><sub>9,8,24,12,11</sub> |  | 3.2<br><sub>2,1,5,2,1</sub> |  | 2.6<br><sub>3,0,5,3,0</sub> |  | 1.6<br><sub>3,2,4,0,1</sub> |  | 1.1 | 0.5 | 0.9 | 16.6 |
| Javonte Green | 98% | 16.8<br><sub>20,15,17,11,15</sub> | 6.1<br><sub>5,1,7,7,5</sub> |  | 2.5<br><sub>2,3,2,1,1</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.8<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.3 | 0.4 | 9.3 |
| Ronald Holland II | 98% | 14.4<br><sub>20,12,14,15,14</sub> | 5.6<br><sub>11,3,5,1,2</sub> |  | 3.1<br><sub>2,2,2,5,5</sub> |  | 1.1<br><sub>0,0,1,2,2</sub> |  | 0.5<br><sub>3,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.9 | 9.8 |
| Taurean Prince | 30% | 8.4<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Elijah Harkless | 30% | 6.7<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 1.0 |
| Tolu Smith | 52% | 5.8<br><sub>8,5,-,-,-</sub> | 2.4<br><sub>0,1,-,-,-</sub> |  | 2.1<br><sub>2,1,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.9 |
| Isaac Jones | 52% | 5.7<br><sub>6,-,-,2,-</sub> | 5.8<br><sub>2,-,-,0,-</sub> |  | 1.5<br><sub>5,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 7.6 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 37.5<br><sub>43,38,40,38,39</sub> | 15.0<br><sub>11,22,17,19,22</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,3,5,5</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.3<br><sub>10,8,11,8,17</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,4,2,3,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 2.6 | 26.3 |
| Bam Adebayo | 98% | 36.2<br><sub>41,33,34,37,38</sub> | 20.1<br><sub>35,18,18,11,37</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 9.8<br><sub>10,10,8,8,14</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>4,0,4,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>1,0,1,0,2</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.5 | 0.8 | 1.9 | 33.7 |
| Giannis Antetokounmpo | 98% | 35.4<br><sub>41,31,34,31,31</sub> | 29.2<br><sub>27,20,29,30,37</sub> | 27.5 · –<br><sub>o 50% · u 50%</sub> | 12.3<br><sub>14,14,14,11,9</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 5.7<br><sub>6,4,3,4,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>0,1,0,1,1</sub> |  | 1.1 | 1.1 | 3.7 | 47.2 |
| Andrew Wiggins | 98% | 31.1<br><sub>23,21,32,19,32</sub> | 12.2<br><sub>3,2,6,13,8</sub> |  | 4.0<br><sub>4,6,3,0,3</sub> |  | 2.1<br><sub>1,4,1,0,4</sub> |  | 1.8<br><sub>1,0,2,2,1</sub> |  | 1.0 | 1.0 | 1.3 | 18.4 |
| Ryan Conwell | 88% | 28.7<br><sub>17,30,19,21,33</sub> | 10.1<br><sub>0,13,6,5,20</sub> |  | 3.0<br><sub>2,1,2,4,5</sub> |  | 2.1<br><sub>2,2,2,2,2</sub> |  | 1.9<br><sub>0,3,2,1,4</sub> |  | 0.9 | 0.2 | 1.1 | 15.2 |
| Bobby Portis | 98% | 22.7<br><sub>18,14,20,17,15</sub> | 9.4<br><sub>4,0,4,5,5</sub> |  | 5.8<br><sub>10,5,1,1,3</sub> |  | 1.4<br><sub>5,0,1,1,2</sub> |  | 1.4<br><sub>0,0,1,1,1</sub> |  | 0.7 | 0.3 | 0.8 | 16.7 |
| Tim Hardaway Jr. | 83% | 20.1<br><sub>7,4,7,-,20</sub> | 7.8<br><sub>0,0,0,-,4</sub> |  | 2.0<br><sub>0,0,0,-,3</sub> |  | 0.9<br><sub>0,1,0,-,2</sub> |  | 1.2<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 10.7 |
| Dru Smith | 58% | 15.9<br><sub>-,1,-,-,6</sub> | 4.6<br><sub>-,0,-,-,0</sub> |  | 2.1<br><sub>-,0,-,-,0</sub> |  | 2.1<br><sub>-,0,-,-,1</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 1.1 | 0.3 | 0.8 | 8.8 |
| Myron Gardner | 64% | 14.3<br><sub>-,1,-,10,19</sub> | 4.3<br><sub>-,0,-,4,0</sub> |  | 3.7<br><sub>-,0,-,3,4</sub> |  | 1.2<br><sub>-,0,-,1,2</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 9.2 |
| Nikola Jovic | 48% | 13.9<br><sub>-,12,-,-,-</sub> | 4.7<br><sub>-,1,-,-,-</sub> |  | 2.6<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.8 | 8.4 |
| Keshad Johnson | 38% | 13.7<br><sub>-,-,-,-,-</sub> | 5.6<br><sub>-,-,-,-,-</sub> |  | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.4 | 0.7 | 8.9 |
| Simone Fontecchio | 58% | 12.5<br><sub>5,-,-,7,7</sub> | 5.4<br><sub>0,-,-,3,0</sub> |  | 2.2<br><sub>0,-,-,0,0</sub> |  | 0.8<br><sub>0,-,-,0,2</sub> |  | 0.8<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.4 |
| Vladislav Goldin | 8% | 9.2 | 2.7 |  | 2.6 |  | 0.7 |  | 0.1 |  | 0.3 | 0.8 | 0.7 | 5.9 |
| Nick Richards | 43% | 8.8<br><sub>-,1,-,-,-</sub> | 3.1<br><sub>-,0,-,-,-</sub> |  | 3.0<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.5 | 0.7 | 6.3 |
| Tre Donaldson | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Pelle Larsson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | 98% | 35.2<br><sub>27,40,38,27,48</sub> | 27.1<br><sub>33,26,14,17,52</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,7,4,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 9.0<br><sub>7,11,8,7,11</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,1,1,0,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.7 | 3.8 | 41.4 |
| Duncan Robinson (DET) | 98% | 31.9<br><sub>32,37,27,34,41</sub> | 16.5<br><sub>24,27,12,22,13</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,1,0,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,2,3,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 3.1<br><sub>6,7,3,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.1 | 22.1 |
| Daniss Jenkins (DET) | 98% | 30.8<br><sub>23,21,32,36,42</sub> | 15.1<br><sub>2,5,31,22,21</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,1,5,6,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>7,4,4,8,0</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>0,1,8,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 1.9 | 24.2 |
| Ausar Thompson (DET) | 98% | 30.0<br><sub>26,34,24,28,43</sub> | 11.0<br><sub>14,11,7,8,17</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>6,17,11,5,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>4,3,3,4,11</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.8 | 1.1 | 1.9 | 23.4 |
| John Collins (DET) | 98% | 26.4<br><sub>19,26,32,28,25</sub> | 11.6<br><sub>4,16,8,24,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>3,1,4,10,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>1,0,1,3,0</sub> |  | 1.0<br><sub>0,0,1,2,2</sub> |  | 0.8 | 0.8 | 1.3 | 18.8 |
| Paul Reed (DET) | 98% | 26.2<br><sub>28,30,20,21,38</sub> | 12.8<br><sub>11,8,8,4,13</sub> |  | 8.4<br><sub>5,7,10,10,11</sub> |  | 2.3<br><sub>4,4,0,2,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.2 | 1.1 | 1.7 | 23.5 |
| Kevin Huerter (DET) | 98% | 24.4<br><sub>20,20,35,33,24</sub> | 10.8<br><sub>9,8,24,12,11</sub> |  | 3.2<br><sub>2,1,5,2,1</sub> |  | 2.5<br><sub>3,0,5,3,0</sub> |  | 1.6<br><sub>3,2,4,0,1</sub> |  | 1.1 | 0.5 | 0.9 | 16.5 |
| Javonte Green (DET) | 98% | 16.8<br><sub>20,15,17,11,15</sub> | 6.1<br><sub>5,1,7,7,5</sub> |  | 2.5<br><sub>2,3,2,1,1</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.8<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.3 | 0.4 | 9.3 |
| Ronald Holland II (DET) | 98% | 14.4<br><sub>20,12,14,15,14</sub> | 5.6<br><sub>11,3,5,1,2</sub> |  | 3.1<br><sub>2,2,2,5,5</sub> |  | 1.1<br><sub>0,0,1,2,2</sub> |  | 0.5<br><sub>3,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.9 | 9.8 |
| Taurean Prince (DET) | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.9 |
| Elijah Harkless (DET) | 30% | 6.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 1.0 |
| Isaac Jones (DET) | 52% | 5.7<br><sub>6,-,-,2,-</sub> | 5.8<br><sub>2,-,-,0,-</sub> |  | 1.5<br><sub>5,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 7.7 |
| Tolu Smith (DET) | 52% | 5.7<br><sub>8,5,-,-,-</sub> | 2.4<br><sub>0,1,-,-,-</sub> |  | 2.1<br><sub>2,1,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Davion Mitchell (MIA) | 98% | 36.6<br><sub>43,38,40,38,39</sub> | 14.3<br><sub>11,22,17,19,22</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,3,5,5</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 7.6<br><sub>10,8,11,8,17</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,4,2,3,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 2.4 | 24.8 |
| Bam Adebayo (MIA) | 98% | 35.5<br><sub>41,33,34,37,38</sub> | 19.3<br><sub>35,18,18,11,37</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 9.7<br><sub>10,10,8,8,14</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>4,0,4,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,0,1,0,2</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.5 | 0.8 | 1.8 | 32.5 |
| Giannis Antetokounmpo (MIA) | 98% | 34.5<br><sub>41,31,34,31,31</sub> | 27.7<br><sub>27,20,29,30,37</sub> | 27.5 · –<br><sub>o 50% · u 50%</sub> | 12.3<br><sub>14,14,14,11,9</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 5.6<br><sub>6,4,3,4,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>0,1,0,1,1</sub> |  | 1.1 | 1.1 | 3.5 | 45.6 |
| Pelle Larsson (MIA) | 100% | 30.4<br><sub>35,29,22,31,-</sub> | 11.5<br><sub>7,13,11,14,-</sub> | 10.5 · – | 3.6<br><sub>3,1,3,7,-</sub> | 3.5 | 3.1<br><sub>4,4,3,2,-</sub> | 3.5 | 1.1<br><sub>0,3,3,2,-</sub> |  | 1.0 | 0.2 | 1.8 | 18.2 |
| Andrew Wiggins (MIA) | 98% | 28.1<br><sub>23,21,32,19,32</sub> | 10.9<br><sub>3,2,6,13,8</sub> |  | 3.7<br><sub>4,6,3,0,3</sub> |  | 1.8<br><sub>1,4,1,0,4</sub> |  | 1.6<br><sub>1,0,2,2,1</sub> |  | 0.9 | 0.9 | 1.2 | 16.4 |
| Ryan Conwell (MIA) | 88% | 22.9<br><sub>17,30,19,21,33</sub> | 8.2<br><sub>0,13,6,5,20</sub> |  | 2.4<br><sub>2,1,2,4,5</sub> |  | 1.8<br><sub>2,2,2,2,2</sub> |  | 1.4<br><sub>0,3,2,1,4</sub> |  | 0.7 | 0.1 | 0.9 | 12.4 |
| Bobby Portis (MIA) | 98% | 19.1<br><sub>18,14,20,17,15</sub> | 8.1<br><sub>4,0,4,5,5</sub> |  | 5.0<br><sub>10,5,1,1,3</sub> |  | 1.2<br><sub>5,0,1,1,2</sub> |  | 1.1<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.3 | 0.8 | 14.3 |
| Tim Hardaway Jr. (MIA) | 83% | 15.9<br><sub>7,4,7,-,20</sub> | 6.1<br><sub>0,0,0,-,4</sub> |  | 1.6<br><sub>0,0,0,-,3</sub> |  | 0.7<br><sub>0,1,0,-,2</sub> |  | 0.9<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 8.3 |
| Nikola Jovic (MIA) | 48% | 11.8<br><sub>-,12,-,-,-</sub> | 3.9<br><sub>-,1,-,-,-</sub> |  | 2.2<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 7.0 |
| Myron Gardner (MIA) | 64% | 11.5<br><sub>-,1,-,10,19</sub> | 3.4<br><sub>-,0,-,4,0</sub> |  | 3.0<br><sub>-,0,-,3,4</sub> |  | 1.0<br><sub>-,0,-,1,2</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.5 | 7.4 |
| Dru Smith (MIA) | 58% | 10.8<br><sub>-,1,-,-,6</sub> | 3.2<br><sub>-,0,-,-,0</sub> |  | 1.5<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,0,-,-,1</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.8 | 0.2 | 0.6 | 6.1 |
| Keshad Johnson (MIA) | 38% | 9.5<br><sub>-,-,-,-,-</sub> | 4.2<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.5 | 6.5 |
| Simone Fontecchio (MIA) | 58% | 9.4<br><sub>5,-,-,7,7</sub> | 4.3<br><sub>0,-,-,3,0</sub> |  | 1.6<br><sub>0,-,-,0,0</sub> |  | 0.7<br><sub>0,-,-,0,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.6 |
| Tre Donaldson (MIA) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Vladislav Goldin (MIA) | 8% | 6.7 | 2.1 |  | 1.9 |  | 0.6 |  | 0.0 |  | 0.2 | 0.6 | 0.4 | 4.6 |
| Nick Richards (MIA) | 43% | 6.6<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 2.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.4 | 0.5 | 5.0 |

</details>

<details><summary>if Klay Thompson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | 98% | 35.2<br><sub>27,40,38,27,48</sub> | 27.1<br><sub>33,26,14,17,52</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,7,4,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 9.0<br><sub>7,11,8,7,11</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,1,1,0,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.7 | 3.8 | 41.4 |
| Duncan Robinson (DET) | 98% | 31.9<br><sub>32,37,27,34,41</sub> | 16.4<br><sub>24,27,12,22,13</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,1,0,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,2,3,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 3.1<br><sub>6,7,3,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.1 | 22.1 |
| Daniss Jenkins (DET) | 98% | 30.7<br><sub>23,21,32,36,42</sub> | 15.0<br><sub>2,5,31,22,21</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,1,5,6,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>7,4,4,8,0</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>0,1,8,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 1.9 | 24.1 |
| Ausar Thompson (DET) | 98% | 30.0<br><sub>26,34,24,28,43</sub> | 11.0<br><sub>14,11,7,8,17</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>6,17,11,5,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>4,3,3,4,11</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.8 | 1.0 | 1.9 | 23.4 |
| John Collins (DET) | 98% | 26.4<br><sub>19,26,32,28,25</sub> | 11.6<br><sub>4,16,8,24,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>3,1,4,10,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>1,0,1,3,0</sub> |  | 1.0<br><sub>0,0,1,2,2</sub> |  | 0.8 | 0.8 | 1.3 | 18.8 |
| Paul Reed (DET) | 98% | 26.2<br><sub>28,30,20,21,38</sub> | 12.7<br><sub>11,8,8,4,13</sub> |  | 8.4<br><sub>5,7,10,10,11</sub> |  | 2.3<br><sub>4,4,0,2,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.1 | 1.7 | 23.4 |
| Kevin Huerter (DET) | 98% | 24.5<br><sub>20,20,35,33,24</sub> | 10.8<br><sub>9,8,24,12,11</sub> |  | 3.2<br><sub>2,1,5,2,1</sub> |  | 2.6<br><sub>3,0,5,3,0</sub> |  | 1.6<br><sub>3,2,4,0,1</sub> |  | 1.1 | 0.6 | 0.9 | 16.5 |
| Javonte Green (DET) | 98% | 16.8<br><sub>20,15,17,11,15</sub> | 6.1<br><sub>5,1,7,7,5</sub> |  | 2.5<br><sub>2,3,2,1,1</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.8<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.3 | 0.4 | 9.3 |
| Ronald Holland II (DET) | 98% | 14.4<br><sub>20,12,14,15,14</sub> | 5.6<br><sub>11,3,5,1,2</sub> |  | 3.1<br><sub>2,2,2,5,5</sub> |  | 1.1<br><sub>0,0,1,2,2</sub> |  | 0.5<br><sub>3,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.9 | 9.8 |
| Taurean Prince (DET) | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Elijah Harkless (DET) | 30% | 6.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 1.0 |
| Isaac Jones (DET) | 52% | 5.8<br><sub>6,-,-,2,-</sub> | 5.9<br><sub>2,-,-,0,-</sub> |  | 1.5<br><sub>5,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 7.7 |
| Tolu Smith (DET) | 52% | 5.8<br><sub>8,5,-,-,-</sub> | 2.4<br><sub>0,1,-,-,-</sub> |  | 2.1<br><sub>2,1,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Davion Mitchell (MIA) | 98% | 36.6<br><sub>43,38,40,38,39</sub> | 14.0<br><sub>11,22,17,19,22</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>2,2,3,5,5</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 7.7<br><sub>10,8,11,8,17</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,4,2,3,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 2.3 | 24.6 |
| Bam Adebayo (MIA) | 98% | 35.5<br><sub>41,33,34,37,38</sub> | 18.8<br><sub>35,18,18,11,37</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 9.8<br><sub>10,10,8,8,14</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>4,0,4,4,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,0,1,0,2</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.6 | 0.8 | 1.8 | 32.0 |
| Giannis Antetokounmpo (MIA) | 98% | 34.3<br><sub>41,31,34,31,31</sub> | 27.5<br><sub>27,20,29,30,37</sub> | 27.5 · –<br><sub>o 50% · u 50%</sub> | 12.1<br><sub>14,14,14,11,9</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 5.4<br><sub>6,4,3,4,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>0,1,0,1,1</sub> |  | 1.1 | 1.1 | 3.5 | 45.0 |
| Klay Thompson (MIA) | 100% | 28.7<br><sub>35,23,32,30,-</sub> | 13.5<br><sub>30,11,23,11,-</sub> | 13.5 · – | 2.1<br><sub>5,0,2,1,-</sub> |  | 1.8<br><sub>3,3,4,2,-</sub> |  | 2.9<br><sub>8,2,7,2,-</sub> | 3.5 | 0.7 | 0.6 | 1.1 | 17.4 |
| Andrew Wiggins (MIA) | 98% | 28.2<br><sub>23,21,32,19,32</sub> | 10.7<br><sub>3,2,6,13,8</sub> |  | 3.7<br><sub>4,6,3,0,3</sub> |  | 1.9<br><sub>1,4,1,0,4</sub> |  | 1.5<br><sub>1,0,2,2,1</sub> |  | 0.9 | 0.9 | 1.2 | 16.2 |
| Ryan Conwell (MIA) | 88% | 23.6<br><sub>17,30,19,21,33</sub> | 8.2<br><sub>0,13,6,5,20</sub> |  | 2.4<br><sub>2,1,2,4,5</sub> |  | 1.8<br><sub>2,2,2,2,2</sub> |  | 1.4<br><sub>0,3,2,1,4</sub> |  | 0.8 | 0.1 | 0.9 | 12.4 |
| Bobby Portis (MIA) | 98% | 19.4<br><sub>18,14,20,17,15</sub> | 7.9<br><sub>4,0,4,5,5</sub> |  | 5.1<br><sub>10,5,1,1,3</sub> |  | 1.2<br><sub>5,0,1,1,2</sub> |  | 1.1<br><sub>0,0,1,1,1</sub> |  | 0.6 | 0.3 | 0.8 | 14.2 |
| Tim Hardaway Jr. (MIA) | 83% | 16.3<br><sub>7,4,7,-,20</sub> | 6.1<br><sub>0,0,0,-,4</sub> |  | 1.6<br><sub>0,0,0,-,3</sub> |  | 0.7<br><sub>0,1,0,-,2</sub> |  | 0.9<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.4 |
| Nikola Jovic (MIA) | 48% | 12.3<br><sub>-,12,-,-,-</sub> | 4.0<br><sub>-,1,-,-,-</sub> |  | 2.3<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 7.3 |
| Myron Gardner (MIA) | 64% | 11.6<br><sub>-,1,-,10,19</sub> | 3.4<br><sub>-,0,-,4,0</sub> |  | 3.0<br><sub>-,0,-,3,4</sub> |  | 1.1<br><sub>-,0,-,1,2</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.5 | 7.4 |
| Dru Smith (MIA) | 58% | 11.0<br><sub>-,1,-,-,6</sub> | 3.1<br><sub>-,0,-,-,0</sub> |  | 1.5<br><sub>-,0,-,-,0</sub> |  | 1.5<br><sub>-,0,-,-,1</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.8 | 0.2 | 0.6 | 6.0 |
| Simone Fontecchio (MIA) | 58% | 9.6<br><sub>5,-,-,7,7</sub> | 4.2<br><sub>0,-,-,3,0</sub> |  | 1.7<br><sub>0,-,-,0,0</sub> |  | 0.7<br><sub>0,-,-,0,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.6 |
| Keshad Johnson (MIA) | 38% | 9.3<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.5 | 6.3 |
| Tre Donaldson (MIA) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Vladislav Goldin (MIA) | 8% | 7.0 | 2.1 |  | 1.9 |  | 0.6 |  | 0.0 |  | 0.2 | 0.6 | 0.4 | 4.6 |
| Nick Richards (MIA) | 43% | 6.8<br><sub>-,1,-,-,-</sub> | 2.4<br><sub>-,0,-,-,-</sub> |  | 2.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.4 | 0.5 | 5.0 |

</details>


### BKN @ MEM
Out: Scotty Pippen Jr. (MEM), Grant Nelson (BKN), Ben Saraf (BKN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaylen Wells PRA over 14.5 (15+) | BKN @ MEM | draftkings | 1.98 | 1.96 | 1.69 | 59.2% | 49.9% | 51.1% | +1.3% | +17.2% | 0.3% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.2–118.3 | BKN 28% | 3.55 / 1.39 | MEM -8.5 | 228.5 | MEM -2.5 covers 66%; o228.5 50% |
| Expected (weighted by chance each plays) | 110.2–118.6 | BKN 27% | 3.69 / 1.37 | MEM -8.5 | 228.5 | MEM -2.5 covers 68%; o228.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quinten Post (MEM) | Day-To-Day | 70% | 7.8 | 2.8 | 1.6 | 0.4 | 0.2 | 0.2 | 0.2 | 0.4 | 4.8 | small |
| Zach Edey (MEM) | Day-To-Day | 70% | 19.8 | 8.6 | 7.7 | 1.0 | 0.1 | 0.5 | 1.4 | 1.4 | 17.3 | small |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 98% | 31.8<br><sub>37,38,36,29,28</sub> | 20.2<br><sub>18,26,25,19,22</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>5,10,9,9,6</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>2,0,1,0,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.8<br><sub>4,4,3,4,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 2.0 | 29.3 |
| Julius Randle | 98% | 31.4<br><sub>36,31,34,30,29</sub> | 17.9<br><sub>21,22,19,13,17</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 6.6<br><sub>11,3,7,4,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>2,4,8,4,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,2,1,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.1 | 28.9 |
| Egor Demin | 98% | 21.9<br><sub>-,-,-,-,23</sub> | 9.1<br><sub>-,-,-,-,22</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>-,-,-,-,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.3 | 1.3 | 14.7 |
| Day'Ron Sharpe | 98% | 21.2<br><sub>22,27,32,20,19</sub> | 9.2<br><sub>4,6,12,6,15</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>6,5,10,4,4</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,8,13,6,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.3<br><sub>0,0,0,0,2</sub> |  | 1.0 | 1.1 | 1.8 | 19.8 |
| Danny Wolf | 71% | 20.2<br><sub>-,19,31,36,29</sub> | 8.0<br><sub>-,12,11,10,10</sub> |  | 5.3<br><sub>-,5,9,3,11</sub> |  | 2.0<br><sub>-,3,1,2,4</sub> |  | 0.9<br><sub>-,2,2,1,1</sub> |  | 0.6 | 0.6 | 1.2 | 15.3 |
| Mikel Brown Jr. | 90% | 20.2<br><sub>27,20,25,-,-</sub> | 10.7<br><sub>13,18,18,-,-</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,2,1,-,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>3,4,3,-,-</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>1,3,3,-,-</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 1.7 | 16.1 |
| Nolan Traore | 92% | 19.5<br><sub>24,27,23,21,-</sub> | 9.8<br><sub>17,16,19,14,-</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>3,4,1,1,-</sub> |  | 3.0<br><sub>4,2,2,2,-</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>5,2,2,2,-</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 1.9 | 14.8 |
| Keon Ellis | 86% | 18.4<br><sub>25,10,-,22,26</sub> | 4.7<br><sub>5,1,-,3,11</sub> |  | 2.0<br><sub>1,2,-,1,4</sub> |  | 1.4<br><sub>0,0,-,4,3</sub> |  | 0.6<br><sub>1,0,-,1,2</sub> |  | 1.1 | 0.6 | 0.6 | 8.2 |
| Noah Clowney | 98% | 17.4<br><sub>20,17,21,8,19</sub> | 6.5<br><sub>2,7,3,2,16</sub> |  | 3.4<br><sub>6,1,10,0,3</sub> |  | 0.9<br><sub>2,1,0,0,0</sub> |  | 0.8<br><sub>0,1,1,0,2</sub> |  | 0.6 | 0.5 | 0.8 | 10.7 |
| Moritz Wagner | 96% | 16.4<br><sub>20,20,16,16,19</sub> | 9.3<br><sub>6,6,9,12,16</sub> |  | 3.9<br><sub>1,1,2,3,3</sub> |  | 1.2<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 0.6 | 0.2 | 1.0 | 14.3 |
| Terance Mann | 72% | 14.8<br><sub>-,16,13,22,18</sub> | 3.6<br><sub>-,0,0,0,6</sub> |  | 1.9<br><sub>-,2,2,1,1</sub> |  | 1.6<br><sub>-,2,0,1,3</sub> |  | 0.3<br><sub>-,0,0,0,2</sub> |  | 0.6 | 0.2 | 0.6 | 7.0 |
| Chaney Johnson | 96% | 13.8<br><sub>28,9,8,15,15</sub> | 3.7<br><sub>4,0,5,2,4</sub> |  | 2.1<br><sub>3,2,2,0,3</sub> |  | 0.8<br><sub>2,1,1,1,2</sub> |  | 0.3<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 6.7 |
| Josh Minott | 63% | 8.9<br><sub>-,6,-,12,7</sub> | 4.7<br><sub>-,0,-,10,0</sub> |  | 1.7<br><sub>-,1,-,2,2</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.5<br><sub>-,0,-,2,0</sub> |  | 0.5 | 0.3 | 0.5 | 6.9 |
| Drake Powell | 58% | 8.5<br><sub>-,-,-,9,7</sub> | 2.5<br><sub>-,-,-,2,6</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.6<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.0 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 32.3<br><sub>33,31,33,33,25</sub> | 16.1<br><sub>10,8,22,13,12</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 9.6<br><sub>6,12,7,11,10</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>4,4,8,5,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>2,0,0,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.6 | 2.8 | 30.9 |
| Ty Jerome | 98% | 30.0<br><sub>29,28,32,32,29</sub> | 21.8<br><sub>23,21,27,22,17</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,2,6,2,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 5.5<br><sub>3,5,2,5,9</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>2,2,5,1,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.3 | 2.4 | 30.8 |
| Cedric Coward | 98% | 28.2<br><sub>33,23,28,27,30</sub> | 15.0<br><sub>23,10,3,15,14</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 7.0<br><sub>9,9,6,11,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>4,0,4,4,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>4,2,1,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.4 | 1.6 | 25.0 |
| Jaylen Wells | 98% | 27.7<br><sub>21,25,26,31,27</sub> | 12.8<br><sub>0,7,14,22,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,0,4,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>3,0,1,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>0,1,4,5,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.1 | 1.0 | 17.5 |
| Jerami Grant | 98% | 23.6<br><sub>24,22,22,20,26</sub> | 11.9<br><sub>11,10,17,14,22</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>1,0,3,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>2,2,2,2,1</sub> |  | 1.4<br><sub>2,2,3,2,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.6 | 1.2 | 15.9 |
| Cam Spencer | 98% | 21.0<br><sub>24,19,17,20,24</sub> | 8.9<br><sub>7,7,7,15,14</sub> |  | 2.5<br><sub>6,1,2,3,2</sub> |  | 5.0<br><sub>9,0,4,3,5</sub> |  | 1.3<br><sub>1,1,1,3,3</sub> |  | 0.8 | 0.2 | 1.2 | 16.4 |
| Javon Small | 96% | 18.8<br><sub>-,21,24,15,15</sub> | 7.8<br><sub>-,10,9,3,10</sub> |  | 2.6<br><sub>-,4,2,1,2</sub> |  | 3.2<br><sub>-,2,5,4,5</sub> |  | 1.0<br><sub>-,1,1,1,2</sub> |  | 0.8 | 0.2 | 1.2 | 13.6 |
| Isaiah Stewart | 98% | 18.4<br><sub>10,-,-,18,20</sub> | 8.5<br><sub>6,-,-,3,12</sub> |  | 4.1<br><sub>1,-,-,1,5</sub> |  | 0.8<br><sub>0,-,-,2,0</sub> |  | 0.5<br><sub>0,-,-,1,0</sub> |  | 0.3 | 1.2 | 1.0 | 13.4 |
| GG Jackson | 88% | 16.7<br><sub>7,-,17,13,22</sub> | 9.4<br><sub>1,-,2,2,14</sub> |  | 3.4<br><sub>2,-,1,1,6</sub> |  | 1.1<br><sub>0,-,0,0,4</sub> |  | 0.9<br><sub>0,-,0,0,3</sub> |  | 0.4 | 0.5 | 1.2 | 13.9 |
| Taylor Hendricks | 72% | 13.7<br><sub>-,4,16,11,19</sub> | 5.7<br><sub>-,4,9,7,10</sub> |  | 3.1<br><sub>-,2,3,2,12</sub> |  | 0.7<br><sub>-,0,0,1,2</sub> |  | 0.7<br><sub>-,1,1,1,2</sub> |  | 0.7 | 0.4 | 0.6 | 9.6 |
| Kris Murray | 71% | 8.6<br><sub>15,13,1,-,1</sub> | 2.3<br><sub>5,2,0,-,0</sub> |  | 1.4<br><sub>1,2,0,-,1</sub> |  | 0.6<br><sub>1,1,0,-,0</sub> |  | 0.1<br><sub>1,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Olivier-Maxence Prosper | 64% | 8.3<br><sub>7,11,1,-,2</sub> | 4.7<br><sub>4,2,0,-,6</sub> |  | 1.7<br><sub>3,3,0,-,1</sub> |  | 0.5<br><sub>1,1,0,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.8 |
| Jahmai Mashack | 48% | 8.2<br><sub>-,4,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,2,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 4.7 |
| Karim Lopez | 48% | 5.9<br><sub>-,4,-,-,-</sub> | 2.2<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 3.7 |

</details>


### CHI @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Tobe Awaka (CHI), Dailyn Swain (CHI), Caleb Wilson (CHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.7–126.5 | CHI 10% | 9.83 / 1.11 | MIN -17.5 | 235.5 | MIN -15.5 covers 57%; o234.5 52% |
| Expected (weighted by chance each plays) | 109.9–124.9 | CHI 15% | 6.89 / 1.17 | MIN -15.5 | 234.5 | MIN -15.5 covers 49%; o234.5 50% |
| if Nic Claxton plays | 109.4–125.3 | CHI 13% | 7.79 / 1.15 | MIN -15.5 | 234.5 | MIN -15.5 covers 51%; o234.5 51% |
| if Norman Powell plays | 109.8–125.3 | CHI 14% | 7.39 / 1.16 | MIN -15.5 | 235.5 | MIN -15.5 covers 50%; o234.5 52% |
| if Jalen Smith plays | 109.4–125.1 | CHI 13% | 7.62 / 1.15 | MIN -15.5 | 234.5 | MIN -15.5 covers 51%; o234.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nic Claxton (CHI) | Questionable | 55% | 24.0 | 9.4 | 6.4 | 2.8 | 0.0 | 0.6 | 1.1 | 1.3 | 18.6 | full tables below |
| Norman Powell (CHI) | Questionable | 55% | 31.9 | 21.5 | 3.6 | 2.2 | 2.3 | 1.2 | 0.2 | 2.4 | 27.3 | full tables below |
| Jalen Smith (CHI) | Questionable | 55% | 31.0 | 15.4 | 9.2 | 1.9 | 1.9 | 0.7 | 1.1 | 1.6 | 26.6 | full tables below |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 33.3<br><sub>32,27,34,25,39</sub> | 18.5<br><sub>13,10,19,9,15</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>4,1,7,2,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 9.1<br><sub>10,6,15,7,14</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>2,1,1,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.6 | 4.0 | 35.2 |
| Isaac Okoro | 98% | 33.1<br><sub>21,15,25,23,41</sub> | 11.4<br><sub>4,6,12,0,15</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>1,1,2,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>0,0,1,4,2</sub> |  | 1.0<br><sub>0,0,0,0,2</sub> |  | 1.1 | 0.6 | 1.4 | 17.1 |
| Matas Buzelis | 98% | 31.9<br><sub>23,26,31,31,29</sub> | 18.6<br><sub>4,12,19,13,11</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>3,5,5,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,3,2,2,2</sub> |  | 2.0<br><sub>0,1,3,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.4 | 3.0 | 26.9 |
| Patrick Williams | 67% | 29.2<br><sub>-,20,25,28,24</sub> | 11.4<br><sub>-,4,7,9,13</sub> |  | 4.1<br><sub>-,0,3,7,4</sub> |  | 2.4<br><sub>-,2,3,4,2</sub> |  | 1.5<br><sub>-,0,1,0,4</sub> |  | 0.9 | 0.5 | 1.7 | 17.9 |
| Buddy Hield | 66% | 26.5<br><sub>12,8,-,-,25</sub> | 12.7<br><sub>6,7,-,-,12</sub> |  | 3.8<br><sub>1,1,-,-,3</sub> |  | 2.6<br><sub>3,1,-,-,3</sub> |  | 1.8<br><sub>1,1,-,-,2</sub> |  | 1.1 | 0.4 | 1.7 | 19.0 |
| Tre Jones | 98% | 26.3<br><sub>19,18,14,28,15</sub> | 15.5<br><sub>8,14,6,13,4</sub> |  | 3.6<br><sub>3,3,1,1,1</sub> |  | 4.9<br><sub>3,4,1,3,3</sub> |  | 0.7<br><sub>0,1,0,1,0</sub> |  | 1.1 | 0.2 | 1.9 | 24.0 |
| Jordan Hawkins | 66% | 23.9<br><sub>2,7,17,24,-</sub> | 10.9<br><sub>2,2,9,7,-</sub> |  | 3.3<br><sub>0,1,0,4,-</sub> |  | 1.4<br><sub>0,0,1,2,-</sub> |  | 1.4<br><sub>0,0,1,1,-</sub> |  | 0.7 | 0.4 | 1.3 | 15.6 |
| Noa Essengue | 96% | 21.6<br><sub>14,14,15,11,8</sub> | 8.9<br><sub>8,6,10,8,5</sub> |  | 4.5<br><sub>6,3,7,4,1</sub> |  | 1.1<br><sub>0,0,1,3,1</sub> |  | 0.9<br><sub>1,0,0,1,1</sub> |  | 0.8 | 0.4 | 1.1 | 14.6 |
| Leonard Miller | 64% | 20.3<br><sub>9,19,-,2,-</sub> | 9.5<br><sub>2,4,-,0,-</sub> |  | 4.8<br><sub>3,6,-,0,-</sub> |  | 1.2<br><sub>0,3,-,0,-</sub> |  | 0.8<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.5 | 1.1 | 15.5 |
| Orlando Robinson | 38% | 17.5<br><sub>-,-,-,-,-</sub> | 7.0<br><sub>-,-,-,-,-</sub> |  | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 1.2 | 13.8 |
| Zach Collins | 66% | 17.0<br><sub>10,14,-,3,-</sub> | 7.1<br><sub>2,3,-,2,-</sub> |  | 5.0<br><sub>3,1,-,2,-</sub> |  | 1.6<br><sub>0,3,-,1,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.4 | 1.0 | 13.8 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 31.8<br><sub>29,37,40,33,25</sub> | 17.8<br><sub>13,14,23,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>6,8,6,6,9</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>3,4,5,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 1.0 | 1.7 | 26.5 |
| Ayo Dosunmu | 98% | 30.3<br><sub>37,34,39,30,27</sub> | 17.9<br><sub>19,21,26,26,18</sub> | 18.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>12,1,2,4,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>8,6,4,1,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.4 | 1.8 | 26.3 |
| Jonathan Kuminga | 98% | 28.2<br><sub>33,32,34,25,24</sub> | 14.5<br><sub>8,16,17,4,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>10,8,8,0,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,5,4,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.6 | 1.6 | 22.7 |
| Rudy Gobert | 98% | 28.1<br><sub>31,33,25,31,23</sub> | 9.6<br><sub>10,8,8,10,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.9<br><sub>10,11,11,15,6</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,2,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.4 | 22.1 |
| LaMelo Ball | 98% | 28.0<br><sub>33,31,35,30,25</sub> | 22.0<br><sub>34,20,22,24,22</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>6,2,2,3,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>3,6,8,5,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>6,4,3,4,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.2 | 3.2 | 32.7 |
| Terrence Shannon Jr. | 98% | 21.3<br><sub>-,-,-,18,21</sub> | 11.8<br><sub>-,-,-,5,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>-,-,-,3,4</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.1 | 1.2 | 16.8 |
| Trey Lyles | 98% | 18.8<br><sub>21,20,29,21,15</sub> | 6.7<br><sub>12,5,5,9,2</sub> |  | 4.2<br><sub>4,2,13,6,0</sub> |  | 1.1<br><sub>0,0,2,2,0</sub> |  | 0.8<br><sub>2,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 12.0 |
| Jaylen Clark | 91% | 18.2<br><sub>21,25,21,19,19</sub> | 6.3<br><sub>4,10,8,3,7</sub> |  | 2.5<br><sub>2,4,3,2,6</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.3 | 0.5 | 10.1 |
| Bones Hyland | 98% | 16.1<br><sub>14,16,10,13,23</sub> | 10.7<br><sub>10,19,4,14,24</sub> |  | 1.9<br><sub>1,2,1,2,3</sub> |  | 3.2<br><sub>3,4,0,2,8</sub> |  | 1.5<br><sub>2,4,1,1,5</sub> |  | 0.8 | 0.3 | 1.1 | 15.8 |
| Joan Beringer | 97% | 15.7<br><sub>14,13,7,16,22</sub> | 7.5<br><sub>2,4,2,4,13</sub> |  | 5.7<br><sub>7,7,3,3,9</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 13.8 |
| Cody Williams | 58% | 6.7<br><sub>7,-,-,2,7</sub> | 0.3<br><sub>0,-,-,0,0</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 1.8 |
| Rocco Zikarsky | 48% | 6.6<br><sub>-,-,-,2,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 2.1<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.1 |
| Zyon Pullin | 38% | 6.4<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Isaiah Evans | 52% | 6.2<br><sub>-,-,-,2,8</sub> | 6.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 8.1 |
| Johni Broome | 5% | 4.7 | 1.8 |  | 1.3 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.5 |

</details>

<details><summary>if Norman Powell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 32.9<br><sub>32,27,34,25,39</sub> | 15.9<br><sub>13,10,19,9,15</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>4,1,7,2,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 8.4<br><sub>10,6,15,7,14</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>2,1,1,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.6 | 3.5 | 31.6 |
| Norman Powell (CHI) | 100% | 31.9<br><sub>29,22,-,-,31</sub> | 21.5<br><sub>18,12,-,-,33</sub> | 21.5 · – | 3.6<br><sub>3,1,-,-,5</sub> | 3.5 | 2.2<br><sub>0,1,-,-,2</sub> |  | 2.3<br><sub>1,0,-,-,4</sub> | 2.5 | 1.2 | 0.2 | 2.4 | 27.3 |
| Isaac Okoro (CHI) | 98% | 31.5<br><sub>21,15,25,23,41</sub> | 10.1<br><sub>4,6,12,0,15</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>1,1,2,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,0,1,4,2</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 1.0 | 0.5 | 1.2 | 15.2 |
| Matas Buzelis (CHI) | 98% | 31.1<br><sub>23,26,31,31,29</sub> | 15.7<br><sub>4,12,19,13,11</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>3,5,5,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,3,2,2,2</sub> |  | 1.9<br><sub>0,1,3,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.3 | 2.5 | 23.7 |
| Patrick Williams (CHI) | 67% | 27.6<br><sub>-,20,25,28,24</sub> | 9.2<br><sub>-,4,7,9,13</sub> |  | 3.8<br><sub>-,0,3,7,4</sub> |  | 2.1<br><sub>-,2,3,4,2</sub> |  | 1.2<br><sub>-,0,1,0,4</sub> |  | 0.9 | 0.5 | 1.3 | 15.1 |
| Tre Jones (CHI) | 98% | 22.3<br><sub>19,18,14,28,15</sub> | 12.4<br><sub>8,14,6,13,4</sub> |  | 3.0<br><sub>3,3,1,1,1</sub> |  | 3.7<br><sub>3,4,1,3,3</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.1 | 1.5 | 19.2 |
| Buddy Hield (CHI) | 66% | 20.4<br><sub>12,8,-,-,25</sub> | 8.9<br><sub>6,7,-,-,12</sub> |  | 2.9<br><sub>1,1,-,-,3</sub> |  | 1.8<br><sub>3,1,-,-,3</sub> |  | 1.2<br><sub>1,1,-,-,2</sub> |  | 0.9 | 0.3 | 1.2 | 13.7 |
| Jordan Hawkins (CHI) | 66% | 18.0<br><sub>2,7,17,24,-</sub> | 7.5<br><sub>2,2,9,7,-</sub> |  | 2.5<br><sub>0,1,0,4,-</sub> |  | 1.0<br><sub>0,0,1,2,-</sub> |  | 0.9<br><sub>0,0,1,1,-</sub> |  | 0.5 | 0.3 | 1.0 | 10.9 |
| Leonard Miller (CHI) | 64% | 17.0<br><sub>9,19,-,2,-</sub> | 7.5<br><sub>2,4,-,0,-</sub> |  | 4.1<br><sub>3,6,-,0,-</sub> |  | 0.8<br><sub>0,3,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.5 | 0.9 | 12.4 |
| Noa Essengue (CHI) | 96% | 16.6<br><sub>14,14,15,11,8</sub> | 6.7<br><sub>8,6,10,8,5</sub> |  | 3.6<br><sub>6,3,7,4,1</sub> |  | 0.8<br><sub>0,0,1,3,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.3 | 0.8 | 11.1 |
| Orlando Robinson (CHI) | 38% | 14.4<br><sub>-,-,-,-,-</sub> | 5.5<br><sub>-,-,-,-,-</sub> |  | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.9 | 10.9 |
| Zach Collins (CHI) | 66% | 14.3<br><sub>10,14,-,3,-</sub> | 5.6<br><sub>2,3,-,2,-</sub> |  | 4.2<br><sub>3,1,-,2,-</sub> |  | 1.2<br><sub>0,3,-,1,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.4 | 0.8 | 11.1 |
| Jaden McDaniels (MIN) | 98% | 31.8<br><sub>29,37,40,33,25</sub> | 17.7<br><sub>13,14,23,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>6,8,6,6,9</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>3,4,5,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 1.0 | 1.8 | 26.5 |
| Ayo Dosunmu (MIN) | 98% | 30.3<br><sub>37,34,39,30,27</sub> | 17.8<br><sub>19,21,26,26,18</sub> | 18.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>12,1,2,4,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>8,6,4,1,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.4 | 1.8 | 26.2 |
| Jonathan Kuminga (MIN) | 98% | 28.2<br><sub>33,32,34,25,24</sub> | 14.4<br><sub>8,16,17,4,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>10,8,8,0,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,5,4,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.6 | 1.6 | 22.7 |
| Rudy Gobert (MIN) | 98% | 28.1<br><sub>31,33,25,31,23</sub> | 9.6<br><sub>10,8,8,10,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 11.0<br><sub>10,11,11,15,6</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,2,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.4 | 22.1 |
| LaMelo Ball (MIN) | 98% | 28.0<br><sub>33,31,35,30,25</sub> | 21.8<br><sub>34,20,22,24,22</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>6,2,2,3,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>3,6,8,5,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>6,4,3,4,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.2 | 3.2 | 32.5 |
| Terrence Shannon Jr. (MIN) | 98% | 21.3<br><sub>-,-,-,18,21</sub> | 11.8<br><sub>-,-,-,5,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>-,-,-,3,4</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.1 | 1.2 | 16.8 |
| Trey Lyles (MIN) | 98% | 18.8<br><sub>21,20,29,21,15</sub> | 6.6<br><sub>12,5,5,9,2</sub> |  | 4.2<br><sub>4,2,13,6,0</sub> |  | 1.1<br><sub>0,0,2,2,0</sub> |  | 0.8<br><sub>2,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 12.0 |
| Jaylen Clark (MIN) | 91% | 18.2<br><sub>21,25,21,19,19</sub> | 6.3<br><sub>4,10,8,3,7</sub> |  | 2.5<br><sub>2,4,3,2,6</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.2 | 0.5 | 10.0 |
| Bones Hyland (MIN) | 98% | 16.1<br><sub>14,16,10,13,23</sub> | 10.7<br><sub>10,19,4,14,24</sub> |  | 1.9<br><sub>1,2,1,2,3</sub> |  | 3.2<br><sub>3,4,0,2,8</sub> |  | 1.6<br><sub>2,4,1,1,5</sub> |  | 0.8 | 0.3 | 1.2 | 15.7 |
| Joan Beringer (MIN) | 97% | 15.7<br><sub>14,13,7,16,22</sub> | 7.5<br><sub>2,4,2,4,13</sub> |  | 5.7<br><sub>7,7,3,3,9</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 13.8 |
| Cody Williams (MIN) | 58% | 6.7<br><sub>7,-,-,2,7</sub> | 0.3<br><sub>0,-,-,0,0</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 1.8 |
| Rocco Zikarsky (MIN) | 48% | 6.6<br><sub>-,-,-,2,-</sub> | 2.5<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 5.0 |
| Zyon Pullin (MIN) | 38% | 6.3<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.3 |
| Isaiah Evans (MIN) | 52% | 6.2<br><sub>-,-,-,2,8</sub> | 6.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 8.1 |
| Johni Broome (MIN) | 5% | 4.8 | 1.8 |  | 1.2 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.2 | 3.3 |

</details>

<details><summary>if Nic Claxton plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 33.5<br><sub>32,27,34,25,39</sub> | 17.9<br><sub>13,10,19,9,15</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>4,1,7,2,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 8.9<br><sub>10,6,15,7,14</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>2,1,1,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.5 | 3.9 | 34.0 |
| Isaac Okoro (CHI) | 98% | 32.6<br><sub>21,15,25,23,41</sub> | 10.8<br><sub>4,6,12,0,15</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>1,1,2,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,0,1,4,2</sub> |  | 1.0<br><sub>0,0,0,0,2</sub> |  | 1.1 | 0.5 | 1.3 | 16.1 |
| Matas Buzelis (CHI) | 98% | 31.5<br><sub>23,26,31,31,29</sub> | 18.2<br><sub>4,12,19,13,11</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>3,5,5,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,3,2,2,2</sub> |  | 2.0<br><sub>0,1,3,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.4 | 2.8 | 26.1 |
| Patrick Williams (CHI) | 67% | 28.4<br><sub>-,20,25,28,24</sub> | 9.8<br><sub>-,4,7,9,13</sub> |  | 3.9<br><sub>-,0,3,7,4</sub> |  | 2.2<br><sub>-,2,3,4,2</sub> |  | 1.3<br><sub>-,0,1,0,4</sub> |  | 0.9 | 0.5 | 1.6 | 15.9 |
| Tre Jones (CHI) | 98% | 26.1<br><sub>19,18,14,28,15</sub> | 14.9<br><sub>8,14,6,13,4</sub> |  | 3.6<br><sub>3,3,1,1,1</sub> |  | 4.5<br><sub>3,4,1,3,3</sub> |  | 0.6<br><sub>0,1,0,1,0</sub> |  | 1.1 | 0.2 | 1.9 | 23.0 |
| Nic Claxton (CHI) | 100% | 24.0<br><sub>-,-,18,16,22</sub> | 9.4<br><sub>-,-,4,17,2</sub> |  | 6.4<br><sub>-,-,4,6,6</sub> |  | 2.8<br><sub>-,-,4,1,2</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.6 | 1.1 | 1.3 | 18.6 |
| Buddy Hield (CHI) | 66% | 24.0<br><sub>12,8,-,-,25</sub> | 10.5<br><sub>6,7,-,-,12</sub> |  | 3.4<br><sub>1,1,-,-,3</sub> |  | 2.2<br><sub>3,1,-,-,3</sub> |  | 1.5<br><sub>1,1,-,-,2</sub> |  | 1.0 | 0.3 | 1.4 | 16.1 |
| Jordan Hawkins (CHI) | 66% | 21.6<br><sub>2,7,17,24,-</sub> | 9.1<br><sub>2,2,9,7,-</sub> |  | 2.9<br><sub>0,1,0,4,-</sub> |  | 1.2<br><sub>0,0,1,2,-</sub> |  | 1.2<br><sub>0,0,1,1,-</sub> |  | 0.6 | 0.4 | 1.1 | 13.2 |
| Leonard Miller (CHI) | 64% | 18.9<br><sub>9,19,-,2,-</sub> | 8.8<br><sub>2,4,-,0,-</sub> |  | 4.5<br><sub>3,6,-,0,-</sub> |  | 1.0<br><sub>0,3,-,0,-</sub> |  | 0.8<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.5 | 1.0 | 14.3 |
| Noa Essengue (CHI) | 96% | 18.4<br><sub>14,14,15,11,8</sub> | 7.5<br><sub>8,6,10,8,5</sub> |  | 4.0<br><sub>6,3,7,4,1</sub> |  | 0.8<br><sub>0,0,1,3,1</sub> |  | 0.7<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.3 | 0.9 | 12.3 |
| Zach Collins (CHI) | 66% | 15.1<br><sub>10,14,-,3,-</sub> | 6.2<br><sub>2,3,-,2,-</sub> |  | 4.4<br><sub>3,1,-,2,-</sub> |  | 1.4<br><sub>0,3,-,1,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.4 | 0.9 | 12.0 |
| Orlando Robinson (CHI) | 38% | 14.7<br><sub>-,-,-,-,-</sub> | 5.9<br><sub>-,-,-,-,-</sub> |  | 4.2<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 1.0 | 11.6 |
| Jaden McDaniels (MIN) | 98% | 31.8<br><sub>29,37,40,33,25</sub> | 17.6<br><sub>13,14,23,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>6,8,6,6,9</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>3,4,5,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 1.0 | 1.8 | 26.4 |
| Ayo Dosunmu (MIN) | 98% | 30.4<br><sub>37,34,39,30,27</sub> | 17.7<br><sub>19,21,26,26,18</sub> | 18.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>12,1,2,4,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>8,6,4,1,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.4 | 1.8 | 26.1 |
| Jonathan Kuminga (MIN) | 98% | 28.2<br><sub>33,32,34,25,24</sub> | 14.4<br><sub>8,16,17,4,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>10,8,8,0,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,5,4,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.6 | 1.6 | 22.6 |
| Rudy Gobert (MIN) | 98% | 28.1<br><sub>31,33,25,31,23</sub> | 9.5<br><sub>10,8,8,10,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.9<br><sub>10,11,11,15,6</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,2,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.4 | 22.1 |
| LaMelo Ball (MIN) | 98% | 28.0<br><sub>33,31,35,30,25</sub> | 21.8<br><sub>34,20,22,24,22</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>6,2,2,3,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>3,6,8,5,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>6,4,3,4,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.2 | 3.2 | 32.5 |
| Terrence Shannon Jr. (MIN) | 98% | 21.2<br><sub>-,-,-,18,21</sub> | 11.8<br><sub>-,-,-,5,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>-,-,-,3,4</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.1 | 1.2 | 16.8 |
| Trey Lyles (MIN) | 98% | 18.9<br><sub>21,20,29,21,15</sub> | 6.7<br><sub>12,5,5,9,2</sub> |  | 4.3<br><sub>4,2,13,6,0</sub> |  | 1.1<br><sub>0,0,2,2,0</sub> |  | 0.8<br><sub>2,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 12.0 |
| Jaylen Clark (MIN) | 91% | 18.2<br><sub>21,25,21,19,19</sub> | 6.3<br><sub>4,10,8,3,7</sub> |  | 2.5<br><sub>2,4,3,2,6</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.3 | 0.5 | 10.0 |
| Bones Hyland (MIN) | 98% | 16.1<br><sub>14,16,10,13,23</sub> | 10.7<br><sub>10,19,4,14,24</sub> |  | 1.9<br><sub>1,2,1,2,3</sub> |  | 3.2<br><sub>3,4,0,2,8</sub> |  | 1.5<br><sub>2,4,1,1,5</sub> |  | 0.8 | 0.3 | 1.2 | 15.8 |
| Joan Beringer (MIN) | 97% | 15.7<br><sub>14,13,7,16,22</sub> | 7.4<br><sub>2,4,2,4,13</sub> |  | 5.7<br><sub>7,7,3,3,9</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 13.7 |
| Cody Williams (MIN) | 58% | 6.6<br><sub>7,-,-,2,7</sub> | 0.3<br><sub>0,-,-,0,0</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 1.8 |
| Rocco Zikarsky (MIN) | 48% | 6.6<br><sub>-,-,-,2,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 5.1 |
| Zyon Pullin (MIN) | 38% | 6.3<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |
| Isaiah Evans (MIN) | 52% | 6.2<br><sub>-,-,-,2,8</sub> | 6.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 8.2 |
| Johni Broome (MIN) | 5% | 4.8 | 1.9 |  | 1.2 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.6 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 33.3<br><sub>32,27,34,25,39</sub> | 17.3<br><sub>13,10,19,9,15</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>4,1,7,2,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 8.8<br><sub>10,6,15,7,14</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>2,1,1,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.5 | 3.9 | 33.5 |
| Isaac Okoro (CHI) | 98% | 31.6<br><sub>21,15,25,23,41</sub> | 10.1<br><sub>4,6,12,0,15</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>1,1,2,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,0,1,4,2</sub> |  | 1.0<br><sub>0,0,0,0,2</sub> |  | 1.0 | 0.5 | 1.3 | 15.2 |
| Matas Buzelis (CHI) | 98% | 31.2<br><sub>23,26,31,31,29</sub> | 16.8<br><sub>4,12,19,13,11</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>3,5,5,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,3,2,2,2</sub> |  | 1.9<br><sub>0,1,3,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.3 | 2.7 | 24.6 |
| Jalen Smith (CHI) | 100% | 31.0<br><sub>28,7,30,30,32</sub> | 15.4<br><sub>13,3,17,23,15</sub> |  | 9.2<br><sub>7,2,8,4,12</sub> |  | 1.9<br><sub>4,0,2,3,3</sub> |  | 1.9<br><sub>1,1,2,5,1</sub> |  | 0.7 | 1.1 | 1.6 | 26.6 |
| Patrick Williams (CHI) | 67% | 27.8<br><sub>-,20,25,28,24</sub> | 9.5<br><sub>-,4,7,9,13</sub> |  | 3.8<br><sub>-,0,3,7,4</sub> |  | 2.2<br><sub>-,2,3,4,2</sub> |  | 1.3<br><sub>-,0,1,0,4</sub> |  | 0.9 | 0.5 | 1.5 | 15.5 |
| Tre Jones (CHI) | 98% | 24.4<br><sub>19,18,14,28,15</sub> | 13.6<br><sub>8,14,6,13,4</sub> |  | 3.3<br><sub>3,3,1,1,1</sub> |  | 4.2<br><sub>3,4,1,3,3</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 1.0 | 0.1 | 1.7 | 21.1 |
| Buddy Hield (CHI) | 66% | 22.6<br><sub>12,8,-,-,25</sub> | 10.0<br><sub>6,7,-,-,12</sub> |  | 3.1<br><sub>1,1,-,-,3</sub> |  | 2.1<br><sub>3,1,-,-,3</sub> |  | 1.4<br><sub>1,1,-,-,2</sub> |  | 0.9 | 0.3 | 1.3 | 15.2 |
| Jordan Hawkins (CHI) | 66% | 19.8<br><sub>2,7,17,24,-</sub> | 8.4<br><sub>2,2,9,7,-</sub> |  | 2.7<br><sub>0,1,0,4,-</sub> |  | 1.1<br><sub>0,0,1,2,-</sub> |  | 1.1<br><sub>0,0,1,1,-</sub> |  | 0.6 | 0.3 | 1.1 | 12.2 |
| Leonard Miller (CHI) | 64% | 17.0<br><sub>9,19,-,2,-</sub> | 7.7<br><sub>2,4,-,0,-</sub> |  | 4.1<br><sub>3,6,-,0,-</sub> |  | 0.9<br><sub>0,3,-,0,-</sub> |  | 0.7<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.4 | 0.9 | 12.7 |
| Noa Essengue (CHI) | 96% | 16.6<br><sub>14,14,15,11,8</sub> | 6.8<br><sub>8,6,10,8,5</sub> |  | 3.6<br><sub>6,3,7,4,1</sub> |  | 0.8<br><sub>0,0,1,3,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.3 | 0.9 | 11.2 |
| Orlando Robinson (CHI) | 38% | 14.9<br><sub>-,-,-,-,-</sub> | 5.9<br><sub>-,-,-,-,-</sub> |  | 4.2<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 1.0 | 11.5 |
| Zach Collins (CHI) | 66% | 13.4<br><sub>10,14,-,3,-</sub> | 5.6<br><sub>2,3,-,2,-</sub> |  | 3.9<br><sub>3,1,-,2,-</sub> |  | 1.2<br><sub>0,3,-,1,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.8 | 10.8 |
| Jaden McDaniels (MIN) | 98% | 31.8<br><sub>29,37,40,33,25</sub> | 17.7<br><sub>13,14,23,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>6,8,6,6,9</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>3,4,5,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 1.0 | 1.7 | 26.5 |
| Ayo Dosunmu (MIN) | 98% | 30.4<br><sub>37,34,39,30,27</sub> | 17.7<br><sub>19,21,26,26,18</sub> | 18.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>12,1,2,4,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>8,6,4,1,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.4 | 1.8 | 26.2 |
| Jonathan Kuminga (MIN) | 98% | 28.2<br><sub>33,32,34,25,24</sub> | 14.3<br><sub>8,16,17,4,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>10,8,8,0,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,5,4,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.6 | 1.6 | 22.6 |
| Rudy Gobert (MIN) | 98% | 28.1<br><sub>31,33,25,31,23</sub> | 9.5<br><sub>10,8,8,10,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.9<br><sub>10,11,11,15,6</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,2,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.4 | 21.9 |
| LaMelo Ball (MIN) | 98% | 28.0<br><sub>33,31,35,30,25</sub> | 21.8<br><sub>34,20,22,24,22</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>6,2,2,3,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>3,6,8,5,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>6,4,3,4,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.2 | 3.2 | 32.4 |
| Terrence Shannon Jr. (MIN) | 98% | 21.2<br><sub>-,-,-,18,21</sub> | 11.8<br><sub>-,-,-,5,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>-,-,-,3,4</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.1 | 1.2 | 16.8 |
| Trey Lyles (MIN) | 98% | 18.9<br><sub>21,20,29,21,15</sub> | 6.7<br><sub>12,5,5,9,2</sub> |  | 4.3<br><sub>4,2,13,6,0</sub> |  | 1.1<br><sub>0,0,2,2,0</sub> |  | 0.8<br><sub>2,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 12.0 |
| Jaylen Clark (MIN) | 91% | 18.2<br><sub>21,25,21,19,19</sub> | 6.3<br><sub>4,10,8,3,7</sub> |  | 2.5<br><sub>2,4,3,2,6</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.3 | 0.5 | 10.0 |
| Bones Hyland (MIN) | 98% | 16.1<br><sub>14,16,10,13,23</sub> | 10.7<br><sub>10,19,4,14,24</sub> |  | 1.9<br><sub>1,2,1,2,3</sub> |  | 3.2<br><sub>3,4,0,2,8</sub> |  | 1.5<br><sub>2,4,1,1,5</sub> |  | 0.8 | 0.3 | 1.2 | 15.8 |
| Joan Beringer (MIN) | 97% | 15.7<br><sub>14,13,7,16,22</sub> | 7.4<br><sub>2,4,2,4,13</sub> |  | 5.7<br><sub>7,7,3,3,9</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 13.7 |
| Cody Williams (MIN) | 58% | 6.6<br><sub>7,-,-,2,7</sub> | 0.3<br><sub>0,-,-,0,0</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 1.8 |
| Rocco Zikarsky (MIN) | 48% | 6.6<br><sub>-,-,-,2,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.1 |
| Zyon Pullin (MIN) | 38% | 6.3<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |
| Isaiah Evans (MIN) | 52% | 6.2<br><sub>-,-,-,2,8</sub> | 6.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 8.2 |
| Johni Broome (MIN) | 5% | 4.8 | 1.8 |  | 1.2 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.2 | 3.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-14/`._
