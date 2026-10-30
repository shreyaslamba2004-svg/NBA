# NBA model · Fri 30 Oct 2026 (US date)

Updated **Sat 31 Oct, 09:49 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-10-30/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

1 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| CHA @ WAS | team points | CHA projected 119, market implies 110 | 50% of tonight's minutes go to players new to CHA since last season, and the team ratings still lean on last season; CHA have played 5 games this season; CHA out: Knueppel, Williams | 42% of tonight's minutes go to players new to WAS since last season, and the team ratings still lean on last season; WAS have played 5 games this season; WAS out: Champagnie, Vukcevic, Watkins |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam PTS over 44.5 (45+) | IND @ MIA | draftkings | 30.00 | 22.99 | 12.42 | 8.1% | 3.1% | 4.3% | +30.5% | +141.5% | 0.3% |
| Pascal Siakam PTS over 39.5 (40+) | IND @ MIA | draftkings | 15.80 | 12.32 | 6.79 | 14.7% | 5.9% | 8.1% | +28.2% | +132.5% | 0.5% |
| Kevin Durant AST over 9.5 (10+) | HOU @ DAL | draftkings | 26.00 | 20.28 | 11.19 | 8.9% | 3.6% | 4.9% | +28.2% | +132.3% | 0.3% |
| Kevin Durant PR over 49.5 (50+) | HOU @ DAL | draftkings | 23.00 | 18.08 | 10.08 | 9.9% | 4.1% | 5.5% | +27.2% | +128.3% | 0.3% |
| Kevin Durant PR over 44.5 (45+) | HOU @ DAL | draftkings | 13.00 | 10.26 | 5.73 | 17.4% | 7.2% | 9.8% | +26.8% | +126.8% | 0.6% |
| Kevin Durant PR over 39.5 (40+) | HOU @ DAL | draftkings | 6.43 | 5.54 | 3.50 | 28.6% | 14.5% | 18.1% | +16.1% | +84.0% | 0.7% |
| Pascal Siakam PTS over 34.5 (35+) | IND @ MIA | draftkings | 7.20 | 6.29 | 4.05 | 24.7% | 13.0% | 15.9% | +14.5% | +77.7% | 0.6% |
| Amen Thompson STL over 3.5 (4+) | HOU @ DAL | draftkings | 13.40 | 11.81 | 7.73 | 12.9% | 7.0% | 8.5% | +13.4% | +73.4% | 0.3% |
| Jarace Walker PRA over 29.5 (30+) | IND @ MIA | draftkings | 8.60 | 7.63 | 5.05 | 19.8% | 10.9% | 13.1% | +12.7% | +70.3% | 0.4% |
| Aaron Nesmith PTS over 24.5 (25+) | IND @ MIA | draftkings | 10.00 | 9.03 | 6.16 | 16.2% | 9.3% | 11.1% | +10.7% | +62.2% | 0.3% |
| Zaccharie Risacher REB over 7.5 (8+) | HOU @ DAL | draftkings | 8.70 | 7.93 | 5.49 | 18.2% | 10.7% | 12.6% | +9.7% | +58.5% | 0.3% |
| Amen Thompson STL over 2.5 (3+) | HOU @ DAL | draftkings | 5.55 | 5.07 | 3.52 | 28.4% | 16.8% | 19.7% | +9.5% | +57.5% | 0.5% |
| Jarace Walker PRA over 34.5 (35+) | IND @ MIA | draftkings | 17.80 | 16.31 | 11.43 | 8.8% | 5.2% | 6.1% | +9.0% | +55.7% | 0.1% |
| Aaron Nesmith PRA over 34.5 (35+) | IND @ MIA | draftkings | 14.20 | 13.05 | 9.18 | 10.9% | 6.6% | 7.7% | +8.8% | +54.6% | 0.2% |
| Pascal Siakam AST over 7.5 (8+) | IND @ MIA | draftkings | 9.30 | 8.55 | 6.02 | 16.6% | 10.1% | 11.7% | +8.7% | +54.6% | 0.3% |
| Alex Sarr BLK over 3.5 (4+) | CHA @ WAS | draftkings | 15.40 | 14.16 | 9.98 | 10.0% | 6.1% | 7.1% | +8.7% | +54.3% | 0.1% |
| Aaron Nesmith PA over 29.5 (30+) | IND @ MIA | draftkings | 14.20 | 13.07 | 9.22 | 10.8% | 6.6% | 7.6% | +8.6% | +54.0% | 0.2% |
| Aaron Nesmith PR over 29.5 (30+) | IND @ MIA | draftkings | 9.80 | 9.03 | 6.37 | 15.7% | 9.5% | 11.1% | +8.5% | +53.8% | 0.2% |
| Alex Sarr BLK over 2.5 (3+) | CHA @ WAS | draftkings | 6.51 | 6.01 | 4.25 | 23.5% | 14.4% | 16.7% | +8.4% | +53.1% | 0.4% |
| Grayson Allen STL over 2.5 (3+) | CHA @ WAS | draftkings | 11.20 | 10.34 | 7.33 | 13.7% | 8.3% | 9.7% | +8.3% | +52.9% | 0.2% |
| Moritz Wagner REB over 7.5 (8+) | DET @ BKN | draftkings | 18.00 | 16.61 | 11.78 | 8.5% | 5.2% | 6.0% | +8.3% | +52.8% | 0.1% |
| Amen Thompson PA over 39.5 (40+) | HOU @ DAL | draftkings | 16.20 | 14.99 | 10.65 | 9.4% | 5.8% | 6.7% | +8.1% | +52.1% | 0.1% |
| Kevin Durant REB over 9.5 (10+) | HOU @ DAL | draftkings | 11.00 | 10.18 | 7.25 | 13.8% | 8.5% | 9.8% | +8.0% | +51.7% | 0.2% |
| Aaron Nesmith PRA over 29.5 (30+) | IND @ MIA | draftkings | 6.84 | 6.33 | 4.51 | 22.2% | 13.7% | 15.8% | +8.0% | +51.6% | 0.3% |
| Aaron Nesmith PTS over 29.5 (30+) | IND @ MIA | draftkings | 22.00 | 20.41 | 14.55 | 6.9% | 4.2% | 4.9% | +7.9% | +51.2% | 0.1% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 8.5 (9+) | HOU @ DAL | draftkings | 16.60 | 12.56 | 6.69 | 14.9% | 5.6% | 8.0% | +32.1% | +148.2% | 0.5% |
| Jay Huff AST over 4.5 (5+) | IND @ MIA | draftkings | 23.00 | 20.70 | 14.01 | 7.1% | 4.1% | 4.8% | +11.1% | +64.2% | 0.1% |
| Zaccharie Risacher REB over 8.5 (9+) | HOU @ DAL | draftkings | 14.80 | 13.40 | 9.18 | 10.9% | 6.3% | 7.5% | +10.4% | +61.1% | 0.2% |
| Pascal Siakam AST over 8.5 (9+) | IND @ MIA | draftkings | 16.00 | 14.60 | 10.13 | 9.9% | 5.8% | 6.9% | +9.6% | +57.9% | 0.2% |
| Moritz Wagner REB over 6.5 (7+) | DET @ BKN | draftkings | 10.70 | 9.86 | 6.96 | 14.4% | 8.7% | 10.1% | +8.5% | +53.8% | 0.2% |
| Jabari Smith Jr. REB over 10.5 (11+) | HOU @ DAL | draftkings | 9.70 | 8.94 | 6.31 | 15.8% | 9.6% | 11.2% | +8.5% | +53.8% | 0.2% |
| Julius Randle REB over 10.5 (11+) | DET @ BKN | draftkings | 9.20 | 8.53 | 6.09 | 16.4% | 10.2% | 11.7% | +7.9% | +51.2% | 0.2% |
| Moussa Diabate AST over 4.5 (5+) | CHA @ WAS | draftkings | 11.80 | 10.94 | 7.82 | 12.8% | 7.9% | 9.1% | +7.8% | +51.0% | 0.2% |
| Kevin Durant REB over 8.5 (9+) | HOU @ DAL | draftkings | 6.89 | 6.40 | 4.58 | 21.8% | 13.6% | 15.6% | +7.7% | +50.5% | 0.3% |
| Zaccharie Risacher REB over 6.5 (7+) | HOU @ DAL | draftkings | 5.26 | 4.89 | 3.51 | 28.5% | 17.8% | 20.4% | +7.5% | +49.7% | 0.4% |
| Daniss Jenkins AST over 6.5 (7+) | DET @ BKN | draftkings | 7.40 | 6.92 | 5.01 | 20.0% | 12.6% | 14.5% | +7.0% | +47.7% | 0.3% |
| Jarace Walker AST over 4.5 (5+) | IND @ MIA | draftkings | 6.02 | 5.65 | 4.13 | 24.2% | 15.5% | 17.7% | +6.5% | +45.7% | 0.3% |
| Pascal Siakam AST over 6.5 (7+) | IND @ MIA | draftkings | 5.51 | 5.18 | 3.79 | 26.4% | 17.0% | 19.3% | +6.5% | +45.5% | 0.4% |
| Kevin Durant REB over 10.5 (11+) | HOU @ DAL | draftkings | 17.40 | 16.39 | 12.07 | 8.3% | 5.4% | 6.1% | +6.2% | +44.2% | 0.1% |
| Daniss Jenkins AST over 8.5 (9+) | DET @ BKN | draftkings | 21.00 | 19.80 | 14.57 | 6.9% | 4.5% | 5.1% | +6.1% | +44.1% | 0.1% |
| Duncan Robinson AST over 4.5 (5+) | DET @ BKN | draftkings | 9.70 | 9.14 | 6.74 | 14.8% | 9.6% | 10.9% | +6.1% | +44.0% | 0.2% |
| Scottie Barnes AST over 10.5 (11+) | ORL @ TOR | draftkings | 13.60 | 12.89 | 9.58 | 10.4% | 6.9% | 7.8% | +5.6% | +42.0% | 0.1% |
| Tari Eason REB over 12.5 (13+) | HOU @ DAL | draftkings | 23.00 | 21.79 | 16.20 | 6.2% | 4.1% | 4.6% | +5.6% | +42.0% | 0.1% |
| Sam Hauser REB over 6.5 (7+) | CHI @ BOS | draftkings | 11.20 | 10.62 | 7.91 | 12.6% | 8.3% | 9.4% | +5.5% | +41.6% | 0.1% |
| Jabari Smith Jr. REB over 8.5 (9+) | HOU @ DAL | draftkings | 4.17 | 3.96 | 2.95 | 33.9% | 22.4% | 25.3% | +5.4% | +41.3% | 0.4% |
| Bam Adebayo REB over 16.5 (17+) | IND @ MIA | draftkings | 18.40 | 17.45 | 13.03 | 7.7% | 5.1% | 5.7% | +5.4% | +41.2% | 0.1% |
| Nikola Jokic AST over 16.5 (17+) | DEN @ PHX | draftkings | 19.40 | 18.45 | 13.87 | 7.2% | 4.8% | 5.4% | +5.1% | +39.9% | 0.1% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 5.5 (6+) | HOU @ DAL | draftkings | 3.25 | Marcus Smart | 52.7% | 48.1% | +10.8% |
| Khaman Maluach PR under 16.5 | DEN @ PHX | draftkings | 1.84 | Oso Ighodaro | 77.0% | 81.1% | +6.6% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant PR over 34.5 (35+) | HOU @ DAL | draftkings | 3.31 | 3.11 | 2.27 | 44.1% | 28.2% | 32.2% | +6.6% | +45.9% | 0.7% |
| Mikel Brown Jr. 3PM under 1.5 | DET @ BKN | draftkings | 2.30 | 2.17 | 1.59 | 62.8% | 40.6% | 46.2% | +6.2% | +44.5% | 1.2% |
| AJ Dybantsa PTS under 15.5 | CHA @ WAS | draftkings | 1.92 | 1.82 | 1.50 | 66.7% | 51.0% | 54.9% | +5.3% | +27.8% | 1.5% |
| Nolan Traore PA under 13.5 | DET @ BKN | draftkings | 1.93 | 1.84 | 1.38 | 72.3% | 48.3% | 54.3% | +5.1% | +39.9% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play).

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CHA @ WAS | Sat 31 Oct 10:00 | 118.8–111.2 | CHA 71% | 1.42 / 3.40 | WAS +7.5 | 229.5 | WAS +1.5 covers 32%; o218.5 73% |
| CHI @ BOS | Sat 31 Oct 10:30 | 110.0–121.2 | CHI 22% | 4.61 / 1.28 | BOS -11.5 | 231.5 | BOS -14.5 covers 41%; o235.5 41% |
| DET @ BKN | Sat 31 Oct 10:30 | 115.4–103.9 | DET 79% | 1.26 / 4.84 | BKN +11.5 | 219.5 | BKN +7.5 covers 39%; o222.5 43% |
| NYK @ PHI | Sat 31 Oct 10:30 | 115.2–108.6 | NYK 68% | 1.48 / 3.08 | PHI +6.5 | 223.5 | PHI +3.5 covers 41%; o225.5 46% |
| ORL @ TOR | Sat 31 Oct 10:30 | 108.2–117.0 | ORL 27% | 3.72 / 1.37 | TOR -8.5 | 225.5 | TOR -5.5 covers 59%; o226.5 47% |
| IND @ MIA | Sat 31 Oct 11:00 | 116.5–126.6 | IND 24% | 4.24 / 1.31 | MIA -10.5 | 242.5 | MIA -8.5 covers 55%; o237.5 62% |
| HOU @ DAL | Sat 31 Oct 11:00 | 116.3–113.3 | HOU 58% | 1.73 / 2.37 | DAL +3.5 | 229.5 | DAL +5.5 covers 57%; o223.5 63% |
| LAC @ MIN | Sat 31 Oct 11:00 | 112.8–113.2 | LAC 49% | 2.04 / 1.96 | MIN +0.5 | 225.5 | MIN -6.5 covers 34%; o222.5 57% |
| LAL @ GSW | Sat 31 Oct 13:00 | 114.7–114.0 | LAL 52% | 1.91 / 2.09 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| DEN @ PHX | Sat 31 Oct 13:00 | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +3.5 covers 53%; o231.5 43% |

