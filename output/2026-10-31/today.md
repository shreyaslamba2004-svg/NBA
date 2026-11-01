# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sun 01 Nov, 11:07 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey PTS over 8.5 (9+) | SAC @ MEM | pointsbetau | 2.05 | 1.85 | 1.62 | 61.9% | 51.6% | 54.2% | +11.1% | +26.8% | 2.0% |
| Tari Eason REB over 7.5 (8+) | OKC @ HOU | draftkings | 3.90 | 3.61 | 2.58 | 38.8% | 24.0% | 27.7% | +7.9% | +51.4% | 0.7% |
| Jaylen Wells PTS over 11.5 (12+) | SAC @ MEM | unibet | 1.66 | 1.56 | 1.34 | 74.6% | 60.6% | 64.1% | +6.2% | +23.6% | 2.0% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 7.5 (8+) | OKC @ HOU | draftkings | 21.00 | 14.37 | 6.90 | 14.5% | 4.5% | 7.0% | +46.2% | +204.4% | 0.6% |
| Cameron Boozer REB over 13.5 (14+) | SAC @ MEM | draftkings | 10.60 | 8.22 | 4.50 | 22.2% | 8.8% | 12.2% | +28.9% | +135.3% | 0.8% |
| Cameron Boozer REB over 15.5 (16+) | SAC @ MEM | draftkings | 20.00 | 15.82 | 8.89 | 11.2% | 4.7% | 6.3% | +26.3% | +125.0% | 0.4% |
| Jerami Grant PTS over 24.5 (25+) | SAC @ MEM | draftkings | 19.00 | 16.18 | 10.05 | 10.0% | 4.9% | 6.2% | +17.3% | +89.0% | 0.2% |
| Tari Eason REB over 9.5 (10+) | OKC @ HOU | draftkings | 9.40 | 8.12 | 5.15 | 19.4% | 9.9% | 12.3% | +15.7% | +82.5% | 0.5% |
| Jerami Grant PTS over 19.5 (20+) | SAC @ MEM | draftkings | 7.50 | 6.49 | 4.12 | 24.3% | 12.5% | 15.4% | +15.7% | +82.2% | 0.6% |
| Cedric Coward REB over 11.5 (12+) | SAC @ MEM | draftkings | 15.40 | 13.39 | 8.57 | 11.7% | 6.1% | 7.5% | +15.0% | +79.8% | 0.3% |
| MIN to win | MIN @ SAS | ladbrokes_au | 6.25 | 5.49 | 4.32 | 23.1% | 18.2% | 18.2% | +13.9% | +44.6% | 0.7% |
| Zach Edey REB over 15.5 (16+) | SAC @ MEM | draftkings | 19.60 | 17.21 | 11.19 | 8.9% | 4.8% | 5.8% | +13.9% | +75.2% | 0.2% |
| Jaylen Wells PRA over 34.5 (35+) | SAC @ MEM | draftkings | 19.80 | 17.54 | 11.57 | 8.6% | 4.7% | 5.7% | +12.9% | +71.1% | 0.2% |
| Zach Edey REB over 13.5 (14+) | SAC @ MEM | draftkings | 9.90 | 8.78 | 5.80 | 17.2% | 9.4% | 11.4% | +12.8% | +70.8% | 0.4% |
| Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings | 28.00 | 24.88 | 16.46 | 6.1% | 3.3% | 4.0% | +12.6% | +70.1% | 0.1% |
| Tari Eason REB over 11.5 (12+) | OKC @ HOU | draftkings | 21.00 | 18.66 | 12.35 | 8.1% | 4.5% | 5.4% | +12.6% | +70.1% | 0.2% |
| Shai Gilgeous-Alexander PTS over 44.5 (45+) | OKC @ HOU | draftkings | 15.20 | 13.57 | 9.07 | 11.0% | 6.2% | 7.4% | +12.0% | +67.6% | 0.2% |
| Kevin Durant REB over 9.5 (10+) | OKC @ HOU | draftkings | 14.60 | 13.04 | 8.71 | 11.5% | 6.4% | 7.7% | +12.0% | +67.5% | 0.2% |
| Shai Gilgeous-Alexander PRA over 59.5 (60+) | OKC @ HOU | draftkings | 20.20 | 18.21 | 12.40 | 8.1% | 4.6% | 5.5% | +10.8% | +62.9% | 0.1% |
| Donovan Mitchell PTS over 44.5 (45+) | CLE @ MIL | draftkings | 26.00 | 23.47 | 16.01 | 6.2% | 3.6% | 4.3% | +10.7% | +62.4% | 0.1% |
| Jaylen Wells PRA over 29.5 (30+) | SAC @ MEM | draftkings | 8.70 | 7.87 | 5.38 | 18.6% | 10.7% | 12.7% | +10.5% | +61.8% | 0.3% |
| Jaylen Wells PR over 29.5 (30+) | SAC @ MEM | draftkings | 12.60 | 11.43 | 7.84 | 12.8% | 7.4% | 8.8% | +10.2% | +60.6% | 0.2% |
| Kevin Durant REB over 7.5 (8+) | OKC @ HOU | draftkings | 5.62 | 5.10 | 3.51 | 28.5% | 16.6% | 19.6% | +10.2% | +60.2% | 0.5% |
| Precious Achiuwa PA over 24.5 (25+) | SAC @ MEM | draftkings | 9.90 | 9.01 | 6.22 | 16.1% | 9.4% | 11.1% | +9.9% | +59.1% | 0.3% |
| Donovan Mitchell PTS over 39.5 (40+) | CLE @ MIL | draftkings | 13.40 | 12.22 | 8.48 | 11.8% | 7.0% | 8.2% | +9.6% | +58.0% | 0.2% |
| Cedric Coward REB over 9.5 (10+) | SAC @ MEM | draftkings | 6.27 | 5.74 | 4.00 | 25.0% | 14.9% | 17.4% | +9.3% | +56.7% | 0.4% |
| Darius Acuff Jr. REB over 7.5 (8+) | SAC @ MEM | draftkings | 16.20 | 14.86 | 10.38 | 9.6% | 5.8% | 6.7% | +9.1% | +56.0% | 0.1% |
| Darius Acuff Jr. REB over 5.5 (6+) | SAC @ MEM | draftkings | 5.31 | 4.87 | 3.41 | 29.4% | 17.6% | 20.5% | +9.1% | +55.9% | 0.5% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer REB over 14.5 (15+) | SAC @ MEM | draftkings | 15.00 | 11.53 | 6.25 | 16.0% | 6.2% | 8.7% | +30.1% | +140.0% | 0.5% |
| Cameron Boozer REB over 16.5 (17+) | SAC @ MEM | draftkings | 26.00 | 21.93 | 13.41 | 7.5% | 3.6% | 4.6% | +18.6% | +93.9% | 0.2% |
| Tari Eason REB over 10.5 (11+) | OKC @ HOU | draftkings | 14.40 | 12.48 | 7.97 | 12.6% | 6.5% | 8.0% | +15.3% | +80.8% | 0.3% |
| Zach Edey REB over 14.5 (15+) | SAC @ MEM | draftkings | 14.00 | 12.29 | 7.99 | 12.5% | 6.7% | 8.1% | +13.9% | +75.3% | 0.3% |
| Cedric Coward REB over 10.5 (11+) | SAC @ MEM | draftkings | 10.00 | 8.83 | 5.78 | 17.3% | 9.3% | 11.3% | +13.3% | +72.9% | 0.4% |
| Kevin Durant REB over 8.5 (9+) | OKC @ HOU | draftkings | 9.20 | 8.17 | 5.41 | 18.5% | 10.2% | 12.2% | +12.6% | +70.2% | 0.4% |
| Tari Eason REB over 8.5 (9+) | OKC @ HOU | draftkings | 5.96 | 5.30 | 3.52 | 28.4% | 15.7% | 18.9% | +12.4% | +69.4% | 0.6% |
| Zach Edey REB over 12.5 (13+) | SAC @ MEM | draftkings | 7.00 | 6.31 | 4.28 | 23.3% | 13.4% | 15.8% | +10.9% | +63.4% | 0.5% |
| Darius Acuff Jr. REB over 6.5 (7+) | SAC @ MEM | draftkings | 9.20 | 8.31 | 5.66 | 17.7% | 10.2% | 12.0% | +10.7% | +62.6% | 0.3% |
| Cedric Coward REB over 12.5 (13+) | SAC @ MEM | draftkings | 22.00 | 19.88 | 13.54 | 7.4% | 4.2% | 5.0% | +10.7% | +62.5% | 0.1% |
| Zach Edey REB over 16.5 (17+) | SAC @ MEM | draftkings | 25.00 | 22.88 | 15.97 | 6.3% | 3.7% | 4.4% | +9.2% | +56.5% | 0.1% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 23.00 | 21.19 | 14.95 | 6.7% | 4.1% | 4.7% | +8.6% | +53.9% | 0.1% |
| Amen Thompson AST over 8.5 (9+) | OKC @ HOU | draftkings | 14.20 | 13.12 | 9.33 | 10.7% | 6.6% | 7.6% | +8.2% | +52.2% | 0.1% |
| Shai Gilgeous-Alexander AST over 10.5 (11+) | OKC @ HOU | draftkings | 15.20 | 14.10 | 10.10 | 9.9% | 6.2% | 7.1% | +7.7% | +50.5% | 0.1% |
| Kenrich Williams REB over 8.5 (9+) | OKC @ HOU | draftkings | 11.20 | 10.45 | 7.55 | 13.2% | 8.3% | 9.6% | +7.2% | +48.3% | 0.2% |
| Precious Achiuwa REB over 12.5 (13+) | SAC @ MEM | draftkings | 9.60 | 9.00 | 6.56 | 15.2% | 9.7% | 11.1% | +6.7% | +46.2% | 0.2% |
| Kenrich Williams REB over 6.5 (7+) | OKC @ HOU | draftkings | 4.56 | 4.28 | 3.14 | 31.9% | 20.5% | 23.3% | +6.4% | +45.3% | 0.4% |
| Kevin Durant REB over 6.5 (7+) | OKC @ HOU | draftkings | 3.53 | 3.32 | 2.43 | 41.1% | 26.5% | 30.1% | +6.4% | +45.2% | 0.6% |
| Jabari Smith Jr. REB over 10.5 (11+) | OKC @ HOU | draftkings | 11.00 | 10.36 | 7.62 | 13.1% | 8.5% | 9.7% | +6.2% | +44.4% | 0.2% |
| Cedric Coward REB over 8.5 (9+) | SAC @ MEM | draftkings | 4.15 | 3.92 | 2.89 | 34.6% | 22.5% | 25.5% | +6.0% | +43.6% | 0.5% |
| Julian Champagnie PTS under 10.5 | MIN @ SAS | tab | 2.00 | 1.89 | 1.66 | 60.2% | 50.4% | 52.8% | +5.7% | +20.4% | 1.4% |
| Tari Eason REB over 12.5 (13+) | OKC @ HOU | draftkings | 29.00 | 27.47 | 20.40 | 4.9% | 3.2% | 3.6% | +5.6% | +42.1% | 0.1% |
| De'Andre Hunter REB over 8.5 (9+) | SAC @ MEM | draftkings | 10.50 | 9.94 | 7.39 | 13.5% | 8.9% | 10.1% | +5.6% | +42.1% | 0.1% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer REB over 9.5 (10+) | SAC @ MEM | draftkings | 2.84 | 2.53 | 1.69 | 59.2% | 32.9% | 39.5% | +12.1% | +68.0% | 1.6% |
| AJ Green 3PM under 1.5 | CLE @ MIL | draftkings | 2.33 | 2.14 | 1.51 | 66.2% | 40.1% | 46.6% | +8.7% | +54.3% | 1.6% |
| Jerami Grant PTS over 14.5 (15+) | SAC @ MEM | draftkings | 3.09 | 2.85 | 2.02 | 49.6% | 30.2% | 35.1% | +8.4% | +53.2% | 1.0% |
| Joan Beringer PR under 18.5 | MIN @ SAS | draftkings | 1.90 | 1.76 | 1.25 | 80.1% | 49.2% | 56.9% | +8.2% | +52.3% | 2.0% |
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.14 | 1.99 | 1.43 | 69.8% | 43.9% | 50.4% | +7.8% | +49.4% | 1.7% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 2.00 | 1.87 | 1.35 | 73.9% | 46.9% | 53.6% | +7.2% | +47.7% | 1.8% |
| Kenrich Williams PTS over 6.5 (7+) | OKC @ HOU | pointsbetau | 1.90 | 1.78 | 1.40 | 71.2% | 51.0% | 56.1% | +6.6% | +35.4% | 1.8% |
| Jaylin Williams 3PM under 1.5 | OKC @ HOU | draftkings | 1.82 | 1.72 | 1.28 | 78.2% | 51.4% | 58.1% | +5.7% | +42.3% | 1.7% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| SAC @ MEM | Sun 01 Nov 11:00 | 115.8–122.4 | SAC 32% | 3.12 / 1.47 | MEM -6.5 | 238.5 | MEM -7.5 covers 47%; o229.5 68% |
| CLE @ MIL | Sun 01 Nov 11:00 | 118.8–114.7 | CLE 61% | 1.63 / 2.60 | MIL +4.5 | 233.5 | MIL +8.5 covers 62%; o234.5 48% |
| MIN @ SAS | Sun 01 Nov 11:00 | 107.9–118.3 | MIN 23% | 4.32 / 1.30 | SAS -10.5 | 226.5 | SAS -12.5 covers 44%; o230.5 41% |
| OKC @ HOU | Sun 01 Nov 11:30 | 112.1–113.1 | OKC 47% | 2.12 / 1.90 | HOU -1.5 | 225.5 | HOU -2.5 covers 47%; o219.5 61% |

