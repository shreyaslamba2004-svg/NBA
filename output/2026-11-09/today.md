# NBA model · Mon 09 Nov 2026 (US date)

Updated **Tue 10 Nov, 01:51 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-09/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray AST over 9.5 (10+) | NOP @ GSW | draftkings | 12.40 | 11.44 | 6.00 | 16.7% | 7.5% | 8.7% | +8.4% | +106.7% | 0.2% |
| Dejounte Murray AST over 11.5 (12+) | NOP @ GSW | draftkings | 29.00 | 27.47 | 15.71 | 6.4% | 3.2% | 3.6% | +5.5% | +84.6% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| NOP @ GSW | Tue 10 Nov 14:00 | 112.6–123.8 | NOP 22% | 4.64 / 1.27 | GSW -11.5 | 236.5 | GSW -11.5 covers 49%; o228.5 66% |

### NOP @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Gary Payton II (GSW), Kristaps Porzingis (GSW), Will Richard (GSW), Yves Missi (NOP), Trey Murphy III (NOP), Trendon Watford (NOP), Zion Williamson (NOP)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Williams PTS over 9.5 (10+) | NOP @ GSW | pointsbetau | 1.95 | 1.94 | 1.92 | 52.2% | 51.3% | 51.4% | +0.4% | +1.9% | 0.1% |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray | 100% | 34.8<br><sub>-,-,45,35,28</sub> | 19.5<br><sub>-,-,20,7,6</sub> | 17.5 · 17.5<br><sub>o 52% · u 48%</sub> | 5.9<br><sub>-,-,8,2,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 6.7<br><sub>-,-,4,4,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>-,-,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 2.0 | 0.4 | 3.4 | 32.1 |
| Saddiq Bey | 100% | 34.4<br><sub>26,36,29,31,26</sub> | 19.7<br><sub>25,18,22,17,13</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>6,5,4,5,4</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,1,3,4,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,2,2,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 1.7 | 28.4 |
| Jeremiah Fears | 100% | 32.9<br><sub>31,38,34,36,29</sub> | 19.8<br><sub>20,12,19,24,25</sub> | 17.5 · 17.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,4,6,5,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.9<br><sub>7,7,2,5,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>1,0,1,0,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.5 | 0.5 | 3.2 | 29.5 |
| Herbert Jones | 100% | 29.3<br><sub>25,28,37,14,20</sub> | 9.1<br><sub>11,9,2,0,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,4,5,4,0</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,3,1,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>1,3,0,0,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.4 | 1.4 | 14.9 |
| Derik Queen | 98% | 28.3<br><sub>23,24,27,10,21</sub> | 14.1<br><sub>8,20,20,6,8</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 8.4<br><sub>8,7,9,4,5</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>4,5,6,1,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 1.2 | 0.8 | 2.8 | 26.5 |
| Karlo Matkovic | 100% | 28.1<br><sub>18,29,21,18,19</sub> | 11.3<br><sub>8,25,5,18,3</sub> | 8.5 · 8.5<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>10,6,4,3,3</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.7<br><sub>1,1,2,1,2</sub> |  | 1.4<br><sub>2,5,1,4,1</sub> |  | 0.9 | 1.1 | 1.4 | 19.4 |
| Bennedict Mathurin | 98% | 21.8<br><sub>19,13,15,7,9</sub> | 9.9<br><sub>7,4,2,2,6</sub> | 9.5 · 10.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>1,0,5,0,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,0,1,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.2 | 1.4 | 15.6 |
| Jordan Poole | 52% | 18.9<br><sub>-,-,-,-,-</sub> | 9.7<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.3 | 1.4 | 14.1 |
| Bryce McGowens | 58% | 16.3<br><sub>15,6,-,-,3</sub> | 5.5<br><sub>3,0,-,-,0</sub> |  | 1.9<br><sub>0,1,-,-,0</sub> |  | 1.2<br><sub>1,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 8.6 |
| DeAndre Jordan | 26% | 15.9<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 5.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.6 | 0.7 | 11.0 |
| Julian Reese | 48% | 9.4<br><sub>3,-,-,-,3</sub> | 2.9<br><sub>2,-,-,-,0</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 5.1 |
| AJ Johnson | 47% | 9.1<br><sub>3,-,-,-,3</sub> | 3.0<br><sub>0,-,-,-,2</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.6 | 0.6 | 4.1 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 100% | 33.8<br><sub>33,37,33,32,39</sub> | 16.3<br><sub>21,17,20,9,15</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>5,8,3,6,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>6,8,2,3,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>4,2,3,2,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.3 | 1.7 | 25.9 |
| Yaxel Lendeborg | 100% | 33.3<br><sub>24,34,29,30,37</sub> | 20.9<br><sub>6,37,16,17,23</sub> | 19.5 · 19.5<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>1,4,5,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>0,6,5,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>1,6,2,1,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 1.0 | 3.1 | 32.3 |
| Stephen Curry | 100% | 32.4<br><sub>31,-,33,28,36</sub> | 27.9<br><sub>31,-,34,29,41</sub> | 27.5 · 27.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,-,6,1,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,-,7,4,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>8,-,5,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.4 | 2.6 | 36.9 |
| Draymond Green | 100% | 28.3<br><sub>32,-,17,27,34</sub> | 6.8<br><sub>2,-,4,2,2</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>9,-,2,11,13</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.8<br><sub>0,-,0,0,0</sub> |  | 1.1 | 0.8 | 2.4 | 19.0 |
| Georges Niang | 97% | 21.0<br><sub>19,21,22,22,25</sub> | 8.3<br><sub>11,3,13,13,11</sub> | 7.5 · 7.5<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>5,1,4,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>1,2,3,3,1</sub> |  | 1.4<br><sub>3,1,1,2,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5 | 0.2 | 1.0 | 12.7 |
| De'Anthony Melton | 98% | 20.4<br><sub>21,28,28,17,17</sub> | 9.2<br><sub>16,21,2,5,4</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>5,6,7,6,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,3,2,2,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3<br><sub>4,6,0,0,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.3 | 1.3 | 14.6 |
| Gui Santos | 100% | 19.5<br><sub>16,9,-,-,12</sub> | 8.1<br><sub>2,4,-,-,3</sub> | 7.5 · 8.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>5,3,-,-,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,-,-,0</sub> |  | 0.8<br><sub>0,0,-,-,0</sub> |  | 0.8 | 0.3 | 1.3 | 13.8 |
| Brandon Williams | 86% | 18.3<br><sub>17,25,-,21,17</sub> | 10.7<br><sub>9,17,-,10,9</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,3,-,1,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.8<br><sub>1,3,-,4,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>0,2,-,0,0</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 1.6 | 15.8 |
| Al Horford | 98% | 16.2<br><sub>17,22,-,18,13</sub> | 5.7<br><sub>3,9,-,8,2</sub> |  | 3.7<br><sub>2,5,-,5,5</sub> |  | 1.5<br><sub>0,2,-,1,4</sub> |  | 0.8<br><sub>1,3,-,2,0</sub> |  | 0.3 | 0.8 | 0.5 | 10.8 |
| Charles Bassey | 96% | 12.4<br><sub>9,20,23,14,11</sub> | 6.1<br><sub>6,6,19,8,8</sub> |  | 5.2<br><sub>4,10,8,7,4</sub> |  | 0.6<br><sub>1,2,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.0 | 0.7 | 11.9 |
| Graham Ike | 88% | 7.2<br><sub>-,6,7,1,-</sub> | 3.1<br><sub>-,2,0,0,-</sub> |  | 1.8<br><sub>-,2,0,1,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |
| LJ Cryer | 58% | 6.6<br><sub>-,2,1,1,-</sub> | 3.1<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.0 | 0.3 | 4.3 |
| Malevy Leons | 48% | 6.1<br><sub>-,-,-,1,-</sub> | 1.9<br><sub>-,-,-,0,-</sub> |  | 1.2<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-09/`._
