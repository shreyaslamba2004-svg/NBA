# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sun 01 Nov, 10:47 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kel'el Ware PTS under 9.5 | CLE @ MIL | pointsbetau | 2.00 | 1.89 | 1.59 | 62.8% | 49.6% | 52.9% | +5.8% | +25.5% | 1.5% |
| Julian Champagnie PTS under 10.5 | MIN @ SAS | tab | 2.00 | 1.89 | 1.67 | 59.9% | 50.4% | 52.8% | +5.6% | +19.9% | 1.4% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 7.5 (8+) | OKC @ HOU | draftkings | 21.00 | 13.32 | 5.99 | 16.7% | 4.5% | 7.5% | +57.8% | +250.7% | 0.7% |
| Tari Eason REB over 11.5 (12+) | OKC @ HOU | draftkings | 21.00 | 16.39 | 9.06 | 11.0% | 4.5% | 6.1% | +28.0% | +131.7% | 0.4% |
| Tari Eason REB over 9.5 (10+) | OKC @ HOU | draftkings | 9.40 | 7.39 | 4.12 | 24.3% | 9.9% | 13.5% | +27.2% | +128.3% | 0.8% |
| Cameron Boozer REB over 13.5 (14+) | SAC @ MEM | draftkings | 9.80 | 7.84 | 4.46 | 22.4% | 9.5% | 12.8% | +25.0% | +119.5% | 0.7% |
| Cameron Boozer REB over 15.5 (16+) | SAC @ MEM | draftkings | 19.00 | 15.27 | 8.73 | 11.5% | 4.9% | 6.6% | +24.5% | +117.5% | 0.3% |
| Kevin Durant REB over 9.5 (10+) | OKC @ HOU | draftkings | 14.60 | 12.00 | 7.08 | 14.1% | 6.4% | 8.3% | +21.6% | +106.2% | 0.4% |
| Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings | 28.00 | 23.47 | 14.23 | 7.0% | 3.3% | 4.3% | +19.3% | +96.8% | 0.2% |
| Amen Thompson AST over 7.5 (8+) | OKC @ HOU | draftkings | 8.20 | 6.93 | 4.26 | 23.5% | 11.4% | 14.4% | +18.2% | +92.5% | 0.6% |
| Amen Thompson AST over 9.5 (10+) | OKC @ HOU | draftkings | 22.00 | 18.69 | 11.53 | 8.7% | 4.2% | 5.3% | +17.8% | +90.8% | 0.2% |
| Amen Thompson PTS over 29.5 (30+) | OKC @ HOU | draftkings | 20.60 | 17.64 | 11.04 | 9.1% | 4.5% | 5.7% | +16.8% | +86.7% | 0.2% |
| Shai Gilgeous-Alexander PRA over 59.5 (60+) | OKC @ HOU | draftkings | 20.20 | 17.33 | 10.88 | 9.2% | 4.6% | 5.8% | +16.5% | +85.6% | 0.2% |
| Shai Gilgeous-Alexander PTS over 44.5 (45+) | OKC @ HOU | draftkings | 15.20 | 13.11 | 8.28 | 12.1% | 6.2% | 7.6% | +16.0% | +83.5% | 0.3% |
| Amen Thompson PRA over 44.5 (45+) | OKC @ HOU | draftkings | 19.00 | 16.39 | 10.38 | 9.6% | 4.9% | 6.1% | +15.9% | +83.1% | 0.2% |
| Amen Thompson PRA over 39.5 (40+) | OKC @ HOU | draftkings | 9.20 | 7.99 | 5.10 | 19.6% | 10.2% | 12.5% | +15.2% | +80.5% | 0.5% |
| MIN to win | MIN @ SAS | ladbrokes_au | 6.25 | 5.49 | 4.32 | 23.1% | 18.2% | 18.2% | +13.9% | +44.6% | 0.7% |
| Jabari Smith Jr. PRA over 34.5 (35+) | OKC @ HOU | draftkings | 9.50 | 8.41 | 5.54 | 18.1% | 9.8% | 11.9% | +13.0% | +71.5% | 0.4% |
| Zach Edey REB over 15.5 (16+) | SAC @ MEM | draftkings | 17.00 | 15.17 | 10.12 | 9.9% | 5.5% | 6.6% | +12.1% | +68.0% | 0.2% |
| Zach Edey REB over 13.5 (14+) | SAC @ MEM | draftkings | 8.80 | 7.86 | 5.24 | 19.1% | 10.6% | 12.7% | +12.0% | +67.8% | 0.4% |
| Amen Thompson PTS over 24.5 (25+) | OKC @ HOU | draftkings | 8.00 | 7.15 | 4.78 | 20.9% | 11.7% | 14.0% | +11.9% | +67.4% | 0.4% |
| Jabari Smith Jr. REB over 9.5 (10+) | OKC @ HOU | draftkings | 7.10 | 6.43 | 4.40 | 22.7% | 13.2% | 15.6% | +10.4% | +61.2% | 0.4% |
| Darius Acuff Jr. REB over 7.5 (8+) | SAC @ MEM | draftkings | 17.00 | 15.41 | 10.58 | 9.5% | 5.5% | 6.5% | +10.3% | +60.7% | 0.2% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ HOU | draftkings | 9.20 | 8.35 | 5.73 | 17.4% | 10.2% | 12.0% | +10.2% | +60.5% | 0.3% |
| Jabari Smith Jr. PRA over 39.5 (40+) | OKC @ HOU | draftkings | 20.00 | 18.15 | 12.48 | 8.0% | 4.7% | 5.5% | +10.2% | +60.3% | 0.1% |
| Jaime Jaquez Jr. AST over 7.5 (8+) | CLE @ MIL | draftkings | 19.80 | 17.99 | 12.38 | 8.1% | 4.7% | 5.6% | +10.1% | +60.0% | 0.1% |
| Jabari Smith Jr. REB over 11.5 (12+) | OKC @ HOU | draftkings | 16.80 | 15.29 | 10.55 | 9.5% | 5.6% | 6.5% | +9.9% | +59.2% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 10.5 (11+) | OKC @ HOU | draftkings | 14.40 | 11.04 | 5.96 | 16.8% | 6.5% | 9.1% | +30.4% | +141.4% | 0.6% |
| Cameron Boozer REB over 14.5 (15+) | SAC @ MEM | draftkings | 13.80 | 10.98 | 6.21 | 16.1% | 6.8% | 9.1% | +25.7% | +122.4% | 0.5% |
| Tari Eason REB over 12.5 (13+) | OKC @ HOU | draftkings | 29.00 | 23.75 | 13.91 | 7.2% | 3.2% | 4.2% | +22.2% | +108.5% | 0.2% |
| Kevin Durant REB over 8.5 (9+) | OKC @ HOU | draftkings | 9.20 | 7.58 | 4.49 | 22.3% | 10.2% | 13.2% | +21.3% | +105.0% | 0.7% |
| Amen Thompson AST over 8.5 (9+) | OKC @ HOU | draftkings | 14.20 | 11.71 | 6.93 | 14.4% | 6.6% | 8.5% | +21.3% | +104.9% | 0.4% |
| Cameron Boozer REB over 16.5 (17+) | SAC @ MEM | draftkings | 25.00 | 21.05 | 12.82 | 7.8% | 3.7% | 4.8% | +18.8% | +95.0% | 0.2% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 23.00 | 19.42 | 11.91 | 8.4% | 4.1% | 5.1% | +18.4% | +93.1% | 0.2% |
| Zach Edey REB over 14.5 (15+) | SAC @ MEM | draftkings | 12.40 | 10.96 | 7.21 | 13.9% | 7.5% | 9.1% | +13.1% | +71.9% | 0.3% |
| Jaime Jaquez Jr. AST over 6.5 (7+) | CLE @ MIL | draftkings | 11.40 | 10.18 | 6.81 | 14.7% | 8.2% | 9.8% | +11.9% | +67.3% | 0.3% |
| Shai Gilgeous-Alexander AST over 10.5 (11+) | OKC @ HOU | draftkings | 15.20 | 13.64 | 9.19 | 10.9% | 6.2% | 7.3% | +11.5% | +65.5% | 0.2% |
| Jabari Smith Jr. REB over 10.5 (11+) | OKC @ HOU | draftkings | 11.00 | 9.88 | 6.66 | 15.0% | 8.5% | 10.1% | +11.4% | +65.1% | 0.3% |
| Darius Acuff Jr. REB over 6.5 (7+) | SAC @ MEM | draftkings | 9.70 | 8.72 | 5.89 | 17.0% | 9.6% | 11.5% | +11.3% | +64.8% | 0.3% |
| Zach Edey PTS over 8.5 (9+) | SAC @ MEM | pointsbetau | 2.05 | 1.85 | 1.59 | 62.9% | 51.3% | 54.2% | +11.1% | +28.9% | 2.0% |
| Zach Edey REB over 16.5 (17+) | SAC @ MEM | draftkings | 23.00 | 20.79 | 14.21 | 7.0% | 4.1% | 4.8% | +10.5% | +61.8% | 0.1% |
| Zach Edey REB over 12.5 (13+) | SAC @ MEM | draftkings | 6.28 | 5.74 | 4.00 | 25.0% | 14.9% | 17.4% | +9.4% | +57.1% | 0.4% |
| Cedric Coward REB over 12.5 (13+) | SAC @ MEM | draftkings | 20.00 | 18.38 | 12.94 | 7.7% | 4.7% | 5.4% | +8.7% | +54.6% | 0.1% |
| Cedric Coward REB over 10.5 (11+) | SAC @ MEM | draftkings | 8.90 | 8.20 | 5.79 | 17.3% | 10.5% | 12.2% | +8.5% | +53.7% | 0.3% |
| Jabari Smith Jr. REB over 8.5 (9+) | OKC @ HOU | draftkings | 4.61 | 4.28 | 3.07 | 32.6% | 20.3% | 23.4% | +7.7% | +50.3% | 0.5% |
| Shai Gilgeous-Alexander AST over 8.5 (9+) | OKC @ HOU | draftkings | 5.70 | 5.33 | 3.87 | 25.9% | 16.4% | 18.8% | +7.0% | +47.4% | 0.4% |
| Jabari Smith Jr. REB over 12.5 (13+) | OKC @ HOU | draftkings | 25.00 | 23.47 | 17.17 | 5.8% | 3.7% | 4.3% | +6.5% | +45.6% | 0.1% |
| De'Andre Hunter REB over 8.5 (9+) | SAC @ MEM | draftkings | 10.50 | 9.86 | 7.23 | 13.8% | 8.9% | 10.1% | +6.4% | +45.3% | 0.2% |
| Aday Mara REB over 10.5 (11+) | OKC @ HOU | draftkings | 16.00 | 15.13 | 11.22 | 8.9% | 5.8% | 6.6% | +5.7% | +42.6% | 0.1% |
| Darius Acuff Jr. REB over 4.5 (5+) | SAC @ MEM | draftkings | 3.20 | 3.03 | 2.26 | 44.2% | 29.2% | 33.0% | +5.5% | +41.4% | 0.6% |
| Jaime Jaquez Jr. AST over 4.5 (5+) | CLE @ MIL | draftkings | 3.56 | 3.38 | 2.54 | 39.4% | 26.2% | 29.5% | +5.2% | +40.4% | 0.5% |
| De'Andre Hunter REB over 6.5 (7+) | SAC @ MEM | draftkings | 4.20 | 3.99 | 2.99 | 33.4% | 22.2% | 25.0% | +5.2% | +40.3% | 0.4% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 7.5 (8+) | OKC @ HOU | draftkings | 3.90 | 3.42 | 2.22 | 45.0% | 24.0% | 29.2% | +14.0% | +75.5% | 1.2% |
| Cameron Boozer REB over 9.5 (10+) | SAC @ MEM | draftkings | 2.70 | 2.45 | 1.69 | 59.3% | 34.6% | 40.8% | +10.1% | +60.0% | 1.5% |
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.14 | 1.96 | 1.37 | 72.9% | 43.9% | 51.1% | +9.4% | +55.9% | 2.0% |
| AJ Green 3PM under 1.5 | CLE @ MIL | draftkings | 2.33 | 2.14 | 1.49 | 67.0% | 40.1% | 46.8% | +9.1% | +56.0% | 1.7% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 2.00 | 1.83 | 1.29 | 77.6% | 46.9% | 54.5% | +9.1% | +55.1% | 2.0% |
| Amen Thompson AST over 5.5 (6+) | OKC @ HOU | draftkings | 2.99 | 2.79 | 2.02 | 49.6% | 31.3% | 35.9% | +7.2% | +48.3% | 0.9% |
| Cameron Boozer REB over 8.5 (9+) | SAC @ MEM | draftkings | 2.09 | 1.96 | 1.43 | 69.7% | 44.7% | 51.0% | +6.5% | +45.7% | 1.5% |
| Kevin Durant REB over 5.5 (6+) | OKC @ HOU | draftkings | 2.34 | 2.22 | 1.66 | 60.3% | 39.9% | 45.0% | +5.4% | +41.1% | 1.0% |
| Cameron Boozer RA over 14.5 (15+) | SAC @ MEM | draftkings | 2.00 | 1.90 | 1.43 | 70.0% | 46.8% | 52.6% | +5.1% | +40.0% | 1.3% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| SAC @ MEM | Sun 01 Nov 11:00 | 115.8–122.4 | SAC 32% | 3.12 / 1.47 | MEM -6.5 | 238.5 | MEM -7.5 covers 47%; o226.5 74% |
| CLE @ MIL | Sun 01 Nov 11:00 | 118.8–114.7 | CLE 61% | 1.63 / 2.60 | MIL +4.5 | 233.5 | MIL +9.5 covers 65%; o235.5 45% |
| MIN @ SAS | Sun 01 Nov 11:00 | 107.9–118.3 | MIN 23% | 4.32 / 1.30 | SAS -10.5 | 226.5 | SAS -12.5 covers 44%; o230.5 41% |
| OKC @ HOU | Sun 01 Nov 11:30 | 112.1–113.1 | OKC 47% | 2.12 / 1.90 | HOU -1.5 | 225.5 | HOU -2.5 covers 47%; o219.5 61% |

