# NBA model · Sun 15 Nov 2026 (US date)

Updated **Mon 16 Nov, 06:28 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-15/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| HOU @ WAS | player points | Alperen Sengun projected 25.2 pts vs DraftKings line 19.5 | minutes 37 vs 35 this season; scoring 0.69/min vs 0.66 this season, 0.61 last season; teammates out: Capela, Smart, VanVleet (~66 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant PR over 44.5 (45+) | HOU @ WAS | draftkings | 20.00 | 16.89 | 7.07 | 14.1% | 4.7% | 5.9% | +18.5% | +182.8% | 0.2% |
| Kevin Durant AST over 7.5 (8+) | HOU @ WAS | draftkings | 12.20 | 10.54 | 4.65 | 21.5% | 7.7% | 9.5% | +15.7% | +162.3% | 0.4% |
| Alperen Sengun PTS over 34.5 (35+) | HOU @ WAS | draftkings | 15.40 | 13.46 | 6.10 | 16.4% | 6.1% | 7.4% | +14.5% | +152.6% | 0.2% |
| UTA to win | SAS @ UTA | betfair_ex_au | 10.02 | 8.94 | 7.36 | 13.6% | 11.2% | 11.2% | +12.1% | +36.2% | 0.3% |
| Alperen Sengun PTS over 39.5 (40+) | HOU @ WAS | draftkings | 29.00 | 25.91 | 12.45 | 8.0% | 3.2% | 3.9% | +11.9% | +132.8% | 0.1% |
| Kevin Durant PR over 39.5 (40+) | HOU @ WAS | draftkings | 9.70 | 8.68 | 4.18 | 23.9% | 9.6% | 11.5% | +11.8% | +132.2% | 0.3% |
| Kevin Durant AST over 9.5 (10+) | HOU @ WAS | draftkings | 30.00 | 27.03 | 13.31 | 7.5% | 3.1% | 3.7% | +10.9% | +125.4% | 0.1% |
| Alperen Sengun PR over 49.5 (50+) | HOU @ WAS | draftkings | 19.40 | 17.70 | 8.96 | 11.2% | 4.8% | 5.7% | +9.7% | +116.4% | 0.1% |
| Alperen Sengun PR over 44.5 (45+) | HOU @ WAS | draftkings | 10.70 | 9.78 | 4.99 | 20.0% | 8.7% | 10.2% | +9.4% | +114.2% | 0.2% |
| DAL to win | DAL @ BOS | draftkings | 6.99 | 6.41 | 4.93 | 20.3% | 15.6% | 15.6% | +9.1% | +41.9% | 0.4% |
| Tari Eason REB over 11.5 (12+) | HOU @ WAS | draftkings | 15.20 | 14.20 | 7.75 | 12.9% | 6.2% | 7.0% | +7.0% | +96.1% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 5.5 (6+) | HOU @ WAS | draftkings | 3.97 | 3.76 | 2.15 | 46.5% | 23.5% | 26.6% | +5.5% | +84.5% | 0.5% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| LAL @ PHX | Mon 16 Nov 08:00 | 112.2–112.1 | LAL 50% | 2.00 / 2.00 | PHX +0.5 | 224.5 | PHX +3.5 covers 59%; o226.5 45% |
| CHA @ LAC | Mon 16 Nov 08:30 | 108.7–111.0 | CHA 44% | 2.29 / 1.77 | LAC -2.5 | 219.5 | LAC +1.5 covers 59%; o213.5 63% |
| SAS @ UTA | Mon 16 Nov 09:00 | 122.2–106.7 | SAS 86% | 1.16 / 7.33 | UTA +15.5 | 228.5 | UTA +15.5 covers 50%; o224.5 60% |
| DAL @ BOS | Mon 16 Nov 10:00 | 105.7–119.7 | DAL 16% | 6.37 / 1.19 | BOS -13.5 | 225.5 | BOS -14.5 covers 48%; o218.5 65% |
| NYK @ TOR | Mon 16 Nov 10:00 | 114.3–107.9 | NYK 67% | 1.48 / 3.07 | TOR +6.5 | 221.5 | TOR +5.5 covers 48%; o217.5 59% |
| HOU @ WAS | Mon 16 Nov 11:00 | 120.2–109.4 | HOU 78% | 1.28 / 4.52 | WAS +10.5 | 229.5 | WAS +8.5 covers 43%; o224.5 61% |
| ATL @ MIL | Mon 16 Nov 12:00 | 118.5–110.2 | ATL 72% | 1.38 / 3.60 | MIL +8.5 | 228.5 | MIL +8.5 covers 50%; o233.5 40% |
| OKC @ SAC | Mon 16 Nov 13:00 | 119.9–107.2 | OKC 82% | 1.23 / 5.40 | SAC +12.5 | 226.5 | SAC +10.5 covers 44%; o222.5 60% |

### LAL @ PHX
Out: Mark Williams (PHX), Austin Reaves (LAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.2–112.1 | LAL 50% | 2.00 / 2.00 | PHX +0.5 | 224.5 | PHX +3.5 covers 59%; o226.5 45% |
| Expected (weighted by chance each plays) | 113.6–111.6 | LAL 55% | 1.80 / 2.24 | PHX +2.5 | 224.5 | PHX +3.5 covers 54%; o226.5 47% |
| if Collin Sexton plays | 113.8–111.2 | LAL 57% | 1.75 / 2.34 | PHX +2.5 | 224.5 | PHX +3.5 covers 52%; o226.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Sexton (LAL) | Questionable | 55% | 21.1 | 12.3 | 2.3 | 2.6 | 1.3 | 0.9 | 0.2 | 1.8 | 17.3 | full tables below |
| Adou Thiero (LAL) | Questionable | 55% | 12.8 | 4.1 | 3.3 | 0.8 | 0.1 | 0.5 | 0.2 | 0.8 | 8.2 | small |
| Drew Timme (PHX) | Day-To-Day | 70% | 6.4 | 2.5 | 1.1 | 0.6 | 0.1 | 0.2 | 0.1 | 0.4 | 4.2 | small |
| Bronny James (LAL) | Questionable | 55% | 7.6 | 2.1 | 0.2 | 0.6 | 0.1 | 0.3 | 0.2 | 0.4 | 2.9 | small |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 37.7<br><sub>35,38,-,39,32</sub> | 38.6<br><sub>40,53,-,32,32</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>9,5,-,8,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>7,5,-,10,5</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>6,5,-,3,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.6 | 5.5 | 54.6 |
| Walker Kessler | 98% | 32.4<br><sub>29,37,29,30,29</sub> | 14.1<br><sub>15,16,12,21,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 12.4<br><sub>8,12,16,10,11</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>0,2,4,4,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.9 | 2.2 | 2.2 | 28.5 |
| Quentin Grimes | 98% | 29.3<br><sub>25,20,32,-,-</sub> | 11.2<br><sub>6,2,12,-,-</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>1,0,1,-,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.7<br><sub>1,0,4,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>0,0,2,-,-</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.3 | 1.8 | 17.4 |
| Matisse Thybulle | 98% | 27.9<br><sub>23,24,28,23,23</sub> | 8.2<br><sub>3,2,4,6,8</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>1,2,2,0,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,0,0,1,1</sub> |  | 1.4<br><sub>1,0,0,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.4 | 0.7 | 1.3 | 12.4 |
| Jake LaRavia | 98% | 27.5<br><sub>21,25,29,32,21</sub> | 7.3<br><sub>9,7,5,4,0</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>2,8,1,3,9</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>2,3,2,3,6</sub> |  | 0.7<br><sub>2,2,0,0,0</sub> |  | 1.3 | 0.6 | 1.4 | 14.1 |
| Sandro Mamukelashvili | 98% | 26.4<br><sub>19,20,18,32,26</sub> | 12.0<br><sub>2,7,7,23,23</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>6,3,3,8,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,1,0,3,2</sub> |  | 1.5<br><sub>0,1,1,5,5</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.5 | 1.1 | 19.6 |
| Ziaire Williams | 98% | 26.1<br><sub>23,20,21,28,20</sub> | 10.6<br><sub>10,8,17,12,9</sub> |  | 3.1<br><sub>4,3,2,2,1</sub> |  | 1.7<br><sub>1,1,0,2,5</sub> |  | 1.4<br><sub>1,2,4,2,1</sub> |  | 1.5 | 0.3 | 1.1 | 15.5 |
| Jarred Vanderbilt | 80% | 14.7<br><sub>7,-,14,13,9</sub> | 3.1<br><sub>0,-,2,4,4</sub> |  | 4.0<br><sub>1,-,10,2,3</sub> |  | 1.1<br><sub>0,-,3,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.2 | 0.8 | 8.2 |
| Jaden Hardy | 58% | 11.5<br><sub>1,-,-,-,4</sub> | 6.0<br><sub>0,-,-,-,3</sub> |  | 1.1<br><sub>0,-,-,-,1</sub> |  | 0.8<br><sub>1,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.8 | 7.8 |
| Kevon Looney | 43% | 9.5<br><sub>-,-,-,-,4</sub> | 1.9<br><sub>-,-,-,-,0</sub> |  | 3.4<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Chris Manon | 58% | 8.8<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 4.5 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Carson Cooper | 38% | 8.3<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 1.5 | 8.5 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.5<br><sub>34,39,29,29,35</sub> | 24.4<br><sub>30,24,32,17,30</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>1,2,2,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.9<br><sub>8,3,4,5,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>4,2,3,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 3.1 | 33.8 |
| Dillon Brooks | 98% | 30.4<br><sub>29,37,26,22,30</sub> | 16.4<br><sub>24,11,7,8,15</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,4,4,4,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>4,3,1,0,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 1.5 | 22.0 |
| Miles Bridges | 98% | 28.2<br><sub>31,31,26,18,25</sub> | 13.3<br><sub>18,13,7,8,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>13,10,5,4,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>5,7,0,2,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>3,1,0,2,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.4 | 1.3 | 22.0 |
| Jalen Green | 98% | 26.4<br><sub>24,34,24,21,21</sub> | 14.0<br><sub>6,16,6,13,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>0,3,5,5,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>3,6,4,1,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 2.3 | 20.5 |
| Oso Ighodaro | 98% | 24.2<br><sub>24,23,18,20,32</sub> | 6.5<br><sub>2,4,7,6,2</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>5,6,4,8,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>1,3,2,2,7</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.4 | 15.3 |
| Collin Gillespie | 98% | 23.9<br><sub>24,20,24,22,27</sub> | 9.2<br><sub>6,7,6,12,13</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>2,3,2,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>2,4,3,8,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.2 | 1.2 | 15.8 |
| Luke Kennard | 98% | 18.6<br><sub>21,14,14,22,21</sub> | 7.4<br><sub>12,11,3,14,8</sub> |  | 1.8<br><sub>1,1,1,1,1</sub> |  | 1.8<br><sub>5,2,0,3,1</sub> |  | 1.0<br><sub>3,3,1,3,0</sub> |  | 0.7 | 0.1 | 0.8 | 11.1 |
| Jordan Goodwin | 98% | 18.0<br><sub>-,-,-,14,24</sub> | 7.2<br><sub>-,-,-,18,6</sub> |  | 3.6<br><sub>-,-,-,3,5</sub> |  | 1.7<br><sub>-,-,-,1,2</sub> |  | 1.1<br><sub>-,-,-,6,2</sub> |  | 1.3 | 0.1 | 0.8 | 12.4 |
| Khaman Maluach | 98% | 16.7<br><sub>22,18,20,22,16</sub> | 6.2<br><sub>8,8,11,11,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>6,10,5,7,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>2,0,2,3,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.8 | 1.0 | 12.0 |
| Ryan Dunn | 98% | 15.2<br><sub>25,23,23,25,10</sub> | 4.3<br><sub>11,8,3,10,0</sub> |  | 3.2<br><sub>3,5,2,8,4</sub> |  | 1.0<br><sub>3,3,0,2,0</sub> |  | 0.4<br><sub>1,2,1,1,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.6 |
| Rasheer Fleming | 52% | 8.1<br><sub>-,-,9,12,-</sub> | 3.1<br><sub>-,-,2,4,-</sub> |  | 1.4<br><sub>-,-,1,2,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,1,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.7 |
| Pat Spencer | 67% | 7.0<br><sub>2,-,6,-,-</sub> | 2.5<br><sub>0,-,2,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Jamaree Bouyea | 58% | 6.9<br><sub>2,-,9,8,-</sub> | 2.8<br><sub>0,-,4,7,-</sub> |  | 0.9<br><sub>0,-,0,1,-</sub> |  | 1.2<br><sub>0,-,3,3,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.9 |
| Koa Peat | 58% | 6.4<br><sub>2,-,6,6,-</sub> | 2.6<br><sub>0,-,4,5,-</sub> |  | 1.3<br><sub>1,-,0,1,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |
| Duop Reath | 58% | 6.2<br><sub>2,-,6,-,-</sub> | 2.7<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>

<details><summary>if Collin Sexton plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 37.1<br><sub>35,38,-,39,32</sub> | 37.2<br><sub>40,53,-,32,32</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>9,5,-,8,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.2<br><sub>7,5,-,10,5</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>6,5,-,3,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8 | 0.6 | 5.0 | 53.0 |
| Walker Kessler (LAL) | 98% | 31.7<br><sub>29,37,29,30,29</sub> | 12.9<br><sub>15,16,12,21,10</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 12.3<br><sub>8,12,16,10,11</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>0,2,4,4,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.9 | 2.2 | 2.0 | 27.1 |
| Quentin Grimes (LAL) | 98% | 27.7<br><sub>25,20,32,-,-</sub> | 9.9<br><sub>6,2,12,-,-</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,0,1,-,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>1,0,4,-,-</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>0,0,2,-,-</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.3 | 1.5 | 15.6 |
| Jake LaRavia (LAL) | 98% | 26.7<br><sub>21,25,29,32,21</sub> | 7.1<br><sub>9,7,5,4,0</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>2,8,1,3,9</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,3,2,3,6</sub> |  | 0.7<br><sub>2,2,0,0,0</sub> |  | 1.3 | 0.6 | 1.4 | 13.6 |
| Matisse Thybulle (LAL) | 98% | 26.6<br><sub>23,24,28,23,23</sub> | 7.2<br><sub>3,2,4,6,8</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,2,2,0,5</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>2,0,0,1,1</sub> |  | 1.2<br><sub>1,0,0,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.2 | 0.7 | 1.1 | 11.2 |
| Sandro Mamukelashvili (LAL) | 98% | 25.3<br><sub>19,20,18,32,26</sub> | 11.0<br><sub>2,7,7,23,23</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>6,3,3,8,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>1,1,0,3,2</sub> |  | 1.5<br><sub>0,1,1,5,5</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.5 | 1.0 | 18.2 |
| Ziaire Williams (LAL) | 98% | 25.1<br><sub>23,20,21,28,20</sub> | 9.9<br><sub>10,8,17,12,9</sub> |  | 3.0<br><sub>4,3,2,2,1</sub> |  | 1.6<br><sub>1,1,0,2,5</sub> |  | 1.4<br><sub>1,2,4,2,1</sub> |  | 1.4 | 0.3 | 1.0 | 14.4 |
| Collin Sexton (LAL) | 100% | 21.1<br><sub>16,11,24,27,13</sub> | 12.3<br><sub>10,0,17,18,10</sub> | 13.5 · – | 2.3<br><sub>3,0,2,2,1</sub> |  | 2.6<br><sub>1,1,2,6,3</sub> | 2.5 | 1.3<br><sub>1,0,0,3,0</sub> | 1.5 | 0.9 | 0.2 | 1.8 | 17.3 |
| Jarred Vanderbilt (LAL) | 80% | 12.7<br><sub>7,-,14,13,9</sub> | 2.8<br><sub>0,-,2,4,4</sub> |  | 3.5<br><sub>1,-,10,2,3</sub> |  | 1.0<br><sub>0,-,3,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 7.2 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Jaden Hardy (LAL) | 58% | 8.0<br><sub>1,-,-,-,4</sub> | 4.0<br><sub>0,-,-,-,3</sub> |  | 0.7<br><sub>0,-,-,-,1</sub> |  | 0.6<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.3 |
| Kevon Looney (LAL) | 43% | 7.8<br><sub>-,-,-,-,4</sub> | 1.6<br><sub>-,-,-,-,0</sub> |  | 2.9<br><sub>-,-,-,-,2</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 5.0 |
| Carson Cooper (LAL) | 38% | 7.2<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 1.4 | 7.5 |
| Chris Manon (LAL) | 58% | 6.8<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.4 |
| Devin Booker (PHX) | 98% | 34.5<br><sub>34,39,29,29,35</sub> | 24.4<br><sub>30,24,32,17,30</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>1,2,2,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.9<br><sub>8,3,4,5,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>4,2,3,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 3.1 | 33.6 |
| Dillon Brooks (PHX) | 98% | 30.4<br><sub>29,37,26,22,30</sub> | 16.4<br><sub>24,11,7,8,15</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,4,4,4,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>4,3,1,0,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 1.5 | 22.1 |
| Miles Bridges (PHX) | 98% | 28.1<br><sub>31,31,26,18,25</sub> | 13.3<br><sub>18,13,7,8,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>13,10,5,4,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>5,7,0,2,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>3,1,0,2,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.4 | 1.3 | 21.9 |
| Jalen Green (PHX) | 98% | 26.4<br><sub>24,34,24,21,21</sub> | 14.0<br><sub>6,16,6,13,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>0,3,5,5,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>3,6,4,1,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.3 | 2.3 | 20.5 |
| Oso Ighodaro (PHX) | 98% | 24.3<br><sub>24,23,18,20,32</sub> | 6.5<br><sub>2,4,7,6,2</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>5,6,4,8,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>1,3,2,2,7</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.4 | 15.2 |
| Collin Gillespie (PHX) | 98% | 23.9<br><sub>24,20,24,22,27</sub> | 9.2<br><sub>6,7,6,12,13</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>2,3,2,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>2,4,3,8,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.2 | 1.2 | 15.8 |
| Luke Kennard (PHX) | 98% | 18.5<br><sub>21,14,14,22,21</sub> | 7.3<br><sub>12,11,3,14,8</sub> |  | 1.8<br><sub>1,1,1,1,1</sub> |  | 1.8<br><sub>5,2,0,3,1</sub> |  | 1.0<br><sub>3,3,1,3,0</sub> |  | 0.7 | 0.1 | 0.8 | 11.0 |
| Jordan Goodwin (PHX) | 98% | 18.0<br><sub>-,-,-,14,24</sub> | 7.2<br><sub>-,-,-,18,6</sub> |  | 3.5<br><sub>-,-,-,3,5</sub> |  | 1.7<br><sub>-,-,-,1,2</sub> |  | 1.1<br><sub>-,-,-,6,2</sub> |  | 1.3 | 0.1 | 0.8 | 12.4 |
| Khaman Maluach (PHX) | 98% | 16.8<br><sub>22,18,20,22,16</sub> | 6.2<br><sub>8,8,11,11,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>6,10,5,7,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>2,0,2,3,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.8 | 1.0 | 12.0 |
| Ryan Dunn (PHX) | 98% | 15.2<br><sub>25,23,23,25,10</sub> | 4.3<br><sub>11,8,3,10,0</sub> |  | 3.2<br><sub>3,5,2,8,4</sub> |  | 1.0<br><sub>3,3,0,2,0</sub> |  | 0.4<br><sub>1,2,1,1,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.6 |
| Rasheer Fleming (PHX) | 52% | 8.1<br><sub>-,-,9,12,-</sub> | 3.0<br><sub>-,-,2,4,-</sub> |  | 1.4<br><sub>-,-,1,2,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,1,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.6 |
| Jamaree Bouyea (PHX) | 58% | 7.0<br><sub>2,-,9,8,-</sub> | 2.8<br><sub>0,-,4,7,-</sub> |  | 0.9<br><sub>0,-,0,1,-</sub> |  | 1.2<br><sub>0,-,3,3,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Pat Spencer (PHX) | 67% | 7.0<br><sub>2,-,6,-,-</sub> | 2.5<br><sub>0,-,2,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Koa Peat (PHX) | 58% | 6.4<br><sub>2,-,6,6,-</sub> | 2.6<br><sub>0,-,4,5,-</sub> |  | 1.3<br><sub>1,-,0,1,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |
| Duop Reath (PHX) | 58% | 6.2<br><sub>2,-,6,-,-</sub> | 2.7<br><sub>0,-,2,-,-</sub> |  | 1.2<br><sub>0,-,2,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>


### CHA @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Kon Knueppel (CHA), Dennis Schroder (CHA), Hannes Steinbach (CHA)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.7–111.0 | CHA 44% | 2.29 / 1.77 | LAC -2.5 | 219.5 | LAC +1.5 covers 59%; o213.5 63% |
| Expected (weighted by chance each plays) | 108.6–111.3 | CHA 43% | 2.35 / 1.74 | LAC -3.5 | 219.5 | LAC +1.5 covers 61%; o213.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nick Martinelli (LAC) | Questionable | 55% | 6.3 | 2.9 | 1.5 | 0.5 | 0.2 | 0.2 | 0.2 | 0.4 | 4.8 | small |

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 31.3<br><sub>31,26,14,-,-</sub> | 20.2<br><sub>17,10,8,-,-</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>1,4,2,-,-</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>4,1,1,-,-</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>3,1,0,-,-</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.5 | 2.5 | 28.0 |
| Naz Reid | 98% | 30.1<br><sub>27,36,26,32,34</sub> | 17.7<br><sub>13,28,14,25,16</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>6,9,6,13,8</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>2,2,2,4,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.1<br><sub>2,2,2,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.8 | 2.5 | 27.8 |
| Grayson Allen | 98% | 29.0<br><sub>19,27,22,34,34</sub> | 14.9<br><sub>11,22,0,27,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>1,2,2,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.9<br><sub>0,4,3,6,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>3,5,0,6,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.3 | 2.1 | 21.9 |
| Moussa Diabate | 98% | 28.5<br><sub>24,29,-,-,32</sub> | 8.5<br><sub>7,7,-,-,7</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 8.8<br><sub>9,6,-,-,13</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,2,-,-,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.0<br><sub>0,0,-,-,0</sub> |  | 1.0 | 0.8 | 1.5 | 19.6 |
| Sion James | 98% | 26.1<br><sub>21,31,21,33,32</sub> | 7.2<br><sub>11,10,11,11,3</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,2,3,4,8</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,1,0,4,6</sub> |  | 1.0<br><sub>3,0,3,3,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.2 | 1.1 | 13.9 |
| Royce O'Neale | 98% | 20.4<br><sub>18,18,26,23,22</sub> | 6.0<br><sub>2,0,7,10,7</sub> |  | 3.4<br><sub>4,3,4,3,4</sub> |  | 1.2<br><sub>0,2,2,1,0</sub> |  | 1.0<br><sub>0,0,2,2,2</sub> |  | 0.7 | 0.2 | 0.7 | 10.7 |
| Coby White | 98% | 20.3<br><sub>16,18,16,20,20</sub> | 13.2<br><sub>7,4,7,10,21</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>0,5,1,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,2,1,9,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>1,0,1,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.5 | 0.1 | 2.2 | 19.2 |
| Ryan Kalkbrenner | 98% | 18.4<br><sub>16,19,21,35,16</sub> | 5.7<br><sub>4,6,4,8,2</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>6,4,5,15,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>0,2,0,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 11.7 |
| Grant Williams | 67% | 17.0<br><sub>-,-,-,-,16</sub> | 6.2<br><sub>-,-,-,-,11</sub> |  | 3.2<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.8<br><sub>-,-,-,-,2</sub> |  | 0.5 | 0.5 | 0.9 | 10.7 |
| Tidjane Salaun | 96% | 15.1<br><sub>19,10,23,18,16</sub> | 5.6<br><sub>1,9,13,14,2</sub> |  | 3.4<br><sub>7,1,4,3,4</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6<br><sub>0,3,2,3,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.6 |
| Christian Anderson | 88% | 14.7<br><sub>9,-,25,16,18</sub> | 6.0<br><sub>8,-,4,9,13</sub> |  | 1.6<br><sub>2,-,3,1,0</sub> |  | 2.0<br><sub>2,-,5,1,2</sub> |  | 0.7<br><sub>1,-,0,3,3</sub> |  | 0.4 | 0.2 | 1.5 | 9.5 |
| Liam McNeeley | 52% | 8.7<br><sub>9,-,19,16,-</sub> | 3.6<br><sub>3,-,8,8,-</sub> |  | 1.6<br><sub>0,-,2,1,-</sub> |  | 0.7<br><sub>1,-,3,1,-</sub> |  | 0.3<br><sub>0,-,1,2,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.8 |
| PJ Hall | 38% | 7.4<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.6 | 5.8 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.0<br><sub>36,39,32,25,37</sub> | 20.7<br><sub>16,26,24,13,24</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>4,1,0,5,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 7.1<br><sub>8,7,10,6,7</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 2.5<br><sub>1,4,3,1,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.2 | 3.2 | 30.2 |
| Rui Hachimura | 98% | 29.1<br><sub>-,37,26,23,32</sub> | 14.0<br><sub>-,21,14,13,7</sub> | 14.5 · –<br><sub>o 46% · u 53%</sub> | 4.6<br><sub>-,9,3,5,11</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>-,7,2,1,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.8<br><sub>-,1,2,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.3 | 1.2 | 20.0 |
| Derrick Jones Jr. | 98% | 27.1<br><sub>-,37,29,24,29</sub> | 10.3<br><sub>-,12,8,11,14</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>-,8,4,3,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>-,1,3,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2<br><sub>-,2,0,2,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.8 | 0.9 | 15.4 |
| Brook Lopez | 98% | 24.8<br><sub>22,35,26,19,31</sub> | 12.2<br><sub>12,20,20,8,26</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>6,8,7,4,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,1,1,1,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>1,2,1,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 1.2 | 1.1 | 18.3 |
| Kris Dunn | 98% | 24.1<br><sub>30,35,24,19,20</sub> | 6.7<br><sub>12,5,14,3,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>4,5,5,2,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>1,3,4,3,6</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>1,1,2,1,0</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.2 | 1.1 | 13.4 |
| Max Strus | 98% | 21.2<br><sub>23,23,19,22,23</sub> | 8.4<br><sub>11,9,7,12,3</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>4,5,4,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>6,5,2,3,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,3,1,2,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.1 | 0.8 | 14.5 |
| Keaton Wagler | 98% | 20.2<br><sub>24,16,18,23,18</sub> | 10.6<br><sub>6,11,15,11,14</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>4,2,2,0,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>4,1,4,4,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>0,3,3,1,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.2 | 1.6 | 16.2 |
| Kobe Sanders | 98% | 20.1<br><sub>38,18,22,26,15</sub> | 8.4<br><sub>26,4,8,9,5</sub> |  | 2.1<br><sub>4,2,2,3,0</sub> |  | 1.9<br><sub>3,1,4,7,1</sub> |  | 1.1<br><sub>5,0,2,1,1</sub> |  | 0.9 | 0.1 | 1.1 | 12.4 |
| Isaiah Jackson | 98% | 16.9<br><sub>26,13,-,16,17</sub> | 6.8<br><sub>19,2,-,4,5</sub> |  | 4.7<br><sub>8,4,-,4,3</sub> |  | 1.4<br><sub>2,2,-,0,3</sub> |  | 0.1<br><sub>1,0,-,0,0</sub> |  | 0.8 | 0.8 | 1.0 | 12.8 |
| Gradey Dick | 97% | 15.6<br><sub>29,7,17,19,19</sub> | 7.3<br><sub>12,4,15,10,13</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>4,2,4,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>3,1,0,2,0</sub> |  | 0.7<br><sub>0,0,2,1,2</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.1 | 0.7 | 10.6 |
| Baba Miller | 72% | 11.3<br><sub>12,6,20,16,-</sub> | 5.1<br><sub>4,2,12,13,-</sub> |  | 1.8<br><sub>0,1,5,4,-</sub> |  | 1.2<br><sub>1,1,4,0,-</sub> |  | 0.3<br><sub>1,0,0,1,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.2 |
| Jalen Pickett | 52% | 7.0<br><sub>-,-,2,8,-</sub> | 2.5<br><sub>-,-,0,3,-</sub> |  | 0.9<br><sub>-,-,0,1,-</sub> |  | 1.0<br><sub>-,-,0,1,-</sub> |  | 0.2<br><sub>-,-,0,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.4 |
| Cam Christie | 52% | 6.1<br><sub>-,-,2,-,-</sub> | 2.2<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.6 |
| Blake Wesley | 52% | 5.9<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.9 |

</details>


### SAS @ UTA
Out: Trey Alexander (UTA), Jaxson Hayes (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Tobias Harris (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 122.2–106.7 | SAS 86% | 1.16 / 7.33 | UTA +15.5 | 228.5 | UTA +15.5 covers 50%; o224.5 60% |
| Expected (weighted by chance each plays) | 122.4–107.0 | SAS 86% | 1.16 / 7.36 | UTA +15.5 | 229.5 | UTA +15.5 covers 50%; o224.5 61% |
| if De'Aaron Fox plays | 122.7–107.2 | SAS 86% | 1.16 / 7.41 | UTA +15.5 | 229.5 | UTA +15.5 covers 50%; o224.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 28.2 | 14.2 | 3.8 | 5.6 | 1.2 | 1.4 | 0.4 | 1.9 | 23.6 | full tables below |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 31.9<br><sub>28,28,26,36,25</sub> | 18.4<br><sub>19,13,17,18,9</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>2,7,5,6,3</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 5.3<br><sub>3,3,4,10,4</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.4 | 1.8 | 29.2 |
| Victor Wembanyama | 98% | 31.2<br><sub>26,24,25,32,21</sub> | 28.6<br><sub>30,29,40,32,12</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 12.0<br><sub>14,7,11,9,12</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,3,3,1,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 3.4 | 2.5 | 44.0 |
| Devin Vassell | 98% | 31.1<br><sub>27,21,-,-,23</sub> | 13.2<br><sub>19,15,-,-,7</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>2,2,-,-,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,3,-,-,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>5,2,-,-,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3 | 0.5 | 1.0 | 20.6 |
| Stephon Castle | 98% | 30.4<br><sub>28,24,30,29,25</sub> | 18.8<br><sub>19,14,4,11,32</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>3,7,8,1,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.4<br><sub>7,5,7,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>1,2,0,1,5</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.3 | 2.7 | 30.4 |
| Julian Champagnie | 98% | 28.1<br><sub>22,21,27,35,23</sub> | 10.5<br><sub>8,14,11,12,7</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>7,4,3,0,8</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,0,2,2,3</sub> |  | 2.1<br><sub>2,4,3,3,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.6 | 0.8 | 17.3 |
| Keldon Johnson | 98% | 25.6<br><sub>27,27,26,28,25</sub> | 11.3<br><sub>3,10,4,10,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>6,7,5,6,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>6,4,3,4,4</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 0.8 | 0.2 | 1.2 | 18.9 |
| Harrison Barnes | 88% | 18.1<br><sub>19,19,21,13,21</sub> | 6.9<br><sub>13,5,11,3,11</sub> |  | 2.0<br><sub>1,3,2,1,1</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 1.0<br><sub>2,1,2,1,3</sub> |  | 0.4 | 0.2 | 0.5 | 9.7 |
| Luke Kornet | 98% | 16.9<br><sub>18,15,13,14,16</sub> | 4.2<br><sub>2,6,2,7,6</sub> |  | 5.2<br><sub>6,4,4,5,7</sub> |  | 1.4<br><sub>1,2,1,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.9 | 0.6 | 10.8 |
| Carter Bryant | 91% | 15.7<br><sub>3,17,14,15,19</sub> | 6.0<br><sub>0,6,8,10,8</sub> |  | 2.6<br><sub>0,4,1,1,3</sub> |  | 1.1<br><sub>0,1,1,2,2</sub> |  | 0.8<br><sub>0,2,2,2,2</sub> |  | 0.4 | 0.4 | 0.6 | 9.8 |
| Jordan McLaughlin | 80% | 13.7<br><sub>8,12,11,2,14</sub> | 4.4<br><sub>2,3,4,4,4</sub> |  | 2.3<br><sub>2,0,4,0,6</sub> |  | 2.3<br><sub>1,0,2,0,2</sub> |  | 0.4<br><sub>0,1,0,0,0</sub> |  | 1.0 | 0.1 | 0.7 | 9.0 |
| Tarris Reed Jr. | 80% | 10.3<br><sub>3,9,9,2,11</sub> | 3.5<br><sub>0,2,4,0,2</sub> |  | 3.8<br><sub>1,3,3,0,4</sub> |  | 0.5<br><sub>0,1,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 7.8 |
| David Jones Garcia | 67% | 7.4<br><sub>3,-,8,2,-</sub> | 2.9<br><sub>0,-,2,0,-</sub> |  | 1.4<br><sub>0,-,0,0,-</sub> |  | 1.3<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 5.5 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 34.2<br><sub>32,30,-,33,38</sub> | 21.4<br><sub>16,19,-,13,27</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>6,5,-,7,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.8<br><sub>9,8,-,7,7</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,0,-,2,4</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.9 | 0.2 | 3.2 | 31.4 |
| Ace Bailey | 98% | 33.3<br><sub>29,32,35,31,35</sub> | 15.4<br><sub>12,7,23,18,21</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>6,2,7,7,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>0,3,2,2,1</sub> |  | 2.2<br><sub>0,1,3,3,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 1.0 | 1.8 | 23.1 |
| Darryn Peterson | 98% | 33.0<br><sub>30,35,31,33,34</sub> | 17.2<br><sub>21,26,25,22,28</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,6,4,4,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.0<br><sub>5,4,4,5,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>3,4,4,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.7 | 2.0 | 25.7 |
| Brice Sensabaugh | 98% | 25.4<br><sub>10,13,14,23,27</sub> | 14.1<br><sub>0,2,5,19,7</sub> |  | 3.8<br><sub>2,3,4,3,3</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 2.1<br><sub>0,0,1,3,1</sub> |  | 0.7 | 0.3 | 1.8 | 19.9 |
| Josh Green | 93% | 24.1<br><sub>24,28,30,26,14</sub> | 5.2<br><sub>3,10,2,3,2</sub> |  | 2.4<br><sub>3,0,5,2,0</sub> |  | 1.1<br><sub>1,1,4,1,0</sub> |  | 0.7<br><sub>1,1,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.8 |
| Josh Okogie | 96% | 23.5<br><sub>24,17,21,15,22</sub> | 6.3<br><sub>12,0,6,7,7</sub> | 4.5 · –<br><sub>o 54% · u 46%</sub> | 3.8<br><sub>4,1,4,3,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>0,0,4,0,1</sub> |  | 0.7<br><sub>2,0,0,1,2</sub> |  | 1.0 | 0.4 | 0.8 | 11.4 |
| Mo Bamba | 86% | 19.0<br><sub>-,17,17,18,20</sub> | 6.3<br><sub>-,3,7,5,9</sub> |  | 6.7<br><sub>-,3,7,1,9</sub> |  | 0.9<br><sub>-,1,0,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.4 | 1.4 | 0.8 | 13.9 |
| Isaiah Collier | 98% | 19.0<br><sub>13,16,24,12,16</sub> | 8.6<br><sub>4,6,17,7,3</sub> |  | 2.8<br><sub>3,4,5,3,2</sub> |  | 4.5<br><sub>3,2,5,2,5</sub> |  | 0.4<br><sub>0,0,4,1,1</sub> |  | 0.7 | 0.2 | 1.5 | 15.9 |
| Svi Mykhailiuk | 96% | 17.4<br><sub>14,6,21,20,7</sub> | 6.0<br><sub>0,0,7,3,0</sub> |  | 1.9<br><sub>0,0,2,0,1</sub> |  | 1.2<br><sub>1,0,3,2,0</sub> |  | 0.9<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 9.1 |
| Kyle Filipowski | 67% | 15.3<br><sub>1,15,15,-,2</sub> | 7.9<br><sub>0,9,7,-,2</sub> |  | 4.6<br><sub>0,6,4,-,0</sub> |  | 1.5<br><sub>0,1,1,-,0</sub> |  | 0.6<br><sub>0,1,0,-,0</sub> |  | 0.6 | 0.3 | 1.1 | 14.0 |
| Tony Bradley | 63% | 12.4<br><sub>1,2,14,-,12</sub> | 3.2<br><sub>0,0,4,-,0</sub> |  | 3.8<br><sub>1,1,5,-,5</sub> |  | 0.6<br><sub>0,0,0,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.7 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper (SAS) | 98% | 29.7<br><sub>28,28,26,36,25</sub> | 16.0<br><sub>19,13,17,18,9</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>2,7,5,6,3</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 4.5<br><sub>3,3,4,10,4</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.3 | 1.6 | 25.7 |
| Victor Wembanyama (SAS) | 98% | 29.6<br><sub>26,24,25,32,21</sub> | 25.6<br><sub>30,29,40,32,12</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 11.3<br><sub>14,7,11,9,12</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>2,3,3,1,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1 | 3.4 | 2.3 | 40.0 |
| Devin Vassell (SAS) | 98% | 28.9<br><sub>27,21,-,-,23</sub> | 12.0<br><sub>19,15,-,-,7</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,2,-,-,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>2,3,-,-,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>5,2,-,-,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.4 | 0.9 | 18.6 |
| Stephon Castle (SAS) | 98% | 28.5<br><sub>28,24,30,29,25</sub> | 17.0<br><sub>19,14,4,11,32</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>3,7,8,1,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 5.7<br><sub>7,5,7,3,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>1,2,0,1,5</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.3 | 2.4 | 27.7 |
| De'Aaron Fox (SAS) | 100% | 28.2<br><sub>26,22,29,31,17</sub> | 14.2<br><sub>9,8,15,17,7</sub> | 13.5 · – | 3.8<br><sub>2,3,9,4,5</sub> | 3.5 | 5.6<br><sub>4,6,6,9,1</sub> | 5.5 | 1.2<br><sub>0,1,2,2,0</sub> | 1.5 | 1.4 | 0.4 | 1.9 | 23.6 |
| Julian Champagnie (SAS) | 98% | 25.5<br><sub>22,21,27,35,23</sub> | 9.7<br><sub>8,14,11,12,7</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>7,4,3,0,8</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,0,2,2,3</sub> |  | 1.9<br><sub>2,4,3,3,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.5 | 0.7 | 15.8 |
| Keldon Johnson (SAS) | 98% | 23.0<br><sub>27,27,26,28,25</sub> | 10.0<br><sub>3,10,4,10,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>6,7,5,6,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>6,4,3,4,4</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.7 | 0.2 | 1.1 | 16.9 |
| Harrison Barnes (SAS) | 88% | 15.8<br><sub>19,19,21,13,21</sub> | 6.1<br><sub>13,5,11,3,11</sub> |  | 1.8<br><sub>1,3,2,1,1</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>2,1,2,1,3</sub> |  | 0.4 | 0.2 | 0.5 | 8.6 |
| Luke Kornet (SAS) | 98% | 15.3<br><sub>18,15,13,14,16</sub> | 3.9<br><sub>2,6,2,7,6</sub> |  | 4.8<br><sub>6,4,4,5,7</sub> |  | 1.2<br><sub>1,2,1,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.5 | 9.9 |
| Carter Bryant (SAS) | 91% | 13.4<br><sub>3,17,14,15,19</sub> | 5.3<br><sub>0,6,8,10,8</sub> |  | 2.3<br><sub>0,4,1,1,3</sub> |  | 1.0<br><sub>0,1,1,2,2</sub> |  | 0.7<br><sub>0,2,2,2,2</sub> |  | 0.3 | 0.3 | 0.6 | 8.6 |
| Jordan McLaughlin (SAS) | 80% | 9.8<br><sub>8,12,11,2,14</sub> | 3.5<br><sub>2,3,4,4,4</sub> |  | 1.8<br><sub>2,0,4,0,6</sub> |  | 1.7<br><sub>1,0,2,0,2</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.7 | 0.1 | 0.5 | 6.9 |
| Tarris Reed Jr. (SAS) | 80% | 8.2<br><sub>3,9,9,2,11</sub> | 3.2<br><sub>0,2,4,0,2</sub> |  | 3.1<br><sub>1,3,3,0,4</sub> |  | 0.5<br><sub>0,1,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.4 | 6.7 |
| David Jones Garcia (SAS) | 67% | 6.2<br><sub>3,-,8,2,-</sub> | 2.7<br><sub>0,-,2,0,-</sub> |  | 1.2<br><sub>0,-,0,0,-</sub> |  | 1.2<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.1 |
| Keyonte George (UTA) | 98% | 34.2<br><sub>32,30,-,33,38</sub> | 21.4<br><sub>16,19,-,13,27</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>6,5,-,7,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.8<br><sub>9,8,-,7,7</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>1,0,-,2,4</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.9 | 0.2 | 3.2 | 31.4 |
| Ace Bailey (UTA) | 98% | 33.3<br><sub>29,32,35,31,35</sub> | 15.4<br><sub>12,7,23,18,21</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>6,2,7,7,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>0,3,2,2,1</sub> |  | 2.1<br><sub>0,1,3,3,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 1.0 | 1.8 | 23.1 |
| Darryn Peterson (UTA) | 98% | 32.9<br><sub>30,35,31,33,34</sub> | 17.3<br><sub>21,26,25,22,28</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>2,6,4,4,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.0<br><sub>5,4,4,5,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>3,4,4,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.8 | 2.0 | 25.9 |
| Brice Sensabaugh (UTA) | 98% | 25.4<br><sub>10,13,14,23,27</sub> | 14.0<br><sub>0,2,5,19,7</sub> |  | 3.8<br><sub>2,3,4,3,3</sub> |  | 1.9<br><sub>2,0,4,1,1</sub> |  | 2.1<br><sub>0,0,1,3,1</sub> |  | 0.7 | 0.3 | 1.8 | 19.8 |
| Josh Green (UTA) | 93% | 24.1<br><sub>24,28,30,26,14</sub> | 5.2<br><sub>3,10,2,3,2</sub> |  | 2.4<br><sub>3,0,5,2,0</sub> |  | 1.1<br><sub>1,1,4,1,0</sub> |  | 0.7<br><sub>1,1,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.8 |
| Josh Okogie (UTA) | 96% | 23.6<br><sub>24,17,21,15,22</sub> | 6.3<br><sub>12,0,6,7,7</sub> | 4.5 · –<br><sub>o 54% · u 46%</sub> | 3.9<br><sub>4,1,4,3,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>0,0,4,0,1</sub> |  | 0.7<br><sub>2,0,0,1,2</sub> |  | 1.0 | 0.4 | 0.8 | 11.5 |
| Mo Bamba (UTA) | 86% | 19.1<br><sub>-,17,17,18,20</sub> | 6.3<br><sub>-,3,7,5,9</sub> |  | 6.7<br><sub>-,3,7,1,9</sub> |  | 0.9<br><sub>-,1,0,1,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.4 | 1.5 | 0.8 | 13.9 |
| Isaiah Collier (UTA) | 98% | 19.0<br><sub>13,16,24,12,16</sub> | 8.5<br><sub>4,6,17,7,3</sub> |  | 2.8<br><sub>3,4,5,3,2</sub> |  | 4.5<br><sub>3,2,5,2,5</sub> |  | 0.4<br><sub>0,0,4,1,1</sub> |  | 0.7 | 0.2 | 1.5 | 15.9 |
| Svi Mykhailiuk (UTA) | 96% | 17.4<br><sub>14,6,21,20,7</sub> | 6.0<br><sub>0,0,7,3,0</sub> |  | 1.9<br><sub>0,0,2,0,1</sub> |  | 1.2<br><sub>1,0,3,2,0</sub> |  | 0.9<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 9.1 |
| Kyle Filipowski (UTA) | 67% | 15.1<br><sub>1,15,15,-,2</sub> | 7.9<br><sub>0,9,7,-,2</sub> |  | 4.6<br><sub>0,6,4,-,0</sub> |  | 1.5<br><sub>0,1,1,-,0</sub> |  | 0.6<br><sub>0,1,0,-,0</sub> |  | 0.6 | 0.3 | 1.1 | 14.0 |
| Tony Bradley (UTA) | 63% | 12.3<br><sub>1,2,14,-,12</sub> | 3.3<br><sub>0,0,4,-,0</sub> |  | 3.7<br><sub>1,1,5,-,5</sub> |  | 0.6<br><sub>0,0,0,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.4 | 0.6 | 7.6 |

</details>


### DAL @ BOS
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.7–119.7 | DAL 16% | 6.37 / 1.19 | BOS -13.5 | 225.5 | BOS -14.5 covers 48%; o218.5 65% |
| Expected (weighted by chance each plays) | 106.8–118.7 | DAL 20% | 4.93 / 1.25 | BOS -11.5 | 225.5 | BOS -14.5 covers 43%; o218.5 64% |
| if Kyrie Irving plays | 106.8–119.8 | DAL 18% | 5.70 / 1.21 | BOS -12.5 | 226.5 | BOS -14.5 covers 46%; o218.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Max Christie (DAL) | Doubtful | 20% | 18.5 | 6.8 | 2.1 | 1.1 | 1.0 | 0.4 | 0.2 | 0.8 | 10.0 | small |
| Santi Aldama (DAL) | Questionable | 55% | 18.6 | 8.9 | 4.1 | 1.5 | 1.1 | 0.5 | 0.4 | 1.0 | 14.5 | small |
| Kyrie Irving (DAL) | Questionable | 55% | 34.8 | 20.8 | 4.2 | 4.2 | 2.5 | 1.0 | 0.4 | 2.2 | 29.2 | full tables below |
| Devin Carter (BOS) | Questionable | 55% | 8.6 | 3.7 | 1.6 | 1.3 | 0.3 | 0.5 | 0.1 | 0.7 | 6.6 | small |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 36.1<br><sub>33,28,39,27,38</sub> | 25.2<br><sub>21,25,43,12,18</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>10,5,10,7,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>7,12,6,3,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>1,3,3,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.8 | 3.2 | 38.2 |
| P.J. Washington | 98% | 34.2<br><sub>33,25,35,16,26</sub> | 15.0<br><sub>26,6,13,10,10</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 7.0<br><sub>6,5,9,3,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>1,0,1,0,1</sub> |  | 2.0<br><sub>6,2,2,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.8 | 1.9 | 23.8 |
| Naji Marshall | 91% | 30.0<br><sub>25,15,25,23,30</sub> | 14.9<br><sub>7,8,6,13,12</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>1,1,5,1,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>5,2,2,4,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>0,1,0,1,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.1 | 1.9 | 23.2 |
| Caleb Martin | 98% | 27.4<br><sub>11,19,19,21,33</sub> | 7.6<br><sub>0,2,0,7,15</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>0,2,3,2,8</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>0,2,5,5,3</sub> |  | 0.8<br><sub>0,0,0,1,1</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.4 | 1.1 | 13.8 |
| Zaccharie Risacher | 98% | 24.5<br><sub>21,16,15,25,14</sub> | 8.7<br><sub>4,11,4,22,5</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>4,6,2,6,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,1,0,3,0</sub> |  | 1.1<br><sub>0,1,0,4,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.7 | 1.0 | 14.4 |
| Daniel Gafford | 92% | 24.1<br><sub>18,19,20,16,17</sub> | 10.2<br><sub>7,18,8,3,10</sub> |  | 6.3<br><sub>1,5,2,3,3</sub> |  | 1.5<br><sub>1,2,3,1,1</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.6 | 1.2 | 1.3 | 17.9 |
| Walter Clayton Jr. | 93% | 23.0<br><sub>23,16,25,22,13</sub> | 8.8<br><sub>12,5,6,5,2</sub> |  | 3.3<br><sub>4,4,6,1,2</sub> |  | 3.9<br><sub>2,6,4,4,2</sub> |  | 1.2<br><sub>1,1,1,0,0</sub> |  | 0.6 | 0.2 | 1.6 | 16.1 |
| Morez Johnson Jr. | 98% | 21.0<br><sub>24,19,-,13,15</sub> | 8.1<br><sub>13,4,-,0,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>17,9,-,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,1,-,0,0</sub> |  | 0.5<br><sub>1,0,-,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 13.8 |
| Marcus Sasser | 58% | 17.5<br><sub>-,9,-,9,-</sub> | 6.5<br><sub>-,4,-,3,-</sub> |  | 1.4<br><sub>-,0,-,1,-</sub> |  | 2.1<br><sub>-,0,-,0,-</sub> |  | 0.9<br><sub>-,0,-,0,-</sub> |  | 0.5 | 0.1 | 0.8 | 10.0 |
| Moussa Cisse | 58% | 10.0<br><sub>1,5,-,8,-</sub> | 3.2<br><sub>0,2,-,0,-</sub> |  | 3.3<br><sub>0,1,-,0,-</sub> |  | 0.2<br><sub>0,1,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.6 | 0.5 | 6.7 |
| Jett Howard | 52% | 10.0<br><sub>1,3,-,5,-</sub> | 4.0<br><sub>0,5,-,3,-</sub> |  | 1.1<br><sub>0,1,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.4<br><sub>0,1,-,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.7 |
| Tobi Lawal | 52% | 9.3<br><sub>1,5,-,12,-</sub> | 3.0<br><sub>0,2,-,0,-</sub> |  | 1.6<br><sub>0,0,-,6,-</sub> |  | 0.6<br><sub>0,0,-,1,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.3 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 32.9<br><sub>-,29,29,32,38</sub> | 25.8<br><sub>-,34,21,21,24</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>-,8,4,6,7</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.7<br><sub>-,9,6,4,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>-,5,5,3,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.5 | 2.6 | 40.6 |
| Paul George | 98% | 30.2<br><sub>35,22,28,30,-</sub> | 19.5<br><sub>25,8,27,36,-</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>3,5,3,5,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>5,1,1,1,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>5,2,5,6,-</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6 | 0.5 | 2.4 | 27.9 |
| Derrick White | 98% | 30.1<br><sub>36,25,27,22,38</sub> | 13.4<br><sub>24,18,9,5,19</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>4,4,3,1,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.9<br><sub>7,5,7,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,4,1,1,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.0 | 1.6 | 22.0 |
| Payton Pritchard | 98% | 27.3<br><sub>18,23,29,30,31</sub> | 14.2<br><sub>10,12,12,18,14</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>1,6,5,6,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 4.3<br><sub>5,5,4,5,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>0,4,4,4,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.1 | 1.3 | 21.9 |
| Neemias Queta | 98% | 23.8<br><sub>29,15,22,22,31</sub> | 10.4<br><sub>9,4,13,4,11</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>12,3,9,6,13</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>3,1,4,3,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.6 | 1.3 | 1.2 | 20.7 |
| Sam Hauser | 98% | 21.4<br><sub>30,17,23,18,24</sub> | 8.1<br><sub>11,9,7,12,8</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>2,3,3,5,9</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>0,3,1,2,0</sub> |  | 1.6<br><sub>3,3,1,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.4 | 0.2 | 0.5 | 12.9 |
| Baylor Scheierman | 98% | 21.2<br><sub>29,15,19,18,29</sub> | 6.6<br><sub>9,5,7,5,9</sub> |  | 4.3<br><sub>11,4,1,3,7</sub> |  | 1.7<br><sub>1,2,0,2,3</sub> |  | 1.0<br><sub>3,1,1,1,3</sub> |  | 0.8 | 0.1 | 0.7 | 12.6 |
| Mitchell Robinson | 98% | 15.0<br><sub>20,15,18,17,11</sub> | 5.2<br><sub>3,6,12,2,2</sub> |  | 6.0<br><sub>10,7,7,6,2</sub> |  | 0.7<br><sub>1,0,2,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.7 | 11.9 |
| Jordan Walsh | 98% | 14.8<br><sub>12,22,11,19,18</sub> | 4.2<br><sub>3,6,0,8,6</sub> |  | 3.2<br><sub>4,3,3,2,3</sub> |  | 0.8<br><sub>0,0,0,2,0</sub> |  | 0.4<br><sub>1,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 8.2 |
| Luka Garza | 98% | 12.7<br><sub>18,19,9,9,11</sub> | 6.9<br><sub>11,6,4,2,5</sub> |  | 3.4<br><sub>5,7,5,0,1</sub> |  | 1.1<br><sub>2,4,0,2,0</sub> |  | 0.7<br><sub>3,2,0,0,1</sub> |  | 0.3 | 0.3 | 0.6 | 11.3 |
| Hugo Gonzalez | 98% | 11.6<br><sub>14,15,10,19,8</sub> | 3.6<br><sub>4,8,0,10,0</sub> |  | 2.4<br><sub>2,1,2,2,1</sub> |  | 0.6<br><sub>0,0,1,2,0</sub> |  | 0.3<br><sub>0,1,0,2,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Mike Conley | 48% | 8.0<br><sub>-,11,10,-,-</sub> | 2.4<br><sub>-,0,3,-,-</sub> |  | 0.8<br><sub>-,0,3,-,-</sub> |  | 1.2<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Dillon Mitchell | 21% | 6.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 1.0 |
| Ron Harper Jr. | 58% | 6.8<br><sub>-,10,4,4,-</sub> | 3.0<br><sub>-,3,2,0,-</sub> |  | 1.0<br><sub>-,0,0,1,-</sub> |  | 0.6<br><sub>-,2,0,0,-</sub> |  | 0.3<br><sub>-,1,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Chris Cenac Jr. | 38% | 5.9<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.7 | 4.9 |
| Amari Williams | 17% | 5.1<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.5 |

</details>

<details><summary>if Kyrie Irving plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 32.9<br><sub>-,29,29,32,38</sub> | 26.0<br><sub>-,34,21,21,24</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>-,8,4,6,7</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.7<br><sub>-,9,6,4,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>-,5,5,3,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.6 | 2.6 | 40.8 |
| Paul George (BOS) | 98% | 30.2<br><sub>35,22,28,30,-</sub> | 19.6<br><sub>25,8,27,36,-</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>3,5,3,5,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>5,1,1,1,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>5,2,5,6,-</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6 | 0.5 | 2.4 | 28.0 |
| Derrick White (BOS) | 98% | 30.1<br><sub>36,25,27,22,38</sub> | 13.3<br><sub>24,18,9,5,19</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>4,4,3,1,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.9<br><sub>7,5,7,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,4,1,1,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 1.0 | 1.6 | 22.0 |
| Payton Pritchard (BOS) | 98% | 27.3<br><sub>18,23,29,30,31</sub> | 14.2<br><sub>10,12,12,18,14</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>1,6,5,6,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 4.2<br><sub>5,5,4,5,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>0,4,4,4,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.1 | 1.3 | 21.9 |
| Neemias Queta (BOS) | 98% | 23.8<br><sub>29,15,22,22,31</sub> | 10.4<br><sub>9,4,13,4,11</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 8.4<br><sub>12,3,9,6,13</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>3,1,4,3,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.6 | 1.3 | 1.2 | 20.7 |
| Sam Hauser (BOS) | 98% | 21.5<br><sub>30,17,23,18,24</sub> | 8.1<br><sub>11,9,7,12,8</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>2,3,3,5,9</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>0,3,1,2,0</sub> |  | 1.5<br><sub>3,3,1,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.4 | 0.2 | 0.4 | 12.9 |
| Baylor Scheierman (BOS) | 98% | 21.2<br><sub>29,15,19,18,29</sub> | 6.5<br><sub>9,5,7,5,9</sub> |  | 4.3<br><sub>11,4,1,3,7</sub> |  | 1.7<br><sub>1,2,0,2,3</sub> |  | 1.0<br><sub>3,1,1,1,3</sub> |  | 0.7 | 0.1 | 0.7 | 12.5 |
| Mitchell Robinson (BOS) | 98% | 15.0<br><sub>20,15,18,17,11</sub> | 5.2<br><sub>3,6,12,2,2</sub> |  | 6.0<br><sub>10,7,7,6,2</sub> |  | 0.7<br><sub>1,0,2,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.7 | 12.0 |
| Jordan Walsh (BOS) | 98% | 14.8<br><sub>12,22,11,19,18</sub> | 4.2<br><sub>3,6,0,8,6</sub> |  | 3.2<br><sub>4,3,3,2,3</sub> |  | 0.8<br><sub>0,0,0,2,0</sub> |  | 0.4<br><sub>1,1,0,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 8.2 |
| Luka Garza (BOS) | 98% | 12.7<br><sub>18,19,9,9,11</sub> | 6.9<br><sub>11,6,4,2,5</sub> |  | 3.3<br><sub>5,7,5,0,1</sub> |  | 1.1<br><sub>2,4,0,2,0</sub> |  | 0.7<br><sub>3,2,0,0,1</sub> |  | 0.3 | 0.3 | 0.6 | 11.3 |
| Hugo Gonzalez (BOS) | 98% | 11.6<br><sub>14,15,10,19,8</sub> | 3.6<br><sub>4,8,0,10,0</sub> |  | 2.4<br><sub>2,1,2,2,1</sub> |  | 0.6<br><sub>0,0,1,2,0</sub> |  | 0.3<br><sub>0,1,0,2,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.5 |
| Mike Conley (BOS) | 48% | 8.0<br><sub>-,11,10,-,-</sub> | 2.4<br><sub>-,0,3,-,-</sub> |  | 0.8<br><sub>-,0,3,-,-</sub> |  | 1.2<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,0,1,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.5 |
| Dillon Mitchell (BOS) | 21% | 6.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 0.9 |
| Ron Harper Jr. (BOS) | 58% | 6.8<br><sub>-,10,4,4,-</sub> | 2.9<br><sub>-,3,2,0,-</sub> |  | 1.0<br><sub>-,0,0,1,-</sub> |  | 0.6<br><sub>-,2,0,0,-</sub> |  | 0.3<br><sub>-,1,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Chris Cenac Jr. (BOS) | 38% | 5.9<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.7 | 4.9 |
| Amari Williams (BOS) | 17% | 5.1<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.6 |
| Cooper Flagg (DAL) | 98% | 35.5<br><sub>33,28,39,27,38</sub> | 21.9<br><sub>21,25,43,12,18</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>10,5,10,7,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>7,12,6,3,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>1,3,3,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.7 | 2.7 | 34.4 |
| Kyrie Irving (DAL) | 100% | 34.8<br><sub>28,29,38,27,37</sub> | 20.8<br><sub>14,21,35,10,34</sub> | 19.5 · – | 4.2<br><sub>2,3,0,3,6</sub> | 3.5 | 4.2<br><sub>2,4,4,4,5</sub> | 3.5 | 2.5<br><sub>0,2,7,2,7</sub> | 2.5 | 1.0 | 0.4 | 2.2 | 29.2 |
| P.J. Washington (DAL) | 98% | 32.5<br><sub>33,25,35,16,26</sub> | 13.3<br><sub>26,6,13,10,10</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 6.8<br><sub>6,5,9,3,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,0,1,0,1</sub> |  | 1.8<br><sub>6,2,2,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.8 | 1.6 | 21.8 |
| Naji Marshall (DAL) | 91% | 27.5<br><sub>25,15,25,23,30</sub> | 12.9<br><sub>7,8,6,13,12</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>1,1,5,1,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,2,2,4,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>0,1,0,1,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.1 | 1.6 | 20.2 |
| Caleb Martin (DAL) | 98% | 23.2<br><sub>11,19,19,21,33</sub> | 6.2<br><sub>0,2,0,7,15</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>0,2,3,2,8</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,2,5,5,3</sub> |  | 0.6<br><sub>0,0,0,1,1</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.3 | 0.9 | 11.5 |
| Daniel Gafford (DAL) | 92% | 21.4<br><sub>18,19,20,16,17</sub> | 8.4<br><sub>7,18,8,3,10</sub> |  | 5.7<br><sub>1,5,2,3,3</sub> |  | 1.2<br><sub>1,2,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,1</sub> |  | 0.5 | 1.1 | 1.1 | 15.3 |
| Zaccharie Risacher (DAL) | 98% | 20.1<br><sub>21,16,15,25,14</sub> | 7.1<br><sub>4,11,4,22,5</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,6,2,6,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,1,0,3,0</sub> |  | 0.9<br><sub>0,1,0,4,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.6 | 0.8 | 11.8 |
| Walter Clayton Jr. (DAL) | 93% | 17.5<br><sub>23,16,25,22,13</sub> | 6.4<br><sub>12,5,6,5,2</sub> |  | 2.5<br><sub>4,4,6,1,2</sub> |  | 2.8<br><sub>2,6,4,4,2</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 0.5 | 0.2 | 1.2 | 11.7 |
| Morez Johnson Jr. (DAL) | 98% | 16.6<br><sub>24,19,-,13,15</sub> | 6.0<br><sub>13,4,-,0,4</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>17,9,-,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,1,-,0,0</sub> |  | 0.4<br><sub>1,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.8 | 10.4 |
| Marcus Sasser (DAL) | 58% | 12.4<br><sub>-,9,-,9,-</sub> | 4.3<br><sub>-,4,-,3,-</sub> |  | 1.0<br><sub>-,0,-,1,-</sub> |  | 1.4<br><sub>-,0,-,0,-</sub> |  | 0.6<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.6 | 6.7 |
| Moussa Cisse (DAL) | 58% | 7.5<br><sub>1,5,-,8,-</sub> | 2.4<br><sub>0,2,-,0,-</sub> |  | 2.5<br><sub>0,1,-,0,-</sub> |  | 0.2<br><sub>0,1,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.5 | 0.4 | 5.0 |
| Tobi Lawal (DAL) | 52% | 7.5<br><sub>1,5,-,12,-</sub> | 2.6<br><sub>0,2,-,0,-</sub> |  | 1.3<br><sub>0,0,-,6,-</sub> |  | 0.5<br><sub>0,0,-,1,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.4 |
| Jett Howard (DAL) | 52% | 6.7<br><sub>1,3,-,5,-</sub> | 2.7<br><sub>0,5,-,3,-</sub> |  | 0.8<br><sub>0,1,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>0,1,-,1,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.9 |

</details>


### NYK @ TOR
Out: Kawhi Leonard (TOR), Malachi Smith (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.3–107.9 | NYK 67% | 1.48 / 3.07 | TOR +6.5 | 221.5 | TOR +5.5 covers 48%; o217.5 59% |
| Expected (weighted by chance each plays) | 113.9–108.0 | NYK 66% | 1.52 / 2.94 | TOR +5.5 | 221.5 | TOR +5.5 covers 49%; o217.5 58% |
| if Scottie Barnes plays | 113.4–108.4 | NYK 64% | 1.57 / 2.77 | TOR +5.5 | 221.5 | TOR +5.5 covers 51%; o217.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes (TOR) | Questionable | 55% | 31.5 | 18.7 | 6.3 | 6.1 | 0.7 | 1.5 | 1.1 | 2.8 | 31.1 | full tables below |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 35.1<br><sub>28,34,28,35,36</sub> | 26.8<br><sub>33,31,23,27,33</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>2,6,4,3,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 6.1<br><sub>4,9,2,5,11</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>5,3,1,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.1 | 2.9 | 35.9 |
| OG Anunoby | 98% | 33.5<br><sub>24,34,29,34,33</sub> | 17.1<br><sub>18,15,19,14,11</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>5,6,3,6,2</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,3,5,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 1.9 | 24.1 |
| Karl-Anthony Towns | 98% | 32.4<br><sub>25,34,27,34,34</sub> | 18.7<br><sub>17,29,21,21,23</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 12.3<br><sub>12,13,16,11,15</sub> | 12.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,3,3,8,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.8 | 2.9 | 34.6 |
| Josh Hart | 98% | 29.6<br><sub>-,-,-,26,23</sub> | 9.3<br><sub>-,-,-,6,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>-,-,-,4,5</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>-,-,-,3,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 1.7 | 19.8 |
| Mikal Bridges | 98% | 25.7<br><sub>22,31,17,17,29</sub> | 9.3<br><sub>7,9,4,2,18</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>4,6,5,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>4,4,1,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.4 | 1.0 | 14.5 |
| Landry Shamet | 98% | 23.4<br><sub>25,29,28,29,21</sub> | 8.0<br><sub>7,9,10,12,5</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,3,2,3</sub> |  | 1.3<br><sub>2,1,2,4,1</sub> |  | 1.4<br><sub>1,3,2,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.5 | 0.2 | 0.9 | 11.1 |
| Miles McBride | 98% | 19.6<br><sub>11,16,25,27,22</sub> | 7.4<br><sub>7,5,8,19,9</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,0,0,2,1</sub> |  | 1.4<br><sub>1,0,3,2,1</sub> |  | 1.3<br><sub>2,1,2,5,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.2 | 0.7 | 10.4 |
| Tyler Kolek | 91% | 13.7<br><sub>11,14,15,13,19</sub> | 4.3<br><sub>0,0,12,4,5</sub> |  | 1.9<br><sub>0,4,3,1,6</sub> |  | 3.4<br><sub>5,5,4,4,2</sub> |  | 0.5<br><sub>0,0,2,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.7 |
| Andre Drummond | 98% | 13.5<br><sub>12,14,16,14,14</sub> | 4.2<br><sub>6,0,2,0,0</sub> |  | 6.0<br><sub>9,8,14,4,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>0,0,3,3,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.8 | 11.1 |
| Jordan Clarkson | 76% | 10.2<br><sub>15,15,11,-,9</sub> | 4.7<br><sub>10,9,2,-,0</sub> |  | 1.4<br><sub>1,2,4,-,1</sub> |  | 0.7<br><sub>1,0,2,-,0</sub> |  | 0.3<br><sub>2,1,0,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.8 |
| Mohamed Diawara | 63% | 8.6<br><sub>21,14,18,11,-</sub> | 2.9<br><sub>8,2,5,2,-</sub> |  | 1.4<br><sub>6,3,3,0,-</sub> |  | 0.9<br><sub>4,3,3,0,-</sub> |  | 0.2<br><sub>1,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Jose Alvarado | 52% | 8.3<br><sub>9,-,6,-,-</sub> | 3.2<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 1.2<br><sub>2,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.6 |
| Dalton Knecht | 64% | 6.7<br><sub>16,5,8,-,-</sub> | 3.0<br><sub>10,0,3,-,-</sub> |  | 1.3<br><sub>7,0,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>2,0,1,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.7 |
| Jaden Akins | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.0 |
| James Wiseman | 48% | 6.4<br><sub>10,-,5,-,-</sub> | 2.3<br><sub>8,-,0,-,-</sub> |  | 2.1<br><sub>8,-,1,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 4.7 |
| Pacome Dadiet | 52% | 6.3<br><sub>9,-,6,-,1</sub> | 2.7<br><sub>4,-,8,-,0</sub> |  | 1.2<br><sub>0,-,2,-,0</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.2<br><sub>0,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 35.5<br><sub>33,37,36,31,37</sub> | 22.5<br><sub>22,27,19,12,31</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>5,7,3,8,14</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>3,5,2,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,0,1,0,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.4 | 2.6 | 33.5 |
| Immanuel Quickley | 86% | 31.8<br><sub>32,-,-,28,28</sub> | 16.8<br><sub>13,-,-,11,26</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>1,-,-,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>7,-,-,4,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>2,-,-,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.1 | 1.7 | 26.9 |
| Ja'Kobe Walter | 98% | 31.5<br><sub>27,29,34,35,32</sub> | 11.9<br><sub>8,7,12,17,6</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 3.7<br><sub>1,6,6,3,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,1,2,5,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 1.1 | 17.6 |
| Collin Murray-Boyles | 98% | 28.7<br><sub>23,34,-,20,32</sub> | 12.7<br><sub>13,19,-,5,14</sub> |  | 5.6<br><sub>3,7,-,4,0</sub> |  | 2.6<br><sub>2,2,-,3,4</sub> |  | 0.6<br><sub>1,0,-,1,1</sub> |  | 1.1 | 1.2 | 1.8 | 20.9 |
| Jakob Poeltl | 91% | 26.7<br><sub>19,31,31,32,25</sub> | 10.3<br><sub>8,19,18,6,9</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>5,11,8,9,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,1,2,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.0 | 1.5 | 19.6 |
| Jamal Shead | 98% | 25.7<br><sub>20,34,36,22,22</sub> | 8.4<br><sub>3,10,20,3,5</sub> |  | 1.9<br><sub>3,3,2,3,1</sub> |  | 6.2<br><sub>6,16,11,6,5</sub> |  | 1.1<br><sub>1,1,4,0,1</sub> |  | 1.0 | 0.2 | 1.9 | 16.5 |
| Jamison Battle | 98% | 24.1<br><sub>19,21,29,25,25</sub> | 10.8<br><sub>9,6,18,12,13</sub> |  | 2.7<br><sub>1,2,1,2,1</sub> |  | 1.0<br><sub>0,0,2,0,1</sub> |  | 1.9<br><sub>2,1,5,2,3</sub> |  | 0.4 | 0.2 | 0.8 | 14.6 |
| Alijah Martin | 91% | 16.1<br><sub>9,31,21,16,18</sub> | 6.5<br><sub>6,27,2,12,7</sub> |  | 2.1<br><sub>1,4,3,1,4</sub> |  | 1.3<br><sub>0,1,3,0,1</sub> |  | 0.8<br><sub>0,6,0,4,1</sub> |  | 0.6 | 0.3 | 1.0 | 9.9 |
| Allen Graves | 98% | 15.1<br><sub>14,16,13,18,13</sub> | 5.0<br><sub>5,3,3,13,0</sub> |  | 2.4<br><sub>1,2,2,5,2</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>1,0,1,3,0</sub> |  | 0.4 | 0.4 | 0.6 | 8.2 |
| Kyle Anderson | 80% | 11.8<br><sub>4,-,16,11,5</sub> | 3.2<br><sub>2,-,6,2,0</sub> |  | 2.0<br><sub>0,-,2,3,0</sub> |  | 2.0<br><sub>1,-,2,4,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.4 | 0.6 | 7.2 |
| Trayce Jackson-Davis | 64% | 9.9<br><sub>4,-,14,-,-</sub> | 3.6<br><sub>1,-,4,-,-</sub> |  | 2.9<br><sub>0,-,6,-,-</sub> |  | 0.6<br><sub>0,-,1,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.5 | 0.5 | 7.1 |
| Jaden Bradley | 67% | 7.7<br><sub>4,8,9,-,2</sub> | 2.7<br><sub>2,3,0,-,1</sub> |  | 1.1<br><sub>1,0,1,-,0</sub> |  | 1.2<br><sub>0,1,3,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.0 |

</details>

<details><summary>if Scottie Barnes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 98% | 35.0<br><sub>28,34,28,35,36</sub> | 26.7<br><sub>33,31,23,27,33</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>2,6,4,3,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 6.1<br><sub>4,9,2,5,11</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>5,3,1,3,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.1 | 2.9 | 35.9 |
| OG Anunoby (NYK) | 98% | 33.5<br><sub>24,34,29,34,33</sub> | 17.1<br><sub>18,15,19,14,11</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>5,6,3,6,2</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>2,2,2,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>1,3,5,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 1.9 | 24.1 |
| Karl-Anthony Towns (NYK) | 98% | 32.5<br><sub>25,34,27,34,34</sub> | 18.6<br><sub>17,29,21,21,23</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 12.3<br><sub>12,13,16,11,15</sub> | 12.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>1,3,3,8,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.7 | 3.0 | 34.6 |
| Josh Hart (NYK) | 98% | 29.6<br><sub>-,-,-,26,23</sub> | 9.3<br><sub>-,-,-,6,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>-,-,-,4,5</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>-,-,-,3,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 1.7 | 19.7 |
| Mikal Bridges (NYK) | 98% | 25.6<br><sub>22,31,17,17,29</sub> | 9.3<br><sub>7,9,4,2,18</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>4,6,5,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>4,4,1,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>1,1,0,0,2</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.4 | 1.0 | 14.4 |
| Landry Shamet (NYK) | 98% | 23.4<br><sub>25,29,28,29,21</sub> | 8.0<br><sub>7,9,10,12,5</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,1,3,2,3</sub> |  | 1.4<br><sub>2,1,2,4,1</sub> |  | 1.4<br><sub>1,3,2,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.5 | 0.2 | 0.9 | 11.1 |
| Miles McBride (NYK) | 98% | 19.6<br><sub>11,16,25,27,22</sub> | 7.3<br><sub>7,5,8,19,9</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,0,0,2,1</sub> |  | 1.4<br><sub>1,0,3,2,1</sub> |  | 1.3<br><sub>2,1,2,5,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.2 | 0.7 | 10.4 |
| Tyler Kolek (NYK) | 91% | 13.8<br><sub>11,14,15,13,19</sub> | 4.3<br><sub>0,0,12,4,5</sub> |  | 1.9<br><sub>0,4,3,1,6</sub> |  | 3.4<br><sub>5,5,4,4,2</sub> |  | 0.5<br><sub>0,0,2,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.7 |
| Andre Drummond (NYK) | 98% | 13.7<br><sub>12,14,16,14,14</sub> | 4.2<br><sub>6,0,2,0,0</sub> |  | 6.1<br><sub>9,8,14,4,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>0,0,3,3,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.8 | 11.3 |
| Jordan Clarkson (NYK) | 76% | 10.1<br><sub>15,15,11,-,9</sub> | 4.7<br><sub>10,9,2,-,0</sub> |  | 1.4<br><sub>1,2,4,-,1</sub> |  | 0.7<br><sub>1,0,2,-,0</sub> |  | 0.3<br><sub>2,1,0,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.8 |
| Mohamed Diawara (NYK) | 63% | 8.7<br><sub>21,14,18,11,-</sub> | 3.0<br><sub>8,2,5,2,-</sub> |  | 1.4<br><sub>6,3,3,0,-</sub> |  | 0.9<br><sub>4,3,3,0,-</sub> |  | 0.3<br><sub>1,0,1,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Jose Alvarado (NYK) | 52% | 8.4<br><sub>9,-,6,-,-</sub> | 3.3<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 1.3<br><sub>2,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.6 |
| Jaden Akins (NYK) | 38% | 6.8<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.0 |
| Dalton Knecht (NYK) | 64% | 6.6<br><sub>16,5,8,-,-</sub> | 3.0<br><sub>10,0,3,-,-</sub> |  | 1.2<br><sub>7,0,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.3<br><sub>2,0,1,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.6 |
| James Wiseman (NYK) | 48% | 6.4<br><sub>10,-,5,-,-</sub> | 2.2<br><sub>8,-,0,-,-</sub> |  | 2.1<br><sub>8,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 4.7 |
| Pacome Dadiet (NYK) | 52% | 6.2<br><sub>9,-,6,-,1</sub> | 2.6<br><sub>4,-,8,-,0</sub> |  | 1.2<br><sub>0,-,2,-,0</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.2<br><sub>0,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| RJ Barrett (TOR) | 98% | 32.5<br><sub>33,37,36,31,37</sub> | 19.3<br><sub>22,27,19,12,31</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>5,7,3,8,14</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.9<br><sub>3,5,2,7,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>3,0,1,0,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.4 | 2.2 | 29.2 |
| Scottie Barnes (TOR) | 100% | 31.5<br><sub>32,-,-,-,-</sub> | 18.7<br><sub>17,-,-,-,-</sub> | 18.5 · – | 6.3<br><sub>6,-,-,-,-</sub> | 6.5 | 6.1<br><sub>6,-,-,-,-</sub> | 4.5 | 0.7<br><sub>1,-,-,-,-</sub> | 0.5 | 1.5 | 1.1 | 2.8 | 31.1 |
| Immanuel Quickley (TOR) | 86% | 29.1<br><sub>32,-,-,28,28</sub> | 14.7<br><sub>13,-,-,11,26</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>1,-,-,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>7,-,-,4,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>2,-,-,1,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.1 | 1.5 | 23.2 |
| Ja'Kobe Walter (TOR) | 98% | 28.4<br><sub>27,29,34,35,32</sub> | 10.0<br><sub>8,7,12,17,6</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>1,6,6,3,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>1,1,2,5,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 0.8 | 15.0 |
| Collin Murray-Boyles (TOR) | 98% | 24.2<br><sub>23,34,-,20,32</sub> | 10.5<br><sub>13,19,-,5,14</sub> |  | 4.9<br><sub>3,7,-,4,0</sub> |  | 1.9<br><sub>2,2,-,3,4</sub> |  | 0.5<br><sub>1,0,-,1,1</sub> |  | 1.0 | 1.1 | 1.4 | 17.3 |
| Jakob Poeltl (TOR) | 91% | 23.4<br><sub>19,31,31,32,25</sub> | 8.8<br><sub>8,19,18,6,9</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>5,11,8,9,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,1,2,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.3 | 16.7 |
| Jamal Shead (TOR) | 98% | 22.9<br><sub>20,34,36,22,22</sub> | 7.0<br><sub>3,10,20,3,5</sub> |  | 1.7<br><sub>3,3,2,3,1</sub> |  | 5.1<br><sub>6,16,11,6,5</sub> |  | 0.9<br><sub>1,1,4,0,1</sub> |  | 0.9 | 0.2 | 1.6 | 13.7 |
| Jamison Battle (TOR) | 98% | 19.5<br><sub>19,21,29,25,25</sub> | 8.3<br><sub>9,6,18,12,13</sub> |  | 2.2<br><sub>1,2,1,2,1</sub> |  | 0.8<br><sub>0,0,2,0,1</sub> |  | 1.4<br><sub>2,1,5,2,3</sub> |  | 0.3 | 0.2 | 0.6 | 11.2 |
| Alijah Martin (TOR) | 91% | 14.1<br><sub>9,31,21,16,18</sub> | 5.7<br><sub>6,27,2,12,7</sub> |  | 1.9<br><sub>1,4,3,1,4</sub> |  | 1.2<br><sub>0,1,3,0,1</sub> |  | 0.6<br><sub>0,6,0,4,1</sub> |  | 0.6 | 0.2 | 0.8 | 8.7 |
| Allen Graves (TOR) | 98% | 12.9<br><sub>14,16,13,18,13</sub> | 4.2<br><sub>5,3,3,13,0</sub> |  | 2.1<br><sub>1,2,2,5,2</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.4<br><sub>1,0,1,3,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.9 |
| Kyle Anderson (TOR) | 80% | 8.1<br><sub>4,-,16,11,5</sub> | 2.2<br><sub>2,-,6,2,0</sub> |  | 1.4<br><sub>0,-,2,3,0</sub> |  | 1.4<br><sub>1,-,2,4,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 5.0 |
| Trayce Jackson-Davis (TOR) | 64% | 7.0<br><sub>4,-,14,-,-</sub> | 2.6<br><sub>1,-,4,-,-</sub> |  | 2.1<br><sub>0,-,6,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.4 | 0.3 | 5.1 |
| Jaden Bradley (TOR) | 67% | 6.4<br><sub>4,8,9,-,2</sub> | 2.3<br><sub>2,3,0,-,1</sub> |  | 0.9<br><sub>1,0,1,-,0</sub> |  | 1.1<br><sub>0,1,3,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |

</details>


### HOU @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Clint Capela (HOU), Marcus Smart (HOU), Fred VanVleet (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 120.2–109.4 | HOU 78% | 1.28 / 4.52 | WAS +10.5 | 229.5 | WAS +8.5 covers 43%; o224.5 61% |
| Expected (weighted by chance each plays) | 119.6–110.1 | HOU 75% | 1.33 / 4.07 | WAS +9.5 | 229.5 | WAS +8.5 covers 47%; o224.5 61% |
| if Alex Sarr plays | 119.8–110.5 | HOU 74% | 1.34 / 3.91 | WAS +9.5 | 230.5 | WAS +8.5 covers 48%; o224.5 62% |
| if Tre Johnson plays | 119.8–109.6 | HOU 77% | 1.30 / 4.28 | WAS +10.5 | 229.5 | WAS +8.5 covers 45%; o224.5 60% |
| if Bub Carrington plays | 119.7–109.5 | HOU 77% | 1.30 / 4.30 | WAS +10.5 | 229.5 | WAS +8.5 covers 45%; o224.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Questionable | 55% | 9.1 | 2.6 | 2.5 | 0.5 | 0.1 | 0.3 | 0.4 | 0.6 | 5.7 | small |
| Alex Sarr (WAS) | Questionable | 55% | 31.5 | 13.1 | 8.2 | 2.3 | 1.3 | 1.0 | 1.7 | 1.5 | 23.6 | full tables below |
| Tre Johnson (WAS) | Questionable | 55% | 28.9 | 11.8 | 2.5 | 1.5 | 1.8 | 0.9 | 0.2 | 1.4 | 15.8 | full tables below |
| Bub Carrington (WAS) | Questionable | 55% | 20.9 | 7.1 | 2.2 | 2.6 | 1.1 | 0.6 | 0.2 | 1.2 | 11.8 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.3<br><sub>32,39,35,29,41</sub> | 18.9<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.9<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.8 | 0.7 | 2.2 | 32.2 |
| Kevin Durant | 98% | 36.7<br><sub>35,38,36,34,33</sub> | 26.5<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 1.0 | 3.4 | 38.4 |
| Alperen Sengun | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.2<br><sub>17,15,20,19,43</sub> | 19.5 · –<br><sub>o 54% · u 46%</sub> | 10.6<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 7.5<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.6 | 1.1 | 3.2 | 43.3 |
| Jabari Smith Jr. | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.2<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.9 | 1.4 | 26.7 |
| Tari Eason | 98% | 30.5<br><sub>24,23,19,22,33</sub> | 13.0<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.8 | 1.3 | 22.6 |
| Reed Sheppard | 88% | 26.3<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.5 | 1.2 | 19.2 |
| Bogdan Bogdanovic | 97% | 16.7<br><sub>5,2,12,10,12</sub> | 6.3<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams | 23% | 15.2<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 5.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.6 | 0.9 | 10.8 |
| Oscar Tshiebwe | 91% | 12.1<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.3<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.6 |
| Jae'Sean Tate | 52% | 10.8<br><sub>-,-,-,1,-</sub> | 3.0<br><sub>-,-,-,0,-</sub> |  | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.3 |
| Bruce Thornton | 58% | 10.8<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Isaiah Crawford | 58% | 9.8<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.8 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 38.1<br><sub>36,31,37,34,44</sub> | 16.6<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.6 | 2.6 | 25.8 |
| Trae Young | 98% | 38.0<br><sub>37,28,38,34,45</sub> | 22.6<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 9.3<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 4.1 | 35.2 |
| Anthony Davis | 98% | 37.6<br><sub>-,-,34,34,44</sub> | 25.5<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 11.8<br><sub>-,-,13,13,15</sub> | 9.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.3 | 1.6 | 2.5 | 40.2 |
| Kyshawn George | 98% | 35.7<br><sub>39,30,35,39,26</sub> | 18.4<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 1.1 | 2.7 | 28.2 |
| Bilal Coulibaly | 98% | 30.4<br><sub>24,20,-,25,29</sub> | 11.0<br><sub>9,0,-,5,4</sub> |  | 4.5<br><sub>5,5,-,6,7</sub> |  | 1.9<br><sub>0,0,-,2,0</sub> |  | 1.1<br><sub>1,0,-,0,0</sub> |  | 1.4 | 1.0 | 1.3 | 17.5 |
| Deandre Ayton | 98% | 19.6<br><sub>23,7,13,9,9</sub> | 6.3<br><sub>8,2,2,2,2</sub> |  | 6.3<br><sub>11,1,8,2,4</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.7 | 13.4 |
| Khris Middleton | 35% | 16.6<br><sub>-,-,-,-,-</sub> | 5.4<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 1.0 | 9.0 |
| Will Riley | 76% | 15.0<br><sub>9,20,4,-,3</sub> | 6.1<br><sub>7,5,0,-,3</sub> |  | 1.7<br><sub>0,2,0,-,0</sub> |  | 1.0<br><sub>0,1,1,-,0</sub> |  | 0.6<br><sub>1,0,0,-,1</sub> |  | 0.5 | 0.1 | 0.7 | 8.9 |
| Anthony Gill | 43% | 11.6<br><sub>-,9,2,-,-</sub> | 3.9<br><sub>-,1,0,-,-</sub> |  | 1.9<br><sub>-,1,2,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 6.5 |
| Tre Mann | 52% | 11.0<br><sub>-,18,2,-,-</sub> | 3.9<br><sub>-,2,0,-,-</sub> |  | 1.1<br><sub>-,0,0,-,-</sub> |  | 1.0<br><sub>-,2,0,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.5 | 0.1 | 0.6 | 6.1 |

</details>

<details><summary>if Alex Sarr plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 37.4<br><sub>32,39,35,29,41</sub> | 18.9<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.8 | 0.7 | 2.2 | 32.2 |
| Alperen Sengun (HOU) | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.1<br><sub>17,15,20,19,43</sub> | 19.5 · –<br><sub>o 54% · u 46%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.6 | 1.1 | 3.2 | 43.3 |
| Kevin Durant (HOU) | 98% | 36.6<br><sub>35,38,36,34,33</sub> | 26.3<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 1.0 | 3.5 | 38.1 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.3<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.9 | 1.4 | 26.7 |
| Tari Eason (HOU) | 98% | 30.5<br><sub>24,23,19,22,33</sub> | 12.8<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.8 | 1.3 | 22.4 |
| Reed Sheppard (HOU) | 88% | 26.2<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7 | 0.5 | 1.3 | 19.2 |
| Bogdan Bogdanovic (HOU) | 97% | 16.8<br><sub>5,2,12,10,12</sub> | 6.2<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams (HOU) | 23% | 15.4<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 6.0<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.6 | 0.9 | 11.0 |
| Oscar Tshiebwe (HOU) | 91% | 12.1<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.4<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.7 |
| Jae'Sean Tate (HOU) | 52% | 10.9<br><sub>-,-,-,1,-</sub> | 3.1<br><sub>-,-,-,0,-</sub> |  | 2.5<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.3 |
| Bruce Thornton (HOU) | 58% | 10.9<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Isaiah Crawford (HOU) | 58% | 9.8<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.7 |
| Trae Young (WAS) | 98% | 37.5<br><sub>37,28,38,34,45</sub> | 21.5<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 9.6<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.6 | 34.3 |
| Anthony Davis (WAS) | 98% | 36.9<br><sub>-,-,34,34,44</sub> | 23.5<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 11.8<br><sub>-,-,13,13,15</sub> | 9.5<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.3 | 1.7 | 2.3 | 38.2 |
| AJ Dybantsa (WAS) | 98% | 36.6<br><sub>36,31,37,34,44</sub> | 15.5<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 2.4 | 24.4 |
| Kyshawn George (WAS) | 98% | 34.7<br><sub>39,30,35,39,26</sub> | 16.8<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 1.1 | 2.5 | 26.1 |
| Alex Sarr (WAS) | 100% | 31.5<br><sub>30,28,25,25,44</sub> | 13.1<br><sub>13,15,4,5,30</sub> | 10.5 · – | 8.2<br><sub>8,14,8,8,9</sub> | 6.5 | 2.3<br><sub>3,1,0,0,2</sub> | 1.5 | 1.3<br><sub>1,1,0,1,4</sub> | 0.5 | 1.0 | 1.7 | 1.5 | 23.6 |
| Bilal Coulibaly (WAS) | 98% | 27.9<br><sub>24,20,-,25,29</sub> | 9.8<br><sub>9,0,-,5,4</sub> |  | 4.1<br><sub>5,5,-,6,7</sub> |  | 1.7<br><sub>0,0,-,2,0</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 1.3 | 0.9 | 1.3 | 15.6 |
| Deandre Ayton (WAS) | 98% | 15.5<br><sub>23,7,13,9,9</sub> | 5.0<br><sub>8,2,2,2,2</sub> |  | 4.9<br><sub>11,1,8,2,4</sub> |  | 0.6<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 10.6 |
| Khris Middleton (WAS) | 35% | 13.6<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.9 | 7.2 |
| Will Riley (WAS) | 76% | 11.5<br><sub>9,20,4,-,3</sub> | 4.5<br><sub>7,5,0,-,3</sub> |  | 1.3<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.4<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 6.7 |
| Anthony Gill (WAS) | 43% | 8.5<br><sub>-,9,2,-,-</sub> | 2.8<br><sub>-,1,0,-,-</sub> |  | 1.3<br><sub>-,1,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |
| Tre Mann (WAS) | 52% | 8.4<br><sub>-,18,2,-,-</sub> | 3.0<br><sub>-,2,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,2,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.6 |

</details>

<details><summary>if Bub Carrington plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 37.4<br><sub>32,39,35,29,41</sub> | 18.9<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.7 | 0.7 | 2.2 | 32.2 |
| Alperen Sengun (HOU) | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.0<br><sub>17,15,20,19,43</sub> | 19.5 · –<br><sub>o 54% · u 46%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.6 | 1.1 | 3.2 | 43.3 |
| Kevin Durant (HOU) | 98% | 36.6<br><sub>35,38,36,34,33</sub> | 26.3<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 1.0 | 3.4 | 38.1 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.2<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.8 | 1.4 | 26.6 |
| Tari Eason (HOU) | 98% | 30.5<br><sub>24,23,19,22,33</sub> | 12.8<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.8 | 1.3 | 22.4 |
| Reed Sheppard (HOU) | 88% | 26.3<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.5 | 1.3 | 19.2 |
| Bogdan Bogdanovic (HOU) | 97% | 16.8<br><sub>5,2,12,10,12</sub> | 6.2<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams (HOU) | 23% | 15.2<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 5.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.5 | 0.9 | 10.8 |
| Oscar Tshiebwe (HOU) | 91% | 12.1<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.4<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.6 |
| Jae'Sean Tate (HOU) | 52% | 11.0<br><sub>-,-,-,1,-</sub> | 3.1<br><sub>-,-,-,0,-</sub> |  | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.3 |
| Bruce Thornton (HOU) | 58% | 10.9<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.2 |
| Isaiah Crawford (HOU) | 58% | 9.9<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.8 |
| Trae Young (WAS) | 98% | 37.5<br><sub>37,28,38,34,45</sub> | 21.8<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 9.3<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.7 | 34.4 |
| Anthony Davis (WAS) | 98% | 37.2<br><sub>-,-,34,34,44</sub> | 24.3<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 11.9<br><sub>-,-,13,13,15</sub> | 9.5<br><sub>o 56% · u 44%</sub> | 2.9<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.4 | 1.6 | 2.4 | 39.1 |
| AJ Dybantsa (WAS) | 98% | 37.2<br><sub>36,31,37,34,44</sub> | 15.7<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.4<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.6 | 2.5 | 24.7 |
| Kyshawn George (WAS) | 98% | 35.2<br><sub>39,30,35,39,26</sub> | 17.3<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 1.1 | 2.5 | 27.0 |
| Bilal Coulibaly (WAS) | 98% | 29.0<br><sub>24,20,-,25,29</sub> | 10.8<br><sub>9,0,-,5,4</sub> |  | 4.4<br><sub>5,5,-,6,7</sub> |  | 1.7<br><sub>0,0,-,2,0</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 1.3 | 1.0 | 1.3 | 16.9 |
| Bub Carrington (WAS) | 100% | 20.9<br><sub>15,21,19,10,16</sub> | 7.1<br><sub>5,9,4,0,2</sub> |  | 2.2<br><sub>1,6,0,0,0</sub> |  | 2.6<br><sub>1,1,4,0,2</sub> |  | 1.1<br><sub>1,3,1,0,0</sub> |  | 0.6 | 0.2 | 1.2 | 11.8 |
| Deandre Ayton (WAS) | 98% | 17.6<br><sub>23,7,13,9,9</sub> | 5.8<br><sub>8,2,2,2,2</sub> |  | 5.7<br><sub>11,1,8,2,4</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.7 | 12.2 |
| Khris Middleton (WAS) | 35% | 14.9<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 8.2 |
| Will Riley (WAS) | 76% | 12.2<br><sub>9,20,4,-,3</sub> | 4.9<br><sub>7,5,0,-,3</sub> |  | 1.4<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.5<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 7.2 |
| Anthony Gill (WAS) | 43% | 9.4<br><sub>-,9,2,-,-</sub> | 3.2<br><sub>-,1,0,-,-</sub> |  | 1.5<br><sub>-,1,2,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |
| Tre Mann (WAS) | 52% | 8.9<br><sub>-,18,2,-,-</sub> | 3.2<br><sub>-,2,0,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,2,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.9 |

</details>

<details><summary>if Tre Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 37.3<br><sub>32,39,35,29,41</sub> | 18.8<br><sub>11,17,8,19,12</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.9<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.8 | 0.7 | 2.2 | 32.0 |
| Alperen Sengun (HOU) | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.1<br><sub>17,15,20,19,43</sub> | 19.5 · –<br><sub>o 54% · u 46%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.6 | 1.1 | 3.2 | 43.3 |
| Kevin Durant (HOU) | 98% | 36.6<br><sub>35,38,36,34,33</sub> | 26.3<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 1.0 | 3.4 | 38.2 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.2<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.8 | 1.4 | 26.7 |
| Tari Eason (HOU) | 98% | 30.6<br><sub>24,23,19,22,33</sub> | 12.9<br><sub>9,2,12,6,14</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.8 | 1.3 | 22.5 |
| Reed Sheppard (HOU) | 88% | 26.3<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.5 | 1.3 | 19.2 |
| Bogdan Bogdanovic (HOU) | 97% | 16.7<br><sub>5,2,12,10,12</sub> | 6.3<br><sub>0,0,8,0,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 1.0<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.6 | 10.1 |
| Steven Adams (HOU) | 23% | 15.3<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 6.0<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.6 | 0.9 | 10.8 |
| Oscar Tshiebwe (HOU) | 91% | 12.0<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.3<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.6 |
| Jae'Sean Tate (HOU) | 52% | 10.9<br><sub>-,-,-,1,-</sub> | 3.1<br><sub>-,-,-,0,-</sub> |  | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.4 |
| Bruce Thornton (HOU) | 58% | 10.9<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.3 |
| Isaiah Crawford (HOU) | 58% | 9.8<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.8 |
| Trae Young (WAS) | 98% | 37.3<br><sub>37,28,38,34,45</sub> | 21.1<br><sub>23,4,20,15,37</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 9.4<br><sub>10,3,7,4,14</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.2 | 3.5 | 33.7 |
| Anthony Davis (WAS) | 98% | 36.9<br><sub>-,-,34,34,44</sub> | 23.2<br><sub>-,-,44,21,30</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 11.9<br><sub>-,-,13,13,15</sub> | 9.5<br><sub>o 56% · u 44%</sub> | 2.9<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.4 | 1.7 | 2.4 | 38.0 |
| AJ Dybantsa (WAS) | 98% | 36.8<br><sub>36,31,37,34,44</sub> | 15.4<br><sub>11,19,21,13,5</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 2.4 | 24.3 |
| Kyshawn George (WAS) | 98% | 34.9<br><sub>39,30,35,39,26</sub> | 17.1<br><sub>33,14,12,25,14</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 1.1 | 2.5 | 26.7 |
| Tre Johnson (WAS) | 100% | 28.9<br><sub>27,28,29,29,30</sub> | 11.8<br><sub>23,4,2,15,13</sub> | 10.5 · – | 2.5<br><sub>1,0,2,3,4</sub> | 2.5 | 1.5<br><sub>1,3,0,1,2</sub> | 1.5 | 1.8<br><sub>5,0,0,2,1</sub> | 1.5 | 0.9 | 0.2 | 1.4 | 15.8 |
| Bilal Coulibaly (WAS) | 98% | 28.2<br><sub>24,20,-,25,29</sub> | 10.0<br><sub>9,0,-,5,4</sub> |  | 4.3<br><sub>5,5,-,6,7</sub> |  | 1.7<br><sub>0,0,-,2,0</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 1.3 | 0.9 | 1.2 | 16.0 |
| Deandre Ayton (WAS) | 98% | 16.6<br><sub>23,7,13,9,9</sub> | 5.4<br><sub>8,2,2,2,2</sub> |  | 5.4<br><sub>11,1,8,2,4</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 0.6 | 11.5 |
| Khris Middleton (WAS) | 35% | 14.2<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.9 | 7.6 |
| Will Riley (WAS) | 76% | 11.7<br><sub>9,20,4,-,3</sub> | 4.6<br><sub>7,5,0,-,3</sub> |  | 1.3<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.4<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 6.8 |
| Anthony Gill (WAS) | 43% | 8.6<br><sub>-,9,2,-,-</sub> | 2.9<br><sub>-,1,0,-,-</sub> |  | 1.4<br><sub>-,1,2,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Tre Mann (WAS) | 52% | 8.4<br><sub>-,18,2,-,-</sub> | 3.0<br><sub>-,2,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,2,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.6 |

</details>


### ATL @ MIL
Out: Ousmane Dieng (MIL), Kam Jones (MIL), Pete Nance (MIL), Cormac Ryan (MIL), Kingston Flemings (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Asa Newell (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.5–110.2 | ATL 72% | 1.38 / 3.60 | MIL +8.5 | 228.5 | MIL +8.5 covers 50%; o233.5 40% |
| Expected (weighted by chance each plays) | 119.3–110.8 | ATL 73% | 1.37 / 3.69 | MIL +8.5 | 229.5 | MIL +8.5 covers 49%; o233.5 42% |
| if Ryan Rollins plays | 118.7–111.3 | ATL 70% | 1.43 / 3.34 | MIL +7.5 | 229.5 | MIL +8.5 covers 53%; o233.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 9.3 | 3.6 | 1.5 | 0.7 | 0.3 | 0.2 | 0.1 | 0.4 | 5.8 | small |
| Ryan Rollins (MIL) | Questionable | 55% | 26.4 | 13.5 | 4.5 | 5.2 | 1.8 | 1.2 | 0.4 | 2.7 | 23.2 | full tables below |
| Jock Landale (ATL) | Questionable | 55% | 15.0 | 6.9 | 4.0 | 1.4 | 0.6 | 0.4 | 0.4 | 0.7 | 12.3 | small |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 35.6<br><sub>-,-,36,38,40</sub> | 22.2<br><sub>-,-,30,15,27</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>-,-,7,7,11</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 8.0<br><sub>-,-,6,4,10</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.5 | 3.0 | 39.8 |
| Nickeil Alexander-Walker | 98% | 34.5<br><sub>32,33,31,34,41</sub> | 22.7<br><sub>26,28,20,20,16</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,2,3,4,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,1,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.8<br><sub>6,4,2,4,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.5 | 2.2 | 29.9 |
| Dyson Daniels | 98% | 33.1<br><sub>34,35,31,31,36</sub> | 11.3<br><sub>8,13,9,10,6</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 8.0<br><sub>16,9,10,6,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>8,12,7,8,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 2.5 | 0.4 | 1.5 | 25.5 |
| Onyeka Okongwu | 98% | 32.5<br><sub>31,33,30,30,35</sub> | 15.7<br><sub>14,22,16,16,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 8.0<br><sub>16,10,2,9,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>4,1,5,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 1.0 | 1.4 | 26.9 |
| CJ McCollum | 98% | 28.6<br><sub>25,23,21,24,32</sub> | 17.5<br><sub>15,4,9,21,20</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>5,3,4,0,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 4.2<br><sub>5,4,3,4,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,0,1,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.6 | 2.0 | 25.0 |
| Aaron Wiggins | 98% | 26.0<br><sub>29,29,26,23,26</sub> | 13.5<br><sub>15,19,20,15,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>4,4,4,3,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>2,3,6,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>3,3,5,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.4 | 1.1 | 19.5 |
| Luguentz Dort | 98% | 24.1<br><sub>31,32,20,18,20</sub> | 8.7<br><sub>6,25,3,4,10</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,7,2,3,1</sub> |  | 1.7<br><sub>3,4,1,2,2</sub> |  | 1.4<br><sub>2,5,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.3 | 0.7 | 13.6 |
| Zuby Ejiofor | 63% | 12.0<br><sub>17,15,18,4,-</sub> | 4.1<br><sub>11,10,7,0,-</sub> |  | 2.8<br><sub>3,5,6,0,-</sub> |  | 1.1<br><sub>2,5,0,0,-</sub> |  | 0.3<br><sub>1,0,1,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.0 |
| Corey Kispert | 52% | 11.7<br><sub>8,16,-,-,-</sub> | 6.2<br><sub>9,7,-,-,-</sub> |  | 1.5<br><sub>0,2,-,-,-</sub> |  | 1.0<br><sub>1,1,-,-,-</sub> |  | 0.8<br><sub>1,1,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 8.7 |
| RayJ Dennis | 52% | 10.2<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.4 |
| Dorian Finney-Smith | 26% | 7.1<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.6 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 34.3<br><sub>35,27,-,35,34</sub> | 22.7<br><sub>23,13,-,27,18</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>5,1,-,2,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>10,2,-,7,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.7<br><sub>1,1,-,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.3 | 2.9 | 33.2 |
| Kyle Kuzma | 98% | 30.7<br><sub>32,31,26,24,31</sub> | 14.8<br><sub>13,27,5,9,14</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 5.7<br><sub>4,4,5,1,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>3,0,3,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,6,1,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 2.4 | 24.1 |
| Jaime Jaquez Jr. | 98% | 30.3<br><sub>28,23,25,30,28</sub> | 17.5<br><sub>14,4,16,25,22</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 5.8<br><sub>3,2,5,5,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>3,2,3,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>2,0,2,2,5</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 2.4 | 28.3 |
| Myles Turner | 98% | 29.3<br><sub>24,24,27,-,31</sub> | 11.5<br><sub>0,3,3,-,14</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>7,5,3,-,11</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>0,7,2,-,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.6<br><sub>0,0,1,-,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 1.8 | 1.8 | 20.6 |
| Brayden Burries | 98% | 26.2<br><sub>38,29,26,23,19</sub> | 10.5<br><sub>21,13,3,8,3</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>11,8,3,5,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>6,4,3,1,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.3 | 1.6 | 19.4 |
| Nate Ament | 93% | 22.1<br><sub>15,23,22,22,22</sub> | 9.2<br><sub>7,12,10,2,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>1,5,2,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>0,1,1,1,1</sub> |  | 1.1<br><sub>0,2,2,0,2</sub> |  | 0.7 | 0.4 | 1.2 | 13.8 |
| AJ Green | 98% | 19.6<br><sub>24,18,8,8,8</sub> | 7.2<br><sub>12,5,0,3,0</sub> |  | 2.0<br><sub>1,1,0,1,0</sub> |  | 1.4<br><sub>0,1,0,1,2</sub> |  | 1.4<br><sub>4,1,0,1,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.6 |
| Kel'el Ware | 96% | 18.5<br><sub>13,9,17,23,17</sub> | 8.8<br><sub>4,0,8,8,10</sub> |  | 6.7<br><sub>3,0,4,5,6</sub> |  | 1.1<br><sub>0,1,1,1,1</sub> |  | 0.7<br><sub>0,0,0,0,2</sub> |  | 0.5 | 1.0 | 1.5 | 16.5 |
| Gary Trent Jr. | 63% | 16.9<br><sub>-,-,6,4,16</sub> | 7.3<br><sub>-,-,5,6,1</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> |  | 0.9<br><sub>-,-,0,0,0</sub> |  | 1.2<br><sub>-,-,1,2,0</sub> |  | 0.6 | 0.1 | 0.8 | 9.2 |
| Caris LeVert | 8% | 16.9<br><sub>-,-,-,-,-</sub> | 6.4<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.5 | 1.2 | 10.7 |
| Kasparas Jakucionis | 72% | 16.0<br><sub>10,7,23,4,-</sub> | 5.9<br><sub>3,1,11,4,-</sub> |  | 2.1<br><sub>0,2,0,2,-</sub> |  | 2.8<br><sub>2,0,4,0,-</sub> |  | 0.5<br><sub>0,0,2,0,-</sub> |  | 0.6 | 0.2 | 1.4 | 10.9 |
| Jericho Sims | 66% | 14.2<br><sub>7,15,8,18,-</sub> | 3.1<br><sub>0,2,2,0,-</sub> |  | 3.9<br><sub>1,2,0,4,-</sub> |  | 1.3<br><sub>0,0,0,1,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.2 | 0.9 | 8.3 |

</details>

<details><summary>if Ryan Rollins plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 35.6<br><sub>-,-,36,38,40</sub> | 22.3<br><sub>-,-,30,15,27</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>-,-,7,7,11</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 7.9<br><sub>-,-,6,4,10</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.5 | 3.0 | 39.8 |
| Nickeil Alexander-Walker (ATL) | 98% | 34.5<br><sub>32,33,31,34,41</sub> | 22.7<br><sub>26,28,20,20,16</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,2,3,4,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,1,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.8<br><sub>6,4,2,4,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.5 | 2.1 | 29.8 |
| Dyson Daniels (ATL) | 98% | 33.1<br><sub>34,35,31,31,36</sub> | 11.4<br><sub>8,13,9,10,6</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 8.1<br><sub>16,9,10,6,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>8,12,7,8,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 2.5 | 0.4 | 1.5 | 25.7 |
| Onyeka Okongwu (ATL) | 98% | 32.5<br><sub>31,33,30,30,35</sub> | 15.7<br><sub>14,22,16,16,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 8.1<br><sub>16,10,2,9,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>4,1,5,3,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 1.0 | 1.4 | 26.9 |
| CJ McCollum (ATL) | 98% | 28.6<br><sub>25,23,21,24,32</sub> | 17.6<br><sub>15,4,9,21,20</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>5,3,4,0,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 4.2<br><sub>5,4,3,4,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,0,1,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.6 | 2.0 | 25.1 |
| Aaron Wiggins (ATL) | 98% | 25.9<br><sub>29,29,26,23,26</sub> | 13.4<br><sub>15,19,20,15,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>4,4,4,3,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,3,6,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>3,3,5,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.4 | 1.2 | 19.4 |
| Luguentz Dort (ATL) | 98% | 24.2<br><sub>31,32,20,18,20</sub> | 8.7<br><sub>6,25,3,4,10</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,7,2,3,1</sub> |  | 1.7<br><sub>3,4,1,2,2</sub> |  | 1.4<br><sub>2,5,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.3 | 0.7 | 13.6 |
| Zuby Ejiofor (ATL) | 63% | 11.9<br><sub>17,15,18,4,-</sub> | 4.0<br><sub>11,10,7,0,-</sub> |  | 2.8<br><sub>3,5,6,0,-</sub> |  | 1.1<br><sub>2,5,0,0,-</sub> |  | 0.3<br><sub>1,0,1,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.0 |
| Corey Kispert (ATL) | 52% | 11.9<br><sub>8,16,-,-,-</sub> | 6.3<br><sub>9,7,-,-,-</sub> |  | 1.5<br><sub>0,2,-,-,-</sub> |  | 1.0<br><sub>1,1,-,-,-</sub> |  | 0.8<br><sub>1,1,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 8.8 |
| RayJ Dennis (ATL) | 52% | 10.3<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.4 |
| Dorian Finney-Smith (ATL) | 26% | 7.0<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.6 |
| Tyler Herro (MIL) | 98% | 33.1<br><sub>35,27,-,35,34</sub> | 21.2<br><sub>23,13,-,27,18</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>5,1,-,2,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>10,2,-,7,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,1,-,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 2.7 | 31.2 |
| Kyle Kuzma (MIL) | 98% | 29.1<br><sub>32,31,26,24,31</sub> | 13.3<br><sub>13,27,5,9,14</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 5.2<br><sub>4,4,5,1,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>3,0,3,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>1,6,1,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.5 | 2.1 | 21.7 |
| Jaime Jaquez Jr. (MIL) | 98% | 29.0<br><sub>28,23,25,30,28</sub> | 15.9<br><sub>14,4,16,25,22</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 5.5<br><sub>3,2,5,5,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>3,2,3,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>2,0,2,2,5</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 2.2 | 25.9 |
| Myles Turner (MIL) | 98% | 28.0<br><sub>24,24,27,-,31</sub> | 10.6<br><sub>0,3,3,-,14</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>7,5,3,-,11</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.4<br><sub>0,7,2,-,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.6<br><sub>0,0,1,-,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 1.8 | 1.8 | 19.1 |
| Ryan Rollins (MIL) | 100% | 26.4<br><sub>14,20,24,24,29</sub> | 13.5<br><sub>10,7,14,8,8</sub> | 10.5 · – | 4.5<br><sub>1,5,5,7,10</sub> |  | 5.2<br><sub>1,6,2,4,2</sub> |  | 1.8<br><sub>1,2,4,2,0</sub> | 1.5 | 1.2 | 0.4 | 2.7 | 23.2 |
| Brayden Burries (MIL) | 98% | 23.3<br><sub>38,29,26,23,19</sub> | 9.4<br><sub>21,13,3,8,3</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>11,8,3,5,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>6,4,3,1,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.9<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.3 | 1.4 | 17.2 |
| Nate Ament (MIL) | 93% | 19.9<br><sub>15,23,22,22,22</sub> | 8.1<br><sub>7,12,10,2,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>1,5,2,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>0,1,1,1,1</sub> |  | 0.9<br><sub>0,2,2,0,2</sub> |  | 0.7 | 0.3 | 1.0 | 12.2 |
| Kel'el Ware (MIL) | 96% | 17.2<br><sub>13,9,17,23,17</sub> | 8.0<br><sub>4,0,8,8,10</sub> |  | 6.2<br><sub>3,0,4,5,6</sub> |  | 1.0<br><sub>0,1,1,1,1</sub> |  | 0.6<br><sub>0,0,0,0,2</sub> |  | 0.5 | 0.9 | 1.4 | 15.1 |
| AJ Green (MIL) | 98% | 15.4<br><sub>24,18,8,8,8</sub> | 5.4<br><sub>12,5,0,3,0</sub> |  | 1.6<br><sub>1,1,0,1,0</sub> |  | 1.1<br><sub>0,1,0,1,2</sub> |  | 0.9<br><sub>4,1,0,1,0</sub> |  | 0.3 | 0.1 | 0.6 | 8.1 |
| Gary Trent Jr. (MIL) | 63% | 13.8<br><sub>-,-,6,4,16</sub> | 6.1<br><sub>-,-,5,6,1</sub> |  | 0.8<br><sub>-,-,0,1,0</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 1.0<br><sub>-,-,1,2,0</sub> |  | 0.5 | 0.1 | 0.6 | 7.7 |
| Caris LeVert (MIL) | 8% | 13.1<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.4 | 0.9 | 8.2 |
| Kasparas Jakucionis (MIL) | 72% | 12.6<br><sub>10,7,23,4,-</sub> | 4.6<br><sub>3,1,11,4,-</sub> |  | 1.6<br><sub>0,2,0,2,-</sub> |  | 2.2<br><sub>2,0,4,0,-</sub> |  | 0.4<br><sub>0,0,2,0,-</sub> |  | 0.5 | 0.1 | 1.1 | 8.4 |
| Jericho Sims (MIL) | 66% | 11.4<br><sub>7,15,8,18,-</sub> | 2.5<br><sub>0,2,2,0,-</sub> |  | 3.0<br><sub>1,2,0,4,-</sub> |  | 1.0<br><sub>0,0,0,1,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.2 | 0.8 | 6.6 |

</details>


### OKC @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.9–107.2 | OKC 82% | 1.23 / 5.40 | SAC +12.5 | 226.5 | SAC +10.5 covers 44%; o222.5 60% |
| Expected (weighted by chance each plays) | 119.8–108.0 | OKC 78% | 1.27 / 4.65 | SAC +11.5 | 227.5 | SAC +10.5 covers 46%; o222.5 62% |
| if Precious Achiuwa plays | 119.4–107.4 | OKC 80% | 1.25 / 5.05 | SAC +11.5 | 226.5 | SAC +10.5 covers 46%; o222.5 59% |
| if Keegan Murray plays | 119.4–107.3 | OKC 80% | 1.24 / 5.11 | SAC +12.5 | 226.5 | SAC +10.5 covers 46%; o222.5 59% |
| if Ajay Mitchell plays | 120.8–107.2 | OKC 83% | 1.20 / 5.90 | SAC +13.5 | 227.5 | SAC +10.5 covers 41%; o222.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa (SAC) | Questionable | 55% | 25.5 | 10.8 | 7.1 | 1.5 | 0.5 | 0.9 | 0.9 | 1.2 | 19.5 | full tables below |
| Keegan Murray (SAC) | Questionable | 55% | 31.1 | 12.1 | 5.0 | 1.7 | 1.7 | 0.8 | 1.1 | 1.2 | 18.8 | full tables below |
| Ajay Mitchell (OKC) | Questionable | 55% | 26.0 | 15.4 | 3.3 | 3.6 | 0.9 | 1.3 | 0.3 | 1.5 | 22.3 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.7<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.8 | 2.6 | 46.2 |
| Jared McCain | 98% | 29.7<br><sub>29,23,31,31,31</sub> | 16.8<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.6 | 22.5 |
| Isaiah Hartenstein | 98% | 28.4<br><sub>26,18,24,34,30</sub> | 11.5<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.3<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.9 |
| Kenrich Williams | 98% | 27.2<br><sub>19,23,19,26,35</sub> | 10.9<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.0 | 18.5 |
| Alex Caruso | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.3<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 10.1<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.3 |
| Bennett Stirtz | 98% | 19.6<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.3<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix | 67% | 17.8<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 9.8 |
| Micah Peavy | 88% | 17.0<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford | 96% | 15.0<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.9 |
| Nikola Topic | 72% | 14.2<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.2 |
| Brooks Barnhizer | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 38.4<br><sub>42,33,39,40,35</sub> | 23.9<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.3 | 3.8 | 35.6 |
| De'Andre Hunter | 98% | 36.6<br><sub>38,-,31,34,42</sub> | 16.9<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.1 | 24.4 |
| Zach LaVine | 98% | 35.0<br><sub>35,35,25,33,36</sub> | 20.1<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.6 | 26.6 |
| Domantas Sabonis | 98% | 34.3<br><sub>35,31,-,24,35</sub> | 15.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.9<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 0.6<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.3 | 3.0 | 34.7 |
| Leaky Black | 80% | 22.0<br><sub>22,40,20,18,12</sub> | 5.6<br><sub>3,12,6,0,0</sub> |  | 3.6<br><sub>6,3,5,3,0</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.9<br><sub>0,4,2,0,0</sub> |  | 1.0 | 0.5 | 0.7 | 10.6 |
| Dylan Cardwell | 98% | 19.5<br><sub>13,15,18,29,13</sub> | 5.6<br><sub>4,9,4,1,6</sub> |  | 7.0<br><sub>6,2,9,11,3</sub> |  | 1.6<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 14.2 |
| Malik Monk | 98% | 18.2<br><sub>24,18,21,3,18</sub> | 10.1<br><sub>13,12,9,1,7</sub> |  | 1.8<br><sub>2,0,2,0,4</sub> |  | 3.0<br><sub>3,7,3,0,3</sub> |  | 1.4<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.4 | 14.8 |
| Emanuel Sharp | 98% | 16.4<br><sub>10,31,12,19,7</sub> | 5.0<br><sub>3,9,5,2,4</sub> |  | 1.5<br><sub>1,5,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.7<br><sub>1,3,1,0,0</sub> |  | 0.5 | 0.2 | 0.6 | 7.3 |
| Alex Karaban | 48% | 13.1<br><sub>-,11,-,-,-</sub> | 4.3<br><sub>-,0,-,-,-</sub> |  | 1.9<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 7.0 |
| Daeqwon Plowden | 83% | 12.0<br><sub>-,-,12,2,2</sub> | 4.3<br><sub>-,-,6,0,0</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,2,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.2 |
| Mason Plumlee | 30% | 11.2<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.5 | 0.7 | 7.2 |

</details>

<details><summary>if Precious Achiuwa plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.7<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.8 | 2.6 | 46.3 |
| Jared McCain (OKC) | 98% | 29.8<br><sub>29,23,31,31,31</sub> | 16.9<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 1.6 | 22.7 |
| Isaiah Hartenstein (OKC) | 98% | 28.3<br><sub>26,18,24,34,30</sub> | 11.4<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.2<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.7 |
| Kenrich Williams (OKC) | 98% | 27.3<br><sub>19,23,19,26,35</sub> | 10.9<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.0 | 18.5 |
| Alex Caruso (OKC) | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.3<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara (OKC) | 98% | 24.6<br><sub>18,27,26,32,21</sub> | 10.1<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.3 |
| Bennett Stirtz (OKC) | 98% | 19.7<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix (OKC) | 67% | 17.8<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 9.7 |
| Micah Peavy (OKC) | 88% | 16.9<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford (OKC) | 96% | 15.1<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 9.0 |
| Nikola Topic (OKC) | 72% | 14.3<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.2 |
| Brooks Barnhizer (OKC) | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Darius Acuff Jr. (SAC) | 98% | 37.0<br><sub>42,33,39,40,35</sub> | 22.6<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.7 | 33.9 |
| De'Andre Hunter (SAC) | 98% | 34.2<br><sub>38,-,31,34,42</sub> | 14.9<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 1.9 | 21.8 |
| Zach LaVine (SAC) | 98% | 33.4<br><sub>35,35,25,33,36</sub> | 18.9<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.5 | 25.0 |
| Domantas Sabonis (SAC) | 98% | 33.0<br><sub>35,31,-,24,35</sub> | 14.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.5<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.8 | 33.1 |
| Precious Achiuwa (SAC) | 100% | 25.5<br><sub>17,22,36,14,-</sub> | 10.8<br><sub>7,9,7,10,-</sub> |  | 7.1<br><sub>3,4,14,3,-</sub> |  | 1.5<br><sub>1,0,2,0,-</sub> |  | 0.5<br><sub>1,1,0,1,-</sub> |  | 0.9 | 0.9 | 1.2 | 19.5 |
| Leaky Black (SAC) | 80% | 18.0<br><sub>22,40,20,18,12</sub> | 4.6<br><sub>3,12,6,0,0</sub> |  | 2.9<br><sub>6,3,5,3,0</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.6 |
| Dylan Cardwell (SAC) | 98% | 17.5<br><sub>13,15,18,29,13</sub> | 5.0<br><sub>4,9,4,1,6</sub> |  | 6.2<br><sub>6,2,9,11,3</sub> |  | 1.4<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.9 | 12.6 |
| Malik Monk (SAC) | 98% | 16.6<br><sub>24,18,21,3,18</sub> | 8.9<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.1<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.3 | 13.2 |
| Emanuel Sharp (SAC) | 98% | 13.7<br><sub>10,31,12,19,7</sub> | 4.1<br><sub>3,9,5,2,4</sub> |  | 1.2<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.0 |
| Alex Karaban (SAC) | 48% | 9.2<br><sub>-,11,-,-,-</sub> | 2.9<br><sub>-,0,-,-,-</sub> |  | 1.4<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Daeqwon Plowden (SAC) | 83% | 9.1<br><sub>-,-,12,2,2</sub> | 3.3<br><sub>-,-,6,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Mason Plumlee (SAC) | 30% | 7.6<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>if Keegan Murray plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.6<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 2.6 | 46.1 |
| Jared McCain (OKC) | 98% | 29.7<br><sub>29,23,31,31,31</sub> | 16.8<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.6 | 22.6 |
| Isaiah Hartenstein (OKC) | 98% | 28.4<br><sub>26,18,24,34,30</sub> | 11.5<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.3<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.9 |
| Kenrich Williams (OKC) | 98% | 27.2<br><sub>19,23,19,26,35</sub> | 10.8<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.2 | 1.0 | 18.4 |
| Alex Caruso (OKC) | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.2<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara (OKC) | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 10.1<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.3 |
| Bennett Stirtz (OKC) | 98% | 19.6<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix (OKC) | 67% | 17.7<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 9.7 |
| Micah Peavy (OKC) | 88% | 17.0<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford (OKC) | 96% | 14.9<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 9.0 |
| Nikola Topic (OKC) | 72% | 14.4<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.3 |
| Brooks Barnhizer (OKC) | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Darius Acuff Jr. (SAC) | 98% | 36.8<br><sub>42,33,39,40,35</sub> | 22.2<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.7 | 33.5 |
| De'Andre Hunter (SAC) | 98% | 34.0<br><sub>38,-,31,34,42</sub> | 15.0<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 1.9 | 21.8 |
| Zach LaVine (SAC) | 98% | 33.0<br><sub>35,35,25,33,36</sub> | 19.0<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.4 | 25.1 |
| Domantas Sabonis (SAC) | 98% | 32.7<br><sub>35,31,-,24,35</sub> | 14.9<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 12.3<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.7 | 32.8 |
| Keegan Murray (SAC) | 100% | 31.1<br><sub>-,-,23,24,40</sub> | 12.1<br><sub>-,-,10,11,16</sub> | 11.5 · – | 5.0<br><sub>-,-,1,2,7</sub> | 4.5 | 1.7<br><sub>-,-,2,1,4</sub> |  | 1.7<br><sub>-,-,0,2,2</sub> | 1.5 | 0.8 | 1.1 | 1.2 | 18.8 |
| Leaky Black (SAC) | 80% | 17.3<br><sub>22,40,20,18,12</sub> | 4.4<br><sub>3,12,6,0,0</sub> |  | 2.8<br><sub>6,3,5,3,0</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.6<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.3 |
| Dylan Cardwell (SAC) | 98% | 17.3<br><sub>13,15,18,29,13</sub> | 5.0<br><sub>4,9,4,1,6</sub> |  | 6.2<br><sub>6,2,9,11,3</sub> |  | 1.4<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 12.7 |
| Malik Monk (SAC) | 98% | 16.5<br><sub>24,18,21,3,18</sub> | 8.9<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.1<br><sub>3,2,0,0,0</sub> |  | 0.4 | 0.3 | 1.3 | 13.2 |
| Emanuel Sharp (SAC) | 98% | 13.5<br><sub>10,31,12,19,7</sub> | 4.0<br><sub>3,9,5,2,4</sub> |  | 1.2<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.8 |
| Daeqwon Plowden (SAC) | 83% | 9.0<br><sub>-,-,12,2,2</sub> | 3.2<br><sub>-,-,6,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.3<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.6 |
| Alex Karaban (SAC) | 48% | 8.4<br><sub>-,11,-,-,-</sub> | 2.7<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.4 |
| Mason Plumlee (SAC) | 30% | 7.5<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>if Ajay Mitchell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 32.2<br><sub>30,29,29,36,39</sub> | 31.4<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 5.9<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 2.4 | 41.1 |
| Jared McCain (OKC) | 98% | 26.2<br><sub>29,23,31,31,31</sub> | 14.9<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.1 | 1.4 | 20.0 |
| Ajay Mitchell (OKC) | 100% | 26.0<br><sub>30,22,28,-,-</sub> | 15.4<br><sub>35,12,14,-,-</sub> | 17.5 · – | 3.3<br><sub>1,4,3,-,-</sub> | 3.5 | 3.6<br><sub>5,0,3,-,-</sub> | 3.5 | 0.9<br><sub>4,0,0,-,-</sub> | 1.5 | 1.3 | 0.3 | 1.5 | 22.3 |
| Isaiah Hartenstein (OKC) | 98% | 25.4<br><sub>26,18,24,34,30</sub> | 10.1<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 10.0<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.5 | 23.7 |
| Kenrich Williams (OKC) | 98% | 22.5<br><sub>19,23,19,26,35</sub> | 9.0<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 0.8 | 15.2 |
| Alex Caruso (OKC) | 98% | 21.7<br><sub>20,13,19,29,27</sub> | 8.9<br><sub>5,0,5,14,5</sub> |  | 3.2<br><sub>6,3,2,7,1</sub> |  | 2.6<br><sub>2,3,1,2,4</sub> |  | 1.3<br><sub>1,0,1,4,1</sub> |  | 1.4 | 0.5 | 0.9 | 14.7 |
| Aday Mara (OKC) | 98% | 21.7<br><sub>18,27,26,32,21</sub> | 8.8<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.6 | 1.6 | 1.3 | 16.2 |
| Bennett Stirtz (OKC) | 98% | 16.3<br><sub>24,29,18,25,12</sub> | 6.6<br><sub>12,11,13,6,5</sub> |  | 1.3<br><sub>1,5,1,1,1</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.0<br><sub>2,2,2,2,1</sub> |  | 0.6 | 0.1 | 0.5 | 9.0 |
| Josh Dix (OKC) | 67% | 15.2<br><sub>15,21,-,-,17</sub> | 5.6<br><sub>5,2,-,-,0</sub> |  | 1.9<br><sub>2,1,-,-,4</sub> |  | 0.8<br><sub>1,2,-,-,3</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.3 |
| Nique Clifford (OKC) | 96% | 13.2<br><sub>-,-,20,16,12</sub> | 4.9<br><sub>-,-,4,5,0</sub> |  | 2.0<br><sub>-,-,4,3,0</sub> |  | 1.3<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.2 |
| Micah Peavy (OKC) | 88% | 13.1<br><sub>18,23,21,12,-</sub> | 3.7<br><sub>7,7,0,0,-</sub> |  | 2.3<br><sub>4,3,2,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.3<br><sub>1,1,0,0,-</sub> |  | 0.5 | 0.2 | 0.3 | 6.4 |
| Nikola Topic (OKC) | 72% | 11.5<br><sub>-,-,-,-,16</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 2.7<br><sub>-,-,-,-,3</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.1 | 1.1 | 7.7 |
| Brooks Barnhizer (OKC) | 52% | 7.0<br><sub>5,8,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 1.6<br><sub>0,4,1,-,-</sub> |  | 0.6<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Darius Acuff Jr. (SAC) | 98% | 38.4<br><sub>42,33,39,40,35</sub> | 23.8<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.3 | 3.8 | 35.5 |
| De'Andre Hunter (SAC) | 98% | 36.6<br><sub>38,-,31,34,42</sub> | 16.8<br><sub>14,-,14,15,24</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.1 | 24.3 |
| Zach LaVine (SAC) | 98% | 34.9<br><sub>35,35,25,33,36</sub> | 20.1<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 2.6 | 26.6 |
| Domantas Sabonis (SAC) | 98% | 34.4<br><sub>35,31,-,24,35</sub> | 15.8<br><sub>16,17,-,0,21</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 13.0<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.3 | 2.9 | 34.6 |
| Leaky Black (SAC) | 80% | 22.0<br><sub>22,40,20,18,12</sub> | 5.6<br><sub>3,12,6,0,0</sub> |  | 3.6<br><sub>6,3,5,3,0</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.9<br><sub>0,4,2,0,0</sub> |  | 1.0 | 0.5 | 0.7 | 10.6 |
| Dylan Cardwell (SAC) | 98% | 19.5<br><sub>13,15,18,29,13</sub> | 5.5<br><sub>4,9,4,1,6</sub> |  | 7.0<br><sub>6,2,9,11,3</sub> |  | 1.6<br><sub>0,3,3,1,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 14.1 |
| Malik Monk (SAC) | 98% | 18.3<br><sub>24,18,21,3,18</sub> | 10.2<br><sub>13,12,9,1,7</sub> |  | 1.8<br><sub>2,0,2,0,4</sub> |  | 3.0<br><sub>3,7,3,0,3</sub> |  | 1.4<br><sub>3,2,0,0,0</sub> |  | 0.5 | 0.3 | 1.4 | 15.0 |
| Emanuel Sharp (SAC) | 98% | 16.5<br><sub>10,31,12,19,7</sub> | 5.0<br><sub>3,9,5,2,4</sub> |  | 1.4<br><sub>1,5,1,2,0</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 0.7<br><sub>1,3,1,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.2 |
| Alex Karaban (SAC) | 48% | 13.1<br><sub>-,11,-,-,-</sub> | 4.4<br><sub>-,0,-,-,-</sub> |  | 1.9<br><sub>-,1,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 7.0 |
| Daeqwon Plowden (SAC) | 83% | 12.0<br><sub>-,-,12,2,2</sub> | 4.3<br><sub>-,-,6,0,0</sub> |  | 1.4<br><sub>-,-,0,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.2 |
| Mason Plumlee (SAC) | 30% | 11.1<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.5 | 0.6 | 7.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-15/`._
