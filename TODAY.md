# NBA model · Sat 31 Oct 2026 (US date)

Updated **Sun 01 Nov, 10:27 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-31/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. REB over 7.5 (8+) | OKC @ HOU | draftkings | 3.14 | 2.99 | 2.24 | 44.6% | 29.8% | 33.5% | +5.1% | +40.1% | 0.6% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 7.5 (8+) | OKC @ HOU | draftkings | 19.80 | 12.97 | 5.99 | 16.7% | 4.7% | 7.7% | +52.8% | +230.6% | 0.7% |
| Tari Eason REB over 11.5 (12+) | OKC @ HOU | draftkings | 21.00 | 16.39 | 9.06 | 11.0% | 4.5% | 6.1% | +28.0% | +131.7% | 0.4% |
| Tari Eason REB over 9.5 (10+) | OKC @ HOU | draftkings | 9.30 | 7.35 | 4.12 | 24.3% | 10.1% | 13.6% | +26.6% | +125.9% | 0.8% |
| Shai Gilgeous-Alexander PTS over 49.5 (50+) | OKC @ HOU | draftkings | 29.00 | 23.98 | 14.23 | 7.0% | 3.2% | 4.2% | +21.1% | +103.8% | 0.2% |
| Kevin Durant REB over 9.5 (10+) | OKC @ HOU | draftkings | 14.40 | 11.90 | 7.08 | 14.1% | 6.5% | 8.4% | +20.9% | +103.4% | 0.4% |
| Amen Thompson PTS over 29.5 (30+) | OKC @ HOU | draftkings | 22.00 | 18.35 | 11.04 | 9.1% | 4.2% | 5.5% | +19.9% | +99.4% | 0.2% |
| Amen Thompson PRA over 44.5 (45+) | OKC @ HOU | draftkings | 20.00 | 16.92 | 10.38 | 9.6% | 4.7% | 5.9% | +18.3% | +92.8% | 0.2% |
| Amen Thompson AST over 9.5 (10+) | OKC @ HOU | draftkings | 22.00 | 18.69 | 11.53 | 8.7% | 4.2% | 5.3% | +17.8% | +90.8% | 0.2% |
| Amen Thompson PRA over 39.5 (40+) | OKC @ HOU | draftkings | 9.50 | 8.14 | 5.10 | 19.6% | 9.8% | 12.3% | +16.7% | +86.4% | 0.5% |
| Amen Thompson AST over 7.5 (8+) | OKC @ HOU | draftkings | 7.90 | 6.78 | 4.26 | 23.5% | 11.8% | 14.7% | +16.4% | +85.4% | 0.6% |
| Amen Thompson PTS over 24.5 (25+) | OKC @ HOU | draftkings | 8.40 | 7.36 | 4.78 | 20.9% | 11.1% | 13.6% | +14.0% | +75.8% | 0.5% |
| Jabari Smith Jr. PRA over 34.5 (35+) | OKC @ HOU | draftkings | 9.70 | 8.52 | 5.54 | 18.1% | 9.6% | 11.7% | +13.9% | +75.1% | 0.4% |
| Shai Gilgeous-Alexander PTS over 44.5 (45+) | OKC @ HOU | draftkings | 14.00 | 12.47 | 8.28 | 12.1% | 6.7% | 8.0% | +12.3% | +69.0% | 0.2% |
| Shai Gilgeous-Alexander PRA over 59.5 (60+) | OKC @ HOU | draftkings | 18.20 | 16.26 | 10.88 | 9.2% | 5.1% | 6.2% | +11.9% | +67.2% | 0.2% |
| Jabari Smith Jr. REB over 11.5 (12+) | OKC @ HOU | draftkings | 17.40 | 15.62 | 10.55 | 9.5% | 5.4% | 6.4% | +11.3% | +64.9% | 0.2% |
| MIN to win | MIN @ SAS | ladbrokes_au | 6.25 | 5.61 | 4.32 | 23.1% | 17.8% | 17.8% | +11.3% | +44.6% | 0.5% |
| Donovan Mitchell PTS over 44.5 (45+) | CLE @ MIL | draftkings | 26.00 | 23.47 | 16.01 | 6.2% | 3.6% | 4.3% | +10.7% | +62.4% | 0.1% |
| Shai Gilgeous-Alexander AST over 9.5 (10+) | OKC @ HOU | draftkings | 9.30 | 8.40 | 5.73 | 17.4% | 10.1% | 11.9% | +10.7% | +62.3% | 0.3% |
| Jabari Smith Jr. PRA over 39.5 (40+) | OKC @ HOU | draftkings | 20.20 | 18.28 | 12.48 | 8.0% | 4.6% | 5.5% | +10.6% | +61.9% | 0.1% |
| Jabari Smith Jr. REB over 9.5 (10+) | OKC @ HOU | draftkings | 7.10 | 6.43 | 4.40 | 22.7% | 13.2% | 15.6% | +10.4% | +61.2% | 0.4% |
| Darius Acuff Jr. REB over 7.5 (8+) | SAC @ MEM | draftkings | 16.40 | 14.86 | 10.19 | 9.8% | 5.7% | 6.7% | +10.3% | +61.0% | 0.2% |
| Darius Acuff Jr. REB over 5.5 (6+) | SAC @ MEM | draftkings | 5.36 | 4.89 | 3.38 | 29.6% | 17.4% | 20.5% | +9.7% | +58.5% | 0.6% |
| Precious Achiuwa PA over 24.5 (25+) | SAC @ MEM | draftkings | 9.70 | 8.84 | 6.12 | 16.3% | 9.6% | 11.3% | +9.7% | +58.5% | 0.3% |
| Jabari Smith Jr. PRA over 29.5 (30+) | OKC @ HOU | draftkings | 4.39 | 4.05 | 2.86 | 34.9% | 21.3% | 24.7% | +8.4% | +53.4% | 0.6% |
| Donovan Mitchell PTS over 39.5 (40+) | CLE @ MIL | draftkings | 13.00 | 11.99 | 8.48 | 11.8% | 7.2% | 8.3% | +8.4% | +53.3% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 10.5 (11+) | OKC @ HOU | draftkings | 14.60 | 11.12 | 5.96 | 16.8% | 6.4% | 9.0% | +31.3% | +144.8% | 0.6% |
| Tari Eason REB over 12.5 (13+) | OKC @ HOU | draftkings | 30.00 | 24.21 | 13.91 | 7.2% | 3.1% | 4.1% | +24.0% | +115.7% | 0.2% |
| Kevin Durant REB over 8.5 (9+) | OKC @ HOU | draftkings | 8.80 | 7.39 | 4.49 | 22.3% | 10.6% | 13.5% | +19.1% | +96.1% | 0.6% |
| Amen Thompson AST over 8.5 (9+) | OKC @ HOU | draftkings | 13.40 | 11.31 | 6.93 | 14.4% | 7.0% | 8.8% | +18.4% | +93.3% | 0.4% |
| Kevin Durant REB over 10.5 (11+) | OKC @ HOU | draftkings | 22.00 | 18.90 | 11.91 | 8.4% | 4.2% | 5.3% | +16.3% | +84.7% | 0.2% |
| Jabari Smith Jr. REB over 10.5 (11+) | OKC @ HOU | draftkings | 11.20 | 9.99 | 6.66 | 15.0% | 8.3% | 10.0% | +12.1% | +68.1% | 0.3% |
| Darius Acuff Jr. REB over 6.5 (7+) | SAC @ MEM | draftkings | 9.40 | 8.42 | 5.66 | 17.7% | 9.9% | 11.9% | +11.6% | +66.2% | 0.4% |
| Shai Gilgeous-Alexander AST over 10.5 (11+) | OKC @ HOU | draftkings | 15.20 | 13.64 | 9.19 | 10.9% | 6.2% | 7.3% | +11.5% | +65.5% | 0.2% |
| Jabari Smith Jr. REB over 8.5 (9+) | OKC @ HOU | draftkings | 4.66 | 4.31 | 3.07 | 32.6% | 20.1% | 23.2% | +8.1% | +51.9% | 0.5% |
| Jabari Smith Jr. REB over 12.5 (13+) | OKC @ HOU | draftkings | 25.00 | 23.47 | 17.17 | 5.8% | 3.7% | 4.3% | +6.5% | +45.6% | 0.1% |
| Shai Gilgeous-Alexander AST over 8.5 (9+) | OKC @ HOU | draftkings | 5.62 | 5.28 | 3.87 | 25.9% | 16.6% | 18.9% | +6.4% | +45.4% | 0.4% |
| Precious Achiuwa REB over 12.5 (13+) | SAC @ MEM | draftkings | 9.30 | 8.80 | 6.52 | 15.3% | 10.1% | 11.4% | +5.7% | +42.6% | 0.2% |
| Julian Champagnie PTS under 10.5 | MIN @ SAS | tab | 2.00 | 1.89 | 1.66 | 60.2% | 50.4% | 52.8% | +5.7% | +20.4% | 1.4% |
| Aday Mara REB over 8.5 (9+) | OKC @ HOU | draftkings | 6.75 | 6.40 | 4.78 | 20.9% | 13.9% | 15.6% | +5.4% | +41.3% | 0.2% |
| De'Andre Hunter REB over 8.5 (9+) | SAC @ MEM | draftkings | 10.30 | 9.79 | 7.33 | 13.6% | 9.1% | 10.2% | +5.2% | +40.5% | 0.1% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Zach Edey PTS over 8.5 (9+) | SAC @ MEM | pointsbetau | 2.05 | Ty Jerome | 61.9% | 52.6% | +7.3% |
| Cameron Boozer PTS under 17.5 | SAC @ MEM | sportsbet | 1.96 | Ty Jerome | 48.9% | 62.9% | +5.2% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tari Eason REB over 7.5 (8+) | OKC @ HOU | draftkings | 3.96 | 3.45 | 2.22 | 45.0% | 23.6% | 28.9% | +14.6% | +78.2% | 1.2% |
| Kevin Durant AST over 3.5 (4+) | OKC @ HOU | draftkings | 2.12 | 1.94 | 1.37 | 72.9% | 44.3% | 51.4% | +9.0% | +54.4% | 2.0% |
| AJ Green 3PM under 1.5 | CLE @ MIL | draftkings | 2.33 | 2.14 | 1.51 | 66.2% | 40.1% | 46.6% | +8.7% | +54.3% | 1.6% |
| Kevin Durant RA over 8.5 (9+) | OKC @ HOU | draftkings | 1.96 | 1.81 | 1.29 | 77.6% | 47.7% | 55.1% | +8.2% | +52.2% | 2.0% |
| Joan Beringer PR under 18.5 | MIN @ SAS | draftkings | 1.85 | 1.72 | 1.25 | 80.1% | 50.6% | 58.0% | +7.1% | +48.1% | 2.0% |
| Amen Thompson AST over 5.5 (6+) | OKC @ HOU | draftkings | 2.91 | 2.74 | 2.02 | 49.6% | 32.1% | 36.5% | +6.2% | +44.4% | 0.8% |
| Tari Eason REB over 5.5 (6+) | OKC @ HOU | draftkings | 1.99 | 1.89 | 1.42 | 70.5% | 47.2% | 53.0% | +5.5% | +40.4% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| SAC @ MEM | Sun 01 Nov 11:00 | 115.8–122.4 | SAC 32% | 3.12 / 1.47 | MEM -6.5 | 238.5 | MEM -8.5 covers 45%; o229.5 68% |
| CLE @ MIL | Sun 01 Nov 11:00 | 118.8–114.7 | CLE 61% | 1.63 / 2.60 | MIL +4.5 | 233.5 | MIL +9.5 covers 65%; o235.5 45% |
| MIN @ SAS | Sun 01 Nov 11:00 | 107.9–118.3 | MIN 23% | 4.32 / 1.30 | SAS -10.5 | 226.5 | SAS -12.5 covers 44%; o229.5 43% |
| OKC @ HOU | Sun 01 Nov 11:30 | 112.1–113.1 | OKC 47% | 2.12 / 1.90 | HOU -1.5 | 225.5 | HOU -2.5 covers 47%; o219.5 61% |

