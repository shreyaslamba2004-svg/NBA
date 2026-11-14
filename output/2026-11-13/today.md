# NBA model · Fri 13 Nov 2026 (US date)

Updated **Sat 14 Nov, 12:51 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-13/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scoot Henderson AST over 5.5 (6+) | POR @ SAC | draftkings | 15.80 | 14.68 | 7.89 | 12.7% | 5.9% | 6.8% | +7.5% | +100.2% | 0.1% |
| GSW to win | GSW @ SAS | sportsbet | 6.15 | 5.74 | 3.45 | 29.0% | 17.4% | 17.4% | +7.1% | +78.5% | 0.4% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| GSW @ SAS | Sat 14 Nov 13:30 | 109.5–117.2 | GSW 29% | 3.45 / 1.41 | SAS -7.5 | 226.5 | SAS -12.5 covers 37%; o215.5 72% |
| POR @ SAC | Sat 14 Nov 14:00 | 119.7–111.2 | POR 73% | 1.37 / 3.71 | SAC +8.5 | 230.5 | SAC +10.5 covers 55%; o229.5 53% |
| OKC @ LAC | Sat 14 Nov 14:30 | 113.1–109.4 | OKC 61% | 1.65 / 2.53 | LAC +3.5 | 222.5 | LAC +7.5 covers 61%; o222.5 50% |

