# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sun 01 Nov, 11:22 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 7.5 (8+) | OKC @ HOU | draftkings | 3.87 | 3.60 | 2.58 | 38.8% | 24.1% | 27.8% | +7.6% | +50.2% | 0.7% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 7.5 (8+) | OKC @ HOU | draftkings | 21.00 | 14.37 | 6.90 | 14.5% | 4.5% | 7.0% | +46.2% | +204.4% | 0.6% |
| Tari Eason REB over 9.5 (10+) | OKC @ HOU | draftkings | 9.20 | 8.02 | 5.15 | 19.4% | 10.2% | 12.5% | +14.8% | +78.7% | 0.4% |
| Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings | 28.00 | 24.88 | 16.46 | 6.1% | 3.3% | 4.0% | +12.6% | +70.1% | 0.1% |
| Tari Eason REB over 11.5 (12+) | OKC @ HOU | draftkings | 21.00 | 18.66 | 12.35 | 8.1% | 4.5% | 5.4% | +12.6% | +70.1% | 0.2% |
| Kevin Durant REB over 9.5 (10+) | OKC @ HOU | draftkings | 14.60 | 13.04 | 8.71 | 11.5% | 6.4% | 7.7% | +12.0% | +67.5% | 0.2% |
| Shai Gilgeous-Alexander PTS over 44.5 (45+) | OKC @ HOU | draftkings | 15.00 | 13.46 | 9.07 | 11.0% | 6.2% | 7.4% | +11.4% | +65.4% | 0.2% |
| Kevin Durant REB over 7.5 (8+) | OKC @ HOU | draftkings | 5.50 | 5.03 | 3.51 | 28.5% | 17.0% | 19.9% | +9.3% | +56.8% | 0.5% |
| Shai Gilgeous-Alexander PRA over 59.5 (60+) | OKC @ HOU | draftkings | 19.40 | 17.76 | 12.40 | 8.1% | 4.8% | 5.6% | +9.2% | +56.5% | 0.1% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ HOU | draftkings | 9.90 | 9.13 | 6.46 | 15.5% | 9.4% | 10.9% | +8.4% | +53.3% | 0.2% |
| Shai Gilgeous-Alexander AST over 11.5 (12+) | OKC @ HOU | draftkings | 25.00 | 23.26 | 16.74 | 6.0% | 3.7% | 4.3% | +7.4% | +49.4% | 0.1% |
| Amen Thompson AST over 7.5 (8+) | OKC @ HOU | draftkings | 8.30 | 7.73 | 5.58 | 17.9% | 11.3% | 12.9% | +7.3% | +48.8% | 0.2% |
| Kenrich Williams REB over 7.5 (8+) | OKC @ HOU | draftkings | 7.10 | 6.62 | 4.78 | 20.9% | 13.2% | 15.1% | +7.2% | +48.5% | 0.3% |
| Amen Thompson PTS over 29.5 (30+) | OKC @ HOU | draftkings | 20.40 | 19.16 | 14.01 | 7.1% | 4.6% | 5.2% | +6.5% | +45.7% | 0.1% |
| Jabari Smith Jr. REB over 9.5 (10+) | OKC @ HOU | draftkings | 7.10 | 6.67 | 4.89 | 20.5% | 13.2% | 15.0% | +6.4% | +45.3% | 0.3% |
| Shai Gilgeous-Alexander PRA over 54.5 (55+) | OKC @ HOU | draftkings | 10.70 | 10.07 | 7.39 | 13.5% | 8.7% | 9.9% | +6.3% | +44.7% | 0.2% |
| Amen Thompson PRA over 39.5 (40+) | OKC @ HOU | draftkings | 9.10 | 8.61 | 6.40 | 15.6% | 10.3% | 11.6% | +5.7% | +42.2% | 0.2% |
| Kenrich Williams REB over 9.5 (10+) | OKC @ HOU | draftkings | 17.40 | 16.50 | 12.33 | 8.1% | 5.4% | 6.1% | +5.4% | +41.1% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 10.5 (11+) | OKC @ HOU | draftkings | 14.00 | 12.29 | 7.97 | 12.6% | 6.7% | 8.1% | +14.0% | +75.7% | 0.3% |
| Tari Eason REB over 8.5 (9+) | OKC @ HOU | draftkings | 5.90 | 5.27 | 3.52 | 28.4% | 15.8% | 19.0% | +12.0% | +67.7% | 0.6% |
| Kevin Durant REB over 8.5 (9+) | OKC @ HOU | draftkings | 9.00 | 8.06 | 5.41 | 18.5% | 10.4% | 12.4% | +11.7% | +66.5% | 0.4% |
| Shai Gilgeous-Alexander AST over 10.5 (11+) | OKC @ HOU | draftkings | 16.20 | 14.71 | 10.10 | 9.9% | 5.8% | 6.8% | +10.2% | +60.4% | 0.2% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 23.00 | 21.19 | 14.95 | 6.7% | 4.1% | 4.7% | +8.6% | +53.9% | 0.1% |
| Amen Thompson AST over 8.5 (9+) | OKC @ HOU | draftkings | 14.20 | 13.12 | 9.33 | 10.7% | 6.6% | 7.6% | +8.2% | +52.2% | 0.1% |
| Kenrich Williams REB over 8.5 (9+) | OKC @ HOU | draftkings | 11.20 | 10.45 | 7.55 | 13.2% | 8.3% | 9.6% | +7.2% | +48.3% | 0.2% |
| Kenrich Williams REB over 6.5 (7+) | OKC @ HOU | draftkings | 4.56 | 4.28 | 3.14 | 31.9% | 20.5% | 23.3% | +6.4% | +45.3% | 0.4% |
| Jabari Smith Jr. REB over 10.5 (11+) | OKC @ HOU | draftkings | 11.00 | 10.36 | 7.62 | 13.1% | 8.5% | 9.7% | +6.2% | +44.4% | 0.2% |
| Kevin Durant REB over 6.5 (7+) | OKC @ HOU | draftkings | 3.50 | 3.30 | 2.43 | 41.1% | 26.7% | 30.3% | +6.1% | +43.9% | 0.6% |
| Shai Gilgeous-Alexander AST over 8.5 (9+) | OKC @ HOU | draftkings | 6.11 | 5.76 | 4.26 | 23.5% | 15.3% | 17.3% | +6.0% | +43.5% | 0.3% |
| Tari Eason REB over 12.5 (13+) | OKC @ HOU | draftkings | 29.00 | 27.47 | 20.40 | 4.9% | 3.2% | 3.6% | +5.6% | +42.1% | 0.1% |
| Amen Thompson AST over 6.5 (7+) | OKC @ HOU | draftkings | 4.93 | 4.68 | 3.49 | 28.6% | 19.0% | 21.4% | +5.4% | +41.2% | 0.3% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.16 | 2.00 | 1.43 | 69.8% | 43.4% | 50.0% | +8.0% | +50.8% | 1.7% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 2.00 | 1.87 | 1.35 | 73.9% | 46.9% | 53.6% | +7.2% | +47.7% | 1.8% |
| Kenrich Williams PTS over 6.5 (7+) | OKC @ HOU | pointsbetau | 1.90 | 1.78 | 1.40 | 71.2% | 51.0% | 56.1% | +6.6% | +35.4% | 1.8% |

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
| Jared McCain PTS over 14.5 (15+) | OKC @ HOU | pointsbetau | 2.00 | 1.95 | 1.90 | 52.6% | 50.7% | 51.2% | +2.4% | +5.2% | 0.6% |
| Kenrich Williams REB over 4.5 (5+) | OKC @ HOU | draftkings | 2.08 | 2.05 | 1.67 | 59.8% | 45.1% | 48.8% | +1.5% | +24.3% | 0.4% |
| Kevin Durant PTS under 22.5 | OKC @ HOU | pointsbetau | 2.00 | 1.98 | 1.85 | 53.9% | 49.3% | 50.4% | +0.9% | +7.9% | 0.2% |
| Alperen Sengun PTS under 18.5 | OKC @ HOU | pointsbetau | 2.05 | 2.03 | 1.97 | 50.7% | 48.7% | 49.2% | +0.9% | +3.9% | 0.2% |
| Jaylin Williams REB under 5.5 | OKC @ HOU | draftkings | 2.05 | 2.03 | 1.67 | 59.9% | 45.6% | 49.2% | +0.8% | +22.8% | 0.2% |
| Aday Mara PTS under 7.5 | OKC @ HOU | pointsbetau | 2.00 | 1.99 | 1.88 | 53.2% | 49.2% | 50.2% | +0.4% | +6.4% | 0.1% |
| Shai Gilgeous-Alexander STL over 1.5 (2+) | OKC @ HOU | draftkings | 2.71 | 2.70 | 2.27 | 44.0% | 34.6% | 37.0% | +0.2% | +19.3% | 0.0% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 34.8<br><sub>36,35,36,30,28</sub> | 29.9<br><sub>32,17,34,26,21</sub> | 29.5 · 28.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,2,6,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 6.6<br><sub>4,3,5,3,2</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.9 | 3.3 | 40.4 |
| Jared McCain | 100% | 31.0<br><sub>22,18,21,30,29</sub> | 15.8<br><sub>20,4,3,18,10</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,0,1,3,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>2,1,0,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>6,0,1,4,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.9 | 21.2 |
| Ajay Mitchell | 100% | 30.2<br><sub>23,23,28,25,28</sub> | 18.9<br><sub>4,12,18,30,29</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,0,6,2,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>6,0,4,5,3</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.3 | 2.1 | 27.0 |
| Josh Dix | 67% | 26.9<br><sub>-,-,-,22,24</sub> | 4.3<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.2 |
| Isaiah Hartenstein | 100% | 26.6<br><sub>17,23,27,26,26</sub> | 9.9<br><sub>4,6,12,15,10</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 9.5<br><sub>3,6,12,13,14</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,2,1,3,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.8 | 1.7 | 22.5 |
| Bennett Stirtz | 96% | 26.4<br><sub>1,2,11,25,28</sub> | 7.7<br><sub>0,0,2,7,8</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> | 1.5<br><sub>o 32% · u 68%</sub> | 0.7 | 0.2 | 1.0 | 10.8 |
| Kenrich Williams | 100% | 26.3<br><sub>7,6,7,24,17</sub> | 9.6<br><sub>3,3,3,3,7</sub> | 6.5 · 6.5<br><sub>o 56% · u 44%</sub> | 5.4<br><sub>2,1,1,7,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,1,0,0,0</sub> |  | 1.4<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.2 | 1.1 | 16.8 |
| Aday Mara | 96% | 23.3<br><sub>12,13,14,20,21</sub> | 7.8<br><sub>7,2,2,11,6</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>2,3,3,10,3</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.3 | 15.0 |
| Jaylin Williams | 98% | 20.7<br><sub>17,15,5,26,20</sub> | 5.9<br><sub>5,3,0,6,0</sub> | 6.5 · 7.5<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>4,7,0,6,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,3,0,3,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.9<br><sub>1,1,0,2,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.5 | 0.5 | 0.8 | 12.9 |
| Micah Peavy | 48% | 13.0<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer | 80% | 12.4<br><sub>1,2,-,3,14</sub> | 3.2<br><sub>0,0,-,0,3</sub> |  | 2.4<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.3 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 100% | 37.0<br><sub>36,39,28,33,39</sub> | 17.8<br><sub>20,17,15,23,15</sub> | 15.5 · 16.5<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>10,11,5,4,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.2<br><sub>4,6,2,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.5 | 0.6 | 2.5 | 30.4 |
| Kevin Durant | 100% | 36.2<br><sub>37,37,30,31,37</sub> | 22.8<br><sub>20,22,22,18,28</sub> | 22.5 · 23.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>7,4,9,5,5</sub> | 4.5<br><sub>o 60% · u 40%</sub> | 4.9<br><sub>6,2,3,4,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,3,1,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 1.0 | 3.6 | 33.9 |
| Jabari Smith Jr. | 100% | 36.0<br><sub>34,33,39,30,35</sub> | 15.8<br><sub>7,14,16,14,22</sub> | 14.5 · 15.5<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>5,5,12,2,3</sub> | 5.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>1,3,5,2,2</sub> |  | 2.5<br><sub>1,2,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.8 | 1.6 | 25.0 |
| Alperen Sengun | 100% | 34.9<br><sub>36,33,37,-,-</sub> | 19.4<br><sub>29,17,29,-,-</sub> | 18.5 · 18.5<br><sub>o 51% · u 49%</sub> | 9.9<br><sub>7,10,9,-,-</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>7,7,9,-,-</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.7<br><sub>2,1,1,-,-</sub> |  | 1.2 | 0.9 | 3.4 | 35.5 |
| Tari Eason | 98% | 28.3<br><sub>27,31,33,31,26</sub> | 11.4<br><sub>12,19,13,5,11</sub> | 10.5 · 10.5<br><sub>o 49% · u 51%</sub> | 6.9<br><sub>6,3,8,9,13</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,0,2,1,2</sub> |  | 1.2<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.7 | 1.4 | 19.8 |
| Marcus Smart | 100% | 27.4<br><sub>21,-,-,-,17</sub> | 9.5<br><sub>5,-,-,-,8</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>3,-,-,-,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>1,-,-,-,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,-,-,-,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.3 | 2.0 | 15.7 |
| Clint Capela | 88% | 19.9<br><sub>-,11,4,22,30</sub> | 5.8<br><sub>-,2,2,10,5</sub> |  | 7.0<br><sub>-,3,2,8,11</sub> |  | 1.2<br><sub>-,1,0,2,5</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.7 | 1.1 | 0.9 | 14.0 |
| Bogdan Bogdanovic | 91% | 16.4<br><sub>9,20,13,15,11</sub> | 6.0<br><sub>3,11,5,16,6</sub> | 7.5 · 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,1,2,2,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.6<br><sub>0,1,1,4,0</sub> | 2.5<br><sub>o 35% · u 65%</sub> | 0.9<br><sub>1,3,1,4,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.1 | 0.8 | 9.7 |
| Oscar Tshiebwe | 76% | 14.3<br><sub>-,-,-,14,11</sub> | 5.5<br><sub>-,-,-,7,0</sub> |  | 5.8<br><sub>-,-,-,5,5</sub> |  | 0.8<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 12.1 |
| Jae'Sean Tate | 64% | 7.0<br><sub>-,1,1,4,-</sub> | 2.2<br><sub>-,0,0,0,-</sub> |  | 1.5<br><sub>-,0,1,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.1<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Bruce Thornton | 63% | 6.5<br><sub>-,4,1,3,-</sub> | 2.1<br><sub>-,0,0,5,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.6<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.1 | 0.1 | 0.3 | 2.9 |
| Isaiah Crawford | 58% | 6.1<br><sub>-,1,1,5,-</sub> | 2.0<br><sub>-,0,0,3,-</sub> |  | 1.1<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.1<br><sub>-,0,0,1,-</sub> |  | 0.1 | 0.2 | 0.2 | 3.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-31/`._
