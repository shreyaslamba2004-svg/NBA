# NBA model · Fri 06 Nov 2026 (US date)

Updated **Sat 07 Nov, 11:56 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-06/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

2 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| TOR @ MIL | player minutes | Jamal Shead projected 32 min; most in his last 10 games is 25 | minutes 32 vs 22 this season; teammates out: Barnes, Leonard, Quickley (~91 min a game) |
| UTA @ DAL | team points | DAL projected 126, market implies 116 | 37% of tonight's minutes go to players new to DAL since last season, and the team ratings still lean on last season; DAL out: Larrea, II | 37% of tonight's minutes go to players new to UTA since last season, and the team ratings still lean on last season; UTA out: Jr., Nurkic |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Austin Reaves 3PM over 1.5 (2+) | POR @ LAL | draftkings | 2.47 | 1.97 | 1.64 | 61.0% | 50.0% | 50.8% | +25.6% | +50.7% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | SAS @ SAC | sportsbet | 10.00 | 8.94 | 5.46 | 18.3% | 11.2% | 11.2% | +11.8% | +83.2% | 0.3% |
| Precious Achiuwa PRA over 29.5 (30+) | SAS @ SAC | draftkings | 17.80 | 16.64 | 6.48 | 15.4% | 5.2% | 6.0% | +7.1% | +174.9% | 0.1% |
| Darius Acuff Jr. AST over 11.5 (12+) | SAS @ SAC | draftkings | 17.40 | 16.26 | 6.34 | 15.8% | 5.4% | 6.2% | +7.0% | +174.6% | 0.1% |
| Precious Achiuwa PA over 19.5 (20+) | SAS @ SAC | draftkings | 14.40 | 13.72 | 5.81 | 17.2% | 6.5% | 7.3% | +5.0% | +147.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| UTA @ DAL | Sat 07 Nov 12:00 | 115.1–125.7 | UTA 23% | 4.40 / 1.29 | DAL -10.5 | 240.5 | DAL -6.5 covers 62%; o226.5 78% |
| OKC @ MEM | Sat 07 Nov 12:00 | 116.2–112.3 | OKC 61% | 1.64 / 2.56 | MEM +4.5 | 228.5 | MEM +4.5 covers 51%; o224.5 59% |
| TOR @ MIL | Sat 07 Nov 12:00 | 115.4–112.0 | TOR 60% | 1.68 / 2.47 | MIL +3.5 | 227.5 | MIL +3.5 covers 49%; o228.5 47% |
| MIN @ NOP | Sat 07 Nov 12:00 | 117.9–118.4 | MIN 49% | 2.05 / 1.95 | NOP +0.5 | 236.5 | NOP +3.5 covers 60%; o230.5 62% |
| POR @ LAL | Sat 07 Nov 14:00 | 110.5–116.3 | POR 34% | 2.95 / 1.51 | LAL -6.5 | 226.5 | LAL -3.5 covers 57%; o231.5 39% |
| SAS @ SAC | Sat 07 Nov 14:00 | 120.9–108.1 | SAS 82% | 1.22 / 5.46 | SAC +12.5 | 228.5 | SAC +17.5 covers 63%; o231.5 44% |

