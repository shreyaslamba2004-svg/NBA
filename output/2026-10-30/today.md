# NBA model · Fri 30 Oct 2026 (US date)

Updated **Sat 31 Oct, 05:25 AM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

2 flag(s). These numbers are unusual: there may be a good reason (injuries, a new role), but check them before betting on the players or games listed.

| Game | Check | Detail | Likely reason |
|---|---|---|---|
| CHA @ WAS | team points | CHA projected 118, market implies 110 | 42% of tonight's minutes go to players new to CHA since last season, and the team ratings still lean on last season; CHA have played 5 games this season; CHA out: Knueppel, Williams | 39% of tonight's minutes go to players new to WAS since last season, and the team ratings still lean on last season; WAS have played 5 games this season; WAS out: Champagnie, Vukcevic, Watkins |
| CHA @ WAS | player points | Grayson Allen projected 19.9 pts vs DraftKings line 14.5 | minutes 32 vs 28 this season; new team (was PHX last season); scoring 0.63/min vs 0.54 this season, 0.57 last season; teammates out: Knueppel, Williams (~51 min a game) |

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam PTS over 39.5 (40+) | IND @ MIA | draftkings | 16.80 | 13.91 | 8.27 | 12.1% | 5.6% | 7.2% | +20.9% | +103.1% | 0.3% |
| Grayson Allen STL over 2.5 (3+) | CHA @ WAS | draftkings | 12.60 | 10.83 | 6.83 | 14.6% | 7.4% | 9.2% | +16.2% | +84.6% | 0.4% |
| Pascal Siakam PTS over 34.5 (35+) | IND @ MIA | draftkings | 7.90 | 7.03 | 4.67 | 21.4% | 11.8% | 14.2% | +12.3% | +69.0% | 0.4% |
| VJ Edgecombe AST over 5.5 (6+) | NYK @ PHI | draftkings | 14.20 | 12.69 | 8.49 | 11.8% | 6.6% | 7.9% | +11.9% | +67.2% | 0.2% |
| Zaccharie Risacher REB over 7.5 (8+) | HOU @ DAL | draftkings | 8.30 | 7.53 | 5.18 | 19.3% | 11.3% | 13.3% | +10.2% | +60.4% | 0.4% |
| Grayson Allen STL over 1.5 (2+) | CHA @ WAS | draftkings | 4.51 | 4.11 | 2.85 | 35.1% | 20.7% | 24.3% | +9.7% | +58.3% | 0.7% |
| Zaccharie Risacher REB over 9.5 (10+) | HOU @ DAL | draftkings | 22.00 | 20.16 | 14.06 | 7.1% | 4.2% | 5.0% | +9.2% | +56.4% | 0.1% |
| Brandon Miller PTS over 49.5 (50+) | CHA @ WAS | draftkings | 30.00 | 27.55 | 19.29 | 5.2% | 3.1% | 3.6% | +9.0% | +55.5% | 0.1% |
| Moussa Diabate AST over 5.5 (6+) | CHA @ WAS | draftkings | 22.00 | 20.37 | 14.46 | 6.9% | 4.2% | 4.9% | +8.1% | +52.1% | 0.1% |
| Amen Thompson STL over 3.5 (4+) | HOU @ DAL | draftkings | 12.20 | 11.39 | 8.25 | 12.1% | 7.7% | 8.8% | +7.1% | +47.9% | 0.2% |
| Jayson Tatum REB over 13.5 (14+) | CHI @ BOS | draftkings | 12.40 | 11.61 | 8.47 | 11.8% | 7.5% | 8.6% | +6.7% | +46.4% | 0.1% |
| Duncan Robinson AST over 5.5 (6+) | DET @ BKN | draftkings | 21.00 | 19.69 | 14.35 | 7.0% | 4.5% | 5.1% | +6.7% | +46.4% | 0.1% |
| Duncan Robinson AST over 3.5 (4+) | DET @ BKN | draftkings | 5.11 | 4.81 | 3.53 | 28.3% | 18.3% | 20.8% | +6.2% | +44.6% | 0.4% |
| CHI to win | CHI @ BOS | ladbrokes_au | 7.75 | 7.30 | 5.35 | 18.7% | 13.7% | 13.7% | +6.1% | +45.0% | 0.2% |
| Ausar Thompson STL over 3.5 (4+) | DET @ BKN | draftkings | 8.60 | 8.15 | 6.07 | 16.5% | 10.9% | 12.3% | +5.5% | +41.8% | 0.2% |
| Anthony Davis BLK over 2.5 (3+) | CHA @ WAS | draftkings | 6.02 | 5.72 | 4.28 | 23.4% | 15.5% | 17.5% | +5.3% | +40.7% | 0.3% |
| Amen Thompson STL over 2.5 (3+) | HOU @ DAL | draftkings | 5.15 | 4.90 | 3.68 | 27.2% | 18.1% | 20.4% | +5.1% | +40.1% | 0.3% |

## Not on Sportsbet: check other books (EV ≥ 5%, any odds)

Bets that pass the same rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Not graded in HEALTH.md.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Zaccharie Risacher REB over 8.5 (9+) | HOU @ DAL | draftkings | 14.20 | 12.61 | 8.34 | 12.0% | 6.6% | 7.9% | +12.7% | +70.3% | 0.2% |
| Duncan Robinson AST over 4.5 (5+) | DET @ BKN | draftkings | 10.70 | 9.81 | 6.87 | 14.5% | 8.7% | 10.2% | +9.0% | +55.7% | 0.2% |
| VJ Edgecombe AST over 6.5 (7+) | NYK @ PHI | draftkings | 25.00 | 23.53 | 17.31 | 5.8% | 3.7% | 4.2% | +6.2% | +44.4% | 0.1% |
| Jayson Tatum REB over 14.5 (15+) | CHI @ BOS | draftkings | 18.00 | 16.98 | 12.56 | 8.0% | 5.2% | 5.9% | +5.9% | +43.4% | 0.1% |
| Jayson Tatum REB over 12.5 (13+) | CHI @ BOS | draftkings | 8.30 | 7.86 | 5.84 | 17.1% | 11.3% | 12.7% | +5.7% | +42.2% | 0.2% |

## Wait for news

These look good but hinge on a questionable player. The model's chance is shown both ways; the EV column weights them by how likely he is to play. Re-check once his status is confirmed (the sheet updates itself).

| Bet | Game | Book | Odds | Wait for news on | Model if he sits | Model if he plays | EV now (blended odds he plays) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Kevin Durant AST over 5.5 (6+) | HOU @ DAL | draftkings | 3.78 | Alperen Sengun | 53.3% | 42.1% | +11.6% |
| VJ Edgecombe AST over 3.5 (4+) | NYK @ PHI | draftkings | 3.70 | Jaylen Brown | 42.4% | 36.7% | +6.5% |
| Khaman Maluach PR under 16.5 | DEN @ PHX | draftkings | 1.84 | Oso Ighodaro | 77.0% | 81.1% | +6.5% |
| Khaman Maluach REB under 7.5 | DEN @ PHX | draftkings | 2.06 | Oso Ighodaro | 67.7% | 74.2% | +6.4% |
| Mikel Brown Jr. 3PM under 1.5 | DET @ BKN | draftkings | 2.32 | Drake Powell | 55.7% | 62.0% | +6.2% |
| Walker Kessler PR under 24.5 | LAL @ GSW | draftkings | 1.89 | Ziaire Williams | 71.6% | 76.1% | +5.1% |

## Check news first

The model and the no-vig market disagree by more than 15 points on these. That's usually late team news the model hasn't seen yet, so confirm before betting.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| John Collins PR under 21.5 | DET @ BKN | draftkings | 1.96 | 1.84 | 1.35 | 74.0% | 47.6% | 54.2% | +6.4% | +45.1% | 1.7% |
| Walker Kessler PTS under 14.5 | LAL @ GSW | draftkings | 1.83 | 1.74 | 1.29 | 77.4% | 51.0% | 57.6% | +5.6% | +41.9% | 1.7% |
| John Collins PRA under 23.5 | DET @ BKN | draftkings | 1.86 | 1.76 | 1.31 | 76.2% | 50.2% | 56.7% | +5.6% | +41.9% | 1.6% |
| John Collins PTS under 14.5 | DET @ BKN | draftkings | 1.93 | 1.83 | 1.37 | 72.9% | 48.5% | 54.6% | +5.2% | +40.4% | 1.4% |

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play).

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| CHA @ WAS | Sat 31 Oct 10:00 | 118.1–111.8 | CHA 67% | 1.49 / 3.05 | WAS +6.5 | 229.5 | WAS +1.5 covers 36%; o218.5 73% |
| CHI @ BOS | Sat 31 Oct 10:30 | 109.0–123.5 | CHI 15% | 6.52 / 1.18 | BOS -14.5 | 232.5 | BOS -14.5 covers 51%; o235.5 43% |
| DET @ BKN | Sat 31 Oct 10:30 | 115.6–103.1 | DET 81% | 1.23 / 5.28 | BKN +12.5 | 218.5 | BKN +8.5 covers 39%; o222.5 42% |
| NYK @ PHI | Sat 31 Oct 10:30 | 115.2–108.6 | NYK 68% | 1.48 / 3.08 | PHI +6.5 | 223.5 | PHI +1.5 covers 35%; o226.5 44% |
| ORL @ TOR | Sat 31 Oct 10:30 | 108.2–117.0 | ORL 27% | 3.72 / 1.37 | TOR -8.5 | 225.5 | TOR -5.5 covers 59%; o227.5 45% |
| IND @ MIA | Sat 31 Oct 11:00 | 116.5–125.8 | IND 26% | 3.90 / 1.35 | MIA -9.5 | 242.5 | MIA -8.5 covers 52%; o237.5 60% |
| HOU @ DAL | Sat 31 Oct 11:00 | 116.6–112.7 | HOU 61% | 1.65 / 2.54 | DAL +4.5 | 229.5 | DAL +6.5 covers 58%; o223.5 62% |
| LAC @ MIN | Sat 31 Oct 11:00 | 112.2–113.6 | LAC 46% | 2.16 / 1.86 | MIN -1.5 | 225.5 | MIN -7.5 covers 34%; o223.5 55% |
| LAL @ GSW | Sat 31 Oct 13:00 | 114.7–114.0 | LAL 52% | 1.91 / 2.09 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| DEN @ PHX | Sat 31 Oct 13:00 | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +4.5 covers 56%; o231.5 43% |

### CHA @ WAS
Out: Justin Champagnie (WAS), Tristan Vukcevic (WAS), Jamir Watkins (WAS), Kon Knueppel (CHA), Coby White (CHA), Grant Williams (CHA)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Anthony Davis BLK over 1.5 (2+) | CHA @ WAS | draftkings | 2.57 | 2.54 | 2.06 | 48.5% | 36.4% | 39.4% | +1.3% | +24.7% | 0.2% |
| Naz Reid 3PM under 2.5 | CHA @ WAS | draftkings | 1.95 | 1.94 | 1.59 | 62.8% | 47.9% | 51.6% | +0.7% | +22.6% | 0.2% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 118.1–111.8 | CHA 67% | 1.49 / 3.05 | WAS +6.5 | 229.5 | WAS +1.5 covers 36%; o218.5 73% |
| Expected (weighted by chance each plays) | 118.6–111.3 | CHA 71% | 1.41 / 3.41 | WAS +7.5 | 229.5 | WAS +1.5 covers 32%; o218.5 74% |
| if Tre Johnson plays | 117.9–112.3 | CHA 66% | 1.53 / 2.90 | WAS +5.5 | 230.5 | WAS +1.5 covers 37%; o218.5 74% |
| if Dennis Schroder plays | 119.0–110.5 | CHA 72% | 1.38 / 3.63 | WAS +8.5 | 229.5 | WAS +1.5 covers 30%; o218.5 72% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tre Johnson (WAS) | Questionable | 55% | 20.3 | 8.0 | 2.5 | 1.3 | 1.0 | 0.6 | 0.3 | 1.0 | 11.7 | full tables below |
| Dennis Schroder (CHA) | Questionable | 55% | 31.4 | 14.6 | 3.5 | 5.4 | 1.1 | 1.1 | 0.2 | 2.6 | 23.5 | full tables below |

<details><summary>CHA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller | 98% | 34.6<br><sub>36,23,36,36,38</sub> | 30.3<br><sub>18,6,34,39,31</sub> | 27.5 · – | 5.9<br><sub>3,2,8,6,12</sub> | 5.5 | 3.6<br><sub>1,0,4,1,3</sub> | 3.5 | 3.6<br><sub>3,1,3,5,3</sub> | 3.5 | 1.3 | 0.7 | 3.1 | 39.8 |
| Grayson Allen | 96% | 31.6<br><sub>29,20,34,28,30</sub> | 19.9<br><sub>21,11,20,15,9</sub> | 14.5 · – | 3.7<br><sub>3,2,3,2,5</sub> | 2.5 | 4.5<br><sub>4,3,5,1,2</sub> | 3.5 | 3.0<br><sub>5,3,4,2,2</sub> | 2.5 | 1.3 | 0.3 | 2.3 | 28.2 |
| Moussa Diabate | 98% | 30.6<br><sub>34,21,22,35,35</sub> | 10.2<br><sub>17,5,4,11,9</sub> | 9.5 · – | 10.7<br><sub>8,8,5,17,9</sub> | 10.5 | 2.8<br><sub>3,1,2,3,2</sub> | 1.5 | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.1 | 1.7 | 23.7 |
| Naz Reid | 98% | 27.2<br><sub>33,25,37,29,13</sub> | 18.6<br><sub>20,17,23,18,7</sub> | 17.5 · – | 7.6<br><sub>11,6,9,12,6</sub> | 7.5 | 2.4<br><sub>7,2,0,1,0</sub> | 2.5 | 2.2<br><sub>4,3,5,2,1</sub> | 2.5 | 0.8 | 0.8 | 2.2 | 28.6 |
| Sion James | 98% | 26.7<br><sub>27,24,26,29,23</sub> | 6.8<br><sub>3,3,0,5,5</sub> | 5.5 · – | 4.0<br><sub>3,2,5,2,2</sub> | 3.5 | 3.1<br><sub>0,5,5,3,3</sub> | 3.5 | 0.9<br><sub>1,1,0,1,1</sub> | 1.5 | 1.0 | 0.3 | 1.1 | 13.9 |
| Royce O'Neale | 98% | 24.1<br><sub>17,17,11,7,34</sub> | 8.1<br><sub>8,6,0,0,9</sub> |  | 4.3<br><sub>4,2,1,0,4</sub> |  | 1.6<br><sub>0,0,0,1,0</sub> |  | 1.5<br><sub>2,2,0,0,3</sub> |  | 1.0 | 0.5 | 0.9 | 14.0 |
| Ryan Kalkbrenner | 98% | 18.1<br><sub>14,19,23,13,13</sub> | 6.4<br><sub>4,6,6,6,1</sub> |  | 5.0<br><sub>5,7,5,4,1</sub> |  | 1.1<br><sub>3,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 0.8 | 12.5 |
| Tidjane Salaun | 86% | 17.3<br><sub>-,23,10,16,12</sub> | 6.4<br><sub>-,11,3,5,2</sub> |  | 4.3<br><sub>-,5,3,5,2</sub> |  | 0.9<br><sub>-,1,0,0,0</sub> |  | 0.7<br><sub>-,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.8 | 11.6 |
| Christian Anderson | 96% | 14.3<br><sub>13,16,3,11,9</sub> | 6.2<br><sub>0,2,0,3,2</sub> |  | 2.0<br><sub>2,0,1,4,0</sub> |  | 1.6<br><sub>2,2,0,1,1</sub> |  | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 1.1 | 9.8 |
| Liam McNeeley | 48% | 13.4<br><sub>3,12,-,-,-</sub> | 4.7<br><sub>0,4,-,-,-</sub> |  | 2.8<br><sub>1,4,-,-,-</sub> |  | 1.0<br><sub>0,0,-,-,-</sub> |  | 0.5<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.1 | 0.8 | 8.4 |
| PJ Hall | 38% | 11.9<br><sub>-,10,-,-,-</sub> | 4.8<br><sub>-,0,-,-,-</sub> |  | 4.3<br><sub>-,1,-,-,-</sub> |  | 0.7<br><sub>-,3,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.6 | 0.9 | 9.8 |
| Hannes Steinbach | 36% | 11.0<br><sub>-,12,-,-,-</sub> | 4.4<br><sub>-,6,-,-,-</sub> |  | 3.4<br><sub>-,5,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |

</details>

<details><summary>WAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Trae Young | 98% | 34.4<br><sub>38,37,34,38,34</sub> | 20.0<br><sub>20,22,25,22,14</sub> | 19.5 · – | 3.0<br><sub>0,1,4,6,5</sub> | 2.5 | 9.8<br><sub>13,12,9,10,8</sub> | 9.5 | 2.4<br><sub>0,4,4,1,1</sub> | 2.5 | 1.0 | 0.2 | 3.2 | 32.7 |
| Anthony Davis | 98% | 34.2<br><sub>34,32,31,36,34</sub> | 21.0<br><sub>34,9,19,29,18</sub> | 20.5 · – | 10.3<br><sub>12,9,6,10,5</sub> | 9.5 | 2.8<br><sub>4,0,4,0,3</sub> | 2.5 | 0.9<br><sub>1,0,0,3,2</sub> | 0.5 | 1.1 | 1.7 | 2.1 | 34.2 |
| Kyshawn George | 98% | 32.2<br><sub>29,26,36,29,38</sub> | 15.2<br><sub>18,11,22,20,8</sub> | 12.5 · – | 4.8<br><sub>5,3,9,4,2</sub> | 4.5 | 4.0<br><sub>3,3,5,2,11</sub> | 3.5 | 1.9<br><sub>1,1,0,2,0</sub> | 1.5 | 1.1 | 1.0 | 2.2 | 24.0 |
| Bilal Coulibaly | 98% | 28.2<br><sub>29,26,25,29,27</sub> | 10.7<br><sub>11,11,7,3,17</sub> |  | 4.1<br><sub>2,6,4,5,2</sub> |  | 1.9<br><sub>1,0,0,1,0</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.3 | 0.8 | 1.1 | 16.7 |
| AJ Dybantsa | 80% | 27.4<br><sub>-,-,-,-,27</sub> | 13.6<br><sub>-,-,-,-,19</sub> | 15.5 · – | 3.3<br><sub>-,-,-,-,2</sub> | 4.5 | 2.0<br><sub>-,-,-,-,2</sub> | 2.5 | 1.0<br><sub>-,-,-,-,1</sub> | 1.5 | 0.9 | 0.6 | 1.6 | 18.9 |
| Alex Sarr | 96% | 25.8<br><sub>24,25,23,26,26</sub> | 11.3<br><sub>6,7,10,12,18</sub> | 10.5 · – | 5.6<br><sub>9,4,2,6,4</sub> | 5.5 | 2.3<br><sub>2,5,3,1,2</sub> | 2.5 | 1.0<br><sub>0,1,0,0,2</sub> |  | 0.8 | 1.6 | 1.2 | 19.2 |
| Bub Carrington | 98% | 23.9<br><sub>19,11,21,28,20</sub> | 8.4<br><sub>10,3,9,6,3</sub> |  | 2.4<br><sub>1,1,2,0,1</sub> |  | 3.2<br><sub>4,0,1,3,3</sub> |  | 1.3<br><sub>2,1,3,2,0</sub> |  | 0.6 | 0.2 | 1.3 | 14.0 |
| Khris Middleton | 83% | 19.0<br><sub>12,16,-,13,23</sub> | 6.4<br><sub>2,6,-,0,4</sub> |  | 2.7<br><sub>2,2,-,1,3</sub> |  | 1.4<br><sub>0,0,-,0,2</sub> |  | 0.6<br><sub>0,0,-,0,1</sub> |  | 0.6 | 0.1 | 1.2 | 10.5 |
| Deandre Ayton | 98% | 15.6<br><sub>15,14,16,12,12</sub> | 5.8<br><sub>11,4,6,0,10</sub> |  | 4.5<br><sub>4,6,5,4,3</sub> |  | 0.6<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 10.9 |
| Will Riley | 63% | 9.6<br><sub>-,1,5,4,-</sub> | 4.2<br><sub>-,0,2,2,-</sub> |  | 1.2<br><sub>-,0,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.5 | 6.2 |
| Anthony Gill | 38% | 9.5<br><sub>-,1,-,-,-</sub> | 3.2<br><sub>-,0,-,-,-</sub> |  | 1.5<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |
| Reece Beekman | 38% | 8.2<br><sub>-,1,-,-,-</sub> | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.3 |
| Tre Mann | 38% | 7.5<br><sub>-,1,-,-,-</sub> | 2.9<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Felix Okpara | 38% | 7.2<br><sub>-,1,-,-,-</sub> | 3.2<br><sub>-,1,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.9 |

</details>

<details><summary>if Dennis Schroder plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller (CHA) | 98% | 31.9<br><sub>36,23,36,36,38</sub> | 27.3<br><sub>18,6,34,39,31</sub> | 27.5 · – | 5.3<br><sub>3,2,8,6,12</sub> | 5.5 | 3.1<br><sub>1,0,4,1,3</sub> | 3.5 | 3.4<br><sub>3,1,3,5,3</sub> | 3.5 | 1.2 | 0.7 | 2.8 | 35.6 |
| Dennis Schroder (CHA) | 100% | 31.4<br><sub>35,20,38,36,34</sub> | 14.6<br><sub>19,4,25,8,14</sub> | 14.5 · – | 3.5<br><sub>4,4,6,2,4</sub> | 3.5 | 5.4<br><sub>6,3,4,5,5</sub> | 5.5 | 1.1<br><sub>0,0,3,0,2</sub> | 1.5 | 1.1 | 0.2 | 2.6 | 23.5 |
| Grayson Allen (CHA) | 96% | 28.3<br><sub>29,20,34,28,30</sub> | 16.7<br><sub>21,11,20,15,9</sub> | 14.5 · – | 3.4<br><sub>3,2,3,2,5</sub> | 2.5 | 3.5<br><sub>4,3,5,1,2</sub> | 3.5 | 2.8<br><sub>5,3,4,2,2</sub> | 2.5 | 1.2 | 0.3 | 1.9 | 23.6 |
| Moussa Diabate (CHA) | 98% | 28.2<br><sub>34,21,22,35,35</sub> | 9.6<br><sub>17,5,4,11,9</sub> | 9.5 · – | 9.7<br><sub>8,8,5,17,9</sub> | 10.5 | 2.5<br><sub>3,1,2,3,2</sub> | 1.5 | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.1 | 1.1 | 1.4 | 21.8 |
| Naz Reid (CHA) | 98% | 24.7<br><sub>33,25,37,29,13</sub> | 15.8<br><sub>20,17,23,18,7</sub> | 17.5 · – | 7.1<br><sub>11,6,9,12,6</sub> | 7.5 | 2.1<br><sub>7,2,0,1,0</sub> | 2.5 | 2.1<br><sub>4,3,5,2,1</sub> | 2.5 | 0.8 | 0.8 | 2.0 | 25.1 |
| Sion James (CHA) | 98% | 23.3<br><sub>27,24,26,29,23</sub> | 6.0<br><sub>3,3,0,5,5</sub> | 5.5 · – | 3.6<br><sub>3,2,5,2,2</sub> | 3.5 | 2.6<br><sub>0,5,5,3,3</sub> | 3.5 | 0.8<br><sub>1,1,0,1,1</sub> | 1.5 | 0.9 | 0.2 | 0.8 | 12.1 |
| Royce O'Neale (CHA) | 98% | 20.3<br><sub>17,17,11,7,34</sub> | 6.6<br><sub>8,6,0,0,9</sub> |  | 3.5<br><sub>4,2,1,0,4</sub> |  | 1.3<br><sub>0,0,0,1,0</sub> |  | 1.2<br><sub>2,2,0,0,3</sub> |  | 0.9 | 0.4 | 0.7 | 11.4 |
| Ryan Kalkbrenner (CHA) | 98% | 16.4<br><sub>14,19,23,13,13</sub> | 6.2<br><sub>4,6,6,6,1</sub> |  | 4.5<br><sub>5,7,5,4,1</sub> |  | 0.9<br><sub>3,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.4 | 1.3 | 0.8 | 11.7 |
| Tidjane Salaun (CHA) | 86% | 15.1<br><sub>-,23,10,16,12</sub> | 6.0<br><sub>-,11,3,5,2</sub> |  | 3.7<br><sub>-,5,3,5,2</sub> |  | 0.8<br><sub>-,1,0,0,0</sub> |  | 0.7<br><sub>-,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.7 | 10.4 |
| Christian Anderson (CHA) | 96% | 11.3<br><sub>13,16,3,11,9</sub> | 5.0<br><sub>0,2,0,3,2</sub> |  | 1.5<br><sub>2,0,1,4,0</sub> |  | 1.3<br><sub>2,2,0,1,1</sub> |  | 0.4<br><sub>0,0,0,1,0</sub> |  | 0.5 | 0.1 | 1.0 | 7.8 |
| PJ Hall (CHA) | 38% | 8.8<br><sub>-,10,-,-,-</sub> | 3.7<br><sub>-,0,-,-,-</sub> |  | 3.1<br><sub>-,1,-,-,-</sub> |  | 0.6<br><sub>-,3,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.4 | 0.7 | 7.4 |
| Liam McNeeley (CHA) | 48% | 8.6<br><sub>3,12,-,-,-</sub> | 3.4<br><sub>0,4,-,-,-</sub> |  | 1.8<br><sub>1,4,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 0.3<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.9 |
| Hannes Steinbach (CHA) | 36% | 8.3<br><sub>-,12,-,-,-</sub> | 3.2<br><sub>-,6,-,-,-</sub> |  | 2.5<br><sub>-,5,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.5 | 6.0 |
| Trae Young (WAS) | 98% | 34.4<br><sub>38,37,34,38,34</sub> | 19.9<br><sub>20,22,25,22,14</sub> | 19.5 · – | 2.9<br><sub>0,1,4,6,5</sub> | 2.5 | 9.7<br><sub>13,12,9,10,8</sub> | 9.5 | 2.4<br><sub>0,4,4,1,1</sub> | 2.5 | 1.0 | 0.2 | 3.2 | 32.6 |
| Anthony Davis (WAS) | 98% | 34.2<br><sub>34,32,31,36,34</sub> | 20.9<br><sub>34,9,19,29,18</sub> | 20.5 · – | 10.3<br><sub>12,9,6,10,5</sub> | 9.5 | 2.9<br><sub>4,0,4,0,3</sub> | 2.5 | 0.9<br><sub>1,0,0,3,2</sub> | 0.5 | 1.1 | 1.7 | 2.1 | 34.1 |
| Kyshawn George (WAS) | 98% | 32.2<br><sub>29,26,36,29,38</sub> | 15.2<br><sub>18,11,22,20,8</sub> | 12.5 · – | 4.8<br><sub>5,3,9,4,2</sub> | 4.5 | 4.0<br><sub>3,3,5,2,11</sub> | 3.5 | 1.9<br><sub>1,1,0,2,0</sub> | 1.5 | 1.1 | 1.0 | 2.2 | 24.0 |
| Bilal Coulibaly (WAS) | 98% | 28.1<br><sub>29,26,25,29,27</sub> | 10.7<br><sub>11,11,7,3,17</sub> |  | 4.1<br><sub>2,6,4,5,2</sub> |  | 1.9<br><sub>1,0,0,1,0</sub> |  | 1.1<br><sub>1,1,0,0,1</sub> |  | 1.3 | 0.9 | 1.1 | 16.6 |
| AJ Dybantsa (WAS) | 80% | 27.4<br><sub>-,-,-,-,27</sub> | 13.4<br><sub>-,-,-,-,19</sub> | 15.5 · – | 3.4<br><sub>-,-,-,-,2</sub> | 4.5 | 1.9<br><sub>-,-,-,-,2</sub> | 2.5 | 0.9<br><sub>-,-,-,-,1</sub> | 1.5 | 0.9 | 0.6 | 1.6 | 18.7 |
| Alex Sarr (WAS) | 96% | 25.8<br><sub>24,25,23,26,26</sub> | 11.3<br><sub>6,7,10,12,18</sub> | 10.5 · – | 5.6<br><sub>9,4,2,6,4</sub> | 5.5 | 2.3<br><sub>2,5,3,1,2</sub> | 2.5 | 1.0<br><sub>0,1,0,0,2</sub> |  | 0.8 | 1.6 | 1.2 | 19.2 |
| Bub Carrington (WAS) | 98% | 23.9<br><sub>19,11,21,28,20</sub> | 8.3<br><sub>10,3,9,6,3</sub> |  | 2.4<br><sub>1,1,2,0,1</sub> |  | 3.2<br><sub>4,0,1,3,3</sub> |  | 1.3<br><sub>2,1,3,2,0</sub> |  | 0.7 | 0.2 | 1.3 | 13.9 |
| Khris Middleton (WAS) | 83% | 19.0<br><sub>12,16,-,13,23</sub> | 6.3<br><sub>2,6,-,0,4</sub> |  | 2.7<br><sub>2,2,-,1,3</sub> |  | 1.4<br><sub>0,0,-,0,2</sub> |  | 0.7<br><sub>0,0,-,0,1</sub> |  | 0.6 | 0.1 | 1.2 | 10.4 |
| Deandre Ayton (WAS) | 98% | 15.6<br><sub>15,14,16,12,12</sub> | 5.8<br><sub>11,4,6,0,10</sub> |  | 4.5<br><sub>4,6,5,4,3</sub> |  | 0.6<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.6 | 0.7 | 10.9 |
| Will Riley (WAS) | 63% | 9.6<br><sub>-,1,5,4,-</sub> | 4.2<br><sub>-,0,2,2,-</sub> |  | 1.2<br><sub>-,0,0,0,-</sub> |  | 0.8<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.4 | 0.1 | 0.6 | 6.2 |
| Anthony Gill (WAS) | 38% | 9.5<br><sub>-,1,-,-,-</sub> | 3.2<br><sub>-,0,-,-,-</sub> |  | 1.5<br><sub>-,0,-,-,-</sub> |  | 0.6<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.3 |
| Reece Beekman (WAS) | 38% | 8.2<br><sub>-,1,-,-,-</sub> | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.3 |
| Tre Mann (WAS) | 38% | 7.5<br><sub>-,1,-,-,-</sub> | 2.9<br><sub>-,0,-,-,-</sub> |  | 1.0<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.6 |
| Felix Okpara (WAS) | 38% | 7.2<br><sub>-,1,-,-,-</sub> | 3.2<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.3 | 0.4 | 3.9 |

