# NBA model · Fri 06 Nov 2026 (US date)

Updated **Sat 07 Nov, 01:57 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-06/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| UTA @ DAL | team points | DAL projected 126, market implies 117 | 38% of tonight's minutes go to players new to DAL since last season, and the team ratings still lean on last season; DAL out: Larrea, II | 37% of tonight's minutes go to players new to UTA since last season, and the team ratings still lean on last season; UTA out: Jr., Nurkic |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | SAS @ SAC | sportsbet | 8.75 | 7.82 | 5.03 | 19.9% | 12.8% | 12.8% | +11.9% | +74.1% | 0.4% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| WAS @ ATL | Sat 07 Nov 11:00 | 114.3–118.1 | WAS 39% | 2.54 / 1.65 | ATL -4.5 | 232.5 | ATL -7.5 covers 40%; o228.5 58% |
| BOS @ CHA | Sat 07 Nov 11:00 | 109.5–101.4 | BOS 72% | 1.40 / 3.52 | CHA +7.5 | 210.5 | CHA +8.5 covers 52%; o207.5 57% |
| PHI @ CLE | Sat 07 Nov 11:30 | 113.4–112.4 | PHI 53% | 1.90 / 2.11 | CLE +1.5 | 225.5 | CLE +2.5 covers 53%; o230.5 40% |
| UTA @ DAL | Sat 07 Nov 12:00 | 115.1–125.7 | UTA 23% | 4.40 / 1.29 | DAL -10.5 | 240.5 | DAL -7.5 covers 59%; o226.5 78% |
| OKC @ MEM | Sat 07 Nov 12:00 | 116.2–112.3 | OKC 61% | 1.64 / 2.56 | MEM +4.5 | 228.5 | MEM +3.5 covers 48%; o224.5 59% |
| TOR @ MIL | Sat 07 Nov 12:00 | 117.4–111.5 | TOR 66% | 1.51 / 2.96 | MIL +6.5 | 228.5 | MIL +6.5 covers 51%; o230.5 46% |
| MIN @ NOP | Sat 07 Nov 12:00 | 117.9–118.4 | MIN 49% | 2.05 / 1.95 | NOP +0.5 | 236.5 | NOP +4.5 covers 63%; o230.5 62% |
| POR @ LAL | Sat 07 Nov 14:00 | 110.7–115.4 | POR 37% | 2.73 / 1.58 | LAL -5.5 | 225.5 | LAL -2.5 covers 57%; o231.5 38% |
| SAS @ SAC | Sat 07 Nov 14:00 | 120.8–108.9 | SAS 80% | 1.25 / 5.03 | SAC +11.5 | 229.5 | SAC +15.5 covers 60%; o228.5 52% |

### WAS @ ATL
Out: Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Jock Landale (ATL), Asa Newell (ATL), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.3–118.1 | WAS 39% | 2.54 / 1.65 | ATL -4.5 | 232.5 | ATL -7.5 covers 40%; o228.5 58% |
| Expected (weighted by chance each plays) | 113.3–118.4 | WAS 36% | 2.80 / 1.55 | ATL -5.5 | 231.5 | ATL -7.5 covers 43%; o228.5 57% |
| if Anthony Davis plays | 112.6–117.0 | WAS 38% | 2.65 / 1.61 | ATL -4.5 | 229.5 | ATL -7.5 covers 42%; o228.5 52% |
| if Jalen Johnson plays | 113.5–119.5 | WAS 34% | 2.97 / 1.51 | ATL -6.5 | 232.5 | ATL -7.5 covers 46%; o228.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Questionable | 55% | 15.3 | 6.1 | 2.5 | 1.2 | 0.6 | 0.4 | 0.1 | 0.8 | 9.8 | small |
| RayJ Dennis (ATL) | Questionable | 55% | 12.1 | 4.2 | 1.7 | 2.0 | 0.5 | 0.4 | 0.3 | 0.8 | 8.0 | small |
| Anthony Davis (WAS) | Questionable | 55% | 33.7 | 22.2 | 11.6 | 2.6 | 0.7 | 1.2 | 1.9 | 2.2 | 36.4 | full tables below |
| Jalen Johnson (ATL) | Questionable | 55% | 33.0 | 21.0 | 9.8 | 7.3 | 1.6 | 1.3 | 0.6 | 3.1 | 38.0 | full tables below |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.1<br><sub>38,34,38,34,34</sub> | 22.2<br><sub>22,14,21,15,18</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>6,5,7,3,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 9.4<br><sub>10,8,9,9,6</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.2 | 4.2 | 35.0 |
| Kyshawn George | 98% | 34.0<br><sub>29,38,32,37,35</sub> | 18.4<br><sub>20,8,12,22,25</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>4,2,3,4,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,11,3,5,7</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>2,0,4,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 1.1 | 2.8 | 28.8 |
| AJ Dybantsa | 93% | 32.7<br><sub>-,27,30,33,32</sub> | 16.5<br><sub>-,19,17,21,9</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>-,2,8,5,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>-,2,1,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>-,1,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.4 | 2.0 | 24.9 |
| Bilal Coulibaly | 98% | 27.5<br><sub>29,27,22,33,23</sub> | 11.0<br><sub>3,17,1,7,6</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>5,2,5,1,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>1,0,1,2,2</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 1.2 | 0.9 | 1.4 | 17.0 |
| Alex Sarr | 97% | 26.6<br><sub>26,26,29,-,23</sub> | 12.9<br><sub>12,18,3,-,11</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 7.2<br><sub>6,4,8,-,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,2,0,-,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9<br><sub>0,2,1,-,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.9 | 1.6 | 1.7 | 22.6 |
| Bub Carrington | 98% | 23.2<br><sub>28,20,20,19,19</sub> | 8.5<br><sub>6,3,9,3,0</sub> |  | 2.6<br><sub>0,1,4,4,1</sub> |  | 3.1<br><sub>3,3,2,4,2</sub> |  | 1.1<br><sub>2,0,3,1,0</sub> |  | 0.6 | 0.2 | 1.8 | 14.2 |
| Tre Johnson | 86% | 20.4<br><sub>23,-,13,22,14</sub> | 8.1<br><sub>7,-,4,4,3</sub> |  | 2.5<br><sub>3,-,2,3,2</sub> |  | 1.0<br><sub>2,-,0,0,0</sub> |  | 1.0<br><sub>1,-,0,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 11.6 |
| Deandre Ayton | 98% | 17.6<br><sub>12,12,17,24,11</sub> | 6.5<br><sub>0,10,3,4,5</sub> |  | 5.8<br><sub>4,3,3,6,4</sub> |  | 0.8<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.9 | 13.1 |
| Khris Middleton | 58% | 15.3<br><sub>13,23,5,-,-</sub> | 5.2<br><sub>0,4,0,-,-</sub> |  | 2.5<br><sub>1,3,0,-,-</sub> |  | 1.1<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.5 | 0.1 | 1.1 | 8.9 |
| Will Riley | 83% | 13.8<br><sub>4,-,1,4,13</sub> | 6.1<br><sub>2,-,0,0,0</sub> |  | 1.9<br><sub>0,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,1,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 1.0 | 9.1 |
| Anthony Gill | 35% | 13.3<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.6 | 8.1 |
| Tre Mann | 52% | 8.0<br><sub>-,-,1,-,3</sub> | 3.2<br><sub>-,-,0,-,2</sub> |  | 1.1<br><sub>-,-,0,-,0</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 5.2 |
| Felix Okpara | 10% | 7.8<br><sub>-,-,-,-,3</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 2.0<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker | 98% | 33.2<br><sub>32,31,29,31,32</sub> | 24.1<br><sub>23,25,12,34,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>1,1,1,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.7<br><sub>5,4,0,9,6</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.5 | 2.7 | 31.9 |
| Dyson Daniels | 98% | 32.6<br><sub>28,32,27,31,34</sub> | 13.0<br><sub>7,4,8,6,8</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>4,6,4,9,16</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>7,5,3,4,8</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.5 | 0.5 | 2.0 | 26.6 |
| Onyeka Okongwu | 98% | 32.6<br><sub>31,33,28,33,31</sub> | 16.8<br><sub>11,29,6,13,14</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 9.0<br><sub>4,12,10,10,16</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,2,1,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,4,0,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.0 | 1.8 | 29.2 |
| Luguentz Dort | 98% | 31.8<br><sub>24,22,29,31,31</sub> | 11.3<br><sub>8,6,11,14,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,3,3,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>3,2,0,0,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7<br><sub>2,1,1,4,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 1.1 | 17.6 |
| CJ McCollum | 98% | 30.8<br><sub>20,31,24,32,25</sub> | 21.2<br><sub>13,5,14,13,15</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>2,3,2,9,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.0<br><sub>1,8,2,12,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>1,0,2,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.6 | 2.5 | 30.0 |
| Aaron Wiggins | 96% | 28.4<br><sub>24,24,23,24,29</sub> | 14.7<br><sub>10,20,10,7,15</sub> |  | 4.0<br><sub>4,7,2,3,4</sub> |  | 2.4<br><sub>3,3,1,2,2</sub> |  | 2.1<br><sub>2,4,2,1,3</sub> |  | 1.1 | 0.5 | 1.6 | 21.1 |
| Kingston Flemings | 80% | 25.2<br><sub>28,16,25,-,23</sub> | 10.3<br><sub>23,2,12,-,14</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>5,1,2,-,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>5,5,6,-,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>3,0,1,-,2</sub> |  | 0.9 | 0.4 | 1.9 | 19.7 |
| Zuby Ejiofor | 58% | 17.6<br><sub>-,-,-,15,17</sub> | 6.9<br><sub>-,-,-,3,11</sub> |  | 4.0<br><sub>-,-,-,5,3</sub> |  | 1.4<br><sub>-,-,-,2,2</sub> |  | 0.6<br><sub>-,-,-,1,1</sub> |  | 0.7 | 0.2 | 0.9 | 12.3 |
| Corey Kispert | 67% | 17.2<br><sub>-,-,5,18,8</sub> | 9.2<br><sub>-,-,0,14,9</sub> |  | 2.1<br><sub>-,-,0,1,0</sub> |  | 1.6<br><sub>-,-,1,0,1</sub> |  | 1.4<br><sub>-,-,0,4,1</sub> |  | 0.3 | 0.2 | 0.9 | 12.9 |
| Dorian Finney-Smith | 43% | 11.5<br><sub>-,-,3,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |

</details>

<details><summary>if Jalen Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 100% | 33.0<br><sub>36,34,28,-,-</sub> | 21.0<br><sub>12,17,13,-,-</sub> | 20.5 · – | 9.8<br><sub>9,8,7,-,-</sub> | 9.5 | 7.3<br><sub>11,7,4,-,-</sub> | 7.5 | 1.6<br><sub>2,2,1,-,-</sub> | 1.5 | 1.3 | 0.6 | 3.1 | 38.0 |
| Nickeil Alexander-Walker (ATL) | 98% | 31.8<br><sub>32,31,29,31,32</sub> | 21.4<br><sub>23,25,12,34,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>1,1,1,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.5<br><sub>5,4,0,9,6</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.5 | 2.2 | 28.2 |
| Dyson Daniels (ATL) | 98% | 30.9<br><sub>28,32,27,31,34</sub> | 11.5<br><sub>7,4,8,6,8</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 7.1<br><sub>4,6,4,9,16</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>7,5,3,4,8</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.3 | 0.5 | 1.6 | 24.3 |
| Onyeka Okongwu (ATL) | 98% | 30.7<br><sub>31,33,28,33,31</sub> | 14.7<br><sub>11,29,6,13,14</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 8.5<br><sub>4,12,10,10,16</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,2,1,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>1,4,0,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.0 | 1.5 | 26.2 |
| CJ McCollum (ATL) | 98% | 28.0<br><sub>20,31,24,32,25</sub> | 17.2<br><sub>13,5,14,13,15</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,3,2,9,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.3<br><sub>1,8,2,12,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,2,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.5 | 2.1 | 24.8 |
| Luguentz Dort (ATL) | 98% | 27.6<br><sub>24,22,29,31,31</sub> | 9.6<br><sub>8,6,11,14,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,3,3,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,2,0,0,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.5<br><sub>2,1,1,4,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.4 | 0.8 | 14.8 |
| Aaron Wiggins (ATL) | 96% | 25.6<br><sub>24,24,23,24,29</sub> | 12.5<br><sub>10,20,10,7,15</sub> |  | 3.6<br><sub>4,7,2,3,4</sub> |  | 2.1<br><sub>3,3,1,2,2</sub> |  | 1.9<br><sub>2,4,2,1,3</sub> |  | 1.0 | 0.5 | 1.3 | 18.2 |
| Kingston Flemings (ATL) | 80% | 21.9<br><sub>28,16,25,-,23</sub> | 8.3<br><sub>23,2,12,-,14</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,1,2,-,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,5,6,-,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>3,0,1,-,2</sub> |  | 0.8 | 0.3 | 1.6 | 15.9 |
| Zuby Ejiofor (ATL) | 58% | 14.4<br><sub>-,-,-,15,17</sub> | 5.4<br><sub>-,-,-,3,11</sub> |  | 3.2<br><sub>-,-,-,5,3</sub> |  | 1.1<br><sub>-,-,-,2,2</sub> |  | 0.5<br><sub>-,-,-,1,1</sub> |  | 0.5 | 0.2 | 0.8 | 9.7 |
| Corey Kispert (ATL) | 67% | 12.6<br><sub>-,-,5,18,8</sub> | 6.8<br><sub>-,-,0,14,9</sub> |  | 1.6<br><sub>-,-,0,1,0</sub> |  | 1.1<br><sub>-,-,1,0,1</sub> |  | 1.0<br><sub>-,-,0,4,1</sub> |  | 0.3 | 0.2 | 0.6 | 9.6 |
| Dorian Finney-Smith (ATL) | 43% | 6.8<br><sub>-,-,3,-,-</sub> | 1.9<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.4 |
| Trae Young (WAS) | 98% | 35.1<br><sub>38,34,38,34,34</sub> | 22.1<br><sub>22,14,21,15,18</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>6,5,7,3,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 9.4<br><sub>10,8,9,9,6</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.2 | 4.2 | 34.9 |
| Kyshawn George (WAS) | 98% | 34.0<br><sub>29,38,32,37,35</sub> | 18.3<br><sub>20,8,12,22,25</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>4,2,3,4,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>2,11,3,5,7</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>2,0,4,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 1.1 | 2.9 | 28.7 |
| AJ Dybantsa (WAS) | 93% | 32.6<br><sub>-,27,30,33,32</sub> | 16.4<br><sub>-,19,17,21,9</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>-,2,8,5,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>-,2,1,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>-,1,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.4 | 2.0 | 24.8 |
| Bilal Coulibaly (WAS) | 98% | 27.5<br><sub>29,27,22,33,23</sub> | 10.9<br><sub>3,17,1,7,6</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>5,2,5,1,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>1,0,1,2,2</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 1.2 | 0.9 | 1.4 | 17.0 |
| Alex Sarr (WAS) | 97% | 26.7<br><sub>26,26,29,-,23</sub> | 12.9<br><sub>12,18,3,-,11</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 7.3<br><sub>6,4,8,-,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,2,0,-,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>0,2,1,-,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.9 | 1.7 | 1.8 | 22.6 |
| Bub Carrington (WAS) | 98% | 23.1<br><sub>28,20,20,19,19</sub> | 8.5<br><sub>6,3,9,3,0</sub> |  | 2.6<br><sub>0,1,4,4,1</sub> |  | 3.1<br><sub>3,3,2,4,2</sub> |  | 1.1<br><sub>2,0,3,1,0</sub> |  | 0.6 | 0.2 | 1.8 | 14.2 |
| Tre Johnson (WAS) | 86% | 20.3<br><sub>23,-,13,22,14</sub> | 8.0<br><sub>7,-,4,4,3</sub> |  | 2.5<br><sub>3,-,2,3,2</sub> |  | 1.0<br><sub>2,-,0,0,0</sub> |  | 0.9<br><sub>1,-,0,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 11.5 |
| Deandre Ayton (WAS) | 98% | 17.5<br><sub>12,12,17,24,11</sub> | 6.4<br><sub>0,10,3,4,5</sub> |  | 5.8<br><sub>4,3,3,6,4</sub> |  | 0.8<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.9 | 13.0 |
| Khris Middleton (WAS) | 58% | 15.3<br><sub>13,23,5,-,-</sub> | 5.2<br><sub>0,4,0,-,-</sub> |  | 2.6<br><sub>1,3,0,-,-</sub> |  | 1.1<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.5 | 0.1 | 1.1 | 8.9 |
| Will Riley (WAS) | 83% | 13.7<br><sub>4,-,1,4,13</sub> | 6.0<br><sub>2,-,0,0,0</sub> |  | 1.9<br><sub>0,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,1,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 1.0 | 9.0 |
| Anthony Gill (WAS) | 35% | 13.2<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.6 | 8.1 |
| Tre Mann (WAS) | 52% | 7.9<br><sub>-,-,1,-,3</sub> | 3.2<br><sub>-,-,0,-,2</sub> |  | 1.1<br><sub>-,-,0,-,0</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 5.1 |
| Felix Okpara (WAS) | 10% | 7.7<br><sub>-,-,-,-,3</sub> | 2.9<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |

</details>

<details><summary>if Anthony Davis plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker (ATL) | 98% | 33.3<br><sub>32,31,29,31,32</sub> | 24.1<br><sub>23,25,12,34,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>1,1,1,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.7<br><sub>5,4,0,9,6</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.5 | 2.7 | 31.7 |
| Dyson Daniels (ATL) | 98% | 32.7<br><sub>28,32,27,31,34</sub> | 13.1<br><sub>7,4,8,6,8</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>4,6,4,9,16</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>7,5,3,4,8</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.5 | 0.5 | 2.0 | 26.7 |
| Onyeka Okongwu (ATL) | 98% | 32.6<br><sub>31,33,28,33,31</sub> | 16.7<br><sub>11,29,6,13,14</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 9.0<br><sub>4,12,10,10,16</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,2,1,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.7<br><sub>1,4,0,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.0 | 1.8 | 29.1 |
| Luguentz Dort (ATL) | 98% | 31.7<br><sub>24,22,29,31,31</sub> | 11.2<br><sub>8,6,11,14,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,3,3,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>3,2,0,0,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.7<br><sub>2,1,1,4,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.4 | 1.1 | 17.5 |
| CJ McCollum (ATL) | 98% | 30.7<br><sub>20,31,24,32,25</sub> | 21.1<br><sub>13,5,14,13,15</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>2,3,2,9,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.0<br><sub>1,8,2,12,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,0,2,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.6 | 2.6 | 29.9 |
| Aaron Wiggins (ATL) | 96% | 28.3<br><sub>24,24,23,24,29</sub> | 14.7<br><sub>10,20,10,7,15</sub> |  | 4.1<br><sub>4,7,2,3,4</sub> |  | 2.4<br><sub>3,3,1,2,2</sub> |  | 2.1<br><sub>2,4,2,1,3</sub> |  | 1.1 | 0.5 | 1.6 | 21.1 |
| Kingston Flemings (ATL) | 80% | 25.1<br><sub>28,16,25,-,23</sub> | 10.2<br><sub>23,2,12,-,14</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>5,1,2,-,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>5,5,6,-,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>3,0,1,-,2</sub> |  | 1.0 | 0.4 | 1.9 | 19.6 |
| Zuby Ejiofor (ATL) | 58% | 17.7<br><sub>-,-,-,15,17</sub> | 6.8<br><sub>-,-,-,3,11</sub> |  | 4.0<br><sub>-,-,-,5,3</sub> |  | 1.4<br><sub>-,-,-,2,2</sub> |  | 0.6<br><sub>-,-,-,1,1</sub> |  | 0.7 | 0.2 | 0.9 | 12.3 |
| Corey Kispert (ATL) | 67% | 17.1<br><sub>-,-,5,18,8</sub> | 9.2<br><sub>-,-,0,14,9</sub> |  | 2.1<br><sub>-,-,0,1,0</sub> |  | 1.6<br><sub>-,-,1,0,1</sub> |  | 1.4<br><sub>-,-,0,4,1</sub> |  | 0.4 | 0.2 | 0.9 | 12.9 |
| Dorian Finney-Smith (ATL) | 43% | 11.4<br><sub>-,-,3,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |
| Trae Young (WAS) | 98% | 34.2<br><sub>38,34,38,34,34</sub> | 19.2<br><sub>22,14,21,15,18</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>6,5,7,3,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 8.8<br><sub>10,8,9,9,6</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.2 | 3.8 | 31.3 |
| Anthony Davis (WAS) | 100% | 33.7<br><sub>36,34,34,34,30</sub> | 22.2<br><sub>29,18,25,27,26</sub> | 21.5 · – | 11.6<br><sub>10,5,13,9,10</sub> | 10.5 | 2.6<br><sub>0,3,1,1,3</sub> | 2.5 | 0.7<br><sub>3,2,0,1,0</sub> | 0.5 | 1.2 | 1.9 | 2.2 | 36.4 |
| Kyshawn George (WAS) | 98% | 32.5<br><sub>29,38,32,37,35</sub> | 15.8<br><sub>20,8,12,22,25</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>4,2,3,4,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,11,3,5,7</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>2,0,4,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 1.1 | 2.5 | 25.2 |
| AJ Dybantsa (WAS) | 93% | 30.6<br><sub>-,27,30,33,32</sub> | 14.5<br><sub>-,19,17,21,9</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>-,2,8,5,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>-,2,1,2,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>-,1,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.4 | 1.8 | 22.2 |
| Alex Sarr (WAS) | 97% | 25.0<br><sub>26,26,29,-,23</sub> | 11.5<br><sub>12,18,3,-,11</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>6,4,8,-,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>1,2,0,-,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9<br><sub>0,2,1,-,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.8 | 1.6 | 1.6 | 20.2 |
| Bilal Coulibaly (WAS) | 98% | 24.6<br><sub>29,27,22,33,23</sub> | 8.8<br><sub>3,17,1,7,6</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>5,2,5,1,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>1,0,1,2,2</sub> |  | 0.7<br><sub>0,1,0,0,0</sub> |  | 1.1 | 0.8 | 1.3 | 14.2 |
| Bub Carrington (WAS) | 98% | 18.6<br><sub>28,20,20,19,19</sub> | 5.8<br><sub>6,3,9,3,0</sub> |  | 2.1<br><sub>0,1,4,4,1</sub> |  | 2.5<br><sub>3,3,2,4,2</sub> |  | 0.8<br><sub>2,0,3,1,0</sub> |  | 0.5 | 0.2 | 1.5 | 10.4 |
| Tre Johnson (WAS) | 86% | 16.0<br><sub>23,-,13,22,14</sub> | 6.0<br><sub>7,-,4,4,3</sub> |  | 2.0<br><sub>3,-,2,3,2</sub> |  | 0.7<br><sub>2,-,0,0,0</sub> |  | 0.6<br><sub>1,-,0,0,1</sub> |  | 0.6 | 0.2 | 1.0 | 8.8 |
| Deandre Ayton (WAS) | 98% | 14.8<br><sub>12,12,17,24,11</sub> | 5.1<br><sub>0,10,3,4,5</sub> |  | 4.8<br><sub>4,3,3,6,4</sub> |  | 0.7<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.8 | 10.6 |
| Will Riley (WAS) | 83% | 11.0<br><sub>4,-,1,4,13</sub> | 4.5<br><sub>2,-,0,0,0</sub> |  | 1.4<br><sub>0,-,0,0,0</sub> |  | 0.8<br><sub>0,-,0,1,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.1 | 0.8 | 6.8 |
| Khris Middleton (WAS) | 58% | 9.5<br><sub>13,23,5,-,-</sub> | 2.9<br><sub>0,4,0,-,-</sub> |  | 1.6<br><sub>1,3,0,-,-</sub> |  | 0.8<br><sub>0,2,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 5.2 |
| Anthony Gill (WAS) | 35% | 7.4<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Tre Mann (WAS) | 52% | 5.9<br><sub>-,-,1,-,3</sub> | 2.5<br><sub>-,-,0,-,2</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.1 |
| Felix Okpara (WAS) | 10% | 5.6<br><sub>-,-,-,-,3</sub> | 2.3<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.0 |

</details>


