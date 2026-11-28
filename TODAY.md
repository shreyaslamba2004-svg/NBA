# NBA model · Sat 28 Nov 2026 (US date)

Updated **Sun 29 Nov, 12:24 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-28/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner PTS over 44.5 (45+) | ORL @ WAS | draftkings | 30.00 | 25.19 | 12.75 | 7.8% | 3.1% | 4.0% | +19.1% | +135.2% | 0.2% |
| Kevin Durant PRA over 49.5 (50+) | PHI @ HOU | draftkings | 22.00 | 19.19 | 10.45 | 9.6% | 4.2% | 5.2% | +14.6% | +110.4% | 0.2% |
| Josh Giddey PRA over 44.5 (45+) | IND @ CHI | draftkings | 15.60 | 13.66 | 7.50 | 13.3% | 6.0% | 7.3% | +14.2% | +107.9% | 0.2% |
| Dominick Barlow REB over 9.5 (10+) | PHI @ HOU | draftkings | 17.40 | 15.53 | 8.88 | 11.3% | 5.4% | 6.4% | +12.0% | +96.0% | 0.2% |
| Alex Sarr AST over 3.5 (4+) | ORL @ WAS | draftkings | 11.60 | 10.41 | 6.00 | 16.7% | 8.1% | 9.6% | +11.5% | +93.2% | 0.3% |
| Kevin Durant PRA over 44.5 (45+) | PHI @ HOU | draftkings | 10.90 | 9.83 | 5.76 | 17.4% | 8.6% | 10.2% | +10.8% | +89.4% | 0.3% |
| Dominick Barlow REB over 7.5 (8+) | PHI @ HOU | draftkings | 7.30 | 6.59 | 3.86 | 25.9% | 12.8% | 15.2% | +10.8% | +89.1% | 0.4% |
| Josh Giddey AST over 15.5 (16+) | IND @ CHI | draftkings | 20.40 | 18.45 | 10.87 | 9.2% | 4.6% | 5.4% | +10.5% | +87.7% | 0.1% |
| Tyrese Maxey PR over 49.5 (50+) | PHI @ HOU | draftkings | 20.20 | 18.45 | 11.08 | 9.0% | 4.6% | 5.4% | +9.6% | +82.4% | 0.1% |
| Josh Giddey PRA over 39.5 (40+) | IND @ CHI | draftkings | 7.10 | 6.54 | 4.00 | 25.0% | 13.2% | 15.3% | +8.7% | +77.5% | 0.4% |
| Josh Giddey AST over 13.5 (14+) | IND @ CHI | draftkings | 9.10 | 8.55 | 5.50 | 18.2% | 10.3% | 11.7% | +6.5% | +65.3% | 0.2% |
| Wendell Carter Jr. PR over 34.5 (35+) | ORL @ WAS | draftkings | 20.80 | 19.65 | 12.83 | 7.8% | 4.5% | 5.1% | +5.9% | +62.1% | 0.1% |
| Tyrese Maxey PR over 44.5 (45+) | PHI @ HOU | draftkings | 10.30 | 9.74 | 6.37 | 15.7% | 9.1% | 10.3% | +5.8% | +61.7% | 0.2% |
| Kevin Durant AST over 7.5 (8+) | PHI @ HOU | draftkings | 15.00 | 14.18 | 9.31 | 10.7% | 6.2% | 7.0% | +5.7% | +61.1% | 0.1% |
| Anthony Davis BLK over 2.5 (3+) | ORL @ WAS | draftkings | 6.17 | 5.85 | 3.86 | 25.9% | 15.2% | 17.1% | +5.5% | +59.9% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ORL @ WAS | Sun 29 Nov 09:00 | 115.5–113.2 | ORL 56% | 1.77 / 2.30 | WAS +2.5 | 228.5 | WAS +3.5 covers 53%; o220.5 67% |
| BKN @ CHA | Sun 29 Nov 10:00 | 102.3–110.9 | BKN 27% | 3.70 / 1.37 | CHA -8.5 | 213.5 | CHA -5.5 covers 59%; o213.5 49% |
| IND @ CHI | Sun 29 Nov 12:00 | 116.1–119.8 | IND 40% | 2.51 / 1.66 | CHI -3.5 | 235.5 | CHI -3.5 covers 51%; o234.5 53% |
| OKC @ MIL | Sun 29 Nov 12:00 | 119.2–110.2 | OKC 74% | 1.35 / 3.83 | MIL +9.5 | 229.5 | MIL +11.5 covers 57%; o228.5 52% |
| PHI @ HOU | Sun 29 Nov 12:30 | 106.9–118.4 | PHI 21% | 4.75 / 1.27 | HOU -11.5 | 225.5 | HOU -12.5 covers 47%; o219.5 62% |