</details>

<details><summary>if Tre Johnson plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandon Miller (CHA) | 98% | 34.6<br><sub>36,23,36,36,38</sub> | 30.3<br><sub>18,6,34,39,31</sub> | 27.5 · – | 5.9<br><sub>3,2,8,6,12</sub> | 5.5 | 3.6<br><sub>1,0,4,1,3</sub> | 3.5 | 3.6<br><sub>3,1,3,5,3</sub> | 3.5 | 1.3 | 0.7 | 3.1 | 39.8 |
| Grayson Allen (CHA) | 96% | 31.5<br><sub>29,20,34,28,30</sub> | 19.9<br><sub>21,11,20,15,9</sub> | 14.5 · – | 3.7<br><sub>3,2,3,2,5</sub> | 2.5 | 4.5<br><sub>4,3,5,1,2</sub> | 3.5 | 3.0<br><sub>5,3,4,2,2</sub> | 2.5 | 1.3 | 0.3 | 2.3 | 28.1 |
| Moussa Diabate (CHA) | 98% | 30.5<br><sub>34,21,22,35,35</sub> | 10.2<br><sub>17,5,4,11,9</sub> | 9.5 · – | 10.6<br><sub>8,8,5,17,9</sub> | 10.5 | 2.8<br><sub>3,1,2,3,2</sub> | 1.5 | 0.0<br><sub>0,0,0,0,0</sub> |  | 1.3 | 1.1 | 1.7 | 23.7 |
| Naz Reid (CHA) | 98% | 27.1<br><sub>33,25,37,29,13</sub> | 18.7<br><sub>20,17,23,18,7</sub> | 17.5 · – | 7.6<br><sub>11,6,9,12,6</sub> | 7.5 | 2.4<br><sub>7,2,0,1,0</sub> | 2.5 | 2.2<br><sub>4,3,5,2,1</sub> | 2.5 | 0.8 | 0.8 | 2.2 | 28.7 |
| Sion James (CHA) | 98% | 26.6<br><sub>27,24,26,29,23</sub> | 6.8<br><sub>3,3,0,5,5</sub> | 5.5 · – | 4.0<br><sub>3,2,5,2,2</sub> | 3.5 | 3.0<br><sub>0,5,5,3,3</sub> | 3.5 | 0.9<br><sub>1,1,0,1,1</sub> | 1.5 | 1.0 | 0.3 | 1.1 | 13.9 |
| Royce O'Neale (CHA) | 98% | 24.1<br><sub>17,17,11,7,34</sub> | 8.1<br><sub>8,6,0,0,9</sub> |  | 4.3<br><sub>4,2,1,0,4</sub> |  | 1.6<br><sub>0,0,0,1,0</sub> |  | 1.5<br><sub>2,2,0,0,3</sub> |  | 1.0 | 0.5 | 0.9 | 14.0 |
| Ryan Kalkbrenner (CHA) | 98% | 18.3<br><sub>14,19,23,13,13</sub> | 6.5<br><sub>4,6,6,6,1</sub> |  | 5.0<br><sub>5,7,5,4,1</sub> |  | 1.1<br><sub>3,1,2,1,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.4 | 0.8 | 12.6 |
| Tidjane Salaun (CHA) | 86% | 17.3<br><sub>-,23,10,16,12</sub> | 6.4<br><sub>-,11,3,5,2</sub> |  | 4.2<br><sub>-,5,3,5,2</sub> |  | 0.9<br><sub>-,1,0,0,0</sub> |  | 0.7<br><sub>-,1,1,1,0</sub> |  | 0.5 | 0.2 | 0.8 | 11.5 |
| Christian Anderson (CHA) | 96% | 14.4<br><sub>13,16,3,11,9</sub> | 6.3<br><sub>0,2,0,3,2</sub> |  | 2.0<br><sub>2,0,1,4,0</sub> |  | 1.6<br><sub>2,2,0,1,1</sub> |  | 0.6<br><sub>0,0,0,1,0</sub> |  | 0.6 | 0.2 | 1.1 | 9.9 |
| Liam McNeeley (CHA) | 48% | 13.3<br><sub>3,12,-,-,-</sub> | 4.6<br><sub>0,4,-,-,-</sub> |  | 2.7<br><sub>1,4,-,-,-</sub> |  | 1.0<br><sub>0,0,-,-,-</sub> |  | 0.5<br><sub>0,0,-,-,-</sub> |  | 0.4 | 0.1 | 0.7 | 8.3 |
| PJ Hall (CHA) | 38% | 11.9<br><sub>-,10,-,-,-</sub> | 4.7<br><sub>-,0,-,-,-</sub> |  | 4.2<br><sub>-,1,-,-,-</sub> |  | 0.8<br><sub>-,3,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.2 | 0.6 | 0.9 | 9.7 |
| Hannes Steinbach (CHA) | 36% | 11.1<br><sub>-,12,-,-,-</sub> | 4.4<br><sub>-,6,-,-,-</sub> |  | 3.4<br><sub>-,5,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 8.3 |
| Trae Young (WAS) | 98% | 33.3<br><sub>38,37,34,38,34</sub> | 19.0<br><sub>20,22,25,22,14</sub> | 19.5 · – | 2.8<br><sub>0,1,4,6,5</sub> | 2.5 | 9.3<br><sub>13,12,9,10,8</sub> | 9.5 | 2.3<br><sub>0,4,4,1,1</sub> | 2.5 | 1.1 | 0.2 | 3.2 | 31.1 |
| Anthony Davis (WAS) | 98% | 32.9<br><sub>34,32,31,36,34</sub> | 20.6<br><sub>34,9,19,29,18</sub> | 20.5 · – | 9.6<br><sub>12,9,6,10,5</sub> | 9.5 | 2.7<br><sub>4,0,4,0,3</sub> | 2.5 | 0.8<br><sub>1,0,0,3,2</sub> | 0.5 | 1.1 | 1.6 | 1.9 | 32.9 |
| Kyshawn George (WAS) | 98% | 30.7<br><sub>29,26,36,29,38</sub> | 14.5<br><sub>18,11,22,20,8</sub> | 12.5 · – | 4.5<br><sub>5,3,9,4,2</sub> | 4.5 | 3.9<br><sub>3,3,5,2,11</sub> | 3.5 | 1.8<br><sub>1,1,0,2,0</sub> | 1.5 | 1.1 | 1.0 | 2.1 | 22.9 |
| Bilal Coulibaly (WAS) | 98% | 26.3<br><sub>29,26,25,29,27</sub> | 9.8<br><sub>11,11,7,3,17</sub> |  | 3.9<br><sub>2,6,4,5,2</sub> |  | 1.8<br><sub>1,0,0,1,0</sub> |  | 1.0<br><sub>1,1,0,0,1</sub> |  | 1.2 | 0.8 | 1.1 | 15.5 |
| AJ Dybantsa (WAS) | 80% | 25.7<br><sub>-,-,-,-,27</sub> | 12.8<br><sub>-,-,-,-,19</sub> | 15.5 · – | 3.2<br><sub>-,-,-,-,2</sub> | 4.5 | 1.9<br><sub>-,-,-,-,2</sub> | 2.5 | 0.9<br><sub>-,-,-,-,1</sub> | 1.5 | 0.9 | 0.6 | 1.6 | 17.9 |
| Alex Sarr (WAS) | 96% | 24.4<br><sub>24,25,23,26,26</sub> | 10.9<br><sub>6,7,10,12,18</sub> | 10.5 · – | 5.3<br><sub>9,4,2,6,4</sub> | 5.5 | 2.2<br><sub>2,5,3,1,2</sub> | 2.5 | 0.9<br><sub>0,1,0,0,2</sub> |  | 0.8 | 1.6 | 1.3 | 18.5 |
| Bub Carrington (WAS) | 98% | 20.3<br><sub>19,11,21,28,20</sub> | 7.0<br><sub>10,3,9,6,3</sub> |  | 2.0<br><sub>1,1,2,0,1</sub> |  | 2.8<br><sub>4,0,1,3,3</sub> |  | 1.1<br><sub>2,1,3,2,0</sub> |  | 0.6 | 0.1 | 1.2 | 11.8 |
| Tre Johnson (WAS) | 100% | 20.3<br><sub>19,26,23,23,-</sub> | 8.0<br><sub>8,20,13,7,-</sub> | 8.5 · – | 2.5<br><sub>1,2,2,3,-</sub> | 2.5 | 1.3<br><sub>0,0,2,2,-</sub> |  | 1.0<br><sub>0,4,2,1,-</sub> | 1.5 | 0.6 | 0.3 | 1.0 | 11.7 |
| Khris Middleton (WAS) | 83% | 17.3<br><sub>12,16,-,13,23</sub> | 5.8<br><sub>2,6,-,0,4</sub> |  | 2.5<br><sub>2,2,-,1,3</sub> |  | 1.3<br><sub>0,0,-,0,2</sub> |  | 0.6<br><sub>0,0,-,0,1</sub> |  | 0.6 | 0.1 | 1.1 | 9.5 |
| Deandre Ayton (WAS) | 98% | 14.5<br><sub>15,14,16,12,12</sub> | 5.2<br><sub>11,4,6,0,10</sub> |  | 4.2<br><sub>4,6,5,4,3</sub> |  | 0.6<br><sub>0,1,0,2,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.5 | 0.7 | 10.0 |
| Will Riley (WAS) | 63% | 8.3<br><sub>-,1,5,4,-</sub> | 3.8<br><sub>-,0,2,2,-</sub> |  | 1.1<br><sub>-,0,0,0,-</sub> |  | 0.7<br><sub>-,0,0,0,-</sub> |  | 0.3<br><sub>-,0,0,0,-</sub> |  | 0.3 | 0.1 | 0.5 | 5.5 |
| Anthony Gill (WAS) | 38% | 8.2<br><sub>-,1,-,-,-</sub> | 2.9<br><sub>-,0,-,-,-</sub> |  | 1.3<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.4 | 4.7 |
| Reece Beekman (WAS) | 38% | 7.2<br><sub>-,1,-,-,-</sub> | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.3<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.0<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.1 |
| Felix Okpara (WAS) | 38% | 6.2<br><sub>-,1,-,-,-</sub> | 2.9<br><sub>-,1,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.4<br><sub>-,0,-,-,-</sub> |  | 0.1<br><sub>-,0,-,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 3.5 |
| Tre Mann (WAS) | 38% | 6.0<br><sub>-,1,-,-,-</sub> | 2.5<br><sub>-,0,-,-,-</sub> |  | 0.8<br><sub>-,0,-,-,-</sub> |  | 0.7<br><sub>-,0,-,-,-</sub> |  | 0.2<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |

</details>


### CHI @ BOS
Out: Devin Carter (BOS), Nic Claxton (CHI)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Payton Pritchard 3PM under 2.5 | CHI @ BOS | draftkings | 2.05 | 2.04 | 1.69 | 59.1% | 45.6% | 49.0% | +0.4% | +21.1% | 0.1% |
| Payton Pritchard PTS under 16.5 | CHI @ BOS | draftkings | 1.91 | 1.90 | 1.58 | 63.2% | 48.9% | 52.5% | +0.2% | +20.6% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 109.0–123.5 | CHI 15% | 6.52 / 1.18 | BOS -14.5 | 232.5 | BOS -14.5 covers 51%; o235.5 43% |
| Expected (weighted by chance each plays) | 109.6–122.6 | CHI 19% | 5.35 / 1.23 | BOS -13.5 | 232.5 | BOS -14.5 covers 46%; o235.5 43% |
| if Jalen Smith plays | 108.9–123.2 | CHI 16% | 6.39 / 1.19 | BOS -14.5 | 231.5 | BOS -14.5 covers 50%; o235.5 43% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tobe Awaka (CHI) | Questionable | 55% | 12.9 | 4.0 | 3.4 | 0.8 | 0.1 | 0.3 | 0.6 | 0.6 | 8.2 | small |
| Patrick Williams (CHI) | Questionable | 55% | 10.9 | 3.5 | 1.6 | 0.7 | 0.4 | 0.3 | 0.2 | 0.6 | 5.9 | small |
| Jalen Smith (CHI) | Questionable | 55% | 23.9 | 10.7 | 6.9 | 1.3 | 1.4 | 0.5 | 0.7 | 0.9 | 19.0 | full tables below |

<details><summary>CHI players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Caleb Wilson | 96% | 35.9<br><sub>32,33,38,32,38</sub> | 18.9<br><sub>16,21,30,17,20</sub> | 17.5 · – | 7.0<br><sub>4,6,14,5,6</sub> | 6.5 | 2.4<br><sub>0,1,3,3,4</sub> | 2.5 | 1.9<br><sub>1,2,1,1,3</sub> | 1.5 | 1.0 | 1.1 | 2.8 | 28.3 |
| Norman Powell | 97% | 32.5<br><sub>22,33,33,24,37</sub> | 19.1<br><sub>15,25,18,20,30</sub> | 19.5 · – | 3.3<br><sub>5,4,2,1,2</sub> | 3.5 | 2.4<br><sub>1,1,3,2,2</sub> | 1.5 | 2.4<br><sub>2,2,3,4,4</sub> | 2.5 | 1.2 | 0.2 | 2.3 | 24.8 |
| Matas Buzelis | 98% | 30.8<br><sub>25,17,35,22,33</sub> | 15.1<br><sub>17,7,21,11,17</sub> | 13.5 · – | 5.8<br><sub>6,5,5,1,5</sub> | 4.5 | 2.0<br><sub>0,3,2,2,3</sub> |  | 1.9<br><sub>0,0,2,2,3</sub> | 1.5 | 0.6 | 1.1 | 2.3 | 22.9 |
| Josh Giddey | 98% | 30.5<br><sub>24,25,30,24,31</sub> | 12.2<br><sub>2,6,9,11,10</sub> | 10.5 · – | 7.2<br><sub>7,4,8,1,8</sub> | 6.5 | 7.6<br><sub>6,9,10,4,11</sub> | 7.5 | 1.5<br><sub>0,0,1,1,1</sub> | 1.5 | 0.9 | 0.5 | 2.6 | 26.9 |
| Leonard Miller | 98% | 21.5<br><sub>26,24,21,14,17</sub> | 9.0<br><sub>4,19,7,9,10</sub> | 9.5 · – | 5.0<br><sub>6,3,4,9,0</sub> | 4.5 | 1.1<br><sub>1,2,0,0,1</sub> |  | 1.0<br><sub>0,2,1,1,1</sub> | 1.5 | 0.5 | 0.4 | 0.9 | 15.1 |
| Tre Jones | 98% | 21.0<br><sub>13,24,18,15,18</sub> | 10.8<br><sub>13,11,10,8,11</sub> | 8.5 · – | 2.8<br><sub>3,3,2,1,4</sub> | 2.5 | 3.6<br><sub>0,8,3,0,3</sub> | 3.5 | 0.5<br><sub>0,0,1,0,1</sub> |  | 0.8 | 0.1 | 1.0 | 17.1 |
| Isaac Okoro | 98% | 20.3<br><sub>18,28,14,11,18</sub> | 6.4<br><sub>4,12,0,1,7</sub> |  | 2.1<br><sub>0,3,1,1,0</sub> |  | 1.2<br><sub>1,1,0,4,1</sub> |  | 0.7<br><sub>0,1,0,0,1</sub> |  | 0.6 | 0.2 | 0.6 | 9.7 |
| Buddy Hield | 88% | 13.3<br><sub>14,15,16,13,9</sub> | 5.2<br><sub>0,13,9,3,2</sub> |  | 1.8<br><sub>2,2,2,0,3</sub> |  | 1.0<br><sub>2,2,2,1,1</sub> |  | 0.7<br><sub>0,3,1,1,0</sub> |  | 0.5 | 0.1 | 0.6 | 8.1 |
| Noa Essengue | 88% | 13.2<br><sub>10,17,-,16,10</sub> | 4.8<br><sub>1,4,-,0,3</sub> |  | 2.0<br><sub>3,1,-,4,0</sub> |  | 0.6<br><sub>0,1,-,0,1</sub> |  | 0.5<br><sub>0,0,-,0,1</sub> |  | 0.6 | 0.2 | 0.5 | 7.4 |
| Zach Collins | 63% | 12.8<br><sub>9,-,11,6,-</sub> | 5.2<br><sub>0,-,2,2,-</sub> |  | 3.9<br><sub>5,-,3,2,-</sub> |  | 1.1<br><sub>0,-,1,0,-</sub> |  | 0.3<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.3 | 0.7 | 10.1 |
| Jaylin Sellers | 52% | 10.2<br><sub>14,-,-,12,-</sub> | 7.0<br><sub>3,-,-,0,-</sub> |  | 1.9<br><sub>1,-,-,0,-</sub> |  | 1.0<br><sub>2,-,-,1,-</sub> |  | 0.6<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.8 | 9.8 |
| Dailyn Swain | 47% | 9.4<br><sub>-,-,-,12,-</sub> | 3.2<br><sub>-,-,-,2,-</sub> |  | 1.3<br><sub>-,-,-,2,-</sub> |  | 1.4<br><sub>-,-,-,2,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.8 | 0.1 | 1.6 | 5.8 |
| Jordan Hawkins | 52% | 9.2<br><sub>-,-,-,7,-</sub> | 3.4<br><sub>-,-,-,4,-</sub> |  | 1.2<br><sub>-,-,-,1,-</sub> |  | 0.6<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 5.2 |

</details>

<details><summary>BOS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum | 98% | 34.0<br><sub>38,37,28,42</sub> | 27.5<br><sub>13,36,23,40</sub> | 27.5 · – | 9.2<br><sub>4,9,7,5</sub> | 7.5 | 6.8<br><sub>11,7,6,8</sub> | 7.5 | 3.1<br><sub>0,3,2,2</sub> | 2.5 | 1.3 | 0.4 | 2.6 | 43.5 |
| Derrick White | 98% | 30.9<br><sub>36,33,18,33</sub> | 14.3<br><sub>17,12,5,16</sub> | 15.5 · – | 4.1<br><sub>1,4,6,5</sub> | 3.5 | 5.1<br><sub>8,6,4,7</sub> | 5.5 | 2.2<br><sub>3,2,1,1</sub> | 2.5 | 1.2 | 1.1 | 1.8 | 23.5 |
| Paul George | 98% | 30.6<br><sub>31,34,25,36</sub> | 19.5<br><sub>38,15,16,20</sub> | 20.5 · – | 5.7<br><sub>5,7,5,7</sub> | 4.5 | 3.3<br><sub>3,2,2,7</sub> | 3.5 | 2.9<br><sub>7,3,3,1</sub> | 3.5 | 1.7 | 0.4 | 2.1 | 28.5 |
| Payton Pritchard | 98% | 27.0<br><sub>28,30,22,24</sub> | 15.1<br><sub>17,4,28,4</sub> | 16.5 · – | 3.3<br><sub>4,1,1,2</sub> | 2.5 | 4.8<br><sub>1,4,4,6</sub> | 4.5 | 2.3<br><sub>2,1,7,0</sub> | 2.5 | 0.8 | 0.1 | 1.2 | 23.2 |
| Sam Hauser | 98% | 22.0<br><sub>18,23,20,25</sub> | 9.1<br><sub>11,6,11,11</sub> |  | 3.8<br><sub>4,2,4,4</sub> |  | 1.3<br><sub>1,2,1,0</sub> |  | 1.8<br><sub>3,2,3,3</sub> |  | 0.5 | 0.2 | 0.5 | 14.2 |
| Mitchell Robinson | 98% | 19.0<br><sub>18,22,16,25</sub> | 6.6<br><sub>4,4,7,7</sub> | 5.5 · – | 7.6<br><sub>3,4,7,5</sub> | 6.5 | 0.7<br><sub>1,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.8 | 1.1 | 0.8 | 14.8 |
| Neemias Queta | 98% | 18.8<br><sub>22,22,19,15</sub> | 8.8<br><sub>3,15,7,7</sub> | 8.5 · – | 6.7<br><sub>4,6,5,3</sub> | 5.5 | 1.2<br><sub>2,1,1,2</sub> |  | 0.1<br><sub>0,1,0,0</sub> |  | 0.7 | 1.3 | 0.9 | 16.8 |
| Jordan Walsh | 96% | 18.5<br><sub>13,20,18,24</sub> | 6.1<br><sub>0,5,4,15</sub> |  | 4.2<br><sub>6,3,3,6</sub> |  | 1.1<br><sub>1,0,2,1</sub> |  | 0.7<br><sub>0,1,0,3</sub> |  | 1.0 | 0.4 | 0.6 | 11.4 |
| Baylor Scheierman | 98% | 17.5<br><sub>18,11,18,21</sub> | 6.1<br><sub>8,2,2,3</sub> |  | 3.4<br><sub>3,0,6,4</sub> |  | 1.6<br><sub>0,0,2,1</sub> |  | 0.9<br><sub>2,0,0,1</sub> |  | 0.8 | 0.1 | 0.6 | 11.1 |
| Luka Garza | 96% | 12.1<br><sub>8,4,13,13</sub> | 7.0<br><sub>2,8,6,2</sub> |  | 3.2<br><sub>2,1,3,4</sub> |  | 0.8<br><sub>0,0,2,0</sub> |  | 0.7<br><sub>0,2,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 11.1 |
| Hugo Gonzalez | 91% | 10.1<br><sub>10,4,24,6</sub> | 3.3<br><sub>0,0,13,0</sub> |  | 2.4<br><sub>3,0,5,2</sub> |  | 0.6<br><sub>0,1,2,0</sub> |  | 0.3<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |
| Dillon Mitchell | 16% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Mike Conley | 52% | 7.9<br><sub>-,-,7,-</sub> | 2.6<br><sub>-,-,6,-</sub> |  | 0.8<br><sub>-,-,0,-</sub> |  | 1.3<br><sub>-,-,0,-</sub> |  | 0.3<br><sub>-,-,2,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Ron Harper Jr. | 48% | 7.3<br><sub>-,-,7,-</sub> | 3.3<br><sub>-,-,3,-</sub> |  | 1.2<br><sub>-,-,1,-</sub> |  | 0.6<br><sub>-,-,0,-</sub> |  | 0.4<br><sub>-,-,1,-</sub> |  | 0.5 | 0.1 | 0.3 | 5.0 |
| Chris Cenac Jr. | 47% | 5.9<br><sub>-,-,5,-</sub> | 2.6<br><sub>-,-,3,-</sub> |  | 1.1<br><sub>-,-,1,-</sub> |  | 0.4<br><sub>-,-,0,-</sub> |  | 0.3<br><sub>-,-,1,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.1 |
| Amari Williams | 16% | 5.7 | 1.8 |  | 1.9 |  | 0.4 |  | 0.0 |  | 0.2 | 0.4 | 0.4 | 4.0 |

</details>

