# NBA model · Sun 15 Nov 2026 (US date)

Updated **Mon 16 Nov, 10:23 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-15/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| HOU @ WAS | player points | Alperen Sengun projected 25.0 pts vs DraftKings line 19.5 | minutes 37 vs 35 this season; scoring 0.68/min vs 0.66 this season, 0.61 last season; teammates out: Capela, Smart, VanVleet (~66 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alperen Sengun PTS over 34.5 (35+) | HOU @ WAS | draftkings | 15.60 | 13.66 | 6.22 | 16.1% | 6.0% | 7.3% | +14.2% | +150.7% | 0.2% |
| Alperen Sengun PTS over 39.5 (40+) | HOU @ WAS | draftkings | 30.00 | 26.32 | 12.05 | 8.3% | 3.1% | 3.8% | +14.0% | +149.0% | 0.1% |
| Alperen Sengun PR over 49.5 (50+) | HOU @ WAS | draftkings | 22.00 | 19.34 | 8.93 | 11.2% | 4.2% | 5.2% | +13.7% | +146.5% | 0.2% |
| Alperen Sengun PR over 44.5 (45+) | HOU @ WAS | draftkings | 12.20 | 10.75 | 4.99 | 20.1% | 7.7% | 9.3% | +13.4% | +144.6% | 0.3% |
| Kevin Durant AST over 7.5 (8+) | HOU @ WAS | draftkings | 11.60 | 10.24 | 4.75 | 21.1% | 8.1% | 9.8% | +13.4% | +144.1% | 0.3% |
| Jaime Jaquez Jr. AST over 7.5 (8+) | ATL @ MIL | draftkings | 14.80 | 13.14 | 6.20 | 16.1% | 6.3% | 7.6% | +12.6% | +138.6% | 0.2% |
| Trae Young AST over 13.5 (14+) | HOU @ WAS | draftkings | 17.20 | 15.65 | 7.87 | 12.7% | 5.4% | 6.4% | +10.0% | +118.7% | 0.1% |
| Trae Young AST over 11.5 (12+) | HOU @ WAS | draftkings | 7.30 | 6.91 | 3.92 | 25.5% | 12.8% | 14.5% | +5.7% | +86.0% | 0.2% |
| Jaime Jaquez Jr. PRA over 39.5 (40+) | ATL @ MIL | draftkings | 14.60 | 13.87 | 7.97 | 12.6% | 6.4% | 7.2% | +5.3% | +83.3% | 0.1% |
| Steven Adams REB over 11.5 (12+) | HOU @ WAS | draftkings | 24.00 | 22.83 | 13.19 | 7.6% | 3.9% | 4.4% | +5.1% | +81.9% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| HOU @ WAS | Mon 16 Nov 11:00 | 119.5–110.3 | HOU 74% | 1.34 / 3.91 | WAS +9.5 | 229.5 | WAS +7.5 covers 45%; o223.5 63% |
| ATL @ MIL | Mon 16 Nov 12:00 | 118.5–110.2 | ATL 72% | 1.38 / 3.60 | MIL +8.5 | 228.5 | MIL +8.5 covers 50%; o233.5 40% |
| OKC @ SAC | Mon 16 Nov 13:00 | 119.4–107.3 | OKC 80% | 1.24 / 5.11 | SAC +12.5 | 226.5 | SAC +10.5 covers 46%; o223.5 57% |

### HOU @ WAS
Out: Justin Champagnie (WAS), Tre Johnson (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Clint Capela (HOU), Marcus Smart (HOU), Fred VanVleet (HOU)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant PTS over 21.5 (22+) | HOU @ WAS | pointsbetau | 1.95 | 1.89 | 1.55 | 64.3% | 51.3% | 53.0% | +3.5% | +25.6% | 0.9% |
| Alperen Sengun PTS over 20.5 (21+) | HOU @ WAS | pointsbetau | 2.00 | 1.94 | 1.55 | 64.5% | 49.6% | 51.6% | +3.1% | +29.0% | 0.8% |
| Kyshawn George PTS over 14.5 (15+) | HOU @ WAS | pointsbetau | 2.00 | 1.97 | 1.81 | 55.2% | 50.0% | 50.7% | +1.4% | +10.5% | 0.4% |
| Reed Sheppard PTS over 12.5 (13+) | HOU @ WAS | tab | 2.00 | 1.98 | 2.13 | 46.9% | 51.0% | 50.4% | +0.9% | -6.2% | 0.2% |
| Tari Eason PTS under 11.5 | HOU @ WAS | pointsbetau | 2.05 | 2.03 | 2.20 | 45.4% | 49.8% | 49.2% | +0.9% | -7.0% | 0.2% |
| Trae Young PTS over 18.5 (19+) | HOU @ WAS | pointsbetau | 1.95 | 1.95 | 1.77 | 56.5% | 50.6% | 51.4% | +0.4% | +10.4% | 0.1% |
| Alex Sarr PTS over 11.5 (12+) | HOU @ WAS | draftkings | 2.22 | 2.21 | 1.98 | 50.5% | 44.4% | 45.2% | +0.3% | +12.1% | 0.1% |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.4<br><sub>32,39,35,29,41</sub> | 18.9<br><sub>11,17,8,19,12</sub> | 17.5 · 17.5<br><sub>o 49% · u 51%</sub> | 8.0<br><sub>8,7,9,7,10</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,0,3,4,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.8 | 0.7 | 2.2 | 32.2 |
| Alperen Sengun | 91% | 36.7<br><sub>39,32,35,37,37</sub> | 25.0<br><sub>17,15,20,19,43</sub> | 19.5 · 20.5<br><sub>o 52% · u 48%</sub> | 10.7<br><sub>12,6,12,13,12</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 7.6<br><sub>10,5,8,9,5</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 0.7<br><sub>0,1,1,1,1</sub> | 0.5<br><sub>o 50% · u 50%</sub> | 1.6 | 1.1 | 3.2 | 43.3 |
| Kevin Durant | 98% | 36.6<br><sub>35,38,36,34,33</sub> | 26.3<br><sub>21,21,23,20,22</sub> | 21.5 · 21.5<br><sub>o 53% · u 47%</sub> | 6.4<br><sub>5,10,12,4,3</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>2,3,8,5,6</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 1.0 | 3.4 | 38.1 |
| Jabari Smith Jr. | 98% | 36.1<br><sub>35,39,38,35,24</sub> | 17.2<br><sub>11,15,14,14,6</sub> | 14.5 · 14.5<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>4,9,7,8,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,2,3,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,1,2,2,1</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.8 | 1.4 | 26.6 |
| Tari Eason | 98% | 30.5<br><sub>24,23,19,22,33</sub> | 12.8<br><sub>9,2,12,6,14</sub> | 11.5 · 11.5<br><sub>o 51% · u 49%</sub> | 7.7<br><sub>6,7,5,3,11</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>1,2,2,0,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,2,0,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.7 | 0.8 | 1.3 | 22.4 |
| Reed Sheppard | 88% | 26.2<br><sub>21,13,17,20,19</sub> | 12.8<br><sub>14,6,8,13,0</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 2.7<br><sub>2,0,0,1,0</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 3.8<br><sub>2,0,0,1,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,2,3,0</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.7 | 0.5 | 1.3 | 19.2 |
| Bogdan Bogdanovic | 97% | 16.7<br><sub>5,2,12,10,12</sub> | 6.2<br><sub>0,0,8,0,11</sub> | 6.5 · 6.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>0,1,3,0,1</sub> |  | 1.8<br><sub>0,0,1,0,3</sub> |  | 0.9<br><sub>0,0,2,0,3</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.6 | 0.1 | 0.6 | 10.0 |
| Steven Adams | 23% | 15.1<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> | 3.5 · 3.5<br><sub>o 53% · u 47%</sub> | 5.9<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.6 | 0.9 | 10.8 |
| Oscar Tshiebwe | 91% | 12.1<br><sub>2,3,-,1,6</sub> | 4.6<br><sub>2,2,-,0,0</sub> |  | 5.4<br><sub>0,0,-,0,5</sub> |  | 0.7<br><sub>0,0,-,0,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.3 | 0.6 | 10.7 |
| Jae'Sean Tate | 52% | 10.9<br><sub>-,-,-,1,-</sub> | 3.0<br><sub>-,-,-,0,-</sub> |  | 2.6<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 6.3 |
| Bruce Thornton | 58% | 10.9<br><sub>-,-,1,3,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 2.6<br><sub>-,-,0,0,-</sub> |  | 0.8<br><sub>-,-,0,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.4 | 6.3 |
| Isaiah Crawford | 58% | 9.9<br><sub>-,-,1,1,-</sub> | 2.9<br><sub>-,-,0,0,-</sub> |  | 1.5<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,0,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.8 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 36.7<br><sub>37,28,38,34,45</sub> | 20.9<br><sub>23,4,20,15,37</sub> | 18.5 · 18.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>2,5,1,3,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 9.3<br><sub>10,3,7,4,14</sub> | 7.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>3,0,3,3,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.2 | 3.5 | 33.4 |
| Anthony Davis | 98% | 36.1<br><sub>-,-,34,34,44</sub> | 22.5<br><sub>-,-,44,21,30</sub> | 22.5 · 22.5<br><sub>o 49% · u 51%</sub> | 11.7<br><sub>-,-,13,13,15</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>-,-,1,0,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.7<br><sub>-,-,2,0,0</sub> | 0.5<br><sub>o 48% · u 52%</sub> | 1.3 | 1.7 | 2.3 | 36.9 |
| AJ Dybantsa | 98% | 35.5<br><sub>36,31,37,34,44</sub> | 15.1<br><sub>11,19,21,13,5</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>9,6,8,4,8</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>3,3,1,2,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.2 | 0.6 | 2.3 | 23.6 |
| Kyshawn George | 98% | 33.8<br><sub>39,30,35,39,26</sub> | 16.2<br><sub>33,14,12,25,14</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 4.8<br><sub>4,7,3,9,1</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>7,6,2,3,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>5,2,2,5,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 1.1 | 2.3 | 25.3 |
| Alex Sarr | 98% | 29.9<br><sub>30,28,25,25,44</sub> | 12.4<br><sub>13,15,4,5,30</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>8,14,8,8,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>3,1,0,0,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,0,1,4</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.0 | 1.6 | 1.5 | 22.3 |
| Bilal Coulibaly | 98% | 26.5<br><sub>24,20,-,25,29</sub> | 9.3<br><sub>9,0,-,5,4</sub> | 7.5 · 6.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,5,-,6,7</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>0,0,-,2,0</sub> |  | 0.9<br><sub>1,0,-,0,0</sub> |  | 1.2 | 0.9 | 1.2 | 14.9 |
| Bub Carrington | 98% | 17.8<br><sub>15,21,19,10,16</sub> | 5.9<br><sub>5,9,4,0,2</sub> |  | 1.8<br><sub>1,6,0,0,0</sub> |  | 2.2<br><sub>1,1,4,0,2</sub> |  | 0.9<br><sub>1,3,1,0,0</sub> |  | 0.5 | 0.1 | 1.1 | 9.9 |
| Deandre Ayton | 98% | 13.7<br><sub>23,7,13,9,9</sub> | 4.6<br><sub>8,2,2,2,2</sub> |  | 4.4<br><sub>11,1,8,2,4</sub> |  | 0.5<br><sub>3,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.6 | 9.6 |
| Khris Middleton | 35% | 11.2<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 6.1 |
| Will Riley | 76% | 9.8<br><sub>9,20,4,-,3</sub> | 3.9<br><sub>7,5,0,-,3</sub> |  | 1.1<br><sub>0,2,0,-,0</sub> |  | 0.7<br><sub>0,1,1,-,0</sub> |  | 0.3<br><sub>1,0,0,-,1</sub> |  | 0.4 | 0.1 | 0.5 | 5.8 |
| Tre Mann | 52% | 7.0<br><sub>-,18,2,-,-</sub> | 2.7<br><sub>-,2,0,-,-</sub> |  | 0.7<br><sub>-,0,0,-,-</sub> |  | 0.7<br><sub>-,2,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.1 |
| Anthony Gill | 43% | 6.7<br><sub>-,9,2,-,-</sub> | 2.3<br><sub>-,1,0,-,-</sub> |  | 1.1<br><sub>-,1,2,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 3.8 |

</details>


### ATL @ MIL
Out: Ousmane Dieng (MIL), Kam Jones (MIL), Pete Nance (MIL), Ryan Rollins (MIL), Cormac Ryan (MIL), Kingston Flemings (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Jock Landale (ATL), Asa Newell (ATL), Jalen Wilson (ATL)

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 35.6<br><sub>-,-,36,38,40</sub> | 22.2<br><sub>-,-,30,15,27</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>-,-,7,7,11</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 8.0<br><sub>-,-,6,4,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.4<br><sub>-,-,0,0,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.5 | 3.0 | 39.8 |
| Nickeil Alexander-Walker | 98% | 34.5<br><sub>32,33,31,34,41</sub> | 22.7<br><sub>26,28,20,20,16</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>4,2,3,4,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,1,4,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.8<br><sub>6,4,2,4,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4 | 0.5 | 2.2 | 29.9 |
| Dyson Daniels | 98% | 33.1<br><sub>34,35,31,31,36</sub> | 11.3<br><sub>8,13,9,10,6</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 8.0<br><sub>16,9,10,6,9</sub> | 6.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>8,12,7,8,4</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>0,0,0,1,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 2.5 | 0.4 | 1.5 | 25.5 |
| Onyeka Okongwu | 98% | 32.5<br><sub>31,33,30,30,35</sub> | 15.7<br><sub>14,22,16,16,17</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 8.0<br><sub>16,10,2,9,6</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>4,1,5,3,1</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>2,2,2,2,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.1 | 1.0 | 1.4 | 26.9 |
| CJ McCollum | 98% | 28.6<br><sub>25,23,21,24,32</sub> | 17.5<br><sub>15,4,9,21,20</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>5,3,4,0,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 4.2<br><sub>5,4,3,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 2.3<br><sub>2,0,1,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.6 | 2.0 | 25.0 |
| Aaron Wiggins | 98% | 26.0<br><sub>29,29,26,23,26</sub> | 13.5<br><sub>15,19,20,15,9</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>4,4,4,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,3,6,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>3,3,5,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.4 | 1.1 | 19.5 |
| Luguentz Dort | 98% | 24.1<br><sub>31,32,20,18,20</sub> | 8.7<br><sub>6,25,3,4,10</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,7,2,3,1</sub> |  | 1.7<br><sub>3,4,1,2,2</sub> |  | 1.4<br><sub>2,5,1,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.3 | 0.7 | 13.6 |
| Zuby Ejiofor | 63% | 12.0<br><sub>17,15,18,4,-</sub> | 4.1<br><sub>11,10,7,0,-</sub> |  | 2.8<br><sub>3,5,6,0,-</sub> |  | 1.1<br><sub>2,5,0,0,-</sub> |  | 0.3<br><sub>1,0,1,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.0 |
| Corey Kispert | 52% | 11.7<br><sub>8,16,-,-,-</sub> | 6.2<br><sub>9,7,-,-,-</sub> |  | 1.5<br><sub>0,2,-,-,-</sub> |  | 1.0<br><sub>1,1,-,-,-</sub> |  | 0.8<br><sub>1,1,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 8.7 |
| RayJ Dennis | 52% | 10.2<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.4 |
| Dorian Finney-Smith | 26% | 7.1<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.6 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 34.3<br><sub>35,27,-,35,34</sub> | 22.7<br><sub>23,13,-,27,18</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>5,1,-,2,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>10,2,-,7,2</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 2.7<br><sub>1,1,-,2,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.3 | 2.9 | 33.2 |
| Kyle Kuzma | 98% | 30.7<br><sub>32,31,26,24,31</sub> | 14.8<br><sub>13,27,5,9,14</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 5.7<br><sub>4,4,5,1,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.6<br><sub>3,0,3,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,6,1,1,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.5 | 2.4 | 24.1 |
| Jaime Jaquez Jr. | 98% | 30.3<br><sub>28,23,25,30,28</sub> | 17.5<br><sub>14,4,16,25,22</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 5.8<br><sub>3,2,5,5,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>3,2,3,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>2,0,2,2,5</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 2.4 | 28.3 |
| Myles Turner | 98% | 29.3<br><sub>24,24,27,-,31</sub> | 11.5<br><sub>0,3,3,-,14</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 6.6<br><sub>7,5,3,-,11</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>0,7,2,-,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.6<br><sub>0,0,1,-,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 1.8 | 1.8 | 20.6 |
| Brayden Burries | 98% | 26.2<br><sub>38,29,26,23,19</sub> | 10.5<br><sub>21,13,3,8,3</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>11,8,3,5,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>6,4,3,1,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.0<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.3 | 1.6 | 19.4 |
| Nate Ament | 93% | 22.1<br><sub>15,23,22,22,22</sub> | 9.2<br><sub>7,12,10,2,9</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>1,5,2,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.1<br><sub>0,1,1,1,1</sub> |  | 1.1<br><sub>0,2,2,0,2</sub> |  | 0.7 | 0.4 | 1.2 | 13.8 |
| AJ Green | 98% | 19.6<br><sub>24,18,8,8,8</sub> | 7.2<br><sub>12,5,0,3,0</sub> |  | 2.0<br><sub>1,1,0,1,0</sub> |  | 1.4<br><sub>0,1,0,1,2</sub> |  | 1.4<br><sub>4,1,0,1,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.6 |
| Kel'el Ware | 96% | 18.5<br><sub>13,9,17,23,17</sub> | 8.8<br><sub>4,0,8,8,10</sub> |  | 6.7<br><sub>3,0,4,5,6</sub> |  | 1.1<br><sub>0,1,1,1,1</sub> |  | 0.7<br><sub>0,0,0,0,2</sub> |  | 0.5 | 1.0 | 1.5 | 16.5 |
| Gary Trent Jr. | 63% | 16.9<br><sub>-,-,6,4,16</sub> | 7.3<br><sub>-,-,5,6,1</sub> |  | 1.0<br><sub>-,-,0,1,0</sub> |  | 0.9<br><sub>-,-,0,0,0</sub> |  | 1.2<br><sub>-,-,1,2,0</sub> |  | 0.6 | 0.1 | 0.8 | 9.2 |
| Caris LeVert | 8% | 16.9<br><sub>-,-,-,-,-</sub> | 6.4<br><sub>-,-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.5 | 1.2 | 10.7 |
| Kasparas Jakucionis | 72% | 16.0<br><sub>10,7,23,4,-</sub> | 5.9<br><sub>3,1,11,4,-</sub> |  | 2.1<br><sub>0,2,0,2,-</sub> |  | 2.8<br><sub>2,0,4,0,-</sub> |  | 0.5<br><sub>0,0,2,0,-</sub> |  | 0.6 | 0.2 | 1.4 | 10.9 |
| Jericho Sims | 66% | 14.2<br><sub>7,15,8,18,-</sub> | 3.1<br><sub>0,2,2,0,-</sub> |  | 3.9<br><sub>1,2,0,4,-</sub> |  | 1.3<br><sub>0,0,0,1,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.2 | 0.9 | 8.3 |

</details>


### OKC @ SAC
Out: Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC), Jaylin Williams (OKC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 119.4–107.3 | OKC 80% | 1.24 / 5.11 | SAC +12.5 | 226.5 | SAC +10.5 covers 46%; o223.5 57% |
| Expected (weighted by chance each plays) | 119.6–108.0 | OKC 79% | 1.27 / 4.67 | SAC +11.5 | 227.5 | SAC +10.5 covers 47%; o223.5 59% |
| if Ajay Mitchell plays | 119.9–107.3 | OKC 82% | 1.23 / 5.41 | SAC +12.5 | 227.5 | SAC +10.5 covers 44%; o223.5 58% |
| if Precious Achiuwa plays | 118.8–108.4 | OKC 77% | 1.30 / 4.36 | SAC +10.5 | 227.5 | SAC +10.5 covers 50%; o223.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ajay Mitchell (OKC) | Questionable | 55% | 26.1 | 15.5 | 3.3 | 3.6 | 0.9 | 1.3 | 0.3 | 1.6 | 22.4 | full tables below |
| Precious Achiuwa (SAC) | Questionable | 55% | 23.4 | 10.0 | 6.5 | 1.4 | 0.5 | 0.8 | 0.8 | 1.1 | 17.9 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.6<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.8 | 2.6 | 46.1 |
| Jared McCain | 98% | 29.7<br><sub>29,23,31,31,31</sub> | 16.9<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.1 | 1.6 | 22.6 |
| Isaiah Hartenstein | 98% | 28.3<br><sub>26,18,24,34,30</sub> | 11.5<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.2<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.7 | 26.8 |
| Kenrich Williams | 98% | 27.3<br><sub>19,23,19,26,35</sub> | 10.8<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.0 | 18.5 |
| Alex Caruso | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.3<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 10.0<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.3 |
| Bennett Stirtz | 98% | 19.6<br><sub>24,29,18,25,12</sub> | 8.0<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Josh Dix | 67% | 17.8<br><sub>15,21,-,-,17</sub> | 6.8<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 9.8 |
| Micah Peavy | 88% | 17.0<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford | 96% | 15.0<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.4<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 8.9 |
| Nikola Topic | 72% | 14.3<br><sub>-,-,-,-,16</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.5 | 9.3 |
| Brooks Barnhizer | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |

</details>

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 36.8<br><sub>42,33,39,40,35</sub> | 22.2<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.3 | 3.7 | 33.5 |
| De'Andre Hunter | 98% | 34.0<br><sub>38,-,31,34,42</sub> | 15.1<br><sub>14,-,14,15,24</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 2.0 | 21.9 |
| Zach LaVine | 98% | 33.1<br><sub>35,35,25,33,36</sub> | 19.0<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 2.5 | 25.1 |
| Domantas Sabonis | 98% | 32.8<br><sub>35,31,-,24,35</sub> | 14.9<br><sub>16,17,-,0,21</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 12.4<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 5.7<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.7 | 32.9 |
| Keegan Murray | 98% | 31.1<br><sub>-,-,23,24,40</sub> | 12.1<br><sub>-,-,10,11,16</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>-,-,2,1,4</sub> |  | 1.7<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 1.1 | 1.2 | 18.8 |
| Leaky Black | 80% | 17.4<br><sub>22,40,20,18,12</sub> | 4.5<br><sub>3,12,6,0,0</sub> |  | 2.8<br><sub>6,3,5,3,0</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.4 |
| Dylan Cardwell | 98% | 17.4<br><sub>13,15,18,29,13</sub> | 5.0<br><sub>4,9,4,1,6</sub> |  | 6.2<br><sub>6,2,9,11,3</sub> |  | 1.4<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 12.7 |
| Malik Monk | 98% | 16.5<br><sub>24,18,21,3,18</sub> | 8.8<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.1<br><sub>3,2,0,0,0</sub> |  | 0.4 | 0.3 | 1.3 | 13.2 |
| Emanuel Sharp | 98% | 13.6<br><sub>10,31,12,19,7</sub> | 4.0<br><sub>3,9,5,2,4</sub> |  | 1.2<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.9 |
| Daeqwon Plowden | 83% | 9.1<br><sub>-,-,12,2,2</sub> | 3.2<br><sub>-,-,6,0,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Alex Karaban | 48% | 8.5<br><sub>-,11,-,-,-</sub> | 2.7<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.4 |
| Mason Plumlee | 30% | 7.5<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>if Precious Achiuwa plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 34.5<br><sub>30,29,29,36,39</sub> | 35.4<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.6<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.8 | 2.6 | 45.9 |
| Jared McCain (OKC) | 98% | 29.7<br><sub>29,23,31,31,31</sub> | 16.8<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.6 | 22.6 |
| Isaiah Hartenstein (OKC) | 98% | 28.3<br><sub>26,18,24,34,30</sub> | 11.4<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 11.3<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.2 | 0.8 | 1.6 | 26.8 |
| Kenrich Williams (OKC) | 98% | 27.2<br><sub>19,23,19,26,35</sub> | 10.8<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.0 | 0.2 | 1.0 | 18.4 |
| Alex Caruso (OKC) | 98% | 25.1<br><sub>20,13,19,29,27</sub> | 10.3<br><sub>5,0,5,14,5</sub> |  | 3.8<br><sub>6,3,2,7,1</sub> |  | 3.1<br><sub>2,3,1,2,4</sub> |  | 1.6<br><sub>1,0,1,4,1</sub> |  | 1.6 | 0.5 | 1.1 | 17.2 |
| Aday Mara (OKC) | 98% | 24.5<br><sub>18,27,26,32,21</sub> | 9.9<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.8 | 1.5 | 18.2 |
| Bennett Stirtz (OKC) | 98% | 19.6<br><sub>24,29,18,25,12</sub> | 7.9<br><sub>12,11,13,6,5</sub> |  | 1.6<br><sub>1,5,1,1,1</sub> |  | 1.4<br><sub>2,3,1,1,0</sub> |  | 1.3<br><sub>2,2,2,2,1</sub> |  | 0.7 | 0.2 | 0.7 | 10.8 |
| Josh Dix (OKC) | 67% | 17.7<br><sub>15,21,-,-,17</sub> | 6.7<br><sub>5,2,-,-,0</sub> |  | 2.1<br><sub>2,1,-,-,4</sub> |  | 0.9<br><sub>1,2,-,-,3</sub> |  | 0.7<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 9.8 |
| Micah Peavy (OKC) | 88% | 16.9<br><sub>18,23,21,12,-</sub> | 4.7<br><sub>7,7,0,0,-</sub> |  | 2.9<br><sub>4,3,2,3,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>1,1,0,0,-</sub> |  | 0.7 | 0.2 | 0.5 | 8.2 |
| Nique Clifford (OKC) | 96% | 15.0<br><sub>-,-,20,16,12</sub> | 5.3<br><sub>-,-,4,5,0</sub> |  | 2.2<br><sub>-,-,4,3,0</sub> |  | 1.5<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.7 | 0.2 | 0.8 | 9.0 |
| Nikola Topic (OKC) | 72% | 14.3<br><sub>-,-,-,-,16</sub> | 4.1<br><sub>-,-,-,-,0</sub> |  | 1.9<br><sub>-,-,-,-,4</sub> |  | 3.2<br><sub>-,-,-,-,3</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.1 | 1.4 | 9.2 |
| Brooks Barnhizer (OKC) | 52% | 8.7<br><sub>5,8,5,-,-</sub> | 2.2<br><sub>0,2,0,-,-</sub> |  | 1.9<br><sub>0,4,1,-,-</sub> |  | 0.7<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.8 |
| Darius Acuff Jr. (SAC) | 98% | 34.7<br><sub>42,33,39,40,35</sub> | 20.5<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.2 | 3.4 | 31.2 |
| Zach LaVine (SAC) | 98% | 31.1<br><sub>35,35,25,33,36</sub> | 17.6<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.6<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.2 | 2.3 | 23.3 |
| De'Andre Hunter (SAC) | 98% | 30.7<br><sub>38,-,31,34,42</sub> | 13.6<br><sub>14,-,14,15,24</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.7 | 19.8 |
| Domantas Sabonis (SAC) | 98% | 30.6<br><sub>35,31,-,24,35</sub> | 13.8<br><sub>16,17,-,0,21</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 11.7<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.4<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.6 | 30.8 |
| Keegan Murray (SAC) | 98% | 28.6<br><sub>-,-,23,24,40</sub> | 11.2<br><sub>-,-,10,11,16</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.5<br><sub>-,-,2,1,4</sub> |  | 1.5<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 1.0 | 1.1 | 17.2 |
| Precious Achiuwa (SAC) | 100% | 23.4<br><sub>17,22,36,14,-</sub> | 10.0<br><sub>7,9,7,10,-</sub> |  | 6.5<br><sub>3,4,14,3,-</sub> |  | 1.4<br><sub>1,0,2,0,-</sub> |  | 0.5<br><sub>1,1,0,1,-</sub> |  | 0.8 | 0.8 | 1.1 | 17.9 |
| Dylan Cardwell (SAC) | 98% | 16.1<br><sub>13,15,18,29,13</sub> | 4.6<br><sub>4,9,4,1,6</sub> |  | 5.7<br><sub>6,2,9,11,3</sub> |  | 1.3<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 11.7 |
| Malik Monk (SAC) | 98% | 15.6<br><sub>24,18,21,3,18</sub> | 8.5<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.0<br><sub>3,2,0,0,0</sub> |  | 0.4 | 0.3 | 1.2 | 12.8 |
| Leaky Black (SAC) | 80% | 15.5<br><sub>22,40,20,18,12</sub> | 4.0<br><sub>3,12,6,0,0</sub> |  | 2.6<br><sub>6,3,5,3,0</sub> |  | 1.0<br><sub>1,5,1,2,0</sub> |  | 0.5<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.3 | 0.6 | 7.5 |
| Emanuel Sharp (SAC) | 98% | 12.1<br><sub>10,31,12,19,7</sub> | 3.6<br><sub>3,9,5,2,4</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.6<br><sub>2,0,0,0,0</sub> |  | 0.4<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.3 |
| Daeqwon Plowden (SAC) | 83% | 8.0<br><sub>-,-,12,2,2</sub> | 2.9<br><sub>-,-,6,0,0</sub> |  | 0.9<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.3<br><sub>-,-,2,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Alex Karaban (SAC) | 48% | 7.1<br><sub>-,11,-,-,-</sub> | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,1,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.9 |
| Mason Plumlee (SAC) | 30% | 7.0<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.8 |

</details>

<details><summary>if Ajay Mitchell plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander (OKC) | 98% | 32.2<br><sub>30,29,29,36,39</sub> | 31.1<br><sub>28,30,26,31,40</sub> | 32.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>3,2,8,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.9<br><sub>4,9,3,2,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.8<br><sub>3,3,0,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.8 | 2.4 | 40.8 |
| Jared McCain (OKC) | 98% | 26.2<br><sub>29,23,31,31,31</sub> | 14.9<br><sub>21,19,21,10,23</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 3.1<br><sub>5,5,3,6,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>0,2,3,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.6<br><sub>3,2,4,2,7</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.1 | 1.4 | 20.0 |
| Ajay Mitchell (OKC) | 100% | 26.1<br><sub>30,22,28,-,-</sub> | 15.5<br><sub>35,12,14,-,-</sub> | 17.5 · – | 3.3<br><sub>1,4,3,-,-</sub> | 3.5 | 3.6<br><sub>5,0,3,-,-</sub> | 3.5 | 0.9<br><sub>4,0,0,-,-</sub> | 1.5 | 1.3 | 0.3 | 1.6 | 22.4 |
| Isaiah Hartenstein (OKC) | 98% | 25.5<br><sub>26,18,24,34,30</sub> | 10.2<br><sub>2,2,7,20,21</sub> | 9.5 · –<br><sub>o 54% · u 46%</sub> | 10.0<br><sub>6,14,9,11,16</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>7,6,5,6,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 0.7 | 1.5 | 23.8 |
| Kenrich Williams (OKC) | 98% | 22.6<br><sub>19,23,19,26,35</sub> | 9.0<br><sub>4,9,3,11,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>6,4,2,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>3,2,0,2,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>1,1,1,2,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.8 | 0.2 | 0.8 | 15.3 |
| Alex Caruso (OKC) | 98% | 21.7<br><sub>20,13,19,29,27</sub> | 8.9<br><sub>5,0,5,14,5</sub> |  | 3.2<br><sub>6,3,2,7,1</sub> |  | 2.6<br><sub>2,3,1,2,4</sub> |  | 1.3<br><sub>1,0,1,4,1</sub> |  | 1.4 | 0.5 | 0.9 | 14.8 |
| Aday Mara (OKC) | 98% | 21.6<br><sub>18,27,26,32,21</sub> | 8.8<br><sub>9,18,10,11,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>7,8,10,6,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>0,3,2,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.5 | 1.6 | 1.3 | 16.1 |
| Bennett Stirtz (OKC) | 98% | 16.3<br><sub>24,29,18,25,12</sub> | 6.5<br><sub>12,11,13,6,5</sub> |  | 1.3<br><sub>1,5,1,1,1</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.0<br><sub>2,2,2,2,1</sub> |  | 0.6 | 0.2 | 0.5 | 9.0 |
| Josh Dix (OKC) | 67% | 15.2<br><sub>15,21,-,-,17</sub> | 5.6<br><sub>5,2,-,-,0</sub> |  | 1.9<br><sub>2,1,-,-,4</sub> |  | 0.8<br><sub>1,2,-,-,3</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.6 | 0.2 | 0.5 | 8.3 |
| Nique Clifford (OKC) | 96% | 13.2<br><sub>-,-,20,16,12</sub> | 4.8<br><sub>-,-,4,5,0</sub> |  | 2.0<br><sub>-,-,4,3,0</sub> |  | 1.3<br><sub>-,-,1,1,0</sub> |  | 0.4<br><sub>-,-,0,1,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.1 |
| Micah Peavy (OKC) | 88% | 13.1<br><sub>18,23,21,12,-</sub> | 3.7<br><sub>7,7,0,0,-</sub> |  | 2.3<br><sub>4,3,2,3,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.3<br><sub>1,1,0,0,-</sub> |  | 0.5 | 0.2 | 0.3 | 6.5 |
| Nikola Topic (OKC) | 72% | 11.5<br><sub>-,-,-,-,16</sub> | 3.5<br><sub>-,-,-,-,0</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 2.6<br><sub>-,-,-,-,3</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.1 | 1.1 | 7.6 |
| Brooks Barnhizer (OKC) | 52% | 7.0<br><sub>5,8,5,-,-</sub> | 1.9<br><sub>0,2,0,-,-</sub> |  | 1.6<br><sub>0,4,1,-,-</sub> |  | 0.6<br><sub>0,3,1,-,-</sub> |  | 0.1<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Darius Acuff Jr. (SAC) | 98% | 36.8<br><sub>42,33,39,40,35</sub> | 22.2<br><sub>22,22,32,29,17</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 3.9<br><sub>3,3,5,4,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>12,8,10,6,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>3,3,3,4,3</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.3 | 3.7 | 33.5 |
| De'Andre Hunter (SAC) | 98% | 34.0<br><sub>38,-,31,34,42</sub> | 15.0<br><sub>14,-,14,15,24</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>2,-,3,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.8<br><sub>2,-,1,2,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>1,-,2,3,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.9 | 21.8 |
| Zach LaVine (SAC) | 98% | 33.1<br><sub>35,35,25,33,36</sub> | 18.9<br><sub>21,14,15,31,12</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,4,4,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.9<br><sub>1,3,2,2,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>3,1,1,6,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 2.4 | 25.0 |
| Domantas Sabonis (SAC) | 98% | 32.7<br><sub>35,31,-,24,35</sub> | 15.0<br><sub>16,17,-,0,21</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 12.3<br><sub>17,12,-,2,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 5.6<br><sub>1,5,-,5,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.3 | 2.7 | 32.9 |
| Keegan Murray (SAC) | 98% | 31.2<br><sub>-,-,23,24,40</sub> | 12.2<br><sub>-,-,10,11,16</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>-,-,1,2,7</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>-,-,2,1,4</sub> |  | 1.7<br><sub>-,-,0,2,2</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 1.1 | 1.2 | 18.9 |
| Leaky Black (SAC) | 80% | 17.5<br><sub>22,40,20,18,12</sub> | 4.5<br><sub>3,12,6,0,0</sub> |  | 2.9<br><sub>6,3,5,3,0</sub> |  | 1.1<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>0,4,2,0,0</sub> |  | 0.7 | 0.4 | 0.6 | 8.4 |
| Dylan Cardwell (SAC) | 98% | 17.4<br><sub>13,15,18,29,13</sub> | 5.0<br><sub>4,9,4,1,6</sub> |  | 6.2<br><sub>6,2,9,11,3</sub> |  | 1.4<br><sub>0,3,3,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 12.7 |
| Malik Monk (SAC) | 98% | 16.4<br><sub>24,18,21,3,18</sub> | 8.8<br><sub>13,12,9,1,7</sub> |  | 1.6<br><sub>2,0,2,0,4</sub> |  | 2.7<br><sub>3,7,3,0,3</sub> |  | 1.1<br><sub>3,2,0,0,0</sub> |  | 0.4 | 0.3 | 1.3 | 13.1 |
| Emanuel Sharp (SAC) | 98% | 13.6<br><sub>10,31,12,19,7</sub> | 4.0<br><sub>3,9,5,2,4</sub> |  | 1.2<br><sub>1,5,1,2,0</sub> |  | 0.7<br><sub>2,0,0,0,0</sub> |  | 0.5<br><sub>1,3,1,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.9 |
| Daeqwon Plowden (SAC) | 83% | 9.1<br><sub>-,-,12,2,2</sub> | 3.3<br><sub>-,-,6,0,0</sub> |  | 1.1<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,2,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.7 |
| Alex Karaban (SAC) | 48% | 8.5<br><sub>-,11,-,-,-</sub> | 2.7<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,1,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.4 |
| Mason Plumlee (SAC) | 30% | 7.5<br><sub>-,-,-,-,-</sub> | 1.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 4.9 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-15/`._