### SAC @ MEM
Out: Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Quinten Post (MEM), Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Precious Achiuwa PTS over 12.5 (13+) | SAC @ MEM | pointsbetau | 1.95 | 1.89 | 1.58 | 63.1% | 49.6% | 53.0% | +3.4% | +23.2% | 0.9% |
| Zach LaVine PTS under 21.5 | SAC @ MEM | betright | 1.98 | 1.92 | 1.72 | 58.1% | 50.0% | 52.0% | +3.0% | +15.0% | 0.8% |
| Jaylen Wells PTS over 13.5 (14+) | SAC @ MEM | sportsbet | 1.96 | 1.91 | 1.64 | 60.9% | 49.6% | 52.4% | +2.8% | +19.4% | 0.7% |
| Precious Achiuwa PRA over 22.5 (23+) | SAC @ MEM | draftkings | 1.88 | 1.87 | 1.55 | 64.5% | 49.7% | 53.4% | +0.7% | +21.6% | 0.2% |
| Zach Edey RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.91 | 1.90 | 1.57 | 63.7% | 49.0% | 52.7% | +0.5% | +21.6% | 0.1% |
| De'Andre Hunter REB over 4.5 (5+) | SAC @ MEM | draftkings | 1.94 | 1.93 | 1.61 | 62.3% | 48.2% | 51.7% | +0.5% | +21.1% | 0.1% |
| Precious Achiuwa PR over 20.5 (21+) | SAC @ MEM | draftkings | 1.85 | 1.84 | 1.52 | 65.6% | 50.7% | 54.4% | +0.5% | +21.2% | 0.1% |
| Zach Edey PR over 17.5 (18+) | SAC @ MEM | draftkings | 1.92 | 1.91 | 1.58 | 63.4% | 48.7% | 52.4% | +0.5% | +21.6% | 0.1% |
| Zach Edey REB over 8.5 (9+) | SAC @ MEM | draftkings | 2.01 | 2.00 | 1.67 | 59.9% | 46.6% | 49.9% | +0.4% | +20.4% | 0.1% |
| Precious Achiuwa RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.99 | 1.99 | 1.66 | 60.4% | 47.0% | 50.3% | +0.2% | +20.2% | 0.0% |
| Darius Acuff Jr. RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.94 | 1.94 | 1.62 | 61.6% | 48.2% | 51.5% | +0.1% | +19.7% | 0.0% |
| Domantas Sabonis PTS over 15.5 (16+) | SAC @ MEM | unibet | 1.88 | 1.88 | 1.66 | 60.2% | 50.7% | 53.1% | +0.1% | +13.5% | 0.0% |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 100% | 36.0<br><sub>35,37,36,33,41</sub> | 23.0<br><sub>12,33,22,19,34</sub> | 23.5 · 23.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.4<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.4 | 33.8 |
| Domantas Sabonis | 100% | 34.1<br><sub>34,39,35,37,40</sub> | 18.3<br><sub>14,27,15,20,9</sub> | 15.5 · 15.5<br><sub>o 51% · u 49%</sub> | 14.1<br><sub>18,19,15,14,15</sub> | 13.5<br><sub>o 53% · u 47%</sub> | 6.0<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 19% · u 81%</sub> | 0.9 | 0.4 | 3.1 | 38.4 |
| Zach LaVine | 100% | 34.0<br><sub>34,39,40,31,39</sub> | 20.9<br><sub>28,22,37,22,21</sub> | 21.5 · 21.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.5<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.3 | 2.6 | 27.8 |
| Precious Achiuwa | 100% | 32.8<br><sub>29,26,39,14,41</sub> | 15.4<br><sub>15,14,12,4,24</sub> | 12.5 · 12.5<br><sub>o 53% · u 47%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.3<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 1.4 | 1.1 | 1.6 | 26.2 |
| De'Andre Hunter | 100% | 29.4<br><sub>20,25,29,33,37</sub> | 12.9<br><sub>6,4,7,24,24</sub> | 12.5 · 12.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>3,7,6,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,2,5,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.9 | 0.2 | 1.8 | 20.2 |
| Emanuel Sharp | 96% | 15.4<br><sub>17,14,14,20,18</sub> | 4.7<br><sub>8,5,3,5,0</sub> | 5.5 · –<br><sub>o 43% · u 57%</sub> | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.9<br><sub>0,1,0,2,0</sub> |  | 0.5<br><sub>2,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.5 |
| Daeqwon Plowden | 71% | 15.1<br><sub>13,20,16,17,-</sub> | 5.0<br><sub>4,3,3,0,-</sub> |  | 1.9<br><sub>2,0,3,2,-</sub> |  | 0.8<br><sub>1,0,1,0,-</sub> |  | 0.7<br><sub>0,1,1,0,-</sub> |  | 0.5 | 0.1 | 0.6 | 7.6 |
| Malik Monk | 96% | 14.1<br><sub>-,12,12,13,8</sub> | 7.1<br><sub>-,0,6,3,2</sub> |  | 1.5<br><sub>-,1,1,2,1</sub> |  | 2.4<br><sub>-,2,2,6,1</sub> |  | 0.8<br><sub>-,0,0,1,0</sub> |  | 0.5 | 0.3 | 1.1 | 11.1 |
| Jonathan Mogbo | 52% | 11.6<br><sub>8,-,18,18,-</sub> | 4.2<br><sub>0,-,7,2,-</sub> |  | 2.3<br><sub>0,-,3,5,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,1,0,-</sub> |  | 0.5 | 0.3 | 0.6 | 7.1 |
| Alex Karaban | 64% | 11.3<br><sub>5,-,-,11,12</sub> | 3.5<br><sub>1,-,-,0,6</sub> |  | 2.3<br><sub>1,-,-,1,0</sub> |  | 0.8<br><sub>0,-,-,1,0</sub> |  | 0.2<br><sub>0,-,-,0,2</sub> |  | 0.4 | 0.3 | 0.8 | 6.6 |
| Nique Clifford | 83% | 10.0<br><sub>17,2,-,5,4</sub> | 3.9<br><sub>6,0,-,2,0</sub> |  | 1.6<br><sub>1,0,-,0,0</sub> |  | 1.1<br><sub>3,0,-,0,1</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.8 | 6.6 |
| Leaky Black | 48% | 9.5<br><sub>-,-,-,8,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 1.8<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,1,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.5 | 0.3 | 0.4 | 5.0 |

