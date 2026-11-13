# NBA model · Thu 12 Nov 2026 (US date)

Updated **Fri 13 Nov, 11:23 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-12/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ryan Kalkbrenner PR over 19.5 (20+) | CHA @ PHX | draftkings | 13.00 | 11.20 | 4.91 | 20.4% | 7.2% | 8.9% | +16.1% | +164.8% | 0.3% |
| Ryan Kalkbrenner REB over 9.5 (10+) | CHA @ PHX | draftkings | 11.80 | 10.66 | 5.26 | 19.0% | 7.9% | 9.4% | +10.7% | +124.2% | 0.2% |
| Ryan Kalkbrenner REB over 11.5 (12+) | CHA @ PHX | draftkings | 25.00 | 22.94 | 11.82 | 8.5% | 3.7% | 4.4% | +9.0% | +111.5% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| DAL @ MIN | Fri 13 Nov 12:00 | 112.5–117.3 | DAL 37% | 2.74 / 1.58 | MIN -4.5 | 229.5 | MIN -5.5 covers 48%; o225.5 59% |
| CHA @ PHX | Fri 13 Nov 13:00 | 108.1–111.6 | CHA 40% | 2.49 / 1.67 | PHX -3.5 | 219.5 | PHX -6.5 covers 42%; o214.5 60% |

