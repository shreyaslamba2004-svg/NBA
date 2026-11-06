# NBA model · Fri 06 Nov 2026 (US date)

Updated **Sat 07 Nov, 09:21 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-06/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

2 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| TOR @ MIL | player minutes | Jamison Battle projected 28 min; most in his last 10 games is 21 | minutes 28 vs 16 this season; teammates out: Leonard (~26 min a game) |
| UTA @ DAL | team points | DAL projected 126, market implies 116 | 38% of tonight's minutes go to players new to DAL since last season, and the team ratings still lean on last season; DAL out: Larrea, II | 37% of tonight's minutes go to players new to UTA since last season, and the team ratings still lean on last season; UTA out: Jr., Nurkic |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | SAS @ SAC | draftkings | 9.10 | 7.82 | 5.11 | 19.6% | 12.8% | 12.8% | +16.4% | +78.1% | 0.5% |
| CHA to win | BOS @ CHA | draftkings | 4.12 | 3.79 | 4.15 | 24.1% | 26.4% | 26.4% | +8.7% | -0.8% | 0.7% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| TOR to win | TOR @ MIL | draftkings | 1.54 | Scottie Barnes | 58.8% | 65.9% | +5.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| WAS @ ATL | Sat 07 Nov 11:00 | 114.1–118.1 | WAS 39% | 2.58 / 1.63 | ATL -4.5 | 232.5 | ATL -7.5 covers 41%; o228.5 58% |
| BOS @ CHA | Sat 07 Nov 11:00 | 110.8–100.9 | BOS 76% | 1.32 / 4.15 | CHA +9.5 | 211.5 | CHA +10.5 covers 52%; o208.5 57% |
| PHI @ CLE | Sat 07 Nov 11:30 | 113.4–112.4 | PHI 53% | 1.90 / 2.11 | CLE +1.5 | 225.5 | CLE +2.5 covers 53%; o231.5 37% |
| UTA @ DAL | Sat 07 Nov 12:00 | 115.1–125.7 | UTA 23% | 4.40 / 1.29 | DAL -10.5 | 240.5 | DAL -6.5 covers 62%; o225.5 80% |
| OKC @ MEM | Sat 07 Nov 12:00 | 116.2–112.3 | OKC 61% | 1.64 / 2.56 | MEM +4.5 | 228.5 | MEM +4.5 covers 51%; o223.5 61% |
| TOR @ MIL | Sat 07 Nov 12:00 | 115.3–112.2 | TOR 59% | 1.70 / 2.43 | MIL +3.5 | 227.5 | MIL +4.5 covers 53%; o229.5 46% |
| MIN @ NOP | Sat 07 Nov 12:00 | 117.9–118.4 | MIN 49% | 2.05 / 1.95 | NOP +0.5 | 236.5 | NOP +3.5 covers 60%; o230.5 62% |
| POR @ LAL | Sat 07 Nov 14:00 | 110.5–116.3 | POR 34% | 2.95 / 1.51 | LAL -6.5 | 226.5 | LAL -3.5 covers 57%; o231.5 39% |
| SAS @ SAC | Sat 07 Nov 14:00 | 120.9–108.3 | SAS 81% | 1.23 / 5.36 | SAC +12.5 | 228.5 | SAC +17.5 covers 63%; o231.5 45% |

