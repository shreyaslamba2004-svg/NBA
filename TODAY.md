# NBA model · Sun 15 Nov 2026 (US date)

Updated **Mon 16 Nov, 11:47 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-15/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaime Jaquez Jr. AST over 7.5 (8+) | ATL @ MIL | draftkings | 13.60 | 12.90 | 7.38 | 13.6% | 6.9% | 7.8% | +5.5% | +84.4% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ATL @ MIL | Mon 16 Nov 12:00 | 118.5–110.2 | ATL 72% | 1.38 / 3.60 | MIL +8.5 | 228.5 | MIL +8.5 covers 50%; o233.5 40% |
| OKC @ SAC | Mon 16 Nov 13:00 | 119.6–106.9 | OKC 82% | 1.22 / 5.45 | SAC +12.5 | 226.5 | SAC +11.5 covers 47%; o223.5 56% |

### ATL @ MIL
Out: Ousmane Dieng (MIL), Kam Jones (MIL), Pete Nance (MIL), Ryan Rollins (MIL), Cormac Ryan (MIL), Kingston Flemings (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Jock Landale (ATL), Asa Newell (ATL), Jalen Wilson (ATL)

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 100% | 35.6<br><sub>-,-,36,38,40</sub> | 22.0<br><sub>-,-,30,15,27</sub> | 22.5 · 21.5<br><sub>o 50% · u 50%</sub> | 9.6<br><sub>-,-,7,7,11</sub> | 9.5<br><sub>o 51% · u 49%</sub> | 7.9<br><sub>-,-,6,4,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 3.0 | 39.5 |
| Nickeil Alexander-Walker | 100% | 34.3<br><sub>32,33,31,34,41</sub> | 22.3<br><sub>26,28,20,20,16</sub> | 21.5 · 22.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>4,2,3,4,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,2,1,4,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.7<br><sub>6,4,2,4,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4 | 0.5 | 2.1 | 29.4 |
| Dyson Daniels | 100% | 32.8<br><sub>34,35,31,31,36</sub> | 11.2<br><sub>8,13,9,10,6</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 8.0<br><sub>16,9,10,6,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>8,12,7,8,4</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 33% · u 67%</sub> | 2.5 | 0.4 | 1.4 | 25.4 |
| Onyeka Okongwu | 100% | 32.4<br><sub>31,33,30,30,35</sub> | 15.5<br><sub>14,22,16,16,17</sub> | 13.5 · 13.5<br><sub>o 51% · u 49%</sub> | 8.0<br><sub>16,10,2,9,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>4,1,5,3,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.0 | 1.4 | 26.7 |
| CJ McCollum | 100% | 29.8<br><sub>25,23,21,24,32</sub> | 18.3<br><sub>15,4,9,21,20</sub> | 15.5 · 15.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>5,3,4,0,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.4<br><sub>5,4,3,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>2,0,1,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.6 | 2.1 | 26.1 |
| Aaron Wiggins | 98% | 25.7<br><sub>29,29,26,23,26</sub> | 13.2<br><sub>15,19,20,15,9</sub> | 12.5 · 12.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,4,4,3,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,3,6,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>3,3,5,4,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.4 | 1.1 | 19.2 |
| Luguentz Dort | 98% | 23.7<br><sub>31,32,20,18,20</sub> | 8.4<br><sub>6,25,3,4,10</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>3,7,2,3,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>3,4,1,2,2</sub> |  | 1.3<br><sub>2,5,1,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.3 | 0.7 | 13.1 |
| Corey Kispert | 52% | 11.6<br><sub>8,16,-,-,-</sub> | 6.1<br><sub>9,7,-,-,-</sub> |  | 1.5<br><sub>0,2,-,-,-</sub> |  | 1.0<br><sub>1,1,-,-,-</sub> |  | 0.8<br><sub>1,1,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 8.5 |
| Zuby Ejiofor | 63% | 11.4<br><sub>17,15,18,4,-</sub> | 3.8<br><sub>11,10,7,0,-</sub> |  | 2.7<br><sub>3,5,6,0,-</sub> |  | 1.1<br><sub>2,5,0,0,-</sub> |  | 0.3<br><sub>1,0,1,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.6 |
| RayJ Dennis | 52% | 9.7<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 6.1 |
| Dorian Finney-Smith | 26% | 6.9<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.5 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 100% | 34.0<br><sub>35,27,-,35,34</sub> | 22.5<br><sub>23,13,-,27,18</sub> | 22.5 · 22.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>5,1,-,2,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>10,2,-,7,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>1,1,-,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.3 | 2.8 | 32.9 |
| Kyle Kuzma | 100% | 30.1<br><sub>32,31,26,24,31</sub> | 14.1<br><sub>13,27,5,9,14</sub> | 12.5 · 11.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>4,4,5,1,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.4<br><sub>3,0,3,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,6,1,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.5 | 2.3 | 23.2 |
| Jaime Jaquez Jr. | 98% | 29.5<br><sub>28,23,25,30,28</sub> | 16.9<br><sub>14,4,16,25,22</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>3,2,5,5,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.8<br><sub>3,2,3,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>2,0,2,2,5</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 2.3 | 27.3 |
| Myles Turner | 100% | 28.8<br><sub>24,24,27,-,31</sub> | 11.2<br><sub>0,3,3,-,14</sub> | 10.5 · 9.5<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>7,5,3,-,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>0,7,2,-,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.6<br><sub>0,0,1,-,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 1.8 | 1.8 | 20.2 |
| Brayden Burries | 100% | 26.3<br><sub>38,29,26,23,19</sub> | 10.8<br><sub>21,13,3,8,3</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>11,8,3,5,4</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>6,4,3,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.3 | 1.6 | 19.8 |
| Nate Ament | 93% | 21.8<br><sub>15,23,22,22,22</sub> | 9.1<br><sub>7,12,10,2,9</sub> | 8.5 · 9.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>1,5,2,4,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>0,1,1,1,1</sub> |  | 1.0<br><sub>0,2,2,0,2</sub> |  | 0.7 | 0.4 | 1.2 | 13.6 |
| Jericho Sims | 100% | 20.5<br><sub>7,15,8,18,-</sub> | 4.5<br><sub>0,2,2,0,-</sub> |  | 5.6<br><sub>1,2,0,4,-</sub> |  | 1.9<br><sub>0,0,0,1,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.3 | 1.3 | 11.9 |
| AJ Green | 98% | 19.1<br><sub>24,18,8,8,8</sub> | 6.9<br><sub>12,5,0,3,0</sub> |  | 2.0<br><sub>1,1,0,1,0</sub> |  | 1.4<br><sub>0,1,0,1,2</sub> |  | 1.3<br><sub>4,1,0,1,0</sub> |  | 0.4 | 0.1 | 0.8 | 10.2 |
| Kel'el Ware | 96% | 18.1<br><sub>13,9,17,23,17</sub> | 8.5<br><sub>4,0,8,8,10</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>3,0,4,5,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>0,1,1,1,1</sub> |  | 0.7<br><sub>0,0,0,0,2</sub> |  | 0.5 | 1.0 | 1.5 | 16.0 |
| Gary Trent Jr. | 63% | 16.4<br><sub>-,-,6,4,16</sub> | 7.2<br><sub>-,-,5,6,1</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> |  | 0.9<br><sub>-,-,0,0,0</sub> |  | 1.2<br><sub>-,-,1,2,0</sub> |  | 0.6 | 0.1 | 0.7 | 9.1 |
| Caris LeVert | 8% | 15.9<br><sub>-,-,-,-,-</sub> | 6.0<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.4 | 1.1 | 9.9 |
| Kasparas Jakucionis | 72% | 15.3<br><sub>10,7,23,4,-</sub> | 5.5<br><sub>3,1,11,4,-</sub> |  | 2.0<br><sub>0,2,0,2,-</sub> |  | 2.7<br><sub>2,0,4,0,-</sub> |  | 0.5<br><sub>0,0,2,0,-</sub> |  | 0.5 | 0.1 | 1.3 | 10.2 |

</details>


### OKC @ SAC
Out: Precious Achiuwa (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.6–106.9 | OKC 82% | 1.22 / 5.45 | SAC +12.5 | 226.5 | SAC +11.5 covers 47%; o223.5 56% |
| Expected (weighted by chance each plays) | 120.0–107.3 | OKC 81% | 1.24 / 5.16 | SAC +12.5 | 227.5 | SAC +11.5 covers 46%; o223.5 58% |
| if Ajay Mitchell plays | 120.5–106.8 | OKC 83% | 1.20 / 6.02 | SAC +13.5 | 227.5 | SAC +11.5 covers 44%; o223.5 58% |
| if De'Andre Hunter plays | 119.4–107.3 | OKC 80% | 1.24 / 5.12 | SAC +12.5 | 226.5 | SAC +11.5 covers 48%; o223.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ajay Mitchell (OKC) | Questionable | 55% | 26.0 | 15.4 | 3.3 | 3.6 | 0.9 | 1.3 | 0.3 | 1.5 | 22.3 | full tables below |
| De'Andre Hunter (SAC) | Questionable | 55% | 33.9 | 15.0 | 5.0 | 1.8 | 2.1 | 0.8 | 0.2 | 1.9 | 21.8 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.4<br><sub>30,29,29,36,39</sub> | 35.7<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 2.6 | 46.2 |
| Jared McCain | 98% | 29.7<br><sub>29,23,31,31,31</sub> | 16.9<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 1.6 | 22.6 |
| Isaiah Hartenstein | 98% | 28.3<br><sub>26,18,24,34,30</sub> | 11.4<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.2<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.6 | 26.8 |
| Kenrich Williams | 98% | 27.3<br><sub>19,23,19,26,35</sub> | 10.8<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.0 | 18.5 |
| Alex Caruso | 98% | 25.0<br><sub>20,13,19,29,27</sub> | 10.2<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.1 |
| Aday Mara | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 10.0<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.4 | 18.2 |
| Bennett Stirtz | 98% | 19.7<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 11.0 |
| Josh Dix | 67% | 17.6<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 9.7 |
| Micah Peavy | 88% | 17.0<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.3 |
| Nique Clifford | 96% | 14.9<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.4<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.9 |
| Nikola Topic | 72% | 14.3<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.3 |
| Brooks Barnhizer | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 38.7<br><sub>42,33,39,40,35</sub> | 25.7<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.3 | 3.8 | 37.4 |
| Zach LaVine | 98% | 35.3<br><sub>35,35,25,33,36</sub> | 20.4<br><sub>21,14,15,31,12</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 2.6 | 26.8 |
| Domantas Sabonis | 98% | 34.7<br><sub>35,31,-,24,35</sub> | 15.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 13.1<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.4 | 2.9 | 35.0 |
| Keegan Murray | 98% | 34.3<br><sub>-,-,23,24,40</sub> | 14.1<br><sub>-,-,10,11,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>-,-,2,1,4</sub> |  | 1.9<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 1.1 | 1.4 | 21.4 |
| Leaky Black | 80% | 22.6<br><sub>22,40,20,18,12</sub> | 5.7<br><sub>3,12,6,0,0</sub> |  | 3.8<br><sub>6,3,5,3,0</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.9<br><sub>0,4,2,0,0</sub> |  | 1.0 | 0.5 | 0.8 | 11.0 |
| Dylan Cardwell | 98% | 19.7<br><sub>13,15,18,29,13</sub> | 5.6<br><sub>4,9,4,1,6</sub> |  | 7.1<br><sub>6,2,9,11,3</sub> |  | 1.6<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 14.3 |
| Malik Monk | 98% | 18.6<br><sub>24,18,21,3,18</sub> | 10.3<br><sub>13,12,9,1,7</sub> |  | 1.9<br><sub>2,0,2,0,4</sub> |  | 3.1<br><sub>3,7,3,0,3</sub> |  | 1.5<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.4 | 15.2 |
| Emanuel Sharp | 98% | 17.3<br><sub>10,31,12,19,7</sub> | 5.1<br><sub>3,9,5,2,4</sub> |  | 1.6<br><sub>1,5,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.7<br><sub>1,3,1,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.5 |
| Alex Karaban | 48% | 13.5<br><sub>-,11,-,-,-</sub> | 4.5<br><sub>-,0,-,-,-</sub> |  | 2.0<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 7.2 |
| Daeqwon Plowden | 83% | 12.4<br><sub>-,-,12,2,2</sub> | 4.4<br><sub>-,-,6,0,0</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,2,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Mason Plumlee | 30% | 11.5<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.5 | 0.7 | 7.3 |

</details>

<details><summary>if De'Andre Hunter plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.7<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 2.6 | 46.2 |
| Jared McCain (OKC) | 98% | 29.6<br><sub>29,23,31,31,31</sub> | 16.8<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.6 | 22.6 |
| Isaiah Hartenstein (OKC) | 98% | 28.4<br><sub>26,18,24,34,30</sub> | 11.5<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.2<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.8 |
| Kenrich Williams (OKC) | 98% | 27.3<br><sub>19,23,19,26,35</sub> | 10.8<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.0 | 18.5 |
| Alex Caruso (OKC) | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.3<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara (OKC) | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 10.0<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.6 | 1.8 | 1.5 | 18.2 |
| Bennett Stirtz (OKC) | 98% | 19.7<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix (OKC) | 67% | 17.6<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 1.0<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 9.8 |
| Micah Peavy (OKC) | 88% | 16.9<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.7<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford (OKC) | 96% | 15.0<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 9.0 |
| Nikola Topic (OKC) | 72% | 14.2<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.2 |
| Brooks Barnhizer (OKC) | 52% | 8.8<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 4.8 |
| Darius Acuff Jr. (SAC) | 98% | 36.9<br><sub>42,33,39,40,35</sub> | 22.2<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.3 | 3.7 | 33.5 |
| De'Andre Hunter (SAC) | 100% | 33.9<br><sub>38,-,31,34,42</sub> | 15.0<br><sub>14,-,14,15,24</sub> | 12.5 · – | 5.0<br><sub>2,-,3,4,5</sub> | 3.5 | 1.8<br><sub>2,-,1,2,2</sub> | 1.5 | 2.1<br><sub>1,-,2,3,2</sub> | 1.5 | 0.8 | 0.2 | 1.9 | 21.8 |
| Zach LaVine (SAC) | 98% | 33.2<br><sub>35,35,25,33,36</sub> | 19.1<br><sub>21,14,15,31,12</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 2.4 | 25.2 |
| Domantas Sabonis (SAC) | 98% | 32.7<br><sub>35,31,-,24,35</sub> | 14.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 12.3<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.8 | 32.9 |
| Keegan Murray (SAC) | 98% | 31.1<br><sub>-,-,23,24,40</sub> | 12.2<br><sub>-,-,10,11,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>-,-,2,1,4</sub> |  | 1.7<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 1.1 | 1.2 | 18.9 |
| Leaky Black (SAC) | 80% | 17.4<br><sub>22,40,20,18,12</sub> | 4.4<br><sub>3,12,6,0,0</sub> |  | 2.8<br><sub>6,3,5,3,0</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.6<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.3 |
| Dylan Cardwell (SAC) | 98% | 17.3<br><sub>13,15,18,29,13</sub> | 5.0<br><sub>4,9,4,1,6</sub> |  | 6.2<br><sub>6,2,9,11,3</sub> |  | 1.4<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 12.6 |
| Malik Monk (SAC) | 98% | 16.5<br><sub>24,18,21,3,18</sub> | 8.8<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.1<br><sub>3,2,0,0,0</sub> |  | 0.4 | 0.3 | 1.3 | 13.1 |
| Emanuel Sharp (SAC) | 98% | 13.5<br><sub>10,31,12,19,7</sub> | 4.0<br><sub>3,9,5,2,4</sub> |  | 1.2<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.8 |
| Daeqwon Plowden (SAC) | 83% | 9.0<br><sub>-,-,12,2,2</sub> | 3.2<br><sub>-,-,6,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.3<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.6 |
| Alex Karaban (SAC) | 48% | 8.4<br><sub>-,11,-,-,-</sub> | 2.7<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.4 |
| Mason Plumlee (SAC) | 30% | 7.6<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>if Ajay Mitchell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 32.2<br><sub>30,29,29,36,39</sub> | 31.3<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.9<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 2.4 | 41.0 |
| Jared McCain (OKC) | 98% | 26.2<br><sub>29,23,31,31,31</sub> | 15.0<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.1 | 1.4 | 20.2 |
| Ajay Mitchell (OKC) | 100% | 26.0<br><sub>30,22,28,-,-</sub> | 15.4<br><sub>35,12,14,-,-</sub> | 17.5 · – | 3.3<br><sub>1,4,3,-,-</sub> | 3.5 | 3.6<br><sub>5,0,3,-,-</sub> | 3.5 | 0.9<br><sub>4,0,0,-,-</sub> | 1.5 | 1.3 | 0.3 | 1.5 | 22.3 |
| Isaiah Hartenstein (OKC) | 98% | 25.4<br><sub>26,18,24,34,30</sub> | 10.1<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 10.0<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.5 | 23.8 |
| Kenrich Williams (OKC) | 98% | 22.5<br><sub>19,23,19,26,35</sub> | 9.0<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 0.8 | 15.2 |
| Alex Caruso (OKC) | 98% | 21.7<br><sub>20,13,19,29,27</sub> | 8.9<br><sub>5,0,5,14,5</sub> |  | 3.2<br><sub>6,3,2,7,1</sub> |  | 2.6<br><sub>2,3,1,2,4</sub> |  | 1.3<br><sub>1,0,1,4,1</sub> |  | 1.4 | 0.5 | 0.9 | 14.7 |
| Aday Mara (OKC) | 98% | 21.6<br><sub>18,27,26,32,21</sub> | 8.8<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.6 | 1.3 | 16.1 |
| Bennett Stirtz (OKC) | 98% | 16.3<br><sub>24,29,18,25,12</sub> | 6.6<br><sub>12,11,13,6,5</sub> |  | 1.3<br><sub>1,5,1,1,1</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.0<br><sub>2,2,2,2,1</sub> |  | 0.6 | 0.1 | 0.5 | 9.0 |
| Josh Dix (OKC) | 67% | 15.3<br><sub>15,21,-,-,17</sub> | 5.7<br><sub>5,2,-,-,0</sub> |  | 1.9<br><sub>2,1,-,-,4</sub> |  | 0.8<br><sub>1,2,-,-,3</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.3 |
| Nique Clifford (OKC) | 96% | 13.2<br><sub>-,-,20,16,12</sub> | 4.9<br><sub>-,-,4,5,0</sub> |  | 2.0<br><sub>-,-,4,3,0</sub> |  | 1.3<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.2 |
| Micah Peavy (OKC) | 88% | 13.2<br><sub>18,23,21,12,-</sub> | 3.7<br><sub>7,7,0,0,-</sub> |  | 2.3<br><sub>4,3,2,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.3<br><sub>1,1,0,0,-</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Nikola Topic (OKC) | 72% | 11.6<br><sub>-,-,-,-,16</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 2.7<br><sub>-,-,-,-,3</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.1 | 1.1 | 7.7 |
| Brooks Barnhizer (OKC) | 52% | 7.0<br><sub>5,8,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 1.5<br><sub>0,4,1,-,-</sub> |  | 0.6<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Darius Acuff Jr. (SAC) | 98% | 38.6<br><sub>42,33,39,40,35</sub> | 25.6<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.3 | 3.8 | 37.3 |
| Zach LaVine (SAC) | 98% | 35.3<br><sub>35,35,25,33,36</sub> | 20.3<br><sub>21,14,15,31,12</sub> | 18.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 2.6 | 26.8 |
| Domantas Sabonis (SAC) | 98% | 34.7<br><sub>35,31,-,24,35</sub> | 15.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 13.1<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.6<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.3 | 2.9 | 35.0 |
| Keegan Murray (SAC) | 98% | 34.3<br><sub>-,-,23,24,40</sub> | 14.1<br><sub>-,-,10,11,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>-,-,2,1,4</sub> |  | 1.9<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 1.1 | 1.4 | 21.5 |
| Leaky Black (SAC) | 80% | 22.6<br><sub>22,40,20,18,12</sub> | 5.7<br><sub>3,12,6,0,0</sub> |  | 3.8<br><sub>6,3,5,3,0</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.9<br><sub>0,4,2,0,0</sub> |  | 1.0 | 0.5 | 0.8 | 10.9 |
| Dylan Cardwell (SAC) | 98% | 19.7<br><sub>13,15,18,29,13</sub> | 5.6<br><sub>4,9,4,1,6</sub> |  | 7.1<br><sub>6,2,9,11,3</sub> |  | 1.6<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.1 | 14.2 |
| Malik Monk (SAC) | 98% | 18.6<br><sub>24,18,21,3,18</sub> | 10.3<br><sub>13,12,9,1,7</sub> |  | 1.9<br><sub>2,0,2,0,4</sub> |  | 3.1<br><sub>3,7,3,0,3</sub> |  | 1.5<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.4 | 15.3 |
| Emanuel Sharp (SAC) | 98% | 17.2<br><sub>10,31,12,19,7</sub> | 5.2<br><sub>3,9,5,2,4</sub> |  | 1.5<br><sub>1,5,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.7<br><sub>1,3,1,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.5 |
| Alex Karaban (SAC) | 48% | 13.4<br><sub>-,11,-,-,-</sub> | 4.4<br><sub>-,0,-,-,-</sub> |  | 2.0<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 7.2 |
| Daeqwon Plowden (SAC) | 83% | 12.4<br><sub>-,-,12,2,2</sub> | 4.4<br><sub>-,-,6,0,0</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,2,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Mason Plumlee (SAC) | 30% | 11.5<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.5 | 0.7 | 7.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-15/`._
