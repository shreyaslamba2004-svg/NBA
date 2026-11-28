# NBA model · Sat 28 Nov 2026 (US date)

Updated **Sat 28 Nov, 06:58 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-28/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant PA over 39.5 (40+) | PHI @ HOU | draftkings | 17.00 | 14.16 | 7.09 | 14.1% | 5.5% | 7.1% | +19.9% | +139.8% | 0.3% |
| Kevin Durant PTS over 34.5 (35+) | PHI @ HOU | draftkings | 16.40 | 13.93 | 7.21 | 13.9% | 5.7% | 7.2% | +17.7% | +127.4% | 0.3% |
| Kevin Durant PRA over 49.5 (50+) | PHI @ HOU | draftkings | 23.00 | 19.65 | 10.27 | 9.7% | 4.1% | 5.1% | +17.1% | +123.9% | 0.2% |
| Kevin Durant PRA over 44.5 (45+) | PHI @ HOU | draftkings | 12.60 | 10.86 | 5.77 | 17.3% | 7.4% | 9.2% | +16.1% | +118.4% | 0.4% |
| Kevin Durant PR over 44.5 (45+) | PHI @ HOU | draftkings | 22.00 | 19.38 | 10.80 | 9.3% | 4.2% | 5.2% | +13.4% | +103.8% | 0.2% |
| Kevin Durant PA over 34.5 (35+) | PHI @ HOU | draftkings | 7.70 | 6.84 | 3.87 | 25.8% | 12.1% | 14.6% | +12.5% | +98.7% | 0.5% |
| Josh Giddey AST over 15.5 (16+) | IND @ CHI | draftkings | 20.80 | 18.66 | 10.79 | 9.3% | 4.5% | 5.4% | +11.4% | +92.8% | 0.1% |
| Josh Giddey PRA over 44.5 (45+) | IND @ CHI | draftkings | 14.00 | 12.56 | 7.27 | 13.8% | 6.7% | 8.0% | +11.4% | +92.6% | 0.2% |
| Kevin Durant PR over 39.5 (40+) | PHI @ HOU | draftkings | 11.20 | 10.06 | 5.83 | 17.2% | 8.3% | 9.9% | +11.3% | +92.0% | 0.3% |
| Kevin Durant PRA over 39.5 (40+) | PHI @ HOU | draftkings | 6.11 | 5.57 | 3.34 | 30.0% | 15.3% | 17.9% | +9.7% | +83.1% | 0.5% |
| Kevin Durant PTS over 29.5 (30+) | PHI @ HOU | draftkings | 6.87 | 6.31 | 3.84 | 26.1% | 13.6% | 15.9% | +8.9% | +78.9% | 0.4% |
| Kevin Durant AST over 7.5 (8+) | PHI @ HOU | draftkings | 16.20 | 14.93 | 9.17 | 10.9% | 5.8% | 6.7% | +8.5% | +76.7% | 0.1% |
| Tyrese Maxey PA over 54.5 (55+) | PHI @ HOU | draftkings | 20.40 | 18.87 | 11.67 | 8.6% | 4.6% | 5.3% | +8.2% | +74.8% | 0.1% |
| Josh Giddey PRA over 39.5 (40+) | IND @ CHI | draftkings | 6.83 | 6.35 | 3.97 | 25.2% | 13.7% | 15.8% | +7.7% | +72.0% | 0.3% |
| Josh Giddey PRA over 49.5 (50+) | IND @ CHI | draftkings | 26.00 | 24.21 | 15.27 | 6.6% | 3.6% | 4.1% | +7.4% | +70.2% | 0.1% |
| Amen Thompson AST over 7.5 (8+) | PHI @ HOU | draftkings | 22.00 | 20.49 | 12.95 | 7.7% | 4.2% | 4.9% | +7.3% | +69.8% | 0.1% |
| Josh Giddey AST over 13.5 (14+) | IND @ CHI | draftkings | 9.30 | 8.70 | 5.56 | 18.0% | 10.1% | 11.5% | +6.8% | +67.4% | 0.2% |
| Alex Sarr AST over 3.5 (4+) | ORL @ WAS | draftkings | 10.00 | 9.40 | 6.06 | 16.5% | 9.3% | 10.6% | +6.4% | +65.0% | 0.2% |
| Amen Thompson AST over 5.5 (6+) | PHI @ HOU | draftkings | 6.48 | 6.10 | 3.94 | 25.4% | 14.4% | 16.4% | +6.3% | +64.3% | 0.3% |
| Tyrese Maxey PA over 49.5 (50+) | PHI @ HOU | draftkings | 11.20 | 10.55 | 6.84 | 14.6% | 8.3% | 9.5% | +6.2% | +63.6% | 0.1% |
| Franz Wagner PR over 54.5 (55+) | ORL @ WAS | draftkings | 27.00 | 25.45 | 16.55 | 6.0% | 3.5% | 3.9% | +6.1% | +63.1% | 0.1% |
| Amen Thompson PA over 29.5 (30+) | PHI @ HOU | draftkings | 11.40 | 10.85 | 7.22 | 13.9% | 8.2% | 9.2% | +5.1% | +58.0% | 0.1% |
| Kevin Durant PR over 34.5 (35+) | PHI @ HOU | draftkings | 5.25 | 4.99 | 3.32 | 30.1% | 17.8% | 20.0% | +5.1% | +58.0% | 0.3% |
| Trae Young AST over 13.5 (14+) | ORL @ WAS | draftkings | 13.20 | 12.56 | 8.39 | 11.9% | 7.1% | 8.0% | +5.0% | +57.3% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ORL @ WAS | Sun 29 Nov 09:00 | 115.4–113.2 | ORL 56% | 1.78 / 2.28 | WAS +2.5 | 228.5 | WAS +3.5 covers 53%; o219.5 69% |
| BKN @ CHA | Sun 29 Nov 10:00 | 104.3–110.2 | BKN 34% | 2.97 / 1.51 | CHA -6.5 | 214.5 | CHA -5.5 covers 52%; o213.5 52% |
| IND @ CHI | Sun 29 Nov 12:00 | 118.3–118.6 | IND 49% | 2.03 / 1.97 | CHI +0.5 | 236.5 | CHI -2.5 covers 45%; o235.5 53% |
| OKC @ MIL | Sun 29 Nov 12:00 | 119.4–111.1 | OKC 72% | 1.39 / 3.56 | MIL +8.5 | 230.5 | MIL +11.5 covers 59%; o228.5 54% |
| PHI @ HOU | Sun 29 Nov 12:30 | 108.3–117.4 | PHI 26% | 3.85 / 1.35 | HOU -9.5 | 225.5 | HOU -12.5 covers 40%; o219.5 63% |