### WAS @ ATL
Out: RayJ Dennis (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Jalen Johnson (ATL), Jock Landale (ATL), Asa Newell (ATL), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.1–118.1 | WAS 39% | 2.58 / 1.63 | ATL -4.5 | 232.5 | ATL -7.5 covers 41%; o228.5 58% |
| Expected (weighted by chance each plays) | 113.3–117.6 | WAS 38% | 2.63 / 1.61 | ATL -4.5 | 231.5 | ATL -7.5 covers 41%; o228.5 55% |
| if Anthony Davis plays | 112.5–117.1 | WAS 37% | 2.67 / 1.60 | ATL -4.5 | 229.5 | ATL -7.5 covers 42%; o228.5 52% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Doubtful | 20% | 7.7 | 2.9 | 2.0 | 0.4 | 0.1 | 0.3 | 0.2 | 0.5 | 5.3 | small |
| Anthony Davis (WAS) | Questionable | 55% | 33.8 | 22.3 | 11.6 | 2.6 | 0.7 | 1.2 | 1.9 | 2.2 | 36.4 | full tables below |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.2<br><sub>38,34,38,34,34</sub> | 22.1<br><sub>22,14,21,15,18</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>6,5,7,3,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 9.4<br><sub>10,8,9,9,6</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.2 | 4.2 | 35.0 |
| Kyshawn George | 98% | 34.0<br><sub>29,38,32,37,35</sub> | 18.4<br><sub>20,8,12,22,25</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>4,2,3,4,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>2,11,3,5,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,0,4,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 1.1 | 2.9 | 28.9 |
| AJ Dybantsa | 93% | 32.7<br><sub>-,27,30,33,32</sub> | 16.5<br><sub>-,19,17,21,9</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>-,2,8,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>-,2,1,2,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0<br><sub>-,1,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.4 | 2.0 | 24.9 |
| Bilal Coulibaly | 98% | 27.4<br><sub>29,27,22,33,23</sub> | 11.0<br><sub>3,17,1,7,6</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>5,2,5,1,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>1,0,1,2,2</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 1.2 | 0.9 | 1.4 | 17.1 |
| Alex Sarr | 97% | 26.7<br><sub>26,26,29,-,23</sub> | 13.0<br><sub>12,18,3,-,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>6,4,8,-,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>1,2,0,-,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>0,2,1,-,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.9 | 1.7 | 1.7 | 22.7 |
| Bub Carrington | 98% | 23.1<br><sub>28,20,20,19,19</sub> | 8.4<br><sub>6,3,9,3,0</sub> |  | 2.6<br><sub>0,1,4,4,1</sub> |  | 3.1<br><sub>3,3,2,4,2</sub> |  | 1.1<br><sub>2,0,3,1,0</sub> |  | 0.6 | 0.2 | 1.8 | 14.1 |
| Tre Johnson | 86% | 20.4<br><sub>23,-,13,22,14</sub> | 8.0<br><sub>7,-,4,4,3</sub> |  | 2.5<br><sub>3,-,2,3,2</sub> |  | 1.0<br><sub>2,-,0,0,0</sub> |  | 0.9<br><sub>1,-,0,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 11.5 |
| Deandre Ayton | 98% | 17.6<br><sub>12,12,17,24,11</sub> | 6.5<br><sub>0,10,3,4,5</sub> |  | 5.8<br><sub>4,3,3,6,4</sub> |  | 0.8<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.9 | 13.1 |
| Khris Middleton | 58% | 15.3<br><sub>13,23,5,-,-</sub> | 5.3<br><sub>0,4,0,-,-</sub> |  | 2.5<br><sub>1,3,0,-,-</sub> |  | 1.1<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.5 | 0.1 | 1.1 | 8.9 |
| Will Riley | 83% | 13.7<br><sub>4,-,1,4,13</sub> | 6.0<br><sub>2,-,0,0,0</sub> |  | 1.9<br><sub>0,-,0,0,0</sub> |  | 1.1<br><sub>0,-,0,1,0</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 1.0 | 8.9 |
| Anthony Gill | 35% | 13.2<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.6 | 8.1 |
| Tre Mann | 52% | 7.9<br><sub>-,-,1,-,3</sub> | 3.2<br><sub>-,-,0,-,2</sub> |  | 1.1<br><sub>-,-,0,-,0</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 5.1 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker | 98% | 32.8<br><sub>32,31,29,31,32</sub> | 24.1<br><sub>23,25,12,34,26</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.9<br><sub>1,1,1,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.6<br><sub>5,4,0,9,6</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.5 | 2.6 | 31.7 |
| Dyson Daniels | 98% | 32.2<br><sub>28,32,27,31,34</sub> | 12.9<br><sub>7,4,8,6,8</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>4,6,4,9,16</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>7,5,3,4,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.4 | 0.5 | 1.8 | 26.4 |
| Onyeka Okongwu | 98% | 32.1<br><sub>31,33,28,33,31</sub> | 16.5<br><sub>11,29,6,13,14</sub> |  | 8.8<br><sub>4,12,10,10,16</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>4,2,1,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>1,4,0,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 1.0 | 1.7 | 28.7 |
| Luguentz Dort | 98% | 30.2<br><sub>24,22,29,31,31</sub> | 10.8<br><sub>8,6,11,14,6</sub> |  | 3.9<br><sub>3,3,3,2,3</sub> |  | 2.0<br><sub>3,2,0,0,3</sub> |  | 1.7<br><sub>2,1,1,4,2</sub> |  | 1.1 | 0.4 | 0.9 | 16.8 |
| CJ McCollum | 98% | 29.7<br><sub>20,31,24,32,25</sub> | 19.9<br><sub>13,5,14,13,15</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>2,3,2,9,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.8<br><sub>1,8,2,12,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>1,0,2,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.6 | 2.4 | 28.3 |
| Aaron Wiggins | 96% | 26.7<br><sub>24,24,23,24,29</sub> | 13.5<br><sub>10,20,10,7,15</sub> |  | 3.8<br><sub>4,7,2,3,4</sub> |  | 2.3<br><sub>3,3,1,2,2</sub> |  | 2.0<br><sub>2,4,2,1,3</sub> |  | 1.1 | 0.5 | 1.4 | 19.6 |
| Kingston Flemings | 80% | 23.3<br><sub>28,16,25,-,23</sub> | 9.4<br><sub>23,2,12,-,14</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>5,1,2,-,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.1<br><sub>5,5,6,-,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>3,0,1,-,2</sub> |  | 0.9 | 0.4 | 1.6 | 18.0 |
| Zuby Ejiofor | 58% | 16.5<br><sub>-,-,-,15,17</sub> | 6.5<br><sub>-,-,-,3,11</sub> |  | 3.8<br><sub>-,-,-,5,3</sub> |  | 1.4<br><sub>-,-,-,2,2</sub> |  | 0.6<br><sub>-,-,-,1,1</sub> |  | 0.6 | 0.2 | 0.9 | 11.6 |
| Jalen Wilson | 76% | 15.1 | 6.2 |  | 2.5 |  | 1.2 |  | 0.6 |  | 0.4 | 0.1 | 0.8 | 10.0 |
| Corey Kispert | 67% | 15.0<br><sub>-,-,5,18,8</sub> | 8.1<br><sub>-,-,0,14,9</sub> |  | 1.9<br><sub>-,-,0,1,0</sub> |  | 1.4<br><sub>-,-,1,0,1</sub> |  | 1.1<br><sub>-,-,0,4,1</sub> |  | 0.3 | 0.2 | 0.8 | 11.3 |
| Dorian Finney-Smith | 43% | 8.1<br><sub>-,-,3,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>if Anthony Davis plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker (ATL) | 98% | 32.7<br><sub>32,31,29,31,32</sub> | 24.0<br><sub>23,25,12,34,26</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.9<br><sub>1,1,1,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.6<br><sub>5,4,0,9,6</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.5 | 2.6 | 31.6 |
| Dyson Daniels (ATL) | 98% | 32.3<br><sub>28,32,27,31,34</sub> | 12.9<br><sub>7,4,8,6,8</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>4,6,4,9,16</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>7,5,3,4,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.4 | 0.5 | 1.8 | 26.4 |
| Onyeka Okongwu (ATL) | 98% | 32.2<br><sub>31,33,28,33,31</sub> | 16.4<br><sub>11,29,6,13,14</sub> |  | 8.8<br><sub>4,12,10,10,16</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>4,2,1,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>1,4,0,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 1.0 | 1.7 | 28.7 |
| Luguentz Dort (ATL) | 98% | 30.2<br><sub>24,22,29,31,31</sub> | 10.8<br><sub>8,6,11,14,6</sub> |  | 3.9<br><sub>3,3,3,2,3</sub> |  | 2.0<br><sub>3,2,0,0,3</sub> |  | 1.6<br><sub>2,1,1,4,2</sub> |  | 1.1 | 0.4 | 0.9 | 16.6 |
| CJ McCollum (ATL) | 98% | 29.6<br><sub>20,31,24,32,25</sub> | 19.8<br><sub>13,5,14,13,15</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>2,3,2,9,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.8<br><sub>1,8,2,12,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>1,0,2,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.6 | 2.4 | 28.2 |
| Aaron Wiggins (ATL) | 96% | 26.8<br><sub>24,24,23,24,29</sub> | 13.5<br><sub>10,20,10,7,15</sub> |  | 3.8<br><sub>4,7,2,3,4</sub> |  | 2.3<br><sub>3,3,1,2,2</sub> |  | 2.0<br><sub>2,4,2,1,3</sub> |  | 1.1 | 0.5 | 1.5 | 19.5 |
| Kingston Flemings (ATL) | 80% | 23.3<br><sub>28,16,25,-,23</sub> | 9.4<br><sub>23,2,12,-,14</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>5,1,2,-,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>5,5,6,-,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>3,0,1,-,2</sub> |  | 0.9 | 0.4 | 1.6 | 17.9 |
| Zuby Ejiofor (ATL) | 58% | 16.3<br><sub>-,-,-,15,17</sub> | 6.4<br><sub>-,-,-,3,11</sub> |  | 3.7<br><sub>-,-,-,5,3</sub> |  | 1.3<br><sub>-,-,-,2,2</sub> |  | 0.5<br><sub>-,-,-,1,1</sub> |  | 0.6 | 0.2 | 0.9 | 11.4 |
| Jalen Wilson (ATL) | 76% | 15.1 | 6.1 |  | 2.5 |  | 1.2 |  | 0.6 |  | 0.4 | 0.1 | 0.8 | 9.8 |
| Corey Kispert (ATL) | 67% | 15.0<br><sub>-,-,5,18,8</sub> | 8.0<br><sub>-,-,0,14,9</sub> |  | 1.9<br><sub>-,-,0,1,0</sub> |  | 1.4<br><sub>-,-,1,0,1</sub> |  | 1.1<br><sub>-,-,0,4,1</sub> |  | 0.3 | 0.2 | 0.8 | 11.3 |
| Dorian Finney-Smith (ATL) | 43% | 8.1<br><sub>-,-,3,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Trae Young (WAS) | 98% | 34.2<br><sub>38,34,38,34,34</sub> | 19.2<br><sub>22,14,21,15,18</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>6,5,7,3,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 8.8<br><sub>10,8,9,9,6</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.2 | 3.8 | 31.2 |
| Anthony Davis (WAS) | 100% | 33.8<br><sub>36,34,34,34,30</sub> | 22.3<br><sub>29,18,25,27,26</sub> | 22.5 · – | 11.6<br><sub>10,5,13,9,10</sub> | 10.5 | 2.6<br><sub>0,3,1,1,3</sub> | 2.5 | 0.7<br><sub>3,2,0,1,0</sub> |  | 1.2 | 1.9 | 2.2 | 36.4 |
| Kyshawn George (WAS) | 98% | 32.4<br><sub>29,38,32,37,35</sub> | 15.7<br><sub>20,8,12,22,25</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>4,2,3,4,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>2,11,3,5,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,0,4,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 1.1 | 2.5 | 25.1 |
| AJ Dybantsa (WAS) | 93% | 30.6<br><sub>-,27,30,33,32</sub> | 14.5<br><sub>-,19,17,21,9</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>-,2,8,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>-,2,1,2,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9<br><sub>-,1,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.3 | 1.8 | 22.1 |
| Alex Sarr (WAS) | 97% | 24.9<br><sub>26,26,29,-,23</sub> | 11.4<br><sub>12,18,3,-,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>6,4,8,-,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>1,2,0,-,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>0,2,1,-,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.8 | 1.6 | 1.6 | 20.2 |
| Bilal Coulibaly (WAS) | 98% | 24.5<br><sub>29,27,22,33,23</sub> | 8.7<br><sub>3,17,1,7,6</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>5,2,5,1,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>1,0,1,2,2</sub> |  | 0.7<br><sub>0,1,0,0,0</sub> |  | 1.1 | 0.8 | 1.3 | 14.1 |
| Bub Carrington (WAS) | 98% | 18.6<br><sub>28,20,20,19,19</sub> | 5.8<br><sub>6,3,9,3,0</sub> |  | 2.1<br><sub>0,1,4,4,1</sub> |  | 2.5<br><sub>3,3,2,4,2</sub> |  | 0.8<br><sub>2,0,3,1,0</sub> |  | 0.5 | 0.2 | 1.5 | 10.3 |
| Tre Johnson (WAS) | 86% | 16.0<br><sub>23,-,13,22,14</sub> | 5.9<br><sub>7,-,4,4,3</sub> |  | 2.0<br><sub>3,-,2,3,2</sub> |  | 0.8<br><sub>2,-,0,0,0</sub> |  | 0.6<br><sub>1,-,0,0,1</sub> |  | 0.6 | 0.2 | 1.0 | 8.7 |
| Deandre Ayton (WAS) | 98% | 14.7<br><sub>12,12,17,24,11</sub> | 5.0<br><sub>0,10,3,4,5</sub> |  | 4.8<br><sub>4,3,3,6,4</sub> |  | 0.7<br><sub>2,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.7 | 10.5 |
| Will Riley (WAS) | 83% | 11.0<br><sub>4,-,1,4,13</sub> | 4.6<br><sub>2,-,0,0,0</sub> |  | 1.4<br><sub>0,-,0,0,0</sub> |  | 0.9<br><sub>0,-,0,1,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.1 | 0.8 | 6.8 |
| Khris Middleton (WAS) | 58% | 9.7<br><sub>13,23,5,-,-</sub> | 2.9<br><sub>0,4,0,-,-</sub> |  | 1.6<br><sub>1,3,0,-,-</sub> |  | 0.8<br><sub>0,2,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 5.3 |
| Anthony Gill (WAS) | 35% | 7.4<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Tre Mann (WAS) | 52% | 5.9<br><sub>-,-,1,-,3</sub> | 2.6<br><sub>-,-,0,-,2</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.1 |

</details>


### BOS @ CHA
Out: Moussa Diabate (CHA), PJ Hall (CHA), Kon Knueppel (CHA), Dennis Schroder (CHA), Grant Williams (CHA), Devin Carter (BOS)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 34.0<br><sub>42,35,34,32,-</sub> | 24.9<br><sub>40,26,32,19,-</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>5,7,4,6,-</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>8,7,7,9,-</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>2,2,1,1,-</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.4 | 2.7 | 38.6 |
| Derrick White | 98% | 31.4<br><sub>33,26,34,30,36</sub> | 13.0<br><sub>16,9,12,7,24</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>5,2,2,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>7,4,2,3,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.7 | 1.5 | 21.1 |
| Paul George | 98% | 31.4<br><sub>36,27,33,-,35</sub> | 17.7<br><sub>20,18,17,-,25</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>7,6,6,-,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>7,8,8,-,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>1,2,3,-,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.3 | 2.4 | 26.0 |
| Payton Pritchard | 98% | 26.0<br><sub>24,35,27,30,18</sub> | 12.4<br><sub>4,30,7,4,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,3,7,3,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.5<br><sub>6,3,3,3,5</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>0,3,0,0,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.1 | 1.0 | 18.9 |
| Neemias Queta | 98% | 23.7<br><sub>15,20,27,26,29</sub> | 8.9<br><sub>7,13,8,16,9</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>3,6,8,6,12</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>2,0,1,1,3</sub> |  | 0.1<br><sub>0,0,0,1,0</sub> |  | 0.7 | 1.2 | 1.0 | 16.9 |
| Sam Hauser | 98% | 22.1<br><sub>25,18,17,19,30</sub> | 7.5<br><sub>11,6,3,2,11</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>0,2,0,1,0</sub> |  | 1.4<br><sub>3,2,1,0,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.5 | 0.2 | 0.3 | 11.6 |
| Baylor Scheierman | 98% | 21.9<br><sub>21,23,20,27,29</sub> | 6.4<br><sub>3,2,10,11,9</sub> |  | 4.0<br><sub>4,3,2,5,11</sub> |  | 1.5<br><sub>1,3,1,2,1</sub> |  | 1.0<br><sub>1,0,2,3,3</sub> |  | 0.8 | 0.1 | 0.7 | 11.9 |
| Mitchell Robinson | 98% | 17.5<br><sub>25,19,-,15,20</sub> | 5.0<br><sub>7,11,-,4,3</sub> |  | 5.4<br><sub>5,4,-,4,10</sub> |  | 0.6<br><sub>0,0,-,0,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.8 | 0.8 | 11.0 |
| Luka Garza | 98% | 14.5<br><sub>13,7,21,18,18</sub> | 7.2<br><sub>2,5,12,14,11</sub> |  | 3.2<br><sub>4,1,6,3,5</sub> |  | 1.0<br><sub>0,1,4,0,2</sub> |  | 0.7<br><sub>0,0,2,4,3</sub> |  | 0.4 | 0.3 | 0.6 | 11.4 |
| Jordan Walsh | 98% | 13.6<br><sub>24,11,13,12,12</sub> | 3.7<br><sub>15,2,0,5,3</sub> |  | 2.9<br><sub>6,2,3,3,4</sub> |  | 0.7<br><sub>1,0,2,0,0</sub> |  | 0.4<br><sub>3,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.4 | 7.3 |
| Hugo Gonzalez | 96% | 12.8<br><sub>6,15,14,16,14</sub> | 3.6<br><sub>0,0,7,6,4</sub> |  | 2.6<br><sub>2,2,1,3,2</sub> |  | 0.5<br><sub>0,0,1,0,0</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.7 |
| Mike Conley | 48% | 6.9<br><sub>-,-,-,4,-</sub> | 2.1<br><sub>-,-,-,3,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 1.0<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,1,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.8 |
| Ron Harper Jr. | 52% | 6.6<br><sub>-,3,-,7,-</sub> | 2.8<br><sub>-,0,-,0,-</sub> |  | 1.0<br><sub>-,0,-,1,-</sub> |  | 0.4<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.2 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 34.5<br><sub>38,37,33,31,26</sub> | 22.0<br><sub>31,19,24,17,10</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>12,7,5,1,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>3,2,5,4,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>3,3,5,3,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.6 | 2.8 | 30.2 |
| Naz Reid | 98% | 34.0<br><sub>13,31,36,27,36</sub> | 17.7<br><sub>7,12,14,13,28</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 8.0<br><sub>6,11,5,6,9</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>0,1,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.5<br><sub>1,2,0,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.8 | 2.4 | 28.1 |
| Grayson Allen | 97% | 30.4<br><sub>30,21,30,19,27</sub> | 14.9<br><sub>9,5,27,11,22</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>5,3,4,1,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,2,3,0,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>2,1,7,3,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 1.8 | 21.4 |
| Sion James | 98% | 29.9<br><sub>23,29,18,21,31</sub> | 7.9<br><sub>5,6,4,11,10</sub> |  | 4.4<br><sub>2,5,2,4,2</sub> |  | 2.8<br><sub>3,4,1,3,1</sub> |  | 1.3<br><sub>1,1,0,3,0</sub> |  | 0.8 | 0.2 | 1.1 | 15.1 |
| Royce O'Neale | 98% | 25.6<br><sub>34,17,23,18,18</sub> | 6.9<br><sub>9,7,8,2,0</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,3,6,4,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>0,1,1,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,2,1,0,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.4 | 0.8 | 12.8 |
| Coby White | 97% | 24.1<br><sub>-,-,-,16,18</sub> | 14.6<br><sub>-,-,-,7,4</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>-,-,-,0,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>-,-,-,1,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 2.0 | 21.2 |
| Ryan Kalkbrenner | 98% | 22.1<br><sub>13,15,19,16,19</sub> | 5.6<br><sub>1,2,6,4,6</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>1,4,3,6,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,0,4,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.4 | 0.8 | 12.2 |
| Tidjane Salaun | 91% | 19.1<br><sub>12,9,12,19,10</sub> | 6.2<br><sub>2,6,5,1,9</sub> |  | 4.4<br><sub>2,2,2,7,1</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 0.9<br><sub>0,2,1,0,3</sub> |  | 0.4 | 0.2 | 0.7 | 11.5 |
| Christian Anderson | 72% | 16.1<br><sub>9,14,8,9,-</sub> | 5.9<br><sub>2,4,2,8,-</sub> |  | 2.1<br><sub>0,3,0,2,-</sub> |  | 2.0<br><sub>1,3,0,2,-</sub> |  | 0.6<br><sub>0,0,0,1,-</sub> |  | 0.5 | 0.3 | 1.0 | 10.0 |
| Liam McNeeley | 52% | 13.1<br><sub>-,3,-,9,-</sub> | 4.2<br><sub>-,0,-,3,-</sub> |  | 2.6<br><sub>-,2,-,0,-</sub> |  | 0.8<br><sub>-,0,-,1,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 7.6 |
| Hannes Steinbach | 48% | 11.5<br><sub>-,2,-,9,-</sub> | 3.6<br><sub>-,0,-,2,-</sub> |  | 2.6<br><sub>-,0,-,2,-</sub> |  | 0.6<br><sub>-,0,-,1,-</sub> |  | 0.1<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 6.8 |

</details>


### PHI @ CLE
Out: Jaylon Tyson (CLE), Dominick Barlow (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.4–112.4 | PHI 53% | 1.90 / 2.11 | CLE +1.5 | 225.5 | CLE +2.5 covers 53%; o231.5 37% |
| Expected (weighted by chance each plays) | 112.7–113.6 | PHI 47% | 2.12 / 1.89 | CLE -1.5 | 226.5 | CLE +2.5 covers 59%; o231.5 39% |
| if Jarrett Allen plays | 112.9–112.8 | PHI 50% | 2.00 / 2.00 | CLE +0.5 | 225.5 | CLE +2.5 covers 56%; o231.5 37% |
| if Peyton Watson plays | 113.2–112.7 | PHI 51% | 1.95 / 2.05 | CLE +0.5 | 225.5 | CLE +2.5 covers 55%; o231.5 38% |
| if Tyrese Proctor plays | 113.6–112.3 | PHI 53% | 1.87 / 2.15 | CLE +1.5 | 225.5 | CLE +2.5 covers 53%; o231.5 38% |

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
| Tyrese Maxey | 98% | 38.0<br><sub>36,38,38,36,34</sub> | 22.8<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.6 | 0.5 | 2.2 | 32.0 |
| Jaylen Brown | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.7<br><sub>20,-,16,25,30</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.4 | 2.8 | 32.0 |
| LeBron James | 98% | 35.2<br><sub>33,34,-,31,33</sub> | 17.9<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.5 | 2.6 | 31.6 |
| VJ Edgecombe | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.4<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 1.3 | 21.5 |
| Joel Embiid | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.4<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.0 | 2.9 | 34.8 |
| Dean Wade | 91% | 22.2<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.2<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.5 | 8.1 |
| Anfernee Simons | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.5 | 0.1 | 0.7 | 11.5 |
| Kentavious Caldwell-Pope | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> |  | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.5 |
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
| James Harden | 98% | 36.9<br><sub>34,36,26,33,35</sub> | 21.8<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 6.9<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 4.0 | 34.0 |
| Donovan Mitchell | 98% | 36.9<br><sub>31,33,24,36,33</sub> | 28.5<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.3<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.4 | 3.3 | 39.1 |
| Evan Mobley | 98% | 35.8<br><sub>32,33,25,33,33</sub> | 20.1<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 9.7<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.8 | 2.1 | 33.8 |
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
| James Harden (CLE) | 98% | 36.9<br><sub>34,36,26,33,35</sub> | 19.6<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 7.1<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 3.9 | 31.9 |
| Donovan Mitchell (CLE) | 98% | 36.9<br><sub>31,33,24,36,33</sub> | 25.9<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.5<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4 | 0.4 | 3.3 | 36.7 |
| Evan Mobley (CLE) | 98% | 35.4<br><sub>32,33,25,33,33</sub> | 18.4<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.9 | 2.0 | 32.0 |
| Sam Merrill (CLE) | 98% | 28.6<br><sub>20,27,19,26,27</sub> | 11.1<br><sub>8,16,6,8,10</sub> |  | 3.1<br><sub>1,2,4,3,7</sub> |  | 2.2<br><sub>1,3,3,2,1</sub> |  | 2.1<br><sub>2,4,1,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 16.4 |
| Jarrett Allen (CLE) | 100% | 27.3<br><sub>30,30,24,28,7</sub> | 13.2<br><sub>8,14,25,14,0</sub> | 13.5 · – | 8.4<br><sub>12,8,11,6,1</sub> | 7.5 | 1.5<br><sub>2,1,4,1,0</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.8 | 1.4 | 1.3 | 23.1 |
| Meleek Thomas (CLE) | 84% | 23.9<br><sub>20,-,23,26,18</sub> | 10.2<br><sub>10,-,13,17,9</sub> |  | 2.9<br><sub>4,-,1,5,1</sub> |  | 1.2<br><sub>1,-,2,1,0</sub> |  | 1.7<br><sub>0,-,3,3,3</sub> |  | 0.8 | 0.3 | 1.2 | 14.3 |
| Mario Hezonja (CLE) | 97% | 23.6<br><sub>17,17,20,27,23</sub> | 8.9<br><sub>5,10,8,12,12</sub> |  | 6.0<br><sub>3,6,11,8,8</sub> |  | 1.9<br><sub>2,2,4,3,1</sub> |  | 1.2<br><sub>1,2,1,3,2</sub> |  | 0.7 | 0.3 | 1.0 | 16.9 |
| Craig Porter Jr. (CLE) | 80% | 15.1<br><sub>-,4,16,8,14</sub> | 3.4<br><sub>-,0,2,0,0</sub> |  | 2.8<br><sub>-,1,2,4,1</sub> |  | 2.2<br><sub>-,0,4,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.5 | 0.9 | 8.3 |
| Tristan Enaruna (CLE) | 52% | 14.8<br><sub>-,-,6,-,16</sub> | 5.2<br><sub>-,-,2,-,4</sub> |  | 2.7<br><sub>-,-,1,-,4</sub> |  | 1.0<br><sub>-,-,0,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.8 |
| Thomas Bryant (CLE) | 58% | 13.2<br><sub>-,-,11,5,13</sub> | 6.1<br><sub>-,-,11,4,8</sub> |  | 3.4<br><sub>-,-,2,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.7<br><sub>-,-,3,0,1</sub> |  | 0.3 | 0.5 | 0.6 | 10.0 |
| Norchad Omier (CLE) | 16% | 9.3 | 3.1 |  | 2.1 |  | 0.7 |  | 0.2 |  | 0.3 | 0.2 | 0.7 | 5.9 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Tyrese Maxey (PHI) | 98% | 38.0<br><sub>36,38,38,36,34</sub> | 23.0<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.6 | 0.5 | 2.2 | 32.2 |
| Jaylen Brown (PHI) | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.6<br><sub>20,-,16,25,30</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.4 | 2.8 | 31.9 |
| LeBron James (PHI) | 98% | 35.2<br><sub>33,34,-,31,33</sub> | 17.8<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.5 | 2.6 | 31.5 |
| VJ Edgecombe (PHI) | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.3<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 1.4 | 21.5 |
| Joel Embiid (PHI) | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.4<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 0.9 | 2.9 | 34.8 |
| Dean Wade (PHI) | 91% | 22.2<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.3<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.6 | 8.0 |
| Anfernee Simons (PHI) | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.5 | 0.1 | 0.7 | 11.5 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> |  | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.5 |
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
| James Harden (CLE) | 98% | 36.6<br><sub>34,36,26,33,35</sub> | 19.2<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 6.8<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 3.7 | 31.4 |
| Donovan Mitchell (CLE) | 98% | 36.5<br><sub>31,33,24,36,33</sub> | 25.5<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.2<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.3 | 3.0 | 36.0 |
| Evan Mobley (CLE) | 98% | 35.6<br><sub>32,33,25,33,33</sub> | 18.1<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 9.8<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.9 | 1.9 | 31.8 |
| Peyton Watson (CLE) | 100% | 30.0<br><sub>28,22,22,-,-</sub> | 13.3<br><sub>22,4,5,-,-</sub> | 10.5 · – | 4.8<br><sub>6,4,2,-,-</sub> | 3.5 | 2.4<br><sub>2,3,6,-,-</sub> | 1.5 | 1.3<br><sub>1,0,1,-,-</sub> | 1.5 | 0.9 | 1.5 | 1.9 | 20.6 |
| Sam Merrill (CLE) | 98% | 27.9<br><sub>20,27,19,26,27</sub> | 10.6<br><sub>8,16,6,8,10</sub> |  | 3.1<br><sub>1,2,4,3,7</sub> |  | 2.1<br><sub>1,3,3,2,1</sub> |  | 2.0<br><sub>2,4,1,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 15.8 |
| Mario Hezonja (CLE) | 97% | 22.9<br><sub>17,17,20,27,23</sub> | 8.8<br><sub>5,10,8,12,12</sub> |  | 6.0<br><sub>3,6,11,8,8</sub> |  | 1.8<br><sub>2,2,4,3,1</sub> |  | 1.2<br><sub>1,2,1,3,2</sub> |  | 0.6 | 0.3 | 1.0 | 16.6 |
| Meleek Thomas (CLE) | 84% | 22.8<br><sub>20,-,23,26,18</sub> | 10.2<br><sub>10,-,13,17,9</sub> |  | 2.9<br><sub>4,-,1,5,1</sub> |  | 1.1<br><sub>1,-,2,1,0</sub> |  | 1.6<br><sub>0,-,3,3,3</sub> |  | 0.8 | 0.3 | 1.2 | 14.2 |
| Tristan Enaruna (CLE) | 52% | 14.6<br><sub>-,-,6,-,16</sub> | 5.2<br><sub>-,-,2,-,4</sub> |  | 2.6<br><sub>-,-,1,-,4</sub> |  | 0.9<br><sub>-,-,0,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.8 |
| Craig Porter Jr. (CLE) | 80% | 14.4<br><sub>-,4,16,8,14</sub> | 3.2<br><sub>-,0,2,0,0</sub> |  | 2.7<br><sub>-,1,2,4,1</sub> |  | 2.1<br><sub>-,0,4,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.4 | 0.8 | 8.1 |
| Thomas Bryant (CLE) | 58% | 13.9<br><sub>-,-,11,5,13</sub> | 6.6<br><sub>-,-,11,4,8</sub> |  | 3.6<br><sub>-,-,2,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.7<br><sub>-,-,3,0,1</sub> |  | 0.3 | 0.6 | 0.6 | 10.8 |
| Ernest Udeh Jr. (CLE) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Norchad Omier (CLE) | 16% | 8.2 | 2.9 |  | 1.8 |  | 0.6 |  | 0.1 |  | 0.3 | 0.2 | 0.6 | 5.4 |
| Tyrese Maxey (PHI) | 98% | 37.9<br><sub>36,38,38,36,34</sub> | 22.9<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.6 | 0.5 | 2.2 | 32.0 |
| Jaylen Brown (PHI) | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.7<br><sub>20,-,16,25,30</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.4 | 2.8 | 32.0 |
| LeBron James (PHI) | 98% | 35.1<br><sub>33,34,-,31,33</sub> | 17.9<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.5 | 2.6 | 31.6 |
| VJ Edgecombe (PHI) | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.3<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 1.3 | 21.4 |
| Joel Embiid (PHI) | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.4<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 9.2<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.0 | 2.9 | 34.8 |
| Dean Wade (PHI) | 91% | 22.1<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.2<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.5 | 8.1 |
| Anfernee Simons (PHI) | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.5 | 0.1 | 0.7 | 11.4 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> |  | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.5 |
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
| James Harden (CLE) | 98% | 36.8<br><sub>34,36,26,33,35</sub> | 20.0<br><sub>16,24,13,14,19</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>2,5,6,4,9</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 6.8<br><sub>6,4,7,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,3,3,3,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 3.8 | 32.1 |
| Donovan Mitchell (CLE) | 98% | 36.6<br><sub>31,33,24,36,33</sub> | 26.1<br><sub>19,22,15,17,27</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,3,4,5,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.1<br><sub>7,3,3,11,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>2,1,2,4,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.4 | 3.2 | 36.5 |
| Evan Mobley (CLE) | 98% | 35.8<br><sub>32,33,25,33,33</sub> | 19.1<br><sub>24,11,27,16,16</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 9.9<br><sub>12,4,5,7,10</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>2,7,3,4,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>5,0,3,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 2.0 | 2.1 | 32.9 |
| Sam Merrill (CLE) | 98% | 28.6<br><sub>20,27,19,26,27</sub> | 10.7<br><sub>8,16,6,8,10</sub> |  | 3.1<br><sub>1,2,4,3,7</sub> |  | 2.2<br><sub>1,3,3,2,1</sub> |  | 2.0<br><sub>2,4,1,2,2</sub> |  | 0.7 | 0.2 | 0.8 | 16.0 |
| Meleek Thomas (CLE) | 84% | 24.5<br><sub>20,-,23,26,18</sub> | 10.8<br><sub>10,-,13,17,9</sub> |  | 3.2<br><sub>4,-,1,5,1</sub> |  | 1.2<br><sub>1,-,2,1,0</sub> |  | 1.8<br><sub>0,-,3,3,3</sub> |  | 0.9 | 0.3 | 1.2 | 15.1 |
| Mario Hezonja (CLE) | 97% | 24.0<br><sub>17,17,20,27,23</sub> | 8.9<br><sub>5,10,8,12,12</sub> |  | 6.0<br><sub>3,6,11,8,8</sub> |  | 1.9<br><sub>2,2,4,3,1</sub> |  | 1.2<br><sub>1,2,1,3,2</sub> |  | 0.7 | 0.3 | 1.0 | 16.8 |
| Tyrese Proctor (CLE) | 100% | 23.6<br><sub>6,20,18,19,22</sub> | 9.5<br><sub>2,7,9,10,11</sub> |  | 3.4<br><sub>1,6,4,4,1</sub> |  | 2.8<br><sub>1,2,5,2,0</sub> |  | 1.4<br><sub>0,1,3,2,2</sub> |  | 0.9 | 0.1 | 1.1 | 15.7 |
| Craig Porter Jr. (CLE) | 80% | 15.5<br><sub>-,4,16,8,14</sub> | 3.6<br><sub>-,0,2,0,0</sub> |  | 2.9<br><sub>-,1,2,4,1</sub> |  | 2.2<br><sub>-,0,4,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.6 | 0.5 | 0.9 | 8.7 |
| Tristan Enaruna (CLE) | 52% | 15.0<br><sub>-,-,6,-,16</sub> | 5.4<br><sub>-,-,2,-,4</sub> |  | 2.7<br><sub>-,-,1,-,4</sub> |  | 0.9<br><sub>-,-,0,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 9.0 |
| Thomas Bryant (CLE) | 58% | 14.6<br><sub>-,-,11,5,13</sub> | 6.8<br><sub>-,-,11,4,8</sub> |  | 3.8<br><sub>-,-,2,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,3,0,1</sub> |  | 0.3 | 0.6 | 0.6 | 11.1 |
| Norchad Omier (CLE) | 16% | 8.9 | 3.0 |  | 2.0 |  | 0.7 |  | 0.2 |  | 0.3 | 0.2 | 0.6 | 5.7 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Tyrese Maxey (PHI) | 98% | 38.0<br><sub>36,38,38,36,34</sub> | 22.9<br><sub>27,27,38,26,19</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>5,4,4,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>4,4,4,11,7</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>3,3,4,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.6 | 0.5 | 2.2 | 32.0 |
| Jaylen Brown (PHI) | 98% | 36.5<br><sub>34,-,38,33,37</sub> | 21.7<br><sub>20,-,16,25,30</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>10,-,4,11,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>2,-,4,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,-,0,4,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.4 | 2.8 | 32.0 |
| LeBron James (PHI) | 98% | 35.1<br><sub>33,34,-,31,33</sub> | 17.9<br><sub>13,20,-,15,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,9,-,7,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>10,8,-,9,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,2,-,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.5 | 2.6 | 31.5 |
| VJ Edgecombe (PHI) | 91% | 34.3<br><sub>29,36,37,33,35</sub> | 12.4<br><sub>8,13,10,21,11</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>7,8,8,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,2,3,5,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,1,2,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 1.4 | 21.5 |
| Joel Embiid (PHI) | 98% | 34.2<br><sub>39,33,-,25,33</sub> | 21.5<br><sub>21,10,-,15,26</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 9.1<br><sub>11,7,-,8,15</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>2,7,-,3,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.0 | 2.9 | 34.9 |
| Dean Wade (PHI) | 91% | 22.1<br><sub>17,27,30,23,22</sub> | 3.5<br><sub>0,0,4,8,3</sub> |  | 3.3<br><sub>1,2,5,2,5</sub> |  | 1.2<br><sub>1,1,10,1,1</sub> |  | 0.5<br><sub>0,0,0,2,0</sub> |  | 0.9 | 0.3 | 0.6 | 8.1 |
| Anfernee Simons (PHI) | 98% | 19.9<br><sub>27,31,25,24,10</sub> | 8.4<br><sub>20,21,19,6,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>3,2,0,2,1</sub> |  | 1.3<br><sub>1,1,2,1,0</sub> |  | 1.4<br><sub>6,5,5,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.5 | 0.1 | 0.7 | 11.5 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.8<br><sub>21,21,18,13,21</sub> | 4.5<br><sub>4,5,3,3,5</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,3,2,1,1</sub> |  | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.6 | 7.6 |
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
| Keyonte George | 98% | 32.6<br><sub>33,37,29,22,44</sub> | 23.5<br><sub>26,31,8,7,39</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,4,3,7,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>6,3,4,0,9</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>0,5,0,1,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.1 | 3.3 | 33.4 |
| Lauri Markkanen | 98% | 31.5<br><sub>6,-,29,31,39</sub> | 22.4<br><sub>2,-,13,22,21</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>0,-,6,8,10</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>0,-,1,3,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.4<br><sub>0,-,2,4,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.5 | 1.8 | 31.6 |
| Ace Bailey | 98% | 31.2<br><sub>34,40,37,24,35</sub> | 15.0<br><sub>17,19,9,5,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>10,6,7,6,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>3,0,1,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.0<br><sub>3,1,1,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 1.0 | 1.7 | 23.3 |
| Darryn Peterson | 97% | 30.0<br><sub>26,26,36,33,30</sub> | 12.8<br><sub>14,18,16,14,7</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>7,5,4,4,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.0<br><sub>4,3,4,6,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>3,3,3,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.6 | 1.6 | 21.0 |
| Jaxson Hayes | 98% | 22.3<br><sub>-,37,20,22,21</sub> | 7.6<br><sub>-,2,7,9,2</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>-,11,7,5,7</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>-,4,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.0 | 14.7 |
| Josh Okogie | 91% | 19.1<br><sub>21,28,14,19,26</sub> | 4.0<br><sub>0,5,0,9,3</sub> |  | 3.5<br><sub>2,9,1,3,6</sub> |  | 1.1<br><sub>0,3,0,2,1</sub> |  | 0.4<br><sub>0,1,0,1,1</sub> |  | 0.8 | 0.3 | 0.7 | 8.6 |
| Brice Sensabaugh | 98% | 16.3<br><sub>9,18,19,14,12</sub> | 10.0<br><sub>11,16,12,7,6</sub> |  | 2.7<br><sub>2,3,3,2,2</sub> |  | 1.3<br><sub>0,1,2,1,0</sub> |  | 1.3<br><sub>3,4,2,1,1</sub> |  | 0.5 | 0.1 | 1.4 | 14.1 |
| Svi Mykhailiuk | 91% | 16.2<br><sub>13,15,18,14,17</sub> | 6.2<br><sub>0,3,6,3,6</sub> |  | 2.1<br><sub>1,2,1,2,3</sub> |  | 1.2<br><sub>0,1,3,0,0</sub> |  | 0.9<br><sub>0,1,2,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 9.4 |
| Josh Green | 88% | 16.1<br><sub>25,24,2,15,23</sub> | 3.2<br><sub>6,2,0,3,7</sub> |  | 1.8<br><sub>4,2,0,1,1</sub> |  | 0.8<br><sub>1,2,0,0,0</sub> |  | 0.3<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 5.8 |
| Mo Bamba | 72% | 15.0<br><sub>29,16,11,18,15</sub> | 5.4<br><sub>14,8,6,8,7</sub> |  | 5.9<br><sub>7,4,4,8,10</sub> |  | 0.8<br><sub>1,1,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 12.0 |
| Isaiah Collier | 98% | 14.6<br><sub>21,24,20,12,3</sub> | 6.9<br><sub>7,7,8,7,0</sub> |  | 2.1<br><sub>8,7,1,2,1</sub> |  | 4.0<br><sub>8,6,4,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.3 | 13.1 |
| Kyle Filipowski | 58% | 11.2<br><sub>8,-,6,8,-</sub> | 5.3<br><sub>0,-,5,1,-</sub> |  | 3.5<br><sub>1,-,0,2,-</sub> |  | 1.2<br><sub>0,-,2,0,-</sub> |  | 0.4<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.2 | 0.8 | 10.0 |
| Kobe Bufkin | 38% | 8.4<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.6 |
| Tony Bradley | 48% | 8.1<br><sub>6,-,-,7,-</sub> | 2.7<br><sub>2,-,-,2,-</sub> |  | 2.4<br><sub>1,-,-,3,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.6 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving | 91% | 32.3<br><sub>33,27,35,-,36</sub> | 24.9<br><sub>18,15,35,-,29</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>6,2,4,-,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.3<br><sub>6,4,9,-,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,3,5,-,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.6 | 2.4 | 34.8 |
| Cooper Flagg | 98% | 31.3<br><sub>40,33,39,40,40</sub> | 23.9<br><sub>29,26,33,17,19</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>6,5,9,4,10</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.0<br><sub>11,8,6,6,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 1.0 | 2.6 | 36.5 |
| P.J. Washington | 98% | 30.6<br><sub>41,27,34,38,39</sub> | 15.4<br><sub>20,18,3,12,21</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>9,9,10,5,10</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,0,1,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>4,2,1,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 1.0 | 1.7 | 24.6 |
| Naji Marshall | 84% | 24.0<br><sub>-,-,-,24,26</sub> | 13.3<br><sub>-,-,-,5,22</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>-,-,-,2,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>-,-,-,7,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.9<br><sub>-,-,-,0,3</sub> |  | 1.1 | 0.1 | 1.8 | 21.0 |
| Zaccharie Risacher | 93% | 20.4<br><sub>30,29,28,19,18</sub> | 7.1<br><sub>6,13,12,0,2</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>8,6,6,5,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>1,1,3,1,2</sub> |  | 0.9<br><sub>1,2,3,0,0</sub> |  | 1.2 | 0.8 | 0.9 | 12.4 |
| Daniel Gafford | 98% | 20.2<br><sub>26,27,29,26,18</sub> | 10.7<br><sub>8,7,18,20,2</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>9,11,7,7,4</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.8 | 1.6 | 1.2 | 18.8 |
| Max Christie | 91% | 18.4<br><sub>26,22,18,8,-</sub> | 7.8<br><sub>11,11,2,0,-</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>5,5,1,2,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>3,2,0,0,-</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>3,3,0,0,-</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.3 | 0.9 | 11.5 |
| Santi Aldama | 89% | 15.0 | 7.4 |  | 3.5 |  | 1.5 |  | 0.8 |  | 0.6 | 0.4 | 0.7 | 12.4 |
| Caleb Martin | 96% | 14.9<br><sub>-,14,25,21,20</sub> | 4.8<br><sub>-,10,8,5,0</sub> |  | 2.5<br><sub>-,2,0,6,3</sub> |  | 1.1<br><sub>-,0,0,0,2</sub> |  | 0.4<br><sub>-,2,2,1,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.3 |
| Walter Clayton Jr. | 88% | 13.6<br><sub>17,15,9,24,21</sub> | 6.4<br><sub>15,0,3,20,8</sub> |  | 2.1<br><sub>4,2,2,1,6</sub> |  | 3.1<br><sub>4,5,1,2,5</sub> |  | 0.9<br><sub>2,0,1,4,2</sub> |  | 0.4 | 0.2 | 0.7 | 11.6 |
| Morez Johnson Jr. | 98% | 11.9<br><sub>15,18,17,17,18</sub> | 5.4<br><sub>6,10,2,13,8</sub> |  | 1.9<br><sub>2,6,2,2,3</sub> |  | 1.2<br><sub>1,3,1,1,1</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.4 | 0.1 | 0.7 | 8.5 |
| Marcus Sasser | 96% | 9.5<br><sub>8,22,7,19,5</sub> | 3.7<br><sub>0,10,0,4,0</sub> |  | 0.9<br><sub>1,1,0,1,1</sub> |  | 1.5<br><sub>0,4,1,1,2</sub> |  | 0.5<br><sub>0,1,0,0,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.2 |
| Moussa Cisse | 58% | 6.7<br><sub>-,3,-,2,-</sub> | 2.7<br><sub>-,0,-,0,-</sub> |  | 2.6<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.5 |
| Tobi Lawal | 52% | 5.7<br><sub>-,3,-,2,-</sub> | 2.3<br><sub>-,0,-,2,-</sub> |  | 1.1<br><sub>-,0,-,0,-</sub> |  | 0.7<br><sub>-,1,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Jett Howard | 52% | 5.4<br><sub>-,3,-,2,-</sub> | 2.4<br><sub>-,0,-,2,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.5 |

</details>


### OKC @ MEM
Out: Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 33.9<br><sub>30,28,31,39,35</sub> | 30.8<br><sub>26,21,26,43,42</sub> | 32.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>3,2,3,8,8</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>1,1,3,4,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.9 | 2.9 | 41.9 |
| Ajay Mitchell | 98% | 30.3<br><sub>25,28,26,35,32</sub> | 18.7<br><sub>30,29,6,20,23</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,4,3,5,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>5,3,5,1,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>1,2,0,0,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.6 | 0.4 | 2.0 | 27.4 |
| Jared McCain | 98% | 26.9<br><sub>30,29,28,27,25</sub> | 14.2<br><sub>18,10,10,7,9</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,4,4,9,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>4,4,2,2,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.1<br><sub>4,0,0,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.1 | 1.7 | 19.4 |
| Isaiah Hartenstein | 98% | 26.6<br><sub>26,26,25,28,26</sub> | 10.1<br><sub>15,10,10,5,3</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 10.6<br><sub>13,14,7,14,12</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>3,3,0,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.8 | 23.9 |
| Kenrich Williams | 96% | 25.2<br><sub>24,17,21,31,29</sub> | 10.2<br><sub>3,7,11,12,13</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>7,3,7,3,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,0,3,1,2</sub> |  | 1.4<br><sub>0,1,3,2,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.1 | 17.7 |
| Aday Mara | 97% | 23.9<br><sub>20,21,28,20,25</sub> | 8.3<br><sub>11,6,7,10,9</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>10,3,9,9,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>2,1,3,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 2.4 | 1.7 | 16.7 |
| Bennett Stirtz | 97% | 21.9<br><sub>25,28,26,12,22</sub> | 7.2<br><sub>7,8,11,9,16</sub> |  | 2.0<br><sub>1,0,1,2,1</sub> |  | 1.5<br><sub>1,3,3,0,1</sub> |  | 1.2<br><sub>1,1,3,3,4</sub> |  | 0.7 | 0.1 | 0.8 | 10.7 |
| Alex Caruso | 98% | 21.8<br><sub>9,-,-,-,20</sub> | 9.2<br><sub>9,-,-,-,7</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,-,-,-,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,-,-,-,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>3,-,-,-,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.5 | 0.4 | 1.0 | 15.4 |
| Micah Peavy | 72% | 20.9<br><sub>-,5,14,16,26</sub> | 5.6<br><sub>-,0,2,8,2</sub> |  | 4.2<br><sub>-,0,1,5,9</sub> |  | 1.1<br><sub>-,0,0,0,1</sub> |  | 0.5<br><sub>-,0,0,2,0</sub> |  | 0.8 | 0.2 | 0.9 | 10.9 |
| Josh Dix | 64% | 15.2<br><sub>22,24,9,12,-</sub> | 5.2<br><sub>0,2,7,0,-</sub> |  | 1.3<br><sub>1,2,0,1,-</sub> |  | 0.8<br><sub>0,0,0,0,-</sub> |  | 0.6<br><sub>0,0,1,0,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.3 |
| Dalen Terry | 52% | 9.7<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 5.8 |
| Brooks Barnhizer | 52% | 9.6<br><sub>3,14,6,-,-</sub> | 2.5<br><sub>0,3,5,-,-</sub> |  | 2.1<br><sub>0,2,2,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.2 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 97% | 32.2<br><sub>31,28,26,38,33</sub> | 15.4<br><sub>13,18,27,18,10</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>7,12,9,9,6</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>4,12,3,5,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,4,3,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.7 | 2.7 | 29.7 |
| Ty Jerome | 98% | 29.1<br><sub>30,24,-,37,29</sub> | 19.9<br><sub>15,10,-,40,23</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>1,2,-,5,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>8,3,-,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,1,-,5,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 2.5 | 29.0 |
| Cedric Coward | 98% | 27.9<br><sub>31,27,23,31,33</sub> | 13.7<br><sub>16,17,10,10,23</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>11,7,7,9,9</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,4,2,3,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>4,3,2,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 1.7 | 23.0 |
| Jaylen Wells | 98% | 24.9<br><sub>30,25,22,34,21</sub> | 9.9<br><sub>14,10,4,16,0</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>3,1,2,3,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,0,0,3,3</sub> |  | 1.6<br><sub>2,2,0,3,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.1 | 0.9 | 14.2 |
| Jerami Grant | 98% | 23.1<br><sub>24,27,23,24,24</sub> | 10.3<br><sub>13,2,14,11,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,3,1,2,2</sub> |  | 1.4<br><sub>3,0,1,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.6 | 1.4 | 14.4 |
| Zach Edey | 98% | 21.0<br><sub>21,19,18,19,25</sub> | 8.1<br><sub>4,13,4,6,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>3,7,6,9,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>2,0,0,1,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.3 | 1.3 | 16.8 |
| Cam Spencer | 98% | 19.5<br><sub>18,23,25,19,24</sub> | 7.8<br><sub>8,8,10,13,7</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>5,6,5,1,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,8,13,7,9</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>2,1,2,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.1 | 1.0 | 15.1 |
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
| Confirmed players only | 115.3–112.2 | TOR 59% | 1.70 / 2.43 | MIL +3.5 | 227.5 | MIL +4.5 covers 53%; o229.5 46% |
| Expected (weighted by chance each plays) | 116.9–111.2 | TOR 65% | 1.55 / 2.83 | MIL +5.5 | 227.5 | MIL +4.5 covers 46%; o229.5 46% |
| if Immanuel Quickley plays | 116.2–111.3 | TOR 64% | 1.57 / 2.75 | MIL +5.5 | 227.5 | MIL +4.5 covers 48%; o229.5 46% |
| if Scottie Barnes plays | 117.1–111.3 | TOR 66% | 1.52 / 2.93 | MIL +5.5 | 228.5 | MIL +4.5 covers 46%; o229.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyle Anderson (TOR) | Questionable | 55% | 17.5 | 5.2 | 3.3 | 3.3 | 0.1 | 0.9 | 0.5 | 0.9 | 11.8 | small |
| Immanuel Quickley (TOR) | Questionable | 55% | 33.8 | 20.2 | 4.2 | 7.1 | 3.0 | 1.5 | 0.1 | 1.7 | 31.5 | full tables below |
| Scottie Barnes (TOR) | Questionable | 55% | 36.6 | 25.5 | 7.6 | 7.8 | 1.0 | 1.9 | 1.1 | 3.5 | 40.9 | full tables below |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 35.8<br><sub>32,34,32,37,33</sub> | 28.1<br><sub>25,9,22,26,22</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>9,3,10,6,5</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>6,5,5,3,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>3,1,4,2,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.4 | 2.8 | 40.6 |
| Ja'Kobe Walter | 98% | 33.4<br><sub>28,32,33,35,27</sub> | 16.4<br><sub>14,9,11,10,8</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>5,3,4,6,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>2,1,2,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>3,3,3,0,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.3 | 1.2 | 23.7 |
| Jamal Shead | 98% | 29.0<br><sub>23,23,25,20,20</sub> | 11.2<br><sub>13,2,9,6,3</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>4,1,2,1,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 7.7<br><sub>7,8,6,6,6</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>1,0,2,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.2 | 2.1 | 21.6 |
| Collin Murray-Boyles | 98% | 29.0<br><sub>15,23,20,28,23</sub> | 15.9<br><sub>10,15,4,18,13</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 6.6<br><sub>2,5,3,7,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,1,1,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.5<br><sub>2,1,0,1,1</sub> | 0.5<br><sub>o 44% · u 56%</sub> | 1.3 | 1.0 | 1.9 | 25.8 |
| Jamison Battle | 98% | 28.3<br><sub>20,19,17,21,19</sub> | 14.0<br><sub>7,2,20,12,9</sub> |  | 3.9<br><sub>0,0,5,0,1</sub> |  | 1.8<br><sub>1,0,0,0,0</sub> |  | 2.6<br><sub>1,0,4,4,2</sub> |  | 0.6 | 0.2 | 1.1 | 19.7 |
| Allen Graves | 97% | 23.8<br><sub>18,9,10,7,14</sub> | 8.6<br><sub>3,7,3,0,5</sub> |  | 4.1<br><sub>1,4,0,0,1</sub> |  | 1.7<br><sub>0,0,0,2,1</sub> |  | 1.0<br><sub>0,1,0,0,1</sub> |  | 0.9 | 0.7 | 0.9 | 14.4 |
| Jakob Poeltl | 74% | 23.5<br><sub>10,23,-,-,19</sub> | 10.6<br><sub>2,12,-,-,8</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>2,11,-,-,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>0,3,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 1.0 | 0.7 | 1.3 | 19.8 |
| Alijah Martin | 88% | 19.3<br><sub>5,-,16,6,9</sub> | 8.5<br><sub>5,-,5,2,6</sub> |  | 2.9<br><sub>1,-,2,2,1</sub> |  | 2.2<br><sub>1,-,4,0,0</sub> |  | 0.7<br><sub>1,-,1,0,0</sub> |  | 1.0 | 0.4 | 1.1 | 13.6 |
| Trayce Jackson-Davis | 96% | 18.6<br><sub>20,1,9,2,4</sub> | 7.1<br><sub>6,0,5,0,1</sub> |  | 6.3<br><sub>11,0,5,0,0</sub> |  | 1.6<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.9 | 0.9 | 14.9 |
| Jaden Bradley | 67% | 14.4<br><sub>5,-,4,-,4</sub> | 4.5<br><sub>0,-,3,-,2</sub> |  | 2.5<br><sub>1,-,1,-,1</sub> |  | 1.2<br><sub>1,-,2,-,0</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 1.4 | 0.3 | 0.9 | 8.3 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.7<br><sub>32,27,27,31,33</sub> | 20.0<br><sub>23,23,15,21,25</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>10,3,3,6,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>7,0,2,3,3</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>3,4,4,4,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.2 | 2.5 | 28.8 |
| Jaime Jaquez Jr. | 98% | 28.4<br><sub>25,27,23,28,31</sub> | 14.8<br><sub>8,19,8,19,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,4,7,8,2</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>0,2,5,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>0,3,1,2,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.2 | 2.4 | 23.9 |
| Myles Turner | 98% | 28.4<br><sub>28,22,24,31,36</sub> | 10.7<br><sub>6,4,10,13,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>9,2,7,5,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>4,2,2,2,6</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,1,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 2.1 | 1.4 | 18.1 |
| Kyle Kuzma | 98% | 26.3<br><sub>29,18,23,22,27</sub> | 11.7<br><sub>17,4,14,2,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>7,6,3,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,1,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>4,0,2,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.3 | 1.9 | 19.3 |
| Ryan Rollins | 98% | 26.1<br><sub>32,17,26,17,24</sub> | 13.8<br><sub>19,4,9,10,13</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>2,4,3,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>4,5,7,2,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.4 | 2.6 | 22.2 |
| AJ Green | 98% | 20.7<br><sub>20,24,20,24,20</sub> | 7.1<br><sub>3,9,0,13,5</sub> |  | 2.1<br><sub>4,1,3,3,2</sub> |  | 1.4<br><sub>3,2,2,3,3</sub> |  | 1.4<br><sub>1,3,0,4,1</sub> |  | 0.4 | 0.1 | 0.9 | 10.7 |
| Brayden Burries | 97% | 19.4<br><sub>16,17,21,26,22</sub> | 8.6<br><sub>4,10,14,9,9</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,5,3,9,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>1,1,1,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.2 | 1.3 | 14.3 |
| Kel'el Ware | 91% | 17.4<br><sub>19,17,24,17,16</sub> | 8.5<br><sub>16,6,19,2,2</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>14,8,10,9,5</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>0,0,3,0,1</sub> |  | 0.7<br><sub>0,0,3,0,0</sub> |  | 0.5 | 0.7 | 1.3 | 15.5 |
| Kasparas Jakucionis | 91% | 17.2<br><sub>21,19,21,22,12</sub> | 6.2<br><sub>7,4,5,7,3</sub> |  | 2.3<br><sub>4,2,3,5,1</sub> |  | 3.0<br><sub>5,6,3,7,1</sub> |  | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.2 | 1.2 | 11.6 |
| Nate Ament | 88% | 13.8<br><sub>14,20,19,8,18</sub> | 5.8<br><sub>7,8,14,4,9</sub> |  | 2.1<br><sub>3,4,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,1,2,0,2</sub> |  | 0.4 | 0.2 | 0.8 | 8.5 |
| Caris LeVert | 23% | 13.4<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 8.2 |
| Gary Trent Jr. | 48% | 8.8<br><sub>-,7,6,-,-</sub> | 3.6<br><sub>-,3,3,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.7 |
| Jericho Sims | 63% | 8.1<br><sub>-,7,-,15,1</sub> | 1.9<br><sub>-,0,-,0,0</sub> |  | 2.2<br><sub>-,0,-,2,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Ousmane Dieng | 71% | 8.0<br><sub>3,13,6,-,2</sub> | 2.9<br><sub>0,4,0,-,0</sub> |  | 1.3<br><sub>0,0,1,-,0</sub> |  | 1.0<br><sub>0,0,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.2 |

</details>

<details><summary>if Immanuel Quickley plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 31.7<br><sub>32,27,27,31,33</sub> | 19.8<br><sub>23,23,15,21,25</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>10,3,3,6,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>7,0,2,3,3</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>3,4,4,4,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.2 | 2.5 | 28.6 |
| Jaime Jaquez Jr. (MIL) | 98% | 28.4<br><sub>25,27,23,28,31</sub> | 14.8<br><sub>8,19,8,19,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,4,7,8,2</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>0,2,5,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>0,3,1,2,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.2 | 2.4 | 23.9 |
| Myles Turner (MIL) | 98% | 28.3<br><sub>28,22,24,31,36</sub> | 10.7<br><sub>6,4,10,13,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>9,2,7,5,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>4,2,2,2,6</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,1,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 2.0 | 1.4 | 18.1 |
| Kyle Kuzma (MIL) | 98% | 26.3<br><sub>29,18,23,22,27</sub> | 11.6<br><sub>17,4,14,2,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>7,6,3,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,1,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>4,0,2,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.3 | 1.9 | 19.2 |
| Ryan Rollins (MIL) | 98% | 26.1<br><sub>32,17,26,17,24</sub> | 13.7<br><sub>19,4,9,10,13</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>2,4,3,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>4,5,7,2,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.4 | 2.6 | 22.1 |
| AJ Green (MIL) | 98% | 20.7<br><sub>20,24,20,24,20</sub> | 7.1<br><sub>3,9,0,13,5</sub> |  | 2.1<br><sub>4,1,3,3,2</sub> |  | 1.4<br><sub>3,2,2,3,3</sub> |  | 1.4<br><sub>1,3,0,4,1</sub> |  | 0.4 | 0.1 | 0.9 | 10.7 |
| Brayden Burries (MIL) | 97% | 19.4<br><sub>16,17,21,26,22</sub> | 8.5<br><sub>4,10,14,9,9</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,5,3,9,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>1,1,1,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.2 | 1.3 | 14.1 |
| Kel'el Ware (MIL) | 91% | 17.4<br><sub>19,17,24,17,16</sub> | 8.5<br><sub>16,6,19,2,2</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>14,8,10,9,5</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>0,0,3,0,1</sub> |  | 0.7<br><sub>0,0,3,0,0</sub> |  | 0.5 | 0.7 | 1.3 | 15.4 |
| Kasparas Jakucionis (MIL) | 91% | 17.2<br><sub>21,19,21,22,12</sub> | 6.2<br><sub>7,4,5,7,3</sub> |  | 2.3<br><sub>4,2,3,5,1</sub> |  | 3.0<br><sub>5,6,3,7,1</sub> |  | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.2 | 1.2 | 11.6 |
| Nate Ament (MIL) | 88% | 13.8<br><sub>14,20,19,8,18</sub> | 5.8<br><sub>7,8,14,4,9</sub> |  | 2.2<br><sub>3,4,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,1,2,0,2</sub> |  | 0.4 | 0.2 | 0.8 | 8.5 |
| Caris LeVert (MIL) | 23% | 13.4<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 8.2 |
| Gary Trent Jr. (MIL) | 48% | 8.8<br><sub>-,7,6,-,-</sub> | 3.6<br><sub>-,3,3,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.7 |
| Jericho Sims (MIL) | 63% | 8.1<br><sub>-,7,-,15,1</sub> | 1.9<br><sub>-,0,-,0,0</sub> |  | 2.2<br><sub>-,0,-,2,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Ousmane Dieng (MIL) | 71% | 8.0<br><sub>3,13,6,-,2</sub> | 2.9<br><sub>0,4,0,-,0</sub> |  | 1.3<br><sub>0,0,1,-,0</sub> |  | 1.0<br><sub>0,0,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.2 |
| RJ Barrett (TOR) | 98% | 35.8<br><sub>32,34,32,37,33</sub> | 26.7<br><sub>25,9,22,26,22</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>9,3,10,6,5</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>6,5,5,3,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>3,1,4,2,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 2.6 | 39.0 |
| Immanuel Quickley (TOR) | 100% | 33.8<br><sub>29,37,33,38,32</sub> | 20.2<br><sub>16,17,12,27,13</sub> | 19.5 · – | 4.2<br><sub>3,6,6,4,1</sub> | 4.5 | 7.1<br><sub>7,8,7,2,7</sub> | 6.5 | 3.0<br><sub>4,4,3,1,2</sub> | 3.5 | 1.5 | 0.1 | 1.7 | 31.5 |
| Ja'Kobe Walter (TOR) | 98% | 32.7<br><sub>28,32,33,35,27</sub> | 14.8<br><sub>14,9,11,10,8</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>5,3,4,6,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>2,1,2,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,3,3,0,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.3 | 1.0 | 21.6 |
| Collin Murray-Boyles (TOR) | 98% | 28.0<br><sub>15,23,20,28,23</sub> | 14.1<br><sub>10,15,4,18,13</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>2,5,3,7,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>1,1,1,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.5<br><sub>2,1,0,1,1</sub> | 0.5<br><sub>o 44% · u 56%</sub> | 1.3 | 1.1 | 1.7 | 23.3 |
| Jamal Shead (TOR) | 98% | 25.9<br><sub>23,23,25,20,20</sub> | 8.7<br><sub>13,2,9,6,3</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>4,1,2,1,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 6.3<br><sub>7,8,6,6,6</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,0,2,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.2 | 1.7 | 17.3 |
| Jamison Battle (TOR) | 98% | 23.9<br><sub>20,19,17,21,19</sub> | 10.4<br><sub>7,2,20,12,9</sub> |  | 3.2<br><sub>0,0,5,0,1</sub> |  | 1.2<br><sub>1,0,0,0,0</sub> |  | 1.9<br><sub>1,0,4,4,2</sub> |  | 0.5 | 0.2 | 0.8 | 14.9 |
| Jakob Poeltl (TOR) | 74% | 22.4<br><sub>10,23,-,-,19</sub> | 8.8<br><sub>2,12,-,-,8</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>2,11,-,-,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>0,3,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 1.0 | 0.7 | 1.1 | 17.1 |
| Allen Graves (TOR) | 97% | 19.1<br><sub>18,9,10,7,14</sub> | 6.4<br><sub>3,7,3,0,5</sub> |  | 3.2<br><sub>1,4,0,0,1</sub> |  | 1.4<br><sub>0,0,0,2,1</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.8 | 0.6 | 0.7 | 11.0 |
| Trayce Jackson-Davis (TOR) | 96% | 13.2<br><sub>20,1,9,2,4</sub> | 4.8<br><sub>6,0,5,0,1</sub> |  | 4.3<br><sub>11,0,5,0,0</sub> |  | 1.0<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.7 | 0.6 | 10.2 |
| Alijah Martin (TOR) | 88% | 12.6<br><sub>5,-,16,6,9</sub> | 5.3<br><sub>5,-,5,2,6</sub> |  | 1.9<br><sub>1,-,2,2,1</sub> |  | 1.3<br><sub>1,-,4,0,0</sub> |  | 0.4<br><sub>1,-,1,0,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.5 |
| Jaden Bradley (TOR) | 67% | 8.8<br><sub>5,-,4,-,4</sub> | 2.7<br><sub>0,-,3,-,2</sub> |  | 1.5<br><sub>1,-,1,-,1</sub> |  | 0.9<br><sub>1,-,2,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.8 | 0.2 | 0.5 | 5.1 |

</details>

<details><summary>if Scottie Barnes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 31.7<br><sub>32,27,27,31,33</sub> | 19.7<br><sub>23,23,15,21,25</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>10,3,3,6,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>7,0,2,3,3</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>3,4,4,4,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.2 | 2.5 | 28.5 |
| Jaime Jaquez Jr. (MIL) | 98% | 28.4<br><sub>25,27,23,28,31</sub> | 14.8<br><sub>8,19,8,19,18</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>6,4,7,8,2</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>0,2,5,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>0,3,1,2,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.2 | 2.4 | 24.0 |
| Myles Turner (MIL) | 98% | 28.4<br><sub>28,22,24,31,36</sub> | 10.8<br><sub>6,4,10,13,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>9,2,7,5,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>4,2,2,2,6</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,1,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 2.1 | 1.4 | 18.1 |
| Kyle Kuzma (MIL) | 98% | 26.3<br><sub>29,18,23,22,27</sub> | 11.7<br><sub>17,4,14,2,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>7,6,3,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,1,3,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>4,0,2,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.7 | 0.3 | 1.9 | 19.4 |
| Ryan Rollins (MIL) | 98% | 26.0<br><sub>32,17,26,17,24</sub> | 13.7<br><sub>19,4,9,10,13</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>2,4,3,3,9</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>4,5,7,2,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.4 | 2.6 | 22.1 |
| AJ Green (MIL) | 98% | 20.7<br><sub>20,24,20,24,20</sub> | 7.1<br><sub>3,9,0,13,5</sub> |  | 2.1<br><sub>4,1,3,3,2</sub> |  | 1.4<br><sub>3,2,2,3,3</sub> |  | 1.4<br><sub>1,3,0,4,1</sub> |  | 0.4 | 0.1 | 0.9 | 10.6 |
| Brayden Burries (MIL) | 97% | 19.4<br><sub>16,17,21,26,22</sub> | 8.5<br><sub>4,10,14,9,9</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,5,3,9,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>1,1,1,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.2 | 1.3 | 14.2 |
| Kel'el Ware (MIL) | 91% | 17.3<br><sub>19,17,24,17,16</sub> | 8.5<br><sub>16,6,19,2,2</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>14,8,10,9,5</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>0,0,3,0,1</sub> |  | 0.7<br><sub>0,0,3,0,0</sub> |  | 0.5 | 0.7 | 1.3 | 15.4 |
| Kasparas Jakucionis (MIL) | 91% | 17.2<br><sub>21,19,21,22,12</sub> | 6.2<br><sub>7,4,5,7,3</sub> |  | 2.3<br><sub>4,2,3,5,1</sub> |  | 3.0<br><sub>5,6,3,7,1</sub> |  | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.5 | 0.2 | 1.3 | 11.5 |
| Nate Ament (MIL) | 88% | 13.8<br><sub>14,20,19,8,18</sub> | 5.8<br><sub>7,8,14,4,9</sub> |  | 2.2<br><sub>3,4,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,1,2,0,2</sub> |  | 0.4 | 0.2 | 0.8 | 8.5 |
| Caris LeVert (MIL) | 23% | 13.3<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 8.1 |
| Gary Trent Jr. (MIL) | 48% | 8.9<br><sub>-,7,6,-,-</sub> | 3.6<br><sub>-,3,3,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.5<br><sub>-,1,1,-,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.8 |
| Jericho Sims (MIL) | 63% | 8.1<br><sub>-,7,-,15,1</sub> | 1.9<br><sub>-,0,-,0,0</sub> |  | 2.2<br><sub>-,0,-,2,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Ousmane Dieng (MIL) | 71% | 8.0<br><sub>3,13,6,-,2</sub> | 2.9<br><sub>0,4,0,-,0</sub> |  | 1.2<br><sub>0,0,1,-,0</sub> |  | 1.0<br><sub>0,0,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.1 |
| Scottie Barnes (TOR) | 100% | 36.6<br><sub>31,39,36,38,32</sub> | 25.5<br><sub>28,41,29,22,17</sub> |  | 7.6<br><sub>6,5,6,15,6</sub> |  | 7.8<br><sub>4,5,5,8,6</sub> |  | 1.0<br><sub>0,1,0,0,1</sub> |  | 1.9 | 1.1 | 3.5 | 40.9 |
| RJ Barrett (TOR) | 98% | 36.1<br><sub>32,34,32,37,33</sub> | 25.4<br><sub>25,9,22,26,22</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,3,10,6,5</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>6,5,5,3,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>3,1,4,2,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 2.6 | 37.0 |
| Ja'Kobe Walter (TOR) | 98% | 33.1<br><sub>28,32,33,35,27</sub> | 14.3<br><sub>14,9,11,10,8</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>5,3,4,6,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>2,1,2,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,3,3,0,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.3 | 0.9 | 20.9 |
| Collin Murray-Boyles (TOR) | 98% | 27.9<br><sub>15,23,20,28,23</sub> | 13.1<br><sub>10,15,4,18,13</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>2,5,3,7,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>1,1,1,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.5<br><sub>2,1,0,1,1</sub> | 0.5<br><sub>o 44% · u 56%</sub> | 1.3 | 1.0 | 1.6 | 22.0 |
| Jamal Shead (TOR) | 98% | 27.1<br><sub>23,23,25,20,20</sub> | 8.8<br><sub>13,2,9,6,3</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>4,1,2,1,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 6.7<br><sub>7,8,6,6,6</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,0,2,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.2 | 1.7 | 17.8 |
| Jamison Battle (TOR) | 98% | 22.4<br><sub>20,19,17,21,19</sub> | 9.8<br><sub>7,2,20,12,9</sub> |  | 3.0<br><sub>0,0,5,0,1</sub> |  | 1.1<br><sub>1,0,0,0,0</sub> |  | 1.8<br><sub>1,0,4,4,2</sub> |  | 0.5 | 0.2 | 0.7 | 14.0 |
| Jakob Poeltl (TOR) | 74% | 22.4<br><sub>10,23,-,-,19</sub> | 8.6<br><sub>2,12,-,-,8</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>2,11,-,-,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>0,3,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 1.0 | 0.7 | 1.1 | 16.8 |
| Allen Graves (TOR) | 97% | 16.8<br><sub>18,9,10,7,14</sub> | 5.4<br><sub>3,7,3,0,5</sub> |  | 2.8<br><sub>1,4,0,0,1</sub> |  | 1.2<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 0.7 | 0.5 | 0.6 | 9.4 |
| Alijah Martin (TOR) | 88% | 13.6<br><sub>5,-,16,6,9</sub> | 5.4<br><sub>5,-,5,2,6</sub> |  | 2.0<br><sub>1,-,2,2,1</sub> |  | 1.4<br><sub>1,-,4,0,0</sub> |  | 0.4<br><sub>1,-,1,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.8 |
| Trayce Jackson-Davis (TOR) | 96% | 11.3<br><sub>20,1,9,2,4</sub> | 4.1<br><sub>6,0,5,0,1</sub> |  | 3.7<br><sub>11,0,5,0,0</sub> |  | 0.9<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.5 | 0.5 | 8.6 |
| Jaden Bradley (TOR) | 67% | 9.5<br><sub>5,-,4,-,4</sub> | 3.1<br><sub>0,-,3,-,2</sub> |  | 1.7<br><sub>1,-,1,-,1</sub> |  | 1.0<br><sub>1,-,2,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 1.0 | 0.2 | 0.6 | 5.8 |

</details>


### MIN @ NOP
Out: Yves Missi (NOP), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Terrence Shannon Jr. (MIN)

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.6<br><sub>35,33,39,29,37</sub> | 19.0<br><sub>19,23,19,13,14</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>7,6,3,6,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>4,7,3,3,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>1,1,2,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 1.0 | 1.9 | 27.9 |
| Ayo Dosunmu | 98% | 33.3<br><sub>32,30,38,37,34</sub> | 19.1<br><sub>17,15,27,19,21</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>3,7,9,12,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 5.1<br><sub>4,2,3,8,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>3,3,2,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.4 | 2.1 | 28.8 |
| Jonathan Kuminga | 98% | 31.8<br><sub>32,22,40,33,32</sub> | 15.5<br><sub>20,5,19,8,16</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>3,1,6,10,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>5,0,3,3,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>3,1,2,2,4</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.8 | 1.6 | 24.2 |
| Rudy Gobert | 98% | 30.7<br><sub>20,30,-,31,33</sub> | 10.2<br><sub>1,9,-,10,8</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 11.9<br><sub>4,13,-,10,11</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>1,4,-,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.9 | 1.7 | 1.4 | 23.9 |
| LaMelo Ball | 98% | 29.1<br><sub>28,29,20,33,31</sub> | 21.9<br><sub>8,24,10,34,20</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,4,8,6,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>8,7,4,3,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>2,6,0,6,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.3 | 3.5 | 33.0 |
| Jaylen Clark | 88% | 20.2<br><sub>7,17,20,21,25</sub> | 7.5<br><sub>3,5,10,4,10</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,0,2,2,4</sub> |  | 1.2<br><sub>1,2,1,0,1</sub> |  | 0.9<br><sub>1,1,2,1,2</sub> |  | 1.1 | 0.2 | 0.7 | 11.1 |
| Trey Lyles | 98% | 19.8<br><sub>22,17,17,21,20</sub> | 7.0<br><sub>7,10,6,12,5</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>3,5,0,4,2</sub> |  | 1.0<br><sub>1,0,0,0,0</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> |  | 0.6 | 0.3 | 0.7 | 12.0 |
| Joan Beringer | 96% | 17.5<br><sub>20,18,34,14,13</sub> | 7.6<br><sub>7,4,12,2,4</sub> |  | 6.2<br><sub>9,4,6,7,7</sub> |  | 0.7<br><sub>2,0,2,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.3 | 0.8 | 14.5 |
| Bones Hyland | 97% | 16.8<br><sub>16,20,14,14,16</sub> | 9.6<br><sub>13,19,6,10,19</sub> |  | 1.8<br><sub>1,0,1,1,2</sub> |  | 3.0<br><sub>3,8,3,3,4</sub> |  | 1.5<br><sub>3,3,0,2,4</sub> |  | 0.7 | 0.3 | 1.2 | 14.3 |
| Zyon Pullin | 38% | 7.8<br><sub>-,2,-,-,-</sub> | 3.5<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.4 |
| Rocco Zikarsky | 36% | 7.5<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.7 | 0.4 | 5.3 |
| Cody Williams | 52% | 6.3<br><sub>-,2,-,7,-</sub> | 0.2<br><sub>-,0,-,0,-</sub> |  | 1.1<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 1.7 |
| Isaiah Evans | 38% | 5.5<br><sub>-,2,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.8 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 32.2<br><sub>30,32,29,40,-</sub> | 14.7<br><sub>6,19,15,18,-</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>1,5,5,5,-</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>3,3,5,5,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>2,2,1,3,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.5 | 1.4 | 22.5 |
| Dejounte Murray | 98% | 31.9<br><sub>30,-,-,-,45</sub> | 16.9<br><sub>10,-,-,-,20</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>8,-,-,-,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 6.2<br><sub>5,-,-,-,4</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>0,-,-,-,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.8 | 0.4 | 3.0 | 29.2 |
| Zion Williamson | 98% | 30.7<br><sub>32,31,30,35,38</sub> | 19.1<br><sub>25,22,15,25,23</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>5,6,6,11,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>2,2,4,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.1<br><sub>1,0,0,0,0</sub> |  | 1.2 | 0.8 | 2.2 | 27.5 |
| Jeremiah Fears | 98% | 27.8<br><sub>24,29,31,38,34</sub> | 14.7<br><sub>11,22,20,12,19</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>4,8,5,4,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>3,13,7,7,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,3,1,0,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.5 | 2.4 | 23.0 |
| Saddiq Bey | 98% | 26.1<br><sub>26,24,26,36,29</sub> | 12.7<br><sub>9,10,25,18,22</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>0,4,6,5,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>3,3,1,1,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.1 | 18.5 |
| Herbert Jones | 98% | 24.1<br><sub>19,32,25,28,37</sub> | 7.4<br><sub>4,16,11,9,2</sub> |  | 2.8<br><sub>2,4,3,4,5</sub> |  | 1.8<br><sub>0,1,2,3,1</sub> |  | 0.8<br><sub>0,0,1,3,0</sub> |  | 1.2 | 0.5 | 1.1 | 12.0 |
| Derik Queen | 98% | 22.5<br><sub>25,22,23,24,27</sub> | 11.4<br><sub>11,9,8,20,20</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 6.6<br><sub>12,2,8,7,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>1,3,4,5,6</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.3<br><sub>0,1,0,1,0</sub> |  | 1.0 | 0.9 | 2.1 | 20.8 |
| Karlo Matkovic | 91% | 16.4<br><sub>18,28,18,29,21</sub> | 6.5<br><sub>5,12,8,25,5</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>3,4,10,6,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>1,1,1,1,2</sub> |  | 0.6<br><sub>1,1,2,5,1</sub> |  | 0.5 | 1.0 | 0.7 | 11.2 |
| Bennedict Mathurin | 98% | 15.6<br><sub>14,19,19,13,15</sub> | 7.5<br><sub>5,10,7,4,2</sub> |  | 2.7<br><sub>1,3,1,0,5</sub> |  | 1.3<br><sub>2,2,2,0,1</sub> |  | 0.5<br><sub>1,2,1,0,0</sub> |  | 0.4 | 0.2 | 1.1 | 11.4 |
| Trendon Watford | 67% | 13.3<br><sub>-,17,18,16,20</sub> | 5.5<br><sub>-,8,7,4,7</sub> |  | 2.4<br><sub>-,1,4,4,3</sub> |  | 1.4<br><sub>-,2,0,1,2</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.4 | 0.9 | 9.3 |
| Jordan Poole | 64% | 12.4<br><sub>7,-,-,-,-</sub> | 6.1<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-,-</sub> |  | 1.6<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 9.0 |
| DeAndre Jordan | 35% | 8.1<br><sub>13,-,-,-,-</sub> | 2.4<br><sub>3,-,-,-,-</sub> |  | 3.0<br><sub>4,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.4 | 5.9 |
| Bryce McGowens | 58% | 7.3<br><sub>3,6,15,6,-</sub> | 2.6<br><sub>0,4,3,0,-</sub> |  | 0.8<br><sub>0,1,0,1,-</sub> |  | 0.5<br><sub>0,2,1,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| AJ Johnson | 30% | 5.4<br><sub>-,-,3,-,-</sub> | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.5 | 0.8 | 0.9 |
| Julian Reese | 36% | 5.4<br><sub>-,-,3,-,-</sub> | 2.2<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.9 | 3.8 |

</details>


### POR @ LAL
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.4<br><sub>33,32,30,35,35</sub> | 23.3<br><sub>23,24,24,28,21</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>4,9,5,3,7</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>9,7,2,5,12</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>4,0,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.4 | 3.9 | 36.5 |
| Damian Lillard | 98% | 32.9<br><sub>31,30,27,30,33</sub> | 19.2<br><sub>21,9,22,20,25</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,2,4,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,1,3,1,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.7 | 29.0 |
| Toumani Camara | 98% | 31.4<br><sub>24,26,31,31,32</sub> | 12.2<br><sub>12,13,14,9,11</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>1,2,4,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>4,3,4,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.3 | 1.5 | 18.2 |
| Jrue Holiday | 98% | 30.2<br><sub>30,24,22,31,28</sub> | 14.2<br><sub>22,6,14,17,15</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>4,6,4,8,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.4<br><sub>3,4,3,10,0</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,2,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 2.5 | 24.1 |
| Donovan Clingan | 98% | 26.7<br><sub>26,29,15,32,29</sub> | 11.4<br><sub>9,11,4,17,24</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 10.3<br><sub>10,8,9,18,11</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>2,1,0,1,1</sub> |  | 0.7 | 1.4 | 1.4 | 23.6 |
| Scoot Henderson | 98% | 25.8<br><sub>17,19,31,26,22</sub> | 11.9<br><sub>2,9,14,8,9</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,0,1,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.2 | 2.4 | 17.3 |
| Sidy Cissoko | 97% | 21.6<br><sub>20,19,19,22,21</sub> | 5.7<br><sub>6,4,1,8,7</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>2,6,3,3,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>4,2,1,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>0,0,0,2,1</sub> |  | 0.9 | 0.3 | 1.0 | 10.5 |
| Robert Williams III | 98% | 17.7<br><sub>21,-,14,15,16</sub> | 6.7<br><sub>14,-,3,2,9</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>10,-,3,6,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,-,1,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.8 | 1.0 | 0.9 | 14.5 |
| Chris Youngblood | 86% | 10.2<br><sub>-,-,7,15,4</sub> | 3.8<br><sub>-,-,3,7,0</sub> |  | 1.3<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |
| Micah Potter | 64% | 7.9<br><sub>-,9,4,-,2</sub> | 3.3<br><sub>-,1,2,-,4</sub> |  | 2.1<br><sub>-,2,1,-,1</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.8 |
| Branden Carlson | 58% | 7.7<br><sub>-,12,4,-,3</sub> | 2.1<br><sub>-,2,0,-,2</sub> |  | 1.7<br><sub>-,2,2,-,0</sub> |  | 0.5<br><sub>-,1,1,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |
| Yang Hansen | 63% | 7.4<br><sub>-,5,13,-,2</sub> | 2.8<br><sub>-,3,6,-,0</sub> |  | 1.7<br><sub>-,2,5,-,0</sub> |  | 0.4<br><sub>-,1,1,-,0</sub> |  | 0.2<br><sub>-,1,2,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.9 |
| Jayson Kent | 71% | 6.6<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 35.5<br><sub>-,37,35,36,35</sub> | 33.6<br><sub>-,37,45,42,40</sub> | 35.5 · –<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>-,7,15,7,9</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>-,5,6,13,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>-,6,8,6,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8 | 0.6 | 4.2 | 48.6 |
| Austin Reaves | 98% | 34.8<br><sub>31,37,39,34,37</sub> | 20.7<br><sub>16,21,19,27,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,4,3,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>1,5,4,5,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 3.2 | 29.7 |
| Walker Kessler | 98% | 28.7<br><sub>26,31,31,32,29</sub> | 11.8<br><sub>11,10,16,15,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 10.5<br><sub>9,13,15,15,8</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,2,1,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.1 | 1.5 | 23.7 |
| Quentin Grimes | 98% | 23.3<br><sub>38,26,26,23,25</sub> | 7.6<br><sub>23,3,7,7,6</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>3,3,1,4,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>5,2,3,4,1</sub> |  | 0.8<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.3 | 1.2 | 12.3 |
| Ziaire Williams | 96% | 21.5<br><sub>-,-,-,15,23</sub> | 7.7<br><sub>-,-,-,9,10</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>-,-,-,2,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>-,-,-,2,1</sub> |  | 0.9<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.3 | 0.9 | 11.5 |
| Sandro Mamukelashvili | 98% | 20.4<br><sub>30,20,24,28,19</sub> | 8.4<br><sub>13,4,11,13,2</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>8,7,1,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>3,0,1,4,1</sub> |  | 0.9<br><sub>0,0,2,2,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.5 | 0.8 | 14.3 |
| Matisse Thybulle | 98% | 20.1<br><sub>28,28,25,19,23</sub> | 5.7<br><sub>15,10,6,6,3</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,3,2,1,1</sub> |  | 1.1<br><sub>0,0,3,2,2</sub> |  | 0.8<br><sub>4,1,2,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.7 | 0.8 | 8.7 |
| Jake LaRavia | 96% | 20.0<br><sub>35,28,25,26,21</sub> | 5.5<br><sub>2,10,8,7,9</sub> | 5.5 · –<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>10,2,2,4,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>0,0,4,2,2</sub> |  | 0.5<br><sub>0,2,2,1,2</sub> |  | 1.1 | 0.6 | 1.1 | 9.9 |
| Collin Sexton | 98% | 16.6<br><sub>21,16,19,16,16</sub> | 9.9<br><sub>21,0,14,6,10</sub> |  | 1.8<br><sub>4,2,3,1,3</sub> |  | 1.8<br><sub>2,1,3,5,1</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 0.8 | 0.2 | 1.4 | 13.6 |
| Jarred Vanderbilt | 72% | 9.3<br><sub>21,13,12,6,7</sub> | 2.7<br><sub>0,0,4,2,0</sub> |  | 2.4<br><sub>7,3,3,1,1</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 5.8 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Lawson Lovering | 91% | 6.7<br><sub>-,-,-,1,1</sub> | 2.0<br><sub>-,-,-,0,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.3 |
| Jaden Hardy | 80% | 6.4<br><sub>9,1,1,1,1</sub> | 3.4<br><sub>2,0,1,2,0</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.6<br><sub>2,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.0 | 0.4 | 4.5 |
| Kevon Looney | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.3 |
| Adou Thiero | 16% | 5.6 | 2.0 |  | 1.4 |  | 0.4 |  | 0.0 |  | 0.2 | 0.1 | 0.5 | 3.8 |
| Chris Manon | 58% | 5.3<br><sub>-,1,-,-,-</sub> | 1.8<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.1 |

</details>


### SAS @ SAC
Out: Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 120.9–108.3 | SAS 81% | 1.23 / 5.36 | SAC +12.5 | 228.5 | SAC +17.5 covers 63%; o231.5 45% |
| Expected (weighted by chance each plays) | 120.9–108.6 | SAS 80% | 1.24 / 5.11 | SAC +12.5 | 229.5 | SAC +17.5 covers 64%; o231.5 45% |
| if De'Andre Hunter plays | 120.8–108.9 | SAS 80% | 1.25 / 4.99 | SAC +11.5 | 229.5 | SAC +17.5 covers 65%; o231.5 46% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Andre Hunter (SAC) | Questionable | 55% | 30.6 | 13.5 | 4.5 | 1.6 | 1.8 | 0.8 | 0.2 | 1.4 | 19.6 | full tables below |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 32.7<br><sub>27,39,34,24,34</sub> | 28.4<br><sub>29,36,43,12,52</sub> | 28.5 · –<br><sub>o 48% · u 52%</sub> | 11.3<br><sub>10,14,7,11,24</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,5,4,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>0,4,3,0,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 3.9 | 2.5 | 43.0 |
| Devin Vassell | 98% | 32.5<br><sub>24,38,34,25,36</sub> | 13.5<br><sub>14,21,9,11,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,5,5,2,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>8,2,2,1,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>4,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.5 | 1.1 | 20.9 |
| Dylan Harper | 98% | 32.4<br><sub>30,37,39,27,36</sub> | 17.1<br><sub>13,13,25,17,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>6,5,7,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>6,8,6,8,0</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.4 | 1.9 | 27.4 |
| De'Aaron Fox | 98% | 31.6<br><sub>26,39,35,22,33</sub> | 15.9<br><sub>11,14,22,12,10</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>4,3,8,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>6,4,7,3,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,1,0,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.4 | 2.1 | 26.1 |
| Stephon Castle | 98% | 30.9<br><sub>27,38,22,26,35</sub> | 17.0<br><sub>15,14,0,16,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,6,5,5,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>5,8,4,4,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.9 | 28.7 |
| Julian Champagnie | 98% | 25.5<br><sub>25,31,27,22,21</sub> | 9.4<br><sub>26,6,12,8,0</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>3,6,3,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,0,1,0,3</sub> |  | 1.8<br><sub>8,2,3,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 0.8 | 15.3 |
| Keldon Johnson | 98% | 21.3<br><sub>22,23,24,27,19</sub> | 9.3<br><sub>14,9,2,15,4</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,0,1,2</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 15.0 |
| Luke Kornet | 98% | 14.8<br><sub>17,14,14,17,14</sub> | 4.0<br><sub>0,1,2,8,2</sub> |  | 4.4<br><sub>4,6,8,5,1</sub> |  | 1.0<br><sub>1,1,0,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.4 |
| Harrison Barnes | 67% | 13.2<br><sub>14,-,-,21,13</sub> | 4.7<br><sub>3,-,-,13,4</sub> |  | 1.5<br><sub>0,-,-,0,2</sub> |  | 0.7<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>0,-,-,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.0 |
| Carter Bryant | 72% | 9.5<br><sub>17,5,11,14,-</sub> | 3.4<br><sub>1,3,6,3,-</sub> |  | 1.6<br><sub>1,0,0,0,-</sub> |  | 0.6<br><sub>2,0,0,0,-</sub> |  | 0.3<br><sub>0,1,2,1,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.6 |
| Jordan McLaughlin | 48% | 7.1<br><sub>7,-,-,8,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 1.3<br><sub>2,-,-,3,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.6 |
| Tarris Reed Jr. | 52% | 7.0<br><sub>5,-,-,7,-</sub> | 2.9<br><sub>4,-,-,4,-</sub> |  | 4.1<br><sub>5,-,-,7,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.6 | 7.4 |
| David Jones Garcia | 48% | 5.9<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 97% | 38.7<br><sub>33,41,37,37,42</sub> | 25.8<br><sub>19,34,38,25,22</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>3,6,5,5,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 8.0<br><sub>5,14,5,6,12</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>3,3,9,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.3 | 3.5 | 38.4 |
| Domantas Sabonis | 98% | 35.0<br><sub>37,40,38,31,35</sub> | 16.0<br><sub>20,9,11,9,16</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 13.6<br><sub>14,15,14,7,17</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 5.9<br><sub>8,7,8,4,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.3 | 2.6 | 35.6 |
| Zach LaVine | 98% | 34.4<br><sub>31,39,21,28,35</sub> | 20.3<br><sub>22,21,11,23,21</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,3,0,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>3,5,1,1,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,3,0,5,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 2.6 | 27.0 |
| Precious Achiuwa | 98% | 29.3<br><sub>14,41,25,27,17</sub> | 12.3<br><sub>4,24,6,6,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>1,9,5,10,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,2,1,3,1</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.8 | 1.1 | 21.7 |
| Leaky Black | 58% | 22.0<br><sub>8,-,-,25,22</sub> | 5.8<br><sub>2,-,-,12,3</sub> |  | 3.5<br><sub>1,-,-,3,6</sub> |  | 1.1<br><sub>1,-,-,1,1</sub> |  | 0.8<br><sub>0,-,-,4,0</sub> |  | 0.9 | 0.4 | 0.7 | 10.4 |
| Malik Monk | 98% | 21.9<br><sub>13,8,14,30,24</sub> | 11.7<br><sub>3,2,8,24,13</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,1,0,1,2</sub> |  | 3.6<br><sub>6,1,3,7,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>1,0,0,5,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.4 | 1.6 | 17.6 |
| Jonathan Mogbo | 48% | 17.0<br><sub>18,-,25,-,-</sub> | 5.3<br><sub>2,-,6,-,-</sub> |  | 2.8<br><sub>5,-,3,-,-</sub> |  | 0.9<br><sub>0,-,3,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.7 | 0.4 | 0.6 | 9.0 |
| Emanuel Sharp | 97% | 16.5<br><sub>20,18,24,20,10</sub> | 4.5<br><sub>5,0,2,9,3</sub> |  | 1.4<br><sub>0,0,1,3,1</sub> |  | 0.9<br><sub>2,0,1,1,2</sub> |  | 0.6<br><sub>1,0,0,3,1</sub> |  | 0.5 | 0.2 | 0.6 | 6.8 |
| Dylan Cardwell | 96% | 16.3<br><sub>-,-,-,-,13</sub> | 4.6<br><sub>-,-,-,-,4</sub> |  | 5.8<br><sub>-,-,-,-,6</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.9 | 0.7 | 11.5 |
| Daeqwon Plowden | 86% | 12.8<br><sub>17,-,4,3,-</sub> | 4.2<br><sub>0,-,4,1,-</sub> |  | 1.6<br><sub>2,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.3 |
| Alex Karaban | 52% | 11.6<br><sub>11,12,10,-,-</sub> | 3.8<br><sub>0,6,0,-,-</sub> |  | 1.6<br><sub>1,0,1,-,-</sub> |  | 0.6<br><sub>1,0,1,-,-</sub> |  | 0.3<br><sub>0,2,0,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 6.0 |
| Nique Clifford | 91% | 11.0<br><sub>5,4,11,3,3</sub> | 4.1<br><sub>2,0,0,0,0</sub> |  | 1.7<br><sub>0,0,1,1,2</sub> |  | 1.1<br><sub>0,1,2,0,0</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.6 | 6.9 |

</details>

<details><summary>if De'Andre Hunter plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. (SAC) | 97% | 36.0<br><sub>33,41,37,37,42</sub> | 23.3<br><sub>19,34,38,25,22</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,6,5,5,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>5,14,5,6,12</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>3,3,9,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.3 | 3.1 | 34.6 |
| Domantas Sabonis (SAC) | 98% | 32.7<br><sub>37,40,38,31,35</sub> | 14.9<br><sub>20,9,11,9,16</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 12.5<br><sub>14,15,14,7,17</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>8,7,8,4,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.3 | 2.4 | 32.6 |
| Zach LaVine (SAC) | 98% | 31.8<br><sub>31,39,21,28,35</sub> | 18.4<br><sub>22,21,11,23,21</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,3,0,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>3,5,1,1,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,3,0,5,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 2.4 | 24.5 |
| De'Andre Hunter (SAC) | 100% | 30.6<br><sub>33,37,32,36,38</sub> | 13.5<br><sub>24,24,19,6,14</sub> | 11.5 · – | 4.5<br><sub>6,5,3,7,2</sub> | 4.5 | 1.6<br><sub>2,1,0,2,2</sub> | 1.5 | 1.8<br><sub>5,4,2,0,1</sub> | 1.5 | 0.8 | 0.2 | 1.4 | 19.6 |
| Precious Achiuwa (SAC) | 98% | 25.8<br><sub>14,41,25,27,17</sub> | 10.9<br><sub>4,24,6,6,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>1,9,5,10,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>0,2,1,3,1</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 1.0 | 0.8 | 1.0 | 19.1 |
| Malik Monk (SAC) | 98% | 19.1<br><sub>13,8,14,30,24</sub> | 10.0<br><sub>3,2,8,24,13</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>2,1,0,1,2</sub> |  | 3.1<br><sub>6,1,3,7,3</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>1,0,0,5,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.5 | 0.3 | 1.4 | 15.1 |
| Leaky Black (SAC) | 58% | 18.3<br><sub>8,-,-,25,22</sub> | 4.7<br><sub>2,-,-,12,3</sub> |  | 3.0<br><sub>1,-,-,3,6</sub> |  | 0.9<br><sub>1,-,-,1,1</sub> |  | 0.6<br><sub>0,-,-,4,0</sub> |  | 0.8 | 0.3 | 0.5 | 8.6 |
| Dylan Cardwell (SAC) | 96% | 14.5<br><sub>-,-,-,-,13</sub> | 4.0<br><sub>-,-,-,-,4</sub> |  | 5.3<br><sub>-,-,-,-,6</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.8 | 0.6 | 10.3 |
| Emanuel Sharp (SAC) | 97% | 13.8<br><sub>20,18,24,20,10</sub> | 3.8<br><sub>5,0,2,9,3</sub> |  | 1.2<br><sub>0,0,1,3,1</sub> |  | 0.8<br><sub>2,0,1,1,2</sub> |  | 0.4<br><sub>1,0,0,3,1</sub> |  | 0.4 | 0.2 | 0.5 | 5.8 |
| Jonathan Mogbo (SAC) | 48% | 12.0<br><sub>18,-,25,-,-</sub> | 3.8<br><sub>2,-,6,-,-</sub> |  | 1.9<br><sub>5,-,3,-,-</sub> |  | 0.6<br><sub>0,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 6.4 |
| Nique Clifford (SAC) | 91% | 8.2<br><sub>5,4,11,3,3</sub> | 3.3<br><sub>2,0,0,0,0</sub> |  | 1.2<br><sub>0,0,1,1,2</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Daeqwon Plowden (SAC) | 86% | 8.0<br><sub>17,-,4,3,-</sub> | 2.7<br><sub>0,-,4,1,-</sub> |  | 1.0<br><sub>2,-,0,1,-</sub> |  | 0.3<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Alex Karaban (SAC) | 52% | 7.5<br><sub>11,12,10,-,-</sub> | 2.6<br><sub>0,6,0,-,-</sub> |  | 1.0<br><sub>1,0,1,-,-</sub> |  | 0.4<br><sub>1,0,1,-,-</sub> |  | 0.2<br><sub>0,2,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.0 |
| Victor Wembanyama (SAS) | 98% | 32.8<br><sub>27,39,34,24,34</sub> | 28.3<br><sub>29,36,43,12,52</sub> | 28.5 · –<br><sub>o 48% · u 52%</sub> | 11.4<br><sub>10,14,7,11,24</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,5,4,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>0,4,3,0,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 3.9 | 2.5 | 43.0 |
| Dylan Harper (SAS) | 98% | 32.5<br><sub>30,37,39,27,36</sub> | 17.1<br><sub>13,13,25,17,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>6,5,7,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>6,8,6,8,0</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.4 | 2.0 | 27.4 |
| Devin Vassell (SAS) | 98% | 32.5<br><sub>24,38,34,25,36</sub> | 13.6<br><sub>14,21,9,11,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,5,5,2,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>8,2,2,1,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>4,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.5 | 1.1 | 21.0 |
| De'Aaron Fox (SAS) | 98% | 31.5<br><sub>26,39,35,22,33</sub> | 16.0<br><sub>11,14,22,12,10</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>4,3,8,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>6,4,7,3,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,1,0,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.4 | 2.1 | 26.1 |
| Stephon Castle (SAS) | 98% | 31.0<br><sub>27,38,22,26,35</sub> | 17.1<br><sub>15,14,0,16,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,6,5,5,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>5,8,4,4,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.9 | 28.8 |
| Julian Champagnie (SAS) | 98% | 25.5<br><sub>25,31,27,22,21</sub> | 9.3<br><sub>26,6,12,8,0</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>3,6,3,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,0,1,0,3</sub> |  | 1.8<br><sub>8,2,3,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 0.8 | 15.2 |
| Keldon Johnson (SAS) | 98% | 21.3<br><sub>22,23,24,27,19</sub> | 9.3<br><sub>14,9,2,15,4</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,0,1,2</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.1 | 0.9 | 15.1 |
| Luke Kornet (SAS) | 98% | 14.7<br><sub>17,14,14,17,14</sub> | 3.9<br><sub>0,1,2,8,2</sub> |  | 4.4<br><sub>4,6,8,5,1</sub> |  | 1.0<br><sub>1,1,0,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.4 |
| Harrison Barnes (SAS) | 67% | 13.3<br><sub>14,-,-,21,13</sub> | 4.8<br><sub>3,-,-,13,4</sub> |  | 1.6<br><sub>0,-,-,0,2</sub> |  | 0.7<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>0,-,-,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.1 |
| Carter Bryant (SAS) | 72% | 9.4<br><sub>17,5,11,14,-</sub> | 3.3<br><sub>1,3,6,3,-</sub> |  | 1.6<br><sub>1,0,0,0,-</sub> |  | 0.6<br><sub>2,0,0,0,-</sub> |  | 0.3<br><sub>0,1,2,1,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.5 |
| Jordan McLaughlin (SAS) | 48% | 7.2<br><sub>7,-,-,8,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 1.3<br><sub>2,-,-,3,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.8 |
| Tarris Reed Jr. (SAS) | 52% | 7.0<br><sub>5,-,-,7,-</sub> | 2.9<br><sub>4,-,-,4,-</sub> |  | 4.1<br><sub>5,-,-,7,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.5 | 7.3 |
| David Jones Garcia (SAS) | 48% | 5.9<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-06/`._