### CHA @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Kon Knueppel (CHA), Coby White (CHA), Grant Williams (CHA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young PTS under 19.5 | CHA @ WAS | pointsbetau | 2.00 | 1.91 | 1.69 | 59.2% | 50.0% | 52.3% | +4.6% | +18.4% | 1.1% |
| Naz Reid PTS under 17.5 | CHA @ WAS | pointsbetau | 2.00 | 1.95 | 1.74 | 57.5% | 49.1% | 51.2% | +2.4% | +15.1% | 0.6% |
| Alex Sarr BLK over 1.5 (2+) | CHA @ WAS | draftkings | 2.73 | 2.67 | 2.12 | 47.2% | 34.2% | 37.5% | +2.3% | +28.8% | 0.3% |
| Alex Sarr PTS over 10.5 (11+) | CHA @ WAS | pointsbetau | 2.10 | 2.06 | 1.98 | 50.5% | 48.0% | 48.6% | +2.1% | +6.1% | 0.5% |
| Kyshawn George PTS over 13.5 (14+) | CHA @ WAS | pointsbetau | 2.15 | 2.11 | 2.00 | 50.0% | 46.5% | 47.4% | +1.9% | +7.5% | 0.4% |
| Brandon Miller PTS under 27.5 | CHA @ WAS | unibet | 1.94 | 1.91 | 1.73 | 57.9% | 50.5% | 52.3% | +1.7% | +12.4% | 0.5% |
| AJ Dybantsa PTS under 14.5 | CHA @ WAS | unibet | 1.94 | 1.91 | 1.63 | 61.2% | 49.4% | 52.3% | +1.7% | +18.9% | 0.5% |
| Anthony Davis BLK over 1.5 (2+) | CHA @ WAS | draftkings | 2.58 | 2.55 | 2.09 | 47.8% | 36.3% | 39.2% | +1.0% | +23.2% | 0.2% |
| Grayson Allen PTS over 14.5 (15+) | CHA @ WAS | draftkings | 1.94 | 1.93 | 1.84 | 54.3% | 51.0% | 51.8% | +0.8% | +5.6% | 0.2% |
| Bilal Coulibaly PTS over 7.5 (8+) | CHA @ WAS | draftkings | 1.97 | 1.96 | 1.61 | 62.2% | 47.4% | 51.1% | +0.7% | +22.5% | 0.2% |
| Dennis Schroder PTS under 14.5 | CHA @ WAS | draftkings | 1.99 | 1.98 | 1.78 | 56.1% | 48.7% | 50.5% | +0.6% | +11.7% | 0.1% |
| Moussa Diabate PTS under 8.5 | CHA @ WAS | pointsbetau | 2.10 | 2.10 | 2.13 | 47.0% | 47.9% | 47.7% | +0.1% | -1.2% | 0.0% |
| Bilal Coulibaly PR over 11.5 (12+) | CHA @ WAS | draftkings | 2.01 | 2.01 | 1.68 | 59.5% | 46.6% | 49.8% | +0.1% | +19.5% | 0.0% |

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 100% | 31.6<br><sub>36,23,36,36,38</sub> | 26.8<br><sub>18,6,34,39,31</sub> | 27.5 · 27.5 | 5.3<br><sub>3,2,8,6,12</sub> | 5.5 | 3.1<br><sub>1,0,4,1,3</sub> | 3.5 | 3.4<br><sub>3,1,3,5,3</sub> | 3.5 | 1.2 | 0.7 | 2.7 | 35.1 |
| Dennis Schroder | 100% | 31.5<br><sub>35,20,38,36,34</sub> | 14.4<br><sub>19,4,25,8,14</sub> | 14.5 · 15.5 | 3.5<br><sub>4,4,6,2,4</sub> | 3.5 | 5.4<br><sub>6,3,4,5,5</sub> | 5.5 | 1.0<br><sub>0,0,3,0,2</sub> | 1.5 | 1.1 | 0.2 | 2.6 | 23.3 |
| Grayson Allen | 96% | 27.9<br><sub>29,20,34,28,30</sub> | 16.2<br><sub>21,11,20,15,9</sub> | 14.5 · 15.5 | 3.3<br><sub>3,2,3,2,5</sub> | 2.5 | 3.5<br><sub>4,3,5,1,2</sub> | 3.5 | 2.7<br><sub>5,3,4,2,2</sub> | 2.5 | 1.2 | 0.3 | 1.9 | 23.1 |
| Moussa Diabate | 100% | 27.9<br><sub>34,21,22,35,35</sub> | 9.5<br><sub>17,5,4,11,9</sub> | 8.5 · 8.5 | 9.6<br><sub>8,8,5,17,9</sub> | 10.5 | 2.5<br><sub>3,1,2,3,2</sub> | 1.5 | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.4 | 21.6 |
| Naz Reid | 100% | 27.0<br><sub>33,25,37,29,13</sub> | 17.1<br><sub>20,17,23,18,7</sub> | 17.5 · 17.5 | 7.7<br><sub>11,6,9,12,6</sub> | 7.5 | 2.4<br><sub>7,2,0,1,0</sub> | 2.5 | 2.3<br><sub>4,3,5,2,1</sub> | 2.5 | 0.9 | 0.9 | 2.2 | 27.2 |
| Sion James | 100% | 24.9<br><sub>27,24,26,29,23</sub> | 6.3<br><sub>3,3,0,5,5</sub> | 5.5 · 5.5 | 3.8<br><sub>3,2,5,2,2</sub> | 3.5 | 2.8<br><sub>0,5,5,3,3</sub> | 2.5 | 0.9<br><sub>1,1,0,1,1</sub> | 1.5 | 1.0 | 0.2 | 0.8 | 13.0 |
| Royce O'Neale | 98% | 20.3<br><sub>17,17,11,7,34</sub> | 6.5<br><sub>8,6,0,0,9</sub> |  | 3.5<br><sub>4,2,1,0,4</sub> |  | 1.4<br><sub>0,0,0,1,0</sub> |  | 1.2<br><sub>2,2,0,0,3</sub> |  | 0.8 | 0.4 | 0.7 | 11.4 |
| Ryan Kalkbrenner | 98% | 16.2<br><sub>14,19,23,13,13</sub> | 6.1<br><sub>4,6,6,6,1</sub> | 5.5 · 5.5 | 4.5<br><sub>5,7,5,4,1</sub> | 4.5 | 0.9<br><sub>3,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.8 | 11.5 |
| Tidjane Salaun | 86% | 15.1<br><sub>-,23,10,16,12</sub> | 5.9<br><sub>-,11,3,5,2</sub> |  | 3.7<br><sub>-,5,3,5,2</sub> |  | 0.8<br><sub>-,1,0,0,0</sub> |  | 0.7<br><sub>-,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 10.4 |
| Christian Anderson | 96% | 11.1<br><sub>13,16,3,11,9</sub> | 5.0<br><sub>0,2,0,3,2</sub> |  | 1.5<br><sub>2,0,1,4,0</sub> |  | 1.3<br><sub>2,2,0,1,1</sub> |  | 0.4<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 1.0 | 7.8 |
| PJ Hall | 38% | 8.8<br><sub>-,10,-,-,-</sub> | 3.7<br><sub>-,0,-,-,-</sub> |  | 3.2<br><sub>-,1,-,-,-</sub> |  | 0.6<br><sub>-,3,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.5 | 0.7 | 7.5 |
| Liam McNeeley | 48% | 8.6<br><sub>3,12,-,-,-</sub> | 3.4<br><sub>0,4,-,-,-</sub> |  | 1.8<br><sub>1,4,-,-,-</sub> |  | 0.6<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.9 |
| Hannes Steinbach | 36% | 8.4<br><sub>-,12,-,-,-</sub> | 3.2<br><sub>-,6,-,-,-</sub> |  | 2.5<br><sub>-,5,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.1 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 100% | 33.6<br><sub>38,37,34,38,34</sub> | 18.8<br><sub>20,22,25,22,14</sub> | 20.5 · 19.5 | 2.8<br><sub>0,1,4,6,5</sub> | 2.5 | 9.3<br><sub>13,12,9,10,8</sub> | 9.5 | 2.3<br><sub>0,4,4,1,1</sub> | 2.5 | 1.1 | 0.2 | 3.2 | 31.0 |
| Anthony Davis | 100% | 33.3<br><sub>34,32,31,36,34</sub> | 20.4<br><sub>34,9,19,29,18</sub> | 21.5 · 21.5 | 9.7<br><sub>12,9,6,10,5</sub> | 9.5 | 2.7<br><sub>4,0,4,0,3</sub> | 2.5 | 0.9<br><sub>1,0,0,3,2</sub> | 0.5 | 1.1 | 1.6 | 2.0 | 32.9 |
| Kyshawn George | 100% | 31.0<br><sub>29,26,36,29,38</sub> | 14.4<br><sub>18,11,22,20,8</sub> | 12.5 · 13.5 | 4.5<br><sub>5,3,9,4,2</sub> | 4.5 | 3.9<br><sub>3,3,5,2,11</sub> | 3.5 | 1.8<br><sub>1,1,0,2,0</sub> | 1.5 | 1.1 | 1.0 | 2.1 | 22.8 |
| AJ Dybantsa | 100% | 27.5<br><sub>-,-,-,-,27</sub> | 13.6<br><sub>-,-,-,-,19</sub> | 15.5 · 15.5 | 3.5<br><sub>-,-,-,-,2</sub> | 4.5 | 2.0<br><sub>-,-,-,-,2</sub> | 2.5 | 1.0<br><sub>-,-,-,-,1</sub> | 1.5 | 1.0 | 0.6 | 1.6 | 19.1 |
| Bilal Coulibaly | 98% | 26.3<br><sub>29,26,25,29,27</sub> | 9.6<br><sub>11,11,7,3,17</sub> | 7.5 · – | 3.9<br><sub>2,6,4,5,2</sub> | 3.5 | 1.8<br><sub>1,0,0,1,0</sub> |  | 0.9<br><sub>1,1,0,0,1</sub> | 0.5 | 1.2 | 0.8 | 1.1 | 15.2 |
| Alex Sarr | 100% | 25.6<br><sub>24,25,23,26,26</sub> | 11.4<br><sub>6,7,10,12,18</sub> | 9.5 · 10.5 | 5.5<br><sub>9,4,2,6,4</sub> | 5.5 | 2.3<br><sub>2,5,3,1,2</sub> | 1.5 | 1.0<br><sub>0,1,0,0,2</sub> |  | 0.8 | 1.6 | 1.3 | 19.2 |
| Bub Carrington | 98% | 20.4<br><sub>19,11,21,28,20</sub> | 6.9<br><sub>10,3,9,6,3</sub> |  | 2.0<br><sub>1,1,2,0,1</sub> |  | 2.9<br><sub>4,0,1,3,3</sub> |  | 1.0<br><sub>2,1,3,2,0</sub> |  | 0.6 | 0.2 | 1.2 | 11.8 |
| Tre Johnson | 66% | 20.0<br><sub>19,26,23,23,-</sub> | 7.9<br><sub>8,20,13,7,-</sub> | 8.5 · 8.5 | 2.4<br><sub>1,2,2,3,-</sub> | 2.5 | 1.3<br><sub>0,0,2,2,-</sub> |  | 1.0<br><sub>0,4,2,1,-</sub> | 1.5 | 0.6 | 0.2 | 0.9 | 11.5 |
| Khris Middleton | 83% | 17.3<br><sub>12,16,-,13,23</sub> | 5.7<br><sub>2,6,-,0,4</sub> |  | 2.4<br><sub>2,2,-,1,3</sub> |  | 1.3<br><sub>0,0,-,0,2</sub> |  | 0.6<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.1 | 1.1 | 9.4 |
| Deandre Ayton | 98% | 14.4<br><sub>15,14,16,12,12</sub> | 5.2<br><sub>11,4,6,0,10</sub> | – · 4.5 | 4.1<br><sub>4,6,5,4,3</sub> |  | 0.6<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.6 | 9.9 |
| Anthony Gill | 38% | 8.3<br><sub>-,1,-,-,-</sub> | 2.9<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Will Riley | 63% | 8.3<br><sub>-,1,5,4,-</sub> | 3.7<br><sub>-,0,2,2,-</sub> |  | 1.1<br><sub>-,0,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.5 |
| Tre Mann | 38% | 6.0<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>


