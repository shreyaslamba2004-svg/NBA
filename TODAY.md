# NBA model · Wed 18 Nov 2026 (US date)

Updated **Thu 19 Nov, 02:09 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-18/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matisse Thybulle STL over 4.5 (5+) | UTA @ LAL | draftkings | 12.80 | 11.70 | 6.49 | 15.4% | 7.3% | 8.6% | +9.4% | +97.1% | 0.2% |
| Matisse Thybulle STL over 3.5 (4+) | UTA @ LAL | draftkings | 6.32 | 5.92 | 3.53 | 28.3% | 14.8% | 16.9% | +6.7% | +79.2% | 0.3% |
| Matisse Thybulle STL over 5.5 (6+) | UTA @ LAL | draftkings | 23.00 | 21.65 | 12.98 | 7.7% | 4.1% | 4.6% | +6.4% | +77.2% | 0.1% |
| Luka Doncic PA over 59.5 (60+) | UTA @ LAL | draftkings | 8.20 | 7.72 | 4.65 | 21.5% | 11.4% | 13.0% | +6.2% | +76.2% | 0.2% |
| Precious Achiuwa REB over 9.5 (10+) | PHX @ SAC | draftkings | 10.80 | 10.20 | 6.21 | 16.1% | 8.6% | 9.8% | +5.8% | +73.8% | 0.1% |
| Jaxson Hayes PR over 19.5 (20+) | UTA @ LAL | draftkings | 11.60 | 11.00 | 6.78 | 14.8% | 8.1% | 9.1% | +5.4% | +71.2% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jake LaRavia PTS over 7.5 (8+) | UTA @ LAL | draftkings | 2.79 | 2.54 | 2.85 | 35.1% | 40.1% | 39.3% | +9.7% | -2.2% | 1.4% |
| Josh Green PTS under 4.5 | UTA @ LAL | draftkings | 1.93 | 1.83 | 1.61 | 62.1% | 53.3% | 54.6% | +5.3% | +19.5% | 1.4% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quentin Grimes PTS under 15.5 | UTA @ LAL | betright | 2.00 | 1.89 | 1.40 | 71.2% | 49.5% | 52.8% | +5.7% | +42.4% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| UTA @ LAL | Thu 19 Nov 14:00 | 107.8–124.5 | UTA 12% | 8.51 / 1.13 | LAL -16.5 | 232.5 | LAL -11.5 covers 64%; o229.5 56% |
| PHX @ SAC | Thu 19 Nov 14:00 | 118.5–113.5 | PHX 64% | 1.55 / 2.81 | SAC +5.5 | 231.5 | SAC +7.5 covers 56%; o226.5 61% |

