# NBA model · Thu 12 Nov 2026 (US date)

Updated **Fri 13 Nov, 12:53 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-12/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Kalkbrenner PR over 19.5 (20+) | CHA @ PHX | draftkings | 14.00 | 12.25 | 5.57 | 17.9% | 6.7% | 8.2% | +14.3% | +151.3% | 0.3% |
| Ryan Kalkbrenner REB over 9.5 (10+) | CHA @ PHX | draftkings | 10.90 | 10.10 | 5.37 | 18.6% | 8.6% | 9.9% | +7.9% | +102.9% | 0.2% |
| Coby White PTS over 29.5 (30+) | CHA @ PHX | draftkings | 20.40 | 19.08 | 10.47 | 9.6% | 4.6% | 5.2% | +6.8% | +94.8% | 0.1% |
| Ryan Kalkbrenner REB over 11.5 (12+) | CHA @ PHX | draftkings | 24.00 | 22.62 | 12.70 | 7.9% | 3.9% | 4.4% | +6.1% | +89.0% | 0.1% |
| Coby White PTS over 24.5 (25+) | CHA @ PHX | draftkings | 9.20 | 8.70 | 4.95 | 20.2% | 10.2% | 11.5% | +5.7% | +85.9% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CHA @ PHX | Fri 13 Nov 13:00 | 108.9–111.2 | CHA 43% | 2.30 / 1.77 | PHX -2.5 | 219.5 | PHX -6.5 covers 38%; o214.5 61% |