<details><summary>if Jalen Smith plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jayson Tatum (BOS) | 98% | 34.0<br><sub>38,37,28,42</sub> | 27.5<br><sub>13,36,23,40</sub> | 27.5 · – | 9.2<br><sub>4,9,7,5</sub> | 7.5 | 6.7<br><sub>11,7,6,8</sub> | 7.5 | 3.1<br><sub>0,3,2,2</sub> | 2.5 | 1.3 | 0.4 | 2.6 | 43.4 |
| Derrick White (BOS) | 98% | 30.8<br><sub>36,33,18,33</sub> | 14.3<br><sub>17,12,5,16</sub> | 15.5 · – | 4.1<br><sub>1,4,6,5</sub> | 3.5 | 5.1<br><sub>8,6,4,7</sub> | 5.5 | 2.2<br><sub>3,2,1,1</sub> | 2.5 | 1.2 | 1.1 | 1.8 | 23.4 |
| Paul George (BOS) | 98% | 30.7<br><sub>31,34,25,36</sub> | 19.4<br><sub>38,15,16,20</sub> | 20.5 · – | 5.7<br><sub>5,7,5,7</sub> | 4.5 | 3.4<br><sub>3,2,2,7</sub> | 3.5 | 2.9<br><sub>7,3,3,1</sub> | 3.5 | 1.7 | 0.4 | 2.2 | 28.5 |
| Payton Pritchard (BOS) | 98% | 27.0<br><sub>28,30,22,24</sub> | 15.2<br><sub>17,4,28,4</sub> | 16.5 · – | 3.3<br><sub>4,1,1,2</sub> | 2.5 | 4.8<br><sub>1,4,4,6</sub> | 4.5 | 2.3<br><sub>2,1,7,0</sub> | 2.5 | 0.8 | 0.1 | 1.2 | 23.3 |
| Sam Hauser (BOS) | 98% | 22.1<br><sub>18,23,20,25</sub> | 9.1<br><sub>11,6,11,11</sub> |  | 3.8<br><sub>4,2,4,4</sub> |  | 1.3<br><sub>1,2,1,0</sub> |  | 1.8<br><sub>3,2,3,3</sub> |  | 0.5 | 0.2 | 0.5 | 14.2 |
| Mitchell Robinson (BOS) | 98% | 19.0<br><sub>18,22,16,25</sub> | 6.5<br><sub>4,4,7,7</sub> | 5.5 · – | 7.6<br><sub>3,4,7,5</sub> | 6.5 | 0.7<br><sub>1,2,0,0</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.8 | 1.1 | 0.8 | 14.9 |
| Neemias Queta (BOS) | 98% | 18.8<br><sub>22,22,19,15</sub> | 8.8<br><sub>3,15,7,7</sub> | 8.5 · – | 6.7<br><sub>4,6,5,3</sub> | 5.5 | 1.3<br><sub>2,1,1,2</sub> |  | 0.1<br><sub>0,1,0,0</sub> |  | 0.7 | 1.3 | 0.9 | 16.8 |
| Jordan Walsh (BOS) | 96% | 18.5<br><sub>13,20,18,24</sub> | 6.1<br><sub>0,5,4,15</sub> |  | 4.2<br><sub>6,3,3,6</sub> |  | 1.1<br><sub>1,0,2,1</sub> |  | 0.7<br><sub>0,1,0,3</sub> |  | 1.0 | 0.5 | 0.6 | 11.4 |
| Baylor Scheierman (BOS) | 98% | 17.4<br><sub>18,11,18,21</sub> | 6.0<br><sub>8,2,2,3</sub> |  | 3.4<br><sub>3,0,6,4</sub> |  | 1.5<br><sub>0,0,2,1</sub> |  | 0.9<br><sub>2,0,0,1</sub> |  | 0.8 | 0.1 | 0.6 | 10.9 |
| Luka Garza (BOS) | 96% | 12.0<br><sub>8,4,13,13</sub> | 7.0<br><sub>2,8,6,2</sub> |  | 3.2<br><sub>2,1,3,4</sub> |  | 0.8<br><sub>0,0,2,0</sub> |  | 0.6<br><sub>0,2,0,0</sub> |  | 0.4 | 0.3 | 0.7 | 11.0 |
| Hugo Gonzalez (BOS) | 91% | 10.1<br><sub>10,4,24,6</sub> | 3.3<br><sub>0,0,13,0</sub> |  | 2.4<br><sub>3,0,5,2</sub> |  | 0.6<br><sub>0,1,2,0</sub> |  | 0.3<br><sub>0,0,1,0</sub> |  | 0.5 | 0.2 | 0.4 | 6.3 |
| Dillon Mitchell (BOS) | 16% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Mike Conley (BOS) | 52% | 7.9<br><sub>-,-,7,-</sub> | 2.6<br><sub>-,-,6,-</sub> |  | 0.8<br><sub>-,-,0,-</sub> |  | 1.3<br><sub>-,-,0,-</sub> |  | 0.3<br><sub>-,-,2,-</sub> |  | 0.5 | 0.1 | 0.4 | 4.7 |
| Ron Harper Jr. (BOS) | 48% | 7.3<br><sub>-,-,7,-</sub> | 3.2<br><sub>-,-,3,-</sub> |  | 1.2<br><sub>-,-,1,-</sub> |  | 0.6<br><sub>-,-,0,-</sub> |  | 0.4<br><sub>-,-,1,-</sub> |  | 0.5 | 0.1 | 0.2 | 5.0 |
| Chris Cenac Jr. (BOS) | 47% | 6.0<br><sub>-,-,5,-</sub> | 2.7<br><sub>-,-,3,-</sub> |  | 1.1<br><sub>-,-,1,-</sub> |  | 0.4<br><sub>-,-,0,-</sub> |  | 0.3<br><sub>-,-,1,-</sub> |  | 0.1 | 0.1 | 0.2 | 4.1 |
| Amari Williams (BOS) | 16% | 5.5 | 1.7 |  | 1.8 |  | 0.4 |  | 0.0 |  | 0.2 | 0.4 | 0.4 | 3.9 |
| Caleb Wilson (CHI) | 96% | 34.3<br><sub>32,33,38,32,38</sub> | 18.4<br><sub>16,21,30,17,20</sub> | 17.5 · – | 6.4<br><sub>4,6,14,5,6</sub> | 6.5 | 2.2<br><sub>0,1,3,3,4</sub> | 2.5 | 1.7<br><sub>1,2,1,1,3</sub> | 1.5 | 1.0 | 1.1 | 2.7 | 27.1 |
| Norman Powell (CHI) | 97% | 30.1<br><sub>22,33,33,24,37</sub> | 17.7<br><sub>15,25,18,20,30</sub> | 19.5 · – | 3.1<br><sub>5,4,2,1,2</sub> | 3.5 | 2.1<br><sub>1,1,3,2,2</sub> | 1.5 | 2.1<br><sub>2,2,3,4,4</sub> | 2.5 | 1.1 | 0.2 | 2.2 | 23.0 |
| Matas Buzelis (CHI) | 98% | 28.4<br><sub>25,17,35,22,33</sub> | 14.1<br><sub>17,7,21,11,17</sub> | 13.5 · – | 5.3<br><sub>6,5,5,1,5</sub> | 4.5 | 1.8<br><sub>0,3,2,2,3</sub> |  | 1.7<br><sub>0,0,2,2,3</sub> | 1.5 | 0.6 | 0.9 | 2.1 | 21.3 |
| Josh Giddey (CHI) | 98% | 28.2<br><sub>24,25,30,24,31</sub> | 11.2<br><sub>2,6,9,11,10</sub> | 10.5 · – | 6.4<br><sub>7,4,8,1,8</sub> | 6.5 | 7.0<br><sub>6,9,10,4,11</sub> | 7.5 | 1.3<br><sub>0,0,1,1,1</sub> | 1.5 | 0.8 | 0.5 | 2.4 | 24.5 |
| Jalen Smith (CHI) | 100% | 23.9<br><sub>19,24,24,20,30</sub> | 10.7<br><sub>15,14,14,7,17</sub> | 10.5 · – | 6.9<br><sub>8,13,3,6,11</sub> | 7.5 | 1.3<br><sub>1,1,1,1,5</sub> |  | 1.4<br><sub>0,2,2,2,3</sub> | 1.5 | 0.5 | 0.7 | 0.9 | 19.0 |
| Tre Jones (CHI) | 98% | 18.3<br><sub>13,24,18,15,18</sub> | 9.6<br><sub>13,11,10,8,11</sub> | 8.5 · – | 2.3<br><sub>3,3,2,1,4</sub> | 2.5 | 3.0<br><sub>0,8,3,0,3</sub> | 3.5 | 0.4<br><sub>0,0,1,0,1</sub> |  | 0.6 | 0.1 | 0.9 | 14.9 |
| Leonard Miller (CHI) | 98% | 18.3<br><sub>26,24,21,14,17</sub> | 8.1<br><sub>4,19,7,9,10</sub> | 9.5 · – | 4.2<br><sub>6,3,4,9,0</sub> | 4.5 | 0.9<br><sub>1,2,0,0,1</sub> |  | 0.8<br><sub>0,2,1,1,1</sub> | 1.5 | 0.4 | 0.3 | 0.8 | 13.2 |
| Isaac Okoro (CHI) | 98% | 17.3<br><sub>18,28,14,11,18</sub> | 5.4<br><sub>4,12,0,1,7</sub> |  | 1.8<br><sub>0,3,1,1,0</sub> |  | 1.0<br><sub>1,1,0,4,1</sub> |  | 0.5<br><sub>0,1,0,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 8.2 |
| Buddy Hield (CHI) | 88% | 11.5<br><sub>14,15,16,13,9</sub> | 4.7<br><sub>0,13,9,3,2</sub> |  | 1.6<br><sub>2,2,2,0,3</sub> |  | 0.9<br><sub>2,2,2,1,1</sub> |  | 0.6<br><sub>0,3,1,1,0</sub> |  | 0.4 | 0.1 | 0.6 | 7.1 |
| Noa Essengue (CHI) | 88% | 11.2<br><sub>10,17,-,16,10</sub> | 4.1<br><sub>1,4,-,0,3</sub> |  | 1.7<br><sub>3,1,-,4,0</sub> |  | 0.5<br><sub>0,1,-,0,1</sub> |  | 0.3<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.2 | 0.5 | 6.3 |
| Zach Collins (CHI) | 63% | 9.8<br><sub>9,-,11,6,-</sub> | 3.9<br><sub>0,-,2,2,-</sub> |  | 2.9<br><sub>5,-,3,2,-</sub> |  | 0.8<br><sub>0,-,1,0,-</sub> |  | 0.2<br><sub>0,-,0,0,-</sub> |  | 0.2 | 0.2 | 0.6 | 7.7 |
| Jaylin Sellers (CHI) | 52% | 8.2<br><sub>14,-,-,12,-</sub> | 5.6<br><sub>3,-,-,0,-</sub> |  | 1.5<br><sub>1,-,-,0,-</sub> |  | 0.9<br><sub>2,-,-,1,-</sub> |  | 0.4<br><sub>1,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.7 | 8.0 |
| Jordan Hawkins (CHI) | 52% | 7.9<br><sub>-,-,-,7,-</sub> | 3.0<br><sub>-,-,-,4,-</sub> |  | 1.0<br><sub>-,-,-,1,-</sub> |  | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.6 |
| Dailyn Swain (CHI) | 47% | 7.5<br><sub>-,-,-,12,-</sub> | 2.5<br><sub>-,-,-,2,-</sub> |  | 1.0<br><sub>-,-,-,2,-</sub> |  | 1.1<br><sub>-,-,-,2,-</sub> |  | 0.1<br><sub>-,-,-,0,-</sub> |  | 0.6 | 0.1 | 1.3 | 4.6 |

</details>


### DET @ BKN
Out: Egor Demin (BKN), Grant Nelson (BKN), Ben Saraf (BKN), Jalen Duren (DET)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Paul Reed STL over 1.5 (2+) | DET @ BKN | draftkings | 2.76 | 2.75 | 2.35 | 42.5% | 34.2% | 36.3% | +0.2% | +17.3% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.6–103.1 | DET 81% | 1.23 / 5.28 | BKN +12.5 | 218.5 | BKN +8.5 covers 39%; o222.5 42% |
| Expected (weighted by chance each plays) | 115.1–103.3 | DET 80% | 1.25 / 5.06 | BKN +11.5 | 218.5 | BKN +8.5 covers 41%; o222.5 42% |
| if Noah Clowney plays | 115.2–103.5 | DET 80% | 1.25 / 4.92 | BKN +11.5 | 218.5 | BKN +8.5 covers 41%; o222.5 42% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Noah Clowney (BKN) | Day-To-Day | 70% | 22.5 | 8.3 | 4.0 | 1.1 | 1.2 | 0.7 | 0.6 | 0.9 | 13.4 | full tables below |
| Drake Powell (BKN) | Questionable | 55% | 15.3 | 4.8 | 1.3 | 1.0 | 0.5 | 0.5 | 0.2 | 0.8 | 7.0 | small |
| Isaiah Joe (DET) | Questionable | 55% | 13.0 | 7.1 | 1.6 | 0.9 | 1.1 | 0.5 | 0.1 | 0.7 | 9.6 | small |
| Elijah Harkless (DET) | Questionable | 55% | 7.7 | 0.5 | 0.3 | 0.4 | 0.0 | 0.2 | 0.3 | 0.4 | 1.2 | small |

<details><summary>DET players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Cade Cunningham | 98% | 34.8<br><sub>35,30,33,36,39</sub> | 25.6<br><sub>22,16,26,19,30</sub> | 24.5 · – | 5.5<br><sub>4,2,8,9,5</sub> | 5.5 | 8.5<br><sub>8,8,8,8,7</sub> | 8.5 | 2.2<br><sub>1,2,3,2,4</sub> | 2.5 | 1.4 | 0.9 | 4.5 | 39.7 |
| Duncan Robinson | 98% | 30.8<br><sub>28,28,32,33,32</sub> | 15.1<br><sub>21,17,21,12,13</sub> | 13.5 · – | 2.9<br><sub>2,1,3,0,2</sub> | 2.5 | 2.7<br><sub>2,2,3,2,2</sub> | 1.5 | 2.9<br><sub>5,5,5,2,3</sub> | 2.5 | 1.0 | 0.3 | 1.3 | 20.7 |
| Paul Reed | 96% | 27.7<br><sub>17,26,23,26,38</sub> | 15.9<br><sub>6,19,8,22,16</sub> | 15.5 · – | 8.6<br><sub>6,11,8,9,4</sub> | 9.5 | 2.4<br><sub>2,3,2,3,0</sub> | 2.5 | 0.6<br><sub>0,2,0,1,2</sub> |  | 1.6 | 1.6 | 1.9 | 26.9 |
| Ausar Thompson | 98% | 27.6<br><sub>33,19,-,25,29</sub> | 9.9<br><sub>11,4,-,11,7</sub> | 10.5 · – | 6.6<br><sub>11,3,-,6,9</sub> | 6.5 | 4.0<br><sub>5,5,-,2,8</sub> | 3.5 | 0.1<br><sub>0,0,-,0,0</sub> |  | 2.1 | 1.4 | 2.0 | 20.5 |
| Daniss Jenkins | 98% | 26.3<br><sub>15,22,38,24,24</sub> | 11.8<br><sub>3,15,18,11,14</sub> | 10.5 · – | 3.4<br><sub>2,5,8,3,2</sub> | 2.5 | 4.5<br><sub>3,5,6,2,3</sub> | 4.5 | 1.3<br><sub>1,1,3,1,2</sub> | 1.5 | 1.0 | 0.3 | 1.8 | 19.6 |
| John Collins | 98% | 26.3<br><sub>25,29,34,27,18</sub> | 11.8<br><sub>6,23,16,2,4</sub> | 14.5 · – | 6.1<br><sub>5,7,11,9,2</sub> | 7.5 | 1.2<br><sub>1,1,0,1,0</sub> |  | 1.1<br><sub>0,5,2,0,0</sub> | 1.5 | 0.9 | 0.9 | 1.4 | 19.2 |
| Kevin Huerter | 93% | 21.3<br><sub>18,20,26,16,19</sub> | 8.6<br><sub>3,5,9,7,3</sub> |  | 3.0<br><sub>3,6,3,1,2</sub> |  | 2.5<br><sub>2,2,2,0,3</sub> |  | 1.2<br><sub>1,1,1,1,1</sub> |  | 1.0 | 0.3 | 1.0 | 14.1 |
| Javonte Green | 93% | 20.8<br><sub>18,13,22,17,21</sub> | 7.4<br><sub>19,5,2,3,7</sub> |  | 3.3<br><sub>4,3,3,1,2</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 1.1<br><sub>5,1,0,1,1</sub> |  | 1.4 | 0.5 | 0.7 | 11.6 |
| Ronald Holland II | 96% | 16.5<br><sub>3,22,23,12,12</sub> | 6.2<br><sub>0,8,2,4,0</sub> |  | 3.6<br><sub>1,5,9,3,2</sub> |  | 1.3<br><sub>1,4,4,2,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.9 | 0.5 | 1.0 | 11.1 |
| Taurean Prince | 66% | 11.4<br><sub>-,-,-,7,6</sub> | 4.2<br><sub>-,-,-,3,1</sub> |  | 1.7<br><sub>-,-,-,0,2</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,1,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.7 |
| Isaac Jones | 21% | 7.7<br><sub>-,-,-,3,-</sub> | 0.5<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 1.3 |
| Tolu Smith | 76% | 7.6<br><sub>-,2,3,6,1</sub> | 3.1<br><sub>-,0,0,1,2</sub> |  | 2.4<br><sub>-,1,1,4,1</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 6.0 |
| Ebuka Okorie | 52% | 6.8<br><sub>-,-,2,4,-</sub> | 2.1<br><sub>-,-,2,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 3.0 |
| Chaz Lanier | 38% | 6.8<br><sub>-,-,-,2,-</sub> | 2.7<br><sub>-,-,-,2,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.7 |

</details>

<details><summary>BKN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle | 98% | 36.1<br><sub>38,35,24,44</sub> | 20.5<br><sub>33,23,10,24</sub> | 19.5 · – | 7.7<br><sub>8,6,7,9</sub> | 6.5 | 5.6<br><sub>7,5,7,4</sub> | 5.5 | 1.3<br><sub>3,2,0,0</sub> | 1.5 | 1.1 | 0.3 | 3.8 | 33.7 |
| Michael Porter Jr. | 98% | 34.4<br><sub>34,33,21,40</sub> | 22.7<br><sub>26,28,10,27</sub> | 21.5 · – | 6.9<br><sub>7,9,0,12</sub> | 6.5 | 2.5<br><sub>1,1,0,2</sub> | 1.5 | 2.9<br><sub>5,4,0,6</sub> | 3.5 | 1.3 | 0.5 | 2.5 | 32.1 |
| Keon Ellis | 91% | 26.9<br><sub>34,22,23,25</sub> | 7.0<br><sub>7,6,9,2</sub> | 6.5 · – | 2.4<br><sub>2,2,1,3</sub> | 2.5 | 2.1<br><sub>4,1,3,4</sub> |  | 1.1<br><sub>1,2,1,0</sub> | 1.5 | 1.5 | 0.7 | 0.9 | 11.6 |
| Mikel Brown Jr. | 91% | 25.6<br><sub>20,20,-,28</sub> | 11.1<br><sub>6,8,-,17</sub> | 11.5 · – | 3.2<br><sub>3,2,-,5</sub> | 3.5 | 4.5<br><sub>3,5,-,5</sub> | 3.5 | 1.5<br><sub>1,2,-,4</sub> | 1.5 | 0.7 | 0.2 | 1.8 | 18.8 |
| Chaney Johnson | 88% | 24.4<br><sub>5,27,21,29</sub> | 8.4<br><sub>0,10,4,15</sub> |  | 3.7<br><sub>1,5,5,3</sub> |  | 1.5<br><sub>0,3,0,2</sub> |  | 1.1<br><sub>0,2,0,3</sub> |  | 0.8 | 0.3 | 1.3 | 13.6 |
| Nolan Traore | 98% | 21.8<br><sub>16,5,25,24</sub> | 9.6<br><sub>3,3,17,15</sub> | 9.5 · – | 1.9<br><sub>2,2,2,1</sub> |  | 3.6<br><sub>0,0,5,3</sub> | 3.5 | 1.0<br><sub>0,0,2,1</sub> |  | 0.9 | 0.5 | 2.1 | 15.1 |
| Day'Ron Sharpe | 98% | 21.7<br><sub>30,23,16,17</sub> | 9.3<br><sub>8,7,11,4</sub> | 8.5 · – | 7.4<br><sub>8,8,4,6</sub> | 7.5 | 2.4<br><sub>3,1,1,0</sub> | 2.5 | 0.3<br><sub>0,1,1,0</sub> |  | 1.1 | 0.8 | 1.8 | 19.1 |
| Moritz Wagner | 88% | 18.0<br><sub>16,14,15,22</sub> | 9.0<br><sub>7,6,13,15</sub> | 7.5 · – | 4.1<br><sub>0,4,3,4</sub> | 3.5 | 1.5<br><sub>1,1,1,3</sub> |  | 0.8<br><sub>1,1,2,2</sub> | 0.5 | 0.7 | 0.3 | 1.3 | 14.6 |
| Josh Minott | 58% | 16.9<br><sub>-,9,21,-</sub> | 8.2<br><sub>-,4,15,-</sub> |  | 3.1<br><sub>-,2,8,-</sub> |  | 1.0<br><sub>-,0,2,-</sub> |  | 1.1<br><sub>-,0,3,-</sub> |  | 1.0 | 0.7 | 1.0 | 12.3 |
| Terance Mann | 35% | 16.3<br><sub>-,-,-,-</sub> | 4.7<br><sub>-,-,-,-</sub> |  | 2.1<br><sub>-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-</sub> |  | 0.5 | 0.2 | 0.8 | 8.5 |
| Danny Wolf | 52% | 15.3<br><sub>-,-,15,-</sub> | 6.4<br><sub>-,-,6,-</sub> |  | 3.5<br><sub>-,-,2,-</sub> |  | 1.6<br><sub>-,-,1,-</sub> |  | 0.7<br><sub>-,-,2,-</sub> |  | 0.4 | 0.5 | 1.0 | 11.4 |

</details>

