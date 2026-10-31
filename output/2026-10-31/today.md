# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sun 01 Nov, 09:47 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PA over 19.5 (20+) | SAC @ MEM | draftkings | 3.91 | 3.72 | 2.78 | 35.9% | 23.9% | 26.9% | +5.2% | +40.6% | 0.4% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 7.5 (8+) | OKC @ HOU | draftkings | 21.00 | 13.32 | 5.99 | 16.7% | 4.5% | 7.5% | +57.8% | +250.7% | 0.7% |
| Tari Eason REB over 11.5 (12+) | OKC @ HOU | draftkings | 22.00 | 16.84 | 9.06 | 11.0% | 4.2% | 5.9% | +30.8% | +142.8% | 0.4% |
| Tari Eason REB over 9.5 (10+) | OKC @ HOU | draftkings | 9.50 | 7.43 | 4.12 | 24.3% | 9.8% | 13.5% | +27.8% | +130.7% | 0.8% |
| Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings | 30.00 | 24.45 | 14.23 | 7.0% | 3.1% | 4.1% | +22.8% | +110.9% | 0.2% |
| Kevin Durant REB over 9.5 (10+) | OKC @ HOU | draftkings | 14.00 | 11.71 | 7.08 | 14.1% | 6.7% | 8.5% | +19.5% | +97.7% | 0.4% |
| Amen Thompson AST over 7.5 (8+) | OKC @ HOU | draftkings | 8.20 | 6.93 | 4.26 | 23.5% | 11.4% | 14.4% | +18.2% | +92.5% | 0.6% |
| Amen Thompson AST over 9.5 (10+) | OKC @ HOU | draftkings | 22.00 | 18.69 | 11.53 | 8.7% | 4.2% | 5.3% | +17.8% | +90.8% | 0.2% |
| Shai Gilgeous-Alexander PTS over 44.5 (45+) | OKC @ HOU | draftkings | 15.60 | 13.32 | 8.28 | 12.1% | 6.0% | 7.5% | +17.2% | +88.3% | 0.3% |
| Shai Gilgeous-Alexander PRA over 59.5 (60+) | OKC @ HOU | draftkings | 20.20 | 17.33 | 10.88 | 9.2% | 4.6% | 5.8% | +16.5% | +85.6% | 0.2% |
| MIN to win | MIN @ SAS | ladbrokes_au | 6.25 | 5.49 | 4.05 | 24.7% | 18.2% | 18.2% | +13.9% | +54.2% | 0.7% |
| Jabari Smith Jr. PRA over 34.5 (35+) | OKC @ HOU | draftkings | 9.70 | 8.52 | 5.54 | 18.1% | 9.6% | 11.7% | +13.9% | +75.1% | 0.4% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ HOU | draftkings | 9.70 | 8.63 | 5.73 | 17.4% | 9.6% | 11.6% | +12.4% | +69.3% | 0.4% |
| Jabari Smith Jr. PRA over 39.5 (40+) | OKC @ HOU | draftkings | 20.40 | 18.38 | 12.48 | 8.0% | 4.6% | 5.4% | +11.0% | +63.5% | 0.1% |
| Precious Achiuwa PA over 24.5 (25+) | SAC @ MEM | draftkings | 9.90 | 8.95 | 6.12 | 16.3% | 9.4% | 11.2% | +10.5% | +61.8% | 0.3% |
| Donovan Mitchell PTS over 44.5 (45+) | CLE @ MIL | draftkings | 26.00 | 23.53 | 16.12 | 6.2% | 3.6% | 4.2% | +10.4% | +61.3% | 0.1% |
| Jabari Smith Jr. REB over 11.5 (12+) | OKC @ HOU | draftkings | 16.80 | 15.29 | 10.55 | 9.5% | 5.6% | 6.5% | +9.9% | +59.2% | 0.2% |
| Jabari Smith Jr. REB over 9.5 (10+) | OKC @ HOU | draftkings | 7.00 | 6.37 | 4.40 | 22.7% | 13.4% | 15.7% | +9.8% | +58.9% | 0.4% |
| Shai Gilgeous-Alexander AST over 11.5 (12+) | OKC @ HOU | draftkings | 24.00 | 21.88 | 15.13 | 6.6% | 3.9% | 4.6% | +9.8% | +58.6% | 0.1% |
| Shai Gilgeous-Alexander PRA over 54.5 (55+) | OKC @ HOU | draftkings | 10.90 | 9.93 | 6.87 | 14.5% | 8.6% | 10.1% | +9.8% | +58.6% | 0.2% |
| Donovan Mitchell PTS over 39.5 (40+) | CLE @ MIL | draftkings | 13.00 | 11.95 | 8.40 | 11.9% | 7.2% | 8.4% | +8.8% | +54.8% | 0.2% |
| Jabari Smith Jr. PA over 29.5 (30+) | OKC @ HOU | draftkings | 15.20 | 14.01 | 9.90 | 10.1% | 6.2% | 7.1% | +8.5% | +53.6% | 0.1% |
| Darius Acuff Jr. REB over 5.5 (6+) | SAC @ MEM | draftkings | 5.16 | 4.77 | 3.38 | 29.6% | 18.1% | 21.0% | +8.2% | +52.6% | 0.5% |
| Jabari Smith Jr. PRA over 29.5 (30+) | OKC @ HOU | draftkings | 4.36 | 4.03 | 2.86 | 34.9% | 21.4% | 24.8% | +8.2% | +52.3% | 0.6% |
| Zion Williamson PRA over 44.5 (45+) | ATL @ NOP | draftkings | 11.80 | 10.91 | 7.75 | 12.9% | 7.9% | 9.2% | +8.2% | +52.2% | 0.2% |
| Zion Williamson PA over 39.5 (40+) | ATL @ NOP | draftkings | 16.20 | 15.02 | 10.71 | 9.3% | 5.8% | 6.7% | +7.9% | +51.3% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 10.5 (11+) | OKC @ HOU | draftkings | 15.00 | 11.29 | 5.96 | 16.8% | 6.2% | 8.9% | +33.0% | +151.5% | 0.6% |
| Amen Thompson AST over 8.5 (9+) | OKC @ HOU | draftkings | 13.60 | 11.42 | 6.93 | 14.4% | 6.9% | 8.8% | +19.1% | +96.2% | 0.4% |
| Kevin Durant REB over 8.5 (9+) | OKC @ HOU | draftkings | 8.80 | 7.39 | 4.49 | 22.3% | 10.6% | 13.5% | +19.1% | +96.1% | 0.6% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 21.00 | 18.38 | 11.91 | 8.4% | 4.5% | 5.4% | +14.2% | +76.3% | 0.2% |
| Shai Gilgeous-Alexander AST over 10.5 (11+) | OKC @ HOU | draftkings | 16.00 | 14.08 | 9.19 | 10.9% | 5.8% | 7.1% | +13.6% | +74.2% | 0.2% |
| Jabari Smith Jr. REB over 10.5 (11+) | OKC @ HOU | draftkings | 10.90 | 9.82 | 6.66 | 15.0% | 8.6% | 10.2% | +11.0% | +63.6% | 0.3% |
| Darius Acuff Jr. REB over 6.5 (7+) | SAC @ MEM | draftkings | 8.90 | 8.14 | 5.66 | 17.7% | 10.5% | 12.3% | +9.4% | +57.3% | 0.3% |
| Shai Gilgeous-Alexander AST over 8.5 (9+) | OKC @ HOU | draftkings | 5.99 | 5.50 | 3.87 | 25.9% | 15.6% | 18.2% | +8.8% | +54.9% | 0.4% |
| Cameron Boozer REB over 14.5 (15+) | SAC @ MEM | draftkings | 13.00 | 11.98 | 8.45 | 11.8% | 7.2% | 8.3% | +8.5% | +53.8% | 0.2% |
| Trey Murphy III AST over 6.5 (7+) | ATL @ NOP | draftkings | 13.40 | 12.42 | 8.86 | 11.3% | 7.0% | 8.1% | +7.9% | +51.3% | 0.2% |
| Jabari Smith Jr. REB over 8.5 (9+) | OKC @ HOU | draftkings | 4.54 | 4.24 | 3.07 | 32.6% | 20.6% | 23.6% | +7.1% | +48.0% | 0.5% |
| Alperen Sengun REB over 14.5 (15+) | OKC @ HOU | draftkings | 12.40 | 11.59 | 8.39 | 11.9% | 7.5% | 8.6% | +7.0% | +47.8% | 0.1% |
| Amen Thompson AST over 10.5 (11+) | OKC @ HOU | draftkings | 30.00 | 28.25 | 20.76 | 4.8% | 3.1% | 3.5% | +6.2% | +44.5% | 0.1% |
| Alperen Sengun REB over 12.5 (13+) | OKC @ HOU | draftkings | 6.14 | 5.80 | 4.29 | 23.3% | 15.2% | 17.2% | +5.9% | +43.2% | 0.3% |
| Zion Williamson REB over 8.5 (9+) | ATL @ NOP | draftkings | 6.33 | 6.00 | 4.46 | 22.4% | 14.8% | 16.7% | +5.6% | +41.9% | 0.3% |
| De'Andre Hunter REB over 8.5 (9+) | SAC @ MEM | draftkings | 10.40 | 9.85 | 7.33 | 13.6% | 9.0% | 10.2% | +5.5% | +41.8% | 0.1% |
| Aday Mara REB over 8.5 (9+) | OKC @ HOU | draftkings | 6.77 | 6.41 | 4.78 | 20.9% | 13.8% | 15.6% | +5.5% | +41.7% | 0.2% |
| Zion Williamson REB over 10.5 (11+) | ATL @ NOP | draftkings | 16.40 | 15.58 | 11.65 | 8.6% | 5.7% | 6.4% | +5.3% | +40.8% | 0.1% |
| Jabari Smith Jr. REB over 12.5 (13+) | OKC @ HOU | draftkings | 24.00 | 22.83 | 17.17 | 5.8% | 3.9% | 4.4% | +5.0% | +39.7% | 0.1% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.12 | 1.95 | 1.37 | 72.9% | 44.1% | 51.3% | +8.7% | +54.4% | 1.9% |
| AJ Green 3PM under 1.5 | CLE @ MIL | draftkings | 2.33 | 2.14 | 1.51 | 66.2% | 40.1% | 46.6% | +8.7% | +54.3% | 1.6% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 1.97 | 1.82 | 1.29 | 77.6% | 47.5% | 55.0% | +8.4% | +52.9% | 2.0% |
| Amen Thompson AST over 5.5 (6+) | OKC @ HOU | draftkings | 2.97 | 2.78 | 2.02 | 49.6% | 31.5% | 36.0% | +6.9% | +47.3% | 0.9% |
| Kevin Durant REB over 5.5 (6+) | OKC @ HOU | draftkings | 2.32 | 2.21 | 1.66 | 60.3% | 40.3% | 45.3% | +5.1% | +39.9% | 1.0% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| ATL @ NOP | Sun 01 Nov 10:00 | 123.4–119.0 | ATL 63% | 1.60 / 2.68 | NOP +4.5 | 242.5 | NOP +4.5 covers 49%; o239.5 56% |
| SAC @ MEM | Sun 01 Nov 11:00 | 115.8–122.4 | SAC 32% | 3.12 / 1.47 | MEM -6.5 | 238.5 | MEM -9.5 covers 42%; o229.5 68% |
| CLE @ MIL | Sun 01 Nov 11:00 | 118.8–114.7 | CLE 61% | 1.63 / 2.60 | MIL +4.5 | 233.5 | MIL +9.5 covers 65%; o235.5 45% |
| MIN @ SAS | Sun 01 Nov 11:00 | 108.4–117.7 | MIN 26% | 3.89 / 1.35 | SAS -9.5 | 225.5 | SAS -12.5 covers 41%; o228.5 45% |
| OKC @ HOU | Sun 01 Nov 11:30 | 112.1–113.1 | OKC 47% | 2.12 / 1.90 | HOU -1.5 | 225.5 | HOU -2.5 covers 47%; o219.5 61% |

