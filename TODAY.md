# NBA model · Mon 09 Nov 2026 (US date)

Updated **Tue 10 Nov, 09:27 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-09/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| NOP to win | NOP @ GSW | draftkings | 5.26 | 4.10 | 4.85 | 20.6% | 24.4% | 24.4% | +28.4% | +8.5% | 1.7% |
| Kevin Durant PRA over 44.5 (45+) | DEN @ HOU | draftkings | 13.00 | 12.08 | 6.47 | 15.5% | 7.2% | 8.3% | +7.7% | +101.1% | 0.2% |
| Pascal Siakam AST over 7.5 (8+) | IND @ DAL | draftkings | 20.80 | 19.38 | 10.48 | 9.5% | 4.5% | 5.2% | +7.3% | +98.5% | 0.1% |
| Kevin Durant PA over 39.5 (40+) | DEN @ HOU | draftkings | 16.80 | 15.70 | 8.58 | 11.7% | 5.6% | 6.4% | +7.0% | +95.8% | 0.1% |
| Derik Queen PA over 24.5 (25+) | NOP @ GSW | draftkings | 10.80 | 10.12 | 5.58 | 17.9% | 8.6% | 9.9% | +6.7% | +93.7% | 0.2% |
| Kevin Durant PRA over 49.5 (50+) | DEN @ HOU | draftkings | 24.00 | 22.57 | 12.58 | 8.0% | 3.9% | 4.4% | +6.3% | +90.8% | 0.1% |
| WAS to win | WAS @ DET | unibet | 5.30 | 5.00 | 3.55 | 28.2% | 20.0% | 20.0% | +6.0% | +49.4% | 0.4% |
| Derik Queen PA over 29.5 (30+) | NOP @ GSW | draftkings | 25.00 | 23.75 | 13.68 | 7.3% | 3.7% | 4.2% | +5.2% | +82.7% | 0.1% |
| Kevin Durant PTS over 34.5 (35+) | DEN @ HOU | draftkings | 16.20 | 15.41 | 8.92 | 11.2% | 5.8% | 6.5% | +5.1% | +81.7% | 0.1% |
| Kevin Durant PR over 39.5 (40+) | DEN @ HOU | draftkings | 12.00 | 11.43 | 6.62 | 15.1% | 7.8% | 8.8% | +5.1% | +81.3% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL to win | LAL @ ATL | draftkings | 2.02 | Austin Reaves | 39.1% | 44.3% | +5.0% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| HOU to win | DEN @ HOU | draftkings | 1.58 | 1.36 | 1.72 | 58.0% | 73.6% | 73.6% | +16.2% | -8.5% | 2.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ ATL | Tue 10 Nov 11:00 | 113.4–117.2 | LAL 39% | 2.56 / 1.64 | ATL -4.5 | 230.5 | ATL -1.5 covers 58%; o236.5 37% |
| CLE @ CHA | Tue 10 Nov 11:00 | 111.1–103.9 | CLE 70% | 1.43 / 3.32 | CHA +7.5 | 214.5 | CHA +8.5 covers 54%; o215.5 48% |
| WAS @ DET | Tue 10 Nov 11:00 | 108.0–117.4 | WAS 25% | 3.97 / 1.34 | DET -9.5 | 225.5 | DET -10.5 covers 47%; o219.5 62% |
| MEM @ TOR | Tue 10 Nov 11:30 | 115.2–117.0 | MEM 45% | 2.23 / 1.81 | TOR -2.5 | 232.5 | TOR -2.5 covers 49%; o228.5 58% |
| IND @ DAL | Tue 10 Nov 12:00 | 111.4–117.0 | IND 34% | 2.91 / 1.52 | DAL -5.5 | 228.5 | DAL -4.5 covers 54%; o226.5 54% |
| DEN @ HOU | Tue 10 Nov 12:30 | 112.0–114.8 | DEN 42% | 2.38 / 1.72 | HOU -3.5 | 226.5 | HOU -4.5 covers 46%; o223.5 57% |
| SAS @ PHX | Tue 10 Nov 13:00 | 117.4–109.1 | SAS 72% | 1.38 / 3.64 | PHX +8.5 | 226.5 | PHX +8.5 covers 50%; o226.5 50% |
| NOP @ GSW | Tue 10 Nov 14:00 | 112.6–123.8 | NOP 22% | 4.64 / 1.27 | GSW -11.5 | 236.5 | GSW -11.5 covers 49%; o229.5 64% |

