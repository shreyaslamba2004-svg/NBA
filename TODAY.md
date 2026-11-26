# NBA model · Wed 25 Nov 2026 (US date)

Updated **Thu 26 Nov, 02:06 PM** Sydney time. Decimal odds. Stakes are quarter-Kelly as % of bankroll, capped at 2%. **EV and stake use the Blend** of model and no-vig market (the model alone hasn't beaten closing lines in backtests); the model-only view is shown alongside. Lines a point or two off DraftKings': [ladders](output/2026-11-25/ladders.md). Is the model getting better or worse? See [HEALTH.md](HEALTH.md). Past days, projected vs actual: [history](history/README.md).

## Sanity checks

All automatic checks passed (team minutes, player minutes vs recent games, team points vs market, player points vs DraftKings).

## Best bets (EV ≥ 5%, odds ≤ 4)

DraftKings prices refresh every 5 to 30 minutes (5 within 3 hours of tip). Australian books are priced about 40 minutes before each tip. **A DraftKings bet is an early flag:** Aussie lines usually sit close, so check Sportsbet's line and price. **Min odds** is the break-even price on the Blend: any price at or above it is +EV, and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) works out the stake at the price you actually find.

_No bets clear the edge threshold right now._

## Long shots (EV ≥ 5%, odds above 4)

Same rules as best bets, kept apart because the model's tails (big nights, rare outcomes) aren't proven yet. Expect long losing runs even if the edge is real.

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Draymond Green AST over 9.5 (10+) | SAC @ GSW | draftkings | 16.80 | 15.20 | 8.93 | 11.2% | 5.6% | 6.6% | +10.6% | +88.1% | 0.2% |
| Draymond Green AST over 7.5 (8+) | SAC @ GSW | draftkings | 6.02 | 5.73 | 3.82 | 26.2% | 15.5% | 17.4% | +5.1% | +57.5% | 0.2% |

## Not on Sportsbet: check other books (EV ≥ 5%, odds ≤ 4)

Bets that pass the best-bets rules but that Sportsbet doesn't list as far as we know (e.g. odd-number assist milestones like 7+, alt-line unders, turnovers). Ladbrokes, TAB and others sometimes do. Graded in HEALTH.md.

_Nothing clears the edge threshold right now._

## Projections

**Plays** = chance he gets on court tonight (how often the coach uses him, and injury status). **Min and stats are his averages in games he plays**, so a bench player can show 40% and 12 min. Confirmed-player tables assume every questionable player sits, so a maybe never dilutes anyone else's numbers. Starters and stars who are questionable get full "if he plays" tables for both teams. Once a status is confirmed the next run drops the alternatives.

Game lines below assume every questionable player sits; each game's section shows what changes if they play. In the player tables, the small numbers under Min, PTS, REB, AST and 3PM are the last 5 games, oldest to newest (- = didn't play). Under each DraftKings line, **o / u** is the Blend chance of over / under that line (what the bets and the [bet tracker](https://claude.ai/artifact/RBrHraqai6JDQ9iUtz2SKt) use); other lines are in the ladders.

| Game | Tip (Syd) | Score | Away win | Fair H2H a/h | Fair line | Fair total | vs market |
|---|--:|--:|--:|--:|--:|--:|--:|
| SAC @ GSW | Thu 26 Nov 14:00 | 105.5–118.0 | SAC 19% | 5.36 / 1.23 | GSW -12.5 | 223.5 | GSW -8.5 covers 61%; o216.5 65% |
| SAS @ POR | Thu 26 Nov 14:00 | 112.9–111.4 | SAS 55% | 1.82 / 2.22 | POR +2.5 | 224.5 | POR +3.5 covers 55%; o224.5 49% |

### SAC @ GSW
Out: Jimmy Butler III (GSW), Stephen Curry (GSW), Moses Moody (GSW), Kristaps Porzingis (GSW), Zach LaVine (SAC), Jonathan Mogbo (SAC), Maxime Raynaud (SAC), Ben Simmons (SAC)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Charles Bassey PTS under 10.5 | SAC @ GSW | tab | 1.95 | 1.87 | 1.63 | 61.5% | 51.7% | 53.5% | +4.5% | +20.1% | 1.2% |

<details><summary>SAC players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Darius Acuff Jr. | 98% | 37.3<br><sub>33,35,36,40,33</sub> | 24.4<br><sub>26,36,18,21,12</sub> | 24.5 · 24.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>0,4,1,6,1</sub> | 3.5<br><sub>o 41% · u 59%</sub> | 7.9<br><sub>6,6,12,8,4</sub> | 7.5<br><sub>o 45% · u 55%</sub> | 2.8<br><sub>3,6,2,2,0</sub> | 2.5<br><sub>o 55% · u 45%</sub> | 1.1 | 0.3 | 4.0 | 35.7 |
| De'Andre Hunter | 88% | 36.4<br><sub>-,35,37,41,38</sub> | 17.0<br><sub>-,7,30,20,15</sub> | 16.5 · 15.5<br><sub>o 51% · u 49%</sub> | 5.0<br><sub>-,1,6,6,7</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.6<br><sub>-,4,2,2,8</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 2.2<br><sub>-,1,5,2,1</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.2 | 2.0 | 24.6 |
| Keegan Murray | 98% | 35.3<br><sub>21,31,40,40,39</sub> | 14.1<br><sub>6,12,13,15,14</sub> | 13.5 · 13.5<br><sub>o 49% · u 51%</sub> | 5.7<br><sub>1,7,7,12,2</sub> | 4.5<br><sub>o 58% · u 42%</sub> | 1.9<br><sub>0,3,4,0,1</sub> | 1.5<br><sub>o 52% · u 48%</sub> | 1.7<br><sub>2,0,2,0,2</sub> | 1.5<br><sub>o 53% · u 47%</sub> | 1.0 | 1.0 | 1.4 | 21.6 |
| Domantas Sabonis | 99% | 33.1<br><sub>29,24,38,32,30</sub> | 15.9<br><sub>11,8,19,15,20</sub> | 14.5 · 14.5<br><sub>o 51% · u 49%</sub> | 12.5<br><sub>13,13,16,17,12</sub> | 13.5<br><sub>o 45% · u 55%</sub> | 5.7<br><sub>3,8,1,4,8</sub> | 5.5<br><sub>o 43% · u 57%</sub> | 0.3<br><sub>0,0,1,0,0</sub> |  | 0.8 | 0.3 | 3.0 | 34.1 |
| Precious Achiuwa | 98% | 20.0<br><sub>-,8,-,22,10</sub> | 8.4<br><sub>-,0,-,5,9</sub> | 6.5 · –<br><sub>o 55% · u 45%</sub> | 5.1<br><sub>-,0,-,7,3</sub> |  | 1.1<br><sub>-,0,-,1,0</sub> |  | 0.3<br><sub>-,0,-,0,0</sub> |  | 0.8 | 0.7 | 1.1 | 14.7 |
| Malik Monk | 98% | 19.0<br><sub>29,20,12,10,16</sub> | 10.1<br><sub>14,8,2,3,15</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 1.8<br><sub>1,1,0,0,3</sub> |  | 3.7<br><sub>10,2,3,1,4</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 1.4<br><sub>1,2,0,0,4</sub> | 1.5<br><sub>o 49% · u 51%</sub> | 0.6 | 0.3 | 1.6 | 15.6 |
| Leaky Black | 91% | 17.0<br><sub>29,17,19,4,13</sub> | 3.9<br><sub>12,3,0,2,3</sub> |  | 2.7<br><sub>9,0,3,0,3</sub> |  | 1.2<br><sub>2,2,1,0,3</sub> |  | 0.5<br><sub>4,1,0,0,1</sub> |  | 0.9 | 0.4 | 0.5 | 7.9 |
| Emanuel Sharp | 98% | 16.4<br><sub>21,14,10,16,13</sub> | 5.4<br><sub>9,6,3,3,0</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 1.2<br><sub>0,2,0,0,1</sub> |  | 0.9<br><sub>2,1,1,0,2</sub> |  | 0.8<br><sub>1,1,1,1,0</sub> | 1.5<br><sub>o 34% · u 66%</sub> | 0.7 | 0.2 | 0.6 | 7.5 |
| Dylan Cardwell | 98% | 14.8<br><sub>19,12,10,6,11</sub> | 4.2<br><sub>10,6,0,0,0</sub> |  | 5.3<br><sub>6,4,4,1,7</sub> |  | 1.1<br><sub>2,0,0,0,0</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 0.9 | 0.8 | 10.7 |
| Daeqwon Plowden | 64% | 11.7<br><sub>24,4,-,-,1</sub> | 4.5<br><sub>13,3,-,-,1</sub> |  | 1.3<br><sub>2,0,-,-,0</sub> |  | 0.6<br><sub>1,0,-,-,0</sub> |  | 0.6<br><sub>3,1,-,-,0</sub> |  | 0.4 | 0.1 | 0.5 | 6.4 |
| Alex Karaban | 52% | 11.0<br><sub>29,4,-,-,1</sub> | 2.0<br><sub>0,0,-,-,0</sub> |  | 1.8<br><sub>5,1,-,-,0</sub> |  | 0.5<br><sub>1,0,-,-,0</sub> |  | 0.2<br><sub>0,0,-,-,0</sub> |  | 0.3 | 0.1 | 0.6 | 4.2 |
| Gabe Vincent | 96% | 10.9<br><sub>-,-,-,-,3</sub> | 3.4<br><sub>-,-,-,-,0</sub> |  | 1.2<br><sub>-,-,-,-,0</sub> |  | 0.9<br><sub>-,-,-,-,0</sub> |  | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.4 | 0.1 | 0.4 | 5.5 |
| Sean Pedulla | 23% | 8.5<br><sub>-,-,-,-,-</sub> | 3.5<br><sub>-,-,-,-,-</sub> |  | 1.5<br><sub>-,-,-,-,-</sub> |  | 0.8<br><sub>-,-,-,-,-</sub> |  | 0.2<br><sub>-,-,-,-,-</sub> |  | 0.2 | 0.2 | 0.4 | 5.8 |
| Mason Plumlee | 38% | 7.8<br><sub>5,4,-,-,-</sub> | 2.0<br><sub>2,0,-,-,-</sub> |  | 2.6<br><sub>0,2,-,-,-</sub> |  | 0.7<br><sub>0,1,-,-,-</sub> |  | 0.0<br><sub>0,0,-,-,-</sub> |  | 0.3 | 0.3 | 0.5 | 5.2 |

</details>

<details><summary>GSW players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Brandin Podziemski | 98% | 32.4<br><sub>22,30,29,32,38</sub> | 18.1<br><sub>8,15,10,15,18</sub> | 16.5 · 17.5<br><sub>o 50% · u 50%</sub> | 5.0<br><sub>3,6,3,3,7</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 3.9<br><sub>0,3,4,2,2</sub> | 4.5<br><sub>o 40% · u 60%</sub> | 2.4<br><sub>2,3,0,0,4</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.1 | 0.3 | 1.7 | 27.1 |
| Yaxel Lendeborg | 98% | 31.7<br><sub>24,33,30,33,34</sub> | 20.2<br><sub>3,28,13,11,12</sub> | 20.5 · 20.5<br><sub>o 48% · u 52%</sub> | 7.1<br><sub>7,8,5,8,8</sub> | 7.5<br><sub>o 44% · u 56%</sub> | 4.0<br><sub>1,3,4,7,3</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 1.8<br><sub>0,2,0,1,1</sub> | 1.5<br><sub>o 56% · u 44%</sub> | 0.9 | 0.7 | 2.8 | 31.3 |
| Draymond Green | 97% | 25.3<br><sub>16,25,23,-,27</sub> | 6.2<br><sub>4,2,3,-,9</sub> | 5.5 · 5.5<br><sub>o 50% · u 50%</sub> | 4.9<br><sub>3,8,1,-,6</sub> | 4.5<br><sub>o 52% · u 48%</sub> | 5.8<br><sub>3,5,2,-,3</sub> | 4.5<br><sub>o 56% · u 44%</sub> | 0.7<br><sub>0,0,1,-,3</sub> | 0.5<br><sub>o 54% · u 46%</sub> | 1.0 | 0.6 | 2.2 | 16.9 |
| De'Anthony Melton | 99% | 23.1<br><sub>18,21,19,25,27</sub> | 10.6<br><sub>8,8,0,9,2</sub> | 10.5 · 11.5<br><sub>o 48% · u 52%</sub> | 3.5<br><sub>4,2,2,1,3</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 3.1<br><sub>3,1,2,5,7</sub> | 2.5<br><sub>o 58% · u 42%</sub> | 1.7<br><sub>2,2,0,1,0</sub> | 1.5<br><sub>o 57% · u 43%</sub> | 1.4 | 0.4 | 1.5 | 17.1 |
| Will Richard | 99% | 19.4<br><sub>30,23,27,27,17</sub> | 7.3<br><sub>7,11,20,15,3</sub> | 6.5 · 5.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>4,3,0,5,2</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.3<br><sub>1,1,3,0,2</sub> |  | 0.9<br><sub>1,2,1,1,1</sub> | 0.5<br><sub>o 62% · u 38%</sub> | 1.0 | 0.2 | 0.7 | 10.8 |
| Gui Santos | 96% | 19.1<br><sub>21,19,17,23,23</sub> | 8.9<br><sub>7,12,6,8,13</sub> | 7.5 · 8.5<br><sub>o 48% · u 52%</sub> | 3.8<br><sub>4,7,6,3,5</sub> | 4.5<br><sub>o 42% · u 58%</sub> | 2.3<br><sub>1,2,6,0,3</sub> | 1.5<br><sub>o 62% · u 38%</sub> | 0.8<br><sub>1,1,0,0,3</sub> |  | 0.7 | 0.3 | 1.2 | 14.9 |
| Charles Bassey | 98% | 18.7<br><sub>20,16,22,25,26</sub> | 9.7<br><sub>11,4,10,16,13</sub> | 10.5 · 10.5<br><sub>o 46% · u 54%</sub> | 7.4<br><sub>5,0,8,13,9</sub> | 7.5<br><sub>o 51% · u 49%</sub> | 1.0<br><sub>2,0,0,1,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.5 | 1.1 | 1.1 | 18.1 |
| Al Horford | 98% | 17.2<br><sub>10,14,-,17,18</sub> | 6.0<br><sub>0,0,-,3,7</sub> |  | 3.7<br><sub>3,5,-,2,3</sub> |  | 1.9<br><sub>1,0,-,2,2</sub> |  | 0.8<br><sub>0,0,-,0,1</sub> |  | 0.5 | 0.8 | 0.5 | 11.5 |
| Gary Payton II | 91% | 15.1<br><sub>13,8,16,24,13</sub> | 7.2<br><sub>2,2,8,2,8</sub> |  | 2.7<br><sub>2,0,8,1,1</sub> |  | 1.2<br><sub>0,0,2,1,0</sub> |  | 0.5<br><sub>0,0,2,0,0</sub> |  | 1.0 | 0.2 | 0.6 | 11.2 |
| Georges Niang | 98% | 14.5<br><sub>15,14,14,15,8</sub> | 6.8<br><sub>5,0,11,5,0</sub> |  | 2.1<br><sub>3,4,1,2,1</sub> |  | 1.0<br><sub>2,2,1,0,0</sub> |  | 1.0<br><sub>1,0,2,1,0</sub> |  | 0.3 | 0.1 | 0.6 | 9.8 |
| Brandon Williams | 88% | 13.3<br><sub>-,-,-,-,-</sub> | 8.6<br><sub>-,-,-,-,-</sub> |  | 1.7<br><sub>-,-,-,-,-</sub> |  | 2.3<br><sub>-,-,-,-,-</sub> |  | 0.4<br><sub>-,-,-,-,-</sub> |  | 0.6 | 0.2 | 1.1 | 12.6 |
| LJ Cryer | 88% | 13.0<br><sub>24,24,19,12,11</sub> | 6.8<br><sub>20,7,9,9,3</sub> |  | 1.0<br><sub>2,1,0,0,0</sub> |  | 1.6<br><sub>6,3,2,1,2</sub> |  | 1.1<br><sub>6,1,3,1,1</sub> |  | 0.3 | 0.1 | 0.5 | 9.3 |
| Graham Ike | 72% | 7.2<br><sub>13,8,15,4,-</sub> | 3.5<br><sub>5,3,2,5,-</sub> |  | 1.7<br><sub>2,5,2,0,-</sub> |  | 0.9<br><sub>3,1,2,0,-</sub> |  | 0.2<br><sub>1,0,0,0,-</sub> |  | 0.2 | 0.4 | 0.4 | 6.1 |
| Malevy Leons | 64% | 6.3<br><sub>14,6,7,4,-</sub> | 2.0<br><sub>5,2,2,0,-</sub> |  | 1.2<br><sub>1,1,1,2,-</sub> |  | 0.4<br><sub>0,0,0,1,-</sub> |  | 0.0<br><sub>1,0,0,0,-</sub> |  | 0.3 | 0.2 | 0.3 | 3.7 |

</details>


### SAS @ POR
Out: Vit Krejci (POR), Ja Morant (POR), Shaedon Sharpe (POR), Chris Youngblood (POR), De'Aaron Fox (SAS), Dylan Harper (SAS), Tobias Harris (SAS)

**Best player props (main lines)**

| Bet | Game | Book | Odds | Min odds | Fair (model) | Model | No-vig mkt | Blend | EV | EV model only | Stake |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Harrison Barnes PTS under 7.5 | SAS @ POR | pointsbetau | 2.10 | 2.01 | 1.71 | 58.5% | 47.9% | 49.8% | +4.6% | +22.8% | 1.0% |
| Donovan Clingan PTS over 10.5 (11+) | SAS @ POR | pointsbetau | 2.00 | 1.93 | 1.68 | 59.5% | 50.0% | 51.7% | +3.5% | +19.0% | 0.9% |
| Victor Wembanyama PTS under 30.5 | SAS @ POR | draftkings | 1.94 | 1.91 | 1.84 | 54.2% | 52.0% | 52.4% | +1.9% | +5.3% | 0.5% |
| Julian Champagnie PTS under 11.5 | SAS @ POR | sportsbet | 1.96 | 1.93 | 1.78 | 56.0% | 50.9% | 51.8% | +1.7% | +10.0% | 0.4% |
| Damian Lillard PTS under 20.5 | SAS @ POR | tab | 1.95 | 1.94 | 1.77 | 56.5% | 50.4% | 51.5% | +0.5% | +10.4% | 0.1% |

<details><summary>SAS players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Stephon Castle | 99% | 33.4<br><sub>35,31,33,29,37</sub> | 19.3<br><sub>20,10,21,19,28</sub> | 18.5 · 18.5<br><sub>o 51% · u 49%</sub> | 5.4<br><sub>4,2,6,3,8</sub> | 5.5<br><sub>o 47% · u 53%</sub> | 6.8<br><sub>9,7,12,6,11</sub> | 7.5<br><sub>o 50% · u 50%</sub> | 1.9<br><sub>0,2,2,5,4</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 1.2 | 0.3 | 3.3 | 31.4 |
| Devin Vassell | 99% | 33.3<br><sub>32,36,32,26,34</sub> | 14.0<br><sub>6,12,15,10,16</sub> | 12.5 · 13.5<br><sub>o 51% · u 49%</sub> | 4.4<br><sub>6,5,4,3,6</sub> | 3.5<br><sub>o 58% · u 42%</sub> | 3.0<br><sub>1,4,4,2,2</sub> | 2.5<br><sub>o 59% · u 41%</sub> | 1.9<br><sub>0,2,1,2,4</sub> | 1.5<br><sub>o 54% · u 46%</sub> | 1.4 | 0.5 | 1.1 | 21.4 |
| Victor Wembanyama | 99% | 32.6<br><sub>35,34,33,32,-</sub> | 30.6<br><sub>26,25,32,50,-</sub> | 30.5 · 29.5<br><sub>o 49% · u 51%</sub> | 12.1<br><sub>10,18,11,19,-</sub> | 12.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>6,4,3,1,-</sub> | 3.5<br><sub>o 49% · u 51%</sub> | 2.2<br><sub>4,1,2,5,-</sub> | 2.5<br><sub>o 40% · u 60%</sub> | 1.4 | 3.7 | 3.0 | 46.6 |
| Julian Champagnie | 99% | 29.3<br><sub>24,30,29,25,30</sub> | 11.4<br><sub>4,14,20,9,22</sub> | 11.5 · 11.5<br><sub>o 48% · u 52%</sub> | 4.8<br><sub>5,6,4,3,7</sub> | 5.5<br><sub>o 42% · u 58%</sub> | 1.8<br><sub>1,0,1,3,3</sub> |  | 2.0<br><sub>1,4,4,3,6</sub> | 2.5<br><sub>o 46% · u 54%</sub> | 1.0 | 0.6 | 0.8 | 17.9 |
| Keldon Johnson | 99% | 25.7<br><sub>29,15,27,23,26</sub> | 11.2<br><sub>11,4,10,10,12</sub> | 10.5 · 10.5<br><sub>o 48% · u 52%</sub> | 5.3<br><sub>10,2,5,4,4</sub> | 5.5<br><sub>o 45% · u 55%</sub> | 2.5<br><sub>2,1,3,4,5</sub> |  | 0.8<br><sub>1,0,0,2,0</sub> |  | 0.8 | 0.2 | 1.1 | 19.0 |
| Harrison Barnes | 96% | 21.1<br><sub>14,10,16,21,26</sub> | 7.2<br><sub>0,0,9,3,9</sub> | 7.5 · 7.5<br><sub>o 47% · u 53%</sub> | 2.4<br><sub>0,3,2,5,2</sub> | 2.5<br><sub>o 47% · u 53%</sub> | 1.3<br><sub>2,4,1,2,2</sub> |  | 1.0<br><sub>0,0,1,0,1</sub> | 1.5<br><sub>o 40% · u 60%</sub> | 0.4 | 0.2 | 0.7 | 10.9 |
| Luke Kornet | 99% | 20.5<br><sub>13,14,15,10,29</sub> | 5.7<br><sub>2,2,4,0,18</sub> |  | 5.8<br><sub>2,1,0,3,11</sub> |  | 1.6<br><sub>0,1,3,0,3</sub> |  | 0.0<br><sub>0,0,0,0,0</sub> |  | 0.6 | 0.9 | 0.6 | 13.1 |
| Jordan McLaughlin | 83% | 16.9<br><sub>19,-,11,18,14</sub> | 4.7<br><sub>10,-,0,0,6</sub> |  | 2.3<br><sub>1,-,1,3,2</sub> |  | 2.4<br><sub>2,-,5,2,0</sub> |  | 0.5<br><sub>2,-,0,0,0</sub> |  | 1.2 | 0.1 | 0.7 | 9.4 |
| Carter Bryant | 96% | 14.1<br><sub>5,2,13,20,12</sub> | 4.6<br><sub>0,0,3,8,0</sub> |  | 2.2<br><sub>1,0,1,3,3</sub> |  | 0.9<br><sub>0,0,0,0,2</sub> |  | 0.6<br><sub>0,0,1,2,0</sub> |  | 0.3 | 0.3 | 0.6 | 7.6 |
| Ja'Kobi Gillespie | 91% | 14.1<br><sub>-,-,-,-,15</sub> | 4.3<br><sub>-,-,-,-,3</sub> |  | 1.8<br><sub>-,-,-,-,2</sub> |  | 1.5<br><sub>-,-,-,-,4</sub> |  | 0.6<br><sub>-,-,-,-,1</sub> |  | 0.6 | 0.1 | 0.4 | 7.6 |
| Tarris Reed Jr. | 63% | 11.8<br><sub>-,-,-,6,15</sub> | 3.9<br><sub>-,-,-,0,7</sub> |  | 4.7<br><sub>-,-,-,4,7</sub> |  | 0.6<br><sub>-,-,-,0,1</sub> |  | 0.0<br><sub>-,-,-,0,0</sub> |  | 0.3 | 0.5 | 0.9 | 9.2 |
| Maliq Brown | 88% | 7.6<br><sub>-,-,-,-,1</sub> | 0.4<br><sub>-,-,-,-,0</sub> |  | 0.3<br><sub>-,-,-,-,0</sub> |  | 1.1<br><sub>-,-,-,-,0</sub> |  | 0.0<br><sub>-,-,-,-,0</sub> |  | 0.2 | 0.2 | 0.4 | 1.8 |
| David Jones Garcia | 64% | 7.5<br><sub>-,-,-,4,2</sub> | 2.7<br><sub>-,-,-,0,2</sub> |  | 1.2<br><sub>-,-,-,1,0</sub> |  | 1.0<br><sub>-,-,-,0,0</sub> |  | 0.1<br><sub>-,-,-,0,0</sub> |  | 0.5 | 0.1 | 0.4 | 4.9 |

</details>

<details><summary>POR players (confirmed only)</summary>

| Player | Plays | Min | PTS | PTS line DK · SB | REB | REB line DK | AST | AST line DK | 3PM | 3PM line DK | STL | BLK | TOV | PRA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Deni Avdija | 72% | 34.3<br><sub>30,-,-,36,30</sub> | 23.7<br><sub>27,-,-,20,31</sub> | 22.5 · 22.5<br><sub>o 50% · u 50%</sub> | 6.7<br><sub>8,-,-,9,3</sub> | 5.5<br><sub>o 57% · u 43%</sub> | 6.3<br><sub>4,-,-,5,7</sub> | 5.5<br><sub>o 56% · u 44%</sub> | 2.0<br><sub>3,-,-,2,5</sub> | 1.5<br><sub>o 55% · u 45%</sub> | 0.9 | 0.5 | 3.2 | 36.6 |
| Damian Lillard | 99% | 32.9<br><sub>24,31,35,33,29</sub> | 20.2<br><sub>9,25,33,15,18</sub> | 20.5 · 20.5<br><sub>o 48% · u 52%</sub> | 4.0<br><sub>2,3,6,3,3</sub> | 3.5<br><sub>o 44% · u 56%</sub> | 4.4<br><sub>4,5,0,3,5</sub> | 3.5<br><sub>o 57% · u 43%</sub> | 2.7<br><sub>2,5,5,1,1</sub> | 3.5<br><sub>o 39% · u 61%</sub> | 0.8 | 0.2 | 2.1 | 28.6 |
| Toumani Camara | 99% | 32.7<br><sub>26,33,37,35,29</sub> | 11.8<br><sub>3,10,18,6,5</sub> | 10.5 · 10.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>0,8,6,5,5</sub> | 4.5<br><sub>o 46% · u 54%</sub> | 1.8<br><sub>0,1,4,0,3</sub> |  | 2.0<br><sub>0,2,4,1,1</sub> | 2.5<br><sub>o 39% · u 61%</sub> | 1.0 | 0.5 | 1.1 | 18.3 |
| Jrue Holiday | 99% | 29.7<br><sub>25,31,31,31,28</sub> | 14.5<br><sub>10,23,22,13,18</sub> | 12.5 · 12.5<br><sub>o 51% · u 49%</sub> | 4.3<br><sub>4,5,2,9,2</sub> | 3.5<br><sub>o 51% · u 49%</sub> | 4.7<br><sub>3,6,7,7,5</sub> | 4.5<br><sub>o 50% · u 50%</sub> | 2.2<br><sub>2,5,2,1,4</sub> | 2.5<br><sub>o 38% · u 62%</sub> | 1.0 | 0.2 | 2.1 | 23.5 |
| Donovan Clingan | 99% | 28.8<br><sub>22,32,26,31,29</sub> | 12.6<br><sub>10,12,7,22,15</sub> | 10.5 · 10.5<br><sub>o 52% · u 48%</sub> | 12.0<br><sub>10,12,13,13,18</sub> | 10.5<br><sub>o 54% · u 46%</sub> | 2.4<br><sub>1,5,2,4,5</sub> |  | 1.2<br><sub>0,0,0,3,1</sub> |  | 0.7 | 1.7 | 1.1 | 27.0 |
| Scoot Henderson | 99% | 25.4<br><sub>23,21,35,23,26</sub> | 11.9<br><sub>10,9,27,3,17</sub> | 10.5 · 10.5<br><sub>o 50% · u 50%</sub> | 2.5<br><sub>1,1,7,1,3</sub> | 2.5<br><sub>o 41% · u 59%</sub> | 2.4<br><sub>0,1,3,1,3</sub> |  | 1.4<br><sub>0,0,5,0,3</sub> | 1.5<br><sub>o 41% · u 59%</sub> | 0.7 | 0.2 | 1.9 | 16.8 |
| Sidy Cissoko | 98% | 24.9<br><sub>28,32,31,23,24</sub> | 7.3<br><sub>5,6,13,11,5</sub> | 6.5 · 6.5<br><sub>o 49% · u 51%</sub> | 3.5<br><sub>4,5,5,2,4</sub> | 2.5<br><sub>o 60% · u 40%</sub> | 1.6<br><sub>3,1,3,1,0</sub> |  | 1.0<br><sub>1,2,1,3,1</sub> |  | 0.8 | 0.3 | 0.9 | 12.4 |
| Robert Williams III | 98% | 17.0<br><sub>15,16,-,17,16</sub> | 6.3<br><sub>2,6,-,4,6</sub> | 5.5 · –<br><sub>o 49% · u 51%</sub> | 6.5<br><sub>5,8,-,3,6</sub> |  | 1.1<br><sub>2,4,-,0,1</sub> |  | 0.1<br><sub>0,0,-,0,0</sub> |  | 0.6 | 1.1 | 0.7 | 13.9 |
| Jayson Kent | 88% | 12.1<br><sub>11,27,17,3,14</sub> | 4.0<br><sub>8,8,2,0,9</sub> |  | 1.4<br><sub>0,3,1,1,2</sub> |  | 0.6<br><sub>0,0,2,0,1</sub> |  | 0.5<br><sub>2,2,0,0,3</sub> |  | 0.5 | 0.1 | 0.5 | 6.0 |
| Branden Carlson | 91% | 8.9<br><sub>14,14,10,9,6</sub> | 2.5<br><sub>5,6,0,2,0</sub> |  | 2.2<br><sub>6,1,1,1,3</sub> |  | 0.3<br><sub>1,0,0,0,0</sub> |  | 0.2<br><sub>1,0,0,0,0</sub> |  | 0.3 | 0.4 | 0.4 | 5.0 |
| Yang Hansen | 58% | 7.2<br><sub>7,-,12,-,3</sub> | 2.7<br><sub>0,-,2,-,2</sub> |  | 1.8<br><sub>1,-,1,-,0</sub> |  | 0.5<br><sub>3,-,1,-,1</sub> |  | 0.1<br><sub>0,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.5 | 5.1 |
| Micah Potter | 58% | 7.0<br><sub>7,1,-,-,3</sub> | 3.1<br><sub>2,0,-,-,0</sub> |  | 2.0<br><sub>4,0,-,-,0</sub> |  | 0.4<br><sub>1,0,-,-,0</sub> |  | 0.3<br><sub>0,0,-,-,0</sub> |  | 0.2 | 0.1 | 0.3 | 5.5 |
| John Tonje | 52% | 6.6<br><sub>7,-,6,-,3</sub> | 2.7<br><sub>7,-,0,-,2</sub> |  | 1.6<br><sub>4,-,3,-,0</sub> |  | 0.7<br><sub>3,-,0,-,1</sub> |  | 0.2<br><sub>1,-,0,-,0</sub> |  | 0.1 | 0.2 | 0.3 | 5.0 |

</details>


---
_Model projections, not advice. Edges are against the best price found at run time. Full data: `output/2026-11-25/`._
