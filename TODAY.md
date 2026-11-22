# NBA model · Sat 21 Nov 2026 (US date)

Updated **Sun 22 Nov, 01:25 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-21/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Neemias Queta REB over 15.5 (16+) | BOS @ SAC | draftkings | 20.40 | 19.19 | 11.56 | 8.6% | 4.6% | 5.2% | +6.2% | +76.4% | 0.1% |
| Neemias Queta REB over 13.5 (14+) | BOS @ SAC | draftkings | 10.10 | 9.58 | 5.91 | 16.9% | 9.2% | 10.4% | +5.4% | +71.0% | 0.1% |
| Darius Acuff Jr. AST over 11.5 (12+) | BOS @ SAC | draftkings | 17.40 | 16.56 | 10.30 | 9.7% | 5.4% | 6.0% | +5.1% | +68.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PTS over 4.5 (5+) | BOS @ SAC | tab | 1.90 | 1.77 | 1.29 | 77.4% | 52.8% | 56.6% | +7.6% | +47.1% | 2.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| BOS @ SAC | Sun 22 Nov 14:00 | 115.1–105.0 | BOS 76% | 1.32 / 4.11 | SAC +10.5 | 220.5 | SAC +12.5 covers 57%; o217.5 55% |

### BOS @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Mitchell Robinson (BOS), Jayson Tatum (BOS), Derrick White (BOS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George PTS under 24.5 | BOS @ SAC | betright | 1.96 | 1.92 | 1.57 | 63.6% | 50.1% | 52.2% | +2.4% | +24.7% | 0.6% |
| Payton Pritchard PTS under 21.5 | BOS @ SAC | unibet | 1.88 | 1.88 | 1.53 | 65.2% | 51.1% | 53.3% | +0.1% | +22.3% | 0.0% |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul George | 98% | 31.9<br><sub>30,-,25,36,23</sub> | 22.5<br><sub>36,-,7,22,10</sub> | 24.5 · 24.5<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,-,7,8,4</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>1,-,6,3,1</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 3.1<br><sub>6,-,1,5,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8 | 0.3 | 2.5 | 32.3 |
| Payton Pritchard | 99% | 31.0<br><sub>30,31,19,32,30</sub> | 19.3<br><sub>18,14,10,21,15</sub> | 21.5 · 21.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>6,1,1,4,1</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>5,1,6,5,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.1 | 1.6 | 28.4 |
| Neemias Queta | 98% | 27.1<br><sub>22,31,15,-,27</sub> | 12.9<br><sub>4,11,8,-,17</sub> | 12.5 · 11.5<br><sub>o 48% · u 52%</sub> | 9.8<br><sub>6,13,6,-,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>3,3,2,-,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.2<br><sub>0,1,1,-,0</sub> |  | 0.8 | 1.2 | 1.4 | 25.1 |
| Sam Hauser | 99% | 26.6<br><sub>18,24,11,25,17</sub> | 11.2<br><sub>12,8,8,12,9</sub> | 11.5 · 12.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>5,9,1,1,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>2,0,0,2,2</sub> |  | 2.3<br><sub>4,2,2,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.2 | 0.5 | 16.8 |
| Baylor Scheierman | 99% | 24.3<br><sub>18,29,18,11,13</sub> | 8.3<br><sub>5,9,12,0,0</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>3,7,5,1,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>2,3,3,1,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,3,2,0,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.1 | 0.8 | 15.0 |
| Jordan Walsh | 98% | 22.0<br><sub>19,18,21,17,4</sub> | 7.3<br><sub>8,6,11,6,0</sub> | – · 6.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>2,3,1,2,0</sub> |  | 1.2<br><sub>2,0,0,0,0</sub> |  | 0.9<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.3 | 0.7 | 12.5 |
| Hugo Gonzalez | 98% | 21.7<br><sub>19,8,18,4,16</sub> | 7.3<br><sub>10,0,9,0,2</sub> |  | 4.3<br><sub>2,1,5,2,6</sub> |  | 1.2<br><sub>2,0,2,0,0</sub> |  | 0.8<br><sub>2,0,2,0,0</sub> |  | 0.9 | 0.4 | 0.8 | 12.8 |
| Devin Carter | 91% | 19.9<br><sub>-,-,12,-,-</sub> | 9.4<br><sub>-,-,0,-,-</sub> |  | 3.6<br><sub>-,-,2,-,-</sub> |  | 2.9<br><sub>-,-,1,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.0 | 0.2 | 1.3 | 16.0 |
| Chris Cenac Jr. | 63% | 18.9<br><sub>-,-,7,12,17</sub> | 7.5<br><sub>-,-,6,4,6</sub> |  | 4.7<br><sub>-,-,3,2,6</sub> |  | 0.9<br><sub>-,-,0,1,0</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.8 | 0.3 | 0.9 | 13.2 |
| Luka Garza | 98% | 18.0<br><sub>9,11,14,18,5</sub> | 8.8<br><sub>2,5,2,3,0</sub> |  | 4.3<br><sub>0,1,3,0,1</sub> |  | 2.0<br><sub>2,0,5,4,1</sub> |  | 0.9<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.5 | 0.8 | 15.2 |
| Mike Conley | 35% | 14.7<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.2 | 0.6 | 8.0 |
| Ron Harper Jr. | 52% | 14.4<br><sub>4,-,12,-,-</sub> | 6.0<br><sub>0,-,10,-,-</sub> |  | 2.1<br><sub>1,-,1,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.9<br><sub>0,-,2,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 9.1 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 35.1<br><sub>40,35,33,35,36</sub> | 22.0<br><sub>29,17,26,36,18</sub> | 21.5 · 22.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>4,4,0,4,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 7.3<br><sub>6,6,6,6,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,3,3,6,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 3.7 | 32.5 |
| Zach LaVine | 88% | 31.9<br><sub>33,36,-,32,39</sub> | 16.6<br><sub>31,12,-,18,19</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,3,-,5,7</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.8<br><sub>2,6,-,2,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>6,3,-,2,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.2 | 2.0 | 22.6 |
| De'Andre Hunter | 88% | 31.6<br><sub>34,42,-,35,37</sub> | 13.3<br><sub>15,24,-,7,30</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>4,5,-,1,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,2,-,4,2</sub> |  | 1.9<br><sub>3,2,-,1,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.2 | 1.6 | 19.5 |
| Domantas Sabonis | 98% | 30.7<br><sub>24,35,29,24,38</sub> | 13.0<br><sub>0,21,11,8,19</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 11.6<br><sub>2,12,13,13,16</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>5,5,3,8,1</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 2.3 | 29.5 |
| Keegan Murray | 98% | 29.8<br><sub>24,40,21,31,40</sub> | 11.7<br><sub>11,16,6,12,13</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,7,1,7,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,4,0,3,4</sub> |  | 1.5<br><sub>2,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.8 | 1.0 | 18.0 |
| Precious Achiuwa | 98% | 20.4<br><sub>14,-,-,8,-</sub> | 8.1<br><sub>10,-,-,0,-</sub> | 5.5 · 4.5<br><sub>o 57% · u 43%</sub> | 5.4<br><sub>3,-,-,0,-</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>0,-,-,0,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.6 | 0.6 | 1.0 | 14.6 |
| Leaky Black | 88% | 18.2<br><sub>18,12,29,17,19</sub> | 4.3<br><sub>0,0,12,3,0</sub> |  | 3.0<br><sub>3,0,9,0,3</sub> |  | 1.2<br><sub>2,0,2,2,1</sub> |  | 0.6<br><sub>0,0,4,1,0</sub> |  | 0.8 | 0.4 | 0.5 | 8.5 |
| Malik Monk | 98% | 15.9<br><sub>3,18,29,20,12</sub> | 7.9<br><sub>1,7,14,8,2</sub> |  | 1.4<br><sub>0,4,1,1,0</sub> |  | 2.9<br><sub>0,3,10,2,3</sub> |  | 1.0<br><sub>0,0,1,2,0</sub> |  | 0.4 | 0.2 | 1.2 | 12.3 |
| Dylan Cardwell | 98% | 13.7<br><sub>29,13,19,12,10</sub> | 3.9<br><sub>1,6,10,6,0</sub> |  | 4.5<br><sub>11,3,6,4,4</sub> |  | 1.0<br><sub>1,3,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.6 | 9.4 |
| Emanuel Sharp | 98% | 13.3<br><sub>19,7,21,14,10</sub> | 4.5<br><sub>2,4,9,6,3</sub> |  | 1.1<br><sub>2,0,0,2,0</sub> |  | 0.6<br><sub>0,0,2,1,1</sub> |  | 0.5<br><sub>0,0,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.1 |
| Daeqwon Plowden | 67% | 8.1<br><sub>2,2,24,4,-</sub> | 2.9<br><sub>0,0,13,3,-</sub> |  | 0.9<br><sub>0,0,2,0,-</sub> |  | 0.4<br><sub>0,0,1,0,-</sub> |  | 0.3<br><sub>0,0,3,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Alex Karaban | 52% | 8.0<br><sub>-,-,29,4,-</sub> | 1.6<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,5,1,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.1 |
| Mason Plumlee | 52% | 6.2<br><sub>-,-,5,4,-</sub> | 1.7<br><sub>-,-,2,0,-</sub> |  | 1.9<br><sub>-,-,0,2,-</sub> |  | 0.6<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-21/`._