<details><summary>if Noah Clowney plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Julius Randle (BKN) | 98% | 35.2<br><sub>38,35,24,44</sub> | 19.2<br><sub>33,23,10,24</sub> | 19.5 · – | 7.5<br><sub>8,6,7,9</sub> | 6.5 | 5.3<br><sub>7,5,7,4</sub> | 5.5 | 1.3<br><sub>3,2,0,0</sub> | 1.5 | 1.1 | 0.3 | 3.5 | 32.1 |
| Michael Porter Jr. (BKN) | 98% | 33.4<br><sub>34,33,21,40</sub> | 20.8<br><sub>26,28,10,27</sub> | 21.5 · – | 6.8<br><sub>7,9,0,12</sub> | 6.5 | 2.3<br><sub>1,1,0,2</sub> | 1.5 | 2.7<br><sub>5,4,0,6</sub> | 3.5 | 1.2 | 0.5 | 2.4 | 29.8 |
| Keon Ellis (BKN) | 91% | 25.7<br><sub>34,22,23,25</sub> | 7.2<br><sub>7,6,9,2</sub> | 6.5 · – | 2.3<br><sub>2,2,1,3</sub> | 2.5 | 2.0<br><sub>4,1,3,4</sub> |  | 1.1<br><sub>1,2,1,0</sub> | 1.5 | 1.4 | 0.7 | 0.8 | 11.5 |
| Mikel Brown Jr. (BKN) | 91% | 23.5<br><sub>20,20,-,28</sub> | 10.2<br><sub>6,8,-,17</sub> | 11.5 · – | 2.9<br><sub>3,2,-,5</sub> | 3.5 | 3.8<br><sub>3,5,-,5</sub> | 3.5 | 1.3<br><sub>1,2,-,4</sub> | 1.5 | 0.7 | 0.1 | 1.7 | 16.9 |
| Noah Clowney (BKN) | 100% | 22.5<br><sub>22,20,20,24</sub> | 8.3<br><sub>9,4,9,3</sub> |  | 4.0<br><sub>3,4,5,4</sub> |  | 1.1<br><sub>1,0,1,1</sub> |  | 1.2<br><sub>1,1,1,1</sub> |  | 0.7 | 0.6 | 0.9 | 13.4 |
| Chaney Johnson (BKN) | 88% | 22.1<br><sub>5,27,21,29</sub> | 7.9<br><sub>0,10,4,15</sub> |  | 3.4<br><sub>1,5,5,3</sub> |  | 1.3<br><sub>0,3,0,2</sub> |  | 1.0<br><sub>0,2,0,3</sub> |  | 0.7 | 0.3 | 1.1 | 12.6 |
| Day'Ron Sharpe (BKN) | 98% | 20.3<br><sub>30,23,16,17</sub> | 8.6<br><sub>8,7,11,4</sub> | 8.5 · – | 6.7<br><sub>8,8,4,6</sub> | 7.5 | 2.2<br><sub>3,1,1,0</sub> | 2.5 | 0.3<br><sub>0,1,1,0</sub> |  | 0.9 | 0.7 | 1.6 | 17.5 |
| Nolan Traore (BKN) | 98% | 19.5<br><sub>16,5,25,24</sub> | 8.2<br><sub>3,3,17,15</sub> | 9.5 · – | 1.7<br><sub>2,2,2,1</sub> |  | 3.1<br><sub>0,0,5,3</sub> | 3.5 | 0.8<br><sub>0,0,2,1</sub> |  | 0.8 | 0.4 | 1.8 | 13.0 |
| Moritz Wagner (BKN) | 88% | 17.1<br><sub>16,14,15,22</sub> | 8.9<br><sub>7,6,13,15</sub> | 7.5 · – | 3.8<br><sub>0,4,3,4</sub> | 3.5 | 1.4<br><sub>1,1,1,3</sub> |  | 0.7<br><sub>1,1,2,2</sub> | 0.5 | 0.7 | 0.3 | 1.2 | 14.1 |
| Josh Minott (BKN) | 58% | 13.7<br><sub>-,9,21,-</sub> | 6.6<br><sub>-,4,15,-</sub> |  | 2.5<br><sub>-,2,8,-</sub> |  | 0.8<br><sub>-,0,2,-</sub> |  | 0.8<br><sub>-,0,3,-</sub> |  | 0.8 | 0.5 | 0.8 | 9.9 |
| Terance Mann (BKN) | 35% | 13.2<br><sub>-,-,-,-</sub> | 3.9<br><sub>-,-,-,-</sub> |  | 1.8<br><sub>-,-,-,-</sub> |  | 1.3<br><sub>-,-,-,-</sub> |  | 0.3<br><sub>-,-,-,-</sub> |  | 0.4 | 0.2 | 0.6 | 7.0 |
| Danny Wolf (BKN) | 52% | 13.0<br><sub>-,-,15,-</sub> | 5.3<br><sub>-,-,6,-</sub> |  | 3.0<br><sub>-,-,2,-</sub> |  | 1.3<br><sub>-,-,1,-</sub> |  | 0.6<br><sub>-,-,2,-</sub> |  | 0.3 | 0.4 | 0.8 | 9.6 |
| Cade Cunningham (DET) | 98% | 34.8<br><sub>35,30,33,36,39</sub> | 25.7<br><sub>22,16,26,19,30</sub> | 24.5 · – | 5.5<br><sub>4,2,8,9,5</sub> | 5.5 | 8.5<br><sub>8,8,8,8,7</sub> | 8.5 | 2.2<br><sub>1,2,3,2,4</sub> | 2.5 | 1.4 | 0.9 | 4.5 | 39.7 |
| Duncan Robinson (DET) | 98% | 30.8<br><sub>28,28,32,33,32</sub> | 15.1<br><sub>21,17,21,12,13</sub> | 13.5 · – | 2.9<br><sub>2,1,3,0,2</sub> | 2.5 | 2.7<br><sub>2,2,3,2,2</sub> | 1.5 | 2.9<br><sub>5,5,5,2,3</sub> | 2.5 | 1.0 | 0.3 | 1.3 | 20.7 |
| Paul Reed (DET) | 96% | 27.7<br><sub>17,26,23,26,38</sub> | 15.9<br><sub>6,19,8,22,16</sub> | 15.5 · – | 8.6<br><sub>6,11,8,9,4</sub> | 9.5 | 2.4<br><sub>2,3,2,3,0</sub> | 2.5 | 0.6<br><sub>0,2,0,1,2</sub> |  | 1.6 | 1.6 | 1.9 | 26.9 |
| Ausar Thompson (DET) | 98% | 27.6<br><sub>33,19,-,25,29</sub> | 9.9<br><sub>11,4,-,11,7</sub> | 10.5 · – | 6.7<br><sub>11,3,-,6,9</sub> | 6.5 | 4.1<br><sub>5,5,-,2,8</sub> | 3.5 | 0.1<br><sub>0,0,-,0,0</sub> |  | 2.1 | 1.4 | 2.0 | 20.6 |
| Daniss Jenkins (DET) | 98% | 26.3<br><sub>15,22,38,24,24</sub> | 11.8<br><sub>3,15,18,11,14</sub> | 10.5 · – | 3.3<br><sub>2,5,8,3,2</sub> | 2.5 | 4.5<br><sub>3,5,6,2,3</sub> | 4.5 | 1.3<br><sub>1,1,3,1,2</sub> | 1.5 | 1.0 | 0.3 | 1.8 | 19.6 |
| John Collins (DET) | 98% | 26.2<br><sub>25,29,34,27,18</sub> | 11.8<br><sub>6,23,16,2,4</sub> | 14.5 · – | 6.1<br><sub>5,7,11,9,2</sub> | 7.5 | 1.3<br><sub>1,1,0,1,0</sub> |  | 1.1<br><sub>0,5,2,0,0</sub> | 1.5 | 0.8 | 0.9 | 1.4 | 19.2 |
| Kevin Huerter (DET) | 93% | 21.3<br><sub>18,20,26,16,19</sub> | 8.5<br><sub>3,5,9,7,3</sub> |  | 3.0<br><sub>3,6,3,1,2</sub> |  | 2.5<br><sub>2,2,2,0,3</sub> |  | 1.2<br><sub>1,1,1,1,1</sub> |  | 1.0 | 0.3 | 1.0 | 14.0 |
| Javonte Green (DET) | 93% | 20.8<br><sub>18,13,22,17,21</sub> | 7.3<br><sub>19,5,2,3,7</sub> |  | 3.3<br><sub>4,3,3,1,2</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 1.1<br><sub>5,1,0,1,1</sub> |  | 1.4 | 0.5 | 0.7 | 11.5 |
| Ronald Holland II (DET) | 96% | 16.4<br><sub>3,22,23,12,12</sub> | 6.2<br><sub>0,8,2,4,0</sub> |  | 3.7<br><sub>1,5,9,3,2</sub> |  | 1.3<br><sub>1,4,4,2,1</sub> |  | 0.4<br><sub>0,0,0,0,0</sub> |  | 0.8 | 0.5 | 1.0 | 11.2 |
| Taurean Prince (DET) | 66% | 11.4<br><sub>-,-,-,7,6</sub> | 4.2<br><sub>-,-,-,3,1</sub> |  | 1.8<br><sub>-,-,-,0,2</sub> |  | 0.8<br><sub>-,-,-,0,0</sub> |  | 0.6<br><sub>-,-,-,1,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.8 |
| Isaac Jones (DET) | 21% | 7.7<br><sub>-,-,-,3,-</sub> | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.5<br><sub>-,-,-,1,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 1.3 |
| Tolu Smith (DET) | 76% | 7.6<br><sub>-,2,3,6,1</sub> | 3.0<br><sub>-,0,0,1,2</sub> |  | 2.4<br><sub>-,1,1,4,1</sub> |  | 0.5<br><sub>-,0,0,0,0</sub> |  | 0.0<br><sub>-,0,0,0,0</sub> |  | 0.2 | 0.3 | 0.5 | 5.9 |
| Chaz Lanier (DET) | 38% | 6.9<br><sub>-,-,-,2,-</sub> | 2.7<br><sub>-,-,-,2,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Ebuka Okorie (DET) | 52% | 6.8<br><sub>-,-,2,4,-</sub> | 2.0<br><sub>-,-,2,0,-</sub> |  | 0.3<br><sub>-,-,0,0,-</sub> |  | 0.7<br><sub>-,-,0,2,-</sub> |  | 0.1<br><sub>-,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.7 | 3.0 |

</details>


### NYK @ PHI
Out: Dominick Barlow (PHI), Ariel Hukporti (PHI), Jose Alvarado (NYK)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| OG Anunoby REB over 5.5 (6+) | NYK @ PHI | draftkings | 2.12 | 2.12 | 1.77 | 56.5% | 44.1% | 47.2% | +0.0% | +19.7% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 115.2–108.6 | NYK 68% | 1.48 / 3.08 | PHI +6.5 | 223.5 | PHI +1.5 covers 35%; o226.5 44% |
| Expected (weighted by chance each plays) | 115.3–109.7 | NYK 65% | 1.54 / 2.87 | PHI +5.5 | 224.5 | PHI +1.5 covers 38%; o226.5 46% |
| if Jaylen Brown plays | 115.1–110.3 | NYK 63% | 1.59 / 2.71 | PHI +4.5 | 225.5 | PHI +1.5 covers 40%; o226.5 47% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaylen Brown (PHI) | Questionable | 55% | 35.9 | 20.8 | 6.2 | 4.0 | 1.8 | 1.1 | 0.5 | 3.3 | 31.0 | full tables below |

<details><summary>NYK players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson | 98% | 36.1<br><sub>34,37,32,36,35</sub> | 26.3<br><sub>21,19,28,23,38</sub> | 27.5 · – | 3.4<br><sub>5,2,3,1,1</sub> | 2.5 | 6.2<br><sub>3,4,4,7,7</sub> | 5.5 | 2.4<br><sub>1,2,1,0,6</sub> | 2.5 | 0.9 | 0.2 | 2.8 | 35.9 |
| OG Anunoby | 98% | 34.8<br><sub>32,34,35,36,31</sub> | 18.4<br><sub>10,20,22,13,23</sub> | 16.5 · – | 6.2<br><sub>5,10,3,7,6</sub> | 5.5 | 2.0<br><sub>0,8,2,2,1</sub> | 1.5 | 2.3<br><sub>1,2,3,1,2</sub> | 2.5 | 1.4 | 0.9 | 1.7 | 26.6 |
| Josh Hart | 98% | 33.6<br><sub>30,36,35,27,36</sub> | 11.1<br><sub>14,10,13,6,2</sub> | 10.5 · – | 8.2<br><sub>7,12,8,4,8</sub> | 7.5 | 4.2<br><sub>3,5,2,4,3</sub> | 3.5 | 1.5<br><sub>2,2,3,2,0</sub> | 1.5 | 1.4 | 0.3 | 1.9 | 23.5 |
| Karl-Anthony Towns | 98% | 31.9<br><sub>24,37,33,33,28</sub> | 19.4<br><sub>19,22,22,27,19</sub> | 19.5 · – | 12.8<br><sub>12,10,14,20,13</sub> | 11.5 | 3.9<br><sub>1,3,4,3,5</sub> | 3.5 | 1.6<br><sub>3,2,0,1,3</sub> | 1.5 | 0.9 | 0.8 | 2.9 | 36.1 |
| Mikal Bridges | 98% | 29.4<br><sub>33,22,35,32,13</sub> | 10.4<br><sub>4,0,6,12,3</sub> | 9.5 · – | 3.0<br><sub>3,1,5,3,0</sub> | 2.5 | 2.5<br><sub>1,4,1,4,0</sub> | 2.5 | 1.2<br><sub>0,0,0,4,1</sub> | 1.5 | 0.9 | 0.5 | 1.0 | 15.9 |
| Landry Shamet | 98% | 26.6<br><sub>25,21,22,28,32</sub> | 9.3<br><sub>5,8,6,13,14</sub> | 8.5 · – | 2.2<br><sub>2,2,2,2,1</sub> |  | 1.6<br><sub>4,0,1,3,5</sub> |  | 1.7<br><sub>1,2,2,3,4</sub> | 1.5 | 0.6 | 0.2 | 0.9 | 13.0 |
| Miles McBride | 98% | 17.2<br><sub>14,30,13,17,14</sub> | 6.2<br><sub>3,20,1,5,3</sub> |  | 1.6<br><sub>1,2,1,1,5</sub> |  | 1.3<br><sub>1,1,1,1,0</sub> |  | 1.0<br><sub>1,6,0,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 9.1 |
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
| Tyrese Maxey | 98% | 38.4<br><sub>40,42,36,34,36</sub> | 24.5<br><sub>28,32,26,29,27</sub> | 23.5 · – | 3.8<br><sub>4,3,4,5,5</sub> | 3.5 | 5.5<br><sub>5,6,4,4,4</sub> | 4.5 | 2.5<br><sub>2,2,4,1,3</sub> | 2.5 | 1.5 | 0.7 | 2.6 | 33.8 |
| Joel Embiid | 98% | 35.8<br><sub>33,34,36,-,39</sub> | 23.8<br><sub>13,24,28,-,21</sub> | 22.5 · – | 8.6<br><sub>11,7,11,-,11</sub> | 8.5 | 4.8<br><sub>6,1,10,-,2</sub> | 4.5 | 1.4<br><sub>2,1,0,-,0</sub> | 1.5 | 0.7 | 1.3 | 3.3 | 37.2 |
| LeBron James | 98% | 35.2<br><sub>34,33,-,33,33</sub> | 18.4<br><sub>14,17,-,18,13</sub> | 16.5 · – | 6.4<br><sub>9,10,-,2,5</sub> | 6.5 | 6.7<br><sub>7,5,-,5,10</sub> | 6.5 | 1.4<br><sub>0,1,-,0,2</sub> | 1.5 | 1.2 | 0.7 | 3.0 | 31.5 |
| VJ Edgecombe | 76% | 34.6<br><sub>35,33,30,-,29</sub> | 13.7<br><sub>9,11,17,-,8</sub> | 11.5 · – | 6.0<br><sub>4,7,13,-,7</sub> | 5.5 | 3.3<br><sub>1,6,2,-,2</sub> | 2.5 | 1.8<br><sub>0,1,5,-,1</sub> | 1.5 | 1.2 | 0.5 | 1.7 | 23.0 |
| Anfernee Simons | 96% | 26.5<br><sub>25,17,20,27,27</sub> | 11.2<br><sub>13,2,4,5,20</sub> |  | 2.4<br><sub>2,3,1,3,3</sub> |  | 1.9<br><sub>0,0,2,3,1</sub> |  | 2.0<br><sub>3,0,1,1,6</sub> |  | 0.6 | 0.2 | 1.1 | 15.5 |
| Kentavious Caldwell-Pope | 98% | 26.1<br><sub>26,25,28,31,21</sub> | 7.9<br><sub>10,3,12,7,4</sub> |  | 2.6<br><sub>4,3,2,3,2</sub> |  | 1.8<br><sub>1,2,1,3,1</sub> |  | 1.1<br><sub>2,1,4,1,0</sub> |  | 0.9 | 0.3 | 0.9 | 12.3 |
| Dean Wade | 86% | 24.6<br><sub>-,-,28,37,17</sub> | 4.8<br><sub>-,-,7,7,0</sub> |  | 3.2<br><sub>-,-,2,5,1</sub> |  | 1.1<br><sub>-,-,0,1,1</sub> |  | 0.7<br><sub>-,-,2,1,0</sub> |  | 0.8 | 0.3 | 0.6 | 9.0 |
| Rayan Rupert | 30% | 13.1<br><sub>-,-,-,-,-</sub> | 4.4<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.9<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.1 | 0.7 | 7.6 |
| Adem Bona | 96% | 12.5<br><sub>10,14,10,25,4</sub> | 3.5<br><sub>0,2,0,6,1</sub> |  | 3.2<br><sub>3,2,1,13,1</sub> |  | 0.4<br><sub>1,0,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.8 | 0.7 | 7.0 |
| Labaron Philon Jr. | 52% | 10.2<br><sub>-,-,4,13,-</sub> | 3.5<br><sub>-,-,0,5,-</sub> |  | 1.3<br><sub>-,-,0,2,-</sub> |  | 0.7<br><sub>-,-,0,1,-</sub> |  | 0.3<br><sub>-,-,0,1,-</sub> |  | 0.2 | 0.1 | 0.6 | 5.4 |
| Justin Edwards | 38% | 8.9<br><sub>-,-,1,-,-</sub> | 3.3<br><sub>-,-,0,-,-</sub> |  | 1.1<br><sub>-,-,0,-,-</sub> |  | 0.6<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 4.9 |
| Caleb Love | 43% | 7.6<br><sub>-,-,1,-,-</sub> | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.5<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.2 |

</details>

<details><summary>if Jaylen Brown plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jalen Brunson (NYK) | 98% | 36.1<br><sub>34,37,32,36,35</sub> | 26.3<br><sub>21,19,28,23,38</sub> | 27.5 · – | 3.4<br><sub>5,2,3,1,1</sub> | 2.5 | 6.2<br><sub>3,4,4,7,7</sub> | 5.5 | 2.4<br><sub>1,2,1,0,6</sub> | 2.5 | 0.9 | 0.2 | 2.8 | 35.9 |
| OG Anunoby (NYK) | 98% | 34.7<br><sub>32,34,35,36,31</sub> | 18.2<br><sub>10,20,22,13,23</sub> | 16.5 · – | 6.2<br><sub>5,10,3,7,6</sub> | 5.5 | 2.0<br><sub>0,8,2,2,1</sub> | 1.5 | 2.3<br><sub>1,2,3,1,2</sub> | 2.5 | 1.4 | 0.8 | 1.7 | 26.4 |
| Josh Hart (NYK) | 98% | 33.7<br><sub>30,36,35,27,36</sub> | 11.1<br><sub>14,10,13,6,2</sub> | 10.5 · – | 8.2<br><sub>7,12,8,4,8</sub> | 7.5 | 4.3<br><sub>3,5,2,4,3</sub> | 3.5 | 1.5<br><sub>2,2,3,2,0</sub> | 1.5 | 1.4 | 0.3 | 1.9 | 23.6 |
| Karl-Anthony Towns (NYK) | 98% | 31.9<br><sub>24,37,33,33,28</sub> | 19.5<br><sub>19,22,22,27,19</sub> | 19.5 · – | 12.8<br><sub>12,10,14,20,13</sub> | 11.5 | 3.9<br><sub>1,3,4,3,5</sub> | 3.5 | 1.6<br><sub>3,2,0,1,3</sub> | 1.5 | 0.9 | 0.8 | 2.9 | 36.2 |
| Mikal Bridges (NYK) | 98% | 29.4<br><sub>33,22,35,32,13</sub> | 10.3<br><sub>4,0,6,12,3</sub> | 9.5 · – | 3.1<br><sub>3,1,5,3,0</sub> | 2.5 | 2.5<br><sub>1,4,1,4,0</sub> | 2.5 | 1.2<br><sub>0,0,0,4,1</sub> | 1.5 | 0.9 | 0.5 | 1.0 | 15.9 |
| Landry Shamet (NYK) | 98% | 26.6<br><sub>25,21,22,28,32</sub> | 9.2<br><sub>5,8,6,13,14</sub> | 8.5 · – | 2.2<br><sub>2,2,2,2,1</sub> |  | 1.6<br><sub>4,0,1,3,5</sub> |  | 1.7<br><sub>1,2,2,3,4</sub> | 1.5 | 0.6 | 0.2 | 0.8 | 13.0 |
| Miles McBride (NYK) | 98% | 17.2<br><sub>14,30,13,17,14</sub> | 6.2<br><sub>3,20,1,5,3</sub> |  | 1.6<br><sub>1,2,1,1,5</sub> |  | 1.3<br><sub>1,1,1,1,0</sub> |  | 1.0<br><sub>1,6,0,1,1</sub> |  | 0.5 | 0.2 | 0.5 | 9.1 |
| Tyler Kolek (NYK) | 64% | 14.8<br><sub>-,-,15,11,18</sub> | 5.2<br><sub>-,-,0,2,9</sub> |  | 1.9<br><sub>-,-,3,1,2</sub> |  | 3.9<br><sub>-,-,9,3,9</sub> |  | 0.6<br><sub>-,-,0,0,3</sub> |  | 0.5 | 0.2 | 0.9 | 10.9 |
| Andre Drummond (NYK) | 98% | 14.1<br><sub>24,7,7,14,15</sub> | 5.4<br><sub>12,2,4,10,4</sub> |  | 6.4<br><sub>14,2,3,8,11</sub> |  | 1.2<br><sub>4,0,2,1,1</sub> |  | 0.2<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.5 | 0.8 | 13.0 |
| Jordan Clarkson (NYK) | 72% | 12.5<br><sub>8,3,5,-,17</sub> | 5.9<br><sub>4,0,0,-,18</sub> |  | 1.8<br><sub>1,1,1,-,3</sub> |  | 1.0<br><sub>1,0,0,-,1</sub> |  | 0.4<br><sub>0,0,0,-,2</sub> |  | 0.4 | 0.1 | 0.8 | 8.7 |
| Tyler Nickel (NYK) | 16% | 8.5 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Mohamed Diawara (NYK) | 38% | 7.8<br><sub>-,-,-,1,-</sub> | 2.8<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,0,-</sub> |  | 0.7<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Dalton Knecht (NYK) | 38% | 7.6<br><sub>-,-,-,-,-</sub> | 3.4<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.5<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.3 | 5.3 |
| Jaden Akins (NYK) | 48% | 7.5<br><sub>-,-,-,2,-</sub> | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.3<br><sub>-,-,-,0,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.0<br><sub>-,-,-,0,-</sub> |  | 0.1 | 0.2 | 0.4 | 1.1 |
| James Wiseman (NYK) | 63% | 7.1<br><sub>-,2,7,1,-</sub> | 2.5<br><sub>-,0,0,0,-</sub> |  | 2.1<br><sub>-,0,2,1,-</sub> |  | 0.4<br><sub>-,0,0,0,-</sub> |  | 0.0<br><sub>-,0,0,0,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.0 |
| Pacome Dadiet (NYK) | 38% | 6.3<br><sub>-,-,-,1,-</sub> | 2.7<br><sub>-,-,-,0,-</sub> |  | 1.4<br><sub>-,-,-,1,-</sub> |  | 0.4<br><sub>-,-,-,0,-</sub> |  | 0.2<br><sub>-,-,-,0,-</sub> |  | 0.2 | 0.1 | 0.2 | 4.5 |
| Tyrese Maxey (PHI) | 98% | 36.9<br><sub>40,42,36,34,36</sub> | 21.6<br><sub>28,32,26,29,27</sub> | 23.5 · – | 3.8<br><sub>4,3,4,5,5</sub> | 3.5 | 5.0<br><sub>5,6,4,4,4</sub> | 4.5 | 2.2<br><sub>2,2,4,1,3</sub> | 2.5 | 1.5 | 0.6 | 2.3 | 30.4 |
| Jaylen Brown (PHI) | 100% | 35.9<br><sub>35,38,35,40,34</sub> | 20.8<br><sub>19,21,27,16,20</sub> | 18.5 · – | 6.2<br><sub>8,8,3,4,10</sub> | 6.5 | 4.0<br><sub>6,4,5,4,2</sub> | 3.5 | 1.8<br><sub>2,1,3,2,1</sub> | 1.5 | 1.1 | 0.5 | 3.3 | 31.0 |
| Joel Embiid (PHI) | 98% | 35.2<br><sub>33,34,36,-,39</sub> | 22.4<br><sub>13,24,28,-,21</sub> | 22.5 · – | 8.5<br><sub>11,7,11,-,11</sub> | 8.5 | 4.5<br><sub>6,1,10,-,2</sub> | 4.5 | 1.2<br><sub>2,1,0,-,0</sub> | 1.5 | 0.7 | 1.3 | 3.0 | 35.5 |
| LeBron James (PHI) | 98% | 34.0<br><sub>34,33,-,33,33</sub> | 16.6<br><sub>14,17,-,18,13</sub> | 16.5 · – | 6.3<br><sub>9,10,-,2,5</sub> | 6.5 | 6.6<br><sub>7,5,-,5,10</sub> | 6.5 | 1.2<br><sub>0,1,-,0,2</sub> | 1.5 | 1.2 | 0.7 | 2.7 | 29.5 |
| VJ Edgecombe (PHI) | 76% | 32.2<br><sub>35,33,30,-,29</sub> | 11.8<br><sub>9,11,17,-,8</sub> | 11.5 · – | 5.8<br><sub>4,7,13,-,7</sub> | 5.5 | 3.1<br><sub>1,6,2,-,2</sub> | 2.5 | 1.5<br><sub>0,1,5,-,1</sub> | 1.5 | 1.1 | 0.5 | 1.5 | 20.6 |
| Anfernee Simons (PHI) | 96% | 21.9<br><sub>25,17,20,27,27</sub> | 8.6<br><sub>13,2,4,5,20</sub> |  | 2.0<br><sub>2,3,1,3,3</sub> |  | 1.5<br><sub>0,0,2,3,1</sub> |  | 1.5<br><sub>3,0,1,1,6</sub> |  | 0.5 | 0.1 | 1.0 | 12.2 |
| Kentavious Caldwell-Pope (PHI) | 98% | 20.8<br><sub>26,25,28,31,21</sub> | 5.9<br><sub>10,3,12,7,4</sub> |  | 2.1<br><sub>4,3,2,3,2</sub> |  | 1.3<br><sub>1,2,1,3,1</sub> |  | 0.7<br><sub>2,1,4,1,0</sub> |  | 0.8 | 0.2 | 0.7 | 9.3 |
| Dean Wade (PHI) | 86% | 20.1<br><sub>-,-,28,37,17</sub> | 3.8<br><sub>-,-,7,7,0</sub> |  | 2.7<br><sub>-,-,2,5,1</sub> |  | 0.8<br><sub>-,-,0,1,1</sub> |  | 0.5<br><sub>-,-,2,1,0</sub> |  | 0.7 | 0.3 | 0.5 | 7.3 |
| Adem Bona (PHI) | 96% | 8.2<br><sub>10,14,10,25,4</sub> | 2.2<br><sub>0,2,0,6,1</sub> |  | 2.1<br><sub>3,2,1,13,1</sub> |  | 0.2<br><sub>1,0,1,1,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.2 | 0.5 | 0.4 | 4.6 |
| Rayan Rupert (PHI) | 30% | 7.5<br><sub>-,-,-,-,-</sub> | 2.5<br><sub>-,-,-,-,-</sub> |  | 1.4<br><sub>-,-,-,-,-</sub> |  | 0.6<br><sub>-,-,-,-,-</sub> |  | 0.1<br><sub>-,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.5 | 4.5 |
| Caleb Love (PHI) | 43% | 6.6<br><sub>-,-,1,-,-</sub> | 0.3<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.0<br><sub>-,-,0,-,-</sub> |  | 0.1 | 0.2 | 0.3 | 1.0 |
| Labaron Philon Jr. (PHI) | 52% | 6.6<br><sub>-,-,4,13,-</sub> | 2.3<br><sub>-,-,0,5,-</sub> |  | 0.9<br><sub>-,-,0,2,-</sub> |  | 0.4<br><sub>-,-,0,1,-</sub> |  | 0.1<br><sub>-,-,0,1,-</sub> |  | 0.1 | 0.1 | 0.4 | 3.5 |
| Justin Edwards (PHI) | 38% | 6.5<br><sub>-,-,1,-,-</sub> | 2.5<br><sub>-,-,0,-,-</sub> |  | 0.8<br><sub>-,-,0,-,-</sub> |  | 0.4<br><sub>-,-,0,-,-</sub> |  | 0.2<br><sub>-,-,0,-,-</sub> |  | 0.3 | 0.1 | 0.2 | 3.8 |

</details>


### ORL @ TOR
Out: Kawhi Leonard (TOR), Malachi Smith (TOR), Paolo Banchero (ORL), Jonathan Isaac (ORL), Noah Penda (ORL), Jalen Suggs (ORL)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Franz Wagner RA under 12.5 | ORL @ TOR | draftkings | 1.89 | 1.88 | 1.55 | 64.4% | 49.4% | 53.1% | +0.6% | +21.8% | 0.2% |
| Desmond Bane 3PM under 2.5 | ORL @ TOR | draftkings | 2.12 | 2.11 | 1.74 | 57.5% | 44.1% | 47.4% | +0.5% | +21.8% | 0.1% |

