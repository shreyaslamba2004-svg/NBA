# NBA model · Fri 20 Nov 2026 (US date)

Updated **Fri 20 Nov, 10:33 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-20/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| CHA to win | CHA @ ATL | draftkings | 2.91 | 2.77 | 2.72 | 36.8% | 36.1% | 36.1% | +5.2% | +7.0% | 0.7% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 9.5 (10+) | TOR @ DET | draftkings | 14.40 | 12.42 | 6.02 | 16.6% | 6.5% | 8.1% | +15.9% | +139.0% | 0.3% |
| Jamal Shead PRA over 24.5 (25+) | TOR @ DET | draftkings | 11.60 | 10.78 | 6.25 | 16.0% | 8.1% | 9.3% | +7.7% | +85.7% | 0.2% |
| Jamal Shead AST over 9.5 (10+) | TOR @ DET | draftkings | 14.20 | 13.26 | 7.80 | 12.8% | 6.6% | 7.5% | +7.1% | +82.0% | 0.1% |
| Luka Doncic PA over 59.5 (60+) | SAC @ LAL | draftkings | 8.80 | 8.30 | 5.02 | 19.9% | 10.6% | 12.0% | +6.0% | +75.1% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III REB over 1.5 (2+) | NOP @ OKC | draftkings | 2.55 | Trey Murphy III | void | 92.2% | +15.3% |
| IND to win | IND @ CLE | draftkings | 3.31 | Peyton Watson | 33.1% | 26.5% | +8.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CHA @ ATL | Sat 21 Nov 11:00 | 106.5–109.7 | CHA 41% | 2.44 / 1.69 | ATL -3.5 | 216.5 | ATL -6.5 covers 41%; o218.5 45% |
| ORL @ BKN | Sat 21 Nov 11:30 | 116.2–110.6 | ORL 65% | 1.53 / 2.89 | BKN +5.5 | 226.5 | BKN +5.5 covers 49%; o224.5 55% |
| IND @ CLE | Sat 21 Nov 11:30 | 113.5–119.6 | IND 33% | 3.02 / 1.50 | CLE -6.5 | 232.5 | CLE -7.5 covers 47%; o233.5 49% |
| TOR @ DET | Sat 21 Nov 11:30 | 105.7–113.3 | TOR 30% | 3.39 / 1.42 | DET -7.5 | 218.5 | DET -7.5 covers 51%; o216.5 55% |
| WAS @ CHI | Sat 21 Nov 12:00 | 115.8–122.9 | WAS 31% | 3.27 / 1.44 | CHI -7.5 | 238.5 | CHI -2.5 covers 64%; o239.5 48% |
| NOP @ OKC | Sat 21 Nov 12:00 | 106.0–119.2 | NOP 17% | 5.81 / 1.21 | OKC -13.5 | 225.5 | OKC -11.5 covers 54%; o228.5 43% |
| PHX @ UTA | Sat 21 Nov 13:30 | 121.2–115.1 | PHX 66% | 1.51 / 2.96 | UTA +6.5 | 236.5 | UTA +4.5 covers 45%; o226.5 70% |
| HOU @ DEN | Sat 21 Nov 14:00 | 111.3–115.7 | HOU 37% | 2.68 / 1.60 | DEN -4.5 | 226.5 | DEN -1.5 covers 60%; o225.5 53% |
| SAC @ LAL | Sat 21 Nov 14:00 | 105.7–122.7 | SAC 11% | 8.76 / 1.13 | LAL -17.5 | 228.5 | LAL -14.5 covers 57%; o229.5 48% |

### CHA @ ATL
Out: Mouhamed Gueye (ATL), Jock Landale (ATL), CJ McCollum (ATL), Asa Newell (ATL), Grayson Allen (CHA), Kon Knueppel (CHA), Dennis Schroder (CHA), Grant Williams (CHA)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.5–109.7 | CHA 41% | 2.44 / 1.69 | ATL -3.5 | 216.5 | ATL -6.5 covers 41%; o218.5 45% |
| Expected (weighted by chance each plays) | 106.6–110.9 | CHA 37% | 2.72 / 1.58 | ATL -4.5 | 217.5 | ATL -6.5 covers 45%; o218.5 48% |
| if Kingston Flemings plays | 107.1–111.2 | CHA 39% | 2.58 / 1.63 | ATL -4.5 | 218.5 | ATL -6.5 covers 43%; o218.5 49% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Questionable | 55% | 13.2 | 5.0 | 2.0 | 0.9 | 0.5 | 0.3 | 0.1 | 0.7 | 7.9 | small |
| RayJ Dennis (ATL) | Questionable | 55% | 13.8 | 5.2 | 1.9 | 2.4 | 0.6 | 0.5 | 0.3 | 0.8 | 9.6 | small |
| Kingston Flemings (ATL) | Questionable | 55% | 22.2 | 8.1 | 2.5 | 3.7 | 0.7 | 0.8 | 0.3 | 1.8 | 14.3 | full tables below |
| Rafael Castro (ATL) | Questionable | 55% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.0 | small |

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 98% | 33.5<br><sub>26,32,34,27,42</sub> | 19.5<br><sub>14,25,16,17,23</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 8.8<br><sub>6,13,8,4,11</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>2,4,3,3,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.4<br><sub>2,4,1,3,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.8 | 2.9 | 31.5 |
| Brandon Miller | 98% | 32.0<br><sub>14,-,-,24,32</sub> | 21.7<br><sub>8,-,-,5,28</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>2,-,-,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>1,-,-,4,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.0<br><sub>0,-,-,1,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.6 | 2.9 | 30.0 |
| Sion James | 98% | 31.9<br><sub>21,33,32,35,30</sub> | 8.2<br><sub>11,11,3,3,3</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>3,4,8,8,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.6<br><sub>0,4,6,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>3,3,0,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 1.8 | 16.5 |
| Moussa Diabate | 98% | 31.6<br><sub>-,-,32,26,38</sub> | 9.2<br><sub>-,-,7,12,5</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 11.2<br><sub>-,-,13,12,16</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>-,-,2,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 1.1 | 1.1 | 1.9 | 23.1 |
| Royce O'Neale | 98% | 26.2<br><sub>26,23,22,19,34</sub> | 7.8<br><sub>7,10,7,3,13</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,3,4,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,1,0,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,2,2,1,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 1.2 | 13.8 |
| Coby White | 98% | 25.0<br><sub>16,20,20,20,26</sub> | 17.8<br><sub>7,10,21,21,19</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>1,2,3,0,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>1,9,3,1,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>1,0,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.2 | 3.2 | 24.9 |
| Ryan Kalkbrenner | 98% | 18.9<br><sub>21,35,16,18,14</sub> | 5.4<br><sub>4,8,2,5,6</sub> |  | 5.4<br><sub>5,15,6,5,3</sub> |  | 1.2<br><sub>0,3,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.0 | 11.9 |
| Christian Anderson | 91% | 18.2<br><sub>25,16,18,18,14</sub> | 8.4<br><sub>4,9,13,16,5</sub> |  | 2.2<br><sub>3,1,0,3,1</sub> |  | 2.5<br><sub>5,1,2,2,4</sub> |  | 1.2<br><sub>0,3,3,4,1</sub> |  | 0.7 | 0.2 | 1.6 | 13.1 |
| Tidjane Salaun | 96% | 14.4<br><sub>23,18,16,5,5</sub> | 5.3<br><sub>13,14,2,0,0</sub> |  | 3.4<br><sub>4,3,4,2,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.6<br><sub>2,3,0,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.2 |
| Liam McNeeley | 52% | 12.8<br><sub>19,16,-,2,-</sub> | 5.2<br><sub>8,8,-,0,-</sub> |  | 2.3<br><sub>2,1,-,0,-</sub> |  | 1.0<br><sub>3,1,-,0,-</sub> |  | 0.5<br><sub>1,2,-,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.5 |
| Hannes Steinbach | 63% | 12.3<br><sub>27,13,-,-,-</sub> | 3.2<br><sub>4,2,-,-,-</sub> |  | 3.4<br><sub>11,3,-,-,-</sub> |  | 0.5<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.6 | 0.7 | 7.2 |
| PJ Hall | 38% | 8.9<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.4 | 0.7 | 7.0 |

</details>

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 37.1<br><sub>36,38,40,35,34</sub> | 23.5<br><sub>30,15,27,14,16</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 9.3<br><sub>7,7,11,11,12</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 8.4<br><sub>6,4,10,5,11</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,0,0,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.5 | 3.5 | 41.2 |
| Nickeil Alexander-Walker | 99% | 35.6<br><sub>31,34,41,33,32</sub> | 23.0<br><sub>20,20,16,20,19</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,4,6,5,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.1<br><sub>1,4,3,4,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.4<br><sub>2,4,1,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.5 | 2.4 | 30.7 |
| Dyson Daniels | 99% | 34.9<br><sub>31,31,36,27,37</sub> | 12.1<br><sub>9,10,6,9,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>10,6,9,10,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.5<br><sub>7,8,4,5,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 2.5 | 0.4 | 1.8 | 26.4 |
| Onyeka Okongwu | 99% | 34.9<br><sub>30,30,35,36,36</sub> | 16.8<br><sub>16,16,17,16,28</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>2,9,6,11,9</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>5,3,1,0,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>2,2,2,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 1.0 | 1.7 | 28.0 |
| Luguentz Dort | 99% | 30.1<br><sub>20,18,20,18,31</sub> | 11.0<br><sub>3,4,10,3,16</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>2,3,1,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,2,2,0,0</sub> |  | 1.8<br><sub>1,1,1,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 0.9 | 16.4 |
| Aaron Wiggins | 98% | 29.3<br><sub>26,23,26,24,26</sub> | 14.1<br><sub>20,15,9,7,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>4,3,4,3,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>6,3,3,3,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>5,4,1,1,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 1.6 | 20.7 |
| Corey Kispert | 63% | 16.9<br><sub>-,-,-,16,17</sub> | 8.1<br><sub>-,-,-,14,8</sub> |  | 1.9<br><sub>-,-,-,3,1</sub> |  | 1.3<br><sub>-,-,-,1,2</sub> |  | 1.2<br><sub>-,-,-,3,2</sub> |  | 0.3 | 0.2 | 0.6 | 11.3 |
| Zuby Ejiofor | 72% | 14.1<br><sub>18,4,-,12,12</sub> | 4.8<br><sub>7,0,-,4,3</sub> |  | 3.0<br><sub>6,0,-,3,3</sub> |  | 1.0<br><sub>0,0,-,0,0</sub> |  | 0.4<br><sub>1,0,-,1,1</sub> |  | 0.5 | 0.2 | 0.6 | 8.8 |
| Dorian Finney-Smith | 38% | 10.2<br><sub>-,-,-,-,5</sub> | 2.3<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.3 |

</details>

<details><summary>if Kingston Flemings plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 36.3<br><sub>36,38,40,35,34</sub> | 22.0<br><sub>30,15,27,14,16</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 9.1<br><sub>7,7,11,11,12</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 7.6<br><sub>6,4,10,5,11</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>0,0,0,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.5 | 3.3 | 38.7 |
| Nickeil Alexander-Walker (ATL) | 99% | 34.8<br><sub>31,34,41,33,32</sub> | 22.0<br><sub>20,20,16,20,19</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,4,6,5,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.6<br><sub>1,4,3,4,7</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.4<br><sub>2,4,1,2,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.5 | 2.2 | 29.1 |
| Onyeka Okongwu (ATL) | 99% | 34.4<br><sub>30,30,35,36,36</sub> | 15.9<br><sub>16,16,17,16,28</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 8.0<br><sub>2,9,6,11,9</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.9<br><sub>5,3,1,0,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>2,2,2,3,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 1.0 | 1.6 | 26.8 |
| Dyson Daniels (ATL) | 99% | 34.3<br><sub>31,31,36,27,37</sub> | 11.9<br><sub>9,10,6,9,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 7.6<br><sub>10,6,9,10,10</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.0<br><sub>7,8,4,5,4</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 2.5 | 0.4 | 1.6 | 25.4 |
| Luguentz Dort (ATL) | 99% | 28.2<br><sub>20,18,20,18,31</sub> | 10.2<br><sub>3,4,10,3,16</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,3,1,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,2,2,0,0</sub> |  | 1.7<br><sub>1,1,1,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 0.8 | 15.2 |
| Aaron Wiggins (ATL) | 98% | 27.6<br><sub>26,23,26,24,26</sub> | 13.6<br><sub>20,15,9,7,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>4,3,4,3,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>6,3,3,3,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>5,4,1,1,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 1.4 | 19.5 |
| Kingston Flemings (ATL) | 100% | 22.2<br><sub>27,24,17,-,-</sub> | 8.1<br><sub>10,8,0,-,-</sub> | 8.5 · – | 2.5<br><sub>2,3,1,-,-</sub> | 2.5 | 3.7<br><sub>1,4,1,-,-</sub> | 3.5 | 0.7<br><sub>0,1,0,-,-</sub> |  | 0.8 | 0.3 | 1.8 | 14.3 |
| Corey Kispert (ATL) | 63% | 15.1<br><sub>-,-,-,16,17</sub> | 7.5<br><sub>-,-,-,14,8</sub> |  | 1.7<br><sub>-,-,-,3,1</sub> |  | 1.1<br><sub>-,-,-,1,2</sub> |  | 1.1<br><sub>-,-,-,3,2</sub> |  | 0.3 | 0.1 | 0.6 | 10.3 |
| Zuby Ejiofor (ATL) | 72% | 12.7<br><sub>18,4,-,12,12</sub> | 4.4<br><sub>7,0,-,4,3</sub> |  | 2.7<br><sub>6,0,-,3,3</sub> |  | 0.9<br><sub>0,0,-,0,0</sub> |  | 0.4<br><sub>1,0,-,1,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.0 |
| Dorian Finney-Smith (ATL) | 38% | 7.7<br><sub>-,-,-,-,5</sub> | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.2 | 3.3 |
| Naz Reid (CHA) | 98% | 33.5<br><sub>26,32,34,27,42</sub> | 19.6<br><sub>14,25,16,17,23</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 8.8<br><sub>6,13,8,4,11</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>2,4,3,3,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.4<br><sub>2,4,1,3,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.8 | 2.9 | 31.6 |
| Sion James (CHA) | 98% | 32.0<br><sub>21,33,32,35,30</sub> | 8.2<br><sub>11,11,3,3,3</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>3,4,8,8,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.6<br><sub>0,4,6,4,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>3,3,0,1,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 1.7 | 16.5 |
| Brandon Miller (CHA) | 98% | 32.0<br><sub>14,-,-,24,32</sub> | 21.6<br><sub>8,-,-,5,28</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>2,-,-,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>1,-,-,4,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.0<br><sub>0,-,-,1,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.6 | 2.9 | 30.0 |
| Moussa Diabate (CHA) | 98% | 31.7<br><sub>-,-,32,26,38</sub> | 9.2<br><sub>-,-,7,12,5</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 11.2<br><sub>-,-,13,12,16</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>-,-,2,2,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>-,-,0,0,0</sub> |  | 1.1 | 1.1 | 1.9 | 23.2 |
| Royce O'Neale (CHA) | 98% | 26.2<br><sub>26,23,22,19,34</sub> | 7.8<br><sub>7,10,7,3,13</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,3,4,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,1,0,1,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,2,2,1,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.4 | 1.2 | 13.9 |
| Coby White (CHA) | 98% | 25.0<br><sub>16,20,20,20,26</sub> | 17.9<br><sub>7,10,21,21,19</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>1,2,3,0,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>1,9,3,1,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>1,0,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.7 | 0.2 | 3.2 | 25.0 |
| Ryan Kalkbrenner (CHA) | 98% | 18.8<br><sub>21,35,16,18,14</sub> | 5.3<br><sub>4,8,2,5,6</sub> |  | 5.3<br><sub>5,15,6,5,3</sub> |  | 1.2<br><sub>0,3,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.0 | 11.9 |
| Christian Anderson (CHA) | 91% | 18.2<br><sub>25,16,18,18,14</sub> | 8.5<br><sub>4,9,13,16,5</sub> |  | 2.1<br><sub>3,1,0,3,1</sub> |  | 2.5<br><sub>5,1,2,2,4</sub> |  | 1.2<br><sub>0,3,3,4,1</sub> |  | 0.7 | 0.2 | 1.6 | 13.1 |
| Tidjane Salaun (CHA) | 96% | 14.3<br><sub>23,18,16,5,5</sub> | 5.3<br><sub>13,14,2,0,0</sub> |  | 3.3<br><sub>4,3,4,2,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.6<br><sub>2,3,0,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.1 |
| Liam McNeeley (CHA) | 52% | 12.8<br><sub>19,16,-,2,-</sub> | 5.3<br><sub>8,8,-,0,-</sub> |  | 2.3<br><sub>2,1,-,0,-</sub> |  | 1.0<br><sub>3,1,-,0,-</sub> |  | 0.6<br><sub>1,2,-,0,-</sub> |  | 0.4 | 0.2 | 0.7 | 8.5 |
| Hannes Steinbach (CHA) | 63% | 12.4<br><sub>27,13,-,-,-</sub> | 3.2<br><sub>4,2,-,-,-</sub> |  | 3.4<br><sub>11,3,-,-,-</sub> |  | 0.5<br><sub>1,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.6 | 0.7 | 7.1 |
| PJ Hall (CHA) | 38% | 9.0<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 3.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.5 | 0.7 | 7.1 |