### ORL @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Paolo Banchero (ORL), Colin Castleton (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Kevin Porter Jr. (ORL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.5–113.2 | ORL 56% | 1.77 / 2.30 | WAS +2.5 | 228.5 | WAS +3.5 covers 53%; o220.5 67% |
| Expected (weighted by chance each plays) | 116.0–112.9 | ORL 59% | 1.70 / 2.42 | WAS +3.5 | 228.5 | WAS +3.5 covers 50%; o220.5 67% |
| if Anthony Black plays | 116.2–112.6 | ORL 60% | 1.66 / 2.51 | WAS +3.5 | 228.5 | WAS +3.5 covers 49%; o220.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Black (ORL) | Questionable | 55% | 32.4 | 15.1 | 4.4 | 4.5 | 1.6 | 1.8 | 0.7 | 2.3 | 23.9 | full tables below |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 99% | 36.9<br><sub>38,36,36,32,38</sub> | 29.1<br><sub>21,27,35,16,20</sub> | 24.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>8,8,5,8,9</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 7.7<br><sub>9,11,7,6,6</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.5<br><sub>0,1,2,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.4 | 2.8 | 43.8 |
| Desmond Bane | 99% | 36.6<br><sub>39,38,31,33,34</sub> | 22.6<br><sub>24,15,21,17,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>8,3,2,1,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.1<br><sub>5,3,3,5,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>3,5,7,3,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.4 | 2.0 | 31.4 |
| Wendell Carter Jr. | 99% | 34.3<br><sub>28,32,35,26,38</sub> | 14.4<br><sub>10,15,8,9,9</sub> | 10.5 · –<br><sub>o 55% · u 45%</sub> | 9.4<br><sub>3,8,8,6,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>1,3,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>1,2,0,1,1</sub> |  | 1.0 | 0.9 | 1.6 | 26.1 |
| Jalen Suggs | 98% | 32.4<br><sub>25,31,30,22,33</sub> | 13.7<br><sub>12,18,8,9,4</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,8,6,4,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 5.2<br><sub>4,4,2,2,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>2,5,2,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.9 | 0.6 | 2.6 | 23.6 |
| Tristan da Silva | 91% | 30.8<br><sub>31,27,24,27,33</sub> | 14.2<br><sub>13,12,6,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>6,2,1,3,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>3,0,2,0,1</sub> |  | 2.4<br><sub>3,2,2,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 1.1 | 20.5 |
| Jevon Carter | 91% | 18.9<br><sub>12,16,10,14,19</sub> | 6.8<br><sub>3,6,3,3,9</sub> |  | 1.8<br><sub>2,2,0,2,0</sub> |  | 2.0<br><sub>1,3,0,2,0</sub> |  | 1.1<br><sub>1,2,1,1,3</sub> |  | 0.9 | 0.2 | 0.6 | 10.6 |
| Goga Bitadze | 96% | 17.1<br><sub>20,20,15,15,13</sub> | 6.2<br><sub>10,8,4,1,2</sub> |  | 6.0<br><sub>6,3,4,4,8</sub> |  | 1.3<br><sub>1,1,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.8 | 13.5 |
| Jase Richardson | 63% | 17.0<br><sub>-,-,-,6,1</sub> | 5.9<br><sub>-,-,-,2,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 9.7 |
| Nikola Vucevic | 63% | 14.8<br><sub>-,-,23,17,-</sub> | 6.1<br><sub>-,-,15,5,-</sub> |  | 4.3<br><sub>-,-,8,3,-</sub> |  | 1.6<br><sub>-,-,1,3,-</sub> |  | 0.6<br><sub>-,-,3,1,-</sub> |  | 0.3 | 0.4 | 0.6 | 12.0 |
| Jamal Cain | 80% | 13.4<br><sub>15,4,-,9,1</sub> | 5.1<br><sub>2,0,-,2,0</sub> |  | 2.6<br><sub>5,1,-,1,0</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.5<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.4 |
| Alex Morales | 58% | 12.9<br><sub>-,-,-,5,1</sub> | 3.0<br><sub>-,-,-,0,0</sub> |  | 2.3<br><sub>-,-,-,1,0</sub> |  | 1.1<br><sub>-,-,-,2,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.4 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 36.3<br><sub>32,38,37,33,41</sub> | 17.8<br><sub>21,23,20,16,20</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>5,12,10,8,11</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,2,6,6,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>1,0,2,0,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.4 | 2.3 | 29.0 |
| Anthony Davis | 99% | 35.3<br><sub>35,34,34,33,37</sub> | 24.0<br><sub>23,25,36,22,33</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 11.0<br><sub>4,14,11,7,13</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>0,2,3,1,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.9<br><sub>0,2,0,2,1</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.3 | 1.8 | 2.3 | 37.9 |
| Kyshawn George | 99% | 35.2<br><sub>38,40,35,36,38</sub> | 17.6<br><sub>18,20,11,24,24</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>6,2,7,3,9</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>1,4,5,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>2,4,1,6,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 1.1 | 2.3 | 26.9 |
| Trae Young | 99% | 34.4<br><sub>33,32,35,28,35</sub> | 17.4<br><sub>13,11,16,11,17</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,1,2,4,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 9.3<br><sub>12,8,5,11,12</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,1,4,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.1 | 29.3 |
| Alex Sarr | 98% | 26.0<br><sub>31,22,20,26,24</sub> | 10.8<br><sub>6,13,3,10,7</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 6.4<br><sub>4,2,3,9,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,3,0,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,3,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 1.7 | 1.3 | 19.2 |
| Bilal Coulibaly | 99% | 23.6<br><sub>16,26,24,25,22</sub> | 8.0<br><sub>11,3,2,12,10</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>5,8,5,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>0,2,0,1,1</sub> |  | 0.8<br><sub>1,0,0,4,2</sub> |  | 1.1 | 0.9 | 1.1 | 13.4 |
| Khris Middleton | 76% | 17.0<br><sub>18,20,28,20,18</sub> | 5.5<br><sub>9,8,5,6,0</sub> |  | 2.5<br><sub>3,4,2,2,5</sub> |  | 1.5<br><sub>3,1,3,2,0</sub> |  | 0.6<br><sub>2,1,0,2,0</sub> |  | 0.5 | 0.1 | 1.1 | 9.5 |
| Tre Johnson | 97% | 13.4<br><sub>21,8,4,15,8</sub> | 5.2<br><sub>9,0,2,11,0</sub> |  | 1.4<br><sub>1,2,1,2,1</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.6<br><sub>2,0,0,3,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.3 |
| Bub Carrington | 88% | 11.6<br><sub>2,-,6,3,7</sub> | 3.6<br><sub>0,-,3,0,0</sub> |  | 1.3<br><sub>0,-,0,0,2</sub> |  | 1.5<br><sub>0,-,0,0,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.3 |
| Deandre Ayton | 99% | 9.9<br><sub>8,9,11,5,5</sub> | 3.0<br><sub>4,0,0,0,0</sub> |  | 3.2<br><sub>0,3,4,2,2</sub> |  | 0.5<br><sub>1,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.4 | 6.7 |
| Will Riley | 91% | 8.4<br><sub>2,10,6,9,5</sub> | 3.7<br><sub>2,0,0,4,5</sub> |  | 1.1<br><sub>1,3,1,3,0</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Anthony Gill | 52% | 7.2<br><sub>2,-,-,3,-</sub> | 2.7<br><sub>2,-,-,0,-</sub> |  | 1.2<br><sub>0,-,-,2,-</sub> |  | 0.5<br><sub>0,-,-,1,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.3 |
| Tre Mann | 63% | 6.0<br><sub>2,-,-,3,1</sub> | 2.7<br><sub>2,-,-,0,0</sub> |  | 0.8<br><sub>0,-,-,0,0</sub> |  | 0.8<br><sub>1,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |

</details>