<details><summary>ORL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Desmond Bane | 98% | 34.6<br><sub>33,27,35,34</sub> | 19.7<br><sub>18,5,22,13</sub> | 19.5 · – | 4.4<br><sub>5,2,6,5</sub> | 4.5 | 3.8<br><sub>2,0,2,4</sub> | 3.5 | 2.4<br><sub>3,1,4,2</sub> | 2.5 | 1.3 | 0.4 | 2.8 | 27.9 |
| Franz Wagner | 98% | 33.7<br><sub>29,33,37,34</sub> | 22.5<br><sub>22,18,23,15</sub> | 22.5 · – | 6.0<br><sub>6,6,13,4</sub> | 6.5 | 5.3<br><sub>5,5,9,5</sub> | 6.5 | 1.4<br><sub>2,1,0,0</sub> | 1.5 | 1.2 | 0.4 | 3.2 | 33.8 |
| Wendell Carter Jr. | 98% | 31.8<br><sub>31,29,33,26</sub> | 11.3<br><sub>22,20,9,3</sub> | 11.5 · – | 7.6<br><sub>7,9,10,10</sub> | 7.5 | 2.3<br><sub>0,1,2,3</sub> | 2.5 | 0.9<br><sub>1,3,0,0</sub> | 0.5 | 0.8 | 0.8 | 1.7 | 21.1 |
| Tristan da Silva | 98% | 30.5<br><sub>28,29,27,31</sub> | 12.6<br><sub>14,5,19,20</sub> | 11.5 · – | 4.3<br><sub>2,3,2,3</sub> | 3.5 | 2.1<br><sub>3,1,2,1</sub> | 1.5 | 1.7<br><sub>4,1,5,4</sub> | 2.5 | 0.9 | 0.4 | 1.4 | 19.0 |
| Anthony Black | 97% | 29.9<br><sub>-,-,26,22</sub> | 14.4<br><sub>-,-,18,8</sub> | 13.5 · – | 3.6<br><sub>-,-,3,2</sub> | 3.5 | 3.5<br><sub>-,-,5,1</sub> | 3.5 | 1.5<br><sub>-,-,5,0</sub> | 1.5 | 1.5 | 0.7 | 2.3 | 21.5 |
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
| Scottie Barnes | 98% | 34.1<br><sub>26,37,28,31</sub> | 22.7<br><sub>23,28,0,28</sub> | 21.5 · – | 7.2<br><sub>6,14,3,6</sub> | 6.5 | 6.7<br><sub>5,5,3,4</sub> | 6.5 | 1.0<br><sub>1,1,0,0</sub> | 1.5 | 1.6 | 1.5 | 3.2 | 36.5 |
| RJ Barrett | 98% | 34.0<br><sub>26,34,32,32</sub> | 24.2<br><sub>20,23,20,25</sub> | 22.5 · – | 6.3<br><sub>4,9,2,9</sub> | 5.5 | 3.8<br><sub>3,4,2,6</sub> | 3.5 | 1.9<br><sub>0,1,0,3</sub> | 1.5 | 0.9 | 0.4 | 2.6 | 34.4 |
| Immanuel Quickley | 98% | 30.0<br><sub>28,29,28,29</sub> | 16.9<br><sub>23,12,19,16</sub> | 17.5 · – | 3.7<br><sub>4,1,3,3</sub> | 3.5 | 5.5<br><sub>7,6,2,7</sub> | 5.5 | 2.5<br><sub>4,0,3,4</sub> | 2.5 | 1.3 | 0.1 | 1.8 | 26.1 |
| Ja'Kobe Walter | 98% | 28.7<br><sub>23,24,31,28</sub> | 12.2<br><sub>10,7,22,14</sub> | 12.5 · – | 3.6<br><sub>3,4,4,5</sub> | 3.5 | 1.7<br><sub>4,2,2,2</sub> | 1.5 | 2.1<br><sub>1,2,5,3</sub> | 2.5 | 1.6 | 0.3 | 0.9 | 17.5 |
| Jamal Shead | 98% | 25.7<br><sub>16,24,21,23</sub> | 8.0<br><sub>2,5,4,13</sub> | 7.5 · – | 1.8<br><sub>2,2,1,4</sub> | 2.5 | 5.2<br><sub>5,5,0,7</sub> | 4.5 | 0.9<br><sub>0,0,0,1</sub> | 0.5 | 1.1 | 0.2 | 2.0 | 15.1 |
| Collin Murray-Boyles | 98% | 22.6<br><sub>20,18,19,15</sub> | 9.4<br><sub>6,8,3,10</sub> | 9.5 · – | 5.6<br><sub>8,3,7,2</sub> | 4.5 | 1.9<br><sub>3,0,2,1</sub> | 1.5 | 0.4<br><sub>0,0,0,2</sub> |  | 1.0 | 1.0 | 1.3 | 16.9 |
| Jakob Poeltl | 98% | 21.7<br><sub>22,27,19,10</sub> | 7.1<br><sub>3,6,0,2</sub> | 7.5 · – | 6.1<br><sub>6,9,1,2</sub> | 5.5 | 1.4<br><sub>0,2,0,0</sub> | 1.5 | 0.0<br><sub>0,0,0,0</sub> |  | 0.8 | 1.0 | 1.2 | 14.5 |
| Jamison Battle | 96% | 17.6<br><sub>11,12,13,20</sub> | 6.8<br><sub>8,5,4,7</sub> |  | 2.8<br><sub>5,0,1,0</sub> |  | 0.8<br><sub>0,0,2,1</sub> |  | 1.0<br><sub>2,1,1,1</sub> |  | 0.4 | 0.2 | 0.6 | 10.4 |
| Allen Graves | 93% | 16.8<br><sub>19,6,20,18</sub> | 5.4<br><sub>5,2,11,3</sub> |  | 3.6<br><sub>5,2,6,1</sub> |  | 0.9<br><sub>0,0,4,0</sub> |  | 0.4<br><sub>0,0,1,0</sub> |  | 0.6 | 0.9 | 0.7 | 9.9 |
| Trayce Jackson-Davis | 88% | 13.6<br><sub>10,1,6,20</sub> | 5.0<br><sub>9,0,3,6</sub> |  | 4.4<br><sub>1,0,1,11</sub> |  | 0.9<br><sub>0,0,1,2</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.5 | 0.8 | 0.7 | 10.3 |
| Kyle Anderson | 72% | 12.3<br><sub>5,-,11,5</sub> | 3.3<br><sub>0,-,0,0</sub> |  | 2.4<br><sub>1,-,2,0</sub> |  | 1.8<br><sub>2,-,0,1</sub> |  | 0.0<br><sub>0,-,0,0</sub> |  | 0.6 | 0.4 | 0.7 | 7.5 |
| Alijah Martin | 93% | 7.3<br><sub>5,1,7,5</sub> | 2.8<br><sub>3,0,2,5</sub> |  | 1.1<br><sub>0,0,2,1</sub> |  | 0.6<br><sub>0,0,1,1</sub> |  | 0.2<br><sub>0,0,0,1</sub> |  | 0.3 | 0.1 | 0.5 | 4.5 |
| Jaden Bradley | 93% | 7.0<br><sub>5,1,5,5</sub> | 2.3<br><sub>0,0,6,0</sub> |  | 1.2<br><sub>0,0,1,1</sub> |  | 0.6<br><sub>0,0,1,1</sub> |  | 0.1<br><sub>0,0,0,0</sub> |  | 0.3 | 0.2 | 0.5 | 4.0 |

</details>


### IND @ MIA
Out: Johnny Furphy (IND), Tyrese Haliburton (IND), T.J. McConnell (IND), Ben Sheppard (IND), Ivica Zubac (IND)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Giannis Antetokounmpo PTS under 31.5 | IND @ MIA | draftkings | 1.93 | 1.93 | 1.62 | 61.9% | 48.3% | 51.7% | +0.0% | +19.8% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.5–125.8 | IND 26% | 3.90 / 1.35 | MIA -9.5 | 242.5 | MIA -8.5 covers 52%; o237.5 60% |
| Expected (weighted by chance each plays) | 116.8–126.0 | IND 26% | 3.88 / 1.35 | MIA -9.5 | 242.5 | MIA -8.5 covers 52%; o237.5 61% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Simone Fontecchio (MIA) | Questionable | 55% | 7.9 | 3.9 | 1.5 | 0.6 | 0.5 | 0.3 | 0.1 | 0.3 | 6.0 | small |

<details><summary>IND players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Pascal Siakam | 98% | 34.6<br><sub>35,29,26,37,34</sub> | 26.9<br><sub>30,23,21,20,26</sub> | 23.5 · – | 7.7<br><sub>8,3,7,13,11</sub> | 7.5 | 4.8<br><sub>1,3,6,6,3</sub> | 4.5 | 1.9<br><sub>1,3,3,1,0</sub> | 1.5 | 1.1 | 0.4 | 2.9 | 39.4 |
| Andrew Nembhard | 70% | 34.4<br><sub>34,32,30,-,35</sub> | 18.8<br><sub>18,16,14,-,18</sub> | 16.5 · – | 3.4<br><sub>2,2,1,-,3</sub> | 3.5 | 9.8<br><sub>9,5,3,-,14</sub> | 9.5 | 2.0<br><sub>0,1,4,-,1</sub> | 1.5 | 1.1 | 0.2 | 2.7 | 31.9 |
| Kelly Oubre Jr. | 98% | 29.5<br><sub>28,20,20,23,30</sub> | 12.4<br><sub>4,3,14,9,15</sub> | 10.5 · – | 4.8<br><sub>2,2,2,3,3</sub> | 3.5 | 1.8<br><sub>3,2,2,1,1</sub> |  | 1.3<br><sub>0,1,1,1,1</sub> | 1.5 | 1.1 | 0.5 | 1.2 | 19.1 |
| Aaron Nesmith | 91% | 28.4<br><sub>-,20,19,21,27</sub> | 15.6<br><sub>-,9,13,13,18</sub> | 13.5 · – | 3.8<br><sub>-,4,1,0,2</sub> | 3.5 | 1.9<br><sub>-,1,2,1,1</sub> |  | 2.3<br><sub>-,1,2,3,3</sub> | 2.5 | 0.7 | 0.5 | 1.5 | 21.3 |
| Jarace Walker | 96% | 26.2<br><sub>19,17,19,29,22</sub> | 11.6<br><sub>3,2,6,10,7</sub> |  | 6.0<br><sub>6,1,7,8,8</sub> |  | 2.8<br><sub>2,1,1,2,1</sub> |  | 1.6<br><sub>1,0,0,2,1</sub> |  | 0.9 | 0.4 | 1.8 | 20.4 |
| Obi Toppin | 98% | 24.2<br><sub>25,25,20,23,22</sub> | 14.5<br><sub>20,13,16,14,13</sub> | 13.5 · – | 5.5<br><sub>3,5,6,6,6</sub> | 5.5 | 2.3<br><sub>1,1,2,2,0</sub> |  | 1.9<br><sub>4,0,4,2,1</sub> | 1.5 | 0.7 | 0.3 | 1.3 | 22.4 |
| Quenton Jackson | 97% | 21.8<br><sub>16,17,18,27,14</sub> | 9.3<br><sub>6,8,5,4,2</sub> |  | 2.8<br><sub>4,1,1,2,2</sub> |  | 4.1<br><sub>1,3,2,4,6</sub> |  | 0.8<br><sub>0,1,0,0,0</sub> |  | 0.9 | 0.2 | 1.3 | 16.2 |
| Jay Huff | 88% | 19.7<br><sub>-,5,21,23,16</sub> | 8.1<br><sub>-,0,14,6,3</sub> | 7.5 · – | 3.9<br><sub>-,2,2,6,6</sub> | 4.5 | 1.5<br><sub>-,0,3,1,2</sub> |  | 1.1<br><sub>-,0,2,0,1</sub> | 1.5 | 0.4 | 1.3 | 0.8 | 13.5 |
| Larry Nance Jr. | 88% | 18.7<br><sub>5,1,22,19,23</sub> | 5.5<br><sub>0,0,6,2,5</sub> |  | 4.0<br><sub>0,0,6,3,5</sub> |  | 1.1<br><sub>0,0,1,1,0</sub> |  | 0.6<br><sub>0,0,1,0,1</sub> |  | 0.9 | 0.3 | 0.7 | 10.6 |
| Jalen Slawson | 88% | 13.5<br><sub>-,16,8,3,12</sub> | 3.8<br><sub>-,4,1,2,2</sub> |  | 2.7<br><sub>-,5,2,1,1</sub> |  | 1.4<br><sub>-,2,0,0,1</sub> |  | 0.3<br><sub>-,0,0,0,0</sub> |  | 0.7 | 0.5 | 0.6 | 7.8 |
| Kobe Brown | 48% | 12.5<br><sub>-,1,-,-,-</sub> | 4.7<br><sub>-,0,-,-,-</sub> |  | 2.5<br><sub>-,0,-,-,-</sub> |  | 1.1<br><sub>-,0,-,-,-</sub> |  | 0.5<br><sub>-,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.7 | 8.3 |
| Braden Smith | 58% | 11.4<br><sub>-,-,-,-,5</sub> | 0.5<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 1.0<br><sub>-,-,-,-,1</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.3 | 0.5 | 1.8 |

</details>

<details><summary>MIA players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Bam Adebayo | 98% | 33.4<br><sub>31,23,39,30,33</sub> | 20.5<br><sub>15,4,20,8,24</sub> | 18.5 · – | 10.6<br><sub>7,6,8,8,9</sub> | 9.5 | 4.0<br><sub>4,3,4,3,3</sub> | 3.5 | 1.6<br><sub>1,0,2,0,0</sub> | 1.5 | 1.5 | 0.7 | 1.8 | 35.1 |
| Davion Mitchell | 98% | 33.4<br><sub>33,33,37,33,34</sub> | 12.9<br><sub>11,18,22,21,10</sub> | 12.5 · – | 2.9<br><sub>0,2,1,0,1</sub> | 2.5 | 7.0<br><sub>11,5,10,2,10</sub> | 6.5 | 1.5<br><sub>1,3,3,2,0</sub> | 1.5 | 1.3 | 0.2 | 1.9 | 22.7 |
| Giannis Antetokounmpo | 98% | 32.6<br><sub>30,33,25,39,31</sub> | 29.8<br><sub>35,36,14,29,24</sub> | 31.5 · – | 12.5<br><sub>6,12,6,14,18</sub> | 11.5 | 6.3<br><sub>1,5,3,11,3</sub> | 6.5 | 0.5<br><sub>0,1,0,2,0</sub> | 0.5 | 1.2 | 1.0 | 3.2 | 48.5 |
| Pelle Larsson | 98% | 31.1<br><sub>24,29,36,34,31</sub> | 12.8<br><sub>2,7,15,12,17</sub> | 12.5 · – | 4.1<br><sub>3,2,7,0,6</sub> |  | 3.9<br><sub>4,1,4,4,8</sub> |  | 1.0<br><sub>0,1,1,1,2</sub> |  | 1.1 | 0.3 | 1.6 | 20.8 |
| Andrew Wiggins | 98% | 28.3<br><sub>27,26,18,34,29</sub> | 13.3<br><sub>11,8,4,12,18</sub> | 13.5 · – | 4.6<br><sub>2,8,1,3,2</sub> | 4.5 | 2.2<br><sub>1,2,1,1,2</sub> | 1.5 | 1.7<br><sub>1,1,0,0,4</sub> | 1.5 | 1.0 | 1.0 | 1.2 | 20.1 |
| Bobby Portis | 98% | 23.6<br><sub>25,21,27,24,23</sub> | 11.5<br><sub>7,11,13,10,11</sub> | 11.5 · – | 7.0<br><sub>4,8,8,12,9</sub> | 7.5 | 1.6<br><sub>1,2,0,2,4</sub> |  | 1.6<br><sub>1,3,2,3,1</sub> | 1.5 | 0.7 | 0.4 | 0.9 | 20.1 |
| Tim Hardaway Jr. | 98% | 19.7<br><sub>18,21,21,16,22</sub> | 8.4<br><sub>3,8,5,5,14</sub> | 8.5 · – | 2.4<br><sub>4,4,0,2,3</sub> |  | 1.0<br><sub>1,1,0,1,1</sub> |  | 1.3<br><sub>1,2,0,1,2</sub> | 1.5 | 0.6 | 0.2 | 0.5 | 11.9 |
| Klay Thompson | 98% | 18.1<br><sub>16,24,27,15,17</sub> | 8.3<br><sub>10,6,14,6,3</sub> | 8.5 · – | 1.7<br><sub>1,2,3,1,1</sub> |  | 1.1<br><sub>0,2,0,1,2</sub> |  | 1.5<br><sub>3,2,4,2,1</sub> | 2.5 | 0.5 | 0.3 | 0.6 | 11.1 |
| Dru Smith | 64% | 13.1<br><sub>-,6,-,15,14</sub> | 4.3<br><sub>-,3,-,6,3</sub> |  | 1.8<br><sub>-,0,-,2,0</sub> |  | 1.9<br><sub>-,1,-,1,3</sub> |  | 0.3<br><sub>-,1,-,2,0</sub> |  | 1.1 | 0.3 | 0.6 | 8.0 |
| Nikola Jovic | 67% | 11.1<br><sub>24,13,6,-,7</sub> | 4.3<br><sub>4,5,0,-,5</sub> |  | 2.4<br><sub>4,4,2,-,3</sub> |  | 1.1<br><sub>2,1,0,-,0</sub> |  | 0.4<br><sub>0,0,0,-,1</sub> |  | 0.4 | 0.3 | 0.5 | 7.7 |
| Tre Donaldson | 16% | 8.5 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 5.9 |
| Keshad Johnson | 23% | 7.8 | 3.6 |  | 1.7 |  | 0.4 |  | 0.2 |  | 0.5 | 0.3 | 0.4 | 5.6 |
| Nick Richards | 48% | 6.7<br><sub>3,3,-,-,-</sub> | 2.7<br><sub>4,3,-,-,-</sub> |  | 2.5<br><sub>1,0,-,-,-</sub> |  | 0.3<br><sub>0,1,-,-,-</sub> |  | 0.1<br><sub>0,1,-,-,-</sub> |  | 0.1 | 0.3 | 0.5 | 5.5 |
| Myron Gardner | 48% | 6.6<br><sub>3,3,-,-,-</sub> | 2.5<br><sub>4,0,-,-,-</sub> |  | 2.0<br><sub>2,0,-,-,-</sub> |  | 0.7<br><sub>0,0,-,-,-</sub> |  | 0.1<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.2 | 0.3 | 5.2 |
| Ryan Conwell | 52% | 6.0<br><sub>3,3,4,-,-</sub> | 2.4<br><sub>0,2,3,-,-</sub> |  | 0.9<br><sub>0,0,1,-,-</sub> |  | 0.6<br><sub>2,0,0,-,-</sub> |  | 0.2<br><sub>0,0,1,-,-</sub> |  | 0.3 | 0.1 | 0.3 | 3.9 |
| Vladislav Goldin | 23% | 5.9 | 2.1 |  | 1.6 |  | 0.4 |  | 0.0 |  | 0.2 | 0.5 | 0.4 | 4.1 |

</details>


### HOU @ DAL
Out: Sergio de Larrea (DAL), Dereck Lively II (DAL), Steven Adams (HOU), Reed Sheppard (HOU)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Amen Thompson STL over 1.5 (2+) | HOU @ DAL | draftkings | 2.31 | 2.30 | 1.91 | 52.4% | 40.6% | 43.5% | +0.5% | +21.0% | 0.1% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 116.6–112.7 | HOU 61% | 1.65 / 2.54 | DAL +4.5 | 229.5 | DAL +6.5 covers 58%; o223.5 62% |
| Expected (weighted by chance each plays) | 117.6–112.8 | HOU 63% | 1.58 / 2.72 | DAL +4.5 | 230.5 | DAL +6.5 covers 55%; o223.5 64% |
| if Alperen Sengun plays | 118.3–112.4 | HOU 66% | 1.52 / 2.94 | DAL +5.5 | 230.5 | DAL +6.5 covers 52%; o223.5 65% |
| if Naji Marshall plays | 116.3–113.3 | HOU 58% | 1.73 / 2.37 | DAL +3.5 | 229.5 | DAL +6.5 covers 60%; o223.5 63% |
| if Marcus Smart plays | 117.4–112.5 | HOU 63% | 1.58 / 2.71 | DAL +4.5 | 229.5 | DAL +6.5 covers 55%; o223.5 63% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alperen Sengun (HOU) | Questionable | 55% | 34.7 | 21.4 | 10.2 | 6.6 | 0.8 | 1.4 | 1.1 | 3.3 | 38.1 | full tables below |
| Naji Marshall (DAL) | Questionable | 55% | 26.0 | 13.7 | 3.8 | 3.6 | 0.8 | 1.2 | 0.1 | 1.8 | 21.1 | full tables below |
| Santi Aldama (DAL) | Doubtful | 20% | 17.9 | 7.7 | 4.2 | 1.5 | 0.7 | 0.6 | 0.4 | 0.8 | 13.4 | small |
| Marcus Smart (HOU) | Questionable | 55% | 26.4 | 9.0 | 2.9 | 3.0 | 1.2 | 1.6 | 0.4 | 1.8 | 14.8 | full tables below |

<details><summary>HOU players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jabari Smith Jr. | 98% | 37.2<br><sub>36,34,33,39,30</sub> | 18.6<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.5<br><sub>5,5,5,12,2</sub> | 6.5 | 2.5<br><sub>1,1,3,5,2</sub> |  | 2.3<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.8 | 28.5 |
| Amen Thompson | 98% | 37.2<br><sub>33,36,39,28,33</sub> | 21.4<br><sub>16,20,17,15,23</sub> | 17.5 · – | 8.1<br><sub>10,10,11,5,4</sub> | 7.5 | 6.2<br><sub>4,4,6,2,3</sub> | 4.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.8 | 0.7 | 2.6 | 35.7 |
| Kevin Durant | 98% | 37.0<br><sub>37,37,37,30,31</sub> | 28.2<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.5<br><sub>6,7,4,9,5</sub> | 5.5 | 6.0<br><sub>3,6,2,3,4</sub> | 3.5 | 2.3<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.3 | 3.8 | 40.7 |
| Fred VanVleet | 98% | 34.4<br><sub>30,32,-,29,29</sub> | 16.2<br><sub>6,14,-,5,24</sub> | 11.5 · – | 3.9<br><sub>2,3,-,4,6</sub> | 3.5 | 6.1<br><sub>11,5,-,5,5</sub> | 5.5 | 2.6<br><sub>2,3,-,0,4</sub> | 2.5 | 1.7 | 0.5 | 1.7 | 26.3 |
| Tari Eason | 98% | 32.4<br><sub>3,27,31,33,31</sub> | 14.5<br><sub>2,12,19,13,5</sub> | 10.5 · – | 7.6<br><sub>1,6,3,8,9</sub> | 5.5 | 1.9<br><sub>0,0,0,2,1</sub> | 1.5 | 1.3<br><sub>0,0,0,1,1</sub> | 1.5 | 1.7 | 0.9 | 1.8 | 24.0 |
| Bogdan Bogdanovic | 88% | 21.5<br><sub>13,9,20,13,15</sub> | 8.8<br><sub>5,3,11,5,16</sub> |  | 2.7<br><sub>1,1,1,2,2</sub> |  | 2.3<br><sub>2,0,1,1,4</sub> |  | 1.3<br><sub>1,1,3,1,4</sub> |  | 0.8 | 0.2 | 0.9 | 13.7 |
| Oscar Tshiebwe | 67% | 20.8<br><sub>-,-,-,-,14</sub> | 9.2<br><sub>-,-,-,-,7</sub> |  | 9.0<br><sub>-,-,-,-,5</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.5 | 1.2 | 19.6 |
| Clint Capela | 83% | 20.0<br><sub>8,-,11,4,22</sub> | 6.1<br><sub>0,-,2,2,10</sub> |  | 7.7<br><sub>3,-,3,2,8</sub> |  | 1.3<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.8 | 1.4 | 0.9 | 15.1 |
| Jae'Sean Tate | 84% | 11.6<br><sub>2,-,1,1,4</sub> | 3.3<br><sub>0,-,0,0,0</sub> |  | 2.5<br><sub>0,-,0,1,0</sub> |  | 0.8<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.5 |
| Bruce Thornton | 80% | 10.1<br><sub>3,-,4,1,3</sub> | 2.3<br><sub>0,-,0,0,5</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.9<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 3.5 |
| Isaiah Crawford | 72% | 9.8<br><sub>3,-,1,1,5</sub> | 2.6<br><sub>3,-,0,0,3</sub> |  | 1.8<br><sub>0,-,0,0,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.3 | 5.1 |

</details>

<details><summary>DAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington | 98% | 33.8<br><sub>31,33,36,41,27</sub> | 15.3<br><sub>10,20,12,20,18</sub> | 12.5 · – | 7.1<br><sub>4,13,4,9,9</sub> | 6.5 | 1.8<br><sub>2,0,2,2,0</sub> |  | 1.6<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.8 | 24.2 |
| Cooper Flagg | 98% | 32.7<br><sub>33,17,-,40,33</sub> | 23.7<br><sub>32,14,-,29,26</sub> | 23.5 · – | 6.3<br><sub>5,5,-,6,5</sub> | 6.5 | 6.0<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.8 | 35.9 |
| Kyrie Irving | 98% | 31.5<br><sub>24,25,-,33,27</sub> | 21.0<br><sub>15,24,-,18,15</sub> | 18.5 · – | 3.9<br><sub>4,1,-,6,2</sub> | 3.5 | 4.0<br><sub>2,3,-,6,4</sub> | 3.5 | 2.4<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.2 | 28.9 |
| Zaccharie Risacher | 88% | 30.4<br><sub>27,32,32,30,29</sub> | 9.9<br><sub>4,11,11,6,13</sub> |  | 5.5<br><sub>6,6,4,8,6</sub> |  | 1.6<br><sub>2,1,2,1,1</sub> |  | 1.0<br><sub>0,1,1,1,2</sub> |  | 1.2 | 1.4 | 1.3 | 17.0 |
| Max Christie | 98% | 27.8<br><sub>29,38,26,26,22</sub> | 11.1<br><sub>5,16,5,11,11</sub> | 8.5 · – | 3.1<br><sub>3,4,5,5,5</sub> | 3.5 | 1.8<br><sub>2,4,1,3,2</sub> |  | 1.7<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.4 | 1.3 | 16.1 |
| Daniel Gafford | 98% | 24.7<br><sub>22,15,23,26,27</sub> | 9.4<br><sub>2,4,12,8,7</sub> | 7.5 · – | 7.6<br><sub>3,3,9,9,11</sub> | 6.5 | 1.6<br><sub>1,5,2,3,2</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.8 | 1.6 | 1.2 | 18.5 |
| Marcus Sasser | 91% | 19.5<br><sub>24,27,27,8,22</sub> | 7.4<br><sub>17,6,12,0,10</sub> |  | 1.7<br><sub>1,2,3,1,1</sub> |  | 2.6<br><sub>1,3,5,0,4</sub> |  | 1.1<br><sub>4,2,2,0,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.7 |
| Morez Johnson Jr. | 98% | 15.3<br><sub>14,17,12,15,18</sub> | 6.2<br><sub>6,8,6,6,10</sub> |  | 2.1<br><sub>3,6,1,2,6</sub> |  | 1.5<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.9 |
| Caleb Martin | 91% | 14.9<br><sub>-,-,-,-,14</sub> | 4.9<br><sub>-,-,-,-,10</sub> |  | 2.4<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,2</sub> |  | 0.7 | 0.3 | 0.7 | 8.5 |
| Walter Clayton Jr. | 67% | 13.7<br><sub>-,1,15,17,15</sub> | 4.5<br><sub>-,0,3,15,0</sub> |  | 2.1<br><sub>-,1,2,4,2</sub> |  | 2.9<br><sub>-,0,5,4,5</sub> |  | 0.5<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.5 |
| Moussa Cisse | 76% | 8.6<br><sub>3,1,7,-,3</sub> | 2.9<br><sub>3,3,4,-,0</sub> |  | 3.3<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.7 | 0.5 | 6.4 |
| Tarik Biberovic | 8% | 8.6 | 3.6 |  | 1.5 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Tobi Lawal | 63% | 6.7<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.1<br><sub>-,0,1,-,0</sub> |  | 0.8<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Jett Howard | 63% | 6.6<br><sub>-,-,4,-,3</sub> | 2.6<br><sub>-,-,5,-,0</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.2 | 3.8 |

