# NBA model · Mon 02 Nov 2026 (US date)

Updated **Mon 02 Nov, 09:38 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-02/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama BLK over 4.5 (5+) | UTA @ SAS | draftkings | 3.73 | 3.53 | 2.62 | 38.2% | 25.1% | 28.3% | +5.7% | +42.4% | 0.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam PRA over 54.5 (55+) | ATL @ IND | draftkings | 21.00 | 17.36 | 10.34 | 9.7% | 4.5% | 5.8% | +20.9% | +103.2% | 0.3% |
| Pascal Siakam PR over 49.5 (50+) | ATL @ IND | draftkings | 21.00 | 17.42 | 10.41 | 9.6% | 4.5% | 5.7% | +20.5% | +101.8% | 0.3% |
| Aday Mara REB over 11.5 (12+) | OKC @ CLE | draftkings | 15.40 | 12.95 | 7.90 | 12.7% | 6.1% | 7.7% | +18.9% | +95.0% | 0.3% |
| Scottie Barnes AST over 9.5 (10+) | TOR @ LAC | draftkings | 10.00 | 8.45 | 5.18 | 19.3% | 9.3% | 11.8% | +18.4% | +93.2% | 0.5% |
| Zion Williamson AST over 5.5 (6+) | NOP @ MEM | draftkings | 13.00 | 11.04 | 6.82 | 14.7% | 7.2% | 9.1% | +17.7% | +90.5% | 0.4% |
| Scottie Barnes AST over 11.5 (12+) | TOR @ LAC | draftkings | 25.00 | 21.28 | 13.17 | 7.6% | 3.7% | 4.7% | +17.5% | +89.8% | 0.2% |
| Joan Beringer PRA over 24.5 (25+) | MIL @ MIN | draftkings | 10.00 | 8.55 | 5.33 | 18.8% | 9.3% | 11.7% | +17.0% | +87.6% | 0.5% |
| Darius Acuff Jr. REB over 7.5 (8+) | SAC @ DAL | draftkings | 18.20 | 15.58 | 9.72 | 10.3% | 5.1% | 6.4% | +16.9% | +87.3% | 0.2% |
| Kevin Durant AST over 7.5 (8+) | BOS @ HOU | draftkings | 18.00 | 15.41 | 9.62 | 10.4% | 5.2% | 6.5% | +16.9% | +87.1% | 0.2% |
| Jayson Tatum REB over 13.5 (14+) | BOS @ HOU | draftkings | 18.80 | 16.23 | 10.29 | 9.7% | 5.0% | 6.2% | +15.8% | +82.7% | 0.2% |
| Joan Beringer PTS over 14.5 (15+) | MIL @ MIN | draftkings | 9.10 | 7.90 | 5.05 | 19.8% | 10.3% | 12.7% | +15.2% | +80.3% | 0.5% |
| Jayson Tatum REB over 11.5 (12+) | BOS @ HOU | draftkings | 8.30 | 7.25 | 4.67 | 21.4% | 11.3% | 13.8% | +14.5% | +77.8% | 0.5% |
| Aday Mara REB over 9.5 (10+) | OKC @ CLE | draftkings | 6.77 | 5.91 | 3.82 | 26.2% | 13.8% | 16.9% | +14.4% | +77.4% | 0.6% |
| Victor Wembanyama PA over 49.5 (50+) | UTA @ SAS | draftkings | 26.00 | 22.78 | 14.73 | 6.8% | 3.6% | 4.4% | +14.2% | +76.5% | 0.1% |
| Darius Acuff Jr. REB over 5.5 (6+) | SAC @ DAL | draftkings | 5.74 | 5.04 | 3.27 | 30.6% | 16.3% | 19.9% | +14.0% | +75.5% | 0.7% |
| Victor Wembanyama BLK over 6.5 (7+) | UTA @ SAS | draftkings | 12.20 | 10.86 | 7.22 | 13.9% | 7.7% | 9.2% | +12.4% | +69.1% | 0.3% |
| Desmond Bane PA over 39.5 (40+) | WAS @ ORL | draftkings | 13.00 | 11.61 | 7.77 | 12.9% | 7.2% | 8.6% | +11.9% | +67.4% | 0.2% |
| Joan Beringer PRA over 29.5 (30+) | MIL @ MIN | draftkings | 21.00 | 18.80 | 12.64 | 7.9% | 4.5% | 5.3% | +11.6% | +66.2% | 0.1% |
| Franz Wagner PA over 44.5 (45+) | WAS @ ORL | draftkings | 12.80 | 11.48 | 7.73 | 12.9% | 7.3% | 8.7% | +11.5% | +65.6% | 0.2% |
| Franz Wagner PA over 49.5 (50+) | WAS @ ORL | draftkings | 24.00 | 21.55 | 14.55 | 6.9% | 3.9% | 4.6% | +11.3% | +65.0% | 0.1% |
| Jrue Holiday AST over 7.5 (8+) | POR @ DEN | draftkings | 9.20 | 8.31 | 5.66 | 17.6% | 10.2% | 12.0% | +10.7% | +62.4% | 0.3% |
| Brandin Podziemski AST over 9.5 (10+) | PHX @ GSW | draftkings | 27.00 | 24.45 | 16.68 | 6.0% | 3.5% | 4.1% | +10.6% | +61.9% | 0.1% |
| Victor Wembanyama BLK over 5.5 (6+) | UTA @ SAS | draftkings | 6.76 | 6.12 | 4.20 | 23.8% | 13.8% | 16.3% | +10.4% | +61.1% | 0.4% |
| Desmond Bane PRA over 44.5 (45+) | WAS @ ORL | draftkings | 12.00 | 10.91 | 7.51 | 13.3% | 7.8% | 9.2% | +10.0% | +59.7% | 0.2% |
| Desmond Bane PA over 44.5 (45+) | WAS @ ORL | draftkings | 24.00 | 21.83 | 15.09 | 6.6% | 3.9% | 4.6% | +9.8% | +59.0% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski PA over 24.5 (25+) | PHX @ GSW | draftkings | 3.58 | Gui Santos | 49.5% | 40.7% | +8.9% |
| Nolan Traore PA under 15.5 | BKN @ NYK | draftkings | 1.96 | Mikel Brown Jr. | 71.7% | 81.1% | +8.6% |
| Nolan Traore RA under 6.5 | BKN @ NYK | draftkings | 2.03 | Mikel Brown Jr. | 69.1% | 77.3% | +8.4% |
| Nolan Traore AST under 4.5 | BKN @ NYK | draftkings | 1.92 | Mikel Brown Jr. | 73.2% | 80.8% | +7.9% |
| Nolan Traore PRA under 18.5 | BKN @ NYK | draftkings | 1.81 | Mikel Brown Jr. | 74.9% | 83.7% | +7.0% |
| Keaton Wagler RA under 8.5 | TOR @ LAC | draftkings | 2.04 | Derrick Jones Jr. | 68.5% | 72.9% | +6.8% |
| Precious Achiuwa PR over 24.5 (25+) | SAC @ DAL | draftkings | 3.44 | Zach LaVine | 51.7% | 40.1% | +6.8% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes AST over 7.5 (8+) | TOR @ LAC | draftkings | 3.82 | 3.54 | 2.52 | 39.7% | 24.5% | 28.3% | +8.0% | +51.5% | 0.7% |
| Zion Williamson AST over 3.5 (4+) | NOP @ MEM | draftkings | 3.50 | 3.25 | 2.32 | 43.1% | 26.7% | 30.8% | +7.8% | +51.0% | 0.8% |
| Jayson Tatum REB over 9.5 (10+) | BOS @ HOU | draftkings | 3.77 | 3.50 | 2.51 | 39.8% | 24.8% | 28.5% | +7.6% | +50.1% | 0.7% |
| Aday Mara REB over 7.5 (8+) | OKC @ CLE | draftkings | 3.17 | 2.96 | 2.13 | 46.9% | 29.5% | 33.8% | +7.3% | +48.7% | 0.8% |
| Khaman Maluach PR under 15.5 | PHX @ GSW | draftkings | 1.82 | 1.72 | 1.28 | 78.0% | 51.4% | 58.0% | +5.6% | +42.0% | 1.7% |
| Joan Beringer PTS over 9.5 (10+) | MIL @ MIN | draftkings | 2.84 | 2.70 | 2.02 | 49.5% | 32.9% | 37.1% | +5.2% | +40.6% | 0.7% |
| Damian Lillard PTS under 20.5 | POR @ DEN | draftkings | 1.95 | 1.86 | 1.40 | 71.5% | 47.9% | 53.8% | +5.0% | +39.6% | 1.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ CLE | Tue 03 Nov 11:00 | 111.8–113.4 | OKC 45% | 2.21 / 1.83 | CLE -2.5 | 224.5 | CLE -4.5 covers 43%; o228.5 42% |
| DET @ CHA | Tue 03 Nov 11:30 | 108.6–105.8 | DET 57% | 1.74 / 2.35 | CHA +2.5 | 214.5 | CHA +4.5 covers 55%; o210.5 58% |
| ATL @ IND | Tue 03 Nov 11:30 | 118.1–117.4 | ATL 52% | 1.91 / 2.09 | IND +1.5 | 235.5 | IND +5.5 covers 63%; o232.5 57% |
| BKN @ NYK | Tue 03 Nov 11:30 | 103.8–117.5 | BKN 16% | 6.10 / 1.20 | NYK -13.5 | 221.5 | NYK -14.5 covers 48%; o220.5 52% |
| WAS @ ORL | Tue 03 Nov 11:30 | 111.2–117.3 | WAS 33% | 3.01 / 1.50 | ORL -6.5 | 228.5 | ORL -1.5 covers 64%; o223.5 60% |
| CHI @ PHI | Tue 03 Nov 11:30 | 113.5–120.1 | CHI 32% | 3.14 / 1.47 | PHI -6.5 | 233.5 | PHI -11.5 covers 37%; o239.5 38% |
| SAC @ DAL | Tue 03 Nov 12:00 | 114.2–123.6 | SAC 26% | 3.92 / 1.34 | DAL -9.5 | 237.5 | DAL -10.5 covers 47%; o234.5 57% |
| NOP @ MEM | Tue 03 Nov 12:00 | 118.6–122.1 | NOP 40% | 2.49 / 1.67 | MEM -3.5 | 240.5 | MEM -6.5 covers 42%; o234.5 62% |
| MIL @ MIN | Tue 03 Nov 12:00 | 108.1–117.3 | MIL 26% | 3.89 / 1.35 | MIN -9.5 | 225.5 | MIN -10.5 covers 47%; o234.5 31% |
| BOS @ HOU | Tue 03 Nov 12:30 | 111.2–109.5 | BOS 55% | 1.81 / 2.24 | HOU +2.5 | 220.5 | HOU -4.5 covers 33%; o219.5 52% |
| UTA @ SAS | Tue 03 Nov 12:30 | 109.9–125.3 | UTA 14% | 7.14 / 1.16 | SAS -15.5 | 234.5 | SAS -16.5 covers 47%; o231.5 58% |
| POR @ DEN | Tue 03 Nov 13:00 | 114.6–121.5 | POR 31% | 3.22 / 1.45 | DEN -6.5 | 236.5 | DEN -4.5 covers 57%; o230.5 62% |
| PHX @ GSW | Tue 03 Nov 14:00 | 115.1–114.4 | PHX 52% | 1.93 / 2.07 | GSW +1.5 | 229.5 | GSW -4.5 covers 36%; o227.5 54% |
| TOR @ LAC | Tue 03 Nov 14:00 | 112.0–109.1 | TOR 58% | 1.72 / 2.39 | LAC +3.5 | 220.5 | LAC +5.5 covers 57%; o220.5 51% |
| MIA @ LAL | Tue 03 Nov 14:00 | 115.9–121.4 | MIA 35% | 2.84 / 1.54 | LAL -5.5 | 237.5 | LAL -2.5 covers 59%; o237.5 49% |

### OKC @ CLE
Out: Jaylon Tyson (CLE), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aday Mara PR over 14.5 (15+) | OKC @ CLE | draftkings | 1.98 | 1.97 | 1.63 | 61.3% | 47.3% | 50.8% | +0.6% | +21.4% | 0.2% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.8–113.4 | OKC 45% | 2.21 / 1.83 | CLE -2.5 | 224.5 | CLE -4.5 covers 43%; o228.5 42% |
| Expected (weighted by chance each plays) | 111.5–114.0 | OKC 44% | 2.30 / 1.77 | CLE -2.5 | 225.5 | CLE -4.5 covers 45%; o228.5 43% |
| if Peyton Watson plays | 111.2–114.5 | OKC 41% | 2.42 / 1.70 | CLE -3.5 | 225.5 | CLE -4.5 covers 47%; o228.5 43% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Peyton Watson (CLE) | Questionable | 55% | 27.7 | 12.2 | 4.4 | 2.1 | 1.3 | 0.9 | 1.2 | 1.8 | 18.8 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.3<br><sub>35,36,30,28,31</sub> | 28.0<br><sub>17,34,26,21,26</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>2,6,3,6,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>3,5,3,2,3</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>3,1,1,1,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.9 | 3.2 | 38.2 |
| Jared McCain | 98% | 29.7<br><sub>18,21,30,29,28</sub> | 14.5<br><sub>4,3,18,10,10</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>0,1,3,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.3<br><sub>0,1,4,0,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.1 | 1.7 | 19.8 |
| Ajay Mitchell | 98% | 28.3<br><sub>23,28,25,28,26</sub> | 15.9<br><sub>12,18,30,29,6</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>0,6,2,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>0,4,5,3,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.8 | 23.6 |
| Aday Mara | 96% | 27.0<br><sub>13,14,20,21,28</sub> | 9.2<br><sub>2,2,11,6,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 7.6<br><sub>3,3,10,3,9</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.8 | 1.9 | 18.6 |
| Bennett Stirtz | 96% | 26.8<br><sub>2,11,25,28,26</sub> | 7.9<br><sub>0,2,7,8,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,1,1,0,1</sub> |  | 2.2<br><sub>0,0,1,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>0,0,1,1,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.2 | 1.0 | 11.9 |
| Isaiah Hartenstein | 98% | 26.3<br><sub>23,27,26,26,25</sub> | 10.2<br><sub>6,12,15,10,10</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 9.7<br><sub>6,12,13,14,7</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,1,3,3,0</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.7 | 1.8 | 23.0 |
| Jaylin Williams | 98% | 24.4<br><sub>15,5,26,20,26</sub> | 7.8<br><sub>3,0,6,0,3</sub> |  | 6.0<br><sub>7,0,6,5,4</sub> |  | 2.4<br><sub>3,0,3,1,1</sub> |  | 1.2<br><sub>1,0,2,0,0</sub> |  | 0.7 | 0.5 | 0.9 | 16.1 |
| Kenrich Williams | 96% | 23.5<br><sub>6,7,24,17,21</sub> | 8.9<br><sub>3,3,3,7,11</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>1,1,7,3,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,0,0,0,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.1 | 0.9 | 16.0 |
| Josh Dix | 76% | 20.6<br><sub>-,-,22,24,9</sub> | 6.7<br><sub>-,-,0,2,7</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.2 | 0.7 | 10.3 |
| Micah Peavy | 58% | 16.0<br><sub>-,-,-,5,14</sub> | 6.4<br><sub>-,-,-,0,2</sub> |  | 3.9<br><sub>-,-,-,0,1</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.3 | 0.7 | 11.0 |
| Brooks Barnhizer | 86% | 11.5<br><sub>2,-,3,14,6</sub> | 2.8<br><sub>0,-,0,3,5</sub> |  | 2.3<br><sub>0,-,0,2,2</sub> |  | 0.7<br><sub>1,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.8 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.8<br><sub>33,39,34,36,26</sub> | 18.3<br><sub>12,19,16,24,13</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>8,5,2,5,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>7,9,6,4,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,3,2,3,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3 | 0.5 | 3.8 | 29.9 |
| Donovan Mitchell | 98% | 36.5<br><sub>35,38,31,33,24</sub> | 24.4<br><sub>22,26,19,22,15</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>5,5,5,3,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.8<br><sub>4,7,7,3,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>2,5,2,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.3 | 3.2 | 34.4 |
| Evan Mobley | 98% | 35.2<br><sub>35,38,32,33,25</sub> | 18.5<br><sub>20,18,24,11,27</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>10,10,12,4,5</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>4,3,2,7,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,4,5,0,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 1.5 | 2.1 | 31.1 |
| Jarrett Allen | 98% | 30.0<br><sub>27,27,30,30,24</sub> | 13.8<br><sub>21,10,8,14,25</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 9.1<br><sub>8,9,12,8,11</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,2,2,1,4</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.1<br><sub>1,0,0,1,0</sub> |  | 0.9 | 1.2 | 1.4 | 24.4 |
| Sam Merrill | 98% | 26.3<br><sub>21,31,20,27,19</sub> | 10.0<br><sub>7,9,8,16,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>2,4,1,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>3,2,1,3,3</sub> |  | 1.9<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 0.8 | 14.7 |
| Meleek Thomas | 67% | 22.6<br><sub>-,19,20,-,23</sub> | 9.0<br><sub>-,16,10,-,13</sub> |  | 2.8<br><sub>-,2,4,-,1</sub> |  | 1.3<br><sub>-,0,1,-,2</sub> |  | 1.2<br><sub>-,4,0,-,3</sub> |  | 0.7 | 0.3 | 1.3 | 13.1 |
| Tyrese Proctor | 80% | 19.4<br><sub>11,-,6,20,18</sub> | 8.1<br><sub>5,-,2,7,9</sub> |  | 2.8<br><sub>2,-,1,6,4</sub> |  | 2.6<br><sub>3,-,1,2,5</sub> |  | 1.2<br><sub>1,-,0,1,3</sub> |  | 0.8 | 0.1 | 1.2 | 13.5 |
| Mario Hezonja | 96% | 18.7<br><sub>20,15,17,17,20</sub> | 7.2<br><sub>9,3,5,10,8</sub> |  | 4.5<br><sub>5,3,3,6,11</sub> |  | 1.7<br><sub>1,1,2,2,4</sub> |  | 0.9<br><sub>2,1,1,2,1</sub> |  | 0.6 | 0.3 | 0.9 | 13.4 |
| Craig Porter Jr. | 66% | 14.2<br><sub>5,-,-,4,16</sub> | 3.5<br><sub>3,-,-,0,2</sub> |  | 2.5<br><sub>1,-,-,1,2</sub> |  | 2.3<br><sub>1,-,-,0,4</sub> |  | 0.3<br><sub>1,-,-,0,0</sub> |  | 0.7 | 0.4 | 0.9 | 8.3 |
| Thomas Bryant | 48% | 11.7<br><sub>-,-,-,-,11</sub> | 5.8<br><sub>-,-,-,-,11</sub> |  | 3.1<br><sub>-,-,-,-,2</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,3</sub> |  | 0.3 | 0.4 | 0.5 | 9.5 |
| Riley Minix | 43% | 11.3<br><sub>-,-,-,-,6</sub> | 4.4<br><sub>-,-,-,-,0</sub> |  | 1.7<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.7 |
| Tristan Enaruna | 48% | 10.1<br><sub>-,-,-,-,6</sub> | 3.8<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.1 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |

</details>

<details><summary>if Peyton Watson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden (CLE) | 98% | 35.3<br><sub>33,39,34,36,26</sub> | 17.3<br><sub>12,19,16,24,13</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 4.9<br><sub>8,5,2,5,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>7,9,6,4,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,3,2,3,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.2 | 0.5 | 3.6 | 28.4 |
| Donovan Mitchell (CLE) | 98% | 35.1<br><sub>35,38,31,33,24</sub> | 23.0<br><sub>22,26,19,22,15</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,5,5,3,4</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>4,7,7,3,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,5,2,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.3 | 2.9 | 32.5 |
| Evan Mobley (CLE) | 98% | 33.5<br><sub>35,38,32,33,25</sub> | 17.2<br><sub>20,18,24,11,27</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>10,10,12,4,5</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,3,2,7,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>2,4,5,0,3</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8 | 1.4 | 1.9 | 29.1 |
| Jarrett Allen (CLE) | 98% | 28.4<br><sub>27,27,30,30,24</sub> | 13.4<br><sub>21,10,8,14,25</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 8.7<br><sub>8,9,12,8,11</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>0,2,2,1,4</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.1<br><sub>1,0,0,1,0</sub> |  | 0.9 | 1.1 | 1.3 | 23.5 |
| Peyton Watson (CLE) | 100% | 27.7<br><sub>31,37,28,22,22</sub> | 12.2<br><sub>11,15,22,4,5</sub> | 13.5 · – | 4.4<br><sub>3,8,6,4,2</sub> | 4.5 | 2.1<br><sub>4,1,2,3,6</sub> | 1.5 | 1.3<br><sub>2,0,1,0,1</sub> | 1.5 | 0.9 | 1.2 | 1.8 | 18.8 |
| Sam Merrill (CLE) | 98% | 21.8<br><sub>21,31,20,27,19</sub> | 8.2<br><sub>7,9,8,16,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>2,4,1,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>3,2,1,3,3</sub> |  | 1.4<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.7 | 12.0 |
| Meleek Thomas (CLE) | 67% | 19.9<br><sub>-,19,20,-,23</sub> | 8.3<br><sub>-,16,10,-,13</sub> |  | 2.5<br><sub>-,2,4,-,1</sub> |  | 1.2<br><sub>-,0,1,-,2</sub> |  | 1.0<br><sub>-,4,0,-,3</sub> |  | 0.6 | 0.2 | 1.1 | 12.0 |
| Mario Hezonja (CLE) | 96% | 16.4<br><sub>20,15,17,17,20</sub> | 6.5<br><sub>9,3,5,10,8</sub> |  | 4.0<br><sub>5,3,3,6,11</sub> |  | 1.5<br><sub>1,1,2,2,4</sub> |  | 0.7<br><sub>2,1,1,2,1</sub> |  | 0.5 | 0.3 | 0.9 | 12.0 |
| Tyrese Proctor (CLE) | 80% | 15.3<br><sub>11,-,6,20,18</sub> | 6.4<br><sub>5,-,2,7,9</sub> |  | 2.2<br><sub>2,-,1,6,4</sub> |  | 2.1<br><sub>3,-,1,2,5</sub> |  | 0.9<br><sub>1,-,0,1,3</sub> |  | 0.6 | 0.1 | 0.9 | 10.7 |
| Craig Porter Jr. (CLE) | 66% | 11.1<br><sub>5,-,-,4,16</sub> | 2.9<br><sub>3,-,-,0,2</sub> |  | 2.1<br><sub>1,-,-,1,2</sub> |  | 1.8<br><sub>1,-,-,0,4</sub> |  | 0.2<br><sub>1,-,-,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 6.8 |
| Thomas Bryant (CLE) | 48% | 8.6<br><sub>-,-,-,-,11</sub> | 4.4<br><sub>-,-,-,-,11</sub> |  | 2.3<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,3</sub> |  | 0.2 | 0.3 | 0.4 | 7.0 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Tristan Enaruna (CLE) | 48% | 7.7<br><sub>-,-,-,-,6</sub> | 3.1<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.8 |
| Riley Minix (CLE) | 43% | 7.6<br><sub>-,-,-,-,6</sub> | 3.2<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,3</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Shai Gilgeous-Alexander (OKC) | 98% | 34.3<br><sub>35,36,30,28,31</sub> | 27.8<br><sub>17,34,26,21,26</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,6,3,6,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>3,5,3,2,3</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>3,1,1,1,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.9 | 3.1 | 38.1 |
| Jared McCain (OKC) | 98% | 29.6<br><sub>18,21,30,29,28</sub> | 14.5<br><sub>4,3,18,10,10</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>0,1,3,4,4</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 2.3<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.3<br><sub>0,1,4,0,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.1 | 1.6 | 19.8 |
| Ajay Mitchell (OKC) | 98% | 28.4<br><sub>23,28,25,28,26</sub> | 16.0<br><sub>12,18,30,29,6</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>0,6,2,4,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>0,4,5,3,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.1<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.3 | 1.8 | 23.8 |
| Aday Mara (OKC) | 96% | 27.0<br><sub>13,14,20,21,28</sub> | 9.3<br><sub>2,2,11,6,7</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 7.6<br><sub>3,3,10,3,9</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.8 | 1.9 | 18.7 |
| Bennett Stirtz (OKC) | 96% | 26.8<br><sub>2,11,25,28,26</sub> | 7.9<br><sub>0,2,7,8,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,1,1,0,1</sub> |  | 2.1<br><sub>0,0,1,3,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1<br><sub>0,0,1,1,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 1.0 | 11.8 |
| Isaiah Hartenstein (OKC) | 98% | 26.2<br><sub>23,27,26,26,25</sub> | 10.1<br><sub>6,12,15,10,10</sub> | 10.5 · –<br><sub>o 45% · u 55%</sub> | 9.7<br><sub>6,12,13,14,7</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,1,3,3,0</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.7 | 1.8 | 22.9 |
| Jaylin Williams (OKC) | 98% | 24.4<br><sub>15,5,26,20,26</sub> | 7.8<br><sub>3,0,6,0,3</sub> |  | 5.9<br><sub>7,0,6,5,4</sub> |  | 2.4<br><sub>3,0,3,1,1</sub> |  | 1.2<br><sub>1,0,2,0,0</sub> |  | 0.7 | 0.5 | 0.9 | 16.1 |
| Kenrich Williams (OKC) | 96% | 23.5<br><sub>6,7,24,17,21</sub> | 8.9<br><sub>3,3,3,7,11</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>1,1,7,3,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,0,0,0,3</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.2 | 1.0 | 16.0 |
| Josh Dix (OKC) | 76% | 20.6<br><sub>-,-,22,24,9</sub> | 6.6<br><sub>-,-,0,2,7</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.1 | 0.7 | 10.2 |
| Micah Peavy (OKC) | 58% | 16.0<br><sub>-,-,-,5,14</sub> | 6.3<br><sub>-,-,-,0,2</sub> |  | 3.9<br><sub>-,-,-,0,1</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 10.9 |
| Brooks Barnhizer (OKC) | 86% | 11.5<br><sub>2,-,3,14,6</sub> | 2.9<br><sub>0,-,0,3,5</sub> |  | 2.4<br><sub>0,-,0,2,2</sub> |  | 0.7<br><sub>1,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.9 |

</details>


### DET @ CHA
Out: Kon Knueppel (CHA), Grant Williams (CHA), Jalen Duren (DET)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Duncan Robinson 3PM under 2.5 | DET @ CHA | draftkings | 2.30 | 2.27 | 1.85 | 54.0% | 40.6% | 44.0% | +1.1% | +24.1% | 0.2% |
| Sion James 3PM under 0.5 | DET @ CHA | draftkings | 2.59 | 2.59 | 2.16 | 46.2% | 36.1% | 38.6% | +0.0% | +19.7% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.6–105.8 | DET 57% | 1.74 / 2.35 | CHA +2.5 | 214.5 | CHA +4.5 covers 55%; o210.5 58% |
| Expected (weighted by chance each plays) | 108.8–106.2 | DET 57% | 1.76 / 2.31 | CHA +2.5 | 214.5 | CHA +4.5 covers 55%; o210.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Isaiah Joe (DET) | Questionable | 55% | 12.2 | 6.0 | 1.5 | 0.8 | 0.8 | 0.4 | 0.1 | 0.5 | 8.2 | small |
| Elijah Harkless (DET) | Questionable | 55% | 7.2 | 0.4 | 0.3 | 0.4 | 0.0 | 0.2 | 0.2 | 0.3 | 1.1 | small |
| Isaac Jones (DET) | Questionable | 55% | 5.8 | 0.3 | 0.2 | 0.3 | 0.0 | 0.2 | 0.2 | 0.2 | 0.8 | small |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 34.9<br><sub>30,33,36,39,28</sub> | 24.4<br><sub>16,26,19,30,20</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>2,8,9,5,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 7.8<br><sub>8,8,8,7,4</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>2,3,2,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.8 | 4.0 | 37.4 |
| Duncan Robinson | 98% | 30.5<br><sub>28,32,33,32,26</sub> | 14.1<br><sub>17,21,12,13,17</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>1,3,0,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,3,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>5,5,2,3,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.2 | 1.1 | 18.8 |
| Ausar Thompson | 98% | 27.9<br><sub>19,-,25,29,26</sub> | 9.6<br><sub>4,-,11,7,11</sub> | 10.5 · –<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>3,-,6,9,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>5,-,2,8,6</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 0.1<br><sub>0,-,0,0,0</sub> |  | 2.0 | 1.0 | 1.6 | 19.9 |
| Paul Reed | 96% | 27.4<br><sub>26,23,26,38,31</sub> | 14.1<br><sub>19,8,22,16,12</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>11,8,9,4,4</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,2,3,0,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.6<br><sub>2,0,1,2,0</sub> | 0.5<br><sub>o 36% · u 64%</sub> | 1.4 | 1.3 | 1.6 | 23.4 |
| John Collins | 98% | 27.0<br><sub>29,34,27,18,26</sub> | 10.9<br><sub>23,16,2,4,4</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>7,11,9,2,9</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>1,0,1,0,0</sub> |  | 1.1<br><sub>5,2,0,0,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.8 | 0.8 | 1.2 | 17.6 |
| Daniss Jenkins | 98% | 25.8<br><sub>22,38,24,24,24</sub> | 11.1<br><sub>15,18,11,14,6</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 3.1<br><sub>5,8,3,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>5,6,2,3,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>1,3,1,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.3 | 1.5 | 18.2 |
| Kevin Huerter | 96% | 22.4<br><sub>20,26,16,19,24</sub> | 7.8<br><sub>5,9,7,3,8</sub> |  | 2.9<br><sub>6,3,1,2,1</sub> |  | 2.3<br><sub>2,2,0,3,3</sub> |  | 1.1<br><sub>1,1,1,1,2</sub> |  | 1.0 | 0.3 | 0.8 | 13.1 |
| Javonte Green | 96% | 21.3<br><sub>13,22,17,21,22</sub> | 7.1<br><sub>5,2,3,7,6</sub> |  | 3.2<br><sub>3,3,1,2,3</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 1.1<br><sub>1,0,1,1,1</sub> |  | 1.3 | 0.5 | 0.6 | 11.2 |
| Ronald Holland II | 96% | 18.7<br><sub>22,23,12,12,22</sub> | 7.0<br><sub>8,2,4,0,18</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,9,3,2,3</sub> |  | 1.3<br><sub>4,4,2,1,2</sub> |  | 0.6<br><sub>0,0,0,0,2</sub> |  | 1.0 | 0.5 | 1.0 | 12.0 |
| Taurean Prince | 52% | 9.7<br><sub>-,-,7,6,-</sub> | 3.4<br><sub>-,-,3,1,-</sub> |  | 1.3<br><sub>-,-,0,2,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.3 |
| Tolu Smith | 86% | 6.9<br><sub>2,3,6,1,3</sub> | 2.7<br><sub>0,0,1,2,2</sub> |  | 2.1<br><sub>1,1,4,1,1</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.1 | 0.3 | 0.4 | 5.1 |
| Chaz Lanier | 52% | 6.4<br><sub>-,-,2,-,3</sub> | 2.4<br><sub>-,-,2,-,6</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,2</sub> |  | 0.2 | 0.1 | 0.1 | 3.4 |
| Ebuka Okorie | 58% | 5.9<br><sub>-,2,4,-,3</sub> | 2.1<br><sub>-,2,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.6<br><sub>-,0,2,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 3.0 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 33.9<br><sub>36,36,38,37,33</sub> | 23.0<br><sub>34,39,31,19,24</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>8,6,12,7,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 3.0<br><sub>4,1,3,2,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.2<br><sub>3,5,3,3,5</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.7 | 3.1 | 31.4 |
| Dennis Schroder | 98% | 31.9<br><sub>38,36,34,29,35</sub> | 12.8<br><sub>25,8,14,8,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>6,2,4,2,3</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 5.0<br><sub>4,5,5,8,7</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>3,0,2,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.2 | 2.7 | 21.0 |
| Moussa Diabate | 98% | 29.8<br><sub>22,35,35,31,28</sub> | 8.8<br><sub>4,11,9,10,10</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 9.0<br><sub>5,17,9,12,8</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,3,2,1,3</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.6 | 19.8 |
| Naz Reid | 98% | 29.7<br><sub>37,29,13,31,36</sub> | 16.4<br><sub>23,18,7,12,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,12,6,11,5</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>0,1,0,1,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.1<br><sub>5,2,1,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.9 | 2.4 | 26.0 |
| Grayson Allen | 96% | 28.2<br><sub>34,28,30,21,30</sub> | 14.6<br><sub>20,15,9,5,27</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>3,2,5,3,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>5,1,2,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,2,2,1,7</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 1.9 | 20.4 |
| Sion James | 98% | 22.1<br><sub>26,29,23,29,18</sub> | 5.4<br><sub>0,5,5,6,4</sub> | 5.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>5,2,2,5,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>5,3,3,4,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.7<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 0.7 | 0.2 | 0.8 | 10.5 |
| Royce O'Neale | 98% | 21.1<br><sub>11,7,34,17,23</sub> | 6.5<br><sub>0,0,9,7,8</sub> |  | 3.6<br><sub>1,0,4,3,6</sub> |  | 1.1<br><sub>0,1,0,1,1</sub> |  | 1.2<br><sub>0,0,3,2,1</sub> |  | 0.7 | 0.4 | 0.7 | 11.2 |
| Ryan Kalkbrenner | 98% | 17.0<br><sub>23,13,13,15,19</sub> | 5.2<br><sub>6,6,1,2,6</sub> |  | 3.9<br><sub>5,4,1,4,3</sub> |  | 1.0<br><sub>2,1,1,0,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.8 | 10.1 |
| Coby White | 23% | 14.3 | 9.9 | 12.5 · –<br><sub>o 44% · u 56%</sub> | 1.9 |  | 1.8 |  | 1.1 | 1.5<br><sub>o 48% · u 52%</sub> | 0.4 | 0.1 | 1.4 | 13.7 |
| Tidjane Salaun | 88% | 13.4<br><sub>10,16,12,9,12</sub> | 4.6<br><sub>3,5,2,6,5</sub> |  | 3.0<br><sub>3,5,2,2,2</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 0.5<br><sub>1,1,0,2,1</sub> |  | 0.4 | 0.2 | 0.6 | 8.2 |
| Christian Anderson | 96% | 11.4<br><sub>3,11,9,14,8</sub> | 4.1<br><sub>0,3,2,4,2</sub> |  | 1.5<br><sub>1,4,0,3,0</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> |  | 0.4<br><sub>0,1,0,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 6.8 |
| Kylan Boswell | 8% | 8.6 | 3.7 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| PJ Hall | 48% | 7.4<br><sub>-,-,-,2,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 2.3<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.1 | 0.4 | 0.6 | 5.5 |
| Liam McNeeley | 52% | 7.4<br><sub>-,-,-,3,-</sub> | 2.6<br><sub>-,-,-,0,-</sub> |  | 1.5<br><sub>-,-,-,2,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Hannes Steinbach | 43% | 6.5<br><sub>-,-,-,2,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 1.8<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.0 |

