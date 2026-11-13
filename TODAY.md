# NBA model · Fri 13 Nov 2026 (US date)

Updated **Sat 14 Nov, 08:16 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-13/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| IND to win | NYK @ IND | sportsbet | 3.85 | 3.61 | 4.25 | 23.5% | 27.7% | 27.7% | +6.6% | -9.5% | 0.6% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| SAC to win | POR @ SAC | sportsbet | 5.60 | 4.98 | 3.71 | 27.0% | 20.1% | 20.1% | +12.5% | +51.1% | 0.7% |
| Scoot Henderson AST over 5.5 (6+) | POR @ SAC | draftkings | 18.20 | 16.31 | 7.89 | 12.7% | 5.1% | 6.1% | +11.6% | +130.6% | 0.2% |
| Kevin Durant PRA over 49.5 (50+) | UTA @ HOU | draftkings | 17.80 | 15.95 | 7.73 | 12.9% | 5.2% | 6.3% | +11.5% | +130.3% | 0.2% |
| Kevin Durant PA over 44.5 (45+) | UTA @ HOU | draftkings | 22.00 | 19.92 | 9.91 | 10.1% | 4.2% | 5.0% | +10.4% | +122.0% | 0.1% |
| Kevin Durant PA over 39.5 (40+) | UTA @ HOU | draftkings | 12.00 | 10.88 | 5.44 | 18.4% | 7.8% | 9.2% | +10.2% | +120.6% | 0.2% |
| Kevin Durant PTS over 39.5 (40+) | UTA @ HOU | draftkings | 24.00 | 21.83 | 11.01 | 9.1% | 3.9% | 4.6% | +9.9% | +118.0% | 0.1% |
| Kevin Durant PRA over 44.5 (45+) | UTA @ HOU | draftkings | 9.20 | 8.47 | 4.41 | 22.7% | 10.2% | 11.8% | +8.6% | +108.4% | 0.3% |
| Derik Queen PTS over 24.5 (25+) | MEM @ NOP | draftkings | 26.00 | 23.98 | 12.56 | 8.0% | 3.6% | 4.2% | +8.4% | +106.9% | 0.1% |
| Kevin Durant AST over 7.5 (8+) | UTA @ HOU | draftkings | 13.40 | 12.38 | 6.51 | 15.4% | 7.0% | 8.1% | +8.3% | +105.9% | 0.2% |
| Cam Spencer AST over 9.5 (10+) | MEM @ NOP | draftkings | 21.00 | 19.49 | 10.39 | 9.6% | 4.5% | 5.1% | +7.8% | +102.2% | 0.1% |
| Derik Queen PA over 29.5 (30+) | MEM @ NOP | draftkings | 27.00 | 25.06 | 13.38 | 7.5% | 3.5% | 4.0% | +7.8% | +101.7% | 0.1% |
| Kevin Durant PR over 44.5 (45+) | UTA @ HOU | draftkings | 16.80 | 15.62 | 8.38 | 11.9% | 5.6% | 6.4% | +7.6% | +100.5% | 0.1% |
| Kevin Durant PTS over 34.5 (35+) | UTA @ HOU | draftkings | 11.40 | 10.64 | 5.78 | 17.3% | 8.2% | 9.4% | +7.2% | +97.2% | 0.2% |
| Cam Spencer AST over 7.5 (8+) | MEM @ NOP | draftkings | 8.40 | 7.86 | 4.32 | 23.2% | 11.1% | 12.7% | +6.8% | +94.6% | 0.2% |
| UTA to win | UTA @ HOU | sportsbet | 10.50 | 9.92 | 10.36 | 9.7% | 10.1% | 10.1% | +5.8% | +1.4% | 0.1% |
| Bam Adebayo REB over 15.5 (16+) | CLE @ MIA | draftkings | 17.80 | 16.92 | 9.74 | 10.3% | 5.2% | 5.9% | +5.2% | +82.7% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| NYK @ IND | Sat 14 Nov 11:00 | 117.2–107.0 | NYK 77% | 1.30 / 4.29 | IND +10.5 | 224.5 | IND +8.5 covers 45%; o219.5 60% |
| MIL @ ORL | Sat 14 Nov 11:00 | 106.3–110.4 | MIL 38% | 2.60 / 1.62 | ORL -4.5 | 216.5 | ORL -9.5 covers 35%; o224.5 34% |
| CLE @ MIA | Sat 14 Nov 12:00 | 119.2–118.9 | CLE 51% | 1.98 / 2.02 | MIA +0.5 | 238.5 | MIA -2.5 covers 44%; o236.5 53% |
| ATL @ CHI | Sat 14 Nov 12:00 | 124.4–116.4 | ATL 72% | 1.40 / 3.51 | CHI +8.5 | 240.5 | CHI +7.5 covers 48%; o245.5 40% |
| MEM @ NOP | Sat 14 Nov 12:00 | 122.6–118.5 | MEM 61% | 1.64 / 2.56 | NOP +4.5 | 240.5 | NOP +3.5 covers 47%; o235.5 61% |
| UTA @ HOU | Sat 14 Nov 12:30 | 103.5–121.9 | UTA 10% | 10.36 / 1.11 | HOU -18.5 | 225.5 | HOU -15.5 covers 58%; o220.5 60% |
| GSW @ SAS | Sat 14 Nov 13:30 | 109.9–114.3 | GSW 37% | 2.68 / 1.60 | SAS -4.5 | 224.5 | SAS -12.5 covers 28%; o217.5 64% |
| POR @ SAC | Sat 14 Nov 14:00 | 119.7–111.2 | POR 73% | 1.37 / 3.71 | SAC +8.5 | 230.5 | SAC +10.5 covers 55%; o229.5 53% |
| OKC @ LAC | Sat 14 Nov 14:30 | 113.1–109.4 | OKC 61% | 1.65 / 2.53 | LAC +3.5 | 222.5 | LAC +7.5 covers 61%; o222.5 50% |

### NYK @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), Ben Sheppard (IND)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.2–107.0 | NYK 77% | 1.30 / 4.29 | IND +10.5 | 224.5 | IND +8.5 covers 45%; o219.5 60% |
| Expected (weighted by chance each plays) | 117.4–107.3 | NYK 76% | 1.31 / 4.25 | IND +10.5 | 224.5 | IND +8.5 covers 45%; o219.5 62% |
| if Aaron Nesmith plays | 117.6–107.6 | NYK 76% | 1.31 / 4.22 | IND +10.5 | 225.5 | IND +8.5 covers 46%; o219.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aaron Nesmith (IND) | Questionable | 55% | 26.3 | 12.2 | 3.0 | 1.6 | 1.8 | 0.6 | 0.4 | 1.3 | 16.9 | full tables below |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 33.4<br><sub>34,28,34,28,35</sub> | 26.8<br><sub>19,33,31,23,27</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>2,2,6,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.9<br><sub>6,4,9,2,5</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>4,5,3,1,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.2 | 2.2 | 36.0 |
| OG Anunoby | 98% | 32.5<br><sub>38,24,34,29,34</sub> | 17.3<br><sub>18,18,15,19,14</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>4,5,6,3,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>3,1,3,5,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.7 | 1.6 | 24.7 |
| Karl-Anthony Towns | 98% | 31.3<br><sub>35,25,34,27,34</sub> | 19.2<br><sub>11,17,29,21,21</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 13.1<br><sub>16,12,13,16,11</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>5,1,3,3,8</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>1,2,2,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.7 | 2.7 | 36.0 |
| Josh Hart | 98% | 30.2<br><sub>27,-,-,-,26</sub> | 9.6<br><sub>8,-,-,-,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>6,-,-,-,4</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>7,-,-,-,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>2,-,-,-,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.2 | 1.5 | 21.1 |
| Landry Shamet | 98% | 24.9<br><sub>30,25,29,28,29</sub> | 8.9<br><sub>22,7,9,10,12</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,2,1,3,2</sub> |  | 1.6<br><sub>1,2,1,2,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>4,1,3,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.6 | 0.2 | 0.7 | 12.3 |
| Mikal Bridges | 98% | 24.5<br><sub>16,22,31,17,17</sub> | 8.6<br><sub>6,7,9,4,2</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,4,6,5,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>0,4,4,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0<br><sub>0,1,1,0,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9 | 0.4 | 0.8 | 13.8 |
| Miles McBride | 98% | 19.8<br><sub>17,11,16,25,27</sub> | 7.8<br><sub>6,7,5,8,19</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>1,1,0,0,2</sub> |  | 1.6<br><sub>2,1,0,3,2</sub> |  | 1.3<br><sub>2,2,1,2,5</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.2 | 0.5 | 11.2 |
| Andre Drummond | 98% | 13.8<br><sub>13,12,14,16,14</sub> | 4.5<br><sub>4,6,0,2,0</sub> | 3.5 · –<br><sub>o 54% · u 46%</sub> | 6.8<br><sub>9,9,8,14,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>0,0,0,3,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.7 | 12.4 |
| Tyler Kolek | 91% | 12.8<br><sub>5,11,14,15,13</sub> | 4.3<br><sub>2,0,0,12,4</sub> |  | 1.7<br><sub>1,0,4,3,1</sub> |  | 3.7<br><sub>1,5,5,4,4</sub> |  | 0.4<br><sub>0,0,0,2,0</sub> |  | 0.5 | 0.1 | 0.7 | 9.8 |
| Mohamed Diawara | 72% | 12.2<br><sub>6,21,14,18,11</sub> | 4.3<br><sub>0,8,2,5,2</sub> |  | 2.1<br><sub>1,6,3,3,0</sub> |  | 1.4<br><sub>0,4,3,3,0</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.8 |
| Jordan Clarkson | 71% | 9.5<br><sub>11,15,15,11,-</sub> | 4.8<br><sub>7,10,9,2,-</sub> |  | 1.4<br><sub>0,1,2,4,-</sub> |  | 0.7<br><sub>0,1,0,2,-</sub> |  | 0.3<br><sub>1,2,1,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 7.0 |
| Jose Alvarado | 63% | 8.6<br><sub>9,9,-,6,-</sub> | 3.3<br><sub>0,0,-,0,-</sub> |  | 1.1<br><sub>0,0,-,1,-</sub> |  | 1.4<br><sub>0,2,-,1,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 5.9 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Dalton Knecht | 64% | 7.1<br><sub>-,16,5,8,-</sub> | 3.3<br><sub>-,10,0,3,-</sub> |  | 1.4<br><sub>-,7,0,0,-</sub> |  | 0.4<br><sub>-,1,0,0,-</sub> |  | 0.3<br><sub>-,2,0,1,-</sub> |  | 0.2 | 0.1 | 0.2 | 5.1 |
| Jaden Akins | 38% | 6.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| James Wiseman | 52% | 6.6<br><sub>-,10,-,5,-</sub> | 2.5<br><sub>-,8,-,0,-</sub> |  | 2.3<br><sub>-,8,-,1,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.2 |
| Pacome Dadiet | 48% | 6.3<br><sub>-,9,-,6,-</sub> | 3.1<br><sub>-,4,-,8,-</sub> |  | 1.3<br><sub>-,0,-,2,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 88% | 34.3<br><sub>-,38,31,34,34</sub> | 17.5<br><sub>-,22,9,12,17</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>-,2,1,3,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 8.5<br><sub>-,5,8,12,10</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>-,2,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.2 | 2.5 | 28.9 |
| Pascal Siakam | 88% | 33.7<br><sub>-,30,32,35,32</sub> | 22.6<br><sub>-,20,23,29,28</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>-,4,2,9,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.6<br><sub>-,2,5,8,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>-,2,2,5,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.4 | 2.2 | 33.8 |
| Kelly Oubre Jr. | 80% | 28.5<br><sub>-,-,16,23,34</sub> | 11.5<br><sub>-,-,2,14,14</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>-,-,1,2,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>-,-,0,2,1</sub> |  | 1.1<br><sub>-,-,0,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.5 | 1.1 | 16.9 |
| Ivica Zubac | 67% | 27.2<br><sub>-,19,19,28,31</sub> | 11.4<br><sub>-,1,10,16,20</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>-,4,12,3,12</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>-,2,5,0,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.9 | 1.6 | 21.9 |
| Quenton Jackson | 98% | 24.3<br><sub>35,22,17,25,21</sub> | 10.8<br><sub>20,13,6,10,4</sub> |  | 3.2<br><sub>7,7,4,5,2</sub> |  | 3.4<br><sub>3,2,1,4,2</sub> |  | 1.2<br><sub>1,3,0,2,1</sub> |  | 0.9 | 0.2 | 1.4 | 17.4 |
| Obi Toppin | 76% | 20.5<br><sub>-,19,22,19,16</sub> | 11.2<br><sub>-,11,10,10,8</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>-,5,7,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>-,1,2,4,1</sub> |  | 1.5<br><sub>-,1,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.5 | 0.3 | 1.0 | 17.4 |
| Jarace Walker | 98% | 18.5<br><sub>45,17,20,10,7</sub> | 7.6<br><sub>15,2,9,7,1</sub> |  | 3.8<br><sub>7,8,5,1,1</sub> |  | 1.7<br><sub>3,1,2,0,0</sub> |  | 1.0<br><sub>1,0,1,2,0</sub> |  | 0.6 | 0.3 | 1.1 | 13.1 |
| Kobe Brown | 72% | 17.1<br><sub>38,7,-,-,-</sub> | 6.1<br><sub>16,0,-,-,-</sub> |  | 3.0<br><sub>6,1,-,-,-</sub> |  | 1.5<br><sub>1,0,-,-,-</sub> |  | 0.7<br><sub>2,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.8 | 10.6 |
| Jay Huff | 80% | 16.1<br><sub>40,14,10,-,11</sub> | 6.8<br><sub>22,6,0,-,6</sub> |  | 2.9<br><sub>8,3,3,-,4</sub> |  | 1.1<br><sub>2,1,0,-,0</sub> |  | 0.9<br><sub>0,2,0,-,0</sub> |  | 0.3 | 1.0 | 0.8 | 10.9 |
| T.J. McConnell | 91% | 16.0<br><sub>-,-,9,8,14</sub> | 8.2<br><sub>-,-,6,2,7</sub> |  | 2.1<br><sub>-,-,2,0,3</sub> |  | 4.7<br><sub>-,-,1,3,7</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.7 | 0.2 | 1.1 | 15.1 |
| Jalen Slawson | 80% | 14.2<br><sub>41,6,12,-,12</sub> | 4.1<br><sub>12,2,4,-,2</sub> |  | 2.6<br><sub>7,2,1,-,3</sub> |  | 1.3<br><sub>3,1,2,-,1</sub> |  | 0.3<br><sub>2,0,0,-,0</sub> |  | 0.6 | 0.6 | 0.7 | 8.0 |
| Braden Smith | 67% | 14.1<br><sub>42,24,12,10,-</sub> | 4.6<br><sub>19,10,0,0,-</sub> |  | 1.1<br><sub>4,1,0,0,-</sub> |  | 2.4<br><sub>10,5,2,0,-</sub> |  | 0.2<br><sub>2,0,0,0,-</sub> |  | 0.6 | 0.3 | 0.9 | 8.1 |
| Larry Nance Jr. | 96% | 13.3<br><sub>-,14,13,14,5</sub> | 4.2<br><sub>-,4,15,4,5</sub> |  | 2.4<br><sub>-,4,2,0,0</sub> |  | 0.8<br><sub>-,1,1,0,0</sub> |  | 0.5<br><sub>-,0,5,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.4 |

</details>

<details><summary>if Aaron Nesmith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard (IND) | 88% | 32.8<br><sub>-,38,31,34,34</sub> | 16.3<br><sub>-,22,9,12,17</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>-,2,1,3,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 8.1<br><sub>-,5,8,12,10</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>-,2,3,1,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.2 | 2.3 | 27.1 |
| Pascal Siakam (IND) | 88% | 32.6<br><sub>-,30,32,35,32</sub> | 21.5<br><sub>-,20,23,29,28</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>-,4,2,9,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 4.2<br><sub>-,2,5,8,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,2,2,5,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.4 | 2.0 | 32.0 |
| Aaron Nesmith (IND) | 100% | 26.3<br><sub>-,30,27,34,22</sub> | 12.2<br><sub>-,16,8,18,2</sub> | 11.5 · – | 3.0<br><sub>-,2,5,2,1</sub> | 3.5 | 1.6<br><sub>-,2,1,2,1</sub> | 1.5 | 1.8<br><sub>-,2,2,4,0</sub> | 2.5 | 0.6 | 0.4 | 1.3 | 16.9 |
| Kelly Oubre Jr. (IND) | 80% | 25.7<br><sub>-,-,16,23,34</sub> | 10.1<br><sub>-,-,2,14,14</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>-,-,1,2,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>-,-,0,2,1</sub> |  | 0.9<br><sub>-,-,0,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.8 | 0.5 | 1.0 | 15.1 |
| Ivica Zubac (IND) | 67% | 25.6<br><sub>-,19,19,28,31</sub> | 11.3<br><sub>-,1,10,16,20</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>-,4,12,3,12</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>-,2,5,0,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.8 | 1.5 | 21.2 |
| Quenton Jackson (IND) | 98% | 21.5<br><sub>35,22,17,25,21</sub> | 9.6<br><sub>20,13,6,10,4</sub> |  | 2.8<br><sub>7,7,4,5,2</sub> |  | 3.1<br><sub>3,2,1,4,2</sub> |  | 1.0<br><sub>1,3,0,2,1</sub> |  | 0.8 | 0.2 | 1.2 | 15.4 |
| Obi Toppin (IND) | 76% | 18.6<br><sub>-,19,22,19,16</sub> | 10.2<br><sub>-,11,10,10,8</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>-,5,7,2,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>-,1,2,4,1</sub> |  | 1.3<br><sub>-,1,2,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.4 | 0.2 | 1.0 | 15.9 |
| Jarace Walker (IND) | 98% | 14.6<br><sub>45,17,20,10,7</sub> | 6.0<br><sub>15,2,9,7,1</sub> |  | 3.0<br><sub>7,8,5,1,1</sub> |  | 1.3<br><sub>3,1,2,0,0</sub> |  | 0.7<br><sub>1,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.8 | 10.4 |
| T.J. McConnell (IND) | 91% | 14.2<br><sub>-,-,9,8,14</sub> | 7.3<br><sub>-,-,6,2,7</sub> |  | 1.9<br><sub>-,-,2,0,3</sub> |  | 4.2<br><sub>-,-,1,3,7</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.7 | 0.2 | 1.0 | 13.4 |
| Jay Huff (IND) | 80% | 13.6<br><sub>40,14,10,-,11</sub> | 5.6<br><sub>22,6,0,-,6</sub> |  | 2.4<br><sub>8,3,3,-,4</sub> |  | 1.0<br><sub>2,1,0,-,0</sub> |  | 0.7<br><sub>0,2,0,-,0</sub> |  | 0.3 | 0.8 | 0.6 | 9.0 |
| Kobe Brown (IND) | 72% | 13.1<br><sub>38,7,-,-,-</sub> | 4.7<br><sub>16,0,-,-,-</sub> |  | 2.3<br><sub>6,1,-,-,-</sub> |  | 1.1<br><sub>1,0,-,-,-</sub> |  | 0.5<br><sub>2,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.1 |
| Jalen Slawson (IND) | 80% | 11.9<br><sub>41,6,12,-,12</sub> | 3.5<br><sub>12,2,4,-,2</sub> |  | 2.1<br><sub>7,2,1,-,3</sub> |  | 1.1<br><sub>3,1,2,-,1</sub> |  | 0.2<br><sub>2,0,0,-,0</sub> |  | 0.6 | 0.5 | 0.6 | 6.7 |
| Larry Nance Jr. (IND) | 96% | 11.0<br><sub>-,14,13,14,5</sub> | 3.5<br><sub>-,4,15,4,5</sub> |  | 2.0<br><sub>-,4,2,0,0</sub> |  | 0.6<br><sub>-,1,1,0,0</sub> |  | 0.4<br><sub>-,0,5,0,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.1 |
| Braden Smith (IND) | 67% | 11.0<br><sub>42,24,12,10,-</sub> | 3.6<br><sub>19,10,0,0,-</sub> |  | 0.9<br><sub>4,1,0,0,-</sub> |  | 1.9<br><sub>10,5,2,0,-</sub> |  | 0.2<br><sub>2,0,0,0,-</sub> |  | 0.5 | 0.2 | 0.7 | 6.4 |
| Jalen Brunson (NYK) | 98% | 33.4<br><sub>34,28,34,28,35</sub> | 27.0<br><sub>19,33,31,23,27</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>2,2,6,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.9<br><sub>6,4,9,2,5</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>4,5,3,1,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.2 | 2.2 | 36.3 |
| OG Anunoby (NYK) | 98% | 32.4<br><sub>38,24,34,29,34</sub> | 17.2<br><sub>18,18,15,19,14</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>4,5,6,3,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>3,1,3,5,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.7 | 1.6 | 24.7 |
| Karl-Anthony Towns (NYK) | 98% | 31.3<br><sub>35,25,34,27,34</sub> | 19.1<br><sub>11,17,29,21,21</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 13.0<br><sub>16,12,13,16,11</sub> | 12.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>5,1,3,3,8</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>1,2,2,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.7 | 2.7 | 35.8 |
| Josh Hart (NYK) | 98% | 30.2<br><sub>27,-,-,-,26</sub> | 9.7<br><sub>8,-,-,-,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>6,-,-,-,4</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>7,-,-,-,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>2,-,-,-,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.2 | 1.5 | 21.2 |
| Landry Shamet (NYK) | 98% | 24.9<br><sub>30,25,29,28,29</sub> | 8.9<br><sub>22,7,9,10,12</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,2,1,3,2</sub> |  | 1.6<br><sub>1,2,1,2,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>4,1,3,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.6 | 0.2 | 0.7 | 12.3 |
| Mikal Bridges (NYK) | 98% | 24.4<br><sub>16,22,31,17,17</sub> | 8.6<br><sub>6,7,9,4,2</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,4,6,5,1</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>0,4,4,1,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0<br><sub>0,1,1,0,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9 | 0.4 | 0.8 | 13.7 |
| Miles McBride (NYK) | 98% | 19.8<br><sub>17,11,16,25,27</sub> | 7.8<br><sub>6,7,5,8,19</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>1,1,0,0,2</sub> |  | 1.6<br><sub>2,1,0,3,2</sub> |  | 1.4<br><sub>2,2,1,2,5</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.2 | 0.5 | 11.3 |
| Andre Drummond (NYK) | 98% | 13.9<br><sub>13,12,14,16,14</sub> | 4.5<br><sub>4,6,0,2,0</sub> | 3.5 · –<br><sub>o 54% · u 46%</sub> | 6.9<br><sub>9,9,8,14,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.1<br><sub>0,0,0,3,3</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.5 | 0.7 | 12.5 |
| Tyler Kolek (NYK) | 91% | 12.8<br><sub>5,11,14,15,13</sub> | 4.4<br><sub>2,0,0,12,4</sub> |  | 1.7<br><sub>1,0,4,3,1</sub> |  | 3.7<br><sub>1,5,5,4,4</sub> |  | 0.4<br><sub>0,0,0,2,0</sub> |  | 0.5 | 0.1 | 0.7 | 9.8 |
| Mohamed Diawara (NYK) | 72% | 12.2<br><sub>6,21,14,18,11</sub> | 4.3<br><sub>0,8,2,5,2</sub> |  | 2.1<br><sub>1,6,3,3,0</sub> |  | 1.4<br><sub>0,4,3,3,0</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.1 | 0.5 | 7.8 |
| Jordan Clarkson (NYK) | 71% | 9.5<br><sub>11,15,15,11,-</sub> | 4.9<br><sub>7,10,9,2,-</sub> |  | 1.4<br><sub>0,1,2,4,-</sub> |  | 0.7<br><sub>0,1,0,2,-</sub> |  | 0.3<br><sub>1,2,1,0,-</sub> |  | 0.3 | 0.1 | 0.6 | 7.0 |
| Jose Alvarado (NYK) | 63% | 8.6<br><sub>9,9,-,6,-</sub> | 3.3<br><sub>0,0,-,0,-</sub> |  | 1.1<br><sub>0,0,-,1,-</sub> |  | 1.4<br><sub>0,2,-,1,-</sub> |  | 0.3<br><sub>0,0,-,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 5.9 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Dalton Knecht (NYK) | 64% | 7.1<br><sub>-,16,5,8,-</sub> | 3.3<br><sub>-,10,0,3,-</sub> |  | 1.4<br><sub>-,7,0,0,-</sub> |  | 0.5<br><sub>-,1,0,0,-</sub> |  | 0.3<br><sub>-,2,0,1,-</sub> |  | 0.2 | 0.1 | 0.2 | 5.1 |
| Jaden Akins (NYK) | 38% | 6.8<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| James Wiseman (NYK) | 52% | 6.6<br><sub>-,10,-,5,-</sub> | 2.5<br><sub>-,8,-,0,-</sub> |  | 2.3<br><sub>-,8,-,1,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.3 |
| Pacome Dadiet (NYK) | 48% | 6.3<br><sub>-,9,-,6,-</sub> | 3.1<br><sub>-,4,-,8,-</sub> |  | 1.3<br><sub>-,0,-,2,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,0,-,1,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |

</details>


### MIL @ ORL
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.3–110.4 | MIL 38% | 2.60 / 1.62 | ORL -4.5 | 216.5 | ORL -9.5 covers 35%; o224.5 34% |
| Expected (weighted by chance each plays) | 105.0–111.9 | MIL 31% | 3.24 / 1.45 | ORL -7.5 | 216.5 | ORL -9.5 covers 43%; o224.5 34% |
| if Tristan da Silva plays | 105.2–110.9 | MIL 34% | 2.94 / 1.52 | ORL -5.5 | 215.5 | ORL -9.5 covers 40%; o224.5 33% |
| if Jamal Cain plays | 105.2–110.4 | MIL 36% | 2.80 / 1.56 | ORL -5.5 | 215.5 | ORL -9.5 covers 38%; o224.5 31% |
| if Jalen Suggs plays | 105.3–111.3 | MIL 33% | 2.99 / 1.50 | ORL -6.5 | 216.5 | ORL -9.5 covers 40%; o224.5 33% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tristan da Silva (ORL) | Day-To-Day | 70% | 29.8 | 13.9 | 4.3 | 2.2 | 2.3 | 0.9 | 0.3 | 1.3 | 20.4 | full tables below |
| Jamal Cain (ORL) | Questionable | 55% | 23.7 | 9.5 | 4.3 | 1.1 | 1.1 | 0.8 | 0.3 | 1.1 | 15.0 | full tables below |
| Jalen Suggs (ORL) | Questionable | 55% | 29.0 | 12.5 | 4.1 | 5.1 | 1.9 | 1.9 | 0.7 | 2.8 | 21.6 | full tables below |

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 32.2<br><sub>33,35,27,-,35</sub> | 20.4<br><sub>25,23,13,-,27</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>5,5,1,-,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>3,10,2,-,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,1,1,-,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.3 | 2.5 | 29.7 |
| Jaime Jaquez Jr. | 98% | 27.1<br><sub>31,28,23,25,30</sub> | 14.5<br><sub>18,14,4,16,25</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>2,3,2,5,5</sub> |  | 3.7<br><sub>2,3,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>4,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 2.0 | 22.9 |
| Kyle Kuzma | 98% | 25.7<br><sub>27,32,31,26,24</sub> | 11.2<br><sub>6,13,27,5,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>5,4,4,5,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,3,0,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,6,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.4 | 1.7 | 18.1 |
| Myles Turner | 98% | 25.6<br><sub>36,24,24,27,-</sub> | 8.9<br><sub>12,0,3,3,-</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>9,7,5,3,-</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>6,0,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>4,0,0,1,-</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 2.0 | 1.4 | 15.7 |
| Ryan Rollins | 98% | 23.5<br><sub>24,14,20,24,24</sub> | 11.6<br><sub>13,10,7,14,8</sub> |  | 3.7<br><sub>9,1,5,5,7</sub> |  | 4.1<br><sub>5,1,6,2,4</sub> |  | 1.5<br><sub>2,1,2,4,2</sub> |  | 1.0 | 0.3 | 2.3 | 19.4 |
| Brayden Burries | 98% | 21.9<br><sub>22,38,29,26,23</sub> | 8.9<br><sub>9,21,13,3,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,11,8,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,6,4,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.3 | 15.6 |
| Nate Ament | 91% | 16.1<br><sub>18,15,23,22,22</sub> | 6.2<br><sub>9,7,12,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,1,5,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.5 | 0.3 | 0.8 | 9.4 |
| Kel'el Ware | 96% | 15.6<br><sub>16,13,9,17,23</sub> | 6.7<br><sub>2,4,0,8,8</sub> |  | 4.9<br><sub>5,3,0,4,5</sub> |  | 0.8<br><sub>1,0,1,1,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 1.2 | 12.4 |
| Cormac Ryan | 8% | 15.0 | 7.5 |  | 1.7 |  | 1.2 |  | 0.9 |  | 0.5 | 0.2 | 1.1 | 10.3 |
| AJ Green | 98% | 14.0<br><sub>20,24,18,8,8</sub> | 4.7<br><sub>5,12,5,0,3</sub> |  | 1.4<br><sub>2,1,1,0,1</sub> |  | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.8<br><sub>1,4,1,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.0 |
| Ousmane Dieng | 76% | 13.7<br><sub>2,-,15,24,18</sub> | 5.1<br><sub>0,-,10,8,9</sub> |  | 2.1<br><sub>0,-,1,3,2</sub> |  | 1.6<br><sub>0,-,0,0,4</sub> |  | 0.5<br><sub>0,-,2,2,2</sub> |  | 0.4 | 0.2 | 0.9 | 8.8 |
| Jericho Sims | 86% | 12.5<br><sub>1,7,15,8,18</sub> | 2.6<br><sub>0,0,2,2,0</sub> |  | 3.2<br><sub>0,1,2,0,4</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.2 | 0.7 | 6.8 |
| Caris LeVert | 16% | 12.1<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.8 | 7.4 |
| Kasparas Jakucionis | 96% | 10.3<br><sub>12,10,7,23,4</sub> | 3.6<br><sub>3,3,1,11,4</sub> |  | 1.3<br><sub>1,0,2,0,2</sub> |  | 1.7<br><sub>1,2,0,4,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.3 | 0.1 | 0.8 | 6.5 |
| Kam Jones | 8% | 9.2 | 2.4 |  | 0.9 |  | 1.8 |  | 0.1 |  | 0.4 | 0.1 | 0.7 | 5.1 |
| Pete Nance | 93% | 8.3<br><sub>-,-,-,-,4</sub> | 2.8<br><sub>-,-,-,-,3</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Gary Trent Jr. | 58% | 7.6<br><sub>-,-,-,6,4</sub> | 3.4<br><sub>-,-,-,5,6</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,1,2</sub> |  | 0.3 | 0.0 | 0.3 | 4.3 |
| Bogoljub Markovic | 52% | 6.0<br><sub>-,-,-,4,4</sub> | 2.8<br><sub>-,-,-,0,0</sub> |  | 1.5<br><sub>-,-,-,2,0</sub> |  | 0.3<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |

</details>

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 98% | 36.9<br><sub>38,38,40,38,39</sub> | 26.6<br><sub>24,15,30,33,38</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>3,8,6,7,8</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>6,15,11,7,1</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,0,3,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.4 | 3.6 | 40.4 |
| Desmond Bane | 98% | 36.0<br><sub>36,32,-,36,34</sub> | 22.7<br><sub>20,15,-,15,25</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>3,6,-,6,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>3,0,-,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.6<br><sub>4,3,-,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.5 | 2.4 | 31.2 |
| Anthony Black | 98% | 35.8<br><sub>-,31,38,33,39</sub> | 18.6<br><sub>-,10,18,26,22</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.3<br><sub>-,7,8,7,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.8<br><sub>-,6,6,5,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>-,1,2,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.2 | 0.8 | 2.7 | 29.7 |
| Wendell Carter Jr. | 98% | 33.5<br><sub>34,34,40,33,28</sub> | 14.1<br><sub>6,27,19,8,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>9,13,11,11,7</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>0,2,0,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>0,2,3,0,0</sub> |  | 1.1 | 0.9 | 1.7 | 25.4 |
| Jase Richardson | 96% | 25.8<br><sub>29,26,30,15,20</sub> | 9.7<br><sub>9,10,2,6,6</sub> |  | 2.9<br><sub>1,2,4,1,1</sub> |  | 3.0<br><sub>5,3,4,1,2</sub> |  | 1.1<br><sub>0,2,0,0,1</sub> |  | 1.1 | 0.4 | 1.0 | 15.6 |
| Jevon Carter | 80% | 22.0<br><sub>18,3,15,4,28</sub> | 9.2<br><sub>5,0,9,0,11</sub> |  | 1.9<br><sub>1,0,1,0,3</sub> |  | 2.5<br><sub>4,0,0,0,4</sub> |  | 1.7<br><sub>1,0,3,0,3</sub> |  | 1.0 | 0.2 | 0.7 | 13.6 |
| Alex Morales | 86% | 19.3<br><sub>14,6,15,29,18</sub> | 4.4<br><sub>3,0,0,7,5</sub> |  | 3.3<br><sub>2,0,2,7,4</sub> |  | 1.3<br><sub>0,0,1,0,3</sub> |  | 0.5<br><sub>0,0,0,1,1</sub> |  | 0.8 | 0.2 | 0.8 | 9.0 |
| Goga Bitadze | 88% | 16.6<br><sub>-,8,7,15,20</sub> | 6.0<br><sub>-,4,4,2,4</sub> |  | 5.9<br><sub>-,5,5,2,7</sub> |  | 1.2<br><sub>-,0,2,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.7 | 1.1 | 0.7 | 13.1 |
| Nikola Vucevic | 98% | 14.6<br><sub>14,4,6,18,14</sub> | 5.8<br><sub>7,0,0,5,3</sub> |  | 4.3<br><sub>6,0,1,4,5</sub> |  | 1.6<br><sub>1,0,2,1,1</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 0.3 | 0.4 | 0.5 | 11.7 |
| Colin Castleton | 52% | 8.3<br><sub>-,2,-,-,1</sub> | 2.7<br><sub>-,0,-,-,0</sub> |  | 2.5<br><sub>-,0,-,-,0</sub> |  | 0.6<br><sub>-,1,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.8 |

</details>

<details><summary>if Jalen Suggs plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 32.1<br><sub>33,35,27,-,35</sub> | 20.3<br><sub>25,23,13,-,27</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>5,5,1,-,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>3,10,2,-,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,1,1,-,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.3 | 2.5 | 29.6 |
| Jaime Jaquez Jr. (MIL) | 98% | 27.1<br><sub>31,28,23,25,30</sub> | 14.4<br><sub>18,14,4,16,25</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>2,3,2,5,5</sub> |  | 3.7<br><sub>2,3,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>4,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 2.0 | 22.9 |
| Kyle Kuzma (MIL) | 98% | 25.7<br><sub>27,32,31,26,24</sub> | 11.1<br><sub>6,13,27,5,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>5,4,4,5,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,3,0,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,6,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.4 | 1.8 | 18.1 |
| Myles Turner (MIL) | 98% | 25.7<br><sub>36,24,24,27,-</sub> | 8.9<br><sub>12,0,3,3,-</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>9,7,5,3,-</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>6,0,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>4,0,0,1,-</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 2.0 | 1.4 | 15.7 |
| Ryan Rollins (MIL) | 98% | 23.4<br><sub>24,14,20,24,24</sub> | 11.5<br><sub>13,10,7,14,8</sub> |  | 3.6<br><sub>9,1,5,5,7</sub> |  | 4.1<br><sub>5,1,6,2,4</sub> |  | 1.5<br><sub>2,1,2,4,2</sub> |  | 1.0 | 0.3 | 2.3 | 19.2 |
| Brayden Burries (MIL) | 98% | 21.9<br><sub>22,38,29,26,23</sub> | 8.9<br><sub>9,21,13,3,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,11,8,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,6,4,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.4 | 15.6 |
| Nate Ament (MIL) | 91% | 16.1<br><sub>18,15,23,22,22</sub> | 6.2<br><sub>9,7,12,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,1,5,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.5 | 0.3 | 0.8 | 9.4 |
| Kel'el Ware (MIL) | 96% | 15.6<br><sub>16,13,9,17,23</sub> | 6.6<br><sub>2,4,0,8,8</sub> |  | 5.0<br><sub>5,3,0,4,5</sub> |  | 0.8<br><sub>1,0,1,1,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 1.2 | 12.4 |
| Cormac Ryan (MIL) | 8% | 14.9 | 7.3 |  | 1.7 |  | 1.1 |  | 0.8 |  | 0.6 | 0.2 | 1.0 | 10.1 |
| AJ Green (MIL) | 98% | 14.0<br><sub>20,24,18,8,8</sub> | 4.6<br><sub>5,12,5,0,3</sub> |  | 1.4<br><sub>2,1,1,0,1</sub> |  | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.8<br><sub>1,4,1,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.0 |
| Ousmane Dieng (MIL) | 76% | 13.7<br><sub>2,-,15,24,18</sub> | 5.1<br><sub>0,-,10,8,9</sub> |  | 2.1<br><sub>0,-,1,3,2</sub> |  | 1.6<br><sub>0,-,0,0,4</sub> |  | 0.5<br><sub>0,-,2,2,2</sub> |  | 0.4 | 0.2 | 0.9 | 8.8 |
| Jericho Sims (MIL) | 86% | 12.4<br><sub>1,7,15,8,18</sub> | 2.6<br><sub>0,0,2,2,0</sub> |  | 3.2<br><sub>0,1,2,0,4</sub> |  | 0.9<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.2 | 0.7 | 6.7 |
| Caris LeVert (MIL) | 16% | 12.0<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.8 | 7.2 |
| Kasparas Jakucionis (MIL) | 96% | 10.4<br><sub>12,10,7,23,4</sub> | 3.6<br><sub>3,3,1,11,4</sub> |  | 1.3<br><sub>1,0,2,0,2</sub> |  | 1.7<br><sub>1,2,0,4,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.3 | 0.1 | 0.9 | 6.6 |
| Kam Jones (MIL) | 8% | 9.1 | 2.4 |  | 0.9 |  | 1.8 |  | 0.1 |  | 0.3 | 0.1 | 0.7 | 5.1 |
| Pete Nance (MIL) | 93% | 8.3<br><sub>-,-,-,-,4</sub> | 2.8<br><sub>-,-,-,-,3</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.9 |
| Gary Trent Jr. (MIL) | 58% | 7.5<br><sub>-,-,-,6,4</sub> | 3.3<br><sub>-,-,-,5,6</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,1,2</sub> |  | 0.3 | 0.0 | 0.3 | 4.2 |
| Bogoljub Markovic (MIL) | 52% | 5.9<br><sub>-,-,-,4,4</sub> | 2.7<br><sub>-,-,-,0,0</sub> |  | 1.5<br><sub>-,-,-,2,0</sub> |  | 0.3<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.5 |
| Franz Wagner (ORL) | 98% | 35.1<br><sub>38,38,40,38,39</sub> | 24.5<br><sub>24,15,30,33,38</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>3,8,6,7,8</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>6,15,11,7,1</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>1,0,3,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 3.3 | 37.2 |
| Desmond Bane (ORL) | 98% | 33.5<br><sub>36,32,-,36,34</sub> | 20.8<br><sub>20,15,-,15,25</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>3,6,-,6,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>3,0,-,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.2<br><sub>4,3,-,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 2.1 | 28.6 |
| Anthony Black (ORL) | 98% | 33.1<br><sub>-,31,38,33,39</sub> | 17.1<br><sub>-,10,18,26,22</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>-,7,8,7,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>-,6,6,5,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>-,1,2,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.0 | 0.8 | 2.4 | 27.1 |
| Wendell Carter Jr. (ORL) | 98% | 31.4<br><sub>34,34,40,33,28</sub> | 13.4<br><sub>6,27,19,8,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>9,13,11,11,7</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,2,0,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>0,2,3,0,0</sub> |  | 1.0 | 0.9 | 1.5 | 24.1 |
| Jalen Suggs (ORL) | 100% | 29.0<br><sub>-,-,-,-,-</sub> | 12.5<br><sub>-,-,-,-,-</sub> | 10.5 · – | 4.1<br><sub>-,-,-,-,-</sub> | 3.5 | 5.1<br><sub>-,-,-,-,-</sub> | 3.5 | 1.9<br><sub>-,-,-,-,-</sub> | 1.5 | 1.9 | 0.7 | 2.8 | 21.6 |
| Jase Richardson (ORL) | 96% | 20.4<br><sub>29,26,30,15,20</sub> | 7.5<br><sub>9,10,2,6,6</sub> |  | 2.4<br><sub>1,2,4,1,1</sub> |  | 2.4<br><sub>5,3,4,1,2</sub> |  | 0.8<br><sub>0,2,0,0,1</sub> |  | 0.8 | 0.4 | 0.8 | 12.3 |
| Jevon Carter (ORL) | 80% | 16.0<br><sub>18,3,15,4,28</sub> | 6.9<br><sub>5,0,9,0,11</sub> |  | 1.4<br><sub>1,0,1,0,3</sub> |  | 1.8<br><sub>4,0,0,0,4</sub> |  | 1.1<br><sub>1,0,3,0,3</sub> |  | 0.7 | 0.2 | 0.5 | 10.1 |
| Alex Morales (ORL) | 86% | 15.6<br><sub>14,6,15,29,18</sub> | 3.5<br><sub>3,0,0,7,5</sub> |  | 2.7<br><sub>2,0,2,7,4</sub> |  | 1.0<br><sub>0,0,1,0,3</sub> |  | 0.3<br><sub>0,0,0,1,1</sub> |  | 0.6 | 0.1 | 0.7 | 7.2 |
| Goga Bitadze (ORL) | 88% | 14.3<br><sub>-,8,7,15,20</sub> | 5.4<br><sub>-,4,4,2,4</sub> |  | 5.0<br><sub>-,5,5,2,7</sub> |  | 1.1<br><sub>-,0,2,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.6 | 1.0 | 0.7 | 11.5 |
| Nikola Vucevic (ORL) | 98% | 12.8<br><sub>14,4,6,18,14</sub> | 5.3<br><sub>7,0,0,5,3</sub> |  | 3.8<br><sub>6,0,1,4,5</sub> |  | 1.4<br><sub>1,0,2,1,1</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.3 | 0.4 | 0.5 | 10.5 |
| Colin Castleton (ORL) | 52% | 6.5<br><sub>-,2,-,-,1</sub> | 2.3<br><sub>-,0,-,-,0</sub> |  | 1.9<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.1 | 0.2 | 0.4 | 4.7 |

