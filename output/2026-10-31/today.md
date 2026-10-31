# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sat 31 Oct, 07:24 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| SAC @ MEM | player points | Jaylen Wells projected 16.8 pts vs DraftKings line 11.5 | minutes 30 vs 28 this season; scoring 0.55/min vs 0.49 this season, 0.48 last season |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jrue Holiday AST over 9.5 (10+) | POR @ UTA | draftkings | 14.80 | 12.38 | 7.48 | 13.4% | 6.3% | 8.1% | +19.6% | +97.8% | 0.4% |
| Damian Lillard AST over 9.5 (10+) | POR @ UTA | draftkings | 14.00 | 11.98 | 7.47 | 13.4% | 6.7% | 8.3% | +16.9% | +87.3% | 0.3% |
| Deni Avdija PTS over 44.5 (45+) | POR @ UTA | draftkings | 27.00 | 23.09 | 14.45 | 6.9% | 3.5% | 4.3% | +16.8% | +86.8% | 0.2% |
| Deni Avdija PTS over 39.5 (40+) | POR @ UTA | draftkings | 13.80 | 11.96 | 7.61 | 13.1% | 6.8% | 8.4% | +15.4% | +81.3% | 0.3% |
| Cameron Boozer REB over 13.5 (14+) | SAC @ MEM | draftkings | 11.20 | 9.71 | 6.18 | 16.2% | 8.3% | 10.3% | +15.4% | +81.2% | 0.4% |
| Kingston Flemings AST over 7.5 (8+) | ATL @ NOP | draftkings | 22.00 | 19.23 | 12.41 | 8.1% | 4.2% | 5.2% | +14.4% | +77.3% | 0.2% |
| Kingston Flemings AST over 5.5 (6+) | ATL @ NOP | draftkings | 7.60 | 6.68 | 4.35 | 23.0% | 12.3% | 15.0% | +13.8% | +74.9% | 0.5% |
| Cameron Boozer REB over 15.5 (16+) | SAC @ MEM | draftkings | 22.00 | 19.49 | 12.89 | 7.8% | 4.2% | 5.1% | +12.8% | +70.6% | 0.1% |
| Precious Achiuwa PA over 24.5 (25+) | SAC @ MEM | draftkings | 10.50 | 9.41 | 6.32 | 15.8% | 8.9% | 10.6% | +11.6% | +66.1% | 0.3% |
| De'Andre Hunter REB over 7.5 (8+) | SAC @ MEM | draftkings | 7.60 | 6.85 | 4.66 | 21.5% | 12.3% | 14.6% | +10.9% | +63.1% | 0.4% |
| Jabari Smith Jr. REB over 11.5 (12+) | OKC @ HOU | draftkings | 17.80 | 16.13 | 11.06 | 9.0% | 5.2% | 6.2% | +10.3% | +60.9% | 0.1% |
| Jrue Holiday AST over 7.5 (8+) | POR @ UTA | draftkings | 5.33 | 4.85 | 3.36 | 29.8% | 17.5% | 20.6% | +9.8% | +58.8% | 0.6% |
| Damian Lillard AST over 7.5 (8+) | POR @ UTA | draftkings | 5.02 | 4.60 | 3.22 | 31.1% | 18.6% | 21.7% | +9.1% | +55.9% | 0.6% |
| De'Andre Hunter REB over 9.5 (10+) | SAC @ MEM | draftkings | 19.40 | 17.83 | 12.49 | 8.0% | 4.8% | 5.6% | +8.9% | +55.3% | 0.1% |
| Deni Avdija PTS over 34.5 (35+) | POR @ UTA | draftkings | 6.43 | 6.00 | 4.34 | 23.1% | 14.5% | 16.7% | +7.2% | +48.3% | 0.3% |
| Trey Murphy III REB over 7.5 (8+) | ATL @ NOP | draftkings | 6.94 | 6.48 | 4.69 | 21.3% | 13.5% | 15.4% | +7.1% | +48.1% | 0.3% |
| Donovan Mitchell PTS over 44.5 (45+) | CLE @ MIL | draftkings | 25.00 | 23.36 | 16.89 | 5.9% | 3.7% | 4.3% | +7.1% | +48.0% | 0.1% |
| Precious Achiuwa PA over 29.5 (30+) | SAC @ MEM | draftkings | 24.00 | 22.42 | 16.25 | 6.2% | 3.9% | 4.5% | +7.0% | +47.7% | 0.1% |
| Dylan Harper REB over 9.5 (10+) | MIN @ SAS | draftkings | 17.20 | 16.10 | 11.71 | 8.5% | 5.4% | 6.2% | +6.8% | +46.9% | 0.1% |
| Precious Achiuwa PA over 19.5 (20+) | SAC @ MEM | draftkings | 4.16 | 3.89 | 2.83 | 35.3% | 22.5% | 25.7% | +6.8% | +46.9% | 0.5% |
| Jrue Holiday PA over 29.5 (30+) | POR @ UTA | draftkings | 8.70 | 8.16 | 5.97 | 16.8% | 10.7% | 12.2% | +6.6% | +45.8% | 0.2% |
| Jeremiah Fears AST over 5.5 (6+) | ATL @ NOP | draftkings | 6.54 | 6.14 | 4.49 | 22.3% | 14.3% | 16.3% | +6.5% | +45.7% | 0.3% |
| Ryan Rollins AST over 7.5 (8+) | CLE @ MIL | draftkings | 8.30 | 7.80 | 5.71 | 17.5% | 11.3% | 12.8% | +6.5% | +45.4% | 0.2% |
| Dylan Harper REB over 7.5 (8+) | MIN @ SAS | draftkings | 6.36 | 6.00 | 4.43 | 22.6% | 14.7% | 16.7% | +6.0% | +43.7% | 0.3% |
| Jeremiah Fears AST over 7.5 (8+) | ATL @ NOP | draftkings | 21.00 | 19.80 | 14.63 | 6.8% | 4.5% | 5.1% | +6.0% | +43.5% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kingston Flemings AST over 6.5 (7+) | ATL @ NOP | draftkings | 13.60 | 11.48 | 7.03 | 14.2% | 6.9% | 8.7% | +18.5% | +93.5% | 0.4% |
| Jrue Holiday AST over 10.5 (11+) | POR @ UTA | draftkings | 23.00 | 19.49 | 12.01 | 8.3% | 4.1% | 5.1% | +18.0% | +91.6% | 0.2% |
| Cameron Boozer REB over 14.5 (15+) | SAC @ MEM | draftkings | 16.40 | 14.04 | 8.77 | 11.4% | 5.7% | 7.1% | +16.8% | +86.9% | 0.3% |
| Jrue Holiday AST over 8.5 (9+) | POR @ UTA | draftkings | 9.00 | 7.75 | 4.88 | 20.5% | 10.4% | 12.9% | +16.2% | +84.4% | 0.5% |
| Damian Lillard AST over 10.5 (11+) | POR @ UTA | draftkings | 22.00 | 19.08 | 12.19 | 8.2% | 4.2% | 5.2% | +15.2% | +80.5% | 0.2% |
| Damian Lillard AST over 8.5 (9+) | POR @ UTA | draftkings | 8.40 | 7.36 | 4.77 | 21.0% | 11.1% | 13.6% | +14.1% | +76.0% | 0.5% |
| Cameron Boozer AST over 10.5 (11+) | SAC @ MEM | draftkings | 22.00 | 19.69 | 13.17 | 7.6% | 4.2% | 5.1% | +11.9% | +67.1% | 0.1% |
| De'Andre Hunter REB over 8.5 (9+) | SAC @ MEM | draftkings | 12.40 | 11.11 | 7.47 | 13.4% | 7.5% | 9.0% | +11.6% | +66.0% | 0.2% |
| Cameron Boozer REB over 12.5 (13+) | SAC @ MEM | draftkings | 7.40 | 6.64 | 4.46 | 22.4% | 12.6% | 15.1% | +11.6% | +65.8% | 0.4% |
| Jeremiah Fears AST over 6.5 (7+) | ATL @ NOP | draftkings | 11.80 | 10.83 | 7.59 | 13.2% | 7.9% | 9.2% | +8.9% | +55.4% | 0.2% |
| Kingston Flemings AST over 4.5 (5+) | ATL @ NOP | draftkings | 4.25 | 3.93 | 2.79 | 35.8% | 22.0% | 25.4% | +8.2% | +52.2% | 0.6% |
| De'Andre Hunter REB over 6.5 (7+) | SAC @ MEM | draftkings | 4.69 | 4.34 | 3.09 | 32.3% | 19.9% | 23.0% | +8.0% | +51.6% | 0.5% |
| Dylan Harper REB over 8.5 (9+) | MIN @ SAS | draftkings | 10.50 | 9.74 | 6.96 | 14.4% | 8.9% | 10.3% | +7.8% | +50.8% | 0.2% |
| Darius Acuff Jr. REB over 6.5 (7+) | SAC @ MEM | draftkings | 8.20 | 7.66 | 5.54 | 18.0% | 11.4% | 13.1% | +7.1% | +47.9% | 0.2% |
| Ryan Rollins AST over 8.5 (9+) | CLE @ MIL | draftkings | 13.60 | 12.76 | 9.32 | 10.7% | 6.9% | 7.8% | +6.6% | +46.0% | 0.1% |
| Trey Murphy III REB over 8.5 (9+) | ATL @ NOP | draftkings | 11.60 | 10.88 | 7.95 | 12.6% | 8.1% | 9.2% | +6.6% | +45.9% | 0.2% |
| Cameron Boozer REB over 16.5 (17+) | SAC @ MEM | draftkings | 29.00 | 27.32 | 20.06 | 5.0% | 3.2% | 3.7% | +6.2% | +44.6% | 0.1% |
| Dejounte Murray AST over 10.5 (11+) | ATL @ NOP | draftkings | 11.80 | 11.11 | 8.18 | 12.2% | 7.9% | 9.0% | +6.2% | +44.2% | 0.1% |
| Jrue Holiday AST over 6.5 (7+) | POR @ UTA | draftkings | 3.35 | 3.19 | 2.40 | 41.7% | 27.9% | 31.4% | +5.0% | +39.8% | 0.5% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 19.80 | 18.87 | 14.17 | 7.1% | 4.7% | 5.3% | +5.0% | +39.7% | 0.1% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| VJ Edgecombe PTS under 16.5 | PHI @ CHA | draftkings | 1.89 | Jaylen Brown | 73.6% | 85.2% | +9.4% |
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.35 | Alperen Sengun | 75.9% | 64.4% | +8.2% |
| Tyrese Maxey PTS under 29.5 | PHI @ CHA | draftkings | 1.87 | Jaylen Brown | 67.7% | 80.8% | +6.0% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 1.97 | Alperen Sengun | 80.8% | 70.7% | +5.3% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AJ Green 3PM under 1.5 | CLE @ MIL | draftkings | 2.35 | 2.16 | 1.51 | 66.2% | 39.8% | 46.4% | +9.0% | +55.7% | 1.7% |
| De'Andre Hunter REB over 5.5 (6+) | SAC @ MEM | draftkings | 3.05 | 2.89 | 2.16 | 46.4% | 30.6% | 34.6% | +5.4% | +41.4% | 0.7% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play).

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| POR @ UTA | Sun 01 Nov 06:00 | 121.7–114.6 | POR 69% | 1.45 / 3.24 | UTA +7.5 | 236.5 | UTA +6.5 covers 48%; o231.5 60% |
| PHI @ CHA | Sun 01 Nov 09:00 | 107.1–110.0 | PHI 42% | 2.37 / 1.73 | CHA -3.5 | 216.5 | CHA +1.5 covers 61%; o214.5 55% |
| ATL @ NOP | Sun 01 Nov 10:00 | 123.8–120.7 | ATL 59% | 1.69 / 2.44 | NOP +3.5 | 244.5 | NOP +4.5 covers 53%; o241.5 56% |
| SAC @ MEM | Sun 01 Nov 11:00 | 115.4–122.8 | SAC 30% | 3.32 / 1.43 | MEM -7.5 | 238.5 | MEM -11.5 covers 39%; o233.5 60% |
| CLE @ MIL | Sun 01 Nov 11:00 | 118.0–113.7 | CLE 62% | 1.61 / 2.64 | MIL +4.5 | 231.5 | MIL +9.5 covers 64%; o237.5 37% |
| MIN @ SAS | Sun 01 Nov 11:00 | 109.9–116.8 | MIN 31% | 3.18 / 1.46 | SAS -6.5 | 226.5 | SAS -12.5 covers 34%; o226.5 50% |
| OKC @ HOU | Sun 01 Nov 11:30 | 111.5–114.0 | OKC 43% | 2.30 / 1.77 | HOU -2.5 | 225.5 | HOU -3.5 covers 48%; o218.5 64% |