</details>


### ATL @ IND
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND), Ivica Zubac (IND), Kingston Flemings (ATL), Mouhamed Gueye (ATL), Jock Landale (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.1–117.4 | ATL 52% | 1.91 / 2.09 | IND +1.5 | 235.5 | IND +5.5 covers 63%; o232.5 57% |
| Expected (weighted by chance each plays) | 119.8–117.7 | ATL 56% | 1.78 / 2.29 | IND +2.5 | 237.5 | IND +5.5 covers 59%; o232.5 59% |
| if Obi Toppin plays | 118.4–118.8 | ATL 49% | 2.03 / 1.97 | IND +0.5 | 237.5 | IND +5.5 covers 66%; o232.5 60% |
| if Jalen Johnson plays | 121.2–116.1 | ATL 64% | 1.56 / 2.79 | IND +5.5 | 237.5 | IND +5.5 covers 51%; o232.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 18.1 | 7.6 | 3.0 | 1.5 | 0.9 | 0.6 | 0.1 | 1.0 | 12.1 | small |
| Keshon Gilbert (ATL) | Doubtful | 20% | 13.8 | 3.8 | 2.0 | 1.8 | 0.2 | 0.6 | 0.3 | 1.1 | 7.7 | small |
| Obi Toppin (IND) | Day-To-Day | 70% | 21.9 | 13.4 | 5.2 | 1.9 | 1.6 | 0.7 | 0.3 | 1.4 | 20.6 | full tables below |
| Jalen Johnson (ATL) | Questionable | 55% | 35.9 | 24.1 | 10.1 | 7.5 | 1.9 | 1.4 | 0.6 | 3.2 | 41.8 | full tables below |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker | 98% | 35.1<br><sub>32,29,32,31,29</sub> | 24.8<br><sub>18,12,23,25,12</sub> |  | 3.8<br><sub>5,2,3,3,2</sub> |  | 4.5<br><sub>4,3,1,1,1</sub> |  | 3.4<br><sub>4,2,5,4,0</sub> |  | 1.3 | 0.5 | 2.8 | 33.0 |
| Onyeka Okongwu | 98% | 33.7<br><sub>26,29,31,33,28</sub> | 17.2<br><sub>8,11,11,29,6</sub> |  | 8.6<br><sub>6,9,4,12,10</sub> |  | 3.6<br><sub>2,1,4,2,1</sub> |  | 1.8<br><sub>0,1,1,4,0</sub> |  | 1.2 | 1.0 | 1.7 | 29.4 |
| Dyson Daniels | 98% | 33.5<br><sub>29,28,28,32,27</sub> | 14.3<br><sub>18,4,7,4,8</sub> |  | 6.8<br><sub>8,0,4,6,4</sub> |  | 6.4<br><sub>3,4,7,5,3</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 2.5 | 0.5 | 1.9 | 27.5 |
| CJ McCollum | 98% | 31.2<br><sub>30,30,20,31,24</sub> | 21.9<br><sub>17,20,13,5,14</sub> |  | 3.3<br><sub>2,1,2,3,2</sub> |  | 4.6<br><sub>1,3,1,8,2</sub> |  | 2.4<br><sub>1,4,1,0,2</sub> |  | 1.1 | 0.6 | 2.5 | 29.9 |
| Luguentz Dort | 98% | 30.1<br><sub>23,21,24,22,29</sub> | 11.3<br><sub>7,11,8,6,11</sub> |  | 4.0<br><sub>2,2,3,3,3</sub> |  | 2.1<br><sub>3,1,3,2,0</sub> |  | 1.8<br><sub>1,0,2,1,1</sub> |  | 1.1 | 0.5 | 1.2 | 17.5 |
| Aaron Wiggins | 96% | 29.9<br><sub>29,27,24,24,23</sub> | 15.9<br><sub>16,12,10,20,10</sub> |  | 4.1<br><sub>5,4,4,7,2</sub> |  | 2.6<br><sub>2,3,3,3,1</sub> |  | 2.1<br><sub>4,2,2,4,2</sub> |  | 1.1 | 0.5 | 1.6 | 22.7 |
| Asa Newell | 52% | 19.8<br><sub>-,1,-,-,19</sub> | 8.6<br><sub>-,0,-,-,13</sub> |  | 4.0<br><sub>-,1,-,-,4</sub> |  | 1.2<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.7 | 0.7 | 0.8 | 13.8 |
| Corey Kispert | 52% | 16.8<br><sub>-,1,-,-,5</sub> | 8.5<br><sub>-,5,-,-,0</sub> |  | 2.4<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,0,-,-,1</sub> |  | 1.1<br><sub>-,1,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 12.3 |
| RayJ Dennis | 16% | 15.0 | 5.6 |  | 2.1 |  | 2.5 |  | 0.6 |  | 0.6 | 0.2 | 0.9 | 10.1 |
| Dorian Finney-Smith | 52% | 15.0<br><sub>-,1,-,-,3</sub> | 3.8<br><sub>-,0,-,-,0</sub> |  | 2.5<br><sub>-,0,-,-,0</sub> |  | 1.1<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.3 |
| Zuby Ejiofor | 47% | 12.4<br><sub>-,1,-,-,-</sub> | 4.0<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.3 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 98% | 34.1<br><sub>29,26,37,34,29</sub> | 27.7<br><sub>23,21,20,26,13</sub> | 22.5 · –<br><sub>o 53% · u 47%</sub> | 7.5<br><sub>3,7,13,11,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>3,6,6,3,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,3,1,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 3.3 | 39.8 |
| Andrew Nembhard | 84% | 33.8<br><sub>32,30,-,35,30</sub> | 18.7<br><sub>16,14,-,18,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>2,1,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 9.2<br><sub>5,3,-,14,9</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,4,-,1,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 3.5 | 30.9 |
| Kelly Oubre Jr. | 98% | 27.9<br><sub>20,20,23,30,22</sub> | 12.1<br><sub>3,14,9,15,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>2,2,3,3,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.5 | 1.6 | 18.4 |
| Jarace Walker | 97% | 27.7<br><sub>17,19,29,22,28</sub> | 13.3<br><sub>2,6,10,7,14</sub> |  | 6.4<br><sub>1,7,8,8,6</sub> |  | 3.3<br><sub>1,1,2,1,4</sub> |  | 1.6<br><sub>0,0,2,1,3</sub> |  | 0.9 | 0.5 | 2.4 | 23.0 |
| Aaron Nesmith | 98% | 27.3<br><sub>20,19,21,27,21</sub> | 14.9<br><sub>9,13,13,18,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,1,0,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,2,1,1,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>1,2,3,3,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.5 | 1.8 | 20.6 |
| Quenton Jackson | 98% | 25.6<br><sub>17,18,27,14,24</sub> | 11.9<br><sub>8,5,4,2,24</sub> |  | 3.2<br><sub>1,1,2,2,4</sub> |  | 4.6<br><sub>3,2,4,6,1</sub> |  | 0.8<br><sub>1,0,0,0,2</sub> |  | 1.1 | 0.2 | 1.8 | 19.7 |
| Jay Huff | 88% | 21.4<br><sub>5,21,23,16,19</sub> | 9.5<br><sub>0,14,6,3,13</sub> |  | 4.1<br><sub>2,2,6,6,1</sub> |  | 1.9<br><sub>0,3,1,2,0</sub> |  | 1.2<br><sub>0,2,0,1,3</sub> |  | 0.5 | 1.5 | 1.2 | 15.4 |
| Kobe Brown | 52% | 19.3<br><sub>1,-,-,-,20</sub> | 7.5<br><sub>0,-,-,-,9</sub> |  | 3.7<br><sub>0,-,-,-,6</sub> |  | 1.7<br><sub>0,-,-,-,4</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.3 | 1.3 | 12.9 |
| Larry Nance Jr. | 88% | 18.9<br><sub>1,22,19,23,18</sub> | 5.7<br><sub>0,6,2,5,6</sub> |  | 3.8<br><sub>0,6,3,5,2</sub> |  | 1.1<br><sub>0,1,1,0,1</sub> |  | 0.6<br><sub>0,1,0,1,2</sub> |  | 0.9 | 0.3 | 0.8 | 10.6 |
| Jalen Slawson | 88% | 16.4<br><sub>16,8,3,12,18</sub> | 5.2<br><sub>4,1,2,2,4</sub> |  | 3.3<br><sub>5,2,1,1,4</sub> |  | 1.6<br><sub>2,0,0,1,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.7 | 0.9 | 10.1 |
| Braden Smith | 67% | 13.7<br><sub>-,-,-,5,12</sub> | 2.5<br><sub>-,-,-,0,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,1,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.3 | 0.8 | 3.9 |

</details>

<details><summary>if Obi Toppin plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker (ATL) | 98% | 35.1<br><sub>32,29,32,31,29</sub> | 24.9<br><sub>18,12,23,25,12</sub> |  | 3.8<br><sub>5,2,3,3,2</sub> |  | 4.5<br><sub>4,3,1,1,1</sub> |  | 3.4<br><sub>4,2,5,4,0</sub> |  | 1.3 | 0.5 | 2.8 | 33.2 |
| Onyeka Okongwu (ATL) | 98% | 33.8<br><sub>26,29,31,33,28</sub> | 17.2<br><sub>8,11,11,29,6</sub> |  | 8.6<br><sub>6,9,4,12,10</sub> |  | 3.5<br><sub>2,1,4,2,1</sub> |  | 1.8<br><sub>0,1,1,4,0</sub> |  | 1.2 | 1.0 | 1.7 | 29.4 |
| Dyson Daniels (ATL) | 98% | 33.6<br><sub>29,28,28,32,27</sub> | 14.4<br><sub>18,4,7,4,8</sub> |  | 6.8<br><sub>8,0,4,6,4</sub> |  | 6.4<br><sub>3,4,7,5,3</sub> |  | 0.6<br><sub>1,0,0,0,0</sub> |  | 2.5 | 0.5 | 2.0 | 27.6 |
| CJ McCollum (ATL) | 98% | 31.2<br><sub>30,30,20,31,24</sub> | 21.9<br><sub>17,20,13,5,14</sub> |  | 3.3<br><sub>2,1,2,3,2</sub> |  | 4.6<br><sub>1,3,1,8,2</sub> |  | 2.4<br><sub>1,4,1,0,2</sub> |  | 1.1 | 0.6 | 2.5 | 29.9 |
| Luguentz Dort (ATL) | 98% | 30.2<br><sub>23,21,24,22,29</sub> | 11.3<br><sub>7,11,8,6,11</sub> |  | 4.0<br><sub>2,2,3,3,3</sub> |  | 2.1<br><sub>3,1,3,2,0</sub> |  | 1.8<br><sub>1,0,2,1,1</sub> |  | 1.1 | 0.5 | 1.2 | 17.5 |
| Aaron Wiggins (ATL) | 96% | 29.9<br><sub>29,27,24,24,23</sub> | 15.9<br><sub>16,12,10,20,10</sub> |  | 4.1<br><sub>5,4,4,7,2</sub> |  | 2.6<br><sub>2,3,3,3,1</sub> |  | 2.1<br><sub>4,2,2,4,2</sub> |  | 1.1 | 0.5 | 1.6 | 22.7 |
| Asa Newell (ATL) | 52% | 20.0<br><sub>-,1,-,-,19</sub> | 8.7<br><sub>-,0,-,-,13</sub> |  | 4.0<br><sub>-,1,-,-,4</sub> |  | 1.2<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.7 | 0.6 | 0.8 | 13.9 |
| Corey Kispert (ATL) | 52% | 16.8<br><sub>-,1,-,-,5</sub> | 8.4<br><sub>-,5,-,-,0</sub> |  | 2.4<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,0,-,-,1</sub> |  | 1.1<br><sub>-,1,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 12.2 |
| RayJ Dennis (ATL) | 16% | 15.0 | 5.6 |  | 2.0 |  | 2.5 |  | 0.6 |  | 0.6 | 0.2 | 0.9 | 10.1 |
| Dorian Finney-Smith (ATL) | 52% | 15.0<br><sub>-,1,-,-,3</sub> | 3.8<br><sub>-,0,-,-,0</sub> |  | 2.5<br><sub>-,0,-,-,0</sub> |  | 1.1<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.3 |
| Zuby Ejiofor (ATL) | 47% | 12.6<br><sub>-,1,-,-,-</sub> | 4.1<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.4 |
| Andrew Nembhard (IND) | 84% | 33.1<br><sub>32,30,-,35,30</sub> | 17.4<br><sub>16,14,-,18,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>2,1,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 8.7<br><sub>5,3,-,14,9</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,4,-,1,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 3.0 | 29.1 |
| Pascal Siakam (IND) | 98% | 32.9<br><sub>29,26,37,34,29</sub> | 25.8<br><sub>23,21,20,26,13</sub> | 22.5 · –<br><sub>o 53% · u 47%</sub> | 7.1<br><sub>3,7,13,11,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.4<br><sub>3,6,6,3,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,3,1,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.9 | 37.3 |
| Kelly Oubre Jr. (IND) | 98% | 26.7<br><sub>20,20,23,30,22</sub> | 10.8<br><sub>3,14,9,15,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>2,2,3,3,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.4 | 1.4 | 16.6 |
| Aaron Nesmith (IND) | 98% | 26.3<br><sub>20,19,21,27,21</sub> | 13.5<br><sub>9,13,13,18,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,1,0,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>1,2,1,1,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>1,2,3,3,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.5 | 1.6 | 18.7 |
| Jarace Walker (IND) | 97% | 26.0<br><sub>17,19,29,22,28</sub> | 11.6<br><sub>2,6,10,7,14</sub> |  | 6.0<br><sub>1,7,8,8,6</sub> |  | 2.8<br><sub>1,1,2,1,4</sub> |  | 1.5<br><sub>0,0,2,1,3</sub> |  | 0.9 | 0.4 | 2.0 | 20.3 |
| Quenton Jackson (IND) | 98% | 23.3<br><sub>17,18,27,14,24</sub> | 10.2<br><sub>8,5,4,2,24</sub> |  | 2.9<br><sub>1,1,2,2,4</sub> |  | 3.8<br><sub>3,2,4,6,1</sub> |  | 0.8<br><sub>1,0,0,0,2</sub> |  | 1.0 | 0.2 | 1.5 | 17.0 |
| Obi Toppin (IND) | 100% | 21.9<br><sub>25,20,23,22,-</sub> | 13.4<br><sub>13,16,14,13,-</sub> |  | 5.2<br><sub>5,6,6,6,-</sub> |  | 1.9<br><sub>1,2,2,0,-</sub> |  | 1.6<br><sub>0,4,2,1,-</sub> |  | 0.7 | 0.3 | 1.4 | 20.6 |
| Jay Huff (IND) | 88% | 19.8<br><sub>5,21,23,16,19</sub> | 8.6<br><sub>0,14,6,3,13</sub> |  | 3.8<br><sub>2,2,6,6,1</sub> |  | 1.6<br><sub>0,3,1,2,0</sub> |  | 1.1<br><sub>0,2,0,1,3</sub> |  | 0.5 | 1.5 | 1.0 | 14.0 |
| Kobe Brown (IND) | 52% | 17.1<br><sub>1,-,-,-,20</sub> | 6.4<br><sub>0,-,-,-,9</sub> |  | 3.3<br><sub>0,-,-,-,6</sub> |  | 1.5<br><sub>0,-,-,-,4</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.5 | 0.2 | 1.1 | 11.2 |
| Larry Nance Jr. (IND) | 88% | 16.2<br><sub>1,22,19,23,18</sub> | 4.9<br><sub>0,6,2,5,6</sub> |  | 3.3<br><sub>0,6,3,5,2</sub> |  | 0.9<br><sub>0,1,1,0,1</sub> |  | 0.5<br><sub>0,1,0,1,2</sub> |  | 0.8 | 0.3 | 0.7 | 9.1 |
| Jalen Slawson (IND) | 88% | 14.6<br><sub>16,8,3,12,18</sub> | 4.5<br><sub>4,1,2,2,4</sub> |  | 3.0<br><sub>5,2,1,1,4</sub> |  | 1.3<br><sub>2,0,0,1,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.7 | 0.8 | 8.7 |
| Braden Smith (IND) | 67% | 12.0<br><sub>-,-,-,5,12</sub> | 2.2<br><sub>-,-,-,0,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 1.1<br><sub>-,-,-,1,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 3.6 |

</details>

<details><summary>if Jalen Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 100% | 35.9<br><sub>38,36,36,34,28</sub> | 24.1<br><sub>26,21,12,17,13</sub> |  | 10.1<br><sub>9,9,9,8,7</sub> |  | 7.5<br><sub>16,3,11,7,4</sub> |  | 1.9<br><sub>2,1,2,2,1</sub> |  | 1.4 | 0.6 | 3.2 | 41.8 |
| Nickeil Alexander-Walker (ATL) | 98% | 34.1<br><sub>32,29,32,31,29</sub> | 21.4<br><sub>18,12,23,25,12</sub> |  | 3.6<br><sub>5,2,3,3,2</sub> |  | 3.5<br><sub>4,3,1,1,1</sub> |  | 3.1<br><sub>4,2,5,4,0</sub> |  | 1.3 | 0.5 | 2.4 | 28.5 |
| Dyson Daniels (ATL) | 98% | 32.9<br><sub>29,28,28,32,27</sub> | 12.4<br><sub>18,4,7,4,8</sub> |  | 6.5<br><sub>8,0,4,6,4</sub> |  | 5.5<br><sub>3,4,7,5,3</sub> |  | 0.5<br><sub>1,0,0,0,0</sub> |  | 2.5 | 0.5 | 1.7 | 24.4 |
| Onyeka Okongwu (ATL) | 98% | 32.6<br><sub>26,29,31,33,28</sub> | 14.9<br><sub>8,11,11,29,6</sub> |  | 8.2<br><sub>6,9,4,12,10</sub> |  | 2.9<br><sub>2,1,4,2,1</sub> |  | 1.6<br><sub>0,1,1,4,0</sub> |  | 1.1 | 1.0 | 1.4 | 26.1 |
| CJ McCollum (ATL) | 98% | 30.3<br><sub>30,30,20,31,24</sub> | 19.2<br><sub>17,20,13,5,14</sub> |  | 3.2<br><sub>2,1,2,3,2</sub> |  | 3.7<br><sub>1,3,1,8,2</sub> |  | 2.2<br><sub>1,4,1,0,2</sub> |  | 1.1 | 0.6 | 2.2 | 26.0 |
| Luguentz Dort (ATL) | 98% | 28.2<br><sub>23,21,24,22,29</sub> | 9.3<br><sub>7,11,8,6,11</sub> |  | 3.6<br><sub>2,2,3,3,3</sub> |  | 1.7<br><sub>3,1,3,2,0</sub> |  | 1.4<br><sub>1,0,2,1,1</sub> |  | 1.1 | 0.4 | 0.9 | 14.6 |
| Aaron Wiggins (ATL) | 96% | 27.3<br><sub>29,27,24,24,23</sub> | 13.1<br><sub>16,12,10,20,10</sub> |  | 3.6<br><sub>5,4,4,7,2</sub> |  | 2.1<br><sub>2,3,3,3,1</sub> |  | 1.9<br><sub>4,2,2,4,2</sub> |  | 1.0 | 0.5 | 1.2 | 18.8 |
| Asa Newell (ATL) | 52% | 14.3<br><sub>-,1,-,-,19</sub> | 5.9<br><sub>-,0,-,-,13</sub> |  | 2.9<br><sub>-,1,-,-,4</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.5 | 0.5 | 0.6 | 9.6 |
| RayJ Dennis (ATL) | 16% | 12.0 | 4.2 |  | 1.6 |  | 1.9 |  | 0.5 |  | 0.4 | 0.2 | 0.7 | 7.7 |
| Corey Kispert (ATL) | 52% | 11.2<br><sub>-,1,-,-,5</sub> | 5.3<br><sub>-,5,-,-,0</sub> |  | 1.6<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,1</sub> |  | 0.6<br><sub>-,1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 7.8 |
| Dorian Finney-Smith (ATL) | 52% | 8.6<br><sub>-,1,-,-,3</sub> | 2.3<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,0,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Zuby Ejiofor (ATL) | 47% | 7.2<br><sub>-,1,-,-,-</sub> | 2.6<br><sub>-,0,-,-,-</sub> |  | 1.4<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Pascal Siakam (IND) | 98% | 34.1<br><sub>29,26,37,34,29</sub> | 27.7<br><sub>23,21,20,26,13</sub> | 22.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>3,7,13,11,5</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 4.5<br><sub>3,6,6,3,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.6<br><sub>3,3,1,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 3.3 | 39.7 |
| Andrew Nembhard (IND) | 84% | 33.8<br><sub>32,30,-,35,30</sub> | 18.6<br><sub>16,14,-,18,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>2,1,-,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 9.2<br><sub>5,3,-,14,9</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,4,-,1,5</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 3.5 | 30.9 |
| Kelly Oubre Jr. (IND) | 98% | 27.9<br><sub>20,20,23,30,22</sub> | 12.0<br><sub>3,14,9,15,10</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>2,2,3,3,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>2,2,1,1,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.0<br><sub>1,1,1,1,1</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.4 | 1.6 | 18.4 |
| Jarace Walker (IND) | 97% | 27.6<br><sub>17,19,29,22,28</sub> | 13.2<br><sub>2,6,10,7,14</sub> |  | 6.3<br><sub>1,7,8,8,6</sub> |  | 3.3<br><sub>1,1,2,1,4</sub> |  | 1.6<br><sub>0,0,2,1,3</sub> |  | 0.9 | 0.5 | 2.5 | 22.7 |
| Aaron Nesmith (IND) | 98% | 27.4<br><sub>20,19,21,27,21</sub> | 14.8<br><sub>9,13,13,18,9</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,1,0,2,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,2,1,1,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 2.0<br><sub>1,2,3,3,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.7 | 0.5 | 1.8 | 20.5 |
| Quenton Jackson (IND) | 98% | 25.5<br><sub>17,18,27,14,24</sub> | 11.8<br><sub>8,5,4,2,24</sub> |  | 3.2<br><sub>1,1,2,2,4</sub> |  | 4.6<br><sub>3,2,4,6,1</sub> |  | 0.9<br><sub>1,0,0,0,2</sub> |  | 1.1 | 0.2 | 1.8 | 19.6 |
| Jay Huff (IND) | 88% | 21.3<br><sub>5,21,23,16,19</sub> | 9.4<br><sub>0,14,6,3,13</sub> |  | 4.1<br><sub>2,2,6,6,1</sub> |  | 1.8<br><sub>0,3,1,2,0</sub> |  | 1.2<br><sub>0,2,0,1,3</sub> |  | 0.5 | 1.5 | 1.2 | 15.3 |
| Kobe Brown (IND) | 52% | 19.3<br><sub>1,-,-,-,20</sub> | 7.5<br><sub>0,-,-,-,9</sub> |  | 3.8<br><sub>0,-,-,-,6</sub> |  | 1.7<br><sub>0,-,-,-,4</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.6 | 0.3 | 1.3 | 13.0 |
| Larry Nance Jr. (IND) | 88% | 18.8<br><sub>1,22,19,23,18</sub> | 5.6<br><sub>0,6,2,5,6</sub> |  | 3.8<br><sub>0,6,3,5,2</sub> |  | 1.1<br><sub>0,1,1,0,1</sub> |  | 0.6<br><sub>0,1,0,1,2</sub> |  | 0.9 | 0.3 | 0.8 | 10.5 |
| Jalen Slawson (IND) | 88% | 16.5<br><sub>16,8,3,12,18</sub> | 5.2<br><sub>4,1,2,2,4</sub> |  | 3.3<br><sub>5,2,1,1,4</sub> |  | 1.6<br><sub>2,0,0,1,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.7 | 0.9 | 10.1 |
| Braden Smith (IND) | 67% | 13.8<br><sub>-,-,-,5,12</sub> | 2.5<br><sub>-,-,-,0,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 1.2<br><sub>-,-,-,1,1</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.3 | 0.8 | 4.0 |

</details>


### BKN @ NYK
Out: Egor Demin (BKN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Karl-Anthony Towns PA under 25.5 | BKN @ NYK | draftkings | 1.93 | 1.93 | 1.59 | 62.8% | 48.3% | 51.9% | +0.5% | +21.5% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 103.8–117.5 | BKN 16% | 6.10 / 1.20 | NYK -13.5 | 221.5 | NYK -14.5 covers 48%; o220.5 52% |
| Expected (weighted by chance each plays) | 104.1–116.9 | BKN 18% | 5.51 / 1.22 | NYK -12.5 | 220.5 | NYK -14.5 covers 45%; o220.5 50% |
| if Mikel Brown Jr. plays | 104.5–116.1 | BKN 21% | 4.86 / 1.26 | NYK -11.5 | 220.5 | NYK -14.5 covers 42%; o220.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Mikel Brown Jr. (BKN) | Day-To-Day | 70% | 21.3 | 9.4 | 2.4 | 3.1 | 1.1 | 0.7 | 0.2 | 1.5 | 14.9 | full tables below |
| Jose Alvarado (NYK) | Questionable | 55% | 11.2 | 4.3 | 1.5 | 1.9 | 0.5 | 0.8 | 0.1 | 0.8 | 7.7 | small |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 98% | 33.8<br><sub>38,35,24,44,25</sub> | 18.7<br><sub>33,23,10,24,15</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 7.1<br><sub>8,6,7,9,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>7,5,7,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>3,2,0,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.2 | 3.3 | 30.5 |
| Michael Porter Jr. | 98% | 32.2<br><sub>34,33,21,40,26</sub> | 19.6<br><sub>26,28,10,27,13</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 6.2<br><sub>7,9,0,12,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.8<br><sub>5,4,0,6,2</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 2.0 | 27.8 |
| Keon Ellis | 93% | 24.0<br><sub>34,22,23,25,21</sub> | 6.9<br><sub>7,6,9,2,6</sub> |  | 2.3<br><sub>2,2,1,3,2</sub> |  | 1.7<br><sub>4,1,3,4,1</sub> |  | 1.0<br><sub>1,2,1,0,2</sub> |  | 1.2 | 0.7 | 0.8 | 10.9 |
| Noah Clowney | 98% | 22.7<br><sub>22,20,20,24,22</sub> | 7.9<br><sub>9,4,9,3,3</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,4,5,4,8</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>1,0,1,1,1</sub> |  | 1.1<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.7 | 0.6 | 0.9 | 12.9 |
| Nolan Traore | 98% | 22.4<br><sub>16,5,25,24,26</sub> | 9.4<br><sub>3,3,17,15,9</sub> | 11.5 · –<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 3.4<br><sub>0,0,5,3,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.0<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.9 | 0.5 | 2.2 | 14.7 |
| Day'Ron Sharpe | 98% | 21.9<br><sub>30,23,16,17,24</sub> | 8.2<br><sub>8,7,11,4,3</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>8,8,4,6,7</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>3,1,1,0,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.3<br><sub>0,1,1,0,0</sub> |  | 1.0 | 0.8 | 1.6 | 17.4 |
| Chaney Johnson | 91% | 20.4<br><sub>5,27,21,29,19</sub> | 7.2<br><sub>0,10,4,15,6</sub> |  | 2.9<br><sub>1,5,5,3,2</sub> |  | 1.1<br><sub>0,3,0,2,0</sub> |  | 0.9<br><sub>0,2,0,3,0</sub> |  | 0.7 | 0.3 | 1.0 | 11.2 |
| Moritz Wagner | 88% | 18.9<br><sub>16,14,15,22,23</sub> | 9.5<br><sub>7,6,13,15,16</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>0,4,3,4,8</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.4<br><sub>1,1,1,3,1</sub> |  | 0.8<br><sub>1,1,2,2,1</sub> |  | 0.6 | 0.3 | 1.2 | 14.9 |
| Terance Mann | 52% | 14.5<br><sub>-,-,-,-,12</sub> | 4.5<br><sub>-,-,-,-,2</sub> |  | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.6 | 7.6 |
| Danny Wolf | 58% | 13.8<br><sub>-,-,15,-,12</sub> | 5.5<br><sub>-,-,6,-,9</sub> |  | 3.1<br><sub>-,-,2,-,6</sub> |  | 1.3<br><sub>-,-,1,-,2</sub> |  | 0.6<br><sub>-,-,2,-,3</sub> |  | 0.3 | 0.4 | 0.9 | 9.9 |
| Ben Saraf | 58% | 13.1<br><sub>-,-,4,-,-</sub> | 5.0<br><sub>-,-,2,-,-</sub> |  | 1.4<br><sub>-,-,1,-,-</sub> |  | 1.9<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.1 | 1.3 | 8.2 |
| Drake Powell | 66% | 11.6<br><sub>-,-,12,-,6</sub> | 3.9<br><sub>-,-,0,-,0</sub> |  | 1.0<br><sub>-,-,2,-,0</sub> |  | 0.7<br><sub>-,-,3,-,2</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Josh Minott | 64% | 11.4<br><sub>-,9,21,-,3</sub> | 5.6<br><sub>-,4,15,-,2</sub> |  | 2.0<br><sub>-,2,8,-,0</sub> |  | 0.7<br><sub>-,0,2,-,0</sub> |  | 0.7<br><sub>-,0,3,-,0</sub> |  | 0.5 | 0.4 | 0.6 | 8.2 |
| Grant Nelson | 23% | 9.3 | 3.3 |  | 2.0 |  | 0.6 |  | 0.0 |  | 0.3 | 0.9 | 0.4 | 5.9 |
| Joshua Jefferson | 80% | 7.0<br><sub>-,-,4,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 1.0 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 34.9<br><sub>37,32,36,35,35</sub> | 26.8<br><sub>19,28,23,38,24</sub> | 24.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,3,1,1,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.7<br><sub>4,4,7,7,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,1,0,6,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 2.8 | 36.9 |
| OG Anunoby | 98% | 33.5<br><sub>34,35,36,31,34</sub> | 18.2<br><sub>20,22,13,23,9</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>10,3,7,6,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>8,2,2,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,3,1,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.9 | 1.6 | 26.2 |
| Josh Hart | 98% | 32.0<br><sub>36,35,27,36,31</sub> | 11.0<br><sub>10,13,6,2,7</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 7.9<br><sub>12,8,4,8,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,2,4,3,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.6 | 0.3 | 1.8 | 23.3 |
| Karl-Anthony Towns | 98% | 31.6<br><sub>37,33,33,28,35</sub> | 19.9<br><sub>22,22,27,19,22</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 12.2<br><sub>10,14,20,13,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>3,4,3,5,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>2,0,1,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 1.0 | 2.8 | 36.1 |
| Mikal Bridges | 98% | 28.8<br><sub>22,35,32,13,30</sub> | 11.2<br><sub>0,6,12,3,12</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,5,3,0,5</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.8<br><sub>4,1,4,0,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>0,0,4,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 1.0 | 17.1 |
| Landry Shamet | 98% | 22.9<br><sub>21,22,28,32,16</sub> | 8.4<br><sub>8,6,13,14,0</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>2,2,2,1,0</sub> |  | 1.6<br><sub>0,1,3,5,0</sub> |  | 1.5<br><sub>2,2,3,4,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.2 | 0.8 | 11.8 |
| Miles McBride | 98% | 19.7<br><sub>30,13,17,14,24</sub> | 7.8<br><sub>20,1,5,3,10</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,1,5,3</sub> |  | 1.7<br><sub>1,1,1,0,1</sub> |  | 1.3<br><sub>6,0,1,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 0.7 | 11.4 |
| Andre Drummond | 98% | 14.1<br><sub>7,7,14,15,12</sub> | 5.4<br><sub>2,4,10,4,3</sub> |  | 5.9<br><sub>2,3,8,11,6</sub> |  | 1.2<br><sub>0,2,1,1,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.6 | 0.8 | 12.6 |
| Tyler Kolek | 71% | 13.9<br><sub>-,15,11,18,13</sub> | 4.8<br><sub>-,0,2,9,2</sub> |  | 1.7<br><sub>-,3,1,2,1</sub> |  | 4.2<br><sub>-,9,3,9,4</sub> |  | 0.6<br><sub>-,0,0,3,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.7 |
| Jordan Clarkson | 83% | 11.7<br><sub>3,5,-,17,9</sub> | 5.9<br><sub>0,0,-,18,4</sub> |  | 1.7<br><sub>1,1,-,3,3</sub> |  | 1.0<br><sub>0,0,-,1,0</sub> |  | 0.4<br><sub>0,0,-,2,0</sub> |  | 0.4 | 0.1 | 0.8 | 8.7 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Mohamed Diawara | 36% | 7.9<br><sub>-,-,1,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.0 |
| Dalton Knecht | 35% | 7.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.4 |
| Jaden Akins | 38% | 7.5<br><sub>-,-,2,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.1 |
| James Wiseman | 52% | 6.8<br><sub>2,7,1,-,-</sub> | 2.4<br><sub>0,0,0,-,-</sub> |  | 2.0<br><sub>0,2,1,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 4.8 |
| Pacome Dadiet | 36% | 6.5<br><sub>-,-,1,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.6 |

</details>

<details><summary>if Mikel Brown Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle (BKN) | 98% | 32.8<br><sub>38,35,24,44,25</sub> | 17.2<br><sub>33,23,10,24,15</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>8,6,7,9,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>7,5,7,4,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>3,2,0,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.2 | 2.9 | 28.1 |
| Michael Porter Jr. (BKN) | 98% | 31.0<br><sub>34,33,21,40,26</sub> | 18.3<br><sub>26,28,10,27,13</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>7,9,0,12,7</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.5<br><sub>5,4,0,6,2</sub> | 3.5<br><sub>o 38% · u 62%</sub> | 0.9 | 0.3 | 1.8 | 26.0 |
| Mikel Brown Jr. (BKN) | 100% | 21.3<br><sub>20,20,-,28,23</sub> | 9.4<br><sub>6,8,-,17,10</sub> | 11.5 · – | 2.4<br><sub>3,2,-,5,0</sub> | 2.5 | 3.1<br><sub>3,5,-,5,4</sub> | 3.5 | 1.1<br><sub>1,2,-,4,0</sub> | 1.5 | 0.7 | 0.2 | 1.5 | 14.9 |
| Keon Ellis (BKN) | 93% | 20.8<br><sub>34,22,23,25,21</sub> | 6.0<br><sub>7,6,9,2,6</sub> |  | 2.0<br><sub>2,2,1,3,2</sub> |  | 1.4<br><sub>4,1,3,4,1</sub> |  | 0.8<br><sub>1,2,1,0,2</sub> |  | 1.1 | 0.6 | 0.7 | 9.3 |
| Day'Ron Sharpe (BKN) | 98% | 20.1<br><sub>30,23,16,17,24</sub> | 7.7<br><sub>8,7,11,4,3</sub> | 8.5 · –<br><sub>o 46% · u 54%</sub> | 6.1<br><sub>8,8,4,6,7</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>3,1,1,0,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.3<br><sub>0,1,1,0,0</sub> |  | 0.9 | 0.7 | 1.5 | 15.7 |
| Nolan Traore (BKN) | 98% | 20.0<br><sub>16,5,25,24,26</sub> | 8.1<br><sub>3,3,17,15,9</sub> | 11.5 · –<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>2,2,2,1,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 2.9<br><sub>0,0,5,3,2</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 0.9<br><sub>0,0,2,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.4 | 2.0 | 12.8 |
| Noah Clowney (BKN) | 98% | 19.9<br><sub>22,20,20,24,22</sub> | 6.8<br><sub>9,4,9,3,3</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,4,5,4,8</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.9<br><sub>1,0,1,1,1</sub> |  | 1.0<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 0.6 | 0.5 | 0.8 | 11.0 |
| Chaney Johnson (BKN) | 91% | 17.9<br><sub>5,27,21,29,19</sub> | 6.4<br><sub>0,10,4,15,6</sub> |  | 2.6<br><sub>1,5,5,3,2</sub> |  | 0.9<br><sub>0,3,0,2,0</sub> |  | 0.8<br><sub>0,2,0,3,0</sub> |  | 0.6 | 0.3 | 0.8 | 9.9 |
| Moritz Wagner (BKN) | 88% | 17.7<br><sub>16,14,15,22,23</sub> | 9.5<br><sub>7,6,13,15,16</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>0,4,3,4,8</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.2<br><sub>1,1,1,3,1</sub> |  | 0.8<br><sub>1,1,2,2,1</sub> |  | 0.6 | 0.3 | 1.1 | 14.6 |
| Terance Mann (BKN) | 52% | 13.1<br><sub>-,-,-,-,12</sub> | 4.0<br><sub>-,-,-,-,2</sub> |  | 1.6<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.9 |
| Danny Wolf (BKN) | 58% | 12.4<br><sub>-,-,15,-,12</sub> | 5.1<br><sub>-,-,6,-,9</sub> |  | 2.7<br><sub>-,-,2,-,6</sub> |  | 1.1<br><sub>-,-,1,-,2</sub> |  | 0.5<br><sub>-,-,2,-,3</sub> |  | 0.3 | 0.4 | 0.8 | 8.9 |
| Josh Minott (BKN) | 64% | 9.5<br><sub>-,9,21,-,3</sub> | 4.6<br><sub>-,4,15,-,2</sub> |  | 1.6<br><sub>-,2,8,-,0</sub> |  | 0.5<br><sub>-,0,2,-,0</sub> |  | 0.5<br><sub>-,0,3,-,0</sub> |  | 0.5 | 0.4 | 0.5 | 6.7 |
| Drake Powell (BKN) | 66% | 9.3<br><sub>-,-,12,-,6</sub> | 3.0<br><sub>-,-,0,-,0</sub> |  | 0.8<br><sub>-,-,2,-,0</sub> |  | 0.6<br><sub>-,-,3,-,2</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Ben Saraf (BKN) | 58% | 8.8<br><sub>-,-,4,-,-</sub> | 3.2<br><sub>-,-,2,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.9 | 5.3 |
| Grant Nelson (BKN) | 23% | 7.4 | 2.7 |  | 1.6 |  | 0.5 |  | 0.0 |  | 0.2 | 0.7 | 0.4 | 4.8 |
| Joshua Jefferson (BKN) | 80% | 6.0<br><sub>-,-,4,-,-</sub> | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.1 | 0.2 | 0.9 |
| Jalen Brunson (NYK) | 98% | 34.9<br><sub>37,32,36,35,35</sub> | 26.6<br><sub>19,28,23,38,24</sub> | 24.5 · –<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>2,3,1,1,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 6.7<br><sub>4,4,7,7,6</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>2,1,0,6,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 2.8 | 36.7 |
| OG Anunoby (NYK) | 98% | 33.4<br><sub>34,35,36,31,34</sub> | 18.1<br><sub>20,22,13,23,9</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>10,3,7,6,4</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>8,2,2,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,3,1,2,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.5 | 0.9 | 1.6 | 26.1 |
| Josh Hart (NYK) | 98% | 32.0<br><sub>36,35,27,36,31</sub> | 10.9<br><sub>10,13,6,2,7</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 7.8<br><sub>12,8,4,8,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.5<br><sub>5,2,4,3,3</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.4<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.6 | 0.3 | 1.8 | 23.2 |
| Karl-Anthony Towns (NYK) | 98% | 31.5<br><sub>37,33,33,28,35</sub> | 19.7<br><sub>22,22,27,19,22</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 12.2<br><sub>10,14,20,13,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>3,4,3,5,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>2,0,1,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 1.0 | 2.8 | 36.0 |
| Mikal Bridges (NYK) | 98% | 28.7<br><sub>22,35,32,13,30</sub> | 11.1<br><sub>0,6,12,3,12</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>1,5,3,0,5</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 2.8<br><sub>4,1,4,0,2</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>0,0,4,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 1.0 | 17.0 |
| Landry Shamet (NYK) | 98% | 22.9<br><sub>21,22,28,32,16</sub> | 8.4<br><sub>8,6,13,14,0</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>2,2,2,1,0</sub> |  | 1.6<br><sub>0,1,3,5,0</sub> |  | 1.5<br><sub>2,2,3,4,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.2 | 0.8 | 11.8 |
| Miles McBride (NYK) | 98% | 19.7<br><sub>30,13,17,14,24</sub> | 7.7<br><sub>20,1,5,3,10</sub> | 6.5 · –<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,1,5,3</sub> |  | 1.7<br><sub>1,1,1,0,1</sub> |  | 1.3<br><sub>6,0,1,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 0.7 | 11.4 |
| Andre Drummond (NYK) | 98% | 14.0<br><sub>7,7,14,15,12</sub> | 5.3<br><sub>2,4,10,4,3</sub> |  | 5.9<br><sub>2,3,8,11,6</sub> |  | 1.2<br><sub>0,2,1,1,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.5 | 0.8 | 12.4 |
| Tyler Kolek (NYK) | 71% | 13.9<br><sub>-,15,11,18,13</sub> | 4.7<br><sub>-,0,2,9,2</sub> |  | 1.7<br><sub>-,3,1,2,1</sub> |  | 4.2<br><sub>-,9,3,9,4</sub> |  | 0.6<br><sub>-,0,0,3,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.6 |
| Jordan Clarkson (NYK) | 83% | 11.6<br><sub>3,5,-,17,9</sub> | 5.8<br><sub>0,0,-,18,4</sub> |  | 1.8<br><sub>1,1,-,3,3</sub> |  | 1.0<br><sub>0,0,-,1,0</sub> |  | 0.4<br><sub>0,0,-,2,0</sub> |  | 0.4 | 0.1 | 0.8 | 8.6 |
| Tyler Nickel (NYK) | 38% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Mohamed Diawara (NYK) | 36% | 7.9<br><sub>-,-,1,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Dalton Knecht (NYK) | 35% | 7.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| Jaden Akins (NYK) | 38% | 7.4<br><sub>-,-,2,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.1 |
| James Wiseman (NYK) | 52% | 6.8<br><sub>2,7,1,-,-</sub> | 2.5<br><sub>0,0,0,-,-</sub> |  | 2.0<br><sub>0,2,1,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 4.8 |
| Pacome Dadiet (NYK) | 36% | 6.6<br><sub>-,-,1,-,-</sub> | 2.7<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |

</details>


### WAS @ ORL
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.2–117.3 | WAS 33% | 3.01 / 1.50 | ORL -6.5 | 228.5 | ORL -1.5 covers 64%; o223.5 60% |
| Expected (weighted by chance each plays) | 111.0–117.0 | WAS 34% | 2.96 / 1.51 | ORL -6.5 | 227.5 | ORL -1.5 covers 64%; o223.5 59% |
| if Alex Sarr plays | 110.7–116.8 | WAS 33% | 3.03 / 1.49 | ORL -6.5 | 227.5 | ORL -1.5 covers 64%; o223.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Gill (WAS) | Questionable | 55% | 12.0 | 4.1 | 2.2 | 0.8 | 0.2 | 0.4 | 0.3 | 0.5 | 7.0 | small |
| Alex Sarr (WAS) | Questionable | 55% | 25.8 | 10.8 | 6.2 | 2.2 | 0.9 | 0.8 | 1.9 | 1.4 | 19.2 | full tables below |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.5<br><sub>37,34,38,34,38</sub> | 21.4<br><sub>22,25,22,14,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>1,4,6,5,7</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 9.7<br><sub>12,9,10,8,9</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>4,4,1,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 3.9 | 34.5 |
| Anthony Davis | 98% | 34.4<br><sub>32,31,36,34,34</sub> | 21.6<br><sub>9,19,29,18,25</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 12.2<br><sub>9,6,10,5,13</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>0,4,0,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.7<br><sub>0,0,3,2,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.1 | 1.9 | 2.4 | 36.6 |
| Kyshawn George | 98% | 32.5<br><sub>26,36,29,38,32</sub> | 16.4<br><sub>11,22,20,8,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>3,9,4,2,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.3<br><sub>3,5,2,11,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,0,2,0,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.1 | 2.5 | 26.2 |
| AJ Dybantsa | 88% | 30.6<br><sub>-,-,-,27,30</sub> | 15.5<br><sub>-,-,-,19,17</sub> | 16.5 · –<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>-,-,-,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>-,-,-,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.8 | 22.9 |
| Bilal Coulibaly | 98% | 27.8<br><sub>26,25,29,27,22</sub> | 10.1<br><sub>11,7,3,17,1</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>6,4,5,2,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>0,0,1,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.2 | 1.0 | 1.4 | 16.4 |
| Bub Carrington | 98% | 24.6<br><sub>11,21,28,20,20</sub> | 8.7<br><sub>3,9,6,3,9</sub> |  | 3.0<br><sub>1,2,0,1,4</sub> |  | 3.1<br><sub>0,1,3,3,2</sub> |  | 1.3<br><sub>1,3,2,0,3</sub> |  | 0.6 | 0.2 | 1.7 | 14.9 |
| Tre Johnson | 72% | 20.1<br><sub>26,23,23,-,13</sub> | 7.3<br><sub>20,13,7,-,4</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>2,2,3,-,2</sub> |  | 1.1<br><sub>0,2,2,-,0</sub> |  | 0.9<br><sub>4,2,1,-,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.5 | 0.3 | 0.9 | 10.9 |
| Deandre Ayton | 98% | 17.9<br><sub>14,16,12,12,17</sub> | 6.0<br><sub>4,6,0,10,3</sub> |  | 5.5<br><sub>6,5,4,3,3</sub> |  | 0.8<br><sub>1,0,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.9 | 12.3 |
| Khris Middleton | 88% | 16.4<br><sub>16,-,13,23,5</sub> | 5.2<br><sub>6,-,0,4,0</sub> |  | 2.8<br><sub>2,-,1,3,0</sub> |  | 1.2<br><sub>0,-,0,2,0</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.1 | 1.1 | 9.2 |
| Will Riley | 67% | 10.2<br><sub>1,5,4,-,1</sub> | 4.4<br><sub>0,2,2,-,0</sub> |  | 1.4<br><sub>0,0,0,-,0</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.6 |
| Reece Beekman | 38% | 8.8<br><sub>1,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 1.3 |
| Felix Okpara | 38% | 8.3<br><sub>1,-,-,-,-</sub> | 3.0<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 3.9 |
| Tre Mann | 52% | 7.7<br><sub>1,-,-,-,1</sub> | 2.8<br><sub>0,-,-,-,0</sub> |  | 1.1<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |

</details>

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane | 98% | 34.6<br><sub>33,27,35,34,39</sub> | 23.7<br><sub>18,5,22,13,28</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>5,2,6,5,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.3<br><sub>2,0,2,4,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>3,1,4,2,6</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.5 | 2.5 | 32.5 |
| Franz Wagner | 98% | 34.4<br><sub>29,33,37,34,39</sub> | 25.6<br><sub>22,18,23,15,26</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>6,6,13,4,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>5,5,9,5,11</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.4 | 3.1 | 38.2 |
| Wendell Carter Jr. | 98% | 33.0<br><sub>31,29,33,26,39</sub> | 15.1<br><sub>22,20,9,3,20</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 8.7<br><sub>7,9,10,10,7</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>0,1,2,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0<br><sub>1,3,0,0,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.9 | 1.8 | 26.2 |
| Anthony Black | 98% | 29.9<br><sub>-,-,26,22,31</sub> | 14.8<br><sub>-,-,18,8,17</sub> | 15.5 · –<br><sub>o 45% · u 55%</sub> | 4.1<br><sub>-,-,3,2,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.4<br><sub>-,-,5,1,10</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>-,-,5,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.7 | 0.7 | 2.0 | 23.2 |
| Tristan da Silva | 98% | 27.5<br><sub>28,29,27,31,23</sub> | 12.1<br><sub>14,5,19,20,8</sub> |  | 3.8<br><sub>2,3,2,3,0</sub> |  | 1.9<br><sub>3,1,2,1,0</sub> |  | 1.6<br><sub>4,1,5,4,2</sub> |  | 1.0 | 0.4 | 1.1 | 17.8 |
| Jase Richardson | 88% | 24.9<br><sub>14,14,17,14,33</sub> | 9.3<br><sub>2,6,6,10,4</sub> |  | 3.0<br><sub>2,1,1,1,6</sub> |  | 2.7<br><sub>3,3,0,1,2</sub> |  | 0.9<br><sub>0,1,2,2,0</sub> |  | 1.0 | 0.3 | 1.1 | 15.1 |
| Jamal Cain | 98% | 17.9<br><sub>14,11,15,16,15</sub> | 7.3<br><sub>0,0,5,9,13</sub> |  | 3.1<br><sub>0,1,5,1,0</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 0.7<br><sub>0,0,1,0,3</sub> |  | 0.6 | 0.3 | 0.8 | 11.3 |
| Jevon Carter | 52% | 15.8<br><sub>-,13,-,22,-</sub> | 5.4<br><sub>-,0,-,6,-</sub> |  | 1.6<br><sub>-,1,-,0,-</sub> |  | 1.7<br><sub>-,1,-,3,-</sub> |  | 0.8<br><sub>-,0,-,2,-</sub> |  | 0.8 | 0.2 | 0.6 | 8.7 |
| Goga Bitadze | 80% | 13.0<br><sub>12,12,-,11,6</sub> | 5.2<br><sub>6,4,-,6,2</sub> |  | 4.6<br><sub>6,3,-,0,4</sub> |  | 1.1<br><sub>1,0,-,1,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.0 | 0.8 | 10.9 |
| Nikola Vucevic | 96% | 12.4<br><sub>5,4,15,16,6</sub> | 5.2<br><sub>0,0,5,5,3</sub> |  | 3.7<br><sub>1,2,3,4,1</sub> |  | 1.5<br><sub>1,0,3,2,0</sub> |  | 0.5<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.4 | 0.6 | 10.5 |
| Alex Morales | 64% | 11.7<br><sub>-,4,-,7,9</sub> | 3.1<br><sub>-,0,-,2,0</sub> |  | 1.8<br><sub>-,1,-,2,1</sub> |  | 1.2<br><sub>-,0,-,1,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.1 |
| Colin Castleton | 52% | 7.7<br><sub>-,4,-,7,-</sub> | 2.6<br><sub>-,7,-,2,-</sub> |  | 2.4<br><sub>-,2,-,2,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.6 |

</details>

<details><summary>if Alex Sarr plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane (ORL) | 98% | 34.6<br><sub>33,27,35,34,39</sub> | 23.6<br><sub>18,5,22,13,28</sub> | 20.5 · –<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>5,2,6,5,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.2<br><sub>2,0,2,4,6</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.8<br><sub>3,1,4,2,6</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.5 | 2.5 | 32.5 |
| Franz Wagner (ORL) | 98% | 34.4<br><sub>29,33,37,34,39</sub> | 25.6<br><sub>22,18,23,15,26</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>6,6,13,4,5</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>5,5,9,5,11</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5 | 0.4 | 3.0 | 38.2 |
| Wendell Carter Jr. (ORL) | 98% | 33.1<br><sub>31,29,33,26,39</sub> | 15.1<br><sub>22,20,9,3,20</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 8.8<br><sub>7,9,10,10,7</sub> | 8.5<br><sub>o 52% · u 48%</sub> | 2.4<br><sub>0,1,2,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.0<br><sub>1,3,0,0,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.1 | 1.0 | 1.8 | 26.2 |
| Anthony Black (ORL) | 98% | 30.0<br><sub>-,-,26,22,31</sub> | 14.8<br><sub>-,-,18,8,17</sub> | 15.5 · –<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>-,-,3,2,6</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 4.4<br><sub>-,-,5,1,10</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>-,-,5,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.8 | 0.7 | 2.0 | 23.3 |
| Tristan da Silva (ORL) | 98% | 27.6<br><sub>28,29,27,31,23</sub> | 12.2<br><sub>14,5,19,20,8</sub> |  | 3.8<br><sub>2,3,2,3,0</sub> |  | 2.0<br><sub>3,1,2,1,0</sub> |  | 1.6<br><sub>4,1,5,4,2</sub> |  | 1.0 | 0.4 | 1.1 | 18.0 |
| Jase Richardson (ORL) | 88% | 24.8<br><sub>14,14,17,14,33</sub> | 9.3<br><sub>2,6,6,10,4</sub> |  | 3.0<br><sub>2,1,1,1,6</sub> |  | 2.7<br><sub>3,3,0,1,2</sub> |  | 0.9<br><sub>0,1,2,2,0</sub> |  | 1.0 | 0.2 | 1.1 | 15.0 |
| Jamal Cain (ORL) | 98% | 17.8<br><sub>14,11,15,16,15</sub> | 7.2<br><sub>0,0,5,9,13</sub> |  | 3.1<br><sub>0,1,5,1,0</sub> |  | 0.9<br><sub>0,0,0,0,0</sub> |  | 0.7<br><sub>0,0,1,0,3</sub> |  | 0.6 | 0.3 | 0.8 | 11.2 |
| Jevon Carter (ORL) | 52% | 15.7<br><sub>-,13,-,22,-</sub> | 5.3<br><sub>-,0,-,6,-</sub> |  | 1.6<br><sub>-,1,-,0,-</sub> |  | 1.7<br><sub>-,1,-,3,-</sub> |  | 0.8<br><sub>-,0,-,2,-</sub> |  | 0.8 | 0.2 | 0.5 | 8.6 |
| Goga Bitadze (ORL) | 80% | 13.0<br><sub>12,12,-,11,6</sub> | 5.2<br><sub>6,4,-,6,2</sub> |  | 4.6<br><sub>6,3,-,0,4</sub> |  | 1.1<br><sub>1,0,-,1,0</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.0 | 0.8 | 10.9 |
| Nikola Vucevic (ORL) | 96% | 12.3<br><sub>5,4,15,16,6</sub> | 5.2<br><sub>0,0,5,5,3</sub> |  | 3.7<br><sub>1,2,3,4,1</sub> |  | 1.5<br><sub>1,0,3,2,0</sub> |  | 0.5<br><sub>0,0,1,0,1</sub> |  | 0.3 | 0.4 | 0.6 | 10.4 |
| Alex Morales (ORL) | 64% | 11.8<br><sub>-,4,-,7,9</sub> | 3.2<br><sub>-,0,-,2,0</sub> |  | 1.8<br><sub>-,1,-,2,1</sub> |  | 1.2<br><sub>-,0,-,1,0</sub> |  | 0.2<br><sub>-,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.2 |
| Colin Castleton (ORL) | 52% | 7.6<br><sub>-,4,-,7,-</sub> | 2.6<br><sub>-,7,-,2,-</sub> |  | 2.4<br><sub>-,2,-,2,-</sub> |  | 0.5<br><sub>-,1,-,0,-</sub> |  | 0.0<br><sub>-,0,-,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.5 |
| Trae Young (WAS) | 98% | 34.4<br><sub>37,34,38,34,38</sub> | 19.8<br><sub>22,25,22,14,21</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>1,4,6,5,7</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 9.6<br><sub>12,9,10,8,9</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>4,4,1,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 3.8 | 32.8 |
| Anthony Davis (WAS) | 98% | 33.4<br><sub>32,31,36,34,34</sub> | 20.6<br><sub>9,19,29,18,25</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 11.3<br><sub>9,6,10,5,13</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>0,4,0,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.7<br><sub>0,0,3,2,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 1.1 | 1.9 | 2.2 | 34.6 |
| Kyshawn George (WAS) | 98% | 30.9<br><sub>26,36,29,38,32</sub> | 14.9<br><sub>11,22,20,8,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>3,9,4,2,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.0<br><sub>3,5,2,11,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,0,2,0,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.1 | 2.2 | 24.0 |
| AJ Dybantsa (WAS) | 88% | 29.0<br><sub>-,-,-,27,30</sub> | 14.9<br><sub>-,-,-,19,17</sub> | 16.5 · –<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>-,-,-,2,8</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>-,-,-,2,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.3 | 1.7 | 21.7 |
| Alex Sarr (WAS) | 100% | 25.8<br><sub>25,23,26,26,29</sub> | 10.8<br><sub>7,10,12,18,3</sub> | 10.5 · – | 6.2<br><sub>4,2,6,4,8</sub> | 6.5 | 2.2<br><sub>5,3,1,2,0</sub> | 1.5 | 0.9<br><sub>1,0,0,2,1</sub> | 0.5 | 0.8 | 1.9 | 1.4 | 19.2 |
| Bilal Coulibaly (WAS) | 98% | 24.9<br><sub>26,25,29,27,22</sub> | 8.8<br><sub>11,7,3,17,1</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,4,5,2,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>0,0,1,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.9 | 1.2 | 14.3 |
| Bub Carrington (WAS) | 98% | 21.2<br><sub>11,21,28,20,20</sub> | 6.8<br><sub>3,9,6,3,9</sub> |  | 2.5<br><sub>1,2,0,1,4</sub> |  | 2.8<br><sub>0,1,3,3,2</sub> |  | 1.1<br><sub>1,3,2,0,3</sub> |  | 0.6 | 0.2 | 1.5 | 12.1 |
| Tre Johnson (WAS) | 72% | 16.9<br><sub>26,23,23,-,13</sub> | 6.3<br><sub>20,13,7,-,4</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,2,3,-,2</sub> |  | 0.9<br><sub>0,2,2,-,0</sub> |  | 0.8<br><sub>4,2,1,-,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.5 | 0.3 | 0.8 | 9.3 |
| Deandre Ayton (WAS) | 98% | 15.3<br><sub>14,16,12,12,17</sub> | 5.3<br><sub>4,6,0,10,3</sub> |  | 4.6<br><sub>6,5,4,3,3</sub> |  | 0.7<br><sub>1,0,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.8 | 10.5 |
| Khris Middleton (WAS) | 88% | 13.1<br><sub>16,-,13,23,5</sub> | 4.1<br><sub>6,-,0,4,0</sub> |  | 2.2<br><sub>2,-,1,3,0</sub> |  | 1.0<br><sub>0,-,0,2,0</sub> |  | 0.4<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.1 | 0.9 | 7.3 |
| Will Riley (WAS) | 67% | 8.5<br><sub>1,5,4,-,1</sub> | 3.9<br><sub>0,2,2,-,0</sub> |  | 1.2<br><sub>0,0,0,-,0</sub> |  | 0.7<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 5.8 |
| Reece Beekman (WAS) | 38% | 7.2<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.1 |
| Felix Okpara (WAS) | 38% | 6.9<br><sub>1,-,-,-,-</sub> | 3.1<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 3.8 |
| Tre Mann (WAS) | 52% | 6.1<br><sub>1,-,-,-,1</sub> | 2.6<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |

</details>


### CHI @ PHI
Out: Dominick Barlow (PHI), Ariel Hukporti (PHI)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.5–120.1 | CHI 32% | 3.14 / 1.47 | PHI -6.5 | 233.5 | PHI -11.5 covers 37%; o239.5 38% |
| Expected (weighted by chance each plays) | 113.0–121.3 | CHI 28% | 3.63 / 1.38 | PHI -8.5 | 234.5 | PHI -11.5 covers 41%; o239.5 39% |
| if Joel Embiid plays | 112.4–121.9 | CHI 25% | 4.02 / 1.33 | PHI -9.5 | 234.5 | PHI -11.5 covers 44%; o239.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dailyn Swain (CHI) | Day-To-Day | 70% | 7.3 | 2.5 | 1.0 | 1.1 | 0.1 | 0.6 | 0.1 | 1.4 | 4.6 | small |
| Joel Embiid (PHI) | Questionable | 55% | 32.8 | 24.4 | 8.9 | 5.0 | 1.3 | 0.9 | 1.2 | 2.8 | 38.3 | full tables below |
| Nic Claxton (CHI) | Doubtful | 20% | 16.9 | 6.6 | 4.5 | 1.7 | 0.1 | 0.4 | 0.7 | 1.1 | 12.8 | small |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson | 96% | 33.3<br><sub>33,38,32,38,31</sub> | 18.4<br><sub>21,30,17,20,23</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>6,14,5,6,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>1,3,3,4,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>2,1,1,3,6</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 1.4 | 2.9 | 27.7 |
| Norman Powell | 98% | 30.5<br><sub>33,33,24,37,31</sub> | 18.5<br><sub>25,18,20,30,16</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>4,2,1,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>1,3,2,2,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.2<br><sub>2,3,4,4,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.2 | 2.2 | 24.0 |
| Josh Giddey | 98% | 28.7<br><sub>25,30,24,31,25</sub> | 12.1<br><sub>6,9,11,10,13</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>4,8,1,8,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>9,10,4,11,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,1,1,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.5 | 3.1 | 26.8 |
| Matas Buzelis | 98% | 26.4<br><sub>17,35,22,33,20</sub> | 14.4<br><sub>7,21,11,17,14</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>5,5,1,5,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>3,2,2,3,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 1.2 | 2.3 | 21.7 |
| Jalen Smith | 91% | 24.6<br><sub>24,24,20,30,27</sub> | 11.6<br><sub>14,14,7,17,5</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 8.1<br><sub>13,3,6,11,12</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>1,1,1,5,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,2,3,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.5 | 0.9 | 1.2 | 21.0 |
| Tre Jones | 98% | 19.5<br><sub>24,18,15,18,20</sub> | 10.3<br><sub>11,10,8,11,12</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,2,1,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>8,3,0,3,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.8 | 0.1 | 1.2 | 16.3 |
| Isaac Okoro | 98% | 17.5<br><sub>28,14,11,18,18</sub> | 5.7<br><sub>12,0,1,7,6</sub> |  | 1.9<br><sub>3,1,1,0,3</sub> |  | 1.0<br><sub>1,0,4,1,2</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 8.6 |
| Leonard Miller | 98% | 15.8<br><sub>24,21,14,17,11</sub> | 7.5<br><sub>19,7,9,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,4,9,0,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.7<br><sub>2,1,1,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.4 | 0.4 | 0.9 | 12.3 |
| Buddy Hield | 91% | 13.1<br><sub>15,16,13,9,17</sub> | 5.7<br><sub>13,9,3,2,5</sub> |  | 1.9<br><sub>2,2,0,3,3</sub> |  | 1.0<br><sub>2,2,1,1,1</sub> |  | 0.8<br><sub>3,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 8.6 |
| Noa Essengue | 88% | 12.7<br><sub>17,-,16,10,16</sub> | 4.3<br><sub>4,-,0,3,10</sub> |  | 2.2<br><sub>1,-,4,0,4</sub> |  | 0.5<br><sub>1,-,0,1,0</sub> |  | 0.3<br><sub>0,-,0,1,1</sub> |  | 0.6 | 0.2 | 0.8 | 7.1 |
| Tobe Awaka | 60% | 11.5<br><sub>-,-,12,-,12</sub> | 3.7<br><sub>-,-,4,-,2</sub> |  | 4.3<br><sub>-,-,6,-,7</sub> |  | 0.6<br><sub>-,-,0,-,1</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.5 | 0.6 | 8.7 |
| Patrick Williams | 38% | 9.5<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 5.3 |
| Jordan Hawkins | 58% | 8.4<br><sub>-,-,7,-,6</sub> | 3.5<br><sub>-,-,4,-,0</sub> |  | 1.2<br><sub>-,-,1,-,0</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Zach Collins | 67% | 8.3<br><sub>-,11,6,-,2</sub> | 3.7<br><sub>-,2,2,-,0</sub> |  | 2.7<br><sub>-,3,2,-,0</sub> |  | 0.8<br><sub>-,1,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 7.1 |
| Jaylin Sellers | 58% | 6.4<br><sub>-,-,12,-,3</sub> | 3.2<br><sub>-,-,0,-,3</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 0.7<br><sub>-,-,1,-,1</sub> |  | 0.3<br><sub>-,-,0,-,1</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 36.8<br><sub>36,34,36,38,38</sub> | 27.6<br><sub>26,29,27,27,38</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>4,5,5,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.9<br><sub>4,4,4,4,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,1,3,3,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.7 | 2.5 | 37.7 |
| Jaylen Brown | 98% | 35.4<br><sub>35,40,34,-,38</sub> | 25.5<br><sub>27,16,20,-,16</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,4,10,-,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,4,2,-,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>3,2,1,-,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.5 | 0.7 | 3.4 | 36.9 |
| LeBron James | 98% | 33.8<br><sub>-,33,33,34,-</sub> | 20.9<br><sub>-,18,13,20,-</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>-,2,5,9,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>-,5,10,8,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>-,0,2,2,-</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.7 | 2.8 | 35.4 |
| VJ Edgecombe | 88% | 32.8<br><sub>30,-,29,36,37</sub> | 14.0<br><sub>17,-,8,13,10</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.4<br><sub>13,-,7,8,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>2,-,2,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>5,-,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.6 | 0.5 | 1.6 | 24.2 |
| Dean Wade | 88% | 25.6<br><sub>28,37,17,27,30</sub> | 5.4<br><sub>7,7,0,0,4</sub> |  | 4.1<br><sub>2,5,1,2,5</sub> |  | 1.7<br><sub>0,1,1,1,10</sub> |  | 0.7<br><sub>2,1,0,0,0</sub> |  | 1.1 | 0.4 | 0.7 | 11.2 |
| Anfernee Simons | 97% | 25.3<br><sub>20,27,27,31,25</sub> | 12.2<br><sub>4,5,20,21,19</sub> |  | 2.5<br><sub>1,3,3,2,0</sub> |  | 2.1<br><sub>2,3,1,1,2</sub> |  | 2.1<br><sub>1,1,6,5,5</sub> |  | 0.9 | 0.2 | 1.2 | 16.8 |
| Kentavious Caldwell-Pope | 98% | 20.8<br><sub>28,31,21,21,18</sub> | 6.3<br><sub>12,7,4,5,3</sub> |  | 2.3<br><sub>2,3,2,3,2</sub> |  | 1.8<br><sub>1,3,1,3,1</sub> |  | 0.8<br><sub>4,1,0,1,1</sub> |  | 1.0 | 0.3 | 0.8 | 10.4 |
| Adem Bona | 97% | 16.9<br><sub>10,25,4,14,22</sub> | 4.7<br><sub>0,6,1,0,2</sub> |  | 4.6<br><sub>1,13,1,2,5</sub> |  | 0.7<br><sub>1,1,0,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.0 | 10.0 |
| Jabari Walker | 91% | 12.9<br><sub>12,-,-,-,19</sub> | 5.2<br><sub>6,-,-,-,12</sub> |  | 3.4<br><sub>3,-,-,-,6</sub> |  | 0.7<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,1</sub> |  | 0.5 | 0.2 | 0.6 | 9.3 |
| Labaron Philon Jr. | 66% | 8.9<br><sub>4,13,-,6,10</sub> | 3.6<br><sub>0,5,-,2,5</sub> |  | 1.3<br><sub>0,2,-,2,1</sub> |  | 0.6<br><sub>0,1,-,0,0</sub> |  | 0.3<br><sub>0,1,-,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.5 |
| Tacko Fall | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Rayan Rupert | 23% | 8.2<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 5.0 |
| Justin Edwards | 52% | 7.7<br><sub>1,-,-,-,2</sub> | 3.2<br><sub>0,-,-,-,0</sub> |  | 1.1<br><sub>0,-,-,-,1</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.3 | 4.9 |
| Caleb Love | 35% | 6.7<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson (CHI) | 96% | 33.2<br><sub>33,38,32,38,31</sub> | 18.3<br><sub>21,30,17,20,23</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 6.6<br><sub>6,14,5,6,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>1,3,3,4,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>2,1,1,3,6</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 1.4 | 2.9 | 27.5 |
| Norman Powell (CHI) | 98% | 30.5<br><sub>33,33,24,37,31</sub> | 18.2<br><sub>25,18,20,30,16</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>4,2,1,2,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.2<br><sub>1,3,2,2,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.1<br><sub>2,3,4,4,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.2 | 2.2 | 23.8 |
| Josh Giddey (CHI) | 98% | 28.8<br><sub>25,30,24,31,25</sub> | 12.1<br><sub>6,9,11,10,13</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>4,8,1,8,4</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>9,10,4,11,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,1,1,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.5 | 3.1 | 26.8 |
| Matas Buzelis (CHI) | 98% | 26.4<br><sub>17,35,22,33,20</sub> | 14.4<br><sub>7,21,11,17,14</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.6<br><sub>5,5,1,5,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>3,2,2,3,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 1.2 | 2.3 | 21.7 |
| Jalen Smith (CHI) | 91% | 24.6<br><sub>24,24,20,30,27</sub> | 11.6<br><sub>14,14,7,17,5</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 8.1<br><sub>13,3,6,11,12</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,1,1,5,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,2,3,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.5 | 0.9 | 1.2 | 21.0 |
| Tre Jones (CHI) | 98% | 19.4<br><sub>24,18,15,18,20</sub> | 10.2<br><sub>11,10,8,11,12</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 2.6<br><sub>3,2,1,4,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>8,3,0,3,4</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.8 | 0.1 | 1.2 | 16.1 |
| Isaac Okoro (CHI) | 98% | 17.5<br><sub>28,14,11,18,18</sub> | 5.6<br><sub>12,0,1,7,6</sub> |  | 1.9<br><sub>3,1,1,0,3</sub> |  | 1.0<br><sub>1,0,4,1,2</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 8.5 |
| Leonard Miller (CHI) | 98% | 15.8<br><sub>24,21,14,17,11</sub> | 7.4<br><sub>19,7,9,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>3,4,9,0,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.7<br><sub>2,1,1,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.4 | 0.3 | 0.9 | 12.3 |
| Buddy Hield (CHI) | 91% | 13.1<br><sub>15,16,13,9,17</sub> | 5.7<br><sub>13,9,3,2,5</sub> |  | 1.9<br><sub>2,2,0,3,3</sub> |  | 1.1<br><sub>2,2,1,1,1</sub> |  | 0.8<br><sub>3,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 8.6 |
| Noa Essengue (CHI) | 88% | 12.6<br><sub>17,-,16,10,16</sub> | 4.3<br><sub>4,-,0,3,10</sub> |  | 2.2<br><sub>1,-,4,0,4</sub> |  | 0.5<br><sub>1,-,0,1,0</sub> |  | 0.3<br><sub>0,-,0,1,1</sub> |  | 0.6 | 0.2 | 0.7 | 7.0 |
| Tobe Awaka (CHI) | 60% | 11.5<br><sub>-,-,12,-,12</sub> | 3.8<br><sub>-,-,4,-,2</sub> |  | 4.3<br><sub>-,-,6,-,7</sub> |  | 0.6<br><sub>-,-,0,-,1</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.5 | 0.6 | 8.7 |
| Patrick Williams (CHI) | 38% | 9.5<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 5.3 |
| Jordan Hawkins (CHI) | 58% | 8.4<br><sub>-,-,7,-,6</sub> | 3.5<br><sub>-,-,4,-,0</sub> |  | 1.2<br><sub>-,-,1,-,0</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Zach Collins (CHI) | 67% | 8.2<br><sub>-,11,6,-,2</sub> | 3.6<br><sub>-,2,2,-,0</sub> |  | 2.7<br><sub>-,3,2,-,0</sub> |  | 0.8<br><sub>-,1,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 7.1 |
| Jaylin Sellers (CHI) | 58% | 6.3<br><sub>-,-,12,-,3</sub> | 3.3<br><sub>-,-,0,-,3</sub> |  | 1.2<br><sub>-,-,0,-,0</sub> |  | 0.7<br><sub>-,-,1,-,1</sub> |  | 0.3<br><sub>-,-,0,-,1</sub> |  | 0.1 | 0.1 | 0.5 | 5.2 |
| Tyrese Maxey (PHI) | 98% | 35.2<br><sub>36,34,36,38,38</sub> | 25.0<br><sub>26,29,27,27,38</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>4,5,5,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.6<br><sub>4,4,4,4,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>4,1,3,3,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7 | 0.6 | 2.2 | 34.6 |
| Jaylen Brown (PHI) | 98% | 34.3<br><sub>35,40,34,-,38</sub> | 22.9<br><sub>27,16,20,-,16</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,4,10,-,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>5,4,2,-,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>3,2,1,-,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4 | 0.5 | 3.1 | 33.8 |
| Joel Embiid (PHI) | 100% | 32.8<br><sub>36,-,39,33,-</sub> | 24.4<br><sub>28,-,21,10,-</sub> | 22.5 · – | 8.9<br><sub>11,-,11,7,-</sub> | 8.5 | 5.0<br><sub>10,-,2,7,-</sub> | 4.5 | 1.3<br><sub>0,-,0,0,-</sub> | 1.5 | 0.9 | 1.2 | 2.8 | 38.3 |
| LeBron James (PHI) | 98% | 32.4<br><sub>-,33,33,34,-</sub> | 17.8<br><sub>-,18,13,20,-</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 6.9<br><sub>-,2,5,9,-</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>-,5,10,8,-</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>-,0,2,2,-</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.7 | 2.6 | 32.0 |
| VJ Edgecombe (PHI) | 88% | 31.0<br><sub>30,-,29,36,37</sub> | 12.5<br><sub>17,-,8,13,10</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>13,-,7,8,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>2,-,2,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.7<br><sub>5,-,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.5 | 1.4 | 22.5 |
| Anfernee Simons (PHI) | 97% | 22.2<br><sub>20,27,27,31,25</sub> | 10.9<br><sub>4,5,20,21,19</sub> |  | 2.2<br><sub>1,3,3,2,0</sub> |  | 1.9<br><sub>2,3,1,1,2</sub> |  | 1.9<br><sub>1,1,6,5,5</sub> |  | 0.8 | 0.2 | 1.0 | 15.0 |
| Dean Wade (PHI) | 88% | 21.9<br><sub>28,37,17,27,30</sub> | 4.7<br><sub>7,7,0,0,4</sub> |  | 3.7<br><sub>2,5,1,2,5</sub> |  | 1.5<br><sub>0,1,1,1,10</sub> |  | 0.6<br><sub>2,1,0,0,0</sub> |  | 1.0 | 0.3 | 0.5 | 9.9 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.6<br><sub>28,31,21,21,18</sub> | 5.7<br><sub>12,7,4,5,3</sub> |  | 2.1<br><sub>2,3,2,3,2</sub> |  | 1.6<br><sub>1,3,1,3,1</sub> |  | 0.7<br><sub>4,1,0,1,1</sub> |  | 0.9 | 0.2 | 0.7 | 9.4 |
| Adem Bona (PHI) | 97% | 10.9<br><sub>10,25,4,14,22</sub> | 3.2<br><sub>0,6,1,0,2</sub> |  | 2.9<br><sub>1,13,1,2,5</sub> |  | 0.5<br><sub>1,1,0,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.6 | 6.6 |
| Jabari Walker (PHI) | 91% | 9.3<br><sub>12,-,-,-,19</sub> | 3.8<br><sub>6,-,-,-,12</sub> |  | 2.4<br><sub>3,-,-,-,6</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.7 |
| Tacko Fall (PHI) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.8 |
| Labaron Philon Jr. (PHI) | 66% | 7.0<br><sub>4,13,-,6,10</sub> | 2.7<br><sub>0,5,-,2,5</sub> |  | 1.0<br><sub>0,2,-,2,1</sub> |  | 0.4<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,1,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.2 |
| Rayan Rupert (PHI) | 23% | 6.3<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 3.8 |
| Caleb Love (PHI) | 35% | 6.2<br><sub>1,-,-,-,-</sub> | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 0.9 |
| Justin Edwards (PHI) | 52% | 6.1<br><sub>1,-,-,-,2</sub> | 2.6<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,1</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |

</details>


### SAC @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.2–123.6 | SAC 26% | 3.92 / 1.34 | DAL -9.5 | 237.5 | DAL -10.5 covers 47%; o234.5 57% |
| Expected (weighted by chance each plays) | 113.8–123.3 | SAC 25% | 4.05 / 1.33 | DAL -9.5 | 236.5 | DAL -10.5 covers 47%; o234.5 55% |
| if Zach LaVine plays | 115.0–122.8 | SAC 29% | 3.44 / 1.41 | DAL -7.5 | 237.5 | DAL -10.5 covers 43%; o234.5 57% |
| if Kyrie Irving plays | 113.1–125.1 | SAC 20% | 5.00 / 1.25 | DAL -12.5 | 238.5 | DAL -10.5 covers 54%; o234.5 58% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Cardwell (SAC) | Questionable | 55% | 15.4 | 4.4 | 5.6 | 1.1 | 0.1 | 0.5 | 1.2 | 0.7 | 11.2 | small |
| Santi Aldama (DAL) | Doubtful | 20% | 18.2 | 8.5 | 4.3 | 1.8 | 0.9 | 0.7 | 0.4 | 0.8 | 14.6 | small |
| Zach LaVine (SAC) | Questionable | 55% | 33.3 | 20.4 | 3.5 | 2.8 | 2.2 | 0.9 | 0.2 | 2.1 | 26.7 | full tables below |
| Kyrie Irving (DAL) | Questionable | 55% | 31.6 | 23.5 | 4.0 | 4.8 | 2.8 | 1.3 | 0.5 | 2.0 | 32.3 | full tables below |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 96% | 37.3<br><sub>37,36,33,41,37</sub> | 28.6<br><sub>33,22,19,34,38</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>2,3,3,6,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>4,7,5,14,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>2,2,3,3,9</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.4 | 3.7 | 39.2 |
| Domantas Sabonis | 98% | 35.8<br><sub>39,35,37,40,38</sub> | 19.2<br><sub>27,15,20,9,11</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 14.6<br><sub>19,15,14,15,14</sub> | 13.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>10,3,8,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.1 | 0.4 | 2.9 | 40.6 |
| Precious Achiuwa | 98% | 33.5<br><sub>26,39,14,41,25</sub> | 16.6<br><sub>14,12,4,24,6</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>6,10,1,9,5</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,0,0,2,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.4 | 1.0 | 1.6 | 27.8 |
| De'Andre Hunter | 98% | 32.2<br><sub>25,29,33,37,32</sub> | 15.7<br><sub>4,7,24,24,19</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>7,6,6,5,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,1,2,1,0</sub> |  | 1.9<br><sub>0,2,5,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 1.6 | 23.1 |
| Jonathan Mogbo | 63% | 21.9<br><sub>-,18,18,-,25</sub> | 6.8<br><sub>-,7,2,-,6</sub> |  | 3.8<br><sub>-,3,5,-,3</sub> |  | 1.2<br><sub>-,1,0,-,3</sub> |  | 0.6<br><sub>-,1,0,-,0</sub> |  | 0.8 | 0.6 | 0.9 | 11.7 |
| Emanuel Sharp | 96% | 21.3<br><sub>14,14,20,18,24</sub> | 6.4<br><sub>5,3,5,0,2</sub> |  | 1.4<br><sub>0,1,0,0,1</sub> |  | 1.2<br><sub>1,0,2,0,1</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.3 | 0.8 | 9.0 |
| Daeqwon Plowden | 80% | 19.0<br><sub>20,16,17,-,4</sub> | 6.9<br><sub>3,3,0,-,4</sub> |  | 2.3<br><sub>0,3,2,-,0</sub> |  | 1.0<br><sub>0,1,0,-,0</sub> |  | 0.9<br><sub>1,1,0,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 10.2 |
| Malik Monk | 97% | 17.8<br><sub>12,12,13,8,14</sub> | 9.7<br><sub>0,6,3,2,8</sub> |  | 2.0<br><sub>1,1,2,1,0</sub> |  | 3.1<br><sub>2,2,6,1,3</sub> |  | 1.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 1.3 | 14.8 |
| Nique Clifford | 88% | 15.9<br><sub>2,-,5,4,11</sub> | 6.3<br><sub>0,-,2,0,0</sub> |  | 2.5<br><sub>0,-,0,0,1</sub> |  | 1.9<br><sub>0,-,0,1,2</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 10.7 |
| Alex Karaban | 67% | 13.7<br><sub>-,-,11,12,10</sub> | 4.4<br><sub>-,-,0,6,0</sub> |  | 1.9<br><sub>-,-,1,0,1</sub> |  | 0.7<br><sub>-,-,1,0,1</sub> |  | 0.4<br><sub>-,-,0,2,0</sub> |  | 0.4 | 0.2 | 0.8 | 7.0 |
| Leaky Black | 38% | 13.2<br><sub>-,-,8,-,-</sub> | 3.4<br><sub>-,-,2,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.4 | 0.5 | 6.7 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 34.4<br><sub>17,-,40,33,39</sub> | 29.3<br><sub>14,-,29,26,33</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>5,-,6,5,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>6,-,11,8,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,-,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 1.1 | 3.1 | 42.6 |
| P.J. Washington | 98% | 33.8<br><sub>33,36,41,27,34</sub> | 17.1<br><sub>20,12,20,18,3</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>13,4,9,9,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>0,2,2,0,1</sub> |  | 1.8<br><sub>2,0,4,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 1.1 | 1.9 | 26.6 |
| Zaccharie Risacher | 91% | 30.3<br><sub>32,32,30,29,28</sub> | 11.0<br><sub>11,11,6,13,12</sub> |  | 6.0<br><sub>6,4,8,6,6</sub> |  | 1.9<br><sub>1,2,1,1,3</sub> |  | 1.4<br><sub>1,1,1,2,3</sub> |  | 1.3 | 1.2 | 1.2 | 18.8 |
| Naji Marshall | 67% | 26.8<br><sub>33,21,-,-,-</sub> | 16.2<br><sub>15,10,-,-,-</sub> |  | 3.9<br><sub>4,4,-,-,-</sub> |  | 4.1<br><sub>6,5,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.2 | 0.1 | 1.9 | 24.3 |
| Daniel Gafford | 98% | 26.4<br><sub>15,23,26,27,29</sub> | 13.0<br><sub>4,12,8,7,18</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 8.1<br><sub>3,9,9,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>5,2,3,2,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.9 | 1.8 | 1.4 | 23.0 |
| Max Christie | 98% | 26.2<br><sub>38,26,26,22,18</sub> | 11.8<br><sub>16,5,11,11,2</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>4,5,5,5,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>4,1,3,2,0</sub> |  | 2.0<br><sub>2,1,3,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 1.2 | 16.7 |
| Caleb Martin | 91% | 21.0<br><sub>-,-,-,14,25</sub> | 7.7<br><sub>-,-,-,10,8</sub> |  | 2.9<br><sub>-,-,-,2,0</sub> |  | 1.7<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,2,2</sub> |  | 0.9 | 0.4 | 0.9 | 12.3 |
| Marcus Sasser | 91% | 16.6<br><sub>27,27,8,22,7</sub> | 7.0<br><sub>6,12,0,10,0</sub> |  | 1.5<br><sub>2,3,1,1,0</sub> |  | 2.5<br><sub>3,5,0,4,1</sub> |  | 1.0<br><sub>2,2,0,1,0</sub> |  | 0.6 | 0.1 | 0.9 | 10.9 |
| Morez Johnson Jr. | 98% | 15.5<br><sub>17,12,15,18,17</sub> | 6.7<br><sub>8,6,6,10,2</sub> |  | 2.2<br><sub>6,1,2,6,2</sub> |  | 1.6<br><sub>0,2,1,3,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 10.5 |
| Walter Clayton Jr. | 76% | 13.4<br><sub>1,15,17,15,9</sub> | 5.4<br><sub>0,3,15,0,3</sub> |  | 2.2<br><sub>1,2,4,2,2</sub> |  | 2.9<br><sub>0,5,4,5,1</sub> |  | 0.5<br><sub>0,1,2,0,1</sub> |  | 0.4 | 0.2 | 0.9 | 10.6 |
| Moussa Cisse | 63% | 8.7<br><sub>1,7,-,3,-</sub> | 3.4<br><sub>3,4,-,0,-</sub> |  | 3.5<br><sub>1,4,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.7 | 0.5 | 7.1 |
| Jett Howard | 52% | 7.5<br><sub>-,4,-,3,-</sub> | 3.1<br><sub>-,5,-,0,-</sub> |  | 0.9<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,1,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.6 |
| Tobi Lawal | 52% | 6.7<br><sub>1,4,-,3,-</sub> | 2.3<br><sub>0,5,-,0,-</sub> |  | 1.1<br><sub>0,1,-,0,-</sub> |  | 0.6<br><sub>0,1,-,1,-</sub> |  | 0.1<br><sub>0,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>if Kyrie Irving plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 32.6<br><sub>17,-,40,33,39</sub> | 25.9<br><sub>14,-,29,26,33</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>5,-,6,5,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>6,-,11,8,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.2<br><sub>2,-,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5 | 1.1 | 2.7 | 38.2 |
| P.J. Washington (DAL) | 98% | 31.7<br><sub>33,36,41,27,34</sub> | 14.4<br><sub>20,12,20,18,3</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>13,4,9,9,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>0,2,2,0,1</sub> |  | 1.6<br><sub>2,0,4,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 1.0 | 1.7 | 23.2 |
| Kyrie Irving (DAL) | 100% | 31.6<br><sub>25,-,33,27,35</sub> | 23.5<br><sub>24,-,18,15,35</sub> | 21.5 · – | 4.0<br><sub>1,-,6,2,4</sub> | 3.5 | 4.8<br><sub>3,-,6,4,9</sub> | 5.5 | 2.8<br><sub>5,-,2,3,5</sub> | 2.5 | 1.3 | 0.5 | 2.0 | 32.3 |
| Zaccharie Risacher (DAL) | 91% | 27.5<br><sub>32,32,30,29,28</sub> | 9.6<br><sub>11,11,6,13,12</sub> |  | 5.5<br><sub>6,4,8,6,6</sub> |  | 1.7<br><sub>1,2,1,1,3</sub> |  | 1.2<br><sub>1,1,1,2,3</sub> |  | 1.2 | 1.1 | 1.2 | 16.9 |
| Naji Marshall (DAL) | 67% | 24.5<br><sub>33,21,-,-,-</sub> | 13.3<br><sub>15,10,-,-,-</sub> |  | 3.7<br><sub>4,4,-,-,-</sub> |  | 3.6<br><sub>6,5,-,-,-</sub> |  | 0.8<br><sub>0,1,-,-,-</sub> |  | 1.1 | 0.1 | 1.7 | 20.6 |
| Daniel Gafford (DAL) | 98% | 24.2<br><sub>15,23,26,27,29</sub> | 11.6<br><sub>4,12,8,7,18</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>3,9,9,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>5,2,3,2,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.8 | 1.7 | 1.2 | 20.7 |
| Max Christie (DAL) | 98% | 24.1<br><sub>38,26,26,22,18</sub> | 10.1<br><sub>16,5,11,11,2</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>4,5,5,5,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>4,1,3,2,0</sub> |  | 1.7<br><sub>2,1,3,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.3 | 1.1 | 14.7 |
| Caleb Martin (DAL) | 91% | 17.6<br><sub>-,-,-,14,25</sub> | 6.2<br><sub>-,-,-,10,8</sub> |  | 2.5<br><sub>-,-,-,2,0</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,2,2</sub> |  | 0.8 | 0.3 | 0.7 | 10.0 |
| Morez Johnson Jr. (DAL) | 98% | 13.2<br><sub>17,12,15,18,17</sub> | 5.4<br><sub>8,6,6,10,2</sub> |  | 1.9<br><sub>6,1,2,6,2</sub> |  | 1.4<br><sub>0,2,1,3,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.8 | 8.6 |
| Marcus Sasser (DAL) | 91% | 12.4<br><sub>27,27,8,22,7</sub> | 4.7<br><sub>6,12,0,10,0</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.8<br><sub>3,5,0,4,1</sub> |  | 0.7<br><sub>2,2,0,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 7.6 |
| Walter Clayton Jr. (DAL) | 76% | 10.0<br><sub>1,15,17,15,9</sub> | 4.1<br><sub>0,3,15,0,3</sub> |  | 1.7<br><sub>1,2,4,2,2</sub> |  | 2.3<br><sub>0,5,4,5,1</sub> |  | 0.4<br><sub>0,1,2,0,1</sub> |  | 0.3 | 0.1 | 0.7 | 8.1 |
| Moussa Cisse (DAL) | 63% | 7.3<br><sub>1,7,-,3,-</sub> | 2.9<br><sub>3,4,-,0,-</sub> |  | 3.0<br><sub>1,4,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 6.1 |
| Jett Howard (DAL) | 52% | 5.9<br><sub>-,4,-,3,-</sub> | 2.8<br><sub>-,5,-,0,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,1,-,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 3.9 |
| Tobi Lawal (DAL) | 52% | 5.9<br><sub>1,4,-,3,-</sub> | 2.2<br><sub>0,5,-,0,-</sub> |  | 1.0<br><sub>0,1,-,0,-</sub> |  | 0.6<br><sub>0,1,-,1,-</sub> |  | 0.1<br><sub>0,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Darius Acuff Jr. (SAC) | 96% | 37.3<br><sub>37,36,33,41,37</sub> | 28.4<br><sub>33,22,19,34,38</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>2,3,3,6,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>4,7,5,14,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.5<br><sub>2,2,3,3,9</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.4 | 3.7 | 39.1 |
| Domantas Sabonis (SAC) | 98% | 35.7<br><sub>39,35,37,40,38</sub> | 19.1<br><sub>27,15,20,9,11</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 14.5<br><sub>19,15,14,15,14</sub> | 13.5<br><sub>o 48% · u 52%</sub> | 6.8<br><sub>10,3,8,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.1 | 0.4 | 2.9 | 40.4 |
| Precious Achiuwa (SAC) | 98% | 33.5<br><sub>26,39,14,41,25</sub> | 16.5<br><sub>14,12,4,24,6</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 9.2<br><sub>6,10,1,9,5</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 2.0<br><sub>1,0,0,2,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.4 | 1.0 | 1.6 | 27.7 |
| De'Andre Hunter (SAC) | 98% | 32.2<br><sub>25,29,33,37,32</sub> | 15.6<br><sub>4,7,24,24,19</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>7,6,6,5,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,1,2,1,0</sub> |  | 1.9<br><sub>0,2,5,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.3 | 1.6 | 23.0 |
| Jonathan Mogbo (SAC) | 63% | 21.9<br><sub>-,18,18,-,25</sub> | 6.7<br><sub>-,7,2,-,6</sub> |  | 3.7<br><sub>-,3,5,-,3</sub> |  | 1.1<br><sub>-,1,0,-,3</sub> |  | 0.6<br><sub>-,1,0,-,0</sub> |  | 0.8 | 0.6 | 0.9 | 11.6 |
| Emanuel Sharp (SAC) | 96% | 21.3<br><sub>14,14,20,18,24</sub> | 6.3<br><sub>5,3,5,0,2</sub> |  | 1.4<br><sub>0,1,0,0,1</sub> |  | 1.2<br><sub>1,0,2,0,1</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.3 | 0.8 | 8.9 |
| Daeqwon Plowden (SAC) | 80% | 19.1<br><sub>20,16,17,-,4</sub> | 6.8<br><sub>3,3,0,-,4</sub> |  | 2.3<br><sub>0,3,2,-,0</sub> |  | 1.0<br><sub>0,1,0,-,0</sub> |  | 0.9<br><sub>1,1,0,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 10.1 |
| Malik Monk (SAC) | 97% | 17.9<br><sub>12,12,13,8,14</sub> | 9.7<br><sub>0,6,3,2,8</sub> |  | 2.0<br><sub>1,1,2,1,0</sub> |  | 3.1<br><sub>2,2,6,1,3</sub> |  | 1.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 1.3 | 14.8 |
| Nique Clifford (SAC) | 88% | 15.9<br><sub>2,-,5,4,11</sub> | 6.3<br><sub>0,-,2,0,0</sub> |  | 2.5<br><sub>0,-,0,0,1</sub> |  | 2.0<br><sub>0,-,0,1,2</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 10.8 |
| Alex Karaban (SAC) | 67% | 13.8<br><sub>-,-,11,12,10</sub> | 4.3<br><sub>-,-,0,6,0</sub> |  | 2.0<br><sub>-,-,1,0,1</sub> |  | 0.7<br><sub>-,-,1,0,1</sub> |  | 0.4<br><sub>-,-,0,2,0</sub> |  | 0.4 | 0.2 | 0.8 | 7.0 |
| Leaky Black (SAC) | 38% | 13.2<br><sub>-,-,8,-,-</sub> | 3.4<br><sub>-,-,2,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.4 | 0.5 | 6.7 |

</details>

<details><summary>if Zach LaVine plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 34.3<br><sub>17,-,40,33,39</sub> | 29.1<br><sub>14,-,29,26,33</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>5,-,6,5,9</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>6,-,11,8,6</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>2,-,2,2,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.6 | 1.1 | 3.1 | 42.3 |
| P.J. Washington (DAL) | 98% | 33.8<br><sub>33,36,41,27,34</sub> | 17.1<br><sub>20,12,20,18,3</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 7.4<br><sub>13,4,9,9,10</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>0,2,2,0,1</sub> |  | 1.8<br><sub>2,0,4,2,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.1 | 1.1 | 1.9 | 26.6 |
| Zaccharie Risacher (DAL) | 91% | 30.4<br><sub>32,32,30,29,28</sub> | 11.0<br><sub>11,11,6,13,12</sub> |  | 5.9<br><sub>6,4,8,6,6</sub> |  | 1.8<br><sub>1,2,1,1,3</sub> |  | 1.4<br><sub>1,1,1,2,3</sub> |  | 1.3 | 1.2 | 1.3 | 18.8 |
| Naji Marshall (DAL) | 67% | 26.8<br><sub>33,21,-,-,-</sub> | 16.1<br><sub>15,10,-,-,-</sub> |  | 3.9<br><sub>4,4,-,-,-</sub> |  | 4.2<br><sub>6,5,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.2 | 0.1 | 1.9 | 24.1 |
| Daniel Gafford (DAL) | 98% | 26.4<br><sub>15,23,26,27,29</sub> | 13.0<br><sub>4,12,8,7,18</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 8.1<br><sub>3,9,9,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>5,2,3,2,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.9 | 1.8 | 1.4 | 23.0 |
| Max Christie (DAL) | 98% | 26.2<br><sub>38,26,26,22,18</sub> | 11.7<br><sub>16,5,11,11,2</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 3.1<br><sub>4,5,5,5,1</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>4,1,3,2,0</sub> |  | 1.9<br><sub>2,1,3,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 1.2 | 16.7 |
| Caleb Martin (DAL) | 91% | 21.0<br><sub>-,-,-,14,25</sub> | 7.7<br><sub>-,-,-,10,8</sub> |  | 2.9<br><sub>-,-,-,2,0</sub> |  | 1.6<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,2,2</sub> |  | 0.9 | 0.4 | 0.9 | 12.2 |
| Marcus Sasser (DAL) | 91% | 16.6<br><sub>27,27,8,22,7</sub> | 6.9<br><sub>6,12,0,10,0</sub> |  | 1.6<br><sub>2,3,1,1,0</sub> |  | 2.5<br><sub>3,5,0,4,1</sub> |  | 1.0<br><sub>2,2,0,1,0</sub> |  | 0.6 | 0.1 | 0.9 | 11.0 |
| Morez Johnson Jr. (DAL) | 98% | 15.5<br><sub>17,12,15,18,17</sub> | 6.7<br><sub>8,6,6,10,2</sub> |  | 2.2<br><sub>6,1,2,6,2</sub> |  | 1.6<br><sub>0,2,1,3,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 10.5 |
| Walter Clayton Jr. (DAL) | 76% | 13.5<br><sub>1,15,17,15,9</sub> | 5.4<br><sub>0,3,15,0,3</sub> |  | 2.3<br><sub>1,2,4,2,2</sub> |  | 2.9<br><sub>0,5,4,5,1</sub> |  | 0.5<br><sub>0,1,2,0,1</sub> |  | 0.4 | 0.2 | 0.9 | 10.6 |
| Moussa Cisse (DAL) | 63% | 8.7<br><sub>1,7,-,3,-</sub> | 3.4<br><sub>3,4,-,0,-</sub> |  | 3.5<br><sub>1,4,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.7 | 0.6 | 7.2 |
| Jett Howard (DAL) | 52% | 7.5<br><sub>-,4,-,3,-</sub> | 3.2<br><sub>-,5,-,0,-</sub> |  | 0.9<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,1,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Tobi Lawal (DAL) | 52% | 6.8<br><sub>1,4,-,3,-</sub> | 2.3<br><sub>0,5,-,0,-</sub> |  | 1.2<br><sub>0,1,-,0,-</sub> |  | 0.7<br><sub>0,1,-,1,-</sub> |  | 0.1<br><sub>0,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Darius Acuff Jr. (SAC) | 96% | 35.7<br><sub>37,36,33,41,37</sub> | 24.1<br><sub>33,22,19,34,38</sub> | 24.5 · –<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,3,3,6,5</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,7,5,14,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>2,2,3,3,9</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.4 | 3.4 | 34.4 |
| Domantas Sabonis (SAC) | 98% | 34.5<br><sub>39,35,37,40,38</sub> | 17.6<br><sub>27,15,20,9,11</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 13.7<br><sub>19,15,14,15,14</sub> | 13.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>10,3,8,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>1,0,0,0,0</sub> |  | 1.0 | 0.4 | 2.7 | 37.5 |
| Zach LaVine (SAC) | 100% | 33.3<br><sub>39,40,31,39,21</sub> | 20.4<br><sub>22,37,22,21,11</sub> | 21.5 · – | 3.5<br><sub>5,2,3,3,0</sub> | 2.5 | 2.8<br><sub>1,5,3,5,1</sub> | 2.5 | 2.2<br><sub>3,3,3,3,0</sub> | 2.5 | 0.9 | 0.2 | 2.1 | 26.7 |
| Precious Achiuwa (SAC) | 98% | 31.8<br><sub>26,39,14,41,25</sub> | 14.8<br><sub>14,12,4,24,6</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>6,10,1,9,5</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>1,0,0,2,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.0 | 1.4 | 25.0 |
| De'Andre Hunter (SAC) | 98% | 28.7<br><sub>25,29,33,37,32</sub> | 13.4<br><sub>4,7,24,24,19</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 5.0<br><sub>7,6,6,5,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,1,2,1,0</sub> |  | 1.5<br><sub>0,2,5,4,2</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.8 | 0.2 | 1.3 | 20.0 |
| Jonathan Mogbo (SAC) | 63% | 18.1<br><sub>-,18,18,-,25</sub> | 5.5<br><sub>-,7,2,-,6</sub> |  | 3.0<br><sub>-,3,5,-,3</sub> |  | 1.0<br><sub>-,1,0,-,3</sub> |  | 0.4<br><sub>-,1,0,-,0</sub> |  | 0.7 | 0.4 | 0.7 | 9.4 |
| Emanuel Sharp (SAC) | 96% | 16.7<br><sub>14,14,20,18,24</sub> | 5.0<br><sub>5,3,5,0,2</sub> |  | 1.1<br><sub>0,1,0,0,1</sub> |  | 1.0<br><sub>1,0,2,0,1</sub> |  | 0.5<br><sub>1,1,1,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.0 |
| Malik Monk (SAC) | 97% | 14.8<br><sub>12,12,13,8,14</sub> | 7.3<br><sub>0,6,3,2,8</sub> |  | 1.6<br><sub>1,1,2,1,0</sub> |  | 2.6<br><sub>2,2,6,1,3</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 1.0 | 11.4 |
| Daeqwon Plowden (SAC) | 80% | 13.6<br><sub>20,16,17,-,4</sub> | 4.3<br><sub>3,3,0,-,4</sub> |  | 1.6<br><sub>0,3,2,-,0</sub> |  | 0.7<br><sub>0,1,0,-,0</sub> |  | 0.5<br><sub>1,1,0,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.6 |
| Alex Karaban (SAC) | 67% | 11.4<br><sub>-,-,11,12,10</sub> | 3.6<br><sub>-,-,0,6,0</sub> |  | 1.7<br><sub>-,-,1,0,1</sub> |  | 0.6<br><sub>-,-,1,0,1</sub> |  | 0.2<br><sub>-,-,0,2,0</sub> |  | 0.4 | 0.2 | 0.6 | 5.8 |
| Nique Clifford (SAC) | 88% | 11.3<br><sub>2,-,5,4,11</sub> | 4.5<br><sub>0,-,2,0,0</sub> |  | 1.7<br><sub>0,-,0,0,1</sub> |  | 1.3<br><sub>0,-,0,1,2</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 7.4 |
| Leaky Black (SAC) | 38% | 9.2<br><sub>-,-,8,-,-</sub> | 2.5<br><sub>-,-,2,-,-</sub> |  | 1.6<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 4.7 |

</details>


### NOP @ MEM
Out: Yves Missi (NOP), Jordan Poole (NOP)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| GG Jackson REB under 3.5 | NOP @ MEM | draftkings | 2.02 | 2.01 | 1.66 | 60.2% | 46.3% | 49.8% | +0.5% | +21.6% | 0.1% |
| Cedric Coward 3PM under 1.5 | NOP @ MEM | draftkings | 2.04 | 2.03 | 1.68 | 59.5% | 45.8% | 49.2% | +0.4% | +21.4% | 0.1% |
| Dejounte Murray 3PM over 1.5 (2+) | NOP @ MEM | draftkings | 2.41 | 2.40 | 2.01 | 49.8% | 38.9% | 41.6% | +0.2% | +20.0% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.6–122.1 | NOP 40% | 2.49 / 1.67 | MEM -3.5 | 240.5 | MEM -6.5 covers 42%; o234.5 62% |
| Expected (weighted by chance each plays) | 118.3–122.1 | NOP 39% | 2.59 / 1.63 | MEM -4.5 | 239.5 | MEM -6.5 covers 43%; o234.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scotty Pippen Jr. (MEM) | Doubtful | 20% | 11.9 | 5.7 | 1.6 | 2.2 | 0.5 | 0.8 | 0.2 | 1.1 | 9.5 | small |
| Quinten Post (MEM) | Questionable | 55% | 8.2 | 3.6 | 1.7 | 0.5 | 0.3 | 0.2 | 0.3 | 0.5 | 5.7 | small |
| Jaron Pierre Jr. (NOP) | Doubtful | 20% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |
| Malik Dia (NOP) | Doubtful | 20% | 8.6 | 3.6 | 1.5 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 91% | 33.3<br><sub>31,37,30,32,29</sub> | 18.4<br><sub>9,26,6,19,15</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.3<br><sub>6,6,1,5,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 3.5<br><sub>3,4,3,3,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 2.4<br><sub>1,4,2,2,1</sub> | 1.5<br><sub>o 64% · u 36%</sub> | 1.3 | 0.6 | 1.8 | 27.3 |
| Dejounte Murray | 98% | 31.6<br><sub>30,35,30,-,-</sub> | 17.6<br><sub>16,22,10,-,-</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 6.3<br><sub>6,6,8,-,-</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>6,6,5,-,-</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>0,1,0,-,-</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.9 | 0.5 | 3.3 | 30.9 |
| Zion Williamson | 96% | 31.4<br><sub>33,33,32,31,30</sub> | 19.3<br><sub>23,17,25,22,15</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 5.9<br><sub>5,1,5,6,6</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,2,2,4</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 1.4 | 0.7 | 2.5 | 28.6 |
| Jeremiah Fears | 98% | 27.2<br><sub>24,23,24,29,31</sub> | 14.6<br><sub>7,10,11,22,20</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>0,6,4,8,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.3<br><sub>1,2,3,13,7</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,0,1,3,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.2 | 0.6 | 2.3 | 23.3 |
| Saddiq Bey | 96% | 26.2<br><sub>22,25,26,24,26</sub> | 14.2<br><sub>20,14,9,10,25</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>3,4,0,4,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,3,3,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.5<br><sub>3,2,1,1,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.9 | 0.2 | 1.2 | 20.8 |
| Derik Queen | 98% | 22.9<br><sub>29,25,25,22,23</sub> | 10.3<br><sub>12,17,11,9,8</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>7,8,12,2,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>2,2,1,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>1,0,0,1,0</sub> |  | 1.0 | 0.9 | 2.1 | 20.2 |
| Herbert Jones | 96% | 22.6<br><sub>18,16,19,32,25</sub> | 7.6<br><sub>3,2,4,16,11</sub> |  | 2.8<br><sub>1,3,2,4,3</sub> |  | 1.9<br><sub>0,1,0,1,2</sub> |  | 0.9<br><sub>1,0,0,0,1</sub> |  | 1.3 | 0.5 | 1.1 | 12.3 |
| Bennedict Mathurin | 98% | 17.7<br><sub>15,20,14,19,19</sub> | 8.7<br><sub>4,9,5,10,7</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>2,4,1,3,1</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.6<br><sub>0,4,2,2,2</sub> |  | 0.6<br><sub>0,1,1,2,1</sub> |  | 0.5 | 0.2 | 1.3 | 13.4 |
| Karlo Matkovic | 88% | 16.5<br><sub>9,8,18,28,18</sub> | 6.5<br><sub>7,3,5,12,8</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>4,0,3,4,10</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>1,0,1,1,1</sub> |  | 0.6<br><sub>0,1,1,1,2</sub> | 0.5<br><sub>o 52% · u 48%</sub> | 0.6 | 1.1 | 0.8 | 11.7 |
| Trendon Watford | 52% | 14.6<br><sub>-,-,-,17,18</sub> | 5.9<br><sub>-,-,-,8,7</sub> |  | 2.7<br><sub>-,-,-,1,4</sub> |  | 1.5<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.4 | 1.1 | 10.2 |
| DeAndre Jordan | 47% | 11.5<br><sub>-,20,13,-,-</sub> | 3.4<br><sub>-,9,3,-,-</sub> |  | 4.6<br><sub>-,9,4,-,-</sub> |  | 0.7<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.7 | 0.6 | 8.7 |
| Bryce McGowens | 67% | 11.0<br><sub>-,-,3,6,15</sub> | 4.0<br><sub>-,-,0,4,3</sub> |  | 1.3<br><sub>-,-,0,1,0</sub> |  | 0.8<br><sub>-,-,0,2,1</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 6.1 |
| Julian Reese | 45% | 5.7<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.9 | 3.8 |
| AJ Johnson | 38% | 5.6<br><sub>-,-,-,-,3</sub> | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.8 | 0.9 | 1.0 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 96% | 30.7<br><sub>37,31,31,28,26</sub> | 17.2<br><sub>25,14,13,18,27</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 9.0<br><sub>13,11,7,12,9</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 5.8<br><sub>6,4,4,12,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>4,2,1,4,3</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.7 | 2.7 | 32.0 |
| Ty Jerome | 98% | 26.8<br><sub>32,32,30,24,-</sub> | 20.0<br><sub>28,31,15,10,-</sub> | 22.5 · –<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>2,4,1,2,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.9<br><sub>5,7,8,3,-</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>3,1,1,1,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.3 | 2.1 | 29.2 |
| Cedric Coward | 98% | 25.8<br><sub>-,32,31,27,23</sub> | 12.2<br><sub>-,17,16,17,10</sub> | 14.5 · –<br><sub>o 42% · u 58%</sub> | 6.1<br><sub>-,11,11,7,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>-,1,3,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>-,3,4,3,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.5 | 1.5 | 21.2 |
| Jaylen Wells | 98% | 25.2<br><sub>25,33,30,25,22</sub> | 11.0<br><sub>17,16,14,10,4</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 3.1<br><sub>4,5,3,1,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,3,0,0,0</sub> |  | 1.6<br><sub>4,2,2,2,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.1 | 0.8 | 15.7 |
| Jerami Grant | 98% | 23.1<br><sub>26,22,24,27,23</sub> | 10.9<br><sub>6,5,13,2,14</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>0,5,3,1,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>3,3,0,3,1</sub> |  | 1.3<br><sub>1,1,3,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.7 | 1.4 | 15.4 |
| Zach Edey | 98% | 20.4<br><sub>22,-,21,19,18</sub> | 8.6<br><sub>8,-,4,13,4</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>10,-,3,7,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>3,-,2,0,0</sub> |  | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.5 | 1.8 | 1.3 | 17.5 |
| Cam Spencer | 96% | 19.1<br><sub>17,16,18,23,25</sub> | 8.2<br><sub>11,13,8,8,10</sub> |  | 2.5<br><sub>2,2,5,6,5</sub> |  | 5.0<br><sub>1,1,5,8,13</sub> |  | 1.2<br><sub>3,3,2,1,2</sub> |  | 0.7 | 0.2 | 1.0 | 15.7 |
| Javon Small | 88% | 18.4<br><sub>-,-,-,-,20</sub> | 7.8<br><sub>-,-,-,-,7</sub> |  | 2.9<br><sub>-,-,-,-,1</sub> |  | 3.2<br><sub>-,-,-,-,5</sub> |  | 0.9<br><sub>-,-,-,-,2</sub> |  | 0.8 | 0.2 | 1.3 | 13.9 |
| GG Jackson | 96% | 16.7<br><sub>15,10,16,21,21</sub> | 9.4<br><sub>2,1,4,12,21</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,3,1,7,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,0,2,2,2</sub> |  | 0.9<br><sub>0,0,0,2,5</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.5 | 0.7 | 1.2 | 14.2 |
| Isaiah Stewart | 98% | 14.9<br><sub>16,22,15,16,21</sub> | 7.0<br><sub>4,13,4,18,24</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>2,5,4,3,4</sub> | 4.5<br><sub>o 38% · u 62%</sub> | 0.8<br><sub>0,2,0,0,0</sub> |  | 0.6<br><sub>0,2,0,2,2</sub> |  | 0.3 | 1.1 | 0.8 | 11.1 |
| Kris Murray | 63% | 10.8<br><sub>13,-,-,3,21</sub> | 3.1<br><sub>0,-,-,0,2</sub> |  | 1.6<br><sub>3,-,-,1,1</sub> |  | 0.8<br><sub>1,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 5.5 |
| Jahmai Mashack | 52% | 9.4<br><sub>-,-,-,-,4</sub> | 3.0<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.4 |
| Olivier-Maxence Prosper | 52% | 8.4<br><sub>-,-,-,3,4</sub> | 4.7<br><sub>-,-,-,4,2</sub> |  | 1.6<br><sub>-,-,-,1,1</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.9 |
| Taylor Hendricks | 64% | 7.6<br><sub>-,7,-,3,4</sub> | 3.2<br><sub>-,0,-,0,6</sub> |  | 1.5<br><sub>-,1,-,1,1</sub> |  | 0.4<br><sub>-,0,-,0,0</sub> |  | 0.3<br><sub>-,0,-,0,2</sub> |  | 0.4 | 0.3 | 0.3 | 5.1 |
| Karim Lopez | 58% | 6.0<br><sub>-,-,-,3,4</sub> | 2.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 4.1 |
| Carson Cooper | 58% | 5.3<br><sub>-,-,-,-,3</sub> | 2.0<br><sub>-,-,-,-,1</sub> |  | 2.4<br><sub>-,-,-,-,2</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.9 | 5.2 |

</details>


### MIL @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Terrence Shannon Jr. AST over 1.5 (2+) | MIL @ MIN | draftkings | 1.86 | 1.86 | 1.55 | 64.4% | 50.2% | 53.8% | +0.1% | +20.0% | 0.0% |
| Joan Beringer REB over 5.5 (6+) | MIL @ MIN | draftkings | 1.88 | 1.88 | 1.57 | 63.6% | 49.6% | 53.1% | +0.1% | +19.9% | 0.0% |

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.5<br><sub>32,31,32,27,27</sub> | 19.6<br><sub>34,13,23,23,15</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>5,6,10,3,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>4,3,7,0,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>5,1,3,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 0.9 | 0.3 | 2.3 | 28.8 |
| Ryan Rollins | 98% | 28.8<br><sub>34,25,32,17,26</sub> | 14.2<br><sub>11,15,19,4,9</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>7,4,2,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.2<br><sub>6,4,4,5,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>2,2,3,0,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.4 | 2.4 | 23.8 |
| Jaime Jaquez Jr. | 98% | 26.2<br><sub>35,27,25,27,23</sub> | 13.4<br><sub>19,21,8,19,8</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>11,8,6,4,7</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.7<br><sub>5,4,0,2,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.0<br><sub>2,2,0,3,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.7 | 0.2 | 2.2 | 22.2 |
| Kyle Kuzma | 98% | 25.9<br><sub>30,35,29,18,23</sub> | 10.8<br><sub>14,14,17,4,14</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>9,12,7,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>4,3,3,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>2,0,4,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.4 | 1.9 | 18.6 |
| Myles Turner | 98% | 23.7<br><sub>30,20,28,22,24</sub> | 9.2<br><sub>12,0,6,4,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>3,5,9,2,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.3<br><sub>1,1,4,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>2,0,0,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 1.8 | 1.3 | 15.3 |
| Kasparas Jakucionis | 88% | 18.8<br><sub>23,25,21,19,21</sub> | 6.2<br><sub>7,12,7,4,5</sub> | 7.5 · –<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>2,3,4,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.7 | 0.2 | 1.5 | 11.6 |
| Kel'el Ware | 88% | 18.5<br><sub>15,29,19,17,24</sub> | 9.5<br><sub>11,19,16,6,19</sub> |  | 5.9<br><sub>4,13,14,8,10</sub> |  | 0.9<br><sub>0,1,0,0,3</sub> |  | 0.8<br><sub>1,2,0,0,3</sub> |  | 0.7 | 0.6 | 1.4 | 16.3 |
| AJ Green | 98% | 17.8<br><sub>17,19,20,24,20</sub> | 5.7<br><sub>11,11,3,9,0</sub> |  | 2.0<br><sub>1,3,4,1,3</sub> |  | 1.1<br><sub>0,0,3,2,2</sub> |  | 0.9<br><sub>3,3,1,3,0</sub> |  | 0.4 | 0.1 | 0.6 | 8.8 |
| Cormac Ryan | 23% | 17.5 | 7.7 |  | 2.2 |  | 1.1 |  | 0.9 |  | 0.6 | 0.2 | 1.1 | 11.0 |
| Brayden Burries | 96% | 14.8<br><sub>8,17,16,17,21</sub> | 6.2<br><sub>3,10,4,10,14</sub> |  | 2.7<br><sub>1,5,2,5,3</sub> |  | 1.3<br><sub>3,2,1,1,1</sub> |  | 0.5<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 10.3 |
| Nate Ament | 76% | 11.9<br><sub>-,11,14,20,19</sub> | 4.8<br><sub>-,1,7,8,14</sub> |  | 2.0<br><sub>-,3,3,4,1</sub> |  | 0.6<br><sub>-,0,0,0,2</sub> |  | 0.4<br><sub>-,0,1,1,2</sub> |  | 0.4 | 0.2 | 0.8 | 7.4 |
| Caris LeVert | 25% | 11.2<br><sub>-,-,-,-,-</sub> | 3.9<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.7 | 6.8 |
| Gary Trent Jr. | 58% | 9.5<br><sub>-,-,-,7,6</sub> | 3.8<br><sub>-,-,-,3,3</sub> |  | 0.8<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,1,1</sub> |  | 0.3 | 0.0 | 0.3 | 5.0 |
| Ousmane Dieng | 88% | 9.2<br><sub>16,-,3,13,6</sub> | 2.9<br><sub>3,-,0,4,0</sub> |  | 1.4<br><sub>1,-,0,0,1</sub> |  | 1.1<br><sub>1,-,0,0,2</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 5.5 |
| Jericho Sims | 52% | 9.0<br><sub>-,-,-,7,-</sub> | 2.9<br><sub>-,-,-,0,-</sub> |  | 2.7<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.6 | 6.5 |
| Pete Nance | 25% | 8.8 | 2.6 |  | 1.4 |  | 0.5 |  | 0.2 |  | 0.2 | 0.2 | 0.3 | 4.6 |
| Kam Jones | 23% | 8.4 | 2.5 |  | 0.9 |  | 1.6 |  | 0.1 |  | 0.3 | 0.1 | 0.6 | 5.0 |
| Bogoljub Markovic | 38% | 6.3<br><sub>-,-,-,5,-</sub> | 2.5<br><sub>-,-,-,2,-</sub> |  | 1.4<br><sub>-,-,-,1,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 33.7<br><sub>31,37,35,33,39</sub> | 18.0<br><sub>14,14,19,23,19</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.7<br><sub>6,6,7,6,3</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>3,4,4,7,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>1,2,1,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.9 | 1.7 | 27.0 |
| Jonathan Kuminga | 98% | 31.5<br><sub>26,36,32,22,40</sub> | 15.1<br><sub>13,10,20,5,19</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.7<br><sub>4,10,3,1,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>1,1,5,0,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>3,0,3,1,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.6 | 1.6 | 23.5 |
| Ayo Dosunmu | 98% | 30.7<br><sub>23,26,32,30,38</sub> | 16.7<br><sub>9,9,17,15,27</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,1,3,7,9</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.5<br><sub>3,0,4,2,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>1,1,3,3,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.3 | 1.7 | 25.5 |
| Rudy Gobert | 98% | 29.1<br><sub>31,36,20,30,-</sub> | 9.9<br><sub>8,5,1,9,-</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 11.0<br><sub>13,20,4,13,-</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,2,1,4,-</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.0<br><sub>0,0,0,0,-</sub> |  | 1.0 | 1.3 | 1.2 | 22.7 |
| LaMelo Ball | 98% | 25.4<br><sub>17,31,28,29,20</sub> | 17.7<br><sub>15,11,8,24,10</sub> | 20.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>1,0,4,4,8</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 6.3<br><sub>8,6,8,7,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,1,2,6,0</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.2 | 2.7 | 27.9 |
| Terrence Shannon Jr. | 98% | 22.3<br><sub>23,24,27,20,18</sub> | 12.4<br><sub>15,14,19,11,2</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>4,4,6,3,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>3,5,2,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>3,3,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.1 | 1.1 | 17.5 |
| Joan Beringer | 93% | 21.4<br><sub>13,17,20,18,34</sub> | 10.2<br><sub>6,12,7,4,12</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 7.0<br><sub>6,7,9,4,6</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.9<br><sub>0,0,2,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.4 | 0.9 | 18.1 |
| Trey Lyles | 98% | 17.3<br><sub>14,13,22,17,17</sub> | 6.3<br><sub>3,3,7,10,6</sub> |  | 3.8<br><sub>6,1,3,5,0</sub> |  | 1.1<br><sub>2,1,1,0,0</sub> |  | 0.8<br><sub>1,1,1,1,1</sub> |  | 0.6 | 0.3 | 0.6 | 11.1 |
| Bones Hyland | 96% | 15.4<br><sub>15,5,16,20,14</sub> | 8.7<br><sub>3,0,13,19,6</sub> |  | 1.8<br><sub>3,1,1,0,1</sub> |  | 2.8<br><sub>2,2,3,8,3</sub> |  | 1.4<br><sub>0,0,3,3,0</sub> |  | 0.7 | 0.2 | 0.9 | 13.3 |
| Jaylen Clark | 86% | 15.2<br><sub>5,-,7,17,20</sub> | 5.7<br><sub>3,-,3,5,10</sub> |  | 1.9<br><sub>1,-,2,0,2</sub> |  | 1.2<br><sub>0,-,1,2,1</sub> |  | 0.6<br><sub>0,-,1,1,2</sub> |  | 0.9 | 0.2 | 0.4 | 8.8 |
| Zyon Pullin | 52% | 6.9<br><sub>5,-,-,2,-</sub> | 3.0<br><sub>2,-,-,2,-</sub> |  | 0.8<br><sub>1,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.8 |
| Rocco Zikarsky | 16% | 6.3 | 2.2 |  | 2.0 |  | 0.4 |  | 0.0 |  | 0.2 | 0.5 | 0.3 | 4.6 |
| Enrique Freeman | 16% | 6.2 | 1.9 |  | 1.4 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Cody Williams | 52% | 6.1<br><sub>5,-,-,2,-</sub> | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 0.9 |
| Isaiah Evans | 52% | 6.0<br><sub>4,-,-,2,-</sub> | 0.3<br><sub>0,-,-,0,-</sub> |  | 1.2<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 2.0 |

</details>


### BOS @ HOU
Out: Steven Adams (HOU), Devin Carter (BOS), Mitchell Robinson (BOS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White REB over 3.5 (4+) | BOS @ HOU | draftkings | 2.26 | 2.22 | 1.79 | 55.9% | 41.4% | 45.1% | +1.9% | +26.4% | 0.4% |
| Paul George AST under 3.5 | BOS @ HOU | draftkings | 1.99 | 1.98 | 1.63 | 61.4% | 47.0% | 50.6% | +0.6% | +22.1% | 0.2% |
| Payton Pritchard REB over 2.5 (3+) | BOS @ HOU | draftkings | 1.90 | 1.90 | 1.58 | 63.4% | 49.2% | 52.7% | +0.2% | +20.6% | 0.1% |
| Payton Pritchard RA over 6.5 (7+) | BOS @ HOU | draftkings | 1.97 | 1.97 | 1.64 | 60.9% | 47.5% | 50.8% | +0.2% | +20.0% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.2–109.5 | BOS 55% | 1.81 / 2.24 | HOU +2.5 | 220.5 | HOU -4.5 covers 33%; o219.5 52% |
| Expected (weighted by chance each plays) | 110.8–110.0 | BOS 53% | 1.90 / 2.11 | HOU +1.5 | 220.5 | HOU -4.5 covers 36%; o219.5 53% |
| if Reed Sheppard plays | 111.4–110.5 | BOS 53% | 1.88 / 2.13 | HOU +1.5 | 221.5 | HOU -4.5 covers 35%; o219.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Reed Sheppard (HOU) | Questionable | 55% | 24.1 | 10.6 | 2.4 | 3.1 | 1.9 | 1.3 | 0.6 | 1.1 | 16.1 | full tables below |
| Clint Capela (HOU) | Questionable | 55% | 15.3 | 4.3 | 4.9 | 1.0 | 0.0 | 0.5 | 0.8 | 0.6 | 10.2 | small |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 37.4<br><sub>38,37,28,42,35</sub> | 27.0<br><sub>13,36,23,40,26</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 8.9<br><sub>4,9,7,5,7</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>11,7,6,8,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>0,3,2,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 3.1 | 42.2 |
| Derrick White | 98% | 34.0<br><sub>36,33,18,33,26</sub> | 14.0<br><sub>17,12,5,16,9</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>1,4,6,5,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.6<br><sub>8,6,4,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>3,2,1,1,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 1.1 | 0.9 | 1.8 | 22.6 |
| Paul George | 98% | 33.1<br><sub>31,34,25,36,27</sub> | 19.2<br><sub>38,15,16,20,18</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,7,5,7,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>3,2,2,7,8</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>7,3,3,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.8 | 0.4 | 2.2 | 27.4 |
| Payton Pritchard | 98% | 32.0<br><sub>28,30,22,24,35</sub> | 15.9<br><sub>17,4,28,4,30</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>4,1,1,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>1,4,4,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>2,1,7,0,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.1 | 1.4 | 23.7 |
| Sam Hauser | 98% | 22.5<br><sub>18,23,20,25,18</sub> | 7.5<br><sub>11,6,11,11,6</sub> |  | 3.3<br><sub>4,2,4,4,3</sub> |  | 1.0<br><sub>1,2,1,0,2</sub> |  | 1.4<br><sub>3,2,3,3,2</sub> |  | 0.4 | 0.2 | 0.4 | 11.8 |
| Neemias Queta | 98% | 21.9<br><sub>22,22,19,15,20</sub> | 8.4<br><sub>3,15,7,7,13</sub> |  | 6.7<br><sub>4,6,5,3,6</sub> |  | 1.2<br><sub>2,1,1,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.6 | 1.1 | 1.0 | 16.4 |
| Baylor Scheierman | 98% | 19.9<br><sub>18,11,18,21,23</sub> | 5.5<br><sub>8,2,2,3,2</sub> |  | 3.3<br><sub>3,0,6,4,3</sub> |  | 1.3<br><sub>0,0,2,1,3</sub> |  | 0.8<br><sub>2,0,0,1,0</sub> |  | 0.7 | 0.1 | 0.6 | 10.2 |
| Jordan Walsh | 97% | 16.1<br><sub>13,20,18,24,11</sub> | 4.4<br><sub>0,5,4,15,2</sub> |  | 3.2<br><sub>6,3,3,6,2</sub> |  | 0.8<br><sub>1,0,2,1,0</sub> |  | 0.4<br><sub>0,1,0,3,0</sub> |  | 0.7 | 0.4 | 0.5 | 8.3 |
| Hugo Gonzalez | 91% | 12.8<br><sub>10,4,24,6,15</sub> | 3.2<br><sub>0,0,13,0,0</sub> |  | 2.6<br><sub>3,0,5,2,2</sub> |  | 0.5<br><sub>0,1,2,0,0</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.4 | 6.3 |
| Luka Garza | 96% | 11.9<br><sub>8,4,13,13,7</sub> | 5.7<br><sub>2,8,6,2,5</sub> |  | 2.9<br><sub>2,1,3,4,1</sub> |  | 0.7<br><sub>0,0,2,0,1</sub> |  | 0.4<br><sub>0,2,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 9.2 |
| Mike Conley | 43% | 8.5<br><sub>-,-,7,-,-</sub> | 2.4<br><sub>-,-,6,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,2,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.4 |
| Dillon Mitchell | 16% | 8.5 | 3.5 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Ron Harper Jr. | 58% | 7.3<br><sub>-,-,7,-,3</sub> | 2.8<br><sub>-,-,3,-,0</sub> |  | 1.1<br><sub>-,-,1,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,1,-,0</sub> |  | 0.4 | 0.1 | 0.2 | 4.3 |
| Amari Williams | 16% | 6.2 | 1.4 |  | 1.8 |  | 0.4 |  | 0.0 |  | 0.1 | 0.4 | 0.4 | 3.6 |
| Chris Cenac Jr. | 52% | 6.0<br><sub>-,-,5,-,2</sub> | 2.6<br><sub>-,-,3,-,3</sub> |  | 1.4<br><sub>-,-,1,-,2</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.7 | 4.5 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.4<br><sub>39,28,33,39,28</sub> | 16.6<br><sub>17,15,23,15,8</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>11,5,4,3,3</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>6,2,3,6,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.5 | 0.7 | 2.2 | 29.0 |
| Jabari Smith Jr. | 98% | 36.9<br><sub>33,39,30,35,33</sub> | 15.9<br><sub>14,16,14,22,30</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>5,12,2,3,9</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 2.2<br><sub>3,5,2,2,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>2,2,3,3,6</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.8 | 1.4 | 25.4 |
| Kevin Durant | 98% | 36.7<br><sub>37,30,31,37,27</sub> | 23.3<br><sub>22,22,18,28,14</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>4,9,5,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>2,3,4,1,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>3,1,2,1,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.7 | 1.1 | 3.1 | 33.8 |
| Alperen Sengun | 64% | 36.0<br><sub>33,37,-,-,33</sub> | 20.7<br><sub>17,29,-,-,16</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 9.6<br><sub>10,9,-,-,9</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>7,9,-,-,9</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.7<br><sub>1,1,-,-,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.2 | 1.1 | 3.1 | 36.5 |
| Fred VanVleet | 71% | 34.6<br><sub>-,29,29,33,-</sub> | 14.4<br><sub>-,5,24,16,-</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>-,4,6,5,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>-,5,5,6,-</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>-,0,4,3,-</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.4 | 1.4 | 23.4 |
| Marcus Smart | 67% | 30.6<br><sub>-,-,-,17,36</sub> | 10.3<br><sub>-,-,-,8,24</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>-,-,-,2,5</sub> |  | 3.3<br><sub>-,-,-,4,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>-,-,-,0,7</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 1.7 | 16.9 |
| Tari Eason | 98% | 26.5<br><sub>31,33,31,26,19</sub> | 10.2<br><sub>19,13,5,11,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>3,8,9,13,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>0,2,1,2,2</sub> |  | 1.2<br><sub>0,1,1,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.7 | 1.0 | 17.8 |
| Bogdan Bogdanovic | 91% | 18.8<br><sub>20,13,15,11,19</sub> | 6.9<br><sub>11,5,16,6,4</sub> |  | 2.2<br><sub>1,2,2,1,2</sub> |  | 1.6<br><sub>1,1,4,0,1</sub> |  | 1.1<br><sub>3,1,4,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 10.8 |
| Oscar Tshiebwe | 86% | 12.5<br><sub>-,-,14,11,4</sub> | 4.8<br><sub>-,-,7,0,2</sub> |  | 4.8<br><sub>-,-,5,5,1</sub> |  | 0.7<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 10.3 |
| Isaiah Crawford | 67% | 11.5<br><sub>1,1,5,-,19</sub> | 3.7<br><sub>0,0,3,-,8</sub> |  | 1.7<br><sub>0,0,0,-,1</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.4<br><sub>0,0,1,-,2</sub> |  | 0.3 | 0.3 | 0.4 | 6.0 |
| Jae'Sean Tate | 67% | 7.9<br><sub>1,1,4,-,6</sub> | 2.4<br><sub>0,0,0,-,0</sub> |  | 1.7<br><sub>0,1,0,-,3</sub> |  | 0.4<br><sub>0,0,0,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.5 |
| Bruce Thornton | 67% | 7.8<br><sub>4,1,3,-,6</sub> | 2.2<br><sub>0,0,5,-,5</sub> |  | 1.4<br><sub>0,0,0,-,1</sub> |  | 0.6<br><sub>0,0,0,-,0</sub> |  | 0.2<br><sub>0,0,1,-,1</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>if Reed Sheppard plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 37.4<br><sub>38,37,28,42,35</sub> | 26.9<br><sub>13,36,23,40,26</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 8.9<br><sub>4,9,7,5,7</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>11,7,6,8,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>0,3,2,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.4 | 3.1 | 42.1 |
| Derrick White (BOS) | 98% | 34.0<br><sub>36,33,18,33,26</sub> | 14.1<br><sub>17,12,5,16,9</sub> | 13.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>1,4,6,5,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.6<br><sub>8,6,4,7,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>3,2,1,1,1</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 1.2 | 1.0 | 1.8 | 22.7 |
| Paul George (BOS) | 98% | 33.0<br><sub>31,34,25,36,27</sub> | 19.1<br><sub>38,15,16,20,18</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>5,7,5,7,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>3,2,2,7,8</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.6<br><sub>7,3,3,1,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.8 | 0.4 | 2.2 | 27.4 |
| Payton Pritchard (BOS) | 98% | 32.0<br><sub>28,30,22,24,35</sub> | 15.9<br><sub>17,4,28,4,30</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>4,1,1,2,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>1,4,4,6,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>2,1,7,0,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.8 | 0.1 | 1.4 | 23.6 |
| Sam Hauser (BOS) | 98% | 22.4<br><sub>18,23,20,25,18</sub> | 7.5<br><sub>11,6,11,11,6</sub> |  | 3.3<br><sub>4,2,4,4,3</sub> |  | 1.0<br><sub>1,2,1,0,2</sub> |  | 1.4<br><sub>3,2,3,3,2</sub> |  | 0.4 | 0.2 | 0.4 | 11.8 |
| Neemias Queta (BOS) | 98% | 21.9<br><sub>22,22,19,15,20</sub> | 8.4<br><sub>3,15,7,7,13</sub> |  | 6.7<br><sub>4,6,5,3,6</sub> |  | 1.2<br><sub>2,1,1,2,0</sub> |  | 0.0<br><sub>0,1,0,0,0</sub> |  | 0.6 | 1.1 | 1.0 | 16.4 |
| Baylor Scheierman (BOS) | 98% | 19.9<br><sub>18,11,18,21,23</sub> | 5.5<br><sub>8,2,2,3,2</sub> |  | 3.4<br><sub>3,0,6,4,3</sub> |  | 1.3<br><sub>0,0,2,1,3</sub> |  | 0.8<br><sub>2,0,0,1,0</sub> |  | 0.7 | 0.1 | 0.6 | 10.2 |
| Jordan Walsh (BOS) | 97% | 16.1<br><sub>13,20,18,24,11</sub> | 4.4<br><sub>0,5,4,15,2</sub> |  | 3.2<br><sub>6,3,3,6,2</sub> |  | 0.7<br><sub>1,0,2,1,0</sub> |  | 0.4<br><sub>0,1,0,3,0</sub> |  | 0.7 | 0.3 | 0.5 | 8.3 |
| Hugo Gonzalez (BOS) | 91% | 12.8<br><sub>10,4,24,6,15</sub> | 3.2<br><sub>0,0,13,0,0</sub> |  | 2.6<br><sub>3,0,5,2,2</sub> |  | 0.5<br><sub>0,1,2,0,0</sub> |  | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 0.4 | 6.3 |
| Luka Garza (BOS) | 96% | 11.9<br><sub>8,4,13,13,7</sub> | 5.7<br><sub>2,8,6,2,5</sub> |  | 2.8<br><sub>2,1,3,4,1</sub> |  | 0.7<br><sub>0,0,2,0,1</sub> |  | 0.4<br><sub>0,2,0,0,0</sub> |  | 0.3 | 0.3 | 0.6 | 9.2 |
| Dillon Mitchell (BOS) | 16% | 8.6 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Mike Conley (BOS) | 43% | 8.5<br><sub>-,-,7,-,-</sub> | 2.4<br><sub>-,-,6,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,2,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.4 |
| Ron Harper Jr. (BOS) | 58% | 7.4<br><sub>-,-,7,-,3</sub> | 2.8<br><sub>-,-,3,-,0</sub> |  | 1.1<br><sub>-,-,1,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,1,-,0</sub> |  | 0.4 | 0.1 | 0.2 | 4.2 |
| Amari Williams (BOS) | 16% | 6.3 | 1.4 |  | 1.8 |  | 0.4 |  | 0.0 |  | 0.1 | 0.4 | 0.4 | 3.6 |
| Chris Cenac Jr. (BOS) | 52% | 6.0<br><sub>-,-,5,-,2</sub> | 2.6<br><sub>-,-,3,-,3</sub> |  | 1.4<br><sub>-,-,1,-,2</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.7 | 4.5 |
| Kevin Durant (HOU) | 98% | 36.2<br><sub>37,30,31,37,27</sub> | 22.7<br><sub>22,22,18,28,14</sub> | 21.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>4,9,5,5,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>2,3,4,1,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>3,1,2,1,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.7 | 1.2 | 3.0 | 33.0 |
| Amen Thompson (HOU) | 98% | 36.2<br><sub>39,28,33,39,28</sub> | 15.7<br><sub>17,15,23,15,8</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>11,5,4,3,3</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>6,2,3,6,1</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.4 | 0.7 | 2.0 | 27.5 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>33,39,30,35,33</sub> | 15.6<br><sub>14,16,14,22,30</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>5,12,2,3,9</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 2.1<br><sub>3,5,2,2,5</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>2,2,3,3,6</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.8 | 1.3 | 24.8 |
| Alperen Sengun (HOU) | 64% | 35.3<br><sub>33,37,-,-,33</sub> | 19.6<br><sub>17,29,-,-,16</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 9.5<br><sub>10,9,-,-,9</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>7,9,-,-,9</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.7<br><sub>1,1,-,-,0</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 1.2 | 1.1 | 3.0 | 35.1 |
| Fred VanVleet (HOU) | 71% | 33.1<br><sub>-,29,29,33,-</sub> | 13.1<br><sub>-,5,24,16,-</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 3.5<br><sub>-,4,6,5,-</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 4.9<br><sub>-,5,5,6,-</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>-,0,4,3,-</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.2 | 0.4 | 1.2 | 21.6 |
| Marcus Smart (HOU) | 67% | 26.9<br><sub>-,-,-,17,36</sub> | 8.7<br><sub>-,-,-,8,24</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>-,-,-,2,5</sub> |  | 2.8<br><sub>-,-,-,4,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>-,-,-,0,7</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.3 | 1.4 | 14.4 |
| Reed Sheppard (HOU) | 100% | 24.1<br><sub>30,24,23,-,-</sub> | 10.6<br><sub>19,13,7,-,-</sub> |  | 2.4<br><sub>6,0,3,-,-</sub> |  | 3.1<br><sub>7,4,4,-,-</sub> |  | 1.9<br><sub>5,2,1,-,-</sub> |  | 1.3 | 0.6 | 1.1 | 16.1 |
| Tari Eason (HOU) | 98% | 23.4<br><sub>31,33,31,26,19</sub> | 9.0<br><sub>19,13,5,11,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>3,8,9,13,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>0,2,1,2,2</sub> |  | 1.0<br><sub>0,1,1,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.6 | 0.9 | 15.7 |
| Bogdan Bogdanovic (HOU) | 91% | 13.6<br><sub>20,13,15,11,19</sub> | 4.9<br><sub>11,5,16,6,4</sub> |  | 1.6<br><sub>1,2,2,1,2</sub> |  | 1.2<br><sub>1,1,4,0,1</sub> |  | 0.7<br><sub>3,1,4,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 7.7 |
| Oscar Tshiebwe (HOU) | 86% | 9.9<br><sub>-,-,14,11,4</sub> | 4.0<br><sub>-,-,7,0,2</sub> |  | 3.6<br><sub>-,-,5,5,1</sub> |  | 0.5<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 8.1 |
| Isaiah Crawford (HOU) | 67% | 8.7<br><sub>1,1,5,-,19</sub> | 3.0<br><sub>0,0,3,-,8</sub> |  | 1.3<br><sub>0,0,0,-,1</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,0,1,-,2</sub> |  | 0.2 | 0.3 | 0.3 | 4.7 |
| Jae'Sean Tate (HOU) | 67% | 6.3<br><sub>1,1,4,-,6</sub> | 1.9<br><sub>0,0,0,-,0</sub> |  | 1.4<br><sub>0,1,0,-,3</sub> |  | 0.3<br><sub>0,0,0,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.2 | 3.7 |
| Bruce Thornton (HOU) | 67% | 5.8<br><sub>4,1,3,-,6</sub> | 1.9<br><sub>0,0,5,-,5</sub> |  | 1.0<br><sub>0,0,0,-,1</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.1<br><sub>0,0,1,-,1</sub> |  | 0.2 | 0.1 | 0.2 | 3.4 |

</details>


### UTA @ SAS
Out: Tobias Harris (SAS), Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Jusuf Nurkic (UTA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama BLK over 3.5 (4+) | UTA @ SAS | draftkings | 2.26 | 2.22 | 1.79 | 55.9% | 41.4% | 45.1% | +1.8% | +26.3% | 0.4% |
| Ace Bailey REB over 5.5 (6+) | UTA @ SAS | draftkings | 2.14 | 2.12 | 1.74 | 57.4% | 43.8% | 47.2% | +1.0% | +22.9% | 0.2% |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ace Bailey | 98% | 32.7<br><sub>22,29,34,40,37</sub> | 14.9<br><sub>6,17,17,19,9</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 6.3<br><sub>7,12,10,6,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,4,3,0,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>1,1,3,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 1.0 | 1.9 | 23.6 |
| Keyonte George | 98% | 32.4<br><sub>32,33,33,37,29</sub> | 21.2<br><sub>19,24,26,31,8</sub> | 21.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>1,9,3,4,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>10,10,6,3,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>3,2,0,5,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.2 | 3.4 | 31.1 |
| Darryn Peterson | 96% | 30.7<br><sub>30,30,26,26,36</sub> | 12.9<br><sub>15,8,14,18,16</sub> | 13.5 · –<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>3,3,7,5,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>1,2,4,3,4</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>1,0,3,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.4 | 1.8 | 20.4 |
| Lauri Markkanen | 98% | 30.3<br><sub>34,38,6,-,29</sub> | 19.3<br><sub>16,28,2,-,13</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>6,7,0,-,6</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>3,1,0,-,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 2.1<br><sub>4,5,0,-,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 1.4 | 27.5 |
| Jaxson Hayes | 98% | 24.7<br><sub>26,19,-,37,20</sub> | 8.2<br><sub>17,9,-,2,7</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 5.9<br><sub>5,5,-,11,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,1,-,4,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.1 | 0.9 | 15.8 |
| Isaiah Collier | 96% | 21.6<br><sub>18,13,21,24,20</sub> | 9.7<br><sub>10,6,7,7,8</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>2,3,8,7,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>7,6,8,6,4</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.2 | 2.1 | 18.6 |
| Brice Sensabaugh | 98% | 18.9<br><sub>16,17,9,18,19</sub> | 10.2<br><sub>10,7,11,16,12</sub> |  | 2.7<br><sub>3,6,2,3,3</sub> |  | 1.6<br><sub>2,1,0,1,2</sub> |  | 1.4<br><sub>2,1,3,4,2</sub> |  | 0.5 | 0.1 | 1.3 | 14.6 |
| Svi Mykhailiuk | 88% | 17.1<br><sub>21,14,13,15,18</sub> | 6.0<br><sub>3,2,0,3,6</sub> |  | 2.1<br><sub>4,3,1,2,1</sub> |  | 1.3<br><sub>1,0,0,1,3</sub> |  | 0.9<br><sub>0,0,0,1,2</sub> |  | 0.5 | 0.1 | 0.7 | 9.4 |
| Josh Okogie | 88% | 16.2<br><sub>-,10,21,28,14</sub> | 3.6<br><sub>-,2,0,5,0</sub> |  | 2.7<br><sub>-,2,2,9,1</sub> |  | 0.9<br><sub>-,2,0,3,0</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.6 | 0.2 | 0.5 | 7.1 |
| Mo Bamba | 63% | 14.6<br><sub>-,-,29,16,11</sub> | 4.6<br><sub>-,-,14,8,6</sub> |  | 5.0<br><sub>-,-,7,4,4</sub> |  | 0.8<br><sub>-,-,1,1,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.9 | 0.6 | 10.4 |
| Josh Green | 80% | 12.8<br><sub>-,3,25,24,2</sub> | 2.6<br><sub>-,0,6,2,0</sub> |  | 1.5<br><sub>-,0,4,2,0</sub> |  | 0.7<br><sub>-,1,1,2,0</sub> |  | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.9 |
| Kyle Filipowski | 66% | 12.2<br><sub>8,-,8,-,6</sub> | 5.7<br><sub>0,-,0,-,5</sub> |  | 3.7<br><sub>1,-,1,-,0</sub> |  | 1.4<br><sub>0,-,0,-,2</sub> |  | 0.5<br><sub>0,-,0,-,1</sub> |  | 0.6 | 0.2 | 0.8 | 10.7 |
| Tony Bradley | 38% | 8.2<br><sub>-,-,6,-,-</sub> | 2.8<br><sub>-,-,2,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.7 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 33.0<br><sub>32,29,27,39,34</sub> | 27.9<br><sub>25,23,29,36,43</sub> | 25.5 · –<br><sub>o 51% · u 49%</sub> | 11.5<br><sub>13,7,10,14,7</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,2,2,5,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>2,2,0,4,3</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 4.1 | 2.6 | 42.9 |
| Dylan Harper | 98% | 32.2<br><sub>36,28,30,37,39</sub> | 17.4<br><sub>20,22,13,13,25</sub> | 17.5 · –<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>3,5,6,5,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>2,2,6,8,6</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>1,3,0,2,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.4 | 2.0 | 28.1 |
| Devin Vassell | 98% | 32.2<br><sub>36,32,24,38,34</sub> | 13.7<br><sub>10,11,14,21,9</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>4,4,4,5,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>2,6,8,2,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>2,1,4,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4 | 0.5 | 1.2 | 21.5 |
| De'Aaron Fox | 98% | 32.0<br><sub>34,28,26,39,35</sub> | 16.8<br><sub>19,19,11,14,22</sub> | 14.5 · –<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>4,3,4,3,8</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.8<br><sub>9,9,6,4,7</sub> | 5.5<br><sub>o 59% · u 41%</sub> | 1.5<br><sub>2,2,2,1,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.5 | 0.5 | 2.3 | 27.8 |
| Stephon Castle | 98% | 29.5<br><sub>33,28,27,38,22</sub> | 16.6<br><sub>15,19,15,14,0</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 5.1<br><sub>7,4,5,6,5</sub> | 5.5<br><sub>o 42% · u 57%</sub> | 6.4<br><sub>5,8,5,8,4</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>3,3,3,1,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.3 | 2.8 | 28.1 |
| Julian Champagnie | 98% | 27.2<br><sub>25,28,25,31,27</sub> | 10.7<br><sub>6,12,26,6,12</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 4.9<br><sub>0,5,3,6,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,3,3,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>2,3,8,2,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.6 | 0.8 | 17.1 |
| Keldon Johnson | 98% | 20.9<br><sub>19,26,22,23,24</sub> | 10.3<br><sub>8,7,14,9,2</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>6,6,4,6,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>1,3,0,2,0</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.7 | 0.2 | 0.9 | 16.2 |
| Luke Kornet | 98% | 14.5<br><sub>16,14,17,14,14</sub> | 4.0<br><sub>7,0,0,1,2</sub> |  | 4.6<br><sub>3,4,4,6,8</sub> |  | 0.9<br><sub>0,1,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.5 | 9.6 |
| Carter Bryant | 98% | 9.8<br><sub>4,10,17,5,11</sub> | 3.8<br><sub>0,4,1,3,6</sub> |  | 1.8<br><sub>0,1,1,0,0</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.4<br><sub>0,0,0,1,2</sub> |  | 0.3 | 0.3 | 0.5 | 6.2 |
| Harrison Barnes | 58% | 8.9<br><sub>5,4,14,-,-</sub> | 3.2<br><sub>0,0,3,-,-</sub> |  | 1.1<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.8 |
| Maliq Brown | 80% | 6.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 2.6<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 3.3 |
| Jordan McLaughlin | 48% | 6.6<br><sub>-,3,7,-,-</sub> | 2.2<br><sub>-,0,0,-,-</sub> |  | 0.9<br><sub>-,1,0,-,-</sub> |  | 1.1<br><sub>-,0,2,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.3 |
| Tarris Reed Jr. | 52% | 6.2<br><sub>-,7,5,-,-</sub> | 2.6<br><sub>-,2,4,-,-</sub> |  | 2.3<br><sub>-,3,5,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.7 | 5.4 |
| Ja'Kobi Gillespie | 88% | 6.1<br><sub>-,3,-,-,-</sub> | 4.6<br><sub>-,3,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| David Jones Garcia | 48% | 5.8<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |

</details>


### POR @ DEN
Out: Julian Strawther (DEN), Ja Morant (POR), Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scoot Henderson 3PM under 1.5 | POR @ DEN | draftkings | 2.29 | 2.27 | 1.86 | 53.6% | 40.8% | 44.0% | +0.8% | +22.9% | 0.2% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.6–121.5 | POR 31% | 3.22 / 1.45 | DEN -6.5 | 236.5 | DEN -4.5 covers 57%; o230.5 62% |
| Expected (weighted by chance each plays) | 114.6–121.4 | POR 31% | 3.25 / 1.44 | DEN -7.5 | 235.5 | DEN -4.5 covers 57%; o230.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alpha Diallo (DEN) | Questionable | 55% | 12.9 | 3.5 | 1.6 | 1.2 | 0.3 | 0.5 | 0.3 | 1.0 | 6.4 | small |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 33.4<br><sub>23,38,33,32,30</sub> | 22.1<br><sub>18,26,23,24,24</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>10,7,4,9,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>4,6,9,7,2</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.5 | 3.5 | 35.5 |
| Damian Lillard | 98% | 31.4<br><sub>24,33,31,30,27</sub> | 17.0<br><sub>25,19,21,9,22</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>3,5,5,2,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.3<br><sub>6,2,4,2,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>6,2,4,1,3</sub> | 3.5<br><sub>o 37% · u 63%</sub> | 1.0 | 0.2 | 2.2 | 26.2 |
| Toumani Camara | 98% | 30.8<br><sub>23,27,24,26,31</sub> | 13.2<br><sub>18,19,12,13,14</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>2,3,1,2,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>3,1,1,1,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>4,5,4,3,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.4 | 1.2 | 19.4 |
| Jrue Holiday | 98% | 29.0<br><sub>21,26,30,24,22</sub> | 14.3<br><sub>8,12,22,6,14</sub> | 12.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>4,1,4,6,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.2<br><sub>1,8,3,4,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.0<br><sub>0,3,2,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 1.9 | 23.7 |
| Scoot Henderson | 98% | 27.2<br><sub>19,21,17,19,31</sub> | 12.9<br><sub>15,4,2,9,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>1,2,3,0,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.4 | 18.8 |
| Donovan Clingan | 98% | 25.0<br><sub>21,21,26,29,15</sub> | 9.8<br><sub>11,8,9,11,4</sub> | 10.5 · –<br><sub>o 46% · u 54%</sub> | 9.8<br><sub>7,10,10,8,9</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>2,3,1,1,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>2,0,2,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.5 | 1.4 | 1.1 | 21.4 |
| Sidy Cissoko | 96% | 21.0<br><sub>25,26,20,19,19</sub> | 5.6<br><sub>3,15,6,4,1</sub> |  | 2.9<br><sub>4,7,2,6,3</sub> |  | 1.7<br><sub>3,1,4,2,1</sub> |  | 0.5<br><sub>1,2,0,0,0</sub> |  | 0.8 | 0.3 | 0.8 | 10.3 |
| Robert Williams III | 98% | 18.9<br><sub>15,18,21,-,14</sub> | 7.1<br><sub>2,13,14,-,3</sub> | 5.5 · –<br><sub>o 56% · u 44%</sub> | 7.0<br><sub>10,6,10,-,3</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.2<br><sub>1,0,1,-,1</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.6 | 1.1 | 0.8 | 15.3 |
| Vit Krejci | 96% | 17.3<br><sub>15,3,7,8,24</sub> | 6.0<br><sub>1,0,4,2,5</sub> |  | 2.1<br><sub>2,2,0,0,4</sub> |  | 1.4<br><sub>3,0,0,1,2</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 9.5 |
| Yang Hansen | 64% | 10.2<br><sub>12,-,-,5,13</sub> | 3.9<br><sub>5,-,-,3,6</sub> |  | 2.7<br><sub>3,-,-,2,5</sub> |  | 0.6<br><sub>0,-,-,1,1</sub> |  | 0.3<br><sub>1,-,-,1,2</sub> |  | 0.3 | 0.3 | 0.6 | 7.2 |
| Micah Potter | 67% | 10.1<br><sub>12,-,-,9,4</sub> | 4.2<br><sub>4,-,-,1,2</sub> |  | 2.8<br><sub>3,-,-,2,1</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 7.6 |
| Chris Youngblood | 64% | 9.4<br><sub>-,-,-,-,7</sub> | 3.6<br><sub>-,-,-,-,3</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.2 | 0.3 | 5.5 |
| Branden Carlson | 58% | 8.7<br><sub>-,-,-,12,4</sub> | 4.4<br><sub>-,-,-,2,0</sub> |  | 1.9<br><sub>-,-,-,2,2</sub> |  | 0.6<br><sub>-,-,-,1,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.4 | 0.7 | 6.9 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 37.3<br><sub>37,43,36,38,37</sub> | 24.9<br><sub>6,42,19,23,39</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>10,3,6,1,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.1<br><sub>3,6,8,6,5</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>0,8,3,5,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.6 | 2.7 | 35.6 |
| Nikola Jokic | 98% | 36.8<br><sub>35,44,35,34,37</sub> | 26.2<br><sub>13,35,19,21,18</sub> | 25.5 · –<br><sub>o 47% · u 53%</sub> | 12.3<br><sub>7,15,7,13,7</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 10.2<br><sub>5,10,11,10,10</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>1,3,1,0,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.7 | 1.1 | 3.9 | 48.8 |
| Christian Braun | 98% | 34.3<br><sub>33,40,34,36,37</sub> | 13.4<br><sub>7,15,9,15,31</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>6,8,4,0,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>1,2,2,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.3<br><sub>1,0,1,3,7</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.5 | 1.2 | 20.5 |
| Aaron Gordon | 98% | 30.1<br><sub>29,37,25,31,29</sub> | 14.6<br><sub>20,7,7,15,15</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>6,5,4,11,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>1,4,2,3,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.4 | 1.4 | 23.4 |
| Cameron Johnson | 97% | 27.6<br><sub>11,-,-,-,34</sub> | 11.3<br><sub>5,-,-,-,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,-,-,-,9</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>1,-,-,-,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.5<br><sub>1,-,-,-,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.4 | 1.0 | 17.5 |
| DeMar DeRozan | 98% | 26.6<br><sub>28,24,29,26,24</sub> | 13.6<br><sub>13,12,21,6,3</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>2,3,4,2,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>0,3,2,5,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 0.4<br><sub>0,0,2,0,0</sub> |  | 0.9 | 0.4 | 1.6 | 19.7 |
| Trevon Brazile | 96% | 19.8<br><sub>18,28,17,32,19</sub> | 6.7<br><sub>4,17,6,11,6</sub> | 6.5 · –<br><sub>o 45% · u 55%</sub> | 4.7<br><sub>12,9,1,8,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 0.9<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>0,3,1,1,1</sub> |  | 0.6 | 0.6 | 0.9 | 12.3 |
| Marvin Bagley III | 98% | 12.6<br><sub>11,9,11,19,11</sub> | 5.6<br><sub>2,5,7,8,0</sub> |  | 3.7<br><sub>3,4,2,5,5</sub> |  | 0.6<br><sub>1,0,0,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 9.9 |
| Bryce Hopkins | 67% | 11.0<br><sub>2,19,31,14,-</sub> | 3.0<br><sub>0,2,13,0,-</sub> |  | 1.7<br><sub>1,2,3,2,-</sub> |  | 0.6<br><sub>0,1,1,0,-</sub> |  | 0.1<br><sub>0,0,1,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.3 |
| Tyus Jones | 91% | 9.9<br><sub>10,10,9,11,11</sub> | 2.6<br><sub>2,2,0,5,3</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 1.2<br><sub>0,0,2,1,0</sub> |  | 0.2<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Cam Whitmore | 58% | 7.4<br><sub>-,11,4,-,-</sub> | 3.5<br><sub>-,4,4,-,-</sub> |  | 1.3<br><sub>-,2,0,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.2 |
| Zeke Nnaji | 38% | 6.9<br><sub>-,-,4,-,-</sub> | 2.4<br><sub>-,-,5,-,-</sub> |  | 1.5<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.2 |
| Ryan Nembhard | 43% | 6.3<br><sub>2,-,4,-,-</sub> | 5.1<br><sub>5,-,4,-,-</sub> |  | 0.9<br><sub>1,-,0,-,-</sub> |  | 1.0<br><sub>1,-,1,-,-</sub> |  | 0.3<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 6.9 |
| DaRon Holmes II | 48% | 5.7<br><sub>2,-,4,-,-</sub> | 2.3<br><sub>3,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>1,-,1,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.8 |

</details>


### PHX @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Draymond Green (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Drew Timme (PHX), Mark Williams (PHX)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.1–114.4 | PHX 52% | 1.93 / 2.07 | GSW +1.5 | 229.5 | GSW -4.5 covers 36%; o227.5 54% |
| Expected (weighted by chance each plays) | 114.4–115.1 | PHX 48% | 2.08 / 1.93 | GSW -1.5 | 229.5 | GSW -4.5 covers 40%; o227.5 53% |
| if Gui Santos plays | 114.1–115.4 | PHX 46% | 2.16 / 1.87 | GSW -1.5 | 229.5 | GSW -4.5 covers 41%; o227.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Day-To-Day | 70% | 25.9 | 10.5 | 4.9 | 2.8 | 1.2 | 1.1 | 0.3 | 1.7 | 18.2 | full tables below |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 33.5<br><sub>29,36,34,39</sub> | 24.5<br><sub>23,43,3,20</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>4,7,2,2</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 5.8<br><sub>2,7,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,2,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 3.3 | 34.0 |
| Miles Bridges | 98% | 30.8<br><sub>29,33,32,37</sub> | 15.4<br><sub>8,16,17,24</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>4,7,8,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>0,3,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,2,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.5 | 1.6 | 24.3 |
| Dillon Brooks | 98% | 28.1<br><sub>27,34,33,21</sub> | 16.4<br><sub>10,15,19,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,2,5,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>0,5,5,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>1,1,3,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.5 | 21.9 |
| Jalen Green | 96% | 27.6<br><sub>25,26,31,25</sub> | 15.5<br><sub>10,12,20,2</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>2,2,4,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>3,1,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>2,1,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.3 | 2.4 | 22.0 |
| Collin Gillespie | 98% | 26.2<br><sub>21,28,23,33</sub> | 10.2<br><sub>0,11,9,16</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,4,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>2,9,2,10</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>0,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.2 | 1.5 | 17.9 |
| Oso Ighodaro | 97% | 20.2<br><sub>15,-,-,21</sub> | 6.0<br><sub>8,-,-,2</sub> |  | 5.2<br><sub>3,-,-,9</sub> |  | 2.8<br><sub>3,-,-,5</sub> |  | 0.0<br><sub>0,-,-,0</sub> |  | 0.8 | 0.6 | 1.3 | 13.9 |
| Jordan Goodwin | 98% | 19.0<br><sub>22,20,17,25</sub> | 7.1<br><sub>3,9,12,11</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,2,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,4,2,5</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.1<br><sub>1,1,4,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.2 | 0.8 | 12.8 |
| Khaman Maluach | 96% | 17.2<br><sub>17,28,26,17</sub> | 6.1<br><sub>2,9,12,9</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>6,9,7,6</sub> | 7.5<br><sub>o 41% · u 59%</sub> | 0.6<br><sub>1,3,1,0</sub> |  | 0.2<br><sub>0,1,0,0</sub> |  | 0.4 | 0.9 | 1.1 | 12.0 |
| Luke Kennard | 98% | 14.6<br><sub>-,18,16,12</sub> | 5.2<br><sub>-,11,9,9</sub> |  | 1.8<br><sub>-,4,1,1</sub> |  | 1.4<br><sub>-,1,2,2</sub> |  | 0.6<br><sub>-,3,3,1</sub> |  | 0.6 | 0.1 | 0.7 | 8.4 |
| Ryan Dunn | 96% | 11.8<br><sub>14,13,14,11</sub> | 3.8<br><sub>3,5,6,5</sub> |  | 2.6<br><sub>2,5,2,3</sub> |  | 0.8<br><sub>0,0,1,1</sub> |  | 0.3<br><sub>0,1,1,1</sub> |  | 0.6 | 0.3 | 0.5 | 7.1 |
| Pat Spencer | 64% | 7.7<br><sub>7,-,-,-</sub> | 2.7<br><sub>3,-,-,-</sub> |  | 1.0<br><sub>3,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.0 |
| Rasheer Fleming | 58% | 6.7<br><sub>12,-,3,-</sub> | 2.6<br><sub>1,-,0,-</sub> |  | 1.2<br><sub>2,-,1,-</sub> |  | 0.3<br><sub>0,-,0,-</sub> |  | 0.2<br><sub>0,-,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.1 |
| Duop Reath | 64% | 6.6<br><sub>9,3,7,-</sub> | 2.5<br><sub>5,0,5,-</sub> |  | 1.3<br><sub>1,0,3,-</sub> |  | 0.3<br><sub>0,0,0,-</sub> |  | 0.2<br><sub>1,0,1,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.1 |
| Jamaree Bouyea | 58% | 6.2<br><sub>7,-,3,-</sub> | 2.6<br><sub>3,-,2,-</sub> |  | 0.9<br><sub>2,-,0,-</sub> |  | 0.9<br><sub>2,-,1,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Koa Peat | 52% | 5.9<br><sub>7,-,3,-</sub> | 2.3<br><sub>4,-,0,-</sub> |  | 1.4<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>0,-,0,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.1 | 0.1 | 0.4 | 4.1 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 96% | 33.8<br><sub>37,36,31,35,24</sub> | 21.0<br><sub>18,26,31,26,6</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 7.4<br><sub>13,9,12,9,1</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>6,5,6,1,0</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,6,1,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.5 | 3.5 | 32.1 |
| Brandin Podziemski | 86% | 33.6<br><sub>33,-,33,32,33</sub> | 19.8<br><sub>18,-,18,8,21</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.5<br><sub>2,-,7,5,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 5.5<br><sub>3,-,5,6,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,-,3,0,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.2 | 2.5 | 30.8 |
| De'Anthony Melton | 98% | 26.1<br><sub>20,27,19,20,21</sub> | 13.2<br><sub>10,25,3,8,16</sub> |  | 3.8<br><sub>1,5,4,6,5</sub> |  | 3.2<br><sub>0,5,3,0,3</sub> |  | 1.9<br><sub>2,4,1,2,4</sub> |  | 1.4 | 0.4 | 2.1 | 20.2 |
| Georges Niang | 96% | 25.7<br><sub>13,23,18,23,19</sub> | 10.8<br><sub>4,4,9,7,11</sub> |  | 3.6<br><sub>3,4,2,3,5</sub> |  | 1.8<br><sub>0,2,0,2,1</sub> |  | 1.9<br><sub>0,0,3,1,3</sub> |  | 0.5 | 0.2 | 1.6 | 16.2 |
| Al Horford | 98% | 23.9<br><sub>19,-,19,18,17</sub> | 8.0<br><sub>3,-,11,4,3</sub> |  | 4.9<br><sub>5,-,3,5,2</sub> |  | 2.2<br><sub>0,-,0,2,0</sub> |  | 1.3<br><sub>1,-,3,0,1</sub> |  | 0.7 | 0.9 | 0.9 | 15.1 |
| Brandon Williams | 98% | 23.5<br><sub>9,24,15,14,17</sub> | 15.1<br><sub>4,20,6,11,9</sub> |  | 3.3<br><sub>2,3,3,3,2</sub> |  | 4.3<br><sub>1,5,3,1,1</sub> |  | 0.9<br><sub>0,2,2,0,0</sub> |  | 1.1 | 0.4 | 2.2 | 22.7 |
| Will Richard | 98% | 23.4<br><sub>3,31,3,23,13</sub> | 6.9<br><sub>0,11,0,6,3</sub> |  | 2.8<br><sub>0,0,0,3,3</sub> |  | 1.6<br><sub>0,1,0,0,2</sub> |  | 1.0<br><sub>0,3,0,0,1</sub> |  | 1.4 | 0.2 | 0.8 | 11.3 |
| Gary Payton II | 98% | 19.3<br><sub>11,17,12,10,8</sub> | 9.1<br><sub>7,2,7,2,2</sub> |  | 3.9<br><sub>2,1,2,2,4</sub> |  | 1.7<br><sub>0,0,0,1,0</sub> |  | 0.7<br><sub>1,0,1,0,0</sub> |  | 1.1 | 0.3 | 1.0 | 14.7 |
| Graham Ike | 67% | 18.1<br><sub>12,26,3,-,-</sub> | 8.2<br><sub>10,12,3,-,-</sub> |  | 4.1<br><sub>2,10,0,-,-</sub> |  | 1.6<br><sub>1,2,1,-,-</sub> |  | 0.6<br><sub>2,0,1,-,-</sub> |  | 0.7 | 0.3 | 1.0 | 13.9 |
| LJ Cryer | 52% | 15.1<br><sub>-,14,3,-,-</sub> | 6.1<br><sub>-,3,6,-,-</sub> |  | 1.4<br><sub>-,1,0,-,-</sub> |  | 1.1<br><sub>-,1,2,-,-</sub> |  | 0.9<br><sub>-,1,2,-,-</sub> |  | 0.3 | 0.1 | 0.8 | 8.6 |
| Charles Bassey | 91% | 15.0<br><sub>-,13,2,2,9</sub> | 6.0<br><sub>-,10,0,0,6</sub> |  | 6.0<br><sub>-,7,1,0,4</sub> |  | 0.7<br><sub>-,0,0,0,1</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.9 | 12.7 |
| Malevy Leons | 52% | 14.0<br><sub>-,4,3,-,-</sub> | 4.1<br><sub>-,2,0,-,-</sub> |  | 2.5<br><sub>-,0,1,-,-</sub> |  | 1.0<br><sub>-,0,0,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.7 | 0.4 | 0.7 | 7.6 |

</details>

<details><summary>if Gui Santos plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | 96% | 34.0<br><sub>37,36,31,35,24</sub> | 20.2<br><sub>18,26,31,26,6</sub> | 18.5 · –<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>13,9,12,9,1</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 3.6<br><sub>6,5,6,1,0</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.8<br><sub>1,6,1,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.6 | 3.4 | 31.3 |
| Brandin Podziemski (GSW) | 86% | 33.3<br><sub>33,-,33,32,33</sub> | 18.5<br><sub>18,-,18,8,21</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>2,-,7,5,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 5.0<br><sub>3,-,5,6,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,-,3,0,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.2 | 2.2 | 29.1 |
| Gui Santos (GSW) | 100% | 25.9<br><sub>20,23,28,-,16</sub> | 10.5<br><sub>5,7,13,-,2</sub> |  | 4.9<br><sub>4,4,3,-,5</sub> |  | 2.8<br><sub>2,3,1,-,1</sub> |  | 1.2<br><sub>1,1,1,-,0</sub> |  | 1.1 | 0.3 | 1.7 | 18.2 |
| De'Anthony Melton (GSW) | 98% | 25.0<br><sub>20,27,19,20,21</sub> | 12.0<br><sub>10,25,3,8,16</sub> |  | 3.8<br><sub>1,5,4,6,5</sub> |  | 3.0<br><sub>0,5,3,0,3</sub> |  | 1.8<br><sub>2,4,1,2,4</sub> |  | 1.4 | 0.4 | 1.8 | 18.7 |
| Georges Niang (GSW) | 96% | 22.9<br><sub>13,23,18,23,19</sub> | 9.3<br><sub>4,4,9,7,11</sub> |  | 3.3<br><sub>3,4,2,3,5</sub> |  | 1.4<br><sub>0,2,0,2,1</sub> |  | 1.6<br><sub>0,0,3,1,3</sub> |  | 0.5 | 0.2 | 1.3 | 14.0 |
| Al Horford (GSW) | 98% | 21.8<br><sub>19,-,19,18,17</sub> | 7.3<br><sub>3,-,11,4,3</sub> |  | 4.7<br><sub>5,-,3,5,2</sub> |  | 1.8<br><sub>0,-,0,2,0</sub> |  | 1.1<br><sub>1,-,3,0,1</sub> |  | 0.6 | 0.9 | 0.8 | 13.8 |
| Brandon Williams (GSW) | 98% | 20.2<br><sub>9,24,15,14,17</sub> | 12.8<br><sub>4,20,6,11,9</sub> |  | 2.8<br><sub>2,3,3,3,2</sub> |  | 3.5<br><sub>1,5,3,1,1</sub> |  | 0.7<br><sub>0,2,2,0,0</sub> |  | 0.9 | 0.3 | 1.8 | 19.2 |
| Will Richard (GSW) | 98% | 19.5<br><sub>3,31,3,23,13</sub> | 5.5<br><sub>0,11,0,6,3</sub> |  | 2.4<br><sub>0,0,0,3,3</sub> |  | 1.2<br><sub>0,1,0,0,2</sub> |  | 0.7<br><sub>0,3,0,0,1</sub> |  | 1.1 | 0.2 | 0.7 | 9.1 |
| Gary Payton II (GSW) | 98% | 16.9<br><sub>11,17,12,10,8</sub> | 8.1<br><sub>7,2,7,2,2</sub> |  | 3.4<br><sub>2,1,2,2,4</sub> |  | 1.4<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>1,0,1,0,0</sub> |  | 0.9 | 0.2 | 0.8 | 12.9 |
| Graham Ike (GSW) | 67% | 15.8<br><sub>12,26,3,-,-</sub> | 6.8<br><sub>10,12,3,-,-</sub> |  | 3.6<br><sub>2,10,0,-,-</sub> |  | 1.4<br><sub>1,2,1,-,-</sub> |  | 0.5<br><sub>2,0,1,-,-</sub> |  | 0.6 | 0.3 | 0.8 | 11.8 |
| LJ Cryer (GSW) | 52% | 13.1<br><sub>-,14,3,-,-</sub> | 5.4<br><sub>-,3,6,-,-</sub> |  | 1.2<br><sub>-,1,0,-,-</sub> |  | 1.0<br><sub>-,1,2,-,-</sub> |  | 0.8<br><sub>-,1,2,-,-</sub> |  | 0.3 | 0.1 | 0.7 | 7.6 |
| Charles Bassey (GSW) | 91% | 12.9<br><sub>-,13,2,2,9</sub> | 5.5<br><sub>-,10,0,0,6</sub> |  | 5.0<br><sub>-,7,1,0,4</sub> |  | 0.6<br><sub>-,0,0,0,1</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.4 | 0.9 | 0.8 | 11.1 |
| Malevy Leons (GSW) | 52% | 11.5<br><sub>-,4,3,-,-</sub> | 3.6<br><sub>-,2,0,-,-</sub> |  | 2.1<br><sub>-,0,1,-,-</sub> |  | 0.9<br><sub>-,0,0,-,-</sub> |  | 0.1<br><sub>-,0,0,-,-</sub> |  | 0.6 | 0.3 | 0.6 | 6.5 |
| Devin Booker (PHX) | 98% | 33.5<br><sub>29,36,34,39</sub> | 24.4<br><sub>23,43,3,20</sub> | 23.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>4,7,2,2</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 5.8<br><sub>2,7,7,5</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>0,2,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 3.3 | 34.0 |
| Miles Bridges (PHX) | 98% | 30.9<br><sub>29,33,32,37</sub> | 15.4<br><sub>8,16,17,24</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>4,7,8,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>0,3,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,2,2,2</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.5 | 1.6 | 24.2 |
| Dillon Brooks (PHX) | 98% | 28.0<br><sub>27,34,33,21</sub> | 16.4<br><sub>10,15,19,22</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,2,5,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>0,5,5,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>1,1,3,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.2 | 1.5 | 21.9 |
| Jalen Green (PHX) | 96% | 27.7<br><sub>25,26,31,25</sub> | 15.5<br><sub>10,12,20,2</sub> | 15.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>2,2,4,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>3,1,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>2,1,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.0 | 0.3 | 2.4 | 22.1 |
| Collin Gillespie (PHX) | 98% | 26.3<br><sub>21,28,23,33</sub> | 10.2<br><sub>0,11,9,16</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,4,1,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 4.2<br><sub>2,9,2,10</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>0,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.2 | 1.5 | 17.9 |
| Oso Ighodaro (PHX) | 97% | 20.1<br><sub>15,-,-,21</sub> | 5.9<br><sub>8,-,-,2</sub> |  | 5.2<br><sub>3,-,-,9</sub> |  | 2.8<br><sub>3,-,-,5</sub> |  | 0.0<br><sub>0,-,-,0</sub> |  | 0.8 | 0.6 | 1.3 | 13.9 |
| Jordan Goodwin (PHX) | 98% | 19.0<br><sub>22,20,17,25</sub> | 7.1<br><sub>3,9,12,11</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,2,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,4,2,5</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.1<br><sub>1,1,4,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.2 | 0.8 | 12.8 |
| Khaman Maluach (PHX) | 96% | 17.1<br><sub>17,28,26,17</sub> | 6.1<br><sub>2,9,12,9</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>6,9,7,6</sub> | 7.5<br><sub>o 41% · u 59%</sub> | 0.6<br><sub>1,3,1,0</sub> |  | 0.2<br><sub>0,1,0,0</sub> |  | 0.4 | 0.9 | 1.1 | 12.0 |
| Luke Kennard (PHX) | 98% | 14.6<br><sub>-,18,16,12</sub> | 5.3<br><sub>-,11,9,9</sub> |  | 1.8<br><sub>-,4,1,1</sub> |  | 1.4<br><sub>-,1,2,2</sub> |  | 0.6<br><sub>-,3,3,1</sub> |  | 0.6 | 0.1 | 0.7 | 8.5 |
| Ryan Dunn (PHX) | 96% | 11.7<br><sub>14,13,14,11</sub> | 3.6<br><sub>3,5,6,5</sub> |  | 2.5<br><sub>2,5,2,3</sub> |  | 0.8<br><sub>0,0,1,1</sub> |  | 0.3<br><sub>0,1,1,1</sub> |  | 0.6 | 0.3 | 0.5 | 7.0 |
| Pat Spencer (PHX) | 64% | 7.6<br><sub>7,-,-,-</sub> | 2.7<br><sub>3,-,-,-</sub> |  | 0.9<br><sub>3,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.0 |
| Rasheer Fleming (PHX) | 58% | 6.8<br><sub>12,-,3,-</sub> | 2.6<br><sub>1,-,0,-</sub> |  | 1.3<br><sub>2,-,1,-</sub> |  | 0.3<br><sub>0,-,0,-</sub> |  | 0.2<br><sub>0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.1 |
| Duop Reath (PHX) | 64% | 6.6<br><sub>9,3,7,-</sub> | 2.5<br><sub>5,0,5,-</sub> |  | 1.3<br><sub>1,0,3,-</sub> |  | 0.3<br><sub>0,0,0,-</sub> |  | 0.2<br><sub>1,0,1,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |
| Jamaree Bouyea (PHX) | 58% | 6.3<br><sub>7,-,3,-</sub> | 2.6<br><sub>3,-,2,-</sub> |  | 0.9<br><sub>2,-,0,-</sub> |  | 0.9<br><sub>2,-,1,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Koa Peat (PHX) | 52% | 6.0<br><sub>7,-,3,-</sub> | 2.4<br><sub>4,-,0,-</sub> |  | 1.4<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>0,-,0,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.1 |

</details>


### TOR @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC), Kawhi Leonard (TOR)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.0–109.1 | TOR 58% | 1.72 / 2.39 | LAC +3.5 | 220.5 | LAC +5.5 covers 57%; o220.5 51% |
| Expected (weighted by chance each plays) | 112.4–109.8 | TOR 57% | 1.75 / 2.33 | LAC +2.5 | 222.5 | LAC +5.5 covers 58%; o220.5 54% |
| if Derrick Jones Jr. plays | 111.9–110.7 | TOR 53% | 1.88 / 2.14 | LAC +1.5 | 222.5 | LAC +5.5 covers 62%; o220.5 54% |
| if Jakob Poeltl plays | 113.1–109.4 | TOR 60% | 1.66 / 2.50 | LAC +3.5 | 222.5 | LAC +5.5 covers 55%; o220.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick Jones Jr. (LAC) | Day-To-Day | 70% | 27.4 | 10.9 | 4.0 | 1.3 | 1.2 | 1.0 | 0.8 | 1.0 | 16.1 | full tables below |
| Jakob Poeltl (TOR) | Day-To-Day | 70% | 21.4 | 8.5 | 6.1 | 1.5 | 0.0 | 0.9 | 0.7 | 1.2 | 16.1 | full tables below |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 36.5<br><sub>26,37,28,31,39</sub> | 23.1<br><sub>23,28,0,28,41</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>6,14,3,6,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 7.0<br><sub>5,5,3,4,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.9<br><sub>1,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.8 | 1.2 | 3.3 | 37.4 |
| RJ Barrett | 98% | 35.3<br><sub>26,34,32,32,34</sub> | 21.9<br><sub>20,23,20,25,9</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>4,9,2,9,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>3,4,2,6,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.4 | 2.6 | 32.1 |
| Immanuel Quickley | 98% | 33.3<br><sub>28,29,28,29,37</sub> | 18.1<br><sub>23,12,19,16,17</sub> | 18.5 · –<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>4,1,3,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>7,6,2,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.7<br><sub>4,0,3,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.1 | 1.8 | 28.4 |
| Ja'Kobe Walter | 98% | 31.5<br><sub>23,24,31,28,32</sub> | 12.0<br><sub>10,7,22,14,9</sub> |  | 3.8<br><sub>3,4,4,5,3</sub> |  | 2.0<br><sub>4,2,2,2,1</sub> |  | 2.2<br><sub>1,2,5,3,3</sub> |  | 1.8 | 0.3 | 1.1 | 17.8 |
| Jamal Shead | 98% | 26.5<br><sub>16,24,21,23,23</sub> | 8.3<br><sub>2,5,4,13,2</sub> |  | 1.9<br><sub>2,2,1,4,1</sub> |  | 5.2<br><sub>5,5,0,7,8</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 1.2 | 0.2 | 2.0 | 15.4 |
| Collin Murray-Boyles | 98% | 24.8<br><sub>20,18,19,15,23</sub> | 10.7<br><sub>6,8,3,10,15</sub> |  | 6.0<br><sub>8,3,7,2,5</sub> |  | 2.0<br><sub>3,0,2,1,1</sub> |  | 0.3<br><sub>0,0,0,2,1</sub> |  | 1.1 | 0.9 | 1.4 | 18.7 |
| Jamison Battle | 96% | 18.5<br><sub>11,12,13,20,19</sub> | 6.5<br><sub>8,5,4,7,2</sub> |  | 2.6<br><sub>5,0,1,0,0</sub> |  | 0.9<br><sub>0,0,2,1,0</sub> |  | 0.9<br><sub>2,1,1,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 9.9 |
| Malachi Smith | 26% | 16.5 | 5.5 |  | 2.5 |  | 2.0 |  | 0.6 |  | 0.7 | 0.2 | 0.7 | 10.0 |
| Allen Graves | 96% | 15.7<br><sub>19,6,20,18,9</sub> | 4.9<br><sub>5,2,11,3,7</sub> |  | 3.2<br><sub>5,2,6,1,4</sub> |  | 0.8<br><sub>0,0,4,0,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.5 | 0.8 | 8.9 |
| Kyle Anderson | 58% | 11.5<br><sub>5,-,11,5,-</sub> | 3.4<br><sub>0,-,0,0,-</sub> |  | 2.2<br><sub>1,-,2,0,-</sub> |  | 1.7<br><sub>2,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.6 | 0.3 | 0.7 | 7.2 |
| Trayce Jackson-Davis | 91% | 8.9<br><sub>10,1,6,20,1</sub> | 3.4<br><sub>9,0,3,6,0</sub> |  | 2.7<br><sub>1,0,1,11,0</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 6.8 |
| Alijah Martin | 67% | 7.2<br><sub>5,1,7,5,-</sub> | 2.8<br><sub>3,0,2,5,-</sub> |  | 1.1<br><sub>0,0,2,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.2<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.6 | 4.5 |
| Jaden Bradley | 67% | 7.1<br><sub>5,1,5,5,-</sub> | 2.2<br><sub>0,0,6,0,-</sub> |  | 1.1<br><sub>0,0,1,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.2 | 0.5 | 3.9 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.6<br><sub>32,37,36,26,31</sub> | 22.3<br><sub>30,26,16,14,24</sub> |  | 2.5<br><sub>1,0,4,1,2</sub> |  | 6.6<br><sub>4,6,11,5,5</sub> |  | 2.8<br><sub>3,4,2,1,4</sub> |  | 1.1 | 0.2 | 3.9 | 31.4 |
| Rui Hachimura | 98% | 32.5<br><sub>32,33,29,-,26</sub> | 15.8<br><sub>10,16,5,-,12</sub> | 17.5 · –<br><sub>o 45% · u 55%</sub> | 4.7<br><sub>8,6,4,-,5</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>2,1,0,-,0</sub> |  | 2.0<br><sub>2,3,1,-,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 1.6 | 21.7 |
| Kris Dunn | 98% | 30.1<br><sub>27,34,33,27,31</sub> | 7.9<br><sub>7,7,15,5,5</sub> |  | 4.0<br><sub>5,5,4,3,5</sub> |  | 4.2<br><sub>7,5,6,3,7</sub> |  | 0.9<br><sub>2,1,1,1,0</sub> |  | 1.9 | 0.3 | 1.8 | 16.1 |
| Keaton Wagler | 96% | 26.8<br><sub>29,24,26,28,25</sub> | 13.8<br><sub>15,13,11,21,12</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>5,3,5,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.2<br><sub>5,3,4,2,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>3,2,1,3,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.3 | 2.4 | 21.0 |
| Brook Lopez | 98% | 24.0<br><sub>27,20,23,22,21</sub> | 11.4<br><sub>17,22,15,2,13</sub> |  | 4.5<br><sub>11,4,1,3,6</sub> |  | 1.4<br><sub>1,0,2,3,0</sub> |  | 1.4<br><sub>1,2,3,0,1</sub> |  | 0.6 | 1.2 | 1.1 | 17.3 |
| Isaiah Jackson | 97% | 23.1<br><sub>15,28,24,19,22</sub> | 9.8<br><sub>13,6,10,4,10</sub> |  | 7.0<br><sub>5,6,6,5,7</sub> |  | 1.7<br><sub>0,3,4,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.3 | 1.7 | 18.4 |
| Kobe Sanders | 96% | 22.5<br><sub>19,19,20,27,24</sub> | 9.3<br><sub>2,5,12,9,7</sub> |  | 2.6<br><sub>0,3,4,4,4</sub> |  | 1.9<br><sub>3,5,2,0,2</sub> |  | 1.2<br><sub>0,1,2,1,1</sub> |  | 1.0 | 0.2 | 1.3 | 13.7 |
| Gradey Dick | 91% | 15.7<br><sub>19,12,18,19,12</sub> | 6.6<br><sub>12,6,6,5,3</sub> |  | 2.3<br><sub>4,4,3,5,0</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>1,0,2,1,1</sub> |  | 0.5 | 0.1 | 0.9 | 9.7 |
| Baba Miller | 86% | 12.4<br><sub>9,-,2,17,5</sub> | 5.3<br><sub>4,-,0,4,0</sub> |  | 1.9<br><sub>3,-,1,7,1</sub> |  | 1.1<br><sub>1,-,0,1,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 8.3 |
| Cam Christie | 64% | 11.0<br><sub>2,-,-,14,5</sub> | 3.7<br><sub>0,-,-,2,2</sub> |  | 1.6<br><sub>0,-,-,0,1</sub> |  | 0.7<br><sub>0,-,-,0,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 6.0 |
| Jalen Pickett | 52% | 8.5<br><sub>2,-,-,8,-</sub> | 2.9<br><sub>3,-,-,4,-</sub> |  | 1.1<br><sub>0,-,-,1,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.9 |
| Nick Martinelli | 64% | 8.3<br><sub>2,-,-,6,5</sub> | 3.2<br><sub>0,-,-,2,3</sub> |  | 2.2<br><sub>1,-,-,3,0</sub> |  | 0.6<br><sub>1,-,-,1,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.7 | 6.1 |
| Blake Wesley | 86% | 8.2<br><sub>-,-,-,-,5</sub> | 3.1<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,4</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.7 | 5.1 |

</details>

<details><summary>if Jakob Poeltl plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland (LAC) | 98% | 32.7<br><sub>32,37,36,26,31</sub> | 22.4<br><sub>30,26,16,14,24</sub> |  | 2.5<br><sub>1,0,4,1,2</sub> |  | 6.5<br><sub>4,6,11,5,5</sub> |  | 2.8<br><sub>3,4,2,1,4</sub> |  | 1.2 | 0.2 | 3.9 | 31.5 |
| Rui Hachimura (LAC) | 98% | 32.5<br><sub>32,33,29,-,26</sub> | 15.7<br><sub>10,16,5,-,12</sub> | 17.5 · –<br><sub>o 45% · u 55%</sub> | 4.7<br><sub>8,6,4,-,5</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>2,1,0,-,0</sub> |  | 1.9<br><sub>2,3,1,-,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.4 | 1.6 | 21.7 |
| Kris Dunn (LAC) | 98% | 30.0<br><sub>27,34,33,27,31</sub> | 7.9<br><sub>7,7,15,5,5</sub> |  | 3.9<br><sub>5,5,4,3,5</sub> |  | 4.2<br><sub>7,5,6,3,7</sub> |  | 0.9<br><sub>2,1,1,1,0</sub> |  | 1.9 | 0.3 | 1.8 | 16.0 |
| Keaton Wagler (LAC) | 96% | 26.8<br><sub>29,24,26,28,25</sub> | 13.7<br><sub>15,13,11,21,12</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>5,3,5,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.3<br><sub>5,3,4,2,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>3,2,1,3,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 2.4 | 21.0 |
| Brook Lopez (LAC) | 98% | 24.0<br><sub>27,20,23,22,21</sub> | 11.5<br><sub>17,22,15,2,13</sub> |  | 4.5<br><sub>11,4,1,3,6</sub> |  | 1.4<br><sub>1,0,2,3,0</sub> |  | 1.4<br><sub>1,2,3,0,1</sub> |  | 0.6 | 1.2 | 1.1 | 17.4 |
| Isaiah Jackson (LAC) | 97% | 23.1<br><sub>15,28,24,19,22</sub> | 9.8<br><sub>13,6,10,4,10</sub> |  | 7.0<br><sub>5,6,6,5,7</sub> |  | 1.7<br><sub>0,3,4,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.3 | 1.7 | 18.4 |
| Kobe Sanders (LAC) | 96% | 22.4<br><sub>19,19,20,27,24</sub> | 9.3<br><sub>2,5,12,9,7</sub> |  | 2.6<br><sub>0,3,4,4,4</sub> |  | 1.9<br><sub>3,5,2,0,2</sub> |  | 1.2<br><sub>0,1,2,1,1</sub> |  | 0.9 | 0.2 | 1.3 | 13.7 |
| Gradey Dick (LAC) | 91% | 15.7<br><sub>19,12,18,19,12</sub> | 6.6<br><sub>12,6,6,5,3</sub> |  | 2.3<br><sub>4,4,3,5,0</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>1,0,2,1,1</sub> |  | 0.5 | 0.1 | 0.9 | 9.6 |
| Baba Miller (LAC) | 86% | 12.3<br><sub>9,-,2,17,5</sub> | 5.2<br><sub>4,-,0,4,0</sub> |  | 1.9<br><sub>3,-,1,7,1</sub> |  | 1.1<br><sub>1,-,0,1,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 8.2 |
| Cam Christie (LAC) | 64% | 10.9<br><sub>2,-,-,14,5</sub> | 3.7<br><sub>0,-,-,2,2</sub> |  | 1.6<br><sub>0,-,-,0,1</sub> |  | 0.7<br><sub>0,-,-,0,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 6.0 |
| Jalen Pickett (LAC) | 52% | 8.5<br><sub>2,-,-,8,-</sub> | 2.9<br><sub>3,-,-,4,-</sub> |  | 1.1<br><sub>0,-,-,1,-</sub> |  | 1.0<br><sub>0,-,-,1,-</sub> |  | 0.3<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Nick Martinelli (LAC) | 64% | 8.3<br><sub>2,-,-,6,5</sub> | 3.2<br><sub>0,-,-,2,3</sub> |  | 2.3<br><sub>1,-,-,3,0</sub> |  | 0.7<br><sub>1,-,-,1,0</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.7 | 6.1 |
| Blake Wesley (LAC) | 86% | 8.2<br><sub>-,-,-,-,5</sub> | 3.1<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,4</sub> |  | 1.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.1 | 0.7 | 5.1 |
| Scottie Barnes (TOR) | 98% | 35.4<br><sub>26,37,28,31,39</sub> | 22.2<br><sub>23,28,0,28,41</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 6.9<br><sub>6,14,3,6,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 6.9<br><sub>5,5,3,4,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.9<br><sub>1,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.8 | 1.2 | 3.3 | 36.0 |
| RJ Barrett (TOR) | 98% | 34.2<br><sub>26,34,32,32,34</sub> | 21.1<br><sub>20,23,20,25,9</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 5.8<br><sub>4,9,2,9,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>3,4,2,6,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.5 | 30.9 |
| Immanuel Quickley (TOR) | 98% | 31.9<br><sub>28,29,28,29,37</sub> | 17.4<br><sub>23,12,19,16,17</sub> | 18.5 · –<br><sub>o 45% · u 55%</sub> | 3.7<br><sub>4,1,3,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>7,6,2,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>4,0,3,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.1 | 1.8 | 27.2 |
| Ja'Kobe Walter (TOR) | 98% | 29.4<br><sub>23,24,31,28,32</sub> | 11.3<br><sub>10,7,22,14,9</sub> |  | 3.4<br><sub>3,4,4,5,3</sub> |  | 1.9<br><sub>4,2,2,2,1</sub> |  | 2.0<br><sub>1,2,5,3,3</sub> |  | 1.6 | 0.3 | 1.0 | 16.6 |
| Jamal Shead (TOR) | 98% | 23.8<br><sub>16,24,21,23,23</sub> | 7.4<br><sub>2,5,4,13,2</sub> |  | 1.8<br><sub>2,2,1,4,1</sub> |  | 4.9<br><sub>5,5,0,7,8</sub> |  | 0.8<br><sub>0,0,0,1,0</sub> |  | 1.1 | 0.2 | 1.8 | 14.0 |
| Collin Murray-Boyles (TOR) | 98% | 22.6<br><sub>20,18,19,15,23</sub> | 9.8<br><sub>6,8,3,10,15</sub> |  | 5.5<br><sub>8,3,7,2,5</sub> |  | 1.9<br><sub>3,0,2,1,1</sub> |  | 0.3<br><sub>0,0,0,2,1</sub> |  | 1.0 | 0.8 | 1.3 | 17.1 |
| Jakob Poeltl (TOR) | 100% | 21.4<br><sub>22,27,19,10,23</sub> | 8.5<br><sub>3,6,0,2,12</sub> |  | 6.1<br><sub>6,9,1,2,11</sub> |  | 1.5<br><sub>0,2,0,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.2 | 16.1 |
| Jamison Battle (TOR) | 96% | 16.3<br><sub>11,12,13,20,19</sub> | 5.8<br><sub>8,5,4,7,2</sub> |  | 2.2<br><sub>5,0,1,0,0</sub> |  | 0.8<br><sub>0,0,2,1,0</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 0.4 | 0.1 | 0.5 | 8.9 |
| Malachi Smith (TOR) | 26% | 13.3 | 4.4 |  | 1.9 |  | 1.6 |  | 0.4 |  | 0.5 | 0.2 | 0.6 | 8.0 |
| Allen Graves (TOR) | 96% | 13.1<br><sub>19,6,20,18,9</sub> | 4.2<br><sub>5,2,11,3,7</sub> |  | 2.7<br><sub>5,2,6,1,4</sub> |  | 0.6<br><sub>0,0,4,0,0</sub> |  | 0.3<br><sub>0,0,1,0,1</sub> |  | 0.4 | 0.5 | 0.7 | 7.6 |
| Kyle Anderson (TOR) | 58% | 8.6<br><sub>5,-,11,5,-</sub> | 2.5<br><sub>0,-,0,0,-</sub> |  | 1.6<br><sub>1,-,2,0,-</sub> |  | 1.3<br><sub>2,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.5 | 5.5 |
| Trayce Jackson-Davis (TOR) | 91% | 7.8<br><sub>10,1,6,20,1</sub> | 3.2<br><sub>9,0,3,6,0</sub> |  | 2.3<br><sub>1,0,1,11,0</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.4 | 6.2 |
| Jaden Bradley (TOR) | 67% | 5.8<br><sub>5,1,5,5,-</sub> | 2.1<br><sub>0,0,6,0,-</sub> |  | 0.9<br><sub>0,0,1,1,-</sub> |  | 0.5<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.4 | 3.5 |
| Alijah Martin (TOR) | 67% | 5.8<br><sub>5,1,7,5,-</sub> | 2.3<br><sub>3,0,2,5,-</sub> |  | 0.9<br><sub>0,0,2,1,-</sub> |  | 0.5<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.5 | 3.6 |

</details>

<details><summary>if Derrick Jones Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland (LAC) | 98% | 30.3<br><sub>32,37,36,26,31</sub> | 20.8<br><sub>30,26,16,14,24</sub> |  | 2.4<br><sub>1,0,4,1,2</sub> |  | 6.1<br><sub>4,6,11,5,5</sub> |  | 2.5<br><sub>3,4,2,1,4</sub> |  | 1.1 | 0.2 | 3.6 | 29.2 |
| Rui Hachimura (LAC) | 98% | 29.3<br><sub>32,33,29,-,26</sub> | 14.1<br><sub>10,16,5,-,12</sub> | 17.5 · –<br><sub>o 45% · u 55%</sub> | 4.3<br><sub>8,6,4,-,5</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>2,1,0,-,0</sub> |  | 1.7<br><sub>2,3,1,-,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.3 | 1.5 | 19.6 |
| Derrick Jones Jr. (LAC) | 100% | 27.4<br><sub>26,35,30,28,26</sub> | 10.9<br><sub>8,16,11,15,10</sub> |  | 4.0<br><sub>6,4,6,5,1</sub> |  | 1.3<br><sub>5,1,1,0,1</sub> |  | 1.2<br><sub>1,3,3,3,2</sub> |  | 1.0 | 0.8 | 1.0 | 16.1 |
| Kris Dunn (LAC) | 98% | 27.3<br><sub>27,34,33,27,31</sub> | 7.5<br><sub>7,7,15,5,5</sub> |  | 3.6<br><sub>5,5,4,3,5</sub> |  | 3.9<br><sub>7,5,6,3,7</sub> |  | 0.8<br><sub>2,1,1,1,0</sub> |  | 1.7 | 0.3 | 1.6 | 15.0 |
| Keaton Wagler (LAC) | 96% | 24.9<br><sub>29,24,26,28,25</sub> | 12.8<br><sub>15,13,11,21,12</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>5,3,5,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>5,3,4,2,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.4<br><sub>3,2,1,3,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.3 | 2.3 | 19.6 |
| Brook Lopez (LAC) | 98% | 21.9<br><sub>27,20,23,22,21</sub> | 10.6<br><sub>17,22,15,2,13</sub> |  | 4.1<br><sub>11,4,1,3,6</sub> |  | 1.3<br><sub>1,0,2,3,0</sub> |  | 1.2<br><sub>1,2,3,0,1</sub> |  | 0.6 | 1.1 | 1.1 | 15.9 |
| Kobe Sanders (LAC) | 96% | 20.5<br><sub>19,19,20,27,24</sub> | 8.6<br><sub>2,5,12,9,7</sub> |  | 2.4<br><sub>0,3,4,4,4</sub> |  | 1.7<br><sub>3,5,2,0,2</sub> |  | 1.1<br><sub>0,1,2,1,1</sub> |  | 0.9 | 0.2 | 1.3 | 12.7 |
| Isaiah Jackson (LAC) | 97% | 20.0<br><sub>15,28,24,19,22</sub> | 8.7<br><sub>13,6,10,4,10</sub> |  | 6.2<br><sub>5,6,6,5,7</sub> |  | 1.5<br><sub>0,3,4,1,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.2 | 1.6 | 16.4 |
| Gradey Dick (LAC) | 91% | 13.5<br><sub>19,12,18,19,12</sub> | 5.9<br><sub>12,6,6,5,3</sub> |  | 2.0<br><sub>4,4,3,5,0</sub> |  | 0.7<br><sub>0,0,0,0,1</sub> |  | 0.6<br><sub>1,0,2,1,1</sub> |  | 0.5 | 0.1 | 0.8 | 8.6 |
| Baba Miller (LAC) | 86% | 9.6<br><sub>9,-,2,17,5</sub> | 4.2<br><sub>4,-,0,4,0</sub> |  | 1.5<br><sub>3,-,1,7,1</sub> |  | 0.9<br><sub>1,-,0,1,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.1 | 0.6 | 6.6 |
| Cam Christie (LAC) | 64% | 7.8<br><sub>2,-,-,14,5</sub> | 2.9<br><sub>0,-,-,2,2</sub> |  | 1.2<br><sub>0,-,-,0,1</sub> |  | 0.6<br><sub>0,-,-,0,1</sub> |  | 0.1<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Jalen Pickett (LAC) | 52% | 7.1<br><sub>2,-,-,8,-</sub> | 2.6<br><sub>3,-,-,4,-</sub> |  | 0.9<br><sub>0,-,-,1,-</sub> |  | 0.9<br><sub>0,-,-,1,-</sub> |  | 0.2<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.4 |
| Nick Martinelli (LAC) | 64% | 6.9<br><sub>2,-,-,6,5</sub> | 2.9<br><sub>0,-,-,2,3</sub> |  | 1.9<br><sub>1,-,-,3,0</sub> |  | 0.6<br><sub>1,-,-,1,0</sub> |  | 0.0<br><sub>0,-,-,0,0</sub> |  | 0.2 | 0.2 | 0.6 | 5.4 |
| Blake Wesley (LAC) | 86% | 6.5<br><sub>-,-,-,-,5</sub> | 2.7<br><sub>-,-,-,-,0</sub> |  | 0.8<br><sub>-,-,-,-,4</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 4.4 |
| Scottie Barnes (TOR) | 98% | 36.5<br><sub>26,37,28,31,39</sub> | 23.2<br><sub>23,28,0,28,41</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>6,14,3,6,5</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 7.0<br><sub>5,5,3,4,5</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.9<br><sub>1,1,0,0,1</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 1.8 | 1.2 | 3.3 | 37.5 |
| RJ Barrett (TOR) | 98% | 35.3<br><sub>26,34,32,32,34</sub> | 21.8<br><sub>20,23,20,25,9</sub> | 20.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>4,9,2,9,3</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 4.1<br><sub>3,4,2,6,5</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>0,1,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.4 | 2.6 | 32.1 |
| Immanuel Quickley (TOR) | 98% | 33.2<br><sub>28,29,28,29,37</sub> | 18.0<br><sub>23,12,19,16,17</sub> | 18.5 · –<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>4,1,3,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 6.3<br><sub>7,6,2,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>4,0,3,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4 | 0.1 | 1.8 | 28.3 |
| Ja'Kobe Walter (TOR) | 98% | 31.6<br><sub>23,24,31,28,32</sub> | 12.1<br><sub>10,7,22,14,9</sub> |  | 3.8<br><sub>3,4,4,5,3</sub> |  | 2.0<br><sub>4,2,2,2,1</sub> |  | 2.2<br><sub>1,2,5,3,3</sub> |  | 1.8 | 0.3 | 1.1 | 17.9 |
| Jamal Shead (TOR) | 98% | 26.4<br><sub>16,24,21,23,23</sub> | 8.2<br><sub>2,5,4,13,2</sub> |  | 1.9<br><sub>2,2,1,4,1</sub> |  | 5.2<br><sub>5,5,0,7,8</sub> |  | 1.0<br><sub>0,0,0,1,0</sub> |  | 1.2 | 0.2 | 2.0 | 15.4 |
| Collin Murray-Boyles (TOR) | 98% | 24.7<br><sub>20,18,19,15,23</sub> | 10.6<br><sub>6,8,3,10,15</sub> |  | 6.0<br><sub>8,3,7,2,5</sub> |  | 2.0<br><sub>3,0,2,1,1</sub> |  | 0.3<br><sub>0,0,0,2,1</sub> |  | 1.1 | 0.9 | 1.4 | 18.7 |
| Jamison Battle (TOR) | 96% | 18.6<br><sub>11,12,13,20,19</sub> | 6.5<br><sub>8,5,4,7,2</sub> |  | 2.6<br><sub>5,0,1,0,0</sub> |  | 0.9<br><sub>0,0,2,1,0</sub> |  | 0.9<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 9.9 |
| Malachi Smith (TOR) | 26% | 16.4 | 5.5 |  | 2.5 |  | 2.0 |  | 0.6 |  | 0.6 | 0.2 | 0.7 | 10.0 |
| Allen Graves (TOR) | 96% | 15.6<br><sub>19,6,20,18,9</sub> | 4.9<br><sub>5,2,11,3,7</sub> |  | 3.2<br><sub>5,2,6,1,4</sub> |  | 0.7<br><sub>0,0,4,0,0</sub> |  | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.5 | 0.8 | 8.9 |
| Kyle Anderson (TOR) | 58% | 11.6<br><sub>5,-,11,5,-</sub> | 3.4<br><sub>0,-,0,0,-</sub> |  | 2.2<br><sub>1,-,2,0,-</sub> |  | 1.8<br><sub>2,-,0,1,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.6 | 0.3 | 0.7 | 7.3 |
| Trayce Jackson-Davis (TOR) | 91% | 8.9<br><sub>10,1,6,20,1</sub> | 3.4<br><sub>9,0,3,6,0</sub> |  | 2.7<br><sub>1,0,1,11,0</sub> |  | 0.7<br><sub>0,0,1,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 6.8 |
| Alijah Martin (TOR) | 67% | 7.2<br><sub>5,1,7,5,-</sub> | 2.8<br><sub>3,0,2,5,-</sub> |  | 1.1<br><sub>0,0,2,1,-</sub> |  | 0.6<br><sub>0,0,1,1,-</sub> |  | 0.2<br><sub>0,0,0,1,-</sub> |  | 0.3 | 0.1 | 0.6 | 4.5 |
| Jaden Bradley (TOR) | 67% | 6.9<br><sub>5,1,5,5,-</sub> | 2.2<br><sub>0,0,6,0,-</sub> |  | 1.1<br><sub>0,0,1,1,-</sub> |  | 0.5<br><sub>0,0,1,1,-</sub> |  | 0.1<br><sub>0,0,0,0,-</sub> |  | 0.5 | 0.2 | 0.5 | 3.8 |

</details>


### MIA @ LAL
Out: Ziaire Williams (LAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Bam Adebayo 3PM over 1.5 (2+) | MIA @ LAL | draftkings | 2.52 | 2.50 | 2.04 | 49.0% | 37.1% | 40.1% | +1.0% | +23.6% | 0.2% |
| Davion Mitchell REB over 2.5 (3+) | MIA @ LAL | draftkings | 2.27 | 2.26 | 1.87 | 53.6% | 41.3% | 44.3% | +0.7% | +21.6% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.9–121.4 | MIA 35% | 2.84 / 1.54 | LAL -5.5 | 237.5 | LAL -2.5 covers 59%; o237.5 49% |
| Expected (weighted by chance each plays) | 116.2–121.3 | MIA 37% | 2.73 / 1.58 | LAL -5.5 | 237.5 | LAL -2.5 covers 58%; o237.5 49% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tim Hardaway Jr. (MIA) | Questionable | 55% | 15.8 | 6.5 | 1.7 | 0.8 | 0.8 | 0.4 | 0.1 | 0.5 | 9.1 | small |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 35.0<br><sub>33,37,33,34,35</sub> | 13.3<br><sub>18,22,21,10,15</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>2,1,0,1,6</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 7.4<br><sub>5,10,2,10,11</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 1.7<br><sub>3,3,2,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.2 | 2.3 | 23.6 |
| Bam Adebayo | 98% | 34.7<br><sub>23,39,30,33,33</sub> | 19.0<br><sub>4,20,8,24,27</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 9.7<br><sub>6,8,8,9,9</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 3.5<br><sub>3,4,3,3,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.7 | 0.6 | 2.0 | 32.3 |
| Giannis Antetokounmpo | 98% | 32.9<br><sub>33,25,39,31,31</sub> | 27.7<br><sub>36,14,29,24,31</sub> | 31.5 · –<br><sub>o 45% · u 55%</sub> | 11.4<br><sub>12,6,14,18,18</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 6.1<br><sub>5,3,11,3,10</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.6<br><sub>1,0,2,0,1</sub> |  | 1.1 | 0.7 | 3.3 | 45.1 |
| Pelle Larsson | 98% | 31.4<br><sub>29,36,34,31,24</sub> | 12.4<br><sub>7,15,12,17,18</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>2,7,0,6,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>1,4,4,8,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>1,1,1,2,1</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.0 | 0.2 | 1.9 | 20.0 |
| Andrew Wiggins | 98% | 30.2<br><sub>26,18,34,29,30</sub> | 13.3<br><sub>8,4,12,18,12</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>8,1,3,2,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.2<br><sub>2,1,1,2,1</sub> |  | 1.8<br><sub>1,0,0,4,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.8 | 1.4 | 19.7 |
| Bobby Portis | 98% | 23.0<br><sub>21,27,24,23,17</sub> | 10.8<br><sub>11,13,10,11,8</sub> | 11.5 · –<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>8,8,12,9,3</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>2,0,2,4,1</sub> |  | 1.5<br><sub>3,2,3,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.3 | 1.0 | 18.5 |
| Klay Thompson | 98% | 22.7<br><sub>24,27,15,17,26</sub> | 10.8<br><sub>6,14,6,3,25</sub> | 8.5 · –<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>2,3,1,1,0</sub> |  | 1.4<br><sub>2,0,1,2,3</sub> |  | 2.0<br><sub>2,4,2,1,7</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.3 | 1.0 | 14.3 |
| Nikola Jovic | 72% | 13.4<br><sub>13,6,-,7,16</sub> | 4.4<br><sub>5,0,-,5,0</sub> |  | 2.6<br><sub>4,2,-,3,4</sub> |  | 1.2<br><sub>1,0,-,0,3</sub> |  | 0.5<br><sub>0,0,-,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 8.3 |
| Dru Smith | 71% | 12.3<br><sub>6,-,15,14,4</sub> | 3.8<br><sub>3,-,6,3,0</sub> |  | 1.6<br><sub>0,-,2,0,0</sub> |  | 1.8<br><sub>1,-,1,3,1</sub> |  | 0.3<br><sub>1,-,2,0,0</sub> |  | 1.0 | 0.2 | 0.7 | 7.2 |
| Keshad Johnson | 23% | 9.7 | 4.3 |  | 2.1 |  | 0.5 |  | 0.3 |  | 0.5 | 0.3 | 0.5 | 6.9 |
| Simone Fontecchio | 52% | 8.5<br><sub>3,-,-,-,2</sub> | 4.0<br><sub>0,-,-,-,3</sub> |  | 1.6<br><sub>1,-,-,-,1</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 6.3 |
| Ryan Conwell | 63% | 7.8<br><sub>3,4,-,-,7</sub> | 2.5<br><sub>2,3,-,-,4</sub> |  | 1.5<br><sub>0,1,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,1,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |
| Myron Gardner | 52% | 7.6<br><sub>3,-,-,-,2</sub> | 2.7<br><sub>0,-,-,-,0</sub> |  | 2.1<br><sub>0,-,-,-,1</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.6 |
| Nick Richards | 58% | 7.2<br><sub>3,-,-,-,2</sub> | 2.5<br><sub>3,-,-,-,0</sub> |  | 2.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>1,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.4 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.8<br><sub>37,38,37,-,37</sub> | 35.3<br><sub>23,52,41,-,37</sub> | 33.5 · –<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>6,8,5,-,7</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 8.4<br><sub>7,10,9,-,5</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 4.6<br><sub>2,8,6,-,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7 | 0.6 | 4.2 | 51.2 |
| Austin Reaves | 98% | 36.0<br><sub>38,36,39,31,37</sub> | 22.1<br><sub>28,29,26,16,21</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.6<br><sub>2,1,4,6,4</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 5.8<br><sub>9,4,7,1,5</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>3,4,4,1,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.5 | 3.2 | 32.5 |
| Walker Kessler | 98% | 30.2<br><sub>35,28,33,26,31</sub> | 11.2<br><sub>22,2,13,11,10</sub> | 12.5 · –<br><sub>o 45% · u 55%</sub> | 10.8<br><sub>8,7,8,9,13</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>3,0,0,1,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.1 | 1.5 | 23.5 |
| Quentin Grimes | 98% | 26.7<br><sub>31,20,19,38,26</sub> | 10.2<br><sub>13,3,2,23,3</sub> |  | 3.5<br><sub>8,1,4,3,3</sub> |  | 2.4<br><sub>4,1,0,5,2</sub> |  | 1.2<br><sub>3,0,0,0,1</sub> |  | 0.9 | 0.3 | 1.1 | 16.1 |
| Matisse Thybulle | 96% | 24.2<br><sub>24,26,22,28,28</sub> | 8.0<br><sub>13,11,5,15,10</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>1,1,2,1,3</sub> |  | 1.3<br><sub>2,1,1,0,0</sub> |  | 1.3<br><sub>3,3,1,4,1</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.9 | 0.7 | 0.9 | 11.8 |
| Jake LaRavia | 93% | 24.2<br><sub>-,15,19,35,28</sub> | 6.6<br><sub>-,0,5,2,10</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>-,4,1,10,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>-,1,1,0,0</sub> |  | 0.7<br><sub>-,0,1,0,2</sub> |  | 1.3 | 0.6 | 1.1 | 11.9 |
| Sandro Mamukelashvili | 98% | 23.2<br><sub>24,21,24,30,20</sub> | 9.6<br><sub>7,9,17,13,4</sub> |  | 5.7<br><sub>5,3,4,8,7</sub> |  | 1.6<br><sub>2,0,2,3,0</sub> |  | 1.1<br><sub>1,1,3,0,0</sub> |  | 0.9 | 0.5 | 0.9 | 16.9 |
| Collin Sexton | 98% | 18.2<br><sub>16,20,14,21,16</sub> | 11.3<br><sub>5,13,9,21,0</sub> |  | 2.1<br><sub>1,2,1,4,2</sub> |  | 2.0<br><sub>2,1,4,2,1</sub> |  | 1.2<br><sub>1,1,0,4,0</sub> |  | 0.9 | 0.2 | 1.4 | 15.3 |
| Jarred Vanderbilt | 52% | 14.3<br><sub>-,-,-,21,13</sub> | 3.6<br><sub>-,-,-,0,0</sub> |  | 3.8<br><sub>-,-,-,7,3</sub> |  | 1.2<br><sub>-,-,-,2,3</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 0.6 | 8.6 |
| Lawson Lovering | 16% | 14.2 | 4.5 |  | 3.6 |  | 1.1 |  | 0.1 |  | 0.6 | 0.3 | 0.6 | 9.2 |
| Cameron Carr | 16% | 12.4 | 5.3 |  | 2.2 |  | 1.1 |  | 0.4 |  | 0.4 | 0.2 | 0.6 | 8.7 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| AK Okereke | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 52% | 7.8<br><sub>5,5,5,-,-</sub> | 1.8<br><sub>0,2,0,-,-</sub> |  | 2.8<br><sub>1,2,0,-,-</sub> |  | 0.6<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.2 |
| Jaden Hardy | 63% | 7.6<br><sub>-,-,-,9,1</sub> | 3.9<br><sub>-,-,-,2,0</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.6<br><sub>-,-,-,2,0</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Chris Manon | 58% | 5.7<br><sub>-,-,-,-,1</sub> | 1.8<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 3.3 |
| Bronny James | 48% | 5.6<br><sub>-,-,-,-,1</sub> | 2.0<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 2.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-02/`._
