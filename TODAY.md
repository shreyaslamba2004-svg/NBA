# NBA model · Mon 09 Nov 2026 (US date)

Updated **Tue 10 Nov, 03:32 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-09/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

4 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| DEN @ HOU | team minutes | DEN players add up to 206 expected minutes (normal is about 240) | 81% of tonight's minutes go to players new to DEN since last season, and the team ratings still lean on last season; DEN out: Strawther |
| DEN @ HOU | player minutes | Tyus Jones projected 28 min; most in his last 10 games is 18 | minutes 28 vs 11 this season; new team (was ORL last season); teammates out: Strawther (~15 min a game) |
| CLE @ CHA | player points | Coby White projected 19.6 pts vs DraftKings line 14.5 | minutes 28 vs 17 this season; new team (was CHI last season); scoring 0.71/min vs 0.36 this season, 0.69 last season; teammates out: Miller, Schroder, Williams (~81 min a game) |
| LAL @ ATL | player points | Austin Reaves projected 27.4 pts vs DraftKings line 20.5 | minutes 38 vs 36 this season; scoring 0.72/min vs 0.70 this season, 0.68 last season |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard AST over 11.5 (12+) | IND @ DAL | draftkings | 17.40 | 13.77 | 5.08 | 19.7% | 5.4% | 7.3% | +26.4% | +242.8% | 0.4% |
| Andrew Nembhard PRA over 39.5 (40+) | IND @ DAL | draftkings | 16.20 | 14.45 | 6.92 | 14.4% | 5.8% | 6.9% | +12.0% | +134.2% | 0.2% |
| Daniss Jenkins AST over 7.5 (8+) | WAS @ DET | draftkings | 11.60 | 10.63 | 5.45 | 18.3% | 8.1% | 9.4% | +9.2% | +112.8% | 0.2% |
| Pascal Siakam PTS over 34.5 (35+) | IND @ DAL | draftkings | 14.40 | 13.46 | 7.33 | 13.6% | 6.5% | 7.4% | +7.0% | +96.5% | 0.1% |
| Pascal Siakam PTS over 39.5 (40+) | IND @ DAL | draftkings | 29.00 | 27.10 | 14.81 | 6.8% | 3.2% | 3.7% | +7.0% | +95.8% | 0.1% |
| WAS to win | WAS @ DET | unibet | 5.30 | 4.96 | 3.42 | 29.3% | 20.2% | 20.2% | +6.9% | +55.1% | 0.4% |
| Pascal Siakam AST over 7.5 (8+) | IND @ DAL | draftkings | 20.60 | 19.31 | 10.59 | 9.4% | 4.5% | 5.2% | +6.8% | +94.6% | 0.1% |
| Daniss Jenkins AST over 9.5 (10+) | WAS @ DET | draftkings | 28.00 | 26.32 | 14.68 | 6.8% | 3.3% | 3.8% | +6.3% | +90.8% | 0.1% |
| Jeremiah Fears AST over 7.5 (8+) | NOP @ GSW | draftkings | 18.60 | 17.70 | 10.22 | 9.8% | 5.0% | 5.7% | +5.1% | +82.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ ATL | Tue 10 Nov 11:00 | 113.5–116.6 | LAL 41% | 2.42 / 1.70 | ATL -3.5 | 229.5 | ATL -1.5 covers 56%; o237.5 34% |
| CLE @ CHA | Tue 10 Nov 11:00 | 111.8–104.9 | CLE 69% | 1.45 / 3.24 | CHA +6.5 | 216.5 | CHA +8.5 covers 54%; o214.5 54% |
| WAS @ DET | Tue 10 Nov 11:00 | 109.0–116.9 | WAS 29% | 3.50 / 1.40 | DET -7.5 | 225.5 | DET -10.5 covers 43%; o217.5 68% |
| MEM @ TOR | Tue 10 Nov 11:30 | 115.3–117.4 | MEM 44% | 2.26 / 1.79 | TOR -2.5 | 232.5 | TOR -3.5 covers 47%; o229.5 56% |
| IND @ DAL | Tue 10 Nov 12:00 | 112.9–117.8 | IND 36% | 2.77 / 1.56 | DAL -5.5 | 230.5 | DAL -3.5 covers 55%; o226.5 59% |
| DEN @ HOU | Tue 10 Nov 12:30 | 109.3–118.2 | DEN 26% | 3.78 / 1.36 | HOU -8.5 | 227.5 | HOU -9.5 covers 49%; o219.5 67% |
| SAS @ PHX | Tue 10 Nov 13:00 | 117.1–109.4 | SAS 71% | 1.41 / 3.44 | PHX +7.5 | 226.5 | PHX +8.5 covers 52%; o227.5 47% |
| NOP @ GSW | Tue 10 Nov 14:00 | 113.6–122.9 | NOP 26% | 3.89 / 1.35 | GSW -9.5 | 236.5 | GSW -9.5 covers 49%; o232.5 58% |