### CHI @ BOS
Out: Devin Carter (BOS), Nic Claxton (CHI), Dailyn Swain (CHI)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Derrick White PTS under 15.5 | CHI @ BOS | draftkings | 1.93 | 1.92 | 1.58 | 63.3% | 48.5% | 52.2% | +0.5% | +21.8% | 0.1% |
| Caleb Wilson RA under 9.5 | CHI @ BOS | draftkings | 1.83 | 1.82 | 1.52 | 65.8% | 51.3% | 54.9% | +0.4% | +20.2% | 0.1% |
| Derrick White PR under 19.5 | CHI @ BOS | draftkings | 1.95 | 1.95 | 1.63 | 61.5% | 47.9% | 51.3% | +0.1% | +20.0% | 0.0% |
| Caleb Wilson REB under 6.5 | CHI @ BOS | draftkings | 2.05 | 2.05 | 1.71 | 58.4% | 45.6% | 48.8% | +0.0% | +19.7% | 0.0% |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson | 96% | 33.6<br><sub>32,33,38,32,38</sub> | 18.2<br><sub>16,21,30,17,20</sub> | 18.5 · – | 6.2<br><sub>4,6,14,5,6</sub> | 6.5 | 2.2<br><sub>0,1,3,3,4</sub> | 2.5 | 1.7<br><sub>1,2,1,1,3</sub> | 1.5 | 1.0 | 1.0 | 2.7 | 26.6 |
| Norman Powell | 97% | 29.7<br><sub>22,33,33,24,37</sub> | 17.6<br><sub>15,25,18,20,30</sub> | 20.5 · – | 3.1<br><sub>5,4,2,1,2</sub> | 3.5 | 2.1<br><sub>1,1,3,2,2</sub> | 1.5 | 2.1<br><sub>2,2,3,4,4</sub> | 2.5 | 1.2 | 0.2 | 2.1 | 22.8 |
| Josh Giddey | 98% | 27.9<br><sub>24,25,30,24,31</sub> | 11.3<br><sub>2,6,9,11,10</sub> | 11.5 · – | 6.3<br><sub>7,4,8,1,8</sub> | 6.5 | 6.6<br><sub>6,9,10,4,11</sub> | 7.5 | 1.4<br><sub>0,0,1,1,1</sub> | 1.5 | 0.8 | 0.5 | 2.5 | 24.1 |
| Matas Buzelis | 98% | 27.5<br><sub>25,17,35,22,33</sub> | 13.9<br><sub>17,7,21,11,17</sub> | 13.5 · – | 5.1<br><sub>6,5,5,1,5</sub> | 5.5 | 1.7<br><sub>0,3,2,2,3</sub> |  | 1.7<br><sub>0,0,2,2,3</sub> | 1.5 | 0.5 | 0.9 | 2.1 | 20.6 |
| Jalen Smith | 98% | 23.2<br><sub>19,24,24,20,30</sub> | 10.9<br><sub>15,14,14,7,17</sub> | 10.5 · – | 6.5<br><sub>8,13,3,6,11</sub> | 7.5 | 1.2<br><sub>1,1,1,1,5</sub> |  | 1.5<br><sub>0,2,2,2,3</sub> | 1.5 | 0.5 | 0.6 | 1.0 | 18.7 |
| Tre Jones | 98% | 18.1<br><sub>13,24,18,15,18</sub> | 10.0<br><sub>13,11,10,8,11</sub> | 8.5 · – | 2.3<br><sub>3,3,2,1,4</sub> | 2.5 | 3.0<br><sub>0,8,3,0,3</sub> | 3.5 | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 15.3 |
| Leonard Miller | 98% | 17.8<br><sub>26,24,21,14,17</sub> | 8.1<br><sub>4,19,7,9,10</sub> | 8.5 · – | 4.0<br><sub>6,3,4,9,0</sub> | 4.5 | 0.9<br><sub>1,2,0,0,1</sub> |  | 0.8<br><sub>0,2,1,1,1</sub> | 1.5 | 0.4 | 0.3 | 0.9 | 12.9 |
| Isaac Okoro | 98% | 16.6<br><sub>18,28,14,11,18</sub> | 5.3<br><sub>4,12,0,1,7</sub> |  | 1.6<br><sub>0,3,1,1,0</sub> |  | 1.0<br><sub>1,1,0,4,1</sub> |  | 0.5<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 7.9 |
| Buddy Hield | 88% | 10.9<br><sub>14,15,16,13,9</sub> | 4.6<br><sub>0,13,9,3,2</sub> |  | 1.5<br><sub>2,2,2,0,3</sub> |  | 0.9<br><sub>2,2,2,1,1</sub> |  | 0.6<br><sub>0,3,1,1,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.9 |
| Noa Essengue | 88% | 9.2<br><sub>10,17,-,16,10</sub> | 3.5<br><sub>1,4,-,0,3</sub> |  | 1.4<br><sub>3,1,-,4,0</sub> |  | 0.4<br><sub>0,1,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.1 | 0.4 | 5.4 |
| Tobe Awaka | 58% | 9.0<br><sub>14,-,-,12,-</sub> | 2.8<br><sub>2,-,-,4,-</sub> |  | 2.4<br><sub>7,-,-,6,-</sub> |  | 0.6<br><sub>2,-,-,0,-</sub> |  | 0.0<br><sub>0,-,-,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 5.8 |
| Zach Collins | 63% | 8.6<br><sub>9,-,11,6,-</sub> | 3.5<br><sub>0,-,2,2,-</sub> |  | 2.5<br><sub>5,-,3,2,-</sub> |  | 0.7<br><sub>0,-,1,0,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.5 | 6.8 |
| Patrick Williams | 48% | 8.4<br><sub>-,-,-,-,-</sub> | 2.7<br><sub>-,-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 4.5 |
| Jaylin Sellers | 52% | 7.4<br><sub>14,-,-,12,-</sub> | 5.1<br><sub>3,-,-,0,-</sub> |  | 1.4<br><sub>1,-,-,0,-</sub> |  | 0.8<br><sub>2,-,-,1,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.6 | 7.3 |
| Jordan Hawkins | 52% | 7.2<br><sub>-,-,-,7,-</sub> | 2.9<br><sub>-,-,-,4,-</sub> |  | 1.0<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.3 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 34.0<br><sub>38,37,28,42</sub> | 27.3<br><sub>13,36,23,40</sub> | 28.5 · – | 9.2<br><sub>4,9,7,5</sub> | 8.5 | 6.8<br><sub>11,7,6,8</sub> | 6.5 | 3.2<br><sub>0,3,2,2</sub> | 2.5 | 1.3 | 0.4 | 2.6 | 43.2 |
| Derrick White | 98% | 30.9<br><sub>36,33,18,33</sub> | 14.2<br><sub>17,12,5,16</sub> | 15.5 · – | 4.1<br><sub>1,4,6,5</sub> | 3.5 | 5.2<br><sub>8,6,4,7</sub> | 5.5 | 2.2<br><sub>3,2,1,1</sub> | 2.5 | 1.2 | 1.0 | 1.8 | 23.4 |
| Paul George | 98% | 30.7<br><sub>31,34,25,36</sub> | 19.3<br><sub>38,15,16,20</sub> | 20.5 · – | 5.7<br><sub>5,7,5,7</sub> | 5.5 | 3.3<br><sub>3,2,2,7</sub> | 3.5 | 2.9<br><sub>7,3,3,1</sub> | 3.5 | 1.7 | 0.4 | 2.1 | 28.3 |
| Payton Pritchard | 98% | 27.0<br><sub>28,30,22,24</sub> | 14.9<br><sub>17,4,28,4</sub> | 15.5 · – | 3.3<br><sub>4,1,1,2</sub> | 2.5 | 4.8<br><sub>1,4,4,6</sub> | 4.5 | 2.3<br><sub>2,1,7,0</sub> | 2.5 | 0.8 | 0.1 | 1.2 | 23.1 |
| Sam Hauser | 98% | 22.1<br><sub>18,23,20,25</sub> | 9.1<br><sub>11,6,11,11</sub> | 8.5 · – | 3.8<br><sub>4,2,4,4</sub> | 2.5 | 1.3<br><sub>1,2,1,0</sub> |  | 1.8<br><sub>3,2,3,3</sub> | 2.5 | 0.5 | 0.2 | 0.5 | 14.2 |
| Mitchell Robinson | 98% | 18.9<br><sub>18,22,16,25</sub> | 6.5<br><sub>4,4,7,7</sub> | 5.5 · – | 7.6<br><sub>3,4,7,5</sub> | 7.5 | 0.7<br><sub>1,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.8 | 1.1 | 0.8 | 14.8 |
| Neemias Queta | 98% | 18.8<br><sub>22,22,19,15</sub> | 8.8<br><sub>3,15,7,7</sub> | 8.5 · – | 6.7<br><sub>4,6,5,3</sub> | 5.5 | 1.3<br><sub>2,1,1,2</sub> |  | 0.1<br><sub>0,1,0,0</sub> |  | 0.7 | 1.3 | 0.9 | 16.8 |
| Jordan Walsh | 96% | 18.5<br><sub>13,20,18,24</sub> | 6.1<br><sub>0,5,4,15</sub> |  | 4.2<br><sub>6,3,3,6</sub> |  | 1.1<br><sub>1,0,2,1</sub> |  | 0.7<br><sub>0,1,0,3</sub> |  | 1.0 | 0.5 | 0.6 | 11.4 |
| Baylor Scheierman | 98% | 17.5<br><sub>18,11,18,21</sub> | 6.0<br><sub>8,2,2,3</sub> |  | 3.4<br><sub>3,0,6,4</sub> |  | 1.5<br><sub>0,0,2,1</sub> |  | 0.9<br><sub>2,0,0,1</sub> |  | 0.8 | 0.1 | 0.6 | 10.9 |
| Luka Garza | 96% | 12.0<br><sub>8,4,13,13</sub> | 6.9<br><sub>2,8,6,2</sub> |  | 3.2<br><sub>2,1,3,4</sub> |  | 0.8<br><sub>0,0,2,0</sub> |  | 0.7<br><sub>0,2,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 11.0 |
| Hugo Gonzalez | 91% | 10.1<br><sub>10,4,24,6</sub> | 3.3<br><sub>0,0,13,0</sub> |  | 2.4<br><sub>3,0,5,2</sub> |  | 0.6<br><sub>0,1,2,0</sub> |  | 0.3<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |
| Dillon Mitchell | 16% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Mike Conley | 52% | 7.9<br><sub>-,-,7,-</sub> | 2.5<br><sub>-,-,6,-</sub> |  | 0.8<br><sub>-,-,0,-</sub> |  | 1.3<br><sub>-,-,0,-</sub> |  | 0.2<br><sub>-,-,2,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.6 |
| Ron Harper Jr. | 48% | 7.2<br><sub>-,-,7,-</sub> | 3.2<br><sub>-,-,3,-</sub> |  | 1.2<br><sub>-,-,1,-</sub> |  | 0.6<br><sub>-,-,0,-</sub> |  | 0.4<br><sub>-,-,1,-</sub> |  | 0.5 | 0.1 | 0.2 | 5.0 |
| Chris Cenac Jr. | 47% | 6.0<br><sub>-,-,5,-</sub> | 2.6<br><sub>-,-,3,-</sub> |  | 1.1<br><sub>-,-,1,-</sub> |  | 0.4<br><sub>-,-,0,-</sub> |  | 0.3<br><sub>-,-,1,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.1 |
| Amari Williams | 16% | 5.6 | 1.7 |  | 1.9 |  | 0.4 |  | 0.0 |  | 0.2 | 0.4 | 0.4 | 3.9 |

</details>


### DET @ BKN
Out: Egor Demin (BKN), Grant Nelson (BKN), Ben Saraf (BKN), Jalen Duren (DET), Isaiah Joe (DET)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle REB over 6.5 (7+) | DET @ BKN | draftkings | 2.06 | 2.04 | 1.69 | 59.1% | 45.6% | 49.0% | +0.9% | +21.8% | 0.2% |
| John Collins REB under 6.5 | DET @ BKN | draftkings | 2.07 | 2.06 | 1.71 | 58.6% | 45.1% | 48.5% | +0.4% | +21.4% | 0.1% |
| Nolan Traore AST under 3.5 | DET @ BKN | draftkings | 1.83 | 1.83 | 1.53 | 65.4% | 51.0% | 54.6% | +0.1% | +19.8% | 0.0% |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 34.4<br><sub>35,30,33,36,39</sub> | 25.6<br><sub>22,16,26,19,30</sub> | 23.5 · – | 5.4<br><sub>4,2,8,9,5</sub> | 5.5 | 8.5<br><sub>8,8,8,8,7</sub> | 9.5 | 2.1<br><sub>1,2,3,2,4</sub> | 1.5 | 1.4 | 0.9 | 4.4 | 39.6 |
| Duncan Robinson | 98% | 30.7<br><sub>28,28,32,33,32</sub> | 15.0<br><sub>21,17,21,12,13</sub> | 13.5 · – | 2.8<br><sub>2,1,3,0,2</sub> | 2.5 | 2.7<br><sub>2,2,3,2,2</sub> | 2.5 | 2.9<br><sub>5,5,5,2,3</sub> | 3.5 | 1.1 | 0.3 | 1.3 | 20.6 |
| Paul Reed | 96% | 27.6<br><sub>17,26,23,26,38</sub> | 15.9<br><sub>6,19,8,22,16</sub> | 15.5 · – | 8.6<br><sub>6,11,8,9,4</sub> | 8.5 | 2.5<br><sub>2,3,2,3,0</sub> | 2.5 | 0.5<br><sub>0,2,0,1,2</sub> |  | 1.5 | 1.6 | 1.9 | 26.9 |
| Ausar Thompson | 98% | 27.3<br><sub>33,19,-,25,29</sub> | 9.7<br><sub>11,4,-,11,7</sub> | 10.5 · – | 6.5<br><sub>11,3,-,6,9</sub> | 6.5 | 4.0<br><sub>5,5,-,2,8</sub> | 3.5 | 0.1<br><sub>0,0,-,0,0</sub> |  | 2.0 | 1.4 | 2.0 | 20.3 |
| John Collins | 98% | 26.2<br><sub>25,29,34,27,18</sub> | 11.8<br><sub>6,23,16,2,4</sub> | 14.5 · – | 6.1<br><sub>5,7,11,9,2</sub> | 6.5 | 1.2<br><sub>1,1,0,1,0</sub> |  | 1.1<br><sub>0,5,2,0,0</sub> | 1.5 | 0.8 | 0.9 | 1.4 | 19.1 |
| Daniss Jenkins | 98% | 26.2<br><sub>15,22,38,24,24</sub> | 11.8<br><sub>3,15,18,11,14</sub> | 10.5 · – | 3.4<br><sub>2,5,8,3,2</sub> | 2.5 | 4.5<br><sub>3,5,6,2,3</sub> | 3.5 | 1.3<br><sub>1,1,3,1,2</sub> | 1.5 | 1.0 | 0.3 | 1.8 | 19.7 |
| Kevin Huerter | 93% | 21.0<br><sub>18,20,26,16,19</sub> | 8.5<br><sub>3,5,9,7,3</sub> | 7.5 · – | 2.9<br><sub>3,6,3,1,2</sub> |  | 2.5<br><sub>2,2,2,0,3</sub> |  | 1.1<br><sub>1,1,1,1,1</sub> | 1.5 | 1.0 | 0.3 | 1.0 | 13.9 |
| Javonte Green | 93% | 20.8<br><sub>18,13,22,17,21</sub> | 7.4<br><sub>19,5,2,3,7</sub> |  | 3.3<br><sub>4,3,3,1,2</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 1.1<br><sub>5,1,0,1,1</sub> |  | 1.4 | 0.5 | 0.7 | 11.6 |
| Ronald Holland II | 96% | 16.4<br><sub>3,22,23,12,12</sub> | 6.3<br><sub>0,8,2,4,0</sub> |  | 3.6<br><sub>1,5,9,3,2</sub> |  | 1.3<br><sub>1,4,4,2,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.5 | 1.0 | 11.3 |
| Taurean Prince | 66% | 11.5<br><sub>-,-,-,7,6</sub> | 4.2<br><sub>-,-,-,3,1</sub> |  | 1.8<br><sub>-,-,-,0,2</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,1,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.8 |
| Elijah Harkless | 38% | 7.5<br><sub>-,-,-,3,-</sub> | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.3 | 0.4 | 1.2 |
| Tolu Smith | 76% | 7.5<br><sub>-,2,3,6,1</sub> | 3.1<br><sub>-,0,0,1,2</sub> |  | 2.4<br><sub>-,1,1,4,1</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 6.0 |
| Isaac Jones | 38% | 7.4<br><sub>-,-,-,3,-</sub> | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 1.2 |
| Ebuka Okorie | 52% | 6.6<br><sub>-,-,2,4,-</sub> | 2.1<br><sub>-,-,2,0,-</sub> |  | 0.2<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 3.1 |
| Chaz Lanier | 38% | 6.6<br><sub>-,-,-,2,-</sub> | 2.6<br><sub>-,-,-,2,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.7 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 98% | 34.9<br><sub>38,35,24,44</sub> | 19.2<br><sub>33,23,10,24</sub> | 19.5 · – | 7.5<br><sub>8,6,7,9</sub> | 6.5 | 5.3<br><sub>7,5,7,4</sub> | 4.5 | 1.3<br><sub>3,2,0,0</sub> | 1.5 | 1.1 | 0.3 | 3.4 | 32.0 |
| Michael Porter Jr. | 98% | 32.5<br><sub>34,33,21,40</sub> | 20.4<br><sub>26,28,10,27</sub> | 21.5 · – | 6.6<br><sub>7,9,0,12</sub> | 6.5 | 2.3<br><sub>1,1,0,2</sub> | 1.5 | 2.6<br><sub>5,4,0,6</sub> | 3.5 | 1.3 | 0.5 | 2.3 | 29.3 |
| Keon Ellis | 91% | 23.6<br><sub>34,22,23,25</sub> | 6.6<br><sub>7,6,9,2</sub> | 6.5 · – | 2.1<br><sub>2,2,1,3</sub> | 2.5 | 1.8<br><sub>4,1,3,4</sub> |  | 0.9<br><sub>1,2,1,0</sub> | 1.5 | 1.4 | 0.7 | 0.8 | 10.5 |
| Mikel Brown Jr. | 91% | 22.6<br><sub>20,20,-,28</sub> | 10.0<br><sub>6,8,-,17</sub> | 11.5 · – | 2.9<br><sub>3,2,-,5</sub> | 2.5 | 3.7<br><sub>3,5,-,5</sub> | 3.5 | 1.3<br><sub>1,2,-,4</sub> | 1.5 | 0.7 | 0.2 | 1.6 | 16.6 |
| Noah Clowney | 98% | 21.5<br><sub>22,20,20,24</sub> | 7.7<br><sub>9,4,9,3</sub> | 6.5 · – | 3.7<br><sub>3,4,5,4</sub> | 3.5 | 1.0<br><sub>1,0,1,1</sub> |  | 1.1<br><sub>1,1,1,1</sub> | 1.5 | 0.7 | 0.6 | 0.9 | 12.4 |
| Chaney Johnson | 88% | 21.3<br><sub>5,27,21,29</sub> | 7.9<br><sub>0,10,4,15</sub> |  | 3.2<br><sub>1,5,5,3</sub> |  | 1.2<br><sub>0,3,0,2</sub> |  | 1.0<br><sub>0,2,0,3</sub> |  | 0.7 | 0.3 | 1.1 | 12.3 |
| Day'Ron Sharpe | 98% | 19.7<br><sub>30,23,16,17</sub> | 8.5<br><sub>8,7,11,4</sub> | 8.5 · – | 6.5<br><sub>8,8,4,6</sub> | 6.5 | 2.1<br><sub>3,1,1,0</sub> | 2.5 | 0.3<br><sub>0,1,1,0</sub> |  | 0.9 | 0.7 | 1.6 | 17.1 |
| Nolan Traore | 98% | 18.6<br><sub>16,5,25,24</sub> | 7.8<br><sub>3,3,17,15</sub> | 10.5 · – | 1.6<br><sub>2,2,2,1</sub> |  | 3.0<br><sub>0,0,5,3</sub> | 3.5 | 0.8<br><sub>0,0,2,1</sub> |  | 0.8 | 0.4 | 1.8 | 12.4 |
| Moritz Wagner | 88% | 16.9<br><sub>16,14,15,22</sub> | 9.1<br><sub>7,6,13,15</sub> | 7.5 · – | 3.9<br><sub>0,4,3,4</sub> | 2.5 | 1.4<br><sub>1,1,1,3</sub> |  | 0.7<br><sub>1,1,2,2</sub> | 0.5 | 0.6 | 0.3 | 1.1 | 14.3 |
| Josh Minott | 58% | 13.0<br><sub>-,9,21,-</sub> | 6.1<br><sub>-,4,15,-</sub> |  | 2.4<br><sub>-,2,8,-</sub> |  | 0.8<br><sub>-,0,2,-</sub> |  | 0.8<br><sub>-,0,3,-</sub> |  | 0.8 | 0.5 | 0.8 | 9.3 |
| Danny Wolf | 52% | 12.5<br><sub>-,-,15,-</sub> | 4.9<br><sub>-,-,6,-</sub> |  | 2.9<br><sub>-,-,2,-</sub> |  | 1.2<br><sub>-,-,1,-</sub> |  | 0.5<br><sub>-,-,2,-</sub> |  | 0.3 | 0.4 | 0.8 | 9.0 |
| Terance Mann | 35% | 12.2<br><sub>-,-,-,-</sub> | 3.6<br><sub>-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-</sub> |  | 1.2<br><sub>-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.4 |
| Drake Powell | 58% | 12.1<br><sub>-,-,12,-</sub> | 3.7<br><sub>-,-,0,-</sub> |  | 1.0<br><sub>-,-,2,-</sub> |  | 0.8<br><sub>-,-,3,-</sub> |  | 0.3<br><sub>-,-,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 5.5 |