### POR @ UTA
Out: Trey Alexander (UTA), Blake Hinson (UTA), Jaren Jackson Jr. (UTA), Jusuf Nurkic (UTA), Ja Morant (POR), Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard AST over 5.5 (6+) | POR @ UTA | draftkings | 2.13 | 2.10 | 1.72 | 58.1% | 44.1% | 47.6% | +1.3% | +23.6% | 0.3% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 121.7–114.6 | POR 69% | 1.45 / 3.24 | UTA +7.5 | 236.5 | UTA +6.5 covers 48%; o231.5 60% |
| Expected (weighted by chance each plays) | 122.0–115.5 | POR 68% | 1.46 / 3.17 | UTA +6.5 | 237.5 | UTA +6.5 covers 50%; o231.5 62% |
| if Robert Williams III plays | 122.8–115.0 | POR 71% | 1.41 / 3.45 | UTA +7.5 | 237.5 | UTA +6.5 covers 46%; o231.5 63% |
| if Lauri Markkanen plays | 121.2–115.5 | POR 66% | 1.52 / 2.91 | UTA +5.5 | 236.5 | UTA +6.5 covers 52%; o231.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Robert Williams III (POR) | Questionable | 55% | 20.9 | 8.4 | 8.2 | 1.5 | 0.2 | 0.7 | 1.7 | 1.1 | 18.0 | full tables below |
| Lauri Markkanen (UTA) | Questionable | 55% | 30.5 | 20.2 | 6.4 | 2.1 | 2.1 | 0.8 | 0.5 | 1.6 | 28.8 | full tables below |
| Chris Youngblood (POR) | Questionable | 55% | 10.9 | 3.9 | 1.6 | 0.8 | 0.6 | 0.4 | 0.2 | 0.5 | 6.3 | small |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.7<br><sub>23,38,33,32</sub> | 28.5<br><sub>18,26,23,24</sub> | 24.5 · – | 7.5<br><sub>10,7,4,9</sub> | 7.5 | 7.4<br><sub>4,6,9,7</sub> | 6.5 | 2.0<br><sub>2,1,4,0</sub> | 1.5 | 0.9 | 0.7 | 4.2 | 43.4 |
| Damian Lillard | 98% | 33.1<br><sub>24,33,31,30</sub> | 21.6<br><sub>25,19,21,9</sub> | 23.5 · – | 4.4<br><sub>3,5,5,2</sub> | 3.5 | 6.4<br><sub>6,2,4,2</sub> | 5.5 | 2.8<br><sub>6,2,4,1</sub> | 3.5 | 1.1 | 0.3 | 2.5 | 32.4 |
| Jrue Holiday | 98% | 31.5<br><sub>21,26,30,24</sub> | 16.3<br><sub>8,12,22,6</sub> | 13.5 · – | 4.9<br><sub>4,1,4,6</sub> | 4.5 | 6.2<br><sub>1,8,3,4</sub> | 4.5 | 2.5<br><sub>0,3,2,2</sub> | 2.5 | 1.2 | 0.3 | 2.5 | 27.5 |
| Toumani Camara | 98% | 30.7<br><sub>23,27,24,26</sub> | 13.0<br><sub>18,19,12,13</sub> | 12.5 · – | 4.8<br><sub>2,3,1,2</sub> | 4.5 | 2.1<br><sub>3,1,1,1</sub> | 1.5 | 2.3<br><sub>4,5,4,3</sub> | 2.5 | 1.2 | 0.5 | 1.4 | 19.9 |
| Donovan Clingan | 98% | 28.3<br><sub>21,21,26,29</sub> | 12.6<br><sub>11,8,9,11</sub> | 11.5 · – | 11.8<br><sub>7,10,10,8</sub> | 11.5 | 2.3<br><sub>2,3,1,1</sub> | 1.5 | 1.3<br><sub>2,0,2,1</sub> | 1.5 | 0.7 | 2.4 | 1.4 | 26.6 |
| Sidy Cissoko | 96% | 25.7<br><sub>25,26,20,19</sub> | 7.2<br><sub>3,15,6,4</sub> |  | 3.9<br><sub>4,7,2,6</sub> |  | 2.4<br><sub>3,1,4,2</sub> |  | 1.0<br><sub>1,2,0,0</sub> |  | 1.1 | 0.5 | 1.1 | 13.4 |
| Scoot Henderson | 98% | 25.5<br><sub>19,21,17,19</sub> | 13.4<br><sub>15,4,2,9</sub> | 14.5 · – | 2.9<br><sub>2,1,2,4</sub> | 3.5 | 3.4<br><sub>1,2,3,0</sub> | 3.5 | 1.7<br><sub>1,0,0,1</sub> | 1.5 | 1.3 | 0.2 | 2.5 | 19.8 |
| Micah Potter | 63% | 15.6<br><sub>12,-,-,9</sub> | 6.4<br><sub>4,-,-,1</sub> |  | 4.5<br><sub>3,-,-,2</sub> |  | 1.0<br><sub>0,-,-,0</sub> |  | 0.7<br><sub>0,-,-,0</sub> |  | 0.5 | 0.4 | 0.9 | 11.9 |
| Vit Krejci | 96% | 15.4<br><sub>15,3,7,8</sub> | 5.5<br><sub>1,0,4,2</sub> |  | 2.1<br><sub>2,2,0,0</sub> |  | 1.5<br><sub>3,0,0,1</sub> |  | 0.8<br><sub>0,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 9.0 |
| Branden Carlson | 48% | 14.4<br><sub>-,-,-,12</sub> | 5.1<br><sub>-,-,-,2</sub> |  | 3.0<br><sub>-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,0</sub> |  | 0.6 | 1.5 | 1.7 | 9.1 |
| Yang Hansen | 58% | 11.4<br><sub>12,-,-,5</sub> | 4.0<br><sub>5,-,-,3</sub> |  | 2.9<br><sub>3,-,-,2</sub> |  | 0.7<br><sub>0,-,-,1</sub> |  | 0.3<br><sub>1,-,-,1</sub> |  | 0.3 | 0.5 | 0.9 | 7.5 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 34.1<br><sub>29,32,33,33,37</sub> | 25.8<br><sub>22,19,24,26,31</sub> | 22.5 · – | 3.8<br><sub>3,1,9,3,4</sub> |  | 7.0<br><sub>5,10,10,6,3</sub> |  | 2.5<br><sub>4,3,2,0,5</sub> | 2.5 | 1.0 | 0.2 | 3.9 | 36.6 |
| Ace Bailey | 98% | 34.0<br><sub>24,22,29,34,40</sub> | 16.8<br><sub>12,6,17,17,19</sub> | 15.5 · – | 6.4<br><sub>5,7,12,10,6</sub> |  | 3.0<br><sub>3,2,4,3,0</sub> |  | 2.1<br><sub>2,1,1,3,1</sub> | 1.5 | 1.0 | 1.4 | 2.3 | 26.2 |
| Jaxson Hayes | 98% | 30.7<br><sub>26,26,19,-,37</sub> | 10.5<br><sub>5,17,9,-,2</sub> | 8.5 · – | 7.2<br><sub>5,5,5,-,11</sub> |  | 2.2<br><sub>3,2,1,-,4</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.9 | 1.5 | 1.3 | 19.8 |
| Darryn Peterson | 96% | 30.6<br><sub>31,30,30,26,26</sub> | 15.0<br><sub>9,15,8,14,18</sub> | 14.5 · – | 4.7<br><sub>4,3,3,7,5</sub> |  | 3.4<br><sub>3,1,2,4,3</sub> |  | 1.2<br><sub>0,1,0,3,3</sub> | 1.5 | 1.1 | 0.4 | 1.7 | 23.1 |
| Isaiah Collier | 96% | 24.7<br><sub>16,18,13,21,24</sub> | 12.6<br><sub>7,10,6,7,7</sub> |  | 3.4<br><sub>3,2,3,8,7</sub> |  | 7.2<br><sub>3,7,6,8,6</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.3 | 2.6 | 23.1 |
| Josh Okogie | 86% | 23.5<br><sub>8,-,10,21,28</sub> | 5.3<br><sub>0,-,2,0,5</sub> |  | 4.0<br><sub>1,-,2,2,9</sub> |  | 1.4<br><sub>0,-,2,0,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 1.1 | 0.4 | 0.8 | 10.7 |
| Josh Green | 72% | 21.4<br><sub>-,-,3,25,24</sub> | 4.7<br><sub>-,-,0,6,2</sub> |  | 2.3<br><sub>-,-,0,4,2</sub> |  | 1.2<br><sub>-,-,1,1,2</sub> |  | 0.6<br><sub>-,-,0,1,0</sub> |  | 0.8 | 0.2 | 0.8 | 8.2 |
| Brice Sensabaugh | 98% | 20.7<br><sub>14,16,17,9,18</sub> | 12.1<br><sub>2,10,7,11,16</sub> |  | 3.0<br><sub>2,3,6,2,3</sub> |  | 1.9<br><sub>1,2,1,0,1</sub> |  | 1.6<br><sub>0,2,1,3,4</sub> |  | 0.6 | 0.2 | 1.7 | 17.0 |
| Mo Bamba | 52% | 19.4<br><sub>-,-,-,29,16</sub> | 6.9<br><sub>-,-,-,14,8</sub> |  | 6.8<br><sub>-,-,-,7,4</sub> |  | 0.9<br><sub>-,-,-,1,1</sub> |  | 0.5<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.4 | 1.0 | 14.7 |
| Svi Mykhailiuk | 88% | 18.7<br><sub>19,21,14,13,15</sub> | 7.0<br><sub>10,3,2,0,3</sub> |  | 2.2<br><sub>1,4,3,1,2</sub> |  | 1.4<br><sub>2,1,0,0,1</sub> |  | 1.1<br><sub>2,0,0,0,1</sub> |  | 0.6 | 0.1 | 0.8 | 10.6 |
| Kyle Filipowski | 58% | 15.0<br><sub>9,8,-,8,-</sub> | 8.0<br><sub>3,0,-,0,-</sub> |  | 4.8<br><sub>0,1,-,1,-</sub> |  | 1.8<br><sub>0,0,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.7 | 0.3 | 1.2 | 14.6 |
| Tony Bradley | 48% | 9.5<br><sub>-,-,-,6,-</sub> | 3.4<br><sub>-,-,-,2,-</sub> |  | 3.0<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.3 | 0.6 | 6.9 |

</details>

<details><summary>if Lauri Markkanen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija (POR) | 98% | 34.6<br><sub>23,38,33,32</sub> | 28.2<br><sub>18,26,23,24</sub> | 24.5 · – | 7.4<br><sub>10,7,4,9</sub> | 7.5 | 7.5<br><sub>4,6,9,7</sub> | 6.5 | 2.0<br><sub>2,1,4,0</sub> | 1.5 | 0.9 | 0.7 | 4.2 | 43.1 |
| Damian Lillard (POR) | 98% | 33.1<br><sub>24,33,31,30</sub> | 21.6<br><sub>25,19,21,9</sub> | 23.5 · – | 4.3<br><sub>3,5,5,2</sub> | 3.5 | 6.4<br><sub>6,2,4,2</sub> | 5.5 | 2.9<br><sub>6,2,4,1</sub> | 3.5 | 1.1 | 0.3 | 2.5 | 32.3 |
| Jrue Holiday (POR) | 98% | 31.5<br><sub>21,26,30,24</sub> | 16.3<br><sub>8,12,22,6</sub> | 13.5 · – | 4.9<br><sub>4,1,4,6</sub> | 4.5 | 6.3<br><sub>1,8,3,4</sub> | 4.5 | 2.5<br><sub>0,3,2,2</sub> | 2.5 | 1.2 | 0.3 | 2.5 | 27.5 |
| Toumani Camara (POR) | 98% | 30.8<br><sub>23,27,24,26</sub> | 13.1<br><sub>18,19,12,13</sub> | 12.5 · – | 4.8<br><sub>2,3,1,2</sub> | 4.5 | 2.1<br><sub>3,1,1,1</sub> | 1.5 | 2.4<br><sub>4,5,4,3</sub> | 2.5 | 1.2 | 0.5 | 1.4 | 19.9 |
| Donovan Clingan (POR) | 98% | 28.4<br><sub>21,21,26,29</sub> | 12.6<br><sub>11,8,9,11</sub> | 11.5 · – | 11.8<br><sub>7,10,10,8</sub> | 11.5 | 2.3<br><sub>2,3,1,1</sub> | 1.5 | 1.3<br><sub>2,0,2,1</sub> | 1.5 | 0.7 | 2.4 | 1.4 | 26.7 |
| Sidy Cissoko (POR) | 96% | 25.7<br><sub>25,26,20,19</sub> | 7.1<br><sub>3,15,6,4</sub> |  | 3.8<br><sub>4,7,2,6</sub> |  | 2.4<br><sub>3,1,4,2</sub> |  | 0.9<br><sub>1,2,0,0</sub> |  | 1.0 | 0.5 | 1.1 | 13.3 |
| Scoot Henderson (POR) | 98% | 25.3<br><sub>19,21,17,19</sub> | 13.4<br><sub>15,4,2,9</sub> | 14.5 · – | 2.9<br><sub>2,1,2,4</sub> | 3.5 | 3.4<br><sub>1,2,3,0</sub> | 3.5 | 1.7<br><sub>1,0,0,1</sub> | 1.5 | 1.3 | 0.2 | 2.5 | 19.7 |
| Micah Potter (POR) | 63% | 15.6<br><sub>12,-,-,9</sub> | 6.3<br><sub>4,-,-,1</sub> |  | 4.5<br><sub>3,-,-,2</sub> |  | 1.0<br><sub>0,-,-,0</sub> |  | 0.7<br><sub>0,-,-,0</sub> |  | 0.5 | 0.4 | 0.9 | 11.8 |
| Vit Krejci (POR) | 96% | 15.4<br><sub>15,3,7,8</sub> | 5.4<br><sub>1,0,4,2</sub> |  | 2.1<br><sub>2,2,0,0</sub> |  | 1.5<br><sub>3,0,0,1</sub> |  | 0.8<br><sub>0,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 9.0 |
| Branden Carlson (POR) | 48% | 14.5<br><sub>-,-,-,12</sub> | 5.2<br><sub>-,-,-,2</sub> |  | 3.0<br><sub>-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,0</sub> |  | 0.6 | 1.5 | 1.7 | 9.1 |
| Yang Hansen (POR) | 58% | 11.5<br><sub>12,-,-,5</sub> | 4.0<br><sub>5,-,-,3</sub> |  | 2.9<br><sub>3,-,-,2</sub> |  | 0.7<br><sub>0,-,-,1</sub> |  | 0.3<br><sub>1,-,-,1</sub> |  | 0.3 | 0.5 | 0.9 | 7.6 |
| Keyonte George (UTA) | 98% | 33.2<br><sub>29,32,33,33,37</sub> | 23.3<br><sub>22,19,24,26,31</sub> | 22.5 · – | 3.7<br><sub>3,1,9,3,4</sub> |  | 6.6<br><sub>5,10,10,6,3</sub> |  | 2.4<br><sub>4,3,2,0,5</sub> | 2.5 | 0.9 | 0.2 | 3.5 | 33.6 |
| Ace Bailey (UTA) | 98% | 32.3<br><sub>24,22,29,34,40</sub> | 14.6<br><sub>12,6,17,17,19</sub> | 15.5 · – | 6.1<br><sub>5,7,12,10,6</sub> |  | 2.6<br><sub>3,2,4,3,0</sub> |  | 1.9<br><sub>2,1,1,3,1</sub> | 1.5 | 0.9 | 1.3 | 1.9 | 23.3 |
| Lauri Markkanen (UTA) | 100% | 30.5<br><sub>36,34,38,6,-</sub> | 20.2<br><sub>18,16,28,2,-</sub> | 22.5 · – | 6.4<br><sub>9,6,7,0,-</sub> |  | 2.1<br><sub>3,3,1,0,-</sub> |  | 2.1<br><sub>1,4,5,0,-</sub> | 2.5 | 0.8 | 0.5 | 1.6 | 28.8 |
| Darryn Peterson (UTA) | 96% | 28.6<br><sub>31,30,30,26,26</sub> | 12.7<br><sub>9,15,8,14,18</sub> | 14.5 · – | 4.4<br><sub>4,3,3,7,5</sub> |  | 2.9<br><sub>3,1,2,4,3</sub> |  | 1.0<br><sub>0,1,0,3,3</sub> | 1.5 | 1.0 | 0.3 | 1.5 | 20.0 |
| Jaxson Hayes (UTA) | 98% | 28.1<br><sub>26,26,19,-,37</sub> | 9.4<br><sub>5,17,9,-,2</sub> | 8.5 · – | 6.8<br><sub>5,5,5,-,11</sub> |  | 2.0<br><sub>3,2,1,-,4</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.8 | 1.4 | 1.1 | 18.2 |
| Isaiah Collier (UTA) | 96% | 21.9<br><sub>16,18,13,21,24</sub> | 10.2<br><sub>7,10,6,7,7</sub> |  | 3.0<br><sub>3,2,3,8,7</sub> |  | 6.3<br><sub>3,7,6,8,6</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.3 | 2.2 | 19.5 |
| Josh Okogie (UTA) | 86% | 20.0<br><sub>8,-,10,21,28</sub> | 4.5<br><sub>0,-,2,0,5</sub> |  | 3.5<br><sub>1,-,2,2,9</sub> |  | 1.2<br><sub>0,-,2,0,3</sub> |  | 0.5<br><sub>0,-,0,0,1</sub> |  | 1.0 | 0.3 | 0.7 | 9.2 |
| Josh Green (UTA) | 72% | 18.4<br><sub>-,-,3,25,24</sub> | 4.0<br><sub>-,-,0,6,2</sub> |  | 2.0<br><sub>-,-,0,4,2</sub> |  | 1.1<br><sub>-,-,1,1,2</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.8 | 0.2 | 0.7 | 7.2 |
| Brice Sensabaugh (UTA) | 98% | 18.2<br><sub>14,16,17,9,18</sub> | 9.8<br><sub>2,10,7,11,16</sub> |  | 2.7<br><sub>2,3,6,2,3</sub> |  | 1.7<br><sub>1,2,1,0,1</sub> |  | 1.3<br><sub>0,2,1,3,4</sub> |  | 0.6 | 0.2 | 1.4 | 14.2 |
| Mo Bamba (UTA) | 52% | 17.1<br><sub>-,-,-,29,16</sub> | 6.0<br><sub>-,-,-,14,8</sub> |  | 6.0<br><sub>-,-,-,7,4</sub> |  | 0.8<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.4 | 1.2 | 0.8 | 12.8 |
| Svi Mykhailiuk (UTA) | 88% | 15.8<br><sub>19,21,14,13,15</sub> | 5.2<br><sub>10,3,2,0,3</sub> |  | 1.8<br><sub>1,4,3,1,2</sub> |  | 1.2<br><sub>2,1,0,0,1</sub> |  | 0.8<br><sub>2,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.6 | 8.3 |
| Kyle Filipowski (UTA) | 58% | 12.6<br><sub>9,8,-,8,-</sub> | 6.2<br><sub>3,0,-,0,-</sub> |  | 4.0<br><sub>0,1,-,1,-</sub> |  | 1.4<br><sub>0,0,-,0,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.6 | 0.3 | 1.0 | 11.6 |
| Tony Bradley (UTA) | 48% | 8.2<br><sub>-,-,-,6,-</sub> | 2.9<br><sub>-,-,-,2,-</sub> |  | 2.6<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 5.9 |

</details>