### SAC @ MEM
Out: Ty Jerome (MEM), Scotty Pippen Jr. (MEM), Quinten Post (MEM), Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey PTS over 8.5 (9+) | SAC @ MEM | pointsbetau | 2.05 | 1.85 | 1.62 | 61.9% | 51.6% | 54.2% | +11.1% | +26.8% | 2.0% |
| Jaylen Wells PTS over 11.5 (12+) | SAC @ MEM | unibet | 1.66 | 1.56 | 1.34 | 74.6% | 60.6% | 64.1% | +6.2% | +23.6% | 2.0% |
| Jaylen Wells PTS over 13.5 (14+) | SAC @ MEM | sportsbet | 1.96 | 1.90 | 1.57 | 63.5% | 48.9% | 52.6% | +3.1% | +24.6% | 0.8% |
| Zach LaVine PTS under 21.5 | SAC @ MEM | betright | 1.98 | 1.94 | 1.78 | 56.1% | 50.0% | 51.5% | +2.1% | +11.2% | 0.5% |
| Cam Spencer 3PM under 1.5 | SAC @ MEM | draftkings | 2.43 | 2.40 | 1.94 | 51.6% | 38.5% | 41.7% | +1.4% | +25.3% | 0.2% |
| Precious Achiuwa PA over 14.5 (15+) | SAC @ MEM | draftkings | 1.88 | 1.87 | 1.55 | 64.6% | 49.9% | 53.6% | +1.0% | +21.8% | 0.3% |
| Zach Edey PRA over 18.5 (19+) | SAC @ MEM | draftkings | 1.90 | 1.89 | 1.58 | 63.3% | 49.5% | 52.9% | +0.6% | +20.3% | 0.2% |
| Cedric Coward REB over 6.5 (7+) | SAC @ MEM | draftkings | 2.06 | 2.05 | 1.70 | 58.9% | 45.5% | 48.8% | +0.6% | +21.2% | 0.1% |
| Cam Spencer AST under 6.5 | SAC @ MEM | draftkings | 1.95 | 1.94 | 1.60 | 62.3% | 47.9% | 51.5% | +0.5% | +21.6% | 0.1% |
| Domantas Sabonis PTS over 15.5 (16+) | SAC @ MEM | unibet | 1.88 | 1.88 | 1.64 | 61.1% | 50.7% | 53.3% | +0.5% | +15.1% | 0.1% |
| Zach Edey RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.98 | 1.97 | 1.64 | 61.0% | 47.3% | 50.7% | +0.4% | +20.7% | 0.1% |
| Precious Achiuwa REB over 7.5 (8+) | SAC @ MEM | draftkings | 1.90 | 1.89 | 1.59 | 63.0% | 49.4% | 52.8% | +0.3% | +19.8% | 0.1% |
| Precious Achiuwa RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.99 | 1.98 | 1.65 | 60.6% | 47.0% | 50.4% | +0.3% | +20.6% | 0.1% |
| Darius Acuff Jr. RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.94 | 1.94 | 1.62 | 61.8% | 48.2% | 51.6% | +0.2% | +20.1% | 0.1% |
| Zach Edey PR over 17.5 (18+) | SAC @ MEM | draftkings | 1.94 | 1.94 | 1.64 | 61.0% | 48.4% | 51.6% | +0.2% | +18.6% | 0.1% |
| De'Andre Hunter REB over 4.5 (5+) | SAC @ MEM | draftkings | 1.92 | 1.91 | 1.61 | 62.2% | 48.9% | 52.3% | +0.2% | +19.2% | 0.1% |
| Jaylen Wells PRA over 19.5 (20+) | SAC @ MEM | draftkings | 1.96 | 1.96 | 1.65 | 60.6% | 47.9% | 51.0% | +0.1% | +18.8% | 0.0% |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.0<br><sub>12,33,22,19,34</sub> | 23.5 · 23.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.5 | 33.9 |
| Zach LaVine | 98% | 34.1<br><sub>34,39,40,31,39</sub> | 21.3<br><sub>28,22,37,22,21</sub> | 21.5 · 21.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 50% · u 50%</sub> | 0.9 | 0.3 | 2.6 | 28.1 |
| Domantas Sabonis | 98% | 34.0<br><sub>34,39,35,37,40</sub> | 18.4<br><sub>14,27,15,20,9</sub> | 16.5 · 15.5<br><sub>o 53% · u 47%</sub> | 14.0<br><sub>18,19,15,14,15</sub> | 14.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 45% · u 55%</sub> | 0.3<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 23% · u 77%</sub> | 0.9 | 0.4 | 3.1 | 38.4 |
| Precious Achiuwa | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.8<br><sub>15,14,12,4,24</sub> | 12.5 · 12.5<br><sub>o 54% · u 46%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 53% · u 47%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.4<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 30% · u 70%</sub> | 1.5 | 1.1 | 1.7 | 26.7 |
| De'Andre Hunter | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.2<br><sub>6,4,7,24,24</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 5.5<br><sub>3,7,6,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,2,5,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.8 | 20.5 |
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
| Cameron Boozer | 96% | 33.5<br><sub>33,37,31,31,28</sub> | 18.7<br><sub>7,25,14,13,18</sub> | 18.5 · 17.5<br><sub>o 49% · u 51%</sub> | 10.7<br><sub>11,13,11,7,12</sub> | 7.5<br><sub>o 59% · u 41%</sub> | 6.7<br><sub>5,6,4,4,12</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 2.1<br><sub>0,4,2,1,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.5 | 0.7 | 2.4 | 36.0 |
| Cedric Coward | 98% | 30.4<br><sub>28,-,32,31,27</sub> | 17.9<br><sub>7,-,17,16,17</sub> | 16.5 · 16.5<br><sub>o 50% · u 50%</sub> | 7.5<br><sub>7,-,11,11,7</sub> | 6.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>2,-,1,3,4</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 2.0<br><sub>1,-,3,4,3</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.0 | 0.5 | 2.0 | 29.2 |
| Jaylen Wells | 98% | 30.3<br><sub>28,25,33,30,25</sub> | 16.8<br><sub>12,17,16,14,10</sub> | 14.5 · 13.5<br><sub>o 53% · u 47%</sub> | 3.7<br><sub>5,4,5,3,1</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 2.1<br><sub>0,3,3,0,0</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 2.3<br><sub>1,4,2,2,2</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.1 | 0.2 | 1.3 | 22.6 |
| Jerami Grant | 98% | 27.3<br><sub>24,26,22,24,27</sub> | 15.3<br><sub>15,6,5,13,2</sub> | 11.5 · –<br><sub>o 52% · u 48%</sub> | 3.0<br><sub>2,0,5,3,1</sub> |  | 2.4<br><sub>3,3,3,0,3</sub> |  | 1.8<br><sub>2,1,1,3,0</sub> | 1.5<br><sub>o 51% · u 49%</sub> | 0.8 | 0.8 | 1.7 | 20.7 |
| Zach Edey | 98% | 24.3<br><sub>21,22,-,21,19</sub> | 10.7<br><sub>6,8,-,4,13</sub> | 8.5 · 8.5<br><sub>o 51% · u 49%</sub> | 9.6<br><sub>9,10,-,3,7</sub> | 7.5<br><sub>o 58% · u 42%</sub> | 1.5<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.7 | 1.7 | 1.7 | 21.9 |
| Cam Spencer | 96% | 22.9<br><sub>16,17,16,18,23</sub> | 11.0<br><sub>3,11,13,8,8</sub> | 12.5 · 11.5<br><sub>o 49% · u 51%</sub> | 3.0<br><sub>3,2,2,5,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>2,1,1,5,8</sub> | 6.5<br><sub>o 48% · u 52%</sub> | 1.6<br><sub>1,3,3,2,1</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 0.8 | 0.2 | 1.2 | 19.9 |
| GG Jackson | 96% | 19.6<br><sub>19,15,10,16,21</sub> | 11.9<br><sub>12,2,1,4,12</sub> |  | 4.2<br><sub>8,4,3,1,7</sub> |  | 1.5<br><sub>0,1,0,2,2</sub> |  | 1.1<br><sub>2,0,0,0,2</sub> |  | 0.5 | 0.7 | 1.6 | 17.6 |
| Jahmai Mashack | 38% | 18.8<br><sub>-,-,-,-,-</sub> | 6.1<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0 | 0.4 | 1.5 | 11.0 |
| Javon Small | 26% | 18.8 | 9.7 |  | 3.0 |  | 3.3 |  | 1.1 |  | 0.9 | 0.2 | 1.5 | 16.1 |
| Isaiah Stewart | 98% | 17.7<br><sub>-,16,22,15,16</sub> | 7.8<br><sub>-,4,13,4,18</sub> | 7.5 · 6.5<br><sub>o 52% · u 48%</sub> | 4.2<br><sub>-,2,5,4,3</sub> | 3.5<br><sub>o 52% · u 48%</sub> | 0.9<br><sub>-,0,2,0,0</sub> |  | 0.6<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.1 | 0.9 | 12.9 |
| Taylor Hendricks | 58% | 11.4<br><sub>-,-,7,-,3</sub> | 4.6<br><sub>-,-,0,-,0</sub> |  | 2.3<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.4 | 0.6 | 7.6 |
| Olivier-Maxence Prosper | 48% | 11.4<br><sub>-,-,-,-,3</sub> | 6.6<br><sub>-,-,-,-,4</sub> |  | 2.4<br><sub>-,-,-,-,1</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 9.7 |
| Kris Murray | 58% | 10.2<br><sub>-,13,-,-,3</sub> | 2.6<br><sub>-,0,-,-,0</sub> |  | 1.6<br><sub>-,3,-,-,1</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.0 |
| Carson Cooper | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Karim Lopez | 48% | 6.9<br><sub>-,-,-,-,3</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 2.2 |

