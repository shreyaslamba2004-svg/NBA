# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sun 01 Nov, 04:38 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

2 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| PHI @ CHA | team minutes | PHI players add up to 206 expected minutes (normal is about 240) | 53% of tonight's minutes go to players new to PHI since last season, and the team ratings still lean on last season; PHI have played 6 games this season; PHI out: Barlow, Embiid, James |
| PHI @ CHA | player points | Anfernee Simons projected 18.7 pts vs DraftKings line 13.5 | minutes 34 vs 24 this season; new team (was BOS last season); scoring 0.55/min vs 0.44 this season, 0.57 last season; teammates out: Barlow, Embiid, James (~92 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 7.5 (8+) | OKC @ HOU | draftkings | 19.40 | 12.84 | 5.99 | 16.7% | 4.8% | 7.8% | +51.1% | +223.9% | 0.7% |
| Deni Avdija PTS over 44.5 (45+) | POR @ UTA | draftkings | 29.00 | 23.42 | 13.52 | 7.4% | 3.2% | 4.3% | +23.7% | +114.6% | 0.2% |
| Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings | 29.00 | 23.98 | 14.23 | 7.0% | 3.2% | 4.2% | +21.1% | +103.8% | 0.2% |
| Shai Gilgeous-Alexander PA over 54.5 (55+) | OKC @ HOU | draftkings | 21.00 | 17.45 | 10.45 | 9.6% | 4.5% | 5.7% | +20.3% | +100.9% | 0.2% |
| Kevin Durant REB over 9.5 (10+) | OKC @ HOU | draftkings | 14.20 | 11.81 | 7.08 | 14.1% | 6.6% | 8.5% | +20.2% | +100.6% | 0.4% |
| Deni Avdija PTS over 39.5 (40+) | POR @ UTA | draftkings | 15.00 | 12.48 | 7.48 | 13.4% | 6.2% | 8.0% | +20.2% | +100.4% | 0.4% |
| Jabari Smith Jr. REB over 11.5 (12+) | OKC @ HOU | draftkings | 21.00 | 17.51 | 10.55 | 9.5% | 4.5% | 5.7% | +19.9% | +99.1% | 0.2% |
| Kevin Durant PTS over 39.5 (40+) | OKC @ HOU | draftkings | 19.40 | 16.37 | 10.01 | 10.0% | 4.8% | 6.1% | +18.5% | +93.8% | 0.2% |
| Jabari Smith Jr. REB over 9.5 (10+) | OKC @ HOU | draftkings | 8.50 | 7.18 | 4.40 | 22.7% | 11.0% | 13.9% | +18.3% | +93.0% | 0.6% |
| Amen Thompson AST over 9.5 (10+) | OKC @ HOU | draftkings | 22.00 | 18.69 | 11.53 | 8.7% | 4.2% | 5.3% | +17.8% | +90.8% | 0.2% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ HOU | draftkings | 10.90 | 9.27 | 5.73 | 17.4% | 8.6% | 10.8% | +17.6% | +90.2% | 0.4% |
| Ace Bailey BLK over 2.5 (3+) | POR @ UTA | draftkings | 11.60 | 9.90 | 6.16 | 16.2% | 8.1% | 10.1% | +17.2% | +88.4% | 0.4% |
| Amen Thompson AST over 7.5 (8+) | OKC @ HOU | draftkings | 8.00 | 6.84 | 4.26 | 23.5% | 11.7% | 14.6% | +17.0% | +87.8% | 0.6% |
| Shai Gilgeous-Alexander PRA over 59.5 (60+) | OKC @ HOU | draftkings | 20.40 | 17.45 | 10.88 | 9.2% | 4.6% | 5.7% | +17.0% | +87.5% | 0.2% |
| Damian Lillard AST over 9.5 (10+) | POR @ UTA | draftkings | 13.60 | 11.71 | 7.39 | 13.5% | 6.9% | 8.5% | +16.1% | +84.0% | 0.3% |
| Jabari Smith Jr. PRA over 34.5 (35+) | OKC @ HOU | draftkings | 10.00 | 8.68 | 5.54 | 18.1% | 9.3% | 11.5% | +15.2% | +80.5% | 0.4% |
| Shai Gilgeous-Alexander PTS over 44.5 (45+) | OKC @ HOU | draftkings | 14.80 | 12.90 | 8.28 | 12.1% | 6.3% | 7.8% | +14.8% | +78.6% | 0.3% |
| Shai Gilgeous-Alexander AST over 11.5 (12+) | OKC @ HOU | draftkings | 27.00 | 23.53 | 15.13 | 6.6% | 3.5% | 4.2% | +14.7% | +78.5% | 0.1% |
| Amen Thompson PTS over 29.5 (30+) | OKC @ HOU | draftkings | 19.40 | 17.01 | 11.04 | 9.1% | 4.8% | 5.9% | +14.0% | +75.8% | 0.2% |
| Shai Gilgeous-Alexander PA over 49.5 (50+) | OKC @ HOU | draftkings | 11.00 | 9.72 | 6.38 | 15.7% | 8.5% | 10.3% | +13.2% | +72.5% | 0.3% |
| Donovan Clingan BLK over 4.5 (5+) | POR @ UTA | draftkings | 15.60 | 13.91 | 9.26 | 10.8% | 6.0% | 7.2% | +12.2% | +68.5% | 0.2% |
| Kingston Flemings AST over 7.5 (8+) | ATL @ NOP | draftkings | 20.60 | 18.38 | 12.24 | 8.2% | 4.5% | 5.4% | +12.2% | +68.3% | 0.2% |
| Deni Avdija PRA over 59.5 (60+) | POR @ UTA | draftkings | 18.00 | 16.08 | 10.73 | 9.3% | 5.2% | 6.2% | +12.0% | +67.8% | 0.2% |
| Jabari Smith Jr. PRA over 39.5 (40+) | OKC @ HOU | draftkings | 20.80 | 18.62 | 12.48 | 8.0% | 4.5% | 5.4% | +11.8% | +66.7% | 0.1% |
| Kingston Flemings AST over 5.5 (6+) | ATL @ NOP | draftkings | 7.10 | 6.40 | 4.35 | 23.0% | 13.2% | 15.6% | +10.9% | +63.3% | 0.4% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. REB over 10.5 (11+) | OKC @ HOU | draftkings | 13.60 | 11.22 | 6.66 | 15.0% | 6.9% | 8.9% | +21.1% | +104.1% | 0.4% |
| Amen Thompson AST over 8.5 (9+) | OKC @ HOU | draftkings | 14.00 | 11.61 | 6.93 | 14.4% | 6.7% | 8.6% | +20.6% | +102.0% | 0.4% |
| Kevin Durant REB over 8.5 (9+) | OKC @ HOU | draftkings | 8.90 | 7.43 | 4.49 | 22.3% | 10.5% | 13.5% | +19.7% | +98.3% | 0.6% |
| Shai Gilgeous-Alexander AST over 10.5 (11+) | OKC @ HOU | draftkings | 18.20 | 15.22 | 9.19 | 10.9% | 5.1% | 6.6% | +19.6% | +98.1% | 0.3% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 21.00 | 18.38 | 11.91 | 8.4% | 4.5% | 5.4% | +14.2% | +76.3% | 0.2% |
| Shai Gilgeous-Alexander AST over 8.5 (9+) | OKC @ HOU | draftkings | 6.66 | 5.89 | 3.87 | 25.9% | 14.0% | 17.0% | +13.2% | +72.3% | 0.6% |
| Kingston Flemings AST over 6.5 (7+) | ATL @ NOP | draftkings | 12.20 | 10.79 | 7.10 | 14.1% | 7.7% | 9.3% | +13.1% | +71.8% | 0.3% |
| Damian Lillard AST over 10.5 (11+) | POR @ UTA | draftkings | 21.00 | 18.62 | 12.29 | 8.1% | 4.5% | 5.4% | +12.8% | +70.9% | 0.2% |
| Damian Lillard AST over 8.5 (9+) | POR @ UTA | draftkings | 8.10 | 7.19 | 4.76 | 21.0% | 11.5% | 13.9% | +12.6% | +70.2% | 0.4% |
| Jabari Smith Jr. REB over 12.5 (13+) | OKC @ HOU | draftkings | 29.00 | 25.84 | 17.17 | 5.8% | 3.2% | 3.9% | +12.3% | +68.9% | 0.1% |
| Amen Thompson AST over 6.5 (7+) | OKC @ HOU | draftkings | 4.65 | 4.19 | 2.85 | 35.1% | 20.1% | 23.8% | +10.9% | +63.2% | 0.8% |
| Aday Mara REB over 10.5 (11+) | OKC @ HOU | draftkings | 18.00 | 16.34 | 11.22 | 8.9% | 5.2% | 6.1% | +10.2% | +60.4% | 0.1% |
| Aday Mara REB over 8.5 (9+) | OKC @ HOU | draftkings | 7.60 | 6.92 | 4.78 | 20.9% | 12.3% | 14.4% | +9.8% | +59.0% | 0.4% |
| Jrue Holiday AST over 8.5 (9+) | POR @ UTA | draftkings | 7.50 | 6.93 | 4.92 | 20.3% | 12.5% | 14.4% | +8.2% | +52.3% | 0.3% |
| Jrue Holiday AST over 10.5 (11+) | POR @ UTA | draftkings | 18.40 | 17.06 | 12.16 | 8.2% | 5.1% | 5.9% | +7.9% | +51.3% | 0.1% |
| Cameron Boozer REB over 14.5 (15+) | SAC @ MEM | draftkings | 13.00 | 12.20 | 8.89 | 11.2% | 7.2% | 8.2% | +6.6% | +46.2% | 0.1% |
| Dylan Harper REB over 8.5 (9+) | MIN @ SAS | draftkings | 10.20 | 9.59 | 7.03 | 14.2% | 9.2% | 10.4% | +6.3% | +45.0% | 0.2% |
| De'Andre Hunter REB over 8.5 (9+) | SAC @ MEM | draftkings | 10.40 | 9.85 | 7.32 | 13.7% | 9.0% | 10.2% | +5.6% | +42.0% | 0.1% |
| Kingston Flemings AST over 4.5 (5+) | ATL @ NOP | draftkings | 3.98 | 3.77 | 2.81 | 35.6% | 23.5% | 26.5% | +5.5% | +41.6% | 0.5% |
| Dejounte Murray AST over 10.5 (11+) | ATL @ NOP | draftkings | 12.20 | 11.59 | 8.66 | 11.6% | 7.7% | 8.6% | +5.3% | +40.9% | 0.1% |
| Trey Murphy III REB over 8.5 (9+) | ATL @ NOP | draftkings | 11.00 | 10.45 | 7.81 | 12.8% | 8.5% | 9.6% | +5.3% | +40.8% | 0.1% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Adem Bona REB under 6.5 | PHI @ CHA | draftkings | 1.99 | Jaylen Brown | 68.0% | 79.8% | +7.5% |
| Adem Bona PR under 14.5 | PHI @ CHA | draftkings | 1.77 | Jaylen Brown | 68.2% | 87.4% | +5.6% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. REB over 7.5 (8+) | OKC @ HOU | draftkings | 3.50 | 3.21 | 2.24 | 44.6% | 26.7% | 31.2% | +9.1% | +56.1% | 0.9% |
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.08 | 1.92 | 1.37 | 72.9% | 45.1% | 52.1% | +8.3% | +51.5% | 1.9% |
| AJ Green 3PM under 1.5 | CLE @ MIL | draftkings | 2.32 | 2.14 | 1.52 | 65.8% | 40.3% | 46.7% | +8.3% | +52.8% | 1.6% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 1.93 | 1.80 | 1.29 | 77.6% | 48.4% | 55.7% | +7.7% | +50.1% | 2.0% |
| Amen Thompson AST over 5.5 (6+) | OKC @ HOU | draftkings | 2.87 | 2.72 | 2.02 | 49.6% | 32.6% | 36.8% | +5.7% | +42.4% | 0.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| POR @ UTA | Sun 01 Nov 06:00 | 122.0–115.3 | POR 68% | 1.46 / 3.17 | UTA +6.5 | 237.5 | UTA +7.5 covers 52%; o231.5 62% |
| PHI @ CHA | Sun 01 Nov 09:00 | 102.6–111.8 | PHI 26% | 3.84 / 1.35 | CHA -9.5 | 214.5 | CHA -1.5 covers 72%; o214.5 50% |
| ATL @ NOP | Sun 01 Nov 10:00 | 123.8–120.7 | ATL 59% | 1.69 / 2.44 | NOP +3.5 | 244.5 | NOP +4.5 covers 53%; o240.5 58% |
| SAC @ MEM | Sun 01 Nov 11:00 | 115.4–122.8 | SAC 30% | 3.32 / 1.43 | MEM -7.5 | 238.5 | MEM -8.5 covers 47%; o230.5 66% |
| CLE @ MIL | Sun 01 Nov 11:00 | 118.0–113.6 | CLE 62% | 1.60 / 2.66 | MIL +4.5 | 231.5 | MIL +9.5 covers 64%; o235.5 41% |
| MIN @ SAS | Sun 01 Nov 11:00 | 107.7–117.9 | MIN 24% | 4.23 / 1.31 | SAS -10.5 | 225.5 | SAS -12.5 covers 43%; o225.5 50% |
| OKC @ HOU | Sun 01 Nov 11:30 | 112.1–113.1 | OKC 47% | 2.12 / 1.90 | HOU -1.5 | 225.5 | HOU -2.5 covers 47%; o219.5 61% |

### POR @ UTA
Out: Trey Alexander (UTA), Blake Hinson (UTA), Jaren Jackson Jr. (UTA), Jusuf Nurkic (UTA), Ja Morant (POR), Shaedon Sharpe (POR)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Damian Lillard AST over 5.5 (6+) | POR @ UTA | draftkings | 2.15 | 2.12 | 1.73 | 57.8% | 43.6% | 47.1% | +1.3% | +24.3% | 0.3% |
| Jrue Holiday AST over 5.5 (6+) | POR @ UTA | draftkings | 2.17 | 2.15 | 1.78 | 56.2% | 43.3% | 46.5% | +0.9% | +21.9% | 0.2% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 122.0–115.3 | POR 68% | 1.46 / 3.17 | UTA +6.5 | 237.5 | UTA +7.5 covers 52%; o231.5 62% |
| Expected (weighted by chance each plays) | 122.1–115.7 | POR 68% | 1.47 / 3.13 | UTA +6.5 | 237.5 | UTA +7.5 covers 53%; o231.5 62% |
| if Robert Williams III plays | 122.7–115.0 | POR 71% | 1.41 / 3.44 | UTA +7.5 | 237.5 | UTA +7.5 covers 49%; o231.5 62% |
| if Lauri Markkanen plays | 121.6–116.2 | POR 65% | 1.54 / 2.85 | UTA +5.5 | 237.5 | UTA +7.5 covers 56%; o231.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Robert Williams III (POR) | Questionable | 55% | 21.0 | 8.6 | 8.0 | 1.5 | 0.2 | 0.7 | 1.7 | 1.1 | 18.1 | full tables below |
| Lauri Markkanen (UTA) | Questionable | 55% | 30.5 | 20.3 | 6.4 | 2.2 | 2.1 | 0.8 | 0.5 | 1.6 | 28.8 | full tables below |
| Chris Youngblood (POR) | Questionable | 55% | 9.9 | 3.6 | 1.4 | 0.8 | 0.5 | 0.3 | 0.2 | 0.5 | 5.8 | small |

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 98% | 34.7<br><sub>23,38,33,32</sub> | 28.3<br><sub>18,26,23,24</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>10,7,4,9</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>4,6,9,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,1,4,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.7 | 4.2 | 43.0 |
| Damian Lillard | 98% | 33.3<br><sub>24,33,31,30</sub> | 21.8<br><sub>25,19,21,9</sub> | 23.5 · –<br><sub>o 44% · u 56%</sub> | 4.4<br><sub>3,5,5,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.4<br><sub>6,2,4,2</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>6,2,4,1</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.3 | 2.5 | 32.6 |
| Jrue Holiday | 98% | 31.5<br><sub>21,26,30,24</sub> | 16.4<br><sub>8,12,22,6</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 4.9<br><sub>4,1,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>1,8,3,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>0,3,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.3 | 2.6 | 27.5 |
| Toumani Camara | 98% | 30.8<br><sub>23,27,24,26</sub> | 13.0<br><sub>18,19,12,13</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>2,3,1,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>3,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>4,5,4,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.5 | 1.5 | 19.8 |
| Donovan Clingan | 98% | 28.4<br><sub>21,21,26,29</sub> | 12.5<br><sub>11,8,9,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 11.6<br><sub>7,10,10,8</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3<br><sub>2,0,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 2.4 | 1.4 | 26.4 |
| Sidy Cissoko | 96% | 25.7<br><sub>25,26,20,19</sub> | 7.1<br><sub>3,15,6,4</sub> |  | 3.8<br><sub>4,7,2,6</sub> |  | 2.4<br><sub>3,1,4,2</sub> |  | 1.0<br><sub>1,2,0,0</sub> |  | 1.1 | 0.5 | 1.1 | 13.3 |
| Scoot Henderson | 98% | 25.5<br><sub>19,21,17,19</sub> | 13.6<br><sub>15,4,2,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,1,2,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>1,2,3,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,0,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 0.2 | 2.6 | 19.9 |
| Micah Potter | 63% | 15.6<br><sub>12,-,-,9</sub> | 6.3<br><sub>4,-,-,1</sub> |  | 4.4<br><sub>3,-,-,2</sub> |  | 1.0<br><sub>0,-,-,0</sub> |  | 0.7<br><sub>0,-,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 11.8 |
| Vit Krejci | 96% | 15.2<br><sub>15,3,7,8</sub> | 5.5<br><sub>1,0,4,2</sub> |  | 2.0<br><sub>2,2,0,0</sub> |  | 1.5<br><sub>3,0,0,1</sub> |  | 0.8<br><sub>0,0,1,0</sub> |  | 0.6 | 0.3 | 0.5 | 9.0 |
| Branden Carlson | 48% | 14.4<br><sub>-,-,-,12</sub> | 5.1<br><sub>-,-,-,2</sub> |  | 3.0<br><sub>-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,0</sub> |  | 0.6 | 1.5 | 1.7 | 8.9 |
| Yang Hansen | 58% | 11.5<br><sub>12,-,-,5</sub> | 4.0<br><sub>5,-,-,3</sub> |  | 2.9<br><sub>3,-,-,2</sub> |  | 0.7<br><sub>0,-,-,1</sub> |  | 0.3<br><sub>1,-,-,1</sub> |  | 0.3 | 0.5 | 0.9 | 7.6 |

</details>

<details><summary>UTA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Keyonte George | 98% | 34.1<br><sub>29,32,33,33,37</sub> | 25.8<br><sub>22,19,24,26,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,1,9,3,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 7.0<br><sub>5,10,10,6,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>4,3,2,0,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 3.9 | 36.6 |
| Ace Bailey | 98% | 34.0<br><sub>24,22,29,34,40</sub> | 16.9<br><sub>12,6,17,17,19</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>5,7,12,10,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 3.0<br><sub>3,2,4,3,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,1,1,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 1.4 | 2.3 | 26.3 |
| Jaxson Hayes | 98% | 30.7<br><sub>26,26,19,-,37</sub> | 10.5<br><sub>5,17,9,-,2</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>5,5,5,-,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>3,2,1,-,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.9 | 1.5 | 1.3 | 19.8 |
| Darryn Peterson | 96% | 30.7<br><sub>31,30,30,26,26</sub> | 15.1<br><sub>9,15,8,14,18</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>4,3,3,7,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.4<br><sub>3,1,2,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>0,1,0,3,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 1.7 | 23.1 |
| Isaiah Collier | 96% | 24.7<br><sub>16,18,13,21,24</sub> | 12.7<br><sub>7,10,6,7,7</sub> |  | 3.4<br><sub>3,2,3,8,7</sub> |  | 7.1<br><sub>3,7,6,8,6</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.3 | 2.6 | 23.1 |
| Josh Okogie | 86% | 23.5<br><sub>8,-,10,21,28</sub> | 5.3<br><sub>0,-,2,0,5</sub> |  | 4.0<br><sub>1,-,2,2,9</sub> |  | 1.4<br><sub>0,-,2,0,3</sub> |  | 0.7<br><sub>0,-,0,0,1</sub> |  | 1.1 | 0.4 | 0.8 | 10.6 |
| Josh Green | 72% | 21.4<br><sub>-,-,3,25,24</sub> | 4.7<br><sub>-,-,0,6,2</sub> |  | 2.3<br><sub>-,-,0,4,2</sub> |  | 1.3<br><sub>-,-,1,1,2</sub> |  | 0.6<br><sub>-,-,0,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 8.2 |
| Brice Sensabaugh | 98% | 20.7<br><sub>14,16,17,9,18</sub> | 12.2<br><sub>2,10,7,11,16</sub> |  | 3.0<br><sub>2,3,6,2,3</sub> |  | 1.9<br><sub>1,2,1,0,1</sub> |  | 1.6<br><sub>0,2,1,3,4</sub> |  | 0.6 | 0.2 | 1.7 | 17.1 |
| Mo Bamba | 52% | 19.4<br><sub>-,-,-,29,16</sub> | 6.9<br><sub>-,-,-,14,8</sub> |  | 6.8<br><sub>-,-,-,7,4</sub> |  | 0.9<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.4 | 1.0 | 14.7 |
| Svi Mykhailiuk | 88% | 18.7<br><sub>19,21,14,13,15</sub> | 7.0<br><sub>10,3,2,0,3</sub> |  | 2.2<br><sub>1,4,3,1,2</sub> |  | 1.5<br><sub>2,1,0,0,1</sub> |  | 1.1<br><sub>2,0,0,0,1</sub> |  | 0.6 | 0.1 | 0.8 | 10.7 |
| Kyle Filipowski | 58% | 14.8<br><sub>9,8,-,8,-</sub> | 7.9<br><sub>3,0,-,0,-</sub> |  | 4.7<br><sub>0,1,-,1,-</sub> |  | 1.8<br><sub>0,0,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.7 | 0.3 | 1.2 | 14.4 |
| Tony Bradley | 48% | 9.7<br><sub>-,-,-,6,-</sub> | 3.5<br><sub>-,-,-,2,-</sub> |  | 3.0<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.6 | 7.0 |

</details>

<details><summary>if Lauri Markkanen plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija (POR) | 98% | 34.6<br><sub>23,38,33,32</sub> | 28.4<br><sub>18,26,23,24</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.3<br><sub>10,7,4,9</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 7.3<br><sub>4,6,9,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,1,4,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.7 | 4.2 | 43.0 |
| Damian Lillard (POR) | 98% | 33.2<br><sub>24,33,31,30</sub> | 21.7<br><sub>25,19,21,9</sub> | 23.5 · –<br><sub>o 44% · u 56%</sub> | 4.3<br><sub>3,5,5,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.4<br><sub>6,2,4,2</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.9<br><sub>6,2,4,1</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.1 | 0.3 | 2.5 | 32.4 |
| Jrue Holiday (POR) | 98% | 31.4<br><sub>21,26,30,24</sub> | 16.3<br><sub>8,12,22,6</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>4,1,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>1,8,3,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.5<br><sub>0,3,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.3 | 2.6 | 27.3 |
| Toumani Camara (POR) | 98% | 30.8<br><sub>23,27,24,26</sub> | 13.0<br><sub>18,19,12,13</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>2,3,1,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.0<br><sub>3,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.4<br><sub>4,5,4,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.5 | 1.5 | 19.9 |
| Donovan Clingan (POR) | 98% | 28.4<br><sub>21,21,26,29</sub> | 12.6<br><sub>11,8,9,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 11.6<br><sub>7,10,10,8</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3<br><sub>2,0,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 2.4 | 1.4 | 26.5 |
| Sidy Cissoko (POR) | 96% | 25.8<br><sub>25,26,20,19</sub> | 7.2<br><sub>3,15,6,4</sub> |  | 3.8<br><sub>4,7,2,6</sub> |  | 2.4<br><sub>3,1,4,2</sub> |  | 1.0<br><sub>1,2,0,0</sub> |  | 1.1 | 0.5 | 1.1 | 13.4 |
| Scoot Henderson (POR) | 98% | 25.5<br><sub>19,21,17,19</sub> | 13.5<br><sub>15,4,2,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.9<br><sub>2,1,2,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.4<br><sub>1,2,3,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.7<br><sub>1,0,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.3 | 0.2 | 2.6 | 19.8 |
| Micah Potter (POR) | 63% | 15.7<br><sub>12,-,-,9</sub> | 6.3<br><sub>4,-,-,1</sub> |  | 4.4<br><sub>3,-,-,2</sub> |  | 1.0<br><sub>0,-,-,0</sub> |  | 0.7<br><sub>0,-,-,0</sub> |  | 0.5 | 0.4 | 1.0 | 11.8 |
| Vit Krejci (POR) | 96% | 15.2<br><sub>15,3,7,8</sub> | 5.6<br><sub>1,0,4,2</sub> |  | 2.0<br><sub>2,2,0,0</sub> |  | 1.4<br><sub>3,0,0,1</sub> |  | 0.8<br><sub>0,0,1,0</sub> |  | 0.6 | 0.3 | 0.6 | 9.0 |
| Branden Carlson (POR) | 48% | 14.4<br><sub>-,-,-,12</sub> | 5.0<br><sub>-,-,-,2</sub> |  | 3.0<br><sub>-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,0</sub> |  | 0.6 | 1.5 | 1.8 | 8.9 |
| Yang Hansen (POR) | 58% | 11.4<br><sub>12,-,-,5</sub> | 3.9<br><sub>5,-,-,3</sub> |  | 2.9<br><sub>3,-,-,2</sub> |  | 0.7<br><sub>0,-,-,1</sub> |  | 0.3<br><sub>1,-,-,1</sub> |  | 0.3 | 0.5 | 0.9 | 7.5 |
| Keyonte George (UTA) | 98% | 33.1<br><sub>29,32,33,33,37</sub> | 23.3<br><sub>22,19,24,26,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>3,1,9,3,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 6.5<br><sub>5,10,10,6,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>4,3,2,0,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 3.5 | 33.5 |
| Ace Bailey (UTA) | 98% | 32.3<br><sub>24,22,29,34,40</sub> | 14.6<br><sub>12,6,17,17,19</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>5,7,12,10,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.6<br><sub>3,2,4,3,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.9<br><sub>2,1,1,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 1.3 | 1.9 | 23.3 |
| Lauri Markkanen (UTA) | 100% | 30.5<br><sub>36,34,38,6,-</sub> | 20.3<br><sub>18,16,28,2,-</sub> | 21.5 · – | 6.4<br><sub>9,6,7,0,-</sub> | 6.5 | 2.2<br><sub>3,3,1,0,-</sub> | 1.5 | 2.1<br><sub>1,4,5,0,-</sub> | 2.5 | 0.8 | 0.5 | 1.6 | 28.8 |
| Darryn Peterson (UTA) | 96% | 28.6<br><sub>31,30,30,26,26</sub> | 12.7<br><sub>9,15,8,14,18</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.4<br><sub>4,3,3,7,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 2.9<br><sub>3,1,2,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.1<br><sub>0,1,0,3,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.0 | 0.3 | 1.6 | 20.1 |
| Jaxson Hayes (UTA) | 98% | 28.0<br><sub>26,26,19,-,37</sub> | 9.4<br><sub>5,17,9,-,2</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 6.8<br><sub>5,5,5,-,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.0<br><sub>3,2,1,-,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.8 | 1.4 | 1.1 | 18.2 |
| Isaiah Collier (UTA) | 96% | 21.9<br><sub>16,18,13,21,24</sub> | 10.2<br><sub>7,10,6,7,7</sub> |  | 3.0<br><sub>3,2,3,8,7</sub> |  | 6.3<br><sub>3,7,6,8,6</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.3 | 2.2 | 19.6 |
| Josh Okogie (UTA) | 86% | 20.0<br><sub>8,-,10,21,28</sub> | 4.4<br><sub>0,-,2,0,5</sub> |  | 3.5<br><sub>1,-,2,2,9</sub> |  | 1.2<br><sub>0,-,2,0,3</sub> |  | 0.5<br><sub>0,-,0,0,1</sub> |  | 1.0 | 0.3 | 0.7 | 9.1 |
| Josh Green (UTA) | 72% | 18.4<br><sub>-,-,3,25,24</sub> | 4.0<br><sub>-,-,0,6,2</sub> |  | 2.0<br><sub>-,-,0,4,2</sub> |  | 1.1<br><sub>-,-,1,1,2</sub> |  | 0.5<br><sub>-,-,0,1,0</sub> |  | 0.8 | 0.2 | 0.7 | 7.2 |
| Brice Sensabaugh (UTA) | 98% | 18.1<br><sub>14,16,17,9,18</sub> | 9.9<br><sub>2,10,7,11,16</sub> |  | 2.6<br><sub>2,3,6,2,3</sub> |  | 1.7<br><sub>1,2,1,0,1</sub> |  | 1.3<br><sub>0,2,1,3,4</sub> |  | 0.6 | 0.2 | 1.4 | 14.2 |
| Mo Bamba (UTA) | 52% | 17.2<br><sub>-,-,-,29,16</sub> | 6.0<br><sub>-,-,-,14,8</sub> |  | 6.0<br><sub>-,-,-,7,4</sub> |  | 0.8<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.4 | 1.3 | 0.8 | 12.8 |
| Svi Mykhailiuk (UTA) | 88% | 15.9<br><sub>19,21,14,13,15</sub> | 5.3<br><sub>10,3,2,0,3</sub> |  | 1.9<br><sub>1,4,3,1,2</sub> |  | 1.2<br><sub>2,1,0,0,1</sub> |  | 0.8<br><sub>2,0,0,0,1</sub> |  | 0.5 | 0.1 | 0.6 | 8.4 |
| Kyle Filipowski (UTA) | 58% | 12.6<br><sub>9,8,-,8,-</sub> | 6.2<br><sub>3,0,-,0,-</sub> |  | 4.0<br><sub>0,1,-,1,-</sub> |  | 1.4<br><sub>0,0,-,0,-</sub> |  | 0.5<br><sub>0,0,-,0,-</sub> |  | 0.6 | 0.3 | 1.0 | 11.6 |
| Tony Bradley (UTA) | 48% | 8.2<br><sub>-,-,-,6,-</sub> | 2.8<br><sub>-,-,-,2,-</sub> |  | 2.6<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.5 | 5.9 |

</details>

<details><summary>if Robert Williams III plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija (POR) | 98% | 34.1<br><sub>23,38,33,32</sub> | 27.2<br><sub>18,26,23,24</sub> | 24.5 · –<br><sub>o 50% · u 50%</sub> | 7.2<br><sub>10,7,4,9</sub> | 7.5<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>4,6,9,7</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>2,1,4,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 0.9 | 0.7 | 4.1 | 41.9 |
| Damian Lillard (POR) | 98% | 32.3<br><sub>24,33,31,30</sub> | 19.3<br><sub>25,19,21,9</sub> | 23.5 · –<br><sub>o 44% · u 56%</sub> | 4.2<br><sub>3,5,5,2</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 6.2<br><sub>6,2,4,2</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.7<br><sub>6,2,4,1</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 1.2 | 0.3 | 2.4 | 29.7 |
| Jrue Holiday (POR) | 98% | 30.3<br><sub>21,26,30,24</sub> | 15.4<br><sub>8,12,22,6</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 4.7<br><sub>4,1,4,6</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 6.2<br><sub>1,8,3,4</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>0,3,2,2</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.3 | 2.3 | 26.2 |
| Toumani Camara (POR) | 98% | 29.7<br><sub>23,27,24,26</sub> | 12.8<br><sub>18,19,12,13</sub> | 12.5 · –<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>2,3,1,2</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.1<br><sub>3,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 2.3<br><sub>4,5,4,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.2 | 0.5 | 1.4 | 19.5 |
| Donovan Clingan (POR) | 98% | 27.2<br><sub>21,21,26,29</sub> | 12.0<br><sub>11,8,9,11</sub> | 11.5 · –<br><sub>o 48% · u 52%</sub> | 10.9<br><sub>7,10,10,8</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>2,3,1,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2<br><sub>2,0,2,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.6 | 2.4 | 1.4 | 25.2 |
| Scoot Henderson (POR) | 98% | 23.8<br><sub>19,21,17,19</sub> | 12.7<br><sub>15,4,2,9</sub> | 13.5 · –<br><sub>o 48% · u 52%</sub> | 2.7<br><sub>2,1,2,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.2<br><sub>1,2,3,0</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.6<br><sub>1,0,0,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.1 | 0.2 | 2.4 | 18.5 |
| Sidy Cissoko (POR) | 96% | 22.5<br><sub>25,26,20,19</sub> | 6.6<br><sub>3,15,6,4</sub> |  | 3.2<br><sub>4,7,2,6</sub> |  | 2.1<br><sub>3,1,4,2</sub> |  | 0.8<br><sub>1,2,0,0</sub> |  | 0.9 | 0.4 | 1.1 | 12.0 |
| Robert Williams III (POR) | 100% | 21.0<br><sub>15,18,21,-</sub> | 8.6<br><sub>2,13,14,-</sub> | 6.5 · – | 8.0<br><sub>10,6,10,-</sub> | 6.5 | 1.5<br><sub>1,0,1,-</sub> |  | 0.2<br><sub>0,0,0,-</sub> |  | 0.7 | 1.7 | 1.1 | 18.1 |
| Micah Potter (POR) | 63% | 13.1<br><sub>12,-,-,9</sub> | 5.7<br><sub>4,-,-,1</sub> |  | 3.6<br><sub>3,-,-,2</sub> |  | 0.9<br><sub>0,-,-,0</sub> |  | 0.6<br><sub>0,-,-,0</sub> |  | 0.4 | 0.3 | 0.8 | 10.2 |
| Vit Krejci (POR) | 96% | 12.7<br><sub>15,3,7,8</sub> | 4.8<br><sub>1,0,4,2</sub> |  | 1.7<br><sub>2,2,0,0</sub> |  | 1.2<br><sub>3,0,0,1</sub> |  | 0.7<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.5 | 7.7 |
| Branden Carlson (POR) | 48% | 12.3<br><sub>-,-,-,12</sub> | 4.4<br><sub>-,-,-,2</sub> |  | 2.5<br><sub>-,-,-,2</sub> |  | 0.8<br><sub>-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,0</sub> |  | 0.5 | 1.3 | 1.8 | 7.8 |
| Yang Hansen (POR) | 58% | 8.1<br><sub>12,-,-,5</sub> | 3.0<br><sub>5,-,-,3</sub> |  | 2.0<br><sub>3,-,-,2</sub> |  | 0.5<br><sub>0,-,-,1</sub> |  | 0.2<br><sub>1,-,-,1</sub> |  | 0.2 | 0.3 | 0.7 | 5.5 |
| Keyonte George (UTA) | 98% | 34.1<br><sub>29,32,33,33,37</sub> | 25.9<br><sub>22,19,24,26,31</sub> | 22.5 · –<br><sub>o 51% · u 49%</sub> | 3.8<br><sub>3,1,9,3,4</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 7.0<br><sub>5,10,10,6,3</sub> | 6.5<br><sub>o 47% · u 53%</sub> | 2.5<br><sub>4,3,2,0,5</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.2 | 3.9 | 36.6 |
| Ace Bailey (UTA) | 98% | 34.0<br><sub>24,22,29,34,40</sub> | 16.8<br><sub>12,6,17,17,19</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>5,7,12,10,6</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>3,2,4,3,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.1<br><sub>2,1,1,3,1</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 1.4 | 2.3 | 26.2 |
| Jaxson Hayes (UTA) | 98% | 30.7<br><sub>26,26,19,-,37</sub> | 10.5<br><sub>5,17,9,-,2</sub> | 8.5 · –<br><sub>o 52% · u 48%</sub> | 7.1<br><sub>5,5,5,-,11</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 2.2<br><sub>3,2,1,-,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.1<br><sub>0,0,0,-,0</sub> |  | 0.9 | 1.5 | 1.3 | 19.8 |
| Darryn Peterson (UTA) | 96% | 30.7<br><sub>31,30,30,26,26</sub> | 15.0<br><sub>9,15,8,14,18</sub> | 14.5 · –<br><sub>o 46% · u 54%</sub> | 4.7<br><sub>4,3,3,7,5</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.4<br><sub>3,1,2,4,3</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.2<br><sub>0,1,0,3,3</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.1 | 0.4 | 1.7 | 23.1 |
| Isaiah Collier (UTA) | 96% | 24.7<br><sub>16,18,13,21,24</sub> | 12.7<br><sub>7,10,6,7,7</sub> |  | 3.3<br><sub>3,2,3,8,7</sub> |  | 7.1<br><sub>3,7,6,8,6</sub> |  | 0.6<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.3 | 2.6 | 23.1 |
| Josh Okogie (UTA) | 86% | 23.5<br><sub>8,-,10,21,28</sub> | 5.3<br><sub>0,-,2,0,5</sub> |  | 4.0<br><sub>1,-,2,2,9</sub> |  | 1.4<br><sub>0,-,2,0,3</sub> |  | 0.6<br><sub>0,-,0,0,1</sub> |  | 1.1 | 0.4 | 0.8 | 10.6 |
| Josh Green (UTA) | 72% | 21.4<br><sub>-,-,3,25,24</sub> | 4.7<br><sub>-,-,0,6,2</sub> |  | 2.3<br><sub>-,-,0,4,2</sub> |  | 1.3<br><sub>-,-,1,1,2</sub> |  | 0.6<br><sub>-,-,0,1,0</sub> |  | 0.9 | 0.2 | 0.8 | 8.2 |
| Brice Sensabaugh (UTA) | 98% | 20.7<br><sub>14,16,17,9,18</sub> | 12.1<br><sub>2,10,7,11,16</sub> |  | 3.0<br><sub>2,3,6,2,3</sub> |  | 1.9<br><sub>1,2,1,0,1</sub> |  | 1.6<br><sub>0,2,1,3,4</sub> |  | 0.6 | 0.2 | 1.7 | 17.1 |
| Mo Bamba (UTA) | 52% | 19.4<br><sub>-,-,-,29,16</sub> | 6.9<br><sub>-,-,-,14,8</sub> |  | 6.8<br><sub>-,-,-,7,4</sub> |  | 0.9<br><sub>-,-,-,1,1</sub> |  | 0.4<br><sub>-,-,-,0,0</sub> |  | 0.5 | 1.4 | 1.0 | 14.7 |
| Svi Mykhailiuk (UTA) | 88% | 18.7<br><sub>19,21,14,13,15</sub> | 7.0<br><sub>10,3,2,0,3</sub> |  | 2.2<br><sub>1,4,3,1,2</sub> |  | 1.4<br><sub>2,1,0,0,1</sub> |  | 1.0<br><sub>2,0,0,0,1</sub> |  | 0.6 | 0.1 | 0.8 | 10.6 |
| Kyle Filipowski (UTA) | 58% | 14.8<br><sub>9,8,-,8,-</sub> | 7.8<br><sub>3,0,-,0,-</sub> |  | 4.7<br><sub>0,1,-,1,-</sub> |  | 1.8<br><sub>0,0,-,0,-</sub> |  | 0.6<br><sub>0,0,-,0,-</sub> |  | 0.7 | 0.3 | 1.2 | 14.4 |
| Tony Bradley (UTA) | 48% | 9.7<br><sub>-,-,-,6,-</sub> | 3.5<br><sub>-,-,-,2,-</sub> |  | 3.0<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.3 | 0.4 | 0.6 | 7.0 |

</details>


### PHI @ CHA
Out: Kon Knueppel (CHA), Coby White (CHA), Grant Williams (CHA), Dominick Barlow (PHI), Joel Embiid (PHI), Ariel Hukporti (PHI), LeBron James (PHI)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller 3PM under 3.5 | PHI @ CHA | draftkings | 2.06 | 2.04 | 1.66 | 60.1% | 45.4% | 49.0% | +1.0% | +23.8% | 0.2% |
| Naz Reid PA under 20.5 | PHI @ CHA | draftkings | 1.91 | 1.90 | 1.57 | 63.7% | 48.9% | 52.6% | +0.5% | +21.7% | 0.1% |
| Naz Reid 3PM under 2.5 | PHI @ CHA | draftkings | 1.89 | 1.88 | 1.56 | 64.2% | 49.4% | 53.1% | +0.5% | +21.4% | 0.1% |
| Naz Reid PTS under 18.5 | PHI @ CHA | draftkings | 1.85 | 1.85 | 1.54 | 65.0% | 50.4% | 54.0% | +0.2% | +20.6% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 102.6–111.8 | PHI 26% | 3.84 / 1.35 | CHA -9.5 | 214.5 | CHA -1.5 covers 72%; o214.5 50% |
| Expected (weighted by chance each plays) | 102.5–109.7 | PHI 30% | 3.30 / 1.43 | CHA -7.5 | 212.5 | CHA -1.5 covers 67%; o214.5 45% |
| if Jaylen Brown plays | 102.5–108.1 | PHI 35% | 2.88 / 1.53 | CHA -5.5 | 210.5 | CHA -1.5 covers 63%; o214.5 41% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tacko Fall (PHI) | Questionable | 55% | 8.6 | 3.8 | 1.6 | 0.8 | 0.2 | 0.3 | 0.2 | 0.4 | 6.1 | small |
| Jabari Walker (PHI) | Questionable | 55% | 18.8 | 7.3 | 4.2 | 0.9 | 0.7 | 0.7 | 0.2 | 0.8 | 12.5 | small |
| Jaylen Brown (PHI) | Questionable | 55% | 37.1 | 27.0 | 6.8 | 5.0 | 2.0 | 1.2 | 0.5 | 3.9 | 38.9 | full tables below |

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.1<br><sub>42,36,34,36,38</sub> | 32.0<br><sub>32,26,29,27,27</sub> | 28.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,4,5,5,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>6,4,4,4,4</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,4,1,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.7 | 0.6 | 3.0 | 42.7 |
| VJ Edgecombe | 84% | 36.5<br><sub>33,30,-,29,36</sub> | 19.6<br><sub>11,17,-,8,13</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 6.7<br><sub>7,13,-,7,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>6,2,-,2,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>1,5,-,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.5 | 2.3 | 30.9 |
| Anfernee Simons | 96% | 34.1<br><sub>17,20,27,27,31</sub> | 18.7<br><sub>2,4,5,20,21</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.4<br><sub>3,1,3,3,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 3.3<br><sub>0,2,3,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>0,1,1,6,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.9 | 25.4 |
| Dean Wade | 88% | 30.4<br><sub>-,28,37,17,27</sub> | 7.0<br><sub>-,7,7,0,0</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.1<br><sub>-,2,5,1,2</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>-,0,1,1,1</sub> |  | 1.0<br><sub>-,2,1,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.2 | 0.8 | 12.6 |
| Kentavious Caldwell-Pope | 98% | 28.3<br><sub>25,28,31,21,21</sub> | 9.9<br><sub>3,12,7,4,5</sub> |  | 3.0<br><sub>3,2,3,2,3</sub> |  | 2.9<br><sub>2,1,3,1,3</sub> |  | 1.2<br><sub>1,4,1,0,1</sub> |  | 1.1 | 0.2 | 1.1 | 15.8 |
| Adem Bona | 97% | 22.5<br><sub>14,10,25,4,14</sub> | 7.0<br><sub>2,0,6,1,0</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 5.4<br><sub>2,1,13,1,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.8<br><sub>0,1,1,0,0</sub> |  | 0.1<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.1 | 1.4 | 13.2 |
| Rayan Rupert | 25% | 22.3<br><sub>-,-,-,-,-</sub> | 8.7<br><sub>-,-,-,-,-</sub> |  | 4.2<br><sub>-,-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 1.1 | 0.2 | 1.6 | 14.7 |
| Justin Edwards | 38% | 18.9<br><sub>-,1,-,-,-</sub> | 8.5<br><sub>-,0,-,-,-</sub> |  | 2.4<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.8 | 0.2 | 0.9 | 12.1 |
| Labaron Philon Jr. | 58% | 17.8<br><sub>-,4,13,-,6</sub> | 5.8<br><sub>-,0,5,-,2</sub> |  | 2.1<br><sub>-,0,2,-,2</sub> |  | 1.1<br><sub>-,0,1,-,0</sub> |  | 0.7<br><sub>-,0,1,-,0</sub> |  | 0.6 | 0.2 | 0.7 | 9.0 |
| Caleb Love | 38% | 14.7<br><sub>-,1,-,-,-</sub> | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.9<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.3 | 0.5 | 2.2 |

</details>

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 33.9<br><sub>23,36,36,38,37</sub> | 24.1<br><sub>6,34,39,31,19</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>2,8,6,12,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>0,4,1,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.1<br><sub>1,3,5,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.6 | 3.0 | 32.7 |
| Dennis Schroder | 98% | 31.8<br><sub>20,38,36,34,29</sub> | 13.9<br><sub>4,25,8,14,8</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,6,2,4,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.4<br><sub>3,4,5,5,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.9 | 0.2 | 2.6 | 22.8 |
| Moussa Diabate | 98% | 29.8<br><sub>21,22,35,35,31</sub> | 9.0<br><sub>5,4,11,9,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 10.4<br><sub>8,5,17,9,12</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>1,2,3,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.0 | 1.5 | 21.7 |
| Naz Reid | 98% | 27.8<br><sub>25,37,29,13,31</sub> | 16.8<br><sub>17,23,18,7,12</sub> | 18.5 · –<br><sub>o 45% · u 55%</sub> | 7.7<br><sub>6,9,12,6,11</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,0,1,0,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>3,5,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.9 | 2.1 | 26.6 |
| Grayson Allen | 96% | 27.4<br><sub>20,34,28,30,21</sub> | 14.6<br><sub>11,20,15,9,5</sub> |  | 3.1<br><sub>2,3,2,5,3</sub> |  | 3.0<br><sub>3,5,1,2,2</sub> |  | 2.4<br><sub>3,4,2,2,1</sub> |  | 0.9 | 0.3 | 1.9 | 20.7 |
| Sion James | 98% | 26.8<br><sub>24,26,29,23,29</sub> | 7.0<br><sub>3,0,5,5,6</sub> | 5.5 · –<br><sub>o 55% · u 45%</sub> | 4.2<br><sub>2,5,2,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>5,5,3,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>1,0,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.2 | 1.1 | 13.9 |
| Royce O'Neale | 98% | 19.7<br><sub>17,11,7,34,17</sub> | 6.5<br><sub>6,0,0,9,7</sub> |  | 3.5<br><sub>2,1,0,4,3</sub> |  | 1.2<br><sub>0,0,1,0,1</sub> |  | 1.2<br><sub>2,0,0,3,2</sub> |  | 0.6 | 0.3 | 0.8 | 11.2 |
| Ryan Kalkbrenner | 98% | 16.3<br><sub>19,23,13,13,15</sub> | 5.2<br><sub>6,6,6,1,2</sub> |  | 4.4<br><sub>7,5,4,1,4</sub> |  | 0.9<br><sub>1,2,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.2 | 0.7 | 10.5 |
| Tidjane Salaun | 88% | 14.2<br><sub>23,10,16,12,9</sub> | 5.3<br><sub>11,3,5,2,6</sub> |  | 3.4<br><sub>5,3,5,2,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.6<br><sub>1,1,1,0,2</sub> |  | 0.3 | 0.2 | 0.7 | 9.4 |
| Christian Anderson | 96% | 13.4<br><sub>16,3,11,9,14</sub> | 5.5<br><sub>2,0,3,2,4</sub> |  | 1.9<br><sub>0,1,4,0,3</sub> |  | 1.6<br><sub>2,0,1,1,3</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.0 |
| Liam McNeeley | 52% | 9.6<br><sub>12,-,-,-,3</sub> | 3.5<br><sub>4,-,-,-,0</sub> |  | 2.0<br><sub>4,-,-,-,2</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 6.1 |
| PJ Hall | 52% | 8.6<br><sub>10,-,-,-,2</sub> | 3.3<br><sub>0,-,-,-,0</sub> |  | 3.0<br><sub>1,-,-,-,1</sub> |  | 0.5<br><sub>3,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.5 | 0.6 | 6.8 |
| Hannes Steinbach | 52% | 7.4<br><sub>12,-,-,-,2</sub> | 2.9<br><sub>6,-,-,-,0</sub> |  | 1.9<br><sub>5,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.2 |

</details>

<details><summary>if Jaylen Brown plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller (CHA) | 98% | 34.0<br><sub>23,36,36,38,37</sub> | 23.6<br><sub>6,34,39,31,19</sub> | 26.5 · –<br><sub>o 47% · u 53%</sub> | 5.7<br><sub>2,8,6,12,7</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 2.9<br><sub>0,4,1,3,2</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 3.1<br><sub>1,3,5,3,3</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.1 | 0.7 | 3.0 | 32.2 |
| Dennis Schroder (CHA) | 98% | 31.8<br><sub>20,38,36,34,29</sub> | 13.6<br><sub>4,25,8,14,8</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,6,2,4,2</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 5.4<br><sub>3,4,5,5,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.3<br><sub>0,3,0,2,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.2 | 2.6 | 22.5 |
| Moussa Diabate (CHA) | 98% | 29.7<br><sub>21,22,35,35,31</sub> | 8.8<br><sub>5,4,11,9,10</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 10.4<br><sub>8,5,17,9,12</sub> | 10.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>1,2,3,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 1.0 | 1.5 | 21.5 |
| Naz Reid (CHA) | 98% | 27.7<br><sub>25,37,29,13,31</sub> | 16.6<br><sub>17,23,18,7,12</sub> | 18.5 · –<br><sub>o 45% · u 55%</sub> | 7.7<br><sub>6,9,12,6,11</sub> | 8.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>2,0,1,0,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 2.1<br><sub>3,5,2,1,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.9 | 2.2 | 26.4 |
| Grayson Allen (CHA) | 96% | 27.4<br><sub>20,34,28,30,21</sub> | 14.4<br><sub>11,20,15,9,5</sub> |  | 3.1<br><sub>2,3,2,5,3</sub> |  | 2.9<br><sub>3,5,1,2,2</sub> |  | 2.4<br><sub>3,4,2,2,1</sub> |  | 0.9 | 0.3 | 1.9 | 20.5 |
| Sion James (CHA) | 98% | 26.9<br><sub>24,26,29,23,29</sub> | 6.9<br><sub>3,0,5,5,6</sub> | 5.5 · –<br><sub>o 55% · u 45%</sub> | 4.1<br><sub>2,5,2,2,5</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 2.7<br><sub>5,5,3,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.0<br><sub>1,0,1,1,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.2 | 1.1 | 13.8 |
| Royce O'Neale (CHA) | 98% | 19.8<br><sub>17,11,7,34,17</sub> | 6.4<br><sub>6,0,0,9,7</sub> |  | 3.5<br><sub>2,1,0,4,3</sub> |  | 1.2<br><sub>0,0,1,0,1</sub> |  | 1.2<br><sub>2,0,0,3,2</sub> |  | 0.6 | 0.3 | 0.8 | 11.2 |
| Ryan Kalkbrenner (CHA) | 98% | 16.3<br><sub>19,23,13,13,15</sub> | 5.2<br><sub>6,6,6,1,2</sub> |  | 4.4<br><sub>7,5,4,1,4</sub> |  | 0.8<br><sub>1,2,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 1.2 | 0.7 | 10.4 |
| Tidjane Salaun (CHA) | 88% | 14.2<br><sub>23,10,16,12,9</sub> | 5.2<br><sub>11,3,5,2,6</sub> |  | 3.4<br><sub>5,3,5,2,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> |  | 0.6<br><sub>1,1,1,0,2</sub> |  | 0.3 | 0.2 | 0.7 | 9.3 |
| Christian Anderson (CHA) | 96% | 13.4<br><sub>16,3,11,9,14</sub> | 5.4<br><sub>2,0,3,2,4</sub> |  | 1.9<br><sub>0,1,4,0,3</sub> |  | 1.6<br><sub>2,0,1,1,3</sub> |  | 0.6<br><sub>0,0,1,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 8.9 |
| Liam McNeeley (CHA) | 52% | 9.6<br><sub>12,-,-,-,3</sub> | 3.5<br><sub>4,-,-,-,0</sub> |  | 2.0<br><sub>4,-,-,-,2</sub> |  | 0.6<br><sub>0,-,-,-,0</sub> |  | 0.3<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 6.1 |
| PJ Hall (CHA) | 52% | 8.5<br><sub>10,-,-,-,2</sub> | 3.2<br><sub>0,-,-,-,0</sub> |  | 3.0<br><sub>1,-,-,-,1</sub> |  | 0.5<br><sub>3,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.1 | 0.4 | 0.6 | 6.7 |
| Hannes Steinbach (CHA) | 52% | 7.3<br><sub>12,-,-,-,2</sub> | 2.9<br><sub>6,-,-,-,0</sub> |  | 1.9<br><sub>5,-,-,-,0</sub> |  | 0.4<br><sub>0,-,-,-,0</sub> |  | 0.1<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.1 |
| Tyrese Maxey (PHI) | 98% | 38.3<br><sub>42,36,34,36,38</sub> | 28.2<br><sub>32,26,29,27,27</sub> | 28.5 · –<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>3,4,5,5,4</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 5.9<br><sub>6,4,4,4,4</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>2,4,1,3,3</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 1.6 | 0.6 | 2.7 | 38.5 |
| Jaylen Brown (PHI) | 100% | 37.1<br><sub>38,35,40,34,-</sub> | 27.0<br><sub>21,27,16,20,-</sub> | 23.5 · – | 6.8<br><sub>8,3,4,10,-</sub> | 6.5 | 5.0<br><sub>4,5,4,2,-</sub> | 4.5 | 2.0<br><sub>1,3,2,1,-</sub> | 1.5 | 1.2 | 0.5 | 3.9 | 38.9 |
| VJ Edgecombe (PHI) | 84% | 35.2<br><sub>33,30,-,29,36</sub> | 14.5<br><sub>11,17,-,8,13</sub> | 16.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>7,13,-,7,8</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,2,-,2,2</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 1.8<br><sub>1,5,-,1,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.4 | 0.4 | 1.8 | 24.9 |
| Anfernee Simons (PHI) | 96% | 30.8<br><sub>17,20,27,27,31</sub> | 13.2<br><sub>2,4,5,20,21</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,1,3,3,2</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 2.5<br><sub>0,2,3,1,1</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 2.3<br><sub>0,1,1,6,5</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.7 | 0.2 | 1.4 | 18.9 |
| Dean Wade (PHI) | 88% | 30.1<br><sub>-,28,37,17,27</sub> | 5.8<br><sub>-,7,7,0,0</sub> | 5.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>-,2,5,1,2</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.2<br><sub>-,0,1,1,1</sub> |  | 0.8<br><sub>-,2,1,0,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.3 | 0.7 | 11.0 |
| Kentavious Caldwell-Pope (PHI) | 98% | 27.1<br><sub>25,28,31,21,21</sub> | 7.8<br><sub>3,12,7,4,5</sub> |  | 3.0<br><sub>3,2,3,2,3</sub> |  | 2.2<br><sub>2,1,3,1,3</sub> |  | 1.0<br><sub>1,4,1,0,1</sub> |  | 1.1 | 0.2 | 0.8 | 12.9 |
| Adem Bona (PHI) | 97% | 18.6<br><sub>14,10,25,4,14</sub> | 4.7<br><sub>2,0,6,1,0</sub> | 6.5 · –<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>2,1,13,1,2</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.5<br><sub>0,1,1,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.0 | 1.0 | 9.7 |
| Rayan Rupert (PHI) | 25% | 18.4<br><sub>-,-,-,-,-</sub> | 6.7<br><sub>-,-,-,-,-</sub> |  | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.9 | 0.2 | 1.2 | 11.4 |
| Justin Edwards (PHI) | 38% | 13.4<br><sub>-,1,-,-,-</sub> | 5.2<br><sub>-,0,-,-,-</sub> |  | 1.7<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.6 | 0.2 | 0.6 | 7.6 |
| Labaron Philon Jr. (PHI) | 58% | 12.1<br><sub>-,4,13,-,6</sub> | 3.8<br><sub>-,0,5,-,2</sub> |  | 1.7<br><sub>-,0,2,-,2</sub> |  | 0.8<br><sub>-,0,1,-,0</sub> |  | 0.4<br><sub>-,0,1,-,0</sub> |  | 0.3 | 0.2 | 0.5 | 6.2 |
| Caleb Love (PHI) | 38% | 9.8<br><sub>-,1,-,-,-</sub> | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 1.6 |

</details>


### ATL @ NOP
Out: Yves Missi (NOP), Jordan Poole (NOP), Mouhamed Gueye (ATL)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 123.8–120.7 | ATL 59% | 1.69 / 2.44 | NOP +3.5 | 244.5 | NOP +4.5 covers 53%; o240.5 58% |
| Expected (weighted by chance each plays) | 124.1–120.6 | ATL 60% | 1.66 / 2.51 | NOP +3.5 | 244.5 | NOP +4.5 covers 53%; o240.5 59% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Wilson (ATL) | Doubtful | 20% | 9.7 | 3.7 | 1.6 | 0.7 | 0.3 | 0.3 | 0.1 | 0.5 | 6.0 | small |
| RayJ Dennis (ATL) | Doubtful | 20% | 7.6 | 2.8 | 1.0 | 1.2 | 0.2 | 0.3 | 0.1 | 0.5 | 5.0 | small |
| Keshon Gilbert (ATL) | Doubtful | 20% | 7.6 | 2.4 | 0.9 | 1.0 | 0.1 | 0.3 | 0.2 | 0.5 | 4.3 | small |
| Zuby Ejiofor (ATL) | Doubtful | 20% | 5.9 | 2.4 | 1.1 | 0.5 | 0.1 | 0.2 | 0.1 | 0.3 | 3.9 | small |

<details><summary>ATL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Johnson | 98% | 35.4<br><sub>29,38,36,36,34</sub> | 21.6<br><sub>19,26,21,12,17</sub> | 22.5 · –<br><sub>o 47% · u 53%</sub> | 9.7<br><sub>7,9,9,9,8</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 7.5<br><sub>8,16,3,11,7</sub> | 8.5<br><sub>o 43% · u 57%</sub> | 1.8<br><sub>0,2,1,2,2</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 1.3 | 0.6 | 3.2 | 38.9 |
| Nickeil Alexander-Walker | 98% | 32.7<br><sub>27,32,29,32,31</sub> | 20.0<br><sub>14,18,12,23,25</sub> | 19.5 · –<br><sub>o 48% · u 52%</sub> | 3.1<br><sub>3,5,2,3,3</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 3.4<br><sub>5,4,3,1,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>2,4,2,5,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.5 | 2.2 | 26.5 |
| Dyson Daniels | 98% | 31.5<br><sub>23,29,28,28,32</sub> | 11.9<br><sub>11,18,4,7,4</sub> | 11.5 · –<br><sub>o 47% · u 53%</sub> | 6.3<br><sub>9,8,0,4,6</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 5.5<br><sub>4,3,4,7,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.5<br><sub>0,1,0,0,0</sub> |  | 2.2 | 0.4 | 1.6 | 23.6 |
| Onyeka Okongwu | 98% | 31.4<br><sub>22,26,29,31,33</sub> | 14.8<br><sub>10,8,11,11,29</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 7.4<br><sub>4,6,9,4,12</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,2,1,4,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.7<br><sub>2,0,1,1,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.1 | 1.0 | 1.4 | 25.1 |
| CJ McCollum | 98% | 29.3<br><sub>22,30,30,20,31</sub> | 18.2<br><sub>13,17,20,13,5</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>1,2,1,2,3</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 3.6<br><sub>2,1,3,1,8</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.5<br><sub>2,1,4,1,0</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.5 | 1.9 | 24.6 |
| Aaron Wiggins | 96% | 24.8<br><sub>22,29,27,24,24</sub> | 11.6<br><sub>19,16,12,10,20</sub> | 12.5 · –<br><sub>o 46% · u 54%</sub> | 3.4<br><sub>1,5,4,4,7</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 2.0<br><sub>1,2,3,3,3</sub> |  | 1.8<br><sub>3,4,2,2,4</sub> | 2.5<br><sub>o 35% · u 65%</sub> | 0.9 | 0.4 | 1.1 | 16.9 |
| Luguentz Dort | 98% | 22.1<br><sub>19,23,21,24,22</sub> | 7.8<br><sub>9,7,11,8,6</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>5,2,2,3,3</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>2,3,1,3,2</sub> |  | 1.2<br><sub>1,1,0,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.2 | 0.7 | 12.1 |
| Kingston Flemings | 96% | 18.4<br><sub>25,15,18,28,16</sub> | 6.6<br><sub>5,2,6,23,2</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 2.6<br><sub>6,1,1,5,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>8,2,4,5,5</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 0.6<br><sub>1,0,0,3,0</sub> |  | 0.7 | 0.3 | 1.3 | 13.1 |
| Jock Landale | 98% | 16.7<br><sub>18,19,18,17,15</sub> | 7.6<br><sub>8,2,8,10,6</sub> |  | 4.5<br><sub>6,4,6,6,10</sub> |  | 1.5<br><sub>4,2,4,0,1</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.4 | 0.5 | 0.8 | 13.7 |
| Corey Kispert | 48% | 9.3<br><sub>10,-,1,-,-</sub> | 4.7<br><sub>11,-,5,-,-</sub> |  | 1.3<br><sub>1,-,0,-,-</sub> |  | 0.8<br><sub>1,-,0,-,-</sub> |  | 0.6<br><sub>3,-,1,-,-</sub> |  | 0.2 | 0.1 | 0.4 | 6.8 |
| Asa Newell | 47% | 8.1<br><sub>8,-,1,-,-</sub> | 3.5<br><sub>3,-,0,-,-</sub> |  | 1.7<br><sub>1,-,1,-,-</sub> |  | 0.5<br><sub>0,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.7 |
| Dorian Finney-Smith | 48% | 7.1<br><sub>8,-,1,-,-</sub> | 2.3<br><sub>3,-,0,-,-</sub> |  | 1.2<br><sub>2,-,0,-,-</sub> |  | 0.5<br><sub>1,-,0,-,-</sub> |  | 0.2<br><sub>1,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |

</details>

<details><summary>NOP players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trey Murphy III | 98% | 34.2<br><sub>32,31,37,30,32</sub> | 17.6<br><sub>11,9,26,6,19</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>4,6,6,1,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 3.3<br><sub>1,3,4,3,3</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 2.7<br><sub>2,1,4,2,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.4 | 0.6 | 1.6 | 26.4 |
| Dejounte Murray | 98% | 32.5<br><sub>34,30,35,30,-</sub> | 17.9<br><sub>23,16,22,10,-</sub> | 17.5 · –<br><sub>o 47% · u 53%</sub> | 6.1<br><sub>3,6,6,8,-</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 6.8<br><sub>7,6,6,5,-</sub> | 5.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>2,0,1,0,-</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.8 | 0.4 | 3.4 | 30.8 |
| Zion Williamson | 96% | 32.2<br><sub>32,33,33,32,31</sub> | 21.1<br><sub>22,23,17,25,22</sub> | 21.5 · –<br><sub>o 49% · u 51%</sub> | 6.2<br><sub>3,5,1,5,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,2,2,2,2</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.2<br><sub>2,0,0,1,0</sub> |  | 1.3 | 0.8 | 2.3 | 30.2 |
| Jeremiah Fears | 98% | 26.8<br><sub>21,24,23,24,29</sub> | 14.9<br><sub>8,7,10,11,22</sub> | 13.5 · –<br><sub>o 51% · u 49%</sub> | 4.0<br><sub>3,0,6,4,8</sub> | 3.5<br><sub>o 55% · u 45%</sub> | 3.9<br><sub>1,1,2,3,13</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>1,1,0,1,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.2 | 0.6 | 2.5 | 22.8 |
| Saddiq Bey | 96% | 26.6<br><sub>24,22,25,26,24</sub> | 13.9<br><sub>13,20,14,9,10</sub> | 12.5 · –<br><sub>o 53% · u 47%</sub> | 4.6<br><sub>5,3,4,0,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>0,1,3,3,3</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.7<br><sub>2,3,2,1,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 0.8 | 0.1 | 1.0 | 20.5 |
| Derik Queen | 98% | 23.7<br><sub>18,29,25,25,22</sub> | 10.9<br><sub>10,12,17,11,9</sub> | 11.5 · –<br><sub>o 45% · u 55%</sub> | 7.2<br><sub>10,7,8,12,2</sub> | 6.5<br><sub>o 53% · u 47%</sub> | 2.6<br><sub>1,2,2,1,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.4<br><sub>0,1,0,0,1</sub> |  | 1.0 | 1.0 | 2.1 | 20.8 |
| Herbert Jones | 96% | 23.6<br><sub>17,18,16,19,32</sub> | 7.4<br><sub>5,3,2,4,16</sub> | 6.5 · –<br><sub>o 50% · u 50%</sub> | 2.8<br><sub>2,1,3,2,4</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.0<br><sub>0,0,1,0,1</sub> |  | 0.9<br><sub>1,1,0,0,0</sub> |  | 1.3 | 0.4 | 1.2 | 12.2 |
| Bennedict Mathurin | 98% | 18.3<br><sub>18,15,20,14,19</sub> | 9.1<br><sub>11,4,9,5,10</sub> |  | 3.5<br><sub>3,2,4,1,3</sub> |  | 1.6<br><sub>2,0,4,2,2</sub> |  | 0.7<br><sub>0,0,1,1,2</sub> |  | 0.6 | 0.2 | 1.3 | 14.1 |
| Karlo Matkovic | 88% | 18.0<br><sub>-,9,8,18,28</sub> | 6.7<br><sub>-,7,3,5,12</sub> | 8.5 · –<br><sub>o 42% · u 58%</sub> | 4.5<br><sub>-,4,0,3,4</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.0<br><sub>-,1,0,1,1</sub> |  | 0.6<br><sub>-,0,1,1,1</sub> |  | 0.6 | 1.1 | 0.9 | 12.2 |
| Trendon Watford | 48% | 13.7<br><sub>-,-,-,-,17</sub> | 5.6<br><sub>-,-,-,-,8</sub> |  | 2.6<br><sub>-,-,-,-,1</sub> |  | 1.6<br><sub>-,-,-,-,2</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.4 | 1.0 | 9.8 |
| DeAndre Jordan | 52% | 12.8<br><sub>-,-,20,13,-</sub> | 3.5<br><sub>-,-,9,3,-</sub> |  | 5.2<br><sub>-,-,9,4,-</sub> |  | 0.8<br><sub>-,-,2,0,-</sub> |  | 0.0<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.7 | 0.7 | 9.5 |
| AJ Johnson | 5% | 12.3<br><sub>-,-,-,-,-</sub> | 5.3<br><sub>-,-,-,-,-</sub> |  | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.6 |
| Julian Reese | 23% | 8.8<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Bryce McGowens | 58% | 8.8<br><sub>-,-,-,3,6</sub> | 3.1<br><sub>-,-,-,0,4</sub> |  | 1.1<br><sub>-,-,-,0,1</sub> |  | 0.6<br><sub>-,-,-,0,2</sub> |  | 0.2<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.8 |
| Jaron Pierre Jr. | 22% | 8.7 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.5 | 5.9 |
| Malik Dia | 19% | 8.6 | 3.5 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.8 |

</details>


### SAC @ MEM
Out: Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.99 | 1.98 | 1.65 | 60.7% | 47.1% | 50.5% | +0.4% | +20.8% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.4–122.8 | SAC 30% | 3.32 / 1.43 | MEM -7.5 | 238.5 | MEM -8.5 covers 47%; o230.5 66% |
| Expected (weighted by chance each plays) | 114.8–123.1 | SAC 28% | 3.53 / 1.39 | MEM -8.5 | 237.5 | MEM -8.5 covers 49%; o230.5 66% |
| if Ty Jerome plays | 114.9–123.6 | SAC 27% | 3.68 / 1.37 | MEM -8.5 | 238.5 | MEM -8.5 covers 51%; o230.5 67% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quinten Post (MEM) | Doubtful | 20% | 14.0 | 5.6 | 3.0 | 0.7 | 0.5 | 0.5 | 0.4 | 0.7 | 9.3 | small |
| Ty Jerome (MEM) | Questionable | 55% | 29.1 | 22.1 | 3.5 | 6.4 | 2.6 | 1.4 | 0.3 | 2.4 | 32.1 | full tables below |
| Scotty Pippen Jr. (MEM) | Questionable | 55% | 18.3 | 9.6 | 2.5 | 3.4 | 0.8 | 1.2 | 0.3 | 1.7 | 15.5 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.1<br><sub>12,33,22,19,34</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.4 | 34.0 |
| Zach LaVine | 98% | 34.1<br><sub>34,39,40,31,39</sub> | 21.3<br><sub>28,22,37,22,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.6 | 28.2 |
| Domantas Sabonis | 98% | 34.0<br><sub>34,39,35,37,40</sub> | 18.2<br><sub>14,27,15,20,9</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 14.1<br><sub>18,19,15,14,15</sub> | 14.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 0.3<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 19% · u 81%</sub> | 0.9 | 0.4 | 3.1 | 38.3 |
| Precious Achiuwa | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.8<br><sub>15,14,12,4,24</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 1.5 | 1.1 | 1.7 | 26.7 |
| De'Andre Hunter | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.2<br><sub>6,4,7,24,24</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,7,6,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,2,5,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.8 | 20.4 |
| Emanuel Sharp | 96% | 15.6<br><sub>17,14,14,20,18</sub> | 4.8<br><sub>8,5,3,5,0</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.6<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.5 |
| Daeqwon Plowden | 71% | 15.3<br><sub>13,20,16,17,-</sub> | 5.0<br><sub>4,3,3,0,-</sub> |  | 1.9<br><sub>2,0,3,2,-</sub> |  | 0.8<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,1,1,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.6 |
| Malik Monk | 96% | 14.3<br><sub>-,12,12,13,8</sub> | 7.3<br><sub>-,0,6,3,2</sub> |  | 1.6<br><sub>-,1,1,2,1</sub> |  | 2.5<br><sub>-,2,2,6,1</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 1.1 | 11.3 |
| Jonathan Mogbo | 52% | 12.3<br><sub>8,-,18,18,-</sub> | 4.4<br><sub>0,-,7,2,-</sub> |  | 2.4<br><sub>0,-,3,5,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.7 | 7.5 |
| Alex Karaban | 64% | 11.4<br><sub>5,-,-,11,12</sub> | 3.6<br><sub>1,-,-,0,6</sub> |  | 2.2<br><sub>1,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.2<br><sub>0,-,-,0,2</sub> |  | 0.4 | 0.3 | 0.8 | 6.5 |
| Nique Clifford | 83% | 10.3<br><sub>17,2,-,5,4</sub> | 4.1<br><sub>6,0,-,2,0</sub> |  | 1.6<br><sub>1,0,-,0,0</sub> |  | 1.1<br><sub>3,0,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.8 |
| Leaky Black | 48% | 9.4<br><sub>-,-,-,8,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.4 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 96% | 33.4<br><sub>33,37,31,31,28</sub> | 18.6<br><sub>7,25,14,13,18</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 10.3<br><sub>11,13,11,7,12</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>5,6,4,4,12</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>0,4,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.7 | 2.4 | 35.6 |
| Cedric Coward | 98% | 30.4<br><sub>28,-,32,31,27</sub> | 17.9<br><sub>7,-,17,16,17</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 7.3<br><sub>7,-,11,11,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>2,-,1,3,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>1,-,3,4,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 0.5 | 2.0 | 28.9 |
| Jaylen Wells | 98% | 30.3<br><sub>28,25,33,30,25</sub> | 16.8<br><sub>12,17,16,14,10</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.6<br><sub>5,4,5,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.1<br><sub>0,3,3,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>1,4,2,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.1 | 0.2 | 1.3 | 22.6 |
| Jerami Grant | 98% | 27.3<br><sub>24,26,22,24,27</sub> | 15.3<br><sub>15,6,5,13,2</sub> |  | 3.0<br><sub>2,0,5,3,1</sub> |  | 2.3<br><sub>3,3,3,0,3</sub> |  | 1.8<br><sub>2,1,1,3,0</sub> |  | 0.8 | 0.8 | 1.7 | 20.6 |
| Zach Edey | 98% | 24.4<br><sub>21,22,-,21,19</sub> | 10.9<br><sub>6,8,-,4,13</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>9,10,-,3,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.5<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.7 | 1.7 | 1.7 | 22.0 |
| Cam Spencer | 96% | 22.7<br><sub>16,17,16,18,23</sub> | 10.8<br><sub>3,11,13,8,8</sub> |  | 2.8<br><sub>3,2,2,5,6</sub> |  | 5.8<br><sub>2,1,1,5,8</sub> |  | 1.6<br><sub>1,3,3,2,1</sub> |  | 0.8 | 0.2 | 1.2 | 19.4 |
| GG Jackson | 96% | 19.7<br><sub>19,15,10,16,21</sub> | 11.9<br><sub>12,2,1,4,12</sub> |  | 4.1<br><sub>8,4,3,1,7</sub> |  | 1.5<br><sub>0,1,0,2,2</sub> |  | 1.1<br><sub>2,0,0,0,2</sub> |  | 0.5 | 0.7 | 1.5 | 17.5 |
| Javon Small | 26% | 18.2 | 9.4 |  | 2.8 |  | 3.2 |  | 1.1 |  | 0.8 | 0.2 | 1.4 | 15.4 |
| Jahmai Mashack | 38% | 17.9<br><sub>-,-,-,-,-</sub> | 5.8<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 1.0 | 0.4 | 1.4 | 10.4 |
| Isaiah Stewart | 98% | 17.5<br><sub>-,16,22,15,16</sub> | 7.8<br><sub>-,4,13,4,18</sub> |  | 4.0<br><sub>-,2,5,4,3</sub> |  | 0.8<br><sub>-,0,2,0,0</sub> |  | 0.6<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.1 | 0.9 | 12.6 |
| Taylor Hendricks | 58% | 11.6<br><sub>-,-,7,-,3</sub> | 4.7<br><sub>-,-,0,-,0</sub> |  | 2.3<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.4 | 0.6 | 7.7 |
| Olivier-Maxence Prosper | 48% | 11.3<br><sub>-,-,-,-,3</sub> | 6.7<br><sub>-,-,-,-,4</sub> |  | 2.3<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.2 | 0.6 | 9.7 |
| Kris Murray | 58% | 10.2<br><sub>-,13,-,-,3</sub> | 2.6<br><sub>-,0,-,-,0</sub> |  | 1.6<br><sub>-,3,-,-,1</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.0 |
| Carson Cooper | 35% | 8.5<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Karim Lopez | 48% | 7.1<br><sub>-,-,-,-,3</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 2.3 |

</details>

<details><summary>if Ty Jerome plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 96% | 32.3<br><sub>33,37,31,31,28</sub> | 15.9<br><sub>7,25,14,13,18</sub> | 16.5 · –<br><sub>o 47% · u 53%</sub> | 9.7<br><sub>11,13,11,7,12</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 6.0<br><sub>5,6,4,4,12</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>0,4,2,1,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.4 | 0.7 | 2.0 | 31.7 |
| Ty Jerome (MEM) | 100% | 29.1<br><sub>32,32,32,30,24</sub> | 22.1<br><sub>45,28,31,15,10</sub> | 22.5 · – | 3.5<br><sub>7,2,4,1,2</sub> | 2.5 | 6.4<br><sub>6,5,7,8,3</sub> | 5.5 | 2.6<br><sub>5,3,1,1,1</sub> | 2.5 | 1.4 | 0.3 | 2.4 | 32.1 |
| Jaylen Wells (MEM) | 98% | 28.0<br><sub>28,25,33,30,25</sub> | 13.9<br><sub>12,17,16,14,10</sub> | 12.5 · –<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>5,4,5,3,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.7<br><sub>0,3,3,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.9<br><sub>1,4,2,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.0 | 0.1 | 1.0 | 18.8 |
| Cedric Coward (MEM) | 98% | 27.9<br><sub>28,-,32,31,27</sub> | 15.0<br><sub>7,-,17,16,17</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 6.7<br><sub>7,-,11,11,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>2,-,1,3,4</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.7<br><sub>1,-,3,4,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.9 | 0.5 | 1.6 | 24.6 |
| Jerami Grant (MEM) | 98% | 24.9<br><sub>24,26,22,24,27</sub> | 11.9<br><sub>15,6,5,13,2</sub> |  | 2.6<br><sub>2,0,5,3,1</sub> |  | 1.8<br><sub>3,3,3,0,3</sub> |  | 1.4<br><sub>2,1,1,3,0</sub> |  | 0.7 | 0.7 | 1.4 | 16.3 |
| Zach Edey (MEM) | 98% | 22.3<br><sub>21,22,-,21,19</sub> | 9.5<br><sub>6,8,-,4,13</sub> | 8.5 · –<br><sub>o 51% · u 49%</sub> | 8.4<br><sub>9,10,-,3,7</sub> | 8.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>0,3,-,2,0</sub> |  | 0.1<br><sub>0,0,-,0,1</sub> |  | 0.6 | 1.6 | 1.5 | 19.3 |
| Cam Spencer (MEM) | 96% | 19.1<br><sub>16,17,16,18,23</sub> | 8.6<br><sub>3,11,13,8,8</sub> |  | 2.4<br><sub>3,2,2,5,6</sub> |  | 4.5<br><sub>2,1,1,5,8</sub> |  | 1.2<br><sub>1,3,3,2,1</sub> |  | 0.7 | 0.2 | 0.9 | 15.4 |
| GG Jackson (MEM) | 96% | 16.9<br><sub>19,15,10,16,21</sub> | 9.6<br><sub>12,2,1,4,12</sub> |  | 3.4<br><sub>8,4,3,1,7</sub> |  | 1.2<br><sub>0,1,0,2,2</sub> |  | 0.8<br><sub>2,0,0,0,2</sub> |  | 0.4 | 0.6 | 1.2 | 14.2 |
| Isaiah Stewart (MEM) | 98% | 15.1<br><sub>-,16,22,15,16</sub> | 6.3<br><sub>-,4,13,4,18</sub> |  | 3.4<br><sub>-,2,5,4,3</sub> |  | 0.7<br><sub>-,0,2,0,0</sub> |  | 0.4<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.0 | 0.8 | 10.4 |
| Javon Small (MEM) | 26% | 12.6 | 5.6 |  | 2.0 |  | 2.1 |  | 0.6 |  | 0.6 | 0.2 | 0.9 | 9.7 |
| Jahmai Mashack (MEM) | 38% | 11.4<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 0.8 | 6.4 |
| Olivier-Maxence Prosper (MEM) | 48% | 9.0<br><sub>-,-,-,-,3</sub> | 5.1<br><sub>-,-,-,-,4</sub> |  | 1.8<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 7.5 |
| Carson Cooper (MEM) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.1 |
| Taylor Hendricks (MEM) | 58% | 8.4<br><sub>-,-,7,-,3</sub> | 3.3<br><sub>-,-,0,-,0</sub> |  | 1.7<br><sub>-,-,1,-,1</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 5.4 |
| Kris Murray (MEM) | 58% | 8.0<br><sub>-,13,-,-,3</sub> | 2.0<br><sub>-,0,-,-,0</sub> |  | 1.3<br><sub>-,3,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 3.9 |
| Karim Lopez (MEM) | 48% | 5.8<br><sub>-,-,-,-,3</sub> | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 1.9 |
| Darius Acuff Jr. (SAC) | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.1<br><sub>12,33,22,19,34</sub> | 23.5 · –<br><sub>o 46% · u 54%</sub> | 4.5<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 6.5<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.5 | 34.0 |
| Zach LaVine (SAC) | 98% | 34.0<br><sub>34,39,40,31,39</sub> | 21.1<br><sub>28,22,37,22,21</sub> | 21.5 · –<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.5<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.5 | 28.0 |
| Domantas Sabonis (SAC) | 98% | 34.0<br><sub>34,39,35,37,40</sub> | 18.4<br><sub>14,27,15,20,9</sub> | 15.5 · –<br><sub>o 52% · u 48%</sub> | 14.0<br><sub>18,19,15,14,15</sub> | 14.5<br><sub>o 46% · u 54%</sub> | 6.1<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 0.2<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 19% · u 81%</sub> | 0.9 | 0.4 | 3.1 | 38.5 |
| Precious Achiuwa (SAC) | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.9<br><sub>15,14,12,4,24</sub> | 12.5 · –<br><sub>o 54% · u 46%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 1.5 | 1.1 | 1.7 | 26.7 |
| De'Andre Hunter (SAC) | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.2<br><sub>6,4,7,24,24</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 5.6<br><sub>3,7,6,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,2,5,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.8 | 20.4 |
| Emanuel Sharp (SAC) | 96% | 15.6<br><sub>17,14,14,20,18</sub> | 4.8<br><sub>8,5,3,5,0</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.6<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.6 |
| Daeqwon Plowden (SAC) | 71% | 15.4<br><sub>13,20,16,17,-</sub> | 5.0<br><sub>4,3,3,0,-</sub> |  | 1.9<br><sub>2,0,3,2,-</sub> |  | 0.8<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,1,1,0,-</sub> |  | 0.5 | 0.2 | 0.6 | 7.6 |
| Malik Monk (SAC) | 96% | 14.3<br><sub>-,12,12,13,8</sub> | 7.3<br><sub>-,0,6,3,2</sub> |  | 1.6<br><sub>-,1,1,2,1</sub> |  | 2.5<br><sub>-,2,2,6,1</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 1.1 | 11.4 |
| Jonathan Mogbo (SAC) | 52% | 12.2<br><sub>8,-,18,18,-</sub> | 4.4<br><sub>0,-,7,2,-</sub> |  | 2.4<br><sub>0,-,3,5,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.6 | 7.4 |
| Alex Karaban (SAC) | 64% | 11.3<br><sub>5,-,-,11,12</sub> | 3.5<br><sub>1,-,-,0,6</sub> |  | 2.2<br><sub>1,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.2<br><sub>0,-,-,0,2</sub> |  | 0.4 | 0.3 | 0.8 | 6.5 |
| Nique Clifford (SAC) | 83% | 10.3<br><sub>17,2,-,5,4</sub> | 4.1<br><sub>6,0,-,2,0</sub> |  | 1.6<br><sub>1,0,-,0,0</sub> |  | 1.1<br><sub>3,0,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.8 |
| Leaky Black (SAC) | 48% | 9.4<br><sub>-,-,-,8,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.4 | 5.0 |

</details>


### CLE @ MIL
Out: Jaylon Tyson (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Myles Turner RA under 6.5 | CLE @ MIL | draftkings | 1.99 | 1.98 | 1.64 | 60.9% | 47.1% | 50.5% | +0.5% | +21.2% | 0.1% |
| Jaime Jaquez Jr. PR under 21.5 | CLE @ MIL | draftkings | 1.86 | 1.86 | 1.55 | 64.7% | 50.2% | 53.8% | +0.2% | +20.5% | 0.1% |
| Jaime Jaquez Jr. PTS under 15.5 | CLE @ MIL | draftkings | 1.93 | 1.93 | 1.61 | 62.2% | 48.3% | 51.8% | +0.2% | +20.3% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.0–113.6 | CLE 62% | 1.60 / 2.66 | MIL +4.5 | 231.5 | MIL +9.5 covers 64%; o235.5 41% |
| Expected (weighted by chance each plays) | 118.4–114.1 | CLE 62% | 1.62 / 2.62 | MIL +4.5 | 232.5 | MIL +9.5 covers 64%; o235.5 43% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Meleek Thomas (CLE) | Questionable | 55% | 18.0 | 7.8 | 2.4 | 1.2 | 0.8 | 0.7 | 0.1 | 0.9 | 11.3 | small |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 36.1<br><sub>33,33,39,34,36</sub> | 19.9<br><sub>16,12,19,16,24</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 4.8<br><sub>3,8,5,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.8<br><sub>5,7,9,6,4</sub> | 7.5<br><sub>o 42% · u 58%</sub> | 2.8<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.5 | 3.4 | 31.4 |
| Donovan Mitchell | 98% | 35.6<br><sub>35,35,38,31,33</sub> | 26.8<br><sub>32,22,26,19,22</sub> | 24.5 · –<br><sub>o 52% · u 48%</sub> | 5.0<br><sub>10,5,5,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.8<br><sub>3,4,7,7,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 3.0<br><sub>2,2,5,2,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.6 | 0.3 | 2.6 | 36.6 |
| Evan Mobley | 98% | 34.5<br><sub>34,35,38,32,33</sub> | 18.4<br><sub>18,20,18,24,11</sub> | 17.5 · –<br><sub>o 49% · u 51%</sub> | 9.1<br><sub>8,10,10,12,4</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>2,4,3,2,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.4<br><sub>1,2,4,5,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.9 | 1.5 | 1.9 | 31.0 |
| Peyton Watson | 98% | 30.4<br><sub>30,31,37,28,22</sub> | 14.6<br><sub>8,11,15,22,4</sub> | 13.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>1,3,8,6,4</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>2,4,1,2,3</sub> |  | 1.3<br><sub>0,2,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.1 | 1.9 | 21.7 |
| Jarrett Allen | 98% | 30.1<br><sub>28,27,27,30,30</sub> | 14.4<br><sub>14,21,10,8,14</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 9.0<br><sub>7,8,9,12,8</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,0,2,2,1</sub> |  | 0.1<br><sub>0,1,0,0,1</sub> |  | 1.2 | 1.3 | 1.3 | 25.0 |
| Sam Merrill | 98% | 26.3<br><sub>24,21,31,20,27</sub> | 10.9<br><sub>5,7,9,8,16</sub> | 9.5 · –<br><sub>o 49% · u 51%</sub> | 2.5<br><sub>5,2,4,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.2<br><sub>2,3,2,1,3</sub> |  | 2.1<br><sub>1,1,1,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.1 | 0.7 | 15.6 |
| Tyrese Proctor | 71% | 17.7<br><sub>5,11,-,6,20</sub> | 7.3<br><sub>0,5,-,2,7</sub> |  | 2.5<br><sub>0,2,-,1,6</sub> |  | 2.3<br><sub>0,3,-,1,2</sub> |  | 1.0<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.1 | 1.0 | 12.1 |
| Mario Hezonja | 96% | 17.6<br><sub>19,20,15,17,17</sub> | 6.6<br><sub>10,9,3,5,10</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.4<br><sub>3,5,3,3,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>2,1,1,2,2</sub> |  | 0.8<br><sub>0,2,1,1,2</sub> | 1.5<br><sub>o 30% · u 70%</sub> | 0.6 | 0.3 | 0.7 | 11.4 |
| Craig Porter Jr. | 58% | 11.0<br><sub>8,5,-,-,4</sub> | 2.9<br><sub>0,3,-,-,0</sub> |  | 2.1<br><sub>3,1,-,-,1</sub> |  | 1.7<br><sub>0,1,-,-,0</sub> |  | 0.2<br><sub>0,1,-,-,0</sub> |  | 0.6 | 0.3 | 0.7 | 6.7 |
| Thomas Bryant | 25% | 10.8<br><sub>-,-,-,-,-</sub> | 4.9<br><sub>-,-,-,-,-</sub> |  | 3.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.3 | 0.4 | 8.4 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Riley Minix | 23% | 8.4<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.3 |
| Tristan Enaruna | 23% | 7.4<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.2 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.6<br><sub>32,32,31,32,27</sub> | 19.1<br><sub>24,34,13,23,23</sub> | 21.5 · –<br><sub>o 45% · u 55%</sub> | 4.5<br><sub>2,5,6,10,3</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>9,4,3,7,0</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,5,1,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 2.3 | 28.3 |
| Ryan Rollins | 98% | 27.9<br><sub>24,34,25,32,17</sub> | 14.4<br><sub>9,11,15,19,4</sub> | 14.5 · –<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,7,4,2,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.0<br><sub>3,6,4,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.3 | 2.3 | 23.4 |
| Jaime Jaquez Jr. | 98% | 26.5<br><sub>31,35,27,25,27</sub> | 14.3<br><sub>22,19,21,8,19</sub> | 15.5 · –<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>7,11,8,6,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 3.8<br><sub>2,5,4,0,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,2,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.9 | 23.2 |
| Kyle Kuzma | 98% | 25.2<br><sub>27,30,35,29,18</sub> | 11.6<br><sub>5,14,14,17,4</sub> | 11.5 · –<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>6,9,12,7,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,4,3,3,1</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.3<br><sub>1,2,0,4,0</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.8 | 0.3 | 1.6 | 19.2 |
| Myles Turner | 98% | 23.6<br><sub>32,30,20,28,22</sub> | 9.8<br><sub>11,12,0,6,4</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>5,3,5,9,2</sub> | 5.5<br><sub>o 41% · u 59%</sub> | 1.3<br><sub>3,1,1,4,2</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 1.5 | 1.3 | 15.8 |
| Kasparas Jakucionis | 88% | 19.3<br><sub>26,23,25,21,19</sub> | 6.5<br><sub>15,7,12,7,4</sub> | 7.5 · –<br><sub>o 44% · u 56%</sub> | 2.4<br><sub>3,2,3,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>3,5,2,5,6</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 0.6<br><sub>1,1,0,1,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 12.3 |
| AJ Green | 98% | 18.7<br><sub>15,17,19,20,24</sub> | 7.1<br><sub>6,11,11,3,9</sub> | 6.5 · –<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,3,4,1</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 1.2<br><sub>2,3,3,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.4 | 0.1 | 0.6 | 10.2 |
| Cormac Ryan | 26% | 17.7 | 8.8 |  | 2.1 |  | 1.3 |  | 1.2 |  | 0.7 | 0.2 | 1.1 | 12.2 |
| Kel'el Ware | 88% | 17.4<br><sub>14,15,29,19,17</sub> | 8.7<br><sub>7,11,19,16,6</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>3,4,13,14,8</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.6 | 0.4 | 1.1 | 15.2 |
| Brayden Burries | 96% | 13.6<br><sub>16,8,17,16,17</sub> | 6.0<br><sub>12,3,10,4,10</sub> |  | 2.7<br><sub>5,1,5,2,5</sub> |  | 1.5<br><sub>0,3,2,1,1</sub> |  | 0.5<br><sub>2,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.1 |
| Ousmane Dieng | 83% | 12.4<br><sub>21,16,-,3,13</sub> | 4.7<br><sub>5,3,-,0,4</sub> |  | 2.0<br><sub>4,1,-,0,0</sub> |  | 1.6<br><sub>3,1,-,0,0</sub> |  | 0.4<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 8.2 |
| Nate Ament | 67% | 11.7<br><sub>-,-,11,14,20</sub> | 5.0<br><sub>-,-,1,7,8</sub> |  | 2.5<br><sub>-,-,3,3,4</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,1,1</sub> |  | 0.5 | 0.2 | 0.7 | 8.0 |
| Caris LeVert | 30% | 10.8<br><sub>-,-,-,-,-</sub> | 4.2<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.6 | 7.0 |
| Gary Trent Jr. | 52% | 9.3<br><sub>-,-,-,-,7</sub> | 3.9<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.0 | 0.3 | 5.0 |
| Jericho Sims | 52% | 9.2<br><sub>2,-,-,-,7</sub> | 3.1<br><sub>0,-,-,-,0</sub> |  | 2.8<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.6 | 6.7 |
| Pete Nance | 30% | 9.1 | 3.0 |  | 1.5 |  | 0.6 |  | 0.3 |  | 0.2 | 0.2 | 0.3 | 5.0 |
| Kam Jones | 26% | 8.3 | 2.4 |  | 0.9 |  | 1.6 |  | 0.2 |  | 0.3 | 0.1 | 0.5 | 4.9 |
| Bogoljub Markovic | 48% | 6.2<br><sub>-,-,-,-,5</sub> | 2.5<br><sub>-,-,-,-,2</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>


### MIN @ SAS
Out: Tobias Harris (SAS), Donte DiVincenzo (MIN), Anthony Edwards (MIN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| LaMelo Ball RA under 10.5 | MIN @ SAS | draftkings | 1.95 | 1.94 | 1.59 | 62.9% | 47.9% | 51.6% | +0.8% | +22.7% | 0.2% |
| Ayo Dosunmu PR under 19.5 | MIN @ SAS | draftkings | 1.92 | 1.91 | 1.57 | 63.5% | 48.7% | 52.4% | +0.5% | +21.8% | 0.1% |
| Stephon Castle RA over 10.5 (11+) | MIN @ SAS | draftkings | 2.01 | 2.01 | 1.67 | 59.8% | 46.5% | 49.8% | +0.1% | +20.1% | 0.0% |

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 33.9<br><sub>30,31,37,35,33</sub> | 16.2<br><sub>15,14,14,19,23</sub> | 16.5 · –<br><sub>o 50% · u 50%</sub> | 5.4<br><sub>6,6,6,7,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,3,4,4,7</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.0 | 0.9 | 1.7 | 24.4 |
| Rudy Gobert | 98% | 30.5<br><sub>30,31,36,20,30</sub> | 8.9<br><sub>14,8,5,1,9</sub> | 8.5 · –<br><sub>o 49% · u 51%</sub> | 10.4<br><sub>9,13,20,4,13</sub> | 10.5<br><sub>o 51% · u 49%</sub> | 1.8<br><sub>1,0,2,1,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.1 | 1.3 | 21.0 |
| Jonathan Kuminga | 98% | 30.3<br><sub>27,26,36,32,22</sub> | 13.5<br><sub>11,13,10,20,5</sub> | 13.5 · –<br><sub>o 50% · u 50%</sub> | 5.1<br><sub>8,4,10,3,1</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 2.0<br><sub>5,1,1,5,0</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.4<br><sub>2,3,0,3,1</sub> | 1.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.5 | 1.4 | 20.6 |
| Ayo Dosunmu | 98% | 29.6<br><sub>27,23,26,32,30</sub> | 13.7<br><sub>14,9,9,17,15</sub> | 15.5 · –<br><sub>o 44% · u 56%</sub> | 4.1<br><sub>7,3,1,3,7</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 3.7<br><sub>10,3,0,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.9 | 0.3 | 1.7 | 21.6 |
| LaMelo Ball | 98% | 28.5<br><sub>23,17,31,28,29</sub> | 18.8<br><sub>12,15,11,8,24</sub> | 19.5 · –<br><sub>o 47% · u 53%</sub> | 4.0<br><sub>5,1,0,4,4</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 5.6<br><sub>5,8,6,8,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 3.1<br><sub>2,4,1,2,6</sub> | 3.5<br><sub>o 42% · u 58%</sub> | 1.3 | 0.2 | 2.8 | 28.4 |
| Terrence Shannon Jr. | 97% | 24.2<br><sub>22,23,24,27,20</sub> | 12.8<br><sub>13,15,14,19,11</sub> | 12.5 · –<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>4,4,4,6,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 1.8<br><sub>1,3,5,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4<br><sub>2,3,3,1,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.1 | 1.3 | 17.5 |
| Bones Hyland | 96% | 16.8<br><sub>8,15,5,16,20</sub> | 8.6<br><sub>3,3,0,13,19</sub> | 8.5 · –<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,3,1,1,0</sub> |  | 2.4<br><sub>0,2,2,3,8</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>1,0,0,3,3</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.3 | 1.1 | 12.8 |
| Joan Beringer | 91% | 16.7<br><sub>15,13,17,20,18</sub> | 6.8<br><sub>9,6,12,7,4</sub> |  | 5.4<br><sub>9,6,7,9,4</sub> |  | 0.6<br><sub>0,0,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.1 | 0.7 | 12.9 |
| Trey Lyles | 98% | 16.2<br><sub>17,14,13,22,17</sub> | 5.1<br><sub>9,3,3,7,10</sub> |  | 3.5<br><sub>6,6,1,3,5</sub> |  | 0.9<br><sub>2,2,1,1,0</sub> |  | 0.6<br><sub>2,1,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 9.5 |
| Jaylen Clark | 80% | 13.5<br><sub>3,5,-,7,17</sub> | 4.5<br><sub>0,3,-,3,5</sub> |  | 1.7<br><sub>2,1,-,2,0</sub> |  | 0.9<br><sub>1,0,-,1,2</sub> |  | 0.5<br><sub>0,0,-,1,1</sub> |  | 0.7 | 0.1 | 0.5 | 7.1 |
| Zyon Pullin | 64% | 8.7<br><sub>-,5,-,-,2</sub> | 3.5<br><sub>-,2,-,-,2</sub> |  | 1.0<br><sub>-,1,-,-,0</sub> |  | 1.1<br><sub>-,0,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.5 | 5.6 |
| Rocco Zikarsky | 16% | 7.0 | 2.4 |  | 2.2 |  | 0.4 |  | 0.0 |  | 0.2 | 0.6 | 0.3 | 5.0 |
| Cody Williams | 58% | 6.4<br><sub>3,5,-,-,2</sub> | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2<br><sub>0,0,-,-,0</sub> |  | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.2 | 1.0 |
| Isaiah Evans | 63% | 6.2<br><sub>2,4,-,-,2</sub> | 0.3<br><sub>0,0,-,-,0</sub> |  | 1.2<br><sub>0,0,-,-,0</sub> |  | 0.5<br><sub>1,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 2.0 |
| Enrique Freeman | 16% | 6.1 | 1.9 |  | 1.3 |  | 0.3 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.5 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 34.4<br><sub>34,32,29,27,39</sub> | 25.5<br><sub>12,25,23,29,36</sub> | 24.5 · –<br><sub>o 51% · u 49%</sub> | 11.4<br><sub>13,13,7,10,14</sub> | 11.5<br><sub>o 46% · u 54%</sub> | 3.2<br><sub>3,2,2,2,5</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.9<br><sub>0,2,2,0,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 3.6 | 2.8 | 40.0 |
| Devin Vassell | 98% | 33.4<br><sub>31,36,32,24,38</sub> | 12.6<br><sub>7,10,11,14,21</sub> | 11.5 · –<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>3,4,4,4,5</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 2.9<br><sub>1,2,6,8,2</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,2,1,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.5 | 1.0 | 20.1 |
| De'Aaron Fox | 98% | 33.0<br><sub>32,34,28,26,39</sub> | 16.4<br><sub>14,19,19,11,14</sub> | 14.5 · –<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>7,4,3,4,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 6.2<br><sub>7,9,9,6,4</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.5<br><sub>0,2,2,2,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 1.5 | 0.4 | 2.2 | 26.8 |
| Stephon Castle | 98% | 32.5<br><sub>28,33,28,27,38</sub> | 17.9<br><sub>24,15,19,15,14</sub> | 16.5 · –<br><sub>o 51% · u 49%</sub> | 5.5<br><sub>7,7,4,5,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 6.3<br><sub>1,5,8,5,8</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.7<br><sub>5,3,3,3,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.2 | 0.3 | 3.1 | 29.7 |
| Dylan Harper | 98% | 31.8<br><sub>32,36,28,30,37</sub> | 16.6<br><sub>18,20,22,13,13</sub> | 15.5 · –<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>7,3,5,6,5</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 4.1<br><sub>5,2,2,6,8</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>0,1,3,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.4 | 1.8 | 26.3 |
| Julian Champagnie | 98% | 28.3<br><sub>30,25,28,25,31</sub> | 9.9<br><sub>8,6,12,26,6</sub> | 9.5 · –<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>3,0,5,3,6</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.4<br><sub>1,0,3,3,0</sub> |  | 1.8<br><sub>2,2,3,8,2</sub> | 2.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.6 | 0.8 | 16.1 |
| Keldon Johnson | 98% | 20.8<br><sub>20,19,26,22,23</sub> | 10.0<br><sub>10,8,7,14,9</sub> | 8.5 · –<br><sub>o 54% · u 46%</sub> | 4.2<br><sub>4,6,6,4,6</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.1<br><sub>1,1,3,0,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 56% · u 44%</sub> | 0.6 | 0.2 | 0.9 | 15.3 |
| Luke Kornet | 98% | 13.9<br><sub>13,16,14,17,14</sub> | 3.3<br><sub>4,7,0,0,1</sub> |  | 4.0<br><sub>1,3,4,4,6</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 8.2 |
| Harrison Barnes | 67% | 8.6<br><sub>9,5,4,14,-</sub> | 2.8<br><sub>3,0,0,3,-</sub> |  | 1.1<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Carter Bryant | 98% | 8.2<br><sub>6,4,10,17,5</sub> | 2.6<br><sub>0,0,4,1,3</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>1,0,0,2,0</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.2 | 0.2 | 0.4 | 4.5 |
| Maliq Brown | 80% | 6.9<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.1 |
| Jordan McLaughlin | 52% | 6.4<br><sub>-,-,3,7,-</sub> | 2.1<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 0.9<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.0 |
| Tarris Reed Jr. | 58% | 6.0<br><sub>1,-,7,5,-</sub> | 2.4<br><sub>0,-,2,4,-</sub> |  | 2.2<br><sub>0,-,3,5,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.7 | 5.0 |
| Ja'Kobi Gillespie | 88% | 5.9<br><sub>1,-,3,-,-</sub> | 4.2<br><sub>2,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>0,-,1,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 5.0 |
| David Jones Garcia | 52% | 5.8<br><sub>1,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |

</details>


### OKC @ HOU
Out: Steven Adams (HOU), Reed Sheppard (HOU), Fred VanVleet (HOU), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander AST over 5.5 (6+) | OKC @ HOU | draftkings | 1.92 | 1.90 | 1.59 | 62.9% | 49.1% | 52.5% | +0.7% | +20.7% | 0.2% |
| Jabari Smith Jr. 3PM over 2.5 (3+) | OKC @ HOU | draftkings | 2.36 | 2.35 | 1.95 | 51.2% | 39.8% | 42.6% | +0.6% | +20.8% | 0.1% |
| Amen Thompson PA over 20.5 (21+) | OKC @ HOU | draftkings | 1.85 | 1.85 | 1.54 | 65.0% | 50.5% | 54.1% | +0.4% | +20.6% | 0.1% |
| Alperen Sengun REB over 8.5 (9+) | OKC @ HOU | draftkings | 1.87 | 1.87 | 1.59 | 62.9% | 50.4% | 53.5% | +0.1% | +17.6% | 0.0% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.6<br><sub>36,35,36,30,28</sub> | 30.4<br><sub>32,17,34,26,21</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,2,6,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 6.7<br><sub>4,3,5,3,2</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.9 | 3.3 | 41.0 |
| Jared McCain | 98% | 30.0<br><sub>22,18,21,30,29</sub> | 15.9<br><sub>20,4,3,18,10</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>2,0,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,1,0,4,4</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 2.4<br><sub>6,0,1,4,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.9 | 21.1 |
| Ajay Mitchell | 98% | 29.6<br><sub>23,23,28,25,28</sub> | 19.0<br><sub>4,12,18,30,29</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>5,0,6,2,4</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 4.4<br><sub>6,0,4,5,3</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.3 | 2.2 | 26.9 |
| Josh Dix | 67% | 27.2<br><sub>-,-,-,22,24</sub> | 4.4<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.4 |
| Bennett Stirtz | 96% | 26.7<br><sub>1,2,11,25,28</sub> | 7.9<br><sub>0,0,2,7,8</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 1.0<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.1 |
| Isaiah Hartenstein | 98% | 26.6<br><sub>17,23,27,26,26</sub> | 10.2<br><sub>4,6,12,15,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>3,6,12,13,14</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,2,1,3,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 22.9 |
| Aday Mara | 96% | 24.2<br><sub>12,13,14,20,21</sub> | 8.2<br><sub>7,2,2,11,6</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>2,3,3,10,3</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.3<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.4 | 15.6 |
| Kenrich Williams | 93% | 21.7<br><sub>7,6,7,24,17</sub> | 8.0<br><sub>3,3,3,3,7</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>2,1,1,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.8 | 0.2 | 0.9 | 13.9 |
| Jaylin Williams | 98% | 21.3<br><sub>17,15,5,26,20</sub> | 6.1<br><sub>5,3,0,6,0</sub> |  | 5.3<br><sub>4,7,0,6,5</sub> |  | 2.0<br><sub>1,3,0,3,1</sub> |  | 0.9<br><sub>1,1,0,2,0</sub> |  | 0.6 | 0.5 | 0.8 | 13.3 |
| Micah Peavy | 48% | 13.1<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer | 80% | 13.0<br><sub>1,2,-,3,14</sub> | 3.5<br><sub>0,0,-,0,3</sub> |  | 2.5<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.8<br><sub>36,39,28,33,39</sub> | 18.8<br><sub>20,17,15,23,15</sub> | 15.5 · –<br><sub>o 55% · u 45%</sub> | 7.4<br><sub>10,11,5,4,3</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 5.7<br><sub>4,6,2,3,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.8 | 31.9 |
| Kevin Durant | 98% | 37.6<br><sub>37,37,30,31,37</sub> | 25.8<br><sub>20,22,22,18,28</sub> | 23.5 · –<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>7,4,9,5,5</sub> | 4.5<br><sub>o 61% · u 39%</sub> | 5.1<br><sub>6,2,3,4,1</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 2.2<br><sub>2,3,1,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 1.0 | 3.8 | 37.4 |
| Jabari Smith Jr. | 98% | 37.1<br><sub>34,33,39,30,35</sub> | 17.4<br><sub>7,14,16,14,22</sub> | 14.5 · –<br><sub>o 54% · u 46%</sub> | 7.4<br><sub>5,5,12,2,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>1,3,5,2,2</sub> |  | 2.7<br><sub>1,2,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.8 | 1.8 | 27.0 |
| Alperen Sengun | 58% | 35.4<br><sub>36,33,37,-,-</sub> | 19.7<br><sub>29,17,29,-,-</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 10.0<br><sub>7,10,9,-,-</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>7,7,9,-,-</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 0.7<br><sub>2,1,1,-,-</sub> |  | 1.2 | 0.9 | 3.6 | 36.0 |
| Tari Eason | 98% | 30.9<br><sub>27,31,33,31,26</sub> | 12.6<br><sub>12,19,13,5,11</sub> |  | 7.4<br><sub>6,3,8,9,13</sub> |  | 1.6<br><sub>0,0,2,1,2</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> |  | 1.4 | 0.7 | 1.5 | 21.7 |
| Marcus Smart | 63% | 26.0<br><sub>21,-,-,-,17</sub> | 9.2<br><sub>5,-,-,-,8</sub> |  | 2.8<br><sub>3,-,-,-,2</sub> |  | 3.2<br><sub>1,-,-,-,4</sub> |  | 1.3<br><sub>0,-,-,-,0</sub> |  | 1.4 | 0.3 | 1.9 | 15.2 |
| Clint Capela | 88% | 22.3<br><sub>-,11,4,22,30</sub> | 6.5<br><sub>-,2,2,10,5</sub> |  | 7.8<br><sub>-,3,2,8,11</sub> |  | 1.4<br><sub>-,1,0,2,5</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.2 | 0.9 | 15.7 |
| Bogdan Bogdanovic | 91% | 19.5<br><sub>9,20,13,15,11</sub> | 7.8<br><sub>3,11,5,16,6</sub> |  | 2.4<br><sub>1,1,2,2,1</sub> |  | 1.9<br><sub>0,1,1,4,0</sub> |  | 1.3<br><sub>1,3,1,4,0</sub> |  | 0.6 | 0.2 | 0.9 | 12.1 |
| Oscar Tshiebwe | 76% | 16.5<br><sub>-,-,-,14,11</sub> | 6.3<br><sub>-,-,-,7,0</sub> |  | 6.8<br><sub>-,-,-,5,5</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.4 | 1.0 | 14.0 |
| Jae'Sean Tate | 64% | 9.5<br><sub>-,1,1,4,-</sub> | 3.1<br><sub>-,0,0,0,-</sub> |  | 2.1<br><sub>-,0,1,0,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Bruce Thornton | 63% | 8.7<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,0,0,5,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Isaiah Crawford | 58% | 8.3<br><sub>-,1,1,5,-</sub> | 2.7<br><sub>-,0,0,3,-</sub> |  | 1.5<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-31/`._