</details>


### NYK @ PHI
Out: Dominick Barlow (PHI), Jaylen Brown (PHI), Ariel Hukporti (PHI), Jose Alvarado (NYK)

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 36.1<br><sub>34,37,32,36,35</sub> | 26.3<br><sub>21,19,28,23,38</sub> | 26.5 · – | 3.4<br><sub>5,2,3,1,1</sub> | 2.5 | 6.2<br><sub>3,4,4,7,7</sub> | 5.5 | 2.4<br><sub>1,2,1,0,6</sub> | 1.5 | 0.9 | 0.2 | 2.8 | 35.9 |
| OG Anunoby | 98% | 34.8<br><sub>32,34,35,36,31</sub> | 18.4<br><sub>10,20,22,13,23</sub> | 16.5 · – | 6.2<br><sub>5,10,3,7,6</sub> | 5.5 | 2.0<br><sub>0,8,2,2,1</sub> | 1.5 | 2.3<br><sub>1,2,3,1,2</sub> | 2.5 | 1.4 | 0.9 | 1.7 | 26.6 |
| Josh Hart | 98% | 33.6<br><sub>30,36,35,27,36</sub> | 11.1<br><sub>14,10,13,6,2</sub> | 10.5 · – | 8.2<br><sub>7,12,8,4,8</sub> | 7.5 | 4.2<br><sub>3,5,2,4,3</sub> | 3.5 | 1.5<br><sub>2,2,3,2,0</sub> | 1.5 | 1.4 | 0.3 | 1.9 | 23.5 |
| Karl-Anthony Towns | 98% | 31.9<br><sub>24,37,33,33,28</sub> | 19.4<br><sub>19,22,22,27,19</sub> | 19.5 · – | 12.8<br><sub>12,10,14,20,13</sub> | 12.5 | 3.9<br><sub>1,3,4,3,5</sub> | 3.5 | 1.6<br><sub>3,2,0,1,3</sub> | 1.5 | 0.9 | 0.8 | 2.9 | 36.1 |
| Mikal Bridges | 98% | 29.4<br><sub>33,22,35,32,13</sub> | 10.4<br><sub>4,0,6,12,3</sub> | 9.5 · – | 3.0<br><sub>3,1,5,3,0</sub> | 2.5 | 2.5<br><sub>1,4,1,4,0</sub> | 2.5 | 1.2<br><sub>0,0,0,4,1</sub> | 1.5 | 0.9 | 0.5 | 1.0 | 15.9 |
| Landry Shamet | 98% | 26.6<br><sub>25,21,22,28,32</sub> | 9.3<br><sub>5,8,6,13,14</sub> | 7.5 · – | 2.2<br><sub>2,2,2,2,1</sub> |  | 1.6<br><sub>4,0,1,3,5</sub> | 1.5 | 1.7<br><sub>1,2,2,3,4</sub> | 1.5 | 0.6 | 0.2 | 0.9 | 13.0 |
| Miles McBride | 98% | 17.2<br><sub>14,30,13,17,14</sub> | 6.2<br><sub>3,20,1,5,3</sub> | 5.5 · – | 1.6<br><sub>1,2,1,1,5</sub> |  | 1.3<br><sub>1,1,1,1,0</sub> | 1.5 | 1.0<br><sub>1,6,0,1,1</sub> | 1.5 | 0.5 | 0.2 | 0.5 | 9.1 |
| Tyler Kolek | 64% | 14.8<br><sub>-,-,15,11,18</sub> | 5.2<br><sub>-,-,0,2,9</sub> |  | 1.9<br><sub>-,-,3,1,2</sub> |  | 3.9<br><sub>-,-,9,3,9</sub> |  | 0.6<br><sub>-,-,0,0,3</sub> |  | 0.5 | 0.2 | 0.9 | 10.9 |
| Andre Drummond | 98% | 14.1<br><sub>24,7,7,14,15</sub> | 5.4<br><sub>12,2,4,10,4</sub> |  | 6.4<br><sub>14,2,3,8,11</sub> |  | 1.2<br><sub>4,0,2,1,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 13.0 |
| Jordan Clarkson | 72% | 12.5<br><sub>8,3,5,-,17</sub> | 6.0<br><sub>4,0,0,-,18</sub> |  | 1.8<br><sub>1,1,1,-,3</sub> |  | 1.0<br><sub>1,0,0,-,1</sub> |  | 0.4<br><sub>0,0,0,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 8.7 |
| Tyler Nickel | 16% | 8.5 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.5 | 5.9 |
| Mohamed Diawara | 38% | 7.8<br><sub>-,-,-,1,-</sub> | 2.7<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Dalton Knecht | 38% | 7.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.3 | 5.3 |
| Jaden Akins | 48% | 7.6<br><sub>-,-,-,2,-</sub> | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.1 |
| James Wiseman | 63% | 7.1<br><sub>-,2,7,1,-</sub> | 2.5<br><sub>-,0,0,0,-</sub> |  | 2.1<br><sub>-,0,2,1,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.1 |
| Pacome Dadiet | 38% | 6.4<br><sub>-,-,-,1,-</sub> | 2.7<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.3 | 4.5 |

</details>

<details><summary>PHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tyrese Maxey | 98% | 38.4<br><sub>40,42,36,34,36</sub> | 24.5<br><sub>28,32,26,29,27</sub> | 25.5 · – | 3.8<br><sub>4,3,4,5,5</sub> | 3.5 | 5.5<br><sub>5,6,4,4,4</sub> | 4.5 | 2.5<br><sub>2,2,4,1,3</sub> | 2.5 | 1.5 | 0.7 | 2.6 | 33.8 |
| Joel Embiid | 98% | 35.8<br><sub>33,34,36,-,39</sub> | 23.8<br><sub>13,24,28,-,21</sub> | 24.5 · – | 8.6<br><sub>11,7,11,-,11</sub> | 8.5 | 4.8<br><sub>6,1,10,-,2</sub> | 4.5 | 1.4<br><sub>2,1,0,-,0</sub> | 1.5 | 0.7 | 1.3 | 3.3 | 37.2 |
| LeBron James | 98% | 35.2<br><sub>34,33,-,33,33</sub> | 18.4<br><sub>14,17,-,18,13</sub> | 17.5 · – | 6.4<br><sub>9,10,-,2,5</sub> | 6.5 | 6.7<br><sub>7,5,-,5,10</sub> | 6.5 | 1.4<br><sub>0,1,-,0,2</sub> | 1.5 | 1.2 | 0.7 | 3.0 | 31.5 |
| VJ Edgecombe | 76% | 34.6<br><sub>35,33,30,-,29</sub> | 13.7<br><sub>9,11,17,-,8</sub> | 13.5 · – | 6.0<br><sub>4,7,13,-,7</sub> | 5.5 | 3.3<br><sub>1,6,2,-,2</sub> | 2.5 | 1.8<br><sub>0,1,5,-,1</sub> | 1.5 | 1.2 | 0.5 | 1.7 | 23.0 |
| Anfernee Simons | 96% | 26.5<br><sub>25,17,20,27,27</sub> | 11.2<br><sub>13,2,4,5,20</sub> | 11.5 · – | 2.4<br><sub>2,3,1,3,3</sub> | 2.5 | 1.9<br><sub>0,0,2,3,1</sub> | 1.5 | 2.0<br><sub>3,0,1,1,6</sub> | 2.5 | 0.6 | 0.2 | 1.1 | 15.5 |
| Kentavious Caldwell-Pope | 98% | 26.1<br><sub>26,25,28,31,21</sub> | 7.9<br><sub>10,3,12,7,4</sub> | 6.5 · – | 2.6<br><sub>4,3,2,3,2</sub> | 2.5 | 1.8<br><sub>1,2,1,3,1</sub> | 1.5 | 1.1<br><sub>2,1,4,1,0</sub> | 1.5 | 0.9 | 0.3 | 0.9 | 12.3 |
| Dean Wade | 86% | 24.6<br><sub>-,-,28,37,17</sub> | 4.8<br><sub>-,-,7,7,0</sub> | 5.5 · – | 3.2<br><sub>-,-,2,5,1</sub> | 3.5 | 1.1<br><sub>-,-,0,1,1</sub> |  | 0.7<br><sub>-,-,2,1,0</sub> | 1.5 | 0.8 | 0.3 | 0.6 | 9.0 |
| Rayan Rupert | 30% | 13.1<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.7 | 7.6 |
| Adem Bona | 96% | 12.5<br><sub>10,14,10,25,4</sub> | 3.5<br><sub>0,2,0,6,1</sub> |  | 3.2<br><sub>3,2,1,13,1</sub> |  | 0.4<br><sub>1,0,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 7.0 |
| Labaron Philon Jr. | 52% | 10.2<br><sub>-,-,4,13,-</sub> | 3.5<br><sub>-,-,0,5,-</sub> |  | 1.3<br><sub>-,-,0,2,-</sub> |  | 0.7<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,1,-</sub> |  | 0.2 | 0.1 | 0.6 | 5.4 |
| Justin Edwards | 38% | 8.9<br><sub>-,-,1,-,-</sub> | 3.3<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.9 |
| Caleb Love | 43% | 7.6<br><sub>-,-,1,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.2 |

</details>


### ORL @ TOR
Out: Kawhi Leonard (TOR), Malachi Smith (TOR), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane 3PM under 2.5 | ORL @ TOR | draftkings | 2.12 | 2.11 | 1.74 | 57.5% | 44.1% | 47.4% | +0.5% | +21.8% | 0.1% |
| Franz Wagner RA under 12.5 | ORL @ TOR | draftkings | 1.87 | 1.86 | 1.55 | 64.4% | 50.1% | 53.7% | +0.3% | +20.3% | 0.1% |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane | 98% | 34.6<br><sub>33,27,35,34</sub> | 19.7<br><sub>18,5,22,13</sub> | 19.5 · – | 4.4<br><sub>5,2,6,5</sub> | 4.5 | 3.8<br><sub>2,0,2,4</sub> | 3.5 | 2.4<br><sub>3,1,4,2</sub> | 2.5 | 1.3 | 0.4 | 2.8 | 27.9 |
| Franz Wagner | 98% | 33.7<br><sub>29,33,37,34</sub> | 22.5<br><sub>22,18,23,15</sub> | 22.5 · – | 6.0<br><sub>6,6,13,4</sub> | 6.5 | 5.3<br><sub>5,5,9,5</sub> | 6.5 | 1.4<br><sub>2,1,0,0</sub> | 1.5 | 1.2 | 0.4 | 3.2 | 33.8 |
| Wendell Carter Jr. | 98% | 31.8<br><sub>31,29,33,26</sub> | 11.3<br><sub>22,20,9,3</sub> | 10.5 · – | 7.6<br><sub>7,9,10,10</sub> | 7.5 | 2.3<br><sub>0,1,2,3</sub> | 2.5 | 0.9<br><sub>1,3,0,0</sub> | 0.5 | 0.8 | 0.8 | 1.7 | 21.1 |
| Tristan da Silva | 98% | 30.5<br><sub>28,29,27,31</sub> | 12.6<br><sub>14,5,19,20</sub> | 12.5 · – | 4.3<br><sub>2,3,2,3</sub> | 3.5 | 2.1<br><sub>3,1,2,1</sub> | 1.5 | 1.7<br><sub>4,1,5,4</sub> | 2.5 | 0.9 | 0.4 | 1.4 | 19.0 |
| Anthony Black | 97% | 29.9<br><sub>-,-,26,22</sub> | 14.4<br><sub>-,-,18,8</sub> | 14.5 · – | 3.6<br><sub>-,-,3,2</sub> | 3.5 | 3.5<br><sub>-,-,5,1</sub> | 3.5 | 1.5<br><sub>-,-,5,0</sub> | 1.5 | 1.5 | 0.7 | 2.3 | 21.5 |
| Jase Richardson | 88% | 18.7<br><sub>14,14,17,14</sub> | 7.6<br><sub>2,6,6,10</sub> | 7.5 · – | 2.0<br><sub>2,1,1,1</sub> |  | 1.8<br><sub>3,3,0,1</sub> | 2.5 | 0.8<br><sub>0,1,2,2</sub> | 0.5 | 0.6 | 0.1 | 1.1 | 11.4 |
| Jevon Carter | 58% | 18.6<br><sub>-,13,-,22</sub> | 6.2<br><sub>-,0,-,6</sub> |  | 1.8<br><sub>-,1,-,0</sub> |  | 1.8<br><sub>-,1,-,3</sub> |  | 1.0<br><sub>-,0,-,2</sub> |  | 0.8 | 0.2 | 0.8 | 9.8 |
| Jamal Cain | 97% | 18.2<br><sub>14,11,15,16</sub> | 6.9<br><sub>0,0,5,9</sub> |  | 3.1<br><sub>0,1,5,1</sub> |  | 0.9<br><sub>0,0,0,0</sub> |  | 0.6<br><sub>0,0,1,0</sub> |  | 0.6 | 0.2 | 0.9 | 10.9 |
| Nikola Vucevic | 96% | 15.6<br><sub>5,4,15,16</sub> | 6.0<br><sub>0,0,5,5</sub> |  | 4.2<br><sub>1,2,3,4</sub> |  | 1.8<br><sub>1,0,3,2</sub> |  | 0.6<br><sub>0,0,1,0</sub> |  | 0.4 | 0.5 | 0.8 | 12.0 |
| Goga Bitadze | 71% | 14.7<br><sub>12,12,-,11</sub> | 5.4<br><sub>6,4,-,6</sub> |  | 4.7<br><sub>6,3,-,0</sub> |  | 1.2<br><sub>1,0,-,1</sub> |  | 0.0<br><sub>0,0,-,0</sub> |  | 0.5 | 0.9 | 0.9 | 11.2 |
| Colin Castleton | 58% | 9.6<br><sub>-,4,-,7</sub> | 3.0<br><sub>-,7,-,2</sub> |  | 2.8<br><sub>-,2,-,2</sub> |  | 0.6<br><sub>-,1,-,0</sub> |  | 0.1<br><sub>-,0,-,0</sub> |  | 0.2 | 0.2 | 0.7 | 6.4 |
| Alex Morales | 58% | 8.7<br><sub>-,4,-,7</sub> | 2.9<br><sub>-,0,-,2</sub> |  | 1.4<br><sub>-,1,-,2</sub> |  | 1.1<br><sub>-,0,-,1</sub> |  | 0.2<br><sub>-,0,-,0</sub> |  | 0.4 | 0.1 | 0.9 | 5.3 |