### ORL @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Paolo Banchero (ORL), Colin Castleton (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Kevin Porter Jr. (ORL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Davis AST over 2.5 (3+) | ORL @ WAS | draftkings | 2.44 | 2.44 | 1.91 | 52.5% | 38.5% | 41.1% | +0.2% | +28.0% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.4–113.2 | ORL 56% | 1.78 / 2.28 | WAS +2.5 | 228.5 | WAS +3.5 covers 53%; o219.5 69% |
| Expected (weighted by chance each plays) | 116.0–113.0 | ORL 59% | 1.71 / 2.41 | WAS +3.5 | 228.5 | WAS +3.5 covers 51%; o219.5 69% |
| if Anthony Black plays | 116.1–112.7 | ORL 60% | 1.67 / 2.49 | WAS +3.5 | 228.5 | WAS +3.5 covers 50%; o219.5 69% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Black (ORL) | Questionable | 55% | 32.3 | 15.0 | 4.4 | 4.4 | 1.6 | 1.8 | 0.7 | 2.3 | 23.9 | full tables below |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner | 99% | 36.9<br><sub>38,36,36,32,38</sub> | 29.2<br><sub>21,27,35,16,20</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 7.1<br><sub>8,8,5,8,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 7.6<br><sub>9,11,7,6,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>0,1,2,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.4 | 0.4 | 2.8 | 43.9 |
| Desmond Bane | 99% | 36.6<br><sub>39,38,31,33,34</sub> | 22.6<br><sub>24,15,21,17,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>8,3,2,1,1</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 4.0<br><sub>5,3,3,5,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.5<br><sub>3,5,7,3,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.4 | 2.0 | 31.4 |
| Wendell Carter Jr. | 99% | 34.3<br><sub>28,32,35,26,38</sub> | 14.4<br><sub>10,15,8,9,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 9.4<br><sub>3,8,8,6,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>1,3,2,3,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>1,2,0,1,1</sub> |  | 1.0 | 0.9 | 1.6 | 26.0 |
| Jalen Suggs | 98% | 32.3<br><sub>25,31,30,22,33</sub> | 13.7<br><sub>12,18,8,9,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>6,8,6,4,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>4,4,2,2,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>2,5,2,0,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.9 | 0.6 | 2.6 | 23.6 |
| Tristan da Silva | 91% | 30.9<br><sub>31,27,24,27,33</sub> | 14.3<br><sub>13,12,6,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 4.3<br><sub>6,2,1,3,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>3,0,2,0,1</sub> |  | 2.4<br><sub>3,2,2,4,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.2 | 1.1 | 20.6 |
| Jevon Carter | 91% | 18.9<br><sub>12,16,10,14,19</sub> | 6.8<br><sub>3,6,3,3,9</sub> |  | 1.8<br><sub>2,2,0,2,0</sub> |  | 2.0<br><sub>1,3,0,2,0</sub> |  | 1.1<br><sub>1,2,1,1,3</sub> |  | 0.9 | 0.2 | 0.6 | 10.6 |
| Goga Bitadze | 96% | 17.1<br><sub>20,20,15,15,13</sub> | 6.2<br><sub>10,8,4,1,2</sub> |  | 5.9<br><sub>6,3,4,4,8</sub> |  | 1.3<br><sub>1,1,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.8 | 13.5 |
| Jase Richardson | 63% | 16.9<br><sub>-,-,-,6,1</sub> | 5.9<br><sub>-,-,-,2,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 1.9<br><sub>-,-,-,1,0</sub> |  | 0.6<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 9.7 |
| Nikola Vucevic | 63% | 14.7<br><sub>-,-,23,17,-</sub> | 6.1<br><sub>-,-,15,5,-</sub> |  | 4.3<br><sub>-,-,8,3,-</sub> |  | 1.5<br><sub>-,-,1,3,-</sub> |  | 0.6<br><sub>-,-,3,1,-</sub> |  | 0.3 | 0.4 | 0.6 | 11.9 |
| Jamal Cain | 80% | 13.6<br><sub>15,4,-,9,1</sub> | 5.1<br><sub>2,0,-,2,0</sub> |  | 2.6<br><sub>5,1,-,1,0</sub> |  | 0.6<br><sub>0,0,-,0,0</sub> |  | 0.5<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.6 | 8.4 |
| Alex Morales | 58% | 12.9<br><sub>-,-,-,5,1</sub> | 3.0<br><sub>-,-,-,0,0</sub> |  | 2.3<br><sub>-,-,-,1,0</sub> |  | 1.0<br><sub>-,-,-,2,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.3 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Dybantsa | 98% | 36.2<br><sub>32,38,37,33,41</sub> | 17.8<br><sub>21,23,20,16,20</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>5,12,10,8,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>3,2,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>1,0,2,0,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.4 | 2.3 | 28.9 |
| Anthony Davis | 99% | 35.3<br><sub>35,34,34,33,37</sub> | 23.9<br><sub>23,25,36,22,33</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 11.1<br><sub>4,14,11,7,13</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>0,2,3,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>0,2,0,2,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 1.3 | 1.8 | 2.3 | 37.8 |
| Kyshawn George | 99% | 35.2<br><sub>38,40,35,36,38</sub> | 17.6<br><sub>18,20,11,24,24</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>6,2,7,3,9</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,4,5,4,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,4,1,6,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 1.1 | 2.3 | 26.8 |
| Trae Young | 99% | 34.3<br><sub>33,32,35,28,35</sub> | 17.4<br><sub>13,11,16,11,17</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,1,2,4,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 9.2<br><sub>12,8,5,11,12</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,1,4,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.1 | 29.2 |
| Alex Sarr | 98% | 26.0<br><sub>31,22,20,26,24</sub> | 10.9<br><sub>6,13,3,10,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>4,2,3,9,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,3,0,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,3,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 1.7 | 1.3 | 19.3 |
| Bilal Coulibaly | 99% | 23.7<br><sub>16,26,24,25,22</sub> | 8.0<br><sub>11,3,2,12,10</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>5,8,5,3,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,2,0,1,1</sub> |  | 0.9<br><sub>1,0,0,4,2</sub> |  | 1.1 | 0.9 | 1.1 | 13.4 |
| Khris Middleton | 76% | 17.0<br><sub>18,20,28,20,18</sub> | 5.5<br><sub>9,8,5,6,0</sub> |  | 2.5<br><sub>3,4,2,2,5</sub> |  | 1.5<br><sub>3,1,3,2,0</sub> |  | 0.6<br><sub>2,1,0,2,0</sub> |  | 0.5 | 0.1 | 1.1 | 9.5 |
| Tre Johnson | 97% | 13.5<br><sub>21,8,4,15,8</sub> | 5.3<br><sub>9,0,2,11,0</sub> |  | 1.4<br><sub>1,2,1,2,1</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.6<br><sub>2,0,0,3,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.3 |
| Bub Carrington | 88% | 11.6<br><sub>2,-,6,3,7</sub> | 3.6<br><sub>0,-,3,0,0</sub> |  | 1.3<br><sub>0,-,0,0,2</sub> |  | 1.5<br><sub>0,-,0,0,0</sub> |  | 0.4<br><sub>0,-,1,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.3 |
| Deandre Ayton | 99% | 9.8<br><sub>8,9,11,5,5</sub> | 3.0<br><sub>4,0,0,0,0</sub> |  | 3.1<br><sub>0,3,4,2,2</sub> |  | 0.5<br><sub>1,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 6.5 |
| Will Riley | 91% | 8.3<br><sub>2,10,6,9,5</sub> | 3.7<br><sub>2,0,0,4,5</sub> |  | 1.1<br><sub>1,3,1,3,0</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Anthony Gill | 52% | 7.2<br><sub>2,-,-,3,-</sub> | 2.7<br><sub>2,-,-,0,-</sub> |  | 1.2<br><sub>0,-,-,2,-</sub> |  | 0.5<br><sub>0,-,-,1,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.4 |
| Tre Mann | 63% | 5.9<br><sub>2,-,-,3,1</sub> | 2.6<br><sub>2,-,-,0,0</sub> |  | 0.8<br><sub>0,-,-,0,0</sub> |  | 0.8<br><sub>1,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>if Anthony Black plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner (ORL) | 99% | 35.0<br><sub>38,36,36,32,38</sub> | 26.8<br><sub>21,27,35,16,20</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>8,8,5,8,9</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 6.9<br><sub>9,11,7,6,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>0,1,2,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.4 | 2.6 | 40.3 |
| Desmond Bane (ORL) | 99% | 33.6<br><sub>39,38,31,33,34</sub> | 20.0<br><sub>24,15,21,17,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>8,3,2,1,1</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 3.5<br><sub>5,3,3,5,5</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>3,5,7,3,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.4 | 1.7 | 27.7 |
| Anthony Black (ORL) | 100% | 32.3<br><sub>33,37,37,35,28</sub> | 15.0<br><sub>20,15,13,14,5</sub> | 13.5 · – | 4.4<br><sub>2,2,7,5,4</sub> | 4.5 | 4.4<br><sub>7,6,6,2,2</sub> | 3.5 | 1.6<br><sub>3,2,2,2,0</sub> | 1.5 | 1.8 | 0.7 | 2.3 | 23.9 |
| Wendell Carter Jr. (ORL) | 99% | 31.5<br><sub>28,32,35,26,38</sub> | 13.1<br><sub>10,15,8,9,9</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 8.7<br><sub>3,8,8,6,13</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,3,2,3,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>1,2,0,1,1</sub> |  | 0.9 | 0.9 | 1.5 | 23.8 |
| Jalen Suggs (ORL) | 98% | 28.7<br><sub>25,31,30,22,33</sub> | 11.6<br><sub>12,18,8,9,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>6,8,6,4,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>4,4,2,2,5</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,5,2,0,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.6 | 2.2 | 20.3 |
| Tristan da Silva (ORL) | 91% | 27.5<br><sub>31,27,24,27,33</sub> | 12.4<br><sub>13,12,6,18,16</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.8<br><sub>6,2,1,3,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>3,0,2,0,1</sub> |  | 2.1<br><sub>3,2,2,4,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.7 | 0.2 | 1.0 | 18.0 |
| Goga Bitadze (ORL) | 96% | 14.6<br><sub>20,20,15,15,13</sub> | 5.6<br><sub>10,8,4,1,2</sub> |  | 5.1<br><sub>6,3,4,4,8</sub> |  | 1.1<br><sub>1,1,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.0 | 0.7 | 11.7 |
| Jevon Carter (ORL) | 91% | 14.5<br><sub>12,16,10,14,19</sub> | 5.3<br><sub>3,6,3,3,9</sub> |  | 1.4<br><sub>2,2,0,2,0</sub> |  | 1.5<br><sub>1,3,0,2,0</sub> |  | 0.8<br><sub>1,2,1,1,3</sub> |  | 0.7 | 0.1 | 0.4 | 8.3 |
| Nikola Vucevic (ORL) | 63% | 11.3<br><sub>-,-,23,17,-</sub> | 4.9<br><sub>-,-,15,5,-</sub> |  | 3.4<br><sub>-,-,8,3,-</sub> |  | 1.2<br><sub>-,-,1,3,-</sub> |  | 0.5<br><sub>-,-,3,1,-</sub> |  | 0.2 | 0.3 | 0.5 | 9.6 |
| Jase Richardson (ORL) | 63% | 11.0<br><sub>-,-,-,6,1</sub> | 3.8<br><sub>-,-,-,2,0</sub> |  | 1.3<br><sub>-,-,-,1,0</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 6.2 |
| Jamal Cain (ORL) | 80% | 8.9<br><sub>15,4,-,9,1</sub> | 3.4<br><sub>2,0,-,2,0</sub> |  | 1.8<br><sub>5,1,-,1,0</sub> |  | 0.4<br><sub>0,0,-,0,0</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.6 |
| Alex Morales (ORL) | 58% | 8.0<br><sub>-,-,-,5,1</sub> | 2.0<br><sub>-,-,-,0,0</sub> |  | 1.5<br><sub>-,-,-,1,0</sub> |  | 0.7<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| AJ Dybantsa (WAS) | 98% | 36.2<br><sub>32,38,37,33,41</sub> | 17.8<br><sub>21,23,20,16,20</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 7.6<br><sub>5,12,10,8,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>3,2,6,6,7</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>1,0,2,0,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.3 | 0.4 | 2.3 | 28.9 |
| Anthony Davis (WAS) | 99% | 35.4<br><sub>35,34,34,33,37</sub> | 24.1<br><sub>23,25,36,22,33</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 11.1<br><sub>4,14,11,7,13</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>0,2,3,1,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9<br><sub>0,2,0,2,1</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 1.3 | 1.8 | 2.3 | 37.9 |
| Kyshawn George (WAS) | 99% | 35.3<br><sub>38,40,35,36,38</sub> | 17.6<br><sub>18,20,11,24,24</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>6,2,7,3,9</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>1,4,5,4,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>2,4,1,6,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.1 | 1.1 | 2.3 | 26.9 |
| Trae Young (WAS) | 99% | 34.4<br><sub>33,32,35,28,35</sub> | 17.4<br><sub>13,11,16,11,17</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,1,2,4,0</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 9.2<br><sub>12,8,5,11,12</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>2,1,4,3,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 0.2 | 3.1 | 29.2 |
| Alex Sarr (WAS) | 98% | 26.0<br><sub>31,22,20,26,24</sub> | 10.8<br><sub>6,13,3,10,7</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 6.4<br><sub>4,2,3,9,2</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,3,0,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>1,3,1,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 1.7 | 1.3 | 19.2 |
| Bilal Coulibaly (WAS) | 99% | 23.5<br><sub>16,26,24,25,22</sub> | 7.9<br><sub>11,3,2,12,10</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>5,8,5,3,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>0,2,0,1,1</sub> |  | 0.8<br><sub>1,0,0,4,2</sub> |  | 1.1 | 0.8 | 1.1 | 13.2 |
| Khris Middleton (WAS) | 76% | 17.0<br><sub>18,20,28,20,18</sub> | 5.5<br><sub>9,8,5,6,0</sub> |  | 2.6<br><sub>3,4,2,2,5</sub> |  | 1.5<br><sub>3,1,3,2,0</sub> |  | 0.6<br><sub>2,1,0,2,0</sub> |  | 0.5 | 0.1 | 1.1 | 9.5 |
| Tre Johnson (WAS) | 97% | 13.5<br><sub>21,8,4,15,8</sub> | 5.2<br><sub>9,0,2,11,0</sub> |  | 1.4<br><sub>1,2,1,2,1</sub> |  | 0.7<br><sub>3,0,0,0,0</sub> |  | 0.6<br><sub>2,0,0,3,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.3 |
| Bub Carrington (WAS) | 88% | 11.7<br><sub>2,-,6,3,7</sub> | 3.6<br><sub>0,-,3,0,0</sub> |  | 1.3<br><sub>0,-,0,0,2</sub> |  | 1.5<br><sub>0,-,0,0,0</sub> |  | 0.5<br><sub>0,-,1,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 6.4 |
| Deandre Ayton (WAS) | 99% | 9.8<br><sub>8,9,11,5,5</sub> | 3.0<br><sub>4,0,0,0,0</sub> |  | 3.1<br><sub>0,3,4,2,2</sub> |  | 0.5<br><sub>1,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.4 | 0.4 | 6.6 |
| Will Riley (WAS) | 91% | 8.4<br><sub>2,10,6,9,5</sub> | 3.7<br><sub>2,0,0,4,5</sub> |  | 1.1<br><sub>1,3,1,3,0</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Anthony Gill (WAS) | 52% | 7.2<br><sub>2,-,-,3,-</sub> | 2.6<br><sub>2,-,-,0,-</sub> |  | 1.2<br><sub>0,-,-,2,-</sub> |  | 0.5<br><sub>0,-,-,1,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.3 |
| Tre Mann (WAS) | 63% | 5.9<br><sub>2,-,-,3,1</sub> | 2.6<br><sub>2,-,-,0,0</sub> |  | 0.8<br><sub>0,-,-,0,0</sub> |  | 0.7<br><sub>1,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