### UTA @ LAL
Out: Austin Reaves (LAL), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darryn Peterson PTS under 18.5 | UTA @ LAL | tab | 1.95 | 1.92 | 1.72 | 58.0% | 50.9% | 52.0% | +1.5% | +13.2% | 0.4% |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 33.5<br><sub>-,33,38,34,35</sub> | 20.9<br><sub>-,13,27,13,30</sub> | 21.5 · 22.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.3 | 31.1 |
| Darryn Peterson | 98% | 32.7<br><sub>31,33,34,34,31</sub> | 18.0<br><sub>25,22,28,17,13</sub> | 18.5 · 18.5<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,5,2,4,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 2.2 | 26.4 |
| Ace Bailey | 99% | 31.5<br><sub>35,31,35,30,23</sub> | 14.6<br><sub>23,18,21,7,5</sub> | 13.5 · 13.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>2,2,1,4,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.0<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.8 | 1.8 | 21.7 |
| Brice Sensabaugh | 99% | 26.5<br><sub>14,23,27,30,35</sub> | 15.7<br><sub>5,19,7,14,40</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>4,3,3,7,11</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>4,1,1,2,5</sub> |  | 2.3<br><sub>1,3,1,0,8</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.3 | 22.1 |
| Mo Bamba | 88% | 24.6<br><sub>17,18,20,36,31</sub> | 9.1<br><sub>7,5,9,26,15</sub> | 8.5 · 8.5<br><sub>o 52% · u 48%</sub> | 7.8<br><sub>7,1,9,5,10</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.5 | 1.1 | 18.1 |
| Josh Okogie | 97% | 22.4<br><sub>21,15,22,27,22</sub> | 6.1<br><sub>6,7,7,7,9</sub> | 6.5 · 5.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,3,2,6,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>4,0,1,0,4</sub> |  | 0.7<br><sub>0,1,2,2,1</sub> |  | 1.1 | 0.2 | 0.9 | 10.8 |
| Jaxson Hayes | 76% | 21.9<br><sub>17,30,13,-,-</sub> | 8.2<br><sub>6,11,12,-,-</sub> |  | 5.2<br><sub>2,8,5,-,-</sub> |  | 1.1<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.7 | 0.8 | 1.0 | 14.5 |
| Svi Mykhailiuk | 97% | 20.1<br><sub>21,20,7,21,33</sub> | 7.3<br><sub>7,3,0,6,8</sub> |  | 2.2<br><sub>2,0,1,2,7</sub> |  | 1.6<br><sub>3,2,0,3,5</sub> |  | 1.2<br><sub>1,1,0,2,2</sub> |  | 0.6 | 0.1 | 0.8 | 11.1 |
| Josh Green | 96% | 18.1<br><sub>30,26,14,15,13</sub> | 4.1<br><sub>2,3,2,6,9</sub> | 4.5 · 4.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>5,2,0,1,1</sub> |  | 0.9<br><sub>4,1,0,1,0</sub> |  | 0.5<br><sub>0,1,0,2,1</sub> |  | 0.6 | 0.1 | 0.7 | 6.7 |
| Isaiah Collier | 63% | 16.4<br><sub>24,12,16,-,-</sub> | 7.9<br><sub>17,7,3,-,-</sub> |  | 2.3<br><sub>5,3,2,-,-</sub> |  | 4.2<br><sub>5,2,5,-,-</sub> |  | 0.4<br><sub>4,1,1,-,-</sub> |  | 0.7 | 0.2 | 1.6 | 14.4 |
| Tony Bradley | 72% | 13.7<br><sub>14,-,12,12,17</sub> | 4.4<br><sub>4,-,0,6,3</sub> |  | 4.0<br><sub>5,-,5,2,7</sub> |  | 0.6<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 9.0 |
| Kyle Filipowski | 52% | 12.1<br><sub>15,-,2,-,-</sub> | 6.0<br><sub>7,-,2,-,-</sub> |  | 3.6<br><sub>4,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.8 |
| Jonas Aidoo | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.7 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 34.5<br><sub>-,39,32,36,42</sub> | 39.9<br><sub>-,32,32,43,36</sub> | 36.5 · 37.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 8.0<br><sub>-,10,5,9,7</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 5.0<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9 | 0.6 | 4.0 | 54.9 |
| Quentin Grimes | 98% | 29.4<br><sub>32,-,-,37,42</sub> | 12.9<br><sub>12,-,-,22,47</sub> | 15.5 · 15.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>1,-,-,6,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>4,-,-,1,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,-,-,5,10</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.4 | 1.5 | 19.5 |
| Walker Kessler | 98% | 28.4<br><sub>29,30,29,32,-</sub> | 12.2<br><sub>12,21,10,14,-</sub> | 13.5 · 13.5<br><sub>o 47% · u 53%</sub> | 11.8<br><sub>16,10,11,12,-</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>4,4,3,3,-</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 25.9 |
| Matisse Thybulle | 98% | 24.5<br><sub>28,23,23,26,31</sub> | 7.9<br><sub>4,6,8,12,7</sub> | 6.5 · 6.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>2,0,5,8,6</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 2.6 | 0.9 | 1.1 | 12.2 |
| Jake LaRavia | 98% | 23.1<br><sub>29,32,21,32,23</sub> | 6.6<br><sub>5,4,0,12,4</sub> | 5.5 · 6.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>1,3,9,3,5</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 1.2 | 0.7 | 1.1 | 12.6 |
| Sandro Mamukelashvili | 99% | 22.1<br><sub>18,32,26,21,23</sub> | 10.5<br><sub>7,23,23,4,3</sub> | 10.5 · 9.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>3,8,3,2,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.4<br><sub>1,5,5,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.5 | 0.8 | 17.1 |
| Ziaire Williams | 98% | 21.6<br><sub>21,28,20,19,24</sub> | 8.8<br><sub>17,12,9,6,0</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.3 | 0.8 | 12.8 |
| Collin Sexton | 98% | 21.2<br><sub>24,27,13,24,25</sub> | 13.8<br><sub>17,18,10,16,10</sub> | 13.5 · 13.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.2 | 1.7 | 19.0 |
| Jarred Vanderbilt | 88% | 13.2<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.1<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.7 |
| Carson Cooper | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 8.2 |
| Kevon Looney | 52% | 9.9<br><sub>-,-,4,-,17</sub> | 2.2<br><sub>-,-,0,-,4</sub> |  | 3.8<br><sub>-,-,2,-,8</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 6.9 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Adou Thiero | 72% | 7.9<br><sub>8,7,14,-,6</sub> | 2.6<br><sub>2,2,2,-,0</sub> |  | 2.0<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Cameron Carr | 63% | 7.0<br><sub>-,7,13,-,-</sub> | 3.8<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Jaden Hardy | 48% | 7.0<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| Chris Manon | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.2 |
| Bronny James | 48% | 5.6<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 2.8 |