</details>

<details><summary>TOR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Scottie Barnes | 98% | 34.1<br><sub>26,37,28,31</sub> | 22.7<br><sub>23,28,0,28</sub> | 21.5 · – | 7.2<br><sub>6,14,3,6</sub> | 7.5 | 6.7<br><sub>5,5,3,4</sub> | 5.5 | 1.0<br><sub>1,1,0,0</sub> | 1.5 | 1.6 | 1.5 | 3.2 | 36.5 |
| RJ Barrett | 98% | 34.0<br><sub>26,34,32,32</sub> | 24.2<br><sub>20,23,20,25</sub> | 22.5 · – | 6.3<br><sub>4,9,2,9</sub> | 5.5 | 3.8<br><sub>3,4,2,6</sub> | 3.5 | 1.9<br><sub>0,1,0,3</sub> | 1.5 | 0.9 | 0.4 | 2.6 | 34.4 |
| Immanuel Quickley | 98% | 30.0<br><sub>28,29,28,29</sub> | 16.9<br><sub>23,12,19,16</sub> | 17.5 · – | 3.7<br><sub>4,1,3,3</sub> | 3.5 | 5.5<br><sub>7,6,2,7</sub> | 5.5 | 2.5<br><sub>4,0,3,4</sub> | 2.5 | 1.3 | 0.1 | 1.8 | 26.1 |
| Ja'Kobe Walter | 98% | 28.7<br><sub>23,24,31,28</sub> | 12.2<br><sub>10,7,22,14</sub> | 12.5 · – | 3.6<br><sub>3,4,4,5</sub> | 3.5 | 1.7<br><sub>4,2,2,2</sub> | 1.5 | 2.1<br><sub>1,2,5,3</sub> | 2.5 | 1.6 | 0.3 | 0.9 | 17.5 |
| Jamal Shead | 98% | 25.7<br><sub>16,24,21,23</sub> | 8.0<br><sub>2,5,4,13</sub> | 7.5 · – | 1.8<br><sub>2,2,1,4</sub> | 2.5 | 5.2<br><sub>5,5,0,7</sub> | 4.5 | 0.9<br><sub>0,0,0,1</sub> | 0.5 | 1.1 | 0.2 | 2.0 | 15.1 |
| Collin Murray-Boyles | 98% | 22.6<br><sub>20,18,19,15</sub> | 9.4<br><sub>6,8,3,10</sub> | 9.5 · – | 5.6<br><sub>8,3,7,2</sub> | 5.5 | 1.9<br><sub>3,0,2,1</sub> | 1.5 | 0.4<br><sub>0,0,0,2</sub> |  | 1.0 | 1.0 | 1.3 | 16.9 |
| Jakob Poeltl | 98% | 21.7<br><sub>22,27,19,10</sub> | 7.1<br><sub>3,6,0,2</sub> | 7.5 · – | 6.1<br><sub>6,9,1,2</sub> | 5.5 | 1.4<br><sub>0,2,0,0</sub> | 1.5 | 0.0<br><sub>0,0,0,0</sub> |  | 0.8 | 1.0 | 1.2 | 14.5 |
| Jamison Battle | 96% | 17.6<br><sub>11,12,13,20</sub> | 6.8<br><sub>8,5,4,7</sub> |  | 2.8<br><sub>5,0,1,0</sub> |  | 0.8<br><sub>0,0,2,1</sub> |  | 1.0<br><sub>2,1,1,1</sub> |  | 0.4 | 0.2 | 0.6 | 10.4 |
| Allen Graves | 93% | 16.8<br><sub>19,6,20,18</sub> | 5.4<br><sub>5,2,11,3</sub> |  | 3.6<br><sub>5,2,6,1</sub> |  | 0.9<br><sub>0,0,4,0</sub> |  | 0.4<br><sub>0,0,1,0</sub> |  | 0.6 | 0.9 | 0.7 | 9.9 |
| Trayce Jackson-Davis | 88% | 13.6<br><sub>10,1,6,20</sub> | 5.0<br><sub>9,0,3,6</sub> |  | 4.4<br><sub>1,0,1,11</sub> |  | 0.9<br><sub>0,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.5 | 0.8 | 0.7 | 10.3 |
| Kyle Anderson | 72% | 12.3<br><sub>5,-,11,5</sub> | 3.3<br><sub>0,-,0,0</sub> |  | 2.4<br><sub>1,-,2,0</sub> |  | 1.8<br><sub>2,-,0,1</sub> |  | 0.0<br><sub>0,-,0,0</sub> |  | 0.6 | 0.4 | 0.7 | 7.5 |
| Alijah Martin | 93% | 7.3<br><sub>5,1,7,5</sub> | 2.8<br><sub>3,0,2,5</sub> |  | 1.1<br><sub>0,0,2,1</sub> |  | 0.6<br><sub>0,0,1,1</sub> |  | 0.2<br><sub>0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Jaden Bradley | 93% | 7.0<br><sub>5,1,5,5</sub> | 2.3<br><sub>0,0,6,0</sub> |  | 1.2<br><sub>0,0,1,1</sub> |  | 0.6<br><sub>0,0,1,1</sub> |  | 0.1<br><sub>0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.0 |

</details>


### IND @ MIA
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND), Obi Toppin (IND), Ivica Zubac (IND)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Bam Adebayo PA over 21.5 (22+) | IND @ MIA | draftkings | 1.96 | 1.92 | 1.70 | 58.8% | 50.0% | 52.2% | +2.4% | +15.3% | 0.6% |
| Bam Adebayo 3PM over 1.5 (2+) | IND @ MIA | draftkings | 2.51 | 2.49 | 2.06 | 48.5% | 37.3% | 40.1% | +0.7% | +21.9% | 0.1% |
| Bam Adebayo STL over 1.5 (2+) | IND @ MIA | draftkings | 2.71 | 2.69 | 2.22 | 45.0% | 34.5% | 37.2% | +0.7% | +21.9% | 0.1% |
| Aaron Nesmith PTS over 13.5 (14+) | IND @ MIA | draftkings | 1.86 | 1.85 | 1.53 | 65.2% | 50.3% | 54.0% | +0.6% | +21.4% | 0.2% |
| Aaron Nesmith PR over 17.5 (18+) | IND @ MIA | draftkings | 1.88 | 1.87 | 1.55 | 64.6% | 49.8% | 53.5% | +0.4% | +21.4% | 0.1% |
| Kelly Oubre Jr. PR over 15.5 (16+) | IND @ MIA | draftkings | 1.81 | 1.81 | 1.51 | 66.2% | 51.6% | 55.3% | +0.2% | +20.0% | 0.1% |
| Pascal Siakam PRA over 35.5 (36+) | IND @ MIA | draftkings | 1.84 | 1.84 | 1.54 | 64.8% | 51.0% | 54.4% | +0.1% | +19.2% | 0.1% |
| Pascal Siakam AST over 4.5 (5+) | IND @ MIA | draftkings | 2.16 | 2.16 | 1.80 | 55.5% | 43.3% | 46.3% | +0.0% | +19.8% | 0.0% |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Andrew Nembhard | 76% | 35.1<br><sub>34,32,30,-,35</sub> | 20.2<br><sub>18,16,14,-,18</sub> | 17.5 · – | 3.6<br><sub>2,2,1,-,3</sub> | 2.5 | 9.6<br><sub>9,5,3,-,14</sub> | 9.5 | 2.1<br><sub>0,1,4,-,1</sub> | 1.5 | 1.2 | 0.2 | 3.2 | 33.5 |
| Pascal Siakam | 98% | 35.0<br><sub>35,29,26,37,34</sub> | 28.0<br><sub>30,23,21,20,26</sub> | 23.5 · – | 8.2<br><sub>8,3,7,13,11</sub> | 7.5 | 5.1<br><sub>1,3,6,6,3</sub> | 4.5 | 1.9<br><sub>1,3,3,1,0</sub> | 1.5 | 1.2 | 0.4 | 3.2 | 41.3 |
| Kelly Oubre Jr. | 98% | 30.1<br><sub>28,20,20,23,30</sub> | 13.9<br><sub>4,3,14,9,15</sub> | 11.5 · – | 5.1<br><sub>2,2,2,3,3</sub> | 4.5 | 2.0<br><sub>3,2,2,1,1</sub> |  | 1.3<br><sub>0,1,1,1,1</sub> | 1.5 | 1.1 | 0.5 | 1.5 | 21.0 |
| Aaron Nesmith | 98% | 29.3<br><sub>-,20,19,21,27</sub> | 17.2<br><sub>-,9,13,13,18</sub> | 13.5 · – | 4.1<br><sub>-,4,1,0,2</sub> | 3.5 | 2.1<br><sub>-,1,2,1,1</sub> |  | 2.4<br><sub>-,1,2,3,3</sub> | 1.5 | 0.8 | 0.5 | 1.8 | 23.5 |
| Jarace Walker | 96% | 27.9<br><sub>19,17,19,29,22</sub> | 13.3<br><sub>3,2,6,10,7</sub> | 10.5 · – | 6.5<br><sub>6,1,7,8,8</sub> | 5.5 | 3.2<br><sub>2,1,1,2,1</sub> |  | 1.7<br><sub>1,0,0,2,1</sub> | 1.5 | 0.9 | 0.4 | 2.2 | 23.0 |
| Quenton Jackson | 97% | 24.8<br><sub>16,17,18,27,14</sub> | 11.3<br><sub>6,8,5,4,2</sub> |  | 3.4<br><sub>4,1,1,2,2</sub> |  | 4.9<br><sub>1,3,2,4,6</sub> |  | 0.9<br><sub>0,1,0,0,0</sub> |  | 1.0 | 0.2 | 1.5 | 19.6 |
| Jay Huff | 88% | 22.7<br><sub>-,5,21,23,16</sub> | 9.6<br><sub>-,0,14,6,3</sub> | 8.5 · – | 4.5<br><sub>-,2,2,6,6</sub> | 4.5 | 2.0<br><sub>-,0,3,1,2</sub> |  | 1.3<br><sub>-,0,2,0,1</sub> | 1.5 | 0.5 | 1.4 | 1.0 | 16.1 |
| Larry Nance Jr. | 88% | 22.4<br><sub>5,1,22,19,23</sub> | 6.4<br><sub>0,0,6,2,5</sub> |  | 4.9<br><sub>0,0,6,3,5</sub> |  | 1.5<br><sub>0,0,1,1,0</sub> |  | 0.7<br><sub>0,0,1,0,1</sub> |  | 1.0 | 0.4 | 0.9 | 12.8 |
| Jalen Slawson | 88% | 15.8<br><sub>-,16,8,3,12</sub> | 4.6<br><sub>-,4,1,2,2</sub> |  | 3.2<br><sub>-,5,2,1,1</sub> |  | 1.7<br><sub>-,2,0,0,1</sub> |  | 0.4<br><sub>-,0,0,0,0</sub> |  | 0.8 | 0.6 | 0.7 | 9.5 |
| Kobe Brown | 48% | 15.0<br><sub>-,1,-,-,-</sub> | 5.8<br><sub>-,0,-,-,-</sub> |  | 3.0<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.8 | 10.2 |
| Braden Smith | 58% | 14.2<br><sub>-,-,-,-,5</sub> | 0.6<br><sub>-,-,-,-,0</sub> |  | 0.5<br><sub>-,-,-,-,0</sub> |  | 1.3<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.6 | 0.3 | 0.6 | 2.4 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Davion Mitchell | 98% | 33.8<br><sub>33,33,37,33,34</sub> | 13.1<br><sub>11,18,22,21,10</sub> | 11.5 · – | 2.9<br><sub>0,2,1,0,1</sub> | 2.5 | 7.0<br><sub>11,5,10,2,10</sub> | 6.5 | 1.5<br><sub>1,3,3,2,0</sub> | 1.5 | 1.3 | 0.2 | 1.9 | 23.0 |
| Bam Adebayo | 98% | 33.6<br><sub>31,23,39,30,33</sub> | 20.5<br><sub>15,4,20,8,24</sub> | 18.5 · – | 10.7<br><sub>7,6,8,8,9</sub> | 9.5 | 3.9<br><sub>4,3,4,3,3</sub> | 3.5 | 1.6<br><sub>1,0,2,0,0</sub> | 1.5 | 1.6 | 0.7 | 1.8 | 35.1 |
| Giannis Antetokounmpo | 98% | 32.8<br><sub>30,33,25,39,31</sub> | 29.6<br><sub>35,36,14,29,24</sub> | 31.5 · – | 12.4<br><sub>6,12,6,14,18</sub> | 11.5 | 6.1<br><sub>1,5,3,11,3</sub> | 6.5 | 0.5<br><sub>0,1,0,2,0</sub> | 0.5 | 1.1 | 0.9 | 3.1 | 48.1 |
| Pelle Larsson | 98% | 30.9<br><sub>24,29,36,34,31</sub> | 12.8<br><sub>2,7,15,12,17</sub> | 11.5 · – | 4.0<br><sub>3,2,7,0,6</sub> | 3.5 | 3.9<br><sub>4,1,4,4,8</sub> | 3.5 | 1.0<br><sub>0,1,1,1,2</sub> |  | 1.1 | 0.3 | 1.6 | 20.7 |
| Andrew Wiggins | 98% | 28.2<br><sub>27,26,18,34,29</sub> | 13.2<br><sub>11,8,4,12,18</sub> | 12.5 · – | 4.7<br><sub>2,8,1,3,2</sub> | 4.5 | 2.2<br><sub>1,2,1,1,2</sub> | 1.5 | 1.6<br><sub>1,1,0,0,4</sub> | 1.5 | 1.0 | 1.0 | 1.2 | 20.1 |
| Bobby Portis | 98% | 23.5<br><sub>25,21,27,24,23</sub> | 11.6<br><sub>7,11,13,10,11</sub> | 11.5 · – | 7.0<br><sub>4,8,8,12,9</sub> | 7.5 | 1.6<br><sub>1,2,0,2,4</sub> |  | 1.6<br><sub>1,3,2,3,1</sub> | 1.5 | 0.7 | 0.4 | 0.9 | 20.2 |
| Tim Hardaway Jr. | 98% | 19.3<br><sub>18,21,21,16,22</sub> | 8.4<br><sub>3,8,5,5,14</sub> | 8.5 · – | 2.4<br><sub>4,4,0,2,3</sub> |  | 1.0<br><sub>1,1,0,1,1</sub> |  | 1.2<br><sub>1,2,0,1,2</sub> | 1.5 | 0.6 | 0.2 | 0.5 | 11.8 |
| Klay Thompson | 98% | 17.6<br><sub>16,24,27,15,17</sub> | 8.1<br><sub>10,6,14,6,3</sub> | 7.5 · – | 1.7<br><sub>1,2,3,1,1</sub> |  | 1.1<br><sub>0,2,0,1,2</sub> |  | 1.4<br><sub>3,2,4,2,1</sub> | 1.5 | 0.5 | 0.3 | 0.6 | 10.9 |
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
| Amen Thompson STL over 1.5 (2+) | HOU @ DAL | draftkings | 2.41 | 2.36 | 1.89 | 53.0% | 38.9% | 42.4% | +2.2% | +27.8% | 0.4% |
| Zaccharie Risacher REB over 4.5 (5+) | HOU @ DAL | draftkings | 2.19 | 2.16 | 1.77 | 56.5% | 43.0% | 46.3% | +1.5% | +23.6% | 0.3% |
| Fred VanVleet STL over 1.5 (2+) | HOU @ DAL | draftkings | 2.55 | 2.51 | 2.05 | 48.7% | 36.8% | 39.8% | +1.4% | +24.2% | 0.2% |
| Jabari Smith Jr. REB over 6.5 (7+) | HOU @ DAL | draftkings | 2.09 | 2.08 | 1.71 | 58.6% | 44.7% | 48.2% | +0.7% | +22.5% | 0.2% |
| Cooper Flagg PRA under 35.5 | HOU @ DAL | draftkings | 1.93 | 1.92 | 1.59 | 63.0% | 48.3% | 52.0% | +0.5% | +21.8% | 0.1% |
| Kevin Durant REB over 5.5 (6+) | HOU @ DAL | draftkings | 2.01 | 2.00 | 1.67 | 60.0% | 46.6% | 50.0% | +0.4% | +20.5% | 0.1% |
| Cooper Flagg PTS under 23.5 | HOU @ DAL | draftkings | 1.92 | 1.91 | 1.58 | 63.2% | 48.7% | 52.4% | +0.4% | +21.2% | 0.1% |
| Cooper Flagg PR under 30.5 | HOU @ DAL | draftkings | 1.85 | 1.85 | 1.53 | 65.3% | 50.4% | 54.1% | +0.4% | +21.0% | 0.1% |
| Kevin Durant PR over 29.5 (30+) | HOU @ DAL | draftkings | 1.94 | 1.94 | 1.61 | 62.2% | 48.1% | 51.6% | +0.3% | +20.9% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.3–113.3 | HOU 58% | 1.73 / 2.37 | DAL +3.5 | 229.5 | DAL +5.5 covers 57%; o223.5 63% |
| Expected (weighted by chance each plays) | 116.6–113.1 | HOU 59% | 1.69 / 2.46 | DAL +3.5 | 229.5 | DAL +5.5 covers 56%; o223.5 63% |
| if Marcus Smart plays | 116.9–113.1 | HOU 60% | 1.66 / 2.52 | DAL +3.5 | 229.5 | DAL +5.5 covers 55%; o223.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Marcus Smart (HOU) | Questionable | 55% | 26.4 | 8.9 | 2.9 | 2.9 | 1.2 | 1.6 | 0.4 | 1.8 | 14.8 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson | 98% | 37.2<br><sub>33,36,39,28,33</sub> | 21.3<br><sub>16,20,17,15,23</sub> | 19.5 · – | 8.1<br><sub>10,10,11,5,4</sub> | 7.5 | 6.2<br><sub>4,4,6,2,3</sub> | 5.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.9 | 0.7 | 2.6 | 35.6 |
| Jabari Smith Jr. | 98% | 37.1<br><sub>36,34,33,39,30</sub> | 18.5<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.5<br><sub>5,5,5,12,2</sub> | 6.5 | 2.5<br><sub>1,1,3,5,2</sub> |  | 2.3<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.8 | 28.5 |
| Kevin Durant | 98% | 37.0<br><sub>37,37,37,30,31</sub> | 28.1<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.5<br><sub>6,7,4,9,5</sub> | 5.5 | 5.9<br><sub>3,6,2,3,4</sub> | 4.5 | 2.3<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.3 | 3.8 | 40.5 |
| Fred VanVleet | 98% | 34.4<br><sub>30,32,-,29,29</sub> | 16.2<br><sub>6,14,-,5,24</sub> | 12.5 · – | 3.9<br><sub>2,3,-,4,6</sub> | 3.5 | 6.1<br><sub>11,5,-,5,5</sub> | 6.5 | 2.6<br><sub>2,3,-,0,4</sub> | 2.5 | 1.7 | 0.4 | 1.7 | 26.2 |
| Tari Eason | 98% | 32.5<br><sub>3,27,31,33,31</sub> | 14.5<br><sub>2,12,19,13,5</sub> | 11.5 · – | 7.6<br><sub>1,6,3,8,9</sub> | 6.5 | 1.9<br><sub>0,0,0,2,1</sub> | 1.5 | 1.3<br><sub>0,0,0,1,1</sub> | 1.5 | 1.7 | 0.9 | 1.8 | 24.0 |
| Bogdan Bogdanovic | 88% | 21.5<br><sub>13,9,20,13,15</sub> | 8.7<br><sub>5,3,11,5,16</sub> |  | 2.6<br><sub>1,1,1,2,2</sub> |  | 2.3<br><sub>2,0,1,1,4</sub> |  | 1.3<br><sub>1,1,3,1,4</sub> |  | 0.8 | 0.2 | 0.9 | 13.7 |
| Oscar Tshiebwe | 67% | 20.9<br><sub>-,-,-,-,14</sub> | 9.3<br><sub>-,-,-,-,7</sub> |  | 9.1<br><sub>-,-,-,-,5</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.5 | 1.1 | 19.8 |
| Clint Capela | 83% | 19.9<br><sub>8,-,11,4,22</sub> | 6.0<br><sub>0,-,2,2,10</sub> |  | 7.6<br><sub>3,-,3,2,8</sub> |  | 1.3<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.8 | 1.4 | 0.9 | 14.9 |
| Jae'Sean Tate | 84% | 11.6<br><sub>2,-,1,1,4</sub> | 3.3<br><sub>0,-,0,0,0</sub> |  | 2.5<br><sub>0,-,0,1,0</sub> |  | 0.8<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.5 |
| Bruce Thornton | 80% | 10.2<br><sub>3,-,4,1,3</sub> | 2.3<br><sub>0,-,0,0,5</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.9<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 3.6 |
| Isaiah Crawford | 72% | 9.8<br><sub>3,-,1,1,5</sub> | 2.6<br><sub>3,-,0,0,3</sub> |  | 1.8<br><sub>0,-,0,0,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.3 | 5.0 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington | 98% | 31.2<br><sub>31,33,36,41,27</sub> | 13.5<br><sub>10,20,12,20,18</sub> | 13.5 · – | 6.5<br><sub>4,13,4,9,9</sub> | 6.5 | 1.6<br><sub>2,0,2,2,0</sub> |  | 1.5<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.7 | 21.6 |
| Cooper Flagg | 98% | 30.9<br><sub>33,17,-,40,33</sub> | 21.7<br><sub>32,14,-,29,26</sub> | 23.5 · – | 6.1<br><sub>5,5,-,6,5</sub> | 6.5 | 5.3<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.5 | 33.1 |
| Kyrie Irving | 98% | 30.7<br><sub>24,25,-,33,27</sub> | 20.2<br><sub>15,24,-,18,15</sub> | 18.5 · – | 3.8<br><sub>4,1,-,6,2</sub> | 3.5 | 3.8<br><sub>2,3,-,6,4</sub> | 3.5 | 2.2<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.1 | 27.8 |
| Zaccharie Risacher | 88% | 27.6<br><sub>27,32,32,30,29</sub> | 9.0<br><sub>4,11,11,6,13</sub> | 8.5 · – | 5.2<br><sub>6,6,4,8,6</sub> | 4.5 | 1.5<br><sub>2,1,2,1,1</sub> |  | 0.9<br><sub>0,1,1,1,2</sub> |  | 1.2 | 1.3 | 1.2 | 15.7 |
| Naji Marshall | 98% | 26.0<br><sub>29,33,21,-,-</sub> | 13.7<br><sub>16,15,10,-,-</sub> | 11.5 · – | 3.8<br><sub>2,4,4,-,-</sub> | 3.5 | 3.6<br><sub>6,6,5,-,-</sub> | 3.5 | 0.8<br><sub>2,0,1,-,-</sub> | 0.5 | 1.2 | 0.1 | 1.8 | 21.1 |
| Max Christie | 98% | 25.8<br><sub>29,38,26,26,22</sub> | 9.8<br><sub>5,16,5,11,11</sub> | 8.5 · – | 2.9<br><sub>3,4,5,5,5</sub> | 3.5 | 1.7<br><sub>2,4,1,3,2</sub> |  | 1.5<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.3 | 1.2 | 14.3 |
| Daniel Gafford | 98% | 22.1<br><sub>22,15,23,26,27</sub> | 8.6<br><sub>2,4,12,8,7</sub> | 7.5 · – | 6.7<br><sub>3,3,9,9,11</sub> | 6.5 | 1.3<br><sub>1,5,2,3,2</sub> |  | 0.0<br><sub>0,0,0,0,1</sub> |  | 0.8 | 1.4 | 1.1 | 16.6 |
| Marcus Sasser | 91% | 17.5<br><sub>24,27,27,8,22</sub> | 6.3<br><sub>17,6,12,0,10</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 2.3<br><sub>1,3,5,0,4</sub> |  | 0.9<br><sub>4,2,2,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 10.1 |
| Walter Clayton Jr. | 67% | 13.1<br><sub>-,1,15,17,15</sub> | 4.4<br><sub>-,0,3,15,0</sub> |  | 2.0<br><sub>-,1,2,4,2</sub> |  | 2.8<br><sub>-,0,5,4,5</sub> |  | 0.5<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.3 |
| Morez Johnson Jr. | 98% | 12.9<br><sub>14,17,12,15,18</sub> | 5.2<br><sub>6,8,6,6,10</sub> |  | 1.8<br><sub>3,6,1,2,6</sub> |  | 1.3<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.8 | 8.3 |
| Caleb Martin | 91% | 12.7<br><sub>-,-,-,-,14</sub> | 4.1<br><sub>-,-,-,-,10</sub> |  | 2.1<br><sub>-,-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.2<br><sub>-,-,-,-,2</sub> |  | 0.6 | 0.3 | 0.6 | 7.1 |
| Moussa Cisse | 76% | 7.5<br><sub>3,1,7,-,3</sub> | 2.6<br><sub>3,3,4,-,0</sub> |  | 2.9<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.6 | 0.4 | 5.7 |
| Tobi Lawal | 63% | 6.1<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.0<br><sub>-,0,1,-,0</sub> |  | 0.8<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Jett Howard | 63% | 5.9<br><sub>-,-,4,-,3</sub> | 2.5<br><sub>-,-,5,-,0</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.2 | 3.5 |

