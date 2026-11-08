# NBA model · Sat 07 Nov 2026 (US date)

Updated **Sun 08 Nov, 12:04 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-07/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Meleek Thomas 3PM over 1.5 (2+) | NYK @ CLE | draftkings | 2.43 | 1.97 | 1.61 | 62.0% | 50.0% | 50.9% | +23.6% | +50.6% | 2.0% |
| ORL to win | ORL @ GSW | draftkings | 3.50 | 3.32 | 4.13 | 24.2% | 30.1% | 30.1% | +5.5% | -15.2% | 0.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| WAS to win | WAS @ OKC | betfair_ex_au | 5.75 | 5.44 | 3.59 | 27.9% | 18.4% | 18.4% | +5.6% | +60.1% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Will Richard PTS under 4.5 | ORL @ GSW | unibet | 2.12 | 2.00 | 1.67 | 60.0% | 49.2% | 50.0% | +6.0% | +27.3% | 1.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| NYK @ CLE | Sun 08 Nov 12:00 | 115.5–107.8 | NYK 71% | 1.41 / 3.42 | CLE +7.5 | 223.5 | CLE +4.5 covers 40%; o222.5 51% |
| WAS @ OKC | Sun 08 Nov 12:00 | 110.9–119.2 | WAS 28% | 3.59 / 1.39 | OKC -8.5 | 229.5 | OKC -12.5 covers 38%; o223.5 64% |
| ORL @ GSW | Sun 08 Nov 12:30 | 108.0–117.9 | ORL 24% | 4.13 / 1.32 | GSW -9.5 | 225.5 | GSW -7.5 covers 57%; o220.5 61% |
| HOU @ PHX | Sun 08 Nov 13:00 | 115.5–109.6 | HOU 66% | 1.51 / 2.96 | PHX +5.5 | 224.5 | PHX +6.5 covers 52%; o223.5 53% |
| SAS @ POR | Sun 08 Nov 14:00 | 114.3–108.7 | SAS 65% | 1.54 / 2.87 | POR +5.5 | 222.5 | POR +5.5 covers 49%; o229.5 36% |

