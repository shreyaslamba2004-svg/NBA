# NBA model · Tue 17 Nov 2026 (US date)

Updated **Wed 18 Nov, 07:16 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-17/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| TOR to win | NYK @ TOR | draftkings | 2.50 | 2.35 | 2.84 | 35.3% | 42.6% | 42.6% | +6.6% | -11.8% | 1.1% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul Reed REB over 13.5 (14+) | DET @ SAS | draftkings | 20.80 | 19.46 | 11.49 | 8.7% | 4.5% | 5.1% | +6.9% | +81.0% | 0.1% |
| Paul Reed REB over 11.5 (12+) | DET @ SAS | draftkings | 9.50 | 8.94 | 5.38 | 18.6% | 9.8% | 11.2% | +6.2% | +76.5% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| NYK @ TOR | Wed 18 Nov 11:30 | 112.7–106.8 | NYK 66% | 1.51 / 2.94 | TOR +5.5 | 219.5 | TOR +4.5 covers 46%; o214.5 60% |
| POR @ MIN | Wed 18 Nov 12:00 | 108.0–112.5 | POR 37% | 2.70 / 1.59 | MIN -4.5 | 220.5 | MIN -3.5 covers 54%; o225.5 39% |
| DET @ SAS | Wed 18 Nov 12:00 | 107.4–113.5 | DET 33% | 3.03 / 1.49 | SAS -6.5 | 220.5 | SAS -9.5 covers 41%; o222.5 46% |
| CHA @ LAL | Wed 18 Nov 15:00 | 107.4–111.9 | CHA 38% | 2.66 / 1.60 | LAL -4.5 | 219.5 | LAL -7.5 covers 42%; o221.5 45% |
| UTA @ LAC | Wed 18 Nov 14:30 | 108.6–123.2 | UTA 15% | 6.72 / 1.17 | LAC -14.5 | 231.5 | LAC -6.5 covers 72%; o225.5 64% |

