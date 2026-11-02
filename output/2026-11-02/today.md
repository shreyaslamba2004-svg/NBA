# NBA model · Mon 02 Nov 2026 (US date)

Updated **Tue 03 Nov, 02:04 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-02/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

2 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| SAC @ DAL | player points | Precious Achiuwa projected 16.6 pts vs DraftKings line 11.5 | minutes 34 vs 29 this season; scoring 0.49/min vs 0.43 this season, 0.42 last season; teammates out: Murray, Raynaud (~54 min a game) |
| ATL @ IND | player points | CJ McCollum projected 21.9 pts vs DraftKings line 16.5 | minutes 31 vs 26 this season; new team (was WAS last season); scoring 0.70/min vs 0.55 this season, 0.63 last season; teammates out: Flemings, Gueye, Landale (~51 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama BLK over 4.5 (5+) | UTA @ SAS | draftkings | 3.72 | 3.51 | 2.59 | 38.6% | 25.1% | 28.5% | +5.9% | +43.4% | 0.5% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Davis BLK over 3.5 (4+) | WAS @ ORL | draftkings | 12.80 | 10.34 | 5.96 | 16.8% | 7.3% | 9.7% | +23.8% | +114.9% | 0.5% |
| Aday Mara REB over 11.5 (12+) | OKC @ CLE | draftkings | 15.40 | 12.89 | 7.80 | 12.8% | 6.1% | 7.8% | +19.5% | +97.5% | 0.3% |
| UTA to win | UTA @ SAS | neds | 10.00 | 8.41 | 7.14 | 14.0% | 11.9% | 11.9% | +18.9% | +40.2% | 0.5% |
| Zion Williamson AST over 5.5 (6+) | NOP @ MEM | draftkings | 13.40 | 11.39 | 7.05 | 14.2% | 7.0% | 8.8% | +17.6% | +90.0% | 0.4% |
| Darius Acuff Jr. REB over 5.5 (6+) | SAC @ DAL | draftkings | 6.10 | 5.29 | 3.38 | 29.6% | 15.3% | 18.9% | +15.2% | +80.6% | 0.8% |
| Darius Acuff Jr. REB over 7.5 (8+) | SAC @ DAL | draftkings | 18.00 | 15.65 | 10.03 | 10.0% | 5.2% | 6.4% | +14.9% | +79.4% | 0.2% |
| Aday Mara REB over 9.5 (10+) | OKC @ CLE | draftkings | 6.74 | 5.88 | 3.78 | 26.5% | 13.9% | 17.0% | +14.7% | +78.4% | 0.6% |
| Joan Beringer PRA over 24.5 (25+) | MIL @ MIN | draftkings | 9.10 | 8.03 | 5.26 | 19.0% | 10.3% | 12.4% | +13.3% | +73.0% | 0.4% |
| Victor Wembanyama PA over 49.5 (50+) | UTA @ SAS | draftkings | 25.00 | 22.12 | 14.53 | 6.9% | 3.7% | 4.5% | +13.1% | +72.1% | 0.1% |
| Victor Wembanyama PA over 44.5 (45+) | UTA @ SAS | draftkings | 13.60 | 12.05 | 7.95 | 12.6% | 6.9% | 8.3% | +12.8% | +71.0% | 0.2% |
| Victor Wembanyama BLK over 6.5 (7+) | UTA @ SAS | draftkings | 12.20 | 10.82 | 7.15 | 14.0% | 7.7% | 9.2% | +12.7% | +70.5% | 0.3% |
| Anthony Davis BLK over 4.5 (5+) | WAS @ ORL | draftkings | 24.00 | 21.32 | 14.15 | 7.1% | 3.9% | 4.7% | +12.5% | +69.7% | 0.1% |
| Kevin Durant AST over 7.5 (8+) | BOS @ HOU | draftkings | 15.80 | 14.04 | 9.33 | 10.7% | 5.9% | 7.1% | +12.4% | +69.4% | 0.2% |
| Aday Mara REB over 13.5 (14+) | OKC @ CLE | draftkings | 29.00 | 26.18 | 17.87 | 5.6% | 3.2% | 3.8% | +10.7% | +62.3% | 0.1% |
| Joan Beringer PTS over 14.5 (15+) | MIL @ MIN | draftkings | 8.30 | 7.51 | 5.13 | 19.5% | 11.3% | 13.3% | +10.5% | +61.7% | 0.4% |
| Joan Beringer PRA over 29.5 (30+) | MIL @ MIN | draftkings | 20.80 | 18.87 | 12.96 | 7.7% | 4.5% | 5.3% | +10.2% | +60.5% | 0.1% |
| Pascal Siakam PRA over 49.5 (50+) | ATL @ IND | draftkings | 12.40 | 11.25 | 7.73 | 12.9% | 7.5% | 8.9% | +10.2% | +60.5% | 0.2% |
| Pascal Siakam PRA over 54.5 (55+) | ATL @ IND | draftkings | 22.00 | 19.96 | 13.73 | 7.3% | 4.2% | 5.0% | +10.2% | +60.2% | 0.1% |
| Jrue Holiday AST over 7.5 (8+) | POR @ DEN | draftkings | 9.20 | 8.38 | 5.78 | 17.3% | 10.2% | 11.9% | +9.9% | +59.1% | 0.3% |
| Joan Beringer REB over 11.5 (12+) | MIL @ MIN | draftkings | 15.00 | 13.66 | 9.45 | 10.6% | 6.2% | 7.3% | +9.8% | +58.8% | 0.2% |
| Victor Wembanyama BLK over 5.5 (6+) | UTA @ SAS | draftkings | 6.59 | 6.01 | 4.15 | 24.1% | 14.2% | 16.7% | +9.8% | +58.6% | 0.4% |
| Tyrese Maxey STL over 3.5 (4+) | CHI @ PHI | draftkings | 13.00 | 11.90 | 8.32 | 12.0% | 7.2% | 8.4% | +9.1% | +56.2% | 0.2% |
| Precious Achiuwa PRA over 39.5 (40+) | SAC @ DAL | draftkings | 24.00 | 22.03 | 15.40 | 6.5% | 3.9% | 4.5% | +9.0% | +55.8% | 0.1% |
| Scottie Barnes AST over 9.5 (10+) | TOR @ LAC | draftkings | 9.70 | 8.91 | 6.26 | 16.0% | 9.6% | 11.2% | +8.9% | +55.1% | 0.2% |
| Jalen Brunson PTS over 39.5 (40+) | BKN @ NYK | draftkings | 14.40 | 13.25 | 9.30 | 10.8% | 6.5% | 7.5% | +8.8% | +54.8% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Keaton Wagler PRA under 23.5 | TOR @ LAC | draftkings | 1.94 | Derrick Jones Jr. | 72.9% | 80.5% | +8.0% |
| Keaton Wagler PR under 19.5 | TOR @ LAC | draftkings | 1.91 | Derrick Jones Jr. | 71.9% | 79.2% | +6.9% |
| Keaton Wagler PTS under 14.5 | TOR @ LAC | draftkings | 1.98 | Derrick Jones Jr. | 67.7% | 74.9% | +6.1% |
| Keaton Wagler RA under 8.5 | TOR @ LAC | draftkings | 1.92 | Derrick Jones Jr. | 71.1% | 76.1% | +5.9% |
| Precious Achiuwa PR over 24.5 (25+) | SAC @ DAL | draftkings | 3.40 | Zach LaVine | 51.9% | 40.2% | +5.6% |
| CJ McCollum PR over 24.5 (25+) | ATL @ IND | draftkings | 3.46 | Jalen Johnson | 48.5% | 35.7% | +5.3% |
| Keaton Wagler PA under 19.5 | TOR @ LAC | draftkings | 1.79 | Derrick Jones Jr. | 74.4% | 80.7% | +5.3% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ja'Kobe Walter REB over 1.5 (2+) | TOR @ LAC | draftkings | 2.56 | 2.07 | 1.20 | 83.5% | 36.5% | 48.3% | +23.5% | +113.8% | 2.0% |
| Joan Beringer PRA over 19.5 (20+) | MIL @ MIN | draftkings | 3.93 | 3.63 | 2.57 | 39.0% | 23.8% | 27.6% | +8.4% | +53.1% | 0.7% |
| Anthony Davis BLK over 1.5 (2+) | WAS @ ORL | draftkings | 2.49 | 2.32 | 1.66 | 60.1% | 37.5% | 43.2% | +7.5% | +49.7% | 1.3% |
| Zion Williamson AST over 3.5 (4+) | NOP @ MEM | draftkings | 3.46 | 3.23 | 2.34 | 42.6% | 27.0% | 30.9% | +7.0% | +47.6% | 0.7% |
| Aday Mara REB over 7.5 (8+) | OKC @ CLE | draftkings | 3.08 | 2.89 | 2.10 | 47.5% | 30.3% | 34.6% | +6.7% | +46.4% | 0.8% |
| Khaman Maluach REB under 6.5 | PHX @ GSW | draftkings | 2.07 | 1.95 | 1.44 | 69.3% | 45.1% | 51.2% | +6.0% | +43.5% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| OKC @ CLE | Tue 03 Nov 11:00 | 111.8–113.4 | OKC 45% | 2.21 / 1.83 | CLE -2.5 | 224.5 | CLE -3.5 covers 46%; o228.5 42% |
| DET @ CHA | Tue 03 Nov 11:30 | 108.6–105.8 | DET 57% | 1.74 / 2.35 | CHA +2.5 | 214.5 | CHA +4.5 covers 55%; o210.5 58% |
| ATL @ IND | Tue 03 Nov 11:30 | 117.3–116.5 | ATL 52% | 1.91 / 2.10 | IND +1.5 | 233.5 | IND +5.5 covers 63%; o232.5 53% |
| BKN @ NYK | Tue 03 Nov 11:30 | 102.9–116.8 | BKN 16% | 6.20 / 1.19 | NYK -13.5 | 219.5 | NYK -14.5 covers 48%; o219.5 51% |
| WAS @ ORL | Tue 03 Nov 11:30 | 111.8–116.4 | WAS 37% | 2.71 / 1.59 | ORL -4.5 | 227.5 | ORL -2.5 covers 57%; o225.5 55% |
| CHI @ PHI | Tue 03 Nov 11:30 | 113.6–120.3 | CHI 32% | 3.13 / 1.47 | PHI -6.5 | 233.5 | PHI -10.5 covers 39%; o238.5 40% |
| SAC @ DAL | Tue 03 Nov 12:00 | 114.2–123.6 | SAC 26% | 3.92 / 1.34 | DAL -9.5 | 237.5 | DAL -10.5 covers 47%; o232.5 61% |
| NOP @ MEM | Tue 03 Nov 12:00 | 118.6–122.1 | NOP 40% | 2.48 / 1.68 | MEM -3.5 | 240.5 | MEM -5.5 covers 45%; o233.5 64% |
| MIL @ MIN | Tue 03 Nov 12:00 | 108.1–117.3 | MIL 26% | 3.89 / 1.35 | MIN -9.5 | 225.5 | MIN -10.5 covers 47%; o233.5 33% |
| BOS @ HOU | Tue 03 Nov 12:30 | 108.8–109.2 | BOS 49% | 2.03 / 1.97 | HOU +0.5 | 217.5 | HOU -4.5 covers 39%; o218.5 48% |
| UTA @ SAS | Tue 03 Nov 12:30 | 109.9–125.3 | UTA 14% | 7.14 / 1.16 | SAS -15.5 | 234.5 | SAS -15.5 covers 50%; o229.5 62% |
| POR @ DEN | Tue 03 Nov 13:00 | 114.6–121.5 | POR 31% | 3.22 / 1.45 | DEN -6.5 | 236.5 | DEN -4.5 covers 57%; o230.5 62% |
| PHX @ GSW | Tue 03 Nov 14:00 | 113.7–112.4 | PHX 54% | 1.86 / 2.16 | GSW +1.5 | 225.5 | GSW -2.5 covers 40%; o228.5 45% |
| TOR @ LAC | Tue 03 Nov 14:00 | 112.3–109.4 | TOR 58% | 1.73 / 2.37 | LAC +3.5 | 221.5 | LAC +4.5 covers 54%; o221.5 50% |
| MIA @ LAL | Tue 03 Nov 14:00 | 117.9–121.4 | MIA 41% | 2.47 / 1.68 | LAL -3.5 | 238.5 | LAL -2.5 covers 54%; o237.5 53% |

### OKC @ CLE
Out: Jaylon Tyson (CLE), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aday Mara PR over 13.5 (14+) | OKC @ CLE | draftkings | 1.76 | 1.76 | 1.47 | 68.0% | 53.0% | 56.8% | +0.1% | +19.8% | 0.0% |
| Ajay Mitchell PRA under 26.5 | OKC @ CLE | draftkings | 1.81 | 1.81 | 1.51 | 66.2% | 51.7% | 55.4% | +0.0% | +19.7% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.8–113.4 | OKC 45% | 2.21 / 1.83 | CLE -2.5 | 224.5 | CLE -3.5 covers 46%; o228.5 42% |
| Expected (weighted by chance each plays) | 111.5–114.0 | OKC 44% | 2.30 / 1.77 | CLE -2.5 | 225.5 | CLE -3.5 covers 48%; o228.5 43% |
| if Peyton Watson plays | 111.2–114.5 | OKC 41% | 2.42 / 1.70 | CLE -3.5 | 225.5 | CLE -3.5 covers 50%; o228.5 43% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Peyton Watson (CLE) | Questionable | 55% | 27.7 | 12.2 | 4.4 | 2.1 | 1.3 | 0.9 | 1.2 | 1.8 | 18.8 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.3<br><sub>35,36,30,28,31</sub> | 27.9<br><sub>17,34,26,21,26</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>2,6,3,6,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>3,5,3,2,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>3,1,1,1,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.8 | 3.1 | 38.1 |
| Jared McCain | 98% | 29.7<br><sub>18,21,30,29,28</sub> | 14.5<br><sub>4,3,18,10,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>0,1,3,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.2<br><sub>0,1,4,0,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.1 | 1.7 | 19.9 |
| Ajay Mitchell | 98% | 28.3<br><sub>23,28,25,28,26</sub> | 15.9<br><sub>12,18,30,29,6</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>0,6,2,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>0,4,5,3,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.3 | 1.9 | 23.7 |
| Aday Mara | 96% | 27.0<br><sub>13,14,20,21,28</sub> | 9.2<br><sub>2,2,11,6,7</sub> | 7.5 · –<br><sub>o 55% · u 45%</sub> | 7.6<br><sub>3,3,10,3,9</sub> | 5.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.8 | 1.9 | 18.6 |
| Bennett Stirtz | 96% | 26.8<br><sub>2,11,25,28,26</sub> | 7.9<br><sub>0,2,7,8,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,1,1,0,1</sub> |  | 2.2<br><sub>0,0,1,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>0,0,1,1,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 1.0 | 11.9 |
| Isaiah Hartenstein | 98% | 26.3<br><sub>23,27,26,26,25</sub> | 10.1<br><sub>6,12,15,10,10</sub> | 10.5 · –<br><sub>o 44% · u 56%</sub> | 9.7<br><sub>6,12,13,14,7</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,1,3,3,0</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.7 | 1.8 | 23.0 |
| Jaylin Williams | 98% | 24.4<br><sub>15,5,26,20,26</sub> | 7.8<br><sub>3,0,6,0,3</sub> |  | 6.0<br><sub>7,0,6,5,4</sub> |  | 2.4<br><sub>3,0,3,1,1</sub> |  | 1.2<br><sub>1,0,2,0,0</sub> |  | 0.7 | 0.5 | 1.0 | 16.1 |
| Kenrich Williams | 96% | 23.5<br><sub>6,7,24,17,21</sub> | 8.9<br><sub>3,3,3,7,11</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>1,1,7,3,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,0,0,0,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.1 | 1.0 | 15.9 |
| Josh Dix | 76% | 20.6<br><sub>-,-,22,24,9</sub> | 6.7<br><sub>-,-,0,2,7</sub> |  | 2.7<br><sub>-,-,1,2,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.1 | 0.7 | 10.3 |
| Micah Peavy | 58% | 16.0<br><sub>-,-,-,5,14</sub> | 6.4<br><sub>-,-,-,0,2</sub> |  | 3.9<br><sub>-,-,-,0,1</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 11.0 |
| Brooks Barnhizer | 86% | 11.5<br><sub>2,-,3,14,6</sub> | 2.8<br><sub>0,-,0,3,5</sub> |  | 2.4<br><sub>0,-,0,2,2</sub> |  | 0.7<br><sub>1,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.8 |

</details>

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.8<br><sub>33,39,34,36,26</sub> | 18.3<br><sub>12,19,16,24,13</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>8,5,2,5,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>7,9,6,4,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>1,3,2,3,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3 | 0.5 | 3.8 | 29.9 |
| Donovan Mitchell | 98% | 36.5<br><sub>35,38,31,33,24</sub> | 24.4<br><sub>22,26,19,22,15</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 5.2<br><sub>5,5,5,3,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.8<br><sub>4,7,7,3,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.7<br><sub>2,5,2,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4 | 0.3 | 3.2 | 34.4 |
| Evan Mobley | 98% | 35.2<br><sub>35,38,32,33,25</sub> | 18.5<br><sub>20,18,24,11,27</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 9.1<br><sub>10,10,12,4,5</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,3,2,7,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,4,5,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.9 | 1.5 | 2.1 | 31.1 |
| Jarrett Allen | 98% | 30.0<br><sub>27,27,30,30,24</sub> | 13.8<br><sub>21,10,8,14,25</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>8,9,12,8,11</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,2,2,1,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>1,0,0,1,0</sub> |  | 0.9 | 1.2 | 1.4 | 24.4 |
| Sam Merrill | 98% | 26.3<br><sub>21,31,20,27,19</sub> | 10.0<br><sub>7,9,8,16,6</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>2,4,1,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>3,2,1,3,3</sub> |  | 1.9<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.1 | 0.8 | 14.7 |
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
| James Harden (CLE) | 98% | 35.3<br><sub>33,39,34,36,26</sub> | 17.3<br><sub>12,19,16,24,13</sub> | 17.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>8,5,2,5,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>7,9,6,4,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,3,2,3,3</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.5 | 3.6 | 28.4 |
| Donovan Mitchell (CLE) | 98% | 35.1<br><sub>35,38,31,33,24</sub> | 23.0<br><sub>22,26,19,22,15</sub> | 22.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>5,5,5,3,4</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>4,7,7,3,3</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>2,5,2,1,2</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.4 | 0.3 | 2.9 | 32.5 |
| Evan Mobley (CLE) | 98% | 33.5<br><sub>35,38,32,33,25</sub> | 17.2<br><sub>20,18,24,11,27</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 8.6<br><sub>10,10,12,4,5</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 3.4<br><sub>4,3,2,7,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>2,4,5,0,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.8 | 1.4 | 1.9 | 29.1 |
| Jarrett Allen (CLE) | 98% | 28.4<br><sub>27,27,30,30,24</sub> | 13.4<br><sub>21,10,8,14,25</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 8.7<br><sub>8,9,12,8,11</sub> | 8.5<br><sub>o 49% · u 51%</sub> | 1.5<br><sub>0,2,2,1,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.1<br><sub>1,0,0,1,0</sub> |  | 0.9 | 1.1 | 1.3 | 23.5 |
| Peyton Watson (CLE) | 100% | 27.7<br><sub>31,37,28,22,22</sub> | 12.2<br><sub>11,15,22,4,5</sub> | 13.5 · – | 4.4<br><sub>3,8,6,4,2</sub> | 4.5 | 2.1<br><sub>4,1,2,3,6</sub> | 1.5 | 1.3<br><sub>2,0,1,0,1</sub> | 1.5 | 0.9 | 1.2 | 1.8 | 18.8 |
| Sam Merrill (CLE) | 98% | 21.8<br><sub>21,31,20,27,19</sub> | 8.2<br><sub>7,9,8,16,6</sub> | 9.5 · –<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,4,1,2,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>3,2,1,3,3</sub> |  | 1.4<br><sub>1,1,2,4,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.6 | 0.1 | 0.7 | 12.0 |
| Meleek Thomas (CLE) | 67% | 19.9<br><sub>-,19,20,-,23</sub> | 8.3<br><sub>-,16,10,-,13</sub> |  | 2.5<br><sub>-,2,4,-,1</sub> |  | 1.2<br><sub>-,0,1,-,2</sub> |  | 1.0<br><sub>-,4,0,-,3</sub> |  | 0.6 | 0.2 | 1.1 | 12.0 |
| Mario Hezonja (CLE) | 96% | 16.4<br><sub>20,15,17,17,20</sub> | 6.5<br><sub>9,3,5,10,8</sub> |  | 4.0<br><sub>5,3,3,6,11</sub> |  | 1.5<br><sub>1,1,2,2,4</sub> |  | 0.7<br><sub>2,1,1,2,1</sub> |  | 0.5 | 0.3 | 0.9 | 12.0 |
| Tyrese Proctor (CLE) | 80% | 15.3<br><sub>11,-,6,20,18</sub> | 6.4<br><sub>5,-,2,7,9</sub> |  | 2.2<br><sub>2,-,1,6,4</sub> |  | 2.1<br><sub>3,-,1,2,5</sub> |  | 0.9<br><sub>1,-,0,1,3</sub> |  | 0.6 | 0.1 | 0.9 | 10.7 |
| Craig Porter Jr. (CLE) | 66% | 11.1<br><sub>5,-,-,4,16</sub> | 2.9<br><sub>3,-,-,0,2</sub> |  | 2.1<br><sub>1,-,-,1,2</sub> |  | 1.8<br><sub>1,-,-,0,4</sub> |  | 0.2<br><sub>1,-,-,0,0</sub> |  | 0.5 | 0.3 | 0.8 | 6.8 |
| Thomas Bryant (CLE) | 48% | 8.6<br><sub>-,-,-,-,11</sub> | 4.4<br><sub>-,-,-,-,11</sub> |  | 2.3<br><sub>-,-,-,-,2</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,3</sub> |  | 0.2 | 0.3 | 0.4 | 7.0 |
| Ernest Udeh Jr. (CLE) | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Tristan Enaruna (CLE) | 48% | 7.7<br><sub>-,-,-,-,6</sub> | 3.1<br><sub>-,-,-,-,2</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.8 |
| Riley Minix (CLE) | 43% | 7.6<br><sub>-,-,-,-,6</sub> | 3.2<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,3</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Shai Gilgeous-Alexander (OKC) | 98% | 34.3<br><sub>35,36,30,28,31</sub> | 27.7<br><sub>17,34,26,21,26</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>2,6,3,6,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>3,5,3,2,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>3,1,1,1,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.8 | 3.1 | 37.9 |
| Jared McCain (OKC) | 98% | 29.6<br><sub>18,21,30,29,28</sub> | 14.6<br><sub>4,3,18,10,10</sub> | 13.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>0,1,3,4,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.3<br><sub>1,0,4,4,2</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 2.2<br><sub>0,1,4,0,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.1 | 1.7 | 19.8 |
| Ajay Mitchell (OKC) | 98% | 28.4<br><sub>23,28,25,28,26</sub> | 16.0<br><sub>12,18,30,29,6</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>0,6,2,4,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>0,4,5,3,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>0,1,1,2,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.3 | 1.9 | 23.8 |
| Aday Mara (OKC) | 96% | 27.0<br><sub>13,14,20,21,28</sub> | 9.3<br><sub>2,2,11,6,7</sub> | 7.5 · –<br><sub>o 55% · u 45%</sub> | 7.6<br><sub>3,3,10,3,9</sub> | 5.5<br><sub>o 59% · u 41%</sub> | 1.8<br><sub>0,1,2,1,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.8 | 1.9 | 18.7 |
| Bennett Stirtz (OKC) | 96% | 26.8<br><sub>2,11,25,28,26</sub> | 7.9<br><sub>0,2,7,8,11</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,1,1,0,1</sub> |  | 2.2<br><sub>0,0,1,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1<br><sub>0,0,1,1,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 1.0 | 11.9 |
| Isaiah Hartenstein (OKC) | 98% | 26.2<br><sub>23,27,26,26,25</sub> | 10.1<br><sub>6,12,15,10,10</sub> | 10.5 · –<br><sub>o 44% · u 56%</sub> | 9.6<br><sub>6,12,13,14,7</sub> | 9.5<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>2,1,3,3,0</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.7 | 1.8 | 22.9 |
| Jaylin Williams (OKC) | 98% | 24.4<br><sub>15,5,26,20,26</sub> | 7.8<br><sub>3,0,6,0,3</sub> |  | 6.0<br><sub>7,0,6,5,4</sub> |  | 2.4<br><sub>3,0,3,1,1</sub> |  | 1.3<br><sub>1,0,2,0,0</sub> |  | 0.7 | 0.5 | 1.0 | 16.1 |
| Kenrich Williams (OKC) | 96% | 23.5<br><sub>6,7,24,17,21</sub> | 8.9<br><sub>3,3,3,7,11</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 5.3<br><sub>1,1,7,3,7</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,0,0,0,3</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.2 | 1.0 | 16.0 |
| Josh Dix (OKC) | 76% | 20.6<br><sub>-,-,22,24,9</sub> | 6.7<br><sub>-,-,0,2,7</sub> |  | 2.6<br><sub>-,-,1,2,0</sub> |  | 1.0<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,0,0,1</sub> |  | 0.6 | 0.2 | 0.7 | 10.3 |
| Micah Peavy (OKC) | 58% | 16.0<br><sub>-,-,-,5,14</sub> | 6.3<br><sub>-,-,-,0,2</sub> |  | 3.9<br><sub>-,-,-,0,1</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.3 | 0.7 | 10.9 |
| Brooks Barnhizer (OKC) | 86% | 11.6<br><sub>2,-,3,14,6</sub> | 2.9<br><sub>0,-,0,3,5</sub> |  | 2.4<br><sub>0,-,0,2,2</sub> |  | 0.7<br><sub>1,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.9 |

</details>


### DET @ CHA
Out: Kon Knueppel (CHA), Grant Williams (CHA), Jalen Duren (DET)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sion James 3PM under 0.5 | DET @ CHA | draftkings | 2.63 | 2.62 | 2.16 | 46.2% | 35.5% | 38.2% | +0.5% | +21.5% | 0.1% |
| Cade Cunningham RA under 14.5 | DET @ CHA | draftkings | 1.75 | 1.74 | 1.46 | 68.5% | 53.6% | 57.4% | +0.1% | +19.6% | 0.1% |

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
| Cade Cunningham | 98% | 34.9<br><sub>30,33,36,39,28</sub> | 24.4<br><sub>16,26,19,30,20</sub> | 24.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>2,8,9,5,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 7.8<br><sub>8,8,8,7,4</sub> | 8.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,3,2,4,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.2 | 0.8 | 4.0 | 37.4 |
| Duncan Robinson | 98% | 30.5<br><sub>28,32,33,32,26</sub> | 14.1<br><sub>17,21,12,13,17</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.5<br><sub>1,3,0,2,4</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 2.2<br><sub>2,3,2,2,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>5,5,2,3,2</sub> | 3.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.2 | 1.1 | 18.8 |
| Ausar Thompson | 98% | 27.9<br><sub>19,-,25,29,26</sub> | 9.6<br><sub>4,-,11,7,11</sub> | 10.5 · –<br><sub>o 42% · u 58%</sub> | 6.5<br><sub>3,-,6,9,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>5,-,2,8,6</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 0.1<br><sub>0,-,0,0,0</sub> |  | 2.0 | 1.0 | 1.6 | 19.9 |
| Paul Reed | 96% | 27.4<br><sub>26,23,26,38,31</sub> | 14.1<br><sub>19,8,22,16,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>11,8,9,4,4</sub> | 8.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>3,2,3,0,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.6<br><sub>2,0,1,2,0</sub> | 0.5<br><sub>o 36% · u 64%</sub> | 1.4 | 1.3 | 1.6 | 23.4 |
| John Collins | 98% | 27.0<br><sub>29,34,27,18,26</sub> | 10.9<br><sub>23,16,2,4,4</sub> | 12.5 · –<br><sub>o 44% · u 56%</sub> | 5.8<br><sub>7,11,9,2,9</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.9<br><sub>1,0,1,0,0</sub> |  | 1.1<br><sub>5,2,0,0,0</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 0.8 | 0.8 | 1.2 | 17.6 |
| Daniss Jenkins | 98% | 25.8<br><sub>22,38,24,24,24</sub> | 11.1<br><sub>15,18,11,14,6</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 3.1<br><sub>5,8,3,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 4.0<br><sub>5,6,2,3,5</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>1,3,1,2,2</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.0 | 0.3 | 1.5 | 18.2 |
| Kevin Huerter | 96% | 22.4<br><sub>20,26,16,19,24</sub> | 7.8<br><sub>5,9,7,3,8</sub> |  | 2.9<br><sub>6,3,1,2,1</sub> |  | 2.3<br><sub>2,2,0,3,3</sub> |  | 1.1<br><sub>1,1,1,1,2</sub> |  | 1.0 | 0.3 | 0.8 | 13.1 |
| Javonte Green | 96% | 21.3<br><sub>13,22,17,21,22</sub> | 7.1<br><sub>5,2,3,7,6</sub> |  | 3.2<br><sub>3,3,1,2,3</sub> |  | 0.8<br><sub>0,0,0,2,1</sub> |  | 1.1<br><sub>1,0,1,1,1</sub> |  | 1.3 | 0.5 | 0.6 | 11.2 |
| Ronald Holland II | 96% | 18.7<br><sub>22,23,12,12,22</sub> | 7.0<br><sub>8,2,4,0,18</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>5,9,3,2,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>4,4,2,1,2</sub> |  | 0.6<br><sub>0,0,0,0,2</sub> |  | 1.0 | 0.5 | 1.0 | 12.0 |
| Taurean Prince | 52% | 9.7<br><sub>-,-,7,6,-</sub> | 3.4<br><sub>-,-,3,1,-</sub> |  | 1.3<br><sub>-,-,0,2,-</sub> |  | 0.6<br><sub>-,-,0,0,-</sub> |  | 0.4<br><sub>-,-,1,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.3 |
| Tolu Smith | 86% | 6.9<br><sub>2,3,6,1,3</sub> | 2.7<br><sub>0,0,1,2,2</sub> |  | 2.1<br><sub>1,1,4,1,1</sub> |  | 0.4<br><sub>0,0,0,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.1 | 0.3 | 0.4 | 5.1 |
| Chaz Lanier | 52% | 6.4<br><sub>-,-,2,-,3</sub> | 2.4<br><sub>-,-,2,-,6</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,0,-,2</sub> |  | 0.2 | 0.1 | 0.1 | 3.4 |
| Ebuka Okorie | 58% | 5.9<br><sub>-,2,4,-,3</sub> | 2.1<br><sub>-,2,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.6<br><sub>-,0,2,-,0</sub> |  | 0.1<br><sub>-,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 3.0 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 33.9<br><sub>36,36,38,37,33</sub> | 23.0<br><sub>34,39,31,19,24</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>8,6,12,7,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 3.0<br><sub>4,1,3,2,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 3.2<br><sub>3,5,3,3,5</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.2 | 0.7 | 3.1 | 31.4 |
| Dennis Schroder | 98% | 31.9<br><sub>38,36,34,29,35</sub> | 12.8<br><sub>25,8,14,8,4</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>6,2,4,2,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 5.0<br><sub>4,5,5,8,7</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 1.2<br><sub>3,0,2,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.0 | 0.2 | 2.7 | 21.0 |
| Moussa Diabate | 98% | 29.8<br><sub>22,35,35,31,28</sub> | 8.8<br><sub>4,11,9,10,10</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 9.0<br><sub>5,17,9,12,8</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>2,3,2,1,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.6 | 19.8 |
| Naz Reid | 98% | 29.7<br><sub>37,29,13,31,36</sub> | 16.4<br><sub>23,18,7,12,14</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>9,12,6,11,5</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>0,1,0,1,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>5,2,1,2,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.9 | 2.4 | 26.0 |
| Grayson Allen | 96% | 28.2<br><sub>34,28,30,21,30</sub> | 14.6<br><sub>20,15,9,5,27</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>3,2,5,3,4</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>5,1,2,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 2.5<br><sub>4,2,2,1,7</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 1.9 | 20.4 |
| Sion James | 98% | 22.1<br><sub>26,29,23,29,18</sub> | 5.4<br><sub>0,5,5,6,4</sub> |  | 3.1<br><sub>5,2,2,5,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>5,3,3,4,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 0.7<br><sub>0,1,1,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.7 | 0.2 | 0.8 | 10.5 |
| Royce O'Neale | 98% | 21.1<br><sub>11,7,34,17,23</sub> | 6.5<br><sub>0,0,9,7,8</sub> |  | 3.6<br><sub>1,0,4,3,6</sub> |  | 1.1<br><sub>0,1,0,1,1</sub> |  | 1.2<br><sub>0,0,3,2,1</sub> |  | 0.7 | 0.4 | 0.7 | 11.2 |
| Ryan Kalkbrenner | 98% | 17.0<br><sub>23,13,13,15,19</sub> | 5.2<br><sub>6,6,1,2,6</sub> |  | 3.9<br><sub>5,4,1,4,3</sub> |  | 1.0<br><sub>2,1,1,0,4</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.8 | 10.1 |
| Coby White | 23% | 14.3 | 9.9 | 12.5 · –<br><sub>o 46% · u 54%</sub> | 1.9 |  | 1.8 |  | 1.1 | 1.5<br><sub>o 48% · u 52%</sub> | 0.4 | 0.1 | 1.4 | 13.7 |
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
| Confirmed players only | 117.3–116.5 | ATL 52% | 1.91 / 2.10 | IND +1.5 | 233.5 | IND +5.5 covers 63%; o232.5 53% |
| Expected (weighted by chance each plays) | 119.3–116.9 | ATL 57% | 1.75 / 2.33 | IND +2.5 | 236.5 | IND +5.5 covers 58%; o232.5 57% |
| if Obi Toppin plays | 117.8–117.9 | ATL 50% | 1.99 / 2.01 | IND +0.5 | 235.5 | IND +5.5 covers 65%; o232.5 57% |
| if Jalen Johnson plays | 120.5–115.3 | ATL 64% | 1.55 / 2.81 | IND +5.5 | 235.5 | IND +5.5 covers 50%; o232.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 18.1 | 7.6 | 3.1 | 1.5 | 0.9 | 0.5 | 0.1 | 1.0 | 12.1 | small |
| Keshon Gilbert (ATL) | Doubtful | 20% | 13.8 | 3.9 | 2.0 | 1.8 | 0.2 | 0.6 | 0.3 | 1.1 | 7.7 | small |
| Obi Toppin (IND) | Day-To-Day | 70% | 20.8 | 12.8 | 4.9 | 1.9 | 1.6 | 0.6 | 0.3 | 1.2 | 19.6 | full tables below |
| Jalen Johnson (ATL) | Questionable | 55% | 35.9 | 24.0 | 10.1 | 7.6 | 1.9 | 1.4 | 0.6 | 3.2 | 41.6 | full tables below |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker | 98% | 35.1<br><sub>32,29,32,31,29</sub> | 24.7<br><sub>18,12,23,25,12</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>5,2,3,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,3,1,1,1</sub> | 2.5<br><sub>o 63% · u 37%</sub> | 3.3<br><sub>4,2,5,4,0</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.5 | 2.8 | 33.0 |
| Onyeka Okongwu | 98% | 33.8<br><sub>26,29,31,33,28</sub> | 17.1<br><sub>8,11,11,29,6</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>6,9,4,12,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,1,4,2,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>0,1,1,4,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 1.0 | 1.8 | 29.2 |
| Dyson Daniels | 98% | 33.6<br><sub>29,28,28,32,27</sub> | 14.4<br><sub>18,4,7,4,8</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 6.8<br><sub>8,0,4,6,4</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.4<br><sub>3,4,7,5,3</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 0.6<br><sub>1,0,0,0,0</sub> |  | 2.5 | 0.4 | 1.9 | 27.6 |
| CJ McCollum | 98% | 31.3<br><sub>30,30,20,31,24</sub> | 21.9<br><sub>17,20,13,5,14</sub> | 16.5 · –<br><sub>o 54% · u 46%</sub> | 3.3<br><sub>2,1,2,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>1,3,1,8,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,4,1,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.6 | 2.5 | 29.9 |
| Luguentz Dort | 98% | 30.1<br><sub>23,21,24,22,29</sub> | 11.4<br><sub>7,11,8,6,11</sub> |  | 4.0<br><sub>2,2,3,3,3</sub> |  | 2.1<br><sub>3,1,3,2,0</sub> |  | 1.8<br><sub>1,0,2,1,1</sub> |  | 1.1 | 0.4 | 1.2 | 17.5 |
| Aaron Wiggins | 96% | 30.0<br><sub>29,27,24,24,23</sub> | 15.9<br><sub>16,12,10,20,10</sub> |  | 4.0<br><sub>5,4,4,7,2</sub> |  | 2.6<br><sub>2,3,3,3,1</sub> |  | 2.1<br><sub>4,2,2,4,2</sub> |  | 1.1 | 0.5 | 1.6 | 22.6 |
| Asa Newell | 52% | 19.9<br><sub>-,1,-,-,19</sub> | 8.6<br><sub>-,0,-,-,13</sub> |  | 4.0<br><sub>-,1,-,-,4</sub> |  | 1.2<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.7 | 0.6 | 0.9 | 13.8 |
| Corey Kispert | 52% | 16.8<br><sub>-,1,-,-,5</sub> | 8.3<br><sub>-,5,-,-,0</sub> |  | 2.3<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,0,-,-,1</sub> |  | 1.1<br><sub>-,1,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 12.1 |
| Dorian Finney-Smith | 52% | 15.0<br><sub>-,1,-,-,3</sub> | 3.8<br><sub>-,0,-,-,0</sub> |  | 2.5<br><sub>-,0,-,-,0</sub> |  | 1.1<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.3 |
| RayJ Dennis | 16% | 14.9 | 5.6 |  | 2.0 |  | 2.5 |  | 0.6 |  | 0.6 | 0.2 | 0.9 | 10.1 |
| Zuby Ejiofor | 47% | 12.5<br><sub>-,1,-,-,-</sub> | 4.1<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.3 |

</details>

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 98% | 34.2<br><sub>26,37,34,29,36</sub> | 26.2<br><sub>21,20,26,13,17</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>7,13,11,5,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>6,6,3,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,1,0,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 3.1 | 38.0 |
| Andrew Nembhard | 88% | 33.9<br><sub>30,-,35,30,35</sub> | 19.0<br><sub>14,-,18,22,23</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>1,-,3,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 9.5<br><sub>3,-,14,9,4</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>4,-,1,5,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.2 | 3.3 | 31.4 |
| Aaron Nesmith | 98% | 29.0<br><sub>19,21,27,21,30</sub> | 15.5<br><sub>13,13,18,9,11</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,0,2,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>2,1,1,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.0<br><sub>2,3,3,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.5 | 1.9 | 21.6 |
| Kelly Oubre Jr. | 98% | 27.1<br><sub>20,23,30,22,20</sub> | 11.9<br><sub>14,9,15,10,11</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>2,3,3,4,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.5 | 1.3 | 17.9 |
| Jarace Walker | 98% | 26.6<br><sub>19,29,22,28,20</sub> | 12.4<br><sub>6,10,7,14,6</sub> |  | 6.2<br><sub>7,8,8,6,6</sub> |  | 3.1<br><sub>1,2,1,4,3</sub> |  | 1.6<br><sub>0,2,1,3,2</sub> |  | 0.9 | 0.4 | 2.0 | 21.6 |
| Quenton Jackson | 98% | 24.6<br><sub>18,27,14,24,24</sub> | 11.4<br><sub>5,4,2,24,12</sub> |  | 3.1<br><sub>1,2,2,4,3</sub> |  | 4.2<br><sub>2,4,6,1,2</sub> |  | 0.9<br><sub>0,0,0,2,3</sub> |  | 1.0 | 0.2 | 1.5 | 18.7 |
| Larry Nance Jr. | 91% | 22.5<br><sub>22,19,23,18,26</sub> | 6.5<br><sub>6,2,5,6,4</sub> |  | 4.6<br><sub>6,3,5,2,6</sub> |  | 1.4<br><sub>1,1,0,1,1</sub> |  | 0.7<br><sub>1,0,1,2,1</sub> |  | 1.1 | 0.5 | 0.9 | 12.4 |
| Jay Huff | 91% | 20.0<br><sub>21,23,16,19,17</sub> | 8.5<br><sub>14,6,3,13,0</sub> |  | 3.8<br><sub>2,6,6,1,3</sub> |  | 1.6<br><sub>3,1,2,0,0</sub> |  | 1.1<br><sub>2,0,1,3,0</sub> |  | 0.5 | 1.5 | 1.0 | 13.9 |
| Jalen Slawson | 91% | 17.7<br><sub>8,3,12,18,18</sub> | 5.2<br><sub>1,2,2,4,3</sub> |  | 3.5<br><sub>2,1,1,4,5</sub> |  | 1.6<br><sub>0,0,1,1,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.0 | 10.3 |
| Kobe Brown | 63% | 17.6<br><sub>-,-,-,20,15</sub> | 6.7<br><sub>-,-,-,9,3</sub> |  | 3.3<br><sub>-,-,-,6,1</sub> |  | 1.6<br><sub>-,-,-,4,1</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.5 | 0.3 | 1.1 | 11.6 |
| Braden Smith | 76% | 11.2<br><sub>-,-,5,12,1</sub> | 3.0<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.9<br><sub>-,-,1,1,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 4.3 |

</details>

<details><summary>if Obi Toppin plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Nickeil Alexander-Walker (ATL) | 98% | 35.1<br><sub>32,29,32,31,29</sub> | 24.9<br><sub>18,12,23,25,12</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>5,2,3,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>4,3,1,1,1</sub> | 2.5<br><sub>o 63% · u 37%</sub> | 3.4<br><sub>4,2,5,4,0</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.5 | 2.8 | 33.1 |
| Onyeka Okongwu (ATL) | 98% | 33.8<br><sub>26,29,31,33,28</sub> | 17.1<br><sub>8,11,11,29,6</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 8.6<br><sub>6,9,4,12,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>2,1,4,2,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>0,1,1,4,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 1.0 | 1.7 | 29.2 |
| Dyson Daniels (ATL) | 98% | 33.5<br><sub>29,28,28,32,27</sub> | 14.4<br><sub>18,4,7,4,8</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 6.8<br><sub>8,0,4,6,4</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.4<br><sub>3,4,7,5,3</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 0.6<br><sub>1,0,0,0,0</sub> |  | 2.5 | 0.4 | 1.9 | 27.6 |
| CJ McCollum (ATL) | 98% | 31.3<br><sub>30,30,20,31,24</sub> | 22.0<br><sub>17,20,13,5,14</sub> | 16.5 · –<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>2,1,2,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 4.6<br><sub>1,3,1,8,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.4<br><sub>1,4,1,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.6 | 2.5 | 30.0 |
| Luguentz Dort (ATL) | 98% | 30.1<br><sub>23,21,24,22,29</sub> | 11.5<br><sub>7,11,8,6,11</sub> |  | 4.0<br><sub>2,2,3,3,3</sub> |  | 2.1<br><sub>3,1,3,2,0</sub> |  | 1.8<br><sub>1,0,2,1,1</sub> |  | 1.1 | 0.4 | 1.1 | 17.6 |
| Aaron Wiggins (ATL) | 96% | 29.9<br><sub>29,27,24,24,23</sub> | 16.0<br><sub>16,12,10,20,10</sub> |  | 4.0<br><sub>5,4,4,7,2</sub> |  | 2.6<br><sub>2,3,3,3,1</sub> |  | 2.1<br><sub>4,2,2,4,2</sub> |  | 1.1 | 0.5 | 1.6 | 22.7 |
| Asa Newell (ATL) | 52% | 20.1<br><sub>-,1,-,-,19</sub> | 8.8<br><sub>-,0,-,-,13</sub> |  | 4.1<br><sub>-,1,-,-,4</sub> |  | 1.2<br><sub>-,0,-,-,1</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.7 | 0.6 | 0.9 | 14.0 |
| Corey Kispert (ATL) | 52% | 16.8<br><sub>-,1,-,-,5</sub> | 8.4<br><sub>-,5,-,-,0</sub> |  | 2.4<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,0,-,-,1</sub> |  | 1.1<br><sub>-,1,-,-,0</sub> |  | 0.3 | 0.2 | 0.6 | 12.2 |
| Dorian Finney-Smith (ATL) | 52% | 15.1<br><sub>-,1,-,-,3</sub> | 3.7<br><sub>-,0,-,-,0</sub> |  | 2.5<br><sub>-,0,-,-,0</sub> |  | 1.1<br><sub>-,0,-,-,0</sub> |  | 0.5<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.3 |
| RayJ Dennis (ATL) | 16% | 15.0 | 5.7 |  | 2.0 |  | 2.5 |  | 0.6 |  | 0.5 | 0.2 | 0.9 | 10.2 |
| Zuby Ejiofor (ATL) | 47% | 12.5<br><sub>-,1,-,-,-</sub> | 4.0<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.5 | 7.3 |
| Pascal Siakam (IND) | 98% | 33.2<br><sub>26,37,34,29,36</sub> | 24.8<br><sub>21,20,26,13,17</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>7,13,11,5,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>6,6,3,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,1,0,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.4 | 2.7 | 36.2 |
| Andrew Nembhard (IND) | 88% | 33.0<br><sub>30,-,35,30,35</sub> | 17.9<br><sub>14,-,18,22,23</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 2.8<br><sub>1,-,3,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 8.9<br><sub>3,-,14,9,4</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>4,-,1,5,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0 | 0.2 | 2.9 | 29.6 |
| Aaron Nesmith (IND) | 98% | 27.8<br><sub>19,21,27,21,30</sub> | 14.0<br><sub>13,13,18,9,11</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>1,0,2,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>2,1,1,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>2,3,3,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.7 | 0.5 | 1.7 | 19.6 |
| Kelly Oubre Jr. (IND) | 98% | 25.1<br><sub>20,23,30,22,20</sub> | 10.3<br><sub>14,9,15,10,11</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>2,3,3,4,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.5<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.5 | 1.1 | 15.8 |
| Jarace Walker (IND) | 98% | 24.3<br><sub>19,29,22,28,20</sub> | 10.7<br><sub>6,10,7,14,6</sub> |  | 5.6<br><sub>7,8,8,6,6</sub> |  | 2.6<br><sub>1,2,1,4,3</sub> |  | 1.4<br><sub>0,2,1,3,2</sub> |  | 0.8 | 0.4 | 1.7 | 18.9 |
| Quenton Jackson (IND) | 98% | 22.4<br><sub>18,27,14,24,24</sub> | 10.0<br><sub>5,4,2,24,12</sub> |  | 2.7<br><sub>1,2,2,4,3</sub> |  | 3.6<br><sub>2,4,6,1,2</sub> |  | 0.8<br><sub>0,0,0,2,3</sub> |  | 0.9 | 0.2 | 1.3 | 16.3 |
| Obi Toppin (IND) | 100% | 20.8<br><sub>20,23,22,-,-</sub> | 12.8<br><sub>16,14,13,-,-</sub> |  | 4.9<br><sub>6,6,6,-,-</sub> |  | 1.9<br><sub>2,2,0,-,-</sub> |  | 1.6<br><sub>4,2,1,-,-</sub> |  | 0.6 | 0.3 | 1.2 | 19.6 |
| Larry Nance Jr. (IND) | 91% | 19.1<br><sub>22,19,23,18,26</sub> | 5.6<br><sub>6,2,5,6,4</sub> |  | 3.8<br><sub>6,3,5,2,6</sub> |  | 1.1<br><sub>1,1,0,1,1</sub> |  | 0.6<br><sub>1,0,1,2,1</sub> |  | 0.9 | 0.4 | 0.8 | 10.6 |
| Jay Huff (IND) | 91% | 18.2<br><sub>21,23,16,19,17</sub> | 7.7<br><sub>14,6,3,13,0</sub> |  | 3.5<br><sub>2,6,6,1,3</sub> |  | 1.4<br><sub>3,1,2,0,0</sub> |  | 1.0<br><sub>2,0,1,3,0</sub> |  | 0.4 | 1.3 | 0.8 | 12.5 |
| Jalen Slawson (IND) | 91% | 15.3<br><sub>8,3,12,18,18</sub> | 4.3<br><sub>1,2,2,4,3</sub> |  | 3.0<br><sub>2,1,1,4,5</sub> |  | 1.3<br><sub>0,0,1,1,0</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.6 | 0.8 | 8.7 |
| Kobe Brown (IND) | 63% | 14.4<br><sub>-,-,-,20,15</sub> | 5.3<br><sub>-,-,-,9,3</sub> |  | 2.7<br><sub>-,-,-,6,1</sub> |  | 1.3<br><sub>-,-,-,4,1</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.4 | 0.2 | 0.9 | 9.3 |
| Braden Smith (IND) | 76% | 8.6<br><sub>-,-,5,12,1</sub> | 2.4<br><sub>-,-,0,1,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.8<br><sub>-,-,1,1,0</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 3.5 |

</details>

<details><summary>if Jalen Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson (ATL) | 100% | 35.9<br><sub>38,36,36,34,28</sub> | 24.0<br><sub>26,21,12,17,13</sub> | 21.5 · – | 10.1<br><sub>9,9,9,8,7</sub> | 9.5 | 7.6<br><sub>16,3,11,7,4</sub> | 7.5 | 1.9<br><sub>2,1,2,2,1</sub> | 1.5 | 1.4 | 0.6 | 3.2 | 41.6 |
| Nickeil Alexander-Walker (ATL) | 98% | 34.1<br><sub>32,29,32,31,29</sub> | 21.4<br><sub>18,12,23,25,12</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>5,2,3,3,2</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,3,1,1,1</sub> | 2.5<br><sub>o 63% · u 37%</sub> | 3.1<br><sub>4,2,5,4,0</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3 | 0.5 | 2.4 | 28.5 |
| Dyson Daniels (ATL) | 98% | 32.9<br><sub>29,28,28,32,27</sub> | 12.3<br><sub>18,4,7,4,8</sub> | 11.5 · –<br><sub>o 54% · u 46%</sub> | 6.5<br><sub>8,0,4,6,4</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 5.5<br><sub>3,4,7,5,3</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 0.5<br><sub>1,0,0,0,0</sub> |  | 2.5 | 0.4 | 1.7 | 24.4 |
| Onyeka Okongwu (ATL) | 98% | 32.6<br><sub>26,29,31,33,28</sub> | 14.9<br><sub>8,11,11,29,6</sub> | 13.5 · –<br><sub>o 53% · u 47%</sub> | 8.2<br><sub>6,9,4,12,10</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,1,4,2,1</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>0,1,1,4,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 1.0 | 1.5 | 26.1 |
| CJ McCollum (ATL) | 98% | 30.3<br><sub>30,30,20,31,24</sub> | 19.2<br><sub>17,20,13,5,14</sub> | 16.5 · –<br><sub>o 54% · u 46%</sub> | 3.1<br><sub>2,1,2,3,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>1,3,1,8,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>1,4,1,0,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.5 | 2.2 | 26.0 |
| Luguentz Dort (ATL) | 98% | 28.2<br><sub>23,21,24,22,29</sub> | 9.2<br><sub>7,11,8,6,11</sub> |  | 3.6<br><sub>2,2,3,3,3</sub> |  | 1.7<br><sub>3,1,3,2,0</sub> |  | 1.4<br><sub>1,0,2,1,1</sub> |  | 1.1 | 0.4 | 0.9 | 14.6 |
| Aaron Wiggins (ATL) | 96% | 27.2<br><sub>29,27,24,24,23</sub> | 13.0<br><sub>16,12,10,20,10</sub> |  | 3.6<br><sub>5,4,4,7,2</sub> |  | 2.1<br><sub>2,3,3,3,1</sub> |  | 1.9<br><sub>4,2,2,4,2</sub> |  | 1.0 | 0.5 | 1.2 | 18.7 |
| Asa Newell (ATL) | 52% | 14.3<br><sub>-,1,-,-,19</sub> | 5.9<br><sub>-,0,-,-,13</sub> |  | 2.9<br><sub>-,1,-,-,4</sub> |  | 0.8<br><sub>-,0,-,-,1</sub> |  | 0.5<br><sub>-,0,-,-,1</sub> |  | 0.5 | 0.4 | 0.7 | 9.6 |
| RayJ Dennis (ATL) | 16% | 11.8 | 4.3 |  | 1.6 |  | 1.9 |  | 0.5 |  | 0.4 | 0.2 | 0.7 | 7.8 |
| Corey Kispert (ATL) | 52% | 11.2<br><sub>-,1,-,-,5</sub> | 5.3<br><sub>-,5,-,-,0</sub> |  | 1.6<br><sub>-,0,-,-,0</sub> |  | 0.9<br><sub>-,0,-,-,1</sub> |  | 0.6<br><sub>-,1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 7.8 |
| Dorian Finney-Smith (ATL) | 52% | 8.6<br><sub>-,1,-,-,3</sub> | 2.2<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,0,-,-,0</sub> |  | 0.6<br><sub>-,0,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Zuby Ejiofor (ATL) | 47% | 7.3<br><sub>-,1,-,-,-</sub> | 2.6<br><sub>-,0,-,-,-</sub> |  | 1.4<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.6 |
| Pascal Siakam (IND) | 98% | 34.1<br><sub>26,37,34,29,36</sub> | 25.9<br><sub>21,20,26,13,17</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>7,13,11,5,5</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>6,6,3,4,5</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,1,0,0,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.5 | 3.1 | 37.7 |
| Andrew Nembhard (IND) | 88% | 34.0<br><sub>30,-,35,30,35</sub> | 18.9<br><sub>14,-,18,22,23</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>1,-,3,2,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 9.6<br><sub>3,-,14,9,4</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>4,-,1,5,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.1 | 0.2 | 3.3 | 31.5 |
| Aaron Nesmith (IND) | 98% | 29.0<br><sub>19,21,27,21,30</sub> | 15.3<br><sub>13,13,18,9,11</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,0,2,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>2,1,1,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 2.0<br><sub>2,3,3,1,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.5 | 1.9 | 21.4 |
| Kelly Oubre Jr. (IND) | 98% | 27.0<br><sub>20,23,30,22,20</sub> | 11.8<br><sub>14,9,15,10,11</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>2,3,3,4,2</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>2,1,1,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0<br><sub>1,1,1,1,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.5 | 1.3 | 17.8 |
| Jarace Walker (IND) | 98% | 26.6<br><sub>19,29,22,28,20</sub> | 12.3<br><sub>6,10,7,14,6</sub> |  | 6.2<br><sub>7,8,8,6,6</sub> |  | 3.1<br><sub>1,2,1,4,3</sub> |  | 1.6<br><sub>0,2,1,3,2</sub> |  | 0.9 | 0.4 | 2.1 | 21.5 |
| Quenton Jackson (IND) | 98% | 24.7<br><sub>18,27,14,24,24</sub> | 11.4<br><sub>5,4,2,24,12</sub> |  | 3.1<br><sub>1,2,2,4,3</sub> |  | 4.2<br><sub>2,4,6,1,2</sub> |  | 0.9<br><sub>0,0,0,2,3</sub> |  | 1.0 | 0.2 | 1.6 | 18.7 |
| Larry Nance Jr. (IND) | 91% | 22.5<br><sub>22,19,23,18,26</sub> | 6.5<br><sub>6,2,5,6,4</sub> |  | 4.5<br><sub>6,3,5,2,6</sub> |  | 1.4<br><sub>1,1,0,1,1</sub> |  | 0.7<br><sub>1,0,1,2,1</sub> |  | 1.1 | 0.5 | 0.9 | 12.4 |
| Jay Huff (IND) | 91% | 19.9<br><sub>21,23,16,19,17</sub> | 8.4<br><sub>14,6,3,13,0</sub> |  | 3.8<br><sub>2,6,6,1,3</sub> |  | 1.6<br><sub>3,1,2,0,0</sub> |  | 1.1<br><sub>2,0,1,3,0</sub> |  | 0.5 | 1.5 | 1.0 | 13.8 |
| Jalen Slawson (IND) | 91% | 17.7<br><sub>8,3,12,18,18</sub> | 5.2<br><sub>1,2,2,4,3</sub> |  | 3.5<br><sub>2,1,1,4,5</sub> |  | 1.6<br><sub>0,0,1,1,0</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.7 | 1.0 | 10.3 |
| Kobe Brown (IND) | 63% | 17.6<br><sub>-,-,-,20,15</sub> | 6.7<br><sub>-,-,-,9,3</sub> |  | 3.3<br><sub>-,-,-,6,1</sub> |  | 1.6<br><sub>-,-,-,4,1</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.5 | 0.2 | 1.1 | 11.6 |
| Braden Smith (IND) | 76% | 11.2<br><sub>-,-,5,12,1</sub> | 3.0<br><sub>-,-,0,1,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 1.0<br><sub>-,-,1,1,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 4.2 |

</details>


### BKN @ NYK
Out: Egor Demin (BKN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Karl-Anthony Towns PA under 25.5 | BKN @ NYK | draftkings | 1.90 | 1.90 | 1.57 | 63.5% | 49.2% | 52.8% | +0.3% | +20.8% | 0.1% |
| Karl-Anthony Towns PR under 34.5 | BKN @ NYK | draftkings | 1.84 | 1.84 | 1.53 | 65.5% | 50.8% | 54.5% | +0.2% | +20.6% | 0.1% |
| Karl-Anthony Towns PRA under 38.5 | BKN @ NYK | draftkings | 1.86 | 1.86 | 1.55 | 64.4% | 50.2% | 53.7% | +0.1% | +19.9% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 102.9–116.8 | BKN 16% | 6.20 / 1.19 | NYK -13.5 | 219.5 | NYK -14.5 covers 48%; o219.5 51% |
| Expected (weighted by chance each plays) | 103.3–116.2 | BKN 18% | 5.59 / 1.22 | NYK -12.5 | 219.5 | NYK -14.5 covers 45%; o219.5 49% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Mikel Brown Jr. (BKN) | Day-To-Day | 70% | 19.7 | 9.0 | 2.1 | 3.0 | 1.1 | 0.6 | 0.1 | 1.4 | 14.1 | small |
| Jose Alvarado (NYK) | Questionable | 55% | 11.1 | 4.2 | 1.5 | 1.9 | 0.5 | 0.7 | 0.1 | 0.8 | 7.7 | small |

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 98% | 33.9<br><sub>35,24,44,25,37</sub> | 18.2<br><sub>23,10,24,15,20</sub> | 18.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>6,7,9,8,5</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>5,7,4,3,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>2,0,0,3,4</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.9 | 0.2 | 3.5 | 29.3 |
| Michael Porter Jr. | 98% | 32.8<br><sub>33,21,40,26,36</sub> | 19.8<br><sub>28,10,27,13,23</sub> | 20.5 · –<br><sub>o 46% · u 54%</sub> | 6.4<br><sub>9,0,12,7,9</sub> | 7.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>1,0,2,1,3</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 2.8<br><sub>4,0,6,2,3</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.3 | 2.2 | 28.3 |
| Nolan Traore | 98% | 24.0<br><sub>5,25,24,26,30</sub> | 10.2<br><sub>3,17,15,9,16</sub> | 11.5 · –<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>2,2,1,2,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 3.6<br><sub>0,5,3,2,6</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>0,2,1,0,4</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.9 | 0.5 | 2.3 | 15.9 |
| Chaney Johnson | 91% | 23.9<br><sub>27,21,29,19,31</sub> | 7.9<br><sub>10,4,15,6,2</sub> |  | 3.0<br><sub>5,5,3,2,2</sub> |  | 1.2<br><sub>3,0,2,0,0</sub> |  | 0.9<br><sub>2,0,3,0,0</sub> |  | 0.7 | 0.4 | 1.1 | 12.1 |
| Keon Ellis | 96% | 22.9<br><sub>22,23,25,21,20</sub> | 6.6<br><sub>6,9,2,6,0</sub> |  | 2.1<br><sub>2,1,3,2,2</sub> |  | 1.5<br><sub>1,3,4,1,1</sub> |  | 1.0<br><sub>2,1,0,2,0</sub> |  | 1.1 | 0.6 | 0.7 | 10.2 |
| Day'Ron Sharpe | 98% | 22.6<br><sub>23,16,17,24,26</sub> | 8.8<br><sub>7,11,4,3,15</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 7.2<br><sub>8,4,6,7,13</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 2.3<br><sub>1,1,0,1,4</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.3<br><sub>1,1,0,0,1</sub> |  | 0.9 | 0.7 | 1.6 | 18.3 |
| Noah Clowney | 98% | 22.6<br><sub>20,20,24,22,24</sub> | 7.8<br><sub>4,9,3,3,8</sub> | 6.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>4,5,4,8,3</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.1<br><sub>0,1,1,1,0</sub> |  | 1.2<br><sub>1,1,1,0,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.6 | 0.6 | 0.9 | 12.5 |
| Moritz Wagner | 91% | 19.0<br><sub>14,15,22,23,21</sub> | 9.6<br><sub>6,13,15,16,14</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>4,3,4,8,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.2<br><sub>1,1,3,1,0</sub> |  | 0.8<br><sub>1,2,2,1,1</sub> |  | 0.6 | 0.3 | 1.2 | 15.0 |
| Terance Mann | 58% | 15.4<br><sub>-,-,-,12,15</sub> | 4.6<br><sub>-,-,-,2,0</sub> |  | 1.9<br><sub>-,-,-,0,1</sub> |  | 1.4<br><sub>-,-,-,2,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.7 | 7.9 |
| Danny Wolf | 52% | 12.0<br><sub>-,15,-,12,-</sub> | 4.9<br><sub>-,6,-,9,-</sub> |  | 2.7<br><sub>-,2,-,6,-</sub> |  | 1.1<br><sub>-,1,-,2,-</sub> |  | 0.5<br><sub>-,2,-,3,-</sub> |  | 0.3 | 0.3 | 0.7 | 8.7 |
| Ben Saraf | 58% | 11.9<br><sub>-,4,-,-,-</sub> | 4.5<br><sub>-,2,-,-,-</sub> |  | 1.2<br><sub>-,1,-,-,-</sub> |  | 1.7<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.5 | 0.1 | 1.3 | 7.4 |
| Josh Minott | 52% | 10.9<br><sub>9,21,-,3,-</sub> | 5.3<br><sub>4,15,-,2,-</sub> |  | 1.8<br><sub>2,8,-,0,-</sub> |  | 0.6<br><sub>0,2,-,0,-</sub> |  | 0.7<br><sub>0,3,-,0,-</sub> |  | 0.5 | 0.4 | 0.6 | 7.7 |
| Drake Powell | 52% | 10.0<br><sub>-,12,-,6,-</sub> | 3.5<br><sub>-,0,-,0,-</sub> |  | 0.8<br><sub>-,2,-,0,-</sub> |  | 0.6<br><sub>-,3,-,2,-</sub> |  | 0.3<br><sub>-,0,-,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 4.9 |
| Grant Nelson | 16% | 9.0 | 3.3 |  | 1.9 |  | 0.6 |  | 0.0 |  | 0.2 | 0.8 | 0.5 | 5.8 |
| Joshua Jefferson | 80% | 6.5<br><sub>-,4,-,-,-</sub> | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 1.0 |

</details>

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 34.8<br><sub>37,32,36,35,35</sub> | 26.6<br><sub>19,28,23,38,24</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>2,3,1,1,5</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 6.7<br><sub>4,4,7,7,6</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>2,1,0,6,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.2 | 2.8 | 36.6 |
| OG Anunoby | 98% | 33.5<br><sub>34,35,36,31,34</sub> | 18.1<br><sub>20,22,13,23,9</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>10,3,7,6,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.3<br><sub>8,2,2,1,3</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>2,3,1,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.9 | 1.6 | 26.1 |
| Josh Hart | 98% | 32.1<br><sub>36,35,27,36,31</sub> | 10.8<br><sub>10,13,6,2,7</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 7.8<br><sub>12,8,4,8,6</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 4.6<br><sub>5,2,4,3,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,3,2,0,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.6 | 0.3 | 1.8 | 23.2 |
| Karl-Anthony Towns | 98% | 31.5<br><sub>37,33,33,28,35</sub> | 19.7<br><sub>22,22,27,19,22</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 12.1<br><sub>10,14,20,13,12</sub> | 12.5<br><sub>o 46% · u 54%</sub> | 4.1<br><sub>3,4,3,5,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>2,0,1,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.9 | 2.8 | 35.9 |
| Mikal Bridges | 98% | 28.8<br><sub>22,35,32,13,30</sub> | 10.8<br><sub>0,6,12,3,12</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>1,5,3,0,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.8<br><sub>4,1,4,0,2</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>0,0,4,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.5 | 1.0 | 16.7 |
| Landry Shamet | 98% | 22.9<br><sub>21,22,28,32,16</sub> | 8.4<br><sub>8,6,13,14,0</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.8<br><sub>2,2,2,1,0</sub> |  | 1.6<br><sub>0,1,3,5,0</sub> |  | 1.5<br><sub>2,2,3,4,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.2 | 0.8 | 11.8 |
| Miles McBride | 98% | 19.6<br><sub>30,13,17,14,24</sub> | 7.8<br><sub>20,1,5,3,10</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>2,1,1,5,3</sub> |  | 1.8<br><sub>1,1,1,0,1</sub> |  | 1.4<br><sub>6,0,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 0.2 | 0.7 | 11.4 |
| Andre Drummond | 98% | 14.1<br><sub>7,7,14,15,12</sub> | 5.4<br><sub>2,4,10,4,3</sub> |  | 5.9<br><sub>2,3,8,11,6</sub> |  | 1.2<br><sub>0,2,1,1,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.6 | 0.8 | 12.6 |
| Tyler Kolek | 71% | 13.9<br><sub>-,15,11,18,13</sub> | 4.8<br><sub>-,0,2,9,2</sub> |  | 1.7<br><sub>-,3,1,2,1</sub> |  | 4.2<br><sub>-,9,3,9,4</sub> |  | 0.6<br><sub>-,0,0,3,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.6 |
| Jordan Clarkson | 83% | 11.7<br><sub>3,5,-,17,9</sub> | 5.9<br><sub>0,0,-,18,4</sub> |  | 1.7<br><sub>1,1,-,3,3</sub> |  | 1.0<br><sub>0,0,-,1,0</sub> |  | 0.4<br><sub>0,0,-,2,0</sub> |  | 0.4 | 0.1 | 0.8 | 8.7 |
| Tyler Nickel | 38% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Mohamed Diawara | 36% | 8.0<br><sub>-,-,1,-,-</sub> | 2.9<br><sub>-,-,0,-,-</sub> |  | 1.3<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Dalton Knecht | 35% | 7.4<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.3 |
| Jaden Akins | 38% | 7.4<br><sub>-,-,2,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| James Wiseman | 52% | 6.8<br><sub>2,7,1,-,-</sub> | 2.5<br><sub>0,0,0,-,-</sub> |  | 2.0<br><sub>0,2,1,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 4.8 |
| Pacome Dadiet | 36% | 6.6<br><sub>-,-,1,-,-</sub> | 2.8<br><sub>-,-,0,-,-</sub> |  | 1.4<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.7 |

</details>


### WAS @ ORL
Out: Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL), Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.8–116.4 | WAS 37% | 2.71 / 1.59 | ORL -4.5 | 227.5 | ORL -2.5 covers 57%; o225.5 55% |
| Expected (weighted by chance each plays) | 111.8–116.1 | WAS 38% | 2.62 / 1.62 | ORL -4.5 | 227.5 | ORL -2.5 covers 56%; o225.5 54% |
| if Alex Sarr plays | 111.9–116.0 | WAS 38% | 2.62 / 1.62 | ORL -4.5 | 227.5 | ORL -2.5 covers 56%; o225.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Gill (WAS) | Questionable | 55% | 12.1 | 4.1 | 2.1 | 0.8 | 0.2 | 0.4 | 0.3 | 0.6 | 7.0 | small |
| Alex Sarr (WAS) | Questionable | 55% | 25.9 | 10.9 | 6.3 | 2.1 | 0.9 | 0.8 | 1.9 | 1.4 | 19.3 | full tables below |

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 35.5<br><sub>37,34,38,34,38</sub> | 21.2<br><sub>22,25,22,14,21</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>1,4,6,5,7</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 9.7<br><sub>12,9,10,8,9</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>4,4,1,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 3.9 | 34.4 |
| Anthony Davis | 98% | 34.3<br><sub>32,31,36,34,34</sub> | 21.7<br><sub>9,19,29,18,25</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 12.2<br><sub>9,6,10,5,13</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.8<br><sub>0,4,0,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.7<br><sub>0,0,3,2,0</sub> |  | 1.1 | 2.1 | 2.5 | 36.8 |
| Kyshawn George | 98% | 32.6<br><sub>26,36,29,38,32</sub> | 16.3<br><sub>11,22,20,8,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>3,9,4,2,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>3,5,2,11,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,0,2,0,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.2 | 2.6 | 26.1 |
| AJ Dybantsa | 88% | 30.7<br><sub>-,-,-,27,30</sub> | 15.5<br><sub>-,-,-,19,17</sub> | 16.5 · –<br><sub>o 45% · u 55%</sub> | 5.8<br><sub>-,-,-,2,8</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>-,-,-,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.8<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.4 | 1.8 | 23.1 |
| Bilal Coulibaly | 98% | 27.9<br><sub>26,25,29,27,22</sub> | 10.3<br><sub>11,7,3,17,1</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>6,4,5,2,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,0,1,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.2 | 1.0 | 1.4 | 16.7 |
| Bub Carrington | 98% | 24.7<br><sub>11,21,28,20,20</sub> | 8.8<br><sub>3,9,6,3,9</sub> |  | 3.0<br><sub>1,2,0,1,4</sub> |  | 3.2<br><sub>0,1,3,3,2</sub> |  | 1.3<br><sub>1,3,2,0,3</sub> |  | 0.6 | 0.2 | 1.7 | 15.0 |
| Tre Johnson | 72% | 20.0<br><sub>26,23,23,-,13</sub> | 7.2<br><sub>20,13,7,-,4</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 2.5<br><sub>2,2,3,-,2</sub> |  | 1.1<br><sub>0,2,2,-,0</sub> |  | 0.9<br><sub>4,2,1,-,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.5 | 0.3 | 0.9 | 10.8 |
| Deandre Ayton | 98% | 17.9<br><sub>14,16,12,12,17</sub> | 5.9<br><sub>4,6,0,10,3</sub> |  | 5.6<br><sub>6,5,4,3,3</sub> |  | 0.8<br><sub>1,0,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.7 | 0.9 | 12.3 |
| Khris Middleton | 88% | 16.4<br><sub>16,-,13,23,5</sub> | 5.3<br><sub>6,-,0,4,0</sub> |  | 2.8<br><sub>2,-,1,3,0</sub> |  | 1.2<br><sub>0,-,0,2,0</sub> |  | 0.5<br><sub>0,-,0,1,0</sub> |  | 0.6 | 0.1 | 1.1 | 9.4 |
| Will Riley | 67% | 10.3<br><sub>1,5,4,-,1</sub> | 4.5<br><sub>0,2,2,-,0</sub> |  | 1.4<br><sub>0,0,0,-,0</sub> |  | 0.8<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.1 | 0.7 | 6.7 |
| Reece Beekman | 38% | 8.7<br><sub>1,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 1.3 |
| Felix Okpara | 38% | 8.3<br><sub>1,-,-,-,-</sub> | 3.0<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 3.8 |
| Tre Mann | 52% | 7.6<br><sub>1,-,-,-,1</sub> | 2.7<br><sub>0,-,-,-,0</sub> |  | 1.1<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |

</details>

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane | 98% | 34.6<br><sub>27,35,34,39,40</sub> | 22.8<br><sub>5,22,13,28,19</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,6,5,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>0,2,4,6,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.8<br><sub>1,4,2,6,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.5 | 2.3 | 31.4 |
| Franz Wagner | 98% | 34.1<br><sub>33,37,34,39,40</sub> | 24.6<br><sub>18,23,15,26,14</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>6,13,4,5,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 6.3<br><sub>5,9,5,11,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 2.9 | 37.1 |
| Wendell Carter Jr. | 98% | 32.3<br><sub>29,33,26,39,35</sub> | 14.1<br><sub>20,9,3,20,7</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>9,10,10,7,10</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,2,3,1,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0<br><sub>3,0,0,1,1</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.9 | 1.7 | 24.9 |
| Anthony Black | 98% | 30.9<br><sub>-,26,22,31,33</sub> | 15.9<br><sub>-,18,8,17,23</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>-,3,2,6,8</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.4<br><sub>-,5,1,10,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>-,5,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.9 | 0.7 | 1.9 | 24.5 |
| Tristan da Silva | 98% | 30.1<br><sub>29,27,31,23,35</sub> | 13.4<br><sub>5,19,20,8,23</sub> |  | 4.5<br><sub>3,2,3,0,10</sub> |  | 2.2<br><sub>1,2,1,0,2</sub> |  | 1.9<br><sub>1,5,4,2,5</sub> |  | 0.9 | 0.4 | 1.2 | 20.1 |
| Jase Richardson | 91% | 23.5<br><sub>14,17,14,33,26</sub> | 8.5<br><sub>6,6,10,4,4</sub> |  | 2.6<br><sub>1,1,1,6,1</sub> |  | 2.6<br><sub>3,0,1,2,3</sub> |  | 0.8<br><sub>1,2,2,0,0</sub> |  | 0.8 | 0.2 | 1.0 | 13.7 |
| Jamal Cain | 98% | 18.4<br><sub>11,15,16,15,18</sub> | 7.7<br><sub>0,5,9,13,5</sub> |  | 3.0<br><sub>1,5,1,0,1</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>0,1,0,3,1</sub> |  | 0.5 | 0.3 | 0.8 | 11.6 |
| Jevon Carter | 48% | 14.3<br><sub>13,-,22,-,-</sub> | 4.8<br><sub>0,-,6,-,-</sub> |  | 1.4<br><sub>1,-,0,-,-</sub> |  | 1.6<br><sub>1,-,3,-,-</sub> |  | 0.7<br><sub>0,-,2,-,-</sub> |  | 0.7 | 0.2 | 0.5 | 7.9 |
| Goga Bitadze | 86% | 11.8<br><sub>12,-,11,6,5</sub> | 4.8<br><sub>4,-,6,2,0</sub> |  | 4.3<br><sub>3,-,0,4,1</sub> |  | 1.0<br><sub>0,-,1,0,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.9 | 0.7 | 10.1 |
| Nikola Vucevic | 96% | 11.8<br><sub>4,15,16,6,7</sub> | 5.1<br><sub>0,5,5,3,2</sub> |  | 3.5<br><sub>2,3,4,1,4</sub> |  | 1.5<br><sub>0,3,2,0,2</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.5 | 0.6 | 10.1 |
| Alex Morales | 52% | 9.5<br><sub>4,-,7,9,-</sub> | 2.7<br><sub>0,-,2,0,-</sub> |  | 1.5<br><sub>1,-,2,1,-</sub> |  | 1.0<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 5.2 |
| Colin Castleton | 48% | 7.3<br><sub>4,-,7,-,-</sub> | 2.5<br><sub>7,-,2,-,-</sub> |  | 2.3<br><sub>2,-,2,-,-</sub> |  | 0.5<br><sub>1,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.3 |

</details>

<details><summary>if Alex Sarr plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane (ORL) | 98% | 34.6<br><sub>27,35,34,39,40</sub> | 22.7<br><sub>5,22,13,28,19</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>2,6,5,2,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 4.0<br><sub>0,2,4,6,1</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>1,4,2,6,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.5 | 2.3 | 31.3 |
| Franz Wagner (ORL) | 98% | 34.1<br><sub>33,37,34,39,40</sub> | 24.5<br><sub>18,23,15,26,14</sub> | 23.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>6,13,4,5,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>5,9,5,11,12</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,0,0,2,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.4 | 0.4 | 2.9 | 36.9 |
| Wendell Carter Jr. (ORL) | 98% | 32.3<br><sub>29,33,26,39,35</sub> | 14.1<br><sub>20,9,3,20,7</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 8.5<br><sub>9,10,10,7,10</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 2.3<br><sub>1,2,3,1,0</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.0<br><sub>3,0,0,1,1</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.9 | 1.7 | 24.9 |
| Anthony Black (ORL) | 98% | 30.9<br><sub>-,26,22,31,33</sub> | 15.9<br><sub>-,18,8,17,23</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>-,3,2,6,8</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 4.3<br><sub>-,5,1,10,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>-,5,0,3,1</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.8 | 0.7 | 1.9 | 24.4 |
| Tristan da Silva (ORL) | 98% | 30.1<br><sub>29,27,31,23,35</sub> | 13.4<br><sub>5,19,20,8,23</sub> |  | 4.5<br><sub>3,2,3,0,10</sub> |  | 2.2<br><sub>1,2,1,0,2</sub> |  | 1.9<br><sub>1,5,4,2,5</sub> |  | 0.9 | 0.4 | 1.2 | 20.0 |
| Jase Richardson (ORL) | 91% | 23.5<br><sub>14,17,14,33,26</sub> | 8.5<br><sub>6,6,10,4,4</sub> |  | 2.6<br><sub>1,1,1,6,1</sub> |  | 2.5<br><sub>3,0,1,2,3</sub> |  | 0.8<br><sub>1,2,2,0,0</sub> |  | 0.9 | 0.2 | 1.0 | 13.7 |
| Jamal Cain (ORL) | 98% | 18.4<br><sub>11,15,16,15,18</sub> | 7.7<br><sub>0,5,9,13,5</sub> |  | 3.0<br><sub>1,5,1,0,1</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.8<br><sub>0,1,0,3,1</sub> |  | 0.5 | 0.3 | 0.8 | 11.6 |
| Jevon Carter (ORL) | 48% | 14.3<br><sub>13,-,22,-,-</sub> | 4.8<br><sub>0,-,6,-,-</sub> |  | 1.4<br><sub>1,-,0,-,-</sub> |  | 1.6<br><sub>1,-,3,-,-</sub> |  | 0.7<br><sub>0,-,2,-,-</sub> |  | 0.7 | 0.2 | 0.5 | 7.8 |
| Goga Bitadze (ORL) | 86% | 11.8<br><sub>12,-,11,6,5</sub> | 4.8<br><sub>4,-,6,2,0</sub> |  | 4.2<br><sub>3,-,0,4,1</sub> |  | 1.0<br><sub>0,-,1,0,0</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.9 | 0.7 | 10.1 |
| Nikola Vucevic (ORL) | 96% | 11.8<br><sub>4,15,16,6,7</sub> | 5.1<br><sub>0,5,5,3,2</sub> |  | 3.5<br><sub>2,3,4,1,4</sub> |  | 1.5<br><sub>0,3,2,0,2</sub> |  | 0.5<br><sub>0,1,0,1,0</sub> |  | 0.3 | 0.5 | 0.6 | 10.1 |
| Alex Morales (ORL) | 52% | 9.5<br><sub>4,-,7,9,-</sub> | 2.7<br><sub>0,-,2,0,-</sub> |  | 1.5<br><sub>1,-,2,1,-</sub> |  | 1.0<br><sub>0,-,1,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.6 | 5.2 |
| Colin Castleton (ORL) | 48% | 7.3<br><sub>4,-,7,-,-</sub> | 2.5<br><sub>7,-,2,-,-</sub> |  | 2.2<br><sub>2,-,2,-,-</sub> |  | 0.5<br><sub>1,-,0,-,-</sub> |  | 0.0<br><sub>0,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.5 | 5.3 |
| Trae Young (WAS) | 98% | 34.5<br><sub>37,34,38,34,38</sub> | 19.9<br><sub>22,25,22,14,21</sub> | 19.5 · –<br><sub>o 50% · u 50%</sub> | 3.3<br><sub>1,4,6,5,7</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 9.7<br><sub>12,9,10,8,9</sub> | 9.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>4,4,1,1,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.3 | 3.7 | 33.0 |
| Anthony Davis (WAS) | 98% | 33.5<br><sub>32,31,36,34,34</sub> | 20.9<br><sub>9,19,29,18,25</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 11.4<br><sub>9,6,10,5,13</sub> | 10.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>0,4,0,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 0.7<br><sub>0,0,3,2,0</sub> |  | 1.1 | 2.0 | 2.3 | 35.0 |
| Kyshawn George (WAS) | 98% | 30.9<br><sub>26,36,29,38,32</sub> | 14.8<br><sub>11,22,20,8,12</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>3,9,4,2,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.0<br><sub>3,5,2,11,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.6<br><sub>1,0,2,0,4</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.1 | 1.1 | 2.3 | 23.9 |
| AJ Dybantsa (WAS) | 88% | 29.0<br><sub>-,-,-,27,30</sub> | 15.0<br><sub>-,-,-,19,17</sub> | 16.5 · –<br><sub>o 45% · u 55%</sub> | 5.2<br><sub>-,-,-,2,8</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>-,-,-,2,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9<br><sub>-,-,-,1,1</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.4 | 1.7 | 21.8 |
| Alex Sarr (WAS) | 100% | 25.9<br><sub>25,23,26,26,29</sub> | 10.9<br><sub>7,10,12,18,3</sub> | 10.5 · – | 6.3<br><sub>4,2,6,4,8</sub> | 6.5 | 2.1<br><sub>5,3,1,2,0</sub> | 1.5 | 0.9<br><sub>1,0,0,2,1</sub> | 0.5 | 0.8 | 1.9 | 1.4 | 19.3 |
| Bilal Coulibaly (WAS) | 98% | 24.9<br><sub>26,25,29,27,22</sub> | 8.9<br><sub>11,7,3,17,1</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.9<br><sub>6,4,5,2,5</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,0,1,0,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>1,0,0,1,0</sub> | 0.5<br><sub>o 61% · u 39%</sub> | 1.1 | 0.9 | 1.2 | 14.4 |
| Bub Carrington (WAS) | 98% | 21.2<br><sub>11,21,28,20,20</sub> | 6.9<br><sub>3,9,6,3,9</sub> |  | 2.5<br><sub>1,2,0,1,4</sub> |  | 2.8<br><sub>0,1,3,3,2</sub> |  | 1.1<br><sub>1,3,2,0,3</sub> |  | 0.6 | 0.2 | 1.4 | 12.2 |
| Tre Johnson (WAS) | 72% | 16.9<br><sub>26,23,23,-,13</sub> | 6.2<br><sub>20,13,7,-,4</sub> | 8.5 · –<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,2,3,-,2</sub> |  | 1.0<br><sub>0,2,2,-,0</sub> |  | 0.8<br><sub>4,2,1,-,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.5 | 0.3 | 0.8 | 9.3 |
| Deandre Ayton (WAS) | 98% | 15.2<br><sub>14,16,12,12,17</sub> | 5.2<br><sub>4,6,0,10,3</sub> |  | 4.6<br><sub>6,5,4,3,3</sub> |  | 0.7<br><sub>1,0,2,0,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.8 | 10.5 |
| Khris Middleton (WAS) | 88% | 13.1<br><sub>16,-,13,23,5</sub> | 4.1<br><sub>6,-,0,4,0</sub> |  | 2.1<br><sub>2,-,1,3,0</sub> |  | 1.0<br><sub>0,-,0,2,0</sub> |  | 0.3<br><sub>0,-,0,1,0</sub> |  | 0.5 | 0.1 | 0.9 | 7.3 |
| Will Riley (WAS) | 67% | 8.5<br><sub>1,5,4,-,1</sub> | 3.9<br><sub>0,2,2,-,0</sub> |  | 1.2<br><sub>0,0,0,-,0</sub> |  | 0.7<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 5.8 |
| Reece Beekman (WAS) | 38% | 7.1<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.1 |
| Felix Okpara (WAS) | 38% | 6.9<br><sub>1,-,-,-,-</sub> | 3.2<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 3.8 |
| Tre Mann (WAS) | 52% | 6.0<br><sub>1,-,-,-,1</sub> | 2.6<br><sub>0,-,-,-,0</sub> |  | 0.8<br><sub>0,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.1 |

</details>


### CHI @ PHI
Out: Dominick Barlow (PHI), Ariel Hukporti (PHI)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson PTS under 19.5 | CHI @ PHI | draftkings | 1.93 | 1.92 | 1.58 | 63.1% | 48.5% | 52.2% | +0.5% | +21.6% | 0.1% |
| Matas Buzelis AST under 1.5 | CHI @ PHI | draftkings | 2.33 | 2.32 | 1.93 | 51.8% | 40.1% | 43.0% | +0.3% | +20.8% | 0.1% |
| Caleb Wilson PA under 22.5 | CHI @ PHI | draftkings | 1.86 | 1.86 | 1.55 | 64.5% | 50.2% | 53.8% | +0.1% | +20.1% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.6–120.3 | CHI 32% | 3.13 / 1.47 | PHI -6.5 | 233.5 | PHI -10.5 covers 39%; o238.5 40% |
| Expected (weighted by chance each plays) | 113.0–121.2 | CHI 28% | 3.58 / 1.39 | PHI -8.5 | 234.5 | PHI -10.5 covers 44%; o238.5 41% |
| if Joel Embiid plays | 112.6–121.9 | CHI 25% | 3.96 / 1.34 | PHI -9.5 | 234.5 | PHI -10.5 covers 47%; o238.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Joel Embiid (PHI) | Questionable | 55% | 32.8 | 24.5 | 8.9 | 5.0 | 1.3 | 0.9 | 1.3 | 2.8 | 38.5 | full tables below |
| Nic Claxton (CHI) | Doubtful | 20% | 16.7 | 6.4 | 4.6 | 1.7 | 0.1 | 0.4 | 0.8 | 1.0 | 12.7 | small |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson | 96% | 32.8<br><sub>33,38,32,38,31</sub> | 18.1<br><sub>21,30,17,20,23</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.6<br><sub>6,14,5,6,5</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>1,3,3,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,1,1,3,6</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 1.4 | 2.9 | 27.3 |
| Norman Powell | 98% | 30.0<br><sub>33,33,24,37,31</sub> | 18.3<br><sub>25,18,20,30,16</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,2,1,2,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,3,2,2,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.2<br><sub>2,3,4,4,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.2 | 2.2 | 23.8 |
| Josh Giddey | 98% | 28.4<br><sub>25,30,24,31,25</sub> | 11.8<br><sub>6,9,11,10,13</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>4,8,1,8,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>9,10,4,11,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,1,1,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.5 | 3.0 | 26.4 |
| Matas Buzelis | 98% | 26.0<br><sub>17,35,22,33,20</sub> | 14.1<br><sub>7,21,11,17,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>5,5,1,5,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.7<br><sub>3,2,2,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.8<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 1.1 | 2.3 | 21.3 |
| Jalen Smith | 91% | 24.2<br><sub>24,24,20,30,27</sub> | 11.4<br><sub>14,14,7,17,5</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>13,3,6,11,12</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>1,1,1,5,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>2,2,2,3,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.5 | 0.8 | 1.2 | 20.7 |
| Tre Jones | 98% | 18.9<br><sub>24,18,15,18,20</sub> | 10.1<br><sub>11,10,8,11,12</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,2,1,4,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>8,3,0,3,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.8 | 0.1 | 1.2 | 16.0 |
| Isaac Okoro | 98% | 17.4<br><sub>28,14,11,18,18</sub> | 5.7<br><sub>12,0,1,7,6</sub> |  | 1.9<br><sub>3,1,1,0,3</sub> |  | 1.0<br><sub>1,0,4,1,2</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 8.6 |
| Leonard Miller | 98% | 15.4<br><sub>24,21,14,17,11</sub> | 7.4<br><sub>19,7,9,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>3,4,9,0,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.7<br><sub>2,1,1,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.4 | 0.4 | 0.9 | 12.1 |
| Buddy Hield | 91% | 12.9<br><sub>15,16,13,9,17</sub> | 5.6<br><sub>13,9,3,2,5</sub> |  | 1.9<br><sub>2,2,0,3,3</sub> |  | 1.1<br><sub>2,2,1,1,1</sub> |  | 0.8<br><sub>3,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 8.5 |
| Noa Essengue | 88% | 12.4<br><sub>17,-,16,10,16</sub> | 4.3<br><sub>4,-,0,3,10</sub> |  | 2.2<br><sub>1,-,4,0,4</sub> |  | 0.5<br><sub>1,-,0,1,0</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.5 | 0.2 | 0.8 | 7.0 |
| Tobe Awaka | 60% | 11.5<br><sub>-,-,12,-,12</sub> | 3.8<br><sub>-,-,4,-,2</sub> |  | 4.2<br><sub>-,-,6,-,7</sub> |  | 0.7<br><sub>-,-,0,-,1</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.5 | 0.6 | 8.7 |
| Patrick Williams | 38% | 9.5<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 5.3 |
| Jordan Hawkins | 58% | 8.3<br><sub>-,-,7,-,6</sub> | 3.6<br><sub>-,-,4,-,0</sub> |  | 1.2<br><sub>-,-,1,-,0</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.4 |
| Zach Collins | 67% | 8.1<br><sub>-,11,6,-,2</sub> | 3.6<br><sub>-,2,2,-,0</sub> |  | 2.6<br><sub>-,3,2,-,0</sub> |  | 0.8<br><sub>-,1,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 7.0 |
| Dailyn Swain | 47% | 7.5<br><sub>-,-,12,-,-</sub> | 2.6<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,2,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.7 | 0.1 | 1.6 | 4.7 |
| Jaylin Sellers | 58% | 6.2<br><sub>-,-,12,-,3</sub> | 3.2<br><sub>-,-,0,-,3</sub> |  | 1.2<br><sub>-,-,0,-,0</sub> |  | 0.7<br><sub>-,-,1,-,1</sub> |  | 0.3<br><sub>-,-,0,-,1</sub> |  | 0.1 | 0.1 | 0.5 | 5.2 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 36.8<br><sub>36,34,36,38,38</sub> | 27.6<br><sub>26,29,27,27,38</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 4.2<br><sub>4,5,5,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 6.0<br><sub>4,4,4,4,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,1,3,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.8 | 0.7 | 2.5 | 37.9 |
| Jaylen Brown | 98% | 35.4<br><sub>35,40,34,-,38</sub> | 25.4<br><sub>27,16,20,-,16</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.6<br><sub>3,4,10,-,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>5,4,2,-,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,2,1,-,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.5 | 0.7 | 3.4 | 37.0 |
| LeBron James | 98% | 33.8<br><sub>-,33,33,34,-</sub> | 20.9<br><sub>-,18,13,20,-</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 7.0<br><sub>-,2,5,9,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 7.5<br><sub>-,5,10,8,-</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>-,0,2,2,-</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.7 | 2.8 | 35.4 |
| VJ Edgecombe | 88% | 32.8<br><sub>30,-,29,36,37</sub> | 14.0<br><sub>17,-,8,13,10</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.4<br><sub>13,-,7,8,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>2,-,2,2,3</sub> | 2.5<br><sub>o 62% · u 38%</sub> | 1.8<br><sub>5,-,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.6 | 0.5 | 1.6 | 24.2 |
| Dean Wade | 88% | 25.6<br><sub>28,37,17,27,30</sub> | 5.4<br><sub>7,7,0,0,4</sub> |  | 4.1<br><sub>2,5,1,2,5</sub> |  | 1.7<br><sub>0,1,1,1,10</sub> |  | 0.7<br><sub>2,1,0,0,0</sub> |  | 1.1 | 0.4 | 0.7 | 11.2 |
| Anfernee Simons | 97% | 25.3<br><sub>20,27,27,31,25</sub> | 12.2<br><sub>4,5,20,21,19</sub> |  | 2.5<br><sub>1,3,3,2,0</sub> |  | 2.1<br><sub>2,3,1,1,2</sub> |  | 2.1<br><sub>1,1,6,5,5</sub> |  | 0.9 | 0.2 | 1.2 | 16.8 |
| Kentavious Caldwell-Pope | 98% | 20.8<br><sub>28,31,21,21,18</sub> | 6.3<br><sub>12,7,4,5,3</sub> |  | 2.3<br><sub>2,3,2,3,2</sub> |  | 1.7<br><sub>1,3,1,3,1</sub> |  | 0.8<br><sub>4,1,0,1,1</sub> |  | 0.9 | 0.2 | 0.8 | 10.4 |
| Adem Bona | 97% | 16.9<br><sub>10,25,4,14,22</sub> | 4.7<br><sub>0,6,1,0,2</sub> |  | 4.6<br><sub>1,13,1,2,5</sub> |  | 0.7<br><sub>1,1,0,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 1.0 | 9.9 |
| Jabari Walker | 91% | 12.9<br><sub>12,-,-,-,19</sub> | 5.2<br><sub>6,-,-,-,12</sub> |  | 3.4<br><sub>3,-,-,-,6</sub> |  | 0.7<br><sub>1,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,1</sub> |  | 0.5 | 0.2 | 0.6 | 9.3 |
| Labaron Philon Jr. | 66% | 8.9<br><sub>4,13,-,6,10</sub> | 3.6<br><sub>0,5,-,2,5</sub> |  | 1.3<br><sub>0,2,-,2,1</sub> |  | 0.6<br><sub>0,1,-,0,0</sub> |  | 0.3<br><sub>0,1,-,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 5.5 |
| Tacko Fall | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Rayan Rupert | 23% | 8.2<br><sub>-,-,-,-,-</sub> | 2.9<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.1 | 0.5 | 4.9 |
| Justin Edwards | 52% | 7.7<br><sub>1,-,-,-,2</sub> | 3.3<br><sub>0,-,-,-,0</sub> |  | 1.1<br><sub>0,-,-,-,1</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.3 | 4.9 |
| Caleb Love | 35% | 6.7<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |

</details>

<details><summary>if Joel Embiid plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson (CHI) | 96% | 32.9<br><sub>33,38,32,38,31</sub> | 18.1<br><sub>21,30,17,20,23</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 6.5<br><sub>6,14,5,6,5</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.6<br><sub>1,3,3,4,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>2,1,1,3,6</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 1.4 | 2.9 | 27.2 |
| Norman Powell (CHI) | 98% | 30.1<br><sub>33,33,24,37,31</sub> | 18.3<br><sub>25,18,20,30,16</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>4,2,1,2,2</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>1,3,2,2,3</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 2.1<br><sub>2,3,4,4,1</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.2 | 2.2 | 23.8 |
| Josh Giddey (CHI) | 98% | 28.3<br><sub>25,30,24,31,25</sub> | 11.8<br><sub>6,9,11,10,13</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 7.2<br><sub>4,8,1,8,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 7.4<br><sub>9,10,4,11,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>0,1,1,1,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.6 | 3.0 | 26.3 |
| Matas Buzelis (CHI) | 98% | 25.9<br><sub>17,35,22,33,20</sub> | 14.0<br><sub>7,21,11,17,14</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>5,5,1,5,5</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>3,2,2,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>0,2,2,3,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.6 | 1.2 | 2.3 | 21.1 |
| Jalen Smith (CHI) | 91% | 24.1<br><sub>24,24,20,30,27</sub> | 11.5<br><sub>14,14,7,17,5</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 7.9<br><sub>13,3,6,11,12</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 1.3<br><sub>1,1,1,5,1</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,2,2,3,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.5 | 0.8 | 1.2 | 20.7 |
| Tre Jones (CHI) | 98% | 18.9<br><sub>24,18,15,18,20</sub> | 10.0<br><sub>11,10,8,11,12</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,2,1,4,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>8,3,0,3,4</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.8 | 0.1 | 1.2 | 15.9 |
| Isaac Okoro (CHI) | 98% | 17.3<br><sub>28,14,11,18,18</sub> | 5.7<br><sub>12,0,1,7,6</sub> |  | 1.9<br><sub>3,1,1,0,3</sub> |  | 1.0<br><sub>1,0,4,1,2</sub> |  | 0.6<br><sub>1,0,0,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 8.6 |
| Leonard Miller (CHI) | 98% | 15.3<br><sub>24,21,14,17,11</sub> | 7.3<br><sub>19,7,9,10,2</sub> | 8.5 · –<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>3,4,9,0,2</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>2,0,0,1,1</sub> |  | 0.7<br><sub>2,1,1,1,0</sub> | 0.5<br><sub>o 60% · u 40%</sub> | 0.4 | 0.4 | 0.9 | 11.9 |
| Buddy Hield (CHI) | 91% | 12.9<br><sub>15,16,13,9,17</sub> | 5.5<br><sub>13,9,3,2,5</sub> |  | 1.9<br><sub>2,2,0,3,3</sub> |  | 1.1<br><sub>2,2,1,1,1</sub> |  | 0.8<br><sub>3,1,1,0,1</sub> |  | 0.5 | 0.2 | 0.8 | 8.5 |
| Noa Essengue (CHI) | 88% | 12.4<br><sub>17,-,16,10,16</sub> | 4.3<br><sub>4,-,0,3,10</sub> |  | 2.1<br><sub>1,-,4,0,4</sub> |  | 0.5<br><sub>1,-,0,1,0</sub> |  | 0.4<br><sub>0,-,0,1,1</sub> |  | 0.5 | 0.2 | 0.8 | 6.9 |
| Tobe Awaka (CHI) | 60% | 11.3<br><sub>-,-,12,-,12</sub> | 3.7<br><sub>-,-,4,-,2</sub> |  | 4.2<br><sub>-,-,6,-,7</sub> |  | 0.7<br><sub>-,-,0,-,1</sub> |  | 0.0<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.5 | 0.6 | 8.6 |
| Patrick Williams (CHI) | 38% | 9.4<br><sub>-,-,-,-,-</sub> | 3.3<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 5.3 |
| Jordan Hawkins (CHI) | 58% | 8.3<br><sub>-,-,7,-,6</sub> | 3.5<br><sub>-,-,4,-,0</sub> |  | 1.1<br><sub>-,-,1,-,0</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.3 |
| Zach Collins (CHI) | 67% | 8.0<br><sub>-,11,6,-,2</sub> | 3.6<br><sub>-,2,2,-,0</sub> |  | 2.6<br><sub>-,3,2,-,0</sub> |  | 0.8<br><sub>-,1,0,-,0</sub> |  | 0.2<br><sub>-,0,0,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 7.0 |
| Dailyn Swain (CHI) | 47% | 7.5<br><sub>-,-,12,-,-</sub> | 2.6<br><sub>-,-,2,-,-</sub> |  | 1.0<br><sub>-,-,2,-,-</sub> |  | 1.1<br><sub>-,-,2,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.7 | 0.1 | 1.5 | 4.7 |
| Jaylin Sellers (CHI) | 58% | 6.3<br><sub>-,-,12,-,3</sub> | 3.3<br><sub>-,-,0,-,3</sub> |  | 1.3<br><sub>-,-,0,-,0</sub> |  | 0.7<br><sub>-,-,1,-,1</sub> |  | 0.3<br><sub>-,-,0,-,1</sub> |  | 0.1 | 0.1 | 0.5 | 5.3 |
| Tyrese Maxey (PHI) | 98% | 35.2<br><sub>36,34,36,38,38</sub> | 25.0<br><sub>26,29,27,27,38</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>4,5,5,4,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 5.6<br><sub>4,4,4,4,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>4,1,3,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.7 | 0.6 | 2.1 | 34.6 |
| Jaylen Brown (PHI) | 98% | 34.3<br><sub>35,40,34,-,38</sub> | 22.9<br><sub>27,16,20,-,16</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>3,4,10,-,4</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>5,4,2,-,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.9<br><sub>3,2,1,-,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.4 | 0.5 | 3.1 | 33.6 |
| Joel Embiid (PHI) | 100% | 32.8<br><sub>36,-,39,33,-</sub> | 24.5<br><sub>28,-,21,10,-</sub> | 21.5 · – | 8.9<br><sub>11,-,11,7,-</sub> | 8.5 | 5.0<br><sub>10,-,2,7,-</sub> | 4.5 | 1.3<br><sub>0,-,0,0,-</sub> | 1.5 | 0.9 | 1.3 | 2.8 | 38.5 |
| LeBron James (PHI) | 98% | 32.5<br><sub>-,33,33,34,-</sub> | 17.8<br><sub>-,18,13,20,-</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 6.9<br><sub>-,2,5,9,-</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 7.2<br><sub>-,5,10,8,-</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>-,0,2,2,-</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.4 | 0.7 | 2.6 | 31.9 |
| VJ Edgecombe (PHI) | 88% | 31.0<br><sub>30,-,29,36,37</sub> | 12.5<br><sub>17,-,8,13,10</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>13,-,7,8,8</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 3.8<br><sub>2,-,2,2,3</sub> | 2.5<br><sub>o 62% · u 38%</sub> | 1.7<br><sub>5,-,1,1,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.5 | 0.5 | 1.4 | 22.4 |
| Anfernee Simons (PHI) | 97% | 22.2<br><sub>20,27,27,31,25</sub> | 10.8<br><sub>4,5,20,21,19</sub> |  | 2.2<br><sub>1,3,3,2,0</sub> |  | 1.9<br><sub>2,3,1,1,2</sub> |  | 1.9<br><sub>1,1,6,5,5</sub> |  | 0.8 | 0.2 | 1.0 | 15.0 |
| Dean Wade (PHI) | 88% | 21.9<br><sub>28,37,17,27,30</sub> | 4.7<br><sub>7,7,0,0,4</sub> |  | 3.7<br><sub>2,5,1,2,5</sub> |  | 1.5<br><sub>0,1,1,1,10</sub> |  | 0.6<br><sub>2,1,0,0,0</sub> |  | 1.0 | 0.3 | 0.5 | 9.9 |
| Kentavious Caldwell-Pope (PHI) | 98% | 18.7<br><sub>28,31,21,21,18</sub> | 5.7<br><sub>12,7,4,5,3</sub> |  | 2.1<br><sub>2,3,2,3,2</sub> |  | 1.6<br><sub>1,3,1,3,1</sub> |  | 0.8<br><sub>4,1,0,1,1</sub> |  | 0.9 | 0.2 | 0.7 | 9.4 |
| Adem Bona (PHI) | 97% | 10.9<br><sub>10,25,4,14,22</sub> | 3.2<br><sub>0,6,1,0,2</sub> |  | 2.9<br><sub>1,13,1,2,5</sub> |  | 0.5<br><sub>1,1,0,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.8 | 0.6 | 6.6 |
| Jabari Walker (PHI) | 91% | 9.3<br><sub>12,-,-,-,19</sub> | 3.8<br><sub>6,-,-,-,12</sub> |  | 2.4<br><sub>3,-,-,-,6</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,1</sub> |  | 0.4 | 0.2 | 0.4 | 6.7 |
| Tacko Fall (PHI) | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.7 |
| Labaron Philon Jr. (PHI) | 66% | 7.0<br><sub>4,13,-,6,10</sub> | 2.7<br><sub>0,5,-,2,5</sub> |  | 1.0<br><sub>0,2,-,2,1</sub> |  | 0.4<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,1,-,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.1 |
| Caleb Love (PHI) | 35% | 6.2<br><sub>1,-,-,-,-</sub> | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 0.9 |
| Justin Edwards (PHI) | 52% | 6.1<br><sub>1,-,-,-,2</sub> | 2.6<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,1</sub> |  | 0.5<br><sub>0,-,-,-,0</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |
| Rayan Rupert (PHI) | 23% | 6.1<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 3.7 |

</details>


### SAC @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.2–123.6 | SAC 26% | 3.92 / 1.34 | DAL -9.5 | 237.5 | DAL -10.5 covers 47%; o232.5 61% |
| Expected (weighted by chance each plays) | 113.8–123.3 | SAC 25% | 4.05 / 1.33 | DAL -9.5 | 236.5 | DAL -10.5 covers 47%; o232.5 59% |
| if Zach LaVine plays | 115.0–122.8 | SAC 29% | 3.44 / 1.41 | DAL -7.5 | 237.5 | DAL -10.5 covers 43%; o232.5 61% |
| if Kyrie Irving plays | 113.1–125.1 | SAC 20% | 5.00 / 1.25 | DAL -12.5 | 238.5 | DAL -10.5 covers 54%; o232.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dylan Cardwell (SAC) | Questionable | 55% | 15.4 | 4.4 | 5.7 | 1.1 | 0.1 | 0.5 | 1.2 | 0.7 | 11.2 | small |
| Santi Aldama (DAL) | Doubtful | 20% | 18.3 | 8.5 | 4.4 | 1.8 | 0.9 | 0.7 | 0.4 | 0.9 | 14.7 | small |
| Zach LaVine (SAC) | Questionable | 55% | 33.3 | 20.4 | 3.5 | 2.8 | 2.1 | 0.9 | 0.2 | 2.1 | 26.7 | full tables below |
| Kyrie Irving (DAL) | Questionable | 55% | 31.6 | 23.3 | 4.1 | 4.8 | 2.8 | 1.3 | 0.5 | 2.0 | 32.3 | full tables below |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 96% | 37.4<br><sub>37,36,33,41,37</sub> | 28.8<br><sub>33,22,19,34,38</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>2,3,3,6,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>4,7,5,14,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>2,2,3,3,9</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.4 | 3.7 | 39.4 |
| Domantas Sabonis | 98% | 35.8<br><sub>39,35,37,40,38</sub> | 19.2<br><sub>27,15,20,9,11</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 14.6<br><sub>19,15,14,15,14</sub> | 13.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>10,3,8,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.1 | 0.4 | 2.9 | 40.6 |
| Precious Achiuwa | 98% | 33.5<br><sub>26,39,14,41,25</sub> | 16.6<br><sub>14,12,4,24,6</sub> | 11.5 · –<br><sub>o 56% · u 44%</sub> | 9.2<br><sub>6,10,1,9,5</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>1,0,0,2,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.4 | 1.1 | 1.6 | 27.8 |
| De'Andre Hunter | 98% | 32.2<br><sub>25,29,33,37,32</sub> | 15.7<br><sub>4,7,24,24,19</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 5.4<br><sub>7,6,6,5,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,2,1,0</sub> |  | 1.9<br><sub>0,2,5,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.6 | 23.0 |
| Jonathan Mogbo | 63% | 21.9<br><sub>-,18,18,-,25</sub> | 6.8<br><sub>-,7,2,-,6</sub> |  | 3.7<br><sub>-,3,5,-,3</sub> |  | 1.1<br><sub>-,1,0,-,3</sub> |  | 0.6<br><sub>-,1,0,-,0</sub> |  | 0.8 | 0.6 | 0.9 | 11.6 |
| Emanuel Sharp | 96% | 21.1<br><sub>14,14,20,18,24</sub> | 6.3<br><sub>5,3,5,0,2</sub> |  | 1.4<br><sub>0,1,0,0,1</sub> |  | 1.2<br><sub>1,0,2,0,1</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.3 | 0.8 | 8.9 |
| Daeqwon Plowden | 80% | 19.1<br><sub>20,16,17,-,4</sub> | 6.9<br><sub>3,3,0,-,4</sub> |  | 2.3<br><sub>0,3,2,-,0</sub> |  | 1.0<br><sub>0,1,0,-,0</sub> |  | 0.9<br><sub>1,1,0,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 10.2 |
| Malik Monk | 97% | 17.9<br><sub>12,12,13,8,14</sub> | 9.8<br><sub>0,6,3,2,8</sub> |  | 2.0<br><sub>1,1,2,1,0</sub> |  | 3.1<br><sub>2,2,6,1,3</sub> |  | 1.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 1.3 | 14.8 |
| Nique Clifford | 88% | 15.8<br><sub>2,-,5,4,11</sub> | 6.3<br><sub>0,-,2,0,0</sub> |  | 2.5<br><sub>0,-,0,0,1</sub> |  | 1.9<br><sub>0,-,0,1,2</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.7 | 0.2 | 0.9 | 10.7 |
| Alex Karaban | 67% | 13.7<br><sub>-,-,11,12,10</sub> | 4.3<br><sub>-,-,0,6,0</sub> |  | 1.9<br><sub>-,-,1,0,1</sub> |  | 0.7<br><sub>-,-,1,0,1</sub> |  | 0.4<br><sub>-,-,0,2,0</sub> |  | 0.4 | 0.2 | 0.8 | 7.0 |
| Leaky Black | 38% | 13.0<br><sub>-,-,8,-,-</sub> | 3.3<br><sub>-,-,2,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.4 | 0.5 | 6.6 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg | 98% | 34.4<br><sub>17,-,40,33,39</sub> | 29.2<br><sub>14,-,29,26,33</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,-,6,5,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>6,-,11,8,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,-,2,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 1.1 | 3.1 | 42.6 |
| P.J. Washington | 98% | 33.8<br><sub>33,36,41,27,34</sub> | 17.1<br><sub>20,12,20,18,3</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>13,4,9,9,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,2,2,0,1</sub> |  | 1.8<br><sub>2,0,4,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1 | 1.1 | 1.9 | 26.5 |
| Zaccharie Risacher | 91% | 30.3<br><sub>32,32,30,29,28</sub> | 10.9<br><sub>11,11,6,13,12</sub> |  | 6.0<br><sub>6,4,8,6,6</sub> |  | 1.9<br><sub>1,2,1,1,3</sub> |  | 1.4<br><sub>1,1,1,2,3</sub> |  | 1.3 | 1.2 | 1.2 | 18.8 |
| Naji Marshall | 67% | 26.8<br><sub>33,21,-,-,-</sub> | 16.1<br><sub>15,10,-,-,-</sub> |  | 4.0<br><sub>4,4,-,-,-</sub> |  | 4.2<br><sub>6,5,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.2 | 0.1 | 1.9 | 24.2 |
| Daniel Gafford | 98% | 26.4<br><sub>15,23,26,27,29</sub> | 13.0<br><sub>4,12,8,7,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 8.1<br><sub>3,9,9,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>5,2,3,2,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.9 | 1.8 | 1.4 | 23.0 |
| Max Christie | 98% | 26.2<br><sub>38,26,26,22,18</sub> | 11.8<br><sub>16,5,11,11,2</sub> | 7.5 · –<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>4,5,5,5,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>4,1,3,2,0</sub> |  | 1.9<br><sub>2,1,3,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 1.2 | 16.7 |
| Caleb Martin | 91% | 21.0<br><sub>-,-,-,14,25</sub> | 7.8<br><sub>-,-,-,10,8</sub> |  | 2.9<br><sub>-,-,-,2,0</sub> |  | 1.6<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,2,2</sub> |  | 0.9 | 0.4 | 0.9 | 12.3 |
| Marcus Sasser | 91% | 16.6<br><sub>27,27,8,22,7</sub> | 6.9<br><sub>6,12,0,10,0</sub> |  | 1.5<br><sub>2,3,1,1,0</sub> |  | 2.5<br><sub>3,5,0,4,1</sub> |  | 1.0<br><sub>2,2,0,1,0</sub> |  | 0.6 | 0.1 | 0.9 | 10.9 |
| Morez Johnson Jr. | 98% | 15.5<br><sub>17,12,15,18,17</sub> | 6.7<br><sub>8,6,6,10,2</sub> |  | 2.2<br><sub>6,1,2,6,2</sub> |  | 1.6<br><sub>0,2,1,3,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 10.5 |
| Walter Clayton Jr. | 76% | 13.4<br><sub>1,15,17,15,9</sub> | 5.4<br><sub>0,3,15,0,3</sub> |  | 2.2<br><sub>1,2,4,2,2</sub> |  | 2.9<br><sub>0,5,4,5,1</sub> |  | 0.5<br><sub>0,1,2,0,1</sub> |  | 0.4 | 0.2 | 0.9 | 10.6 |
| Moussa Cisse | 63% | 8.7<br><sub>1,7,-,3,-</sub> | 3.4<br><sub>3,4,-,0,-</sub> |  | 3.5<br><sub>1,4,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.7 | 0.5 | 7.1 |
| Jett Howard | 52% | 7.5<br><sub>-,4,-,3,-</sub> | 3.2<br><sub>-,5,-,0,-</sub> |  | 0.9<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,1,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.6 |
| Tobi Lawal | 52% | 6.7<br><sub>1,4,-,3,-</sub> | 2.3<br><sub>0,5,-,0,-</sub> |  | 1.2<br><sub>0,1,-,0,-</sub> |  | 0.7<br><sub>0,1,-,1,-</sub> |  | 0.1<br><sub>0,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |

</details>

<details><summary>if Kyrie Irving plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 32.6<br><sub>17,-,40,33,39</sub> | 25.9<br><sub>14,-,29,26,33</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>5,-,6,5,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 5.8<br><sub>6,-,11,8,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>2,-,2,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 1.0 | 2.8 | 38.2 |
| P.J. Washington (DAL) | 98% | 31.7<br><sub>33,36,41,27,34</sub> | 14.5<br><sub>20,12,20,18,3</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 7.0<br><sub>13,4,9,9,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 1.8<br><sub>0,2,2,0,1</sub> |  | 1.6<br><sub>2,0,4,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 1.0 | 1.7 | 23.2 |
| Kyrie Irving (DAL) | 100% | 31.6<br><sub>25,-,33,27,35</sub> | 23.3<br><sub>24,-,18,15,35</sub> | 20.5 · – | 4.1<br><sub>1,-,6,2,4</sub> | 3.5 | 4.8<br><sub>3,-,6,4,9</sub> | 5.5 | 2.8<br><sub>5,-,2,3,5</sub> | 2.5 | 1.3 | 0.5 | 2.0 | 32.3 |
| Zaccharie Risacher (DAL) | 91% | 27.5<br><sub>32,32,30,29,28</sub> | 9.6<br><sub>11,11,6,13,12</sub> |  | 5.5<br><sub>6,4,8,6,6</sub> |  | 1.8<br><sub>1,2,1,1,3</sub> |  | 1.2<br><sub>1,1,1,2,3</sub> |  | 1.2 | 1.1 | 1.2 | 16.9 |
| Naji Marshall (DAL) | 67% | 24.5<br><sub>33,21,-,-,-</sub> | 13.3<br><sub>15,10,-,-,-</sub> |  | 3.7<br><sub>4,4,-,-,-</sub> |  | 3.7<br><sub>6,5,-,-,-</sub> |  | 0.8<br><sub>0,1,-,-,-</sub> |  | 1.1 | 0.1 | 1.7 | 20.6 |
| Daniel Gafford (DAL) | 98% | 24.2<br><sub>15,23,26,27,29</sub> | 11.5<br><sub>4,12,8,7,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>3,9,9,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>5,2,3,2,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.8 | 1.6 | 1.2 | 20.6 |
| Max Christie (DAL) | 98% | 24.1<br><sub>38,26,26,22,18</sub> | 10.1<br><sub>16,5,11,11,2</sub> | 7.5 · –<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>4,5,5,5,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>4,1,3,2,0</sub> |  | 1.7<br><sub>2,1,3,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.7 | 0.3 | 1.0 | 14.7 |
| Caleb Martin (DAL) | 91% | 17.5<br><sub>-,-,-,14,25</sub> | 6.2<br><sub>-,-,-,10,8</sub> |  | 2.5<br><sub>-,-,-,2,0</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,2,2</sub> |  | 0.8 | 0.3 | 0.8 | 10.0 |
| Morez Johnson Jr. (DAL) | 98% | 13.2<br><sub>17,12,15,18,17</sub> | 5.4<br><sub>8,6,6,10,2</sub> |  | 1.9<br><sub>6,1,2,6,2</sub> |  | 1.4<br><sub>0,2,1,3,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.8 | 8.7 |
| Marcus Sasser (DAL) | 91% | 12.4<br><sub>27,27,8,22,7</sub> | 4.7<br><sub>6,12,0,10,0</sub> |  | 1.1<br><sub>2,3,1,1,0</sub> |  | 1.8<br><sub>3,5,0,4,1</sub> |  | 0.7<br><sub>2,2,0,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 7.6 |
| Walter Clayton Jr. (DAL) | 76% | 10.0<br><sub>1,15,17,15,9</sub> | 4.1<br><sub>0,3,15,0,3</sub> |  | 1.7<br><sub>1,2,4,2,2</sub> |  | 2.3<br><sub>0,5,4,5,1</sub> |  | 0.4<br><sub>0,1,2,0,1</sub> |  | 0.3 | 0.1 | 0.7 | 8.0 |
| Moussa Cisse (DAL) | 63% | 7.3<br><sub>1,7,-,3,-</sub> | 3.0<br><sub>3,4,-,0,-</sub> |  | 3.0<br><sub>1,4,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.6 | 0.4 | 6.2 |
| Jett Howard (DAL) | 52% | 6.0<br><sub>-,4,-,3,-</sub> | 2.8<br><sub>-,5,-,0,-</sub> |  | 0.7<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,1,-,0,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.0 |
| Tobi Lawal (DAL) | 52% | 5.9<br><sub>1,4,-,3,-</sub> | 2.2<br><sub>0,5,-,0,-</sub> |  | 1.0<br><sub>0,1,-,0,-</sub> |  | 0.6<br><sub>0,1,-,1,-</sub> |  | 0.1<br><sub>0,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Darius Acuff Jr. (SAC) | 96% | 37.3<br><sub>37,36,33,41,37</sub> | 28.6<br><sub>33,22,19,34,38</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>2,3,3,6,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>4,7,5,14,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.5<br><sub>2,2,3,3,9</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.4 | 3.7 | 39.3 |
| Domantas Sabonis (SAC) | 98% | 35.8<br><sub>39,35,37,40,38</sub> | 19.1<br><sub>27,15,20,9,11</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 14.6<br><sub>19,15,14,15,14</sub> | 13.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>10,3,8,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.1 | 0.4 | 2.9 | 40.5 |
| Precious Achiuwa (SAC) | 98% | 33.4<br><sub>26,39,14,41,25</sub> | 16.5<br><sub>14,12,4,24,6</sub> | 11.5 · –<br><sub>o 56% · u 44%</sub> | 9.2<br><sub>6,10,1,9,5</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,0,0,2,1</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.4 | 1.0 | 1.6 | 27.6 |
| De'Andre Hunter (SAC) | 98% | 32.2<br><sub>25,29,33,37,32</sub> | 15.6<br><sub>4,7,24,24,19</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 5.5<br><sub>7,6,6,5,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>1,1,2,1,0</sub> |  | 1.9<br><sub>0,2,5,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.7 | 23.0 |
| Jonathan Mogbo (SAC) | 63% | 21.9<br><sub>-,18,18,-,25</sub> | 6.7<br><sub>-,7,2,-,6</sub> |  | 3.7<br><sub>-,3,5,-,3</sub> |  | 1.1<br><sub>-,1,0,-,3</sub> |  | 0.6<br><sub>-,1,0,-,0</sub> |  | 0.8 | 0.6 | 0.9 | 11.6 |
| Emanuel Sharp (SAC) | 96% | 21.2<br><sub>14,14,20,18,24</sub> | 6.3<br><sub>5,3,5,0,2</sub> |  | 1.4<br><sub>0,1,0,0,1</sub> |  | 1.2<br><sub>1,0,2,0,1</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 0.7 | 0.3 | 0.8 | 8.9 |
| Daeqwon Plowden (SAC) | 80% | 19.1<br><sub>20,16,17,-,4</sub> | 6.8<br><sub>3,3,0,-,4</sub> |  | 2.3<br><sub>0,3,2,-,0</sub> |  | 1.0<br><sub>0,1,0,-,0</sub> |  | 0.9<br><sub>1,1,0,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 10.2 |
| Malik Monk (SAC) | 97% | 17.9<br><sub>12,12,13,8,14</sub> | 9.8<br><sub>0,6,3,2,8</sub> |  | 2.0<br><sub>1,1,2,1,0</sub> |  | 3.1<br><sub>2,2,6,1,3</sub> |  | 1.0<br><sub>0,0,1,0,0</sub> |  | 0.6 | 0.3 | 1.3 | 14.8 |
| Nique Clifford (SAC) | 88% | 16.0<br><sub>2,-,5,4,11</sub> | 6.3<br><sub>0,-,2,0,0</sub> |  | 2.5<br><sub>0,-,0,0,1</sub> |  | 2.0<br><sub>0,-,0,1,2</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 10.8 |
| Alex Karaban (SAC) | 67% | 13.7<br><sub>-,-,11,12,10</sub> | 4.3<br><sub>-,-,0,6,0</sub> |  | 1.9<br><sub>-,-,1,0,1</sub> |  | 0.7<br><sub>-,-,1,0,1</sub> |  | 0.4<br><sub>-,-,0,2,0</sub> |  | 0.4 | 0.2 | 0.8 | 7.0 |
| Leaky Black (SAC) | 38% | 13.0<br><sub>-,-,8,-,-</sub> | 3.4<br><sub>-,-,2,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 0.9<br><sub>-,-,1,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.6 | 0.4 | 0.5 | 6.7 |

</details>

<details><summary>if Zach LaVine plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cooper Flagg (DAL) | 98% | 34.3<br><sub>17,-,40,33,39</sub> | 29.1<br><sub>14,-,29,26,33</sub> | 25.5 · –<br><sub>o 50% · u 50%</sub> | 6.8<br><sub>5,-,6,5,9</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 6.5<br><sub>6,-,11,8,6</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>2,-,2,2,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 1.1 | 3.1 | 42.4 |
| P.J. Washington (DAL) | 98% | 33.8<br><sub>33,36,41,27,34</sub> | 17.1<br><sub>20,12,20,18,3</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 7.4<br><sub>13,4,9,9,10</sub> | 6.5<br><sub>o 54% · u 46%</sub> | 2.0<br><sub>0,2,2,0,1</sub> |  | 1.8<br><sub>2,0,4,2,1</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.1 | 1.1 | 1.9 | 26.6 |
| Zaccharie Risacher (DAL) | 91% | 30.4<br><sub>32,32,30,29,28</sub> | 11.0<br><sub>11,11,6,13,12</sub> |  | 6.0<br><sub>6,4,8,6,6</sub> |  | 1.9<br><sub>1,2,1,1,3</sub> |  | 1.4<br><sub>1,1,1,2,3</sub> |  | 1.3 | 1.2 | 1.2 | 18.8 |
| Naji Marshall (DAL) | 67% | 26.8<br><sub>33,21,-,-,-</sub> | 16.0<br><sub>15,10,-,-,-</sub> |  | 3.9<br><sub>4,4,-,-,-</sub> |  | 4.2<br><sub>6,5,-,-,-</sub> |  | 0.9<br><sub>0,1,-,-,-</sub> |  | 1.2 | 0.1 | 1.9 | 24.1 |
| Daniel Gafford (DAL) | 98% | 26.4<br><sub>15,23,26,27,29</sub> | 13.0<br><sub>4,12,8,7,18</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 8.1<br><sub>3,9,9,11,7</sub> | 7.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>5,2,3,2,2</sub> |  | 0.0<br><sub>0,0,0,1,0</sub> |  | 0.9 | 1.8 | 1.4 | 22.9 |
| Max Christie (DAL) | 98% | 26.2<br><sub>38,26,26,22,18</sub> | 11.7<br><sub>16,5,11,11,2</sub> | 7.5 · –<br><sub>o 56% · u 44%</sub> | 3.0<br><sub>4,5,5,5,1</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>4,1,3,2,0</sub> |  | 1.9<br><sub>2,1,3,3,0</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.8 | 0.3 | 1.2 | 16.6 |
| Caleb Martin (DAL) | 91% | 21.0<br><sub>-,-,-,14,25</sub> | 7.7<br><sub>-,-,-,10,8</sub> |  | 3.0<br><sub>-,-,-,2,0</sub> |  | 1.6<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,2,2</sub> |  | 0.9 | 0.4 | 0.9 | 12.3 |
| Marcus Sasser (DAL) | 91% | 16.6<br><sub>27,27,8,22,7</sub> | 7.0<br><sub>6,12,0,10,0</sub> |  | 1.5<br><sub>2,3,1,1,0</sub> |  | 2.5<br><sub>3,5,0,4,1</sub> |  | 1.0<br><sub>2,2,0,1,0</sub> |  | 0.6 | 0.1 | 0.9 | 11.0 |
| Morez Johnson Jr. (DAL) | 98% | 15.5<br><sub>17,12,15,18,17</sub> | 6.7<br><sub>8,6,6,10,2</sub> |  | 2.2<br><sub>6,1,2,6,2</sub> |  | 1.6<br><sub>0,2,1,3,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 1.0 | 10.4 |
| Walter Clayton Jr. (DAL) | 76% | 13.5<br><sub>1,15,17,15,9</sub> | 5.4<br><sub>0,3,15,0,3</sub> |  | 2.3<br><sub>1,2,4,2,2</sub> |  | 2.9<br><sub>0,5,4,5,1</sub> |  | 0.5<br><sub>0,1,2,0,1</sub> |  | 0.4 | 0.2 | 0.9 | 10.7 |
| Moussa Cisse (DAL) | 63% | 8.7<br><sub>1,7,-,3,-</sub> | 3.4<br><sub>3,4,-,0,-</sub> |  | 3.5<br><sub>1,4,-,0,-</sub> |  | 0.2<br><sub>0,0,-,0,-</sub> |  | 0.0<br><sub>0,0,-,0,-</sub> |  | 0.3 | 0.7 | 0.5 | 7.1 |
| Jett Howard (DAL) | 52% | 7.5<br><sub>-,4,-,3,-</sub> | 3.2<br><sub>-,5,-,0,-</sub> |  | 0.9<br><sub>-,0,-,0,-</sub> |  | 0.5<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,1,-,0,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.7 |
| Tobi Lawal (DAL) | 52% | 6.8<br><sub>1,4,-,3,-</sub> | 2.3<br><sub>0,5,-,0,-</sub> |  | 1.1<br><sub>0,1,-,0,-</sub> |  | 0.7<br><sub>0,1,-,1,-</sub> |  | 0.1<br><sub>0,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.1 |
| Darius Acuff Jr. (SAC) | 96% | 35.7<br><sub>37,36,33,41,37</sub> | 24.1<br><sub>33,22,19,34,38</sub> | 24.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,3,3,6,5</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 5.8<br><sub>4,7,5,14,5</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 2.2<br><sub>2,2,3,3,9</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.1 | 0.4 | 3.4 | 34.4 |
| Domantas Sabonis (SAC) | 98% | 34.4<br><sub>39,35,37,40,38</sub> | 17.5<br><sub>27,15,20,9,11</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 13.7<br><sub>19,15,14,15,14</sub> | 13.5<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>10,3,8,7,8</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>1,0,0,0,0</sub> |  | 1.0 | 0.4 | 2.7 | 37.3 |
| Zach LaVine (SAC) | 100% | 33.3<br><sub>39,40,31,39,21</sub> | 20.4<br><sub>22,37,22,21,11</sub> | 21.5 · – | 3.5<br><sub>5,2,3,3,0</sub> | 2.5 | 2.8<br><sub>1,5,3,5,1</sub> | 2.5 | 2.1<br><sub>3,3,3,3,0</sub> | 2.5 | 0.9 | 0.2 | 2.1 | 26.7 |
| Precious Achiuwa (SAC) | 98% | 31.9<br><sub>26,39,14,41,25</sub> | 14.8<br><sub>14,12,4,24,6</sub> | 11.5 · –<br><sub>o 56% · u 44%</sub> | 8.5<br><sub>6,10,1,9,5</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.8<br><sub>1,0,0,2,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 1.4 | 1.0 | 1.4 | 25.2 |
| De'Andre Hunter (SAC) | 98% | 28.7<br><sub>25,29,33,37,32</sub> | 13.4<br><sub>4,7,24,24,19</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>7,6,6,5,3</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>1,1,2,1,0</sub> |  | 1.5<br><sub>0,2,5,4,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.3 | 19.9 |
| Jonathan Mogbo (SAC) | 63% | 18.2<br><sub>-,18,18,-,25</sub> | 5.5<br><sub>-,7,2,-,6</sub> |  | 3.0<br><sub>-,3,5,-,3</sub> |  | 1.0<br><sub>-,1,0,-,3</sub> |  | 0.4<br><sub>-,1,0,-,0</sub> |  | 0.7 | 0.4 | 0.8 | 9.5 |
| Emanuel Sharp (SAC) | 96% | 16.7<br><sub>14,14,20,18,24</sub> | 5.0<br><sub>5,3,5,0,2</sub> |  | 1.1<br><sub>0,1,0,0,1</sub> |  | 0.9<br><sub>1,0,2,0,1</sub> |  | 0.5<br><sub>1,1,1,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 7.0 |
| Malik Monk (SAC) | 97% | 14.8<br><sub>12,12,13,8,14</sub> | 7.4<br><sub>0,6,3,2,8</sub> |  | 1.6<br><sub>1,1,2,1,0</sub> |  | 2.6<br><sub>2,2,6,1,3</sub> |  | 0.7<br><sub>0,0,1,0,0</sub> |  | 0.5 | 0.3 | 1.0 | 11.6 |
| Daeqwon Plowden (SAC) | 80% | 13.5<br><sub>20,16,17,-,4</sub> | 4.3<br><sub>3,3,0,-,4</sub> |  | 1.6<br><sub>0,3,2,-,0</sub> |  | 0.7<br><sub>0,1,0,-,0</sub> |  | 0.5<br><sub>1,1,0,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.6 |
| Nique Clifford (SAC) | 88% | 11.4<br><sub>2,-,5,4,11</sub> | 4.5<br><sub>0,-,2,0,0</sub> |  | 1.7<br><sub>0,-,0,0,1</sub> |  | 1.3<br><sub>0,-,0,1,2</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.2 | 0.7 | 7.4 |
| Alex Karaban (SAC) | 67% | 11.4<br><sub>-,-,11,12,10</sub> | 3.6<br><sub>-,-,0,6,0</sub> |  | 1.7<br><sub>-,-,1,0,1</sub> |  | 0.6<br><sub>-,-,1,0,1</sub> |  | 0.2<br><sub>-,-,0,2,0</sub> |  | 0.4 | 0.2 | 0.6 | 5.9 |
| Leaky Black (SAC) | 38% | 9.1<br><sub>-,-,8,-,-</sub> | 2.4<br><sub>-,-,2,-,-</sub> |  | 1.6<br><sub>-,-,1,-,-</sub> |  | 0.6<br><sub>-,-,1,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.2 | 0.3 | 4.6 |

</details>


### NOP @ MEM
Out: Yves Missi (NOP), Jordan Poole (NOP)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dejounte Murray 3PM over 1.5 (2+) | NOP @ MEM | draftkings | 2.43 | 2.40 | 1.98 | 50.6% | 38.7% | 41.7% | +1.3% | +23.0% | 0.2% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.6–122.1 | NOP 40% | 2.48 / 1.68 | MEM -3.5 | 240.5 | MEM -5.5 covers 45%; o233.5 64% |
| Expected (weighted by chance each plays) | 118.3–122.1 | NOP 39% | 2.57 / 1.64 | MEM -4.5 | 239.5 | MEM -5.5 covers 46%; o233.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scotty Pippen Jr. (MEM) | Doubtful | 20% | 12.0 | 5.7 | 1.7 | 2.2 | 0.5 | 0.8 | 0.2 | 1.1 | 9.6 | small |
| Quinten Post (MEM) | Questionable | 55% | 8.2 | 3.6 | 1.7 | 0.5 | 0.3 | 0.2 | 0.3 | 0.5 | 5.7 | small |
| Jaron Pierre Jr. (NOP) | Doubtful | 20% | 8.6 | 3.5 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |
| Malik Dia (NOP) | Doubtful | 20% | 8.6 | 3.6 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 5.9 | small |

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 91% | 33.2<br><sub>31,37,30,32,29</sub> | 18.3<br><sub>9,26,6,19,15</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 5.3<br><sub>6,6,1,5,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 3.5<br><sub>3,4,3,3,5</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.4<br><sub>1,4,2,2,1</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.6 | 1.8 | 27.2 |
| Dejounte Murray | 98% | 31.6<br><sub>30,35,30,-,-</sub> | 17.6<br><sub>16,22,10,-,-</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>6,6,8,-,-</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>6,6,5,-,-</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.7<br><sub>0,1,0,-,-</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.9 | 0.5 | 3.3 | 30.8 |
| Zion Williamson | 96% | 31.4<br><sub>33,33,32,31,30</sub> | 19.4<br><sub>23,17,25,22,15</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 6.0<br><sub>5,1,5,6,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>2,2,2,2,4</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.1<br><sub>0,0,1,0,0</sub> |  | 1.4 | 0.8 | 2.5 | 28.7 |
| Jeremiah Fears | 98% | 27.3<br><sub>24,23,24,29,31</sub> | 14.7<br><sub>7,10,11,22,20</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>0,6,4,8,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 4.4<br><sub>1,2,3,13,7</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,0,1,3,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.3 | 0.6 | 2.4 | 23.4 |
| Saddiq Bey | 96% | 26.1<br><sub>22,25,26,24,26</sub> | 14.1<br><sub>20,14,9,10,25</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>3,4,0,4,6</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.0<br><sub>1,3,3,3,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.5<br><sub>3,2,1,1,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.9 | 0.2 | 1.2 | 20.7 |
| Derik Queen | 98% | 22.9<br><sub>29,25,25,22,23</sub> | 10.3<br><sub>12,17,11,9,8</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>7,8,12,2,8</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>2,2,1,3,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.3<br><sub>1,0,0,1,0</sub> |  | 1.0 | 0.9 | 2.1 | 20.2 |
| Herbert Jones | 96% | 22.6<br><sub>18,16,19,32,25</sub> | 7.5<br><sub>3,2,4,16,11</sub> |  | 2.8<br><sub>1,3,2,4,3</sub> |  | 1.9<br><sub>0,1,0,1,2</sub> |  | 0.9<br><sub>1,0,0,0,1</sub> |  | 1.3 | 0.5 | 1.1 | 12.2 |
| Bennedict Mathurin | 98% | 17.7<br><sub>15,20,14,19,19</sub> | 8.7<br><sub>4,9,5,10,7</sub> | 9.5 · –<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>2,4,1,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.6<br><sub>0,4,2,2,2</sub> |  | 0.6<br><sub>0,1,1,2,1</sub> |  | 0.6 | 0.2 | 1.3 | 13.5 |
| Karlo Matkovic | 88% | 16.5<br><sub>9,8,18,28,18</sub> | 6.4<br><sub>7,3,5,12,8</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 4.3<br><sub>4,0,3,4,10</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 0.8<br><sub>1,0,1,1,1</sub> |  | 0.6<br><sub>0,1,1,1,2</sub> | 0.5<br><sub>o 51% · u 49%</sub> | 0.6 | 1.1 | 0.8 | 11.6 |
| Trendon Watford | 52% | 14.6<br><sub>-,-,-,17,18</sub> | 6.0<br><sub>-,-,-,8,7</sub> |  | 2.7<br><sub>-,-,-,1,4</sub> |  | 1.5<br><sub>-,-,-,2,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.4 | 1.1 | 10.2 |
| DeAndre Jordan | 47% | 11.6<br><sub>-,20,13,-,-</sub> | 3.4<br><sub>-,9,3,-,-</sub> |  | 4.7<br><sub>-,9,4,-,-</sub> |  | 0.7<br><sub>-,2,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.7 | 0.6 | 8.7 |
| Bryce McGowens | 67% | 11.0<br><sub>-,-,3,6,15</sub> | 4.0<br><sub>-,-,0,4,3</sub> |  | 1.3<br><sub>-,-,0,1,0</sub> |  | 0.8<br><sub>-,-,0,2,1</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 6.1 |
| AJ Johnson | 38% | 5.8<br><sub>-,-,-,-,3</sub> | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.8 | 1.0 | 1.0 |
| Julian Reese | 45% | 5.7<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.9 | 3.8 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 96% | 30.7<br><sub>37,31,31,28,26</sub> | 17.1<br><sub>25,14,13,18,27</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 9.0<br><sub>13,11,7,12,9</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 5.8<br><sub>6,4,4,12,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>4,2,1,4,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.7 | 2.6 | 32.0 |
| Ty Jerome | 98% | 26.8<br><sub>32,32,30,24,-</sub> | 20.1<br><sub>28,31,15,10,-</sub> | 22.5 · –<br><sub>o 45% · u 55%</sub> | 3.3<br><sub>2,4,1,2,-</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 5.9<br><sub>5,7,8,3,-</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>3,1,1,1,-</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.2 | 0.3 | 2.1 | 29.3 |
| Cedric Coward | 98% | 25.8<br><sub>-,32,31,27,23</sub> | 12.2<br><sub>-,17,16,17,10</sub> | 13.5 · –<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>-,11,11,7,7</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>-,1,3,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.5<br><sub>-,3,4,3,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.5 | 1.6 | 21.2 |
| Jaylen Wells | 98% | 25.4<br><sub>25,33,30,25,22</sub> | 11.1<br><sub>17,16,14,10,4</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>4,5,3,1,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,3,0,0,0</sub> |  | 1.6<br><sub>4,2,2,2,0</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.8 | 0.1 | 0.8 | 15.7 |
| Jerami Grant | 98% | 23.2<br><sub>26,22,24,27,23</sub> | 11.0<br><sub>6,5,13,2,14</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>0,5,3,1,2</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>3,3,0,3,1</sub> |  | 1.3<br><sub>1,1,3,0,1</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 0.7 | 1.4 | 15.4 |
| Zach Edey | 98% | 20.5<br><sub>22,-,21,19,18</sub> | 8.6<br><sub>8,-,4,13,4</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.8<br><sub>10,-,3,7,6</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.1<br><sub>3,-,2,0,0</sub> |  | 0.1<br><sub>0,-,0,1,0</sub> |  | 0.5 | 1.8 | 1.3 | 17.6 |
| Cam Spencer | 96% | 19.1<br><sub>17,16,18,23,25</sub> | 8.2<br><sub>11,13,8,8,10</sub> |  | 2.5<br><sub>2,2,5,6,5</sub> |  | 5.0<br><sub>1,1,5,8,13</sub> |  | 1.2<br><sub>3,3,2,1,2</sub> |  | 0.7 | 0.2 | 1.0 | 15.7 |
| Javon Small | 88% | 18.3<br><sub>-,-,-,-,20</sub> | 7.7<br><sub>-,-,-,-,7</sub> |  | 2.8<br><sub>-,-,-,-,1</sub> |  | 3.2<br><sub>-,-,-,-,5</sub> |  | 0.9<br><sub>-,-,-,-,2</sub> |  | 0.8 | 0.2 | 1.3 | 13.8 |
| GG Jackson | 96% | 16.6<br><sub>15,10,16,21,21</sub> | 9.3<br><sub>2,1,4,12,21</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>4,3,1,7,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,0,2,2,2</sub> |  | 0.9<br><sub>0,0,0,2,5</sub> | 0.5<br><sub>o 63% · u 37%</sub> | 0.5 | 0.6 | 1.2 | 14.0 |
| Isaiah Stewart | 98% | 15.0<br><sub>16,22,15,16,21</sub> | 7.0<br><sub>4,13,4,18,24</sub> | 8.5 · –<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>2,5,4,3,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 0.8<br><sub>0,2,0,0,0</sub> |  | 0.6<br><sub>0,2,0,2,2</sub> |  | 0.3 | 1.1 | 0.8 | 11.2 |
| Kris Murray | 63% | 11.0<br><sub>13,-,-,3,21</sub> | 3.2<br><sub>0,-,-,0,2</sub> |  | 1.6<br><sub>3,-,-,1,1</sub> |  | 0.8<br><sub>1,-,-,0,1</sub> |  | 0.2<br><sub>0,-,-,0,0</sub> |  | 0.5 | 0.2 | 0.4 | 5.6 |
| Jahmai Mashack | 52% | 9.5<br><sub>-,-,-,-,4</sub> | 3.0<br><sub>-,-,-,-,2</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.7 | 5.4 |
| Olivier-Maxence Prosper | 52% | 8.4<br><sub>-,-,-,3,4</sub> | 4.7<br><sub>-,-,-,4,2</sub> |  | 1.6<br><sub>-,-,-,1,1</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.4 | 6.8 |
| Taylor Hendricks | 64% | 7.6<br><sub>-,7,-,3,4</sub> | 3.2<br><sub>-,0,-,0,6</sub> |  | 1.5<br><sub>-,1,-,1,1</sub> |  | 0.4<br><sub>-,0,-,0,0</sub> |  | 0.3<br><sub>-,0,-,0,2</sub> |  | 0.5 | 0.3 | 0.3 | 5.0 |
| Karim Lopez | 58% | 6.2<br><sub>-,-,-,3,4</sub> | 2.5<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,1,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.5 | 0.3 | 4.2 |
| Carson Cooper | 58% | 5.4<br><sub>-,-,-,-,3</sub> | 2.1<br><sub>-,-,-,-,1</sub> |  | 2.4<br><sub>-,-,-,-,2</sub> |  | 0.8<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.3 | 0.9 | 5.4 |

</details>


### MIL @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro PA under 25.5 | MIL @ MIN | draftkings | 1.95 | 1.94 | 1.61 | 62.1% | 47.9% | 51.4% | +0.4% | +21.2% | 0.1% |

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.4<br><sub>32,31,32,27,27</sub> | 19.5<br><sub>34,13,23,23,15</sub> | 21.5 · –<br><sub>o 45% · u 55%</sub> | 4.8<br><sub>5,6,10,3,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>4,3,7,0,2</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>5,1,3,4,4</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.0 | 0.3 | 2.4 | 28.7 |
| Ryan Rollins | 98% | 28.7<br><sub>34,25,32,17,26</sub> | 14.2<br><sub>11,15,19,4,9</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 4.3<br><sub>7,4,2,4,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 5.2<br><sub>6,4,4,5,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 1.7<br><sub>2,2,3,0,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.3 | 2.4 | 23.7 |
| Jaime Jaquez Jr. | 98% | 26.2<br><sub>35,27,25,27,23</sub> | 13.4<br><sub>19,21,8,19,8</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 5.1<br><sub>11,8,6,4,7</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 3.7<br><sub>5,4,0,2,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.0<br><sub>2,2,0,3,1</sub> | 0.5<br><sub>o 64% · u 36%</sub> | 0.7 | 0.2 | 2.2 | 22.2 |
| Kyle Kuzma | 98% | 26.0<br><sub>30,35,29,18,23</sub> | 10.8<br><sub>14,14,17,4,14</sub> | 11.5 · –<br><sub>o 46% · u 54%</sub> | 5.0<br><sub>9,12,7,6,3</sub> | 5.5<br><sub>o 44% · u 56%</sub> | 2.7<br><sub>4,3,3,1,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.1<br><sub>2,0,4,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.4 | 1.9 | 18.6 |
| Myles Turner | 98% | 23.7<br><sub>30,20,28,22,24</sub> | 9.3<br><sub>12,0,6,4,10</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>3,5,9,2,7</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>1,1,4,2,2</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>2,0,0,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.7 | 1.8 | 1.3 | 15.4 |
| Kasparas Jakucionis | 88% | 18.9<br><sub>23,25,21,19,21</sub> | 6.3<br><sub>7,12,7,4,5</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.4<br><sub>2,3,4,2,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 3.0<br><sub>5,2,5,6,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 0.5<br><sub>1,0,1,0,1</sub> |  | 0.7 | 0.2 | 1.5 | 11.7 |
| Kel'el Ware | 88% | 18.6<br><sub>15,29,19,17,24</sub> | 9.5<br><sub>11,19,16,6,19</sub> |  | 6.0<br><sub>4,13,14,8,10</sub> |  | 0.9<br><sub>0,1,0,0,3</sub> |  | 0.8<br><sub>1,2,0,0,3</sub> |  | 0.7 | 0.6 | 1.4 | 16.4 |
| AJ Green | 98% | 17.7<br><sub>17,19,20,24,20</sub> | 5.7<br><sub>11,11,3,9,0</sub> |  | 1.9<br><sub>1,3,4,1,3</sub> |  | 1.1<br><sub>0,0,3,2,2</sub> |  | 0.9<br><sub>3,3,1,3,0</sub> |  | 0.4 | 0.1 | 0.6 | 8.8 |
| Cormac Ryan | 23% | 17.4 | 7.8 |  | 2.1 |  | 1.1 |  | 0.9 |  | 0.7 | 0.2 | 1.1 | 11.1 |
| Brayden Burries | 96% | 15.0<br><sub>8,17,16,17,21</sub> | 6.2<br><sub>3,10,4,10,14</sub> |  | 2.7<br><sub>1,5,2,5,3</sub> |  | 1.3<br><sub>3,2,1,1,1</sub> |  | 0.5<br><sub>1,1,0,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 10.3 |
| Nate Ament | 76% | 12.0<br><sub>-,11,14,20,19</sub> | 4.7<br><sub>-,1,7,8,14</sub> |  | 2.1<br><sub>-,3,3,4,1</sub> |  | 0.6<br><sub>-,0,0,0,2</sub> |  | 0.4<br><sub>-,0,1,1,2</sub> |  | 0.4 | 0.2 | 0.8 | 7.4 |
| Caris LeVert | 25% | 11.1<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.7 | 6.8 |
| Gary Trent Jr. | 58% | 9.4<br><sub>-,-,-,7,6</sub> | 3.7<br><sub>-,-,-,3,3</sub> |  | 0.7<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,0,1</sub> |  | 0.5<br><sub>-,-,-,1,1</sub> |  | 0.3 | 0.0 | 0.3 | 4.9 |
| Ousmane Dieng | 88% | 9.2<br><sub>16,-,3,13,6</sub> | 2.9<br><sub>3,-,0,4,0</sub> |  | 1.4<br><sub>1,-,0,0,1</sub> |  | 1.1<br><sub>1,-,0,0,2</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.7 | 5.5 |
| Jericho Sims | 52% | 9.0<br><sub>-,-,-,7,-</sub> | 2.9<br><sub>-,-,-,0,-</sub> |  | 2.7<br><sub>-,-,-,0,-</sub> |  | 0.8<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.6 | 6.5 |
| Pete Nance | 25% | 8.8 | 2.6 |  | 1.4 |  | 0.5 |  | 0.2 |  | 0.2 | 0.2 | 0.3 | 4.6 |
| Kam Jones | 23% | 8.5 | 2.5 |  | 0.9 |  | 1.6 |  | 0.1 |  | 0.3 | 0.1 | 0.6 | 5.1 |
| Bogoljub Markovic | 38% | 6.2<br><sub>-,-,-,5,-</sub> | 2.5<br><sub>-,-,-,2,-</sub> |  | 1.4<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 33.7<br><sub>31,37,35,33,39</sub> | 18.0<br><sub>14,14,19,23,19</sub> | 17.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>6,6,7,6,3</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>3,4,4,7,3</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.5<br><sub>1,2,1,1,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.9 | 1.7 | 27.0 |
| Jonathan Kuminga | 98% | 31.5<br><sub>26,36,32,22,40</sub> | 15.1<br><sub>13,10,20,5,19</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>4,10,3,1,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.7<br><sub>1,1,5,0,3</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>3,0,3,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.6 | 1.6 | 23.5 |
| Ayo Dosunmu | 98% | 30.7<br><sub>23,26,32,30,38</sub> | 16.6<br><sub>9,9,17,15,27</sub> | 16.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>3,1,3,7,9</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.5<br><sub>3,0,4,2,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>1,1,3,3,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.3 | 1.7 | 25.6 |
| Rudy Gobert | 98% | 29.1<br><sub>31,36,20,30,-</sub> | 9.9<br><sub>8,5,1,9,-</sub> | 9.5 · –<br><sub>o 52% · u 48%</sub> | 11.0<br><sub>13,20,4,13,-</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>0,2,1,4,-</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.0<br><sub>0,0,0,0,-</sub> |  | 1.0 | 1.3 | 1.2 | 22.7 |
| LaMelo Ball | 98% | 25.4<br><sub>17,31,28,29,20</sub> | 17.7<br><sub>15,11,8,24,10</sub> | 21.5 · –<br><sub>o 43% · u 57%</sub> | 3.9<br><sub>1,0,4,4,8</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 6.3<br><sub>8,6,8,7,4</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,1,2,6,0</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.4 | 0.2 | 2.7 | 27.9 |
| Terrence Shannon Jr. | 98% | 22.3<br><sub>23,24,27,20,18</sub> | 12.4<br><sub>15,14,19,11,2</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>4,4,6,3,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>3,5,2,2,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.4<br><sub>3,3,1,2,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.6 | 0.1 | 1.1 | 17.5 |
| Joan Beringer | 93% | 21.4<br><sub>13,17,20,18,34</sub> | 10.2<br><sub>6,12,7,4,12</sub> | 7.5 · –<br><sub>o 53% · u 47%</sub> | 7.0<br><sub>6,7,9,4,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 0.9<br><sub>0,0,2,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.5 | 0.9 | 18.1 |
| Trey Lyles | 98% | 17.3<br><sub>14,13,22,17,17</sub> | 6.3<br><sub>3,3,7,10,6</sub> |  | 3.8<br><sub>6,1,3,5,0</sub> |  | 1.1<br><sub>2,1,1,0,0</sub> |  | 0.8<br><sub>1,1,1,1,1</sub> |  | 0.6 | 0.2 | 0.6 | 11.1 |
| Bones Hyland | 96% | 15.4<br><sub>15,5,16,20,14</sub> | 8.7<br><sub>3,0,13,19,6</sub> |  | 1.8<br><sub>3,1,1,0,1</sub> |  | 2.8<br><sub>2,2,3,8,3</sub> |  | 1.4<br><sub>0,0,3,3,0</sub> |  | 0.7 | 0.2 | 0.9 | 13.3 |
| Jaylen Clark | 86% | 15.2<br><sub>5,-,7,17,20</sub> | 5.7<br><sub>3,-,3,5,10</sub> |  | 1.9<br><sub>1,-,2,0,2</sub> |  | 1.1<br><sub>0,-,1,2,1</sub> |  | 0.6<br><sub>0,-,1,1,2</sub> |  | 0.9 | 0.2 | 0.4 | 8.8 |
| Zyon Pullin | 52% | 6.9<br><sub>5,-,-,2,-</sub> | 3.0<br><sub>2,-,-,2,-</sub> |  | 0.8<br><sub>1,-,-,0,-</sub> |  | 1.0<br><sub>0,-,-,0,-</sub> |  | 0.1<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Rocco Zikarsky | 16% | 6.3 | 2.2 |  | 2.0 |  | 0.4 |  | 0.0 |  | 0.2 | 0.6 | 0.3 | 4.6 |
| Enrique Freeman | 16% | 6.3 | 1.9 |  | 1.4 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Isaiah Evans | 52% | 6.0<br><sub>4,-,-,2,-</sub> | 0.3<br><sub>0,-,-,0,-</sub> |  | 1.1<br><sub>0,-,-,0,-</sub> |  | 0.5<br><sub>1,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 2.0 |
| Cody Williams | 52% | 6.0<br><sub>5,-,-,2,-</sub> | 0.3<br><sub>0,-,-,0,-</sub> |  | 0.2<br><sub>0,-,-,0,-</sub> |  | 0.4<br><sub>0,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 0.9 |

</details>


### BOS @ HOU
Out: Steven Adams (HOU), Devin Carter (BOS)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.8–109.2 | BOS 49% | 2.03 / 1.97 | HOU +0.5 | 217.5 | HOU -4.5 covers 39%; o218.5 48% |
| Expected (weighted by chance each plays) | 108.4–109.2 | BOS 48% | 2.09 / 1.91 | HOU -1.5 | 217.5 | HOU -4.5 covers 40%; o218.5 48% |
| if Reed Sheppard plays | 108.8–110.0 | BOS 47% | 2.15 / 1.87 | HOU -1.5 | 218.5 | HOU -4.5 covers 41%; o218.5 50% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Mitchell Robinson (BOS) | Day-To-Day | 70% | 16.6 | 4.9 | 5.6 | 0.6 | 0.0 | 0.7 | 0.8 | 0.7 | 11.0 | small |
| Reed Sheppard (HOU) | Questionable | 55% | 24.1 | 10.6 | 2.4 | 3.1 | 1.9 | 1.3 | 0.5 | 1.1 | 16.1 | full tables below |
| Clint Capela (HOU) | Questionable | 55% | 15.2 | 4.2 | 5.0 | 1.0 | 0.0 | 0.5 | 0.8 | 0.6 | 10.2 | small |

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 36.8<br><sub>37,28,42,35,34</sub> | 26.4<br><sub>36,23,40,26,32</sub> | 26.5 · –<br><sub>o 46% · u 54%</sub> | 8.5<br><sub>9,7,5,7,4</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>7,6,8,7,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,2,2,2,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.4 | 2.9 | 40.8 |
| Derrick White | 98% | 33.4<br><sub>33,18,33,26,34</sub> | 13.4<br><sub>12,5,16,9,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>4,6,5,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.1<br><sub>6,4,7,4,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.9 | 1.7 | 21.3 |
| Paul George | 98% | 33.2<br><sub>34,25,36,27,33</sub> | 18.7<br><sub>15,16,20,18,17</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>7,5,7,6,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,7,8,8</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,1,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.4 | 2.2 | 27.0 |
| Payton Pritchard | 98% | 30.3<br><sub>30,22,24,35,27</sub> | 15.1<br><sub>4,28,4,30,7</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>1,1,2,3,7</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>4,4,6,3,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,7,0,3,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.3 | 22.2 |
| Neemias Queta | 98% | 23.5<br><sub>22,19,15,20,27</sub> | 8.9<br><sub>15,7,7,13,8</sub> |  | 7.1<br><sub>6,5,3,6,8</sub> |  | 1.3<br><sub>1,1,2,0,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.7 | 1.2 | 1.1 | 17.2 |
| Sam Hauser | 98% | 20.6<br><sub>23,20,25,18,17</sub> | 6.8<br><sub>6,11,11,6,3</sub> |  | 3.0<br><sub>2,4,4,3,2</sub> |  | 0.9<br><sub>2,1,0,2,0</sub> |  | 1.2<br><sub>2,3,3,2,1</sub> |  | 0.4 | 0.2 | 0.4 | 10.7 |
| Baylor Scheierman | 98% | 19.7<br><sub>11,18,21,23,20</sub> | 5.5<br><sub>2,2,3,2,10</sub> |  | 3.2<br><sub>0,6,4,3,2</sub> |  | 1.2<br><sub>0,2,1,3,1</sub> |  | 0.8<br><sub>0,0,1,0,2</sub> |  | 0.6 | 0.1 | 0.6 | 9.9 |
| Jordan Walsh | 98% | 15.3<br><sub>20,18,24,11,13</sub> | 4.0<br><sub>5,4,15,2,0</sub> |  | 3.0<br><sub>3,3,6,2,3</sub> |  | 0.8<br><sub>0,2,1,0,2</sub> |  | 0.4<br><sub>1,0,3,0,0</sub> |  | 0.6 | 0.3 | 0.4 | 7.7 |
| Luka Garza | 97% | 15.0<br><sub>4,13,13,7,21</sub> | 7.0<br><sub>8,6,2,5,12</sub> |  | 3.5<br><sub>1,3,4,1,6</sub> |  | 0.9<br><sub>0,2,0,1,4</sub> |  | 0.6<br><sub>2,0,0,0,2</sub> |  | 0.4 | 0.4 | 0.7 | 11.5 |
| Hugo Gonzalez | 93% | 12.8<br><sub>4,24,6,15,14</sub> | 3.3<br><sub>0,13,0,0,7</sub> |  | 2.5<br><sub>0,5,2,2,1</sub> |  | 0.6<br><sub>1,2,0,0,1</sub> |  | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |
| Dillon Mitchell | 16% | 8.6 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Mike Conley | 38% | 8.4<br><sub>-,7,-,-,-</sub> | 2.4<br><sub>-,6,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,2,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.4 |
| Ron Harper Jr. | 52% | 7.4<br><sub>-,7,-,3,-</sub> | 2.8<br><sub>-,3,-,0,-</sub> |  | 1.1<br><sub>-,1,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,1,-,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.3 |
| Amari Williams | 30% | 6.2<br><sub>-,-,-,-,-</sub> | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.4 | 0.4 | 3.5 |
| Chris Cenac Jr. | 48% | 5.9<br><sub>-,5,-,2,-</sub> | 2.7<br><sub>-,3,-,3,-</sub> |  | 1.4<br><sub>-,1,-,2,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,1,-,0,-</sub> |  | 0.1 | 0.1 | 0.6 | 4.5 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.5<br><sub>39,28,33,39,28</sub> | 16.6<br><sub>17,15,23,15,8</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 7.5<br><sub>11,5,4,3,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 5.0<br><sub>6,2,3,6,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.5 | 0.7 | 2.2 | 29.1 |
| Jabari Smith Jr. | 98% | 36.9<br><sub>33,39,30,35,33</sub> | 16.0<br><sub>14,16,14,22,30</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>5,12,2,3,9</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>3,5,2,2,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.6<br><sub>2,2,3,3,6</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.7 | 0.8 | 1.4 | 25.5 |
| Kevin Durant | 98% | 36.7<br><sub>37,30,31,37,27</sub> | 23.2<br><sub>22,22,18,28,14</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>4,9,5,5,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>2,3,4,1,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.3<br><sub>3,1,2,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 1.1 | 3.2 | 33.9 |
| Alperen Sengun | 64% | 36.0<br><sub>33,37,-,-,33</sub> | 20.7<br><sub>17,29,-,-,16</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 9.7<br><sub>10,9,-,-,9</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>7,9,-,-,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.8<br><sub>1,1,-,-,0</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.2 | 1.1 | 3.2 | 36.6 |
| Fred VanVleet | 71% | 34.7<br><sub>-,29,29,33,-</sub> | 14.5<br><sub>-,5,24,16,-</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>-,4,6,5,-</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 5.2<br><sub>-,5,5,6,-</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.6<br><sub>-,0,4,3,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.3 | 0.4 | 1.4 | 23.5 |
| Marcus Smart | 67% | 30.7<br><sub>-,-,-,17,36</sub> | 10.3<br><sub>-,-,-,8,24</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>-,-,-,2,5</sub> |  | 3.3<br><sub>-,-,-,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6<br><sub>-,-,-,0,7</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.6 | 0.4 | 1.7 | 16.9 |
| Tari Eason | 98% | 26.4<br><sub>31,33,31,26,19</sub> | 10.2<br><sub>19,13,5,11,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>3,8,9,13,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>0,2,1,2,2</sub> |  | 1.2<br><sub>0,1,1,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.7 | 1.0 | 17.7 |
| Bogdan Bogdanovic | 91% | 18.8<br><sub>20,13,15,11,19</sub> | 6.9<br><sub>11,5,16,6,4</sub> |  | 2.2<br><sub>1,2,2,1,2</sub> |  | 1.6<br><sub>1,1,4,0,1</sub> |  | 1.1<br><sub>3,1,4,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 10.8 |
| Oscar Tshiebwe | 86% | 12.3<br><sub>-,-,14,11,4</sub> | 4.7<br><sub>-,-,7,0,2</sub> |  | 4.8<br><sub>-,-,5,5,1</sub> |  | 0.7<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.3 | 0.6 | 10.2 |
| Isaiah Crawford | 67% | 11.5<br><sub>1,1,5,-,19</sub> | 3.7<br><sub>0,0,3,-,8</sub> |  | 1.7<br><sub>0,0,0,-,1</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.4<br><sub>0,0,1,-,2</sub> |  | 0.3 | 0.3 | 0.4 | 6.0 |
| Jae'Sean Tate | 67% | 7.9<br><sub>1,1,4,-,6</sub> | 2.4<br><sub>0,0,0,-,0</sub> |  | 1.8<br><sub>0,1,0,-,3</sub> |  | 0.5<br><sub>0,0,0,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.6 |
| Bruce Thornton | 67% | 7.7<br><sub>4,1,3,-,6</sub> | 2.2<br><sub>0,0,5,-,5</sub> |  | 1.4<br><sub>0,0,0,-,1</sub> |  | 0.7<br><sub>0,0,0,-,0</sub> |  | 0.2<br><sub>0,0,1,-,1</sub> |  | 0.2 | 0.1 | 0.4 | 4.2 |

</details>

<details><summary>if Reed Sheppard plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 36.8<br><sub>37,28,42,35,34</sub> | 26.3<br><sub>36,23,40,26,32</sub> | 26.5 · –<br><sub>o 46% · u 54%</sub> | 8.5<br><sub>9,7,5,7,4</sub> | 7.5<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>7,6,8,7,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,2,2,2,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.3 | 0.4 | 2.9 | 40.7 |
| Derrick White (BOS) | 98% | 33.4<br><sub>33,18,33,26,34</sub> | 13.3<br><sub>12,5,16,9,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,6,5,2,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.1<br><sub>6,4,7,4,2</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>2,1,1,1,2</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.1 | 0.9 | 1.7 | 21.2 |
| Paul George (BOS) | 98% | 33.2<br><sub>34,25,36,27,33</sub> | 18.7<br><sub>15,16,20,18,17</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>7,5,7,6,6</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>2,2,7,8,8</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>3,3,1,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 1.8 | 0.4 | 2.2 | 27.0 |
| Payton Pritchard (BOS) | 98% | 30.4<br><sub>30,22,24,35,27</sub> | 15.1<br><sub>4,28,4,30,7</sub> | 14.5 · –<br><sub>o 47% · u 53%</sub> | 3.3<br><sub>1,1,2,3,7</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>4,4,6,3,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.3<br><sub>1,7,0,3,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.1 | 1.3 | 22.2 |
| Neemias Queta (BOS) | 98% | 23.5<br><sub>22,19,15,20,27</sub> | 8.9<br><sub>15,7,7,13,8</sub> |  | 7.1<br><sub>6,5,3,6,8</sub> |  | 1.3<br><sub>1,1,2,0,1</sub> |  | 0.1<br><sub>1,0,0,0,0</sub> |  | 0.7 | 1.2 | 1.1 | 17.3 |
| Sam Hauser (BOS) | 98% | 20.6<br><sub>23,20,25,18,17</sub> | 6.8<br><sub>6,11,11,6,3</sub> |  | 3.0<br><sub>2,4,4,3,2</sub> |  | 0.9<br><sub>2,1,0,2,0</sub> |  | 1.2<br><sub>2,3,3,2,1</sub> |  | 0.4 | 0.2 | 0.4 | 10.7 |
| Baylor Scheierman (BOS) | 98% | 19.6<br><sub>11,18,21,23,20</sub> | 5.5<br><sub>2,2,3,2,10</sub> |  | 3.2<br><sub>0,6,4,3,2</sub> |  | 1.2<br><sub>0,2,1,3,1</sub> |  | 0.8<br><sub>0,0,1,0,2</sub> |  | 0.6 | 0.1 | 0.6 | 9.9 |
| Jordan Walsh (BOS) | 98% | 15.3<br><sub>20,18,24,11,13</sub> | 4.0<br><sub>5,4,15,2,0</sub> |  | 3.0<br><sub>3,3,6,2,3</sub> |  | 0.7<br><sub>0,2,1,0,2</sub> |  | 0.4<br><sub>1,0,3,0,0</sub> |  | 0.6 | 0.3 | 0.4 | 7.7 |
| Luka Garza (BOS) | 97% | 14.9<br><sub>4,13,13,7,21</sub> | 7.0<br><sub>8,6,2,5,12</sub> |  | 3.5<br><sub>1,3,4,1,6</sub> |  | 0.9<br><sub>0,2,0,1,4</sub> |  | 0.6<br><sub>2,0,0,0,2</sub> |  | 0.4 | 0.3 | 0.7 | 11.3 |
| Hugo Gonzalez (BOS) | 93% | 12.7<br><sub>4,24,6,15,14</sub> | 3.3<br><sub>0,13,0,0,7</sub> |  | 2.5<br><sub>0,5,2,2,1</sub> |  | 0.5<br><sub>1,2,0,0,1</sub> |  | 0.3<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |
| Mike Conley (BOS) | 38% | 8.6<br><sub>-,7,-,-,-</sub> | 2.4<br><sub>-,6,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,2,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 4.5 |
| Dillon Mitchell (BOS) | 16% | 8.5 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Ron Harper Jr. (BOS) | 52% | 7.4<br><sub>-,7,-,3,-</sub> | 2.8<br><sub>-,3,-,0,-</sub> |  | 1.1<br><sub>-,1,-,0,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.3<br><sub>-,1,-,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.2 |
| Amari Williams (BOS) | 30% | 6.3<br><sub>-,-,-,-,-</sub> | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.4 | 0.5 | 3.6 |
| Chris Cenac Jr. (BOS) | 48% | 5.9<br><sub>-,5,-,2,-</sub> | 2.7<br><sub>-,3,-,3,-</sub> |  | 1.4<br><sub>-,1,-,2,-</sub> |  | 0.4<br><sub>-,0,-,0,-</sub> |  | 0.2<br><sub>-,1,-,0,-</sub> |  | 0.2 | 0.1 | 0.7 | 4.5 |
| Kevin Durant (HOU) | 98% | 36.2<br><sub>37,30,31,37,27</sub> | 22.6<br><sub>22,22,18,28,14</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 5.9<br><sub>4,9,5,5,3</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>2,3,4,1,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.1<br><sub>3,1,2,1,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.7 | 1.2 | 3.0 | 33.0 |
| Amen Thompson (HOU) | 98% | 36.2<br><sub>39,28,33,39,28</sub> | 15.7<br><sub>17,15,23,15,8</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 7.3<br><sub>11,5,4,3,3</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>6,2,3,6,1</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 1.4 | 0.7 | 2.0 | 27.5 |
| Jabari Smith Jr. (HOU) | 98% | 36.1<br><sub>33,39,30,35,33</sub> | 15.6<br><sub>14,16,14,22,30</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.2<br><sub>5,12,2,3,9</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>3,5,2,2,5</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 2.5<br><sub>2,2,3,3,6</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.8 | 1.3 | 24.9 |
| Alperen Sengun (HOU) | 64% | 35.3<br><sub>33,37,-,-,33</sub> | 19.4<br><sub>17,29,-,-,16</sub> | 17.5 · –<br><sub>o 52% · u 48%</sub> | 9.5<br><sub>10,9,-,-,9</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 6.0<br><sub>7,9,-,-,9</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 0.7<br><sub>1,1,-,-,0</sub> | 0.5<br><sub>o 53% · u 47%</sub> | 1.2 | 1.1 | 3.0 | 34.9 |
| Fred VanVleet (HOU) | 71% | 33.1<br><sub>-,29,29,33,-</sub> | 13.1<br><sub>-,5,24,16,-</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.5<br><sub>-,4,6,5,-</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 4.9<br><sub>-,5,5,6,-</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>-,0,4,3,-</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.4 | 1.2 | 21.5 |
| Marcus Smart (HOU) | 67% | 26.9<br><sub>-,-,-,17,36</sub> | 8.7<br><sub>-,-,-,8,24</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>-,-,-,2,5</sub> |  | 2.8<br><sub>-,-,-,4,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>-,-,-,0,7</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.3 | 0.3 | 1.5 | 14.3 |
| Reed Sheppard (HOU) | 100% | 24.1<br><sub>30,24,23,-,-</sub> | 10.6<br><sub>19,13,7,-,-</sub> |  | 2.4<br><sub>6,0,3,-,-</sub> |  | 3.1<br><sub>7,4,4,-,-</sub> |  | 1.9<br><sub>5,2,1,-,-</sub> |  | 1.3 | 0.5 | 1.1 | 16.1 |
| Tari Eason (HOU) | 98% | 23.4<br><sub>31,33,31,26,19</sub> | 9.1<br><sub>19,13,5,11,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.5<br><sub>3,8,9,13,3</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>0,2,1,2,2</sub> |  | 1.0<br><sub>0,1,1,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.0 | 0.6 | 0.9 | 15.7 |
| Bogdan Bogdanovic (HOU) | 91% | 13.6<br><sub>20,13,15,11,19</sub> | 4.9<br><sub>11,5,16,6,4</sub> |  | 1.6<br><sub>1,2,2,1,2</sub> |  | 1.1<br><sub>1,1,4,0,1</sub> |  | 0.7<br><sub>3,1,4,0,0</sub> |  | 0.3 | 0.1 | 0.6 | 7.6 |
| Oscar Tshiebwe (HOU) | 86% | 9.9<br><sub>-,-,14,11,4</sub> | 3.9<br><sub>-,-,7,0,2</sub> |  | 3.6<br><sub>-,-,5,5,1</sub> |  | 0.6<br><sub>-,-,2,0,1</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.3 | 0.5 | 8.1 |
| Isaiah Crawford (HOU) | 67% | 8.7<br><sub>1,1,5,-,19</sub> | 3.0<br><sub>0,0,3,-,8</sub> |  | 1.3<br><sub>0,0,0,-,1</sub> |  | 0.4<br><sub>0,0,0,-,0</sub> |  | 0.3<br><sub>0,0,1,-,2</sub> |  | 0.2 | 0.3 | 0.3 | 4.7 |
| Jae'Sean Tate (HOU) | 67% | 6.3<br><sub>1,1,4,-,6</sub> | 1.9<br><sub>0,0,0,-,0</sub> |  | 1.4<br><sub>0,1,0,-,3</sub> |  | 0.3<br><sub>0,0,0,-,1</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.7 |
| Bruce Thornton (HOU) | 67% | 5.8<br><sub>4,1,3,-,6</sub> | 1.9<br><sub>0,0,5,-,5</sub> |  | 1.0<br><sub>0,0,0,-,1</sub> |  | 0.5<br><sub>0,0,0,-,0</sub> |  | 0.1<br><sub>0,0,1,-,1</sub> |  | 0.2 | 0.1 | 0.3 | 3.4 |

</details>


### UTA @ SAS
Out: Tobias Harris (SAS), Trey Alexander (UTA), Jaren Jackson Jr. (UTA), Jusuf Nurkic (UTA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama BLK over 3.5 (4+) | UTA @ SAS | draftkings | 2.24 | 2.20 | 1.80 | 55.7% | 42.0% | 45.4% | +1.8% | +24.8% | 0.4% |
| Isaiah Collier PTS over 7.5 (8+) | UTA @ SAS | draftkings | 1.98 | 1.96 | 1.61 | 62.1% | 47.2% | 50.9% | +0.8% | +22.9% | 0.2% |
| Isaiah Collier PA over 12.5 (13+) | UTA @ SAS | draftkings | 1.88 | 1.88 | 1.55 | 64.4% | 49.6% | 53.3% | +0.4% | +21.4% | 0.1% |
| Ace Bailey REB over 5.5 (6+) | UTA @ SAS | draftkings | 2.09 | 2.08 | 1.74 | 57.4% | 44.8% | 48.0% | +0.3% | +20.0% | 0.1% |

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Ace Bailey | 98% | 32.8<br><sub>22,29,34,40,37</sub> | 15.0<br><sub>6,17,17,19,9</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 6.3<br><sub>7,12,10,6,7</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>2,4,3,0,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>1,1,3,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 1.0 | 1.9 | 23.7 |
| Keyonte George | 98% | 32.4<br><sub>32,33,33,37,29</sub> | 21.1<br><sub>19,24,26,31,8</sub> | 20.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>1,9,3,4,3</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>10,10,6,3,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.1<br><sub>3,2,0,5,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.1 | 3.4 | 31.0 |
| Darryn Peterson | 96% | 30.8<br><sub>30,30,26,26,36</sub> | 13.1<br><sub>15,8,14,18,16</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>3,3,7,5,4</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 3.0<br><sub>1,2,4,3,4</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.4<br><sub>1,0,3,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.1 | 0.4 | 1.8 | 20.6 |
| Lauri Markkanen | 98% | 30.3<br><sub>34,38,6,-,29</sub> | 19.4<br><sub>16,28,2,-,13</sub> | 19.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>6,7,0,-,6</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>3,1,0,-,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.2<br><sub>4,5,0,-,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.4 | 1.4 | 27.5 |
| Jaxson Hayes | 98% | 24.7<br><sub>26,19,-,37,20</sub> | 8.2<br><sub>17,9,-,2,7</sub> | 7.5 · –<br><sub>o 52% · u 48%</sub> | 5.9<br><sub>5,5,-,11,7</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>2,1,-,4,2</sub> |  | 0.0<br><sub>0,0,-,0,0</sub> |  | 0.7 | 1.1 | 0.9 | 15.8 |
| Isaiah Collier | 96% | 21.6<br><sub>18,13,21,24,20</sub> | 9.8<br><sub>10,6,7,7,8</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,3,8,7,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>7,6,8,6,4</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.2 | 2.0 | 18.6 |
| Brice Sensabaugh | 98% | 18.9<br><sub>16,17,9,18,19</sub> | 10.2<br><sub>10,7,11,16,12</sub> |  | 2.7<br><sub>3,6,2,3,3</sub> |  | 1.6<br><sub>2,1,0,1,2</sub> |  | 1.4<br><sub>2,1,3,4,2</sub> |  | 0.5 | 0.1 | 1.2 | 14.5 |
| Svi Mykhailiuk | 88% | 17.0<br><sub>21,14,13,15,18</sub> | 6.0<br><sub>3,2,0,3,6</sub> |  | 2.1<br><sub>4,3,1,2,1</sub> |  | 1.3<br><sub>1,0,0,1,3</sub> |  | 0.9<br><sub>0,0,0,1,2</sub> |  | 0.5 | 0.1 | 0.7 | 9.4 |
| Josh Okogie | 88% | 16.2<br><sub>-,10,21,28,14</sub> | 3.5<br><sub>-,2,0,5,0</sub> |  | 2.6<br><sub>-,2,2,9,1</sub> |  | 0.9<br><sub>-,2,0,3,0</sub> |  | 0.4<br><sub>-,0,0,1,0</sub> |  | 0.7 | 0.2 | 0.5 | 7.1 |
| Mo Bamba | 63% | 14.6<br><sub>-,-,29,16,11</sub> | 4.6<br><sub>-,-,14,8,6</sub> |  | 5.1<br><sub>-,-,7,4,4</sub> |  | 0.8<br><sub>-,-,1,1,0</sub> |  | 0.3<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.9 | 0.7 | 10.5 |
| Josh Green | 80% | 12.8<br><sub>-,3,25,24,2</sub> | 2.7<br><sub>-,0,6,2,0</sub> |  | 1.5<br><sub>-,0,4,2,0</sub> |  | 0.7<br><sub>-,1,1,2,0</sub> |  | 0.3<br><sub>-,0,1,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.8 |
| Kyle Filipowski | 66% | 12.2<br><sub>8,-,8,-,6</sub> | 5.7<br><sub>0,-,0,-,5</sub> |  | 3.7<br><sub>1,-,1,-,0</sub> |  | 1.4<br><sub>0,-,0,-,2</sub> |  | 0.5<br><sub>0,-,0,-,1</sub> |  | 0.6 | 0.2 | 0.8 | 10.7 |
| Tony Bradley | 38% | 8.1<br><sub>-,-,6,-,-</sub> | 2.8<br><sub>-,-,2,-,-</sub> |  | 2.4<br><sub>-,-,1,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.7 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 33.0<br><sub>32,29,27,39,34</sub> | 27.9<br><sub>25,23,29,36,43</sub> | 26.5 · –<br><sub>o 48% · u 52%</sub> | 11.5<br><sub>13,7,10,14,7</sub> | 11.5<br><sub>o 51% · u 49%</sub> | 3.4<br><sub>2,2,2,5,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.4<br><sub>2,2,0,4,3</sub> | 1.5<br><sub>o 63% · u 37%</sub> | 1.3 | 4.1 | 2.6 | 42.8 |
| Dylan Harper | 98% | 32.2<br><sub>36,28,30,37,39</sub> | 17.4<br><sub>20,22,13,13,25</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.9<br><sub>3,5,6,5,7</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>2,2,6,8,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>1,3,0,2,2</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.3 | 0.4 | 2.0 | 28.1 |
| Devin Vassell | 98% | 32.2<br><sub>36,32,24,38,34</sub> | 13.6<br><sub>10,11,14,21,9</sub> | 11.5 · –<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>4,4,4,5,5</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 3.1<br><sub>2,6,8,2,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.2<br><sub>2,1,4,1,0</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 1.4 | 0.5 | 1.2 | 21.4 |
| De'Aaron Fox | 98% | 32.0<br><sub>34,28,26,39,35</sub> | 16.8<br><sub>19,19,11,14,22</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 4.1<br><sub>4,3,4,3,8</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.8<br><sub>9,9,6,4,7</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>2,2,2,1,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.5 | 2.2 | 27.8 |
| Stephon Castle | 98% | 29.5<br><sub>33,28,27,38,22</sub> | 16.5<br><sub>15,19,15,14,0</sub> | 15.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>7,4,5,6,5</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 6.5<br><sub>5,8,5,8,4</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>3,3,3,1,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.2 | 0.3 | 2.8 | 28.1 |
| Julian Champagnie | 98% | 27.2<br><sub>25,28,25,31,27</sub> | 10.8<br><sub>6,12,26,6,12</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.9<br><sub>0,5,3,6,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>0,3,3,0,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 2.2<br><sub>2,3,8,2,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.6 | 0.8 | 17.3 |
| Keldon Johnson | 98% | 20.9<br><sub>19,26,22,23,24</sub> | 10.4<br><sub>8,7,14,9,2</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>6,6,4,6,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>1,3,0,2,0</sub> |  | 0.7<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 16.2 |
| Luke Kornet | 98% | 14.5<br><sub>16,14,17,14,14</sub> | 4.0<br><sub>7,0,0,1,2</sub> |  | 4.6<br><sub>3,4,4,6,8</sub> |  | 0.9<br><sub>0,1,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.8 | 0.5 | 9.6 |
| Carter Bryant | 98% | 9.9<br><sub>4,10,17,5,11</sub> | 3.8<br><sub>0,4,1,3,6</sub> |  | 1.8<br><sub>0,1,1,0,0</sub> |  | 0.7<br><sub>0,0,2,0,0</sub> |  | 0.4<br><sub>0,0,0,1,2</sub> |  | 0.3 | 0.3 | 0.5 | 6.3 |
| Harrison Barnes | 58% | 8.9<br><sub>5,4,14,-,-</sub> | 3.2<br><sub>0,0,3,-,-</sub> |  | 1.1<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.9 |
| Maliq Brown | 80% | 6.9<br><sub>-,-,-,-,-</sub> | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 2.7<br><sub>-,-,-,-,-</sub> |  | 0.0<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.4 | 3.3 |
| Jordan McLaughlin | 48% | 6.6<br><sub>-,3,7,-,-</sub> | 2.2<br><sub>-,0,0,-,-</sub> |  | 1.0<br><sub>-,1,0,-,-</sub> |  | 1.1<br><sub>-,0,2,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.5 | 0.1 | 0.3 | 4.3 |
| Tarris Reed Jr. | 52% | 6.2<br><sub>-,7,5,-,-</sub> | 2.6<br><sub>-,2,4,-,-</sub> |  | 2.3<br><sub>-,3,5,-,-</sub> |  | 0.4<br><sub>-,0,0,-,-</sub> |  | 0.0<br><sub>-,0,0,-,-</sub> |  | 0.2 | 0.3 | 0.7 | 5.4 |
| Ja'Kobi Gillespie | 88% | 6.1<br><sub>-,3,-,-,-</sub> | 4.6<br><sub>-,3,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,1,-,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.4 |
| David Jones Garcia | 48% | 5.8<br><sub>-,-,-,-,-</sub> | 2.6<br><sub>-,-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.4 | 5.0 |

</details>


### POR @ DEN
Out: Julian Strawther (DEN), Ja Morant (POR), Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scoot Henderson 3PM under 1.5 | POR @ DEN | draftkings | 2.29 | 2.27 | 1.87 | 53.5% | 40.8% | 44.0% | +0.7% | +22.5% | 0.1% |
| Cameron Johnson 3PM under 1.5 | POR @ DEN | draftkings | 2.18 | 2.18 | 1.81 | 55.1% | 42.9% | 45.9% | +0.1% | +20.1% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.6–121.5 | POR 31% | 3.22 / 1.45 | DEN -6.5 | 236.5 | DEN -4.5 covers 57%; o230.5 62% |
| Expected (weighted by chance each plays) | 114.6–121.4 | POR 31% | 3.25 / 1.44 | DEN -7.5 | 235.5 | DEN -4.5 covers 57%; o230.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alpha Diallo (DEN) | Questionable | 55% | 12.9 | 3.5 | 1.7 | 1.2 | 0.3 | 0.5 | 0.3 | 1.0 | 6.4 | small |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 33.5<br><sub>23,38,33,32,30</sub> | 22.2<br><sub>18,26,23,24,24</sub> | 22.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>10,7,4,9,5</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 6.7<br><sub>4,6,9,7,2</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>2,1,4,0,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.5 | 3.5 | 35.6 |
| Damian Lillard | 98% | 31.3<br><sub>24,33,31,30,27</sub> | 16.9<br><sub>25,19,21,9,22</sub> | 20.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>3,5,5,2,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 5.3<br><sub>6,2,4,2,4</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 2.5<br><sub>6,2,4,1,3</sub> | 3.5<br><sub>o 37% · u 63%</sub> | 1.0 | 0.2 | 2.2 | 26.2 |
| Toumani Camara | 98% | 30.7<br><sub>23,27,24,26,31</sub> | 13.2<br><sub>18,19,12,13,14</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 4.3<br><sub>2,3,1,2,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>3,1,1,1,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>4,5,4,3,4</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.1 | 0.4 | 1.2 | 19.5 |
| Jrue Holiday | 98% | 29.0<br><sub>21,26,30,24,22</sub> | 14.3<br><sub>8,12,22,6,14</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>4,1,4,6,4</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 5.2<br><sub>1,8,3,4,3</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>0,3,2,2,2</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.0 | 0.2 | 1.9 | 23.7 |
| Scoot Henderson | 98% | 27.3<br><sub>19,21,17,19,31</sub> | 12.8<br><sub>15,4,2,9,14</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>2,1,2,4,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.3<br><sub>1,2,3,0,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>1,0,0,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.2 | 2.4 | 18.8 |
| Donovan Clingan | 98% | 25.0<br><sub>21,21,26,29,15</sub> | 9.8<br><sub>11,8,9,11,4</sub> | 10.5 · –<br><sub>o 47% · u 53%</sub> | 9.8<br><sub>7,10,10,8,9</sub> | 10.5<br><sub>o 48% · u 52%</sub> | 1.9<br><sub>2,3,1,1,0</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.0<br><sub>2,0,2,1,0</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 0.5 | 1.4 | 1.1 | 21.5 |
| Sidy Cissoko | 96% | 20.8<br><sub>25,26,20,19,19</sub> | 5.6<br><sub>3,15,6,4,1</sub> |  | 2.9<br><sub>4,7,2,6,3</sub> |  | 1.7<br><sub>3,1,4,2,1</sub> |  | 0.5<br><sub>1,2,0,0,0</sub> |  | 0.8 | 0.3 | 0.8 | 10.2 |
| Robert Williams III | 98% | 18.9<br><sub>15,18,21,-,14</sub> | 7.1<br><sub>2,13,14,-,3</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 7.0<br><sub>10,6,10,-,3</sub> | 6.5<br><sub>o 52% · u 48%</sub> | 1.2<br><sub>1,0,1,-,1</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.7 | 1.1 | 0.8 | 15.3 |
| Vit Krejci | 96% | 17.2<br><sub>15,3,7,8,24</sub> | 6.0<br><sub>1,0,4,2,5</sub> |  | 2.1<br><sub>2,2,0,0,4</sub> |  | 1.4<br><sub>3,0,0,1,2</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 9.5 |
| Yang Hansen | 64% | 10.3<br><sub>12,-,-,5,13</sub> | 3.9<br><sub>5,-,-,3,6</sub> |  | 2.6<br><sub>3,-,-,2,5</sub> |  | 0.6<br><sub>0,-,-,1,1</sub> |  | 0.3<br><sub>1,-,-,1,2</sub> |  | 0.3 | 0.3 | 0.7 | 7.2 |
| Micah Potter | 67% | 10.0<br><sub>12,-,-,9,4</sub> | 4.1<br><sub>4,-,-,1,2</sub> |  | 2.8<br><sub>3,-,-,2,1</sub> |  | 0.6<br><sub>0,-,-,0,0</sub> |  | 0.4<br><sub>0,-,-,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 7.5 |
| Chris Youngblood | 64% | 9.3<br><sub>-,-,-,-,7</sub> | 3.6<br><sub>-,-,-,-,3</sub> |  | 1.3<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.2 | 0.3 | 5.5 |
| Branden Carlson | 58% | 8.7<br><sub>-,-,-,12,4</sub> | 4.4<br><sub>-,-,-,2,0</sub> |  | 1.9<br><sub>-,-,-,2,2</sub> |  | 0.6<br><sub>-,-,-,1,1</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.4 | 0.7 | 6.8 |

</details>

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 37.3<br><sub>37,43,36,38,37</sub> | 24.9<br><sub>6,42,19,23,39</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 4.5<br><sub>10,3,6,1,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>3,6,8,6,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 3.1<br><sub>0,8,3,5,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.6 | 2.7 | 35.6 |
| Nikola Jokic | 98% | 36.8<br><sub>35,44,35,34,37</sub> | 26.2<br><sub>13,35,19,21,18</sub> | 25.5 · –<br><sub>o 49% · u 51%</sub> | 12.3<br><sub>7,15,7,13,7</sub> | 12.5<br><sub>o 47% · u 53%</sub> | 10.2<br><sub>5,10,11,10,10</sub> | 9.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>1,3,1,0,0</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.7 | 1.1 | 3.8 | 48.7 |
| Christian Braun | 98% | 34.3<br><sub>33,40,34,36,37</sub> | 13.4<br><sub>7,15,9,15,31</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>6,8,4,0,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.3<br><sub>1,2,2,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3<br><sub>1,0,1,3,7</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.5 | 1.2 | 20.5 |
| Aaron Gordon | 98% | 30.1<br><sub>29,37,25,31,29</sub> | 14.6<br><sub>20,7,7,15,15</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>6,5,4,11,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>1,4,2,3,5</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.4<br><sub>3,1,0,2,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.4 | 1.4 | 23.4 |
| Cameron Johnson | 97% | 27.6<br><sub>11,-,-,-,34</sub> | 11.3<br><sub>5,-,-,-,12</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 4.0<br><sub>2,-,-,-,9</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>1,-,-,-,3</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.5<br><sub>1,-,-,-,2</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.4 | 1.0 | 17.6 |
| DeMar DeRozan | 98% | 26.6<br><sub>28,24,29,26,24</sub> | 13.6<br><sub>13,12,21,6,3</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>2,3,4,2,1</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 3.5<br><sub>0,3,2,5,5</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 0.4<br><sub>0,0,2,0,0</sub> |  | 0.9 | 0.4 | 1.6 | 19.7 |
| Trevon Brazile | 96% | 19.8<br><sub>18,28,17,32,19</sub> | 6.6<br><sub>4,17,6,11,6</sub> | 6.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>12,9,1,8,3</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.9<br><sub>0,0,0,0,1</sub> |  | 0.7<br><sub>0,3,1,1,1</sub> |  | 0.6 | 0.6 | 0.9 | 12.2 |
| Marvin Bagley III | 98% | 12.7<br><sub>11,9,11,19,11</sub> | 5.6<br><sub>2,5,7,8,0</sub> |  | 3.7<br><sub>3,4,2,5,5</sub> |  | 0.7<br><sub>1,0,0,1,0</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.6 | 9.9 |
| Bryce Hopkins | 67% | 11.0<br><sub>2,19,31,14,-</sub> | 3.0<br><sub>0,2,13,0,-</sub> |  | 1.7<br><sub>1,2,3,2,-</sub> |  | 0.6<br><sub>0,1,1,0,-</sub> |  | 0.2<br><sub>0,0,1,0,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.3 |
| Tyus Jones | 91% | 9.9<br><sub>10,10,9,11,11</sub> | 2.6<br><sub>2,2,0,5,3</sub> |  | 0.8<br><sub>0,0,0,0,0</sub> |  | 1.3<br><sub>0,0,2,1,0</sub> |  | 0.2<br><sub>0,0,0,1,1</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Cam Whitmore | 58% | 7.4<br><sub>-,11,4,-,-</sub> | 3.5<br><sub>-,4,4,-,-</sub> |  | 1.3<br><sub>-,2,0,-,-</sub> |  | 0.4<br><sub>-,0,1,-,-</sub> |  | 0.2<br><sub>-,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.2 |
| Zeke Nnaji | 38% | 6.9<br><sub>-,-,4,-,-</sub> | 2.4<br><sub>-,-,5,-,-</sub> |  | 1.4<br><sub>-,-,1,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,1,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 4.2 |
| Ryan Nembhard | 43% | 6.3<br><sub>2,-,4,-,-</sub> | 5.2<br><sub>5,-,4,-,-</sub> |  | 0.9<br><sub>1,-,0,-,-</sub> |  | 0.9<br><sub>1,-,1,-,-</sub> |  | 0.3<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 7.0 |
| DaRon Holmes II | 48% | 5.7<br><sub>2,-,4,-,-</sub> | 2.3<br><sub>3,-,0,-,-</sub> |  | 1.1<br><sub>1,-,0,-,-</sub> |  | 0.4<br><sub>1,-,1,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 3.8 |

</details>


### PHX @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Gui Santos (GSW), Drew Timme (PHX), Mark Williams (PHX)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 113.7–112.4 | PHX 54% | 1.86 / 2.16 | GSW +1.5 | 225.5 | GSW -2.5 covers 40%; o228.5 45% |
| Expected (weighted by chance each plays) | 112.8–114.0 | PHX 47% | 2.14 / 1.88 | GSW -1.5 | 226.5 | GSW -2.5 covers 47%; o228.5 46% |
| if Stephen Curry plays | 112.8–114.1 | PHX 46% | 2.16 / 1.86 | GSW -1.5 | 226.5 | GSW -2.5 covers 48%; o228.5 46% |
| if Draymond Green plays | 113.4–112.9 | PHX 51% | 1.95 / 2.06 | GSW +0.5 | 225.5 | GSW -2.5 covers 42%; o228.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephen Curry (GSW) | Day-To-Day | 70% | 30.4 | 23.7 | 3.7 | 4.6 | 3.9 | 1.1 | 0.4 | 2.8 | 32.1 | full tables below |
| Draymond Green (GSW) | Day-To-Day | 70% | 29.3 | 8.4 | 5.7 | 5.7 | 1.0 | 1.1 | 0.7 | 2.7 | 19.8 | full tables below |

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 33.5<br><sub>29,36,34,39</sub> | 24.4<br><sub>23,43,3,20</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,7,2,2</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 5.8<br><sub>2,7,7,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>0,2,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.2 | 3.3 | 33.9 |
| Miles Bridges | 98% | 30.8<br><sub>29,33,32,37</sub> | 15.6<br><sub>8,16,17,24</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>4,7,8,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>0,3,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>0,2,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.5 | 1.6 | 24.5 |
| Dillon Brooks | 98% | 28.1<br><sub>27,34,33,21</sub> | 16.6<br><sub>10,15,19,22</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,2,5,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,5,5,2</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 2.0<br><sub>1,1,3,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 1.5 | 22.2 |
| Jalen Green | 96% | 27.6<br><sub>25,26,31,25</sub> | 15.3<br><sub>10,12,20,2</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>2,2,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>3,1,4,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,1,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.3 | 2.4 | 21.8 |
| Collin Gillespie | 98% | 26.2<br><sub>21,28,23,33</sub> | 10.0<br><sub>0,11,9,16</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,4,1,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>2,9,2,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>0,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.2 | 1.5 | 17.7 |
| Oso Ighodaro | 97% | 20.1<br><sub>15,-,-,21</sub> | 6.0<br><sub>8,-,-,2</sub> |  | 5.2<br><sub>3,-,-,9</sub> |  | 2.8<br><sub>3,-,-,5</sub> |  | 0.0<br><sub>0,-,-,0</sub> |  | 0.8 | 0.6 | 1.3 | 14.0 |
| Jordan Goodwin | 98% | 19.0<br><sub>22,20,17,25</sub> | 7.1<br><sub>3,9,12,11</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,2,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,4,2,5</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.1<br><sub>1,1,4,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.1 | 0.8 | 12.8 |
| Khaman Maluach | 96% | 17.3<br><sub>17,28,26,17</sub> | 6.1<br><sub>2,9,12,9</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>6,9,7,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>1,3,1,0</sub> |  | 0.2<br><sub>0,1,0,0</sub> |  | 0.4 | 0.9 | 1.1 | 12.0 |
| Luke Kennard | 98% | 14.7<br><sub>-,18,16,12</sub> | 5.3<br><sub>-,11,9,9</sub> |  | 1.8<br><sub>-,4,1,1</sub> |  | 1.4<br><sub>-,1,2,2</sub> |  | 0.6<br><sub>-,3,3,1</sub> |  | 0.6 | 0.1 | 0.7 | 8.6 |
| Ryan Dunn | 96% | 11.6<br><sub>14,13,14,11</sub> | 3.6<br><sub>3,5,6,5</sub> |  | 2.6<br><sub>2,5,2,3</sub> |  | 0.8<br><sub>0,0,1,1</sub> |  | 0.3<br><sub>0,1,1,1</sub> |  | 0.5 | 0.3 | 0.5 | 7.0 |
| Pat Spencer | 64% | 7.6<br><sub>7,-,-,-</sub> | 2.7<br><sub>3,-,-,-</sub> |  | 0.9<br><sub>3,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.0 |
| Rasheer Fleming | 58% | 6.7<br><sub>12,-,3,-</sub> | 2.4<br><sub>1,-,0,-</sub> |  | 1.3<br><sub>2,-,1,-</sub> |  | 0.3<br><sub>0,-,0,-</sub> |  | 0.2<br><sub>0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.0 |
| Duop Reath | 64% | 6.5<br><sub>9,3,7,-</sub> | 2.6<br><sub>5,0,5,-</sub> |  | 1.4<br><sub>1,0,3,-</sub> |  | 0.3<br><sub>0,0,0,-</sub> |  | 0.2<br><sub>1,0,1,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |
| Jamaree Bouyea | 58% | 6.2<br><sub>7,-,3,-</sub> | 2.6<br><sub>3,-,2,-</sub> |  | 0.9<br><sub>2,-,0,-</sub> |  | 0.9<br><sub>2,-,1,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.4 |
| Koa Peat | 52% | 5.9<br><sub>7,-,3,-</sub> | 2.3<br><sub>4,-,0,-</sub> |  | 1.4<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>0,-,0,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.0 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 88% | 34.0<br><sub>-,33,32,33,37</sub> | 18.9<br><sub>-,18,8,21,17</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>-,7,5,5,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 5.7<br><sub>-,5,6,6,8</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.3<br><sub>-,3,0,4,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 2.3 | 30.2 |
| Yaxel Lendeborg | 96% | 33.4<br><sub>36,31,35,24,34</sub> | 22.2<br><sub>26,31,26,6,37</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>9,12,9,1,4</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>5,6,1,0,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.1<br><sub>6,1,2,1,6</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.0 | 0.5 | 3.3 | 33.3 |
| De'Anthony Melton | 98% | 26.6<br><sub>27,19,20,21,28</sub> | 13.2<br><sub>25,3,8,16,21</sub> |  | 4.0<br><sub>5,4,6,5,6</sub> |  | 3.3<br><sub>5,3,0,3,3</sub> |  | 1.9<br><sub>4,1,2,4,6</sub> |  | 1.4 | 0.4 | 2.1 | 20.5 |
| Georges Niang | 96% | 26.3<br><sub>23,18,23,19,21</sub> | 10.4<br><sub>4,9,7,11,3</sub> |  | 3.5<br><sub>4,2,3,5,1</sub> |  | 1.8<br><sub>2,0,2,1,2</sub> |  | 1.8<br><sub>0,3,1,3,1</sub> |  | 0.5 | 0.2 | 1.6 | 15.7 |
| Brandon Williams | 98% | 25.1<br><sub>24,15,14,17,25</sub> | 15.5<br><sub>20,6,11,9,17</sub> |  | 3.4<br><sub>3,3,3,2,3</sub> |  | 4.5<br><sub>5,3,1,1,3</sub> |  | 0.9<br><sub>2,2,0,0,2</sub> |  | 1.1 | 0.4 | 2.2 | 23.5 |
| Al Horford | 98% | 24.3<br><sub>-,19,18,17,22</sub> | 7.9<br><sub>-,11,4,3,9</sub> |  | 5.0<br><sub>-,3,5,2,5</sub> |  | 2.2<br><sub>-,0,2,0,2</sub> |  | 1.3<br><sub>-,3,0,1,3</sub> |  | 0.7 | 1.0 | 0.9 | 15.2 |
| Will Richard | 98% | 23.8<br><sub>31,3,23,13,22</sub> | 6.4<br><sub>11,0,6,3,3</sub> |  | 2.9<br><sub>0,0,3,3,0</sub> |  | 1.6<br><sub>1,0,0,2,3</sub> |  | 0.9<br><sub>3,0,0,1,1</sub> |  | 1.2 | 0.2 | 0.8 | 10.9 |
| Gary Payton II | 98% | 18.6<br><sub>17,12,10,8,15</sub> | 8.2<br><sub>2,7,2,2,5</sub> |  | 3.6<br><sub>1,2,2,4,2</sub> |  | 1.7<br><sub>0,0,1,0,2</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 1.0 | 0.3 | 0.8 | 13.5 |
| Charles Bassey | 93% | 17.2<br><sub>13,2,2,9,20</sub> | 6.7<br><sub>10,0,0,6,6</sub> |  | 6.8<br><sub>7,1,0,4,10</sub> |  | 0.9<br><sub>0,0,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 0.9 | 14.4 |
| Graham Ike | 72% | 17.0<br><sub>26,3,-,-,6</sub> | 6.9<br><sub>12,3,-,-,2</sub> |  | 4.2<br><sub>10,0,-,-,2</sub> |  | 1.3<br><sub>2,1,-,-,0</sub> |  | 0.5<br><sub>0,1,-,-,0</sub> |  | 0.6 | 0.3 | 0.9 | 12.4 |
| LJ Cryer | 58% | 13.8<br><sub>14,3,-,-,2</sub> | 5.4<br><sub>3,6,-,-,0</sub> |  | 1.3<br><sub>1,0,-,-,0</sub> |  | 1.0<br><sub>1,2,-,-,0</sub> |  | 0.8<br><sub>1,2,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 7.8 |
| Malevy Leons | 48% | 12.2<br><sub>4,3,-,-,-</sub> | 3.6<br><sub>2,0,-,-,-</sub> |  | 2.2<br><sub>0,1,-,-,-</sub> |  | 0.9<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.6 | 0.4 | 0.6 | 6.7 |

</details>

<details><summary>if Stephen Curry plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 88% | 33.1<br><sub>-,33,32,33,37</sub> | 16.1<br><sub>-,18,8,21,17</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>-,7,5,5,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.5<br><sub>-,5,6,6,8</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>-,3,0,4,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.1 | 0.2 | 1.8 | 26.1 |
| Yaxel Lendeborg (GSW) | 96% | 32.8<br><sub>36,31,35,24,34</sub> | 19.1<br><sub>26,31,26,6,37</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 7.0<br><sub>9,12,9,1,4</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>5,6,1,0,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>6,1,2,1,6</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.5 | 3.0 | 29.6 |
| Stephen Curry (GSW) | 100% | 30.4<br><sub>-,27,32,31,-</sub> | 23.7<br><sub>-,24,44,31,-</sub> | 26.5 · – | 3.7<br><sub>-,3,8,4,-</sub> | 3.5 | 4.6<br><sub>-,3,6,6,-</sub> | 4.5 | 3.9<br><sub>-,3,6,8,-</sub> | 3.5 | 1.1 | 0.4 | 2.8 | 32.1 |
| De'Anthony Melton (GSW) | 98% | 24.2<br><sub>27,19,20,21,28</sub> | 11.2<br><sub>25,3,8,16,21</sub> |  | 3.7<br><sub>5,4,6,5,6</sub> |  | 2.6<br><sub>5,3,0,3,3</sub> |  | 1.7<br><sub>4,1,2,4,6</sub> |  | 1.3 | 0.4 | 1.7 | 17.5 |
| Georges Niang (GSW) | 96% | 21.8<br><sub>23,18,23,19,21</sub> | 7.8<br><sub>4,9,7,11,3</sub> |  | 3.0<br><sub>4,2,3,5,1</sub> |  | 1.3<br><sub>2,0,2,1,2</sub> |  | 1.3<br><sub>0,3,1,3,1</sub> |  | 0.4 | 0.2 | 1.0 | 12.2 |
| Al Horford (GSW) | 98% | 21.7<br><sub>-,19,18,17,22</sub> | 6.8<br><sub>-,11,4,3,9</sub> |  | 4.6<br><sub>-,3,5,2,5</sub> |  | 1.8<br><sub>-,0,2,0,2</sub> |  | 1.1<br><sub>-,3,0,1,3</sub> |  | 0.6 | 0.9 | 0.7 | 13.2 |
| Brandon Williams (GSW) | 98% | 20.9<br><sub>24,15,14,17,25</sub> | 12.0<br><sub>20,6,11,9,17</sub> |  | 2.9<br><sub>3,3,3,2,3</sub> |  | 3.3<br><sub>5,3,1,1,3</sub> |  | 0.7<br><sub>2,2,0,0,2</sub> |  | 0.9 | 0.4 | 1.7 | 18.1 |
| Will Richard (GSW) | 98% | 18.8<br><sub>31,3,23,13,22</sub> | 4.8<br><sub>11,0,6,3,3</sub> |  | 2.3<br><sub>0,0,3,3,0</sub> |  | 1.1<br><sub>1,0,0,2,3</sub> |  | 0.6<br><sub>3,0,0,1,1</sub> |  | 1.0 | 0.2 | 0.6 | 8.2 |
| Gary Payton II (GSW) | 98% | 15.6<br><sub>17,12,10,8,15</sub> | 6.7<br><sub>2,7,2,2,5</sub> |  | 3.0<br><sub>1,2,2,4,2</sub> |  | 1.3<br><sub>0,0,1,0,2</sub> |  | 0.5<br><sub>0,1,0,0,1</sub> |  | 0.9 | 0.2 | 0.7 | 11.0 |
| Charles Bassey (GSW) | 93% | 15.4<br><sub>13,2,2,9,20</sub> | 5.9<br><sub>10,0,0,6,6</sub> |  | 6.2<br><sub>7,1,0,4,10</sub> |  | 0.8<br><sub>0,0,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.8 | 12.9 |
| Graham Ike (GSW) | 72% | 14.0<br><sub>26,3,-,-,6</sub> | 5.7<br><sub>12,3,-,-,2</sub> |  | 3.4<br><sub>10,0,-,-,2</sub> |  | 1.0<br><sub>2,1,-,-,0</sub> |  | 0.3<br><sub>0,1,-,-,0</sub> |  | 0.5 | 0.3 | 0.7 | 10.2 |
| LJ Cryer (GSW) | 58% | 9.6<br><sub>14,3,-,-,2</sub> | 3.7<br><sub>3,6,-,-,0</sub> |  | 0.9<br><sub>1,0,-,-,0</sub> |  | 0.7<br><sub>1,2,-,-,0</sub> |  | 0.5<br><sub>1,2,-,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.4 |
| Malevy Leons (GSW) | 48% | 9.0<br><sub>4,3,-,-,-</sub> | 2.5<br><sub>2,0,-,-,-</sub> |  | 1.6<br><sub>0,1,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.5 | 0.3 | 0.4 | 4.8 |
| Devin Booker (PHX) | 98% | 33.5<br><sub>29,36,34,39</sub> | 24.2<br><sub>23,43,3,20</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,7,2,2</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 5.8<br><sub>2,7,7,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>0,2,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 3.3 | 33.8 |
| Miles Bridges (PHX) | 98% | 30.8<br><sub>29,33,32,37</sub> | 15.6<br><sub>8,16,17,24</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>4,7,8,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>0,3,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>0,2,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.5 | 1.6 | 24.4 |
| Dillon Brooks (PHX) | 98% | 28.1<br><sub>27,34,33,21</sub> | 16.4<br><sub>10,15,19,22</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,2,5,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,5,5,2</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 2.0<br><sub>1,1,3,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 1.5 | 22.0 |
| Jalen Green (PHX) | 96% | 27.6<br><sub>25,26,31,25</sub> | 15.2<br><sub>10,12,20,2</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>2,2,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>3,1,4,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,1,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.3 | 2.4 | 21.8 |
| Collin Gillespie (PHX) | 98% | 26.2<br><sub>21,28,23,33</sub> | 10.0<br><sub>0,11,9,16</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,4,1,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>2,9,2,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.8<br><sub>0,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.2 | 1.5 | 17.6 |
| Oso Ighodaro (PHX) | 97% | 20.2<br><sub>15,-,-,21</sub> | 6.0<br><sub>8,-,-,2</sub> |  | 5.2<br><sub>3,-,-,9</sub> |  | 2.8<br><sub>3,-,-,5</sub> |  | 0.0<br><sub>0,-,-,0</sub> |  | 0.8 | 0.6 | 1.3 | 14.0 |
| Jordan Goodwin (PHX) | 98% | 19.0<br><sub>22,20,17,25</sub> | 7.1<br><sub>3,9,12,11</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,2,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,4,2,5</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.1<br><sub>1,1,4,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.1 | 0.8 | 12.8 |
| Khaman Maluach (PHX) | 96% | 17.2<br><sub>17,28,26,17</sub> | 6.1<br><sub>2,9,12,9</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>6,9,7,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>1,3,1,0</sub> |  | 0.2<br><sub>0,1,0,0</sub> |  | 0.4 | 0.9 | 1.1 | 11.9 |
| Luke Kennard (PHX) | 98% | 14.6<br><sub>-,18,16,12</sub> | 5.3<br><sub>-,11,9,9</sub> |  | 1.8<br><sub>-,4,1,1</sub> |  | 1.4<br><sub>-,1,2,2</sub> |  | 0.6<br><sub>-,3,3,1</sub> |  | 0.6 | 0.1 | 0.8 | 8.4 |
| Ryan Dunn (PHX) | 96% | 11.6<br><sub>14,13,14,11</sub> | 3.6<br><sub>3,5,6,5</sub> |  | 2.6<br><sub>2,5,2,3</sub> |  | 0.8<br><sub>0,0,1,1</sub> |  | 0.3<br><sub>0,1,1,1</sub> |  | 0.5 | 0.3 | 0.5 | 7.0 |
| Pat Spencer (PHX) | 64% | 7.7<br><sub>7,-,-,-</sub> | 2.7<br><sub>3,-,-,-</sub> |  | 1.0<br><sub>3,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.0 |
| Rasheer Fleming (PHX) | 58% | 6.7<br><sub>12,-,3,-</sub> | 2.4<br><sub>1,-,0,-</sub> |  | 1.3<br><sub>2,-,1,-</sub> |  | 0.3<br><sub>0,-,0,-</sub> |  | 0.2<br><sub>0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.0 |
| Duop Reath (PHX) | 64% | 6.5<br><sub>9,3,7,-</sub> | 2.5<br><sub>5,0,5,-</sub> |  | 1.4<br><sub>1,0,3,-</sub> |  | 0.3<br><sub>0,0,0,-</sub> |  | 0.2<br><sub>1,0,1,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |
| Jamaree Bouyea (PHX) | 58% | 6.3<br><sub>7,-,3,-</sub> | 2.6<br><sub>3,-,2,-</sub> |  | 0.9<br><sub>2,-,0,-</sub> |  | 0.9<br><sub>2,-,1,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Koa Peat (PHX) | 52% | 6.0<br><sub>7,-,3,-</sub> | 2.3<br><sub>4,-,0,-</sub> |  | 1.4<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>0,-,0,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.1 |

</details>

<details><summary>if Draymond Green plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski (GSW) | 88% | 33.3<br><sub>-,33,32,33,37</sub> | 18.3<br><sub>-,18,8,21,17</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.5<br><sub>-,7,5,5,8</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 4.9<br><sub>-,5,6,6,8</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.2<br><sub>-,3,0,4,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.2 | 2.0 | 28.7 |
| Yaxel Lendeborg (GSW) | 96% | 32.8<br><sub>36,31,35,24,34</sub> | 21.1<br><sub>26,31,26,6,37</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>9,12,9,1,4</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>5,6,1,0,6</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>6,1,2,1,6</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.9 | 0.5 | 3.2 | 31.5 |
| Draymond Green (GSW) | 100% | 29.3<br><sub>-,27,32,32,-</sub> | 8.4<br><sub>-,3,3,2,-</sub> | 4.5 · – | 5.7<br><sub>-,4,9,4,-</sub> | 4.5 | 5.7<br><sub>-,7,6,9,-</sub> | 6.5 | 1.0<br><sub>-,1,0,0,-</sub> |  | 1.1 | 0.7 | 2.7 | 19.8 |
| De'Anthony Melton (GSW) | 98% | 25.3<br><sub>27,19,20,21,28</sub> | 12.9<br><sub>25,3,8,16,21</sub> |  | 3.9<br><sub>5,4,6,5,6</sub> |  | 2.7<br><sub>5,3,0,3,3</sub> |  | 1.9<br><sub>4,1,2,4,6</sub> |  | 1.4 | 0.4 | 1.9 | 19.5 |
| Brandon Williams (GSW) | 98% | 22.3<br><sub>24,15,14,17,25</sub> | 13.7<br><sub>20,6,11,9,17</sub> |  | 2.9<br><sub>3,3,3,2,3</sub> |  | 3.6<br><sub>5,3,1,1,3</sub> |  | 0.8<br><sub>2,2,0,0,2</sub> |  | 1.0 | 0.3 | 1.9 | 20.2 |
| Georges Niang (GSW) | 96% | 22.0<br><sub>23,18,23,19,21</sub> | 8.8<br><sub>4,9,7,11,3</sub> |  | 3.0<br><sub>4,2,3,5,1</sub> |  | 1.3<br><sub>2,0,2,1,2</sub> |  | 1.5<br><sub>0,3,1,3,1</sub> |  | 0.4 | 0.2 | 1.2 | 13.1 |
| Al Horford (GSW) | 98% | 21.9<br><sub>-,19,18,17,22</sub> | 7.5<br><sub>-,11,4,3,9</sub> |  | 4.6<br><sub>-,3,5,2,5</sub> |  | 1.8<br><sub>-,0,2,0,2</sub> |  | 1.2<br><sub>-,3,0,1,3</sub> |  | 0.6 | 0.8 | 0.8 | 13.9 |
| Will Richard (GSW) | 98% | 20.6<br><sub>31,3,23,13,22</sub> | 5.8<br><sub>11,0,6,3,3</sub> |  | 2.5<br><sub>0,0,3,3,0</sub> |  | 1.3<br><sub>1,0,0,2,3</sub> |  | 0.8<br><sub>3,0,0,1,1</sub> |  | 1.1 | 0.2 | 0.7 | 9.6 |
| Gary Payton II (GSW) | 98% | 17.0<br><sub>17,12,10,8,15</sub> | 7.8<br><sub>2,7,2,2,5</sub> |  | 3.3<br><sub>1,2,2,4,2</sub> |  | 1.4<br><sub>0,0,1,0,2</sub> |  | 0.6<br><sub>0,1,0,0,1</sub> |  | 1.0 | 0.2 | 0.8 | 12.6 |
| Charles Bassey (GSW) | 93% | 15.2<br><sub>13,2,2,9,20</sub> | 6.2<br><sub>10,0,0,6,6</sub> |  | 6.2<br><sub>7,1,0,4,10</sub> |  | 0.7<br><sub>0,0,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 0.8 | 13.1 |
| Graham Ike (GSW) | 72% | 13.6<br><sub>26,3,-,-,6</sub> | 5.9<br><sub>12,3,-,-,2</sub> |  | 3.4<br><sub>10,0,-,-,2</sub> |  | 1.0<br><sub>2,1,-,-,0</sub> |  | 0.4<br><sub>0,1,-,-,0</sub> |  | 0.5 | 0.3 | 0.7 | 10.3 |
| LJ Cryer (GSW) | 58% | 11.2<br><sub>14,3,-,-,2</sub> | 4.8<br><sub>3,6,-,-,0</sub> |  | 1.1<br><sub>1,0,-,-,0</sub> |  | 0.8<br><sub>1,2,-,-,0</sub> |  | 0.7<br><sub>1,2,-,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 6.7 |
| Malevy Leons (GSW) | 48% | 8.9<br><sub>4,3,-,-,-</sub> | 2.7<br><sub>2,0,-,-,-</sub> |  | 1.6<br><sub>0,1,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.5 | 0.3 | 0.5 | 4.9 |
| Devin Booker (PHX) | 98% | 33.5<br><sub>29,36,34,39</sub> | 24.4<br><sub>23,43,3,20</sub> | 24.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,7,2,2</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 5.8<br><sub>2,7,7,5</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>0,2,0,3</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 3.3 | 34.0 |
| Miles Bridges (PHX) | 98% | 30.7<br><sub>29,33,32,37</sub> | 15.5<br><sub>8,16,17,24</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 6.2<br><sub>4,7,8,10</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.7<br><sub>0,3,4,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.7<br><sub>0,2,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 0.9 | 0.5 | 1.6 | 24.4 |
| Dillon Brooks (PHX) | 98% | 28.2<br><sub>27,34,33,21</sub> | 16.6<br><sub>10,15,19,22</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 3.7<br><sub>4,2,5,1</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>0,5,5,2</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 2.0<br><sub>1,1,3,4</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.2 | 1.5 | 22.1 |
| Jalen Green (PHX) | 96% | 27.6<br><sub>25,26,31,25</sub> | 15.3<br><sub>10,12,20,2</sub> | 15.5 · –<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>2,2,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.8<br><sub>3,1,4,2</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>2,1,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.3 | 2.4 | 21.8 |
| Collin Gillespie (PHX) | 98% | 26.3<br><sub>21,28,23,33</sub> | 10.0<br><sub>0,11,9,16</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 3.5<br><sub>1,4,1,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>2,9,2,10</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>0,2,3,4</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4 | 0.2 | 1.5 | 17.7 |
| Oso Ighodaro (PHX) | 97% | 20.1<br><sub>15,-,-,21</sub> | 6.0<br><sub>8,-,-,2</sub> |  | 5.2<br><sub>3,-,-,9</sub> |  | 2.8<br><sub>3,-,-,5</sub> |  | 0.0<br><sub>0,-,-,0</sub> |  | 0.8 | 0.6 | 1.3 | 14.0 |
| Jordan Goodwin (PHX) | 98% | 19.0<br><sub>22,20,17,25</sub> | 7.1<br><sub>3,9,12,11</sub> | 7.5 · –<br><sub>o 45% · u 55%</sub> | 3.9<br><sub>4,2,4,5</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>0,4,2,5</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 1.1<br><sub>1,1,4,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.4 | 0.1 | 0.8 | 12.8 |
| Khaman Maluach (PHX) | 96% | 17.2<br><sub>17,28,26,17</sub> | 6.1<br><sub>2,9,12,9</sub> | 7.5 · –<br><sub>o 46% · u 54%</sub> | 5.3<br><sub>6,9,7,6</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>1,3,1,0</sub> |  | 0.2<br><sub>0,1,0,0</sub> |  | 0.4 | 0.9 | 1.1 | 12.0 |
| Luke Kennard (PHX) | 98% | 14.6<br><sub>-,18,16,12</sub> | 5.3<br><sub>-,11,9,9</sub> |  | 1.8<br><sub>-,4,1,1</sub> |  | 1.4<br><sub>-,1,2,2</sub> |  | 0.6<br><sub>-,3,3,1</sub> |  | 0.5 | 0.1 | 0.7 | 8.5 |
| Ryan Dunn (PHX) | 96% | 11.7<br><sub>14,13,14,11</sub> | 3.7<br><sub>3,5,6,5</sub> |  | 2.6<br><sub>2,5,2,3</sub> |  | 0.8<br><sub>0,0,1,1</sub> |  | 0.3<br><sub>0,1,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 7.1 |
| Pat Spencer (PHX) | 64% | 7.6<br><sub>7,-,-,-</sub> | 2.7<br><sub>3,-,-,-</sub> |  | 0.9<br><sub>3,-,-,-</sub> |  | 1.3<br><sub>1,-,-,-</sub> |  | 0.2<br><sub>1,-,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 4.9 |
| Rasheer Fleming (PHX) | 58% | 6.8<br><sub>12,-,3,-</sub> | 2.5<br><sub>1,-,0,-</sub> |  | 1.3<br><sub>2,-,1,-</sub> |  | 0.3<br><sub>0,-,0,-</sub> |  | 0.2<br><sub>0,-,0,-</sub> |  | 0.3 | 0.2 | 0.4 | 4.0 |
| Duop Reath (PHX) | 64% | 6.4<br><sub>9,3,7,-</sub> | 2.5<br><sub>5,0,5,-</sub> |  | 1.3<br><sub>1,0,3,-</sub> |  | 0.3<br><sub>0,0,0,-</sub> |  | 0.2<br><sub>1,0,1,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |
| Jamaree Bouyea (PHX) | 58% | 6.3<br><sub>7,-,3,-</sub> | 2.6<br><sub>3,-,2,-</sub> |  | 0.9<br><sub>2,-,0,-</sub> |  | 0.9<br><sub>2,-,1,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Koa Peat (PHX) | 52% | 6.0<br><sub>7,-,3,-</sub> | 2.4<br><sub>4,-,0,-</sub> |  | 1.4<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>0,-,0,-</sub> |  | 0.1<br><sub>0,-,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 4.2 |

</details>


### TOR @ LAC
Out: Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC), Kawhi Leonard (TOR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Immanuel Quickley 3PM under 2.5 | TOR @ LAC | draftkings | 2.21 | 2.21 | 1.84 | 54.5% | 42.3% | 45.3% | +0.2% | +20.4% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.3–109.4 | TOR 58% | 1.73 / 2.37 | LAC +3.5 | 221.5 | LAC +4.5 covers 54%; o221.5 50% |
| Expected (weighted by chance each plays) | 112.6–110.2 | TOR 57% | 1.76 / 2.31 | LAC +2.5 | 222.5 | LAC +4.5 covers 55%; o221.5 53% |
| if Derrick Jones Jr. plays | 111.9–110.6 | TOR 53% | 1.88 / 2.14 | LAC +1.5 | 222.5 | LAC +4.5 covers 59%; o221.5 52% |
| if Jakob Poeltl plays | 113.6–109.9 | TOR 60% | 1.67 / 2.50 | LAC +3.5 | 223.5 | LAC +4.5 covers 52%; o221.5 54% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick Jones Jr. (LAC) | Day-To-Day | 70% | 28.0 | 10.8 | 4.0 | 1.3 | 1.2 | 1.0 | 0.8 | 1.0 | 16.1 | full tables below |
| Jakob Poeltl (TOR) | Day-To-Day | 70% | 20.3 | 7.9 | 5.8 | 1.4 | 0.0 | 0.8 | 0.6 | 1.1 | 15.1 | full tables below |

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 35.6<br><sub>37,28,31,39,36</sub> | 22.5<br><sub>28,0,28,41,29</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>14,3,6,5,6</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 6.6<br><sub>5,3,4,5,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,0,0,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.8 | 1.1 | 3.2 | 36.1 |
| RJ Barrett | 98% | 34.3<br><sub>34,32,32,34,32</sub> | 21.4<br><sub>23,20,25,9,22</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>9,2,9,3,10</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,2,6,5,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>1,0,3,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 2.5 | 31.4 |
| Immanuel Quickley | 98% | 31.9<br><sub>29,28,29,37,33</sub> | 17.1<br><sub>12,19,16,17,12</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>1,3,3,6,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>6,2,7,8,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>0,3,4,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.1 | 1.7 | 27.0 |
| Ja'Kobe Walter | 98% | 31.1<br><sub>24,31,28,32,33</sub> | 11.9<br><sub>7,22,14,9,11</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,4,5,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>2,2,2,1,2</sub> |  | 2.1<br><sub>2,5,3,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.3 | 1.0 | 17.6 |
| Jamal Shead | 98% | 26.0<br><sub>24,21,23,23,25</sub> | 8.1<br><sub>5,4,13,2,9</sub> |  | 1.9<br><sub>2,1,4,1,2</sub> |  | 5.3<br><sub>5,0,7,8,6</sub> |  | 1.0<br><sub>0,0,1,0,2</sub> |  | 1.2 | 0.2 | 1.9 | 15.3 |
| Collin Murray-Boyles | 98% | 24.0<br><sub>18,19,15,23,20</sub> | 10.2<br><sub>8,3,10,15,4</sub> |  | 5.7<br><sub>3,7,2,5,3</sub> |  | 1.9<br><sub>0,2,1,1,1</sub> |  | 0.2<br><sub>0,0,2,1,0</sub> |  | 1.1 | 0.8 | 1.3 | 17.8 |
| Jamison Battle | 97% | 18.2<br><sub>12,13,20,19,17</sub> | 7.3<br><sub>5,4,7,2,20</sub> |  | 2.6<br><sub>0,1,0,0,5</sub> |  | 0.9<br><sub>0,2,1,0,0</sub> |  | 1.0<br><sub>1,1,1,0,4</sub> |  | 0.4 | 0.1 | 0.7 | 10.8 |
| Malachi Smith | 23% | 16.1 | 5.4 |  | 2.4 |  | 1.9 |  | 0.5 |  | 0.6 | 0.2 | 0.7 | 9.7 |
| Allen Graves | 96% | 14.3<br><sub>6,20,18,9,10</sub> | 4.6<br><sub>2,11,3,7,3</sub> |  | 2.8<br><sub>2,6,1,4,0</sub> |  | 0.8<br><sub>0,4,0,0,0</sub> |  | 0.3<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.5 | 0.7 | 8.2 |
| Alijah Martin | 76% | 12.1<br><sub>1,7,5,-,16</sub> | 4.8<br><sub>0,2,5,-,5</sub> |  | 1.7<br><sub>0,2,1,-,2</sub> |  | 1.3<br><sub>0,1,1,-,4</sub> |  | 0.4<br><sub>0,0,1,-,1</sub> |  | 0.5 | 0.2 | 0.8 | 7.8 |
| Kyle Anderson | 66% | 10.9<br><sub>-,11,5,-,4</sub> | 3.2<br><sub>-,0,0,-,2</sub> |  | 2.1<br><sub>-,2,0,-,3</sub> |  | 1.7<br><sub>-,0,1,-,3</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.9 |
| Trayce Jackson-Davis | 91% | 10.0<br><sub>1,6,20,1,9</sub> | 3.8<br><sub>0,3,6,0,5</sub> |  | 3.1<br><sub>0,1,11,0,5</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 7.6 |
| Jaden Bradley | 72% | 7.7<br><sub>1,5,5,-,4</sub> | 2.5<br><sub>0,6,0,-,3</sub> |  | 1.3<br><sub>0,1,1,-,1</sub> |  | 0.9<br><sub>0,1,1,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 4.6 |

</details>

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 33.3<br><sub>37,36,26,31,33</sub> | 22.4<br><sub>26,16,14,24,15</sub> |  | 2.5<br><sub>0,4,1,2,0</sub> |  | 6.7<br><sub>6,11,5,5,7</sub> |  | 2.8<br><sub>4,2,1,4,1</sub> |  | 1.2 | 0.2 | 3.9 | 31.5 |
| Rui Hachimura | 98% | 33.0<br><sub>33,29,-,26,30</sub> | 16.3<br><sub>16,5,-,12,24</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>6,4,-,5,7</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>1,0,-,0,0</sub> |  | 2.1<br><sub>3,1,-,2,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.4 | 1.6 | 22.2 |
| Kris Dunn | 98% | 30.0<br><sub>34,33,27,31,27</sub> | 8.1<br><sub>7,15,5,5,12</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>5,4,3,5,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>5,6,3,7,4</sub> |  | 0.9<br><sub>1,1,1,0,0</sub> |  | 2.0 | 0.3 | 1.6 | 16.1 |
| Keaton Wagler | 96% | 26.1<br><sub>24,26,28,25,19</sub> | 12.5<br><sub>13,11,21,12,7</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>3,5,4,6,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,4,2,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>2,1,3,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 2.2 | 19.5 |
| Kobe Sanders | 96% | 25.9<br><sub>19,20,27,24,30</sub> | 10.7<br><sub>5,12,9,7,16</sub> |  | 2.9<br><sub>3,4,4,4,3</sub> |  | 2.0<br><sub>5,2,0,2,0</sub> |  | 1.4<br><sub>1,2,1,1,4</sub> |  | 1.1 | 0.2 | 1.5 | 15.6 |
| Brook Lopez | 98% | 25.0<br><sub>20,23,22,21,19</sub> | 11.6<br><sub>22,15,2,13,7</sub> |  | 4.5<br><sub>4,1,3,6,2</sub> |  | 1.4<br><sub>0,2,3,0,0</sub> |  | 1.4<br><sub>2,3,0,1,1</sub> |  | 0.6 | 1.3 | 1.2 | 17.4 |
| Isaiah Jackson | 97% | 23.9<br><sub>28,24,19,22,22</sub> | 9.8<br><sub>6,10,4,10,5</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>6,6,5,7,8</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,4,1,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.3 | 1.6 | 18.6 |
| Gradey Dick | 91% | 14.2<br><sub>12,18,19,12,3</sub> | 5.8<br><sub>6,6,5,3,0</sub> |  | 2.1<br><sub>4,3,5,0,1</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>0,2,1,1,0</sub> |  | 0.5 | 0.1 | 0.8 | 8.7 |
| Baba Miller | 88% | 13.4<br><sub>-,2,17,5,6</sub> | 5.5<br><sub>-,0,4,0,2</sub> |  | 2.1<br><sub>-,1,7,1,2</sub> |  | 1.3<br><sub>-,0,1,0,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 8.9 |
| Nick Martinelli | 67% | 11.8<br><sub>-,-,6,5,6</sub> | 4.6<br><sub>-,-,2,3,10</sub> |  | 2.8<br><sub>-,-,3,0,3</sub> |  | 0.7<br><sub>-,-,1,0,0</sub> |  | 0.5<br><sub>-,-,0,0,2</sub> |  | 0.4 | 0.2 | 0.7 | 8.1 |
| Cam Christie | 71% | 11.5<br><sub>-,-,14,5,6</sub> | 3.6<br><sub>-,-,2,2,3</sub> |  | 1.8<br><sub>-,-,0,1,1</sub> |  | 0.7<br><sub>-,-,0,1,0</sub> |  | 0.2<br><sub>-,-,0,0,1</sub> |  | 0.5 | 0.1 | 0.7 | 6.1 |
| Jalen Pickett | 58% | 9.7<br><sub>-,-,8,-,6</sub> | 3.3<br><sub>-,-,4,-,0</sub> |  | 1.2<br><sub>-,-,1,-,2</sub> |  | 1.1<br><sub>-,-,1,-,3</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.7 |
| Blake Wesley | 88% | 8.8<br><sub>-,-,-,5,4</sub> | 3.3<br><sub>-,-,-,0,2</sub> |  | 1.1<br><sub>-,-,-,4,0</sub> |  | 0.9<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 5.3 |

</details>

<details><summary>if Jakob Poeltl plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland (LAC) | 98% | 33.2<br><sub>37,36,26,31,33</sub> | 22.3<br><sub>26,16,14,24,15</sub> |  | 2.5<br><sub>0,4,1,2,0</sub> |  | 6.6<br><sub>6,11,5,5,7</sub> |  | 2.8<br><sub>4,2,1,4,1</sub> |  | 1.2 | 0.2 | 3.9 | 31.4 |
| Rui Hachimura (LAC) | 98% | 32.9<br><sub>33,29,-,26,30</sub> | 16.3<br><sub>16,5,-,12,24</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.7<br><sub>6,4,-,5,7</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>1,0,-,0,0</sub> |  | 2.1<br><sub>3,1,-,2,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.4 | 1.6 | 22.3 |
| Kris Dunn (LAC) | 98% | 29.9<br><sub>34,33,27,31,27</sub> | 8.0<br><sub>7,15,5,5,12</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>5,4,3,5,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.3<br><sub>5,6,3,7,4</sub> |  | 0.9<br><sub>1,1,1,0,0</sub> |  | 2.0 | 0.3 | 1.6 | 16.0 |
| Keaton Wagler (LAC) | 96% | 26.2<br><sub>24,26,28,25,19</sub> | 12.5<br><sub>13,11,21,12,7</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>3,5,4,6,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.2<br><sub>3,4,2,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.5<br><sub>2,1,3,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 2.2 | 19.6 |
| Kobe Sanders (LAC) | 96% | 25.9<br><sub>19,20,27,24,30</sub> | 10.7<br><sub>5,12,9,7,16</sub> |  | 2.9<br><sub>3,4,4,4,3</sub> |  | 2.0<br><sub>5,2,0,2,0</sub> |  | 1.5<br><sub>1,2,1,1,4</sub> |  | 1.1 | 0.2 | 1.5 | 15.6 |
| Brook Lopez (LAC) | 98% | 25.0<br><sub>20,23,22,21,19</sub> | 11.6<br><sub>22,15,2,13,7</sub> |  | 4.5<br><sub>4,1,3,6,2</sub> |  | 1.4<br><sub>0,2,3,0,0</sub> |  | 1.4<br><sub>2,3,0,1,1</sub> |  | 0.6 | 1.2 | 1.2 | 17.4 |
| Isaiah Jackson (LAC) | 97% | 23.8<br><sub>28,24,19,22,22</sub> | 9.8<br><sub>6,10,4,10,5</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 7.1<br><sub>6,6,5,7,8</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>3,4,1,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.3 | 1.7 | 18.6 |
| Gradey Dick (LAC) | 91% | 14.3<br><sub>12,18,19,12,3</sub> | 5.8<br><sub>6,6,5,3,0</sub> |  | 2.1<br><sub>4,3,5,0,1</sub> |  | 0.7<br><sub>0,0,0,1,0</sub> |  | 0.6<br><sub>0,2,1,1,0</sub> |  | 0.5 | 0.1 | 0.8 | 8.7 |
| Baba Miller (LAC) | 88% | 13.4<br><sub>-,2,17,5,6</sub> | 5.6<br><sub>-,0,4,0,2</sub> |  | 2.1<br><sub>-,1,7,1,2</sub> |  | 1.3<br><sub>-,0,1,0,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 8.9 |
| Cam Christie (LAC) | 71% | 11.7<br><sub>-,-,14,5,6</sub> | 3.6<br><sub>-,-,2,2,3</sub> |  | 1.8<br><sub>-,-,0,1,1</sub> |  | 0.7<br><sub>-,-,0,1,0</sub> |  | 0.2<br><sub>-,-,0,0,1</sub> |  | 0.5 | 0.1 | 0.7 | 6.2 |
| Nick Martinelli (LAC) | 67% | 11.7<br><sub>-,-,6,5,6</sub> | 4.6<br><sub>-,-,2,3,10</sub> |  | 2.8<br><sub>-,-,3,0,3</sub> |  | 0.7<br><sub>-,-,1,0,0</sub> |  | 0.5<br><sub>-,-,0,0,2</sub> |  | 0.4 | 0.2 | 0.7 | 8.1 |
| Jalen Pickett (LAC) | 58% | 9.9<br><sub>-,-,8,-,6</sub> | 3.4<br><sub>-,-,4,-,0</sub> |  | 1.3<br><sub>-,-,1,-,2</sub> |  | 1.2<br><sub>-,-,1,-,3</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 5.8 |
| Blake Wesley (LAC) | 88% | 8.8<br><sub>-,-,-,5,4</sub> | 3.3<br><sub>-,-,-,0,2</sub> |  | 1.1<br><sub>-,-,-,4,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.1 | 0.7 | 5.4 |
| Scottie Barnes (TOR) | 98% | 34.4<br><sub>37,28,31,39,36</sub> | 22.0<br><sub>28,0,28,41,29</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 6.7<br><sub>14,3,6,5,6</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 6.6<br><sub>5,3,4,5,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,0,0,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.7 | 1.1 | 3.3 | 35.3 |
| RJ Barrett (TOR) | 98% | 33.2<br><sub>34,32,32,34,32</sub> | 20.7<br><sub>23,20,25,9,22</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 5.8<br><sub>9,2,9,3,10</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,2,6,5,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.8<br><sub>1,0,3,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 2.4 | 30.4 |
| Immanuel Quickley (TOR) | 98% | 30.6<br><sub>29,28,29,37,33</sub> | 16.3<br><sub>12,19,16,17,12</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 3.7<br><sub>1,3,3,6,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>6,2,7,8,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>0,3,4,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.2 | 0.1 | 1.6 | 25.8 |
| Ja'Kobe Walter (TOR) | 98% | 29.1<br><sub>24,31,28,32,33</sub> | 11.1<br><sub>7,22,14,9,11</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.4<br><sub>4,4,5,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>2,2,2,1,2</sub> |  | 1.9<br><sub>2,5,3,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.3 | 1.0 | 16.4 |
| Jamal Shead (TOR) | 98% | 23.4<br><sub>24,21,23,23,25</sub> | 7.2<br><sub>5,4,13,2,9</sub> |  | 1.7<br><sub>2,1,4,1,2</sub> |  | 5.0<br><sub>5,0,7,8,6</sub> |  | 0.8<br><sub>0,0,1,0,2</sub> |  | 1.1 | 0.2 | 1.8 | 13.9 |
| Collin Murray-Boyles (TOR) | 98% | 21.3<br><sub>18,19,15,23,20</sub> | 9.1<br><sub>8,3,10,15,4</sub> |  | 4.9<br><sub>3,7,2,5,3</sub> |  | 1.7<br><sub>0,2,1,1,1</sub> |  | 0.2<br><sub>0,0,2,1,0</sub> |  | 1.0 | 0.7 | 1.2 | 15.8 |
| Jakob Poeltl (TOR) | 100% | 20.3<br><sub>27,19,10,23,-</sub> | 7.9<br><sub>6,0,2,12,-</sub> | 8.5 · – | 5.8<br><sub>9,1,2,11,-</sub> | 6.5 | 1.4<br><sub>2,0,0,3,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.8 | 0.6 | 1.1 | 15.1 |
| Jamison Battle (TOR) | 97% | 16.2<br><sub>12,13,20,19,17</sub> | 6.7<br><sub>5,4,7,2,20</sub> |  | 2.3<br><sub>0,1,0,0,5</sub> |  | 0.8<br><sub>0,2,1,0,0</sub> |  | 0.9<br><sub>1,1,1,0,4</sub> |  | 0.4 | 0.1 | 0.6 | 9.7 |
| Malachi Smith (TOR) | 23% | 13.7 | 4.8 |  | 2.1 |  | 1.7 |  | 0.4 |  | 0.5 | 0.2 | 0.6 | 8.6 |
| Allen Graves (TOR) | 96% | 13.2<br><sub>6,20,18,9,10</sub> | 4.4<br><sub>2,11,3,7,3</sub> |  | 2.6<br><sub>2,6,1,4,0</sub> |  | 0.7<br><sub>0,4,0,0,0</sub> |  | 0.3<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.4 | 0.7 | 7.7 |
| Alijah Martin (TOR) | 76% | 9.3<br><sub>1,7,5,-,16</sub> | 3.9<br><sub>0,2,5,-,5</sub> |  | 1.3<br><sub>0,2,1,-,2</sub> |  | 1.1<br><sub>0,1,1,-,4</sub> |  | 0.3<br><sub>0,0,1,-,1</sub> |  | 0.4 | 0.1 | 0.6 | 6.3 |
| Trayce Jackson-Davis (TOR) | 91% | 9.0<br><sub>1,6,20,1,9</sub> | 3.7<br><sub>0,3,6,0,5</sub> |  | 2.8<br><sub>0,1,11,0,5</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 7.1 |
| Kyle Anderson (TOR) | 66% | 8.3<br><sub>-,11,5,-,4</sub> | 2.5<br><sub>-,0,0,-,2</sub> |  | 1.6<br><sub>-,2,0,-,3</sub> |  | 1.3<br><sub>-,0,1,-,3</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 5.5 |
| Jaden Bradley (TOR) | 72% | 6.4<br><sub>1,5,5,-,4</sub> | 2.2<br><sub>0,6,0,-,3</sub> |  | 1.1<br><sub>0,1,1,-,1</sub> |  | 0.8<br><sub>0,1,1,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.1 |

</details>

<details><summary>if Derrick Jones Jr. plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland (LAC) | 98% | 31.8<br><sub>37,36,26,31,33</sub> | 21.1<br><sub>26,16,14,24,15</sub> |  | 2.4<br><sub>0,4,1,2,0</sub> |  | 6.3<br><sub>6,11,5,5,7</sub> |  | 2.6<br><sub>4,2,1,4,1</sub> |  | 1.1 | 0.2 | 3.6 | 29.7 |
| Rui Hachimura (LAC) | 98% | 30.5<br><sub>33,29,-,26,30</sub> | 15.1<br><sub>16,5,-,12,24</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>6,4,-,5,7</sub> | 5.5<br><sub>o 40% · u 60%</sub> | 1.2<br><sub>1,0,-,0,0</sub> |  | 1.9<br><sub>3,1,-,2,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.4 | 1.5 | 20.7 |
| Derrick Jones Jr. (LAC) | 100% | 28.0<br><sub>35,30,28,26,28</sub> | 10.8<br><sub>16,11,15,10,9</sub> |  | 4.0<br><sub>4,6,5,1,7</sub> |  | 1.3<br><sub>1,1,0,1,1</sub> |  | 1.2<br><sub>3,3,3,2,1</sub> |  | 1.0 | 0.8 | 1.0 | 16.1 |
| Kris Dunn (LAC) | 98% | 27.4<br><sub>34,33,27,31,27</sub> | 7.5<br><sub>7,15,5,5,12</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>5,4,3,5,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 3.9<br><sub>5,6,3,7,4</sub> |  | 0.8<br><sub>1,1,1,0,0</sub> |  | 1.8 | 0.3 | 1.4 | 14.8 |
| Keaton Wagler (LAC) | 96% | 23.4<br><sub>24,26,28,25,19</sub> | 11.2<br><sub>13,11,21,12,7</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>3,5,4,6,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>3,4,2,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>2,1,3,1,0</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.8 | 0.2 | 2.0 | 17.7 |
| Kobe Sanders (LAC) | 96% | 22.8<br><sub>19,20,27,24,30</sub> | 9.6<br><sub>5,12,9,7,16</sub> |  | 2.6<br><sub>3,4,4,4,3</sub> |  | 1.7<br><sub>5,2,0,2,0</sub> |  | 1.2<br><sub>1,2,1,1,4</sub> |  | 0.9 | 0.2 | 1.4 | 13.9 |
| Brook Lopez (LAC) | 98% | 21.7<br><sub>20,23,22,21,19</sub> | 10.2<br><sub>22,15,2,13,7</sub> |  | 4.0<br><sub>4,1,3,6,2</sub> |  | 1.2<br><sub>0,2,3,0,0</sub> |  | 1.2<br><sub>2,3,0,1,1</sub> |  | 0.5 | 1.1 | 1.1 | 15.5 |
| Isaiah Jackson (LAC) | 97% | 20.3<br><sub>28,24,19,22,22</sub> | 8.5<br><sub>6,10,4,10,5</sub> | 8.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>6,6,5,7,8</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>3,4,1,4,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.1 | 1.5 | 16.2 |
| Baba Miller (LAC) | 88% | 11.9<br><sub>-,2,17,5,6</sub> | 5.0<br><sub>-,0,4,0,2</sub> |  | 1.9<br><sub>-,1,7,1,2</sub> |  | 1.1<br><sub>-,0,1,0,1</sub> |  | 0.2<br><sub>-,0,0,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 8.0 |
| Gradey Dick (LAC) | 91% | 11.7<br><sub>12,18,19,12,3</sub> | 4.9<br><sub>6,6,5,3,0</sub> |  | 1.8<br><sub>4,3,5,0,1</sub> |  | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.5<br><sub>0,2,1,1,0</sub> |  | 0.5 | 0.1 | 0.7 | 7.3 |
| Cam Christie (LAC) | 71% | 8.5<br><sub>-,-,14,5,6</sub> | 3.0<br><sub>-,-,2,2,3</sub> |  | 1.3<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.1<br><sub>-,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 4.8 |
| Nick Martinelli (LAC) | 67% | 8.4<br><sub>-,-,6,5,6</sub> | 3.7<br><sub>-,-,2,3,10</sub> |  | 2.0<br><sub>-,-,3,0,3</sub> |  | 0.6<br><sub>-,-,1,0,0</sub> |  | 0.3<br><sub>-,-,0,0,2</sub> |  | 0.3 | 0.2 | 0.5 | 6.2 |
| Jalen Pickett (LAC) | 58% | 8.2<br><sub>-,-,8,-,6</sub> | 2.9<br><sub>-,-,4,-,0</sub> |  | 1.1<br><sub>-,-,1,-,2</sub> |  | 1.0<br><sub>-,-,1,-,3</sub> |  | 0.2<br><sub>-,-,0,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Blake Wesley (LAC) | 88% | 7.0<br><sub>-,-,-,5,4</sub> | 2.9<br><sub>-,-,-,0,2</sub> |  | 0.8<br><sub>-,-,-,4,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |
| Scottie Barnes (TOR) | 98% | 35.6<br><sub>37,28,31,39,36</sub> | 22.5<br><sub>28,0,28,41,29</sub> | 23.5 · –<br><sub>o 48% · u 52%</sub> | 7.0<br><sub>14,3,6,5,6</sub> | 7.5<br><sub>o 43% · u 57%</sub> | 6.6<br><sub>5,3,4,5,5</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.9<br><sub>1,0,0,1,0</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 1.8 | 1.1 | 3.2 | 36.1 |
| RJ Barrett (TOR) | 98% | 34.3<br><sub>34,32,32,34,32</sub> | 21.3<br><sub>23,20,25,9,22</sub> | 21.5 · –<br><sub>o 46% · u 54%</sub> | 6.2<br><sub>9,2,9,3,10</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>4,2,6,5,5</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 1.9<br><sub>1,0,3,1,4</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.3 | 2.5 | 31.4 |
| Immanuel Quickley (TOR) | 98% | 32.0<br><sub>29,28,29,37,33</sub> | 17.1<br><sub>12,19,16,17,12</sub> | 18.5 · –<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>1,3,3,6,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>6,2,7,8,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>0,3,4,4,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.3 | 0.1 | 1.7 | 27.0 |
| Ja'Kobe Walter (TOR) | 98% | 30.9<br><sub>24,31,28,32,33</sub> | 11.8<br><sub>7,22,14,9,11</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 3.7<br><sub>4,4,5,3,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>2,2,2,1,2</sub> |  | 2.1<br><sub>2,5,3,3,3</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.3 | 1.0 | 17.4 |
| Jamal Shead (TOR) | 98% | 26.1<br><sub>24,21,23,23,25</sub> | 8.1<br><sub>5,4,13,2,9</sub> |  | 1.9<br><sub>2,1,4,1,2</sub> |  | 5.4<br><sub>5,0,7,8,6</sub> |  | 1.0<br><sub>0,0,1,0,2</sub> |  | 1.2 | 0.2 | 2.0 | 15.4 |
| Collin Murray-Boyles (TOR) | 98% | 24.0<br><sub>18,19,15,23,20</sub> | 10.3<br><sub>8,3,10,15,4</sub> |  | 5.7<br><sub>3,7,2,5,3</sub> |  | 1.9<br><sub>0,2,1,1,1</sub> |  | 0.2<br><sub>0,0,2,1,0</sub> |  | 1.1 | 0.8 | 1.3 | 17.9 |
| Jamison Battle (TOR) | 97% | 18.2<br><sub>12,13,20,19,17</sub> | 7.3<br><sub>5,4,7,2,20</sub> |  | 2.6<br><sub>0,1,0,0,5</sub> |  | 0.9<br><sub>0,2,1,0,0</sub> |  | 1.0<br><sub>1,1,1,0,4</sub> |  | 0.4 | 0.2 | 0.7 | 10.8 |
| Malachi Smith (TOR) | 23% | 15.9 | 5.3 |  | 2.4 |  | 1.9 |  | 0.5 |  | 0.6 | 0.2 | 0.7 | 9.7 |
| Allen Graves (TOR) | 96% | 14.3<br><sub>6,20,18,9,10</sub> | 4.6<br><sub>2,11,3,7,3</sub> |  | 2.8<br><sub>2,6,1,4,0</sub> |  | 0.8<br><sub>0,4,0,0,0</sub> |  | 0.3<br><sub>0,1,0,1,0</sub> |  | 0.4 | 0.5 | 0.8 | 8.2 |
| Alijah Martin (TOR) | 76% | 12.1<br><sub>1,7,5,-,16</sub> | 4.8<br><sub>0,2,5,-,5</sub> |  | 1.7<br><sub>0,2,1,-,2</sub> |  | 1.4<br><sub>0,1,1,-,4</sub> |  | 0.4<br><sub>0,0,1,-,1</sub> |  | 0.5 | 0.2 | 0.8 | 7.8 |
| Kyle Anderson (TOR) | 66% | 10.8<br><sub>-,11,5,-,4</sub> | 3.2<br><sub>-,0,0,-,2</sub> |  | 2.1<br><sub>-,2,0,-,3</sub> |  | 1.6<br><sub>-,0,1,-,3</sub> |  | 0.0<br><sub>-,0,0,-,0</sub> |  | 0.5 | 0.3 | 0.6 | 6.9 |
| Trayce Jackson-Davis (TOR) | 91% | 10.0<br><sub>1,6,20,1,9</sub> | 3.8<br><sub>0,3,6,0,5</sub> |  | 3.1<br><sub>0,1,11,0,5</sub> |  | 0.7<br><sub>0,1,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.5 | 7.6 |
| Jaden Bradley (TOR) | 72% | 7.6<br><sub>1,5,5,-,4</sub> | 2.4<br><sub>0,6,0,-,3</sub> |  | 1.2<br><sub>0,1,1,-,1</sub> |  | 0.9<br><sub>0,1,1,-,2</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 4.6 |

</details>


### MIA @ LAL
Out: Ziaire Williams (LAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Bam Adebayo 3PM over 1.5 (2+) | MIA @ LAL | draftkings | 2.52 | 2.50 | 2.06 | 48.5% | 37.2% | 40.0% | +0.8% | +22.2% | 0.1% |
| Davion Mitchell REB over 2.5 (3+) | MIA @ LAL | draftkings | 2.24 | 2.23 | 1.85 | 54.0% | 41.8% | 44.9% | +0.5% | +20.9% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 117.9–121.4 | MIA 41% | 2.47 / 1.68 | LAL -3.5 | 238.5 | LAL -2.5 covers 54%; o237.5 53% |
| Expected (weighted by chance each plays) | 118.1–121.0 | MIA 42% | 2.38 / 1.72 | LAL -3.5 | 238.5 | LAL -2.5 covers 52%; o237.5 53% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tim Hardaway Jr. (MIA) | Questionable | 55% | 15.7 | 6.5 | 1.7 | 0.8 | 0.8 | 0.4 | 0.1 | 0.5 | 9.0 | small |

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 35.0<br><sub>33,37,33,34,35</sub> | 13.3<br><sub>18,22,21,10,15</sub> | 12.5 · –<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>2,1,0,1,6</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 7.6<br><sub>5,10,2,10,11</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>3,3,2,0,3</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.2 | 2.3 | 23.8 |
| Bam Adebayo | 98% | 34.6<br><sub>23,39,30,33,33</sub> | 19.4<br><sub>4,20,8,24,27</sub> | 19.5 · –<br><sub>o 46% · u 54%</sub> | 9.8<br><sub>6,8,8,9,9</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 3.5<br><sub>3,4,3,3,3</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.7<br><sub>0,2,0,0,0</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.6 | 0.5 | 2.0 | 32.7 |
| Giannis Antetokounmpo | 98% | 32.9<br><sub>33,25,39,31,31</sub> | 28.1<br><sub>36,14,29,24,31</sub> | 31.5 · –<br><sub>o 45% · u 55%</sub> | 11.5<br><sub>12,6,14,18,18</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 6.0<br><sub>5,3,11,3,10</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.5<br><sub>1,0,2,0,1</sub> |  | 1.1 | 0.7 | 3.3 | 45.7 |
| Pelle Larsson | 98% | 31.4<br><sub>29,36,34,31,24</sub> | 12.3<br><sub>7,15,12,17,18</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>2,7,0,6,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>1,4,4,8,3</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.0<br><sub>1,1,1,2,1</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.2 | 1.9 | 20.0 |
| Andrew Wiggins | 98% | 30.2<br><sub>26,18,34,29,30</sub> | 13.7<br><sub>8,4,12,18,12</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.3<br><sub>8,1,3,2,2</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>2,1,1,2,1</sub> |  | 1.8<br><sub>1,0,0,4,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.0 | 0.8 | 1.5 | 20.1 |
| Bobby Portis | 98% | 22.9<br><sub>21,27,24,23,17</sub> | 11.1<br><sub>11,13,10,11,8</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 6.3<br><sub>8,8,12,9,3</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>2,0,2,4,1</sub> |  | 1.6<br><sub>3,2,3,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 0.7 | 0.3 | 1.0 | 18.8 |
| Klay Thompson | 98% | 22.5<br><sub>24,27,15,17,26</sub> | 10.8<br><sub>6,14,6,3,25</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,3,1,1,0</sub> |  | 1.4<br><sub>2,0,1,2,3</sub> |  | 2.0<br><sub>2,4,2,1,7</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.5 | 0.3 | 1.0 | 14.3 |
| Nikola Jovic | 72% | 13.4<br><sub>13,6,-,7,16</sub> | 4.4<br><sub>5,0,-,5,0</sub> |  | 2.6<br><sub>4,2,-,3,4</sub> |  | 1.2<br><sub>1,0,-,0,3</sub> |  | 0.5<br><sub>0,0,-,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 8.3 |
| Dru Smith | 71% | 12.2<br><sub>6,-,15,14,4</sub> | 3.7<br><sub>3,-,6,3,0</sub> |  | 1.6<br><sub>0,-,2,0,0</sub> |  | 1.8<br><sub>1,-,1,3,1</sub> |  | 0.3<br><sub>1,-,2,0,0</sub> |  | 1.0 | 0.2 | 0.7 | 7.0 |
| Keshad Johnson | 23% | 9.6 | 4.3 |  | 2.1 |  | 0.5 |  | 0.3 |  | 0.5 | 0.2 | 0.5 | 6.8 |
| Simone Fontecchio | 52% | 8.6<br><sub>3,-,-,-,2</sub> | 4.1<br><sub>0,-,-,-,3</sub> |  | 1.6<br><sub>1,-,-,-,1</sub> |  | 0.7<br><sub>0,-,-,-,0</sub> |  | 0.5<br><sub>0,-,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 6.4 |
| Ryan Conwell | 63% | 7.8<br><sub>3,4,-,-,7</sub> | 2.5<br><sub>2,3,-,-,4</sub> |  | 1.5<br><sub>0,1,-,-,0</sub> |  | 0.7<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,1,-,-,1</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Myron Gardner | 52% | 7.5<br><sub>3,-,-,-,2</sub> | 2.7<br><sub>0,-,-,-,0</sub> |  | 2.1<br><sub>0,-,-,-,1</sub> |  | 0.8<br><sub>0,-,-,-,1</sub> |  | 0.2<br><sub>0,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 5.6 |
| Nick Richards | 58% | 7.1<br><sub>3,-,-,-,2</sub> | 2.5<br><sub>3,-,-,-,0</sub> |  | 2.5<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>1,-,-,-,0</sub> |  | 0.1<br><sub>1,-,-,-,0</sub> |  | 0.1 | 0.3 | 0.5 | 5.3 |

</details>

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 35.9<br><sub>38,37,-,37,35</sub> | 35.4<br><sub>52,41,-,37,45</sub> | 33.5 · –<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>8,5,-,7,15</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 8.0<br><sub>10,9,-,5,6</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>8,6,-,6,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7 | 0.5 | 4.1 | 50.8 |
| Austin Reaves | 98% | 35.7<br><sub>36,39,31,37,39</sub> | 22.1<br><sub>29,26,16,21,19</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>1,4,6,4,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 5.7<br><sub>4,7,1,5,4</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>4,4,1,1,2</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.5 | 3.1 | 32.1 |
| Walker Kessler | 98% | 30.2<br><sub>28,33,26,31,31</sub> | 11.4<br><sub>2,13,11,10,16</sub> | 11.5 · –<br><sub>o 50% · u 50%</sub> | 10.9<br><sub>7,8,9,13,15</sub> | 10.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>0,0,1,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 2.1 | 1.5 | 23.9 |
| Quentin Grimes | 98% | 26.6<br><sub>20,19,38,26,26</sub> | 10.1<br><sub>3,2,23,3,7</sub> |  | 3.3<br><sub>1,4,3,3,1</sub> |  | 2.5<br><sub>1,0,5,2,3</sub> |  | 1.2<br><sub>0,0,0,1,1</sub> |  | 0.8 | 0.3 | 1.3 | 15.9 |
| Matisse Thybulle | 97% | 24.2<br><sub>26,22,28,28,25</sub> | 8.0<br><sub>11,5,15,10,6</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 2.5<br><sub>1,2,1,3,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>1,1,0,0,3</sub> |  | 1.3<br><sub>3,1,4,1,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.8 | 0.7 | 0.9 | 11.7 |
| Jake LaRavia | 96% | 23.7<br><sub>15,19,35,28,25</sub> | 6.4<br><sub>0,5,2,10,8</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 3.7<br><sub>4,1,10,2,2</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>1,1,0,0,4</sub> |  | 0.7<br><sub>0,1,0,2,2</sub> |  | 1.2 | 0.6 | 1.1 | 11.6 |
| Sandro Mamukelashvili | 98% | 23.4<br><sub>21,24,30,20,24</sub> | 9.6<br><sub>9,17,13,4,11</sub> |  | 5.4<br><sub>3,4,8,7,1</sub> |  | 1.6<br><sub>0,2,3,0,1</sub> |  | 1.2<br><sub>1,3,0,0,2</sub> |  | 0.8 | 0.5 | 0.8 | 16.5 |
| Collin Sexton | 98% | 18.5<br><sub>20,14,21,16,19</sub> | 11.4<br><sub>13,9,21,0,14</sub> |  | 2.1<br><sub>2,1,4,2,3</sub> |  | 2.1<br><sub>1,4,2,1,3</sub> |  | 1.2<br><sub>1,0,4,0,1</sub> |  | 0.9 | 0.1 | 1.5 | 15.7 |
| Lawson Lovering | 16% | 14.2 | 4.6 |  | 3.7 |  | 1.0 |  | 0.1 |  | 0.7 | 0.3 | 0.6 | 9.3 |
| Jarred Vanderbilt | 63% | 13.7<br><sub>-,-,21,13,12</sub> | 3.4<br><sub>-,-,0,0,4</sub> |  | 3.5<br><sub>-,-,7,3,3</sub> |  | 1.1<br><sub>-,-,2,3,1</sub> |  | 0.2<br><sub>-,-,0,0,0</sub> |  | 0.6 | 0.2 | 0.6 | 8.1 |
| AK Okereke | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Kevon Looney | 52% | 7.9<br><sub>5,5,-,-,-</sub> | 1.8<br><sub>2,0,-,-,-</sub> |  | 2.9<br><sub>2,0,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.3 |
| Jaden Hardy | 67% | 7.6<br><sub>-,-,9,1,1</sub> | 4.0<br><sub>-,-,2,0,1</sub> |  | 0.7<br><sub>-,-,0,1,0</sub> |  | 0.6<br><sub>-,-,2,0,0</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.3 |
| Cameron Carr | 80% | 6.9<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| Bronny James | 52% | 5.8<br><sub>-,-,-,1,2</sub> | 2.3<br><sub>-,-,-,0,0</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.2 | 0.1 | 0.5 | 3.0 |
| Chris Manon | 58% | 5.8<br><sub>-,-,-,1,-</sub> | 1.9<br><sub>-,-,-,0,-</sub> |  | 1.1<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.4 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-02/`._
