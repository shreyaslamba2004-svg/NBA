# NBA model · Fri 30 Oct 2026 (US date)

Updated **Sat 31 Oct, 11:09 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-30/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jarace Walker PTS over 10.5 (11+) | IND @ MIA | pointsbetau | 2.00 | 1.86 | 1.58 | 63.4% | 50.4% | 53.6% | +7.3% | +26.7% | 1.8% |
| Pascal Siakam AST over 5.5 (6+) | IND @ MIA | draftkings | 3.66 | 3.43 | 2.50 | 39.9% | 25.5% | 29.1% | +6.6% | +46.2% | 0.6% |

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quenton Jackson PA over 24.5 (25+) | IND @ MIA | draftkings | 26.00 | 17.61 | 8.39 | 11.9% | 3.6% | 5.7% | +47.6% | +210.0% | 0.5% |
| Quenton Jackson PR over 19.5 (20+) | IND @ MIA | draftkings | 13.80 | 9.69 | 4.77 | 20.9% | 6.8% | 10.3% | +42.4% | +189.1% | 0.8% |
| Quenton Jackson AST over 7.5 (8+) | IND @ MIA | draftkings | 17.60 | 12.42 | 6.15 | 16.2% | 5.3% | 8.1% | +41.6% | +186.0% | 0.6% |
| Quenton Jackson PRA over 29.5 (30+) | IND @ MIA | draftkings | 27.00 | 19.23 | 9.59 | 10.4% | 3.5% | 5.2% | +40.5% | +181.5% | 0.4% |
| Kevin Durant PRA over 54.5 (55+) | HOU @ DAL | draftkings | 21.00 | 15.50 | 8.02 | 12.5% | 4.5% | 6.5% | +35.5% | +161.8% | 0.4% |
| Quenton Jackson PTS over 19.5 (20+) | IND @ MIA | draftkings | 30.00 | 22.22 | 11.53 | 8.7% | 3.1% | 4.5% | +35.1% | +160.1% | 0.3% |
| Kevin Durant PA over 49.5 (50+) | HOU @ DAL | draftkings | 27.00 | 20.33 | 10.75 | 9.3% | 3.5% | 4.9% | +32.9% | +151.2% | 0.3% |
| Kevin Durant PRA over 49.5 (50+) | HOU @ DAL | draftkings | 11.20 | 8.77 | 4.86 | 20.6% | 8.3% | 11.4% | +27.7% | +130.6% | 0.7% |
| Pascal Siakam PA over 49.5 (50+) | IND @ MIA | draftkings | 24.00 | 19.23 | 10.95 | 9.1% | 3.9% | 5.2% | +24.9% | +119.1% | 0.3% |
| Pascal Siakam PTS over 44.5 (45+) | IND @ MIA | draftkings | 27.00 | 21.69 | 12.42 | 8.1% | 3.5% | 4.6% | +24.4% | +117.4% | 0.2% |
| Kevin Durant PR over 49.5 (50+) | HOU @ DAL | draftkings | 20.80 | 16.78 | 9.64 | 10.4% | 4.5% | 6.0% | +24.0% | +115.7% | 0.3% |
| Kevin Durant PTS over 44.5 (45+) | HOU @ DAL | draftkings | 28.00 | 22.73 | 13.15 | 7.6% | 3.3% | 4.4% | +23.3% | +113.0% | 0.2% |
| Pascal Siakam PA over 44.5 (45+) | IND @ MIA | draftkings | 13.20 | 10.74 | 6.24 | 16.0% | 7.1% | 9.3% | +22.9% | +111.4% | 0.5% |
| Kevin Durant PTS over 39.5 (40+) | HOU @ DAL | draftkings | 14.00 | 11.76 | 7.16 | 14.0% | 6.7% | 8.5% | +19.0% | +95.6% | 0.4% |
| Pascal Siakam PTS over 39.5 (40+) | IND @ MIA | draftkings | 13.20 | 11.12 | 6.79 | 14.7% | 7.1% | 9.0% | +18.7% | +94.3% | 0.4% |
| Pascal Siakam AST over 7.5 (8+) | IND @ MIA | draftkings | 11.20 | 9.61 | 6.02 | 16.6% | 8.3% | 10.4% | +16.6% | +86.2% | 0.4% |
| Kevin Durant PR over 44.5 (45+) | HOU @ DAL | draftkings | 10.30 | 8.87 | 5.58 | 17.9% | 9.1% | 11.3% | +16.2% | +84.5% | 0.4% |
| Zaccharie Risacher REB over 7.5 (8+) | HOU @ DAL | draftkings | 9.10 | 8.20 | 5.56 | 18.0% | 10.3% | 12.2% | +11.0% | +63.8% | 0.3% |
| Pascal Siakam PA over 39.5 (40+) | IND @ MIA | draftkings | 6.31 | 5.69 | 3.86 | 25.9% | 14.8% | 17.6% | +11.0% | +63.6% | 0.5% |
| Jabari Smith Jr. REB over 11.5 (12+) | HOU @ DAL | draftkings | 14.80 | 13.50 | 9.34 | 10.7% | 6.3% | 7.4% | +9.7% | +58.5% | 0.2% |
| Kevin Durant PTS over 34.5 (35+) | HOU @ DAL | draftkings | 6.50 | 5.94 | 4.13 | 24.2% | 14.4% | 16.8% | +9.4% | +57.2% | 0.4% |
| Pascal Siakam AST over 9.5 (10+) | IND @ MIA | draftkings | 29.00 | 26.53 | 18.45 | 5.4% | 3.2% | 3.8% | +9.4% | +57.2% | 0.1% |
| Jabari Smith Jr. REB over 9.5 (10+) | HOU @ DAL | draftkings | 6.35 | 5.82 | 4.06 | 24.6% | 14.7% | 17.2% | +9.2% | +56.3% | 0.4% |
| Quenton Jackson REB over 5.5 (6+) | IND @ MIA | draftkings | 10.50 | 9.64 | 6.77 | 14.8% | 8.9% | 10.4% | +8.9% | +55.2% | 0.2% |
| Amen Thompson STL over 3.5 (4+) | HOU @ DAL | draftkings | 12.00 | 11.04 | 7.76 | 12.9% | 7.8% | 9.1% | +8.8% | +54.7% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 8.5 (9+) | HOU @ DAL | draftkings | 22.00 | 14.81 | 7.01 | 14.3% | 4.2% | 6.8% | +48.6% | +213.9% | 0.6% |
| Quenton Jackson AST over 8.5 (9+) | IND @ MIA | draftkings | 27.00 | 19.69 | 10.06 | 9.9% | 3.5% | 5.1% | +37.2% | +168.5% | 0.4% |
| Jay Huff AST over 4.5 (5+) | IND @ MIA | draftkings | 27.00 | 22.83 | 14.01 | 7.1% | 3.5% | 4.4% | +18.3% | +92.7% | 0.2% |
| Pascal Siakam AST over 8.5 (9+) | IND @ MIA | draftkings | 19.00 | 16.23 | 10.13 | 9.9% | 4.9% | 6.2% | +17.0% | +87.5% | 0.2% |
| Zaccharie Risacher REB over 8.5 (9+) | HOU @ DAL | draftkings | 15.20 | 13.59 | 9.10 | 11.0% | 6.2% | 7.4% | +11.9% | +67.1% | 0.2% |
| Pascal Siakam AST over 6.5 (7+) | IND @ MIA | draftkings | 6.29 | 5.63 | 3.79 | 26.4% | 14.9% | 17.8% | +11.6% | +66.1% | 0.5% |
| Jabari Smith Jr. REB over 10.5 (11+) | HOU @ DAL | draftkings | 9.60 | 8.71 | 5.98 | 16.7% | 9.7% | 11.5% | +10.2% | +60.6% | 0.3% |
| Bam Adebayo REB over 14.5 (15+) | IND @ MIA | draftkings | 9.70 | 8.93 | 6.28 | 15.9% | 9.6% | 11.2% | +8.7% | +54.4% | 0.2% |
| Zaccharie Risacher REB over 6.5 (7+) | HOU @ DAL | draftkings | 5.36 | 4.98 | 3.56 | 28.1% | 17.4% | 20.1% | +7.7% | +50.5% | 0.4% |
| Quenton Jackson REB over 4.5 (5+) | IND @ MIA | draftkings | 5.77 | 5.36 | 3.85 | 26.0% | 16.2% | 18.6% | +7.5% | +49.8% | 0.4% |
| Tari Eason REB over 10.5 (11+) | HOU @ DAL | draftkings | 9.50 | 8.83 | 6.34 | 15.8% | 9.8% | 11.3% | +7.5% | +49.8% | 0.2% |
| Amen Thompson AST over 8.5 (9+) | HOU @ DAL | draftkings | 9.60 | 8.93 | 6.41 | 15.6% | 9.7% | 11.2% | +7.5% | +49.7% | 0.2% |
| Jarace Walker AST over 4.5 (5+) | IND @ MIA | draftkings | 6.17 | 5.74 | 4.13 | 24.2% | 15.2% | 17.4% | +7.4% | +49.3% | 0.4% |
| Bam Adebayo REB over 16.5 (17+) | IND @ MIA | draftkings | 19.40 | 18.08 | 13.03 | 7.7% | 4.8% | 5.5% | +7.3% | +48.9% | 0.1% |
| Jabari Smith Jr. REB over 8.5 (9+) | HOU @ DAL | draftkings | 4.25 | 3.97 | 2.86 | 34.9% | 22.0% | 25.2% | +7.2% | +48.4% | 0.5% |
| Quenton Jackson REB over 6.5 (7+) | IND @ MIA | draftkings | 18.40 | 17.27 | 12.62 | 7.9% | 5.1% | 5.8% | +6.6% | +45.8% | 0.1% |
| Jabari Smith Jr. REB over 12.5 (13+) | HOU @ DAL | draftkings | 22.00 | 20.70 | 15.22 | 6.6% | 4.2% | 4.8% | +6.2% | +44.5% | 0.1% |
| Fred VanVleet REB over 6.5 (7+) | HOU @ DAL | draftkings | 11.60 | 10.93 | 8.06 | 12.4% | 8.1% | 9.2% | +6.1% | +44.0% | 0.1% |
| Bam Adebayo REB over 12.5 (13+) | IND @ MIA | draftkings | 4.85 | 4.58 | 3.39 | 29.5% | 19.3% | 21.8% | +5.8% | +42.9% | 0.4% |
| Sandro Mamukelashvili REB over 8.5 (9+) | LAL @ GSW | draftkings | 11.00 | 10.43 | 7.78 | 12.9% | 8.5% | 9.6% | +5.5% | +41.4% | 0.1% |
| Nikola Jokic AST over 16.5 (17+) | DEN @ PHX | draftkings | 19.60 | 18.59 | 13.87 | 7.2% | 4.8% | 5.4% | +5.4% | +41.3% | 0.1% |
| Kevin Durant REB over 10.5 (11+) | HOU @ DAL | draftkings | 16.00 | 15.20 | 11.34 | 8.8% | 5.8% | 6.6% | +5.3% | +41.0% | 0.1% |
| Kevin Durant REB over 8.5 (9+) | HOU @ DAL | draftkings | 6.22 | 5.91 | 4.42 | 22.6% | 15.0% | 16.9% | +5.3% | +40.7% | 0.2% |
| Sandro Mamukelashvili REB over 6.5 (7+) | LAL @ GSW | draftkings | 4.48 | 4.26 | 3.20 | 31.3% | 20.9% | 23.5% | +5.1% | +40.1% | 0.4% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Khaman Maluach PR under 16.5 | DEN @ PHX | draftkings | 1.88 | Oso Ighodaro | 77.0% | 81.1% | +7.3% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Quenton Jackson PR over 9.5 (10+) | IND @ MIA | draftkings | 2.01 | 1.83 | 1.27 | 78.6% | 46.5% | 54.5% | +9.6% | +58.0% | 2.0% |
| Quenton Jackson PA over 9.5 (10+) | IND @ MIA | draftkings | 1.83 | 1.68 | 1.18 | 84.6% | 51.0% | 59.4% | +8.9% | +55.1% | 2.0% |
| Quenton Jackson AST over 3.5 (4+) | IND @ MIA | draftkings | 2.29 | 2.10 | 1.48 | 67.6% | 40.8% | 47.5% | +8.8% | +54.8% | 1.7% |
| Kevin Durant PRA over 39.5 (40+) | HOU @ DAL | draftkings | 3.14 | 2.92 | 2.10 | 47.7% | 29.8% | 34.2% | +7.5% | +49.8% | 0.9% |
| Kevin Durant RA over 9.5 (10+) | HOU @ DAL | draftkings | 1.95 | 1.84 | 1.36 | 73.3% | 48.0% | 54.3% | +6.0% | +43.1% | 1.6% |
| Kevin Durant AST over 3.5 (4+) | HOU @ DAL | draftkings | 1.78 | 1.68 | 1.27 | 78.9% | 53.0% | 59.5% | +5.6% | +40.0% | 1.8% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play).

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| IND @ MIA | Sat 31 Oct 11:00 | 116.5–126.6 | IND 24% | 4.24 / 1.31 | MIA -10.5 | 242.5 | MIA -8.5 covers 55%; o237.5 62% |
| HOU @ DAL | Sat 31 Oct 11:00 | 116.8–113.2 | HOU 60% | 1.68 / 2.48 | DAL +3.5 | 229.5 | DAL +5.5 covers 55%; o223.5 63% |
| LAC @ MIN | Sat 31 Oct 11:00 | 112.8–113.2 | LAC 49% | 2.04 / 1.96 | MIN +0.5 | 225.5 | MIN -6.5 covers 34%; o222.5 57% |
| LAL @ GSW | Sat 31 Oct 13:00 | 114.7–114.0 | LAL 52% | 1.91 / 2.10 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| DEN @ PHX | Sat 31 Oct 13:00 | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +4.5 covers 56%; o231.5 43% |

