# NBA model · Mon 16 Nov 2026 (US date)

Updated **Mon 16 Nov, 05:38 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-16/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| HOU @ MIA | player points | Alperen Sengun projected 24.5 pts vs DraftKings line 19.5 | minutes 38 vs 35 this season; scoring 0.65/min vs 0.66 this season, 0.61 last season; teammates out: Capela, Smart, VanVleet (~66 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant PRA over 49.5 (50+) | HOU @ MIA | draftkings | 18.80 | 15.90 | 6.68 | 15.0% | 5.0% | 6.3% | +18.3% | +181.6% | 0.3% |
| Kevin Durant PA over 44.5 (45+) | HOU @ MIA | draftkings | 24.00 | 20.37 | 8.64 | 11.6% | 3.9% | 4.9% | +17.8% | +177.7% | 0.2% |
| Derik Queen PRA over 34.5 (35+) | GSW @ NOP | draftkings | 19.00 | 16.37 | 7.16 | 14.0% | 4.9% | 6.1% | +16.2% | +165.5% | 0.2% |
| Amen Thompson AST over 7.5 (8+) | HOU @ MIA | draftkings | 14.00 | 12.06 | 5.28 | 18.9% | 6.7% | 8.3% | +16.1% | +165.0% | 0.3% |
| Kevin Durant PA over 39.5 (40+) | HOU @ MIA | draftkings | 12.20 | 10.62 | 4.76 | 21.0% | 7.7% | 9.4% | +15.0% | +156.3% | 0.3% |
| Kevin Durant PTS over 39.5 (40+) | HOU @ MIA | draftkings | 26.00 | 22.78 | 10.38 | 9.6% | 3.6% | 4.4% | +14.2% | +150.4% | 0.1% |
| Kevin Durant AST over 7.5 (8+) | HOU @ MIA | draftkings | 10.50 | 9.34 | 4.42 | 22.6% | 8.9% | 10.7% | +12.5% | +137.6% | 0.3% |
| Zion Williamson AST over 5.5 (6+) | GSW @ NOP | draftkings | 9.50 | 8.47 | 4.03 | 24.8% | 9.8% | 11.8% | +12.2% | +135.5% | 0.4% |
| Kevin Durant PTS over 34.5 (35+) | HOU @ MIA | draftkings | 12.80 | 11.47 | 5.55 | 18.0% | 7.3% | 8.7% | +11.6% | +130.7% | 0.2% |
| Kevin Durant AST over 9.5 (10+) | HOU @ MIA | draftkings | 28.00 | 25.32 | 12.51 | 8.0% | 3.3% | 4.0% | +10.7% | +123.9% | 0.1% |
| Derik Queen PR over 29.5 (30+) | GSW @ NOP | draftkings | 15.20 | 13.76 | 6.82 | 14.6% | 6.2% | 7.3% | +10.5% | +122.7% | 0.2% |
| Reed Sheppard AST over 5.5 (6+) | HOU @ MIA | draftkings | 12.80 | 11.63 | 5.84 | 17.1% | 7.3% | 8.6% | +10.1% | +119.2% | 0.2% |
| Derik Queen PTS over 19.5 (20+) | GSW @ NOP | draftkings | 12.00 | 10.95 | 5.56 | 18.0% | 7.8% | 9.1% | +9.6% | +115.7% | 0.2% |
| Amen Thompson PA over 34.5 (35+) | HOU @ MIA | draftkings | 19.00 | 17.33 | 8.82 | 11.3% | 4.9% | 5.8% | +9.6% | +115.4% | 0.1% |
| Alperen Sengun PTS over 34.5 (35+) | HOU @ MIA | draftkings | 15.00 | 13.72 | 7.00 | 14.3% | 6.2% | 7.3% | +9.4% | +114.4% | 0.2% |
| Alperen Sengun PTS over 39.5 (40+) | HOU @ MIA | draftkings | 30.00 | 27.47 | 14.04 | 7.1% | 3.1% | 3.6% | +9.3% | +113.7% | 0.1% |
| Amen Thompson PRA over 39.5 (40+) | HOU @ MIA | draftkings | 10.20 | 9.43 | 4.99 | 20.0% | 9.2% | 10.6% | +8.1% | +104.5% | 0.2% |
| Derik Queen PTS over 24.5 (25+) | GSW @ NOP | draftkings | 30.00 | 27.86 | 14.93 | 6.7% | 3.1% | 3.6% | +7.6% | +100.9% | 0.1% |
| Amen Thompson PRA over 44.5 (45+) | HOU @ MIA | draftkings | 20.60 | 19.16 | 10.31 | 9.7% | 4.5% | 5.2% | +7.5% | +99.8% | 0.1% |
| Amen Thompson PA over 29.5 (30+) | HOU @ MIA | draftkings | 8.20 | 7.68 | 4.23 | 23.7% | 11.4% | 13.0% | +6.7% | +94.0% | 0.2% |
| Saddiq Bey AST over 5.5 (6+) | GSW @ NOP | draftkings | 14.80 | 13.99 | 7.90 | 12.7% | 6.3% | 7.1% | +5.8% | +87.3% | 0.1% |
| Derik Queen REB over 11.5 (12+) | GSW @ NOP | draftkings | 15.80 | 14.95 | 8.50 | 11.8% | 5.9% | 6.7% | +5.7% | +85.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PRA over 24.5 (25+) | GSW @ NOP | draftkings | 3.78 | Jaron Pierre Jr. | 53.3% | 46.6% | +5.2% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Gillespie REB over 3.5 (4+) | PHX @ DEN | draftkings | 2.30 | 2.10 | 3.02 | 33.2% | 49.9% | 47.7% | +9.6% | -23.7% | 1.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ORL @ BOS | Tue 17 Nov 11:00 | 105.9–116.1 | ORL 23% | 4.27 / 1.31 | BOS -10.5 | 221.5 | BOS -8.5 covers 55%; o211.5 71% |
| CHI @ CLE | Tue 17 Nov 11:00 | 114.0–122.2 | CHI 28% | 3.63 / 1.38 | CLE -8.5 | 236.5 | CLE -9.5 covers 46%; o243.5 34% |
| MEM @ WAS | Tue 17 Nov 11:00 | 122.5–119.0 | MEM 60% | 1.66 / 2.50 | WAS +3.5 | 241.5 | WAS +3.5 covers 49%; o229.5 74% |
| PHI @ BKN | Tue 17 Nov 11:30 | 115.3–110.2 | PHI 65% | 1.54 / 2.84 | BKN +5.5 | 225.5 | BKN +5.5 covers 51%; o225.5 50% |
| HOU @ MIA | Tue 17 Nov 11:30 | 118.6–116.0 | HOU 57% | 1.74 / 2.35 | MIA +2.5 | 234.5 | MIA +2.5 covers 48%; o230.5 58% |
| POR @ MIN | Tue 17 Nov 12:00 | 111.2–115.6 | POR 38% | 2.65 / 1.61 | MIN -4.5 | 226.5 | MIN -2.5 covers 56%; o228.5 46% |
| GSW @ NOP | Tue 17 Nov 12:00 | 119.7–112.6 | GSW 69% | 1.44 / 3.26 | NOP +7.5 | 232.5 | NOP +3.5 covers 39%; o225.5 64% |
| PHX @ DEN | Tue 17 Nov 13:00 | 111.7–118.0 | PHX 33% | 3.07 / 1.48 | DEN -6.5 | 229.5 | DEN -10.5 covers 38%; o227.5 55% |

### ORL @ BOS
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL)

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 32.7<br><sub>38,40,38,39,36</sub> | 20.7<br><sub>15,30,33,38,35</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>8,6,7,8,9</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>15,11,7,1,12</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>0,3,1,3,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.7 | 32.0 |
| Desmond Bane | 98% | 31.4<br><sub>32,-,36,34,35</sub> | 16.2<br><sub>15,-,15,25,21</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>6,-,6,3,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>0,-,4,2,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>3,-,4,7,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.3 | 1.9 | 22.8 |
| Anthony Black | 98% | 30.2<br><sub>31,38,33,39,37</sub> | 13.7<br><sub>10,18,26,22,5</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>7,8,7,7,2</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>6,6,5,8,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>1,2,2,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.6 | 2.1 | 21.5 |
| Wendell Carter Jr. | 98% | 28.8<br><sub>34,40,33,28,30</sub> | 10.6<br><sub>27,19,8,9,12</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>13,11,11,7,8</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,0,1,3,0</sub> |  | 0.8<br><sub>2,3,0,0,1</sub> |  | 0.6 | 0.6 | 1.4 | 19.0 |
| Jalen Suggs | 98% | 27.0<br><sub>-,-,-,-,21</sub> | 10.2<br><sub>-,-,-,-,3</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.5 | 2.1 | 17.6 |
| Tristan da Silva | 83% | 26.2<br><sub>30,39,-,-,31</sub> | 10.8<br><sub>18,19,-,-,12</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>2,7,-,-,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>1,2,-,-,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>4,5,-,-,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.2 | 1.0 | 15.9 |
| Jevon Carter | 86% | 14.0<br><sub>3,15,4,28,17</sub> | 5.1<br><sub>0,9,0,11,5</sub> |  | 1.2<br><sub>0,1,0,3,2</sub> |  | 1.4<br><sub>0,0,0,4,2</sub> |  | 0.7<br><sub>0,3,0,3,1</sub> |  | 0.6 | 0.1 | 0.4 | 7.7 |
| Goga Bitadze | 88% | 13.3<br><sub>8,7,15,20,18</sub> | 4.7<br><sub>4,4,2,4,12</sub> |  | 4.0<br><sub>5,5,2,7,4</sub> |  | 0.9<br><sub>0,2,1,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.7 | 9.6 |
| Jamal Cain | 83% | 13.0<br><sub>25,36,20,-,4</sub> | 5.1<br><sub>5,18,5,-,0</sub> |  | 2.3<br><sub>5,12,3,-,4</sub> |  | 0.6<br><sub>0,1,1,-,1</sub> |  | 0.5<br><sub>1,2,1,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 8.0 |
| Jase Richardson | 72% | 12.8<br><sub>26,30,15,20,-</sub> | 4.9<br><sub>10,2,6,6,-</sub> |  | 1.3<br><sub>2,4,1,1,-</sub> |  | 1.3<br><sub>3,4,1,2,-</sub> |  | 0.4<br><sub>2,0,0,1,-</sub> |  | 0.4 | 0.2 | 0.5 | 7.4 |
| Nikola Vucevic | 98% | 11.8<br><sub>4,6,18,14,11</sub> | 4.6<br><sub>0,0,5,3,2</sub> |  | 3.1<br><sub>0,1,4,5,3</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 0.4<br><sub>0,0,1,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 9.0 |
| Alex Morales | 66% | 7.9<br><sub>6,15,29,18,-</sub> | 2.0<br><sub>0,0,7,5,-</sub> |  | 1.3<br><sub>0,2,7,4,-</sub> |  | 0.5<br><sub>0,1,0,3,-</sub> |  | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.2 | 0.0 | 0.4 | 3.8 |
| Colin Castleton | 48% | 5.9<br><sub>2,-,-,1,-</sub> | 2.1<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 33.7<br><sub>-,29,29,32,38</sub> | 27.0<br><sub>-,34,21,21,24</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>-,8,4,6,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.6<br><sub>-,9,6,4,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>-,5,5,3,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.6 | 2.9 | 41.6 |
| Paul George | 98% | 30.6<br><sub>35,22,28,30,-</sub> | 19.8<br><sub>25,8,27,36,-</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,5,3,5,-</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.1<br><sub>5,1,1,1,-</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>5,2,5,6,-</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.7 | 0.5 | 2.5 | 27.8 |
| Derrick White | 98% | 30.4<br><sub>36,25,27,22,38</sub> | 13.6<br><sub>24,18,9,5,19</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>4,4,3,1,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.5<br><sub>7,5,7,3,7</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>1,4,1,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 1.1 | 1.7 | 21.6 |
| Payton Pritchard | 98% | 27.4<br><sub>18,23,29,30,31</sub> | 14.0<br><sub>10,12,12,18,14</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>1,6,5,6,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.8<br><sub>5,5,4,5,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>0,4,4,4,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.1 | 1.3 | 21.1 |
| Neemias Queta | 98% | 23.4<br><sub>29,15,22,22,31</sub> | 9.3<br><sub>9,4,13,4,11</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>12,3,9,6,13</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>3,1,4,3,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.6 | 1.3 | 1.3 | 18.9 |
| Sam Hauser | 98% | 20.7<br><sub>30,17,23,18,24</sub> | 7.7<br><sub>11,9,7,12,8</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,3,3,5,9</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1<br><sub>0,3,1,2,0</sub> |  | 1.4<br><sub>3,3,1,4,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.4 | 0.2 | 0.4 | 12.2 |
| Baylor Scheierman | 98% | 19.9<br><sub>29,15,19,18,29</sub> | 5.9<br><sub>9,5,7,5,9</sub> |  | 3.8<br><sub>11,4,1,3,7</sub> |  | 1.4<br><sub>1,2,0,2,3</sub> |  | 0.9<br><sub>3,1,1,1,3</sub> |  | 0.7 | 0.1 | 0.7 | 11.1 |
| Mitchell Robinson | 98% | 13.8<br><sub>20,15,18,17,11</sub> | 4.1<br><sub>3,6,12,2,2</sub> |  | 5.2<br><sub>10,7,7,6,2</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 0.6 | 9.8 |
| Jordan Walsh | 98% | 13.4<br><sub>12,22,11,19,18</sub> | 3.6<br><sub>3,6,0,8,6</sub> |  | 2.8<br><sub>4,3,3,2,3</sub> |  | 0.6<br><sub>0,0,0,2,0</sub> |  | 0.4<br><sub>1,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.4 | 7.1 |
| Luka Garza | 98% | 11.9<br><sub>18,19,9,9,11</sub> | 5.8<br><sub>11,6,4,2,5</sub> |  | 3.0<br><sub>5,7,5,0,1</sub> |  | 1.0<br><sub>2,4,0,2,0</sub> |  | 0.6<br><sub>3,2,0,0,1</sub> |  | 0.3 | 0.3 | 0.6 | 9.7 |
| Hugo Gonzalez | 98% | 10.0<br><sub>14,15,10,19,8</sub> | 2.9<br><sub>4,8,0,10,0</sub> |  | 2.0<br><sub>2,1,2,2,1</sub> |  | 0.5<br><sub>0,0,1,2,0</sub> |  | 0.2<br><sub>0,1,0,2,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.4 |
| Devin Carter | 8% | 8.6 | 3.8 |  | 1.6 |  | 1.2 |  | 0.3 |  | 0.4 | 0.1 | 0.7 | 6.6 |
| Mike Conley | 48% | 7.4<br><sub>-,11,10,-,-</sub> | 2.0<br><sub>-,0,3,-,-</sub> |  | 0.8<br><sub>-,0,3,-,-</sub> |  | 1.0<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |
| Dillon Mitchell | 38% | 6.6<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 1.0 |
| Ron Harper Jr. | 58% | 6.2<br><sub>-,10,4,4,-</sub> | 2.7<br><sub>-,3,2,0,-</sub> |  | 0.9<br><sub>-,0,0,1,-</sub> |  | 0.5<br><sub>-,2,0,0,-</sub> |  | 0.3<br><sub>-,1,0,0,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.1 |
| Chris Cenac Jr. | 38% | 5.9<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.8 | 4.9 |
| Amari Williams | 30% | 4.8<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.3 |

