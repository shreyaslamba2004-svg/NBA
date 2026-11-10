# NBA model · Mon 09 Nov 2026 (US date)

Updated **Tue 10 Nov, 11:21 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-09/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamison Battle PTS over 9.5 (10+) | MEM @ TOR | draftkings | 2.23 | 1.88 | 1.58 | 63.1% | 51.7% | 53.2% | +18.6% | +40.8% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard AST over 11.5 (12+) | IND @ DAL | draftkings | 14.40 | 12.15 | 5.07 | 19.7% | 6.5% | 8.2% | +18.6% | +183.8% | 0.4% |
| Kevin Durant PRA over 44.5 (45+) | DEN @ HOU | draftkings | 13.00 | 12.08 | 6.47 | 15.5% | 7.2% | 8.3% | +7.7% | +101.1% | 0.2% |
| Kevin Durant PA over 39.5 (40+) | DEN @ HOU | draftkings | 16.80 | 15.70 | 8.58 | 11.7% | 5.6% | 6.4% | +7.0% | +95.8% | 0.1% |
| Kevin Durant PTS over 34.5 (35+) | DEN @ HOU | draftkings | 17.20 | 16.13 | 8.92 | 11.2% | 5.4% | 6.2% | +6.6% | +92.9% | 0.1% |
| Kevin Durant PRA over 49.5 (50+) | DEN @ HOU | draftkings | 24.00 | 22.57 | 12.58 | 8.0% | 3.9% | 4.4% | +6.3% | +90.8% | 0.1% |
| Pascal Siakam AST over 7.5 (8+) | IND @ DAL | draftkings | 22.00 | 20.83 | 11.90 | 8.4% | 4.2% | 4.8% | +5.5% | +84.9% | 0.1% |
| Kevin Durant PR over 39.5 (40+) | DEN @ HOU | draftkings | 12.20 | 11.57 | 6.62 | 15.1% | 7.7% | 8.6% | +5.5% | +84.4% | 0.1% |
| Pascal Siakam AST over 5.5 (6+) | IND @ DAL | draftkings | 7.00 | 6.65 | 3.84 | 26.1% | 13.4% | 15.0% | +5.2% | +82.4% | 0.2% |
| Kevin Durant PR over 44.5 (45+) | DEN @ HOU | draftkings | 24.00 | 22.83 | 13.17 | 7.6% | 3.9% | 4.4% | +5.2% | +82.2% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MEM @ TOR | Tue 10 Nov 11:30 | 115.0–116.8 | MEM 45% | 2.22 / 1.82 | TOR -2.5 | 231.5 | TOR +1.5 covers 58%; o225.5 63% |
| IND @ DAL | Tue 10 Nov 12:00 | 112.8–117.7 | IND 36% | 2.75 / 1.57 | DAL -5.5 | 230.5 | DAL -4.5 covers 52%; o226.5 58% |
| DEN @ HOU | Tue 10 Nov 12:30 | 112.0–114.8 | DEN 42% | 2.38 / 1.72 | HOU -3.5 | 226.5 | HOU -4.5 covers 46%; o223.5 57% |
| SAS @ PHX | Tue 10 Nov 13:00 | 117.4–109.1 | SAS 72% | 1.38 / 3.64 | PHX +8.5 | 226.5 | PHX +8.5 covers 50%; o226.5 50% |
| NOP @ GSW | Tue 10 Nov 14:00 | 112.6–123.8 | NOP 22% | 4.64 / 1.27 | GSW -11.5 | 236.5 | GSW -11.5 covers 49%; o229.5 64% |