</details>

<details><summary>MEM players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer | 100% | 33.6<br><sub>33,37,31,31,28</sub> | 18.6<br><sub>7,25,14,13,18</sub> | 18.5 · 17.5<br><sub>o 52% · u 48%</sub> | 10.7<br><sub>11,13,11,7,12</sub> | 8.5<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>5,6,4,4,12</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>0,4,2,1,4</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.5 | 0.7 | 2.4 | 36.1 |
| Cedric Coward | 100% | 30.5<br><sub>28,-,32,31,27</sub> | 17.6<br><sub>7,-,17,16,17</sub> | 16.5 · 16.5<br><sub>o 54% · u 46%</sub> | 7.5<br><sub>7,-,11,11,7</sub> | 6.5<br><sub>o 50% · u 50%</sub> | 3.8<br><sub>2,-,1,3,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,-,3,4,3</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.5 | 2.1 | 28.9 |
| Jaylen Wells | 100% | 30.4<br><sub>28,25,33,30,25</sub> | 16.3<br><sub>12,17,16,14,10</sub> | 13.5 · 13.5<br><sub>o 52% · u 48%</sub> | 3.7<br><sub>5,4,5,3,1</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.1<br><sub>0,3,3,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>1,4,2,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.1 | 0.2 | 1.3 | 22.1 |
| Jerami Grant | 98% | 27.2<br><sub>24,26,22,24,27</sub> | 14.5<br><sub>15,6,5,13,2</sub> |  | 3.0<br><sub>2,0,5,3,1</sub> |  | 2.3<br><sub>3,3,3,0,3</sub> |  | 1.7<br><sub>2,1,1,3,0</sub> |  | 0.8 | 0.8 | 1.6 | 19.7 |
| Cam Spencer | 100% | 26.5<br><sub>16,17,16,18,23</sub> | 12.9<br><sub>3,11,13,8,8</sub> | 11.5 · 11.5<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,2,2,5,6</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 6.8<br><sub>2,1,1,5,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,3,3,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.9 | 0.2 | 1.4 | 23.2 |
| Zach Edey | 100% | 25.0<br><sub>21,22,-,21,19</sub> | 10.9<br><sub>6,8,-,4,13</sub> | 8.5 · 8.5<br><sub>o 52% · u 48%</sub> | 9.9<br><sub>9,10,-,3,7</sub> | 8.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.7 | 1.8 | 1.8 | 22.3 |
| GG Jackson | 96% | 19.3<br><sub>19,15,10,16,21</sub> | 11.5<br><sub>12,2,1,4,12</sub> |  | 4.1<br><sub>8,4,3,1,7</sub> |  | 1.5<br><sub>0,1,0,2,2</sub> |  | 1.1<br><sub>2,0,0,0,2</sub> |  | 0.5 | 0.7 | 1.5 | 17.1 |
| Jahmai Mashack | 38% | 18.4<br><sub>-,-,-,-,-</sub> | 6.0<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0 | 0.3 | 1.5 | 10.9 |
| Javon Small | 26% | 17.9 | 9.1 |  | 2.8 |  | 3.1 |  | 1.1 |  | 0.8 | 0.2 | 1.4 | 15.0 |
| Isaiah Stewart | 98% | 17.6<br><sub>-,16,22,15,16</sub> | 7.7<br><sub>-,4,13,4,18</sub> | 7.5 · 6.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>-,2,5,4,3</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 0.8<br><sub>-,0,2,0,0</sub> |  | 0.6<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.1 | 0.9 | 12.7 |
| Taylor Hendricks | 58% | 11.1<br><sub>-,-,7,-,3</sub> | 4.4<br><sub>-,-,0,-,0</sub> |  | 2.2<br><sub>-,-,1,-,1</sub> |  | 0.6<br><sub>-,-,0,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.4 | 0.5 | 7.3 |
| Olivier-Maxence Prosper | 48% | 11.0<br><sub>-,-,-,-,3</sub> | 6.4<br><sub>-,-,-,-,4</sub> |  | 2.3<br><sub>-,-,-,-,1</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 9.4 |
| Kris Murray | 58% | 9.8<br><sub>-,13,-,-,3</sub> | 2.5<br><sub>-,0,-,-,0</sub> |  | 1.6<br><sub>-,3,-,-,1</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.5 | 4.8 |
| Carson Cooper | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Karim Lopez | 48% | 6.9<br><sub>-,-,-,-,3</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 2.2 |

