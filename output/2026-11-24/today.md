# NBA model · Tue 24 Nov 2026 (US date)

Updated **Wed 25 Nov, 01:51 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-24/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zaccharie Risacher PTS over 7.5 (8+) | DAL @ DEN | pointsbetau | 2.00 | 1.88 | 1.62 | 61.8% | 51.3% | 53.2% | +6.4% | +23.6% | 1.6% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic AST over 15.5 (16+) | DAL @ DEN | draftkings | 13.80 | 12.38 | 7.15 | 14.0% | 6.8% | 8.1% | +11.5% | +93.1% | 0.2% |
| Nikola Jokic AST over 17.5 (18+) | DAL @ DEN | draftkings | 27.00 | 24.75 | 15.07 | 6.6% | 3.5% | 4.0% | +9.0% | +79.1% | 0.1% |
| Nikola Jokic PRA over 69.5 (70+) | DAL @ DEN | draftkings | 20.00 | 18.62 | 11.74 | 8.5% | 4.7% | 5.4% | +7.4% | +70.3% | 0.1% |
| Nikola Jokic PRA over 64.5 (65+) | DAL @ DEN | draftkings | 11.60 | 10.89 | 7.02 | 14.2% | 8.1% | 9.2% | +6.5% | +65.2% | 0.1% |
| Nikola Jokic AST over 13.5 (14+) | DAL @ DEN | draftkings | 6.10 | 5.80 | 3.85 | 26.0% | 15.3% | 17.2% | +5.2% | +58.5% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DAL @ DEN | Wed 25 Nov 14:00 | 113.7–121.3 | DAL 30% | 3.34 / 1.43 | DEN -7.5 | 234.5 | DEN -7.5 covers 50%; o234.5 51% |

