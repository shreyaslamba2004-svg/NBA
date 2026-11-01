# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sun 01 Nov, 11:42 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 7.5 (8+) | OKC @ HOU | draftkings | 21.00 | 13.32 | 5.99 | 16.7% | 4.5% | 7.5% | +57.8% | +250.7% | 0.7% |
| Tari Eason REB over 11.5 (12+) | OKC @ HOU | draftkings | 21.00 | 16.39 | 9.06 | 11.0% | 4.5% | 6.1% | +28.0% | +131.7% | 0.4% |
| Tari Eason REB over 9.5 (10+) | OKC @ HOU | draftkings | 9.40 | 7.39 | 4.12 | 24.3% | 9.9% | 13.5% | +27.2% | +128.3% | 0.8% |
| Kevin Durant REB over 9.5 (10+) | OKC @ HOU | draftkings | 14.60 | 12.00 | 7.08 | 14.1% | 6.4% | 8.3% | +21.6% | +106.2% | 0.4% |
| Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings | 28.00 | 23.47 | 14.23 | 7.0% | 3.3% | 4.3% | +19.3% | +96.8% | 0.2% |
| Amen Thompson AST over 7.5 (8+) | OKC @ HOU | draftkings | 8.20 | 6.93 | 4.26 | 23.5% | 11.4% | 14.4% | +18.2% | +92.5% | 0.6% |
| Amen Thompson AST over 9.5 (10+) | OKC @ HOU | draftkings | 22.00 | 18.69 | 11.53 | 8.7% | 4.2% | 5.3% | +17.8% | +90.8% | 0.2% |
| Amen Thompson PTS over 29.5 (30+) | OKC @ HOU | draftkings | 20.60 | 17.64 | 11.04 | 9.1% | 4.5% | 5.7% | +16.8% | +86.7% | 0.2% |
| Shai Gilgeous-Alexander PRA over 59.5 (60+) | OKC @ HOU | draftkings | 20.20 | 17.33 | 10.88 | 9.2% | 4.6% | 5.8% | +16.5% | +85.6% | 0.2% |
| Shai Gilgeous-Alexander PTS over 44.5 (45+) | OKC @ HOU | draftkings | 15.20 | 13.11 | 8.28 | 12.1% | 6.2% | 7.6% | +16.0% | +83.5% | 0.3% |
| Amen Thompson PRA over 44.5 (45+) | OKC @ HOU | draftkings | 19.00 | 16.39 | 10.38 | 9.6% | 4.9% | 6.1% | +15.9% | +83.1% | 0.2% |
| Amen Thompson PRA over 39.5 (40+) | OKC @ HOU | draftkings | 9.20 | 7.99 | 5.10 | 19.6% | 10.2% | 12.5% | +15.2% | +80.5% | 0.5% |
| Jabari Smith Jr. PRA over 34.5 (35+) | OKC @ HOU | draftkings | 9.50 | 8.41 | 5.54 | 18.1% | 9.8% | 11.9% | +13.0% | +71.5% | 0.4% |
| Amen Thompson PTS over 24.5 (25+) | OKC @ HOU | draftkings | 8.00 | 7.15 | 4.78 | 20.9% | 11.7% | 14.0% | +11.9% | +67.4% | 0.4% |
| Jabari Smith Jr. REB over 9.5 (10+) | OKC @ HOU | draftkings | 7.10 | 6.43 | 4.40 | 22.7% | 13.2% | 15.6% | +10.4% | +61.2% | 0.4% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ HOU | draftkings | 9.20 | 8.35 | 5.73 | 17.4% | 10.2% | 12.0% | +10.2% | +60.5% | 0.3% |
| Jabari Smith Jr. PRA over 39.5 (40+) | OKC @ HOU | draftkings | 20.00 | 18.15 | 12.48 | 8.0% | 4.7% | 5.5% | +10.2% | +60.3% | 0.1% |
| Jabari Smith Jr. REB over 11.5 (12+) | OKC @ HOU | draftkings | 16.80 | 15.29 | 10.55 | 9.5% | 5.6% | 6.5% | +9.9% | +59.2% | 0.2% |
| Shai Gilgeous-Alexander PRA over 54.5 (55+) | OKC @ HOU | draftkings | 10.70 | 9.81 | 6.87 | 14.5% | 8.7% | 10.2% | +9.0% | +55.7% | 0.2% |
| Jabari Smith Jr. PA over 29.5 (30+) | OKC @ HOU | draftkings | 15.20 | 14.01 | 9.90 | 10.1% | 6.2% | 7.1% | +8.5% | +53.6% | 0.1% |
| Amen Thompson PR over 34.5 (35+) | OKC @ HOU | draftkings | 9.50 | 8.76 | 6.19 | 16.2% | 9.8% | 11.4% | +8.4% | +53.4% | 0.2% |
| Shai Gilgeous-Alexander AST over 11.5 (12+) | OKC @ HOU | draftkings | 23.00 | 21.28 | 15.13 | 6.6% | 4.1% | 4.7% | +8.1% | +52.0% | 0.1% |
| Jabari Smith Jr. PRA over 29.5 (30+) | OKC @ HOU | draftkings | 4.35 | 4.02 | 2.86 | 34.9% | 21.5% | 24.9% | +8.1% | +52.0% | 0.6% |
| Amen Thompson PR over 39.5 (40+) | OKC @ HOU | draftkings | 20.60 | 19.16 | 13.78 | 7.3% | 4.5% | 5.2% | +7.5% | +49.5% | 0.1% |
| Amen Thompson PRA over 34.5 (35+) | OKC @ HOU | draftkings | 4.19 | 3.90 | 2.81 | 35.6% | 22.3% | 25.6% | +7.4% | +49.2% | 0.6% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 10.5 (11+) | OKC @ HOU | draftkings | 14.40 | 11.04 | 5.96 | 16.8% | 6.5% | 9.1% | +30.4% | +141.4% | 0.6% |
| Tari Eason REB over 12.5 (13+) | OKC @ HOU | draftkings | 29.00 | 23.75 | 13.91 | 7.2% | 3.2% | 4.2% | +22.2% | +108.5% | 0.2% |
| Kevin Durant REB over 8.5 (9+) | OKC @ HOU | draftkings | 9.20 | 7.58 | 4.49 | 22.3% | 10.2% | 13.2% | +21.3% | +105.0% | 0.7% |
| Amen Thompson AST over 8.5 (9+) | OKC @ HOU | draftkings | 14.20 | 11.71 | 6.93 | 14.4% | 6.6% | 8.5% | +21.3% | +104.9% | 0.4% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 23.00 | 19.42 | 11.91 | 8.4% | 4.1% | 5.1% | +18.4% | +93.1% | 0.2% |
| Shai Gilgeous-Alexander AST over 10.5 (11+) | OKC @ HOU | draftkings | 15.20 | 13.64 | 9.19 | 10.9% | 6.2% | 7.3% | +11.5% | +65.5% | 0.2% |
| Jabari Smith Jr. REB over 10.5 (11+) | OKC @ HOU | draftkings | 11.00 | 9.88 | 6.66 | 15.0% | 8.5% | 10.1% | +11.4% | +65.1% | 0.3% |
| Jabari Smith Jr. REB over 8.5 (9+) | OKC @ HOU | draftkings | 4.61 | 4.28 | 3.07 | 32.6% | 20.3% | 23.4% | +7.7% | +50.3% | 0.5% |
| Shai Gilgeous-Alexander AST over 8.5 (9+) | OKC @ HOU | draftkings | 5.70 | 5.33 | 3.87 | 25.9% | 16.4% | 18.8% | +7.0% | +47.4% | 0.4% |
| Jabari Smith Jr. REB over 12.5 (13+) | OKC @ HOU | draftkings | 25.00 | 23.47 | 17.17 | 5.8% | 3.7% | 4.3% | +6.5% | +45.6% | 0.1% |
| Aday Mara REB over 10.5 (11+) | OKC @ HOU | draftkings | 16.00 | 15.13 | 11.22 | 8.9% | 5.8% | 6.6% | +5.7% | +42.6% | 0.1% |
| Aday Mara REB over 8.5 (9+) | OKC @ HOU | draftkings | 6.68 | 6.36 | 4.78 | 20.9% | 14.0% | 15.7% | +5.0% | +39.8% | 0.2% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 7.5 (8+) | OKC @ HOU | draftkings | 3.90 | 3.42 | 2.22 | 45.0% | 24.0% | 29.2% | +14.0% | +75.5% | 1.2% |
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.14 | 1.96 | 1.37 | 72.9% | 43.9% | 51.1% | +9.4% | +55.9% | 2.0% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 2.00 | 1.83 | 1.29 | 77.6% | 46.9% | 54.5% | +9.1% | +55.1% | 2.0% |
| Amen Thompson AST over 5.5 (6+) | OKC @ HOU | draftkings | 2.99 | 2.79 | 2.02 | 49.6% | 31.3% | 35.9% | +7.2% | +48.3% | 0.9% |
| Kevin Durant REB over 5.5 (6+) | OKC @ HOU | draftkings | 2.34 | 2.22 | 1.66 | 60.3% | 39.9% | 45.0% | +5.4% | +41.1% | 1.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ HOU | Sun 01 Nov 11:30 | 112.1–113.1 | OKC 47% | 2.12 / 1.90 | HOU -1.5 | 225.5 | HOU -2.5 covers 47%; o219.5 61% |