### IND @ MIA
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND), Obi Toppin (IND), Ivica Zubac (IND)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jarace Walker PTS over 10.5 (11+) | IND @ MIA | pointsbetau | 2.00 | 1.86 | 1.58 | 63.4% | 50.4% | 53.6% | +7.3% | +26.7% | 1.8% |
| Pascal Siakam PTS over 23.5 (24+) | IND @ MIA | pointsbetau | 1.95 | 1.88 | 1.63 | 61.5% | 50.4% | 53.2% | +3.8% | +20.1% | 1.0% |
| Andrew Nembhard PTS over 17.5 (18+) | IND @ MIA | unibet | 2.00 | 1.93 | 1.71 | 58.5% | 49.4% | 51.7% | +3.4% | +17.1% | 0.9% |
| Giannis Antetokounmpo PTS under 31.5 | IND @ MIA | sportsbet | 1.90 | 1.87 | 1.63 | 61.4% | 50.9% | 53.6% | +1.8% | +16.8% | 0.5% |
| Bam Adebayo STL over 1.5 (2+) | IND @ MIA | draftkings | 2.78 | 2.73 | 2.22 | 45.0% | 33.8% | 36.6% | +1.7% | +25.0% | 0.2% |
| Kelly Oubre Jr. PTS over 11.5 (12+) | IND @ MIA | sportsbet | 1.92 | 1.89 | 1.64 | 61.0% | 50.2% | 52.9% | +1.5% | +17.1% | 0.4% |
| Giannis Antetokounmpo PTS under 30.5 | IND @ MIA | pointsbetau | 2.00 | 1.98 | 1.71 | 58.3% | 48.1% | 50.6% | +1.2% | +16.6% | 0.3% |
| Kelly Oubre Jr. PTS over 12.5 (13+) | IND @ MIA | unibet | 2.00 | 1.98 | 1.85 | 54.2% | 49.1% | 50.4% | +0.8% | +8.3% | 0.2% |
| Aaron Nesmith PTS over 13.5 (14+) | IND @ MIA | pointsbetau | 1.80 | 1.79 | 1.53 | 65.2% | 52.7% | 55.8% | +0.5% | +17.4% | 0.1% |
| Pascal Siakam 3PM over 1.5 (2+) | IND @ MIA | draftkings | 2.14 | 2.14 | 1.81 | 55.2% | 44.0% | 46.8% | +0.1% | +18.1% | 0.0% |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 76% | 35.1<br><sub>34,32,30,-,35</sub> | 20.2<br><sub>18,16,14,-,18</sub> | 17.5 · 16.5 | 3.6<br><sub>2,2,1,-,3</sub> | 2.5 | 9.6<br><sub>9,5,3,-,14</sub> | 8.5 | 2.1<br><sub>0,1,4,-,1</sub> | 1.5 | 1.2 | 0.2 | 3.2 | 33.5 |
| Pascal Siakam | 98% | 35.0<br><sub>35,29,26,37,34</sub> | 28.0<br><sub>30,23,21,20,26</sub> | 24.5 · 23.5 | 8.2<br><sub>8,3,7,13,11</sub> | 7.5 | 5.1<br><sub>1,3,6,6,3</sub> | 3.5 | 1.9<br><sub>1,3,3,1,0</sub> | 1.5 | 1.2 | 0.4 | 3.2 | 41.3 |
| Kelly Oubre Jr. | 98% | 30.1<br><sub>28,20,20,23,30</sub> | 13.9<br><sub>4,3,14,9,15</sub> | 12.5 · 11.5 | 5.1<br><sub>2,2,2,3,3</sub> | 4.5 | 2.0<br><sub>3,2,2,1,1</sub> |  | 1.3<br><sub>0,1,1,1,1</sub> | 1.5 | 1.1 | 0.5 | 1.5 | 21.0 |
| Aaron Nesmith | 98% | 29.3<br><sub>-,20,19,21,27</sub> | 17.2<br><sub>-,9,13,13,18</sub> | 14.5 · 13.5 | 4.1<br><sub>-,4,1,0,2</sub> | 3.5 | 2.1<br><sub>-,1,2,1,1</sub> |  | 2.4<br><sub>-,1,2,3,3</sub> | 1.5 | 0.8 | 0.5 | 1.8 | 23.5 |
| Jarace Walker | 96% | 27.9<br><sub>19,17,19,29,22</sub> | 13.3<br><sub>3,2,6,10,7</sub> | 10.5 · 10.5 | 6.5<br><sub>6,1,7,8,8</sub> | 5.5 | 3.2<br><sub>2,1,1,2,1</sub> |  | 1.7<br><sub>1,0,0,2,1</sub> | 1.5 | 0.9 | 0.4 | 2.2 | 23.0 |
| Quenton Jackson | 97% | 24.8<br><sub>16,17,18,27,14</sub> | 11.3<br><sub>6,8,5,4,2</sub> |  | 3.4<br><sub>4,1,1,2,2</sub> |  | 4.9<br><sub>1,3,2,4,6</sub> |  | 0.9<br><sub>0,1,0,0,0</sub> |  | 1.0 | 0.2 | 1.5 | 19.6 |
| Jay Huff | 88% | 22.7<br><sub>-,5,21,23,16</sub> | 9.6<br><sub>-,0,14,6,3</sub> | 8.5 · 8.5 | 4.5<br><sub>-,2,2,6,6</sub> | 4.5 | 2.0<br><sub>-,0,3,1,2</sub> |  | 1.3<br><sub>-,0,2,0,1</sub> | 1.5 | 0.5 | 1.4 | 1.0 | 16.1 |
| Larry Nance Jr. | 88% | 22.4<br><sub>5,1,22,19,23</sub> | 6.4<br><sub>0,0,6,2,5</sub> | 6.5 · 6.5 | 4.9<br><sub>0,0,6,3,5</sub> | 4.5 | 1.5<br><sub>0,0,1,1,0</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 1.0 | 0.4 | 0.9 | 12.8 |
| Jalen Slawson | 88% | 15.8<br><sub>-,16,8,3,12</sub> | 4.6<br><sub>-,4,1,2,2</sub> |  | 3.2<br><sub>-,5,2,1,1</sub> |  | 1.7<br><sub>-,2,0,0,1</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.6 | 0.7 | 9.5 |
| Kobe Brown | 48% | 15.0<br><sub>-,1,-,-,-</sub> | 5.8<br><sub>-,0,-,-,-</sub> |  | 3.0<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.8 | 10.2 |
| Braden Smith | 58% | 14.2<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.3 | 0.6 | 2.4 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 33.8<br><sub>33,33,37,33,34</sub> | 13.1<br><sub>11,18,22,21,10</sub> | 11.5 · 11.5 | 2.9<br><sub>0,2,1,0,1</sub> | 2.5 | 7.0<br><sub>11,5,10,2,10</sub> | 6.5 | 1.5<br><sub>1,3,3,2,0</sub> | 1.5 | 1.3 | 0.2 | 1.9 | 23.0 |
| Bam Adebayo | 98% | 33.6<br><sub>31,23,39,30,33</sub> | 20.5<br><sub>15,4,20,8,24</sub> | 18.5 · 18.5 | 10.7<br><sub>7,6,8,8,9</sub> | 9.5 | 3.9<br><sub>4,3,4,3,3</sub> | 3.5 | 1.6<br><sub>1,0,2,0,0</sub> | 1.5 | 1.6 | 0.7 | 1.8 | 35.1 |
| Giannis Antetokounmpo | 98% | 32.8<br><sub>30,33,25,39,31</sub> | 29.6<br><sub>35,36,14,29,24</sub> | 31.5 · 31.5 | 12.4<br><sub>6,12,6,14,18</sub> | 11.5 | 6.1<br><sub>1,5,3,11,3</sub> | 6.5 | 0.5<br><sub>0,1,0,2,0</sub> | 0.5 | 1.1 | 0.9 | 3.1 | 48.1 |
| Pelle Larsson | 98% | 30.9<br><sub>24,29,36,34,31</sub> | 12.8<br><sub>2,7,15,12,17</sub> | 11.5 · 11.5 | 4.0<br><sub>3,2,7,0,6</sub> | 3.5 | 3.9<br><sub>4,1,4,4,8</sub> | 3.5 | 1.0<br><sub>0,1,1,1,2</sub> |  | 1.1 | 0.3 | 1.6 | 20.7 |
| Andrew Wiggins | 98% | 28.2<br><sub>27,26,18,34,29</sub> | 13.2<br><sub>11,8,4,12,18</sub> | 12.5 · 12.5 | 4.7<br><sub>2,8,1,3,2</sub> | 3.5 | 2.2<br><sub>1,2,1,1,2</sub> | 1.5 | 1.6<br><sub>1,1,0,0,4</sub> | 1.5 | 1.0 | 1.0 | 1.2 | 20.1 |
| Bobby Portis | 98% | 23.5<br><sub>25,21,27,24,23</sub> | 11.6<br><sub>7,11,13,10,11</sub> | 10.5 · 11.5 | 7.0<br><sub>4,8,8,12,9</sub> | 6.5 | 1.6<br><sub>1,2,0,2,4</sub> |  | 1.6<br><sub>1,3,2,3,1</sub> | 1.5 | 0.7 | 0.4 | 0.9 | 20.2 |
| Tim Hardaway Jr. | 98% | 19.3<br><sub>18,21,21,16,22</sub> | 8.4<br><sub>3,8,5,5,14</sub> | 8.5 · 8.5 | 2.4<br><sub>4,4,0,2,3</sub> |  | 1.0<br><sub>1,1,0,1,1</sub> |  | 1.2<br><sub>1,2,0,1,2</sub> | 1.5 | 0.6 | 0.2 | 0.5 | 11.8 |
| Klay Thompson | 98% | 17.6<br><sub>16,24,27,15,17</sub> | 8.1<br><sub>10,6,14,6,3</sub> | 7.5 · 7.5 | 1.7<br><sub>1,2,3,1,1</sub> |  | 1.1<br><sub>0,2,0,1,2</sub> |  | 1.4<br><sub>3,2,4,2,1</sub> | 2.5 | 0.5 | 0.3 | 0.6 | 10.9 |
| Dru Smith | 64% | 12.7<br><sub>-,6,-,15,14</sub> | 4.2<br><sub>-,3,-,6,3</sub> |  | 1.7<br><sub>-,0,-,2,0</sub> |  | 1.9<br><sub>-,1,-,1,3</sub> |  | 0.3<br><sub>-,1,-,2,0</sub> |  | 1.0 | 0.3 | 0.6 | 7.8 |
| Nikola Jovic | 67% | 10.1<br><sub>24,13,6,-,7</sub> | 3.9<br><sub>4,5,0,-,5</sub> |  | 2.1<br><sub>4,4,2,-,3</sub> |  | 1.0<br><sub>2,1,0,-,0</sub> |  | 0.4<br><sub>0,0,0,-,1</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Tre Donaldson | 16% | 8.6 | 3.7 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Simone Fontecchio | 48% | 7.8<br><sub>3,3,-,-,-</sub> | 3.9<br><sub>0,0,-,-,-</sub> |  | 1.5<br><sub>0,1,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.5<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 6.0 |
| Keshad Johnson | 23% | 7.2 | 3.4 |  | 1.5 |  | 0.3 |  | 0.2 |  | 0.4 | 0.2 | 0.3 | 5.2 |
| Nick Richards | 48% | 6.6<br><sub>3,3,-,-,-</sub> | 2.7<br><sub>4,3,-,-,-</sub> |  | 2.4<br><sub>1,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.1<br><sub>0,1,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.4 |
| Myron Gardner | 48% | 6.2<br><sub>3,3,-,-,-</sub> | 2.5<br><sub>4,0,-,-,-</sub> |  | 1.8<br><sub>2,0,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |
| Ryan Conwell | 52% | 5.9<br><sub>3,3,4,-,-</sub> | 2.4<br><sub>0,2,3,-,-</sub> |  | 0.9<br><sub>0,0,1,-,-</sub> |  | 0.7<br><sub>2,0,0,-,-</sub> |  | 0.2<br><sub>0,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Vladislav Goldin | 23% | 5.4 | 1.9 |  | 1.6 |  | 0.4 |  | 0.0 |  | 0.2 | 0.4 | 0.3 | 3.8 |