</details>


### BKN @ CHA
Out: PJ Hall (CHA), Kon Knueppel (CHA), Dennis Schroder (CHA), Nolan Traore (BKN), Moritz Wagner (BKN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 104.3–110.2 | BKN 34% | 2.97 / 1.51 | CHA -6.5 | 214.5 | CHA -5.5 covers 52%; o213.5 52% |
| Expected (weighted by chance each plays) | 104.8–111.3 | BKN 32% | 3.08 / 1.48 | CHA -6.5 | 216.5 | CHA -5.5 covers 53%; o213.5 56% |
| if Grayson Allen plays | 105.4–112.1 | BKN 32% | 3.15 / 1.47 | CHA -6.5 | 217.5 | CHA -5.5 covers 54%; o213.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Grayson Allen (CHA) | Questionable | 55% | 23.5 | 12.7 | 2.7 | 3.4 | 2.2 | 0.9 | 0.3 | 1.7 | 18.7 | full tables below |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 99% | 34.6<br><sub>34,27,39,35,39</sub> | 21.6<br><sub>33,17,27,29,28</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.0<br><sub>6,0,9,4,9</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 4.3<br><sub>1,4,6,4,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,3,1,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.2 | 3.1 | 32.0 |
| Michael Porter Jr. | 91% | 33.0<br><sub>40,27,34,31,34</sub> | 18.8<br><sub>25,5,16,11,12</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>6,3,4,6,11</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,1,5,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.6<br><sub>2,1,3,0,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.3 | 1.8 | 27.0 |
| Day'Ron Sharpe | 99% | 26.1<br><sub>25,22,26,26,31</sub> | 10.1<br><sub>6,6,17,6,11</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,5,11,5,14</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,1,2,7,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,0,1</sub> |  | 1.2 | 0.8 | 1.6 | 21.3 |
| Egor Demin | 98% | 24.5<br><sub>26,31,21,25,25</sub> | 10.9<br><sub>9,22,6,10,15</sub> |  | 2.7<br><sub>3,4,3,3,3</sub> |  | 2.9<br><sub>4,4,2,4,4</sub> |  | 1.8<br><sub>2,3,0,2,0</sub> |  | 0.8 | 0.3 | 1.5 | 16.5 |
| Mikel Brown Jr. | 98% | 22.9<br><sub>18,27,24,29,23</sub> | 11.0<br><sub>3,15,18,17,6</sub> |  | 2.1<br><sub>1,1,1,5,2</sub> |  | 3.2<br><sub>5,4,0,7,2</sub> |  | 1.6<br><sub>1,2,3,4,0</sub> |  | 0.7 | 0.2 | 1.9 | 16.4 |
| Noah Clowney | 99% | 22.8<br><sub>24,19,22,26,27</sub> | 8.4<br><sub>9,7,0,13,17</sub> |  | 3.5<br><sub>3,3,2,2,5</sub> |  | 1.1<br><sub>3,1,2,1,1</sub> |  | 1.1<br><sub>1,1,0,3,3</sub> |  | 0.6 | 0.5 | 0.9 | 13.1 |
| Danny Wolf | 91% | 20.6<br><sub>11,23,26,25,19</sub> | 8.5<br><sub>3,6,20,11,5</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>2,6,5,5,0</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,2,2,4,1</sub> |  | 1.1<br><sub>1,1,4,3,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.5 | 0.4 | 1.0 | 14.4 |
| Keon Ellis | 93% | 17.6<br><sub>20,6,8,16,23</sub> | 4.6<br><sub>8,3,0,6,7</sub> |  | 1.7<br><sub>2,1,1,0,2</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 0.6<br><sub>2,1,0,2,1</sub> |  | 0.9 | 0.5 | 0.5 | 7.4 |
| Ben Saraf | 52% | 11.2<br><sub>-,-,-,-,-</sub> | 4.5<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.2 | 7.5 |
| Grant Nelson | 88% | 11.0<br><sub>-,-,-,8,13</sub> | 3.7<br><sub>-,-,-,2,1</sub> |  | 2.5<br><sub>-,-,-,1,6</sub> |  | 0.8<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 7.0 |
| Chaney Johnson | 76% | 9.5<br><sub>1,6,-,-,-</sub> | 2.7<br><sub>0,2,-,-,-</sub> |  | 1.5<br><sub>0,2,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 4.7 |
| Terance Mann | 67% | 9.1<br><sub>-,5,-,3,2</sub> | 2.4<br><sub>-,0,-,0,0</sub> |  | 1.1<br><sub>-,1,-,0,0</sub> |  | 0.8<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.3 |
| Tyler Bilodeau | 3% | 8.5 | 3.8 |  | 1.5 |  | 0.7 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Josh Minott | 52% | 7.5<br><sub>-,4,-,2,-</sub> | 3.7<br><sub>-,0,-,0,-</sub> |  | 1.2<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.3 |
| Drake Powell | 58% | 7.1<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |
| Joshua Jefferson | 80% | 6.1<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.0 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naz Reid | 99% | 31.7<br><sub>27,42,39,38,35</sub> | 18.9<br><sub>17,23,12,24,18</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 7.8<br><sub>4,11,10,6,8</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 2.9<br><sub>3,4,3,3,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>3,4,2,3,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.9 | 2.5 | 29.6 |
| Moussa Diabate | 99% | 30.5<br><sub>26,38,30,35,38</sub> | 10.4<br><sub>12,5,21,10,14</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 10.6<br><sub>12,16,15,10,14</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 1.1 | 1.6 | 23.6 |
| Brandon Miller | 99% | 30.5<br><sub>24,32,33,35,34</sub> | 22.7<br><sub>5,28,19,20,35</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>2,2,8,3,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,4,3,5,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,5,5,4,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.6 | 2.8 | 30.7 |
| Sion James | 99% | 27.8<br><sub>35,30,32,28,26</sub> | 7.0<br><sub>3,3,9,5,5</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>8,6,1,4,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 3.3<br><sub>4,4,2,4,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>1,0,1,1,1</sub> |  | 1.0 | 0.1 | 1.3 | 14.3 |
| Coby White | 98% | 24.1<br><sub>20,26,26,28,25</sub> | 16.8<br><sub>21,19,11,21,11</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>0,3,4,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 4.7<br><sub>1,4,9,2,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,2,0,5,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.2 | 2.6 | 24.5 |
| Christian Anderson | 93% | 22.5<br><sub>18,14,21,25,28</sub> | 10.5<br><sub>16,5,4,25,15</sub> |  | 2.2<br><sub>3,1,1,2,1</sub> |  | 3.5<br><sub>2,4,2,3,4</sub> |  | 1.7<br><sub>4,1,0,6,3</sub> |  | 0.7 | 0.3 | 1.7 | 16.2 |
| Royce O'Neale | 99% | 20.7<br><sub>19,34,21,13,23</sub> | 6.3<br><sub>3,13,9,0,0</sub> |  | 3.4<br><sub>3,4,1,1,6</sub> |  | 1.4<br><sub>1,1,0,1,2</sub> |  | 1.1<br><sub>1,4,3,0,0</sub> |  | 0.8 | 0.3 | 0.7 | 11.1 |
| Grant Williams | 88% | 19.4<br><sub>20,30,-,-,15</sub> | 7.7<br><sub>11,12,-,-,0</sub> |  | 3.2<br><sub>2,4,-,-,1</sub> |  | 1.5<br><sub>1,0,-,-,0</sub> |  | 1.1<br><sub>3,2,-,-,0</sub> |  | 0.7 | 0.4 | 0.9 | 12.4 |
| Ryan Kalkbrenner | 92% | 14.8<br><sub>18,14,17,9,-</sub> | 4.6<br><sub>5,6,6,0,-</sub> |  | 4.0<br><sub>5,3,6,2,-</sub> |  | 0.8<br><sub>1,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.4 | 1.1 | 0.7 | 9.4 |
| Tidjane Salaun | 98% | 12.7<br><sub>5,5,13,17,8</sub> | 4.9<br><sub>0,0,4,0,4</sub> |  | 2.9<br><sub>2,1,2,5,1</sub> |  | 0.7<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.4 |
| Liam McNeeley | 58% | 9.9<br><sub>2,-,7,9,-</sub> | 4.1<br><sub>0,-,2,3,-</sub> |  | 1.7<br><sub>0,-,1,2,-</sub> |  | 0.7<br><sub>0,-,0,0,-</sub> |  | 0.4<br><sub>0,-,0,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 6.5 |
| Hannes Steinbach | 64% | 8.8<br><sub>-,-,-,4,8</sub> | 3.0<br><sub>-,-,-,3,3</sub> |  | 2.5<br><sub>-,-,-,1,3</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.4 | 0.5 | 5.8 |

</details>

<details><summary>if Grayson Allen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle (BKN) | 99% | 34.5<br><sub>34,27,39,35,39</sub> | 21.7<br><sub>33,17,27,29,28</sub> | 19.5 · –<br><sub>o 51% · u 49%</sub> | 6.1<br><sub>6,0,9,4,9</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 4.3<br><sub>1,4,6,4,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>2,3,1,2,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.2 | 3.1 | 32.1 |
| Michael Porter Jr. (BKN) | 91% | 32.9<br><sub>40,27,34,31,34</sub> | 18.9<br><sub>25,5,16,11,12</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>6,3,4,6,11</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>2,1,5,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.6<br><sub>2,1,3,0,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.0 | 0.3 | 1.8 | 27.1 |
| Day'Ron Sharpe (BKN) | 99% | 26.0<br><sub>25,22,26,26,31</sub> | 10.1<br><sub>6,6,17,6,11</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,5,11,5,14</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,1,2,7,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 0.3<br><sub>0,0,0,0,1</sub> |  | 1.2 | 0.8 | 1.6 | 21.3 |
| Egor Demin (BKN) | 98% | 24.5<br><sub>26,31,21,25,25</sub> | 11.1<br><sub>9,22,6,10,15</sub> |  | 2.7<br><sub>3,4,3,3,3</sub> |  | 2.9<br><sub>4,4,2,4,4</sub> |  | 1.8<br><sub>2,3,0,2,0</sub> |  | 0.8 | 0.3 | 1.5 | 16.7 |
| Mikel Brown Jr. (BKN) | 98% | 22.9<br><sub>18,27,24,29,23</sub> | 11.0<br><sub>3,15,18,17,6</sub> |  | 2.1<br><sub>1,1,1,5,2</sub> |  | 3.3<br><sub>5,4,0,7,2</sub> |  | 1.6<br><sub>1,2,3,4,0</sub> |  | 0.7 | 0.2 | 1.9 | 16.4 |
| Noah Clowney (BKN) | 99% | 22.7<br><sub>24,19,22,26,27</sub> | 8.5<br><sub>9,7,0,13,17</sub> |  | 3.5<br><sub>3,3,2,2,5</sub> |  | 1.1<br><sub>3,1,2,1,1</sub> |  | 1.2<br><sub>1,1,0,3,3</sub> |  | 0.6 | 0.5 | 0.8 | 13.2 |
| Danny Wolf (BKN) | 91% | 20.6<br><sub>11,23,26,25,19</sub> | 8.5<br><sub>3,6,20,11,5</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>2,6,5,5,0</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>1,2,2,4,1</sub> |  | 1.1<br><sub>1,1,4,3,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.5 | 0.4 | 1.0 | 14.5 |
| Keon Ellis (BKN) | 93% | 17.6<br><sub>20,6,8,16,23</sub> | 4.6<br><sub>8,3,0,6,7</sub> |  | 1.7<br><sub>2,1,1,0,2</sub> |  | 1.2<br><sub>0,0,1,0,3</sub> |  | 0.6<br><sub>2,1,0,2,1</sub> |  | 0.9 | 0.4 | 0.5 | 7.4 |
| Ben Saraf (BKN) | 52% | 11.4<br><sub>-,-,-,-,-</sub> | 4.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 1.2 | 7.6 |
| Grant Nelson (BKN) | 88% | 11.0<br><sub>-,-,-,8,13</sub> | 3.6<br><sub>-,-,-,2,1</sub> |  | 2.5<br><sub>-,-,-,1,6</sub> |  | 0.8<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 6.9 |
| Chaney Johnson (BKN) | 76% | 9.5<br><sub>1,6,-,-,-</sub> | 2.7<br><sub>0,2,-,-,-</sub> |  | 1.5<br><sub>0,2,-,-,-</sub> |  | 0.5<br><sub>0,1,-,-,-</sub> |  | 0.2<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 4.7 |
| Terance Mann (BKN) | 67% | 9.1<br><sub>-,5,-,3,2</sub> | 2.4<br><sub>-,0,-,0,0</sub> |  | 1.1<br><sub>-,1,-,0,0</sub> |  | 0.8<br><sub>-,0,-,0,0</sub> |  | 0.1<br><sub>-,0,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.3 |
| Tyler Bilodeau (BKN) | 3% | 8.5 | 3.7 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Josh Minott (BKN) | 52% | 7.5<br><sub>-,4,-,2,-</sub> | 3.7<br><sub>-,0,-,0,-</sub> |  | 1.2<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 5.3 |
| Drake Powell (BKN) | 58% | 7.1<br><sub>-,-,-,-,-</sub> | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |
| Joshua Jefferson (BKN) | 80% | 6.0<br><sub>-,-,-,-,-</sub> | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 1.0 |
| Naz Reid (CHA) | 99% | 29.3<br><sub>27,42,39,38,35</sub> | 16.9<br><sub>17,23,12,24,18</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>4,11,10,6,8</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>3,4,3,3,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>3,4,2,3,2</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.8 | 2.2 | 27.0 |
| Brandon Miller (CHA) | 99% | 28.2<br><sub>24,32,33,35,34</sub> | 20.7<br><sub>5,28,19,20,35</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>2,2,8,3,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>4,4,3,5,1</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>1,5,5,4,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.9 | 0.5 | 2.3 | 28.0 |
| Moussa Diabate (CHA) | 99% | 27.9<br><sub>26,38,30,35,38</sub> | 10.0<br><sub>12,5,21,10,14</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 9.8<br><sub>12,16,15,10,14</sub> | 10.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,2,2,3,2</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.0 | 1.5 | 22.3 |
| Sion James (CHA) | 99% | 24.5<br><sub>35,30,32,28,26</sub> | 6.0<br><sub>3,3,9,5,5</sub> | 5.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>8,6,1,4,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.9<br><sub>4,4,2,4,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 0.9<br><sub>1,0,1,1,1</sub> |  | 0.9 | 0.1 | 1.1 | 12.7 |
| Grayson Allen (CHA) | 100% | 23.5<br><sub>25,-,-,-,-</sub> | 12.7<br><sub>12,-,-,-,-</sub> | 12.5 · – | 2.7<br><sub>5,-,-,-,-</sub> | 2.5 | 3.4<br><sub>4,-,-,-,-</sub> |  | 2.2<br><sub>2,-,-,-,-</sub> | 2.5 | 0.9 | 0.3 | 1.7 | 18.7 |
| Coby White (CHA) | 98% | 22.1<br><sub>20,26,26,28,25</sub> | 15.4<br><sub>21,19,11,21,11</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>0,3,4,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 4.4<br><sub>1,4,9,2,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>2,2,0,5,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.2 | 2.3 | 22.7 |
| Christian Anderson (CHA) | 93% | 19.6<br><sub>18,14,21,25,28</sub> | 9.6<br><sub>16,5,4,25,15</sub> |  | 1.9<br><sub>3,1,1,2,1</sub> |  | 3.0<br><sub>2,4,2,3,4</sub> |  | 1.4<br><sub>4,1,0,6,3</sub> |  | 0.7 | 0.2 | 1.5 | 14.5 |
| Royce O'Neale (CHA) | 99% | 19.3<br><sub>19,34,21,13,23</sub> | 6.1<br><sub>3,13,9,0,0</sub> |  | 3.2<br><sub>3,4,1,1,6</sub> |  | 1.3<br><sub>1,1,0,1,2</sub> |  | 1.0<br><sub>1,4,3,0,0</sub> |  | 0.8 | 0.2 | 0.6 | 10.6 |
| Grant Williams (CHA) | 88% | 18.7<br><sub>20,30,-,-,15</sub> | 7.6<br><sub>11,12,-,-,0</sub> |  | 3.1<br><sub>2,4,-,-,1</sub> |  | 1.4<br><sub>1,0,-,-,0</sub> |  | 1.1<br><sub>3,2,-,-,0</sub> |  | 0.6 | 0.4 | 0.8 | 12.1 |
| Ryan Kalkbrenner (CHA) | 92% | 12.2<br><sub>18,14,17,9,-</sub> | 3.9<br><sub>5,6,6,0,-</sub> |  | 3.4<br><sub>5,3,6,2,-</sub> |  | 0.7<br><sub>1,1,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.9 | 0.6 | 8.1 |
| Tidjane Salaun (CHA) | 98% | 11.2<br><sub>5,5,13,17,8</sub> | 4.4<br><sub>0,0,4,0,4</sub> |  | 2.5<br><sub>2,1,2,5,1</sub> |  | 0.6<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 7.5 |
| Hannes Steinbach (CHA) | 64% | 7.9<br><sub>-,-,-,4,8</sub> | 2.8<br><sub>-,-,-,3,3</sub> |  | 2.3<br><sub>-,-,-,1,3</sub> |  | 0.4<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.4 | 0.4 | 5.4 |
| Liam McNeeley (CHA) | 58% | 7.8<br><sub>2,-,7,9,-</sub> | 3.4<br><sub>0,-,2,3,-</sub> |  | 1.4<br><sub>0,-,1,2,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.3<br><sub>0,-,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |

</details>


### IND @ CHI
Out: Tobe Awaka (CHI), Norman Powell (CHI), Jaylin Sellers (CHI), Caleb Wilson (CHI), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND)

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 96% | 35.1<br><sub>34,33,30,33,35</sub> | 26.1<br><sub>31,24,21,25,20</sub> |  | 6.8<br><sub>2,4,7,6,8</sub> |  | 4.3<br><sub>2,3,2,1,5</sub> |  | 1.8<br><sub>0,2,2,3,2</sub> |  | 1.3 | 0.4 | 2.2 | 37.2 |
| Andrew Nembhard | 91% | 34.6<br><sub>-,-,26,32,38</sub> | 17.6<br><sub>-,-,12,16,15</sub> |  | 3.2<br><sub>-,-,3,2,2</sub> |  | 8.8<br><sub>-,-,8,8,6</sub> |  | 2.0<br><sub>-,-,3,2,2</sub> |  | 1.4 | 0.2 | 2.7 | 29.6 |
| Aaron Nesmith | 72% | 29.6<br><sub>36,29,29,32,-</sub> | 13.0<br><sub>12,2,2,9,-</sub> |  | 4.1<br><sub>4,3,10,2,-</sub> |  | 2.3<br><sub>4,3,7,2,-</sub> |  | 1.8<br><sub>0,0,0,0,-</sub> |  | 0.9 | 0.5 | 1.2 | 19.4 |
| Ivica Zubac | 91% | 27.0<br><sub>22,24,27,31,26</sub> | 13.2<br><sub>8,4,21,10,14</sub> |  | 10.4<br><sub>5,3,10,14,15</sub> |  | 1.8<br><sub>2,4,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 1.5 | 25.4 |
| Kelly Oubre Jr. | 91% | 26.9<br><sub>29,23,23,27,28</sub> | 13.3<br><sub>16,17,17,15,20</sub> |  | 4.4<br><sub>4,4,6,5,4</sub> |  | 1.4<br><sub>2,0,0,0,2</sub> |  | 1.2<br><sub>2,2,3,0,4</sub> |  | 1.0 | 0.7 | 1.1 | 19.1 |
| Obi Toppin | 91% | 21.2<br><sub>14,17,26,22,24</sub> | 12.6<br><sub>5,6,17,9,17</sub> |  | 4.5<br><sub>2,1,3,5,6</sub> |  | 2.1<br><sub>1,1,2,1,4</sub> |  | 1.4<br><sub>0,0,2,0,2</sub> |  | 0.7 | 0.2 | 1.0 | 19.2 |
| Quenton Jackson | 99% | 20.5<br><sub>30,22,18,17,20</sub> | 9.3<br><sub>15,15,3,2,9</sub> |  | 3.0<br><sub>6,2,2,1,3</sub> |  | 3.1<br><sub>8,3,2,3,0</sub> |  | 0.9<br><sub>1,2,1,0,1</sub> |  | 1.2 | 0.2 | 1.2 | 15.4 |
| Braden Smith | 83% | 16.9<br><sub>-,18,11,18,24</sub> | 5.4<br><sub>-,8,5,6,6</sub> |  | 1.8<br><sub>-,5,3,1,2</sub> |  | 3.6<br><sub>-,3,5,4,6</sub> |  | 0.4<br><sub>-,2,1,0,1</sub> |  | 1.0 | 0.3 | 0.9 | 10.8 |
| Jalen Slawson | 91% | 14.6<br><sub>14,12,14,14,20</sub> | 4.9<br><sub>8,5,4,7,16</sub> |  | 3.4<br><sub>5,4,2,3,10</sub> |  | 1.4<br><sub>2,2,2,0,2</sub> |  | 0.4<br><sub>1,1,0,0,3</sub> |  | 0.9 | 1.0 | 0.7 | 9.7 |
| Jarace Walker | 91% | 14.0<br><sub>14,17,11,1,14</sub> | 5.9<br><sub>2,1,8,0,4</sub> |  | 3.2<br><sub>5,3,1,0,8</sub> |  | 1.6<br><sub>2,1,3,0,3</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 10.7 |
| Kobe Brown | 88% | 10.2<br><sub>3,2,-,-,7</sub> | 3.6<br><sub>0,0,-,-,4</sub> |  | 1.9<br><sub>0,0,-,-,0</sub> |  | 0.9<br><sub>0,0,-,-,1</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.4 |
| Jay Huff | 71% | 9.9<br><sub>18,15,1,1,-</sub> | 4.4<br><sub>11,5,0,2,-</sub> |  | 2.0<br><sub>0,3,0,0,-</sub> |  | 0.7<br><sub>2,0,0,0,-</sub> |  | 0.4<br><sub>3,0,0,0,-</sub> |  | 0.3 | 0.7 | 0.5 | 7.1 |
| Larry Nance Jr. | 98% | 9.6<br><sub>7,9,11,11,4</sub> | 3.1<br><sub>4,3,7,5,0</sub> |  | 2.0<br><sub>2,1,2,3,0</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.3<br><sub>1,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 5.7 |
| Johnny Furphy | 5% | 9.5 | 2.7 |  | 2.4 |  | 0.9 |  | 0.2 |  | 0.5 | 0.1 | 0.4 | 6.0 |