<details><summary>if Anthony Black plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner (ORL) | 99% | 35.0<br><sub>38,36,36,32,38</sub> | 26.8<br><sub>21,27,35,16,20</sub> | 24.5 · –<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>8,8,5,8,9</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 7.0<br><sub>9,11,7,6,6</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,1,2,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.4 | 2.6 | 40.3 |
| Desmond Bane (ORL) | 99% | 33.6<br><sub>39,38,31,33,34</sub> | 20.0<br><sub>24,15,21,17,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>8,3,2,1,1</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.5<br><sub>5,3,3,5,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,5,7,3,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 1.7 | 27.8 |
| Anthony Black (ORL) | 100% | 32.4<br><sub>33,37,37,35,28</sub> | 15.1<br><sub>20,15,13,14,5</sub> | 14.5 · – | 4.4<br><sub>2,2,7,5,4</sub> | 4.5 | 4.5<br><sub>7,6,6,2,2</sub> | 4.5 | 1.6<br><sub>3,2,2,2,0</sub> | 1.5 | 1.8 | 0.7 | 2.3 | 23.9 |
| Wendell Carter Jr. (ORL) | 99% | 31.5<br><sub>28,32,35,26,38</sub> | 13.1<br><sub>10,15,8,9,9</sub> | 10.5 · –<br><sub>o 55% · u 45%</sub> | 8.8<br><sub>3,8,8,6,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,3,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>1,2,0,1,1</sub> |  | 0.9 | 0.9 | 1.5 | 23.8 |
| Jalen Suggs (ORL) | 98% | 28.7<br><sub>25,31,30,22,33</sub> | 11.6<br><sub>12,18,8,9,4</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>6,8,6,4,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>4,4,2,2,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,5,2,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.7 | 0.6 | 2.2 | 20.3 |
| Tristan da Silva (ORL) | 91% | 27.4<br><sub>31,27,24,27,33</sub> | 12.5<br><sub>13,12,6,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>6,2,1,3,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>3,0,2,0,1</sub> |  | 2.1<br><sub>3,2,2,4,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 1.0 | 18.1 |
| Goga Bitadze (ORL) | 96% | 14.5<br><sub>20,20,15,15,13</sub> | 5.5<br><sub>10,8,4,1,2</sub> |  | 5.1<br><sub>6,3,4,4,8</sub> |  | 1.1<br><sub>1,1,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.0 | 0.7 | 11.7 |
| Jevon Carter (ORL) | 91% | 14.5<br><sub>12,16,10,14,19</sub> | 5.3<br><sub>3,6,3,3,9</sub> |  | 1.4<br><sub>2,2,0,2,0</sub> |  | 1.5<br><sub>1,3,0,2,0</sub> |  | 0.8<br><sub>1,2,1,1,3</sub> |  | 0.7 | 0.2 | 0.4 | 8.3 |
| Nikola Vucevic (ORL) | 63% | 11.3<br><sub>-,-,23,17,-</sub> | 4.9<br><sub>-,-,15,5,-</sub> |  | 3.4<br><sub>-,-,8,3,-</sub> |  | 1.3<br><sub>-,-,1,3,-</sub> |  | 0.5<br><sub>-,-,3,1,-</sub> |  | 0.2 | 0.3 | 0.5 | 9.6 |
| Jase Richardson (ORL) | 63% | 11.1<br><sub>-,-,-,6,1</sub> | 3.8<br><sub>-,-,-,2,0</sub> |  | 1.3<br><sub>-,-,-,1,0</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |
| Jamal Cain (ORL) | 80% | 8.8<br><sub>15,4,-,9,1</sub> | 3.4<br><sub>2,0,-,2,0</sub> |  | 1.7<br><sub>5,1,-,1,0</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.6 |
| Alex Morales (ORL) | 58% | 8.1<br><sub>-,-,-,5,1</sub> | 2.0<br><sub>-,-,-,0,0</sub> |  | 1.5<br><sub>-,-,-,1,0</sub> |  | 0.7<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| AJ Dybantsa (WAS) | 98% | 36.2<br><sub>32,38,37,33,41</sub> | 17.7<br><sub>21,23,20,16,20</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 7.6<br><sub>5,12,10,8,11</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>3,2,6,6,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>1,0,2,0,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.4 | 2.3 | 28.9 |
| Anthony Davis (WAS) | 99% | 35.3<br><sub>35,34,34,33,37</sub> | 24.0<br><sub>23,25,36,22,33</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 11.0<br><sub>4,14,11,7,13</sub> | 10.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>0,2,3,1,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 0.9<br><sub>0,2,0,2,1</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.3 | 1.8 | 2.2 | 37.9 |
| Kyshawn George (WAS) | 99% | 35.2<br><sub>38,40,35,36,38</sub> | 17.6<br><sub>18,20,11,24,24</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>6,2,7,3,9</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>1,4,5,4,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.7<br><sub>2,4,1,6,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 1.1 | 2.3 | 26.8 |
| Trae Young (WAS) | 99% | 34.4<br><sub>33,32,35,28,35</sub> | 17.4<br><sub>13,11,16,11,17</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 2.7<br><sub>2,1,2,4,0</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 9.3<br><sub>12,8,5,11,12</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,1,4,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.1 | 29.3 |
| Alex Sarr (WAS) | 98% | 26.0<br><sub>31,22,20,26,24</sub> | 10.8<br><sub>6,13,3,10,7</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>4,2,3,9,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,3,0,2,0</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,3,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 1.7 | 1.3 | 19.2 |
| Bilal Coulibaly (WAS) | 99% | 23.6<br><sub>16,26,24,25,22</sub> | 7.9<br><sub>11,3,2,12,10</sub> | 7.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>5,8,5,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>0,2,0,1,1</sub> |  | 0.8<br><sub>1,0,0,4,2</sub> |  | 1.1 | 0.9 | 1.1 | 13.3 |
| Khris Middleton (WAS) | 76% | 16.9<br><sub>18,20,28,20,18</sub> | 5.4<br><sub>9,8,5,6,0</sub> |  | 2.5<br><sub>3,4,2,2,5</sub> |  | 1.5<br><sub>3,1,3,2,0</sub> |  | 0.6<br><sub>2,1,0,2,0</sub> |  | 0.5 | 0.1 | 1.1 | 9.4 |
| Tre Johnson (WAS) | 97% | 13.4<br><sub>21,8,4,15,8</sub> | 5.2<br><sub>9,0,2,11,0</sub> |  | 1.4<br><sub>1,2,1,2,1</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.6<br><sub>2,0,0,3,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.3 |
| Bub Carrington (WAS) | 88% | 11.7<br><sub>2,-,6,3,7</sub> | 3.6<br><sub>0,-,3,0,0</sub> |  | 1.3<br><sub>0,-,0,0,2</sub> |  | 1.4<br><sub>0,-,0,0,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.3 |
| Deandre Ayton (WAS) | 99% | 9.9<br><sub>8,9,11,5,5</sub> | 3.0<br><sub>4,0,0,0,0</sub> |  | 3.2<br><sub>0,3,4,2,2</sub> |  | 0.5<br><sub>1,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 6.6 |
| Will Riley (WAS) | 91% | 8.4<br><sub>2,10,6,9,5</sub> | 3.7<br><sub>2,0,0,4,5</sub> |  | 1.1<br><sub>1,3,1,3,0</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Anthony Gill (WAS) | 52% | 7.1<br><sub>2,-,-,3,-</sub> | 2.6<br><sub>2,-,-,0,-</sub> |  | 1.2<br><sub>0,-,-,2,-</sub> |  | 0.5<br><sub>0,-,-,1,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.3 |
| Tre Mann (WAS) | 63% | 6.0<br><sub>2,-,-,3,1</sub> | 2.6<br><sub>2,-,-,0,0</sub> |  | 0.9<br><sub>0,-,-,0,0</sub> |  | 0.8<br><sub>1,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.3 |

</details>