</details>


### PHX @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keegan Murray PTS over 9.5 (10+) | PHX @ SAC | pointsbetau | 2.05 | 2.04 | 1.83 | 54.8% | 48.1% | 49.1% | +0.7% | +12.3% | 0.2% |
| Precious Achiuwa PTS over 7.5 (8+) | PHX @ SAC | draftkings | 1.88 | 1.87 | 1.54 | 64.8% | 51.3% | 53.4% | +0.6% | +22.2% | 0.2% |
| Miles Bridges PTS under 14.5 | PHX @ SAC | draftkings | 1.93 | 1.92 | 1.80 | 55.5% | 51.3% | 51.9% | +0.1% | +6.9% | 0.0% |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.6<br><sub>29,29,35,28,37</sub> | 26.8<br><sub>32,17,30,17,20</sub> | 26.5 · 26.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>4,5,7,7,8</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>3,2,4,0,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.3 | 2.8 | 36.4 |
| Dillon Brooks | 98% | 29.0<br><sub>26,22,30,22,27</sub> | 16.1<br><sub>7,8,15,1,15</sub> | 13.5 · 13.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.2 | 1.4 | 21.5 |
| Miles Bridges | 98% | 28.2<br><sub>26,18,25,24,29</sub> | 14.5<br><sub>7,8,11,14,16</sub> | 14.5 · 14.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>5,4,6,3,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.5 | 1.2 | 23.1 |
| Jalen Green | 98% | 26.8<br><sub>24,21,21,21,27</sub> | 15.6<br><sub>6,13,12,9,16</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.3 | 2.0 | 22.2 |
| Oso Ighodaro | 98% | 25.4<br><sub>18,20,32,17,33</sub> | 6.7<br><sub>7,6,2,4,8</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.9 | 1.4 | 16.1 |
| Collin Gillespie | 98% | 25.3<br><sub>24,22,27,28,26</sub> | 10.5<br><sub>6,12,13,26,10</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,2,2,4,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.2 | 1.0 | 17.6 |
| Jordan Goodwin | 98% | 21.5<br><sub>-,14,24,31,20</sub> | 8.9<br><sub>-,18,6,14,11</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4 | 0.2 | 0.8 | 15.6 |
| Luke Kennard | 98% | 18.5<br><sub>14,22,21,23,17</sub> | 7.8<br><sub>3,14,8,18,12</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,1,1,6,2</sub> |  | 1.9<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.1 | 0.7 | 11.7 |
| Ryan Dunn | 98% | 16.1<br><sub>23,25,10,24,12</sub> | 4.8<br><sub>3,10,0,3,5</sub> |  | 3.5<br><sub>2,8,4,6,1</sub> |  | 1.1<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.4 | 0.6 | 9.4 |
| Khaman Maluach | 98% | 14.9<br><sub>20,22,16,13,11</sub> | 5.5<br><sub>11,11,4,7,4</sub> |  | 4.8<br><sub>5,7,2,4,6</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.8 | 11.0 |
| Rasheer Fleming | 43% | 8.7<br><sub>9,12,-,-,-</sub> | 3.2<br><sub>2,4,-,-,-</sub> |  | 1.5<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 4.9 |
| Jamaree Bouyea | 48% | 7.3<br><sub>9,8,-,-,-</sub> | 3.0<br><sub>4,7,-,-,-</sub> |  | 1.0<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.1 |
| Koa Peat | 67% | 6.7<br><sub>6,6,-,8,1</sub> | 3.2<br><sub>4,5,-,10,0</sub> |  | 1.6<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 34.8<br><sub>33,39,40,35,33</sub> | 23.7<br><sub>22,32,29,17,26</sub> | 24.5 · 24.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 7.1<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,3,4,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 4.0 | 34.6 |
| Domantas Sabonis | 98% | 30.9<br><sub>31,-,24,35,29</sub> | 14.5<br><sub>17,-,0,21,11</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 11.8<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.3<br><sub>1,-,0,1,0</sub> |  | 0.8 | 0.3 | 2.6 | 31.6 |
| De'Andre Hunter | 76% | 30.7<br><sub>-,31,34,42,-</sub> | 13.7<br><sub>-,14,15,24,-</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>-,3,4,5,-</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>-,1,2,2,-</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>-,2,3,2,-</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.7 | 19.7 |
| Zach LaVine | 76% | 30.6<br><sub>35,25,33,36,-</sub> | 18.1<br><sub>14,15,31,12,-</sub> | 17.5 · 17.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,4,3,3,-</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 2.5 | 23.9 |
| Keegan Murray | 98% | 27.1<br><sub>-,23,24,40,21</sub> | 10.8<br><sub>-,10,11,16,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>-,1,2,7,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>-,2,1,4,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>-,0,2,2,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.9 | 1.0 | 16.3 |
| Precious Achiuwa | 98% | 23.5<br><sub>22,36,14,-,-</sub> | 10.1<br><sub>9,7,10,-,-</sub> | 7.5 · 7.5<br><sub>o 53% · u 47%</sub> | 6.4<br><sub>4,14,3,-,-</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>0,2,0,-,-</sub> |  | 0.3<br><sub>1,0,1,-,-</sub> |  | 0.9 | 0.8 | 1.2 | 17.7 |
| Leaky Black | 86% | 20.0<br><sub>40,20,18,12,29</sub> | 4.8<br><sub>12,6,0,0,12</sub> |  | 3.5<br><sub>3,5,3,0,9</sub> |  | 1.3<br><sub>5,1,2,0,2</sub> |  | 0.6<br><sub>4,2,0,0,4</sub> |  | 1.0 | 0.5 | 0.6 | 9.5 |
| Malik Monk | 98% | 17.9<br><sub>18,21,3,18,29</sub> | 9.8<br><sub>12,9,1,7,14</sub> |  | 1.9<br><sub>0,2,0,4,1</sub> |  | 3.5<br><sub>7,3,0,3,10</sub> |  | 1.2<br><sub>2,0,0,0,1</sub> |  | 0.5 | 0.3 | 1.5 | 15.2 |
| Dylan Cardwell | 98% | 17.0<br><sub>15,18,29,13,19</sub> | 5.5<br><sub>9,4,1,6,10</sub> | 4.5 · 4.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>2,9,11,3,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 13.2 |
| Emanuel Sharp | 98% | 15.5<br><sub>31,12,19,7,21</sub> | 4.7<br><sub>9,5,2,4,9</sub> |  | 1.5<br><sub>5,1,2,0,0</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>3,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.6 | 6.9 |
| Alex Karaban | 52% | 14.2<br><sub>11,-,-,-,29</sub> | 2.9<br><sub>0,-,-,-,0</sub> |  | 2.0<br><sub>1,-,-,-,5</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.6 |
| Daeqwon Plowden | 88% | 13.5<br><sub>-,12,2,2,24</sub> | 5.4<br><sub>-,6,0,0,13</sub> |  | 1.6<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.7<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.7 |
| Mason Plumlee | 52% | 6.5<br><sub>-,-,-,-,5</sub> | 2.0<br><sub>-,-,-,-,2</sub> |  | 2.1<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 4.8 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-18/`._
