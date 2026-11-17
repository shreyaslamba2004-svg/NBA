# NBA model · Mon 16 Nov 2026 (US date)

Updated **Tue 17 Nov, 11:47 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-16/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Draymond Green AST over 11.5 (12+) | GSW @ NOP | draftkings | 22.00 | 19.19 | 9.56 | 10.5% | 4.2% | 5.2% | +14.5% | +130.2% | 0.2% |
| Derik Queen PRA over 34.5 (35+) | GSW @ NOP | draftkings | 20.20 | 17.83 | 9.10 | 11.0% | 4.6% | 5.6% | +13.3% | +122.1% | 0.2% |
| Draymond Green AST over 9.5 (10+) | GSW @ NOP | draftkings | 9.20 | 8.24 | 4.35 | 23.0% | 10.2% | 12.1% | +11.7% | +111.7% | 0.4% |
| Derik Queen PRA over 29.5 (30+) | GSW @ NOP | draftkings | 9.00 | 8.10 | 4.33 | 23.1% | 10.4% | 12.3% | +11.1% | +107.9% | 0.4% |
| Derik Queen AST over 5.5 (6+) | GSW @ NOP | draftkings | 12.20 | 11.12 | 6.13 | 16.3% | 7.7% | 9.0% | +9.7% | +98.9% | 0.2% |
| Derik Queen PR over 29.5 (30+) | GSW @ NOP | draftkings | 16.20 | 14.88 | 8.39 | 11.9% | 5.8% | 6.7% | +8.8% | +93.1% | 0.1% |
| Derik Queen PTS over 19.5 (20+) | GSW @ NOP | draftkings | 12.80 | 11.95 | 7.02 | 14.2% | 7.3% | 8.4% | +7.1% | +82.3% | 0.1% |
| PHX to win | PHX @ DEN | unibet | 4.80 | 4.50 | 3.70 | 27.0% | 22.2% | 22.2% | +6.8% | +29.6% | 0.4% |
| Nikola Jokic PA over 54.5 (55+) | PHX @ DEN | draftkings | 21.00 | 19.92 | 12.24 | 8.2% | 4.5% | 5.0% | +5.5% | +71.6% | 0.1% |
| Derik Queen PR over 24.5 (25+) | GSW @ NOP | draftkings | 6.43 | 6.11 | 3.78 | 26.5% | 14.5% | 16.4% | +5.3% | +70.3% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| POR @ MIN | Tue 17 Nov 12:00 | 111.5–115.7 | POR 38% | 2.62 / 1.62 | MIN -4.5 | 227.5 | MIN -2.5 covers 56%; o227.5 49% |
| GSW @ NOP | Tue 17 Nov 12:00 | 120.6–113.0 | GSW 71% | 1.42 / 3.40 | NOP +7.5 | 233.5 | NOP +3.5 covers 38%; o223.5 70% |
| PHX @ DEN | Tue 17 Nov 13:00 | 110.4–119.2 | PHX 26% | 3.78 / 1.36 | DEN -8.5 | 229.5 | DEN -9.5 covers 48%; o229.5 50% |