</details>

<details><summary>if Jamal Cain plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 32.3<br><sub>33,35,27,-,35</sub> | 20.4<br><sub>25,23,13,-,27</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>5,5,1,-,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>3,10,2,-,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,1,1,-,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.3 | 2.4 | 29.7 |
| Jaime Jaquez Jr. (MIL) | 98% | 27.2<br><sub>31,28,23,25,30</sub> | 14.5<br><sub>18,14,4,16,25</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>2,3,2,5,5</sub> |  | 3.7<br><sub>2,3,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>4,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 2.0 | 23.0 |
| Myles Turner (MIL) | 98% | 25.7<br><sub>36,24,24,27,-</sub> | 8.8<br><sub>12,0,3,3,-</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.0<br><sub>9,7,5,3,-</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>6,0,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>4,0,0,1,-</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 2.0 | 1.4 | 15.7 |
| Kyle Kuzma (MIL) | 98% | 25.6<br><sub>27,32,31,26,24</sub> | 11.1<br><sub>6,13,27,5,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>5,4,4,5,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,3,0,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>1,1,6,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.4 | 1.7 | 18.0 |
| Ryan Rollins (MIL) | 98% | 23.5<br><sub>24,14,20,24,24</sub> | 11.5<br><sub>13,10,7,14,8</sub> |  | 3.6<br><sub>9,1,5,5,7</sub> |  | 4.1<br><sub>5,1,6,2,4</sub> |  | 1.5<br><sub>2,1,2,4,2</sub> |  | 1.0 | 0.3 | 2.3 | 19.3 |
| Brayden Burries (MIL) | 98% | 21.9<br><sub>22,38,29,26,23</sub> | 8.8<br><sub>9,21,13,3,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,11,8,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,6,4,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.4 | 15.6 |
| Nate Ament (MIL) | 91% | 16.1<br><sub>18,15,23,22,22</sub> | 6.2<br><sub>9,7,12,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,1,5,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.5 | 0.3 | 0.8 | 9.4 |
| Kel'el Ware (MIL) | 96% | 15.6<br><sub>16,13,9,17,23</sub> | 6.6<br><sub>2,4,0,8,8</sub> |  | 4.9<br><sub>5,3,0,4,5</sub> |  | 0.8<br><sub>1,0,1,1,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 1.2 | 12.4 |
| Cormac Ryan (MIL) | 8% | 15.3 | 7.6 |  | 1.7 |  | 1.2 |  | 0.9 |  | 0.6 | 0.2 | 1.1 | 10.5 |
| AJ Green (MIL) | 98% | 13.9<br><sub>20,24,18,8,8</sub> | 4.6<br><sub>5,12,5,0,3</sub> |  | 1.4<br><sub>2,1,1,0,1</sub> |  | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.8<br><sub>1,4,1,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 6.9 |
| Ousmane Dieng (MIL) | 76% | 13.7<br><sub>2,-,15,24,18</sub> | 5.1<br><sub>0,-,10,8,9</sub> |  | 2.1<br><sub>0,-,1,3,2</sub> |  | 1.6<br><sub>0,-,0,0,4</sub> |  | 0.5<br><sub>0,-,2,2,2</sub> |  | 0.4 | 0.2 | 0.9 | 8.8 |
| Jericho Sims (MIL) | 86% | 12.5<br><sub>1,7,15,8,18</sub> | 2.6<br><sub>0,0,2,2,0</sub> |  | 3.2<br><sub>0,1,2,0,4</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.2 | 0.7 | 6.8 |
| Caris LeVert (MIL) | 16% | 12.0<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.8 | 7.4 |
| Kasparas Jakucionis (MIL) | 96% | 10.2<br><sub>12,10,7,23,4</sub> | 3.5<br><sub>3,3,1,11,4</sub> |  | 1.3<br><sub>1,0,2,0,2</sub> |  | 1.7<br><sub>1,2,0,4,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.3 | 0.1 | 0.8 | 6.5 |
| Kam Jones (MIL) | 8% | 9.1 | 2.3 |  | 0.9 |  | 1.8 |  | 0.1 |  | 0.4 | 0.1 | 0.7 | 5.0 |
| Pete Nance (MIL) | 93% | 8.2<br><sub>-,-,-,-,4</sub> | 2.8<br><sub>-,-,-,-,3</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Gary Trent Jr. (MIL) | 58% | 7.5<br><sub>-,-,-,6,4</sub> | 3.3<br><sub>-,-,-,5,6</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,1,2</sub> |  | 0.3 | 0.0 | 0.3 | 4.3 |
| Bogoljub Markovic (MIL) | 52% | 6.0<br><sub>-,-,-,4,4</sub> | 2.8<br><sub>-,-,-,0,0</sub> |  | 1.5<br><sub>-,-,-,2,0</sub> |  | 0.3<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.5 |
| Franz Wagner (ORL) | 98% | 35.6<br><sub>38,38,40,38,39</sub> | 25.3<br><sub>24,15,30,33,38</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>3,8,6,7,8</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>6,15,11,7,1</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>1,0,3,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.3 | 3.3 | 38.6 |
| Desmond Bane (ORL) | 98% | 34.5<br><sub>36,32,-,36,34</sub> | 21.4<br><sub>20,15,-,15,25</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>3,6,-,6,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>3,0,-,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.3<br><sub>4,3,-,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.4 | 2.2 | 29.8 |
| Anthony Black (ORL) | 98% | 34.2<br><sub>-,31,38,33,39</sub> | 17.6<br><sub>-,10,18,26,22</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>-,7,8,7,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.5<br><sub>-,6,6,5,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>-,1,2,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.1 | 0.8 | 2.6 | 28.2 |
| Wendell Carter Jr. (ORL) | 98% | 32.1<br><sub>34,34,40,33,28</sub> | 13.2<br><sub>6,27,19,8,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.9<br><sub>9,13,11,11,7</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,2,0,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>0,2,3,0,0</sub> |  | 1.0 | 0.8 | 1.5 | 24.1 |
| Jamal Cain (ORL) | 100% | 23.7<br><sub>25,25,36,20,-</sub> | 9.5<br><sub>10,5,18,5,-</sub> |  | 4.3<br><sub>3,5,12,3,-</sub> |  | 1.1<br><sub>1,0,1,1,-</sub> |  | 1.1<br><sub>2,1,2,1,-</sub> |  | 0.8 | 0.3 | 1.1 | 15.0 |
| Jase Richardson (ORL) | 96% | 23.0<br><sub>29,26,30,15,20</sub> | 8.3<br><sub>9,10,2,6,6</sub> |  | 2.7<br><sub>1,2,4,1,1</sub> |  | 2.8<br><sub>5,3,4,1,2</sub> |  | 0.9<br><sub>0,2,0,0,1</sub> |  | 0.9 | 0.4 | 1.0 | 13.8 |
| Jevon Carter (ORL) | 80% | 19.0<br><sub>18,3,15,4,28</sub> | 7.7<br><sub>5,0,9,0,11</sub> |  | 1.7<br><sub>1,0,1,0,3</sub> |  | 2.3<br><sub>4,0,0,0,4</sub> |  | 1.4<br><sub>1,0,3,0,3</sub> |  | 0.8 | 0.2 | 0.6 | 11.7 |
| Alex Morales (ORL) | 86% | 17.7<br><sub>14,6,15,29,18</sub> | 4.0<br><sub>3,0,0,7,5</sub> |  | 3.0<br><sub>2,0,2,7,4</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 0.4<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 0.8 | 8.2 |
| Goga Bitadze (ORL) | 88% | 15.2<br><sub>-,8,7,15,20</sub> | 5.6<br><sub>-,4,4,2,4</sub> |  | 5.4<br><sub>-,5,5,2,7</sub> |  | 1.2<br><sub>-,0,2,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 12.2 |
| Nikola Vucevic (ORL) | 98% | 13.4<br><sub>14,4,6,18,14</sub> | 5.5<br><sub>7,0,0,5,3</sub> |  | 3.9<br><sub>6,0,1,4,5</sub> |  | 1.5<br><sub>1,0,2,1,1</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 0.3 | 0.4 | 0.5 | 10.9 |
| Colin Castleton (ORL) | 52% | 6.8<br><sub>-,2,-,-,1</sub> | 2.3<br><sub>-,0,-,-,0</sub> |  | 2.0<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |

</details>

<details><summary>if Tristan da Silva plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro (MIL) | 98% | 32.3<br><sub>33,35,27,-,35</sub> | 20.4<br><sub>25,23,13,-,27</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>5,5,1,-,2</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>3,10,2,-,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>4,1,1,-,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.3 | 2.5 | 29.7 |
| Jaime Jaquez Jr. (MIL) | 98% | 27.1<br><sub>31,28,23,25,30</sub> | 14.3<br><sub>18,14,4,16,25</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>2,3,2,5,5</sub> |  | 3.7<br><sub>2,3,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>4,2,0,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.3 | 2.0 | 22.8 |
| Kyle Kuzma (MIL) | 98% | 25.7<br><sub>27,32,31,26,24</sub> | 11.2<br><sub>6,13,27,5,9</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>5,4,4,5,1</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>4,3,0,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,6,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.4 | 1.8 | 18.1 |
| Myles Turner (MIL) | 98% | 25.6<br><sub>36,24,24,27,-</sub> | 8.8<br><sub>12,0,3,3,-</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>9,7,5,3,-</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>6,0,7,2,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>4,0,0,1,-</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 2.0 | 1.4 | 15.6 |
| Ryan Rollins (MIL) | 98% | 23.5<br><sub>24,14,20,24,24</sub> | 11.5<br><sub>13,10,7,14,8</sub> |  | 3.7<br><sub>9,1,5,5,7</sub> |  | 4.2<br><sub>5,1,6,2,4</sub> |  | 1.5<br><sub>2,1,2,4,2</sub> |  | 1.0 | 0.4 | 2.3 | 19.4 |
| Brayden Burries (MIL) | 98% | 21.9<br><sub>22,38,29,26,23</sub> | 8.8<br><sub>9,21,13,3,8</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>5,11,8,3,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>3,6,4,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.4 | 15.6 |
| Nate Ament (MIL) | 91% | 16.1<br><sub>18,15,23,22,22</sub> | 6.2<br><sub>9,7,12,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,1,5,2,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.7<br><sub>0,0,1,1,1</sub> |  | 0.6<br><sub>2,0,2,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.5 | 0.3 | 0.9 | 9.4 |
| Kel'el Ware (MIL) | 96% | 15.5<br><sub>16,13,9,17,23</sub> | 6.6<br><sub>2,4,0,8,8</sub> |  | 5.0<br><sub>5,3,0,4,5</sub> |  | 0.8<br><sub>1,0,1,1,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 1.2 | 12.3 |
| Cormac Ryan (MIL) | 8% | 15.1 | 7.3 |  | 1.7 |  | 1.1 |  | 0.9 |  | 0.6 | 0.2 | 1.1 | 10.1 |
| AJ Green (MIL) | 98% | 14.0<br><sub>20,24,18,8,8</sub> | 4.7<br><sub>5,12,5,0,3</sub> |  | 1.4<br><sub>2,1,1,0,1</sub> |  | 0.9<br><sub>3,0,1,0,1</sub> |  | 0.8<br><sub>1,4,1,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.0 |
| Ousmane Dieng (MIL) | 76% | 13.7<br><sub>2,-,15,24,18</sub> | 5.1<br><sub>0,-,10,8,9</sub> |  | 2.1<br><sub>0,-,1,3,2</sub> |  | 1.6<br><sub>0,-,0,0,4</sub> |  | 0.5<br><sub>0,-,2,2,2</sub> |  | 0.4 | 0.2 | 0.9 | 8.8 |
| Jericho Sims (MIL) | 86% | 12.5<br><sub>1,7,15,8,18</sub> | 2.6<br><sub>0,0,2,2,0</sub> |  | 3.2<br><sub>0,1,2,0,4</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.2 | 0.7 | 6.8 |
| Caris LeVert (MIL) | 16% | 11.9<br><sub>-,-,-,-,-</sub> | 4.3<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.8 | 7.2 |
| Kasparas Jakucionis (MIL) | 96% | 10.3<br><sub>12,10,7,23,4</sub> | 3.5<br><sub>3,3,1,11,4</sub> |  | 1.3<br><sub>1,0,2,0,2</sub> |  | 1.7<br><sub>1,2,0,4,0</sub> |  | 0.3<br><sub>1,0,0,2,0</sub> |  | 0.4 | 0.1 | 0.9 | 6.5 |
| Kam Jones (MIL) | 8% | 9.2 | 2.3 |  | 0.9 |  | 1.9 |  | 0.1 |  | 0.4 | 0.1 | 0.7 | 5.1 |
| Pete Nance (MIL) | 93% | 8.3<br><sub>-,-,-,-,4</sub> | 2.8<br><sub>-,-,-,-,3</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.8 |
| Gary Trent Jr. (MIL) | 58% | 7.5<br><sub>-,-,-,6,4</sub> | 3.3<br><sub>-,-,-,5,6</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.4<br><sub>-,-,-,1,2</sub> |  | 0.3 | 0.0 | 0.3 | 4.2 |
| Bogoljub Markovic (MIL) | 52% | 6.1<br><sub>-,-,-,4,4</sub> | 2.7<br><sub>-,-,-,0,0</sub> |  | 1.5<br><sub>-,-,-,2,0</sub> |  | 0.3<br><sub>-,-,-,1,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.5 |
| Franz Wagner (ORL) | 98% | 35.1<br><sub>38,38,40,38,39</sub> | 24.3<br><sub>24,15,30,33,38</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>3,8,6,7,8</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>6,15,11,7,1</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>1,0,3,1,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3 | 0.3 | 3.3 | 37.6 |
| Desmond Bane (ORL) | 98% | 33.7<br><sub>36,32,-,36,34</sub> | 20.7<br><sub>20,15,-,15,25</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>3,6,-,6,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>3,0,-,4,2</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 3.2<br><sub>4,3,-,4,7</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 2.2 | 28.9 |
| Anthony Black (ORL) | 98% | 33.6<br><sub>-,31,38,33,39</sub> | 16.8<br><sub>-,10,18,26,22</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>-,7,8,7,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 5.5<br><sub>-,6,6,5,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>-,1,2,2,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 2.0 | 0.8 | 2.5 | 27.4 |
| Wendell Carter Jr. (ORL) | 98% | 31.5<br><sub>34,34,40,33,28</sub> | 13.1<br><sub>6,27,19,8,9</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.7<br><sub>9,13,11,11,7</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 2.1<br><sub>0,2,0,1,3</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>0,2,3,0,0</sub> |  | 1.0 | 0.8 | 1.6 | 23.9 |
| Tristan da Silva (ORL) | 100% | 29.8<br><sub>32,30,39,-,-</sub> | 13.9<br><sub>10,18,19,-,-</sub> | 12.5 · – | 4.3<br><sub>4,2,7,-,-</sub> | 3.5 | 2.2<br><sub>3,1,2,-,-</sub> |  | 2.3<br><sub>2,4,5,-,-</sub> | 2.5 | 0.9 | 0.3 | 1.3 | 20.4 |
| Jase Richardson (ORL) | 96% | 22.0<br><sub>29,26,30,15,20</sub> | 7.9<br><sub>9,10,2,6,6</sub> |  | 2.6<br><sub>1,2,4,1,1</sub> |  | 2.7<br><sub>5,3,4,1,2</sub> |  | 0.9<br><sub>0,2,0,0,1</sub> |  | 0.9 | 0.4 | 0.9 | 13.1 |
| Jevon Carter (ORL) | 80% | 17.6<br><sub>18,3,15,4,28</sub> | 7.3<br><sub>5,0,9,0,11</sub> |  | 1.6<br><sub>1,0,1,0,3</sub> |  | 2.1<br><sub>4,0,0,0,4</sub> |  | 1.2<br><sub>1,0,3,0,3</sub> |  | 0.8 | 0.2 | 0.6 | 11.0 |
| Alex Morales (ORL) | 86% | 16.6<br><sub>14,6,15,29,18</sub> | 3.8<br><sub>3,0,0,7,5</sub> |  | 2.8<br><sub>2,0,2,7,4</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 0.3<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 0.7 | 7.7 |
| Goga Bitadze (ORL) | 88% | 14.4<br><sub>-,8,7,15,20</sub> | 5.4<br><sub>-,4,4,2,4</sub> |  | 5.1<br><sub>-,5,5,2,7</sub> |  | 1.1<br><sub>-,0,2,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.6 | 1.0 | 0.7 | 11.6 |
| Nikola Vucevic (ORL) | 98% | 12.8<br><sub>14,4,6,18,14</sub> | 5.3<br><sub>7,0,0,5,3</sub> |  | 3.8<br><sub>6,0,1,4,5</sub> |  | 1.5<br><sub>1,0,2,1,1</sub> |  | 0.5<br><sub>1,0,0,1,0</sub> |  | 0.3 | 0.4 | 0.5 | 10.5 |
| Colin Castleton (ORL) | 52% | 6.4<br><sub>-,2,-,-,1</sub> | 2.2<br><sub>-,0,-,-,0</sub> |  | 1.9<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.0<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.6 |

</details>