### MEM @ TOR
Out: Scottie Barnes (TOR), Kawhi Leonard (TOR), Collin Murray-Boyles (TOR), Immanuel Quickley (TOR), Jahmai Mashack (MEM), Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamison Battle PTS over 9.5 (10+) | MEM @ TOR | draftkings | 2.23 | 1.88 | 1.58 | 63.1% | 51.7% | 53.2% | +18.6% | +40.8% | 2.0% |
| Jerami Grant PTS under 10.5 | MEM @ TOR | tab | 2.00 | 1.96 | 1.74 | 57.5% | 50.0% | 51.0% | +2.0% | +14.9% | 0.5% |
| Jamal Shead PTS under 11.5 | MEM @ TOR | draftkings | 2.01 | 2.00 | 1.80 | 55.4% | 49.1% | 49.9% | +0.4% | +11.4% | 0.1% |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 100% | 32.4<br><sub>28,26,38,33,31</sub> | 14.7<br><sub>18,27,18,10,8</sub> | 16.5 · 17.5<br><sub>o 48% · u 52%</sub> | 8.9<br><sub>12,9,9,6,12</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>12,3,5,4,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>4,3,2,2,0</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.6 | 2.8 | 28.3 |
| Ty Jerome | 100% | 29.9<br><sub>24,-,37,29,28</sub> | 22.5<br><sub>10,-,40,23,21</sub> | 21.5 · 22.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,-,5,4,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 5.2<br><sub>3,-,5,3,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,-,5,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.3 | 2.8 | 31.1 |
| Cedric Coward | 100% | 28.9<br><sub>27,23,31,33,23</sub> | 13.7<br><sub>17,10,10,23,10</sub> | 13.5 · 13.5<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>7,7,9,9,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,2,3,4,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.4 | 2.1 | 22.9 |
| Jaylen Wells | 100% | 27.3<br><sub>25,22,34,21,25</sub> | 10.6<br><sub>10,4,16,0,7</sub> | 9.5 · 10.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>1,2,3,1,0</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>0,0,3,3,0</sub> |  | 1.5<br><sub>2,0,3,0,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.1 | 1.1 | 15.1 |
| Jerami Grant | 98% | 22.9<br><sub>27,23,24,24,22</sub> | 10.3<br><sub>2,14,11,11,10</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>1,2,4,1,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,1,2,2,2</sub> |  | 1.2<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.6 | 1.5 | 14.0 |
| Zach Edey | 100% | 22.4<br><sub>19,18,19,25,20</sub> | 9.1<br><sub>13,4,6,11,14</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 8.1<br><sub>7,6,9,13,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>0,0,1,1,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.5 | 1.5 | 1.6 | 18.3 |
| Javon Small | 91% | 20.8<br><sub>-,20,-,-,21</sub> | 9.3<br><sub>-,7,-,-,10</sub> |  | 2.8<br><sub>-,1,-,-,4</sub> |  | 3.1<br><sub>-,5,-,-,2</sub> |  | 1.1<br><sub>-,2,-,-,1</sub> |  | 0.8 | 0.2 | 1.8 | 15.2 |
| Cam Spencer | 98% | 19.5<br><sub>23,25,19,24,19</sub> | 7.6<br><sub>8,10,13,7,7</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>6,5,1,6,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>8,13,7,9,0</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.1<br><sub>1,2,2,1,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.1 | 1.2 | 14.2 |
| Kris Murray | 80% | 12.6<br><sub>3,21,19,15,13</sub> | 3.1<br><sub>0,2,0,5,2</sub> |  | 1.9<br><sub>1,1,4,1,2</sub> |  | 0.7<br><sub>0,1,1,1,1</sub> |  | 0.2<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 5.7 |
| GG Jackson | 72% | 12.2<br><sub>21,21,16,7,-</sub> | 6.4<br><sub>12,21,6,1,-</sub> |  | 2.3<br><sub>7,3,0,2,-</sub> |  | 0.7<br><sub>2,2,1,0,-</sub> |  | 0.6<br><sub>2,5,0,0,-</sub> |  | 0.3 | 0.3 | 1.1 | 9.3 |
| Quinten Post | 91% | 12.2<br><sub>7,-,-,11,15</sub> | 4.4<br><sub>10,-,-,2,0</sub> |  | 2.2<br><sub>4,-,-,1,2</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>2,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.1 |
| Olivier-Maxence Prosper | 63% | 10.2<br><sub>3,4,-,7,11</sub> | 4.8<br><sub>4,2,-,4,2</sub> |  | 1.9<br><sub>1,1,-,3,3</sub> |  | 0.5<br><sub>0,1,-,1,1</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.2 |
| Taylor Hendricks | 58% | 7.7<br><sub>3,4,-,-,4</sub> | 3.0<br><sub>0,6,-,-,4</sub> |  | 1.5<br><sub>1,1,-,-,2</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,2,-,-,1</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Carson Cooper | 48% | 5.8<br><sub>-,3,-,-,-</sub> | 2.4<br><sub>-,1,-,-,-</sub> |  | 2.3<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.2 | 1.0 | 5.4 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 100% | 36.2<br><sub>34,32,37,33,37</sub> | 27.6<br><sub>9,22,26,22,27</sub> | 25.5 · 25.5<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>3,10,6,5,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,4,2,3,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.6 | 3.4 | 40.3 |
| Ja'Kobe Walter | 100% | 32.8<br><sub>32,33,35,27,29</sub> | 15.4<br><sub>9,11,10,8,7</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>3,4,6,1,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.7<br><sub>1,2,5,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,3,0,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.8 | 0.5 | 1.5 | 22.6 |
| Jamal Shead | 100% | 32.0<br><sub>23,25,20,20,34</sub> | 11.5<br><sub>2,9,6,3,10</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>1,2,1,3,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>8,6,6,6,16</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,2,0,1,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.6 | 0.3 | 2.7 | 23.5 |
| Jakob Poeltl | 100% | 26.8<br><sub>23,-,-,19,31</sub> | 12.9<br><sub>12,-,-,8,19</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>11,-,-,5,11</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>3,-,-,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,-,-,0,0</sub> |  | 1.0 | 1.3 | 1.8 | 23.8 |
| Jamison Battle | 98% | 26.1<br><sub>19,17,21,19,21</sub> | 12.2<br><sub>2,20,12,9,6</sub> | 8.5 · 10.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>0,5,0,1,2</sub> |  | 1.5<br><sub>0,0,0,0,0</sub> |  | 1.9<br><sub>0,4,4,2,1</sub> |  | 0.6 | 0.3 | 1.1 | 17.3 |
| Kyle Anderson | 100% | 23.2<br><sub>-,4,8,4,-</sub> | 7.1<br><sub>-,2,2,2,-</sub> |  | 4.8<br><sub>-,3,0,0,-</sub> |  | 4.3<br><sub>-,3,0,1,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 1.1 | 0.8 | 1.5 | 16.2 |
| Malachi Smith | 88% | 23.2 | 8.4 |  | 3.9 |  | 3.9 |  | 0.9 |  | 0.9 | 0.4 | 1.2 | 16.2 |
| Alijah Martin | 88% | 21.9<br><sub>-,16,6,9,31</sub> | 10.4<br><sub>-,5,2,6,27</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>-,2,2,1,4</sub> |  | 2.1<br><sub>-,4,0,0,1</sub> |  | 1.1<br><sub>-,1,0,0,6</sub> |  | 0.9 | 0.4 | 1.8 | 15.8 |
| Allen Graves | 98% | 20.2<br><sub>9,10,7,14,16</sub> | 7.3<br><sub>7,3,0,5,3</sub> | 7.5 · 7.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,0,0,1,2</sub> |  | 1.3<br><sub>0,0,2,1,0</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 0.7 | 0.6 | 0.6 | 12.3 |
| Kevin McCullar Jr. | 23% | 14.6<br><sub>-,-,-,-,-</sub> | 5.1<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.2 | 0.8 | 9.4 |
| Trayce Jackson-Davis | 72% | 12.1<br><sub>1,9,2,4,-</sub> | 4.8<br><sub>0,5,0,1,-</sub> |  | 4.3<br><sub>0,5,0,0,-</sub> |  | 0.9<br><sub>0,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.7 | 0.8 | 0.6 | 10.0 |
| Jaden Bradley | 71% | 11.2<br><sub>-,4,-,4,8</sub> | 4.6<br><sub>-,3,-,2,3</sub> |  | 1.9<br><sub>-,1,-,1,0</sub> |  | 1.3<br><sub>-,2,-,0,1</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.9 | 0.2 | 0.7 | 7.8 |

