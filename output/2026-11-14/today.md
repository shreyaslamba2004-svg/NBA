# NBA model · Sat 14 Nov 2026 (US date)

Updated **Sun 15 Nov, 11:10 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-14/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

3 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| DAL @ CLE | player minutes | Tyrese Proctor projected 32 min; most in his last 10 games is 27 | minutes 32 vs 18 this season; teammates out: Allen, Harden, Merrill, Tomlin (~125 min a game) |
| DAL @ CLE | player minutes | Meleek Thomas projected 31 min; most in his last 10 games is 27 | minutes 31 vs 22 this season; teammates out: Allen, Harden, Merrill, Tomlin (~125 min a game) |
| DAL @ CLE | player points | Mario Hezonja projected 9.2 pts vs DraftKings line 14.5 | minutes 23 vs 18 this season; scoring 0.41/min vs 0.41 this season; teammates out: Allen, Harden, Merrill, Tomlin (~125 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| CHI to win | CHI @ MIN | sportsbet | 9.50 | 7.94 | 7.39 | 13.5% | 12.6% | 12.6% | +19.6% | +28.6% | 0.6% |
| Karlo Matkovic REB over 7.5 (8+) | DEN @ NOP | draftkings | 9.40 | 8.57 | 4.34 | 23.0% | 9.9% | 11.7% | +9.7% | +116.5% | 0.3% |
| Karlo Matkovic REB over 9.5 (10+) | DEN @ NOP | draftkings | 22.00 | 20.37 | 10.83 | 9.2% | 4.2% | 4.9% | +7.9% | +103.1% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yves Missi PTS under 5.5 | DEN @ NOP | draftkings | 2.20 | 2.04 | 2.03 | 49.3% | 49.1% | 49.1% | +8.1% | +8.5% | 1.7% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DEN @ NOP | Sun 15 Nov 11:00 | 124.6–113.7 | DEN 78% | 1.28 / 4.54 | NOP +11.5 | 238.5 | NOP +12.5 covers 54%; o235.5 56% |
| DAL @ CLE | Sun 15 Nov 11:30 | 116.8–113.7 | DAL 58% | 1.71 / 2.40 | CLE +3.5 | 230.5 | CLE +8.5 covers 65%; o228.5 54% |
| DET @ MIA | Sun 15 Nov 12:00 | 118.1–111.9 | DET 67% | 1.49 / 3.04 | MIA +6.5 | 229.5 | MIA +4.5 covers 44%; o228.5 53% |
| BKN @ MEM | Sun 15 Nov 12:00 | 109.3–114.3 | BKN 36% | 2.78 / 1.56 | MEM -5.5 | 223.5 | MEM -3.5 covers 55%; o224.5 47% |
| CHI @ MIN | Sun 15 Nov 12:00 | 109.8–125.3 | CHI 14% | 7.39 / 1.16 | MIN -15.5 | 235.5 | MIN -16.5 covers 47%; o237.5 45% |

### DEN @ NOP
Out: Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Julian Strawther (DEN), Cam Whitmore (DEN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey PTS over 18.5 (19+) | DEN @ NOP | sportsbet | 2.02 | 2.00 | 1.99 | 50.1% | 49.9% | 49.9% | +0.9% | +1.3% | 0.2% |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 36.0<br><sub>39,28,34,39,32</sub> | 26.3<br><sub>35,14,16,38,30</sub> | 24.5 · 24.5<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>5,5,6,2,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.6<br><sub>6,7,8,2,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,2,2,5,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.6 | 2.3 | 37.3 |
| Nikola Jokic | 98% | 35.9<br><sub>36,30,36,39,37</sub> | 28.3<br><sub>26,32,19,25,27</sub> | 26.5 · 26.5<br><sub>o 51% · u 49%</sub> | 12.7<br><sub>9,10,13,16,11</sub> | 11.5<br><sub>o 55% · u 45%</sub> | 10.6<br><sub>8,11,8,9,8</sub> | 9.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>2,0,1,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.6 | 1.0 | 3.4 | 51.6 |
| Christian Braun | 98% | 33.2<br><sub>37,28,29,32,37</sub> | 13.4<br><sub>14,11,6,4,12</sub> | 11.5 · 11.5<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>3,3,4,5,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>3,3,1,3,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,1,0,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.5 | 1.0 | 20.4 |
| Cameron Johnson | 98% | 29.6<br><sub>34,30,29,31,30</sub> | 13.4<br><sub>7,12,18,8,23</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>4,2,4,2,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,2,1,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.0<br><sub>1,4,2,2,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.4 | 1.1 | 19.8 |
| Aaron Gordon | 98% | 28.8<br><sub>30,25,27,30,27</sub> | 13.8<br><sub>5,17,12,3,9</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,1,5,5,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>2,0,0,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,1,0,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.4 | 1.3 | 22.0 |
| DeMar DeRozan | 88% | 22.0<br><sub>20,-,22,19,20</sub> | 12.0<br><sub>9,-,11,7,8</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>0,-,1,4,1</sub> |  | 3.3<br><sub>1,-,5,2,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.7 | 0.3 | 1.1 | 17.3 |
| Spencer Jones | 71% | 17.3<br><sub>-,-,21,14,22</sub> | 4.7<br><sub>-,-,13,0,3</sub> |  | 2.8<br><sub>-,-,6,0,1</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.5<br><sub>-,-,3,0,1</sub> |  | 0.7 | 0.6 | 0.5 | 8.3 |
| Trevon Brazile | 98% | 15.6<br><sub>18,23,14,14,13</sub> | 5.2<br><sub>6,6,3,5,7</sub> |  | 4.1<br><sub>5,7,4,2,5</sub> |  | 0.8<br><sub>1,1,2,0,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.4 | 0.6 | 10.1 |
| Marvin Bagley III | 98% | 13.2<br><sub>12,14,12,12,12</sub> | 6.7<br><sub>6,10,10,6,4</sub> |  | 4.1<br><sub>4,2,3,3,2</sub> |  | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 11.5 |
| Tyus Jones | 96% | 10.0<br><sub>8,18,13,6,11</sub> | 2.8<br><sub>2,6,3,2,0</sub> |  | 0.9<br><sub>0,1,4,0,1</sub> |  | 1.8<br><sub>1,8,4,0,4</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.5 |
| Bryce Hopkins | 63% | 8.7<br><sub>-,28,3,3,-</sub> | 3.0<br><sub>-,18,3,2,-</sub> |  | 1.5<br><sub>-,4,1,0,-</sub> |  | 0.5<br><sub>-,1,0,0,-</sub> |  | 0.1<br><sub>-,1,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.0 |
| Zeke Nnaji | 35% | 7.0<br><sub>-,4,-,-,-</sub> | 2.5<br><sub>-,2,-,-,-</sub> |  | 1.6<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.5 |
| Alpha Diallo | 58% | 6.3<br><sub>6,4,-,1,-</sub> | 2.5<br><sub>0,0,-,0,-</sub> |  | 1.0<br><sub>1,0,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zion Williamson | 98% | 34.4<br><sub>36,31,-,30,33</sub> | 22.8<br><sub>13,25,-,29,22</sub> | 20.5 · 20.5<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>8,4,-,4,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>4,2,-,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.2<br><sub>0,0,-,1,0</sub> |  | 1.4 | 0.6 | 2.1 | 32.7 |
| Saddiq Bey | 98% | 33.6<br><sub>31,26,24,29,35</sub> | 19.6<br><sub>17,13,9,15,30</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,4,0,1,10</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>4,3,4,2,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>3,1,1,3,6</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.2 | 1.3 | 27.9 |
| Jeremiah Fears | 98% | 33.0<br><sub>36,29,29,28,34</sub> | 17.6<br><sub>24,25,11,14,18</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>5,6,3,4,5</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>5,5,8,5,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,3,1,2,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.5 | 2.6 | 28.1 |
| Herbert Jones | 98% | 29.0<br><sub>14,20,24,25,32</sub> | 8.9<br><sub>0,4,10,2,8</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>4,0,6,2,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>0,1,1,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1<br><sub>0,0,2,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.5 | 1.1 | 14.7 |
| Derik Queen | 98% | 26.1<br><sub>10,21,21,14,23</sub> | 14.3<br><sub>6,8,16,9,10</sub> |  | 7.3<br><sub>4,5,4,0,6</sub> |  | 3.4<br><sub>1,3,0,0,2</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 1.1 | 0.8 | 2.3 | 24.9 |
| Karlo Matkovic | 96% | 24.8<br><sub>18,19,17,22,19</sub> | 10.3<br><sub>18,3,4,4,1</sub> | 6.5 · 5.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>3,3,6,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,2,2,1,0</sub> |  | 1.2<br><sub>4,1,0,0,0</sub> |  | 0.7 | 0.8 | 1.0 | 17.3 |
| Jordan Poole | 67% | 22.9<br><sub>-,-,34,21,21</sub> | 10.8<br><sub>-,-,7,14,13</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>-,-,3,0,2</sub> |  | 2.9<br><sub>-,-,2,1,5</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>-,-,1,2,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.4 | 1.3 | 15.9 |
| Yves Missi | 97% | 20.2<br><sub>-,-,-,-,-</sub> | 6.2<br><sub>-,-,-,-,-</sub> | 5.5 · 5.5<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>-,-,-,-,-</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 1.5 | 0.9 | 13.9 |
| DeAndre Jordan | 52% | 16.5<br><sub>-,-,-,11,17</sub> | 4.1<br><sub>-,-,-,0,6</sub> |  | 6.2<br><sub>-,-,-,3,8</sub> |  | 1.0<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 11.3 |
| AJ Johnson | 64% | 9.7<br><sub>-,3,12,7,4</sub> | 2.8<br><sub>-,2,2,2,1</sub> |  | 1.4<br><sub>-,0,2,1,0</sub> |  | 0.9<br><sub>-,0,3,0,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.1 |
| Jaron Pierre Jr. | 88% | 9.6<br><sub>-,-,-,7,4</sub> | 3.7<br><sub>-,-,-,4,0</sub> |  | 1.9<br><sub>-,-,-,4,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.8 | 6.3 |
| Julian Reese | 67% | 9.4<br><sub>-,3,9,7,4</sub> | 2.8<br><sub>-,0,2,2,0</sub> |  | 1.6<br><sub>-,0,0,2,2</sub> |  | 0.6<br><sub>-,0,0,1,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.4 | 5.1 |
| Malik Dia | 80% | 8.3<br><sub>-,-,-,-,4</sub> | 2.8<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.3 | 4.3 |

</details>


### DAL @ CLE
Out: Jarrett Allen (CLE), James Harden (CLE), Sam Merrill (CLE), Nae'Qwan Tomlin (CLE), Peyton Watson (CLE), Max Christie (DAL), Sergio de Larrea (DAL), Dereck Lively II (DAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Proctor PTS under 15.5 | DAL @ CLE | draftkings | 1.93 | 1.88 | 1.71 | 58.5% | 52.3% | 53.1% | +2.3% | +12.6% | 0.6% |
| Kyrie Irving PTS under 22.5 | DAL @ CLE | betright | 1.98 | 1.95 | 1.68 | 59.6% | 50.0% | 51.3% | +1.5% | +18.0% | 0.4% |
| Jaylon Tyson PTS under 15.5 | DAL @ CLE | sportsbet | 2.00 | 1.99 | 1.74 | 57.4% | 49.1% | 50.2% | +0.5% | +14.7% | 0.1% |
| Meleek Thomas PTS under 17.5 | DAL @ CLE | tab | 1.95 | 1.94 | 1.56 | 64.3% | 49.5% | 51.4% | +0.4% | +25.4% | 0.1% |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 100% | 33.7<br><sub>40,33,28,39,27</sub> | 23.2<br><sub>19,21,25,43,12</sub> | 24.5 · 24.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>10,10,5,10,7</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 5.6<br><sub>5,7,12,6,3</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,3,3,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.7 | 2.6 | 35.5 |
| Kyrie Irving | 100% | 33.3<br><sub>36,28,29,38,27</sub> | 21.4<br><sub>29,14,21,35,10</sub> | 22.5 · 22.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>7,2,3,0,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>5,2,4,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>5,0,2,7,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 2.0 | 29.6 |
| P.J. Washington | 100% | 32.4<br><sub>39,33,25,35,16</sub> | 14.1<br><sub>21,26,6,13,10</sub> | 13.5 · 12.5<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>10,6,5,9,3</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>3,1,0,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>3,6,2,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.8 | 1.4 | 22.4 |
| Naji Marshall | 91% | 23.9<br><sub>26,25,15,25,23</sub> | 11.6<br><sub>22,7,8,6,13</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>5,1,1,5,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.2<br><sub>3,5,2,2,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.8<br><sub>3,0,1,0,1</sub> |  | 1.0 | 0.1 | 1.5 | 18.1 |
| Zaccharie Risacher | 97% | 20.8<br><sub>18,21,16,15,25</sub> | 7.2<br><sub>2,4,11,4,22</sub> | 6.5 · 5.5<br><sub>o 53% · u 47%</sub> | 3.9<br><sub>1,4,6,2,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,1,1,0,3</sub> |  | 0.8<br><sub>0,0,1,0,4</sub> |  | 0.8 | 0.6 | 0.9 | 12.3 |
| Daniel Gafford | 100% | 20.6<br><sub>18,18,19,20,16</sub> | 8.7<br><sub>2,7,18,8,3</sub> | 7.5 · 7.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>4,1,5,2,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>1,1,2,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 16.0 |
| Caleb Martin | 100% | 18.4<br><sub>20,11,19,19,21</sub> | 4.6<br><sub>0,0,2,0,7</sub> | 4.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>3,0,2,3,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,0,2,5,5</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.8 | 0.3 | 0.7 | 8.7 |
| Walter Clayton Jr. | 91% | 17.7<br><sub>21,23,16,25,22</sub> | 6.4<br><sub>8,12,5,6,5</sub> |  | 2.7<br><sub>6,4,4,6,1</sub> |  | 3.1<br><sub>5,2,6,4,4</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.6 | 0.2 | 1.3 | 12.2 |
| Santi Aldama | 98% | 14.9<br><sub>-,13,15,19,10</sub> | 7.1<br><sub>-,8,12,10,3</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>-,9,2,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>-,1,0,1,1</sub> |  | 0.7<br><sub>-,0,2,1,1</sub> |  | 0.5 | 0.3 | 0.8 | 11.7 |
| Morez Johnson Jr. | 98% | 14.1<br><sub>18,24,19,-,13</sub> | 5.6<br><sub>8,13,4,-,0</sub> |  | 2.7<br><sub>3,17,9,-,2</sub> |  | 1.1<br><sub>1,2,1,-,0</sub> |  | 0.3<br><sub>1,1,0,-,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.4 |
| Marcus Sasser | 67% | 11.1<br><sub>5,-,9,-,9</sub> | 3.9<br><sub>0,-,4,-,3</sub> |  | 0.8<br><sub>1,-,0,-,1</sub> |  | 1.3<br><sub>2,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Moussa Cisse | 64% | 6.9<br><sub>-,1,5,-,8</sub> | 2.4<br><sub>-,0,2,-,0</sub> |  | 2.6<br><sub>-,0,1,-,0</sub> |  | 0.2<br><sub>-,0,1,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.2 |
| Tobi Lawal | 63% | 6.7<br><sub>-,1,5,-,12</sub> | 2.6<br><sub>-,0,2,-,0</sub> |  | 1.3<br><sub>-,0,0,-,6</sub> |  | 0.6<br><sub>-,0,0,-,1</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Jett Howard | 63% | 6.1<br><sub>-,1,3,-,5</sub> | 2.8<br><sub>-,0,5,-,3</sub> |  | 0.7<br><sub>-,0,1,-,0</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,1,-,1</sub> |  | 0.1 | 0.1 | 0.2 | 3.9 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 100% | 35.6<br><sub>33,37,23,36,33</sub> | 29.1<br><sub>23,37,11,23,25</sub> |  | 5.3<br><sub>7,4,2,7,4</sub> |  | 6.3<br><sub>8,4,4,6,7</sub> |  | 3.4<br><sub>1,5,1,2,5</sub> |  | 1.4 | 0.4 | 3.2 | 40.8 |
| Evan Mobley | 100% | 33.9<br><sub>32,33,24,33,-</sub> | 18.6<br><sub>22,12,9,10,-</sub> |  | 9.0<br><sub>6,9,2,5,-</sub> |  | 4.3<br><sub>4,5,3,3,-</sub> |  | 1.4<br><sub>3,1,2,0,-</sub> |  | 0.9 | 1.6 | 2.0 | 31.8 |
| Jaylon Tyson | 100% | 33.3<br><sub>-,-,-,23,30</sub> | 15.1<br><sub>-,-,-,3,16</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>-,-,-,0,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>-,-,-,1,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>-,-,-,1,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.5 | 1.8 | 24.1 |
| Tyrese Proctor | 100% | 32.4<br><sub>19,23,23,23,27</sub> | 15.0<br><sub>3,7,6,15,22</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>6,3,1,3,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>3,3,4,1,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>0,2,0,3,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.1 | 1.6 | 24.1 |
| Meleek Thomas | 100% | 31.2<br><sub>27,24,27,22,18</sub> | 15.8<br><sub>12,9,18,14,12</sub> | 18.5 · 17.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>1,4,3,4,0</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.3<br><sub>3,0,3,1,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>2,3,4,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.4 | 1.4 | 21.7 |
| Mario Hezonja | 98% | 22.6<br><sub>27,19,17,7,9</sub> | 9.2<br><sub>15,0,10,0,4</sub> | 14.5 · 14.5<br><sub>o 44% · u 56%</sub> | 5.9<br><sub>10,5,3,0,4</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,1,0,0,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>2,0,0,0,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.4 | 1.0 | 16.7 |
| Thomas Bryant | 67% | 21.4<br><sub>16,15,15,-,16</sub> | 10.6<br><sub>13,5,11,-,9</sub> | 14.5 · 13.5<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>6,3,2,-,1</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>0,1,0,-,1</sub> |  | 1.2<br><sub>1,1,2,-,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.7 | 1.0 | 17.1 |
| Craig Porter Jr. | 72% | 19.5<br><sub>3,15,17,-,9</sub> | 3.9<br><sub>0,0,9,-,0</sub> | 8.5 · 8.5<br><sub>o 43% · u 57%</sub> | 3.5<br><sub>0,1,2,-,2</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>0,1,4,-,2</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.9 | 0.6 | 0.9 | 11.0 |
| Riley Minix | 47% | 17.0<br><sub>-,10,17,-,-</sub> | 6.0<br><sub>-,8,2,-,-</sub> |  | 2.9<br><sub>-,3,2,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,2,0,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 9.8 |
| Norchad Omier | 48% | 15.7<br><sub>3,-,12,-,-</sub> | 4.6<br><sub>0,-,0,-,-</sub> |  | 3.9<br><sub>2,-,3,-,-</sub> |  | 1.7<br><sub>1,-,2,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.8 | 0.2 | 0.8 | 10.2 |
| Khalifa Diop | 3% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.1 | 0.4 | 5.9 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>


### DET @ MIA
Out: Pelle Larsson (MIA), Jalen Duren (DET), Isaiah Joe (DET)

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 35.2<br><sub>27,40,38,27,48</sub> | 27.2<br><sub>33,26,14,17,52</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,7,4,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 9.0<br><sub>7,11,8,7,11</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>4,1,1,0,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.7 | 3.8 | 41.5 |
| Duncan Robinson | 98% | 32.0<br><sub>32,37,27,34,41</sub> | 16.5<br><sub>24,27,12,22,13</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>2,1,0,3,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,2,3,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.1<br><sub>6,7,3,4,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.2 | 1.1 | 22.1 |
| Daniss Jenkins | 98% | 30.7<br><sub>23,21,32,36,42</sub> | 15.1<br><sub>2,5,31,22,21</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>1,1,5,6,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>7,4,4,8,0</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,1,8,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 1.9 | 24.2 |
| Ausar Thompson | 98% | 30.0<br><sub>26,34,24,28,43</sub> | 11.0<br><sub>14,11,7,8,17</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>6,17,11,5,11</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>4,3,3,4,11</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.8 | 1.0 | 1.9 | 23.3 |
| John Collins | 98% | 26.5<br><sub>19,26,32,28,25</sub> | 11.7<br><sub>4,16,8,24,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>3,1,4,10,4</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>1,0,1,3,0</sub> |  | 1.0<br><sub>0,0,1,2,2</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.8 | 1.3 | 18.8 |
| Paul Reed | 98% | 26.2<br><sub>28,30,20,21,38</sub> | 12.8<br><sub>11,8,8,4,13</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 8.3<br><sub>5,7,10,10,11</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>4,4,0,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.3<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 24% · u 76%</sub> | 1.3 | 1.1 | 1.7 | 23.4 |
| Kevin Huerter | 98% | 24.4<br><sub>20,20,35,33,24</sub> | 10.8<br><sub>9,8,24,12,11</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,1,5,2,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.6<br><sub>3,0,5,3,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>3,2,4,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.5 | 0.9 | 16.5 |
| Javonte Green | 98% | 16.9<br><sub>20,15,17,11,15</sub> | 6.1<br><sub>5,1,7,7,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>2,3,2,1,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.9<br><sub>1,0,1,0,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.3 | 0.4 | 9.4 |
| Ronald Holland II | 98% | 14.4<br><sub>20,12,14,15,14</sub> | 5.6<br><sub>11,3,5,1,2</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>2,2,2,5,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>0,0,1,2,2</sub> |  | 0.5<br><sub>3,1,1,0,0</sub> |  | 0.7 | 0.4 | 0.9 | 9.8 |
| Taurean Prince | 30% | 8.6<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Elijah Harkless | 30% | 6.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| Tolu Smith | 52% | 5.8<br><sub>8,5,-,-,-</sub> | 2.4<br><sub>0,1,-,-,-</sub> |  | 2.1<br><sub>2,1,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Isaac Jones | 52% | 5.7<br><sub>6,-,-,2,-</sub> | 5.8<br><sub>2,-,-,0,-</sub> |  | 1.5<br><sub>5,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 7.7 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 37.2<br><sub>43,38,40,38,39</sub> | 14.2<br><sub>11,22,17,19,22</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,3,5,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 7.8<br><sub>10,8,11,8,17</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>0,4,2,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.3 | 2.4 | 25.1 |
| Bam Adebayo | 98% | 36.0<br><sub>41,33,34,37,38</sub> | 19.1<br><sub>35,18,18,11,37</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 10.0<br><sub>10,10,8,8,14</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>4,0,4,4,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>1,0,1,0,2</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 1.5 | 0.8 | 1.8 | 32.8 |
| Giannis Antetokounmpo | 98% | 34.8<br><sub>41,31,34,31,31</sub> | 27.8<br><sub>27,20,29,30,37</sub> | 28.5 · –<br><sub>o 50% · u 50%</sub> | 12.4<br><sub>14,14,14,11,9</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>6,4,3,4,2</sub> |  | 0.6<br><sub>0,1,0,1,1</sub> | 0.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.1 | 3.6 | 45.8 |
| Andrew Wiggins | 98% | 29.0<br><sub>23,21,32,19,32</sub> | 11.0<br><sub>3,2,6,13,8</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,6,3,0,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>1,4,1,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,0,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.9 | 1.3 | 16.7 |
| Klay Thompson | 76% | 29.0<br><sub>35,23,32,30,-</sub> | 13.5<br><sub>30,11,23,11,-</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>5,0,2,1,-</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.8<br><sub>3,3,4,2,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.9<br><sub>8,2,7,2,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.6 | 1.1 | 17.5 |
| Ryan Conwell | 88% | 24.7<br><sub>17,30,19,21,33</sub> | 8.8<br><sub>0,13,6,5,20</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,2,2,2,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>0,3,2,1,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.2 | 1.0 | 13.2 |
| Bobby Portis | 98% | 20.4<br><sub>18,14,20,17,15</sub> | 8.3<br><sub>4,0,4,5,5</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 5.4<br><sub>10,5,1,1,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>5,0,1,1,2</sub> |  | 1.2<br><sub>0,0,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.6 | 0.3 | 0.8 | 15.0 |
| Tim Hardaway Jr. | 83% | 16.9<br><sub>7,4,7,-,20</sub> | 6.4<br><sub>0,0,0,-,4</sub> |  | 1.6<br><sub>0,0,0,-,3</sub> |  | 0.7<br><sub>0,1,0,-,2</sub> |  | 1.0<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.7 |
| Nikola Jovic | 48% | 12.8<br><sub>-,12,-,-,-</sub> | 4.2<br><sub>-,1,-,-,-</sub> |  | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.7 | 7.6 |
| Myron Gardner | 64% | 12.4<br><sub>-,1,-,10,19</sub> | 3.6<br><sub>-,0,-,4,0</sub> | 4.5 · – | 3.2<br><sub>-,0,-,3,4</sub> | 4.5 | 1.1<br><sub>-,0,-,1,2</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> | 0.5 | 0.5 | 0.3 | 0.6 | 7.9 |
| Dru Smith | 58% | 12.0<br><sub>-,1,-,-,6</sub> | 3.4<br><sub>-,0,-,-,0</sub> |  | 1.6<br><sub>-,0,-,-,0</sub> |  | 1.5<br><sub>-,0,-,-,1</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.8 | 0.2 | 0.6 | 6.6 |
| Keshad Johnson | 38% | 11.6<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.3 | 0.6 | 7.8 |
| Simone Fontecchio | 58% | 10.1<br><sub>5,-,-,7,7</sub> | 4.4<br><sub>0,-,-,3,0</sub> |  | 1.8<br><sub>0,-,-,0,0</sub> |  | 0.7<br><sub>0,-,-,0,2</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.9 |
| Tre Donaldson | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Nick Richards | 43% | 7.4<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.4 | 0.6 | 5.2 |

</details>


### BKN @ MEM
Out: Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Quinten Post (MEM), Grant Nelson (BKN), Ben Saraf (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.3–114.3 | BKN 36% | 2.78 / 1.56 | MEM -5.5 | 223.5 | MEM -3.5 covers 55%; o224.5 47% |
| Expected (weighted by chance each plays) | 109.5–115.4 | BKN 34% | 2.97 / 1.51 | MEM -6.5 | 224.5 | MEM -3.5 covers 58%; o224.5 50% |
| if Zach Edey plays | 107.9–115.8 | BKN 29% | 3.49 / 1.40 | MEM -8.5 | 223.5 | MEM -3.5 covers 63%; o224.5 48% |
| if Michael Porter Jr. plays | 110.6–114.0 | BKN 40% | 2.48 / 1.68 | MEM -3.5 | 224.5 | MEM -3.5 covers 50%; o224.5 50% |
| if Jerami Grant plays | 108.4–115.9 | BKN 30% | 3.36 / 1.42 | MEM -7.5 | 224.5 | MEM -3.5 covers 62%; o224.5 49% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey (MEM) | Questionable | 55% | 24.0 | 10.7 | 9.0 | 1.3 | 0.1 | 0.6 | 1.7 | 1.8 | 21.0 | full tables below |
| Michael Porter Jr. (BKN) | Questionable | 55% | 31.8 | 20.1 | 7.1 | 2.0 | 2.8 | 1.0 | 0.4 | 2.0 | 29.2 | full tables below |
| Jerami Grant (MEM) | Questionable | 55% | 26.3 | 14.5 | 2.8 | 2.0 | 1.8 | 0.7 | 0.6 | 1.6 | 19.2 | full tables below |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 98% | 33.8<br><sub>36,31,34,30,29</sub> | 20.4<br><sub>21,22,19,13,17</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>11,3,7,4,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>2,4,8,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,2,1,0,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 3.5 | 32.1 |
| Egor Demin | 98% | 24.4<br><sub>-,-,-,-,23</sub> | 11.1<br><sub>-,-,-,-,22</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>-,-,-,-,4</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.3 | 1.4 | 17.3 |
| Day'Ron Sharpe | 98% | 24.1<br><sub>22,27,32,20,19</sub> | 10.7<br><sub>4,6,12,6,15</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>6,5,10,4,4</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>3,8,13,6,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,0,2</sub> |  | 1.2 | 1.2 | 2.2 | 22.7 |
| Danny Wolf | 71% | 24.0<br><sub>-,19,31,36,29</sub> | 9.9<br><sub>-,12,11,10,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>-,5,9,3,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>-,3,1,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>-,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.7 | 1.4 | 18.5 |
| Mikel Brown Jr. | 96% | 22.9<br><sub>27,20,25,-,-</sub> | 12.1<br><sub>13,18,18,-,-</sub> |  | 2.4<br><sub>2,2,1,-,-</sub> |  | 3.6<br><sub>3,4,3,-,-</sub> |  | 1.6<br><sub>1,3,3,-,-</sub> |  | 0.8 | 0.2 | 2.1 | 18.0 |
| Nolan Traore | 98% | 22.8<br><sub>24,27,23,21,-</sub> | 12.4<br><sub>17,16,19,14,-</sub> |  | 2.3<br><sub>3,4,1,1,-</sub> |  | 3.5<br><sub>4,2,2,2,-</sub> |  | 1.5<br><sub>5,2,2,2,-</sub> |  | 1.1 | 0.4 | 2.4 | 18.2 |
| Noah Clowney | 98% | 21.1<br><sub>20,17,21,8,19</sub> | 8.5<br><sub>2,7,3,2,16</sub> |  | 4.1<br><sub>6,1,10,0,3</sub> |  | 1.1<br><sub>2,1,0,0,0</sub> |  | 1.1<br><sub>0,1,1,0,2</sub> |  | 0.7 | 0.6 | 1.0 | 13.7 |
| Keon Ellis | 86% | 21.1<br><sub>25,10,-,22,26</sub> | 5.8<br><sub>5,1,-,3,11</sub> |  | 2.3<br><sub>1,2,-,1,4</sub> |  | 1.6<br><sub>0,0,-,4,3</sub> |  | 0.8<br><sub>1,0,-,1,2</sub> |  | 1.3 | 0.7 | 0.7 | 9.7 |
| Moritz Wagner | 96% | 18.2<br><sub>20,20,16,16,19</sub> | 10.2<br><sub>6,6,9,12,16</sub> |  | 4.2<br><sub>1,1,2,3,3</sub> |  | 1.3<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 0.6 | 0.3 | 1.1 | 15.7 |
| Chaney Johnson | 96% | 17.1<br><sub>28,9,8,15,15</sub> | 4.9<br><sub>4,0,5,2,4</sub> |  | 2.5<br><sub>3,2,2,0,3</sub> |  | 1.0<br><sub>2,1,1,1,2</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.4 | 0.9 | 8.4 |
| Terance Mann | 72% | 16.9<br><sub>-,16,13,22,18</sub> | 4.0<br><sub>-,0,0,0,6</sub> |  | 2.1<br><sub>-,2,2,1,1</sub> |  | 1.7<br><sub>-,2,0,1,3</sub> |  | 0.4<br><sub>-,0,0,0,2</sub> |  | 0.6 | 0.2 | 0.7 | 7.9 |
| Josh Minott | 63% | 11.9<br><sub>-,6,-,12,7</sub> | 6.3<br><sub>-,0,-,10,0</sub> |  | 2.2<br><sub>-,1,-,2,2</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.7<br><sub>-,0,-,2,0</sub> |  | 0.7 | 0.5 | 0.7 | 9.2 |
| Drake Powell | 58% | 11.6<br><sub>-,-,-,9,7</sub> | 3.7<br><sub>-,-,-,2,6</sub> |  | 1.2<br><sub>-,-,-,2,0</sub> |  | 0.8<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 5.7 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 34.8<br><sub>33,31,33,33,25</sub> | 19.5<br><sub>10,8,22,13,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 10.4<br><sub>6,12,7,11,10</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>4,4,8,5,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>2,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.7 | 3.3 | 35.8 |
| Cedric Coward | 98% | 31.3<br><sub>33,23,28,27,30</sub> | 18.1<br><sub>23,10,3,15,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>9,9,6,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,0,4,4,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>4,2,1,1,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.5 | 2.2 | 29.5 |
| Jaylen Wells | 98% | 30.7<br><sub>21,25,26,31,27</sub> | 16.0<br><sub>0,7,14,22,11</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>1,0,4,2,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>3,0,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>0,1,4,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.4 | 21.2 |
| Cam Spencer | 98% | 26.8<br><sub>24,19,17,20,24</sub> | 12.9<br><sub>7,7,7,15,14</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>6,1,2,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>9,0,4,3,5</sub> | 8.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 1.8 | 22.4 |
| Isaiah Stewart | 98% | 25.0<br><sub>10,-,-,18,20</sub> | 12.2<br><sub>6,-,-,3,12</sub> |  | 5.4<br><sub>1,-,-,1,5</sub> |  | 1.2<br><sub>0,-,-,2,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.4 | 1.6 | 1.3 | 18.8 |
| Javon Small | 96% | 24.8<br><sub>-,21,24,15,15</sub> | 12.0<br><sub>-,10,9,3,10</sub> |  | 3.6<br><sub>-,4,2,1,2</sub> |  | 4.2<br><sub>-,2,5,4,5</sub> |  | 1.5<br><sub>-,1,1,1,2</sub> |  | 1.0 | 0.3 | 1.7 | 19.7 |
| GG Jackson | 88% | 22.8<br><sub>7,-,17,13,22</sub> | 13.4<br><sub>1,-,2,2,14</sub> |  | 4.4<br><sub>2,-,1,1,6</sub> |  | 1.6<br><sub>0,-,0,0,4</sub> |  | 1.4<br><sub>0,-,0,0,3</sub> |  | 0.6 | 0.7 | 1.6 | 19.4 |
| Taylor Hendricks | 72% | 19.3<br><sub>-,4,16,11,19</sub> | 8.0<br><sub>-,4,9,7,10</sub> |  | 4.3<br><sub>-,2,3,2,12</sub> |  | 1.0<br><sub>-,0,0,1,2</sub> |  | 1.1<br><sub>-,1,1,1,2</sub> |  | 1.0 | 0.5 | 0.9 | 13.3 |
| Jahmai Mashack | 48% | 16.3<br><sub>-,4,-,-,-</sub> | 5.0<br><sub>-,0,-,-,-</sub> |  | 2.2<br><sub>-,0,-,-,-</sub> |  | 2.1<br><sub>-,2,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.8 | 0.3 | 1.3 | 9.3 |
| Kris Murray | 71% | 16.0<br><sub>15,13,1,-,1</sub> | 3.8<br><sub>5,2,0,-,0</sub> |  | 2.6<br><sub>1,2,0,-,1</sub> |  | 1.0<br><sub>1,1,0,-,0</sub> |  | 0.3<br><sub>1,0,0,-,0</sub> |  | 0.6 | 0.3 | 0.6 | 7.4 |
| Olivier-Maxence Prosper | 64% | 13.6<br><sub>7,11,1,-,2</sub> | 7.3<br><sub>4,2,0,-,6</sub> |  | 2.8<br><sub>3,3,0,-,1</sub> |  | 0.8<br><sub>1,1,0,-,0</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 10.9 |
| Karim Lopez | 48% | 9.6<br><sub>-,4,-,-,-</sub> | 2.7<br><sub>-,2,-,-,-</sub> |  | 1.8<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.4 | 0.6 | 5.0 |

</details>

<details><summary>if Michael Porter Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. (BKN) | 100% | 31.8<br><sub>37,38,36,29,28</sub> | 20.1<br><sub>18,26,25,19,22</sub> | 21.5 · – | 7.1<br><sub>5,10,9,9,6</sub> | 6.5 | 2.0<br><sub>2,0,1,0,3</sub> | 1.5 | 2.8<br><sub>4,4,3,4,4</sub> | 3.5 | 1.0 | 0.4 | 2.0 | 29.2 |
| Julius Randle (BKN) | 98% | 31.3<br><sub>36,31,34,30,29</sub> | 17.8<br><sub>21,22,19,13,17</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 6.5<br><sub>11,3,7,4,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>2,4,8,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>0,2,1,0,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.2 | 3.0 | 28.7 |
| Egor Demin (BKN) | 98% | 21.6<br><sub>-,-,-,-,23</sub> | 9.0<br><sub>-,-,-,-,22</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>-,-,-,-,4</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.8 | 0.3 | 1.3 | 14.5 |
| Day'Ron Sharpe (BKN) | 98% | 21.3<br><sub>22,27,32,20,19</sub> | 9.3<br><sub>4,6,12,6,15</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>6,5,10,4,4</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>3,8,13,6,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 0.3<br><sub>0,0,0,0,2</sub> |  | 1.0 | 1.1 | 1.8 | 19.9 |
| Mikel Brown Jr. (BKN) | 96% | 20.1<br><sub>27,20,25,-,-</sub> | 10.7<br><sub>13,18,18,-,-</sub> |  | 2.2<br><sub>2,2,1,-,-</sub> |  | 3.2<br><sub>3,4,3,-,-</sub> |  | 1.3<br><sub>1,3,3,-,-</sub> |  | 0.8 | 0.2 | 1.7 | 16.1 |
| Danny Wolf (BKN) | 71% | 20.1<br><sub>-,19,31,36,29</sub> | 7.9<br><sub>-,12,11,10,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>-,5,9,3,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>-,3,1,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>-,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.6 | 1.2 | 15.2 |
| Nolan Traore (BKN) | 98% | 19.4<br><sub>24,27,23,21,-</sub> | 9.7<br><sub>17,16,19,14,-</sub> |  | 1.9<br><sub>3,4,1,1,-</sub> |  | 3.0<br><sub>4,2,2,2,-</sub> |  | 1.1<br><sub>5,2,2,2,-</sub> |  | 0.9 | 0.4 | 1.9 | 14.6 |
| Keon Ellis (BKN) | 86% | 18.4<br><sub>25,10,-,22,26</sub> | 4.7<br><sub>5,1,-,3,11</sub> |  | 2.0<br><sub>1,2,-,1,4</sub> |  | 1.4<br><sub>0,0,-,4,3</sub> |  | 0.6<br><sub>1,0,-,1,2</sub> |  | 1.1 | 0.6 | 0.6 | 8.2 |
| Noah Clowney (BKN) | 98% | 17.5<br><sub>20,17,21,8,19</sub> | 6.5<br><sub>2,7,3,2,16</sub> |  | 3.4<br><sub>6,1,10,0,3</sub> |  | 0.9<br><sub>2,1,0,0,0</sub> |  | 0.8<br><sub>0,1,1,0,2</sub> |  | 0.6 | 0.5 | 0.8 | 10.7 |
| Moritz Wagner (BKN) | 96% | 16.5<br><sub>20,20,16,16,19</sub> | 9.3<br><sub>6,6,9,12,16</sub> |  | 3.9<br><sub>1,1,2,3,3</sub> |  | 1.1<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 0.6 | 0.2 | 1.0 | 14.3 |
| Terance Mann (BKN) | 72% | 14.8<br><sub>-,16,13,22,18</sub> | 3.6<br><sub>-,0,0,0,6</sub> |  | 1.9<br><sub>-,2,2,1,1</sub> |  | 1.6<br><sub>-,2,0,1,3</sub> |  | 0.3<br><sub>-,0,0,0,2</sub> |  | 0.6 | 0.2 | 0.6 | 7.0 |
| Chaney Johnson (BKN) | 96% | 13.7<br><sub>28,9,8,15,15</sub> | 3.7<br><sub>4,0,5,2,4</sub> |  | 2.1<br><sub>3,2,2,0,3</sub> |  | 0.8<br><sub>2,1,1,1,2</sub> |  | 0.3<br><sub>1,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 6.6 |
| Josh Minott (BKN) | 63% | 9.0<br><sub>-,6,-,12,7</sub> | 4.7<br><sub>-,0,-,10,0</sub> |  | 1.7<br><sub>-,1,-,2,2</sub> |  | 0.5<br><sub>-,0,-,1,0</sub> |  | 0.5<br><sub>-,0,-,2,0</sub> |  | 0.5 | 0.3 | 0.5 | 6.9 |
| Drake Powell (BKN) | 58% | 8.5<br><sub>-,-,-,9,7</sub> | 2.5<br><sub>-,-,-,2,6</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.6<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.0 |
| Cameron Boozer (MEM) | 98% | 34.8<br><sub>33,31,33,33,25</sub> | 19.6<br><sub>10,8,22,13,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 10.4<br><sub>6,12,7,11,10</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>4,4,8,5,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>2,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.7 | 3.3 | 35.8 |
| Cedric Coward (MEM) | 98% | 31.3<br><sub>33,23,28,27,30</sub> | 18.0<br><sub>23,10,3,15,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>9,9,6,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,0,4,4,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>4,2,1,1,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.5 | 2.2 | 29.6 |
| Jaylen Wells (MEM) | 98% | 30.6<br><sub>21,25,26,31,27</sub> | 15.9<br><sub>0,7,14,22,11</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>1,0,4,2,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>3,0,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>0,1,4,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.4 | 21.2 |
| Cam Spencer (MEM) | 98% | 26.8<br><sub>24,19,17,20,24</sub> | 12.8<br><sub>7,7,7,15,14</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>6,1,2,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>9,0,4,3,5</sub> | 8.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 1.8 | 22.2 |
| Isaiah Stewart (MEM) | 98% | 24.9<br><sub>10,-,-,18,20</sub> | 12.2<br><sub>6,-,-,3,12</sub> |  | 5.4<br><sub>1,-,-,1,5</sub> |  | 1.2<br><sub>0,-,-,2,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.4 | 1.6 | 1.3 | 18.8 |
| Javon Small (MEM) | 96% | 24.8<br><sub>-,21,24,15,15</sub> | 12.1<br><sub>-,10,9,3,10</sub> |  | 3.6<br><sub>-,4,2,1,2</sub> |  | 4.2<br><sub>-,2,5,4,5</sub> |  | 1.5<br><sub>-,1,1,1,2</sub> |  | 1.0 | 0.3 | 1.7 | 19.8 |
| GG Jackson (MEM) | 88% | 22.8<br><sub>7,-,17,13,22</sub> | 13.4<br><sub>1,-,2,2,14</sub> |  | 4.4<br><sub>2,-,1,1,6</sub> |  | 1.6<br><sub>0,-,0,0,4</sub> |  | 1.4<br><sub>0,-,0,0,3</sub> |  | 0.6 | 0.7 | 1.6 | 19.4 |
| Taylor Hendricks (MEM) | 72% | 19.3<br><sub>-,4,16,11,19</sub> | 8.0<br><sub>-,4,9,7,10</sub> |  | 4.3<br><sub>-,2,3,2,12</sub> |  | 1.0<br><sub>-,0,0,1,2</sub> |  | 1.1<br><sub>-,1,1,1,2</sub> |  | 1.0 | 0.5 | 0.9 | 13.3 |
| Jahmai Mashack (MEM) | 48% | 16.4<br><sub>-,4,-,-,-</sub> | 4.9<br><sub>-,0,-,-,-</sub> |  | 2.2<br><sub>-,0,-,-,-</sub> |  | 2.1<br><sub>-,2,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.9 | 0.3 | 1.3 | 9.3 |
| Kris Murray (MEM) | 71% | 15.9<br><sub>15,13,1,-,1</sub> | 3.8<br><sub>5,2,0,-,0</sub> |  | 2.6<br><sub>1,2,0,-,1</sub> |  | 1.0<br><sub>1,1,0,-,0</sub> |  | 0.3<br><sub>1,0,0,-,0</sub> |  | 0.6 | 0.3 | 0.6 | 7.4 |
| Olivier-Maxence Prosper (MEM) | 64% | 13.6<br><sub>7,11,1,-,2</sub> | 7.3<br><sub>4,2,0,-,6</sub> |  | 2.8<br><sub>3,3,0,-,1</sub> |  | 0.8<br><sub>1,1,0,-,0</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 10.8 |
| Karim Lopez (MEM) | 48% | 9.7<br><sub>-,4,-,-,-</sub> | 2.7<br><sub>-,2,-,-,-</sub> |  | 1.8<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.4 | 0.6 | 5.1 |

</details>

<details><summary>if Zach Edey plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle (BKN) | 98% | 33.8<br><sub>36,31,34,30,29</sub> | 20.3<br><sub>21,22,19,13,17</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>11,3,7,4,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>2,4,8,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,2,1,0,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.3 | 3.5 | 32.0 |
| Egor Demin (BKN) | 98% | 24.5<br><sub>-,-,-,-,23</sub> | 11.0<br><sub>-,-,-,-,22</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>-,-,-,-,4</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.3 | 1.5 | 17.2 |
| Day'Ron Sharpe (BKN) | 98% | 24.1<br><sub>22,27,32,20,19</sub> | 10.8<br><sub>4,6,12,6,15</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>6,5,10,4,4</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>3,8,13,6,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,0,2</sub> |  | 1.2 | 1.2 | 2.2 | 22.8 |
| Danny Wolf (BKN) | 71% | 24.0<br><sub>-,19,31,36,29</sub> | 9.9<br><sub>-,12,11,10,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>-,5,9,3,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>-,3,1,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>-,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.7 | 1.4 | 18.5 |
| Mikel Brown Jr. (BKN) | 96% | 22.8<br><sub>27,20,25,-,-</sub> | 11.9<br><sub>13,18,18,-,-</sub> |  | 2.4<br><sub>2,2,1,-,-</sub> |  | 3.6<br><sub>3,4,3,-,-</sub> |  | 1.6<br><sub>1,3,3,-,-</sub> |  | 0.8 | 0.2 | 2.1 | 17.9 |
| Nolan Traore (BKN) | 98% | 22.8<br><sub>24,27,23,21,-</sub> | 12.4<br><sub>17,16,19,14,-</sub> |  | 2.3<br><sub>3,4,1,1,-</sub> |  | 3.5<br><sub>4,2,2,2,-</sub> |  | 1.5<br><sub>5,2,2,2,-</sub> |  | 1.1 | 0.4 | 2.4 | 18.2 |
| Keon Ellis (BKN) | 86% | 21.2<br><sub>25,10,-,22,26</sub> | 5.7<br><sub>5,1,-,3,11</sub> |  | 2.3<br><sub>1,2,-,1,4</sub> |  | 1.6<br><sub>0,0,-,4,3</sub> |  | 0.8<br><sub>1,0,-,1,2</sub> |  | 1.3 | 0.6 | 0.7 | 9.7 |
| Noah Clowney (BKN) | 98% | 21.1<br><sub>20,17,21,8,19</sub> | 8.4<br><sub>2,7,3,2,16</sub> |  | 4.1<br><sub>6,1,10,0,3</sub> |  | 1.1<br><sub>2,1,0,0,0</sub> |  | 1.1<br><sub>0,1,1,0,2</sub> |  | 0.7 | 0.6 | 1.0 | 13.6 |
| Moritz Wagner (BKN) | 96% | 18.2<br><sub>20,20,16,16,19</sub> | 10.1<br><sub>6,6,9,12,16</sub> |  | 4.2<br><sub>1,1,2,3,3</sub> |  | 1.3<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 0.6 | 0.3 | 1.1 | 15.7 |
| Chaney Johnson (BKN) | 96% | 17.0<br><sub>28,9,8,15,15</sub> | 4.9<br><sub>4,0,5,2,4</sub> |  | 2.5<br><sub>3,2,2,0,3</sub> |  | 1.0<br><sub>2,1,1,1,2</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.4 | 0.9 | 8.4 |
| Terance Mann (BKN) | 72% | 16.8<br><sub>-,16,13,22,18</sub> | 4.0<br><sub>-,0,0,0,6</sub> |  | 2.1<br><sub>-,2,2,1,1</sub> |  | 1.7<br><sub>-,2,0,1,3</sub> |  | 0.4<br><sub>-,0,0,0,2</sub> |  | 0.6 | 0.2 | 0.7 | 7.8 |
| Josh Minott (BKN) | 63% | 12.0<br><sub>-,6,-,12,7</sub> | 6.2<br><sub>-,0,-,10,0</sub> |  | 2.3<br><sub>-,1,-,2,2</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.7<br><sub>-,0,-,2,0</sub> |  | 0.7 | 0.5 | 0.7 | 9.1 |
| Drake Powell (BKN) | 58% | 11.6<br><sub>-,-,-,9,7</sub> | 3.7<br><sub>-,-,-,2,6</sub> |  | 1.2<br><sub>-,-,-,2,0</sub> |  | 0.8<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 5.7 |
| Cameron Boozer (MEM) | 98% | 34.2<br><sub>33,31,33,33,25</sub> | 18.9<br><sub>10,8,22,13,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 9.9<br><sub>6,12,7,11,10</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>4,4,8,5,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>2,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.6 | 3.2 | 34.6 |
| Cedric Coward (MEM) | 98% | 30.9<br><sub>33,23,28,27,30</sub> | 17.2<br><sub>23,10,3,15,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>9,9,6,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>4,0,4,4,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>4,2,1,1,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.5 | 2.0 | 28.4 |
| Jaylen Wells (MEM) | 98% | 29.8<br><sub>21,25,26,31,27</sub> | 14.7<br><sub>0,7,14,22,11</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>1,0,4,2,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>3,0,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>0,1,4,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.1 | 1.2 | 19.8 |
| Cam Spencer (MEM) | 98% | 25.1<br><sub>24,19,17,20,24</sub> | 11.8<br><sub>7,7,7,15,14</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>6,1,2,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>9,0,4,3,5</sub> | 8.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 1.6 | 21.0 |
| Zach Edey (MEM) | 100% | 24.0<br><sub>25,20,23,20,-</sub> | 10.7<br><sub>11,14,8,2,-</sub> | 8.5 · – | 9.0<br><sub>13,6,9,5,-</sub> | 7.5 | 1.3<br><sub>1,1,1,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.6 | 1.7 | 1.8 | 21.0 |
| Javon Small (MEM) | 96% | 23.1<br><sub>-,21,24,15,15</sub> | 10.8<br><sub>-,10,9,3,10</sub> |  | 3.2<br><sub>-,4,2,1,2</sub> |  | 4.3<br><sub>-,2,5,4,5</sub> |  | 1.4<br><sub>-,1,1,1,2</sub> |  | 0.9 | 0.3 | 1.6 | 18.2 |
| GG Jackson (MEM) | 88% | 20.7<br><sub>7,-,17,13,22</sub> | 11.9<br><sub>1,-,2,2,14</sub> |  | 3.9<br><sub>2,-,1,1,6</sub> |  | 1.6<br><sub>0,-,0,0,4</sub> |  | 1.2<br><sub>0,-,0,0,3</sub> |  | 0.5 | 0.7 | 1.5 | 17.3 |
| Isaiah Stewart (MEM) | 98% | 19.6<br><sub>10,-,-,18,20</sub> | 9.4<br><sub>6,-,-,3,12</sub> |  | 4.1<br><sub>1,-,-,1,5</sub> |  | 1.0<br><sub>0,-,-,2,0</sub> |  | 0.6<br><sub>0,-,-,1,0</sub> |  | 0.3 | 1.2 | 1.1 | 14.4 |
| Taylor Hendricks (MEM) | 72% | 16.9<br><sub>-,4,16,11,19</sub> | 7.0<br><sub>-,4,9,7,10</sub> |  | 3.7<br><sub>-,2,3,2,12</sub> |  | 0.9<br><sub>-,0,0,1,2</sub> |  | 0.9<br><sub>-,1,1,1,2</sub> |  | 0.8 | 0.5 | 0.8 | 11.6 |
| Jahmai Mashack (MEM) | 48% | 15.5<br><sub>-,4,-,-,-</sub> | 4.8<br><sub>-,0,-,-,-</sub> |  | 2.0<br><sub>-,0,-,-,-</sub> |  | 2.2<br><sub>-,2,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.8 | 0.3 | 1.3 | 9.1 |
| Kris Murray (MEM) | 71% | 13.4<br><sub>15,13,1,-,1</sub> | 3.5<br><sub>5,2,0,-,0</sub> |  | 2.1<br><sub>1,2,0,-,1</sub> |  | 0.8<br><sub>1,1,0,-,0</sub> |  | 0.2<br><sub>1,0,0,-,0</sub> |  | 0.5 | 0.3 | 0.5 | 6.4 |
| Olivier-Maxence Prosper (MEM) | 64% | 11.4<br><sub>7,11,1,-,2</sub> | 6.3<br><sub>4,2,0,-,6</sub> |  | 2.2<br><sub>3,3,0,-,1</sub> |  | 0.7<br><sub>1,1,0,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 9.2 |
| Karim Lopez (MEM) | 48% | 7.7<br><sub>-,4,-,-,-</sub> | 2.3<br><sub>-,2,-,-,-</sub> |  | 1.3<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 4.1 |

</details>

<details><summary>if Jerami Grant plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle (BKN) | 98% | 33.8<br><sub>36,31,34,30,29</sub> | 20.4<br><sub>21,22,19,13,17</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>11,3,7,4,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>2,4,8,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>0,2,1,0,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.3 | 3.5 | 32.1 |
| Egor Demin (BKN) | 98% | 24.4<br><sub>-,-,-,-,23</sub> | 11.0<br><sub>-,-,-,-,22</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>-,-,-,-,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>-,-,-,-,4</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.3 | 1.4 | 17.2 |
| Day'Ron Sharpe (BKN) | 98% | 24.1<br><sub>22,27,32,20,19</sub> | 10.7<br><sub>4,6,12,6,15</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 8.2<br><sub>6,5,10,4,4</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>3,8,13,6,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,0,2</sub> |  | 1.2 | 1.2 | 2.2 | 22.7 |
| Danny Wolf (BKN) | 71% | 24.0<br><sub>-,19,31,36,29</sub> | 10.0<br><sub>-,12,11,10,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>-,5,9,3,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>-,3,1,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>-,2,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.7 | 1.4 | 18.5 |
| Nolan Traore (BKN) | 98% | 22.9<br><sub>24,27,23,21,-</sub> | 12.4<br><sub>17,16,19,14,-</sub> |  | 2.3<br><sub>3,4,1,1,-</sub> |  | 3.5<br><sub>4,2,2,2,-</sub> |  | 1.5<br><sub>5,2,2,2,-</sub> |  | 1.1 | 0.4 | 2.4 | 18.2 |
| Mikel Brown Jr. (BKN) | 96% | 22.7<br><sub>27,20,25,-,-</sub> | 12.0<br><sub>13,18,18,-,-</sub> |  | 2.4<br><sub>2,2,1,-,-</sub> |  | 3.5<br><sub>3,4,3,-,-</sub> |  | 1.6<br><sub>1,3,3,-,-</sub> |  | 0.8 | 0.2 | 2.1 | 17.9 |
| Noah Clowney (BKN) | 98% | 21.1<br><sub>20,17,21,8,19</sub> | 8.4<br><sub>2,7,3,2,16</sub> |  | 4.1<br><sub>6,1,10,0,3</sub> |  | 1.1<br><sub>2,1,0,0,0</sub> |  | 1.1<br><sub>0,1,1,0,2</sub> |  | 0.7 | 0.6 | 1.0 | 13.6 |
| Keon Ellis (BKN) | 86% | 21.1<br><sub>25,10,-,22,26</sub> | 5.7<br><sub>5,1,-,3,11</sub> |  | 2.3<br><sub>1,2,-,1,4</sub> |  | 1.6<br><sub>0,0,-,4,3</sub> |  | 0.8<br><sub>1,0,-,1,2</sub> |  | 1.3 | 0.6 | 0.7 | 9.6 |
| Moritz Wagner (BKN) | 96% | 18.2<br><sub>20,20,16,16,19</sub> | 10.1<br><sub>6,6,9,12,16</sub> |  | 4.2<br><sub>1,1,2,3,3</sub> |  | 1.3<br><sub>2,0,0,1,4</sub> |  | 0.7<br><sub>1,0,1,1,2</sub> |  | 0.6 | 0.3 | 1.1 | 15.6 |
| Chaney Johnson (BKN) | 96% | 17.1<br><sub>28,9,8,15,15</sub> | 4.9<br><sub>4,0,5,2,4</sub> |  | 2.5<br><sub>3,2,2,0,3</sub> |  | 1.0<br><sub>2,1,1,1,2</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.4 | 0.9 | 8.4 |
| Terance Mann (BKN) | 72% | 16.9<br><sub>-,16,13,22,18</sub> | 4.0<br><sub>-,0,0,0,6</sub> |  | 2.1<br><sub>-,2,2,1,1</sub> |  | 1.7<br><sub>-,2,0,1,3</sub> |  | 0.4<br><sub>-,0,0,0,2</sub> |  | 0.6 | 0.2 | 0.7 | 7.8 |
| Josh Minott (BKN) | 63% | 11.9<br><sub>-,6,-,12,7</sub> | 6.2<br><sub>-,0,-,10,0</sub> |  | 2.2<br><sub>-,1,-,2,2</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.7<br><sub>-,0,-,2,0</sub> |  | 0.7 | 0.5 | 0.6 | 9.1 |
| Drake Powell (BKN) | 58% | 11.7<br><sub>-,-,-,9,7</sub> | 3.7<br><sub>-,-,-,2,6</sub> |  | 1.2<br><sub>-,-,-,2,0</sub> |  | 0.9<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 5.8 |
| Cameron Boozer (MEM) | 98% | 33.2<br><sub>33,31,33,33,25</sub> | 18.1<br><sub>10,8,22,13,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 9.9<br><sub>6,12,7,11,10</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,4,8,5,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.6 | 3.0 | 33.2 |
| Cedric Coward (MEM) | 98% | 29.9<br><sub>33,23,28,27,30</sub> | 16.8<br><sub>23,10,3,15,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>9,9,6,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>4,0,4,4,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>4,2,1,1,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.5 | 1.9 | 27.8 |
| Jaylen Wells (MEM) | 98% | 29.1<br><sub>21,25,26,31,27</sub> | 14.4<br><sub>0,7,14,22,11</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>1,0,4,2,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>3,0,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>0,1,4,5,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.2 | 19.4 |
| Jerami Grant (MEM) | 100% | 26.3<br><sub>24,22,22,20,26</sub> | 14.5<br><sub>11,10,17,14,22</sub> | 11.5 · – | 2.8<br><sub>1,0,3,2,1</sub> | 2.5 | 2.0<br><sub>2,2,2,2,1</sub> |  | 1.8<br><sub>2,2,3,2,3</sub> | 1.5 | 0.7 | 0.6 | 1.6 | 19.2 |
| Cam Spencer (MEM) | 98% | 24.8<br><sub>24,19,17,20,24</sub> | 11.4<br><sub>7,7,7,15,14</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>6,1,2,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>9,0,4,3,5</sub> | 8.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 1.4 | 20.4 |
| Javon Small (MEM) | 96% | 22.6<br><sub>-,21,24,15,15</sub> | 10.4<br><sub>-,10,9,3,10</sub> |  | 3.3<br><sub>-,4,2,1,2</sub> |  | 3.9<br><sub>-,2,5,4,5</sub> |  | 1.3<br><sub>-,1,1,1,2</sub> |  | 0.9 | 0.3 | 1.4 | 17.6 |
| Isaiah Stewart (MEM) | 98% | 21.0<br><sub>10,-,-,18,20</sub> | 9.9<br><sub>6,-,-,3,12</sub> |  | 4.7<br><sub>1,-,-,1,5</sub> |  | 1.0<br><sub>0,-,-,2,0</sub> |  | 0.7<br><sub>0,-,-,1,0</sub> |  | 0.4 | 1.3 | 1.1 | 15.5 |
| GG Jackson (MEM) | 88% | 19.2<br><sub>7,-,17,13,22</sub> | 11.1<br><sub>1,-,2,2,14</sub> |  | 3.8<br><sub>2,-,1,1,6</sub> |  | 1.4<br><sub>0,-,0,0,4</sub> |  | 1.1<br><sub>0,-,0,0,3</sub> |  | 0.5 | 0.6 | 1.3 | 16.2 |
| Taylor Hendricks (MEM) | 72% | 16.1<br><sub>-,4,16,11,19</sub> | 6.7<br><sub>-,4,9,7,10</sub> |  | 3.6<br><sub>-,2,3,2,12</sub> |  | 0.8<br><sub>-,0,0,1,2</sub> |  | 0.8<br><sub>-,1,1,1,2</sub> |  | 0.8 | 0.4 | 0.8 | 11.1 |
| Jahmai Mashack (MEM) | 48% | 15.2<br><sub>-,4,-,-,-</sub> | 4.8<br><sub>-,0,-,-,-</sub> |  | 2.0<br><sub>-,0,-,-,-</sub> |  | 2.1<br><sub>-,2,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.8 | 0.3 | 1.2 | 8.9 |
| Kris Murray (MEM) | 71% | 12.3<br><sub>15,13,1,-,1</sub> | 3.1<br><sub>5,2,0,-,0</sub> |  | 2.0<br><sub>1,2,0,-,1</sub> |  | 0.8<br><sub>1,1,0,-,0</sub> |  | 0.2<br><sub>1,0,0,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 5.8 |
| Olivier-Maxence Prosper (MEM) | 64% | 10.3<br><sub>7,11,1,-,2</sub> | 5.7<br><sub>4,2,0,-,6</sub> |  | 2.1<br><sub>3,3,0,-,1</sub> |  | 0.6<br><sub>1,1,0,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.1 | 0.5 | 8.4 |
| Karim Lopez (MEM) | 48% | 7.2<br><sub>-,4,-,-,-</sub> | 2.4<br><sub>-,2,-,-,-</sub> |  | 1.3<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.4 | 0.5 | 4.1 |

</details>


### CHI @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Tobe Awaka (CHI), Nic Claxton (CHI), Jalen Smith (CHI), Dailyn Swain (CHI), Caleb Wilson (CHI)

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 32.9<br><sub>32,27,34,25,39</sub> | 15.9<br><sub>13,10,19,9,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>4,1,7,2,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 8.4<br><sub>10,6,15,7,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>2,1,1,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.6 | 3.5 | 31.6 |
| Norman Powell | 98% | 32.0<br><sub>29,22,-,-,31</sub> | 21.6<br><sub>18,12,-,-,33</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>3,1,-,-,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>0,1,-,-,2</sub> |  | 2.3<br><sub>1,0,-,-,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.2 | 2.4 | 27.4 |
| Isaac Okoro | 98% | 31.5<br><sub>21,15,25,23,41</sub> | 10.1<br><sub>4,6,12,0,15</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>1,1,2,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>0,0,1,4,2</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 1.0 | 0.5 | 1.1 | 15.1 |
| Matas Buzelis | 98% | 31.2<br><sub>23,26,31,31,29</sub> | 15.9<br><sub>4,12,19,13,11</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>3,5,5,3,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,3,2,2,2</sub> |  | 1.8<br><sub>0,1,3,3,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 1.3 | 2.6 | 23.8 |
| Patrick Williams | 67% | 27.6<br><sub>-,20,25,28,24</sub> | 9.2<br><sub>-,4,7,9,13</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>-,0,3,7,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>-,2,3,4,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.2<br><sub>-,0,1,0,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.5 | 1.3 | 15.1 |
| Tre Jones | 98% | 22.3<br><sub>19,18,14,28,15</sub> | 12.5<br><sub>8,14,6,13,4</sub> |  | 3.0<br><sub>3,3,1,1,1</sub> |  | 3.8<br><sub>3,4,1,3,3</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.1 | 1.5 | 19.2 |
| Buddy Hield | 66% | 20.5<br><sub>12,8,-,-,25</sub> | 8.9<br><sub>6,7,-,-,12</sub> |  | 2.9<br><sub>1,1,-,-,3</sub> |  | 1.8<br><sub>3,1,-,-,3</sub> |  | 1.2<br><sub>1,1,-,-,2</sub> |  | 0.9 | 0.3 | 1.2 | 13.6 |
| Jordan Hawkins | 66% | 18.1<br><sub>2,7,17,24,-</sub> | 7.5<br><sub>2,2,9,7,-</sub> |  | 2.5<br><sub>0,1,0,4,-</sub> |  | 1.0<br><sub>0,0,1,2,-</sub> |  | 0.9<br><sub>0,0,1,1,-</sub> |  | 0.5 | 0.3 | 1.0 | 11.0 |
| Leonard Miller | 64% | 17.0<br><sub>9,19,-,2,-</sub> | 7.7<br><sub>2,4,-,0,-</sub> |  | 4.1<br><sub>3,6,-,0,-</sub> |  | 0.8<br><sub>0,3,-,0,-</sub> |  | 0.7<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.5 | 0.9 | 12.6 |
| Noa Essengue | 96% | 16.7<br><sub>14,14,15,11,8</sub> | 6.8<br><sub>8,6,10,8,5</sub> |  | 3.6<br><sub>6,3,7,4,1</sub> |  | 0.8<br><sub>0,0,1,3,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.3 | 0.8 | 11.2 |
| Orlando Robinson | 38% | 14.4<br><sub>-,-,-,-,-</sub> | 5.4<br><sub>-,-,-,-,-</sub> |  | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.9 | 10.8 |
| Zach Collins | 66% | 14.3<br><sub>10,14,-,3,-</sub> | 5.7<br><sub>2,3,-,2,-</sub> |  | 4.2<br><sub>3,1,-,2,-</sub> |  | 1.2<br><sub>0,3,-,1,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.4 | 0.8 | 11.2 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 31.8<br><sub>29,37,40,33,25</sub> | 17.7<br><sub>13,14,23,16,16</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>6,8,6,6,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>3,4,5,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.2 | 1.0 | 1.8 | 26.5 |
| Ayo Dosunmu | 98% | 30.3<br><sub>37,34,39,30,27</sub> | 17.8<br><sub>19,21,26,26,18</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>12,1,2,4,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>8,6,4,1,1</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.4 | 1.8 | 26.2 |
| Jonathan Kuminga | 98% | 28.2<br><sub>33,32,34,25,24</sub> | 14.4<br><sub>8,16,17,4,14</sub> | 14.5 · –<br><sub>o 46% · u 53%</sub> | 5.7<br><sub>10,8,8,0,8</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>3,5,4,0,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>2,4,1,0,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.6 | 1.6 | 22.7 |
| Rudy Gobert | 98% | 28.1<br><sub>31,33,25,31,23</sub> | 9.6<br><sub>10,8,8,10,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 11.0<br><sub>10,11,11,15,6</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,2,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.5 | 1.4 | 22.1 |
| LaMelo Ball | 98% | 28.0<br><sub>33,31,35,30,25</sub> | 21.8<br><sub>34,20,22,24,22</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>6,2,2,3,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>3,6,8,5,9</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>6,4,3,4,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.2 | 3.2 | 32.5 |
| Terrence Shannon Jr. | 98% | 21.3<br><sub>-,-,-,18,21</sub> | 11.8<br><sub>-,-,-,5,6</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>-,-,-,3,4</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.7 | 0.1 | 1.2 | 16.8 |
| Trey Lyles | 98% | 18.8<br><sub>21,20,29,21,15</sub> | 6.6<br><sub>12,5,5,9,2</sub> |  | 4.2<br><sub>4,2,13,6,0</sub> |  | 1.1<br><sub>0,0,2,2,0</sub> |  | 0.8<br><sub>2,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 12.0 |
| Jaylen Clark | 91% | 18.2<br><sub>21,25,21,19,19</sub> | 6.3<br><sub>4,10,8,3,7</sub> |  | 2.5<br><sub>2,4,3,2,6</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.2 | 0.5 | 10.0 |
| Bones Hyland | 98% | 16.1<br><sub>14,16,10,13,23</sub> | 10.7<br><sub>10,19,4,14,24</sub> |  | 1.9<br><sub>1,2,1,2,3</sub> |  | 3.2<br><sub>3,4,0,2,8</sub> |  | 1.6<br><sub>2,4,1,1,5</sub> |  | 0.8 | 0.3 | 1.2 | 15.7 |
| Joan Beringer | 97% | 15.7<br><sub>14,13,7,16,22</sub> | 7.5<br><sub>2,4,2,4,13</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>7,7,3,3,9</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.7 | 13.8 |
| Cody Williams | 58% | 6.7<br><sub>7,-,-,2,7</sub> | 0.3<br><sub>0,-,-,0,0</sub> |  | 1.2<br><sub>1,-,-,0,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 1.8 |
| Rocco Zikarsky | 48% | 6.6<br><sub>-,-,-,2,-</sub> | 2.5<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 5.0 |
| Zyon Pullin | 38% | 6.3<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.3 |
| Isaiah Evans | 52% | 6.2<br><sub>-,-,-,2,8</sub> | 6.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 8.1 |
| Johni Broome | 5% | 4.8 | 1.8 |  | 1.2 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.2 | 3.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-14/`._