</details>

<details><summary>if Marcus Smart plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington (DAL) | 98% | 31.1<br><sub>31,33,36,41,27</sub> | 13.4<br><sub>10,20,12,20,18</sub> | 13.5 · – | 6.5<br><sub>4,13,4,9,9</sub> | 6.5 | 1.6<br><sub>2,0,2,2,0</sub> |  | 1.5<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.7 | 21.6 |
| Cooper Flagg (DAL) | 98% | 31.0<br><sub>33,17,-,40,33</sub> | 21.6<br><sub>32,14,-,29,26</sub> | 23.5 · – | 6.1<br><sub>5,5,-,6,5</sub> | 6.5 | 5.3<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.5 | 33.0 |
| Kyrie Irving (DAL) | 98% | 30.8<br><sub>24,25,-,33,27</sub> | 20.2<br><sub>15,24,-,18,15</sub> | 18.5 · – | 3.8<br><sub>4,1,-,6,2</sub> | 3.5 | 3.8<br><sub>2,3,-,6,4</sub> | 3.5 | 2.2<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.1 | 27.8 |
| Zaccharie Risacher (DAL) | 88% | 27.6<br><sub>27,32,32,30,29</sub> | 9.0<br><sub>4,11,11,6,13</sub> | 8.5 · – | 5.2<br><sub>6,6,4,8,6</sub> | 4.5 | 1.5<br><sub>2,1,2,1,1</sub> |  | 0.9<br><sub>0,1,1,1,2</sub> |  | 1.1 | 1.3 | 1.2 | 15.7 |
| Naji Marshall (DAL) | 98% | 26.0<br><sub>29,33,21,-,-</sub> | 13.6<br><sub>16,15,10,-,-</sub> | 11.5 · – | 3.8<br><sub>2,4,4,-,-</sub> | 3.5 | 3.6<br><sub>6,6,5,-,-</sub> | 3.5 | 0.8<br><sub>2,0,1,-,-</sub> | 0.5 | 1.2 | 0.1 | 1.8 | 21.0 |
| Max Christie (DAL) | 98% | 25.8<br><sub>29,38,26,26,22</sub> | 9.8<br><sub>5,16,5,11,11</sub> | 8.5 · – | 2.9<br><sub>3,4,5,5,5</sub> | 3.5 | 1.7<br><sub>2,4,1,3,2</sub> |  | 1.5<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.3 | 1.2 | 14.4 |
| Daniel Gafford (DAL) | 98% | 22.0<br><sub>22,15,23,26,27</sub> | 8.5<br><sub>2,4,12,8,7</sub> | 7.5 · – | 6.7<br><sub>3,3,9,9,11</sub> | 6.5 | 1.4<br><sub>1,5,2,3,2</sub> |  | 0.0<br><sub>0,0,0,0,1</sub> |  | 0.7 | 1.5 | 1.1 | 16.5 |
| Marcus Sasser (DAL) | 91% | 17.5<br><sub>24,27,27,8,22</sub> | 6.3<br><sub>17,6,12,0,10</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 2.3<br><sub>1,3,5,0,4</sub> |  | 0.9<br><sub>4,2,2,0,1</sub> |  | 0.7 | 0.1 | 0.9 | 10.1 |
| Walter Clayton Jr. (DAL) | 67% | 13.1<br><sub>-,1,15,17,15</sub> | 4.5<br><sub>-,0,3,15,0</sub> |  | 2.0<br><sub>-,1,2,4,2</sub> |  | 2.8<br><sub>-,0,5,4,5</sub> |  | 0.5<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.4 |
| Morez Johnson Jr. (DAL) | 98% | 12.9<br><sub>14,17,12,15,18</sub> | 5.2<br><sub>6,8,6,6,10</sub> |  | 1.8<br><sub>3,6,1,2,6</sub> |  | 1.2<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.8 | 8.3 |
| Caleb Martin (DAL) | 91% | 12.7<br><sub>-,-,-,-,14</sub> | 4.1<br><sub>-,-,-,-,10</sub> |  | 2.1<br><sub>-,-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,2</sub> |  | 0.6 | 0.3 | 0.6 | 7.1 |
| Moussa Cisse (DAL) | 76% | 7.5<br><sub>3,1,7,-,3</sub> | 2.6<br><sub>3,3,4,-,0</sub> |  | 2.9<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.6 | 0.5 | 5.6 |
| Tobi Lawal (DAL) | 63% | 6.1<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.0<br><sub>-,0,1,-,0</sub> |  | 0.8<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 3.9 |
| Jett Howard (DAL) | 63% | 6.0<br><sub>-,-,4,-,3</sub> | 2.5<br><sub>-,-,5,-,0</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.2 | 3.6 |
| Amen Thompson (HOU) | 98% | 36.9<br><sub>33,36,39,28,33</sub> | 20.5<br><sub>16,20,17,15,23</sub> | 19.5 · – | 8.0<br><sub>10,10,11,5,4</sub> | 7.5 | 5.8<br><sub>4,4,6,2,3</sub> | 5.5 | 0.3<br><sub>1,1,0,0,0</sub> |  | 1.8 | 0.8 | 2.5 | 34.3 |
| Jabari Smith Jr. (HOU) | 98% | 36.3<br><sub>36,34,33,39,30</sub> | 17.6<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.3<br><sub>5,5,5,12,2</sub> | 6.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 2.2<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.6 | 27.3 |
| Kevin Durant (HOU) | 98% | 36.0<br><sub>37,37,37,30,31</sub> | 27.2<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.3<br><sub>6,7,4,9,5</sub> | 5.5 | 5.6<br><sub>3,6,2,3,4</sub> | 4.5 | 2.3<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.2 | 3.4 | 39.2 |
| Fred VanVleet (HOU) | 98% | 33.5<br><sub>30,32,-,29,29</sub> | 15.3<br><sub>6,14,-,5,24</sub> | 12.5 · – | 3.9<br><sub>2,3,-,4,6</sub> | 3.5 | 5.7<br><sub>11,5,-,5,5</sub> | 6.5 | 2.5<br><sub>2,3,-,0,4</sub> | 2.5 | 1.6 | 0.4 | 1.5 | 24.9 |
| Tari Eason (HOU) | 98% | 29.6<br><sub>3,27,31,33,31</sub> | 12.8<br><sub>2,12,19,13,5</sub> | 11.5 · – | 6.9<br><sub>1,6,3,8,9</sub> | 6.5 | 1.7<br><sub>0,0,0,2,1</sub> | 1.5 | 1.2<br><sub>0,0,0,1,1</sub> | 1.5 | 1.6 | 0.8 | 1.4 | 21.4 |
| Marcus Smart (HOU) | 100% | 26.4<br><sub>26,21,-,-,-</sub> | 8.9<br><sub>10,5,-,-,-</sub> |  | 2.9<br><sub>2,3,-,-,-</sub> |  | 2.9<br><sub>2,1,-,-,-</sub> |  | 1.2<br><sub>2,0,-,-,-</sub> |  | 1.6 | 0.4 | 1.8 | 14.8 |
| Oscar Tshiebwe (HOU) | 67% | 18.7<br><sub>-,-,-,-,14</sub> | 8.2<br><sub>-,-,-,-,7</sub> |  | 8.2<br><sub>-,-,-,-,5</sub> |  | 1.2<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.5 | 1.0 | 17.7 |
| Bogdan Bogdanovic (HOU) | 88% | 17.8<br><sub>13,9,20,13,15</sub> | 6.8<br><sub>5,3,11,5,16</sub> |  | 2.2<br><sub>1,1,1,2,2</sub> |  | 1.9<br><sub>2,0,1,1,4</sub> |  | 1.0<br><sub>1,1,3,1,4</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Clint Capela (HOU) | 83% | 17.1<br><sub>8,-,11,4,22</sub> | 5.4<br><sub>0,-,2,2,10</sub> |  | 6.5<br><sub>3,-,3,2,8</sub> |  | 1.1<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.7 | 1.2 | 0.8 | 13.0 |
| Jae'Sean Tate (HOU) | 84% | 8.6<br><sub>2,-,1,1,4</sub> | 2.5<br><sub>0,-,0,0,0</sub> |  | 1.9<br><sub>0,-,0,1,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |
| Isaiah Crawford (HOU) | 72% | 7.7<br><sub>3,-,1,1,5</sub> | 2.2<br><sub>3,-,0,0,3</sub> |  | 1.4<br><sub>0,-,0,0,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.3 | 4.2 |
| Bruce Thornton (HOU) | 80% | 7.5<br><sub>3,-,4,1,3</sub> | 1.9<br><sub>0,-,0,0,5</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 2.9 |