</details>

<details><summary>if Naji Marshall plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington (DAL) | 98% | 31.1<br><sub>31,33,36,41,27</sub> | 13.4<br><sub>10,20,12,20,18</sub> | 12.5 · – | 6.5<br><sub>4,13,4,9,9</sub> | 6.5 | 1.6<br><sub>2,0,2,2,0</sub> |  | 1.5<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.7 | 21.5 |
| Cooper Flagg (DAL) | 98% | 30.9<br><sub>33,17,-,40,33</sub> | 21.7<br><sub>32,14,-,29,26</sub> | 23.5 · – | 6.1<br><sub>5,5,-,6,5</sub> | 6.5 | 5.3<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.5 | 33.1 |
| Kyrie Irving (DAL) | 98% | 30.7<br><sub>24,25,-,33,27</sub> | 20.1<br><sub>15,24,-,18,15</sub> | 18.5 · – | 3.8<br><sub>4,1,-,6,2</sub> | 3.5 | 3.9<br><sub>2,3,-,6,4</sub> | 3.5 | 2.2<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.1 | 27.7 |
| Zaccharie Risacher (DAL) | 88% | 27.5<br><sub>27,32,32,30,29</sub> | 9.0<br><sub>4,11,11,6,13</sub> |  | 5.1<br><sub>6,6,4,8,6</sub> |  | 1.5<br><sub>2,1,2,1,1</sub> |  | 0.9<br><sub>0,1,1,1,2</sub> |  | 1.1 | 1.3 | 1.2 | 15.7 |
| Naji Marshall (DAL) | 100% | 26.0<br><sub>29,33,21,-,-</sub> | 13.7<br><sub>16,15,10,-,-</sub> | 11.5 · – | 3.8<br><sub>2,4,4,-,-</sub> | 3.5 | 3.6<br><sub>6,6,5,-,-</sub> | 3.5 | 0.8<br><sub>2,0,1,-,-</sub> | 0.5 | 1.2 | 0.1 | 1.8 | 21.1 |
| Max Christie (DAL) | 98% | 25.8<br><sub>29,38,26,26,22</sub> | 9.8<br><sub>5,16,5,11,11</sub> | 8.5 · – | 2.9<br><sub>3,4,5,5,5</sub> | 3.5 | 1.7<br><sub>2,4,1,3,2</sub> |  | 1.5<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.3 | 1.2 | 14.3 |
| Daniel Gafford (DAL) | 98% | 22.0<br><sub>22,15,23,26,27</sub> | 8.5<br><sub>2,4,12,8,7</sub> | 7.5 · – | 6.7<br><sub>3,3,9,9,11</sub> | 6.5 | 1.3<br><sub>1,5,2,3,2</sub> |  | 0.0<br><sub>0,0,0,0,1</sub> |  | 0.8 | 1.4 | 1.1 | 16.5 |
| Marcus Sasser (DAL) | 91% | 17.4<br><sub>24,27,27,8,22</sub> | 6.3<br><sub>17,6,12,0,10</sub> |  | 1.4<br><sub>1,2,3,1,1</sub> |  | 2.3<br><sub>1,3,5,0,4</sub> |  | 0.9<br><sub>4,2,2,0,1</sub> |  | 0.6 | 0.1 | 1.0 | 10.0 |
| Walter Clayton Jr. (DAL) | 67% | 13.0<br><sub>-,1,15,17,15</sub> | 4.5<br><sub>-,0,3,15,0</sub> |  | 2.0<br><sub>-,1,2,4,2</sub> |  | 2.8<br><sub>-,0,5,4,5</sub> |  | 0.5<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.3 |
| Morez Johnson Jr. (DAL) | 98% | 12.8<br><sub>14,17,12,15,18</sub> | 5.2<br><sub>6,8,6,6,10</sub> |  | 1.8<br><sub>3,6,1,2,6</sub> |  | 1.3<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.3 | 0.1 | 0.8 | 8.2 |
| Caleb Martin (DAL) | 91% | 12.7<br><sub>-,-,-,-,14</sub> | 4.1<br><sub>-,-,-,-,10</sub> |  | 2.1<br><sub>-,-,-,-,2</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,2</sub> |  | 0.6 | 0.3 | 0.6 | 7.1 |
| Tarik Biberovic (DAL) | 8% | 8.6 | 3.7 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.2 | 0.2 | 0.4 | 6.0 |
| Moussa Cisse (DAL) | 76% | 7.4<br><sub>3,1,7,-,3</sub> | 2.5<br><sub>3,3,4,-,0</sub> |  | 2.8<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.6 | 0.4 | 5.6 |
| Tobi Lawal (DAL) | 63% | 6.2<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.0<br><sub>-,0,1,-,0</sub> |  | 0.9<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.0 |
| Jett Howard (DAL) | 63% | 5.9<br><sub>-,-,4,-,3</sub> | 2.5<br><sub>-,-,5,-,0</sub> |  | 0.7<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.1 | 0.1 | 0.2 | 3.5 |
| Jabari Smith Jr. (HOU) | 98% | 37.2<br><sub>36,34,33,39,30</sub> | 18.6<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.5<br><sub>5,5,5,12,2</sub> | 6.5 | 2.5<br><sub>1,1,3,5,2</sub> |  | 2.3<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.8 | 28.5 |
| Amen Thompson (HOU) | 98% | 37.2<br><sub>33,36,39,28,33</sub> | 21.3<br><sub>16,20,17,15,23</sub> | 17.5 · – | 8.1<br><sub>10,10,11,5,4</sub> | 7.5 | 6.2<br><sub>4,4,6,2,3</sub> | 4.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.9 | 0.7 | 2.6 | 35.6 |
| Kevin Durant (HOU) | 98% | 37.0<br><sub>37,37,37,30,31</sub> | 28.1<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.5<br><sub>6,7,4,9,5</sub> | 5.5 | 6.0<br><sub>3,6,2,3,4</sub> | 3.5 | 2.3<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.3 | 3.8 | 40.5 |
| Fred VanVleet (HOU) | 98% | 34.4<br><sub>30,32,-,29,29</sub> | 16.3<br><sub>6,14,-,5,24</sub> | 11.5 · – | 3.9<br><sub>2,3,-,4,6</sub> | 3.5 | 6.1<br><sub>11,5,-,5,5</sub> | 5.5 | 2.6<br><sub>2,3,-,0,4</sub> | 2.5 | 1.7 | 0.5 | 1.6 | 26.3 |
| Tari Eason (HOU) | 98% | 32.5<br><sub>3,27,31,33,31</sub> | 14.5<br><sub>2,12,19,13,5</sub> | 10.5 · – | 7.7<br><sub>1,6,3,8,9</sub> | 5.5 | 1.9<br><sub>0,0,0,2,1</sub> | 1.5 | 1.3<br><sub>0,0,0,1,1</sub> | 1.5 | 1.7 | 0.9 | 1.8 | 24.0 |
| Bogdan Bogdanovic (HOU) | 88% | 21.5<br><sub>13,9,20,13,15</sub> | 8.7<br><sub>5,3,11,5,16</sub> |  | 2.7<br><sub>1,1,1,2,2</sub> |  | 2.3<br><sub>2,0,1,1,4</sub> |  | 1.3<br><sub>1,1,3,1,4</sub> |  | 0.8 | 0.2 | 0.9 | 13.7 |
| Oscar Tshiebwe (HOU) | 67% | 20.9<br><sub>-,-,-,-,14</sub> | 9.3<br><sub>-,-,-,-,7</sub> |  | 9.0<br><sub>-,-,-,-,5</sub> |  | 1.4<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.9 | 0.5 | 1.1 | 19.7 |
| Clint Capela (HOU) | 83% | 20.0<br><sub>8,-,11,4,22</sub> | 6.1<br><sub>0,-,2,2,10</sub> |  | 7.6<br><sub>3,-,3,2,8</sub> |  | 1.3<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.8 | 1.4 | 0.9 | 15.1 |
| Jae'Sean Tate (HOU) | 84% | 11.7<br><sub>2,-,1,1,4</sub> | 3.4<br><sub>0,-,0,0,0</sub> |  | 2.5<br><sub>0,-,0,1,0</sub> |  | 0.8<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.4 | 0.2 | 0.5 | 6.6 |
| Bruce Thornton (HOU) | 80% | 10.2<br><sub>3,-,4,1,3</sub> | 2.3<br><sub>0,-,0,0,5</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.9<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>0,-,0,0,1</sub> |  | 0.4 | 0.1 | 0.5 | 3.6 |
| Isaiah Crawford (HOU) | 72% | 9.8<br><sub>3,-,1,1,5</sub> | 2.6<br><sub>3,-,0,0,3</sub> |  | 1.8<br><sub>0,-,0,0,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.2<br><sub>1,-,0,0,1</sub> |  | 0.3 | 0.3 | 0.3 | 5.1 |

</details>

<details><summary>if Alperen Sengun plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington (DAL) | 98% | 33.8<br><sub>31,33,36,41,27</sub> | 15.3<br><sub>10,20,12,20,18</sub> | 12.5 · – | 7.2<br><sub>4,13,4,9,9</sub> | 6.5 | 1.8<br><sub>2,0,2,2,0</sub> |  | 1.6<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.9 | 24.2 |
| Cooper Flagg (DAL) | 98% | 32.6<br><sub>33,17,-,40,33</sub> | 23.5<br><sub>32,14,-,29,26</sub> | 23.5 · – | 6.3<br><sub>5,5,-,6,5</sub> | 6.5 | 6.0<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.8 | 35.8 |
| Kyrie Irving (DAL) | 98% | 31.4<br><sub>24,25,-,33,27</sub> | 21.0<br><sub>15,24,-,18,15</sub> | 18.5 · – | 3.9<br><sub>4,1,-,6,2</sub> | 3.5 | 4.0<br><sub>2,3,-,6,4</sub> | 3.5 | 2.4<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.2 | 28.9 |
| Zaccharie Risacher (DAL) | 88% | 30.4<br><sub>27,32,32,30,29</sub> | 9.8<br><sub>4,11,11,6,13</sub> |  | 5.5<br><sub>6,6,4,8,6</sub> |  | 1.6<br><sub>2,1,2,1,1</sub> |  | 1.0<br><sub>0,1,1,1,2</sub> |  | 1.2 | 1.4 | 1.3 | 16.9 |
| Max Christie (DAL) | 98% | 27.8<br><sub>29,38,26,26,22</sub> | 11.2<br><sub>5,16,5,11,11</sub> | 8.5 · – | 3.0<br><sub>3,4,5,5,5</sub> | 3.5 | 1.8<br><sub>2,4,1,3,2</sub> |  | 1.7<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.4 | 1.3 | 16.1 |
| Daniel Gafford (DAL) | 98% | 24.8<br><sub>22,15,23,26,27</sub> | 9.4<br><sub>2,4,12,8,7</sub> | 7.5 · – | 7.5<br><sub>3,3,9,9,11</sub> | 6.5 | 1.6<br><sub>1,5,2,3,2</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.9 | 1.6 | 1.2 | 18.5 |
| Marcus Sasser (DAL) | 91% | 19.5<br><sub>24,27,27,8,22</sub> | 7.5<br><sub>17,6,12,0,10</sub> |  | 1.7<br><sub>1,2,3,1,1</sub> |  | 2.6<br><sub>1,3,5,0,4</sub> |  | 1.1<br><sub>4,2,2,0,1</sub> |  | 0.7 | 0.1 | 1.0 | 11.8 |
| Morez Johnson Jr. (DAL) | 98% | 15.3<br><sub>14,17,12,15,18</sub> | 6.2<br><sub>6,8,6,6,10</sub> |  | 2.1<br><sub>3,6,1,2,6</sub> |  | 1.5<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.8 |
| Caleb Martin (DAL) | 91% | 15.0<br><sub>-,-,-,-,14</sub> | 5.0<br><sub>-,-,-,-,10</sub> |  | 2.5<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,2</sub> |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Walter Clayton Jr. (DAL) | 67% | 13.7<br><sub>-,1,15,17,15</sub> | 4.5<br><sub>-,0,3,15,0</sub> |  | 2.1<br><sub>-,1,2,4,2</sub> |  | 2.9<br><sub>-,0,5,4,5</sub> |  | 0.5<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.5 |
| Tarik Biberovic (DAL) | 8% | 8.8 | 3.8 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.2 | 0.4 | 6.2 |
| Moussa Cisse (DAL) | 76% | 8.5<br><sub>3,1,7,-,3</sub> | 2.9<br><sub>3,3,4,-,0</sub> |  | 3.2<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.7 | 0.5 | 6.4 |
| Jett Howard (DAL) | 63% | 6.7<br><sub>-,-,4,-,3</sub> | 2.6<br><sub>-,-,5,-,0</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Tobi Lawal (DAL) | 63% | 6.7<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.1<br><sub>-,0,1,-,0</sub> |  | 0.8<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Amen Thompson (HOU) | 98% | 36.2<br><sub>33,36,39,28,33</sub> | 18.7<br><sub>16,20,17,15,23</sub> | 17.5 · – | 7.4<br><sub>10,10,11,5,4</sub> | 7.5 | 5.1<br><sub>4,4,6,2,3</sub> | 4.5 | 0.4<br><sub>1,1,0,0,0</sub> |  | 1.8 | 0.7 | 2.3 | 31.2 |
| Jabari Smith Jr. (HOU) | 98% | 35.8<br><sub>36,34,33,39,30</sub> | 15.9<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.2<br><sub>5,5,5,12,2</sub> | 6.5 | 2.2<br><sub>1,1,3,5,2</sub> |  | 2.2<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.4 | 25.3 |
| Kevin Durant (HOU) | 98% | 35.6<br><sub>37,37,37,30,31</sub> | 24.8<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.1<br><sub>6,7,4,9,5</sub> | 5.5 | 5.2<br><sub>3,6,2,3,4</sub> | 3.5 | 2.2<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.2 | 3.2 | 36.2 |
| Alperen Sengun (HOU) | 100% | 34.7<br><sub>30,36,33,37,-</sub> | 21.4<br><sub>23,29,17,29,-</sub> | 20.5 · – | 10.2<br><sub>10,7,10,9,-</sub> | 8.5 | 6.6<br><sub>5,7,7,9,-</sub> | 5.5 | 0.8<br><sub>2,2,1,1,-</sub> |  | 1.4 | 1.1 | 3.3 | 38.1 |
| Fred VanVleet (HOU) | 98% | 32.5<br><sub>30,32,-,29,29</sub> | 13.9<br><sub>6,14,-,5,24</sub> | 11.5 · – | 3.6<br><sub>2,3,-,4,6</sub> | 3.5 | 5.5<br><sub>11,5,-,5,5</sub> | 5.5 | 2.3<br><sub>2,3,-,0,4</sub> | 2.5 | 1.6 | 0.4 | 1.4 | 22.9 |
| Tari Eason (HOU) | 98% | 28.7<br><sub>3,27,31,33,31</sub> | 11.6<br><sub>2,12,19,13,5</sub> | 10.5 · – | 6.4<br><sub>1,6,3,8,9</sub> | 5.5 | 1.6<br><sub>0,0,0,2,1</sub> | 1.5 | 1.1<br><sub>0,0,0,1,1</sub> | 1.5 | 1.5 | 0.8 | 1.3 | 19.6 |
| Bogdan Bogdanovic (HOU) | 88% | 16.8<br><sub>13,9,20,13,15</sub> | 6.1<br><sub>5,3,11,5,16</sub> |  | 2.1<br><sub>1,1,1,2,2</sub> |  | 1.8<br><sub>2,0,1,1,4</sub> |  | 0.9<br><sub>1,1,3,1,4</sub> |  | 0.7 | 0.1 | 0.6 | 10.0 |
| Oscar Tshiebwe (HOU) | 67% | 15.8<br><sub>-,-,-,-,14</sub> | 6.8<br><sub>-,-,-,-,7</sub> |  | 6.7<br><sub>-,-,-,-,5</sub> |  | 1.0<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.4 | 0.9 | 14.5 |
| Clint Capela (HOU) | 83% | 14.8<br><sub>8,-,11,4,22</sub> | 4.4<br><sub>0,-,2,2,10</sub> |  | 5.5<br><sub>3,-,3,2,8</sub> |  | 0.9<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.6 | 1.0 | 0.7 | 10.8 |
| Jae'Sean Tate (HOU) | 84% | 7.3<br><sub>2,-,1,1,4</sub> | 2.2<br><sub>0,-,0,0,0</sub> |  | 1.6<br><sub>0,-,0,1,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.2 | 0.1 | 0.3 | 4.2 |
| Bruce Thornton (HOU) | 80% | 6.7<br><sub>3,-,4,1,3</sub> | 1.8<br><sub>0,-,0,0,5</sub> |  | 0.2<br><sub>0,-,0,0,0</sub> |  | 0.6<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.3 | 2.6 |
| Isaiah Crawford (HOU) | 72% | 6.6<br><sub>3,-,1,1,5</sub> | 2.2<br><sub>3,-,0,0,3</sub> |  | 1.2<br><sub>0,-,0,0,0</sub> |  | 0.4<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.2 | 0.2 | 3.8 |

</details>

<details><summary>if Marcus Smart plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P.J. Washington (DAL) | 98% | 33.9<br><sub>31,33,36,41,27</sub> | 15.3<br><sub>10,20,12,20,18</sub> | 12.5 · – | 7.1<br><sub>4,13,4,9,9</sub> | 6.5 | 1.8<br><sub>2,0,2,2,0</sub> |  | 1.6<br><sub>2,2,0,4,2</sub> | 1.5 | 1.0 | 1.0 | 1.9 | 24.1 |
| Cooper Flagg (DAL) | 98% | 32.7<br><sub>33,17,-,40,33</sub> | 23.6<br><sub>32,14,-,29,26</sub> | 23.5 · – | 6.3<br><sub>5,5,-,6,5</sub> | 6.5 | 6.0<br><sub>2,6,-,11,8</sub> | 5.5 | 1.2<br><sub>1,2,-,2,2</sub> | 1.5 | 1.4 | 1.0 | 2.8 | 35.9 |
| Kyrie Irving (DAL) | 98% | 31.5<br><sub>24,25,-,33,27</sub> | 20.9<br><sub>15,24,-,18,15</sub> | 18.5 · – | 3.9<br><sub>4,1,-,6,2</sub> | 3.5 | 4.0<br><sub>2,3,-,6,4</sub> | 3.5 | 2.4<br><sub>1,5,-,2,3</sub> | 2.5 | 1.2 | 0.5 | 2.2 | 28.8 |
| Zaccharie Risacher (DAL) | 88% | 30.4<br><sub>27,32,32,30,29</sub> | 9.8<br><sub>4,11,11,6,13</sub> |  | 5.5<br><sub>6,6,4,8,6</sub> |  | 1.6<br><sub>2,1,2,1,1</sub> |  | 1.0<br><sub>0,1,1,1,2</sub> |  | 1.2 | 1.4 | 1.3 | 17.0 |
| Max Christie (DAL) | 98% | 27.7<br><sub>29,38,26,26,22</sub> | 11.2<br><sub>5,16,5,11,11</sub> | 8.5 · – | 3.1<br><sub>3,4,5,5,5</sub> | 3.5 | 1.9<br><sub>2,4,1,3,2</sub> |  | 1.7<br><sub>1,2,1,3,3</sub> | 1.5 | 0.7 | 0.4 | 1.3 | 16.1 |
| Daniel Gafford (DAL) | 98% | 24.7<br><sub>22,15,23,26,27</sub> | 9.4<br><sub>2,4,12,8,7</sub> | 7.5 · – | 7.5<br><sub>3,3,9,9,11</sub> | 6.5 | 1.6<br><sub>1,5,2,3,2</sub> |  | 0.1<br><sub>0,0,0,0,1</sub> |  | 0.9 | 1.6 | 1.2 | 18.5 |
| Marcus Sasser (DAL) | 91% | 19.4<br><sub>24,27,27,8,22</sub> | 7.4<br><sub>17,6,12,0,10</sub> |  | 1.7<br><sub>1,2,3,1,1</sub> |  | 2.6<br><sub>1,3,5,0,4</sub> |  | 1.1<br><sub>4,2,2,0,1</sub> |  | 0.7 | 0.2 | 1.0 | 11.8 |
| Morez Johnson Jr. (DAL) | 98% | 15.3<br><sub>14,17,12,15,18</sub> | 6.2<br><sub>6,8,6,6,10</sub> |  | 2.1<br><sub>3,6,1,2,6</sub> |  | 1.5<br><sub>1,0,2,1,3</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.4 | 0.1 | 0.9 | 9.8 |
| Caleb Martin (DAL) | 91% | 15.1<br><sub>-,-,-,-,14</sub> | 5.0<br><sub>-,-,-,-,10</sub> |  | 2.4<br><sub>-,-,-,-,2</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,2</sub> |  | 0.7 | 0.3 | 0.7 | 8.6 |
| Walter Clayton Jr. (DAL) | 67% | 13.6<br><sub>-,1,15,17,15</sub> | 4.5<br><sub>-,0,3,15,0</sub> |  | 2.1<br><sub>-,1,2,4,2</sub> |  | 2.9<br><sub>-,0,5,4,5</sub> |  | 0.5<br><sub>-,0,1,2,0</sub> |  | 0.4 | 0.2 | 0.7 | 9.5 |
| Tarik Biberovic (DAL) | 8% | 8.6 | 3.6 |  | 1.6 |  | 0.8 |  | 0.2 |  | 0.3 | 0.1 | 0.5 | 6.0 |
| Moussa Cisse (DAL) | 76% | 8.5<br><sub>3,1,7,-,3</sub> | 2.9<br><sub>3,3,4,-,0</sub> |  | 3.2<br><sub>0,1,4,-,0</sub> |  | 0.2<br><sub>0,0,0,-,0</sub> |  | 0.0<br><sub>0,0,0,-,0</sub> |  | 0.3 | 0.7 | 0.5 | 6.4 |
| Tobi Lawal (DAL) | 63% | 6.8<br><sub>-,1,4,-,3</sub> | 2.1<br><sub>-,0,5,-,0</sub> |  | 1.1<br><sub>-,0,1,-,0</sub> |  | 0.8<br><sub>-,0,1,-,1</sub> |  | 0.1<br><sub>-,0,1,-,0</sub> |  | 0.3 | 0.1 | 0.3 | 4.0 |
| Jett Howard (DAL) | 63% | 6.6<br><sub>-,-,4,-,3</sub> | 2.6<br><sub>-,-,5,-,0</sub> |  | 0.8<br><sub>-,-,0,-,0</sub> |  | 0.4<br><sub>-,-,0,-,0</sub> |  | 0.2<br><sub>-,-,1,-,0</sub> |  | 0.2 | 0.1 | 0.2 | 3.8 |
| Amen Thompson (HOU) | 98% | 36.9<br><sub>33,36,39,28,33</sub> | 20.6<br><sub>16,20,17,15,23</sub> | 17.5 · – | 8.0<br><sub>10,10,11,5,4</sub> | 7.5 | 5.8<br><sub>4,4,6,2,3</sub> | 4.5 | 0.3<br><sub>1,1,0,0,0</sub> |  | 1.8 | 0.7 | 2.5 | 34.4 |
| Jabari Smith Jr. (HOU) | 98% | 36.4<br><sub>36,34,33,39,30</sub> | 17.6<br><sub>30,7,14,16,14</sub> | 15.5 · – | 7.3<br><sub>5,5,5,12,2</sub> | 6.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 2.2<br><sub>4,1,2,2,3</sub> | 2.5 | 0.9 | 1.0 | 1.6 | 27.2 |
| Kevin Durant (HOU) | 98% | 36.0<br><sub>37,37,37,30,31</sub> | 27.3<br><sub>30,20,22,22,18</sub> | 23.5 · – | 6.4<br><sub>6,7,4,9,5</sub> | 5.5 | 5.6<br><sub>3,6,2,3,4</sub> | 3.5 | 2.3<br><sub>2,2,3,1,2</sub> | 1.5 | 1.0 | 1.2 | 3.4 | 39.2 |
| Fred VanVleet (HOU) | 98% | 33.7<br><sub>30,32,-,29,29</sub> | 15.4<br><sub>6,14,-,5,24</sub> | 11.5 · – | 3.9<br><sub>2,3,-,4,6</sub> | 3.5 | 5.7<br><sub>11,5,-,5,5</sub> | 5.5 | 2.5<br><sub>2,3,-,0,4</sub> | 2.5 | 1.6 | 0.4 | 1.5 | 25.0 |
| Tari Eason (HOU) | 98% | 29.7<br><sub>3,27,31,33,31</sub> | 12.8<br><sub>2,12,19,13,5</sub> | 10.5 · – | 6.9<br><sub>1,6,3,8,9</sub> | 5.5 | 1.7<br><sub>0,0,0,2,1</sub> | 1.5 | 1.2<br><sub>0,0,0,1,1</sub> | 1.5 | 1.6 | 0.8 | 1.4 | 21.4 |
| Marcus Smart (HOU) | 100% | 26.4<br><sub>26,21,-,-,-</sub> | 9.0<br><sub>10,5,-,-,-</sub> |  | 2.9<br><sub>2,3,-,-,-</sub> |  | 3.0<br><sub>2,1,-,-,-</sub> |  | 1.2<br><sub>2,0,-,-,-</sub> |  | 1.6 | 0.4 | 1.8 | 14.8 |
| Oscar Tshiebwe (HOU) | 67% | 18.7<br><sub>-,-,-,-,14</sub> | 8.1<br><sub>-,-,-,-,7</sub> |  | 8.2<br><sub>-,-,-,-,5</sub> |  | 1.2<br><sub>-,-,-,-,2</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.8 | 0.5 | 1.0 | 17.5 |
| Bogdan Bogdanovic (HOU) | 88% | 17.7<br><sub>13,9,20,13,15</sub> | 6.8<br><sub>5,3,11,5,16</sub> |  | 2.2<br><sub>1,1,1,2,2</sub> |  | 1.9<br><sub>2,0,1,1,4</sub> |  | 1.0<br><sub>1,1,3,1,4</sub> |  | 0.7 | 0.2 | 0.7 | 10.9 |
| Clint Capela (HOU) | 83% | 17.3<br><sub>8,-,11,4,22</sub> | 5.5<br><sub>0,-,2,2,10</sub> |  | 6.6<br><sub>3,-,3,2,8</sub> |  | 1.1<br><sub>0,-,1,0,2</sub> |  | 0.0<br><sub>0,-,0,0,0</sub> |  | 0.7 | 1.2 | 0.8 | 13.2 |
| Jae'Sean Tate (HOU) | 84% | 8.6<br><sub>2,-,1,1,4</sub> | 2.5<br><sub>0,-,0,0,0</sub> |  | 1.9<br><sub>0,-,0,1,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,0</sub> |  | 0.3 | 0.2 | 0.3 | 4.9 |
| Isaiah Crawford (HOU) | 72% | 7.8<br><sub>3,-,1,1,5</sub> | 2.2<br><sub>3,-,0,0,3</sub> |  | 1.4<br><sub>0,-,0,0,0</sub> |  | 0.5<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>1,-,0,0,1</sub> |  | 0.2 | 0.3 | 0.3 | 4.2 |
| Bruce Thornton (HOU) | 80% | 7.5<br><sub>3,-,4,1,3</sub> | 1.9<br><sub>0,-,0,0,5</sub> |  | 0.3<br><sub>0,-,0,0,0</sub> |  | 0.7<br><sub>0,-,0,0,0</sub> |  | 0.1<br><sub>0,-,0,0,1</sub> |  | 0.3 | 0.1 | 0.4 | 2.9 |