### ATL @ NOP
Out: Yves Missi (NOP), Dejounte Murray (NOP), Jordan Poole (NOP), RayJ Dennis (ATL), Keshon Gilbert (ATL), Mouhamed Gueye (ATL), Jalen Wilson (ATL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Aaron Wiggins PTS under 12.5 | ATL @ NOP | tab | 1.90 | 1.85 | 1.59 | 62.9% | 51.0% | 54.0% | +2.6% | +19.5% | 0.7% |
| Saddiq Bey PTS over 12.5 (13+) | ATL @ NOP | pointsbetau | 1.90 | 1.85 | 1.60 | 62.6% | 51.0% | 53.9% | +2.5% | +19.0% | 0.7% |
| CJ McCollum PTS over 16.5 (17+) | ATL @ NOP | pointsbetau | 2.05 | 2.03 | 1.87 | 53.4% | 48.0% | 49.3% | +1.1% | +9.5% | 0.3% |
| Jalen Johnson PTS under 22.5 | ATL @ NOP | tab | 1.90 | 1.88 | 1.64 | 60.9% | 50.6% | 53.2% | +1.1% | +15.7% | 0.3% |
| Trey Murphy III RA over 8.5 (9+) | ATL @ NOP | draftkings | 2.08 | 2.06 | 1.69 | 59.2% | 45.0% | 48.5% | +0.9% | +23.2% | 0.2% |
| Karlo Matkovic PR over 13.5 (14+) | ATL @ NOP | draftkings | 1.88 | 1.87 | 1.55 | 64.4% | 49.9% | 53.5% | +0.4% | +20.9% | 0.1% |
| Saddiq Bey PR over 17.5 (18+) | ATL @ NOP | draftkings | 1.96 | 1.95 | 1.65 | 60.5% | 48.1% | 51.2% | +0.4% | +18.6% | 0.1% |
| Zion Williamson RA over 8.5 (9+) | ATL @ NOP | draftkings | 1.85 | 1.84 | 1.53 | 65.4% | 50.6% | 54.3% | +0.3% | +20.9% | 0.1% |
| Trey Murphy III PTS under 17.5 | ATL @ NOP | tab | 1.95 | 1.95 | 1.93 | 51.9% | 51.0% | 51.2% | +0.0% | +1.3% | 0.0% |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 100% | 34.9<br><sub>29,38,36,36,34</sub> | 21.2<br><sub>19,26,21,12,17</sub> | 22.5 · 21.5<br><sub>o 46% · u 54%</sub> | 9.6<br><sub>7,9,9,9,8</sub> | 9.5<br><sub>o 48% · u 52%</sub> | 7.4<br><sub>8,16,3,11,7</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.3 | 0.6 | 3.1 | 38.2 |
| Nickeil Alexander-Walker | 100% | 32.5<br><sub>27,32,29,32,31</sub> | 19.5<br><sub>14,18,12,23,25</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,5,2,3,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 3.4<br><sub>5,4,3,1,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 3.3<br><sub>2,4,2,5,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.5 | 2.2 | 26.1 |
| Dyson Daniels | 100% | 31.1<br><sub>23,29,28,28,32</sub> | 12.0<br><sub>11,18,4,7,4</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>9,8,0,4,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 5.4<br><sub>4,3,4,7,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 2.1 | 0.4 | 1.6 | 23.6 |
| Onyeka Okongwu | 100% | 30.9<br><sub>22,26,29,31,33</sub> | 14.4<br><sub>10,8,11,11,29</sub> | 13.5 · 12.5<br><sub>o 49% · u 51%</sub> | 7.3<br><sub>4,6,9,4,12</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.8<br><sub>1,2,1,4,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,1,1,4</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.1 | 1.0 | 1.4 | 24.6 |
| CJ McCollum | 100% | 29.3<br><sub>22,30,30,20,31</sub> | 18.2<br><sub>13,17,20,13,5</sub> | 15.5 · 15.5<br><sub>o 53% · u 47%</sub> | 2.9<br><sub>1,2,1,2,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>2,1,3,1,8</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.5<br><sub>2,1,4,1,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.5 | 1.9 | 24.6 |
| Aaron Wiggins | 96% | 24.3<br><sub>22,29,27,24,24</sub> | 11.5<br><sub>19,16,12,10,20</sub> | 12.5 · 12.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>1,5,4,4,7</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.9<br><sub>1,2,3,3,3</sub> |  | 1.8<br><sub>3,4,2,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.4 | 1.0 | 16.6 |
| Luguentz Dort | 98% | 21.6<br><sub>19,23,21,24,22</sub> | 7.4<br><sub>9,7,11,8,6</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 2.7<br><sub>5,2,2,3,3</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.5<br><sub>2,3,1,3,2</sub> |  | 1.2<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.2 | 0.7 | 11.6 |
| Kingston Flemings | 96% | 18.3<br><sub>25,15,18,28,16</sub> | 6.5<br><sub>5,2,6,23,2</sub> | 7.5 · 6.5<br><sub>o 45% · u 55%</sub> | 2.6<br><sub>6,1,1,5,1</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>8,2,4,5,5</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 0.6<br><sub>1,0,0,3,0</sub> |  | 0.7 | 0.3 | 1.3 | 12.9 |
| Jock Landale | 98% | 16.7<br><sub>18,19,18,17,15</sub> | 7.6<br><sub>8,2,8,10,6</sub> |  | 4.5<br><sub>6,4,6,6,10</sub> |  | 1.5<br><sub>4,2,4,0,1</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.4 | 0.5 | 0.8 | 13.6 |
| Corey Kispert | 48% | 9.2<br><sub>10,-,1,-,-</sub> | 4.6<br><sub>11,-,5,-,-</sub> |  | 1.3<br><sub>1,-,0,-,-</sub> |  | 0.8<br><sub>1,-,0,-,-</sub> |  | 0.5<br><sub>3,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 6.7 |
| Asa Newell | 47% | 7.8<br><sub>8,-,1,-,-</sub> | 3.4<br><sub>3,-,0,-,-</sub> |  | 1.6<br><sub>1,-,1,-,-</sub> |  | 0.5<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.5 |
| Dorian Finney-Smith | 48% | 7.2<br><sub>8,-,1,-,-</sub> | 2.3<br><sub>3,-,0,-,-</sub> |  | 1.2<br><sub>2,-,0,-,-</sub> |  | 0.5<br><sub>1,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 100% | 35.1<br><sub>32,31,37,30,32</sub> | 18.1<br><sub>11,9,26,6,19</sub> | 17.5 · 16.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>4,6,6,1,5</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 3.9<br><sub>1,3,4,3,3</sub> | 2.5<br><sub>o 63% · u 37%</sub> | 2.8<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.4 | 0.5 | 1.8 | 27.7 |
| Zion Williamson | 100% | 33.2<br><sub>32,33,33,32,31</sub> | 22.5<br><sub>22,23,17,25,22</sub> | 20.5 · 21.5<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>3,5,1,5,6</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>3,2,2,2,2</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.2<br><sub>2,0,0,1,0</sub> |  | 1.4 | 0.8 | 2.5 | 32.7 |
| Jeremiah Fears | 100% | 29.8<br><sub>21,24,23,24,29</sub> | 17.5<br><sub>8,7,10,11,22</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>3,0,6,4,8</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 5.0<br><sub>1,1,2,3,13</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.3 | 0.6 | 2.8 | 26.9 |
| Herbert Jones | 100% | 28.5<br><sub>17,18,16,19,32</sub> | 9.3<br><sub>5,3,2,4,16</sub> | 7.5 · –<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>2,1,3,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.4<br><sub>0,0,1,0,1</sub> |  | 1.2<br><sub>1,1,0,0,0</sub> |  | 1.5 | 0.5 | 1.5 | 15.1 |
| Saddiq Bey | 96% | 28.4<br><sub>24,22,25,26,24</sub> | 15.5<br><sub>13,20,14,9,10</sub> | 13.5 · 12.5<br><sub>o 54% · u 46%</sub> | 4.8<br><sub>5,3,4,0,4</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 2.4<br><sub>0,1,3,3,3</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.9<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.2 | 22.7 |
| Karlo Matkovic | 100% | 26.2<br><sub>-,9,8,18,28</sub> | 9.9<br><sub>-,7,3,5,12</sub> | 7.5 · 8.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>-,4,0,3,4</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.5<br><sub>-,1,0,1,1</sub> |  | 1.0<br><sub>-,0,1,1,1</sub> |  | 0.8 | 1.5 | 1.3 | 17.8 |
| Derik Queen | 98% | 26.0<br><sub>18,29,25,25,22</sub> | 12.1<br><sub>10,12,17,11,9</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 7.9<br><sub>10,7,8,12,2</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>1,2,2,1,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 0.4<br><sub>0,1,0,0,1</sub> |  | 1.1 | 1.0 | 2.3 | 23.2 |
| Bennedict Mathurin | 98% | 20.2<br><sub>18,15,20,14,19</sub> | 10.2<br><sub>11,4,9,5,10</sub> |  | 3.8<br><sub>3,2,4,1,3</sub> |  | 1.9<br><sub>2,0,4,2,2</sub> |  | 0.8<br><sub>0,0,1,1,2</sub> |  | 0.6 | 0.2 | 1.5 | 15.9 |
| Trendon Watford | 48% | 16.1<br><sub>-,-,-,-,17</sub> | 6.4<br><sub>-,-,-,-,8</sub> |  | 3.1<br><sub>-,-,-,-,1</sub> |  | 1.9<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.4 | 1.1 | 11.4 |
| DeAndre Jordan | 52% | 15.4<br><sub>-,-,20,13,-</sub> | 4.2<br><sub>-,-,9,3,-</sub> |  | 6.1<br><sub>-,-,9,4,-</sub> |  | 1.0<br><sub>-,-,2,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.8 | 0.8 | 11.3 |
| AJ Johnson | 5% | 12.2<br><sub>-,-,-,-,-</sub> | 5.1<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.5 |
| Bryce McGowens | 58% | 11.1<br><sub>-,-,-,3,6</sub> | 3.9<br><sub>-,-,-,0,4</sub> |  | 1.4<br><sub>-,-,-,0,1</sub> |  | 0.8<br><sub>-,-,-,0,2</sub> |  | 0.3<br><sub>-,-,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.1 |
| Julian Reese | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>


### SAC @ MEM
Out: Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PA over 14.5 (15+) | SAC @ MEM | draftkings | 1.90 | 1.88 | 1.57 | 63.9% | 49.5% | 53.1% | +0.9% | +21.4% | 0.2% |
| Darius Acuff Jr. RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.95 | 1.94 | 1.61 | 62.3% | 47.9% | 51.5% | +0.5% | +21.6% | 0.1% |
| Precious Achiuwa RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.95 | 1.95 | 1.64 | 61.1% | 48.0% | 51.2% | +0.1% | +19.3% | 0.0% |
| Precious Achiuwa REB over 7.5 (8+) | SAC @ MEM | draftkings | 1.89 | 1.89 | 1.59 | 63.0% | 49.5% | 52.8% | +0.0% | +19.2% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.8–122.4 | SAC 32% | 3.12 / 1.47 | MEM -6.5 | 238.5 | MEM -9.5 covers 42%; o229.5 68% |
| Expected (weighted by chance each plays) | 115.0–122.9 | SAC 29% | 3.42 / 1.41 | MEM -7.5 | 237.5 | MEM -9.5 covers 45%; o229.5 68% |
| if Ty Jerome plays | 115.3–123.3 | SAC 29% | 3.50 / 1.40 | MEM -8.5 | 238.5 | MEM -9.5 covers 46%; o229.5 69% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quinten Post (MEM) | Doubtful | 20% | 14.1 | 5.7 | 3.0 | 0.8 | 0.5 | 0.5 | 0.4 | 0.7 | 9.4 | small |
| Ty Jerome (MEM) | Questionable | 55% | 29.0 | 22.6 | 3.5 | 6.4 | 2.6 | 1.4 | 0.3 | 2.5 | 32.5 | full tables below |
| Scotty Pippen Jr. (MEM) | Questionable | 55% | 18.6 | 9.8 | 2.6 | 3.5 | 0.8 | 1.2 | 0.4 | 1.8 | 15.9 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.0<br><sub>12,33,22,19,34</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.4<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.5 | 33.9 |
| Zach LaVine | 98% | 34.1<br><sub>34,39,40,31,39</sub> | 21.3<br><sub>28,22,37,22,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.6 | 28.1 |
| Domantas Sabonis | 98% | 34.0<br><sub>34,39,35,37,40</sub> | 18.4<br><sub>14,27,15,20,9</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 14.0<br><sub>18,19,15,14,15</sub> | 14.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 0.3<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 19% · u 81%</sub> | 0.9 | 0.4 | 3.1 | 38.4 |
| Precious Achiuwa | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.8<br><sub>15,14,12,4,24</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 1.5 | 1.1 | 1.7 | 26.7 |
| De'Andre Hunter | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.2<br><sub>6,4,7,24,24</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>3,7,6,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,2,5,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.8 | 20.5 |
| Emanuel Sharp | 96% | 15.6<br><sub>17,14,14,20,18</sub> | 4.9<br><sub>8,5,3,5,0</sub> | 5.5 · –<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.6<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.6 |
| Daeqwon Plowden | 71% | 15.4<br><sub>13,20,16,17,-</sub> | 5.0<br><sub>4,3,3,0,-</sub> |  | 1.9<br><sub>2,0,3,2,-</sub> |  | 0.8<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,1,1,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.7 |
| Malik Monk | 96% | 14.3<br><sub>-,12,12,13,8</sub> | 7.4<br><sub>-,0,6,3,2</sub> |  | 1.6<br><sub>-,1,1,2,1</sub> |  | 2.5<br><sub>-,2,2,6,1</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 1.1 | 11.4 |
| Jonathan Mogbo | 52% | 12.3<br><sub>8,-,18,18,-</sub> | 4.5<br><sub>0,-,7,2,-</sub> |  | 2.4<br><sub>0,-,3,5,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.7 | 7.6 |
| Alex Karaban | 64% | 11.4<br><sub>5,-,-,11,12</sub> | 3.6<br><sub>1,-,-,0,6</sub> |  | 2.2<br><sub>1,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.2<br><sub>0,-,-,0,2</sub> |  | 0.4 | 0.3 | 0.8 | 6.5 |
| Nique Clifford | 83% | 10.2<br><sub>17,2,-,5,4</sub> | 4.0<br><sub>6,0,-,2,0</sub> |  | 1.6<br><sub>1,0,-,0,0</sub> |  | 1.1<br><sub>3,0,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.7 |
| Leaky Black | 48% | 9.5<br><sub>-,-,-,8,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 96% | 33.5<br><sub>33,37,31,31,28</sub> | 18.7<br><sub>7,25,14,13,18</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 10.7<br><sub>11,13,11,7,12</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>5,6,4,4,12</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>0,4,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.7 | 2.4 | 36.0 |
| Cedric Coward | 98% | 30.4<br><sub>28,-,32,31,27</sub> | 17.9<br><sub>7,-,17,16,17</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>7,-,11,11,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.8<br><sub>2,-,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.0<br><sub>1,-,3,4,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.5 | 2.0 | 29.2 |
| Jaylen Wells | 98% | 30.3<br><sub>28,25,33,30,25</sub> | 16.8<br><sub>12,17,16,14,10</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.7<br><sub>5,4,5,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>0,3,3,0,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>1,4,2,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 1.3 | 22.6 |
| Jerami Grant | 98% | 27.3<br><sub>24,26,22,24,27</sub> | 15.3<br><sub>15,6,5,13,2</sub> |  | 3.0<br><sub>2,0,5,3,1</sub> |  | 2.4<br><sub>3,3,3,0,3</sub> |  | 1.8<br><sub>2,1,1,3,0</sub> |  | 0.8 | 0.8 | 1.7 | 20.7 |
| Zach Edey | 98% | 24.3<br><sub>21,22,-,21,19</sub> | 10.7<br><sub>6,8,-,4,13</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 9.6<br><sub>9,10,-,3,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.7 | 1.7 | 1.7 | 21.9 |
| Cam Spencer | 96% | 22.9<br><sub>16,17,16,18,23</sub> | 11.0<br><sub>3,11,13,8,8</sub> |  | 3.0<br><sub>3,2,2,5,6</sub> |  | 5.9<br><sub>2,1,1,5,8</sub> |  | 1.6<br><sub>1,3,3,2,1</sub> |  | 0.8 | 0.2 | 1.2 | 19.9 |
| GG Jackson | 96% | 19.6<br><sub>19,15,10,16,21</sub> | 11.9<br><sub>12,2,1,4,12</sub> |  | 4.2<br><sub>8,4,3,1,7</sub> |  | 1.5<br><sub>0,1,0,2,2</sub> |  | 1.1<br><sub>2,0,0,0,2</sub> |  | 0.5 | 0.7 | 1.6 | 17.6 |
| Jahmai Mashack | 38% | 18.8<br><sub>-,-,-,-,-</sub> | 6.1<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0 | 0.4 | 1.5 | 11.0 |
| Javon Small | 26% | 18.8 | 9.7 |  | 3.0 |  | 3.3 |  | 1.1 |  | 0.9 | 0.2 | 1.5 | 16.1 |
| Isaiah Stewart | 98% | 17.7<br><sub>-,16,22,15,16</sub> | 7.8<br><sub>-,4,13,4,18</sub> |  | 4.2<br><sub>-,2,5,4,3</sub> |  | 0.9<br><sub>-,0,2,0,0</sub> |  | 0.6<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.1 | 0.9 | 12.9 |
| Taylor Hendricks | 58% | 11.4<br><sub>-,-,7,-,3</sub> | 4.6<br><sub>-,-,0,-,0</sub> |  | 2.3<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.4 | 0.6 | 7.6 |
| Olivier-Maxence Prosper | 48% | 11.4<br><sub>-,-,-,-,3</sub> | 6.6<br><sub>-,-,-,-,4</sub> |  | 2.4<br><sub>-,-,-,-,1</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 9.7 |
| Kris Murray | 58% | 10.2<br><sub>-,13,-,-,3</sub> | 2.6<br><sub>-,0,-,-,0</sub> |  | 1.6<br><sub>-,3,-,-,1</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.0 |
| Carson Cooper | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Karim Lopez | 48% | 6.9<br><sub>-,-,-,-,3</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 2.2 |

</details>

<details><summary>if Ty Jerome plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 96% | 32.2<br><sub>33,37,31,31,28</sub> | 16.1<br><sub>7,25,14,13,18</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 10.1<br><sub>11,13,11,7,12</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>5,6,4,4,12</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 1.8<br><sub>0,4,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.4 | 0.7 | 2.0 | 32.3 |
| Ty Jerome (MEM) | 100% | 29.0<br><sub>32,32,32,30,24</sub> | 22.6<br><sub>45,28,31,15,10</sub> | 22.5 · – | 3.5<br><sub>7,2,4,1,2</sub> | 2.5 | 6.4<br><sub>6,5,7,8,3</sub> | 5.5 | 2.6<br><sub>5,3,1,1,1</sub> | 2.5 | 1.4 | 0.3 | 2.5 | 32.5 |
| Jaylen Wells (MEM) | 98% | 28.1<br><sub>28,25,33,30,25</sub> | 14.2<br><sub>12,17,16,14,10</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.3<br><sub>5,4,5,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>0,3,3,0,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.9<br><sub>1,4,2,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.1 | 1.0 | 19.3 |
| Cedric Coward (MEM) | 98% | 27.9<br><sub>28,-,32,31,27</sub> | 15.5<br><sub>7,-,17,16,17</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 6.8<br><sub>7,-,11,11,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>2,-,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>1,-,3,4,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 1.6 | 25.3 |
| Jerami Grant (MEM) | 98% | 24.9<br><sub>24,26,22,24,27</sub> | 12.0<br><sub>15,6,5,13,2</sub> |  | 2.7<br><sub>2,0,5,3,1</sub> |  | 1.9<br><sub>3,3,3,0,3</sub> |  | 1.4<br><sub>2,1,1,3,0</sub> |  | 0.7 | 0.8 | 1.4 | 16.6 |
| Zach Edey (MEM) | 98% | 22.3<br><sub>21,22,-,21,19</sub> | 9.6<br><sub>6,8,-,4,13</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 8.6<br><sub>9,10,-,3,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.4<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.6 | 1.6 | 1.4 | 19.5 |
| Cam Spencer (MEM) | 96% | 20.4<br><sub>16,17,16,18,23</sub> | 9.1<br><sub>3,11,13,8,8</sub> |  | 2.6<br><sub>3,2,2,5,6</sub> |  | 4.9<br><sub>2,1,1,5,8</sub> |  | 1.3<br><sub>1,3,3,2,1</sub> |  | 0.7 | 0.2 | 1.0 | 16.6 |
| GG Jackson (MEM) | 96% | 16.9<br><sub>19,15,10,16,21</sub> | 9.4<br><sub>12,2,1,4,12</sub> |  | 3.5<br><sub>8,4,3,1,7</sub> |  | 1.2<br><sub>0,1,0,2,2</sub> |  | 0.8<br><sub>2,0,0,0,2</sub> |  | 0.4 | 0.6 | 1.2 | 14.2 |
| Isaiah Stewart (MEM) | 98% | 15.2<br><sub>-,16,22,15,16</sub> | 6.4<br><sub>-,4,13,4,18</sub> |  | 3.6<br><sub>-,2,5,4,3</sub> |  | 0.7<br><sub>-,0,2,0,0</sub> |  | 0.4<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.0 | 0.8 | 10.7 |
| Javon Small (MEM) | 26% | 13.1 | 5.9 |  | 2.0 |  | 2.1 |  | 0.7 |  | 0.6 | 0.2 | 1.0 | 10.1 |
| Jahmai Mashack (MEM) | 38% | 12.0<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.3 | 0.9 | 6.8 |
| Olivier-Maxence Prosper (MEM) | 48% | 9.1<br><sub>-,-,-,-,3</sub> | 5.2<br><sub>-,-,-,-,4</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 7.7 |
| Carson Cooper (MEM) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Taylor Hendricks (MEM) | 58% | 8.5<br><sub>-,-,7,-,3</sub> | 3.3<br><sub>-,-,0,-,0</sub> |  | 1.8<br><sub>-,-,1,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 5.5 |
| Kris Murray (MEM) | 58% | 8.1<br><sub>-,13,-,-,3</sub> | 2.0<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,3,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 3.9 |
| Karim Lopez (MEM) | 48% | 5.8<br><sub>-,-,-,-,3</sub> | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 2.0 |
| Darius Acuff Jr. (SAC) | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.1<br><sub>12,33,22,19,34</sub> | 23.5 · –<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.5 | 34.1 |
| Domantas Sabonis (SAC) | 98% | 34.1<br><sub>34,39,35,37,40</sub> | 18.4<br><sub>14,27,15,20,9</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 14.1<br><sub>18,19,15,14,15</sub> | 14.5<br><sub>o 46% · u 54%</sub> | 6.1<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 0.3<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 19% · u 81%</sub> | 0.9 | 0.4 | 3.1 | 38.5 |
| Zach LaVine (SAC) | 98% | 34.0<br><sub>34,39,40,31,39</sub> | 21.4<br><sub>28,22,37,22,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.5 | 28.2 |
| Precious Achiuwa (SAC) | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.8<br><sub>15,14,12,4,24</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 1.4 | 1.1 | 1.7 | 26.6 |
| De'Andre Hunter (SAC) | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.1<br><sub>6,4,7,24,24</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>3,7,6,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,2,5,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.8 | 20.4 |
| Emanuel Sharp (SAC) | 96% | 15.6<br><sub>17,14,14,20,18</sub> | 4.8<br><sub>8,5,3,5,0</sub> | 5.5 · –<br><sub>o 44% · u 56%</sub> | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.6<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.6 |
| Daeqwon Plowden (SAC) | 71% | 15.4<br><sub>13,20,16,17,-</sub> | 5.0<br><sub>4,3,3,0,-</sub> |  | 1.9<br><sub>2,0,3,2,-</sub> |  | 0.8<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,1,1,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.6 |
| Malik Monk (SAC) | 96% | 14.3<br><sub>-,12,12,13,8</sub> | 7.3<br><sub>-,0,6,3,2</sub> |  | 1.6<br><sub>-,1,1,2,1</sub> |  | 2.5<br><sub>-,2,2,6,1</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 1.1 | 11.4 |
| Jonathan Mogbo (SAC) | 52% | 12.3<br><sub>8,-,18,18,-</sub> | 4.5<br><sub>0,-,7,2,-</sub> |  | 2.4<br><sub>0,-,3,5,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.7 | 7.6 |
| Alex Karaban (SAC) | 64% | 11.5<br><sub>5,-,-,11,12</sub> | 3.6<br><sub>1,-,-,0,6</sub> |  | 2.3<br><sub>1,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.2<br><sub>0,-,-,0,2</sub> |  | 0.4 | 0.3 | 0.8 | 6.6 |
| Nique Clifford (SAC) | 83% | 10.3<br><sub>17,2,-,5,4</sub> | 4.0<br><sub>6,0,-,2,0</sub> |  | 1.6<br><sub>1,0,-,0,0</sub> |  | 1.1<br><sub>3,0,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.8 |
| Leaky Black (SAC) | 48% | 9.5<br><sub>-,-,-,8,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.3 | 0.4 | 5.0 |

</details>


### CLE @ MIL
Out: Jaylon Tyson (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Myles Turner RA under 6.5 | CLE @ MIL | draftkings | 2.05 | 2.03 | 1.66 | 60.4% | 45.7% | 49.4% | +1.2% | +23.8% | 0.3% |
| Tyler Herro PRA under 30.5 | CLE @ MIL | draftkings | 1.92 | 1.91 | 1.58 | 63.1% | 48.7% | 52.3% | +0.4% | +21.1% | 0.1% |
| Jaime Jaquez Jr. PTS under 15.5 | CLE @ MIL | draftkings | 1.97 | 1.97 | 1.64 | 61.1% | 47.4% | 50.8% | +0.2% | +20.3% | 0.1% |
| Tyler Herro PTS under 21.5 | CLE @ MIL | draftkings | 1.81 | 1.81 | 1.51 | 66.0% | 51.5% | 55.2% | +0.0% | +19.7% | 0.0% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.5<br><sub>33,33,39,34,36</sub> | 19.5<br><sub>16,12,19,16,24</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>3,8,5,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>5,7,9,6,4</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.4 | 3.3 | 31.2 |
| Donovan Mitchell | 98% | 35.1<br><sub>35,35,38,31,33</sub> | 26.9<br><sub>32,22,26,19,22</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>10,5,5,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.9<br><sub>3,4,7,7,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>2,2,5,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.3 | 2.6 | 36.8 |
| Evan Mobley | 98% | 34.0<br><sub>34,35,38,32,33</sub> | 17.7<br><sub>18,20,18,24,11</sub> | 17.5 · –<br><sub>o 48% · u 52%</sub> | 8.8<br><sub>8,10,10,12,4</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>2,4,3,2,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>1,2,4,5,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.4 | 1.7 | 30.1 |
| Jarrett Allen | 98% | 29.1<br><sub>28,27,27,30,30</sub> | 13.5<br><sub>14,21,10,8,14</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 8.6<br><sub>7,8,9,12,8</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,0,2,2,1</sub> |  | 0.1<br><sub>0,1,0,0,1</sub> |  | 1.2 | 1.3 | 1.2 | 23.7 |
| Peyton Watson | 98% | 28.8<br><sub>30,31,37,28,22</sub> | 13.7<br><sub>8,11,15,22,4</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>1,3,8,6,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,4,1,2,3</sub> |  | 1.2<br><sub>0,2,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.1 | 1.7 | 20.6 |
| Sam Merrill | 98% | 24.8<br><sub>24,21,31,20,27</sub> | 10.1<br><sub>5,7,9,8,16</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>5,2,4,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,3,2,1,3</sub> |  | 1.9<br><sub>1,1,1,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.1 | 0.7 | 14.6 |
| Meleek Thomas | 58% | 17.9<br><sub>-,-,19,20,-</sub> | 7.7<br><sub>-,-,16,10,-</sub> |  | 2.4<br><sub>-,-,2,4,-</sub> |  | 1.2<br><sub>-,-,0,1,-</sub> |  | 0.8<br><sub>-,-,4,0,-</sub> |  | 0.7 | 0.1 | 0.9 | 11.3 |
| Mario Hezonja | 96% | 16.0<br><sub>19,20,15,17,17</sub> | 6.0<br><sub>10,9,3,5,10</sub> | 8.5 · –<br><sub>o 40% · u 60%</sub> | 3.0<br><sub>3,5,3,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,1,1,2,2</sub> |  | 0.7<br><sub>0,2,1,1,2</sub> | 1.5<br><sub>o 29% · u 71%</sub> | 0.5 | 0.3 | 0.6 | 10.4 |
| Tyrese Proctor | 71% | 15.8<br><sub>5,11,-,6,20</sub> | 6.6<br><sub>0,5,-,2,7</sub> |  | 2.2<br><sub>0,2,-,1,6</sub> |  | 2.3<br><sub>0,3,-,1,2</sub> |  | 0.8<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.1 | 0.9 | 11.0 |
| Craig Porter Jr. | 58% | 9.2<br><sub>8,5,-,-,4</sub> | 2.6<br><sub>0,3,-,-,0</sub> |  | 1.7<br><sub>3,1,-,-,1</sub> |  | 1.5<br><sub>0,1,-,-,0</sub> |  | 0.1<br><sub>0,1,-,-,0</sub> |  | 0.5 | 0.3 | 0.6 | 5.8 |
| Thomas Bryant | 25% | 8.8<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.3 | 7.0 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Riley Minix | 23% | 7.2<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.7 |
| Tristan Enaruna | 23% | 6.1<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.7 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.5<br><sub>32,32,31,32,27</sub> | 19.1<br><sub>24,34,13,23,23</sub> | 21.5 · –<br><sub>o 44% · u 56%</sub> | 4.5<br><sub>2,5,6,10,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>9,4,3,7,0</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,5,1,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 2.3 | 28.3 |
| Ryan Rollins | 98% | 27.9<br><sub>24,34,25,32,17</sub> | 14.6<br><sub>9,11,15,19,4</sub> | 14.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,7,4,2,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>3,6,4,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.3 | 2.3 | 23.6 |
| Jaime Jaquez Jr. | 98% | 26.4<br><sub>31,35,27,25,27</sub> | 14.5<br><sub>22,19,21,8,19</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>7,11,8,6,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>2,5,4,0,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,2,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.9 | 23.4 |
| Kyle Kuzma | 98% | 25.2<br><sub>27,30,35,29,18</sub> | 11.6<br><sub>5,14,14,17,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>6,9,12,7,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,4,3,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,2,0,4,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 1.6 | 19.2 |
| Myles Turner | 98% | 23.6<br><sub>32,30,20,28,22</sub> | 9.8<br><sub>11,12,0,6,4</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>5,3,5,9,2</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>3,1,1,4,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 1.5 | 1.2 | 15.8 |
| Kasparas Jakucionis | 88% | 19.3<br><sub>26,23,25,21,19</sub> | 6.6<br><sub>15,7,12,7,4</sub> | 7.5 · –<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>3,2,3,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,5,2,5,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.6<br><sub>1,1,0,1,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 12.4 |
| AJ Green | 98% | 18.6<br><sub>15,17,19,20,24</sub> | 7.0<br><sub>6,11,11,3,9</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,3,4,1</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 1.2<br><sub>2,3,3,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.4 | 0.1 | 0.5 | 10.1 |
| Cormac Ryan | 26% | 17.7 | 8.9 |  | 2.1 |  | 1.3 |  | 1.2 |  | 0.7 | 0.2 | 1.2 | 12.3 |
| Kel'el Ware | 88% | 17.4<br><sub>14,15,29,19,17</sub> | 8.8<br><sub>7,11,19,16,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.9<br><sub>3,4,13,14,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.6 | 0.4 | 1.1 | 15.3 |
| Brayden Burries | 96% | 13.6<br><sub>16,8,17,16,17</sub> | 6.0<br><sub>12,3,10,4,10</sub> |  | 2.7<br><sub>5,1,5,2,5</sub> |  | 1.4<br><sub>0,3,2,1,1</sub> |  | 0.6<br><sub>2,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.1 |
| Ousmane Dieng | 83% | 12.4<br><sub>21,16,-,3,13</sub> | 4.8<br><sub>5,3,-,0,4</sub> |  | 1.9<br><sub>4,1,-,0,0</sub> |  | 1.6<br><sub>3,1,-,0,0</sub> |  | 0.4<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 8.2 |
| Nate Ament | 67% | 11.7<br><sub>-,-,11,14,20</sub> | 5.0<br><sub>-,-,1,7,8</sub> |  | 2.4<br><sub>-,-,3,3,4</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,1,1</sub> |  | 0.5 | 0.2 | 0.7 | 7.9 |
| Caris LeVert | 30% | 10.9<br><sub>-,-,-,-,-</sub> | 4.2<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.6 | 6.9 |
| Gary Trent Jr. | 52% | 9.3<br><sub>-,-,-,-,7</sub> | 4.0<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.0 | 0.3 | 5.1 |
| Jericho Sims | 52% | 9.2<br><sub>2,-,-,-,7</sub> | 3.1<br><sub>0,-,-,-,0</sub> |  | 2.8<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.8 |
| Pete Nance | 30% | 9.0 | 3.0 |  | 1.4 |  | 0.6 |  | 0.3 |  | 0.3 | 0.2 | 0.3 | 5.0 |
| Kam Jones | 26% | 8.4 | 2.5 |  | 0.9 |  | 1.6 |  | 0.1 |  | 0.3 | 0.1 | 0.5 | 5.0 |
| Bogoljub Markovic | 48% | 6.3<br><sub>-,-,-,-,5</sub> | 2.5<br><sub>-,-,-,-,2</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.3 |

</details>


### MIN @ SAS
Out: Tobias Harris (SAS), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Rudy Gobert (MIN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| LaMelo Ball RA under 10.5 | MIN @ SAS | draftkings | 2.03 | 2.02 | 1.69 | 59.3% | 46.2% | 49.5% | +0.4% | +20.4% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 108.4–117.7 | MIN 26% | 3.89 / 1.35 | SAS -9.5 | 225.5 | SAS -12.5 covers 41%; o228.5 45% |
| Expected (weighted by chance each plays) | 108.3–118.1 | MIN 25% | 4.05 / 1.33 | SAS -9.5 | 226.5 | SAS -12.5 covers 42%; o228.5 45% |
| if Stephon Castle plays | 107.9–118.3 | MIN 23% | 4.32 / 1.30 | SAS -10.5 | 226.5 | SAS -12.5 covers 44%; o228.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephon Castle (SAS) | Questionable | 55% | 32.5 | 17.9 | 5.5 | 6.3 | 1.7 | 1.2 | 0.3 | 3.1 | 29.7 | full tables below |

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.7<br><sub>30,31,37,35,33</sub> | 16.8<br><sub>15,14,14,19,23</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,6,6,7,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,3,4,4,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.9 | 1.8 | 25.2 |
| Ayo Dosunmu | 98% | 31.9<br><sub>27,23,26,32,30</sub> | 14.9<br><sub>14,9,9,17,15</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>7,3,1,3,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>10,3,0,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.4 | 1.8 | 23.3 |
| Jonathan Kuminga | 98% | 31.9<br><sub>27,26,36,32,22</sub> | 14.6<br><sub>11,13,10,20,5</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>8,4,10,3,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>5,1,1,5,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>2,3,0,3,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 1.4 | 22.3 |
| LaMelo Ball | 98% | 30.2<br><sub>23,17,31,28,29</sub> | 19.7<br><sub>12,15,11,8,24</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>5,1,0,4,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>5,8,6,8,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>2,4,1,2,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.2 | 2.9 | 29.6 |
| Terrence Shannon Jr. | 97% | 27.1<br><sub>22,23,24,27,20</sub> | 14.2<br><sub>13,15,14,19,11</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>4,4,4,6,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>1,3,5,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>2,3,3,1,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.1 | 1.4 | 19.4 |
| Bones Hyland | 96% | 18.8<br><sub>8,15,5,16,20</sub> | 9.4<br><sub>3,3,0,13,19</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,3,1,1,0</sub> |  | 2.5<br><sub>0,2,2,3,8</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,0,0,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.3 | 1.1 | 13.9 |
| Joan Beringer | 91% | 18.5<br><sub>15,13,17,20,18</sub> | 7.3<br><sub>9,6,12,7,4</sub> | 9.5 · –<br><sub>o 42% · u 58%</sub> | 6.2<br><sub>9,6,7,9,4</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 0.7<br><sub>0,0,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.2 |
| Trey Lyles | 98% | 18.1<br><sub>17,14,13,22,17</sub> | 5.6<br><sub>9,3,3,7,10</sub> |  | 4.0<br><sub>6,6,1,3,5</sub> |  | 1.0<br><sub>2,2,1,1,0</sub> |  | 0.7<br><sub>2,1,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 10.6 |
| Jaylen Clark | 80% | 15.5<br><sub>3,5,-,7,17</sub> | 4.9<br><sub>0,3,-,3,5</sub> |  | 2.0<br><sub>2,1,-,2,0</sub> |  | 1.0<br><sub>1,0,-,1,2</sub> |  | 0.5<br><sub>0,0,-,1,1</sub> |  | 0.8 | 0.2 | 0.5 | 7.9 |
| Zyon Pullin | 64% | 11.7<br><sub>-,5,-,-,2</sub> | 4.3<br><sub>-,2,-,-,2</sub> |  | 1.3<br><sub>-,1,-,-,0</sub> |  | 1.5<br><sub>-,0,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 7.1 |
| Rocco Zikarsky | 16% | 11.0 | 3.6 |  | 3.6 |  | 0.5 |  | 0.0 |  | 0.3 | 0.9 | 0.4 | 7.7 |
| Enrique Freeman | 16% | 9.0 | 2.7 |  | 1.8 |  | 0.4 |  | 0.1 |  | 0.3 | 0.3 | 0.4 | 5.0 |
| Cody Williams | 58% | 8.8<br><sub>3,5,-,-,2</sub> | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 1.3 |
| Isaiah Evans | 63% | 8.5<br><sub>2,4,-,-,2</sub> | 0.5<br><sub>0,0,-,-,0</sub> |  | 1.7<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>1,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 2.8 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Vassell | 98% | 35.9<br><sub>31,36,32,24,38</sub> | 14.7<br><sub>7,10,11,14,21</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 5.1<br><sub>3,4,4,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 3.4<br><sub>1,2,6,8,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>1,2,1,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.4 | 0.5 | 1.2 | 23.2 |
| Victor Wembanyama | 98% | 35.7<br><sub>34,32,29,27,39</sub> | 27.0<br><sub>12,25,23,29,36</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 11.7<br><sub>13,13,7,10,14</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 3.6<br><sub>3,2,2,2,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>0,2,2,0,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.3 | 3.5 | 3.0 | 42.3 |
| De'Aaron Fox | 98% | 35.4<br><sub>32,34,28,26,39</sub> | 19.1<br><sub>14,19,19,11,14</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>7,4,3,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 7.2<br><sub>7,9,9,6,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.6<br><sub>0,2,2,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.6 | 0.4 | 2.5 | 30.7 |
| Dylan Harper | 98% | 34.9<br><sub>32,36,28,30,37</sub> | 19.6<br><sub>18,20,22,13,13</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 6.2<br><sub>7,3,5,6,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 5.1<br><sub>5,2,2,6,8</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>0,1,3,0,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.2 | 0.4 | 2.2 | 30.9 |
| Julian Champagnie | 98% | 31.2<br><sub>30,25,28,25,31</sub> | 11.5<br><sub>8,6,12,26,6</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 5.2<br><sub>3,0,5,3,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>1,0,3,3,0</sub> |  | 2.1<br><sub>2,2,3,8,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.1 | 0.7 | 0.9 | 18.3 |
| Keldon Johnson | 98% | 24.1<br><sub>20,19,26,22,23</sub> | 11.7<br><sub>10,8,7,14,9</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>4,6,6,4,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,1,3,0,2</sub> |  | 0.9<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 1.1 | 18.0 |
| Luke Kornet | 98% | 16.1<br><sub>13,16,14,17,14</sub> | 3.8<br><sub>4,7,0,0,1</sub> |  | 4.7<br><sub>1,3,4,4,6</sub> |  | 1.1<br><sub>0,0,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.8 | 0.6 | 9.6 |
| Harrison Barnes | 67% | 12.0<br><sub>9,5,4,14,-</sub> | 3.6<br><sub>3,0,0,3,-</sub> |  | 1.4<br><sub>0,0,0,0,-</sub> |  | 0.6<br><sub>0,0,0,0,-</sub> |  | 0.4<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.7 |
| Carter Bryant | 98% | 10.9<br><sub>6,4,10,17,5</sub> | 3.2<br><sub>0,0,4,1,3</sub> |  | 1.9<br><sub>0,0,1,1,0</sub> |  | 0.7<br><sub>1,0,0,2,0</sub> |  | 0.3<br><sub>0,0,0,0,1</sub> |  | 0.3 | 0.3 | 0.5 | 5.8 |
| Jordan McLaughlin | 52% | 9.1<br><sub>-,-,3,7,-</sub> | 2.8<br><sub>-,-,0,0,-</sub> |  | 1.2<br><sub>-,-,1,0,-</sub> |  | 1.4<br><sub>-,-,0,2,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.5 | 0.1 | 0.5 | 5.4 |
| Maliq Brown | 80% | 8.2<br><sub>1,-,-,-,-</sub> | 0.5<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.5 | 3.1 |
| Ja'Kobi Gillespie | 88% | 7.6<br><sub>1,-,3,-,-</sub> | 3.9<br><sub>2,-,3,-,-</sub> |  | 0.3<br><sub>0,-,0,-,-</sub> |  | 0.7<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.9 |
| Tarris Reed Jr. | 58% | 7.6<br><sub>1,-,7,5,-</sub> | 2.6<br><sub>0,-,2,4,-</sub> |  | 2.8<br><sub>0,-,3,5,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.3 | 0.8 | 5.9 |
| David Jones Garcia | 52% | 6.9<br><sub>1,-,-,-,-</sub> | 2.6<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 1.2<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.1 |

</details>

<details><summary>if Stephon Castle plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels (MIN) | 98% | 34.7<br><sub>30,31,37,35,33</sub> | 16.7<br><sub>15,14,14,19,23</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,6,6,7,6</sub> | 5.5<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>3,3,4,4,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.9 | 1.8 | 25.1 |
| Jonathan Kuminga (MIN) | 98% | 32.0<br><sub>27,26,36,32,22</sub> | 14.6<br><sub>11,13,10,20,5</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>8,4,10,3,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.2<br><sub>5,1,1,5,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>2,3,0,3,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 1.4 | 22.4 |
| Ayo Dosunmu (MIN) | 98% | 31.8<br><sub>27,23,26,32,30</sub> | 14.9<br><sub>14,9,9,17,15</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 4.4<br><sub>7,3,1,3,7</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 4.0<br><sub>10,3,0,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.3 | 1.8 | 23.3 |
| LaMelo Ball (MIN) | 98% | 30.3<br><sub>23,17,31,28,29</sub> | 19.7<br><sub>12,15,11,8,24</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>5,1,0,4,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>5,8,6,8,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>2,4,1,2,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.2 | 2.9 | 29.6 |
| Terrence Shannon Jr. (MIN) | 97% | 27.0<br><sub>22,23,24,27,20</sub> | 14.1<br><sub>13,15,14,19,11</sub> | 12.5 · –<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>4,4,4,6,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 2.0<br><sub>1,3,5,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>2,3,3,1,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.1 | 1.4 | 19.4 |
| Bones Hyland (MIN) | 96% | 18.8<br><sub>8,15,5,16,20</sub> | 9.4<br><sub>3,3,0,13,19</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,3,1,1,0</sub> |  | 2.4<br><sub>0,2,2,3,8</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,0,0,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.3 | 1.1 | 13.9 |
| Joan Beringer (MIN) | 91% | 18.5<br><sub>15,13,17,20,18</sub> | 7.2<br><sub>9,6,12,7,4</sub> | 9.5 · –<br><sub>o 42% · u 58%</sub> | 6.2<br><sub>9,6,7,9,4</sub> | 7.5<br><sub>o 48% · u 52%</sub> | 0.7<br><sub>0,0,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.1 |
| Trey Lyles (MIN) | 98% | 18.1<br><sub>17,14,13,22,17</sub> | 5.6<br><sub>9,3,3,7,10</sub> |  | 4.0<br><sub>6,6,1,3,5</sub> |  | 0.9<br><sub>2,2,1,1,0</sub> |  | 0.7<br><sub>2,1,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 10.6 |
| Jaylen Clark (MIN) | 80% | 15.6<br><sub>3,5,-,7,17</sub> | 5.0<br><sub>0,3,-,3,5</sub> |  | 2.0<br><sub>2,1,-,2,0</sub> |  | 0.9<br><sub>1,0,-,1,2</sub> |  | 0.5<br><sub>0,0,-,1,1</sub> |  | 0.8 | 0.2 | 0.5 | 8.0 |
| Zyon Pullin (MIN) | 64% | 11.9<br><sub>-,5,-,-,2</sub> | 4.3<br><sub>-,2,-,-,2</sub> |  | 1.3<br><sub>-,1,-,-,0</sub> |  | 1.5<br><sub>-,0,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 7.1 |
| Rocco Zikarsky (MIN) | 16% | 10.9 | 3.5 |  | 3.6 |  | 0.5 |  | 0.0 |  | 0.2 | 0.9 | 0.5 | 7.6 |
| Enrique Freeman (MIN) | 16% | 9.0 | 2.6 |  | 1.9 |  | 0.4 |  | 0.1 |  | 0.3 | 0.2 | 0.4 | 4.8 |
| Cody Williams (MIN) | 58% | 8.7<br><sub>3,5,-,-,2</sub> | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 1.3 |
| Isaiah Evans (MIN) | 63% | 8.6<br><sub>2,4,-,-,2</sub> | 0.4<br><sub>0,0,-,-,0</sub> |  | 1.7<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>1,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 2.8 |
| Victor Wembanyama (SAS) | 98% | 34.1<br><sub>34,32,29,27,39</sub> | 25.2<br><sub>12,25,23,29,36</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 11.3<br><sub>13,13,7,10,14</sub> | 11.5<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>3,2,2,2,5</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.9<br><sub>0,2,2,0,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 3.6 | 2.7 | 39.7 |
| Devin Vassell (SAS) | 98% | 33.4<br><sub>31,36,32,24,38</sub> | 12.6<br><sub>7,10,11,14,21</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>3,4,4,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,2,6,8,2</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.9<br><sub>1,2,1,4,1</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.2 | 0.5 | 1.0 | 20.2 |
| De'Aaron Fox (SAS) | 98% | 32.9<br><sub>32,34,28,26,39</sub> | 16.4<br><sub>14,19,19,11,14</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 4.2<br><sub>7,4,3,4,3</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.1<br><sub>7,9,9,6,4</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,2,2,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.4 | 2.2 | 26.7 |
| Stephon Castle (SAS) | 100% | 32.5<br><sub>28,33,28,27,38</sub> | 17.9<br><sub>24,15,19,15,14</sub> | 16.5 · – | 5.5<br><sub>7,7,4,5,6</sub> | 5.5 | 6.3<br><sub>1,5,8,5,8</sub> | 5.5 | 1.7<br><sub>5,3,3,3,1</sub> | 1.5 | 1.2 | 0.3 | 3.1 | 29.7 |
| Dylan Harper (SAS) | 98% | 31.7<br><sub>32,36,28,30,37</sub> | 16.5<br><sub>18,20,22,13,13</sub> | 16.5 · –<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>7,3,5,6,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.1<br><sub>5,2,2,6,8</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 1.2<br><sub>0,1,3,0,2</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.1 | 0.4 | 1.9 | 26.1 |
| Julian Champagnie (SAS) | 98% | 28.3<br><sub>30,25,28,25,31</sub> | 10.0<br><sub>8,6,12,26,6</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>3,0,5,3,6</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>1,0,3,3,0</sub> |  | 1.8<br><sub>2,2,3,8,2</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 0.9 | 0.6 | 0.8 | 16.2 |
| Keldon Johnson (SAS) | 98% | 20.7<br><sub>20,19,26,22,23</sub> | 9.9<br><sub>10,8,7,14,9</sub> | 10.5 · –<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>4,6,6,4,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.1<br><sub>1,1,3,0,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.6 | 0.2 | 0.9 | 15.2 |
| Luke Kornet (SAS) | 98% | 13.9<br><sub>13,16,14,17,14</sub> | 3.3<br><sub>4,7,0,0,1</sub> |  | 4.0<br><sub>1,3,4,4,6</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 8.2 |
| Harrison Barnes (SAS) | 67% | 8.6<br><sub>9,5,4,14,-</sub> | 2.8<br><sub>3,0,0,3,-</sub> |  | 1.1<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Carter Bryant (SAS) | 98% | 8.1<br><sub>6,4,10,17,5</sub> | 2.6<br><sub>0,0,4,1,3</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>1,0,0,2,0</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.2 | 0.2 | 0.4 | 4.5 |
| Maliq Brown (SAS) | 80% | 6.9<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 2.2<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 2.9 |
| Jordan McLaughlin (SAS) | 52% | 6.3<br><sub>-,-,3,7,-</sub> | 2.1<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 1.0<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.0 |
| Tarris Reed Jr. (SAS) | 58% | 6.0<br><sub>1,-,7,5,-</sub> | 2.4<br><sub>0,-,2,4,-</sub> |  | 2.2<br><sub>0,-,3,5,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.7 | 5.0 |
| Ja'Kobi Gillespie (SAS) | 88% | 5.9<br><sub>1,-,3,-,-</sub> | 4.2<br><sub>2,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>0,-,1,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 5.0 |
| David Jones Garcia (SAS) | 52% | 5.7<br><sub>1,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |

</details>


### OKC @ HOU
Out: Steven Adams (HOU), Reed Sheppard (HOU), Fred VanVleet (HOU), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. 3PM over 2.5 (3+) | OKC @ HOU | draftkings | 2.43 | 2.39 | 1.95 | 51.2% | 38.7% | 41.8% | +1.6% | +24.3% | 0.3% |
| Kevin Durant PA over 26.5 (27+) | OKC @ HOU | draftkings | 1.92 | 1.91 | 1.61 | 62.1% | 49.1% | 52.3% | +0.3% | +19.0% | 0.1% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.6<br><sub>36,35,36,30,28</sub> | 30.4<br><sub>32,17,34,26,21</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,2,6,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 6.7<br><sub>4,3,5,3,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.9 | 3.3 | 41.0 |
| Jared McCain | 98% | 30.0<br><sub>22,18,21,30,29</sub> | 15.9<br><sub>20,4,3,18,10</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>2,0,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,1,0,4,4</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>6,0,1,4,0</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 0.8 | 0.2 | 1.9 | 21.1 |
| Ajay Mitchell | 98% | 29.6<br><sub>23,23,28,25,28</sub> | 19.0<br><sub>4,12,18,30,29</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>5,0,6,2,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>6,0,4,5,3</sub> | 3.5<br><sub>o 59% · u 41%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.3 | 2.2 | 26.9 |
| Josh Dix | 67% | 27.2<br><sub>-,-,-,22,24</sub> | 4.4<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.4 |
| Bennett Stirtz | 96% | 26.7<br><sub>1,2,11,25,28</sub> | 7.9<br><sub>0,0,2,7,8</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 1.0<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.1 |
| Isaiah Hartenstein | 98% | 26.6<br><sub>17,23,27,26,26</sub> | 10.2<br><sub>4,6,12,15,10</sub> | 9.5 · –<br><sub>o 53% · u 47%</sub> | 9.5<br><sub>3,6,12,13,14</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,2,1,3,3</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 22.9 |
| Aday Mara | 96% | 24.2<br><sub>12,13,14,20,21</sub> | 8.2<br><sub>7,2,2,11,6</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>2,3,3,10,3</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 1.3<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.4 | 15.6 |
| Kenrich Williams | 93% | 21.7<br><sub>7,6,7,24,17</sub> | 8.0<br><sub>3,3,3,3,7</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>2,1,1,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.9 | 13.9 |
| Jaylin Williams | 98% | 21.3<br><sub>17,15,5,26,20</sub> | 6.1<br><sub>5,3,0,6,0</sub> |  | 5.3<br><sub>4,7,0,6,5</sub> |  | 2.0<br><sub>1,3,0,3,1</sub> |  | 0.9<br><sub>1,1,0,2,0</sub> |  | 0.6 | 0.5 | 0.8 | 13.3 |
| Micah Peavy | 48% | 13.1<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer | 80% | 13.0<br><sub>1,2,-,3,14</sub> | 3.5<br><sub>0,0,-,0,3</sub> |  | 2.5<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.8<br><sub>36,39,28,33,39</sub> | 18.8<br><sub>20,17,15,23,15</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>10,11,5,4,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>4,6,2,3,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.8 | 31.9 |
| Kevin Durant | 98% | 37.6<br><sub>37,37,30,31,37</sub> | 25.8<br><sub>20,22,22,18,28</sub> | 22.5 · –<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>7,4,9,5,5</sub> | 4.5<br><sub>o 61% · u 39%</sub> | 5.1<br><sub>6,2,3,4,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,3,1,2,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.8 | 1.0 | 3.8 | 37.4 |
| Jabari Smith Jr. | 98% | 37.1<br><sub>34,33,39,30,35</sub> | 17.4<br><sub>7,14,16,14,22</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>5,5,12,2,3</sub> | 5.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>1,3,5,2,2</sub> |  | 2.7<br><sub>1,2,2,3,3</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.8 | 1.8 | 27.0 |
| Alperen Sengun | 58% | 35.4<br><sub>36,33,37,-,-</sub> | 19.7<br><sub>29,17,29,-,-</sub> | 18.5 · –<br><sub>o 48% · u 52%</sub> | 10.0<br><sub>7,10,9,-,-</sub> | 8.5<br><sub>o 53% · u 47%</sub> | 6.3<br><sub>7,7,9,-,-</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>2,1,1,-,-</sub> |  | 1.2 | 0.9 | 3.6 | 36.0 |
| Tari Eason | 98% | 30.9<br><sub>27,31,33,31,26</sub> | 12.6<br><sub>12,19,13,5,11</sub> | 10.5 · –<br><sub>o 51% · u 49%</sub> | 7.4<br><sub>6,3,8,9,13</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,2,1,2</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.4 | 0.7 | 1.5 | 21.7 |
| Marcus Smart | 63% | 26.0<br><sub>21,-,-,-,17</sub> | 9.2<br><sub>5,-,-,-,8</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 2.8<br><sub>3,-,-,-,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>1,-,-,-,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,-,-,-,0</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.4 | 0.3 | 1.9 | 15.2 |
| Clint Capela | 88% | 22.3<br><sub>-,11,4,22,30</sub> | 6.5<br><sub>-,2,2,10,5</sub> |  | 7.8<br><sub>-,3,2,8,11</sub> |  | 1.4<br><sub>-,1,0,2,5</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.2 | 0.9 | 15.7 |
| Bogdan Bogdanovic | 91% | 19.5<br><sub>9,20,13,15,11</sub> | 7.8<br><sub>3,11,5,16,6</sub> |  | 2.4<br><sub>1,1,2,2,1</sub> |  | 1.9<br><sub>0,1,1,4,0</sub> |  | 1.3<br><sub>1,3,1,4,0</sub> |  | 0.6 | 0.2 | 0.9 | 12.1 |
| Oscar Tshiebwe | 76% | 16.5<br><sub>-,-,-,14,11</sub> | 6.3<br><sub>-,-,-,7,0</sub> |  | 6.8<br><sub>-,-,-,5,5</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.4 | 1.0 | 14.0 |
| Jae'Sean Tate | 64% | 9.5<br><sub>-,1,1,4,-</sub> | 3.1<br><sub>-,0,0,0,-</sub> |  | 2.1<br><sub>-,0,1,0,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Bruce Thornton | 63% | 8.7<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,0,0,5,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Isaiah Crawford | 58% | 8.3<br><sub>-,1,1,5,-</sub> | 2.7<br><sub>-,0,0,3,-</sub> |  | 1.5<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-31/`._