</details>


### LAC @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Kris Dunn RA under 8.5 | LAC @ MIN | draftkings | 1.93 | 1.91 | 1.58 | 63.4% | 48.7% | 52.4% | +0.8% | +22.1% | 0.2% |
| Rui Hachimura PR under 19.5 | LAC @ MIN | draftkings | 1.92 | 1.91 | 1.58 | 63.4% | 48.7% | 52.4% | +0.5% | +21.7% | 0.1% |
| LaMelo Ball 3PM under 3.5 | LAC @ MIN | draftkings | 1.91 | 1.90 | 1.58 | 63.2% | 48.9% | 52.5% | +0.3% | +20.8% | 0.1% |
| LaMelo Ball PR under 25.5 | LAC @ MIN | draftkings | 1.85 | 1.85 | 1.54 | 65.0% | 50.4% | 54.0% | +0.2% | +20.6% | 0.1% |
| Rui Hachimura 3PM under 1.5 | LAC @ MIN | draftkings | 2.32 | 2.32 | 1.93 | 51.9% | 40.3% | 43.2% | +0.2% | +20.4% | 0.0% |
| Darius Garland PRA under 33.5 | LAC @ MIN | draftkings | 1.92 | 1.92 | 1.60 | 62.5% | 48.7% | 52.2% | +0.0% | +19.8% | 0.0% |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 31.5<br><sub>32,37,36,26</sub> | 22.4<br><sub>30,26,16,14</sub> | 23.5 · – | 2.5<br><sub>1,0,4,1</sub> | 2.5 | 6.3<br><sub>4,6,11,5</sub> | 7.5 | 2.6<br><sub>3,4,2,1</sub> | 2.5 | 1.2 | 0.2 | 3.4 | 31.3 |
| Rui Hachimura | 98% | 30.4<br><sub>32,33,29,-</sub> | 13.8<br><sub>10,16,5,-</sub> | 14.5 · – | 4.1<br><sub>8,6,4,-</sub> | 4.5 | 1.1<br><sub>2,1,0,-</sub> | 1.5 | 1.6<br><sub>2,3,1,-</sub> | 1.5 | 0.8 | 0.4 | 1.4 | 19.0 |
| Derrick Jones Jr. | 98% | 28.2<br><sub>26,35,30,28</sub> | 10.7<br><sub>8,16,11,15</sub> | 10.5 · – | 4.1<br><sub>6,4,6,5</sub> | 4.5 | 1.3<br><sub>5,1,1,0</sub> |  | 1.1<br><sub>1,3,3,3</sub> | 1.5 | 1.1 | 0.8 | 1.0 | 16.1 |
| Kris Dunn | 98% | 27.9<br><sub>27,34,33,27</sub> | 7.2<br><sub>7,7,15,5</sub> | 7.5 · – | 3.7<br><sub>5,5,4,3</sub> | 3.5 | 3.9<br><sub>7,5,6,3</sub> | 4.5 | 0.8<br><sub>2,1,1,1</sub> | 0.5 | 1.9 | 0.3 | 1.5 | 14.8 |
| Keaton Wagler | 93% | 25.5<br><sub>29,24,26,28</sub> | 13.3<br><sub>15,13,11,21</sub> | 12.5 · – | 3.2<br><sub>5,3,5,4</sub> | 3.5 | 3.1<br><sub>5,3,4,2</sub> | 2.5 | 1.4<br><sub>3,2,1,3</sub> | 1.5 | 1.0 | 0.3 | 2.3 | 19.6 |
| Brook Lopez | 98% | 22.5<br><sub>27,20,23,22</sub> | 10.1<br><sub>17,22,15,2</sub> |  | 4.0<br><sub>11,4,1,3</sub> |  | 1.4<br><sub>1,0,2,3</sub> |  | 1.1<br><sub>1,2,3,0</sub> |  | 0.6 | 1.1 | 1.0 | 15.5 |
| Kobe Sanders | 96% | 20.8<br><sub>19,19,20,27</sub> | 8.6<br><sub>2,5,12,9</sub> | 7.5 · – | 2.4<br><sub>0,3,4,4</sub> |  | 1.8<br><sub>3,5,2,0</sub> |  | 1.0<br><sub>0,1,2,1</sub> | 1.5 | 1.0 | 0.2 | 1.2 | 12.8 |
| Isaiah Jackson | 96% | 19.6<br><sub>15,28,24,19</sub> | 8.4<br><sub>13,6,10,4</sub> | 7.5 · – | 5.8<br><sub>5,6,6,5</sub> | 6.5 | 1.4<br><sub>0,3,4,1</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.9 | 1.0 | 1.4 | 15.5 |
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
| Jaden McDaniels | 98% | 34.5<br><sub>29,30,31,37,35</sub> | 16.9<br><sub>17,15,14,14,19</sub> | 17.5 · – | 5.7<br><sub>8,6,6,6,7</sub> | 5.5 | 2.9<br><sub>1,3,3,4,4</sub> | 2.5 | 1.4<br><sub>1,2,1,2,1</sub> | 1.5 | 1.1 | 1.0 | 1.8 | 25.5 |
| Jonathan Kuminga | 98% | 31.2<br><sub>30,27,26,36,32</sub> | 14.5<br><sub>12,11,13,10,20</sub> | 14.5 · – | 5.8<br><sub>1,8,4,10,3</sub> | 5.5 | 2.5<br><sub>3,5,1,1,5</sub> | 2.5 | 1.4<br><sub>2,2,3,0,3</sub> | 1.5 | 1.1 | 0.5 | 1.8 | 22.9 |
| Rudy Gobert | 98% | 30.9<br><sub>33,30,31,36,20</sub> | 9.7<br><sub>5,14,8,5,1</sub> | 10.5 · – | 10.8<br><sub>15,9,13,20,4</sub> | 11.5 | 1.7<br><sub>1,1,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.2 | 1.5 | 22.2 |
| Ayo Dosunmu | 98% | 30.2<br><sub>29,27,23,26,32</sub> | 15.8<br><sub>16,14,9,9,17</sub> | 16.5 · – | 4.0<br><sub>5,7,3,1,3</sub> | 4.5 | 4.4<br><sub>3,10,3,0,4</sub> | 4.5 | 1.6<br><sub>1,1,1,1,3</sub> | 1.5 | 1.1 | 0.3 | 1.9 | 24.2 |
| LaMelo Ball | 98% | 28.2<br><sub>29,23,17,31,28</sub> | 19.3<br><sub>21,12,15,11,8</sub> | 20.5 · – | 3.8<br><sub>2,5,1,0,4</sub> | 4.5 | 6.4<br><sub>6,5,8,6,8</sub> | 7.5 | 3.1<br><sub>5,2,4,1,2</sub> | 3.5 | 1.2 | 0.3 | 3.1 | 29.5 |
| Terrence Shannon Jr. | 96% | 25.8<br><sub>20,22,23,24,27</sub> | 14.6<br><sub>10,13,15,14,19</sub> | 14.5 · – | 3.1<br><sub>1,4,4,4,6</sub> | 3.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 1.6<br><sub>2,2,3,3,1</sub> | 1.5 | 0.7 | 0.1 | 1.6 | 19.9 |
| Trey Lyles | 97% | 17.7<br><sub>12,17,14,13,22</sub> | 5.1<br><sub>1,9,3,3,7</sub> |  | 3.9<br><sub>1,6,6,1,3</sub> |  | 1.1<br><sub>0,2,2,1,1</sub> |  | 0.7<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.2 | 0.6 | 10.2 |
| Joan Beringer | 91% | 17.0<br><sub>14,15,13,17,20</sub> | 7.8<br><sub>0,9,6,12,7</sub> |  | 6.1<br><sub>6,9,6,7,9</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.6 |
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

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.7–114.0 | LAL 52% | 1.91 / 2.09 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| Expected (weighted by chance each plays) | 114.5–114.5 | LAL 50% | 1.99 / 2.01 | GSW +0.5 | 228.5 | GSW +3.5 covers 59%; o234.5 38% |
| if Gui Santos plays | 114.4–115.0 | LAL 49% | 2.05 / 1.95 | GSW +0.5 | 229.5 | GSW +3.5 covers 60%; o234.5 39% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Questionable | 55% | 23.6 | 9.2 | 4.2 | 2.3 | 1.1 | 1.1 | 0.3 | 1.5 | 15.7 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.6<br><sub>30,37,38,37,-</sub> | 34.4<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 6.5 | 8.1<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.6 |
| Austin Reaves | 98% | 35.6<br><sub>32,38,36,39,31</sub> | 21.3<br><sub>23,28,29,26,16</sub> | 23.5 · – | 4.2<br><sub>4,2,1,4,6</sub> | 4.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 31.1 |
| Walker Kessler | 98% | 29.8<br><sub>30,35,28,33,26</sub> | 11.3<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.7<br><sub>9,8,7,8,9</sub> | 9.5 | 1.6<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.5 |
| Quentin Grimes | 98% | 27.1<br><sub>27,31,20,19,38</sub> | 10.0<br><sub>10,13,3,2,23</sub> | 9.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 3.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.7 |
| Sandro Mamukelashvili | 98% | 24.8<br><sub>22,24,21,24,30</sub> | 9.8<br><sub>5,7,9,17,13</sub> | 9.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> | 0.5 | 1.0 | 0.5 | 1.0 | 16.9 |
| Jake LaRavia | 91% | 23.8<br><sub>18,-,15,19,35</sub> | 5.8<br><sub>10,-,0,5,2</sub> |  | 3.8<br><sub>2,-,4,1,10</sub> |  | 1.4<br><sub>2,-,1,1,0</sub> |  | 0.5<br><sub>2,-,0,1,0</sub> |  | 1.4 | 0.6 | 1.2 | 11.0 |
| Matisse Thybulle | 96% | 23.2<br><sub>23,24,26,22,28</sub> | 6.5<br><sub>3,13,11,5,15</sub> | 6.5 · – | 2.2<br><sub>3,1,1,2,1</sub> | 2.5 | 1.2<br><sub>1,2,1,1,0</sub> |  | 1.1<br><sub>1,3,3,1,4</sub> | 1.5 | 2.0 | 0.7 | 1.0 | 9.9 |
| Collin Sexton | 98% | 19.2<br><sub>-,16,20,14,21</sub> | 11.6<br><sub>-,5,13,9,21</sub> |  | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> |  | 1.3<br><sub>-,1,1,0,4</sub> |  | 1.0 | 0.1 | 1.7 | 15.7 |
| Jarred Vanderbilt | 48% | 16.7<br><sub>-,-,-,-,21</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 4.2<br><sub>-,-,-,-,7</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 9.7 |
| Lawson Lovering | 23% | 13.9 | 4.1 |  | 3.4 |  | 0.9 |  | 0.1 |  | 0.7 | 0.3 | 0.6 | 8.5 |
| Jaden Hardy | 52% | 9.3<br><sub>7,-,-,-,9</sub> | 4.4<br><sub>3,-,-,-,2</sub> |  | 0.9<br><sub>2,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 6.0 |
| AK Okereke | 30% | 8.7<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Arthur Kaluma | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Kevon Looney | 64% | 7.9<br><sub>15,5,5,5,-</sub> | 1.9<br><sub>6,0,2,0,-</sub> |  | 2.6<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.1 |
| Bronny James | 26% | 6.3<br><sub>7,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 2.7 |
| Chris Manon | 52% | 5.8<br><sub>6,-,-,-,-</sub> | 1.7<br><sub>2,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 3.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg | 96% | 34.7<br><sub>29,37,36,31,35</sub> | 21.0<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.3<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.1 | 33.2 |
| Brandin Podziemski | 80% | 31.7<br><sub>-,33,-,33,32</sub> | 15.0<br><sub>-,18,-,18,8</sub> | 14.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 4.5 | 4.1<br><sub>-,3,-,5,6</sub> | 3.5 | 1.9<br><sub>-,2,-,3,0</sub> | 1.5 | 1.2 | 0.2 | 1.9 | 23.9 |
| Stephen Curry | 98% | 31.1<br><sub>21,30,-,27,32</sub> | 24.2<br><sub>23,24,-,24,44</sub> | 24.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.7<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.3 | 0.3 | 3.0 | 32.4 |
| Draymond Green | 83% | 28.8<br><sub>21,31,-,27,32</sub> | 8.1<br><sub>2,5,-,3,3</sub> | 6.5 · – | 5.3<br><sub>4,5,-,4,9</sub> | 5.5 | 6.0<br><sub>8,6,-,7,6</sub> | 5.5 | 1.1<br><sub>0,1,-,1,0</sub> | 0.5 | 1.2 | 0.6 | 2.5 | 19.3 |
| De'Anthony Melton | 98% | 21.5<br><sub>21,20,27,19,20</sub> | 9.3<br><sub>0,10,25,3,8</sub> | 9.5 · – | 3.0<br><sub>2,1,5,4,6</sub> | 2.5 | 2.3<br><sub>2,0,5,3,0</sub> | 1.5 | 1.3<br><sub>0,2,4,1,2</sub> | 1.5 | 1.4 | 0.3 | 1.5 | 14.6 |
| Georges Niang | 93% | 20.1<br><sub>20,13,23,18,23</sub> | 7.9<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.6<br><sub>2,3,4,2,3</sub> |  | 1.1<br><sub>2,0,2,0,2</sub> |  | 1.3<br><sub>0,0,0,3,1</sub> | 1.5 | 0.6 | 0.1 | 1.0 | 11.7 |
| Al Horford | 98% | 19.4<br><sub>17,19,-,19,18</sub> | 6.0<br><sub>0,3,-,11,4</sub> | 5.5 · – | 4.2<br><sub>4,5,-,3,5</sub> | 3.5 | 1.6<br><sub>2,0,-,0,2</sub> |  | 0.9<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.7 | 0.7 | 11.7 |
| Will Richard | 98% | 16.8<br><sub>20,3,31,3,23</sub> | 4.7<br><sub>8,0,11,0,6</sub> |  | 1.9<br><sub>5,0,0,0,3</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>0,0,3,0,0</sub> |  | 1.1 | 0.1 | 0.6 | 7.5 |
| Brandon Williams | 98% | 16.6<br><sub>18,9,24,15,14</sub> | 9.5<br><sub>14,4,20,6,11</sub> |  | 2.2<br><sub>4,2,3,3,3</sub> |  | 2.9<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.2 | 1.5 | 14.6 |
| Gary Payton II | 98% | 14.2<br><sub>18,11,17,12,10</sub> | 6.4<br><sub>10,7,2,7,2</sub> |  | 2.7<br><sub>1,2,1,2,2</sub> |  | 1.1<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 10.1 |
| Graham Ike | 67% | 12.5<br><sub>12,12,26,3,-</sub> | 5.9<br><sub>8,10,12,3,-</sub> |  | 2.8<br><sub>2,2,10,0,-</sub> |  | 1.0<br><sub>1,1,2,1,-</sub> |  | 0.3<br><sub>1,2,0,1,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.8 |
| Charles Bassey | 91% | 9.4<br><sub>-,-,13,2,2</sub> | 3.9<br><sub>-,-,10,0,0</sub> |  | 3.4<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 7.8 |
| LJ Cryer | 63% | 8.3<br><sub>9,-,14,3,-</sub> | 3.6<br><sub>9,-,3,6,-</sub> |  | 0.8<br><sub>1,-,1,0,-</sub> |  | 0.7<br><sub>3,-,1,2,-</sub> |  | 0.5<br><sub>2,-,1,2,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.0 |
| Malevy Leons | 58% | 7.9<br><sub>9,-,4,3,-</sub> | 2.4<br><sub>0,-,2,0,-</sub> |  | 1.3<br><sub>1,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 4.3 |