### POR @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 100% | 34.0<br><sub>39,24,34,35,35</sub> | 23.3<br><sub>22,15,24,28,34</sub> | 23.5 · 23.5<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>9,4,6,3,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>11,1,8,6,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,2,2,4,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.6 | 3.6 | 35.9 |
| Toumani Camara | 100% | 32.0<br><sub>30,21,30,38,36</sub> | 11.8<br><sub>18,4,12,14,14</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>6,4,3,5,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,0,3,3,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>4,0,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 1.4 | 17.9 |
| Damian Lillard | 100% | 31.8<br><sub>37,20,24,32,33</sub> | 19.8<br><sub>22,12,25,18,29</sub> | 21.5 · 20.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>0,0,3,3,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>4,7,3,3,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>4,2,4,2,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.2 | 2.6 | 28.4 |
| Jrue Holiday | 98% | 28.9<br><sub>31,20,25,30,27</sub> | 13.3<br><sub>12,11,11,19,6</sub> | 12.5 · 13.5<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>1,0,1,3,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,0,2,5,5</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>3,1,2,5,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 2.4 | 22.0 |
| Sidy Cissoko | 100% | 27.9<br><sub>22,16,33,29,26</sub> | 7.9<br><sub>7,4,17,19,3</sub> | 6.5 · 6.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>2,3,3,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>3,1,3,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>2,0,3,4,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.5 | 1.3 | 13.8 |
| Donovan Clingan | 100% | 27.2<br><sub>28,22,26,30,27</sub> | 10.9<br><sub>17,6,7,5,13</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 10.6<br><sub>11,5,13,12,11</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>1,0,3,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>3,0,1,1,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.6 | 2.0 | 1.3 | 23.4 |
| Scoot Henderson | 98% | 24.5<br><sub>23,24,23,19,23</sub> | 11.1<br><sub>2,13,11,5,11</sub> | 10.5 · 9.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,2,1,2,0</sub> |  | 2.5<br><sub>0,1,4,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>0,0,3,1,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.2 | 15.9 |
| Robert Williams III | 98% | 17.0<br><sub>16,-,15,17,17</sub> | 6.2<br><sub>9,-,6,10,2</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>5,-,4,7,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.0<br><sub>2,-,0,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.3 | 0.8 | 13.8 |
| Jayson Kent | 63% | 11.9<br><sub>-,12,-,-,11</sub> | 4.2<br><sub>-,4,-,-,3</sub> |  | 1.6<br><sub>-,1,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,1</sub> |  | 0.5 | 0.2 | 0.7 | 6.3 |
| Branden Carlson | 76% | 9.0<br><sub>-,12,8,10,8</sub> | 2.5<br><sub>-,4,2,0,5</sub> |  | 2.3<br><sub>-,2,5,2,3</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.1<br><sub>-,0,0,0,1</sub> |  | 0.2 | 0.6 | 0.5 | 5.2 |
| Micah Potter | 52% | 8.3<br><sub>-,14,5,-,-</sub> | 3.5<br><sub>-,7,0,-,-</sub> |  | 2.2<br><sub>-,3,3,-,-</sub> |  | 0.5<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.2 |
| Yang Hansen | 52% | 7.7<br><sub>3,26,5,-,-</sub> | 2.9<br><sub>2,12,0,-,-</sub> |  | 2.0<br><sub>0,10,1,-,-</sub> |  | 0.4<br><sub>0,1,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.2 | 0.6 | 5.3 |
| John Tonje | 36% | 6.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 34.8<br><sub>37,40,33,25,37</sub> | 17.1<br><sub>14,23,16,16,18</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>8,6,6,9,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>4,5,3,3,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>0,2,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 1.0 | 2.1 | 25.9 |
| Ayo Dosunmu | 100% | 33.5<br><sub>34,39,30,27,33</sub> | 18.4<br><sub>21,26,26,18,24</sub> | 17.5 · 17.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>1,2,4,2,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.8<br><sub>6,4,1,1,0</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>0,4,4,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.4 | 2.3 | 26.6 |
| Jonathan Kuminga | 100% | 31.9<br><sub>32,34,25,24,35</sub> | 14.0<br><sub>16,17,4,14,11</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>8,8,0,8,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>5,4,0,5,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>4,1,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.7 | 1.7 | 22.3 |
| LaMelo Ball | 100% | 30.4<br><sub>31,35,30,25,30</sub> | 21.0<br><sub>20,22,24,22,19</sub> | 20.5 · 20.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>2,2,3,3,8</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.1<br><sub>6,8,5,9,6</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 3.5<br><sub>4,3,4,6,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.8 | 0.3 | 3.4 | 31.5 |
| Rudy Gobert | 100% | 30.0<br><sub>33,25,31,23,27</sub> | 9.6<br><sub>8,8,10,9,1</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 10.9<br><sub>11,11,15,6,10</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>2,0,2,1,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.4 | 1.3 | 22.2 |
| Terrence Shannon Jr. | 98% | 22.4<br><sub>-,-,18,21,22</sub> | 10.9<br><sub>-,-,5,6,14</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>-,-,3,2,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>-,-,3,4,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.1 | 1.2 | 15.6 |
| Trey Lyles | 98% | 19.3<br><sub>20,29,21,15,19</sub> | 5.7<br><sub>5,5,9,2,5</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,13,6,0,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>0,2,2,0,2</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.6 | 0.3 | 0.6 | 10.7 |
| Bones Hyland | 98% | 18.2<br><sub>16,10,13,23,21</sub> | 10.0<br><sub>19,4,14,24,12</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>2,1,2,3,1</sub> |  | 2.8<br><sub>4,0,2,8,2</sub> |  | 1.4<br><sub>4,1,1,5,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 1.3 | 14.6 |
| Joan Beringer | 98% | 14.6<br><sub>13,7,16,22,13</sub> | 6.0<br><sub>4,2,4,13,2</sub> |  | 4.9<br><sub>7,3,3,9,5</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 11.4 |
| Zyon Pullin | 35% | 7.5<br><sub>-,-,-,-,-</sub> | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.7 |
| Rocco Zikarsky | 38% | 7.3<br><sub>-,-,2,-,-</sub> | 2.6<br><sub>-,-,0,-,-</sub> |  | 2.2<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.1 |
| Cody Williams | 52% | 6.1<br><sub>-,-,2,7,-</sub> | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 1.3 |
| Isaiah Evans | 52% | 5.8<br><sub>-,-,2,8,-</sub> | 5.9<br><sub>-,-,0,2,-</sub> |  | 1.1<br><sub>-,-,0,1,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 7.4 |
| Johni Broome | 5% | 5.4 | 2.0 |  | 1.3 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.7 |