### GSW @ SAS
Out: Tobias Harris (SAS), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos PTS over 6.5 (7+) | GSW @ SAS | pointsbetau | 2.10 | 2.04 | 1.98 | 50.4% | 48.7% | 48.9% | +2.7% | +5.9% | 0.6% |
| Georges Niang PTS over 6.5 (7+) | GSW @ SAS | pointsbetau | 1.90 | 1.86 | 1.52 | 65.8% | 52.0% | 53.8% | +2.3% | +25.1% | 0.6% |
| Charles Bassey PTS over 4.5 (5+) | GSW @ SAS | pointsbetau | 1.90 | 1.88 | 1.57 | 63.6% | 51.6% | 53.2% | +1.1% | +20.9% | 0.3% |
| Yaxel Lendeborg PTS over 21.5 (22+) | GSW @ SAS | pointsbetau | 2.00 | 1.99 | 1.81 | 55.4% | 49.4% | 50.2% | +0.3% | +10.8% | 0.1% |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 96% | 35.0<br><sub>33,32,39,26,37</sub> | 18.2<br><sub>20,9,15,25,22</sub> | 17.5 · 16.5<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>3,6,7,2,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.3<br><sub>3,2,4,5,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 1.9 | 28.3 |
| Yaxel Lendeborg | 98% | 34.5<br><sub>29,30,37,27,36</sub> | 24.0<br><sub>16,17,23,23,25</sub> | 20.5 · 21.5<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>5,8,8,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>5,6,3,4,0</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>2,1,2,4,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.6 | 3.2 | 34.9 |
| Draymond Green | 93% | 28.6<br><sub>17,27,34,21,27</sub> | 6.7<br><sub>4,2,2,2,7</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>4,5,6,3,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 6.4<br><sub>2,11,13,6,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>0,0,0,0,1</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.7 | 2.4 | 18.2 |
| De'Anthony Melton | 98% | 25.3<br><sub>28,17,17,26,25</sub> | 11.4<br><sub>2,5,4,16,11</sub> | 12.5 · 12.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>7,6,1,4,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.8<br><sub>2,2,1,3,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>0,0,1,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.3 | 0.4 | 1.7 | 18.1 |
| Georges Niang | 98% | 21.8<br><sub>22,22,25,19,19</sub> | 9.0<br><sub>13,13,11,9,5</sub> | 6.5 · 6.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>4,4,2,2,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>3,3,1,2,0</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.4 | 0.2 | 1.0 | 13.2 |
| Will Richard | 98% | 20.3<br><sub>28,16,12,-,19</sub> | 5.9<br><sub>6,10,4,-,9</sub> | – · 4.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>5,0,2,-,4</sub> |  | 1.2<br><sub>0,2,1,-,0</sub> |  | 0.7<br><sub>2,2,0,-,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.4 |
| Al Horford | 98% | 19.9<br><sub>-,18,13,15,21</sub> | 6.6<br><sub>-,8,2,5,2</sub> | 6.5 · 6.5<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>-,5,5,2,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>-,1,4,6,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>-,2,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.8 | 0.7 | 12.6 |
| Gui Santos | 91% | 18.0<br><sub>-,-,12,21,12</sub> | 7.2<br><sub>-,-,3,3,0</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>-,-,1,7,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>-,-,0,4,1</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 1.1 | 12.3 |
| Gary Payton II | 76% | 16.2<br><sub>20,10,13,-,-</sub> | 7.2<br><sub>2,9,4,-,-</sub> | 5.5 · 5.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>2,0,0,-,-</sub> |  | 1.3<br><sub>1,0,0,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.9 | 0.2 | 0.8 | 11.2 |
| Charles Bassey | 97% | 14.1<br><sub>23,14,11,18,13</sub> | 6.7<br><sub>19,8,8,12,7</sub> | – · 4.5<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>8,7,4,10,6</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 12.6 |
| LJ Cryer | 71% | 14.1<br><sub>1,1,-,20,18</sub> | 6.5<br><sub>0,0,-,10,13</sub> |  | 1.4<br><sub>0,0,-,0,1</sub> |  | 1.1<br><sub>0,0,-,3,1</sub> |  | 1.0<br><sub>0,0,-,2,3</sub> |  | 0.3 | 0.1 | 0.7 | 9.0 |
| Graham Ike | 91% | 9.6<br><sub>7,1,-,12,4</sub> | 3.9<br><sub>0,0,-,4,4</sub> |  | 2.2<br><sub>0,1,-,5,0</sub> |  | 0.7<br><sub>0,0,-,2,1</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| Malevy Leons | 58% | 8.6<br><sub>-,1,-,12,4</sub> | 2.6<br><sub>-,0,-,0,0</sub> |  | 1.6<br><sub>-,0,-,3,3</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.7 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 31.6<br><sub>36,28,28,26,36</sub> | 16.6<br><sub>21,19,13,17,18</sub> | 16.5 · 15.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>5,2,7,5,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 4.6<br><sub>0,3,3,4,10</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>1,1,1,0,2</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.2 | 0.3 | 1.8 | 26.6 |
| Victor Wembanyama | 98% | 31.0<br><sub>34,26,24,25,32</sub> | 27.8<br><sub>52,30,29,40,32</sub> | 26.5 · 27.5<br><sub>o 50% · u 50%</sub> | 11.3<br><sub>24,14,7,11,9</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>2,2,3,3,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>1,4,3,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 3.7 | 2.6 | 42.3 |
| Devin Vassell | 98% | 30.0<br><sub>36,27,21,-,-</sub> | 11.8<br><sub>2,19,15,-,-</sub> | 11.5 · 11.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>7,2,2,-,-</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>4,2,3,-,-</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>0,5,2,-,-</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.4 | 1.1 | 18.5 |
| De'Aaron Fox | 98% | 29.7<br><sub>33,26,22,29,31</sub> | 14.4<br><sub>10,9,8,15,17</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>3,2,3,9,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 6.0<br><sub>4,4,6,6,9</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>0,0,1,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.4 | 2.1 | 24.1 |
| Stephon Castle | 98% | 29.5<br><sub>35,28,24,30,29</sub> | 15.3<br><sub>17,19,14,4,11</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>10,3,7,8,1</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>3,7,5,7,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>2,1,2,0,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 2.7 | 26.2 |
| Julian Champagnie | 98% | 26.2<br><sub>21,22,21,27,35</sub> | 9.2<br><sub>0,8,14,11,12</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>4,7,4,3,0</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>3,2,0,2,2</sub> |  | 1.8<br><sub>0,2,4,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.4 | 0.8 | 15.1 |
| Keldon Johnson | 98% | 23.8<br><sub>19,27,27,26,28</sub> | 9.3<br><sub>4,3,10,4,10</sub> | 9.5 · 8.5<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>5,6,7,5,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>2,6,4,3,4</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.2 | 1.2 | 16.2 |
| Luke Kornet | 98% | 14.5<br><sub>14,18,15,13,14</sub> | 3.7<br><sub>2,2,6,2,7</sub> |  | 4.3<br><sub>1,6,4,4,5</sub> |  | 1.1<br><sub>2,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.1 |
| Harrison Barnes | 88% | 14.2<br><sub>13,19,19,21,13</sub> | 5.0<br><sub>4,13,5,11,3</sub> |  | 1.6<br><sub>2,1,3,2,1</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.6<br><sub>1,2,1,2,1</sub> |  | 0.4 | 0.1 | 0.5 | 7.4 |
| Carter Bryant | 88% | 11.9<br><sub>-,3,17,14,15</sub> | 4.3<br><sub>-,0,6,8,10</sub> |  | 1.9<br><sub>-,0,4,1,1</sub> |  | 0.8<br><sub>-,0,1,1,2</sub> |  | 0.6<br><sub>-,0,2,2,2</sub> |  | 0.3 | 0.3 | 0.6 | 7.1 |
| Jordan McLaughlin | 71% | 7.5<br><sub>-,8,12,11,2</sub> | 2.7<br><sub>-,2,3,4,4</sub> |  | 1.0<br><sub>-,2,0,4,0</sub> |  | 1.2<br><sub>-,1,0,2,0</sub> |  | 0.2<br><sub>-,0,1,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.9 |
| Tarris Reed Jr. | 76% | 6.5<br><sub>-,3,9,9,2</sub> | 2.6<br><sub>-,0,2,4,0</sub> |  | 2.5<br><sub>-,1,3,3,0</sub> |  | 0.3<br><sub>-,0,1,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.1 | 0.3 | 0.5 | 5.4 |
| Maliq Brown | 80% | 6.3<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 2.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 3.4 |
| David Jones Garcia | 67% | 6.2<br><sub>-,3,-,8,2</sub> | 2.5<br><sub>-,0,-,2,0</sub> |  | 1.1<br><sub>-,0,-,0,0</sub> |  | 1.1<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 4.8 |
| Ja'Kobi Gillespie | 88% | 5.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.1 |