### UTA @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Jusuf Nurkic (UTA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brice Sensabaugh PTS over 7.5 (8+) | UTA @ DAL | sportsbet | 2.08 | 2.00 | 1.63 | 61.4% | 49.1% | 50.0% | +4.0% | +27.6% | 0.9% |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 100% | 32.4<br><sub>33,37,29,22,44</sub> | 23.2<br><sub>26,31,8,7,39</sub> | 21.5 · 21.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>3,4,3,7,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>6,3,4,0,9</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>0,5,0,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.1 | 3.2 | 33.1 |
| Lauri Markkanen | 100% | 31.4<br><sub>6,-,29,31,39</sub> | 21.7<br><sub>2,-,13,22,21</sub> | 20.5 · 20.5<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>0,-,6,8,10</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>0,-,1,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.3<br><sub>0,-,2,4,5</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.5 | 1.8 | 30.9 |
| Ace Bailey | 100% | 31.0<br><sub>34,40,37,24,35</sub> | 14.7<br><sub>17,19,9,5,15</sub> | 13.5 · 12.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>10,6,7,6,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>3,0,1,2,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.9<br><sub>3,1,1,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 1.0 | 1.7 | 22.8 |
| Darryn Peterson | 100% | 30.3<br><sub>26,26,36,33,30</sub> | 12.8<br><sub>14,18,16,14,7</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>7,5,4,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.0<br><sub>4,3,4,6,7</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>3,3,3,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.6 | 1.6 | 20.8 |
| Jaxson Hayes | 100% | 24.9<br><sub>-,37,20,22,21</sub> | 8.6<br><sub>-,2,7,9,2</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>-,11,7,5,7</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>-,4,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.2 | 16.4 |
| Josh Okogie | 91% | 18.5<br><sub>21,28,14,19,26</sub> | 3.9<br><sub>0,5,0,9,3</sub> |  | 3.4<br><sub>2,9,1,3,6</sub> |  | 1.1<br><sub>0,3,0,2,1</sub> |  | 0.4<br><sub>0,1,0,1,1</sub> |  | 0.8 | 0.3 | 0.7 | 8.3 |
| Svi Mykhailiuk | 91% | 16.3<br><sub>13,15,18,14,17</sub> | 6.1<br><sub>0,3,6,3,6</sub> | 5.5 · 5.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>1,2,1,2,3</sub> |  | 1.2<br><sub>0,1,3,0,0</sub> |  | 0.9<br><sub>0,1,2,1,0</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.5 | 0.1 | 0.6 | 9.3 |
| Brice Sensabaugh | 98% | 16.2<br><sub>9,18,19,14,12</sub> | 10.0<br><sub>11,16,12,7,6</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>2,3,3,2,2</sub> |  | 1.3<br><sub>0,1,2,1,0</sub> |  | 1.2<br><sub>3,4,2,1,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.5 | 0.1 | 1.4 | 14.0 |
| Josh Green | 88% | 15.9<br><sub>25,24,2,15,23</sub> | 3.2<br><sub>6,2,0,3,7</sub> |  | 1.7<br><sub>4,2,0,1,1</sub> |  | 0.8<br><sub>1,2,0,0,0</sub> |  | 0.3<br><sub>1,0,0,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 5.7 |
| Mo Bamba | 72% | 14.8<br><sub>29,16,11,18,15</sub> | 5.3<br><sub>14,8,6,8,7</sub> | – · 6.5<br><sub>o 50% · u 50%</sub> | 5.8<br><sub>7,4,4,8,10</sub> |  | 0.8<br><sub>1,1,0,0,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.0 | 0.7 | 11.9 |
| Isaiah Collier | 98% | 14.4<br><sub>21,24,20,12,3</sub> | 6.7<br><sub>7,7,8,7,0</sub> |  | 2.1<br><sub>8,7,1,2,1</sub> |  | 4.0<br><sub>8,6,4,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.2 | 1.3 | 12.8 |
| Kyle Filipowski | 58% | 11.1<br><sub>8,-,6,8,-</sub> | 5.2<br><sub>0,-,5,1,-</sub> |  | 3.4<br><sub>1,-,0,2,-</sub> |  | 1.2<br><sub>0,-,2,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.8 |
| Kobe Bufkin | 38% | 8.2<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |
| Tony Bradley | 48% | 7.9<br><sub>6,-,-,7,-</sub> | 2.7<br><sub>2,-,-,2,-</sub> |  | 2.3<br><sub>1,-,-,3,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.5 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving | 100% | 32.2<br><sub>33,27,35,-,36</sub> | 24.0<br><sub>18,15,35,-,29</sub> | 22.5 · 22.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>6,2,4,-,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.2<br><sub>6,4,9,-,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>2,3,5,-,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.6 | 2.4 | 33.8 |
| Cooper Flagg | 100% | 31.1<br><sub>40,33,39,40,40</sub> | 23.2<br><sub>29,26,33,17,19</sub> | 25.5 · 25.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>6,5,9,4,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 6.0<br><sub>11,8,6,6,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 1.0 | 2.7 | 35.7 |
| P.J. Washington | 100% | 30.7<br><sub>41,27,34,38,39</sub> | 15.1<br><sub>20,18,3,12,21</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>9,9,10,5,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>2,0,1,1,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>4,2,1,2,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 1.0 | 1.7 | 24.2 |
| Naji Marshall | 84% | 24.0<br><sub>-,-,-,24,26</sub> | 13.0<br><sub>-,-,-,5,22</sub> | 12.5 · 11.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>-,-,-,2,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>-,-,-,7,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>-,-,-,0,3</sub> |  | 1.1 | 0.2 | 1.8 | 20.6 |
| Daniel Gafford | 100% | 21.6<br><sub>26,27,29,26,18</sub> | 11.1<br><sub>8,7,18,20,2</sub> | 8.5 · 8.5<br><sub>o 53% · u 47%</sub> | 7.1<br><sub>9,11,7,7,4</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>3,2,2,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.8 | 1.7 | 1.2 | 19.7 |
| Zaccharie Risacher | 93% | 20.0<br><sub>30,29,28,19,18</sub> | 6.8<br><sub>6,13,12,0,2</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>8,6,6,5,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,1,3,1,2</sub> |  | 0.9<br><sub>1,2,3,0,0</sub> |  | 1.1 | 0.8 | 0.9 | 12.1 |
| Caleb Martin | 100% | 19.3<br><sub>-,14,25,21,20</sub> | 6.1<br><sub>-,10,8,5,0</sub> |  | 3.2<br><sub>-,2,0,6,3</sub> |  | 1.4<br><sub>-,0,0,0,2</sub> |  | 0.6<br><sub>-,2,2,1,0</sub> |  | 0.9 | 0.4 | 0.9 | 10.7 |
| Max Christie | 98% | 18.1<br><sub>26,22,18,8,-</sub> | 7.5<br><sub>11,11,2,0,-</sub> | – · 7.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>5,5,1,2,-</sub> |  | 1.4<br><sub>3,2,0,0,-</sub> |  | 1.2<br><sub>3,3,0,0,-</sub> |  | 0.6 | 0.3 | 0.9 | 11.1 |
| Santi Aldama | 96% | 14.7 | 7.1 | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.5 |  | 1.4 |  | 0.8 |  | 0.6 | 0.4 | 0.7 | 12.1 |
| Walter Clayton Jr. | 88% | 13.6<br><sub>17,15,9,24,21</sub> | 6.3<br><sub>15,0,3,20,8</sub> |  | 2.1<br><sub>4,2,2,1,6</sub> |  | 3.1<br><sub>4,5,1,2,5</sub> |  | 0.9<br><sub>2,0,1,4,2</sub> |  | 0.4 | 0.2 | 0.7 | 11.5 |
| Morez Johnson Jr. | 98% | 11.8<br><sub>15,18,17,17,18</sub> | 5.2<br><sub>6,10,2,13,8</sub> |  | 1.9<br><sub>2,6,2,2,3</sub> |  | 1.2<br><sub>1,3,1,1,1</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.4 | 0.1 | 0.7 | 8.3 |
| Marcus Sasser | 96% | 9.5<br><sub>8,22,7,19,5</sub> | 3.6<br><sub>0,10,0,4,0</sub> |  | 0.9<br><sub>1,1,0,1,1</sub> |  | 1.5<br><sub>0,4,1,1,2</sub> |  | 0.5<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.0 |
| Moussa Cisse | 58% | 6.7<br><sub>-,3,-,2,-</sub> | 2.7<br><sub>-,0,-,0,-</sub> |  | 2.7<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.6 | 0.4 | 5.5 |
| Jett Howard | 52% | 5.4<br><sub>-,3,-,2,-</sub> | 2.3<br><sub>-,0,-,2,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.4 |
| Tobi Lawal | 52% | 5.4<br><sub>-,3,-,2,-</sub> | 2.2<br><sub>-,0,-,2,-</sub> |  | 1.1<br><sub>-,0,-,0,-</sub> |  | 0.7<br><sub>-,1,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>