### BOS @ CHA
Out: Christian Anderson (CHA), PJ Hall (CHA), Kon Knueppel (CHA), Grant Williams (CHA), Devin Carter (BOS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.5–101.4 | BOS 72% | 1.40 / 3.52 | CHA +7.5 | 210.5 | CHA +8.5 covers 52%; o207.5 57% |
| Expected (weighted by chance each plays) | 109.9–101.8 | BOS 71% | 1.40 / 3.47 | CHA +8.5 | 211.5 | CHA +8.5 covers 51%; o207.5 58% |
| if Moussa Diabate plays | 108.7–102.2 | BOS 68% | 1.47 / 3.14 | CHA +6.5 | 210.5 | CHA +8.5 covers 56%; o207.5 57% |
| if Payton Pritchard plays | 110.9–100.8 | BOS 77% | 1.31 / 4.27 | CHA +10.5 | 211.5 | CHA +8.5 covers 45%; o207.5 59% |
| if Dennis Schroder plays | 109.1–101.7 | BOS 70% | 1.42 / 3.36 | CHA +7.5 | 210.5 | CHA +8.5 covers 53%; o207.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Moussa Diabate (CHA) | Questionable | 55% | 30.7 | 8.3 | 9.4 | 2.5 | 0.0 | 0.9 | 0.8 | 1.4 | 20.1 | full tables below |
| Payton Pritchard (BOS) | Questionable | 55% | 26.0 | 12.4 | 3.0 | 3.5 | 1.8 | 0.7 | 0.1 | 1.0 | 18.9 | full tables below |
| Dennis Schroder (CHA) | Questionable | 55% | 30.7 | 12.4 | 3.4 | 5.1 | 1.3 | 0.8 | 0.2 | 2.2 | 21.0 | full tables below |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 36.1<br><sub>42,35,34,32,-</sub> | 27.4<br><sub>40,26,32,19,-</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>5,7,4,6,-</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>8,7,7,9,-</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,2,1,1,-</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.4 | 2.8 | 41.9 |
| Derrick White | 98% | 34.4<br><sub>33,26,34,30,36</sub> | 14.9<br><sub>16,9,12,7,24</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,2,2,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,4,2,3,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.8 | 1.7 | 24.0 |
| Paul George | 98% | 33.8<br><sub>36,27,33,-,35</sub> | 20.2<br><sub>20,18,17,-,25</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>7,6,6,-,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.8<br><sub>7,8,8,-,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,2,3,-,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.9 | 0.3 | 2.6 | 29.1 |
| Neemias Queta | 98% | 26.1<br><sub>15,20,27,26,29</sub> | 9.8<br><sub>7,13,8,16,9</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>3,6,8,6,12</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>2,0,1,1,3</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.8 | 1.3 | 1.1 | 18.7 |
| Baylor Scheierman | 98% | 25.0<br><sub>21,23,20,27,29</sub> | 7.4<br><sub>3,2,10,11,9</sub> |  | 4.5<br><sub>4,3,2,5,11</sub> |  | 1.8<br><sub>1,3,1,2,1</sub> |  | 1.2<br><sub>1,0,2,3,3</sub> |  | 0.9 | 0.1 | 0.7 | 13.7 |
| Sam Hauser | 98% | 24.6<br><sub>25,18,17,19,30</sub> | 8.4<br><sub>11,6,3,2,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>0,2,0,1,0</sub> |  | 1.6<br><sub>3,2,1,0,3</sub> |  | 0.5 | 0.2 | 0.4 | 12.9 |
| Mitchell Robinson | 98% | 19.2<br><sub>25,19,-,15,20</sub> | 5.3<br><sub>7,11,-,4,3</sub> |  | 5.7<br><sub>5,4,-,4,10</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.8 | 0.8 | 11.8 |
| Luka Garza | 98% | 15.9<br><sub>13,7,21,18,18</sub> | 7.8<br><sub>2,5,12,14,11</sub> |  | 3.5<br><sub>4,1,6,3,5</sub> |  | 1.1<br><sub>0,1,4,0,2</sub> |  | 0.8<br><sub>0,0,2,4,3</sub> |  | 0.4 | 0.3 | 0.7 | 12.3 |
| Jordan Walsh | 98% | 15.8<br><sub>24,11,13,12,12</sub> | 4.3<br><sub>15,2,0,5,3</sub> |  | 3.3<br><sub>6,2,3,3,4</sub> |  | 0.8<br><sub>1,0,2,0,0</sub> |  | 0.5<br><sub>3,0,0,1,1</sub> |  | 0.7 | 0.3 | 0.4 | 8.4 |
| Hugo Gonzalez | 96% | 15.0<br><sub>6,15,14,16,14</sub> | 4.2<br><sub>0,0,7,6,4</sub> |  | 2.9<br><sub>2,2,1,3,2</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.5 | 7.7 |
| Ron Harper Jr. | 52% | 8.6<br><sub>-,3,-,7,-</sub> | 3.3<br><sub>-,0,-,0,-</sub> |  | 1.3<br><sub>-,0,-,1,-</sub> |  | 0.5<br><sub>-,0,-,1,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.2 | 0.2 | 5.2 |
| Mike Conley | 48% | 8.5<br><sub>-,-,-,4,-</sub> | 2.6<br><sub>-,-,-,3,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.5 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 34.6<br><sub>38,37,33,31,26</sub> | 22.3<br><sub>31,19,24,17,10</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>12,7,5,1,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>3,2,5,4,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.3<br><sub>3,3,5,3,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.5 | 2.9 | 30.6 |
| Naz Reid | 98% | 34.4<br><sub>13,31,36,27,36</sub> | 18.8<br><sub>7,12,14,13,28</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 8.2<br><sub>6,11,5,6,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.6<br><sub>1,2,0,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.8 | 2.5 | 29.5 |
| Grayson Allen | 97% | 30.7<br><sub>30,21,30,19,27</sub> | 16.1<br><sub>9,5,27,11,22</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,3,4,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>2,2,3,0,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>2,1,7,3,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.4 | 1.9 | 22.9 |
| Sion James | 98% | 30.6<br><sub>23,29,18,21,31</sub> | 8.1<br><sub>5,6,4,11,10</sub> |  | 4.4<br><sub>2,5,2,4,2</sub> |  | 3.0<br><sub>3,4,1,3,1</sub> |  | 1.3<br><sub>1,1,0,3,0</sub> |  | 0.8 | 0.2 | 1.1 | 15.5 |
| Royce O'Neale | 98% | 25.9<br><sub>34,17,23,18,18</sub> | 7.3<br><sub>9,7,8,2,0</sub> |  | 4.3<br><sub>4,3,6,4,3</sub> |  | 1.6<br><sub>0,1,1,0,2</sub> |  | 1.5<br><sub>3,2,1,0,0</sub> |  | 0.7 | 0.4 | 0.8 | 13.2 |
| Coby White | 97% | 24.5<br><sub>-,-,-,16,18</sub> | 15.7<br><sub>-,-,-,7,4</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>-,-,-,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>-,-,-,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.1 | 2.0 | 22.5 |
| Ryan Kalkbrenner | 98% | 23.2<br><sub>13,15,19,16,19</sub> | 6.3<br><sub>1,2,6,4,6</sub> |  | 5.5<br><sub>1,4,3,6,4</sub> |  | 1.4<br><sub>1,0,4,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.4 | 0.9 | 13.2 |
| Tidjane Salaun | 91% | 19.5<br><sub>12,9,12,19,10</sub> | 6.4<br><sub>2,6,5,1,9</sub> |  | 4.4<br><sub>2,2,2,7,1</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>0,2,1,0,3</sub> |  | 0.4 | 0.2 | 0.7 | 11.8 |
| Liam McNeeley | 52% | 14.7<br><sub>-,3,-,9,-</sub> | 4.6<br><sub>-,0,-,3,-</sub> |  | 2.9<br><sub>-,2,-,0,-</sub> |  | 1.0<br><sub>-,0,-,1,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.6 | 8.4 |

</details>

<details><summary>if Payton Pritchard plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 34.0<br><sub>42,35,34,32,-</sub> | 24.9<br><sub>40,26,32,19,-</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>5,7,4,6,-</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>8,7,7,9,-</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>2,2,1,1,-</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.4 | 2.8 | 38.5 |
| Derrick White (BOS) | 98% | 31.4<br><sub>33,26,34,30,36</sub> | 12.8<br><sub>16,9,12,7,24</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,2,2,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>7,4,2,3,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.7 | 1.5 | 20.9 |
| Paul George (BOS) | 98% | 31.1<br><sub>36,27,33,-,35</sub> | 17.8<br><sub>20,18,17,-,25</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>7,6,6,-,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.4<br><sub>7,8,8,-,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,2,3,-,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.3 | 2.3 | 26.0 |
| Payton Pritchard (BOS) | 100% | 26.0<br><sub>24,35,27,30,18</sub> | 12.4<br><sub>4,30,7,4,10</sub> | 13.5 · – | 3.0<br><sub>2,3,7,3,1</sub> | 2.5 | 3.5<br><sub>6,3,3,3,5</sub> | 3.5 | 1.8<br><sub>0,3,0,0,0</sub> | 2.5 | 0.7 | 0.1 | 1.0 | 18.9 |
| Neemias Queta (BOS) | 98% | 23.7<br><sub>15,20,27,26,29</sub> | 8.9<br><sub>7,13,8,16,9</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>3,6,8,6,12</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,1,1,3</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.7 | 1.2 | 1.0 | 16.9 |
| Sam Hauser (BOS) | 98% | 22.1<br><sub>25,18,17,19,30</sub> | 7.6<br><sub>11,6,3,2,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.0<br><sub>0,2,0,1,0</sub> |  | 1.4<br><sub>3,2,1,0,3</sub> |  | 0.5 | 0.2 | 0.3 | 11.6 |
| Baylor Scheierman (BOS) | 98% | 21.8<br><sub>21,23,20,27,29</sub> | 6.4<br><sub>3,2,10,11,9</sub> |  | 4.0<br><sub>4,3,2,5,11</sub> |  | 1.4<br><sub>1,3,1,2,1</sub> |  | 1.0<br><sub>1,0,2,3,3</sub> |  | 0.8 | 0.1 | 0.6 | 11.9 |
| Mitchell Robinson (BOS) | 98% | 17.4<br><sub>25,19,-,15,20</sub> | 5.0<br><sub>7,11,-,4,3</sub> |  | 5.3<br><sub>5,4,-,4,10</sub> |  | 0.6<br><sub>0,0,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.8 | 0.8 | 10.9 |
| Luka Garza (BOS) | 98% | 14.5<br><sub>13,7,21,18,18</sub> | 7.2<br><sub>2,5,12,14,11</sub> |  | 3.2<br><sub>4,1,6,3,5</sub> |  | 0.9<br><sub>0,1,4,0,2</sub> |  | 0.7<br><sub>0,0,2,4,3</sub> |  | 0.4 | 0.3 | 0.6 | 11.4 |
| Jordan Walsh (BOS) | 98% | 13.4<br><sub>24,11,13,12,12</sub> | 3.7<br><sub>15,2,0,5,3</sub> |  | 2.8<br><sub>6,2,3,3,4</sub> |  | 0.7<br><sub>1,0,2,0,0</sub> |  | 0.4<br><sub>3,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.3 | 7.1 |
| Hugo Gonzalez (BOS) | 96% | 12.7<br><sub>6,15,14,16,14</sub> | 3.6<br><sub>0,0,7,6,4</sub> |  | 2.5<br><sub>2,2,1,3,2</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.6 |
| Mike Conley (BOS) | 48% | 6.9<br><sub>-,-,-,4,-</sub> | 2.2<br><sub>-,-,-,3,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,1,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.9 |
| Ron Harper Jr. (BOS) | 52% | 6.6<br><sub>-,3,-,7,-</sub> | 2.7<br><sub>-,0,-,0,-</sub> |  | 1.0<br><sub>-,0,-,1,-</sub> |  | 0.4<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.2 |
| Brandon Miller (CHA) | 98% | 34.6<br><sub>38,37,33,31,26</sub> | 22.3<br><sub>31,19,24,17,10</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>12,7,5,1,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>3,2,5,4,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.3<br><sub>3,3,5,3,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.6 | 2.9 | 30.7 |
| Naz Reid (CHA) | 98% | 34.4<br><sub>13,31,36,27,36</sub> | 18.6<br><sub>7,12,14,13,28</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 8.2<br><sub>6,11,5,6,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.6<br><sub>1,2,0,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.8 | 2.5 | 29.4 |
| Grayson Allen (CHA) | 97% | 30.7<br><sub>30,21,30,19,27</sub> | 16.1<br><sub>9,5,27,11,22</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,3,4,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>2,2,3,0,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>2,1,7,3,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.4 | 1.9 | 22.9 |
| Sion James (CHA) | 98% | 30.6<br><sub>23,29,18,21,31</sub> | 8.1<br><sub>5,6,4,11,10</sub> |  | 4.4<br><sub>2,5,2,4,2</sub> |  | 3.0<br><sub>3,4,1,3,1</sub> |  | 1.3<br><sub>1,1,0,3,0</sub> |  | 0.8 | 0.2 | 1.1 | 15.5 |
| Royce O'Neale (CHA) | 98% | 25.9<br><sub>34,17,23,18,18</sub> | 7.2<br><sub>9,7,8,2,0</sub> |  | 4.2<br><sub>4,3,6,4,3</sub> |  | 1.6<br><sub>0,1,1,0,2</sub> |  | 1.5<br><sub>3,2,1,0,0</sub> |  | 0.7 | 0.4 | 0.8 | 13.1 |
| Coby White (CHA) | 97% | 24.6<br><sub>-,-,-,16,18</sub> | 15.6<br><sub>-,-,-,7,4</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>-,-,-,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>-,-,-,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.1 | 2.0 | 22.4 |
| Ryan Kalkbrenner (CHA) | 98% | 23.2<br><sub>13,15,19,16,19</sub> | 6.2<br><sub>1,2,6,4,6</sub> |  | 5.5<br><sub>1,4,3,6,4</sub> |  | 1.4<br><sub>1,0,4,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.4 | 0.9 | 13.1 |
| Tidjane Salaun (CHA) | 91% | 19.5<br><sub>12,9,12,19,10</sub> | 6.4<br><sub>2,6,5,1,9</sub> |  | 4.4<br><sub>2,2,2,7,1</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>0,2,1,0,3</sub> |  | 0.4 | 0.2 | 0.7 | 11.8 |
| Liam McNeeley (CHA) | 52% | 14.8<br><sub>-,3,-,9,-</sub> | 4.6<br><sub>-,0,-,3,-</sub> |  | 2.9<br><sub>-,2,-,0,-</sub> |  | 0.9<br><sub>-,0,-,1,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.6 | 8.4 |

</details>

<details><summary>if Moussa Diabate plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 36.1<br><sub>42,35,34,32,-</sub> | 27.3<br><sub>40,26,32,19,-</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>5,7,4,6,-</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>8,7,7,9,-</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,2,1,1,-</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.4 | 2.9 | 41.8 |
| Derrick White (BOS) | 98% | 34.4<br><sub>33,26,34,30,36</sub> | 15.0<br><sub>16,9,12,7,24</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,2,2,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,4,2,3,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.8 | 1.7 | 24.0 |
| Paul George (BOS) | 98% | 33.7<br><sub>36,27,33,-,35</sub> | 20.2<br><sub>20,18,17,-,25</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>7,6,6,-,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.8<br><sub>7,8,8,-,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,2,3,-,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.9 | 0.3 | 2.6 | 29.0 |
| Neemias Queta (BOS) | 98% | 26.1<br><sub>15,20,27,26,29</sub> | 9.8<br><sub>7,13,8,16,9</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>3,6,8,6,12</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>2,0,1,1,3</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.8 | 1.3 | 1.2 | 18.6 |
| Baylor Scheierman (BOS) | 98% | 24.9<br><sub>21,23,20,27,29</sub> | 7.3<br><sub>3,2,10,11,9</sub> |  | 4.5<br><sub>4,3,2,5,11</sub> |  | 1.8<br><sub>1,3,1,2,1</sub> |  | 1.2<br><sub>1,0,2,3,3</sub> |  | 0.9 | 0.1 | 0.7 | 13.6 |
| Sam Hauser (BOS) | 98% | 24.6<br><sub>25,18,17,19,30</sub> | 8.3<br><sub>11,6,3,2,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>0,2,0,1,0</sub> |  | 1.6<br><sub>3,2,1,0,3</sub> |  | 0.5 | 0.2 | 0.4 | 12.8 |
| Mitchell Robinson (BOS) | 98% | 19.2<br><sub>25,19,-,15,20</sub> | 5.3<br><sub>7,11,-,4,3</sub> |  | 5.7<br><sub>5,4,-,4,10</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.8 | 0.8 | 11.8 |
| Luka Garza (BOS) | 98% | 15.9<br><sub>13,7,21,18,18</sub> | 7.7<br><sub>2,5,12,14,11</sub> |  | 3.5<br><sub>4,1,6,3,5</sub> |  | 1.1<br><sub>0,1,4,0,2</sub> |  | 0.8<br><sub>0,0,2,4,3</sub> |  | 0.4 | 0.3 | 0.7 | 12.3 |
| Jordan Walsh (BOS) | 98% | 15.9<br><sub>24,11,13,12,12</sub> | 4.4<br><sub>15,2,0,5,3</sub> |  | 3.3<br><sub>6,2,3,3,4</sub> |  | 0.8<br><sub>1,0,2,0,0</sub> |  | 0.5<br><sub>3,0,0,1,1</sub> |  | 0.7 | 0.3 | 0.4 | 8.5 |
| Hugo Gonzalez (BOS) | 96% | 15.1<br><sub>6,15,14,16,14</sub> | 4.2<br><sub>0,0,7,6,4</sub> |  | 3.0<br><sub>2,2,1,3,2</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.5 | 7.8 |
| Ron Harper Jr. (BOS) | 52% | 8.6<br><sub>-,3,-,7,-</sub> | 3.2<br><sub>-,0,-,0,-</sub> |  | 1.3<br><sub>-,0,-,1,-</sub> |  | 0.5<br><sub>-,0,-,1,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.2 | 0.3 | 5.1 |
| Mike Conley (BOS) | 48% | 8.5<br><sub>-,-,-,4,-</sub> | 2.6<br><sub>-,-,-,3,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.5 |
| Brandon Miller (CHA) | 98% | 34.6<br><sub>38,37,33,31,26</sub> | 22.7<br><sub>31,19,24,17,10</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>12,7,5,1,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>3,2,5,4,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.3<br><sub>3,3,5,3,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.6 | 2.7 | 31.0 |
| Naz Reid (CHA) | 98% | 33.1<br><sub>13,31,36,27,36</sub> | 17.2<br><sub>7,12,14,13,28</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>6,11,5,6,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.5<br><sub>1,2,0,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.8 | 2.4 | 27.7 |
| Moussa Diabate (CHA) | 100% | 30.7<br><sub>35,31,28,24,29</sub> | 8.3<br><sub>9,10,10,7,7</sub> | 7.5 · – | 9.4<br><sub>9,12,8,9,6</sub> | 8.5 | 2.5<br><sub>2,1,3,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.8 | 1.4 | 20.1 |
| Grayson Allen (CHA) | 97% | 29.7<br><sub>30,21,30,19,27</sub> | 14.9<br><sub>9,5,27,11,22</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,3,4,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,2,3,0,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>2,1,7,3,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.4 | 1.8 | 21.3 |
| Sion James (CHA) | 98% | 28.5<br><sub>23,29,18,21,31</sub> | 7.9<br><sub>5,6,4,11,10</sub> |  | 4.2<br><sub>2,5,2,4,2</sub> |  | 2.8<br><sub>3,4,1,3,1</sub> |  | 1.2<br><sub>1,1,0,3,0</sub> |  | 0.8 | 0.2 | 1.0 | 14.9 |
| Royce O'Neale (CHA) | 98% | 22.7<br><sub>34,17,23,18,18</sub> | 6.6<br><sub>9,7,8,2,0</sub> |  | 3.8<br><sub>4,3,6,4,3</sub> |  | 1.4<br><sub>0,1,1,0,2</sub> |  | 1.3<br><sub>3,2,1,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 11.8 |
| Coby White (CHA) | 97% | 21.5<br><sub>-,-,-,16,18</sub> | 13.6<br><sub>-,-,-,7,4</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>-,-,-,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>-,-,-,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.5 | 0.1 | 1.8 | 19.5 |
| Ryan Kalkbrenner (CHA) | 98% | 20.1<br><sub>13,15,19,16,19</sub> | 5.5<br><sub>1,2,6,4,6</sub> |  | 4.8<br><sub>1,4,3,6,4</sub> |  | 1.2<br><sub>1,0,4,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.2 | 0.8 | 11.5 |
| Tidjane Salaun (CHA) | 91% | 15.9<br><sub>12,9,12,19,10</sub> | 5.4<br><sub>2,6,5,1,9</sub> |  | 3.8<br><sub>2,2,2,7,1</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.7<br><sub>0,2,1,0,3</sub> |  | 0.4 | 0.2 | 0.6 | 9.9 |
| Liam McNeeley (CHA) | 52% | 11.4<br><sub>-,3,-,9,-</sub> | 3.7<br><sub>-,0,-,3,-</sub> |  | 2.2<br><sub>-,2,-,0,-</sub> |  | 0.7<br><sub>-,0,-,1,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.7 |

</details>

<details><summary>if Dennis Schroder plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 36.1<br><sub>42,35,34,32,-</sub> | 27.4<br><sub>40,26,32,19,-</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>5,7,4,6,-</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>8,7,7,9,-</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,2,1,1,-</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.4 | 2.9 | 41.9 |
| Derrick White (BOS) | 98% | 34.4<br><sub>33,26,34,30,36</sub> | 15.0<br><sub>16,9,12,7,24</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,2,2,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,4,2,3,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.8 | 1.7 | 24.1 |
| Paul George (BOS) | 98% | 33.8<br><sub>36,27,33,-,35</sub> | 20.2<br><sub>20,18,17,-,25</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>7,6,6,-,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.8<br><sub>7,8,8,-,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,2,3,-,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.9 | 0.3 | 2.5 | 28.9 |
| Neemias Queta (BOS) | 98% | 26.2<br><sub>15,20,27,26,29</sub> | 9.8<br><sub>7,13,8,16,9</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>3,6,8,6,12</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>2,0,1,1,3</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.8 | 1.3 | 1.2 | 18.6 |
| Baylor Scheierman (BOS) | 98% | 25.0<br><sub>21,23,20,27,29</sub> | 7.4<br><sub>3,2,10,11,9</sub> |  | 4.5<br><sub>4,3,2,5,11</sub> |  | 1.8<br><sub>1,3,1,2,1</sub> |  | 1.2<br><sub>1,0,2,3,3</sub> |  | 0.9 | 0.1 | 0.7 | 13.6 |
| Sam Hauser (BOS) | 98% | 24.6<br><sub>25,18,17,19,30</sub> | 8.4<br><sub>11,6,3,2,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>0,2,0,1,0</sub> |  | 1.6<br><sub>3,2,1,0,3</sub> |  | 0.5 | 0.2 | 0.4 | 12.9 |
| Mitchell Robinson (BOS) | 98% | 19.3<br><sub>25,19,-,15,20</sub> | 5.3<br><sub>7,11,-,4,3</sub> |  | 5.7<br><sub>5,4,-,4,10</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.8 | 0.9 | 11.9 |
| Luka Garza (BOS) | 98% | 15.8<br><sub>13,7,21,18,18</sub> | 7.7<br><sub>2,5,12,14,11</sub> |  | 3.4<br><sub>4,1,6,3,5</sub> |  | 1.1<br><sub>0,1,4,0,2</sub> |  | 0.8<br><sub>0,0,2,4,3</sub> |  | 0.4 | 0.3 | 0.7 | 12.2 |
| Jordan Walsh (BOS) | 98% | 15.8<br><sub>24,11,13,12,12</sub> | 4.3<br><sub>15,2,0,5,3</sub> |  | 3.3<br><sub>6,2,3,3,4</sub> |  | 0.8<br><sub>1,0,2,0,0</sub> |  | 0.5<br><sub>3,0,0,1,1</sub> |  | 0.7 | 0.3 | 0.4 | 8.4 |
| Hugo Gonzalez (BOS) | 96% | 15.2<br><sub>6,15,14,16,14</sub> | 4.2<br><sub>0,0,7,6,4</sub> |  | 3.0<br><sub>2,2,1,3,2</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.5 | 7.8 |
| Ron Harper Jr. (BOS) | 52% | 8.7<br><sub>-,3,-,7,-</sub> | 3.3<br><sub>-,0,-,0,-</sub> |  | 1.3<br><sub>-,0,-,1,-</sub> |  | 0.5<br><sub>-,0,-,1,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.2 | 0.3 | 5.2 |
| Mike Conley (BOS) | 48% | 8.4<br><sub>-,-,-,4,-</sub> | 2.6<br><sub>-,-,-,3,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,1,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.5 |
| Brandon Miller (CHA) | 98% | 34.1<br><sub>38,37,33,31,26</sub> | 20.4<br><sub>31,19,24,17,10</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>12,7,5,1,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>3,2,5,4,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.1<br><sub>3,3,5,3,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.6 | 2.5 | 28.5 |
| Naz Reid (CHA) | 98% | 33.0<br><sub>13,31,36,27,36</sub> | 16.5<br><sub>7,12,14,13,28</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>6,11,5,6,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.4<br><sub>1,2,0,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.8 | 2.3 | 26.6 |
| Dennis Schroder (CHA) | 100% | 30.7<br><sub>34,29,35,23,20</sub> | 12.4<br><sub>14,8,4,5,5</sub> |  | 3.4<br><sub>4,2,3,2,5</sub> |  | 5.1<br><sub>5,8,7,1,4</sub> |  | 1.3<br><sub>2,1,0,0,1</sub> |  | 0.8 | 0.2 | 2.2 | 21.0 |
| Grayson Allen (CHA) | 97% | 29.4<br><sub>30,21,30,19,27</sub> | 14.6<br><sub>9,5,27,11,22</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>5,3,4,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>2,2,3,0,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,1,7,3,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.3 | 1.7 | 20.6 |
| Sion James (CHA) | 98% | 28.0<br><sub>23,29,18,21,31</sub> | 7.3<br><sub>5,6,4,11,10</sub> |  | 4.2<br><sub>2,5,2,4,2</sub> |  | 2.5<br><sub>3,4,1,3,1</sub> |  | 1.1<br><sub>1,1,0,3,0</sub> |  | 0.8 | 0.1 | 0.8 | 13.9 |
| Royce O'Neale (CHA) | 98% | 22.6<br><sub>34,17,23,18,18</sub> | 6.4<br><sub>9,7,8,2,0</sub> |  | 3.9<br><sub>4,3,6,4,3</sub> |  | 1.3<br><sub>0,1,1,0,2</sub> |  | 1.2<br><sub>3,2,1,0,0</sub> |  | 0.7 | 0.3 | 0.6 | 11.6 |
| Coby White (CHA) | 97% | 21.3<br><sub>-,-,-,16,18</sub> | 13.4<br><sub>-,-,-,7,4</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>-,-,-,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.7<br><sub>-,-,-,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.5 | 0.1 | 1.7 | 19.0 |
| Ryan Kalkbrenner (CHA) | 98% | 19.9<br><sub>13,15,19,16,19</sub> | 5.2<br><sub>1,2,6,4,6</sub> |  | 4.8<br><sub>1,4,3,6,4</sub> |  | 1.1<br><sub>1,0,4,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.2 | 0.7 | 11.1 |
| Tidjane Salaun (CHA) | 91% | 16.2<br><sub>12,9,12,19,10</sub> | 5.6<br><sub>2,6,5,1,9</sub> |  | 3.9<br><sub>2,2,2,7,1</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.8<br><sub>0,2,1,0,3</sub> |  | 0.4 | 0.2 | 0.6 | 10.1 |
| Liam McNeeley (CHA) | 52% | 10.8<br><sub>-,3,-,9,-</sub> | 3.4<br><sub>-,0,-,3,-</sub> |  | 2.1<br><sub>-,2,-,0,-</sub> |  | 0.6<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 6.1 |

</details>


### PHI @ CLE
Out: Jaylon Tyson (CLE), Dominick Barlow (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.4–112.4 | PHI 53% | 1.90 / 2.11 | CLE +1.5 | 225.5 | CLE +2.5 covers 53%; o230.5 40% |
| Expected (weighted by chance each plays) | 112.7–113.6 | PHI 47% | 2.12 / 1.89 | CLE -1.5 | 226.5 | CLE +2.5 covers 59%; o230.5 42% |
| if Jarrett Allen plays | 112.9–112.8 | PHI 50% | 2.00 / 2.00 | CLE +0.5 | 225.5 | CLE +2.5 covers 56%; o230.5 39% |
| if Peyton Watson plays | 113.2–112.7 | PHI 51% | 1.95 / 2.05 | CLE +0.5 | 225.5 | CLE +2.5 covers 55%; o230.5 40% |
| if Tyrese Proctor plays | 113.6–112.3 | PHI 53% | 1.87 / 2.15 | CLE +1.5 | 225.5 | CLE +2.5 covers 53%; o230.5 40% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jarrett Allen (CLE) | Questionable | 55% | 27.3 | 13.2 | 8.4 | 1.5 | 0.1 | 0.8 | 1.4 | 1.3 | 23.1 | full tables below |
| Adem Bona (PHI) | Doubtful | 20% | 12.3 | 3.0 | 3.3 | 0.5 | 0.0 | 0.4 | 0.6 | 0.7 | 6.8 | small |
| Peyton Watson (CLE) | Questionable | 55% | 30.0 | 13.3 | 4.8 | 2.4 | 1.3 | 0.9 | 1.5 | 1.9 | 20.6 | full tables below |
| Tyrese Proctor (CLE) | Questionable | 55% | 23.6 | 9.5 | 3.4 | 2.8 | 1.4 | 0.9 | 0.1 | 1.1 | 15.7 | full tables below |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.0<br><sub>36,38,38,36,34</sub> | 22.8<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.5 | 2.2 | 32.0 |
| Jaylen Brown | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.7<br><sub>20,-,16,25,30</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.4 | 2.8 | 32.0 |
| LeBron James | 98% | 35.2<br><sub>33,34,-,31,33</sub> | 17.9<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.5 | 2.6 | 31.6 |
| VJ Edgecombe | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.4<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 1.3 | 21.5 |
| Joel Embiid | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.4<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 9.1<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.0 | 2.9 | 34.8 |
| Dean Wade | 91% | 22.2<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.2<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.5 | 8.1 |
| Anfernee Simons | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.5 | 0.1 | 0.7 | 11.5 |
| Kentavious Caldwell-Pope | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.5 |
| Tacko Fall | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Jabari Walker | 67% | 7.8<br><sub>-,-,19,2,-</sub> | 3.1<br><sub>-,-,12,0,-</sub> |  | 1.9<br><sub>-,-,6,0,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.4 |
| Caleb Love | 35% | 6.8<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.2 | 1.0 |
| Justin Edwards | 52% | 6.7<br><sub>-,-,2,2,-</sub> | 2.8<br><sub>-,-,0,2,-</sub> |  | 0.9<br><sub>-,-,1,1,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.1 |
| Rayan Rupert | 43% | 6.7<br><sub>-,-,-,2,-</sub> | 2.4<br><sub>-,-,-,2,-</sub> |  | 1.2<br><sub>-,-,-,2,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.1 |
| Labaron Philon Jr. | 58% | 6.5<br><sub>-,6,10,2,-</sub> | 2.6<br><sub>-,2,5,0,-</sub> |  | 1.0<br><sub>-,2,1,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.9<br><sub>34,36,26,33,35</sub> | 21.8<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.9<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 4.0 | 34.0 |
| Donovan Mitchell | 98% | 36.9<br><sub>31,33,24,36,33</sub> | 28.5<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.3<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 3.3 | 39.1 |
| Evan Mobley | 98% | 35.8<br><sub>32,33,25,33,33</sub> | 20.1<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 9.7<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 53%</sub> | 4.0<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.8 | 2.1 | 33.8 |
| Sam Merrill | 98% | 29.7<br><sub>20,27,19,26,27</sub> | 11.8<br><sub>8,16,6,8,10</sub> |  | 3.3<br><sub>1,2,4,3,7</sub> |  | 2.3<br><sub>1,3,3,2,1</sub> |  | 2.2<br><sub>2,4,1,2,2</sub> |  | 0.7 | 0.2 | 0.9 | 17.4 |
| Meleek Thomas | 84% | 27.3<br><sub>20,-,23,26,18</sub> | 12.1<br><sub>10,-,13,17,9</sub> |  | 3.4<br><sub>4,-,1,5,1</sub> |  | 1.3<br><sub>1,-,2,1,0</sub> |  | 2.0<br><sub>0,-,3,3,3</sub> |  | 1.0 | 0.3 | 1.4 | 16.8 |
| Mario Hezonja | 97% | 26.0<br><sub>17,17,20,27,23</sub> | 10.0<br><sub>5,10,8,12,12</sub> |  | 6.4<br><sub>3,6,11,8,8</sub> |  | 2.1<br><sub>2,2,4,3,1</sub> |  | 1.4<br><sub>1,2,1,3,2</sub> |  | 0.7 | 0.3 | 1.1 | 18.5 |
| Craig Porter Jr. | 80% | 17.4<br><sub>-,4,16,8,14</sub> | 3.8<br><sub>-,0,2,0,0</sub> |  | 3.4<br><sub>-,1,2,4,1</sub> |  | 2.5<br><sub>-,0,4,1,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.5 | 0.9 | 9.7 |
| Tristan Enaruna | 52% | 16.8<br><sub>-,-,6,-,16</sub> | 5.8<br><sub>-,-,2,-,4</sub> |  | 3.0<br><sub>-,-,1,-,4</sub> |  | 1.0<br><sub>-,-,0,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.2 | 0.7 | 9.8 |
| Thomas Bryant | 58% | 16.4<br><sub>-,-,11,5,13</sub> | 7.5<br><sub>-,-,11,4,8</sub> |  | 4.2<br><sub>-,-,2,0,0</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,3,0,1</sub> |  | 0.4 | 0.6 | 0.7 | 12.3 |
| Norchad Omier | 16% | 12.8 | 3.8 |  | 3.0 |  | 0.9 |  | 0.3 |  | 0.4 | 0.2 | 0.8 | 7.7 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Jarrett Allen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 98% | 36.9<br><sub>34,36,26,33,35</sub> | 19.6<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 7.1<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 3.9 | 31.9 |
| Donovan Mitchell (CLE) | 98% | 36.9<br><sub>31,33,24,36,33</sub> | 25.9<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.5<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.4 | 3.3 | 36.7 |
| Evan Mobley (CLE) | 98% | 35.4<br><sub>32,33,25,33,33</sub> | 18.4<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 9.6<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 53%</sub> | 4.0<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.9 | 2.0 | 32.0 |
| Sam Merrill (CLE) | 98% | 28.6<br><sub>20,27,19,26,27</sub> | 11.1<br><sub>8,16,6,8,10</sub> |  | 3.1<br><sub>1,2,4,3,7</sub> |  | 2.2<br><sub>1,3,3,2,1</sub> |  | 2.1<br><sub>2,4,1,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 16.4 |
| Jarrett Allen (CLE) | 100% | 27.3<br><sub>30,30,24,28,7</sub> | 13.2<br><sub>8,14,25,14,0</sub> | 12.5 · – | 8.4<br><sub>12,8,11,6,1</sub> | 7.5 | 1.5<br><sub>2,1,4,1,0</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.8 | 1.4 | 1.3 | 23.1 |
| Meleek Thomas (CLE) | 84% | 23.9<br><sub>20,-,23,26,18</sub> | 10.2<br><sub>10,-,13,17,9</sub> |  | 2.9<br><sub>4,-,1,5,1</sub> |  | 1.2<br><sub>1,-,2,1,0</sub> |  | 1.7<br><sub>0,-,3,3,3</sub> |  | 0.8 | 0.3 | 1.2 | 14.3 |
| Mario Hezonja (CLE) | 97% | 23.6<br><sub>17,17,20,27,23</sub> | 8.9<br><sub>5,10,8,12,12</sub> |  | 6.0<br><sub>3,6,11,8,8</sub> |  | 1.9<br><sub>2,2,4,3,1</sub> |  | 1.2<br><sub>1,2,1,3,2</sub> |  | 0.7 | 0.3 | 1.0 | 16.9 |
| Craig Porter Jr. (CLE) | 80% | 15.1<br><sub>-,4,16,8,14</sub> | 3.4<br><sub>-,0,2,0,0</sub> |  | 2.8<br><sub>-,1,2,4,1</sub> |  | 2.2<br><sub>-,0,4,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.5 | 0.9 | 8.3 |
| Tristan Enaruna (CLE) | 52% | 14.8<br><sub>-,-,6,-,16</sub> | 5.2<br><sub>-,-,2,-,4</sub> |  | 2.7<br><sub>-,-,1,-,4</sub> |  | 1.0<br><sub>-,-,0,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.8 |
| Thomas Bryant (CLE) | 58% | 13.2<br><sub>-,-,11,5,13</sub> | 6.1<br><sub>-,-,11,4,8</sub> |  | 3.4<br><sub>-,-,2,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.7<br><sub>-,-,3,0,1</sub> |  | 0.3 | 0.5 | 0.6 | 10.0 |
| Norchad Omier (CLE) | 16% | 9.3 | 3.1 |  | 2.1 |  | 0.7 |  | 0.2 |  | 0.3 | 0.2 | 0.7 | 5.9 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Tyrese Maxey (PHI) | 98% | 38.0<br><sub>36,38,38,36,34</sub> | 23.0<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.5 | 2.2 | 32.2 |
| Jaylen Brown (PHI) | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.6<br><sub>20,-,16,25,30</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.4 | 2.8 | 31.9 |
| LeBron James (PHI) | 98% | 35.2<br><sub>33,34,-,31,33</sub> | 17.8<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.5 | 2.6 | 31.5 |
| VJ Edgecombe (PHI) | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.3<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 1.4 | 21.5 |
| Joel Embiid (PHI) | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.4<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 9.1<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.9 | 2.9 | 34.8 |
| Dean Wade (PHI) | 91% | 22.2<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.3<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.6 | 8.0 |
| Anfernee Simons (PHI) | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.5 | 0.1 | 0.7 | 11.5 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.5 |
| Tacko Fall (PHI) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Jabari Walker (PHI) | 67% | 7.8<br><sub>-,-,19,2,-</sub> | 3.0<br><sub>-,-,12,0,-</sub> |  | 1.9<br><sub>-,-,6,0,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.3 |
| Rayan Rupert (PHI) | 43% | 6.8<br><sub>-,-,-,2,-</sub> | 2.4<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,2,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.2 |
| Caleb Love (PHI) | 35% | 6.7<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| Justin Edwards (PHI) | 52% | 6.6<br><sub>-,-,2,2,-</sub> | 2.7<br><sub>-,-,0,2,-</sub> |  | 0.9<br><sub>-,-,1,1,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Labaron Philon Jr. (PHI) | 58% | 6.5<br><sub>-,6,10,2,-</sub> | 2.6<br><sub>-,2,5,0,-</sub> |  | 0.9<br><sub>-,2,1,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>

<details><summary>if Peyton Watson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 98% | 36.6<br><sub>34,36,26,33,35</sub> | 19.2<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.8<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 3.7 | 31.4 |
| Donovan Mitchell (CLE) | 98% | 36.5<br><sub>31,33,24,36,33</sub> | 25.5<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.2<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.3 | 3.0 | 36.0 |
| Evan Mobley (CLE) | 98% | 35.6<br><sub>32,33,25,33,33</sub> | 18.1<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 9.8<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 53%</sub> | 3.9<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.9 | 1.9 | 31.8 |
| Peyton Watson (CLE) | 100% | 30.0<br><sub>28,22,22,-,-</sub> | 13.3<br><sub>22,4,5,-,-</sub> | 10.5 · – | 4.8<br><sub>6,4,2,-,-</sub> | 3.5 | 2.4<br><sub>2,3,6,-,-</sub> | 1.5 | 1.3<br><sub>1,0,1,-,-</sub> | 1.5 | 0.9 | 1.5 | 1.9 | 20.6 |
| Sam Merrill (CLE) | 98% | 27.9<br><sub>20,27,19,26,27</sub> | 10.6<br><sub>8,16,6,8,10</sub> |  | 3.1<br><sub>1,2,4,3,7</sub> |  | 2.1<br><sub>1,3,3,2,1</sub> |  | 2.0<br><sub>2,4,1,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 15.8 |
| Mario Hezonja (CLE) | 97% | 22.9<br><sub>17,17,20,27,23</sub> | 8.8<br><sub>5,10,8,12,12</sub> |  | 6.0<br><sub>3,6,11,8,8</sub> |  | 1.8<br><sub>2,2,4,3,1</sub> |  | 1.2<br><sub>1,2,1,3,2</sub> |  | 0.6 | 0.3 | 1.0 | 16.6 |
| Meleek Thomas (CLE) | 84% | 22.8<br><sub>20,-,23,26,18</sub> | 10.2<br><sub>10,-,13,17,9</sub> |  | 2.9<br><sub>4,-,1,5,1</sub> |  | 1.1<br><sub>1,-,2,1,0</sub> |  | 1.6<br><sub>0,-,3,3,3</sub> |  | 0.8 | 0.3 | 1.2 | 14.2 |
| Tristan Enaruna (CLE) | 52% | 14.6<br><sub>-,-,6,-,16</sub> | 5.2<br><sub>-,-,2,-,4</sub> |  | 2.6<br><sub>-,-,1,-,4</sub> |  | 0.9<br><sub>-,-,0,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.8 |
| Craig Porter Jr. (CLE) | 80% | 14.4<br><sub>-,4,16,8,14</sub> | 3.2<br><sub>-,0,2,0,0</sub> |  | 2.7<br><sub>-,1,2,4,1</sub> |  | 2.1<br><sub>-,0,4,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.4 | 0.8 | 8.1 |
| Thomas Bryant (CLE) | 58% | 13.9<br><sub>-,-,11,5,13</sub> | 6.6<br><sub>-,-,11,4,8</sub> |  | 3.6<br><sub>-,-,2,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.7<br><sub>-,-,3,0,1</sub> |  | 0.3 | 0.6 | 0.6 | 10.8 |
| Ernest Udeh Jr. (CLE) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Norchad Omier (CLE) | 16% | 8.2 | 2.9 |  | 1.8 |  | 0.6 |  | 0.1 |  | 0.3 | 0.2 | 0.6 | 5.4 |
| Tyrese Maxey (PHI) | 98% | 37.9<br><sub>36,38,38,36,34</sub> | 22.9<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.5 | 2.2 | 32.0 |
| Jaylen Brown (PHI) | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.7<br><sub>20,-,16,25,30</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.4 | 2.8 | 32.0 |
| LeBron James (PHI) | 98% | 35.1<br><sub>33,34,-,31,33</sub> | 17.9<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.5 | 2.6 | 31.6 |
| VJ Edgecombe (PHI) | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.3<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 1.3 | 21.4 |
| Joel Embiid (PHI) | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.4<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 9.2<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.0 | 2.9 | 34.8 |
| Dean Wade (PHI) | 91% | 22.1<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.2<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.5 | 8.1 |
| Anfernee Simons (PHI) | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.5 | 0.1 | 0.7 | 11.4 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.5 |
| Tacko Fall (PHI) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jabari Walker (PHI) | 67% | 7.7<br><sub>-,-,19,2,-</sub> | 3.0<br><sub>-,-,12,0,-</sub> |  | 1.9<br><sub>-,-,6,0,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.3 |
| Caleb Love (PHI) | 35% | 6.8<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| Rayan Rupert (PHI) | 43% | 6.7<br><sub>-,-,-,2,-</sub> | 2.4<br><sub>-,-,-,2,-</sub> |  | 1.2<br><sub>-,-,-,2,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.0 |
| Justin Edwards (PHI) | 52% | 6.6<br><sub>-,-,2,2,-</sub> | 2.7<br><sub>-,-,0,2,-</sub> |  | 0.9<br><sub>-,-,1,1,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Labaron Philon Jr. (PHI) | 58% | 6.5<br><sub>-,6,10,2,-</sub> | 2.6<br><sub>-,2,5,0,-</sub> |  | 0.9<br><sub>-,2,1,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>if Tyrese Proctor plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 98% | 36.8<br><sub>34,36,26,33,35</sub> | 20.0<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.8<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 3.8 | 32.1 |
| Donovan Mitchell (CLE) | 98% | 36.6<br><sub>31,33,24,36,33</sub> | 26.1<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 3.2 | 36.5 |
| Evan Mobley (CLE) | 98% | 35.8<br><sub>32,33,25,33,33</sub> | 19.1<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 9.9<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 53%</sub> | 3.9<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 2.0 | 2.1 | 32.9 |
| Sam Merrill (CLE) | 98% | 28.6<br><sub>20,27,19,26,27</sub> | 10.7<br><sub>8,16,6,8,10</sub> |  | 3.1<br><sub>1,2,4,3,7</sub> |  | 2.2<br><sub>1,3,3,2,1</sub> |  | 2.0<br><sub>2,4,1,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 16.0 |
| Meleek Thomas (CLE) | 84% | 24.5<br><sub>20,-,23,26,18</sub> | 10.8<br><sub>10,-,13,17,9</sub> |  | 3.2<br><sub>4,-,1,5,1</sub> |  | 1.2<br><sub>1,-,2,1,0</sub> |  | 1.8<br><sub>0,-,3,3,3</sub> |  | 0.9 | 0.3 | 1.2 | 15.1 |
| Mario Hezonja (CLE) | 97% | 24.0<br><sub>17,17,20,27,23</sub> | 8.9<br><sub>5,10,8,12,12</sub> |  | 6.0<br><sub>3,6,11,8,8</sub> |  | 1.9<br><sub>2,2,4,3,1</sub> |  | 1.2<br><sub>1,2,1,3,2</sub> |  | 0.7 | 0.3 | 1.0 | 16.8 |
| Tyrese Proctor (CLE) | 100% | 23.6<br><sub>6,20,18,19,22</sub> | 9.5<br><sub>2,7,9,10,11</sub> |  | 3.4<br><sub>1,6,4,4,1</sub> |  | 2.8<br><sub>1,2,5,2,0</sub> |  | 1.4<br><sub>0,1,3,2,2</sub> |  | 0.9 | 0.1 | 1.1 | 15.7 |
| Craig Porter Jr. (CLE) | 80% | 15.5<br><sub>-,4,16,8,14</sub> | 3.6<br><sub>-,0,2,0,0</sub> |  | 2.9<br><sub>-,1,2,4,1</sub> |  | 2.2<br><sub>-,0,4,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.5 | 0.9 | 8.7 |
| Tristan Enaruna (CLE) | 52% | 15.0<br><sub>-,-,6,-,16</sub> | 5.4<br><sub>-,-,2,-,4</sub> |  | 2.7<br><sub>-,-,1,-,4</sub> |  | 0.9<br><sub>-,-,0,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 9.0 |
| Thomas Bryant (CLE) | 58% | 14.6<br><sub>-,-,11,5,13</sub> | 6.8<br><sub>-,-,11,4,8</sub> |  | 3.8<br><sub>-,-,2,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,3,0,1</sub> |  | 0.3 | 0.6 | 0.6 | 11.1 |
| Norchad Omier (CLE) | 16% | 8.9 | 3.0 |  | 2.0 |  | 0.7 |  | 0.2 |  | 0.3 | 0.2 | 0.6 | 5.7 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Tyrese Maxey (PHI) | 98% | 38.0<br><sub>36,38,38,36,34</sub> | 22.9<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.6 | 0.5 | 2.2 | 32.0 |
| Jaylen Brown (PHI) | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.7<br><sub>20,-,16,25,30</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.4 | 2.8 | 32.0 |
| LeBron James (PHI) | 98% | 35.1<br><sub>33,34,-,31,33</sub> | 17.9<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.3 | 0.5 | 2.6 | 31.5 |
| VJ Edgecombe (PHI) | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.4<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 1.4 | 21.5 |
| Joel Embiid (PHI) | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.5<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 9.1<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.0 | 2.9 | 34.9 |
| Dean Wade (PHI) | 91% | 22.1<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.2<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.6 | 8.1 |
| Anfernee Simons (PHI) | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.5 | 0.1 | 0.7 | 11.5 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.6 |
| Tacko Fall (PHI) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Jabari Walker (PHI) | 67% | 7.7<br><sub>-,-,19,2,-</sub> | 3.1<br><sub>-,-,12,0,-</sub> |  | 1.9<br><sub>-,-,6,0,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.3 |
| Rayan Rupert (PHI) | 43% | 6.8<br><sub>-,-,-,2,-</sub> | 2.4<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,2,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.2 |
| Justin Edwards (PHI) | 52% | 6.7<br><sub>-,-,2,2,-</sub> | 2.7<br><sub>-,-,0,2,-</sub> |  | 0.9<br><sub>-,-,1,1,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.0 |
| Caleb Love (PHI) | 35% | 6.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| Labaron Philon Jr. (PHI) | 58% | 6.5<br><sub>-,6,10,2,-</sub> | 2.6<br><sub>-,2,5,0,-</sub> |  | 0.9<br><sub>-,2,1,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |

</details>


### UTA @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Jusuf Nurkic (UTA)

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 32.6<br><sub>33,37,29,22,44</sub> | 23.6<br><sub>26,31,8,7,39</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,4,3,7,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.8<br><sub>6,3,4,0,9</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>0,5,0,1,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.2 | 33.5 |
| Lauri Markkanen | 98% | 31.5<br><sub>6,-,29,31,39</sub> | 22.2<br><sub>2,-,13,22,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 7.1<br><sub>0,-,6,8,10</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>0,-,1,3,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>0,-,2,4,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.5 | 1.8 | 31.4 |
| Ace Bailey | 98% | 31.2<br><sub>34,40,37,24,35</sub> | 14.8<br><sub>17,19,9,5,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>10,6,7,6,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>3,0,1,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>3,1,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.0 | 1.7 | 23.1 |
| Darryn Peterson | 97% | 30.0<br><sub>26,26,36,33,30</sub> | 12.7<br><sub>14,18,16,14,7</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>7,5,4,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 4.0<br><sub>4,3,4,6,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>3,3,3,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.6 | 1.6 | 20.8 |
| Jaxson Hayes | 98% | 22.3<br><sub>-,37,20,22,21</sub> | 7.7<br><sub>-,2,7,9,2</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>-,11,7,5,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>-,4,2,0,1</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.0 | 14.7 |
| Josh Okogie | 91% | 19.2<br><sub>21,28,14,19,26</sub> | 4.0<br><sub>0,5,0,9,3</sub> |  | 3.5<br><sub>2,9,1,3,6</sub> |  | 1.1<br><sub>0,3,0,2,1</sub> |  | 0.4<br><sub>0,1,0,1,1</sub> |  | 0.8 | 0.3 | 0.7 | 8.6 |
| Brice Sensabaugh | 98% | 16.3<br><sub>9,18,19,14,12</sub> | 10.1<br><sub>11,16,12,7,6</sub> |  | 2.7<br><sub>2,3,3,2,2</sub> |  | 1.3<br><sub>0,1,2,1,0</sub> |  | 1.3<br><sub>3,4,2,1,1</sub> |  | 0.5 | 0.1 | 1.4 | 14.1 |
| Svi Mykhailiuk | 91% | 16.2<br><sub>13,15,18,14,17</sub> | 6.2<br><sub>0,3,6,3,6</sub> |  | 2.1<br><sub>1,2,1,2,3</sub> |  | 1.2<br><sub>0,1,3,0,0</sub> |  | 0.9<br><sub>0,1,2,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 9.5 |
| Josh Green | 88% | 16.1<br><sub>25,24,2,15,23</sub> | 3.2<br><sub>6,2,0,3,7</sub> |  | 1.8<br><sub>4,2,0,1,1</sub> |  | 0.8<br><sub>1,2,0,0,0</sub> |  | 0.3<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 5.8 |
| Mo Bamba | 72% | 14.9<br><sub>29,16,11,18,15</sub> | 5.4<br><sub>14,8,6,8,7</sub> |  | 5.9<br><sub>7,4,4,8,10</sub> |  | 0.8<br><sub>1,1,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 12.1 |
| Isaiah Collier | 98% | 14.6<br><sub>21,24,20,12,3</sub> | 6.9<br><sub>7,7,8,7,0</sub> |  | 2.1<br><sub>8,7,1,2,1</sub> |  | 4.0<br><sub>8,6,4,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.4 | 13.0 |
| Kyle Filipowski | 58% | 11.2<br><sub>8,-,6,8,-</sub> | 5.3<br><sub>0,-,5,1,-</sub> |  | 3.4<br><sub>1,-,0,2,-</sub> |  | 1.2<br><sub>0,-,2,0,-</sub> |  | 0.4<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.8 | 10.0 |
| Kobe Bufkin | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.7 |
| Tony Bradley | 48% | 8.1<br><sub>6,-,-,7,-</sub> | 2.7<br><sub>2,-,-,2,-</sub> |  | 2.4<br><sub>1,-,-,3,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.6 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving | 98% | 32.3<br><sub>33,27,35,-,36</sub> | 24.7<br><sub>18,15,35,-,29</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>6,2,4,-,7</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 5.2<br><sub>6,4,9,-,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>2,3,5,-,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.6 | 2.3 | 34.6 |
| Cooper Flagg | 98% | 31.3<br><sub>40,33,39,40,40</sub> | 23.7<br><sub>29,26,33,17,19</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 6.7<br><sub>6,5,9,4,10</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.0<br><sub>11,8,6,6,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 1.0 | 2.7 | 36.3 |
| P.J. Washington | 98% | 30.6<br><sub>41,27,34,38,39</sub> | 15.3<br><sub>20,18,3,12,21</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>9,9,10,5,10</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,0,1,1,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>4,2,1,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 1.0 | 1.7 | 24.5 |
| Naji Marshall | 84% | 24.0<br><sub>-,-,-,24,26</sub> | 13.2<br><sub>-,-,-,5,22</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>-,-,-,2,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>-,-,-,7,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>-,-,-,0,3</sub> |  | 1.1 | 0.2 | 1.8 | 20.8 |
| Zaccharie Risacher | 93% | 20.4<br><sub>30,29,28,19,18</sub> | 7.0<br><sub>6,13,12,0,2</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>8,6,6,5,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,1,3,1,2</sub> |  | 0.9<br><sub>1,2,3,0,0</sub> |  | 1.1 | 0.8 | 0.9 | 12.3 |
| Daniel Gafford | 98% | 20.2<br><sub>26,27,29,26,18</sub> | 10.6<br><sub>8,7,18,20,2</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>9,11,7,7,4</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.8 | 1.6 | 1.2 | 18.6 |
| Max Christie | 91% | 18.4<br><sub>26,22,18,8,-</sub> | 7.8<br><sub>11,11,2,0,-</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>5,5,1,2,-</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>3,2,0,0,-</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>3,3,0,0,-</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.3 | 0.9 | 11.4 |
| Santi Aldama | 89% | 15.0 | 7.3 |  | 3.6 |  | 1.4 |  | 0.8 |  | 0.6 | 0.4 | 0.7 | 12.4 |
| Caleb Martin | 96% | 14.9<br><sub>-,14,25,21,20</sub> | 4.8<br><sub>-,10,8,5,0</sub> |  | 2.5<br><sub>-,2,0,6,3</sub> |  | 1.1<br><sub>-,0,0,0,2</sub> |  | 0.4<br><sub>-,2,2,1,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.3 |
| Walter Clayton Jr. | 88% | 13.6<br><sub>17,15,9,24,21</sub> | 6.4<br><sub>15,0,3,20,8</sub> |  | 2.1<br><sub>4,2,2,1,6</sub> |  | 3.1<br><sub>4,5,1,2,5</sub> |  | 0.9<br><sub>2,0,1,4,2</sub> |  | 0.5 | 0.2 | 0.7 | 11.6 |
| Morez Johnson Jr. | 98% | 11.9<br><sub>15,18,17,17,18</sub> | 5.3<br><sub>6,10,2,13,8</sub> |  | 1.9<br><sub>2,6,2,2,3</sub> |  | 1.2<br><sub>1,3,1,1,1</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.4 | 0.1 | 0.7 | 8.5 |
| Marcus Sasser | 96% | 9.5<br><sub>8,22,7,19,5</sub> | 3.7<br><sub>0,10,0,4,0</sub> |  | 0.9<br><sub>1,1,0,1,1</sub> |  | 1.5<br><sub>0,4,1,1,2</sub> |  | 0.5<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.1 |
| Moussa Cisse | 58% | 6.7<br><sub>-,3,-,2,-</sub> | 2.7<br><sub>-,0,-,0,-</sub> |  | 2.6<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.5 |
| Tobi Lawal | 52% | 5.7<br><sub>-,3,-,2,-</sub> | 2.3<br><sub>-,0,-,2,-</sub> |  | 1.1<br><sub>-,0,-,0,-</sub> |  | 0.7<br><sub>-,1,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Jett Howard | 52% | 5.4<br><sub>-,3,-,2,-</sub> | 2.4<br><sub>-,0,-,2,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.5 |

</details>


### OKC @ MEM
Out: Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 33.9<br><sub>30,28,31,39,35</sub> | 30.8<br><sub>26,21,26,43,42</sub> | 32.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>3,2,3,8,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,1,3,4,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.9 | 2.9 | 41.9 |
| Ajay Mitchell | 98% | 30.3<br><sub>25,28,26,35,32</sub> | 18.7<br><sub>30,29,6,20,23</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,4,3,5,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>5,3,5,1,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>1,2,0,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.6 | 0.4 | 2.0 | 27.4 |
| Jared McCain | 98% | 26.9<br><sub>30,29,28,27,25</sub> | 14.2<br><sub>18,10,10,7,9</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,4,4,9,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>4,4,2,2,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>4,0,0,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.1 | 1.7 | 19.4 |
| Isaiah Hartenstein | 98% | 26.6<br><sub>26,26,25,28,26</sub> | 10.1<br><sub>15,10,10,5,3</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 10.6<br><sub>13,14,7,14,12</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,3,0,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.8 | 23.9 |
| Kenrich Williams | 96% | 25.2<br><sub>24,17,21,31,29</sub> | 10.2<br><sub>3,7,11,12,13</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>7,3,7,3,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,0,3,1,2</sub> |  | 1.4<br><sub>0,1,3,2,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.2 | 1.1 | 17.7 |
| Aday Mara | 97% | 23.9<br><sub>20,21,28,20,25</sub> | 8.3<br><sub>11,6,7,10,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>10,3,9,9,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>2,1,3,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 2.4 | 1.7 | 16.7 |
| Bennett Stirtz | 97% | 21.9<br><sub>25,28,26,12,22</sub> | 7.2<br><sub>7,8,11,9,16</sub> |  | 2.0<br><sub>1,0,1,2,1</sub> |  | 1.5<br><sub>1,3,3,0,1</sub> |  | 1.2<br><sub>1,1,3,3,4</sub> |  | 0.7 | 0.1 | 0.8 | 10.7 |
| Alex Caruso | 98% | 21.8<br><sub>9,-,-,-,20</sub> | 9.2<br><sub>9,-,-,-,7</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,-,-,-,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,-,-,-,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>3,-,-,-,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.5 | 0.4 | 1.0 | 15.4 |
| Micah Peavy | 72% | 20.9<br><sub>-,5,14,16,26</sub> | 5.6<br><sub>-,0,2,8,2</sub> |  | 4.2<br><sub>-,0,1,5,9</sub> |  | 1.1<br><sub>-,0,0,0,1</sub> |  | 0.5<br><sub>-,0,0,2,0</sub> |  | 0.8 | 0.2 | 0.9 | 10.9 |
| Josh Dix | 64% | 15.2<br><sub>22,24,9,12,-</sub> | 5.2<br><sub>0,2,7,0,-</sub> |  | 1.3<br><sub>1,2,0,1,-</sub> |  | 0.8<br><sub>0,0,0,0,-</sub> |  | 0.6<br><sub>0,0,1,0,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.3 |
| Dalen Terry | 52% | 9.7<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 5.8 |
| Brooks Barnhizer | 52% | 9.6<br><sub>3,14,6,-,-</sub> | 2.5<br><sub>0,3,5,-,-</sub> |  | 2.1<br><sub>0,2,2,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.2 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 97% | 32.2<br><sub>31,28,26,38,33</sub> | 15.4<br><sub>13,18,27,18,10</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 9.2<br><sub>7,12,9,9,6</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 5.1<br><sub>4,12,3,5,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>1,4,3,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.7 | 2.7 | 29.7 |
| Ty Jerome | 98% | 29.1<br><sub>30,24,-,37,29</sub> | 19.9<br><sub>15,10,-,40,23</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>1,2,-,5,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>8,3,-,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,1,-,5,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 2.5 | 29.0 |
| Cedric Coward | 98% | 27.9<br><sub>31,27,23,31,33</sub> | 13.7<br><sub>16,17,10,10,23</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>11,7,7,9,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>3,4,2,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>4,3,2,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 1.7 | 23.0 |
| Jaylen Wells | 98% | 24.9<br><sub>30,25,22,34,21</sub> | 9.9<br><sub>14,10,4,16,0</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,1,2,3,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,0,0,3,3</sub> |  | 1.6<br><sub>2,2,0,3,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.1 | 0.9 | 14.2 |
| Jerami Grant | 98% | 23.1<br><sub>24,27,23,24,24</sub> | 10.3<br><sub>13,2,14,11,11</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,3,1,2,2</sub> |  | 1.4<br><sub>3,0,1,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.6 | 1.4 | 14.4 |
| Zach Edey | 98% | 21.0<br><sub>21,19,18,19,25</sub> | 8.1<br><sub>4,13,4,6,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>3,7,6,9,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>2,0,0,1,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.3 | 1.3 | 16.8 |
| Cam Spencer | 98% | 19.5<br><sub>18,23,25,19,24</sub> | 7.8<br><sub>8,8,10,13,7</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>5,6,5,1,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,8,13,7,9</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,1,2,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.1 | 1.0 | 15.1 |
| Javon Small | 88% | 16.4<br><sub>-,-,20,-,-</sub> | 7.0<br><sub>-,-,7,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 2.4<br><sub>-,-,5,-,-</sub> |  | 0.8<br><sub>-,-,2,-,-</sub> |  | 0.6 | 0.2 | 1.2 | 11.7 |
| GG Jackson | 97% | 13.2<br><sub>16,21,21,16,7</sub> | 7.0<br><sub>4,12,21,6,1</sub> |  | 2.6<br><sub>1,7,3,0,2</sub> |  | 0.8<br><sub>2,2,2,1,0</sub> |  | 0.8<br><sub>0,2,5,0,0</sub> |  | 0.4 | 0.4 | 1.0 | 10.4 |
| Kris Murray | 76% | 12.2<br><sub>-,3,21,19,15</sub> | 3.1<br><sub>-,0,2,0,5</sub> |  | 1.9<br><sub>-,1,1,4,1</sub> |  | 0.8<br><sub>-,0,1,1,1</sub> |  | 0.2<br><sub>-,0,0,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 5.8 |
| Quinten Post | 91% | 10.2<br><sub>12,7,-,-,11</sub> | 4.1<br><sub>12,10,-,-,2</sub> |  | 1.8<br><sub>2,4,-,-,1</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.4<br><sub>2,2,-,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.3 |
| Olivier-Maxence Prosper | 58% | 8.7<br><sub>-,3,4,-,7</sub> | 4.9<br><sub>-,4,2,-,4</sub> |  | 1.7<br><sub>-,1,1,-,3</sub> |  | 0.5<br><sub>-,0,1,-,1</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.1 |
| Jahmai Mashack | 38% | 8.2<br><sub>-,-,4,-,-</sub> | 2.9<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.7 | 4.8 |
| Taylor Hendricks | 52% | 6.9<br><sub>-,3,4,-,-</sub> | 2.8<br><sub>-,0,6,-,-</sub> |  | 1.4<br><sub>-,1,1,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,2,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Karim Lopez | 47% | 5.9<br><sub>-,3,4,-,-</sub> | 2.7<br><sub>-,0,2,-,-</sub> |  | 1.1<br><sub>-,1,1,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |
| Carson Cooper | 48% | 5.3<br><sub>-,-,3,-,-</sub> | 2.1<br><sub>-,-,1,-,-</sub> |  | 2.5<br><sub>-,-,2,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.9 | 5.5 |

</details>


### TOR @ MIL
Out: Kam Jones (MIL), Pete Nance (MIL), Cormac Ryan (MIL), Kawhi Leonard (TOR), Malachi Smith (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.4–111.5 | TOR 66% | 1.51 / 2.96 | MIL +6.5 | 228.5 | MIL +6.5 covers 51%; o230.5 46% |
| Expected (weighted by chance each plays) | 118.2–111.4 | TOR 68% | 1.47 / 3.13 | MIL +6.5 | 229.5 | MIL +6.5 covers 49%; o230.5 48% |
| if Scottie Barnes plays | 118.8–111.3 | TOR 70% | 1.43 / 3.35 | MIL +7.5 | 229.5 | MIL +6.5 covers 47%; o230.5 49% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes (TOR) | Questionable | 55% | 34.4 | 22.6 | 7.2 | 7.2 | 0.9 | 1.8 | 1.1 | 3.3 | 37.0 | full tables below |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 35.7<br><sub>32,34,32,37,33</sub> | 25.9<br><sub>25,9,22,26,22</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>9,3,10,6,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 5.2<br><sub>6,5,5,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>3,1,4,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.5 | 2.6 | 37.9 |
| Immanuel Quickley | 98% | 33.7<br><sub>29,37,33,38,32</sub> | 20.3<br><sub>16,17,12,27,13</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,6,6,4,1</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 7.0<br><sub>7,8,7,2,7</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>4,4,3,1,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.5 | 0.1 | 1.7 | 31.5 |
| Ja'Kobe Walter | 98% | 32.1<br><sub>28,32,33,35,27</sub> | 14.4<br><sub>14,9,11,10,8</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,3,4,6,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>2,1,2,5,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.6<br><sub>3,3,3,0,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.5 | 0.3 | 1.0 | 21.0 |
| Collin Murray-Boyles | 98% | 27.8<br><sub>15,23,20,28,23</sub> | 14.0<br><sub>10,15,4,18,13</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>2,5,3,7,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,1,1,0,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.5<br><sub>2,1,0,1,1</sub> |  | 1.3 | 1.1 | 1.7 | 22.9 |
| Jamal Shead | 98% | 25.7<br><sub>23,23,25,20,20</sub> | 8.5<br><sub>13,2,9,6,3</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>4,1,2,1,3</sub> |  | 6.4<br><sub>7,8,6,6,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>1,0,2,0,1</sub> |  | 1.3 | 0.2 | 1.7 | 17.1 |
| Jakob Poeltl | 80% | 22.1<br><sub>10,23,-,-,19</sub> | 8.9<br><sub>2,12,-,-,8</sub> |  | 6.5<br><sub>2,11,-,-,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>0,3,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 1.0 | 0.7 | 1.1 | 17.1 |
| Jamison Battle | 98% | 22.1<br><sub>20,19,17,21,19</sub> | 10.0<br><sub>7,2,20,12,9</sub> |  | 3.0<br><sub>0,0,5,0,1</sub> |  | 1.1<br><sub>1,0,0,0,0</sub> |  | 1.8<br><sub>1,0,4,4,2</sub> |  | 0.5 | 0.2 | 0.7 | 14.1 |
| Allen Graves | 97% | 17.7<br><sub>18,9,10,7,14</sub> | 6.0<br><sub>3,7,3,0,5</sub> |  | 3.0<br><sub>1,4,0,0,1</sub> |  | 1.2<br><sub>0,0,0,2,1</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.7 | 0.5 | 0.6 | 10.3 |
| Kyle Anderson | 80% | 13.2<br><sub>5,-,4,8,4</sub> | 3.8<br><sub>0,-,2,2,2</sub> |  | 2.4<br><sub>0,-,3,0,0</sub> |  | 2.4<br><sub>1,-,3,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.4 | 0.7 | 8.6 |
| Alijah Martin | 88% | 12.0<br><sub>5,-,16,6,9</sub> | 5.1<br><sub>5,-,5,2,6</sub> |  | 1.9<br><sub>1,-,2,2,1</sub> |  | 1.2<br><sub>1,-,4,0,0</sub> |  | 0.4<br><sub>1,-,1,0,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.2 |
| Trayce Jackson-Davis | 96% | 11.7<br><sub>20,1,9,2,4</sub> | 4.4<br><sub>6,0,5,0,1</sub> |  | 3.8<br><sub>11,0,5,0,0</sub> |  | 0.9<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.6 | 0.5 | 9.1 |
| Jaden Bradley | 67% | 8.1<br><sub>5,-,4,-,4</sub> | 2.6<br><sub>0,-,3,-,2</sub> |  | 1.4<br><sub>1,-,1,-,1</sub> |  | 0.8<br><sub>1,-,2,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.8 | 0.2 | 0.5 | 4.9 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.7<br><sub>32,27,27,31,33</sub> | 19.7<br><sub>23,23,15,21,25</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>10,3,3,6,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>7,0,2,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>3,4,4,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.5 | 28.6 |
| Jaime Jaquez Jr. | 98% | 28.4<br><sub>25,27,23,28,31</sub> | 14.9<br><sub>8,19,8,19,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,4,7,8,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>0,2,5,2,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>0,3,1,2,4</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.2 | 2.4 | 23.9 |
| Myles Turner | 98% | 28.4<br><sub>28,22,24,31,36</sub> | 10.7<br><sub>6,4,10,13,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>9,2,7,5,9</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,2,2,6</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>0,0,1,3,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 2.1 | 1.4 | 18.1 |
| Kyle Kuzma | 98% | 26.3<br><sub>29,18,23,22,27</sub> | 11.7<br><sub>17,4,14,2,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>7,6,3,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,1,3,3,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>4,0,2,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.9 | 19.4 |
| Ryan Rollins | 98% | 26.0<br><sub>32,17,26,17,24</sub> | 13.7<br><sub>19,4,9,10,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>2,4,3,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>4,5,7,2,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 2.6 | 22.1 |
| AJ Green | 98% | 20.7<br><sub>20,24,20,24,20</sub> | 7.1<br><sub>3,9,0,13,5</sub> |  | 2.1<br><sub>4,1,3,3,2</sub> |  | 1.4<br><sub>3,2,2,3,3</sub> |  | 1.4<br><sub>1,3,0,4,1</sub> |  | 0.4 | 0.1 | 0.9 | 10.7 |
| Brayden Burries | 97% | 19.4<br><sub>16,17,21,26,22</sub> | 8.5<br><sub>4,10,14,9,9</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>2,5,3,9,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>1,1,1,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.2 | 1.3 | 14.2 |
| Kel'el Ware | 91% | 17.3<br><sub>19,17,24,17,16</sub> | 8.5<br><sub>16,6,19,2,2</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>14,8,10,9,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 0.9<br><sub>0,0,3,0,1</sub> |  | 0.7<br><sub>0,0,3,0,0</sub> |  | 0.5 | 0.7 | 1.3 | 15.5 |
| Kasparas Jakucionis | 91% | 17.2<br><sub>21,19,21,22,12</sub> | 6.2<br><sub>7,4,5,7,3</sub> |  | 2.3<br><sub>4,2,3,5,1</sub> |  | 3.0<br><sub>5,6,3,7,1</sub> |  | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.2 | 1.2 | 11.5 |
| Nate Ament | 88% | 13.8<br><sub>14,20,19,8,18</sub> | 5.8<br><sub>7,8,14,4,9</sub> |  | 2.1<br><sub>3,4,1,1,2</sub> |  | 0.5<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,1,2,0,2</sub> |  | 0.4 | 0.2 | 0.8 | 8.5 |
| Caris LeVert | 23% | 13.3<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 8.1 |
| Gary Trent Jr. | 48% | 8.9<br><sub>-,7,6,-,-</sub> | 3.6<br><sub>-,3,3,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,1,1,-,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.8 |
| Jericho Sims | 63% | 8.1<br><sub>-,7,-,15,1</sub> | 1.9<br><sub>-,0,-,0,0</sub> |  | 2.2<br><sub>-,0,-,2,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Ousmane Dieng | 71% | 8.0<br><sub>3,13,6,-,2</sub> | 2.9<br><sub>0,4,0,-,0</sub> |  | 1.2<br><sub>0,0,1,-,0</sub> |  | 1.0<br><sub>0,0,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.1 |

</details>

<details><summary>if Scottie Barnes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 31.7<br><sub>32,27,27,31,33</sub> | 19.8<br><sub>23,23,15,21,25</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>10,3,3,6,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>7,0,2,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>3,4,4,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.5 | 28.6 |
| Jaime Jaquez Jr. (MIL) | 98% | 28.4<br><sub>25,27,23,28,31</sub> | 14.8<br><sub>8,19,8,19,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>6,4,7,8,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>0,2,5,2,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>0,3,1,2,4</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.2 | 2.4 | 24.0 |
| Myles Turner (MIL) | 98% | 28.4<br><sub>28,22,24,31,36</sub> | 10.8<br><sub>6,4,10,13,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>9,2,7,5,9</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,2,2,6</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>0,0,1,3,4</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 2.1 | 1.4 | 18.2 |
| Kyle Kuzma (MIL) | 98% | 26.2<br><sub>29,18,23,22,27</sub> | 11.6<br><sub>17,4,14,2,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>7,6,3,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,1,3,3,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>4,0,2,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.9 | 19.2 |
| Ryan Rollins (MIL) | 98% | 26.0<br><sub>32,17,26,17,24</sub> | 13.8<br><sub>19,4,9,10,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>2,4,3,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>4,5,7,2,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 2.6 | 22.2 |
| AJ Green (MIL) | 98% | 20.7<br><sub>20,24,20,24,20</sub> | 7.1<br><sub>3,9,0,13,5</sub> |  | 2.1<br><sub>4,1,3,3,2</sub> |  | 1.4<br><sub>3,2,2,3,3</sub> |  | 1.4<br><sub>1,3,0,4,1</sub> |  | 0.4 | 0.1 | 0.9 | 10.6 |
| Brayden Burries (MIL) | 97% | 19.4<br><sub>16,17,21,26,22</sub> | 8.6<br><sub>4,10,14,9,9</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>2,5,3,9,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,1,1,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.2 | 1.3 | 14.2 |
| Kasparas Jakucionis (MIL) | 91% | 17.3<br><sub>21,19,21,22,12</sub> | 6.2<br><sub>7,4,5,7,3</sub> |  | 2.3<br><sub>4,2,3,5,1</sub> |  | 3.1<br><sub>5,6,3,7,1</sub> |  | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.2 | 1.2 | 11.6 |
| Kel'el Ware (MIL) | 91% | 17.3<br><sub>19,17,24,17,16</sub> | 8.5<br><sub>16,6,19,2,2</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>14,8,10,9,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 0.9<br><sub>0,0,3,0,1</sub> |  | 0.7<br><sub>0,0,3,0,0</sub> |  | 0.5 | 0.7 | 1.3 | 15.4 |
| Nate Ament (MIL) | 88% | 13.7<br><sub>14,20,19,8,18</sub> | 5.7<br><sub>7,8,14,4,9</sub> |  | 2.2<br><sub>3,4,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,1,2,0,2</sub> |  | 0.4 | 0.2 | 0.8 | 8.4 |
| Caris LeVert (MIL) | 23% | 13.3<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 8.1 |
| Gary Trent Jr. (MIL) | 48% | 8.9<br><sub>-,7,6,-,-</sub> | 3.6<br><sub>-,3,3,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,1,1,-,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.7 |
| Ousmane Dieng (MIL) | 71% | 8.0<br><sub>3,13,6,-,2</sub> | 2.9<br><sub>0,4,0,-,0</sub> |  | 1.2<br><sub>0,0,1,-,0</sub> |  | 1.0<br><sub>0,0,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.1 |
| Jericho Sims (MIL) | 63% | 8.0<br><sub>-,7,-,15,1</sub> | 1.9<br><sub>-,0,-,0,0</sub> |  | 2.2<br><sub>-,0,-,2,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Scottie Barnes (TOR) | 100% | 34.4<br><sub>31,39,36,38,32</sub> | 22.6<br><sub>28,41,29,22,17</sub> | 22.5 · – | 7.2<br><sub>6,5,6,15,6</sub> | 7.5 | 7.2<br><sub>4,5,5,8,6</sub> | 5.5 | 0.9<br><sub>0,1,0,0,1</sub> |  | 1.8 | 1.1 | 3.3 | 37.0 |
| RJ Barrett (TOR) | 98% | 33.7<br><sub>32,34,32,37,33</sub> | 22.0<br><sub>25,9,22,26,22</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>9,3,10,6,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>6,5,5,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,1,4,2,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.4 | 2.3 | 32.3 |
| Immanuel Quickley (TOR) | 98% | 32.2<br><sub>29,37,33,38,32</sub> | 18.0<br><sub>16,17,12,27,13</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,6,6,4,1</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.5<br><sub>7,8,7,2,7</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>4,4,3,1,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4 | 0.1 | 1.5 | 28.4 |
| Ja'Kobe Walter (TOR) | 98% | 30.0<br><sub>28,32,33,35,27</sub> | 12.3<br><sub>14,9,11,10,8</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>5,3,4,6,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,1,2,5,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.3<br><sub>3,3,3,0,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.5 | 0.3 | 0.8 | 18.1 |
| Collin Murray-Boyles (TOR) | 98% | 24.1<br><sub>15,23,20,28,23</sub> | 11.6<br><sub>10,15,4,18,13</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>2,5,3,7,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,1,0,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.4<br><sub>2,1,0,1,1</sub> |  | 1.1 | 0.9 | 1.4 | 19.3 |
| Jamal Shead (TOR) | 98% | 22.9<br><sub>23,23,25,20,20</sub> | 7.1<br><sub>13,2,9,6,3</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,1,2,1,3</sub> |  | 5.5<br><sub>7,8,6,6,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 0.8<br><sub>1,0,2,0,1</sub> |  | 1.1 | 0.2 | 1.3 | 14.5 |
| Jakob Poeltl (TOR) | 80% | 20.3<br><sub>10,23,-,-,19</sub> | 8.1<br><sub>2,12,-,-,8</sub> |  | 5.9<br><sub>2,11,-,-,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>0,3,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.9 | 0.7 | 1.0 | 15.5 |
| Jamison Battle (TOR) | 98% | 18.1<br><sub>20,19,17,21,19</sub> | 7.9<br><sub>7,2,20,12,9</sub> |  | 2.4<br><sub>0,0,5,0,1</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 1.4<br><sub>1,0,4,4,2</sub> |  | 0.4 | 0.1 | 0.5 | 11.2 |
| Allen Graves (TOR) | 97% | 13.8<br><sub>18,9,10,7,14</sub> | 4.5<br><sub>3,7,3,0,5</sub> |  | 2.4<br><sub>1,4,0,0,1</sub> |  | 0.9<br><sub>0,0,0,2,1</sub> |  | 0.5<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.4 | 0.5 | 7.8 |
| Alijah Martin (TOR) | 88% | 9.3<br><sub>5,-,16,6,9</sub> | 4.0<br><sub>5,-,5,2,6</sub> |  | 1.4<br><sub>1,-,2,2,1</sub> |  | 1.0<br><sub>1,-,4,0,0</sub> |  | 0.3<br><sub>1,-,1,0,0</sub> |  | 0.5 | 0.2 | 0.6 | 6.4 |
| Kyle Anderson (TOR) | 80% | 8.6<br><sub>5,-,4,8,4</sub> | 2.4<br><sub>0,-,2,2,2</sub> |  | 1.6<br><sub>0,-,3,0,0</sub> |  | 1.5<br><sub>1,-,3,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.5 |
| Trayce Jackson-Davis (TOR) | 96% | 7.6<br><sub>20,1,9,2,4</sub> | 3.2<br><sub>6,0,5,0,1</sub> |  | 2.4<br><sub>11,0,5,0,0</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.4 | 0.3 | 6.2 |
| Jaden Bradley (TOR) | 67% | 6.5<br><sub>5,-,4,-,4</sub> | 2.5<br><sub>0,-,3,-,2</sub> |  | 1.2<br><sub>1,-,1,-,1</sub> |  | 0.7<br><sub>1,-,2,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.6 | 0.1 | 0.4 | 4.3 |

</details>


### MIN @ NOP
Out: Yves Missi (NOP), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.9–118.4 | MIN 49% | 2.05 / 1.95 | NOP +0.5 | 236.5 | NOP +4.5 covers 63%; o230.5 62% |
| Expected (weighted by chance each plays) | 118.4–118.7 | MIN 49% | 2.06 / 1.95 | NOP +0.5 | 236.5 | NOP +4.5 covers 63%; o230.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Terrence Shannon Jr. (MIN) | Questionable | 55% | 19.2 | 10.3 | 2.3 | 1.8 | 1.2 | 0.6 | 0.1 | 1.1 | 14.5 | small |
| Jaron Pierre Jr. (NOP) | Doubtful | 20% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 5.9 | small |
| Malik Dia (NOP) | Doubtful | 20% | 8.6 | 3.6 | 1.5 | 0.8 | 0.2 | 0.2 | 0.2 | 0.4 | 5.9 | small |

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.6<br><sub>35,33,39,29,37</sub> | 18.9<br><sub>19,23,19,13,14</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>7,6,3,6,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>4,7,3,3,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,1,2,2,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.9 | 1.9 | 27.8 |
| Ayo Dosunmu | 98% | 33.3<br><sub>32,30,38,37,34</sub> | 19.2<br><sub>17,15,27,19,21</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>3,7,9,12,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>4,2,3,8,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>3,3,2,1,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.4 | 2.1 | 28.9 |
| Jonathan Kuminga | 98% | 31.8<br><sub>32,22,40,33,32</sub> | 15.5<br><sub>20,5,19,8,16</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>3,1,6,10,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>5,0,3,3,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>3,1,2,2,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.8 | 1.6 | 24.2 |
| Rudy Gobert | 98% | 30.7<br><sub>20,30,-,31,33</sub> | 10.2<br><sub>1,9,-,10,8</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 11.9<br><sub>4,13,-,10,11</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,4,-,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.9 | 1.7 | 1.4 | 23.9 |
| LaMelo Ball | 98% | 29.0<br><sub>28,29,20,33,31</sub> | 21.7<br><sub>8,24,10,34,20</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>4,4,8,6,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.7<br><sub>8,7,4,3,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>2,6,0,6,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.3 | 3.5 | 32.7 |
| Jaylen Clark | 88% | 20.1<br><sub>7,17,20,21,25</sub> | 7.5<br><sub>3,5,10,4,10</sub> |  | 2.4<br><sub>2,0,2,2,4</sub> |  | 1.2<br><sub>1,2,1,0,1</sub> |  | 0.9<br><sub>1,1,2,1,2</sub> |  | 1.1 | 0.2 | 0.7 | 11.1 |
| Trey Lyles | 98% | 19.8<br><sub>22,17,17,21,20</sub> | 7.0<br><sub>7,10,6,12,5</sub> |  | 3.9<br><sub>3,5,0,4,2</sub> |  | 1.1<br><sub>1,0,0,0,0</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> |  | 0.6 | 0.3 | 0.7 | 12.0 |
| Joan Beringer | 96% | 17.5<br><sub>20,18,34,14,13</sub> | 7.5<br><sub>7,4,12,2,4</sub> |  | 6.2<br><sub>9,4,6,7,7</sub> |  | 0.7<br><sub>2,0,2,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.3 | 0.8 | 14.5 |
| Bones Hyland | 97% | 16.7<br><sub>16,20,14,14,16</sub> | 9.6<br><sub>13,19,6,10,19</sub> |  | 1.8<br><sub>1,0,1,1,2</sub> |  | 2.9<br><sub>3,8,3,3,4</sub> |  | 1.5<br><sub>3,3,0,2,4</sub> |  | 0.7 | 0.3 | 1.2 | 14.3 |
| Zyon Pullin | 38% | 7.7<br><sub>-,2,-,-,-</sub> | 3.5<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Rocco Zikarsky | 36% | 7.6<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.8 | 0.3 | 5.4 |
| Cody Williams | 52% | 6.3<br><sub>-,2,-,7,-</sub> | 0.2<br><sub>-,0,-,0,-</sub> |  | 1.2<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 1.7 |
| Isaiah Evans | 38% | 5.5<br><sub>-,2,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 91% | 32.2<br><sub>30,32,29,40,-</sub> | 14.8<br><sub>6,19,15,18,-</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>1,5,5,5,-</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>3,3,5,5,-</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>2,2,1,3,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.5 | 1.4 | 22.6 |
| Dejounte Murray | 98% | 31.9<br><sub>30,-,-,-,45</sub> | 16.9<br><sub>10,-,-,-,20</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>8,-,-,-,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 6.2<br><sub>5,-,-,-,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,-,-,-,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.8 | 0.4 | 3.0 | 29.3 |
| Zion Williamson | 98% | 30.7<br><sub>32,31,30,35,38</sub> | 19.3<br><sub>25,22,15,25,23</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>5,6,6,11,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>2,2,4,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.1<br><sub>1,0,0,0,0</sub> |  | 1.2 | 0.7 | 2.2 | 27.7 |
| Jeremiah Fears | 98% | 27.8<br><sub>24,29,31,38,34</sub> | 14.7<br><sub>11,22,20,12,19</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>4,8,5,4,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>3,13,7,7,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>1,3,1,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 2.4 | 23.0 |
| Saddiq Bey | 98% | 26.1<br><sub>26,24,26,36,29</sub> | 12.7<br><sub>9,10,25,18,22</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>0,4,6,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>3,3,1,1,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.1 | 1.1 | 18.6 |
| Herbert Jones | 98% | 24.1<br><sub>19,32,25,28,37</sub> | 7.5<br><sub>4,16,11,9,2</sub> |  | 2.8<br><sub>2,4,3,4,5</sub> |  | 1.8<br><sub>0,1,2,3,1</sub> |  | 0.8<br><sub>0,0,1,3,0</sub> |  | 1.2 | 0.4 | 1.1 | 12.1 |
| Derik Queen | 98% | 22.5<br><sub>25,22,23,24,27</sub> | 11.4<br><sub>11,9,8,20,20</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>12,2,8,7,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>1,3,4,5,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.3<br><sub>0,1,0,1,0</sub> |  | 1.0 | 0.9 | 2.1 | 20.9 |
| Karlo Matkovic | 91% | 16.4<br><sub>18,28,18,29,21</sub> | 6.5<br><sub>5,12,8,25,5</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,4,10,6,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>1,1,1,1,2</sub> |  | 0.6<br><sub>1,1,2,5,1</sub> |  | 0.5 | 1.0 | 0.7 | 11.2 |
| Bennedict Mathurin | 98% | 15.6<br><sub>14,19,19,13,15</sub> | 7.5<br><sub>5,10,7,4,2</sub> |  | 2.7<br><sub>1,3,1,0,5</sub> |  | 1.3<br><sub>2,2,2,0,1</sub> |  | 0.5<br><sub>1,2,1,0,0</sub> |  | 0.4 | 0.2 | 1.1 | 11.5 |
| Trendon Watford | 67% | 13.3<br><sub>-,17,18,16,20</sub> | 5.5<br><sub>-,8,7,4,7</sub> |  | 2.4<br><sub>-,1,4,4,3</sub> |  | 1.4<br><sub>-,2,0,1,2</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.4 | 0.9 | 9.3 |
| Jordan Poole | 64% | 12.4<br><sub>7,-,-,-,-</sub> | 6.2<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-,-</sub> |  | 1.6<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 9.1 |
| DeAndre Jordan | 35% | 8.1<br><sub>13,-,-,-,-</sub> | 2.4<br><sub>3,-,-,-,-</sub> |  | 3.0<br><sub>4,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.4 | 5.9 |
| Bryce McGowens | 58% | 7.3<br><sub>3,6,15,6,-</sub> | 2.7<br><sub>0,4,3,0,-</sub> |  | 0.8<br><sub>0,1,0,1,-</sub> |  | 0.5<br><sub>0,2,1,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| AJ Johnson | 30% | 5.4<br><sub>-,-,3,-,-</sub> | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.5 | 0.9 | 0.9 |
| Julian Reese | 34% | 5.4<br><sub>-,-,3,-,-</sub> | 2.3<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.9 | 3.8 |

</details>


### POR @ LAL
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.7–115.4 | POR 37% | 2.73 / 1.58 | LAL -5.5 | 225.5 | LAL -2.5 covers 57%; o231.5 38% |
| Expected (weighted by chance each plays) | 110.7–115.9 | POR 36% | 2.79 / 1.56 | LAL -5.5 | 226.5 | LAL -2.5 covers 58%; o231.5 39% |
| if Sandro Mamukelashvili plays | 110.4–116.2 | POR 34% | 2.95 / 1.51 | LAL -6.5 | 226.5 | LAL -2.5 covers 60%; o231.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sandro Mamukelashvili (LAL) | Questionable | 55% | 20.4 | 8.4 | 4.4 | 1.5 | 0.9 | 0.8 | 0.5 | 0.8 | 14.4 | full tables below |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.4<br><sub>33,32,30,35,35</sub> | 23.3<br><sub>23,24,24,28,21</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>4,9,5,3,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.7<br><sub>9,7,2,5,12</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>4,0,2,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.4 | 3.8 | 36.5 |
| Damian Lillard | 98% | 33.0<br><sub>31,30,27,30,33</sub> | 19.2<br><sub>21,9,22,20,25</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,2,4,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,1,3,1,2</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.2 | 2.7 | 29.1 |
| Toumani Camara | 98% | 31.4<br><sub>24,26,31,31,32</sub> | 12.3<br><sub>12,13,14,9,11</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,2,4,5,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>4,3,4,3,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 1.5 | 18.3 |
| Jrue Holiday | 98% | 30.1<br><sub>30,24,22,31,28</sub> | 14.1<br><sub>22,6,14,17,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>4,6,4,8,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.3<br><sub>3,4,3,10,0</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,2,3,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 2.5 | 23.8 |
| Donovan Clingan | 98% | 26.7<br><sub>26,29,15,32,29</sub> | 11.5<br><sub>9,11,4,17,24</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 10.3<br><sub>10,8,9,18,11</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>2,1,0,1,1</sub> |  | 0.7 | 1.4 | 1.4 | 23.7 |
| Scoot Henderson | 98% | 25.8<br><sub>17,19,31,26,22</sub> | 11.8<br><sub>2,9,14,8,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,0,1,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,1,1,2,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.5 | 17.2 |
| Sidy Cissoko | 97% | 21.6<br><sub>20,19,19,22,21</sub> | 5.8<br><sub>6,4,1,8,7</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,6,3,3,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>4,2,1,0,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>0,0,0,2,1</sub> |  | 0.9 | 0.3 | 1.0 | 10.5 |
| Robert Williams III | 98% | 17.8<br><sub>21,-,14,15,16</sub> | 6.7<br><sub>14,-,3,2,9</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>10,-,3,6,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,-,1,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.9 | 0.9 | 14.5 |
| Chris Youngblood | 86% | 10.3<br><sub>-,-,7,15,4</sub> | 3.8<br><sub>-,-,3,7,0</sub> |  | 1.4<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.9 |
| Micah Potter | 64% | 7.8<br><sub>-,9,4,-,2</sub> | 3.2<br><sub>-,1,2,-,4</sub> |  | 2.1<br><sub>-,2,1,-,1</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.8 |
| Branden Carlson | 58% | 7.7<br><sub>-,12,4,-,3</sub> | 2.1<br><sub>-,2,0,-,2</sub> |  | 1.7<br><sub>-,2,2,-,0</sub> |  | 0.5<br><sub>-,1,1,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |
| Yang Hansen | 63% | 7.5<br><sub>-,5,13,-,2</sub> | 2.8<br><sub>-,3,6,-,0</sub> |  | 1.7<br><sub>-,2,5,-,0</sub> |  | 0.4<br><sub>-,1,1,-,0</sub> |  | 0.2<br><sub>-,1,2,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.9 |
| Jayson Kent | 71% | 6.6<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.9<br><sub>-,37,35,36,35</sub> | 34.4<br><sub>-,37,45,42,40</sub> | 34.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>-,7,15,7,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 7.8<br><sub>-,5,6,13,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>-,6,8,6,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.9 | 0.6 | 4.4 | 49.4 |
| Austin Reaves | 98% | 36.7<br><sub>31,37,39,34,37</sub> | 21.6<br><sub>16,21,19,27,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>6,4,3,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.2<br><sub>1,5,4,5,4</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.6 | 3.4 | 30.9 |
| Walker Kessler | 98% | 31.3<br><sub>26,31,31,32,29</sub> | 12.2<br><sub>11,10,16,15,15</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 11.3<br><sub>9,13,15,15,8</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>1,2,1,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.1 | 2.4 | 1.6 | 25.0 |
| Quentin Grimes | 98% | 25.0<br><sub>38,26,26,23,25</sub> | 8.1<br><sub>23,3,7,7,6</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>3,3,1,4,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>5,2,3,4,1</sub> |  | 0.8<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 0.3 | 1.2 | 13.1 |
| Ziaire Williams | 96% | 24.2<br><sub>-,-,-,15,23</sub> | 8.9<br><sub>-,-,-,9,10</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>-,-,-,2,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>-,-,-,2,1</sub> |  | 1.1<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.3 | 1.0 | 13.1 |
| Matisse Thybulle | 98% | 22.7<br><sub>28,28,25,19,23</sub> | 6.4<br><sub>15,10,6,6,3</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,3,2,1,1</sub> |  | 1.2<br><sub>0,0,3,2,2</sub> |  | 1.0<br><sub>4,1,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.8 | 0.8 | 0.8 | 9.7 |
| Jake LaRavia | 96% | 22.5<br><sub>35,28,25,26,21</sub> | 6.2<br><sub>2,10,8,7,9</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>10,2,2,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>0,0,4,2,2</sub> |  | 0.6<br><sub>0,2,2,1,2</sub> |  | 1.3 | 0.7 | 1.1 | 10.9 |
| Collin Sexton | 98% | 17.4<br><sub>21,16,19,16,16</sub> | 10.4<br><sub>21,0,14,6,10</sub> |  | 1.9<br><sub>4,2,3,1,3</sub> |  | 1.9<br><sub>2,1,3,5,1</sub> |  | 1.0<br><sub>4,0,1,0,1</sub> |  | 0.8 | 0.2 | 1.4 | 14.2 |
| Jarred Vanderbilt | 72% | 11.4<br><sub>21,13,12,6,7</sub> | 3.1<br><sub>0,0,4,2,0</sub> |  | 2.9<br><sub>7,3,3,1,1</sub> |  | 0.9<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 6.8 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Lawson Lovering | 91% | 8.0<br><sub>-,-,-,1,1</sub> | 2.4<br><sub>-,-,-,0,0</sub> |  | 2.2<br><sub>-,-,-,1,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 5.0 |
| Kevon Looney | 38% | 6.9<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.2 | 4.6 |
| Jaden Hardy | 80% | 6.7<br><sub>9,1,1,1,1</sub> | 3.4<br><sub>2,0,1,2,0</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.5<br><sub>2,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.0 | 0.4 | 4.5 |
| Adou Thiero | 16% | 6.7 | 2.2 |  | 1.6 |  | 0.4 |  | 0.0 |  | 0.2 | 0.1 | 0.5 | 4.3 |
| Chris Manon | 58% | 5.6<br><sub>-,1,-,-,-</sub> | 1.8<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.2 |

</details>

<details><summary>if Sandro Mamukelashvili plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 35.5<br><sub>-,37,35,36,35</sub> | 33.6<br><sub>-,37,45,42,40</sub> | 34.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>-,7,15,7,9</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 7.9<br><sub>-,5,6,13,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>-,6,8,6,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8 | 0.6 | 4.2 | 48.7 |
| Austin Reaves (LAL) | 98% | 34.7<br><sub>31,37,39,34,37</sub> | 20.7<br><sub>16,21,19,27,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,4,3,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>1,5,4,5,4</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.5 | 3.2 | 29.7 |
| Walker Kessler (LAL) | 98% | 28.7<br><sub>26,31,31,32,29</sub> | 11.9<br><sub>11,10,16,15,15</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 10.5<br><sub>9,13,15,15,8</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,2,1,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.2 | 1.5 | 23.9 |
| Quentin Grimes (LAL) | 98% | 23.2<br><sub>38,26,26,23,25</sub> | 7.5<br><sub>23,3,7,7,6</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,3,1,4,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>5,2,3,4,1</sub> |  | 0.8<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 0.3 | 1.1 | 12.3 |
| Ziaire Williams (LAL) | 96% | 21.5<br><sub>-,-,-,15,23</sub> | 7.7<br><sub>-,-,-,9,10</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>-,-,-,2,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>-,-,-,2,1</sub> |  | 0.9<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.3 | 0.9 | 11.5 |
| Sandro Mamukelashvili (LAL) | 100% | 20.4<br><sub>30,20,24,28,19</sub> | 8.4<br><sub>13,4,11,13,2</sub> | 7.5 · – | 4.4<br><sub>8,7,1,3,6</sub> | 4.5 | 1.5<br><sub>3,0,1,4,1</sub> |  | 0.9<br><sub>0,0,2,2,0</sub> | 0.5 | 0.8 | 0.5 | 0.8 | 14.4 |
| Matisse Thybulle (LAL) | 98% | 20.1<br><sub>28,28,25,19,23</sub> | 5.7<br><sub>15,10,6,6,3</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,3,2,1,1</sub> |  | 1.1<br><sub>0,0,3,2,2</sub> |  | 0.8<br><sub>4,1,2,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.7 | 0.7 | 0.8 | 8.7 |
| Jake LaRavia (LAL) | 96% | 20.0<br><sub>35,28,25,26,21</sub> | 5.5<br><sub>2,10,8,7,9</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>10,2,2,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.3<br><sub>0,0,4,2,2</sub> |  | 0.5<br><sub>0,2,2,1,2</sub> |  | 1.1 | 0.6 | 1.1 | 9.9 |
| Collin Sexton (LAL) | 98% | 16.6<br><sub>21,16,19,16,16</sub> | 9.9<br><sub>21,0,14,6,10</sub> |  | 1.9<br><sub>4,2,3,1,3</sub> |  | 1.8<br><sub>2,1,3,5,1</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 0.8 | 0.2 | 1.4 | 13.6 |
| Jarred Vanderbilt (LAL) | 72% | 9.2<br><sub>21,13,12,6,7</sub> | 2.7<br><sub>0,0,4,2,0</sub> |  | 2.4<br><sub>7,3,3,1,1</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 5.8 |
| Arthur Kaluma (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| AK Okereke (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Lawson Lovering (LAL) | 91% | 6.8<br><sub>-,-,-,1,1</sub> | 2.1<br><sub>-,-,-,0,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.4 |
| Jaden Hardy (LAL) | 80% | 6.4<br><sub>9,1,1,1,1</sub> | 3.4<br><sub>2,0,1,2,0</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.5<br><sub>2,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.0 | 0.4 | 4.5 |
| Kevon Looney (LAL) | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.3 |
| Adou Thiero (LAL) | 16% | 5.5 | 1.9 |  | 1.4 |  | 0.4 |  | 0.0 |  | 0.2 | 0.1 | 0.4 | 3.8 |
| Chris Manon (LAL) | 58% | 5.3<br><sub>-,1,-,-,-</sub> | 1.8<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.1 |
| Deni Avdija (POR) | 98% | 34.4<br><sub>33,32,30,35,35</sub> | 23.3<br><sub>23,24,24,28,21</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>4,9,5,3,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.6<br><sub>9,7,2,5,12</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>4,0,2,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.4 | 3.8 | 36.5 |
| Damian Lillard (POR) | 98% | 32.9<br><sub>31,30,27,30,33</sub> | 19.1<br><sub>21,9,22,20,25</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,2,4,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,1,3,1,2</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.2 | 2.7 | 28.9 |
| Toumani Camara (POR) | 98% | 31.4<br><sub>24,26,31,31,32</sub> | 12.2<br><sub>12,13,14,9,11</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,2,4,5,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>4,3,4,3,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 1.5 | 18.2 |
| Jrue Holiday (POR) | 98% | 30.2<br><sub>30,24,22,31,28</sub> | 14.1<br><sub>22,6,14,17,15</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>4,6,4,8,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.4<br><sub>3,4,3,10,0</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,2,3,5</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 2.5 | 23.9 |
| Donovan Clingan (POR) | 98% | 26.7<br><sub>26,29,15,32,29</sub> | 11.5<br><sub>9,11,4,17,24</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 10.3<br><sub>10,8,9,18,11</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>2,1,0,1,1</sub> |  | 0.7 | 1.4 | 1.4 | 23.7 |
| Scoot Henderson (POR) | 98% | 25.8<br><sub>17,19,31,26,22</sub> | 11.8<br><sub>2,9,14,8,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,0,1,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,1,1,2,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.5 | 17.2 |
| Sidy Cissoko (POR) | 97% | 21.6<br><sub>20,19,19,22,21</sub> | 5.8<br><sub>6,4,1,8,7</sub> | 5.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,6,3,3,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>4,2,1,0,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6<br><sub>0,0,0,2,1</sub> |  | 0.9 | 0.3 | 1.0 | 10.6 |
| Robert Williams III (POR) | 98% | 17.8<br><sub>21,-,14,15,16</sub> | 6.7<br><sub>14,-,3,2,9</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>10,-,3,6,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,-,1,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.8 | 1.0 | 0.9 | 14.5 |
| Chris Youngblood (POR) | 86% | 10.2<br><sub>-,-,7,15,4</sub> | 3.8<br><sub>-,-,3,7,0</sub> |  | 1.4<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |
| Micah Potter (POR) | 64% | 7.9<br><sub>-,9,4,-,2</sub> | 3.3<br><sub>-,1,2,-,4</sub> |  | 2.1<br><sub>-,2,1,-,1</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.8 |
| Branden Carlson (POR) | 58% | 7.7<br><sub>-,12,4,-,3</sub> | 2.1<br><sub>-,2,0,-,2</sub> |  | 1.7<br><sub>-,2,2,-,0</sub> |  | 0.5<br><sub>-,1,1,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 4.3 |
| Yang Hansen (POR) | 63% | 7.4<br><sub>-,5,13,-,2</sub> | 2.8<br><sub>-,3,6,-,0</sub> |  | 1.7<br><sub>-,2,5,-,0</sub> |  | 0.4<br><sub>-,1,1,-,0</sub> |  | 0.2<br><sub>-,1,2,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 4.9 |
| Jayson Kent (POR) | 71% | 6.6<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |

</details>


### SAS @ SAC
Out: Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 32.7<br><sub>27,39,34,24,34</sub> | 28.3<br><sub>29,36,43,12,52</sub> | 27.5 · –<br><sub>o 51% · u 49%</sub> | 11.3<br><sub>10,14,7,11,24</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,5,4,5,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>0,4,3,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 3.9 | 2.5 | 43.0 |
| Dylan Harper | 98% | 32.5<br><sub>30,37,39,27,36</sub> | 17.0<br><sub>13,13,25,17,21</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>6,5,7,7,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 4.7<br><sub>6,8,6,8,0</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.4 | 1.9 | 27.4 |
| Devin Vassell | 98% | 32.5<br><sub>24,38,34,25,36</sub> | 13.6<br><sub>14,21,9,11,2</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>4,5,5,2,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>8,2,2,1,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>4,1,0,0,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.5 | 1.1 | 21.0 |
| De'Aaron Fox | 98% | 31.6<br><sub>26,39,35,22,33</sub> | 16.0<br><sub>11,14,22,12,10</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>4,3,8,2,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>6,4,7,3,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>2,1,0,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.4 | 2.1 | 26.1 |
| Stephon Castle | 98% | 30.9<br><sub>27,38,22,26,35</sub> | 17.0<br><sub>15,14,0,16,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,6,5,5,10</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>5,8,4,4,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.3 | 2.9 | 28.6 |
| Julian Champagnie | 98% | 25.5<br><sub>25,31,27,22,21</sub> | 9.3<br><sub>26,6,12,8,0</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>3,6,3,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,0,1,0,3</sub> |  | 1.8<br><sub>8,2,3,2,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.5 | 0.8 | 15.2 |
| Keldon Johnson | 98% | 21.3<br><sub>22,23,24,27,19</sub> | 9.3<br><sub>14,9,2,15,4</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,0,1,2</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 15.1 |
| Luke Kornet | 98% | 14.7<br><sub>17,14,14,17,14</sub> | 3.9<br><sub>0,1,2,8,2</sub> |  | 4.4<br><sub>4,6,8,5,1</sub> |  | 1.0<br><sub>1,1,0,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.3 |
| Harrison Barnes | 67% | 13.4<br><sub>14,-,-,21,13</sub> | 4.8<br><sub>3,-,-,13,4</sub> |  | 1.6<br><sub>0,-,-,0,2</sub> |  | 0.7<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>0,-,-,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.1 |
| Carter Bryant | 72% | 9.4<br><sub>17,5,11,14,-</sub> | 3.3<br><sub>1,3,6,3,-</sub> |  | 1.6<br><sub>1,0,0,0,-</sub> |  | 0.6<br><sub>2,0,0,0,-</sub> |  | 0.3<br><sub>0,1,2,1,-</sub> |  | 0.2 | 0.3 | 0.3 | 5.5 |
| Jordan McLaughlin | 48% | 7.2<br><sub>7,-,-,8,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 1.3<br><sub>2,-,-,3,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.7 |
| Tarris Reed Jr. | 52% | 7.0<br><sub>5,-,-,7,-</sub> | 2.9<br><sub>4,-,-,4,-</sub> |  | 4.1<br><sub>5,-,-,7,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.5 | 7.3 |
| David Jones Garcia | 48% | 5.8<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.8 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 97% | 36.3<br><sub>33,41,37,37,42</sub> | 23.5<br><sub>19,34,38,25,22</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>3,6,5,5,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>5,14,5,6,12</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,3,9,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.3 | 3.2 | 34.9 |
| Domantas Sabonis | 98% | 32.9<br><sub>37,40,38,31,35</sub> | 14.9<br><sub>20,9,11,9,16</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 12.6<br><sub>14,15,14,7,17</sub> | 13.5<br><sub>o 46% · u 54%</sub> | 5.4<br><sub>8,7,8,4,1</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.3 | 2.4 | 32.9 |
| Zach LaVine | 98% | 32.0<br><sub>31,39,21,28,35</sub> | 18.4<br><sub>22,21,11,23,21</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>3,3,0,4,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>3,5,1,1,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>3,3,0,5,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 2.4 | 24.4 |
| De'Andre Hunter | 98% | 30.5<br><sub>33,37,32,36,38</sub> | 13.4<br><sub>24,24,19,6,14</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>6,5,3,7,2</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,1,0,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>5,4,2,0,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.4 | 19.6 |
| Precious Achiuwa | 98% | 25.8<br><sub>14,41,25,27,17</sub> | 10.9<br><sub>4,24,6,6,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>1,9,5,10,3</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>0,2,1,3,1</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 1.0 | 0.8 | 1.0 | 19.1 |
| Malik Monk | 98% | 19.2<br><sub>13,8,14,30,24</sub> | 10.0<br><sub>3,2,8,24,13</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,1,0,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.1<br><sub>6,1,3,7,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>1,0,0,5,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.5 | 0.3 | 1.4 | 15.1 |
| Leaky Black | 58% | 18.4<br><sub>8,-,-,25,22</sub> | 4.8<br><sub>2,-,-,12,3</sub> |  | 3.0<br><sub>1,-,-,3,6</sub> |  | 0.9<br><sub>1,-,-,1,1</sub> |  | 0.6<br><sub>0,-,-,4,0</sub> |  | 0.7 | 0.4 | 0.5 | 8.8 |
| Dylan Cardwell | 96% | 14.5<br><sub>-,-,-,-,13</sub> | 4.0<br><sub>-,-,-,-,4</sub> |  | 5.3<br><sub>-,-,-,-,6</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.8 | 0.6 | 10.2 |
| Emanuel Sharp | 97% | 13.8<br><sub>20,18,24,20,10</sub> | 3.8<br><sub>5,0,2,9,3</sub> |  | 1.2<br><sub>0,0,1,3,1</sub> |  | 0.7<br><sub>2,0,1,1,2</sub> |  | 0.4<br><sub>1,0,0,3,1</sub> |  | 0.4 | 0.2 | 0.5 | 5.7 |
| Jonathan Mogbo | 48% | 12.0<br><sub>18,-,25,-,-</sub> | 3.8<br><sub>2,-,6,-,-</sub> |  | 1.9<br><sub>5,-,3,-,-</sub> |  | 0.6<br><sub>0,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |
| Nique Clifford | 91% | 8.2<br><sub>5,4,11,3,3</sub> | 3.3<br><sub>2,0,0,0,0</sub> |  | 1.2<br><sub>0,0,1,1,2</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Daeqwon Plowden | 86% | 8.0<br><sub>17,-,4,3,-</sub> | 2.6<br><sub>0,-,4,1,-</sub> |  | 1.0<br><sub>2,-,0,1,-</sub> |  | 0.3<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Alex Karaban | 52% | 7.5<br><sub>11,12,10,-,-</sub> | 2.6<br><sub>0,6,0,-,-</sub> |  | 1.0<br><sub>1,0,1,-,-</sub> |  | 0.4<br><sub>1,0,1,-,-</sub> |  | 0.2<br><sub>0,2,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.0 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-06/`._