</details>


### CLE @ MIL
Out: Jaylon Tyson (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kel'el Ware PTS under 9.5 | CLE @ MIL | pointsbetau | 2.00 | 1.89 | 1.59 | 62.8% | 49.6% | 52.9% | +5.8% | +25.5% | 1.5% |
| Evan Mobley PTS under 17.5 | CLE @ MIL | pointsbetau | 2.00 | 1.95 | 1.78 | 56.0% | 49.6% | 51.2% | +2.4% | +12.0% | 0.6% |
| Jaime Jaquez Jr. PTS under 15.5 | CLE @ MIL | pointsbetau | 2.00 | 1.96 | 1.76 | 56.9% | 49.0% | 51.0% | +2.0% | +13.9% | 0.5% |
| Myles Turner PTS under 9.5 | CLE @ MIL | pointsbetau | 2.10 | 2.06 | 1.92 | 52.1% | 47.3% | 48.5% | +1.9% | +9.4% | 0.4% |
| Myles Turner PTS under 10.5 | CLE @ MIL | tab | 1.87 | 1.84 | 1.68 | 59.4% | 52.8% | 54.5% | +1.8% | +11.1% | 0.5% |
| Jaime Jaquez Jr. AST over 3.5 (4+) | CLE @ MIL | draftkings | 2.22 | 2.18 | 1.76 | 56.8% | 42.1% | 45.8% | +1.6% | +26.1% | 0.3% |
| Sam Merrill PTS under 9.5 | CLE @ MIL | tab | 1.95 | 1.92 | 1.88 | 53.2% | 51.5% | 52.0% | +1.5% | +3.9% | 0.4% |
| Tyler Herro PRA under 30.5 | CLE @ MIL | draftkings | 1.92 | 1.91 | 1.57 | 63.7% | 48.7% | 52.5% | +0.6% | +22.1% | 0.2% |
| Kyle Kuzma PTS under 11.5 | CLE @ MIL | unibet | 2.00 | 1.99 | 1.86 | 53.7% | 49.0% | 50.2% | +0.4% | +7.3% | 0.1% |
| Donovan Mitchell PTS over 24.5 (25+) | CLE @ MIL | pointsbetau | 2.00 | 1.99 | 1.88 | 53.1% | 49.2% | 50.2% | +0.3% | +6.2% | 0.1% |
| Tyler Herro PTS under 20.5 | CLE @ MIL | tab | 1.90 | 1.90 | 1.59 | 62.9% | 49.3% | 52.7% | +0.1% | +19.5% | 0.0% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 100% | 35.2<br><sub>33,33,39,34,36</sub> | 19.4<br><sub>16,12,19,16,24</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>3,8,5,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>5,7,9,6,4</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.4 | 3.2 | 30.9 |
| Donovan Mitchell | 100% | 35.0<br><sub>35,35,38,31,33</sub> | 26.6<br><sub>32,22,26,19,22</sub> | 24.5 · 23.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>10,5,5,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.9<br><sub>3,4,7,7,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>2,2,5,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.3 | 2.6 | 36.4 |
| Evan Mobley | 100% | 33.7<br><sub>34,35,38,32,33</sub> | 17.3<br><sub>18,20,18,24,11</sub> | 17.5 · 18.5<br><sub>o 49% · u 51%</sub> | 8.8<br><sub>8,10,10,12,4</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 3.5<br><sub>2,4,3,2,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.2<br><sub>1,2,4,5,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.9 | 1.5 | 1.7 | 29.6 |
| Peyton Watson | 100% | 29.6<br><sub>30,31,37,28,22</sub> | 14.0<br><sub>8,11,15,22,4</sub> | 13.5 · 13.5<br><sub>o 50% · u 50%</sub> | 4.6<br><sub>1,3,8,6,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>2,4,1,2,3</sub> |  | 1.2<br><sub>0,2,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.1 | 1.7 | 21.0 |
| Jarrett Allen | 100% | 29.0<br><sub>28,27,27,30,30</sub> | 13.4<br><sub>14,21,10,8,14</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 8.5<br><sub>7,8,9,12,8</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 1.6<br><sub>0,0,2,2,1</sub> |  | 0.1<br><sub>0,1,0,0,1</sub> |  | 1.2 | 1.3 | 1.2 | 23.5 |
| Sam Merrill | 98% | 24.2<br><sub>24,21,31,20,27</sub> | 9.9<br><sub>5,7,9,8,16</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 2.3<br><sub>5,2,4,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,3,2,1,3</sub> |  | 1.9<br><sub>1,1,1,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.1 | 0.6 | 14.2 |
| Meleek Thomas | 63% | 17.4<br><sub>-,-,19,20,-</sub> | 7.5<br><sub>-,-,16,10,-</sub> |  | 2.3<br><sub>-,-,2,4,-</sub> |  | 1.1<br><sub>-,-,0,1,-</sub> |  | 0.8<br><sub>-,-,4,0,-</sub> |  | 0.7 | 0.1 | 0.9 | 10.9 |
| Tyrese Proctor | 71% | 15.7<br><sub>5,11,-,6,20</sub> | 6.7<br><sub>0,5,-,2,7</sub> |  | 2.1<br><sub>0,2,-,1,6</sub> |  | 2.3<br><sub>0,3,-,1,2</sub> |  | 0.9<br><sub>0,1,-,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 11.2 |
| Mario Hezonja | 96% | 15.7<br><sub>19,20,15,17,17</sub> | 5.9<br><sub>10,9,3,5,10</sub> | 8.5 · –<br><sub>o 40% · u 60%</sub> | 3.0<br><sub>3,5,3,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>2,1,1,2,2</sub> |  | 0.7<br><sub>0,2,1,1,2</sub> | 1.5<br><sub>o 29% · u 71%</sub> | 0.5 | 0.3 | 0.6 | 10.1 |
| Craig Porter Jr. | 58% | 8.9<br><sub>8,5,-,-,4</sub> | 2.5<br><sub>0,3,-,-,0</sub> |  | 1.6<br><sub>3,1,-,-,1</sub> |  | 1.4<br><sub>0,1,-,-,0</sub> |  | 0.1<br><sub>0,1,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 5.5 |
| Ernest Udeh Jr. | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Thomas Bryant | 25% | 8.4<br><sub>-,-,-,-,-</sub> | 4.0<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 6.7 |
| Riley Minix | 23% | 7.0<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.7 |
| Tristan Enaruna | 23% | 5.9<br><sub>-,-,-,-,-</sub> | 2.1<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.6 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 100% | 31.4<br><sub>32,32,31,32,27</sub> | 18.8<br><sub>24,34,13,23,23</sub> | 21.5 · 21.5<br><sub>o 47% · u 53%</sub> | 4.5<br><sub>2,5,6,10,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>9,4,3,7,0</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,5,1,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 2.3 | 28.1 |
| Jaime Jaquez Jr. | 100% | 28.5<br><sub>31,35,27,25,27</sub> | 15.2<br><sub>22,19,21,8,19</sub> | 15.5 · 15.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>7,11,8,6,4</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 4.1<br><sub>2,5,4,0,2</sub> | 3.5<br><sub>o 46% · u 54%</sub> | 1.2<br><sub>1,2,2,0,3</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.8 | 0.3 | 2.0 | 24.8 |
| Ryan Rollins | 100% | 28.3<br><sub>24,34,25,32,17</sub> | 14.6<br><sub>9,11,15,19,4</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 4.0<br><sub>6,7,4,2,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>3,6,4,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.3 | 2.3 | 23.7 |
| Kyle Kuzma | 100% | 26.1<br><sub>27,30,35,29,18</sub> | 11.8<br><sub>5,14,14,17,4</sub> | 11.5 · 11.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>6,9,12,7,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.9<br><sub>3,4,3,3,1</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,2,0,4,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 1.7 | 19.7 |
| Myles Turner | 100% | 24.2<br><sub>32,30,20,28,22</sub> | 10.0<br><sub>11,12,0,6,4</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 4.8<br><sub>5,3,5,9,2</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 1.4<br><sub>3,1,1,4,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.7 | 1.6 | 1.3 | 16.2 |
| Kasparas Jakucionis | 88% | 19.2<br><sub>26,23,25,21,19</sub> | 6.6<br><sub>15,7,12,7,4</sub> | 7.5 · 7.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,2,3,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,5,2,5,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.6<br><sub>1,1,0,1,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.7 | 0.2 | 1.5 | 12.4 |
| AJ Green | 98% | 18.5<br><sub>15,17,19,20,24</sub> | 6.8<br><sub>6,11,11,3,9</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,3,4,1</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 1.2<br><sub>2,3,3,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.4 | 0.1 | 0.5 | 9.9 |
| Cormac Ryan | 26% | 17.6 | 8.8 |  | 2.0 |  | 1.2 |  | 1.1 |  | 0.7 | 0.2 | 1.1 | 12.1 |
| Kel'el Ware | 88% | 17.4<br><sub>14,15,29,19,17</sub> | 8.6<br><sub>7,11,19,16,6</sub> | 9.5 · 9.5<br><sub>o 47% · u 53%</sub> | 5.8<br><sub>3,4,13,14,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 0.6<br><sub>1,0,1,0,0</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.6 | 0.4 | 1.2 | 15.1 |
| Brayden Burries | 96% | 13.4<br><sub>16,8,17,16,17</sub> | 5.9<br><sub>12,3,10,4,10</sub> |  | 2.7<br><sub>5,1,5,2,5</sub> |  | 1.4<br><sub>0,3,2,1,1</sub> |  | 0.5<br><sub>2,1,1,0,0</sub> |  | 0.5 | 0.1 | 0.8 | 10.0 |
| Ousmane Dieng | 83% | 12.3<br><sub>21,16,-,3,13</sub> | 4.6<br><sub>5,3,-,0,4</sub> |  | 1.9<br><sub>4,1,-,0,0</sub> |  | 1.5<br><sub>3,1,-,0,0</sub> |  | 0.4<br><sub>1,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.8 | 8.1 |
| Nate Ament | 67% | 11.7<br><sub>-,-,11,14,20</sub> | 5.0<br><sub>-,-,1,7,8</sub> |  | 2.4<br><sub>-,-,3,3,4</sub> |  | 0.5<br><sub>-,-,0,0,0</sub> |  | 0.4<br><sub>-,-,0,1,1</sub> |  | 0.4 | 0.2 | 0.7 | 7.9 |
| Caris LeVert | 30% | 10.9<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.3 | 0.6 | 6.9 |
| Gary Trent Jr. | 52% | 9.2<br><sub>-,-,-,-,7</sub> | 3.9<br><sub>-,-,-,-,3</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,1</sub> |  | 0.3 | 0.0 | 0.3 | 4.9 |
| Jericho Sims | 52% | 9.1<br><sub>2,-,-,-,7</sub> | 3.0<br><sub>0,-,-,-,0</sub> |  | 2.8<br><sub>0,-,-,-,0</sub> |  | 0.9<br><sub>0,-,-,-,0</sub> |  | 0.0<br><sub>0,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 6.7 |
| Pete Nance | 30% | 8.9 | 2.9 |  | 1.5 |  | 0.6 |  | 0.3 |  | 0.2 | 0.2 | 0.3 | 5.0 |
| Kam Jones | 26% | 8.3 | 2.4 |  | 0.9 |  | 1.6 |  | 0.2 |  | 0.3 | 0.1 | 0.5 | 4.9 |
| Bogoljub Markovic | 48% | 6.2<br><sub>-,-,-,-,5</sub> | 2.4<br><sub>-,-,-,-,2</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.1<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 4.2 |

</details>


### MIN @ SAS
Out: Tobias Harris (SAS), Donte DiVincenzo (MIN), Anthony Edwards (MIN), Rudy Gobert (MIN)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julian Champagnie PTS under 10.5 | MIN @ SAS | tab | 2.00 | 1.89 | 1.67 | 59.9% | 50.4% | 52.8% | +5.6% | +19.9% | 1.4% |
| Joan Beringer PTS under 9.5 | MIN @ SAS | draftkings | 2.03 | 1.95 | 1.72 | 58.3% | 49.0% | 51.3% | +4.2% | +18.3% | 1.0% |
| Victor Wembanyama PTS under 24.5 | MIN @ SAS | pointsbetau | 2.00 | 1.94 | 1.90 | 52.7% | 51.3% | 51.6% | +3.3% | +5.4% | 0.8% |
| Devin Vassell PTS under 12.5 | MIN @ SAS | tab | 1.95 | 1.92 | 1.80 | 55.6% | 50.8% | 52.0% | +1.5% | +8.5% | 0.4% |
| LaMelo Ball PTS under 19.5 | MIN @ SAS | betright | 1.95 | 1.95 | 1.83 | 54.5% | 50.3% | 51.4% | +0.3% | +6.4% | 0.1% |

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 34.8<br><sub>30,31,37,35,33</sub> | 16.3<br><sub>15,14,14,19,23</sub> | 15.5 · 16.5<br><sub>o 49% · u 51%</sub> | 5.6<br><sub>6,6,6,7,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,4,4,7</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.4<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 1.1 | 0.9 | 1.8 | 24.7 |
| Ayo Dosunmu | 100% | 33.2<br><sub>27,23,26,32,30</sub> | 15.1<br><sub>14,9,9,17,15</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 4.6<br><sub>7,3,1,3,7</sub> | 3.5<br><sub>o 60% · u 40%</sub> | 4.1<br><sub>10,3,0,4,2</sub> | 3.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.4 | 1.8 | 23.9 |
| Jonathan Kuminga | 100% | 32.4<br><sub>27,26,36,32,22</sub> | 14.5<br><sub>11,13,10,20,5</sub> | 13.5 · 13.5<br><sub>o 52% · u 48%</sub> | 5.7<br><sub>8,4,10,3,1</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.2<br><sub>5,1,1,5,0</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 1.5<br><sub>2,3,0,3,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.5 | 1.4 | 22.4 |
| LaMelo Ball | 100% | 30.6<br><sub>23,17,31,28,29</sub> | 19.7<br><sub>12,15,11,8,24</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,1,0,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.8<br><sub>5,8,6,8,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>2,4,1,2,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.2 | 2.9 | 29.6 |
| Terrence Shannon Jr. | 97% | 26.6<br><sub>22,23,24,27,20</sub> | 13.7<br><sub>13,15,14,19,11</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 3.1<br><sub>4,4,4,6,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>1,3,5,2,2</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.6<br><sub>2,3,3,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.1 | 1.4 | 18.9 |
| Joan Beringer | 100% | 24.5<br><sub>15,13,17,20,18</sub> | 9.2<br><sub>9,6,12,7,4</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 8.1<br><sub>9,6,7,9,4</sub> | 8.5<br><sub>o 46% · u 54%</sub> | 0.9<br><sub>0,0,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 1.6 | 1.0 | 18.2 |
| Bones Hyland | 96% | 18.6<br><sub>8,15,5,16,20</sub> | 9.2<br><sub>3,3,0,13,19</sub> | 8.5 · 8.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>1,3,1,1,0</sub> |  | 2.4<br><sub>0,2,2,3,8</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>1,0,0,3,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 0.3 | 1.1 | 13.7 |
| Trey Lyles | 98% | 17.6<br><sub>17,14,13,22,17</sub> | 5.2<br><sub>9,3,3,7,10</sub> |  | 3.9<br><sub>6,6,1,3,5</sub> |  | 0.9<br><sub>2,2,1,1,0</sub> |  | 0.7<br><sub>2,1,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 10.0 |
| Jaylen Clark | 80% | 14.9<br><sub>3,5,-,7,17</sub> | 4.7<br><sub>0,3,-,3,5</sub> |  | 1.9<br><sub>2,1,-,2,0</sub> |  | 0.9<br><sub>1,0,-,1,2</sub> |  | 0.5<br><sub>0,0,-,1,1</sub> |  | 0.7 | 0.2 | 0.5 | 7.5 |
| Zyon Pullin | 64% | 10.2<br><sub>-,5,-,-,2</sub> | 3.6<br><sub>-,2,-,-,2</sub> |  | 1.1<br><sub>-,1,-,-,0</sub> |  | 1.3<br><sub>-,0,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 6.1 |
| Rocco Zikarsky | 16% | 10.1 | 3.2 |  | 3.2 |  | 0.5 |  | 0.0 |  | 0.2 | 0.9 | 0.4 | 6.9 |
| Enrique Freeman | 16% | 8.6 | 2.5 |  | 1.8 |  | 0.4 |  | 0.1 |  | 0.3 | 0.2 | 0.4 | 4.7 |
| Cody Williams | 58% | 8.0<br><sub>3,5,-,-,2</sub> | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.5<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 1.2 |
| Isaiah Evans | 63% | 7.8<br><sub>2,4,-,-,2</sub> | 0.4<br><sub>0,0,-,-,0</sub> |  | 1.6<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>1,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 2.5 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 100% | 34.0<br><sub>34,32,29,27,39</sub> | 25.1<br><sub>12,25,23,29,36</sub> | 24.5 · 24.5<br><sub>o 49% · u 51%</sub> | 11.3<br><sub>13,13,7,10,14</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,2,2,2,5</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>0,2,2,0,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2 | 3.6 | 2.8 | 39.5 |
| Devin Vassell | 100% | 33.1<br><sub>31,36,32,24,38</sub> | 12.4<br><sub>7,10,11,14,21</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>3,4,4,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>1,2,6,8,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,2,1,4,1</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.2 | 0.5 | 1.0 | 19.9 |
| De'Aaron Fox | 100% | 32.7<br><sub>32,34,28,26,39</sub> | 16.3<br><sub>14,19,19,11,14</sub> | 15.5 · 14.5<br><sub>o 49% · u 51%</sub> | 4.1<br><sub>7,4,3,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>7,9,9,6,4</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 1.5<br><sub>0,2,2,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.4 | 0.4 | 2.2 | 26.6 |
| Stephon Castle | 100% | 32.2<br><sub>28,33,28,27,38</sub> | 17.6<br><sub>24,15,19,15,14</sub> | 15.5 · 16.5<br><sub>o 49% · u 51%</sub> | 5.4<br><sub>7,7,4,5,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.3<br><sub>1,5,8,5,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>5,3,3,3,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 3.0 | 29.4 |
| Dylan Harper | 100% | 32.1<br><sub>32,36,28,30,37</sub> | 16.7<br><sub>18,20,22,13,13</sub> | 15.5 · 15.5<br><sub>o 51% · u 49%</sub> | 5.7<br><sub>7,3,5,6,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.1<br><sub>5,2,2,6,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>0,1,3,0,2</sub> | 0.5<br><sub>o 67% · u 33%</sub> | 1.1 | 0.4 | 1.9 | 26.5 |
| Julian Champagnie | 98% | 28.1<br><sub>30,25,28,25,31</sub> | 9.9<br><sub>8,6,12,26,6</sub> | 10.5 · 10.5<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>3,0,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>1,0,3,3,0</sub> |  | 1.8<br><sub>2,2,3,8,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 0.9 | 0.6 | 0.8 | 16.1 |
| Keldon Johnson | 98% | 20.6<br><sub>20,19,26,22,23</sub> | 9.9<br><sub>10,8,7,14,9</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 4.2<br><sub>4,6,6,4,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,1,3,0,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 0.6 | 0.2 | 0.9 | 15.2 |
| Luke Kornet | 98% | 13.9<br><sub>13,16,14,17,14</sub> | 3.3<br><sub>4,7,0,0,1</sub> |  | 4.0<br><sub>1,3,4,4,6</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 8.2 |
| Harrison Barnes | 67% | 8.5<br><sub>9,5,4,14,-</sub> | 2.8<br><sub>3,0,0,3,-</sub> |  | 1.1<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Carter Bryant | 98% | 8.1<br><sub>6,4,10,17,5</sub> | 2.5<br><sub>0,0,4,1,3</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>1,0,0,2,0</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.2 | 0.2 | 0.4 | 4.5 |
| Maliq Brown | 80% | 6.9<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 2.5<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 3.1 |
| Jordan McLaughlin | 52% | 6.3<br><sub>-,-,3,7,-</sub> | 2.2<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 1.0<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.1 |
| Ja'Kobi Gillespie | 88% | 5.9<br><sub>1,-,3,-,-</sub> | 4.2<br><sub>2,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>0,-,1,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 5.0 |
| Tarris Reed Jr. | 58% | 5.9<br><sub>1,-,7,5,-</sub> | 2.4<br><sub>0,-,2,4,-</sub> |  | 2.2<br><sub>0,-,3,5,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.8 | 5.0 |
| David Jones Garcia | 52% | 5.7<br><sub>1,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |

</details>


### OKC @ HOU
Out: Steven Adams (HOU), Reed Sheppard (HOU), Fred VanVleet (HOU), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson PRA over 27.5 (28+) | OKC @ HOU | draftkings | 1.85 | 1.84 | 1.53 | 65.2% | 50.8% | 54.4% | +0.9% | +20.9% | 0.2% |
| Kevin Durant PA over 26.5 (27+) | OKC @ HOU | draftkings | 1.95 | 1.94 | 1.61 | 62.1% | 48.0% | 51.5% | +0.5% | +21.2% | 0.1% |
| Marcus Smart 3PM under 1.5 | OKC @ HOU | draftkings | 1.92 | 1.91 | 1.59 | 62.8% | 48.7% | 52.2% | +0.2% | +20.4% | 0.1% |
| Shai Gilgeous-Alexander STL over 1.5 (2+) | OKC @ HOU | draftkings | 2.72 | 2.72 | 2.28 | 43.8% | 34.4% | 36.8% | +0.0% | +19.2% | 0.0% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.6<br><sub>36,35,36,30,28</sub> | 30.4<br><sub>32,17,34,26,21</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,2,6,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 6.7<br><sub>4,3,5,3,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.9 | 3.3 | 41.0 |
| Jared McCain | 98% | 30.0<br><sub>22,18,21,30,29</sub> | 15.9<br><sub>20,4,3,18,10</sub> | 14.5 · –<br><sub>o 51% · u 49%</sub> | 2.9<br><sub>2,0,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,1,0,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>6,0,1,4,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.9 | 21.1 |
| Ajay Mitchell | 98% | 29.6<br><sub>23,23,28,25,28</sub> | 19.0<br><sub>4,12,18,30,29</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 3.5<br><sub>5,0,6,2,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>6,0,4,5,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.3 | 2.2 | 26.9 |
| Josh Dix | 67% | 27.2<br><sub>-,-,-,22,24</sub> | 4.4<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.4 |
| Bennett Stirtz | 96% | 26.7<br><sub>1,2,11,25,28</sub> | 7.9<br><sub>0,0,2,7,8</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 1.0<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.1 |
| Isaiah Hartenstein | 98% | 26.6<br><sub>17,23,27,26,26</sub> | 10.2<br><sub>4,6,12,15,10</sub> | 9.5 · –<br><sub>o 51% · u 49%</sub> | 9.5<br><sub>3,6,12,13,14</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,2,1,3,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 22.9 |
| Aday Mara | 96% | 24.2<br><sub>12,13,14,20,21</sub> | 8.2<br><sub>7,2,2,11,6</sub> | 7.5 · –<br><sub>o 51% · u 49%</sub> | 6.2<br><sub>2,3,3,10,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.4 | 15.6 |
| Kenrich Williams | 93% | 21.7<br><sub>7,6,7,24,17</sub> | 8.0<br><sub>3,3,3,3,7</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>2,1,1,7,3</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.9 | 13.9 |
| Jaylin Williams | 98% | 21.3<br><sub>17,15,5,26,20</sub> | 6.1<br><sub>5,3,0,6,0</sub> | 7.5 · –<br><sub>o 43% · u 57%</sub> | 5.3<br><sub>4,7,0,6,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 2.0<br><sub>1,3,0,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9<br><sub>1,1,0,2,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.6 | 0.5 | 0.8 | 13.3 |
| Micah Peavy | 48% | 13.1<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer | 80% | 13.0<br><sub>1,2,-,3,14</sub> | 3.5<br><sub>0,0,-,0,3</sub> |  | 2.5<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.8<br><sub>36,39,28,33,39</sub> | 18.8<br><sub>20,17,15,23,15</sub> | 15.5 · –<br><sub>o 54% · u 46%</sub> | 7.4<br><sub>10,11,5,4,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>4,6,2,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.8 | 31.9 |
| Kevin Durant | 98% | 37.6<br><sub>37,37,30,31,37</sub> | 25.8<br><sub>20,22,22,18,28</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>7,4,9,5,5</sub> | 4.5<br><sub>o 60% · u 40%</sub> | 5.1<br><sub>6,2,3,4,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,3,1,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 1.0 | 3.8 | 37.4 |
| Jabari Smith Jr. | 98% | 37.1<br><sub>34,33,39,30,35</sub> | 17.4<br><sub>7,14,16,14,22</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>5,5,12,2,3</sub> | 5.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>1,3,5,2,2</sub> |  | 2.7<br><sub>1,2,2,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.8 | 1.8 | 27.0 |
| Alperen Sengun | 58% | 35.4<br><sub>36,33,37,-,-</sub> | 19.7<br><sub>29,17,29,-,-</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 10.0<br><sub>7,10,9,-,-</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>7,7,9,-,-</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.7<br><sub>2,1,1,-,-</sub> |  | 1.2 | 0.9 | 3.6 | 36.0 |
| Tari Eason | 98% | 30.9<br><sub>27,31,33,31,26</sub> | 12.6<br><sub>12,19,13,5,11</sub> | 10.5 · –<br><sub>o 52% · u 48%</sub> | 7.4<br><sub>6,3,8,9,13</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.6<br><sub>0,0,2,1,2</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 1.4 | 0.7 | 1.5 | 21.7 |
| Marcus Smart | 63% | 26.0<br><sub>21,-,-,-,17</sub> | 9.2<br><sub>5,-,-,-,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,-,-,-,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>1,-,-,-,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,-,-,-,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.3 | 1.9 | 15.2 |
| Clint Capela | 88% | 22.3<br><sub>-,11,4,22,30</sub> | 6.5<br><sub>-,2,2,10,5</sub> |  | 7.8<br><sub>-,3,2,8,11</sub> |  | 1.4<br><sub>-,1,0,2,5</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.2 | 0.9 | 15.7 |
| Bogdan Bogdanovic | 91% | 19.5<br><sub>9,20,13,15,11</sub> | 7.8<br><sub>3,11,5,16,6</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 2.4<br><sub>1,1,2,2,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.9<br><sub>0,1,1,4,0</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.3<br><sub>1,3,1,4,0</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 0.6 | 0.2 | 0.9 | 12.1 |
| Oscar Tshiebwe | 76% | 16.5<br><sub>-,-,-,14,11</sub> | 6.3<br><sub>-,-,-,7,0</sub> |  | 6.8<br><sub>-,-,-,5,5</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.4 | 1.0 | 14.0 |
| Jae'Sean Tate | 64% | 9.5<br><sub>-,1,1,4,-</sub> | 3.1<br><sub>-,0,0,0,-</sub> |  | 2.1<br><sub>-,0,1,0,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Bruce Thornton | 63% | 8.7<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,0,0,5,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Isaiah Crawford | 58% | 8.3<br><sub>-,1,1,5,-</sub> | 2.7<br><sub>-,0,0,3,-</sub> |  | 1.5<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-31/`._
