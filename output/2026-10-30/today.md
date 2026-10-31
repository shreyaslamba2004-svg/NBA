# NBA model · Fri 30 Oct 2026 (US date)

Updated **Sat 31 Oct, 11:04 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-30/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Clint Capela REB over 13.5 (14+) | HOU @ DAL | draftkings | 16.40 | 11.52 | 5.67 | 17.6% | 5.7% | 8.7% | +42.4% | +189.1% | 0.7% |
| Clint Capela REB over 15.5 (16+) | HOU @ DAL | draftkings | 29.00 | 21.32 | 11.00 | 9.1% | 3.2% | 4.7% | +36.0% | +163.8% | 0.3% |
| Kevin Durant PRA over 54.5 (55+) | HOU @ DAL | draftkings | 21.00 | 16.39 | 9.06 | 11.0% | 4.5% | 6.1% | +28.0% | +131.7% | 0.4% |
| Quenton Jackson PA over 19.5 (20+) | IND @ MIA | draftkings | 12.00 | 9.43 | 5.25 | 19.1% | 7.8% | 10.6% | +27.3% | +128.7% | 0.6% |
| Kevin Durant PA over 49.5 (50+) | HOU @ DAL | draftkings | 27.00 | 21.46 | 12.09 | 8.3% | 3.5% | 4.7% | +25.9% | +123.3% | 0.2% |
| Quenton Jackson AST over 7.5 (8+) | IND @ MIA | draftkings | 17.60 | 14.12 | 8.07 | 12.4% | 5.3% | 7.1% | +24.6% | +118.2% | 0.4% |
| Kevin Durant PRA over 49.5 (50+) | HOU @ DAL | draftkings | 11.20 | 9.10 | 5.28 | 18.9% | 8.3% | 11.0% | +23.1% | +112.1% | 0.6% |
| Pascal Siakam PTS over 44.5 (45+) | IND @ MIA | draftkings | 27.00 | 22.27 | 13.17 | 7.6% | 3.5% | 4.5% | +21.4% | +105.1% | 0.2% |
| Pascal Siakam PA over 44.5 (45+) | IND @ MIA | draftkings | 13.20 | 11.00 | 6.61 | 15.1% | 7.1% | 9.1% | +20.0% | +99.8% | 0.4% |
| Pascal Siakam PA over 49.5 (50+) | IND @ MIA | draftkings | 24.00 | 20.04 | 12.06 | 8.3% | 3.9% | 5.0% | +19.8% | +99.0% | 0.2% |
| Kevin Durant PR over 49.5 (50+) | HOU @ DAL | draftkings | 20.80 | 17.67 | 10.93 | 9.2% | 4.5% | 5.7% | +17.7% | +90.3% | 0.2% |
| Pascal Siakam PTS over 39.5 (40+) | IND @ MIA | draftkings | 13.20 | 11.27 | 7.02 | 14.2% | 7.1% | 8.9% | +17.1% | +88.1% | 0.4% |
| Kevin Durant PTS over 44.5 (45+) | HOU @ DAL | draftkings | 28.00 | 24.21 | 15.38 | 6.5% | 3.3% | 4.1% | +15.6% | +82.0% | 0.1% |
| Quenton Jackson PR over 19.5 (20+) | IND @ MIA | draftkings | 13.80 | 12.02 | 7.72 | 13.0% | 6.8% | 8.3% | +14.8% | +78.7% | 0.3% |
| Kevin Durant PTS over 39.5 (40+) | HOU @ DAL | draftkings | 14.00 | 12.29 | 7.99 | 12.5% | 6.7% | 8.1% | +13.9% | +75.3% | 0.3% |
| Kevin Durant PRA over 44.5 (45+) | HOU @ DAL | draftkings | 5.84 | 5.13 | 3.34 | 29.9% | 16.0% | 19.5% | +13.8% | +74.8% | 0.7% |
| Quenton Jackson PA over 24.5 (25+) | IND @ MIA | draftkings | 26.00 | 22.94 | 15.03 | 6.7% | 3.6% | 4.4% | +13.3% | +73.0% | 0.1% |
| Kevin Durant PR over 44.5 (45+) | HOU @ DAL | draftkings | 10.30 | 9.23 | 6.19 | 16.2% | 9.1% | 10.8% | +11.7% | +66.3% | 0.3% |
| Pascal Siakam AST over 7.5 (8+) | IND @ MIA | draftkings | 11.20 | 10.03 | 6.74 | 14.8% | 8.3% | 10.0% | +11.7% | +66.3% | 0.3% |
| Zaccharie Risacher REB over 7.5 (8+) | HOU @ DAL | draftkings | 9.10 | 8.24 | 5.63 | 17.8% | 10.3% | 12.1% | +10.5% | +61.5% | 0.3% |
| Quenton Jackson PRA over 29.5 (30+) | IND @ MIA | draftkings | 27.00 | 24.57 | 16.94 | 5.9% | 3.5% | 4.1% | +9.9% | +59.4% | 0.1% |
| Pascal Siakam PA over 39.5 (40+) | IND @ MIA | draftkings | 6.31 | 5.74 | 3.96 | 25.2% | 14.8% | 17.4% | +9.9% | +59.3% | 0.5% |
| Bam Adebayo REB over 15.5 (16+) | IND @ MIA | draftkings | 13.80 | 12.59 | 8.73 | 11.5% | 6.8% | 7.9% | +9.6% | +58.1% | 0.2% |
| Pascal Siakam PTS over 34.5 (35+) | IND @ MIA | draftkings | 6.21 | 5.74 | 4.07 | 24.5% | 15.0% | 17.4% | +8.2% | +52.4% | 0.4% |
| Clint Capela PR over 24.5 (25+) | HOU @ DAL | draftkings | 10.80 | 9.99 | 7.10 | 14.1% | 8.6% | 10.0% | +8.1% | +52.2% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 8.5 (9+) | HOU @ DAL | draftkings | 22.00 | 14.84 | 7.02 | 14.2% | 4.2% | 6.7% | +48.4% | +213.2% | 0.6% |
| Clint Capela REB over 14.5 (15+) | HOU @ DAL | draftkings | 22.00 | 15.65 | 7.81 | 12.8% | 4.2% | 6.4% | +40.5% | +181.7% | 0.5% |
| Quenton Jackson AST over 6.5 (7+) | IND @ MIA | draftkings | 10.80 | 8.64 | 4.92 | 20.3% | 8.6% | 11.6% | +25.0% | +119.5% | 0.6% |
| Quenton Jackson AST over 8.5 (9+) | IND @ MIA | draftkings | 27.00 | 22.42 | 13.41 | 7.5% | 3.5% | 4.5% | +20.4% | +101.3% | 0.2% |
| Jay Huff AST over 4.5 (5+) | IND @ MIA | draftkings | 27.00 | 23.36 | 14.83 | 6.7% | 3.5% | 4.3% | +15.6% | +82.1% | 0.1% |
| Zaccharie Risacher REB over 8.5 (9+) | HOU @ DAL | draftkings | 15.20 | 13.53 | 8.98 | 11.1% | 6.2% | 7.4% | +12.4% | +69.2% | 0.2% |
| Pascal Siakam AST over 8.5 (9+) | IND @ MIA | draftkings | 19.00 | 17.21 | 11.79 | 8.5% | 4.9% | 5.8% | +10.4% | +61.1% | 0.1% |
| Bam Adebayo REB over 14.5 (15+) | IND @ MIA | draftkings | 9.70 | 8.86 | 6.15 | 16.3% | 9.6% | 11.3% | +9.5% | +57.7% | 0.3% |
| Jabari Smith Jr. REB over 10.5 (11+) | HOU @ DAL | draftkings | 9.60 | 8.87 | 6.29 | 15.9% | 9.7% | 11.3% | +8.2% | +52.6% | 0.2% |
| Bam Adebayo REB over 16.5 (17+) | IND @ MIA | draftkings | 19.40 | 17.92 | 12.73 | 7.9% | 4.8% | 5.6% | +8.2% | +52.4% | 0.1% |
| Pascal Siakam AST over 6.5 (7+) | IND @ MIA | draftkings | 6.29 | 5.82 | 4.14 | 24.1% | 14.9% | 17.2% | +8.1% | +51.8% | 0.4% |
| Zaccharie Risacher REB over 6.5 (7+) | HOU @ DAL | draftkings | 5.36 | 5.00 | 3.60 | 27.8% | 17.4% | 20.0% | +7.3% | +48.8% | 0.4% |
| Andrew Nembhard AST over 14.5 (15+) | IND @ MIA | draftkings | 13.20 | 12.35 | 8.96 | 11.2% | 7.1% | 8.1% | +6.9% | +47.3% | 0.1% |
| Bam Adebayo REB over 12.5 (13+) | IND @ MIA | draftkings | 4.85 | 4.56 | 3.34 | 29.9% | 19.3% | 21.9% | +6.3% | +45.0% | 0.4% |
| Tari Eason REB over 10.5 (11+) | HOU @ DAL | draftkings | 9.50 | 8.94 | 6.56 | 15.2% | 9.8% | 11.2% | +6.3% | +44.8% | 0.2% |
| Kevin Durant REB over 10.5 (11+) | HOU @ DAL | draftkings | 16.00 | 15.06 | 11.09 | 9.0% | 5.8% | 6.6% | +6.2% | +44.3% | 0.1% |
| Fred VanVleet REB over 6.5 (7+) | HOU @ DAL | draftkings | 11.60 | 10.93 | 8.05 | 12.4% | 8.1% | 9.2% | +6.1% | +44.2% | 0.1% |
| Jabari Smith Jr. REB over 8.5 (9+) | HOU @ DAL | draftkings | 4.25 | 4.02 | 2.98 | 33.5% | 22.0% | 24.9% | +5.7% | +42.4% | 0.4% |
| Jarace Walker AST over 4.5 (5+) | IND @ MIA | draftkings | 6.17 | 5.84 | 4.35 | 23.0% | 15.2% | 17.1% | +5.6% | +41.9% | 0.3% |
| Kevin Durant REB over 8.5 (9+) | HOU @ DAL | draftkings | 6.22 | 5.90 | 4.40 | 22.8% | 15.0% | 17.0% | +5.5% | +41.5% | 0.3% |
| Sandro Mamukelashvili REB over 8.5 (9+) | LAL @ GSW | draftkings | 11.00 | 10.43 | 7.78 | 12.9% | 8.5% | 9.6% | +5.5% | +41.4% | 0.1% |
| Nikola Jokic AST over 16.5 (17+) | DEN @ PHX | draftkings | 19.60 | 18.59 | 13.87 | 7.2% | 4.8% | 5.4% | +5.4% | +41.3% | 0.1% |
| Amen Thompson AST over 8.5 (9+) | HOU @ DAL | draftkings | 9.60 | 9.12 | 6.83 | 14.6% | 9.7% | 11.0% | +5.2% | +40.5% | 0.1% |
| Sandro Mamukelashvili REB over 6.5 (7+) | LAL @ GSW | draftkings | 4.48 | 4.26 | 3.20 | 31.3% | 20.9% | 23.5% | +5.1% | +40.1% | 0.4% |
| Andrew Nembhard AST over 16.5 (17+) | IND @ MIA | draftkings | 27.00 | 25.71 | 19.32 | 5.2% | 3.5% | 3.9% | +5.0% | +39.7% | 0.1% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Khaman Maluach PR under 16.5 | DEN @ PHX | draftkings | 1.88 | Oso Ighodaro | 77.0% | 81.1% | +7.3% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Clint Capela REB over 9.5 (10+) | HOU @ DAL | draftkings | 3.78 | 3.23 | 2.01 | 49.7% | 24.7% | 31.0% | +17.1% | +87.8% | 1.5% |
| Clint Capela REB over 7.5 (8+) | HOU @ DAL | draftkings | 2.10 | 1.97 | 1.45 | 69.1% | 44.6% | 50.7% | +6.6% | +45.2% | 1.5% |
| Kevin Durant RA over 9.5 (10+) | HOU @ DAL | draftkings | 1.95 | 1.84 | 1.36 | 73.3% | 48.0% | 54.3% | +6.0% | +43.1% | 1.6% |
| Quenton Jackson AST over 3.5 (4+) | IND @ MIA | draftkings | 2.29 | 2.17 | 1.62 | 61.9% | 40.8% | 46.1% | +5.5% | +41.7% | 1.1% |
| Kevin Durant PRA over 39.5 (40+) | HOU @ DAL | draftkings | 3.14 | 2.98 | 2.22 | 44.9% | 29.8% | 33.6% | +5.4% | +41.1% | 0.6% |
| Kevin Durant AST over 3.5 (4+) | HOU @ DAL | draftkings | 1.78 | 1.69 | 1.28 | 78.3% | 53.0% | 59.3% | +5.3% | +39.0% | 1.7% |
| Quenton Jackson PA over 9.5 (10+) | IND @ MIA | draftkings | 1.83 | 1.74 | 1.31 | 76.6% | 51.0% | 57.4% | +5.2% | +40.5% | 1.6% |

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
| Jarace Walker PTS over 10.5 (11+) | IND @ MIA | pointsbetau | 2.00 | 1.91 | 1.71 | 58.5% | 50.4% | 52.4% | +4.8% | +16.9% | 1.2% |
| Pascal Siakam PTS over 23.5 (24+) | IND @ MIA | pointsbetau | 1.95 | 1.88 | 1.61 | 61.9% | 50.4% | 53.3% | +4.0% | +20.9% | 1.1% |
| Andrew Nembhard PTS over 17.5 (18+) | IND @ MIA | unibet | 2.00 | 1.96 | 1.78 | 56.0% | 49.4% | 51.1% | +2.2% | +12.1% | 0.5% |
| Bam Adebayo STL over 1.5 (2+) | IND @ MIA | draftkings | 2.78 | 2.74 | 2.25 | 44.5% | 33.8% | 36.5% | +1.4% | +23.8% | 0.2% |
| Giannis Antetokounmpo PTS under 31.5 | IND @ MIA | sportsbet | 1.90 | 1.88 | 1.66 | 60.3% | 50.9% | 53.3% | +1.3% | +14.6% | 0.4% |
| Giannis Antetokounmpo PTS under 30.5 | IND @ MIA | pointsbetau | 2.00 | 1.99 | 1.76 | 57.0% | 48.1% | 50.3% | +0.6% | +13.9% | 0.1% |
| Bam Adebayo REB over 9.5 (10+) | IND @ MIA | draftkings | 2.01 | 2.01 | 1.69 | 59.2% | 46.7% | 49.9% | +0.2% | +19.1% | 0.1% |
| Kelly Oubre Jr. REB over 4.5 (5+) | IND @ MIA | draftkings | 2.09 | 2.09 | 1.76 | 56.8% | 44.9% | 47.9% | +0.1% | +18.7% | 0.0% |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 100% | 35.1<br><sub>34,32,30,-,35</sub> | 19.6<br><sub>18,16,14,-,18</sub> | 17.5 · 16.5 | 3.7<br><sub>2,2,1,-,3</sub> | 2.5 | 9.8<br><sub>9,5,3,-,14</sub> | 8.5 | 2.1<br><sub>0,1,4,-,1</sub> | 1.5 | 1.1 | 0.2 | 3.2 | 33.1 |
| Pascal Siakam | 100% | 35.0<br><sub>35,29,26,37,34</sub> | 27.9<br><sub>30,23,21,20,26</sub> | 24.5 · 23.5 | 8.0<br><sub>8,3,7,13,11</sub> | 7.5 | 4.9<br><sub>1,3,6,6,3</sub> | 3.5 | 1.9<br><sub>1,3,3,1,0</sub> | 1.5 | 1.2 | 0.4 | 3.1 | 40.8 |
| Kelly Oubre Jr. | 100% | 30.5<br><sub>28,20,20,23,30</sub> | 13.5<br><sub>4,3,14,9,15</sub> | 12.5 · 11.5 | 5.2<br><sub>2,2,2,3,3</sub> | 4.5 | 2.0<br><sub>3,2,2,1,1</sub> |  | 1.3<br><sub>0,1,1,1,1</sub> | 1.5 | 1.2 | 0.5 | 1.4 | 20.7 |
| Aaron Nesmith | 100% | 29.2<br><sub>-,20,19,21,27</sub> | 16.4<br><sub>-,9,13,13,18</sub> | 14.5 · 13.5 | 4.1<br><sub>-,4,1,0,2</sub> | 3.5 | 2.1<br><sub>-,1,2,1,1</sub> |  | 2.3<br><sub>-,1,2,3,3</sub> | 1.5 | 0.8 | 0.5 | 1.7 | 22.6 |
| Jarace Walker | 96% | 27.3<br><sub>19,17,19,29,22</sub> | 12.5<br><sub>3,2,6,10,7</sub> | 10.5 · 10.5 | 6.4<br><sub>6,1,7,8,8</sub> | 5.5 | 3.2<br><sub>2,1,1,2,1</sub> |  | 1.6<br><sub>1,0,0,2,1</sub> | 1.5 | 0.9 | 0.4 | 2.0 | 22.1 |
| Jay Huff | 100% | 23.5<br><sub>-,5,21,23,16</sub> | 9.5<br><sub>-,0,14,6,3</sub> | 8.5 · 8.5 | 4.7<br><sub>-,2,2,6,6</sub> | 4.5 | 2.0<br><sub>-,0,3,1,2</sub> |  | 1.3<br><sub>-,0,2,0,1</sub> | 1.5 | 0.5 | 1.5 | 1.0 | 16.1 |
| Quenton Jackson | 97% | 23.0<br><sub>16,17,18,27,14</sub> | 9.8<br><sub>6,8,5,4,2</sub> |  | 3.1<br><sub>4,1,1,2,2</sub> |  | 4.5<br><sub>1,3,2,4,6</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 0.9 | 0.2 | 1.4 | 17.4 |
| Larry Nance Jr. | 88% | 20.7<br><sub>5,1,22,19,23</sub> | 6.0<br><sub>0,0,6,2,5</sub> | 6.5 · 6.5 | 4.5<br><sub>0,0,6,3,5</sub> | 4.5 | 1.3<br><sub>0,0,1,1,0</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 1.0 | 0.4 | 0.7 | 11.8 |
| Jalen Slawson | 88% | 14.6<br><sub>-,16,8,3,12</sub> | 4.2<br><sub>-,4,1,2,2</sub> |  | 3.0<br><sub>-,5,2,1,1</sub> |  | 1.5<br><sub>-,2,0,0,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.6 | 0.7 | 8.7 |
| Kobe Brown | 48% | 14.2<br><sub>-,1,-,-,-</sub> | 5.5<br><sub>-,0,-,-,-</sub> |  | 2.9<br><sub>-,0,-,-,-</sub> |  | 1.2<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.8 | 9.6 |
| Braden Smith | 58% | 12.7<br><sub>-,-,-,-,5</sub> | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.5 | 0.3 | 0.6 | 2.1 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 100% | 33.7<br><sub>33,33,37,33,34</sub> | 13.0<br><sub>11,18,22,21,10</sub> | 11.5 · 11.5 | 2.8<br><sub>0,2,1,0,1</sub> | 2.5 | 7.2<br><sub>11,5,10,2,10</sub> | 6.5 | 1.5<br><sub>1,3,3,2,0</sub> | 1.5 | 1.3 | 0.2 | 1.9 | 23.0 |
| Bam Adebayo | 100% | 33.6<br><sub>31,23,39,30,33</sub> | 20.1<br><sub>15,4,20,8,24</sub> | 18.5 · 18.5 | 10.7<br><sub>7,6,8,8,9</sub> | 9.5 | 3.9<br><sub>4,3,4,3,3</sub> | 3.5 | 1.6<br><sub>1,0,2,0,0</sub> | 1.5 | 1.5 | 0.7 | 1.8 | 34.7 |
| Giannis Antetokounmpo | 100% | 33.1<br><sub>30,33,25,39,31</sub> | 30.0<br><sub>35,36,14,29,24</sub> | 31.5 · 31.5 | 12.5<br><sub>6,12,6,14,18</sub> | 11.5 | 6.1<br><sub>1,5,3,11,3</sub> | 6.5 | 0.5<br><sub>0,1,0,2,0</sub> | 0.5 | 1.2 | 0.9 | 3.2 | 48.6 |
| Pelle Larsson | 98% | 30.6<br><sub>24,29,36,34,31</sub> | 12.4<br><sub>2,7,15,12,17</sub> | 11.5 · 11.5 | 4.0<br><sub>3,2,7,0,6</sub> | 3.5 | 3.8<br><sub>4,1,4,4,8</sub> | 3.5 | 1.0<br><sub>0,1,1,1,2</sub> |  | 1.1 | 0.3 | 1.6 | 20.2 |
| Andrew Wiggins | 100% | 28.4<br><sub>27,26,18,34,29</sub> | 13.0<br><sub>11,8,4,12,18</sub> | 12.5 · 12.5 | 4.7<br><sub>2,8,1,3,2</sub> | 3.5 | 2.2<br><sub>1,2,1,1,2</sub> | 1.5 | 1.7<br><sub>1,1,0,0,4</sub> | 1.5 | 1.0 | 1.0 | 1.2 | 20.0 |
| Bobby Portis | 98% | 23.1<br><sub>25,21,27,24,23</sub> | 11.2<br><sub>7,11,13,10,11</sub> | 10.5 · 11.5 | 6.8<br><sub>4,8,8,12,9</sub> | 6.5 | 1.6<br><sub>1,2,0,2,4</sub> |  | 1.6<br><sub>1,3,2,3,1</sub> | 1.5 | 0.7 | 0.4 | 0.8 | 19.6 |
| Klay Thompson | 100% | 21.5<br><sub>16,24,27,15,17</sub> | 9.7<br><sub>10,6,14,6,3</sub> | 7.5 · 7.5 | 2.0<br><sub>1,2,3,1,1</sub> |  | 1.3<br><sub>0,2,0,1,2</sub> |  | 1.8<br><sub>3,2,4,2,1</sub> | 2.5 | 0.6 | 0.3 | 0.8 | 13.1 |
| Tim Hardaway Jr. | 98% | 19.0<br><sub>18,21,21,16,22</sub> | 8.1<br><sub>3,8,5,5,14</sub> | 8.5 · 8.5 | 2.3<br><sub>4,4,0,2,3</sub> |  | 1.0<br><sub>1,1,0,1,1</sub> |  | 1.2<br><sub>1,2,0,1,2</sub> | 1.5 | 0.6 | 0.2 | 0.5 | 11.4 |
| Dru Smith | 64% | 12.5<br><sub>-,6,-,15,14</sub> | 4.1<br><sub>-,3,-,6,3</sub> |  | 1.7<br><sub>-,0,-,2,0</sub> |  | 1.9<br><sub>-,1,-,1,3</sub> |  | 0.3<br><sub>-,1,-,2,0</sub> |  | 1.0 | 0.3 | 0.6 | 7.6 |
| Nikola Jovic | 67% | 10.0<br><sub>24,13,6,-,7</sub> | 3.9<br><sub>4,5,0,-,5</sub> |  | 2.1<br><sub>4,4,2,-,3</sub> |  | 1.0<br><sub>2,1,0,-,0</sub> |  | 0.3<br><sub>0,0,0,-,1</sub> |  | 0.4 | 0.2 | 0.5 | 7.0 |
| Tre Donaldson | 16% | 8.6 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.0 |
| Simone Fontecchio | 48% | 7.5<br><sub>3,3,-,-,-</sub> | 3.7<br><sub>0,0,-,-,-</sub> |  | 1.4<br><sub>0,1,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.4<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 5.7 |
| Keshad Johnson | 23% | 7.1 | 3.4 |  | 1.6 |  | 0.3 |  | 0.2 |  | 0.4 | 0.2 | 0.3 | 5.3 |
| Nick Richards | 48% | 6.5<br><sub>3,3,-,-,-</sub> | 2.6<br><sub>4,3,-,-,-</sub> |  | 2.4<br><sub>1,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.1<br><sub>0,1,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.3 |
| Myron Gardner | 48% | 6.0<br><sub>3,3,-,-,-</sub> | 2.4<br><sub>4,0,-,-,-</sub> |  | 1.8<br><sub>2,0,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |
| Ryan Conwell | 52% | 5.7<br><sub>3,3,4,-,-</sub> | 2.3<br><sub>0,2,3,-,-</sub> |  | 0.9<br><sub>0,0,1,-,-</sub> |  | 0.7<br><sub>2,0,0,-,-</sub> |  | 0.2<br><sub>0,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.8 |
| Vladislav Goldin | 23% | 5.4 | 1.9 |  | 1.6 |  | 0.3 |  | 0.0 |  | 0.2 | 0.4 | 0.3 | 3.8 |