<details><summary>if Robert Williams III plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija (POR) | 98% | 34.1<br><sub>23,38,33,32</sub> | 27.4<br><sub>18,26,23,24</sub> | 24.5 · – | 7.1<br><sub>10,7,4,9</sub> | 7.5 | 7.3<br><sub>4,6,9,7</sub> | 6.5 | 1.9<br><sub>2,1,4,0</sub> | 1.5 | 0.9 | 0.7 | 4.1 | 41.8 |
| Damian Lillard (POR) | 98% | 32.2<br><sub>24,33,31,30</sub> | 19.1<br><sub>25,19,21,9</sub> | 23.5 · – | 4.2<br><sub>3,5,5,2</sub> | 3.5 | 6.2<br><sub>6,2,4,2</sub> | 5.5 | 2.7<br><sub>6,2,4,1</sub> | 3.5 | 1.1 | 0.3 | 2.4 | 29.6 |
| Jrue Holiday (POR) | 98% | 30.2<br><sub>21,26,30,24</sub> | 15.5<br><sub>8,12,22,6</sub> | 13.5 · – | 4.6<br><sub>4,1,4,6</sub> | 4.5 | 6.2<br><sub>1,8,3,4</sub> | 4.5 | 2.3<br><sub>0,3,2,2</sub> | 2.5 | 1.1 | 0.3 | 2.3 | 26.3 |
| Toumani Camara (POR) | 98% | 29.6<br><sub>23,27,24,26</sub> | 12.9<br><sub>18,19,12,13</sub> | 12.5 · – | 4.5<br><sub>2,3,1,2</sub> | 4.5 | 2.0<br><sub>3,1,1,1</sub> | 1.5 | 2.3<br><sub>4,5,4,3</sub> | 2.5 | 1.1 | 0.5 | 1.4 | 19.5 |
| Donovan Clingan (POR) | 98% | 27.2<br><sub>21,21,26,29</sub> | 12.0<br><sub>11,8,9,11</sub> | 11.5 · – | 10.9<br><sub>7,10,10,8</sub> | 11.5 | 2.2<br><sub>2,3,1,1</sub> | 1.5 | 1.2<br><sub>2,0,2,1</sub> | 1.5 | 0.6 | 2.4 | 1.3 | 25.2 |
| Scoot Henderson (POR) | 98% | 23.8<br><sub>19,21,17,19</sub> | 12.7<br><sub>15,4,2,9</sub> | 14.5 · – | 2.7<br><sub>2,1,2,4</sub> | 3.5 | 3.2<br><sub>1,2,3,0</sub> | 3.5 | 1.6<br><sub>1,0,0,1</sub> | 1.5 | 1.2 | 0.2 | 2.4 | 18.6 |
| Sidy Cissoko (POR) | 96% | 22.4<br><sub>25,26,20,19</sub> | 6.6<br><sub>3,15,6,4</sub> |  | 3.2<br><sub>4,7,2,6</sub> |  | 2.1<br><sub>3,1,4,2</sub> |  | 0.8<br><sub>1,2,0,0</sub> |  | 0.9 | 0.4 | 1.0 | 11.9 |
| Robert Williams III (POR) | 100% | 20.9<br><sub>15,18,21,-</sub> | 8.4<br><sub>2,13,14,-</sub> |  | 8.2<br><sub>10,6,10,-</sub> |  | 1.5<br><sub>1,0,1,-</sub> |  | 0.2<br><sub>0,0,0,-</sub> |  | 0.7 | 1.7 | 1.1 | 18.0 |
| Micah Potter (POR) | 63% | 13.1<br><sub>12,-,-,9</sub> | 5.8<br><sub>4,-,-,1</sub> |  | 3.7<br><sub>3,-,-,2</sub> |  | 0.9<br><sub>0,-,-,0</sub> |  | 0.6<br><sub>0,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 10.3 |
| Vit Krejci (POR) | 96% | 13.0<br><sub>15,3,7,8</sub> | 4.9<br><sub>1,0,4,2</sub> |  | 1.7<br><sub>2,2,0,0</sub> |  | 1.2<br><sub>3,0,0,1</sub> |  | 0.7<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.8 |
| Branden Carlson (POR) | 48% | 12.3<br><sub>-,-,-,12</sub> | 4.5<br><sub>-,-,-,2</sub> |  | 2.6<br><sub>-,-,-,2</sub> |  | 0.8<br><sub>-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,0</sub> |  | 0.5 | 1.3 | 1.6 | 7.9 |
| Yang Hansen (POR) | 58% | 8.1<br><sub>12,-,-,5</sub> | 3.1<br><sub>5,-,-,3</sub> |  | 2.0<br><sub>3,-,-,2</sub> |  | 0.5<br><sub>0,-,-,1</sub> |  | 0.2<br><sub>1,-,-,1</sub> |  | 0.2 | 0.3 | 0.7 | 5.6 |
| Keyonte George (UTA) | 98% | 34.1<br><sub>29,32,33,33,37</sub> | 25.9<br><sub>22,19,24,26,31</sub> | 22.5 · – | 3.8<br><sub>3,1,9,3,4</sub> |  | 7.0<br><sub>5,10,10,6,3</sub> |  | 2.5<br><sub>4,3,2,0,5</sub> | 2.5 | 1.0 | 0.2 | 3.9 | 36.7 |
| Ace Bailey (UTA) | 98% | 34.0<br><sub>24,22,29,34,40</sub> | 16.8<br><sub>12,6,17,17,19</sub> | 15.5 · – | 6.5<br><sub>5,7,12,10,6</sub> |  | 2.9<br><sub>3,2,4,3,0</sub> |  | 2.1<br><sub>2,1,1,3,1</sub> | 1.5 | 1.0 | 1.4 | 2.3 | 26.2 |
| Jaxson Hayes (UTA) | 98% | 30.7<br><sub>26,26,19,-,37</sub> | 10.6<br><sub>5,17,9,-,2</sub> | 8.5 · – | 7.1<br><sub>5,5,5,-,11</sub> |  | 2.2<br><sub>3,2,1,-,4</sub> |  | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.9 | 1.5 | 1.3 | 19.9 |
| Darryn Peterson (UTA) | 96% | 30.7<br><sub>31,30,30,26,26</sub> | 15.0<br><sub>9,15,8,14,18</sub> | 14.5 · – | 4.7<br><sub>4,3,3,7,5</sub> |  | 3.4<br><sub>3,1,2,4,3</sub> |  | 1.2<br><sub>0,1,0,3,3</sub> | 1.5 | 1.1 | 0.4 | 1.7 | 23.1 |
| Isaiah Collier (UTA) | 96% | 24.7<br><sub>16,18,13,21,24</sub> | 12.7<br><sub>7,10,6,7,7</sub> |  | 3.3<br><sub>3,2,3,8,7</sub> |  | 7.2<br><sub>3,7,6,8,6</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.3 | 2.7 | 23.2 |
| Josh Okogie (UTA) | 86% | 23.5<br><sub>8,-,10,21,28</sub> | 5.3<br><sub>0,-,2,0,5</sub> |  | 4.0<br><sub>1,-,2,2,9</sub> |  | 1.4<br><sub>0,-,2,0,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 1.1 | 0.4 | 0.8 | 10.7 |
| Josh Green (UTA) | 72% | 21.4<br><sub>-,-,3,25,24</sub> | 4.7<br><sub>-,-,0,6,2</sub> |  | 2.2<br><sub>-,-,0,4,2</sub> |  | 1.3<br><sub>-,-,1,1,2</sub> |  | 0.6<br><sub>-,-,0,1,0</sub> |  | 0.9 | 0.2 | 0.8 | 8.2 |
| Brice Sensabaugh (UTA) | 98% | 20.7<br><sub>14,16,17,9,18</sub> | 12.1<br><sub>2,10,7,11,16</sub> |  | 3.1<br><sub>2,3,6,2,3</sub> |  | 1.9<br><sub>1,2,1,0,1</sub> |  | 1.6<br><sub>0,2,1,3,4</sub> |  | 0.6 | 0.2 | 1.7 | 17.1 |
| Mo Bamba (UTA) | 52% | 19.4<br><sub>-,-,-,29,16</sub> | 6.9<br><sub>-,-,-,14,8</sub> |  | 6.8<br><sub>-,-,-,7,4</sub> |  | 0.9<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.4 | 1.0 | 14.6 |
| Svi Mykhailiuk (UTA) | 88% | 18.7<br><sub>19,21,14,13,15</sub> | 7.0<br><sub>10,3,2,0,3</sub> |  | 2.2<br><sub>1,4,3,1,2</sub> |  | 1.4<br><sub>2,1,0,0,1</sub> |  | 1.0<br><sub>2,0,0,0,1</sub> |  | 0.6 | 0.1 | 0.8 | 10.6 |
| Kyle Filipowski (UTA) | 58% | 14.8<br><sub>9,8,-,8,-</sub> | 7.9<br><sub>3,0,-,0,-</sub> |  | 4.7<br><sub>0,1,-,1,-</sub> |  | 1.8<br><sub>0,0,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.7 | 0.3 | 1.2 | 14.4 |
| Tony Bradley (UTA) | 48% | 9.7<br><sub>-,-,-,6,-</sub> | 3.5<br><sub>-,-,-,2,-</sub> |  | 3.0<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.6 | 7.1 |

</details>


### PHI @ CHA
Out: Kon Knueppel (CHA), Coby White (CHA), Grant Williams (CHA), Dominick Barlow (PHI), Ariel Hukporti (PHI)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Dennis Schroder AST under 5.5 | PHI @ CHA | draftkings | 2.08 | 2.06 | 1.68 | 59.5% | 44.9% | 48.6% | +1.1% | +23.8% | 0.2% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 107.1–110.0 | PHI 42% | 2.37 / 1.73 | CHA -3.5 | 216.5 | CHA +1.5 covers 61%; o214.5 55% |
| Expected (weighted by chance each plays) | 108.3–111.3 | PHI 42% | 2.38 / 1.72 | CHA -3.5 | 219.5 | CHA +1.5 covers 61%; o214.5 61% |
| if Jaylen Brown plays | 108.7–111.8 | PHI 42% | 2.40 / 1.71 | CHA -3.5 | 220.5 | CHA +1.5 covers 61%; o214.5 62% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaylen Brown (PHI) | Day-To-Day | 70% | 36.0 | 21.9 | 6.3 | 4.2 | 1.8 | 1.2 | 0.5 | 3.2 | 32.3 | full tables below |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.4<br><sub>40,42,36,34,36</sub> | 26.1<br><sub>28,32,26,29,27</sub> | 29.5 · – | 3.9<br><sub>4,3,4,5,5</sub> |  | 5.5<br><sub>5,6,4,4,4</sub> |  | 2.6<br><sub>2,2,4,1,3</sub> | 3.5 | 1.6 | 0.6 | 2.5 | 35.5 |
| Joel Embiid | 98% | 35.8<br><sub>33,34,36,-,39</sub> | 25.9<br><sub>13,24,28,-,21</sub> |  | 8.2<br><sub>11,7,11,-,11</sub> |  | 4.9<br><sub>6,1,10,-,2</sub> |  | 1.4<br><sub>2,1,0,-,0</sub> |  | 0.8 | 1.2 | 3.2 | 39.0 |
| LeBron James | 98% | 35.2<br><sub>34,33,-,33,33</sub> | 19.2<br><sub>14,17,-,18,13</sub> |  | 6.2<br><sub>9,10,-,2,5</sub> |  | 6.5<br><sub>7,5,-,5,10</sub> |  | 1.4<br><sub>0,1,-,0,2</sub> |  | 1.4 | 0.6 | 3.0 | 31.9 |
| VJ Edgecombe | 76% | 34.5<br><sub>35,33,30,-,29</sub> | 13.4<br><sub>9,11,17,-,8</sub> | 16.5 · – | 6.0<br><sub>4,7,13,-,7</sub> |  | 3.5<br><sub>1,6,2,-,2</sub> |  | 1.8<br><sub>0,1,5,-,1</sub> | 1.5 | 1.4 | 0.5 | 1.6 | 22.9 |
| Anfernee Simons | 96% | 26.5<br><sub>25,17,20,27,27</sub> | 10.8<br><sub>13,2,4,5,20</sub> |  | 2.6<br><sub>2,3,1,3,3</sub> |  | 1.9<br><sub>0,0,2,3,1</sub> |  | 1.9<br><sub>3,0,1,1,6</sub> |  | 0.7 | 0.2 | 1.0 | 15.2 |
| Kentavious Caldwell-Pope | 98% | 26.1<br><sub>26,25,28,31,21</sub> | 7.5<br><sub>10,3,12,7,4</sub> |  | 2.7<br><sub>4,3,2,3,2</sub> |  | 1.8<br><sub>1,2,1,3,1</sub> |  | 1.1<br><sub>2,1,4,1,0</sub> |  | 1.1 | 0.2 | 0.8 | 12.0 |
| Dean Wade | 86% | 24.7<br><sub>-,-,28,37,17</sub> | 4.4<br><sub>-,-,7,7,0</sub> |  | 3.3<br><sub>-,-,2,5,1</sub> |  | 1.0<br><sub>-,-,0,1,1</sub> |  | 0.7<br><sub>-,-,2,1,0</sub> |  | 0.9 | 0.3 | 0.6 | 8.7 |
| Rayan Rupert | 30% | 13.2<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.1 | 0.8 | 7.7 |
| Adem Bona | 96% | 12.7<br><sub>10,14,10,25,4</sub> | 3.3<br><sub>0,2,0,6,1</sub> |  | 3.1<br><sub>3,2,1,13,1</sub> |  | 0.4<br><sub>1,0,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 6.8 |
| Labaron Philon Jr. | 52% | 9.9<br><sub>-,-,4,13,-</sub> | 3.3<br><sub>-,-,0,5,-</sub> |  | 1.2<br><sub>-,-,0,2,-</sub> |  | 0.7<br><sub>-,-,0,1,-</sub> |  | 0.2<br><sub>-,-,0,1,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.2 |
| Justin Edwards | 38% | 9.3<br><sub>-,-,1,-,-</sub> | 3.4<br><sub>-,-,0,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.5 | 0.1 | 0.4 | 5.1 |
| Caleb Love | 43% | 7.4<br><sub>-,-,1,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.2 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 32.4<br><sub>36,23,36,36,38</sub> | 24.0<br><sub>18,6,34,39,31</sub> | 27.5 · – | 5.6<br><sub>3,2,8,6,12</sub> | 5.5 | 2.9<br><sub>1,0,4,1,3</sub> | 2.5 | 3.0<br><sub>3,1,3,5,3</sub> | 3.5 | 1.1 | 0.7 | 3.0 | 32.5 |
| Dennis Schroder | 98% | 31.5<br><sub>35,20,38,36,34</sub> | 14.3<br><sub>19,4,25,8,14</sub> | 14.5 · – | 3.6<br><sub>4,4,6,2,4</sub> | 3.5 | 5.1<br><sub>6,3,4,5,5</sub> | 5.5 | 1.2<br><sub>0,0,3,0,2</sub> | 1.5 | 1.0 | 0.3 | 2.8 | 23.1 |
| Moussa Diabate | 98% | 28.8<br><sub>34,21,22,35,35</sub> | 9.2<br><sub>17,5,4,11,9</sub> |  | 9.8<br><sub>8,8,5,17,9</sub> |  | 2.4<br><sub>3,1,2,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.1 | 1.5 | 21.4 |
| Grayson Allen | 96% | 28.5<br><sub>29,20,34,28,30</sub> | 15.9<br><sub>21,11,20,15,9</sub> |  | 3.4<br><sub>3,2,3,2,5</sub> |  | 3.1<br><sub>4,3,5,1,2</sub> |  | 2.5<br><sub>5,3,4,2,2</sub> |  | 1.0 | 0.4 | 2.0 | 22.4 |
| Naz Reid | 98% | 24.8<br><sub>33,25,37,29,13</sub> | 15.2<br><sub>20,17,23,18,7</sub> | 17.5 · – | 6.9<br><sub>11,6,9,12,6</sub> | 8.5 | 2.0<br><sub>7,2,0,1,0</sub> | 2.5 | 1.9<br><sub>4,3,5,2,1</sub> | 2.5 | 0.6 | 0.8 | 2.0 | 24.1 |
| Sion James | 98% | 23.4<br><sub>27,24,26,29,23</sub> | 6.1<br><sub>3,3,0,5,5</sub> |  | 3.5<br><sub>3,2,5,2,2</sub> |  | 2.5<br><sub>0,5,5,3,3</sub> |  | 0.9<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.2 | 0.9 | 12.1 |
| Royce O'Neale | 98% | 20.2<br><sub>17,17,11,7,34</sub> | 6.2<br><sub>8,6,0,0,9</sub> |  | 3.5<br><sub>4,2,1,0,4</sub> |  | 1.2<br><sub>0,0,0,1,0</sub> |  | 1.1<br><sub>2,2,0,0,3</sub> |  | 0.7 | 0.3 | 0.7 | 10.9 |
| Ryan Kalkbrenner | 98% | 16.3<br><sub>14,19,23,13,13</sub> | 5.4<br><sub>4,6,6,6,1</sub> |  | 4.4<br><sub>5,7,5,4,1</sub> |  | 0.9<br><sub>3,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.8 | 10.7 |
| Tidjane Salaun | 86% | 14.6<br><sub>-,23,10,16,12</sub> | 5.4<br><sub>-,11,3,5,2</sub> |  | 3.5<br><sub>-,5,3,5,2</sub> |  | 0.8<br><sub>-,1,0,0,0</sub> |  | 0.6<br><sub>-,1,1,1,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.7 |
| Christian Anderson | 96% | 10.2<br><sub>13,16,3,11,9</sub> | 4.3<br><sub>0,2,0,3,2</sub> |  | 1.3<br><sub>2,0,1,4,0</sub> |  | 1.1<br><sub>2,2,0,1,1</sub> |  | 0.4<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.1 | 0.9 | 6.7 |
| PJ Hall | 38% | 8.6<br><sub>-,10,-,-,-</sub> | 3.2<br><sub>-,0,-,-,-</sub> |  | 3.0<br><sub>-,1,-,-,-</sub> |  | 0.6<br><sub>-,3,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.5 | 0.6 | 6.8 |
| Liam McNeeley | 48% | 8.6<br><sub>3,12,-,-,-</sub> | 3.2<br><sub>0,4,-,-,-</sub> |  | 1.8<br><sub>1,4,-,-,-</sub> |  | 0.5<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.5 |
| Hannes Steinbach | 36% | 8.3<br><sub>-,12,-,-,-</sub> | 3.2<br><sub>-,6,-,-,-</sub> |  | 2.4<br><sub>-,5,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 5.9 |