</details>


### CLE @ MIL
Out: Jaylon Tyson (CLE)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kel'el Ware PTS under 9.5 | CLE @ MIL | pointsbetau | 2.00 | 1.91 | 1.64 | 61.2% | 49.5% | 52.4% | +4.9% | +22.3% | 1.2% |
| Jaime Jaquez Jr. PTS under 15.5 | CLE @ MIL | pointsbetau | 2.00 | 1.92 | 1.64 | 61.1% | 49.0% | 52.0% | +4.1% | +22.1% | 1.0% |
| Myles Turner PTS under 10.5 | CLE @ MIL | tab | 1.87 | 1.82 | 1.64 | 61.0% | 52.8% | 54.9% | +2.6% | +14.1% | 0.7% |
| Myles Turner PTS under 9.5 | CLE @ MIL | pointsbetau | 2.10 | 2.05 | 1.88 | 53.3% | 47.3% | 48.8% | +2.6% | +11.9% | 0.6% |
| Evan Mobley PTS under 17.5 | CLE @ MIL | pointsbetau | 2.00 | 1.97 | 1.84 | 54.4% | 49.6% | 50.8% | +1.6% | +8.8% | 0.4% |
| Myles Turner RA under 6.5 | CLE @ MIL | draftkings | 2.05 | 2.03 | 1.66 | 60.4% | 45.7% | 49.4% | +1.2% | +23.8% | 0.3% |
| Sam Merrill PTS under 9.5 | CLE @ MIL | tab | 1.95 | 1.93 | 1.98 | 50.6% | 52.1% | 51.8% | +1.1% | -1.2% | 0.3% |
| Kyle Kuzma PTS under 11.5 | CLE @ MIL | unibet | 2.00 | 1.98 | 1.83 | 54.6% | 49.0% | 50.4% | +0.8% | +9.1% | 0.2% |
| Donovan Mitchell PTS over 24.5 (25+) | CLE @ MIL | pointsbetau | 2.00 | 1.99 | 1.85 | 53.9% | 49.0% | 50.2% | +0.4% | +7.8% | 0.1% |
| Tyler Herro PRA under 30.5 | CLE @ MIL | draftkings | 1.92 | 1.91 | 1.58 | 63.1% | 48.7% | 52.3% | +0.4% | +21.1% | 0.1% |
| Kyle Kuzma REB under 5.5 | CLE @ MIL | draftkings | 1.86 | 1.86 | 1.55 | 64.6% | 50.2% | 53.8% | +0.2% | +20.3% | 0.1% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.5<br><sub>33,33,39,34,36</sub> | 19.5<br><sub>16,12,19,16,24</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>3,8,5,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>5,7,9,6,4</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.4 | 3.3 | 31.2 |
| Donovan Mitchell | 98% | 35.1<br><sub>35,35,38,31,33</sub> | 26.8<br><sub>32,22,26,19,22</sub> | 24.5 · 23.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>10,5,5,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.9<br><sub>3,4,7,7,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>2,2,5,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.3 | 2.6 | 36.7 |
| Evan Mobley | 98% | 34.0<br><sub>34,35,38,32,33</sub> | 17.6<br><sub>18,20,18,24,11</sub> | 17.5 · 18.5<br><sub>o 49% · u 51%</sub> | 8.8<br><sub>8,10,10,12,4</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>2,4,3,2,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,2,4,5,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.4 | 1.8 | 30.0 |
| Jarrett Allen | 98% | 29.1<br><sub>28,27,27,30,30</sub> | 13.5<br><sub>14,21,10,8,14</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>7,8,9,12,8</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,0,2,2,1</sub> |  | 0.1<br><sub>0,1,0,0,1</sub> |  | 1.2 | 1.3 | 1.2 | 23.7 |
| Peyton Watson | 98% | 28.8<br><sub>30,31,37,28,22</sub> | 13.8<br><sub>8,11,15,22,4</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>1,3,8,6,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,4,1,2,3</sub> |  | 1.2<br><sub>0,2,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.1 | 1.7 | 20.6 |
| Sam Merrill | 98% | 24.8<br><sub>24,21,31,20,27</sub> | 10.2<br><sub>5,7,9,8,16</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>5,2,4,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,3,2,1,3</sub> |  | 1.9<br><sub>1,1,1,2,4</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 0.1 | 0.7 | 14.6 |
| Meleek Thomas | 63% | 17.9<br><sub>-,-,19,20,-</sub> | 7.7<br><sub>-,-,16,10,-</sub> |  | 2.4<br><sub>-,-,2,4,-</sub> |  | 1.2<br><sub>-,-,0,1,-</sub> |  | 0.8<br><sub>-,-,4,0,-</sub> |  | 0.7 | 0.1 | 1.0 | 11.3 |
| Mario Hezonja | 96% | 16.0<br><sub>19,20,15,17,17</sub> | 6.1<br><sub>10,9,3,5,10</sub> | 7.5 · –<br><sub>o 48% · u 52%</sub> | 3.0<br><sub>3,5,3,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>2,1,1,2,2</sub> |  | 0.7<br><sub>0,2,1,1,2</sub> | 1.5<br><sub>o 29% · u 71%</sub> | 0.5 | 0.3 | 0.6 | 10.4 |
| Tyrese Proctor | 71% | 15.8<br><sub>5,11,-,6,20</sub> | 6.6<br><sub>0,5,-,2,7</sub> |  | 2.1<br><sub>0,2,-,1,6</sub> |  | 2.3<br><sub>0,3,-,1,2</sub> |  | 0.8<br><sub>0,1,-,0,1</sub> |  | 0.8 | 0.1 | 0.9 | 11.0 |
| Craig Porter Jr. | 58% | 9.2<br><sub>8,5,-,-,4</sub> | 2.6<br><sub>0,3,-,-,0</sub> |  | 1.7<br><sub>3,1,-,-,1</sub> |  | 1.5<br><sub>0,1,-,-,0</sub> |  | 0.1<br><sub>0,1,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 5.8 |
| Thomas Bryant | 25% | 8.8<br><sub>-,-,-,-,-</sub> | 4.1<br><sub>-,-,-,-,-</sub> |  | 2.4<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.3 | 0.3 | 7.0 |
| Ernest Udeh Jr. | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Riley Minix | 23% | 7.2<br><sub>-,-,-,-,-</sub> | 3.2<br><sub>-,-,-,-,-</sub> |  | 1.0<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.7 |
| Tristan Enaruna | 23% | 6.1<br><sub>-,-,-,-,-</sub> | 2.2<br><sub>-,-,-,-,-</sub> |  | 1.1<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.7 |