</details>


### IND @ DAL
Out: Sergio de Larrea (DAL), Morez Johnson Jr. (DAL), Dereck Lively II (DAL), Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND)

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 86% | 32.5<br><sub>29,36,-,30,32</sub> | 23.6<br><sub>13,17,-,20,23</sub> | 21.5 · 20.5<br><sub>o 52% · u 48%</sub> | 6.6<br><sub>5,5,-,4,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>4,5,-,2,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>0,0,-,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.4 | 34.4 |
| Andrew Nembhard | 80% | 32.3<br><sub>30,35,-,38,31</sub> | 17.8<br><sub>22,23,-,22,9</sub> | 15.5 · 15.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>2,3,-,2,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 8.6<br><sub>9,4,-,5,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>5,4,-,2,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2 | 0.2 | 2.4 | 29.4 |
| Aaron Nesmith | 86% | 26.3<br><sub>21,30,-,30,27</sub> | 13.5<br><sub>9,11,-,16,8</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>3,3,-,2,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,4,-,2,1</sub> |  | 1.8<br><sub>1,0,-,2,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.4 | 1.4 | 19.0 |
| Jarace Walker | 98% | 22.9<br><sub>28,20,45,17,20</sub> | 9.6<br><sub>14,6,15,2,9</sub> |  | 5.2<br><sub>6,6,7,8,5</sub> |  | 2.4<br><sub>4,3,3,1,2</sub> |  | 1.2<br><sub>3,2,1,0,1</sub> |  | 0.8 | 0.4 | 1.5 | 17.1 |
| Ivica Zubac | 58% | 20.8<br><sub>-,-,-,19,19</sub> | 9.6<br><sub>-,-,-,1,10</sub> | 11.5 · 11.5<br><sub>o 47% · u 53%</sub> | 8.2<br><sub>-,-,-,4,12</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>-,-,-,2,5</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.7 | 1.2 | 19.6 |
| Kelly Oubre Jr. | 67% | 20.6<br><sub>22,20,-,-,16</sub> | 8.3<br><sub>10,11,-,-,2</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>4,2,-,-,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>1,1,-,-,0</sub> |  | 0.7<br><sub>1,2,-,-,0</sub> |  | 0.8 | 0.4 | 0.8 | 12.8 |
| Quenton Jackson | 98% | 20.3<br><sub>24,24,35,22,17</sub> | 9.9<br><sub>24,12,20,13,6</sub> |  | 2.9<br><sub>4,3,7,7,4</sub> |  | 3.2<br><sub>1,2,3,2,1</sub> |  | 0.8<br><sub>2,3,1,3,0</sub> |  | 0.9 | 0.2 | 1.2 | 16.0 |
| Obi Toppin | 64% | 19.8<br><sub>-,-,-,19,22</sub> | 11.6<br><sub>-,-,-,11,10</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>-,-,-,5,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>-,-,-,1,2</sub> |  | 1.4<br><sub>-,-,-,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.6 | 0.3 | 1.1 | 18.2 |
| Jay Huff | 96% | 15.7<br><sub>19,17,40,14,10</sub> | 6.5<br><sub>13,0,22,6,0</sub> |  | 3.3<br><sub>1,3,8,3,3</sub> |  | 1.2<br><sub>0,0,2,1,0</sub> |  | 0.7<br><sub>3,0,0,2,0</sub> |  | 0.4 | 1.1 | 0.7 | 11.0 |
| Braden Smith | 88% | 15.0<br><sub>12,1,42,24,12</sub> | 5.2<br><sub>1,0,19,10,0</sub> |  | 1.5<br><sub>0,0,4,1,0</sub> |  | 2.8<br><sub>1,0,10,5,2</sub> |  | 0.3<br><sub>0,0,2,0,0</sub> |  | 0.7 | 0.3 | 0.9 | 9.6 |
| Kobe Brown | 72% | 13.7<br><sub>20,15,38,7,-</sub> | 5.0<br><sub>9,3,16,0,-</sub> |  | 2.6<br><sub>6,1,6,1,-</sub> |  | 1.3<br><sub>4,1,1,0,-</sub> |  | 0.5<br><sub>0,1,2,0,-</sub> |  | 0.5 | 0.2 | 0.7 | 8.9 |
| Larry Nance Jr. | 91% | 13.6<br><sub>18,26,-,14,13</sub> | 4.4<br><sub>6,4,-,4,15</sub> |  | 3.0<br><sub>2,6,-,4,2</sub> |  | 0.9<br><sub>1,1,-,1,1</sub> |  | 0.5<br><sub>2,1,-,0,5</sub> |  | 0.7 | 0.2 | 0.6 | 8.2 |
| Jalen Slawson | 93% | 13.3<br><sub>18,18,41,6,12</sub> | 4.0<br><sub>4,3,12,2,4</sub> |  | 2.7<br><sub>4,5,7,2,1</sub> |  | 1.3<br><sub>1,0,3,1,2</sub> |  | 0.3<br><sub>0,0,2,0,0</sub> |  | 0.8 | 0.6 | 0.7 | 8.0 |
| T.J. McConnell | 96% | 12.3<br><sub>-,-,-,-,9</sub> | 6.5<br><sub>-,-,-,-,6</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 3.7<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.1 | 0.8 | 12.0 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 34.0<br><sub>39,40,40,33,28</sub> | 24.7<br><sub>33,17,19,21,25</sub> | 24.5 · 24.5<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>9,4,10,10,5</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.1<br><sub>6,6,5,7,12</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.9 | 2.6 | 38.1 |
| P.J. Washington | 98% | 33.2<br><sub>34,38,39,33,25</sub> | 14.5<br><sub>3,12,21,26,6</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 7.7<br><sub>10,5,10,6,5</sub> | 6.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>1,1,3,1,0</sub> |  | 1.8<br><sub>1,2,3,6,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 1.0 | 1.5 | 23.8 |
| Kyrie Irving | 98% | 33.1<br><sub>35,-,36,28,29</sub> | 22.9<br><sub>35,-,29,14,21</sub> | 21.5 · 21.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>4,-,7,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.4<br><sub>9,-,5,2,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>5,-,5,0,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.5 | 2.1 | 31.8 |
| Naji Marshall | 88% | 24.2<br><sub>-,24,26,25,15</sub> | 12.6<br><sub>-,5,22,7,8</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,2,5,1,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>-,7,3,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.9<br><sub>-,0,3,0,1</sub> |  | 1.0 | 0.1 | 1.5 | 19.7 |
| Daniel Gafford | 98% | 21.9<br><sub>29,26,18,18,19</sub> | 10.8<br><sub>18,20,2,7,18</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>7,7,4,1,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>2,0,1,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.6 | 1.1 | 19.3 |
| Zaccharie Risacher | 96% | 21.3<br><sub>28,19,18,21,16</sub> | 6.8<br><sub>12,0,2,4,11</sub> |  | 4.6<br><sub>6,5,1,4,6</sub> |  | 1.2<br><sub>3,1,2,1,1</sub> |  | 0.7<br><sub>3,0,0,0,1</sub> |  | 0.9 | 0.9 | 0.8 | 12.7 |
| Max Christie | 98% | 16.8<br><sub>18,8,-,9,17</sub> | 6.0<br><sub>2,0,-,0,5</sub> |  | 2.1<br><sub>1,2,-,1,2</sub> |  | 1.1<br><sub>0,0,-,1,0</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.2 | 0.7 | 9.2 |
| Caleb Martin | 97% | 16.6<br><sub>25,21,20,11,19</sub> | 4.4<br><sub>8,5,0,0,2</sub> |  | 2.6<br><sub>0,6,3,0,2</sub> |  | 1.1<br><sub>0,0,2,0,2</sub> |  | 0.3<br><sub>2,1,0,0,0</sub> |  | 0.7 | 0.3 | 0.6 | 8.2 |
| Walter Clayton Jr. | 91% | 16.2<br><sub>9,24,21,23,16</sub> | 6.5<br><sub>3,20,8,12,5</sub> |  | 2.7<br><sub>2,1,6,4,4</sub> |  | 3.0<br><sub>1,2,5,2,6</sub> |  | 0.7<br><sub>1,4,2,1,1</sub> |  | 0.6 | 0.2 | 1.0 | 12.2 |
| Santi Aldama | 97% | 15.9<br><sub>-,-,-,13,15</sub> | 6.7<br><sub>-,-,-,8,12</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>-,-,-,9,2</sub> |  | 1.4<br><sub>-,-,-,1,0</sub> |  | 0.7<br><sub>-,-,-,0,2</sub> |  | 0.6 | 0.4 | 0.7 | 12.1 |
| Marcus Sasser | 80% | 12.2<br><sub>7,19,5,-,9</sub> | 4.2<br><sub>0,4,0,-,4</sub> |  | 1.1<br><sub>0,1,1,-,0</sub> |  | 1.6<br><sub>1,1,2,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.1 | 0.5 | 6.8 |
| Moussa Cisse | 67% | 7.3<br><sub>-,2,-,1,5</sub> | 2.7<br><sub>-,0,-,0,2</sub> |  | 3.0<br><sub>-,0,-,0,1</sub> |  | 0.2<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 6.0 |
| Tobi Lawal | 66% | 6.6<br><sub>-,2,-,1,5</sub> | 2.4<br><sub>-,2,-,0,2</sub> |  | 2.4<br><sub>-,0,-,0,0</sub> |  | 0.6<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.4 |
| Jett Howard | 64% | 6.0<br><sub>-,2,-,1,3</sub> | 2.5<br><sub>-,2,-,0,5</sub> |  | 0.8<br><sub>-,0,-,0,1</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,1</sub> |  | 0.1 | 0.1 | 0.3 | 3.7 |