### NYK @ CLE
Out: Jarrett Allen (CLE), Sam Merrill (CLE), Jaylon Tyson (CLE), Josh Hart (NYK)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Meleek Thomas 3PM over 1.5 (2+) | NYK @ CLE | draftkings | 2.43 | 1.97 | 1.61 | 62.0% | 50.0% | 50.9% | +23.6% | +50.6% | 2.0% |
| Jalen Brunson PTS under 25.5 | NYK @ CLE | unibet | 2.08 | 2.03 | 1.77 | 56.4% | 48.8% | 49.3% | +2.6% | +17.3% | 0.6% |
| Evan Mobley PTS under 17.5 | NYK @ CLE | tab | 1.95 | 1.94 | 1.66 | 60.2% | 50.9% | 51.6% | +0.7% | +17.5% | 0.2% |
| Meleek Thomas PTS under 11.5 | NYK @ CLE | draftkings | 1.93 | 1.93 | 2.00 | 50.1% | 51.9% | 51.8% | +0.2% | -3.1% | 0.1% |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 100% | 36.8<br><sub>36,35,35,34,28</sub> | 25.2<br><sub>23,38,24,19,33</sub> | 26.5 · 25.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>1,1,5,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>7,7,6,6,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>0,6,3,4,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.1 | 0.2 | 2.6 | 35.0 |
| OG Anunoby | 100% | 35.6<br><sub>36,31,34,38,24</sub> | 18.2<br><sub>13,23,9,18,18</sub> | 16.5 · 16.5<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>7,6,4,4,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,1,3,2,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>1,2,1,3,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.6 | 0.8 | 1.6 | 26.2 |
| Karl-Anthony Towns | 100% | 33.7<br><sub>33,28,35,35,25</sub> | 18.9<br><sub>27,19,22,11,17</sub> | 18.5 · 19.5<br><sub>o 48% · u 52%</sub> | 13.2<br><sub>20,13,12,16,12</sub> | 13.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>3,5,3,5,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,3,3,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.7 | 2.9 | 35.8 |
| Landry Shamet | 100% | 30.6<br><sub>28,32,16,30,25</sub> | 11.1<br><sub>13,14,0,22,7</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>2,1,0,1,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,5,0,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>3,4,0,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.2 | 0.9 | 15.1 |
| Mikal Bridges | 100% | 29.0<br><sub>32,13,30,16,22</sub> | 9.7<br><sub>12,3,12,6,7</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>3,0,5,2,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.6<br><sub>4,0,2,0,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>4,1,2,0,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 1.0 | 15.4 |
| Miles McBride | 98% | 20.1<br><sub>17,14,24,17,11</sub> | 7.4<br><sub>5,3,10,6,7</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,5,3,1,1</sub> |  | 1.6<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.2 | 0.5 | 10.7 |
| Jordan Clarkson | 88% | 15.0<br><sub>-,17,9,11,15</sub> | 7.3<br><sub>-,18,4,7,10</sub> |  | 1.9<br><sub>-,3,3,0,1</sub> |  | 1.0<br><sub>-,1,0,0,1</sub> |  | 0.6<br><sub>-,2,0,1,2</sub> |  | 0.4 | 0.1 | 0.8 | 10.2 |
| Tyler Kolek | 86% | 14.2<br><sub>11,18,13,5,11</sub> | 4.3<br><sub>2,9,2,2,0</sub> |  | 1.8<br><sub>1,2,1,1,0</sub> |  | 3.5<br><sub>3,9,4,1,5</sub> |  | 0.5<br><sub>0,3,0,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 9.5 |
| Andre Drummond | 98% | 14.1<br><sub>14,15,12,13,12</sub> | 4.9<br><sub>10,4,3,4,6</sub> | 4.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>8,11,6,9,9</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>1,1,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 15% · u 85%</sub> | 0.5 | 0.4 | 0.8 | 12.2 |
| Jose Alvarado | 97% | 14.1<br><sub>-,-,-,9,9</sub> | 4.9<br><sub>-,-,-,0,0</sub> |  | 1.8<br><sub>-,-,-,0,0</sub> |  | 2.1<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.1 | 0.8 | 8.8 |
| Mohamed Diawara | 52% | 12.8<br><sub>1,-,-,6,21</sub> | 4.2<br><sub>0,-,-,0,8</sub> |  | 2.2<br><sub>0,-,-,1,6</sub> |  | 1.2<br><sub>0,-,-,0,4</sub> |  | 0.5<br><sub>0,-,-,0,1</sub> |  | 0.3 | 0.1 | 0.6 | 7.7 |
| Dalton Knecht | 52% | 12.2<br><sub>-,-,-,-,16</sub> | 5.3<br><sub>-,-,-,-,10</sub> |  | 2.4<br><sub>-,-,-,-,7</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,2</sub> |  | 0.3 | 0.2 | 0.4 | 8.4 |
| James Wiseman | 52% | 8.7<br><sub>1,-,-,-,10</sub> | 2.8<br><sub>0,-,-,-,8</sub> |  | 2.8<br><sub>1,-,-,-,8</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.3 | 0.6 | 6.0 |
| Tyler Nickel | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Jaden Akins | 38% | 8.5<br><sub>2,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |
| Pacome Dadiet | 48% | 8.3<br><sub>1,-,-,-,9</sub> | 3.0<br><sub>0,-,-,-,4</sub> |  | 1.5<br><sub>1,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.0 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 100% | 36.2<br><sub>36,26,33,35,30</sub> | 17.3<br><sub>24,13,14,19,17</sub> | 16.5 · 17.5<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>5,6,4,9,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>4,7,6,6,3</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.5<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.5 | 3.6 | 28.1 |
| Donovan Mitchell | 100% | 36.1<br><sub>33,24,36,33,33</sub> | 22.3<br><sub>22,15,17,27,23</sub> | 22.5 · 22.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>3,4,5,3,7</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>3,3,11,6,8</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>1,2,4,5,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.4 | 2.9 | 32.1 |
| Evan Mobley | 100% | 35.0<br><sub>33,25,33,33,32</sub> | 16.6<br><sub>11,27,16,16,22</sub> | 17.5 · 17.5<br><sub>o 48% · u 52%</sub> | 8.1<br><sub>4,5,7,10,6</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>7,3,4,3,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>0,3,1,1,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 1.7 | 1.8 | 28.1 |
| Peyton Watson | 100% | 31.6<br><sub>22,22,-,-,28</sub> | 13.3<br><sub>4,5,-,-,13</sub> | 11.5 · 11.5<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>4,2,-,-,9</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>3,6,-,-,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>0,1,-,-,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 1.3 | 1.7 | 20.5 |
| Meleek Thomas | 100% | 30.2<br><sub>-,23,26,18,27</sub> | 12.3<br><sub>-,13,17,9,12</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>-,1,5,1,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>-,2,1,0,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>-,3,3,3,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 1.6 | 17.2 |
| Mario Hezonja | 98% | 24.9<br><sub>17,20,27,23,27</sub> | 9.5<br><sub>10,8,12,12,15</sub> | 10.5 · 10.5<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>6,11,8,8,10</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>2,4,3,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>2,1,3,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.6 | 0.3 | 1.0 | 17.6 |
| Tyrese Proctor | 88% | 21.5<br><sub>20,18,19,22,19</sub> | 7.6<br><sub>7,9,10,11,3</sub> | 5.5 · 6.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>6,4,4,1,6</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,5,2,0,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>1,3,2,2,0</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.8 | 0.1 | 1.0 | 12.9 |
| Thomas Bryant | 66% | 16.2<br><sub>-,11,5,13,16</sub> | 7.7<br><sub>-,11,4,8,13</sub> |  | 4.0<br><sub>-,2,0,0,6</sub> |  | 0.6<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,3,0,1,1</sub> |  | 0.4 | 0.5 | 0.8 | 12.3 |
| Craig Porter Jr. | 86% | 13.1<br><sub>4,16,8,14,3</sub> | 2.8<br><sub>0,2,0,0,0</sub> |  | 2.2<br><sub>1,2,4,1,0</sub> |  | 1.8<br><sub>0,4,1,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.4 | 0.6 | 6.7 |
| Riley Minix | 35% | 12.4<br><sub>-,6,-,-,-</sub> | 4.1<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.5 |
| Ernest Udeh Jr. | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Norchad Omier | 64% | 7.7<br><sub>-,-,-,-,3</sub> | 2.2<br><sub>-,-,-,-,0</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 0.7<br><sub>-,-,-,-,1</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.7 |