</details>

<details><summary>if Jaylen Brown plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller (CHA) | 98% | 32.4<br><sub>36,23,36,36,38</sub> | 24.3<br><sub>18,6,34,39,31</sub> | 27.5 · – | 5.7<br><sub>3,2,8,6,12</sub> | 5.5 | 2.9<br><sub>1,0,4,1,3</sub> | 2.5 | 3.0<br><sub>3,1,3,5,3</sub> | 3.5 | 1.1 | 0.7 | 3.0 | 32.8 |
| Dennis Schroder (CHA) | 98% | 31.5<br><sub>35,20,38,36,34</sub> | 14.3<br><sub>19,4,25,8,14</sub> | 14.5 · – | 3.7<br><sub>4,4,6,2,4</sub> | 3.5 | 5.2<br><sub>6,3,4,5,5</sub> | 5.5 | 1.2<br><sub>0,0,3,0,2</sub> | 1.5 | 1.0 | 0.3 | 2.7 | 23.1 |
| Moussa Diabate (CHA) | 98% | 28.9<br><sub>34,21,22,35,35</sub> | 9.2<br><sub>17,5,4,11,9</sub> |  | 9.9<br><sub>8,8,5,17,9</sub> |  | 2.4<br><sub>3,1,2,3,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.1 | 1.5 | 21.5 |
| Grayson Allen (CHA) | 96% | 28.4<br><sub>29,20,34,28,30</sub> | 16.1<br><sub>21,11,20,15,9</sub> |  | 3.4<br><sub>3,2,3,2,5</sub> |  | 3.1<br><sub>4,3,5,1,2</sub> |  | 2.5<br><sub>5,3,4,2,2</sub> |  | 1.0 | 0.3 | 2.0 | 22.6 |
| Naz Reid (CHA) | 98% | 24.7<br><sub>33,25,37,29,13</sub> | 15.4<br><sub>20,17,23,18,7</sub> | 17.5 · – | 6.9<br><sub>11,6,9,12,6</sub> | 8.5 | 2.0<br><sub>7,2,0,1,0</sub> | 2.5 | 1.9<br><sub>4,3,5,2,1</sub> | 2.5 | 0.7 | 0.8 | 1.9 | 24.2 |
| Sion James (CHA) | 98% | 23.4<br><sub>27,24,26,29,23</sub> | 6.1<br><sub>3,3,0,5,5</sub> |  | 3.5<br><sub>3,2,5,2,2</sub> |  | 2.5<br><sub>0,5,5,3,3</sub> |  | 0.9<br><sub>1,1,0,1,1</sub> |  | 0.7 | 0.2 | 0.9 | 12.1 |
| Royce O'Neale (CHA) | 98% | 20.3<br><sub>17,17,11,7,34</sub> | 6.3<br><sub>8,6,0,0,9</sub> |  | 3.5<br><sub>4,2,1,0,4</sub> |  | 1.2<br><sub>0,0,0,1,0</sub> |  | 1.2<br><sub>2,2,0,0,3</sub> |  | 0.7 | 0.4 | 0.7 | 11.0 |
| Ryan Kalkbrenner (CHA) | 98% | 16.2<br><sub>14,19,23,13,13</sub> | 5.5<br><sub>4,6,6,6,1</sub> |  | 4.3<br><sub>5,7,5,4,1</sub> |  | 0.9<br><sub>3,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.8 | 10.7 |
| Tidjane Salaun (CHA) | 86% | 14.7<br><sub>-,23,10,16,12</sub> | 5.5<br><sub>-,11,3,5,2</sub> |  | 3.6<br><sub>-,5,3,5,2</sub> |  | 0.8<br><sub>-,1,0,0,0</sub> |  | 0.6<br><sub>-,1,1,1,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.8 |
| Christian Anderson (CHA) | 96% | 10.1<br><sub>13,16,3,11,9</sub> | 4.3<br><sub>0,2,0,3,2</sub> |  | 1.3<br><sub>2,0,1,4,0</sub> |  | 1.1<br><sub>2,2,0,1,1</sub> |  | 0.4<br><sub>0,0,0,1,0</sub> |  | 0.4 | 0.1 | 0.9 | 6.7 |
| PJ Hall (CHA) | 38% | 8.7<br><sub>-,10,-,-,-</sub> | 3.4<br><sub>-,0,-,-,-</sub> |  | 3.0<br><sub>-,1,-,-,-</sub> |  | 0.6<br><sub>-,3,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.5 | 0.6 | 6.9 |
| Liam McNeeley (CHA) | 48% | 8.5<br><sub>3,12,-,-,-</sub> | 3.2<br><sub>0,4,-,-,-</sub> |  | 1.8<br><sub>1,4,-,-,-</sub> |  | 0.5<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.6 |
| Hannes Steinbach (CHA) | 36% | 8.4<br><sub>-,12,-,-,-</sub> | 3.2<br><sub>-,6,-,-,-</sub> |  | 2.4<br><sub>-,5,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Tyrese Maxey (PHI) | 98% | 36.9<br><sub>40,42,36,34,36</sub> | 22.2<br><sub>28,32,26,29,27</sub> | 29.5 · – | 3.8<br><sub>4,3,4,5,5</sub> |  | 5.1<br><sub>5,6,4,4,4</sub> |  | 2.3<br><sub>2,2,4,1,3</sub> | 3.5 | 1.6 | 0.6 | 2.2 | 31.1 |
| Jaylen Brown (PHI) | 100% | 36.0<br><sub>35,38,35,40,34</sub> | 21.9<br><sub>19,21,27,16,20</sub> |  | 6.3<br><sub>8,8,3,4,10</sub> |  | 4.2<br><sub>6,4,5,4,2</sub> |  | 1.8<br><sub>2,1,3,2,1</sub> |  | 1.2 | 0.5 | 3.2 | 32.3 |
| Joel Embiid (PHI) | 98% | 35.3<br><sub>33,34,36,-,39</sub> | 23.5<br><sub>13,24,28,-,21</sub> |  | 8.2<br><sub>11,7,11,-,11</sub> |  | 4.6<br><sub>6,1,10,-,2</sub> |  | 1.3<br><sub>2,1,0,-,0</sub> |  | 0.8 | 1.2 | 2.9 | 36.4 |
| LeBron James (PHI) | 98% | 34.1<br><sub>34,33,-,33,33</sub> | 17.1<br><sub>14,17,-,18,13</sub> |  | 6.2<br><sub>9,10,-,2,5</sub> |  | 6.3<br><sub>7,5,-,5,10</sub> |  | 1.3<br><sub>0,1,-,0,2</sub> |  | 1.4 | 0.6 | 2.7 | 29.5 |
| VJ Edgecombe (PHI) | 76% | 32.2<br><sub>35,33,30,-,29</sub> | 11.3<br><sub>9,11,17,-,8</sub> | 16.5 · – | 5.6<br><sub>4,7,13,-,7</sub> |  | 3.2<br><sub>1,6,2,-,2</sub> |  | 1.5<br><sub>0,1,5,-,1</sub> | 1.5 | 1.2 | 0.4 | 1.4 | 20.1 |
| Anfernee Simons (PHI) | 96% | 21.8<br><sub>25,17,20,27,27</sub> | 8.4<br><sub>13,2,4,5,20</sub> |  | 2.1<br><sub>2,3,1,3,3</sub> |  | 1.5<br><sub>0,0,2,3,1</sub> |  | 1.4<br><sub>3,0,1,1,6</sub> |  | 0.5 | 0.2 | 0.9 | 12.0 |
| Kentavious Caldwell-Pope (PHI) | 98% | 21.0<br><sub>26,25,28,31,21</sub> | 5.7<br><sub>10,3,12,7,4</sub> |  | 2.1<br><sub>4,3,2,3,2</sub> |  | 1.3<br><sub>1,2,1,3,1</sub> |  | 0.7<br><sub>2,1,4,1,0</sub> |  | 0.9 | 0.2 | 0.6 | 9.1 |
| Dean Wade (PHI) | 86% | 19.8<br><sub>-,-,28,37,17</sub> | 3.5<br><sub>-,-,7,7,0</sub> |  | 2.7<br><sub>-,-,2,5,1</sub> |  | 0.8<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,2,1,0</sub> |  | 0.7 | 0.2 | 0.5 | 6.9 |
| Adem Bona (PHI) | 96% | 8.1<br><sub>10,14,10,25,4</sub> | 2.1<br><sub>0,2,0,6,1</sub> |  | 2.0<br><sub>3,2,1,13,1</sub> |  | 0.2<br><sub>1,0,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 4.3 |
| Rayan Rupert (PHI) | 30% | 7.7<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.4 |
| Justin Edwards (PHI) | 38% | 6.6<br><sub>-,-,1,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.8 |
| Caleb Love (PHI) | 43% | 6.4<br><sub>-,-,1,-,-</sub> | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.2 | 1.0 |
| Labaron Philon Jr. (PHI) | 52% | 6.1<br><sub>-,-,4,13,-</sub> | 2.2<br><sub>-,-,0,5,-</sub> |  | 0.8<br><sub>-,-,0,2,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.1<br><sub>-,-,0,1,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.4 |

</details>