### DAL @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Sergio de Larrea (DAL), Dereck Lively II (DAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naji Marshall PTS over 9.5 (10+) | DAL @ MIN | draftkings | 2.18 | 2.15 | 1.74 | 57.5% | 44.8% | 46.5% | +1.3% | +25.3% | 0.3% |
| Naji Marshall PTS over 8.5 (9+) | DAL @ MIN | draftkings | 1.88 | 1.86 | 1.54 | 65.1% | 52.0% | 53.7% | +0.9% | +22.1% | 0.2% |
| Jaden McDaniels PTS under 17.5 | DAL @ MIN | tab | 1.90 | 1.89 | 1.68 | 59.4% | 52.0% | 53.0% | +0.8% | +13.0% | 0.2% |
| Kyrie Irving PTS under 22.5 | DAL @ MIN | sportsbet | 1.96 | 1.95 | 1.72 | 58.3% | 50.1% | 51.2% | +0.4% | +14.3% | 0.1% |
| Jonathan Kuminga PTS under 13.5 | DAL @ MIN | pointsbetau | 2.00 | 1.99 | 1.85 | 53.9% | 49.6% | 50.2% | +0.4% | +7.9% | 0.1% |

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 33.4<br><sub>40,40,33,28,39</sub> | 23.0<br><sub>17,19,21,25,43</sub> | 24.5 · 24.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>4,10,10,5,10</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>6,5,7,12,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>0,0,1,3,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.9 | 2.8 | 34.9 |
| Kyrie Irving | 98% | 33.3<br><sub>-,36,28,29,38</sub> | 21.8<br><sub>-,29,14,21,35</sub> | 22.5 · 22.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>-,7,2,3,0</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>-,5,2,4,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>-,5,0,2,7</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.4 | 2.2 | 30.0 |
| P.J. Washington | 98% | 31.3<br><sub>38,39,33,25,35</sub> | 13.2<br><sub>12,21,26,6,13</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>5,10,6,5,9</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,3,1,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>2,3,6,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.9 | 1.6 | 21.3 |
| Naji Marshall | 91% | 23.6<br><sub>24,26,25,15,25</sub> | 11.3<br><sub>5,22,7,8,6</sub> | 8.5 · 8.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>2,5,1,1,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.0<br><sub>7,3,5,2,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>0,3,0,1,0</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.2 | 1.6 | 17.7 |
| Daniel Gafford | 98% | 20.0<br><sub>26,18,18,19,20</sub> | 8.9<br><sub>20,2,7,18,8</sub> | 7.5 · 7.5<br><sub>o 54% · u 46%</sub> | 5.7<br><sub>7,4,1,5,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,1,2,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.4 | 1.1 | 15.8 |
| Zaccharie Risacher | 96% | 17.5<br><sub>19,18,21,16,15</sub> | 5.5<br><sub>0,2,4,11,4</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>5,1,4,6,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8<br><sub>1,2,1,1,0</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.6 | 0.8 | 9.6 |
| Walter Clayton Jr. | 91% | 16.8<br><sub>24,21,23,16,25</sub> | 6.4<br><sub>20,8,12,5,6</sub> |  | 3.1<br><sub>1,6,4,4,6</sub> |  | 2.9<br><sub>2,5,2,6,4</sub> |  | 0.7<br><sub>4,2,1,1,1</sub> |  | 0.6 | 0.2 | 1.2 | 12.4 |
| Santi Aldama | 98% | 16.3<br><sub>-,-,13,15,19</sub> | 7.7<br><sub>-,-,8,12,10</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>-,-,9,2,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>-,-,1,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8<br><sub>-,-,0,2,1</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 0.5 | 0.4 | 1.0 | 12.7 |
| Caleb Martin | 98% | 14.7<br><sub>21,20,11,19,19</sub> | 3.3<br><sub>5,0,0,2,0</sub> | 3.5 · –<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>6,3,0,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>0,2,0,2,5</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.2<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 33% · u 67%</sub> | 0.6 | 0.2 | 0.6 | 6.6 |
| Max Christie | 98% | 12.3<br><sub>8,-,9,17,5</sub> | 4.1<br><sub>0,-,0,5,0</sub> |  | 1.4<br><sub>2,-,1,2,2</sub> |  | 0.7<br><sub>0,-,1,0,0</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.2 |
| Morez Johnson Jr. | 98% | 11.2<br><sub>17,18,24,19,-</sub> | 4.3<br><sub>13,8,13,4,-</sub> | 6.5 · – | 2.3<br><sub>2,3,17,9,-</sub> | 4.5 | 0.9<br><sub>1,1,2,1,-</sub> | 1.5 | 0.2<br><sub>0,1,1,0,-</sub> | 0.5 | 0.3 | 0.1 | 0.7 | 7.5 |
| Marcus Sasser | 64% | 8.6<br><sub>19,5,-,9,-</sub> | 3.0<br><sub>4,0,-,4,-</sub> |  | 0.8<br><sub>1,1,-,0,-</sub> |  | 1.0<br><sub>1,2,-,0,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.8 |
| Moussa Cisse | 58% | 6.7<br><sub>2,-,1,5,-</sub> | 2.6<br><sub>0,-,0,2,-</sub> |  | 2.5<br><sub>0,-,0,1,-</sub> |  | 0.2<br><sub>0,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.3 |
| Tobi Lawal | 58% | 6.1<br><sub>2,-,1,5,-</sub> | 2.4<br><sub>2,-,0,2,-</sub> |  | 2.1<br><sub>0,-,0,0,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |
| Jett Howard | 58% | 5.8<br><sub>2,-,1,3,-</sub> | 2.5<br><sub>2,-,0,5,-</sub> |  | 0.7<br><sub>0,-,0,1,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>0,-,0,1,-</sub> |  | 0.1 | 0.1 | 0.3 | 3.6 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 32.6<br><sub>39,29,37,40,33</sub> | 16.7<br><sub>19,13,14,23,16</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>3,6,8,6,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,3,4,5,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>2,2,0,2,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 1.0 | 1.7 | 25.4 |
| Ayo Dosunmu | 98% | 31.0<br><sub>38,37,34,39,30</sub> | 18.0<br><sub>27,19,21,26,26</sub> | 18.5 · 17.5<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>9,12,1,2,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>3,8,6,4,1</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>2,1,0,4,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.4 | 1.8 | 26.6 |
| Jonathan Kuminga | 98% | 29.0<br><sub>40,33,32,34,25</sub> | 13.7<br><sub>19,8,16,17,4</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>6,10,8,8,0</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>3,3,5,4,0</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>2,2,4,1,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.6 | 1.5 | 21.6 |
| Rudy Gobert | 98% | 29.0<br><sub>-,31,33,25,31</sub> | 9.4<br><sub>-,10,8,8,10</sub> | 8.5 · 9.5<br><sub>o 48% · u 52%</sub> | 11.3<br><sub>-,10,11,11,15</sub> | 11.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>-,1,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.4 | 22.5 |
| LaMelo Ball | 98% | 28.9<br><sub>20,33,31,35,30</sub> | 21.0<br><sub>10,34,20,22,24</sub> | 20.5 · 20.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>8,6,2,2,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.5<br><sub>4,3,6,8,5</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>0,6,4,3,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.2 | 3.1 | 31.7 |
| Terrence Shannon Jr. | 98% | 20.5<br><sub>18,-,-,-,18</sub> | 11.0<br><sub>2,-,-,-,5</sub> | 9.5 · 9.5<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,-,-,-,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>4,-,-,-,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,-,-,-,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.1 | 1.2 | 15.6 |
| Trey Lyles | 98% | 20.2<br><sub>17,21,20,29,21</sub> | 6.9<br><sub>6,12,5,5,9</sub> | 5.5 · 5.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>0,4,2,13,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>0,0,0,2,2</sub> |  | 0.9<br><sub>1,2,1,0,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.6 | 0.3 | 0.6 | 12.8 |
| Jaylen Clark | 91% | 17.7<br><sub>20,21,25,21,19</sub> | 5.9<br><sub>10,4,10,8,3</sub> | 4.5 · –<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,4,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0<br><sub>1,0,1,0,0</sub> |  | 0.7<br><sub>2,1,2,1,0</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 0.5 | 9.3 |
| Joan Beringer | 97% | 14.5<br><sub>34,14,13,7,16</sub> | 6.4<br><sub>12,2,4,2,4</sub> |  | 5.1<br><sub>6,7,7,3,3</sub> |  | 0.6<br><sub>2,2,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 12.1 |
| Bones Hyland | 98% | 14.3<br><sub>14,14,16,10,13</sub> | 8.7<br><sub>6,10,19,4,14</sub> |  | 1.6<br><sub>1,1,2,1,2</sub> |  | 2.5<br><sub>3,3,4,0,2</sub> |  | 1.2<br><sub>0,2,4,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 12.8 |
| Rocco Zikarsky | 48% | 7.1<br><sub>-,-,-,-,2</sub> | 2.6<br><sub>-,-,-,-,0</sub> |  | 2.4<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.6 | 0.4 | 5.4 |
| Zyon Pullin | 38% | 6.2<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.5 |
| Cody Williams | 52% | 5.9<br><sub>-,7,-,-,2</sub> | 0.3<br><sub>-,0,-,-,0</sub> |  | 1.7<br><sub>-,1,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 2.4 |
| Isaiah Evans | 52% | 5.5<br><sub>-,-,-,-,2</sub> | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 1.9 |