### DAL @ DEN
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zaccharie Risacher PTS over 7.5 (8+) | DAL @ DEN | pointsbetau | 2.00 | 1.88 | 1.62 | 61.8% | 51.3% | 53.2% | +6.4% | +23.6% | 1.6% |
| Cooper Flagg PTS under 23.5 | DAL @ DEN | sportsbet | 1.96 | 1.95 | 1.58 | 63.4% | 48.7% | 51.4% | +0.8% | +24.3% | 0.2% |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 100% | 32.6<br><sub>38,27,34,36,31</sub> | 21.6<br><sub>18,17,33,22,28</sub> | 23.5 · 23.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>8,3,5,6,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>5,4,9,8,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,2,3,3,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.7 | 2.6 | 33.2 |
| Kyrie Irving | 100% | 31.8<br><sub>37,-,29,35,27</sub> | 18.8<br><sub>34,-,17,25,16</sub> | 22.5 · 22.5<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>6,-,6,6,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>5,-,5,4,8</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>7,-,1,3,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 1.7 | 27.0 |
| P.J. Washington | 98% | 27.9<br><sub>26,25,25,-,-</sub> | 12.4<br><sub>10,8,21,-,-</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>4,5,5,-,-</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>1,4,2,-,-</sub> |  | 1.6<br><sub>2,0,5,-,-</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.7 | 1.2 | 19.8 |
| Zaccharie Risacher | 100% | 25.0<br><sub>14,27,18,29,28</sub> | 9.6<br><sub>5,18,3,11,15</sub> | 7.5 · 6.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>2,5,3,7,8</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>0,0,0,1,2</sub> |  | 1.1<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.7 | 1.0 | 15.9 |
| Naji Marshall | 96% | 22.8<br><sub>30,23,27,14,25</sub> | 10.5<br><sub>12,13,12,4,6</sub> | 10.5 · 9.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>3,2,5,3,0</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.8<br><sub>5,2,2,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.8<br><sub>0,3,2,0,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.1 | 1.3 | 16.5 |
| Daniel Gafford | 100% | 22.8<br><sub>17,19,24,31,28</sub> | 9.4<br><sub>10,3,6,10,10</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>3,4,6,10,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>1,2,2,3,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.0<br><sub>1,0,0,0,0</sub> |  | 0.7 | 1.2 | 1.0 | 17.3 |
| Caleb Martin | 100% | 22.1<br><sub>33,34,20,20,29</sub> | 5.9<br><sub>15,12,8,0,13</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>8,5,5,4,6</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>3,5,3,3,4</sub> |  | 0.7<br><sub>1,4,2,0,3</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.3 | 0.7 | 11.5 |
| Walter Clayton Jr. | 96% | 18.6<br><sub>13,23,27,25,21</sub> | 6.9<br><sub>2,13,8,16,9</sub> |  | 2.6<br><sub>2,4,2,5,0</sub> |  | 3.1<br><sub>2,3,7,1,3</sub> |  | 0.9<br><sub>0,3,2,2,2</sub> |  | 0.5 | 0.1 | 1.3 | 12.6 |
| Max Christie | 98% | 15.7<br><sub>-,-,8,24,16</sub> | 5.8<br><sub>-,-,5,13,3</sub> |  | 1.9<br><sub>-,-,1,4,2</sub> |  | 0.9<br><sub>-,-,2,0,0</sub> |  | 0.8<br><sub>-,-,1,3,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.6 |
| Morez Johnson Jr. | 99% | 15.5<br><sub>15,26,15,17,20</sub> | 5.9<br><sub>4,2,3,9,7</sub> | 5.5 · 5.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>2,6,1,7,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,4,1,2,2</sub> |  | 0.3<br><sub>0,0,0,1,1</sub> |  | 0.4 | 0.1 | 0.8 | 10.4 |
| Santi Aldama | 98% | 13.3<br><sub>16,-,6,9,16</sub> | 6.3<br><sub>7,-,0,0,9</sub> |  | 2.9<br><sub>2,-,0,1,4</sub> |  | 1.1<br><sub>1,-,0,0,1</sub> |  | 0.7<br><sub>2,-,0,0,1</sub> |  | 0.4 | 0.3 | 0.6 | 10.3 |
| Marcus Sasser | 52% | 8.0<br><sub>-,18,4,-,-</sub> | 2.8<br><sub>-,5,0,-,-</sub> |  | 0.7<br><sub>-,1,2,-,-</sub> |  | 1.1<br><sub>-,2,1,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Moussa Cisse | 52% | 6.4<br><sub>-,4,4,-,-</sub> | 2.2<br><sub>-,1,0,-,-</sub> |  | 2.2<br><sub>-,1,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.4 | 0.3 | 4.7 |
| Jett Howard | 52% | 5.9<br><sub>-,7,-,-,-</sub> | 2.9<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.0 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 100% | 35.8<br><sub>37,38,39,38,42</sub> | 26.4<br><sub>26,28,24,26,37</sub> | 25.5 · 25.5<br><sub>o 50% · u 50%</sub> | 12.7<br><sub>8,15,8,7,18</sub> | 11.5<br><sub>o 55% · u 45%</sub> | 11.1<br><sub>10,7,9,11,11</sub> | 9.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,2,3,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.9 | 3.4 | 50.2 |
| Jamal Murray | 100% | 35.6<br><sub>38,35,38,36,45</sub> | 24.6<br><sub>23,28,21,14,45</sub> | 23.5 · 22.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>7,4,7,2,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>9,4,2,7,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>0,1,2,1,6</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.6 | 2.4 | 36.2 |
| Christian Braun | 100% | 31.2<br><sub>28,33,35,31,38</sub> | 13.1<br><sub>17,10,15,19,21</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>7,3,5,5,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>1,3,3,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>1,2,1,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.4 | 1.0 | 20.4 |
| Cameron Johnson | 100% | 28.4<br><sub>31,27,26,29,36</sub> | 13.2<br><sub>12,9,8,19,16</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,0,5,3,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>2,1,1,6,5</sub> |  | 1.7<br><sub>1,0,0,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.3 | 1.0 | 19.6 |
| Aaron Gordon | 100% | 27.7<br><sub>33,24,31,31,33</sub> | 13.2<br><sub>11,11,13,18,18</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>5,1,8,3,8</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>1,1,2,2,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>1,2,0,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.4 | 1.2 | 21.1 |
| DeMar DeRozan | 93% | 19.3<br><sub>24,14,25,22,18</sub> | 10.0<br><sub>9,2,18,15,4</sub> | 10.5 · 10.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,1,2,2,0</sub> |  | 2.8<br><sub>2,1,2,2,1</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.2 | 1.0 | 14.8 |
| Spencer Jones | 91% | 15.5<br><sub>12,21,17,18,20</sub> | 4.1<br><sub>4,4,2,3,0</sub> |  | 2.6<br><sub>2,3,2,1,4</sub> |  | 0.8<br><sub>1,3,0,1,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.4 | 0.6 | 7.5 |
| Trevon Brazile | 98% | 13.4<br><sub>16,23,11,11,15</sub> | 4.9<br><sub>5,9,0,4,8</sub> |  | 3.5<br><sub>3,4,6,4,0</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,1,0,0,2</sub> |  | 0.4 | 0.4 | 0.6 | 8.9 |
| Marvin Bagley III | 98% | 11.1<br><sub>13,10,9,10,11</sub> | 5.9<br><sub>7,4,4,10,2</sub> |  | 3.7<br><sub>7,2,3,6,2</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.2<br><sub>0,0,0,2,0</sub> |  | 0.3 | 0.5 | 0.6 | 10.2 |
| Tyus Jones | 98% | 8.9<br><sub>10,10,9,14,8</sub> | 2.4<br><sub>2,0,0,5,0</sub> |  | 0.8<br><sub>0,1,0,3,0</sub> |  | 1.8<br><sub>3,2,0,4,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |
| Julian Strawther | 52% | 7.5<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| Bryce Hopkins | 52% | 6.7<br><sub>-,4,-,-,-</sub> | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Cam Whitmore | 58% | 6.7<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.2 |
| Zeke Nnaji | 16% | 6.1<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.0 |
| Ryan Nembhard | 38% | 6.0<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Alpha Diallo | 35% | 5.8<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.6 |
| DaRon Holmes II | 52% | 5.6<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-24/`._