</details>


### ORL @ BKN
Out: Grant Nelson (BKN), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL)

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 33.2<br><sub>38,39,36,38,36</sub> | 24.4<br><sub>33,38,35,21,27</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>7,8,9,8,8</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 6.7<br><sub>7,1,12,9,11</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>1,3,3,0,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 2.9 | 36.8 |
| Desmond Bane | 98% | 32.9<br><sub>36,34,35,39,38</sub> | 19.8<br><sub>15,25,21,24,15</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>6,3,5,8,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>4,2,3,5,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>4,7,6,3,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.4 | 1.9 | 27.2 |
| Anthony Black | 98% | 31.3<br><sub>33,39,37,33,37</sub> | 15.5<br><sub>26,22,5,20,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>7,7,2,2,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 4.8<br><sub>5,8,5,7,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,3,1,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.8 | 0.7 | 2.4 | 24.4 |
| Wendell Carter Jr. | 98% | 29.2<br><sub>33,28,30,28,32</sub> | 12.6<br><sub>8,9,12,10,15</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 7.2<br><sub>11,7,8,3,8</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,3,0,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8<br><sub>0,0,1,1,2</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.8 | 1.4 | 21.6 |
| Jalen Suggs | 98% | 27.6<br><sub>-,-,21,25,31</sub> | 11.4<br><sub>-,-,3,12,18</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>-,-,2,6,8</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.5<br><sub>-,-,3,4,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>-,-,1,2,5</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.7 | 0.6 | 2.4 | 19.5 |
| Tristan da Silva | 88% | 26.2<br><sub>-,-,31,31,27</sub> | 11.7<br><sub>-,-,12,13,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>-,-,6,6,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>-,-,2,3,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>-,-,2,3,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.1 | 17.1 |
| Goga Bitadze | 91% | 16.0<br><sub>15,20,18,20,20</sub> | 6.5<br><sub>2,4,12,10,8</sub> |  | 4.8<br><sub>2,7,4,6,3</sub> |  | 1.2<br><sub>1,0,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.8 | 12.6 |
| Jevon Carter | 88% | 14.8<br><sub>4,28,17,12,16</sub> | 5.9<br><sub>0,11,5,3,6</sub> |  | 1.5<br><sub>0,3,2,2,2</sub> |  | 1.8<br><sub>0,4,2,1,3</sub> |  | 0.9<br><sub>0,3,1,1,2</sub> |  | 0.7 | 0.2 | 0.5 | 9.2 |
| Jase Richardson | 52% | 12.4<br><sub>15,20,-,-,-</sub> | 4.6<br><sub>6,6,-,-,-</sub> |  | 1.4<br><sub>1,1,-,-,-</sub> |  | 1.4<br><sub>1,2,-,-,-</sub> |  | 0.4<br><sub>0,1,-,-,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.3 |
| Jamal Cain | 88% | 11.5<br><sub>20,-,4,15,4</sub> | 4.5<br><sub>5,-,0,2,0</sub> |  | 2.1<br><sub>3,-,4,5,1</sub> |  | 0.5<br><sub>1,-,1,0,0</sub> |  | 0.4<br><sub>1,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.2 |
| Nikola Vucevic | 63% | 9.0<br><sub>18,14,11,-,-</sub> | 3.8<br><sub>5,3,2,-,-</sub> |  | 2.5<br><sub>4,5,3,-,-</sub> |  | 1.0<br><sub>1,1,0,-,-</sub> |  | 0.3<br><sub>1,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 7.3 |
| Alex Morales | 52% | 7.4<br><sub>29,18,-,-,-</sub> | 1.9<br><sub>7,5,-,-,-</sub> |  | 1.3<br><sub>7,4,-,-,-</sub> |  | 0.5<br><sub>0,3,-,-,-</sub> |  | 0.1<br><sub>1,1,-,-,-</sub> |  | 0.3 | 0.0 | 0.4 | 3.7 |
| Colin Castleton | 48% | 6.1<br><sub>-,1,-,-,-</sub> | 2.2<br><sub>-,0,-,-,-</sub> |  | 1.8<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.6 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 88% | 31.0<br><sub>29,28,-,40,27</sub> | 18.9<br><sub>19,22,-,25,5</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>9,6,-,6,3</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>0,3,-,2,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>4,4,-,2,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.4 | 2.0 | 27.0 |
| Julius Randle | 98% | 30.4<br><sub>30,29,31,34,27</sub> | 18.5<br><sub>13,17,22,33,17</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>4,4,4,6,0</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,5,5,1,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,0,3,2,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 3.0 | 28.0 |
| Egor Demin | 98% | 23.1<br><sub>-,23,27,26,31</sub> | 10.7<br><sub>-,22,11,9,22</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>-,1,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.7<br><sub>-,1,2,4,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>-,4,3,2,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.3 | 1.5 | 15.9 |
| Day'Ron Sharpe | 98% | 21.9<br><sub>20,19,28,25,22</sub> | 8.7<br><sub>6,15,16,6,6</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 6.9<br><sub>4,4,11,9,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>6,5,5,5,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>0,2,0,0,0</sub> |  | 1.0 | 1.0 | 1.7 | 18.9 |
| Nolan Traore | 98% | 20.7<br><sub>21,-,20,30,23</sub> | 10.2<br><sub>14,-,11,23,13</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,-,1,1,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 3.1<br><sub>2,-,2,4,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>2,-,0,2,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.9 | 15.0 |
| Mikel Brown Jr. | 98% | 19.7<br><sub>-,-,20,18,27</sub> | 9.7<br><sub>-,-,6,3,15</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>-,-,1,1,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 3.1<br><sub>-,-,2,5,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>-,-,2,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.2 | 1.8 | 14.6 |
| Noah Clowney | 98% | 19.4<br><sub>8,19,35,24,19</sub> | 7.5<br><sub>2,16,15,9,7</sub> |  | 3.3<br><sub>0,3,7,3,3</sub> |  | 1.0<br><sub>0,0,3,3,1</sub> |  | 1.0<br><sub>0,2,3,1,1</sub> |  | 0.6 | 0.6 | 0.9 | 11.8 |
| Danny Wolf | 88% | 18.8<br><sub>36,29,28,11,23</sub> | 8.0<br><sub>10,10,14,3,6</sub> |  | 4.4<br><sub>3,11,6,2,6</sub> |  | 1.7<br><sub>2,4,1,1,2</sub> |  | 1.0<br><sub>1,1,4,1,1</sub> |  | 0.6 | 0.5 | 1.1 | 14.1 |
| Moritz Wagner | 98% | 15.9<br><sub>16,19,18,10,20</sub> | 8.2<br><sub>12,16,10,4,11</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>3,3,6,5,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,4,4,1,3</sub> |  | 0.6<br><sub>1,2,2,0,2</sub> | 0.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.2 | 1.0 | 13.1 |
| Keon Ellis | 91% | 11.8<br><sub>22,26,7,20,6</sub> | 2.9<br><sub>3,11,0,8,3</sub> |  | 1.2<br><sub>1,4,0,2,1</sub> |  | 0.8<br><sub>4,3,1,0,0</sub> |  | 0.3<br><sub>1,2,0,2,1</sub> |  | 0.7 | 0.4 | 0.4 | 4.9 |
| Ben Saraf | 58% | 9.5<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 1.2 | 6.5 |
| Terance Mann | 67% | 9.4<br><sub>22,18,9,-,5</sub> | 2.5<br><sub>0,6,2,-,0</sub> |  | 1.1<br><sub>1,1,1,-,1</sub> |  | 0.9<br><sub>1,3,1,-,0</sub> |  | 0.2<br><sub>0,2,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Chaney Johnson | 98% | 8.9<br><sub>15,15,12,1,6</sub> | 2.6<br><sub>2,4,1,0,2</sub> |  | 1.4<br><sub>0,3,5,0,2</sub> |  | 0.5<br><sub>1,2,0,0,1</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 4.5 |
| Tyler Bilodeau | 3% | 8.5 | 3.7 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Josh Minott | 64% | 7.4<br><sub>12,7,2,-,4</sub> | 4.0<br><sub>10,0,0,-,0</sub> |  | 1.3<br><sub>2,2,0,-,0</sub> |  | 0.4<br><sub>1,0,0,-,0</sub> |  | 0.4<br><sub>2,0,0,-,0</sub> |  | 0.4 | 0.3 | 0.4 | 5.7 |
| Drake Powell | 64% | 6.4<br><sub>9,7,2,-,-</sub> | 2.1<br><sub>2,6,2,-,-</sub> |  | 0.6<br><sub>2,0,0,-,-</sub> |  | 0.5<br><sub>1,0,0,-,-</sub> |  | 0.1<br><sub>0,1,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.2 |
| Joshua Jefferson | 80% | 5.6<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 0.9 |

</details>