</details>


### HOU @ DAL
Out: Santi Aldama (DAL), Sergio de Larrea (DAL), Dereck Lively II (DAL), Steven Adams (HOU), Alperen Sengun (HOU), Reed Sheppard (HOU)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Naji Marshall PTS over 11.5 (12+) | HOU @ DAL | unibet | 2.00 | 1.93 | 1.71 | 58.5% | 49.6% | 51.8% | +3.6% | +16.9% | 0.9% |
| Cooper Flagg PTS under 24.5 | HOU @ DAL | pointsbetau | 1.83 | 1.79 | 1.49 | 67.0% | 52.2% | 55.9% | +2.4% | +22.8% | 0.7% |
| Cooper Flagg PTS under 23.5 | HOU @ DAL | sportsbet | 1.96 | 1.92 | 1.58 | 63.2% | 48.3% | 52.0% | +2.0% | +23.9% | 0.5% |
| Amen Thompson STL over 1.5 (2+) | HOU @ DAL | draftkings | 2.30 | 2.27 | 1.88 | 53.2% | 40.9% | 44.0% | +1.2% | +22.5% | 0.2% |
| Kevin Durant PTS over 23.5 (24+) | HOU @ DAL | pointsbetau | 1.90 | 1.88 | 1.60 | 62.4% | 50.0% | 53.1% | +0.9% | +18.6% | 0.3% |
| Tari Eason STL over 1.5 (2+) | HOU @ DAL | draftkings | 2.58 | 2.56 | 2.11 | 47.5% | 36.3% | 39.1% | +0.9% | +22.5% | 0.1% |
| Fred VanVleet REB over 3.5 (4+) | HOU @ DAL | draftkings | 2.22 | 2.20 | 1.83 | 54.7% | 42.4% | 45.5% | +0.9% | +21.4% | 0.2% |
| Tari Eason PTS over 13.5 (14+) | HOU @ DAL | sportsbet | 2.08 | 2.07 | 2.18 | 45.9% | 49.1% | 48.3% | +0.5% | -4.5% | 0.1% |
| Cooper Flagg PRA under 35.5 | HOU @ DAL | draftkings | 1.93 | 1.92 | 1.59 | 62.9% | 48.5% | 52.1% | +0.4% | +21.2% | 0.1% |
| Zaccharie Risacher REB over 4.5 (5+) | HOU @ DAL | draftkings | 2.16 | 2.15 | 1.78 | 56.0% | 43.3% | 46.5% | +0.4% | +21.0% | 0.1% |
| Tari Eason RA over 7.5 (8+) | HOU @ DAL | draftkings | 1.86 | 1.86 | 1.55 | 64.4% | 50.3% | 53.8% | +0.2% | +20.0% | 0.1% |
| Cooper Flagg PR under 30.5 | HOU @ DAL | draftkings | 1.85 | 1.84 | 1.53 | 65.2% | 50.6% | 54.2% | +0.2% | +20.5% | 0.1% |
| Tari Eason REB over 6.5 (7+) | HOU @ DAL | draftkings | 2.10 | 2.10 | 1.76 | 56.8% | 44.6% | 47.7% | +0.1% | +19.3% | 0.0% |
| Kevin Durant PA over 28.5 (29+) | HOU @ DAL | draftkings | 1.86 | 1.86 | 1.56 | 64.1% | 50.3% | 53.7% | +0.1% | +19.3% | 0.0% |
| Cooper Flagg PA under 29.5 | HOU @ DAL | draftkings | 1.85 | 1.85 | 1.55 | 64.5% | 50.4% | 53.9% | +0.0% | +19.7% | 0.0% |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.3<br><sub>33,36,39,28,33</sub> | 20.7<br><sub>16,20,17,15,23</sub> | 18.5 · 18.5 | 8.1<br><sub>10,10,11,5,4</sub> | 7.5 | 5.8<br><sub>4,4,6,2,3</sub> | 4.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.8 | 0.7 | 2.5 | 34.6 |
| Jabari Smith Jr. | 98% | 36.8<br><sub>36,34,33,39,30</sub> | 18.1<br><sub>30,7,14,16,14</sub> | 16.5 · 16.5 | 7.5<br><sub>5,5,5,12,2</sub> | 6.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 2.2<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.6 | 27.9 |
| Kevin Durant | 98% | 36.7<br><sub>37,37,37,30,31</sub> | 27.9<br><sub>30,20,22,22,18</sub> | 24.5 · 23.5 | 6.5<br><sub>6,7,4,9,5</sub> | 5.5 | 5.7<br><sub>3,6,2,3,4</sub> | 3.5 | 2.4<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.2 | 3.5 | 40.1 |
| Fred VanVleet | 98% | 34.2<br><sub>30,32,-,29,29</sub> | 15.7<br><sub>6,14,-,5,24</sub> | 12.5 · 12.5 | 4.0<br><sub>2,3,-,4,6</sub> | 3.5 | 5.8<br><sub>11,5,-,5,5</sub> | 6.5 | 2.5<br><sub>2,3,-,0,4</sub> | 2.5 | 1.6 | 0.4 | 1.5 | 25.4 |
| Tari Eason | 98% | 31.3<br><sub>3,27,31,33,31</sub> | 13.8<br><sub>2,12,19,13,5</sub> | 11.5 · 13.5 | 7.3<br><sub>1,6,3,8,9</sub> | 6.5 | 1.8<br><sub>0,0,0,2,1</sub> | 1.5 | 1.3<br><sub>0,0,0,1,1</sub> | 0.5 | 1.6 | 0.9 | 1.6 | 22.9 |
| Marcus Smart | 52% | 26.5<br><sub>26,21,-,-,-</sub> | 8.9<br><sub>10,5,-,-,-</sub> | – · 8.5 | 2.9<br><sub>2,3,-,-,-</sub> |  | 3.0<br><sub>2,1,-,-,-</sub> |  | 1.2<br><sub>2,0,-,-,-</sub> |  | 1.7 | 0.4 | 1.8 | 14.8 |
| Oscar Tshiebwe | 67% | 19.4<br><sub>-,-,-,-,14</sub> | 8.5<br><sub>-,-,-,-,7</sub> |  | 8.5<br><sub>-,-,-,-,5</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.5 | 1.1 | 18.3 |
| Bogdan Bogdanovic | 88% | 19.2<br><sub>13,9,20,13,15</sub> | 7.6<br><sub>5,3,11,5,16</sub> |  | 2.4<br><sub>1,1,1,2,2</sub> |  | 2.0<br><sub>2,0,1,1,4</sub> |  | 1.1<br><sub>1,1,3,1,4</sub> |  | 0.7 | 0.2 | 0.7 | 12.0 |
| Clint Capela | 83% | 18.5<br><sub>8,-,11,4,22</sub> | 5.5<br><sub>0,-,2,2,10</sub> | 6.5 · 6.5 | 7.1<br><sub>3,-,3,2,8</sub> | 7.5 | 1.2<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.7 | 1.2 | 0.8 | 13.8 |
| Jae'Sean Tate | 84% | 9.5<br><sub>2,-,1,1,4</sub> | 2.7<br><sub>0,-,0,0,0</sub> |  | 2.1<br><sub>0,-,0,1,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.4 |
| Isaiah Crawford | 72% | 8.6<br><sub>3,-,1,1,5</sub> | 2.3<br><sub>3,-,0,0,3</sub> |  | 1.6<br><sub>0,-,0,0,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.3 | 4.5 |
| Bruce Thornton | 80% | 8.3<br><sub>3,-,4,1,3</sub> | 2.0<br><sub>0,-,0,0,5</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.8<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 3.1 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington | 98% | 31.2<br><sub>31,33,36,41,27</sub> | 13.5<br><sub>10,20,12,20,18</sub> | 13.5 · 13.5 | 6.5<br><sub>4,13,4,9,9</sub> | 6.5 | 1.6<br><sub>2,0,2,2,0</sub> |  | 1.5<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.7 | 21.6 |
| Cooper Flagg | 98% | 30.9<br><sub>33,17,-,40,33</sub> | 21.6<br><sub>32,14,-,29,26</sub> | 23.5 · 23.5 | 6.1<br><sub>5,5,-,6,5</sub> | 6.5 | 5.3<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.5 | 33.0 |
| Kyrie Irving | 98% | 30.8<br><sub>24,25,-,33,27</sub> | 20.3<br><sub>15,24,-,18,15</sub> | 18.5 · 19.5 | 3.8<br><sub>4,1,-,6,2</sub> | 3.5 | 3.8<br><sub>2,3,-,6,4</sub> | 3.5 | 2.2<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.1 | 27.9 |
| Zaccharie Risacher | 88% | 27.6<br><sub>27,32,32,30,29</sub> | 9.0<br><sub>4,11,11,6,13</sub> | 8.5 · 8.5 | 5.2<br><sub>6,6,4,8,6</sub> | 4.5 | 1.5<br><sub>2,1,2,1,1</sub> |  | 0.9<br><sub>0,1,1,1,2</sub> |  | 1.1 | 1.3 | 1.2 | 15.7 |
| Naji Marshall | 98% | 26.1<br><sub>29,33,21,-,-</sub> | 13.7<br><sub>16,15,10,-,-</sub> | 11.5 · 11.5 | 3.8<br><sub>2,4,4,-,-</sub> | 3.5 | 3.6<br><sub>6,6,5,-,-</sub> | 3.5 | 0.9<br><sub>2,0,1,-,-</sub> | 0.5 | 1.2 | 0.1 | 1.8 | 21.1 |
| Max Christie | 98% | 25.8<br><sub>29,38,26,26,22</sub> | 9.8<br><sub>5,16,5,11,11</sub> | 8.5 · 9.5 | 2.9<br><sub>3,4,5,5,5</sub> | 3.5 | 1.7<br><sub>2,4,1,3,2</sub> |  | 1.5<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.3 | 1.2 | 14.4 |
| Daniel Gafford | 98% | 22.0<br><sub>22,15,23,26,27</sub> | 8.6<br><sub>2,4,12,8,7</sub> | 7.5 · 7.5 | 6.7<br><sub>3,3,9,9,11</sub> | 6.5 | 1.4<br><sub>1,5,2,3,2</sub> |  | 0.0<br><sub>0,0,0,0,1</sub> |  | 0.8 | 1.4 | 1.1 | 16.6 |
| Marcus Sasser | 91% | 17.5<br><sub>24,27,27,8,22</sub> | 6.3<br><sub>17,6,12,0,10</sub> | 5.5 · – | 1.4<br><sub>1,2,3,1,1</sub> |  | 2.3<br><sub>1,3,5,0,4</sub> |  | 0.9<br><sub>4,2,2,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 10.0 |
| Walter Clayton Jr. | 67% | 13.1<br><sub>-,1,15,17,15</sub> | 4.5<br><sub>-,0,3,15,0</sub> |  | 2.0<br><sub>-,1,2,4,2</sub> |  | 2.8<br><sub>-,0,5,4,5</sub> |  | 0.4<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.3 |
| Morez Johnson Jr. | 98% | 12.9<br><sub>14,17,12,15,18</sub> | 5.2<br><sub>6,8,6,6,10</sub> |  | 1.8<br><sub>3,6,1,2,6</sub> |  | 1.2<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.8 | 8.3 |
| Caleb Martin | 91% | 12.7<br><sub>-,-,-,-,14</sub> | 4.1<br><sub>-,-,-,-,10</sub> |  | 2.1<br><sub>-,-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,2</sub> |  | 0.6 | 0.3 | 0.6 | 7.1 |
| Moussa Cisse | 76% | 7.5<br><sub>3,1,7,-,3</sub> | 2.6<br><sub>3,3,4,-,0</sub> |  | 2.9<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.6 | 0.4 | 5.6 |
| Tobi Lawal | 63% | 6.1<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.0<br><sub>-,0,1,-,0</sub> |  | 0.8<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 3.9 |
| Jett Howard | 63% | 5.9<br><sub>-,-,4,-,3</sub> | 2.5<br><sub>-,-,5,-,0</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.2 | 3.5 |