</details>


### GSW @ NOP
Out: Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derik Queen PTS over 10.5 (11+) | GSW @ NOP | draftkings | 1.99 | 1.97 | 1.64 | 61.1% | 48.9% | 50.8% | +1.1% | +21.5% | 0.3% |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 100% | 33.7<br><sub>32,39,26,37,22</sub> | 19.8<br><sub>9,15,25,22,8</sub> | 18.5 · 17.5<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>6,7,2,6,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>3,1,4,4,0</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>2,4,5,4,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 1.9 | 30.0 |
| Yaxel Lendeborg | 100% | 33.1<br><sub>30,37,27,36,24</sub> | 21.7<br><sub>17,23,23,25,3</sub> | 23.5 · 23.5<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>8,8,7,10,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>6,3,4,0,1</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,2,4,2,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.8 | 3.1 | 33.3 |
| Draymond Green | 100% | 27.9<br><sub>27,34,21,27,16</sub> | 6.5<br><sub>2,2,2,7,4</sub> | 5.5 · 5.5<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>5,6,3,5,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 7.3<br><sub>11,13,6,7,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.7<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.8 | 2.5 | 19.1 |
| De'Anthony Melton | 98% | 23.4<br><sub>17,17,26,25,18</sub> | 12.3<br><sub>5,4,16,11,8</sub> | 11.5 · 13.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>6,1,4,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>2,1,3,4,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,1,4,3,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.5 | 0.4 | 1.5 | 19.1 |
| Al Horford | 100% | 23.2<br><sub>18,13,15,21,10</sub> | 8.0<br><sub>8,2,5,2,0</sub> |  | 5.1<br><sub>5,5,2,1,3</sub> |  | 2.9<br><sub>1,4,6,4,1</sub> |  | 1.3<br><sub>2,0,1,0,0</sub> |  | 0.6 | 1.1 | 0.8 | 16.0 |
| Will Richard | 98% | 23.0<br><sub>16,12,-,19,30</sub> | 7.2<br><sub>10,4,-,9,7</sub> | 4.5 · 6.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>0,2,-,4,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>2,1,-,0,1</sub> |  | 0.9<br><sub>2,0,-,2,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.2 | 0.9 | 11.6 |
| LJ Cryer | 100% | 22.7<br><sub>1,-,20,18,24</sub> | 11.9<br><sub>0,-,10,13,20</sub> |  | 1.8<br><sub>0,-,0,1,2</sub> |  | 2.6<br><sub>0,-,3,1,6</sub> |  | 2.2<br><sub>0,-,2,3,6</sub> |  | 0.5 | 0.1 | 1.2 | 16.3 |
| Georges Niang | 98% | 20.1<br><sub>22,25,19,19,15</sub> | 8.6<br><sub>13,11,9,5,5</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,2,2,5,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>3,1,2,0,2</sub> |  | 1.4<br><sub>2,3,1,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.4 | 0.2 | 0.9 | 13.1 |
| Gui Santos | 91% | 18.6<br><sub>-,12,21,12,21</sub> | 8.2<br><sub>-,3,3,0,7</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>-,1,7,3,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>-,0,4,1,1</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.7 | 0.4 | 1.2 | 13.9 |
| Gary Payton II | 83% | 15.8<br><sub>10,13,-,-,13</sub> | 7.6<br><sub>9,4,-,-,2</sub> |  | 2.8<br><sub>0,0,-,-,2</sub> |  | 1.3<br><sub>0,0,-,-,0</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 11.8 |
| Charles Bassey | 98% | 15.2<br><sub>14,11,18,13,20</sub> | 7.8<br><sub>8,8,12,7,11</sub> |  | 6.5<br><sub>7,4,10,6,5</sub> |  | 0.8<br><sub>0,0,1,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.2 | 1.0 | 15.1 |
| Graham Ike | 91% | 11.1<br><sub>1,-,12,4,13</sub> | 4.8<br><sub>0,-,4,4,5</sub> |  | 2.7<br><sub>1,-,5,0,2</sub> |  | 1.2<br><sub>0,-,2,1,3</sub> |  | 0.3<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.4 | 0.6 | 8.7 |
| Malevy Leons | 64% | 9.7<br><sub>1,-,12,4,14</sub> | 2.9<br><sub>0,-,0,0,5</sub> |  | 1.8<br><sub>0,-,3,3,1</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.5 | 0.4 | 0.5 | 5.3 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 100% | 35.2<br><sub>26,24,29,35,41</sub> | 19.0<br><sub>13,9,15,30,16</sub> | 18.5 · 18.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>4,0,1,10,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>3,4,2,0,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>1,1,3,6,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 1.5 | 27.8 |
| Zion Williamson | 100% | 33.9<br><sub>31,-,30,33,31</sub> | 22.0<br><sub>25,-,29,22,24</sub> | 21.5 · 21.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>2,-,2,4,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.4<br><sub>0,-,1,0,2</sub> |  | 1.4 | 0.7 | 2.5 | 32.1 |
| Jeremiah Fears | 100% | 32.5<br><sub>29,29,28,34,33</sub> | 18.2<br><sub>25,11,14,18,13</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>6,3,4,5,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 6.0<br><sub>5,8,5,7,7</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>3,1,2,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 0.6 | 3.0 | 29.0 |
| Herbert Jones | 100% | 28.1<br><sub>20,24,25,32,27</sub> | 8.9<br><sub>4,10,2,8,10</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>0,6,2,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>1,1,3,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>0,2,0,0,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.5 | 1.4 | 14.6 |
| Derik Queen | 98% | 25.9<br><sub>21,21,14,23,25</sub> | 13.0<br><sub>8,16,9,10,10</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>5,4,0,6,5</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 3.5<br><sub>3,0,0,2,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.5<br><sub>0,0,1,0,2</sub> |  | 1.1 | 1.0 | 2.5 | 23.7 |
| Yves Missi | 100% | 24.2<br><sub>-,-,-,-,22</sub> | 7.4<br><sub>-,-,-,-,3</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>-,-,-,-,8</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 1.9 | 1.1 | 16.9 |
| Jordan Poole | 72% | 23.1<br><sub>-,34,21,21,24</sub> | 11.5<br><sub>-,7,14,13,14</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>-,3,0,2,2</sub> |  | 3.4<br><sub>-,2,1,5,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>-,1,2,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 0.4 | 1.8 | 17.2 |
| Karlo Matkovic | 97% | 21.6<br><sub>19,17,22,19,14</sub> | 8.1<br><sub>3,4,4,1,5</sub> |  | 4.9<br><sub>3,6,4,3,3</sub> |  | 1.3<br><sub>2,2,1,0,1</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 0.7 | 0.9 | 1.0 | 14.3 |
| Jaron Pierre Jr. | 91% | 17.2<br><sub>-,-,7,4,23</sub> | 7.4<br><sub>-,-,4,0,13</sub> |  | 2.5<br><sub>-,-,4,0,2</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,1,0,2</sub> |  | 0.7 | 0.3 | 1.2 | 10.9 |
| DeAndre Jordan | 48% | 14.3<br><sub>-,-,11,17,-</sub> | 3.9<br><sub>-,-,0,6,-</sub> |  | 5.7<br><sub>-,-,3,8,-</sub> |  | 0.8<br><sub>-,-,0,1,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.7 | 0.7 | 10.4 |
| Julian Reese | 58% | 8.3<br><sub>3,9,7,4,-</sub> | 2.4<br><sub>0,2,2,0,-</sub> |  | 1.6<br><sub>0,0,2,2,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.6 | 4.5 |
| AJ Johnson | 52% | 8.2<br><sub>3,12,7,4,-</sub> | 2.3<br><sub>2,2,2,1,-</sub> |  | 1.2<br><sub>0,2,1,0,-</sub> |  | 0.8<br><sub>0,3,0,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.6 | 4.2 |
| Malik Dia | 52% | 7.0<br><sub>-,-,-,4,-</sub> | 2.4<br><sub>-,-,-,2,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.9<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.6 |