</details>

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Matas Buzelis | 99% | 31.2<br><sub>30,25,38,27,34</sub> | 18.9<br><sub>25,9,21,15,24</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>5,5,5,6,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>4,1,3,0,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.5<br><sub>5,1,4,4,0</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 1.1 | 2.2 | 27.3 |
| Josh Giddey | 99% | 30.9<br><sub>28,23,41,22,34</sub> | 15.5<br><sub>18,2,23,4,12</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 7.8<br><sub>14,6,14,2,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 10.0<br><sub>9,7,22,11,7</sub> | 8.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,0,2,0,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.6 | 3.0 | 33.3 |
| Isaac Okoro | 99% | 29.3<br><sub>25,29,42,27,31</sub> | 10.8<br><sub>12,9,11,12,10</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,7,1,4,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.0<br><sub>4,1,2,3,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4<br><sub>4,1,2,3,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.4 | 0.9 | 16.1 |
| Jalen Smith | 92% | 27.1<br><sub>21,-,34,25,-</sub> | 15.0<br><sub>14,-,26,11,-</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 8.6<br><sub>6,-,4,6,-</sub> | 7.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>3,-,1,4,-</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>2,-,6,1,-</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.8 | 0.9 | 1.1 | 25.6 |
| Buddy Hield | 91% | 25.5<br><sub>19,23,40,27,27</sub> | 13.8<br><sub>11,15,33,17,9</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>1,4,7,5,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>2,0,6,0,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>3,4,7,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 1.2 | 20.0 |
| Nic Claxton | 98% | 24.2<br><sub>22,29,-,23,29</sub> | 10.5<br><sub>14,11,-,6,10</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 6.4<br><sub>4,7,-,6,2</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>1,1,-,0,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.0 | 1.2 | 19.0 |
| Tre Jones | 99% | 22.0<br><sub>16,25,12,27,20</sub> | 13.5<br><sub>10,12,9,16,10</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>2,1,2,4,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>6,7,4,9,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.5<br><sub>0,0,0,1,0</sub> |  | 1.0 | 0.2 | 1.4 | 21.3 |
| Patrick Williams | 91% | 19.1<br><sub>13,23,16,19,15</sub> | 7.3<br><sub>2,6,2,7,11</sub> |  | 3.0<br><sub>1,3,2,5,1</sub> |  | 1.4<br><sub>2,1,0,2,0</sub> |  | 0.9<br><sub>0,0,0,1,3</sub> |  | 0.7 | 0.4 | 0.9 | 11.7 |
| Jordan Hawkins | 71% | 16.5<br><sub>-,-,14,18,21</sub> | 7.6<br><sub>-,-,6,19,10</sub> |  | 2.1<br><sub>-,-,1,1,3</sub> |  | 1.2<br><sub>-,-,1,2,2</sub> |  | 1.1<br><sub>-,-,2,4,3</sub> |  | 0.5 | 0.3 | 0.6 | 10.9 |
| Zach Collins | 67% | 16.3<br><sub>11,15,17,-,19</sub> | 6.7<br><sub>3,6,5,-,6</sub> |  | 4.6<br><sub>2,2,1,-,3</sub> |  | 1.7<br><sub>0,4,0,-,2</sub> |  | 0.5<br><sub>1,0,1,-,2</sub> |  | 0.5 | 0.5 | 0.9 | 13.0 |
| Noa Essengue | 91% | 11.8<br><sub>15,15,11,4,11</sub> | 5.4<br><sub>5,8,9,6,5</sub> |  | 2.7<br><sub>3,4,4,2,0</sub> |  | 0.6<br><sub>0,0,0,0,2</sub> |  | 0.5<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.2 | 0.7 | 8.7 |
| Leonard Miller | 48% | 11.3<br><sub>7,-,-,-,-</sub> | 5.5<br><sub>4,-,-,-,-</sub> |  | 2.9<br><sub>2,-,-,-,-</sub> |  | 0.7<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.3 | 0.6 | 9.1 |
| Orlando Robinson | 25% | 8.4<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.9 |