</details>


### HOU @ DAL
Out: Santi Aldama (DAL), Sergio de Larrea (DAL), Dereck Lively II (DAL), Steven Adams (HOU), Alperen Sengun (HOU), Reed Sheppard (HOU)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Fred VanVleet PTS over 12.5 (13+) | HOU @ DAL | sportsbet | 1.96 | 1.89 | 1.59 | 62.7% | 49.6% | 52.9% | +3.7% | +23.0% | 1.0% |
| Clint Capela PTS over 6.5 (7+) | HOU @ DAL | unibet | 1.97 | 1.91 | 1.77 | 56.5% | 50.9% | 52.3% | +3.2% | +11.4% | 0.8% |
| Naji Marshall PTS over 11.5 (12+) | HOU @ DAL | unibet | 2.00 | 1.95 | 1.77 | 56.4% | 49.6% | 51.3% | +2.6% | +12.7% | 0.6% |
| Amen Thompson STL over 1.5 (2+) | HOU @ DAL | draftkings | 2.30 | 2.27 | 1.88 | 53.2% | 40.9% | 44.0% | +1.1% | +22.3% | 0.2% |
| Jabari Smith Jr. REB over 6.5 (7+) | HOU @ DAL | draftkings | 2.10 | 2.08 | 1.70 | 58.9% | 44.5% | 48.1% | +1.0% | +23.6% | 0.2% |
| Fred VanVleet REB over 3.5 (4+) | HOU @ DAL | draftkings | 2.22 | 2.20 | 1.83 | 54.6% | 42.4% | 45.4% | +0.9% | +21.1% | 0.2% |
| Tari Eason STL over 1.5 (2+) | HOU @ DAL | draftkings | 2.58 | 2.56 | 2.12 | 47.2% | 36.3% | 39.1% | +0.8% | +21.9% | 0.1% |
| Cooper Flagg PRA under 35.5 | HOU @ DAL | draftkings | 1.93 | 1.91 | 1.58 | 63.4% | 48.5% | 52.2% | +0.6% | +22.1% | 0.2% |
| Cooper Flagg PA under 29.5 | HOU @ DAL | draftkings | 1.85 | 1.85 | 1.54 | 65.1% | 50.4% | 54.1% | +0.3% | +20.7% | 0.1% |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 100% | 37.1<br><sub>33,36,39,28,33</sub> | 20.1<br><sub>16,20,17,15,23</sub> | 18.5 · 18.5 | 8.0<br><sub>10,10,11,5,4</sub> | 7.5 | 5.7<br><sub>4,4,6,2,3</sub> | 4.5 | 0.3<br><sub>1,1,0,0,0</sub> |  | 1.8 | 0.7 | 2.5 | 33.9 |
| Jabari Smith Jr. | 100% | 36.7<br><sub>36,34,33,39,30</sub> | 17.5<br><sub>30,7,14,16,14</sub> | 16.5 · 16.5 | 7.4<br><sub>5,5,5,12,2</sub> | 6.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 2.2<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.6 | 27.2 |
| Kevin Durant | 100% | 36.5<br><sub>37,37,37,30,31</sub> | 27.1<br><sub>30,20,22,22,18</sub> | 24.5 · 23.5 | 6.5<br><sub>6,7,4,9,5</sub> | 5.5 | 5.7<br><sub>3,6,2,3,4</sub> | 3.5 | 2.4<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.2 | 3.5 | 39.3 |
| Fred VanVleet | 100% | 34.1<br><sub>30,32,-,29,29</sub> | 15.2<br><sub>6,14,-,5,24</sub> | 12.5 · 12.5 | 4.0<br><sub>2,3,-,4,6</sub> | 3.5 | 5.8<br><sub>11,5,-,5,5</sub> | 6.5 | 2.5<br><sub>2,3,-,0,4</sub> | 2.5 | 1.7 | 0.4 | 1.5 | 25.0 |
| Tari Eason | 98% | 30.9<br><sub>3,27,31,33,31</sub> | 13.5<br><sub>2,12,19,13,5</sub> | 11.5 · 13.5 | 7.2<br><sub>1,6,3,8,9</sub> | 6.5 | 1.8<br><sub>0,0,0,2,1</sub> | 1.5 | 1.3<br><sub>0,0,0,1,1</sub> | 0.5 | 1.6 | 0.8 | 1.5 | 22.5 |
| Marcus Smart | 52% | 26.3<br><sub>26,21,-,-,-</sub> | 8.8<br><sub>10,5,-,-,-</sub> | – · 8.5 | 3.0<br><sub>2,3,-,-,-</sub> |  | 2.9<br><sub>2,1,-,-,-</sub> |  | 1.2<br><sub>2,0,-,-,-</sub> |  | 1.6 | 0.5 | 1.8 | 14.7 |
| Clint Capela | 100% | 25.8<br><sub>8,-,11,4,22</sub> | 7.7<br><sub>0,-,2,2,10</sub> | 6.5 · 6.5 | 9.8<br><sub>3,-,3,2,8</sub> | 7.5 | 1.6<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 1.0 | 1.8 | 1.2 | 19.1 |
| Oscar Tshiebwe | 67% | 19.4<br><sub>-,-,-,-,14</sub> | 8.3<br><sub>-,-,-,-,7</sub> |  | 8.5<br><sub>-,-,-,-,5</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.5 | 1.0 | 18.1 |
| Bogdan Bogdanovic | 88% | 18.5<br><sub>13,9,20,13,15</sub> | 7.1<br><sub>5,3,11,5,16</sub> |  | 2.4<br><sub>1,1,1,2,2</sub> |  | 1.9<br><sub>2,0,1,1,4</sub> |  | 1.0<br><sub>1,1,3,1,4</sub> |  | 0.7 | 0.2 | 0.7 | 11.4 |
| Jae'Sean Tate | 84% | 9.0<br><sub>2,-,1,1,4</sub> | 2.5<br><sub>0,-,0,0,0</sub> |  | 2.0<br><sub>0,-,0,1,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.4 | 5.1 |
| Isaiah Crawford | 72% | 8.2<br><sub>3,-,1,1,5</sub> | 2.2<br><sub>3,-,0,0,3</sub> |  | 1.5<br><sub>0,-,0,0,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.3 | 4.3 |
| Bruce Thornton | 80% | 8.0<br><sub>3,-,4,1,3</sub> | 2.0<br><sub>0,-,0,0,5</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.8<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 3.0 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington | 100% | 30.9<br><sub>31,33,36,41,27</sub> | 13.3<br><sub>10,20,12,20,18</sub> | 13.5 · 13.5 | 6.5<br><sub>4,13,4,9,9</sub> | 6.5 | 1.6<br><sub>2,0,2,2,0</sub> |  | 1.5<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.7 | 21.4 |
| Cooper Flagg | 100% | 30.8<br><sub>33,17,-,40,33</sub> | 21.5<br><sub>32,14,-,29,26</sub> | 23.5 · 23.5 | 6.1<br><sub>5,5,-,6,5</sub> | 6.5 | 5.3<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.5 | 32.9 |
| Kyrie Irving | 100% | 30.8<br><sub>24,25,-,33,27</sub> | 20.0<br><sub>15,24,-,18,15</sub> | 18.5 · 19.5 | 3.7<br><sub>4,1,-,6,2</sub> | 3.5 | 3.8<br><sub>2,3,-,6,4</sub> | 3.5 | 2.2<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.1 | 27.6 |
| Zaccharie Risacher | 88% | 27.3<br><sub>27,32,32,30,29</sub> | 8.8<br><sub>4,11,11,6,13</sub> | 8.5 · 8.5 | 5.1<br><sub>6,6,4,8,6</sub> | 4.5 | 1.4<br><sub>2,1,2,1,1</sub> |  | 0.9<br><sub>0,1,1,1,2</sub> |  | 1.1 | 1.3 | 1.1 | 15.4 |
| Max Christie | 100% | 26.1<br><sub>29,38,26,26,22</sub> | 9.8<br><sub>5,16,5,11,11</sub> | 8.5 · 9.5 | 2.9<br><sub>3,4,5,5,5</sub> | 3.5 | 1.7<br><sub>2,4,1,3,2</sub> |  | 1.5<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.4 | 1.2 | 14.4 |
| Naji Marshall | 98% | 25.6<br><sub>29,33,21,-,-</sub> | 13.4<br><sub>16,15,10,-,-</sub> | 11.5 · 11.5 | 3.7<br><sub>2,4,4,-,-</sub> | 3.5 | 3.5<br><sub>6,6,5,-,-</sub> | 3.5 | 0.8<br><sub>2,0,1,-,-</sub> | 0.5 | 1.2 | 0.1 | 1.7 | 20.7 |
| Daniel Gafford | 100% | 23.0<br><sub>22,15,23,26,27</sub> | 9.0<br><sub>2,4,12,8,7</sub> | 7.5 · 7.5 | 7.0<br><sub>3,3,9,9,11</sub> | 6.5 | 1.4<br><sub>1,5,2,3,2</sub> |  | 0.0<br><sub>0,0,0,0,1</sub> |  | 0.8 | 1.5 | 1.1 | 17.4 |
| Marcus Sasser | 91% | 17.2<br><sub>24,27,27,8,22</sub> | 6.1<br><sub>17,6,12,0,10</sub> | 5.5 · – | 1.4<br><sub>1,2,3,1,1</sub> |  | 2.2<br><sub>1,3,5,0,4</sub> |  | 0.9<br><sub>4,2,2,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 9.8 |
| Morez Johnson Jr. | 98% | 12.9<br><sub>14,17,12,15,18</sub> | 5.3<br><sub>6,8,6,6,10</sub> |  | 1.8<br><sub>3,6,1,2,6</sub> |  | 1.2<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.8 | 8.3 |
| Walter Clayton Jr. | 67% | 12.8<br><sub>-,1,15,17,15</sub> | 4.3<br><sub>-,0,3,15,0</sub> |  | 2.0<br><sub>-,1,2,4,2</sub> |  | 2.8<br><sub>-,0,5,4,5</sub> |  | 0.4<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.0 |
| Caleb Martin | 91% | 12.6<br><sub>-,-,-,-,14</sub> | 4.0<br><sub>-,-,-,-,10</sub> |  | 2.0<br><sub>-,-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,2</sub> |  | 0.6 | 0.3 | 0.6 | 7.0 |
| Moussa Cisse | 76% | 7.4<br><sub>3,1,7,-,3</sub> | 2.5<br><sub>3,3,4,-,0</sub> |  | 2.8<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.6 | 0.4 | 5.6 |
| Tobi Lawal | 63% | 6.1<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.0<br><sub>-,0,1,-,0</sub> |  | 0.9<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.2 | 0.2 | 0.3 | 3.9 |
| Jett Howard | 63% | 5.9<br><sub>-,-,4,-,3</sub> | 2.4<br><sub>-,-,5,-,0</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.2 | 3.5 |