</details>


### CHI @ CLE
Out: Sam Merrill (CLE), Evan Mobley (CLE), Nae'Qwan Tomlin (CLE), Tobe Awaka (CHI), Orlando Robinson (CHI), Caleb Wilson (CHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.0–122.2 | CHI 28% | 3.63 / 1.38 | CLE -8.5 | 236.5 | CLE -9.5 covers 46%; o243.5 34% |
| Expected (weighted by chance each plays) | 113.7–122.8 | CHI 26% | 3.92 / 1.34 | CLE -9.5 | 236.5 | CLE -9.5 covers 49%; o243.5 35% |
| if Peyton Watson plays | 113.3–124.0 | CHI 22% | 4.55 / 1.28 | CLE -10.5 | 237.5 | CLE -9.5 covers 53%; o243.5 36% |
| if Jaylon Tyson plays | 114.2–123.1 | CHI 26% | 3.88 / 1.35 | CLE -8.5 | 237.5 | CLE -9.5 covers 48%; o243.5 36% |
| if Jalen Smith plays | 114.2–121.3 | CHI 30% | 3.29 / 1.44 | CLE -7.5 | 235.5 | CLE -9.5 covers 43%; o243.5 33% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Peyton Watson (CLE) | Questionable | 55% | 29.4 | 13.3 | 5.0 | 2.7 | 1.3 | 1.0 | 1.5 | 1.6 | 21.0 | full tables below |
| Jaylon Tyson (CLE) | Questionable | 55% | 28.8 | 12.7 | 5.0 | 2.9 | 1.9 | 0.9 | 0.4 | 1.4 | 20.5 | full tables below |
| Jalen Smith (CHI) | Questionable | 55% | 26.5 | 12.9 | 8.1 | 1.6 | 1.6 | 0.6 | 0.8 | 1.0 | 22.7 | full tables below |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 31.1<br><sub>27,34,25,39,26</sub> | 14.6<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 8.4<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 2.8 | 30.0 |
| Norman Powell | 98% | 30.9<br><sub>22,-,-,31,30</sub> | 21.3<br><sub>12,-,-,33,24</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,-,-,5,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.4<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 26.9 |
| Matas Buzelis | 98% | 30.3<br><sub>26,31,31,29,30</sub> | 16.9<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 1.1 | 2.3 | 24.6 |
| Isaac Okoro | 98% | 29.1<br><sub>15,25,23,41,31</sub> | 9.4<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.4 | 0.9 | 14.2 |
| Patrick Williams | 76% | 26.0<br><sub>20,25,28,24,26</sub> | 9.1<br><sub>4,7,9,13,14</sub> |  | 3.7<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.7 |
| Tre Jones | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.3<br><sub>14,6,13,4,16</sub> |  | 2.8<br><sub>3,1,1,1,0</sub> |  | 3.8<br><sub>4,1,3,3,4</sub> |  | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.3 | 18.8 |
| Nic Claxton | 98% | 20.2<br><sub>-,18,16,22,-</sub> | 7.8<br><sub>-,4,17,2,-</sub> |  | 5.8<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.9 | 15.7 |
| Zach Collins | 71% | 18.4<br><sub>14,-,3,-,28</sub> | 7.3<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.4 |
| Leonard Miller | 67% | 17.5<br><sub>19,-,2,-,17</sub> | 7.9<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.0<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.2 |
| Buddy Hield | 71% | 17.4<br><sub>8,-,-,25,20</sub> | 8.3<br><sub>7,-,-,12,16</sub> |  | 2.4<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.3<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 0.9 | 12.4 |
| Noa Essengue | 96% | 13.8<br><sub>14,15,11,8,7</sub> | 5.6<br><sub>6,10,8,5,0</sub> |  | 3.1<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 9.3 |
| Jordan Hawkins | 58% | 12.7<br><sub>7,17,24,-,-</sub> | 5.4<br><sub>2,9,7,-,-</sub> |  | 1.7<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.8 |
| Dailyn Swain | 52% | 8.5<br><sub>7,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 5.2 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.2<br><sub>34,25,33,35,-</sub> | 21.7<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.6 | 3.4 | 33.8 |
| Donovan Mitchell | 98% | 35.1<br><sub>37,23,36,33,-</sub> | 29.7<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 3.0 | 40.9 |
| Meleek Thomas | 93% | 31.5<br><sub>24,27,22,18,34</sub> | 17.4<br><sub>9,18,14,12,20</sub> |  | 3.9<br><sub>4,3,4,0,4</sub> |  | 2.4<br><sub>0,3,1,3,2</sub> |  | 2.9<br><sub>3,4,2,2,3</sub> |  | 1.3 | 0.5 | 1.5 | 23.7 |
| Tyrese Proctor | 96% | 31.1<br><sub>23,23,23,27,34</sub> | 15.5<br><sub>7,6,15,22,24</sub> |  | 5.3<br><sub>3,1,3,4,11</sub> |  | 4.9<br><sub>3,4,1,3,10</sub> |  | 2.5<br><sub>2,0,3,5,4</sub> |  | 1.4 | 0.1 | 1.5 | 25.8 |
| Jarrett Allen | 76% | 29.5<br><sub>-,19,32,32,-</sub> | 15.5<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 10.1<br><sub>-,7,14,8,-</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>-,1,3,1,-</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.1 | 1.5 | 1.4 | 27.2 |
| Mario Hezonja | 98% | 25.1<br><sub>19,17,7,9,34</sub> | 11.1<br><sub>0,10,0,4,22</sub> |  | 6.5<br><sub>5,3,0,4,7</sub> |  | 2.0<br><sub>1,0,0,0,4</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 0.9 | 0.4 | 1.1 | 19.6 |
| Thomas Bryant | 72% | 23.7<br><sub>15,15,-,16,27</sub> | 12.7<br><sub>5,11,-,9,19</sub> |  | 6.2<br><sub>3,2,-,1,11</sub> |  | 1.1<br><sub>1,0,-,1,3</sub> |  | 1.5<br><sub>1,2,-,0,2</sub> |  | 0.7 | 0.8 | 1.1 | 20.1 |
| Craig Porter Jr. | 80% | 23.5<br><sub>15,17,-,9,28</sub> | 5.5<br><sub>0,9,-,0,9</sub> |  | 4.7<br><sub>1,2,-,2,9</sub> |  | 4.1<br><sub>1,4,-,2,6</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.8 | 1.1 | 14.4 |
| Norchad Omier | 52% | 23.2<br><sub>-,12,-,-,27</sub> | 6.9<br><sub>-,0,-,-,13</sub> |  | 5.7<br><sub>-,3,-,-,8</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.9 | 0.2 | 0.7 | 15.0 |
| Riley Minix | 52% | 18.0<br><sub>10,17,-,-,22</sub> | 6.1<br><sub>8,2,-,-,2</sub> |  | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.0<br><sub>0,0,-,-,0</sub> |  | 0.8<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 9.7 |
| Ernest Udeh Jr. | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell (CHI) | 98% | 29.4<br><sub>22,-,-,31,30</sub> | 19.6<br><sub>12,-,-,33,24</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>1,-,-,5,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.3<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 24.9 |
| Josh Giddey (CHI) | 98% | 29.0<br><sub>27,34,25,39,26</sub> | 13.0<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 7.9<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.6 | 27.4 |
| Matas Buzelis (CHI) | 98% | 27.8<br><sub>26,31,31,29,30</sub> | 15.3<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>3,2,2,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.7 | 0.9 | 2.1 | 22.4 |
| Jalen Smith (CHI) | 100% | 26.5<br><sub>7,30,30,32,-</sub> | 12.9<br><sub>3,17,23,15,-</sub> | 13.5 · – | 8.1<br><sub>2,8,4,12,-</sub> | 7.5 | 1.6<br><sub>0,2,3,3,-</sub> | 1.5 | 1.6<br><sub>1,2,5,1,-</sub> | 1.5 | 0.6 | 0.8 | 1.0 | 22.7 |
| Isaac Okoro (CHI) | 98% | 25.2<br><sub>15,25,23,41,31</sub> | 8.2<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.7 | 0.3 | 0.8 | 12.4 |
| Patrick Williams (CHI) | 76% | 23.5<br><sub>20,25,28,24,26</sub> | 8.1<br><sub>4,7,9,13,14</sub> |  | 3.3<br><sub>0,3,7,4,5</sub> |  | 1.7<br><sub>2,3,4,2,1</sub> |  | 1.1<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.4 | 1.0 | 13.1 |
| Tre Jones (CHI) | 98% | 20.7<br><sub>18,14,28,15,24</sub> | 11.4<br><sub>14,6,13,4,16</sub> |  | 2.6<br><sub>3,1,1,1,0</sub> |  | 3.6<br><sub>4,1,3,3,4</sub> |  | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.2 | 17.5 |
| Nic Claxton (CHI) | 98% | 18.1<br><sub>-,18,16,22,-</sub> | 7.0<br><sub>-,4,17,2,-</sub> |  | 5.1<br><sub>-,4,6,6,-</sub> |  | 2.0<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.5 | 0.7 | 0.8 | 14.1 |
| Buddy Hield (CHI) | 71% | 15.6<br><sub>8,-,-,25,20</sub> | 7.4<br><sub>7,-,-,12,16</sub> |  | 2.2<br><sub>1,-,-,3,4</sub> |  | 1.4<br><sub>1,-,-,3,2</sub> |  | 1.1<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 0.9 | 10.9 |
| Zach Collins (CHI) | 71% | 15.0<br><sub>14,-,3,-,28</sub> | 6.1<br><sub>3,-,2,-,8</sub> |  | 4.3<br><sub>1,-,2,-,5</sub> |  | 1.6<br><sub>3,-,1,-,4</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.8 | 12.0 |
| Leonard Miller (CHI) | 67% | 14.7<br><sub>19,-,2,-,17</sub> | 6.7<br><sub>4,-,0,-,4</sub> |  | 3.5<br><sub>6,-,0,-,3</sub> |  | 0.9<br><sub>3,-,0,-,4</sub> |  | 0.6<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.7 | 11.1 |
| Noa Essengue (CHI) | 96% | 10.2<br><sub>14,15,11,8,7</sub> | 4.2<br><sub>6,10,8,5,0</sub> |  | 2.3<br><sub>3,7,4,1,1</sub> |  | 0.5<br><sub>0,1,3,1,0</sub> |  | 0.3<br><sub>0,0,1,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Jordan Hawkins (CHI) | 58% | 8.7<br><sub>7,17,24,-,-</sub> | 3.7<br><sub>2,9,7,-,-</sub> |  | 1.1<br><sub>1,0,4,-,-</sub> |  | 0.5<br><sub>0,1,2,-,-</sub> |  | 0.3<br><sub>0,1,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.3 |
| Dailyn Swain (CHI) | 52% | 6.4<br><sub>7,-,-,-,-</sub> | 2.1<br><sub>3,-,-,-,-</sub> |  | 0.9<br><sub>1,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 4.0 |
| James Harden (CLE) | 98% | 35.2<br><sub>34,25,33,35,-</sub> | 21.7<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.6 | 3.4 | 33.8 |
| Donovan Mitchell (CLE) | 98% | 35.1<br><sub>37,23,36,33,-</sub> | 29.7<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 3.0 | 40.9 |
| Meleek Thomas (CLE) | 93% | 31.4<br><sub>24,27,22,18,34</sub> | 17.3<br><sub>9,18,14,12,20</sub> |  | 3.9<br><sub>4,3,4,0,4</sub> |  | 2.4<br><sub>0,3,1,3,2</sub> |  | 2.9<br><sub>3,4,2,2,3</sub> |  | 1.3 | 0.5 | 1.5 | 23.6 |
| Tyrese Proctor (CLE) | 96% | 31.1<br><sub>23,23,23,27,34</sub> | 15.5<br><sub>7,6,15,22,24</sub> |  | 5.3<br><sub>3,1,3,4,11</sub> |  | 4.9<br><sub>3,4,1,3,10</sub> |  | 2.5<br><sub>2,0,3,5,4</sub> |  | 1.4 | 0.1 | 1.5 | 25.7 |
| Jarrett Allen (CLE) | 76% | 29.6<br><sub>-,19,32,32,-</sub> | 15.4<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 10.1<br><sub>-,7,14,8,-</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>-,1,3,1,-</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.5 | 1.4 | 27.2 |
| Mario Hezonja (CLE) | 98% | 25.2<br><sub>19,17,7,9,34</sub> | 11.1<br><sub>0,10,0,4,22</sub> |  | 6.5<br><sub>5,3,0,4,7</sub> |  | 2.0<br><sub>1,0,0,0,4</sub> |  | 1.3<br><sub>0,0,0,0,2</sub> |  | 0.9 | 0.4 | 1.1 | 19.7 |
| Craig Porter Jr. (CLE) | 80% | 23.6<br><sub>15,17,-,9,28</sub> | 5.5<br><sub>0,9,-,0,9</sub> |  | 4.8<br><sub>1,2,-,2,9</sub> |  | 4.1<br><sub>1,4,-,2,6</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 1.1 | 0.8 | 1.1 | 14.4 |
| Thomas Bryant (CLE) | 72% | 23.5<br><sub>15,15,-,16,27</sub> | 12.5<br><sub>5,11,-,9,19</sub> |  | 6.2<br><sub>3,2,-,1,11</sub> |  | 1.1<br><sub>1,0,-,1,3</sub> |  | 1.5<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.8 | 1.1 | 19.9 |
| Norchad Omier (CLE) | 52% | 23.1<br><sub>-,12,-,-,27</sub> | 6.8<br><sub>-,0,-,-,13</sub> |  | 5.6<br><sub>-,3,-,-,8</sub> |  | 2.4<br><sub>-,2,-,-,2</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.9 | 0.2 | 0.7 | 14.9 |
| Riley Minix (CLE) | 52% | 18.0<br><sub>10,17,-,-,22</sub> | 6.1<br><sub>8,2,-,-,2</sub> |  | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.0<br><sub>0,0,-,-,0</sub> |  | 0.8<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 9.7 |
| Ernest Udeh Jr. (CLE) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>if Peyton Watson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 31.1<br><sub>27,34,25,39,26</sub> | 14.6<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 8.5<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.8 | 30.1 |
| Norman Powell (CHI) | 98% | 30.9<br><sub>22,-,-,31,30</sub> | 21.2<br><sub>12,-,-,33,24</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,-,-,5,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.4<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 26.7 |
| Matas Buzelis (CHI) | 98% | 30.3<br><sub>26,31,31,29,30</sub> | 16.9<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 1.1 | 2.3 | 24.6 |
| Isaac Okoro (CHI) | 98% | 29.1<br><sub>15,25,23,41,31</sub> | 9.4<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.4 | 1.0 | 14.2 |
| Patrick Williams (CHI) | 76% | 25.9<br><sub>20,25,28,24,26</sub> | 9.1<br><sub>4,7,9,13,14</sub> |  | 3.6<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.7 |
| Tre Jones (CHI) | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.2<br><sub>14,6,13,4,16</sub> |  | 2.8<br><sub>3,1,1,1,0</sub> |  | 3.8<br><sub>4,1,3,3,4</sub> |  | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.2 | 18.8 |
| Nic Claxton (CHI) | 98% | 20.2<br><sub>-,18,16,22,-</sub> | 7.7<br><sub>-,4,17,2,-</sub> |  | 5.7<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.9 | 15.7 |
| Zach Collins (CHI) | 71% | 18.3<br><sub>14,-,3,-,28</sub> | 7.2<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.3 |
| Leonard Miller (CHI) | 67% | 17.5<br><sub>19,-,2,-,17</sub> | 7.9<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.0<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.1 |
| Buddy Hield (CHI) | 71% | 17.3<br><sub>8,-,-,25,20</sub> | 8.3<br><sub>7,-,-,12,16</sub> |  | 2.4<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.3<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 0.9 | 12.3 |
| Noa Essengue (CHI) | 96% | 13.8<br><sub>14,15,11,8,7</sub> | 5.6<br><sub>6,10,8,5,0</sub> |  | 3.1<br><sub>3,7,4,1,1</sub> |  | 0.7<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 9.3 |
| Jordan Hawkins (CHI) | 58% | 12.8<br><sub>7,17,24,-,-</sub> | 5.4<br><sub>2,9,7,-,-</sub> |  | 1.7<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.8 |
| Dailyn Swain (CHI) | 52% | 8.3<br><sub>7,-,-,-,-</sub> | 2.7<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 5.1 |
| James Harden (CLE) | 98% | 34.4<br><sub>34,25,33,35,-</sub> | 19.7<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.6 | 3.0 | 31.4 |
| Donovan Mitchell (CLE) | 98% | 34.3<br><sub>37,23,36,33,-</sub> | 27.6<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 2.8 | 38.4 |
| Peyton Watson (CLE) | 100% | 29.4<br><sub>29,21,30,30,-</sub> | 13.3<br><sub>12,13,7,4,-</sub> | 13.5 · – | 5.0<br><sub>6,2,5,4,-</sub> | 4.5 | 2.7<br><sub>3,1,4,2,-</sub> | 2.5 | 1.3<br><sub>1,2,2,0,-</sub> | 1.5 | 1.0 | 1.5 | 1.6 | 21.0 |
| Meleek Thomas (CLE) | 93% | 28.6<br><sub>24,27,22,18,34</sub> | 14.9<br><sub>9,18,14,12,20</sub> |  | 3.4<br><sub>4,3,4,0,4</sub> |  | 2.0<br><sub>0,3,1,3,2</sub> |  | 2.6<br><sub>3,4,2,2,3</sub> |  | 1.2 | 0.4 | 1.4 | 20.4 |
| Tyrese Proctor (CLE) | 96% | 28.1<br><sub>23,23,23,27,34</sub> | 13.2<br><sub>7,6,15,22,24</sub> |  | 4.7<br><sub>3,1,3,4,11</sub> |  | 4.4<br><sub>3,4,1,3,10</sub> |  | 2.2<br><sub>2,0,3,5,4</sub> |  | 1.2 | 0.1 | 1.2 | 22.3 |
| Jarrett Allen (CLE) | 76% | 27.6<br><sub>-,19,32,32,-</sub> | 14.2<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 9.3<br><sub>-,7,14,8,-</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,1,3,1,-</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.5 | 1.2 | 25.0 |
| Mario Hezonja (CLE) | 98% | 22.2<br><sub>19,17,7,9,34</sub> | 9.6<br><sub>0,10,0,4,22</sub> |  | 5.6<br><sub>5,3,0,4,7</sub> |  | 1.7<br><sub>1,0,0,0,4</sub> |  | 1.1<br><sub>0,0,0,0,2</sub> |  | 0.8 | 0.4 | 1.0 | 17.0 |
| Thomas Bryant (CLE) | 72% | 20.7<br><sub>15,15,-,16,27</sub> | 11.4<br><sub>5,11,-,9,19</sub> |  | 5.5<br><sub>3,2,-,1,11</sub> |  | 1.0<br><sub>1,0,-,1,3</sub> |  | 1.3<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.7 | 1.0 | 17.9 |
| Norchad Omier (CLE) | 52% | 20.7<br><sub>-,12,-,-,27</sub> | 6.0<br><sub>-,0,-,-,13</sub> |  | 5.0<br><sub>-,3,-,-,8</sub> |  | 2.1<br><sub>-,2,-,-,2</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.8 | 0.2 | 0.7 | 13.1 |
| Craig Porter Jr. (CLE) | 80% | 19.3<br><sub>15,17,-,9,28</sub> | 4.5<br><sub>0,9,-,0,9</sub> |  | 3.9<br><sub>1,2,-,2,9</sub> |  | 3.4<br><sub>1,4,-,2,6</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.9 | 0.6 | 1.0 | 11.8 |
| Riley Minix (CLE) | 52% | 16.1<br><sub>10,17,-,-,22</sub> | 5.3<br><sub>8,2,-,-,2</sub> |  | 2.3<br><sub>3,2,-,-,0</sub> |  | 0.8<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.5 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |

</details>

<details><summary>if Jaylon Tyson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey (CHI) | 98% | 31.1<br><sub>27,34,25,39,26</sub> | 14.8<br><sub>10,19,9,15,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>1,7,2,10,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 8.4<br><sub>6,15,7,14,5</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,1,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.5 | 2.7 | 30.1 |
| Norman Powell (CHI) | 98% | 30.9<br><sub>22,-,-,31,30</sub> | 21.2<br><sub>12,-,-,33,24</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,-,-,5,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.5<br><sub>0,-,-,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.2 | 2.1 | 26.8 |
| Matas Buzelis (CHI) | 98% | 30.4<br><sub>26,31,31,29,30</sub> | 16.9<br><sub>12,19,13,11,18</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>5,5,3,6,9</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,2,2,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,3,3,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 1.0 | 2.3 | 24.7 |
| Isaac Okoro (CHI) | 98% | 29.0<br><sub>15,25,23,41,31</sub> | 9.4<br><sub>6,12,0,15,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>1,2,2,3,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>0,1,4,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.4 | 1.0 | 14.2 |
| Patrick Williams (CHI) | 76% | 26.0<br><sub>20,25,28,24,26</sub> | 9.1<br><sub>4,7,9,13,14</sub> |  | 3.6<br><sub>0,3,7,4,5</sub> |  | 1.9<br><sub>2,3,4,2,1</sub> |  | 1.3<br><sub>0,1,0,4,2</sub> |  | 0.8 | 0.5 | 1.1 | 14.7 |
| Tre Jones (CHI) | 98% | 22.3<br><sub>18,14,28,15,24</sub> | 12.3<br><sub>14,6,13,4,16</sub> |  | 2.8<br><sub>3,1,1,1,0</sub> |  | 3.8<br><sub>4,1,3,3,4</sub> |  | 0.6<br><sub>1,0,1,0,1</sub> |  | 0.9 | 0.2 | 1.3 | 18.9 |
| Nic Claxton (CHI) | 98% | 20.2<br><sub>-,18,16,22,-</sub> | 7.8<br><sub>-,4,17,2,-</sub> |  | 5.8<br><sub>-,4,6,6,-</sub> |  | 2.2<br><sub>-,4,1,2,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.6 | 0.8 | 0.9 | 15.8 |
| Zach Collins (CHI) | 71% | 18.3<br><sub>14,-,3,-,28</sub> | 7.2<br><sub>3,-,2,-,8</sub> |  | 5.3<br><sub>1,-,2,-,5</sub> |  | 1.8<br><sub>3,-,1,-,4</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 14.3 |
| Buddy Hield (CHI) | 71% | 17.4<br><sub>8,-,-,25,20</sub> | 8.4<br><sub>7,-,-,12,16</sub> |  | 2.5<br><sub>1,-,-,3,4</sub> |  | 1.6<br><sub>1,-,-,3,2</sub> |  | 1.3<br><sub>1,-,-,2,4</sub> |  | 0.7 | 0.2 | 0.9 | 12.4 |
| Leonard Miller (CHI) | 67% | 17.4<br><sub>19,-,2,-,17</sub> | 7.8<br><sub>4,-,0,-,4</sub> |  | 4.2<br><sub>6,-,0,-,3</sub> |  | 1.0<br><sub>3,-,0,-,4</sub> |  | 0.7<br><sub>0,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.8 | 13.1 |
| Noa Essengue (CHI) | 96% | 13.7<br><sub>14,15,11,8,7</sub> | 5.6<br><sub>6,10,8,5,0</sub> |  | 3.1<br><sub>3,7,4,1,1</sub> |  | 0.6<br><sub>0,1,3,1,0</sub> |  | 0.5<br><sub>0,0,1,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 9.3 |
| Jordan Hawkins (CHI) | 58% | 12.8<br><sub>7,17,24,-,-</sub> | 5.4<br><sub>2,9,7,-,-</sub> |  | 1.7<br><sub>1,0,4,-,-</sub> |  | 0.7<br><sub>0,1,2,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.8 |
| Dailyn Swain (CHI) | 52% | 8.5<br><sub>7,-,-,-,-</sub> | 2.8<br><sub>3,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.0 | 5.2 |
| Donovan Mitchell (CLE) | 98% | 34.7<br><sub>37,23,36,33,-</sub> | 28.3<br><sub>37,11,23,25,-</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>4,2,7,4,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,4,6,7,-</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>5,1,2,5,-</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6 | 0.4 | 2.9 | 39.3 |
| James Harden (CLE) | 98% | 34.6<br><sub>34,25,33,35,-</sub> | 20.3<br><sub>7,11,32,20,-</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>2,3,2,6,-</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>5,5,4,8,-</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>1,2,5,2,-</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.6 | 3.2 | 32.2 |
| Jaylon Tyson (CLE) | 100% | 28.8<br><sub>-,-,23,30,34</sub> | 12.7<br><sub>-,-,3,16,18</sub> | 14.5 · – | 5.0<br><sub>-,-,0,3,4</sub> | 4.5 | 2.9<br><sub>-,-,1,1,4</sub> | 2.5 | 1.9<br><sub>-,-,1,4,3</sub> | 2.5 | 0.9 | 0.4 | 1.4 | 20.5 |
| Meleek Thomas (CLE) | 93% | 28.7<br><sub>24,27,22,18,34</sub> | 14.8<br><sub>9,18,14,12,20</sub> |  | 3.5<br><sub>4,3,4,0,4</sub> |  | 2.0<br><sub>0,3,1,3,2</sub> |  | 2.5<br><sub>3,4,2,2,3</sub> |  | 1.2 | 0.4 | 1.4 | 20.4 |
| Tyrese Proctor (CLE) | 96% | 28.0<br><sub>23,23,23,27,34</sub> | 13.4<br><sub>7,6,15,22,24</sub> |  | 4.8<br><sub>3,1,3,4,11</sub> |  | 4.3<br><sub>3,4,1,3,10</sub> |  | 2.2<br><sub>2,0,3,5,4</sub> |  | 1.2 | 0.1 | 1.3 | 22.5 |
| Jarrett Allen (CLE) | 76% | 27.8<br><sub>-,19,32,32,-</sub> | 14.0<br><sub>-,12,11,9,-</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 9.5<br><sub>-,7,14,8,-</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,1,3,1,-</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.1<br><sub>-,1,0,0,-</sub> |  | 1.0 | 1.5 | 1.2 | 25.0 |
| Mario Hezonja (CLE) | 98% | 22.5<br><sub>19,17,7,9,34</sub> | 9.8<br><sub>0,10,0,4,22</sub> |  | 5.8<br><sub>5,3,0,4,7</sub> |  | 1.7<br><sub>1,0,0,0,4</sub> |  | 1.1<br><sub>0,0,0,0,2</sub> |  | 0.8 | 0.4 | 1.1 | 17.3 |
| Thomas Bryant (CLE) | 72% | 21.3<br><sub>15,15,-,16,27</sub> | 11.4<br><sub>5,11,-,9,19</sub> |  | 5.7<br><sub>3,2,-,1,11</sub> |  | 1.0<br><sub>1,0,-,1,3</sub> |  | 1.4<br><sub>1,2,-,0,2</sub> |  | 0.6 | 0.8 | 1.0 | 18.1 |
| Norchad Omier (CLE) | 52% | 20.6<br><sub>-,12,-,-,27</sub> | 5.9<br><sub>-,0,-,-,13</sub> |  | 5.0<br><sub>-,3,-,-,8</sub> |  | 2.1<br><sub>-,2,-,-,2</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.8 | 0.2 | 0.7 | 13.1 |
| Craig Porter Jr. (CLE) | 80% | 20.0<br><sub>15,17,-,9,28</sub> | 4.7<br><sub>0,9,-,0,9</sub> |  | 4.0<br><sub>1,2,-,2,9</sub> |  | 3.6<br><sub>1,4,-,2,6</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 1.0 | 0.6 | 1.0 | 12.4 |
| Riley Minix (CLE) | 52% | 16.7<br><sub>10,17,-,-,22</sub> | 5.5<br><sub>8,2,-,-,2</sub> |  | 2.4<br><sub>3,2,-,-,0</sub> |  | 0.9<br><sub>0,0,-,-,0</sub> |  | 0.7<br><sub>2,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.8 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>