</details>


### OKC @ MIL
Out: Kasparas Jakucionis (MIL), Chet Holmgren (OKC), Aday Mara (OKC), Nikola Topic (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 99% | 35.3<br><sub>36,37,-,38,37</sub> | 35.1<br><sub>34,40,-,38,32</sub> | 32.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>5,3,-,5,3</sub> |  | 6.1<br><sub>3,8,-,7,5</sub> |  | 2.3<br><sub>1,4,-,4,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.9 | 2.5 | 45.6 |
| Ajay Mitchell | 99% | 30.8<br><sub>34,31,22,35,31</sub> | 18.0<br><sub>13,8,17,12,25</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>6,2,3,4,3</sub> |  | 4.4<br><sub>6,4,3,3,3</sub> |  | 1.3<br><sub>0,1,2,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.6 | 26.4 |
| Jared McCain | 99% | 30.6<br><sub>33,30,29,36,28</sub> | 16.6<br><sub>18,18,20,13,9</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>3,3,2,5,1</sub> |  | 2.0<br><sub>1,0,3,0,1</sub> |  | 2.8<br><sub>4,3,2,1,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.2 | 1.4 | 22.2 |
| Isaiah Hartenstein | 99% | 29.2<br><sub>27,28,23,30,31</sub> | 10.8<br><sub>6,5,2,18,8</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 12.5<br><sub>17,8,8,9,16</sub> |  | 4.7<br><sub>6,4,4,3,6</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.6 | 28.0 |
| Kenrich Williams | 98% | 25.5<br><sub>23,28,26,26,25</sub> | 10.4<br><sub>10,6,12,20,13</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.3<br><sub>5,2,4,9,5</sub> |  | 2.2<br><sub>1,4,2,2,1</sub> |  | 1.6<br><sub>0,1,2,4,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.2 | 0.8 | 18.0 |
| Bennett Stirtz | 99% | 23.2<br><sub>17,25,32,19,24</sub> | 9.2<br><sub>6,18,21,5,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>0,2,3,9,1</sub> |  | 2.0<br><sub>2,2,5,3,2</sub> |  | 1.7<br><sub>2,4,5,1,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8 | 0.3 | 0.7 | 13.7 |
| Micah Peavy | 96% | 23.1<br><sub>-,9,31,24,25</sub> | 6.2<br><sub>-,2,9,7,2</sub> |  | 4.7<br><sub>-,2,6,3,7</sub> |  | 0.9<br><sub>-,0,1,2,0</sub> |  | 0.6<br><sub>-,0,1,1,0</sub> |  | 0.9 | 0.3 | 0.7 | 11.8 |
| Alex Caruso | 67% | 21.3<br><sub>9,-,-,-,26</sub> | 8.9<br><sub>5,-,-,-,11</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>0,-,-,-,2</sub> |  | 2.8<br><sub>1,-,-,-,2</sub> |  | 1.4<br><sub>0,-,-,-,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.6 | 0.9 | 14.9 |
| Josh Dix | 58% | 17.5<br><sub>-,-,32,16,-</sub> | 4.8<br><sub>-,-,13,0,-</sub> |  | 2.1<br><sub>-,-,5,1,-</sub> |  | 1.1<br><sub>-,-,4,1,-</sub> |  | 0.5<br><sub>-,-,3,0,-</sub> |  | 0.5 | 0.2 | 0.4 | 8.1 |
| Nique Clifford | 76% | 15.3<br><sub>13,15,26,6,12</sub> | 5.3<br><sub>7,4,11,0,0</sub> |  | 2.4<br><sub>0,5,3,0,2</sub> |  | 1.2<br><sub>0,1,0,0,0</sub> |  | 0.4<br><sub>1,0,1,0,0</sub> |  | 0.7 | 0.2 | 0.7 | 8.9 |
| Brooks Barnhizer | 52% | 10.9<br><sub>-,-,19,9,-</sub> | 3.0<br><sub>-,-,8,7,-</sub> |  | 2.5<br><sub>-,-,4,4,-</sub> |  | 0.8<br><sub>-,-,2,0,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.4 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 99% | 30.8<br><sub>24,31,40,37,37</sub> | 19.2<br><sub>8,19,50,32,28</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>2,4,11,6,2</sub> |  | 4.4<br><sub>4,3,7,8,5</sub> |  | 2.3<br><sub>0,4,7,4,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.3 | 2.5 | 27.9 |
| Kyle Kuzma | 99% | 25.4<br><sub>30,-,33,32,31</sub> | 12.5<br><sub>26,-,12,18,13</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>5,-,5,5,3</sub> |  | 2.3<br><sub>1,-,1,3,2</sub> |  | 1.5<br><sub>2,-,2,2,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.6 | 0.4 | 1.6 | 19.3 |
| Jaime Jaquez Jr. | 99% | 24.9<br><sub>23,22,25,25,35</sub> | 13.1<br><sub>10,9,9,3,21</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>2,1,0,4,5</sub> |  | 3.1<br><sub>5,2,1,2,4</sub> |  | 1.4<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.2 | 1.8 | 20.5 |
| Myles Turner | 99% | 23.8<br><sub>21,-,26,28,26</sub> | 9.3<br><sub>4,-,5,27,3</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.4<br><sub>5,-,6,11,6</sub> |  | 1.8<br><sub>4,-,5,1,2</sub> |  | 1.2<br><sub>0,-,1,5,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.5 | 1.6 | 1.3 | 16.5 |
| Brayden Burries | 99% | 21.7<br><sub>25,28,26,29,22</sub> | 10.5<br><sub>20,14,26,14,3</sub> |  | 5.0<br><sub>7,3,8,10,3</sub> |  | 2.4<br><sub>1,3,4,4,3</sub> |  | 1.0<br><sub>3,2,2,1,0</sub> |  | 0.8 | 0.2 | 1.5 | 17.9 |
| Ryan Rollins | 99% | 21.4<br><sub>-,21,28,22,19</sub> | 10.4<br><sub>-,15,8,6,2</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>-,3,6,1,3</sub> |  | 3.4<br><sub>-,6,1,3,3</sub> |  | 1.3<br><sub>-,1,0,0,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.3 | 1.9 | 17.2 |
| Kel'el Ware | 98% | 17.5<br><sub>17,26,22,23,22</sub> | 8.0<br><sub>11,11,6,9,13</sub> |  | 5.8<br><sub>3,5,8,3,14</sub> |  | 1.0<br><sub>1,0,3,0,2</sub> |  | 0.6<br><sub>1,2,0,1,1</sub> |  | 0.5 | 0.9 | 1.1 | 14.8 |
| Nate Ament | 98% | 16.5<br><sub>17,35,14,25,21</sub> | 6.8<br><sub>7,18,2,7,8</sub> |  | 2.9<br><sub>4,9,1,4,3</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.7<br><sub>0,2,0,0,2</sub> |  | 0.4 | 0.3 | 0.9 | 10.4 |
| Cormac Ryan | 52% | 14.2<br><sub>-,-,-,-,-</sub> | 7.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.2 | 0.9 | 10.4 |
| Pete Nance | 96% | 11.7<br><sub>-,28,-,-,-</sub> | 4.0<br><sub>-,7,-,-,-</sub> |  | 2.0<br><sub>-,3,-,-,-</sub> |  | 0.9<br><sub>-,3,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.8 |
| AJ Green | 67% | 9.1<br><sub>14,-,12,-,5</sub> | 3.6<br><sub>11,-,9,-,0</sub> |  | 0.9<br><sub>0,-,0,-,0</sub> |  | 0.6<br><sub>1,-,0,-,0</sub> |  | 0.5<br><sub>3,-,3,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.1 |
| Kam Jones | 52% | 9.0<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 1.9<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.6 | 5.5 |
| Caris LeVert | 66% | 8.9<br><sub>8,11,5,8,12</sub> | 4.0<br><sub>8,3,0,0,2</sub> |  | 1.2<br><sub>3,3,1,0,1</sub> |  | 1.0<br><sub>2,1,0,0,2</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.2 |
| Jericho Sims | 52% | 7.8<br><sub>18,10,-,-,-</sub> | 2.0<br><sub>4,0,-,-,-</sub> |  | 2.1<br><sub>6,0,-,-,-</sub> |  | 0.6<br><sub>2,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.7 |
| Ousmane Dieng | 58% | 7.6<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.3 |
| Gary Trent Jr. | 58% | 7.4<br><sub>16,7,-,5,-</sub> | 3.6<br><sub>1,0,-,0,-</sub> |  | 0.6<br><sub>1,1,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.4<br><sub>0,0,-,0,-</sub> |  | 0.2 | 0.0 | 0.3 | 4.6 |
| Bogoljub Markovic | 38% | 5.6<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 4.3 |

</details>


### PHI @ HOU
Out: Jaylen Brown (PHI), Joel Embiid (PHI), Ariel Hukporti (PHI), LeBron James (PHI), Dean Wade (PHI)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson AST over 3.5 (4+) | PHI @ HOU | draftkings | 2.23 | 2.23 | 1.75 | 57.1% | 42.2% | 44.9% | +0.1% | +27.3% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.3–117.4 | PHI 26% | 3.85 / 1.35 | HOU -9.5 | 225.5 | HOU -12.5 covers 40%; o219.5 63% |
| Expected (weighted by chance each plays) | 108.6–117.6 | PHI 26% | 3.78 / 1.36 | HOU -9.5 | 226.5 | HOU -12.5 covers 41%; o219.5 64% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Steven Adams (HOU) | Questionable | 55% | 14.8 | 3.8 | 5.4 | 1.0 | 0.0 | 0.4 | 0.5 | 0.7 | 10.3 | small |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 88% | 38.4<br><sub>35,-,36,35,37</sub> | 29.8<br><sub>24,-,17,22,30</sub> | 27.5 · –<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,-,4,2,4</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>9,-,4,5,6</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>4,-,0,2,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.5 | 3.0 | 40.3 |
| VJ Edgecombe | 98% | 38.1<br><sub>33,43,38,35,36</sub> | 19.0<br><sub>14,24,16,12,18</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 6.6<br><sub>9,8,3,7,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 5.5<br><sub>4,6,6,7,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,4,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7 | 0.5 | 2.6 | 31.1 |
| Kentavious Caldwell-Pope | 99% | 30.2<br><sub>31,32,35,17,28</sub> | 9.1<br><sub>0,8,11,2,5</sub> |  | 3.2<br><sub>2,8,1,3,1</sub> |  | 2.6<br><sub>3,1,2,1,3</sub> |  | 1.2<br><sub>0,2,3,0,1</sub> |  | 1.2 | 0.3 | 1.1 | 14.9 |
| Anfernee Simons | 99% | 28.6<br><sub>26,38,26,18,15</sub> | 15.2<br><sub>9,18,18,3,6</sub> |  | 2.5<br><sub>1,2,0,0,1</sub> |  | 2.4<br><sub>2,2,1,0,1</sub> |  | 2.4<br><sub>1,3,4,0,2</sub> |  | 0.7 | 0.2 | 1.6 | 20.1 |
| Jabari Walker | 96% | 27.0<br><sub>16,13,20,20,17</sub> | 11.6<br><sub>12,6,9,10,7</sub> |  | 7.2<br><sub>5,5,7,5,2</sub> |  | 1.8<br><sub>1,2,4,2,1</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 0.8 | 0.3 | 1.1 | 20.7 |
| Dominick Barlow | 93% | 25.3<br><sub>-,-,11,16,16</sub> | 9.0<br><sub>-,-,12,6,9</sub> |  | 5.5<br><sub>-,-,4,2,8</sub> |  | 1.4<br><sub>-,-,1,0,0</sub> |  | 0.3<br><sub>-,-,1,0,0</sub> |  | 0.9 | 0.8 | 1.1 | 15.9 |
| Adem Bona | 98% | 21.5<br><sub>-,-,-,5,13</sub> | 5.8<br><sub>-,-,-,4,0</sub> |  | 5.6<br><sub>-,-,-,2,6</sub> |  | 0.9<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.6 | 1.3 | 1.2 | 12.3 |
| Labaron Philon Jr. | 64% | 17.8<br><sub>-,17,6,3,-</sub> | 7.0<br><sub>-,10,2,2,-</sub> |  | 2.3<br><sub>-,1,0,1,-</sub> |  | 1.8<br><sub>-,2,0,1,-</sub> |  | 0.8<br><sub>-,2,0,0,-</sub> |  | 0.6 | 0.1 | 1.0 | 11.1 |
| Justin Edwards | 52% | 17.4<br><sub>-,13,-,3,-</sub> | 7.2<br><sub>-,2,-,5,-</sub> |  | 2.4<br><sub>-,1,-,1,-</sub> |  | 1.1<br><sub>-,0,-,0,-</sub> |  | 0.8<br><sub>-,0,-,1,-</sub> |  | 0.8 | 0.2 | 0.7 | 10.6 |
| Rayan Rupert | 36% | 15.0<br><sub>-,-,-,-,-</sub> | 5.7<br><sub>-,-,-,-,-</sub> |  | 2.8<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.1 | 1.0 | 9.7 |
| Tacko Fall | 48% | 13.3<br><sub>-,10,-,-,-</sub> | 9.2<br><sub>-,2,-,-,-</sub> |  | 3.3<br><sub>-,3,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.7 | 0.6 | 13.2 |
| Caleb Love | 48% | 12.2<br><sub>-,6,-,-,-</sub> | 4.0<br><sub>-,3,-,-,-</sub> |  | 1.5<br><sub>-,1,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,1,-,-,-</sub> |  | 0.6 | 0.1 | 0.5 | 6.6 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant | 99% | 36.0<br><sub>29,32,35,33,33</sub> | 24.2<br><sub>22,21,16,32,20</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 6.1<br><sub>2,2,4,9,10</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>3,3,4,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>2,4,0,4,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.7 | 0.9 | 2.8 | 34.9 |
| Amen Thompson | 88% | 35.0<br><sub>-,31,26,28,36</sub> | 17.0<br><sub>-,15,22,20,18</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.6<br><sub>-,9,6,4,10</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.1<br><sub>-,3,0,5,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>-,0,0,1,0</sub> | 0.5<br><sub>o 25% · u 75%</sub> | 1.2 | 0.8 | 2.0 | 28.7 |
| Alperen Sengun | 96% | 34.5<br><sub>30,14,36,31,32</sub> | 21.4<br><sub>23,7,28,20,23</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 10.1<br><sub>7,7,11,8,11</sub> | 9.5<br><sub>o 47% · u 53%</sub> | 7.2<br><sub>2,1,10,7,11</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 0.8<br><sub>1,1,1,1,3</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 1.0 | 1.1 | 2.7 | 38.7 |
| Jabari Smith Jr. | 99% | 34.3<br><sub>32,26,32,28,32</sub> | 14.9<br><sub>12,17,21,13,13</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>10,4,4,6,4</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,2,3,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>1,3,3,1,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.6 | 1.0 | 1.2 | 23.5 |
| Fred VanVleet | 91% | 33.5<br><sub>26,27,33,31,34</sub> | 14.3<br><sub>8,15,25,6,13</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>5,2,1,2,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 5.5<br><sub>6,6,9,4,6</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.6<br><sub>2,3,3,2,3</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.5 | 1.4 | 23.1 |
| Tari Eason | 99% | 23.6<br><sub>27,25,23,22,15</sub> | 9.7<br><sub>7,11,7,10,7</sub> |  | 5.5<br><sub>7,4,6,4,2</sub> |  | 1.4<br><sub>3,3,1,4,0</sub> |  | 1.1<br><sub>0,1,1,2,1</sub> |  | 1.0 | 0.7 | 1.0 | 16.6 |
| Marcus Smart | 76% | 20.9<br><sub>-,18,23,25,18</sub> | 6.4<br><sub>-,4,3,4,4</sub> |  | 2.4<br><sub>-,2,2,3,3</sub> |  | 2.2<br><sub>-,4,2,3,3</sub> |  | 0.9<br><sub>-,1,1,0,0</sub> |  | 1.0 | 0.4 | 1.2 | 11.1 |
| Reed Sheppard | 96% | 18.6<br><sub>19,25,14,17,15</sub> | 8.1<br><sub>5,20,0,5,7</sub> |  | 1.7<br><sub>2,4,2,3,1</sub> |  | 2.2<br><sub>2,2,0,5,1</sub> |  | 1.4<br><sub>1,6,0,1,1</sub> |  | 1.0 | 0.5 | 0.8 | 12.1 |
| Clint Capela | 30% | 11.8<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 4.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.7 | 0.5 | 8.6 |
| Bogdan Bogdanovic | 98% | 11.5<br><sub>26,11,5,9,10</sub> | 4.1<br><sub>6,1,0,2,5</sub> |  | 1.3<br><sub>0,3,1,1,0</sub> |  | 1.1<br><sub>1,0,0,2,1</sub> |  | 0.5<br><sub>2,0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 6.5 |
| Oscar Tshiebwe | 72% | 8.6<br><sub>6,11,-,-,-</sub> | 3.5<br><sub>6,4,-,-,-</sub> |  | 3.8<br><sub>6,4,-,-,-</sub> |  | 0.6<br><sub>0,3,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 7.8 |
| Isaiah Crawford | 52% | 7.1<br><sub>21,2,-,-,-</sub> | 2.4<br><sub>11,0,-,-,-</sub> |  | 1.5<br><sub>10,0,-,-,-</sub> |  | 0.3<br><sub>3,0,-,-,-</sub> |  | 0.2<br><sub>1,0,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |
| Jae'Sean Tate | 48% | 6.2<br><sub>12,1,-,-,-</sub> | 2.0<br><sub>3,0,-,-,-</sub> |  | 1.4<br><sub>3,0,-,-,-</sub> |  | 0.4<br><sub>2,1,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.9 |
| Bruce Thornton | 52% | 5.9<br><sub>12,1,-,-,-</sub> | 2.6<br><sub>7,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-28/`._