</details>


### LAC @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Rudy Gobert PTS under 10.5 | LAC @ MIN | tab | 1.87 | 1.83 | 1.60 | 62.3% | 52.2% | 54.8% | +2.4% | +16.5% | 0.7% |
| Brook Lopez PTS under 10.5 | LAC @ MIN | tab | 1.90 | 1.86 | 1.70 | 58.8% | 51.9% | 53.6% | +1.9% | +11.7% | 0.5% |
| LaMelo Ball PTS under 20.5 | LAC @ MIN | draftkings | 1.92 | 1.89 | 1.63 | 61.2% | 50.0% | 52.8% | +1.2% | +17.4% | 0.3% |
| Darius Garland PTS under 22.5 | LAC @ MIN | pointsbetau | 2.00 | 1.98 | 1.80 | 55.4% | 48.9% | 50.5% | +1.1% | +10.8% | 0.3% |
| Jaden McDaniels PTS under 17.5 | LAC @ MIN | draftkings | 1.95 | 1.93 | 1.72 | 58.2% | 49.6% | 51.7% | +1.0% | +13.6% | 0.3% |
| Rui Hachimura PTS under 14.5 | LAC @ MIN | pointsbetau | 1.95 | 1.93 | 1.67 | 60.0% | 48.9% | 51.7% | +1.0% | +17.2% | 0.3% |
| Kris Dunn RA under 8.5 | LAC @ MIN | draftkings | 1.93 | 1.91 | 1.58 | 63.4% | 48.7% | 52.4% | +0.8% | +22.1% | 0.2% |
| Rui Hachimura 3PM under 1.5 | LAC @ MIN | draftkings | 2.36 | 2.34 | 1.93 | 51.9% | 39.6% | 42.7% | +0.7% | +22.5% | 0.1% |
| LaMelo Ball 3PM under 3.5 | LAC @ MIN | draftkings | 1.91 | 1.90 | 1.58 | 63.2% | 48.9% | 52.5% | +0.3% | +20.8% | 0.1% |
| Derrick Jones Jr. PTS under 10.5 | LAC @ MIN | tab | 1.95 | 1.95 | 1.84 | 54.2% | 50.4% | 51.3% | +0.3% | +5.8% | 0.1% |
| LaMelo Ball PR under 25.5 | LAC @ MIN | draftkings | 1.85 | 1.85 | 1.54 | 65.0% | 50.4% | 54.0% | +0.2% | +20.6% | 0.1% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 31.5<br><sub>32,37,36,26</sub> | 22.4<br><sub>30,26,16,14</sub> | 23.5 · 23.5 | 2.5<br><sub>1,0,4,1</sub> | 2.5 | 6.3<br><sub>4,6,11,5</sub> | 7.5 | 2.6<br><sub>3,4,2,1</sub> | 2.5 | 1.2 | 0.2 | 3.4 | 31.3 |
| Rui Hachimura | 98% | 30.4<br><sub>32,33,29,-</sub> | 13.8<br><sub>10,16,5,-</sub> | 14.5 · 14.5 | 4.1<br><sub>8,6,4,-</sub> | 4.5 | 1.1<br><sub>2,1,0,-</sub> | 1.5 | 1.6<br><sub>2,3,1,-</sub> | 1.5 | 0.8 | 0.4 | 1.4 | 19.0 |
| Derrick Jones Jr. | 98% | 28.2<br><sub>26,35,30,28</sub> | 10.7<br><sub>8,16,11,15</sub> | 10.5 · 10.5 | 4.1<br><sub>6,4,6,5</sub> | 4.5 | 1.3<br><sub>5,1,1,0</sub> |  | 1.1<br><sub>1,3,3,3</sub> | 1.5 | 1.1 | 0.8 | 1.0 | 16.1 |
| Kris Dunn | 98% | 27.9<br><sub>27,34,33,27</sub> | 7.2<br><sub>7,7,15,5</sub> | 7.5 · 8.5 | 3.7<br><sub>5,5,4,3</sub> | 3.5 | 3.9<br><sub>7,5,6,3</sub> | 4.5 | 0.8<br><sub>2,1,1,1</sub> | 0.5 | 1.9 | 0.3 | 1.5 | 14.8 |
| Keaton Wagler | 93% | 25.5<br><sub>29,24,26,28</sub> | 13.3<br><sub>15,13,11,21</sub> | 12.5 · 12.5 | 3.2<br><sub>5,3,5,4</sub> | 3.5 | 3.1<br><sub>5,3,4,2</sub> | 2.5 | 1.4<br><sub>3,2,1,3</sub> | 1.5 | 1.0 | 0.3 | 2.3 | 19.6 |
| Brook Lopez | 98% | 22.5<br><sub>27,20,23,22</sub> | 10.1<br><sub>17,22,15,2</sub> | 9.5 · 10.5 | 4.0<br><sub>11,4,1,3</sub> | 4.5 | 1.4<br><sub>1,0,2,3</sub> |  | 1.1<br><sub>1,2,3,0</sub> | 1.5 | 0.6 | 1.1 | 1.0 | 15.5 |
| Kobe Sanders | 96% | 20.8<br><sub>19,19,20,27</sub> | 8.6<br><sub>2,5,12,9</sub> | 7.5 · 7.5 | 2.4<br><sub>0,3,4,4</sub> |  | 1.8<br><sub>3,5,2,0</sub> |  | 1.0<br><sub>0,1,2,1</sub> | 1.5 | 1.0 | 0.2 | 1.2 | 12.8 |
| Isaiah Jackson | 96% | 19.6<br><sub>15,28,24,19</sub> | 8.4<br><sub>13,6,10,4</sub> | 7.5 · 8.5 | 5.8<br><sub>5,6,6,5</sub> | 6.5 | 1.4<br><sub>0,3,4,1</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.9 | 1.0 | 1.4 | 15.5 |
| Gradey Dick | 91% | 16.0<br><sub>19,12,18,19</sub> | 7.0<br><sub>12,6,6,5</sub> |  | 2.6<br><sub>4,4,3,5</sub> |  | 0.8<br><sub>0,0,0,0</sub> |  | 0.7<br><sub>1,0,2,1</sub> |  | 0.6 | 0.1 | 0.9 | 10.4 |
| Baba Miller | 80% | 13.2<br><sub>9,-,2,17</sub> | 5.9<br><sub>4,-,0,4</sub> |  | 2.0<br><sub>3,-,1,7</sub> |  | 1.4<br><sub>1,-,0,1</sub> |  | 0.2<br><sub>0,-,0,0</sub> |  | 0.6 | 0.1 | 0.8 | 9.3 |
| Cam Christie | 58% | 9.6<br><sub>2,-,-,14</sub> | 3.4<br><sub>0,-,-,2</sub> |  | 1.5<br><sub>0,-,-,0</sub> |  | 0.6<br><sub>0,-,-,0</sub> |  | 0.1<br><sub>0,-,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.5 |
| Jalen Pickett | 52% | 7.6<br><sub>2,-,-,8</sub> | 2.8<br><sub>3,-,-,4</sub> |  | 1.0<br><sub>0,-,-,1</sub> |  | 1.0<br><sub>0,-,-,1</sub> |  | 0.2<br><sub>1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Nick Martinelli | 58% | 6.9<br><sub>2,-,-,6</sub> | 3.1<br><sub>0,-,-,2</sub> |  | 1.8<br><sub>1,-,-,3</sub> |  | 0.7<br><sub>1,-,-,1</sub> |  | 0.1<br><sub>0,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.6 |
| Blake Wesley | 30% | 6.6 | 2.7 |  | 0.8 |  | 0.9 |  | 0.1 |  | 0.4 | 0.1 | 0.5 | 4.4 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.5<br><sub>29,30,31,37,35</sub> | 16.9<br><sub>17,15,14,14,19</sub> | 17.5 · 17.5 | 5.7<br><sub>8,6,6,6,7</sub> | 5.5 | 2.9<br><sub>1,3,3,4,4</sub> | 2.5 | 1.4<br><sub>1,2,1,2,1</sub> | 1.5 | 1.1 | 1.0 | 1.8 | 25.5 |
| Jonathan Kuminga | 98% | 31.2<br><sub>30,27,26,36,32</sub> | 14.5<br><sub>12,11,13,10,20</sub> | 14.5 · 14.5 | 5.8<br><sub>1,8,4,10,3</sub> | 5.5 | 2.5<br><sub>3,5,1,1,5</sub> | 2.5 | 1.4<br><sub>2,2,3,0,3</sub> | 1.5 | 1.1 | 0.5 | 1.8 | 22.9 |
| Rudy Gobert | 98% | 30.9<br><sub>33,30,31,36,20</sub> | 9.7<br><sub>5,14,8,5,1</sub> | 10.5 · 10.5 | 10.8<br><sub>15,9,13,20,4</sub> | 11.5 | 1.7<br><sub>1,1,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.2 | 1.5 | 22.2 |
| Ayo Dosunmu | 98% | 30.2<br><sub>29,27,23,26,32</sub> | 15.8<br><sub>16,14,9,9,17</sub> | 16.5 · 15.5 | 4.0<br><sub>5,7,3,1,3</sub> | 4.5 | 4.4<br><sub>3,10,3,0,4</sub> | 4.5 | 1.6<br><sub>1,1,1,1,3</sub> | 1.5 | 1.1 | 0.3 | 1.9 | 24.2 |
| LaMelo Ball | 98% | 28.2<br><sub>29,23,17,31,28</sub> | 19.3<br><sub>21,12,15,11,8</sub> | 20.5 · 20.5 | 3.8<br><sub>2,5,1,0,4</sub> | 4.5 | 6.4<br><sub>6,5,8,6,8</sub> | 7.5 | 3.1<br><sub>5,2,4,1,2</sub> | 3.5 | 1.2 | 0.3 | 3.1 | 29.5 |
| Terrence Shannon Jr. | 96% | 25.8<br><sub>20,22,23,24,27</sub> | 14.6<br><sub>10,13,15,14,19</sub> | 14.5 · 13.5 | 3.1<br><sub>1,4,4,4,6</sub> | 2.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 1.6<br><sub>2,2,3,3,1</sub> | 1.5 | 0.7 | 0.1 | 1.6 | 19.9 |
| Trey Lyles | 97% | 17.7<br><sub>12,17,14,13,22</sub> | 5.1<br><sub>1,9,3,3,7</sub> |  | 3.9<br><sub>1,6,6,1,3</sub> |  | 1.1<br><sub>0,2,2,1,1</sub> |  | 0.7<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.2 | 0.6 | 10.2 |
| Joan Beringer | 91% | 17.0<br><sub>14,15,13,17,20</sub> | 7.8<br><sub>0,9,6,12,7</sub> | 6.5 · 6.5 | 6.1<br><sub>6,9,6,7,9</sub> | 5.5 | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.6 |
| Bones Hyland | 96% | 15.5<br><sub>4,8,15,5,16</sub> | 7.8<br><sub>3,3,3,0,13</sub> |  | 1.8<br><sub>1,1,3,1,1</sub> |  | 2.1<br><sub>0,0,2,2,3</sub> |  | 1.2<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.3 | 1.0 | 11.7 |
| Jaylen Clark | 71% | 9.5<br><sub>3,3,5,-,7</sub> | 3.1<br><sub>1,0,3,-,3</sub> |  | 1.3<br><sub>1,2,1,-,2</sub> |  | 0.6<br><sub>1,1,0,-,1</sub> |  | 0.3<br><sub>0,0,0,-,1</sub> |  | 0.5 | 0.1 | 0.3 | 5.0 |
| Zyon Pullin | 52% | 8.3<br><sub>-,-,5,-,-</sub> | 2.9<br><sub>-,-,2,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.6 | 5.2 |
| Rocco Zikarsky | 23% | 7.1 | 2.4 |  | 2.2 |  | 0.4 |  | 0.0 |  | 0.2 | 0.6 | 0.3 | 5.0 |
| Enrique Freeman | 16% | 6.4 | 1.9 |  | 1.4 |  | 0.3 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.6 |
| Cody Williams | 52% | 6.4<br><sub>3,3,5,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 1.0 |
| Isaiah Evans | 52% | 6.1<br><sub>2,2,4,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 1.0<br><sub>1,0,0,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.0 |