</details>


### DEN @ HOU
Out: Steven Adams (HOU), Clint Capela (HOU), Oscar Tshiebwe (HOU), Julian Strawther (DEN)

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 91% | 35.8<br><sub>38,37,39,28,34</sub> | 23.8<br><sub>23,39,35,14,16</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>1,8,5,5,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.7<br><sub>6,5,6,7,8</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>5,7,4,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.0 | 0.5 | 2.6 | 33.9 |
| Nikola Jokic | 91% | 35.4<br><sub>34,37,36,30,36</sub> | 25.5<br><sub>21,18,26,32,19</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 11.3<br><sub>13,7,9,10,13</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 9.0<br><sub>10,10,8,11,8</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>0,0,2,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.6 | 0.8 | 3.7 | 45.8 |
| Christian Braun | 91% | 31.5<br><sub>36,37,37,28,29</sub> | 12.0<br><sub>15,31,14,11,6</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>0,3,3,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>4,1,3,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>3,7,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 1.0 | 18.1 |
| Cameron Johnson | 91% | 28.4<br><sub>-,34,34,30,29</sub> | 11.5<br><sub>-,12,7,12,18</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>-,9,4,2,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>-,3,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.5<br><sub>-,2,1,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 1.1 | 17.0 |
| Aaron Gordon | 91% | 27.6<br><sub>31,29,30,25,27</sub> | 12.3<br><sub>15,15,5,17,12</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>11,4,6,1,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>3,5,2,0,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>2,2,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 1.3 | 19.3 |
| DeMar DeRozan | 74% | 23.5<br><sub>26,24,20,-,22</sub> | 11.9<br><sub>6,3,9,-,11</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>2,1,0,-,1</sub> |  | 2.8<br><sub>5,5,1,-,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.4<br><sub>0,0,0,-,0</sub> | 0.5<br><sub>o 40% · u 60%</sub> | 0.7 | 0.3 | 1.2 | 16.8 |
| Spencer Jones | 52% | 17.9<br><sub>-,-,-,-,21</sub> | 6.1<br><sub>-,-,-,-,13</sub> | 4.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>-,-,-,-,6</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,3</sub> |  | 0.6 | 0.4 | 1.1 | 10.6 |
| Trevon Brazile | 97% | 16.5<br><sub>32,19,18,23,14</sub> | 5.2<br><sub>11,6,6,6,3</sub> |  | 3.9<br><sub>8,3,5,7,4</sub> |  | 0.8<br><sub>0,1,1,1,2</sub> |  | 0.5<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.3 | 0.7 | 9.9 |
| Tyus Jones | 96% | 11.9<br><sub>11,11,8,18,13</sub> | 3.3<br><sub>5,3,2,6,3</sub> |  | 1.0<br><sub>0,0,0,1,4</sub> |  | 1.9<br><sub>1,0,1,8,4</sub> |  | 0.3<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.1 | 0.5 | 6.2 |
| Marvin Bagley III | 98% | 11.9<br><sub>19,11,12,14,12</sub> | 5.8<br><sub>8,0,6,10,10</sub> |  | 3.3<br><sub>5,5,4,2,3</sub> |  | 0.6<br><sub>1,0,0,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 9.6 |
| Bryce Hopkins | 67% | 9.4<br><sub>14,-,-,28,3</sub> | 3.0<br><sub>0,-,-,18,3</sub> |  | 1.4<br><sub>2,-,-,4,1</sub> |  | 0.4<br><sub>0,-,-,1,0</sub> |  | 0.1<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Cam Whitmore | 58% | 6.9<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Alpha Diallo | 64% | 6.5<br><sub>-,-,6,4,-</sub> | 3.0<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Zeke Nnaji | 43% | 6.2<br><sub>-,-,-,4,-</sub> | 2.0<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.6 |
| Ryan Nembhard | 52% | 6.1<br><sub>-,-,-,4,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.0 |
| DaRon Holmes II | 48% | 5.5<br><sub>-,-,-,4,-</sub> | 2.4<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 3.8 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.8<br><sub>35,33,36,35,39</sub> | 16.9<br><sub>22,30,14,11,15</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.6<br><sub>3,9,10,4,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,5,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>3,6,4,2,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 1.1 | 1.2 | 26.5 |
| Kevin Durant | 98% | 36.1<br><sub>37,27,33,35,38</sub> | 23.1<br><sub>28,14,12,21,21</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>5,3,3,5,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>1,4,3,2,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 1.1 | 2.9 | 34.0 |
| Amen Thompson | 98% | 35.8<br><sub>39,28,25,32,39</sub> | 16.9<br><sub>15,8,14,11,17</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>3,3,3,8,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>6,1,3,1,0</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.9 | 1.9 | 28.8 |
| Alperen Sengun | 84% | 35.7<br><sub>-,33,38,39,32</sub> | 19.8<br><sub>-,16,26,17,15</sub> | 20.5 · –<br><sub>o 48% · u 52%</sub> | 10.1<br><sub>-,9,7,12,6</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>-,9,10,10,5</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 0.7<br><sub>-,0,1,0,1</sub> | 0.5<br><sub>o 43% · u 57%</sub> | 1.2 | 1.3 | 2.8 | 36.7 |
| Fred VanVleet | 88% | 32.7<br><sub>33,-,27,30,31</sub> | 13.2<br><sub>16,-,8,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>5,-,2,3,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.1<br><sub>6,-,9,3,4</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,-,2,4,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.4 | 1.4 | 21.8 |
| Tari Eason | 98% | 25.5<br><sub>26,19,27,24,23</sub> | 10.5<br><sub>11,8,13,9,2</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>13,3,4,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,3,1,2</sub> |  | 1.2<br><sub>0,2,3,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.8 | 1.0 | 18.2 |
| Marcus Smart | 88% | 22.4<br><sub>17,36,20,18,20</sub> | 8.3<br><sub>8,24,8,4,5</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>2,5,4,1,2</sub> |  | 2.4<br><sub>4,3,4,1,0</sub> |  | 1.2<br><sub>0,7,2,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 1.2 | 13.2 |
| Reed Sheppard | 76% | 20.8<br><sub>-,-,17,21,13</sub> | 9.5<br><sub>-,-,8,14,6</sub> |  | 1.9<br><sub>-,-,1,2,0</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.7<br><sub>-,-,2,3,2</sub> |  | 1.2 | 0.5 | 1.0 | 14.0 |
| Bogdan Bogdanovic | 96% | 9.7<br><sub>11,19,5,5,2</sub> | 3.5<br><sub>6,4,0,0,0</sub> |  | 1.2<br><sub>1,2,0,0,1</sub> |  | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.5 |
| Isaiah Crawford | 52% | 7.1<br><sub>-,19,2,-,-</sub> | 2.5<br><sub>-,8,0,-,-</sub> |  | 1.0<br><sub>-,1,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,2,0,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 3.8 |
| Jae'Sean Tate | 52% | 6.1<br><sub>-,6,2,-,-</sub> | 2.1<br><sub>-,0,0,-,-</sub> |  | 1.4<br><sub>-,3,1,-,-</sub> |  | 0.4<br><sub>-,1,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Bruce Thornton | 52% | 5.9<br><sub>-,6,2,-,-</sub> | 2.2<br><sub>-,5,2,-,-</sub> |  | 1.0<br><sub>-,1,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,1,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.7 |