</details>


### WAS @ OKC
Out: Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC), Justin Champagnie (WAS), Anthony Davis (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaiah Hartenstein PTS over 8.5 (9+) | WAS @ OKC | unibet | 2.07 | 2.00 | 1.79 | 56.0% | 49.5% | 50.0% | +3.4% | +16.0% | 0.8% |
| Aday Mara PTS over 7.5 (8+) | WAS @ OKC | sportsbet | 1.78 | 1.73 | 1.53 | 65.2% | 57.2% | 57.8% | +3.0% | +16.2% | 1.0% |
| Kenrich Williams PTS over 7.5 (8+) | WAS @ OKC | draftkings | 1.96 | 1.91 | 1.55 | 64.4% | 51.3% | 52.3% | +2.6% | +26.3% | 0.7% |
| Aday Mara PTS over 8.5 (9+) | WAS @ OKC | pointsbetau | 2.05 | 2.01 | 1.78 | 56.3% | 49.1% | 49.6% | +1.8% | +15.5% | 0.4% |
| Bilal Coulibaly PTS over 8.5 (9+) | WAS @ OKC | tab | 1.95 | 1.94 | 1.60 | 62.4% | 50.6% | 51.5% | +0.5% | +21.9% | 0.1% |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 100% | 33.9<br><sub>34,38,34,34,37</sub> | 18.8<br><sub>14,21,15,18,23</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,7,3,2,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 9.3<br><sub>8,9,9,6,10</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>1,1,2,2,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 3.6 | 31.4 |
| Kyshawn George | 100% | 33.4<br><sub>38,32,37,35,39</sub> | 18.5<br><sub>8,12,22,25,33</sub> | 17.5 · 16.5<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>2,3,4,4,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 4.9<br><sub>11,3,5,7,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>0,4,4,3,5</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 1.0 | 2.8 | 28.9 |
| AJ Dybantsa | 100% | 32.6<br><sub>27,30,33,32,36</sub> | 14.8<br><sub>19,17,21,9,11</sub> | 18.5 · 18.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>2,8,5,6,9</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>2,1,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.1 | 0.3 | 2.0 | 23.3 |
| Bilal Coulibaly | 100% | 27.8<br><sub>27,22,33,23,24</sub> | 10.7<br><sub>17,1,7,6,9</sub> | 8.5 · 7.5<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>2,5,1,2,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,1,2,2,0</sub> |  | 1.0<br><sub>1,0,0,0,1</sub> |  | 1.0 | 0.9 | 1.5 | 16.8 |
| Alex Sarr | 100% | 27.7<br><sub>26,29,-,23,30</sub> | 12.9<br><sub>18,3,-,11,13</sub> | 12.5 · 11.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>4,8,-,9,8</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>2,0,-,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>2,1,-,0,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.8 | 1.5 | 1.7 | 22.6 |
| Tre Johnson | 88% | 23.1<br><sub>-,13,22,14,27</sub> | 9.2<br><sub>-,4,4,3,23</sub> | 10.5 · 10.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>-,2,3,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>-,0,0,0,1</sub> |  | 1.2<br><sub>-,0,0,1,5</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.2 | 13.0 |
| Bub Carrington | 98% | 20.8<br><sub>20,20,19,19,15</sub> | 7.5<br><sub>3,9,3,0,5</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>1,4,4,1,1</sub> |  | 2.7<br><sub>3,2,4,2,1</sub> |  | 1.1<br><sub>0,3,1,0,1</sub> |  | 0.5 | 0.2 | 1.5 | 12.6 |
| Deandre Ayton | 98% | 19.2<br><sub>12,17,24,11,23</sub> | 6.6<br><sub>10,3,4,5,8</sub> | 6.5 · 7.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>3,3,6,4,11</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>0,1,2,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 1.1 | 13.3 |
| Khris Middleton | 52% | 14.5<br><sub>23,5,-,-,-</sub> | 5.3<br><sub>4,0,-,-,-</sub> |  | 2.3<br><sub>3,0,-,-,-</sub> |  | 0.9<br><sub>2,0,-,-,-</sub> |  | 0.5<br><sub>1,0,-,-,-</sub> |  | 0.4 | 0.1 | 1.1 | 8.6 |
| Will Riley | 88% | 13.0<br><sub>-,1,4,13,9</sub> | 5.4<br><sub>-,0,0,0,7</sub> |  | 1.7<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,0,1,0,0</sub> |  | 0.5<br><sub>-,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.8 | 8.0 |
| Anthony Gill | 26% | 10.2<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 6.1 |
| Tre Mann | 48% | 7.2<br><sub>-,1,-,3,-</sub> | 3.1<br><sub>-,0,-,2,-</sub> |  | 1.0<br><sub>-,0,-,0,-</sub> |  | 0.8<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.0 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 32.7<br><sub>28,31,39,35,30</sub> | 31.8<br><sub>21,26,43,42,28</sub> | 32.5 · 31.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>6,4,3,4,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.8<br><sub>2,3,8,8,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>1,3,4,5,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.8 | 2.7 | 42.9 |
| Ajay Mitchell | 100% | 29.4<br><sub>28,26,35,32,30</sub> | 18.7<br><sub>29,6,20,23,35</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>4,3,5,7,1</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.5<br><sub>3,5,1,4,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>2,0,0,1,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.3 | 1.8 | 27.2 |
| Aday Mara | 100% | 27.0<br><sub>21,28,20,25,18</sub> | 9.9<br><sub>6,7,10,9,9</sub> | 8.5 · 7.5<br><sub>o 50% · u 50%</sub> | 8.3<br><sub>3,9,9,5,7</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,3,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 2.1 | 1.8 | 19.6 |
| Jared McCain | 98% | 26.7<br><sub>29,28,27,25,29</sub> | 14.3<br><sub>10,10,7,9,21</sub> | 12.5 · 13.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>4,4,9,1,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>4,2,2,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>0,0,0,1,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.1 | 1.4 | 19.5 |
| Isaiah Hartenstein | 100% | 26.0<br><sub>26,25,28,26,26</sub> | 9.9<br><sub>10,10,5,3,2</sub> | 8.5 · 8.5<br><sub>o 50% · u 50%</sub> | 10.5<br><sub>14,7,14,12,6</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,0,4,4,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.8 | 1.5 | 24.0 |
| Kenrich Williams | 100% | 25.3<br><sub>17,21,31,29,19</sub> | 9.9<br><sub>7,11,12,13,4</sub> | 7.5 · 8.5<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>3,7,3,4,6</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>0,3,1,2,3</sub> |  | 1.4<br><sub>1,3,2,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 1.0 | 18.2 |
| Bennett Stirtz | 98% | 22.1<br><sub>28,26,12,22,24</sub> | 7.6<br><sub>8,11,9,16,12</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>0,1,2,1,1</sub> |  | 1.6<br><sub>3,3,0,1,2</sub> |  | 1.1<br><sub>1,3,3,4,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 0.8 | 10.9 |
| Alex Caruso | 98% | 21.9<br><sub>-,-,-,20,20</sub> | 9.2<br><sub>-,-,-,7,5</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,-,-,4,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.4 | 0.9 | 15.7 |
| Micah Peavy | 80% | 18.7<br><sub>5,14,16,26,18</sub> | 5.0<br><sub>0,2,8,2,7</sub> |  | 3.7<br><sub>0,1,5,9,4</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>0,0,2,0,1</sub> |  | 0.7 | 0.2 | 0.9 | 9.8 |
| Josh Dix | 67% | 16.4<br><sub>24,9,12,-,15</sub> | 5.4<br><sub>2,7,0,-,5</sub> |  | 1.8<br><sub>2,0,1,-,2</sub> |  | 0.6<br><sub>0,0,0,-,1</sub> |  | 0.5<br><sub>0,1,0,-,1</sub> |  | 0.5 | 0.2 | 0.6 | 7.8 |
| Brooks Barnhizer | 63% | 9.9<br><sub>14,6,-,-,5</sub> | 2.6<br><sub>3,5,-,-,0</sub> |  | 2.2<br><sub>2,2,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.5 |
| Dalen Terry | 63% | 8.5<br><sub>-,-,-,-,5</sub> | 3.0<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.4 | 5.4 |

</details>


### ORL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Paolo Banchero (ORL), Desmond Bane (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 36.6<br><sub>34,39,40,38,38</sub> | 23.9<br><sub>15,26,14,24,15</sub> | – · 24.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>4,5,6,3,8</sub> |  | 7.5<br><sub>5,11,12,6,15</sub> |  | 1.6<br><sub>0,2,1,1,0</sub> |  | 1.5 | 0.3 | 3.9 | 37.5 |
| Wendell Carter Jr. | 98% | 33.6<br><sub>26,39,35,34,34</sub> | 14.1<br><sub>3,20,7,6,27</sub> | – · 13.5<br><sub>o 51% · u 49%</sub> | 8.5<br><sub>10,7,10,9,13</sub> |  | 2.3<br><sub>3,1,0,0,2</sub> |  | 0.9<br><sub>0,1,1,0,2</sub> |  | 1.2 | 0.6 | 2.0 | 24.9 |
| Tristan da Silva | 98% | 33.4<br><sub>31,23,35,32,30</sub> | 15.3<br><sub>20,8,23,10,18</sub> | – · 14.5<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>3,0,10,4,2</sub> |  | 2.6<br><sub>1,0,2,3,1</sub> |  | 2.4<br><sub>4,2,5,2,4</sub> |  | 1.0 | 0.3 | 2.0 | 22.6 |
| Anthony Black | 98% | 33.3<br><sub>22,31,33,-,31</sub> | 17.9<br><sub>8,17,23,-,10</sub> | – · 17.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>2,6,8,-,7</sub> |  | 5.0<br><sub>1,10,3,-,6</sub> |  | 1.8<br><sub>0,3,1,-,1</sub> |  | 1.9 | 0.6 | 2.9 | 27.2 |
| Jase Richardson | 91% | 28.8<br><sub>14,33,26,29,26</sub> | 11.6<br><sub>10,4,4,9,10</sub> | – · 9.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>1,6,1,1,2</sub> |  | 3.3<br><sub>1,2,3,5,3</sub> |  | 1.2<br><sub>2,0,0,0,2</sub> |  | 1.2 | 0.3 | 1.6 | 17.8 |
| Jamal Cain | 98% | 26.8<br><sub>16,15,18,25,25</sub> | 10.6<br><sub>9,13,5,10,5</sub> | – · 8.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>1,0,1,3,5</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> |  | 1.3<br><sub>0,3,1,2,1</sub> |  | 0.8 | 0.3 | 1.5 | 16.3 |
| Jevon Carter | 63% | 18.7<br><sub>22,-,-,18,3</sub> | 6.8<br><sub>6,-,-,5,0</sub> |  | 1.8<br><sub>0,-,-,1,0</sub> |  | 2.0<br><sub>3,-,-,4,0</sub> |  | 1.1<br><sub>2,-,-,1,0</sub> |  | 0.8 | 0.2 | 0.8 | 10.6 |
| Alex Morales | 67% | 14.1<br><sub>7,9,-,14,6</sub> | 3.8<br><sub>2,0,-,3,0</sub> |  | 1.9<br><sub>2,1,-,2,0</sub> |  | 1.1<br><sub>1,0,-,0,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.6 | 0.1 | 0.9 | 6.9 |
| Nikola Vucevic | 98% | 13.4<br><sub>16,6,7,14,4</sub> | 5.8<br><sub>5,3,2,7,0</sub> |  | 3.6<br><sub>4,1,4,6,0</sub> |  | 1.5<br><sub>2,0,2,1,0</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.4 | 0.6 | 10.9 |
| Goga Bitadze | 67% | 13.2<br><sub>11,6,5,-,8</sub> | 5.2<br><sub>6,2,0,-,4</sub> |  | 4.4<br><sub>0,4,1,-,5</sub> |  | 1.1<br><sub>1,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.7 | 0.8 | 10.6 |
| Colin Castleton | 52% | 8.8<br><sub>7,-,-,-,2</sub> | 2.9<br><sub>2,-,-,-,0</sub> |  | 2.6<br><sub>2,-,-,-,0</sub> |  | 0.6<br><sub>0,-,-,-,1</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 6.1 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 91% | 30.5<br><sub>32,33,37,33,32</sub> | 14.8<br><sub>8,21,17,20,9</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>5,5,8,3,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>6,6,8,2,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,4,2,3,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 1.6 | 23.4 |
| Yaxel Lendeborg | 98% | 30.4<br><sub>35,24,34,29,30</sub> | 19.4<br><sub>26,6,37,16,17</sub> | 18.5 · 17.5<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>9,1,4,5,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>1,0,6,5,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>2,1,6,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.6 | 2.5 | 29.3 |
| Stephen Curry | 98% | 30.2<br><sub>32,31,-,33,28</sub> | 25.1<br><sub>44,31,-,34,29</sub> | 26.5 · 25.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>8,4,-,6,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 4.6<br><sub>6,6,-,7,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>6,8,-,5,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 2.7 | 33.4 |
| Draymond Green | 91% | 25.0<br><sub>32,32,-,17,27</sub> | 6.0<br><sub>3,2,-,4,2</sub> | 4.5 · 4.5<br><sub>o 54% · u 46%</sub> | 4.8<br><sub>9,4,-,4,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>6,9,-,2,11</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.7<br><sub>0,0,-,0,0</sub> |  | 1.0 | 0.6 | 2.1 | 15.9 |
| De'Anthony Melton | 98% | 19.7<br><sub>20,21,28,28,17</sub> | 8.9<br><sub>8,16,21,2,5</sub> | 7.5 · 8.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>6,5,6,7,6</sub> |  | 2.0<br><sub>0,3,3,2,2</sub> |  | 1.3<br><sub>2,4,6,0,0</sub> |  | 1.2 | 0.4 | 1.3 | 14.2 |
| Al Horford | 98% | 17.7<br><sub>18,17,22,-,18</sub> | 5.8<br><sub>4,3,9,-,8</sub> |  | 3.7<br><sub>5,2,5,-,5</sub> |  | 1.4<br><sub>2,0,2,-,1</sub> |  | 0.8<br><sub>0,1,3,-,2</sub> |  | 0.4 | 0.7 | 0.6 | 10.9 |
| Georges Niang | 97% | 17.6<br><sub>23,19,21,22,22</sub> | 7.2<br><sub>7,11,3,13,13</sub> | 7.5 · 7.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>3,5,1,4,4</sub> |  | 1.1<br><sub>2,1,2,3,3</sub> |  | 1.1<br><sub>1,3,1,1,2</sub> |  | 0.4 | 0.2 | 0.8 | 10.8 |
| Brandon Williams | 80% | 17.4<br><sub>14,17,25,-,21</sub> | 10.5<br><sub>11,9,17,-,10</sub> |  | 2.3<br><sub>3,2,3,-,1</sub> |  | 2.7<br><sub>1,1,3,-,4</sub> |  | 0.6<br><sub>0,0,2,-,0</sub> |  | 0.7 | 0.3 | 1.5 | 15.5 |
| Gui Santos | 86% | 15.9<br><sub>-,16,9,-,-</sub> | 6.7<br><sub>-,2,4,-,-</sub> |  | 3.1<br><sub>-,5,3,-,-</sub> |  | 1.5<br><sub>-,1,1,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.7 | 0.2 | 1.0 | 11.3 |
| Will Richard | 98% | 15.1<br><sub>23,13,22,28,16</sub> | 4.2<br><sub>6,3,3,6,10</sub> | 4.5 · –<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>3,3,0,5,0</sub> |  | 0.9<br><sub>0,2,3,0,2</sub> |  | 0.5<br><sub>0,1,1,2,2</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.1 | 0.5 | 6.9 |
| Charles Bassey | 96% | 12.9<br><sub>2,9,20,23,14</sub> | 6.0<br><sub>0,6,6,19,8</sub> |  | 4.9<br><sub>0,4,10,8,7</sub> |  | 0.7<br><sub>0,1,2,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.8 | 11.6 |
| Gary Payton II | 98% | 12.1<br><sub>10,8,15,20,10</sub> | 5.5<br><sub>2,2,5,2,9</sub> |  | 2.2<br><sub>2,4,2,2,0</sub> |  | 0.9<br><sub>1,0,2,1,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.8 | 0.2 | 0.5 | 8.5 |
| Graham Ike | 88% | 7.0<br><sub>-,-,6,7,1</sub> | 3.0<br><sub>-,-,2,0,0</sub> |  | 1.7<br><sub>-,-,2,0,1</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| LJ Cryer | 71% | 6.4<br><sub>-,-,2,1,1</sub> | 3.2<br><sub>-,-,0,0,0</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.1 | 0.0 | 0.4 | 4.4 |
| Malevy Leons | 52% | 5.9<br><sub>-,-,-,-,1</sub> | 1.9<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 3.4 |

</details>


### HOU @ PHX
Out: Jordan Goodwin (PHX), Drew Timme (PHX), Mark Williams (PHX), Steven Adams (HOU), Clint Capela (HOU)

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.3<br><sub>30,35,33,36,35</sub> | 15.9<br><sub>14,22,30,14,11</sub> |  | 7.2<br><sub>2,3,9,10,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>2,2,5,0,2</sub> |  | 2.3<br><sub>3,3,6,4,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.8 | 1.5 | 25.3 |
| Alperen Sengun | 76% | 36.0<br><sub>-,-,33,38,39</sub> | 21.6<br><sub>-,-,16,26,17</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 9.9<br><sub>-,-,9,7,12</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>-,-,9,10,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>-,-,0,1,0</sub> |  | 1.4 | 1.1 | 3.4 | 38.1 |
| Kevin Durant | 98% | 35.8<br><sub>31,37,27,33,35</sub> | 22.6<br><sub>18,28,14,12,21</sub> |  | 5.7<br><sub>5,5,3,3,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.5<br><sub>4,1,4,3,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 1.1 | 3.4 | 32.8 |
| Amen Thompson | 98% | 35.2<br><sub>33,39,28,25,32</sub> | 17.0<br><sub>23,15,8,14,11</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>4,3,3,3,8</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>3,6,1,3,1</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.5 | 28.6 |
| Fred VanVleet | 86% | 32.7<br><sub>29,33,-,27,30</sub> | 13.2<br><sub>24,16,-,8,18</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>6,5,-,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.1<br><sub>5,6,-,9,3</sub> |  | 2.5<br><sub>4,3,-,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.4 | 1.7 | 21.9 |
| Tari Eason | 98% | 25.6<br><sub>31,26,19,27,24</sub> | 10.1<br><sub>5,11,8,13,9</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>9,13,3,4,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,2,2,3,1</sub> |  | 1.1<br><sub>1,0,2,3,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.7 | 1.2 | 17.5 |
| Reed Sheppard | 71% | 22.8<br><sub>23,-,-,17,21</sub> | 10.5<br><sub>7,-,-,8,14</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>3,-,-,1,2</sub> |  | 3.0<br><sub>4,-,-,1,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>1,-,-,2,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.5 | 1.3 | 15.8 |
| Marcus Smart | 83% | 22.7<br><sub>-,17,36,20,18</sub> | 8.4<br><sub>-,8,24,8,4</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>-,2,5,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.6<br><sub>-,4,3,4,1</sub> |  | 1.2<br><sub>-,0,7,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.3 | 1.5 | 13.6 |
| Bogdan Bogdanovic | 93% | 11.6<br><sub>15,11,19,5,5</sub> | 4.3<br><sub>16,6,4,0,0</sub> |  | 1.4<br><sub>2,1,2,0,0</sub> |  | 1.0<br><sub>4,0,1,1,0</sub> |  | 0.6<br><sub>4,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.7 |
| Oscar Tshiebwe | 88% | 8.9<br><sub>14,11,4,7,2</sub> | 3.8<br><sub>7,0,2,4,2</sub> |  | 3.5<br><sub>5,5,1,1,0</sub> |  | 0.5<br><sub>2,0,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 7.8 |
| Isaiah Crawford | 58% | 7.2<br><sub>5,-,19,2,-</sub> | 2.3<br><sub>3,-,8,0,-</sub> |  | 1.1<br><sub>0,-,1,0,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.2<br><sub>1,-,2,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.8 |
| Jae'Sean Tate | 63% | 6.0<br><sub>4,-,6,2,-</sub> | 2.0<br><sub>0,-,0,0,-</sub> |  | 1.4<br><sub>0,-,3,1,-</sub> |  | 0.4<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Bruce Thornton | 63% | 5.9<br><sub>3,-,6,2,-</sub> | 1.9<br><sub>5,-,5,2,-</sub> |  | 1.0<br><sub>0,-,1,0,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>1,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.4 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 35.7<br><sub>34,39,35,34,34</sub> | 25.6<br><sub>3,20,26,33,30</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>2,2,3,1,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.0<br><sub>7,5,5,2,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,3,2,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.3 | 3.4 | 35.2 |
| Miles Bridges | 98% | 32.8<br><sub>32,37,35,31,31</sub> | 15.3<br><sub>17,24,21,18,18</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 6.6<br><sub>8,10,6,7,13</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>4,2,3,5,5</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>2,2,3,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.5 | 1.4 | 25.0 |
| Dillon Brooks | 98% | 32.3<br><sub>33,21,34,35,29</sub> | 17.7<br><sub>19,22,18,15,24</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>5,1,8,6,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>5,2,4,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.2<br><sub>3,4,2,0,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 1.8 | 23.7 |
| Jalen Green | 98% | 30.5<br><sub>31,25,36,32,24</sub> | 16.1<br><sub>20,2,11,22,6</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>4,2,8,2,0</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>4,2,8,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>1,0,0,2,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.4 | 2.5 | 23.2 |
| Collin Gillespie | 98% | 26.4<br><sub>23,33,24,23,24</sub> | 10.0<br><sub>9,16,3,2,6</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,3,1,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.9<br><sub>2,10,2,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>3,4,1,0,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.2 | 1.3 | 17.0 |
| Oso Ighodaro | 98% | 23.9<br><sub>-,21,24,23,24</sub> | 6.8<br><sub>-,2,14,9,2</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>-,9,2,7,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>-,5,2,7,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.2 | 15.2 |
| Luke Kennard | 98% | 19.2<br><sub>16,12,18,14,21</sub> | 6.3<br><sub>9,9,6,0,12</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>1,1,2,0,1</sub> |  | 1.9<br><sub>2,2,1,1,5</sub> |  | 0.8<br><sub>3,1,2,0,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.1 | 0.8 | 10.2 |
| Khaman Maluach | 98% | 17.9<br><sub>26,17,13,16,22</sub> | 5.7<br><sub>12,9,5,6,8</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>7,6,2,6,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>1,0,0,2,2</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 1.0 | 11.7 |
| Ryan Dunn | 97% | 17.1<br><sub>14,11,10,18,25</sub> | 4.9<br><sub>6,5,5,2,11</sub> |  | 3.5<br><sub>2,3,3,6,3</sub> |  | 1.1<br><sub>1,1,1,2,3</sub> |  | 0.5<br><sub>1,1,1,0,1</sub> |  | 0.7 | 0.5 | 0.6 | 9.5 |
| Rasheer Fleming | 52% | 8.1<br><sub>3,-,-,-,-</sub> | 2.8<br><sub>0,-,-,-,-</sub> |  | 1.4<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.5 |
| Pat Spencer | 80% | 7.2<br><sub>-,-,-,3,2</sub> | 2.5<br><sub>-,-,-,0,0</sub> |  | 0.9<br><sub>-,-,-,0,0</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Duop Reath | 80% | 7.1<br><sub>7,-,-,7,2</sub> | 2.6<br><sub>5,-,-,7,0</sub> |  | 1.3<br><sub>3,-,-,0,0</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.2<br><sub>1,-,-,1,0</sub> |  | 0.2 | 0.2 | 0.2 | 4.2 |
| Jamaree Bouyea | 64% | 6.9<br><sub>3,-,-,3,2</sub> | 2.6<br><sub>2,-,-,3,0</sub> |  | 0.9<br><sub>0,-,-,0,0</sub> |  | 0.9<br><sub>1,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Koa Peat | 63% | 6.3<br><sub>3,-,-,3,2</sub> | 2.1<br><sub>0,-,-,2,0</sub> |  | 1.5<br><sub>0,-,-,1,1</sub> |  | 0.3<br><sub>0,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.3 | 3.9 |

</details>


### SAS @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Robert Williams III (POR), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 32.7<br><sub>39,34,24,34,26</sub> | 27.2<br><sub>36,43,12,52,30</sub> | 27.5 · –<br><sub>o 47% · u 53%</sub> | 11.1<br><sub>14,7,11,24,14</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>5,4,5,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,3,0,1,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.3 | 3.5 | 2.7 | 41.5 |
| Devin Vassell | 98% | 32.3<br><sub>38,34,25,36,27</sub> | 11.3<br><sub>21,9,11,2,19</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>5,5,2,7,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>2,2,1,4,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>1,0,0,0,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.3 | 0.5 | 1.2 | 18.0 |
| Dylan Harper | 98% | 32.0<br><sub>37,39,27,36,28</sub> | 16.8<br><sub>13,25,17,21,19</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.2<br><sub>5,7,7,5,2</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>8,6,8,0,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>2,2,1,1,1</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.2 | 0.3 | 2.0 | 25.7 |
| De'Aaron Fox | 98% | 31.6<br><sub>39,35,22,33,26</sub> | 14.9<br><sub>14,22,12,10,9</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>3,8,2,3,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>4,7,3,4,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,1,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.4 | 2.3 | 23.8 |
| Stephon Castle | 98% | 31.1<br><sub>38,22,26,35,28</sub> | 16.7<br><sub>14,0,16,17,19</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>6,5,5,10,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>8,4,4,3,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>1,0,2,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 0.3 | 2.9 | 27.2 |
| Julian Champagnie | 98% | 25.0<br><sub>31,27,22,21,22</sub> | 8.2<br><sub>6,12,8,0,8</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>6,3,6,4,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,1,0,3,2</sub> |  | 1.5<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.5 | 0.7 | 13.9 |
| Keldon Johnson | 98% | 22.1<br><sub>23,24,27,19,27</sub> | 9.4<br><sub>9,2,15,4,3</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>6,6,7,5,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,0,1,2,6</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.2 | 0.9 | 15.3 |
| Luke Kornet | 98% | 15.5<br><sub>14,14,17,14,18</sub> | 4.0<br><sub>1,2,8,2,2</sub> |  | 4.4<br><sub>6,8,5,1,6</sub> |  | 1.0<br><sub>1,0,2,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.5 | 9.3 |
| Harrison Barnes | 72% | 14.1<br><sub>-,-,21,13,19</sub> | 4.7<br><sub>-,-,13,4,13</sub> |  | 1.6<br><sub>-,-,0,2,1</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 0.6<br><sub>-,-,3,1,2</sub> |  | 0.3 | 0.1 | 0.5 | 6.9 |
| Carter Bryant | 80% | 8.9<br><sub>5,11,14,-,3</sub> | 2.8<br><sub>3,6,3,-,0</sub> |  | 1.5<br><sub>0,0,0,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.2<br><sub>1,2,1,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.9 |
| Jordan McLaughlin | 52% | 7.7<br><sub>-,-,8,-,8</sub> | 2.5<br><sub>-,-,0,-,2</sub> |  | 1.1<br><sub>-,-,1,-,2</sub> |  | 1.1<br><sub>-,-,3,-,1</sub> |  | 0.1<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Tarris Reed Jr. | 58% | 6.5<br><sub>-,-,7,-,3</sub> | 2.5<br><sub>-,-,4,-,0</sub> |  | 3.3<br><sub>-,-,7,-,1</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.3 | 0.5 | 6.1 |
| David Jones Garcia | 58% | 6.0<br><sub>-,-,-,-,3</sub> | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 35.1<br><sub>32,30,35,35,39</sub> | 23.4<br><sub>24,24,28,21,22</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>9,5,3,7,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>7,2,5,12,11</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.5 | 3.8 | 37.4 |
| Damian Lillard | 98% | 34.4<br><sub>30,27,30,33,37</sub> | 20.1<br><sub>9,22,20,25,22</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>2,5,6,3,0</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>2,4,6,5,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>1,3,1,2,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 2.7 | 30.2 |
| Jrue Holiday | 98% | 31.7<br><sub>24,22,31,28,31</sub> | 13.8<br><sub>6,14,17,15,12</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>6,4,8,4,1</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 5.4<br><sub>4,3,10,0,7</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,2,3,5,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.2 | 2.1 | 23.9 |
| Toumani Camara | 98% | 31.6<br><sub>26,31,31,32,30</sub> | 12.2<br><sub>13,14,9,11,18</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>2,4,5,4,6</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>3,4,3,1,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.4 | 1.2 | 18.4 |
| Donovan Clingan | 98% | 28.8<br><sub>29,15,32,29,28</sub> | 12.2<br><sub>11,4,17,24,17</sub> | 10.5 · –<br><sub>o 53% · u 47%</sub> | 10.9<br><sub>8,9,18,11,11</sub> | 11.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>1,0,3,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>1,0,1,1,3</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 1.9 | 1.4 | 25.2 |
| Scoot Henderson | 98% | 27.0<br><sub>19,31,26,22,23</sub> | 12.2<br><sub>9,14,8,9,2</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>4,3,2,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>0,1,2,1,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,1,2,1,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 2.3 | 18.0 |
| Sidy Cissoko | 98% | 23.7<br><sub>19,19,22,21,22</sub> | 6.4<br><sub>4,1,8,7,7</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>6,3,3,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>2,1,0,4,3</sub> |  | 0.8<br><sub>0,0,2,1,2</sub> |  | 0.8 | 0.4 | 1.0 | 11.7 |
| Chris Youngblood | 88% | 13.6<br><sub>-,7,15,4,11</sub> | 5.0<br><sub>-,3,7,0,7</sub> |  | 1.7<br><sub>-,0,2,0,1</sub> |  | 0.8<br><sub>-,0,1,1,0</sub> |  | 0.8<br><sub>-,1,1,0,2</sub> |  | 0.4 | 0.2 | 0.5 | 7.6 |
| Micah Potter | 52% | 9.4<br><sub>9,4,-,2,-</sub> | 4.0<br><sub>1,2,-,4,-</sub> |  | 2.7<br><sub>2,1,-,1,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,1,-</sub> |  | 0.2 | 0.2 | 0.5 | 7.3 |
| Branden Carlson | 52% | 9.2<br><sub>12,4,-,3,-</sub> | 2.8<br><sub>2,0,-,2,-</sub> |  | 2.0<br><sub>2,2,-,0,-</sub> |  | 0.6<br><sub>1,1,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.5 | 0.6 | 5.3 |
| Yang Hansen | 67% | 9.1<br><sub>5,13,-,2,3</sub> | 3.5<br><sub>3,6,-,0,2</sub> |  | 2.1<br><sub>2,5,-,0,0</sub> |  | 0.5<br><sub>1,1,-,0,0</sub> |  | 0.2<br><sub>1,2,-,0,0</sub> |  | 0.2 | 0.3 | 0.6 | 6.1 |
| Jayson Kent | 52% | 7.8<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-07/`._