</details>


### LAL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Ziaire Williams (LAL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Sandro Mamukelashvili REB over 4.5 (5+) | LAL @ GSW | draftkings | 2.10 | 2.08 | 1.69 | 59.2% | 44.5% | 48.2% | +1.2% | +24.4% | 0.3% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.7–114.0 | LAL 52% | 1.91 / 2.10 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| Expected (weighted by chance each plays) | 114.5–114.5 | LAL 50% | 1.99 / 2.01 | GSW +0.5 | 228.5 | GSW +3.5 covers 59%; o234.5 38% |
| if Gui Santos plays | 114.4–115.0 | LAL 49% | 2.04 / 1.96 | GSW +0.5 | 229.5 | GSW +3.5 covers 60%; o234.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 23.4 | 9.2 | 4.2 | 2.2 | 1.1 | 1.0 | 0.3 | 1.5 | 15.6 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.5<br><sub>30,37,38,37,-</sub> | 34.4<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 6.5 | 8.0<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.5 |
| Austin Reaves | 98% | 35.5<br><sub>32,38,36,39,31</sub> | 21.4<br><sub>23,28,29,26,16</sub> |  | 4.1<br><sub>4,2,1,4,6</sub> | 4.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 31.1 |
| Walker Kessler | 98% | 29.8<br><sub>30,35,28,33,26</sub> | 11.2<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.8<br><sub>9,8,7,8,9</sub> | 9.5 | 1.5<br><sub>1,3,0,0,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.6 |
| Quentin Grimes | 98% | 27.2<br><sub>27,31,20,19,38</sub> | 10.0<br><sub>10,13,3,2,23</sub> | 8.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 3.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.7 |
| Sandro Mamukelashvili | 98% | 24.9<br><sub>22,24,21,24,30</sub> | 9.8<br><sub>5,7,9,17,13</sub> | 9.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> | 0.5 | 1.0 | 0.5 | 1.0 | 17.0 |
| Jake LaRavia | 91% | 23.9<br><sub>18,-,15,19,35</sub> | 5.8<br><sub>10,-,0,5,2</sub> |  | 3.8<br><sub>2,-,4,1,10</sub> |  | 1.4<br><sub>2,-,1,1,0</sub> |  | 0.5<br><sub>2,-,0,1,0</sub> |  | 1.4 | 0.6 | 1.2 | 11.0 |
| Matisse Thybulle | 96% | 23.2<br><sub>23,24,26,22,28</sub> | 6.4<br><sub>3,13,11,5,15</sub> | 6.5 · – | 2.2<br><sub>3,1,1,2,1</sub> | 2.5 | 1.2<br><sub>1,2,1,1,0</sub> |  | 1.1<br><sub>1,3,3,1,4</sub> | 1.5 | 2.0 | 0.7 | 1.0 | 9.9 |
| Collin Sexton | 98% | 19.2<br><sub>-,16,20,14,21</sub> | 11.5<br><sub>-,5,13,9,21</sub> |  | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> |  | 1.3<br><sub>-,1,1,0,4</sub> |  | 1.1 | 0.1 | 1.8 | 15.6 |
| Jarred Vanderbilt | 48% | 16.7<br><sub>-,-,-,-,21</sub> | 4.3<br><sub>-,-,-,-,0</sub> |  | 4.3<br><sub>-,-,-,-,7</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 9.9 |
| Lawson Lovering | 23% | 13.9 | 4.2 |  | 3.4 |  | 1.0 |  | 0.1 |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Jaden Hardy | 52% | 9.3<br><sub>7,-,-,-,9</sub> | 4.4<br><sub>3,-,-,-,2</sub> |  | 0.8<br><sub>2,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 5.9 |
| Arthur Kaluma | 23% | 8.7<br><sub>-,-,-,-,-</sub> | 3.7<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 6.1 |
| AK Okereke | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Kevon Looney | 64% | 8.1<br><sub>15,5,5,5,-</sub> | 2.0<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.3 |
| Bronny James | 26% | 6.2<br><sub>7,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 2.7 |
| Chris Manon | 52% | 5.8<br><sub>6,-,-,-,-</sub> | 1.6<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 96% | 34.6<br><sub>29,37,36,31,35</sub> | 20.9<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.3<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.1 | 33.1 |
| Brandin Podziemski | 80% | 31.7<br><sub>-,33,-,33,32</sub> | 15.0<br><sub>-,18,-,18,8</sub> | 14.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 5.5 | 4.1<br><sub>-,3,-,5,6</sub> | 3.5 | 1.9<br><sub>-,2,-,3,0</sub> | 1.5 | 1.2 | 0.2 | 1.9 | 23.9 |
| Stephen Curry | 98% | 31.1<br><sub>21,30,-,27,32</sub> | 24.3<br><sub>23,24,-,24,44</sub> | 24.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.7<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 3.0 | 32.5 |
| Draymond Green | 83% | 28.7<br><sub>21,31,-,27,32</sub> | 8.1<br><sub>2,5,-,3,3</sub> | 5.5 · – | 5.2<br><sub>4,5,-,4,9</sub> | 5.5 | 6.0<br><sub>8,6,-,7,6</sub> | 5.5 | 1.0<br><sub>0,1,-,1,0</sub> | 0.5 | 1.2 | 0.6 | 2.5 | 19.3 |
| De'Anthony Melton | 98% | 21.6<br><sub>21,20,27,19,20</sub> | 9.3<br><sub>0,10,25,3,8</sub> | 9.5 · – | 3.0<br><sub>2,1,5,4,6</sub> | 2.5 | 2.3<br><sub>2,0,5,3,0</sub> | 1.5 | 1.3<br><sub>0,2,4,1,2</sub> | 1.5 | 1.4 | 0.3 | 1.5 | 14.6 |
| Georges Niang | 93% | 20.0<br><sub>20,13,23,18,23</sub> | 7.9<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.5<br><sub>2,3,4,2,3</sub> |  | 1.1<br><sub>2,0,2,0,2</sub> |  | 1.3<br><sub>0,0,0,3,1</sub> | 1.5 | 0.6 | 0.1 | 1.0 | 11.6 |
| Al Horford | 98% | 19.4<br><sub>17,19,-,19,18</sub> | 6.0<br><sub>0,3,-,11,4</sub> | 5.5 · – | 4.2<br><sub>4,5,-,3,5</sub> | 3.5 | 1.6<br><sub>2,0,-,0,2</sub> |  | 0.9<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.7 | 0.7 | 11.7 |
| Will Richard | 98% | 16.8<br><sub>20,3,31,3,23</sub> | 4.7<br><sub>8,0,11,0,6</sub> |  | 1.9<br><sub>5,0,0,0,3</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>0,0,3,0,0</sub> |  | 1.1 | 0.1 | 0.6 | 7.5 |
| Brandon Williams | 98% | 16.5<br><sub>18,9,24,15,14</sub> | 9.4<br><sub>14,4,20,6,11</sub> |  | 2.2<br><sub>4,2,3,3,3</sub> |  | 2.9<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.2 | 1.5 | 14.5 |
| Gary Payton II | 98% | 14.2<br><sub>18,11,17,12,10</sub> | 6.5<br><sub>10,7,2,7,2</sub> |  | 2.7<br><sub>1,2,1,2,2</sub> |  | 1.1<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 10.2 |
| Graham Ike | 67% | 12.5<br><sub>12,12,26,3,-</sub> | 6.0<br><sub>8,10,12,3,-</sub> |  | 2.8<br><sub>2,2,10,0,-</sub> |  | 1.0<br><sub>1,1,2,1,-</sub> |  | 0.3<br><sub>1,2,0,1,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.8 |
| Charles Bassey | 91% | 9.3<br><sub>-,-,13,2,2</sub> | 3.9<br><sub>-,-,10,0,0</sub> |  | 3.4<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 7.7 |
| LJ Cryer | 63% | 8.2<br><sub>9,-,14,3,-</sub> | 3.5<br><sub>9,-,3,6,-</sub> |  | 0.8<br><sub>1,-,1,0,-</sub> |  | 0.7<br><sub>3,-,1,2,-</sub> |  | 0.5<br><sub>2,-,1,2,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.0 |
| Malevy Leons | 58% | 8.0<br><sub>9,-,4,3,-</sub> | 2.4<br><sub>0,-,2,0,-</sub> |  | 1.4<br><sub>1,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 4.4 |