### IND @ CLE
Out: Evan Mobley (CLE), Nae'Qwan Tomlin (CLE), Jaylon Tyson (CLE), Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.5–119.6 | IND 33% | 3.02 / 1.50 | CLE -6.5 | 232.5 | CLE -7.5 covers 47%; o233.5 49% |
| Expected (weighted by chance each plays) | 113.8–120.9 | IND 31% | 3.23 / 1.45 | CLE -7.5 | 234.5 | CLE -7.5 covers 49%; o233.5 52% |
| if Peyton Watson plays | 113.4–122.2 | IND 27% | 3.77 / 1.36 | CLE -8.5 | 235.5 | CLE -7.5 covers 54%; o233.5 54% |
| if Andrew Nembhard plays | 114.2–119.3 | IND 36% | 2.78 / 1.56 | CLE -5.5 | 233.5 | CLE -7.5 covers 44%; o233.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Braden Smith (IND) | Questionable | 55% | 16.8 | 5.4 | 1.8 | 2.9 | 0.4 | 0.9 | 0.2 | 0.9 | 10.0 | small |
| Peyton Watson (CLE) | Questionable | 55% | 25.5 | 11.5 | 4.4 | 2.1 | 1.1 | 0.8 | 1.3 | 1.4 | 18.0 | full tables below |
| Andrew Nembhard (IND) | Questionable | 55% | 33.0 | 16.5 | 2.9 | 8.1 | 1.9 | 0.9 | 0.1 | 2.3 | 27.4 | full tables below |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 91% | 34.2<br><sub>35,32,32,34,33</sub> | 24.6<br><sub>29,28,19,31,24</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>9,8,3,2,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 4.9<br><sub>8,5,2,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>5,2,2,0,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.3 | 35.7 |
| Aaron Nesmith | 91% | 31.2<br><sub>34,22,33,36,29</sub> | 14.6<br><sub>18,2,18,12,2</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,1,7,4,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>2,1,1,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.0<br><sub>4,0,2,0,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 1.5 | 20.9 |
| Kelly Oubre Jr. | 88% | 28.4<br><sub>23,34,30,29,23</sub> | 12.8<br><sub>14,14,16,16,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,6,5,4,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>2,1,0,2,0</sub> |  | 1.3<br><sub>1,0,1,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 1.2 | 18.7 |
| Ivica Zubac | 86% | 26.6<br><sub>28,31,26,22,24</sub> | 11.6<br><sub>16,20,12,8,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>3,12,13,5,3</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>0,1,1,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 1.4 | 22.7 |
| Quenton Jackson | 98% | 26.0<br><sub>25,21,20,30,22</sub> | 12.0<br><sub>10,4,3,15,15</sub> |  | 3.6<br><sub>5,2,5,6,2</sub> |  | 4.7<br><sub>4,2,4,8,3</sub> |  | 1.2<br><sub>2,1,1,1,2</sub> |  | 1.2 | 0.2 | 1.6 | 20.4 |
| Obi Toppin | 88% | 19.9<br><sub>19,16,16,14,17</sub> | 11.0<br><sub>10,8,9,5,6</sub> |  | 4.0<br><sub>2,3,3,2,1</sub> |  | 1.9<br><sub>4,1,1,1,1</sub> |  | 1.4<br><sub>0,2,1,0,0</sub> |  | 0.6 | 0.2 | 1.0 | 16.9 |
| T.J. McConnell | 91% | 19.5<br><sub>8,14,17,19,18</sub> | 10.2<br><sub>2,7,6,12,14</sub> |  | 2.7<br><sub>0,3,3,5,2</sub> |  | 6.2<br><sub>3,7,7,5,5</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.2 | 1.6 | 19.1 |
| Jarace Walker | 88% | 19.0<br><sub>10,7,-,14,17</sub> | 7.8<br><sub>7,1,-,2,1</sub> |  | 3.9<br><sub>1,1,-,5,3</sub> |  | 1.9<br><sub>0,0,-,2,1</sub> |  | 1.0<br><sub>2,0,-,0,0</sub> |  | 0.6 | 0.3 | 1.1 | 13.6 |
| Jay Huff | 88% | 17.2<br><sub>-,11,8,18,15</sub> | 7.7<br><sub>-,6,8,11,5</sub> |  | 3.3<br><sub>-,4,1,0,3</sub> |  | 1.2<br><sub>-,0,0,2,0</sub> |  | 0.9<br><sub>-,0,2,3,0</sub> |  | 0.4 | 0.9 | 0.7 | 12.2 |
| Kobe Brown | 86% | 14.8<br><sub>-,-,-,3,2</sub> | 5.2<br><sub>-,-,-,0,0</sub> |  | 2.5<br><sub>-,-,-,0,0</sub> |  | 1.4<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 9.2 |
| Jalen Slawson | 88% | 14.8<br><sub>-,12,10,14,12</sub> | 4.6<br><sub>-,2,1,8,5</sub> |  | 3.0<br><sub>-,3,4,5,4</sub> |  | 1.5<br><sub>-,1,0,2,2</sub> |  | 0.4<br><sub>-,0,0,1,1</sub> |  | 0.8 | 0.5 | 0.7 | 9.1 |
| Larry Nance Jr. | 97% | 13.1<br><sub>14,5,14,7,9</sub> | 4.2<br><sub>4,5,2,4,3</sub> |  | 2.4<br><sub>0,0,2,2,1</sub> |  | 0.8<br><sub>0,0,1,2,0</sub> |  | 0.5<br><sub>0,1,0,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.5 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 99% | 34.8<br><sub>36,33,-,36,35</sub> | 29.0<br><sub>23,25,-,39,34</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>7,4,-,4,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.3<br><sub>6,7,-,4,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>2,5,-,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.4 | 3.0 | 39.3 |
| James Harden | 99% | 34.6<br><sub>33,35,-,34,36</sub> | 19.4<br><sub>32,20,-,9,14</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>2,6,-,4,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.8<br><sub>4,8,-,10,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>5,2,-,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 3.2 | 31.3 |
| Jarrett Allen | 88% | 29.2<br><sub>32,32,-,30,30</sub> | 14.8<br><sub>11,9,-,13,19</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 9.7<br><sub>14,8,-,14,9</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,1,-,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.9 | 1.2 | 1.4 | 26.4 |
| Tyrese Proctor | 96% | 27.5<br><sub>23,27,34,29,26</sub> | 13.0<br><sub>15,22,24,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,4,11,3,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>1,3,10,2,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,5,4,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.1 | 1.3 | 20.7 |
| Meleek Thomas | 96% | 26.5<br><sub>22,18,34,30,22</sub> | 12.8<br><sub>14,12,20,10,14</sub> |  | 3.2<br><sub>4,0,4,6,2</sub> |  | 1.9<br><sub>1,3,2,3,2</sub> |  | 2.2<br><sub>2,2,3,1,4</sub> |  | 1.0 | 0.3 | 1.2 | 17.9 |
| Sam Merrill | 98% | 24.2<br><sub>-,-,-,-,23</sub> | 9.4<br><sub>-,-,-,-,7</sub> |  | 2.9<br><sub>-,-,-,-,2</sub> |  | 2.0<br><sub>-,-,-,-,3</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 0.8 | 0.1 | 0.6 | 14.3 |
| Mario Hezonja | 98% | 23.2<br><sub>7,9,34,15,28</sub> | 9.7<br><sub>0,4,22,9,16</sub> |  | 5.9<br><sub>0,4,7,4,7</sub> |  | 2.1<br><sub>0,0,4,2,5</sub> |  | 1.1<br><sub>0,0,2,1,2</sub> |  | 0.7 | 0.3 | 1.0 | 17.7 |
| Thomas Bryant | 86% | 16.8<br><sub>-,16,27,18,12</sub> | 8.8<br><sub>-,9,19,9,5</sub> |  | 4.8<br><sub>-,1,11,5,4</sub> |  | 1.0<br><sub>-,1,3,4,0</sub> |  | 0.9<br><sub>-,0,2,0,1</sub> |  | 0.4 | 0.6 | 0.6 | 14.5 |
| Norchad Omier | 67% | 16.7<br><sub>-,-,27,13,16</sub> | 4.7<br><sub>-,-,13,4,2</sub> |  | 5.3<br><sub>-,-,8,6,7</sub> |  | 1.3<br><sub>-,-,2,2,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 11.3 |
| Craig Porter Jr. | 88% | 15.6<br><sub>-,9,28,14,12</sub> | 3.8<br><sub>-,0,9,2,2</sub> |  | 3.1<br><sub>-,2,9,1,3</sub> |  | 2.6<br><sub>-,2,6,3,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.5 | 0.8 | 9.5 |
| Riley Minix | 48% | 12.0<br><sub>-,-,22,-,-</sub> | 4.1<br><sub>-,-,2,-,-</sub> |  | 1.6<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 6.3 |
| Zack Austin | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Andrew Nembhard plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 99% | 34.7<br><sub>33,35,-,34,36</sub> | 19.4<br><sub>32,20,-,9,14</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>2,6,-,4,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.8<br><sub>4,8,-,10,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>5,2,-,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 3.3 | 31.2 |
| Donovan Mitchell (CLE) | 99% | 34.7<br><sub>36,33,-,36,35</sub> | 28.9<br><sub>23,25,-,39,34</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>7,4,-,4,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.3<br><sub>6,7,-,4,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>2,5,-,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.3 | 3.0 | 39.1 |
| Jarrett Allen (CLE) | 88% | 29.2<br><sub>32,32,-,30,30</sub> | 14.8<br><sub>11,9,-,13,19</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 9.7<br><sub>14,8,-,14,9</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,1,-,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,-,0,0</sub> |  | 1.0 | 1.2 | 1.4 | 26.4 |
| Tyrese Proctor (CLE) | 96% | 27.6<br><sub>23,27,34,29,26</sub> | 12.9<br><sub>15,22,24,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,4,11,3,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>1,3,10,2,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>3,5,4,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.1 | 1.3 | 20.6 |
| Meleek Thomas (CLE) | 96% | 26.5<br><sub>22,18,34,30,22</sub> | 12.8<br><sub>14,12,20,10,14</sub> |  | 3.2<br><sub>4,0,4,6,2</sub> |  | 1.9<br><sub>1,3,2,3,2</sub> |  | 2.2<br><sub>2,2,3,1,4</sub> |  | 1.0 | 0.3 | 1.2 | 17.9 |
| Sam Merrill (CLE) | 98% | 24.1<br><sub>-,-,-,-,23</sub> | 9.4<br><sub>-,-,-,-,7</sub> |  | 2.8<br><sub>-,-,-,-,2</sub> |  | 2.0<br><sub>-,-,-,-,3</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 0.7 | 0.1 | 0.6 | 14.2 |
| Mario Hezonja (CLE) | 98% | 23.3<br><sub>7,9,34,15,28</sub> | 9.7<br><sub>0,4,22,9,16</sub> |  | 6.0<br><sub>0,4,7,4,7</sub> |  | 2.1<br><sub>0,0,4,2,5</sub> |  | 1.2<br><sub>0,0,2,1,2</sub> |  | 0.7 | 0.3 | 1.0 | 17.8 |
| Thomas Bryant (CLE) | 86% | 16.7<br><sub>-,16,27,18,12</sub> | 8.7<br><sub>-,9,19,9,5</sub> |  | 4.8<br><sub>-,1,11,5,4</sub> |  | 1.0<br><sub>-,1,3,4,0</sub> |  | 0.9<br><sub>-,0,2,0,1</sub> |  | 0.4 | 0.6 | 0.6 | 14.4 |
| Norchad Omier (CLE) | 67% | 16.7<br><sub>-,-,27,13,16</sub> | 4.7<br><sub>-,-,13,4,2</sub> |  | 5.3<br><sub>-,-,8,6,7</sub> |  | 1.3<br><sub>-,-,2,2,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.5 | 0.4 | 0.8 | 11.3 |
| Craig Porter Jr. (CLE) | 88% | 15.7<br><sub>-,9,28,14,12</sub> | 3.8<br><sub>-,0,9,2,2</sub> |  | 3.1<br><sub>-,2,9,1,3</sub> |  | 2.6<br><sub>-,2,6,3,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.5 | 0.8 | 9.6 |
| Riley Minix (CLE) | 48% | 11.9<br><sub>-,-,22,-,-</sub> | 4.1<br><sub>-,-,2,-,-</sub> |  | 1.6<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.3 |
| Zack Austin (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Andrew Nembhard (IND) | 100% | 33.0<br><sub>34,34,34,-,-</sub> | 16.5<br><sub>12,17,12,-,-</sub> | 15.5 · – | 2.9<br><sub>3,2,4,-,-</sub> | 2.5 | 8.1<br><sub>12,10,6,-,-</sub> | 6.5 | 1.9<br><sub>1,3,1,-,-</sub> | 1.5 | 0.9 | 0.1 | 2.3 | 27.4 |
| Pascal Siakam (IND) | 91% | 33.0<br><sub>35,32,32,34,33</sub> | 23.4<br><sub>29,28,19,31,24</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>9,8,3,2,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>8,5,2,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>5,2,2,0,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 1.9 | 33.2 |
| Aaron Nesmith (IND) | 91% | 28.4<br><sub>34,22,33,36,29</sub> | 12.5<br><sub>18,2,18,12,2</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>2,1,7,4,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,1,1,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.7<br><sub>4,0,2,0,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.4 | 1.2 | 17.8 |
| Kelly Oubre Jr. (IND) | 88% | 25.1<br><sub>23,34,30,29,23</sub> | 10.8<br><sub>14,14,16,16,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>2,6,5,4,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.3<br><sub>2,1,0,2,0</sub> |  | 1.1<br><sub>1,0,1,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.4 | 1.0 | 15.8 |
| Ivica Zubac (IND) | 86% | 24.8<br><sub>28,31,26,22,24</sub> | 10.6<br><sub>16,20,12,8,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.7<br><sub>3,12,13,5,3</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>0,1,1,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.6 | 1.2 | 21.0 |
| Quenton Jackson (IND) | 98% | 21.9<br><sub>25,21,20,30,22</sub> | 9.8<br><sub>10,4,3,15,15</sub> |  | 3.1<br><sub>5,2,5,6,2</sub> |  | 3.3<br><sub>4,2,4,8,3</sub> |  | 0.9<br><sub>2,1,1,1,2</sub> |  | 0.9 | 0.2 | 1.3 | 16.3 |
| Obi Toppin (IND) | 88% | 17.7<br><sub>19,16,16,14,17</sub> | 9.6<br><sub>10,8,9,5,6</sub> |  | 3.6<br><sub>2,3,3,2,1</sub> |  | 1.6<br><sub>4,1,1,1,1</sub> |  | 1.2<br><sub>0,2,1,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 14.8 |
| Jarace Walker (IND) | 88% | 16.2<br><sub>10,7,-,14,17</sub> | 6.3<br><sub>7,1,-,2,1</sub> |  | 3.4<br><sub>1,1,-,5,3</sub> |  | 1.5<br><sub>0,0,-,2,1</sub> |  | 0.8<br><sub>2,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 11.2 |
| T.J. McConnell (IND) | 91% | 16.0<br><sub>8,14,17,19,18</sub> | 8.4<br><sub>2,7,6,12,14</sub> |  | 2.2<br><sub>0,3,3,5,2</sub> |  | 5.0<br><sub>3,7,7,5,5</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.2 | 1.2 | 15.7 |
| Jay Huff (IND) | 88% | 14.7<br><sub>-,11,8,18,15</sub> | 6.4<br><sub>-,6,8,11,5</sub> |  | 2.9<br><sub>-,4,1,0,3</sub> |  | 1.0<br><sub>-,0,0,2,0</sub> |  | 0.8<br><sub>-,0,2,3,0</sub> |  | 0.3 | 0.8 | 0.6 | 10.3 |
| Jalen Slawson (IND) | 88% | 12.3<br><sub>-,12,10,14,12</sub> | 3.8<br><sub>-,2,1,8,5</sub> |  | 2.6<br><sub>-,3,4,5,4</sub> |  | 1.1<br><sub>-,1,0,2,2</sub> |  | 0.3<br><sub>-,0,0,1,1</sub> |  | 0.6 | 0.4 | 0.5 | 7.6 |
| Larry Nance Jr. (IND) | 97% | 11.0<br><sub>14,5,14,7,9</sub> | 3.6<br><sub>4,5,2,4,3</sub> |  | 2.1<br><sub>0,0,2,2,1</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.4<br><sub>0,1,0,1,1</sub> |  | 0.5 | 0.1 | 0.4 | 6.4 |
| Kobe Brown (IND) | 86% | 8.7<br><sub>-,-,-,3,2</sub> | 3.0<br><sub>-,-,-,0,0</sub> |  | 1.6<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.4 | 5.2 |

</details>

<details><summary>if Peyton Watson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell (CLE) | 99% | 32.6<br><sub>36,33,-,36,35</sub> | 26.9<br><sub>23,25,-,39,34</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>7,4,-,4,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 5.1<br><sub>6,7,-,4,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>2,5,-,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.3 | 0.3 | 2.7 | 36.8 |
| James Harden (CLE) | 99% | 32.5<br><sub>33,35,-,34,36</sub> | 18.2<br><sub>32,20,-,9,14</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>2,6,-,4,6</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>4,8,-,10,9</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>5,2,-,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 2.9 | 29.6 |
| Jarrett Allen (CLE) | 88% | 27.1<br><sub>32,32,-,30,30</sub> | 14.3<br><sub>11,9,-,13,19</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 9.1<br><sub>14,8,-,14,9</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>3,1,-,3,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.9 | 1.1 | 1.3 | 25.3 |
| Peyton Watson (CLE) | 100% | 25.5<br><sub>30,30,-,22,-</sub> | 11.5<br><sub>7,4,-,14,-</sub> | 12.5 · – | 4.4<br><sub>5,4,-,4,-</sub> | 4.5 | 2.1<br><sub>4,2,-,0,-</sub> |  | 1.1<br><sub>2,0,-,2,-</sub> | 1.5 | 0.8 | 1.3 | 1.4 | 18.0 |
| Meleek Thomas (CLE) | 96% | 23.7<br><sub>22,18,34,30,22</sub> | 11.7<br><sub>14,12,20,10,14</sub> |  | 3.0<br><sub>4,0,4,6,2</sub> |  | 1.8<br><sub>1,3,2,3,2</sub> |  | 1.9<br><sub>2,2,3,1,4</sub> |  | 0.9 | 0.2 | 1.1 | 16.5 |
| Tyrese Proctor (CLE) | 96% | 23.5<br><sub>23,27,34,29,26</sub> | 11.1<br><sub>15,22,24,17,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>3,4,11,3,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>1,3,10,2,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,5,4,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.1 | 1.1 | 17.9 |
| Sam Merrill (CLE) | 98% | 21.6<br><sub>-,-,-,-,23</sub> | 8.5<br><sub>-,-,-,-,7</sub> |  | 2.6<br><sub>-,-,-,-,2</sub> |  | 1.8<br><sub>-,-,-,-,3</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.7 | 0.1 | 0.6 | 12.9 |
| Mario Hezonja (CLE) | 98% | 20.6<br><sub>7,9,34,15,28</sub> | 9.0<br><sub>0,4,22,9,16</sub> |  | 5.3<br><sub>0,4,7,4,7</sub> |  | 1.9<br><sub>0,0,4,2,5</sub> |  | 1.0<br><sub>0,0,2,1,2</sub> |  | 0.7 | 0.2 | 0.9 | 16.2 |
| Norchad Omier (CLE) | 67% | 15.7<br><sub>-,-,27,13,16</sub> | 4.7<br><sub>-,-,13,4,2</sub> |  | 4.9<br><sub>-,-,8,6,7</sub> |  | 1.3<br><sub>-,-,2,2,0</sub> |  | 0.2<br><sub>-,-,1,0,0</sub> |  | 0.5 | 0.4 | 0.7 | 11.0 |
| Thomas Bryant (CLE) | 86% | 14.9<br><sub>-,16,27,18,12</sub> | 8.2<br><sub>-,9,19,9,5</sub> |  | 4.3<br><sub>-,1,11,5,4</sub> |  | 0.9<br><sub>-,1,3,4,0</sub> |  | 0.8<br><sub>-,0,2,0,1</sub> |  | 0.4 | 0.5 | 0.6 | 13.3 |
| Craig Porter Jr. (CLE) | 88% | 13.7<br><sub>-,9,28,14,12</sub> | 3.4<br><sub>-,0,9,2,2</sub> |  | 2.8<br><sub>-,2,9,1,3</sub> |  | 2.5<br><sub>-,2,6,3,1</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.5 | 0.7 | 8.7 |
| Zack Austin (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Riley Minix (CLE) | 48% | 8.2<br><sub>-,-,22,-,-</sub> | 3.0<br><sub>-,-,2,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.5 |
| Pascal Siakam (IND) | 91% | 34.1<br><sub>35,32,32,34,33</sub> | 24.5<br><sub>29,28,19,31,24</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>9,8,3,2,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 4.9<br><sub>8,5,2,2,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>5,2,2,0,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.3 | 2.2 | 35.6 |
| Aaron Nesmith (IND) | 91% | 31.2<br><sub>34,22,33,36,29</sub> | 14.6<br><sub>18,2,18,12,2</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,1,7,4,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>2,1,1,4,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.0<br><sub>4,0,2,0,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 1.5 | 20.8 |
| Kelly Oubre Jr. (IND) | 88% | 28.4<br><sub>23,34,30,29,23</sub> | 12.9<br><sub>14,14,16,16,17</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>2,6,5,4,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>2,1,0,2,0</sub> |  | 1.3<br><sub>1,0,1,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 1.2 | 18.7 |
| Ivica Zubac (IND) | 86% | 26.7<br><sub>28,31,26,22,24</sub> | 11.6<br><sub>16,20,12,8,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>3,12,13,5,3</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>0,1,1,2,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.7 | 1.4 | 22.8 |
| Quenton Jackson (IND) | 98% | 26.0<br><sub>25,21,20,30,22</sub> | 12.0<br><sub>10,4,3,15,15</sub> |  | 3.6<br><sub>5,2,5,6,2</sub> |  | 4.7<br><sub>4,2,4,8,3</sub> |  | 1.1<br><sub>2,1,1,1,2</sub> |  | 1.2 | 0.2 | 1.6 | 20.4 |
| Obi Toppin (IND) | 88% | 19.8<br><sub>19,16,16,14,17</sub> | 10.9<br><sub>10,8,9,5,6</sub> |  | 3.9<br><sub>2,3,3,2,1</sub> |  | 1.9<br><sub>4,1,1,1,1</sub> |  | 1.3<br><sub>0,2,1,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 16.7 |
| T.J. McConnell (IND) | 91% | 19.5<br><sub>8,14,17,19,18</sub> | 10.1<br><sub>2,7,6,12,14</sub> |  | 2.7<br><sub>0,3,3,5,2</sub> |  | 6.2<br><sub>3,7,7,5,5</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.2 | 1.6 | 19.0 |
| Jarace Walker (IND) | 88% | 19.0<br><sub>10,7,-,14,17</sub> | 7.7<br><sub>7,1,-,2,1</sub> |  | 3.9<br><sub>1,1,-,5,3</sub> |  | 1.9<br><sub>0,0,-,2,1</sub> |  | 0.9<br><sub>2,0,-,0,0</sub> |  | 0.6 | 0.3 | 1.1 | 13.5 |
| Jay Huff (IND) | 88% | 17.2<br><sub>-,11,8,18,15</sub> | 7.7<br><sub>-,6,8,11,5</sub> |  | 3.3<br><sub>-,4,1,0,3</sub> |  | 1.2<br><sub>-,0,0,2,0</sub> |  | 0.9<br><sub>-,0,2,3,0</sub> |  | 0.4 | 1.0 | 0.7 | 12.2 |
| Jalen Slawson (IND) | 88% | 14.9<br><sub>-,12,10,14,12</sub> | 4.7<br><sub>-,2,1,8,5</sub> |  | 3.0<br><sub>-,3,4,5,4</sub> |  | 1.4<br><sub>-,1,0,2,2</sub> |  | 0.4<br><sub>-,0,0,1,1</sub> |  | 0.8 | 0.5 | 0.7 | 9.1 |
| Kobe Brown (IND) | 86% | 14.8<br><sub>-,-,-,3,2</sub> | 5.3<br><sub>-,-,-,0,0</sub> |  | 2.5<br><sub>-,-,-,0,0</sub> |  | 1.4<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 9.2 |
| Larry Nance Jr. (IND) | 97% | 13.2<br><sub>14,5,14,7,9</sub> | 4.2<br><sub>4,5,2,4,3</sub> |  | 2.4<br><sub>0,0,2,2,1</sub> |  | 0.8<br><sub>0,0,1,2,0</sub> |  | 0.5<br><sub>0,1,0,1,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.5 |

</details>


### TOR @ DET
Out: Jalen Duren (DET), Ronald Holland II (DET), Taurean Prince (DET), Duncan Robinson (DET), RJ Barrett (TOR), Kawhi Leonard (TOR), Collin Murray-Boyles (TOR)

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 37.1<br><sub>-,-,36,34,-</sub> | 24.1<br><sub>-,-,30,20,-</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>-,-,9,4,-</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>-,-,4,2,-</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>-,-,4,1,-</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.7 | 1.5 | 3.5 | 38.3 |
| Immanuel Quickley | 91% | 34.8<br><sub>28,28,38,34,34</sub> | 19.0<br><sub>11,26,17,14,24</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>4,4,6,1,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>4,6,6,7,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>1,3,3,2,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.1 | 1.9 | 29.0 |
| Ja'Kobe Walter | 99% | 34.6<br><sub>35,32,36,33,38</sub> | 13.3<br><sub>17,6,7,25,18</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>3,5,2,1,7</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>1,0,1,2,6</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>5,1,1,7,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6 | 0.3 | 1.3 | 19.4 |
| Jamal Shead | 99% | 27.4<br><sub>22,22,26,20,24</sub> | 9.9<br><sub>3,5,19,7,15</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>3,1,2,0,1</sub> |  | 6.1<br><sub>6,5,4,6,6</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>0,1,3,1,1</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.1 | 0.2 | 2.1 | 18.0 |
| Jamison Battle | 98% | 27.2<br><sub>25,25,8,7,33</sub> | 10.8<br><sub>12,13,0,0,19</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,1,3,1,5</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>0,1,0,0,0</sub> |  | 1.9<br><sub>2,3,0,0,5</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.5 | 0.2 | 1.0 | 15.2 |
| Jakob Poeltl | 93% | 26.7<br><sub>32,25,17,18,29</sub> | 10.2<br><sub>6,9,11,3,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>9,5,5,6,9</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,3,1,1,5</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.0 | 1.6 | 19.8 |
| Allen Graves | 98% | 25.1<br><sub>18,13,16,13,31</sub> | 7.8<br><sub>13,0,2,3,9</sub> |  | 4.2<br><sub>5,2,5,2,4</sub> |  | 1.3<br><sub>0,0,3,1,0</sub> |  | 0.9<br><sub>3,0,0,1,1</sub> |  | 0.8 | 0.6 | 0.9 | 13.3 |
| Alijah Martin | 96% | 16.6<br><sub>16,18,12,8,17</sub> | 5.9<br><sub>12,7,2,0,2</sub> |  | 2.4<br><sub>1,4,3,2,2</sub> |  | 1.0<br><sub>0,1,0,0,0</sub> |  | 0.7<br><sub>4,1,0,0,0</sub> |  | 0.7 | 0.2 | 1.0 | 9.2 |
| Trayce Jackson-Davis | 58% | 16.4<br><sub>-,-,-,-,17</sub> | 5.8<br><sub>-,-,-,-,3</sub> |  | 5.2<br><sub>-,-,-,-,7</sub> |  | 1.0<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.9 | 0.9 | 12.0 |
| Kyle Anderson | 63% | 13.9<br><sub>11,5,-,-,4</sub> | 3.8<br><sub>2,0,-,-,0</sub> |  | 2.5<br><sub>3,0,-,-,0</sub> |  | 2.2<br><sub>4,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.6 | 0.5 | 0.8 | 8.5 |
| Malachi Smith | 96% | 12.4<br><sub>-,2,-,-,8</sub> | 4.0<br><sub>-,0,-,-,0</sub> |  | 2.0<br><sub>-,0,-,-,1</sub> |  | 1.4<br><sub>-,0,-,-,3</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 7.4 |

</details>

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 70% | 36.2<br><sub>27,48,36,38,-</sub> | 25.6<br><sub>17,52,33,27,-</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>3,5,5,5,-</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 8.7<br><sub>7,11,8,6,-</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>0,3,3,1,-</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.8 | 4.2 | 39.5 |
| Daniss Jenkins | 98% | 34.3<br><sub>36,42,35,38,36</sub> | 16.6<br><sub>22,21,10,25,17</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>6,6,1,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.7<br><sub>8,0,5,5,9</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>2,3,1,3,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.3 | 2.4 | 26.4 |
| Kevin Huerter | 98% | 32.2<br><sub>33,24,38,36,36</sub> | 13.2<br><sub>12,11,20,9,11</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,1,4,7,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.5<br><sub>3,0,7,1,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>0,1,2,0,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2 | 0.8 | 1.7 | 20.5 |
| Ausar Thompson | 98% | 30.4<br><sub>28,43,18,29,34</sub> | 11.3<br><sub>8,17,10,14,10</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 8.0<br><sub>5,11,8,9,7</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 5.0<br><sub>4,11,5,12,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 1.8 | 1.1 | 2.3 | 24.3 |
| John Collins | 98% | 29.9<br><sub>28,25,26,23,30</sub> | 13.9<br><sub>24,10,8,11,20</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>10,4,7,1,7</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>3,0,0,0,2</sub> |  | 1.3<br><sub>2,2,2,1,4</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.9 | 1.6 | 21.1 |
| Paul Reed | 98% | 27.3<br><sub>21,38,23,25,20</sub> | 14.1<br><sub>4,13,9,10,17</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 8.3<br><sub>10,11,9,6,7</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>2,3,1,5,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.2 | 1.3 | 1.9 | 24.6 |
| Javonte Green | 98% | 24.6<br><sub>11,15,12,23,35</sub> | 8.7<br><sub>7,5,5,6,18</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>1,1,1,6,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.7<br><sub>0,0,0,0,0</sub> |  | 1.3<br><sub>0,1,0,0,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.5 | 0.6 | 13.1 |
| Isaiah Joe | 93% | 15.3<br><sub>-,-,-,-,16</sub> | 7.8<br><sub>-,-,-,-,11</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 1.0<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,3</sub> |  | 0.5 | 0.1 | 0.7 | 10.6 |
| Chaz Lanier | 66% | 13.3<br><sub>2,-,-,25,16</sub> | 4.6<br><sub>0,-,-,3,9</sub> |  | 1.1<br><sub>0,-,-,3,1</sub> |  | 0.7<br><sub>0,-,-,1,0</sub> |  | 0.7<br><sub>0,-,-,1,3</sub> |  | 0.3 | 0.1 | 0.2 | 6.4 |
| Elijah Harkless | 63% | 11.3<br><sub>-,-,2,4,14</sub> | 3.5<br><sub>-,-,2,0,6</sub> |  | 1.6<br><sub>-,-,0,1,2</sub> |  | 1.2<br><sub>-,-,0,1,4</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 6.3 |
| Tolu Smith | 58% | 8.7<br><sub>-,-,1,-,3</sub> | 3.5<br><sub>-,-,3,-,3</sub> |  | 2.8<br><sub>-,-,2,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.4 | 0.5 | 6.7 |
| Isaac Jones | 48% | 6.7<br><sub>2,-,2,-,-</sub> | 7.9<br><sub>0,-,0,-,-</sub> |  | 1.6<br><sub>0,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 9.7 |

</details>


### WAS @ CHI
Out: Tobe Awaka (CHI), Orlando Robinson (CHI), Caleb Wilson (CHI), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.8–122.9 | WAS 31% | 3.27 / 1.44 | CHI -7.5 | 238.5 | CHI -2.5 covers 64%; o239.5 48% |
| Expected (weighted by chance each plays) | 115.9–122.8 | WAS 31% | 3.19 / 1.46 | CHI -7.5 | 238.5 | CHI -2.5 covers 63%; o239.5 48% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Questionable | 55% | 5.8 | 2.3 | 1.7 | 0.4 | 0.1 | 0.2 | 0.2 | 0.3 | 4.3 | small |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 34.7<br><sub>34,44,30,32,38</sub> | 16.7<br><sub>13,5,16,21,23</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>4,8,7,5,12</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,4,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>0,1,2,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 2.0 | 26.1 |
| Anthony Davis | 98% | 34.5<br><sub>34,44,31,35,34</sub> | 23.3<br><sub>21,30,14,23,25</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 11.4<br><sub>13,15,8,4,14</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>0,4,5,0,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.6<br><sub>0,0,0,0,2</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 1.2 | 1.7 | 2.1 | 37.6 |
| Trae Young | 99% | 34.4<br><sub>34,45,26,33,32</sub> | 18.5<br><sub>15,37,0,13,11</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>3,2,1,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 9.5<br><sub>4,14,8,12,8</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>3,4,0,2,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.2 | 3.1 | 31.0 |
| Kyshawn George | 99% | 34.0<br><sub>39,26,30,38,40</sub> | 17.2<br><sub>25,14,11,18,20</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>9,1,2,6,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>3,5,4,1,4</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>5,3,1,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 1.1 | 2.2 | 26.6 |
| Alex Sarr | 98% | 27.4<br><sub>25,44,27,31,22</sub> | 13.5<br><sub>5,30,25,6,13</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>8,9,9,4,2</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>0,2,2,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,4,3,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 1.7 | 1.5 | 23.0 |
| Bilal Coulibaly | 99% | 22.7<br><sub>25,29,21,16,26</sub> | 7.9<br><sub>5,4,9,11,3</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,7,2,5,8</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>2,0,0,0,2</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.8 | 1.0 | 13.2 |
| Tre Johnson | 96% | 17.4<br><sub>29,30,-,21,8</sub> | 7.1<br><sub>15,13,-,9,0</sub> |  | 1.8<br><sub>3,4,-,1,2</sub> |  | 0.9<br><sub>1,2,-,3,0</sub> |  | 0.9<br><sub>2,1,-,2,0</sub> |  | 0.6 | 0.2 | 0.7 | 9.8 |
| Khris Middleton | 58% | 14.2<br><sub>-,-,9,18,20</sub> | 5.1<br><sub>-,-,8,9,8</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>-,-,0,3,4</sub> |  | 1.3<br><sub>-,-,2,3,1</sub> |  | 0.5<br><sub>-,-,2,2,1</sub> |  | 0.5 | 0.1 | 0.9 | 8.7 |
| Deandre Ayton | 99% | 11.7<br><sub>9,9,10,8,9</sub> | 3.9<br><sub>2,2,2,4,0</sub> |  | 3.8<br><sub>2,4,1,0,3</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 8.2 |
| Will Riley | 88% | 10.2<br><sub>-,3,16,2,10</sub> | 4.7<br><sub>-,3,14,2,0</sub> |  | 1.4<br><sub>-,0,3,1,3</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.4<br><sub>-,1,2,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.9 |
| Bub Carrington | 76% | 9.9<br><sub>10,16,23,2,-</sub> | 3.1<br><sub>0,2,11,0,-</sub> |  | 1.1<br><sub>0,0,0,0,-</sub> |  | 1.4<br><sub>0,2,4,0,-</sub> |  | 0.3<br><sub>0,0,3,0,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.6 |
| Anthony Gill | 52% | 6.9<br><sub>-,-,6,2,-</sub> | 2.6<br><sub>-,-,5,2,-</sub> |  | 1.2<br><sub>-,-,1,0,-</sub> |  | 0.5<br><sub>-,-,0,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Tre Mann | 52% | 5.8<br><sub>-,-,11,2,-</sub> | 2.7<br><sub>-,-,4,2,-</sub> |  | 0.8<br><sub>-,-,1,0,-</sub> |  | 0.8<br><sub>-,-,1,1,-</sub> |  | 0.2<br><sub>-,-,1,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.3 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell | 98% | 29.8<br><sub>-,31,30,33,26</sub> | 22.1<br><sub>-,33,24,27,17</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>-,5,5,2,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.6<br><sub>-,2,3,6,5</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>-,4,3,0,5</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.2 | 2.0 | 28.1 |
| Matas Buzelis | 98% | 28.6<br><sub>31,29,30,31,30</sub> | 17.6<br><sub>13,11,18,23,25</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>3,6,9,3,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,2,2,0,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.3<br><sub>3,3,2,3,5</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 1.2 | 2.3 | 25.8 |
| Josh Giddey | 98% | 28.4<br><sub>25,39,26,24,28</sub> | 13.5<br><sub>9,15,8,4,18</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>2,10,8,4,14</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 8.8<br><sub>7,14,5,8,9</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>1,3,2,1,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.6 | 2.7 | 29.5 |
| Isaac Okoro | 98% | 26.2<br><sub>23,41,31,32,25</sub> | 9.5<br><sub>0,15,9,13,12</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>2,3,7,6,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>4,2,4,2,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>0,2,0,3,4</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.4 | 0.8 | 14.6 |
| Jalen Smith | 98% | 26.2<br><sub>30,32,-,28,21</sub> | 14.1<br><sub>23,15,-,17,14</sub> | 15.5 · –<br><sub>o 46% · u 54%</sub> | 9.2<br><sub>4,12,-,11,6</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>3,3,-,3,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.8<br><sub>5,1,-,3,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 1.1 | 1.1 | 25.2 |
| Patrick Williams | 88% | 19.6<br><sub>28,24,26,13,13</sub> | 7.1<br><sub>9,13,14,0,2</sub> |  | 3.1<br><sub>7,4,5,0,1</sub> |  | 1.6<br><sub>4,2,1,0,2</sub> |  | 0.9<br><sub>0,4,2,0,0</sub> |  | 0.8 | 0.4 | 0.9 | 11.8 |
| Tre Jones | 98% | 19.5<br><sub>28,15,24,23,16</sub> | 11.3<br><sub>13,4,16,16,10</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,0,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,3,4,6,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.5<br><sub>1,0,1,0,0</sub> |  | 1.0 | 0.2 | 1.1 | 17.9 |
| Nic Claxton | 98% | 18.9<br><sub>16,22,-,17,22</sub> | 8.3<br><sub>17,2,-,8,14</sub> | 10.5 · –<br><sub>o 43% · u 57%</sub> | 5.6<br><sub>6,6,-,2,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>1,2,-,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.6 | 0.9 | 0.9 | 16.0 |
| Buddy Hield | 84% | 16.6<br><sub>-,25,20,19,19</sub> | 8.2<br><sub>-,12,16,6,11</sub> |  | 2.4<br><sub>-,3,4,4,1</sub> |  | 1.6<br><sub>-,3,2,2,2</sub> |  | 1.4<br><sub>-,2,4,2,3</sub> |  | 0.7 | 0.2 | 0.8 | 12.2 |
| Zach Collins | 66% | 12.6<br><sub>3,-,28,-,11</sub> | 5.6<br><sub>2,-,8,-,3</sub> |  | 4.0<br><sub>2,-,5,-,2</sub> |  | 1.3<br><sub>1,-,4,-,0</sub> |  | 0.3<br><sub>0,-,0,-,1</sub> |  | 0.4 | 0.3 | 0.7 | 10.9 |
| Leonard Miller | 80% | 12.2<br><sub>2,-,17,1,7</sub> | 6.2<br><sub>0,-,4,0,4</sub> |  | 3.2<br><sub>0,-,3,0,2</sub> |  | 0.8<br><sub>0,-,4,0,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.4 | 0.6 | 10.2 |
| Noa Essengue | 91% | 12.1<br><sub>11,8,7,14,15</sub> | 5.1<br><sub>8,5,0,1,5</sub> |  | 2.9<br><sub>4,1,1,2,3</sub> |  | 0.7<br><sub>3,1,0,1,0</sub> |  | 0.4<br><sub>1,1,0,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.6 |
| Jordan Hawkins | 63% | 7.9<br><sub>24,-,-,4,-</sub> | 3.5<br><sub>7,-,-,0,-</sub> |  | 1.1<br><sub>4,-,-,0,-</sub> |  | 0.6<br><sub>2,-,-,1,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 5.2 |

</details>


### NOP @ OKC
Out: Chet Holmgren (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Bennedict Mathurin (NOP), Bryce McGowens (NOP), Dejounte Murray (NOP), Trendon Watford (NOP)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.0–119.2 | NOP 17% | 5.81 / 1.21 | OKC -13.5 | 225.5 | OKC -11.5 covers 54%; o228.5 43% |
| Expected (weighted by chance each plays) | 106.2–119.3 | NOP 17% | 5.76 / 1.21 | OKC -13.5 | 225.5 | OKC -11.5 covers 55%; o228.5 44% |
| if Trey Murphy III plays | 107.3–118.8 | NOP 20% | 4.88 / 1.26 | OKC -11.5 | 225.5 | OKC -11.5 covers 50%; o228.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alex Caruso (OKC) | Questionable | 55% | 17.3 | 7.5 | 2.5 | 2.3 | 1.0 | 1.1 | 0.4 | 0.8 | 12.4 | small |
| Trey Murphy III (NOP) | Questionable | 55% | 30.8 | 15.5 | 4.7 | 3.4 | 2.5 | 1.0 | 0.4 | 1.8 | 23.6 | full tables below |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 35.4<br><sub>29,35,41,33,42</sub> | 18.3<br><sub>15,30,16,23,10</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>1,10,6,6,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 3.1<br><sub>2,0,4,3,6</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.6<br><sub>3,6,2,5,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.2 | 1.5 | 27.1 |
| Zion Williamson | 98% | 32.8<br><sub>30,33,31,25,32</sub> | 18.9<br><sub>29,22,24,16,24</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>4,5,6,6,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>2,4,2,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>1,0,2,0,0</sub> |  | 1.1 | 0.6 | 2.4 | 28.4 |
| Jeremiah Fears | 99% | 31.5<br><sub>28,34,33,29,31</sub> | 15.6<br><sub>14,18,13,19,16</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>4,5,4,10,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.6<br><sub>5,7,7,10,4</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 1.5<br><sub>2,0,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.5 | 2.9 | 25.9 |
| Herbert Jones | 98% | 28.4<br><sub>25,32,27,24,32</sub> | 9.5<br><sub>2,8,10,8,9</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>2,2,2,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>3,3,1,3,3</sub> |  | 1.3<br><sub>0,0,2,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.5 | 1.4 | 15.0 |
| Jordan Poole | 86% | 26.5<br><sub>21,21,24,31,30</sub> | 12.2<br><sub>14,13,14,11,22</sub> |  | 2.5<br><sub>0,2,2,2,1</sub> |  | 3.8<br><sub>1,5,5,5,5</sub> |  | 2.0<br><sub>2,1,1,1,3</sub> |  | 0.7 | 0.4 | 2.0 | 18.5 |
| Derik Queen | 99% | 24.2<br><sub>14,23,25,21,19</sub> | 12.0<br><sub>9,10,10,17,9</sub> |  | 6.8<br><sub>0,6,5,10,5</sub> |  | 2.8<br><sub>0,2,4,0,0</sub> |  | 0.7<br><sub>1,0,2,4,0</sub> |  | 0.9 | 0.8 | 2.5 | 21.7 |
| Yves Missi | 98% | 20.9<br><sub>-,-,22,23,17</sub> | 6.1<br><sub>-,-,3,6,4</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 6.4<br><sub>-,-,8,14,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>-,-,1,1,2</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 1.3 | 1.0 | 13.9 |
| Karlo Matkovic | 98% | 19.6<br><sub>22,19,14,20,10</sub> | 7.2<br><sub>4,1,5,3,0</sub> |  | 4.3<br><sub>4,3,3,2,2</sub> |  | 1.1<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.8 | 0.9 | 12.6 |
| Jaron Pierre Jr. | 89% | 17.9<br><sub>7,4,23,19,17</sub> | 7.5<br><sub>4,0,13,10,7</sub> |  | 2.3<br><sub>4,0,2,4,1</sub> |  | 0.8<br><sub>0,0,0,0,1</sub> |  | 1.0<br><sub>1,0,2,2,1</sub> |  | 0.5 | 0.2 | 1.1 | 10.6 |
| DeAndre Jordan | 52% | 13.6<br><sub>11,17,-,-,10</sub> | 3.9<br><sub>0,6,-,-,8</sub> |  | 4.9<br><sub>3,8,-,-,2</sub> |  | 0.8<br><sub>0,1,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.5 | 0.7 | 9.6 |
| AJ Johnson | 52% | 8.4<br><sub>7,4,-,6,-</sub> | 3.1<br><sub>2,1,-,0,-</sub> |  | 1.2<br><sub>1,0,-,0,-</sub> |  | 0.7<br><sub>0,0,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.0 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 99% | 33.5<br><sub>29,36,39,30,36</sub> | 31.9<br><sub>26,31,40,37,34</sub> | 32.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>8,4,4,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 6.4<br><sub>3,2,5,2,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>0,0,2,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.8 | 2.7 | 42.1 |
| Ajay Mitchell | 98% | 29.2<br><sub>28,-,-,27,34</sub> | 17.6<br><sub>14,-,-,14,13</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,-,-,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>3,-,-,5,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.1<br><sub>0,-,-,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.4 | 0.4 | 1.8 | 25.8 |
| Jared McCain | 98% | 29.0<br><sub>31,31,31,30,33</sub> | 16.4<br><sub>21,10,23,12,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>3,6,4,1,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>3,3,2,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.8<br><sub>4,2,7,1,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 1.6 | 21.9 |
| Isaiah Hartenstein | 99% | 25.4<br><sub>24,34,30,18,27</sub> | 10.3<br><sub>7,20,21,3,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 11.1<br><sub>9,11,16,11,17</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>5,6,6,2,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.4 | 25.6 |
| Aday Mara | 98% | 24.1<br><sub>26,32,21,26,27</sub> | 10.5<br><sub>10,11,10,16,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 7.4<br><sub>10,6,3,13,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,2,0,3,8</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.9 | 1.6 | 20.3 |
| Kenrich Williams | 98% | 23.0<br><sub>19,26,35,19,23</sub> | 9.5<br><sub>3,11,8,10,10</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,2,8,1,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>0,2,4,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>1,2,0,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.2 | 0.9 | 16.0 |
| Bennett Stirtz | 98% | 18.7<br><sub>18,25,12,17,17</sub> | 6.7<br><sub>13,6,5,0,6</sub> |  | 1.4<br><sub>1,1,1,1,0</sub> |  | 1.5<br><sub>1,1,0,2,2</sub> |  | 1.1<br><sub>2,2,1,0,2</sub> |  | 0.7 | 0.2 | 0.7 | 9.6 |
| Jaylin Williams | 98% | 18.2<br><sub>-,-,-,-,16</sub> | 5.8<br><sub>-,-,-,-,3</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>-,-,-,-,1</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.5 | 0.7 | 12.4 |
| Nique Clifford | 96% | 15.3<br><sub>20,16,12,24,13</sub> | 5.8<br><sub>4,5,0,9,7</sub> |  | 2.1<br><sub>4,3,0,3,0</sub> |  | 1.4<br><sub>1,1,0,0,0</sub> |  | 0.5<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.8 | 9.3 |
| Micah Peavy | 91% | 14.1<br><sub>21,12,-,13,-</sub> | 4.2<br><sub>0,0,-,5,-</sub> |  | 2.5<br><sub>2,3,-,3,-</sub> |  | 0.5<br><sub>0,0,-,1,-</sub> |  | 0.4<br><sub>0,0,-,1,-</sub> |  | 0.5 | 0.2 | 0.4 | 7.2 |
| Josh Dix | 67% | 13.6<br><sub>-,-,17,-,-</sub> | 4.9<br><sub>-,-,0,-,-</sub> |  | 1.5<br><sub>-,-,4,-,-</sub> |  | 0.8<br><sub>-,-,3,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.4 | 7.3 |
| Brooks Barnhizer | 52% | 7.3<br><sub>5,-,-,4,-</sub> | 1.8<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>1,-,-,0,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>if Trey Murphy III plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey (NOP) | 98% | 32.1<br><sub>29,35,41,33,42</sub> | 16.1<br><sub>15,30,16,23,10</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>1,10,6,6,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>2,0,4,3,6</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.3<br><sub>3,6,2,5,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9 | 0.2 | 1.4 | 23.8 |
| Trey Murphy III (NOP) | 100% | 30.8<br><sub>-,-,-,-,-</sub> | 15.5<br><sub>-,-,-,-,-</sub> | 13.5 · – | 4.7<br><sub>-,-,-,-,-</sub> | 3.5 | 3.4<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> | 1.5 | 1.0 | 0.4 | 1.8 | 23.6 |
| Zion Williamson (NOP) | 98% | 30.7<br><sub>30,33,31,25,32</sub> | 17.6<br><sub>29,22,24,16,24</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 5.4<br><sub>4,5,6,6,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>2,4,2,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>1,0,2,0,0</sub> |  | 1.1 | 0.6 | 2.3 | 26.2 |
| Jeremiah Fears (NOP) | 99% | 30.0<br><sub>28,34,33,29,31</sub> | 14.7<br><sub>14,18,13,19,16</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>4,5,4,10,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.4<br><sub>5,7,7,10,4</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>2,0,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.4 | 2.8 | 24.5 |
| Herbert Jones (NOP) | 98% | 25.3<br><sub>25,32,27,24,32</sub> | 8.2<br><sub>2,8,10,8,9</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>2,2,2,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>3,3,1,3,3</sub> |  | 1.2<br><sub>0,0,2,2,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.4 | 1.3 | 13.1 |
| Jordan Poole (NOP) | 86% | 23.8<br><sub>21,21,24,31,30</sub> | 10.8<br><sub>14,13,14,11,22</sub> |  | 2.2<br><sub>0,2,2,2,1</sub> |  | 3.5<br><sub>1,5,5,5,5</sub> |  | 1.7<br><sub>2,1,1,1,3</sub> |  | 0.7 | 0.4 | 1.8 | 16.6 |
| Derik Queen (NOP) | 99% | 21.5<br><sub>14,23,25,21,19</sub> | 10.4<br><sub>9,10,10,17,9</sub> |  | 6.0<br><sub>0,6,5,10,5</sub> |  | 2.5<br><sub>0,2,4,0,0</sub> |  | 0.6<br><sub>1,0,2,4,0</sub> |  | 0.8 | 0.8 | 2.3 | 18.9 |
| Yves Missi (NOP) | 98% | 18.7<br><sub>-,-,22,23,17</sub> | 5.4<br><sub>-,-,3,6,4</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 5.7<br><sub>-,-,8,14,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>-,-,1,1,2</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 1.2 | 1.0 | 12.4 |
| Karlo Matkovic (NOP) | 98% | 15.3<br><sub>22,19,14,20,10</sub> | 5.5<br><sub>4,1,5,3,0</sub> |  | 3.3<br><sub>4,3,3,2,2</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.6 | 0.8 | 9.6 |
| Jaron Pierre Jr. (NOP) | 89% | 14.8<br><sub>7,4,23,19,17</sub> | 6.0<br><sub>4,0,13,10,7</sub> |  | 1.9<br><sub>4,0,2,4,1</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>1,0,2,2,1</sub> |  | 0.5 | 0.2 | 0.9 | 8.5 |
| DeAndre Jordan (NOP) | 52% | 11.7<br><sub>11,17,-,-,10</sub> | 3.2<br><sub>0,6,-,-,8</sub> |  | 4.2<br><sub>3,8,-,-,2</sub> |  | 0.7<br><sub>0,1,-,-,1</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.4 | 0.7 | 8.1 |
| AJ Johnson (NOP) | 52% | 6.4<br><sub>7,4,-,6,-</sub> | 2.4<br><sub>2,1,-,0,-</sub> |  | 0.9<br><sub>1,0,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.1<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.9 |
| Shai Gilgeous-Alexander (OKC) | 99% | 33.5<br><sub>29,36,39,30,36</sub> | 31.9<br><sub>26,31,40,37,34</sub> | 32.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>8,4,4,2,5</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 6.4<br><sub>3,2,5,2,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>0,0,2,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.8 | 2.7 | 42.2 |
| Ajay Mitchell (OKC) | 98% | 29.2<br><sub>28,-,-,27,34</sub> | 17.6<br><sub>14,-,-,14,13</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,-,-,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>3,-,-,5,6</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.1<br><sub>0,-,-,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.4 | 0.3 | 1.8 | 25.8 |
| Jared McCain (OKC) | 98% | 28.9<br><sub>31,31,31,30,33</sub> | 16.5<br><sub>21,10,23,12,18</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>3,6,4,1,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,3,2,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.8<br><sub>4,2,7,1,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 1.6 | 21.9 |
| Isaiah Hartenstein (OKC) | 99% | 25.4<br><sub>24,34,30,18,27</sub> | 10.3<br><sub>7,20,21,3,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 11.1<br><sub>9,11,16,11,17</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>5,6,6,2,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.8 | 1.4 | 25.6 |
| Aday Mara (OKC) | 98% | 24.1<br><sub>26,32,21,26,27</sub> | 10.5<br><sub>10,11,10,16,10</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 7.4<br><sub>10,6,3,13,6</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,2,0,3,8</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.9 | 1.6 | 20.3 |
| Kenrich Williams (OKC) | 98% | 23.1<br><sub>19,26,35,19,23</sub> | 9.4<br><sub>3,11,8,10,10</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,2,8,1,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>0,2,4,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>1,2,0,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.2 | 0.9 | 16.0 |
| Bennett Stirtz (OKC) | 98% | 18.7<br><sub>18,25,12,17,17</sub> | 6.8<br><sub>13,6,5,0,6</sub> |  | 1.4<br><sub>1,1,1,1,0</sub> |  | 1.5<br><sub>1,1,0,2,2</sub> |  | 1.1<br><sub>2,2,1,0,2</sub> |  | 0.7 | 0.2 | 0.7 | 9.7 |
| Jaylin Williams (OKC) | 98% | 18.2<br><sub>-,-,-,-,16</sub> | 5.7<br><sub>-,-,-,-,3</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>-,-,-,-,1</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.5 | 0.7 | 12.3 |
| Nique Clifford (OKC) | 96% | 15.4<br><sub>20,16,12,24,13</sub> | 5.8<br><sub>4,5,0,9,7</sub> |  | 2.1<br><sub>4,3,0,3,0</sub> |  | 1.4<br><sub>1,1,0,0,0</sub> |  | 0.5<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.8 | 9.3 |
| Micah Peavy (OKC) | 91% | 14.1<br><sub>21,12,-,13,-</sub> | 4.2<br><sub>0,0,-,5,-</sub> |  | 2.5<br><sub>2,3,-,3,-</sub> |  | 0.6<br><sub>0,0,-,1,-</sub> |  | 0.4<br><sub>0,0,-,1,-</sub> |  | 0.5 | 0.2 | 0.4 | 7.3 |
| Josh Dix (OKC) | 67% | 13.5<br><sub>-,-,17,-,-</sub> | 4.9<br><sub>-,-,0,-,-</sub> |  | 1.5<br><sub>-,-,4,-,-</sub> |  | 0.8<br><sub>-,-,3,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.4 | 7.2 |
| Brooks Barnhizer (OKC) | 52% | 7.3<br><sub>5,-,-,4,-</sub> | 1.9<br><sub>0,-,-,0,-</sub> |  | 1.6<br><sub>1,-,-,0,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |

</details>


### PHX @ UTA
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA), Mark Williams (PHX)

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.7<br><sub>29,35,28,37,33</sub> | 27.3<br><sub>17,30,17,20,29</sub> | 27.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,1,4,4,2</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>5,7,7,8,6</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.1<br><sub>2,4,0,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.3 | 2.6 | 37.1 |
| Dillon Brooks | 98% | 29.5<br><sub>22,30,22,27,31</sub> | 16.8<br><sub>8,15,1,15,29</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>4,3,2,4,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,1,0,4,5</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>0,3,0,3,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 1.4 | 22.6 |
| Miles Bridges | 98% | 28.4<br><sub>18,25,24,29,29</sub> | 14.3<br><sub>8,11,14,16,13</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>4,6,3,8,6</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>2,3,3,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>2,0,2,2,1</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.6 | 1.1 | 23.4 |
| Jalen Green | 98% | 27.3<br><sub>21,21,21,27,30</sub> | 16.3<br><sub>13,12,9,16,18</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,4,2,5,7</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>1,0,1,3,7</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>3,1,1,2,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.3 | 2.1 | 23.2 |
| Oso Ighodaro | 98% | 23.1<br><sub>20,32,17,33,21</sub> | 6.4<br><sub>6,2,4,8,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>8,3,2,11,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.9<br><sub>2,7,3,3,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.8 | 1.2 | 14.9 |
| Collin Gillespie | 98% | 22.9<br><sub>22,27,28,26,17</sub> | 9.2<br><sub>12,13,26,10,9</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,2,4,3,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 3.6<br><sub>8,1,4,3,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>4,3,5,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.1 | 1.1 | 15.6 |
| Jordan Goodwin | 98% | 19.4<br><sub>14,24,31,20,17</sub> | 7.6<br><sub>18,6,14,11,2</sub> |  | 4.2<br><sub>3,5,7,6,5</sub> |  | 2.1<br><sub>1,2,6,2,3</sub> |  | 1.2<br><sub>6,2,1,1,0</sub> |  | 1.3 | 0.2 | 0.8 | 13.8 |
| Luke Kennard | 98% | 17.5<br><sub>22,21,23,17,17</sub> | 7.2<br><sub>14,8,18,12,3</sub> |  | 2.1<br><sub>1,1,6,2,3</sub> |  | 1.7<br><sub>3,1,4,0,1</sub> |  | 1.0<br><sub>3,0,3,4,1</sub> |  | 0.5 | 0.1 | 0.6 | 10.9 |
| Khaman Maluach | 98% | 16.9<br><sub>22,16,13,11,21</sub> | 6.3<br><sub>11,4,7,4,10</sub> |  | 5.1<br><sub>7,2,4,6,2</sub> |  | 0.7<br><sub>3,1,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.0 | 0.9 | 12.1 |
| Ryan Dunn | 98% | 15.6<br><sub>25,10,24,12,13</sub> | 4.4<br><sub>10,0,3,5,6</sub> |  | 3.6<br><sub>8,4,6,1,5</sub> |  | 1.1<br><sub>2,0,1,0,2</sub> |  | 0.5<br><sub>1,0,1,1,0</sub> |  | 0.7 | 0.4 | 0.5 | 9.1 |
| Rasheer Fleming | 52% | 7.8<br><sub>12,-,-,-,4</sub> | 3.0<br><sub>4,-,-,-,0</sub> |  | 1.4<br><sub>2,-,-,-,1</sub> |  | 0.3<br><sub>0,-,-,-,1</sub> |  | 0.3<br><sub>1,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |
| Koa Peat | 72% | 7.0<br><sub>6,-,8,1,4</sub> | 3.4<br><sub>5,-,10,0,2</sub> |  | 1.6<br><sub>1,-,2,1,0</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 5.3 |
| Pat Spencer | 52% | 6.9<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.9 |
| Jamaree Bouyea | 52% | 6.8<br><sub>8,-,-,-,4</sub> | 3.0<br><sub>7,-,-,-,0</sub> |  | 0.9<br><sub>1,-,-,-,1</sub> |  | 1.1<br><sub>3,-,-,-,1</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.0 |
| Duop Reath | 48% | 6.4<br><sub>-,-,-,-,-</sub> | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.4 |
| Drew Timme | 8% | 6.3 | 2.6 |  | 1.2 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.4 | 4.3 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 99% | 34.9<br><sub>33,38,34,35,39</sub> | 23.9<br><sub>13,27,13,30,30</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>7,4,4,2,1</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 7.0<br><sub>7,7,8,11,10</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>2,4,1,4,5</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 3.6 | 34.9 |
| Ace Bailey | 99% | 31.5<br><sub>31,35,30,23,27</sub> | 15.7<br><sub>18,21,7,5,19</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>7,3,8,1,8</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,1,4,4,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>3,3,1,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.9 | 1.9 | 23.3 |
| Darryn Peterson | 98% | 31.0<br><sub>33,34,34,31,19</sub> | 17.4<br><sub>22,28,17,13,11</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>4,7,5,5,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>5,2,4,2,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,4,3,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.6 | 2.3 | 25.3 |
| Jaxson Hayes | 84% | 24.6<br><sub>30,13,-,-,25</sub> | 9.6<br><sub>11,12,-,-,6</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>8,5,-,-,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,1,-,-,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.8 | 1.1 | 1.2 | 17.1 |
| Svi Mykhailiuk | 98% | 23.5<br><sub>20,7,21,33,34</sub> | 8.9<br><sub>3,0,6,8,15</sub> |  | 2.5<br><sub>0,1,2,7,3</sub> |  | 2.0<br><sub>2,0,3,5,5</sub> |  | 1.6<br><sub>1,0,2,2,4</sub> |  | 0.7 | 0.1 | 1.1 | 13.5 |
| Mo Bamba | 91% | 23.2<br><sub>18,20,36,31,23</sub> | 9.1<br><sub>5,9,26,15,6</sub> |  | 8.2<br><sub>1,9,5,10,16</sub> |  | 1.1<br><sub>1,1,4,3,0</sub> |  | 0.6<br><sub>0,0,6,1,0</sub> |  | 0.5 | 1.7 | 1.1 | 18.4 |
| Josh Green | 96% | 22.6<br><sub>26,14,15,13,28</sub> | 5.2<br><sub>3,2,6,9,11</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,0,1,1,2</sub> |  | 1.2<br><sub>1,0,1,0,2</sub> |  | 0.7<br><sub>1,0,2,1,2</sub> |  | 0.8 | 0.2 | 0.8 | 8.6 |
| Brice Sensabaugh | 99% | 21.4<br><sub>23,27,30,35,14</sub> | 13.3<br><sub>19,7,14,40,8</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>3,3,7,11,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>1,1,2,5,2</sub> |  | 1.8<br><sub>3,1,0,8,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.6 | 0.2 | 1.9 | 18.6 |
| Josh Okogie | 98% | 20.1<br><sub>15,22,27,22,15</sub> | 5.7<br><sub>7,7,7,9,3</sub> |  | 3.0<br><sub>3,2,6,2,0</sub> |  | 1.2<br><sub>0,1,0,4,0</sub> |  | 0.6<br><sub>1,2,2,1,0</sub> |  | 1.0 | 0.3 | 0.8 | 9.8 |
| Isaiah Collier | 67% | 15.8<br><sub>12,16,-,-,10</sub> | 7.8<br><sub>7,3,-,-,0</sub> |  | 2.2<br><sub>3,2,-,-,1</sub> |  | 3.9<br><sub>2,5,-,-,2</sub> |  | 0.4<br><sub>1,1,-,-,0</sub> |  | 0.6 | 0.2 | 1.5 | 13.9 |
| Kyle Filipowski | 58% | 12.0<br><sub>-,2,-,-,6</sub> | 6.2<br><sub>-,2,-,-,0</sub> |  | 3.6<br><sub>-,0,-,-,3</sub> |  | 1.2<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.9 | 11.1 |
| Tony Bradley | 63% | 10.9<br><sub>-,12,12,17,-</sub> | 3.6<br><sub>-,0,6,3,-</sub> |  | 3.4<br><sub>-,5,2,7,-</sub> |  | 0.5<br><sub>-,1,0,1,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.2 | 0.3 | 0.6 | 7.6 |

</details>


### HOU @ DEN
Out: Bryce Hopkins (DEN), Julian Strawther (DEN), Cam Whitmore (DEN), Clint Capela (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.3–115.7 | HOU 37% | 2.68 / 1.60 | DEN -4.5 | 226.5 | DEN -1.5 covers 60%; o225.5 53% |
| Expected (weighted by chance each plays) | 112.2–114.9 | HOU 42% | 2.36 / 1.74 | DEN -3.5 | 227.5 | DEN -1.5 covers 55%; o225.5 54% |
| if Alperen Sengun plays | 112.8–114.6 | HOU 45% | 2.24 / 1.81 | DEN -2.5 | 227.5 | DEN -1.5 covers 52%; o225.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alperen Sengun (HOU) | Questionable | 55% | 33.7 | 18.7 | 9.4 | 6.3 | 0.7 | 1.1 | 0.8 | 2.5 | 34.4 | full tables below |
| Steven Adams (HOU) | Questionable | 55% | 19.6 | 5.5 | 6.8 | 1.4 | 0.0 | 0.6 | 0.6 | 1.0 | 13.7 | small |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 84% | 36.7<br><sub>29,41,29,-,31</sub> | 17.9<br><sub>19,12,26,-,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>7,10,7,-,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 4.5<br><sub>4,3,7,-,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.4<br><sub>0,0,3,-,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 1.4 | 0.7 | 2.1 | 30.2 |
| Kevin Durant | 99% | 36.6<br><sub>34,33,30,29,32</sub> | 24.4<br><sub>20,22,25,22,21</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,3,4,2,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 5.3<br><sub>5,6,5,3,3</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>1,2,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.8 | 3.0 | 35.5 |
| Jabari Smith Jr. | 99% | 36.0<br><sub>35,24,28,32,26</sub> | 17.5<br><sub>14,6,9,12,17</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>8,3,6,10,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,0,5,1,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>2,1,1,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.8 | 1.2 | 27.1 |
| Fred VanVleet | 84% | 34.0<br><sub>30,34,-,26,27</sub> | 15.1<br><sub>18,17,-,8,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>2,2,-,5,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 5.6<br><sub>6,3,-,6,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>4,3,-,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.3 | 0.4 | 1.3 | 24.2 |
| Tari Eason | 99% | 29.7<br><sub>22,33,30,27,25</sub> | 13.2<br><sub>6,14,25,7,11</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>3,11,7,7,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>0,2,1,3,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.6<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.6 | 1.4 | 22.1 |
| Reed Sheppard | 91% | 27.0<br><sub>20,19,26,19,25</sub> | 12.2<br><sub>13,0,11,5,20</sub> |  | 2.5<br><sub>1,0,1,2,4</sub> |  | 3.5<br><sub>1,3,6,2,2</sub> |  | 2.2<br><sub>3,0,3,1,6</sub> |  | 1.3 | 0.6 | 1.1 | 18.2 |
| Marcus Smart | 58% | 23.9<br><sub>17,-,-,-,18</sub> | 8.3<br><sub>6,-,-,-,4</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>2,-,-,-,2</sub> |  | 2.6<br><sub>1,-,-,-,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>2,-,-,-,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.2 | 0.3 | 1.3 | 13.7 |
| Bogdan Bogdanovic | 98% | 18.3<br><sub>10,12,22,26,11</sub> | 7.0<br><sub>0,11,12,6,1</sub> |  | 2.2<br><sub>0,1,3,0,3</sub> |  | 1.6<br><sub>0,3,4,1,0</sub> |  | 1.0<br><sub>0,3,2,2,0</sub> |  | 0.5 | 0.1 | 0.7 | 10.8 |
| Oscar Tshiebwe | 96% | 14.8<br><sub>1,6,12,6,11</sub> | 5.8<br><sub>0,0,4,6,4</sub> |  | 6.2<br><sub>0,5,9,6,4</sub> |  | 1.1<br><sub>0,0,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 13.2 |
| Isaiah Crawford | 72% | 11.4<br><sub>1,-,9,21,2</sub> | 3.9<br><sub>0,-,4,11,0</sub> |  | 2.4<br><sub>0,-,2,10,0</sub> |  | 0.6<br><sub>0,-,0,3,0</sub> |  | 0.4<br><sub>0,-,0,1,0</sub> |  | 0.3 | 0.2 | 0.4 | 6.8 |
| Jae'Sean Tate | 67% | 10.9<br><sub>1,-,8,12,1</sub> | 3.3<br><sub>0,-,4,3,0</sub> |  | 2.5<br><sub>0,-,2,3,0</sub> |  | 0.7<br><sub>0,-,0,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 6.5 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.5<br><sub>39,37,37,38,39</sub> | 26.1<br><sub>25,27,26,28,24</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 11.8<br><sub>16,11,8,15,8</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 9.8<br><sub>9,8,10,7,9</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.5 | 47.7 |
| Jamal Murray | 98% | 37.1<br><sub>39,32,38,35,38</sub> | 25.4<br><sub>38,30,23,28,21</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>2,4,7,4,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 6.1<br><sub>2,8,9,4,2</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>5,4,0,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.6 | 2.4 | 35.9 |
| Christian Braun | 98% | 33.6<br><sub>32,37,28,33,35</sub> | 12.7<br><sub>4,12,17,10,15</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>5,5,7,3,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>3,4,1,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3<br><sub>0,2,1,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.4 | 1.1 | 19.2 |
| Aaron Gordon | 98% | 30.4<br><sub>30,27,33,24,31</sub> | 12.9<br><sub>3,9,11,11,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>5,3,5,1,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.4 | 1.2 | 20.4 |
| Cameron Johnson | 98% | 30.0<br><sub>31,30,31,27,26</sub> | 12.3<br><sub>8,23,12,9,8</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>2,4,5,0,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,3,2,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,4,1,0,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.3 | 1.0 | 18.0 |
| DeMar DeRozan | 91% | 22.7<br><sub>19,20,24,14,25</sub> | 11.3<br><sub>7,8,9,2,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>4,1,3,1,2</sub> |  | 2.7<br><sub>2,4,2,1,2</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 0.7 | 0.3 | 1.0 | 16.0 |
| Spencer Jones | 88% | 16.0<br><sub>14,22,12,21,17</sub> | 3.9<br><sub>0,3,4,4,2</sub> |  | 2.1<br><sub>0,1,2,3,2</sub> |  | 0.8<br><sub>1,0,1,3,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 6.8 |
| Trevon Brazile | 98% | 15.3<br><sub>14,13,16,23,11</sub> | 4.3<br><sub>5,7,5,9,0</sub> |  | 3.5<br><sub>2,5,3,4,6</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.3 |
| Marvin Bagley III | 98% | 12.5<br><sub>12,12,13,10,9</sub> | 5.8<br><sub>6,4,7,4,4</sub> |  | 3.5<br><sub>3,2,7,2,3</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 9.9 |
| Tyus Jones | 98% | 9.8<br><sub>6,11,10,10,9</sub> | 2.6<br><sub>2,0,2,0,0</sub> |  | 0.8<br><sub>0,1,0,1,0</sub> |  | 1.6<br><sub>0,4,3,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 5.1 |
| Zeke Nnaji | 23% | 6.8<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.8 |
| Alpha Diallo | 38% | 6.4<br><sub>1,-,-,-,-</sub> | 2.6<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Ryan Nembhard | 52% | 5.8<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.9 |

</details>

<details><summary>if Alperen Sengun plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic (DEN) | 98% | 37.6<br><sub>39,37,37,38,39</sub> | 26.0<br><sub>25,27,26,28,24</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 11.8<br><sub>16,11,8,15,8</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 9.8<br><sub>9,8,10,7,9</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.9 | 3.5 | 47.6 |
| Jamal Murray (DEN) | 98% | 37.1<br><sub>39,32,38,35,38</sub> | 25.2<br><sub>38,30,23,28,21</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>2,4,7,4,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 6.1<br><sub>2,8,9,4,2</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>5,4,0,1,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.6 | 2.4 | 35.8 |
| Christian Braun (DEN) | 98% | 33.6<br><sub>32,37,28,33,35</sub> | 12.7<br><sub>4,12,17,10,15</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>5,5,7,3,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>3,4,1,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.3<br><sub>0,2,1,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.4 | 1.1 | 19.2 |
| Aaron Gordon (DEN) | 98% | 30.5<br><sub>30,27,33,24,31</sub> | 12.7<br><sub>3,9,11,11,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>5,3,5,1,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>2,2,1,1,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.4 | 1.2 | 20.3 |
| Cameron Johnson (DEN) | 98% | 30.0<br><sub>31,30,31,27,26</sub> | 12.2<br><sub>8,23,12,9,8</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>2,4,5,0,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,3,2,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,4,1,0,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.4 | 1.0 | 17.9 |
| DeMar DeRozan (DEN) | 91% | 22.6<br><sub>19,20,24,14,25</sub> | 11.3<br><sub>7,8,9,2,18</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>4,1,3,1,2</sub> |  | 2.7<br><sub>2,4,2,1,2</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 0.7 | 0.3 | 1.1 | 16.0 |
| Spencer Jones (DEN) | 88% | 16.0<br><sub>14,22,12,21,17</sub> | 3.9<br><sub>0,3,4,4,2</sub> |  | 2.1<br><sub>0,1,2,3,2</sub> |  | 0.8<br><sub>1,0,1,3,0</sub> |  | 0.3<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 6.8 |
| Trevon Brazile (DEN) | 98% | 15.4<br><sub>14,13,16,23,11</sub> | 4.3<br><sub>5,7,5,9,0</sub> |  | 3.5<br><sub>2,5,3,4,6</sub> |  | 0.5<br><sub>0,0,0,0,0</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.6 | 8.3 |
| Marvin Bagley III (DEN) | 98% | 12.5<br><sub>12,12,13,10,9</sub> | 5.7<br><sub>6,4,7,4,4</sub> |  | 3.5<br><sub>3,2,7,2,3</sub> |  | 0.6<br><sub>0,1,0,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 9.8 |
| Tyus Jones (DEN) | 98% | 9.8<br><sub>6,11,10,10,9</sub> | 2.6<br><sub>2,0,2,0,0</sub> |  | 0.9<br><sub>0,1,0,1,0</sub> |  | 1.6<br><sub>0,4,3,2,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 5.1 |
| Zeke Nnaji (DEN) | 23% | 6.8<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.8 |
| Alpha Diallo (DEN) | 38% | 6.5<br><sub>1,-,-,-,-</sub> | 2.6<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |
| Ryan Nembhard (DEN) | 52% | 5.8<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.9 |
| Kevin Durant (HOU) | 99% | 35.9<br><sub>34,33,30,29,32</sub> | 22.1<br><sub>20,22,25,22,21</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>4,3,4,2,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.5<br><sub>5,6,5,3,3</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>1,2,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.8 | 2.8 | 32.1 |
| Amen Thompson (HOU) | 84% | 35.8<br><sub>29,41,29,-,31</sub> | 16.1<br><sub>19,12,26,-,15</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>7,10,7,-,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 4.2<br><sub>4,3,7,-,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>0,0,3,-,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 1.4 | 0.7 | 1.8 | 27.9 |
| Jabari Smith Jr. (HOU) | 99% | 35.0<br><sub>35,24,28,32,26</sub> | 14.9<br><sub>14,6,9,12,17</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>8,3,6,10,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>0,0,5,1,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>2,1,1,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.8 | 1.0 | 23.7 |
| Alperen Sengun (HOU) | 100% | 33.7<br><sub>37,37,28,30,14</sub> | 18.7<br><sub>19,43,19,23,7</sub> | 20.5 · – | 9.4<br><sub>13,12,8,7,7</sub> | 8.5 | 6.3<br><sub>9,5,8,2,1</sub> | 6.5 | 0.7<br><sub>1,1,1,1,1</sub> | 0.5 | 1.1 | 0.8 | 2.5 | 34.4 |
| Fred VanVleet (HOU) | 84% | 32.5<br><sub>30,34,-,26,27</sub> | 12.9<br><sub>18,17,-,8,15</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>2,2,-,5,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 5.0<br><sub>6,3,-,6,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>4,3,-,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.4 | 1.1 | 21.2 |
| Tari Eason (HOU) | 99% | 26.3<br><sub>22,33,30,27,25</sub> | 10.8<br><sub>6,14,25,7,11</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>3,11,7,7,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,2,1,3,3</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3<br><sub>0,2,3,0,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.6 | 1.1 | 18.4 |
| Reed Sheppard (HOU) | 91% | 22.8<br><sub>20,19,26,19,25</sub> | 9.7<br><sub>13,0,11,5,20</sub> |  | 2.0<br><sub>1,0,1,2,4</sub> |  | 2.6<br><sub>1,3,6,2,2</sub> |  | 1.7<br><sub>3,0,3,1,6</sub> |  | 1.1 | 0.5 | 0.9 | 14.3 |
| Marcus Smart (HOU) | 58% | 20.2<br><sub>17,-,-,-,18</sub> | 6.8<br><sub>6,-,-,-,4</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,-,-,-,2</sub> |  | 2.0<br><sub>1,-,-,-,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9<br><sub>2,-,-,-,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.3 | 1.0 | 11.0 |
| Bogdan Bogdanovic (HOU) | 98% | 14.1<br><sub>10,12,22,26,11</sub> | 5.0<br><sub>0,11,12,6,1</sub> |  | 1.6<br><sub>0,1,3,0,3</sub> |  | 1.1<br><sub>0,3,4,1,0</sub> |  | 0.7<br><sub>0,3,2,2,0</sub> |  | 0.4 | 0.1 | 0.5 | 7.7 |
| Oscar Tshiebwe (HOU) | 96% | 11.4<br><sub>1,6,12,6,11</sub> | 4.4<br><sub>0,0,4,6,4</sub> |  | 4.7<br><sub>0,5,9,6,4</sub> |  | 0.8<br><sub>0,0,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 9.9 |
| Isaiah Crawford (HOU) | 72% | 8.4<br><sub>1,-,9,21,2</sub> | 2.8<br><sub>0,-,4,11,0</sub> |  | 1.8<br><sub>0,-,2,10,0</sub> |  | 0.4<br><sub>0,-,0,3,0</sub> |  | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.2 | 0.2 | 0.3 | 5.0 |
| Jae'Sean Tate (HOU) | 67% | 7.2<br><sub>1,-,8,12,1</sub> | 2.3<br><sub>0,-,4,3,0</sub> |  | 1.6<br><sub>0,-,2,3,0</sub> |  | 0.5<br><sub>0,-,0,2,1</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |

</details>


### SAC @ LAL
Out: Austin Reaves (LAL), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 105.7–122.7 | SAC 11% | 8.76 / 1.13 | LAL -17.5 | 228.5 | LAL -14.5 covers 57%; o229.5 48% |
| Expected (weighted by chance each plays) | 106.1–122.1 | SAC 13% | 7.66 / 1.15 | LAL -15.5 | 228.5 | LAL -14.5 covers 54%; o229.5 47% |
| if Precious Achiuwa plays | 106.4–121.9 | SAC 14% | 7.22 / 1.16 | LAL -15.5 | 228.5 | LAL -14.5 covers 53%; o229.5 47% |
| if De'Andre Hunter plays | 106.3–121.9 | SAC 14% | 7.28 / 1.16 | LAL -15.5 | 228.5 | LAL -14.5 covers 53%; o229.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa (SAC) | Doubtful | 20% | 24.3 | 9.6 | 6.2 | 1.2 | 0.4 | 1.0 | 0.7 | 1.2 | 17.0 | full tables below |
| De'Andre Hunter (SAC) | Questionable | 55% | 33.6 | 14.6 | 4.5 | 2.0 | 1.9 | 0.9 | 0.2 | 1.9 | 21.0 | full tables below |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 37.8<br><sub>39,40,35,33,35</sub> | 26.2<br><sub>32,29,17,26,36</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>5,4,4,0,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.4<br><sub>10,6,6,6,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>3,4,3,3,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.4 | 4.7 | 37.1 |
| Zach LaVine | 84% | 33.9<br><sub>25,33,36,-,32</sub> | 21.1<br><sub>15,31,12,-,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>4,3,3,-,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.2<br><sub>2,2,6,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>1,6,3,-,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 2.9 | 27.5 |
| Domantas Sabonis | 98% | 33.2<br><sub>-,24,35,29,24</sub> | 15.1<br><sub>-,0,21,11,8</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 12.0<br><sub>-,2,12,13,13</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>-,5,5,3,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.4<br><sub>-,0,1,0,0</sub> |  | 0.8 | 0.2 | 2.7 | 32.4 |
| Keegan Murray | 98% | 32.7<br><sub>23,24,40,21,31</sub> | 12.9<br><sub>10,11,16,6,12</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>1,2,7,1,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,1,4,0,3</sub> |  | 1.6<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.9 | 1.3 | 19.3 |
| Leaky Black | 88% | 24.8<br><sub>20,18,12,29,17</sub> | 6.0<br><sub>6,0,0,12,3</sub> |  | 3.8<br><sub>5,3,0,9,0</sub> |  | 1.6<br><sub>1,2,0,2,2</sub> |  | 0.9<br><sub>2,0,0,4,1</sub> |  | 1.2 | 0.5 | 0.9 | 11.4 |
| Malik Monk | 98% | 22.4<br><sub>21,3,18,29,20</sub> | 11.7<br><sub>9,1,7,14,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>2,0,4,1,1</sub> |  | 4.2<br><sub>3,0,3,10,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>0,0,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.7 | 0.3 | 2.0 | 18.0 |
| Dylan Cardwell | 98% | 18.7<br><sub>18,29,13,19,12</sub> | 5.7<br><sub>4,1,6,10,6</sub> |  | 6.7<br><sub>9,11,3,6,4</sub> |  | 1.4<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.0 | 1.0 | 13.8 |
| Emanuel Sharp | 98% | 18.2<br><sub>12,19,7,21,14</sub> | 5.9<br><sub>5,2,4,9,6</sub> |  | 1.5<br><sub>1,2,0,0,2</sub> |  | 1.0<br><sub>0,0,0,2,1</sub> |  | 0.8<br><sub>1,0,0,1,1</sub> |  | 0.8 | 0.2 | 0.8 | 8.4 |
| Alex Karaban | 58% | 16.3<br><sub>-,-,-,29,4</sub> | 3.4<br><sub>-,-,-,0,0</sub> |  | 2.3<br><sub>-,-,-,5,1</sub> |  | 0.7<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 6.3 |
| Daeqwon Plowden | 88% | 14.8<br><sub>12,2,2,24,4</sub> | 5.7<br><sub>6,0,0,13,3</sub> |  | 1.6<br><sub>0,0,0,2,0</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.9<br><sub>2,0,0,3,1</sub> |  | 0.4 | 0.1 | 0.6 | 8.0 |
| Mason Plumlee | 63% | 9.7<br><sub>-,-,-,5,4</sub> | 2.4<br><sub>-,-,-,2,0</sub> |  | 3.1<br><sub>-,-,-,0,2</sub> |  | 0.8<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.4 | 0.6 | 6.4 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 35.3<br><sub>39,32,36,42,37</sub> | 39.4<br><sub>32,32,43,36,29</sub> | 36.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>8,5,3,6,5</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 8.2<br><sub>10,5,9,7,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>3,5,5,5,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.6 | 4.2 | 54.2 |
| Quentin Grimes | 98% | 30.4<br><sub>-,-,37,42,35</sub> | 14.1<br><sub>-,-,22,47,20</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>-,-,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>-,-,1,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>-,-,5,10,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.3 | 1.4 | 20.6 |
| Walker Kessler | 98% | 29.0<br><sub>30,29,32,-,31</sub> | 12.5<br><sub>21,10,14,-,10</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 11.5<br><sub>10,11,12,-,11</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>4,3,3,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 1.0 | 2.1 | 1.6 | 25.8 |
| Jake LaRavia | 98% | 25.4<br><sub>32,21,32,23,30</sub> | 7.0<br><sub>4,0,12,4,4</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,9,3,5,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,6,3,2,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.7 | 1.2 | 13.2 |
| Matisse Thybulle | 98% | 23.2<br><sub>23,23,26,31,21</sub> | 7.1<br><sub>6,8,12,7,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>0,5,8,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,1,0,0,3</sub> |  | 1.1<br><sub>2,2,2,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 2.5 | 0.8 | 1.0 | 10.9 |
| Sandro Mamukelashvili | 99% | 21.5<br><sub>32,26,21,23,21</sub> | 9.7<br><sub>23,23,4,3,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>8,3,2,3,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,2,3,2,0</sub> |  | 1.3<br><sub>5,5,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 0.8 | 15.6 |
| Collin Sexton | 99% | 21.3<br><sub>27,13,24,25,20</sub> | 13.8<br><sub>18,10,16,10,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,1,0,4,0</sub> |  | 2.9<br><sub>6,3,3,3,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.2 | 1.6 | 18.7 |
| Ziaire Williams | 98% | 20.2<br><sub>28,20,19,24,18</sub> | 8.4<br><sub>12,9,6,0,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>2,1,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>2,5,3,1,0</sub> |  | 1.1<br><sub>2,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.2 | 0.2 | 0.8 | 11.8 |
| Jarred Vanderbilt | 88% | 13.0<br><sub>13,9,12,14,12</sub> | 2.9<br><sub>4,4,2,4,0</sub> |  | 3.7<br><sub>2,3,4,7,5</sub> |  | 1.1<br><sub>0,1,0,0,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.3 | 0.6 | 7.7 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 47% | 8.7<br><sub>-,4,-,17,-</sub> | 2.0<br><sub>-,0,-,4,-</sub> |  | 2.9<br><sub>-,2,-,8,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.3 | 5.6 |
| AK Okereke | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Adou Thiero | 80% | 8.2<br><sub>7,14,-,6,6</sub> | 2.6<br><sub>2,2,-,0,0</sub> |  | 1.9<br><sub>2,2,-,0,1</sub> |  | 0.7<br><sub>1,1,-,1,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |
| Carson Cooper | 58% | 7.7<br><sub>-,-,-,18,2</sub> | 2.3<br><sub>-,-,-,3,2</sub> |  | 2.3<br><sub>-,-,-,4,1</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 5.2 |
| Jaden Hardy | 52% | 6.8<br><sub>-,4,-,-,2</sub> | 3.7<br><sub>-,3,-,-,0</sub> |  | 0.6<br><sub>-,1,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,1</sub> |  | 0.4<br><sub>-,1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Cameron Carr | 67% | 6.5<br><sub>7,13,-,-,2</sub> | 2.5<br><sub>2,0,-,-,5</sub> |  | 1.1<br><sub>3,2,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,1</sub> |  | 0.2<br><sub>0,0,-,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Bronny James | 52% | 5.7<br><sub>-,4,-,-,2</sub> | 2.0<br><sub>-,4,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 2.6 |
| Chris Manon | 52% | 5.6<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.0 |

</details>

<details><summary>if De'Andre Hunter plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 35.3<br><sub>39,32,36,42,37</sub> | 39.3<br><sub>32,32,43,36,29</sub> | 36.5 · –<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>8,5,3,6,5</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 8.1<br><sub>10,5,9,7,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>3,5,5,5,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.5 | 4.2 | 54.1 |
| Quentin Grimes (LAL) | 98% | 30.4<br><sub>-,-,37,42,35</sub> | 14.0<br><sub>-,-,22,47,20</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>-,-,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>-,-,1,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>-,-,5,10,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.3 | 1.4 | 20.6 |
| Walker Kessler (LAL) | 98% | 29.0<br><sub>30,29,32,-,31</sub> | 12.4<br><sub>21,10,14,-,10</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 11.4<br><sub>10,11,12,-,11</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>4,3,3,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.9 | 2.0 | 1.6 | 25.6 |
| Jake LaRavia (LAL) | 98% | 25.3<br><sub>32,21,32,23,30</sub> | 7.0<br><sub>4,0,12,4,4</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,9,3,5,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,6,3,2,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.7 | 1.2 | 13.1 |
| Matisse Thybulle (LAL) | 98% | 23.1<br><sub>23,23,26,31,21</sub> | 7.0<br><sub>6,8,12,7,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>0,5,8,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,1,0,0,3</sub> |  | 1.1<br><sub>2,2,2,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 2.5 | 0.8 | 0.9 | 10.8 |
| Sandro Mamukelashvili (LAL) | 99% | 21.5<br><sub>32,26,21,23,21</sub> | 9.7<br><sub>23,23,4,3,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>8,3,2,3,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,2,3,2,0</sub> |  | 1.2<br><sub>5,5,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 0.8 | 15.6 |
| Collin Sexton (LAL) | 99% | 21.3<br><sub>27,13,24,25,20</sub> | 13.7<br><sub>18,10,16,10,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,1,0,4,0</sub> |  | 2.9<br><sub>6,3,3,3,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.2 | 1.6 | 18.7 |
| Ziaire Williams (LAL) | 98% | 20.1<br><sub>28,20,19,24,18</sub> | 8.3<br><sub>12,9,6,0,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>2,1,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>2,5,3,1,0</sub> |  | 1.1<br><sub>2,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.2 | 0.2 | 0.8 | 11.8 |
| Jarred Vanderbilt (LAL) | 88% | 13.0<br><sub>13,9,12,14,12</sub> | 2.9<br><sub>4,4,2,4,0</sub> |  | 3.7<br><sub>2,3,4,7,5</sub> |  | 1.1<br><sub>0,1,0,0,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.3 | 0.6 | 7.7 |
| Arthur Kaluma (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney (LAL) | 47% | 8.7<br><sub>-,4,-,17,-</sub> | 2.0<br><sub>-,0,-,4,-</sub> |  | 3.0<br><sub>-,2,-,8,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.3 | 5.6 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Adou Thiero (LAL) | 80% | 8.1<br><sub>7,14,-,6,6</sub> | 2.6<br><sub>2,2,-,0,0</sub> |  | 1.9<br><sub>2,2,-,0,1</sub> |  | 0.7<br><sub>1,1,-,1,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |
| Carson Cooper (LAL) | 58% | 7.9<br><sub>-,-,-,18,2</sub> | 2.3<br><sub>-,-,-,3,2</sub> |  | 2.3<br><sub>-,-,-,4,1</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 5.2 |
| Jaden Hardy (LAL) | 52% | 6.9<br><sub>-,4,-,-,2</sub> | 3.8<br><sub>-,3,-,-,0</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,1</sub> |  | 0.4<br><sub>-,1,-,-,0</sub> |  | 0.2 | 0.0 | 0.4 | 5.0 |
| Cameron Carr (LAL) | 67% | 6.5<br><sub>7,13,-,-,2</sub> | 2.5<br><sub>2,0,-,-,5</sub> |  | 1.0<br><sub>3,2,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,1</sub> |  | 0.2<br><sub>0,0,-,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Bronny James (LAL) | 52% | 5.7<br><sub>-,4,-,-,2</sub> | 2.0<br><sub>-,4,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 2.6 |
| Chris Manon (LAL) | 52% | 5.5<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.2 | 3.0 |
| Darius Acuff Jr. (SAC) | 98% | 36.4<br><sub>39,40,35,33,35</sub> | 24.2<br><sub>32,29,17,26,36</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>5,4,4,0,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.2<br><sub>10,6,6,6,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>3,4,3,3,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 4.2 | 34.9 |
| De'Andre Hunter (SAC) | 100% | 33.6<br><sub>31,34,42,-,35</sub> | 14.6<br><sub>14,15,24,-,7</sub> | 13.5 · – | 4.5<br><sub>3,4,5,-,1</sub> | 3.5 | 2.0<br><sub>1,2,2,-,4</sub> |  | 1.9<br><sub>2,3,2,-,1</sub> | 1.5 | 0.9 | 0.2 | 1.9 | 21.0 |
| Zach LaVine (SAC) | 84% | 32.3<br><sub>25,33,36,-,32</sub> | 18.9<br><sub>15,31,12,-,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>4,3,3,-,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>2,2,6,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>1,6,3,-,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 2.6 | 24.9 |
| Domantas Sabonis (SAC) | 98% | 31.2<br><sub>-,24,35,29,24</sub> | 13.3<br><sub>-,0,21,11,8</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 11.1<br><sub>-,2,12,13,13</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>-,5,5,3,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.8 | 0.2 | 2.5 | 29.3 |
| Keegan Murray (SAC) | 98% | 29.7<br><sub>23,24,40,21,31</sub> | 11.3<br><sub>10,11,16,6,12</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>1,2,7,1,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>2,1,4,0,3</sub> |  | 1.4<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.8 | 1.1 | 17.2 |
| Leaky Black (SAC) | 88% | 20.0<br><sub>20,18,12,29,17</sub> | 4.8<br><sub>6,0,0,12,3</sub> |  | 3.1<br><sub>5,3,0,9,0</sub> |  | 1.2<br><sub>1,2,0,2,2</sub> |  | 0.7<br><sub>2,0,0,4,1</sub> |  | 1.0 | 0.4 | 0.7 | 9.2 |
| Malik Monk (SAC) | 98% | 19.2<br><sub>21,3,18,29,20</sub> | 9.9<br><sub>9,1,7,14,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>2,0,4,1,1</sub> |  | 3.6<br><sub>3,0,3,10,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.3<br><sub>0,0,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.2 | 1.7 | 15.2 |
| Emanuel Sharp (SAC) | 98% | 15.6<br><sub>12,19,7,21,14</sub> | 4.8<br><sub>5,2,4,9,6</sub> |  | 1.2<br><sub>1,2,0,0,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.7 | 0.2 | 0.7 | 6.8 |
| Dylan Cardwell (SAC) | 98% | 15.5<br><sub>18,29,13,19,12</sub> | 4.7<br><sub>4,1,6,10,6</sub> |  | 5.5<br><sub>9,11,3,6,4</sub> |  | 1.1<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.8 | 11.3 |
| Alex Karaban (SAC) | 58% | 11.6<br><sub>-,-,-,29,4</sub> | 2.2<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,5,1</sub> |  | 0.4<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 4.3 |
| Daeqwon Plowden (SAC) | 88% | 11.5<br><sub>12,2,2,24,4</sub> | 4.3<br><sub>6,0,0,13,3</sub> |  | 1.2<br><sub>0,0,0,2,0</sub> |  | 0.5<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>2,0,0,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Mason Plumlee (SAC) | 63% | 7.1<br><sub>-,-,-,5,4</sub> | 1.8<br><sub>-,-,-,2,0</sub> |  | 2.4<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>if Precious Achiuwa plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 35.3<br><sub>39,32,36,42,37</sub> | 39.2<br><sub>32,32,43,36,29</sub> | 36.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>8,5,3,6,5</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 8.1<br><sub>10,5,9,7,7</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 5.0<br><sub>3,5,5,5,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.6 | 4.1 | 54.0 |
| Quentin Grimes (LAL) | 98% | 30.4<br><sub>-,-,37,42,35</sub> | 13.9<br><sub>-,-,22,47,20</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>-,-,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>-,-,1,3,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>-,-,5,10,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.3 | 1.4 | 20.6 |
| Walker Kessler (LAL) | 98% | 28.9<br><sub>30,29,32,-,31</sub> | 12.4<br><sub>21,10,14,-,10</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 11.4<br><sub>10,11,12,-,11</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>4,3,3,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 1.0 | 2.0 | 1.6 | 25.6 |
| Jake LaRavia (LAL) | 98% | 25.3<br><sub>32,21,32,23,30</sub> | 6.9<br><sub>4,0,12,4,4</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,9,3,5,6</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>3,6,3,2,2</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.7 | 1.2 | 13.1 |
| Matisse Thybulle (LAL) | 98% | 23.1<br><sub>23,23,26,31,21</sub> | 7.1<br><sub>6,8,12,7,2</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>0,5,8,6,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,1,0,0,3</sub> |  | 1.1<br><sub>2,2,2,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 2.5 | 0.8 | 0.9 | 10.9 |
| Sandro Mamukelashvili (LAL) | 99% | 21.5<br><sub>32,26,21,23,21</sub> | 9.8<br><sub>23,23,4,3,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>8,3,2,3,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>3,2,3,2,0</sub> |  | 1.3<br><sub>5,5,0,0,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.4 | 0.8 | 15.7 |
| Collin Sexton (LAL) | 99% | 21.3<br><sub>27,13,24,25,20</sub> | 13.8<br><sub>18,10,16,10,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,1,0,4,0</sub> |  | 2.9<br><sub>6,3,3,3,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>3,0,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 1.6 | 18.7 |
| Ziaire Williams (LAL) | 98% | 20.1<br><sub>28,20,19,24,18</sub> | 8.3<br><sub>12,9,6,0,7</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>2,1,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>2,5,3,1,0</sub> |  | 1.1<br><sub>2,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.2 | 0.2 | 0.8 | 11.7 |
| Jarred Vanderbilt (LAL) | 88% | 13.0<br><sub>13,9,12,14,12</sub> | 2.8<br><sub>4,4,2,4,0</sub> |  | 3.7<br><sub>2,3,4,7,5</sub> |  | 1.2<br><sub>0,1,0,0,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.3 | 0.6 | 7.7 |
| Arthur Kaluma (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Kevon Looney (LAL) | 47% | 8.7<br><sub>-,4,-,17,-</sub> | 2.0<br><sub>-,0,-,4,-</sub> |  | 3.0<br><sub>-,2,-,8,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.3 | 5.7 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Adou Thiero (LAL) | 80% | 8.1<br><sub>7,14,-,6,6</sub> | 2.6<br><sub>2,2,-,0,0</sub> |  | 1.9<br><sub>2,2,-,0,1</sub> |  | 0.7<br><sub>1,1,-,1,1</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.2 |
| Carson Cooper (LAL) | 58% | 7.9<br><sub>-,-,-,18,2</sub> | 2.3<br><sub>-,-,-,3,2</sub> |  | 2.3<br><sub>-,-,-,4,1</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 5.2 |
| Jaden Hardy (LAL) | 52% | 6.9<br><sub>-,4,-,-,2</sub> | 3.7<br><sub>-,3,-,-,0</sub> |  | 0.6<br><sub>-,1,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,1</sub> |  | 0.4<br><sub>-,1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Cameron Carr (LAL) | 67% | 6.5<br><sub>7,13,-,-,2</sub> | 2.5<br><sub>2,0,-,-,5</sub> |  | 1.1<br><sub>3,2,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,1</sub> |  | 0.2<br><sub>0,0,-,-,1</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Bronny James (LAL) | 52% | 5.7<br><sub>-,4,-,-,2</sub> | 2.1<br><sub>-,4,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 2.6 |
| Chris Manon (LAL) | 52% | 5.5<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.0 |
| Darius Acuff Jr. (SAC) | 98% | 37.1<br><sub>39,40,35,33,35</sub> | 24.9<br><sub>32,29,17,26,36</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>5,4,4,0,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.4<br><sub>10,6,6,6,6</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>3,4,3,3,6</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.3 | 4.3 | 35.9 |
| Zach LaVine (SAC) | 84% | 33.2<br><sub>25,33,36,-,32</sub> | 19.6<br><sub>15,31,12,-,18</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>4,3,3,-,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>2,2,6,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>1,6,3,-,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.3 | 2.8 | 25.9 |
| Domantas Sabonis (SAC) | 98% | 32.3<br><sub>-,24,35,29,24</sub> | 13.9<br><sub>-,0,21,11,8</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 11.6<br><sub>-,2,12,13,13</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>-,5,5,3,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 0.4<br><sub>-,0,1,0,0</sub> |  | 0.8 | 0.2 | 2.8 | 30.7 |
| Keegan Murray (SAC) | 98% | 30.7<br><sub>23,24,40,21,31</sub> | 11.7<br><sub>10,11,16,6,12</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>1,2,7,1,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>2,1,4,0,3</sub> |  | 1.4<br><sub>0,2,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.8 | 1.2 | 17.7 |
| Precious Achiuwa (SAC) | 100% | 24.3<br><sub>36,14,-,-,8</sub> | 9.6<br><sub>7,10,-,-,0</sub> |  | 6.2<br><sub>14,3,-,-,0</sub> |  | 1.2<br><sub>2,0,-,-,0</sub> |  | 0.4<br><sub>0,1,-,-,0</sub> |  | 1.0 | 0.7 | 1.2 | 17.0 |
| Leaky Black (SAC) | 88% | 21.0<br><sub>20,18,12,29,17</sub> | 5.0<br><sub>6,0,0,12,3</sub> |  | 3.2<br><sub>5,3,0,9,0</sub> |  | 1.3<br><sub>1,2,0,2,2</sub> |  | 0.7<br><sub>2,0,0,4,1</sub> |  | 1.0 | 0.4 | 0.7 | 9.5 |
| Malik Monk (SAC) | 98% | 20.2<br><sub>21,3,18,29,20</sub> | 10.6<br><sub>9,1,7,14,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,0,4,1,1</sub> |  | 3.9<br><sub>3,0,3,10,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>0,0,0,1,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.3 | 1.7 | 16.3 |
| Emanuel Sharp (SAC) | 98% | 16.4<br><sub>12,19,7,21,14</sub> | 5.2<br><sub>5,2,4,9,6</sub> |  | 1.3<br><sub>1,2,0,0,2</sub> |  | 0.9<br><sub>0,0,0,2,1</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.7 | 0.2 | 0.7 | 7.4 |
| Dylan Cardwell (SAC) | 98% | 16.3<br><sub>18,29,13,19,12</sub> | 5.0<br><sub>4,1,6,10,6</sub> |  | 5.7<br><sub>9,11,3,6,4</sub> |  | 1.2<br><sub>3,1,3,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.9 | 0.8 | 11.9 |
| Alex Karaban (SAC) | 58% | 13.0<br><sub>-,-,-,29,4</sub> | 2.4<br><sub>-,-,-,0,0</sub> |  | 1.8<br><sub>-,-,-,5,1</sub> |  | 0.5<br><sub>-,-,-,1,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 4.7 |
| Daeqwon Plowden (SAC) | 88% | 12.5<br><sub>12,2,2,24,4</sub> | 4.8<br><sub>6,0,0,13,3</sub> |  | 1.3<br><sub>0,0,0,2,0</sub> |  | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.7<br><sub>2,0,0,3,1</sub> |  | 0.3 | 0.1 | 0.5 | 6.7 |
| Mason Plumlee (SAC) | 63% | 7.6<br><sub>-,-,-,5,4</sub> | 1.9<br><sub>-,-,-,2,0</sub> |  | 2.5<br><sub>-,-,-,0,2</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 5.0 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-20/`._