### ATL @ NOP
Out: Yves Missi (NOP), Jordan Poole (NOP), Mouhamed Gueye (ATL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jeremiah Fears AST over 3.5 (4+) | ATL @ NOP | draftkings | 2.26 | 2.25 | 1.86 | 53.7% | 41.4% | 44.5% | +0.6% | +21.4% | 0.1% |
| Zion Williamson PTS under 22.5 | ATL @ NOP | draftkings | 1.94 | 1.93 | 1.60 | 62.5% | 48.1% | 51.7% | +0.4% | +21.4% | 0.1% |
| Jalen Johnson PRA under 41.5 | ATL @ NOP | draftkings | 1.92 | 1.91 | 1.58 | 63.2% | 48.7% | 52.4% | +0.4% | +21.2% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 123.8–120.7 | ATL 59% | 1.69 / 2.44 | NOP +3.5 | 244.5 | NOP +4.5 covers 53%; o241.5 56% |
| Expected (weighted by chance each plays) | 124.2–120.7 | ATL 60% | 1.67 / 2.50 | NOP +3.5 | 244.5 | NOP +4.5 covers 53%; o241.5 57% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 9.9 | 3.9 | 1.6 | 0.7 | 0.3 | 0.3 | 0.1 | 0.5 | 6.2 | small |
| RayJ Dennis (ATL) | Doubtful | 20% | 7.8 | 2.9 | 1.1 | 1.2 | 0.3 | 0.3 | 0.1 | 0.5 | 5.2 | small |
| Keshon Gilbert (ATL) | Doubtful | 20% | 7.8 | 2.5 | 0.9 | 1.1 | 0.1 | 0.3 | 0.2 | 0.6 | 4.5 | small |
| Zuby Ejiofor (ATL) | Doubtful | 20% | 5.9 | 2.4 | 1.0 | 0.5 | 0.1 | 0.2 | 0.1 | 0.3 | 3.8 | small |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 35.4<br><sub>29,38,36,36,34</sub> | 21.7<br><sub>19,26,21,12,17</sub> | 22.5 · – | 9.6<br><sub>7,9,9,9,8</sub> | 10.5 | 7.5<br><sub>8,16,3,11,7</sub> | 8.5 | 1.8<br><sub>0,2,1,2,2</sub> | 1.5 | 1.3 | 0.6 | 3.2 | 38.9 |
| Nickeil Alexander-Walker | 98% | 32.7<br><sub>27,32,29,32,31</sub> | 19.9<br><sub>14,18,12,23,25</sub> | 19.5 · – | 3.2<br><sub>3,5,2,3,3</sub> | 3.5 | 3.4<br><sub>5,4,3,1,1</sub> | 3.5 | 3.3<br><sub>2,4,2,5,4</sub> | 3.5 | 1.2 | 0.5 | 2.2 | 26.5 |
| Dyson Daniels | 98% | 31.5<br><sub>23,29,28,28,32</sub> | 12.0<br><sub>11,18,4,7,4</sub> | 11.5 · – | 6.3<br><sub>9,8,0,4,6</sub> | 5.5 | 5.5<br><sub>4,3,4,7,5</sub> | 4.5 | 0.5<br><sub>0,1,0,0,0</sub> |  | 2.2 | 0.4 | 1.6 | 23.7 |
| Onyeka Okongwu | 98% | 31.4<br><sub>22,26,29,31,33</sub> | 14.7<br><sub>10,8,11,11,29</sub> | 13.5 · – | 7.5<br><sub>4,6,9,4,12</sub> | 7.5 | 2.9<br><sub>1,2,1,4,2</sub> | 2.5 | 1.7<br><sub>2,0,1,1,4</sub> | 1.5 | 1.1 | 1.0 | 1.4 | 25.0 |
| CJ McCollum | 98% | 29.3<br><sub>22,30,30,20,31</sub> | 18.2<br><sub>13,17,20,13,5</sub> | 16.5 · – | 2.8<br><sub>1,2,1,2,3</sub> | 2.5 | 3.6<br><sub>2,1,3,1,8</sub> | 3.5 | 2.5<br><sub>2,1,4,1,0</sub> | 2.5 | 1.0 | 0.5 | 1.9 | 24.7 |
| Aaron Wiggins | 96% | 24.8<br><sub>22,29,27,24,24</sub> | 11.6<br><sub>19,16,12,10,20</sub> | 12.5 · – | 3.4<br><sub>1,5,4,4,7</sub> | 3.5 | 2.0<br><sub>1,2,3,3,3</sub> |  | 1.8<br><sub>3,4,2,2,4</sub> | 2.5 | 0.9 | 0.4 | 1.1 | 17.0 |
| Luguentz Dort | 98% | 22.3<br><sub>19,23,21,24,22</sub> | 7.9<br><sub>9,7,11,8,6</sub> | 7.5 · – | 2.8<br><sub>5,2,2,3,3</sub> | 2.5 | 1.5<br><sub>2,3,1,3,2</sub> |  | 1.3<br><sub>1,1,0,2,1</sub> | 1.5 | 0.8 | 0.3 | 0.7 | 12.1 |
| Kingston Flemings | 96% | 18.4<br><sub>25,15,18,28,16</sub> | 6.6<br><sub>5,2,6,23,2</sub> | 7.5 · – | 2.6<br><sub>6,1,1,5,1</sub> | 2.5 | 3.9<br><sub>8,2,4,5,5</sub> | 2.5 | 0.5<br><sub>1,0,0,3,0</sub> |  | 0.7 | 0.3 | 1.3 | 13.1 |
| Jock Landale | 98% | 16.8<br><sub>18,19,18,17,15</sub> | 7.7<br><sub>8,2,8,10,6</sub> |  | 4.5<br><sub>6,4,6,6,10</sub> |  | 1.6<br><sub>4,2,4,0,1</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.4 | 0.5 | 0.8 | 13.8 |
| Corey Kispert | 48% | 9.2<br><sub>10,-,1,-,-</sub> | 4.7<br><sub>11,-,5,-,-</sub> |  | 1.3<br><sub>1,-,0,-,-</sub> |  | 0.8<br><sub>1,-,0,-,-</sub> |  | 0.5<br><sub>3,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 6.8 |
| Asa Newell | 47% | 8.1<br><sub>8,-,1,-,-</sub> | 3.5<br><sub>3,-,0,-,-</sub> |  | 1.6<br><sub>1,-,1,-,-</sub> |  | 0.5<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.6 |
| Dorian Finney-Smith | 48% | 7.2<br><sub>8,-,1,-,-</sub> | 2.4<br><sub>3,-,0,-,-</sub> |  | 1.2<br><sub>2,-,0,-,-</sub> |  | 0.5<br><sub>1,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 34.2<br><sub>32,31,37,30,32</sub> | 17.6<br><sub>11,9,26,6,19</sub> | 16.5 · – | 5.5<br><sub>4,6,6,1,5</sub> | 4.5 | 3.3<br><sub>1,3,4,3,3</sub> | 2.5 | 2.7<br><sub>2,1,4,2,2</sub> | 2.5 | 1.3 | 0.5 | 1.6 | 26.5 |
| Dejounte Murray | 98% | 32.5<br><sub>34,30,35,30,-</sub> | 17.8<br><sub>23,16,22,10,-</sub> | 16.5 · – | 6.1<br><sub>3,6,6,8,-</sub> | 5.5 | 6.8<br><sub>7,6,6,5,-</sub> | 5.5 | 1.6<br><sub>2,0,1,0,-</sub> | 1.5 | 1.8 | 0.4 | 3.4 | 30.6 |
| Zion Williamson | 96% | 32.1<br><sub>32,33,33,32,31</sub> | 20.9<br><sub>22,23,17,25,22</sub> | 22.5 · – | 6.2<br><sub>3,5,1,5,6</sub> | 5.5 | 3.0<br><sub>3,2,2,2,2</sub> | 2.5 | 0.2<br><sub>2,0,0,1,0</sub> |  | 1.3 | 0.8 | 2.3 | 30.1 |
| Jeremiah Fears | 98% | 26.8<br><sub>21,24,23,24,29</sub> | 14.9<br><sub>8,7,10,11,22</sub> | 13.5 · – | 4.0<br><sub>3,0,6,4,8</sub> | 3.5 | 3.9<br><sub>1,1,2,3,13</sub> | 3.5 | 1.4<br><sub>1,1,0,1,3</sub> | 1.5 | 1.2 | 0.6 | 2.5 | 22.8 |
| Saddiq Bey | 96% | 26.5<br><sub>24,22,25,26,24</sub> | 13.8<br><sub>13,20,14,9,10</sub> | 12.5 · – | 4.6<br><sub>5,3,4,0,4</sub> | 4.5 | 2.0<br><sub>0,1,3,3,3</sub> | 1.5 | 1.7<br><sub>2,3,2,1,1</sub> | 1.5 | 0.8 | 0.2 | 1.0 | 20.5 |
| Derik Queen | 98% | 23.8<br><sub>18,29,25,25,22</sub> | 11.1<br><sub>10,12,17,11,9</sub> | 11.5 · – | 7.3<br><sub>10,7,8,12,2</sub> | 7.5 | 2.6<br><sub>1,2,2,1,3</sub> | 2.5 | 0.4<br><sub>0,1,0,0,1</sub> |  | 1.0 | 1.0 | 2.1 | 20.9 |
| Herbert Jones | 96% | 23.6<br><sub>17,18,16,19,32</sub> | 7.5<br><sub>5,3,2,4,16</sub> | 5.5 · – | 2.8<br><sub>2,1,3,2,4</sub> | 2.5 | 2.0<br><sub>0,0,1,0,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 1.3 | 0.5 | 1.2 | 12.2 |
| Bennedict Mathurin | 98% | 18.3<br><sub>18,15,20,14,19</sub> | 9.2<br><sub>11,4,9,5,10</sub> |  | 3.5<br><sub>3,2,4,1,3</sub> |  | 1.6<br><sub>2,0,4,2,2</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.6 | 0.2 | 1.3 | 14.2 |
| Karlo Matkovic | 88% | 17.9<br><sub>-,9,8,18,28</sub> | 6.6<br><sub>-,7,3,5,12</sub> | 7.5 · – | 4.5<br><sub>-,4,0,3,4</sub> | 4.5 | 1.0<br><sub>-,1,0,1,1</sub> |  | 0.6<br><sub>-,0,1,1,1</sub> |  | 0.6 | 1.1 | 0.9 | 12.0 |
| Trendon Watford | 48% | 13.7<br><sub>-,-,-,-,17</sub> | 5.5<br><sub>-,-,-,-,8</sub> |  | 2.6<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,2</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 9.7 |
| DeAndre Jordan | 52% | 12.8<br><sub>-,-,20,13,-</sub> | 3.5<br><sub>-,-,9,3,-</sub> |  | 5.1<br><sub>-,-,9,4,-</sub> |  | 0.8<br><sub>-,-,2,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.7 | 0.7 | 9.4 |
| AJ Johnson | 5% | 12.6<br><sub>-,-,-,-,-</sub> | 5.3<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.6 | 8.7 |
| Bryce McGowens | 58% | 8.8<br><sub>-,-,-,3,6</sub> | 3.1<br><sub>-,-,-,0,4</sub> |  | 1.1<br><sub>-,-,-,0,1</sub> |  | 0.6<br><sub>-,-,-,0,2</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.8 |
| Malik Dia | 19% | 8.6 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.5 | 5.8 |
| Jaron Pierre Jr. | 22% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Julian Reese | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |

</details>


### SAC @ MEM
Out: Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. REB over 3.5 (4+) | SAC @ MEM | draftkings | 1.93 | 1.91 | 1.58 | 63.3% | 48.5% | 52.2% | +1.0% | +22.5% | 0.3% |
| Precious Achiuwa RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.96 | 1.96 | 1.63 | 61.4% | 47.7% | 51.1% | +0.3% | +20.5% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.4–122.8 | SAC 30% | 3.32 / 1.43 | MEM -7.5 | 238.5 | MEM -11.5 covers 39%; o233.5 60% |
| Expected (weighted by chance each plays) | 114.8–123.1 | SAC 28% | 3.53 / 1.39 | MEM -8.5 | 237.5 | MEM -11.5 covers 41%; o233.5 60% |
| if Ty Jerome plays | 114.9–123.6 | SAC 27% | 3.68 / 1.37 | MEM -8.5 | 238.5 | MEM -11.5 covers 42%; o233.5 60% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quinten Post (MEM) | Doubtful | 20% | 14.0 | 5.6 | 2.9 | 0.7 | 0.5 | 0.5 | 0.4 | 0.7 | 9.3 | small |
| Ty Jerome (MEM) | Questionable | 55% | 29.0 | 22.1 | 3.5 | 6.4 | 2.6 | 1.3 | 0.3 | 2.4 | 32.0 | full tables below |
| Scotty Pippen Jr. (MEM) | Questionable | 55% | 18.3 | 9.5 | 2.5 | 3.4 | 0.8 | 1.2 | 0.3 | 1.7 | 15.4 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 96% | 36.4<br><sub>35,37,36,33,41</sub> | 23.1<br><sub>12,33,22,19,34</sub> | 22.5 · – | 4.5<br><sub>3,2,3,3,6</sub> | 3.5 | 6.5<br><sub>3,4,7,5,14</sub> | 5.5 | 2.7<br><sub>0,2,2,3,3</sub> | 2.5 | 1.2 | 0.4 | 3.5 | 34.1 |
| Zach LaVine | 98% | 34.1<br><sub>34,39,40,31,39</sub> | 21.3<br><sub>28,22,37,22,21</sub> | 20.5 · – | 3.8<br><sub>4,5,2,3,3</sub> | 2.5 | 3.0<br><sub>4,1,5,3,5</sub> | 2.5 | 2.5<br><sub>3,3,3,3,3</sub> | 2.5 | 0.9 | 0.3 | 2.6 | 28.1 |
| Domantas Sabonis | 98% | 34.0<br><sub>34,39,35,37,40</sub> | 18.3<br><sub>14,27,15,20,9</sub> | 16.5 · – | 14.0<br><sub>18,19,15,14,15</sub> | 13.5 | 6.0<br><sub>8,10,3,8,7</sub> | 6.5 | 0.2<br><sub>0,1,0,0,0</sub> | 0.5 | 0.9 | 0.4 | 3.1 | 38.4 |
| Precious Achiuwa | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.8<br><sub>15,14,12,4,24</sub> | 12.5 · – | 8.9<br><sub>5,6,10,1,9</sub> | 7.5 | 1.9<br><sub>2,1,0,0,2</sub> | 1.5 | 0.3<br><sub>1,0,0,0,0</sub> | 0.5 | 1.5 | 1.1 | 1.7 | 26.6 |
| De'Andre Hunter | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.1<br><sub>6,4,7,24,24</sub> | 12.5 · – | 5.5<br><sub>3,7,6,6,5</sub> | 4.5 | 1.7<br><sub>1,1,1,2,1</sub> | 1.5 | 1.6<br><sub>2,0,2,5,4</sub> | 1.5 | 0.8 | 0.2 | 1.8 | 20.4 |
| Emanuel Sharp | 96% | 15.6<br><sub>17,14,14,20,18</sub> | 4.9<br><sub>8,5,3,5,0</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.6<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.6 |
| Daeqwon Plowden | 71% | 15.3<br><sub>13,20,16,17,-</sub> | 5.0<br><sub>4,3,3,0,-</sub> |  | 1.9<br><sub>2,0,3,2,-</sub> |  | 0.7<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,1,1,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.6 |
| Malik Monk | 96% | 14.3<br><sub>-,12,12,13,8</sub> | 7.3<br><sub>-,0,6,3,2</sub> |  | 1.6<br><sub>-,1,1,2,1</sub> |  | 2.5<br><sub>-,2,2,6,1</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 1.1 | 11.4 |
| Jonathan Mogbo | 52% | 12.2<br><sub>8,-,18,18,-</sub> | 4.4<br><sub>0,-,7,2,-</sub> |  | 2.4<br><sub>0,-,3,5,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.7 | 7.5 |
| Alex Karaban | 64% | 11.4<br><sub>5,-,-,11,12</sub> | 3.6<br><sub>1,-,-,0,6</sub> |  | 2.2<br><sub>1,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.2<br><sub>0,-,-,0,2</sub> |  | 0.4 | 0.3 | 0.8 | 6.6 |
| Nique Clifford | 83% | 10.3<br><sub>17,2,-,5,4</sub> | 4.1<br><sub>6,0,-,2,0</sub> |  | 1.6<br><sub>1,0,-,0,0</sub> |  | 1.1<br><sub>3,0,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.8 |
| Leaky Black | 48% | 9.5<br><sub>-,-,-,8,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 96% | 33.4<br><sub>33,37,31,31,28</sub> | 18.6<br><sub>7,25,14,13,18</sub> | 17.5 · – | 10.3<br><sub>11,13,11,7,12</sub> | 8.5 | 6.7<br><sub>5,6,4,4,12</sub> | 5.5 | 2.1<br><sub>0,4,2,1,4</sub> | 1.5 | 1.5 | 0.7 | 2.4 | 35.5 |
| Cedric Coward | 98% | 30.4<br><sub>28,-,32,31,27</sub> | 17.9<br><sub>7,-,17,16,17</sub> | 15.5 · – | 7.3<br><sub>7,-,11,11,7</sub> | 6.5 | 3.7<br><sub>2,-,1,3,4</sub> | 2.5 | 2.0<br><sub>1,-,3,4,3</sub> | 1.5 | 0.9 | 0.5 | 2.0 | 28.9 |
| Jaylen Wells | 98% | 30.2<br><sub>28,25,33,30,25</sub> | 16.8<br><sub>12,17,16,14,10</sub> | 11.5 · – | 3.6<br><sub>5,4,5,3,1</sub> | 2.5 | 2.1<br><sub>0,3,3,0,0</sub> | 1.5 | 2.3<br><sub>1,4,2,2,2</sub> | 1.5 | 1.1 | 0.2 | 1.3 | 22.4 |
| Jerami Grant | 98% | 27.2<br><sub>24,26,22,24,27</sub> | 15.2<br><sub>15,6,5,13,2</sub> |  | 2.9<br><sub>2,0,5,3,1</sub> |  | 2.4<br><sub>3,3,3,0,3</sub> |  | 1.8<br><sub>2,1,1,3,0</sub> |  | 0.8 | 0.8 | 1.7 | 20.5 |
| Zach Edey | 98% | 24.4<br><sub>21,22,-,21,19</sub> | 10.9<br><sub>6,8,-,4,13</sub> | 9.5 · – | 9.6<br><sub>9,10,-,3,7</sub> | 8.5 | 1.5<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.7 | 1.7 | 1.7 | 22.0 |
| Cam Spencer | 96% | 22.6<br><sub>16,17,16,18,23</sub> | 10.7<br><sub>3,11,13,8,8</sub> |  | 2.8<br><sub>3,2,2,5,6</sub> |  | 5.8<br><sub>2,1,1,5,8</sub> |  | 1.6<br><sub>1,3,3,2,1</sub> |  | 0.8 | 0.2 | 1.2 | 19.3 |
| GG Jackson | 96% | 19.7<br><sub>19,15,10,16,21</sub> | 12.0<br><sub>12,2,1,4,12</sub> |  | 4.1<br><sub>8,4,3,1,7</sub> |  | 1.6<br><sub>0,1,0,2,2</sub> |  | 1.1<br><sub>2,0,0,0,2</sub> |  | 0.5 | 0.7 | 1.5 | 17.6 |
| Javon Small | 26% | 18.2 | 9.5 |  | 2.8 |  | 3.1 |  | 1.1 |  | 0.8 | 0.2 | 1.4 | 15.4 |
| Jahmai Mashack | 38% | 18.0<br><sub>-,-,-,-,-</sub> | 5.8<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0 | 0.4 | 1.5 | 10.5 |
| Isaiah Stewart | 98% | 17.5<br><sub>-,16,22,15,16</sub> | 7.7<br><sub>-,4,13,4,18</sub> |  | 4.0<br><sub>-,2,5,4,3</sub> |  | 0.8<br><sub>-,0,2,0,0</sub> |  | 0.6<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.1 | 0.9 | 12.6 |
| Taylor Hendricks | 58% | 11.6<br><sub>-,-,7,-,3</sub> | 4.7<br><sub>-,-,0,-,0</sub> |  | 2.3<br><sub>-,-,1,-,1</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.4 | 0.6 | 7.6 |
| Olivier-Maxence Prosper | 48% | 11.3<br><sub>-,-,-,-,3</sub> | 6.7<br><sub>-,-,-,-,4</sub> |  | 2.3<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 9.7 |
| Kris Murray | 58% | 10.1<br><sub>-,13,-,-,3</sub> | 2.6<br><sub>-,0,-,-,0</sub> |  | 1.6<br><sub>-,3,-,-,1</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.0 |
| Carson Cooper | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Karim Lopez | 48% | 6.9<br><sub>-,-,-,-,3</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 2.2 |

</details>

<details><summary>if Ty Jerome plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 96% | 32.2<br><sub>33,37,31,31,28</sub> | 15.8<br><sub>7,25,14,13,18</sub> | 17.5 · – | 9.8<br><sub>11,13,11,7,12</sub> | 8.5 | 6.1<br><sub>5,6,4,4,12</sub> | 5.5 | 1.8<br><sub>0,4,2,1,4</sub> | 1.5 | 1.4 | 0.7 | 2.0 | 31.7 |
| Ty Jerome (MEM) | 100% | 29.0<br><sub>32,32,32,30,24</sub> | 22.1<br><sub>45,28,31,15,10</sub> | 21.5 · – | 3.5<br><sub>7,2,4,1,2</sub> | 2.5 | 6.4<br><sub>6,5,7,8,3</sub> | 5.5 | 2.6<br><sub>5,3,1,1,1</sub> | 2.5 | 1.3 | 0.3 | 2.4 | 32.0 |
| Jaylen Wells (MEM) | 98% | 27.9<br><sub>28,25,33,30,25</sub> | 13.9<br><sub>12,17,16,14,10</sub> | 11.5 · – | 3.2<br><sub>5,4,5,3,1</sub> | 2.5 | 1.7<br><sub>0,3,3,0,0</sub> | 1.5 | 1.9<br><sub>1,4,2,2,2</sub> | 1.5 | 1.0 | 0.1 | 1.0 | 18.8 |
| Cedric Coward (MEM) | 98% | 27.8<br><sub>28,-,32,31,27</sub> | 15.0<br><sub>7,-,17,16,17</sub> | 15.5 · – | 6.6<br><sub>7,-,11,11,7</sub> | 6.5 | 2.9<br><sub>2,-,1,3,4</sub> | 2.5 | 1.7<br><sub>1,-,3,4,3</sub> | 1.5 | 0.9 | 0.5 | 1.6 | 24.5 |
| Jerami Grant (MEM) | 98% | 24.8<br><sub>24,26,22,24,27</sub> | 11.9<br><sub>15,6,5,13,2</sub> |  | 2.6<br><sub>2,0,5,3,1</sub> |  | 1.8<br><sub>3,3,3,0,3</sub> |  | 1.4<br><sub>2,1,1,3,0</sub> |  | 0.7 | 0.8 | 1.3 | 16.3 |
| Zach Edey (MEM) | 98% | 22.2<br><sub>21,22,-,21,19</sub> | 9.5<br><sub>6,8,-,4,13</sub> | 9.5 · – | 8.4<br><sub>9,10,-,3,7</sub> | 8.5 | 1.3<br><sub>0,3,-,2,0</sub> |  | 0.1<br><sub>0,0,-,0,1</sub> |  | 0.6 | 1.6 | 1.4 | 19.2 |
| Cam Spencer (MEM) | 96% | 19.1<br><sub>16,17,16,18,23</sub> | 8.6<br><sub>3,11,13,8,8</sub> |  | 2.4<br><sub>3,2,2,5,6</sub> |  | 4.5<br><sub>2,1,1,5,8</sub> |  | 1.2<br><sub>1,3,3,2,1</sub> |  | 0.7 | 0.2 | 0.9 | 15.4 |
| GG Jackson (MEM) | 96% | 16.9<br><sub>19,15,10,16,21</sub> | 9.6<br><sub>12,2,1,4,12</sub> |  | 3.4<br><sub>8,4,3,1,7</sub> |  | 1.2<br><sub>0,1,0,2,2</sub> |  | 0.8<br><sub>2,0,0,0,2</sub> |  | 0.4 | 0.6 | 1.2 | 14.2 |
| Isaiah Stewart (MEM) | 98% | 15.1<br><sub>-,16,22,15,16</sub> | 6.2<br><sub>-,4,13,4,18</sub> |  | 3.4<br><sub>-,2,5,4,3</sub> |  | 0.7<br><sub>-,0,2,0,0</sub> |  | 0.4<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.0 | 0.8 | 10.3 |
| Javon Small (MEM) | 26% | 12.6 | 5.7 |  | 1.9 |  | 2.1 |  | 0.6 |  | 0.6 | 0.2 | 0.9 | 9.7 |
| Jahmai Mashack (MEM) | 38% | 11.4<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.8 | 6.3 |
| Olivier-Maxence Prosper (MEM) | 48% | 9.0<br><sub>-,-,-,-,3</sub> | 5.2<br><sub>-,-,-,-,4</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 7.6 |
| Carson Cooper (MEM) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.2 |
| Taylor Hendricks (MEM) | 58% | 8.4<br><sub>-,-,7,-,3</sub> | 3.3<br><sub>-,-,0,-,0</sub> |  | 1.6<br><sub>-,-,1,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 5.4 |
| Kris Murray (MEM) | 58% | 7.9<br><sub>-,13,-,-,3</sub> | 2.0<br><sub>-,0,-,-,0</sub> |  | 1.3<br><sub>-,3,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.1 | 0.3 | 3.9 |
| Karim Lopez (MEM) | 48% | 5.7<br><sub>-,-,-,-,3</sub> | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 1.9 |
| Darius Acuff Jr. (SAC) | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.1<br><sub>12,33,22,19,34</sub> | 22.5 · – | 4.4<br><sub>3,2,3,3,6</sub> | 3.5 | 6.5<br><sub>3,4,7,5,14</sub> | 5.5 | 2.7<br><sub>0,2,2,3,3</sub> | 2.5 | 1.2 | 0.4 | 3.4 | 34.0 |
| Zach LaVine (SAC) | 98% | 34.1<br><sub>34,39,40,31,39</sub> | 21.3<br><sub>28,22,37,22,21</sub> | 20.5 · – | 3.9<br><sub>4,5,2,3,3</sub> | 2.5 | 3.0<br><sub>4,1,5,3,5</sub> | 2.5 | 2.6<br><sub>3,3,3,3,3</sub> | 2.5 | 1.0 | 0.3 | 2.6 | 28.2 |
| Domantas Sabonis (SAC) | 98% | 34.0<br><sub>34,39,35,37,40</sub> | 18.4<br><sub>14,27,15,20,9</sub> | 16.5 · – | 14.1<br><sub>18,19,15,14,15</sub> | 13.5 | 6.0<br><sub>8,10,3,8,7</sub> | 6.5 | 0.2<br><sub>0,1,0,0,0</sub> | 0.5 | 0.9 | 0.4 | 3.1 | 38.5 |
| Precious Achiuwa (SAC) | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.7<br><sub>15,14,12,4,24</sub> | 12.5 · – | 8.9<br><sub>5,6,10,1,9</sub> | 7.5 | 1.9<br><sub>2,1,0,0,2</sub> | 1.5 | 0.3<br><sub>1,0,0,0,0</sub> | 0.5 | 1.5 | 1.1 | 1.7 | 26.6 |
| De'Andre Hunter (SAC) | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.2<br><sub>6,4,7,24,24</sub> | 12.5 · – | 5.6<br><sub>3,7,6,6,5</sub> | 4.5 | 1.7<br><sub>1,1,1,2,1</sub> | 1.5 | 1.6<br><sub>2,0,2,5,4</sub> | 1.5 | 0.8 | 0.2 | 1.8 | 20.4 |
| Emanuel Sharp (SAC) | 96% | 15.6<br><sub>17,14,14,20,18</sub> | 4.9<br><sub>8,5,3,5,0</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.6<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.6 |
| Daeqwon Plowden (SAC) | 71% | 15.4<br><sub>13,20,16,17,-</sub> | 5.0<br><sub>4,3,3,0,-</sub> |  | 1.9<br><sub>2,0,3,2,-</sub> |  | 0.8<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,1,1,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.6 |
| Malik Monk (SAC) | 96% | 14.3<br><sub>-,12,12,13,8</sub> | 7.3<br><sub>-,0,6,3,2</sub> |  | 1.6<br><sub>-,1,1,2,1</sub> |  | 2.5<br><sub>-,2,2,6,1</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 1.1 | 11.3 |
| Jonathan Mogbo (SAC) | 52% | 12.1<br><sub>8,-,18,18,-</sub> | 4.4<br><sub>0,-,7,2,-</sub> |  | 2.3<br><sub>0,-,3,5,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.6 | 7.4 |
| Alex Karaban (SAC) | 64% | 11.4<br><sub>5,-,-,11,12</sub> | 3.6<br><sub>1,-,-,0,6</sub> |  | 2.2<br><sub>1,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.2<br><sub>0,-,-,0,2</sub> |  | 0.4 | 0.3 | 0.8 | 6.6 |
| Nique Clifford (SAC) | 83% | 10.3<br><sub>17,2,-,5,4</sub> | 4.0<br><sub>6,0,-,2,0</sub> |  | 1.6<br><sub>1,0,-,0,0</sub> |  | 1.1<br><sub>3,0,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.7 |
| Leaky Black (SAC) | 48% | 9.5<br><sub>-,-,-,8,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.4 | 5.0 |

</details>


### CLE @ MIL
Out: Jaylon Tyson (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kel'el Ware REB under 6.5 | CLE @ MIL | draftkings | 1.98 | 1.96 | 1.61 | 62.1% | 47.2% | 50.9% | +0.8% | +22.9% | 0.2% |
| Jaime Jaquez Jr. PR under 21.5 | CLE @ MIL | draftkings | 1.88 | 1.87 | 1.55 | 64.3% | 49.8% | 53.4% | +0.3% | +20.8% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.0–113.7 | CLE 62% | 1.61 / 2.64 | MIL +4.5 | 231.5 | MIL +9.5 covers 64%; o237.5 37% |
| Expected (weighted by chance each plays) | 118.3–114.1 | CLE 61% | 1.63 / 2.60 | MIL +4.5 | 232.5 | MIL +9.5 covers 64%; o237.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Meleek Thomas (CLE) | Questionable | 55% | 17.9 | 7.8 | 2.4 | 1.2 | 0.8 | 0.7 | 0.1 | 1.0 | 11.3 | small |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.0<br><sub>33,33,39,34,36</sub> | 20.0<br><sub>16,12,19,16,24</sub> | 19.5 · – | 4.8<br><sub>3,8,5,2,5</sub> | 4.5 | 6.8<br><sub>5,7,9,6,4</sub> |  | 2.8<br><sub>3,1,3,2,3</sub> | 2.5 | 1.5 | 0.4 | 3.4 | 31.5 |
| Donovan Mitchell | 98% | 35.5<br><sub>35,35,38,31,33</sub> | 26.9<br><sub>32,22,26,19,22</sub> | 25.5 · – | 5.0<br><sub>10,5,5,5,3</sub> | 4.5 | 4.8<br><sub>3,4,7,7,3</sub> | 5.5 | 3.1<br><sub>2,2,5,2,1</sub> | 2.5 | 1.6 | 0.3 | 2.6 | 36.7 |
| Evan Mobley | 98% | 34.5<br><sub>34,35,38,32,33</sub> | 18.3<br><sub>18,20,18,24,11</sub> | 17.5 · – | 9.1<br><sub>8,10,10,12,4</sub> | 9.5 | 3.5<br><sub>2,4,3,2,7</sub> | 3.5 | 1.3<br><sub>1,2,4,5,0</sub> | 1.5 | 0.9 | 1.5 | 1.9 | 30.9 |
| Peyton Watson | 98% | 30.4<br><sub>30,31,37,28,22</sub> | 14.6<br><sub>8,11,15,22,4</sub> | 13.5 · – | 4.8<br><sub>1,3,8,6,4</sub> | 4.5 | 2.4<br><sub>2,4,1,2,3</sub> |  | 1.3<br><sub>0,2,0,1,0</sub> | 1.5 | 1.1 | 1.1 | 1.8 | 21.7 |
| Jarrett Allen | 98% | 30.1<br><sub>28,27,27,30,30</sub> | 14.3<br><sub>14,21,10,8,14</sub> | 14.5 · – | 9.0<br><sub>7,8,9,12,8</sub> | 9.5 | 1.7<br><sub>0,0,2,2,1</sub> |  | 0.1<br><sub>0,1,0,0,1</sub> |  | 1.2 | 1.3 | 1.2 | 25.0 |
| Sam Merrill | 98% | 26.3<br><sub>24,21,31,20,27</sub> | 10.9<br><sub>5,7,9,8,16</sub> | 8.5 · – | 2.4<br><sub>5,2,4,1,2</sub> | 2.5 | 2.2<br><sub>2,3,2,1,3</sub> |  | 2.1<br><sub>1,1,1,2,4</sub> | 1.5 | 0.8 | 0.1 | 0.7 | 15.5 |
| Tyrese Proctor | 71% | 17.7<br><sub>5,11,-,6,20</sub> | 7.3<br><sub>0,5,-,2,7</sub> |  | 2.4<br><sub>0,2,-,1,6</sub> |  | 2.4<br><sub>0,3,-,1,2</sub> |  | 1.0<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.1 | 1.0 | 12.1 |
| Mario Hezonja | 96% | 17.6<br><sub>19,20,15,17,17</sub> | 6.7<br><sub>10,9,3,5,10</sub> | 7.5 · – | 3.4<br><sub>3,5,3,3,6</sub> | 3.5 | 1.4<br><sub>2,1,1,2,2</sub> |  | 0.8<br><sub>0,2,1,1,2</sub> | 1.5 | 0.6 | 0.3 | 0.7 | 11.5 |
| Thomas Bryant | 25% | 11.1<br><sub>-,-,-,-,-</sub> | 5.0<br><sub>-,-,-,-,-</sub> |  | 3.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 8.6 |
| Craig Porter Jr. | 58% | 11.0<br><sub>8,5,-,-,4</sub> | 2.9<br><sub>0,3,-,-,0</sub> |  | 2.1<br><sub>3,1,-,-,1</sub> |  | 1.7<br><sub>0,1,-,-,0</sub> |  | 0.2<br><sub>0,1,-,-,0</sub> |  | 0.6 | 0.3 | 0.7 | 6.7 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Riley Minix | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 5.3 |
| Tristan Enaruna | 23% | 7.3<br><sub>-,-,-,-,-</sub> | 2.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.5<br><sub>32,32,31,32,27</sub> | 19.0<br><sub>24,34,13,23,23</sub> | 22.5 · – | 4.5<br><sub>2,5,6,10,3</sub> | 4.5 | 4.7<br><sub>9,4,3,7,0</sub> | 4.5 | 2.5<br><sub>4,5,1,3,4</sub> | 2.5 | 0.9 | 0.2 | 2.3 | 28.2 |
| Ryan Rollins | 98% | 27.8<br><sub>24,34,25,32,17</sub> | 14.4<br><sub>9,11,15,19,4</sub> | 15.5 · – | 3.9<br><sub>6,7,4,2,4</sub> | 4.5 | 5.1<br><sub>3,6,4,4,5</sub> | 4.5 | 2.0<br><sub>1,2,2,3,0</sub> | 1.5 | 1.3 | 0.3 | 2.3 | 23.4 |
| Jaime Jaquez Jr. | 98% | 26.4<br><sub>31,35,27,25,27</sub> | 14.3<br><sub>22,19,21,8,19</sub> | 15.5 · – | 5.1<br><sub>7,11,8,6,4</sub> | 5.5 | 3.8<br><sub>2,5,4,0,2</sub> | 3.5 | 1.1<br><sub>1,2,2,0,3</sub> | 1.5 | 0.7 | 0.2 | 1.9 | 23.2 |
| Kyle Kuzma | 98% | 25.3<br><sub>27,30,35,29,18</sub> | 11.7<br><sub>5,14,14,17,4</sub> | 11.5 · – | 4.8<br><sub>6,9,12,7,6</sub> | 5.5 | 2.8<br><sub>3,4,3,3,1</sub> | 2.5 | 1.3<br><sub>1,2,0,4,0</sub> | 1.5 | 0.8 | 0.3 | 1.6 | 19.3 |
| Myles Turner | 98% | 23.6<br><sub>32,30,20,28,22</sub> | 9.8<br><sub>11,12,0,6,4</sub> | 9.5 · – | 4.7<br><sub>5,3,5,9,2</sub> | 4.5 | 1.3<br><sub>3,1,1,4,2</sub> | 1.5 | 1.3<br><sub>2,2,0,0,0</sub> | 1.5 | 0.7 | 1.5 | 1.2 | 15.8 |
| Kasparas Jakucionis | 88% | 19.3<br><sub>26,23,25,21,19</sub> | 6.6<br><sub>15,7,12,7,4</sub> | 7.5 · – | 2.4<br><sub>3,2,3,4,2</sub> | 2.5 | 3.4<br><sub>3,5,2,5,6</sub> | 3.5 | 0.6<br><sub>1,1,0,1,0</sub> | 0.5 | 0.7 | 0.2 | 1.5 | 12.4 |
| AJ Green | 98% | 18.7<br><sub>15,17,19,20,24</sub> | 7.0<br><sub>6,11,11,3,9</sub> | 6.5 · – | 1.9<br><sub>0,1,3,4,1</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 1.2<br><sub>2,3,3,1,3</sub> | 1.5 | 0.4 | 0.1 | 0.5 | 10.2 |
| Cormac Ryan | 26% | 17.6 | 8.8 |  | 2.1 |  | 1.2 |  | 1.2 |  | 0.7 | 0.2 | 1.1 | 12.1 |
| Kel'el Ware | 88% | 17.3<br><sub>14,15,29,19,17</sub> | 8.8<br><sub>7,11,19,16,6</sub> | 9.5 · – | 5.8<br><sub>3,4,13,14,8</sub> | 6.5 | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.6 | 0.4 | 1.1 | 15.3 |
| Brayden Burries | 96% | 13.5<br><sub>16,8,17,16,17</sub> | 6.0<br><sub>12,3,10,4,10</sub> |  | 2.7<br><sub>5,1,5,2,5</sub> |  | 1.4<br><sub>0,3,2,1,1</sub> |  | 0.5<br><sub>2,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.1 |
| Ousmane Dieng | 83% | 12.4<br><sub>21,16,-,3,13</sub> | 4.8<br><sub>5,3,-,0,4</sub> |  | 2.0<br><sub>4,1,-,0,0</sub> |  | 1.6<br><sub>3,1,-,0,0</sub> |  | 0.4<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 8.3 |
| Nate Ament | 67% | 11.8<br><sub>-,-,11,14,20</sub> | 5.0<br><sub>-,-,1,7,8</sub> |  | 2.5<br><sub>-,-,3,3,4</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,1,1</sub> |  | 0.5 | 0.2 | 0.7 | 8.0 |
| Caris LeVert | 30% | 10.9<br><sub>-,-,-,-,-</sub> | 4.2<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.5 | 0.3 | 0.6 | 6.9 |
| Gary Trent Jr. | 52% | 9.4<br><sub>-,-,-,-,7</sub> | 3.9<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.0 | 0.4 | 5.0 |
| Jericho Sims | 52% | 9.3<br><sub>2,-,-,-,7</sub> | 3.1<br><sub>0,-,-,-,0</sub> |  | 2.8<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.8 |
| Pete Nance | 30% | 9.0 | 2.9 |  | 1.5 |  | 0.6 |  | 0.3 |  | 0.2 | 0.2 | 0.3 | 5.0 |
| Kam Jones | 26% | 8.2 | 2.3 |  | 0.9 |  | 1.6 |  | 0.1 |  | 0.3 | 0.1 | 0.5 | 4.8 |
| Bogoljub Markovic | 48% | 6.1<br><sub>-,-,-,-,5</sub> | 2.5<br><sub>-,-,-,-,2</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>


### MIN @ SAS
Out: Tobias Harris (SAS), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.6<br><sub>29,30,31,37,35</sub> | 16.8<br><sub>17,15,14,14,19</sub> | 16.5 · – | 5.6<br><sub>8,6,6,6,7</sub> | 5.5 | 2.7<br><sub>1,3,3,4,4</sub> | 2.5 | 1.4<br><sub>1,2,1,2,1</sub> | 1.5 | 1.1 | 0.9 | 1.7 | 25.1 |
| Jonathan Kuminga | 98% | 31.2<br><sub>30,27,26,36,32</sub> | 14.5<br><sub>12,11,13,10,20</sub> | 13.5 · – | 5.5<br><sub>1,8,4,10,3</sub> | 5.5 | 2.3<br><sub>3,5,1,1,5</sub> | 2.5 | 1.4<br><sub>2,2,3,0,3</sub> | 1.5 | 1.0 | 0.5 | 1.5 | 22.3 |
| Rudy Gobert | 98% | 30.9<br><sub>33,30,31,36,20</sub> | 9.2<br><sub>5,14,8,5,1</sub> | 8.5 · – | 10.5<br><sub>15,9,13,20,4</sub> | 10.5 | 1.7<br><sub>1,1,0,2,1</sub> | 1.5 | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.2 | 1.4 | 21.4 |
| Ayo Dosunmu | 98% | 30.2<br><sub>29,27,23,26,32</sub> | 14.6<br><sub>16,14,9,9,17</sub> | 15.5 · – | 4.1<br><sub>5,7,3,1,3</sub> | 4.5 | 4.0<br><sub>3,10,3,0,4</sub> | 3.5 | 1.5<br><sub>1,1,1,1,3</sub> | 1.5 | 1.0 | 0.3 | 1.7 | 22.8 |
| LaMelo Ball | 98% | 28.1<br><sub>29,23,17,31,28</sub> | 18.4<br><sub>21,12,15,11,8</sub> | 19.5 · – | 3.8<br><sub>2,5,1,0,4</sub> | 4.5 | 5.9<br><sub>6,5,8,6,8</sub> | 6.5 | 3.0<br><sub>5,2,4,1,2</sub> | 3.5 | 1.2 | 0.2 | 2.8 | 28.1 |
| Terrence Shannon Jr. | 96% | 25.6<br><sub>20,22,23,24,27</sub> | 13.6<br><sub>10,13,15,14,19</sub> | 12.5 · – | 3.0<br><sub>1,4,4,4,6</sub> | 3.5 | 2.1<br><sub>1,1,3,5,2</sub> | 1.5 | 1.4<br><sub>2,2,3,3,1</sub> | 1.5 | 0.7 | 0.1 | 1.4 | 18.7 |
| Trey Lyles | 97% | 17.8<br><sub>12,17,14,13,22</sub> | 5.2<br><sub>1,9,3,3,7</sub> |  | 3.9<br><sub>1,6,6,1,3</sub> |  | 1.0<br><sub>0,2,2,1,1</sub> |  | 0.7<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.3 | 0.5 | 10.1 |
| Joan Beringer | 91% | 17.2<br><sub>14,15,13,17,20</sub> | 7.4<br><sub>0,9,6,12,7</sub> |  | 5.9<br><sub>6,9,6,7,9</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.0 |
| Bones Hyland | 96% | 15.5<br><sub>4,8,15,5,16</sub> | 7.4<br><sub>3,3,3,0,13</sub> | 8.5 · – | 1.8<br><sub>1,1,3,1,1</sub> |  | 1.9<br><sub>0,0,2,2,3</sub> | 2.5 | 1.1<br><sub>1,1,0,0,3</sub> | 1.5 | 0.6 | 0.3 | 0.9 | 11.1 |
| Jaylen Clark | 71% | 9.6<br><sub>3,3,5,-,7</sub> | 3.2<br><sub>1,0,3,-,3</sub> |  | 1.4<br><sub>1,2,1,-,2</sub> |  | 0.6<br><sub>1,1,0,-,1</sub> |  | 0.3<br><sub>0,0,0,-,1</sub> |  | 0.5 | 0.1 | 0.3 | 5.1 |
| Zyon Pullin | 52% | 8.3<br><sub>-,-,5,-,-</sub> | 2.9<br><sub>-,-,2,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.1 |
| Rocco Zikarsky | 23% | 7.3 | 2.5 |  | 2.3 |  | 0.4 |  | 0.0 |  | 0.2 | 0.6 | 0.3 | 5.1 |
| Enrique Freeman | 16% | 6.5 | 2.0 |  | 1.4 |  | 0.3 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Cody Williams | 52% | 6.4<br><sub>3,3,5,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.3 | 1.0 |
| Isaiah Evans | 52% | 6.0<br><sub>2,2,4,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 1.0<br><sub>1,0,0,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 2.0 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 34.4<br><sub>34,32,29,27,39</sub> | 25.2<br><sub>12,25,23,29,36</sub> | 24.5 · – | 11.4<br><sub>13,13,7,10,14</sub> | 11.5 | 3.2<br><sub>3,2,2,2,5</sub> | 2.5 | 1.9<br><sub>0,2,2,0,4</sub> | 1.5 | 1.2 | 3.7 | 2.7 | 39.8 |
| Devin Vassell | 98% | 33.4<br><sub>31,36,32,24,38</sub> | 12.6<br><sub>7,10,11,14,21</sub> | 11.5 · – | 4.7<br><sub>3,4,4,4,5</sub> | 3.5 | 2.9<br><sub>1,2,6,8,2</sub> | 2.5 | 1.9<br><sub>1,2,1,4,1</sub> | 2.5 | 1.2 | 0.5 | 1.0 | 20.1 |
| De'Aaron Fox | 98% | 33.0<br><sub>32,34,28,26,39</sub> | 16.2<br><sub>14,19,19,11,14</sub> | 14.5 · – | 4.1<br><sub>7,4,3,4,3</sub> | 3.5 | 6.2<br><sub>7,9,9,6,4</sub> | 5.5 | 1.4<br><sub>0,2,2,2,1</sub> | 1.5 | 1.5 | 0.4 | 2.2 | 26.5 |
| Stephon Castle | 98% | 32.4<br><sub>28,33,28,27,38</sub> | 17.9<br><sub>24,15,19,15,14</sub> | 16.5 · – | 5.4<br><sub>7,7,4,5,6</sub> | 5.5 | 6.3<br><sub>1,5,8,5,8</sub> | 5.5 | 1.7<br><sub>5,3,3,3,1</sub> | 1.5 | 1.2 | 0.3 | 3.1 | 29.6 |
| Dylan Harper | 98% | 31.7<br><sub>32,36,28,30,37</sub> | 16.5<br><sub>18,20,22,13,13</sub> | 16.5 · – | 5.6<br><sub>7,3,5,6,5</sub> | 4.5 | 4.1<br><sub>5,2,2,6,8</sub> | 4.5 | 1.2<br><sub>0,1,3,0,2</sub> | 1.5 | 1.1 | 0.4 | 1.8 | 26.2 |
| Julian Champagnie | 98% | 28.4<br><sub>30,25,28,25,31</sub> | 9.8<br><sub>8,6,12,26,6</sub> | 9.5 · – | 4.8<br><sub>3,0,5,3,6</sub> | 4.5 | 1.4<br><sub>1,0,3,3,0</sub> |  | 1.8<br><sub>2,2,3,8,2</sub> | 2.5 | 0.9 | 0.6 | 0.8 | 16.0 |
| Keldon Johnson | 98% | 20.8<br><sub>20,19,26,22,23</sub> | 10.0<br><sub>10,8,7,14,9</sub> | 9.5 · – | 4.2<br><sub>4,6,6,4,6</sub> | 4.5 | 1.1<br><sub>1,1,3,0,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> | 0.5 | 0.6 | 0.2 | 0.9 | 15.3 |
| Luke Kornet | 98% | 14.1<br><sub>13,16,14,17,14</sub> | 3.4<br><sub>4,7,0,0,1</sub> |  | 4.1<br><sub>1,3,4,4,6</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 8.3 |
| Harrison Barnes | 67% | 8.6<br><sub>9,5,4,14,-</sub> | 2.7<br><sub>3,0,0,3,-</sub> |  | 1.1<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Carter Bryant | 98% | 8.2<br><sub>6,4,10,17,5</sub> | 2.6<br><sub>0,0,4,1,3</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>1,0,0,2,0</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.2 | 0.2 | 0.4 | 4.5 |
| Maliq Brown | 80% | 6.8<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 2.5<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.1 |
| Jordan McLaughlin | 52% | 6.3<br><sub>-,-,3,7,-</sub> | 2.1<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 0.9<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |
| Ja'Kobi Gillespie | 88% | 5.9<br><sub>1,-,3,-,-</sub> | 4.1<br><sub>2,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.4<br><sub>0,-,1,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 4.9 |
| Tarris Reed Jr. | 58% | 5.9<br><sub>1,-,7,5,-</sub> | 2.4<br><sub>0,-,2,4,-</sub> |  | 2.2<br><sub>0,-,3,5,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.7 | 5.0 |
| David Jones Garcia | 52% | 5.7<br><sub>1,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |

</details>


### OKC @ HOU
Out: Steven Adams (HOU), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander 3PM under 1.5 | OKC @ HOU | draftkings | 2.17 | 2.17 | 1.82 | 54.8% | 43.2% | 46.1% | +0.0% | +19.0% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 111.5–114.0 | OKC 43% | 2.30 / 1.77 | HOU -2.5 | 225.5 | HOU -3.5 covers 48%; o218.5 64% |
| Expected (weighted by chance each plays) | 111.0–115.3 | OKC 38% | 2.61 / 1.62 | HOU -4.5 | 225.5 | HOU -3.5 covers 53%; o218.5 66% |
| if Alperen Sengun plays | 111.7–115.3 | OKC 40% | 2.48 / 1.67 | HOU -3.5 | 226.5 | HOU -3.5 covers 51%; o218.5 67% |
| if Reed Sheppard plays | 111.7–114.6 | OKC 42% | 2.38 / 1.73 | HOU -3.5 | 226.5 | HOU -3.5 covers 49%; o218.5 66% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alperen Sengun (HOU) | Day-To-Day | 70% | 35.3 | 19.5 | 10.0 | 5.7 | 0.7 | 1.2 | 1.0 | 3.6 | 35.2 | full tables below |
| Reed Sheppard (HOU) | Day-To-Day | 70% | 25.5 | 12.0 | 2.7 | 3.6 | 2.1 | 1.4 | 0.6 | 1.6 | 18.3 | full tables below |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.8<br><sub>36,35,36,30,28</sub> | 29.9<br><sub>32,17,34,26,21</sub> |  | 3.9<br><sub>6,2,6,3,6</sub> |  | 6.5<br><sub>4,3,5,3,2</sub> |  | 1.5<br><sub>3,3,1,1,1</sub> | 1.5 | 1.5 | 0.9 | 3.2 | 40.3 |
| Jared McCain | 98% | 30.2<br><sub>22,18,21,30,29</sub> | 15.6<br><sub>20,4,3,18,10</sub> |  | 2.9<br><sub>2,0,1,3,4</sub> |  | 2.3<br><sub>2,1,0,4,4</sub> |  | 2.3<br><sub>6,0,1,4,0</sub> | 2.5 | 0.8 | 0.2 | 1.9 | 20.8 |
| Ajay Mitchell | 98% | 29.8<br><sub>23,23,28,25,28</sub> | 18.9<br><sub>4,12,18,30,29</sub> |  | 3.5<br><sub>5,0,6,2,4</sub> |  | 4.4<br><sub>6,0,4,5,3</sub> |  | 1.3<br><sub>0,0,1,1,2</sub> | 1.5 | 1.5 | 0.3 | 2.1 | 26.8 |
| Isaiah Hartenstein | 98% | 27.0<br><sub>17,23,27,26,26</sub> | 10.1<br><sub>4,6,12,15,10</sub> |  | 9.7<br><sub>3,6,12,13,14</sub> |  | 3.2<br><sub>3,2,1,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 23.0 |
| Josh Dix | 67% | 26.9<br><sub>-,-,-,22,24</sub> | 4.3<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.2 |
| Bennett Stirtz | 96% | 26.2<br><sub>1,2,11,25,28</sub> | 7.8<br><sub>0,0,2,7,8</sub> |  | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.0 |
| Aday Mara | 96% | 23.2<br><sub>12,13,14,20,21</sub> | 7.9<br><sub>7,2,2,11,6</sub> |  | 5.9<br><sub>2,3,3,10,3</sub> |  | 1.2<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.3 | 15.0 |
| Kenrich Williams | 93% | 21.6<br><sub>7,6,7,24,17</sub> | 8.1<br><sub>3,3,3,3,7</sub> |  | 4.5<br><sub>2,1,1,7,3</sub> |  | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> |  | 0.8 | 0.2 | 0.9 | 14.0 |
| Jaylin Williams | 98% | 20.6<br><sub>17,15,5,26,20</sub> | 5.9<br><sub>5,3,0,6,0</sub> |  | 5.2<br><sub>4,7,0,6,5</sub> |  | 1.9<br><sub>1,3,0,3,1</sub> |  | 0.9<br><sub>1,1,0,2,0</sub> |  | 0.6 | 0.5 | 0.8 | 13.0 |
| Micah Peavy | 48% | 13.2<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.7 |
| Brooks Barnhizer | 80% | 12.4<br><sub>1,2,-,3,14</sub> | 3.2<br><sub>0,0,-,0,3</sub> |  | 2.4<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |
| Ochai Agbaji | 23% | 11.9 | 4.5 |  | 1.7 |  | 0.5 |  | 0.4 |  | 0.4 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.4<br><sub>33,36,39,28,33</sub> | 19.2<br><sub>16,20,17,15,23</sub> | 16.5 · – | 8.0<br><sub>10,10,11,5,4</sub> | 7.5 | 5.7<br><sub>4,4,6,2,3</sub> | 4.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.6 | 0.7 | 2.9 | 32.9 |
| Kevin Durant | 98% | 37.0<br><sub>37,37,37,30,31</sub> | 25.4<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.6<br><sub>6,7,4,9,5</sub> | 5.5 | 5.4<br><sub>3,6,2,3,4</sub> | 2.5 | 2.3<br><sub>2,2,3,1,2</sub> | 1.5 | 0.9 | 1.1 | 3.8 | 37.5 |
| Jabari Smith Jr. | 98% | 37.0<br><sub>36,34,33,39,30</sub> | 16.9<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.7<br><sub>5,5,5,12,2</sub> | 5.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 2.6<br><sub>4,1,2,2,3</sub> | 1.5 | 0.8 | 0.9 | 1.8 | 26.9 |
| Fred VanVleet | 98% | 34.7<br><sub>30,32,-,29,29</sub> | 14.5<br><sub>6,14,-,5,24</sub> |  | 3.9<br><sub>2,3,-,4,6</sub> |  | 5.8<br><sub>11,5,-,5,5</sub> |  | 2.5<br><sub>2,3,-,0,4</sub> |  | 1.4 | 0.4 | 1.9 | 24.2 |
| Tari Eason | 98% | 31.0<br><sub>3,27,31,33,31</sub> | 12.9<br><sub>2,12,19,13,5</sub> |  | 7.3<br><sub>1,6,3,8,9</sub> |  | 1.7<br><sub>0,0,0,2,1</sub> |  | 1.4<br><sub>0,0,0,1,1</sub> |  | 1.5 | 0.8 | 1.7 | 21.9 |
| Marcus Smart | 52% | 26.2<br><sub>26,21,-,-,-</sub> | 9.3<br><sub>10,5,-,-,-</sub> |  | 2.9<br><sub>2,3,-,-,-</sub> |  | 2.8<br><sub>2,1,-,-,-</sub> |  | 1.3<br><sub>2,0,-,-,-</sub> |  | 1.4 | 0.4 | 2.0 | 15.0 |
| Oscar Tshiebwe | 67% | 19.7<br><sub>-,-,-,-,14</sub> | 8.2<br><sub>-,-,-,-,7</sub> |  | 8.1<br><sub>-,-,-,-,5</sub> |  | 1.2<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.4 | 1.2 | 17.4 |
| Bogdan Bogdanovic | 88% | 18.2<br><sub>13,9,20,13,15</sub> | 6.9<br><sub>5,3,11,5,16</sub> |  | 2.3<br><sub>1,1,1,2,2</sub> |  | 1.8<br><sub>2,0,1,1,4</sub> |  | 1.1<br><sub>1,1,3,1,4</sub> |  | 0.6 | 0.2 | 0.9 | 11.0 |
| Clint Capela | 83% | 17.6<br><sub>8,-,11,4,22</sub> | 5.2<br><sub>0,-,2,2,10</sub> |  | 6.1<br><sub>3,-,3,2,8</sub> |  | 1.0<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.0 | 0.9 | 12.2 |
| Julian Phillips | 23% | 10.0 | 3.4 |  | 1.3 |  | 0.5 |  | 0.3 |  | 0.4 | 0.2 | 0.4 | 5.2 |
| Jae'Sean Tate | 84% | 8.6<br><sub>2,-,1,1,4</sub> | 2.7<br><sub>0,-,0,0,0</sub> |  | 1.9<br><sub>0,-,0,1,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.1 | 0.4 | 5.1 |
| Quadir Copeland | 16% | 8.5 | 3.5 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Isaiah Crawford | 72% | 7.9<br><sub>3,-,1,1,5</sub> | 2.5<br><sub>3,-,0,0,3</sub> |  | 1.4<br><sub>0,-,0,0,0</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.3 | 4.3 |
| Bruce Thornton | 80% | 7.7<br><sub>3,-,4,1,3</sub> | 2.4<br><sub>0,-,0,0,5</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.2 | 0.1 | 0.4 | 3.3 |

</details>

<details><summary>if Alperen Sengun plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 36.3<br><sub>33,36,39,28,33</sub> | 17.7<br><sub>16,20,17,15,23</sub> | 16.5 · – | 7.5<br><sub>10,10,11,5,4</sub> | 7.5 | 4.9<br><sub>4,4,6,2,3</sub> | 4.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.5 | 0.7 | 2.5 | 30.1 |
| Kevin Durant (HOU) | 98% | 36.1<br><sub>37,37,37,30,31</sub> | 22.0<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.2<br><sub>6,7,4,9,5</sub> | 5.5 | 4.6<br><sub>3,6,2,3,4</sub> | 2.5 | 2.0<br><sub>2,2,3,1,2</sub> | 1.5 | 0.8 | 1.1 | 3.5 | 32.8 |
| Jabari Smith Jr. (HOU) | 98% | 35.6<br><sub>36,34,33,39,30</sub> | 15.1<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.3<br><sub>5,5,5,12,2</sub> | 5.5 | 1.9<br><sub>1,1,3,5,2</sub> |  | 2.4<br><sub>4,1,2,2,3</sub> | 1.5 | 0.8 | 0.9 | 1.6 | 24.2 |
| Alperen Sengun (HOU) | 100% | 35.3<br><sub>30,36,33,37,-</sub> | 19.5<br><sub>23,29,17,29,-</sub> | 19.5 · – | 10.0<br><sub>10,7,10,9,-</sub> | 8.5 | 5.7<br><sub>5,7,7,9,-</sub> | 5.5 | 0.7<br><sub>2,2,1,1,-</sub> |  | 1.2 | 1.0 | 3.6 | 35.2 |
| Fred VanVleet (HOU) | 98% | 32.2<br><sub>30,32,-,29,29</sub> | 12.8<br><sub>6,14,-,5,24</sub> |  | 3.5<br><sub>2,3,-,4,6</sub> |  | 5.0<br><sub>11,5,-,5,5</sub> |  | 2.2<br><sub>2,3,-,0,4</sub> |  | 1.3 | 0.4 | 1.7 | 21.3 |
| Tari Eason (HOU) | 98% | 26.3<br><sub>3,27,31,33,31</sub> | 10.6<br><sub>2,12,19,13,5</sub> |  | 6.2<br><sub>1,6,3,8,9</sub> |  | 1.3<br><sub>0,0,0,2,1</sub> |  | 1.1<br><sub>0,0,0,1,1</sub> |  | 1.3 | 0.7 | 1.3 | 18.0 |
| Marcus Smart (HOU) | 52% | 22.9<br><sub>26,21,-,-,-</sub> | 7.7<br><sub>10,5,-,-,-</sub> |  | 2.3<br><sub>2,3,-,-,-</sub> |  | 2.2<br><sub>2,1,-,-,-</sub> |  | 1.1<br><sub>2,0,-,-,-</sub> |  | 1.3 | 0.3 | 1.7 | 12.3 |
| Oscar Tshiebwe (HOU) | 67% | 14.6<br><sub>-,-,-,-,14</sub> | 6.0<br><sub>-,-,-,-,7</sub> |  | 5.7<br><sub>-,-,-,-,5</sub> |  | 0.8<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.9 | 12.5 |
| Bogdan Bogdanovic (HOU) | 88% | 14.5<br><sub>13,9,20,13,15</sub> | 5.4<br><sub>5,3,11,5,16</sub> |  | 1.8<br><sub>1,1,1,2,2</sub> |  | 1.4<br><sub>2,0,1,1,4</sub> |  | 0.8<br><sub>1,1,3,1,4</sub> |  | 0.5 | 0.1 | 0.8 | 8.5 |
| Clint Capela (HOU) | 83% | 12.8<br><sub>8,-,11,4,22</sub> | 3.9<br><sub>0,-,2,2,10</sub> |  | 4.4<br><sub>3,-,3,2,8</sub> |  | 0.7<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.7 | 0.7 | 9.0 |
| Quadir Copeland (HOU) | 16% | 8.7 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Julian Phillips (HOU) | 23% | 6.5 | 2.2 |  | 0.8 |  | 0.3 |  | 0.2 |  | 0.3 | 0.1 | 0.3 | 3.3 |
| Jae'Sean Tate (HOU) | 84% | 6.2<br><sub>2,-,1,1,4</sub> | 2.2<br><sub>0,-,0,0,0</sub> |  | 1.4<br><sub>0,-,0,1,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Isaiah Crawford (HOU) | 72% | 5.8<br><sub>3,-,1,1,5</sub> | 2.2<br><sub>3,-,0,0,3</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,0,1</sub> |  | 0.1 | 0.2 | 0.2 | 3.6 |
| Bruce Thornton (HOU) | 80% | 5.8<br><sub>3,-,4,1,3</sub> | 2.1<br><sub>0,-,0,0,5</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.2 | 0.1 | 0.3 | 2.9 |
| Shai Gilgeous-Alexander (OKC) | 98% | 34.8<br><sub>36,35,36,30,28</sub> | 29.8<br><sub>32,17,34,26,21</sub> |  | 3.9<br><sub>6,2,6,3,6</sub> |  | 6.5<br><sub>4,3,5,3,2</sub> |  | 1.5<br><sub>3,3,1,1,1</sub> | 1.5 | 1.5 | 0.9 | 3.2 | 40.2 |
| Jared McCain (OKC) | 98% | 30.2<br><sub>22,18,21,30,29</sub> | 15.6<br><sub>20,4,3,18,10</sub> |  | 2.9<br><sub>2,0,1,3,4</sub> |  | 2.3<br><sub>2,1,0,4,4</sub> |  | 2.3<br><sub>6,0,1,4,0</sub> | 2.5 | 0.8 | 0.2 | 1.8 | 20.8 |
| Ajay Mitchell (OKC) | 98% | 29.7<br><sub>23,23,28,25,28</sub> | 18.9<br><sub>4,12,18,30,29</sub> |  | 3.5<br><sub>5,0,6,2,4</sub> |  | 4.4<br><sub>6,0,4,5,3</sub> |  | 1.3<br><sub>0,0,1,1,2</sub> | 1.5 | 1.5 | 0.3 | 2.1 | 26.9 |
| Josh Dix (OKC) | 67% | 26.9<br><sub>-,-,-,22,24</sub> | 4.4<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.3 |
| Isaiah Hartenstein (OKC) | 98% | 26.9<br><sub>17,23,27,26,26</sub> | 10.1<br><sub>4,6,12,15,10</sub> |  | 9.6<br><sub>3,6,12,13,14</sub> |  | 3.2<br><sub>3,2,1,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 22.9 |
| Bennett Stirtz (OKC) | 96% | 26.2<br><sub>1,2,11,25,28</sub> | 7.8<br><sub>0,0,2,7,8</sub> |  | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.0 |
| Aday Mara (OKC) | 96% | 23.2<br><sub>12,13,14,20,21</sub> | 8.0<br><sub>7,2,2,11,6</sub> |  | 5.9<br><sub>2,3,3,10,3</sub> |  | 1.2<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.3 | 15.1 |
| Kenrich Williams (OKC) | 93% | 21.6<br><sub>7,6,7,24,17</sub> | 8.0<br><sub>3,3,3,3,7</sub> |  | 4.5<br><sub>2,1,1,7,3</sub> |  | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> |  | 0.8 | 0.2 | 0.9 | 13.9 |
| Jaylin Williams (OKC) | 98% | 20.7<br><sub>17,15,5,26,20</sub> | 6.0<br><sub>5,3,0,6,0</sub> |  | 5.2<br><sub>4,7,0,6,5</sub> |  | 1.9<br><sub>1,3,0,3,1</sub> |  | 0.9<br><sub>1,1,0,2,0</sub> |  | 0.6 | 0.5 | 0.8 | 13.1 |
| Micah Peavy (OKC) | 48% | 13.2<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer (OKC) | 80% | 12.4<br><sub>1,2,-,3,14</sub> | 3.2<br><sub>0,0,-,0,3</sub> |  | 2.4<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.3 |
| Ochai Agbaji (OKC) | 23% | 11.8 | 4.5 |  | 1.7 |  | 0.6 |  | 0.4 |  | 0.3 | 0.2 | 0.4 | 6.7 |

</details>

<details><summary>if Reed Sheppard plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson (HOU) | 98% | 36.6<br><sub>33,36,39,28,33</sub> | 18.4<br><sub>16,20,17,15,23</sub> | 16.5 · – | 7.8<br><sub>10,10,11,5,4</sub> | 7.5 | 4.8<br><sub>4,4,6,2,3</sub> | 4.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.6 | 0.7 | 2.6 | 31.0 |
| Jabari Smith Jr. (HOU) | 98% | 36.3<br><sub>36,34,33,39,30</sub> | 16.0<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.5<br><sub>5,5,5,12,2</sub> | 5.5 | 2.0<br><sub>1,1,3,5,2</sub> |  | 2.5<br><sub>4,1,2,2,3</sub> | 1.5 | 0.8 | 0.9 | 1.6 | 25.5 |
| Kevin Durant (HOU) | 98% | 36.1<br><sub>37,37,37,30,31</sub> | 22.8<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.3<br><sub>6,7,4,9,5</sub> | 5.5 | 4.9<br><sub>3,6,2,3,4</sub> | 2.5 | 2.2<br><sub>2,2,3,1,2</sub> | 1.5 | 0.8 | 1.1 | 3.7 | 34.0 |
| Fred VanVleet (HOU) | 98% | 32.7<br><sub>30,32,-,29,29</sub> | 13.4<br><sub>6,14,-,5,24</sub> |  | 3.6<br><sub>2,3,-,4,6</sub> |  | 5.0<br><sub>11,5,-,5,5</sub> |  | 2.3<br><sub>2,3,-,0,4</sub> |  | 1.3 | 0.4 | 1.7 | 22.1 |
| Tari Eason (HOU) | 98% | 27.9<br><sub>3,27,31,33,31</sub> | 11.6<br><sub>2,12,19,13,5</sub> |  | 6.6<br><sub>1,6,3,8,9</sub> |  | 1.4<br><sub>0,0,0,2,1</sub> |  | 1.2<br><sub>0,0,0,1,1</sub> |  | 1.3 | 0.7 | 1.4 | 19.6 |
| Reed Sheppard (HOU) | 100% | 25.5<br><sub>16,-,30,24,23</sub> | 12.0<br><sub>3,-,19,13,7</sub> | 11.5 · – | 2.7<br><sub>2,-,6,0,3</sub> |  | 3.6<br><sub>4,-,7,4,4</sub> | 3.5 | 2.1<br><sub>1,-,5,2,1</sub> | 2.5 | 1.4 | 0.6 | 1.6 | 18.3 |
| Marcus Smart (HOU) | 52% | 23.4<br><sub>26,21,-,-,-</sub> | 8.2<br><sub>10,5,-,-,-</sub> |  | 2.6<br><sub>2,3,-,-,-</sub> |  | 2.4<br><sub>2,1,-,-,-</sub> |  | 1.1<br><sub>2,0,-,-,-</sub> |  | 1.3 | 0.3 | 1.7 | 13.2 |
| Oscar Tshiebwe (HOU) | 67% | 16.9<br><sub>-,-,-,-,14</sub> | 7.3<br><sub>-,-,-,-,7</sub> |  | 6.9<br><sub>-,-,-,-,5</sub> |  | 1.0<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.4 | 0.9 | 15.1 |
| Clint Capela (HOU) | 83% | 15.2<br><sub>8,-,11,4,22</sub> | 4.6<br><sub>0,-,2,2,10</sub> |  | 5.2<br><sub>3,-,3,2,8</sub> |  | 0.9<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.5 | 0.8 | 0.8 | 10.7 |
| Bogdan Bogdanovic (HOU) | 88% | 14.1<br><sub>13,9,20,13,15</sub> | 5.3<br><sub>5,3,11,5,16</sub> |  | 1.8<br><sub>1,1,1,2,2</sub> |  | 1.4<br><sub>2,0,1,1,4</sub> |  | 0.8<br><sub>1,1,3,1,4</sub> |  | 0.5 | 0.1 | 0.7 | 8.4 |
| Quadir Copeland (HOU) | 16% | 8.7 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Julian Phillips (HOU) | 23% | 7.8 | 2.7 |  | 1.0 |  | 0.3 |  | 0.2 |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Jae'Sean Tate (HOU) | 84% | 6.5<br><sub>2,-,1,1,4</sub> | 2.3<br><sub>0,-,0,0,0</sub> |  | 1.4<br><sub>0,-,0,1,0</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.1 |
| Isaiah Crawford (HOU) | 72% | 6.0<br><sub>3,-,1,1,5</sub> | 2.3<br><sub>3,-,0,0,3</sub> |  | 1.1<br><sub>0,-,0,0,0</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.2 | 0.2 | 3.7 |
| Bruce Thornton (HOU) | 80% | 5.8<br><sub>3,-,4,1,3</sub> | 2.2<br><sub>0,-,0,0,5</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.2 | 0.1 | 0.3 | 3.0 |
| Shai Gilgeous-Alexander (OKC) | 98% | 34.8<br><sub>36,35,36,30,28</sub> | 29.8<br><sub>32,17,34,26,21</sub> |  | 3.9<br><sub>6,2,6,3,6</sub> |  | 6.5<br><sub>4,3,5,3,2</sub> |  | 1.5<br><sub>3,3,1,1,1</sub> | 1.5 | 1.5 | 0.9 | 3.2 | 40.2 |
| Jared McCain (OKC) | 98% | 30.3<br><sub>22,18,21,30,29</sub> | 15.7<br><sub>20,4,3,18,10</sub> |  | 2.9<br><sub>2,0,1,3,4</sub> |  | 2.3<br><sub>2,1,0,4,4</sub> |  | 2.4<br><sub>6,0,1,4,0</sub> | 2.5 | 0.8 | 0.2 | 1.9 | 20.9 |
| Ajay Mitchell (OKC) | 98% | 29.7<br><sub>23,23,28,25,28</sub> | 18.9<br><sub>4,12,18,30,29</sub> |  | 3.5<br><sub>5,0,6,2,4</sub> |  | 4.3<br><sub>6,0,4,5,3</sub> |  | 1.3<br><sub>0,0,1,1,2</sub> | 1.5 | 1.5 | 0.3 | 2.1 | 26.8 |
| Isaiah Hartenstein (OKC) | 98% | 27.1<br><sub>17,23,27,26,26</sub> | 10.2<br><sub>4,6,12,15,10</sub> |  | 9.6<br><sub>3,6,12,13,14</sub> |  | 3.2<br><sub>3,2,1,3,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 23.0 |
| Josh Dix (OKC) | 67% | 26.9<br><sub>-,-,-,22,24</sub> | 4.4<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.3 |
| Bennett Stirtz (OKC) | 96% | 26.2<br><sub>1,2,11,25,28</sub> | 7.8<br><sub>0,0,2,7,8</sub> |  | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.0 |
| Aday Mara (OKC) | 96% | 23.3<br><sub>12,13,14,20,21</sub> | 7.9<br><sub>7,2,2,11,6</sub> |  | 5.9<br><sub>2,3,3,10,3</sub> |  | 1.2<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.3 | 15.0 |
| Kenrich Williams (OKC) | 93% | 21.6<br><sub>7,6,7,24,17</sub> | 8.1<br><sub>3,3,3,3,7</sub> |  | 4.5<br><sub>2,1,1,7,3</sub> |  | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> |  | 0.8 | 0.2 | 0.9 | 13.9 |
| Jaylin Williams (OKC) | 98% | 20.5<br><sub>17,15,5,26,20</sub> | 5.9<br><sub>5,3,0,6,0</sub> |  | 5.2<br><sub>4,7,0,6,5</sub> |  | 1.9<br><sub>1,3,0,3,1</sub> |  | 0.9<br><sub>1,1,0,2,0</sub> |  | 0.6 | 0.5 | 0.8 | 13.0 |
| Micah Peavy (OKC) | 48% | 13.2<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.7 |
| Brooks Barnhizer (OKC) | 80% | 12.4<br><sub>1,2,-,3,14</sub> | 3.3<br><sub>0,0,-,0,3</sub> |  | 2.4<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.3 |
| Ochai Agbaji (OKC) | 23% | 11.6 | 4.5 |  | 1.7 |  | 0.5 |  | 0.4 |  | 0.4 | 0.2 | 0.4 | 6.7 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-31/`._