</details>

<details><summary>if Gui Santos plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | 96% | 34.0<br><sub>29,37,36,31,35</sub> | 21.1<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.1<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.0 | 33.1 |
| Brandin Podziemski (GSW) | 80% | 30.3<br><sub>-,33,-,33,32</sub> | 14.3<br><sub>-,18,-,18,8</sub> | 14.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 5.5 | 3.8<br><sub>-,3,-,5,6</sub> | 3.5 | 1.8<br><sub>-,2,-,3,0</sub> | 1.5 | 1.2 | 0.2 | 1.8 | 22.9 |
| Stephen Curry (GSW) | 98% | 30.0<br><sub>21,30,-,27,32</sub> | 23.6<br><sub>23,24,-,24,44</sub> | 24.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.4<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 2.9 | 31.5 |
| Draymond Green (GSW) | 83% | 26.4<br><sub>21,31,-,27,32</sub> | 7.3<br><sub>2,5,-,3,3</sub> | 5.5 · – | 4.9<br><sub>4,5,-,4,9</sub> | 5.5 | 5.5<br><sub>8,6,-,7,6</sub> | 5.5 | 0.9<br><sub>0,1,-,1,0</sub> | 0.5 | 1.1 | 0.6 | 2.4 | 17.7 |
| Gui Santos (GSW) | 100% | 23.4<br><sub>25,20,23,28,-</sub> | 9.2<br><sub>12,5,7,13,-</sub> |  | 4.2<br><sub>5,4,4,3,-</sub> |  | 2.2<br><sub>0,2,3,1,-</sub> |  | 1.1<br><sub>1,1,1,1,-</sub> |  | 1.0 | 0.3 | 1.5 | 15.6 |
| De'Anthony Melton (GSW) | 98% | 19.6<br><sub>21,20,27,19,20</sub> | 8.4<br><sub>0,10,25,3,8</sub> | 9.5 · – | 2.8<br><sub>2,1,5,4,6</sub> | 2.5 | 2.0<br><sub>2,0,5,3,0</sub> | 1.5 | 1.1<br><sub>0,2,4,1,2</sub> | 1.5 | 1.3 | 0.3 | 1.3 | 13.3 |
| Al Horford (GSW) | 98% | 17.5<br><sub>17,19,-,19,18</sub> | 5.3<br><sub>0,3,-,11,4</sub> | 5.5 · – | 3.8<br><sub>4,5,-,3,5</sub> | 3.5 | 1.4<br><sub>2,0,-,0,2</sub> |  | 0.8<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.6 | 0.6 | 10.5 |
| Georges Niang (GSW) | 93% | 17.2<br><sub>20,13,23,18,23</sub> | 7.0<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.3<br><sub>2,3,4,2,3</sub> |  | 0.9<br><sub>2,0,2,0,2</sub> |  | 1.1<br><sub>0,0,0,3,1</sub> | 1.5 | 0.5 | 0.1 | 0.9 | 10.3 |
| Brandon Williams (GSW) | 98% | 15.3<br><sub>18,9,24,15,14</sub> | 8.8<br><sub>14,4,20,6,11</sub> |  | 2.1<br><sub>4,2,3,3,3</sub> |  | 2.6<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.2 | 1.4 | 13.5 |
| Will Richard (GSW) | 98% | 14.7<br><sub>20,3,31,3,23</sub> | 4.2<br><sub>8,0,11,0,6</sub> |  | 1.7<br><sub>5,0,0,0,3</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4<br><sub>0,0,3,0,0</sub> |  | 0.9 | 0.1 | 0.5 | 6.7 |
| Gary Payton II (GSW) | 98% | 12.6<br><sub>18,11,17,12,10</sub> | 6.1<br><sub>10,7,2,7,2</sub> |  | 2.4<br><sub>1,2,1,2,2</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.6 | 9.5 |
| Graham Ike (GSW) | 67% | 8.7<br><sub>12,12,26,3,-</sub> | 4.1<br><sub>8,10,12,3,-</sub> |  | 2.0<br><sub>2,2,10,0,-</sub> |  | 0.8<br><sub>1,1,2,1,-</sub> |  | 0.2<br><sub>1,2,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.9 |
| Charles Bassey (GSW) | 91% | 7.8<br><sub>-,-,13,2,2</sub> | 3.3<br><sub>-,-,10,0,0</sub> |  | 3.0<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 6.6 |
| LJ Cryer (GSW) | 63% | 6.7<br><sub>9,-,14,3,-</sub> | 3.0<br><sub>9,-,3,6,-</sub> |  | 0.7<br><sub>1,-,1,0,-</sub> |  | 0.6<br><sub>3,-,1,2,-</sub> |  | 0.3<br><sub>2,-,1,2,-</sub> |  | 0.1 | 0.0 | 0.4 | 4.3 |
| Malevy Leons (GSW) | 58% | 6.1<br><sub>9,-,4,3,-</sub> | 2.0<br><sub>0,-,2,0,-</sub> |  | 1.1<br><sub>1,-,0,1,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.6 |
| Luka Doncic (LAL) | 98% | 36.5<br><sub>30,37,38,37,-</sub> | 34.3<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 6.5 | 8.0<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.4 |
| Austin Reaves (LAL) | 98% | 35.5<br><sub>32,38,36,39,31</sub> | 21.3<br><sub>23,28,29,26,16</sub> |  | 4.1<br><sub>4,2,1,4,6</sub> | 4.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 31.0 |
| Walker Kessler (LAL) | 98% | 29.7<br><sub>30,35,28,33,26</sub> | 11.3<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.9<br><sub>9,8,7,8,9</sub> | 9.5 | 1.5<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.7 |
| Quentin Grimes (LAL) | 98% | 27.2<br><sub>27,31,20,19,38</sub> | 9.9<br><sub>10,13,3,2,23</sub> | 8.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 3.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.6 |
| Sandro Mamukelashvili (LAL) | 98% | 24.8<br><sub>22,24,21,24,30</sub> | 9.7<br><sub>5,7,9,17,13</sub> | 9.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> | 0.5 | 1.0 | 0.5 | 1.0 | 16.9 |
| Jake LaRavia (LAL) | 91% | 23.9<br><sub>18,-,15,19,35</sub> | 5.8<br><sub>10,-,0,5,2</sub> |  | 3.8<br><sub>2,-,4,1,10</sub> |  | 1.4<br><sub>2,-,1,1,0</sub> |  | 0.5<br><sub>2,-,0,1,0</sub> |  | 1.4 | 0.6 | 1.2 | 11.0 |
| Matisse Thybulle (LAL) | 96% | 23.2<br><sub>23,24,26,22,28</sub> | 6.5<br><sub>3,13,11,5,15</sub> | 6.5 · – | 2.2<br><sub>3,1,1,2,1</sub> | 2.5 | 1.2<br><sub>1,2,1,1,0</sub> |  | 1.1<br><sub>1,3,3,1,4</sub> | 1.5 | 2.0 | 0.7 | 1.0 | 9.9 |
| Collin Sexton (LAL) | 98% | 19.3<br><sub>-,16,20,14,21</sub> | 11.6<br><sub>-,5,13,9,21</sub> |  | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> |  | 1.3<br><sub>-,1,1,0,4</sub> |  | 1.1 | 0.1 | 1.8 | 15.8 |
| Jarred Vanderbilt (LAL) | 48% | 16.5<br><sub>-,-,-,-,21</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 4.2<br><sub>-,-,-,-,7</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.2 | 0.8 | 9.7 |
| Lawson Lovering (LAL) | 23% | 13.9 | 4.2 |  | 3.4 |  | 1.0 |  | 0.1 |  | 0.7 | 0.3 | 0.6 | 8.5 |
| Jaden Hardy (LAL) | 52% | 9.2<br><sub>7,-,-,-,9</sub> | 4.4<br><sub>3,-,-,-,2</sub> |  | 0.8<br><sub>2,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 5.8 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.7<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| AK Okereke (LAL) | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Kevon Looney (LAL) | 64% | 8.1<br><sub>15,5,5,5,-</sub> | 2.0<br><sub>6,0,2,0,-</sub> |  | 2.7<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.3 |
| Bronny James (LAL) | 26% | 6.4<br><sub>7,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 2.8 |
| Chris Manon (LAL) | 52% | 5.9<br><sub>6,-,-,-,-</sub> | 1.7<br><sub>2,-,-,-,-</sub> |  | 1.2<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.2 |