</details>

<details><summary>MIL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyler Herro | 98% | 31.5<br><sub>32,32,31,32,27</sub> | 19.1<br><sub>24,34,13,23,23</sub> | 21.5 · 21.5<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>2,5,6,10,3</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 4.7<br><sub>9,4,3,7,0</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 2.4<br><sub>4,5,1,3,4</sub> | 2.5<br><sub>o 52% · u 48%</sub> | 0.9 | 0.2 | 2.3 | 28.3 |
| Ryan Rollins | 98% | 27.9<br><sub>24,34,25,32,17</sub> | 14.6<br><sub>9,11,15,19,4</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,7,4,2,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>3,6,4,4,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 2.0<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.3 | 2.3 | 23.6 |
| Jaime Jaquez Jr. | 98% | 26.4<br><sub>31,35,27,25,27</sub> | 14.5<br><sub>22,19,21,8,19</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>7,11,8,6,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>2,5,4,0,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,2,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.9 | 23.4 |
| Kyle Kuzma | 98% | 25.2<br><sub>27,30,35,29,18</sub> | 11.6<br><sub>5,14,14,17,4</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>6,9,12,7,6</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.8<br><sub>3,4,3,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,2,0,4,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 1.6 | 19.2 |
| Myles Turner | 98% | 23.6<br><sub>32,30,20,28,22</sub> | 9.8<br><sub>11,12,0,6,4</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>5,3,5,9,2</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>3,1,1,4,2</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.6 | 1.5 | 1.2 | 15.8 |
| Kasparas Jakucionis | 88% | 19.3<br><sub>26,23,25,21,19</sub> | 6.6<br><sub>15,7,12,7,4</sub> | 7.5 · 7.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,2,3,4,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 3.4<br><sub>3,5,2,5,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.6<br><sub>1,1,0,1,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 12.4 |
| AJ Green | 98% | 18.6<br><sub>15,17,19,20,24</sub> | 7.0<br><sub>6,11,11,3,9</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,3,4,1</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 1.2<br><sub>2,3,3,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.4 | 0.1 | 0.5 | 10.1 |
| Cormac Ryan | 26% | 17.7 | 8.9 |  | 2.1 |  | 1.3 |  | 1.2 |  | 0.7 | 0.2 | 1.2 | 12.3 |
| Kel'el Ware | 88% | 17.4<br><sub>14,15,29,19,17</sub> | 8.8<br><sub>7,11,19,16,6</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>3,4,13,14,8</sub> | 7.5<br><sub>o 40% · u 60%</sub> | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.6 | 0.4 | 1.1 | 15.3 |
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
| Victor Wembanyama PTS under 24.5 | MIN @ SAS | pointsbetau | 2.00 | 1.95 | 1.95 | 51.2% | 51.3% | 51.3% | +2.6% | +2.5% | 0.6% |
| Devin Vassell PTS under 12.5 | MIN @ SAS | tab | 1.95 | 1.93 | 1.84 | 54.4% | 50.8% | 51.7% | +0.9% | +6.3% | 0.2% |
| Bones Hyland PTS over 8.5 (9+) | MIN @ SAS | pointsbetau | 2.05 | 2.04 | 1.96 | 51.1% | 48.4% | 49.1% | +0.6% | +4.7% | 0.1% |
| LaMelo Ball PTS under 19.5 | MIN @ SAS | draftkings | 1.95 | 1.95 | 1.84 | 54.5% | 50.3% | 51.3% | +0.2% | +6.3% | 0.1% |

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.7<br><sub>30,31,37,35,33</sub> | 16.7<br><sub>15,14,14,19,23</sub> | 16.5 · 16.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,6,6,7,6</sub> | 5.5<br><sub>o 48% · u 52%</sub> | 2.8<br><sub>3,3,4,4,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.1 | 0.9 | 1.8 | 25.1 |
| Jonathan Kuminga | 98% | 32.0<br><sub>27,26,36,32,22</sub> | 14.7<br><sub>11,13,10,20,5</sub> | 13.5 · 13.5<br><sub>o 52% · u 48%</sub> | 5.6<br><sub>8,4,10,3,1</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 2.1<br><sub>5,1,1,5,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>2,3,0,3,1</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.0 | 0.5 | 1.4 | 22.4 |
| Ayo Dosunmu | 98% | 31.8<br><sub>27,23,26,32,30</sub> | 14.8<br><sub>14,9,9,17,15</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>7,3,1,3,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.0<br><sub>10,3,0,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.4 | 1.8 | 23.2 |
| LaMelo Ball | 98% | 30.3<br><sub>23,17,31,28,29</sub> | 19.7<br><sub>12,15,11,8,24</sub> | 19.5 · 19.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>5,1,0,4,4</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 5.8<br><sub>5,8,6,8,7</sub> | 6.5<br><sub>o 43% · u 57%</sub> | 3.3<br><sub>2,4,1,2,6</sub> | 3.5<br><sub>o 47% · u 53%</sub> | 1.3 | 0.2 | 3.0 | 29.7 |
| Terrence Shannon Jr. | 97% | 27.0<br><sub>22,23,24,27,20</sub> | 14.1<br><sub>13,15,14,19,11</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>4,4,4,6,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>1,3,5,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>2,3,3,1,2</sub> | 1.5<br><sub>o 44% · u 56%</sub> | 0.6 | 0.1 | 1.4 | 19.3 |
| Bones Hyland | 96% | 18.8<br><sub>8,15,5,16,20</sub> | 9.4<br><sub>3,3,0,13,19</sub> | 8.5 · 8.5<br><sub>o 49% · u 51%</sub> | 2.1<br><sub>1,3,1,1,0</sub> |  | 2.4<br><sub>0,2,2,3,8</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>1,0,0,3,3</sub> | 1.5<br><sub>o 47% · u 53%</sub> | 0.6 | 0.3 | 1.1 | 14.0 |
| Joan Beringer | 91% | 18.5<br><sub>15,13,17,20,18</sub> | 7.2<br><sub>9,6,12,7,4</sub> | 10.5 · 9.5<br><sub>o 44% · u 56%</sub> | 6.2<br><sub>9,6,7,9,4</sub> | 8.5<br><sub>o 41% · u 59%</sub> | 0.7<br><sub>0,0,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.1 |
| Trey Lyles | 98% | 18.1<br><sub>17,14,13,22,17</sub> | 5.6<br><sub>9,3,3,7,10</sub> |  | 4.0<br><sub>6,6,1,3,5</sub> |  | 0.9<br><sub>2,2,1,1,0</sub> |  | 0.7<br><sub>2,1,1,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 10.6 |
| Jaylen Clark | 80% | 15.6<br><sub>3,5,-,7,17</sub> | 5.0<br><sub>0,3,-,3,5</sub> |  | 2.0<br><sub>2,1,-,2,0</sub> |  | 1.0<br><sub>1,0,-,1,2</sub> |  | 0.6<br><sub>0,0,-,1,1</sub> |  | 0.8 | 0.2 | 0.5 | 8.0 |
| Zyon Pullin | 64% | 11.9<br><sub>-,5,-,-,2</sub> | 4.3<br><sub>-,2,-,-,2</sub> |  | 1.3<br><sub>-,1,-,-,0</sub> |  | 1.5<br><sub>-,0,-,-,0</sub> |  | 0.3<br><sub>-,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.7 | 7.1 |
| Rocco Zikarsky | 16% | 10.9 | 3.4 |  | 3.5 |  | 0.5 |  | 0.0 |  | 0.2 | 0.9 | 0.4 | 7.4 |
| Enrique Freeman | 16% | 9.1 | 2.6 |  | 1.8 |  | 0.4 |  | 0.1 |  | 0.3 | 0.3 | 0.4 | 4.9 |
| Cody Williams | 58% | 8.7<br><sub>3,5,-,-,2</sub> | 0.4<br><sub>0,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>0,0,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 1.3 |
| Isaiah Evans | 63% | 8.5<br><sub>2,4,-,-,2</sub> | 0.4<br><sub>0,0,-,-,0</sub> |  | 1.7<br><sub>0,0,-,-,0</sub> |  | 0.6<br><sub>1,1,-,-,0</sub> |  | 0.0<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 2.8 |