### CLE @ MIA
Out: Sam Merrill (CLE), Evan Mobley (CLE)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.2–118.9 | CLE 51% | 1.98 / 2.02 | MIA +0.5 | 238.5 | MIA -2.5 covers 44%; o236.5 53% |
| Expected (weighted by chance each plays) | 119.0–119.2 | CLE 49% | 2.03 / 1.97 | MIA +0.5 | 238.5 | MIA -2.5 covers 45%; o236.5 53% |
| if Pelle Larsson plays | 118.4–120.5 | CLE 44% | 2.28 / 1.78 | MIA -2.5 | 238.5 | MIA -2.5 covers 50%; o236.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pelle Larsson (MIA) | Doubtful | 20% | 28.4 | 11.3 | 3.5 | 3.2 | 1.1 | 0.9 | 0.2 | 1.6 | 18.0 | full tables below |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.4<br><sub>35,30,34,25,33</sub> | 20.2<br><sub>19,17,7,11,32</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>9,6,2,3,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>6,3,5,5,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,3,1,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.5 | 3.2 | 31.9 |
| Donovan Mitchell | 98% | 35.4<br><sub>33,33,37,23,36</sub> | 27.6<br><sub>27,23,37,11,23</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>3,7,4,2,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>6,8,4,4,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>5,1,5,1,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.4 | 2.9 | 38.5 |
| Peyton Watson | 98% | 29.8<br><sub>-,28,29,21,30</sub> | 13.4<br><sub>-,13,12,13,7</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>-,9,6,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>-,2,3,1,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4<br><sub>-,1,1,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 1.3 | 1.6 | 21.1 |
| Jarrett Allen | 98% | 28.2<br><sub>7,-,-,19,32</sub> | 13.8<br><sub>0,-,-,12,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 9.3<br><sub>1,-,-,7,14</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,-,-,1,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.1<br><sub>0,-,-,1,0</sub> |  | 0.8 | 1.2 | 1.2 | 24.8 |
| Meleek Thomas | 91% | 25.7<br><sub>18,27,24,27,22</sub> | 11.5<br><sub>9,12,9,18,14</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,1,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,3,0,3,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>3,2,3,4,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.4 | 1.2 | 16.0 |
| Jaylon Tyson | 97% | 22.3<br><sub>-,-,-,-,23</sub> | 9.3<br><sub>-,-,-,-,3</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>-,-,-,-,0</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>-,-,-,-,1</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.3 | 1.1 | 15.6 |
| Tyrese Proctor | 91% | 22.3<br><sub>22,19,23,23,23</sub> | 9.2<br><sub>11,3,7,6,15</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>1,6,3,1,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>0,3,3,4,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>2,0,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.1 | 1.1 | 15.2 |
| Mario Hezonja | 98% | 18.2<br><sub>23,27,19,17,7</sub> | 7.3<br><sub>12,15,0,10,0</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>8,10,5,3,0</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,1,0,0</sub> |  | 0.9<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.6 | 0.3 | 0.8 | 13.4 |
| Thomas Bryant | 63% | 14.5<br><sub>13,16,15,15,-</sub> | 7.4<br><sub>8,13,5,11,-</sub> |  | 3.8<br><sub>0,6,3,2,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.9<br><sub>1,1,1,2,-</sub> |  | 0.4 | 0.4 | 0.6 | 11.8 |
| Craig Porter Jr. | 67% | 13.7<br><sub>14,3,15,17,-</sub> | 3.2<br><sub>0,0,0,9,-</sub> |  | 2.5<br><sub>1,0,1,2,-</sub> |  | 2.3<br><sub>1,0,1,4,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.6 | 0.3 | 0.7 | 8.0 |
| Riley Minix | 52% | 12.3<br><sub>-,-,10,17,-</sub> | 4.6<br><sub>-,-,8,2,-</sub> |  | 2.2<br><sub>-,-,3,2,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,2,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.4 |
| Norchad Omier | 52% | 8.7<br><sub>-,3,-,12,-</sub> | 2.7<br><sub>-,0,-,0,-</sub> |  | 2.1<br><sub>-,2,-,3,-</sub> |  | 0.9<br><sub>-,1,-,2,-</sub> |  | 0.1<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.7 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 38.0<br><sub>29,43,38,40,38</sub> | 15.4<br><sub>15,11,22,17,19</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>0,2,2,3,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 8.3<br><sub>7,10,8,11,8</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>4,0,4,2,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.3 | 2.2 | 26.9 |
| Bam Adebayo | 98% | 36.4<br><sub>31,41,33,34,37</sub> | 19.4<br><sub>16,35,18,18,11</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 10.6<br><sub>9,10,10,8,8</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 3.8<br><sub>4,4,0,4,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>1,1,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.6 | 0.7 | 1.7 | 33.8 |
| Giannis Antetokounmpo | 98% | 35.4<br><sub>34,41,31,34,31</sub> | 28.7<br><sub>30,27,20,29,30</sub> | 29.5 · –<br><sub>o 49% · u 51%</sub> | 12.9<br><sub>12,14,14,14,11</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 6.4<br><sub>7,6,4,3,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.6<br><sub>0,0,1,0,1</sub> |  | 1.1 | 0.9 | 3.4 | 48.0 |
| Klay Thompson | 92% | 30.2<br><sub>27,35,23,32,30</sub> | 15.7<br><sub>19,30,11,23,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,5,0,2,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.0<br><sub>1,3,3,4,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 3.1<br><sub>4,8,2,7,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.6 | 1.1 | 19.9 |
| Andrew Wiggins | 98% | 27.0<br><sub>24,23,21,32,19</sub> | 11.0<br><sub>7,3,2,6,13</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>0,4,6,3,0</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>2,1,4,1,0</sub> |  | 1.6<br><sub>2,1,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.8 | 1.1 | 16.5 |
| Bobby Portis | 98% | 21.1<br><sub>18,18,14,20,17</sub> | 8.9<br><sub>2,4,0,4,5</sub> |  | 5.5<br><sub>3,10,5,1,1</sub> |  | 1.4<br><sub>2,5,0,1,1</sub> |  | 1.2<br><sub>0,0,0,1,1</sub> |  | 0.6 | 0.3 | 0.7 | 15.8 |
| Ryan Conwell | 88% | 20.0<br><sub>8,17,30,19,21</sub> | 6.9<br><sub>5,0,13,6,5</sub> |  | 2.2<br><sub>1,2,1,2,4</sub> |  | 1.6<br><sub>1,2,2,2,2</sub> |  | 1.0<br><sub>1,0,3,2,1</sub> |  | 0.7 | 0.1 | 0.7 | 10.8 |
| Tim Hardaway Jr. | 76% | 14.2<br><sub>19,7,4,7,-</sub> | 5.7<br><sub>9,0,0,0,-</sub> |  | 1.5<br><sub>0,0,0,0,-</sub> |  | 0.6<br><sub>0,0,1,0,-</sub> |  | 0.8<br><sub>3,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 7.9 |
| Nikola Jovic | 52% | 12.6<br><sub>7,-,12,-,-</sub> | 4.5<br><sub>2,-,1,-,-</sub> |  | 2.3<br><sub>1,-,0,-,-</sub> |  | 1.1<br><sub>0,-,1,-,-</sub> |  | 0.5<br><sub>0,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.8 |
| Keshad Johnson | 52% | 11.8<br><sub>-,-,-,-,-</sub> | 5.2<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.5 | 8.0 |
| Dru Smith | 52% | 11.6<br><sub>11,-,1,-,-</sub> | 3.5<br><sub>3,-,0,-,-</sub> |  | 1.6<br><sub>3,-,0,-,-</sub> |  | 1.6<br><sub>2,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.9 | 0.2 | 0.6 | 6.7 |
| Simone Fontecchio | 52% | 9.2<br><sub>-,5,-,-,7</sub> | 4.5<br><sub>-,0,-,-,3</sub> |  | 1.6<br><sub>-,0,-,-,0</sub> |  | 0.7<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 6.7 |
| Tre Donaldson | 5% | 8.8 | 3.7 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Myron Gardner | 58% | 8.3<br><sub>1,-,1,-,10</sub> | 3.1<br><sub>0,-,0,-,4</sub> |  | 2.3<br><sub>0,-,0,-,3</sub> |  | 0.8<br><sub>0,-,0,-,1</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 6.2 |
| Nick Richards | 52% | 7.6<br><sub>1,-,1,-,-</sub> | 2.7<br><sub>0,-,0,-,-</sub> |  | 2.6<br><sub>1,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.4 | 0.5 | 5.6 |

</details>

<details><summary>if Pelle Larsson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Donovan Mitchell (CLE) | 98% | 35.5<br><sub>33,33,37,23,36</sub> | 27.7<br><sub>27,23,37,11,23</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>3,7,4,2,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>6,8,4,4,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>5,1,5,1,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.4 | 2.9 | 38.5 |
| James Harden (CLE) | 98% | 35.3<br><sub>35,30,34,25,33</sub> | 20.1<br><sub>19,17,7,11,32</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>9,6,2,3,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>6,3,5,5,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,3,1,2,5</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.5 | 3.2 | 31.7 |
| Peyton Watson (CLE) | 98% | 29.9<br><sub>-,28,29,21,30</sub> | 13.4<br><sub>-,13,12,13,7</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>-,9,6,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>-,2,3,1,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>-,1,1,2,2</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.9 | 1.3 | 1.6 | 21.0 |
| Jarrett Allen (CLE) | 98% | 28.2<br><sub>7,-,-,19,32</sub> | 13.8<br><sub>0,-,-,12,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 9.3<br><sub>1,-,-,7,14</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,-,-,1,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.1<br><sub>0,-,-,1,0</sub> |  | 0.8 | 1.2 | 1.2 | 24.6 |
| Meleek Thomas (CLE) | 91% | 25.7<br><sub>18,27,24,27,22</sub> | 11.5<br><sub>9,12,9,18,14</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>1,1,4,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,3,0,3,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>3,2,3,4,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0 | 0.4 | 1.2 | 16.0 |
| Tyrese Proctor (CLE) | 91% | 22.4<br><sub>22,19,23,23,23</sub> | 9.2<br><sub>11,3,7,6,15</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>1,6,3,1,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>0,3,3,4,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>2,0,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.1 | 1.1 | 15.3 |
| Jaylon Tyson (CLE) | 97% | 22.3<br><sub>-,-,-,-,23</sub> | 9.2<br><sub>-,-,-,-,3</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>-,-,-,-,0</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>-,-,-,-,1</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.3 | 1.1 | 15.5 |
| Mario Hezonja (CLE) | 98% | 18.1<br><sub>23,27,19,17,7</sub> | 7.3<br><sub>12,15,0,10,0</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>8,10,5,3,0</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,1,0,0</sub> |  | 0.9<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.6 | 0.3 | 0.8 | 13.3 |
| Thomas Bryant (CLE) | 63% | 14.4<br><sub>13,16,15,15,-</sub> | 7.3<br><sub>8,13,5,11,-</sub> |  | 3.8<br><sub>0,6,3,2,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.8<br><sub>1,1,1,2,-</sub> |  | 0.4 | 0.4 | 0.6 | 11.6 |
| Craig Porter Jr. (CLE) | 67% | 13.7<br><sub>14,3,15,17,-</sub> | 3.1<br><sub>0,0,0,9,-</sub> |  | 2.5<br><sub>1,0,1,2,-</sub> |  | 2.2<br><sub>1,0,1,4,-</sub> |  | 0.2<br><sub>0,0,0,0,-</sub> |  | 0.7 | 0.3 | 0.7 | 7.9 |
| Riley Minix (CLE) | 52% | 12.3<br><sub>-,-,10,17,-</sub> | 4.5<br><sub>-,-,8,2,-</sub> |  | 2.2<br><sub>-,-,3,2,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.6<br><sub>-,-,2,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 7.3 |
| Norchad Omier (CLE) | 52% | 8.7<br><sub>-,3,-,12,-</sub> | 2.7<br><sub>-,0,-,0,-</sub> |  | 2.1<br><sub>-,2,-,3,-</sub> |  | 0.9<br><sub>-,1,-,2,-</sub> |  | 0.1<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 5.7 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Davion Mitchell (MIA) | 98% | 35.9<br><sub>29,43,38,40,38</sub> | 14.3<br><sub>15,11,22,17,19</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>0,2,2,3,5</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 8.1<br><sub>7,10,8,11,8</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>4,0,4,2,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 2.1 | 25.2 |
| Bam Adebayo (MIA) | 98% | 35.3<br><sub>31,41,33,34,37</sub> | 19.4<br><sub>16,35,18,18,11</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 10.2<br><sub>9,10,10,8,8</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 3.7<br><sub>4,4,0,4,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>1,1,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.6 | 1.6 | 33.3 |
| Giannis Antetokounmpo (MIA) | 98% | 34.5<br><sub>34,41,31,34,31</sub> | 28.8<br><sub>30,27,20,29,30</sub> | 29.5 · –<br><sub>o 49% · u 51%</sub> | 12.5<br><sub>12,14,14,14,11</sub> | 11.5<br><sub>o 54% · u 46%</sub> | 5.9<br><sub>7,6,4,3,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.6<br><sub>0,0,1,0,1</sub> |  | 1.0 | 0.9 | 3.4 | 47.2 |
| Pelle Larsson (MIA) | 100% | 28.4<br><sub>30,35,29,22,31</sub> | 11.3<br><sub>9,7,13,11,14</sub> |  | 3.5<br><sub>3,3,1,3,7</sub> |  | 3.2<br><sub>2,4,4,3,2</sub> |  | 1.1<br><sub>1,0,3,3,2</sub> |  | 0.9 | 0.2 | 1.6 | 18.0 |
| Klay Thompson (MIA) | 92% | 26.6<br><sub>27,35,23,32,30</sub> | 13.6<br><sub>19,30,11,23,11</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>1,5,0,2,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.8<br><sub>1,3,3,4,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.8<br><sub>4,8,2,7,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.5 | 1.0 | 17.4 |
| Andrew Wiggins (MIA) | 98% | 24.0<br><sub>24,23,21,32,19</sub> | 9.8<br><sub>7,3,2,6,13</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>0,4,6,3,0</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>2,1,4,1,0</sub> |  | 1.3<br><sub>2,1,0,2,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.7 | 1.0 | 14.7 |
| Bobby Portis (MIA) | 98% | 18.1<br><sub>18,18,14,20,17</sub> | 7.8<br><sub>2,4,0,4,5</sub> |  | 4.7<br><sub>3,10,5,1,1</sub> |  | 1.2<br><sub>2,5,0,1,1</sub> |  | 1.0<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.2 | 0.6 | 13.7 |
| Ryan Conwell (MIA) | 88% | 15.3<br><sub>8,17,30,19,21</sub> | 5.6<br><sub>5,0,13,6,5</sub> |  | 1.7<br><sub>1,2,1,2,4</sub> |  | 1.3<br><sub>1,2,2,2,2</sub> |  | 0.8<br><sub>1,0,3,2,1</sub> |  | 0.6 | 0.1 | 0.5 | 8.6 |
| Tim Hardaway Jr. (MIA) | 76% | 9.6<br><sub>19,7,4,7,-</sub> | 4.0<br><sub>9,0,0,0,-</sub> |  | 1.0<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.5<br><sub>3,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| Nikola Jovic (MIA) | 52% | 8.8<br><sub>7,-,12,-,-</sub> | 3.1<br><sub>2,-,1,-,-</sub> |  | 1.6<br><sub>1,-,0,-,-</sub> |  | 0.8<br><sub>0,-,1,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.5 |
| Tre Donaldson (MIA) | 5% | 8.7 | 3.8 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Dru Smith (MIA) | 52% | 7.3<br><sub>11,-,1,-,-</sub> | 2.3<br><sub>3,-,0,-,-</sub> |  | 1.1<br><sub>3,-,0,-,-</sub> |  | 1.1<br><sub>2,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.6 | 0.1 | 0.4 | 4.4 |
| Simone Fontecchio (MIA) | 52% | 7.1<br><sub>-,5,-,-,7</sub> | 3.5<br><sub>-,0,-,-,3</sub> |  | 1.2<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.4<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.2 |
| Keshad Johnson (MIA) | 52% | 6.7<br><sub>-,-,-,-,-</sub> | 3.1<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 4.8 |
| Myron Gardner (MIA) | 58% | 6.3<br><sub>1,-,1,-,10</sub> | 2.5<br><sub>0,-,0,-,4</sub> |  | 1.8<br><sub>0,-,0,-,3</sub> |  | 0.6<br><sub>0,-,0,-,1</sub> |  | 0.2<br><sub>0,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 5.0 |
| Nick Richards (MIA) | 52% | 6.1<br><sub>1,-,1,-,-</sub> | 2.5<br><sub>0,-,0,-,-</sub> |  | 2.2<br><sub>1,-,0,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.1<br><sub>0,-,0,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 5.0 |

</details>