</details>


### POR @ SAC
Out: Precious Achiuwa (SAC), Alex Karaban (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 33.6<br><sub>35,39,24,34,35</sub> | 25.3<br><sub>21,22,15,24,28</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>7,9,4,6,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>12,11,1,8,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,1,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.5 | 3.5 | 38.9 |
| Toumani Camara | 98% | 31.2<br><sub>32,30,21,30,38</sub> | 13.2<br><sub>11,18,4,12,14</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>4,6,4,3,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,1,0,3,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,4,0,2,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.4 | 1.3 | 19.7 |
| Damian Lillard | 98% | 30.5<br><sub>33,37,20,24,32</sub> | 19.9<br><sub>25,22,12,25,18</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>3,0,0,3,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.6<br><sub>5,4,7,3,3</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.9<br><sub>2,4,2,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 2.2 | 29.0 |
| Jrue Holiday | 98% | 28.5<br><sub>28,31,20,25,30</sub> | 14.7<br><sub>15,12,11,11,19</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>4,1,0,1,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>0,7,0,2,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>5,3,1,2,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.2 | 1.9 | 23.9 |
| Donovan Clingan | 98% | 26.7<br><sub>29,28,22,26,30</sub> | 11.7<br><sub>24,17,6,7,5</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 10.9<br><sub>11,11,5,13,12</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>1,1,0,3,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,3,0,1,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.6 | 1.9 | 1.3 | 24.6 |
| Sidy Cissoko | 98% | 25.4<br><sub>21,22,16,33,29</sub> | 8.5<br><sub>7,7,4,17,19</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>4,2,3,3,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>4,3,1,3,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>1,2,0,3,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 1.1 | 14.2 |
| Scoot Henderson | 98% | 24.8<br><sub>22,23,24,23,19</sub> | 12.1<br><sub>9,2,13,11,5</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 3.2<br><sub>1,0,1,4,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>1,0,0,3,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 2.1 | 17.6 |
| Robert Williams III | 98% | 17.9<br><sub>16,16,-,15,17</sub> | 7.4<br><sub>9,9,-,6,10</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>8,5,-,4,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>1,2,-,0,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.2 | 0.9 | 15.4 |
| Jayson Kent | 52% | 11.1<br><sub>-,-,12,-,-</sub> | 4.0<br><sub>-,-,4,-,-</sub> |  | 1.6<br><sub>-,-,1,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 6.3 |
| Branden Carlson | 67% | 11.0<br><sub>3,-,12,8,10</sub> | 3.0<br><sub>2,-,4,2,0</sub> |  | 2.6<br><sub>0,-,2,5,2</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 6.0 |
| Micah Potter | 58% | 9.2<br><sub>2,-,14,5,-</sub> | 3.8<br><sub>4,-,7,0,-</sub> |  | 2.5<br><sub>1,-,3,3,-</sub> |  | 0.6<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>1,-,1,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| Yang Hansen | 64% | 9.0<br><sub>2,3,26,5,-</sub> | 3.3<br><sub>0,2,12,0,-</sub> |  | 2.4<br><sub>0,0,10,1,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.2<br><sub>0,0,1,0,-</sub> |  | 0.2 | 0.2 | 0.8 | 6.2 |
| John Tonje | 38% | 6.9<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 37.8<br><sub>37,42,33,39,40</sub> | 26.1<br><sub>25,22,22,32,29</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,3,3,5,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>6,12,8,10,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>2,3,3,3,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.3 | 3.7 | 37.4 |
| Domantas Sabonis | 98% | 33.2<br><sub>31,35,31,-,24</sub> | 15.2<br><sub>9,16,17,-,0</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 12.2<br><sub>7,17,12,-,2</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>4,1,5,-,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.3<br><sub>0,0,1,-,0</sub> |  | 0.9 | 0.4 | 2.8 | 33.3 |
| De'Andre Hunter | 98% | 33.2<br><sub>36,38,-,31,34</sub> | 14.0<br><sub>6,14,-,14,15</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>7,2,-,3,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,2,-,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,-,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 1.9 | 20.5 |
| Zach LaVine | 98% | 33.1<br><sub>28,35,35,25,33</sub> | 19.3<br><sub>23,21,14,15,31</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>4,4,4,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>1,1,3,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>5,3,1,1,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.3 | 2.7 | 24.9 |
| Keegan Murray | 98% | 28.6<br><sub>-,-,-,23,24</sub> | 11.5<br><sub>-,-,-,10,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>-,-,-,1,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>-,-,-,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2<br><sub>-,-,-,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 1.1 | 1.1 | 17.3 |
| Leaky Black | 76% | 21.8<br><sub>25,22,40,20,18</sub> | 5.2<br><sub>12,3,12,6,0</sub> |  | 3.4<br><sub>3,6,3,5,3</sub> |  | 1.4<br><sub>1,1,5,1,2</sub> |  | 0.7<br><sub>4,0,4,2,0</sub> |  | 1.1 | 0.5 | 0.7 | 10.1 |
| Dylan Cardwell | 98% | 20.7<br><sub>-,13,15,18,29</sub> | 6.4<br><sub>-,4,9,4,1</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>-,6,2,9,11</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>-,0,3,3,1</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.1 | 15.4 |
| Emanuel Sharp | 98% | 17.9<br><sub>20,10,31,12,19</sub> | 4.7<br><sub>9,3,9,5,2</sub> |  | 1.6<br><sub>3,1,5,1,2</sub> |  | 0.8<br><sub>1,2,0,0,0</sub> |  | 0.6<br><sub>3,1,3,1,0</sub> |  | 0.7 | 0.3 | 0.5 | 7.1 |
| Malik Monk | 98% | 14.8<br><sub>30,24,18,21,3</sub> | 8.1<br><sub>24,13,12,9,1</sub> |  | 1.3<br><sub>1,2,0,2,0</sub> |  | 2.4<br><sub>7,3,7,3,0</sub> |  | 0.9<br><sub>5,3,2,0,0</sub> |  | 0.5 | 0.3 | 1.2 | 11.8 |
| Daeqwon Plowden | 76% | 9.8<br><sub>3,-,-,12,2</sub> | 3.3<br><sub>1,-,-,6,0</sub> |  | 1.1<br><sub>1,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.3<br><sub>0,-,-,2,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.8 |
| Mason Plumlee | 5% | 8.1 | 2.4 |  | 2.7 |  | 0.8 |  | 0.0 |  | 0.3 | 0.3 | 0.5 | 5.9 |

</details>


### OKC @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.1–109.4 | OKC 61% | 1.65 / 2.53 | LAC +3.5 | 222.5 | LAC +7.5 covers 61%; o222.5 50% |
| Expected (weighted by chance each plays) | 113.7–109.8 | OKC 61% | 1.64 / 2.56 | LAC +4.5 | 223.5 | LAC +7.5 covers 60%; o222.5 52% |
| if Ajay Mitchell plays | 114.1–110.4 | OKC 61% | 1.65 / 2.55 | LAC +3.5 | 224.5 | LAC +7.5 covers 61%; o222.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ajay Mitchell (OKC) | Questionable | 55% | 27.8 | 16.5 | 3.4 | 3.7 | 1.0 | 1.3 | 0.2 | 1.8 | 23.7 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 35.0<br><sub>35,30,29,29,36</sub> | 31.7<br><sub>42,28,30,26,31</sub> | 31.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>4,3,2,8,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.9<br><sub>8,4,9,3,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>5,3,3,0,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.7 | 3.3 | 42.8 |
| Jared McCain | 98% | 30.4<br><sub>25,29,23,31,31</sub> | 16.4<br><sub>9,21,19,21,10</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>1,5,5,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>0,0,2,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.5<br><sub>1,3,2,4,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 2.1 | 22.4 |
| Isaiah Hartenstein | 98% | 28.5<br><sub>26,26,18,24,34</sub> | 10.7<br><sub>3,2,2,7,20</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 10.6<br><sub>12,6,14,9,11</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,7,6,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.7 | 1.9 | 25.4 |
| Aday Mara | 98% | 28.3<br><sub>25,18,27,26,32</sub> | 11.1<br><sub>9,9,18,10,11</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>5,7,8,10,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>2,0,3,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.4 | 1.6 | 1.8 | 21.0 |
| Alex Caruso | 98% | 25.9<br><sub>20,20,13,19,29</sub> | 10.3<br><sub>7,5,0,5,14</sub> | 6.5 · –<br><sub>o 55% · u 45%</sub> | 4.2<br><sub>4,6,3,2,7</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.6 | 0.4 | 1.2 | 17.4 |
| Kenrich Williams | 98% | 25.7<br><sub>29,19,23,19,26</sub> | 10.0<br><sub>13,4,9,3,11</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>4,6,4,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,1,1,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 1.1 | 17.1 |
| Bennett Stirtz | 98% | 24.8<br><sub>22,24,29,18,25</sub> | 9.8<br><sub>16,12,11,13,6</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>1,1,5,1,1</sub> |  | 1.7<br><sub>1,2,3,1,1</sub> |  | 1.6<br><sub>4,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 1.0 | 13.4 |
| Micah Peavy | 88% | 19.5<br><sub>26,18,23,21,12</sub> | 5.0<br><sub>2,7,7,0,0</sub> |  | 3.2<br><sub>9,4,3,2,3</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.6<br><sub>0,1,1,0,0</sub> |  | 0.7 | 0.2 | 0.5 | 9.0 |
| Nique Clifford | 93% | 18.0<br><sub>-,-,-,20,16</sub> | 6.3<br><sub>-,-,-,4,5</sub> |  | 2.8<br><sub>-,-,-,4,3</sub> |  | 1.8<br><sub>-,-,-,1,1</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.7 | 0.2 | 1.1 | 10.8 |
| Josh Dix | 63% | 17.4<br><sub>-,15,21,-,-</sub> | 4.4<br><sub>-,5,2,-,-</sub> |  | 1.6<br><sub>-,2,1,-,-</sub> |  | 0.9<br><sub>-,1,2,-,-</sub> |  | 0.5<br><sub>-,1,0,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.0 |
| Brooks Barnhizer | 63% | 9.5<br><sub>-,5,8,5,-</sub> | 2.2<br><sub>-,0,2,0,-</sub> |  | 2.0<br><sub>-,0,4,1,-</sub> |  | 0.7<br><sub>-,0,3,1,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.9 |
| Nikola Topic | 63% | 8.8 | 2.8 |  | 1.0 |  | 2.0 |  | 0.2 |  | 0.3 | 0.1 | 1.0 | 5.8 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 30.8<br><sub>33,36,39,32,25</sub> | 18.1<br><sub>15,16,26,24,13</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>0,4,1,0,5</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>7,8,7,10,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,1,4,3,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 3.3 | 26.9 |
| Rui Hachimura | 98% | 27.9<br><sub>30,-,37,26,23</sub> | 14.1<br><sub>24,-,21,14,13</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,-,9,3,5</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>0,-,7,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 2.0<br><sub>4,-,1,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.3 | 1.4 | 20.0 |
| Derrick Jones Jr. | 98% | 26.9<br><sub>28,-,37,29,24</sub> | 10.2<br><sub>9,-,12,8,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>7,-,8,4,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,-,1,3,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4<br><sub>1,-,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.7 | 1.1 | 15.5 |
| Kris Dunn | 98% | 25.2<br><sub>27,30,35,24,19</sub> | 7.5<br><sub>12,12,5,14,3</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,4,5,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,1,3,4,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>0,1,1,2,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.3 | 1.4 | 14.3 |
| Brook Lopez | 98% | 22.5<br><sub>19,22,35,26,19</sub> | 10.9<br><sub>7,12,20,20,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>2,6,8,7,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 1.0 | 1.1 | 16.5 |
| Kobe Sanders | 98% | 22.0<br><sub>30,38,18,22,26</sub> | 9.3<br><sub>16,26,4,8,9</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>0,3,1,4,7</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>4,5,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.2 | 1.4 | 13.9 |
| Max Strus | 98% | 21.1<br><sub>-,23,23,19,22</sub> | 8.5<br><sub>-,11,9,7,12</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>-,4,5,4,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>-,6,5,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>-,3,3,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.2 | 1.0 | 14.7 |
| Keaton Wagler | 98% | 20.9<br><sub>19,24,16,18,23</sub> | 9.4<br><sub>7,6,11,15,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>4,4,2,2,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>4,4,1,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,0,3,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.2 | 1.8 | 15.5 |
| Isaiah Jackson | 98% | 17.1<br><sub>22,26,13,-,16</sub> | 6.9<br><sub>5,19,2,-,4</sub> |  | 5.2<br><sub>8,8,4,-,4</sub> |  | 1.3<br><sub>2,2,2,-,0</sub> |  | 0.0<br><sub>0,1,0,-,0</sub> |  | 0.8 | 0.8 | 1.3 | 13.4 |
| Gradey Dick | 96% | 14.5<br><sub>3,29,7,17,19</sub> | 6.6<br><sub>0,12,4,15,10</sub> |  | 2.3<br><sub>1,4,2,4,3</sub> |  | 0.7<br><sub>0,3,1,0,2</sub> |  | 0.7<br><sub>0,0,0,2,1</sub> |  | 0.6 | 0.1 | 0.8 | 9.6 |
| Baba Miller | 93% | 14.3<br><sub>6,12,6,20,16</sub> | 6.3<br><sub>2,4,2,12,13</sub> |  | 2.4<br><sub>2,0,1,5,4</sub> |  | 1.5<br><sub>1,1,1,4,0</sub> |  | 0.4<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.9 | 10.2 |
| Jalen Pickett | 58% | 7.6<br><sub>6,-,-,2,8</sub> | 2.8<br><sub>0,-,-,0,3</sub> |  | 1.0<br><sub>2,-,-,0,1</sub> |  | 1.1<br><sub>3,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,1</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Cam Christie | 58% | 6.1<br><sub>6,-,-,2,-</sub> | 2.3<br><sub>3,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.8 |
| Blake Wesley | 52% | 6.1<br><sub>4,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>if Ajay Mitchell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland (LAC) | 98% | 30.8<br><sub>33,36,39,32,25</sub> | 18.2<br><sub>15,16,26,24,13</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>0,4,1,0,5</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>7,8,7,10,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,1,4,3,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.2 | 3.3 | 27.0 |
| Rui Hachimura (LAC) | 98% | 27.9<br><sub>30,-,37,26,23</sub> | 14.2<br><sub>24,-,21,14,13</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>7,-,9,3,5</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>0,-,7,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 2.0<br><sub>4,-,1,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.3 | 1.4 | 20.1 |
| Derrick Jones Jr. (LAC) | 98% | 26.8<br><sub>28,-,37,29,24</sub> | 10.2<br><sub>9,-,12,8,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>7,-,8,4,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>1,-,1,3,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4<br><sub>1,-,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.7 | 1.1 | 15.6 |
| Kris Dunn (LAC) | 98% | 25.2<br><sub>27,30,35,24,19</sub> | 7.5<br><sub>12,12,5,14,3</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>2,4,5,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,1,3,4,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>0,1,1,2,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.3 | 1.4 | 14.3 |
| Brook Lopez (LAC) | 98% | 22.5<br><sub>19,22,35,26,19</sub> | 10.9<br><sub>7,12,20,20,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>2,6,8,7,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.9 | 1.1 | 16.5 |
| Kobe Sanders (LAC) | 98% | 22.0<br><sub>30,38,18,22,26</sub> | 9.3<br><sub>16,26,4,8,9</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>0,3,1,4,7</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>4,5,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.2 | 1.4 | 13.8 |
| Max Strus (LAC) | 98% | 21.1<br><sub>-,23,23,19,22</sub> | 8.6<br><sub>-,11,9,7,12</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>-,4,5,4,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>-,6,5,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>-,3,3,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.2 | 1.0 | 14.8 |
| Keaton Wagler (LAC) | 98% | 20.9<br><sub>19,24,16,18,23</sub> | 9.6<br><sub>7,6,11,15,11</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>4,4,2,2,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>4,4,1,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,0,3,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.2 | 1.8 | 15.6 |
| Isaiah Jackson (LAC) | 98% | 17.1<br><sub>22,26,13,-,16</sub> | 7.0<br><sub>5,19,2,-,4</sub> |  | 5.2<br><sub>8,8,4,-,4</sub> |  | 1.3<br><sub>2,2,2,-,0</sub> |  | 0.0<br><sub>0,1,0,-,0</sub> |  | 0.8 | 0.7 | 1.3 | 13.4 |
| Gradey Dick (LAC) | 96% | 14.7<br><sub>3,29,7,17,19</sub> | 6.7<br><sub>0,12,4,15,10</sub> |  | 2.3<br><sub>1,4,2,4,3</sub> |  | 0.7<br><sub>0,3,1,0,2</sub> |  | 0.7<br><sub>0,0,0,2,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.8 |
| Baba Miller (LAC) | 93% | 14.3<br><sub>6,12,6,20,16</sub> | 6.3<br><sub>2,4,2,12,13</sub> |  | 2.4<br><sub>2,0,1,5,4</sub> |  | 1.5<br><sub>1,1,1,4,0</sub> |  | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.9 | 10.2 |
| Jalen Pickett (LAC) | 58% | 7.5<br><sub>6,-,-,2,8</sub> | 2.8<br><sub>0,-,-,0,3</sub> |  | 1.0<br><sub>2,-,-,0,1</sub> |  | 1.1<br><sub>3,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,1</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Blake Wesley (LAC) | 52% | 6.1<br><sub>4,-,-,-,-</sub> | 2.6<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Cam Christie (LAC) | 58% | 6.0<br><sub>6,-,-,2,-</sub> | 2.3<br><sub>3,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Shai Gilgeous-Alexander (OKC) | 98% | 33.5<br><sub>35,30,29,29,36</sub> | 29.5<br><sub>42,28,30,26,31</sub> | 31.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>4,3,2,8,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.5<br><sub>8,4,9,3,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>5,3,3,0,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.7 | 2.9 | 40.0 |
| Jared McCain (OKC) | 98% | 27.8<br><sub>25,29,23,31,31</sub> | 14.5<br><sub>9,21,19,21,10</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>1,5,5,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>0,0,2,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.2<br><sub>1,3,2,4,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.6 | 19.8 |
| Ajay Mitchell (OKC) | 100% | 27.8<br><sub>32,30,22,28,-</sub> | 16.5<br><sub>23,35,12,14,-</sub> | 18.5 · – | 3.4<br><sub>7,1,4,3,-</sub> | 3.5 | 3.7<br><sub>4,5,0,3,-</sub> | 3.5 | 1.0<br><sub>1,4,0,0,-</sub> | 1.5 | 1.3 | 0.2 | 1.8 | 23.7 |
| Isaiah Hartenstein (OKC) | 98% | 26.3<br><sub>26,26,18,24,34</sub> | 9.6<br><sub>3,2,2,7,20</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.8<br><sub>12,6,14,9,11</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,7,6,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.6 | 23.2 |
| Aday Mara (OKC) | 98% | 25.2<br><sub>25,18,27,26,32</sub> | 9.6<br><sub>9,9,18,10,11</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>5,7,8,10,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,0,3,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.5 | 1.5 | 1.6 | 18.3 |
| Alex Caruso (OKC) | 98% | 22.5<br><sub>20,20,13,19,29</sub> | 8.4<br><sub>7,5,0,5,14</sub> | 6.5 · –<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>4,6,3,2,7</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.4 | 1.0 | 14.4 |
| Kenrich Williams (OKC) | 98% | 22.3<br><sub>29,19,23,19,26</sub> | 8.3<br><sub>13,4,9,3,11</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>4,6,4,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>3,1,1,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.1 | 0.9 | 14.3 |
| Bennett Stirtz (OKC) | 98% | 21.5<br><sub>22,24,29,18,25</sub> | 8.0<br><sub>16,12,11,13,6</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,1,5,1,1</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 1.3<br><sub>4,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.2 | 0.9 | 11.0 |
| Micah Peavy (OKC) | 88% | 15.8<br><sub>26,18,23,21,12</sub> | 4.0<br><sub>2,7,7,0,0</sub> |  | 2.6<br><sub>9,4,3,2,3</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.4<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.2 | 0.4 | 7.2 |
| Nique Clifford (OKC) | 93% | 14.6<br><sub>-,-,-,20,16</sub> | 5.0<br><sub>-,-,-,4,5</sub> |  | 2.2<br><sub>-,-,-,4,3</sub> |  | 1.4<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.6 | 0.2 | 0.9 | 8.6 |
| Josh Dix (OKC) | 63% | 13.3<br><sub>-,15,21,-,-</sub> | 3.4<br><sub>-,5,2,-,-</sub> |  | 1.2<br><sub>-,2,1,-,-</sub> |  | 0.7<br><sub>-,1,2,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.2 |
| Brooks Barnhizer (OKC) | 63% | 7.8<br><sub>-,5,8,5,-</sub> | 1.9<br><sub>-,0,2,0,-</sub> |  | 1.6<br><sub>-,0,4,1,-</sub> |  | 0.6<br><sub>-,0,3,1,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Nikola Topic (OKC) | 63% | 6.2 | 2.0 |  | 0.7 |  | 1.5 |  | 0.1 |  | 0.3 | 0.0 | 0.7 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-13/`._