### OKC @ HOU
Out: Steven Adams (HOU), Reed Sheppard (HOU), Fred VanVleet (HOU), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason PTS over 10.5 (11+) | OKC @ HOU | pointsbetau | 2.00 | 1.94 | 1.67 | 59.9% | 48.9% | 51.6% | +3.2% | +19.8% | 0.8% |
| Jared McCain PTS over 14.5 (15+) | OKC @ HOU | pointsbetau | 2.00 | 1.96 | 1.91 | 52.3% | 50.7% | 51.1% | +2.2% | +4.7% | 0.6% |
| Amen Thompson PRA over 27.5 (28+) | OKC @ HOU | draftkings | 1.85 | 1.84 | 1.53 | 65.2% | 50.8% | 54.4% | +0.9% | +20.9% | 0.2% |
| Kevin Durant PA over 26.5 (27+) | OKC @ HOU | draftkings | 1.95 | 1.94 | 1.61 | 62.1% | 48.0% | 51.5% | +0.5% | +21.2% | 0.1% |
| Marcus Smart 3PM under 1.5 | OKC @ HOU | draftkings | 1.92 | 1.91 | 1.59 | 62.8% | 48.7% | 52.2% | +0.2% | +20.4% | 0.1% |
| Shai Gilgeous-Alexander STL over 1.5 (2+) | OKC @ HOU | draftkings | 2.72 | 2.72 | 2.28 | 43.8% | 34.4% | 36.8% | +0.0% | +19.2% | 0.0% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.6<br><sub>36,35,36,30,28</sub> | 30.4<br><sub>32,17,34,26,21</sub> | 29.5 · 28.5<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>6,2,6,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 6.7<br><sub>4,3,5,3,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.9 | 3.3 | 41.0 |
| Jared McCain | 98% | 30.0<br><sub>22,18,21,30,29</sub> | 15.9<br><sub>20,4,3,18,10</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>2,0,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,1,0,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>6,0,1,4,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.9 | 21.1 |
| Ajay Mitchell | 98% | 29.6<br><sub>23,23,28,25,28</sub> | 19.0<br><sub>4,12,18,30,29</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>5,0,6,2,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>6,0,4,5,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.3 | 2.2 | 26.9 |
| Josh Dix | 67% | 27.2<br><sub>-,-,-,22,24</sub> | 4.4<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.4 |
| Bennett Stirtz | 96% | 26.7<br><sub>1,2,11,25,28</sub> | 7.9<br><sub>0,0,2,7,8</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 1.0<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.1 |
| Isaiah Hartenstein | 98% | 26.6<br><sub>17,23,27,26,26</sub> | 10.2<br><sub>4,6,12,15,10</sub> | 9.5 · 9.5<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>3,6,12,13,14</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,2,1,3,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 22.9 |
| Aday Mara | 96% | 24.2<br><sub>12,13,14,20,21</sub> | 8.2<br><sub>7,2,2,11,6</sub> | 7.5 · 7.5<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>2,3,3,10,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.4 | 15.6 |
| Kenrich Williams | 93% | 21.7<br><sub>7,6,7,24,17</sub> | 8.0<br><sub>3,3,3,3,7</sub> | 6.5 · 6.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>2,1,1,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.9 | 13.9 |
| Jaylin Williams | 98% | 21.3<br><sub>17,15,5,26,20</sub> | 6.1<br><sub>5,3,0,6,0</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>4,7,0,6,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>1,3,0,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9<br><sub>1,1,0,2,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.5 | 0.8 | 13.3 |
| Micah Peavy | 48% | 13.1<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer | 80% | 13.0<br><sub>1,2,-,3,14</sub> | 3.5<br><sub>0,0,-,0,3</sub> |  | 2.5<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.8<br><sub>36,39,28,33,39</sub> | 18.8<br><sub>20,17,15,23,15</sub> | 15.5 · 16.5<br><sub>o 54% · u 46%</sub> | 7.4<br><sub>10,11,5,4,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>4,6,2,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.8 | 31.9 |
| Kevin Durant | 98% | 37.6<br><sub>37,37,30,31,37</sub> | 25.8<br><sub>20,22,22,18,28</sub> | 22.5 · 23.5<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>7,4,9,5,5</sub> | 4.5<br><sub>o 60% · u 40%</sub> | 5.1<br><sub>6,2,3,4,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,3,1,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 1.0 | 3.8 | 37.4 |
| Jabari Smith Jr. | 98% | 37.1<br><sub>34,33,39,30,35</sub> | 17.4<br><sub>7,14,16,14,22</sub> | 14.5 · 15.5<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>5,5,12,2,3</sub> | 5.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>1,3,5,2,2</sub> |  | 2.7<br><sub>1,2,2,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.8 | 1.8 | 27.0 |
| Alperen Sengun | 58% | 35.4<br><sub>36,33,37,-,-</sub> | 19.7<br><sub>29,17,29,-,-</sub> | 18.5 · 18.5<br><sub>o 51% · u 49%</sub> | 10.0<br><sub>7,10,9,-,-</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>7,7,9,-,-</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.7<br><sub>2,1,1,-,-</sub> |  | 1.2 | 0.9 | 3.6 | 36.0 |
| Tari Eason | 98% | 30.9<br><sub>27,31,33,31,26</sub> | 12.6<br><sub>12,19,13,5,11</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>6,3,8,9,13</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,2,1,2</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.7 | 1.5 | 21.7 |
| Marcus Smart | 63% | 26.0<br><sub>21,-,-,-,17</sub> | 9.2<br><sub>5,-,-,-,8</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,-,-,-,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>1,-,-,-,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,-,-,-,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.3 | 1.9 | 15.2 |
| Clint Capela | 88% | 22.3<br><sub>-,11,4,22,30</sub> | 6.5<br><sub>-,2,2,10,5</sub> |  | 7.8<br><sub>-,3,2,8,11</sub> |  | 1.4<br><sub>-,1,0,2,5</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.2 | 0.9 | 15.7 |
| Bogdan Bogdanovic | 91% | 19.5<br><sub>9,20,13,15,11</sub> | 7.8<br><sub>3,11,5,16,6</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>1,1,2,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.9<br><sub>0,1,1,4,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.3<br><sub>1,3,1,4,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.2 | 0.9 | 12.1 |
| Oscar Tshiebwe | 76% | 16.5<br><sub>-,-,-,14,11</sub> | 6.3<br><sub>-,-,-,7,0</sub> |  | 6.8<br><sub>-,-,-,5,5</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.4 | 1.0 | 14.0 |
| Jae'Sean Tate | 64% | 9.5<br><sub>-,1,1,4,-</sub> | 3.1<br><sub>-,0,0,0,-</sub> |  | 2.1<br><sub>-,0,1,0,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Bruce Thornton | 63% | 8.7<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,0,0,5,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Isaiah Crawford | 58% | 8.3<br><sub>-,1,1,5,-</sub> | 2.7<br><sub>-,0,0,3,-</sub> |  | 1.5<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-31/`._