### BKN @ CHA
Out: PJ Hall (CHA), Kon Knueppel (CHA), Dennis Schroder (CHA), Nolan Traore (BKN), Moritz Wagner (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 102.3–110.9 | BKN 27% | 3.70 / 1.37 | CHA -8.5 | 213.5 | CHA -5.5 covers 59%; o213.5 49% |
| Expected (weighted by chance each plays) | 102.9–112.1 | BKN 26% | 3.86 / 1.35 | CHA -9.5 | 214.5 | CHA -5.5 covers 61%; o213.5 53% |
| if Grayson Allen plays | 103.5–112.9 | BKN 25% | 3.98 / 1.34 | CHA -9.5 | 216.5 | CHA -5.5 covers 61%; o213.5 56% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Grayson Allen (CHA) | Questionable | 55% | 23.5 | 12.7 | 2.7 | 3.4 | 2.2 | 0.9 | 0.3 | 1.7 | 18.8 | full tables below |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 99% | 33.8<br><sub>27,39,35,39,31</sub> | 20.8<br><sub>17,27,29,28,21</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>0,9,4,9,5</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 4.3<br><sub>4,6,4,3,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>3,1,2,2,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 3.1 | 30.9 |
| Michael Porter Jr. | 91% | 32.7<br><sub>27,34,31,34,31</sub> | 18.5<br><sub>5,16,11,12,17</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>3,4,6,11,2</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,5,2,4,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>1,3,0,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.3 | 1.9 | 26.5 |
| Day'Ron Sharpe | 99% | 24.2<br><sub>22,26,26,31,20</sub> | 9.1<br><sub>6,17,6,11,7</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>5,11,5,14,4</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,2,7,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,1,0</sub> |  | 1.1 | 0.8 | 1.5 | 19.3 |
| Mikel Brown Jr. | 98% | 24.1<br><sub>27,24,29,23,25</sub> | 11.8<br><sub>15,18,17,6,21</sub> |  | 2.3<br><sub>1,1,5,2,2</sub> |  | 3.2<br><sub>4,0,7,2,2</sub> |  | 1.7<br><sub>2,3,4,0,4</sub> |  | 0.7 | 0.2 | 1.9 | 17.3 |
| Egor Demin | 98% | 23.3<br><sub>31,21,25,25,17</sub> | 10.1<br><sub>22,6,10,15,7</sub> |  | 2.5<br><sub>4,3,3,3,1</sub> |  | 2.7<br><sub>4,2,4,4,1</sub> |  | 1.6<br><sub>3,0,2,0,1</sub> |  | 0.8 | 0.2 | 1.5 | 15.4 |
| Noah Clowney | 99% | 22.1<br><sub>19,22,26,27,21</sub> | 8.1<br><sub>7,0,13,17,6</sub> |  | 3.4<br><sub>3,2,2,5,3</sub> |  | 1.1<br><sub>1,2,1,1,3</sub> |  | 1.1<br><sub>1,0,3,3,1</sub> |  | 0.6 | 0.5 | 0.9 | 12.6 |
| Danny Wolf | 91% | 21.3<br><sub>23,26,25,19,22</sub> | 8.3<br><sub>6,20,11,5,5</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,5,5,0,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,2,4,1,3</sub> |  | 1.1<br><sub>1,4,3,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.5 | 0.4 | 1.1 | 14.4 |
| Keon Ellis | 96% | 17.6<br><sub>6,8,16,23,17</sub> | 4.2<br><sub>3,0,6,7,0</sub> |  | 1.7<br><sub>1,1,0,2,1</sub> |  | 1.2<br><sub>0,1,0,3,1</sub> |  | 0.5<br><sub>1,0,2,1,0</sub> |  | 0.9 | 0.4 | 0.5 | 7.0 |
| Grant Nelson | 91% | 14.3<br><sub>-,-,8,13,21</sub> | 4.0<br><sub>-,-,2,1,0</sub> |  | 3.3<br><sub>-,-,1,6,5</sub> |  | 1.5<br><sub>-,-,2,0,4</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.6 | 0.8 | 8.7 |
| Chaney Johnson | 83% | 12.1<br><sub>6,-,-,-,12</sub> | 3.4<br><sub>2,-,-,-,7</sub> |  | 1.8<br><sub>2,-,-,-,2</sub> |  | 0.6<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,1</sub> |  | 0.4 | 0.3 | 0.5 | 5.9 |
| Ben Saraf | 58% | 11.6<br><sub>-,-,-,-,9</sub> | 4.5<br><sub>-,-,-,-,4</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.1 | 1.1 | 7.5 |
| Terance Mann | 76% | 11.4<br><sub>5,-,3,2,7</sub> | 3.0<br><sub>0,-,0,0,2</sub> |  | 1.4<br><sub>1,-,0,0,0</sub> |  | 1.0<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.3 |
| Josh Minott | 58% | 9.3<br><sub>4,-,2,-,9</sub> | 4.5<br><sub>0,-,0,-,3</sub> |  | 1.5<br><sub>0,-,0,-,1</sub> |  | 0.5<br><sub>0,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.4 |
| Tyler Bilodeau | 3% | 8.6 | 3.7 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.5 | 6.1 |
| Drake Powell | 58% | 7.7<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.6 |
| Joshua Jefferson | 80% | 6.2<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 0.9 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 99% | 31.7<br><sub>27,42,39,38,35</sub> | 18.9<br><sub>17,23,12,24,18</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 7.9<br><sub>4,11,10,6,8</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,4,3,3,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>3,4,2,3,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.9 | 2.5 | 29.6 |
| Moussa Diabate | 99% | 30.4<br><sub>26,38,30,35,38</sub> | 10.4<br><sub>12,5,21,10,14</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 10.5<br><sub>12,16,15,10,14</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.6 | 23.4 |
| Brandon Miller | 99% | 30.4<br><sub>24,32,33,35,34</sub> | 22.6<br><sub>5,28,19,20,35</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,2,8,3,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>4,4,3,5,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>1,5,5,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0 | 0.6 | 2.8 | 30.5 |
| Sion James | 99% | 27.7<br><sub>35,30,32,28,26</sub> | 7.0<br><sub>3,3,9,5,5</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>8,6,1,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 3.4<br><sub>4,4,2,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.0<br><sub>1,0,1,1,1</sub> |  | 1.0 | 0.1 | 1.3 | 14.4 |
| Coby White | 98% | 24.0<br><sub>20,26,26,28,25</sub> | 16.8<br><sub>21,19,11,21,11</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>0,3,4,3,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 4.7<br><sub>1,4,9,2,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,2,0,5,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.2 | 2.6 | 24.5 |
| Christian Anderson | 93% | 22.5<br><sub>18,14,21,25,28</sub> | 10.5<br><sub>16,5,4,25,15</sub> |  | 2.2<br><sub>3,1,1,2,1</sub> |  | 3.6<br><sub>2,4,2,3,4</sub> |  | 1.7<br><sub>4,1,0,6,3</sub> |  | 0.7 | 0.3 | 1.7 | 16.3 |
| Royce O'Neale | 99% | 20.7<br><sub>19,34,21,13,23</sub> | 6.4<br><sub>3,13,9,0,0</sub> |  | 3.4<br><sub>3,4,1,1,6</sub> |  | 1.3<br><sub>1,1,0,1,2</sub> |  | 1.1<br><sub>1,4,3,0,0</sub> |  | 0.8 | 0.2 | 0.7 | 11.1 |
| Grant Williams | 88% | 19.4<br><sub>20,30,-,-,15</sub> | 7.8<br><sub>11,12,-,-,0</sub> |  | 3.2<br><sub>2,4,-,-,1</sub> |  | 1.5<br><sub>1,0,-,-,0</sub> |  | 1.1<br><sub>3,2,-,-,0</sub> |  | 0.7 | 0.4 | 1.0 | 12.6 |
| Ryan Kalkbrenner | 92% | 14.8<br><sub>18,14,17,9,-</sub> | 4.6<br><sub>5,6,6,0,-</sub> |  | 4.1<br><sub>5,3,6,2,-</sub> |  | 0.8<br><sub>1,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.4 | 1.0 | 0.7 | 9.5 |
| Tidjane Salaun | 98% | 12.7<br><sub>5,5,13,17,8</sub> | 4.9<br><sub>0,0,4,0,4</sub> |  | 2.8<br><sub>2,1,2,5,1</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> |  | 0.6<br><sub>0,0,0,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.4 |
| Liam McNeeley | 58% | 10.0<br><sub>2,-,7,9,-</sub> | 4.0<br><sub>0,-,2,3,-</sub> |  | 1.7<br><sub>0,-,1,2,-</sub> |  | 0.7<br><sub>0,-,0,0,-</sub> |  | 0.4<br><sub>0,-,0,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.5 |
| Hannes Steinbach | 64% | 8.9<br><sub>-,-,-,4,8</sub> | 3.0<br><sub>-,-,-,3,3</sub> |  | 2.5<br><sub>-,-,-,1,3</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 5.9 |

</details>

<details><summary>if Grayson Allen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle (BKN) | 99% | 33.7<br><sub>27,39,35,39,31</sub> | 21.0<br><sub>17,27,29,28,21</sub> | 19.5 · –<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>0,9,4,9,5</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 4.3<br><sub>4,6,4,3,5</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>3,1,2,2,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 3.1 | 31.1 |
| Michael Porter Jr. (BKN) | 91% | 32.6<br><sub>27,34,31,34,31</sub> | 18.5<br><sub>5,16,11,12,17</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>3,4,6,11,2</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>1,5,2,4,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.5<br><sub>1,3,0,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.3 | 1.9 | 26.4 |
| Day'Ron Sharpe (BKN) | 99% | 24.3<br><sub>22,26,26,31,20</sub> | 9.2<br><sub>6,17,6,11,7</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>5,11,5,14,4</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,2,7,5,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>0,0,0,1,0</sub> |  | 1.1 | 0.8 | 1.5 | 19.4 |
| Mikel Brown Jr. (BKN) | 98% | 24.0<br><sub>27,24,29,23,25</sub> | 11.9<br><sub>15,18,17,6,21</sub> |  | 2.3<br><sub>1,1,5,2,2</sub> |  | 3.2<br><sub>4,0,7,2,2</sub> |  | 1.7<br><sub>2,3,4,0,4</sub> |  | 0.7 | 0.2 | 1.9 | 17.4 |
| Egor Demin (BKN) | 98% | 23.2<br><sub>31,21,25,25,17</sub> | 10.2<br><sub>22,6,10,15,7</sub> |  | 2.5<br><sub>4,3,3,3,1</sub> |  | 2.7<br><sub>4,2,4,4,1</sub> |  | 1.6<br><sub>3,0,2,0,1</sub> |  | 0.8 | 0.2 | 1.4 | 15.4 |
| Noah Clowney (BKN) | 99% | 22.2<br><sub>19,22,26,27,21</sub> | 8.1<br><sub>7,0,13,17,6</sub> |  | 3.4<br><sub>3,2,2,5,3</sub> |  | 1.1<br><sub>1,2,1,1,3</sub> |  | 1.1<br><sub>1,0,3,3,1</sub> |  | 0.6 | 0.5 | 0.8 | 12.6 |
| Danny Wolf (BKN) | 91% | 21.2<br><sub>23,26,25,19,22</sub> | 8.3<br><sub>6,20,11,5,5</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>6,5,5,0,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>2,2,4,1,3</sub> |  | 1.1<br><sub>1,4,3,1,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.5 | 0.4 | 1.1 | 14.4 |
| Keon Ellis (BKN) | 96% | 17.5<br><sub>6,8,16,23,17</sub> | 4.1<br><sub>3,0,6,7,0</sub> |  | 1.7<br><sub>1,1,0,2,1</sub> |  | 1.1<br><sub>0,1,0,3,1</sub> |  | 0.5<br><sub>1,0,2,1,0</sub> |  | 0.9 | 0.4 | 0.5 | 7.0 |
| Grant Nelson (BKN) | 91% | 14.3<br><sub>-,-,8,13,21</sub> | 4.0<br><sub>-,-,2,1,0</sub> |  | 3.3<br><sub>-,-,1,6,5</sub> |  | 1.4<br><sub>-,-,2,0,4</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.6 | 0.8 | 8.7 |
| Chaney Johnson (BKN) | 83% | 12.1<br><sub>6,-,-,-,12</sub> | 3.4<br><sub>2,-,-,-,7</sub> |  | 1.8<br><sub>2,-,-,-,2</sub> |  | 0.7<br><sub>1,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,1</sub> |  | 0.4 | 0.3 | 0.5 | 5.9 |
| Ben Saraf (BKN) | 58% | 11.6<br><sub>-,-,-,-,9</sub> | 4.6<br><sub>-,-,-,-,4</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.1 | 1.1 | 7.6 |
| Terance Mann (BKN) | 76% | 11.4<br><sub>5,-,3,2,7</sub> | 3.0<br><sub>0,-,0,0,2</sub> |  | 1.4<br><sub>1,-,0,0,0</sub> |  | 1.0<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.3 |
| Josh Minott (BKN) | 58% | 9.2<br><sub>4,-,2,-,9</sub> | 4.6<br><sub>0,-,0,-,3</sub> |  | 1.5<br><sub>0,-,0,-,1</sub> |  | 0.4<br><sub>0,-,0,-,0</sub> |  | 0.5<br><sub>0,-,0,-,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Tyler Bilodeau (BKN) | 3% | 8.5 | 3.5 |  | 1.6 |  | 0.7 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Drake Powell (BKN) | 58% | 7.8<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.7 |
| Joshua Jefferson (BKN) | 80% | 6.2<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.0 |
| Naz Reid (CHA) | 99% | 29.4<br><sub>27,42,39,38,35</sub> | 17.0<br><sub>17,23,12,24,18</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>4,11,10,6,8</sub> | 8.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>3,4,3,3,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>3,4,2,3,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.8 | 2.2 | 27.2 |
| Brandon Miller (CHA) | 99% | 28.2<br><sub>24,32,33,35,34</sub> | 20.6<br><sub>5,28,19,20,35</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>2,2,8,3,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,4,3,5,1</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>1,5,5,4,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.5 | 2.3 | 27.9 |
| Moussa Diabate (CHA) | 99% | 28.0<br><sub>26,38,30,35,38</sub> | 10.0<br><sub>12,5,21,10,14</sub> | 10.5 · –<br><sub>o 48% · u 52%</sub> | 9.8<br><sub>12,16,15,10,14</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.0 | 1.5 | 22.2 |
| Sion James (CHA) | 99% | 24.5<br><sub>35,30,32,28,26</sub> | 6.0<br><sub>3,3,9,5,5</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>8,6,1,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>4,4,2,4,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>1,0,1,1,1</sub> |  | 0.9 | 0.1 | 1.1 | 12.7 |
| Grayson Allen (CHA) | 100% | 23.5<br><sub>25,-,-,-,-</sub> | 12.7<br><sub>12,-,-,-,-</sub> | 12.5 · – | 2.7<br><sub>5,-,-,-,-</sub> | 2.5 | 3.4<br><sub>4,-,-,-,-</sub> |  | 2.2<br><sub>2,-,-,-,-</sub> | 2.5 | 0.9 | 0.3 | 1.7 | 18.8 |
| Coby White (CHA) | 98% | 22.1<br><sub>20,26,26,28,25</sub> | 15.6<br><sub>21,19,11,21,11</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>0,3,4,3,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 4.3<br><sub>1,4,9,2,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,2,0,5,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.2 | 2.3 | 22.8 |
| Christian Anderson (CHA) | 93% | 19.8<br><sub>18,14,21,25,28</sub> | 9.6<br><sub>16,5,4,25,15</sub> |  | 2.0<br><sub>3,1,1,2,1</sub> |  | 3.1<br><sub>2,4,2,3,4</sub> |  | 1.5<br><sub>4,1,0,6,3</sub> |  | 0.6 | 0.2 | 1.5 | 14.7 |
| Royce O'Neale (CHA) | 99% | 19.3<br><sub>19,34,21,13,23</sub> | 6.2<br><sub>3,13,9,0,0</sub> |  | 3.2<br><sub>3,4,1,1,6</sub> |  | 1.3<br><sub>1,1,0,1,2</sub> |  | 1.1<br><sub>1,4,3,0,0</sub> |  | 0.8 | 0.2 | 0.6 | 10.7 |
| Grant Williams (CHA) | 88% | 18.6<br><sub>20,30,-,-,15</sub> | 7.6<br><sub>11,12,-,-,0</sub> |  | 3.1<br><sub>2,4,-,-,1</sub> |  | 1.5<br><sub>1,0,-,-,0</sub> |  | 1.1<br><sub>3,2,-,-,0</sub> |  | 0.6 | 0.4 | 0.9 | 12.2 |
| Ryan Kalkbrenner (CHA) | 92% | 12.2<br><sub>18,14,17,9,-</sub> | 4.0<br><sub>5,6,6,0,-</sub> |  | 3.4<br><sub>5,3,6,2,-</sub> |  | 0.7<br><sub>1,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.9 | 0.6 | 8.0 |
| Tidjane Salaun (CHA) | 98% | 11.2<br><sub>5,5,13,17,8</sub> | 4.5<br><sub>0,0,4,0,4</sub> |  | 2.5<br><sub>2,1,2,5,1</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.6 |
| Liam McNeeley (CHA) | 58% | 7.8<br><sub>2,-,7,9,-</sub> | 3.4<br><sub>0,-,2,3,-</sub> |  | 1.4<br><sub>0,-,1,2,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.3<br><sub>0,-,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.5 |
| Hannes Steinbach (CHA) | 64% | 7.8<br><sub>-,-,-,4,8</sub> | 2.7<br><sub>-,-,-,3,3</sub> |  | 2.2<br><sub>-,-,-,1,3</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 5.3 |

</details>


### IND @ CHI
Out: Tobe Awaka (CHI), Norman Powell (CHI), Jaylin Sellers (CHI), Caleb Wilson (CHI), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND)

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 96% | 33.9<br><sub>33,30,33,35,25</sub> | 24.7<br><sub>24,21,25,20,11</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>4,7,6,8,2</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>3,2,1,5,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>2,2,3,2,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.2 | 0.4 | 2.0 | 35.1 |
| Andrew Nembhard | 93% | 33.4<br><sub>-,26,32,38,26</sub> | 17.2<br><sub>-,12,16,15,14</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>-,3,2,2,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 8.3<br><sub>-,8,8,6,3</sub> | 7.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>-,3,2,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.2 | 2.5 | 28.6 |
| Aaron Nesmith | 80% | 28.7<br><sub>29,29,32,-,24</sub> | 12.4<br><sub>2,2,9,-,6</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>3,10,2,-,4</sub> |  | 2.2<br><sub>3,7,2,-,0</sub> |  | 1.6<br><sub>0,0,0,-,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.5 | 1.2 | 18.6 |
| Ivica Zubac | 91% | 26.7<br><sub>24,27,31,26,24</sub> | 12.6<br><sub>4,21,10,14,5</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 10.3<br><sub>3,10,14,15,16</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,2,1,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 1.4 | 24.7 |
| Kelly Oubre Jr. | 93% | 24.0<br><sub>23,23,27,28,17</sub> | 11.8<br><sub>17,17,15,20,8</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 3.9<br><sub>4,6,5,4,3</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 1.2<br><sub>0,0,0,2,0</sub> |  | 1.1<br><sub>2,3,0,4,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.6 | 1.0 | 16.9 |
| Quenton Jackson | 99% | 21.1<br><sub>22,18,17,20,23</sub> | 9.2<br><sub>15,3,2,9,9</sub> |  | 3.0<br><sub>2,2,1,3,4</sub> |  | 3.1<br><sub>3,2,3,0,1</sub> |  | 0.9<br><sub>2,1,0,1,1</sub> |  | 1.3 | 0.2 | 1.2 | 15.4 |
| Obi Toppin | 91% | 18.8<br><sub>17,26,22,24,15</sub> | 10.9<br><sub>6,17,9,17,2</sub> |  | 3.9<br><sub>1,3,5,6,3</sub> |  | 1.9<br><sub>1,2,1,4,1</sub> |  | 1.2<br><sub>0,2,0,2,0</sub> |  | 0.6 | 0.2 | 1.0 | 16.7 |
| Braden Smith | 88% | 17.6<br><sub>18,11,18,24,21</sub> | 5.5<br><sub>8,5,6,6,2</sub> |  | 1.8<br><sub>5,3,1,2,1</sub> |  | 3.4<br><sub>3,5,4,6,1</sub> |  | 0.4<br><sub>2,1,0,1,0</sub> |  | 0.9 | 0.2 | 1.0 | 10.6 |
| Jalen Slawson | 93% | 16.0<br><sub>12,14,14,20,21</sub> | 5.1<br><sub>5,4,7,16,4</sub> |  | 3.7<br><sub>4,2,3,10,6</sub> |  | 1.8<br><sub>2,2,0,2,4</sub> |  | 0.4<br><sub>1,0,0,3,0</sub> |  | 0.9 | 0.9 | 0.7 | 10.6 |
| Jarace Walker | 91% | 14.6<br><sub>17,11,1,14,15</sub> | 6.0<br><sub>1,8,0,4,6</sub> |  | 3.4<br><sub>3,1,0,8,5</sub> |  | 1.7<br><sub>1,3,0,3,3</sub> |  | 0.7<br><sub>0,1,0,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 11.1 |
| Jay Huff | 80% | 13.6<br><sub>15,1,1,-,22</sub> | 6.4<br><sub>5,0,2,-,18</sub> |  | 2.6<br><sub>3,0,0,-,1</sub> |  | 0.9<br><sub>0,0,0,-,0</sub> |  | 0.7<br><sub>0,0,0,-,2</sub> |  | 0.3 | 0.9 | 0.6 | 9.9 |
| Larry Nance Jr. | 98% | 10.8<br><sub>9,11,11,4,8</sub> | 3.5<br><sub>3,7,5,0,2</sub> |  | 2.2<br><sub>1,2,3,0,2</sub> |  | 0.8<br><sub>0,0,0,0,2</sub> |  | 0.3<br><sub>1,1,1,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.5 |
| Kobe Brown | 88% | 9.9<br><sub>2,-,-,7,-</sub> | 3.5<br><sub>0,-,-,4,-</sub> |  | 1.9<br><sub>0,-,-,0,-</sub> |  | 0.9<br><sub>0,-,-,1,-</sub> |  | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.2 |
| Johnny Furphy | 3% | 9.8 | 2.9 |  | 2.4 |  | 1.0 |  | 0.2 |  | 0.5 | 0.2 | 0.4 | 6.2 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matas Buzelis | 99% | 31.1<br><sub>30,25,38,27,34</sub> | 18.9<br><sub>25,9,21,15,24</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>5,5,5,6,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>4,1,3,0,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>5,1,4,4,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 1.1 | 2.2 | 27.2 |
| Josh Giddey | 99% | 30.9<br><sub>28,23,41,22,34</sub> | 15.5<br><sub>18,2,23,4,12</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 7.8<br><sub>14,6,14,2,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 10.0<br><sub>9,7,22,11,7</sub> | 8.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>1,0,2,0,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.6 | 3.0 | 33.3 |
| Isaac Okoro | 99% | 29.3<br><sub>25,29,42,27,31</sub> | 10.8<br><sub>12,9,11,12,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,7,1,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>4,1,2,3,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4<br><sub>4,1,2,3,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.4 | 0.9 | 16.2 |
| Jalen Smith | 92% | 27.2<br><sub>21,-,34,25,-</sub> | 15.2<br><sub>14,-,26,11,-</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 8.6<br><sub>6,-,4,6,-</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>3,-,1,4,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,-,6,1,-</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.9 | 1.1 | 25.8 |
| Buddy Hield | 91% | 25.4<br><sub>19,23,40,27,27</sub> | 14.1<br><sub>11,15,33,17,9</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>1,4,7,5,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.4<br><sub>2,0,6,0,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,4,7,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 1.2 | 20.3 |
| Nic Claxton | 98% | 24.2<br><sub>22,29,-,23,29</sub> | 10.5<br><sub>14,11,-,6,10</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>4,7,-,6,2</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>1,1,-,0,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.8 | 1.0 | 1.2 | 19.1 |
| Tre Jones | 99% | 22.0<br><sub>16,25,12,27,20</sub> | 13.5<br><sub>10,12,9,16,10</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,1,2,4,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>6,7,4,9,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.5<br><sub>0,0,0,1,0</sub> |  | 1.1 | 0.2 | 1.4 | 21.3 |
| Patrick Williams | 91% | 19.2<br><sub>13,23,16,19,15</sub> | 7.3<br><sub>2,6,2,7,11</sub> |  | 3.0<br><sub>1,3,2,5,1</sub> |  | 1.5<br><sub>2,1,0,2,0</sub> |  | 0.9<br><sub>0,0,0,1,3</sub> |  | 0.7 | 0.4 | 0.9 | 11.7 |
| Jordan Hawkins | 71% | 16.5<br><sub>-,-,14,18,21</sub> | 7.6<br><sub>-,-,6,19,10</sub> |  | 2.1<br><sub>-,-,1,1,3</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> |  | 1.1<br><sub>-,-,2,4,3</sub> |  | 0.5 | 0.3 | 0.7 | 11.0 |
| Zach Collins | 67% | 16.4<br><sub>11,15,17,-,19</sub> | 6.8<br><sub>3,6,5,-,6</sub> |  | 4.6<br><sub>2,2,1,-,3</sub> |  | 1.6<br><sub>0,4,0,-,2</sub> |  | 0.5<br><sub>1,0,1,-,2</sub> |  | 0.5 | 0.5 | 0.9 | 13.0 |
| Noa Essengue | 91% | 11.9<br><sub>15,15,11,4,11</sub> | 5.5<br><sub>5,8,9,6,5</sub> |  | 2.7<br><sub>3,4,4,2,0</sub> |  | 0.6<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.2 | 0.7 | 8.8 |
| Leonard Miller | 48% | 11.3<br><sub>7,-,-,-,-</sub> | 5.5<br><sub>4,-,-,-,-</sub> |  | 2.9<br><sub>2,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 9.1 |
| Orlando Robinson | 25% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.9 |