</details>


### LAC @ MIN
Out: Donte DiVincenzo (MIN), Anthony Edwards (MIN), Bradley Beal (LAC), Brandon Ingram (LAC), Max Strus (LAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels 3PM under 1.5 | LAC @ MIN | draftkings | 2.07 | 2.06 | 1.70 | 58.7% | 45.1% | 48.5% | +0.5% | +21.5% | 0.1% |
| LaMelo Ball 3PM under 3.5 | LAC @ MIN | draftkings | 1.87 | 1.87 | 1.56 | 64.2% | 50.0% | 53.5% | +0.1% | +20.0% | 0.0% |
| LaMelo Ball PA under 28.5 | LAC @ MIN | draftkings | 1.83 | 1.83 | 1.52 | 65.6% | 51.2% | 54.8% | +0.1% | +19.9% | 0.0% |

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 112.2–113.6 | LAC 46% | 2.16 / 1.86 | MIN -1.5 | 225.5 | MIN -7.5 covers 34%; o223.5 55% |
| Expected (weighted by chance each plays) | 112.4–113.4 | LAC 47% | 2.11 / 1.90 | MIN -1.5 | 225.5 | MIN -7.5 covers 33%; o223.5 54% |
| if Rui Hachimura plays | 112.7–113.2 | LAC 49% | 2.06 / 1.94 | MIN +0.5 | 225.5 | MIN -7.5 covers 32%; o223.5 55% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Rui Hachimura (LAC) | Questionable | 55% | 30.5 | 13.8 | 4.1 | 1.1 | 1.6 | 0.9 | 0.4 | 1.4 | 19.1 | full tables below |

<details><summary>LAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland | 98% | 32.8<br><sub>32,37,36,26</sub> | 23.6<br><sub>30,26,16,14</sub> | 22.5 · – | 2.7<br><sub>1,0,4,1</sub> | 2.5 | 6.6<br><sub>4,6,11,5</sub> | 7.5 | 2.7<br><sub>3,4,2,1</sub> | 2.5 | 1.3 | 0.2 | 3.5 | 33.0 |
| Derrick Jones Jr. | 98% | 30.5<br><sub>26,35,30,28</sub> | 11.6<br><sub>8,16,11,15</sub> | 10.5 · – | 4.4<br><sub>6,4,6,5</sub> | 4.5 | 1.4<br><sub>5,1,1,0</sub> |  | 1.2<br><sub>1,3,3,3</sub> | 1.5 | 1.2 | 0.8 | 1.1 | 17.4 |
| Kris Dunn | 98% | 30.1<br><sub>27,34,33,27</sub> | 8.0<br><sub>7,7,15,5</sub> | 7.5 · – | 4.0<br><sub>5,5,4,3</sub> | 3.5 | 4.3<br><sub>7,5,6,3</sub> | 4.5 | 0.9<br><sub>2,1,1,1</sub> | 0.5 | 2.0 | 0.4 | 1.7 | 16.2 |
| Keaton Wagler | 93% | 27.2<br><sub>29,24,26,28</sub> | 14.5<br><sub>15,13,11,21</sub> | 12.5 · – | 3.4<br><sub>5,3,5,4</sub> | 3.5 | 3.3<br><sub>5,3,4,2</sub> | 2.5 | 1.5<br><sub>3,2,1,3</sub> | 1.5 | 1.0 | 0.3 | 2.5 | 21.2 |
| Brook Lopez | 98% | 24.9<br><sub>27,20,23,22</sub> | 11.4<br><sub>17,22,15,2</sub> |  | 4.5<br><sub>11,4,1,3</sub> |  | 1.6<br><sub>1,0,2,3</sub> |  | 1.3<br><sub>1,2,3,0</sub> |  | 0.7 | 1.3 | 1.1 | 17.5 |
| Kobe Sanders | 96% | 23.3<br><sub>19,19,20,27</sub> | 10.0<br><sub>2,5,12,9</sub> |  | 2.7<br><sub>0,3,4,4</sub> |  | 2.0<br><sub>3,5,2,0</sub> |  | 1.2<br><sub>0,1,2,1</sub> |  | 1.1 | 0.2 | 1.4 | 14.7 |
| Isaiah Jackson | 96% | 23.2<br><sub>15,28,24,19</sub> | 9.9<br><sub>13,6,10,4</sub> | 8.5 · – | 6.8<br><sub>5,6,6,5</sub> | 6.5 | 1.6<br><sub>0,3,4,1</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 1.1 | 1.2 | 1.6 | 18.3 |
| Gradey Dick | 91% | 17.8<br><sub>19,12,18,19</sub> | 8.0<br><sub>12,6,6,5</sub> |  | 2.9<br><sub>4,4,3,5</sub> |  | 0.9<br><sub>0,0,0,0</sub> |  | 0.8<br><sub>1,0,2,1</sub> |  | 0.7 | 0.1 | 1.0 | 11.8 |
| Baba Miller | 80% | 14.8<br><sub>9,-,2,17</sub> | 7.0<br><sub>4,-,0,4</sub> |  | 2.2<br><sub>3,-,1,7</sub> |  | 1.5<br><sub>1,-,0,1</sub> |  | 0.3<br><sub>0,-,0,0</sub> |  | 0.6 | 0.2 | 0.9 | 10.7 |
| Cam Christie | 58% | 12.4<br><sub>2,-,-,14</sub> | 4.2<br><sub>0,-,-,2</sub> |  | 1.9<br><sub>0,-,-,0</sub> |  | 0.7<br><sub>0,-,-,0</sub> |  | 0.2<br><sub>0,-,-,0</sub> |  | 0.5 | 0.1 | 0.7 | 6.8 |
| Jalen Pickett | 52% | 10.1<br><sub>2,-,-,8</sub> | 3.7<br><sub>3,-,-,4</sub> |  | 1.3<br><sub>0,-,-,1</sub> |  | 1.2<br><sub>0,-,-,1</sub> |  | 0.3<br><sub>1,-,-,0</sub> |  | 0.3 | 0.1 | 0.5 | 6.1 |
| Nick Martinelli | 58% | 9.5<br><sub>2,-,-,6</sub> | 3.9<br><sub>0,-,-,2</sub> |  | 2.5<br><sub>1,-,-,3</sub> |  | 0.8<br><sub>1,-,-,1</sub> |  | 0.1<br><sub>0,-,-,0</sub> |  | 0.3 | 0.2 | 0.7 | 7.2 |
| Blake Wesley | 30% | 9.2 | 3.8 |  | 1.0 |  | 1.2 |  | 0.2 |  | 0.5 | 0.1 | 0.8 | 6.1 |

</details>

<details><summary>MIN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jaden McDaniels | 98% | 34.6<br><sub>29,30,31,37,35</sub> | 17.0<br><sub>17,15,14,14,19</sub> | 16.5 · – | 5.7<br><sub>8,6,6,6,7</sub> | 5.5 | 2.9<br><sub>1,3,3,4,4</sub> | 2.5 | 1.4<br><sub>1,2,1,2,1</sub> | 1.5 | 1.2 | 0.9 | 1.8 | 25.7 |
| Jonathan Kuminga | 98% | 31.1<br><sub>30,27,26,36,32</sub> | 14.5<br><sub>12,11,13,10,20</sub> | 14.5 · – | 5.8<br><sub>1,8,4,10,3</sub> | 5.5 | 2.6<br><sub>3,5,1,1,5</sub> | 2.5 | 1.4<br><sub>2,2,3,0,3</sub> | 1.5 | 1.1 | 0.5 | 1.8 | 22.8 |
| Rudy Gobert | 98% | 31.0<br><sub>33,30,31,36,20</sub> | 9.7<br><sub>5,14,8,5,1</sub> | 10.5 · – | 10.9<br><sub>15,9,13,20,4</sub> | 11.5 | 1.7<br><sub>1,1,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.2 | 1.5 | 22.3 |
| Ayo Dosunmu | 98% | 30.2<br><sub>29,27,23,26,32</sub> | 15.9<br><sub>16,14,9,9,17</sub> | 15.5 · – | 4.0<br><sub>5,7,3,1,3</sub> | 4.5 | 4.4<br><sub>3,10,3,0,4</sub> | 4.5 | 1.6<br><sub>1,1,1,1,3</sub> | 1.5 | 1.1 | 0.3 | 1.9 | 24.3 |
| LaMelo Ball | 98% | 28.2<br><sub>29,23,17,31,28</sub> | 19.2<br><sub>21,12,15,11,8</sub> | 20.5 · – | 3.8<br><sub>2,5,1,0,4</sub> | 4.5 | 6.4<br><sub>6,5,8,6,8</sub> | 7.5 | 3.0<br><sub>5,2,4,1,2</sub> | 3.5 | 1.2 | 0.3 | 3.1 | 29.5 |
| Terrence Shannon Jr. | 96% | 25.8<br><sub>20,22,23,24,27</sub> | 14.6<br><sub>10,13,15,14,19</sub> | 14.5 · – | 3.1<br><sub>1,4,4,4,6</sub> | 3.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 1.6<br><sub>2,2,3,3,1</sub> | 1.5 | 0.7 | 0.1 | 1.6 | 20.0 |
| Trey Lyles | 97% | 17.8<br><sub>12,17,14,13,22</sub> | 5.2<br><sub>1,9,3,3,7</sub> |  | 3.9<br><sub>1,6,6,1,3</sub> |  | 1.1<br><sub>0,2,2,1,1</sub> |  | 0.7<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.2 | 0.6 | 10.2 |
| Joan Beringer | 91% | 17.1<br><sub>14,15,13,17,20</sub> | 7.9<br><sub>0,9,6,12,7</sub> |  | 6.1<br><sub>6,9,6,7,9</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.7 |
| Bones Hyland | 96% | 15.6<br><sub>4,8,15,5,16</sub> | 7.8<br><sub>3,3,3,0,13</sub> |  | 1.8<br><sub>1,1,3,1,1</sub> |  | 2.1<br><sub>0,0,2,2,3</sub> |  | 1.2<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.3 | 1.0 | 11.6 |
| Jaylen Clark | 71% | 9.5<br><sub>3,3,5,-,7</sub> | 3.1<br><sub>1,0,3,-,3</sub> |  | 1.3<br><sub>1,2,1,-,2</sub> |  | 0.6<br><sub>1,1,0,-,1</sub> |  | 0.3<br><sub>0,0,0,-,1</sub> |  | 0.5 | 0.1 | 0.3 | 5.0 |
| Zyon Pullin | 52% | 8.3<br><sub>-,-,5,-,-</sub> | 2.9<br><sub>-,-,2,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.1 |
| Rocco Zikarsky | 23% | 7.1 | 2.4 |  | 2.2 |  | 0.4 |  | 0.0 |  | 0.2 | 0.6 | 0.3 | 4.9 |
| Enrique Freeman | 16% | 6.5 | 1.9 |  | 1.4 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.7 |
| Cody Williams | 52% | 6.4<br><sub>3,3,5,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.4<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 1.0 |
| Isaiah Evans | 52% | 6.2<br><sub>2,2,4,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 1.1<br><sub>1,0,0,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.0 |

</details>

<details><summary>if Rui Hachimura plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Garland (LAC) | 98% | 31.4<br><sub>32,37,36,26</sub> | 22.4<br><sub>30,26,16,14</sub> | 22.5 · – | 2.5<br><sub>1,0,4,1</sub> | 2.5 | 6.3<br><sub>4,6,11,5</sub> | 7.5 | 2.6<br><sub>3,4,2,1</sub> | 2.5 | 1.2 | 0.2 | 3.5 | 31.2 |
| Rui Hachimura (LAC) | 100% | 30.5<br><sub>32,33,29,-</sub> | 13.8<br><sub>10,16,5,-</sub> | 15.5 · – | 4.1<br><sub>8,6,4,-</sub> | 4.5 | 1.1<br><sub>2,1,0,-</sub> | 1.5 | 1.6<br><sub>2,3,1,-</sub> | 1.5 | 0.9 | 0.4 | 1.4 | 19.1 |
| Derrick Jones Jr. (LAC) | 98% | 28.1<br><sub>26,35,30,28</sub> | 10.6<br><sub>8,16,11,15</sub> | 10.5 · – | 4.1<br><sub>6,4,6,5</sub> | 4.5 | 1.3<br><sub>5,1,1,0</sub> |  | 1.1<br><sub>1,3,3,3</sub> | 1.5 | 1.1 | 0.8 | 1.0 | 16.1 |
| Kris Dunn (LAC) | 98% | 27.9<br><sub>27,34,33,27</sub> | 7.2<br><sub>7,7,15,5</sub> | 7.5 · – | 3.7<br><sub>5,5,4,3</sub> | 3.5 | 3.9<br><sub>7,5,6,3</sub> | 4.5 | 0.8<br><sub>2,1,1,1</sub> | 0.5 | 1.9 | 0.3 | 1.5 | 14.8 |
| Keaton Wagler (LAC) | 93% | 25.4<br><sub>29,24,26,28</sub> | 13.3<br><sub>15,13,11,21</sub> | 12.5 · – | 3.2<br><sub>5,3,5,4</sub> | 3.5 | 3.1<br><sub>5,3,4,2</sub> | 2.5 | 1.4<br><sub>3,2,1,3</sub> | 1.5 | 1.0 | 0.3 | 2.2 | 19.6 |
| Brook Lopez (LAC) | 98% | 22.6<br><sub>27,20,23,22</sub> | 10.1<br><sub>17,22,15,2</sub> |  | 4.0<br><sub>11,4,1,3</sub> |  | 1.4<br><sub>1,0,2,3</sub> |  | 1.2<br><sub>1,2,3,0</sub> |  | 0.6 | 1.1 | 1.0 | 15.6 |
| Kobe Sanders (LAC) | 96% | 20.8<br><sub>19,19,20,27</sub> | 8.5<br><sub>2,5,12,9</sub> |  | 2.4<br><sub>0,3,4,4</sub> |  | 1.8<br><sub>3,5,2,0</sub> |  | 1.0<br><sub>0,1,2,1</sub> |  | 1.0 | 0.2 | 1.3 | 12.7 |
| Isaiah Jackson (LAC) | 96% | 19.7<br><sub>15,28,24,19</sub> | 8.3<br><sub>13,6,10,4</sub> | 8.5 · – | 5.8<br><sub>5,6,6,5</sub> | 6.5 | 1.4<br><sub>0,3,4,1</sub> |  | 0.0<br><sub>0,0,0,0</sub> |  | 0.9 | 1.1 | 1.5 | 15.5 |
| Gradey Dick (LAC) | 91% | 15.8<br><sub>19,12,18,19</sub> | 7.0<br><sub>12,6,6,5</sub> |  | 2.6<br><sub>4,4,3,5</sub> |  | 0.8<br><sub>0,0,0,0</sub> |  | 0.7<br><sub>1,0,2,1</sub> |  | 0.6 | 0.1 | 0.9 | 10.3 |
| Baba Miller (LAC) | 80% | 13.2<br><sub>9,-,2,17</sub> | 5.9<br><sub>4,-,0,4</sub> |  | 2.0<br><sub>3,-,1,7</sub> |  | 1.4<br><sub>1,-,0,1</sub> |  | 0.2<br><sub>0,-,0,0</sub> |  | 0.6 | 0.2 | 0.8 | 9.3 |
| Cam Christie (LAC) | 58% | 9.6<br><sub>2,-,-,14</sub> | 3.4<br><sub>0,-,-,2</sub> |  | 1.5<br><sub>0,-,-,0</sub> |  | 0.6<br><sub>0,-,-,0</sub> |  | 0.1<br><sub>0,-,-,0</sub> |  | 0.4 | 0.1 | 0.6 | 5.5 |
| Jalen Pickett (LAC) | 52% | 7.7<br><sub>2,-,-,8</sub> | 2.8<br><sub>3,-,-,4</sub> |  | 1.0<br><sub>0,-,-,1</sub> |  | 1.0<br><sub>0,-,-,1</sub> |  | 0.2<br><sub>1,-,-,0</sub> |  | 0.2 | 0.1 | 0.4 | 4.8 |
| Nick Martinelli (LAC) | 58% | 6.8<br><sub>2,-,-,6</sub> | 3.1<br><sub>0,-,-,2</sub> |  | 1.8<br><sub>1,-,-,3</sub> |  | 0.7<br><sub>1,-,-,1</sub> |  | 0.1<br><sub>0,-,-,0</sub> |  | 0.2 | 0.2 | 0.5 | 5.6 |
| Blake Wesley (LAC) | 30% | 6.4 | 2.7 |  | 0.7 |  | 0.9 |  | 0.1 |  | 0.4 | 0.1 | 0.5 | 4.2 |
| Jaden McDaniels (MIN) | 98% | 34.6<br><sub>29,30,31,37,35</sub> | 17.0<br><sub>17,15,14,14,19</sub> | 16.5 · – | 5.7<br><sub>8,6,6,6,7</sub> | 5.5 | 2.9<br><sub>1,3,3,4,4</sub> | 2.5 | 1.4<br><sub>1,2,1,2,1</sub> | 1.5 | 1.2 | 0.9 | 1.8 | 25.6 |
| Jonathan Kuminga (MIN) | 98% | 31.2<br><sub>30,27,26,36,32</sub> | 14.4<br><sub>12,11,13,10,20</sub> | 14.5 · – | 5.8<br><sub>1,8,4,10,3</sub> | 5.5 | 2.5<br><sub>3,5,1,1,5</sub> | 2.5 | 1.4<br><sub>2,2,3,0,3</sub> | 1.5 | 1.1 | 0.5 | 1.8 | 22.8 |
| Rudy Gobert (MIN) | 98% | 30.9<br><sub>33,30,31,36,20</sub> | 9.7<br><sub>5,14,8,5,1</sub> | 10.5 · – | 10.8<br><sub>15,9,13,20,4</sub> | 11.5 | 1.6<br><sub>1,1,0,2,1</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.2 | 1.5 | 22.2 |
| Ayo Dosunmu (MIN) | 98% | 30.2<br><sub>29,27,23,26,32</sub> | 15.8<br><sub>16,14,9,9,17</sub> | 15.5 · – | 4.0<br><sub>5,7,3,1,3</sub> | 4.5 | 4.4<br><sub>3,10,3,0,4</sub> | 4.5 | 1.6<br><sub>1,1,1,1,3</sub> | 1.5 | 1.1 | 0.3 | 1.9 | 24.3 |
| LaMelo Ball (MIN) | 98% | 28.1<br><sub>29,23,17,31,28</sub> | 19.2<br><sub>21,12,15,11,8</sub> | 20.5 · – | 3.8<br><sub>2,5,1,0,4</sub> | 4.5 | 6.4<br><sub>6,5,8,6,8</sub> | 7.5 | 3.0<br><sub>5,2,4,1,2</sub> | 3.5 | 1.2 | 0.3 | 3.1 | 29.4 |
| Terrence Shannon Jr. (MIN) | 96% | 25.8<br><sub>20,22,23,24,27</sub> | 14.6<br><sub>10,13,15,14,19</sub> | 14.5 · – | 3.1<br><sub>1,4,4,4,6</sub> | 3.5 | 2.3<br><sub>1,1,3,5,2</sub> |  | 1.6<br><sub>2,2,3,3,1</sub> | 1.5 | 0.7 | 0.1 | 1.6 | 19.9 |
| Trey Lyles (MIN) | 97% | 17.6<br><sub>12,17,14,13,22</sub> | 5.1<br><sub>1,9,3,3,7</sub> |  | 3.9<br><sub>1,6,6,1,3</sub> |  | 1.1<br><sub>0,2,2,1,1</sub> |  | 0.7<br><sub>0,2,1,1,1</sub> |  | 0.5 | 0.2 | 0.6 | 10.1 |
| Joan Beringer (MIN) | 91% | 17.0<br><sub>14,15,13,17,20</sub> | 7.9<br><sub>0,9,6,12,7</sub> |  | 6.1<br><sub>6,9,6,7,9</sub> |  | 0.7<br><sub>1,0,0,0,2</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.2 | 0.8 | 14.7 |
| Bones Hyland (MIN) | 96% | 15.6<br><sub>4,8,15,5,16</sub> | 7.8<br><sub>3,3,3,0,13</sub> |  | 1.8<br><sub>1,1,3,1,1</sub> |  | 2.1<br><sub>0,0,2,2,3</sub> |  | 1.2<br><sub>1,1,0,0,3</sub> |  | 0.6 | 0.3 | 1.0 | 11.6 |
| Jaylen Clark (MIN) | 71% | 9.6<br><sub>3,3,5,-,7</sub> | 3.1<br><sub>1,0,3,-,3</sub> |  | 1.3<br><sub>1,2,1,-,2</sub> |  | 0.6<br><sub>1,1,0,-,1</sub> |  | 0.3<br><sub>0,0,0,-,1</sub> |  | 0.5 | 0.1 | 0.3 | 5.1 |
| Zyon Pullin (MIN) | 52% | 8.3<br><sub>-,-,5,-,-</sub> | 2.9<br><sub>-,-,2,-,-</sub> |  | 1.0<br><sub>-,-,1,-,-</sub> |  | 1.2<br><sub>-,-,0,-,-</sub> |  | 0.1<br><sub>-,-,0,-,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.2 |
| Rocco Zikarsky (MIN) | 23% | 7.1 | 2.4 |  | 2.2 |  | 0.4 |  | 0.0 |  | 0.2 | 0.6 | 0.3 | 5.0 |
| Enrique Freeman (MIN) | 16% | 6.4 | 1.9 |  | 1.4 |  | 0.4 |  | 0.1 |  | 0.2 | 0.2 | 0.3 | 3.6 |
| Cody Williams (MIN) | 52% | 6.4<br><sub>3,3,5,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 0.2<br><sub>0,0,0,-,-</sub> |  | 0.5<br><sub>0,0,0,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 1.0 |
| Isaiah Evans (MIN) | 52% | 6.1<br><sub>2,2,4,-,-</sub> | 0.3<br><sub>0,0,0,-,-</sub> |  | 1.1<br><sub>1,0,0,-,-</sub> |  | 0.6<br><sub>0,1,1,-,-</sub> |  | 0.0<br><sub>0,0,0,-,-</sub> |  | 0.2 | 0.1 | 0.2 | 2.0 |

</details>


### LAL @ GSW
Out: Jimmy Butler III (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW)

| Scenario | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|
| Confirmed players only | 114.7–114.0 | LAL 52% | 1.91 / 2.09 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| Expected (weighted by chance each plays) | 114.7–114.1 | LAL 52% | 1.92 / 2.09 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 38% |
| if Gui Santos plays | 114.4–115.0 | LAL 49% | 2.05 / 1.95 | GSW +0.5 | 229.5 | GSW +3.5 covers 60%; o234.5 39% |
| if Ziaire Williams plays | 114.6–114.0 | LAL 52% | 1.91 / 2.10 | GSW +1.5 | 228.5 | GSW +3.5 covers 57%; o234.5 37% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Gui Santos (GSW) | Doubtful | 20% | 23.6 | 9.2 | 4.2 | 2.3 | 1.1 | 1.1 | 0.3 | 1.5 | 15.7 | full tables below |
| Ziaire Williams (LAL) | Questionable | 55% | 24.4 | 9.1 | 2.6 | 1.4 | 1.2 | 1.5 | 0.3 | 1.1 | 13.1 | full tables below |

<details><summary>LAL players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Luka Doncic | 98% | 36.6<br><sub>30,37,38,37,-</sub> | 34.4<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 7.5 | 8.1<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.6 |
| Austin Reaves | 98% | 35.6<br><sub>32,38,36,39,31</sub> | 21.3<br><sub>23,28,29,26,16</sub> | 23.5 · – | 4.2<br><sub>4,2,1,4,6</sub> | 3.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 31.1 |
| Walker Kessler | 98% | 29.8<br><sub>30,35,28,33,26</sub> | 11.3<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.7<br><sub>9,8,7,8,9</sub> | 9.5 | 1.6<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.5 |
| Quentin Grimes | 98% | 27.1<br><sub>27,31,20,19,38</sub> | 10.0<br><sub>10,13,3,2,23</sub> | 7.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 2.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.7 |
| Sandro Mamukelashvili | 98% | 24.8<br><sub>22,24,21,24,30</sub> | 9.8<br><sub>5,7,9,17,13</sub> | 8.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.2<br><sub>0,1,1,3,0</sub> | 0.5 | 1.0 | 0.5 | 1.0 | 16.9 |
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
| Brandin Podziemski | 80% | 31.7<br><sub>-,33,-,33,32</sub> | 15.0<br><sub>-,18,-,18,8</sub> | 15.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 5.5 | 4.1<br><sub>-,3,-,5,6</sub> | 3.5 | 1.9<br><sub>-,2,-,3,0</sub> | 2.5 | 1.2 | 0.2 | 1.9 | 23.9 |
| Stephen Curry | 98% | 31.1<br><sub>21,30,-,27,32</sub> | 24.2<br><sub>23,24,-,24,44</sub> | 25.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.7<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.3 | 0.3 | 3.0 | 32.4 |
| Draymond Green | 83% | 28.8<br><sub>21,31,-,27,32</sub> | 8.1<br><sub>2,5,-,3,3</sub> | 6.5 · – | 5.3<br><sub>4,5,-,4,9</sub> | 5.5 | 6.0<br><sub>8,6,-,7,6</sub> | 5.5 | 1.1<br><sub>0,1,-,1,0</sub> | 0.5 | 1.2 | 0.6 | 2.5 | 19.3 |
| De'Anthony Melton | 98% | 21.5<br><sub>21,20,27,19,20</sub> | 9.3<br><sub>0,10,25,3,8</sub> | 9.5 · – | 3.0<br><sub>2,1,5,4,6</sub> | 3.5 | 2.3<br><sub>2,0,5,3,0</sub> | 2.5 | 1.3<br><sub>0,2,4,1,2</sub> | 1.5 | 1.4 | 0.3 | 1.5 | 14.6 |
| Georges Niang | 93% | 20.1<br><sub>20,13,23,18,23</sub> | 7.9<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.6<br><sub>2,3,4,2,3</sub> | 2.5 | 1.1<br><sub>2,0,2,0,2</sub> |  | 1.3<br><sub>0,0,0,3,1</sub> | 1.5 | 0.6 | 0.1 | 1.0 | 11.7 |
| Al Horford | 98% | 19.4<br><sub>17,19,-,19,18</sub> | 6.0<br><sub>0,3,-,11,4</sub> | 5.5 · – | 4.2<br><sub>4,5,-,3,5</sub> | 3.5 | 1.6<br><sub>2,0,-,0,2</sub> |  | 0.9<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.7 | 0.7 | 11.7 |
| Will Richard | 98% | 16.8<br><sub>20,3,31,3,23</sub> | 4.7<br><sub>8,0,11,0,6</sub> |  | 1.9<br><sub>5,0,0,0,3</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>0,0,3,0,0</sub> |  | 1.1 | 0.1 | 0.6 | 7.5 |
| Brandon Williams | 98% | 16.6<br><sub>18,9,24,15,14</sub> | 9.5<br><sub>14,4,20,6,11</sub> |  | 2.2<br><sub>4,2,3,3,3</sub> |  | 2.9<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.2 | 1.5 | 14.6 |
| Gary Payton II | 98% | 14.2<br><sub>18,11,17,12,10</sub> | 6.4<br><sub>10,7,2,7,2</sub> |  | 2.7<br><sub>1,2,1,2,2</sub> |  | 1.1<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 10.1 |
| Graham Ike | 67% | 12.5<br><sub>12,12,26,3,-</sub> | 5.9<br><sub>8,10,12,3,-</sub> |  | 2.8<br><sub>2,2,10,0,-</sub> |  | 1.0<br><sub>1,1,2,1,-</sub> |  | 0.3<br><sub>1,2,0,1,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.8 |
| Charles Bassey | 91% | 9.4<br><sub>-,-,13,2,2</sub> | 3.9<br><sub>-,-,10,0,0</sub> |  | 3.4<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 7.8 |
| LJ Cryer | 63% | 8.3<br><sub>9,-,14,3,-</sub> | 3.6<br><sub>9,-,3,6,-</sub> |  | 0.8<br><sub>1,-,1,0,-</sub> |  | 0.7<br><sub>3,-,1,2,-</sub> |  | 0.5<br><sub>2,-,1,2,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.0 |
| Malevy Leons | 58% | 7.9<br><sub>9,-,4,3,-</sub> | 2.4<br><sub>0,-,2,0,-</sub> |  | 1.3<br><sub>1,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 4.3 |

</details>

<details><summary>if Ziaire Williams plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | 96% | 34.7<br><sub>29,37,36,31,35</sub> | 21.0<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.3<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.1 | 33.2 |
| Brandin Podziemski (GSW) | 80% | 31.7<br><sub>-,33,-,33,32</sub> | 15.0<br><sub>-,18,-,18,8</sub> | 15.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 5.5 | 4.0<br><sub>-,3,-,5,6</sub> | 3.5 | 1.9<br><sub>-,2,-,3,0</sub> | 2.5 | 1.2 | 0.2 | 1.9 | 23.8 |
| Stephen Curry (GSW) | 98% | 31.1<br><sub>21,30,-,27,32</sub> | 24.3<br><sub>23,24,-,24,44</sub> | 25.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.7<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 3.0 | 32.4 |
| Draymond Green (GSW) | 83% | 28.8<br><sub>21,31,-,27,32</sub> | 8.1<br><sub>2,5,-,3,3</sub> | 6.5 · – | 5.3<br><sub>4,5,-,4,9</sub> | 5.5 | 6.0<br><sub>8,6,-,7,6</sub> | 5.5 | 1.1<br><sub>0,1,-,1,0</sub> | 0.5 | 1.1 | 0.6 | 2.5 | 19.4 |
| De'Anthony Melton (GSW) | 98% | 21.5<br><sub>21,20,27,19,20</sub> | 9.3<br><sub>0,10,25,3,8</sub> | 9.5 · – | 3.0<br><sub>2,1,5,4,6</sub> | 3.5 | 2.3<br><sub>2,0,5,3,0</sub> | 2.5 | 1.3<br><sub>0,2,4,1,2</sub> | 1.5 | 1.4 | 0.3 | 1.5 | 14.6 |
| Georges Niang (GSW) | 93% | 20.1<br><sub>20,13,23,18,23</sub> | 8.0<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.6<br><sub>2,3,4,2,3</sub> | 2.5 | 1.1<br><sub>2,0,2,0,2</sub> |  | 1.3<br><sub>0,0,0,3,1</sub> | 1.5 | 0.6 | 0.1 | 1.0 | 11.6 |
| Al Horford (GSW) | 98% | 19.4<br><sub>17,19,-,19,18</sub> | 6.0<br><sub>0,3,-,11,4</sub> | 5.5 · – | 4.2<br><sub>4,5,-,3,5</sub> | 3.5 | 1.6<br><sub>2,0,-,0,2</sub> |  | 0.9<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.7 | 0.7 | 11.7 |
| Will Richard (GSW) | 98% | 16.8<br><sub>20,3,31,3,23</sub> | 4.7<br><sub>8,0,11,0,6</sub> |  | 1.9<br><sub>5,0,0,0,3</sub> |  | 0.9<br><sub>1,0,1,0,0</sub> |  | 0.5<br><sub>0,0,3,0,0</sub> |  | 1.1 | 0.1 | 0.6 | 7.5 |
| Brandon Williams (GSW) | 98% | 16.6<br><sub>18,9,24,15,14</sub> | 9.4<br><sub>14,4,20,6,11</sub> |  | 2.2<br><sub>4,2,3,3,3</sub> |  | 2.9<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.9 | 0.2 | 1.5 | 14.5 |
| Gary Payton II (GSW) | 98% | 14.2<br><sub>18,11,17,12,10</sub> | 6.5<br><sub>10,7,2,7,2</sub> |  | 2.7<br><sub>1,2,1,2,2</sub> |  | 1.1<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.7 | 10.2 |
| Graham Ike (GSW) | 67% | 12.5<br><sub>12,12,26,3,-</sub> | 5.9<br><sub>8,10,12,3,-</sub> |  | 2.8<br><sub>2,2,10,0,-</sub> |  | 1.0<br><sub>1,1,2,1,-</sub> |  | 0.3<br><sub>1,2,0,1,-</sub> |  | 0.5 | 0.2 | 0.8 | 9.8 |
| Charles Bassey (GSW) | 91% | 9.4<br><sub>-,-,13,2,2</sub> | 3.9<br><sub>-,-,10,0,0</sub> |  | 3.4<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.4 | 0.6 | 0.5 | 7.8 |
| LJ Cryer (GSW) | 63% | 8.3<br><sub>9,-,14,3,-</sub> | 3.6<br><sub>9,-,3,6,-</sub> |  | 0.8<br><sub>1,-,1,0,-</sub> |  | 0.7<br><sub>3,-,1,2,-</sub> |  | 0.5<br><sub>2,-,1,2,-</sub> |  | 0.2 | 0.1 | 0.5 | 5.0 |
| Malevy Leons (GSW) | 58% | 7.9<br><sub>9,-,4,3,-</sub> | 2.5<br><sub>0,-,2,0,-</sub> |  | 1.4<br><sub>1,-,0,1,-</sub> |  | 0.6<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.4 | 0.2 | 0.4 | 4.4 |
| Luka Doncic (LAL) | 98% | 35.4<br><sub>30,37,38,37,-</sub> | 32.5<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 7.5 | 7.8<br><sub>7,7,10,9,-</sub> | 7.5 | 4.1<br><sub>5,2,8,6,-</sub> | 4.5 | 1.8 | 0.5 | 4.6 | 47.5 |
| Austin Reaves (LAL) | 98% | 33.9<br><sub>32,38,36,39,31</sub> | 19.8<br><sub>23,28,29,26,16</sub> | 23.5 · – | 4.0<br><sub>4,2,1,4,6</sub> | 3.5 | 5.3<br><sub>6,9,4,7,1</sub> | 5.5 | 2.1<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.3 | 29.1 |
| Walker Kessler (LAL) | 98% | 27.4<br><sub>30,35,28,33,26</sub> | 10.7<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.2<br><sub>9,8,7,8,9</sub> | 9.5 | 1.4<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.8 | 1.8 | 1.5 | 21.4 |
| Ziaire Williams (LAL) | 100% | 24.4<br><sub>24,31,30,29,-</sub> | 9.1<br><sub>9,14,11,11,-</sub> | 8.5 · – | 2.6<br><sub>3,5,2,2,-</sub> | 2.5 | 1.4<br><sub>4,0,1,4,-</sub> |  | 1.2<br><sub>1,1,3,2,-</sub> | 1.5 | 1.5 | 0.3 | 1.1 | 13.1 |
| Quentin Grimes (LAL) | 98% | 24.2<br><sub>27,31,20,19,38</sub> | 9.1<br><sub>10,13,3,2,23</sub> | 7.5 · – | 2.9<br><sub>2,8,1,4,3</sub> | 2.5 | 2.3<br><sub>4,4,1,0,5</sub> | 2.5 | 1.0<br><sub>0,3,0,0,0</sub> | 1.5 | 0.9 | 0.3 | 1.2 | 14.4 |
| Sandro Mamukelashvili (LAL) | 98% | 22.1<br><sub>22,24,21,24,30</sub> | 9.1<br><sub>5,7,9,17,13</sub> | 8.5 · – | 4.9<br><sub>4,5,3,4,8</sub> | 4.5 | 1.7<br><sub>2,2,0,2,3</sub> |  | 1.1<br><sub>0,1,1,3,0</sub> | 0.5 | 0.9 | 0.5 | 1.0 | 15.7 |
| Matisse Thybulle (LAL) | 96% | 20.6<br><sub>23,24,26,22,28</sub> | 6.0<br><sub>3,13,11,5,15</sub> | 6.5 · – | 2.0<br><sub>3,1,1,2,1</sub> | 2.5 | 1.1<br><sub>1,2,1,1,0</sub> |  | 1.0<br><sub>1,3,3,1,4</sub> | 1.5 | 1.9 | 0.6 | 0.9 | 9.1 |
| Jake LaRavia (LAL) | 91% | 18.8<br><sub>18,-,15,19,35</sub> | 4.7<br><sub>10,-,0,5,2</sub> |  | 3.1<br><sub>2,-,4,1,10</sub> |  | 1.2<br><sub>2,-,1,1,0</sub> |  | 0.4<br><sub>2,-,0,1,0</sub> |  | 1.1 | 0.4 | 1.0 | 9.0 |
| Collin Sexton (LAL) | 98% | 18.0<br><sub>-,16,20,14,21</sub> | 11.2<br><sub>-,5,13,9,21</sub> |  | 1.9<br><sub>-,1,2,1,4</sub> |  | 2.1<br><sub>-,2,1,4,2</sub> |  | 1.2<br><sub>-,1,1,0,4</sub> |  | 1.0 | 0.1 | 1.6 | 15.2 |
| Jarred Vanderbilt (LAL) | 48% | 13.1<br><sub>-,-,-,-,21</sub> | 3.3<br><sub>-,-,-,-,0</sub> |  | 3.5<br><sub>-,-,-,-,7</sub> |  | 1.0<br><sub>-,-,-,-,2</sub> |  | 0.2<br><sub>-,-,-,-,0</sub> |  | 0.7 | 0.2 | 0.7 | 7.8 |
| Lawson Lovering (LAL) | 23% | 12.2 | 3.6 |  | 3.1 |  | 0.8 |  | 0.1 |  | 0.7 | 0.3 | 0.7 | 7.5 |
| AK Okereke (LAL) | 30% | 8.6<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.6<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.3 | 0.2 | 0.4 | 5.8 |
| Arthur Kaluma (LAL) | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.6<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.9 |
| Jaden Hardy (LAL) | 52% | 8.0<br><sub>7,-,-,-,9</sub> | 4.0<br><sub>3,-,-,-,2</sub> |  | 0.7<br><sub>2,-,-,-,0</sub> |  | 0.6<br><sub>0,-,-,-,2</sub> |  | 0.5<br><sub>1,-,-,-,0</sub> |  | 0.2 | 0.1 | 0.6 | 5.4 |
| Kevon Looney (LAL) | 64% | 6.8<br><sub>15,5,5,5,-</sub> | 1.8<br><sub>6,0,2,0,-</sub> |  | 2.3<br><sub>5,1,2,0,-</sub> |  | 0.5<br><sub>1,0,0,0,-</sub> |  | 0.0<br><sub>0,0,0,0,-</sub> |  | 0.2 | 0.2 | 0.3 | 4.6 |
| Bronny James (LAL) | 26% | 5.8<br><sub>7,-,-,-,-</sub> | 1.9<br><sub>2,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.3<br><sub>0,-,-,-,-</sub> |  | 0.0<br><sub>0,-,-,-,-</sub> |  | 0.1 | 0.1 | 0.5 | 2.4 |
| Chris Manon (LAL) | 52% | 5.4<br><sub>6,-,-,-,-</sub> | 1.6<br><sub>2,-,-,-,-</sub> |  | 1.1<br><sub>1,-,-,-,-</sub> |  | 0.4<br><sub>0,-,-,-,-</sub> |  | 0.1<br><sub>0,-,-,-,-</sub> |  | 0.4 | 0.1 | 0.3 | 3.1 |

</details>

<details><summary>if Gui Santos plays: both teams</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Yaxel Lendeborg (GSW) | 96% | 34.0<br><sub>29,37,36,31,35</sub> | 21.0<br><sub>12,18,26,31,26</sub> | 19.5 · – | 8.1<br><sub>3,13,9,12,9</sub> | 7.5 | 3.9<br><sub>2,6,5,6,1</sub> | 3.5 | 1.9<br><sub>1,1,6,1,2</sub> | 1.5 | 1.1 | 0.5 | 3.0 | 33.0 |
| Brandin Podziemski (GSW) | 80% | 30.3<br><sub>-,33,-,33,32</sub> | 14.3<br><sub>-,18,-,18,8</sub> | 15.5 · – | 4.8<br><sub>-,2,-,7,5</sub> | 5.5 | 3.9<br><sub>-,3,-,5,6</sub> | 3.5 | 1.8<br><sub>-,2,-,3,0</sub> | 2.5 | 1.2 | 0.2 | 1.8 | 23.0 |
| Stephen Curry (GSW) | 98% | 29.9<br><sub>21,30,-,27,32</sub> | 23.6<br><sub>23,24,-,24,44</sub> | 25.5 · – | 3.5<br><sub>2,2,-,3,8</sub> | 3.5 | 4.4<br><sub>1,4,-,3,6</sub> | 4.5 | 3.7<br><sub>2,3,-,3,6</sub> | 3.5 | 1.2 | 0.3 | 2.9 | 31.5 |
| Draymond Green (GSW) | 83% | 26.2<br><sub>21,31,-,27,32</sub> | 7.2<br><sub>2,5,-,3,3</sub> | 6.5 · – | 4.9<br><sub>4,5,-,4,9</sub> | 5.5 | 5.4<br><sub>8,6,-,7,6</sub> | 5.5 | 0.9<br><sub>0,1,-,1,0</sub> | 0.5 | 1.1 | 0.6 | 2.3 | 17.6 |
| Gui Santos (GSW) | 100% | 23.6<br><sub>25,20,23,28,-</sub> | 9.2<br><sub>12,5,7,13,-</sub> |  | 4.2<br><sub>5,4,4,3,-</sub> |  | 2.3<br><sub>0,2,3,1,-</sub> |  | 1.1<br><sub>1,1,1,1,-</sub> |  | 1.1 | 0.3 | 1.5 | 15.7 |
| De'Anthony Melton (GSW) | 98% | 19.6<br><sub>21,20,27,19,20</sub> | 8.5<br><sub>0,10,25,3,8</sub> | 9.5 · – | 2.9<br><sub>2,1,5,4,6</sub> | 3.5 | 2.0<br><sub>2,0,5,3,0</sub> | 2.5 | 1.1<br><sub>0,2,4,1,2</sub> | 1.5 | 1.2 | 0.3 | 1.4 | 13.3 |
| Al Horford (GSW) | 98% | 17.5<br><sub>17,19,-,19,18</sub> | 5.3<br><sub>0,3,-,11,4</sub> | 5.5 · – | 3.8<br><sub>4,5,-,3,5</sub> | 3.5 | 1.4<br><sub>2,0,-,0,2</sub> |  | 0.8<br><sub>0,1,-,3,0</sub> | 0.5 | 0.6 | 0.6 | 0.6 | 10.5 |
| Georges Niang (GSW) | 93% | 17.2<br><sub>20,13,23,18,23</sub> | 7.0<br><sub>7,4,4,9,7</sub> | 7.5 · – | 2.3<br><sub>2,3,4,2,3</sub> | 2.5 | 1.0<br><sub>2,0,2,0,2</sub> |  | 1.0<br><sub>0,0,0,3,1</sub> | 1.5 | 0.5 | 0.1 | 1.0 | 10.2 |
| Brandon Williams (GSW) | 98% | 15.3<br><sub>18,9,24,15,14</sub> | 8.9<br><sub>14,4,20,6,11</sub> |  | 2.1<br><sub>4,2,3,3,3</sub> |  | 2.6<br><sub>3,1,5,3,1</sub> |  | 0.6<br><sub>1,0,2,2,0</sub> |  | 0.8 | 0.2 | 1.4 | 13.6 |
| Will Richard (GSW) | 98% | 14.6<br><sub>20,3,31,3,23</sub> | 4.2<br><sub>8,0,11,0,6</sub> |  | 1.7<br><sub>5,0,0,0,3</sub> |  | 0.8<br><sub>1,0,1,0,0</sub> |  | 0.4<br><sub>0,0,3,0,0</sub> |  | 0.9 | 0.1 | 0.5 | 6.7 |
| Gary Payton II (GSW) | 98% | 12.7<br><sub>18,11,17,12,10</sub> | 6.2<br><sub>10,7,2,7,2</sub> |  | 2.5<br><sub>1,2,1,2,2</sub> |  | 1.0<br><sub>0,0,0,0,1</sub> |  | 0.4<br><sub>0,1,0,1,0</sub> |  | 0.9 | 0.2 | 0.6 | 9.6 |
| Graham Ike (GSW) | 67% | 8.7<br><sub>12,12,26,3,-</sub> | 4.1<br><sub>8,10,12,3,-</sub> |  | 2.0<br><sub>2,2,10,0,-</sub> |  | 0.8<br><sub>1,1,2,1,-</sub> |  | 0.2<br><sub>1,2,0,1,-</sub> |  | 0.4 | 0.2 | 0.6 | 6.9 |
| Charles Bassey (GSW) | 91% | 7.8<br><sub>-,-,13,2,2</sub> | 3.3<br><sub>-,-,10,0,0</sub> |  | 2.9<br><sub>-,-,7,1,0</sub> |  | 0.4<br><sub>-,-,0,0,0</sub> |  | 0.0<br><sub>-,-,0,0,0</sub> |  | 0.3 | 0.5 | 0.5 | 6.6 |
| LJ Cryer (GSW) | 63% | 6.8<br><sub>9,-,14,3,-</sub> | 3.0<br><sub>9,-,3,6,-</sub> |  | 0.7<br><sub>1,-,1,0,-</sub> |  | 0.5<br><sub>3,-,1,2,-</sub> |  | 0.4<br><sub>2,-,1,2,-</sub> |  | 0.1 | 0.0 | 0.4 | 4.2 |
| Malevy Leons (GSW) | 58% | 6.1<br><sub>9,-,4,3,-</sub> | 2.0<br><sub>0,-,2,0,-</sub> |  | 1.1<br><sub>1,-,0,1,-</sub> |  | 0.5<br><sub>0,-,0,0,-</sub> |  | 0.1<br><sub>0,-,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.5 |
| Luka Doncic (LAL) | 98% | 36.6<br><sub>30,37,38,37,-</sub> | 34.3<br><sub>28,23,52,41,-</sub> | 34.5 · – | 7.1<br><sub>8,6,8,5,-</sub> | 7.5 | 8.1<br><sub>7,7,10,9,-</sub> | 7.5 | 4.5<br><sub>5,2,8,6,-</sub> | 4.5 | 1.9 | 0.5 | 4.9 | 49.5 |
| Austin Reaves (LAL) | 98% | 35.5<br><sub>32,38,36,39,31</sub> | 21.1<br><sub>23,28,29,26,16</sub> | 23.5 · – | 4.2<br><sub>4,2,1,4,6</sub> | 3.5 | 5.6<br><sub>6,9,4,7,1</sub> | 5.5 | 2.3<br><sub>1,3,4,4,1</sub> | 2.5 | 1.1 | 0.5 | 3.5 | 30.8 |
| Walker Kessler (LAL) | 98% | 29.8<br><sub>30,35,28,33,26</sub> | 11.2<br><sub>26,22,2,13,11</sub> | 14.5 · – | 9.7<br><sub>9,8,7,8,9</sub> | 9.5 | 1.6<br><sub>1,3,0,0,1</sub> |  | 0.3<br><sub>0,0,0,0,0</sub> |  | 0.9 | 1.9 | 1.6 | 22.4 |
| Quentin Grimes (LAL) | 98% | 27.1<br><sub>27,31,20,19,38</sub> | 9.9<br><sub>10,13,3,2,23</sub> | 7.5 · – | 3.2<br><sub>2,8,1,4,3</sub> | 2.5 | 2.5<br><sub>4,4,1,0,5</sub> | 2.5 | 1.1<br><sub>0,3,0,0,0</sub> | 1.5 | 1.0 | 0.3 | 1.2 | 15.7 |
| Sandro Mamukelashvili (LAL) | 98% | 24.8<br><sub>22,24,21,24,30</sub> | 9.8<br><sub>5,7,9,17,13</sub> | 8.5 · – | 5.4<br><sub>4,5,3,4,8</sub> | 4.5 | 1.8<br><sub>2,2,0,2,3</sub> |  | 1.1<br><sub>0,1,1,3,0</sub> | 0.5 | 1.0 | 0.5 | 1.0 | 17.0 |
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
| Confirmed players only | 115.3–113.2 | DEN 56% | 1.78 / 2.29 | PHX +2.5 | 228.5 | PHX +4.5 covers 56%; o231.5 43% |
| Expected (weighted by chance each plays) | 115.8–113.9 | DEN 55% | 1.83 / 2.20 | PHX +1.5 | 229.5 | PHX +4.5 covers 58%; o231.5 45% |

**Questionable players: chance to play, and their projection if they do**

| Player | Status | Chance | Min | PTS | REB | AST | 3PM | STL | BLK | TOV | PRA | Effect on others |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Alpha Diallo (DEN) | Questionable | 55% | 14.3 | 3.7 | 1.8 | 1.1 | 0.3 | 0.7 | 0.3 | 0.9 | 6.6 | small |
| Oso Ighodaro (PHX) | Questionable | 55% | 17.0 | 5.4 | 4.4 | 2.1 | 0.0 | 0.6 | 0.6 | 0.8 | 11.8 | small |
| Cameron Johnson (DEN) | Questionable | 55% | 20.1 | 8.2 | 2.8 | 1.6 | 1.1 | 0.6 | 0.3 | 0.8 | 12.6 | small |

<details><summary>DEN players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Jamal Murray | 98% | 37.6<br><sub>37,43,36,38</sub> | 24.0<br><sub>6,42,19,23</sub> | 22.5 · – | 4.4<br><sub>10,3,6,1</sub> | 4.5 | 6.1<br><sub>3,6,8,6</sub> | 6.5 | 3.3<br><sub>0,8,3,5</sub> | 2.5 | 1.1 | 0.5 | 2.6 | 34.5 |
| Nikola Jokic | 98% | 37.0<br><sub>35,44,35,34</sub> | 25.7<br><sub>13,35,19,21</sub> | 25.5 · – | 12.8<br><sub>7,15,7,13</sub> | 12.5 | 10.1<br><sub>5,10,11,10</sub> | 9.5 | 1.6<br><sub>1,3,1,0</sub> | 1.5 | 1.6 | 1.0 | 4.0 | 48.6 |
| Christian Braun | 98% | 34.7<br><sub>33,40,34,36</sub> | 12.3<br><sub>7,15,9,15</sub> | 12.5 · – | 4.7<br><sub>6,8,4,0</sub> | 4.5 | 2.5<br><sub>1,2,2,4</sub> |  | 1.2<br><sub>1,0,1,3</sub> | 1.5 | 1.1 | 0.4 | 1.3 | 19.5 |
| Aaron Gordon | 98% | 31.3<br><sub>29,37,25,31</sub> | 14.2<br><sub>20,7,7,15</sub> | 14.5 · – | 6.1<br><sub>6,5,4,11</sub> | 5.5 | 2.7<br><sub>1,4,2,3</sub> | 2.5 | 1.5<br><sub>3,1,0,2</sub> | 1.5 | 0.8 | 0.3 | 1.5 | 23.1 |
| DeMar DeRozan | 98% | 28.2<br><sub>28,24,29,26</sub> | 15.0<br><sub>13,12,21,6</sub> | 14.5 · – | 2.7<br><sub>2,3,4,2</sub> | 2.5 | 3.5<br><sub>0,3,2,5</sub> | 2.5 | 0.6<br><sub>0,0,2,0</sub> | 0.5 | 0.9 | 0.3 | 1.8 | 21.2 |
| Trevon Brazile | 93% | 25.9<br><sub>18,28,17,32</sub> | 8.7<br><sub>4,17,6,11</sub> | 8.5 · – | 6.3<br><sub>12,9,1,8</sub> | 5.5 | 1.1<br><sub>0,0,0,0</sub> |  | 1.1<br><sub>0,3,1,1</sub> |  | 0.8 | 0.5 | 1.3 | 16.1 |
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
| Collin Gillespie | 98% | 24.9<br><sub>21,28,23</sub> | 9.5<br><sub>0,11,9</sub> | 9.5 · – | 3.5<br><sub>1,4,1</sub> | 3.5 | 3.8<br><sub>2,9,2</sub> | 3.5 | 1.7<br><sub>0,2,3</sub> | 2.5 | 1.1 | 0.2 | 1.2 | 16.8 |
| Khaman Maluach | 96% | 20.4<br><sub>17,28,26</sub> | 6.3<br><sub>2,9,12</sub> | 8.5 · – | 6.3<br><sub>6,9,7</sub> | 7.5 | 0.7<br><sub>1,3,1</sub> |  | 0.3<br><sub>0,1,0</sub> |  | 0.4 | 1.1 | 1.1 | 13.4 |
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