### MEM @ WAS
Out: Justin Champagnie (WAS), Tre Johnson (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), GG Jackson (MEM), Ty Jerome (MEM), Scotty Pippen Jr. (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 122.5–119.0 | MEM 60% | 1.66 / 2.50 | WAS +3.5 | 241.5 | WAS +3.5 covers 49%; o229.5 74% |
| Expected (weighted by chance each plays) | 122.8–118.8 | MEM 62% | 1.62 / 2.61 | WAS +4.5 | 241.5 | WAS +3.5 covers 47%; o229.5 74% |
| if Zach Edey plays | 122.3–118.6 | MEM 60% | 1.66 / 2.53 | WAS +3.5 | 240.5 | WAS +3.5 covers 49%; o229.5 73% |
| if Isaiah Stewart plays | 122.8–118.8 | MEM 61% | 1.63 / 2.58 | WAS +4.5 | 241.5 | WAS +3.5 covers 48%; o229.5 74% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey (MEM) | Questionable | 55% | 24.0 | 11.0 | 10.0 | 1.3 | 0.1 | 0.6 | 1.5 | 1.7 | 22.3 | full tables below |
| Quinten Post (MEM) | Questionable | 55% | 15.1 | 5.4 | 3.1 | 0.8 | 0.7 | 0.5 | 0.3 | 0.6 | 9.4 | small |
| Isaiah Stewart (MEM) | Questionable | 55% | 21.1 | 10.8 | 4.8 | 1.2 | 0.7 | 0.4 | 1.1 | 1.1 | 16.7 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 34.2<br><sub>31,33,33,25,29</sub> | 19.8<br><sub>8,22,13,12,15</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 10.7<br><sub>12,7,11,10,8</sub> |  | 5.8<br><sub>4,8,5,3,5</sub> |  | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.7 | 3.3 | 36.4 |
| Cedric Coward | 98% | 32.1<br><sub>23,28,27,30,33</sub> | 19.1<br><sub>10,3,15,14,23</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 8.7<br><sub>9,6,11,7,12</sub> |  | 3.9<br><sub>0,4,4,6,4</sub> |  | 2.1<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.6 | 2.1 | 31.7 |
| Jaylen Wells | 98% | 30.3<br><sub>25,26,31,27,25</sub> | 16.0<br><sub>7,14,22,11,5</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>0,4,2,2,2</sub> |  | 1.8<br><sub>0,1,1,1,2</sub> |  | 2.2<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.2 | 1.2 | 21.4 |
| Cam Spencer | 98% | 29.6<br><sub>19,17,20,24,34</sub> | 15.6<br><sub>7,7,15,14,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>1,2,3,2,1</sub> |  | 7.4<br><sub>0,4,3,5,8</sub> |  | 2.1<br><sub>1,1,3,3,3</sub> |  | 1.0 | 0.2 | 1.8 | 26.6 |
| Jerami Grant | 98% | 28.0<br><sub>22,22,20,26,-</sub> | 16.7<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>0,3,2,1,-</sub> |  | 2.0<br><sub>2,2,2,1,-</sub> |  | 1.9<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.6 | 1.7 | 21.8 |
| Javon Small | 96% | 28.0<br><sub>21,24,15,15,30</sub> | 15.7<br><sub>10,9,3,10,19</sub> |  | 4.1<br><sub>4,2,1,2,2</sub> |  | 4.9<br><sub>2,5,4,5,5</sub> |  | 1.7<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.7 | 24.7 |
| Taylor Hendricks | 80% | 24.8<br><sub>4,16,11,19,29</sub> | 11.7<br><sub>4,9,7,10,22</sub> |  | 5.8<br><sub>2,3,2,12,5</sub> |  | 1.5<br><sub>0,0,1,2,4</sub> |  | 1.4<br><sub>1,1,1,2,0</sub> |  | 1.3 | 0.7 | 1.2 | 18.9 |
| Olivier-Maxence Prosper | 67% | 18.1<br><sub>11,1,-,2,20</sub> | 10.6<br><sub>2,0,-,6,11</sub> |  | 4.0<br><sub>3,0,-,1,4</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 1.0<br><sub>0,0,-,0,2</sub> |  | 0.9 | 0.3 | 0.9 | 15.6 |
| Kris Murray | 80% | 17.7<br><sub>13,1,-,1,19</sub> | 3.9<br><sub>2,0,-,0,3</sub> |  | 3.1<br><sub>2,0,-,1,2</sub> |  | 1.2<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.4 | 0.6 | 8.3 |
| Jahmai Mashack | 52% | 13.3<br><sub>4,-,-,-,2</sub> | 4.3<br><sub>0,-,-,-,0</sub> |  | 1.8<br><sub>0,-,-,-,0</sub> |  | 1.7<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.8 | 0.3 | 0.9 | 7.9 |
| Karim Lopez | 52% | 10.1<br><sub>4,-,-,-,2</sub> | 3.1<br><sub>2,-,-,-,0</sub> |  | 2.6<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.4 | 0.5 | 6.2 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 36.6<br><sub>37,28,38,34,45</sub> | 21.0<br><sub>23,4,20,15,37</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,5,1,3,2</sub> |  | 10.0<br><sub>10,3,7,4,14</sub> |  | 2.6<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.6 | 34.5 |
| Anthony Davis | 98% | 36.1<br><sub>-,-,34,34,44</sub> | 25.0<br><sub>-,-,44,21,30</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 12.8<br><sub>-,-,13,13,15</sub> |  | 2.9<br><sub>-,-,1,0,4</sub> |  | 0.7<br><sub>-,-,2,0,0</sub> |  | 1.3 | 2.1 | 2.5 | 40.8 |
| AJ Dybantsa | 98% | 35.5<br><sub>36,31,37,34,44</sub> | 16.0<br><sub>11,19,21,13,5</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,6,8,4,8</sub> |  | 2.6<br><sub>3,3,1,2,4</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.7 | 2.4 | 25.2 |
| Kyshawn George | 98% | 33.9<br><sub>39,30,35,39,26</sub> | 17.8<br><sub>33,14,12,25,14</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>4,7,3,9,1</sub> |  | 4.6<br><sub>7,6,2,3,5</sub> |  | 2.4<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.4 | 2.6 | 27.8 |
| Alex Sarr | 98% | 29.7<br><sub>30,28,25,25,44</sub> | 13.8<br><sub>13,15,4,5,30</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 8.3<br><sub>8,14,8,8,9</sub> |  | 2.3<br><sub>3,1,0,0,2</sub> |  | 1.3<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 1.9 | 1.7 | 24.4 |
| Bilal Coulibaly | 98% | 26.7<br><sub>24,20,-,25,29</sub> | 9.7<br><sub>9,0,-,5,4</sub> | 6.5 · –<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>5,5,-,6,7</sub> |  | 1.9<br><sub>0,0,-,2,0</sub> |  | 0.8<br><sub>1,0,-,0,0</sub> |  | 1.3 | 1.0 | 1.2 | 16.1 |
| Bub Carrington | 98% | 18.0<br><sub>15,21,19,10,16</sub> | 6.3<br><sub>5,9,4,0,2</sub> |  | 2.1<br><sub>1,6,0,0,0</sub> |  | 2.4<br><sub>1,1,4,0,2</sub> |  | 0.9<br><sub>1,3,1,0,0</sub> |  | 0.5 | 0.2 | 1.1 | 10.8 |
| Deandre Ayton | 98% | 13.7<br><sub>23,7,13,9,9</sub> | 5.0<br><sub>8,2,2,2,2</sub> |  | 4.6<br><sub>11,1,8,2,4</sub> |  | 0.6<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.6 | 10.3 |
| Khris Middleton | 35% | 11.3<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.8 | 6.8 |
| Will Riley | 76% | 9.8<br><sub>9,20,4,-,3</sub> | 4.2<br><sub>7,5,0,-,3</sub> |  | 1.2<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.3<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 6.2 |
| Anthony Gill | 43% | 7.0<br><sub>-,9,2,-,-</sub> | 2.4<br><sub>-,1,0,-,-</sub> |  | 1.3<br><sub>-,1,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.1 |
| Tre Mann | 52% | 6.7<br><sub>-,18,2,-,-</sub> | 2.8<br><sub>-,2,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.7<br><sub>-,2,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Felix Okpara | 58% | 6.1<br><sub>-,-,2,-,-</sub> | 2.4<br><sub>-,-,2,-,-</sub> |  | 1.9<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.6 |

</details>

<details><summary>if Isaiah Stewart plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 33.8<br><sub>31,33,33,25,29</sub> | 19.0<br><sub>8,22,13,12,15</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 10.3<br><sub>12,7,11,10,8</sub> |  | 5.8<br><sub>4,8,5,3,5</sub> |  | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.7 | 3.2 | 35.1 |
| Cedric Coward (MEM) | 98% | 31.7<br><sub>23,28,27,30,33</sub> | 18.3<br><sub>10,3,15,14,23</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 8.5<br><sub>9,6,11,7,12</sub> |  | 3.8<br><sub>0,4,4,6,4</sub> |  | 2.0<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.5 | 2.0 | 30.7 |
| Jaylen Wells (MEM) | 98% | 29.4<br><sub>25,26,31,27,25</sub> | 14.4<br><sub>7,14,22,11,5</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>0,4,2,2,2</sub> |  | 1.8<br><sub>0,1,1,1,2</sub> |  | 2.0<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.2 | 1.2 | 19.6 |
| Cam Spencer (MEM) | 98% | 28.9<br><sub>19,17,20,24,34</sub> | 14.7<br><sub>7,7,15,14,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>1,2,3,2,1</sub> |  | 7.6<br><sub>0,4,3,5,8</sub> |  | 2.0<br><sub>1,1,3,3,3</sub> |  | 1.0 | 0.2 | 1.7 | 25.7 |
| Javon Small (MEM) | 96% | 27.2<br><sub>21,24,15,15,30</sub> | 14.3<br><sub>10,9,3,10,19</sub> |  | 3.9<br><sub>4,2,1,2,2</sub> |  | 5.2<br><sub>2,5,4,5,5</sub> |  | 1.6<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.6 | 23.3 |
| Jerami Grant (MEM) | 98% | 27.0<br><sub>22,22,20,26,-</sub> | 15.3<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>0,3,2,1,-</sub> |  | 2.0<br><sub>2,2,2,1,-</sub> |  | 1.8<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.6 | 1.5 | 20.2 |
| Taylor Hendricks (MEM) | 80% | 22.8<br><sub>4,16,11,19,29</sub> | 10.5<br><sub>4,9,7,10,22</sub> |  | 5.4<br><sub>2,3,2,12,5</sub> |  | 1.4<br><sub>0,0,1,2,4</sub> |  | 1.2<br><sub>1,1,1,2,0</sub> |  | 1.2 | 0.7 | 1.1 | 17.2 |
| Isaiah Stewart (MEM) | 100% | 21.1<br><sub>-,-,18,20,15</sub> | 10.8<br><sub>-,-,3,12,11</sub> |  | 4.8<br><sub>-,-,1,5,3</sub> |  | 1.2<br><sub>-,-,2,0,3</sub> |  | 0.7<br><sub>-,-,1,0,0</sub> |  | 0.4 | 1.1 | 1.1 | 16.7 |
| Olivier-Maxence Prosper (MEM) | 67% | 16.5<br><sub>11,1,-,2,20</sub> | 9.0<br><sub>2,0,-,6,11</sub> |  | 3.6<br><sub>3,0,-,1,4</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 0.9<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.2 | 0.9 | 13.5 |
| Kris Murray (MEM) | 80% | 16.0<br><sub>13,1,-,1,19</sub> | 3.7<br><sub>2,0,-,0,3</sub> |  | 2.8<br><sub>2,0,-,1,2</sub> |  | 1.1<br><sub>1,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.3 | 0.6 | 7.6 |
| Jahmai Mashack (MEM) | 52% | 11.4<br><sub>4,-,-,-,2</sub> | 3.6<br><sub>0,-,-,-,0</sub> |  | 1.5<br><sub>0,-,-,-,0</sub> |  | 1.4<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.7 | 0.2 | 0.8 | 6.6 |
| Karim Lopez (MEM) | 52% | 8.3<br><sub>4,-,-,-,2</sub> | 2.6<br><sub>2,-,-,-,0</sub> |  | 2.0<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 5.1 |
| Trae Young (WAS) | 98% | 36.5<br><sub>37,28,38,34,45</sub> | 21.1<br><sub>23,4,20,15,37</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,5,1,3,2</sub> |  | 10.0<br><sub>10,3,7,4,14</sub> |  | 2.6<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.6 | 34.6 |
| Anthony Davis (WAS) | 98% | 36.1<br><sub>-,-,34,34,44</sub> | 25.1<br><sub>-,-,44,21,30</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 12.8<br><sub>-,-,13,13,15</sub> |  | 3.0<br><sub>-,-,1,0,4</sub> |  | 0.7<br><sub>-,-,2,0,0</sub> |  | 1.3 | 2.1 | 2.5 | 40.8 |
| AJ Dybantsa (WAS) | 98% | 35.5<br><sub>36,31,37,34,44</sub> | 16.0<br><sub>11,19,21,13,5</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,6,8,4,8</sub> |  | 2.6<br><sub>3,3,1,2,4</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.7 | 2.4 | 25.3 |
| Kyshawn George (WAS) | 98% | 33.8<br><sub>39,30,35,39,26</sub> | 17.8<br><sub>33,14,12,25,14</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>4,7,3,9,1</sub> |  | 4.6<br><sub>7,6,2,3,5</sub> |  | 2.4<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.4 | 2.6 | 27.7 |
| Alex Sarr (WAS) | 98% | 29.8<br><sub>30,28,25,25,44</sub> | 13.8<br><sub>13,15,4,5,30</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 8.3<br><sub>8,14,8,8,9</sub> |  | 2.4<br><sub>3,1,0,0,2</sub> |  | 1.3<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 2.0 | 1.7 | 24.6 |
| Bilal Coulibaly (WAS) | 98% | 26.8<br><sub>24,20,-,25,29</sub> | 9.8<br><sub>9,0,-,5,4</sub> | 6.5 · –<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>5,5,-,6,7</sub> |  | 1.9<br><sub>0,0,-,2,0</sub> |  | 0.8<br><sub>1,0,-,0,0</sub> |  | 1.3 | 1.0 | 1.2 | 16.1 |
| Bub Carrington (WAS) | 98% | 18.0<br><sub>15,21,19,10,16</sub> | 6.3<br><sub>5,9,4,0,2</sub> |  | 2.1<br><sub>1,6,0,0,0</sub> |  | 2.4<br><sub>1,1,4,0,2</sub> |  | 0.9<br><sub>1,3,1,0,0</sub> |  | 0.6 | 0.2 | 1.1 | 10.8 |
| Deandre Ayton (WAS) | 98% | 13.8<br><sub>23,7,13,9,9</sub> | 5.1<br><sub>8,2,2,2,2</sub> |  | 4.6<br><sub>11,1,8,2,4</sub> |  | 0.6<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 10.3 |
| Khris Middleton (WAS) | 35% | 11.3<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.8 | 6.8 |
| Will Riley (WAS) | 76% | 9.8<br><sub>9,20,4,-,3</sub> | 4.3<br><sub>7,5,0,-,3</sub> |  | 1.2<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.3<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Anthony Gill (WAS) | 43% | 7.0<br><sub>-,9,2,-,-</sub> | 2.3<br><sub>-,1,0,-,-</sub> |  | 1.3<br><sub>-,1,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.1 |
| Tre Mann (WAS) | 52% | 6.8<br><sub>-,18,2,-,-</sub> | 2.9<br><sub>-,2,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.7<br><sub>-,2,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Felix Okpara (WAS) | 58% | 6.2<br><sub>-,-,2,-,-</sub> | 2.4<br><sub>-,-,2,-,-</sub> |  | 1.8<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.7 |

</details>

<details><summary>if Zach Edey plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 33.9<br><sub>31,33,33,25,29</sub> | 19.1<br><sub>8,22,13,12,15</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>12,7,11,10,8</sub> |  | 6.0<br><sub>4,8,5,3,5</sub> |  | 1.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.7 | 3.2 | 35.2 |
| Cedric Coward (MEM) | 98% | 31.8<br><sub>23,28,27,30,33</sub> | 18.1<br><sub>10,3,15,14,23</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 8.4<br><sub>9,6,11,7,12</sub> |  | 3.9<br><sub>0,4,4,6,4</sub> |  | 2.0<br><sub>2,1,1,0,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.5 | 2.1 | 30.5 |
| Jaylen Wells (MEM) | 98% | 29.5<br><sub>25,26,31,27,25</sub> | 14.4<br><sub>7,14,22,11,5</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>0,4,2,2,2</sub> |  | 1.8<br><sub>0,1,1,1,2</sub> |  | 2.0<br><sub>1,4,5,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.1 | 1.2 | 19.6 |
| Cam Spencer (MEM) | 98% | 28.8<br><sub>19,17,20,24,34</sub> | 14.5<br><sub>7,7,15,14,17</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>1,2,3,2,1</sub> |  | 7.6<br><sub>0,4,3,5,8</sub> |  | 2.0<br><sub>1,1,3,3,3</sub> |  | 1.0 | 0.2 | 1.7 | 25.5 |
| Javon Small (MEM) | 96% | 27.3<br><sub>21,24,15,15,30</sub> | 14.2<br><sub>10,9,3,10,19</sub> |  | 3.8<br><sub>4,2,1,2,2</sub> |  | 5.2<br><sub>2,5,4,5,5</sub> |  | 1.6<br><sub>1,1,1,2,3</sub> |  | 1.1 | 0.3 | 1.7 | 23.2 |
| Jerami Grant (MEM) | 98% | 27.0<br><sub>22,22,20,26,-</sub> | 15.3<br><sub>10,17,14,22,-</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>0,3,2,1,-</sub> |  | 2.0<br><sub>2,2,2,1,-</sub> |  | 1.8<br><sub>2,3,2,3,-</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.6 | 1.6 | 20.2 |
| Zach Edey (MEM) | 100% | 24.0<br><sub>20,23,20,-,-</sub> | 11.0<br><sub>14,8,2,-,-</sub> | 8.5 · – | 10.0<br><sub>6,9,5,-,-</sub> |  | 1.3<br><sub>1,1,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.6 | 1.5 | 1.7 | 22.3 |
| Taylor Hendricks (MEM) | 80% | 22.4<br><sub>4,16,11,19,29</sub> | 10.3<br><sub>4,9,7,10,22</sub> |  | 5.2<br><sub>2,3,2,12,5</sub> |  | 1.3<br><sub>0,0,1,2,4</sub> |  | 1.2<br><sub>1,1,1,2,0</sub> |  | 1.2 | 0.7 | 1.1 | 16.8 |
| Olivier-Maxence Prosper (MEM) | 67% | 16.2<br><sub>11,1,-,2,20</sub> | 8.8<br><sub>2,0,-,6,11</sub> |  | 3.6<br><sub>3,0,-,1,4</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 0.9<br><sub>0,0,-,0,2</sub> |  | 0.8 | 0.2 | 0.8 | 13.3 |
| Kris Murray (MEM) | 80% | 15.7<br><sub>13,1,-,1,19</sub> | 3.7<br><sub>2,0,-,0,3</sub> |  | 2.7<br><sub>2,0,-,1,2</sub> |  | 1.1<br><sub>1,0,-,0,3</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.7 | 0.3 | 0.6 | 7.4 |
| Jahmai Mashack (MEM) | 52% | 10.9<br><sub>4,-,-,-,2</sub> | 3.5<br><sub>0,-,-,-,0</sub> |  | 1.4<br><sub>0,-,-,-,0</sub> |  | 1.4<br><sub>2,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.8 | 6.3 |
| Karim Lopez (MEM) | 52% | 7.8<br><sub>4,-,-,-,2</sub> | 2.5<br><sub>2,-,-,-,0</sub> |  | 1.8<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.4 | 4.8 |
| Trae Young (WAS) | 98% | 36.5<br><sub>37,28,38,34,45</sub> | 21.1<br><sub>23,4,20,15,37</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,5,1,3,2</sub> |  | 10.0<br><sub>10,3,7,4,14</sub> |  | 2.6<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.6 | 34.6 |
| Anthony Davis (WAS) | 98% | 36.1<br><sub>-,-,34,34,44</sub> | 25.1<br><sub>-,-,44,21,30</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 12.8<br><sub>-,-,13,13,15</sub> |  | 3.0<br><sub>-,-,1,0,4</sub> |  | 0.7<br><sub>-,-,2,0,0</sub> |  | 1.3 | 2.2 | 2.5 | 40.8 |
| AJ Dybantsa (WAS) | 98% | 35.5<br><sub>36,31,37,34,44</sub> | 15.9<br><sub>11,19,21,13,5</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>9,6,8,4,8</sub> |  | 2.6<br><sub>3,3,1,2,4</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.7 | 2.4 | 25.2 |
| Kyshawn George (WAS) | 98% | 33.8<br><sub>39,30,35,39,26</sub> | 17.8<br><sub>33,14,12,25,14</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>4,7,3,9,1</sub> |  | 4.6<br><sub>7,6,2,3,5</sub> |  | 2.4<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.4 | 2.6 | 27.7 |
| Alex Sarr (WAS) | 98% | 29.8<br><sub>30,28,25,25,44</sub> | 13.8<br><sub>13,15,4,5,30</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 8.4<br><sub>8,14,8,8,9</sub> |  | 2.3<br><sub>3,1,0,0,2</sub> |  | 1.3<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 1.9 | 1.7 | 24.5 |
| Bilal Coulibaly (WAS) | 98% | 26.8<br><sub>24,20,-,25,29</sub> | 9.8<br><sub>9,0,-,5,4</sub> | 6.5 · –<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>5,5,-,6,7</sub> |  | 1.9<br><sub>0,0,-,2,0</sub> |  | 0.8<br><sub>1,0,-,0,0</sub> |  | 1.3 | 1.0 | 1.2 | 16.1 |
| Bub Carrington (WAS) | 98% | 18.0<br><sub>15,21,19,10,16</sub> | 6.3<br><sub>5,9,4,0,2</sub> |  | 2.1<br><sub>1,6,0,0,0</sub> |  | 2.5<br><sub>1,1,4,0,2</sub> |  | 0.9<br><sub>1,3,1,0,0</sub> |  | 0.5 | 0.2 | 1.1 | 10.8 |
| Deandre Ayton (WAS) | 98% | 13.8<br><sub>23,7,13,9,9</sub> | 5.0<br><sub>8,2,2,2,2</sub> |  | 4.6<br><sub>11,1,8,2,4</sub> |  | 0.6<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 10.3 |
| Khris Middleton (WAS) | 35% | 11.3<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.8 | 6.8 |
| Will Riley (WAS) | 76% | 9.8<br><sub>9,20,4,-,3</sub> | 4.3<br><sub>7,5,0,-,3</sub> |  | 1.2<br><sub>0,2,0,-,0</sub> |  | 0.8<br><sub>0,1,1,-,0</sub> |  | 0.3<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 6.3 |
| Anthony Gill (WAS) | 43% | 7.0<br><sub>-,9,2,-,-</sub> | 2.3<br><sub>-,1,0,-,-</sub> |  | 1.3<br><sub>-,1,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.1 |
| Tre Mann (WAS) | 52% | 6.8<br><sub>-,18,2,-,-</sub> | 2.9<br><sub>-,2,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.7<br><sub>-,2,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.4 |
| Felix Okpara (WAS) | 58% | 6.2<br><sub>-,-,2,-,-</sub> | 2.5<br><sub>-,-,2,-,-</sub> |  | 1.8<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.7 |

</details>


### PHI @ BKN
Out: Grant Nelson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Dominick Barlow (PHI), Adem Bona (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.3–110.2 | PHI 65% | 1.54 / 2.84 | BKN +5.5 | 225.5 | BKN +5.5 covers 51%; o225.5 50% |
| Expected (weighted by chance each plays) | 115.7–109.9 | PHI 66% | 1.50 / 2.98 | BKN +5.5 | 225.5 | BKN +5.5 covers 49%; o225.5 50% |
| if Joel Embiid plays | 115.7–109.9 | PHI 67% | 1.50 / 3.00 | BKN +5.5 | 225.5 | BKN +5.5 covers 49%; o225.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Joel Embiid (PHI) | Day-To-Day | 70% | 32.3 | 22.1 | 8.2 | 4.2 | 1.0 | 0.8 | 1.1 | 2.8 | 34.5 | full tables below |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.2<br><sub>34,32,36,34,35</sub> | 27.2<br><sub>19,17,27,24,27</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,3,4,1,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>7,4,7,4,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>3,2,3,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.6 | 0.7 | 2.6 | 37.3 |
| Jaylen Brown | 98% | 36.0<br><sub>37,34,35,26,36</sub> | 25.3<br><sub>30,20,29,13,18</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>7,5,7,5,6</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.2<br><sub>1,5,4,2,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>3,2,2,1,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.6 | 3.3 | 36.1 |
| VJ Edgecombe | 96% | 35.9<br><sub>35,32,35,32,36</sub> | 15.1<br><sub>11,19,13,8,15</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>6,3,6,4,8</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>3,2,3,5,8</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>1,3,3,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.6 | 0.5 | 1.6 | 25.6 |
| LeBron James | 98% | 34.7<br><sub>33,32,33,29,-</sub> | 19.3<br><sub>13,8,22,11,-</sub> |  | 6.9<br><sub>10,7,5,8,-</sub> |  | 6.9<br><sub>8,3,5,5,-</sub> |  | 1.3<br><sub>1,0,2,1,-</sub> |  | 1.4 | 0.7 | 3.2 | 33.1 |
| Dean Wade | 96% | 28.5<br><sub>22,21,18,23,34</sub> | 5.5<br><sub>3,0,0,8,6</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>5,5,1,9,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,1,1,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8<br><sub>0,0,0,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.4 | 0.8 | 11.7 |
| Kentavious Caldwell-Pope | 98% | 23.3<br><sub>21,17,21,16,27</sub> | 5.8<br><sub>5,5,6,0,11</sub> |  | 2.6<br><sub>1,2,6,0,4</sub> |  | 1.8<br><sub>0,0,3,2,5</sub> |  | 0.8<br><sub>1,1,2,0,3</sub> |  | 1.0 | 0.4 | 0.8 | 10.2 |
| Anfernee Simons | 98% | 22.5<br><sub>10,19,16,18,23</sub> | 10.6<br><sub>0,6,3,17,17</sub> |  | 2.3<br><sub>1,2,4,3,3</sub> |  | 1.8<br><sub>0,2,2,0,2</sub> |  | 1.9<br><sub>0,1,1,3,5</sub> |  | 0.6 | 0.1 | 1.0 | 14.7 |
| Jabari Walker | 88% | 15.4<br><sub>-,17,19,15,16</sub> | 5.9<br><sub>-,8,9,2,9</sub> |  | 4.4<br><sub>-,5,11,4,8</sub> |  | 0.8<br><sub>-,1,0,0,1</sub> |  | 0.5<br><sub>-,0,1,0,1</sub> |  | 0.5 | 0.2 | 0.7 | 11.0 |
| Rayan Rupert | 47% | 9.8<br><sub>-,-,-,6,-</sub> | 3.3<br><sub>-,-,-,0,-</sub> |  | 1.9<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.1 | 0.6 | 5.8 |
| Justin Edwards | 64% | 8.4<br><sub>-,4,-,6,1</sub> | 3.3<br><sub>-,3,-,0,0</sub> |  | 1.1<br><sub>-,1,-,0,1</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.3<br><sub>-,1,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |
| Tacko Fall | 67% | 8.2<br><sub>-,3,-,-,1</sub> | 0.5<br><sub>-,0,-,-,0</sub> |  | 2.1<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.4 | 0.3 | 2.8 |
| Labaron Philon Jr. | 67% | 8.1<br><sub>-,4,-,6,2</sub> | 3.2<br><sub>-,3,-,2,0</sub> |  | 1.2<br><sub>-,1,-,1,0</sub> |  | 0.8<br><sub>-,1,-,3,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Caleb Love | 48% | 8.0<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 1.2 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 76% | 31.9<br><sub>38,36,29,28,-</sub> | 20.0<br><sub>26,25,19,22,-</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>10,9,9,6,-</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,0,3,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>4,3,4,4,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.4 | 2.1 | 28.9 |
| Julius Randle | 98% | 31.5<br><sub>31,34,30,29,31</sub> | 18.3<br><sub>22,19,13,17,22</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>3,7,4,4,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>4,8,4,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 3.2 | 29.2 |
| Day'Ron Sharpe | 98% | 24.0<br><sub>27,32,20,19,28</sub> | 10.2<br><sub>6,12,6,15,16</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 8.0<br><sub>5,10,4,4,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>8,13,6,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 1.0 | 0.9 | 1.9 | 22.3 |
| Danny Wolf | 76% | 23.1<br><sub>19,31,36,29,28</sub> | 9.8<br><sub>12,11,10,10,14</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>5,9,3,11,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>2,2,1,1,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.5 | 0.6 | 1.3 | 17.7 |
| Egor Demin | 98% | 23.1<br><sub>-,-,-,23,27</sub> | 9.5<br><sub>-,-,-,22,11</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>-,-,-,1,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>-,-,-,1,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>-,-,-,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.3 | 1.5 | 15.1 |
| Mikel Brown Jr. | 97% | 22.1<br><sub>20,25,-,-,20</sub> | 10.7<br><sub>18,18,-,-,6</sub> |  | 2.4<br><sub>2,1,-,-,1</sub> |  | 3.3<br><sub>4,3,-,-,2</sub> |  | 1.4<br><sub>3,3,-,-,2</sub> |  | 0.7 | 0.2 | 1.8 | 16.4 |
| Nolan Traore | 98% | 21.6<br><sub>27,23,21,-,20</sub> | 10.7<br><sub>16,19,14,-,11</sub> |  | 2.0<br><sub>4,1,1,-,1</sub> |  | 3.1<br><sub>2,2,2,-,2</sub> |  | 1.2<br><sub>2,2,2,-,0</sub> |  | 0.8 | 0.4 | 2.2 | 15.9 |
| Noah Clowney | 98% | 21.4<br><sub>17,21,8,19,35</sub> | 8.4<br><sub>7,3,2,16,15</sub> |  | 4.1<br><sub>1,10,0,3,7</sub> |  | 1.1<br><sub>1,0,0,0,3</sub> |  | 1.1<br><sub>1,1,0,2,3</sub> |  | 0.5 | 0.6 | 1.0 | 13.5 |
| Moritz Wagner | 96% | 17.0<br><sub>20,16,16,19,18</sub> | 9.3<br><sub>6,9,12,16,10</sub> |  | 4.0<br><sub>1,2,3,3,6</sub> |  | 1.3<br><sub>0,0,1,4,4</sub> |  | 0.8<br><sub>0,1,1,2,2</sub> |  | 0.5 | 0.2 | 0.9 | 14.7 |
| Keon Ellis | 88% | 14.8<br><sub>10,-,22,26,7</sub> | 3.6<br><sub>1,-,3,11,0</sub> |  | 1.6<br><sub>2,-,1,4,0</sub> |  | 1.0<br><sub>0,-,4,3,1</sub> |  | 0.4<br><sub>0,-,1,2,0</sub> |  | 0.8 | 0.4 | 0.5 | 6.2 |
| Chaney Johnson | 97% | 13.2<br><sub>9,8,15,15,12</sub> | 3.7<br><sub>0,5,2,4,1</sub> |  | 2.2<br><sub>2,2,0,3,5</sub> |  | 0.8<br><sub>1,1,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 6.6 |
| Terance Mann | 80% | 12.7<br><sub>16,13,22,18,9</sub> | 3.0<br><sub>0,0,0,6,2</sub> |  | 1.5<br><sub>2,2,1,1,1</sub> |  | 1.2<br><sub>2,0,1,3,1</sub> |  | 0.2<br><sub>0,0,0,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.7 |
| Josh Minott | 67% | 7.7<br><sub>6,-,12,7,2</sub> | 4.2<br><sub>0,-,10,0,0</sub> |  | 1.5<br><sub>1,-,2,2,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.4<br><sub>0,-,2,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 6.1 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. (BKN) | 76% | 31.9<br><sub>38,36,29,28,-</sub> | 20.1<br><sub>26,25,19,22,-</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>10,9,9,6,-</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>0,1,0,3,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>4,3,4,4,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.4 | 2.1 | 29.0 |
| Julius Randle (BKN) | 98% | 31.5<br><sub>31,34,30,29,31</sub> | 18.2<br><sub>22,19,13,17,22</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>3,7,4,4,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>4,8,4,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>2,1,0,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 3.1 | 29.1 |
| Day'Ron Sharpe (BKN) | 98% | 24.1<br><sub>27,32,20,19,28</sub> | 10.2<br><sub>6,12,6,15,16</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 8.1<br><sub>5,10,4,4,11</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>8,13,6,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,2,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 1.0 | 0.9 | 1.9 | 22.4 |
| Egor Demin (BKN) | 98% | 23.1<br><sub>-,-,-,23,27</sub> | 9.5<br><sub>-,-,-,22,11</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>-,-,-,1,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>-,-,-,1,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>-,-,-,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.3 | 1.5 | 15.1 |
| Danny Wolf (BKN) | 76% | 23.0<br><sub>19,31,36,29,28</sub> | 9.8<br><sub>12,11,10,10,14</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>5,9,3,11,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>2,2,1,1,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.5 | 0.6 | 1.3 | 17.6 |
| Mikel Brown Jr. (BKN) | 97% | 22.1<br><sub>20,25,-,-,20</sub> | 10.8<br><sub>18,18,-,-,6</sub> |  | 2.4<br><sub>2,1,-,-,1</sub> |  | 3.3<br><sub>4,3,-,-,2</sub> |  | 1.4<br><sub>3,3,-,-,2</sub> |  | 0.7 | 0.2 | 1.8 | 16.5 |
| Nolan Traore (BKN) | 98% | 21.6<br><sub>27,23,21,-,20</sub> | 10.6<br><sub>16,19,14,-,11</sub> |  | 2.0<br><sub>4,1,1,-,1</sub> |  | 3.1<br><sub>2,2,2,-,2</sub> |  | 1.1<br><sub>2,2,2,-,0</sub> |  | 0.9 | 0.4 | 2.2 | 15.7 |
| Noah Clowney (BKN) | 98% | 21.4<br><sub>17,21,8,19,35</sub> | 8.4<br><sub>7,3,2,16,15</sub> |  | 4.1<br><sub>1,10,0,3,7</sub> |  | 1.1<br><sub>1,0,0,0,3</sub> |  | 1.1<br><sub>1,1,0,2,3</sub> |  | 0.6 | 0.6 | 1.0 | 13.5 |
| Moritz Wagner (BKN) | 96% | 17.0<br><sub>20,16,16,19,18</sub> | 9.3<br><sub>6,9,12,16,10</sub> |  | 4.0<br><sub>1,2,3,3,6</sub> |  | 1.3<br><sub>0,0,1,4,4</sub> |  | 0.8<br><sub>0,1,1,2,2</sub> |  | 0.5 | 0.3 | 1.0 | 14.7 |
| Keon Ellis (BKN) | 88% | 14.8<br><sub>10,-,22,26,7</sub> | 3.6<br><sub>1,-,3,11,0</sub> |  | 1.6<br><sub>2,-,1,4,0</sub> |  | 1.0<br><sub>0,-,4,3,1</sub> |  | 0.4<br><sub>0,-,1,2,0</sub> |  | 0.8 | 0.4 | 0.5 | 6.2 |
| Chaney Johnson (BKN) | 97% | 13.1<br><sub>9,8,15,15,12</sub> | 3.6<br><sub>0,5,2,4,1</sub> |  | 2.2<br><sub>2,2,0,3,5</sub> |  | 0.8<br><sub>1,1,1,2,0</sub> |  | 0.3<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 6.6 |
| Terance Mann (BKN) | 80% | 12.6<br><sub>16,13,22,18,9</sub> | 3.0<br><sub>0,0,0,6,2</sub> |  | 1.5<br><sub>2,2,1,1,1</sub> |  | 1.2<br><sub>2,0,1,3,1</sub> |  | 0.2<br><sub>0,0,0,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.7 |
| Josh Minott (BKN) | 67% | 7.8<br><sub>6,-,12,7,2</sub> | 4.2<br><sub>0,-,10,0,0</sub> |  | 1.5<br><sub>1,-,2,2,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.5<br><sub>0,-,2,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 6.1 |
| Tyrese Maxey (PHI) | 98% | 36.9<br><sub>34,32,36,34,35</sub> | 23.7<br><sub>19,17,27,24,27</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>1,3,4,1,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 6.0<br><sub>7,4,7,4,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>3,2,3,3,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.6 | 0.6 | 2.3 | 33.3 |
| Jaylen Brown (PHI) | 98% | 35.4<br><sub>37,34,35,26,36</sub> | 22.2<br><sub>30,20,29,13,18</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>7,5,7,5,6</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 4.0<br><sub>1,5,4,2,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,2,2,1,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.6 | 3.1 | 32.5 |
| VJ Edgecombe (PHI) | 96% | 34.3<br><sub>35,32,35,32,36</sub> | 12.8<br><sub>11,19,13,8,15</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.9<br><sub>6,3,6,4,8</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>3,2,3,5,8</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,3,3,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.5 | 1.6 | 22.6 |
| LeBron James (PHI) | 98% | 33.7<br><sub>33,32,33,29,-</sub> | 16.7<br><sub>13,8,22,11,-</sub> |  | 6.5<br><sub>10,7,5,8,-</sub> |  | 6.6<br><sub>8,3,5,5,-</sub> |  | 1.2<br><sub>1,0,2,1,-</sub> |  | 1.3 | 0.6 | 2.9 | 29.8 |
| Joel Embiid (PHI) | 100% | 32.3<br><sub>33,25,29,31,28</sub> | 22.1<br><sub>26,6,18,16,20</sub> | 21.5 · – | 8.2<br><sub>15,7,10,6,4</sub> | 8.5 | 4.2<br><sub>2,1,5,1,3</sub> | 3.5 | 1.0<br><sub>0,0,0,1,0</sub> | 0.5 | 0.8 | 1.1 | 2.8 | 34.5 |
| Dean Wade (PHI) | 96% | 23.6<br><sub>22,21,18,23,34</sub> | 4.1<br><sub>3,0,0,8,6</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>5,5,1,9,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>1,1,1,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.5<br><sub>0,0,0,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.3 | 0.6 | 9.2 |
| Kentavious Caldwell-Pope (PHI) | 98% | 19.5<br><sub>21,17,21,16,27</sub> | 4.6<br><sub>5,5,6,0,11</sub> |  | 2.2<br><sub>1,2,6,0,4</sub> |  | 1.5<br><sub>0,0,3,2,5</sub> |  | 0.6<br><sub>1,1,2,0,3</sub> |  | 0.9 | 0.3 | 0.6 | 8.2 |
| Anfernee Simons (PHI) | 98% | 19.5<br><sub>10,19,16,18,23</sub> | 8.5<br><sub>0,6,3,17,17</sub> |  | 1.9<br><sub>1,2,4,3,3</sub> |  | 1.5<br><sub>0,2,2,0,2</sub> |  | 1.5<br><sub>0,1,1,3,5</sub> |  | 0.5 | 0.1 | 0.9 | 12.0 |
| Jabari Walker (PHI) | 88% | 12.6<br><sub>-,17,19,15,16</sub> | 4.9<br><sub>-,8,9,2,9</sub> |  | 3.6<br><sub>-,5,11,4,8</sub> |  | 0.6<br><sub>-,1,0,0,1</sub> |  | 0.3<br><sub>-,0,1,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 9.1 |
| Rayan Rupert (PHI) | 47% | 7.8<br><sub>-,-,-,6,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 1.5<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 4.9 |
| Justin Edwards (PHI) | 64% | 6.5<br><sub>-,4,-,6,1</sub> | 2.7<br><sub>-,3,-,0,0</sub> |  | 0.9<br><sub>-,1,-,0,1</sub> |  | 0.4<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,1,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Caleb Love (PHI) | 48% | 6.5<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 1.0 |
| Tacko Fall (PHI) | 67% | 6.4<br><sub>-,3,-,-,1</sub> | 0.3<br><sub>-,0,-,-,0</sub> |  | 1.7<br><sub>-,1,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.3 | 0.4 | 2.3 |
| Labaron Philon Jr. (PHI) | 67% | 5.9<br><sub>-,4,-,6,2</sub> | 2.5<br><sub>-,3,-,2,0</sub> |  | 0.9<br><sub>-,1,-,1,0</sub> |  | 0.6<br><sub>-,1,-,3,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.1 |

</details>


### HOU @ MIA
Out: Clint Capela (HOU), Marcus Smart (HOU), Fred VanVleet (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.6–116.0 | HOU 57% | 1.74 / 2.35 | MIA +2.5 | 234.5 | MIA +2.5 covers 48%; o230.5 58% |
| Expected (weighted by chance each plays) | 117.8–117.2 | HOU 52% | 1.92 / 2.08 | MIA +1.5 | 234.5 | MIA +2.5 covers 54%; o230.5 59% |
| if Pelle Larsson plays | 117.2–118.0 | HOU 48% | 2.08 / 1.92 | MIA -1.5 | 234.5 | MIA +2.5 covers 58%; o230.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pelle Larsson (MIA) | Questionable | 55% | 27.4 | 10.8 | 3.3 | 3.0 | 1.0 | 0.9 | 0.2 | 1.6 | 17.0 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 38.4<br><sub>32,39,35,29,41</sub> | 18.7<br><sub>11,17,8,19,12</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 7.9<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.7 | 0.7 | 2.4 | 31.9 |
| Alperen Sengun | 91% | 37.7<br><sub>39,32,35,37,37</sub> | 24.5<br><sub>17,15,20,19,43</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 10.5<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 7.1<br><sub>10,5,8,9,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 0.8<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.3 | 1.2 | 3.4 | 42.1 |
| Kevin Durant | 98% | 37.5<br><sub>35,38,36,34,33</sub> | 25.9<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.2<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 1.0 | 3.6 | 37.9 |
| Jabari Smith Jr. | 98% | 36.8<br><sub>35,39,38,35,24</sub> | 16.9<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>2,1,2,2,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.9 | 1.4 | 26.5 |
| Tari Eason | 98% | 31.0<br><sub>24,23,19,22,33</sub> | 12.2<br><sub>9,2,12,6,14</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>6,7,5,3,11</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.6 | 0.8 | 1.4 | 21.6 |
| Reed Sheppard | 88% | 25.8<br><sub>21,13,17,20,19</sub> | 12.6<br><sub>14,6,8,13,0</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>2,0,0,1,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>2,0,0,1,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.6 | 1.3 | 18.6 |
| Bogdan Bogdanovic | 97% | 16.2<br><sub>5,2,12,10,12</sub> | 6.2<br><sub>0,0,8,0,11</sub> |  | 1.9<br><sub>0,1,3,0,1</sub> |  | 1.6<br><sub>0,0,1,0,3</sub> |  | 0.9<br><sub>0,0,2,0,3</sub> |  | 0.5 | 0.1 | 0.7 | 9.7 |
| Steven Adams | 23% | 15.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 5.6<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.5 | 0.9 | 10.2 |
| Oscar Tshiebwe | 91% | 11.5<br><sub>2,3,-,1,6</sub> | 4.3<br><sub>2,2,-,0,0</sub> |  | 4.8<br><sub>0,0,-,0,5</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 9.8 |
| Julian Phillips | 8% | 11.3 | 3.6 |  | 1.3 |  | 0.6 |  | 0.3 |  | 0.5 | 0.2 | 0.4 | 5.4 |
| Bruce Thornton | 58% | 9.8<br><sub>-,-,1,3,-</sub> | 3.0<br><sub>-,-,0,0,-</sub> |  | 2.4<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.1 |
| Jae'Sean Tate | 52% | 9.6<br><sub>-,-,-,1,-</sub> | 2.9<br><sub>-,-,-,0,-</sub> |  | 2.3<br><sub>-,-,-,0,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford | 58% | 9.1<br><sub>-,-,1,1,-</sub> | 2.8<br><sub>-,-,0,0,-</sub> |  | 1.4<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.5 |
| Quadir Copeland | 3% | 8.8 | 3.7 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.1 | 0.4 | 6.0 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 37.5<br><sub>38,40,38,39,32</sub> | 15.2<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.4<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 2.2 | 26.6 |
| Bam Adebayo | 98% | 36.9<br><sub>33,34,37,38,36</sub> | 20.1<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 10.0<br><sub>10,8,8,14,5</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>0,1,0,2,1</sub> |  | 1.8 | 0.7 | 1.7 | 33.8 |
| Giannis Antetokounmpo | 98% | 34.9<br><sub>31,34,31,31,31</sub> | 28.7<br><sub>20,29,30,37,34</sub> | 28.5 · –<br><sub>o 48% · u 52%</sub> | 12.1<br><sub>14,14,11,9,14</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>4,3,4,2,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 40% · u 60%</sub> | 1.1 | 1.0 | 3.5 | 46.4 |
| Andrew Wiggins | 98% | 27.8<br><sub>21,32,19,32,23</sub> | 10.3<br><sub>2,6,13,8,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.8 | 1.1 | 15.6 |
| Klay Thompson | 83% | 27.0<br><sub>23,32,30,-,20</sub> | 13.4<br><sub>11,23,11,-,26</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,2,1,-,1</sub> |  | 1.8<br><sub>3,4,2,-,4</sub> |  | 2.7<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.6 | 1.1 | 17.1 |
| Ryan Conwell | 91% | 23.7<br><sub>30,19,21,33,26</sub> | 8.3<br><sub>13,6,5,20,9</sub> |  | 2.6<br><sub>1,2,4,5,4</sub> |  | 1.7<br><sub>2,2,2,2,1</sub> |  | 1.4<br><sub>3,2,1,4,2</sub> |  | 0.8 | 0.1 | 0.9 | 12.6 |
| Bobby Portis | 98% | 20.1<br><sub>14,20,17,15,18</sub> | 7.9<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,1,2,2</sub> |  | 1.1<br><sub>0,1,1,1,1</sub> |  | 0.6 | 0.3 | 0.7 | 14.3 |
| Myron Gardner | 67% | 16.7<br><sub>1,-,10,19,26</sub> | 4.5<br><sub>0,-,4,0,5</sub> |  | 4.4<br><sub>0,-,3,4,9</sub> |  | 1.6<br><sub>0,-,1,2,3</sub> |  | 0.5<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.4 | 0.7 | 10.5 |
| Tim Hardaway Jr. | 64% | 15.8<br><sub>4,7,-,20,-</sub> | 6.1<br><sub>0,0,-,4,-</sub> |  | 1.6<br><sub>0,0,-,3,-</sub> |  | 0.8<br><sub>1,0,-,2,-</sub> |  | 0.9<br><sub>0,0,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 8.4 |
| Nikola Jovic | 52% | 12.6<br><sub>12,-,-,-,11</sub> | 3.9<br><sub>1,-,-,-,2</sub> |  | 2.2<br><sub>0,-,-,-,1</sub> |  | 1.1<br><sub>1,-,-,-,2</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.2 |
| Simone Fontecchio | 64% | 11.7<br><sub>-,-,7,7,14</sub> | 5.0<br><sub>-,-,3,0,7</sub> |  | 1.9<br><sub>-,-,0,0,5</sub> |  | 0.8<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 7.8 |
| Dru Smith | 52% | 11.3<br><sub>1,-,-,6,-</sub> | 3.4<br><sub>0,-,-,0,-</sub> |  | 1.5<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>0,-,-,1,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.8 | 0.2 | 0.6 | 6.5 |
| Keshad Johnson | 52% | 7.7<br><sub>-,-,-,-,1</sub> | 2.9<br><sub>-,-,-,-,0</sub> |  | 1.6<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 4.9 |
| Nick Richards | 38% | 7.1<br><sub>1,-,-,-,-</sub> | 2.4<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.1 |
| Tre Donaldson | 58% | 7.0<br><sub>-,-,-,-,1</sub> | 6.1<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 3.7 | 6.8 |

</details>

<details><summary>if Pelle Larsson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 38.4<br><sub>32,39,35,29,41</sub> | 18.7<br><sub>11,17,8,19,12</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 7.8<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.7 | 0.7 | 2.4 | 31.9 |
| Alperen Sengun (HOU) | 91% | 37.7<br><sub>39,32,35,37,37</sub> | 24.4<br><sub>17,15,20,19,43</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 10.5<br><sub>12,6,12,13,12</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>10,5,8,9,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 0.8<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.3 | 1.2 | 3.4 | 42.1 |
| Kevin Durant (HOU) | 98% | 37.5<br><sub>35,38,36,34,33</sub> | 25.7<br><sub>21,21,23,20,22</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 1.0 | 3.6 | 37.7 |
| Jabari Smith Jr. (HOU) | 98% | 36.7<br><sub>35,39,38,35,24</sub> | 16.8<br><sub>11,15,14,14,6</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>2,1,2,2,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.9 | 1.4 | 26.4 |
| Tari Eason (HOU) | 98% | 31.0<br><sub>24,23,19,22,33</sub> | 12.1<br><sub>9,2,12,6,14</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>6,7,5,3,11</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.6 | 0.8 | 1.4 | 21.5 |
| Reed Sheppard (HOU) | 88% | 25.9<br><sub>21,13,17,20,19</sub> | 12.5<br><sub>14,6,8,13,0</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>2,0,0,1,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>2,0,0,1,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.6 | 1.3 | 18.6 |
| Bogdan Bogdanovic (HOU) | 97% | 16.3<br><sub>5,2,12,10,12</sub> | 6.2<br><sub>0,0,8,0,11</sub> |  | 1.9<br><sub>0,1,3,0,1</sub> |  | 1.7<br><sub>0,0,1,0,3</sub> |  | 0.9<br><sub>0,0,2,0,3</sub> |  | 0.5 | 0.1 | 0.7 | 9.8 |
| Steven Adams (HOU) | 23% | 15.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 5.6<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.6 | 1.0 | 10.2 |
| Oscar Tshiebwe (HOU) | 91% | 11.5<br><sub>2,3,-,1,6</sub> | 4.3<br><sub>2,2,-,0,0</sub> |  | 4.8<br><sub>0,0,-,0,5</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 9.7 |
| Julian Phillips (HOU) | 8% | 11.4 | 3.6 |  | 1.3 |  | 0.5 |  | 0.4 |  | 0.6 | 0.2 | 0.4 | 5.5 |
| Bruce Thornton (HOU) | 58% | 9.8<br><sub>-,-,1,3,-</sub> | 3.0<br><sub>-,-,0,0,-</sub> |  | 2.4<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.1 |
| Jae'Sean Tate (HOU) | 52% | 9.7<br><sub>-,-,-,1,-</sub> | 2.9<br><sub>-,-,-,0,-</sub> |  | 2.3<br><sub>-,-,-,0,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.8 |
| Isaiah Crawford (HOU) | 58% | 9.0<br><sub>-,-,1,1,-</sub> | 2.7<br><sub>-,-,0,0,-</sub> |  | 1.4<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.5 |
| Quadir Copeland (HOU) | 3% | 8.6 | 3.4 |  | 1.5 |  | 0.7 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.7 |
| Davion Mitchell (MIA) | 98% | 35.8<br><sub>38,40,38,39,32</sub> | 14.1<br><sub>22,17,19,22,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,3,5,5,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 8.2<br><sub>8,11,8,17,9</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>4,2,3,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 2.1 | 25.2 |
| Bam Adebayo (MIA) | 98% | 35.6<br><sub>33,34,37,38,36</sub> | 19.8<br><sub>18,18,11,37,20</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 9.6<br><sub>10,8,8,14,5</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>0,4,4,3,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>0,1,0,2,1</sub> |  | 1.7 | 0.7 | 1.7 | 32.9 |
| Giannis Antetokounmpo (MIA) | 98% | 34.3<br><sub>31,34,31,31,31</sub> | 28.8<br><sub>20,29,30,37,34</sub> | 28.5 · –<br><sub>o 48% · u 52%</sub> | 12.1<br><sub>14,14,11,9,14</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 5.4<br><sub>4,3,4,2,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>1,0,1,1,1</sub> | 0.5<br><sub>o 40% · u 60%</sub> | 1.2 | 1.0 | 3.5 | 46.4 |
| Pelle Larsson (MIA) | 100% | 27.4<br><sub>29,22,31,-,-</sub> | 10.8<br><sub>13,11,14,-,-</sub> | 10.5 · – | 3.3<br><sub>1,3,7,-,-</sub> | 3.5 | 3.0<br><sub>4,3,2,-,-</sub> |  | 1.0<br><sub>3,3,2,-,-</sub> | 1.5 | 0.9 | 0.2 | 1.6 | 17.0 |
| Andrew Wiggins (MIA) | 98% | 24.8<br><sub>21,32,19,32,23</sub> | 9.3<br><sub>2,6,13,8,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>6,3,0,3,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.7<br><sub>4,1,0,4,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,2,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.7 | 1.1 | 14.2 |
| Klay Thompson (MIA) | 83% | 22.8<br><sub>23,32,30,-,20</sub> | 11.5<br><sub>11,23,11,-,26</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,2,1,-,1</sub> |  | 1.5<br><sub>3,4,2,-,4</sub> |  | 2.2<br><sub>2,7,2,-,6</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.4 | 1.0 | 14.8 |
| Ryan Conwell (MIA) | 91% | 18.8<br><sub>30,19,21,33,26</sub> | 6.8<br><sub>13,6,5,20,9</sub> |  | 2.1<br><sub>1,2,4,5,4</sub> |  | 1.4<br><sub>2,2,2,2,1</sub> |  | 1.0<br><sub>3,2,1,4,2</sub> |  | 0.6 | 0.1 | 0.8 | 10.3 |
| Bobby Portis (MIA) | 98% | 17.6<br><sub>14,20,17,15,18</sub> | 7.1<br><sub>0,4,5,5,7</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>5,1,1,3,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,1,1,2,2</sub> |  | 0.9<br><sub>0,1,1,1,1</sub> |  | 0.5 | 0.2 | 0.7 | 12.7 |
| Myron Gardner (MIA) | 67% | 11.9<br><sub>1,-,10,19,26</sub> | 3.3<br><sub>0,-,4,0,5</sub> |  | 3.2<br><sub>0,-,3,4,9</sub> |  | 1.2<br><sub>0,-,1,2,3</sub> |  | 0.3<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.7 |
| Tim Hardaway Jr. (MIA) | 64% | 10.2<br><sub>4,7,-,20,-</sub> | 4.0<br><sub>0,0,-,4,-</sub> |  | 1.0<br><sub>0,0,-,3,-</sub> |  | 0.5<br><sub>1,0,-,2,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Nikola Jovic (MIA) | 52% | 9.9<br><sub>12,-,-,-,11</sub> | 3.1<br><sub>1,-,-,-,2</sub> |  | 1.7<br><sub>0,-,-,-,1</sub> |  | 0.9<br><sub>1,-,-,-,2</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.7 |
| Simone Fontecchio (MIA) | 64% | 9.6<br><sub>-,-,7,7,14</sub> | 4.4<br><sub>-,-,3,0,7</sub> |  | 1.6<br><sub>-,-,0,0,5</sub> |  | 0.7<br><sub>-,-,0,2,0</sub> |  | 0.5<br><sub>-,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 6.6 |
| Dru Smith (MIA) | 52% | 7.3<br><sub>1,-,-,6,-</sub> | 2.3<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.3 |
| Keshad Johnson (MIA) | 52% | 6.5<br><sub>-,-,-,-,1</sub> | 2.7<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.4 |
| Nick Richards (MIA) | 38% | 5.8<br><sub>1,-,-,-,-</sub> | 2.2<br><sub>0,-,-,-,-</sub> |  | 2.1<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 4.6 |
| Tre Donaldson (MIA) | 58% | 5.6<br><sub>-,-,-,-,1</sub> | 6.0<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 3.2 | 6.6 |

</details>


### POR @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.2<br><sub>39,24,34,35,35</sub> | 23.7<br><sub>22,15,24,28,34</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>9,4,6,3,6</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.2<br><sub>11,1,8,6,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>1,2,2,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.6 | 3.7 | 36.3 |
| Toumani Camara | 98% | 32.2<br><sub>30,21,30,38,36</sub> | 11.9<br><sub>18,4,12,14,14</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>6,4,3,5,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>1,0,3,3,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,0,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.5 | 1.4 | 18.1 |
| Damian Lillard | 98% | 32.0<br><sub>37,20,24,32,33</sub> | 19.7<br><sub>22,12,25,18,29</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>0,0,3,3,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>4,7,3,3,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.7<br><sub>4,2,4,2,6</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.2 | 2.5 | 28.3 |
| Jrue Holiday | 98% | 28.6<br><sub>31,20,25,30,27</sub> | 13.4<br><sub>12,11,11,19,6</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,0,1,3,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>7,0,2,5,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,1,2,5,0</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 2.4 | 22.0 |
| Donovan Clingan | 98% | 26.4<br><sub>28,22,26,30,27</sub> | 10.8<br><sub>17,6,7,5,13</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>11,5,13,12,11</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>1,0,3,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0<br><sub>3,0,1,1,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.6 | 2.0 | 1.4 | 22.9 |
| Scoot Henderson | 98% | 25.1<br><sub>23,24,23,19,23</sub> | 11.3<br><sub>2,13,11,5,11</sub> |  | 2.5<br><sub>2,2,1,2,0</sub> |  | 2.7<br><sub>0,1,4,2,1</sub> |  | 1.3<br><sub>0,0,3,1,2</sub> |  | 0.9 | 0.2 | 2.3 | 16.5 |
| Sidy Cissoko | 98% | 25.0<br><sub>22,16,33,29,26</sub> | 7.1<br><sub>7,4,17,19,3</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,3,3,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>3,1,3,0,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.4 | 1.1 | 12.4 |
| Robert Williams III | 98% | 17.2<br><sub>16,-,15,17,17</sub> | 6.3<br><sub>9,-,6,10,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>5,-,4,7,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>2,-,0,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.3 | 0.9 | 13.9 |
| Jayson Kent | 63% | 12.2<br><sub>-,12,-,-,11</sub> | 4.0<br><sub>-,4,-,-,3</sub> |  | 1.6<br><sub>-,1,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,1</sub> |  | 0.5 | 0.2 | 0.7 | 6.1 |
| Branden Carlson | 76% | 9.6<br><sub>-,12,8,10,8</sub> | 2.8<br><sub>-,4,2,0,5</sub> |  | 2.4<br><sub>-,2,5,2,3</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 0.2<br><sub>-,0,0,0,1</sub> |  | 0.2 | 0.6 | 0.5 | 5.7 |
| Micah Potter | 52% | 8.4<br><sub>-,14,5,-,-</sub> | 3.6<br><sub>-,7,0,-,-</sub> |  | 2.3<br><sub>-,3,3,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.3 |
| Yang Hansen | 52% | 8.0<br><sub>3,26,5,-,-</sub> | 3.1<br><sub>2,12,0,-,-</sub> |  | 2.1<br><sub>0,10,1,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.1 | 0.2 | 0.6 | 5.6 |
| John Tonje | 36% | 6.8<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.4 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 35.2<br><sub>37,40,33,25,37</sub> | 16.7<br><sub>14,23,16,16,18</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>8,6,6,9,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>4,5,3,3,6</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>0,2,2,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3 | 1.0 | 2.1 | 25.7 |
| Ayo Dosunmu | 98% | 33.4<br><sub>34,39,30,27,33</sub> | 18.8<br><sub>21,26,26,18,24</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>1,2,4,2,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.7<br><sub>6,4,1,1,0</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,4,4,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 2.3 | 26.9 |
| Jonathan Kuminga | 98% | 31.7<br><sub>32,34,25,24,35</sub> | 14.1<br><sub>16,17,4,14,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>8,8,0,8,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>5,4,0,5,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>4,1,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 1.7 | 22.3 |
| LaMelo Ball | 98% | 30.6<br><sub>31,35,30,25,30</sub> | 21.0<br><sub>20,22,24,22,19</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>2,2,3,3,8</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.2<br><sub>6,8,5,9,6</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 3.5<br><sub>4,3,4,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.7 | 0.3 | 3.3 | 31.6 |
| Rudy Gobert | 98% | 29.9<br><sub>33,25,31,23,27</sub> | 9.9<br><sub>8,8,10,9,1</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 10.8<br><sub>11,11,15,6,10</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>2,0,2,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.4 | 1.4 | 22.5 |
| Terrence Shannon Jr. | 98% | 22.3<br><sub>-,-,18,21,22</sub> | 10.8<br><sub>-,-,5,6,14</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>-,-,3,2,6</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>-,-,3,4,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.1 | 1.2 | 15.4 |
| Trey Lyles | 98% | 19.6<br><sub>20,29,21,15,19</sub> | 6.0<br><sub>5,5,9,2,5</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>2,13,6,0,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>0,2,2,0,2</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 11.0 |
| Bones Hyland | 98% | 18.1<br><sub>16,10,13,23,21</sub> | 10.0<br><sub>19,4,14,24,12</sub> |  | 1.9<br><sub>2,1,2,3,1</sub> |  | 2.8<br><sub>4,0,2,8,2</sub> |  | 1.4<br><sub>4,1,1,5,3</sub> |  | 0.8 | 0.3 | 1.3 | 14.7 |
| Joan Beringer | 98% | 14.7<br><sub>13,7,16,22,13</sub> | 6.0<br><sub>4,2,4,13,2</sub> |  | 5.1<br><sub>7,3,3,9,5</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 11.6 |
| Rocco Zikarsky | 38% | 7.3<br><sub>-,-,2,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.2<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.2 |
| Zyon Pullin | 35% | 7.2<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.6 |
| Cody Williams | 52% | 6.2<br><sub>-,-,2,7,-</sub> | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.4 |
| Isaiah Evans | 52% | 5.7<br><sub>-,-,2,8,-</sub> | 5.8<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 7.2 |
| Johni Broome | 5% | 5.6 | 2.1 |  | 1.3 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.8 |

</details>


### GSW @ NOP
Out: Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.7–112.6 | GSW 69% | 1.44 / 3.26 | NOP +7.5 | 232.5 | NOP +3.5 covers 39%; o225.5 64% |
| Expected (weighted by chance each plays) | 120.4–113.8 | GSW 67% | 1.48 / 3.07 | NOP +6.5 | 234.5 | NOP +3.5 covers 41%; o225.5 69% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 19.4 | 8.6 | 3.9 | 2.2 | 0.8 | 0.8 | 0.4 | 1.3 | 14.7 | small |
| Jaron Pierre Jr. (NOP) | Questionable | 55% | 16.7 | 7.3 | 2.4 | 1.0 | 0.9 | 0.6 | 0.3 | 1.1 | 10.6 | small |
| Malik Dia (NOP) | Questionable | 55% | 8.1 | 2.8 | 0.3 | 1.1 | 0.3 | 0.4 | 0.2 | 0.4 | 4.2 | small |
| Julian Reese (NOP) | Questionable | 55% | 9.8 | 3.2 | 1.8 | 0.7 | 0.1 | 0.3 | 0.5 | 0.6 | 5.7 | small |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 96% | 33.9<br><sub>32,39,26,37,22</sub> | 20.8<br><sub>9,15,25,22,8</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>6,7,2,6,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,1,4,4,0</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>2,4,5,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.3 | 1.9 | 31.0 |
| Yaxel Lendeborg | 98% | 33.8<br><sub>30,37,27,36,24</sub> | 23.4<br><sub>17,23,23,25,3</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 7.7<br><sub>8,8,7,10,7</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>6,3,4,0,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>1,2,4,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.9 | 3.5 | 35.3 |
| Draymond Green | 96% | 28.7<br><sub>27,34,21,27,16</sub> | 6.8<br><sub>2,2,2,7,4</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>5,6,3,5,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 7.1<br><sub>11,13,6,7,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.1 | 0.8 | 2.7 | 19.7 |
| De'Anthony Melton | 98% | 25.8<br><sub>17,17,26,25,18</sub> | 14.7<br><sub>5,4,16,11,8</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>6,1,4,4,4</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 3.2<br><sub>2,1,3,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>0,1,4,3,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.6 | 0.5 | 1.8 | 22.0 |
| Will Richard | 98% | 25.4<br><sub>16,12,-,19,30</sub> | 8.0<br><sub>10,4,-,9,7</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>0,2,-,4,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>2,1,-,0,1</sub> |  | 1.0<br><sub>2,0,-,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.2 | 1.0 | 12.8 |
| Georges Niang | 98% | 22.2<br><sub>22,25,19,19,15</sub> | 9.7<br><sub>13,11,9,5,5</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>4,2,2,5,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>3,1,2,0,2</sub> |  | 1.6<br><sub>2,3,1,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5 | 0.2 | 1.1 | 14.7 |
| Al Horford | 98% | 19.4<br><sub>18,13,15,21,10</sub> | 7.3<br><sub>8,2,5,2,0</sub> |  | 4.3<br><sub>5,5,2,1,3</sub> |  | 2.4<br><sub>1,4,6,4,1</sub> |  | 1.0<br><sub>2,0,1,0,0</sub> |  | 0.6 | 0.9 | 0.7 | 14.0 |
| LJ Cryer | 76% | 18.6<br><sub>1,-,20,18,24</sub> | 9.7<br><sub>0,-,10,13,20</sub> |  | 1.6<br><sub>0,-,0,1,2</sub> |  | 2.0<br><sub>0,-,3,1,6</sub> |  | 1.7<br><sub>0,-,2,3,6</sub> |  | 0.5 | 0.1 | 0.9 | 13.2 |
| Gary Payton II | 83% | 17.5<br><sub>10,13,-,-,13</sub> | 8.6<br><sub>9,4,-,-,2</sub> |  | 3.2<br><sub>0,0,-,-,2</sub> |  | 1.4<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 1.1 | 0.2 | 0.8 | 13.2 |
| Charles Bassey | 98% | 17.2<br><sub>14,11,18,13,20</sub> | 8.9<br><sub>8,8,12,7,11</sub> |  | 7.3<br><sub>7,4,10,6,5</sub> |  | 0.9<br><sub>0,0,1,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.4 | 1.0 | 17.2 |
| Graham Ike | 91% | 13.2<br><sub>1,-,12,4,13</sub> | 5.7<br><sub>0,-,4,4,5</sub> |  | 3.2<br><sub>1,-,5,0,2</sub> |  | 1.3<br><sub>0,-,2,1,3</sub> |  | 0.4<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.5 | 0.7 | 10.2 |
| Malevy Leons | 64% | 12.3<br><sub>1,-,12,4,14</sub> | 3.9<br><sub>0,-,0,0,5</sub> |  | 2.4<br><sub>0,-,3,3,1</sub> |  | 0.8<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.6 | 0.5 | 0.6 | 7.0 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 35.3<br><sub>26,24,29,35,41</sub> | 19.6<br><sub>13,9,15,30,16</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>4,0,1,10,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.4<br><sub>3,4,2,0,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>1,1,3,6,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.2 | 1.7 | 28.7 |
| Zion Williamson | 98% | 35.0<br><sub>31,-,30,33,31</sub> | 23.6<br><sub>25,-,29,22,24</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>2,-,2,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.4<br><sub>0,-,1,0,2</sub> |  | 1.4 | 0.7 | 2.8 | 34.3 |
| Jeremiah Fears | 98% | 33.7<br><sub>29,29,28,34,33</sub> | 19.7<br><sub>25,11,14,18,13</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>6,3,4,5,4</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 6.0<br><sub>5,8,5,7,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>3,1,2,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.6 | 3.2 | 30.6 |
| Herbert Jones | 98% | 28.5<br><sub>20,24,25,32,27</sub> | 9.4<br><sub>4,10,2,8,10</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>0,6,2,2,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.5<br><sub>1,1,3,3,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,2,0,0,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.5 | 1.4 | 15.2 |
| Derik Queen | 98% | 27.5<br><sub>21,21,14,23,25</sub> | 14.3<br><sub>8,16,9,10,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>5,4,0,6,5</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 4.0<br><sub>3,0,0,2,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>0,0,1,0,2</sub> |  | 1.2 | 1.0 | 2.9 | 26.1 |
| Jordan Poole | 72% | 24.8<br><sub>-,34,21,21,24</sub> | 12.9<br><sub>-,7,14,13,14</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>-,3,0,2,2</sub> |  | 3.5<br><sub>-,2,1,5,5</sub> |  | 1.9<br><sub>-,1,2,1,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.5 | 1.9 | 18.9 |
| Yves Missi | 98% | 24.2<br><sub>-,-,-,-,22</sub> | 7.5<br><sub>-,-,-,-,3</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 7.8<br><sub>-,-,-,-,8</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 1.8 | 1.1 | 17.1 |
| Karlo Matkovic | 97% | 23.7<br><sub>19,17,22,19,14</sub> | 9.3<br><sub>3,4,4,1,5</sub> |  | 5.3<br><sub>3,6,4,3,3</sub> |  | 1.5<br><sub>2,2,1,0,1</sub> |  | 1.1<br><sub>1,0,0,0,1</sub> |  | 0.8 | 0.9 | 1.1 | 16.2 |
| DeAndre Jordan | 48% | 15.5<br><sub>-,-,11,17,-</sub> | 4.3<br><sub>-,-,0,6,-</sub> |  | 6.0<br><sub>-,-,3,8,-</sub> |  | 0.9<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.7 | 0.7 | 11.2 |
| AJ Johnson | 52% | 10.1<br><sub>3,12,7,4,-</sub> | 3.0<br><sub>2,2,2,1,-</sub> |  | 1.5<br><sub>0,2,1,0,-</sub> |  | 1.0<br><sub>0,3,0,0,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 5.5 |

</details>


### PHX @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN), Mark Williams (PHX)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.7–118.0 | PHX 33% | 3.07 / 1.48 | DEN -6.5 | 229.5 | DEN -10.5 covers 38%; o227.5 55% |
| Expected (weighted by chance each plays) | 111.7–118.0 | PHX 33% | 3.07 / 1.48 | DEN -6.5 | 229.5 | DEN -10.5 covers 38%; o227.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Drew Timme (PHX) | Day-To-Day | 70% | 6.5 | 2.6 | 1.1 | 0.7 | 0.2 | 0.2 | 0.1 | 0.3 | 4.4 | small |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.5<br><sub>34,39,29,29,35</sub> | 23.6<br><sub>30,24,32,17,30</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>1,2,2,3,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 5.9<br><sub>8,3,4,5,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>4,2,3,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.3 | 2.6 | 32.9 |
| Dillon Brooks | 98% | 30.3<br><sub>29,37,26,22,30</sub> | 16.8<br><sub>24,11,7,8,15</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,4,4,4,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>4,3,1,0,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 1.3 | 22.5 |
| Miles Bridges | 98% | 28.1<br><sub>31,31,26,18,25</sub> | 13.8<br><sub>18,13,7,8,11</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>13,10,5,4,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>5,7,0,2,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>3,1,0,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.4 | 1.1 | 22.5 |
| Jalen Green | 98% | 26.4<br><sub>24,34,24,21,21</sub> | 13.3<br><sub>6,16,6,13,12</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>0,3,5,5,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>3,6,4,1,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,0,0,3,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.3 | 1.9 | 19.6 |
| Oso Ighodaro | 98% | 24.3<br><sub>24,23,18,20,32</sub> | 6.9<br><sub>2,4,7,6,2</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>5,6,4,8,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>1,3,2,2,7</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.7 | 1.2 | 15.8 |
| Collin Gillespie | 98% | 23.9<br><sub>24,20,24,22,27</sub> | 8.9<br><sub>6,7,6,12,13</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>2,3,2,2,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>2,4,3,8,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 1.0 | 15.5 |
| Luke Kennard | 98% | 18.4<br><sub>21,14,14,22,21</sub> | 7.2<br><sub>12,11,3,14,8</sub> |  | 1.9<br><sub>1,1,1,1,1</sub> |  | 1.8<br><sub>5,2,0,3,1</sub> |  | 0.9<br><sub>3,3,1,3,0</sub> |  | 0.6 | 0.1 | 0.6 | 11.0 |
| Jordan Goodwin | 98% | 18.1<br><sub>-,-,-,14,24</sub> | 7.0<br><sub>-,-,-,18,6</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>-,-,-,3,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>-,-,-,1,2</sub> |  | 1.1<br><sub>-,-,-,6,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 0.7 | 12.2 |
| Khaman Maluach | 98% | 16.6<br><sub>22,18,20,22,16</sub> | 5.7<br><sub>8,8,11,11,4</sub> |  | 5.0<br><sub>6,10,5,7,2</sub> |  | 0.8<br><sub>2,0,2,3,1</sub> |  | 0.2<br><sub>0,0,1,0,0</sub> |  | 0.3 | 0.9 | 0.9 | 11.4 |
| Ryan Dunn | 98% | 15.2<br><sub>25,23,23,25,10</sub> | 4.5<br><sub>11,8,3,10,0</sub> |  | 3.2<br><sub>3,5,2,8,4</sub> |  | 1.1<br><sub>3,3,0,2,0</sub> |  | 0.5<br><sub>1,2,1,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 8.8 |
| Rasheer Fleming | 52% | 8.3<br><sub>-,-,9,12,-</sub> | 3.1<br><sub>-,-,2,4,-</sub> |  | 1.4<br><sub>-,-,1,2,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,1,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Pat Spencer | 67% | 7.3<br><sub>2,-,6,-,-</sub> | 2.7<br><sub>0,-,2,-,-</sub> |  | 1.0<br><sub>0,-,2,-,-</sub> |  | 1.3<br><sub>0,-,2,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.0 |
| Jamaree Bouyea | 58% | 7.0<br><sub>2,-,9,8,-</sub> | 2.8<br><sub>0,-,4,7,-</sub> |  | 0.9<br><sub>0,-,0,1,-</sub> |  | 1.2<br><sub>0,-,3,3,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.0 |
| Koa Peat | 58% | 6.5<br><sub>2,-,6,6,-</sub> | 2.8<br><sub>0,-,4,5,-</sub> |  | 1.4<br><sub>1,-,0,1,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.5 |
| Duop Reath | 58% | 6.5<br><sub>2,-,6,-,-</sub> | 2.7<br><sub>0,-,2,-,-</sub> |  | 1.3<br><sub>0,-,2,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.4 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 36.9<br><sub>30,36,39,37,37</sub> | 26.9<br><sub>32,19,25,27,26</sub> | 26.5 · –<br><sub>o 49% · u 51%</sub> | 12.8<br><sub>10,13,16,11,8</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 10.8<br><sub>11,8,9,8,10</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.9 | 3.8 | 50.6 |
| Jamal Murray | 98% | 36.8<br><sub>28,34,39,32,38</sub> | 25.2<br><sub>14,16,38,30,23</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>5,6,2,4,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>7,8,2,8,9</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>2,2,5,4,0</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.6 | 2.6 | 36.8 |
| Christian Braun | 98% | 32.8<br><sub>28,29,32,37,28</sub> | 12.4<br><sub>11,6,4,12,17</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>3,4,5,5,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.4 | 1.1 | 19.4 |
| Cameron Johnson | 98% | 30.3<br><sub>30,29,31,30,31</sub> | 12.8<br><sub>12,18,8,23,12</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.1<br><sub>2,4,2,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>2,1,1,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.8<br><sub>4,2,2,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.3 | 1.1 | 19.4 |
| Aaron Gordon | 98% | 30.1<br><sub>25,27,30,27,33</sub> | 13.3<br><sub>17,12,3,9,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>1,5,5,3,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>0,0,2,2,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.4 | 1.4 | 21.6 |
| DeMar DeRozan | 88% | 22.8<br><sub>-,22,19,20,24</sub> | 11.7<br><sub>-,11,7,8,9</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>-,1,4,1,3</sub> |  | 3.1<br><sub>-,5,2,4,2</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.3 | 1.2 | 17.1 |
| Trevon Brazile | 98% | 16.1<br><sub>23,14,14,13,16</sub> | 5.1<br><sub>6,3,5,7,5</sub> |  | 3.9<br><sub>7,4,2,5,3</sub> |  | 0.7<br><sub>1,2,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 9.7 |
| Spencer Jones | 80% | 13.9<br><sub>-,21,14,22,12</sub> | 3.7<br><sub>-,13,0,3,4</sub> |  | 2.1<br><sub>-,6,0,1,2</sub> |  | 0.7<br><sub>-,0,1,0,1</sub> |  | 0.4<br><sub>-,3,0,1,0</sub> |  | 0.4 | 0.4 | 0.5 | 6.5 |
| Marvin Bagley III | 98% | 13.5<br><sub>14,12,12,12,13</sub> | 6.6<br><sub>10,10,6,4,7</sub> |  | 4.2<br><sub>2,3,3,2,7</sub> |  | 0.7<br><sub>2,0,0,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 11.5 |
| Tyus Jones | 97% | 9.7<br><sub>18,13,6,11,10</sub> | 2.5<br><sub>6,3,2,0,2</sub> |  | 0.9<br><sub>1,4,0,1,0</sub> |  | 1.7<br><sub>8,4,0,4,3</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.2 |
| Bryce Hopkins | 52% | 8.4<br><sub>28,3,3,-,-</sub> | 2.9<br><sub>18,3,2,-,-</sub> |  | 1.3<br><sub>4,1,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.1<br><sub>1,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Zeke Nnaji | 30% | 6.7<br><sub>4,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.0 |
| Alpha Diallo | 52% | 6.2<br><sub>4,-,1,-,-</sub> | 2.5<br><sub>0,-,0,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-16/`._