### LAL @ ATL
Out: RayJ Dennis (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Asa Newell (ATL), Jalen Wilson (ATL), Quentin Grimes (LAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.4–117.2 | LAL 39% | 2.56 / 1.64 | ATL -4.5 | 230.5 | ATL -1.5 covers 58%; o236.5 37% |
| Expected (weighted by chance each plays) | 114.2–117.3 | LAL 41% | 2.42 / 1.71 | ATL -3.5 | 231.5 | ATL -1.5 covers 56%; o236.5 39% |
| if Austin Reaves plays | 115.0–117.0 | LAL 44% | 2.26 / 1.80 | ATL -2.5 | 231.5 | ATL -1.5 covers 53%; o236.5 40% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Austin Reaves (LAL) | Questionable | 55% | 37.1 | 22.3 | 4.3 | 5.0 | 2.2 | 1.1 | 0.5 | 3.5 | 31.7 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 37.0<br><sub>35,36,35,38,-</sub> | 37.6<br><sub>45,42,40,53,-</sub> | 36.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>15,7,9,5,-</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 8.1<br><sub>6,13,7,5,-</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>8,6,6,5,-</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.6 | 4.9 | 53.3 |
| Walker Kessler | 98% | 32.6<br><sub>31,32,29,37,29</sub> | 12.6<br><sub>16,15,15,16,12</sub> | 14.5 · –<br><sub>o 44% · u 56%</sub> | 12.9<br><sub>15,15,8,12,16</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>1,2,0,2,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.2 | 2.1 | 27.5 |
| Matisse Thybulle | 98% | 28.2<br><sub>25,19,23,24,28</sub> | 8.2<br><sub>6,6,3,2,4</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>2,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,2,2,0,0</sub> |  | 1.3<br><sub>2,2,1,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.3 | 0.8 | 1.1 | 12.3 |
| Jake LaRavia | 97% | 27.8<br><sub>25,26,21,25,29</sub> | 7.5<br><sub>8,7,9,7,5</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>2,4,2,8,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>4,2,2,3,2</sub> |  | 0.8<br><sub>2,1,2,2,0</sub> |  | 1.4 | 0.7 | 1.4 | 13.7 |
| Ziaire Williams | 98% | 25.9<br><sub>-,15,23,20,21</sub> | 10.8<br><sub>-,9,10,8,17</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>-,2,4,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>-,2,1,1,0</sub> |  | 1.4<br><sub>-,3,1,2,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.4 | 1.1 | 15.6 |
| Collin Sexton | 98% | 25.6<br><sub>19,16,16,11,24</sub> | 15.2<br><sub>14,6,10,0,17</sub> |  | 2.7<br><sub>3,1,3,0,2</sub> |  | 2.9<br><sub>3,5,1,1,2</sub> |  | 1.5<br><sub>1,0,1,0,0</sub> |  | 1.1 | 0.2 | 2.1 | 20.8 |
| Sandro Mamukelashvili | 98% | 23.7<br><sub>24,28,19,20,18</sub> | 9.6<br><sub>11,13,2,7,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>1,3,6,3,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>1,4,1,1,0</sub> |  | 1.1<br><sub>2,2,0,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 0.5 | 1.0 | 16.4 |
| Jarred Vanderbilt | 67% | 15.2<br><sub>12,6,7,-,14</sub> | 3.3<br><sub>4,2,0,-,2</sub> |  | 4.3<br><sub>3,1,1,-,10</sub> |  | 1.2<br><sub>1,0,0,-,3</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.7 | 0.3 | 0.8 | 8.8 |
| Lawson Lovering | 52% | 13.3<br><sub>-,1,1,-,-</sub> | 3.9<br><sub>-,0,0,-,-</sub> |  | 3.7<br><sub>-,1,0,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.6 | 0.3 | 0.7 | 8.3 |
| Adou Thiero | 88% | 12.0<br><sub>-,-,-,7,8</sub> | 3.9<br><sub>-,-,-,4,2</sub> |  | 3.1<br><sub>-,-,-,4,2</sub> |  | 0.7<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 7.8 |
| Jaden Hardy | 52% | 11.4<br><sub>1,1,1,-,-</sub> | 5.6<br><sub>1,2,0,-,-</sub> |  | 1.0<br><sub>0,0,0,-,-</sub> |  | 0.8<br><sub>0,0,1,-,-</sub> |  | 0.7<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.8 | 7.4 |
| Chris Manon | 58% | 10.1<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 5.3 |
| Kevon Looney | 30% | 9.4<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 3.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 6.1 |
| Bronny James | 58% | 8.6<br><sub>2,1,1,-,-</sub> | 2.9<br><sub>0,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.7<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 3.9 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Cameron Carr | 64% | 8.5<br><sub>1,1,1,-,-</sub> | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.8<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 1.5 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 34.1<br><sub>28,-,-,-,36</sub> | 20.1<br><sub>13,-,-,-,30</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 8.7<br><sub>7,-,-,-,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>4,-,-,-,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,-,-,-,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 3.2 | 35.8 |
| Nickeil Alexander-Walker | 98% | 31.7<br><sub>29,31,32,33,31</sub> | 20.3<br><sub>12,34,26,28,20</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,4,4,2,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.8<br><sub>1,4,2,2,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>0,9,6,4,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 2.3 | 26.0 |
| Dyson Daniels | 98% | 30.9<br><sub>27,31,34,35,31</sub> | 11.0<br><sub>8,6,8,13,9</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>4,9,16,9,10</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 5.6<br><sub>3,4,8,12,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.4 | 0.4 | 1.7 | 23.2 |
| Onyeka Okongwu | 98% | 30.2<br><sub>28,33,31,33,30</sub> | 13.3<br><sub>6,13,14,22,16</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>10,10,16,10,2</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>1,3,4,1,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.8 | 1.3 | 23.0 |
| CJ McCollum | 98% | 24.8<br><sub>24,32,25,23,21</sub> | 14.2<br><sub>14,13,15,4,9</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,9,5,3,4</sub> |  | 3.3<br><sub>2,12,5,4,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,2,2,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.4 | 1.9 | 20.2 |
| Aaron Wiggins | 98% | 23.8<br><sub>23,24,29,29,26</sub> | 11.5<br><sub>10,7,15,19,20</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,3,4,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,2,2,3,6</sub> |  | 1.8<br><sub>2,1,3,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.2 | 16.4 |
| Luguentz Dort | 98% | 23.1<br><sub>29,31,31,32,20</sub> | 7.9<br><sub>11,14,6,25,3</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>3,2,3,7,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,3,4,1</sub> |  | 1.3<br><sub>1,4,2,5,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 0.7 | 12.0 |
| Kingston Flemings | 88% | 21.7<br><sub>25,-,23,25,27</sub> | 8.5<br><sub>12,-,14,11,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,-,3,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,-,4,6,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 0.7<br><sub>1,-,2,1,0</sub> |  | 0.7 | 0.3 | 1.9 | 14.8 |
| Zuby Ejiofor | 71% | 13.9<br><sub>-,15,17,15,18</sub> | 5.4<br><sub>-,3,11,10,7</sub> |  | 3.3<br><sub>-,5,3,5,6</sub> |  | 1.4<br><sub>-,2,2,5,0</sub> |  | 0.4<br><sub>-,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.2 |
| Corey Kispert | 63% | 9.6<br><sub>5,18,8,16,-</sub> | 4.9<br><sub>0,14,9,7,-</sub> |  | 1.1<br><sub>0,1,0,2,-</sub> |  | 0.7<br><sub>1,0,1,1,-</sub> |  | 0.6<br><sub>0,4,1,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 6.7 |
| Jock Landale | 72% | 9.4<br><sub>1,-,-,-,-</sub> | 4.2<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 7.4 |
| Dorian Finney-Smith | 35% | 6.1<br><sub>3,-,-,-,-</sub> | 1.7<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.1 |

</details>

<details><summary>if Austin Reaves plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 34.0<br><sub>28,-,-,-,36</sub> | 20.0<br><sub>13,-,-,-,30</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>7,-,-,-,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>4,-,-,-,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,-,-,-,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 3.1 | 35.6 |
| Nickeil Alexander-Walker (ATL) | 98% | 31.7<br><sub>29,31,32,33,31</sub> | 20.2<br><sub>12,34,26,28,20</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,4,4,2,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.8<br><sub>1,4,2,2,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>0,9,6,4,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 2.3 | 25.9 |
| Dyson Daniels (ATL) | 98% | 30.9<br><sub>27,31,34,35,31</sub> | 10.9<br><sub>8,6,8,13,9</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>4,9,16,9,10</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 5.6<br><sub>3,4,8,12,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 2.4 | 0.4 | 1.7 | 23.2 |
| Onyeka Okongwu (ATL) | 98% | 30.2<br><sub>28,33,31,33,30</sub> | 13.3<br><sub>6,13,14,22,16</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>10,10,16,10,2</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>1,3,4,1,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.8 | 1.3 | 23.0 |
| CJ McCollum (ATL) | 98% | 24.9<br><sub>24,32,25,23,21</sub> | 14.2<br><sub>14,13,15,4,9</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,9,5,3,4</sub> |  | 3.4<br><sub>2,12,5,4,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>2,2,2,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.4 | 1.9 | 20.2 |
| Aaron Wiggins (ATL) | 98% | 23.9<br><sub>23,24,29,29,26</sub> | 11.6<br><sub>10,7,15,19,20</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,3,4,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,2,2,3,6</sub> |  | 1.8<br><sub>2,1,3,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.2 | 16.5 |
| Luguentz Dort (ATL) | 98% | 23.1<br><sub>29,31,31,32,20</sub> | 8.0<br><sub>11,14,6,25,3</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,2,3,7,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,0,3,4,1</sub> |  | 1.3<br><sub>1,4,2,5,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 0.7 | 12.1 |
| Kingston Flemings (ATL) | 88% | 21.8<br><sub>25,-,23,25,27</sub> | 8.6<br><sub>12,-,14,11,10</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,-,3,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,-,4,6,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 0.7<br><sub>1,-,2,1,0</sub> |  | 0.7 | 0.3 | 1.9 | 14.9 |
| Zuby Ejiofor (ATL) | 71% | 13.8<br><sub>-,15,17,15,18</sub> | 5.3<br><sub>-,3,11,10,7</sub> |  | 3.3<br><sub>-,5,3,5,6</sub> |  | 1.4<br><sub>-,2,2,5,0</sub> |  | 0.4<br><sub>-,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 10.1 |
| Corey Kispert (ATL) | 63% | 9.6<br><sub>5,18,8,16,-</sub> | 4.9<br><sub>0,14,9,7,-</sub> |  | 1.1<br><sub>0,1,0,2,-</sub> |  | 0.7<br><sub>1,0,1,1,-</sub> |  | 0.6<br><sub>0,4,1,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 6.8 |
| Jock Landale (ATL) | 72% | 9.4<br><sub>1,-,-,-,-</sub> | 4.2<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 7.3 |
| Dorian Finney-Smith (ATL) | 35% | 6.1<br><sub>3,-,-,-,-</sub> | 1.7<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.0 |
| Austin Reaves (LAL) | 100% | 37.1<br><sub>39,34,37,38,37</sub> | 22.3<br><sub>19,27,21,25,43</sub> | 21.5 · – | 4.3<br><sub>3,2,3,3,5</sub> | 3.5 | 5.0<br><sub>4,5,4,2,4</sub> | 4.5 | 2.2<br><sub>2,4,1,1,4</sub> | 1.5 | 1.1 | 0.5 | 3.5 | 31.7 |
| Luka Doncic (LAL) | 98% | 36.7<br><sub>35,36,35,38,-</sub> | 36.3<br><sub>45,42,40,53,-</sub> | 36.5 · –<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>15,7,9,5,-</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>6,13,7,5,-</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>8,6,6,5,-</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.5 | 4.3 | 51.5 |
| Walker Kessler (LAL) | 98% | 30.5<br><sub>31,32,29,37,29</sub> | 10.7<br><sub>16,15,15,16,12</sub> | 14.5 · –<br><sub>o 44% · u 56%</sub> | 12.0<br><sub>15,15,8,12,16</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>1,2,0,2,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.9 | 2.1 | 1.7 | 24.4 |
| Jake LaRavia (LAL) | 97% | 24.1<br><sub>25,26,21,25,29</sub> | 6.2<br><sub>8,7,9,7,5</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>2,4,2,8,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>4,2,2,3,2</sub> |  | 0.7<br><sub>2,1,2,2,0</sub> |  | 1.2 | 0.6 | 1.2 | 11.5 |
| Matisse Thybulle (LAL) | 98% | 24.0<br><sub>25,19,23,24,28</sub> | 6.3<br><sub>6,6,3,2,4</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,1,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>3,2,2,0,0</sub> |  | 0.9<br><sub>2,2,1,0,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.9 | 0.8 | 0.9 | 9.7 |
| Ziaire Williams (LAL) | 98% | 21.7<br><sub>-,15,23,20,21</sub> | 8.0<br><sub>-,9,10,8,17</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>-,2,4,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>-,2,1,1,0</sub> |  | 1.0<br><sub>-,3,1,2,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.3 | 0.8 | 11.9 |
| Sandro Mamukelashvili (LAL) | 98% | 20.2<br><sub>24,28,19,20,18</sub> | 7.7<br><sub>11,13,2,7,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>1,3,6,3,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,4,1,1,0</sub> |  | 0.8<br><sub>2,2,0,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.7 | 0.5 | 0.8 | 13.4 |
| Collin Sexton (LAL) | 98% | 19.2<br><sub>19,16,16,11,24</sub> | 10.7<br><sub>14,6,10,0,17</sub> |  | 2.1<br><sub>3,1,3,0,2</sub> |  | 2.0<br><sub>3,5,1,1,2</sub> |  | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.8 | 0.2 | 1.6 | 14.7 |
| Jarred Vanderbilt (LAL) | 67% | 11.8<br><sub>12,6,7,-,14</sub> | 2.6<br><sub>4,2,0,-,2</sub> |  | 3.4<br><sub>3,1,1,-,10</sub> |  | 0.9<br><sub>1,0,0,-,3</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 6.8 |
| AK Okereke (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Adou Thiero (LAL) | 88% | 7.7<br><sub>-,-,-,7,8</sub> | 2.5<br><sub>-,-,-,4,2</sub> |  | 2.1<br><sub>-,-,-,4,2</sub> |  | 0.5<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.1 |
| Lawson Lovering (LAL) | 52% | 7.5<br><sub>-,1,1,-,-</sub> | 2.2<br><sub>-,0,0,-,-</sub> |  | 2.0<br><sub>-,1,0,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |
| Kevon Looney (LAL) | 30% | 6.8<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.7 |
| Jaden Hardy (LAL) | 52% | 6.6<br><sub>1,1,1,-,-</sub> | 3.4<br><sub>1,2,0,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,1,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |
| Chris Manon (LAL) | 58% | 5.8<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.3 |
| Bronny James (LAL) | 58% | 5.6<br><sub>2,1,1,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.9 |
| Cameron Carr (LAL) | 64% | 5.5<br><sub>1,1,1,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.0 |

</details>


### CLE @ CHA
Out: Moussa Diabate (CHA), Kon Knueppel (CHA), Brandon Miller (CHA), Dennis Schroder (CHA), Grant Williams (CHA), Sam Merrill (CLE), Jaylon Tyson (CLE)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.1–103.9 | CLE 70% | 1.43 / 3.32 | CHA +7.5 | 214.5 | CHA +8.5 covers 54%; o215.5 48% |
| Expected (weighted by chance each plays) | 112.0–104.7 | CLE 71% | 1.42 / 3.40 | CHA +7.5 | 216.5 | CHA +8.5 covers 53%; o215.5 52% |
| if Jarrett Allen plays | 112.8–105.2 | CLE 71% | 1.41 / 3.45 | CHA +7.5 | 217.5 | CHA +8.5 covers 52%; o215.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jarrett Allen (CLE) | Questionable | 55% | 25.9 | 11.8 | 7.0 | 1.4 | 0.1 | 0.9 | 1.2 | 1.2 | 20.1 | full tables below |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 98% | 36.7<br><sub>24,36,33,33,37</sub> | 26.4<br><sub>15,17,27,23,37</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>4,5,3,7,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 5.2<br><sub>3,11,6,8,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>2,4,5,1,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.3 | 2.7 | 36.7 |
| James Harden | 98% | 36.5<br><sub>26,33,35,30,34</sub> | 18.6<br><sub>13,14,19,17,7</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>6,4,9,6,2</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>7,6,6,3,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>3,3,3,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.5 | 3.1 | 29.8 |
| Evan Mobley | 98% | 35.3<br><sub>25,33,33,32,33</sub> | 16.8<br><sub>27,16,16,22,12</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>5,7,10,6,9</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>3,4,3,4,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>3,1,1,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.5 | 1.8 | 28.8 |
| Peyton Watson | 98% | 31.5<br><sub>22,-,-,28,29</sub> | 13.7<br><sub>5,-,-,13,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>2,-,-,9,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>6,-,-,2,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4<br><sub>1,-,-,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.2 | 1.6 | 21.3 |
| Meleek Thomas | 88% | 26.7<br><sub>23,26,18,27,24</sub> | 10.4<br><sub>13,17,9,12,9</sub> |  | 3.0<br><sub>1,5,1,1,4</sub> |  | 1.4<br><sub>2,1,0,3,0</sub> |  | 1.7<br><sub>3,3,3,2,3</sub> |  | 0.9 | 0.2 | 1.1 | 14.8 |
| Tyrese Proctor | 91% | 23.2<br><sub>18,19,22,19,23</sub> | 8.2<br><sub>9,10,11,3,7</sub> |  | 3.4<br><sub>4,4,1,6,3</sub> |  | 2.7<br><sub>5,2,0,3,3</sub> |  | 1.2<br><sub>3,2,2,0,2</sub> |  | 0.9 | 0.1 | 1.0 | 14.2 |
| Mario Hezonja | 98% | 22.9<br><sub>20,27,23,27,19</sub> | 9.0<br><sub>8,12,12,15,0</sub> |  | 5.9<br><sub>11,8,8,10,5</sub> |  | 1.6<br><sub>4,3,1,1,1</sub> |  | 1.3<br><sub>1,3,2,2,0</sub> |  | 0.7 | 0.2 | 0.9 | 16.4 |
| Thomas Bryant | 71% | 16.2<br><sub>11,5,13,16,15</sub> | 7.2<br><sub>11,4,8,13,5</sub> |  | 3.7<br><sub>2,0,0,6,3</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>3,0,1,1,1</sub> |  | 0.4 | 0.5 | 0.7 | 11.6 |
| Craig Porter Jr. | 88% | 15.3<br><sub>16,8,14,3,15</sub> | 3.1<br><sub>2,0,0,0,0</sub> |  | 2.5<br><sub>2,4,1,0,1</sub> |  | 2.2<br><sub>4,1,1,0,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.4 | 0.7 | 7.8 |
| Riley Minix | 48% | 11.4<br><sub>6,-,-,-,10</sub> | 4.1<br><sub>0,-,-,-,8</sub> |  | 1.8<br><sub>3,-,-,-,3</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,2</sub> |  | 0.3 | 0.2 | 0.5 | 6.5 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Norchad Omier | 52% | 7.4<br><sub>-,-,-,3,-</sub> | 2.1<br><sub>-,-,-,0,-</sub> |  | 1.8<br><sub>-,-,-,2,-</sub> |  | 0.7<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 98% | 33.9<br><sub>31,36,27,36,26</sub> | 19.7<br><sub>12,14,13,28,14</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 8.7<br><sub>11,5,6,9,6</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>1,2,2,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>2,0,2,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.9 | 2.8 | 31.1 |
| Grayson Allen | 98% | 31.5<br><sub>21,30,19,27,22</sub> | 17.3<br><sub>5,27,11,22,0</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>3,4,1,2,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>2,3,0,4,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>1,7,3,5,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 2.3 | 24.8 |
| Sion James | 98% | 30.0<br><sub>29,18,21,31,21</sub> | 8.5<br><sub>6,4,11,10,11</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>5,2,4,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>4,1,3,1,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 1.4 | 16.4 |
| Royce O'Neale | 98% | 27.5<br><sub>17,23,18,18,26</sub> | 8.4<br><sub>7,8,2,0,7</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,0,2,2</sub> |  | 1.6<br><sub>2,1,0,0,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.4 | 1.1 | 15.2 |
| Coby White | 98% | 26.9<br><sub>-,-,16,18,16</sub> | 18.0<br><sub>-,-,7,4,7</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>-,-,0,5,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>-,-,3,2,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>-,-,1,0,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.2 | 2.7 | 25.4 |
| Tidjane Salaun | 93% | 26.2<br><sub>9,12,19,10,23</sub> | 10.1<br><sub>6,5,1,9,13</sub> |  | 6.0<br><sub>2,2,7,1,4</sub> |  | 1.4<br><sub>0,0,0,0,0</sub> |  | 1.6<br><sub>2,1,0,3,2</sub> |  | 0.8 | 0.3 | 1.2 | 17.5 |
| Christian Anderson | 80% | 25.4<br><sub>14,8,9,-,25</sub> | 10.2<br><sub>4,2,8,-,4</sub> |  | 3.5<br><sub>3,0,2,-,3</sub> |  | 3.5<br><sub>3,0,2,-,5</sub> |  | 1.4<br><sub>0,0,1,-,0</sub> |  | 0.8 | 0.5 | 1.9 | 17.1 |
| Hannes Steinbach | 52% | 23.9<br><sub>2,-,9,-,27</sub> | 6.0<br><sub>0,-,2,-,4</sub> |  | 6.2<br><sub>0,-,2,-,11</sub> |  | 1.0<br><sub>0,-,1,-,1</sub> |  | 0.3<br><sub>0,-,0,-,0</sub> |  | 0.6 | 0.9 | 1.0 | 13.2 |
| Ryan Kalkbrenner | 98% | 23.8<br><sub>15,19,16,19,21</sub> | 7.1<br><sub>2,6,4,6,4</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>4,3,6,4,5</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>0,4,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.2 | 14.9 |
| Liam McNeeley | 58% | 21.4<br><sub>3,-,9,-,19</sub> | 9.0<br><sub>0,-,3,-,8</sub> |  | 3.9<br><sub>2,-,0,-,2</sub> |  | 1.7<br><sub>0,-,1,-,3</sub> |  | 1.2<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.2 | 1.2 | 14.6 |
| PJ Hall | 48% | 13.3<br><sub>2,-,-,-,-</sub> | 4.9<br><sub>0,-,-,-,-</sub> |  | 4.5<br><sub>1,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.6 | 0.8 | 10.2 |
| Michael Ajayi | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>if Jarrett Allen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid (CHA) | 98% | 33.8<br><sub>31,36,27,36,26</sub> | 19.7<br><sub>12,14,13,28,14</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 8.6<br><sub>11,5,6,9,6</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>1,2,2,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>2,0,2,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.9 | 2.8 | 31.0 |
| Grayson Allen (CHA) | 98% | 31.5<br><sub>21,30,19,27,22</sub> | 17.5<br><sub>5,27,11,22,0</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>3,4,1,2,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>2,3,0,4,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>1,7,3,5,0</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 2.2 | 25.1 |
| Sion James (CHA) | 98% | 30.0<br><sub>29,18,21,31,21</sub> | 8.5<br><sub>6,4,11,10,11</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>5,2,4,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>4,1,3,1,0</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 1.4 | 16.4 |
| Royce O'Neale (CHA) | 98% | 27.6<br><sub>17,23,18,18,26</sub> | 8.5<br><sub>7,8,2,0,7</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,0,2,2</sub> |  | 1.6<br><sub>2,1,0,0,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.4 | 1.1 | 15.2 |
| Coby White (CHA) | 98% | 26.9<br><sub>-,-,16,18,16</sub> | 18.1<br><sub>-,-,7,4,7</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>-,-,0,5,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>-,-,3,2,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>-,-,1,0,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.2 | 2.7 | 25.5 |
| Tidjane Salaun (CHA) | 93% | 26.2<br><sub>9,12,19,10,23</sub> | 10.2<br><sub>6,5,1,9,13</sub> |  | 6.0<br><sub>2,2,7,1,4</sub> |  | 1.4<br><sub>0,0,0,0,0</sub> |  | 1.6<br><sub>2,1,0,3,2</sub> |  | 0.8 | 0.3 | 1.2 | 17.6 |
| Christian Anderson (CHA) | 80% | 25.5<br><sub>14,8,9,-,25</sub> | 10.2<br><sub>4,2,8,-,4</sub> |  | 3.5<br><sub>3,0,2,-,3</sub> |  | 3.4<br><sub>3,0,2,-,5</sub> |  | 1.4<br><sub>0,0,1,-,0</sub> |  | 0.8 | 0.5 | 1.9 | 17.2 |
| Hannes Steinbach (CHA) | 52% | 24.0<br><sub>2,-,9,-,27</sub> | 6.1<br><sub>0,-,2,-,4</sub> |  | 6.3<br><sub>0,-,2,-,11</sub> |  | 1.0<br><sub>0,-,1,-,1</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.6 | 0.9 | 1.1 | 13.4 |
| Ryan Kalkbrenner (CHA) | 98% | 23.8<br><sub>15,19,16,19,21</sub> | 7.1<br><sub>2,6,4,6,4</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>4,3,6,4,5</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>0,4,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.2 | 14.9 |
| Liam McNeeley (CHA) | 58% | 21.4<br><sub>3,-,9,-,19</sub> | 9.0<br><sub>0,-,3,-,8</sub> |  | 4.0<br><sub>2,-,0,-,2</sub> |  | 1.7<br><sub>0,-,1,-,3</sub> |  | 1.1<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.2 | 1.2 | 14.6 |
| PJ Hall (CHA) | 48% | 13.3<br><sub>2,-,-,-,-</sub> | 4.9<br><sub>0,-,-,-,-</sub> |  | 4.5<br><sub>1,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.6 | 0.8 | 10.2 |
| Michael Ajayi (CHA) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.9 |
| Donovan Mitchell (CLE) | 98% | 35.6<br><sub>24,36,33,33,37</sub> | 25.7<br><sub>15,17,27,23,37</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>4,5,3,7,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 5.1<br><sub>3,11,6,8,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>2,4,5,1,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.3 | 2.7 | 35.6 |
| James Harden (CLE) | 98% | 35.2<br><sub>26,33,35,30,34</sub> | 17.4<br><sub>13,14,19,17,7</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>6,4,9,6,2</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 6.1<br><sub>7,6,6,3,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,3,3,3,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.5 | 3.0 | 28.2 |
| Evan Mobley (CLE) | 98% | 33.7<br><sub>25,33,33,32,33</sub> | 15.7<br><sub>27,16,16,22,12</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 7.9<br><sub>5,7,10,6,9</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>3,4,3,4,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>3,1,1,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 1.5 | 1.7 | 27.2 |
| Peyton Watson (CLE) | 98% | 29.4<br><sub>22,-,-,28,29</sub> | 12.2<br><sub>5,-,-,13,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>2,-,-,9,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>6,-,-,2,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>1,-,-,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.1 | 1.5 | 19.2 |
| Jarrett Allen (CLE) | 100% | 25.9<br><sub>24,28,7,-,-</sub> | 11.8<br><sub>25,14,0,-,-</sub> | 12.5 · – | 7.0<br><sub>11,6,1,-,-</sub> | 7.5 | 1.4<br><sub>4,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.9 | 1.2 | 1.2 | 20.1 |
| Meleek Thomas (CLE) | 88% | 23.2<br><sub>23,26,18,27,24</sub> | 9.4<br><sub>13,17,9,12,9</sub> |  | 2.6<br><sub>1,5,1,1,4</sub> |  | 1.2<br><sub>2,1,0,3,0</sub> |  | 1.5<br><sub>3,3,3,2,3</sub> |  | 0.8 | 0.2 | 1.1 | 13.2 |
| Mario Hezonja (CLE) | 98% | 20.2<br><sub>20,27,23,27,19</sub> | 7.5<br><sub>8,12,12,15,0</sub> |  | 5.1<br><sub>11,8,8,10,5</sub> |  | 1.4<br><sub>4,3,1,1,1</sub> |  | 1.1<br><sub>1,3,2,2,0</sub> |  | 0.6 | 0.1 | 0.9 | 14.1 |
| Tyrese Proctor (CLE) | 91% | 20.1<br><sub>18,19,22,19,23</sub> | 7.1<br><sub>9,10,11,3,7</sub> |  | 2.9<br><sub>4,4,1,6,3</sub> |  | 2.4<br><sub>5,2,0,3,3</sub> |  | 1.0<br><sub>3,2,2,0,2</sub> |  | 0.8 | 0.1 | 0.9 | 12.3 |
| Thomas Bryant (CLE) | 71% | 13.2<br><sub>11,5,13,16,15</sub> | 6.0<br><sub>11,4,8,13,5</sub> |  | 3.0<br><sub>2,0,0,6,3</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>3,0,1,1,1</sub> |  | 0.3 | 0.4 | 0.6 | 9.7 |
| Craig Porter Jr. (CLE) | 88% | 13.1<br><sub>16,8,14,3,15</sub> | 2.6<br><sub>2,0,0,0,0</sub> |  | 2.2<br><sub>2,4,1,0,1</sub> |  | 1.9<br><sub>4,1,1,0,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 6.7 |
| Riley Minix (CLE) | 48% | 9.8<br><sub>6,-,-,-,10</sub> | 3.5<br><sub>0,-,-,-,8</sub> |  | 1.6<br><sub>3,-,-,-,3</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,2</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| Ernest Udeh Jr. (CLE) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Norchad Omier (CLE) | 52% | 6.0<br><sub>-,-,-,3,-</sub> | 1.9<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,2,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |

</details>


### WAS @ DET
Out: Jalen Duren (DET), Isaiah Joe (DET), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.0–117.4 | WAS 25% | 3.97 / 1.34 | DET -9.5 | 225.5 | DET -10.5 covers 47%; o219.5 62% |
| Expected (weighted by chance each plays) | 109.1–116.6 | WAS 28% | 3.55 / 1.39 | DET -7.5 | 225.5 | DET -10.5 covers 42%; o219.5 63% |
| if Bilal Coulibaly plays | 108.9–116.8 | WAS 28% | 3.52 / 1.40 | DET -7.5 | 225.5 | DET -10.5 covers 43%; o219.5 63% |
| if Anthony Davis plays | 109.2–116.9 | WAS 29% | 3.44 / 1.41 | DET -7.5 | 226.5 | DET -10.5 covers 42%; o219.5 64% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Bilal Coulibaly (WAS) | Questionable | 55% | 26.3 | 9.4 | 3.9 | 1.7 | 0.9 | 1.1 | 1.0 | 1.3 | 14.9 | full tables below |
| Anthony Davis (WAS) | Questionable | 55% | 34.1 | 20.9 | 11.1 | 2.8 | 0.7 | 1.2 | 1.9 | 2.5 | 34.8 | full tables below |
| Elijah Harkless (DET) | Questionable | 55% | 7.3 | 0.4 | 0.3 | 0.4 | 0.0 | 0.2 | 0.2 | 0.3 | 1.1 | small |
| Isaac Jones (DET) | Questionable | 55% | 6.3 | 3.1 | 1.6 | 0.3 | 0.1 | 0.3 | 0.4 | 0.4 | 5.1 | small |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 36.2<br><sub>38,34,34,37,28</sub> | 20.6<br><sub>21,15,18,23,4</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>7,3,2,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 9.2<br><sub>9,9,6,10,3</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.3 | 3.8 | 32.9 |
| AJ Dybantsa | 96% | 35.1<br><sub>30,33,32,36,31</sub> | 16.7<br><sub>17,21,9,11,19</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>8,5,6,9,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>1,2,3,3,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,1,0,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.3 | 2.3 | 25.6 |
| Kyshawn George | 98% | 35.0<br><sub>32,37,35,39,30</sub> | 18.7<br><sub>12,22,25,33,14</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>3,4,4,4,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>3,5,7,7,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>4,4,3,5,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 1.4 | 2.9 | 28.9 |
| Alex Sarr | 98% | 28.9<br><sub>29,-,23,30,28</sub> | 13.1<br><sub>3,-,11,13,15</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>8,-,9,8,14</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>0,-,1,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>1,-,0,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.9 | 2.1 | 1.8 | 23.2 |
| Tre Johnson | 88% | 27.0<br><sub>13,22,14,27,28</sub> | 10.9<br><sub>4,4,3,23,4</sub> |  | 2.7<br><sub>2,3,2,1,0</sub> |  | 1.4<br><sub>0,0,0,1,3</sub> |  | 1.6<br><sub>0,0,1,5,0</sub> |  | 0.8 | 0.2 | 1.4 | 14.9 |
| Bub Carrington | 98% | 23.6<br><sub>20,19,19,15,21</sub> | 7.8<br><sub>9,3,0,5,9</sub> |  | 2.7<br><sub>4,4,1,1,6</sub> |  | 2.8<br><sub>2,4,2,1,1</sub> |  | 1.3<br><sub>3,1,0,1,3</sub> |  | 0.7 | 0.2 | 1.5 | 13.4 |
| Deandre Ayton | 98% | 19.5<br><sub>17,24,11,23,7</sub> | 6.5<br><sub>3,4,5,8,2</sub> |  | 5.9<br><sub>3,6,4,11,1</sub> |  | 0.8<br><sub>1,2,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.9 | 13.2 |
| Will Riley | 88% | 17.5<br><sub>1,4,13,9,20</sub> | 6.8<br><sub>0,0,0,7,5</sub> |  | 2.0<br><sub>0,0,0,0,2</sub> |  | 1.2<br><sub>0,1,0,0,1</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 10.0 |
| Khris Middleton | 48% | 17.4<br><sub>5,-,-,-,-</sub> | 5.8<br><sub>0,-,-,-,-</sub> |  | 2.9<br><sub>0,-,-,-,-</sub> |  | 1.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 1.2 | 9.9 |
| Anthony Gill | 48% | 16.9<br><sub>-,-,-,-,9</sub> | 5.8<br><sub>-,-,-,-,1</sub> |  | 3.0<br><sub>-,-,-,-,1</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.4 | 0.8 | 9.7 |
| Tre Mann | 52% | 14.2<br><sub>1,-,3,-,18</sub> | 5.5<br><sub>0,-,2,-,2</sub> |  | 1.5<br><sub>0,-,0,-,0</sub> |  | 1.5<br><sub>0,-,0,-,2</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.7 | 0.3 | 0.8 | 8.4 |
| Felix Okpara | 52% | 9.3<br><sub>-,-,3,-,-</sub> | 3.1<br><sub>-,-,0,-,-</sub> |  | 2.3<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 5.9 |

</details>

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 33.2<br><sub>39,28,27,40,38</sub> | 25.9<br><sub>30,20,33,26,14</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>5,5,5,7,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 9.0<br><sub>7,4,7,11,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>4,1,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.8 | 3.7 | 40.0 |
| Duncan Robinson | 98% | 29.4<br><sub>32,26,32,37,27</sub> | 15.5<br><sub>13,17,24,27,12</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,4,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.6<br><sub>2,2,3,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>3,2,6,7,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 1.1 | 21.0 |
| John Collins | 98% | 27.2<br><sub>18,26,19,26,32</sub> | 12.0<br><sub>4,4,4,16,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>2,9,3,1,4</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,0,1,0,1</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 1.0 | 0.9 | 1.3 | 19.5 |
| Ausar Thompson | 98% | 26.9<br><sub>29,26,26,34,24</sub> | 10.0<br><sub>7,11,14,11,7</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>9,8,6,17,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>8,6,4,3,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.9 | 1.0 | 1.6 | 22.0 |
| Daniss Jenkins | 98% | 26.7<br><sub>24,24,23,21,32</sub> | 12.7<br><sub>14,6,2,5,31</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,3,1,1,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>3,5,7,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>2,2,0,1,8</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.3 | 1.6 | 21.2 |
| Kevin Huerter | 97% | 25.7<br><sub>19,24,20,20,35</sub> | 11.2<br><sub>3,8,9,8,24</sub> | 7.5 · –<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>2,1,2,1,5</sub> |  | 3.3<br><sub>3,3,3,0,5</sub> |  | 1.7<br><sub>1,2,3,2,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.7 | 1.0 | 18.1 |
| Paul Reed | 97% | 24.9<br><sub>38,31,28,30,20</sub> | 13.6<br><sub>16,12,11,8,8</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 8.0<br><sub>4,4,5,7,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>0,1,4,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.3<br><sub>2,0,0,0,0</sub> |  | 1.3 | 1.3 | 1.5 | 23.8 |
| Javonte Green | 97% | 19.6<br><sub>21,22,20,15,17</sub> | 7.1<br><sub>7,6,5,1,7</sub> |  | 3.1<br><sub>2,3,2,3,2</sub> |  | 0.9<br><sub>2,1,0,1,2</sub> |  | 1.0<br><sub>1,1,1,0,1</sub> |  | 1.3 | 0.4 | 0.5 | 11.1 |
| Ronald Holland II | 98% | 16.9<br><sub>12,22,20,12,14</sub> | 7.3<br><sub>0,18,11,3,5</sub> |  | 3.5<br><sub>2,3,2,2,2</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>0,2,3,1,1</sub> |  | 0.9 | 0.6 | 0.9 | 12.1 |
| Taurean Prince | 38% | 9.7<br><sub>6,-,-,-,-</sub> | 3.8<br><sub>1,-,-,-,-</sub> |  | 1.4<br><sub>2,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.9 |
| Chaz Lanier | 48% | 6.9<br><sub>-,3,7,-,-</sub> | 2.9<br><sub>-,6,5,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,2,1,-,-</sub> |  | 0.2 | 0.1 | 0.1 | 4.1 |
| Tolu Smith | 67% | 6.9<br><sub>1,3,8,5,-</sub> | 2.8<br><sub>2,2,0,1,-</sub> |  | 2.5<br><sub>1,1,2,1,-</sub> |  | 0.4<br><sub>0,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.8 |
| Ebuka Okorie | 52% | 6.2<br><sub>-,3,6,-,-</sub> | 2.2<br><sub>-,0,4,-,-</sub> |  | 0.8<br><sub>-,0,2,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |

</details>

<details><summary>if Bilal Coulibaly plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | 98% | 33.2<br><sub>39,28,27,40,38</sub> | 25.8<br><sub>30,20,33,26,14</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>5,5,5,7,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 9.0<br><sub>7,4,7,11,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>4,1,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.8 | 3.7 | 39.9 |
| Duncan Robinson (DET) | 98% | 29.2<br><sub>32,26,32,37,27</sub> | 15.4<br><sub>13,17,24,27,12</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,4,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.6<br><sub>2,2,3,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>3,2,6,7,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 1.1 | 20.9 |
| John Collins (DET) | 98% | 27.2<br><sub>18,26,19,26,32</sub> | 11.9<br><sub>4,4,4,16,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>2,9,3,1,4</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,0,1,0,1</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 1.0 | 0.9 | 1.3 | 19.4 |
| Ausar Thompson (DET) | 98% | 26.9<br><sub>29,26,26,34,24</sub> | 10.1<br><sub>7,11,14,11,7</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>9,8,6,17,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>8,6,4,3,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.9 | 1.0 | 1.6 | 22.1 |
| Daniss Jenkins (DET) | 98% | 26.6<br><sub>24,24,23,21,32</sub> | 12.6<br><sub>14,6,2,5,31</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,3,1,1,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 5.1<br><sub>3,5,7,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>2,2,0,1,8</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.3 | 1.6 | 21.1 |
| Kevin Huerter (DET) | 97% | 25.8<br><sub>19,24,20,20,35</sub> | 11.2<br><sub>3,8,9,8,24</sub> | 7.5 · –<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>2,1,2,1,5</sub> |  | 3.3<br><sub>3,3,3,0,5</sub> |  | 1.7<br><sub>1,2,3,2,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.7 | 1.0 | 18.1 |
| Paul Reed (DET) | 97% | 24.9<br><sub>38,31,28,30,20</sub> | 13.4<br><sub>16,12,11,8,8</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 8.0<br><sub>4,4,5,7,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>0,1,4,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.3<br><sub>2,0,0,0,0</sub> |  | 1.3 | 1.2 | 1.5 | 23.6 |
| Javonte Green (DET) | 97% | 19.7<br><sub>21,22,20,15,17</sub> | 7.0<br><sub>7,6,5,1,7</sub> |  | 3.1<br><sub>2,3,2,3,2</sub> |  | 0.9<br><sub>2,1,0,1,2</sub> |  | 1.0<br><sub>1,1,1,0,1</sub> |  | 1.3 | 0.4 | 0.5 | 11.0 |
| Ronald Holland II (DET) | 98% | 16.9<br><sub>12,22,20,12,14</sub> | 7.2<br><sub>0,18,11,3,5</sub> |  | 3.5<br><sub>2,3,2,2,2</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>0,2,3,1,1</sub> |  | 0.9 | 0.6 | 0.9 | 12.0 |
| Taurean Prince (DET) | 38% | 9.7<br><sub>6,-,-,-,-</sub> | 3.8<br><sub>1,-,-,-,-</sub> |  | 1.4<br><sub>2,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.9 |
| Chaz Lanier (DET) | 48% | 6.9<br><sub>-,3,7,-,-</sub> | 2.9<br><sub>-,6,5,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,2,1,-,-</sub> |  | 0.2 | 0.1 | 0.1 | 4.0 |
| Tolu Smith (DET) | 67% | 6.9<br><sub>1,3,8,5,-</sub> | 2.8<br><sub>2,2,0,1,-</sub> |  | 2.5<br><sub>1,1,2,1,-</sub> |  | 0.4<br><sub>0,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.8 |
| Ebuka Okorie (DET) | 52% | 6.3<br><sub>-,3,6,-,-</sub> | 2.3<br><sub>-,0,4,-,-</sub> |  | 0.9<br><sub>-,0,2,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Trae Young (WAS) | 98% | 35.3<br><sub>38,34,34,37,28</sub> | 19.8<br><sub>21,15,18,23,4</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>7,3,2,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 9.2<br><sub>9,9,6,10,3</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.3 | 3.5 | 32.1 |
| Kyshawn George (WAS) | 98% | 34.4<br><sub>32,37,35,39,30</sub> | 17.7<br><sub>12,22,25,33,14</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>3,4,4,4,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>3,5,7,7,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>4,4,3,5,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 1.3 | 2.6 | 28.0 |
| AJ Dybantsa (WAS) | 96% | 33.9<br><sub>30,33,32,36,31</sub> | 15.9<br><sub>17,21,9,11,19</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>8,5,6,9,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>1,2,3,3,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,1,0,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.2 | 0.3 | 2.1 | 24.8 |
| Alex Sarr (WAS) | 98% | 27.5<br><sub>29,-,23,30,28</sub> | 12.3<br><sub>3,-,11,13,15</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>8,-,9,8,14</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,-,1,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>1,-,0,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 2.0 | 1.7 | 21.9 |
| Bilal Coulibaly (WAS) | 100% | 26.3<br><sub>22,33,23,24,20</sub> | 9.4<br><sub>1,7,6,9,0</sub> |  | 3.9<br><sub>5,1,2,5,5</sub> |  | 1.7<br><sub>1,2,2,0,0</sub> |  | 0.9<br><sub>0,0,0,1,0</sub> |  | 1.1 | 1.0 | 1.3 | 14.9 |
| Tre Johnson (WAS) | 88% | 23.3<br><sub>13,22,14,27,28</sub> | 9.8<br><sub>4,4,3,23,4</sub> |  | 2.4<br><sub>2,3,2,1,0</sub> |  | 1.1<br><sub>0,0,0,1,3</sub> |  | 1.4<br><sub>0,0,1,5,0</sub> |  | 0.7 | 0.2 | 1.2 | 13.4 |
| Bub Carrington (WAS) | 98% | 20.7<br><sub>20,19,19,15,21</sub> | 6.9<br><sub>9,3,0,5,9</sub> |  | 2.3<br><sub>4,4,1,1,6</sub> |  | 2.5<br><sub>2,4,2,1,1</sub> |  | 1.1<br><sub>3,1,0,1,3</sub> |  | 0.6 | 0.2 | 1.4 | 11.6 |
| Deandre Ayton (WAS) | 98% | 16.9<br><sub>17,24,11,23,7</sub> | 5.8<br><sub>3,4,5,8,2</sub> |  | 5.2<br><sub>3,6,4,11,1</sub> |  | 0.7<br><sub>1,2,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.8 | 11.7 |
| Will Riley (WAS) | 88% | 14.6<br><sub>1,4,13,9,20</sub> | 5.5<br><sub>0,0,0,7,5</sub> |  | 1.6<br><sub>0,0,0,0,2</sub> |  | 1.0<br><sub>0,1,0,0,1</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 8.1 |
| Khris Middleton (WAS) | 48% | 14.3<br><sub>5,-,-,-,-</sub> | 4.6<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>0,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 8.0 |
| Anthony Gill (WAS) | 48% | 12.8<br><sub>-,-,-,-,9</sub> | 4.3<br><sub>-,-,-,-,1</sub> |  | 2.3<br><sub>-,-,-,-,1</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.4 |
| Tre Mann (WAS) | 52% | 11.5<br><sub>1,-,3,-,18</sub> | 4.5<br><sub>0,-,2,-,2</sub> |  | 1.3<br><sub>0,-,0,-,0</sub> |  | 1.2<br><sub>0,-,0,-,2</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 6.9 |
| Felix Okpara (WAS) | 52% | 7.3<br><sub>-,-,3,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 1.8<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |

</details>

<details><summary>if Anthony Davis plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | 98% | 33.2<br><sub>39,28,27,40,38</sub> | 26.0<br><sub>30,20,33,26,14</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>5,5,5,7,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 9.0<br><sub>7,4,7,11,8</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>4,1,4,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.8 | 3.6 | 40.1 |
| Duncan Robinson (DET) | 98% | 29.4<br><sub>32,26,32,37,27</sub> | 15.5<br><sub>13,17,24,27,12</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,4,2,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.6<br><sub>2,2,3,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>3,2,6,7,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 1.1 | 21.0 |
| John Collins (DET) | 98% | 27.3<br><sub>18,26,19,26,32</sub> | 12.0<br><sub>4,4,4,16,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>2,9,3,1,4</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,0,1,0,1</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 1.0 | 0.9 | 1.3 | 19.4 |
| Ausar Thompson (DET) | 98% | 26.9<br><sub>29,26,26,34,24</sub> | 10.1<br><sub>7,11,14,11,7</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>9,8,6,17,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>8,6,4,3,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.9 | 1.0 | 1.6 | 22.1 |
| Daniss Jenkins (DET) | 98% | 26.6<br><sub>24,24,23,21,32</sub> | 12.6<br><sub>14,6,2,5,31</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,3,1,1,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>3,5,7,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>2,2,0,1,8</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.3 | 1.6 | 21.2 |
| Kevin Huerter (DET) | 97% | 25.8<br><sub>19,24,20,20,35</sub> | 11.2<br><sub>3,8,9,8,24</sub> | 7.5 · –<br><sub>o 55% · u 45%</sub> | 3.6<br><sub>2,1,2,1,5</sub> |  | 3.3<br><sub>3,3,3,0,5</sub> |  | 1.7<br><sub>1,2,3,2,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 1.0 | 18.1 |
| Paul Reed (DET) | 97% | 24.8<br><sub>38,31,28,30,20</sub> | 13.4<br><sub>16,12,11,8,8</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 7.9<br><sub>4,4,5,7,10</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>0,1,4,4,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.3<br><sub>2,0,0,0,0</sub> |  | 1.3 | 1.3 | 1.5 | 23.6 |
| Javonte Green (DET) | 97% | 19.7<br><sub>21,22,20,15,17</sub> | 7.0<br><sub>7,6,5,1,7</sub> |  | 3.1<br><sub>2,3,2,3,2</sub> |  | 0.9<br><sub>2,1,0,1,2</sub> |  | 1.0<br><sub>1,1,1,0,1</sub> |  | 1.3 | 0.4 | 0.4 | 11.0 |
| Ronald Holland II (DET) | 98% | 16.9<br><sub>12,22,20,12,14</sub> | 7.3<br><sub>0,18,11,3,5</sub> |  | 3.6<br><sub>2,3,2,2,2</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.7<br><sub>0,2,3,1,1</sub> |  | 0.9 | 0.6 | 0.9 | 12.1 |
| Taurean Prince (DET) | 38% | 9.7<br><sub>6,-,-,-,-</sub> | 3.8<br><sub>1,-,-,-,-</sub> |  | 1.4<br><sub>2,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.9 |
| Chaz Lanier (DET) | 48% | 7.0<br><sub>-,3,7,-,-</sub> | 3.0<br><sub>-,6,5,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,2,1,-,-</sub> |  | 0.2 | 0.1 | 0.1 | 4.2 |
| Tolu Smith (DET) | 67% | 6.9<br><sub>1,3,8,5,-</sub> | 2.8<br><sub>2,2,0,1,-</sub> |  | 2.5<br><sub>1,1,2,1,-</sub> |  | 0.4<br><sub>0,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.7 |
| Ebuka Okorie (DET) | 52% | 6.2<br><sub>-,3,6,-,-</sub> | 2.2<br><sub>-,0,4,-,-</sub> |  | 0.8<br><sub>-,0,2,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Trae Young (WAS) | 98% | 35.2<br><sub>38,34,34,37,28</sub> | 18.5<br><sub>21,15,18,23,4</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>7,3,2,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 8.9<br><sub>9,9,6,10,3</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.3 | 3.4 | 30.4 |
| Anthony Davis (WAS) | 100% | 34.1<br><sub>34,34,30,-,-</sub> | 20.9<br><sub>25,27,26,-,-</sub> | 20.5 · – | 11.1<br><sub>13,9,10,-,-</sub> | 9.5 | 2.8<br><sub>1,1,3,-,-</sub> | 2.5 | 0.7<br><sub>0,1,0,-,-</sub> |  | 1.2 | 1.9 | 2.5 | 34.8 |
| Kyshawn George (WAS) | 98% | 33.6<br><sub>32,37,35,39,30</sub> | 15.9<br><sub>12,22,25,33,14</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>3,4,4,4,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.5<br><sub>3,5,7,7,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>4,4,3,5,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 1.3 | 2.5 | 25.6 |
| AJ Dybantsa (WAS) | 96% | 33.1<br><sub>30,33,32,36,31</sub> | 14.5<br><sub>17,21,9,11,19</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>8,5,6,9,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,2,3,3,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,1,0,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.3 | 2.0 | 22.9 |
| Alex Sarr (WAS) | 98% | 26.9<br><sub>29,-,23,30,28</sub> | 11.1<br><sub>3,-,11,13,15</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>8,-,9,8,14</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,-,1,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0<br><sub>1,-,0,1,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.8 | 1.9 | 1.6 | 20.2 |
| Tre Johnson (WAS) | 88% | 22.8<br><sub>13,22,14,27,28</sub> | 9.4<br><sub>4,4,3,23,4</sub> |  | 2.4<br><sub>2,3,2,1,0</sub> |  | 1.1<br><sub>0,0,0,1,3</sub> |  | 1.3<br><sub>0,0,1,5,0</sub> |  | 0.7 | 0.2 | 1.2 | 12.8 |
| Bub Carrington (WAS) | 98% | 20.0<br><sub>20,19,19,15,21</sub> | 6.2<br><sub>9,3,0,5,9</sub> |  | 2.2<br><sub>4,4,1,1,6</sub> |  | 2.3<br><sub>2,4,2,1,1</sub> |  | 0.9<br><sub>3,1,0,1,3</sub> |  | 0.6 | 0.2 | 1.3 | 10.7 |
| Deandre Ayton (WAS) | 98% | 15.9<br><sub>17,24,11,23,7</sub> | 5.2<br><sub>3,4,5,8,2</sub> |  | 4.8<br><sub>3,6,4,11,1</sub> |  | 0.7<br><sub>1,2,1,3,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.8 | 10.7 |
| Will Riley (WAS) | 88% | 14.4<br><sub>1,4,13,9,20</sub> | 5.3<br><sub>0,0,0,7,5</sub> |  | 1.6<br><sub>0,0,0,0,2</sub> |  | 1.0<br><sub>0,1,0,0,1</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 0.8 | 7.9 |
| Khris Middleton (WAS) | 48% | 12.4<br><sub>5,-,-,-,-</sub> | 3.7<br><sub>0,-,-,-,-</sub> |  | 2.0<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.9 | 6.7 |
| Tre Mann (WAS) | 52% | 11.1<br><sub>1,-,3,-,18</sub> | 4.6<br><sub>0,-,2,-,2</sub> |  | 1.1<br><sub>0,-,0,-,0</sub> |  | 1.1<br><sub>0,-,0,-,2</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 6.8 |
| Anthony Gill (WAS) | 48% | 9.6<br><sub>-,-,-,-,9</sub> | 3.1<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |
| Felix Okpara (WAS) | 52% | 6.4<br><sub>-,-,3,-,-</sub> | 2.4<br><sub>-,-,0,-,-</sub> |  | 1.6<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.4 |

</details>


### MEM @ TOR
Out: Kawhi Leonard (TOR), Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.2–117.0 | MEM 45% | 2.23 / 1.81 | TOR -2.5 | 232.5 | TOR -2.5 covers 49%; o228.5 58% |
| Expected (weighted by chance each plays) | 114.2–118.6 | MEM 38% | 2.63 / 1.61 | TOR -4.5 | 232.5 | TOR -2.5 covers 56%; o228.5 58% |
| if Immanuel Quickley plays | 114.8–117.7 | MEM 42% | 2.38 / 1.73 | TOR -3.5 | 232.5 | TOR -2.5 covers 52%; o228.5 58% |
| if Collin Murray-Boyles plays | 114.7–117.4 | MEM 43% | 2.34 / 1.74 | TOR -2.5 | 231.5 | TOR -2.5 covers 51%; o228.5 57% |
| if Scottie Barnes plays | 114.7–117.8 | MEM 42% | 2.41 / 1.71 | TOR -3.5 | 232.5 | TOR -2.5 covers 52%; o228.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Immanuel Quickley (TOR) | Questionable | 55% | 32.5 | 21.3 | 4.2 | 6.4 | 2.9 | 1.5 | 0.2 | 1.8 | 32.0 | full tables below |
| Collin Murray-Boyles (TOR) | Questionable | 55% | 30.3 | 15.8 | 7.2 | 2.9 | 0.4 | 1.4 | 1.4 | 2.2 | 25.8 | full tables below |
| Scottie Barnes (TOR) | Questionable | 55% | 35.0 | 25.9 | 7.7 | 7.3 | 0.8 | 1.8 | 1.3 | 3.6 | 40.9 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 31.5<br><sub>28,26,38,33,31</sub> | 14.8<br><sub>18,27,18,10,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.6 | 2.8 | 27.7 |
| Ty Jerome | 98% | 28.6<br><sub>24,-,37,29,28</sub> | 21.8<br><sub>10,-,40,23,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,-,5,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.8<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.3 | 2.7 | 29.8 |
| Cedric Coward | 98% | 26.9<br><sub>27,23,31,33,23</sub> | 13.4<br><sub>17,10,10,23,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.4 | 1.8 | 21.8 |
| Jaylen Wells | 98% | 25.8<br><sub>25,22,34,21,25</sub> | 10.3<br><sub>10,4,16,0,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>0,0,3,3,0</sub> |  | 1.4<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.1 | 14.3 |
| Jerami Grant | 98% | 22.5<br><sub>27,23,24,24,22</sub> | 10.3<br><sub>2,14,11,11,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,1,2,2,2</sub> |  | 1.2<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.6 | 1.5 | 13.9 |
| Zach Edey | 98% | 20.8<br><sub>19,18,19,25,20</sub> | 8.8<br><sub>13,4,6,11,14</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.3 | 1.5 | 17.1 |
| Javon Small | 91% | 19.5<br><sub>-,20,-,-,21</sub> | 8.8<br><sub>-,7,-,-,10</sub> |  | 2.7<br><sub>-,1,-,-,4</sub> |  | 2.9<br><sub>-,5,-,-,2</sub> |  | 1.0<br><sub>-,2,-,-,1</sub> |  | 0.8 | 0.2 | 1.7 | 14.4 |
| Cam Spencer | 98% | 18.1<br><sub>23,25,19,24,19</sub> | 7.1<br><sub>8,10,13,7,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>8,13,7,9,0</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.1 | 13.2 |
| Kris Murray | 80% | 12.2<br><sub>3,21,19,15,13</sub> | 3.1<br><sub>0,2,0,5,2</sub> |  | 1.8<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.6 | 5.6 |
| GG Jackson | 72% | 11.6<br><sub>21,21,16,7,-</sub> | 6.2<br><sub>12,21,6,1,-</sub> |  | 2.1<br><sub>7,3,0,2,-</sub> |  | 0.6<br><sub>2,2,1,0,-</sub> |  | 0.5<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.0 | 9.0 |
| Quinten Post | 91% | 11.6<br><sub>7,-,-,11,15</sub> | 4.5<br><sub>10,-,-,2,0</sub> |  | 2.1<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.0 |
| Olivier-Maxence Prosper | 63% | 9.8<br><sub>3,4,-,7,11</sub> | 4.8<br><sub>4,2,-,4,2</sub> |  | 1.9<br><sub>1,1,-,3,3</sub> |  | 0.5<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.2 |
| Jahmai Mashack | 52% | 7.7<br><sub>-,4,-,-,4</sub> | 2.5<br><sub>-,2,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,1,-,-,2</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 4.3 |
| Taylor Hendricks | 58% | 7.2<br><sub>3,4,-,-,4</sub> | 3.0<br><sub>0,6,-,-,4</sub> |  | 1.4<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.7 |
| Carson Cooper | 48% | 5.8<br><sub>-,3,-,-,-</sub> | 2.5<br><sub>-,1,-,-,-</sub> |  | 2.4<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.3 | 1.0 | 5.6 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 36.6<br><sub>34,32,37,33,37</sub> | 29.0<br><sub>9,22,26,22,27</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 7.2<br><sub>3,10,6,5,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>1,4,2,3,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.6 | 3.5 | 41.9 |
| Ja'Kobe Walter | 98% | 32.6<br><sub>32,33,35,27,29</sub> | 15.9<br><sub>9,11,10,8,7</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>3,4,6,1,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>1,2,5,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.4<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.8 | 0.5 | 1.4 | 23.2 |
| Jamal Shead | 98% | 30.9<br><sub>23,25,20,20,34</sub> | 11.4<br><sub>2,9,6,3,10</sub> |  | 2.7<br><sub>1,2,1,3,3</sub> |  | 8.8<br><sub>8,6,6,6,16</sub> |  | 1.3<br><sub>0,2,0,1,1</sub> |  | 1.5 | 0.3 | 2.7 | 22.9 |
| Jakob Poeltl | 86% | 27.2<br><sub>23,-,-,19,31</sub> | 13.2<br><sub>12,-,-,8,19</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 8.6<br><sub>11,-,-,5,11</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>3,-,-,1,1</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.1 | 1.3 | 1.8 | 24.2 |
| Jamison Battle | 98% | 26.5<br><sub>19,17,21,19,21</sub> | 12.5<br><sub>2,20,12,9,6</sub> |  | 3.8<br><sub>0,5,0,1,2</sub> |  | 1.5<br><sub>0,0,0,0,0</sub> |  | 2.0<br><sub>0,4,4,2,1</sub> |  | 0.6 | 0.3 | 1.1 | 17.7 |
| Malachi Smith | 88% | 23.6 | 8.7 |  | 3.9 |  | 3.9 |  | 0.9 |  | 1.0 | 0.4 | 1.2 | 16.5 |
| Alijah Martin | 88% | 23.1<br><sub>-,16,6,9,31</sub> | 11.3<br><sub>-,5,2,6,27</sub> |  | 3.5<br><sub>-,2,2,1,4</sub> |  | 2.2<br><sub>-,4,0,0,1</sub> |  | 1.2<br><sub>-,1,0,0,6</sub> |  | 1.0 | 0.5 | 1.8 | 17.0 |
| Allen Graves | 98% | 21.5<br><sub>9,10,7,14,16</sub> | 7.8<br><sub>7,3,0,5,3</sub> |  | 4.0<br><sub>4,0,0,1,2</sub> |  | 1.4<br><sub>0,0,2,1,0</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.6 | 0.7 | 13.2 |
| Kevin McCullar Jr. | 23% | 15.4<br><sub>-,-,-,-,-</sub> | 5.5<br><sub>-,-,-,-,-</sub> |  | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.2 | 0.9 | 10.1 |
| Kyle Anderson | 63% | 14.0<br><sub>-,4,8,4,-</sub> | 4.6<br><sub>-,2,2,2,-</sub> |  | 2.9<br><sub>-,3,0,0,-</sub> |  | 2.7<br><sub>-,3,0,1,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.7 | 0.5 | 0.9 | 10.2 |
| Trayce Jackson-Davis | 72% | 12.2<br><sub>1,9,2,4,-</sub> | 5.1<br><sub>0,5,0,1,-</sub> |  | 4.3<br><sub>0,5,0,0,-</sub> |  | 0.9<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.7 | 0.8 | 0.6 | 10.3 |
| Jaden Bradley | 71% | 11.3<br><sub>-,4,-,4,8</sub> | 4.8<br><sub>-,3,-,2,3</sub> |  | 1.9<br><sub>-,1,-,1,0</sub> |  | 1.3<br><sub>-,2,-,0,1</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.9 | 0.2 | 0.7 | 8.0 |

</details>

<details><summary>if Immanuel Quickley plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 31.6<br><sub>28,26,38,33,31</sub> | 14.8<br><sub>18,27,18,10,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.6 | 2.8 | 27.8 |
| Ty Jerome (MEM) | 98% | 28.6<br><sub>24,-,37,29,28</sub> | 21.8<br><sub>10,-,40,23,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,-,5,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.8<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 2.7 | 29.8 |
| Cedric Coward (MEM) | 98% | 27.0<br><sub>27,23,31,33,23</sub> | 13.4<br><sub>17,10,10,23,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 1.9 | 21.9 |
| Jaylen Wells (MEM) | 98% | 25.8<br><sub>25,22,34,21,25</sub> | 10.3<br><sub>10,4,16,0,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>0,0,3,3,0</sub> |  | 1.4<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.1 | 14.4 |
| Jerami Grant (MEM) | 98% | 22.6<br><sub>27,23,24,24,22</sub> | 10.3<br><sub>2,14,11,11,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,1,2,2,2</sub> |  | 1.2<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.5 | 1.5 | 13.9 |
| Zach Edey (MEM) | 98% | 20.7<br><sub>19,18,19,25,20</sub> | 8.7<br><sub>13,4,6,11,14</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.3 | 1.5 | 17.1 |
| Javon Small (MEM) | 91% | 19.4<br><sub>-,20,-,-,21</sub> | 8.7<br><sub>-,7,-,-,10</sub> |  | 2.7<br><sub>-,1,-,-,4</sub> |  | 2.8<br><sub>-,5,-,-,2</sub> |  | 1.0<br><sub>-,2,-,-,1</sub> |  | 0.8 | 0.2 | 1.7 | 14.2 |
| Cam Spencer (MEM) | 98% | 18.1<br><sub>23,25,19,24,19</sub> | 7.2<br><sub>8,10,13,7,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>8,13,7,9,0</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.1 | 13.2 |
| Kris Murray (MEM) | 80% | 12.3<br><sub>3,21,19,15,13</sub> | 3.1<br><sub>0,2,0,5,2</sub> |  | 1.9<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.2 | 0.6 | 5.7 |
| GG Jackson (MEM) | 72% | 11.7<br><sub>21,21,16,7,-</sub> | 6.2<br><sub>12,21,6,1,-</sub> |  | 2.1<br><sub>7,3,0,2,-</sub> |  | 0.7<br><sub>2,2,1,0,-</sub> |  | 0.6<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.0 | 9.0 |
| Quinten Post (MEM) | 91% | 11.5<br><sub>7,-,-,11,15</sub> | 4.4<br><sub>10,-,-,2,0</sub> |  | 2.1<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 6.9 |
| Olivier-Maxence Prosper (MEM) | 63% | 9.9<br><sub>3,4,-,7,11</sub> | 4.8<br><sub>4,2,-,4,2</sub> |  | 1.9<br><sub>1,1,-,3,3</sub> |  | 0.4<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.2 |
| Jahmai Mashack (MEM) | 52% | 7.6<br><sub>-,4,-,-,4</sub> | 2.4<br><sub>-,2,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.8<br><sub>-,1,-,-,2</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 4.2 |
| Taylor Hendricks (MEM) | 58% | 7.3<br><sub>3,4,-,-,4</sub> | 3.1<br><sub>0,6,-,-,4</sub> |  | 1.4<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Carson Cooper (MEM) | 48% | 5.8<br><sub>-,3,-,-,-</sub> | 2.5<br><sub>-,1,-,-,-</sub> |  | 2.4<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 1.0 | 5.6 |
| RJ Barrett (TOR) | 98% | 35.1<br><sub>34,32,37,33,37</sub> | 27.0<br><sub>9,22,26,22,27</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>3,10,6,5,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,4,2,3,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.5 | 3.1 | 38.7 |
| Immanuel Quickley (TOR) | 100% | 32.5<br><sub>37,33,38,32,-</sub> | 21.3<br><sub>17,12,27,13,-</sub> | 18.5 · – | 4.2<br><sub>6,6,4,1,-</sub> | 3.5 | 6.4<br><sub>8,7,2,7,-</sub> | 5.5 | 2.9<br><sub>4,3,1,2,-</sub> | 2.5 | 1.5 | 0.2 | 1.8 | 32.0 |
| Ja'Kobe Walter (TOR) | 98% | 30.7<br><sub>32,33,35,27,29</sub> | 14.1<br><sub>9,11,10,8,7</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>3,4,6,1,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.3<br><sub>1,2,5,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6 | 0.4 | 1.1 | 20.5 |
| Jamal Shead (TOR) | 98% | 27.4<br><sub>23,25,20,20,34</sub> | 9.1<br><sub>2,9,6,3,10</sub> |  | 2.4<br><sub>1,2,1,3,3</sub> |  | 7.3<br><sub>8,6,6,6,16</sub> |  | 1.1<br><sub>0,2,0,1,1</sub> |  | 1.4 | 0.2 | 2.1 | 18.8 |
| Jakob Poeltl (TOR) | 86% | 25.2<br><sub>23,-,-,19,31</sub> | 11.9<br><sub>12,-,-,8,19</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 8.0<br><sub>11,-,-,5,11</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,-,-,1,1</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.0 | 1.2 | 1.5 | 22.0 |
| Jamison Battle (TOR) | 98% | 22.2<br><sub>19,17,21,19,21</sub> | 9.9<br><sub>2,20,12,9,6</sub> |  | 3.1<br><sub>0,5,0,1,2</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 1.6<br><sub>0,4,4,2,1</sub> |  | 0.5 | 0.2 | 0.8 | 14.2 |
| Malachi Smith (TOR) | 88% | 21.2 | 7.7 |  | 3.4 |  | 3.1 |  | 0.8 |  | 0.8 | 0.3 | 1.0 | 14.2 |
| Allen Graves (TOR) | 98% | 17.7<br><sub>9,10,7,14,16</sub> | 5.9<br><sub>7,3,0,5,3</sub> |  | 3.2<br><sub>4,0,0,1,2</sub> |  | 1.1<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.6 | 0.5 | 10.2 |
| Alijah Martin (TOR) | 88% | 16.6<br><sub>-,16,6,9,31</sub> | 7.6<br><sub>-,5,2,6,27</sub> |  | 2.6<br><sub>-,2,2,1,4</sub> |  | 1.5<br><sub>-,4,0,0,1</sub> |  | 0.8<br><sub>-,1,0,0,6</sub> |  | 0.7 | 0.3 | 1.3 | 11.7 |
| Kevin McCullar Jr. (TOR) | 23% | 11.6<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.1 | 0.6 | 7.2 |
| Kyle Anderson (TOR) | 63% | 11.2<br><sub>-,4,8,4,-</sub> | 3.4<br><sub>-,2,2,2,-</sub> |  | 2.2<br><sub>-,3,0,0,-</sub> |  | 2.0<br><sub>-,3,0,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.4 | 0.7 | 7.6 |
| Trayce Jackson-Davis (TOR) | 72% | 9.1<br><sub>1,9,2,4,-</sub> | 3.6<br><sub>0,5,0,1,-</sub> |  | 3.2<br><sub>0,5,0,0,-</sub> |  | 0.7<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.6 | 0.5 | 7.4 |
| Jaden Bradley (TOR) | 71% | 8.0<br><sub>-,4,-,4,8</sub> | 3.4<br><sub>-,3,-,2,3</sub> |  | 1.4<br><sub>-,1,-,1,0</sub> |  | 1.0<br><sub>-,2,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 5.7 |

</details>

<details><summary>if Scottie Barnes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 31.5<br><sub>28,26,38,33,31</sub> | 14.7<br><sub>18,27,18,10,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.6 | 2.8 | 27.7 |
| Ty Jerome (MEM) | 98% | 28.7<br><sub>24,-,37,29,28</sub> | 21.8<br><sub>10,-,40,23,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,-,5,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.8<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 2.7 | 29.9 |
| Cedric Coward (MEM) | 98% | 26.9<br><sub>27,23,31,33,23</sub> | 13.5<br><sub>17,10,10,23,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.4 | 1.9 | 21.9 |
| Jaylen Wells (MEM) | 98% | 26.0<br><sub>25,22,34,21,25</sub> | 10.3<br><sub>10,4,16,0,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>0,0,3,3,0</sub> |  | 1.4<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.1 | 14.4 |
| Jerami Grant (MEM) | 98% | 22.5<br><sub>27,23,24,24,22</sub> | 10.4<br><sub>2,14,11,11,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,1,2,2,2</sub> |  | 1.2<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.5 | 1.5 | 14.0 |
| Zach Edey (MEM) | 98% | 20.8<br><sub>19,18,19,25,20</sub> | 8.8<br><sub>13,4,6,11,14</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.4 | 1.5 | 17.1 |
| Javon Small (MEM) | 91% | 19.5<br><sub>-,20,-,-,21</sub> | 8.8<br><sub>-,7,-,-,10</sub> |  | 2.7<br><sub>-,1,-,-,4</sub> |  | 2.8<br><sub>-,5,-,-,2</sub> |  | 1.0<br><sub>-,2,-,-,1</sub> |  | 0.8 | 0.2 | 1.6 | 14.3 |
| Cam Spencer (MEM) | 98% | 18.0<br><sub>23,25,19,24,19</sub> | 7.1<br><sub>8,10,13,7,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>8,13,7,9,0</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.1 | 13.1 |
| Kris Murray (MEM) | 80% | 12.2<br><sub>3,21,19,15,13</sub> | 3.1<br><sub>0,2,0,5,2</sub> |  | 1.8<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 5.6 |
| GG Jackson (MEM) | 72% | 11.6<br><sub>21,21,16,7,-</sub> | 6.2<br><sub>12,21,6,1,-</sub> |  | 2.1<br><sub>7,3,0,2,-</sub> |  | 0.6<br><sub>2,2,1,0,-</sub> |  | 0.5<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.0 | 9.0 |
| Quinten Post (MEM) | 91% | 11.6<br><sub>7,-,-,11,15</sub> | 4.4<br><sub>10,-,-,2,0</sub> |  | 2.1<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.0 |
| Olivier-Maxence Prosper (MEM) | 63% | 9.8<br><sub>3,4,-,7,11</sub> | 4.7<br><sub>4,2,-,4,2</sub> |  | 1.9<br><sub>1,1,-,3,3</sub> |  | 0.4<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.0 |
| Jahmai Mashack (MEM) | 52% | 7.7<br><sub>-,4,-,-,4</sub> | 2.5<br><sub>-,2,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,1,-,-,2</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.7 | 4.3 |
| Taylor Hendricks (MEM) | 58% | 7.3<br><sub>3,4,-,-,4</sub> | 3.1<br><sub>0,6,-,-,4</sub> |  | 1.4<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Carson Cooper (MEM) | 48% | 5.8<br><sub>-,3,-,-,-</sub> | 2.5<br><sub>-,1,-,-,-</sub> |  | 2.4<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.3 | 1.0 | 5.6 |
| Scottie Barnes (TOR) | 100% | 35.0<br><sub>39,36,38,32,-</sub> | 25.9<br><sub>41,29,22,17,-</sub> | 23.5 · – | 7.7<br><sub>5,6,15,6,-</sub> | 7.5 | 7.3<br><sub>5,5,8,6,-</sub> | 5.5 | 0.8<br><sub>1,0,0,1,-</sub> |  | 1.8 | 1.3 | 3.6 | 40.9 |
| RJ Barrett (TOR) | 98% | 34.8<br><sub>34,32,37,33,37</sub> | 25.7<br><sub>9,22,26,22,27</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.7<br><sub>3,10,6,5,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.6<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,4,2,3,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.5 | 2.8 | 37.0 |
| Ja'Kobe Walter (TOR) | 98% | 31.0<br><sub>32,33,35,27,29</sub> | 13.3<br><sub>9,11,10,8,7</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>3,4,6,1,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.3<br><sub>1,2,5,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.2<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.7 | 0.4 | 1.1 | 19.7 |
| Jamal Shead (TOR) | 98% | 28.2<br><sub>23,25,20,20,34</sub> | 9.1<br><sub>2,9,6,3,10</sub> |  | 2.4<br><sub>1,2,1,3,3</sub> |  | 7.5<br><sub>8,6,6,6,16</sub> |  | 1.1<br><sub>0,2,0,1,1</sub> |  | 1.4 | 0.2 | 2.1 | 19.1 |
| Jakob Poeltl (TOR) | 86% | 25.1<br><sub>23,-,-,19,31</sub> | 11.3<br><sub>12,-,-,8,19</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 7.9<br><sub>11,-,-,5,11</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>3,-,-,1,1</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.0 | 1.2 | 1.5 | 21.2 |
| Jamison Battle (TOR) | 98% | 21.0<br><sub>19,17,21,19,21</sub> | 9.1<br><sub>2,20,12,9,6</sub> |  | 2.9<br><sub>0,5,0,1,2</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.5<br><sub>0,4,4,2,1</sub> |  | 0.5 | 0.2 | 0.7 | 13.0 |
| Malachi Smith (TOR) | 88% | 19.6 | 6.9 |  | 3.2 |  | 2.6 |  | 0.7 |  | 0.8 | 0.3 | 0.8 | 12.7 |
| Alijah Martin (TOR) | 88% | 18.2<br><sub>-,16,6,9,31</sub> | 8.3<br><sub>-,5,2,6,27</sub> |  | 2.7<br><sub>-,2,2,1,4</sub> |  | 1.6<br><sub>-,4,0,0,1</sub> |  | 0.9<br><sub>-,1,0,0,6</sub> |  | 0.8 | 0.4 | 1.2 | 12.7 |
| Allen Graves (TOR) | 98% | 16.4<br><sub>9,10,7,14,16</sub> | 5.3<br><sub>7,3,0,5,3</sub> |  | 3.0<br><sub>4,0,0,1,2</sub> |  | 0.9<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.6 | 0.5 | 9.2 |
| Kevin McCullar Jr. (TOR) | 23% | 10.8<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.6 | 6.5 |
| Kyle Anderson (TOR) | 63% | 9.7<br><sub>-,4,8,4,-</sub> | 2.9<br><sub>-,2,2,2,-</sub> |  | 1.9<br><sub>-,3,0,0,-</sub> |  | 1.7<br><sub>-,3,0,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.4 | 0.6 | 6.4 |
| Jaden Bradley (TOR) | 71% | 8.8<br><sub>-,4,-,4,8</sub> | 3.6<br><sub>-,3,-,2,3</sub> |  | 1.4<br><sub>-,1,-,1,0</sub> |  | 1.1<br><sub>-,2,-,0,1</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.7 | 0.2 | 0.6 | 6.2 |
| Trayce Jackson-Davis (TOR) | 72% | 8.4<br><sub>1,9,2,4,-</sub> | 3.4<br><sub>0,5,0,1,-</sub> |  | 2.9<br><sub>0,5,0,0,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.6 | 0.4 | 6.9 |

</details>

<details><summary>if Collin Murray-Boyles plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 31.5<br><sub>28,26,38,33,31</sub> | 14.7<br><sub>18,27,18,10,8</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.6 | 2.8 | 27.6 |
| Ty Jerome (MEM) | 98% | 28.7<br><sub>24,-,37,29,28</sub> | 21.9<br><sub>10,-,40,23,21</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,-,5,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.8<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.3 | 2.7 | 30.0 |
| Cedric Coward (MEM) | 98% | 27.0<br><sub>27,23,31,33,23</sub> | 13.4<br><sub>17,10,10,23,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.4 | 1.9 | 21.9 |
| Jaylen Wells (MEM) | 98% | 25.9<br><sub>25,22,34,21,25</sub> | 10.3<br><sub>10,4,16,0,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>0,0,3,3,0</sub> |  | 1.4<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.1 | 14.3 |
| Jerami Grant (MEM) | 98% | 22.5<br><sub>27,23,24,24,22</sub> | 10.3<br><sub>2,14,11,11,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>3,1,2,2,2</sub> |  | 1.2<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.5 | 1.5 | 13.9 |
| Zach Edey (MEM) | 98% | 20.7<br><sub>19,18,19,25,20</sub> | 8.8<br><sub>13,4,6,11,14</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.4 | 1.5 | 17.1 |
| Javon Small (MEM) | 91% | 19.4<br><sub>-,20,-,-,21</sub> | 8.7<br><sub>-,7,-,-,10</sub> |  | 2.7<br><sub>-,1,-,-,4</sub> |  | 2.8<br><sub>-,5,-,-,2</sub> |  | 1.0<br><sub>-,2,-,-,1</sub> |  | 0.7 | 0.2 | 1.6 | 14.2 |
| Cam Spencer (MEM) | 98% | 18.0<br><sub>23,25,19,24,19</sub> | 7.1<br><sub>8,10,13,7,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>8,13,7,9,0</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.1 | 13.1 |
| Kris Murray (MEM) | 80% | 12.3<br><sub>3,21,19,15,13</sub> | 3.1<br><sub>0,2,0,5,2</sub> |  | 1.9<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 5.6 |
| GG Jackson (MEM) | 72% | 11.7<br><sub>21,21,16,7,-</sub> | 6.3<br><sub>12,21,6,1,-</sub> |  | 2.2<br><sub>7,3,0,2,-</sub> |  | 0.7<br><sub>2,2,1,0,-</sub> |  | 0.5<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.0 | 9.1 |
| Quinten Post (MEM) | 91% | 11.5<br><sub>7,-,-,11,15</sub> | 4.4<br><sub>10,-,-,2,0</sub> |  | 2.1<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 6.9 |
| Olivier-Maxence Prosper (MEM) | 63% | 9.9<br><sub>3,4,-,7,11</sub> | 4.8<br><sub>4,2,-,4,2</sub> |  | 1.9<br><sub>1,1,-,3,3</sub> |  | 0.5<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.2 |
| Jahmai Mashack (MEM) | 52% | 7.7<br><sub>-,4,-,-,4</sub> | 2.5<br><sub>-,2,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,0</sub> |  | 0.8<br><sub>-,1,-,-,2</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 4.3 |
| Taylor Hendricks (MEM) | 58% | 7.3<br><sub>3,4,-,-,4</sub> | 3.1<br><sub>0,6,-,-,4</sub> |  | 1.4<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Carson Cooper (MEM) | 48% | 5.8<br><sub>-,3,-,-,-</sub> | 2.4<br><sub>-,1,-,-,-</sub> |  | 2.4<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 1.0 | 5.6 |
| RJ Barrett (TOR) | 98% | 35.9<br><sub>34,32,37,33,37</sub> | 27.4<br><sub>9,22,26,22,27</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 7.0<br><sub>3,10,6,5,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 5.6<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>1,4,2,3,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.6 | 3.3 | 40.0 |
| Ja'Kobe Walter (TOR) | 98% | 31.9<br><sub>32,33,35,27,29</sub> | 14.8<br><sub>9,11,10,8,7</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>3,4,6,1,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>1,2,5,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.7 | 0.4 | 1.3 | 21.8 |
| Collin Murray-Boyles (TOR) | 100% | 30.3<br><sub>23,20,28,23,34</sub> | 15.8<br><sub>15,4,18,13,19</sub> | 12.5 · – | 7.2<br><sub>5,3,7,3,7</sub> | 6.5 | 2.9<br><sub>1,1,0,2,2</sub> | 1.5 | 0.4<br><sub>1,0,1,1,0</sub> |  | 1.4 | 1.4 | 2.2 | 25.8 |
| Jamal Shead (TOR) | 98% | 29.0<br><sub>23,25,20,20,34</sub> | 10.1<br><sub>2,9,6,3,10</sub> |  | 2.5<br><sub>1,2,1,3,3</sub> |  | 8.5<br><sub>8,6,6,6,16</sub> |  | 1.2<br><sub>0,2,0,1,1</sub> |  | 1.4 | 0.2 | 2.4 | 21.1 |
| Jakob Poeltl (TOR) | 86% | 25.3<br><sub>23,-,-,19,31</sub> | 12.2<br><sub>12,-,-,8,19</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 8.0<br><sub>11,-,-,5,11</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>3,-,-,1,1</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.0 | 1.2 | 1.7 | 22.4 |
| Jamison Battle (TOR) | 98% | 22.6<br><sub>19,17,21,19,21</sub> | 10.3<br><sub>2,20,12,9,6</sub> |  | 3.2<br><sub>0,5,0,1,2</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 1.7<br><sub>0,4,4,2,1</sub> |  | 0.5 | 0.2 | 0.8 | 14.7 |
| Malachi Smith (TOR) | 88% | 21.0 | 7.9 |  | 3.4 |  | 3.4 |  | 0.8 |  | 0.8 | 0.3 | 1.0 | 14.6 |
| Alijah Martin (TOR) | 88% | 20.2<br><sub>-,16,6,9,31</sub> | 9.0<br><sub>-,5,2,6,27</sub> |  | 3.1<br><sub>-,2,2,1,4</sub> |  | 2.0<br><sub>-,4,0,0,1</sub> |  | 1.0<br><sub>-,1,0,0,6</sub> |  | 0.9 | 0.4 | 1.6 | 14.1 |
| Allen Graves (TOR) | 98% | 17.1<br><sub>9,10,7,14,16</sub> | 5.9<br><sub>7,3,0,5,3</sub> |  | 3.1<br><sub>4,0,0,1,2</sub> |  | 1.0<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.6 | 0.5 | 0.5 | 10.0 |
| Kevin McCullar Jr. (TOR) | 23% | 11.7<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.1 | 0.7 | 7.3 |
| Kyle Anderson (TOR) | 63% | 11.6<br><sub>-,4,8,4,-</sub> | 3.6<br><sub>-,2,2,2,-</sub> |  | 2.3<br><sub>-,3,0,0,-</sub> |  | 2.1<br><sub>-,3,0,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.4 | 0.7 | 8.1 |
| Jaden Bradley (TOR) | 71% | 9.2<br><sub>-,4,-,4,8</sub> | 3.7<br><sub>-,3,-,2,3</sub> |  | 1.5<br><sub>-,1,-,1,0</sub> |  | 1.1<br><sub>-,2,-,0,1</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.8 | 0.2 | 0.7 | 6.3 |
| Trayce Jackson-Davis (TOR) | 72% | 9.0<br><sub>1,9,2,4,-</sub> | 3.7<br><sub>0,5,0,1,-</sub> |  | 3.2<br><sub>0,5,0,0,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.6 | 0.5 | 7.5 |

</details>


### IND @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.4–117.0 | IND 34% | 2.91 / 1.52 | DAL -5.5 | 228.5 | DAL -4.5 covers 54%; o226.5 54% |
| Expected (weighted by chance each plays) | 112.2–117.6 | IND 34% | 2.90 / 1.53 | DAL -5.5 | 229.5 | DAL -4.5 covers 54%; o226.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| T.J. McConnell (IND) | Questionable | 55% | 12.2 | 6.5 | 1.8 | 3.7 | 0.1 | 0.7 | 0.1 | 0.8 | 11.9 | small |
| Morez Johnson Jr. (DAL) | Questionable | 55% | 14.7 | 6.0 | 3.3 | 1.4 | 0.3 | 0.5 | 0.1 | 0.8 | 10.7 | small |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 80% | 33.1<br><sub>30,35,-,38,31</sub> | 18.5<br><sub>22,23,-,22,9</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>2,3,-,2,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 8.9<br><sub>9,4,-,5,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>5,4,-,2,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.2 | 2.5 | 30.5 |
| Pascal Siakam | 86% | 32.8<br><sub>29,36,-,30,32</sub> | 23.8<br><sub>13,17,-,20,23</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>5,5,-,4,2</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>4,5,-,2,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,0,-,2,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 2.5 | 35.0 |
| Aaron Nesmith | 86% | 27.3<br><sub>21,30,-,30,27</sub> | 14.5<br><sub>9,11,-,16,8</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>3,3,-,2,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,4,-,2,1</sub> |  | 1.9<br><sub>1,0,-,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.4 | 1.5 | 20.3 |
| Jarace Walker | 98% | 24.0<br><sub>28,20,45,17,20</sub> | 10.3<br><sub>14,6,15,2,9</sub> |  | 5.5<br><sub>6,6,7,8,5</sub> |  | 2.6<br><sub>4,3,3,1,2</sub> |  | 1.2<br><sub>3,2,1,0,1</sub> |  | 0.8 | 0.4 | 1.6 | 18.5 |
| Quenton Jackson | 98% | 21.9<br><sub>24,24,35,22,17</sub> | 10.7<br><sub>24,12,20,13,6</sub> |  | 3.2<br><sub>4,3,7,7,4</sub> |  | 3.6<br><sub>1,2,3,2,1</sub> |  | 0.9<br><sub>2,3,1,3,0</sub> |  | 1.0 | 0.2 | 1.4 | 17.5 |
| Kelly Oubre Jr. | 67% | 21.3<br><sub>22,20,-,-,16</sub> | 8.7<br><sub>10,11,-,-,2</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,2,-,-,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>1,1,-,-,0</sub> |  | 0.8<br><sub>1,2,-,-,0</sub> |  | 0.9 | 0.4 | 0.9 | 13.2 |
| Ivica Zubac | 58% | 20.9<br><sub>-,-,-,19,19</sub> | 9.7<br><sub>-,-,-,1,10</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 8.3<br><sub>-,-,-,4,12</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>-,-,-,2,5</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.7 | 1.3 | 19.8 |
| Obi Toppin | 64% | 20.6<br><sub>-,-,-,19,22</sub> | 12.2<br><sub>-,-,-,11,10</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>-,-,-,5,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>-,-,-,1,2</sub> |  | 1.5<br><sub>-,-,-,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.3 | 1.2 | 19.1 |
| Jay Huff | 96% | 16.9<br><sub>19,17,40,14,10</sub> | 7.0<br><sub>13,0,22,6,0</sub> |  | 3.5<br><sub>1,3,8,3,3</sub> |  | 1.3<br><sub>0,0,2,1,0</sub> |  | 0.8<br><sub>3,0,0,2,0</sub> |  | 0.4 | 1.1 | 0.8 | 11.8 |
| Braden Smith | 88% | 16.3<br><sub>12,1,42,24,12</sub> | 5.8<br><sub>1,0,19,10,0</sub> |  | 1.6<br><sub>0,0,4,1,0</sub> |  | 3.1<br><sub>1,0,10,5,2</sub> |  | 0.3<br><sub>0,0,2,0,0</sub> |  | 0.8 | 0.3 | 1.0 | 10.6 |
| Kobe Brown | 72% | 14.8<br><sub>20,15,38,7,-</sub> | 5.3<br><sub>9,3,16,0,-</sub> |  | 2.8<br><sub>6,1,6,1,-</sub> |  | 1.4<br><sub>4,1,1,0,-</sub> |  | 0.6<br><sub>0,1,2,0,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.5 |
| Larry Nance Jr. | 91% | 14.3<br><sub>18,26,-,14,13</sub> | 4.5<br><sub>6,4,-,4,15</sub> |  | 3.1<br><sub>2,6,-,4,2</sub> |  | 1.0<br><sub>1,1,-,1,1</sub> |  | 0.5<br><sub>2,1,-,0,5</sub> |  | 0.7 | 0.2 | 0.6 | 8.6 |
| Jalen Slawson | 93% | 14.3<br><sub>18,18,41,6,12</sub> | 4.2<br><sub>4,3,12,2,4</sub> |  | 2.8<br><sub>4,5,7,2,1</sub> |  | 1.4<br><sub>1,0,3,1,2</sub> |  | 0.3<br><sub>0,0,2,0,0</sub> |  | 0.8 | 0.6 | 0.8 | 8.4 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 34.0<br><sub>39,40,40,33,28</sub> | 24.6<br><sub>33,17,19,21,25</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>9,4,10,10,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.1<br><sub>6,6,5,7,12</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.9 | 2.6 | 38.0 |
| Kyrie Irving | 98% | 33.1<br><sub>35,-,36,28,29</sub> | 22.8<br><sub>35,-,29,14,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,-,7,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.3<br><sub>9,-,5,2,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>5,-,5,0,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3 | 0.5 | 2.1 | 31.7 |
| P.J. Washington | 98% | 33.1<br><sub>34,38,39,33,25</sub> | 14.3<br><sub>3,12,21,26,6</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 7.7<br><sub>10,5,10,6,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,3,1,0</sub> |  | 1.8<br><sub>1,2,3,6,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.9 | 1.5 | 23.7 |
| Naji Marshall | 88% | 24.2<br><sub>-,24,26,25,15</sub> | 12.5<br><sub>-,5,22,7,8</sub> |  | 3.6<br><sub>-,2,5,1,1</sub> |  | 3.5<br><sub>-,7,3,5,2</sub> |  | 0.9<br><sub>-,0,3,0,1</sub> |  | 1.0 | 0.1 | 1.5 | 19.6 |
| Daniel Gafford | 98% | 21.9<br><sub>29,26,18,18,19</sub> | 10.7<br><sub>18,20,2,7,18</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>7,7,4,1,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,0,1,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.6 | 1.1 | 19.2 |
| Zaccharie Risacher | 96% | 21.4<br><sub>28,19,18,21,16</sub> | 6.8<br><sub>12,0,2,4,11</sub> |  | 4.6<br><sub>6,5,1,4,6</sub> |  | 1.2<br><sub>3,1,2,1,1</sub> |  | 0.7<br><sub>3,0,0,0,1</sub> |  | 0.9 | 0.9 | 0.8 | 12.6 |
| Max Christie | 98% | 16.8<br><sub>18,8,-,9,17</sub> | 6.0<br><sub>2,0,-,0,5</sub> |  | 2.1<br><sub>1,2,-,1,2</sub> |  | 1.1<br><sub>0,0,-,1,0</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.2 | 0.7 | 9.2 |
| Caleb Martin | 97% | 16.7<br><sub>25,21,20,11,19</sub> | 4.4<br><sub>8,5,0,0,2</sub> |  | 2.7<br><sub>0,6,3,0,2</sub> |  | 1.2<br><sub>0,0,2,0,2</sub> |  | 0.3<br><sub>2,1,0,0,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.2 |
| Walter Clayton Jr. | 91% | 16.3<br><sub>9,24,21,23,16</sub> | 6.5<br><sub>3,20,8,12,5</sub> |  | 2.7<br><sub>2,1,6,4,4</sub> |  | 3.0<br><sub>1,2,5,2,6</sub> |  | 0.7<br><sub>1,4,2,1,1</sub> |  | 0.6 | 0.2 | 1.0 | 12.2 |
| Santi Aldama | 97% | 15.8<br><sub>-,-,-,13,15</sub> | 6.6<br><sub>-,-,-,8,12</sub> |  | 4.0<br><sub>-,-,-,9,2</sub> |  | 1.4<br><sub>-,-,-,1,0</sub> |  | 0.7<br><sub>-,-,-,0,2</sub> |  | 0.6 | 0.4 | 0.7 | 12.0 |
| Marcus Sasser | 80% | 12.2<br><sub>7,19,5,-,9</sub> | 4.2<br><sub>0,4,0,-,4</sub> |  | 1.1<br><sub>0,1,1,-,0</sub> |  | 1.5<br><sub>1,1,2,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.8 |
| Moussa Cisse | 67% | 7.3<br><sub>-,2,-,1,5</sub> | 2.7<br><sub>-,0,-,0,2</sub> |  | 3.0<br><sub>-,0,-,0,1</sub> |  | 0.2<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 6.0 |
| Tobi Lawal | 66% | 6.7<br><sub>-,2,-,1,5</sub> | 2.4<br><sub>-,2,-,0,2</sub> |  | 2.4<br><sub>-,0,-,0,0</sub> |  | 0.6<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.2 | 0.3 | 5.4 |
| Jett Howard | 64% | 6.0<br><sub>-,2,-,1,3</sub> | 2.5<br><sub>-,2,-,0,5</sub> |  | 0.8<br><sub>-,0,-,0,1</sub> |  | 0.4<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,1</sub> |  | 0.1 | 0.1 | 0.2 | 3.6 |

</details>


### DEN @ HOU
Out: Steven Adams (HOU), Clint Capela (HOU), Oscar Tshiebwe (HOU), Julian Strawther (DEN)

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 91% | 35.8<br><sub>38,37,39,28,34</sub> | 23.8<br><sub>23,39,35,14,16</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>1,8,5,5,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 5.7<br><sub>6,5,6,7,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>5,7,4,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.5 | 2.6 | 33.9 |
| Nikola Jokic | 91% | 35.4<br><sub>34,37,36,30,36</sub> | 25.5<br><sub>21,18,26,32,19</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 11.3<br><sub>13,7,9,10,13</sub> | 10.5<br><sub>o 52% · u 48%</sub> | 9.0<br><sub>10,10,8,11,8</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,0,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.8 | 3.7 | 45.8 |
| Christian Braun | 91% | 31.5<br><sub>36,37,37,28,29</sub> | 12.0<br><sub>15,31,14,11,6</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>0,3,3,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>4,1,3,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>3,7,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 1.0 | 18.1 |
| Cameron Johnson | 91% | 28.4<br><sub>-,34,34,30,29</sub> | 11.5<br><sub>-,12,7,12,18</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>-,9,4,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>-,3,2,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>-,2,1,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 1.1 | 17.0 |
| Aaron Gordon | 91% | 27.6<br><sub>31,29,30,25,27</sub> | 12.3<br><sub>15,15,5,17,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>11,4,6,1,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>3,5,2,0,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>2,2,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.3 | 19.3 |
| DeMar DeRozan | 74% | 23.5<br><sub>26,24,20,-,22</sub> | 11.9<br><sub>6,3,9,-,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,1,0,-,1</sub> |  | 2.8<br><sub>5,5,1,-,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.4<br><sub>0,0,0,-,0</sub> | 0.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.3 | 1.2 | 16.8 |
| Spencer Jones | 52% | 17.9<br><sub>-,-,-,-,21</sub> | 6.1<br><sub>-,-,-,-,13</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>-,-,-,-,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,3</sub> |  | 0.6 | 0.4 | 1.1 | 10.6 |
| Trevon Brazile | 97% | 16.5<br><sub>32,19,18,23,14</sub> | 5.2<br><sub>11,6,6,6,3</sub> |  | 3.9<br><sub>8,3,5,7,4</sub> |  | 0.8<br><sub>0,1,1,1,2</sub> |  | 0.5<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.3 | 0.7 | 9.9 |
| Tyus Jones | 96% | 11.9<br><sub>11,11,8,18,13</sub> | 3.3<br><sub>5,3,2,6,3</sub> |  | 1.0<br><sub>0,0,0,1,4</sub> |  | 1.9<br><sub>1,0,1,8,4</sub> |  | 0.3<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.1 | 0.5 | 6.2 |
| Marvin Bagley III | 98% | 11.9<br><sub>19,11,12,14,12</sub> | 5.8<br><sub>8,0,6,10,10</sub> |  | 3.3<br><sub>5,5,4,2,3</sub> |  | 0.6<br><sub>1,0,0,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 9.6 |
| Bryce Hopkins | 67% | 9.4<br><sub>14,-,-,28,3</sub> | 3.0<br><sub>0,-,-,18,3</sub> |  | 1.4<br><sub>2,-,-,4,1</sub> |  | 0.4<br><sub>0,-,-,1,0</sub> |  | 0.1<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Cam Whitmore | 58% | 6.9<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Alpha Diallo | 64% | 6.5<br><sub>-,-,6,4,-</sub> | 3.0<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Zeke Nnaji | 43% | 6.2<br><sub>-,-,-,4,-</sub> | 2.0<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.6 |
| Ryan Nembhard | 52% | 6.1<br><sub>-,-,-,4,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.0 |
| DaRon Holmes II | 48% | 5.5<br><sub>-,-,-,4,-</sub> | 2.4<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 3.8 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.8<br><sub>35,33,36,35,39</sub> | 16.9<br><sub>22,30,14,11,15</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.6<br><sub>3,9,10,4,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,5,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,6,4,2,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 1.1 | 1.2 | 26.5 |
| Kevin Durant | 98% | 36.1<br><sub>37,27,33,35,38</sub> | 23.1<br><sub>28,14,12,21,21</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>5,3,3,5,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>1,4,3,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 1.1 | 2.9 | 34.0 |
| Amen Thompson | 98% | 35.8<br><sub>39,28,25,32,39</sub> | 16.9<br><sub>15,8,14,11,17</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>3,3,3,8,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>6,1,3,1,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.9 | 1.9 | 28.8 |
| Alperen Sengun | 84% | 35.7<br><sub>-,33,38,39,32</sub> | 19.8<br><sub>-,16,26,17,15</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 10.1<br><sub>-,9,7,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>-,9,10,10,5</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 0.7<br><sub>-,0,1,0,1</sub> | 0.5<br><sub>o 43% · u 57%</sub> | 1.2 | 1.3 | 2.8 | 36.7 |
| Fred VanVleet | 88% | 32.7<br><sub>33,-,27,30,31</sub> | 13.2<br><sub>16,-,8,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>5,-,2,3,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.1<br><sub>6,-,9,3,4</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,-,2,4,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.4 | 1.4 | 21.8 |
| Tari Eason | 98% | 25.5<br><sub>26,19,27,24,23</sub> | 10.5<br><sub>11,8,13,9,2</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>13,3,4,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,3,1,2</sub> |  | 1.2<br><sub>0,2,3,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.8 | 1.0 | 18.2 |
| Marcus Smart | 88% | 22.4<br><sub>17,36,20,18,20</sub> | 8.3<br><sub>8,24,8,4,5</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>2,5,4,1,2</sub> |  | 2.4<br><sub>4,3,4,1,0</sub> |  | 1.2<br><sub>0,7,2,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.4 | 1.2 | 13.2 |
| Reed Sheppard | 76% | 20.8<br><sub>-,-,17,21,13</sub> | 9.5<br><sub>-,-,8,14,6</sub> |  | 1.9<br><sub>-,-,1,2,0</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.7<br><sub>-,-,2,3,2</sub> |  | 1.2 | 0.5 | 1.0 | 14.0 |
| Bogdan Bogdanovic | 96% | 9.7<br><sub>11,19,5,5,2</sub> | 3.5<br><sub>6,4,0,0,0</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Isaiah Crawford | 52% | 7.1<br><sub>-,19,2,-,-</sub> | 2.5<br><sub>-,8,0,-,-</sub> |  | 1.0<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.8 |
| Jae'Sean Tate | 52% | 6.1<br><sub>-,6,2,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,3,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Bruce Thornton | 52% | 5.9<br><sub>-,6,2,-,-</sub> | 2.2<br><sub>-,5,2,-,-</sub> |  | 1.0<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.7 |

</details>


### SAS @ PHX
Out: Mark Williams (PHX), Tobias Harris (SAS), Devin Vassell (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.4–109.1 | SAS 72% | 1.38 / 3.64 | PHX +8.5 | 226.5 | PHX +8.5 covers 50%; o226.5 50% |
| Expected (weighted by chance each plays) | 117.1–109.4 | SAS 71% | 1.41 / 3.47 | PHX +8.5 | 226.5 | PHX +8.5 covers 51%; o226.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Goodwin (PHX) | Questionable | 55% | 14.0 | 5.1 | 2.9 | 1.4 | 0.7 | 0.9 | 0.1 | 0.5 | 9.4 | small |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 33.7<br><sub>39,27,36,28,28</sub> | 18.5<br><sub>25,17,21,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>7,7,5,2,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>6,8,0,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1 | 0.3 | 2.1 | 28.1 |
| Victor Wembanyama | 98% | 32.9<br><sub>34,24,34,26,24</sub> | 27.7<br><sub>43,12,52,30,29</sub> | 27.5 · –<br><sub>o 47% · u 53%</sub> | 12.5<br><sub>7,11,24,14,7</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,5,2,2,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>3,0,1,4,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 3.3 | 2.8 | 43.5 |
| Stephon Castle | 98% | 32.5<br><sub>22,26,35,28,24</sub> | 18.1<br><sub>0,16,17,19,14</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>5,5,10,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 5.9<br><sub>4,4,3,7,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,2,2,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 3.0 | 29.6 |
| De'Aaron Fox | 98% | 32.2<br><sub>35,22,33,26,22</sub> | 16.2<br><sub>22,12,10,9,8</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>8,2,3,2,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>7,3,4,4,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>0,1,0,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.4 | 2.3 | 25.4 |
| Julian Champagnie | 98% | 26.8<br><sub>27,22,21,22,21</sub> | 9.3<br><sub>12,8,0,8,14</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>3,6,4,7,4</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>1,0,3,2,0</sub> |  | 1.7<br><sub>3,2,0,2,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.4 | 0.7 | 15.4 |
| Keldon Johnson | 98% | 26.1<br><sub>24,27,19,27,27</sub> | 10.7<br><sub>2,15,4,3,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>6,7,5,6,7</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>0,1,2,6,4</sub> |  | 0.9<br><sub>0,1,0,0,0</sub> |  | 0.8 | 0.2 | 1.2 | 18.0 |
| Luke Kornet | 98% | 17.9<br><sub>14,17,14,18,15</sub> | 4.4<br><sub>2,8,2,2,6</sub> |  | 5.3<br><sub>8,5,1,6,4</sub> |  | 1.1<br><sub>0,2,2,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.7 | 10.8 |
| Harrison Barnes | 80% | 17.5<br><sub>-,21,13,19,19</sub> | 5.5<br><sub>-,13,4,13,5</sub> |  | 2.0<br><sub>-,0,2,1,3</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.8<br><sub>-,3,1,2,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.3 |
| Carter Bryant | 86% | 15.1<br><sub>11,14,-,3,17</sub> | 4.7<br><sub>6,3,-,0,6</sub> |  | 2.4<br><sub>0,0,-,0,4</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.6<br><sub>2,1,-,0,2</sub> |  | 0.4 | 0.4 | 0.7 | 7.9 |
| Jordan McLaughlin | 63% | 13.4<br><sub>-,8,-,8,12</sub> | 4.2<br><sub>-,0,-,2,3</sub> |  | 1.6<br><sub>-,1,-,2,0</sub> |  | 1.6<br><sub>-,3,-,1,0</sub> |  | 0.5<br><sub>-,0,-,0,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.4 |
| Tarris Reed Jr. | 64% | 9.9<br><sub>-,7,-,3,9</sub> | 3.4<br><sub>-,4,-,0,2</sub> |  | 4.4<br><sub>-,7,-,1,3</sub> |  | 0.4<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.4 | 0.9 | 8.1 |
| David Jones Garcia | 58% | 7.2<br><sub>-,-,-,3,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 36.2<br><sub>39,35,34,34,39</sub> | 25.4<br><sub>20,26,33,30,24</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,3,1,1,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>5,5,2,8,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.3 | 3.0 | 35.0 |
| Dillon Brooks | 98% | 33.0<br><sub>21,34,35,29,37</sub> | 17.2<br><sub>22,18,15,24,11</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>1,8,6,1,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>4,2,0,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 1.5 | 23.4 |
| Miles Bridges | 98% | 32.4<br><sub>37,35,31,31,31</sub> | 15.0<br><sub>24,21,18,18,13</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>10,6,7,13,10</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>2,3,5,5,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>2,3,4,3,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.5 | 1.3 | 24.9 |
| Jalen Green | 98% | 31.5<br><sub>25,36,32,24,34</sub> | 16.1<br><sub>2,11,22,6,16</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>2,8,2,0,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>2,8,2,3,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>0,0,2,0,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.4 | 2.5 | 23.8 |
| Collin Gillespie | 98% | 24.6<br><sub>33,24,23,24,20</sub> | 9.1<br><sub>16,3,2,6,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.6<br><sub>10,2,2,2,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>4,1,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 1.1 | 15.9 |
| Oso Ighodaro | 98% | 23.9<br><sub>21,24,23,24,23</sub> | 6.8<br><sub>2,14,9,2,4</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 5.5<br><sub>9,2,7,5,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>5,2,7,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.1 | 15.4 |
| Ryan Dunn | 98% | 18.3<br><sub>11,10,18,25,23</sub> | 5.2<br><sub>5,5,2,11,8</sub> |  | 3.8<br><sub>3,3,6,3,5</sub> |  | 1.2<br><sub>1,1,2,3,3</sub> |  | 0.6<br><sub>1,1,0,1,2</sub> |  | 0.7 | 0.5 | 0.5 | 10.3 |
| Khaman Maluach | 98% | 17.9<br><sub>17,13,16,22,18</sub> | 5.9<br><sub>9,5,6,8,8</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>6,2,6,6,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>0,0,2,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.9 | 12.1 |
| Luke Kennard | 98% | 17.3<br><sub>12,18,14,21,14</sub> | 6.2<br><sub>9,6,0,12,11</sub> |  | 2.0<br><sub>1,2,0,1,1</sub> |  | 1.7<br><sub>2,1,1,5,2</sub> |  | 0.8<br><sub>1,2,0,3,3</sub> |  | 0.5 | 0.1 | 0.6 | 9.9 |
| Drew Timme | 16% | 8.0 | 2.9 |  | 1.3 |  | 0.6 |  | 0.2 |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Rasheer Fleming | 47% | 7.6<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Pat Spencer | 63% | 7.0<br><sub>-,-,3,2,-</sub> | 2.4<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 1.1<br><sub>-,-,2,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.0 | 0.5 | 4.4 |
| Duop Reath | 63% | 6.9<br><sub>-,-,7,2,-</sub> | 2.6<br><sub>-,-,7,0,-</sub> |  | 1.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea | 52% | 6.6<br><sub>-,-,3,2,-</sub> | 2.5<br><sub>-,-,3,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Koa Peat | 52% | 6.1<br><sub>-,-,3,2,-</sub> | 2.1<br><sub>-,-,2,0,-</sub> |  | 1.5<br><sub>-,-,1,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.0 |

</details>


### NOP @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Will Richard (GSW), Yves Missi (NOP), Trey Murphy III (NOP), Trendon Watford (NOP), Zion Williamson (NOP)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.6–123.8 | NOP 22% | 4.64 / 1.27 | GSW -11.5 | 236.5 | GSW -11.5 covers 49%; o229.5 64% |
| Expected (weighted by chance each plays) | 112.3–124.1 | NOP 21% | 4.85 / 1.26 | GSW -11.5 | 236.5 | GSW -11.5 covers 51%; o229.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gary Payton II (GSW) | Questionable | 55% | 13.7 | 6.7 | 2.6 | 1.1 | 0.4 | 0.8 | 0.2 | 0.6 | 10.4 | small |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray | 98% | 34.7<br><sub>-,-,45,35,28</sub> | 19.6<br><sub>-,-,20,7,6</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 5.9<br><sub>-,-,8,2,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>-,-,4,4,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>-,-,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 2.0 | 0.4 | 3.4 | 32.2 |
| Saddiq Bey | 98% | 33.6<br><sub>26,36,29,31,26</sub> | 19.3<br><sub>25,18,22,17,13</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,5,4,5,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,1,3,4,3</sub> |  | 2.3<br><sub>1,2,2,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 1.6 | 27.8 |
| Jeremiah Fears | 98% | 32.8<br><sub>31,38,34,36,29</sub> | 20.0<br><sub>20,12,19,24,25</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,4,6,5,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>7,7,2,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,0,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.5 | 3.1 | 29.8 |
| Herbert Jones | 98% | 28.3<br><sub>25,28,37,14,20</sub> | 9.0<br><sub>11,9,2,0,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>3,4,5,4,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,3,1,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>1,3,0,0,0</sub> |  | 1.3 | 0.4 | 1.4 | 14.6 |
| Derik Queen | 98% | 28.3<br><sub>23,24,27,10,21</sub> | 14.3<br><sub>8,20,20,6,8</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 8.4<br><sub>8,7,9,4,5</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,5,6,1,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 1.2 | 0.8 | 2.8 | 26.8 |
| Karlo Matkovic | 96% | 27.4<br><sub>18,29,21,18,19</sub> | 11.2<br><sub>8,25,5,18,3</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>10,6,4,3,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,1,2,1,2</sub> |  | 1.4<br><sub>2,5,1,4,1</sub> |  | 0.9 | 1.1 | 1.4 | 19.1 |
| Bennedict Mathurin | 98% | 22.4<br><sub>19,13,15,7,9</sub> | 10.5<br><sub>7,4,2,2,6</sub> |  | 3.8<br><sub>1,0,5,0,0</sub> |  | 2.0<br><sub>2,0,1,0,1</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.5 | 16.3 |
| Jordan Poole | 52% | 19.0<br><sub>-,-,-,-,-</sub> | 9.7<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.3 | 1.5 | 14.1 |
| Bryce McGowens | 58% | 17.3<br><sub>15,6,-,-,3</sub> | 6.0<br><sub>3,0,-,-,0</sub> |  | 2.0<br><sub>0,1,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.7 | 0.2 | 0.7 | 9.2 |
| DeAndre Jordan | 26% | 16.0<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 5.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.7 | 0.7 | 11.1 |
| Julian Reese | 48% | 10.2<br><sub>3,-,-,-,3</sub> | 3.2<br><sub>2,-,-,-,0</sub> |  | 1.6<br><sub>1,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 5.6 |
| AJ Johnson | 47% | 9.8<br><sub>3,-,-,-,3</sub> | 3.3<br><sub>0,-,-,-,2</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.6 | 0.6 | 4.4 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 91% | 34.3<br><sub>33,37,33,32,39</sub> | 16.9<br><sub>21,17,20,9,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>5,8,3,6,7</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>6,8,2,3,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>4,2,3,2,4</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.3 | 0.3 | 1.7 | 26.6 |
| Yaxel Lendeborg | 98% | 33.9<br><sub>24,34,29,30,37</sub> | 21.3<br><sub>6,37,16,17,23</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 7.5<br><sub>1,4,5,8,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>0,6,5,6,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>1,6,2,1,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 1.0 | 3.2 | 32.8 |
| Stephen Curry | 98% | 32.9<br><sub>31,-,33,28,36</sub> | 28.2<br><sub>31,-,34,29,41</sub> | 28.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,-,6,1,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.2<br><sub>6,-,7,4,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>8,-,5,6,5</sub> | 4.5<br><sub>o 46% · u 53%</sub> | 1.2 | 0.4 | 2.7 | 37.3 |
| Draymond Green | 91% | 28.6<br><sub>32,-,17,27,34</sub> | 7.2<br><sub>2,-,4,2,2</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>9,-,2,11,13</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 0.8<br><sub>0,-,0,0,0</sub> |  | 1.1 | 0.8 | 2.4 | 19.4 |
| Georges Niang | 97% | 21.8<br><sub>19,21,22,22,25</sub> | 8.8<br><sub>11,3,13,13,11</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>5,1,4,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,2,3,3,1</sub> |  | 1.5<br><sub>3,1,1,2,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.5 | 0.2 | 1.0 | 13.3 |
| De'Anthony Melton | 98% | 21.3<br><sub>21,28,28,17,17</sub> | 9.7<br><sub>16,21,2,5,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>5,6,7,6,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>3,3,2,2,1</sub> |  | 1.4<br><sub>4,6,0,0,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.3 | 15.2 |
| Brandon Williams | 86% | 18.8<br><sub>17,25,-,21,17</sub> | 10.9<br><sub>9,17,-,10,9</sub> |  | 2.4<br><sub>2,3,-,1,0</sub> |  | 2.8<br><sub>1,3,-,4,2</sub> |  | 0.6<br><sub>0,2,-,0,0</sub> |  | 0.8 | 0.3 | 1.6 | 16.1 |
| Al Horford | 98% | 17.0<br><sub>17,22,-,18,13</sub> | 5.9<br><sub>3,9,-,8,2</sub> |  | 3.9<br><sub>2,5,-,5,5</sub> |  | 1.5<br><sub>0,2,-,1,4</sub> |  | 0.9<br><sub>1,3,-,2,0</sub> |  | 0.4 | 0.8 | 0.5 | 11.3 |
| Gui Santos | 82% | 16.4<br><sub>16,9,-,-,12</sub> | 6.9<br><sub>2,4,-,-,3</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>5,3,-,-,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>1,1,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.7 | 0.3 | 1.1 | 11.6 |
| Charles Bassey | 96% | 12.8<br><sub>9,20,23,14,11</sub> | 6.3<br><sub>6,6,19,8,8</sub> |  | 5.4<br><sub>4,10,8,7,4</sub> |  | 0.6<br><sub>1,2,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.1 | 0.7 | 12.3 |
| Graham Ike | 88% | 8.1<br><sub>-,6,7,1,-</sub> | 3.5<br><sub>-,2,0,0,-</sub> |  | 2.0<br><sub>-,2,0,1,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| LJ Cryer | 58% | 7.4<br><sub>-,2,1,1,-</sub> | 3.6<br><sub>-,0,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.0 | 0.3 | 4.9 |
| Malevy Leons | 48% | 6.8<br><sub>-,-,-,1,-</sub> | 2.1<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.3 | 3.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-09/`._