### CHA @ PHX
Out: Pat Spencer (PHX), Drew Timme (PHX), Mark Williams (PHX), Kon Knueppel (CHA), Brandon Miller (CHA), Dennis Schroder (CHA), Hannes Steinbach (CHA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Oso Ighodaro PTS over 6.5 (7+) | CHA @ PHX | draftkings | 2.17 | 2.14 | 1.99 | 50.1% | 46.1% | 46.7% | +1.3% | +8.8% | 0.3% |
| Jalen Green PTS under 13.5 | CHA @ PHX | pointsbetau | 2.05 | 2.03 | 2.05 | 48.8% | 49.3% | 49.2% | +0.9% | -0.0% | 0.2% |
| Devin Booker PTS under 24.5 | CHA @ PHX | pointsbetau | 2.00 | 1.99 | 1.74 | 57.3% | 49.2% | 50.2% | +0.5% | +14.6% | 0.1% |
| Grayson Allen PTS under 17.5 | CHA @ PHX | pointsbetau | 2.00 | 1.99 | 1.79 | 55.8% | 49.3% | 50.1% | +0.3% | +11.6% | 0.1% |

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 100% | 31.6<br><sub>36,27,36,26,32</sub> | 20.0<br><sub>14,13,28,14,25</sub> | 20.5 · 20.5<br><sub>o 51% · u 49%</sub> | 8.0<br><sub>5,6,9,6,13</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,2,2,2,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>0,2,2,2,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.8 | 2.8 | 30.7 |
| Grayson Allen | 100% | 31.1<br><sub>30,19,27,22,34</sub> | 17.4<br><sub>27,11,22,0,27</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>4,1,2,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>3,0,4,3,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>7,3,5,0,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.3 | 2.2 | 24.8 |
| Sion James | 100% | 29.7<br><sub>18,21,31,21,33</sub> | 8.5<br><sub>4,11,10,11,11</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,4,2,3,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>1,3,1,0,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,3,0,3,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 1.3 | 15.9 |
| Moussa Diabate | 100% | 29.1<br><sub>28,24,29,-,-</sub> | 8.9<br><sub>10,7,7,-,-</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 9.4<br><sub>8,9,6,-,-</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,2,2,-,-</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.0<br><sub>0,0,0,-,-</sub> |  | 1.1 | 1.0 | 1.7 | 20.9 |
| Coby White | 100% | 25.6<br><sub>-,16,18,16,20</sub> | 18.1<br><sub>-,7,4,7,10</sub> | 14.5 · 14.5<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>-,0,5,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>-,3,2,1,9</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>-,1,0,1,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.2 | 2.8 | 26.1 |
| Ryan Kalkbrenner | 98% | 24.9<br><sub>19,16,19,21,35</sub> | 7.7<br><sub>6,4,6,4,8</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>3,6,4,5,15</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>4,0,2,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.5 | 1.4 | 15.9 |
| Royce O'Neale | 98% | 23.8<br><sub>23,18,18,26,23</sub> | 7.3<br><sub>8,2,0,7,10</sub> | 7.5 · 6.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,4,3,4,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>1,0,2,2,1</sub> |  | 1.3<br><sub>1,0,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.4 | 0.9 | 13.1 |
| Tidjane Salaun | 96% | 18.7<br><sub>12,19,10,23,18</sub> | 7.2<br><sub>5,1,9,13,14</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>2,7,1,4,3</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>1,0,3,2,3</sub> |  | 0.6 | 0.2 | 0.9 | 12.2 |
| Grant Williams | 58% | 18.2<br><sub>-,-,-,-,-</sub> | 6.6<br><sub>-,-,-,-,-</sub> |  | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.5 | 1.1 | 11.4 |
| Christian Anderson | 86% | 16.9<br><sub>8,9,-,25,16</sub> | 6.6<br><sub>2,8,-,4,9</sub> |  | 2.2<br><sub>0,2,-,3,1</sub> |  | 2.2<br><sub>0,2,-,5,1</sub> |  | 0.9<br><sub>0,1,-,0,3</sub> |  | 0.5 | 0.3 | 1.9 | 11.0 |
| Liam McNeeley | 64% | 16.3<br><sub>-,9,-,19,16</sub> | 6.8<br><sub>-,3,-,8,8</sub> |  | 3.0<br><sub>-,0,-,2,1</sub> |  | 1.2<br><sub>-,1,-,3,1</sub> |  | 0.8<br><sub>-,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.9 | 11.0 |
| PJ Hall | 38% | 9.1<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.7 | 7.1 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 100% | 34.0<br><sub>34,34,39,29,29</sub> | 24.1<br><sub>33,30,24,32,17</sub> | 25.5 · 24.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>1,1,2,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.8<br><sub>2,8,3,4,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>2,4,2,3,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 2.8 | 33.4 |
| Dillon Brooks | 100% | 30.0<br><sub>35,29,37,26,22</sub> | 15.9<br><sub>15,24,11,7,8</sub> | 15.5 · 14.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>6,1,4,4,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>2,1,1,0,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>0,4,3,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 1.4 | 21.4 |
| Miles Bridges | 100% | 29.1<br><sub>31,31,31,26,18</sub> | 13.7<br><sub>18,18,13,7,8</sub> | 15.5 · 15.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>7,13,10,5,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>5,5,7,0,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>4,3,1,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.5 | 1.1 | 22.4 |
| Jalen Green | 100% | 28.1<br><sub>32,24,34,24,21</sub> | 14.6<br><sub>22,6,16,6,13</sub> | 13.5 · 13.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>2,0,3,5,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>2,3,6,4,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.7<br><sub>2,0,0,0,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.3 | 2.2 | 21.6 |
| Oso Ighodaro | 100% | 23.7<br><sub>23,24,23,18,20</sub> | 7.1<br><sub>9,2,4,7,6</sub> | 6.5 · 5.5<br><sub>o 54% · u 46%</sub> | 5.5<br><sub>7,5,6,4,8</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>7,1,3,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.7 | 1.3 | 15.4 |
| Collin Gillespie | 98% | 23.1<br><sub>23,24,20,24,22</sub> | 8.5<br><sub>2,6,7,6,12</sub> | 7.5 · 7.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>3,2,3,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.7<br><sub>2,2,4,3,8</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 1.0 | 15.1 |
| Ryan Dunn | 98% | 19.1<br><sub>18,25,23,23,25</sub> | 5.6<br><sub>2,11,8,3,10</sub> |  | 3.8<br><sub>6,3,5,2,8</sub> |  | 1.3<br><sub>2,3,3,0,2</sub> |  | 0.6<br><sub>0,1,2,1,1</sub> |  | 0.8 | 0.4 | 0.6 | 10.7 |
| Khaman Maluach | 98% | 18.0<br><sub>16,22,18,20,22</sub> | 6.1<br><sub>6,8,8,11,11</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>6,6,10,5,7</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 0.8<br><sub>2,2,0,2,3</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.9 | 1.0 | 12.1 |
| Luke Kennard | 98% | 17.9<br><sub>14,21,14,14,22</sub> | 6.8<br><sub>0,12,11,3,14</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>0,1,1,1,1</sub> |  | 1.8<br><sub>1,5,2,0,3</sub> |  | 0.9<br><sub>0,3,3,1,3</sub> |  | 0.6 | 0.1 | 0.6 | 10.5 |
| Jordan Goodwin | 98% | 16.4<br><sub>-,-,-,-,14</sub> | 6.5<br><sub>-,-,-,-,18</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>-,-,-,-,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>-,-,-,-,1</sub> |  | 1.0<br><sub>-,-,-,-,6</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.1 | 0.6 | 11.3 |
| Rasheer Fleming | 58% | 9.4<br><sub>-,-,-,9,12</sub> | 3.5<br><sub>-,-,-,2,4</sub> |  | 1.5<br><sub>-,-,-,1,2</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.4 | 5.3 |
| Jamaree Bouyea | 67% | 7.6<br><sub>3,2,-,9,8</sub> | 2.9<br><sub>3,0,-,4,7</sub> |  | 0.9<br><sub>0,0,-,0,1</sub> |  | 1.3<br><sub>0,0,-,3,3</sub> |  | 0.2<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.1 |
| Koa Peat | 66% | 6.9<br><sub>3,2,-,6,6</sub> | 2.7<br><sub>2,0,-,4,5</sub> |  | 1.3<br><sub>1,1,-,0,1</sub> |  | 0.3<br><sub>0,0,-,1,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 4.3 |
| Duop Reath | 67% | 6.2<br><sub>7,2,-,6,-</sub> | 2.6<br><sub>7,0,-,2,-</sub> |  | 1.1<br><sub>0,0,-,2,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>1,0,-,0,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.1 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-12/`._