</details>


### SAS @ PHX
Out: Mark Williams (PHX), Tobias Harris (SAS), Devin Vassell (SAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.4–109.1 | SAS 72% | 1.38 / 3.64 | PHX +8.5 | 226.5 | PHX +8.5 covers 50%; o226.5 50% |
| Expected (weighted by chance each plays) | 117.1–109.4 | SAS 71% | 1.41 / 3.47 | PHX +8.5 | 226.5 | PHX +8.5 covers 51%; o226.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jordan Goodwin (PHX) | Questionable | 55% | 14.0 | 5.1 | 2.9 | 1.4 | 0.7 | 0.9 | 0.1 | 0.5 | 9.4 | small |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 33.7<br><sub>39,27,36,28,28</sub> | 18.5<br><sub>25,17,21,19,13</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>7,7,5,2,7</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>6,8,0,3,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>2,1,1,1,1</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.1 | 0.3 | 2.1 | 28.1 |
| Victor Wembanyama | 98% | 32.9<br><sub>34,24,34,26,24</sub> | 27.7<br><sub>43,12,52,30,29</sub> | 27.5 · –<br><sub>o 47% · u 53%</sub> | 12.5<br><sub>7,11,24,14,7</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,5,2,2,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>3,0,1,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 3.3 | 2.8 | 43.5 |
| Stephon Castle | 98% | 32.5<br><sub>22,26,35,28,24</sub> | 18.1<br><sub>0,16,17,19,14</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>5,5,10,3,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 5.9<br><sub>4,4,3,7,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,2,2,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 0.3 | 3.0 | 29.6 |
| De'Aaron Fox | 98% | 32.2<br><sub>35,22,33,26,22</sub> | 16.2<br><sub>22,12,10,9,8</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>8,2,3,2,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>7,3,4,4,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,1,0,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.4 | 2.3 | 25.4 |
| Julian Champagnie | 98% | 26.8<br><sub>27,22,21,22,21</sub> | 9.3<br><sub>12,8,0,8,14</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>3,6,4,7,4</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>1,0,3,2,0</sub> |  | 1.7<br><sub>3,2,0,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.4 | 0.7 | 15.4 |
| Keldon Johnson | 98% | 26.1<br><sub>24,27,19,27,27</sub> | 10.7<br><sub>2,15,4,3,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>6,7,5,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,1,2,6,4</sub> |  | 0.9<br><sub>0,1,0,0,0</sub> |  | 0.8 | 0.2 | 1.2 | 18.0 |
| Luke Kornet | 98% | 17.9<br><sub>14,17,14,18,15</sub> | 4.4<br><sub>2,8,2,2,6</sub> |  | 5.3<br><sub>8,5,1,6,4</sub> |  | 1.1<br><sub>0,2,2,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.7 | 10.8 |
| Harrison Barnes | 80% | 17.5<br><sub>-,21,13,19,19</sub> | 5.5<br><sub>-,13,4,13,5</sub> |  | 2.0<br><sub>-,0,2,1,3</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.8<br><sub>-,3,1,2,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.3 |
| Carter Bryant | 86% | 15.1<br><sub>11,14,-,3,17</sub> | 4.7<br><sub>6,3,-,0,6</sub> |  | 2.4<br><sub>0,0,-,0,4</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.6<br><sub>2,1,-,0,2</sub> |  | 0.4 | 0.4 | 0.7 | 7.9 |
| Jordan McLaughlin | 63% | 13.4<br><sub>-,8,-,8,12</sub> | 4.2<br><sub>-,0,-,2,3</sub> |  | 1.6<br><sub>-,1,-,2,0</sub> |  | 1.6<br><sub>-,3,-,1,0</sub> |  | 0.5<br><sub>-,0,-,0,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.4 |
| Tarris Reed Jr. | 64% | 9.9<br><sub>-,7,-,3,9</sub> | 3.4<br><sub>-,4,-,0,2</sub> |  | 4.4<br><sub>-,7,-,1,3</sub> |  | 0.4<br><sub>-,0,-,0,1</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.4 | 0.9 | 8.1 |
| David Jones Garcia | 58% | 7.2<br><sub>-,-,-,3,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 36.2<br><sub>39,35,34,34,39</sub> | 25.4<br><sub>20,26,33,30,24</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>2,3,1,1,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>5,5,2,8,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>3,2,2,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 3.0 | 35.0 |
| Dillon Brooks | 98% | 33.0<br><sub>21,34,35,29,37</sub> | 17.2<br><sub>22,18,15,24,11</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>1,8,6,1,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>4,2,0,4,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 1.5 | 23.4 |
| Miles Bridges | 98% | 32.4<br><sub>37,35,31,31,31</sub> | 15.0<br><sub>24,21,18,18,13</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>10,6,7,13,10</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 3.2<br><sub>2,3,5,5,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>2,3,4,3,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 1.3 | 24.9 |
| Jalen Green | 98% | 31.5<br><sub>25,36,32,24,34</sub> | 16.1<br><sub>2,11,22,6,16</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>2,8,2,0,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>2,8,2,3,6</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>0,0,2,0,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.4 | 2.5 | 23.8 |
| Collin Gillespie | 98% | 24.6<br><sub>33,24,23,24,20</sub> | 9.1<br><sub>16,3,2,6,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.6<br><sub>10,2,2,2,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>4,1,0,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 1.1 | 15.9 |
| Oso Ighodaro | 98% | 23.9<br><sub>21,24,23,24,23</sub> | 6.8<br><sub>2,14,9,2,4</sub> | 5.5 · –<br><sub>o 54% · u 46%</sub> | 5.5<br><sub>9,2,7,5,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>5,2,7,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.1 | 15.4 |
| Ryan Dunn | 98% | 18.3<br><sub>11,10,18,25,23</sub> | 5.2<br><sub>5,5,2,11,8</sub> |  | 3.8<br><sub>3,3,6,3,5</sub> |  | 1.2<br><sub>1,1,2,3,3</sub> |  | 0.6<br><sub>1,1,0,1,2</sub> |  | 0.7 | 0.5 | 0.5 | 10.3 |
| Khaman Maluach | 98% | 17.9<br><sub>17,13,16,22,18</sub> | 5.9<br><sub>9,5,6,8,8</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>6,2,6,6,10</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>0,0,2,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.9 | 12.1 |
| Luke Kennard | 98% | 17.3<br><sub>12,18,14,21,14</sub> | 6.2<br><sub>9,6,0,12,11</sub> |  | 2.0<br><sub>1,2,0,1,1</sub> |  | 1.7<br><sub>2,1,1,5,2</sub> |  | 0.8<br><sub>1,2,0,3,3</sub> |  | 0.5 | 0.1 | 0.6 | 9.9 |
| Drew Timme | 16% | 8.0 | 2.9 |  | 1.3 |  | 0.6 |  | 0.2 |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Rasheer Fleming | 47% | 7.6<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |
| Pat Spencer | 63% | 7.0<br><sub>-,-,3,2,-</sub> | 2.4<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 1.1<br><sub>-,-,2,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.0 | 0.5 | 4.4 |
| Duop Reath | 63% | 6.9<br><sub>-,-,7,2,-</sub> | 2.6<br><sub>-,-,7,0,-</sub> |  | 1.3<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea | 52% | 6.6<br><sub>-,-,3,2,-</sub> | 2.5<br><sub>-,-,3,0,-</sub> |  | 0.9<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Koa Peat | 52% | 6.1<br><sub>-,-,3,2,-</sub> | 2.1<br><sub>-,-,2,0,-</sub> |  | 1.5<br><sub>-,-,1,1,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.0 |

</details>


### NOP @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Will Richard (GSW), Yves Missi (NOP), Trey Murphy III (NOP), Trendon Watford (NOP), Zion Williamson (NOP)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.6–123.8 | NOP 22% | 4.64 / 1.27 | GSW -11.5 | 236.5 | GSW -11.5 covers 49%; o229.5 64% |
| Expected (weighted by chance each plays) | 112.3–124.1 | NOP 21% | 4.85 / 1.26 | GSW -11.5 | 236.5 | GSW -11.5 covers 51%; o229.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gary Payton II (GSW) | Questionable | 55% | 13.7 | 6.7 | 2.6 | 1.1 | 0.4 | 0.8 | 0.2 | 0.6 | 10.4 | small |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray | 98% | 34.7<br><sub>-,-,45,35,28</sub> | 19.6<br><sub>-,-,20,7,6</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>-,-,8,2,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>-,-,4,4,3</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,-,1,1,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 2.0 | 0.4 | 3.4 | 32.2 |
| Saddiq Bey | 98% | 33.6<br><sub>26,36,29,31,26</sub> | 19.3<br><sub>25,18,22,17,13</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>6,5,4,5,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,1,3,4,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,2,2,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.2 | 1.6 | 27.8 |
| Jeremiah Fears | 98% | 32.8<br><sub>31,38,34,36,29</sub> | 20.0<br><sub>20,12,19,24,25</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,4,6,5,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.0<br><sub>7,7,2,5,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>1,0,1,0,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.5 | 0.5 | 3.1 | 29.8 |
| Herbert Jones | 98% | 28.3<br><sub>25,28,37,14,20</sub> | 9.0<br><sub>11,9,2,0,4</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>3,4,5,4,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,3,1,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>1,3,0,0,0</sub> |  | 1.3 | 0.4 | 1.4 | 14.6 |
| Derik Queen | 98% | 28.3<br><sub>23,24,27,10,21</sub> | 14.3<br><sub>8,20,20,6,8</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 8.4<br><sub>8,7,9,4,5</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>4,5,6,1,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 1.2 | 0.8 | 2.8 | 26.8 |
| Karlo Matkovic | 96% | 27.4<br><sub>18,29,21,18,19</sub> | 11.2<br><sub>8,25,5,18,3</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>10,6,4,3,3</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>1,1,2,1,2</sub> |  | 1.4<br><sub>2,5,1,4,1</sub> |  | 0.9 | 1.1 | 1.4 | 19.1 |
| Bennedict Mathurin | 98% | 22.4<br><sub>19,13,15,7,9</sub> | 10.5<br><sub>7,4,2,2,6</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>1,0,5,0,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>2,0,1,0,1</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.5 | 16.3 |
| Jordan Poole | 52% | 19.0<br><sub>-,-,-,-,-</sub> | 9.7<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.3 | 1.5 | 14.1 |
| Bryce McGowens | 58% | 17.3<br><sub>15,6,-,-,3</sub> | 6.0<br><sub>3,0,-,-,0</sub> |  | 2.0<br><sub>0,1,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.7 | 0.2 | 0.7 | 9.2 |
| DeAndre Jordan | 26% | 16.0<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 5.8<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.7 | 0.7 | 11.1 |
| Julian Reese | 48% | 10.2<br><sub>3,-,-,-,3</sub> | 3.2<br><sub>2,-,-,-,0</sub> |  | 1.6<br><sub>1,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 5.6 |
| AJ Johnson | 47% | 9.8<br><sub>3,-,-,-,3</sub> | 3.3<br><sub>0,-,-,-,2</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.6 | 0.6 | 4.4 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 91% | 34.3<br><sub>33,37,33,32,39</sub> | 16.9<br><sub>21,17,20,9,15</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>5,8,3,6,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 4.1<br><sub>6,8,2,3,1</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>4,2,3,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.3 | 1.7 | 26.6 |
| Yaxel Lendeborg | 98% | 33.9<br><sub>24,34,29,30,37</sub> | 21.3<br><sub>6,37,16,17,23</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>1,4,5,8,8</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>0,6,5,6,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>1,6,2,1,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 1.0 | 3.2 | 32.8 |
| Stephen Curry | 98% | 32.9<br><sub>31,-,33,28,36</sub> | 28.2<br><sub>31,-,34,29,41</sub> | 28.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>4,-,6,1,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>6,-,7,4,6</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>8,-,5,6,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 2.7 | 37.3 |
| Draymond Green | 91% | 28.6<br><sub>32,-,17,27,34</sub> | 7.2<br><sub>2,-,4,2,2</sub> | 5.5 · –<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,-,4,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>9,-,2,11,13</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>0,-,0,0,0</sub> |  | 1.1 | 0.8 | 2.4 | 19.4 |
| Georges Niang | 97% | 21.8<br><sub>19,21,22,22,25</sub> | 8.8<br><sub>11,3,13,13,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>5,1,4,4,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,2,3,3,1</sub> |  | 1.5<br><sub>3,1,1,2,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5 | 0.2 | 1.0 | 13.3 |
| De'Anthony Melton | 98% | 21.3<br><sub>21,28,28,17,17</sub> | 9.7<br><sub>16,21,2,5,4</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>5,6,7,6,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>3,3,2,2,1</sub> |  | 1.4<br><sub>4,6,0,0,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 1.3 | 15.2 |
| Brandon Williams | 86% | 18.8<br><sub>17,25,-,21,17</sub> | 10.9<br><sub>9,17,-,10,9</sub> |  | 2.4<br><sub>2,3,-,1,0</sub> |  | 2.8<br><sub>1,3,-,4,2</sub> |  | 0.6<br><sub>0,2,-,0,0</sub> |  | 0.8 | 0.3 | 1.6 | 16.1 |
| Al Horford | 98% | 17.0<br><sub>17,22,-,18,13</sub> | 5.9<br><sub>3,9,-,8,2</sub> |  | 3.9<br><sub>2,5,-,5,5</sub> |  | 1.5<br><sub>0,2,-,1,4</sub> |  | 0.9<br><sub>1,3,-,2,0</sub> |  | 0.4 | 0.8 | 0.5 | 11.3 |
| Gui Santos | 82% | 16.4<br><sub>16,9,-,-,12</sub> | 6.9<br><sub>2,4,-,-,3</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>5,3,-,-,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>1,1,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.7 | 0.3 | 1.1 | 11.6 |
| Charles Bassey | 96% | 12.8<br><sub>9,20,23,14,11</sub> | 6.3<br><sub>6,6,19,8,8</sub> |  | 5.4<br><sub>4,10,8,7,4</sub> |  | 0.6<br><sub>1,2,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.1 | 0.7 | 12.3 |
| Graham Ike | 88% | 8.1<br><sub>-,6,7,1,-</sub> | 3.5<br><sub>-,2,0,0,-</sub> |  | 2.0<br><sub>-,2,0,1,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| LJ Cryer | 58% | 7.4<br><sub>-,2,1,1,-</sub> | 3.6<br><sub>-,0,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.0 | 0.3 | 4.9 |
| Malevy Leons | 48% | 6.8<br><sub>-,-,-,1,-</sub> | 2.1<br><sub>-,-,-,0,-</sub> |  | 1.3<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.3 | 3.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-09/`._