</details>

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Victor Wembanyama | 98% | 34.4<br><sub>34,32,29,27,39</sub> | 25.5<br><sub>12,25,23,29,36</sub> | 24.5 · 24.5<br><sub>o 49% · u 51%</sub> | 11.4<br><sub>13,13,7,10,14</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,2,2,2,5</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.9<br><sub>0,2,2,0,4</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.2 | 3.6 | 2.8 | 40.0 |
| Devin Vassell | 98% | 33.4<br><sub>31,36,32,24,38</sub> | 12.6<br><sub>7,10,11,14,21</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.7<br><sub>3,4,4,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,2,6,8,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,2,1,4,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 1.2 | 0.5 | 1.0 | 20.1 |
| De'Aaron Fox | 98% | 33.0<br><sub>32,34,28,26,39</sub> | 16.4<br><sub>14,19,19,11,14</sub> | 15.5 · 14.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>7,4,3,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>7,9,9,6,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,2,2,2,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.4 | 2.2 | 26.8 |
| Stephon Castle | 98% | 32.5<br><sub>28,33,28,27,38</sub> | 18.0<br><sub>24,15,19,15,14</sub> | 15.5 · 16.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>7,7,4,5,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.3<br><sub>1,5,8,5,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>5,3,3,3,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 3.1 | 29.8 |
| Dylan Harper | 98% | 31.8<br><sub>32,36,28,30,37</sub> | 16.6<br><sub>18,20,22,13,13</sub> | 15.5 · 15.5<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>7,3,5,6,5</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.1<br><sub>5,2,2,6,8</sub> | 4.5<br><sub>o 48% · u 52%</sub> | 1.2<br><sub>0,1,3,0,2</sub> | 0.5<br><sub>o 66% · u 34%</sub> | 1.1 | 0.4 | 1.9 | 26.3 |
| Julian Champagnie | 98% | 28.3<br><sub>30,25,28,25,31</sub> | 9.9<br><sub>8,6,12,26,6</sub> | 10.5 · 10.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>3,0,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>1,0,3,3,0</sub> |  | 1.8<br><sub>2,2,3,8,2</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.6 | 0.8 | 16.1 |
| Keldon Johnson | 98% | 20.8<br><sub>20,19,26,22,23</sub> | 10.0<br><sub>10,8,7,14,9</sub> | 9.5 · 9.5<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>4,6,6,4,6</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.1<br><sub>1,1,3,0,2</sub> |  | 0.7<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 57% · u 43%</sub> | 0.6 | 0.2 | 0.9 | 15.3 |
| Luke Kornet | 98% | 13.9<br><sub>13,16,14,17,14</sub> | 3.3<br><sub>4,7,0,0,1</sub> |  | 4.0<br><sub>1,3,4,4,6</sub> |  | 0.9<br><sub>0,0,1,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.7 | 0.5 | 8.2 |
| Harrison Barnes | 67% | 8.6<br><sub>9,5,4,14,-</sub> | 2.7<br><sub>3,0,0,3,-</sub> |  | 1.1<br><sub>0,0,0,0,-</sub> |  | 0.5<br><sub>0,0,0,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |
| Carter Bryant | 98% | 8.2<br><sub>6,4,10,17,5</sub> | 2.6<br><sub>0,0,4,1,3</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> |  | 0.5<br><sub>1,0,0,2,0</sub> |  | 0.2<br><sub>0,0,0,0,1</sub> |  | 0.2 | 0.2 | 0.4 | 4.6 |
| Maliq Brown | 80% | 6.9<br><sub>1,-,-,-,-</sub> | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 2.4<br><sub>1,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.0 |
| Jordan McLaughlin | 52% | 6.3<br><sub>-,-,3,7,-</sub> | 2.1<br><sub>-,-,0,0,-</sub> |  | 0.9<br><sub>-,-,1,0,-</sub> |  | 1.0<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.0 |
| Tarris Reed Jr. | 58% | 6.0<br><sub>1,-,7,5,-</sub> | 2.4<br><sub>0,-,2,4,-</sub> |  | 2.2<br><sub>0,-,3,5,-</sub> |  | 0.4<br><sub>0,-,0,0,-</sub> |  | 0.0<br><sub>0,-,0,0,-</sub> |  | 0.1 | 0.3 | 0.7 | 5.0 |
| Ja'Kobi Gillespie | 88% | 5.9<br><sub>1,-,3,-,-</sub> | 4.2<br><sub>2,-,3,-,-</sub> |  | 0.2<br><sub>0,-,0,-,-</sub> |  | 0.6<br><sub>0,-,0,-,-</sub> |  | 0.5<br><sub>0,-,1,-,-</sub> |  | 0.1 | 0.1 | 0.4 | 5.0 |
| David Jones Garcia | 52% | 5.7<br><sub>1,-,-,-,-</sub> | 2.5<br><sub>2,-,-,-,-</sub> |  | 1.1<br><sub>0,-,-,-,-</sub> |  | 1.0<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |

</details>


### OKC @ HOU
Out: Steven Adams (HOU), Reed Sheppard (HOU), Fred VanVleet (HOU), Alex Caruso (OKC), Chet Holmgren (OKC), Cason Wallace (OKC), Jalen Williams (OKC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jared McCain PTS over 14.5 (15+) | OKC @ HOU | pointsbetau | 2.00 | 1.95 | 1.90 | 52.6% | 50.7% | 51.2% | +2.4% | +5.2% | 0.6% |
| Kenrich Williams REB over 4.5 (5+) | OKC @ HOU | draftkings | 2.06 | 2.04 | 1.67 | 59.8% | 45.6% | 49.1% | +1.2% | +23.1% | 0.3% |
| Kevin Durant PTS under 22.5 | OKC @ HOU | pointsbetau | 2.00 | 1.98 | 1.85 | 53.9% | 49.3% | 50.4% | +0.9% | +7.9% | 0.2% |
| Alperen Sengun PTS under 18.5 | OKC @ HOU | pointsbetau | 2.05 | 2.03 | 1.97 | 50.7% | 48.7% | 49.2% | +0.9% | +3.9% | 0.2% |
| Jaylin Williams REB under 5.5 | OKC @ HOU | draftkings | 2.05 | 2.03 | 1.67 | 59.9% | 45.6% | 49.2% | +0.8% | +22.8% | 0.2% |
| Aday Mara PTS under 7.5 | OKC @ HOU | pointsbetau | 2.00 | 1.99 | 1.88 | 53.2% | 49.2% | 50.2% | +0.4% | +6.4% | 0.1% |
| Shai Gilgeous-Alexander STL over 1.5 (2+) | OKC @ HOU | draftkings | 2.72 | 2.72 | 2.27 | 44.0% | 34.4% | 36.8% | +0.2% | +19.8% | 0.0% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 100% | 34.8<br><sub>36,35,36,30,28</sub> | 29.9<br><sub>32,17,34,26,21</sub> | 29.5 · 28.5<br><sub>o 50% · u 50%</sub> | 3.9<br><sub>6,2,6,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 6.6<br><sub>4,3,5,3,2</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.5 | 0.9 | 3.3 | 40.4 |
| Jared McCain | 100% | 31.0<br><sub>22,18,21,30,29</sub> | 15.8<br><sub>20,4,3,18,10</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 3.0<br><sub>2,0,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,1,0,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>6,0,1,4,0</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 0.8 | 0.2 | 1.9 | 21.2 |
| Ajay Mitchell | 100% | 30.2<br><sub>23,23,28,25,28</sub> | 18.9<br><sub>4,12,18,30,29</sub> | 18.5 · 18.5<br><sub>o 49% · u 51%</sub> | 3.6<br><sub>5,0,6,2,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.5<br><sub>6,0,4,5,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 43% · u 57%</sub> | 1.5 | 0.3 | 2.1 | 27.0 |
| Josh Dix | 67% | 26.9<br><sub>-,-,-,22,24</sub> | 4.3<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.7<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.2 |
| Isaiah Hartenstein | 100% | 26.6<br><sub>17,23,27,26,26</sub> | 9.9<br><sub>4,6,12,15,10</sub> | 9.5 · 9.5<br><sub>o 49% · u 51%</sub> | 9.5<br><sub>3,6,12,13,14</sub> | 9.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,2,1,3,3</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.8 | 1.7 | 22.5 |
| Bennett Stirtz | 96% | 26.4<br><sub>1,2,11,25,28</sub> | 7.7<br><sub>0,0,2,7,8</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 0.9<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 10.8 |
| Kenrich Williams | 100% | 26.3<br><sub>7,6,7,24,17</sub> | 9.6<br><sub>3,3,3,3,7</sub> | 6.5 · 6.5<br><sub>o 56% · u 44%</sub> | 5.4<br><sub>2,1,1,7,3</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.7<br><sub>0,1,0,0,0</sub> |  | 1.4<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 0.9 | 0.2 | 1.1 | 16.8 |
| Aday Mara | 96% | 23.3<br><sub>12,13,14,20,21</sub> | 7.8<br><sub>7,2,2,11,6</sub> | 7.5 · 7.5<br><sub>o 50% · u 50%</sub> | 5.9<br><sub>2,3,3,10,3</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 1.2<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.3 | 1.3 | 15.0 |
| Jaylin Williams | 98% | 20.7<br><sub>17,15,5,26,20</sub> | 5.9<br><sub>5,3,0,6,0</sub> | 7.5 · 7.5<br><sub>o 49% · u 51%</sub> | 5.1<br><sub>4,7,0,6,5</sub> | 5.5<br><sub>o 51% · u 49%</sub> | 1.9<br><sub>1,3,0,3,1</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 0.9<br><sub>1,1,0,2,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.5 | 0.5 | 0.8 | 12.9 |
| Micah Peavy | 48% | 13.0<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer | 80% | 12.4<br><sub>1,2,-,3,14</sub> | 3.2<br><sub>0,0,-,0,3</sub> |  | 2.4<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.3 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 100% | 37.0<br><sub>36,39,28,33,39</sub> | 17.8<br><sub>20,17,15,23,15</sub> | 15.5 · 16.5<br><sub>o 53% · u 47%</sub> | 7.3<br><sub>10,11,5,4,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.2<br><sub>4,6,2,3,6</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.5 | 0.6 | 2.5 | 30.4 |
| Kevin Durant | 100% | 36.2<br><sub>37,37,30,31,37</sub> | 22.8<br><sub>20,22,22,18,28</sub> | 22.5 · 23.5<br><sub>o 50% · u 50%</sub> | 6.1<br><sub>7,4,9,5,5</sub> | 4.5<br><sub>o 59% · u 41%</sub> | 4.9<br><sub>6,2,3,4,1</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,3,1,2,1</sub> | 1.5<br><sub>o 60% · u 40%</sub> | 0.8 | 1.0 | 3.6 | 33.9 |
| Jabari Smith Jr. | 100% | 36.0<br><sub>34,33,39,30,35</sub> | 15.8<br><sub>7,14,16,14,22</sub> | 14.5 · 15.5<br><sub>o 51% · u 49%</sub> | 7.1<br><sub>5,5,12,2,3</sub> | 5.5<br><sub>o 59% · u 41%</sub> | 2.1<br><sub>1,3,5,2,2</sub> |  | 2.5<br><sub>1,2,2,3,3</sub> | 2.5<br><sub>o 43% · u 57%</sub> | 0.8 | 0.8 | 1.6 | 25.0 |
| Alperen Sengun | 100% | 34.9<br><sub>36,33,37,-,-</sub> | 19.4<br><sub>29,17,29,-,-</sub> | 18.5 · 18.5<br><sub>o 51% · u 49%</sub> | 9.9<br><sub>7,10,9,-,-</sub> | 8.5<br><sub>o 55% · u 45%</sub> | 6.3<br><sub>7,7,9,-,-</sub> | 5.5<br><sub>o 55% · u 45%</sub> | 0.7<br><sub>2,1,1,-,-</sub> |  | 1.2 | 0.9 | 3.4 | 35.5 |
| Tari Eason | 98% | 28.3<br><sub>27,31,33,31,26</sub> | 11.4<br><sub>12,19,13,5,11</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 6.9<br><sub>6,3,8,9,13</sub> | 5.5<br><sub>o 52% · u 48%</sub> | 1.4<br><sub>0,0,2,1,2</sub> |  | 1.2<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 35% · u 65%</sub> | 1.3 | 0.7 | 1.4 | 19.8 |
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