</details>


### CHA @ PHX
Out: Mark Williams (PHX), Kon Knueppel (CHA), Brandon Miller (CHA), Dennis Schroder (CHA), Hannes Steinbach (CHA)

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Grayson Allen | 98% | 31.2<br><sub>30,19,27,22,34</sub> | 17.9<br><sub>27,11,22,0,27</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,1,2,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>3,0,4,3,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>7,3,5,0,6</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.3 | 2.2 | 25.4 |
| Naz Reid | 98% | 31.1<br><sub>36,27,36,26,32</sub> | 19.8<br><sub>14,13,28,14,25</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>5,6,9,6,13</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>2,2,2,2,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>0,2,2,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.8 | 2.7 | 30.2 |
| Sion James | 98% | 29.9<br><sub>18,21,31,21,33</sub> | 8.6<br><sub>4,11,10,11,11</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,4,2,3,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>1,3,1,0,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,3,0,3,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.3 | 16.0 |
| Moussa Diabate | 98% | 29.0<br><sub>28,24,29,-,-</sub> | 9.0<br><sub>10,7,7,-,-</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 9.4<br><sub>8,9,6,-,-</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>3,2,2,-,-</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.0<br><sub>0,0,0,-,-</sub> |  | 1.1 | 1.0 | 1.7 | 20.9 |
| Ryan Kalkbrenner | 98% | 25.0<br><sub>19,16,19,21,35</sub> | 8.0<br><sub>6,4,6,4,8</sub> | 4.5 · –<br><sub>o 55% · u 45%</sub> | 6.8<br><sub>3,6,4,5,15</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>4,0,2,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.5 | 1.3 | 16.4 |
| Royce O'Neale | 98% | 23.9<br><sub>23,18,18,26,23</sub> | 7.5<br><sub>8,2,0,7,10</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>6,4,3,4,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,0,2,2,1</sub> |  | 1.3<br><sub>1,0,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.3 | 0.9 | 13.4 |
| Coby White | 98% | 22.6<br><sub>-,16,18,16,20</sub> | 16.0<br><sub>-,7,4,7,10</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>-,0,5,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>-,3,2,1,9</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>-,1,0,1,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 2.5 | 23.1 |
| Grant Williams | 58% | 18.8<br><sub>-,-,-,-,-</sub> | 6.8<br><sub>-,-,-,-,-</sub> |  | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.5 | 1.2 | 11.8 |
| Tidjane Salaun | 96% | 18.7<br><sub>12,19,10,23,18</sub> | 7.2<br><sub>5,1,9,13,14</sub> |  | 4.2<br><sub>2,7,1,4,3</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>1,0,3,2,3</sub> |  | 0.6 | 0.2 | 0.9 | 12.3 |
| Christian Anderson | 86% | 17.1<br><sub>8,9,-,25,16</sub> | 6.8<br><sub>2,8,-,4,9</sub> |  | 2.2<br><sub>0,2,-,3,1</sub> |  | 2.2<br><sub>0,2,-,5,1</sub> |  | 0.9<br><sub>0,1,-,0,3</sub> |  | 0.5 | 0.3 | 1.9 | 11.2 |
| Liam McNeeley | 64% | 16.8<br><sub>-,9,-,19,16</sub> | 6.9<br><sub>-,3,-,8,8</sub> |  | 3.1<br><sub>-,0,-,2,1</sub> |  | 1.3<br><sub>-,1,-,3,1</sub> |  | 0.8<br><sub>-,0,-,1,2</sub> |  | 0.5 | 0.1 | 0.9 | 11.3 |
| PJ Hall | 38% | 8.8<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.7 | 7.0 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.1<br><sub>34,34,39,29,29</sub> | 24.5<br><sub>33,30,24,32,17</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,1,2,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.7<br><sub>2,8,3,4,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>2,4,2,3,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.3 | 2.8 | 33.7 |
| Dillon Brooks | 98% | 29.8<br><sub>35,29,37,26,22</sub> | 15.9<br><sub>15,24,11,7,8</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>6,1,4,4,4</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>2,1,1,0,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,4,3,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.2 | 1.4 | 21.4 |
| Miles Bridges | 98% | 28.4<br><sub>31,31,31,26,18</sub> | 13.5<br><sub>18,18,13,7,8</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>7,13,10,5,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>5,5,7,0,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>4,3,1,0,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.5 | 1.1 | 22.1 |
| Jalen Green | 98% | 27.6<br><sub>32,24,34,24,21</sub> | 14.6<br><sub>22,6,16,6,13</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>2,0,3,5,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>2,3,6,4,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>2,0,0,0,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.3 | 2.1 | 21.4 |
| Collin Gillespie | 98% | 22.7<br><sub>23,24,20,24,22</sub> | 8.4<br><sub>2,6,7,6,12</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>3,2,3,2,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>2,2,4,3,8</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.1 | 1.0 | 14.8 |
| Oso Ighodaro | 98% | 21.5<br><sub>23,24,23,18,20</sub> | 6.4<br><sub>9,2,4,7,6</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>7,5,6,4,8</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.5<br><sub>7,1,3,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.7 | 1.2 | 14.0 |
| Ryan Dunn | 98% | 19.0<br><sub>18,25,23,23,25</sub> | 5.6<br><sub>2,11,8,3,10</sub> |  | 3.9<br><sub>6,3,5,2,8</sub> |  | 1.3<br><sub>2,3,3,0,2</sub> |  | 0.6<br><sub>0,1,2,1,1</sub> |  | 0.8 | 0.4 | 0.6 | 10.8 |
| Khaman Maluach | 98% | 17.8<br><sub>16,22,18,20,22</sub> | 6.1<br><sub>6,8,8,11,11</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>6,6,10,5,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>2,2,0,2,3</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 1.0 | 1.0 | 12.0 |
| Luke Kennard | 98% | 17.5<br><sub>14,21,14,14,22</sub> | 6.8<br><sub>0,12,11,3,14</sub> |  | 1.8<br><sub>0,1,1,1,1</sub> |  | 1.8<br><sub>1,5,2,0,3</sub> |  | 0.9<br><sub>0,3,3,1,3</sub> |  | 0.6 | 0.1 | 0.6 | 10.4 |
| Jordan Goodwin | 98% | 15.9<br><sub>-,-,-,-,14</sub> | 6.4<br><sub>-,-,-,-,18</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>-,-,-,-,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>-,-,-,-,1</sub> |  | 1.0<br><sub>-,-,-,-,6</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.1 | 0.6 | 11.1 |
| Rasheer Fleming | 58% | 9.2<br><sub>-,-,-,9,12</sub> | 3.4<br><sub>-,-,-,2,4</sub> |  | 1.5<br><sub>-,-,-,1,2</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.4 | 5.2 |
| Jamaree Bouyea | 67% | 7.3<br><sub>3,2,-,9,8</sub> | 2.9<br><sub>3,0,-,4,7</sub> |  | 0.9<br><sub>0,0,-,0,1</sub> |  | 1.2<br><sub>0,0,-,3,3</sub> |  | 0.2<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |
| Koa Peat | 66% | 6.9<br><sub>3,2,-,6,6</sub> | 2.7<br><sub>2,0,-,4,5</sub> |  | 1.3<br><sub>1,1,-,0,1</sub> |  | 0.3<br><sub>0,0,-,1,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 4.3 |
| Pat Spencer | 67% | 6.9<br><sub>3,2,-,6,-</sub> | 2.4<br><sub>0,0,-,2,-</sub> |  | 0.9<br><sub>0,0,-,2,-</sub> |  | 1.1<br><sub>2,0,-,2,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Drew Timme | 16% | 6.3 | 2.5 |  | 1.0 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Duop Reath | 67% | 6.2<br><sub>7,2,-,6,-</sub> | 2.6<br><sub>7,0,-,2,-</sub> |  | 1.2<br><sub>0,0,-,2,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.2<br><sub>1,0,-,0,-</sub> |  | 0.1 | 0.2 | 0.2 | 4.1 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-12/`._