### NYK @ TOR
Out: Kawhi Leonard (TOR), Malachi Smith (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.7–106.8 | NYK 66% | 1.51 / 2.94 | TOR +5.5 | 219.5 | TOR +4.5 covers 46%; o214.5 60% |
| Expected (weighted by chance each plays) | 112.6–107.2 | NYK 65% | 1.54 / 2.84 | TOR +5.5 | 219.5 | TOR +4.5 covers 47%; o214.5 61% |
| if Scottie Barnes plays | 112.5–107.5 | NYK 64% | 1.57 / 2.75 | TOR +4.5 | 219.5 | TOR +4.5 covers 49%; o214.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes (TOR) | Questionable | 55% | 33.4 | 19.7 | 6.8 | 6.2 | 0.9 | 1.4 | 1.1 | 2.8 | 32.7 | full tables below |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 35.4<br><sub>34,28,35,36,41</sub> | 26.4<br><sub>31,23,27,33,28</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>6,4,3,1,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>9,2,5,11,9</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,1,3,4,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 2.9 | 35.8 |
| OG Anunoby | 98% | 34.4<br><sub>34,29,34,33,44</sub> | 17.3<br><sub>15,19,14,11,21</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,3,6,2,9</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>2,2,2,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,5,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.9 | 2.0 | 24.4 |
| Karl-Anthony Towns | 98% | 33.8<br><sub>34,27,34,34,43</sub> | 19.9<br><sub>29,21,21,23,28</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 13.0<br><sub>13,16,11,15,17</sub> | 12.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,3,8,5,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>2,2,2,3,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.7 | 3.1 | 36.6 |
| Josh Hart | 98% | 28.4<br><sub>-,-,26,23,26</sub> | 8.4<br><sub>-,-,6,0,0</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>-,-,4,5,5</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.5<br><sub>-,-,3,4,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.3 | 1.6 | 18.2 |
| Mikal Bridges | 98% | 26.6<br><sub>31,17,17,29,32</sub> | 9.4<br><sub>9,4,2,18,5</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>6,5,1,3,7</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>4,1,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>1,0,0,2,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.5 | 1.1 | 14.8 |
| Landry Shamet | 98% | 24.6<br><sub>29,28,29,21,30</sub> | 9.1<br><sub>9,10,12,5,23</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,3,2,3,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3<br><sub>1,2,4,1,0</sub> |  | 1.5<br><sub>3,2,2,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 0.9 | 12.2 |
| Miles McBride | 98% | 17.6<br><sub>16,25,27,22,14</sub> | 6.3<br><sub>5,8,19,9,3</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,0,2,1,1</sub> |  | 1.2<br><sub>0,3,2,1,0</sub> |  | 1.0<br><sub>1,2,5,3,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.2 | 0.6 | 8.9 |
| Tyler Kolek | 91% | 14.0<br><sub>14,15,13,19,16</sub> | 4.2<br><sub>0,12,4,5,0</sub> |  | 1.8<br><sub>4,3,1,6,0</sub> |  | 3.6<br><sub>5,4,4,2,7</sub> |  | 0.5<br><sub>0,2,0,1,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.7 |
| Andre Drummond | 98% | 11.9<br><sub>14,16,14,14,7</sub> | 3.6<br><sub>0,2,0,0,2</sub> |  | 5.4<br><sub>8,14,4,6,3</sub> |  | 0.8<br><sub>0,3,3,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.8 |
| Jordan Clarkson | 84% | 10.0<br><sub>15,11,-,9,7</sub> | 4.6<br><sub>9,2,-,0,2</sub> |  | 1.4<br><sub>2,4,-,1,2</sub> |  | 0.7<br><sub>0,2,-,0,0</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.7 |
| Tyler Nickel | 38% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Mohamed Diawara | 52% | 8.1<br><sub>14,18,11,-,-</sub> | 2.8<br><sub>2,5,2,-,-</sub> |  | 1.3<br><sub>3,3,0,-,-</sub> |  | 0.8<br><sub>3,3,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Jose Alvarado | 58% | 7.4<br><sub>-,6,-,-,2</sub> | 2.9<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,1,-,-,0</sub> |  | 1.2<br><sub>-,1,-,-,1</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.0 |
| Jaden Akins | 38% | 6.8<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.0 |
| Dalton Knecht | 64% | 6.7<br><sub>5,8,-,-,-</sub> | 2.9<br><sub>0,3,-,-,-</sub> |  | 1.3<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.6 |
| James Wiseman | 52% | 6.2<br><sub>-,5,-,-,3</sub> | 2.2<br><sub>-,0,-,-,0</sub> |  | 2.1<br><sub>-,1,-,-,3</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.1 | 0.3 | 0.5 | 4.6 |
| Pacome Dadiet | 52% | 6.0<br><sub>-,6,-,1,-</sub> | 2.7<br><sub>-,8,-,0,-</sub> |  | 1.1<br><sub>-,2,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,1,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 98% | 35.7<br><sub>37,36,31,37,37</sub> | 22.6<br><sub>27,19,12,31,14</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 6.4<br><sub>7,3,8,14,5</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>5,2,7,5,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,1,0,4,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.4 | 2.7 | 33.6 |
| Immanuel Quickley | 88% | 33.0<br><sub>-,-,28,28,38</sub> | 18.0<br><sub>-,-,11,26,17</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>-,-,4,4,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>-,-,4,6,6</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>-,-,1,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.1 | 1.7 | 28.2 |
| Ja'Kobe Walter | 98% | 32.8<br><sub>29,34,35,32,36</sub> | 12.2<br><sub>7,12,17,6,7</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>6,6,3,5,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,0,1,0,1</sub> |  | 2.2<br><sub>1,2,5,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.3 | 1.1 | 17.9 |
| Collin Murray-Boyles | 98% | 31.6<br><sub>34,-,20,32,40</sub> | 13.5<br><sub>19,-,5,14,6</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>7,-,4,0,13</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,-,3,4,2</sub> |  | 0.5<br><sub>0,-,1,1,0</sub> |  | 1.2 | 1.3 | 1.9 | 22.7 |
| Jamal Shead | 98% | 25.9<br><sub>34,36,22,22,26</sub> | 9.0<br><sub>10,20,3,5,19</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>3,2,3,1,2</sub> |  | 6.2<br><sub>16,11,6,5,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>1,4,0,1,3</sub> |  | 1.0 | 0.2 | 1.9 | 17.2 |
| Jakob Poeltl | 91% | 24.4<br><sub>31,31,32,25,17</sub> | 9.7<br><sub>19,18,6,9,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>11,8,9,5,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,2,1,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.3 | 18.4 |
| Jamison Battle | 98% | 19.9<br><sub>21,29,25,25,8</sub> | 8.7<br><sub>6,18,12,13,0</sub> |  | 2.4<br><sub>2,1,2,1,3</sub> |  | 0.8<br><sub>0,2,0,1,0</sub> |  | 1.4<br><sub>1,5,2,3,0</sub> |  | 0.3 | 0.2 | 0.6 | 11.8 |
| Allen Graves | 98% | 16.8<br><sub>16,13,18,13,16</sub> | 5.5<br><sub>3,3,13,0,2</sub> |  | 2.9<br><sub>2,2,5,2,5</sub> |  | 1.1<br><sub>0,1,0,0,3</sub> |  | 0.6<br><sub>0,1,3,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 9.4 |
| Alijah Martin | 93% | 14.1<br><sub>31,21,16,18,12</sub> | 5.6<br><sub>27,2,12,7,2</sub> |  | 2.0<br><sub>4,3,1,4,3</sub> |  | 1.1<br><sub>1,3,0,1,0</sub> |  | 0.6<br><sub>6,0,4,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 8.7 |
| Kyle Anderson | 64% | 10.1<br><sub>-,16,11,5,-</sub> | 2.9<br><sub>-,6,2,0,-</sub> |  | 1.7<br><sub>-,2,3,0,-</sub> |  | 1.7<br><sub>-,2,4,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.3 | 0.5 | 6.3 |
| Trayce Jackson-Davis | 52% | 9.8<br><sub>-,14,-,-,-</sub> | 3.6<br><sub>-,4,-,-,-</sub> |  | 2.9<br><sub>-,6,-,-,-</sub> |  | 0.6<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.5 | 0.5 | 7.1 |
| Jaden Bradley | 58% | 7.8<br><sub>8,9,-,2,-</sub> | 2.8<br><sub>3,0,-,1,-</sub> |  | 1.2<br><sub>0,1,-,0,-</sub> |  | 1.1<br><sub>1,3,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.0 |

</details>

<details><summary>if Scottie Barnes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 98% | 35.4<br><sub>34,28,35,36,41</sub> | 26.4<br><sub>31,23,27,33,28</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>6,4,3,1,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>9,2,5,11,9</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>3,1,3,4,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 2.9 | 35.7 |
| OG Anunoby (NYK) | 98% | 34.3<br><sub>34,29,34,33,44</sub> | 17.3<br><sub>15,19,14,11,21</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,3,6,2,9</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>2,2,2,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,5,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.9 | 2.0 | 24.4 |
| Karl-Anthony Towns (NYK) | 98% | 33.7<br><sub>34,27,34,34,43</sub> | 19.8<br><sub>29,21,21,23,28</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 13.0<br><sub>13,16,11,15,17</sub> | 12.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>3,3,8,5,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>2,2,2,3,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.7 | 3.1 | 36.6 |
| Josh Hart (NYK) | 98% | 28.3<br><sub>-,-,26,23,26</sub> | 8.3<br><sub>-,-,6,0,0</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>-,-,4,5,5</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.5<br><sub>-,-,3,4,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.3 | 1.6 | 18.2 |
| Mikal Bridges (NYK) | 98% | 26.6<br><sub>31,17,17,29,32</sub> | 9.5<br><sub>9,4,2,18,5</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>6,5,1,3,7</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.4<br><sub>4,1,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0<br><sub>1,0,0,2,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.9 | 0.5 | 1.1 | 14.9 |
| Landry Shamet (NYK) | 98% | 24.6<br><sub>29,28,29,21,30</sub> | 9.1<br><sub>9,10,12,5,23</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,3,2,3,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3<br><sub>1,2,4,1,0</sub> |  | 1.6<br><sub>3,2,2,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.6 | 0.2 | 0.9 | 12.2 |
| Miles McBride (NYK) | 98% | 17.6<br><sub>16,25,27,22,14</sub> | 6.3<br><sub>5,8,19,9,3</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,0,2,1,1</sub> |  | 1.2<br><sub>0,3,2,1,0</sub> |  | 1.0<br><sub>1,2,5,3,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.2 | 0.6 | 8.9 |
| Tyler Kolek (NYK) | 91% | 13.9<br><sub>14,15,13,19,16</sub> | 4.2<br><sub>0,12,4,5,0</sub> |  | 1.8<br><sub>4,3,1,6,0</sub> |  | 3.6<br><sub>5,4,4,2,7</sub> |  | 0.5<br><sub>0,2,0,1,0</sub> |  | 0.4 | 0.1 | 0.8 | 9.6 |
| Andre Drummond (NYK) | 98% | 11.9<br><sub>14,16,14,14,7</sub> | 3.6<br><sub>0,2,0,0,2</sub> |  | 5.3<br><sub>8,14,4,6,3</sub> |  | 0.8<br><sub>0,3,3,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.7 | 9.8 |
| Jordan Clarkson (NYK) | 84% | 9.9<br><sub>15,11,-,9,7</sub> | 4.7<br><sub>9,2,-,0,2</sub> |  | 1.4<br><sub>2,4,-,1,2</sub> |  | 0.7<br><sub>0,2,-,0,0</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.7 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Mohamed Diawara (NYK) | 52% | 8.0<br><sub>14,18,11,-,-</sub> | 2.8<br><sub>2,5,2,-,-</sub> |  | 1.3<br><sub>3,3,0,-,-</sub> |  | 0.8<br><sub>3,3,0,-,-</sub> |  | 0.2<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Jose Alvarado (NYK) | 58% | 7.4<br><sub>-,6,-,-,2</sub> | 2.9<br><sub>-,0,-,-,0</sub> |  | 1.0<br><sub>-,1,-,-,0</sub> |  | 1.2<br><sub>-,1,-,-,1</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 5.0 |
| Jaden Akins (NYK) | 38% | 6.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 0.9 |
| Dalton Knecht (NYK) | 64% | 6.7<br><sub>5,8,-,-,-</sub> | 2.9<br><sub>0,3,-,-,-</sub> |  | 1.3<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.6 |
| James Wiseman (NYK) | 52% | 6.2<br><sub>-,5,-,-,3</sub> | 2.2<br><sub>-,0,-,-,0</sub> |  | 2.0<br><sub>-,1,-,-,3</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.1 | 0.3 | 0.5 | 4.6 |
| Pacome Dadiet (NYK) | 52% | 5.9<br><sub>-,6,-,1,-</sub> | 2.6<br><sub>-,8,-,0,-</sub> |  | 1.1<br><sub>-,2,-,0,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,1,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Scottie Barnes (TOR) | 100% | 33.4<br><sub>-,-,-,-,36</sub> | 19.7<br><sub>-,-,-,-,30</sub> | 20.5 · – | 6.8<br><sub>-,-,-,-,9</sub> | 6.5 | 6.2<br><sub>-,-,-,-,4</sub> | 4.5 | 0.9<br><sub>-,-,-,-,4</sub> | 0.5 | 1.4 | 1.1 | 2.8 | 32.7 |
| RJ Barrett (TOR) | 98% | 32.7<br><sub>37,36,31,37,37</sub> | 19.0<br><sub>27,19,12,31,14</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>7,3,8,14,5</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>5,2,7,5,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>0,1,0,4,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.4 | 2.2 | 28.8 |
| Immanuel Quickley (TOR) | 88% | 29.9<br><sub>-,-,28,28,38</sub> | 15.3<br><sub>-,-,11,26,17</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,-,4,4,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>-,-,4,6,6</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>-,-,1,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.1 | 1.5 | 24.1 |
| Ja'Kobe Walter (TOR) | 98% | 29.1<br><sub>29,34,35,32,36</sub> | 10.1<br><sub>7,12,17,6,7</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>6,6,3,5,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,0,1,0,1</sub> |  | 1.7<br><sub>1,2,5,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.3 | 0.8 | 15.0 |
| Collin Murray-Boyles (TOR) | 98% | 26.0<br><sub>34,-,20,32,40</sub> | 10.5<br><sub>19,-,5,14,6</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>7,-,4,0,13</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>2,-,3,4,2</sub> |  | 0.4<br><sub>0,-,1,1,0</sub> |  | 1.0 | 1.1 | 1.5 | 18.0 |
| Jamal Shead (TOR) | 98% | 23.5<br><sub>34,36,22,22,26</sub> | 7.8<br><sub>10,20,3,5,19</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>3,2,3,1,2</sub> |  | 5.2<br><sub>16,11,6,5,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.0<br><sub>1,4,0,1,3</sub> |  | 0.9 | 0.2 | 1.6 | 14.8 |
| Jakob Poeltl (TOR) | 91% | 21.5<br><sub>31,31,32,25,17</sub> | 8.3<br><sub>19,18,6,9,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>11,8,9,5,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>1,2,1,3,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.1 | 15.7 |
| Jamison Battle (TOR) | 98% | 15.6<br><sub>21,29,25,25,8</sub> | 6.5<br><sub>6,18,12,13,0</sub> |  | 1.9<br><sub>2,1,2,1,3</sub> |  | 0.6<br><sub>0,2,0,1,0</sub> |  | 1.0<br><sub>1,5,2,3,0</sub> |  | 0.3 | 0.1 | 0.5 | 8.9 |
| Allen Graves (TOR) | 98% | 13.6<br><sub>16,13,18,13,16</sub> | 4.2<br><sub>3,3,13,0,2</sub> |  | 2.4<br><sub>2,2,5,2,5</sub> |  | 0.8<br><sub>0,1,0,0,3</sub> |  | 0.4<br><sub>0,1,3,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.5 |
| Alijah Martin (TOR) | 93% | 12.1<br><sub>31,21,16,18,12</sub> | 5.0<br><sub>27,2,12,7,2</sub> |  | 1.7<br><sub>4,3,1,4,3</sub> |  | 0.9<br><sub>1,3,0,1,0</sub> |  | 0.5<br><sub>6,0,4,1,0</sub> |  | 0.5 | 0.2 | 0.8 | 7.6 |
| Kyle Anderson (TOR) | 64% | 7.1<br><sub>-,16,11,5,-</sub> | 1.9<br><sub>-,6,2,0,-</sub> |  | 1.2<br><sub>-,2,3,0,-</sub> |  | 1.2<br><sub>-,2,4,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.4 |
| Trayce Jackson-Davis (TOR) | 52% | 7.0<br><sub>-,14,-,-,-</sub> | 2.6<br><sub>-,4,-,-,-</sub> |  | 2.1<br><sub>-,6,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.4 | 0.4 | 5.2 |
| Jaden Bradley (TOR) | 58% | 6.1<br><sub>8,9,-,2,-</sub> | 2.1<br><sub>3,0,-,1,-</sub> |  | 0.9<br><sub>0,1,-,0,-</sub> |  | 0.9<br><sub>1,3,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.0 |

</details>


### POR @ MIN
Out: Jaylen Clark (MIN), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Jonathan Kuminga (MIN), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.0–112.5 | POR 37% | 2.70 / 1.59 | MIN -4.5 | 220.5 | MIN -3.5 covers 54%; o225.5 39% |
| Expected (weighted by chance each plays) | 109.4–113.1 | POR 39% | 2.55 / 1.65 | MIN -4.5 | 222.5 | MIN -3.5 covers 52%; o225.5 43% |
| if Deni Avdija plays | 110.5–113.5 | POR 41% | 2.42 / 1.71 | MIN -3.5 | 223.5 | MIN -3.5 covers 49%; o225.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija (POR) | Questionable | 55% | 33.6 | 23.4 | 6.4 | 5.9 | 1.8 | 0.9 | 0.6 | 3.9 | 35.7 | full tables below |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Toumani Camara | 98% | 32.6<br><sub>21,30,38,36,26</sub> | 13.2<br><sub>4,12,14,14,3</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>4,3,5,2,0</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>0,3,3,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.6 | 1.9 | 19.3 |
| Damian Lillard | 98% | 32.4<br><sub>20,24,32,33,24</sub> | 21.6<br><sub>12,25,18,29,9</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>0,3,3,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>7,3,3,6,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>2,4,2,6,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.3 | 2.8 | 31.1 |
| Jrue Holiday | 98% | 30.1<br><sub>20,25,30,27,25</sub> | 16.0<br><sub>11,11,19,6,10</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>0,1,3,5,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.4<br><sub>0,2,5,5,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>1,2,5,0,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.3 | 2.7 | 25.6 |
| Sidy Cissoko | 98% | 28.5<br><sub>16,33,29,26,28</sub> | 8.6<br><sub>4,17,19,3,5</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>1,3,0,1,3</sub> |  | 1.1<br><sub>0,3,4,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.5 | 1.5 | 14.8 |
| Scoot Henderson | 98% | 27.9<br><sub>24,23,19,23,23</sub> | 14.2<br><sub>13,11,5,11,10</sub> |  | 2.8<br><sub>2,1,2,0,1</sub> |  | 3.2<br><sub>1,4,2,1,0</sub> |  | 1.6<br><sub>0,3,1,2,0</sub> |  | 1.0 | 0.3 | 2.7 | 20.2 |
| Donovan Clingan | 98% | 27.1<br><sub>22,26,30,27,22</sub> | 11.6<br><sub>6,7,5,13,10</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 10.8<br><sub>5,13,12,11,10</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>0,3,2,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.6 | 2.3 | 1.6 | 24.4 |
| Robert Williams III | 98% | 19.2<br><sub>-,15,17,17,15</sub> | 7.5<br><sub>-,6,10,2,2</sub> |  | 7.2<br><sub>-,4,7,7,5</sub> |  | 1.3<br><sub>-,0,0,1,2</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.6 | 1.4 | 1.0 | 15.9 |
| Jayson Kent | 67% | 16.0<br><sub>12,-,-,11,11</sub> | 5.9<br><sub>4,-,-,3,8</sub> |  | 1.9<br><sub>1,-,-,1,0</sub> |  | 0.7<br><sub>1,-,-,0,0</sub> |  | 0.7<br><sub>0,-,-,1,2</sub> |  | 0.6 | 0.2 | 0.8 | 8.5 |
| Branden Carlson | 83% | 14.6<br><sub>12,8,10,8,14</sub> | 4.2<br><sub>4,2,0,5,5</sub> |  | 3.7<br><sub>2,5,2,3,6</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,0,0,1,1</sub> |  | 0.3 | 0.8 | 0.7 | 8.6 |
| Yang Hansen | 63% | 12.7<br><sub>26,5,-,-,7</sub> | 4.7<br><sub>12,0,-,-,0</sub> |  | 3.3<br><sub>10,1,-,-,1</sub> |  | 0.9<br><sub>1,0,-,-,3</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.3 | 0.4 | 1.0 | 8.8 |
| Micah Potter | 58% | 12.0<br><sub>14,5,-,-,7</sub> | 5.2<br><sub>7,0,-,-,2</sub> |  | 3.3<br><sub>3,3,-,-,4</sub> |  | 0.8<br><sub>1,0,-,-,1</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 0.3 | 0.3 | 0.7 | 9.2 |
| John Tonje | 52% | 12.0<br><sub>-,-,-,-,7</sub> | 5.6<br><sub>-,-,-,-,7</sub> |  | 2.6<br><sub>-,-,-,-,4</sub> |  | 1.4<br><sub>-,-,-,-,3</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.2 | 0.7 | 9.6 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 36.4<br><sub>40,33,25,37,31</sub> | 17.8<br><sub>23,16,16,18,13</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>6,6,9,5,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>5,3,3,6,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.4 | 1.1 | 2.0 | 27.1 |
| Ayo Dosunmu | 98% | 34.8<br><sub>39,30,27,33,30</sub> | 18.8<br><sub>26,26,18,24,8</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>2,4,2,5,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,1,1,0,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>4,4,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.5 | 2.1 | 27.2 |
| Rudy Gobert | 98% | 32.2<br><sub>25,31,23,27,32</sub> | 10.8<br><sub>8,10,9,1,18</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.9<br><sub>11,15,6,10,15</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>0,2,1,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.3 | 1.3 | 24.7 |
| LaMelo Ball | 98% | 31.5<br><sub>35,30,25,30,24</sub> | 21.1<br><sub>22,24,22,19,6</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>2,3,3,8,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>8,5,9,6,0</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>3,4,6,4,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.6 | 0.3 | 3.2 | 31.8 |
| Terrence Shannon Jr. | 98% | 29.8<br><sub>-,18,21,22,35</sub> | 15.6<br><sub>-,5,6,14,34</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>-,3,2,6,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>-,3,4,0,6</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>-,0,0,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 1.6 | 22.0 |
| Trey Lyles | 98% | 24.4<br><sub>29,21,15,19,19</sub> | 7.6<br><sub>5,9,2,5,9</sub> |  | 4.9<br><sub>13,6,0,1,3</sub> |  | 1.3<br><sub>2,2,0,2,1</sub> |  | 1.0<br><sub>0,1,0,0,2</sub> |  | 0.7 | 0.4 | 0.8 | 13.8 |
| Joan Beringer | 98% | 20.4<br><sub>7,16,22,13,16</sub> | 7.4<br><sub>2,4,13,2,0</sub> |  | 6.8<br><sub>3,3,9,5,4</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.5 | 0.8 | 14.8 |
| Bones Hyland | 98% | 19.6<br><sub>10,13,23,21,13</sub> | 10.0<br><sub>4,14,24,12,5</sub> |  | 2.0<br><sub>1,2,3,1,1</sub> |  | 3.0<br><sub>0,2,8,2,5</sub> |  | 1.5<br><sub>1,1,5,3,0</sub> |  | 0.9 | 0.3 | 1.2 | 15.1 |
| Rocco Zikarsky | 38% | 11.0<br><sub>-,2,-,-,-</sub> | 3.6<br><sub>-,0,-,-,-</sub> |  | 3.4<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 1.0 | 0.6 | 7.5 |
| Cody Williams | 58% | 9.1<br><sub>-,2,7,-,4</sub> | 0.3<br><sub>-,0,0,-,0</sub> |  | 1.4<br><sub>-,0,1,-,1</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 2.1 |
| Isaiah Evans | 58% | 8.8<br><sub>-,2,8,-,4</sub> | 6.5<br><sub>-,0,2,-,0</sub> |  | 1.5<br><sub>-,0,1,-,0</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 8.4 |
| Johni Broome | 3% | 8.7 | 3.1 |  | 1.9 |  | 0.6 |  | 0.2 |  | 0.4 | 0.3 | 0.4 | 5.6 |

</details>

<details><summary>if Deni Avdija plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels (MIN) | 98% | 36.3<br><sub>40,33,25,37,31</sub> | 17.7<br><sub>23,16,16,18,13</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>6,6,9,5,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>5,3,3,6,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,2,0,2,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3 | 1.1 | 2.0 | 27.0 |
| Ayo Dosunmu (MIN) | 98% | 34.8<br><sub>39,30,27,33,30</sub> | 18.8<br><sub>26,26,18,24,8</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>2,4,2,5,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,1,1,0,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>4,4,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.5 | 2.1 | 27.2 |
| Rudy Gobert (MIN) | 98% | 32.2<br><sub>25,31,23,27,32</sub> | 10.9<br><sub>8,10,9,1,18</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.9<br><sub>11,15,6,10,15</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>0,2,1,4,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.3 | 1.3 | 24.8 |
| LaMelo Ball (MIN) | 98% | 31.5<br><sub>35,30,25,30,24</sub> | 21.2<br><sub>22,24,22,19,6</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>2,3,3,8,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>8,5,9,6,0</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.7<br><sub>3,4,6,4,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.7 | 0.3 | 3.2 | 31.9 |
| Terrence Shannon Jr. (MIN) | 98% | 29.8<br><sub>-,18,21,22,35</sub> | 15.7<br><sub>-,5,6,14,34</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>-,3,2,6,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>-,3,4,0,6</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>-,0,0,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.2 | 1.6 | 22.1 |
| Trey Lyles (MIN) | 98% | 24.4<br><sub>29,21,15,19,19</sub> | 7.6<br><sub>5,9,2,5,9</sub> |  | 4.9<br><sub>13,6,0,1,3</sub> |  | 1.2<br><sub>2,2,0,2,1</sub> |  | 1.0<br><sub>0,1,0,0,2</sub> |  | 0.7 | 0.4 | 0.8 | 13.8 |
| Joan Beringer (MIN) | 98% | 20.5<br><sub>7,16,22,13,16</sub> | 7.5<br><sub>2,4,13,2,0</sub> |  | 6.8<br><sub>3,3,9,5,4</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.5 | 0.8 | 14.9 |
| Bones Hyland (MIN) | 98% | 19.7<br><sub>10,13,23,21,13</sub> | 10.1<br><sub>4,14,24,12,5</sub> |  | 2.0<br><sub>1,2,3,1,1</sub> |  | 3.1<br><sub>0,2,8,2,5</sub> |  | 1.5<br><sub>1,1,5,3,0</sub> |  | 0.9 | 0.3 | 1.2 | 15.1 |
| Rocco Zikarsky (MIN) | 38% | 11.0<br><sub>-,2,-,-,-</sub> | 3.6<br><sub>-,0,-,-,-</sub> |  | 3.4<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 1.0 | 0.7 | 7.5 |
| Cody Williams (MIN) | 58% | 9.2<br><sub>-,2,7,-,4</sub> | 0.3<br><sub>-,0,0,-,0</sub> |  | 1.4<br><sub>-,0,1,-,1</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 2.2 |
| Isaiah Evans (MIN) | 58% | 8.9<br><sub>-,2,8,-,4</sub> | 6.6<br><sub>-,0,2,-,0</sub> |  | 1.5<br><sub>-,0,1,-,0</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 8.5 |
| Johni Broome (MIN) | 3% | 8.8 | 3.1 |  | 2.0 |  | 0.5 |  | 0.2 |  | 0.4 | 0.3 | 0.5 | 5.6 |
| Deni Avdija (POR) | 100% | 33.6<br><sub>24,34,35,35,30</sub> | 23.4<br><sub>15,24,28,34,27</sub> | 24.5 · – | 6.4<br><sub>4,6,3,6,8</sub> | 5.5 | 5.9<br><sub>1,8,6,4,4</sub> | 5.5 | 1.8<br><sub>2,2,4,3,3</sub> | 1.5 | 0.9 | 0.6 | 3.9 | 35.7 |
| Toumani Camara (POR) | 98% | 30.9<br><sub>21,30,38,36,26</sub> | 11.0<br><sub>4,12,14,14,3</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>4,3,5,2,0</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>0,3,3,1,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.5 | 1.4 | 16.7 |
| Damian Lillard (POR) | 98% | 30.4<br><sub>20,24,32,33,24</sub> | 18.7<br><sub>12,25,18,29,9</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>0,3,3,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>7,3,3,6,4</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,4,2,6,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.2 | 2.4 | 26.9 |
| Jrue Holiday (POR) | 98% | 27.9<br><sub>20,25,30,27,25</sub> | 13.0<br><sub>11,11,19,6,10</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>0,1,3,5,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>0,2,5,5,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>1,2,5,0,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 2.2 | 21.3 |
| Donovan Clingan (POR) | 98% | 26.2<br><sub>22,26,30,27,22</sub> | 10.4<br><sub>6,7,5,13,10</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 10.6<br><sub>5,13,12,11,10</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,3,2,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.6 | 2.3 | 1.4 | 22.8 |
| Sidy Cissoko (POR) | 98% | 25.6<br><sub>16,33,29,26,28</sub> | 6.9<br><sub>4,17,19,3,5</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>3,3,2,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>1,3,0,1,3</sub> |  | 0.8<br><sub>0,3,4,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.4 | 1.1 | 12.2 |
| Scoot Henderson (POR) | 98% | 24.5<br><sub>24,23,19,23,23</sub> | 11.1<br><sub>13,11,5,11,10</sub> |  | 2.4<br><sub>2,1,2,0,1</sub> |  | 2.4<br><sub>1,4,2,1,0</sub> |  | 1.3<br><sub>0,3,1,2,0</sub> |  | 0.8 | 0.2 | 2.1 | 15.9 |
| Robert Williams III (POR) | 98% | 16.7<br><sub>-,15,17,17,15</sub> | 6.0<br><sub>-,6,10,2,2</sub> |  | 6.3<br><sub>-,4,7,7,5</sub> |  | 1.1<br><sub>-,0,0,1,2</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.6 | 1.2 | 0.8 | 13.4 |
| Jayson Kent (POR) | 67% | 12.6<br><sub>12,-,-,11,11</sub> | 4.5<br><sub>4,-,-,3,8</sub> |  | 1.6<br><sub>1,-,-,1,0</sub> |  | 0.6<br><sub>1,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,1,2</sub> |  | 0.5 | 0.2 | 0.6 | 6.7 |
| Branden Carlson (POR) | 83% | 11.5<br><sub>12,8,10,8,14</sub> | 3.3<br><sub>4,2,0,5,5</sub> |  | 3.0<br><sub>2,5,2,3,6</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.2<br><sub>0,0,0,1,1</sub> |  | 0.2 | 0.6 | 0.6 | 6.9 |
| Micah Potter (POR) | 58% | 9.0<br><sub>14,5,-,-,7</sub> | 3.8<br><sub>7,0,-,-,2</sub> |  | 2.4<br><sub>3,3,-,-,4</sub> |  | 0.6<br><sub>1,0,-,-,1</sub> |  | 0.3<br><sub>1,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 6.8 |
| Yang Hansen (POR) | 63% | 8.4<br><sub>26,5,-,-,7</sub> | 3.1<br><sub>12,0,-,-,0</sub> |  | 2.1<br><sub>10,1,-,-,1</sub> |  | 0.5<br><sub>1,0,-,-,3</sub> |  | 0.2<br><sub>1,0,-,-,0</sub> |  | 0.2 | 0.3 | 0.7 | 5.8 |
| John Tonje (POR) | 52% | 8.1<br><sub>-,-,-,-,7</sub> | 4.2<br><sub>-,-,-,-,7</sub> |  | 1.9<br><sub>-,-,-,-,4</sub> |  | 0.9<br><sub>-,-,-,-,3</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 7.0 |

</details>


### DET @ SAS
Out: Tobias Harris (SAS), Jalen Duren (DET), Ronald Holland II (DET), Isaiah Joe (DET), Taurean Prince (DET), Duncan Robinson (DET)

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 38.2<br><sub>40,38,27,48,36</sub> | 27.2<br><sub>26,14,17,52,33</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>7,4,3,5,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 8.8<br><sub>11,8,7,11,8</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>1,1,0,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.8 | 4.4 | 41.4 |
| Daniss Jenkins | 98% | 34.6<br><sub>21,32,36,42,35</sub> | 15.8<br><sub>5,31,22,21,10</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>1,5,6,6,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 5.2<br><sub>4,4,8,0,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>1,8,2,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 2.1 | 25.1 |
| Kevin Huerter | 98% | 33.0<br><sub>20,35,33,24,38</sub> | 12.6<br><sub>8,24,12,11,20</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>1,5,2,1,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>0,5,3,0,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>2,4,0,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.8 | 1.3 | 20.1 |
| Ausar Thompson | 98% | 31.5<br><sub>34,24,28,43,18</sub> | 11.6<br><sub>11,7,8,17,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>17,11,5,11,8</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>3,3,4,11,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.7 | 1.1 | 2.1 | 24.6 |
| John Collins | 98% | 30.6<br><sub>26,32,28,25,26</sub> | 13.6<br><sub>16,8,24,10,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>1,4,10,4,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>0,1,3,0,0</sub> |  | 1.4<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.8 | 1.5 | 20.9 |
| Paul Reed | 98% | 29.8<br><sub>30,20,21,38,23</sub> | 13.7<br><sub>8,8,4,13,9</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>7,10,10,11,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>4,0,2,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.1 | 1.8 | 24.4 |
| Javonte Green | 98% | 20.5<br><sub>15,17,11,15,12</sub> | 6.6<br><sub>1,7,7,5,5</sub> |  | 2.9<br><sub>3,2,1,1,1</sub> |  | 0.8<br><sub>1,2,0,0,0</sub> |  | 0.9<br><sub>0,1,0,1,0</sub> |  | 1.0 | 0.4 | 0.5 | 10.3 |
| Tolu Smith | 58% | 12.6<br><sub>5,-,-,-,1</sub> | 4.4<br><sub>1,-,-,-,3</sub> |  | 4.0<br><sub>1,-,-,-,2</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.5 | 0.6 | 9.1 |
| Isaac Jones | 52% | 8.9<br><sub>-,-,2,-,2</sub> | 10.7<br><sub>-,-,0,-,0</sub> |  | 2.1<br><sub>-,-,0,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.5 | 0.4 | 13.2 |
| Elijah Harkless | 48% | 8.5<br><sub>-,-,-,-,2</sub> | 2.6<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.7 | 3.6 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 31.9<br><sub>28,26,36,25,34</sub> | 16.5<br><sub>13,17,18,9,31</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>7,5,6,3,9</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>3,4,10,4,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,0,2,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.4 | 1.8 | 26.1 |
| Victor Wembanyama | 98% | 31.7<br><sub>24,25,32,21,35</sub> | 25.5<br><sub>29,40,32,12,26</sub> | 28.5 · –<br><sub>o 46% · u 54%</sub> | 11.5<br><sub>7,11,9,12,10</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>3,3,1,6,6</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>3,2,2,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.2 | 4.4 | 2.7 | 40.2 |
| Stephon Castle | 98% | 31.0<br><sub>24,30,29,25,35</sub> | 16.5<br><sub>14,4,11,32,20</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>7,8,1,5,4</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 5.8<br><sub>5,7,3,6,9</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,0,1,5,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 2.7 | 27.4 |
| Devin Vassell | 98% | 30.7<br><sub>21,-,-,23,32</sub> | 11.5<br><sub>15,-,-,7,6</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>2,-,-,2,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>3,-,-,2,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>2,-,-,0,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.4 | 1.0 | 17.8 |
| De'Aaron Fox | 98% | 28.9<br><sub>22,29,31,17,-</sub> | 13.5<br><sub>8,15,17,7,-</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>3,9,4,5,-</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>6,6,9,1,-</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,2,2,0,-</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.4 | 2.1 | 22.2 |
| Julian Champagnie | 98% | 25.4<br><sub>21,27,35,23,24</sub> | 8.5<br><sub>14,11,12,7,4</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,3,0,8,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>0,2,2,3,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>4,3,3,1,1</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.5 | 0.8 | 14.2 |
| Keldon Johnson | 98% | 24.2<br><sub>27,26,28,25,29</sub> | 10.0<br><sub>10,4,10,18,11</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>7,5,6,4,10</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>4,3,4,4,2</sub> |  | 0.7<br><sub>0,0,0,2,1</sub> |  | 0.7 | 0.2 | 1.2 | 16.9 |
| Harrison Barnes | 91% | 13.8<br><sub>19,21,13,21,14</sub> | 4.5<br><sub>5,11,3,11,0</sub> |  | 1.5<br><sub>3,2,1,1,0</sub> |  | 0.6<br><sub>0,0,0,1,2</sub> |  | 0.6<br><sub>1,2,1,3,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.6 |
| Luke Kornet | 98% | 13.7<br><sub>15,13,14,16,13</sub> | 3.4<br><sub>6,2,7,6,2</sub> |  | 4.0<br><sub>4,4,5,7,2</sub> |  | 0.9<br><sub>2,1,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.5 | 8.4 |
| Jordan McLaughlin | 86% | 10.0<br><sub>12,11,2,14,19</sub> | 3.1<br><sub>3,4,4,4,10</sub> |  | 1.5<br><sub>0,4,0,6,1</sub> |  | 1.3<br><sub>0,2,0,2,2</sub> |  | 0.3<br><sub>1,0,0,0,2</sub> |  | 0.6 | 0.1 | 0.5 | 5.9 |
| Carter Bryant | 91% | 9.2<br><sub>17,14,15,19,5</sub> | 3.1<br><sub>6,8,10,8,0</sub> |  | 1.6<br><sub>4,1,1,3,1</sub> |  | 0.6<br><sub>1,1,2,2,0</sub> |  | 0.3<br><sub>2,2,2,2,0</sub> |  | 0.2 | 0.2 | 0.4 | 5.2 |
| Tarris Reed Jr. | 64% | 6.1<br><sub>9,9,2,11,-</sub> | 2.2<br><sub>2,4,0,2,-</sub> |  | 2.1<br><sub>3,3,0,4,-</sub> |  | 0.3<br><sub>1,1,0,1,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.5 |
| David Jones Garcia | 58% | 5.6<br><sub>-,8,2,-,-</sub> | 2.3<br><sub>-,2,0,-,-</sub> |  | 1.0<br><sub>-,0,0,-,-</sub> |  | 0.8<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.1 |

</details>


### CHA @ LAL
Out: Walker Kessler (LAL), Austin Reaves (LAL), Kon Knueppel (CHA), Dennis Schroder (CHA), Hannes Steinbach (CHA)

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 29.7<br><sub>26,14,-,-,24</sub> | 18.9<br><sub>10,8,-,-,5</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>4,2,-,-,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>1,1,-,-,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>1,0,-,-,1</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.4 | 2.5 | 26.0 |
| Naz Reid | 98% | 29.5<br><sub>36,26,32,34,27</sub> | 17.1<br><sub>28,14,25,16,17</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>9,6,13,8,4</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,2,4,3,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,2,4,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.6 | 2.4 | 26.4 |
| Grayson Allen | 98% | 28.4<br><sub>27,22,34,34,25</sub> | 14.5<br><sub>22,0,27,14,12</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>2,2,4,4,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 3.6<br><sub>4,3,6,6,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>5,0,6,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.2 | 21.2 |
| Moussa Diabate | 98% | 28.3<br><sub>29,-,-,32,26</sub> | 8.5<br><sub>7,-,-,7,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 8.9<br><sub>6,-,-,13,12</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,-,-,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.1 | 0.8 | 1.6 | 19.7 |
| Sion James | 98% | 28.1<br><sub>31,21,33,32,35</sub> | 7.1<br><sub>10,11,11,3,3</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>2,3,4,8,8</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>1,0,4,6,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>0,3,3,0,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.1 | 1.2 | 14.2 |
| Coby White | 98% | 20.4<br><sub>18,16,20,20,20</sub> | 13.5<br><sub>4,7,10,21,21</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>5,1,2,3,0</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,1,9,3,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>0,1,0,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.5 | 0.1 | 2.3 | 19.2 |
| Royce O'Neale | 98% | 19.3<br><sub>18,26,23,22,19</sub> | 5.7<br><sub>0,7,10,7,3</sub> |  | 3.1<br><sub>3,4,3,4,3</sub> |  | 1.2<br><sub>2,2,1,0,1</sub> |  | 0.9<br><sub>0,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.0 |
| Grant Williams | 76% | 19.3<br><sub>-,-,-,16,20</sub> | 7.5<br><sub>-,-,-,11,11</sub> |  | 3.2<br><sub>-,-,-,2,2</sub> |  | 1.4<br><sub>-,-,-,1,1</sub> |  | 1.1<br><sub>-,-,-,2,3</sub> |  | 0.6 | 0.4 | 1.0 | 12.2 |
| Ryan Kalkbrenner | 98% | 18.7<br><sub>19,21,35,16,18</sub> | 5.4<br><sub>6,4,8,2,5</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>4,5,15,6,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.0<br><sub>2,0,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 11.3 |
| Christian Anderson | 88% | 15.7<br><sub>-,25,16,18,18</sub> | 6.8<br><sub>-,4,9,13,16</sub> |  | 1.8<br><sub>-,3,1,0,3</sub> |  | 2.1<br><sub>-,5,1,2,2</sub> |  | 1.0<br><sub>-,0,3,3,4</sub> |  | 0.5 | 0.2 | 1.4 | 10.8 |
| Tidjane Salaun | 96% | 11.8<br><sub>10,23,18,16,5</sub> | 4.4<br><sub>9,13,14,2,0</sub> |  | 2.6<br><sub>1,4,3,4,2</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.5<br><sub>3,2,3,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.5 |
| Liam McNeeley | 63% | 9.1<br><sub>-,19,16,-,2</sub> | 3.8<br><sub>-,8,8,-,0</sub> |  | 1.6<br><sub>-,2,1,-,0</sub> |  | 0.7<br><sub>-,3,1,-,0</sub> |  | 0.4<br><sub>-,1,2,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 6.1 |
| PJ Hall | 38% | 7.4<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.4 | 0.5 | 5.7 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 37.7<br><sub>38,-,39,32,36</sub> | 39.1<br><sub>53,-,32,32,43</sub> | 36.5 · –<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>5,-,8,5,3</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>5,-,10,5,9</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>5,-,3,5,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.9 | 0.7 | 4.5 | 54.8 |
| Quentin Grimes | 98% | 33.6<br><sub>20,32,-,-,37</sub> | 11.6<br><sub>2,12,-,-,22</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>0,1,-,-,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>0,4,-,-,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,2,-,-,5</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.3 | 1.6 | 18.3 |
| Jake LaRavia | 98% | 29.8<br><sub>25,29,32,21,32</sub> | 7.7<br><sub>7,5,4,0,12</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>8,1,3,9,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,2,3,6,3</sub> |  | 0.9<br><sub>2,0,0,0,2</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.8 | 1.2 | 14.5 |
| Matisse Thybulle | 98% | 27.8<br><sub>24,28,23,23,26</sub> | 7.9<br><sub>2,4,6,8,12</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>2,2,0,5,8</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,0,1,1,0</sub> |  | 1.4<br><sub>0,0,2,2,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.5 | 0.9 | 1.0 | 12.4 |
| Sandro Mamukelashvili | 98% | 25.9<br><sub>20,18,32,26,21</sub> | 11.1<br><sub>7,7,23,23,4</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>3,3,8,3,2</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,0,3,2,3</sub> |  | 1.6<br><sub>1,1,5,5,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 0.9 | 18.2 |
| Ziaire Williams | 98% | 25.8<br><sub>20,21,28,20,19</sub> | 9.8<br><sub>8,17,12,9,6</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>3,2,2,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,0,2,5,3</sub> |  | 1.5<br><sub>2,4,2,1,0</sub> |  | 1.6 | 0.3 | 0.9 | 14.4 |
| Collin Sexton | 98% | 25.7<br><sub>11,24,27,13,24</sub> | 14.9<br><sub>0,17,18,10,16</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>0,2,2,1,0</sub> |  | 3.1<br><sub>1,2,6,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>0,0,3,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.2 | 1.8 | 20.5 |
| Jarred Vanderbilt | 86% | 14.4<br><sub>-,14,13,9,12</sub> | 3.0<br><sub>-,2,4,4,2</sub> |  | 3.8<br><sub>-,10,2,3,4</sub> |  | 1.0<br><sub>-,3,0,1,0</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.3 | 0.6 | 7.8 |
| Adou Thiero | 67% | 11.6<br><sub>7,8,7,14,-</sub> | 3.3<br><sub>4,2,2,2,-</sub> |  | 2.8<br><sub>4,2,2,2,-</sub> |  | 0.7<br><sub>2,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.8 |
| Cameron Carr | 80% | 9.5<br><sub>-,-,7,13,-</sub> | 4.2<br><sub>-,-,2,0,-</sub> |  | 1.5<br><sub>-,-,3,2,-</sub> |  | 0.7<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.4 |
| Jaden Hardy | 52% | 9.4<br><sub>-,-,-,4,-</sub> | 4.1<br><sub>-,-,-,3,-</sub> |  | 0.9<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.6 |
| Kevon Looney | 38% | 9.0<br><sub>-,-,-,4,-</sub> | 1.6<br><sub>-,-,-,0,-</sub> |  | 2.7<br><sub>-,-,-,2,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.9 |
| AK Okereke | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Carson Cooper | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 1.3 | 7.6 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Chris Manon | 52% | 7.6<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 3.5 |
| Bronny James | 52% | 6.9<br><sub>-,-,-,4,-</sub> | 2.0<br><sub>-,-,-,4,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.7 |

</details>


### UTA @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Jaxson Hayes (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 34.2<br><sub>30,-,33,38,34</sub> | 22.3<br><sub>19,-,13,27,13</sub> | 21.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>5,-,7,4,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 6.3<br><sub>8,-,7,7,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>0,-,2,4,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.9 | 0.2 | 3.5 | 32.6 |
| Darryn Peterson | 98% | 33.6<br><sub>35,31,33,34,34</sub> | 19.2<br><sub>26,25,22,28,17</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>6,4,4,7,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>4,4,5,2,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>4,4,2,4,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.6 | 2.2 | 28.1 |
| Ace Bailey | 98% | 32.8<br><sub>32,35,31,35,30</sub> | 16.1<br><sub>7,23,18,21,7</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>2,7,7,3,8</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>3,2,2,1,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>1,3,3,3,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.9 | 1.9 | 24.0 |
| Brice Sensabaugh | 98% | 27.1<br><sub>13,14,23,27,30</sub> | 15.4<br><sub>2,5,19,7,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>3,4,3,3,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,4,1,1,2</sub> |  | 2.1<br><sub>0,1,3,1,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.3 | 2.3 | 21.9 |
| Mo Bamba | 88% | 26.2<br><sub>17,17,18,20,36</sub> | 9.9<br><sub>3,7,5,9,26</sub> |  | 8.6<br><sub>3,7,1,9,5</sub> |  | 1.4<br><sub>1,0,1,1,4</sub> |  | 0.7<br><sub>0,0,0,0,6</sub> |  | 0.7 | 1.8 | 1.2 | 19.8 |
| Josh Okogie | 96% | 25.2<br><sub>17,21,15,22,27</sub> | 6.8<br><sub>0,6,7,7,7</sub> | 5.5 · –<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>1,4,3,2,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>0,4,0,1,0</sub> |  | 0.8<br><sub>0,0,1,2,2</sub> |  | 1.2 | 0.3 | 1.0 | 12.3 |
| Josh Green | 96% | 21.9<br><sub>28,30,26,14,15</sub> | 4.6<br><sub>10,2,3,2,6</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>0,5,2,0,1</sub> |  | 1.2<br><sub>1,4,1,0,1</sub> |  | 0.6<br><sub>1,0,1,0,2</sub> |  | 0.7 | 0.2 | 0.7 | 8.0 |
| Svi Mykhailiuk | 97% | 18.5<br><sub>6,21,20,7,21</sub> | 6.9<br><sub>0,7,3,0,6</sub> |  | 2.0<br><sub>0,2,0,1,2</sub> |  | 1.4<br><sub>0,3,2,0,3</sub> |  | 1.1<br><sub>0,1,1,0,2</sub> |  | 0.5 | 0.1 | 0.7 | 10.3 |
| Isaiah Collier | 76% | 18.3<br><sub>16,24,12,16,-</sub> | 8.7<br><sub>6,17,7,3,-</sub> |  | 2.6<br><sub>4,5,3,2,-</sub> |  | 4.6<br><sub>2,5,2,5,-</sub> |  | 0.4<br><sub>0,4,1,1,-</sub> |  | 0.8 | 0.2 | 1.9 | 15.9 |
| Kyle Filipowski | 58% | 14.1<br><sub>15,15,-,2,-</sub> | 7.0<br><sub>9,7,-,2,-</sub> |  | 4.4<br><sub>6,4,-,0,-</sub> |  | 1.4<br><sub>1,1,-,0,-</sub> |  | 0.5<br><sub>1,0,-,0,-</sub> |  | 0.6 | 0.2 | 1.0 | 12.8 |
| Tony Bradley | 67% | 13.6<br><sub>2,14,-,12,12</sub> | 4.3<br><sub>0,4,-,0,6</sub> |  | 4.0<br><sub>1,5,-,5,2</sub> |  | 0.7<br><sub>0,0,-,1,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 9.0 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 30.4<br><sub>39,32,25,37,35</sub> | 22.3<br><sub>26,24,13,24,27</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>1,0,5,4,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 7.1<br><sub>7,10,6,7,7</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>4,3,1,3,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.2 | 3.1 | 32.0 |
| Rui Hachimura | 98% | 27.1<br><sub>37,26,23,32,22</sub> | 13.3<br><sub>21,14,13,7,4</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>9,3,5,11,2</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>7,2,1,3,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.9<br><sub>1,2,3,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.7 | 0.3 | 1.2 | 19.2 |
| Derrick Jones Jr. | 98% | 26.6<br><sub>37,29,24,29,26</sub> | 10.9<br><sub>12,8,11,14,13</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>8,4,3,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,3,0,0,1</sub> |  | 1.3<br><sub>2,0,2,4,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.0 | 0.9 | 16.6 |
| Brook Lopez | 98% | 25.2<br><sub>35,26,19,31,29</sub> | 13.3<br><sub>20,20,8,26,7</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>8,7,4,7,5</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,1,1,4,8</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,1,1,3,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 1.4 | 1.2 | 20.6 |
| Kris Dunn | 98% | 23.0<br><sub>35,24,19,20,18</sub> | 7.0<br><sub>5,14,3,2,7</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>5,5,2,3,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.6<br><sub>3,4,3,6,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>1,2,1,0,0</sub> |  | 1.6 | 0.3 | 1.0 | 13.8 |
| Max Strus | 98% | 22.4<br><sub>23,19,22,23,25</sub> | 9.7<br><sub>9,7,12,3,14</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>5,4,3,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>5,2,3,3,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>3,1,2,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 0.9 | 16.6 |
| Keaton Wagler | 98% | 22.2<br><sub>16,18,23,18,28</sub> | 12.2<br><sub>11,15,11,14,12</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,0,2,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.4<br><sub>1,4,4,1,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.6<br><sub>3,3,1,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.7 | 18.7 |
| Kobe Sanders | 98% | 20.8<br><sub>18,22,26,15,20</sub> | 9.4<br><sub>4,8,9,5,2</sub> |  | 2.5<br><sub>2,2,3,0,6</sub> |  | 2.2<br><sub>1,4,7,1,4</sub> |  | 1.3<br><sub>0,2,1,1,0</sub> |  | 0.9 | 0.2 | 1.1 | 14.2 |
| Isaiah Jackson | 98% | 16.7<br><sub>13,-,16,17,15</sub> | 7.7<br><sub>2,-,4,5,13</sub> |  | 5.2<br><sub>4,-,4,3,2</sub> |  | 1.4<br><sub>2,-,0,3,2</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.8 | 1.1 | 1.1 | 14.4 |
| Gradey Dick | 97% | 15.9<br><sub>7,17,19,19,19</sub> | 8.4<br><sub>4,15,10,13,12</sub> |  | 2.6<br><sub>2,4,3,3,2</sub> |  | 0.9<br><sub>1,0,2,0,0</sub> |  | 0.8<br><sub>0,2,1,2,2</sub> |  | 0.6 | 0.1 | 0.7 | 11.9 |
| Baba Miller | 80% | 11.8<br><sub>6,20,16,-,5</sub> | 5.8<br><sub>2,12,13,-,2</sub> |  | 2.0<br><sub>1,5,4,-,0</sub> |  | 1.4<br><sub>1,4,0,-,0</sub> |  | 0.3<br><sub>0,0,1,-,0</sub> |  | 0.5 | 0.3 | 0.7 | 9.3 |
| Jalen Pickett | 48% | 6.9<br><sub>-,2,8,-,-</sub> | 2.6<br><sub>-,0,3,-,-</sub> |  | 0.9<br><sub>-,0,1,-,-</sub> |  | 1.1<br><sub>-,0,1,-,-</sub> |  | 0.2<br><sub>-,0,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Cam Christie | 48% | 6.4<br><sub>-,2,-,-,-</sub> | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.0 |
| Nick Martinelli | 58% | 6.3<br><sub>-,2,-,-,-</sub> | 3.1<br><sub>-,2,-,-,-</sub> |  | 1.7<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.3 |
| Blake Wesley | 52% | 6.1<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-17/`._