</details>


### LAC @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brook Lopez PTS under 10.5 | LAC @ MIN | tab | 1.90 | 1.85 | 1.66 | 60.1% | 52.0% | 54.0% | +2.7% | +14.2% | 0.8% |
| Rudy Gobert PTS under 10.5 | LAC @ MIN | tab | 1.87 | 1.82 | 1.59 | 63.0% | 52.2% | 54.9% | +2.7% | +17.7% | 0.8% |
| Darius Garland PTS under 22.5 | LAC @ MIN | pointsbetau | 2.00 | 1.95 | 1.72 | 58.1% | 48.9% | 51.2% | +2.4% | +16.3% | 0.6% |
| Jaden McDaniels PTS under 17.5 | LAC @ MIN | draftkings | 1.95 | 1.92 | 1.67 | 59.7% | 49.6% | 52.1% | +1.8% | +16.6% | 0.5% |
| Rui Hachimura PTS under 14.5 | LAC @ MIN | pointsbetau | 1.95 | 1.92 | 1.63 | 61.3% | 49.0% | 52.0% | +1.6% | +19.6% | 0.4% |
| Derrick Jones Jr. PTS under 10.5 | LAC @ MIN | tab | 1.95 | 1.93 | 1.79 | 55.8% | 50.4% | 51.7% | +1.0% | +8.9% | 0.3% |
| LaMelo Ball PTS under 20.5 | LAC @ MIN | draftkings | 1.92 | 1.90 | 1.66 | 60.2% | 50.0% | 52.6% | +0.8% | +15.5% | 0.2% |
| Rui Hachimura 3PM under 1.5 | LAC @ MIN | draftkings | 2.36 | 2.35 | 1.94 | 51.7% | 39.6% | 42.6% | +0.6% | +21.9% | 0.1% |
| Darius Garland PA under 30.5 | LAC @ MIN | draftkings | 1.92 | 1.91 | 1.57 | 63.6% | 48.7% | 52.5% | +0.6% | +21.9% | 0.2% |
| Darius Garland PRA under 33.5 | LAC @ MIN | draftkings | 1.87 | 1.86 | 1.54 | 64.9% | 50.0% | 53.7% | +0.4% | +21.2% | 0.1% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 100% | 30.9<br><sub>32,37,36,26</sub> | 21.8<br><sub>30,26,16,14</sub> | 23.5 · 23.5 | 2.5<br><sub>1,0,4,1</sub> | 2.5 | 6.2<br><sub>4,6,11,5</sub> | 7.5 | 2.6<br><sub>3,4,2,1</sub> | 2.5 | 1.2 | 0.2 | 3.5 | 30.6 |
| Rui Hachimura | 100% | 30.5<br><sub>32,33,29,-</sub> | 13.6<br><sub>10,16,5,-</sub> | 14.5 · 14.5 | 4.1<br><sub>8,6,4,-</sub> | 4.5 | 1.1<br><sub>2,1,0,-</sub> | 1.5 | 1.6<br><sub>2,3,1,-</sub> | 1.5 | 0.9 | 0.4 | 1.4 | 18.8 |
| Derrick Jones Jr. | 100% | 28.0<br><sub>26,35,30,28</sub> | 10.5<br><sub>8,16,11,15</sub> | 10.5 · 10.5 | 4.1<br><sub>6,4,6,5</sub> | 4.5 | 1.3<br><sub>5,1,1,0</sub> |  | 1.1<br><sub>1,3,3,3</sub> | 1.5 | 1.1 | 0.8 | 1.0 | 15.9 |
| Kris Dunn | 100% | 27.9<br><sub>27,34,33,27</sub> | 7.1<br><sub>7,7,15,5</sub> | 7.5 · 8.5 | 3.7<br><sub>5,5,4,3</sub> | 3.5 | 3.9<br><sub>7,5,6,3</sub> | 4.5 | 0.8<br><sub>2,1,1,1</sub> | 0.5 | 1.9 | 0.3 | 1.5 | 14.7 |
| Keaton Wagler | 93% | 25.2<br><sub>29,24,26,28</sub> | 13.0<br><sub>15,13,11,21</sub> | 12.5 · 12.5 | 3.2<br><sub>5,3,5,4</sub> | 3.5 | 3.1<br><sub>5,3,4,2</sub> | 2.5 | 1.4<br><sub>3,2,1,3</sub> | 1.5 | 1.0 | 0.3 | 2.3 | 19.3 |
| Isaiah Jackson | 100% | 22.8<br><sub>15,28,24,19</sub> | 9.5<br><sub>13,6,10,4</sub> | 7.5 · 8.5 | 6.7<br><sub>5,6,6,5</sub> | 6.5 | 1.6<br><sub>0,3,4,1</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 1.0 | 1.2 | 1.7 | 17.9 |
| Brook Lopez | 98% | 22.5<br><sub>27,20,23,22</sub> | 9.9<br><sub>17,22,15,2</sub> | 10.5 · 10.5 | 4.0<br><sub>11,4,1,3</sub> | 4.5 | 1.4<br><sub>1,0,2,3</sub> |  | 1.2<br><sub>1,2,3,0</sub> | 1.5 | 0.6 | 1.1 | 1.0 | 15.4 |
| Kobe Sanders | 96% | 20.6<br><sub>19,19,20,27</sub> | 8.3<br><sub>2,5,12,9</sub> | 7.5 · 7.5 | 2.4<br><sub>0,3,4,4</sub> |  | 1.8<br><sub>3,5,2,0</sub> |  | 1.0<br><sub>0,1,2,1</sub> | 1.5 | 1.0 | 0.2 | 1.3 | 12.6 |
| Gradey Dick | 91% | 15.8<br><sub>19,12,18,19</sub> | 6.9<br><sub>12,6,6,5</sub> |  | 2.5<br><sub>4,4,3,5</sub> |  | 0.8<br><sub>0,0,0,0</sub> |  | 0.7<br><sub>1,0,2,1</sub> |  | 0.6 | 0.1 | 0.9 | 10.3 |
| Baba Miller | 80% | 13.3<br><sub>9,-,2,17</sub> | 6.0<br><sub>4,-,0,4</sub> |  | 2.0<br><sub>3,-,1,7</sub> |  | 1.4<br><sub>1,-,0,1</sub> |  | 0.3<br><sub>0,-,0,0</sub> |  | 0.6 | 0.2 | 0.8 | 9.4 |
| Cam Christie | 58% | 9.4<br><sub>2,-,-,14</sub> | 3.3<br><sub>0,-,-,2</sub> |  | 1.5<br><sub>0,-,-,0</sub> |  | 0.7<br><sub>0,-,-,0</sub> |  | 0.1<br><sub>0,-,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 5.4 |
| Jalen Pickett | 52% | 7.6<br><sub>2,-,-,8</sub> | 2.8<br><sub>3,-,-,4</sub> |  | 1.0<br><sub>0,-,-,1</sub> |  | 1.0<br><sub>0,-,-,1</sub> |  | 0.2<br><sub>1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Nick Martinelli | 58% | 6.9<br><sub>2,-,-,6</sub> | 3.2<br><sub>0,-,-,2</sub> |  | 1.8<br><sub>1,-,-,3</sub> |  | 0.7<br><sub>1,-,-,1</sub> |  | 0.1<br><sub>0,-,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.6 |
| Blake Wesley | 30% | 6.4 | 2.7 |  | 0.7 |  | 0.9 |  | 0.1 |  | 0.4 | 0.1 | 0.5 | 4.3 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 100% | 34.6<br><sub>29,30,31,37,35</sub> | 16.6<br><sub>17,15,14,14,19</sub> | 17.5 · 17.5 | 5.8<br><sub>8,6,6,6,7</sub> | 5.5 | 2.9<br><sub>1,3,3,4,4</sub> | 2.5 | 1.4<br><sub>1,2,1,2,1</sub> | 1.5 | 1.1 | 0.9 | 1.8 | 25.2 |
| Ayo Dosunmu | 100% | 32.4<br><sub>29,27,23,26,32</sub> | 16.6<br><sub>16,14,9,9,17</sub> | 16.5 · 15.5 | 4.3<br><sub>5,7,3,1,3</sub> | 4.5 | 4.6<br><sub>3,10,3,0,4</sub> | 4.5 | 1.7<br><sub>1,1,1,1,3</sub> | 1.5 | 1.2 | 0.4 | 2.0 | 25.5 |
| Jonathan Kuminga | 100% | 32.0<br><sub>30,27,26,36,32</sub> | 14.7<br><sub>12,11,13,10,20</sub> | 14.5 · 14.5 | 5.9<br><sub>1,8,4,10,3</sub> | 5.5 | 2.6<br><sub>3,5,1,1,5</sub> | 2.5 | 1.4<br><sub>2,2,3,0,3</sub> | 1.5 | 1.1 | 0.5 | 1.8 | 23.2 |
| Rudy Gobert | 100% | 30.8<br><sub>33,30,31,36,20</sub> | 9.6<br><sub>5,14,8,5,1</sub> | 10.5 · 10.5 | 10.9<br><sub>15,9,13,20,4</sub> | 11.5 | 1.7<br><sub>1,1,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.3 | 1.5 | 22.1 |
| LaMelo Ball | 100% | 28.6<br><sub>29,23,17,31,28</sub> | 19.5<br><sub>21,12,15,11,8</sub> | 20.5 · 20.5 | 3.9<br><sub>2,5,1,0,4</sub> | 4.5 | 6.5<br><sub>6,5,8,6,8</sub> | 7.5 | 3.1<br><sub>5,2,4,1,2</sub> | 3.5 | 1.2 | 0.3 | 3.2 | 29.9 |
| Terrence Shannon Jr. | 96% | 25.6<br><sub>20,22,23,24,27</sub> | 14.4<br><sub>10,13,15,14,19</sub> | 14.5 · 13.5 | 3.0<br><sub>1,4,4,4,6</sub> | 2.5 | 2.2<br><sub>1,1,3,5,2</sub> |  | 1.6<br><sub>2,2,3,3,1</sub> | 1.5 | 0.7 | 0.1 | 1.6 | 19.6 |
| Trey Lyles | 97% | 17.5<br><sub>12,17,14,13,22</sub> | 5.0<br><sub>1,9,3,3,7</sub> |  | 3.9<br><sub>1,6,6,1,3</sub> |  | 1.1<br><sub>0,2,2,1,1</sub> |  | 0.6<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.3 | 0.6 | 9.9 |
| Joan Beringer | 91% | 16.5<br><sub>14,15,13,17,20</sub> | 7.5<br><sub>0,9,6,12,7</sub> | 6.5 · 6.5 | 5.9<br><sub>6,9,6,7,9</sub> | 5.5 | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.1 |
| Bones Hyland | 96% | 15.4<br><sub>4,8,15,5,16</sub> | 7.6<br><sub>3,3,3,0,13</sub> |  | 1.8<br><sub>1,1,3,1,1</sub> |  | 2.1<br><sub>0,0,2,2,3</sub> |  | 1.1<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.3 | 1.0 | 11.4 |
| Jaylen Clark | 71% | 9.4<br><sub>3,3,5,-,7</sub> | 3.1<br><sub>1,0,3,-,3</sub> |  | 1.2<br><sub>1,2,1,-,2</sub> |  | 0.6<br><sub>1,1,0,-,1</sub> |  | 0.2<br><sub>0,0,0,-,1</sub> |  | 0.5 | 0.1 | 0.3 | 5.0 |
| Zyon Pullin | 52% | 8.1<br><sub>-,-,5,-,-</sub> | 2.9<br><sub>-,-,2,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.1 |
| Rocco Zikarsky | 23% | 6.8 | 2.3 |  | 2.1 |  | 0.4 |  | 0.0 |  | 0.2 | 0.6 | 0.3 | 4.8 |
| Enrique Freeman | 16% | 6.4 | 1.9 |  | 1.4 |  | 0.3 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.6 |
| Cody Williams | 52% | 6.2<br><sub>3,3,5,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 1.0 |
| Isaiah Evans | 52% | 6.0<br><sub>2,2,4,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 1.1<br><sub>1,0,0,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.0 |

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