### SAC @ MEM
Out: Dylan Cardwell (SAC), Keegan Murray (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zach LaVine PTS under 21.5 | SAC @ MEM | betright | 1.98 | 1.94 | 1.79 | 55.7% | 50.0% | 51.4% | +1.9% | +10.4% | 0.5% |
| Precious Achiuwa RA over 9.5 (10+) | SAC @ MEM | draftkings | 2.01 | 1.99 | 1.64 | 61.1% | 46.6% | 50.2% | +0.9% | +22.8% | 0.2% |
| Darius Acuff Jr. RA over 9.5 (10+) | SAC @ MEM | draftkings | 1.95 | 1.94 | 1.61 | 62.3% | 48.0% | 51.5% | +0.7% | +21.6% | 0.2% |
| Precious Achiuwa REB over 7.5 (8+) | SAC @ MEM | draftkings | 1.92 | 1.91 | 1.59 | 63.0% | 48.9% | 52.4% | +0.6% | +20.7% | 0.2% |
| Domantas Sabonis PTS over 15.5 (16+) | SAC @ MEM | unibet | 1.88 | 1.88 | 1.66 | 60.4% | 50.7% | 53.1% | +0.2% | +13.9% | 0.1% |
| De'Andre Hunter REB over 4.5 (5+) | SAC @ MEM | draftkings | 1.93 | 1.93 | 1.62 | 61.9% | 48.4% | 51.8% | +0.2% | +19.7% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.8–122.4 | SAC 32% | 3.12 / 1.47 | MEM -6.5 | 238.5 | MEM -8.5 covers 45%; o229.5 68% |
| Expected (weighted by chance each plays) | 115.0–122.9 | SAC 29% | 3.42 / 1.41 | MEM -7.5 | 237.5 | MEM -8.5 covers 48%; o229.5 68% |
| if Ty Jerome plays | 115.3–123.3 | SAC 29% | 3.50 / 1.40 | MEM -8.5 | 238.5 | MEM -8.5 covers 49%; o229.5 69% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quinten Post (MEM) | Doubtful | 20% | 14.1 | 5.7 | 3.0 | 0.8 | 0.5 | 0.5 | 0.4 | 0.7 | 9.4 | small |
| Ty Jerome (MEM) | Questionable | 55% | 29.0 | 22.6 | 3.5 | 6.4 | 2.6 | 1.4 | 0.3 | 2.5 | 32.5 | full tables below |
| Scotty Pippen Jr. (MEM) | Questionable | 55% | 18.6 | 9.8 | 2.6 | 3.5 | 0.8 | 1.2 | 0.4 | 1.8 | 15.9 | small |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.0<br><sub>12,33,22,19,34</sub> | 23.5 · 23.5<br><sub>o 48% · u 52%</sub> | 4.4<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.5 | 33.9 |
| Zach LaVine | 98% | 34.1<br><sub>34,39,40,31,39</sub> | 21.3<br><sub>28,22,37,22,21</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.6 | 28.1 |
| Domantas Sabonis | 98% | 34.0<br><sub>34,39,35,37,40</sub> | 18.4<br><sub>14,27,15,20,9</sub> | 15.5 · 15.5<br><sub>o 51% · u 49%</sub> | 14.0<br><sub>18,19,15,14,15</sub> | 14.5<br><sub>o 46% · u 54%</sub> | 6.0<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 19% · u 81%</sub> | 0.9 | 0.4 | 3.1 | 38.4 |
| Precious Achiuwa | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.8<br><sub>15,14,12,4,24</sub> | 12.5 · 12.5<br><sub>o 53% · u 47%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 1.5 | 1.1 | 1.7 | 26.7 |
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
| Cameron Boozer | 96% | 33.5<br><sub>33,37,31,31,28</sub> | 18.7<br><sub>7,25,14,13,18</sub> | – · 17.5<br><sub>o 49% · u 51%</sub> | 10.7<br><sub>11,13,11,7,12</sub> |  | 6.7<br><sub>5,6,4,4,12</sub> |  | 2.1<br><sub>0,4,2,1,4</sub> |  | 1.5 | 0.7 | 2.4 | 36.0 |
| Cedric Coward | 98% | 30.4<br><sub>28,-,32,31,27</sub> | 17.9<br><sub>7,-,17,16,17</sub> | – · 16.5<br><sub>o 51% · u 49%</sub> | 7.5<br><sub>7,-,11,11,7</sub> |  | 3.8<br><sub>2,-,1,3,4</sub> |  | 2.0<br><sub>1,-,3,4,3</sub> |  | 1.0 | 0.5 | 2.0 | 29.2 |
| Jaylen Wells | 98% | 30.3<br><sub>28,25,33,30,25</sub> | 16.8<br><sub>12,17,16,14,10</sub> | – · 13.5<br><sub>o 49% · u 51%</sub> | 3.7<br><sub>5,4,5,3,1</sub> |  | 2.1<br><sub>0,3,3,0,0</sub> |  | 2.3<br><sub>1,4,2,2,2</sub> |  | 1.1 | 0.2 | 1.3 | 22.6 |
| Jerami Grant | 98% | 27.3<br><sub>24,26,22,24,27</sub> | 15.3<br><sub>15,6,5,13,2</sub> |  | 3.0<br><sub>2,0,5,3,1</sub> |  | 2.4<br><sub>3,3,3,0,3</sub> |  | 1.8<br><sub>2,1,1,3,0</sub> |  | 0.8 | 0.8 | 1.7 | 20.7 |
| Zach Edey | 98% | 24.3<br><sub>21,22,-,21,19</sub> | 10.7<br><sub>6,8,-,4,13</sub> | – · 8.5<br><sub>o 50% · u 50%</sub> | 9.6<br><sub>9,10,-,3,7</sub> |  | 1.5<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.7 | 1.7 | 1.7 | 21.9 |
| Cam Spencer | 96% | 22.9<br><sub>16,17,16,18,23</sub> | 11.0<br><sub>3,11,13,8,8</sub> | – · 11.5<br><sub>o 47% · u 53%</sub> | 3.0<br><sub>3,2,2,5,6</sub> |  | 5.9<br><sub>2,1,1,5,8</sub> |  | 1.6<br><sub>1,3,3,2,1</sub> |  | 0.8 | 0.2 | 1.2 | 19.9 |
| GG Jackson | 96% | 19.6<br><sub>19,15,10,16,21</sub> | 11.9<br><sub>12,2,1,4,12</sub> |  | 4.2<br><sub>8,4,3,1,7</sub> |  | 1.5<br><sub>0,1,0,2,2</sub> |  | 1.1<br><sub>2,0,0,0,2</sub> |  | 0.5 | 0.7 | 1.6 | 17.6 |
| Jahmai Mashack | 38% | 18.8<br><sub>-,-,-,-,-</sub> | 6.1<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 2.5<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 1.0 | 0.4 | 1.5 | 11.0 |
| Javon Small | 26% | 18.8 | 9.7 |  | 3.0 |  | 3.3 |  | 1.1 |  | 0.9 | 0.2 | 1.5 | 16.1 |
| Isaiah Stewart | 98% | 17.7<br><sub>-,16,22,15,16</sub> | 7.8<br><sub>-,4,13,4,18</sub> | – · 6.5<br><sub>o 50% · u 50%</sub> | 4.2<br><sub>-,2,5,4,3</sub> |  | 0.9<br><sub>-,0,2,0,0</sub> |  | 0.6<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.1 | 0.9 | 12.9 |
| Taylor Hendricks | 58% | 11.4<br><sub>-,-,7,-,3</sub> | 4.6<br><sub>-,-,0,-,0</sub> |  | 2.3<br><sub>-,-,1,-,1</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.7 | 0.4 | 0.6 | 7.6 |
| Olivier-Maxence Prosper | 48% | 11.4<br><sub>-,-,-,-,3</sub> | 6.6<br><sub>-,-,-,-,4</sub> |  | 2.4<br><sub>-,-,-,-,1</sub> |  | 0.8<br><sub>-,-,-,-,0</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.2 | 0.6 | 9.7 |
| Kris Murray | 58% | 10.2<br><sub>-,13,-,-,3</sub> | 2.6<br><sub>-,0,-,-,0</sub> |  | 1.6<br><sub>-,3,-,-,1</sub> |  | 0.7<br><sub>-,1,-,-,0</sub> |  | 0.2<br><sub>-,0,-,-,0</sub> |  | 0.5 | 0.2 | 0.5 | 5.0 |
| Carson Cooper | 35% | 8.6<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Karim Lopez | 48% | 6.9<br><sub>-,-,-,-,3</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.4<br><sub>-,-,-,-,1</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.2 | 2.2 |

</details>

<details><summary>if Ty Jerome plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cameron Boozer (MEM) | 96% | 32.2<br><sub>33,37,31,31,28</sub> | 16.1<br><sub>7,25,14,13,18</sub> | – · 17.5<br><sub>o 49% · u 51%</sub> | 10.1<br><sub>11,13,11,7,12</sub> |  | 6.1<br><sub>5,6,4,4,12</sub> |  | 1.8<br><sub>0,4,2,1,4</sub> |  | 1.4 | 0.7 | 2.0 | 32.3 |
| Ty Jerome (MEM) | 100% | 29.0<br><sub>32,32,32,30,24</sub> | 22.6<br><sub>45,28,31,15,10</sub> |  | 3.5<br><sub>7,2,4,1,2</sub> |  | 6.4<br><sub>6,5,7,8,3</sub> |  | 2.6<br><sub>5,3,1,1,1</sub> |  | 1.4 | 0.3 | 2.5 | 32.5 |
| Jaylen Wells (MEM) | 98% | 28.1<br><sub>28,25,33,30,25</sub> | 14.2<br><sub>12,17,16,14,10</sub> | – · 13.5<br><sub>o 49% · u 51%</sub> | 3.3<br><sub>5,4,5,3,1</sub> |  | 1.8<br><sub>0,3,3,0,0</sub> |  | 1.9<br><sub>1,4,2,2,2</sub> |  | 1.0 | 0.1 | 1.0 | 19.3 |
| Cedric Coward (MEM) | 98% | 27.9<br><sub>28,-,32,31,27</sub> | 15.5<br><sub>7,-,17,16,17</sub> | – · 16.5<br><sub>o 51% · u 49%</sub> | 6.8<br><sub>7,-,11,11,7</sub> |  | 3.0<br><sub>2,-,1,3,4</sub> |  | 1.7<br><sub>1,-,3,4,3</sub> |  | 0.9 | 0.5 | 1.6 | 25.3 |
| Jerami Grant (MEM) | 98% | 24.9<br><sub>24,26,22,24,27</sub> | 12.0<br><sub>15,6,5,13,2</sub> |  | 2.7<br><sub>2,0,5,3,1</sub> |  | 1.9<br><sub>3,3,3,0,3</sub> |  | 1.4<br><sub>2,1,1,3,0</sub> |  | 0.7 | 0.8 | 1.4 | 16.6 |
| Zach Edey (MEM) | 98% | 22.3<br><sub>21,22,-,21,19</sub> | 9.6<br><sub>6,8,-,4,13</sub> | – · 8.5<br><sub>o 50% · u 50%</sub> | 8.6<br><sub>9,10,-,3,7</sub> |  | 1.4<br><sub>0,3,-,2,0</sub> |  | 0.2<br><sub>0,0,-,0,1</sub> |  | 0.6 | 1.6 | 1.4 | 19.5 |
| Cam Spencer (MEM) | 96% | 20.4<br><sub>16,17,16,18,23</sub> | 9.1<br><sub>3,11,13,8,8</sub> | – · 11.5<br><sub>o 47% · u 53%</sub> | 2.6<br><sub>3,2,2,5,6</sub> |  | 4.9<br><sub>2,1,1,5,8</sub> |  | 1.3<br><sub>1,3,3,2,1</sub> |  | 0.7 | 0.2 | 1.0 | 16.6 |
| GG Jackson (MEM) | 96% | 16.9<br><sub>19,15,10,16,21</sub> | 9.4<br><sub>12,2,1,4,12</sub> |  | 3.5<br><sub>8,4,3,1,7</sub> |  | 1.2<br><sub>0,1,0,2,2</sub> |  | 0.8<br><sub>2,0,0,0,2</sub> |  | 0.4 | 0.6 | 1.2 | 14.2 |
| Isaiah Stewart (MEM) | 98% | 15.2<br><sub>-,16,22,15,16</sub> | 6.4<br><sub>-,4,13,4,18</sub> | – · 6.5<br><sub>o 50% · u 50%</sub> | 3.6<br><sub>-,2,5,4,3</sub> |  | 0.7<br><sub>-,0,2,0,0</sub> |  | 0.4<br><sub>-,0,2,0,2</sub> |  | 0.3 | 1.0 | 0.8 | 10.7 |
| Javon Small (MEM) | 26% | 13.1 | 5.9 |  | 2.0 |  | 2.1 |  | 0.7 |  | 0.6 | 0.2 | 1.0 | 10.1 |
| Jahmai Mashack (MEM) | 38% | 12.0<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.7 | 0.3 | 0.9 | 6.8 |
| Olivier-Maxence Prosper (MEM) | 48% | 9.1<br><sub>-,-,-,-,3</sub> | 5.2<br><sub>-,-,-,-,4</sub> |  | 1.9<br><sub>-,-,-,-,1</sub> |  | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.2 | 0.4 | 7.7 |
| Carson Cooper (MEM) | 35% | 8.7<br><sub>-,-,-,-,-</sub> | 3.8<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Taylor Hendricks (MEM) | 58% | 8.5<br><sub>-,-,7,-,3</sub> | 3.3<br><sub>-,-,0,-,0</sub> |  | 1.8<br><sub>-,-,1,-,1</sub> |  | 0.5<br><sub>-,-,0,-,0</sub> |  | 0.3<br><sub>-,-,0,-,0</sub> |  | 0.5 | 0.3 | 0.4 | 5.5 |
| Kris Murray (MEM) | 58% | 8.1<br><sub>-,13,-,-,3</sub> | 2.0<br><sub>-,0,-,-,0</sub> |  | 1.4<br><sub>-,3,-,-,1</sub> |  | 0.5<br><sub>-,1,-,-,0</sub> |  | 0.1<br><sub>-,0,-,-,0</sub> |  | 0.4 | 0.2 | 0.3 | 3.9 |
| Karim Lopez (MEM) | 48% | 5.8<br><sub>-,-,-,-,3</sub> | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,1</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 2.0 |
| Darius Acuff Jr. (SAC) | 96% | 36.3<br><sub>35,37,36,33,41</sub> | 23.1<br><sub>12,33,22,19,34</sub> | 23.5 · 23.5<br><sub>o 48% · u 52%</sub> | 4.5<br><sub>3,2,3,3,6</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 6.5<br><sub>3,4,7,5,14</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.7<br><sub>0,2,2,3,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.4 | 3.5 | 34.1 |
| Domantas Sabonis (SAC) | 98% | 34.1<br><sub>34,39,35,37,40</sub> | 18.4<br><sub>14,27,15,20,9</sub> | 15.5 · 15.5<br><sub>o 51% · u 49%</sub> | 14.1<br><sub>18,19,15,14,15</sub> | 14.5<br><sub>o 46% · u 54%</sub> | 6.1<br><sub>8,10,3,8,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 0.3<br><sub>0,1,0,0,0</sub> | 0.5<br><sub>o 19% · u 81%</sub> | 0.9 | 0.4 | 3.1 | 38.5 |
| Zach LaVine (SAC) | 98% | 34.0<br><sub>34,39,40,31,39</sub> | 21.4<br><sub>28,22,37,22,21</sub> | 21.5 · 21.5<br><sub>o 49% · u 51%</sub> | 3.8<br><sub>4,5,2,3,3</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 3.0<br><sub>4,1,5,3,5</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 2.6<br><sub>3,3,3,3,3</sub> | 2.5<br><sub>o 51% · u 49%</sub> | 0.9 | 0.3 | 2.5 | 28.2 |
| Precious Achiuwa (SAC) | 98% | 33.2<br><sub>29,26,39,14,41</sub> | 15.8<br><sub>15,14,12,4,24</sub> | 12.5 · 12.5<br><sub>o 53% · u 47%</sub> | 8.9<br><sub>5,6,10,1,9</sub> | 7.5<br><sub>o 52% · u 48%</sub> | 1.9<br><sub>2,1,0,0,2</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 0.3<br><sub>1,0,0,0,0</sub> | 0.5<br><sub>o 31% · u 69%</sub> | 1.4 | 1.1 | 1.7 | 26.6 |
| De'Andre Hunter (SAC) | 98% | 29.6<br><sub>20,25,29,33,37</sub> | 13.1<br><sub>6,4,7,24,24</sub> | 12.5 · 12.5<br><sub>o 50% · u 50%</sub> | 5.6<br><sub>3,7,6,6,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>1,1,1,2,1</sub> | 1.5<br><sub>o 50% · u 50%</sub> | 1.6<br><sub>2,0,2,5,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 0.8 | 0.2 | 1.8 | 20.4 |
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
| Kel'el Ware PTS under 9.5 | CLE @ MIL | pointsbetau | 2.00 | 1.91 | 1.64 | 61.2% | 49.6% | 52.5% | +5.0% | +22.3% | 1.2% |
| Jaime Jaquez Jr. PTS under 15.5 | CLE @ MIL | pointsbetau | 2.00 | 1.92 | 1.64 | 61.1% | 49.0% | 52.0% | +4.1% | +22.1% | 1.0% |
| Myles Turner PTS under 10.5 | CLE @ MIL | tab | 1.87 | 1.82 | 1.64 | 61.0% | 52.8% | 54.9% | +2.6% | +14.1% | 0.7% |
| Myles Turner PTS under 9.5 | CLE @ MIL | pointsbetau | 2.10 | 2.06 | 1.88 | 53.3% | 46.9% | 48.5% | +1.9% | +11.9% | 0.4% |
| Evan Mobley PTS under 17.5 | CLE @ MIL | pointsbetau | 2.00 | 1.97 | 1.84 | 54.4% | 49.6% | 50.8% | +1.6% | +8.8% | 0.4% |
| Myles Turner RA under 6.5 | CLE @ MIL | draftkings | 2.05 | 2.03 | 1.66 | 60.4% | 45.7% | 49.4% | +1.2% | +23.8% | 0.3% |
| Donovan Mitchell PTS over 24.5 (25+) | CLE @ MIL | pointsbetau | 2.00 | 1.98 | 1.85 | 53.9% | 49.3% | 50.5% | +1.0% | +7.8% | 0.2% |
| Kyle Kuzma PTS under 11.5 | CLE @ MIL | tab | 2.00 | 1.98 | 1.83 | 54.6% | 49.0% | 50.4% | +0.8% | +9.1% | 0.2% |
| Tyler Herro PRA under 30.5 | CLE @ MIL | draftkings | 1.92 | 1.91 | 1.58 | 63.1% | 48.7% | 52.3% | +0.4% | +21.1% | 0.1% |
| Sam Merrill PTS under 9.5 | CLE @ MIL | tab | 1.95 | 1.95 | 1.98 | 50.6% | 51.5% | 51.3% | +0.2% | -1.2% | 0.1% |

<details><summary>CLE players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| James Harden | 98% | 35.5<br><sub>33,33,39,34,36</sub> | 19.5<br><sub>16,12,19,16,24</sub> | 18.5 · 18.5<br><sub>o 50% · u 50%</sub> | 4.7<br><sub>3,8,5,2,5</sub> | 4.5<br><sub>o 53% · u 47%</sub> | 6.9<br><sub>5,7,9,6,4</sub> | 6.5<br><sub>o 55% · u 45%</sub> | 2.6<br><sub>3,1,3,2,3</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.4 | 3.3 | 31.2 |
| Donovan Mitchell | 98% | 35.1<br><sub>35,35,38,31,33</sub> | 26.8<br><sub>32,22,26,19,22</sub> | 24.5 · 23.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>10,5,5,5,3</sub> | 4.5<br><sub>o 55% · u 45%</sub> | 4.9<br><sub>3,4,7,7,3</sub> | 4.5<br><sub>o 54% · u 46%</sub> | 2.9<br><sub>2,2,5,2,1</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 1.6 | 0.3 | 2.6 | 36.7 |
| Evan Mobley | 98% | 34.0<br><sub>34,35,38,32,33</sub> | 17.6<br><sub>18,20,18,24,11</sub> | 17.5 · 18.5<br><sub>o 49% · u 51%</sub> | 8.8<br><sub>8,10,10,12,4</sub> | 9.5<br><sub>o 44% · u 56%</sub> | 3.6<br><sub>2,4,3,2,7</sub> | 3.5<br><sub>o 50% · u 50%</sub> | 1.3<br><sub>1,2,4,5,0</sub> | 1.5<br><sub>o 38% · u 62%</sub> | 0.9 | 1.4 | 1.8 | 30.0 |
| Jarrett Allen | 98% | 29.1<br><sub>28,27,27,30,30</sub> | 13.5<br><sub>14,21,10,8,14</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 8.6<br><sub>7,8,9,12,8</sub> | 9.5<br><sub>o 45% · u 55%</sub> | 1.6<br><sub>0,0,2,2,1</sub> |  | 0.1<br><sub>0,1,0,0,1</sub> |  | 1.2 | 1.3 | 1.2 | 23.7 |
| Peyton Watson | 98% | 28.8<br><sub>30,31,37,28,22</sub> | 13.8<br><sub>8,11,15,22,4</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 4.5<br><sub>1,3,8,6,4</sub> | 4.5<br><sub>o 47% · u 53%</sub> | 2.3<br><sub>2,4,1,2,3</sub> |  | 1.2<br><sub>0,2,0,1,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 1.1 | 1.7 | 20.6 |
| Sam Merrill | 98% | 24.8<br><sub>24,21,31,20,27</sub> | 10.2<br><sub>5,7,9,8,16</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 2.4<br><sub>5,2,4,1,2</sub> | 2.5<br><sub>o 48% · u 52%</sub> | 2.1<br><sub>2,3,2,1,3</sub> |  | 1.9<br><sub>1,1,1,2,4</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 0.1 | 0.7 | 14.6 |
| Meleek Thomas | 63% | 17.9<br><sub>-,-,19,20,-</sub> | 7.7<br><sub>-,-,16,10,-</sub> |  | 2.4<br><sub>-,-,2,4,-</sub> |  | 1.2<br><sub>-,-,0,1,-</sub> |  | 0.8<br><sub>-,-,4,0,-</sub> |  | 0.7 | 0.1 | 1.0 | 11.3 |
| Mario Hezonja | 96% | 16.0<br><sub>19,20,15,17,17</sub> | 6.1<br><sub>10,9,3,5,10</sub> | 8.5 · –<br><sub>o 40% · u 60%</sub> | 3.0<br><sub>3,5,3,3,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>2,1,1,2,2</sub> |  | 0.7<br><sub>0,2,1,1,2</sub> | 1.5<br><sub>o 29% · u 71%</sub> | 0.5 | 0.3 | 0.6 | 10.4 |
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
| Ryan Rollins | 98% | 27.9<br><sub>24,34,25,32,17</sub> | 14.6<br><sub>9,11,15,19,4</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 3.9<br><sub>6,7,4,2,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.1<br><sub>3,6,4,4,5</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 2.0<br><sub>1,2,2,3,0</sub> | 1.5<br><sub>o 59% · u 41%</sub> | 1.3 | 0.3 | 2.3 | 23.6 |
| Jaime Jaquez Jr. | 98% | 26.4<br><sub>31,35,27,25,27</sub> | 14.5<br><sub>22,19,21,8,19</sub> | 15.5 · 15.5<br><sub>o 48% · u 52%</sub> | 5.1<br><sub>7,11,8,6,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 3.8<br><sub>2,5,4,0,2</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 1.1<br><sub>1,2,2,0,3</sub> | 1.5<br><sub>o 37% · u 63%</sub> | 0.7 | 0.2 | 1.9 | 23.4 |
| Kyle Kuzma | 98% | 25.2<br><sub>27,30,35,29,18</sub> | 11.6<br><sub>5,14,14,17,4</sub> | 11.5 · 11.5<br><sub>o 49% · u 51%</sub> | 4.8<br><sub>6,9,12,7,6</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,4,3,3,1</sub> | 2.5<br><sub>o 49% · u 51%</sub> | 1.3<br><sub>1,2,0,4,0</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 0.8 | 0.3 | 1.6 | 19.2 |
| Myles Turner | 98% | 23.6<br><sub>32,30,20,28,22</sub> | 9.8<br><sub>11,12,0,6,4</sub> | 9.5 · 10.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>5,3,5,9,2</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>3,1,1,4,2</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.3<br><sub>2,2,0,0,0</sub> | 1.5<br><sub>o 46% · u 54%</sub> | 0.6 | 1.5 | 1.2 | 15.8 |
| Kasparas Jakucionis | 88% | 19.3<br><sub>26,23,25,21,19</sub> | 6.6<br><sub>15,7,12,7,4</sub> | 7.5 · 7.5<br><sub>o 45% · u 55%</sub> | 2.4<br><sub>3,2,3,4,2</sub> | 2.5<br><sub>o 53% · u 47%</sub> | 3.4<br><sub>3,5,2,5,6</sub> | 3.5<br><sub>o 48% · u 52%</sub> | 0.6<br><sub>1,1,0,1,0</sub> | 0.5<br><sub>o 59% · u 41%</sub> | 0.8 | 0.2 | 1.5 | 12.4 |
| AJ Green | 98% | 18.6<br><sub>15,17,19,20,24</sub> | 7.0<br><sub>6,11,11,3,9</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 1.9<br><sub>0,1,3,4,1</sub> |  | 1.2<br><sub>1,0,0,3,2</sub> |  | 1.2<br><sub>2,3,3,1,3</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 0.4 | 0.1 | 0.5 | 10.1 |
| Cormac Ryan | 26% | 17.7 | 8.9 |  | 2.1 |  | 1.3 |  | 1.2 |  | 0.7 | 0.2 | 1.2 | 12.3 |
| Kel'el Ware | 88% | 17.4<br><sub>14,15,29,19,17</sub> | 8.8<br><sub>7,11,19,16,6</sub> | 9.5 · 9.5<br><sub>o 48% · u 52%</sub> | 5.9<br><sub>3,4,13,14,8</sub> | 6.5<br><sub>o 51% · u 49%</sub> | 0.7<br><sub>1,0,1,0,0</sub> |  | 0.8<br><sub>0,1,2,0,0</sub> |  | 0.6 | 0.4 | 1.1 | 15.3 |
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
| Jonathan Kuminga PTS over 13.5 (14+) | MIN @ SAS | draftkings | 2.00 | 1.94 | 1.92 | 52.1% | 51.2% | 51.4% | +2.9% | +4.2% | 0.7% |
| Victor Wembanyama PTS under 24.5 | MIN @ SAS | pointsbetau | 2.00 | 1.95 | 1.95 | 51.2% | 51.3% | 51.3% | +2.6% | +2.5% | 0.6% |
| Devin Vassell PTS under 12.5 | MIN @ SAS | tab | 1.95 | 1.93 | 1.84 | 54.4% | 50.8% | 51.7% | +0.9% | +6.3% | 0.2% |
| LaMelo Ball PTS under 19.5 | MIN @ SAS | betright | 1.95 | 1.94 | 1.84 | 54.5% | 50.7% | 51.6% | +0.8% | +6.3% | 0.2% |
| Dylan Harper AST under 4.5 | MIN @ SAS | draftkings | 2.00 | 1.99 | 1.64 | 61.1% | 46.7% | 50.3% | +0.6% | +22.1% | 0.2% |

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.7<br><sub>30,31,37,35,33</sub> | 16.7<br><sub>15,14,14,19,23</sub> | 16.5 · 16.5<br><sub>o 49% · u 51%</sub> | 5.5<br><sub>6,6,6,7,6</sub> | 5.5<br><sub>o 49% · u 51%</sub> | 2.8<br><sub>3,3,4,4,7</sub> | 2.5<br><sub>o 56% · u 44%</sub> | 1.4<br><sub>2,1,2,1,1</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.1 | 0.9 | 1.8 | 25.1 |
| Jonathan Kuminga | 98% | 32.0<br><sub>27,26,36,32,22</sub> | 14.7<br><sub>11,13,10,20,5</sub> | 13.5 · 13.5<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>8,4,10,3,1</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>5,1,1,5,0</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.5<br><sub>2,3,0,3,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.0 | 0.5 | 1.4 | 22.4 |
| Ayo Dosunmu | 98% | 31.8<br><sub>27,23,26,32,30</sub> | 14.8<br><sub>14,9,9,17,15</sub> | 14.5 · 14.5<br><sub>o 49% · u 51%</sub> | 4.4<br><sub>7,3,1,3,7</sub> | 4.5<br><sub>o 43% · u 57%</sub> | 4.0<br><sub>10,3,0,4,2</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>1,1,1,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 1.0 | 0.4 | 1.8 | 23.2 |
| LaMelo Ball | 98% | 30.3<br><sub>23,17,31,28,29</sub> | 19.7<br><sub>12,15,11,8,24</sub> | 19.5 · 19.5<br><sub>o 48% · u 52%</sub> | 4.2<br><sub>5,1,0,4,4</sub> | 4.5<br><sub>o 44% · u 56%</sub> | 5.8<br><sub>5,8,6,8,7</sub> | 6.5<br><sub>o 46% · u 54%</sub> | 3.3<br><sub>2,4,1,2,6</sub> | 3.5<br><sub>o 43% · u 57%</sub> | 1.3 | 0.2 | 3.0 | 29.7 |
| Terrence Shannon Jr. | 97% | 27.0<br><sub>22,23,24,27,20</sub> | 14.1<br><sub>13,15,14,19,11</sub> | 11.5 · 12.5<br><sub>o 51% · u 49%</sub> | 3.2<br><sub>4,4,4,6,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 2.0<br><sub>1,3,5,2,2</sub> | 1.5<br><sub>o 58% · u 42%</sub> | 1.6<br><sub>2,3,3,1,2</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.6 | 0.1 | 1.4 | 19.3 |
| Bones Hyland | 96% | 18.8<br><sub>8,15,5,16,20</sub> | 9.4<br><sub>3,3,0,13,19</sub> | 8.5 · 8.5<br><sub>o 47% · u 53%</sub> | 2.1<br><sub>1,3,1,1,0</sub> |  | 2.4<br><sub>0,2,2,3,8</sub> | 2.5<br><sub>o 45% · u 55%</sub> | 1.5<br><sub>1,0,0,3,3</sub> | 1.5<br><sub>o 45% · u 55%</sub> | 0.6 | 0.3 | 1.1 | 14.0 |
| Joan Beringer | 91% | 18.5<br><sub>15,13,17,20,18</sub> | 7.2<br><sub>9,6,12,7,4</sub> | 9.5 · 9.5<br><sub>o 45% · u 55%</sub> | 6.2<br><sub>9,6,7,9,4</sub> | 8.5<br><sub>o 39% · u 61%</sub> | 0.7<br><sub>0,0,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.1 |
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
| Victor Wembanyama | 98% | 34.4<br><sub>34,32,29,27,39</sub> | 25.5<br><sub>12,25,23,29,36</sub> | 23.5 · 24.5<br><sub>o 50% · u 50%</sub> | 11.4<br><sub>13,13,7,10,14</sub> | 11.5<br><sub>o 49% · u 51%</sub> | 3.2<br><sub>3,2,2,2,5</sub> | 3.5<br><sub>o 40% · u 60%</sub> | 1.9<br><sub>0,2,2,0,4</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 1.2 | 3.6 | 2.8 | 40.0 |
| Devin Vassell | 98% | 33.4<br><sub>31,36,32,24,38</sub> | 12.6<br><sub>7,10,11,14,21</sub> | 12.5 · 11.5<br><sub>o 52% · u 48%</sub> | 4.7<br><sub>3,4,4,4,5</sub> | 4.5<br><sub>o 45% · u 55%</sub> | 2.9<br><sub>1,2,6,8,2</sub> | 2.5<br><sub>o 54% · u 46%</sub> | 1.9<br><sub>1,2,1,4,1</sub> | 2.5<br><sub>o 37% · u 63%</sub> | 1.2 | 0.5 | 1.0 | 20.1 |
| De'Aaron Fox | 98% | 33.0<br><sub>32,34,28,26,39</sub> | 16.4<br><sub>14,19,19,11,14</sub> | 15.5 · 14.5<br><sub>o 49% · u 51%</sub> | 4.2<br><sub>7,4,3,4,3</sub> | 3.5<br><sub>o 56% · u 44%</sub> | 6.2<br><sub>7,9,9,6,4</sub> | 6.5<br><sub>o 44% · u 56%</sub> | 1.5<br><sub>0,2,2,2,1</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 1.5 | 0.4 | 2.2 | 26.8 |
| Stephon Castle | 98% | 32.5<br><sub>28,33,28,27,38</sub> | 18.0<br><sub>24,15,19,15,14</sub> | 15.5 · 16.5<br><sub>o 53% · u 47%</sub> | 5.5<br><sub>7,7,4,5,6</sub> | 4.5<br><sub>o 57% · u 43%</sub> | 6.3<br><sub>1,5,8,5,8</sub> | 5.5<br><sub>o 54% · u 46%</sub> | 1.7<br><sub>5,3,3,3,1</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.2 | 0.3 | 3.1 | 29.8 |
| Dylan Harper | 98% | 31.8<br><sub>32,36,28,30,37</sub> | 16.6<br><sub>18,20,22,13,13</sub> | 16.5 · 15.5<br><sub>o 51% · u 49%</sub> | 5.6<br><sub>7,3,5,6,5</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 4.1<br><sub>5,2,2,6,8</sub> | 4.5<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>0,1,3,0,2</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 1.1 | 0.4 | 1.9 | 26.3 |
| Julian Champagnie | 98% | 28.3<br><sub>30,25,28,25,31</sub> | 9.9<br><sub>8,6,12,26,6</sub> | 10.5 · 10.5<br><sub>o 47% · u 53%</sub> | 4.8<br><sub>3,0,5,3,6</sub> | 4.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>1,0,3,3,0</sub> |  | 1.8<br><sub>2,2,3,8,2</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.6 | 0.8 | 16.1 |
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
| Amen Thompson PR over 22.5 (23+) | OKC @ HOU | draftkings | 1.96 | 1.87 | 1.58 | 63.4% | 50.0% | 53.3% | +4.6% | +24.4% | 1.2% |
| Kevin Durant PA over 26.5 (27+) | OKC @ HOU | draftkings | 1.96 | 1.95 | 1.61 | 62.1% | 47.6% | 51.2% | +0.5% | +21.7% | 0.1% |
| Amen Thompson PRA over 27.5 (28+) | OKC @ HOU | draftkings | 1.85 | 1.85 | 1.53 | 65.2% | 50.4% | 54.1% | +0.3% | +20.9% | 0.1% |
| Marcus Smart 3PM under 1.5 | OKC @ HOU | draftkings | 1.92 | 1.91 | 1.59 | 62.8% | 48.7% | 52.2% | +0.2% | +20.4% | 0.1% |

<details><summary>OKC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shai Gilgeous-Alexander | 98% | 34.6<br><sub>36,35,36,30,28</sub> | 30.4<br><sub>32,17,34,26,21</sub> | 29.5 · –<br><sub>o 48% · u 52%</sub> | 3.9<br><sub>6,2,6,3,6</sub> | 4.5<br><sub>o 41% · u 59%</sub> | 6.7<br><sub>4,3,5,3,2</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 1.6<br><sub>3,3,1,1,1</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.5 | 0.9 | 3.3 | 41.0 |
| Jared McCain | 98% | 30.0<br><sub>22,18,21,30,29</sub> | 15.9<br><sub>20,4,3,18,10</sub> | 14.5 · –<br><sub>o 50% · u 50%</sub> | 2.9<br><sub>2,0,1,3,4</sub> | 2.5<br><sub>o 57% · u 43%</sub> | 2.3<br><sub>2,1,0,4,4</sub> | 2.5<br><sub>o 42% · u 58%</sub> | 2.4<br><sub>6,0,1,4,0</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 0.8 | 0.2 | 1.9 | 21.1 |
| Ajay Mitchell | 98% | 29.6<br><sub>23,23,28,25,28</sub> | 19.0<br><sub>4,12,18,30,29</sub> | 18.5 · –<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>5,0,6,2,4</sub> | 3.5<br><sub>o 53% · u 47%</sub> | 4.4<br><sub>6,0,4,5,3</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 1.3<br><sub>0,0,1,1,2</sub> | 1.5<br><sub>o 42% · u 58%</sub> | 1.5 | 0.3 | 2.2 | 26.9 |
| Josh Dix | 67% | 27.2<br><sub>-,-,-,22,24</sub> | 4.4<br><sub>-,-,-,0,2</sub> |  | 2.6<br><sub>-,-,-,1,2</sub> |  | 1.3<br><sub>-,-,-,0,0</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.7 | 0.2 | 1.2 | 8.4 |
| Bennett Stirtz | 96% | 26.7<br><sub>1,2,11,25,28</sub> | 7.9<br><sub>0,0,2,7,8</sub> | 7.5 · –<br><sub>o 49% · u 51%</sub> | 1.6<br><sub>0,0,1,1,0</sub> |  | 1.6<br><sub>0,0,0,1,3</sub> |  | 1.0<br><sub>0,0,0,1,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.1 |
| Isaiah Hartenstein | 98% | 26.6<br><sub>17,23,27,26,26</sub> | 10.2<br><sub>4,6,12,15,10</sub> | 9.5 · –<br><sub>o 50% · u 50%</sub> | 9.5<br><sub>3,6,12,13,14</sub> | 9.5<br><sub>o 50% · u 50%</sub> | 3.2<br><sub>3,2,1,3,3</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.0 | 0.8 | 1.8 | 22.9 |
| Aday Mara | 96% | 24.2<br><sub>12,13,14,20,21</sub> | 8.2<br><sub>7,2,2,11,6</sub> | 7.5 · –<br><sub>o 50% · u 50%</sub> | 6.2<br><sub>2,3,3,10,3</sub> | 5.5<br><sub>o 46% · u 54%</sub> | 1.3<br><sub>1,0,1,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.7 | 1.4 | 1.4 | 15.6 |
| Kenrich Williams | 93% | 21.7<br><sub>7,6,7,24,17</sub> | 8.0<br><sub>3,3,3,3,7</sub> | 6.5 · –<br><sub>o 54% · u 46%</sub> | 4.5<br><sub>2,1,1,7,3</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.4<br><sub>0,1,0,0,0</sub> |  | 1.1<br><sub>1,1,1,0,1</sub> | 1.5<br><sub>o 33% · u 67%</sub> | 0.8 | 0.2 | 0.9 | 13.9 |
| Jaylin Williams | 98% | 21.3<br><sub>17,15,5,26,20</sub> | 6.1<br><sub>5,3,0,6,0</sub> |  | 5.3<br><sub>4,7,0,6,5</sub> |  | 2.0<br><sub>1,3,0,3,1</sub> |  | 0.9<br><sub>1,1,0,2,0</sub> |  | 0.6 | 0.5 | 0.8 | 13.3 |
| Micah Peavy | 48% | 13.1<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.7<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.3 | 0.3 | 0.5 | 1.6 |
| Brooks Barnhizer | 80% | 13.0<br><sub>1,2,-,3,14</sub> | 3.5<br><sub>0,0,-,0,3</sub> |  | 2.5<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,1,-,0,0</sub> |  | 0.2<br><sub>0,0,-,0,0</sub> |  | 0.5 | 0.2 | 0.5 | 6.7 |

</details>

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.8<br><sub>36,39,28,33,39</sub> | 18.8<br><sub>20,17,15,23,15</sub> | 15.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>10,11,5,4,3</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 5.7<br><sub>4,6,2,3,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 0.4<br><sub>1,0,0,0,0</sub> |  | 1.6 | 0.6 | 2.8 | 31.9 |
| Kevin Durant | 98% | 37.6<br><sub>37,37,30,31,37</sub> | 25.8<br><sub>20,22,22,18,28</sub> | 22.5 · –<br><sub>o 52% · u 48%</sub> | 6.5<br><sub>7,4,9,5,5</sub> | 4.5<br><sub>o 61% · u 39%</sub> | 5.1<br><sub>6,2,3,4,1</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 2.2<br><sub>2,3,1,2,1</sub> | 1.5<br><sub>o 61% · u 39%</sub> | 0.8 | 1.0 | 3.8 | 37.4 |
| Jabari Smith Jr. | 98% | 37.1<br><sub>34,33,39,30,35</sub> | 17.4<br><sub>7,14,16,14,22</sub> | 14.5 · –<br><sub>o 53% · u 47%</sub> | 7.4<br><sub>5,5,12,2,3</sub> | 5.5<br><sub>o 60% · u 40%</sub> | 2.3<br><sub>1,3,5,2,2</sub> |  | 2.7<br><sub>1,2,2,3,3</sub> | 2.5<br><sub>o 44% · u 56%</sub> | 0.8 | 0.8 | 1.8 | 27.0 |
| Alperen Sengun | 58% | 35.4<br><sub>36,33,37,-,-</sub> | 19.7<br><sub>29,17,29,-,-</sub> | 18.5 · –<br><sub>o 50% · u 50%</sub> | 10.0<br><sub>7,10,9,-,-</sub> | 8.5<br><sub>o 54% · u 46%</sub> | 6.3<br><sub>7,7,9,-,-</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>2,1,1,-,-</sub> |  | 1.2 | 0.9 | 3.6 | 36.0 |
| Tari Eason | 98% | 30.9<br><sub>27,31,33,31,26</sub> | 12.6<br><sub>12,19,13,5,11</sub> | 10.5 · –<br><sub>o 50% · u 50%</sub> | 7.4<br><sub>6,3,8,9,13</sub> | 5.5<br><sub>o 53% · u 47%</sub> | 1.6<br><sub>0,0,2,1,2</sub> |  | 1.4<br><sub>0,0,1,1,0</sub> | 1.5<br><sub>o 36% · u 64%</sub> | 1.4 | 0.7 | 1.5 | 21.7 |
| Marcus Smart | 63% | 26.0<br><sub>21,-,-,-,17</sub> | 9.2<br><sub>5,-,-,-,8</sub> | 9.5 · –<br><sub>o 47% · u 53%</sub> | 2.8<br><sub>3,-,-,-,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 3.2<br><sub>1,-,-,-,4</sub> | 3.5<br><sub>o 45% · u 55%</sub> | 1.3<br><sub>0,-,-,-,0</sub> | 1.5<br><sub>o 48% · u 52%</sub> | 1.4 | 0.3 | 1.9 | 15.2 |
| Clint Capela | 88% | 22.3<br><sub>-,11,4,22,30</sub> | 6.5<br><sub>-,2,2,10,5</sub> |  | 7.8<br><sub>-,3,2,8,11</sub> |  | 1.4<br><sub>-,1,0,2,5</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.8 | 1.2 | 0.9 | 15.7 |
| Bogdan Bogdanovic | 91% | 19.5<br><sub>9,20,13,15,11</sub> | 7.8<br><sub>3,11,5,16,6</sub> |  | 2.4<br><sub>1,1,2,2,1</sub> |  | 1.9<br><sub>0,1,1,4,0</sub> |  | 1.3<br><sub>1,3,1,4,0</sub> |  | 0.6 | 0.2 | 0.9 | 12.1 |
| Oscar Tshiebwe | 76% | 16.5<br><sub>-,-,-,14,11</sub> | 6.3<br><sub>-,-,-,7,0</sub> |  | 6.8<br><sub>-,-,-,5,5</sub> |  | 0.9<br><sub>-,-,-,2,0</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.6 | 0.4 | 1.0 | 14.0 |
| Jae'Sean Tate | 64% | 9.5<br><sub>-,1,1,4,-</sub> | 3.1<br><sub>-,0,0,0,-</sub> |  | 2.1<br><sub>-,0,1,0,-</sub> |  | 0.5<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.7 |
| Bruce Thornton | 63% | 8.7<br><sub>-,4,1,3,-</sub> | 2.7<br><sub>-,0,0,5,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.1 | 0.4 | 3.7 |
| Isaiah Crawford | 58% | 8.3<br><sub>-,1,1,5,-</sub> | 2.7<br><sub>-,0,0,3,-</sub> |  | 1.5<br><sub>-,0,0,0,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.2<br><sub>-,0,0,1,-</sub> |  | 0.2 | 0.3 | 0.3 | 4.6 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-31/`._
