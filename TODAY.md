# NBA model · Wed 18 Nov 2026 (US date)

Updated **Thu 19 Nov, 07:40 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-18/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| DET @ NOP | player minutes | Javonte Green projected 29 min; most in his last 10 games is 23 | minutes 29 vs 17 this season; teammates out: Duren, II, Robinson (~66 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jarrett Allen BLK over 3.5 (4+) | MEM @ CLE | draftkings | 14.20 | 13.26 | 7.80 | 12.8% | 6.6% | 7.5% | +7.1% | +82.1% | 0.1% |
| MIL to win | MIL @ MIA | sportsbet | 6.80 | 6.41 | 6.12 | 16.4% | 15.6% | 15.6% | +6.2% | +11.2% | 0.3% |
| Devin Booker AST over 9.5 (10+) | PHX @ SAC | draftkings | 14.80 | 13.99 | 8.50 | 11.8% | 6.3% | 7.1% | +5.9% | +74.2% | 0.1% |
| Nikola Jokic AST over 15.5 (16+) | BOS @ DEN | draftkings | 19.80 | 18.73 | 11.47 | 8.7% | 4.7% | 5.3% | +5.6% | +72.6% | 0.1% |
| Donovan Mitchell PR over 49.5 (50+) | MEM @ CLE | draftkings | 21.00 | 19.92 | 12.31 | 8.1% | 4.5% | 5.0% | +5.3% | +70.6% | 0.1% |
| Donovan Mitchell PR over 44.5 (45+) | MEM @ CLE | draftkings | 11.40 | 10.85 | 6.73 | 14.9% | 8.2% | 9.2% | +5.2% | +69.4% | 0.1% |
| James Harden PTS over 29.5 (30+) | MEM @ CLE | draftkings | 14.00 | 13.32 | 8.27 | 12.1% | 6.7% | 7.5% | +5.1% | +69.3% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| DET to win | DET @ NOP | draftkings | 1.52 | Cade Cunningham | 62.5% | 70.9% | +6.6% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| MEM @ CLE | Thu 19 Nov 11:00 | 115.9–118.9 | MEM 41% | 2.42 / 1.71 | CLE -3.5 | 234.5 | CLE -4.5 covers 47%; o238.5 42% |
| HOU @ IND | Thu 19 Nov 11:00 | 118.0–113.9 | HOU 62% | 1.62 / 2.60 | IND +4.5 | 231.5 | IND +7.5 covers 59%; o225.5 63% |
| MIL @ MIA | Thu 19 Nov 11:00 | 109.2–123.0 | MIL 16% | 6.12 / 1.20 | MIA -13.5 | 231.5 | MIA -11.5 covers 57%; o237.5 38% |
| PHI @ ORL | Thu 19 Nov 11:00 | 110.4–111.5 | PHI 47% | 2.11 / 1.90 | ORL -1.5 | 221.5 | ORL +1.5 covers 56%; o221.5 51% |
| CHI @ BKN | Thu 19 Nov 11:30 | 116.4–118.6 | CHI 43% | 2.31 / 1.76 | BKN -2.5 | 234.5 | BKN -2.5 covers 51%; o239.5 40% |
| WAS @ TOR | Thu 19 Nov 11:30 | 110.2–117.8 | WAS 29% | 3.42 / 1.41 | TOR -7.5 | 227.5 | TOR -4.5 covers 59%; o225.5 55% |
| DET @ NOP | Thu 19 Nov 12:00 | 114.3–109.7 | DET 63% | 1.60 / 2.67 | NOP +4.5 | 223.5 | NOP +4.5 covers 49%; o225.5 46% |
| ATL @ OKC | Thu 19 Nov 12:00 | 109.4–118.3 | ATL 27% | 3.76 / 1.36 | OKC -8.5 | 227.5 | OKC -6.5 covers 57%; o228.5 48% |
| BOS @ DEN | Thu 19 Nov 13:30 | 112.7–108.4 | BOS 61% | 1.63 / 2.59 | DEN +4.5 | 221.5 | DEN +2.5 covers 45%; o219.5 53% |
| GSW @ DAL | Thu 19 Nov 12:00 | 114.1–116.4 | GSW 43% | 2.31 / 1.76 | DAL -2.5 | 230.5 | DAL -4.5 covers 44%; o224.5 62% |
| UTA @ LAL | Thu 19 Nov 14:00 | 107.9–124.0 | UTA 13% | 7.92 / 1.14 | LAL -16.5 | 231.5 | LAL -10.5 covers 65%; o228.5 57% |
| PHX @ SAC | Thu 19 Nov 14:00 | 119.9–112.1 | PHX 71% | 1.40 / 3.50 | SAC +7.5 | 231.5 | SAC +7.5 covers 49%; o226.5 61% |

### MEM @ CLE
Out: Evan Mobley (CLE), Nae'Qwan Tomlin (CLE), Jaylon Tyson (CLE), GG Jackson (MEM), Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Isaiah Stewart (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.9–118.9 | MEM 41% | 2.42 / 1.71 | CLE -3.5 | 234.5 | CLE -4.5 covers 47%; o238.5 42% |
| Expected (weighted by chance each plays) | 115.6–119.9 | MEM 38% | 2.62 / 1.62 | CLE -4.5 | 235.5 | CLE -4.5 covers 50%; o238.5 43% |
| if Sam Merrill plays | 115.4–119.7 | MEM 38% | 2.63 / 1.61 | CLE -4.5 | 234.5 | CLE -4.5 covers 50%; o238.5 43% |
| if Peyton Watson plays | 115.9–120.9 | MEM 36% | 2.78 / 1.56 | CLE -5.5 | 236.5 | CLE -4.5 covers 52%; o238.5 46% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sam Merrill (CLE) | Questionable | 55% | 22.5 | 9.2 | 2.7 | 1.9 | 1.7 | 0.7 | 0.2 | 0.7 | 13.8 | full tables below |
| Peyton Watson (CLE) | Doubtful | 20% | 28.3 | 12.7 | 4.6 | 2.4 | 1.3 | 0.9 | 1.5 | 1.6 | 19.8 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 33.0<br><sub>33,33,25,29,29</sub> | 18.2<br><sub>22,13,12,15,29</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 9.0<br><sub>7,11,10,8,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>8,5,3,5,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,2,1,0,7</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.6 | 3.3 | 32.9 |
| Cedric Coward | 98% | 30.4<br><sub>28,27,30,33,27</sub> | 15.8<br><sub>3,15,14,23,18</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>6,11,7,12,8</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>4,4,6,4,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,1,0,4,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.4 | 1.8 | 26.9 |
| Cam Spencer | 98% | 29.1<br><sub>17,20,24,34,32</sub> | 13.4<br><sub>7,15,14,17,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,3,2,1,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 7.1<br><sub>4,3,5,8,9</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>1,3,3,3,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.2 | 1.7 | 23.8 |
| Jaylen Wells | 98% | 28.8<br><sub>26,31,27,25,27</sub> | 12.5<br><sub>14,22,11,5,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,2,2,2,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,5,2,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.1 | 1.0 | 17.1 |
| Javon Small | 97% | 27.1<br><sub>24,15,15,30,29</sub> | 13.1<br><sub>9,3,10,19,12</sub> |  | 3.7<br><sub>2,1,2,2,5</sub> |  | 5.3<br><sub>5,4,5,5,12</sub> |  | 1.7<br><sub>1,1,2,3,0</sub> |  | 0.9 | 0.2 | 1.7 | 22.0 |
| Jerami Grant | 98% | 25.8<br><sub>22,20,26,-,23</sub> | 13.1<br><sub>17,14,22,-,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>3,2,1,-,1</sub> |  | 1.9<br><sub>2,2,1,-,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>3,2,3,-,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.6 | 1.3 | 17.4 |
| Zach Edey | 83% | 23.4<br><sub>23,20,-,-,21</sub> | 10.1<br><sub>8,2,-,-,23</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>9,5,-,-,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,-,-,1</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.6 | 1.2 | 1.6 | 20.5 |
| Taylor Hendricks | 86% | 19.5<br><sub>16,11,19,29,19</sub> | 8.6<br><sub>9,7,10,22,9</sub> |  | 4.0<br><sub>3,2,12,5,3</sub> |  | 1.0<br><sub>0,1,2,4,0</sub> |  | 1.1<br><sub>1,1,2,0,1</sub> |  | 0.9 | 0.4 | 0.9 | 13.6 |
| Olivier-Maxence Prosper | 72% | 14.9<br><sub>1,-,2,20,16</sub> | 7.9<br><sub>0,-,6,11,12</sub> |  | 2.8<br><sub>0,-,1,4,0</sub> |  | 0.9<br><sub>0,-,0,0,1</sub> |  | 0.7<br><sub>0,-,0,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 11.5 |
| Kris Murray | 84% | 13.0<br><sub>1,-,1,19,6</sub> | 2.8<br><sub>0,-,0,3,0</sub> |  | 1.9<br><sub>0,-,1,2,1</sub> |  | 0.8<br><sub>0,-,0,3,0</sub> |  | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.5 |
| Quinten Post | 96% | 12.3<br><sub>2,-,-,-,9</sub> | 4.6<br><sub>0,-,-,-,5</sub> |  | 2.5<br><sub>1,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.7 |
| Jahmai Mashack | 58% | 9.5<br><sub>-,-,-,2,2</sub> | 3.1<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.5 |
| Karim Lopez | 63% | 7.4<br><sub>-,-,-,2,1</sub> | 3.1<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 5.2 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell | 98% | 36.2<br><sub>23,36,33,-,36</sub> | 29.0<br><sub>11,23,25,-,39</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 5.2<br><sub>2,7,4,-,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 6.0<br><sub>4,6,7,-,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.2<br><sub>1,2,5,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.5 | 3.0 | 40.1 |
| James Harden | 98% | 35.7<br><sub>25,33,35,-,34</sub> | 20.2<br><sub>11,32,20,-,9</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>3,2,6,-,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 7.1<br><sub>5,4,8,-,10</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,5,2,-,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.7 | 3.5 | 32.5 |
| Jarrett Allen | 83% | 31.0<br><sub>19,32,32,-,30</sub> | 16.1<br><sub>12,11,9,-,13</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 10.3<br><sub>7,14,8,-,14</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>1,3,1,-,3</sub> |  | 0.1<br><sub>1,0,0,-,0</sub> |  | 1.0 | 2.0 | 1.4 | 28.2 |
| Meleek Thomas | 96% | 30.7<br><sub>27,22,18,34,30</sub> | 16.1<br><sub>18,14,12,20,10</sub> |  | 3.9<br><sub>3,4,0,4,6</sub> |  | 2.3<br><sub>3,1,3,2,3</sub> |  | 2.6<br><sub>4,2,2,3,1</sub> |  | 1.2 | 0.4 | 1.5 | 22.3 |
| Tyrese Proctor | 96% | 29.9<br><sub>23,23,27,34,29</sub> | 14.8<br><sub>6,15,22,24,17</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>1,3,4,11,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.3<br><sub>4,1,3,10,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>0,3,5,4,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.2 | 0.2 | 1.5 | 23.9 |
| Mario Hezonja | 98% | 21.4<br><sub>17,7,9,34,15</sub> | 9.3<br><sub>10,0,4,22,9</sub> |  | 5.7<br><sub>3,0,4,7,4</sub> |  | 1.7<br><sub>0,0,0,4,2</sub> |  | 1.1<br><sub>0,0,0,2,1</sub> |  | 0.7 | 0.3 | 1.0 | 16.7 |
| Thomas Bryant | 80% | 21.3<br><sub>15,-,16,27,18</sub> | 11.1<br><sub>11,-,9,19,9</sub> |  | 5.8<br><sub>2,-,1,11,5</sub> |  | 1.2<br><sub>0,-,1,3,4</sub> |  | 1.2<br><sub>2,-,0,2,0</sub> |  | 0.5 | 0.8 | 0.9 | 18.0 |
| Craig Porter Jr. | 86% | 19.5<br><sub>17,-,9,28,14</sub> | 4.5<br><sub>9,-,0,9,2</sub> |  | 3.9<br><sub>2,-,2,9,1</sub> |  | 3.5<br><sub>4,-,2,6,3</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.9 | 0.6 | 0.9 | 11.8 |
| Norchad Omier | 63% | 17.8<br><sub>12,-,-,27,13</sub> | 5.8<br><sub>0,-,-,13,4</sub> |  | 5.4<br><sub>3,-,-,8,6</sub> |  | 1.7<br><sub>2,-,-,2,2</sub> |  | 0.3<br><sub>0,-,-,1,0</sub> |  | 0.6 | 0.4 | 1.0 | 12.9 |
| Riley Minix | 48% | 15.8<br><sub>17,-,-,22,-</sub> | 5.8<br><sub>2,-,-,2,-</sub> |  | 2.2<br><sub>2,-,-,0,-</sub> |  | 0.7<br><sub>0,-,-,0,-</sub> |  | 0.6<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.7 |
| Khalifa Diop | 30% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Zack Austin | 3% | 8.5 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>if Sam Merrill plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell (CLE) | 98% | 35.1<br><sub>23,36,33,-,36</sub> | 27.5<br><sub>11,23,25,-,39</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>2,7,4,-,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>4,6,7,-,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>1,2,5,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.4 | 3.0 | 38.4 |
| James Harden (CLE) | 98% | 34.7<br><sub>25,33,35,-,34</sub> | 19.6<br><sub>11,32,20,-,9</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>3,2,6,-,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 7.1<br><sub>5,4,8,-,10</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,5,2,-,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.6 | 3.3 | 31.8 |
| Jarrett Allen (CLE) | 83% | 29.2<br><sub>19,32,32,-,30</sub> | 14.9<br><sub>12,11,9,-,13</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 9.8<br><sub>7,14,8,-,14</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,3,1,-,3</sub> |  | 0.1<br><sub>1,0,0,-,0</sub> |  | 1.0 | 1.8 | 1.4 | 26.6 |
| Meleek Thomas (CLE) | 96% | 28.4<br><sub>27,22,18,34,30</sub> | 14.1<br><sub>18,14,12,20,10</sub> |  | 3.6<br><sub>3,4,0,4,6</sub> |  | 2.2<br><sub>3,1,3,2,3</sub> |  | 2.3<br><sub>4,2,2,3,1</sub> |  | 1.1 | 0.3 | 1.4 | 19.9 |
| Tyrese Proctor (CLE) | 96% | 28.2<br><sub>23,23,27,34,29</sub> | 14.0<br><sub>6,15,22,24,17</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>1,3,4,11,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.2<br><sub>4,1,3,10,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,3,5,4,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.1 | 1.4 | 22.7 |
| Sam Merrill (CLE) | 100% | 22.5<br><sub>-,-,-,-,-</sub> | 9.2<br><sub>-,-,-,-,-</sub> |  | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.2 | 0.7 | 13.8 |
| Mario Hezonja (CLE) | 98% | 19.3<br><sub>17,7,9,34,15</sub> | 8.4<br><sub>10,0,4,22,9</sub> |  | 5.2<br><sub>3,0,4,7,4</sub> |  | 1.5<br><sub>0,0,0,4,2</sub> |  | 0.9<br><sub>0,0,0,2,1</sub> |  | 0.7 | 0.3 | 0.9 | 15.1 |
| Thomas Bryant (CLE) | 80% | 19.0<br><sub>15,-,16,27,18</sub> | 10.1<br><sub>11,-,9,19,9</sub> |  | 5.2<br><sub>2,-,1,11,5</sub> |  | 1.1<br><sub>0,-,1,3,4</sub> |  | 1.1<br><sub>2,-,0,2,0</sub> |  | 0.5 | 0.7 | 0.8 | 16.4 |
| Craig Porter Jr. (CLE) | 86% | 16.5<br><sub>17,-,9,28,14</sub> | 4.0<br><sub>9,-,0,9,2</sub> |  | 3.3<br><sub>2,-,2,9,1</sub> |  | 3.0<br><sub>4,-,2,6,3</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.5 | 0.9 | 10.3 |
| Norchad Omier (CLE) | 63% | 16.1<br><sub>12,-,-,27,13</sub> | 5.3<br><sub>0,-,-,13,4</sub> |  | 4.9<br><sub>3,-,-,8,6</sub> |  | 1.5<br><sub>2,-,-,2,2</sub> |  | 0.2<br><sub>0,-,-,1,0</sub> |  | 0.5 | 0.3 | 0.9 | 11.8 |
| Riley Minix (CLE) | 48% | 13.3<br><sub>17,-,-,22,-</sub> | 4.8<br><sub>2,-,-,2,-</sub> |  | 1.9<br><sub>2,-,-,0,-</sub> |  | 0.6<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.5 | 7.3 |
| Zack Austin (CLE) | 3% | 8.5 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Khalifa Diop (CLE) | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Cameron Boozer (MEM) | 98% | 33.0<br><sub>33,33,25,29,29</sub> | 18.1<br><sub>22,13,12,15,29</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 8.9<br><sub>7,11,10,8,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>8,5,3,5,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,2,1,0,7</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.6 | 3.3 | 32.7 |
| Cedric Coward (MEM) | 98% | 30.4<br><sub>28,27,30,33,27</sub> | 15.9<br><sub>3,15,14,23,18</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>6,11,7,12,8</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>4,4,6,4,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,1,0,4,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.4 | 1.8 | 26.9 |
| Cam Spencer (MEM) | 98% | 29.2<br><sub>17,20,24,34,32</sub> | 13.3<br><sub>7,15,14,17,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,3,2,1,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 7.1<br><sub>4,3,5,8,9</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>1,3,3,3,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.2 | 1.7 | 23.7 |
| Jaylen Wells (MEM) | 98% | 28.9<br><sub>26,31,27,25,27</sub> | 12.4<br><sub>14,22,11,5,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,2,2,2,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,5,2,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.1 | 1.0 | 17.1 |
| Javon Small (MEM) | 97% | 27.1<br><sub>24,15,15,30,29</sub> | 13.0<br><sub>9,3,10,19,12</sub> |  | 3.7<br><sub>2,1,2,2,5</sub> |  | 5.3<br><sub>5,4,5,5,12</sub> |  | 1.7<br><sub>1,1,2,3,0</sub> |  | 0.9 | 0.2 | 1.6 | 22.0 |
| Jerami Grant (MEM) | 98% | 25.9<br><sub>22,20,26,-,23</sub> | 13.2<br><sub>17,14,22,-,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>3,2,1,-,1</sub> |  | 1.9<br><sub>2,2,1,-,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>3,2,3,-,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.6 | 1.3 | 17.5 |
| Zach Edey (MEM) | 83% | 23.3<br><sub>23,20,-,-,21</sub> | 10.0<br><sub>8,2,-,-,23</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>9,5,-,-,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,-,-,1</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.6 | 1.2 | 1.6 | 20.4 |
| Taylor Hendricks (MEM) | 86% | 19.5<br><sub>16,11,19,29,19</sub> | 8.6<br><sub>9,7,10,22,9</sub> |  | 3.9<br><sub>3,2,12,5,3</sub> |  | 1.0<br><sub>0,1,2,4,0</sub> |  | 1.0<br><sub>1,1,2,0,1</sub> |  | 0.9 | 0.4 | 0.9 | 13.5 |
| Olivier-Maxence Prosper (MEM) | 72% | 14.9<br><sub>1,-,2,20,16</sub> | 7.9<br><sub>0,-,6,11,12</sub> |  | 2.8<br><sub>0,-,1,4,0</sub> |  | 0.8<br><sub>0,-,0,0,1</sub> |  | 0.7<br><sub>0,-,0,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 11.5 |
| Kris Murray (MEM) | 84% | 13.0<br><sub>1,-,1,19,6</sub> | 2.8<br><sub>0,-,0,3,0</sub> |  | 1.9<br><sub>0,-,1,2,1</sub> |  | 0.9<br><sub>0,-,0,3,0</sub> |  | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.6 |
| Quinten Post (MEM) | 96% | 12.3<br><sub>2,-,-,-,9</sub> | 4.6<br><sub>0,-,-,-,5</sub> |  | 2.5<br><sub>1,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.8 |
| Jahmai Mashack (MEM) | 58% | 9.5<br><sub>-,-,-,2,2</sub> | 3.1<br><sub>-,-,-,0,0</sub> |  | 1.1<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 5.5 |
| Karim Lopez (MEM) | 63% | 7.4<br><sub>-,-,-,2,1</sub> | 3.1<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 5.2 |

</details>

<details><summary>if Peyton Watson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell (CLE) | 98% | 35.1<br><sub>23,36,33,-,36</sub> | 27.5<br><sub>11,23,25,-,39</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>2,7,4,-,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>4,6,7,-,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>1,2,5,-,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5 | 0.4 | 2.9 | 38.3 |
| James Harden (CLE) | 98% | 34.9<br><sub>25,33,35,-,34</sub> | 19.4<br><sub>11,32,20,-,9</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>3,2,6,-,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>5,4,8,-,10</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,5,2,-,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.6 | 3.2 | 31.4 |
| Jarrett Allen (CLE) | 83% | 28.8<br><sub>19,32,32,-,30</sub> | 14.5<br><sub>12,11,9,-,13</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>7,14,8,-,14</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,3,1,-,3</sub> |  | 0.1<br><sub>1,0,0,-,0</sub> |  | 1.0 | 1.8 | 1.4 | 25.9 |
| Peyton Watson (CLE) | 100% | 28.3<br><sub>21,30,30,-,22</sub> | 12.7<br><sub>13,7,4,-,14</sub> |  | 4.6<br><sub>2,5,4,-,4</sub> |  | 2.4<br><sub>1,4,2,-,0</sub> |  | 1.3<br><sub>2,2,0,-,2</sub> |  | 0.9 | 1.5 | 1.6 | 19.8 |
| Tyrese Proctor (CLE) | 96% | 28.0<br><sub>23,23,27,34,29</sub> | 13.6<br><sub>6,15,22,24,17</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>1,3,4,11,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.0<br><sub>4,1,3,10,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>0,3,5,4,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.1 | 1.4 | 22.1 |
| Meleek Thomas (CLE) | 96% | 28.0<br><sub>27,22,18,34,30</sub> | 13.8<br><sub>18,14,12,20,10</sub> |  | 3.5<br><sub>3,4,0,4,6</sub> |  | 2.1<br><sub>3,1,3,2,3</sub> |  | 2.3<br><sub>4,2,2,3,1</sub> |  | 1.1 | 0.3 | 1.3 | 19.4 |
| Thomas Bryant (CLE) | 80% | 18.8<br><sub>15,-,16,27,18</sub> | 10.0<br><sub>11,-,9,19,9</sub> |  | 5.0<br><sub>2,-,1,11,5</sub> |  | 1.1<br><sub>0,-,1,3,4</sub> |  | 1.0<br><sub>2,-,0,2,0</sub> |  | 0.5 | 0.7 | 0.8 | 16.0 |
| Mario Hezonja (CLE) | 98% | 18.6<br><sub>17,7,9,34,15</sub> | 7.9<br><sub>10,0,4,22,9</sub> |  | 5.0<br><sub>3,0,4,7,4</sub> |  | 1.4<br><sub>0,0,0,4,2</sub> |  | 0.9<br><sub>0,0,0,2,1</sub> |  | 0.6 | 0.3 | 0.9 | 14.3 |
| Craig Porter Jr. (CLE) | 86% | 16.0<br><sub>17,-,9,28,14</sub> | 3.8<br><sub>9,-,0,9,2</sub> |  | 3.2<br><sub>2,-,2,9,1</sub> |  | 2.9<br><sub>4,-,2,6,3</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.8 | 0.5 | 0.8 | 9.9 |
| Norchad Omier (CLE) | 63% | 15.5<br><sub>12,-,-,27,13</sub> | 5.0<br><sub>0,-,-,13,4</sub> |  | 4.6<br><sub>3,-,-,8,6</sub> |  | 1.4<br><sub>2,-,-,2,2</sub> |  | 0.2<br><sub>0,-,-,1,0</sub> |  | 0.5 | 0.3 | 0.9 | 11.0 |
| Riley Minix (CLE) | 48% | 12.8<br><sub>17,-,-,22,-</sub> | 4.6<br><sub>2,-,-,2,-</sub> |  | 1.8<br><sub>2,-,-,0,-</sub> |  | 0.6<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 7.1 |
| Khalifa Diop (CLE) | 30% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Zack Austin (CLE) | 3% | 8.6 | 3.7 |  | 1.5 |  | 0.7 |  | 0.2 |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Cameron Boozer (MEM) | 98% | 33.0<br><sub>33,33,25,29,29</sub> | 18.1<br><sub>22,13,12,15,29</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 8.9<br><sub>7,11,10,8,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>8,5,3,5,7</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>0,2,1,0,7</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.6 | 3.3 | 32.7 |
| Cedric Coward (MEM) | 98% | 30.4<br><sub>28,27,30,33,27</sub> | 15.9<br><sub>3,15,14,23,18</sub> | 16.5 · –<br><sub>o 46% · u 54%</sub> | 7.5<br><sub>6,11,7,12,8</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>4,4,6,4,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,1,0,4,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.4 | 1.8 | 26.9 |
| Cam Spencer (MEM) | 98% | 29.1<br><sub>17,20,24,34,32</sub> | 13.4<br><sub>7,15,14,17,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>2,3,2,1,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 7.1<br><sub>4,3,5,8,9</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>1,3,3,3,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.2 | 1.7 | 23.8 |
| Jaylen Wells (MEM) | 98% | 28.9<br><sub>26,31,27,25,27</sub> | 12.4<br><sub>14,22,11,5,8</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>4,2,2,2,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>1,1,1,2,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>4,5,2,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.1 | 1.0 | 17.1 |
| Javon Small (MEM) | 97% | 27.2<br><sub>24,15,15,30,29</sub> | 13.1<br><sub>9,3,10,19,12</sub> |  | 3.7<br><sub>2,1,2,2,5</sub> |  | 5.3<br><sub>5,4,5,5,12</sub> |  | 1.7<br><sub>1,1,2,3,0</sub> |  | 0.9 | 0.2 | 1.6 | 22.1 |
| Jerami Grant (MEM) | 98% | 25.9<br><sub>22,20,26,-,23</sub> | 13.2<br><sub>17,14,22,-,8</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>3,2,1,-,1</sub> |  | 1.9<br><sub>2,2,1,-,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>3,2,3,-,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.6 | 1.3 | 17.5 |
| Zach Edey (MEM) | 83% | 23.4<br><sub>23,20,-,-,21</sub> | 10.1<br><sub>8,2,-,-,23</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>9,5,-,-,10</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>1,0,-,-,1</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.6 | 1.2 | 1.6 | 20.5 |
| Taylor Hendricks (MEM) | 86% | 19.3<br><sub>16,11,19,29,19</sub> | 8.5<br><sub>9,7,10,22,9</sub> |  | 4.0<br><sub>3,2,12,5,3</sub> |  | 1.0<br><sub>0,1,2,4,0</sub> |  | 1.0<br><sub>1,1,2,0,1</sub> |  | 0.9 | 0.4 | 0.9 | 13.4 |
| Olivier-Maxence Prosper (MEM) | 72% | 14.9<br><sub>1,-,2,20,16</sub> | 7.9<br><sub>0,-,6,11,12</sub> |  | 2.8<br><sub>0,-,1,4,0</sub> |  | 0.8<br><sub>0,-,0,0,1</sub> |  | 0.7<br><sub>0,-,0,2,1</sub> |  | 0.6 | 0.2 | 0.7 | 11.6 |
| Kris Murray (MEM) | 84% | 13.0<br><sub>1,-,1,19,6</sub> | 2.8<br><sub>0,-,0,3,0</sub> |  | 1.9<br><sub>0,-,1,2,1</sub> |  | 0.8<br><sub>0,-,0,3,0</sub> |  | 0.2<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 5.6 |
| Quinten Post (MEM) | 96% | 12.3<br><sub>2,-,-,-,9</sub> | 4.6<br><sub>0,-,-,-,5</sub> |  | 2.6<br><sub>1,-,-,-,3</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 7.8 |
| Jahmai Mashack (MEM) | 58% | 9.4<br><sub>-,-,-,2,2</sub> | 3.2<br><sub>-,-,-,0,0</sub> |  | 1.1<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.7 | 5.5 |
| Karim Lopez (MEM) | 63% | 7.5<br><sub>-,-,-,2,1</sub> | 3.2<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 5.3 |

</details>


### HOU @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND), Clint Capela (HOU)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.0–113.9 | HOU 62% | 1.62 / 2.60 | IND +4.5 | 231.5 | IND +7.5 covers 59%; o225.5 63% |
| Expected (weighted by chance each plays) | 117.9–114.2 | HOU 61% | 1.65 / 2.54 | IND +4.5 | 231.5 | IND +7.5 covers 60%; o225.5 63% |
| if Amen Thompson plays | 118.5–113.3 | HOU 65% | 1.55 / 2.83 | IND +5.5 | 231.5 | IND +7.5 covers 56%; o225.5 63% |
| if Andrew Nembhard plays | 117.4–115.3 | HOU 56% | 1.79 / 2.27 | IND +2.5 | 232.5 | IND +7.5 covers 65%; o225.5 65% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | Questionable | 55% | 35.5 | 16.4 | 7.9 | 4.2 | 0.3 | 1.6 | 0.8 | 2.0 | 28.4 | full tables below |
| Andrew Nembhard (IND) | Questionable | 55% | 32.5 | 16.6 | 2.8 | 7.7 | 1.9 | 1.0 | 0.2 | 2.3 | 27.1 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 99% | 36.5<br><sub>36,34,33,30,29</sub> | 25.8<br><sub>23,20,22,25,22</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>12,4,3,4,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.8<br><sub>8,5,6,5,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.9 | 3.0 | 36.6 |
| Alperen Sengun | 91% | 36.3<br><sub>35,37,37,28,30</sub> | 23.7<br><sub>20,19,43,19,23</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>12,13,12,8,7</sub> | 9.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>8,9,5,8,2</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>1,1,1,1,1</sub> |  | 1.4 | 1.0 | 2.9 | 40.9 |
| Jabari Smith Jr. | 98% | 36.1<br><sub>38,35,24,28,32</sub> | 16.0<br><sub>14,14,6,9,12</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>7,8,3,6,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>3,0,0,5,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,2,1,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.9 | 1.3 | 25.4 |
| Fred VanVleet | 80% | 34.8<br><sub>30,30,34,-,26</sub> | 15.0<br><sub>12,18,17,-,8</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,2,2,-,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.5<br><sub>2,6,3,-,6</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>3,4,3,-,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.4 | 1.4 | 24.3 |
| Tari Eason | 99% | 30.0<br><sub>19,22,33,30,27</sub> | 12.4<br><sub>12,6,14,25,7</sub> |  | 7.4<br><sub>5,3,11,7,7</sub> |  | 1.7<br><sub>2,0,2,1,3</sub> |  | 1.4<br><sub>2,0,2,3,0</sub> |  | 1.5 | 0.7 | 1.3 | 21.5 |
| Reed Sheppard | 91% | 25.1<br><sub>17,20,19,26,19</sub> | 11.2<br><sub>8,13,0,11,5</sub> |  | 2.4<br><sub>0,1,0,1,2</sub> |  | 3.1<br><sub>0,1,3,6,2</sub> |  | 2.0<br><sub>2,3,0,3,1</sub> |  | 1.5 | 0.5 | 1.1 | 16.6 |
| Marcus Smart | 52% | 22.2<br><sub>17,17,-,-,-</sub> | 7.9<br><sub>5,6,-,-,-</sub> |  | 2.5<br><sub>2,2,-,-,-</sub> |  | 2.4<br><sub>2,1,-,-,-</sub> |  | 1.1<br><sub>1,2,-,-,-</sub> |  | 1.3 | 0.3 | 1.3 | 12.8 |
| Bogdan Bogdanovic | 98% | 22.1<br><sub>12,10,12,22,26</sub> | 7.9<br><sub>8,0,11,12,6</sub> |  | 2.7<br><sub>3,0,1,3,0</sub> |  | 2.0<br><sub>1,0,3,4,1</sub> |  | 1.3<br><sub>2,0,3,2,2</sub> |  | 0.7 | 0.2 | 0.9 | 12.6 |
| Steven Adams | 38% | 15.8<br><sub>-,-,-,12,-</sub> | 4.1<br><sub>-,-,-,6,-</sub> |  | 6.1<br><sub>-,-,-,7,-</sub> |  | 1.0<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.5 | 0.9 | 11.3 |
| Isaiah Crawford | 67% | 13.5<br><sub>1,1,-,9,21</sub> | 4.1<br><sub>0,0,-,4,11</sub> |  | 2.9<br><sub>0,0,-,2,10</sub> |  | 0.7<br><sub>0,0,-,0,3</sub> |  | 0.4<br><sub>0,0,-,0,1</sub> |  | 0.4 | 0.4 | 0.5 | 7.7 |
| Oscar Tshiebwe | 96% | 11.3<br><sub>-,1,6,12,6</sub> | 4.4<br><sub>-,0,0,4,6</sub> |  | 5.3<br><sub>-,0,5,9,6</sub> |  | 0.7<br><sub>-,0,0,3,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 10.4 |
| Bruce Thornton | 67% | 10.1<br><sub>1,3,-,6,12</sub> | 4.2<br><sub>0,0,-,2,7</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.4 |
| Jae'Sean Tate | 63% | 10.0<br><sub>-,1,-,8,12</sub> | 2.9<br><sub>-,0,-,4,3</sub> |  | 2.4<br><sub>-,0,-,2,3</sub> |  | 0.6<br><sub>-,0,-,0,2</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.9 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 91% | 33.9<br><sub>32,35,32,32,34</sub> | 23.9<br><sub>23,29,28,19,31</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>2,9,8,3,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>5,8,5,2,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,5,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.4 | 2.2 | 34.2 |
| Aaron Nesmith | 91% | 31.3<br><sub>27,34,22,33,36</sub> | 14.9<br><sub>8,18,2,18,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>5,2,1,7,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,2,1,1,4</sub> |  | 2.1<br><sub>2,4,0,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.5 | 1.5 | 20.8 |
| Kelly Oubre Jr. | 88% | 28.8<br><sub>16,23,34,30,29</sub> | 12.6<br><sub>2,14,14,16,16</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,2,6,5,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,2,1,0,2</sub> |  | 1.3<br><sub>0,1,0,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.6 | 1.2 | 18.1 |
| Quenton Jackson | 98% | 26.7<br><sub>17,25,21,20,30</sub> | 12.5<br><sub>6,10,4,3,15</sub> |  | 3.5<br><sub>4,5,2,5,6</sub> |  | 4.3<br><sub>1,4,2,4,8</sub> |  | 1.2<br><sub>0,2,1,1,1</sub> |  | 1.2 | 0.2 | 1.6 | 20.3 |
| Ivica Zubac | 80% | 26.5<br><sub>19,28,31,26,22</sub> | 11.8<br><sub>10,16,20,12,8</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 9.1<br><sub>12,3,12,13,5</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>5,0,1,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 1.4 | 22.6 |
| Obi Toppin | 88% | 18.7<br><sub>22,19,16,16,14</sub> | 10.5<br><sub>10,10,8,9,5</sub> |  | 3.9<br><sub>7,2,3,3,2</sub> |  | 1.7<br><sub>2,4,1,1,1</sub> |  | 1.3<br><sub>2,0,2,1,0</sub> |  | 0.5 | 0.2 | 0.9 | 16.1 |
| T.J. McConnell | 91% | 17.7<br><sub>9,8,14,17,19</sub> | 9.4<br><sub>6,2,7,6,12</sub> |  | 2.4<br><sub>2,0,3,3,5</sub> |  | 5.5<br><sub>1,3,7,7,5</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.2 | 1.4 | 17.4 |
| Jarace Walker | 83% | 17.6<br><sub>20,10,7,-,14</sub> | 7.3<br><sub>9,7,1,-,2</sub> |  | 3.7<br><sub>5,1,1,-,5</sub> |  | 1.7<br><sub>2,0,0,-,2</sub> |  | 0.9<br><sub>1,2,0,-,0</sub> |  | 0.6 | 0.3 | 1.0 | 12.7 |
| Jay Huff | 88% | 16.6<br><sub>10,-,11,8,18</sub> | 7.3<br><sub>0,-,6,8,11</sub> |  | 3.0<br><sub>3,-,4,1,0</sub> |  | 1.1<br><sub>0,-,0,0,2</sub> |  | 0.9<br><sub>0,-,0,2,3</sub> |  | 0.4 | 1.0 | 0.7 | 11.4 |
| Kobe Brown | 80% | 14.8<br><sub>-,-,-,-,3</sub> | 5.5<br><sub>-,-,-,-,0</sub> |  | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.2 |
| Jalen Slawson | 88% | 14.2<br><sub>12,-,12,10,14</sub> | 4.3<br><sub>4,-,2,1,8</sub> |  | 2.8<br><sub>1,-,3,4,5</sub> |  | 1.3<br><sub>2,-,1,0,2</sub> |  | 0.3<br><sub>0,-,0,0,1</sub> |  | 0.7 | 0.6 | 0.7 | 8.4 |
| Braden Smith | 58% | 13.1<br><sub>12,10,-,-,-</sub> | 4.3<br><sub>0,0,-,-,-</sub> |  | 1.0<br><sub>0,0,-,-,-</sub> |  | 2.3<br><sub>2,0,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.7 | 0.2 | 0.8 | 7.6 |
| Larry Nance Jr. | 96% | 12.4<br><sub>13,14,5,14,7</sub> | 3.9<br><sub>15,4,5,2,4</sub> |  | 2.3<br><sub>2,0,0,2,2</sub> |  | 0.8<br><sub>1,0,0,1,2</sub> |  | 0.4<br><sub>5,0,1,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 6.9 |

</details>

<details><summary>if Andrew Nembhard plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant (HOU) | 99% | 36.5<br><sub>36,34,33,30,29</sub> | 25.9<br><sub>23,20,22,25,22</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>12,4,3,4,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>8,5,6,5,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.9 | 3.0 | 36.7 |
| Alperen Sengun (HOU) | 91% | 36.3<br><sub>35,37,37,28,30</sub> | 23.7<br><sub>20,19,43,19,23</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 10.3<br><sub>12,13,12,8,7</sub> | 9.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>8,9,5,8,2</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>1,1,1,1,1</sub> |  | 1.4 | 1.0 | 2.9 | 40.9 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>38,35,24,28,32</sub> | 15.9<br><sub>14,14,6,9,12</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>7,8,3,6,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>3,0,0,5,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,2,1,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.8 | 1.3 | 25.4 |
| Fred VanVleet (HOU) | 80% | 34.8<br><sub>30,30,34,-,26</sub> | 15.1<br><sub>12,18,17,-,8</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>1,2,2,-,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 5.4<br><sub>2,6,3,-,6</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>3,4,3,-,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.4 | 1.4 | 24.3 |
| Tari Eason (HOU) | 99% | 29.9<br><sub>19,22,33,30,27</sub> | 12.4<br><sub>12,6,14,25,7</sub> |  | 7.4<br><sub>5,3,11,7,7</sub> |  | 1.7<br><sub>2,0,2,1,3</sub> |  | 1.4<br><sub>2,0,2,3,0</sub> |  | 1.5 | 0.7 | 1.3 | 21.5 |
| Reed Sheppard (HOU) | 91% | 25.1<br><sub>17,20,19,26,19</sub> | 11.2<br><sub>8,13,0,11,5</sub> |  | 2.4<br><sub>0,1,0,1,2</sub> |  | 3.0<br><sub>0,1,3,6,2</sub> |  | 2.0<br><sub>2,3,0,3,1</sub> |  | 1.5 | 0.5 | 1.1 | 16.6 |
| Marcus Smart (HOU) | 52% | 22.4<br><sub>17,17,-,-,-</sub> | 7.8<br><sub>5,6,-,-,-</sub> |  | 2.5<br><sub>2,2,-,-,-</sub> |  | 2.4<br><sub>2,1,-,-,-</sub> |  | 1.1<br><sub>1,2,-,-,-</sub> |  | 1.3 | 0.3 | 1.3 | 12.8 |
| Bogdan Bogdanovic (HOU) | 98% | 22.1<br><sub>12,10,12,22,26</sub> | 7.9<br><sub>8,0,11,12,6</sub> |  | 2.7<br><sub>3,0,1,3,0</sub> |  | 2.0<br><sub>1,0,3,4,1</sub> |  | 1.3<br><sub>2,0,3,2,2</sub> |  | 0.7 | 0.2 | 0.9 | 12.6 |
| Steven Adams (HOU) | 38% | 15.6<br><sub>-,-,-,12,-</sub> | 4.1<br><sub>-,-,-,6,-</sub> |  | 6.0<br><sub>-,-,-,7,-</sub> |  | 1.0<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.5 | 0.9 | 11.2 |
| Isaiah Crawford (HOU) | 67% | 13.6<br><sub>1,1,-,9,21</sub> | 4.1<br><sub>0,0,-,4,11</sub> |  | 2.9<br><sub>0,0,-,2,10</sub> |  | 0.7<br><sub>0,0,-,0,3</sub> |  | 0.4<br><sub>0,0,-,0,1</sub> |  | 0.4 | 0.4 | 0.5 | 7.7 |
| Oscar Tshiebwe (HOU) | 96% | 11.3<br><sub>-,1,6,12,6</sub> | 4.4<br><sub>-,0,0,4,6</sub> |  | 5.3<br><sub>-,0,5,9,6</sub> |  | 0.7<br><sub>-,0,0,3,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.3 | 0.5 | 10.4 |
| Bruce Thornton (HOU) | 67% | 10.1<br><sub>1,3,-,6,12</sub> | 4.2<br><sub>0,0,-,2,7</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.4 |
| Jae'Sean Tate (HOU) | 63% | 10.0<br><sub>-,1,-,8,12</sub> | 3.0<br><sub>-,0,-,4,3</sub> |  | 2.4<br><sub>-,0,-,2,3</sub> |  | 0.6<br><sub>-,0,-,0,2</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.9 |
| Andrew Nembhard (IND) | 100% | 32.5<br><sub>31,34,34,34,-</sub> | 16.6<br><sub>9,12,17,12,-</sub> | 14.5 · – | 2.8<br><sub>1,3,2,4,-</sub> | 2.5 | 7.7<br><sub>8,12,10,6,-</sub> | 6.5 | 1.9<br><sub>3,1,3,1,-</sub> | 1.5 | 1.0 | 0.2 | 2.3 | 27.1 |
| Pascal Siakam (IND) | 91% | 32.0<br><sub>32,35,32,32,34</sub> | 22.3<br><sub>23,29,28,19,31</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>2,9,8,3,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>5,8,5,2,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>2,5,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 2.0 | 31.9 |
| Aaron Nesmith (IND) | 91% | 27.6<br><sub>27,34,22,33,36</sub> | 12.8<br><sub>8,18,2,18,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>5,2,1,7,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>1,2,1,1,4</sub> |  | 1.8<br><sub>2,4,0,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.4 | 1.2 | 17.8 |
| Kelly Oubre Jr. (IND) | 88% | 25.4<br><sub>16,23,34,30,29</sub> | 11.0<br><sub>2,14,14,16,16</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>1,2,6,5,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>0,2,1,0,2</sub> |  | 1.1<br><sub>0,1,0,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.5 | 1.1 | 15.9 |
| Ivica Zubac (IND) | 80% | 24.3<br><sub>19,28,31,26,22</sub> | 10.9<br><sub>10,16,20,12,8</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 8.5<br><sub>12,3,12,13,5</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>5,0,1,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 1.3 | 20.8 |
| Quenton Jackson (IND) | 98% | 22.6<br><sub>17,25,21,20,30</sub> | 10.5<br><sub>6,10,4,3,15</sub> |  | 3.1<br><sub>4,5,2,5,6</sub> |  | 3.3<br><sub>1,4,2,4,8</sub> |  | 1.0<br><sub>0,2,1,1,1</sub> |  | 1.0 | 0.2 | 1.3 | 16.9 |
| Obi Toppin (IND) | 88% | 16.7<br><sub>22,19,16,16,14</sub> | 9.2<br><sub>10,10,8,9,5</sub> |  | 3.5<br><sub>7,2,3,3,2</sub> |  | 1.4<br><sub>2,4,1,1,1</sub> |  | 1.1<br><sub>2,0,2,1,0</sub> |  | 0.5 | 0.2 | 0.8 | 14.2 |
| T.J. McConnell (IND) | 91% | 14.9<br><sub>9,8,14,17,19</sub> | 7.9<br><sub>6,2,7,6,12</sub> |  | 2.1<br><sub>2,0,3,3,5</sub> |  | 4.6<br><sub>1,3,7,7,5</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.2 | 1.1 | 14.7 |
| Jarace Walker (IND) | 83% | 14.9<br><sub>20,10,7,-,14</sub> | 6.2<br><sub>9,7,1,-,2</sub> |  | 3.2<br><sub>5,1,1,-,5</sub> |  | 1.3<br><sub>2,0,0,-,2</sub> |  | 0.7<br><sub>1,2,0,-,0</sub> |  | 0.5 | 0.3 | 0.9 | 10.7 |
| Jay Huff (IND) | 88% | 14.6<br><sub>10,-,11,8,18</sub> | 6.6<br><sub>0,-,6,8,11</sub> |  | 2.7<br><sub>3,-,4,1,0</sub> |  | 0.9<br><sub>0,-,0,0,2</sub> |  | 0.7<br><sub>0,-,0,2,3</sub> |  | 0.4 | 0.9 | 0.7 | 10.2 |
| Jalen Slawson (IND) | 88% | 12.3<br><sub>12,-,12,10,14</sub> | 3.6<br><sub>4,-,2,1,8</sub> |  | 2.5<br><sub>1,-,3,4,5</sub> |  | 1.1<br><sub>2,-,1,0,2</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.7 | 0.5 | 0.6 | 7.2 |
| Kobe Brown (IND) | 80% | 9.9<br><sub>-,-,-,-,3</sub> | 3.6<br><sub>-,-,-,-,0</sub> |  | 1.7<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Larry Nance Jr. (IND) | 96% | 9.7<br><sub>13,14,5,14,7</sub> | 3.1<br><sub>15,4,5,2,4</sub> |  | 1.9<br><sub>2,0,0,2,2</sub> |  | 0.6<br><sub>1,0,0,1,2</sub> |  | 0.3<br><sub>5,0,1,0,1</sub> |  | 0.5 | 0.1 | 0.3 | 5.6 |
| Braden Smith (IND) | 58% | 8.7<br><sub>12,10,-,-,-</sub> | 2.9<br><sub>0,0,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 1.5<br><sub>2,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 5.0 |

</details>

<details><summary>if Amen Thompson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 100% | 35.5<br><sub>35,29,41,29,-</sub> | 16.4<br><sub>8,19,12,26,-</sub> | 15.5 · – | 7.9<br><sub>9,7,10,7,-</sub> | 7.5 | 4.2<br><sub>3,4,3,7,-</sub> | 3.5 | 0.3<br><sub>0,0,0,3,-</sub> |  | 1.6 | 0.8 | 2.0 | 28.4 |
| Kevin Durant (HOU) | 99% | 35.4<br><sub>36,34,33,30,29</sub> | 24.2<br><sub>23,20,22,25,22</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>12,4,3,4,2</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>8,5,6,5,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>1,1,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.9 | 2.9 | 34.6 |
| Alperen Sengun (HOU) | 91% | 35.2<br><sub>35,37,37,28,30</sub> | 21.9<br><sub>20,19,43,19,23</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 10.0<br><sub>12,13,12,8,7</sub> | 9.5<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>8,9,5,8,2</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>1,1,1,1,1</sub> |  | 1.3 | 1.0 | 2.7 | 38.8 |
| Jabari Smith Jr. (HOU) | 98% | 34.6<br><sub>38,35,24,28,32</sub> | 14.5<br><sub>14,14,6,9,12</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>7,8,3,6,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>3,0,0,5,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>2,2,1,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.9 | 1.2 | 23.5 |
| Fred VanVleet (HOU) | 80% | 31.7<br><sub>30,30,34,-,26</sub> | 13.0<br><sub>12,18,17,-,8</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>1,2,2,-,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 4.8<br><sub>2,6,3,-,6</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>3,4,3,-,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.4 | 1.2 | 21.1 |
| Tari Eason (HOU) | 99% | 25.5<br><sub>19,22,33,30,27</sub> | 10.0<br><sub>12,6,14,25,7</sub> |  | 6.2<br><sub>5,3,11,7,7</sub> |  | 1.4<br><sub>2,0,2,1,3</sub> |  | 1.1<br><sub>2,0,2,3,0</sub> |  | 1.3 | 0.6 | 1.1 | 17.6 |
| Reed Sheppard (HOU) | 91% | 19.5<br><sub>17,20,19,26,19</sub> | 8.8<br><sub>8,13,0,11,5</sub> |  | 1.8<br><sub>0,1,0,1,2</sub> |  | 2.4<br><sub>0,1,3,6,2</sub> |  | 1.5<br><sub>2,3,0,3,1</sub> |  | 1.2 | 0.4 | 0.9 | 12.9 |
| Marcus Smart (HOU) | 52% | 16.9<br><sub>17,17,-,-,-</sub> | 5.9<br><sub>5,6,-,-,-</sub> |  | 1.9<br><sub>2,2,-,-,-</sub> |  | 1.8<br><sub>2,1,-,-,-</sub> |  | 0.8<br><sub>1,2,-,-,-</sub> |  | 1.0 | 0.2 | 1.1 | 9.6 |
| Bogdan Bogdanovic (HOU) | 98% | 14.5<br><sub>12,10,12,22,26</sub> | 5.2<br><sub>8,0,11,12,6</sub> |  | 1.7<br><sub>3,0,1,3,0</sub> |  | 1.3<br><sub>1,0,3,4,1</sub> |  | 0.8<br><sub>2,0,3,2,2</sub> |  | 0.5 | 0.1 | 0.6 | 8.2 |
| Steven Adams (HOU) | 38% | 12.4<br><sub>-,-,-,12,-</sub> | 3.4<br><sub>-,-,-,6,-</sub> |  | 4.8<br><sub>-,-,-,7,-</sub> |  | 0.8<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.4 | 0.7 | 9.0 |
| Isaiah Crawford (HOU) | 67% | 9.7<br><sub>1,1,-,9,21</sub> | 3.2<br><sub>0,0,-,4,11</sub> |  | 2.1<br><sub>0,0,-,2,10</sub> |  | 0.5<br><sub>0,0,-,0,3</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.3 | 0.3 | 0.3 | 5.8 |
| Oscar Tshiebwe (HOU) | 96% | 8.1<br><sub>-,1,6,12,6</sub> | 3.4<br><sub>-,0,0,4,6</sub> |  | 3.7<br><sub>-,0,5,9,6</sub> |  | 0.5<br><sub>-,0,0,3,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 7.7 |
| Jae'Sean Tate (HOU) | 63% | 7.3<br><sub>-,1,-,8,12</sub> | 2.3<br><sub>-,0,-,4,3</sub> |  | 1.8<br><sub>-,0,-,2,3</sub> |  | 0.5<br><sub>-,0,-,0,2</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.6 |
| Bruce Thornton (HOU) | 67% | 7.0<br><sub>1,3,-,6,12</sub> | 3.3<br><sub>0,0,-,2,7</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.5<br><sub>0,0,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Pascal Siakam (IND) | 91% | 34.0<br><sub>32,35,32,32,34</sub> | 23.8<br><sub>23,29,28,19,31</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>2,9,8,3,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>5,8,5,2,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,5,2,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 0.3 | 2.2 | 34.1 |
| Aaron Nesmith (IND) | 91% | 31.2<br><sub>27,34,22,33,36</sub> | 14.8<br><sub>8,18,2,18,12</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>5,2,1,7,4</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,2,1,1,4</sub> |  | 2.0<br><sub>2,4,0,2,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.5 | 1.5 | 20.6 |
| Kelly Oubre Jr. (IND) | 88% | 28.9<br><sub>16,23,34,30,29</sub> | 12.6<br><sub>2,14,14,16,16</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>1,2,6,5,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,2,1,0,2</sub> |  | 1.2<br><sub>0,1,0,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.6 | 1.2 | 18.1 |
| Quenton Jackson (IND) | 98% | 26.8<br><sub>17,25,21,20,30</sub> | 12.5<br><sub>6,10,4,3,15</sub> |  | 3.5<br><sub>4,5,2,5,6</sub> |  | 4.3<br><sub>1,4,2,4,8</sub> |  | 1.2<br><sub>0,2,1,1,1</sub> |  | 1.2 | 0.2 | 1.6 | 20.3 |
| Ivica Zubac (IND) | 80% | 26.4<br><sub>19,28,31,26,22</sub> | 11.7<br><sub>10,16,20,12,8</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 9.1<br><sub>12,3,12,13,5</sub> | 9.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>5,0,1,1,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 1.4 | 22.6 |
| Obi Toppin (IND) | 88% | 18.8<br><sub>22,19,16,16,14</sub> | 10.6<br><sub>10,10,8,9,5</sub> |  | 3.9<br><sub>7,2,3,3,2</sub> |  | 1.7<br><sub>2,4,1,1,1</sub> |  | 1.3<br><sub>2,0,2,1,0</sub> |  | 0.5 | 0.2 | 1.0 | 16.1 |
| T.J. McConnell (IND) | 91% | 17.8<br><sub>9,8,14,17,19</sub> | 9.3<br><sub>6,2,7,6,12</sub> |  | 2.5<br><sub>2,0,3,3,5</sub> |  | 5.5<br><sub>1,3,7,7,5</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.2 | 1.4 | 17.3 |
| Jarace Walker (IND) | 83% | 17.7<br><sub>20,10,7,-,14</sub> | 7.3<br><sub>9,7,1,-,2</sub> |  | 3.8<br><sub>5,1,1,-,5</sub> |  | 1.7<br><sub>2,0,0,-,2</sub> |  | 0.9<br><sub>1,2,0,-,0</sub> |  | 0.6 | 0.3 | 1.0 | 12.8 |
| Jay Huff (IND) | 88% | 16.6<br><sub>10,-,11,8,18</sub> | 7.4<br><sub>0,-,6,8,11</sub> |  | 3.0<br><sub>3,-,4,1,0</sub> |  | 1.1<br><sub>0,-,0,0,2</sub> |  | 0.9<br><sub>0,-,0,2,3</sub> |  | 0.4 | 1.1 | 0.7 | 11.5 |
| Kobe Brown (IND) | 80% | 14.7<br><sub>-,-,-,-,3</sub> | 5.4<br><sub>-,-,-,-,0</sub> |  | 2.4<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.1 |
| Jalen Slawson (IND) | 88% | 14.2<br><sub>12,-,12,10,14</sub> | 4.3<br><sub>4,-,2,1,8</sub> |  | 2.8<br><sub>1,-,3,4,5</sub> |  | 1.2<br><sub>2,-,1,0,2</sub> |  | 0.3<br><sub>0,-,0,0,1</sub> |  | 0.7 | 0.6 | 0.6 | 8.3 |
| Braden Smith (IND) | 58% | 13.0<br><sub>12,10,-,-,-</sub> | 4.2<br><sub>0,0,-,-,-</sub> |  | 1.0<br><sub>0,0,-,-,-</sub> |  | 2.3<br><sub>2,0,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.8 | 7.5 |
| Larry Nance Jr. (IND) | 96% | 12.4<br><sub>13,14,5,14,7</sub> | 3.9<br><sub>15,4,5,2,4</sub> |  | 2.3<br><sub>2,0,0,2,2</sub> |  | 0.8<br><sub>1,0,0,1,2</sub> |  | 0.4<br><sub>5,0,1,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.0 |

</details>


### MIL @ MIA
Out: Myron Gardner (MIA), Ousmane Dieng (MIL), Kam Jones (MIL), Pete Nance (MIL), Ryan Rollins (MIL), Cormac Ryan (MIL)

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 32.4<br><sub>27,-,35,34,20</sub> | 21.7<br><sub>13,-,27,18,5</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>1,-,2,1,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>2,-,7,2,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>1,-,2,2,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.3 | 2.5 | 31.6 |
| Jaime Jaquez Jr. | 98% | 30.7<br><sub>23,25,30,28,30</sub> | 17.0<br><sub>4,16,25,22,6</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 6.0<br><sub>2,5,5,6,5</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 4.6<br><sub>2,3,3,4,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>0,2,2,5,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 2.6 | 27.6 |
| Kyle Kuzma | 98% | 28.7<br><sub>31,26,24,31,22</sub> | 13.7<br><sub>27,5,9,14,14</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>4,5,1,4,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.3<br><sub>0,3,1,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>6,1,1,1,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.7 | 0.4 | 2.1 | 22.4 |
| Myles Turner | 98% | 28.3<br><sub>24,27,-,31,23</sub> | 10.6<br><sub>3,3,-,14,8</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>5,3,-,11,7</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>7,2,-,3,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.6<br><sub>0,1,-,4,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 1.5 | 1.6 | 19.1 |
| Brayden Burries | 98% | 27.0<br><sub>29,26,23,19,29</sub> | 10.9<br><sub>13,3,8,3,13</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>8,3,5,4,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>4,3,1,3,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.3 | 1.5 | 20.5 |
| Kel'el Ware | 97% | 21.6<br><sub>9,17,23,17,25</sub> | 9.6<br><sub>0,8,8,10,8</sub> |  | 7.9<br><sub>0,4,5,6,11</sub> |  | 1.2<br><sub>1,1,1,1,2</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 0.6 | 1.3 | 1.5 | 18.7 |
| Gary Trent Jr. | 67% | 21.4<br><sub>-,6,4,16,30</sub> | 9.9<br><sub>-,5,6,1,18</sub> |  | 1.4<br><sub>-,0,1,0,2</sub> |  | 1.1<br><sub>-,0,0,0,1</sub> |  | 1.7<br><sub>-,1,2,0,4</sub> |  | 0.7 | 0.1 | 0.8 | 12.5 |
| Kasparas Jakucionis | 80% | 21.1<br><sub>7,23,4,-,26</sub> | 9.0<br><sub>1,11,4,-,25</sub> |  | 2.9<br><sub>2,0,2,-,5</sub> |  | 3.8<br><sub>0,4,0,-,5</sub> |  | 1.1<br><sub>0,2,0,-,4</sub> |  | 0.8 | 0.2 | 1.8 | 15.7 |
| Nate Ament | 96% | 20.8<br><sub>23,22,22,22,17</sub> | 8.3<br><sub>12,10,2,9,5</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>5,2,4,3,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>1,1,1,1,1</sub> |  | 1.0<br><sub>2,2,0,2,1</sub> |  | 0.7 | 0.3 | 1.1 | 12.6 |
| AJ Green | 98% | 17.1<br><sub>18,8,8,8,6</sub> | 6.2<br><sub>5,0,3,0,0</sub> |  | 1.8<br><sub>1,0,1,0,0</sub> |  | 1.3<br><sub>1,0,1,2,0</sub> |  | 1.1<br><sub>1,0,1,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 9.2 |
| Caris LeVert | 8% | 16.2<br><sub>-,-,-,-,-</sub> | 6.1<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.5 | 1.0 | 10.4 |
| Jericho Sims | 71% | 13.1<br><sub>15,8,18,-,11</sub> | 2.7<br><sub>2,2,0,-,4</sub> |  | 3.5<br><sub>2,0,4,-,2</sub> |  | 0.9<br><sub>0,0,1,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.8 | 7.1 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 35.1<br><sub>40,38,39,32,33</sub> | 14.6<br><sub>17,19,22,15,16</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>3,5,5,4,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 9.3<br><sub>11,8,17,9,10</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>2,3,3,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.3 | 2.0 | 27.3 |
| Bam Adebayo | 98% | 33.2<br><sub>34,37,38,36,16</sub> | 19.8<br><sub>18,11,37,20,4</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>8,8,14,5,1</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>4,4,3,4,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>1,0,2,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.6 | 0.7 | 1.4 | 33.0 |
| Giannis Antetokounmpo | 98% | 33.1<br><sub>34,31,31,31,29</sub> | 28.7<br><sub>29,30,37,34,20</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 13.2<br><sub>14,11,9,14,13</sub> | 12.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>3,4,2,8,6</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 0.5<br><sub>0,1,1,1,0</sub> |  | 1.0 | 1.1 | 2.9 | 47.6 |
| Andrew Wiggins | 98% | 28.3<br><sub>32,19,32,23,34</sub> | 11.9<br><sub>6,13,8,10,17</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>3,0,3,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,0,4,1,1</sub> |  | 1.7<br><sub>2,2,1,0,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.9 | 1.1 | 17.9 |
| Pelle Larsson | 76% | 27.2<br><sub>22,31,-,-,-</sub> | 10.9<br><sub>11,14,-,-,-</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,7,-,-,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,2,-,-,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>3,2,-,-,-</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.0 | 0.2 | 1.4 | 17.9 |
| Klay Thompson | 88% | 23.7<br><sub>32,30,-,20,22</sub> | 12.6<br><sub>23,11,-,26,17</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>2,1,-,1,0</sub> |  | 1.8<br><sub>4,2,-,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>7,2,-,6,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.5 | 0.6 | 0.9 | 16.4 |
| Ryan Conwell | 91% | 22.6<br><sub>19,21,33,26,30</sub> | 9.1<br><sub>6,5,20,9,14</sub> |  | 2.7<br><sub>2,4,5,4,2</sub> |  | 1.8<br><sub>2,2,2,1,3</sub> |  | 1.4<br><sub>2,1,4,2,1</sub> |  | 0.7 | 0.2 | 0.9 | 13.5 |
| Bobby Portis | 98% | 19.3<br><sub>20,17,15,18,23</sub> | 8.8<br><sub>4,5,5,7,16</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>1,1,3,4,6</sub> |  | 1.4<br><sub>1,1,2,2,0</sub> |  | 1.2<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.3 | 0.6 | 15.4 |
| Simone Fontecchio | 67% | 12.3<br><sub>-,7,7,14,19</sub> | 6.3<br><sub>-,3,0,7,10</sub> |  | 2.3<br><sub>-,0,0,5,6</sub> |  | 1.0<br><sub>-,0,2,0,2</sub> |  | 1.0<br><sub>-,0,0,1,2</sub> |  | 0.4 | 0.1 | 0.5 | 9.7 |
| Tim Hardaway Jr. | 58% | 11.8<br><sub>7,-,20,-,-</sub> | 5.1<br><sub>0,-,4,-,-</sub> |  | 1.4<br><sub>0,-,3,-,-</sub> |  | 0.7<br><sub>0,-,2,-,-</sub> |  | 0.7<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 7.2 |
| Nikola Jovic | 52% | 10.8<br><sub>-,-,-,11,-</sub> | 4.1<br><sub>-,-,-,2,-</sub> |  | 2.1<br><sub>-,-,-,1,-</sub> |  | 1.2<br><sub>-,-,-,2,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.4 |
| Dru Smith | 48% | 8.8<br><sub>-,-,6,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,1,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.7 | 0.2 | 0.4 | 5.6 |
| Keshad Johnson | 63% | 7.2<br><sub>-,-,-,1,3</sub> | 3.5<br><sub>-,-,-,0,0</sub> |  | 1.7<br><sub>-,-,-,0,2</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.5 |
| Nick Richards | 52% | 6.2<br><sub>-,-,-,-,3</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 2.3<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.1 | 0.3 | 0.4 | 5.1 |
| Tre Donaldson | 67% | 5.6<br><sub>-,-,-,1,3</sub> | 2.2<br><sub>-,-,-,2,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 2.9 |

</details>


### PHI @ ORL
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Dominick Barlow (PHI), Adem Bona (PHI), Jaylen Brown (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.4–111.5 | PHI 47% | 2.11 / 1.90 | ORL -1.5 | 221.5 | ORL +1.5 covers 56%; o221.5 51% |
| Expected (weighted by chance each plays) | 111.0–111.6 | PHI 49% | 2.05 / 1.96 | ORL +0.5 | 222.5 | ORL +1.5 covers 54%; o221.5 52% |
| if Dean Wade plays | 111.5–111.8 | PHI 49% | 2.03 / 1.97 | ORL +0.5 | 223.5 | ORL +1.5 covers 54%; o221.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dean Wade (PHI) | Questionable | 55% | 30.0 | 5.5 | 5.1 | 1.5 | 0.9 | 1.1 | 0.5 | 0.8 | 12.1 | full tables below |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 99% | 39.3<br><sub>36,34,35,36,35</sub> | 26.8<br><sub>27,24,27,27,24</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,1,2,4,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>7,4,8,6,9</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>3,3,1,5,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.6 | 2.6 | 36.5 |
| VJ Edgecombe | 96% | 37.3<br><sub>35,32,36,31,33</sub> | 14.4<br><sub>13,8,15,11,14</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>6,4,8,4,9</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 3.7<br><sub>3,5,8,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>3,0,1,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.6 | 0.5 | 1.6 | 24.4 |
| LeBron James | 98% | 36.3<br><sub>33,29,-,33,-</sub> | 19.5<br><sub>22,11,-,15,-</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>5,8,-,7,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.4<br><sub>5,5,-,11,-</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>2,1,-,0,-</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.7 | 3.3 | 33.1 |
| Joel Embiid | 98% | 35.0<br><sub>29,31,28,-,32</sub> | 25.0<br><sub>18,16,20,-,37</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 8.6<br><sub>10,6,4,-,5</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>5,1,3,-,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,0,-,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 1.2 | 3.3 | 37.9 |
| Kentavious Caldwell-Pope | 99% | 29.9<br><sub>21,16,27,22,31</sub> | 6.9<br><sub>6,0,11,9,0</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>6,0,4,5,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>3,2,5,0,3</sub> |  | 1.1<br><sub>2,0,3,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.4 | 0.9 | 12.2 |
| Anfernee Simons | 98% | 28.8<br><sub>16,18,23,15,26</sub> | 12.2<br><sub>3,17,17,12,9</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>4,3,3,0,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>1,3,5,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.2 | 1.1 | 16.6 |
| Jabari Walker | 91% | 21.7<br><sub>19,15,16,25,16</sub> | 8.0<br><sub>9,2,9,11,12</sub> |  | 6.0<br><sub>11,4,8,7,5</sub> |  | 1.0<br><sub>0,0,1,1,1</sub> |  | 0.8<br><sub>1,0,1,3,1</sub> |  | 0.7 | 0.3 | 0.8 | 14.9 |
| Rayan Rupert | 38% | 13.5<br><sub>-,6,-,-,-</sub> | 4.3<br><sub>-,0,-,-,-</sub> |  | 2.6<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.7 | 0.2 | 0.8 | 7.8 |
| Justin Edwards | 52% | 12.0<br><sub>-,6,1,-,-</sub> | 4.2<br><sub>-,0,0,-,-</sub> |  | 1.6<br><sub>-,0,1,-,-</sub> |  | 0.6<br><sub>-,0,0,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.5 | 0.2 | 0.5 | 6.4 |
| Tacko Fall | 58% | 11.6<br><sub>-,-,1,5,-</sub> | 0.6<br><sub>-,-,0,0,-</sub> |  | 2.9<br><sub>-,-,0,3,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.6 | 0.5 | 3.9 |
| Labaron Philon Jr. | 63% | 11.5<br><sub>-,6,2,6,-</sub> | 3.9<br><sub>-,2,0,3,-</sub> |  | 1.5<br><sub>-,1,0,1,-</sub> |  | 0.9<br><sub>-,3,0,0,-</sub> |  | 0.3<br><sub>-,0,0,1,-</sub> |  | 0.4 | 0.1 | 0.6 | 6.3 |
| Caleb Love | 38% | 11.4<br><sub>-,-,1,-,-</sub> | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.7<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 1.7 |

</details>

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 33.3<br><sub>40,38,39,36,38</sub> | 23.6<br><sub>30,33,38,35,21</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>6,7,8,9,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>11,7,1,12,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>3,1,3,3,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.4 | 2.8 | 36.0 |
| Desmond Bane | 98% | 32.7<br><sub>-,36,34,35,39</sub> | 18.4<br><sub>-,15,25,21,24</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>-,6,3,5,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>-,4,2,3,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>-,4,7,6,3</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.4 | 1.8 | 25.8 |
| Anthony Black | 98% | 30.4<br><sub>38,33,39,37,33</sub> | 14.4<br><sub>18,26,22,5,20</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>8,7,7,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>6,5,8,5,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,2,3,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.7 | 2.2 | 22.9 |
| Wendell Carter Jr. | 98% | 29.1<br><sub>40,33,28,30,28</sub> | 11.7<br><sub>19,8,9,12,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>11,11,7,8,3</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>0,1,3,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8<br><sub>3,0,0,1,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.8 | 1.3 | 21.1 |
| Jalen Suggs | 98% | 27.3<br><sub>-,-,-,21,25</sub> | 11.1<br><sub>-,-,-,3,12</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>-,-,-,2,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>-,-,-,3,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>-,-,-,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.6 | 2.3 | 19.1 |
| Tristan da Silva | 88% | 26.9<br><sub>39,-,-,31,31</sub> | 12.2<br><sub>19,-,-,12,13</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 4.1<br><sub>7,-,-,6,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,-,-,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>5,-,-,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.3 | 1.0 | 18.1 |
| Goga Bitadze | 91% | 14.5<br><sub>7,15,20,18,20</sub> | 5.4<br><sub>4,2,4,12,10</sub> |  | 5.0<br><sub>5,2,7,4,6</sub> |  | 1.2<br><sub>2,1,0,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.7 | 11.6 |
| Jamal Cain | 88% | 14.5<br><sub>36,20,-,4,15</sub> | 5.9<br><sub>18,5,-,0,2</sub> |  | 2.9<br><sub>12,3,-,4,5</sub> |  | 0.7<br><sub>1,1,-,1,0</sub> |  | 0.6<br><sub>2,1,-,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.4 |
| Jevon Carter | 88% | 13.2<br><sub>15,4,28,17,12</sub> | 5.1<br><sub>9,0,11,5,3</sub> |  | 1.3<br><sub>1,0,3,2,2</sub> |  | 1.4<br><sub>0,0,4,2,1</sub> |  | 0.7<br><sub>3,0,3,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 7.8 |
| Jase Richardson | 63% | 12.4<br><sub>30,15,20,-,-</sub> | 4.7<br><sub>2,6,6,-,-</sub> |  | 1.4<br><sub>4,1,1,-,-</sub> |  | 1.3<br><sub>4,1,2,-,-</sub> |  | 0.4<br><sub>0,0,1,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 7.4 |
| Nikola Vucevic | 76% | 8.8<br><sub>6,18,14,11,-</sub> | 3.7<br><sub>0,5,3,2,-</sub> |  | 2.5<br><sub>1,4,5,3,-</sub> |  | 1.0<br><sub>2,1,1,0,-</sub> |  | 0.3<br><sub>0,1,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 7.2 |
| Alex Morales | 58% | 7.0<br><sub>15,29,18,-,-</sub> | 1.7<br><sub>0,7,5,-,-</sub> |  | 1.2<br><sub>2,7,4,-,-</sub> |  | 0.5<br><sub>1,0,3,-,-</sub> |  | 0.1<br><sub>0,1,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |
| Colin Castleton | 48% | 5.8<br><sub>-,-,1,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 1.8<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.4 |

</details>

<details><summary>if Dean Wade plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner (ORL) | 98% | 33.3<br><sub>40,38,39,36,38</sub> | 23.6<br><sub>30,33,38,35,21</sub> | 25.5 · –<br><sub>o 46% · u 54%</sub> | 6.1<br><sub>6,7,8,9,8</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>11,7,1,12,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>3,1,3,3,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.4 | 2.8 | 36.0 |
| Desmond Bane (ORL) | 98% | 32.7<br><sub>-,36,34,35,39</sub> | 18.4<br><sub>-,15,25,21,24</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>-,6,3,5,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>-,4,2,3,5</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>-,4,7,6,3</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.4 | 1.9 | 25.9 |
| Anthony Black (ORL) | 98% | 30.3<br><sub>38,33,39,37,33</sub> | 14.4<br><sub>18,26,22,5,20</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>8,7,7,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>6,5,8,5,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,2,3,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.7 | 2.2 | 22.9 |
| Wendell Carter Jr. (ORL) | 98% | 29.0<br><sub>40,33,28,30,28</sub> | 11.7<br><sub>19,8,9,12,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.6<br><sub>11,11,7,8,3</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>0,1,3,0,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8<br><sub>3,0,0,1,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.8 | 1.3 | 21.0 |
| Jalen Suggs (ORL) | 98% | 27.3<br><sub>-,-,-,21,25</sub> | 11.1<br><sub>-,-,-,3,12</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>-,-,-,2,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>-,-,-,3,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.6<br><sub>-,-,-,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.6 | 2.3 | 19.0 |
| Tristan da Silva (ORL) | 88% | 27.0<br><sub>39,-,-,31,31</sub> | 12.3<br><sub>19,-,-,12,13</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>7,-,-,6,6</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,-,-,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>5,-,-,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.3 | 1.0 | 18.2 |
| Goga Bitadze (ORL) | 91% | 14.6<br><sub>7,15,20,18,20</sub> | 5.5<br><sub>4,2,4,12,10</sub> |  | 5.0<br><sub>5,2,7,4,6</sub> |  | 1.2<br><sub>2,1,0,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 0.7 | 11.7 |
| Jamal Cain (ORL) | 88% | 14.5<br><sub>36,20,-,4,15</sub> | 5.9<br><sub>18,5,-,0,2</sub> |  | 2.9<br><sub>12,3,-,4,5</sub> |  | 0.7<br><sub>1,1,-,1,0</sub> |  | 0.6<br><sub>2,1,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 9.4 |
| Jevon Carter (ORL) | 88% | 13.2<br><sub>15,4,28,17,12</sub> | 5.1<br><sub>9,0,11,5,3</sub> |  | 1.3<br><sub>1,0,3,2,2</sub> |  | 1.4<br><sub>0,0,4,2,1</sub> |  | 0.7<br><sub>3,0,3,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 7.8 |
| Jase Richardson (ORL) | 63% | 12.4<br><sub>30,15,20,-,-</sub> | 4.7<br><sub>2,6,6,-,-</sub> |  | 1.4<br><sub>4,1,1,-,-</sub> |  | 1.3<br><sub>4,1,2,-,-</sub> |  | 0.4<br><sub>0,0,1,-,-</sub> |  | 0.4 | 0.2 | 0.5 | 7.4 |
| Nikola Vucevic (ORL) | 76% | 8.7<br><sub>6,18,14,11,-</sub> | 3.6<br><sub>0,5,3,2,-</sub> |  | 2.5<br><sub>1,4,5,3,-</sub> |  | 0.9<br><sub>2,1,1,0,-</sub> |  | 0.3<br><sub>0,1,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 7.1 |
| Alex Morales (ORL) | 58% | 7.1<br><sub>15,29,18,-,-</sub> | 1.7<br><sub>0,7,5,-,-</sub> |  | 1.3<br><sub>2,7,4,-,-</sub> |  | 0.5<br><sub>1,0,3,-,-</sub> |  | 0.1<br><sub>0,1,1,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.5 |
| Colin Castleton (ORL) | 48% | 5.8<br><sub>-,-,1,-,-</sub> | 2.1<br><sub>-,-,0,-,-</sub> |  | 1.8<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.4 |
| Tyrese Maxey (PHI) | 99% | 38.1<br><sub>36,34,35,36,35</sub> | 26.2<br><sub>27,24,27,27,24</sub> | 25.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>4,1,2,4,1</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>7,4,8,6,9</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>3,3,1,5,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.6 | 2.6 | 35.6 |
| VJ Edgecombe (PHI) | 96% | 35.9<br><sub>35,32,36,31,33</sub> | 14.6<br><sub>13,8,15,11,14</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>6,4,8,4,9</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 3.7<br><sub>3,5,8,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,0,1,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.5 | 0.5 | 1.6 | 24.2 |
| LeBron James (PHI) | 98% | 34.9<br><sub>33,29,-,33,-</sub> | 18.7<br><sub>22,11,-,15,-</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>5,8,-,7,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>5,5,-,11,-</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>2,1,-,0,-</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.7 | 3.3 | 31.9 |
| Joel Embiid (PHI) | 98% | 33.5<br><sub>29,31,28,-,32</sub> | 24.1<br><sub>18,16,20,-,37</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 8.2<br><sub>10,6,4,-,5</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 4.0<br><sub>5,1,3,-,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,0,-,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 1.1 | 3.2 | 36.2 |
| Dean Wade (PHI) | 100% | 30.0<br><sub>18,23,34,35,32</sub> | 5.5<br><sub>0,8,6,12,8</sub> | 5.5 · – | 5.1<br><sub>1,9,5,7,11</sub> | 4.5 | 1.5<br><sub>1,0,2,3,1</sub> | 1.5 | 0.9<br><sub>0,2,2,3,1</sub> | 1.5 | 1.1 | 0.5 | 0.8 | 12.1 |
| Kentavious Caldwell-Pope (PHI) | 99% | 26.5<br><sub>21,16,27,22,31</sub> | 6.6<br><sub>6,0,11,9,0</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>6,0,4,5,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>3,2,5,0,3</sub> |  | 1.0<br><sub>2,0,3,2,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.4 | 0.8 | 11.3 |
| Anfernee Simons (PHI) | 98% | 24.9<br><sub>16,18,23,15,26</sub> | 11.1<br><sub>3,17,17,12,9</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>4,3,3,0,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>1,3,5,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.2 | 1.1 | 15.0 |
| Jabari Walker (PHI) | 91% | 16.5<br><sub>19,15,16,25,16</sub> | 6.5<br><sub>9,2,9,11,12</sub> |  | 4.5<br><sub>11,4,8,7,5</sub> |  | 0.7<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>1,0,1,3,1</sub> |  | 0.5 | 0.2 | 0.7 | 11.7 |
| Rayan Rupert (PHI) | 38% | 9.0<br><sub>-,6,-,-,-</sub> | 3.0<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.1 | 0.6 | 5.3 |
| Labaron Philon Jr. (PHI) | 63% | 8.2<br><sub>-,6,2,6,-</sub> | 3.0<br><sub>-,2,0,3,-</sub> |  | 1.1<br><sub>-,1,0,1,-</sub> |  | 0.7<br><sub>-,3,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.8 |
| Tacko Fall (PHI) | 58% | 8.0<br><sub>-,-,1,5,-</sub> | 0.4<br><sub>-,-,0,0,-</sub> |  | 2.0<br><sub>-,-,0,3,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.2 | 0.4 | 0.3 | 2.8 |
| Caleb Love (PHI) | 38% | 7.7<br><sub>-,-,1,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.1 |
| Justin Edwards (PHI) | 52% | 7.6<br><sub>-,6,1,-,-</sub> | 2.9<br><sub>-,0,0,-,-</sub> |  | 1.0<br><sub>-,0,1,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.3 |

</details>


### CHI @ BKN
Out: Grant Nelson (BKN), Drake Powell (BKN), Ben Saraf (BKN), Tobe Awaka (CHI), Orlando Robinson (CHI), Caleb Wilson (CHI)

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Norman Powell | 98% | 30.6<br><sub>-,-,31,30,33</sub> | 21.2<br><sub>-,-,33,24,27</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>-,-,5,5,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.7<br><sub>-,-,2,3,6</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>-,-,4,3,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.3 | 2.3 | 27.1 |
| Matas Buzelis | 98% | 29.2<br><sub>31,31,29,30,31</sub> | 17.5<br><sub>19,13,11,18,23</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>5,3,6,9,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>2,2,2,2,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.1<br><sub>3,3,3,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 1.1 | 2.5 | 25.0 |
| Josh Giddey | 98% | 29.0<br><sub>34,25,39,26,24</sub> | 12.7<br><sub>19,9,15,8,4</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>7,2,10,8,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 8.1<br><sub>15,7,14,5,8</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>1,1,3,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.7 | 3.0 | 27.1 |
| Jalen Smith | 98% | 27.9<br><sub>30,30,32,-,28</sub> | 14.5<br><sub>17,23,15,-,17</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 8.7<br><sub>8,4,12,-,11</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,3,3,-,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.8<br><sub>2,5,1,-,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 1.1 | 1.2 | 25.1 |
| Isaac Okoro | 98% | 27.8<br><sub>25,23,41,31,32</sub> | 9.4<br><sub>12,0,15,9,13</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,3,7,6</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.9<br><sub>1,4,2,4,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.0 | 14.2 |
| Tre Jones | 98% | 20.3<br><sub>14,28,15,24,23</sub> | 11.1<br><sub>6,13,4,16,16</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>1,1,1,0,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>1,3,3,4,6</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.4<br><sub>0,1,0,1,0</sub> |  | 1.0 | 0.2 | 1.4 | 17.2 |
| Patrick Williams | 74% | 20.3<br><sub>25,28,24,26,13</sub> | 7.1<br><sub>7,9,13,14,0</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>3,7,4,5,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>3,4,2,1,0</sub> |  | 0.9<br><sub>1,0,4,2,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 0.4 | 1.0 | 11.5 |
| Nic Claxton | 98% | 18.0<br><sub>18,16,22,-,17</sub> | 7.2<br><sub>4,17,2,-,8</sub> |  | 4.8<br><sub>4,6,6,-,2</sub> |  | 2.0<br><sub>4,1,2,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.6 | 0.8 | 0.9 | 13.9 |
| Buddy Hield | 76% | 16.8<br><sub>-,-,25,20,19</sub> | 8.2<br><sub>-,-,12,16,6</sub> |  | 2.4<br><sub>-,-,3,4,4</sub> |  | 1.7<br><sub>-,-,3,2,2</sub> |  | 1.3<br><sub>-,-,2,4,2</sub> |  | 0.7 | 0.2 | 1.0 | 12.2 |
| Noa Essengue | 96% | 12.3<br><sub>15,11,8,7,14</sub> | 4.9<br><sub>10,8,5,0,1</sub> |  | 2.6<br><sub>7,4,1,1,2</sub> |  | 0.7<br><sub>1,3,1,0,1</sub> |  | 0.4<br><sub>0,1,1,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.2 |
| Zach Collins | 58% | 11.9<br><sub>-,3,-,28,-</sub> | 5.1<br><sub>-,2,-,8,-</sub> |  | 3.5<br><sub>-,2,-,5,-</sub> |  | 1.2<br><sub>-,1,-,4,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.3 | 0.7 | 9.8 |
| Leonard Miller | 76% | 10.9<br><sub>-,2,-,17,1</sub> | 5.1<br><sub>-,0,-,4,0</sub> |  | 2.6<br><sub>-,0,-,3,0</sub> |  | 0.7<br><sub>-,0,-,4,0</sub> |  | 0.4<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 8.5 |
| Jordan Hawkins | 63% | 8.8<br><sub>17,24,-,-,4</sub> | 3.8<br><sub>9,7,-,-,0</sub> |  | 1.1<br><sub>0,4,-,-,0</sub> |  | 0.6<br><sub>1,2,-,-,1</sub> |  | 0.3<br><sub>1,1,-,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |
| Dailyn Swain | 63% | 6.0<br><sub>-,-,-,-,2</sub> | 2.5<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 4.0 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Michael Porter Jr. | 83% | 33.3<br><sub>36,29,28,-,40</sub> | 23.0<br><sub>25,19,22,-,25</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>9,9,6,-,6</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>1,0,3,-,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 3.2<br><sub>3,4,4,-,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.1 | 32.6 |
| Julius Randle | 98% | 32.4<br><sub>34,30,29,31,34</sub> | 20.8<br><sub>19,13,17,22,33</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 6.8<br><sub>7,4,4,4,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>8,4,5,5,1</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>1,0,0,3,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 3.0 | 32.1 |
| Egor Demin | 98% | 24.2<br><sub>-,-,23,27,26</sub> | 10.6<br><sub>-,-,22,11,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>-,-,1,1,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.1<br><sub>-,-,1,2,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>-,-,4,3,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.3 | 1.5 | 16.6 |
| Day'Ron Sharpe | 98% | 24.1<br><sub>32,20,19,28,25</sub> | 10.9<br><sub>12,6,15,16,6</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 8.7<br><sub>10,4,4,11,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>13,6,5,5,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.3<br><sub>0,0,2,0,0</sub> |  | 1.2 | 1.1 | 1.8 | 23.4 |
| Nolan Traore | 98% | 24.0<br><sub>23,21,-,20,30</sub> | 12.7<br><sub>19,14,-,11,23</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>1,1,-,1,1</sub> |  | 3.5<br><sub>2,2,-,2,4</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.4<br><sub>2,2,-,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.5 | 2.1 | 18.5 |
| Noah Clowney | 98% | 21.6<br><sub>21,8,19,35,24</sub> | 9.0<br><sub>3,2,16,15,9</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>10,0,3,7,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>0,0,0,3,3</sub> |  | 1.2<br><sub>1,0,2,3,1</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.7 | 0.7 | 0.9 | 14.3 |
| Mikel Brown Jr. | 98% | 20.3<br><sub>25,-,-,20,18</sub> | 9.6<br><sub>18,-,-,6,3</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,-,-,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 3.4<br><sub>3,-,-,2,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>3,-,-,2,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.5 | 15.3 |
| Danny Wolf | 84% | 18.0<br><sub>31,36,29,28,11</sub> | 7.8<br><sub>11,10,10,14,3</sub> |  | 4.7<br><sub>9,3,11,6,2</sub> |  | 1.8<br><sub>1,2,4,1,1</sub> |  | 0.9<br><sub>2,1,1,4,1</sub> |  | 0.5 | 0.5 | 0.9 | 14.4 |
| Keon Ellis | 88% | 17.4<br><sub>-,22,26,7,20</sub> | 4.7<br><sub>-,3,11,0,8</sub> |  | 1.9<br><sub>-,1,4,0,2</sub> |  | 1.1<br><sub>-,4,3,1,0</sub> |  | 0.6<br><sub>-,1,2,0,2</sub> |  | 1.1 | 0.6 | 0.5 | 7.8 |
| Moritz Wagner | 97% | 15.0<br><sub>16,16,19,18,10</sub> | 8.7<br><sub>9,12,16,10,4</sub> |  | 4.0<br><sub>2,3,3,6,5</sub> |  | 1.2<br><sub>0,1,4,4,1</sub> |  | 0.7<br><sub>1,1,2,2,0</sub> |  | 0.5 | 0.2 | 0.8 | 13.9 |
| Terance Mann | 64% | 10.9<br><sub>13,22,18,9,-</sub> | 2.8<br><sub>0,0,6,2,-</sub> |  | 1.4<br><sub>2,1,1,1,-</sub> |  | 1.1<br><sub>0,1,3,1,-</sub> |  | 0.2<br><sub>0,0,2,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.3 |
| Chaney Johnson | 98% | 9.8<br><sub>8,15,15,12,1</sub> | 3.0<br><sub>5,2,4,1,0</sub> |  | 1.7<br><sub>2,0,3,5,0</sub> |  | 0.6<br><sub>1,1,2,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.2 |
| Josh Minott | 58% | 7.6<br><sub>-,12,7,2,-</sub> | 4.2<br><sub>-,10,0,0,-</sub> |  | 1.5<br><sub>-,2,2,0,-</sub> |  | 0.4<br><sub>-,1,0,0,-</sub> |  | 0.4<br><sub>-,2,0,0,-</sub> |  | 0.5 | 0.3 | 0.4 | 6.2 |

</details>


### WAS @ TOR
Out: Scottie Barnes (TOR), Kawhi Leonard (TOR), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 110.2–117.8 | WAS 29% | 3.42 / 1.41 | TOR -7.5 | 227.5 | TOR -4.5 covers 59%; o225.5 55% |
| Expected (weighted by chance each plays) | 110.9–118.9 | WAS 28% | 3.53 / 1.40 | TOR -8.5 | 229.5 | TOR -4.5 covers 61%; o225.5 59% |
| if RJ Barrett plays | 111.5–120.2 | WAS 26% | 3.77 / 1.36 | TOR -8.5 | 231.5 | TOR -4.5 covers 63%; o225.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Felix Okpara (WAS) | Questionable | 55% | 5.9 | 2.3 | 1.6 | 0.4 | 0.1 | 0.1 | 0.2 | 0.4 | 4.3 | small |
| RJ Barrett (TOR) | Questionable | 55% | 35.1 | 26.5 | 6.8 | 5.3 | 2.1 | 0.9 | 0.4 | 2.5 | 38.6 | full tables below |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 99% | 34.2<br><sub>38,34,45,26,33</sub> | 17.6<br><sub>20,15,37,0,13</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,3,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 8.8<br><sub>7,4,14,8,12</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,3,4,0,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 3.6 | 29.2 |
| Anthony Davis | 98% | 33.8<br><sub>34,34,44,31,35</sub> | 20.6<br><sub>44,21,30,14,23</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 10.6<br><sub>13,13,15,8,4</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>1,0,4,5,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 1.1 | 1.6 | 2.3 | 33.8 |
| AJ Dybantsa | 98% | 33.1<br><sub>37,34,44,30,32</sub> | 14.8<br><sub>21,13,5,16,21</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>8,4,8,7,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,2,4,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.5 | 2.4 | 23.1 |
| Kyshawn George | 99% | 32.5<br><sub>35,39,26,30,38</sub> | 15.4<br><sub>12,25,14,11,18</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>3,9,1,2,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>2,3,5,4,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>2,5,3,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 1.1 | 2.6 | 24.1 |
| Alex Sarr | 98% | 27.7<br><sub>25,25,44,27,31</sub> | 12.2<br><sub>4,5,30,25,6</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>8,8,9,9,4</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,0,2,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>0,1,4,3,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 1.3 | 1.5 | 21.3 |
| Tre Johnson | 96% | 21.3<br><sub>29,29,30,-,21</sub> | 8.7<br><sub>2,15,13,-,9</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,3,4,-,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>0,1,2,-,3</sub> |  | 1.2<br><sub>0,2,1,-,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.2 | 1.3 | 11.9 |
| Bilal Coulibaly | 98% | 20.9<br><sub>-,25,29,21,16</sub> | 7.4<br><sub>-,5,4,9,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>-,6,7,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>-,2,0,0,0</sub> |  | 0.7<br><sub>-,0,0,1,1</sub> |  | 0.8 | 0.7 | 1.1 | 11.8 |
| Khris Middleton | 52% | 13.1<br><sub>-,-,-,9,18</sub> | 4.7<br><sub>-,-,-,8,9</sub> |  | 2.0<br><sub>-,-,-,0,3</sub> |  | 1.2<br><sub>-,-,-,2,3</sub> |  | 0.4<br><sub>-,-,-,2,2</sub> |  | 0.4 | 0.1 | 1.0 | 7.8 |
| Deandre Ayton | 99% | 12.0<br><sub>13,9,9,10,8</sub> | 3.9<br><sub>2,2,2,2,4</sub> |  | 3.7<br><sub>8,2,4,1,0</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 8.0 |
| Bub Carrington | 99% | 11.8<br><sub>19,10,16,23,2</sub> | 3.7<br><sub>4,0,2,11,0</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 1.5<br><sub>4,0,2,4,0</sub> |  | 0.4<br><sub>1,0,0,3,0</sub> |  | 0.3 | 0.1 | 0.8 | 6.4 |
| Will Riley | 86% | 8.2<br><sub>4,-,3,16,2</sub> | 3.7<br><sub>0,-,3,14,2</sub> |  | 1.0<br><sub>0,-,0,3,1</sub> |  | 0.6<br><sub>1,-,0,0,0</sub> |  | 0.2<br><sub>0,-,1,2,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Anthony Gill | 58% | 7.2<br><sub>2,-,-,6,2</sub> | 2.7<br><sub>0,-,-,5,2</sub> |  | 1.2<br><sub>2,-,-,1,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Tre Mann | 63% | 6.0<br><sub>2,-,-,11,2</sub> | 2.6<br><sub>0,-,-,4,2</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.7<br><sub>0,-,-,1,1</sub> |  | 0.2<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Collin Murray-Boyles | 98% | 34.1<br><sub>-,20,32,40,33</sub> | 18.1<br><sub>-,5,14,6,8</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>-,4,0,13,1</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>-,3,4,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.5<br><sub>-,1,1,0,0</sub> |  | 1.6 | 1.5 | 2.3 | 29.4 |
| Immanuel Quickley | 88% | 33.2<br><sub>-,28,28,38,34</sub> | 22.2<br><sub>-,11,26,17,14</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>-,4,4,6,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>-,4,6,6,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>-,1,3,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.1 | 1.7 | 33.8 |
| Ja'Kobe Walter | 98% | 33.1<br><sub>34,35,32,36,33</sub> | 16.1<br><sub>12,17,6,7,25</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>6,3,5,2,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>0,1,0,1,2</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 2.6<br><sub>2,5,1,1,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.6 | 0.3 | 1.2 | 23.0 |
| Jamal Shead | 98% | 28.1<br><sub>36,22,22,26,20</sub> | 11.4<br><sub>20,3,5,19,7</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,3,1,2,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 8.0<br><sub>11,6,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>4,0,1,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.3 | 0.2 | 2.1 | 21.8 |
| Jakob Poeltl | 91% | 25.8<br><sub>31,32,25,17,18</sub> | 12.8<br><sub>18,6,9,11,3</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 8.8<br><sub>8,9,5,5,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.0 | 1.4 | 23.9 |
| Jamison Battle | 98% | 24.7<br><sub>29,25,25,8,7</sub> | 11.9<br><sub>18,12,13,0,0</sub> |  | 3.4<br><sub>1,2,1,3,1</sub> |  | 1.1<br><sub>2,0,1,0,0</sub> |  | 1.9<br><sub>5,2,3,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 16.4 |
| Allen Graves | 98% | 22.8<br><sub>13,18,13,16,13</sub> | 8.7<br><sub>3,13,0,2,3</sub> |  | 4.6<br><sub>2,5,2,5,2</sub> |  | 1.6<br><sub>1,0,0,3,1</sub> |  | 1.0<br><sub>1,3,0,0,1</sub> |  | 0.8 | 0.5 | 0.8 | 14.9 |
| Alijah Martin | 96% | 17.7<br><sub>21,16,18,12,8</sub> | 7.8<br><sub>2,12,7,2,0</sub> |  | 2.7<br><sub>3,1,4,3,2</sub> |  | 1.6<br><sub>3,0,1,0,0</sub> |  | 0.8<br><sub>0,4,1,0,0</sub> |  | 0.9 | 0.3 | 1.1 | 12.1 |
| Kyle Anderson | 52% | 15.8<br><sub>16,11,5,-,-</sub> | 5.4<br><sub>6,2,0,-,-</sub> |  | 3.1<br><sub>2,3,0,-,-</sub> |  | 3.0<br><sub>2,4,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.8 | 0.5 | 0.8 | 11.5 |
| Trayce Jackson-Davis | 52% | 15.0<br><sub>14,-,-,-,-</sub> | 6.3<br><sub>4,-,-,-,-</sub> |  | 5.2<br><sub>6,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.9 | 0.8 | 0.8 | 12.7 |
| Kevin McCullar Jr. | 16% | 12.3<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.1 | 0.8 | 8.0 |
| Malachi Smith | 96% | 12.1<br><sub>1,-,2,-,-</sub> | 4.6<br><sub>0,-,0,-,-</sub> |  | 2.0<br><sub>0,-,0,-,-</sub> |  | 1.8<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.6 | 8.4 |
| Jaden Bradley | 52% | 9.8<br><sub>9,-,2,-,-</sub> | 3.6<br><sub>0,-,1,-,-</sub> |  | 1.6<br><sub>1,-,0,-,-</sub> |  | 1.4<br><sub>3,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.6 |

</details>

<details><summary>if RJ Barrett plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| RJ Barrett (TOR) | 100% | 35.1<br><sub>36,31,37,37,39</sub> | 26.5<br><sub>19,12,31,14,22</sub> | 23.5 · – | 6.8<br><sub>3,8,14,5,5</sub> | 6.5 | 5.3<br><sub>2,7,5,6,5</sub> | 4.5 | 2.1<br><sub>1,0,4,0,2</sub> | 1.5 | 0.9 | 0.4 | 2.5 | 38.6 |
| Ja'Kobe Walter (TOR) | 98% | 32.1<br><sub>34,35,32,36,33</sub> | 14.0<br><sub>12,17,6,7,25</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>6,3,5,2,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,1,0,1,2</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 2.3<br><sub>2,5,1,1,7</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.5 | 0.3 | 1.0 | 20.2 |
| Immanuel Quickley (TOR) | 88% | 32.0<br><sub>-,28,28,38,34</sub> | 19.5<br><sub>-,11,26,17,14</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>-,4,4,6,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>-,4,6,6,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>-,1,3,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.4 | 0.1 | 1.6 | 30.4 |
| Collin Murray-Boyles (TOR) | 98% | 31.1<br><sub>-,20,32,40,33</sub> | 15.0<br><sub>-,5,14,6,8</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>-,4,0,13,1</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>-,3,4,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.5<br><sub>-,1,1,0,0</sub> |  | 1.4 | 1.4 | 1.8 | 25.0 |
| Jamal Shead (TOR) | 98% | 25.5<br><sub>36,22,22,26,20</sub> | 9.4<br><sub>20,3,5,19,7</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,3,1,2,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 7.2<br><sub>11,6,5,4,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>4,0,1,3,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 1.7 | 18.8 |
| Jakob Poeltl (TOR) | 91% | 23.5<br><sub>31,32,25,17,18</sub> | 11.0<br><sub>18,6,9,11,3</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.9<br><sub>8,9,5,5,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,1,3,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.8 | 1.2 | 21.0 |
| Jamison Battle (TOR) | 98% | 18.9<br><sub>29,25,25,8,7</sub> | 8.6<br><sub>18,12,13,0,0</sub> |  | 2.5<br><sub>1,2,1,3,1</sub> |  | 0.9<br><sub>2,0,1,0,0</sub> |  | 1.4<br><sub>5,2,3,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 11.9 |
| Allen Graves (TOR) | 98% | 16.7<br><sub>13,18,13,16,13</sub> | 5.7<br><sub>3,13,0,2,3</sub> |  | 3.3<br><sub>2,5,2,5,2</sub> |  | 1.1<br><sub>1,0,0,3,1</sub> |  | 0.6<br><sub>1,3,0,0,1</sub> |  | 0.6 | 0.3 | 0.6 | 10.2 |
| Alijah Martin (TOR) | 96% | 14.1<br><sub>21,16,18,12,8</sub> | 5.9<br><sub>2,12,7,2,0</sub> |  | 2.2<br><sub>3,1,4,3,2</sub> |  | 1.3<br><sub>3,0,1,0,0</sub> |  | 0.6<br><sub>0,4,1,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 9.3 |
| Kyle Anderson (TOR) | 52% | 11.5<br><sub>16,11,5,-,-</sub> | 3.5<br><sub>6,2,0,-,-</sub> |  | 2.2<br><sub>2,3,0,-,-</sub> |  | 2.2<br><sub>2,4,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.6 | 0.4 | 0.6 | 7.9 |
| Trayce Jackson-Davis (TOR) | 52% | 11.0<br><sub>14,-,-,-,-</sub> | 4.5<br><sub>4,-,-,-,-</sub> |  | 3.9<br><sub>6,-,-,-,-</sub> |  | 0.8<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.7 | 0.7 | 0.6 | 9.2 |
| Jaden Bradley (TOR) | 52% | 8.2<br><sub>9,-,2,-,-</sub> | 2.9<br><sub>0,-,1,-,-</sub> |  | 1.4<br><sub>1,-,0,-,-</sub> |  | 1.3<br><sub>3,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 5.6 |
| Kevin McCullar Jr. (TOR) | 16% | 7.8<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 4.9 |
| Malachi Smith (TOR) | 96% | 7.8<br><sub>1,-,2,-,-</sub> | 2.9<br><sub>0,-,0,-,-</sub> |  | 1.3<br><sub>0,-,0,-,-</sub> |  | 1.1<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.2 |
| Trae Young (WAS) | 99% | 34.3<br><sub>38,34,45,26,33</sub> | 17.6<br><sub>20,15,37,0,13</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>1,3,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 8.8<br><sub>7,4,14,8,12</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,3,4,0,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 3.6 | 29.2 |
| Anthony Davis (WAS) | 98% | 33.9<br><sub>34,34,44,31,35</sub> | 20.8<br><sub>44,21,30,14,23</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 10.6<br><sub>13,13,15,8,4</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>1,0,4,5,0</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 1.1 | 1.6 | 2.3 | 34.0 |
| AJ Dybantsa (WAS) | 98% | 33.0<br><sub>37,34,44,30,32</sub> | 14.9<br><sub>21,13,5,16,21</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.0<br><sub>8,4,8,7,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,2,4,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>1,0,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.5 | 2.4 | 23.1 |
| Kyshawn George (WAS) | 99% | 32.5<br><sub>35,39,26,30,38</sub> | 15.6<br><sub>12,25,14,11,18</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>3,9,1,2,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>2,3,5,4,1</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>2,5,3,1,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 1.1 | 2.6 | 24.3 |
| Alex Sarr (WAS) | 98% | 27.7<br><sub>25,25,44,27,31</sub> | 12.3<br><sub>4,5,30,25,6</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>8,8,9,9,4</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>0,0,2,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1<br><sub>0,1,4,3,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 1.3 | 1.5 | 21.4 |
| Tre Johnson (WAS) | 96% | 21.3<br><sub>29,29,30,-,21</sub> | 8.7<br><sub>2,15,13,-,9</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,3,4,-,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1<br><sub>0,1,2,-,3</sub> |  | 1.2<br><sub>0,2,1,-,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.2 | 1.3 | 11.9 |
| Bilal Coulibaly (WAS) | 98% | 20.9<br><sub>-,25,29,21,16</sub> | 7.4<br><sub>-,5,4,9,11</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>-,6,7,2,5</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>-,2,0,0,0</sub> |  | 0.6<br><sub>-,0,0,1,1</sub> |  | 0.8 | 0.7 | 1.1 | 11.9 |
| Khris Middleton (WAS) | 52% | 13.2<br><sub>-,-,-,9,18</sub> | 4.7<br><sub>-,-,-,8,9</sub> |  | 1.9<br><sub>-,-,-,0,3</sub> |  | 1.2<br><sub>-,-,-,2,3</sub> |  | 0.5<br><sub>-,-,-,2,2</sub> |  | 0.4 | 0.1 | 1.0 | 7.9 |
| Deandre Ayton (WAS) | 99% | 12.1<br><sub>13,9,9,10,8</sub> | 3.9<br><sub>2,2,2,2,4</sub> |  | 3.7<br><sub>8,2,4,1,0</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 8.1 |
| Bub Carrington (WAS) | 99% | 11.8<br><sub>19,10,16,23,2</sub> | 3.7<br><sub>4,0,2,11,0</sub> |  | 1.2<br><sub>0,0,0,0,0</sub> |  | 1.5<br><sub>4,0,2,4,0</sub> |  | 0.5<br><sub>1,0,0,3,0</sub> |  | 0.3 | 0.1 | 0.8 | 6.4 |
| Will Riley (WAS) | 86% | 8.2<br><sub>4,-,3,16,2</sub> | 3.8<br><sub>0,-,3,14,2</sub> |  | 1.0<br><sub>0,-,0,3,1</sub> |  | 0.6<br><sub>1,-,0,0,0</sub> |  | 0.3<br><sub>0,-,1,2,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Anthony Gill (WAS) | 58% | 7.2<br><sub>2,-,-,6,2</sub> | 2.7<br><sub>0,-,-,5,2</sub> |  | 1.1<br><sub>2,-,-,1,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Tre Mann (WAS) | 63% | 6.1<br><sub>2,-,-,11,2</sub> | 2.7<br><sub>0,-,-,4,2</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.7<br><sub>0,-,-,1,1</sub> |  | 0.2<br><sub>0,-,-,1,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

</details>


### DET @ NOP
Out: Bennedict Mathurin (NOP), Bryce McGowens (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Jalen Duren (DET), Ronald Holland II (DET), Taurean Prince (DET), Duncan Robinson (DET)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.3–109.7 | DET 63% | 1.60 / 2.67 | NOP +4.5 | 223.5 | NOP +4.5 covers 49%; o225.5 46% |
| Expected (weighted by chance each plays) | 116.1–109.8 | DET 67% | 1.49 / 3.04 | NOP +6.5 | 225.5 | NOP +4.5 covers 45%; o225.5 50% |
| if Cade Cunningham plays | 117.4–109.5 | DET 71% | 1.41 / 3.43 | NOP +7.5 | 226.5 | NOP +4.5 covers 40%; o225.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | Questionable | 55% | 36.7 | 29.6 | 5.2 | 9.1 | 2.7 | 1.3 | 0.8 | 4.0 | 43.9 | full tables below |
| Isaiah Joe (DET) | Questionable | 55% | 16.8 | 9.4 | 1.8 | 1.4 | 1.5 | 0.6 | 0.1 | 0.9 | 12.5 | small |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Daniss Jenkins | 98% | 35.5<br><sub>32,36,42,35,38</sub> | 21.1<br><sub>31,22,21,10,25</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>5,6,6,1,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>4,8,0,5,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>8,2,3,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3 | 0.3 | 2.7 | 32.0 |
| Kevin Huerter | 98% | 34.4<br><sub>35,33,24,38,36</sub> | 17.7<br><sub>24,12,11,20,9</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>5,2,1,4,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.8<br><sub>5,3,0,7,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>4,0,1,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.7 | 2.2 | 26.7 |
| Ausar Thompson | 98% | 31.7<br><sub>24,28,43,18,29</sub> | 14.6<br><sub>7,8,17,10,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>11,5,11,8,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 6.7<br><sub>3,4,11,5,12</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 2.2 | 1.2 | 2.9 | 29.8 |
| Paul Reed | 98% | 30.6<br><sub>20,21,38,23,25</sub> | 17.6<br><sub>8,4,13,9,10</sub> |  | 10.0<br><sub>10,10,11,9,6</sub> |  | 3.4<br><sub>0,2,3,1,5</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 1.5 | 1.6 | 2.1 | 31.0 |
| John Collins | 98% | 30.1<br><sub>32,28,25,26,23</sub> | 16.4<br><sub>8,24,10,8,11</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.7<br><sub>4,10,4,7,1</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>1,3,0,0,0</sub> |  | 1.2<br><sub>1,2,2,2,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.9 | 1.9 | 24.6 |
| Javonte Green | 98% | 28.8<br><sub>17,11,15,12,23</sub> | 12.0<br><sub>7,7,5,5,6</sub> |  | 4.3<br><sub>2,1,1,1,6</sub> |  | 1.5<br><sub>2,0,0,0,0</sub> |  | 1.9<br><sub>1,0,1,0,0</sub> |  | 1.7 | 0.6 | 0.8 | 17.8 |
| Chaz Lanier | 58% | 23.5<br><sub>-,2,-,-,25</sub> | 7.9<br><sub>-,0,-,-,3</sub> |  | 2.0<br><sub>-,0,-,-,3</sub> |  | 1.5<br><sub>-,0,-,-,1</sub> |  | 1.5<br><sub>-,0,-,-,1</sub> |  | 0.7 | 0.1 | 0.5 | 11.4 |
| Tolu Smith | 52% | 17.7<br><sub>-,-,-,1,-</sub> | 6.5<br><sub>-,-,-,3,-</sub> |  | 6.3<br><sub>-,-,-,2,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.9 | 1.0 | 13.9 |
| Elijah Harkless | 52% | 14.8<br><sub>-,-,-,2,4</sub> | 4.3<br><sub>-,-,-,2,0</sub> |  | 2.4<br><sub>-,-,-,0,1</sub> |  | 1.3<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.8 | 0.4 | 1.0 | 7.9 |
| Isaac Jones | 52% | 13.3<br><sub>-,2,-,2,-</sub> | 14.5<br><sub>-,0,-,0,-</sub> |  | 3.4<br><sub>-,0,-,1,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.6 | 0.9 | 0.7 | 18.6 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Saddiq Bey | 98% | 32.9<br><sub>24,29,35,41,33</sub> | 17.3<br><sub>9,15,30,16,23</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>0,1,10,6,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>4,2,0,4,3</sub> |  | 2.3<br><sub>1,3,6,2,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.2 | 1.4 | 25.0 |
| Zion Williamson | 98% | 32.7<br><sub>-,30,33,31,25</sub> | 20.7<br><sub>-,29,22,24,16</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>-,4,5,6,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>-,2,4,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.3<br><sub>-,1,0,2,0</sub> |  | 1.3 | 0.8 | 2.3 | 30.0 |
| Jeremiah Fears | 99% | 31.7<br><sub>29,28,34,33,29</sub> | 17.3<br><sub>11,14,18,13,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>3,4,5,4,10</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>8,5,7,7,10</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>1,2,0,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.6 | 2.8 | 27.4 |
| Herbert Jones | 98% | 25.8<br><sub>24,25,32,27,24</sub> | 8.1<br><sub>10,2,8,10,8</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>6,2,2,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>1,3,3,1,3</sub> |  | 1.0<br><sub>2,0,0,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.5 | 1.2 | 12.8 |
| Jordan Poole | 80% | 25.4<br><sub>34,21,21,24,31</sub> | 12.1<br><sub>7,14,13,14,11</sub> |  | 2.2<br><sub>3,0,2,2,2</sub> |  | 3.5<br><sub>2,1,5,5,5</sub> |  | 1.9<br><sub>1,2,1,1,1</sub> |  | 0.8 | 0.4 | 1.8 | 17.8 |
| Derik Queen | 99% | 24.9<br><sub>21,14,23,25,21</sub> | 12.4<br><sub>16,9,10,10,17</sub> |  | 7.2<br><sub>4,0,6,5,10</sub> |  | 2.9<br><sub>0,0,2,4,0</sub> |  | 0.7<br><sub>0,1,0,2,4</sub> |  | 1.0 | 1.0 | 2.4 | 22.4 |
| Yves Missi | 98% | 22.3<br><sub>-,-,-,22,23</sub> | 6.8<br><sub>-,-,-,3,6</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>-,-,-,8,14</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>-,-,-,1,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.5 | 2.0 | 1.1 | 15.2 |
| Karlo Matkovic | 98% | 22.0<br><sub>17,22,19,14,20</sub> | 8.1<br><sub>4,4,1,5,3</sub> |  | 4.9<br><sub>6,4,3,3,2</sub> |  | 1.1<br><sub>2,1,0,1,0</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.9 | 1.0 | 14.1 |
| Jaron Pierre Jr. | 87% | 17.0<br><sub>-,7,4,23,19</sub> | 7.2<br><sub>-,4,0,13,10</sub> |  | 2.5<br><sub>-,4,0,2,4</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,1,0,2,2</sub> |  | 0.5 | 0.2 | 1.1 | 10.6 |
| DeAndre Jordan | 38% | 12.8<br><sub>-,11,17,-,-</sub> | 3.4<br><sub>-,0,6,-,-</sub> |  | 4.6<br><sub>-,3,8,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.7 | 0.6 | 8.6 |
| AJ Johnson | 63% | 8.0<br><sub>12,7,4,-,6</sub> | 2.8<br><sub>2,2,1,-,0</sub> |  | 1.0<br><sub>2,1,0,-,0</sub> |  | 0.6<br><sub>3,0,0,-,0</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.4 |
| Malik Dia | 60% | 7.9<br><sub>-,-,4,-,5</sub> | 3.2<br><sub>-,-,2,-,2</sub> |  | 1.0<br><sub>-,-,0,-,1</sub> |  | 1.0<br><sub>-,-,1,-,1</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 5.3 |
| Julian Reese | 60% | 7.4<br><sub>9,7,4,-,5</sub> | 2.6<br><sub>2,2,0,-,0</sub> |  | 1.4<br><sub>0,2,2,-,1</sub> |  | 0.3<br><sub>0,1,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.4 |

</details>

<details><summary>if Cade Cunningham plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham (DET) | 100% | 36.7<br><sub>38,27,48,36,38</sub> | 29.6<br><sub>14,17,52,33,27</sub> | 25.5 · – | 5.2<br><sub>4,3,5,5,5</sub> | 4.5 | 9.1<br><sub>8,7,11,8,6</sub> | 7.5 | 2.7<br><sub>1,0,3,3,1</sub> | 1.5 | 1.3 | 0.8 | 4.0 | 43.9 |
| Daniss Jenkins (DET) | 98% | 34.1<br><sub>32,36,42,35,38</sub> | 17.4<br><sub>31,22,21,10,25</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>5,6,6,1,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.8<br><sub>4,8,0,5,5</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>8,2,3,1,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.2 | 0.3 | 2.1 | 27.2 |
| Kevin Huerter (DET) | 98% | 32.2<br><sub>35,33,24,38,36</sub> | 13.6<br><sub>24,12,11,20,9</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>5,2,1,4,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.6<br><sub>5,3,0,7,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>4,0,1,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.7 | 1.5 | 21.1 |
| Ausar Thompson (DET) | 98% | 30.9<br><sub>24,28,43,18,29</sub> | 12.2<br><sub>7,8,17,10,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>11,5,11,8,9</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>3,4,11,5,12</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.1<br><sub>0,0,0,0,0</sub> |  | 2.0 | 1.2 | 2.2 | 25.9 |
| Paul Reed (DET) | 98% | 30.2<br><sub>20,21,38,23,25</sub> | 15.2<br><sub>8,4,13,9,10</sub> |  | 9.6<br><sub>10,10,11,9,6</sub> |  | 2.8<br><sub>0,2,3,1,5</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 1.5 | 1.6 | 1.7 | 27.6 |
| John Collins (DET) | 98% | 29.3<br><sub>32,28,25,26,23</sub> | 13.4<br><sub>8,24,10,8,11</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 6.3<br><sub>4,10,4,7,1</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>1,3,0,0,0</sub> |  | 1.2<br><sub>1,2,2,2,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.9 | 1.4 | 20.9 |
| Javonte Green (DET) | 98% | 20.2<br><sub>17,11,15,12,23</sub> | 7.2<br><sub>7,7,5,5,6</sub> |  | 2.9<br><sub>2,1,1,1,6</sub> |  | 0.8<br><sub>2,0,0,0,0</sub> |  | 1.1<br><sub>1,0,1,0,0</sub> |  | 1.2 | 0.4 | 0.5 | 10.9 |
| Chaz Lanier (DET) | 58% | 16.5<br><sub>-,2,-,-,25</sub> | 5.2<br><sub>-,0,-,-,3</sub> |  | 1.4<br><sub>-,0,-,-,3</sub> |  | 0.9<br><sub>-,0,-,-,1</sub> |  | 0.9<br><sub>-,0,-,-,1</sub> |  | 0.5 | 0.1 | 0.4 | 7.5 |
| Tolu Smith (DET) | 52% | 11.1<br><sub>-,-,-,1,-</sub> | 3.9<br><sub>-,-,-,3,-</sub> |  | 4.0<br><sub>-,-,-,2,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.5 | 0.6 | 8.5 |
| Elijah Harkless (DET) | 52% | 7.9<br><sub>-,-,-,2,4</sub> | 2.0<br><sub>-,-,-,2,0</sub> |  | 1.3<br><sub>-,-,-,0,1</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 3.9 |
| Isaac Jones (DET) | 52% | 7.5<br><sub>-,2,-,2,-</sub> | 9.1<br><sub>-,0,-,0,-</sub> |  | 2.0<br><sub>-,0,-,1,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.5 | 0.4 | 11.5 |
| Saddiq Bey (NOP) | 98% | 32.9<br><sub>24,29,35,41,33</sub> | 17.3<br><sub>9,15,30,16,23</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>0,1,10,6,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>4,2,0,4,3</sub> |  | 2.3<br><sub>1,3,6,2,5</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.2 | 1.4 | 25.0 |
| Zion Williamson (NOP) | 98% | 32.7<br><sub>-,30,33,31,25</sub> | 20.6<br><sub>-,29,22,24,16</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>-,4,5,6,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>-,2,4,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.3<br><sub>-,1,0,2,0</sub> |  | 1.3 | 0.8 | 2.3 | 30.0 |
| Jeremiah Fears (NOP) | 99% | 31.8<br><sub>29,28,34,33,29</sub> | 17.3<br><sub>11,14,18,13,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>3,4,5,4,10</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>8,5,7,7,10</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>1,2,0,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.6 | 2.8 | 27.3 |
| Herbert Jones (NOP) | 98% | 25.7<br><sub>24,25,32,27,24</sub> | 8.0<br><sub>10,2,8,10,8</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>6,2,2,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>1,3,3,1,3</sub> |  | 1.0<br><sub>2,0,0,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2 | 0.5 | 1.2 | 12.7 |
| Jordan Poole (NOP) | 80% | 25.3<br><sub>34,21,21,24,31</sub> | 12.2<br><sub>7,14,13,14,11</sub> |  | 2.2<br><sub>3,0,2,2,2</sub> |  | 3.5<br><sub>2,1,5,5,5</sub> |  | 1.9<br><sub>1,2,1,1,1</sub> |  | 0.7 | 0.4 | 1.8 | 17.9 |
| Derik Queen (NOP) | 99% | 24.9<br><sub>21,14,23,25,21</sub> | 12.4<br><sub>16,9,10,10,17</sub> |  | 7.1<br><sub>4,0,6,5,10</sub> |  | 2.9<br><sub>0,0,2,4,0</sub> |  | 0.7<br><sub>0,1,0,2,4</sub> |  | 1.0 | 1.0 | 2.4 | 22.4 |
| Yves Missi (NOP) | 98% | 22.3<br><sub>-,-,-,22,23</sub> | 6.7<br><sub>-,-,-,3,6</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>-,-,-,8,14</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>-,-,-,1,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.5 | 2.0 | 1.1 | 15.2 |
| Karlo Matkovic (NOP) | 98% | 22.1<br><sub>17,22,19,14,20</sub> | 8.1<br><sub>4,4,1,5,3</sub> |  | 4.9<br><sub>6,4,3,3,2</sub> |  | 1.1<br><sub>2,1,0,1,0</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 0.6 | 1.0 | 1.0 | 14.1 |
| Jaron Pierre Jr. (NOP) | 87% | 17.0<br><sub>-,7,4,23,19</sub> | 7.2<br><sub>-,4,0,13,10</sub> |  | 2.5<br><sub>-,4,0,2,4</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.9<br><sub>-,1,0,2,2</sub> |  | 0.5 | 0.2 | 1.1 | 10.5 |
| DeAndre Jordan (NOP) | 38% | 12.9<br><sub>-,11,17,-,-</sub> | 3.4<br><sub>-,0,6,-,-</sub> |  | 4.7<br><sub>-,3,8,-,-</sub> |  | 0.7<br><sub>-,0,1,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.8 | 0.7 | 8.7 |
| AJ Johnson (NOP) | 63% | 8.1<br><sub>12,7,4,-,6</sub> | 2.8<br><sub>2,2,1,-,0</sub> |  | 1.0<br><sub>2,1,0,-,0</sub> |  | 0.7<br><sub>3,0,0,-,0</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 4.5 |
| Malik Dia (NOP) | 60% | 7.9<br><sub>-,-,4,-,5</sub> | 3.2<br><sub>-,-,2,-,2</sub> |  | 1.0<br><sub>-,-,0,-,1</sub> |  | 1.0<br><sub>-,-,1,-,1</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 5.2 |
| Julian Reese (NOP) | 60% | 7.4<br><sub>9,7,4,-,5</sub> | 2.6<br><sub>2,2,0,-,0</sub> |  | 1.5<br><sub>0,2,2,-,1</sub> |  | 0.3<br><sub>0,1,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.4 |

</details>


### ATL @ OKC
Out: Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Kingston Flemings (ATL), Mouhamed Gueye (ATL), Jock Landale (ATL), CJ McCollum (ATL), Asa Newell (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.4–118.3 | ATL 27% | 3.76 / 1.36 | OKC -8.5 | 227.5 | OKC -6.5 covers 57%; o228.5 48% |
| Expected (weighted by chance each plays) | 109.2–118.3 | ATL 26% | 3.85 / 1.35 | OKC -9.5 | 227.5 | OKC -6.5 covers 58%; o228.5 48% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaylin Williams (OKC) | Questionable | 55% | 12.8 | 4.1 | 3.4 | 1.2 | 0.5 | 0.4 | 0.3 | 0.5 | 8.8 | small |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 36.6<br><sub>-,36,38,40,35</sub> | 20.7<br><sub>-,30,15,27,14</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 9.6<br><sub>-,7,7,11,11</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>-,6,4,10,5</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>-,0,0,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 3.9 | 37.8 |
| Nickeil Alexander-Walker | 98% | 35.3<br><sub>33,31,34,41,33</sub> | 22.1<br><sub>28,20,20,16,20</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>2,3,4,6,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,1,4,3,4</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.4<br><sub>4,2,4,1,2</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.5 | 2.8 | 29.2 |
| Onyeka Okongwu | 98% | 34.1<br><sub>33,30,30,35,36</sub> | 15.8<br><sub>22,16,16,17,16</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 8.5<br><sub>10,2,9,6,11</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>1,5,3,1,0</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>2,2,2,2,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 1.0 | 1.9 | 27.3 |
| Dyson Daniels | 98% | 33.5<br><sub>35,31,31,36,27</sub> | 12.3<br><sub>13,9,10,6,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>9,10,6,9,10</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>12,7,8,4,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.5<br><sub>0,0,1,0,0</sub> |  | 2.0 | 0.4 | 2.1 | 25.9 |
| Aaron Wiggins | 98% | 27.9<br><sub>29,26,23,26,24</sub> | 13.5<br><sub>19,20,15,9,7</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,4,3,4,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>3,6,3,3,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>3,5,4,1,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.4 | 1.7 | 19.9 |
| Luguentz Dort | 98% | 25.7<br><sub>32,20,18,20,18</sub> | 9.3<br><sub>25,3,4,10,3</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>7,2,3,1,4</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>4,1,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>5,1,1,1,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.3 | 1.1 | 14.0 |
| Corey Kispert | 52% | 14.9<br><sub>16,-,-,-,16</sub> | 7.6<br><sub>7,-,-,-,14</sub> |  | 1.9<br><sub>2,-,-,-,3</sub> |  | 1.1<br><sub>1,-,-,-,1</sub> |  | 1.1<br><sub>1,-,-,-,3</sub> |  | 0.3 | 0.1 | 0.8 | 10.7 |
| Jalen Wilson | 47% | 14.3<br><sub>-,-,-,-,-</sub> | 5.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.8 | 9.2 |
| RayJ Dennis | 64% | 13.7<br><sub>-,-,-,-,10</sub> | 5.1<br><sub>-,-,-,-,6</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 2.2<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.2 | 0.9 | 9.3 |
| Zuby Ejiofor | 67% | 13.2<br><sub>15,18,4,-,12</sub> | 4.5<br><sub>10,7,0,-,4</sub> |  | 2.9<br><sub>5,6,0,-,3</sub> |  | 1.2<br><sub>5,0,0,-,0</sub> |  | 0.4<br><sub>0,1,0,-,1</sub> |  | 0.4 | 0.3 | 0.7 | 8.6 |
| Dorian Finney-Smith | 23% | 8.0<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 33.2<br><sub>29,29,36,39,30</sub> | 31.3<br><sub>30,26,31,40,37</sub> | 32.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>2,8,4,4,2</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 6.0<br><sub>9,3,2,5,2</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>3,0,0,2,4</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.8 | 2.7 | 41.4 |
| Jared McCain | 98% | 27.2<br><sub>23,31,31,31,30</sub> | 15.1<br><sub>19,21,10,23,12</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>5,3,6,4,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>2,3,3,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>2,4,2,7,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.1 | 1.6 | 20.1 |
| Ajay Mitchell | 98% | 27.2<br><sub>22,28,-,-,27</sub> | 15.9<br><sub>12,14,-,-,14</sub> | 18.5 · –<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>4,3,-,-,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>0,3,-,-,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>0,0,-,-,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.8 | 23.0 |
| Isaiah Hartenstein | 98% | 24.3<br><sub>18,24,34,30,18</sub> | 9.4<br><sub>2,7,20,21,3</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 10.1<br><sub>14,9,11,16,11</sub> | 10.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>6,5,6,6,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.7 | 23.4 |
| Aday Mara | 98% | 22.4<br><sub>27,26,32,21,26</sub> | 9.5<br><sub>18,10,11,10,16</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.9<br><sub>8,10,6,3,13</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>3,2,2,0,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.0<br><sub>1,0,0,0,0</sub> |  | 0.3 | 1.7 | 1.7 | 18.1 |
| Alex Caruso | 98% | 20.5<br><sub>13,19,29,27,18</sub> | 8.3<br><sub>0,5,14,5,11</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>3,2,7,1,2</sub> |  | 2.3<br><sub>3,1,2,4,3</sub> |  | 1.1<br><sub>0,1,4,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.5 | 1.0 | 13.8 |
| Kenrich Williams | 98% | 20.2<br><sub>23,19,26,35,19</sub> | 7.6<br><sub>9,3,11,8,10</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>4,2,2,8,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,0,2,4,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>1,1,2,0,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.7 | 0.2 | 0.9 | 13.1 |
| Bennett Stirtz | 98% | 17.3<br><sub>29,18,25,12,17</sub> | 6.4<br><sub>11,13,6,5,0</sub> |  | 1.4<br><sub>5,1,1,1,1</sub> |  | 1.1<br><sub>3,1,1,0,2</sub> |  | 0.9<br><sub>2,2,2,1,0</sub> |  | 0.7 | 0.2 | 0.7 | 9.0 |
| Nique Clifford | 96% | 15.1<br><sub>-,20,16,12,24</sub> | 5.1<br><sub>-,4,5,0,9</sub> |  | 2.3<br><sub>-,4,3,0,3</sub> |  | 1.2<br><sub>-,1,1,0,0</sub> |  | 0.4<br><sub>-,0,1,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 8.5 |
| Micah Peavy | 91% | 14.5<br><sub>23,21,12,-,13</sub> | 4.2<br><sub>7,0,0,-,5</sub> |  | 2.6<br><sub>3,2,3,-,3</sub> |  | 0.5<br><sub>0,0,0,-,1</sub> |  | 0.4<br><sub>1,0,0,-,1</sub> |  | 0.6 | 0.2 | 0.4 | 7.3 |
| Josh Dix | 67% | 12.1<br><sub>21,-,-,17,-</sub> | 4.1<br><sub>2,-,-,0,-</sub> |  | 1.5<br><sub>1,-,-,4,-</sub> |  | 0.7<br><sub>2,-,-,3,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |
| Nikola Topic | 86% | 10.9<br><sub>-,-,-,16,13</sub> | 3.5<br><sub>-,-,-,0,8</sub> |  | 1.3<br><sub>-,-,-,4,0</sub> |  | 2.1<br><sub>-,-,-,3,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.1 | 1.3 | 6.8 |
| Brooks Barnhizer | 58% | 6.4<br><sub>8,5,-,-,4</sub> | 1.8<br><sub>2,0,-,-,0</sub> |  | 1.4<br><sub>4,1,-,-,0</sub> |  | 0.5<br><sub>3,1,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |

</details>


### BOS @ DEN
Out: Julian Strawther (DEN), Cam Whitmore (DEN)

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 33.8<br><sub>29,32,38,30,36</sub> | 24.0<br><sub>21,21,24,32,24</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>4,6,7,6,12</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>6,4,8,6,4</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>5,3,2,5,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.5 | 2.6 | 38.6 |
| Paul George | 98% | 30.2<br><sub>28,30,-,25,36</sub> | 18.0<br><sub>27,36,-,7,22</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>3,5,-,7,8</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>1,1,-,6,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>5,6,-,1,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.5 | 0.4 | 2.0 | 26.6 |
| Derrick White | 98% | 30.0<br><sub>27,22,38,23,32</sub> | 12.6<br><sub>9,5,19,16,9</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>3,1,1,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 4.3<br><sub>7,3,7,2,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,1,3,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.8 | 1.3 | 20.3 |
| Payton Pritchard | 98% | 26.4<br><sub>29,30,31,19,32</sub> | 13.0<br><sub>12,18,14,10,21</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,6,1,1,4</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.8<br><sub>4,5,1,6,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>4,4,2,2,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.6 | 0.1 | 1.0 | 19.9 |
| Neemias Queta | 98% | 20.4<br><sub>22,22,31,15,-</sub> | 8.0<br><sub>13,4,11,8,-</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>9,6,13,6,-</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>4,3,3,2,-</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>0,0,1,1,-</sub> |  | 0.5 | 0.9 | 0.9 | 16.2 |
| Sam Hauser | 98% | 20.1<br><sub>23,18,24,11,25</sub> | 7.9<br><sub>7,12,8,8,12</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>3,5,9,1,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>1,2,0,0,2</sub> |  | 1.5<br><sub>1,4,2,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.4 | 0.2 | 0.3 | 12.1 |
| Baylor Scheierman | 98% | 15.9<br><sub>19,18,29,18,11</sub> | 5.1<br><sub>7,5,9,12,0</sub> |  | 2.9<br><sub>1,3,7,5,1</sub> |  | 1.2<br><sub>0,2,3,3,1</sub> |  | 0.7<br><sub>1,1,3,2,0</sub> |  | 0.6 | 0.1 | 0.5 | 9.3 |
| Mitchell Robinson | 98% | 15.4<br><sub>18,17,11,15,18</sub> | 4.4<br><sub>12,2,2,0,4</sub> |  | 5.8<br><sub>7,6,2,7,5</sub> |  | 0.7<br><sub>2,2,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.7 | 0.6 | 10.9 |
| Jordan Walsh | 98% | 14.1<br><sub>11,19,18,21,17</sub> | 4.3<br><sub>0,8,6,11,6</sub> |  | 2.6<br><sub>3,2,3,1,2</sub> |  | 0.7<br><sub>0,2,0,0,0</sub> |  | 0.5<br><sub>0,1,0,2,2</sub> |  | 0.5 | 0.3 | 0.4 | 7.6 |
| Luka Garza | 98% | 13.3<br><sub>9,9,11,14,18</sub> | 6.3<br><sub>4,2,5,2,3</sub> |  | 3.1<br><sub>5,0,1,3,0</sub> |  | 1.3<br><sub>0,2,0,5,4</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.3 | 0.5 | 10.8 |
| Devin Carter | 91% | 12.5<br><sub>-,-,-,12,-</sub> | 4.9<br><sub>-,-,-,0,-</sub> |  | 2.2<br><sub>-,-,-,2,-</sub> |  | 1.6<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.2 | 0.9 | 8.7 |
| Hugo Gonzalez | 98% | 8.9<br><sub>10,19,8,18,4</sub> | 2.9<br><sub>0,10,0,9,0</sub> |  | 1.8<br><sub>2,2,1,5,2</sub> |  | 0.5<br><sub>1,2,0,2,0</sub> |  | 0.2<br><sub>0,2,0,2,0</sub> |  | 0.4 | 0.2 | 0.3 | 5.1 |
| Chris Cenac Jr. | 58% | 7.5<br><sub>-,-,-,7,12</sub> | 2.8<br><sub>-,-,-,6,4</sub> |  | 1.6<br><sub>-,-,-,3,2</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Mike Conley | 38% | 7.1<br><sub>10,-,-,-,-</sub> | 1.9<br><sub>3,-,-,-,-</sub> |  | 0.7<br><sub>3,-,-,-,-</sub> |  | 1.0<br><sub>1,-,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |
| Ron Harper Jr. | 58% | 6.7<br><sub>4,4,-,12,-</sub> | 3.1<br><sub>2,0,-,10,-</sub> |  | 1.0<br><sub>0,1,-,1,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.3<br><sub>0,0,-,2,-</sub> |  | 0.3 | 0.1 | 0.2 | 4.6 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nikola Jokic | 98% | 37.1<br><sub>36,39,37,37,38</sub> | 24.4<br><sub>19,25,27,26,28</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 11.9<br><sub>13,16,11,8,15</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 10.1<br><sub>8,9,8,10,7</sub> | 8.5<br><sub>o 57% · u 43%</sub> | 1.5<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.8 | 3.7 | 46.4 |
| Jamal Murray | 98% | 37.0<br><sub>34,39,32,38,35</sub> | 23.0<br><sub>16,38,30,23,28</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>6,2,4,7,4</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.5<br><sub>8,2,8,9,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>2,5,4,0,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.6 | 2.5 | 34.1 |
| Christian Braun | 98% | 32.8<br><sub>29,32,37,28,33</sub> | 12.0<br><sub>6,4,12,17,10</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>4,5,5,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>1,3,4,1,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.3<br><sub>0,0,2,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.4 | 0.9 | 18.8 |
| Cameron Johnson | 98% | 29.9<br><sub>29,31,30,31,27</sub> | 12.3<br><sub>18,8,23,12,9</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>4,2,4,5,0</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>1,1,3,2,1</sub> |  | 1.9<br><sub>2,2,4,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.3 | 1.0 | 18.3 |
| Aaron Gordon | 98% | 29.3<br><sub>27,30,27,33,24</sub> | 11.9<br><sub>12,3,9,11,11</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>5,5,3,5,1</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>0,2,2,1,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.5 | 0.4 | 1.2 | 19.4 |
| DeMar DeRozan | 91% | 20.3<br><sub>22,19,20,24,14</sub> | 9.5<br><sub>11,7,8,9,2</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,4,1,3,1</sub> |  | 2.6<br><sub>5,2,4,2,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.2 | 1.0 | 14.0 |
| Trevon Brazile | 98% | 17.8<br><sub>14,14,13,16,23</sub> | 5.2<br><sub>3,5,7,5,9</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>4,2,5,3,4</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.3 | 0.3 | 0.7 | 10.0 |
| Spencer Jones | 86% | 16.6<br><sub>21,14,22,12,21</sub> | 4.2<br><sub>13,0,3,4,4</sub> |  | 2.4<br><sub>6,0,1,2,3</sub> |  | 0.8<br><sub>0,1,0,1,3</sub> |  | 0.5<br><sub>3,0,1,0,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.4 |
| Marvin Bagley III | 98% | 12.6<br><sub>12,12,12,13,10</sub> | 5.8<br><sub>10,6,4,7,4</sub> |  | 3.7<br><sub>3,3,2,7,2</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 10.2 |
| Tyus Jones | 97% | 10.0<br><sub>13,6,11,10,10</sub> | 2.5<br><sub>3,2,0,2,0</sub> |  | 0.9<br><sub>4,0,1,0,1</sub> |  | 1.7<br><sub>4,0,4,3,2</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.1 |
| Bryce Hopkins | 58% | 8.0<br><sub>3,3,-,-,4</sub> | 2.6<br><sub>3,2,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.1<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |
| Zeke Nnaji | 26% | 6.4<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 3.7 |
| Alpha Diallo | 48% | 6.1<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### GSW @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.1–116.4 | GSW 43% | 2.31 / 1.76 | DAL -2.5 | 230.5 | DAL -4.5 covers 44%; o224.5 62% |
| Expected (weighted by chance each plays) | 115.0–116.6 | GSW 45% | 2.23 / 1.81 | DAL -2.5 | 231.5 | DAL -4.5 covers 42%; o224.5 64% |
| if Draymond Green plays | 115.0–116.2 | GSW 46% | 2.15 / 1.87 | DAL -1.5 | 231.5 | DAL -4.5 covers 41%; o224.5 64% |
| if Al Horford plays | 114.5–115.9 | GSW 46% | 2.17 / 1.85 | DAL -1.5 | 230.5 | DAL -4.5 covers 42%; o224.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Max Christie (DAL) | Questionable | 55% | 11.0 | 4.0 | 1.4 | 0.7 | 0.5 | 0.3 | 0.1 | 0.5 | 6.1 | small |
| Draymond Green (GSW) | Questionable | 55% | 28.8 | 6.3 | 5.7 | 6.9 | 0.7 | 1.1 | 0.8 | 2.7 | 18.8 | full tables below |
| Al Horford (GSW) | Questionable | 55% | 20.0 | 6.4 | 4.6 | 2.5 | 0.9 | 0.5 | 0.9 | 0.7 | 13.6 | full tables below |
| Tobi Lawal (DAL) | Doubtful | 20% | 6.8 | 2.6 | 1.5 | 0.4 | 0.2 | 0.3 | 0.1 | 0.3 | 4.5 | small |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 98% | 34.4<br><sub>37,27,36,24,33</sub> | 23.6<br><sub>23,23,25,3,28</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 7.9<br><sub>8,7,10,7,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,4,0,1,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,4,2,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.8 | 3.6 | 36.0 |
| Brandin Podziemski | 96% | 33.9<br><sub>39,26,37,22,30</sub> | 19.6<br><sub>15,25,22,8,15</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>7,2,6,3,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 5.3<br><sub>1,4,4,0,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>4,5,4,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.2 | 30.6 |
| Will Richard | 98% | 28.0<br><sub>12,-,19,30,23</sub> | 8.7<br><sub>4,-,9,7,11</sub> |  | 3.4<br><sub>2,-,4,4,3</sub> |  | 2.0<br><sub>1,-,0,1,1</sub> |  | 1.1<br><sub>0,-,2,1,2</sub> |  | 1.5 | 0.3 | 1.2 | 14.1 |
| De'Anthony Melton | 98% | 27.0<br><sub>17,26,25,18,21</sub> | 14.2<br><sub>4,16,11,8,8</sub> |  | 4.4<br><sub>1,4,4,4,2</sub> |  | 3.5<br><sub>1,3,4,3,1</sub> |  | 2.1<br><sub>1,4,3,2,2</sub> |  | 1.6 | 0.5 | 2.1 | 22.1 |
| Georges Niang | 98% | 24.9<br><sub>25,19,19,15,14</sub> | 10.6<br><sub>11,9,5,5,0</sub> |  | 3.8<br><sub>2,2,5,3,4</sub> |  | 2.0<br><sub>1,2,0,2,2</sub> |  | 1.6<br><sub>3,1,1,1,0</sub> |  | 0.6 | 0.2 | 1.2 | 16.4 |
| LJ Cryer | 84% | 24.4<br><sub>-,20,18,24,24</sub> | 11.0<br><sub>-,10,13,20,7</sub> |  | 2.2<br><sub>-,0,1,2,1</sub> |  | 2.8<br><sub>-,3,1,6,3</sub> |  | 1.9<br><sub>-,2,3,6,1</sub> |  | 0.7 | 0.1 | 1.2 | 15.9 |
| Gui Santos | 91% | 24.3<br><sub>12,21,12,21,19</sub> | 10.4<br><sub>3,3,0,7,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>1,7,3,4,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>0,4,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>0,0,0,1,1</sub> |  | 1.0 | 0.4 | 1.7 | 18.2 |
| Charles Bassey | 98% | 19.7<br><sub>11,18,13,20,16</sub> | 8.8<br><sub>8,12,7,11,4</sub> |  | 7.6<br><sub>4,10,6,5,0</sub> |  | 1.3<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 1.1 | 17.7 |
| Gary Payton II | 88% | 18.4<br><sub>13,-,-,13,8</sub> | 7.9<br><sub>4,-,-,2,2</sub> |  | 3.3<br><sub>0,-,-,2,0</sub> |  | 1.5<br><sub>0,-,-,0,0</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 1.0 | 0.3 | 0.9 | 12.7 |
| Graham Ike | 91% | 15.9<br><sub>-,12,4,13,8</sub> | 6.3<br><sub>-,4,4,5,3</sub> |  | 4.1<br><sub>-,5,0,2,5</sub> |  | 1.8<br><sub>-,2,1,3,1</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.5 | 0.8 | 12.2 |
| Malevy Leons | 67% | 14.8<br><sub>-,12,4,14,6</sub> | 4.1<br><sub>-,0,0,5,2</sub> |  | 2.8<br><sub>-,3,3,1,1</sub> |  | 1.0<br><sub>-,0,0,0,0</sub> |  | 0.2<br><sub>-,0,0,1,0</sub> |  | 0.7 | 0.6 | 0.7 | 7.9 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving | 98% | 34.3<br><sub>29,38,27,37,-</sub> | 23.1<br><sub>21,35,10,34,-</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,0,3,6,-</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>4,4,4,5,-</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>2,7,2,7,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 2.3 | 31.9 |
| Cooper Flagg | 98% | 34.0<br><sub>28,39,27,38,27</sub> | 23.3<br><sub>25,43,12,18,17</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>5,10,7,8,3</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>12,6,3,5,4</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,3,1,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.9 | 2.8 | 36.4 |
| P.J. Washington | 98% | 31.3<br><sub>25,35,16,26,25</sub> | 13.7<br><sub>6,13,10,10,8</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>5,9,3,4,5</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>0,1,0,1,4</sub> |  | 1.7<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.9 | 1.6 | 22.2 |
| Naji Marshall | 93% | 25.1<br><sub>15,25,23,30,23</sub> | 12.5<br><sub>8,6,13,12,13</sub> |  | 3.6<br><sub>1,5,1,3,2</sub> |  | 3.8<br><sub>2,2,4,5,2</sub> |  | 0.9<br><sub>1,0,1,0,3</sub> |  | 1.0 | 0.1 | 1.9 | 19.9 |
| Caleb Martin | 98% | 20.8<br><sub>19,19,21,33,34</sub> | 5.8<br><sub>2,0,7,15,12</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>2,3,2,8,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,5,5,3,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>0,0,1,1,4</sub> |  | 0.8 | 0.3 | 0.8 | 10.9 |
| Zaccharie Risacher | 98% | 20.3<br><sub>16,15,25,14,27</sub> | 7.7<br><sub>11,4,22,5,18</sub> |  | 3.9<br><sub>6,2,6,2,5</sub> |  | 1.1<br><sub>1,0,3,0,0</sub> |  | 0.9<br><sub>1,0,4,1,1</sub> |  | 0.8 | 0.6 | 0.9 | 12.8 |
| Daniel Gafford | 98% | 19.4<br><sub>19,20,16,17,19</sub> | 8.9<br><sub>18,8,3,10,3</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>5,2,3,3,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,3,1,1,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.6 | 1.3 | 1.1 | 15.8 |
| Walter Clayton Jr. | 89% | 17.7<br><sub>16,25,22,13,23</sub> | 6.7<br><sub>5,6,5,2,13</sub> |  | 2.9<br><sub>4,6,1,2,4</sub> |  | 3.1<br><sub>6,4,4,2,3</sub> |  | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.4 | 12.6 |
| Morez Johnson Jr. | 98% | 16.3<br><sub>19,-,13,15,26</sub> | 6.1<br><sub>4,-,0,4,2</sub> |  | 3.3<br><sub>9,-,2,2,6</sub> |  | 1.4<br><sub>1,-,0,0,4</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 10.8 |
| Santi Aldama | 91% | 14.5<br><sub>15,19,10,16,-</sub> | 7.0<br><sub>12,10,3,7,-</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,4,1,2,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,1,1,-</sub> |  | 0.8<br><sub>2,1,1,2,-</sub> |  | 0.5 | 0.4 | 0.9 | 11.7 |
| Marcus Sasser | 64% | 13.8<br><sub>9,-,9,-,18</sub> | 4.9<br><sub>4,-,3,-,5</sub> |  | 1.2<br><sub>0,-,1,-,1</sub> |  | 1.7<br><sub>0,-,0,-,2</sub> |  | 0.6<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.1 | 0.8 | 7.8 |
| Moussa Cisse | 63% | 6.6<br><sub>5,-,8,-,4</sub> | 2.3<br><sub>2,-,0,-,1</sub> |  | 2.6<br><sub>1,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.0<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.1 |
| Jett Howard | 63% | 6.2<br><sub>3,-,5,-,7</sub> | 2.6<br><sub>5,-,3,-,0</sub> |  | 0.7<br><sub>1,-,0,-,0</sub> |  | 0.4<br><sub>0,-,0,-,1</sub> |  | 0.2<br><sub>1,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>

<details><summary>if Al Horford plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving (DAL) | 98% | 34.4<br><sub>29,38,27,37,-</sub> | 23.2<br><sub>21,35,10,34,-</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,0,3,6,-</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>4,4,4,5,-</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>2,7,2,7,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.5 | 2.3 | 32.1 |
| Cooper Flagg (DAL) | 98% | 34.1<br><sub>28,39,27,38,27</sub> | 23.3<br><sub>25,43,12,18,17</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>5,10,7,8,3</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.0<br><sub>12,6,3,5,4</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,3,1,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.9 | 2.9 | 36.3 |
| P.J. Washington (DAL) | 98% | 31.4<br><sub>25,35,16,26,25</sub> | 13.7<br><sub>6,13,10,10,8</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>5,9,3,4,5</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,1,0,1,4</sub> |  | 1.7<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.9 | 1.6 | 22.3 |
| Naji Marshall (DAL) | 93% | 25.0<br><sub>15,25,23,30,23</sub> | 12.4<br><sub>8,6,13,12,13</sub> |  | 3.6<br><sub>1,5,1,3,2</sub> |  | 3.8<br><sub>2,2,4,5,2</sub> |  | 0.9<br><sub>1,0,1,0,3</sub> |  | 1.0 | 0.1 | 1.9 | 19.8 |
| Caleb Martin (DAL) | 98% | 20.8<br><sub>19,19,21,33,34</sub> | 5.7<br><sub>2,0,7,15,12</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>2,3,2,8,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,5,5,3,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>0,0,1,1,4</sub> |  | 0.9 | 0.3 | 0.8 | 10.9 |
| Zaccharie Risacher (DAL) | 98% | 20.3<br><sub>16,15,25,14,27</sub> | 7.7<br><sub>11,4,22,5,18</sub> |  | 4.0<br><sub>6,2,6,2,5</sub> |  | 1.1<br><sub>1,0,3,0,0</sub> |  | 0.8<br><sub>1,0,4,1,1</sub> |  | 0.8 | 0.6 | 0.9 | 12.8 |
| Daniel Gafford (DAL) | 98% | 19.4<br><sub>19,20,16,17,19</sub> | 8.9<br><sub>18,8,3,10,3</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>5,2,3,3,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,3,1,1,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.6 | 1.3 | 1.1 | 15.7 |
| Walter Clayton Jr. (DAL) | 89% | 17.8<br><sub>16,25,22,13,23</sub> | 6.7<br><sub>5,6,5,2,13</sub> |  | 2.9<br><sub>4,6,1,2,4</sub> |  | 3.1<br><sub>6,4,4,2,3</sub> |  | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.4 | 12.7 |
| Morez Johnson Jr. (DAL) | 98% | 16.4<br><sub>19,-,13,15,26</sub> | 6.0<br><sub>4,-,0,4,2</sub> |  | 3.3<br><sub>9,-,2,2,6</sub> |  | 1.4<br><sub>1,-,0,0,4</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 1.0 | 10.8 |
| Santi Aldama (DAL) | 91% | 14.4<br><sub>15,19,10,16,-</sub> | 7.1<br><sub>12,10,3,7,-</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,4,1,2,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,1,1,-</sub> |  | 0.8<br><sub>2,1,1,2,-</sub> |  | 0.5 | 0.3 | 0.9 | 11.8 |
| Marcus Sasser (DAL) | 64% | 13.8<br><sub>9,-,9,-,18</sub> | 4.9<br><sub>4,-,3,-,5</sub> |  | 1.2<br><sub>0,-,1,-,1</sub> |  | 1.6<br><sub>0,-,0,-,2</sub> |  | 0.6<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.1 | 0.8 | 7.8 |
| Moussa Cisse (DAL) | 63% | 6.6<br><sub>5,-,8,-,4</sub> | 2.4<br><sub>2,-,0,-,1</sub> |  | 2.6<br><sub>1,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.0<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.1 |
| Jett Howard (DAL) | 63% | 6.1<br><sub>3,-,5,-,7</sub> | 2.6<br><sub>5,-,3,-,0</sub> |  | 0.7<br><sub>1,-,0,-,0</sub> |  | 0.4<br><sub>0,-,0,-,1</sub> |  | 0.2<br><sub>1,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.3 | 3.7 |
| Yaxel Lendeborg (GSW) | 98% | 34.3<br><sub>37,27,36,24,33</sub> | 23.2<br><sub>23,23,25,3,28</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>8,7,10,7,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>3,4,0,1,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,4,2,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.8 | 3.5 | 35.4 |
| Brandin Podziemski (GSW) | 96% | 34.1<br><sub>39,26,37,22,30</sub> | 19.1<br><sub>15,25,22,8,15</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>7,2,6,3,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>1,4,4,0,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>4,5,4,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.1 | 29.9 |
| De'Anthony Melton (GSW) | 98% | 25.9<br><sub>17,26,25,18,21</sub> | 13.4<br><sub>4,16,11,8,8</sub> |  | 4.2<br><sub>1,4,4,4,2</sub> |  | 3.3<br><sub>1,3,4,3,1</sub> |  | 1.9<br><sub>1,4,3,2,2</sub> |  | 1.5 | 0.4 | 1.8 | 20.9 |
| Will Richard (GSW) | 98% | 25.6<br><sub>12,-,19,30,23</sub> | 7.9<br><sub>4,-,9,7,11</sub> |  | 3.2<br><sub>2,-,4,4,3</sub> |  | 1.8<br><sub>1,-,0,1,1</sub> |  | 1.0<br><sub>0,-,2,1,2</sub> |  | 1.4 | 0.2 | 1.0 | 12.9 |
| Georges Niang (GSW) | 98% | 22.9<br><sub>25,19,19,15,14</sub> | 9.7<br><sub>11,9,5,5,0</sub> |  | 3.5<br><sub>2,2,5,3,4</sub> |  | 1.8<br><sub>1,2,0,2,2</sub> |  | 1.5<br><sub>3,1,1,1,0</sub> |  | 0.5 | 0.2 | 1.0 | 15.1 |
| Gui Santos (GSW) | 91% | 22.2<br><sub>12,21,12,21,19</sub> | 9.5<br><sub>3,3,0,7,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>1,7,3,4,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>0,4,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.9 | 0.4 | 1.5 | 16.5 |
| LJ Cryer (GSW) | 84% | 21.5<br><sub>-,20,18,24,24</sub> | 10.1<br><sub>-,10,13,20,7</sub> |  | 1.9<br><sub>-,0,1,2,1</sub> |  | 2.5<br><sub>-,3,1,6,3</sub> |  | 1.7<br><sub>-,2,3,6,1</sub> |  | 0.6 | 0.1 | 1.1 | 14.5 |
| Al Horford (GSW) | 100% | 20.0<br><sub>13,15,21,10,14</sub> | 6.4<br><sub>2,5,2,0,0</sub> | 6.5 · – | 4.6<br><sub>5,2,1,3,5</sub> | 4.5 | 2.5<br><sub>4,6,4,1,0</sub> | 2.5 | 0.9<br><sub>0,1,0,0,0</sub> | 1.5 | 0.5 | 0.9 | 0.7 | 13.6 |
| Charles Bassey (GSW) | 98% | 17.0<br><sub>11,18,13,20,16</sub> | 8.1<br><sub>8,12,7,11,4</sub> |  | 6.7<br><sub>4,10,6,5,0</sub> |  | 1.1<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.2 | 0.9 | 15.9 |
| Gary Payton II (GSW) | 88% | 17.0<br><sub>13,-,-,13,8</sub> | 7.4<br><sub>4,-,-,2,2</sub> |  | 3.1<br><sub>0,-,-,2,0</sub> |  | 1.4<br><sub>0,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.9 | 0.3 | 0.8 | 11.9 |
| Graham Ike (GSW) | 91% | 13.7<br><sub>-,12,4,13,8</sub> | 5.6<br><sub>-,4,4,5,3</sub> |  | 3.6<br><sub>-,5,0,2,5</sub> |  | 1.5<br><sub>-,2,1,3,1</sub> |  | 0.3<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.4 | 0.7 | 10.8 |
| Malevy Leons (GSW) | 67% | 12.6<br><sub>-,12,4,14,6</sub> | 3.5<br><sub>-,0,0,5,2</sub> |  | 2.4<br><sub>-,3,3,1,1</sub> |  | 0.8<br><sub>-,0,0,0,0</sub> |  | 0.1<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.5 | 0.6 | 6.7 |

</details>

<details><summary>if Draymond Green plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kyrie Irving (DAL) | 98% | 34.4<br><sub>29,38,27,37,-</sub> | 23.2<br><sub>21,35,10,34,-</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>3,0,3,6,-</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>4,4,4,5,-</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>2,7,2,7,-</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.4 | 2.3 | 32.0 |
| Cooper Flagg (DAL) | 98% | 34.1<br><sub>28,39,27,38,27</sub> | 23.4<br><sub>25,43,12,18,17</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>5,10,7,8,3</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>12,6,3,5,4</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,3,1,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.9 | 2.9 | 36.4 |
| P.J. Washington (DAL) | 98% | 31.4<br><sub>25,35,16,26,25</sub> | 13.8<br><sub>6,13,10,10,8</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>5,9,3,4,5</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,1,0,1,4</sub> |  | 1.7<br><sub>2,2,1,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.9 | 1.6 | 22.3 |
| Naji Marshall (DAL) | 93% | 25.1<br><sub>15,25,23,30,23</sub> | 12.5<br><sub>8,6,13,12,13</sub> |  | 3.6<br><sub>1,5,1,3,2</sub> |  | 3.8<br><sub>2,2,4,5,2</sub> |  | 0.9<br><sub>1,0,1,0,3</sub> |  | 1.0 | 0.1 | 1.9 | 19.9 |
| Caleb Martin (DAL) | 98% | 20.9<br><sub>19,19,21,33,34</sub> | 5.8<br><sub>2,0,7,15,12</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>2,3,2,8,5</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,5,5,3,5</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.6<br><sub>0,0,1,1,4</sub> |  | 0.8 | 0.3 | 0.8 | 10.9 |
| Zaccharie Risacher (DAL) | 98% | 20.3<br><sub>16,15,25,14,27</sub> | 7.7<br><sub>11,4,22,5,18</sub> |  | 4.0<br><sub>6,2,6,2,5</sub> |  | 1.1<br><sub>1,0,3,0,0</sub> |  | 0.9<br><sub>1,0,4,1,1</sub> |  | 0.8 | 0.6 | 0.9 | 12.8 |
| Daniel Gafford (DAL) | 98% | 19.3<br><sub>19,20,16,17,19</sub> | 8.9<br><sub>18,8,3,10,3</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>5,2,3,3,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,3,1,1,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.6 | 1.3 | 1.0 | 15.7 |
| Walter Clayton Jr. (DAL) | 89% | 17.8<br><sub>16,25,22,13,23</sub> | 6.7<br><sub>5,6,5,2,13</sub> |  | 2.9<br><sub>4,6,1,2,4</sub> |  | 3.1<br><sub>6,4,4,2,3</sub> |  | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.2 | 1.4 | 12.7 |
| Morez Johnson Jr. (DAL) | 98% | 16.3<br><sub>19,-,13,15,26</sub> | 6.0<br><sub>4,-,0,4,2</sub> |  | 3.3<br><sub>9,-,2,2,6</sub> |  | 1.4<br><sub>1,-,0,0,4</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.9 | 10.8 |
| Santi Aldama (DAL) | 91% | 14.4<br><sub>15,19,10,16,-</sub> | 7.1<br><sub>12,10,3,7,-</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>2,4,1,2,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,1,1,1,-</sub> |  | 0.8<br><sub>2,1,1,2,-</sub> |  | 0.5 | 0.3 | 0.9 | 11.7 |
| Marcus Sasser (DAL) | 64% | 13.7<br><sub>9,-,9,-,18</sub> | 4.9<br><sub>4,-,3,-,5</sub> |  | 1.2<br><sub>0,-,1,-,1</sub> |  | 1.6<br><sub>0,-,0,-,2</sub> |  | 0.6<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.1 | 0.8 | 7.7 |
| Moussa Cisse (DAL) | 63% | 6.6<br><sub>5,-,8,-,4</sub> | 2.3<br><sub>2,-,0,-,1</sub> |  | 2.6<br><sub>1,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.0<br><sub>0,-,0,-,0</sub> |  | 0.2 | 0.5 | 0.4 | 5.1 |
| Jett Howard (DAL) | 63% | 6.2<br><sub>3,-,5,-,7</sub> | 2.6<br><sub>5,-,3,-,0</sub> |  | 0.7<br><sub>1,-,0,-,0</sub> |  | 0.4<br><sub>0,-,0,-,1</sub> |  | 0.2<br><sub>1,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.7 |
| Yaxel Lendeborg (GSW) | 98% | 34.2<br><sub>37,27,36,24,33</sub> | 24.2<br><sub>23,23,25,3,28</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>8,7,10,7,8</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>3,4,0,1,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>2,4,2,0,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.8 | 3.5 | 36.1 |
| Brandin Podziemski (GSW) | 96% | 34.1<br><sub>39,26,37,22,30</sub> | 19.2<br><sub>15,25,22,8,15</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>7,2,6,3,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>1,4,4,0,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>4,5,4,2,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 2.1 | 29.7 |
| Draymond Green (GSW) | 100% | 28.8<br><sub>34,21,27,16,25</sub> | 6.3<br><sub>2,2,7,4,2</sub> | 5.5 · – | 5.7<br><sub>6,3,5,3,8</sub> | 4.5 | 6.9<br><sub>13,6,7,3,5</sub> | 5.5 | 0.7<br><sub>0,0,1,0,0</sub> |  | 1.1 | 0.8 | 2.7 | 18.8 |
| De'Anthony Melton (GSW) | 98% | 24.9<br><sub>17,26,25,18,21</sub> | 13.3<br><sub>4,16,11,8,8</sub> |  | 4.1<br><sub>1,4,4,4,2</sub> |  | 3.0<br><sub>1,3,4,3,1</sub> |  | 1.9<br><sub>1,4,3,2,2</sub> |  | 1.4 | 0.4 | 1.8 | 20.4 |
| Will Richard (GSW) | 98% | 23.6<br><sub>12,-,19,30,23</sub> | 7.3<br><sub>4,-,9,7,11</sub> |  | 3.0<br><sub>2,-,4,4,3</sub> |  | 1.5<br><sub>1,-,0,1,1</sub> |  | 0.9<br><sub>0,-,2,1,2</sub> |  | 1.2 | 0.2 | 0.9 | 11.8 |
| Georges Niang (GSW) | 98% | 20.8<br><sub>25,19,19,15,14</sub> | 9.0<br><sub>11,9,5,5,0</sub> |  | 3.2<br><sub>2,2,5,3,4</sub> |  | 1.5<br><sub>1,2,0,2,2</sub> |  | 1.4<br><sub>3,1,1,1,0</sub> |  | 0.4 | 0.2 | 1.0 | 13.7 |
| LJ Cryer (GSW) | 84% | 20.5<br><sub>-,20,18,24,24</sub> | 10.0<br><sub>-,10,13,20,7</sub> |  | 1.8<br><sub>-,0,1,2,1</sub> |  | 2.2<br><sub>-,3,1,6,3</sub> |  | 1.6<br><sub>-,2,3,6,1</sub> |  | 0.5 | 0.1 | 1.1 | 14.0 |
| Gui Santos (GSW) | 91% | 20.4<br><sub>12,21,12,21,19</sub> | 9.0<br><sub>3,3,0,7,12</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>1,7,3,4,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>0,4,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>0,0,0,1,1</sub> |  | 0.8 | 0.3 | 1.4 | 15.3 |
| Charles Bassey (GSW) | 98% | 17.1<br><sub>11,18,13,20,16</sub> | 8.2<br><sub>8,12,7,11,4</sub> |  | 6.6<br><sub>4,10,6,5,0</sub> |  | 1.0<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.0 | 15.9 |
| Gary Payton II (GSW) | 88% | 16.5<br><sub>13,-,-,13,8</sub> | 7.5<br><sub>4,-,-,2,2</sub> |  | 3.0<br><sub>0,-,-,2,0</sub> |  | 1.4<br><sub>0,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.9 | 0.3 | 0.8 | 11.9 |
| Graham Ike (GSW) | 91% | 11.5<br><sub>-,12,4,13,8</sub> | 5.0<br><sub>-,4,4,5,3</sub> |  | 3.0<br><sub>-,5,0,2,5</sub> |  | 1.2<br><sub>-,2,1,3,1</sub> |  | 0.3<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.3 | 0.6 | 9.2 |
| Malevy Leons (GSW) | 67% | 10.0<br><sub>-,12,4,14,6</sub> | 2.9<br><sub>-,0,0,5,2</sub> |  | 1.9<br><sub>-,3,3,1,1</sub> |  | 0.6<br><sub>-,0,0,0,0</sub> |  | 0.1<br><sub>-,0,0,1,0</sub> |  | 0.4 | 0.4 | 0.5 | 5.4 |

</details>


### UTA @ LAL
Out: Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.9–124.0 | UTA 13% | 7.92 / 1.14 | LAL -16.5 | 231.5 | LAL -10.5 covers 65%; o228.5 57% |
| Expected (weighted by chance each plays) | 107.9–124.7 | UTA 12% | 8.15 / 1.14 | LAL -16.5 | 232.5 | LAL -10.5 covers 67%; o228.5 59% |
| if Jaxson Hayes plays | 108.7–122.8 | UTA 16% | 6.38 / 1.19 | LAL -14.5 | 231.5 | LAL -10.5 covers 60%; o228.5 57% |
| if Walker Kessler plays | 107.6–125.1 | UTA 11% | 9.31 / 1.12 | LAL -17.5 | 232.5 | LAL -10.5 covers 69%; o228.5 59% |
| if Austin Reaves plays | 107.8–125.2 | UTA 11% | 9.23 / 1.12 | LAL -17.5 | 233.5 | LAL -10.5 covers 69%; o228.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaxson Hayes (UTA) | Day-To-Day | 70% | 21.4 | 8.2 | 5.1 | 1.1 | 0.0 | 0.7 | 0.8 | 1.0 | 14.4 | full tables below |
| Walker Kessler (LAL) | Day-To-Day | 70% | 28.4 | 12.2 | 11.8 | 1.9 | 0.1 | 0.9 | 2.4 | 1.6 | 25.8 | full tables below |
| Austin Reaves (LAL) | Day-To-Day | 70% | 31.8 | 21.8 | 4.1 | 5.0 | 2.1 | 1.2 | 0.5 | 2.7 | 30.9 | full tables below |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 33.9<br><sub>-,33,38,34,35</sub> | 21.1<br><sub>-,13,27,13,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.4 | 31.4 |
| Darryn Peterson | 98% | 33.5<br><sub>31,33,34,34,31</sub> | 18.3<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.6 | 2.2 | 26.9 |
| Ace Bailey | 99% | 32.4<br><sub>35,31,35,30,23</sub> | 15.7<br><sub>23,18,21,7,5</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,2,1,4,4</sub> |  | 2.2<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.8 | 1.7 | 23.1 |
| Brice Sensabaugh | 99% | 28.7<br><sub>14,23,27,30,35</sub> | 16.5<br><sub>5,19,7,14,40</sub> |  | 4.5<br><sub>4,3,3,7,11</sub> |  | 2.4<br><sub>4,1,1,2,5</sub> |  | 2.6<br><sub>1,3,1,0,8</sub> |  | 0.9 | 0.3 | 2.3 | 23.4 |
| Mo Bamba | 88% | 25.9<br><sub>17,18,20,36,31</sub> | 9.4<br><sub>7,5,9,26,15</sub> |  | 8.2<br><sub>7,1,9,5,10</sub> |  | 1.3<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.5 | 1.2 | 19.0 |
| Josh Okogie | 97% | 24.9<br><sub>21,15,22,27,22</sub> | 6.8<br><sub>6,7,7,7,9</sub> |  | 3.7<br><sub>4,3,2,6,2</sub> |  | 1.5<br><sub>4,0,1,0,4</sub> |  | 0.8<br><sub>0,1,2,2,1</sub> |  | 1.3 | 0.2 | 1.0 | 11.9 |
| Svi Mykhailiuk | 97% | 22.4<br><sub>21,20,7,21,33</sub> | 8.0<br><sub>7,3,0,6,8</sub> |  | 2.5<br><sub>2,0,1,2,7</sub> |  | 1.8<br><sub>3,2,0,3,5</sub> |  | 1.4<br><sub>1,1,0,2,2</sub> |  | 0.6 | 0.1 | 0.9 | 12.3 |
| Josh Green | 96% | 20.3<br><sub>30,26,14,15,13</sub> | 4.6<br><sub>2,3,2,6,9</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>5,2,0,1,1</sub> |  | 1.1<br><sub>4,1,0,1,0</sub> |  | 0.6<br><sub>0,1,0,2,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.6 |
| Isaiah Collier | 63% | 18.2<br><sub>24,12,16,-,-</sub> | 8.6<br><sub>17,7,3,-,-</sub> |  | 2.6<br><sub>5,3,2,-,-</sub> |  | 4.7<br><sub>5,2,5,-,-</sub> |  | 0.5<br><sub>4,1,1,-,-</sub> |  | 0.8 | 0.2 | 1.9 | 15.9 |
| Tony Bradley | 72% | 15.2<br><sub>14,-,12,12,17</sub> | 4.8<br><sub>4,-,0,6,3</sub> |  | 4.4<br><sub>5,-,5,2,7</sub> |  | 0.7<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.4 | 0.7 | 9.9 |
| Kyle Filipowski | 52% | 14.8<br><sub>15,-,2,-,-</sub> | 7.1<br><sub>7,-,2,-,-</sub> |  | 4.5<br><sub>4,-,0,-,-</sub> |  | 1.5<br><sub>1,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.7 | 0.2 | 1.1 | 13.1 |
| Kobe Bufkin | 23% | 11.7<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.7 |
| Jonas Aidoo | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Harrison Ingram | 8% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.5<br><sub>-,39,32,36,42</sub> | 41.5<br><sub>-,32,32,43,36</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>-,10,5,9,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 5.3<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.8 | 4.1 | 57.2 |
| Quentin Grimes | 98% | 32.9<br><sub>32,-,-,37,42</sub> | 14.7<br><sub>12,-,-,22,47</sub> |  | 4.2<br><sub>1,-,-,6,6</sub> |  | 3.2<br><sub>4,-,-,1,3</sub> |  | 2.0<br><sub>2,-,-,5,10</sub> |  | 1.1 | 0.4 | 1.6 | 22.1 |
| Matisse Thybulle | 98% | 28.1<br><sub>28,23,23,26,31</sub> | 8.7<br><sub>4,6,8,12,7</sub> |  | 3.6<br><sub>2,0,5,8,6</sub> |  | 1.4<br><sub>0,1,1,0,0</sub> |  | 1.6<br><sub>0,2,2,2,2</sub> |  | 2.9 | 1.1 | 1.1 | 13.7 |
| Jake LaRavia | 98% | 26.4<br><sub>29,32,21,32,23</sub> | 7.4<br><sub>5,4,0,12,4</sub> |  | 4.7<br><sub>1,3,9,3,5</sub> |  | 2.2<br><sub>2,3,6,3,2</sub> |  | 0.8<br><sub>0,0,0,2,0</sub> |  | 1.3 | 0.9 | 1.1 | 14.4 |
| Sandro Mamukelashvili | 99% | 24.7<br><sub>18,32,26,21,23</sub> | 11.8<br><sub>7,23,23,4,3</sub> |  | 5.6<br><sub>3,8,3,2,3</sub> |  | 1.9<br><sub>0,3,2,3,2</sub> |  | 1.6<br><sub>1,5,5,0,0</sub> |  | 0.9 | 0.6 | 0.9 | 19.3 |
| Ziaire Williams | 98% | 24.0<br><sub>21,28,20,19,24</sub> | 9.8<br><sub>17,12,9,6,0</sub> |  | 3.1<br><sub>2,2,1,2,1</sub> |  | 1.6<br><sub>0,2,5,3,1</sub> |  | 1.4<br><sub>4,2,1,0,0</sub> |  | 1.5 | 0.4 | 0.9 | 14.4 |
| Collin Sexton | 98% | 23.8<br><sub>24,27,13,24,25</sub> | 15.2<br><sub>17,18,10,16,10</sub> |  | 2.6<br><sub>2,2,1,0,4</sub> |  | 3.1<br><sub>2,6,3,3,3</sub> |  | 1.5<br><sub>0,3,0,2,1</sub> |  | 1.0 | 0.2 | 1.7 | 21.0 |
| Carson Cooper | 52% | 15.6<br><sub>-,-,-,-,18</sub> | 3.8<br><sub>-,-,-,-,3</sub> |  | 4.4<br><sub>-,-,-,-,4</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.6 | 0.8 | 9.6 |
| Jarred Vanderbilt | 88% | 14.6<br><sub>14,13,9,12,14</sub> | 3.5<br><sub>2,4,4,2,4</sub> |  | 4.5<br><sub>10,2,3,4,7</sub> |  | 1.2<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 9.2 |
| Kevon Looney | 52% | 12.3<br><sub>-,-,4,-,17</sub> | 2.5<br><sub>-,-,0,-,4</sub> |  | 4.8<br><sub>-,-,2,-,8</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.4 | 8.2 |
| Adou Thiero | 72% | 10.9<br><sub>8,7,14,-,6</sub> | 3.3<br><sub>2,2,2,-,0</sub> |  | 2.8<br><sub>2,2,2,-,0</sub> |  | 0.9<br><sub>0,1,1,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 7.0 |
| Cameron Carr | 63% | 9.1<br><sub>-,7,13,-,-</sub> | 5.0<br><sub>-,2,0,-,-</sub> |  | 1.6<br><sub>-,3,2,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 7.2 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| AK Okereke | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Jaden Hardy | 48% | 8.3<br><sub>-,-,4,-,-</sub> | 4.4<br><sub>-,-,3,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 6.0 |
| Chris Manon | 52% | 6.9<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.2 | 3.5 |
| Bronny James | 48% | 6.6<br><sub>-,-,4,-,-</sub> | 2.3<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 3.0 |

</details>

<details><summary>if Jaxson Hayes plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 36.5<br><sub>-,39,32,36,42</sub> | 41.4<br><sub>-,32,32,43,36</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.4<br><sub>-,10,5,9,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 5.3<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.7 | 4.1 | 57.1 |
| Quentin Grimes (LAL) | 98% | 32.9<br><sub>32,-,-,37,42</sub> | 14.6<br><sub>12,-,-,22,47</sub> |  | 4.2<br><sub>1,-,-,6,6</sub> |  | 3.2<br><sub>4,-,-,1,3</sub> |  | 2.0<br><sub>2,-,-,5,10</sub> |  | 1.1 | 0.4 | 1.6 | 22.1 |
| Matisse Thybulle (LAL) | 98% | 28.1<br><sub>28,23,23,26,31</sub> | 8.7<br><sub>4,6,8,12,7</sub> |  | 3.6<br><sub>2,0,5,8,6</sub> |  | 1.4<br><sub>0,1,1,0,0</sub> |  | 1.6<br><sub>0,2,2,2,2</sub> |  | 2.9 | 1.1 | 1.1 | 13.7 |
| Jake LaRavia (LAL) | 98% | 26.4<br><sub>29,32,21,32,23</sub> | 7.4<br><sub>5,4,0,12,4</sub> |  | 4.7<br><sub>1,3,9,3,5</sub> |  | 2.3<br><sub>2,3,6,3,2</sub> |  | 0.8<br><sub>0,0,0,2,0</sub> |  | 1.3 | 0.9 | 1.1 | 14.4 |
| Sandro Mamukelashvili (LAL) | 99% | 24.7<br><sub>18,32,26,21,23</sub> | 11.8<br><sub>7,23,23,4,3</sub> |  | 5.5<br><sub>3,8,3,2,3</sub> |  | 1.9<br><sub>0,3,2,3,2</sub> |  | 1.6<br><sub>1,5,5,0,0</sub> |  | 0.9 | 0.6 | 0.9 | 19.3 |
| Ziaire Williams (LAL) | 98% | 23.9<br><sub>21,28,20,19,24</sub> | 9.7<br><sub>17,12,9,6,0</sub> |  | 3.0<br><sub>2,2,1,2,1</sub> |  | 1.5<br><sub>0,2,5,3,1</sub> |  | 1.4<br><sub>4,2,1,0,0</sub> |  | 1.5 | 0.4 | 0.9 | 14.3 |
| Collin Sexton (LAL) | 98% | 23.8<br><sub>24,27,13,24,25</sub> | 15.0<br><sub>17,18,10,16,10</sub> |  | 2.6<br><sub>2,2,1,0,4</sub> |  | 3.2<br><sub>2,6,3,3,3</sub> |  | 1.6<br><sub>0,3,0,2,1</sub> |  | 1.0 | 0.2 | 1.7 | 20.8 |
| Carson Cooper (LAL) | 52% | 15.6<br><sub>-,-,-,-,18</sub> | 3.8<br><sub>-,-,-,-,3</sub> |  | 4.4<br><sub>-,-,-,-,4</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.6 | 0.8 | 9.5 |
| Jarred Vanderbilt (LAL) | 88% | 14.6<br><sub>14,13,9,12,14</sub> | 3.5<br><sub>2,4,4,2,4</sub> |  | 4.5<br><sub>10,2,3,4,7</sub> |  | 1.2<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 9.2 |
| Kevon Looney (LAL) | 52% | 12.3<br><sub>-,-,4,-,17</sub> | 2.6<br><sub>-,-,0,-,4</sub> |  | 4.8<br><sub>-,-,2,-,8</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.5 | 0.4 | 8.3 |
| Adou Thiero (LAL) | 72% | 10.9<br><sub>8,7,14,-,6</sub> | 3.4<br><sub>2,2,2,-,0</sub> |  | 2.8<br><sub>2,2,2,-,0</sub> |  | 0.9<br><sub>0,1,1,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 7.0 |
| Cameron Carr (LAL) | 63% | 9.2<br><sub>-,7,13,-,-</sub> | 5.0<br><sub>-,2,0,-,-</sub> |  | 1.6<br><sub>-,3,2,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 7.2 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Jaden Hardy (LAL) | 48% | 8.4<br><sub>-,-,4,-,-</sub> | 4.5<br><sub>-,-,3,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 6.0 |
| Chris Manon (LAL) | 52% | 6.9<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 3.5 |
| Bronny James (LAL) | 48% | 6.5<br><sub>-,-,4,-,-</sub> | 2.3<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.9 |
| Keyonte George (UTA) | 98% | 33.2<br><sub>-,33,38,34,35</sub> | 21.1<br><sub>-,13,27,13,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.3 | 31.3 |
| Darryn Peterson (UTA) | 98% | 32.3<br><sub>31,33,34,34,31</sub> | 17.8<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.6 | 2.2 | 25.9 |
| Ace Bailey (UTA) | 99% | 31.2<br><sub>35,31,35,30,23</sub> | 14.6<br><sub>23,18,21,7,5</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,2,1,4,4</sub> |  | 2.0<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.8 | 1.8 | 21.6 |
| Brice Sensabaugh (UTA) | 99% | 25.0<br><sub>14,23,27,30,35</sub> | 14.8<br><sub>5,19,7,14,40</sub> |  | 3.9<br><sub>4,3,3,7,11</sub> |  | 2.0<br><sub>4,1,1,2,5</sub> |  | 2.1<br><sub>1,3,1,0,8</sub> |  | 0.7 | 0.2 | 2.1 | 20.8 |
| Mo Bamba (UTA) | 88% | 23.4<br><sub>17,18,20,36,31</sub> | 8.8<br><sub>7,5,9,26,15</sub> |  | 7.4<br><sub>7,1,9,5,10</sub> |  | 1.2<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.4 | 1.1 | 17.3 |
| Josh Okogie (UTA) | 97% | 21.8<br><sub>21,15,22,27,22</sub> | 6.0<br><sub>6,7,7,7,9</sub> |  | 3.2<br><sub>4,3,2,6,2</sub> |  | 1.2<br><sub>4,0,1,0,4</sub> |  | 0.7<br><sub>0,1,2,2,1</sub> |  | 1.1 | 0.2 | 0.9 | 10.5 |
| Jaxson Hayes (UTA) | 100% | 21.4<br><sub>17,30,13,-,-</sub> | 8.2<br><sub>6,11,12,-,-</sub> |  | 5.1<br><sub>2,8,5,-,-</sub> |  | 1.1<br><sub>1,0,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.7 | 0.8 | 1.0 | 14.4 |
| Svi Mykhailiuk (UTA) | 97% | 18.6<br><sub>21,20,7,21,33</sub> | 6.6<br><sub>7,3,0,6,8</sub> |  | 2.0<br><sub>2,0,1,2,7</sub> |  | 1.4<br><sub>3,2,0,3,5</sub> |  | 1.1<br><sub>1,1,0,2,2</sub> |  | 0.5 | 0.1 | 0.8 | 10.1 |
| Josh Green (UTA) | 96% | 16.9<br><sub>30,26,14,15,13</sub> | 3.8<br><sub>2,3,2,6,9</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>5,2,0,1,1</sub> |  | 0.8<br><sub>4,1,0,1,0</sub> |  | 0.4<br><sub>0,1,0,2,1</sub> |  | 0.6 | 0.1 | 0.6 | 6.3 |
| Isaiah Collier (UTA) | 63% | 15.6<br><sub>24,12,16,-,-</sub> | 7.3<br><sub>17,7,3,-,-</sub> |  | 2.2<br><sub>5,3,2,-,-</sub> |  | 4.0<br><sub>5,2,5,-,-</sub> |  | 0.4<br><sub>4,1,1,-,-</sub> |  | 0.7 | 0.2 | 1.6 | 13.5 |
| Tony Bradley (UTA) | 72% | 13.1<br><sub>14,-,12,12,17</sub> | 4.2<br><sub>4,-,0,6,3</sub> |  | 3.9<br><sub>5,-,5,2,7</sub> |  | 0.6<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.7 |
| Kyle Filipowski (UTA) | 52% | 11.5<br><sub>15,-,2,-,-</sub> | 5.8<br><sub>7,-,2,-,-</sub> |  | 3.4<br><sub>4,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.3 |
| Kobe Bufkin (UTA) | 23% | 9.5<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.4 |
| Jonas Aidoo (UTA) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Harrison Ingram (UTA) | 8% | 8.5<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>

<details><summary>if Austin Reaves plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 33.8<br><sub>-,39,32,36,42</sub> | 36.4<br><sub>-,32,32,43,36</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 7.6<br><sub>-,10,5,9,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 4.7<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.6 | 3.8 | 51.2 |
| Austin Reaves (LAL) | 100% | 31.8<br><sub>37,-,25,-,-</sub> | 21.8<br><sub>43,-,18,-,-</sub> | 21.5 · – | 4.1<br><sub>5,-,3,-,-</sub> | 3.5 | 5.0<br><sub>4,-,5,-,-</sub> | 4.5 | 2.1<br><sub>4,-,1,-,-</sub> | 1.5 | 1.2 | 0.5 | 2.7 | 30.9 |
| Quentin Grimes (LAL) | 98% | 27.9<br><sub>32,-,-,37,42</sub> | 11.4<br><sub>12,-,-,22,47</sub> |  | 3.6<br><sub>1,-,-,6,6</sub> |  | 2.6<br><sub>4,-,-,1,3</sub> |  | 1.5<br><sub>2,-,-,5,10</sub> |  | 1.0 | 0.3 | 1.3 | 17.6 |
| Matisse Thybulle (LAL) | 98% | 23.6<br><sub>28,23,23,26,31</sub> | 7.0<br><sub>4,6,8,12,7</sub> |  | 3.0<br><sub>2,0,5,8,6</sub> |  | 1.1<br><sub>0,1,1,0,0</sub> |  | 1.3<br><sub>0,2,2,2,2</sub> |  | 2.6 | 0.8 | 0.9 | 11.2 |
| Jake LaRavia (LAL) | 98% | 22.9<br><sub>29,32,21,32,23</sub> | 6.4<br><sub>5,4,0,12,4</sub> |  | 4.2<br><sub>1,3,9,3,5</sub> |  | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> |  | 1.2 | 0.7 | 1.0 | 12.5 |
| Sandro Mamukelashvili (LAL) | 99% | 22.2<br><sub>18,32,26,21,23</sub> | 9.9<br><sub>7,23,23,4,3</sub> |  | 5.1<br><sub>3,8,3,2,3</sub> |  | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.3<br><sub>1,5,5,0,0</sub> |  | 0.8 | 0.5 | 0.8 | 16.8 |
| Ziaire Williams (LAL) | 98% | 21.4<br><sub>21,28,20,19,24</sub> | 8.3<br><sub>17,12,9,6,0</sub> |  | 2.8<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> |  | 1.3 | 0.3 | 0.8 | 12.4 |
| Collin Sexton (LAL) | 98% | 19.8<br><sub>24,27,13,24,25</sub> | 12.5<br><sub>17,18,10,16,10</sub> |  | 2.2<br><sub>2,2,1,0,4</sub> |  | 2.6<br><sub>2,6,3,3,3</sub> |  | 1.2<br><sub>0,3,0,2,1</sub> |  | 0.9 | 0.2 | 1.4 | 17.4 |
| Jarred Vanderbilt (LAL) | 88% | 13.1<br><sub>14,13,9,12,14</sub> | 3.4<br><sub>2,4,4,2,4</sub> |  | 4.2<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.6 |
| Carson Cooper (LAL) | 52% | 12.8<br><sub>-,-,-,-,18</sub> | 3.6<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.5 | 0.7 | 8.2 |
| Kevon Looney (LAL) | 52% | 9.8<br><sub>-,-,4,-,17</sub> | 2.3<br><sub>-,-,0,-,4</sub> |  | 4.0<br><sub>-,-,2,-,8</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.3 | 7.1 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Adou Thiero (LAL) | 72% | 7.6<br><sub>8,7,14,-,6</sub> | 2.5<br><sub>2,2,2,-,0</sub> |  | 2.1<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.3 |
| Jaden Hardy (LAL) | 48% | 6.8<br><sub>-,-,4,-,-</sub> | 4.0<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.3 |
| Cameron Carr (LAL) | 63% | 6.6<br><sub>-,7,13,-,-</sub> | 3.6<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.2 |
| Chris Manon (LAL) | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.2 |
| Bronny James (LAL) | 48% | 5.6<br><sub>-,-,4,-,-</sub> | 2.4<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.0 |
| Keyonte George (UTA) | 98% | 34.0<br><sub>-,33,38,34,35</sub> | 21.2<br><sub>-,13,27,13,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.4 | 31.5 |
| Darryn Peterson (UTA) | 98% | 33.4<br><sub>31,33,34,34,31</sub> | 18.2<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.6 | 2.2 | 26.8 |
| Ace Bailey (UTA) | 99% | 32.3<br><sub>35,31,35,30,23</sub> | 15.6<br><sub>23,18,21,7,5</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,2,1,4,4</sub> |  | 2.2<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.8 | 1.7 | 22.9 |
| Brice Sensabaugh (UTA) | 99% | 28.8<br><sub>14,23,27,30,35</sub> | 16.6<br><sub>5,19,7,14,40</sub> |  | 4.5<br><sub>4,3,3,7,11</sub> |  | 2.4<br><sub>4,1,1,2,5</sub> |  | 2.6<br><sub>1,3,1,0,8</sub> |  | 0.9 | 0.3 | 2.3 | 23.6 |
| Mo Bamba (UTA) | 88% | 25.9<br><sub>17,18,20,36,31</sub> | 9.4<br><sub>7,5,9,26,15</sub> |  | 8.2<br><sub>7,1,9,5,10</sub> |  | 1.3<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.5 | 1.2 | 18.9 |
| Josh Okogie (UTA) | 97% | 24.9<br><sub>21,15,22,27,22</sub> | 6.8<br><sub>6,7,7,7,9</sub> |  | 3.7<br><sub>4,3,2,6,2</sub> |  | 1.4<br><sub>4,0,1,0,4</sub> |  | 0.8<br><sub>0,1,2,2,1</sub> |  | 1.3 | 0.2 | 1.0 | 11.9 |
| Svi Mykhailiuk (UTA) | 97% | 22.3<br><sub>21,20,7,21,33</sub> | 7.9<br><sub>7,3,0,6,8</sub> |  | 2.5<br><sub>2,0,1,2,7</sub> |  | 1.8<br><sub>3,2,0,3,5</sub> |  | 1.4<br><sub>1,1,0,2,2</sub> |  | 0.6 | 0.1 | 0.9 | 12.2 |
| Josh Green (UTA) | 96% | 20.4<br><sub>30,26,14,15,13</sub> | 4.7<br><sub>2,3,2,6,9</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>5,2,0,1,1</sub> |  | 1.1<br><sub>4,1,0,1,0</sub> |  | 0.6<br><sub>0,1,0,2,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.6 |
| Isaiah Collier (UTA) | 63% | 18.3<br><sub>24,12,16,-,-</sub> | 8.6<br><sub>17,7,3,-,-</sub> |  | 2.6<br><sub>5,3,2,-,-</sub> |  | 4.7<br><sub>5,2,5,-,-</sub> |  | 0.5<br><sub>4,1,1,-,-</sub> |  | 0.8 | 0.2 | 1.9 | 15.9 |
| Tony Bradley (UTA) | 72% | 15.2<br><sub>14,-,12,12,17</sub> | 4.8<br><sub>4,-,0,6,3</sub> |  | 4.4<br><sub>5,-,5,2,7</sub> |  | 0.7<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.4 | 0.7 | 9.9 |
| Kyle Filipowski (UTA) | 52% | 14.7<br><sub>15,-,2,-,-</sub> | 7.1<br><sub>7,-,2,-,-</sub> |  | 4.5<br><sub>4,-,0,-,-</sub> |  | 1.4<br><sub>1,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.7 | 0.2 | 1.1 | 13.0 |
| Kobe Bufkin (UTA) | 23% | 11.6<br><sub>-,-,-,-,-</sub> | 4.7<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.7 |
| Jonas Aidoo (UTA) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Harrison Ingram (UTA) | 8% | 8.4<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.7 |

</details>

<details><summary>if Walker Kessler plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic (LAL) | 98% | 34.5<br><sub>-,39,32,36,42</sub> | 40.1<br><sub>-,32,32,43,36</sub> | 35.5 · –<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>-,8,5,3,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 8.0<br><sub>-,10,5,9,7</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 5.0<br><sub>-,3,5,5,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.9 | 0.6 | 4.0 | 55.0 |
| Quentin Grimes (LAL) | 98% | 29.2<br><sub>32,-,-,37,42</sub> | 12.8<br><sub>12,-,-,22,47</sub> |  | 3.6<br><sub>1,-,-,6,6</sub> |  | 3.0<br><sub>4,-,-,1,3</sub> |  | 1.7<br><sub>2,-,-,5,10</sub> |  | 1.0 | 0.3 | 1.5 | 19.4 |
| Walker Kessler (LAL) | 100% | 28.4<br><sub>29,30,29,32,-</sub> | 12.2<br><sub>12,21,10,14,-</sub> | 14.5 · – | 11.8<br><sub>16,10,11,12,-</sub> | 11.5 | 1.9<br><sub>4,4,3,3,-</sub> | 1.5 | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.9 | 2.4 | 1.6 | 25.8 |
| Matisse Thybulle (LAL) | 98% | 24.3<br><sub>28,23,23,26,31</sub> | 7.8<br><sub>4,6,8,12,7</sub> |  | 3.0<br><sub>2,0,5,8,6</sub> |  | 1.2<br><sub>0,1,1,0,0</sub> |  | 1.4<br><sub>0,2,2,2,2</sub> |  | 2.6 | 0.9 | 1.1 | 12.1 |
| Jake LaRavia (LAL) | 98% | 23.0<br><sub>29,32,21,32,23</sub> | 6.5<br><sub>5,4,0,12,4</sub> |  | 4.0<br><sub>1,3,9,3,5</sub> |  | 2.0<br><sub>2,3,6,3,2</sub> |  | 0.7<br><sub>0,0,0,2,0</sub> |  | 1.2 | 0.7 | 1.1 | 12.5 |
| Sandro Mamukelashvili (LAL) | 99% | 22.2<br><sub>18,32,26,21,23</sub> | 10.5<br><sub>7,23,23,4,3</sub> |  | 4.8<br><sub>3,8,3,2,3</sub> |  | 1.8<br><sub>0,3,2,3,2</sub> |  | 1.4<br><sub>1,5,5,0,0</sub> |  | 0.8 | 0.5 | 0.8 | 17.1 |
| Ziaire Williams (LAL) | 98% | 21.6<br><sub>21,28,20,19,24</sub> | 8.8<br><sub>17,12,9,6,0</sub> |  | 2.6<br><sub>2,2,1,2,1</sub> |  | 1.4<br><sub>0,2,5,3,1</sub> |  | 1.2<br><sub>4,2,1,0,0</sub> |  | 1.3 | 0.3 | 0.8 | 12.8 |
| Collin Sexton (LAL) | 98% | 21.0<br><sub>24,27,13,24,25</sub> | 13.7<br><sub>17,18,10,16,10</sub> |  | 2.2<br><sub>2,2,1,0,4</sub> |  | 2.9<br><sub>2,6,3,3,3</sub> |  | 1.4<br><sub>0,3,0,2,1</sub> |  | 0.9 | 0.2 | 1.7 | 18.8 |
| Jarred Vanderbilt (LAL) | 88% | 13.2<br><sub>14,13,9,12,14</sub> | 3.5<br><sub>2,4,4,2,4</sub> |  | 4.1<br><sub>10,2,3,4,7</sub> |  | 1.1<br><sub>3,0,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Carson Cooper (LAL) | 52% | 12.4<br><sub>-,-,-,-,18</sub> | 3.5<br><sub>-,-,-,-,3</sub> |  | 3.6<br><sub>-,-,-,-,4</sub> |  | 1.1<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 8.2 |
| Kevon Looney (LAL) | 52% | 10.0<br><sub>-,-,4,-,17</sub> | 2.3<br><sub>-,-,0,-,4</sub> |  | 3.9<br><sub>-,-,2,-,8</sub> |  | 0.9<br><sub>-,-,0,-,0</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.4 | 0.4 | 0.4 | 7.1 |
| AK Okereke (LAL) | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Adou Thiero (LAL) | 72% | 7.8<br><sub>8,7,14,-,6</sub> | 2.6<br><sub>2,2,2,-,0</sub> |  | 2.0<br><sub>2,2,2,-,0</sub> |  | 0.7<br><sub>0,1,1,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Cameron Carr (LAL) | 63% | 7.0<br><sub>-,7,13,-,-</sub> | 3.8<br><sub>-,2,0,-,-</sub> |  | 1.2<br><sub>-,3,2,-,-</sub> |  | 0.5<br><sub>-,0,0,-,-</sub> |  | 0.3<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.6 |
| Jaden Hardy (LAL) | 48% | 7.0<br><sub>-,-,4,-,-</sub> | 4.1<br><sub>-,-,3,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.4 |
| Bronny James (LAL) | 48% | 5.7<br><sub>-,-,4,-,-</sub> | 2.2<br><sub>-,-,4,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 2.8 |
| Chris Manon (LAL) | 52% | 5.7<br><sub>-,-,-,-,-</sub> | 1.7<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 3.2 |
| Keyonte George (UTA) | 98% | 33.9<br><sub>-,33,38,34,35</sub> | 21.1<br><sub>-,13,27,13,30</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>-,7,4,4,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.5<br><sub>-,7,7,8,11</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>-,2,4,1,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 3.4 | 31.4 |
| Darryn Peterson (UTA) | 98% | 33.4<br><sub>31,33,34,34,31</sub> | 18.2<br><sub>25,22,28,17,13</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>4,4,7,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>4,5,2,4,2</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>4,2,4,3,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.2 | 0.6 | 2.2 | 26.8 |
| Ace Bailey (UTA) | 99% | 32.4<br><sub>35,31,35,30,23</sub> | 15.6<br><sub>23,18,21,7,5</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>7,7,3,8,1</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>2,2,1,4,4</sub> |  | 2.2<br><sub>3,3,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.8 | 1.7 | 23.0 |
| Brice Sensabaugh (UTA) | 99% | 28.7<br><sub>14,23,27,30,35</sub> | 16.6<br><sub>5,19,7,14,40</sub> |  | 4.5<br><sub>4,3,3,7,11</sub> |  | 2.4<br><sub>4,1,1,2,5</sub> |  | 2.6<br><sub>1,3,1,0,8</sub> |  | 0.9 | 0.3 | 2.3 | 23.5 |
| Mo Bamba (UTA) | 88% | 25.8<br><sub>17,18,20,36,31</sub> | 9.4<br><sub>7,5,9,26,15</sub> |  | 8.2<br><sub>7,1,9,5,10</sub> |  | 1.3<br><sub>0,1,1,4,3</sub> |  | 0.6<br><sub>0,0,0,6,1</sub> |  | 0.6 | 1.5 | 1.2 | 18.9 |
| Josh Okogie (UTA) | 97% | 24.8<br><sub>21,15,22,27,22</sub> | 6.7<br><sub>6,7,7,7,9</sub> |  | 3.7<br><sub>4,3,2,6,2</sub> |  | 1.4<br><sub>4,0,1,0,4</sub> |  | 0.8<br><sub>0,1,2,2,1</sub> |  | 1.3 | 0.3 | 1.0 | 11.8 |
| Svi Mykhailiuk (UTA) | 97% | 22.2<br><sub>21,20,7,21,33</sub> | 7.9<br><sub>7,3,0,6,8</sub> |  | 2.5<br><sub>2,0,1,2,7</sub> |  | 1.8<br><sub>3,2,0,3,5</sub> |  | 1.4<br><sub>1,1,0,2,2</sub> |  | 0.6 | 0.1 | 0.9 | 12.1 |
| Josh Green (UTA) | 96% | 20.5<br><sub>30,26,14,15,13</sub> | 4.7<br><sub>2,3,2,6,9</sub> | 4.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>5,2,0,1,1</sub> |  | 1.1<br><sub>4,1,0,1,0</sub> |  | 0.6<br><sub>0,1,0,2,1</sub> |  | 0.8 | 0.1 | 0.7 | 7.7 |
| Isaiah Collier (UTA) | 63% | 18.2<br><sub>24,12,16,-,-</sub> | 8.5<br><sub>17,7,3,-,-</sub> |  | 2.6<br><sub>5,3,2,-,-</sub> |  | 4.7<br><sub>5,2,5,-,-</sub> |  | 0.5<br><sub>4,1,1,-,-</sub> |  | 0.8 | 0.2 | 1.9 | 15.8 |
| Tony Bradley (UTA) | 72% | 15.2<br><sub>14,-,12,12,17</sub> | 4.8<br><sub>4,-,0,6,3</sub> |  | 4.4<br><sub>5,-,5,2,7</sub> |  | 0.7<br><sub>0,-,1,0,1</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.4 | 0.7 | 9.8 |
| Kyle Filipowski (UTA) | 52% | 14.9<br><sub>15,-,2,-,-</sub> | 7.1<br><sub>7,-,2,-,-</sub> |  | 4.5<br><sub>4,-,0,-,-</sub> |  | 1.5<br><sub>1,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.7 | 0.2 | 1.1 | 13.1 |
| Kobe Bufkin (UTA) | 23% | 11.7<br><sub>-,-,-,-,-</sub> | 4.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.9 |
| Jonas Aidoo (UTA) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.8 |
| Harrison Ingram (UTA) | 8% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>


### PHX @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Mark Williams (PHX)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.9–112.1 | PHX 71% | 1.40 / 3.50 | SAC +7.5 | 231.5 | SAC +7.5 covers 49%; o226.5 61% |
| Expected (weighted by chance each plays) | 119.1–113.0 | PHX 67% | 1.48 / 3.07 | SAC +6.5 | 232.5 | SAC +7.5 covers 53%; o226.5 62% |
| if Precious Achiuwa plays | 119.5–112.9 | PHX 68% | 1.46 / 3.17 | SAC +6.5 | 232.5 | SAC +7.5 covers 52%; o226.5 62% |
| if De'Andre Hunter plays | 119.5–113.0 | PHX 68% | 1.46 / 3.17 | SAC +6.5 | 232.5 | SAC +7.5 covers 52%; o226.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa (SAC) | Questionable | 55% | 25.4 | 11.1 | 6.9 | 1.4 | 0.4 | 1.0 | 0.9 | 1.3 | 19.3 | full tables below |
| De'Andre Hunter (SAC) | Questionable | 55% | 33.4 | 15.2 | 4.8 | 1.8 | 1.9 | 0.9 | 0.2 | 1.8 | 21.8 | full tables below |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.4<br><sub>29,29,35,28,37</sub> | 27.4<br><sub>32,17,30,17,20</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 6.1<br><sub>4,5,7,7,8</sub> |  | 2.2<br><sub>3,2,4,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.7 | 36.9 |
| Dillon Brooks | 98% | 29.0<br><sub>26,22,30,22,27</sub> | 16.2<br><sub>7,8,15,1,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.2 | 1.4 | 21.6 |
| Miles Bridges | 98% | 28.1<br><sub>26,18,25,24,29</sub> | 14.5<br><sub>7,8,11,14,16</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>5,4,6,3,8</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.5 | 1.2 | 23.0 |
| Jalen Green | 98% | 26.4<br><sub>24,21,21,21,27</sub> | 15.3<br><sub>6,13,12,9,16</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.3 | 2.0 | 21.8 |
| Collin Gillespie | 98% | 25.0<br><sub>24,22,27,28,26</sub> | 10.4<br><sub>6,12,13,26,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,2,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.1 | 1.0 | 17.4 |
| Oso Ighodaro | 98% | 24.9<br><sub>18,20,32,17,33</sub> | 6.6<br><sub>7,6,2,4,8</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.4 | 15.8 |
| Jordan Goodwin | 98% | 20.3<br><sub>-,14,24,31,20</sub> | 8.4<br><sub>-,18,6,14,11</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.2 | 0.7 | 14.7 |
| Luke Kennard | 98% | 17.8<br><sub>14,22,21,23,17</sub> | 7.5<br><sub>3,14,8,18,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,1,6,2</sub> |  | 1.8<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.5 | 0.1 | 0.6 | 11.2 |
| Ryan Dunn | 98% | 15.4<br><sub>23,25,10,24,12</sub> | 4.5<br><sub>3,10,0,3,5</sub> |  | 3.3<br><sub>2,8,4,6,1</sub> |  | 1.0<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.4 | 0.5 | 8.9 |
| Khaman Maluach | 98% | 14.3<br><sub>20,22,16,13,11</sub> | 5.3<br><sub>11,11,4,7,4</sub> |  | 4.7<br><sub>5,7,2,4,6</sub> |  | 0.6<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 10.6 |
| Rasheer Fleming | 43% | 8.5<br><sub>9,12,-,-,-</sub> | 3.2<br><sub>2,4,-,-,-</sub> |  | 1.5<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.9 |
| Jamaree Bouyea | 48% | 6.9<br><sub>9,8,-,-,-</sub> | 2.9<br><sub>4,7,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.9 |
| Pat Spencer | 52% | 6.8<br><sub>6,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Koa Peat | 67% | 6.6<br><sub>6,6,-,8,1</sub> | 3.3<br><sub>4,5,-,10,0</sub> |  | 1.5<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| Drew Timme | 8% | 6.5 | 2.7 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.1 | 0.4 | 4.4 |
| Duop Reath | 48% | 6.3<br><sub>6,-,-,-,-</sub> | 2.8<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>2,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.5 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 38.2<br><sub>33,39,40,35,33</sub> | 27.0<br><sub>22,32,29,17,26</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,3,4,3,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.3 | 4.7 | 38.9 |
| Zach LaVine | 76% | 34.3<br><sub>35,25,33,36,-</sub> | 21.5<br><sub>14,15,31,12,-</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>4,4,3,3,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.2<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.3 | 3.0 | 28.3 |
| Domantas Sabonis | 98% | 34.1<br><sub>31,-,24,35,29</sub> | 16.2<br><sub>17,-,0,21,11</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 13.0<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 0.4<br><sub>1,-,0,1,0</sub> |  | 0.9 | 0.3 | 2.9 | 34.9 |
| Keegan Murray | 98% | 32.0<br><sub>-,23,24,40,21</sub> | 13.0<br><sub>-,10,11,16,6</sub> |  | 4.8<br><sub>-,1,2,7,1</sub> |  | 1.7<br><sub>-,2,1,4,0</sub> |  | 1.5<br><sub>-,0,2,2,2</sub> |  | 0.9 | 1.0 | 1.2 | 19.5 |
| Leaky Black | 86% | 27.0<br><sub>40,20,18,12,29</sub> | 6.7<br><sub>12,6,0,0,12</sub> |  | 4.6<br><sub>3,5,3,0,9</sub> |  | 1.8<br><sub>5,1,2,0,2</sub> |  | 1.0<br><sub>4,2,0,0,4</sub> |  | 1.3 | 0.7 | 0.8 | 13.1 |
| Malik Monk | 98% | 22.7<br><sub>18,21,3,18,29</sub> | 12.6<br><sub>12,9,1,7,14</sub> |  | 2.4<br><sub>0,2,0,4,1</sub> |  | 4.3<br><sub>7,3,0,3,10</sub> |  | 1.7<br><sub>2,0,0,0,1</sub> |  | 0.7 | 0.4 | 1.9 | 19.2 |
| Alex Karaban | 52% | 22.1<br><sub>11,-,-,-,29</sub> | 4.7<br><sub>0,-,-,-,0</sub> |  | 3.0<br><sub>1,-,-,-,5</sub> |  | 1.1<br><sub>0,-,-,-,1</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.8 | 0.3 | 1.0 | 8.8 |
| Dylan Cardwell | 98% | 20.7<br><sub>15,18,29,13,19</sub> | 6.8<br><sub>9,4,1,6,10</sub> |  | 7.7<br><sub>2,9,11,3,6</sub> |  | 1.7<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.1 | 16.2 |
| Emanuel Sharp | 98% | 19.1<br><sub>31,12,19,7,21</sub> | 6.1<br><sub>9,5,2,4,9</sub> |  | 1.7<br><sub>5,1,2,0,0</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 0.8<br><sub>3,1,0,0,1</sub> |  | 0.7 | 0.3 | 0.7 | 8.7 |
| Daeqwon Plowden | 88% | 17.3<br><sub>-,12,2,2,24</sub> | 6.8<br><sub>-,6,0,0,13</sub> |  | 2.0<br><sub>-,0,0,0,2</sub> |  | 0.8<br><sub>-,0,0,0,1</sub> |  | 1.1<br><sub>-,2,0,0,3</sub> |  | 0.5 | 0.2 | 0.7 | 9.6 |
| Mason Plumlee | 52% | 9.1<br><sub>-,-,-,-,5</sub> | 2.7<br><sub>-,-,-,-,2</sub> |  | 2.9<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.4 | 0.6 | 6.3 |

</details>

<details><summary>if De'Andre Hunter plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker (PHX) | 98% | 34.5<br><sub>29,29,35,28,37</sub> | 27.3<br><sub>32,17,30,17,20</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>4,5,7,7,8</sub> |  | 2.2<br><sub>3,2,4,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.8 | 36.8 |
| Dillon Brooks (PHX) | 98% | 29.0<br><sub>26,22,30,22,27</sub> | 16.2<br><sub>7,8,15,1,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.2 | 1.4 | 21.6 |
| Miles Bridges (PHX) | 98% | 28.2<br><sub>26,18,25,24,29</sub> | 14.5<br><sub>7,8,11,14,16</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>5,4,6,3,8</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.5 | 1.2 | 23.1 |
| Jalen Green (PHX) | 98% | 26.5<br><sub>24,21,21,21,27</sub> | 15.4<br><sub>6,13,12,9,16</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.3 | 2.1 | 21.9 |
| Oso Ighodaro (PHX) | 98% | 25.0<br><sub>18,20,32,17,33</sub> | 6.6<br><sub>7,6,2,4,8</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.4 | 15.8 |
| Collin Gillespie (PHX) | 98% | 24.9<br><sub>24,22,27,28,26</sub> | 10.3<br><sub>6,12,13,26,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>2,2,2,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.1 | 1.0 | 17.3 |
| Jordan Goodwin (PHX) | 98% | 20.4<br><sub>-,14,24,31,20</sub> | 8.4<br><sub>-,18,6,14,11</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.2 | 0.8 | 14.8 |
| Luke Kennard (PHX) | 98% | 17.7<br><sub>14,22,21,23,17</sub> | 7.5<br><sub>3,14,8,18,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,1,6,2</sub> |  | 1.8<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.5 | 0.1 | 0.6 | 11.2 |
| Ryan Dunn (PHX) | 98% | 15.4<br><sub>23,25,10,24,12</sub> | 4.5<br><sub>3,10,0,3,5</sub> |  | 3.3<br><sub>2,8,4,6,1</sub> |  | 1.0<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.4 | 0.5 | 8.8 |
| Khaman Maluach (PHX) | 98% | 14.3<br><sub>20,22,16,13,11</sub> | 5.3<br><sub>11,11,4,7,4</sub> |  | 4.7<br><sub>5,7,2,4,6</sub> |  | 0.6<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 10.6 |
| Rasheer Fleming (PHX) | 43% | 8.5<br><sub>9,12,-,-,-</sub> | 3.2<br><sub>2,4,-,-,-</sub> |  | 1.4<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Jamaree Bouyea (PHX) | 48% | 6.9<br><sub>9,8,-,-,-</sub> | 2.9<br><sub>4,7,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.0 |
| Pat Spencer (PHX) | 52% | 6.8<br><sub>6,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Koa Peat (PHX) | 67% | 6.6<br><sub>6,6,-,8,1</sub> | 3.3<br><sub>4,5,-,10,0</sub> |  | 1.5<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| Duop Reath (PHX) | 48% | 6.3<br><sub>6,-,-,-,-</sub> | 2.8<br><sub>2,-,-,-,-</sub> |  | 1.3<br><sub>2,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.2 | 4.4 |
| Drew Timme (PHX) | 8% | 6.3 | 2.4 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.0 | 0.4 | 4.1 |
| Darius Acuff Jr. (SAC) | 98% | 36.2<br><sub>33,39,40,35,33</sub> | 24.4<br><sub>22,32,29,17,26</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.3<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>3,3,4,3,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.2 | 4.3 | 35.6 |
| De'Andre Hunter (SAC) | 100% | 33.4<br><sub>-,31,34,42,-</sub> | 15.2<br><sub>-,14,15,24,-</sub> | 13.5 · – | 4.8<br><sub>-,3,4,5,-</sub> | 3.5 | 1.8<br><sub>-,1,2,2,-</sub> | 1.5 | 1.9<br><sub>-,2,3,2,-</sub> | 1.5 | 0.9 | 0.2 | 1.8 | 21.8 |
| Domantas Sabonis (SAC) | 98% | 32.2<br><sub>31,-,24,35,29</sub> | 15.0<br><sub>17,-,0,21,11</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 12.1<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>1,-,0,1,0</sub> |  | 0.9 | 0.3 | 2.6 | 32.5 |
| Zach LaVine (SAC) | 76% | 31.7<br><sub>35,25,33,36,-</sub> | 19.1<br><sub>14,15,31,12,-</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>4,4,3,3,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.9<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.3 | 2.6 | 25.2 |
| Keegan Murray (SAC) | 98% | 28.4<br><sub>-,23,24,40,21</sub> | 11.3<br><sub>-,10,11,16,6</sub> |  | 4.3<br><sub>-,1,2,7,1</sub> |  | 1.5<br><sub>-,2,1,4,0</sub> |  | 1.3<br><sub>-,0,2,2,2</sub> |  | 0.9 | 1.0 | 1.1 | 17.1 |
| Leaky Black (SAC) | 86% | 21.9<br><sub>40,20,18,12,29</sub> | 5.5<br><sub>12,6,0,0,12</sub> |  | 3.7<br><sub>3,5,3,0,9</sub> |  | 1.4<br><sub>5,1,2,0,2</sub> |  | 0.7<br><sub>4,2,0,0,4</sub> |  | 1.0 | 0.5 | 0.6 | 10.6 |
| Malik Monk (SAC) | 98% | 18.9<br><sub>18,21,3,18,29</sub> | 10.4<br><sub>12,9,1,7,14</sub> |  | 2.0<br><sub>0,2,0,4,1</sub> |  | 3.5<br><sub>7,3,0,3,10</sub> |  | 1.3<br><sub>2,0,0,0,1</sub> |  | 0.6 | 0.3 | 1.5 | 15.9 |
| Dylan Cardwell (SAC) | 98% | 17.9<br><sub>15,18,29,13,19</sub> | 5.9<br><sub>9,4,1,6,10</sub> |  | 6.5<br><sub>2,9,11,3,6</sub> |  | 1.4<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 1.0 | 13.8 |
| Alex Karaban (SAC) | 52% | 16.9<br><sub>11,-,-,-,29</sub> | 3.5<br><sub>0,-,-,-,0</sub> |  | 2.3<br><sub>1,-,-,-,5</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 6.5 |
| Emanuel Sharp (SAC) | 98% | 16.2<br><sub>31,12,19,7,21</sub> | 5.0<br><sub>9,5,2,4,9</sub> |  | 1.4<br><sub>5,1,2,0,0</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.6<br><sub>3,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.7 | 7.1 |
| Daeqwon Plowden (SAC) | 88% | 13.9<br><sub>-,12,2,2,24</sub> | 5.5<br><sub>-,6,0,0,13</sub> |  | 1.6<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.8<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.5 | 7.8 |
| Mason Plumlee (SAC) | 52% | 7.0<br><sub>-,-,-,-,5</sub> | 2.0<br><sub>-,-,-,-,2</sub> |  | 2.2<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 4.9 |

</details>

<details><summary>if Precious Achiuwa plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker (PHX) | 98% | 34.5<br><sub>29,29,35,28,37</sub> | 27.2<br><sub>32,17,30,17,20</sub> | 26.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,3,1,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>4,5,7,7,8</sub> |  | 2.2<br><sub>3,2,4,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.3 | 2.8 | 36.8 |
| Dillon Brooks (PHX) | 98% | 29.1<br><sub>26,22,30,22,27</sub> | 16.2<br><sub>7,8,15,1,15</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>4,4,3,2,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.9<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>1,0,3,0,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.8 | 0.2 | 1.4 | 21.8 |
| Miles Bridges (PHX) | 98% | 28.2<br><sub>26,18,25,24,29</sub> | 14.5<br><sub>7,8,11,14,16</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>5,4,6,3,8</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>0,2,0,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.5 | 1.2 | 23.1 |
| Jalen Green (PHX) | 98% | 26.4<br><sub>24,21,21,21,27</sub> | 15.3<br><sub>6,13,12,9,16</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,5,4,2,5</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>4,1,0,1,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,3,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.3 | 2.1 | 21.8 |
| Collin Gillespie (PHX) | 98% | 24.9<br><sub>24,22,27,28,26</sub> | 10.3<br><sub>6,12,13,26,10</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,2,2,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.0<br><sub>3,8,1,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>2,4,3,5,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.1 | 1.0 | 17.3 |
| Oso Ighodaro (PHX) | 98% | 24.9<br><sub>18,20,32,17,33</sub> | 6.5<br><sub>7,6,2,4,8</sub> | 6.5 · –<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>4,8,3,2,11</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>2,2,7,3,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.8 | 1.4 | 15.8 |
| Jordan Goodwin (PHX) | 98% | 20.4<br><sub>-,14,24,31,20</sub> | 8.4<br><sub>-,18,6,14,11</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>-,3,5,7,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>-,1,2,6,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>-,6,2,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.2 | 0.8 | 14.7 |
| Luke Kennard (PHX) | 98% | 17.8<br><sub>14,22,21,23,17</sub> | 7.4<br><sub>3,14,8,18,12</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,1,6,2</sub> |  | 1.8<br><sub>0,3,1,4,0</sub> |  | 1.1<br><sub>1,3,0,3,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.5 | 0.1 | 0.6 | 11.1 |
| Ryan Dunn (PHX) | 98% | 15.4<br><sub>23,25,10,24,12</sub> | 4.5<br><sub>3,10,0,3,5</sub> |  | 3.3<br><sub>2,8,4,6,1</sub> |  | 1.0<br><sub>0,2,0,1,0</sub> |  | 0.5<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.3 | 0.5 | 8.9 |
| Khaman Maluach (PHX) | 98% | 14.3<br><sub>20,22,16,13,11</sub> | 5.4<br><sub>11,11,4,7,4</sub> |  | 4.7<br><sub>5,7,2,4,6</sub> |  | 0.6<br><sub>2,3,1,0,0</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 10.7 |
| Rasheer Fleming (PHX) | 43% | 8.5<br><sub>9,12,-,-,-</sub> | 3.1<br><sub>2,4,-,-,-</sub> |  | 1.4<br><sub>1,2,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Jamaree Bouyea (PHX) | 48% | 6.9<br><sub>9,8,-,-,-</sub> | 2.9<br><sub>4,7,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.1<br><sub>3,3,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.0 |
| Pat Spencer (PHX) | 52% | 6.9<br><sub>6,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 0.9<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.7 |
| Koa Peat (PHX) | 67% | 6.6<br><sub>6,6,-,8,1</sub> | 3.3<br><sub>4,5,-,10,0</sub> |  | 1.5<br><sub>0,1,-,2,1</sub> |  | 0.3<br><sub>1,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| Duop Reath (PHX) | 48% | 6.3<br><sub>6,-,-,-,-</sub> | 2.8<br><sub>2,-,-,-,-</sub> |  | 1.4<br><sub>2,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.2 | 4.5 |
| Drew Timme (PHX) | 8% | 6.2 | 2.5 |  | 1.1 |  | 0.6 |  | 0.1 |  | 0.2 | 0.0 | 0.4 | 4.2 |
| Darius Acuff Jr. (SAC) | 98% | 37.2<br><sub>33,39,40,35,33</sub> | 25.5<br><sub>22,32,29,17,26</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>3,5,4,4,0</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 7.5<br><sub>8,10,6,6,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,3,4,3,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.2 | 4.5 | 37.1 |
| Zach LaVine (SAC) | 76% | 33.1<br><sub>35,25,33,36,-</sub> | 20.4<br><sub>14,15,31,12,-</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>4,4,3,3,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.0<br><sub>3,2,2,6,-</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>1,1,6,3,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.3 | 2.8 | 26.8 |
| Domantas Sabonis (SAC) | 98% | 32.9<br><sub>31,-,24,35,29</sub> | 15.1<br><sub>17,-,0,21,11</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 12.4<br><sub>12,-,2,12,13</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>5,-,5,5,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>1,-,0,1,0</sub> |  | 0.9 | 0.3 | 2.8 | 33.1 |
| Keegan Murray (SAC) | 98% | 29.1<br><sub>-,23,24,40,21</sub> | 11.8<br><sub>-,10,11,16,6</sub> |  | 4.3<br><sub>-,1,2,7,1</sub> |  | 1.5<br><sub>-,2,1,4,0</sub> |  | 1.4<br><sub>-,0,2,2,2</sub> |  | 0.9 | 1.0 | 1.1 | 17.7 |
| Precious Achiuwa (SAC) | 100% | 25.4<br><sub>22,36,14,-,-</sub> | 11.1<br><sub>9,7,10,-,-</sub> | 8.5 · – | 6.9<br><sub>4,14,3,-,-</sub> | 5.5 | 1.4<br><sub>0,2,0,-,-</sub> |  | 0.4<br><sub>1,0,1,-,-</sub> |  | 1.0 | 0.9 | 1.3 | 19.3 |
| Leaky Black (SAC) | 86% | 22.9<br><sub>40,20,18,12,29</sub> | 5.6<br><sub>12,6,0,0,12</sub> |  | 3.8<br><sub>3,5,3,0,9</sub> |  | 1.5<br><sub>5,1,2,0,2</sub> |  | 0.8<br><sub>4,2,0,0,4</sub> |  | 1.1 | 0.5 | 0.7 | 10.9 |
| Malik Monk (SAC) | 98% | 19.4<br><sub>18,21,3,18,29</sub> | 10.8<br><sub>12,9,1,7,14</sub> |  | 2.0<br><sub>0,2,0,4,1</sub> |  | 3.7<br><sub>7,3,0,3,10</sub> |  | 1.4<br><sub>2,0,0,0,1</sub> |  | 0.6 | 0.3 | 1.6 | 16.5 |
| Dylan Cardwell (SAC) | 98% | 18.3<br><sub>15,18,29,13,19</sub> | 6.0<br><sub>9,4,1,6,10</sub> |  | 6.5<br><sub>2,9,11,3,6</sub> |  | 1.5<br><sub>3,3,1,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.2 | 1.0 | 14.1 |
| Alex Karaban (SAC) | 52% | 18.0<br><sub>11,-,-,-,29</sub> | 3.7<br><sub>0,-,-,-,0</sub> |  | 2.3<br><sub>1,-,-,-,5</sub> |  | 0.9<br><sub>0,-,-,-,1</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.9 | 6.9 |
| Emanuel Sharp (SAC) | 98% | 16.7<br><sub>31,12,19,7,21</sub> | 5.1<br><sub>9,5,2,4,9</sub> |  | 1.5<br><sub>5,1,2,0,0</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.6<br><sub>3,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.7 | 7.3 |
| Daeqwon Plowden (SAC) | 88% | 14.4<br><sub>-,12,2,2,24</sub> | 5.8<br><sub>-,6,0,0,13</sub> |  | 1.6<br><sub>-,0,0,0,2</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.8<br><sub>-,2,0,0,3</sub> |  | 0.4 | 0.1 | 0.6 | 8.1 |
| Mason Plumlee (SAC) | 52% | 7.2<br><sub>-,-,-,-,5</sub> | 2.2<br><sub>-,-,-,-,2</sub> |  | 2.3<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 5.0 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-18/`._