### OKC @ MEM
Out: Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 33.6<br><sub>30,28,31,39,35</sub> | 30.4<br><sub>26,21,26,43,42</sub> | 33.5 · 32.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>3,6,4,3,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>3,2,3,8,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,1,3,4,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6 | 0.9 | 2.8 | 41.4 |
| Ajay Mitchell | 100% | 30.2<br><sub>25,28,26,35,32</sub> | 18.2<br><sub>30,29,6,20,23</sub> | 19.5 · 20.5<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>2,4,3,5,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.4<br><sub>5,3,5,1,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>1,2,0,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 2.0 | 26.8 |
| Jared McCain | 100% | 28.7<br><sub>30,29,28,27,25</sub> | 15.1<br><sub>18,10,10,7,9</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,4,4,9,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>4,4,2,2,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.2<br><sub>4,0,0,0,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.1 | 1.8 | 20.6 |
| Kenrich Williams | 100% | 27.2<br><sub>24,17,21,31,29</sub> | 10.8<br><sub>3,7,11,12,13</sub> | 8.5 · 8.5<br><sub>o 53% · u 47%</sub> | 6.1<br><sub>7,3,7,3,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>0,0,3,1,2</sub> |  | 1.5<br><sub>0,1,3,2,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.2 | 19.0 |
| Isaiah Hartenstein | 100% | 26.6<br><sub>26,26,25,28,26</sub> | 10.1<br><sub>15,10,10,5,3</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 10.6<br><sub>13,14,7,14,12</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,3,0,4,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.8 | 23.9 |
| Aday Mara | 97% | 23.7<br><sub>20,21,28,20,25</sub> | 8.1<br><sub>11,6,7,10,9</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>10,3,9,9,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>2,1,3,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 2.4 | 1.7 | 16.5 |
| Alex Caruso | 98% | 21.7<br><sub>9,-,-,-,20</sub> | 9.0<br><sub>9,-,-,-,7</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>2,-,-,-,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>3,-,-,-,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>3,-,-,-,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.4 | 1.0 | 15.2 |
| Bennett Stirtz | 97% | 21.7<br><sub>25,28,26,12,22</sub> | 7.0<br><sub>7,8,11,9,16</sub> | 6.5 · –<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,0,1,2,1</sub> |  | 1.4<br><sub>1,3,3,0,1</sub> |  | 1.1<br><sub>1,1,3,3,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.1 | 0.8 | 10.5 |
| Micah Peavy | 72% | 20.6<br><sub>-,5,14,16,26</sub> | 5.5<br><sub>-,0,2,8,2</sub> |  | 4.0<br><sub>-,0,1,5,9</sub> |  | 1.1<br><sub>-,0,0,0,1</sub> |  | 0.5<br><sub>-,0,0,2,0</sub> |  | 0.7 | 0.2 | 0.9 | 10.6 |
| Josh Dix | 64% | 14.9<br><sub>22,24,9,12,-</sub> | 5.0<br><sub>0,2,7,0,-</sub> |  | 1.3<br><sub>1,2,0,1,-</sub> |  | 0.8<br><sub>0,0,0,0,-</sub> |  | 0.6<br><sub>0,0,1,0,-</sub> |  | 0.5 | 0.2 | 0.5 | 7.1 |
| Brooks Barnhizer | 52% | 9.4<br><sub>3,14,6,-,-</sub> | 2.4<br><sub>0,3,5,-,-</sub> |  | 2.1<br><sub>0,2,2,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.0 |
| Dalen Terry | 52% | 9.4<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 5.6 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 100% | 32.6<br><sub>31,28,26,38,33</sub> | 15.3<br><sub>13,18,27,18,10</sub> | 16.5 · 16.5<br><sub>o 49% · u 51%</sub> | 9.3<br><sub>7,12,9,9,6</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 5.2<br><sub>4,12,3,5,4</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,4,3,2,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.7 | 2.7 | 29.9 |
| Ty Jerome | 100% | 29.4<br><sub>30,24,-,37,29</sub> | 19.9<br><sub>15,10,-,40,23</sub> | 20.5 · 20.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>1,2,-,5,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>8,3,-,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>1,1,-,5,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.2 | 2.5 | 29.0 |
| Cedric Coward | 100% | 28.3<br><sub>31,27,23,31,33</sub> | 13.7<br><sub>16,17,10,10,23</sub> | 14.5 · 13.5<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>11,7,7,9,9</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>3,4,2,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>4,3,2,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.4 | 1.8 | 23.1 |
| Jaylen Wells | 100% | 25.5<br><sub>30,25,22,34,21</sub> | 9.9<br><sub>14,10,4,16,0</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,1,2,3,1</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,0,0,3,3</sub> |  | 1.6<br><sub>2,2,0,3,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.2 | 0.9 | 14.3 |
| Jerami Grant | 98% | 23.1<br><sub>24,27,23,24,24</sub> | 10.1<br><sub>13,2,14,11,11</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,1,2,4,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,3,1,2,2</sub> |  | 1.4<br><sub>3,0,1,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.6 | 0.6 | 1.3 | 14.3 |
| Zach Edey | 100% | 22.9<br><sub>21,19,18,19,25</sub> | 8.8<br><sub>4,13,4,6,11</sub> | 7.5 · 7.5<br><sub>o 52% · u 48%</sub> | 8.4<br><sub>3,7,6,9,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>2,0,0,1,1</sub> |  | 0.1<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.4 | 1.4 | 18.3 |
| Cam Spencer | 98% | 19.5<br><sub>18,23,25,19,24</sub> | 7.6<br><sub>8,8,10,13,7</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>5,6,5,1,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>5,8,13,7,9</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>2,1,2,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.1 | 1.1 | 14.9 |
| Javon Small | 88% | 16.5<br><sub>-,-,20,-,-</sub> | 6.8<br><sub>-,-,7,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 2.4<br><sub>-,-,5,-,-</sub> |  | 0.8<br><sub>-,-,2,-,-</sub> |  | 0.6 | 0.2 | 1.3 | 11.6 |
| GG Jackson | 97% | 13.1<br><sub>16,21,21,16,7</sub> | 7.0<br><sub>4,12,21,6,1</sub> |  | 2.6<br><sub>1,7,3,0,2</sub> |  | 0.8<br><sub>2,2,2,1,0</sub> |  | 0.7<br><sub>0,2,5,0,0</sub> |  | 0.3 | 0.3 | 1.0 | 10.4 |
| Kris Murray | 76% | 12.0<br><sub>-,3,21,19,15</sub> | 3.0<br><sub>-,0,2,0,5</sub> |  | 1.9<br><sub>-,1,1,4,1</sub> |  | 0.8<br><sub>-,0,1,1,1</sub> |  | 0.2<br><sub>-,0,0,0,1</sub> |  | 0.4 | 0.2 | 0.5 | 5.7 |
| Quinten Post | 91% | 10.9<br><sub>12,7,-,-,11</sub> | 4.4<br><sub>12,10,-,-,2</sub> |  | 1.9<br><sub>2,4,-,-,1</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.4<br><sub>2,2,-,-,0</sub> |  | 0.2 | 0.3 | 0.6 | 6.8 |
| Olivier-Maxence Prosper | 58% | 8.7<br><sub>-,3,4,-,7</sub> | 4.9<br><sub>-,4,2,-,4</sub> |  | 1.8<br><sub>-,1,1,-,3</sub> |  | 0.4<br><sub>-,0,1,-,1</sub> |  | 0.4<br><sub>-,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 7.1 |
| Jahmai Mashack | 38% | 8.2<br><sub>-,-,4,-,-</sub> | 2.8<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.7 | 4.8 |
| Taylor Hendricks | 52% | 6.8<br><sub>-,3,4,-,-</sub> | 2.8<br><sub>-,0,6,-,-</sub> |  | 1.3<br><sub>-,1,1,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,2,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.4 |
| Karim Lopez | 47% | 5.9<br><sub>-,3,4,-,-</sub> | 2.7<br><sub>-,0,2,-,-</sub> |  | 1.1<br><sub>-,1,1,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |

</details>


### TOR @ MIL
Out: Kam Jones (MIL), Pete Nance (MIL), Cormac Ryan (MIL), Scottie Barnes (TOR), Kawhi Leonard (TOR), Immanuel Quickley (TOR), Malachi Smith (TOR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyle Kuzma PTS over 9.5 (10+) | TOR @ MIL | tab | 1.90 | 1.89 | 1.65 | 60.7% | 52.1% | 52.8% | +0.4% | +15.4% | 0.1% |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett | 100% | 36.2<br><sub>32,34,32,37,33</sub> | 27.1<br><sub>25,9,22,26,22</sub> | 27.5 · 26.5<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>9,3,10,6,5</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>6,5,5,3,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,1,4,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.5 | 2.8 | 39.5 |
| Ja'Kobe Walter | 100% | 33.6<br><sub>28,32,33,35,27</sub> | 16.2<br><sub>14,9,11,10,8</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,3,4,6,1</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>2,1,2,5,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>3,3,3,0,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6 | 0.3 | 1.3 | 23.4 |
| Jamal Shead | 100% | 32.0<br><sub>23,23,25,20,20</sub> | 11.4<br><sub>13,2,9,6,3</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>4,1,2,1,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 8.3<br><sub>7,8,6,6,6</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,0,2,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.2 | 2.4 | 22.6 |
| Collin Murray-Boyles | 100% | 31.1<br><sub>15,23,20,28,23</sub> | 16.7<br><sub>10,15,4,18,13</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>2,5,3,7,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>1,1,1,0,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.5<br><sub>2,1,0,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.4 | 1.1 | 2.0 | 27.4 |
| Jamison Battle | 98% | 26.2<br><sub>20,19,17,21,19</sub> | 11.8<br><sub>7,2,20,12,9</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>0,0,5,0,1</sub> |  | 1.6<br><sub>1,0,0,0,0</sub> |  | 2.3<br><sub>1,0,4,4,2</sub> |  | 0.6 | 0.2 | 1.0 | 17.0 |
| Jakob Poeltl | 100% | 23.4<br><sub>10,23,-,-,19</sub> | 10.2<br><sub>2,12,-,-,8</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>2,11,-,-,5</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>0,3,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 1.0 | 0.7 | 1.4 | 19.2 |
| Allen Graves | 97% | 21.7<br><sub>18,9,10,7,14</sub> | 7.6<br><sub>3,7,3,0,5</sub> |  | 3.7<br><sub>1,4,0,0,1</sub> |  | 1.5<br><sub>0,0,0,2,1</sub> |  | 0.9<br><sub>0,1,0,0,1</sub> |  | 0.9 | 0.6 | 0.8 | 12.8 |
| Alijah Martin | 88% | 16.7<br><sub>5,-,16,6,9</sub> | 7.1<br><sub>5,-,5,2,6</sub> |  | 2.5<br><sub>1,-,2,2,1</sub> |  | 1.8<br><sub>1,-,4,0,0</sub> |  | 0.6<br><sub>1,-,1,0,0</sub> |  | 0.8 | 0.3 | 0.9 | 11.4 |
| Kyle Anderson | 80% | 16.5<br><sub>5,-,4,8,4</sub> | 4.9<br><sub>0,-,2,2,2</sub> |  | 3.1<br><sub>0,-,3,0,0</sub> |  | 3.1<br><sub>1,-,3,0,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.9 | 0.5 | 0.9 | 11.1 |
| Trayce Jackson-Davis | 96% | 16.0<br><sub>20,1,9,2,4</sub> | 6.0<br><sub>6,0,5,0,1</sub> |  | 5.2<br><sub>11,0,5,0,0</sub> |  | 1.3<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 0.8 | 12.6 |
| Jaden Bradley | 67% | 12.6<br><sub>5,-,4,-,4</sub> | 4.0<br><sub>0,-,3,-,2</sub> |  | 2.2<br><sub>1,-,1,-,1</sub> |  | 1.1<br><sub>1,-,2,-,0</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 1.1 | 0.3 | 0.8 | 7.3 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 100% | 31.7<br><sub>32,27,27,31,33</sub> | 19.6<br><sub>23,23,15,21,25</sub> | 21.5 · 20.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>10,3,3,6,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>7,0,2,3,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.5<br><sub>3,4,4,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.2 | 2.6 | 28.4 |
| Jaime Jaquez Jr. | 100% | 29.6<br><sub>25,27,23,28,31</sub> | 15.3<br><sub>8,19,8,19,18</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>6,4,7,8,2</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>0,2,5,2,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>0,3,1,2,4</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 0.2 | 2.5 | 24.8 |
| Myles Turner | 100% | 28.4<br><sub>28,22,24,31,36</sub> | 10.6<br><sub>6,4,10,13,12</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>9,2,7,5,9</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,2,2,2,6</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>0,0,1,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.7 | 2.1 | 1.4 | 18.0 |
| Kyle Kuzma | 100% | 26.5<br><sub>29,18,23,22,27</sub> | 11.7<br><sub>17,4,14,2,6</sub> | 10.5 · 9.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>7,6,3,2,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>3,1,3,3,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>4,0,2,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.3 | 1.9 | 19.4 |
| Ryan Rollins | 98% | 25.8<br><sub>32,17,26,17,24</sub> | 13.4<br><sub>19,4,9,10,13</sub> | 12.5 · 11.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,4,3,3,9</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>4,5,7,2,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.7<br><sub>3,0,1,1,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.4 | 2.5 | 21.8 |
| Brayden Burries | 100% | 23.1<br><sub>16,17,21,26,22</sub> | 10.1<br><sub>4,10,14,9,9</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>2,5,3,9,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,1,1,1,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.6 | 16.9 |
| AJ Green | 98% | 20.4<br><sub>20,24,20,24,20</sub> | 6.9<br><sub>3,9,0,13,5</sub> | 5.5 · 6.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>4,1,3,3,2</sub> |  | 1.4<br><sub>3,2,2,3,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>1,3,0,4,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.4 | 0.1 | 0.8 | 10.3 |
| Kel'el Ware | 91% | 17.3<br><sub>19,17,24,17,16</sub> | 8.4<br><sub>16,6,19,2,2</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>14,8,10,9,5</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 0.9<br><sub>0,0,3,0,1</sub> |  | 0.7<br><sub>0,0,3,0,0</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 0.5 | 0.7 | 1.3 | 15.5 |
| Kasparas Jakucionis | 91% | 17.0<br><sub>21,19,21,22,12</sub> | 6.0<br><sub>7,4,5,7,3</sub> | 5.5 · 5.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>4,2,3,5,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.0<br><sub>5,6,3,7,1</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.6<br><sub>1,0,1,0,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 0.5 | 0.2 | 1.2 | 11.2 |
| Nate Ament | 88% | 13.7<br><sub>14,20,19,8,18</sub> | 5.8<br><sub>7,8,14,4,9</sub> |  | 2.1<br><sub>3,4,1,1,2</sub> |  | 0.5<br><sub>0,0,2,0,0</sub> |  | 0.5<br><sub>1,1,2,0,2</sub> |  | 0.4 | 0.2 | 0.8 | 8.4 |
| Caris LeVert | 23% | 13.1<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 8.1 |
| Gary Trent Jr. | 48% | 8.6<br><sub>-,7,6,-,-</sub> | 3.4<br><sub>-,3,3,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,1,1,-,-</sub> |  | 0.3 | 0.0 | 0.4 | 4.5 |
| Jericho Sims | 63% | 7.9<br><sub>-,7,-,15,1</sub> | 1.9<br><sub>-,0,-,0,0</sub> |  | 2.2<br><sub>-,0,-,2,0</sub> |  | 0.7<br><sub>-,0,-,1,0</sub> |  | 0.0<br><sub>-,0,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.8 |
| Ousmane Dieng | 71% | 7.8<br><sub>3,13,6,-,2</sub> | 2.7<br><sub>0,4,0,-,0</sub> |  | 1.2<br><sub>0,0,1,-,0</sub> |  | 1.0<br><sub>0,0,2,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 4.9 |

</details>


### MIN @ NOP
Out: Yves Missi (NOP), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Terrence Shannon Jr. (MIN)

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 34.5<br><sub>35,33,39,29,37</sub> | 18.6<br><sub>19,23,19,13,14</sub> | 16.5 · 17.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>7,6,3,6,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>4,7,3,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>1,1,2,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.9 | 1.9 | 27.4 |
| Ayo Dosunmu | 100% | 33.8<br><sub>32,30,38,37,34</sub> | 18.9<br><sub>17,15,27,19,21</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>3,7,9,12,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>4,2,3,8,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>3,3,2,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.4 | 2.1 | 28.7 |
| Jonathan Kuminga | 100% | 32.2<br><sub>32,22,40,33,32</sub> | 15.5<br><sub>20,5,19,8,16</sub> | 14.5 · 14.5<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>3,1,6,10,8</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>5,0,3,3,5</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>3,1,2,2,4</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.8 | 1.6 | 24.2 |
| Rudy Gobert | 100% | 30.6<br><sub>20,30,-,31,33</sub> | 10.2<br><sub>1,9,-,10,8</sub> | 9.5 · 10.5<br><sub>o 48% · u 52%</sub> | 11.8<br><sub>4,13,-,10,11</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>1,4,-,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.9 | 1.7 | 1.5 | 23.8 |
| LaMelo Ball | 100% | 29.1<br><sub>28,29,20,33,31</sub> | 21.6<br><sub>8,24,10,34,20</sub> | 21.5 · 21.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>4,4,8,6,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>8,7,4,3,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>2,6,0,6,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.3 | 3.5 | 32.7 |
| Jaylen Clark | 88% | 20.1<br><sub>7,17,20,21,25</sub> | 7.4<br><sub>3,5,10,4,10</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>2,0,2,2,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>1,2,1,0,1</sub> |  | 0.9<br><sub>1,1,2,1,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.1 | 0.2 | 0.7 | 11.0 |
| Trey Lyles | 98% | 19.5<br><sub>22,17,17,21,20</sub> | 6.9<br><sub>7,10,6,12,5</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>3,5,0,4,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>1,0,0,0,0</sub> |  | 1.0<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.5 | 0.3 | 0.7 | 11.8 |
| Joan Beringer | 96% | 17.1<br><sub>20,18,34,14,13</sub> | 7.4<br><sub>7,4,12,2,4</sub> |  | 6.0<br><sub>9,4,6,7,7</sub> |  | 0.7<br><sub>2,0,2,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.3 | 0.8 | 14.1 |
| Bones Hyland | 97% | 16.8<br><sub>16,20,14,14,16</sub> | 9.5<br><sub>13,19,6,10,19</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,0,1,1,2</sub> |  | 3.0<br><sub>3,8,3,3,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>3,3,0,2,4</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.3 | 1.2 | 14.3 |
| Zyon Pullin | 38% | 7.6<br><sub>-,2,-,-,-</sub> | 3.4<br><sub>-,2,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.2 |
| Rocco Zikarsky | 36% | 7.2<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.7 | 0.4 | 5.2 |
| Cody Williams | 52% | 6.4<br><sub>-,2,-,7,-</sub> | 0.2<br><sub>-,0,-,0,-</sub> |  | 1.2<br><sub>-,0,-,1,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 1.7 |
| Isaiah Evans | 38% | 5.6<br><sub>-,2,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 100% | 32.2<br><sub>30,32,29,40,-</sub> | 14.4<br><sub>6,19,15,18,-</sub> | 15.5 · 15.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>1,5,5,5,-</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,3,5,5,-</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>2,2,1,3,-</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.5 | 1.4 | 22.2 |
| Dejounte Murray | 100% | 32.2<br><sub>30,-,-,-,45</sub> | 16.6<br><sub>10,-,-,-,20</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>8,-,-,-,8</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>5,-,-,-,4</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>0,-,-,-,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.8 | 0.4 | 3.0 | 29.0 |
| Zion Williamson | 100% | 30.8<br><sub>32,31,30,35,38</sub> | 18.9<br><sub>25,22,15,25,23</sub> | 19.5 · 19.5<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>5,6,6,11,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>2,2,4,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.1<br><sub>1,0,0,0,0</sub> |  | 1.3 | 0.8 | 2.2 | 27.2 |
| Jeremiah Fears | 100% | 27.8<br><sub>24,29,31,38,34</sub> | 14.6<br><sub>11,22,20,12,19</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>4,8,5,4,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.0<br><sub>3,13,7,7,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>1,3,1,0,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.5 | 2.4 | 22.8 |
| Saddiq Bey | 98% | 25.6<br><sub>26,24,26,36,29</sub> | 12.9<br><sub>9,10,25,18,22</sub> | 12.5 · 12.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>0,4,6,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>3,3,1,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,1,1,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.1 | 1.0 | 18.6 |
| Herbert Jones | 98% | 23.6<br><sub>19,32,25,28,37</sub> | 7.1<br><sub>4,16,11,9,2</sub> |  | 2.7<br><sub>2,4,3,4,5</sub> |  | 1.7<br><sub>0,1,2,3,1</sub> |  | 0.8<br><sub>0,0,1,3,0</sub> |  | 1.2 | 0.4 | 1.0 | 11.6 |
| Derik Queen | 98% | 22.4<br><sub>25,22,23,24,27</sub> | 11.0<br><sub>11,9,8,20,20</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>12,2,8,7,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>1,3,4,5,6</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.3<br><sub>0,1,0,1,0</sub> |  | 1.0 | 0.9 | 2.1 | 20.4 |
| Karlo Matkovic | 100% | 20.5<br><sub>18,28,18,29,21</sub> | 8.0<br><sub>5,12,8,25,5</sub> | 6.5 · 6.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>3,4,10,6,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.1<br><sub>1,1,1,1,2</sub> |  | 0.8<br><sub>1,1,2,5,1</sub> |  | 0.7 | 1.2 | 0.9 | 13.9 |
| Bennedict Mathurin | 98% | 15.5<br><sub>14,19,19,13,15</sub> | 7.3<br><sub>5,10,7,4,2</sub> | 6.5 · 6.5<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>1,3,1,0,5</sub> |  | 1.3<br><sub>2,2,2,0,1</sub> |  | 0.5<br><sub>1,2,1,0,0</sub> |  | 0.5 | 0.2 | 1.1 | 11.3 |
| Trendon Watford | 67% | 13.3<br><sub>-,17,18,16,20</sub> | 5.4<br><sub>-,8,7,4,7</sub> |  | 2.4<br><sub>-,1,4,4,3</sub> |  | 1.4<br><sub>-,2,0,1,2</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.4 | 1.0 | 9.2 |
| Jordan Poole | 64% | 12.3<br><sub>7,-,-,-,-</sub> | 6.2<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-,-</sub> |  | 1.6<br><sub>0,-,-,-,-</sub> |  | 0.9<br><sub>0,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 9.1 |
| DeAndre Jordan | 35% | 8.1<br><sub>13,-,-,-,-</sub> | 2.3<br><sub>3,-,-,-,-</sub> |  | 3.1<br><sub>4,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.4 | 5.8 |
| Bryce McGowens | 58% | 7.3<br><sub>3,6,15,6,-</sub> | 2.6<br><sub>0,4,3,0,-</sub> |  | 0.8<br><sub>0,1,0,1,-</sub> |  | 0.5<br><sub>0,2,1,0,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| AJ Johnson | 30% | 5.4<br><sub>-,-,3,-,-</sub> | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.6 | 0.8 | 0.9 |
| Julian Reese | 36% | 5.4<br><sub>-,-,3,-,-</sub> | 2.2<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.8 | 3.8 |

</details>


### POR @ LAL
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Austin Reaves 3PM over 1.5 (2+) | POR @ LAL | draftkings | 2.47 | 1.97 | 1.64 | 61.0% | 50.0% | 50.8% | +25.6% | +50.7% | 2.0% |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.4<br><sub>33,32,30,35,35</sub> | 23.3<br><sub>23,24,24,28,21</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>4,9,5,3,7</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>9,7,2,5,12</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>4,0,2,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.4 | 3.9 | 36.5 |
| Damian Lillard | 98% | 32.9<br><sub>31,30,27,30,33</sub> | 19.2<br><sub>21,9,22,20,25</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.6<br><sub>4,2,4,6,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>4,1,3,1,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 2.7 | 29.0 |
| Toumani Camara | 98% | 31.4<br><sub>24,26,31,31,32</sub> | 12.2<br><sub>12,13,14,9,11</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>1,2,4,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,1,0,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>4,3,4,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.3 | 1.5 | 18.2 |
| Jrue Holiday | 98% | 30.2<br><sub>30,24,22,31,28</sub> | 14.2<br><sub>22,6,14,17,15</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>4,6,4,8,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.4<br><sub>3,4,3,10,0</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,2,2,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 2.5 | 24.1 |
| Donovan Clingan | 98% | 26.7<br><sub>26,29,15,32,29</sub> | 11.4<br><sub>9,11,4,17,24</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 10.3<br><sub>10,8,9,18,11</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>2,1,0,1,1</sub> |  | 0.7 | 1.4 | 1.4 | 23.6 |
| Scoot Henderson | 98% | 25.8<br><sub>17,19,31,26,22</sub> | 11.9<br><sub>2,9,14,8,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,4,3,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,0,1,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,1,1,2,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.2 | 2.4 | 17.3 |
| Sidy Cissoko | 97% | 21.6<br><sub>20,19,19,22,21</sub> | 5.7<br><sub>6,4,1,8,7</sub> | 5.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>2,6,3,3,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>4,2,1,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>0,0,0,2,1</sub> |  | 0.9 | 0.3 | 1.0 | 10.5 |
| Robert Williams III | 98% | 17.7<br><sub>21,-,14,15,16</sub> | 6.7<br><sub>14,-,3,2,9</sub> | 6.5 · –<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>10,-,3,6,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>1,-,1,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.8 | 1.0 | 0.9 | 14.5 |
| Chris Youngblood | 86% | 10.2<br><sub>-,-,7,15,4</sub> | 3.8<br><sub>-,-,3,7,0</sub> |  | 1.3<br><sub>-,-,0,2,0</sub> |  | 0.7<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,1,1,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.8 |
| Micah Potter | 64% | 7.9<br><sub>-,9,4,-,2</sub> | 3.3<br><sub>-,1,2,-,4</sub> |  | 2.1<br><sub>-,2,1,-,1</sub> |  | 0.5<br><sub>-,0,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.8 |
| Branden Carlson | 58% | 7.7<br><sub>-,12,4,-,3</sub> | 2.1<br><sub>-,2,0,-,2</sub> |  | 1.7<br><sub>-,2,2,-,0</sub> |  | 0.5<br><sub>-,1,1,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.3 |
| Yang Hansen | 63% | 7.4<br><sub>-,5,13,-,2</sub> | 2.8<br><sub>-,3,6,-,0</sub> |  | 1.7<br><sub>-,2,5,-,0</sub> |  | 0.4<br><sub>-,1,1,-,0</sub> |  | 0.2<br><sub>-,1,2,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 4.9 |
| Jayson Kent | 71% | 6.6<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 35.5<br><sub>-,37,35,36,35</sub> | 33.6<br><sub>-,37,45,42,40</sub> | 35.5 · –<br><sub>o 47% · u 53%</sub> | 7.1<br><sub>-,7,15,7,9</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>-,5,6,13,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>-,6,8,6,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.8 | 0.6 | 4.2 | 48.6 |
| Austin Reaves | 98% | 34.8<br><sub>31,37,39,34,37</sub> | 20.7<br><sub>16,21,19,27,21</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,4,3,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>1,5,4,5,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>1,1,2,4,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.5 | 3.2 | 29.7 |
| Walker Kessler | 98% | 28.7<br><sub>26,31,31,32,29</sub> | 11.8<br><sub>11,10,16,15,15</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 10.5<br><sub>9,13,15,15,8</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>1,2,1,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.0 | 2.1 | 1.5 | 23.7 |
| Quentin Grimes | 98% | 23.3<br><sub>38,26,26,23,25</sub> | 7.6<br><sub>23,3,7,7,6</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>3,3,1,4,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>5,2,3,4,1</sub> |  | 0.8<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.3 | 1.2 | 12.3 |
| Ziaire Williams | 96% | 21.5<br><sub>-,-,-,15,23</sub> | 7.7<br><sub>-,-,-,9,10</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>-,-,-,2,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>-,-,-,2,1</sub> |  | 0.9<br><sub>-,-,-,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.3 | 0.9 | 11.5 |
| Sandro Mamukelashvili | 98% | 20.4<br><sub>30,20,24,28,19</sub> | 8.4<br><sub>13,4,11,13,2</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>8,7,1,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>3,0,1,4,1</sub> |  | 0.9<br><sub>0,0,2,2,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 0.5 | 0.8 | 14.3 |
| Matisse Thybulle | 98% | 20.1<br><sub>28,28,25,19,23</sub> | 5.7<br><sub>15,10,6,6,3</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,3,2,1,1</sub> |  | 1.1<br><sub>0,0,3,2,2</sub> |  | 0.8<br><sub>4,1,2,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.7 | 0.7 | 0.8 | 8.7 |
| Jake LaRavia | 96% | 20.0<br><sub>35,28,25,26,21</sub> | 5.5<br><sub>2,10,8,7,9</sub> | 4.5 · –<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>10,2,2,4,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.3<br><sub>0,0,4,2,2</sub> |  | 0.5<br><sub>0,2,2,1,2</sub> |  | 1.1 | 0.6 | 1.1 | 9.9 |
| Collin Sexton | 98% | 16.6<br><sub>21,16,19,16,16</sub> | 9.9<br><sub>21,0,14,6,10</sub> |  | 1.8<br><sub>4,2,3,1,3</sub> |  | 1.8<br><sub>2,1,3,5,1</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 0.8 | 0.2 | 1.4 | 13.6 |
| Jarred Vanderbilt | 72% | 9.3<br><sub>21,13,12,6,7</sub> | 2.7<br><sub>0,0,4,2,0</sub> |  | 2.4<br><sub>7,3,3,1,1</sub> |  | 0.7<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 5.8 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Lawson Lovering | 91% | 6.7<br><sub>-,-,-,1,1</sub> | 2.0<br><sub>-,-,-,0,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.3 |
| Jaden Hardy | 80% | 6.4<br><sub>9,1,1,1,1</sub> | 3.4<br><sub>2,0,1,2,0</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.6<br><sub>2,0,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.0 | 0.4 | 4.5 |
| Kevon Looney | 38% | 6.1<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.3 |
| Adou Thiero | 16% | 5.6 | 2.0 |  | 1.4 |  | 0.4 |  | 0.0 |  | 0.2 | 0.1 | 0.5 | 3.8 |
| Chris Manon | 58% | 5.3<br><sub>-,1,-,-,-</sub> | 1.8<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.1 |

</details>


### SAS @ SAC
Out: De'Andre Hunter (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Tobias Harris (SAS)

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 32.8<br><sub>27,39,34,24,34</sub> | 28.2<br><sub>29,36,43,12,52</sub> | 28.5 · –<br><sub>o 48% · u 52%</sub> | 11.3<br><sub>10,14,7,11,24</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,5,4,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>0,4,3,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 3.9 | 2.5 | 43.0 |
| Dylan Harper | 98% | 32.5<br><sub>30,37,39,27,36</sub> | 17.1<br><sub>13,13,25,17,21</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>6,5,7,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>6,8,6,8,0</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.4 | 1.9 | 27.5 |
| Devin Vassell | 98% | 32.4<br><sub>24,38,34,25,36</sub> | 13.5<br><sub>14,21,9,11,2</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>4,5,5,2,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.0<br><sub>8,2,2,1,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>4,1,0,0,0</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.3 | 0.5 | 1.1 | 20.9 |
| De'Aaron Fox | 98% | 31.5<br><sub>26,39,35,22,33</sub> | 15.9<br><sub>11,14,22,12,10</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,3,8,2,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>6,4,7,3,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,1,0,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.4 | 2.1 | 26.0 |
| Stephon Castle | 98% | 30.9<br><sub>27,38,22,26,35</sub> | 17.1<br><sub>15,14,0,16,17</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.3<br><sub>5,6,5,5,10</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 6.4<br><sub>5,8,4,4,3</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.9 | 28.8 |
| Julian Champagnie | 98% | 25.6<br><sub>25,31,27,22,21</sub> | 9.4<br><sub>26,6,12,8,0</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>3,6,3,6,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>3,0,1,0,3</sub> |  | 1.8<br><sub>8,2,3,2,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.5 | 0.8 | 15.3 |
| Keldon Johnson | 98% | 21.2<br><sub>22,23,24,27,19</sub> | 9.3<br><sub>14,9,2,15,4</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>4,6,6,7,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>0,2,0,1,2</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 15.1 |
| Luke Kornet | 98% | 14.7<br><sub>17,14,14,17,14</sub> | 3.9<br><sub>0,1,2,8,2</sub> |  | 4.4<br><sub>4,6,8,5,1</sub> |  | 1.0<br><sub>1,1,0,2,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.3 |
| Harrison Barnes | 67% | 13.4<br><sub>14,-,-,21,13</sub> | 4.8<br><sub>3,-,-,13,4</sub> |  | 1.6<br><sub>0,-,-,0,2</sub> |  | 0.7<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>0,-,-,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.1 |
| Carter Bryant | 72% | 9.5<br><sub>17,5,11,14,-</sub> | 3.4<br><sub>1,3,6,3,-</sub> |  | 1.6<br><sub>1,0,0,0,-</sub> |  | 0.6<br><sub>2,0,0,0,-</sub> |  | 0.3<br><sub>0,1,2,1,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.6 |
| Jordan McLaughlin | 48% | 7.2<br><sub>7,-,-,8,-</sub> | 2.4<br><sub>0,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 1.3<br><sub>2,-,-,3,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.8 |
| Tarris Reed Jr. | 52% | 7.0<br><sub>5,-,-,7,-</sub> | 2.9<br><sub>4,-,-,4,-</sub> |  | 4.1<br><sub>5,-,-,7,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.5 | 7.3 |
| David Jones Garcia | 48% | 5.9<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.8 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 97% | 38.7<br><sub>33,41,37,37,42</sub> | 25.6<br><sub>19,34,38,25,22</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>3,6,5,5,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 8.2<br><sub>5,14,5,6,12</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>3,3,9,2,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.3 | 3.5 | 38.5 |
| Domantas Sabonis | 98% | 35.0<br><sub>37,40,38,31,35</sub> | 16.2<br><sub>20,9,11,9,16</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 13.6<br><sub>14,15,14,7,17</sub> | 12.5<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>8,7,8,4,1</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.3 | 2.6 | 35.8 |
| Zach LaVine | 98% | 34.6<br><sub>31,39,21,28,35</sub> | 20.4<br><sub>22,21,11,23,21</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>3,3,0,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>3,5,1,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>3,3,0,5,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.2 | 2.6 | 27.1 |
| Precious Achiuwa | 98% | 29.3<br><sub>14,41,25,27,17</sub> | 12.4<br><sub>4,24,6,6,7</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>1,9,5,10,3</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>0,2,1,3,1</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 1.1 | 0.8 | 1.1 | 21.9 |
| Malik Monk | 98% | 22.2<br><sub>13,8,14,30,24</sub> | 11.7<br><sub>3,2,8,24,13</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,1,0,1,2</sub> |  | 3.7<br><sub>6,1,3,7,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,0,0,5,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.4 | 1.6 | 17.7 |
| Leaky Black | 58% | 22.0<br><sub>8,-,-,25,22</sub> | 5.8<br><sub>2,-,-,12,3</sub> |  | 3.6<br><sub>1,-,-,3,6</sub> |  | 1.1<br><sub>1,-,-,1,1</sub> |  | 0.7<br><sub>0,-,-,4,0</sub> |  | 0.9 | 0.4 | 0.7 | 10.5 |
| Jonathan Mogbo | 48% | 17.0<br><sub>18,-,25,-,-</sub> | 5.3<br><sub>2,-,6,-,-</sub> |  | 2.7<br><sub>5,-,3,-,-</sub> |  | 0.9<br><sub>0,-,3,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.6 | 0.4 | 0.6 | 8.9 |
| Emanuel Sharp | 97% | 16.6<br><sub>20,18,24,20,10</sub> | 4.5<br><sub>5,0,2,9,3</sub> |  | 1.4<br><sub>0,0,1,3,1</sub> |  | 0.9<br><sub>2,0,1,1,2</sub> |  | 0.5<br><sub>1,0,0,3,1</sub> |  | 0.5 | 0.2 | 0.6 | 6.8 |
| Dylan Cardwell | 96% | 16.5<br><sub>-,-,-,-,13</sub> | 4.7<br><sub>-,-,-,-,4</sub> |  | 5.9<br><sub>-,-,-,-,6</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 1.0 | 0.7 | 11.7 |
| Daeqwon Plowden | 86% | 12.9<br><sub>17,-,4,3,-</sub> | 4.2<br><sub>0,-,4,1,-</sub> |  | 1.6<br><sub>2,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.4 |
| Alex Karaban | 52% | 11.6<br><sub>11,12,10,-,-</sub> | 3.9<br><sub>0,6,0,-,-</sub> |  | 1.6<br><sub>1,0,1,-,-</sub> |  | 0.6<br><sub>1,0,1,-,-</sub> |  | 0.3<br><sub>0,2,0,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 6.0 |
| Nique Clifford | 91% | 11.1<br><sub>5,4,11,3,3</sub> | 4.1<br><sub>2,0,0,0,0</sub> |  | 1.7<br><sub>0,0,1,1,2</sub> |  | 1.1<br><sub>0,1,2,0,0</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-06/`._