### ATL @ CHI
Out: Tobe Awaka (CHI), Caleb Wilson (CHI), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Asa Newell (ATL), Jalen Wilson (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 124.4–116.4 | ATL 72% | 1.40 / 3.51 | CHI +8.5 | 240.5 | CHI +7.5 covers 48%; o245.5 40% |
| Expected (weighted by chance each plays) | 125.8–117.6 | ATL 72% | 1.40 / 3.53 | CHI +8.5 | 243.5 | CHI +7.5 covers 47%; o245.5 46% |
| if Kingston Flemings plays | 125.2–115.9 | ATL 74% | 1.34 / 3.91 | CHI +9.5 | 241.5 | CHI +7.5 covers 45%; o245.5 40% |
| if Norman Powell plays | 124.6–118.3 | ATL 68% | 1.48 / 3.09 | CHI +6.5 | 242.5 | CHI +7.5 covers 53%; o245.5 44% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dailyn Swain (CHI) | Questionable | 55% | 9.6 | 3.2 | 1.4 | 1.4 | 0.2 | 0.6 | 0.2 | 1.2 | 5.9 | small |
| RayJ Dennis (ATL) | Questionable | 55% | 9.1 | 3.5 | 1.2 | 1.5 | 0.3 | 0.4 | 0.2 | 0.6 | 6.1 | small |
| Kingston Flemings (ATL) | Questionable | 55% | 22.0 | 8.4 | 2.8 | 4.0 | 0.8 | 0.9 | 0.4 | 1.9 | 15.3 | full tables below |
| Norman Powell (CHI) | Questionable | 55% | 30.5 | 20.1 | 3.3 | 2.3 | 2.3 | 1.3 | 0.3 | 2.4 | 25.6 | full tables below |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 35.7<br><sub>-,-,-,36,38</sub> | 23.2<br><sub>-,-,-,30,15</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 9.6<br><sub>-,-,-,7,7</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>-,-,-,6,4</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.6 | 3.0 | 40.4 |
| Nickeil Alexander-Walker | 98% | 33.5<br><sub>31,32,33,31,34</sub> | 23.5<br><sub>34,26,28,20,20</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>4,4,2,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.6<br><sub>4,2,2,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.4<br><sub>9,6,4,2,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.5 | 0.5 | 2.2 | 30.6 |
| Dyson Daniels | 98% | 32.5<br><sub>31,34,35,31,31</sub> | 11.7<br><sub>6,8,13,9,10</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>9,16,9,10,6</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.5<br><sub>4,8,12,7,8</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,0,0,0,1</sub> | 0.5<br><sub>o 41% · u 59%</sub> | 2.9 | 0.5 | 1.6 | 25.7 |
| Onyeka Okongwu | 98% | 32.0<br><sub>33,31,33,30,30</sub> | 15.4<br><sub>13,14,22,16,16</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 8.4<br><sub>10,16,10,2,9</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>3,4,1,5,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 1.0 | 1.3 | 27.0 |
| CJ McCollum | 98% | 27.2<br><sub>32,25,23,21,24</sub> | 17.0<br><sub>13,15,4,9,21</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>9,5,3,4,0</sub> |  | 4.3<br><sub>12,5,4,3,4</sub> |  | 2.1<br><sub>2,2,0,1,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.6 | 2.1 | 24.5 |
| Aaron Wiggins | 98% | 26.1<br><sub>24,29,29,26,23</sub> | 13.8<br><sub>7,15,19,20,15</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>3,4,4,4,3</sub> |  | 2.6<br><sub>2,2,3,6,3</sub> |  | 2.2<br><sub>1,3,3,5,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 1.4 | 19.9 |
| Luguentz Dort | 98% | 25.1<br><sub>31,31,32,20,18</sub> | 8.8<br><sub>14,6,25,3,4</sub> |  | 3.2<br><sub>2,3,7,2,3</sub> |  | 1.8<br><sub>0,3,4,1,2</sub> |  | 1.4<br><sub>4,2,5,1,1</sub> |  | 1.1 | 0.3 | 0.7 | 13.8 |
| Jock Landale | 80% | 14.9<br><sub>-,-,-,-,14</sub> | 6.2<br><sub>-,-,-,-,5</sub> |  | 4.2<br><sub>-,-,-,-,5</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.5 | 0.7 | 11.7 |
| Zuby Ejiofor | 80% | 12.7<br><sub>15,17,15,18,4</sub> | 4.4<br><sub>3,11,10,7,0</sub> |  | 3.1<br><sub>5,3,5,6,0</sub> |  | 1.3<br><sub>2,2,5,0,0</sub> |  | 0.4<br><sub>1,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 8.7 |
| Corey Kispert | 52% | 11.7<br><sub>18,8,16,-,-</sub> | 6.0<br><sub>14,9,7,-,-</sub> |  | 1.5<br><sub>1,0,2,-,-</sub> |  | 1.0<br><sub>0,1,1,-,-</sub> |  | 0.8<br><sub>4,1,1,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 8.5 |
| Dorian Finney-Smith | 30% | 7.1<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.5 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Josh Giddey | 98% | 32.1<br><sub>25,32,27,34,25</sub> | 16.4<br><sub>13,13,10,19,9</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>4,4,1,7,2</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 9.1<br><sub>5,10,6,15,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 3.5 | 32.5 |
| Matas Buzelis | 98% | 31.6<br><sub>20,23,26,31,31</sub> | 18.3<br><sub>14,4,12,19,13</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>5,3,5,5,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,2,3,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.2<br><sub>2,0,1,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.4 | 2.7 | 27.0 |
| Jalen Smith | 98% | 28.6<br><sub>27,28,7,30,30</sub> | 15.2<br><sub>5,13,3,17,23</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 8.8<br><sub>12,7,2,8,4</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,4,0,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>0,1,1,2,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 1.1 | 1.4 | 25.9 |
| Patrick Williams | 64% | 27.6<br><sub>-,-,20,25,28</sub> | 9.5<br><sub>-,-,4,7,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>-,-,0,3,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>-,-,2,3,4</sub> |  | 1.2<br><sub>-,-,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.0 | 0.6 | 1.4 | 15.9 |
| Tre Jones | 98% | 26.1<br><sub>20,19,18,14,28</sub> | 15.5<br><sub>12,8,14,6,13</sub> |  | 3.4<br><sub>4,3,3,1,1</sub> |  | 5.0<br><sub>4,3,4,1,3</sub> |  | 0.5<br><sub>0,0,1,0,1</sub> |  | 1.2 | 0.2 | 1.8 | 23.9 |
| Isaac Okoro | 98% | 25.6<br><sub>18,21,15,25,23</sub> | 8.8<br><sub>6,4,6,12,0</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>3,1,1,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,0,0,1,4</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.4 | 1.0 | 13.1 |
| Nic Claxton | 97% | 20.3<br><sub>-,-,-,18,16</sub> | 9.4<br><sub>-,-,-,4,17</sub> |  | 5.8<br><sub>-,-,-,4,6</sub> |  | 2.6<br><sub>-,-,-,4,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.9 | 1.2 | 17.8 |
| Jordan Hawkins | 86% | 20.3<br><sub>6,2,7,17,24</sub> | 9.1<br><sub>0,2,2,9,7</sub> |  | 2.6<br><sub>0,0,1,0,4</sub> |  | 1.2<br><sub>0,0,0,1,2</sub> |  | 1.2<br><sub>0,0,0,1,1</sub> |  | 0.6 | 0.4 | 1.2 | 12.9 |
| Leonard Miller | 80% | 16.9<br><sub>11,9,19,-,2</sub> | 7.9<br><sub>2,2,4,-,0</sub> |  | 4.3<br><sub>2,3,6,-,0</sub> |  | 1.0<br><sub>1,0,3,-,0</sub> |  | 0.7<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.4 | 0.8 | 13.2 |
| Noa Essengue | 96% | 16.5<br><sub>16,14,14,15,11</sub> | 6.9<br><sub>10,8,6,10,8</sub> |  | 4.2<br><sub>4,6,3,7,4</sub> |  | 0.9<br><sub>0,0,0,1,3</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.4 | 0.9 | 11.9 |
| Buddy Hield | 58% | 15.4<br><sub>17,12,8,-,-</sub> | 7.3<br><sub>5,6,7,-,-</sub> |  | 2.1<br><sub>3,1,1,-,-</sub> |  | 1.4<br><sub>1,3,1,-,-</sub> |  | 1.0<br><sub>1,1,1,-,-</sub> |  | 0.6 | 0.2 | 1.0 | 10.9 |
| Zach Collins | 86% | 12.9<br><sub>2,10,14,-,3</sub> | 5.4<br><sub>0,2,3,-,2</sub> |  | 4.0<br><sub>0,3,1,-,2</sub> |  | 1.2<br><sub>0,0,3,-,1</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 10.6 |

</details>

<details><summary>if Norman Powell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 35.7<br><sub>-,-,-,36,38</sub> | 23.3<br><sub>-,-,-,30,15</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 9.7<br><sub>-,-,-,7,7</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 7.7<br><sub>-,-,-,6,4</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.6 | 3.0 | 40.7 |
| Nickeil Alexander-Walker (ATL) | 98% | 33.4<br><sub>31,32,33,31,34</sub> | 23.4<br><sub>34,26,28,20,20</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.5<br><sub>4,4,2,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.6<br><sub>4,2,2,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.4<br><sub>9,6,4,2,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.5 | 0.5 | 2.2 | 30.6 |
| Dyson Daniels (ATL) | 98% | 32.5<br><sub>31,34,35,31,31</sub> | 11.7<br><sub>6,8,13,9,10</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>9,16,9,10,6</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.5<br><sub>4,8,12,7,8</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,0,0,0,1</sub> | 0.5<br><sub>o 41% · u 59%</sub> | 3.0 | 0.5 | 1.6 | 25.8 |
| Onyeka Okongwu (ATL) | 98% | 32.1<br><sub>33,31,33,30,30</sub> | 15.3<br><sub>13,14,22,16,16</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 8.4<br><sub>10,16,10,2,9</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 3.2<br><sub>3,4,1,5,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 1.0 | 1.3 | 26.9 |
| CJ McCollum (ATL) | 98% | 27.2<br><sub>32,25,23,21,24</sub> | 17.1<br><sub>13,15,4,9,21</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>9,5,3,4,0</sub> |  | 4.2<br><sub>12,5,4,3,4</sub> |  | 2.1<br><sub>2,2,0,1,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.6 | 2.1 | 24.6 |
| Aaron Wiggins (ATL) | 98% | 26.2<br><sub>24,29,29,26,23</sub> | 13.9<br><sub>7,15,19,20,15</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 3.6<br><sub>3,4,4,4,3</sub> |  | 2.6<br><sub>2,2,3,6,3</sub> |  | 2.2<br><sub>1,3,3,5,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 1.4 | 20.1 |
| Luguentz Dort (ATL) | 98% | 25.1<br><sub>31,31,32,20,18</sub> | 8.8<br><sub>14,6,25,3,4</sub> |  | 3.2<br><sub>2,3,7,2,3</sub> |  | 1.8<br><sub>0,3,4,1,2</sub> |  | 1.4<br><sub>4,2,5,1,1</sub> |  | 1.1 | 0.3 | 0.7 | 13.8 |
| Jock Landale (ATL) | 80% | 14.9<br><sub>-,-,-,-,14</sub> | 6.2<br><sub>-,-,-,-,5</sub> |  | 4.2<br><sub>-,-,-,-,5</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.5 | 0.7 | 11.7 |
| Zuby Ejiofor (ATL) | 80% | 12.8<br><sub>15,17,15,18,4</sub> | 4.4<br><sub>3,11,10,7,0</sub> |  | 3.1<br><sub>5,3,5,6,0</sub> |  | 1.3<br><sub>2,2,5,0,0</sub> |  | 0.4<br><sub>1,1,0,1,0</sub> |  | 0.5 | 0.3 | 0.7 | 8.7 |
| Corey Kispert (ATL) | 52% | 11.7<br><sub>18,8,16,-,-</sub> | 6.2<br><sub>14,9,7,-,-</sub> |  | 1.5<br><sub>1,0,2,-,-</sub> |  | 1.0<br><sub>0,1,1,-,-</sub> |  | 0.8<br><sub>4,1,1,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 8.6 |
| Dorian Finney-Smith (ATL) | 30% | 7.0<br><sub>-,-,-,-,-</sub> | 1.9<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.5 |
| Josh Giddey (CHI) | 98% | 30.5<br><sub>25,32,27,34,25</sub> | 14.1<br><sub>13,13,10,19,9</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>4,4,1,7,2</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 8.9<br><sub>5,10,6,15,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.6 | 3.2 | 30.0 |
| Norman Powell (CHI) | 100% | 30.5<br><sub>31,29,22,-,-</sub> | 20.1<br><sub>16,18,12,-,-</sub> | 21.5 · – | 3.3<br><sub>2,3,1,-,-</sub> | 2.5 | 2.3<br><sub>3,0,1,-,-</sub> | 1.5 | 2.3<br><sub>1,1,0,-,-</sub> | 2.5 | 1.3 | 0.3 | 2.4 | 25.6 |
| Matas Buzelis (CHI) | 98% | 29.7<br><sub>20,23,26,31,31</sub> | 17.0<br><sub>14,4,12,19,13</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>5,3,5,5,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>1,2,3,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.0<br><sub>2,0,1,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.3 | 2.5 | 25.3 |
| Jalen Smith (CHI) | 98% | 27.5<br><sub>27,28,7,30,30</sub> | 14.2<br><sub>5,13,3,17,23</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 8.7<br><sub>12,7,2,8,4</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,4,0,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>0,1,1,2,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 1.1 | 1.2 | 24.8 |
| Patrick Williams (CHI) | 64% | 25.0<br><sub>-,-,20,25,28</sub> | 8.0<br><sub>-,-,4,7,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>-,-,0,3,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>-,-,2,3,4</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.9 | 0.5 | 1.1 | 13.8 |
| Isaac Okoro (CHI) | 98% | 22.2<br><sub>18,21,15,25,23</sub> | 7.2<br><sub>6,4,6,12,0</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>3,1,1,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>2,0,0,1,4</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.4 | 0.8 | 10.9 |
| Tre Jones (CHI) | 98% | 21.9<br><sub>20,19,18,14,28</sub> | 12.2<br><sub>12,8,14,6,13</sub> |  | 2.9<br><sub>4,3,3,1,1</sub> |  | 3.9<br><sub>4,3,4,1,3</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 1.0 | 0.2 | 1.4 | 19.0 |
| Nic Claxton (CHI) | 97% | 17.9<br><sub>-,-,-,18,16</sub> | 7.9<br><sub>-,-,-,4,17</sub> |  | 5.2<br><sub>-,-,-,4,6</sub> |  | 2.3<br><sub>-,-,-,4,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.8 | 1.1 | 15.3 |
| Jordan Hawkins (CHI) | 86% | 14.9<br><sub>6,2,7,17,24</sub> | 6.4<br><sub>0,2,2,9,7</sub> |  | 2.0<br><sub>0,0,1,0,4</sub> |  | 0.9<br><sub>0,0,0,1,2</sub> |  | 0.8<br><sub>0,0,0,1,1</sub> |  | 0.4 | 0.3 | 0.8 | 9.3 |
| Noa Essengue (CHI) | 96% | 13.0<br><sub>16,14,14,15,11</sub> | 5.6<br><sub>10,8,6,10,8</sub> |  | 3.3<br><sub>4,6,3,7,4</sub> |  | 0.7<br><sub>0,0,0,1,3</sub> |  | 0.5<br><sub>1,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.7 | 9.6 |
| Leonard Miller (CHI) | 80% | 12.0<br><sub>11,9,19,-,2</sub> | 5.8<br><sub>2,2,4,-,0</sub> |  | 3.1<br><sub>2,3,6,-,0</sub> |  | 0.7<br><sub>1,0,3,-,0</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.3 | 0.6 | 9.6 |
| Buddy Hield (CHI) | 58% | 11.7<br><sub>17,12,8,-,-</sub> | 5.5<br><sub>5,6,7,-,-</sub> |  | 1.7<br><sub>3,1,1,-,-</sub> |  | 1.1<br><sub>1,3,1,-,-</sub> |  | 0.7<br><sub>1,1,1,-,-</sub> |  | 0.5 | 0.2 | 0.7 | 8.2 |
| Zach Collins (CHI) | 86% | 10.1<br><sub>2,10,14,-,3</sub> | 4.3<br><sub>0,2,3,-,2</sub> |  | 3.2<br><sub>0,3,1,-,2</sub> |  | 1.0<br><sub>0,0,3,-,1</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.3 | 0.6 | 8.5 |

</details>

<details><summary>if Kingston Flemings plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 98% | 33.8<br><sub>-,-,-,36,38</sub> | 22.1<br><sub>-,-,-,30,15</sub> | 22.5 · –<br><sub>o 48% · u 52%</sub> | 9.2<br><sub>-,-,-,7,7</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>-,-,-,6,4</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>-,-,-,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.6 | 2.8 | 38.2 |
| Nickeil Alexander-Walker (ATL) | 98% | 31.4<br><sub>31,32,33,31,34</sub> | 22.4<br><sub>34,26,28,20,20</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,4,2,3,4</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.1<br><sub>4,2,2,1,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 3.2<br><sub>9,6,4,2,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.5 | 1.9 | 28.8 |
| Dyson Daniels (ATL) | 98% | 30.6<br><sub>31,34,35,31,31</sub> | 10.7<br><sub>6,8,13,9,10</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>9,16,9,10,6</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 5.9<br><sub>4,8,12,7,8</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,0,0,0,1</sub> | 0.5<br><sub>o 41% · u 59%</sub> | 2.9 | 0.5 | 1.4 | 23.6 |
| Onyeka Okongwu (ATL) | 98% | 30.1<br><sub>33,31,33,30,30</sub> | 13.9<br><sub>13,14,22,16,16</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>10,16,10,2,9</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>3,4,1,5,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 1.0 | 1.3 | 24.7 |
| CJ McCollum (ATL) | 98% | 24.9<br><sub>32,25,23,21,24</sub> | 15.8<br><sub>13,15,4,9,21</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>9,5,3,4,0</sub> |  | 3.6<br><sub>12,5,4,3,4</sub> |  | 1.9<br><sub>2,2,0,1,3</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.6 | 1.8 | 22.4 |
| Aaron Wiggins (ATL) | 98% | 23.1<br><sub>24,29,29,26,23</sub> | 12.1<br><sub>7,15,19,20,15</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,4,4,4,3</sub> |  | 2.0<br><sub>2,2,3,6,3</sub> |  | 1.9<br><sub>1,3,3,5,4</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.4 | 1.2 | 17.4 |
| Kingston Flemings (ATL) | 100% | 22.0<br><sub>-,23,25,27,24</sub> | 8.4<br><sub>-,14,11,10,8</sub> | 10.5 · – | 2.8<br><sub>-,3,1,2,3</sub> | 2.5 | 4.0<br><sub>-,4,6,1,4</sub> | 4.5 | 0.8<br><sub>-,2,1,0,1</sub> | 0.5 | 0.9 | 0.4 | 1.9 | 15.3 |
| Luguentz Dort (ATL) | 98% | 21.8<br><sub>31,31,32,20,18</sub> | 7.5<br><sub>14,6,25,3,4</sub> |  | 2.9<br><sub>2,3,7,2,3</sub> |  | 1.4<br><sub>0,3,4,1,2</sub> |  | 1.2<br><sub>4,2,5,1,1</sub> |  | 0.9 | 0.3 | 0.6 | 11.8 |
| Jock Landale (ATL) | 80% | 13.7<br><sub>-,-,-,-,14</sub> | 6.3<br><sub>-,-,-,-,5</sub> |  | 3.9<br><sub>-,-,-,-,5</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.4 | 0.4 | 0.6 | 11.4 |
| Zuby Ejiofor (ATL) | 80% | 10.1<br><sub>15,17,15,18,4</sub> | 4.0<br><sub>3,11,10,7,0</sub> |  | 2.4<br><sub>5,3,5,6,0</sub> |  | 1.0<br><sub>2,2,5,0,0</sub> |  | 0.3<br><sub>1,1,0,1,0</sub> |  | 0.4 | 0.2 | 0.5 | 7.4 |
| Corey Kispert (ATL) | 52% | 9.1<br><sub>18,8,16,-,-</sub> | 5.2<br><sub>14,9,7,-,-</sub> |  | 1.2<br><sub>1,0,2,-,-</sub> |  | 0.8<br><sub>0,1,1,-,-</sub> |  | 0.6<br><sub>4,1,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 7.1 |
| Dorian Finney-Smith (ATL) | 30% | 6.4<br><sub>-,-,-,-,-</sub> | 2.0<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.4 |
| Josh Giddey (CHI) | 98% | 32.1<br><sub>25,32,27,34,25</sub> | 16.5<br><sub>13,13,10,19,9</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>4,4,1,7,2</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 9.1<br><sub>5,10,6,15,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.6 | 3.6 | 32.6 |
| Matas Buzelis (CHI) | 98% | 31.6<br><sub>20,23,26,31,31</sub> | 18.4<br><sub>14,4,12,19,13</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>5,3,5,5,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>1,2,3,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.2<br><sub>2,0,1,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.4 | 2.7 | 27.1 |
| Jalen Smith (CHI) | 98% | 28.7<br><sub>27,28,7,30,30</sub> | 15.1<br><sub>5,13,3,17,23</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 8.8<br><sub>12,7,2,8,4</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,4,0,2,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>0,1,1,2,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 1.1 | 1.4 | 25.9 |
| Patrick Williams (CHI) | 64% | 27.7<br><sub>-,-,20,25,28</sub> | 9.6<br><sub>-,-,4,7,9</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>-,-,0,3,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>-,-,2,3,4</sub> |  | 1.2<br><sub>-,-,0,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.0 | 0.6 | 1.4 | 15.9 |
| Tre Jones (CHI) | 98% | 26.2<br><sub>20,19,18,14,28</sub> | 15.4<br><sub>12,8,14,6,13</sub> |  | 3.4<br><sub>4,3,3,1,1</sub> |  | 5.0<br><sub>4,3,4,1,3</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 1.2 | 0.2 | 1.7 | 23.8 |
| Isaac Okoro (CHI) | 98% | 25.5<br><sub>18,21,15,25,23</sub> | 8.8<br><sub>6,4,6,12,0</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>3,1,1,2,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>2,0,0,1,4</sub> |  | 0.8<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.4 | 1.0 | 13.1 |
| Jordan Hawkins (CHI) | 86% | 20.3<br><sub>6,2,7,17,24</sub> | 9.1<br><sub>0,2,2,9,7</sub> |  | 2.6<br><sub>0,0,1,0,4</sub> |  | 1.2<br><sub>0,0,0,1,2</sub> |  | 1.2<br><sub>0,0,0,1,1</sub> |  | 0.6 | 0.4 | 1.2 | 12.9 |
| Nic Claxton (CHI) | 97% | 20.2<br><sub>-,-,-,18,16</sub> | 9.4<br><sub>-,-,-,4,17</sub> |  | 5.7<br><sub>-,-,-,4,6</sub> |  | 2.6<br><sub>-,-,-,4,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.9 | 1.2 | 17.8 |
| Leonard Miller (CHI) | 80% | 16.9<br><sub>11,9,19,-,2</sub> | 7.9<br><sub>2,2,4,-,0</sub> |  | 4.3<br><sub>2,3,6,-,0</sub> |  | 1.0<br><sub>1,0,3,-,0</sub> |  | 0.7<br><sub>0,0,0,-,0</sub> |  | 0.5 | 0.4 | 0.9 | 13.2 |
| Noa Essengue (CHI) | 96% | 16.5<br><sub>16,14,14,15,11</sub> | 6.9<br><sub>10,8,6,10,8</sub> |  | 4.2<br><sub>4,6,3,7,4</sub> |  | 0.9<br><sub>0,0,0,1,3</sub> |  | 0.7<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.4 | 0.9 | 11.9 |
| Buddy Hield (CHI) | 58% | 15.4<br><sub>17,12,8,-,-</sub> | 7.3<br><sub>5,6,7,-,-</sub> |  | 2.1<br><sub>3,1,1,-,-</sub> |  | 1.4<br><sub>1,3,1,-,-</sub> |  | 1.0<br><sub>1,1,1,-,-</sub> |  | 0.6 | 0.2 | 1.0 | 10.9 |
| Zach Collins (CHI) | 86% | 12.9<br><sub>2,10,14,-,3</sub> | 5.3<br><sub>0,2,3,-,2</sub> |  | 4.0<br><sub>0,3,1,-,2</sub> |  | 1.3<br><sub>0,0,3,-,1</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.4 | 0.8 | 10.5 |

</details>


### MEM @ NOP
Out: Bryce McGowens (NOP), Yves Missi (NOP), Trey Murphy III (NOP), Dejounte Murray (NOP), Trendon Watford (NOP), Zach Edey (MEM), Jahmai Mashack (MEM), Scotty Pippen Jr. (MEM), Quinten Post (MEM)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 122.6–118.5 | MEM 61% | 1.64 / 2.56 | NOP +4.5 | 240.5 | NOP +3.5 covers 47%; o235.5 61% |
| Expected (weighted by chance each plays) | 122.6–118.3 | MEM 61% | 1.63 / 2.59 | NOP +4.5 | 240.5 | NOP +3.5 covers 47%; o235.5 61% |
| if Bennedict Mathurin plays | 122.2–118.2 | MEM 61% | 1.65 / 2.55 | NOP +4.5 | 240.5 | NOP +3.5 covers 48%; o235.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Bennedict Mathurin (NOP) | Questionable | 55% | 22.5 | 10.0 | 4.0 | 2.0 | 0.7 | 0.7 | 0.3 | 1.3 | 16.0 | full tables below |

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 98% | 33.6<br><sub>38,33,31,33,33</sub> | 16.9<br><sub>18,10,8,22,13</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 10.1<br><sub>9,6,12,7,11</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>5,4,4,8,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>2,2,0,0,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.7 | 0.7 | 3.0 | 32.6 |
| Ty Jerome | 98% | 31.5<br><sub>37,29,28,32,32</sub> | 24.1<br><sub>40,23,21,27,22</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,4,2,6,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>5,3,5,2,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>5,2,2,5,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 2.5 | 33.6 |
| Jaylen Wells | 98% | 29.0<br><sub>34,21,25,26,31</sub> | 12.7<br><sub>16,0,7,14,22</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,1,0,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>3,3,0,1,1</sub> |  | 1.9<br><sub>3,0,1,4,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 1.0 | 17.9 |
| Cedric Coward | 98% | 28.9<br><sub>31,33,23,28,27</sub> | 14.7<br><sub>10,23,10,3,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>9,9,9,6,11</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>3,4,0,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.5 | 1.6 | 25.6 |
| Jerami Grant | 98% | 24.1<br><sub>24,24,22,22,20</sub> | 11.8<br><sub>11,11,10,17,14</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>4,1,0,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,2,2,2,2</sub> |  | 1.5<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.7 | 1.2 | 16.2 |
| Cam Spencer | 98% | 22.1<br><sub>19,24,19,17,20</sub> | 10.1<br><sub>13,7,7,7,15</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>1,6,1,2,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>7,9,0,4,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,1,1,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.2 | 1.2 | 18.2 |
| Javon Small | 96% | 20.7<br><sub>-,-,21,24,15</sub> | 9.4<br><sub>-,-,10,9,3</sub> |  | 2.9<br><sub>-,-,4,2,1</sub> |  | 3.6<br><sub>-,-,2,5,4</sub> |  | 1.2<br><sub>-,-,1,1,1</sub> |  | 0.8 | 0.2 | 1.2 | 15.9 |
| Isaiah Stewart | 98% | 19.0<br><sub>28,10,-,-,18</sub> | 9.0<br><sub>14,6,-,-,3</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>5,1,-,-,1</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.0<br><sub>2,0,-,-,2</sub> |  | 0.6<br><sub>2,0,-,-,1</sub> |  | 0.3 | 1.2 | 0.9 | 14.2 |
| GG Jackson | 86% | 15.1<br><sub>16,7,-,17,13</sub> | 7.8<br><sub>6,1,-,2,2</sub> |  | 3.1<br><sub>0,2,-,1,1</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.5 | 0.9 | 11.8 |
| Taylor Hendricks | 67% | 12.3<br><sub>-,-,4,16,11</sub> | 4.9<br><sub>-,-,4,9,7</sub> |  | 2.6<br><sub>-,-,2,3,2</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.6<br><sub>-,-,1,1,1</sub> |  | 0.6 | 0.4 | 0.5 | 8.1 |
| Kris Murray | 66% | 10.9<br><sub>19,15,13,1,-</sub> | 2.8<br><sub>0,5,2,0,-</sub> |  | 1.9<br><sub>4,1,2,0,-</sub> |  | 0.7<br><sub>1,1,1,0,-</sub> |  | 0.1<br><sub>0,1,0,0,-</sub> |  | 0.4 | 0.3 | 0.3 | 5.3 |
| Olivier-Maxence Prosper | 58% | 8.9<br><sub>-,7,11,1,-</sub> | 4.6<br><sub>-,4,2,0,-</sub> |  | 1.9<br><sub>-,3,3,0,-</sub> |  | 0.5<br><sub>-,1,1,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 7.1 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zion Williamson | 98% | 35.6<br><sub>38,36,31,-,30</sub> | 24.6<br><sub>23,13,25,-,29</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>4,8,4,-,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 4.1<br><sub>2,4,2,-,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,0,0,-,1</sub> |  | 1.6 | 0.9 | 2.8 | 35.3 |
| Jeremiah Fears | 98% | 33.9<br><sub>34,36,29,29,28</sub> | 21.1<br><sub>19,24,25,11,14</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>6,5,6,3,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 6.4<br><sub>2,5,5,8,5</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,0,3,1,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.6 | 3.3 | 32.5 |
| Saddiq Bey | 98% | 32.9<br><sub>29,31,26,24,29</sub> | 20.2<br><sub>22,17,13,9,15</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>4,5,4,0,1</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>3,4,3,4,2</sub> |  | 2.2<br><sub>2,3,1,1,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 1.5 | 28.3 |
| Herbert Jones | 98% | 29.9<br><sub>37,14,20,24,25</sub> | 9.9<br><sub>2,0,4,10,2</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>5,4,0,6,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>1,0,1,1,3</sub> |  | 1.2<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.6 | 0.6 | 1.5 | 16.5 |
| Karlo Matkovic | 96% | 28.9<br><sub>21,18,19,17,22</sub> | 12.2<br><sub>5,18,3,4,4</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>4,3,3,6,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>2,1,2,2,1</sub> |  | 1.4<br><sub>1,4,1,0,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.9 | 1.3 | 1.4 | 20.7 |
| Derik Queen | 98% | 28.2<br><sub>27,10,21,21,14</sub> | 15.2<br><sub>20,6,8,16,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.3<br><sub>9,4,5,4,0</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>6,1,3,0,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,0,0,0,1</sub> |  | 1.3 | 1.2 | 2.9 | 27.3 |
| Jordan Poole | 63% | 25.9<br><sub>-,-,-,34,21</sub> | 13.5<br><sub>-,-,-,7,14</sub> |  | 2.7<br><sub>-,-,-,3,0</sub> |  | 3.7<br><sub>-,-,-,2,1</sub> |  | 2.2<br><sub>-,-,-,1,2</sub> |  | 0.9 | 0.5 | 1.8 | 19.9 |
| DeAndre Jordan | 38% | 18.0<br><sub>-,-,-,-,11</sub> | 4.6<br><sub>-,-,-,-,0</sub> |  | 7.2<br><sub>-,-,-,-,3</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 1.2 | 0.9 | 12.9 |
| Jaron Pierre Jr. | 80% | 14.8<br><sub>-,-,-,-,7</sub> | 4.7<br><sub>-,-,-,-,4</sub> |  | 4.9<br><sub>-,-,-,-,4</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.8 | 0.2 | 0.7 | 10.7 |
| AJ Johnson | 58% | 14.6<br><sub>-,-,3,12,7</sub> | 4.1<br><sub>-,-,2,2,2</sub> |  | 1.8<br><sub>-,-,0,2,1</sub> |  | 1.4<br><sub>-,-,0,3,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.6 | 0.3 | 0.7 | 7.3 |
| Julian Reese | 63% | 13.5<br><sub>-,-,3,9,7</sub> | 4.2<br><sub>-,-,0,2,2</sub> |  | 2.1<br><sub>-,-,0,0,2</sub> |  | 1.0<br><sub>-,-,0,0,1</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.6 | 0.6 | 0.8 | 7.3 |
| Malik Dia | 35% | 8.6 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.5 | 5.9 |

</details>

<details><summary>if Bennedict Mathurin plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 98% | 33.6<br><sub>38,33,31,33,33</sub> | 16.9<br><sub>18,10,8,22,13</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>9,6,12,7,11</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>5,4,4,8,5</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>2,2,0,0,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.7 | 3.0 | 32.7 |
| Ty Jerome (MEM) | 98% | 31.5<br><sub>37,29,28,32,32</sub> | 24.0<br><sub>40,23,21,27,22</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,4,2,6,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>5,3,5,2,5</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>5,2,2,5,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.2 | 0.3 | 2.6 | 33.5 |
| Jaylen Wells (MEM) | 98% | 29.0<br><sub>34,21,25,26,31</sub> | 12.7<br><sub>16,0,7,14,22</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,1,0,4,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.7<br><sub>3,3,0,1,1</sub> |  | 1.9<br><sub>3,0,1,4,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.2 | 1.0 | 17.9 |
| Cedric Coward (MEM) | 98% | 28.8<br><sub>31,33,23,28,27</sub> | 14.7<br><sub>10,23,10,3,15</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 7.8<br><sub>9,9,9,6,11</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>3,4,0,4,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,4,2,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.5 | 1.6 | 25.6 |
| Jerami Grant (MEM) | 98% | 24.0<br><sub>24,24,22,22,20</sub> | 11.7<br><sub>11,11,10,17,14</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>4,1,0,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,2,2,2,2</sub> |  | 1.5<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.7 | 0.6 | 1.1 | 16.2 |
| Cam Spencer (MEM) | 98% | 22.0<br><sub>19,24,19,17,20</sub> | 9.9<br><sub>13,7,7,7,15</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>1,6,1,2,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>7,9,0,4,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,1,1,1,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.2 | 1.2 | 18.1 |
| Javon Small (MEM) | 96% | 20.7<br><sub>-,-,21,24,15</sub> | 9.4<br><sub>-,-,10,9,3</sub> |  | 2.9<br><sub>-,-,4,2,1</sub> |  | 3.6<br><sub>-,-,2,5,4</sub> |  | 1.2<br><sub>-,-,1,1,1</sub> |  | 0.8 | 0.2 | 1.2 | 15.9 |
| Isaiah Stewart (MEM) | 98% | 19.0<br><sub>28,10,-,-,18</sub> | 9.0<br><sub>14,6,-,-,3</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>5,1,-,-,1</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.0<br><sub>2,0,-,-,2</sub> |  | 0.6<br><sub>2,0,-,-,1</sub> |  | 0.3 | 1.2 | 0.9 | 14.1 |
| GG Jackson (MEM) | 86% | 15.3<br><sub>16,7,-,17,13</sub> | 7.9<br><sub>6,1,-,2,2</sub> |  | 3.1<br><sub>0,2,-,1,1</sub> |  | 1.0<br><sub>1,0,-,0,0</sub> |  | 0.8<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.5 | 1.0 | 12.0 |
| Taylor Hendricks (MEM) | 67% | 12.3<br><sub>-,-,4,16,11</sub> | 4.9<br><sub>-,-,4,9,7</sub> |  | 2.6<br><sub>-,-,2,3,2</sub> |  | 0.6<br><sub>-,-,0,0,1</sub> |  | 0.6<br><sub>-,-,1,1,1</sub> |  | 0.6 | 0.4 | 0.5 | 8.1 |
| Kris Murray (MEM) | 66% | 11.0<br><sub>19,15,13,1,-</sub> | 2.8<br><sub>0,5,2,0,-</sub> |  | 1.9<br><sub>4,1,2,0,-</sub> |  | 0.7<br><sub>1,1,1,0,-</sub> |  | 0.2<br><sub>0,1,0,0,-</sub> |  | 0.4 | 0.3 | 0.3 | 5.3 |
| Olivier-Maxence Prosper (MEM) | 58% | 8.9<br><sub>-,7,11,1,-</sub> | 4.6<br><sub>-,4,2,0,-</sub> |  | 1.9<br><sub>-,3,3,0,-</sub> |  | 0.5<br><sub>-,1,1,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 7.0 |
| Zion Williamson (NOP) | 98% | 35.3<br><sub>38,36,31,-,30</sub> | 23.7<br><sub>23,13,25,-,29</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>4,8,4,-,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 4.0<br><sub>2,4,2,-,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.2<br><sub>0,0,0,-,1</sub> |  | 1.5 | 0.8 | 2.5 | 34.3 |
| Jeremiah Fears (NOP) | 98% | 33.3<br><sub>34,36,29,29,28</sub> | 19.9<br><sub>19,24,25,11,14</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,5,6,3,4</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 6.4<br><sub>2,5,5,8,5</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,0,3,1,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.6 | 3.2 | 31.2 |
| Saddiq Bey (NOP) | 98% | 32.5<br><sub>29,31,26,24,29</sub> | 18.8<br><sub>22,17,13,9,15</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>4,5,4,0,1</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>3,4,3,4,2</sub> |  | 2.2<br><sub>2,3,1,1,3</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.2 | 1.4 | 26.8 |
| Herbert Jones (NOP) | 98% | 28.8<br><sub>37,14,20,24,25</sub> | 9.0<br><sub>2,0,4,10,2</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>5,4,0,6,2</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>1,0,1,1,3</sub> |  | 1.1<br><sub>0,0,0,2,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.5 | 0.6 | 1.4 | 15.3 |
| Karlo Matkovic (NOP) | 96% | 26.9<br><sub>21,18,19,17,22</sub> | 10.8<br><sub>5,18,3,4,4</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>4,3,3,6,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>2,1,2,2,1</sub> |  | 1.3<br><sub>1,4,1,0,0</sub> | 0.5<br><sub>o 65% · u 35%</sub> | 0.8 | 1.3 | 1.2 | 18.7 |
| Derik Queen (NOP) | 98% | 26.6<br><sub>27,10,21,21,14</sub> | 13.7<br><sub>20,6,8,16,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.9<br><sub>9,4,5,4,0</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>6,1,3,0,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 0.4<br><sub>0,0,0,0,1</sub> |  | 1.3 | 1.1 | 2.6 | 25.1 |
| Jordan Poole (NOP) | 63% | 23.8<br><sub>-,-,-,34,21</sub> | 12.2<br><sub>-,-,-,7,14</sub> |  | 2.5<br><sub>-,-,-,3,0</sub> |  | 3.3<br><sub>-,-,-,2,1</sub> |  | 1.9<br><sub>-,-,-,1,2</sub> |  | 0.9 | 0.5 | 1.6 | 17.9 |
| Bennedict Mathurin (NOP) | 100% | 22.5<br><sub>15,7,9,24,-</sub> | 10.0<br><sub>2,2,6,6,-</sub> |  | 4.0<br><sub>5,0,0,2,-</sub> |  | 2.0<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,0,0,0,-</sub> |  | 0.7 | 0.3 | 1.3 | 16.0 |
| DeAndre Jordan (NOP) | 38% | 16.3<br><sub>-,-,-,-,11</sub> | 4.1<br><sub>-,-,-,-,0</sub> |  | 6.6<br><sub>-,-,-,-,3</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 1.1 | 0.8 | 11.7 |
| Jaron Pierre Jr. (NOP) | 80% | 12.9<br><sub>-,-,-,-,7</sub> | 4.1<br><sub>-,-,-,-,4</sub> |  | 4.3<br><sub>-,-,-,-,4</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.7 | 0.1 | 0.7 | 9.3 |
| AJ Johnson (NOP) | 58% | 12.0<br><sub>-,-,3,12,7</sub> | 3.4<br><sub>-,-,2,2,2</sub> |  | 1.5<br><sub>-,-,0,2,1</sub> |  | 1.2<br><sub>-,-,0,3,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.6 | 6.1 |
| Julian Reese (NOP) | 63% | 11.2<br><sub>-,-,3,9,7</sub> | 3.5<br><sub>-,-,0,2,2</sub> |  | 1.8<br><sub>-,-,0,0,2</sub> |  | 0.9<br><sub>-,-,0,0,1</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.5 | 0.5 | 0.6 | 6.1 |
| Malik Dia (NOP) | 35% | 8.5 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.8 |

</details>


### UTA @ HOU
Out: Steven Adams (HOU), Clint Capela (HOU), Marcus Smart (HOU), Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Lauri Markkanen (UTA), Jusuf Nurkic (UTA)

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 31.6<br><sub>44,32,30,-,33</sub> | 20.7<br><sub>39,16,19,-,13</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>2,6,5,-,7</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>9,9,8,-,7</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,1,0,-,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.2 | 3.2 | 29.6 |
| Darryn Peterson | 98% | 31.1<br><sub>30,30,35,31,33</sub> | 15.9<br><sub>7,21,26,25,22</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>2,2,6,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.7<br><sub>7,5,4,4,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>0,3,4,4,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.6 | 2.1 | 23.4 |
| Ace Bailey | 98% | 31.0<br><sub>35,29,32,35,31</sub> | 15.0<br><sub>15,12,7,23,18</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>5,6,2,7,7</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,0,3,2,2</sub> |  | 2.0<br><sub>1,0,1,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.9 | 2.0 | 22.0 |
| Jaxson Hayes | 98% | 27.1<br><sub>21,28,29,17,30</sub> | 9.1<br><sub>2,8,18,6,11</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>7,6,6,2,8</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,3,1,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.2 | 1.2 | 16.7 |
| Josh Green | 91% | 24.3<br><sub>23,24,28,30,26</sub> | 5.2<br><sub>7,3,10,2,3</sub> | 4.5 · –<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,3,0,5,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2<br><sub>0,1,1,4,1</sub> |  | 0.7<br><sub>1,1,1,0,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.9 | 0.2 | 0.8 | 8.8 |
| Brice Sensabaugh | 98% | 20.1<br><sub>12,10,13,14,23</sub> | 11.7<br><sub>6,0,2,5,19</sub> |  | 2.9<br><sub>2,2,3,4,3</sub> |  | 1.5<br><sub>0,2,0,4,1</sub> |  | 1.6<br><sub>1,0,0,1,3</sub> |  | 0.7 | 0.2 | 1.7 | 16.1 |
| Josh Okogie | 96% | 19.3<br><sub>26,24,17,21,15</sub> | 5.2<br><sub>3,12,0,6,7</sub> |  | 3.1<br><sub>6,4,1,4,3</sub> |  | 1.0<br><sub>1,0,0,4,0</sub> |  | 0.5<br><sub>1,2,0,0,1</sub> |  | 0.9 | 0.3 | 0.8 | 9.3 |
| Svi Mykhailiuk | 96% | 17.5<br><sub>17,14,6,21,20</sub> | 6.3<br><sub>6,0,0,7,3</sub> |  | 1.9<br><sub>3,0,0,2,0</sub> |  | 1.2<br><sub>0,1,0,3,2</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.1 | 0.7 | 9.4 |
| Mo Bamba | 80% | 17.2<br><sub>15,-,17,17,18</sub> | 5.7<br><sub>7,-,3,7,5</sub> |  | 5.6<br><sub>10,-,3,7,1</sub> |  | 0.7<br><sub>1,-,1,0,1</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5 | 1.3 | 0.8 | 12.0 |
| Isaiah Collier | 98% | 17.1<br><sub>3,13,16,24,12</sub> | 8.4<br><sub>0,4,6,17,7</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>1,3,4,5,3</sub> |  | 4.0<br><sub>0,3,2,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>0,0,0,4,1</sub> |  | 0.8 | 0.2 | 1.6 | 14.6 |
| Kyle Filipowski | 63% | 14.0<br><sub>-,1,15,15,-</sub> | 6.7<br><sub>-,0,9,7,-</sub> |  | 4.1<br><sub>-,0,6,4,-</sub> |  | 1.3<br><sub>-,0,1,1,-</sub> |  | 0.5<br><sub>-,0,1,0,-</sub> |  | 0.6 | 0.3 | 1.1 | 12.0 |
| Tony Bradley | 58% | 9.7<br><sub>-,1,2,14,-</sub> | 3.1<br><sub>-,0,0,4,-</sub> |  | 2.8<br><sub>-,1,1,5,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.3 | 0.5 | 6.3 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 36.5<br><sub>36,35,39,38,35</sub> | 17.3<br><sub>14,11,15,14,14</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>10,4,9,7,8</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>0,2,2,3,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.7<br><sub>4,2,1,2,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 1.0 | 1.4 | 27.0 |
| Kevin Durant | 98% | 35.9<br><sub>33,35,38,36,34</sub> | 25.5<br><sub>12,21,21,23,20</sub> | 21.5 · –<br><sub>o 53% · u 47%</sub> | 6.2<br><sub>3,5,10,12,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>3,2,3,8,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>0,2,1,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 1.1 | 3.1 | 36.7 |
| Alperen Sengun | 88% | 35.6<br><sub>38,39,32,35,37</sub> | 22.0<br><sub>26,17,15,20,19</sub> | 20.5 · –<br><sub>o 51% · u 49%</sub> | 10.2<br><sub>7,12,6,12,13</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 7.5<br><sub>10,10,5,8,9</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 0.7<br><sub>1,0,1,1,1</sub> |  | 1.4 | 1.3 | 2.8 | 39.7 |
| Amen Thompson | 98% | 35.3<br><sub>25,32,39,35,29</sub> | 17.8<br><sub>14,11,17,8,19</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>3,8,7,9,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 4.6<br><sub>3,1,0,3,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.2<br><sub>0,0,0,0,0</sub> |  | 1.7 | 0.8 | 2.1 | 29.8 |
| Fred VanVleet | 91% | 32.8<br><sub>27,30,31,30,30</sub> | 14.0<br><sub>8,18,16,12,18</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>2,3,3,1,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.4<br><sub>9,3,4,2,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>2,4,4,3,4</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.4 | 1.5 | 22.9 |
| Tari Eason | 98% | 25.9<br><sub>27,24,23,19,22</sub> | 10.9<br><sub>13,9,2,12,6</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>4,6,7,5,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,1,2,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2<br><sub>3,1,0,2,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.9 | 1.2 | 18.6 |
| Reed Sheppard | 88% | 22.8<br><sub>17,21,13,17,20</sub> | 11.4<br><sub>8,14,6,8,13</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,2,0,0,1</sub> |  | 2.9<br><sub>1,2,0,0,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,3,2,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.6 | 1.2 | 16.6 |
| Bogdan Bogdanovic | 96% | 13.8<br><sub>5,5,2,12,10</sub> | 5.0<br><sub>0,0,0,8,0</sub> |  | 1.7<br><sub>0,0,1,3,0</sub> |  | 1.3<br><sub>1,0,0,1,0</sub> |  | 0.8<br><sub>0,0,0,2,0</sub> |  | 0.5 | 0.1 | 0.6 | 8.0 |
| Oscar Tshiebwe | 91% | 8.7<br><sub>7,2,3,-,1</sub> | 3.5<br><sub>4,2,2,-,0</sub> |  | 3.6<br><sub>1,0,0,-,0</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.4 | 7.6 |
| Isaiah Crawford | 64% | 7.5<br><sub>2,-,-,1,1</sub> | 2.3<br><sub>0,-,-,0,0</sub> |  | 1.1<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>0,-,-,0,0</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.2 | 3.8 |
| Jae'Sean Tate | 52% | 7.4<br><sub>2,-,-,-,1</sub> | 2.1<br><sub>0,-,-,-,0</sub> |  | 1.8<br><sub>1,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.4 |
| Bruce Thornton | 66% | 7.4<br><sub>2,-,-,1,3</sub> | 2.5<br><sub>2,-,-,0,0</sub> |  | 1.8<br><sub>0,-,-,0,0</sub> |  | 0.5<br><sub>0,-,-,0,0</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.3 | 4.8 |

</details>


### GSW @ SAS
Out: Tobias Harris (SAS), Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Brandon Williams (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.9–114.3 | GSW 37% | 2.68 / 1.60 | SAS -4.5 | 224.5 | SAS -12.5 covers 28%; o217.5 64% |
| Expected (weighted by chance each plays) | 109.9–115.6 | GSW 34% | 2.94 / 1.51 | SAS -5.5 | 225.5 | SAS -12.5 covers 32%; o217.5 67% |
| if De'Aaron Fox plays | 109.8–115.9 | GSW 33% | 3.03 / 1.49 | SAS -6.5 | 225.5 | SAS -12.5 covers 32%; o217.5 67% |
| if Devin Vassell plays | 110.5–115.5 | GSW 36% | 2.80 / 1.56 | SAS -5.5 | 225.5 | SAS -12.5 covers 30%; o217.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| De'Aaron Fox (SAS) | Questionable | 55% | 32.0 | 15.3 | 4.0 | 6.2 | 1.5 | 1.5 | 0.4 | 2.3 | 25.5 | full tables below |
| Devin Vassell (SAS) | Questionable | 55% | 31.9 | 12.8 | 4.3 | 3.1 | 2.1 | 1.3 | 0.4 | 1.2 | 20.3 | full tables below |

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 96% | 35.1<br><sub>33,32,39,26,37</sub> | 18.3<br><sub>20,9,15,25,22</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>3,6,7,2,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,3,1,4,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>3,2,4,5,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 2.0 | 28.3 |
| Yaxel Lendeborg | 98% | 34.6<br><sub>29,30,37,27,36</sub> | 24.2<br><sub>16,17,23,23,25</sub> | 20.5 · –<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>5,8,8,7,10</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>5,6,3,4,0</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>2,1,2,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.6 | 3.2 | 35.1 |
| Draymond Green | 93% | 28.8<br><sub>17,27,34,21,27</sub> | 6.8<br><sub>4,2,2,2,7</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 5.2<br><sub>4,5,6,3,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.4<br><sub>2,11,13,6,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>0,0,0,0,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.7 | 2.4 | 18.3 |
| De'Anthony Melton | 98% | 25.4<br><sub>28,17,17,26,25</sub> | 11.5<br><sub>2,5,4,16,11</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>7,6,1,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>2,2,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>0,0,1,4,3</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.4 | 1.7 | 18.3 |
| Georges Niang | 98% | 21.8<br><sub>22,22,25,19,19</sub> | 9.1<br><sub>13,13,11,9,5</sub> |  | 2.9<br><sub>4,4,2,2,5</sub> |  | 1.3<br><sub>3,3,1,2,0</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 0.4 | 0.2 | 1.0 | 13.3 |
| Will Richard | 98% | 20.3<br><sub>28,16,12,-,19</sub> | 5.9<br><sub>6,10,4,-,9</sub> |  | 2.4<br><sub>5,0,2,-,4</sub> |  | 1.2<br><sub>0,2,1,-,0</sub> |  | 0.7<br><sub>2,2,0,-,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.4 |
| Al Horford | 98% | 19.9<br><sub>-,18,13,15,21</sub> | 6.6<br><sub>-,8,2,5,2</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>-,5,5,2,1</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>-,1,4,6,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>-,2,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.8 | 0.7 | 12.6 |
| Gui Santos | 91% | 18.0<br><sub>-,-,12,21,12</sub> | 7.2<br><sub>-,-,3,3,0</sub> |  | 3.3<br><sub>-,-,1,7,3</sub> |  | 1.8<br><sub>-,-,0,4,1</sub> |  | 0.7<br><sub>-,-,0,0,0</sub> |  | 0.6 | 0.2 | 1.2 | 12.3 |
| Gary Payton II | 76% | 16.1<br><sub>20,10,13,-,-</sub> | 7.2<br><sub>2,9,4,-,-</sub> |  | 2.8<br><sub>2,0,0,-,-</sub> |  | 1.3<br><sub>1,0,0,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.9 | 0.2 | 0.8 | 11.2 |
| LJ Cryer | 71% | 14.2<br><sub>1,1,-,20,18</sub> | 6.6<br><sub>0,0,-,10,13</sub> |  | 1.4<br><sub>0,0,-,0,1</sub> |  | 1.1<br><sub>0,0,-,3,1</sub> |  | 1.0<br><sub>0,0,-,2,3</sub> |  | 0.3 | 0.1 | 0.7 | 9.1 |
| Charles Bassey | 91% | 14.0<br><sub>23,14,11,18,13</sub> | 6.7<br><sub>19,8,8,12,7</sub> |  | 5.3<br><sub>8,7,4,10,6</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 12.7 |
| Graham Ike | 91% | 9.7<br><sub>7,1,-,12,4</sub> | 3.9<br><sub>0,0,-,4,4</sub> |  | 2.2<br><sub>0,1,-,5,0</sub> |  | 0.7<br><sub>0,0,-,2,1</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| Malevy Leons | 58% | 8.7<br><sub>-,1,-,12,4</sub> | 2.6<br><sub>-,0,-,0,0</sub> |  | 1.6<br><sub>-,0,-,3,3</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Harper | 98% | 35.2<br><sub>36,28,28,26,36</sub> | 20.0<br><sub>21,19,13,17,18</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 5.9<br><sub>5,2,7,5,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>0,3,3,4,10</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>1,1,1,0,2</sub> | 0.5<br><sub>o 68% · u 32%</sub> | 1.4 | 0.4 | 2.2 | 31.7 |
| Victor Wembanyama | 98% | 33.0<br><sub>34,26,24,25,32</sub> | 30.1<br><sub>52,30,29,40,32</sub> | 28.5 · –<br><sub>o 49% · u 51%</sub> | 11.9<br><sub>24,14,7,11,9</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 3.8<br><sub>2,2,3,3,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,4,3,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 3.8 | 3.0 | 45.8 |
| Stephon Castle | 98% | 33.0<br><sub>35,28,24,30,29</sub> | 18.0<br><sub>17,19,14,4,11</sub> | 16.5 · –<br><sub>o 46% · u 53%</sub> | 5.6<br><sub>10,3,7,8,1</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>3,7,5,7,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>2,1,2,0,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 3.2 | 30.6 |
| Julian Champagnie | 98% | 31.9<br><sub>21,22,21,27,35</sub> | 11.6<br><sub>0,8,14,11,12</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>4,7,4,3,0</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>3,2,0,2,2</sub> |  | 2.3<br><sub>0,2,4,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 1.0 | 18.7 |
| Keldon Johnson | 98% | 28.6<br><sub>19,27,27,26,28</sub> | 11.6<br><sub>4,3,10,4,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>5,6,7,5,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>2,6,4,3,4</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.4 | 19.9 |
| Harrison Barnes | 88% | 19.9<br><sub>13,19,19,21,13</sub> | 6.8<br><sub>4,13,5,11,3</sub> |  | 2.3<br><sub>2,1,3,2,1</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 1.0<br><sub>1,2,1,2,1</sub> |  | 0.5 | 0.1 | 0.6 | 10.0 |
| Luke Kornet | 98% | 19.3<br><sub>14,18,15,13,14</sub> | 4.7<br><sub>2,2,6,2,7</sub> |  | 5.7<br><sub>1,6,4,4,5</sub> |  | 1.5<br><sub>2,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.9 | 0.7 | 11.9 |
| Carter Bryant | 88% | 17.7<br><sub>-,3,17,14,15</sub> | 6.0<br><sub>-,0,6,8,10</sub> |  | 2.7<br><sub>-,0,4,1,1</sub> |  | 1.2<br><sub>-,0,1,1,2</sub> |  | 0.9<br><sub>-,0,2,2,2</sub> |  | 0.4 | 0.5 | 0.7 | 9.9 |
| Jordan McLaughlin | 71% | 16.6<br><sub>-,8,12,11,2</sub> | 5.4<br><sub>-,2,3,4,4</sub> |  | 2.1<br><sub>-,2,0,4,0</sub> |  | 2.5<br><sub>-,1,0,2,0</sub> |  | 0.6<br><sub>-,0,1,0,0</sub> |  | 1.1 | 0.1 | 0.8 | 10.0 |
| Tarris Reed Jr. | 76% | 12.1<br><sub>-,3,9,9,2</sub> | 4.3<br><sub>-,0,2,4,0</sub> |  | 4.6<br><sub>-,1,3,3,0</sub> |  | 0.6<br><sub>-,0,1,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.8 | 9.5 |
| David Jones Garcia | 67% | 10.1<br><sub>-,3,-,8,2</sub> | 3.7<br><sub>-,0,-,2,0</sub> |  | 1.7<br><sub>-,0,-,0,0</sub> |  | 1.5<br><sub>-,0,-,0,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.7 | 0.2 | 0.6 | 6.9 |
| Ja'Kobi Gillespie | 88% | 9.9<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Maliq Brown | 80% | 9.5<br><sub>-,-,-,-,-</sub> | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 4.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 4.8 |

</details>

<details><summary>if De'Aaron Fox plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 96% | 35.0<br><sub>33,32,39,26,37</sub> | 18.3<br><sub>20,9,15,25,22</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>3,6,7,2,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,3,1,4,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>3,2,4,5,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 2.0 | 28.4 |
| Yaxel Lendeborg (GSW) | 98% | 34.6<br><sub>29,30,37,27,36</sub> | 24.2<br><sub>16,17,23,23,25</sub> | 20.5 · –<br><sub>o 53% · u 47%</sub> | 7.2<br><sub>5,8,8,7,10</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>5,6,3,4,0</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>2,1,2,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.6 | 3.2 | 35.1 |
| Draymond Green (GSW) | 93% | 28.7<br><sub>17,27,34,21,27</sub> | 6.7<br><sub>4,2,2,2,7</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>4,5,6,3,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.3<br><sub>2,11,13,6,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>0,0,0,0,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.7 | 2.4 | 18.1 |
| De'Anthony Melton (GSW) | 98% | 25.3<br><sub>28,17,17,26,25</sub> | 11.5<br><sub>2,5,4,16,11</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>7,6,1,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>2,2,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>0,0,1,4,3</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.4 | 1.7 | 18.2 |
| Georges Niang (GSW) | 98% | 21.8<br><sub>22,22,25,19,19</sub> | 9.1<br><sub>13,13,11,9,5</sub> |  | 2.9<br><sub>4,4,2,2,5</sub> |  | 1.3<br><sub>3,3,1,2,0</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 0.4 | 0.2 | 1.0 | 13.3 |
| Will Richard (GSW) | 98% | 20.4<br><sub>28,16,12,-,19</sub> | 5.9<br><sub>6,10,4,-,9</sub> |  | 2.4<br><sub>5,0,2,-,4</sub> |  | 1.2<br><sub>0,2,1,-,0</sub> |  | 0.7<br><sub>2,2,0,-,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.4 |
| Al Horford (GSW) | 98% | 19.9<br><sub>-,18,13,15,21</sub> | 6.6<br><sub>-,8,2,5,2</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>-,5,5,2,1</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>-,1,4,6,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>-,2,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.8 | 0.6 | 12.6 |
| Gui Santos (GSW) | 91% | 18.1<br><sub>-,-,12,21,12</sub> | 7.2<br><sub>-,-,3,3,0</sub> |  | 3.4<br><sub>-,-,1,7,3</sub> |  | 1.8<br><sub>-,-,0,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.6 | 0.2 | 1.1 | 12.4 |
| Gary Payton II (GSW) | 76% | 16.1<br><sub>20,10,13,-,-</sub> | 7.2<br><sub>2,9,4,-,-</sub> |  | 2.8<br><sub>2,0,0,-,-</sub> |  | 1.3<br><sub>1,0,0,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.9 | 0.2 | 0.8 | 11.2 |
| LJ Cryer (GSW) | 71% | 14.2<br><sub>1,1,-,20,18</sub> | 6.5<br><sub>0,0,-,10,13</sub> |  | 1.3<br><sub>0,0,-,0,1</sub> |  | 1.1<br><sub>0,0,-,3,1</sub> |  | 1.0<br><sub>0,0,-,2,3</sub> |  | 0.3 | 0.1 | 0.7 | 9.0 |
| Charles Bassey (GSW) | 91% | 14.1<br><sub>23,14,11,18,13</sub> | 6.7<br><sub>19,8,8,12,7</sub> |  | 5.3<br><sub>8,7,4,10,6</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 12.7 |
| Graham Ike (GSW) | 91% | 9.7<br><sub>7,1,-,12,4</sub> | 3.9<br><sub>0,0,-,4,4</sub> |  | 2.2<br><sub>0,1,-,5,0</sub> |  | 0.7<br><sub>0,0,-,2,1</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| Malevy Leons (GSW) | 58% | 8.7<br><sub>-,1,-,12,4</sub> | 2.6<br><sub>-,0,-,0,0</sub> |  | 1.6<br><sub>-,0,-,3,3</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.3 | 0.4 | 4.7 |
| Dylan Harper (SAS) | 98% | 34.0<br><sub>36,28,28,26,36</sub> | 18.0<br><sub>21,19,13,17,18</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>5,2,7,5,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 4.9<br><sub>0,3,3,4,10</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>1,1,1,0,2</sub> | 0.5<br><sub>o 68% · u 32%</sub> | 1.3 | 0.3 | 2.0 | 28.6 |
| Victor Wembanyama (SAS) | 98% | 32.5<br><sub>34,26,24,25,32</sub> | 28.3<br><sub>52,30,29,40,32</sub> | 28.5 · –<br><sub>o 49% · u 51%</sub> | 12.0<br><sub>24,14,7,11,9</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 3.2<br><sub>2,2,3,3,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,4,3,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 3.8 | 2.8 | 43.5 |
| De'Aaron Fox (SAS) | 100% | 32.0<br><sub>33,26,22,29,31</sub> | 15.3<br><sub>10,9,8,15,17</sub> | 13.5 · – | 4.0<br><sub>3,2,3,9,4</sub> | 3.5 | 6.2<br><sub>4,4,6,6,9</sub> | 5.5 | 1.5<br><sub>0,0,1,2,2</sub> | 1.5 | 1.5 | 0.4 | 2.3 | 25.5 |
| Stephon Castle (SAS) | 98% | 31.6<br><sub>35,28,24,30,29</sub> | 16.1<br><sub>17,19,14,4,11</sub> | 16.5 · –<br><sub>o 46% · u 53%</sub> | 5.4<br><sub>10,3,7,8,1</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>3,7,5,7,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>2,1,2,0,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 2.9 | 27.6 |
| Julian Champagnie (SAS) | 98% | 29.5<br><sub>21,22,21,27,35</sub> | 10.6<br><sub>0,8,14,11,12</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>4,7,4,3,0</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>3,2,0,2,2</sub> |  | 2.1<br><sub>0,2,4,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.5 | 0.9 | 17.1 |
| Keldon Johnson (SAS) | 98% | 26.3<br><sub>19,27,27,26,28</sub> | 10.1<br><sub>4,3,10,4,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>5,6,7,5,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,6,4,3,4</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.2 | 17.7 |
| Luke Kornet (SAS) | 98% | 16.2<br><sub>14,18,15,13,14</sub> | 4.0<br><sub>2,2,6,2,7</sub> |  | 4.7<br><sub>1,6,4,4,5</sub> |  | 1.2<br><sub>2,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 9.9 |
| Harrison Barnes (SAS) | 88% | 16.1<br><sub>13,19,19,21,13</sub> | 5.5<br><sub>4,13,5,11,3</sub> |  | 1.8<br><sub>2,1,3,2,1</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.8<br><sub>1,2,1,2,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.1 |
| Carter Bryant (SAS) | 88% | 14.1<br><sub>-,3,17,14,15</sub> | 4.7<br><sub>-,0,6,8,10</sub> |  | 2.2<br><sub>-,0,4,1,1</sub> |  | 0.9<br><sub>-,0,1,1,2</sub> |  | 0.7<br><sub>-,0,2,2,2</sub> |  | 0.3 | 0.4 | 0.6 | 7.8 |
| Jordan McLaughlin (SAS) | 71% | 11.2<br><sub>-,8,12,11,2</sub> | 3.7<br><sub>-,2,3,4,4</sub> |  | 1.5<br><sub>-,2,0,4,0</sub> |  | 1.6<br><sub>-,1,0,2,0</sub> |  | 0.4<br><sub>-,0,1,0,0</sub> |  | 0.8 | 0.1 | 0.6 | 6.8 |
| Tarris Reed Jr. (SAS) | 76% | 8.0<br><sub>-,3,9,9,2</sub> | 2.8<br><sub>-,0,2,4,0</sub> |  | 3.0<br><sub>-,1,3,3,0</sub> |  | 0.4<br><sub>-,0,1,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.6 | 6.2 |
| Maliq Brown (SAS) | 80% | 7.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 3.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |
| David Jones Garcia (SAS) | 67% | 7.4<br><sub>-,3,-,8,2</sub> | 2.7<br><sub>-,0,-,2,0</sub> |  | 1.2<br><sub>-,0,-,0,0</sub> |  | 1.1<br><sub>-,0,-,0,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.5 | 0.1 | 0.5 | 5.1 |
| Ja'Kobi Gillespie (SAS) | 88% | 6.8<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.5 |

</details>

<details><summary>if Devin Vassell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 96% | 35.1<br><sub>33,32,39,26,37</sub> | 18.4<br><sub>20,9,15,25,22</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>3,6,7,2,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,3,1,4,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>3,2,4,5,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 2.0 | 28.4 |
| Yaxel Lendeborg (GSW) | 98% | 34.5<br><sub>29,30,37,27,36</sub> | 24.3<br><sub>16,17,23,23,25</sub> | 20.5 · –<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>5,8,8,7,10</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>5,6,3,4,0</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>2,1,2,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.6 | 3.2 | 35.2 |
| Draymond Green (GSW) | 93% | 28.7<br><sub>17,27,34,21,27</sub> | 6.7<br><sub>4,2,2,2,7</sub> | 5.5 · –<br><sub>o 52% · u 48%</sub> | 5.1<br><sub>4,5,6,3,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.3<br><sub>2,11,13,6,7</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>0,0,0,0,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.7 | 2.4 | 18.2 |
| De'Anthony Melton (GSW) | 98% | 25.4<br><sub>28,17,17,26,25</sub> | 11.6<br><sub>2,5,4,16,11</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>7,6,1,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.8<br><sub>2,2,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>0,0,1,4,3</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.4 | 1.7 | 18.3 |
| Georges Niang (GSW) | 98% | 21.8<br><sub>22,22,25,19,19</sub> | 9.1<br><sub>13,13,11,9,5</sub> |  | 2.9<br><sub>4,4,2,2,5</sub> |  | 1.3<br><sub>3,3,1,2,0</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 0.4 | 0.2 | 1.0 | 13.3 |
| Will Richard (GSW) | 98% | 20.3<br><sub>28,16,12,-,19</sub> | 5.9<br><sub>6,10,4,-,9</sub> |  | 2.4<br><sub>5,0,2,-,4</sub> |  | 1.2<br><sub>0,2,1,-,0</sub> |  | 0.7<br><sub>2,2,0,-,2</sub> |  | 0.9 | 0.2 | 0.7 | 9.4 |
| Al Horford (GSW) | 98% | 19.9<br><sub>-,18,13,15,21</sub> | 6.6<br><sub>-,8,2,5,2</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>-,5,5,2,1</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>-,1,4,6,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>-,2,0,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.8 | 0.6 | 12.7 |
| Gui Santos (GSW) | 91% | 18.0<br><sub>-,-,12,21,12</sub> | 7.2<br><sub>-,-,3,3,0</sub> |  | 3.4<br><sub>-,-,1,7,3</sub> |  | 1.8<br><sub>-,-,0,4,1</sub> |  | 0.6<br><sub>-,-,0,0,0</sub> |  | 0.6 | 0.2 | 1.2 | 12.3 |
| Gary Payton II (GSW) | 76% | 16.1<br><sub>20,10,13,-,-</sub> | 7.2<br><sub>2,9,4,-,-</sub> |  | 2.8<br><sub>2,0,0,-,-</sub> |  | 1.3<br><sub>1,0,0,-,-</sub> |  | 0.5<br><sub>0,1,0,-,-</sub> |  | 0.9 | 0.2 | 0.8 | 11.2 |
| LJ Cryer (GSW) | 71% | 14.3<br><sub>1,1,-,20,18</sub> | 6.6<br><sub>0,0,-,10,13</sub> |  | 1.4<br><sub>0,0,-,0,1</sub> |  | 1.1<br><sub>0,0,-,3,1</sub> |  | 1.0<br><sub>0,0,-,2,3</sub> |  | 0.3 | 0.1 | 0.7 | 9.1 |
| Charles Bassey (GSW) | 91% | 14.1<br><sub>23,14,11,18,13</sub> | 6.7<br><sub>19,8,8,12,7</sub> |  | 5.3<br><sub>8,7,4,10,6</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 12.7 |
| Graham Ike (GSW) | 91% | 9.7<br><sub>7,1,-,12,4</sub> | 3.9<br><sub>0,0,-,4,4</sub> |  | 2.2<br><sub>0,1,-,5,0</sub> |  | 0.7<br><sub>0,0,-,2,1</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.9 |
| Malevy Leons (GSW) | 58% | 8.8<br><sub>-,1,-,12,4</sub> | 2.7<br><sub>-,0,-,0,0</sub> |  | 1.6<br><sub>-,0,-,3,3</sub> |  | 0.5<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.4 | 0.3 | 0.4 | 4.8 |
| Dylan Harper (SAS) | 98% | 33.9<br><sub>36,28,28,26,36</sub> | 18.6<br><sub>21,19,13,17,18</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>5,2,7,5,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.4<br><sub>0,3,3,4,10</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>1,1,1,0,2</sub> | 0.5<br><sub>o 68% · u 32%</sub> | 1.3 | 0.3 | 2.1 | 29.8 |
| Victor Wembanyama (SAS) | 98% | 32.3<br><sub>34,26,24,25,32</sub> | 28.9<br><sub>52,30,29,40,32</sub> | 28.5 · –<br><sub>o 49% · u 51%</sub> | 11.9<br><sub>24,14,7,11,9</sub> | 11.5<br><sub>o 53% · u 47%</sub> | 3.6<br><sub>2,2,3,3,1</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.1<br><sub>1,4,3,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 3.7 | 2.8 | 44.3 |
| Devin Vassell (SAS) | 100% | 31.9<br><sub>36,27,21,-,-</sub> | 12.8<br><sub>2,19,15,-,-</sub> | 11.5 · – | 4.3<br><sub>7,2,2,-,-</sub> | 3.5 | 3.1<br><sub>4,2,3,-,-</sub> | 2.5 | 2.1<br><sub>0,5,2,-,-</sub> | 1.5 | 1.3 | 0.4 | 1.2 | 20.3 |
| Stephon Castle (SAS) | 98% | 31.6<br><sub>35,28,24,30,29</sub> | 16.7<br><sub>17,19,14,4,11</sub> | 16.5 · –<br><sub>o 46% · u 53%</sub> | 5.4<br><sub>10,3,7,8,1</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>3,7,5,7,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,1,2,0,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 3.0 | 28.7 |
| Julian Champagnie (SAS) | 98% | 29.5<br><sub>21,22,21,27,35</sub> | 10.6<br><sub>0,8,14,11,12</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>4,7,4,3,0</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>3,2,0,2,2</sub> |  | 2.1<br><sub>0,2,4,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 0.9 | 17.1 |
| Keldon Johnson (SAS) | 98% | 26.3<br><sub>19,27,27,26,28</sub> | 10.4<br><sub>4,3,10,4,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>5,6,7,5,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>2,6,4,3,4</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.2 | 18.2 |
| Harrison Barnes (SAS) | 88% | 16.2<br><sub>13,19,19,21,13</sub> | 5.5<br><sub>4,13,5,11,3</sub> |  | 1.9<br><sub>2,1,3,2,1</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 0.8<br><sub>1,2,1,2,1</sub> |  | 0.4 | 0.1 | 0.5 | 8.2 |
| Luke Kornet (SAS) | 98% | 16.2<br><sub>14,18,15,13,14</sub> | 4.0<br><sub>2,2,6,2,7</sub> |  | 4.8<br><sub>1,6,4,4,5</sub> |  | 1.2<br><sub>2,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.6 | 10.0 |
| Carter Bryant (SAS) | 88% | 14.2<br><sub>-,3,17,14,15</sub> | 4.9<br><sub>-,0,6,8,10</sub> |  | 2.2<br><sub>-,0,4,1,1</sub> |  | 1.0<br><sub>-,0,1,1,2</sub> |  | 0.7<br><sub>-,0,2,2,2</sub> |  | 0.3 | 0.4 | 0.6 | 8.1 |
| Jordan McLaughlin (SAS) | 71% | 11.1<br><sub>-,8,12,11,2</sub> | 3.7<br><sub>-,2,3,4,4</sub> |  | 1.5<br><sub>-,2,0,4,0</sub> |  | 1.7<br><sub>-,1,0,2,0</sub> |  | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.8 | 0.1 | 0.5 | 6.9 |
| Tarris Reed Jr. (SAS) | 76% | 8.0<br><sub>-,3,9,9,2</sub> | 2.8<br><sub>-,0,2,4,0</sub> |  | 2.9<br><sub>-,1,3,3,0</sub> |  | 0.4<br><sub>-,0,1,1,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.6 | 6.1 |
| Maliq Brown (SAS) | 80% | 7.7<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |
| David Jones Garcia (SAS) | 67% | 7.2<br><sub>-,3,-,8,2</sub> | 2.7<br><sub>-,0,-,2,0</sub> |  | 1.2<br><sub>-,0,-,0,0</sub> |  | 1.2<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.5 | 0.1 | 0.5 | 5.1 |
| Ja'Kobi Gillespie (SAS) | 88% | 6.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.5 |

</details>


### POR @ SAC
Out: Precious Achiuwa (SAC), Alex Karaban (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR)

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 33.6<br><sub>35,39,24,34,35</sub> | 25.3<br><sub>21,22,15,24,28</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>7,9,4,6,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>12,11,1,8,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,1,2,2,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.5 | 3.5 | 38.9 |
| Toumani Camara | 98% | 31.2<br><sub>32,30,21,30,38</sub> | 13.2<br><sub>11,18,4,12,14</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>4,6,4,3,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,1,0,3,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,4,0,2,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.4 | 1.3 | 19.7 |
| Damian Lillard | 98% | 30.5<br><sub>33,37,20,24,32</sub> | 19.9<br><sub>25,22,12,25,18</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>3,0,0,3,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.6<br><sub>5,4,7,3,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 2.9<br><sub>2,4,2,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.2 | 2.2 | 29.0 |
| Jrue Holiday | 98% | 28.5<br><sub>28,31,20,25,30</sub> | 14.7<br><sub>15,12,11,11,19</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,1,0,1,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>0,7,0,2,5</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>5,3,1,2,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.2 | 1.9 | 23.9 |
| Donovan Clingan | 98% | 26.7<br><sub>29,28,22,26,30</sub> | 11.7<br><sub>24,17,6,7,5</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 10.9<br><sub>11,11,5,13,12</sub> | 11.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,1,0,3,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9<br><sub>1,3,0,1,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.6 | 1.9 | 1.3 | 24.6 |
| Sidy Cissoko | 98% | 25.4<br><sub>21,22,16,33,29</sub> | 8.5<br><sub>7,7,4,17,19</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>4,2,3,3,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>4,3,1,3,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>1,2,0,3,4</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.4 | 1.1 | 14.2 |
| Scoot Henderson | 98% | 24.8<br><sub>22,23,24,23,19</sub> | 12.1<br><sub>9,2,13,11,5</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 3.2<br><sub>1,0,1,4,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>1,0,0,3,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.2 | 2.1 | 17.6 |
| Robert Williams III | 98% | 17.9<br><sub>16,16,-,15,17</sub> | 7.4<br><sub>9,9,-,6,10</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>8,5,-,4,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,2,-,0,0</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.2 | 0.9 | 15.4 |
| Jayson Kent | 52% | 11.1<br><sub>-,-,12,-,-</sub> | 4.0<br><sub>-,-,4,-,-</sub> |  | 1.6<br><sub>-,-,1,-,-</sub> |  | 0.7<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 6.3 |
| Branden Carlson | 67% | 11.0<br><sub>3,-,12,8,10</sub> | 3.0<br><sub>2,-,4,2,0</sub> |  | 2.6<br><sub>0,-,2,5,2</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 6.0 |
| Micah Potter | 58% | 9.2<br><sub>2,-,14,5,-</sub> | 3.8<br><sub>4,-,7,0,-</sub> |  | 2.5<br><sub>1,-,3,3,-</sub> |  | 0.6<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>1,-,1,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.8 |
| Yang Hansen | 64% | 9.0<br><sub>2,3,26,5,-</sub> | 3.3<br><sub>0,2,12,0,-</sub> |  | 2.4<br><sub>0,0,10,1,-</sub> |  | 0.5<br><sub>0,0,1,0,-</sub> |  | 0.2<br><sub>0,0,1,0,-</sub> |  | 0.2 | 0.2 | 0.8 | 6.2 |
| John Tonje | 38% | 6.9<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 37.8<br><sub>37,42,33,39,40</sub> | 26.1<br><sub>25,22,22,32,29</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,3,3,5,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 7.5<br><sub>6,12,8,10,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,3,3,3,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 3.7 | 37.4 |
| Domantas Sabonis | 98% | 33.2<br><sub>31,35,31,-,24</sub> | 15.2<br><sub>9,16,17,-,0</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 12.2<br><sub>7,17,12,-,2</sub> | 11.5<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>4,1,5,-,5</sub> | 6.5<br><sub>o 42% · u 58%</sub> | 0.3<br><sub>0,0,1,-,0</sub> |  | 0.9 | 0.4 | 2.8 | 33.3 |
| De'Andre Hunter | 98% | 33.2<br><sub>36,38,-,31,34</sub> | 14.0<br><sub>6,14,-,14,15</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>7,2,-,3,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>2,2,-,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>0,1,-,2,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.9 | 20.5 |
| Zach LaVine | 98% | 33.1<br><sub>28,35,35,25,33</sub> | 19.3<br><sub>23,21,14,15,31</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>4,4,4,4,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>1,1,3,2,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>5,3,1,1,6</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.0 | 0.3 | 2.7 | 24.9 |
| Keegan Murray | 98% | 28.6<br><sub>-,-,-,23,24</sub> | 11.5<br><sub>-,-,-,10,11</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>-,-,-,1,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>-,-,-,2,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.2<br><sub>-,-,-,0,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 1.1 | 1.1 | 17.3 |
| Leaky Black | 76% | 21.8<br><sub>25,22,40,20,18</sub> | 5.2<br><sub>12,3,12,6,0</sub> |  | 3.4<br><sub>3,6,3,5,3</sub> |  | 1.4<br><sub>1,1,5,1,2</sub> |  | 0.7<br><sub>4,0,4,2,0</sub> |  | 1.1 | 0.5 | 0.7 | 10.1 |
| Dylan Cardwell | 98% | 20.7<br><sub>-,13,15,18,29</sub> | 6.4<br><sub>-,4,9,4,1</sub> |  | 7.4<br><sub>-,6,2,9,11</sub> |  | 1.6<br><sub>-,0,3,3,1</sub> |  | 0.1<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.4 | 1.1 | 15.4 |
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
| Jared McCain | 98% | 30.4<br><sub>25,29,23,31,31</sub> | 16.4<br><sub>9,21,19,21,10</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>1,5,5,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>0,0,2,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.5<br><sub>1,3,2,4,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 2.1 | 22.4 |
| Isaiah Hartenstein | 98% | 28.5<br><sub>26,26,18,24,34</sub> | 10.7<br><sub>3,2,2,7,20</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 10.6<br><sub>12,6,14,9,11</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>4,7,6,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.7 | 1.9 | 25.4 |
| Aday Mara | 98% | 28.3<br><sub>25,18,27,26,32</sub> | 11.1<br><sub>9,9,18,10,11</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>5,7,8,10,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>2,0,3,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.4 | 1.6 | 1.8 | 21.0 |
| Alex Caruso | 98% | 25.9<br><sub>20,20,13,19,29</sub> | 10.3<br><sub>7,5,0,5,14</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>4,6,3,2,7</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.6 | 0.4 | 1.2 | 17.4 |
| Kenrich Williams | 98% | 25.7<br><sub>29,19,23,19,26</sub> | 10.0<br><sub>13,4,9,3,11</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>4,6,4,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,1,1,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.2 | 1.1 | 17.1 |
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
| Darius Garland | 98% | 30.8<br><sub>33,36,39,32,25</sub> | 18.1<br><sub>15,16,26,24,13</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>0,4,1,0,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>7,8,7,10,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,1,4,3,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 3.3 | 26.9 |
| Rui Hachimura | 98% | 27.9<br><sub>30,-,37,26,23</sub> | 14.1<br><sub>24,-,21,14,13</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>7,-,9,3,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,-,7,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 2.0<br><sub>4,-,1,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.3 | 1.4 | 20.0 |
| Derrick Jones Jr. | 98% | 26.9<br><sub>28,-,37,29,24</sub> | 10.2<br><sub>9,-,12,8,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>7,-,8,4,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>1,-,1,3,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4<br><sub>1,-,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.7 | 1.1 | 15.5 |
| Kris Dunn | 98% | 25.2<br><sub>27,30,35,24,19</sub> | 7.5<br><sub>12,12,5,14,3</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>2,4,5,5,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>4,1,3,4,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>0,1,1,2,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.3 | 1.4 | 14.3 |
| Brook Lopez | 98% | 22.5<br><sub>19,22,35,26,19</sub> | 10.9<br><sub>7,12,20,20,8</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>2,6,8,7,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 1.0 | 1.1 | 16.5 |
| Kobe Sanders | 98% | 22.0<br><sub>30,38,18,22,26</sub> | 9.3<br><sub>16,26,4,8,9</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>0,3,1,4,7</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>4,5,0,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 1.4 | 13.9 |
| Max Strus | 98% | 21.1<br><sub>-,23,23,19,22</sub> | 8.5<br><sub>-,11,9,7,12</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,4,5,4,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>-,6,5,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>-,3,3,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.2 | 1.0 | 14.7 |
| Keaton Wagler | 98% | 20.9<br><sub>19,24,16,18,23</sub> | 9.4<br><sub>7,6,11,15,11</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,4,2,2,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.1<br><sub>4,4,1,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,0,3,3,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.2 | 1.8 | 15.5 |
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
| Darius Garland (LAC) | 98% | 30.8<br><sub>33,36,39,32,25</sub> | 18.2<br><sub>15,16,26,24,13</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>0,4,1,0,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>7,8,7,10,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,1,4,3,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 3.3 | 27.0 |
| Rui Hachimura (LAC) | 98% | 27.9<br><sub>30,-,37,26,23</sub> | 14.2<br><sub>24,-,21,14,13</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>7,-,9,3,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>0,-,7,2,1</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 2.0<br><sub>4,-,1,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.3 | 1.4 | 20.1 |
| Derrick Jones Jr. (LAC) | 98% | 26.8<br><sub>28,-,37,29,24</sub> | 10.2<br><sub>9,-,12,8,11</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>7,-,8,4,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>1,-,1,3,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4<br><sub>1,-,2,0,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.7 | 1.1 | 15.6 |
| Kris Dunn (LAC) | 98% | 25.2<br><sub>27,30,35,24,19</sub> | 7.5<br><sub>12,12,5,14,3</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>2,4,5,5,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>4,1,3,4,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 0.9<br><sub>0,1,1,2,1</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.4 | 0.3 | 1.4 | 14.3 |
| Brook Lopez (LAC) | 98% | 22.5<br><sub>19,22,35,26,19</sub> | 10.9<br><sub>7,12,20,20,8</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>2,6,8,7,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.2<br><sub>0,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3<br><sub>1,1,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.5 | 0.9 | 1.1 | 16.5 |
| Kobe Sanders (LAC) | 98% | 22.0<br><sub>30,38,18,22,26</sub> | 9.3<br><sub>16,26,4,8,9</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>3,4,2,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>0,3,1,4,7</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>4,5,0,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 1.4 | 13.8 |
| Max Strus (LAC) | 98% | 21.1<br><sub>-,23,23,19,22</sub> | 8.6<br><sub>-,11,9,7,12</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>-,4,5,4,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>-,6,5,2,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>-,3,3,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.5 | 0.2 | 1.0 | 14.8 |
| Keaton Wagler (LAC) | 98% | 20.9<br><sub>19,24,16,18,23</sub> | 9.6<br><sub>7,6,11,15,11</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,4,2,2,0</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>4,4,1,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.2<br><sub>0,0,3,3,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.2 | 1.8 | 15.6 |
| Isaiah Jackson (LAC) | 98% | 17.1<br><sub>22,26,13,-,16</sub> | 7.0<br><sub>5,19,2,-,4</sub> |  | 5.2<br><sub>8,8,4,-,4</sub> |  | 1.3<br><sub>2,2,2,-,0</sub> |  | 0.0<br><sub>0,1,0,-,0</sub> |  | 0.8 | 0.7 | 1.3 | 13.4 |
| Gradey Dick (LAC) | 96% | 14.7<br><sub>3,29,7,17,19</sub> | 6.7<br><sub>0,12,4,15,10</sub> |  | 2.3<br><sub>1,4,2,4,3</sub> |  | 0.7<br><sub>0,3,1,0,2</sub> |  | 0.7<br><sub>0,0,0,2,1</sub> |  | 0.5 | 0.1 | 0.8 | 9.8 |
| Baba Miller (LAC) | 93% | 14.3<br><sub>6,12,6,20,16</sub> | 6.3<br><sub>2,4,2,12,13</sub> |  | 2.4<br><sub>2,0,1,5,4</sub> |  | 1.5<br><sub>1,1,1,4,0</sub> |  | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.3 | 0.9 | 10.2 |
| Jalen Pickett (LAC) | 58% | 7.5<br><sub>6,-,-,2,8</sub> | 2.8<br><sub>0,-,-,0,3</sub> |  | 1.0<br><sub>2,-,-,0,1</sub> |  | 1.1<br><sub>3,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,1</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Blake Wesley (LAC) | 52% | 6.1<br><sub>4,-,-,-,-</sub> | 2.6<br><sub>2,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.8<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Cam Christie (LAC) | 58% | 6.0<br><sub>6,-,-,2,-</sub> | 2.3<br><sub>3,-,-,0,-</sub> |  | 1.0<br><sub>1,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Shai Gilgeous-Alexander (OKC) | 98% | 33.5<br><sub>35,30,29,29,36</sub> | 29.5<br><sub>42,28,30,26,31</sub> | 31.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>4,3,2,8,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.5<br><sub>8,4,9,3,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>5,3,3,0,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.7 | 2.9 | 40.0 |
| Jared McCain (OKC) | 98% | 27.8<br><sub>25,29,23,31,31</sub> | 14.5<br><sub>9,21,19,21,10</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>1,5,5,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,0,2,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.2<br><sub>1,3,2,4,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.6 | 19.8 |
| Ajay Mitchell (OKC) | 100% | 27.8<br><sub>32,30,22,28,-</sub> | 16.5<br><sub>23,35,12,14,-</sub> | 18.5 · – | 3.4<br><sub>7,1,4,3,-</sub> | 3.5 | 3.7<br><sub>4,5,0,3,-</sub> | 3.5 | 1.0<br><sub>1,4,0,0,-</sub> | 1.5 | 1.3 | 0.2 | 1.8 | 23.7 |
| Isaiah Hartenstein (OKC) | 98% | 26.3<br><sub>26,26,18,24,34</sub> | 9.6<br><sub>3,2,2,7,20</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.8<br><sub>12,6,14,9,11</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,7,6,5,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.6 | 23.2 |
| Aday Mara (OKC) | 98% | 25.2<br><sub>25,18,27,26,32</sub> | 9.6<br><sub>9,9,18,10,11</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>5,7,8,10,6</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>2,0,3,2,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 0.5 | 1.5 | 1.6 | 18.3 |
| Alex Caruso (OKC) | 98% | 22.5<br><sub>20,20,13,19,29</sub> | 8.4<br><sub>7,5,0,5,14</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,6,3,2,7</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,2,3,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>1,1,0,1,4</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.4 | 1.0 | 14.4 |
| Kenrich Williams (OKC) | 98% | 22.3<br><sub>29,19,23,19,26</sub> | 8.3<br><sub>13,4,9,3,11</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>4,6,4,2,2</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>3,1,1,1,2</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.1 | 0.9 | 14.3 |
| Bennett Stirtz (OKC) | 98% | 21.5<br><sub>22,24,29,18,25</sub> | 8.0<br><sub>16,12,11,13,6</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>1,1,5,1,1</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 1.3<br><sub>4,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.2 | 0.9 | 11.0 |
| Micah Peavy (OKC) | 88% | 15.8<br><sub>26,18,23,21,12</sub> | 4.0<br><sub>2,7,7,0,0</sub> |  | 2.6<br><sub>9,4,3,2,3</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 0.4<br><sub>0,1,1,0,0</sub> |  | 0.6 | 0.2 | 0.4 | 7.2 |
| Nique Clifford (OKC) | 93% | 14.6<br><sub>-,-,-,20,16</sub> | 5.0<br><sub>-,-,-,4,5</sub> |  | 2.2<br><sub>-,-,-,4,3</sub> |  | 1.4<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.6 | 0.2 | 0.9 | 8.6 |
| Josh Dix (OKC) | 63% | 13.3<br><sub>-,15,21,-,-</sub> | 3.4<br><sub>-,5,2,-,-</sub> |  | 1.2<br><sub>-,2,1,-,-</sub> |  | 0.7<br><sub>-,1,2,-,-</sub> |  | 0.3<br><sub>-,1,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.2 |
| Brooks Barnhizer (OKC) | 63% | 7.8<br><sub>-,5,8,5,-</sub> | 1.9<br><sub>-,0,2,0,-</sub> |  | 1.6<br><sub>-,0,4,1,-</sub> |  | 0.6<br><sub>-,0,3,1,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Nikola Topic (OKC) | 63% | 6.2 | 2.0 |  | 0.7 |  | 1.5 |  | 0.1 |  | 0.3 | 0.0 | 0.7 | 4.2 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-13/`._