</details>


### OKC @ MIL
Out: Kasparas Jakucionis (MIL), Chet Holmgren (OKC), Aday Mara (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 99% | 35.3<br><sub>36,37,-,38,37</sub> | 35.0<br><sub>34,40,-,38,32</sub> | 32.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>5,3,-,5,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 6.1<br><sub>3,8,-,7,5</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,4,-,4,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.9 | 2.5 | 45.6 |
| Ajay Mitchell | 99% | 30.7<br><sub>34,31,22,35,31</sub> | 17.8<br><sub>13,8,17,12,25</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>6,2,3,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.4<br><sub>6,4,3,3,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.3<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.6 | 26.2 |
| Jared McCain | 99% | 30.6<br><sub>33,30,29,36,28</sub> | 16.6<br><sub>18,18,20,13,9</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>3,3,2,5,1</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>1,0,3,0,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>4,3,2,1,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.9 | 0.2 | 1.4 | 22.2 |
| Isaiah Hartenstein | 99% | 29.2<br><sub>27,28,23,30,31</sub> | 10.8<br><sub>6,5,2,18,8</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 12.6<br><sub>17,8,8,9,16</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,4,4,3,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 28.0 |
| Kenrich Williams | 98% | 25.5<br><sub>23,28,26,26,25</sub> | 10.4<br><sub>10,6,12,20,13</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>5,2,4,9,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>1,4,2,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>0,1,2,4,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.2 | 0.9 | 17.9 |
| Bennett Stirtz | 99% | 23.2<br><sub>17,25,32,19,24</sub> | 9.1<br><sub>6,18,21,5,6</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>0,2,3,9,1</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,2,5,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.7<br><sub>2,4,5,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.2 | 0.7 | 13.5 |
| Micah Peavy | 96% | 23.1<br><sub>-,9,31,24,25</sub> | 6.2<br><sub>-,2,9,7,2</sub> |  | 4.7<br><sub>-,2,6,3,7</sub> |  | 1.0<br><sub>-,0,1,2,0</sub> |  | 0.6<br><sub>-,0,1,1,0</sub> |  | 0.9 | 0.3 | 0.7 | 11.9 |
| Alex Caruso | 67% | 21.3<br><sub>9,-,-,-,26</sub> | 8.8<br><sub>5,-,-,-,11</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>0,-,-,-,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>1,-,-,-,2</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,-,-,-,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.5 | 0.9 | 14.8 |
| Josh Dix | 58% | 17.5<br><sub>-,-,32,16,-</sub> | 4.8<br><sub>-,-,13,0,-</sub> |  | 2.1<br><sub>-,-,5,1,-</sub> |  | 1.1<br><sub>-,-,4,1,-</sub> |  | 0.5<br><sub>-,-,3,0,-</sub> |  | 0.5 | 0.2 | 0.4 | 8.0 |
| Nique Clifford | 76% | 15.3<br><sub>13,15,26,6,12</sub> | 5.4<br><sub>7,4,11,0,0</sub> |  | 2.4<br><sub>0,5,3,0,2</sub> |  | 1.1<br><sub>0,1,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.9 |
| Brooks Barnhizer | 52% | 11.0<br><sub>-,-,19,9,-</sub> | 3.1<br><sub>-,-,8,7,-</sub> |  | 2.6<br><sub>-,-,4,4,-</sub> |  | 0.8<br><sub>-,-,2,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.5 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 99% | 31.1<br><sub>31,40,37,37,35</sub> | 18.9<br><sub>19,50,32,28,20</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>4,11,6,2,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 4.3<br><sub>3,7,8,5,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>4,7,4,3,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.3 | 2.5 | 27.5 |
| Kyle Kuzma | 99% | 26.3<br><sub>-,33,32,31,30</sub> | 12.2<br><sub>-,12,18,13,11</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>-,5,5,3,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>-,1,3,2,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>-,2,2,3,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 0.4 | 1.6 | 19.0 |
| Jaime Jaquez Jr. | 99% | 25.8<br><sub>22,25,25,35,35</sub> | 13.0<br><sub>9,9,3,21,16</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>1,0,4,5,11</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>2,1,2,4,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.2 | 1.8 | 20.8 |
| Myles Turner | 99% | 24.2<br><sub>-,26,28,26,29</sub> | 9.7<br><sub>-,5,27,3,7</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>-,6,11,6,12</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>-,5,1,2,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>-,1,5,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.5 | 1.6 | 1.3 | 16.9 |
| Brayden Burries | 99% | 23.3<br><sub>28,26,29,22,28</sub> | 11.8<br><sub>14,26,14,3,23</sub> |  | 5.2<br><sub>3,8,10,3,6</sub> |  | 2.4<br><sub>3,4,4,3,1</sub> |  | 1.1<br><sub>2,2,1,0,2</sub> |  | 0.8 | 0.2 | 1.7 | 19.4 |
| Ryan Rollins | 99% | 23.2<br><sub>21,28,22,19,30</sub> | 11.0<br><sub>15,8,6,2,12</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,6,1,3,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.6<br><sub>6,1,3,3,6</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,0,0,0,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.3 | 2.1 | 18.4 |
| Kel'el Ware | 98% | 17.5<br><sub>26,22,23,22,20</sub> | 7.9<br><sub>11,6,9,13,7</sub> |  | 5.8<br><sub>5,8,3,14,7</sub> |  | 1.1<br><sub>0,3,0,2,2</sub> |  | 0.6<br><sub>2,0,1,1,1</sub> |  | 0.4 | 1.0 | 1.1 | 14.7 |
| Nate Ament | 98% | 14.8<br><sub>35,14,25,21,13</sub> | 5.9<br><sub>18,2,7,8,0</sub> |  | 2.6<br><sub>9,1,4,3,4</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 0.6<br><sub>2,0,0,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.1 |
| Cormac Ryan | 52% | 14.5<br><sub>-,-,-,-,-</sub> | 7.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.4 |
| Pete Nance | 96% | 10.9<br><sub>28,-,-,-,9</sub> | 3.6<br><sub>7,-,-,-,0</sub> |  | 1.8<br><sub>3,-,-,-,0</sub> |  | 0.8<br><sub>3,-,-,-,0</sub> |  | 0.4<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 6.2 |
| Kam Jones | 52% | 9.2<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 2.0<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.5 |
| AJ Green | 76% | 9.0<br><sub>-,12,-,5,5</sub> | 3.5<br><sub>-,9,-,0,0</sub> |  | 0.9<br><sub>-,0,-,0,1</sub> |  | 0.6<br><sub>-,0,-,0,0</sub> |  | 0.5<br><sub>-,3,-,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.0 |
| Caris LeVert | 71% | 8.5<br><sub>11,5,8,12,6</sub> | 3.6<br><sub>3,0,0,2,2</sub> |  | 1.2<br><sub>3,1,0,1,1</sub> |  | 1.0<br><sub>1,0,0,2,0</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 5.8 |
| Jericho Sims | 48% | 8.1<br><sub>10,-,-,-,-</sub> | 2.0<br><sub>0,-,-,-,-</sub> |  | 2.1<br><sub>0,-,-,-,-</sub> |  | 0.6<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 4.8 |
| Ousmane Dieng | 52% | 7.7<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.3 |
| Gary Trent Jr. | 52% | 7.4<br><sub>7,-,5,-,-</sub> | 3.6<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.0 | 0.3 | 4.6 |
| Bogoljub Markovic | 38% | 5.6<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.4 |

</details>


### PHI @ HOU
Out: Jaylen Brown (PHI), Joel Embiid (PHI), Ariel Hukporti (PHI), LeBron James (PHI), Dean Wade (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 106.9–118.4 | PHI 21% | 4.75 / 1.27 | HOU -11.5 | 225.5 | HOU -12.5 covers 47%; o219.5 62% |
| Expected (weighted by chance each plays) | 107.2–118.6 | PHI 21% | 4.68 / 1.27 | HOU -11.5 | 225.5 | HOU -12.5 covers 47%; o219.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Steven Adams (HOU) | Questionable | 55% | 14.8 | 3.8 | 5.4 | 1.0 | 0.0 | 0.4 | 0.5 | 0.7 | 10.3 | small |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 91% | 37.9<br><sub>-,36,35,37,29</sub> | 29.3<br><sub>-,17,22,30,14</sub> | 26.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>-,4,2,4,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 6.8<br><sub>-,4,5,6,6</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>-,0,2,3,0</sub> | 2.5<br><sub>o 42% · u 57%</sub> | 1.4 | 0.5 | 3.0 | 39.8 |
| VJ Edgecombe | 98% | 36.7<br><sub>43,38,35,36,32</sub> | 18.3<br><sub>24,16,12,18,9</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>8,3,7,6,5</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 5.5<br><sub>6,6,7,5,7</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>4,1,1,2,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.6 | 0.5 | 2.5 | 30.1 |
| Anfernee Simons | 99% | 29.6<br><sub>38,26,18,15,25</sub> | 15.4<br><sub>18,18,3,6,19</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 2.6<br><sub>2,0,0,1,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.5<br><sub>2,1,0,1,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.6<br><sub>3,4,0,2,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.2 | 1.7 | 20.4 |
| Jabari Walker | 96% | 28.8<br><sub>13,20,20,17,23</sub> | 12.2<br><sub>6,9,10,7,4</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>5,7,5,2,4</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,4,2,1,1</sub> |  | 1.1<br><sub>1,0,0,1,1</sub> |  | 0.9 | 0.3 | 1.3 | 21.5 |
| Kentavious Caldwell-Pope | 99% | 27.2<br><sub>32,35,17,28,21</sub> | 8.2<br><sub>8,11,2,5,8</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>8,1,3,1,0</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.3<br><sub>1,2,1,3,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>2,3,0,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.3 | 1.1 | 13.3 |
| Dominick Barlow | 96% | 25.7<br><sub>-,11,16,16,18</sub> | 9.3<br><sub>-,12,6,9,12</sub> |  | 5.8<br><sub>-,4,2,8,8</sub> |  | 1.4<br><sub>-,1,0,0,1</sub> |  | 0.3<br><sub>-,1,0,0,0</sub> |  | 0.9 | 0.9 | 1.1 | 16.5 |
| Adem Bona | 98% | 21.6<br><sub>-,-,5,13,14</sub> | 5.6<br><sub>-,-,4,0,0</sub> |  | 5.5<br><sub>-,-,2,6,3</sub> |  | 0.9<br><sub>-,-,0,0,0</sub> |  | 0.1<br><sub>-,-,0,0,0</sub> |  | 0.6 | 1.4 | 1.2 | 12.0 |
| Labaron Philon Jr. | 67% | 19.1<br><sub>17,6,3,-,11</sub> | 7.2<br><sub>10,2,2,-,3</sub> |  | 2.2<br><sub>1,0,1,-,0</sub> |  | 1.9<br><sub>2,0,1,-,2</sub> |  | 0.9<br><sub>2,0,0,-,1</sub> |  | 0.6 | 0.1 | 1.1 | 11.3 |
| Justin Edwards | 58% | 18.9<br><sub>13,-,3,-,7</sub> | 7.6<br><sub>2,-,5,-,3</sub> |  | 2.6<br><sub>1,-,1,-,1</sub> |  | 1.1<br><sub>0,-,0,-,0</sub> |  | 0.9<br><sub>0,-,1,-,1</sub> |  | 0.8 | 0.2 | 0.8 | 11.2 |
| Tacko Fall | 52% | 14.7<br><sub>10,-,-,-,4</sub> | 3.8<br><sub>2,-,-,-,4</sub> |  | 3.7<br><sub>3,-,-,-,1</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.9 | 0.6 | 8.2 |
| Rayan Rupert | 36% | 14.0<br><sub>-,-,-,-,-</sub> | 5.3<br><sub>-,-,-,-,-</sub> |  | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.8 | 0.1 | 0.9 | 9.0 |
| Caleb Love | 48% | 13.1<br><sub>6,-,-,-,-</sub> | 4.2<br><sub>3,-,-,-,-</sub> |  | 1.6<br><sub>1,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.5<br><sub>1,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.5 | 6.9 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 99% | 35.9<br><sub>29,32,35,33,33</sub> | 24.1<br><sub>22,21,16,32,20</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>2,2,4,9,10</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>3,3,4,4,2</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>2,4,0,4,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.7 | 0.9 | 2.8 | 34.7 |
| Amen Thompson | 88% | 35.1<br><sub>-,31,26,28,36</sub> | 17.1<br><sub>-,15,22,20,18</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 7.7<br><sub>-,9,6,4,10</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 4.0<br><sub>-,3,0,5,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>-,0,0,1,0</sub> | 0.5<br><sub>o 26% · u 74%</sub> | 1.2 | 0.8 | 2.0 | 28.7 |
| Alperen Sengun | 96% | 34.4<br><sub>30,14,36,31,32</sub> | 21.5<br><sub>23,7,28,20,23</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 10.2<br><sub>7,7,11,8,11</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>2,1,10,7,11</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>1,1,1,1,3</sub> | 0.5<br><sub>o 55% · u 45%</sub> | 1.0 | 1.1 | 2.8 | 38.9 |
| Jabari Smith Jr. | 99% | 34.3<br><sub>32,26,32,28,32</sub> | 14.7<br><sub>12,17,21,13,13</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>10,4,4,6,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,2,3,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.1<br><sub>1,3,3,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.6 | 1.0 | 1.2 | 23.2 |
| Fred VanVleet | 91% | 33.4<br><sub>26,27,33,31,34</sub> | 14.2<br><sub>8,15,25,6,13</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>5,2,1,2,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 5.2<br><sub>6,6,9,4,6</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>2,3,3,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.5 | 1.4 | 22.7 |
| Tari Eason | 99% | 23.6<br><sub>27,25,23,22,15</sub> | 9.6<br><sub>7,11,7,10,7</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>7,4,6,4,2</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>3,3,1,4,0</sub> |  | 1.1<br><sub>0,1,1,2,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.0 | 0.7 | 1.0 | 16.4 |
| Marcus Smart | 76% | 20.8<br><sub>-,18,23,25,18</sub> | 6.5<br><sub>-,4,3,4,4</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>-,2,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.2<br><sub>-,4,2,3,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9<br><sub>-,1,1,0,0</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.9 | 0.4 | 1.2 | 11.0 |
| Reed Sheppard | 96% | 18.7<br><sub>19,25,14,17,15</sub> | 8.2<br><sub>5,20,0,5,7</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>2,4,2,3,1</sub> |  | 2.2<br><sub>2,2,0,5,1</sub> |  | 1.4<br><sub>1,6,0,1,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.5 | 0.8 | 12.2 |
| Clint Capela | 30% | 12.0<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 4.5<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.7 | 0.5 | 8.7 |
| Bogdan Bogdanovic | 98% | 11.5<br><sub>26,11,5,9,10</sub> | 4.1<br><sub>6,1,0,2,5</sub> |  | 1.4<br><sub>0,3,1,1,0</sub> |  | 1.0<br><sub>1,0,0,2,1</sub> |  | 0.5<br><sub>2,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 6.5 |
| Oscar Tshiebwe | 72% | 8.7<br><sub>6,11,-,-,-</sub> | 3.5<br><sub>6,4,-,-,-</sub> |  | 3.8<br><sub>6,4,-,-,-</sub> |  | 0.6<br><sub>0,3,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 7.8 |
| Isaiah Crawford | 52% | 7.1<br><sub>21,2,-,-,-</sub> | 2.4<br><sub>11,0,-,-,-</sub> |  | 1.4<br><sub>10,0,-,-,-</sub> |  | 0.3<br><sub>3,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |
| Jae'Sean Tate | 48% | 6.3<br><sub>12,1,-,-,-</sub> | 2.0<br><sub>3,0,-,-,-</sub> |  | 1.4<br><sub>3,0,-,-,-</sub> |  | 0.4<br><sub>2,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.9 |
| Bruce Thornton | 52% | 5.9<br><sub>12,1,-,-,-</sub> | 2.6<br><sub>7,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-28/`._