</details>

<details><summary>if Gui Santos plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | 96% | 34.0<br><sub>29,37,36,31,35</sub> | 21.0<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.1<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.0 | 33.0 |
| Brandin Podziemski (GSW) | 80% | 30.3<br><sub>-,33,-,33,32</sub> | 14.3<br><sub>-,18,-,18,8</sub> | 14.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 4.5 | 3.9<br><sub>-,3,-,5,6</sub> | 3.5 | 1.8<br><sub>-,2,-,3,0</sub> | 1.5 | 1.2 | 0.2 | 1.8 | 23.0 |
| Stephen Curry (GSW) | 98% | 29.9<br><sub>21,30,-,27,32</sub> | 23.6<br><sub>23,24,-,24,44</sub> | 24.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.4<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 2.9 | 31.5 |
| Draymond Green (GSW) | 83% | 26.2<br><sub>21,31,-,27,32</sub> | 7.2<br><sub>2,5,-,3,3</sub> | 6.5 · – | 4.9<br><sub>4,5,-,4,9</sub> | 5.5 | 5.4<br><sub>8,6,-,7,6</sub> | 5.5 | 0.9<br><sub>0,1,-,1,0</sub> | 0.5 | 1.1 | 0.6 | 2.3 | 17.6 |
| Gui Santos (GSW) | 100% | 23.6<br><sub>25,20,23,28,-</sub> | 9.2<br><sub>12,5,7,13,-</sub> |  | 4.2<br><sub>5,4,4,3,-</sub> |  | 2.3<br><sub>0,2,3,1,-</sub> |  | 1.1<br><sub>1,1,1,1,-</sub> |  | 1.1 | 0.3 | 1.5 | 15.7 |
| De'Anthony Melton (GSW) | 98% | 19.6<br><sub>21,20,27,19,20</sub> | 8.5<br><sub>0,10,25,3,8</sub> | 9.5 · – | 2.9<br><sub>2,1,5,4,6</sub> | 2.5 | 2.0<br><sub>2,0,5,3,0</sub> | 1.5 | 1.1<br><sub>0,2,4,1,2</sub> | 1.5 | 1.2 | 0.3 | 1.4 | 13.3 |
| Al Horford (GSW) | 98% | 17.5<br><sub>17,19,-,19,18</sub> | 5.3<br><sub>0,3,-,11,4</sub> | 5.5 · – | 3.8<br><sub>4,5,-,3,5</sub> | 3.5 | 1.4<br><sub>2,0,-,0,2</sub> |  | 0.8<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.6 | 0.6 | 10.5 |
| Georges Niang (GSW) | 93% | 17.2<br><sub>20,13,23,18,23</sub> | 7.0<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.3<br><sub>2,3,4,2,3</sub> |  | 1.0<br><sub>2,0,2,0,2</sub> |  | 1.0<br><sub>0,0,0,3,1</sub> | 1.5 | 0.5 | 0.1 | 1.0 | 10.2 |
| Brandon Williams (GSW) | 98% | 15.3<br><sub>18,9,24,15,14</sub> | 8.9<br><sub>14,4,20,6,11</sub> |  | 2.1<br><sub>4,2,3,3,3</sub> |  | 2.6<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.2 | 1.4 | 13.6 |
| Will Richard (GSW) | 98% | 14.6<br><sub>20,3,31,3,23</sub> | 4.2<br><sub>8,0,11,0,6</sub> |  | 1.7<br><sub>5,0,0,0,3</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4<br><sub>0,0,3,0,0</sub> |  | 0.9 | 0.1 | 0.5 | 6.7 |
| Gary Payton II (GSW) | 98% | 12.7<br><sub>18,11,17,12,10</sub> | 6.2<br><sub>10,7,2,7,2</sub> |  | 2.5<br><sub>1,2,1,2,2</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.6 | 9.6 |
| Graham Ike (GSW) | 67% | 8.7<br><sub>12,12,26,3,-</sub> | 4.1<br><sub>8,10,12,3,-</sub> |  | 2.0<br><sub>2,2,10,0,-</sub> |  | 0.8<br><sub>1,1,2,1,-</sub> |  | 0.2<br><sub>1,2,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.9 |
| Charles Bassey (GSW) | 91% | 7.8<br><sub>-,-,13,2,2</sub> | 3.3<br><sub>-,-,10,0,0</sub> |  | 2.9<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 6.6 |
| LJ Cryer (GSW) | 63% | 6.8<br><sub>9,-,14,3,-</sub> | 3.0<br><sub>9,-,3,6,-</sub> |  | 0.7<br><sub>1,-,1,0,-</sub> |  | 0.5<br><sub>3,-,1,2,-</sub> |  | 0.4<br><sub>2,-,1,2,-</sub> |  | 0.1 | 0.0 | 0.4 | 4.2 |
| Malevy Leons (GSW) | 58% | 6.1<br><sub>9,-,4,3,-</sub> | 2.0<br><sub>0,-,2,0,-</sub> |  | 1.1<br><sub>1,-,0,1,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.5 |
| Luka Doncic (LAL) | 98% | 36.6<br><sub>30,37,38,37,-</sub> | 34.3<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 6.5 | 8.1<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.5 |
| Austin Reaves (LAL) | 98% | 35.5<br><sub>32,38,36,39,31</sub> | 21.1<br><sub>23,28,29,26,16</sub> | 23.5 · – | 4.2<br><sub>4,2,1,4,6</sub> | 4.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 30.8 |
| Walker Kessler (LAL) | 98% | 29.8<br><sub>30,35,28,33,26</sub> | 11.2<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.7<br><sub>9,8,7,8,9</sub> | 9.5 | 1.6<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.4 |
| Quentin Grimes (LAL) | 98% | 27.1<br><sub>27,31,20,19,38</sub> | 9.9<br><sub>10,13,3,2,23</sub> | 9.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 3.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.7 |
| Sandro Mamukelashvili (LAL) | 98% | 24.8<br><sub>22,24,21,24,30</sub> | 9.8<br><sub>5,7,9,17,13</sub> | 9.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.1<br><sub>0,1,1,3,0</sub> | 0.5 | 1.0 | 0.5 | 1.0 | 17.0 |
| Jake LaRavia (LAL) | 91% | 23.9<br><sub>18,-,15,19,35</sub> | 5.8<br><sub>10,-,0,5,2</sub> |  | 3.8<br><sub>2,-,4,1,10</sub> |  | 1.4<br><sub>2,-,1,1,0</sub> |  | 0.6<br><sub>2,-,0,1,0</sub> |  | 1.4 | 0.6 | 1.2 | 11.1 |
| Matisse Thybulle (LAL) | 96% | 23.1<br><sub>23,24,26,22,28</sub> | 6.5<br><sub>3,13,11,5,15</sub> | 6.5 · – | 2.2<br><sub>3,1,1,2,1</sub> | 2.5 | 1.2<br><sub>1,2,1,1,0</sub> |  | 1.1<br><sub>1,3,3,1,4</sub> | 1.5 | 2.0 | 0.7 | 1.0 | 9.9 |
| Collin Sexton (LAL) | 98% | 19.2<br><sub>-,16,20,14,21</sub> | 11.6<br><sub>-,5,13,9,21</sub> |  | 2.0<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> |  | 1.3<br><sub>-,1,1,0,4</sub> |  | 1.1 | 0.1 | 1.7 | 15.7 |
| Jarred Vanderbilt (LAL) | 48% | 16.7<br><sub>-,-,-,-,21</sub> | 4.2<br><sub>-,-,-,-,0</sub> |  | 4.2<br><sub>-,-,-,-,7</sub> |  | 1.3<br><sub>-,-,-,-,2</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.2 | 0.8 | 9.8 |
| Lawson Lovering (LAL) | 23% | 13.9 | 4.2 |  | 3.4 |  | 1.0 |  | 0.1 |  | 0.7 | 0.3 | 0.7 | 8.5 |
| Jaden Hardy (LAL) | 52% | 9.3<br><sub>7,-,-,-,9</sub> | 4.4<br><sub>3,-,-,-,2</sub> |  | 0.8<br><sub>2,-,-,-,0</sub> |  | 0.7<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.7 | 5.9 |
| Arthur Kaluma (LAL) | 23% | 8.6<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.9 |
| AK Okereke (LAL) | 30% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Kevon Looney (LAL) | 64% | 7.8<br><sub>15,5,5,5,-</sub> | 1.9<br><sub>6,0,2,0,-</sub> |  | 2.6<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.1 |
| Bronny James (LAL) | 26% | 6.4<br><sub>7,-,-,-,-</sub> | 2.2<br><sub>2,-,-,-,-</sub> |  | 0.2<br><sub>0,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 2.8 |
| Chris Manon (LAL) | 52% | 5.8<br><sub>6,-,-,-,-</sub> | 1.7<br><sub>2,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.2 | 3.2 |

</details>


### DEN @ PHX
Out: Drew Timme (PHX), Mark Williams (PHX), Julian Strawther (DEN)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +3.5 covers 53%; o231.5 43% |
| Expected (weighted by chance each plays) | 115.6–113.6 | DEN 55% | 1.82 / 2.22 | PHX +2.5 | 229.5 | PHX +3.5 covers 55%; o231.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alpha Diallo (DEN) | Doubtful | 20% | 14.3 | 3.7 | 1.8 | 1.1 | 0.3 | 0.7 | 0.3 | 0.9 | 6.6 | small |
| Oso Ighodaro (PHX) | Questionable | 55% | 17.0 | 5.4 | 4.4 | 2.1 | 0.0 | 0.6 | 0.6 | 0.8 | 11.8 | small |
| Cameron Johnson (DEN) | Questionable | 55% | 20.1 | 8.2 | 2.8 | 1.6 | 1.1 | 0.6 | 0.3 | 0.8 | 12.6 | small |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 37.6<br><sub>37,43,36,38</sub> | 24.0<br><sub>6,42,19,23</sub> | 23.5 · – | 4.4<br><sub>10,3,6,1</sub> | 4.5 | 6.1<br><sub>3,6,8,6</sub> | 6.5 | 3.3<br><sub>0,8,3,5</sub> | 2.5 | 1.1 | 0.5 | 2.6 | 34.5 |
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
| Devin Booker | 98% | 34.0<br><sub>29,36,34</sub> | 23.2<br><sub>23,43,3</sub> | 23.5 · – | 4.1<br><sub>4,7,2</sub> | 3.5 | 6.0<br><sub>2,7,7</sub> | 5.5 | 1.8<br><sub>0,2,0</sub> | 1.5 | 0.9 | 0.3 | 2.8 | 33.3 |
| Dillon Brooks | 98% | 32.3<br><sub>27,34,33</sub> | 19.1<br><sub>10,15,19</sub> | 16.5 · – | 4.4<br><sub>4,2,5</sub> | 3.5 | 2.2<br><sub>0,5,5</sub> |  | 2.2<br><sub>1,1,3</sub> | 1.5 | 1.0 | 0.2 | 1.4 | 25.8 |
| Miles Bridges | 98% | 30.9<br><sub>29,33,32</sub> | 15.3<br><sub>8,16,17</sub> | 15.5 · – | 6.2<br><sub>4,7,8</sub> | 5.5 | 2.8<br><sub>0,3,4</sub> | 2.5 | 1.6<br><sub>0,2,2</sub> | 1.5 | 0.8 | 0.4 | 1.2 | 24.4 |
| Jalen Green | 96% | 29.5<br><sub>25,26,31</sub> | 16.0<br><sub>10,12,20</sub> | 15.5 · – | 4.2<br><sub>2,2,4</sub> | 3.5 | 3.1<br><sub>3,1,4</sub> | 3.5 | 2.0<br><sub>2,1,1</sub> | 2.5 | 1.0 | 0.3 | 1.9 | 23.4 |
| Collin Gillespie | 98% | 24.9<br><sub>21,28,23</sub> | 9.5<br><sub>0,11,9</sub> | 8.5 · – | 3.5<br><sub>1,4,1</sub> | 3.5 | 3.8<br><sub>2,9,2</sub> | 3.5 | 1.7<br><sub>0,2,3</sub> | 2.5 | 1.1 | 0.2 | 1.2 | 16.8 |
| Khaman Maluach | 96% | 20.4<br><sub>17,28,26</sub> | 6.3<br><sub>2,9,12</sub> | 8.5 · – | 6.3<br><sub>6,9,7</sub> | 8.5 | 0.7<br><sub>1,3,1</sub> |  | 0.3<br><sub>0,1,0</sub> |  | 0.4 | 1.1 | 1.1 | 13.4 |
| Jordan Goodwin | 98% | 18.0<br><sub>22,20,17</sub> | 6.8<br><sub>3,9,12</sub> | 6.5 · – | 3.8<br><sub>4,2,4</sub> | 4.5 | 1.6<br><sub>0,4,2</sub> | 1.5 | 1.0<br><sub>1,1,4</sub> | 1.5 | 1.1 | 0.2 | 0.7 | 12.2 |
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