</details>


### PHX @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN), Mark Williams (PHX)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.4–119.2 | PHX 26% | 3.78 / 1.36 | DEN -8.5 | 229.5 | DEN -9.5 covers 48%; o229.5 50% |
| Expected (weighted by chance each plays) | 110.6–119.1 | PHX 27% | 3.70 / 1.37 | DEN -8.5 | 229.5 | DEN -9.5 covers 47%; o229.5 51% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Dunn (PHX) | Questionable | 55% | 17.6 | 5.2 | 3.7 | 1.3 | 0.6 | 0.6 | 0.4 | 0.5 | 10.1 | small |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 35.0<br><sub>39,29,29,35,28</sub> | 23.0<br><sub>24,32,17,30,17</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,2,3,1,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 6.2<br><sub>3,4,5,7,7</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,3,2,4,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 2.5 | 32.6 |
| Dillon Brooks | 98% | 29.9<br><sub>37,26,22,30,22</sub> | 15.3<br><sub>11,7,8,15,1</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>4,4,4,3,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>1,0,2,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>3,1,0,3,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.3 | 20.7 |
| Miles Bridges | 98% | 28.5<br><sub>31,26,18,25,24</sub> | 14.2<br><sub>13,7,8,11,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>10,5,4,6,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>7,0,2,3,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.4 | 1.0 | 22.9 |
| Jalen Green | 98% | 26.6<br><sub>34,24,21,21,21</sub> | 13.3<br><sub>16,6,13,12,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>3,5,5,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.7<br><sub>6,4,1,0,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>0,0,3,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.3 | 1.9 | 19.6 |
| Collin Gillespie | 98% | 25.9<br><sub>20,24,22,27,28</sub> | 9.9<br><sub>7,6,12,13,26</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>3,2,2,2,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>4,3,8,1,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>1,2,4,3,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.2 | 1.0 | 17.0 |
| Oso Ighodaro | 98% | 23.6<br><sub>23,18,20,32,17</sub> | 6.4<br><sub>4,7,6,2,4</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,4,8,3,2</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 3.2<br><sub>3,2,2,7,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 1.1 | 14.9 |
| Jordan Goodwin | 98% | 23.1<br><sub>-,-,14,24,31</sub> | 9.0<br><sub>-,-,18,6,14</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>-,-,3,5,7</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>-,-,1,2,6</sub> |  | 1.4<br><sub>-,-,6,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.2 | 0.8 | 15.9 |
| Luke Kennard | 98% | 20.4<br><sub>14,14,22,21,23</sub> | 8.0<br><sub>11,3,14,8,18</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>1,1,1,1,6</sub> |  | 2.0<br><sub>2,0,3,1,4</sub> |  | 1.1<br><sub>3,1,3,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.6 | 0.1 | 0.7 | 12.2 |
| Khaman Maluach | 98% | 17.0<br><sub>18,20,22,16,13</sub> | 5.8<br><sub>8,11,11,4,7</sub> |  | 5.1<br><sub>10,5,7,2,4</sub> |  | 0.8<br><sub>0,2,3,1,0</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.8 | 0.8 | 11.6 |
| Rasheer Fleming | 48% | 10.1<br><sub>-,9,12,-,-</sub> | 3.7<br><sub>-,2,4,-,-</sub> |  | 1.8<br><sub>-,1,2,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.4 | 0.3 | 0.4 | 5.7 |
| Koa Peat | 63% | 9.2<br><sub>-,6,6,-,8</sub> | 4.4<br><sub>-,4,5,-,10</sub> |  | 2.0<br><sub>-,0,1,-,2</sub> |  | 0.4<br><sub>-,1,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.9 |
| Drew Timme | 8% | 8.7 | 3.3 |  | 1.4 |  | 0.8 |  | 0.2 |  | 0.3 | 0.1 | 0.5 | 5.5 |
| Jamaree Bouyea | 52% | 8.2<br><sub>-,9,8,-,-</sub> | 3.2<br><sub>-,4,7,-,-</sub> |  | 1.1<br><sub>-,0,1,-,-</sub> |  | 1.3<br><sub>-,3,3,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.6 |
| Pat Spencer | 58% | 7.9<br><sub>-,6,-,-,-</sub> | 2.9<br><sub>-,2,-,-,-</sub> |  | 1.0<br><sub>-,2,-,-,-</sub> |  | 1.3<br><sub>-,2,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Duop Reath | 52% | 7.7<br><sub>-,6,-,-,-</sub> | 3.1<br><sub>-,2,-,-,-</sub> |  | 1.6<br><sub>-,2,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 5.1 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 36.6<br><sub>30,36,39,37,37</sub> | 26.6<br><sub>32,19,25,27,26</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 12.9<br><sub>10,13,16,11,8</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 10.5<br><sub>11,8,9,8,10</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.8 | 3.7 | 50.0 |
| Jamal Murray | 98% | 36.4<br><sub>28,34,39,32,38</sub> | 25.1<br><sub>14,16,38,30,23</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,6,2,4,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 6.7<br><sub>7,8,2,8,9</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>2,2,5,4,0</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.6 | 2.6 | 36.6 |
| Christian Braun | 98% | 32.6<br><sub>28,29,32,37,28</sub> | 12.8<br><sub>11,6,4,12,17</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>3,4,5,5,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>3,1,3,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.4 | 1.1 | 19.8 |
| Cameron Johnson | 98% | 30.2<br><sub>30,29,31,30,31</sub> | 13.0<br><sub>12,18,8,23,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>2,4,2,4,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,1,1,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.8<br><sub>4,2,2,4,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.3 | 1.1 | 19.6 |
| Aaron Gordon | 98% | 29.9<br><sub>25,27,30,27,33</sub> | 13.4<br><sub>17,12,3,9,11</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>1,5,5,3,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>0,0,2,2,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.4 | 1.3 | 21.4 |
| DeMar DeRozan | 88% | 22.7<br><sub>-,22,19,20,24</sub> | 11.4<br><sub>-,11,7,8,9</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>-,1,4,1,3</sub> |  | 3.1<br><sub>-,5,2,4,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.3 | 1.2 | 16.8 |
| Trevon Brazile | 98% | 16.1<br><sub>23,14,14,13,16</sub> | 5.2<br><sub>6,3,5,7,5</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>7,4,2,5,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>1,2,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 9.9 |
| Spencer Jones | 80% | 13.8<br><sub>-,21,14,22,12</sub> | 3.9<br><sub>-,13,0,3,4</sub> |  | 2.0<br><sub>-,6,0,1,2</sub> |  | 0.7<br><sub>-,0,1,0,1</sub> |  | 0.4<br><sub>-,3,0,1,0</sub> |  | 0.4 | 0.3 | 0.5 | 6.6 |
| Marvin Bagley III | 98% | 13.2<br><sub>14,12,12,12,13</sub> | 6.5<br><sub>10,10,6,4,7</sub> |  | 4.1<br><sub>2,3,3,2,7</sub> |  | 0.7<br><sub>2,0,0,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 11.3 |
| Tyus Jones | 97% | 9.8<br><sub>18,13,6,11,10</sub> | 2.6<br><sub>6,3,2,0,2</sub> |  | 1.0<br><sub>1,4,0,1,0</sub> |  | 1.8<br><sub>8,4,0,4,3</sub> |  | 0.2<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.3 |
| Bryce Hopkins | 52% | 8.2<br><sub>28,3,3,-,-</sub> | 2.7<br><sub>18,3,2,-,-</sub> |  | 1.2<br><sub>4,1,0,-,-</sub> |  | 0.4<br><sub>1,0,0,-,-</sub> |  | 0.1<br><sub>1,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Zeke Nnaji | 30% | 6.8<br><sub>4,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 1.5<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.0 |
| Alpha Diallo | 52% | 6.2<br><sub>4,-,1,-,-</sub> | 2.5<br><sub>0,-,0,-,-</sub> |  | 1.0<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-16/`._