</details>


### DEN @ PHX
Out: Drew Timme (PHX), Mark Williams (PHX), Julian Strawther (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +4.5 covers 56%; o231.5 43% |
| Expected (weighted by chance each plays) | 115.6–113.6 | DEN 55% | 1.82 / 2.22 | PHX +2.5 | 229.5 | PHX +4.5 covers 58%; o231.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alpha Diallo (DEN) | Doubtful | 20% | 14.3 | 3.7 | 1.8 | 1.1 | 0.3 | 0.7 | 0.3 | 0.9 | 6.6 | small |
| Oso Ighodaro (PHX) | Questionable | 55% | 17.0 | 5.4 | 4.4 | 2.1 | 0.0 | 0.6 | 0.6 | 0.8 | 11.8 | small |
| Cameron Johnson (DEN) | Questionable | 55% | 20.1 | 8.2 | 2.8 | 1.6 | 1.1 | 0.6 | 0.3 | 0.8 | 12.6 | small |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 37.6<br><sub>37,43,36,38</sub> | 24.0<br><sub>6,42,19,23</sub> | 22.5 · – | 4.4<br><sub>10,3,6,1</sub> | 4.5 | 6.1<br><sub>3,6,8,6</sub> | 6.5 | 3.3<br><sub>0,8,3,5</sub> | 2.5 | 1.1 | 0.5 | 2.6 | 34.5 |
| Nikola Jokic | 98% | 37.0<br><sub>35,44,35,34</sub> | 25.7<br><sub>13,35,19,21</sub> | 25.5 · – | 12.8<br><sub>7,15,7,13</sub> | 12.5 | 10.1<br><sub>5,10,11,10</sub> | 9.5 | 1.6<br><sub>1,3,1,0</sub> | 1.5 | 1.6 | 1.0 | 4.0 | 48.6 |
| Christian Braun | 98% | 34.7<br><sub>33,40,34,36</sub> | 12.3<br><sub>7,15,9,15</sub> | 11.5 · – | 4.7<br><sub>6,8,4,0</sub> | 4.5 | 2.5<br><sub>1,2,2,4</sub> |  | 1.2<br><sub>1,0,1,3</sub> | 1.5 | 1.1 | 0.4 | 1.3 | 19.5 |
| Aaron Gordon | 98% | 31.3<br><sub>29,37,25,31</sub> | 14.2<br><sub>20,7,7,15</sub> | 14.5 · – | 6.1<br><sub>6,5,4,11</sub> | 5.5 | 2.7<br><sub>1,4,2,3</sub> | 2.5 | 1.5<br><sub>3,1,0,2</sub> | 1.5 | 0.8 | 0.3 | 1.5 | 23.1 |
| DeMar DeRozan | 98% | 28.2<br><sub>28,24,29,26</sub> | 15.0<br><sub>13,12,21,6</sub> | 13.5 · – | 2.7<br><sub>2,3,4,2</sub> | 2.5 | 3.5<br><sub>0,3,2,5</sub> | 2.5 | 0.6<br><sub>0,0,2,0</sub> | 0.5 | 0.9 | 0.3 | 1.8 | 21.2 |
| Trevon Brazile | 93% | 25.9<br><sub>18,28,17,32</sub> | 8.7<br><sub>4,17,6,11</sub> | 7.5 · – | 6.3<br><sub>12,9,1,8</sub> | 5.5 | 1.1<br><sub>0,0,0,0</sub> |  | 1.1<br><sub>0,3,1,1</sub> |  | 0.8 | 0.5 | 1.3 | 16.1 |
| Marvin Bagley III | 98% | 16.3<br><sub>11,9,11,19</sub> | 7.1<br><sub>2,5,7,8</sub> |  | 4.8<br><sub>3,4,2,5</sub> |  | 0.8<br><sub>1,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0</sub> |  | 0.5 | 0.6 | 0.8 | 12.7 |
| Bryce Hopkins | 93% | 16.1<br><sub>2,19,31,14</sub> | 3.8<br><sub>0,2,13,0</sub> |  | 2.2<br><sub>1,2,3,2</sub> |  | 0.8<br><sub>0,1,1,0</sub> |  | 0.3<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 6.8 |
| Tyus Jones | 88% | 11.7<br><sub>10,10,9,11</sub> | 3.1<br><sub>2,2,0,5</sub> |  | 1.1<br><sub>0,0,0,0</sub> |  | 1.5<br><sub>0,0,2,1</sub> |  | 0.3<br><sub>0,0,0,1</sub> |  | 0.6 | 0.1 | 0.5 | 5.7 |
| Cam Whitmore | 58% | 8.9<br><sub>-,11,4,-</sub> | 4.2<br><sub>-,4,4,-</sub> |  | 1.6<br><sub>-,2,0,-</sub> |  | 0.5<br><sub>-,0,1,-</sub> |  | 0.3<br><sub>-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 6.3 |
| Zeke Nnaji | 47% | 8.5<br><sub>-,-,4,-</sub> | 2.8<br><sub>-,-,5,-</sub> |  | 1.8<br><sub>-,-,1,-</sub> |  | 0.4<br><sub>-,-,0,-</sub> |  | 0.1<br><sub>-,-,1,-</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Ryan Nembhard | 52% | 6.7<br><sub>2,-,4,-</sub> | 4.1<br><sub>5,-,4,-</sub> |  | 0.9<br><sub>1,-,0,-</sub> |  | 0.7<br><sub>1,-,1,-</sub> |  | 0.2<br><sub>1,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.7 |
| DaRon Holmes II | 52% | 6.6<br><sub>2,-,4,-</sub> | 2.7<br><sub>3,-,0,-</sub> |  | 1.3<br><sub>1,-,0,-</sub> |  | 0.4<br><sub>1,-,1,-</sub> |  | 0.3<br><sub>1,-,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.4 |

</details>

<details><summary>PHX players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Devin Booker | 98% | 34.0<br><sub>29,36,34</sub> | 23.2<br><sub>23,43,3</sub> | 23.5 · – | 4.1<br><sub>4,7,2</sub> | 4.5 | 6.0<br><sub>2,7,7</sub> | 5.5 | 1.8<br><sub>0,2,0</sub> | 1.5 | 0.9 | 0.3 | 2.8 | 33.3 |
| Dillon Brooks | 98% | 32.3<br><sub>27,34,33</sub> | 19.1<br><sub>10,15,19</sub> | 16.5 · – | 4.4<br><sub>4,2,5</sub> | 3.5 | 2.2<br><sub>0,5,5</sub> |  | 2.2<br><sub>1,1,3</sub> | 1.5 | 1.0 | 0.2 | 1.4 | 25.8 |
| Miles Bridges | 98% | 30.9<br><sub>29,33,32</sub> | 15.3<br><sub>8,16,17</sub> | 15.5 · – | 6.2<br><sub>4,7,8</sub> | 5.5 | 2.8<br><sub>0,3,4</sub> | 2.5 | 1.6<br><sub>0,2,2</sub> | 1.5 | 0.8 | 0.4 | 1.2 | 24.4 |
| Jalen Green | 96% | 29.5<br><sub>25,26,31</sub> | 16.0<br><sub>10,12,20</sub> | 15.5 · – | 4.2<br><sub>2,2,4</sub> | 3.5 | 3.1<br><sub>3,1,4</sub> | 3.5 | 2.0<br><sub>2,1,1</sub> | 2.5 | 1.0 | 0.3 | 1.9 | 23.4 |
| Collin Gillespie | 98% | 24.9<br><sub>21,28,23</sub> | 9.5<br><sub>0,11,9</sub> | 9.5 · – | 3.5<br><sub>1,4,1</sub> | 3.5 | 3.8<br><sub>2,9,2</sub> | 3.5 | 1.7<br><sub>0,2,3</sub> | 2.5 | 1.1 | 0.2 | 1.2 | 16.8 |
| Khaman Maluach | 96% | 20.4<br><sub>17,28,26</sub> | 6.3<br><sub>2,9,12</sub> | 8.5 · – | 6.3<br><sub>6,9,7</sub> | 8.5 | 0.7<br><sub>1,3,1</sub> |  | 0.3<br><sub>0,1,0</sub> |  | 0.4 | 1.1 | 1.1 | 13.4 |
| Jordan Goodwin | 98% | 18.0<br><sub>22,20,17</sub> | 6.8<br><sub>3,9,12</sub> | 6.5 · – | 3.8<br><sub>4,2,4</sub> | 3.5 | 1.6<br><sub>0,4,2</sub> | 1.5 | 1.0<br><sub>1,1,4</sub> | 1.5 | 1.1 | 0.2 | 0.7 | 12.2 |
| Luke Kennard | 97% | 17.4<br><sub>-,18,16</sub> | 6.5<br><sub>-,11,9</sub> |  | 2.2<br><sub>-,4,1</sub> |  | 1.6<br><sub>-,1,2</sub> |  | 0.8<br><sub>-,3,3</sub> |  | 0.6 | 0.1 | 0.6 | 10.3 |
| Ryan Dunn | 93% | 14.3<br><sub>14,13,14</sub> | 4.5<br><sub>3,5,6</sub> |  | 3.2<br><sub>2,5,2</sub> |  | 0.9<br><sub>0,0,1</sub> |  | 0.4<br><sub>0,1,1</sub> |  | 0.6 | 0.3 | 0.4 | 8.7 |
| Pat Spencer | 64% | 8.5<br><sub>7,-,-</sub> | 2.9<br><sub>3,-,-</sub> |  | 1.1<br><sub>3,-,-</sub> |  | 1.4<br><sub>1,-,-</sub> |  | 0.2<br><sub>1,-,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.4 |
| Rasheer Fleming | 67% | 7.9<br><sub>12,-,3</sub> | 2.9<br><sub>1,-,0</sub> |  | 1.5<br><sub>2,-,1</sub> |  | 0.3<br><sub>0,-,0</sub> |  | 0.3<br><sub>0,-,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.7 |
| Duop Reath | 88% | 7.7<br><sub>9,3,7</sub> | 2.8<br><sub>5,0,5</sub> |  | 1.6<br><sub>1,0,3</sub> |  | 0.4<br><sub>0,0,0</sub> |  | 0.3<br><sub>1,0,1</sub> |  | 0.2 | 0.2 | 0.3 | 4.7 |
| Jamaree Bouyea | 67% | 6.5<br><sub>7,-,3</sub> | 2.6<br><sub>3,-,2</sub> |  | 0.9<br><sub>2,-,0</sub> |  | 1.0<br><sub>2,-,1</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.3 | 0.1 | 0.4 | 4.5 |
| Koa Peat | 64% | 6.5<br><sub>7,-,3</sub> | 2.4<br><sub>4,-,0</sub> |  | 1.5<br><sub>1,-,0</sub> |  | 0.4<br><sub>0,-,0</sub> |  | 0.1<br><sub>0,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 4.3 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-10-30/`._