### LAL @ ATL
Out: Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Asa Newell (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.5–116.6 | LAL 41% | 2.42 / 1.70 | ATL -3.5 | 229.5 | ATL -1.5 covers 56%; o237.5 34% |
| Expected (weighted by chance each plays) | 115.1–117.7 | LAL 43% | 2.35 / 1.74 | ATL -2.5 | 232.5 | ATL -1.5 covers 54%; o237.5 41% |
| if Luka Doncic plays | 116.0–116.7 | LAL 48% | 2.08 / 1.92 | ATL -1.5 | 232.5 | ATL -1.5 covers 49%; o237.5 40% |
| if Quentin Grimes plays | 114.4–117.0 | LAL 43% | 2.35 / 1.74 | ATL -2.5 | 231.5 | ATL -1.5 covers 54%; o237.5 37% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Questionable | 55% | 8.2 | 3.0 | 1.3 | 0.6 | 0.2 | 0.2 | 0.0 | 0.4 | 4.9 | small |
| Luka Doncic (LAL) | Day-To-Day | 70% | 37.0 | 35.3 | 7.6 | 7.7 | 4.8 | 1.8 | 0.5 | 4.5 | 50.6 | full tables below |
| Jock Landale (ATL) | Questionable | 55% | 9.4 | 4.2 | 2.4 | 0.8 | 0.3 | 0.3 | 0.2 | 0.4 | 7.3 | small |
| Quentin Grimes (LAL) | Day-To-Day | 70% | 28.3 | 11.0 | 3.1 | 2.8 | 1.2 | 0.9 | 0.3 | 1.7 | 16.8 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Austin Reaves | 98% | 37.9<br><sub>39,34,37,38,37</sub> | 27.4<br><sub>19,27,21,25,43</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>3,2,3,3,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>4,5,4,2,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>2,4,1,1,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.5 | 4.1 | 38.0 |
| Walker Kessler | 98% | 32.5<br><sub>31,32,29,37,29</sub> | 13.7<br><sub>16,15,15,16,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 12.5<br><sub>15,15,8,12,16</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>1,2,0,2,4</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.0 | 2.3 | 28.3 |
| Matisse Thybulle | 98% | 28.1<br><sub>25,19,23,24,28</sub> | 8.4<br><sub>6,6,3,2,4</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>2,1,1,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>3,2,2,0,0</sub> |  | 1.3<br><sub>2,2,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 2.2 | 0.9 | 1.4 | 12.6 |
| Jake LaRavia | 97% | 27.4<br><sub>25,26,21,25,29</sub> | 8.1<br><sub>8,7,9,7,5</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>2,4,2,8,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>4,2,2,3,2</sub> |  | 0.8<br><sub>2,1,2,2,0</sub> |  | 1.4 | 0.8 | 1.5 | 14.5 |
| Ziaire Williams | 98% | 25.5<br><sub>-,15,23,20,21</sub> | 11.9<br><sub>-,9,10,8,17</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>-,2,4,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,2,1,1,0</sub> |  | 1.4<br><sub>-,3,1,2,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.5 | 0.4 | 1.2 | 16.7 |
| Collin Sexton | 98% | 25.1<br><sub>19,16,16,11,24</sub> | 16.3<br><sub>14,6,10,0,17</sub> |  | 2.8<br><sub>3,1,3,0,2</sub> |  | 3.2<br><sub>3,5,1,1,2</sub> |  | 1.5<br><sub>1,0,1,0,0</sub> |  | 1.1 | 0.2 | 2.2 | 22.2 |
| Sandro Mamukelashvili | 98% | 23.5<br><sub>24,28,19,20,18</sub> | 10.6<br><sub>11,13,2,7,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>1,3,6,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>1,4,1,1,0</sub> |  | 1.1<br><sub>2,2,0,1,1</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.9 | 0.6 | 1.1 | 17.8 |
| Jarred Vanderbilt | 67% | 15.8<br><sub>12,6,7,-,14</sub> | 3.9<br><sub>4,2,0,-,2</sub> |  | 4.6<br><sub>3,1,1,-,10</sub> |  | 1.4<br><sub>1,0,0,-,3</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.8 | 0.2 | 0.8 | 9.9 |
| Lawson Lovering | 52% | 13.6<br><sub>-,1,1,-,-</sub> | 4.0<br><sub>-,0,0,-,-</sub> |  | 3.5<br><sub>-,1,0,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.6 | 0.5 | 0.8 | 8.4 |
| Jaden Hardy | 52% | 12.0<br><sub>1,1,1,-,-</sub> | 6.3<br><sub>1,2,0,-,-</sub> |  | 1.1<br><sub>0,0,0,-,-</sub> |  | 0.9<br><sub>0,0,1,-,-</sub> |  | 0.8<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.9 | 8.3 |
| Adou Thiero | 88% | 11.8<br><sub>-,-,-,7,8</sub> | 4.2<br><sub>-,-,-,4,2</sub> |  | 3.3<br><sub>-,-,-,4,2</sub> |  | 0.8<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 8.2 |
| Chris Manon | 58% | 9.6<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.4 | 4.9 |
| Bronny James | 58% | 8.8<br><sub>2,1,1,-,-</sub> | 3.0<br><sub>0,2,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.7<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 4.0 |
| AK Okereke | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.1 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Kevon Looney | 30% | 8.4<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 3.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 5.8 |
| Cameron Carr | 64% | 8.3<br><sub>1,1,1,-,-</sub> | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.8<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 1.5 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 34.9<br><sub>28,-,-,-,36</sub> | 20.0<br><sub>13,-,-,-,30</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 9.0<br><sub>7,-,-,-,7</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>4,-,-,-,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,-,-,-,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.5 | 3.4 | 36.1 |
| Nickeil Alexander-Walker | 98% | 32.4<br><sub>29,31,32,33,31</sub> | 20.3<br><sub>12,34,26,28,20</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,4,4,2,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>1,4,2,2,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>0,9,6,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.4 | 2.4 | 26.3 |
| Dyson Daniels | 98% | 31.5<br><sub>27,31,34,35,31</sub> | 11.1<br><sub>8,6,8,13,9</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>4,9,16,9,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>3,4,8,12,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.4 | 0.4 | 1.7 | 23.4 |
| Onyeka Okongwu | 98% | 31.2<br><sub>28,33,31,33,30</sub> | 13.8<br><sub>6,13,14,22,16</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>10,10,16,10,2</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>1,3,4,1,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.8 | 1.4 | 23.8 |
| CJ McCollum | 98% | 25.7<br><sub>24,32,25,23,21</sub> | 14.7<br><sub>14,13,15,4,9</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>2,9,5,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.5<br><sub>2,12,5,4,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,2,2,0,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 2.0 | 21.0 |
| Aaron Wiggins | 98% | 24.6<br><sub>23,24,29,29,26</sub> | 12.5<br><sub>10,7,15,19,20</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,3,4,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,2,2,3,6</sub> |  | 1.9<br><sub>2,1,3,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.2 | 17.7 |
| Luguentz Dort | 98% | 24.2<br><sub>29,31,31,32,20</sub> | 8.2<br><sub>11,14,6,25,3</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>3,2,3,7,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,3,4,1</sub> |  | 1.3<br><sub>1,4,2,5,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 0.7 | 12.6 |
| Kingston Flemings | 88% | 22.6<br><sub>25,-,23,25,27</sub> | 8.7<br><sub>12,-,14,11,10</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>2,-,3,1,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>6,-,4,6,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>1,-,2,1,0</sub> |  | 0.8 | 0.3 | 2.0 | 15.2 |
| Zuby Ejiofor | 71% | 13.9<br><sub>-,15,17,15,18</sub> | 5.4<br><sub>-,3,11,10,7</sub> |  | 3.1<br><sub>-,5,3,5,6</sub> |  | 1.4<br><sub>-,2,2,5,0</sub> |  | 0.4<br><sub>-,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 9.9 |
| Corey Kispert | 63% | 10.9<br><sub>5,18,8,16,-</sub> | 5.4<br><sub>0,14,9,7,-</sub> |  | 1.3<br><sub>0,1,0,2,-</sub> |  | 0.8<br><sub>1,0,1,1,-</sub> |  | 0.7<br><sub>0,4,1,1,-</sub> |  | 0.2 | 0.1 | 0.5 | 7.6 |
| RayJ Dennis | 40% | 7.2<br><sub>-,8,-,-,-</sub> | 2.5<br><sub>-,4,-,-,-</sub> |  | 0.9<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,2,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Dorian Finney-Smith | 35% | 6.4<br><sub>3,-,-,-,-</sub> | 1.8<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.1 |

</details>

<details><summary>if Luka Doncic plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 34.9<br><sub>28,-,-,-,36</sub> | 20.0<br><sub>13,-,-,-,30</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 9.0<br><sub>7,-,-,-,7</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>4,-,-,-,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,-,-,-,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.4 | 3.4 | 36.0 |
| Nickeil Alexander-Walker (ATL) | 98% | 32.5<br><sub>29,31,32,33,31</sub> | 20.4<br><sub>12,34,26,28,20</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,4,4,2,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>1,4,2,2,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>0,9,6,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.4 | 2.4 | 26.4 |
| Dyson Daniels (ATL) | 98% | 31.5<br><sub>27,31,34,35,31</sub> | 11.1<br><sub>8,6,8,13,9</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>4,9,16,9,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>3,4,8,12,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.4 | 0.4 | 1.7 | 23.4 |
| Onyeka Okongwu (ATL) | 98% | 31.2<br><sub>28,33,31,33,30</sub> | 13.8<br><sub>6,13,14,22,16</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>10,10,16,10,2</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>1,3,4,1,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.8 | 1.4 | 23.7 |
| CJ McCollum (ATL) | 98% | 25.7<br><sub>24,32,25,23,21</sub> | 14.7<br><sub>14,13,15,4,9</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>2,9,5,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.5<br><sub>2,12,5,4,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,2,2,0,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 2.0 | 21.0 |
| Aaron Wiggins (ATL) | 98% | 24.6<br><sub>23,24,29,29,26</sub> | 12.6<br><sub>10,7,15,19,20</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,3,4,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,2,2,3,6</sub> |  | 1.9<br><sub>2,1,3,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.3 | 17.7 |
| Luguentz Dort (ATL) | 98% | 24.1<br><sub>29,31,31,32,20</sub> | 8.2<br><sub>11,14,6,25,3</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>3,2,3,7,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,0,3,4,1</sub> |  | 1.3<br><sub>1,4,2,5,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 0.7 | 12.5 |
| Kingston Flemings (ATL) | 88% | 22.6<br><sub>25,-,23,25,27</sub> | 8.7<br><sub>12,-,14,11,10</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>2,-,3,1,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>6,-,4,6,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>1,-,2,1,0</sub> |  | 0.8 | 0.3 | 2.0 | 15.2 |
| Zuby Ejiofor (ATL) | 71% | 14.0<br><sub>-,15,17,15,18</sub> | 5.4<br><sub>-,3,11,10,7</sub> |  | 3.1<br><sub>-,5,3,5,6</sub> |  | 1.4<br><sub>-,2,2,5,0</sub> |  | 0.4<br><sub>-,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 9.9 |
| Corey Kispert (ATL) | 63% | 11.0<br><sub>5,18,8,16,-</sub> | 5.4<br><sub>0,14,9,7,-</sub> |  | 1.3<br><sub>0,1,0,2,-</sub> |  | 0.8<br><sub>1,0,1,1,-</sub> |  | 0.7<br><sub>0,4,1,1,-</sub> |  | 0.2 | 0.1 | 0.5 | 7.6 |
| RayJ Dennis (ATL) | 40% | 7.1<br><sub>-,8,-,-,-</sub> | 2.5<br><sub>-,4,-,-,-</sub> |  | 0.9<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,2,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.5 |
| Dorian Finney-Smith (ATL) | 35% | 6.3<br><sub>3,-,-,-,-</sub> | 1.8<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.1 |
| Luka Doncic (LAL) | 100% | 37.0<br><sub>35,36,35,38,-</sub> | 35.3<br><sub>45,42,40,53,-</sub> | 33.5 · – | 7.6<br><sub>15,7,9,5,-</sub> | 7.5 | 7.7<br><sub>6,13,7,5,-</sub> | 7.5 | 4.8<br><sub>8,6,6,5,-</sub> | 4.5 | 1.8 | 0.5 | 4.5 | 50.6 |
| Austin Reaves (LAL) | 98% | 36.9<br><sub>39,34,37,38,37</sub> | 22.3<br><sub>19,27,21,25,43</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>3,2,3,3,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>4,5,4,2,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,4,1,1,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.5 | 3.4 | 31.4 |
| Walker Kessler (LAL) | 98% | 30.6<br><sub>31,32,29,37,29</sub> | 11.1<br><sub>16,15,15,16,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 12.0<br><sub>15,15,8,12,16</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,2,0,2,4</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.0 | 1.7 | 24.7 |
| Jake LaRavia (LAL) | 97% | 24.2<br><sub>25,26,21,25,29</sub> | 6.2<br><sub>8,7,9,7,5</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,4,2,8,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>4,2,2,3,2</sub> |  | 0.6<br><sub>2,1,2,2,0</sub> |  | 1.2 | 0.7 | 1.1 | 11.6 |
| Matisse Thybulle (LAL) | 98% | 24.2<br><sub>25,19,23,24,28</sub> | 6.6<br><sub>6,6,3,2,4</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,1,1,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>3,2,2,0,0</sub> |  | 1.0<br><sub>2,2,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 2.0 | 0.8 | 0.9 | 9.9 |
| Ziaire Williams (LAL) | 98% | 21.6<br><sub>-,15,23,20,21</sub> | 8.3<br><sub>-,9,10,8,17</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>-,2,4,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>-,2,1,1,0</sub> |  | 1.1<br><sub>-,3,1,2,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.3 | 0.9 | 12.1 |
| Sandro Mamukelashvili (LAL) | 98% | 20.0<br><sub>24,28,19,20,18</sub> | 7.6<br><sub>11,13,2,7,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>1,3,6,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>1,4,1,1,0</sub> |  | 0.8<br><sub>2,2,0,1,1</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.7 | 0.5 | 0.8 | 13.4 |
| Collin Sexton (LAL) | 98% | 19.0<br><sub>19,16,16,11,24</sub> | 10.6<br><sub>14,6,10,0,17</sub> |  | 2.1<br><sub>3,1,3,0,2</sub> |  | 1.9<br><sub>3,5,1,1,2</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.8 | 0.2 | 1.6 | 14.5 |
| Jarred Vanderbilt (LAL) | 67% | 12.1<br><sub>12,6,7,-,14</sub> | 3.0<br><sub>4,2,0,-,2</sub> |  | 3.5<br><sub>3,1,1,-,10</sub> |  | 0.9<br><sub>1,0,0,-,3</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.2 | 0.6 | 7.4 |
| Arthur Kaluma (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Adou Thiero (LAL) | 88% | 8.1<br><sub>-,-,-,7,8</sub> | 2.7<br><sub>-,-,-,4,2</sub> |  | 2.3<br><sub>-,-,-,4,2</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Lawson Lovering (LAL) | 52% | 7.8<br><sub>-,1,1,-,-</sub> | 2.3<br><sub>-,0,0,-,-</sub> |  | 2.1<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.9 |
| Jaden Hardy (LAL) | 52% | 6.9<br><sub>1,1,1,-,-</sub> | 3.6<br><sub>1,2,0,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,1,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.7 |
| Kevon Looney (LAL) | 30% | 6.9<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.8 |
| Chris Manon (LAL) | 58% | 6.0<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.2 |
| Cameron Carr (LAL) | 64% | 5.7<br><sub>1,1,1,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.0 |
| Bronny James (LAL) | 58% | 5.7<br><sub>2,1,1,-,-</sub> | 2.4<br><sub>0,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.1 |

</details>

<details><summary>if Quentin Grimes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 34.9<br><sub>28,-,-,-,36</sub> | 20.1<br><sub>13,-,-,-,30</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 9.0<br><sub>7,-,-,-,7</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>4,-,-,-,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,-,-,-,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.5 | 3.4 | 36.2 |
| Nickeil Alexander-Walker (ATL) | 98% | 32.5<br><sub>29,31,32,33,31</sub> | 20.4<br><sub>12,34,26,28,20</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,4,4,2,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>1,4,2,2,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>0,9,6,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.4 | 2.4 | 26.4 |
| Dyson Daniels (ATL) | 98% | 31.5<br><sub>27,31,34,35,31</sub> | 11.1<br><sub>8,6,8,13,9</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>4,9,16,9,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>3,4,8,12,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.4 | 0.4 | 1.7 | 23.4 |
| Onyeka Okongwu (ATL) | 98% | 31.2<br><sub>28,33,31,33,30</sub> | 13.8<br><sub>6,13,14,22,16</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>10,10,16,10,2</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>1,3,4,1,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.8 | 1.4 | 23.8 |
| CJ McCollum (ATL) | 98% | 25.6<br><sub>24,32,25,23,21</sub> | 14.7<br><sub>14,13,15,4,9</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>2,9,5,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.5<br><sub>2,12,5,4,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,2,2,0,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 2.0 | 21.1 |
| Aaron Wiggins (ATL) | 98% | 24.5<br><sub>23,24,29,29,26</sub> | 12.4<br><sub>10,7,15,19,20</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,3,4,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,2,2,3,6</sub> |  | 1.9<br><sub>2,1,3,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.3 | 17.6 |
| Luguentz Dort (ATL) | 98% | 24.2<br><sub>29,31,31,32,20</sub> | 8.3<br><sub>11,14,6,25,3</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>3,2,3,7,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,3,4,1</sub> |  | 1.3<br><sub>1,4,2,5,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 0.7 | 12.6 |
| Kingston Flemings (ATL) | 88% | 22.6<br><sub>25,-,23,25,27</sub> | 8.7<br><sub>12,-,14,11,10</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>2,-,3,1,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>6,-,4,6,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>1,-,2,1,0</sub> |  | 0.8 | 0.3 | 1.9 | 15.2 |
| Zuby Ejiofor (ATL) | 71% | 14.1<br><sub>-,15,17,15,18</sub> | 5.5<br><sub>-,3,11,10,7</sub> |  | 3.2<br><sub>-,5,3,5,6</sub> |  | 1.4<br><sub>-,2,2,5,0</sub> |  | 0.5<br><sub>-,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.1 |
| Corey Kispert (ATL) | 63% | 11.0<br><sub>5,18,8,16,-</sub> | 5.4<br><sub>0,14,9,7,-</sub> |  | 1.3<br><sub>0,1,0,2,-</sub> |  | 0.8<br><sub>1,0,1,1,-</sub> |  | 0.7<br><sub>0,4,1,1,-</sub> |  | 0.2 | 0.1 | 0.5 | 7.6 |
| RayJ Dennis (ATL) | 40% | 7.3<br><sub>-,8,-,-,-</sub> | 2.5<br><sub>-,4,-,-,-</sub> |  | 1.0<br><sub>-,2,-,-,-</sub> |  | 1.1<br><sub>-,2,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.5 |
| Dorian Finney-Smith (ATL) | 35% | 6.3<br><sub>3,-,-,-,-</sub> | 1.8<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.0 |
| Austin Reaves (LAL) | 98% | 36.9<br><sub>39,34,37,38,37</sub> | 27.2<br><sub>19,27,21,25,43</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>3,2,3,3,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>4,5,4,2,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,4,1,1,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.5 | 3.8 | 37.3 |
| Walker Kessler (LAL) | 98% | 31.4<br><sub>31,32,29,37,29</sub> | 13.2<br><sub>16,15,15,16,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 12.2<br><sub>15,15,8,12,16</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,0,2,4</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.0 | 2.1 | 27.4 |
| Quentin Grimes (LAL) | 100% | 28.3<br><sub>26,23,25,20,32</sub> | 11.0<br><sub>7,7,6,2,12</sub> |  | 3.1<br><sub>1,4,1,0,1</sub> |  | 2.8<br><sub>3,4,1,0,4</sub> |  | 1.2<br><sub>1,1,0,0,2</sub> |  | 0.9 | 0.3 | 1.7 | 16.8 |
| Matisse Thybulle (LAL) | 98% | 25.8<br><sub>25,19,23,24,28</sub> | 7.8<br><sub>6,6,3,2,4</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>2,1,1,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>3,2,2,0,0</sub> |  | 1.2<br><sub>2,2,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 2.1 | 0.8 | 1.1 | 11.8 |
| Jake LaRavia (LAL) | 97% | 25.6<br><sub>25,26,21,25,29</sub> | 7.7<br><sub>8,7,9,7,5</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>2,4,2,8,1</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,2,3,2</sub> |  | 0.8<br><sub>2,1,2,2,0</sub> |  | 1.3 | 0.7 | 1.4 | 13.8 |
| Ziaire Williams (LAL) | 98% | 23.1<br><sub>-,15,23,20,21</sub> | 10.8<br><sub>-,9,10,8,17</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>-,2,4,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>-,2,1,1,0</sub> |  | 1.3<br><sub>-,3,1,2,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.4 | 1.3 | 15.1 |
| Collin Sexton (LAL) | 98% | 22.1<br><sub>19,16,16,11,24</sub> | 14.2<br><sub>14,6,10,0,17</sub> |  | 2.5<br><sub>3,1,3,0,2</sub> |  | 2.6<br><sub>3,5,1,1,2</sub> |  | 1.3<br><sub>1,0,1,0,0</sub> |  | 1.0 | 0.2 | 2.1 | 19.3 |
| Sandro Mamukelashvili (LAL) | 98% | 21.2<br><sub>24,28,19,20,18</sub> | 9.7<br><sub>11,13,2,7,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>1,3,6,3,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>1,4,1,1,0</sub> |  | 1.0<br><sub>2,2,0,1,1</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.8 | 0.5 | 1.0 | 16.1 |
| Jarred Vanderbilt (LAL) | 67% | 13.0<br><sub>12,6,7,-,14</sub> | 3.5<br><sub>4,2,0,-,2</sub> |  | 3.8<br><sub>3,1,1,-,10</sub> |  | 1.2<br><sub>1,0,0,-,3</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.4 |
| Lawson Lovering (LAL) | 52% | 9.3<br><sub>-,1,1,-,-</sub> | 2.9<br><sub>-,0,0,-,-</sub> |  | 2.5<br><sub>-,1,0,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 6.0 |
| Adou Thiero (LAL) | 88% | 9.2<br><sub>-,-,-,7,8</sub> | 3.2<br><sub>-,-,-,4,2</sub> |  | 2.6<br><sub>-,-,-,4,2</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 6.4 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| AK Okereke (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Jaden Hardy (LAL) | 52% | 7.7<br><sub>1,1,1,-,-</sub> | 4.5<br><sub>1,2,0,-,-</sub> |  | 0.7<br><sub>0,0,0,-,-</sub> |  | 0.6<br><sub>0,0,1,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.6 | 5.7 |
| Kevon Looney (LAL) | 30% | 7.3<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.8<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.2 |
| Chris Manon (LAL) | 58% | 6.9<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Bronny James (LAL) | 58% | 6.0<br><sub>2,1,1,-,-</sub> | 2.4<br><sub>0,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.1 |
| Cameron Carr (LAL) | 64% | 5.9<br><sub>1,1,1,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.1 |

</details>


### CLE @ CHA
Out: PJ Hall (CHA), Kon Knueppel (CHA), Brandon Miller (CHA), Dennis Schroder (CHA), Grant Williams (CHA), Sam Merrill (CLE), Jaylon Tyson (CLE)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.8–104.9 | CLE 69% | 1.45 / 3.24 | CHA +6.5 | 216.5 | CHA +8.5 covers 54%; o214.5 54% |
| Expected (weighted by chance each plays) | 111.4–105.3 | CLE 67% | 1.49 / 3.06 | CHA +6.5 | 216.5 | CHA +8.5 covers 56%; o214.5 54% |
| if Moussa Diabate plays | 110.0–105.4 | CLE 63% | 1.59 / 2.71 | CHA +4.5 | 215.5 | CHA +8.5 covers 61%; o214.5 51% |
| if Jarrett Allen plays | 112.8–105.4 | CLE 71% | 1.42 / 3.40 | CHA +7.5 | 217.5 | CHA +8.5 covers 53%; o214.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Moussa Diabate (CHA) | Questionable | 55% | 30.2 | 9.1 | 9.8 | 2.6 | 0.0 | 1.1 | 0.8 | 1.7 | 21.5 | full tables below |
| Jarrett Allen (CLE) | Questionable | 55% | 26.1 | 11.6 | 6.8 | 1.4 | 0.1 | 0.9 | 1.2 | 1.1 | 19.8 | full tables below |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 98% | 36.6<br><sub>24,36,33,33,37</sub> | 26.4<br><sub>15,17,27,23,37</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>4,5,3,7,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>3,11,6,8,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>2,4,5,1,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.3 | 2.9 | 36.7 |
| James Harden | 98% | 36.4<br><sub>26,33,35,30,34</sub> | 18.2<br><sub>13,14,19,17,7</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>6,4,9,6,2</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.5<br><sub>7,6,6,3,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>3,3,3,3,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 3.3 | 29.6 |
| Evan Mobley | 98% | 35.3<br><sub>25,33,33,32,33</sub> | 16.6<br><sub>27,16,16,22,12</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 8.2<br><sub>5,7,10,6,9</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,4,3,4,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>3,1,1,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 1.6 | 1.8 | 28.6 |
| Peyton Watson | 98% | 31.6<br><sub>22,-,-,28,29</sub> | 13.9<br><sub>5,-,-,13,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>2,-,-,9,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>6,-,-,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>1,-,-,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1 | 1.2 | 1.7 | 21.3 |
| Meleek Thomas | 88% | 26.2<br><sub>23,26,18,27,24</sub> | 10.7<br><sub>13,17,9,12,9</sub> |  | 2.9<br><sub>1,5,1,1,4</sub> |  | 1.4<br><sub>2,1,0,3,0</sub> |  | 1.6<br><sub>3,3,3,2,3</sub> |  | 0.9 | 0.2 | 1.2 | 15.1 |
| Tyrese Proctor | 91% | 23.3<br><sub>18,19,22,19,23</sub> | 8.2<br><sub>9,10,11,3,7</sub> |  | 3.3<br><sub>4,4,1,6,3</sub> |  | 2.6<br><sub>5,2,0,3,3</sub> |  | 1.3<br><sub>3,2,2,0,2</sub> |  | 0.9 | 0.1 | 1.0 | 14.1 |
| Mario Hezonja | 98% | 22.8<br><sub>20,27,23,27,19</sub> | 9.1<br><sub>8,12,12,15,0</sub> |  | 5.8<br><sub>11,8,8,10,5</sub> |  | 1.5<br><sub>4,3,1,1,1</sub> |  | 1.3<br><sub>1,3,2,2,0</sub> |  | 0.7 | 0.2 | 1.0 | 16.4 |
| Thomas Bryant | 71% | 16.0<br><sub>11,5,13,16,15</sub> | 7.1<br><sub>11,4,8,13,5</sub> |  | 3.7<br><sub>2,0,0,6,3</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>3,0,1,1,1</sub> |  | 0.4 | 0.5 | 0.7 | 11.5 |
| Craig Porter Jr. | 88% | 14.8<br><sub>16,8,14,3,15</sub> | 3.3<br><sub>2,0,0,0,0</sub> |  | 2.5<br><sub>2,4,1,0,1</sub> |  | 2.1<br><sub>4,1,1,0,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.4 | 0.7 | 7.8 |
| Riley Minix | 48% | 11.5<br><sub>6,-,-,-,10</sub> | 4.2<br><sub>0,-,-,-,8</sub> |  | 1.8<br><sub>3,-,-,-,3</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,2</sub> |  | 0.3 | 0.1 | 0.4 | 6.5 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Norchad Omier | 52% | 7.7<br><sub>-,-,-,3,-</sub> | 2.2<br><sub>-,-,-,0,-</sub> |  | 1.8<br><sub>-,-,-,2,-</sub> |  | 0.7<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.8 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 98% | 33.9<br><sub>31,36,27,36,26</sub> | 19.6<br><sub>12,14,13,28,14</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 8.8<br><sub>11,5,6,9,6</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>1,2,2,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,0,2,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.9 | 2.7 | 31.3 |
| Grayson Allen | 98% | 31.4<br><sub>21,30,19,27,22</sub> | 17.5<br><sub>5,27,11,22,0</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>3,4,1,2,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>2,3,0,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>1,7,3,5,0</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 2.1 | 25.1 |
| Sion James | 98% | 30.2<br><sub>29,18,21,31,21</sub> | 8.6<br><sub>6,4,11,10,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>5,2,4,2,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.3<br><sub>4,1,3,1,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 1.4 | 16.5 |
| Royce O'Neale | 98% | 27.9<br><sub>17,23,18,18,26</sub> | 8.8<br><sub>7,8,2,0,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,1,0,2,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 1.1 | 15.8 |
| Coby White | 98% | 27.7<br><sub>-,-,16,18,16</sub> | 19.6<br><sub>-,-,7,4,7</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>-,-,0,5,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.2<br><sub>-,-,3,2,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>-,-,1,0,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.2 | 2.8 | 27.4 |
| Tidjane Salaun | 93% | 26.5<br><sub>9,12,19,10,23</sub> | 10.4<br><sub>6,5,1,9,13</sub> |  | 6.0<br><sub>2,2,7,1,4</sub> |  | 1.4<br><sub>0,0,0,0,0</sub> |  | 1.6<br><sub>2,1,0,3,2</sub> |  | 0.7 | 0.3 | 1.2 | 17.8 |
| Christian Anderson | 80% | 25.7<br><sub>14,8,9,-,25</sub> | 10.7<br><sub>4,2,8,-,4</sub> |  | 3.4<br><sub>3,0,2,-,3</sub> |  | 3.6<br><sub>3,0,2,-,5</sub> |  | 1.4<br><sub>0,0,1,-,0</sub> |  | 0.9 | 0.4 | 1.9 | 17.7 |
| Hannes Steinbach | 52% | 24.0<br><sub>2,-,9,-,27</sub> | 6.6<br><sub>0,-,2,-,4</sub> |  | 6.2<br><sub>0,-,2,-,11</sub> |  | 1.1<br><sub>0,-,1,-,1</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.6 | 0.8 | 1.0 | 14.0 |
| Ryan Kalkbrenner | 98% | 23.9<br><sub>15,19,16,19,21</sub> | 7.0<br><sub>2,6,4,6,4</sub> |  | 6.4<br><sub>4,3,6,4,5</sub> |  | 1.5<br><sub>0,4,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.3 | 1.2 | 14.9 |
| Liam McNeeley | 58% | 21.5<br><sub>3,-,9,-,19</sub> | 9.3<br><sub>0,-,3,-,8</sub> |  | 4.0<br><sub>2,-,0,-,2</sub> |  | 1.6<br><sub>0,-,1,-,3</sub> |  | 1.2<br><sub>0,-,0,-,1</sub> |  | 0.4 | 0.2 | 1.1 | 14.9 |

</details>

<details><summary>if Jarrett Allen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid (CHA) | 98% | 34.0<br><sub>31,36,27,36,26</sub> | 19.8<br><sub>12,14,13,28,14</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 8.8<br><sub>11,5,6,9,6</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,2,2,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,0,2,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.9 | 2.8 | 31.5 |
| Grayson Allen (CHA) | 98% | 31.3<br><sub>21,30,19,27,22</sub> | 17.4<br><sub>5,27,11,22,0</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>3,4,1,2,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>2,3,0,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>1,7,3,5,0</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 2.1 | 25.0 |
| Sion James (CHA) | 98% | 30.1<br><sub>29,18,21,31,21</sub> | 8.5<br><sub>6,4,11,10,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>5,2,4,2,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.3<br><sub>4,1,3,1,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 1.4 | 16.5 |
| Royce O'Neale (CHA) | 98% | 27.9<br><sub>17,23,18,18,26</sub> | 8.9<br><sub>7,8,2,0,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,1,0,2,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 1.1 | 15.9 |
| Coby White (CHA) | 98% | 27.7<br><sub>-,-,16,18,16</sub> | 19.6<br><sub>-,-,7,4,7</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>-,-,0,5,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.2<br><sub>-,-,3,2,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>-,-,1,0,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.2 | 2.8 | 27.4 |
| Tidjane Salaun (CHA) | 93% | 26.5<br><sub>9,12,19,10,23</sub> | 10.4<br><sub>6,5,1,9,13</sub> |  | 6.0<br><sub>2,2,7,1,4</sub> |  | 1.5<br><sub>0,0,0,0,0</sub> |  | 1.6<br><sub>2,1,0,3,2</sub> |  | 0.7 | 0.3 | 1.2 | 17.9 |
| Christian Anderson (CHA) | 80% | 25.9<br><sub>14,8,9,-,25</sub> | 10.8<br><sub>4,2,8,-,4</sub> |  | 3.5<br><sub>3,0,2,-,3</sub> |  | 3.6<br><sub>3,0,2,-,5</sub> |  | 1.4<br><sub>0,0,1,-,0</sub> |  | 0.9 | 0.4 | 1.9 | 17.9 |
| Hannes Steinbach (CHA) | 52% | 23.9<br><sub>2,-,9,-,27</sub> | 6.6<br><sub>0,-,2,-,4</sub> |  | 6.3<br><sub>0,-,2,-,11</sub> |  | 1.2<br><sub>0,-,1,-,1</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.6 | 0.8 | 1.1 | 14.1 |
| Ryan Kalkbrenner (CHA) | 98% | 23.8<br><sub>15,19,16,19,21</sub> | 7.0<br><sub>2,6,4,6,4</sub> |  | 6.4<br><sub>4,3,6,4,5</sub> |  | 1.5<br><sub>0,4,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.3 | 1.2 | 14.9 |
| Liam McNeeley (CHA) | 58% | 21.5<br><sub>3,-,9,-,19</sub> | 9.3<br><sub>0,-,3,-,8</sub> |  | 4.0<br><sub>2,-,0,-,2</sub> |  | 1.6<br><sub>0,-,1,-,3</sub> |  | 1.2<br><sub>0,-,0,-,1</sub> |  | 0.4 | 0.2 | 1.1 | 14.9 |
| Donovan Mitchell (CLE) | 98% | 35.6<br><sub>24,36,33,33,37</sub> | 25.4<br><sub>15,17,27,23,37</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>4,5,3,7,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>3,11,6,8,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>2,4,5,1,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.3 | 2.9 | 35.4 |
| James Harden (CLE) | 98% | 35.2<br><sub>26,33,35,30,34</sub> | 17.5<br><sub>13,14,19,17,7</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,4,9,6,2</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>7,6,6,3,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,3,3,3,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 3.0 | 28.5 |
| Evan Mobley (CLE) | 98% | 33.8<br><sub>25,33,33,32,33</sub> | 15.8<br><sub>27,16,16,22,12</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 7.9<br><sub>5,7,10,6,9</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>3,4,3,4,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,1,1,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 1.4 | 1.7 | 27.2 |
| Peyton Watson (CLE) | 98% | 29.6<br><sub>22,-,-,28,29</sub> | 12.3<br><sub>5,-,-,13,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>2,-,-,9,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>6,-,-,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2<br><sub>1,-,-,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.1 | 1.6 | 19.2 |
| Jarrett Allen (CLE) | 100% | 26.1<br><sub>24,28,7,-,-</sub> | 11.6<br><sub>25,14,0,-,-</sub> | 12.5 · – | 6.8<br><sub>11,6,1,-,-</sub> | 7.5 | 1.4<br><sub>4,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.9 | 1.2 | 1.1 | 19.8 |
| Meleek Thomas (CLE) | 88% | 22.7<br><sub>23,26,18,27,24</sub> | 9.3<br><sub>13,17,9,12,9</sub> |  | 2.4<br><sub>1,5,1,1,4</sub> |  | 1.2<br><sub>2,1,0,3,0</sub> |  | 1.4<br><sub>3,3,3,2,3</sub> |  | 0.8 | 0.2 | 1.2 | 12.9 |
| Mario Hezonja (CLE) | 98% | 20.4<br><sub>20,27,23,27,19</sub> | 8.0<br><sub>8,12,12,15,0</sub> |  | 5.2<br><sub>11,8,8,10,5</sub> |  | 1.3<br><sub>4,3,1,1,1</sub> |  | 1.1<br><sub>1,3,2,2,0</sub> |  | 0.6 | 0.1 | 0.9 | 14.6 |
| Tyrese Proctor (CLE) | 91% | 20.3<br><sub>18,19,22,19,23</sub> | 7.1<br><sub>9,10,11,3,7</sub> |  | 2.8<br><sub>4,4,1,6,3</sub> |  | 2.4<br><sub>5,2,0,3,3</sub> |  | 1.0<br><sub>3,2,2,0,2</sub> |  | 0.8 | 0.1 | 0.9 | 12.3 |
| Thomas Bryant (CLE) | 71% | 13.2<br><sub>11,5,13,16,15</sub> | 6.1<br><sub>11,4,8,13,5</sub> |  | 3.1<br><sub>2,0,0,6,3</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>3,0,1,1,1</sub> |  | 0.3 | 0.4 | 0.6 | 9.8 |
| Craig Porter Jr. (CLE) | 88% | 12.6<br><sub>16,8,14,3,15</sub> | 2.8<br><sub>2,0,0,0,0</sub> |  | 2.1<br><sub>2,4,1,0,1</sub> |  | 1.9<br><sub>4,1,1,0,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 6.7 |
| Riley Minix (CLE) | 48% | 9.6<br><sub>6,-,-,-,10</sub> | 3.5<br><sub>0,-,-,-,8</sub> |  | 1.5<br><sub>3,-,-,-,3</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,2</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Ernest Udeh Jr. (CLE) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Norchad Omier (CLE) | 52% | 6.3<br><sub>-,-,-,3,-</sub> | 2.1<br><sub>-,-,-,0,-</sub> |  | 1.6<br><sub>-,-,-,2,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>if Moussa Diabate plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid (CHA) | 98% | 33.3<br><sub>31,36,27,36,26</sub> | 19.4<br><sub>12,14,13,28,14</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 8.7<br><sub>11,5,6,9,6</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>1,2,2,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,0,2,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.8 | 2.6 | 30.9 |
| Grayson Allen (CHA) | 98% | 30.3<br><sub>21,30,19,27,22</sub> | 16.7<br><sub>5,27,11,22,0</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>3,4,1,2,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>2,3,0,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>1,7,3,5,0</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 2.0 | 24.0 |
| Moussa Diabate (CHA) | 100% | 30.2<br><sub>31,28,24,29,-</sub> | 9.1<br><sub>10,10,7,7,-</sub> | 8.5 · – | 9.8<br><sub>12,8,9,6,-</sub> | 9.5 | 2.6<br><sub>1,3,2,2,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 1.1 | 0.8 | 1.7 | 21.5 |
| Sion James (CHA) | 98% | 28.7<br><sub>29,18,21,31,21</sub> | 8.1<br><sub>6,4,11,10,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>5,2,4,2,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.0<br><sub>4,1,3,1,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 1.2 | 15.3 |
| Royce O'Neale (CHA) | 98% | 27.5<br><sub>17,23,18,18,26</sub> | 8.5<br><sub>7,8,2,0,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>1,1,0,2,2</sub> |  | 1.7<br><sub>2,1,0,0,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.3 | 1.1 | 15.1 |
| Coby White (CHA) | 98% | 24.8<br><sub>-,-,16,18,16</sub> | 17.2<br><sub>-,-,7,4,7</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>-,-,0,5,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.8<br><sub>-,-,3,2,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>-,-,1,0,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.2 | 2.4 | 24.2 |
| Christian Anderson (CHA) | 80% | 22.8<br><sub>14,8,9,-,25</sub> | 9.5<br><sub>4,2,8,-,4</sub> |  | 3.1<br><sub>3,0,2,-,3</sub> |  | 3.5<br><sub>3,0,2,-,5</sub> |  | 1.2<br><sub>0,0,1,-,0</sub> |  | 0.7 | 0.4 | 1.8 | 16.1 |
| Ryan Kalkbrenner (CHA) | 98% | 22.3<br><sub>15,19,16,19,21</sub> | 6.7<br><sub>2,6,4,6,4</sub> |  | 5.8<br><sub>4,3,6,4,5</sub> |  | 1.4<br><sub>0,4,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.1 | 13.8 |
| Tidjane Salaun (CHA) | 93% | 22.0<br><sub>9,12,19,10,23</sub> | 8.4<br><sub>6,5,1,9,13</sub> |  | 5.1<br><sub>2,2,7,1,4</sub> |  | 1.1<br><sub>0,0,0,0,0</sub> |  | 1.2<br><sub>2,1,0,3,2</sub> |  | 0.6 | 0.2 | 1.0 | 14.5 |
| Hannes Steinbach (CHA) | 52% | 17.2<br><sub>2,-,9,-,27</sub> | 4.6<br><sub>0,-,2,-,4</sub> |  | 4.4<br><sub>0,-,2,-,11</sub> |  | 0.9<br><sub>0,-,1,-,1</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.7 | 0.7 | 9.9 |
| Liam McNeeley (CHA) | 58% | 17.0<br><sub>3,-,9,-,19</sub> | 7.2<br><sub>0,-,3,-,8</sub> |  | 3.2<br><sub>2,-,0,-,2</sub> |  | 1.3<br><sub>0,-,1,-,3</sub> |  | 0.8<br><sub>0,-,0,-,1</sub> |  | 0.3 | 0.1 | 0.9 | 11.7 |
| Donovan Mitchell (CLE) | 98% | 36.6<br><sub>24,36,33,33,37</sub> | 26.3<br><sub>15,17,27,23,37</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>4,5,3,7,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>3,11,6,8,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>2,4,5,1,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.3 | 2.9 | 36.6 |
| James Harden (CLE) | 98% | 36.5<br><sub>26,33,35,30,34</sub> | 18.2<br><sub>13,14,19,17,7</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>6,4,9,6,2</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.5<br><sub>7,6,6,3,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>3,3,3,3,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 3.3 | 29.5 |
| Evan Mobley (CLE) | 98% | 35.4<br><sub>25,33,33,32,33</sub> | 16.5<br><sub>27,16,16,22,12</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 8.2<br><sub>5,7,10,6,9</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,4,3,4,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>3,1,1,3,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 1.6 | 1.8 | 28.5 |
| Peyton Watson (CLE) | 98% | 31.6<br><sub>22,-,-,28,29</sub> | 13.8<br><sub>5,-,-,13,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>2,-,-,9,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>6,-,-,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>1,-,-,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.1 | 1.2 | 1.7 | 21.2 |
| Meleek Thomas (CLE) | 88% | 26.1<br><sub>23,26,18,27,24</sub> | 10.6<br><sub>13,17,9,12,9</sub> |  | 2.9<br><sub>1,5,1,1,4</sub> |  | 1.4<br><sub>2,1,0,3,0</sub> |  | 1.6<br><sub>3,3,3,2,3</sub> |  | 0.9 | 0.2 | 1.2 | 14.9 |
| Tyrese Proctor (CLE) | 91% | 23.4<br><sub>18,19,22,19,23</sub> | 8.2<br><sub>9,10,11,3,7</sub> |  | 3.3<br><sub>4,4,1,6,3</sub> |  | 2.7<br><sub>5,2,0,3,3</sub> |  | 1.3<br><sub>3,2,2,0,2</sub> |  | 1.0 | 0.1 | 1.0 | 14.2 |
| Mario Hezonja (CLE) | 98% | 22.8<br><sub>20,27,23,27,19</sub> | 9.0<br><sub>8,12,12,15,0</sub> |  | 5.8<br><sub>11,8,8,10,5</sub> |  | 1.5<br><sub>4,3,1,1,1</sub> |  | 1.3<br><sub>1,3,2,2,0</sub> |  | 0.7 | 0.2 | 1.0 | 16.3 |
| Thomas Bryant (CLE) | 71% | 15.9<br><sub>11,5,13,16,15</sub> | 7.0<br><sub>11,4,8,13,5</sub> |  | 3.7<br><sub>2,0,0,6,3</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>3,0,1,1,1</sub> |  | 0.4 | 0.5 | 0.6 | 11.4 |
| Craig Porter Jr. (CLE) | 88% | 14.8<br><sub>16,8,14,3,15</sub> | 3.3<br><sub>2,0,0,0,0</sub> |  | 2.4<br><sub>2,4,1,0,1</sub> |  | 2.0<br><sub>4,1,1,0,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.4 | 0.7 | 7.8 |
| Riley Minix (CLE) | 48% | 11.6<br><sub>6,-,-,-,10</sub> | 4.2<br><sub>0,-,-,-,8</sub> |  | 1.8<br><sub>3,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,2</sub> |  | 0.3 | 0.1 | 0.4 | 6.6 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Norchad Omier (CLE) | 52% | 7.7<br><sub>-,-,-,3,-</sub> | 2.2<br><sub>-,-,-,0,-</sub> |  | 1.8<br><sub>-,-,-,2,-</sub> |  | 0.7<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.8 |

</details>


### WAS @ DET
Out: Jalen Duren (DET), Isaiah Joe (DET), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.0–116.9 | WAS 29% | 3.50 / 1.40 | DET -7.5 | 225.5 | DET -10.5 covers 43%; o217.5 68% |
| Expected (weighted by chance each plays) | 109.2–116.8 | WAS 29% | 3.42 / 1.41 | DET -7.5 | 225.5 | DET -10.5 covers 42%; o217.5 67% |
| if Anthony Davis plays | 109.2–116.7 | WAS 30% | 3.36 / 1.42 | DET -7.5 | 225.5 | DET -10.5 covers 41%; o217.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Davis (WAS) | Questionable | 55% | 33.4 | 20.1 | 10.8 | 2.6 | 0.7 | 1.2 | 2.0 | 2.4 | 33.6 | full tables below |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.2<br><sub>38,34,34,37,28</sub> | 19.5<br><sub>21,15,18,23,4</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>7,3,2,2,5</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 8.9<br><sub>9,9,6,10,3</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.3 | 3.5 | 31.5 |
| Kyshawn George | 98% | 34.5<br><sub>32,37,35,39,30</sub> | 17.7<br><sub>12,22,25,33,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>3,4,4,4,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.8<br><sub>3,5,7,7,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>4,4,3,5,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 1.2 | 2.7 | 27.8 |
| AJ Dybantsa | 96% | 34.1<br><sub>30,33,32,36,31</sub> | 15.8<br><sub>17,21,9,11,19</sub> | 17.5 · –<br><sub>o 45% · u 55%</sub> | 6.2<br><sub>8,5,6,9,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>1,2,3,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,1,0,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.4 | 2.2 | 24.6 |
| Alex Sarr | 98% | 27.3<br><sub>29,-,23,30,28</sub> | 12.5<br><sub>3,-,11,13,15</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>8,-,9,8,14</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>0,-,1,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>1,-,0,1,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.9 | 1.9 | 1.7 | 22.2 |
| Bilal Coulibaly | 98% | 26.2<br><sub>22,33,23,24,20</sub> | 9.4<br><sub>1,7,6,9,0</sub> |  | 3.9<br><sub>5,1,2,5,5</sub> |  | 1.8<br><sub>1,2,2,0,0</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 1.1 | 1.0 | 1.2 | 15.1 |
| Tre Johnson | 88% | 23.2<br><sub>13,22,14,27,28</sub> | 9.7<br><sub>4,4,3,23,4</sub> |  | 2.5<br><sub>2,3,2,1,0</sub> |  | 1.2<br><sub>0,0,0,1,3</sub> |  | 1.4<br><sub>0,0,1,5,0</sub> |  | 0.8 | 0.2 | 1.2 | 13.4 |
| Bub Carrington | 98% | 21.2<br><sub>20,19,19,15,21</sub> | 7.4<br><sub>9,3,0,5,9</sub> |  | 2.4<br><sub>4,4,1,1,6</sub> |  | 2.6<br><sub>2,4,2,1,1</sub> |  | 1.1<br><sub>3,1,0,1,3</sub> |  | 0.6 | 0.2 | 1.4 | 12.3 |
| Deandre Ayton | 98% | 17.1<br><sub>17,24,11,23,7</sub> | 6.0<br><sub>3,4,5,8,2</sub> |  | 5.1<br><sub>3,6,4,11,1</sub> |  | 0.7<br><sub>1,2,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.9 | 11.8 |
| Will Riley | 88% | 14.5<br><sub>1,4,13,9,20</sub> | 5.7<br><sub>0,0,0,7,5</sub> |  | 1.8<br><sub>0,0,0,0,2</sub> |  | 1.1<br><sub>0,1,0,0,1</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.8 | 8.5 |
| Khris Middleton | 48% | 14.3<br><sub>5,-,-,-,-</sub> | 4.8<br><sub>0,-,-,-,-</sub> |  | 2.3<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.1 | 8.2 |
| Anthony Gill | 48% | 12.1<br><sub>-,-,-,-,9</sub> | 4.0<br><sub>-,-,-,-,1</sub> |  | 2.1<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 6.8 |
| Tre Mann | 52% | 11.0<br><sub>1,-,3,-,18</sub> | 4.2<br><sub>0,-,2,-,2</sub> |  | 1.3<br><sub>0,-,0,-,0</sub> |  | 1.2<br><sub>0,-,0,-,2</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.6 | 0.1 | 0.6 | 6.7 |
| Felix Okpara | 52% | 7.6<br><sub>-,-,3,-,-</sub> | 3.0<br><sub>-,-,0,-,-</sub> |  | 1.7<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 5.1 |

</details>

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 33.2<br><sub>39,28,27,40,38</sub> | 25.5<br><sub>30,20,33,26,14</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,5,5,7,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 8.6<br><sub>7,4,7,11,8</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>4,1,4,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.8 | 3.7 | 39.5 |
| Duncan Robinson | 98% | 29.4<br><sub>32,26,32,37,27</sub> | 15.7<br><sub>13,17,24,27,12</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,4,2,1,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,2,3,2,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 3.0<br><sub>3,2,6,7,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 1.1 | 21.2 |
| Ausar Thompson | 98% | 27.1<br><sub>29,26,26,34,24</sub> | 10.2<br><sub>7,11,14,11,7</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>9,8,6,17,11</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>8,6,4,3,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.9 | 1.0 | 1.6 | 22.0 |
| John Collins | 98% | 27.1<br><sub>18,26,19,26,32</sub> | 12.2<br><sub>4,4,4,16,8</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>2,9,3,1,4</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.1<br><sub>0,0,1,0,1</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 1.0 | 0.8 | 1.3 | 19.5 |
| Daniss Jenkins | 98% | 26.7<br><sub>24,24,23,21,32</sub> | 12.6<br><sub>14,6,2,5,31</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,3,1,1,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 5.2<br><sub>3,5,7,4,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>2,2,0,1,8</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.5 | 21.2 |
| Kevin Huerter | 97% | 25.3<br><sub>19,24,20,20,35</sub> | 10.6<br><sub>3,8,9,8,24</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>2,1,2,1,5</sub> |  | 3.1<br><sub>3,3,3,0,5</sub> |  | 1.6<br><sub>1,2,3,2,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 1.0 | 17.3 |
| Paul Reed | 97% | 25.1<br><sub>38,31,28,30,20</sub> | 13.7<br><sub>16,12,11,8,8</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 8.0<br><sub>4,4,5,7,10</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>0,1,4,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.4<br><sub>2,0,0,0,0</sub> |  | 1.3 | 1.3 | 1.6 | 23.9 |
| Javonte Green | 97% | 19.5<br><sub>21,22,20,15,17</sub> | 7.0<br><sub>7,6,5,1,7</sub> |  | 3.1<br><sub>2,3,2,3,2</sub> |  | 0.9<br><sub>2,1,0,1,2</sub> |  | 1.0<br><sub>1,1,1,0,1</sub> |  | 1.2 | 0.4 | 0.4 | 11.1 |
| Ronald Holland II | 98% | 17.4<br><sub>12,22,20,12,14</sub> | 7.4<br><sub>0,18,11,3,5</sub> |  | 3.7<br><sub>2,3,2,2,2</sub> |  | 1.3<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>0,2,3,1,1</sub> |  | 1.0 | 0.6 | 1.0 | 12.3 |
| Taurean Prince | 38% | 9.7<br><sub>6,-,-,-,-</sub> | 3.5<br><sub>1,-,-,-,-</sub> |  | 1.5<br><sub>2,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.7 |
| Ugonna Onyenso | 8% | 8.6 | 3.5 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Elijah Harkless | 36% | 7.1<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| Tolu Smith | 67% | 6.8<br><sub>1,3,8,5,-</sub> | 2.7<br><sub>2,2,0,1,-</sub> |  | 2.4<br><sub>1,1,2,1,-</sub> |  | 0.4<br><sub>0,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.5 |
| Chaz Lanier | 48% | 6.5<br><sub>-,3,7,-,-</sub> | 2.6<br><sub>-,6,5,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,2,1,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Isaac Jones | 48% | 6.2<br><sub>-,3,6,-,-</sub> | 3.3<br><sub>-,0,2,-,-</sub> |  | 1.7<br><sub>-,0,5,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.5 | 0.3 | 5.3 |
| Ebuka Okorie | 52% | 5.9<br><sub>-,3,6,-,-</sub> | 2.1<br><sub>-,0,4,-,-</sub> |  | 0.9<br><sub>-,0,2,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |

</details>

<details><summary>if Anthony Davis plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | 98% | 33.2<br><sub>39,28,27,40,38</sub> | 25.5<br><sub>30,20,33,26,14</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,5,5,7,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 8.7<br><sub>7,4,7,11,8</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>4,1,4,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.8 | 3.7 | 39.5 |
| Duncan Robinson (DET) | 98% | 29.4<br><sub>32,26,32,37,27</sub> | 15.5<br><sub>13,17,24,27,12</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,4,2,1,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,2,3,2,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 3.0<br><sub>3,2,6,7,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 1.1 | 21.1 |
| John Collins (DET) | 98% | 27.2<br><sub>18,26,19,26,32</sub> | 12.3<br><sub>4,4,4,16,8</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>2,9,3,1,4</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.1<br><sub>0,0,1,0,1</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.9 | 0.8 | 1.3 | 19.6 |
| Ausar Thompson (DET) | 98% | 27.1<br><sub>29,26,26,34,24</sub> | 10.1<br><sub>7,11,14,11,7</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>9,8,6,17,11</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>8,6,4,3,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.9 | 1.0 | 1.6 | 21.9 |
| Daniss Jenkins (DET) | 98% | 26.6<br><sub>24,24,23,21,32</sub> | 12.5<br><sub>14,6,2,5,31</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,3,1,1,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 5.2<br><sub>3,5,7,4,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>2,2,0,1,8</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.5 | 21.2 |
| Kevin Huerter (DET) | 97% | 25.4<br><sub>19,24,20,20,35</sub> | 10.7<br><sub>3,8,9,8,24</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>2,1,2,1,5</sub> |  | 3.1<br><sub>3,3,3,0,5</sub> |  | 1.6<br><sub>1,2,3,2,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 1.0 | 17.3 |
| Paul Reed (DET) | 97% | 25.1<br><sub>38,31,28,30,20</sub> | 13.7<br><sub>16,12,11,8,8</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 8.0<br><sub>4,4,5,7,10</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>0,1,4,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.4<br><sub>2,0,0,0,0</sub> |  | 1.3 | 1.3 | 1.6 | 23.9 |
| Javonte Green (DET) | 97% | 19.5<br><sub>21,22,20,15,17</sub> | 7.0<br><sub>7,6,5,1,7</sub> |  | 3.1<br><sub>2,3,2,3,2</sub> |  | 0.9<br><sub>2,1,0,1,2</sub> |  | 1.0<br><sub>1,1,1,0,1</sub> |  | 1.2 | 0.4 | 0.4 | 11.1 |
| Ronald Holland II (DET) | 98% | 17.3<br><sub>12,22,20,12,14</sub> | 7.3<br><sub>0,18,11,3,5</sub> |  | 3.7<br><sub>2,3,2,2,2</sub> |  | 1.3<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>0,2,3,1,1</sub> |  | 1.0 | 0.6 | 1.0 | 12.2 |
| Taurean Prince (DET) | 38% | 9.7<br><sub>6,-,-,-,-</sub> | 3.5<br><sub>1,-,-,-,-</sub> |  | 1.5<br><sub>2,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| Ugonna Onyenso (DET) | 8% | 8.5 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.7 |
| Elijah Harkless (DET) | 36% | 7.0<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| Tolu Smith (DET) | 67% | 6.8<br><sub>1,3,8,5,-</sub> | 2.7<br><sub>2,2,0,1,-</sub> |  | 2.4<br><sub>1,1,2,1,-</sub> |  | 0.4<br><sub>0,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.5 |
| Chaz Lanier (DET) | 48% | 6.5<br><sub>-,3,7,-,-</sub> | 2.6<br><sub>-,6,5,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,2,1,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Isaac Jones (DET) | 48% | 6.3<br><sub>-,3,6,-,-</sub> | 3.4<br><sub>-,0,2,-,-</sub> |  | 1.7<br><sub>-,0,5,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.5 | 0.3 | 5.5 |
| Ebuka Okorie (DET) | 52% | 5.9<br><sub>-,3,6,-,-</sub> | 2.1<br><sub>-,0,4,-,-</sub> |  | 0.9<br><sub>-,0,2,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |
| Trae Young (WAS) | 98% | 34.2<br><sub>38,34,34,37,28</sub> | 17.5<br><sub>21,15,18,23,4</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>7,3,2,2,5</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>9,9,6,10,3</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 3.2 | 29.1 |
| Anthony Davis (WAS) | 100% | 33.4<br><sub>34,34,30,-,-</sub> | 20.1<br><sub>25,27,26,-,-</sub> | 20.5 · – | 10.8<br><sub>13,9,10,-,-</sub> | 9.5 | 2.6<br><sub>1,1,3,-,-</sub> | 2.5 | 0.7<br><sub>0,1,0,-,-</sub> |  | 1.2 | 2.0 | 2.4 | 33.6 |
| Kyshawn George (WAS) | 98% | 32.4<br><sub>32,37,35,39,30</sub> | 15.5<br><sub>12,22,25,33,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>3,4,4,4,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.3<br><sub>3,5,7,7,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>4,4,3,5,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 1.2 | 2.5 | 24.7 |
| AJ Dybantsa (WAS) | 96% | 31.7<br><sub>30,33,32,36,31</sub> | 14.4<br><sub>17,21,9,11,19</sub> | 17.5 · –<br><sub>o 45% · u 55%</sub> | 5.6<br><sub>8,5,6,9,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,2,3,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9<br><sub>1,1,0,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.3 | 2.1 | 22.3 |
| Alex Sarr (WAS) | 98% | 25.3<br><sub>29,-,23,30,28</sub> | 11.2<br><sub>3,-,11,13,15</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>8,-,9,8,14</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,-,1,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0<br><sub>1,-,0,1,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 1.8 | 1.5 | 19.8 |
| Bilal Coulibaly (WAS) | 98% | 22.4<br><sub>22,33,23,24,20</sub> | 7.3<br><sub>1,7,6,9,0</sub> |  | 3.2<br><sub>5,1,2,5,5</sub> |  | 1.4<br><sub>1,2,2,0,0</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 1.0 | 0.8 | 1.1 | 12.0 |
| Tre Johnson (WAS) | 88% | 19.3<br><sub>13,22,14,27,28</sub> | 7.7<br><sub>4,4,3,23,4</sub> |  | 2.1<br><sub>2,3,2,1,0</sub> |  | 0.9<br><sub>0,0,0,1,3</sub> |  | 1.1<br><sub>0,0,1,5,0</sub> |  | 0.7 | 0.2 | 1.0 | 10.8 |
| Bub Carrington (WAS) | 98% | 17.7<br><sub>20,19,19,15,21</sub> | 5.5<br><sub>9,3,0,5,9</sub> |  | 1.9<br><sub>4,4,1,1,6</sub> |  | 2.1<br><sub>2,4,2,1,1</sub> |  | 0.8<br><sub>3,1,0,1,3</sub> |  | 0.5 | 0.2 | 1.2 | 9.6 |
| Deandre Ayton (WAS) | 98% | 13.6<br><sub>17,24,11,23,7</sub> | 4.6<br><sub>3,4,5,8,2</sub> |  | 4.0<br><sub>3,6,4,11,1</sub> |  | 0.6<br><sub>1,2,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 9.2 |
| Will Riley (WAS) | 88% | 12.3<br><sub>1,4,13,9,20</sub> | 4.8<br><sub>0,0,0,7,5</sub> |  | 1.4<br><sub>0,0,0,0,2</sub> |  | 0.9<br><sub>0,1,0,0,1</sub> |  | 0.4<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 7.2 |
| Khris Middleton (WAS) | 48% | 8.9<br><sub>5,-,-,-,-</sub> | 2.8<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>0,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.7 | 4.8 |
| Anthony Gill (WAS) | 48% | 8.5<br><sub>-,-,-,-,9</sub> | 2.8<br><sub>-,-,-,-,1</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.7 |
| Tre Mann (WAS) | 52% | 7.7<br><sub>1,-,3,-,18</sub> | 3.2<br><sub>0,-,2,-,2</sub> |  | 0.9<br><sub>0,-,0,-,0</sub> |  | 0.9<br><sub>0,-,0,-,2</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.1 |
| Felix Okpara (WAS) | 52% | 5.9<br><sub>-,-,3,-,-</sub> | 2.3<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.1 |

</details>


### MEM @ TOR
Out: Kawhi Leonard (TOR), Malachi Smith (TOR), Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.3–117.4 | MEM 44% | 2.26 / 1.79 | TOR -2.5 | 232.5 | TOR -3.5 covers 47%; o229.5 56% |
| Expected (weighted by chance each plays) | 114.5–118.9 | MEM 38% | 2.63 / 1.61 | TOR -4.5 | 233.5 | TOR -3.5 covers 53%; o229.5 58% |
| if Immanuel Quickley plays | 114.5–118.5 | MEM 39% | 2.57 / 1.64 | TOR -4.5 | 232.5 | TOR -3.5 covers 52%; o229.5 57% |
| if Scottie Barnes plays | 113.9–118.8 | MEM 37% | 2.71 / 1.58 | TOR -4.5 | 232.5 | TOR -3.5 covers 54%; o229.5 56% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Immanuel Quickley (TOR) | Questionable | 55% | 32.7 | 20.3 | 4.2 | 7.0 | 2.8 | 1.6 | 0.1 | 1.9 | 31.4 | full tables below |
| Scottie Barnes (TOR) | Questionable | 55% | 34.8 | 24.4 | 7.6 | 7.4 | 0.8 | 1.8 | 1.4 | 3.7 | 39.4 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 31.4<br><sub>28,26,38,33,31</sub> | 14.8<br><sub>18,27,18,10,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.6 | 2.8 | 28.0 |
| Ty Jerome | 98% | 29.0<br><sub>24,-,37,29,28</sub> | 21.3<br><sub>10,-,40,23,21</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,-,5,4,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.0<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.2 | 2.7 | 29.6 |
| Cedric Coward | 98% | 27.0<br><sub>27,23,31,33,23</sub> | 13.4<br><sub>17,10,10,23,10</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 1.9 | 21.8 |
| Jaylen Wells | 98% | 25.4<br><sub>25,22,34,21,25</sub> | 10.2<br><sub>10,4,16,0,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,0,3,3,0</sub> |  | 1.4<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.1 | 1.1 | 14.2 |
| Jerami Grant | 98% | 22.7<br><sub>27,23,24,24,22</sub> | 10.6<br><sub>2,14,11,11,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,1,2,2,2</sub> |  | 1.2<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.5 | 1.5 | 14.4 |
| Zach Edey | 98% | 20.9<br><sub>19,18,19,25,20</sub> | 9.1<br><sub>13,4,6,11,14</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.3 | 1.4 | 17.5 |
| Javon Small | 91% | 18.9<br><sub>-,20,-,-,21</sub> | 8.5<br><sub>-,7,-,-,10</sub> |  | 2.7<br><sub>-,1,-,-,4</sub> |  | 2.7<br><sub>-,5,-,-,2</sub> |  | 1.0<br><sub>-,2,-,-,1</sub> |  | 0.8 | 0.2 | 1.6 | 13.9 |
| Cam Spencer | 98% | 18.5<br><sub>23,25,19,24,19</sub> | 7.1<br><sub>8,10,13,7,7</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>8,13,7,9,0</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.1 | 13.2 |
| Kris Murray | 80% | 11.9<br><sub>3,21,19,15,13</sub> | 3.0<br><sub>0,2,0,5,2</sub> |  | 1.7<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.6 | 5.5 |
| GG Jackson | 72% | 11.9<br><sub>21,21,16,7,-</sub> | 6.3<br><sub>12,21,6,1,-</sub> |  | 2.2<br><sub>7,3,0,2,-</sub> |  | 0.7<br><sub>2,2,1,0,-</sub> |  | 0.6<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.0 | 9.2 |
| Quinten Post | 91% | 11.4<br><sub>7,-,-,11,15</sub> | 4.4<br><sub>10,-,-,2,0</sub> |  | 2.1<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 6.9 |
| Olivier-Maxence Prosper | 63% | 9.8<br><sub>3,4,-,7,11</sub> | 4.9<br><sub>4,2,-,4,2</sub> |  | 1.9<br><sub>1,1,-,3,3</sub> |  | 0.5<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.3 |
| Jahmai Mashack | 52% | 7.6<br><sub>-,4,-,-,4</sub> | 2.5<br><sub>-,2,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,1,-,-,2</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.1 | 0.7 | 4.3 |
| Taylor Hendricks | 58% | 7.5<br><sub>3,4,-,-,4</sub> | 3.2<br><sub>0,6,-,-,4</sub> |  | 1.5<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.3<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.9 |
| Carson Cooper | 48% | 5.5<br><sub>-,3,-,-,-</sub> | 2.1<br><sub>-,1,-,-,-</sub> |  | 2.1<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 1.1 | 5.2 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 36.4<br><sub>34,32,37,33,37</sub> | 27.9<br><sub>9,22,26,22,27</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>3,10,6,5,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 6.0<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>1,4,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.6 | 3.3 | 41.1 |
| Ja'Kobe Walter | 98% | 33.8<br><sub>32,33,35,27,29</sub> | 15.3<br><sub>9,11,10,8,7</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>3,4,6,1,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.9<br><sub>1,2,5,2,2</sub> |  | 2.5<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.8 | 0.4 | 1.4 | 22.8 |
| Collin Murray-Boyles | 98% | 32.1<br><sub>23,20,28,23,34</sub> | 16.6<br><sub>15,4,18,13,19</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>5,3,7,3,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>1,1,0,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.5<br><sub>1,0,1,1,0</sub> |  | 1.5 | 1.3 | 2.4 | 27.6 |
| Jamal Shead | 98% | 31.8<br><sub>23,25,20,20,34</sub> | 11.2<br><sub>2,9,6,3,10</sub> |  | 2.9<br><sub>1,2,1,3,3</sub> |  | 8.7<br><sub>8,6,6,6,16</sub> |  | 1.4<br><sub>0,2,0,1,1</sub> |  | 1.6 | 0.3 | 2.7 | 22.8 |
| Jamison Battle | 98% | 26.9<br><sub>19,17,21,19,21</sub> | 12.4<br><sub>2,20,12,9,6</sub> |  | 3.9<br><sub>0,5,0,1,2</sub> |  | 1.5<br><sub>0,0,0,0,0</sub> |  | 2.0<br><sub>0,4,4,2,1</sub> |  | 0.6 | 0.3 | 1.0 | 17.8 |
| Jakob Poeltl | 86% | 26.9<br><sub>23,-,-,19,31</sub> | 12.4<br><sub>12,-,-,8,19</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 8.3<br><sub>11,-,-,5,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,-,-,1,1</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.1 | 1.3 | 1.9 | 23.1 |
| Alijah Martin | 88% | 23.3<br><sub>-,16,6,9,31</sub> | 10.7<br><sub>-,5,2,6,27</sub> |  | 3.5<br><sub>-,2,2,1,4</sub> |  | 2.4<br><sub>-,4,0,0,1</sub> |  | 1.2<br><sub>-,1,0,0,6</sub> |  | 1.0 | 0.5 | 1.7 | 16.5 |
| Allen Graves | 98% | 20.5<br><sub>9,10,7,14,16</sub> | 7.2<br><sub>7,3,0,5,3</sub> |  | 3.6<br><sub>4,0,0,1,2</sub> |  | 1.2<br><sub>0,0,2,1,0</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.7 | 0.7 | 12.0 |
| Kyle Anderson | 63% | 14.6<br><sub>-,4,8,4,-</sub> | 4.6<br><sub>-,2,2,2,-</sub> |  | 2.8<br><sub>-,3,0,0,-</sub> |  | 2.6<br><sub>-,3,0,1,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.8 | 0.5 | 0.9 | 10.0 |
| Trayce Jackson-Davis | 72% | 13.6<br><sub>1,9,2,4,-</sub> | 5.5<br><sub>0,5,0,1,-</sub> |  | 4.7<br><sub>0,5,0,0,-</sub> |  | 1.0<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.7 | 0.8 | 0.7 | 11.1 |
| Jaden Bradley | 71% | 12.1<br><sub>-,4,-,4,8</sub> | 4.9<br><sub>-,3,-,2,3</sub> |  | 2.0<br><sub>-,1,-,1,0</sub> |  | 1.6<br><sub>-,2,-,0,1</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.9 | 0.3 | 0.8 | 8.4 |

</details>

<details><summary>if Immanuel Quickley plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 31.5<br><sub>28,26,38,33,31</sub> | 14.7<br><sub>18,27,18,10,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.6 | 2.8 | 27.9 |
| Ty Jerome (MEM) | 98% | 29.0<br><sub>24,-,37,29,28</sub> | 21.3<br><sub>10,-,40,23,21</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,-,5,4,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.0<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.2 | 2.7 | 29.7 |
| Cedric Coward (MEM) | 98% | 27.0<br><sub>27,23,31,33,23</sub> | 13.3<br><sub>17,10,10,23,10</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 1.9 | 21.7 |
| Jaylen Wells (MEM) | 98% | 25.4<br><sub>25,22,34,21,25</sub> | 10.2<br><sub>10,4,16,0,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,0,3,3,0</sub> |  | 1.4<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.1 | 1.1 | 14.1 |
| Jerami Grant (MEM) | 98% | 22.7<br><sub>27,23,24,24,22</sub> | 10.6<br><sub>2,14,11,11,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,1,2,2,2</sub> |  | 1.2<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.5 | 1.5 | 14.4 |
| Zach Edey (MEM) | 98% | 20.8<br><sub>19,18,19,25,20</sub> | 9.0<br><sub>13,4,6,11,14</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.3 | 1.4 | 17.3 |
| Javon Small (MEM) | 91% | 19.0<br><sub>-,20,-,-,21</sub> | 8.5<br><sub>-,7,-,-,10</sub> |  | 2.7<br><sub>-,1,-,-,4</sub> |  | 2.6<br><sub>-,5,-,-,2</sub> |  | 1.0<br><sub>-,2,-,-,1</sub> |  | 0.8 | 0.2 | 1.6 | 13.9 |
| Cam Spencer (MEM) | 98% | 18.5<br><sub>23,25,19,24,19</sub> | 7.1<br><sub>8,10,13,7,7</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>8,13,7,9,0</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.1 | 13.1 |
| Kris Murray (MEM) | 80% | 12.0<br><sub>3,21,19,15,13</sub> | 3.0<br><sub>0,2,0,5,2</sub> |  | 1.7<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.6 | 5.5 |
| GG Jackson (MEM) | 72% | 11.9<br><sub>21,21,16,7,-</sub> | 6.3<br><sub>12,21,6,1,-</sub> |  | 2.2<br><sub>7,3,0,2,-</sub> |  | 0.7<br><sub>2,2,1,0,-</sub> |  | 0.6<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.0 | 9.2 |
| Quinten Post (MEM) | 91% | 11.4<br><sub>7,-,-,11,15</sub> | 4.3<br><sub>10,-,-,2,0</sub> |  | 2.0<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 6.8 |
| Olivier-Maxence Prosper (MEM) | 63% | 9.6<br><sub>3,4,-,7,11</sub> | 4.8<br><sub>4,2,-,4,2</sub> |  | 1.9<br><sub>1,1,-,3,3</sub> |  | 0.5<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.2 |
| Jahmai Mashack (MEM) | 52% | 7.5<br><sub>-,4,-,-,4</sub> | 2.5<br><sub>-,2,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,1,-,-,2</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.3 |
| Taylor Hendricks (MEM) | 58% | 7.4<br><sub>3,4,-,-,4</sub> | 3.1<br><sub>0,6,-,-,4</sub> |  | 1.4<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.3<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.9 |
| Carson Cooper (MEM) | 48% | 5.4<br><sub>-,3,-,-,-</sub> | 2.1<br><sub>-,1,-,-,-</sub> |  | 2.1<br><sub>-,2,-,-,-</sub> |  | 0.9<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 1.0 | 5.1 |
| RJ Barrett (TOR) | 98% | 35.2<br><sub>34,32,37,33,37</sub> | 25.7<br><sub>9,22,26,22,27</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>3,10,6,5,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 5.0<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,4,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.6 | 2.9 | 37.6 |
| Immanuel Quickley (TOR) | 100% | 32.7<br><sub>37,33,38,32,-</sub> | 20.3<br><sub>17,12,27,13,-</sub> | 18.5 · – | 4.2<br><sub>6,6,4,1,-</sub> | 3.5 | 7.0<br><sub>8,7,2,7,-</sub> | 5.5 | 2.8<br><sub>4,3,1,2,-</sub> | 2.5 | 1.6 | 0.1 | 1.9 | 31.4 |
| Ja'Kobe Walter (TOR) | 98% | 30.7<br><sub>32,33,35,27,29</sub> | 13.2<br><sub>9,11,10,8,7</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>3,4,6,1,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,2,5,2,2</sub> |  | 2.1<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.7 | 0.4 | 1.1 | 19.9 |
| Collin Murray-Boyles (TOR) | 98% | 30.0<br><sub>23,20,28,23,34</sub> | 14.7<br><sub>15,4,18,13,19</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>5,3,7,3,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>1,1,0,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.4<br><sub>1,0,1,1,0</sub> |  | 1.4 | 1.3 | 2.0 | 24.6 |
| Jamal Shead (TOR) | 98% | 27.8<br><sub>23,25,20,20,34</sub> | 8.8<br><sub>2,9,6,3,10</sub> |  | 2.5<br><sub>1,2,1,3,3</sub> |  | 7.4<br><sub>8,6,6,6,16</sub> |  | 1.1<br><sub>0,2,0,1,1</sub> |  | 1.4 | 0.2 | 2.1 | 18.8 |
| Jakob Poeltl (TOR) | 86% | 25.2<br><sub>23,-,-,19,31</sub> | 11.1<br><sub>12,-,-,8,19</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>11,-,-,5,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>3,-,-,1,1</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.0 | 1.2 | 1.5 | 21.0 |
| Jamison Battle (TOR) | 98% | 22.1<br><sub>19,17,21,19,21</sub> | 9.9<br><sub>2,20,12,9,6</sub> |  | 3.1<br><sub>0,5,0,1,2</sub> |  | 1.0<br><sub>0,0,0,0,0</sub> |  | 1.6<br><sub>0,4,4,2,1</sub> |  | 0.5 | 0.2 | 0.7 | 14.1 |
| Alijah Martin (TOR) | 88% | 17.5<br><sub>-,16,6,9,31</sub> | 8.0<br><sub>-,5,2,6,27</sub> |  | 2.6<br><sub>-,2,2,1,4</sub> |  | 1.6<br><sub>-,4,0,0,1</sub> |  | 0.9<br><sub>-,1,0,0,6</sub> |  | 0.8 | 0.4 | 1.3 | 12.3 |
| Allen Graves (TOR) | 98% | 16.2<br><sub>9,10,7,14,16</sub> | 5.6<br><sub>7,3,0,5,3</sub> |  | 3.0<br><sub>4,0,0,1,2</sub> |  | 0.9<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.6 | 0.6 | 9.5 |
| Kyle Anderson (TOR) | 63% | 11.2<br><sub>-,4,8,4,-</sub> | 3.3<br><sub>-,2,2,2,-</sub> |  | 2.2<br><sub>-,3,0,0,-</sub> |  | 1.9<br><sub>-,3,0,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.4 | 0.7 | 7.4 |
| Trayce Jackson-Davis (TOR) | 72% | 9.1<br><sub>1,9,2,4,-</sub> | 3.6<br><sub>0,5,0,1,-</sub> |  | 3.2<br><sub>0,5,0,0,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.6 | 0.5 | 7.5 |
| Jaden Bradley (TOR) | 71% | 8.2<br><sub>-,4,-,4,8</sub> | 3.1<br><sub>-,3,-,2,3</sub> |  | 1.4<br><sub>-,1,-,1,0</sub> |  | 1.1<br><sub>-,2,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 5.6 |

</details>

<details><summary>if Scottie Barnes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 31.5<br><sub>28,26,38,33,31</sub> | 14.8<br><sub>18,27,18,10,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.6 | 2.8 | 28.0 |
| Ty Jerome (MEM) | 98% | 28.9<br><sub>24,-,37,29,28</sub> | 21.1<br><sub>10,-,40,23,21</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,-,5,4,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.0<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.2 | 2.7 | 29.4 |
| Cedric Coward (MEM) | 98% | 27.1<br><sub>27,23,31,33,23</sub> | 13.4<br><sub>17,10,10,23,10</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 1.9 | 21.9 |
| Jaylen Wells (MEM) | 98% | 25.4<br><sub>25,22,34,21,25</sub> | 10.1<br><sub>10,4,16,0,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,0,3,3,0</sub> |  | 1.4<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.1 | 1.1 | 14.1 |
| Jerami Grant (MEM) | 98% | 22.6<br><sub>27,23,24,24,22</sub> | 10.5<br><sub>2,14,11,11,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,1,2,2,2</sub> |  | 1.3<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.5 | 1.5 | 14.3 |
| Zach Edey (MEM) | 98% | 20.9<br><sub>19,18,19,25,20</sub> | 9.0<br><sub>13,4,6,11,14</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.3 | 1.4 | 17.4 |
| Javon Small (MEM) | 91% | 18.9<br><sub>-,20,-,-,21</sub> | 8.5<br><sub>-,7,-,-,10</sub> |  | 2.7<br><sub>-,1,-,-,4</sub> |  | 2.6<br><sub>-,5,-,-,2</sub> |  | 1.0<br><sub>-,2,-,-,1</sub> |  | 0.8 | 0.2 | 1.6 | 13.9 |
| Cam Spencer (MEM) | 98% | 18.6<br><sub>23,25,19,24,19</sub> | 7.1<br><sub>8,10,13,7,7</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>8,13,7,9,0</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.2 | 13.1 |
| GG Jackson (MEM) | 72% | 11.9<br><sub>21,21,16,7,-</sub> | 6.2<br><sub>12,21,6,1,-</sub> |  | 2.2<br><sub>7,3,0,2,-</sub> |  | 0.7<br><sub>2,2,1,0,-</sub> |  | 0.6<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.0 | 9.2 |
| Kris Murray (MEM) | 80% | 11.9<br><sub>3,21,19,15,13</sub> | 3.1<br><sub>0,2,0,5,2</sub> |  | 1.7<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.6 | 5.5 |
| Quinten Post (MEM) | 91% | 11.4<br><sub>7,-,-,11,15</sub> | 4.3<br><sub>10,-,-,2,0</sub> |  | 2.0<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 6.8 |
| Olivier-Maxence Prosper (MEM) | 63% | 9.7<br><sub>3,4,-,7,11</sub> | 4.9<br><sub>4,2,-,4,2</sub> |  | 1.8<br><sub>1,1,-,3,3</sub> |  | 0.5<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.2 |
| Taylor Hendricks (MEM) | 58% | 7.5<br><sub>3,4,-,-,4</sub> | 3.1<br><sub>0,6,-,-,4</sub> |  | 1.4<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.3<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.9 |
| Jahmai Mashack (MEM) | 52% | 7.5<br><sub>-,4,-,-,4</sub> | 2.5<br><sub>-,2,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,1,-,-,2</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 4.3 |
| Carson Cooper (MEM) | 48% | 5.4<br><sub>-,3,-,-,-</sub> | 2.1<br><sub>-,1,-,-,-</sub> |  | 2.1<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 1.1 | 5.2 |
| RJ Barrett (TOR) | 98% | 35.2<br><sub>34,32,37,33,37</sub> | 24.5<br><sub>9,22,26,22,27</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>3,10,6,5,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.6<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,4,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.5 | 2.8 | 35.7 |
| Scottie Barnes (TOR) | 100% | 34.8<br><sub>39,36,38,32,-</sub> | 24.4<br><sub>41,29,22,17,-</sub> | 23.5 · – | 7.6<br><sub>5,6,15,6,-</sub> | 7.5 | 7.4<br><sub>5,5,8,6,-</sub> | 5.5 | 0.8<br><sub>1,0,0,1,-</sub> |  | 1.8 | 1.4 | 3.7 | 39.4 |
| Ja'Kobe Walter (TOR) | 98% | 31.2<br><sub>32,33,35,27,29</sub> | 12.7<br><sub>9,11,10,8,7</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,4,6,1,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>1,2,5,2,2</sub> |  | 2.1<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.7 | 0.4 | 1.0 | 19.1 |
| Collin Murray-Boyles (TOR) | 98% | 30.0<br><sub>23,20,28,23,34</sub> | 14.0<br><sub>15,4,18,13,19</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>5,3,7,3,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>1,1,0,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.4<br><sub>1,0,1,1,0</sub> |  | 1.4 | 1.3 | 1.9 | 23.7 |
| Jamal Shead (TOR) | 98% | 28.9<br><sub>23,25,20,20,34</sub> | 8.8<br><sub>2,9,6,3,10</sub> |  | 2.5<br><sub>1,2,1,3,3</sub> |  | 7.5<br><sub>8,6,6,6,16</sub> |  | 1.2<br><sub>0,2,0,1,1</sub> |  | 1.5 | 0.3 | 2.1 | 18.8 |
| Jakob Poeltl (TOR) | 86% | 25.3<br><sub>23,-,-,19,31</sub> | 10.7<br><sub>12,-,-,8,19</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>11,-,-,5,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>3,-,-,1,1</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.1 | 1.2 | 1.5 | 20.4 |
| Jamison Battle (TOR) | 98% | 21.2<br><sub>19,17,21,19,21</sub> | 9.0<br><sub>2,20,12,9,6</sub> |  | 3.0<br><sub>0,5,0,1,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.4<br><sub>0,4,4,2,1</sub> |  | 0.5 | 0.2 | 0.7 | 12.9 |
| Alijah Martin (TOR) | 88% | 19.0<br><sub>-,16,6,9,31</sub> | 8.4<br><sub>-,5,2,6,27</sub> |  | 2.9<br><sub>-,2,2,1,4</sub> |  | 1.8<br><sub>-,4,0,0,1</sub> |  | 0.9<br><sub>-,1,0,0,6</sub> |  | 0.8 | 0.4 | 1.4 | 13.0 |
| Allen Graves (TOR) | 98% | 15.9<br><sub>9,10,7,14,16</sub> | 5.3<br><sub>7,3,0,5,3</sub> |  | 2.8<br><sub>4,0,0,1,2</sub> |  | 0.9<br><sub>0,0,2,1,0</sub> |  | 0.4<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.6 | 0.6 | 8.9 |
| Kyle Anderson (TOR) | 63% | 9.3<br><sub>-,4,8,4,-</sub> | 2.6<br><sub>-,2,2,2,-</sub> |  | 1.8<br><sub>-,3,0,0,-</sub> |  | 1.6<br><sub>-,3,0,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.4 | 0.5 | 5.9 |
| Jaden Bradley (TOR) | 71% | 9.0<br><sub>-,4,-,4,8</sub> | 3.4<br><sub>-,3,-,2,3</sub> |  | 1.5<br><sub>-,1,-,1,0</sub> |  | 1.1<br><sub>-,2,-,0,1</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.7 | 0.2 | 0.6 | 6.0 |
| Trayce Jackson-Davis (TOR) | 72% | 8.2<br><sub>1,9,2,4,-</sub> | 3.2<br><sub>0,5,0,1,-</sub> |  | 2.9<br><sub>0,5,0,0,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.5 | 0.4 | 6.6 |

</details>


### IND @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.9–117.8 | IND 36% | 2.77 / 1.56 | DAL -5.5 | 230.5 | DAL -3.5 covers 55%; o226.5 59% |
| Expected (weighted by chance each plays) | 113.5–118.2 | IND 37% | 2.72 / 1.58 | DAL -4.5 | 231.5 | DAL -3.5 covers 54%; o226.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| T.J. McConnell (IND) | Questionable | 55% | 12.2 | 6.6 | 1.7 | 3.7 | 0.2 | 0.7 | 0.1 | 0.9 | 12.0 | small |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 80% | 32.8<br><sub>30,35,-,38,31</sub> | 18.5<br><sub>22,23,-,22,9</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>2,3,-,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 8.9<br><sub>9,4,-,5,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>5,4,-,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.1 | 2.5 | 30.5 |
| Pascal Siakam | 86% | 32.6<br><sub>29,36,-,30,32</sub> | 24.2<br><sub>13,17,-,20,23</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,5,-,4,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>4,5,-,2,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,0,-,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 2.6 | 35.4 |
| Aaron Nesmith | 86% | 27.8<br><sub>21,30,-,30,27</sub> | 14.5<br><sub>9,11,-,16,8</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,3,-,2,5</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>2,4,-,2,1</sub> |  | 1.9<br><sub>1,0,-,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.4 | 1.6 | 20.1 |
| Jarace Walker | 98% | 23.9<br><sub>28,20,45,17,20</sub> | 10.4<br><sub>14,6,15,2,9</sub> |  | 5.5<br><sub>6,6,7,8,5</sub> |  | 2.7<br><sub>4,3,3,1,2</sub> |  | 1.3<br><sub>3,2,1,0,1</sub> |  | 0.9 | 0.4 | 1.6 | 18.7 |
| Quenton Jackson | 98% | 22.0<br><sub>24,24,35,22,17</sub> | 10.9<br><sub>24,12,20,13,6</sub> |  | 3.3<br><sub>4,3,7,7,4</sub> |  | 3.6<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>2,3,1,3,0</sub> |  | 1.0 | 0.2 | 1.4 | 17.8 |
| Kelly Oubre Jr. | 67% | 21.7<br><sub>22,20,-,-,16</sub> | 9.1<br><sub>10,11,-,-,2</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,2,-,-,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>1,1,-,-,0</sub> |  | 0.8<br><sub>1,2,-,-,0</sub> |  | 0.9 | 0.4 | 0.9 | 13.8 |
| Ivica Zubac | 58% | 20.9<br><sub>-,-,-,19,19</sub> | 9.8<br><sub>-,-,-,1,10</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>-,-,-,4,12</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>-,-,-,2,5</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.6 | 1.3 | 19.9 |
| Obi Toppin | 64% | 20.5<br><sub>-,-,-,19,22</sub> | 12.2<br><sub>-,-,-,11,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>-,-,-,5,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>-,-,-,1,2</sub> |  | 1.5<br><sub>-,-,-,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.3 | 1.3 | 19.1 |
| Jay Huff | 96% | 16.3<br><sub>19,17,40,14,10</sub> | 7.0<br><sub>13,0,22,6,0</sub> |  | 3.4<br><sub>1,3,8,3,3</sub> |  | 1.3<br><sub>0,0,2,1,0</sub> |  | 0.8<br><sub>3,0,0,2,0</sub> |  | 0.5 | 1.1 | 0.8 | 11.7 |
| Braden Smith | 88% | 15.8<br><sub>12,1,42,24,12</sub> | 5.5<br><sub>1,0,19,10,0</sub> |  | 1.5<br><sub>0,0,4,1,0</sub> |  | 3.1<br><sub>1,0,10,5,2</sub> |  | 0.3<br><sub>0,0,2,0,0</sub> |  | 0.8 | 0.3 | 0.9 | 10.1 |
| Kobe Brown | 72% | 14.9<br><sub>20,15,38,7,-</sub> | 5.4<br><sub>9,3,16,0,-</sub> |  | 2.8<br><sub>6,1,6,1,-</sub> |  | 1.4<br><sub>4,1,1,0,-</sub> |  | 0.6<br><sub>0,1,2,0,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.5 |
| Jalen Slawson | 93% | 14.4<br><sub>18,18,41,6,12</sub> | 4.2<br><sub>4,3,12,2,4</sub> |  | 2.8<br><sub>4,5,7,2,1</sub> |  | 1.4<br><sub>1,0,3,1,2</sub> |  | 0.3<br><sub>0,0,2,0,0</sub> |  | 0.8 | 0.6 | 0.8 | 8.5 |
| Larry Nance Jr. | 91% | 14.2<br><sub>18,26,-,14,13</sub> | 4.5<br><sub>6,4,-,4,15</sub> |  | 3.1<br><sub>2,6,-,4,2</sub> |  | 1.0<br><sub>1,1,-,1,1</sub> |  | 0.5<br><sub>2,1,-,0,5</sub> |  | 0.7 | 0.2 | 0.6 | 8.5 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 33.0<br><sub>39,40,40,33,28</sub> | 23.2<br><sub>33,17,19,21,25</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>9,4,10,10,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.0<br><sub>6,6,5,7,12</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.9 | 2.4 | 36.2 |
| Kyrie Irving | 98% | 32.2<br><sub>35,-,36,28,29</sub> | 21.9<br><sub>35,-,29,14,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>4,-,7,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.4<br><sub>9,-,5,2,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>5,-,5,0,2</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.5 | 2.0 | 30.8 |
| P.J. Washington | 98% | 31.3<br><sub>34,38,39,33,25</sub> | 13.7<br><sub>3,12,21,26,6</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>10,5,10,6,5</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,1,3,1,0</sub> |  | 1.8<br><sub>1,2,3,6,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.9 | 1.4 | 22.6 |
| Naji Marshall | 88% | 22.9<br><sub>-,24,26,25,15</sub> | 12.0<br><sub>-,5,22,7,8</sub> |  | 3.5<br><sub>-,2,5,1,1</sub> |  | 3.4<br><sub>-,7,3,5,2</sub> |  | 0.8<br><sub>-,0,3,0,1</sub> |  | 1.0 | 0.1 | 1.4 | 18.8 |
| Daniel Gafford | 98% | 20.1<br><sub>29,26,18,18,19</sub> | 9.9<br><sub>18,20,2,7,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>7,7,4,1,5</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>2,0,1,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.5 | 1.0 | 17.6 |
| Zaccharie Risacher | 96% | 19.7<br><sub>28,19,18,21,16</sub> | 6.3<br><sub>12,0,2,4,11</sub> |  | 4.3<br><sub>6,5,1,4,6</sub> |  | 1.1<br><sub>3,1,2,1,1</sub> |  | 0.6<br><sub>3,0,0,0,1</sub> |  | 0.8 | 0.8 | 0.7 | 11.7 |
| Max Christie | 98% | 16.2<br><sub>18,8,-,9,17</sub> | 5.9<br><sub>2,0,-,0,5</sub> |  | 1.9<br><sub>1,2,-,1,2</sub> |  | 1.0<br><sub>0,0,-,1,0</sub> |  | 0.9<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.2 | 0.7 | 8.9 |
| Walter Clayton Jr. | 91% | 15.4<br><sub>9,24,21,23,16</sub> | 6.2<br><sub>3,20,8,12,5</sub> |  | 2.6<br><sub>2,1,6,4,4</sub> |  | 2.9<br><sub>1,2,5,2,6</sub> |  | 0.7<br><sub>1,4,2,1,1</sub> |  | 0.6 | 0.2 | 0.9 | 11.7 |
| Santi Aldama | 97% | 14.9<br><sub>-,-,-,13,15</sub> | 6.7<br><sub>-,-,-,8,12</sub> |  | 4.0<br><sub>-,-,-,9,2</sub> |  | 1.3<br><sub>-,-,-,1,0</sub> |  | 0.7<br><sub>-,-,-,0,2</sub> |  | 0.6 | 0.4 | 0.7 | 12.0 |
| Caleb Martin | 97% | 14.5<br><sub>25,21,20,11,19</sub> | 4.0<br><sub>8,5,0,0,2</sub> |  | 2.3<br><sub>0,6,3,0,2</sub> |  | 1.0<br><sub>0,0,2,0,2</sub> |  | 0.3<br><sub>2,1,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 7.3 |
| Morez Johnson Jr. | 98% | 14.4<br><sub>17,17,18,24,19</sub> | 6.0<br><sub>2,13,8,13,4</sub> |  | 3.2<br><sub>2,2,3,17,9</sub> |  | 1.3<br><sub>1,1,1,2,1</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.4 | 0.1 | 0.8 | 10.5 |
| Marcus Sasser | 80% | 11.6<br><sub>7,19,5,-,9</sub> | 4.4<br><sub>0,4,0,-,4</sub> |  | 1.0<br><sub>0,1,1,-,0</sub> |  | 1.6<br><sub>1,1,2,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.0 |
| Moussa Cisse | 67% | 7.6<br><sub>-,2,-,1,5</sub> | 2.9<br><sub>-,0,-,0,2</sub> |  | 3.2<br><sub>-,0,-,0,1</sub> |  | 0.2<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.5 | 6.3 |
| Tobi Lawal | 66% | 6.4<br><sub>-,2,-,1,5</sub> | 2.7<br><sub>-,2,-,0,2</sub> |  | 2.3<br><sub>-,0,-,0,0</sub> |  | 0.6<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.7 |
| Jett Howard | 64% | 6.2<br><sub>-,2,-,1,3</sub> | 2.7<br><sub>-,2,-,0,5</sub> |  | 0.8<br><sub>-,0,-,0,1</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,1</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |

</details>


### DEN @ HOU
Out: Steven Adams (HOU), Clint Capela (HOU), Oscar Tshiebwe (HOU), Julian Strawther (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.3–118.2 | DEN 26% | 3.78 / 1.36 | HOU -8.5 | 227.5 | HOU -9.5 covers 49%; o219.5 67% |
| Expected (weighted by chance each plays) | 109.4–117.1 | DEN 29% | 3.40 / 1.42 | HOU -7.5 | 226.5 | HOU -9.5 covers 45%; o219.5 65% |
| if Jamal Murray plays | 109.3–118.2 | DEN 26% | 3.78 / 1.36 | HOU -8.5 | 227.5 | HOU -9.5 covers 49%; o219.5 67% |
| if Christian Braun plays | 109.3–118.2 | DEN 26% | 3.78 / 1.36 | HOU -8.5 | 227.5 | HOU -9.5 covers 49%; o219.5 67% |
| if Cameron Johnson plays | 109.3–118.2 | DEN 26% | 3.78 / 1.36 | HOU -8.5 | 227.5 | HOU -9.5 covers 49%; o219.5 67% |
| if Nikola Jokic plays | 109.3–118.1 | DEN 27% | 3.76 / 1.36 | HOU -8.5 | 227.5 | HOU -9.5 covers 48%; o219.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray (DEN) | Questionable | 55% | 36.9 | 28.0 | 4.8 | 7.4 | 3.2 | 1.1 | 0.4 | 3.5 | 40.2 | full tables below |
| Christian Braun (DEN) | Questionable | 55% | 34.9 | 17.6 | 4.6 | 3.6 | 1.6 | 1.3 | 0.4 | 1.7 | 25.8 | full tables below |
| Cameron Johnson (DEN) | Questionable | 55% | 33.0 | 17.1 | 4.3 | 3.2 | 2.2 | 1.1 | 0.4 | 1.8 | 24.6 | full tables below |
| Nikola Jokic (DEN) | Questionable | 55% | 36.0 | 28.2 | 12.3 | 10.4 | 1.7 | 1.7 | 0.8 | 4.4 | 51.0 | full tables below |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aaron Gordon | 54% | 32.3<br><sub>31,29,30,25,27</sub> | 20.1<br><sub>15,15,5,17,12</sub> |  | 5.9<br><sub>11,4,6,1,5</sub> |  | 3.5<br><sub>3,5,2,0,0</sub> |  | 1.7<br><sub>2,2,1,1,0</sub> |  | 0.9 | 0.3 | 2.2 | 29.5 |
| DeMar DeRozan | 44% | 30.3<br><sub>26,24,20,-,22</sub> | 20.8<br><sub>6,3,9,-,11</sub> |  | 2.9<br><sub>2,1,0,-,1</sub> |  | 5.3<br><sub>5,5,1,-,5</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.9 | 0.3 | 2.3 | 29.0 |
| Tyus Jones | 96% | 28.0<br><sub>11,11,8,18,13</sub> | 10.2<br><sub>5,3,2,6,3</sub> |  | 2.7<br><sub>0,0,0,1,4</sub> |  | 5.8<br><sub>1,0,1,8,4</sub> |  | 1.3<br><sub>1,1,0,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 18.7 |
| Bryce Hopkins | 67% | 27.6<br><sub>14,-,-,28,3</sub> | 11.6<br><sub>0,-,-,18,3</sub> |  | 4.0<br><sub>2,-,-,4,1</sub> |  | 1.4<br><sub>0,-,-,1,0</sub> |  | 0.9<br><sub>0,-,-,1,0</sub> |  | 0.8 | 0.4 | 1.6 | 17.0 |
| Trevon Brazile | 97% | 27.5<br><sub>32,19,18,23,14</sub> | 10.6<br><sub>11,6,6,6,3</sub> |  | 6.5<br><sub>8,3,5,7,4</sub> |  | 1.3<br><sub>0,1,1,1,2</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.0 | 0.6 | 1.3 | 18.4 |
| Marvin Bagley III | 98% | 27.4<br><sub>19,11,12,14,12</sub> | 16.7<br><sub>8,0,6,10,10</sub> |  | 7.5<br><sub>5,5,4,2,3</sub> |  | 1.8<br><sub>1,0,0,2,0</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.8 | 26.0 |
| Spencer Jones | 52% | 27.2<br><sub>-,-,-,-,21</sub> | 12.3<br><sub>-,-,-,-,13</sub> |  | 5.3<br><sub>-,-,-,-,6</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,3</sub> |  | 0.9 | 0.6 | 1.3 | 18.8 |
| Alpha Diallo | 64% | 24.5<br><sub>-,-,6,4,-</sub> | 10.4<br><sub>-,-,0,0,-</sub> |  | 3.4<br><sub>-,-,1,0,-</sub> |  | 1.9<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8 | 0.3 | 1.3 | 15.7 |
| Zeke Nnaji | 43% | 23.8<br><sub>-,-,-,4,-</sub> | 9.1<br><sub>-,-,-,2,-</sub> |  | 4.8<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.9 | 1.4 | 15.2 |
| Ryan Nembhard | 52% | 23.8<br><sub>-,-,-,4,-</sub> | 13.5<br><sub>-,-,-,0,-</sub> |  | 3.2<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.3 | 1.8 | 19.0 |
| Cam Whitmore | 58% | 23.3<br><sub>-,-,-,-,-</sub> | 13.1<br><sub>-,-,-,-,-</sub> |  | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.5 | 1.4 | 18.4 |
| DaRon Holmes II | 48% | 22.1<br><sub>-,-,-,4,-</sub> | 9.7<br><sub>-,-,-,0,-</sub> |  | 4.1<br><sub>-,-,-,1,-</sub> |  | 1.5<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.6 | 1.4 | 15.3 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.8<br><sub>35,33,36,35,39</sub> | 17.3<br><sub>22,30,14,11,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>3,9,10,4,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,5,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,6,4,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.9 | 1.2 | 27.0 |
| Kevin Durant | 98% | 36.3<br><sub>37,27,33,35,38</sub> | 22.4<br><sub>28,14,12,21,21</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>5,3,3,5,10</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>1,4,3,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 3.0 | 33.2 |
| Amen Thompson | 98% | 35.9<br><sub>39,28,25,32,39</sub> | 17.4<br><sub>15,8,14,11,17</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>3,3,3,8,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>6,1,3,1,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.8 | 1.9 | 29.3 |
| Alperen Sengun | 84% | 35.8<br><sub>-,33,38,39,32</sub> | 20.2<br><sub>-,16,26,17,15</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>-,9,7,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>-,9,10,10,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>-,0,1,0,1</sub> |  | 1.3 | 1.2 | 2.8 | 37.3 |
| Fred VanVleet | 88% | 33.0<br><sub>33,-,27,30,31</sub> | 13.2<br><sub>16,-,8,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>5,-,2,3,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.4<br><sub>6,-,9,3,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,-,2,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.4 | 22.1 |
| Tari Eason | 98% | 25.5<br><sub>26,19,27,24,23</sub> | 10.7<br><sub>11,8,13,9,2</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>13,3,4,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,3,1,2</sub> |  | 1.1<br><sub>0,2,3,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.8 | 1.0 | 18.4 |
| Marcus Smart | 88% | 22.7<br><sub>17,36,20,18,20</sub> | 8.5<br><sub>8,24,8,4,5</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,5,4,1,2</sub> |  | 2.5<br><sub>4,3,4,1,0</sub> |  | 1.2<br><sub>0,7,2,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 1.3 | 13.4 |
| Reed Sheppard | 76% | 20.8<br><sub>-,-,17,21,13</sub> | 9.8<br><sub>-,-,8,14,6</sub> |  | 2.0<br><sub>-,-,1,2,0</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.7<br><sub>-,-,2,3,2</sub> |  | 1.2 | 0.5 | 1.0 | 14.4 |
| Bogdan Bogdanovic | 96% | 9.8<br><sub>11,19,5,5,2</sub> | 3.7<br><sub>6,4,0,0,0</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.9<br><sub>0,1,1,0,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford | 52% | 7.3<br><sub>-,19,2,-,-</sub> | 2.5<br><sub>-,8,0,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.9 |
| Jae'Sean Tate | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,3,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Bruce Thornton | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.4<br><sub>-,5,2,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.0 |

</details>

<details><summary>if Jamal Murray plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray (DEN) | 100% | 36.9<br><sub>38,37,39,28,34</sub> | 28.0<br><sub>23,39,35,14,16</sub> | 20.5 · – | 4.8<br><sub>1,8,5,5,6</sub> | 4.5 | 7.4<br><sub>6,5,6,7,8</sub> | 6.5 | 3.2<br><sub>5,7,4,2,2</sub> | 2.5 | 1.1 | 0.4 | 3.5 | 40.2 |
| Aaron Gordon (DEN) | 54% | 32.2<br><sub>31,29,30,25,27</sub> | 17.4<br><sub>15,15,5,17,12</sub> |  | 5.9<br><sub>11,4,6,1,5</sub> |  | 3.5<br><sub>3,5,2,0,0</sub> |  | 1.6<br><sub>2,2,1,1,0</sub> |  | 0.9 | 0.3 | 2.2 | 26.8 |
| DeMar DeRozan (DEN) | 44% | 30.0<br><sub>26,24,20,-,22</sub> | 18.2<br><sub>6,3,9,-,11</sub> |  | 2.9<br><sub>2,1,0,-,1</sub> |  | 5.2<br><sub>5,5,1,-,5</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 1.0 | 0.3 | 2.3 | 26.3 |
| Trevon Brazile (DEN) | 97% | 27.6<br><sub>32,19,18,23,14</sub> | 9.2<br><sub>11,6,6,6,3</sub> |  | 6.5<br><sub>8,3,5,7,4</sub> |  | 1.4<br><sub>0,1,1,1,2</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 1.0 | 0.6 | 1.3 | 17.1 |
| Bryce Hopkins (DEN) | 67% | 27.6<br><sub>14,-,-,28,3</sub> | 10.1<br><sub>0,-,-,18,3</sub> |  | 4.0<br><sub>2,-,-,4,1</sub> |  | 1.4<br><sub>0,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.9 | 0.4 | 1.6 | 15.5 |
| Marvin Bagley III (DEN) | 98% | 27.4<br><sub>19,11,12,14,12</sub> | 14.5<br><sub>8,0,6,10,10</sub> |  | 7.6<br><sub>5,5,4,2,3</sub> |  | 1.8<br><sub>1,0,0,2,0</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.9 | 23.9 |
| Spencer Jones (DEN) | 52% | 27.2<br><sub>-,-,-,-,21</sub> | 10.8<br><sub>-,-,-,-,13</sub> |  | 5.3<br><sub>-,-,-,-,6</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,3</sub> |  | 0.9 | 0.6 | 1.3 | 17.3 |
| Tyus Jones (DEN) | 96% | 27.2<br><sub>11,11,8,18,13</sub> | 8.6<br><sub>5,3,2,6,3</sub> |  | 2.6<br><sub>0,0,0,1,4</sub> |  | 5.7<br><sub>1,0,1,8,4</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 16.9 |
| Alpha Diallo (DEN) | 64% | 24.7<br><sub>-,-,6,4,-</sub> | 9.2<br><sub>-,-,0,0,-</sub> |  | 3.4<br><sub>-,-,1,0,-</sub> |  | 2.0<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8 | 0.3 | 1.4 | 14.5 |
| Zeke Nnaji (DEN) | 43% | 23.8<br><sub>-,-,-,4,-</sub> | 7.9<br><sub>-,-,-,2,-</sub> |  | 4.8<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.9 | 1.0 | 1.4 | 14.1 |
| Cam Whitmore (DEN) | 58% | 23.4<br><sub>-,-,-,-,-</sub> | 11.5<br><sub>-,-,-,-,-</sub> |  | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.5 | 1.5 | 16.8 |
| Ryan Nembhard (DEN) | 52% | 23.1<br><sub>-,-,-,4,-</sub> | 11.2<br><sub>-,-,-,0,-</sub> |  | 3.2<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,0,-</sub> |  | 1.0<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.3 | 1.7 | 16.6 |
| DaRon Holmes II (DEN) | 48% | 21.9<br><sub>-,-,-,4,-</sub> | 8.3<br><sub>-,-,-,0,-</sub> |  | 4.1<br><sub>-,-,-,1,-</sub> |  | 1.5<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.6 | 1.4 | 13.8 |
| Jabari Smith Jr. (HOU) | 98% | 36.7<br><sub>35,33,36,35,39</sub> | 17.2<br><sub>22,30,14,11,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>3,9,10,4,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,5,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,6,4,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.9 | 1.2 | 26.9 |
| Kevin Durant (HOU) | 98% | 36.3<br><sub>37,27,33,35,38</sub> | 22.6<br><sub>28,14,12,21,21</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>5,3,3,5,10</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>1,4,3,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 3.0 | 33.3 |
| Amen Thompson (HOU) | 98% | 35.8<br><sub>39,28,25,32,39</sub> | 17.3<br><sub>15,8,14,11,17</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>3,3,3,8,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>6,1,3,1,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.8 | 1.9 | 29.1 |
| Alperen Sengun (HOU) | 84% | 35.7<br><sub>-,33,38,39,32</sub> | 20.1<br><sub>-,16,26,17,15</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 10.4<br><sub>-,9,7,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>-,9,10,10,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>-,0,1,0,1</sub> |  | 1.3 | 1.2 | 2.8 | 37.2 |
| Fred VanVleet (HOU) | 88% | 33.1<br><sub>33,-,27,30,31</sub> | 13.3<br><sub>16,-,8,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>5,-,2,3,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.4<br><sub>6,-,9,3,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,-,2,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.4 | 22.2 |
| Tari Eason (HOU) | 98% | 25.5<br><sub>26,19,27,24,23</sub> | 10.6<br><sub>11,8,13,9,2</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>13,3,4,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,3,1,2</sub> |  | 1.1<br><sub>0,2,3,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.8 | 1.0 | 18.4 |
| Marcus Smart (HOU) | 88% | 22.7<br><sub>17,36,20,18,20</sub> | 8.4<br><sub>8,24,8,4,5</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,5,4,1,2</sub> |  | 2.5<br><sub>4,3,4,1,0</sub> |  | 1.2<br><sub>0,7,2,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 1.3 | 13.4 |
| Reed Sheppard (HOU) | 76% | 20.8<br><sub>-,-,17,21,13</sub> | 9.9<br><sub>-,-,8,14,6</sub> |  | 2.0<br><sub>-,-,1,2,0</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.7<br><sub>-,-,2,3,2</sub> |  | 1.2 | 0.5 | 1.0 | 14.5 |
| Bogdan Bogdanovic (HOU) | 96% | 9.8<br><sub>11,19,5,5,2</sub> | 3.7<br><sub>6,4,0,0,0</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.9<br><sub>0,1,1,0,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford (HOU) | 52% | 7.3<br><sub>-,19,2,-,-</sub> | 2.5<br><sub>-,8,0,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.9 |
| Jae'Sean Tate (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,3,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.9 |
| Bruce Thornton (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.4<br><sub>-,5,2,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.0 |

</details>

<details><summary>if Cameron Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Johnson (DEN) | 100% | 33.0<br><sub>-,34,34,30,29</sub> | 17.1<br><sub>-,12,7,12,18</sub> |  | 4.3<br><sub>-,9,4,2,4</sub> |  | 3.2<br><sub>-,3,2,2,1</sub> |  | 2.2<br><sub>-,2,1,4,2</sub> |  | 1.1 | 0.4 | 1.8 | 24.6 |
| Aaron Gordon (DEN) | 54% | 32.3<br><sub>31,29,30,25,27</sub> | 18.4<br><sub>15,15,5,17,12</sub> |  | 5.9<br><sub>11,4,6,1,5</sub> |  | 3.5<br><sub>3,5,2,0,0</sub> |  | 1.7<br><sub>2,2,1,1,0</sub> |  | 0.9 | 0.3 | 2.2 | 27.9 |
| DeMar DeRozan (DEN) | 44% | 30.2<br><sub>26,24,20,-,22</sub> | 19.3<br><sub>6,3,9,-,11</sub> |  | 2.8<br><sub>2,1,0,-,1</sub> |  | 5.3<br><sub>5,5,1,-,5</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.9 | 0.3 | 2.3 | 27.4 |
| Tyus Jones (DEN) | 96% | 28.1<br><sub>11,11,8,18,13</sub> | 9.4<br><sub>5,3,2,6,3</sub> |  | 2.7<br><sub>0,0,0,1,4</sub> |  | 5.8<br><sub>1,0,1,8,4</sub> |  | 1.2<br><sub>1,1,0,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 18.0 |
| Trevon Brazile (DEN) | 97% | 27.6<br><sub>32,19,18,23,14</sub> | 9.9<br><sub>11,6,6,6,3</sub> |  | 6.5<br><sub>8,3,5,7,4</sub> |  | 1.4<br><sub>0,1,1,1,2</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.0 | 0.6 | 1.3 | 17.7 |
| Bryce Hopkins (DEN) | 67% | 27.4<br><sub>14,-,-,28,3</sub> | 10.6<br><sub>0,-,-,18,3</sub> |  | 3.9<br><sub>2,-,-,4,1</sub> |  | 1.4<br><sub>0,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.8 | 0.4 | 1.6 | 15.9 |
| Spencer Jones (DEN) | 52% | 26.9<br><sub>-,-,-,-,21</sub> | 11.2<br><sub>-,-,-,-,13</sub> |  | 5.3<br><sub>-,-,-,-,6</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,3</sub> |  | 0.8 | 0.7 | 1.3 | 17.8 |
| Marvin Bagley III (DEN) | 98% | 26.7<br><sub>19,11,12,14,12</sub> | 15.0<br><sub>8,0,6,10,10</sub> |  | 7.4<br><sub>5,5,4,2,3</sub> |  | 1.7<br><sub>1,0,0,2,0</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.9 | 1.8 | 24.2 |
| Ryan Nembhard (DEN) | 52% | 23.7<br><sub>-,-,-,4,-</sub> | 12.4<br><sub>-,-,-,0,-</sub> |  | 3.2<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,0,-</sub> |  | 1.0<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.3 | 1.8 | 17.9 |
| Alpha Diallo (DEN) | 64% | 23.5<br><sub>-,-,6,4,-</sub> | 9.4<br><sub>-,-,0,0,-</sub> |  | 3.2<br><sub>-,-,1,0,-</sub> |  | 1.9<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8 | 0.3 | 1.3 | 14.5 |
| Zeke Nnaji (DEN) | 43% | 22.7<br><sub>-,-,-,4,-</sub> | 8.0<br><sub>-,-,-,2,-</sub> |  | 4.7<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.9 | 1.3 | 13.9 |
| DaRon Holmes II (DEN) | 48% | 21.4<br><sub>-,-,-,4,-</sub> | 8.8<br><sub>-,-,-,0,-</sub> |  | 4.0<br><sub>-,-,-,1,-</sub> |  | 1.4<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.6 | 1.3 | 14.2 |
| Cam Whitmore (DEN) | 58% | 21.3<br><sub>-,-,-,-,-</sub> | 11.0<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.8 | 0.5 | 1.4 | 15.9 |
| Jabari Smith Jr. (HOU) | 98% | 36.8<br><sub>35,33,36,35,39</sub> | 17.3<br><sub>22,30,14,11,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>3,9,10,4,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,5,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,6,4,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.9 | 1.2 | 27.0 |
| Kevin Durant (HOU) | 98% | 36.3<br><sub>37,27,33,35,38</sub> | 22.4<br><sub>28,14,12,21,21</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>5,3,3,5,10</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>1,4,3,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 3.0 | 33.2 |
| Amen Thompson (HOU) | 98% | 35.9<br><sub>39,28,25,32,39</sub> | 17.4<br><sub>15,8,14,11,17</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>3,3,3,8,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>6,1,3,1,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.8 | 1.9 | 29.3 |
| Alperen Sengun (HOU) | 84% | 35.8<br><sub>-,33,38,39,32</sub> | 20.2<br><sub>-,16,26,17,15</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>-,9,7,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>-,9,10,10,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>-,0,1,0,1</sub> |  | 1.3 | 1.2 | 2.8 | 37.3 |
| Fred VanVleet (HOU) | 88% | 33.0<br><sub>33,-,27,30,31</sub> | 13.2<br><sub>16,-,8,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>5,-,2,3,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.4<br><sub>6,-,9,3,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,-,2,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.4 | 22.1 |
| Tari Eason (HOU) | 98% | 25.5<br><sub>26,19,27,24,23</sub> | 10.7<br><sub>11,8,13,9,2</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>13,3,4,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,3,1,2</sub> |  | 1.1<br><sub>0,2,3,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.8 | 1.0 | 18.4 |
| Marcus Smart (HOU) | 88% | 22.7<br><sub>17,36,20,18,20</sub> | 8.5<br><sub>8,24,8,4,5</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,5,4,1,2</sub> |  | 2.5<br><sub>4,3,4,1,0</sub> |  | 1.2<br><sub>0,7,2,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 1.3 | 13.4 |
| Reed Sheppard (HOU) | 76% | 20.8<br><sub>-,-,17,21,13</sub> | 9.8<br><sub>-,-,8,14,6</sub> |  | 2.0<br><sub>-,-,1,2,0</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.7<br><sub>-,-,2,3,2</sub> |  | 1.2 | 0.5 | 1.0 | 14.4 |
| Bogdan Bogdanovic (HOU) | 96% | 9.8<br><sub>11,19,5,5,2</sub> | 3.7<br><sub>6,4,0,0,0</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.9<br><sub>0,1,1,0,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford (HOU) | 52% | 7.3<br><sub>-,19,2,-,-</sub> | 2.5<br><sub>-,8,0,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.9 |
| Jae'Sean Tate (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,3,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Bruce Thornton (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.4<br><sub>-,5,2,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.0 |

</details>

<details><summary>if Christian Braun plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Christian Braun (DEN) | 100% | 34.9<br><sub>36,37,37,28,29</sub> | 17.6<br><sub>15,31,14,11,6</sub> |  | 4.6<br><sub>0,3,3,3,4</sub> |  | 3.6<br><sub>4,1,3,3,1</sub> |  | 1.6<br><sub>3,7,1,1,0</sub> |  | 1.3 | 0.4 | 1.7 | 25.8 |
| Aaron Gordon (DEN) | 54% | 32.3<br><sub>31,29,30,25,27</sub> | 18.5<br><sub>15,15,5,17,12</sub> |  | 5.9<br><sub>11,4,6,1,5</sub> |  | 3.5<br><sub>3,5,2,0,0</sub> |  | 1.7<br><sub>2,2,1,1,0</sub> |  | 0.9 | 0.3 | 2.2 | 27.9 |
| DeMar DeRozan (DEN) | 44% | 30.0<br><sub>26,24,20,-,22</sub> | 19.1<br><sub>6,3,9,-,11</sub> |  | 2.8<br><sub>2,1,0,-,1</sub> |  | 5.3<br><sub>5,5,1,-,5</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 1.0 | 0.3 | 2.3 | 27.2 |
| Bryce Hopkins (DEN) | 67% | 27.6<br><sub>14,-,-,28,3</sub> | 10.6<br><sub>0,-,-,18,3</sub> |  | 4.0<br><sub>2,-,-,4,1</sub> |  | 1.4<br><sub>0,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.9 | 0.4 | 1.6 | 15.9 |
| Trevon Brazile (DEN) | 97% | 27.5<br><sub>32,19,18,23,14</sub> | 9.7<br><sub>11,6,6,6,3</sub> |  | 6.5<br><sub>8,3,5,7,4</sub> |  | 1.4<br><sub>0,1,1,1,2</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.0 | 0.6 | 1.3 | 17.5 |
| Marvin Bagley III (DEN) | 98% | 27.4<br><sub>19,11,12,14,12</sub> | 15.3<br><sub>8,0,6,10,10</sub> |  | 7.5<br><sub>5,5,4,2,3</sub> |  | 1.8<br><sub>1,0,0,2,0</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.8 | 24.6 |
| Spencer Jones (DEN) | 52% | 27.1<br><sub>-,-,-,-,21</sub> | 11.2<br><sub>-,-,-,-,13</sub> |  | 5.2<br><sub>-,-,-,-,6</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,3</sub> |  | 0.9 | 0.6 | 1.3 | 17.7 |
| Tyus Jones (DEN) | 96% | 27.1<br><sub>11,11,8,18,13</sub> | 9.0<br><sub>5,3,2,6,3</sub> |  | 2.6<br><sub>0,0,0,1,4</sub> |  | 5.6<br><sub>1,0,1,8,4</sub> |  | 1.2<br><sub>1,1,0,0,1</sub> |  | 1.1 | 0.2 | 1.5 | 17.2 |
| Alpha Diallo (DEN) | 64% | 24.5<br><sub>-,-,6,4,-</sub> | 9.6<br><sub>-,-,0,0,-</sub> |  | 3.4<br><sub>-,-,1,0,-</sub> |  | 2.0<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8 | 0.3 | 1.3 | 15.0 |
| Zeke Nnaji (DEN) | 43% | 23.8<br><sub>-,-,-,4,-</sub> | 8.3<br><sub>-,-,-,2,-</sub> |  | 4.8<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.9 | 1.4 | 14.5 |
| Cam Whitmore (DEN) | 58% | 23.3<br><sub>-,-,-,-,-</sub> | 12.1<br><sub>-,-,-,-,-</sub> |  | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.5 | 1.5 | 17.4 |
| Ryan Nembhard (DEN) | 52% | 23.0<br><sub>-,-,-,4,-</sub> | 11.8<br><sub>-,-,-,0,-</sub> |  | 3.2<br><sub>-,-,-,0,-</sub> |  | 2.1<br><sub>-,-,-,0,-</sub> |  | 1.0<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.3 | 1.7 | 17.1 |
| DaRon Holmes II (DEN) | 48% | 22.1<br><sub>-,-,-,4,-</sub> | 8.9<br><sub>-,-,-,0,-</sub> |  | 4.1<br><sub>-,-,-,1,-</sub> |  | 1.5<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.6 | 1.4 | 14.5 |
| Jabari Smith Jr. (HOU) | 98% | 36.8<br><sub>35,33,36,35,39</sub> | 17.3<br><sub>22,30,14,11,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>3,9,10,4,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,5,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,6,4,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.9 | 1.2 | 27.0 |
| Kevin Durant (HOU) | 98% | 36.3<br><sub>37,27,33,35,38</sub> | 22.4<br><sub>28,14,12,21,21</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>5,3,3,5,10</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>1,4,3,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 3.0 | 33.2 |
| Amen Thompson (HOU) | 98% | 35.9<br><sub>39,28,25,32,39</sub> | 17.4<br><sub>15,8,14,11,17</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>3,3,3,8,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>6,1,3,1,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.8 | 1.9 | 29.3 |
| Alperen Sengun (HOU) | 84% | 35.8<br><sub>-,33,38,39,32</sub> | 20.2<br><sub>-,16,26,17,15</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>-,9,7,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>-,9,10,10,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>-,0,1,0,1</sub> |  | 1.3 | 1.2 | 2.8 | 37.3 |
| Fred VanVleet (HOU) | 88% | 33.0<br><sub>33,-,27,30,31</sub> | 13.2<br><sub>16,-,8,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>5,-,2,3,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.4<br><sub>6,-,9,3,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,-,2,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.4 | 22.1 |
| Tari Eason (HOU) | 98% | 25.5<br><sub>26,19,27,24,23</sub> | 10.7<br><sub>11,8,13,9,2</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>13,3,4,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,3,1,2</sub> |  | 1.1<br><sub>0,2,3,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.8 | 1.0 | 18.4 |
| Marcus Smart (HOU) | 88% | 22.7<br><sub>17,36,20,18,20</sub> | 8.5<br><sub>8,24,8,4,5</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,5,4,1,2</sub> |  | 2.5<br><sub>4,3,4,1,0</sub> |  | 1.2<br><sub>0,7,2,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 1.3 | 13.4 |
| Reed Sheppard (HOU) | 76% | 20.8<br><sub>-,-,17,21,13</sub> | 9.8<br><sub>-,-,8,14,6</sub> |  | 2.0<br><sub>-,-,1,2,0</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.7<br><sub>-,-,2,3,2</sub> |  | 1.2 | 0.5 | 1.0 | 14.4 |
| Bogdan Bogdanovic (HOU) | 96% | 9.8<br><sub>11,19,5,5,2</sub> | 3.7<br><sub>6,4,0,0,0</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.9<br><sub>0,1,1,0,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford (HOU) | 52% | 7.3<br><sub>-,19,2,-,-</sub> | 2.5<br><sub>-,8,0,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.9 |
| Jae'Sean Tate (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,3,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Bruce Thornton (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.4<br><sub>-,5,2,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.0 |

</details>

<details><summary>if Nikola Jokic plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 100% | 36.0<br><sub>34,37,36,30,36</sub> | 28.2<br><sub>21,18,26,32,19</sub> | 25.5 · – | 12.3<br><sub>13,7,9,10,13</sub> | 10.5 | 10.4<br><sub>10,10,8,11,8</sub> | 8.5 | 1.7<br><sub>0,0,2,0,1</sub> | 1.5 | 1.7 | 0.8 | 4.4 | 51.0 |
| Aaron Gordon (DEN) | 54% | 32.1<br><sub>31,29,30,25,27</sub> | 16.6<br><sub>15,15,5,17,12</sub> |  | 5.8<br><sub>11,4,6,1,5</sub> |  | 3.5<br><sub>3,5,2,0,0</sub> |  | 1.6<br><sub>2,2,1,1,0</sub> |  | 0.8 | 0.3 | 2.1 | 25.9 |
| DeMar DeRozan (DEN) | 44% | 30.2<br><sub>26,24,20,-,22</sub> | 17.3<br><sub>6,3,9,-,11</sub> |  | 2.9<br><sub>2,1,0,-,1</sub> |  | 5.1<br><sub>5,5,1,-,5</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.9 | 0.3 | 2.3 | 25.3 |
| Tyus Jones (DEN) | 96% | 28.1<br><sub>11,11,8,18,13</sub> | 8.9<br><sub>5,3,2,6,3</sub> |  | 2.7<br><sub>0,0,0,1,4</sub> |  | 5.8<br><sub>1,0,1,8,4</sub> |  | 1.2<br><sub>1,1,0,0,1</sub> |  | 1.2 | 0.2 | 1.5 | 17.5 |
| Trevon Brazile (DEN) | 97% | 27.6<br><sub>32,19,18,23,14</sub> | 9.3<br><sub>11,6,6,6,3</sub> |  | 6.5<br><sub>8,3,5,7,4</sub> |  | 1.4<br><sub>0,1,1,1,2</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 1.0 | 0.5 | 1.3 | 17.1 |
| Bryce Hopkins (DEN) | 67% | 27.5<br><sub>14,-,-,28,3</sub> | 10.1<br><sub>0,-,-,18,3</sub> |  | 3.9<br><sub>2,-,-,4,1</sub> |  | 1.4<br><sub>0,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.9 | 0.4 | 1.6 | 15.4 |
| Marvin Bagley III (DEN) | 98% | 27.4<br><sub>19,11,12,14,12</sub> | 14.7<br><sub>8,0,6,10,10</sub> |  | 7.6<br><sub>5,5,4,2,3</sub> |  | 1.8<br><sub>1,0,0,2,0</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.8 | 24.1 |
| Spencer Jones (DEN) | 52% | 27.1<br><sub>-,-,-,-,21</sub> | 10.7<br><sub>-,-,-,-,13</sub> |  | 5.3<br><sub>-,-,-,-,6</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,3</sub> |  | 0.9 | 0.6 | 1.3 | 17.2 |
| Alpha Diallo (DEN) | 64% | 25.3<br><sub>-,-,6,4,-</sub> | 9.5<br><sub>-,-,0,0,-</sub> |  | 3.5<br><sub>-,-,1,0,-</sub> |  | 2.0<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8 | 0.3 | 1.4 | 15.0 |
| Zeke Nnaji (DEN) | 43% | 24.0<br><sub>-,-,-,4,-</sub> | 7.5<br><sub>-,-,-,2,-</sub> |  | 4.9<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.9 | 1.4 | 13.8 |
| Ryan Nembhard (DEN) | 52% | 23.9<br><sub>-,-,-,4,-</sub> | 10.0<br><sub>-,-,-,0,-</sub> |  | 3.3<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,0,-</sub> |  | 0.9<br><sub>-,-,-,0,-</sub> |  | 0.9 | 0.3 | 1.7 | 15.6 |
| Cam Whitmore (DEN) | 58% | 23.3<br><sub>-,-,-,-,-</sub> | 11.6<br><sub>-,-,-,-,-</sub> |  | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.5 | 1.5 | 16.9 |
| DaRon Holmes II (DEN) | 48% | 21.8<br><sub>-,-,-,4,-</sub> | 7.9<br><sub>-,-,-,0,-</sub> |  | 4.1<br><sub>-,-,-,1,-</sub> |  | 1.6<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.5 | 1.4 | 13.5 |
| Jabari Smith Jr. (HOU) | 98% | 36.8<br><sub>35,33,36,35,39</sub> | 17.3<br><sub>22,30,14,11,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>3,9,10,4,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,5,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,6,4,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.9 | 1.2 | 27.1 |
| Kevin Durant (HOU) | 98% | 36.3<br><sub>37,27,33,35,38</sub> | 22.5<br><sub>28,14,12,21,21</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>5,3,3,5,10</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>1,4,3,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.1 | 2.9 | 33.3 |
| Amen Thompson (HOU) | 98% | 35.8<br><sub>39,28,25,32,39</sub> | 17.4<br><sub>15,8,14,11,17</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>3,3,3,8,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>6,1,3,1,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.8 | 1.9 | 29.2 |
| Alperen Sengun (HOU) | 84% | 35.7<br><sub>-,33,38,39,32</sub> | 20.0<br><sub>-,16,26,17,15</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>-,9,7,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>-,9,10,10,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>-,0,1,0,1</sub> |  | 1.3 | 1.2 | 2.8 | 37.1 |
| Fred VanVleet (HOU) | 88% | 33.0<br><sub>33,-,27,30,31</sub> | 13.1<br><sub>16,-,8,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>5,-,2,3,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.4<br><sub>6,-,9,3,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>3,-,2,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.3 | 22.1 |
| Tari Eason (HOU) | 98% | 25.5<br><sub>26,19,27,24,23</sub> | 10.7<br><sub>11,8,13,9,2</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>13,3,4,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,3,1,2</sub> |  | 1.1<br><sub>0,2,3,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.8 | 1.0 | 18.4 |
| Marcus Smart (HOU) | 88% | 22.8<br><sub>17,36,20,18,20</sub> | 8.5<br><sub>8,24,8,4,5</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,5,4,1,2</sub> |  | 2.5<br><sub>4,3,4,1,0</sub> |  | 1.2<br><sub>0,7,2,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 1.3 | 13.4 |
| Reed Sheppard (HOU) | 76% | 20.8<br><sub>-,-,17,21,13</sub> | 9.9<br><sub>-,-,8,14,6</sub> |  | 2.0<br><sub>-,-,1,2,0</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.7<br><sub>-,-,2,3,2</sub> |  | 1.2 | 0.5 | 0.9 | 14.5 |
| Bogdan Bogdanovic (HOU) | 96% | 9.7<br><sub>11,19,5,5,2</sub> | 3.8<br><sub>6,4,0,0,0</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford (HOU) | 52% | 7.3<br><sub>-,19,2,-,-</sub> | 2.5<br><sub>-,8,0,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.9 |
| Jae'Sean Tate (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.0<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,3,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Bruce Thornton (HOU) | 52% | 6.0<br><sub>-,6,2,-,-</sub> | 2.4<br><sub>-,5,2,-,-</sub> |  | 1.1<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.0 |

</details>


### SAS @ PHX
Out: Mark Williams (PHX), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.1–109.4 | SAS 71% | 1.41 / 3.44 | PHX +7.5 | 226.5 | PHX +8.5 covers 52%; o227.5 47% |
| Expected (weighted by chance each plays) | 116.7–109.7 | SAS 70% | 1.43 / 3.31 | PHX +7.5 | 226.5 | PHX +8.5 covers 53%; o227.5 47% |
| if Devin Vassell plays | 117.2–109.6 | SAS 71% | 1.42 / 3.40 | PHX +7.5 | 226.5 | PHX +8.5 covers 52%; o227.5 48% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell (SAS) | Questionable | 55% | 30.9 | 12.1 | 4.1 | 2.4 | 1.9 | 1.2 | 0.4 | 1.1 | 18.6 | full tables below |
| Jordan Goodwin (PHX) | Questionable | 55% | 14.4 | 5.3 | 3.0 | 1.4 | 0.7 | 0.9 | 0.1 | 0.6 | 9.7 | small |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 33.7<br><sub>39,27,36,28,28</sub> | 18.3<br><sub>25,17,21,19,13</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>7,7,5,2,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>6,8,0,3,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.2 | 0.3 | 2.2 | 28.1 |
| Victor Wembanyama | 98% | 33.2<br><sub>34,24,34,26,24</sub> | 27.7<br><sub>43,12,52,30,29</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 11.8<br><sub>7,11,24,14,7</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>4,5,2,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>3,0,1,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 3.4 | 2.8 | 42.8 |
| Stephon Castle | 98% | 32.9<br><sub>22,26,35,28,24</sub> | 18.2<br><sub>0,16,17,19,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>5,5,10,3,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 5.8<br><sub>4,4,3,7,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>0,2,2,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 3.1 | 29.7 |
| De'Aaron Fox | 98% | 32.5<br><sub>35,22,33,26,22</sub> | 16.3<br><sub>22,12,10,9,8</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>8,2,3,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>7,3,4,4,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>0,1,0,0,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.4 | 0.4 | 2.4 | 25.6 |
| Julian Champagnie | 98% | 27.0<br><sub>27,22,21,22,21</sub> | 9.3<br><sub>12,8,0,8,14</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>3,6,4,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,0,3,2,0</sub> |  | 1.8<br><sub>3,2,0,2,4</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.4 | 0.8 | 15.4 |
| Keldon Johnson | 98% | 25.5<br><sub>24,27,19,27,27</sub> | 10.8<br><sub>2,15,4,3,10</sub> |  | 5.5<br><sub>6,7,5,6,7</sub> |  | 1.6<br><sub>0,1,2,6,4</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 17.9 |
| Luke Kornet | 98% | 17.4<br><sub>14,17,14,18,15</sub> | 4.4<br><sub>2,8,2,2,6</sub> |  | 5.0<br><sub>8,5,1,6,4</sub> |  | 1.1<br><sub>0,2,2,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.7 | 10.6 |
| Harrison Barnes | 80% | 17.4<br><sub>-,21,13,19,19</sub> | 5.5<br><sub>-,13,4,13,5</sub> |  | 2.0<br><sub>-,0,2,1,3</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.7<br><sub>-,3,1,2,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.2 |
| Carter Bryant | 86% | 14.7<br><sub>11,14,-,3,17</sub> | 4.8<br><sub>6,3,-,0,6</sub> |  | 2.4<br><sub>0,0,-,0,4</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.6<br><sub>2,1,-,0,2</sub> |  | 0.3 | 0.5 | 0.6 | 8.0 |
| Jordan McLaughlin | 63% | 13.1<br><sub>-,8,-,8,12</sub> | 3.9<br><sub>-,0,-,2,3</sub> |  | 1.6<br><sub>-,1,-,2,0</sub> |  | 1.7<br><sub>-,3,-,1,0</sub> |  | 0.4<br><sub>-,0,-,0,1</sub> |  | 0.7 | 0.1 | 0.6 | 7.2 |
| Tarris Reed Jr. | 64% | 9.8<br><sub>-,7,-,3,9</sub> | 3.5<br><sub>-,4,-,0,2</sub> |  | 4.4<br><sub>-,7,-,1,3</sub> |  | 0.3<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.4 | 0.9 | 8.2 |
| David Jones Garcia | 58% | 7.5<br><sub>-,-,-,3,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 1.5<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 36.4<br><sub>39,35,34,34,39</sub> | 25.4<br><sub>20,26,33,30,24</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,3,1,1,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>5,5,2,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.3 | 3.1 | 35.2 |
| Dillon Brooks | 98% | 33.3<br><sub>21,34,35,29,37</sub> | 17.6<br><sub>22,18,15,24,11</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>1,8,6,1,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>4,2,0,4,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.2 | 1.6 | 23.8 |
| Miles Bridges | 98% | 32.5<br><sub>37,35,31,31,31</sub> | 15.2<br><sub>24,21,18,18,13</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>10,6,7,13,10</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>2,3,5,5,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,3,4,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.5 | 1.3 | 25.1 |
| Jalen Green | 98% | 31.4<br><sub>25,36,32,24,34</sub> | 16.3<br><sub>2,11,22,6,16</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>2,8,2,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>2,8,2,3,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>0,0,2,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.4 | 2.4 | 23.9 |
| Collin Gillespie | 98% | 24.6<br><sub>33,24,23,24,20</sub> | 8.9<br><sub>16,3,2,6,7</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.7<br><sub>10,2,2,2,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>4,1,0,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.1 | 1.0 | 15.8 |
| Oso Ighodaro | 98% | 23.6<br><sub>21,24,23,24,23</sub> | 6.8<br><sub>2,14,9,2,4</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 5.5<br><sub>9,2,7,5,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>5,2,7,1,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 1.2 | 15.2 |
| Ryan Dunn | 98% | 18.2<br><sub>11,10,18,25,23</sub> | 5.2<br><sub>5,5,2,11,8</sub> |  | 3.8<br><sub>3,3,6,3,5</sub> |  | 1.3<br><sub>1,1,2,3,3</sub> |  | 0.6<br><sub>1,1,0,1,2</sub> |  | 0.7 | 0.4 | 0.6 | 10.3 |
| Khaman Maluach | 98% | 17.6<br><sub>17,13,16,22,18</sub> | 5.9<br><sub>9,5,6,8,8</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 5.5<br><sub>6,2,6,6,10</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>0,0,2,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.9 | 12.0 |
| Luke Kennard | 98% | 17.1<br><sub>12,18,14,21,14</sub> | 6.2<br><sub>9,6,0,12,11</sub> |  | 1.9<br><sub>1,2,0,1,1</sub> |  | 1.7<br><sub>2,1,1,5,2</sub> |  | 0.8<br><sub>1,2,0,3,3</sub> |  | 0.6 | 0.1 | 0.7 | 9.9 |
| Drew Timme | 16% | 7.9 | 2.9 |  | 1.3 |  | 0.7 |  | 0.2 |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Rasheer Fleming | 47% | 7.8<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Pat Spencer | 63% | 7.2<br><sub>-,-,3,2,-</sub> | 2.5<br><sub>-,-,0,0,-</sub> |  | 1.0<br><sub>-,-,0,0,-</sub> |  | 1.1<br><sub>-,-,2,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Duop Reath | 63% | 6.8<br><sub>-,-,7,2,-</sub> | 2.6<br><sub>-,-,7,0,-</sub> |  | 1.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea | 52% | 6.6<br><sub>-,-,3,2,-</sub> | 2.6<br><sub>-,-,3,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Koa Peat | 52% | 5.9<br><sub>-,-,3,2,-</sub> | 2.0<br><sub>-,-,2,0,-</sub> |  | 1.5<br><sub>-,-,1,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.2 | 3.8 |

</details>

<details><summary>if Devin Vassell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker (PHX) | 98% | 36.3<br><sub>39,35,34,34,39</sub> | 25.4<br><sub>20,26,33,30,24</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,3,1,1,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>5,5,2,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.3 | 3.1 | 35.2 |
| Dillon Brooks (PHX) | 98% | 33.3<br><sub>21,34,35,29,37</sub> | 17.6<br><sub>22,18,15,24,11</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>1,8,6,1,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>4,2,0,4,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.2 | 1.6 | 23.7 |
| Miles Bridges (PHX) | 98% | 32.6<br><sub>37,35,31,31,31</sub> | 15.4<br><sub>24,21,18,18,13</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>10,6,7,13,10</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>2,3,5,5,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,3,4,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.5 | 1.3 | 25.4 |
| Jalen Green (PHX) | 98% | 31.5<br><sub>25,36,32,24,34</sub> | 16.5<br><sub>2,11,22,6,16</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>2,8,2,0,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>2,8,2,3,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>0,0,2,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.4 | 2.4 | 24.0 |
| Collin Gillespie (PHX) | 98% | 24.6<br><sub>33,24,23,24,20</sub> | 8.9<br><sub>16,3,2,6,7</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.7<br><sub>10,2,2,2,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>4,1,0,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 1.0 | 15.8 |
| Oso Ighodaro (PHX) | 98% | 23.6<br><sub>21,24,23,24,23</sub> | 6.8<br><sub>2,14,9,2,4</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 5.5<br><sub>9,2,7,5,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>5,2,7,1,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 1.2 | 15.2 |
| Ryan Dunn (PHX) | 98% | 18.2<br><sub>11,10,18,25,23</sub> | 5.2<br><sub>5,5,2,11,8</sub> |  | 3.8<br><sub>3,3,6,3,5</sub> |  | 1.3<br><sub>1,1,2,3,3</sub> |  | 0.6<br><sub>1,1,0,1,2</sub> |  | 0.7 | 0.4 | 0.5 | 10.3 |
| Khaman Maluach (PHX) | 98% | 17.6<br><sub>17,13,16,22,18</sub> | 5.8<br><sub>9,5,6,8,8</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 5.4<br><sub>6,2,6,6,10</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>0,0,2,2,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.9 | 11.9 |
| Luke Kennard (PHX) | 98% | 17.0<br><sub>12,18,14,21,14</sub> | 6.1<br><sub>9,6,0,12,11</sub> |  | 1.9<br><sub>1,2,0,1,1</sub> |  | 1.7<br><sub>2,1,1,5,2</sub> |  | 0.8<br><sub>1,2,0,3,3</sub> |  | 0.6 | 0.1 | 0.7 | 9.7 |
| Rasheer Fleming (PHX) | 47% | 8.0<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.5 |
| Drew Timme (PHX) | 16% | 7.8 | 2.9 |  | 1.3 |  | 0.6 |  | 0.2 |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Pat Spencer (PHX) | 63% | 7.1<br><sub>-,-,3,2,-</sub> | 2.5<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 1.1<br><sub>-,-,2,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Duop Reath (PHX) | 63% | 6.8<br><sub>-,-,7,2,-</sub> | 2.6<br><sub>-,-,7,0,-</sub> |  | 1.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea (PHX) | 52% | 6.5<br><sub>-,-,3,2,-</sub> | 2.5<br><sub>-,-,3,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |
| Koa Peat (PHX) | 52% | 6.0<br><sub>-,-,3,2,-</sub> | 2.0<br><sub>-,-,2,0,-</sub> |  | 1.5<br><sub>-,-,1,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.2 | 3.9 |
| Victor Wembanyama (SAS) | 98% | 31.7<br><sub>34,24,34,26,24</sub> | 26.4<br><sub>43,12,52,30,29</sub> | 27.5 · –<br><sub>o 48% · u 52%</sub> | 11.4<br><sub>7,11,24,14,7</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>4,5,2,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>3,0,1,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 3.3 | 2.6 | 40.9 |
| Dylan Harper (SAS) | 98% | 31.4<br><sub>39,27,36,28,28</sub> | 16.7<br><sub>25,17,21,19,13</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>7,7,5,2,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>6,8,0,3,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1 | 0.3 | 2.0 | 25.9 |
| Devin Vassell (SAS) | 100% | 30.9<br><sub>34,25,36,27,21</sub> | 12.1<br><sub>9,11,2,19,15</sub> | 10.5 · – | 4.1<br><sub>5,2,7,2,2</sub> | 3.5 | 2.4<br><sub>2,1,4,2,3</sub> | 2.5 | 1.9<br><sub>0,0,0,5,2</sub> | 1.5 | 1.2 | 0.4 | 1.1 | 18.6 |
| Stephon Castle (SAS) | 98% | 30.4<br><sub>22,26,35,28,24</sub> | 16.5<br><sub>0,16,17,19,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,5,10,3,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 5.4<br><sub>4,4,3,7,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>0,2,2,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.3 | 2.9 | 27.2 |
| De'Aaron Fox (SAS) | 98% | 30.1<br><sub>35,22,33,26,22</sub> | 14.7<br><sub>22,12,10,9,8</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>8,2,3,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>7,3,4,4,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>0,1,0,0,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.2 | 0.4 | 2.2 | 23.4 |
| Julian Champagnie (SAS) | 98% | 24.0<br><sub>27,22,21,22,21</sub> | 8.1<br><sub>12,8,0,8,14</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>3,6,4,7,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>1,0,3,2,0</sub> |  | 1.5<br><sub>3,2,0,2,4</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 0.8 | 13.6 |
| Keldon Johnson (SAS) | 98% | 22.9<br><sub>24,27,19,27,27</sub> | 9.8<br><sub>2,15,4,3,10</sub> |  | 5.0<br><sub>6,7,5,6,7</sub> |  | 1.5<br><sub>0,1,2,6,4</sub> |  | 0.7<br><sub>0,1,0,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 16.2 |
| Luke Kornet (SAS) | 98% | 14.9<br><sub>14,17,14,18,15</sub> | 3.6<br><sub>2,8,2,2,6</sub> |  | 4.2<br><sub>8,5,1,6,4</sub> |  | 0.9<br><sub>0,2,2,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.6 | 0.6 | 8.8 |
| Harrison Barnes (SAS) | 80% | 14.6<br><sub>-,21,13,19,19</sub> | 4.7<br><sub>-,13,4,13,5</sub> |  | 1.6<br><sub>-,0,2,1,3</sub> |  | 0.7<br><sub>-,0,0,0,0</sub> |  | 0.6<br><sub>-,3,1,2,1</sub> |  | 0.4 | 0.1 | 0.5 | 7.0 |
| Carter Bryant (SAS) | 86% | 11.9<br><sub>11,14,-,3,17</sub> | 3.9<br><sub>6,3,-,0,6</sub> |  | 1.9<br><sub>0,0,-,0,4</sub> |  | 0.7<br><sub>0,0,-,0,1</sub> |  | 0.4<br><sub>2,1,-,0,2</sub> |  | 0.3 | 0.3 | 0.5 | 6.5 |
| Jordan McLaughlin (SAS) | 63% | 9.5<br><sub>-,8,-,8,12</sub> | 3.1<br><sub>-,0,-,2,3</sub> |  | 1.2<br><sub>-,1,-,2,0</sub> |  | 1.3<br><sub>-,3,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,1</sub> |  | 0.6 | 0.1 | 0.5 | 5.7 |
| Tarris Reed Jr. (SAS) | 64% | 8.0<br><sub>-,7,-,3,9</sub> | 3.1<br><sub>-,4,-,0,2</sub> |  | 3.6<br><sub>-,7,-,1,3</sub> |  | 0.3<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.3 | 0.7 | 7.0 |
| David Jones Garcia (SAS) | 58% | 6.0<br><sub>-,-,-,3,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |

</details>


### NOP @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Will Richard (GSW), Yves Missi (NOP)

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 31.8<br><sub>29,40,-,34,30</sub> | 15.8<br><sub>15,18,-,10,26</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>5,5,-,4,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.4<br><sub>5,5,-,5,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.4<br><sub>1,3,-,1,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 1.6 | 24.0 |
| Dejounte Murray | 98% | 31.4<br><sub>-,-,45,35,28</sub> | 15.2<br><sub>-,-,20,7,6</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>-,-,8,2,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 5.7<br><sub>-,-,4,4,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>-,-,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.9 | 0.3 | 3.0 | 26.1 |
| Zion Williamson | 98% | 30.7<br><sub>30,35,38,36,31</sub> | 18.6<br><sub>15,25,23,13,25</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>6,11,4,8,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>4,4,2,4,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.3 | 0.5 | 2.2 | 27.1 |
| Jeremiah Fears | 98% | 29.2<br><sub>31,38,34,36,29</sub> | 15.8<br><sub>20,12,19,24,25</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,4,6,5,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>7,7,2,5,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,0,1,0,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 2.6 | 24.3 |
| Saddiq Bey | 98% | 26.3<br><sub>26,36,29,31,26</sub> | 13.4<br><sub>25,18,22,17,13</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,5,4,5,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>1,1,3,4,3</sub> |  | 1.7<br><sub>1,2,2,3,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.1 | 1.1 | 19.6 |
| Herbert Jones | 98% | 20.1<br><sub>25,28,37,14,20</sub> | 5.9<br><sub>11,9,2,0,4</sub> |  | 2.3<br><sub>3,4,5,4,0</sub> |  | 1.4<br><sub>2,3,1,0,1</sub> |  | 0.7<br><sub>1,3,0,0,0</sub> |  | 1.1 | 0.3 | 1.0 | 9.6 |
| Derik Queen | 98% | 19.9<br><sub>23,24,27,10,21</sub> | 9.4<br><sub>8,20,20,6,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>8,7,9,4,5</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.7<br><sub>4,5,6,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.8 | 0.6 | 2.1 | 18.0 |
| Karlo Matkovic | 96% | 16.4<br><sub>18,29,21,18,19</sub> | 6.5<br><sub>8,25,5,18,3</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>10,6,4,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.9<br><sub>1,1,2,1,2</sub> |  | 0.7<br><sub>2,5,1,4,1</sub> |  | 0.5 | 0.7 | 0.8 | 11.3 |
| Trendon Watford | 80% | 14.2<br><sub>18,16,20,19,17</sub> | 5.8<br><sub>7,4,7,12,5</sub> |  | 2.7<br><sub>4,4,3,6,3</sub> |  | 1.3<br><sub>0,1,2,1,0</sub> |  | 0.2<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.3 | 1.0 | 9.8 |
| Bennedict Mathurin | 98% | 13.5<br><sub>19,13,15,7,9</sub> | 6.4<br><sub>7,4,2,2,6</sub> |  | 2.3<br><sub>1,0,5,0,0</sub> |  | 1.1<br><sub>2,0,1,0,1</sub> |  | 0.5<br><sub>1,0,0,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 9.9 |
| Jordan Poole | 52% | 12.8<br><sub>-,-,-,-,-</sub> | 6.1<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.1 | 9.1 |
| DeAndre Jordan | 26% | 8.8<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 3.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.4 | 6.0 |
| Malik Dia | 5% | 8.6 | 3.7 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jaron Pierre Jr. | 5% | 8.3 | 3.4 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.7 |
| Bryce McGowens | 58% | 7.3<br><sub>15,6,-,-,3</sub> | 2.4<br><sub>3,0,-,-,0</sub> |  | 0.9<br><sub>0,1,-,-,0</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Julian Reese | 48% | 5.8<br><sub>3,-,-,-,3</sub> | 2.3<br><sub>2,-,-,-,0</sub> |  | 1.0<br><sub>1,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 3.8 |
| AJ Johnson | 47% | 5.7<br><sub>3,-,-,-,3</sub> | 2.5<br><sub>0,-,-,-,2</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 3.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 91% | 33.5<br><sub>33,37,33,32,39</sub> | 16.4<br><sub>21,17,20,9,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,8,3,6,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>6,8,2,3,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>4,2,3,2,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.2 | 1.6 | 26.0 |
| Yaxel Lendeborg | 98% | 33.0<br><sub>24,34,29,30,37</sub> | 20.7<br><sub>6,37,16,17,23</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>1,4,5,8,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>0,6,5,6,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>1,6,2,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.9 | 3.1 | 32.3 |
| Stephen Curry | 98% | 32.1<br><sub>31,-,33,28,36</sub> | 26.7<br><sub>31,-,34,29,41</sub> | 28.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,-,6,1,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 5.3<br><sub>6,-,7,4,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>8,-,5,6,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.4 | 2.5 | 35.8 |
| Draymond Green | 91% | 28.1<br><sub>32,-,17,27,34</sub> | 6.9<br><sub>2,-,4,2,2</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>9,-,2,11,13</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.8<br><sub>0,-,0,0,0</sub> |  | 1.1 | 0.8 | 2.5 | 19.2 |
| Georges Niang | 97% | 20.0<br><sub>19,21,22,22,25</sub> | 8.1<br><sub>11,3,13,13,11</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>5,1,4,4,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,2,3,3,1</sub> |  | 1.4<br><sub>3,1,1,2,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.5 | 0.2 | 0.9 | 12.3 |
| De'Anthony Melton | 98% | 19.5<br><sub>21,28,28,17,17</sub> | 9.0<br><sub>16,21,2,5,4</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>5,6,7,6,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>3,3,2,2,1</sub> |  | 1.3<br><sub>4,6,0,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 1.2 | 14.2 |
| Brandon Williams | 86% | 17.4<br><sub>17,25,-,21,17</sub> | 10.2<br><sub>9,17,-,10,9</sub> |  | 2.3<br><sub>2,3,-,1,0</sub> |  | 2.9<br><sub>1,3,-,4,2</sub> |  | 0.6<br><sub>0,2,-,0,0</sub> |  | 0.8 | 0.3 | 1.5 | 15.4 |
| Al Horford | 98% | 15.7<br><sub>17,22,-,18,13</sub> | 5.6<br><sub>3,9,-,8,2</sub> |  | 3.7<br><sub>2,5,-,5,5</sub> |  | 1.5<br><sub>0,2,-,1,4</sub> |  | 0.8<br><sub>1,3,-,2,0</sub> |  | 0.4 | 0.7 | 0.5 | 10.8 |
| Gui Santos | 82% | 14.7<br><sub>16,9,-,-,12</sub> | 6.2<br><sub>2,4,-,-,3</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>5,3,-,-,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,1,-,-,0</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 10.7 |
| Gary Payton II | 98% | 13.9<br><sub>8,15,20,10,13</sub> | 6.7<br><sub>2,5,2,9,4</sub> |  | 2.5<br><sub>4,2,2,0,0</sub> |  | 1.1<br><sub>0,2,1,0,0</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.8 | 0.2 | 0.6 | 10.4 |
| Charles Bassey | 96% | 12.5<br><sub>9,20,23,14,11</sub> | 6.3<br><sub>6,6,19,8,8</sub> |  | 5.3<br><sub>4,10,8,7,4</sub> |  | 0.6<br><sub>1,2,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.7 | 12.2 |
| Graham Ike | 88% | 6.8<br><sub>-,6,7,1,-</sub> | 3.0<br><sub>-,2,0,0,-</sub> |  | 1.7<br><sub>-,2,0,1,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| LJ Cryer | 58% | 6.6<br><sub>-,2,1,1,-</sub> | 3.2<br><sub>-,0,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.0 | 0.4 | 4.4 |
| Malevy Leons | 48% | 6.1<br><sub>-,-,-,1,-</sub> | 2.0<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.3 | 3.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-09/`._
